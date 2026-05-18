# components/navigation/footer.py
import antigravity as ag
from styles.theme import VIPColors

def footer() -> ag.Component:
    return ag.footer(
        ag.vstack(
            # Secção principal do rodapé com colunas
            ag.hstack(
                # Coluna 1: Sobre e Contactos
                ag.vstack(
                    ag.image(src="/assets/branding/VIP-COLOR.png", height="40px", alt="Logo VIP Esportes"),
                    ag.text("Transformando a sua rotina na areia.", color=VIPColors.text_light, margin_top="1rem"),
                    ag.text("📞 (XX) XXXXX-XXXX", color=VIPColors.text_light),
                    ag.text("✉️ contato@vipesportes.com.br", color=VIPColors.text_light),
                    align_items="flex-start"
                ),
                
                # Coluna 2: Navegação Rápida
                ag.vstack(
                    ag.heading("Navegação", size="md", color=VIPColors.highlight),
                    ag.link("A VIP", href="/a-vip", color=VIPColors.text_light),
                    ag.link("Modalidades", href="/modalidades", color=VIPColors.text_light),
                    ag.link("Unidades", href="/unidades", color=VIPColors.text_light),
                    align_items="flex-start"
                ),

                # Coluna 3: Clube de Vantagens
                ag.vstack(
                    ag.heading("Vantagem Exclusiva", size="md", color=VIPColors.highlight),
                    ag.text(
                        "Os nossos alunos têm acesso ao Meu Clube Esportes — O maior Clube de vantagens e benefícios desportivos do Brasil.",
                        color=VIPColors.text_light,
                        max_width="250px"
                    ),
                    ag.button("Aceder ao Clube", variant="outline", color=VIPColors.highlight, border_color=VIPColors.highlight),
                    align_items="flex-start"
                ),
                
                justify_content="space-between",
                width="100%",
                padding_bottom="2rem",
                border_bottom=f"1px solid {VIPColors.secondary}"
            ),
            
            # Direitos de Autor
            ag.text(
                "© 2026 VIP Esportes. Todos os direitos reservados.", 
                color=VIPColors.text_light, 
                font_size="0.9rem",
                margin_top="1.5rem"
            ),
            
            align_items="center",
            width="100%"
        ),
        
        background_color=VIPColors.text_dark,
        padding="3rem 2rem 1.5rem",
        color=VIPColors.text_light
    )