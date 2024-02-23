import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size
from portafolio.components.media import media

def header () -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value),
        rx.vstack(
           heading("Nombre", True),
           heading("Habilidad principal"), 
           rx.text(
               rx.icon("map-pin"),
               "Localizacion",
               display="inherit"
           ),
           media(),
           spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value
    )