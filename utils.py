import json

def extract_route(string):
    return string.split()[1][1:]

def read_file(path):
    strPath = str(path)
    if strPath.split(".") == ["txt", "html", "css", "js"]:
        with open(path, "r") as file:
            conteudo = file.read()
    else:
        with open(path, "rb") as file:
            conteudo = file.read()

    return conteudo

def load_data(file):
    with open(f"data/{file}", "r") as file:
        conteudo = json.load(file)
    return conteudo

def load_template(file):
    with open(f"templates/{file}", "r") as file:
        conteudo = file.read()
    return conteudo

def notes_plus(new):
    data = load_data("notes.json")
    data.append(new)
    newData = json.dumps(data)
    with open(f"data/notes.json", "w") as file:
        file.write(newData)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        return (f'HTTP/1.1 {code} {reason}\n{headers}\n\n' + body).encode()
    else:
        return (f'HTTP/1.1 {code} {reason}\n\n' + body).encode() 
