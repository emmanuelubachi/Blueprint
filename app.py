from shiny import App, Inputs, Outputs, Session, render, ui

from pathlib import Path

from modules import layout

page_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css", href="style/style.css"),
    ui.tags.link(
        rel="stylesheet",
        type="text/css",
        href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.7.0/flowbite.min.css",
    ),
    ui.tags.script(src="https://cdn.tailwindcss.com"),
)

body_scripts = ui.tags.head(
    ui.tags.script(
        src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.7.0/flowbite.min.js"
    ),
    ui.tags.script(src="js/index.js"),
)

app_ui = ui.page_fluid(
    ui.head_content(page_dependencies),
    layout(),
    body_scripts,
    title="Shiny for Python Template",
    lang="en",
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def slider_val():
        return f"{input.num()}"


www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
