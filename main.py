# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def map():
    # Crie o mapa com o Folium
    mapa = folium.Map(location=[-15.7801, -47.9292], zoom_start=6)

    # Adicione marcadores ou personalizações ao mapa, conforme necessário
    # Exemplo:
    folium.Marker([-25.4, -54.59], popup='Usina Hidrelétrica de Itaipu').add_to(mapa)

    # Salve o mapa em um arquivo temporário
    mapa.save('templates/mapa_usinas.html')

    # Renderize o template HTML com o mapa
    return render_template('mapa_usinas.html')

if __name__ == '__main__':
    app.run(debug=True)


