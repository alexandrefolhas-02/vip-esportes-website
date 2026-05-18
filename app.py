# app.py
import antigravity as ag
from pages.index import homepage
# Futuras importações:
# from pages.unidades import unidades_page

# Inicializar a aplicação
app = ag.App(name="VIP_Esportes_Web")

# Definir as rotas (URLs)
app.add_route("/", homepage)
# app.add_route("/unidades", unidades_page)

# Ponto de entrada exigido pela Vercel e ambientes locais
if __name__ == "__main__":
    app.run(port=3000)