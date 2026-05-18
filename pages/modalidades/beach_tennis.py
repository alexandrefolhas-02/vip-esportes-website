# pages/modalidades/beach_tennis.py
import antigravity as ag
from components.navigation.navbar import navbar
from components.navigation.footer import footer
from styles.theme import VIPColors

def beach_tennis_page() -> ag.Component:
    return ag.page(
        title="Beach Tennis | VIP Esportes",
        children=[
            navbar(),
            
            # Hero Banner Específico da Modalidade
            ag.box(
                background_image="linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('/assets/images/beach-tennis-hero.jpg')",
                background_size="cover",
                padding="6rem 2rem",
                text_align="center",
                children=[
                    ag.heading("Beach Tennis", size="3xl", color=VIPColors.text_light),
                    ag.text("Dinâmico, divertido e para todas as idades.", color=VIPColors.text_light, font_size="1.5rem", margin_top="1rem")
                ]
            ),
            
            # Níveis de Turma
            ag.box(
                padding="4rem 5%",
                children=[
                    ag.heading("Turmas por Nível Técnico", color=VIPColors.secondary, margin_bottom="2rem", text_align="center"),
                    ag.grid(
                        columns="repeat(3, 1fr)", gap="2rem",
                        children=[
                            ag.card(title="Iniciante", description="Foco em controlo de bola, posicionamento e golpes básicos. Ideal para quem está a começar."),
                            ag.card(title="Intermediário", description="Foco em tática de jogo, saque, movimentação rápida e efeitos (spin/slice)."),
                            ag.card(title="Avançado", description="Foco em estratégia, jogadas ensaiadas, ganho de potência e ritmo intenso.")
                        ]
                    )
                ]
            ),
            
            # Destaque: Campeonato do Mundo
            ag.box(
                background_color=VIPColors.primary,
                padding="3rem 5%",
                color=VIPColors.text_light,
                border_radius="10px",
                margin="2rem 5%",
                text_align="center",
                children=[
                    ag.heading("🏆 ITF BT 400 - Copacabana (Abril 2026)", size="xl", margin_bottom="1rem"),
                    ag.text("A VIP Esportes faz parte do campeonato do mundo! Prepare-se para viver a emoção do Beach Tennis no coração do Rio de Janeiro."),
                    ag.button("Saber Mais sobre o Evento", variant="outline", border_color=VIPColors.text_light, color=VIPColors.text_light, margin_top="1.5rem")
                ]
            ),
            
            footer()
        ]
    )