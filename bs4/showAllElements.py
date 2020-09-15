from bs4 import BeautifulSoup
import tqdm

def get_list_of_files(path):
    with open(path) as fp:
        return fp

def parse_docs(path):
    docs = []
    soup = BeautifulSoup(open(path, encoding='utf-8').read())
    text = '\n'.join([''.join(s.findAll(text=True)) for s in
                        soup.findAll(True)])  # parse all <p>, <div>, and <h> tags
    docs.append(text)

    return docs

path = 'datas/sample02.html'
result = parse_docs(path)    
print(result)