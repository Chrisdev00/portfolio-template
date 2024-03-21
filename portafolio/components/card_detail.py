import reflex as rx
from portafolio.styles.styles import Size, IMAGE_HEIGHT, EmSize
from portafolio.data import Extra

def card_detail (extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title),    
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color_scheme="gray"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True
        
    )