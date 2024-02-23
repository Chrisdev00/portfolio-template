import reflex as rx
from portafolio.views.header import header
from portafolio.views.footer import footer
from portafolio.views.about import about
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack
from portafolio.views.extra import extra
from portafolio.styles.styles import MAX_WIDTH, EmSize, Size



def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            info("Experiencia"),
            info("Proyectos"),
            info("Formacion"),
            extra(),
            rx.divider(),
            footer(),
            spacing=Size.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"                  
        )
    )


app = rx.App()
app.add_page(index)
