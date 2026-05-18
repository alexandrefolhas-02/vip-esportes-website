# pages/index.py
import antigravity as ag
from components.navigation.navbar import navbar
from components.sections.hero_banner import hero_banner
from components.navigation.footer import footer
from styles.theme import VIPColors

def homepage() -> ag.Component:
    return ag.page(
        title="VIP Esportes | Escola de Beach Tennis, Vôlei e Futevôlei",
        children=[
            # 1. Menu de Navegação Superior
            navbar(),
            
            # 2. Painel de Impacto Inicial
            hero_banner(),
            
            # 3. Secção: Destaque da Metodologia
            ag.box(
                padding="4rem 2rem",
                background_color=VIPColors.background,
                text_align="center",
                children=[
                    ag.heading("Metodologia de Excelência", color=VIPColors.secondary, size="xl"),
                    ag.text(
                        "Desde o Beach Tennis ao desenvolvimento técnico de Voleibol com a assinatura e experiência de uma bicampeã olímpica como a Paula Pequeno. Estrutura de ponta para a sua evolução no desporto.",
                        margin_top="1rem",
                        max_width="700px",
                        margin_x="auto"
                    )
                ]
            ),
            
            # 4. Rodapé
            footer()
        ]
    )