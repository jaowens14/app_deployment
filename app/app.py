import flet
import os
from flet import IconButton, Page, Row, TextField, icons
import controls

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 5
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 5
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

flet.app(target=main, view=flet.WEB_BROWSER, port=8502)
