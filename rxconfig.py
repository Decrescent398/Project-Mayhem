import reflex as rx

config = rx.Config(
    app_name="project_mayhem",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)