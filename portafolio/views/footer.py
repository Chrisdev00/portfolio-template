import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size
from portafolio.components.media import media
from portafolio.data import Media

def footer (data: Media) -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(data),
        spacing=Size.SMALL.value
    )