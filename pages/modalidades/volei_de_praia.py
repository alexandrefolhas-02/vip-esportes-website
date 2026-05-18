# pages/modalidades/volei_de_praia.py
import antigravity as ag
from components.navigation.navbar import navbar
from components.navigation.footer import footer
from styles.theme import VIPColors

def volei_de_praia_page() -> ag.Component:
    return ag.page(
        title="Vôlei de Praia | Metodologia Paula Pequeno | VIP Esportes",
        children=[
            navbar(),
            
            ag.box(
                background_image="linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/assets/images/volei-hero.jpg')",
                background_size="cover",
                padding="6rem 2rem",
                text_align="center",
                children=[
                    ag.heading("Vôlei de Praia", size="3xl", color=VIPColors.text_light),
                    ag.text("Aprenda com quem fez história no desporto mundial.", color=VIPColors.text_light, font_size="1.5rem", margin_top="1rem")
                ]
            ),
            
            # Secção Metodologia Paula Pequeno com Vídeo da Campanha
            ag.box(
                padding="4rem 5%",
                display="flex",
                flex_direction="row", # Lado a lado em ecrãs grandes
                align_items="center",
                gap="3rem",
                children=[
                    # Coluna do Texto
                    ag.vstack(
                        ag.heading("Metodologia Paula Pequeno", color=VIPColors.secondary, size="2xl"),
                        ag.text(
                            "O nosso programa de Vôlei de Praia é construído sobre a experiência e a técnica de uma bicampeã olímpica. "
                            "Desenvolvemos um método que respeita o seu tempo de aprendizagem, elevando o seu condicionamento físico "
                            "e a sua leitura de jogo de forma contínua e estimulante.",
                            font_size="1.1rem",
                            line_height="1.6",
                            margin_top="1rem"
                        ),
                        ag.button("Agendar Aula de Vôlei", background_color=VIPColors.primary, color=VIPColors.text_light, margin_top="2rem"),
                        align_items="flex-start",
                        flex="1"
                    ),
                    
                    # Coluna do Vídeo Promocional da Campanha
                    ag.box(
                        flex="1",
                        border_radius="15px",
                        overflow="hidden",
                        box_shadow="0 10px 30px rgba(0,0,0,0.15)",
                        children=[
                            ag.video(
                                src="/assets/videos/campanha-paula-pequeno.mp4",
                                poster="/assets/images/thumbnail-video-paula.jpg",
                                controls=True,
                                width="100%",
                                auto_play=True,
                                muted=True,
                                loop=True
                            )
                        ]
                    )
                ]
            ),
            
            footer()
        ]
    )