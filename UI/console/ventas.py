from textual.app import App, ComposeResult
from textual.widgets import Input
from textual_autocomplete import AutoComplete, Dropdown, DropdownItem
from db.model import *

ITEMS = [
    DropdownItem("Amox"),
    DropdownItem("Edinburgh"),
    DropdownItem("Aberdeen"),
    DropdownItem("Dundee"),
]

class Example01(App):

    CSS = """
    Dropdown { max-width: 32; }
    """

    def compose(self) -> ComposeResult:
        yield AutoComplete(Input(placeholder="type away..."), Dropdown(items=ITEMS))


app = Example01()

if __name__ == "__main__":
    app.run()