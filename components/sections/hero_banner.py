# components/sections/hero_banner.py
import antigravity as ag
from styles.theme import VIPColors

def hero_banner() -> ag.Component:
    return ag.box(
        # Fundo do Banner com imagem fotográfica tratada e overlay escuro
        background_image="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/assets/images/hero-praia-edit.jpg')",
        background_size="cover",
        background_position="center",
        height="90vh",
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
        text_align="center",
        padding="2rem",
        
        # Conteúdo sobre o vídeo/imagem
        children=[
            ag.heading(
                "Muito mais que esporte. Seu novo estilo de vida na praia.",
                font_size="4rem",
                color=VIPColors.text_light,
                margin_bottom="1rem",
                max_width="800px"
            ),
            ag.text(
                "Escola de excelência em Beach Tennis, Vôlei de Praia e Futevôlei no Rio de Janeiro.",
                font_size="1.5rem",
                color=VIPColors.text_light,
                margin_bottom="2.5rem",
                max_width="600px"
            ),
            ag.hstack(
                ag.button(
                    "Agendar Aula Experimental Gratuita",
                    background_color=VIPColors.primary,
                    color=VIPColors.text_light,
                    font_size="1.2rem",
                    padding="1rem 2rem",
                    border_radius="30px",
                    _hover={"transform": "scale(1.05)", "transition": "0.3s"}
                ),
                ag.button(
                    "Conhecer as Unidades",
                    background_color="transparent",
                    color=VIPColors.text_light,
                    border=f"2px solid {VIPColors.text_light}",
                    font_size="1.2rem",
                    padding="1rem 2rem",
                    border_radius="30px",
                    _hover={"background_color": VIPColors.text_light, "color": VIPColors.secondary, "transition": "0.3s"}
                ),
                spacing="1.5rem"
            )
        ]
    )