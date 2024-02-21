import reflex as rx
from portafolio.views.header import header

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),                      
        )
    )


app = rx.App()
app.add_page(index)
