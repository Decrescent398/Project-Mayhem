import reflex as rx

config = rx.Config(
    app_name="project_mayhem",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    api_url="http://projectmayhem.github.io:8000",
)