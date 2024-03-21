import reflex as rx
from portafolio import data
from portafolio.views.header import header
from portafolio.views.footer import footer
from portafolio.views.about import about
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack
from portafolio.views.extra import extra
from portafolio.styles.styles import MAX_WIDTH, EmSize, Size, BASE_STYLE, STYLESHEETS

Data = data.data

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(Data),
            about(Data.about),
            rx.divider(),
            tech_stack(Data.technologies),
            info("Experiencia", Data.experience),
            info("Proyectos", Data.projects),
            info("Formacion", Data.training),
            extra(Data.extras),
            rx.divider(),
            footer(Data.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"                  
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accentColor="sky",
        radius="full"
    )
    
)
app.add_page(index)
