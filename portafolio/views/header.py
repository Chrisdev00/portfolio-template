import reflex as rx
from portafolio.components.heading import heading

def header () -> rx.Component:
    return rx.hstack(
        rx.avatar(),
        rx.vstack(
           heading("Nombre", True),
           heading("Habilidad principal"), 
           rx.text(
               rx.icon("map-pin"),
               "Localizacion",
               display="inherit"
           ) 
        )
    )