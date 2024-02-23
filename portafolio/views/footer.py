import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import Size
from portafolio.components.media import media

def footer () -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(),
        spacing=Size.SMALL.value
    )