import flet
import os
from flet import IconButton, Page, Row, TextField, icons
DEFAULT_FLET_PORT = 80

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )


flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))

flet.app(target=main, view=flet.WEB_BROWSER, port=flet_port)
