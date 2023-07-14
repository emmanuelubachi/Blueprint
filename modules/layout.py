from shiny import ui
from components import *

tit = "Noteworthy technology acquisitions 2021"
desc = "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."

tit2 = "2 Noteworthy technology acquisitions 2021"
desc2 = "2 Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."

tit3 = "3 Noteworthy technology acquisitions 2021"
desc3 = "3 Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."


def page_layout():
    page_layout = ui.tags.main(
        ui.h1("Hello", class_="text-3xl font-bold underline"),
        ui.input_slider("num", "Number:", min=10, max=100, value=30),
        ui.div(
            {"class": "bold-output;"},
            ui.output_text("slider_val"),
        ),
        ui.row(
            ui.column(4, card(tit, desc)),
            ui.column(4, card_link(tit2, desc2)),
            ui.column(4, card(tit3, desc3)),
            align="center",
        ),
        ui.row(
            ui.column(4, flex_card()),
            ui.column(4, help_card()),
            ui.column(4, image_card()),
            align="center",
        ),
    )
    return page_layout
