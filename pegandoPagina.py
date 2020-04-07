
from urllib.request import Request,urlopen,urlretrieve
from bs4 import BeautifulSoup
import pandas as pd

#Interando as paginas do site
cards = []

### PARA SAITES QUE NAO DAO ERROR DE 404
url = 'https://alura-site-scraping.herokuapp.com/index.php'
response = urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")

#Pegando paginas 

paginas = int(soup.find('span',class_ = 'info-pages').get_text().split()[-1])
for i  in range(25):
    
    response = urlopen('https://alura-site-scraping.herokuapp.com/index.php?page=' + str(i + 1))
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html,"html.parser")
    
    #Obtendo as tegs de interesse
    anuncios = soup.find('div',id = 'container-cards').findAll('div', class_ = 'card')
    #Coletando os Cards
    for anuncio in anuncios:
        card = {}
    
        #valor
        valor_carro = anuncio.find('p',class_ = 'txt-value').getText()
        card['valor'] = valor_carro 
    
        #Info
        infos = anuncio.find('div', class_ = 'body-card').find_all('p')
        for info in infos:
             card[info.get('class')[0].split('-')[-1]] =  info.get_text()
    
        #Acessorios
        items =  anuncio.find('div', class_ = 'body-card').ul.find_all('li')
        items.pop()
        acessorios = []
        for item in items:
            acessorios.append(item.get_text().replace('►',""))
            card['items'] = acessorios

        #Adicionando resultado a lista de cards
        cards.append(card)

        #Imagens
        img = anuncio.find('div', class_ = "image-card").img
        url_img = img.get('src')
        nome = url_img.split('/')[-1]
        urlretrieve(url_img , './web/' + nome )

#Criando um DataFrame com os resultados
dataset = pd.DataFrame(cards)    
dataset.to_csv('./data/dataset.csv',sep= ";" ,index=False, encoding='utf-8-sig')







