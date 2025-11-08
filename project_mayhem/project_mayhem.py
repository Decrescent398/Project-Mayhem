import reflex as rx
from rxconfig import config

def index() -> rx.Component:
    return rx.box(
        rx.video(
            src="/project_mayhem_tv.mp4",
            playing=True,
            loop=True,
            controls=False,
            muted=True,
            width="100%",
            height="100%",
            object_fit="cover",
            display="block",
        ),
        position="fixed",
        inset="0",
        display="flex",
        align_items="center",
        justify_content="center",
        background_color="black",
        overflow="hidden",
    )

app = rx.App(
    style={
        "html, body, #root": {
            "height": "100%",
            "width": "100%",
            "margin": "0",
            "padding": "0",
            "background_color": "black",
        },
        "::selection": {"background_color": "#4e8cff"},
    },
    theme=rx.theme(
        breakpoints=["520px", "768px", "1024px", "1280px", "1640px"],
    ),
)

app.add_page(index)