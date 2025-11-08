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
        rx.box(
            rx.text(
                "PROJECT MAYHEM",
                style={
                    "color": "#ffffff",
                    "font_size": "clamp(2.25rem, 4vw, 5.5rem)",
                    "font_weight": "9000",
                    "font_family": "Audiowide",
                    "letter_spacing": "0.5em",
                    "text_shadow": "0 0 25px rgba(0,255,255,0.9), 0 0 50px rgba(0,255,255,0.5)",
                    "animation": "flicker 3s infinite",
                    "text_align": "center",
                },
            ),
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
        ),
        rx.box(
            rx.flex(
                rx.link(
                    rx.button(
                        "RSVP",
                        style = {
                            "border": "1px solid rgba(150,255,255,0.18)",
                            "background": "linear-gradient(135deg, rgba(180, 220, 230, 0.4) 0%,   /* light bluish */rgba(160, 200, 180, 0.3) 100%  /* soft greenish */)",
                            "color": "#bdf7ff",
                            "font_weight": "300",
                            "text_transform": "uppercase",
                            "letter_spacing": "0.08em",
                            "padding": "0.8rem 2.2rem",
                            "border_radius": "0",
                            "box_shadow": "0 0 6px rgba(100,255,255,0.1)",
                        },
                    ),
                    href="https://forms.fillout.com/t/reCt3Bv43eus",
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        "Slack",
                        style = {
                            "border": "1px solid rgba(150,255,255,0.18)",
                            "background": "linear-gradient(135deg, rgba(180, 220, 230, 0.4) 0%,   /* light bluish */rgba(160, 200, 180, 0.3) 100%  /* soft greenish */)",
                            "color": "#bdf7ff",
                            "font_weight": "300",
                            "text_transform": "uppercase",
                            "letter_spacing": "0.08em",
                            "padding": "0.8rem 2.2rem",
                            "border_radius": "0",
                            "box_shadow": "0 0 6px rgba(100,255,255,0.1)",
                        }, 
                    ),
                    href="https://hackclub.slack.com/archives/C09RHUBJ6SJ",
                    is_external="True",
                ),
                spacing="9",
                width="100%",
            ),
            position="absolute",
            top="75%",
            left="50%",
            transform="translate(-50%, -50%)",
            style={
                "justify_content": "center",
                "align_items": "center",
                "gap": "2rem",
                "margin_top": "2rem",
                "flex_wrap": "wrap",
            },
        ),
        rx.box(
            rx.text(
                "Ship borderline insane projects, get prizes that make you question why they exist",
                style={
                    "color": "#ffffff",
                    "font_size": "clamp(0.75rem, 1.5vw, 1rem)",
                    "font_weight": "750",
                    "font_family": "Audiowide",
                    "letter_spacing": "0.1em",
                    "animation": "flicker 3s infinite",
                    "text_align": "center",
                },
            ),
            position="absolute",
            top="90%",
            left="50%",
            transform="translate(-50%, -50%)",
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