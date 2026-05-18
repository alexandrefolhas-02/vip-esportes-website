# pages/unidades.py
import antigravity as ag
from components.navigation.navbar import navbar
from components.navigation.footer import footer
from components.cards.unit_card import unit_card
from styles.theme import VIPColors

def unidades_page() -> ag.Component:
    return ag.page(
        title="Unidades e Horários | VIP Esportes",
        children=[
            navbar(),
            
            # Cabeçalho da Página
            ag.box(
                padding="4rem 2rem",
                background_color=VIPColors.background,
                text_align="center",
                children=[
                    ag.heading("Onde treinar com a VIP", size="2xl", color=VIPColors.secondary),
                    ag.text(
                        "Encontre a unidade ideal para si. Estamos presentes em praias, condomínios, colégios e clubes parceiros por todo o Rio de Janeiro.",
                        margin_top="1rem",
                        font_size="1.2rem",
                        color=VIPColors.text_dark,
                        max_width="800px",
                        margin_x="auto"
                    )
                ]
            ),
            
            # Contentor Principal com as Categorias
            ag.box(
                padding="2rem 5%",
                children=[
                    
                    # Categoria: Praias e Centros de Treinamento
                    ag.heading("⛱️ Praias & Centros de Treinamento", size="xl", color=VIPColors.primary, margin_top="2rem", margin_bottom="1.5rem"),
                    ag.grid(
                        columns="repeat(auto-fit, minmax(300px, 1fr))", gap="2rem",
                        children=[
                            unit_card("Unidade CDesign", "Praia do Recreio", "Beach Tennis", "Pratique Beach Tennis na energia única da Praia do Recreio, com uma estrutura de topo."),
                            unit_card("Unidade Guaratiba", "VIP Esportes Guaratiba", "Vôlei de Praia", "O nosso centro de treino estruturado para a prática de Vôlei de Praia com foco na técnica.")
                        ]
                    ),
                    
                    # Categoria: Condomínios
                    ag.heading("🏡 Unidades em Condomínios", size="xl", color=VIPColors.primary, margin_top="4rem", margin_bottom="1.5rem"),
                    ag.grid(
                        columns="repeat(auto-fit, minmax(300px, 1fr))", gap="2rem",
                        children=[
                            unit_card("Unidade Tennis Route", "Cond. Interlagos de Itaúna", "Beach Tennis", "Toda a excelência da VIP Esportes na comodidade e segurança do Condomínio Interlagos de Itaúna."),
                            unit_card("Unidade Nova Ipanema", "Cond. Nova Ipanema", "Beach Tennis e Vôlei de Praia", "Um ponto completo na Barra da Tijuca, unindo a febre do Beach Tennis com a tradição do Vôlei de Praia.")
                        ]
                    ),
                    
                    # Categoria: Clubes e Competição
                    ag.heading("⚓ Clubes & Performance", size="xl", color=VIPColors.primary, margin_top="4rem", margin_bottom="1.5rem"),
                    ag.grid(
                        columns="repeat(auto-fit, minmax(300px, 1fr))", gap="2rem",
                        children=[
                            unit_card("Unidade Clube Aquidabã", "Iate Clube Aquidabã", "Vôlei", "A tradição e estrutura de um clube náutico unidas à metodologia de vôlei da VIP Esportes."),
                            unit_card("Unidade Clube de Aeronáutica", "Clube de Aeronáutica", "Equipa de Competição", "O coração do alto rendimento da VIP. Espaço dedicado ao treino focado e preparação para torneios oficiais.", cta_text="Falar com Coordenador")
                        ]
                    ),
                    
                    # Categoria: Colégios
                    ag.heading("🏫 VIP Colégios", size="xl", color=VIPColors.primary, margin_top="4rem", margin_bottom="1.5rem"),
                    ag.text("Metodologia integrada ao ambiente escolar, promovendo saúde, disciplina e paixão pelo voleibol desde a base.", margin_bottom="2rem"),
                    ag.grid(
                        columns="repeat(auto-fit, minmax(250px, 1fr))", gap="1.5rem",
                        children=[
                            unit_card("Colégio Ícone Recreio", "Recreio", "Vôlei", "Aulas exclusivas de voleibol para alunos.", cta_text="Consultar Horários"),
                            unit_card("Colégio Ícone Freguesia", "Freguesia", "Vôlei", "Aulas exclusivas de voleibol para alunos.", cta_text="Consultar Horários"),
                            unit_card("Colégio Ícone Taquara", "Taquara", "Vôlei", "Aulas exclusivas de voleibol para alunos.", cta_text="Consultar Horários"),
                            unit_card("Colégio St Georges", "Colégio St Georges", "Vôlei", "Aulas exclusivas de voleibol para alunos.", cta_text="Consultar Horários"),
                            unit_card("Colégio Start", "Colégio Start", "Vôlei", "Aulas exclusivas de voleibol para alunos.", cta_text="Consultar Horários"),
                        ]
                    )
                ]
            ),
            
            footer()
        ]
    )