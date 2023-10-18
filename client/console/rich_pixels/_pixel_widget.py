from rich_pixels import Pixels
from textual.app import App, ComposeResult
from textual.widget import Widget
from rich.panel import Panel

class MyWidget(Widget):
    def render(self):
        my_renderable = Panel("press q to quit")
        return my_renderable

class MyApp(App):
    def compose(self) -> ComposeResult:
        """Called to add widgets to the app."""
        yield MyWidget()

MyApp().run()

