import random
from typing import Iterable
from rich.align import Align
from rich.box import DOUBLE
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import App
from textual.scroll_view import ScrollView
from textual.layouts import vertical
from textual._layout import WidgetPlacement
from textual.geometry import Size
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.geometry import Spacing, Offset
from textual.widgets import DataTable, Markdown, Header, Footer

class Modal(Widget):
    content: Reactive[RenderableType] = Reactive('')
    title: Reactive[str | None] = Reactive(None)
    width: Reactive[int | None] = Reactive(None)
    height: Reactive[int | None] = Reactive(None)
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    style: Reactive[str] = Reactive("")

    def __init__(
        self, *,
        content: RenderableType = 'Default Modal Content',
        title: str | None = None,
        width: int | None = None,
        height: int | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(name=name)
        self.content = content
        self.title = title
        self.width = width
        self.height = height
        self.view = None

    def render(self):
        console_size = self.console.options.size
        if self.width:
            width = min(self.width, self.console.options.max_width)
        else:
            width = int(.8 * console_size.width)

        if self.height:
            height = min(self.height, self.console.options.max_height)
        else:
            height = int(.8 * console_size.height)

        offset_y = int((console_size.height - height) / 2)
        offset_x = int((console_size.width - width) / 2)

        if self.view:
            gutter = (offset_y, 0, 0, offset_x)
            self.view.layout.gutter = Spacing.unpack(gutter)
            self.view.update(self)
        self.border_style = 'green' if self.mouse_over else 'blue'
        self.border = 'bold' if self.has_focus else 'round'

        centered = Align.center(
            self.content,
            width=width,
            height=height,
            vertical='top',
        )
        return centered

    async def on_focus(self, event: events.Focus) -> None:
        self.has_focus = True

    async def on_blur(self, event: events.Blur) -> None:
        self.has_focus = False

    async def on_enter(self, event: events.Enter) -> None:
        self.mouse_over = True

    async def on_leave(self, event: events.Leave) -> None:
        self.mouse_over = False


class ModalView(Modal, layout=vertical):
    def __init__(
        self,
        modal: Modal,
        *,
        z: int = 0,
        auto_width: bool = False,
        name: str | None = None
    ) -> None:
        layout = vertical(auto_width=auto_width, z=z)
        self.modal = self.widget = modal
        layout.add(self.modal)
        super(Modal, self).__init__(name=name, layout=layout)
        self.modal.view = self

    def set_content(self, value):
        self.modal.content = value

    def get_arrangement(self, size: Size, scroll: Offset) -> Iterable[WidgetPlacement]:
        # Ignoring cache - would be better to figure out how to reliably load uncached when gutter has changed...
        # Current problem seems to be gutter changes mid render of widget, but I'm not 100% sure on this
        return list(self.layout.arrange(size, scroll))

    def set_layout_size(self):
        """Set layout_size based on console.options.size"""
        width = self.modal.width or int(self.console.options.size.width * .8)
        render_width = int(((self.console.options.size.width - width) / 2) + width)
        self.layout_size = render_width

    async def on_mount(self):
        self.set_layout_size()

    async def on_resize(self, event: events.Resize) -> None:
        self.set_layout_size()
        await super().on_resize(event)
        
class ExampleApp(App):
    modal_content_index: int = 1

    async def on_load(self, event: events.Load) -> None:
        await self.bind("b", "view.toggle('sidebar')", "Toggle Sidebar")
        # Note 'm' hides and show's the modal
        await self.bind("m", "view.toggle('modal')", "Toggle Modal")
        # Note 'c' cycles content in the modal - was handy
        await self.bind("c", "cycle_modal", "Cycle Modal Content")
        await self.bind("q", "quit", "Quit")

    async def action_cycle_modal(self):
        """Just showing some different content"""
        self.modal_content_index += 1
        match self.modal_content_index:
            case 2:
                content = Text.from_markup('[bold red]Stylized text[/] with [green on white]R$CH[/]')
            case 3:
                content = DataTable('Entry', 'Album')
                content.add_row('Pulk/Pull Revolving Doors', 'Amnesiac')
                content.add_row('Paranoid Android', 'OK Computer')
            case 4:
                content = Markdown(
                    "# Foobar\nFoobar is a Python library for dealing with word pluralization.\n\n## Installation\n"
                    "Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.\n\n```bash\n"
                )
            case _:
                self.modal_content_index = 1
                content = 'Just a string.'

        self.modal.set_content(content)

    async def on_mount(self, event: events.Mount) -> None:
        """ Everything up top is just app setup, not important to the floating Modal bit - left it in as it's how I tested while dev'ing and makes a decently dense backdrop"""
        body = ScrollView(
            '\n'.join('Fusce rhoncus bibendum est, mattis porta dolor imperdiet eget' for _ in range(50)), gutter=1,
        )
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        menu = DataTable.grid()
        for item in random.choices(dir(__builtins__), k=20):
            menu.add_row(f'◉ {item}')
        await self.view.dock(ScrollView(menu), edge="left", size=30, name="sidebar")
        await self.view.dock(body, edge="right")


        """ !!! This is the important bit - Create the ModalView and dock it """
        self.modal = ModalView(
            Modal(content='Just some modal content', width=35, height=15, title='Modal Title'),
            z=1,
        )
        await self.view.dock(self.modal, edge='left', z=1, name='modal')


if __name__ == '__main__':
    ExampleApp.run(title="Modal Example App", log='do_some_modal.log')