import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size
from portafolio.components.media import media

def about (description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mi"),
        rx.text(description)
    )