from utils import load_data, load_template, notes_plus, build_response
import urllib
from database import Database
from database import Note

d = Database('banco')

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        print(request)
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        print(corpo)
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split("=")
            valor = urllib.parse.unquote_plus(valor)
            params[chave] = valor

        if params["acao"] == "add":
            if params["titulo"] and params["detalhes"]:
                n = Note(title = params["titulo"], content = params["detalhes"])
                d.add(n)
        
        elif params["acao"] == "delete":
            d.delete(params["id"])

        elif params["acao"] == "edit":
            n = Note(title = params["novo_titulo"], content = params["nova_desc"], id = params["id"])
            d.update(n)

        

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('./components/note.html')
    notes_li = [
        note_template.format(itemId = dado.id, title=dado.title, details=dado.content)
        for dado in d.get_all()]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    if request.startswith('POST'):
        resp = (build_response(code=303, reason='See Other', headers='Location: /', body=body))
    else:
        resp = (build_response(code=200, body=body))
    return resp