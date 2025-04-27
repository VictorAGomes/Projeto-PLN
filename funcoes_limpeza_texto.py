import re
import nltk
from nltk.tokenize import RegexpTokenizer

# Baixar recursos do NLTK
nltk.download('punkt')
nltk.download('stopwords')

def normalizar_texto(texto):
    """
    Normaliza o texto, removendo quebras de linha excessivas, espaços extras e espaços do início e fim.
    """
    texto = re.sub(r'\n+', ' ', texto)  # Remove quebras de linha excessivas
    texto = re.sub(r'\s+', ' ', texto)  # Remove espaços extras
    texto = texto.strip()  # Remove espaços do início e fim
    return texto

def remover_caracteres_especiais(texto):
    """
    Remove caracteres especiais não-ASCII do texto, preservando acentos e caracteres especiais como ç, ã, etc.
    """
    return re.sub(r'[^a-zA-ZáéíóúãõçÁÉÍÓÚÃÕÇ0-9\s]+', '', texto)

def tokenizar_texto(texto):
    """
    Tokeniza o texto utilizando o RegexpTokenizer do NLTK, que preserva acentos e caracteres especiais.
    """
    tokenizer = RegexpTokenizer(r'\w+|[^\w\s]', gaps=False)
    return tokenizer.tokenize(texto)

def lematizar_tokens(tokens):
    """
    Lematiza os tokens utilizando o NLTK.
    """
    from nltk.stem import RSLPStemmer
    stemmer = RSLPStemmer()
    return [stemmer.stem(token) for token in tokens]
