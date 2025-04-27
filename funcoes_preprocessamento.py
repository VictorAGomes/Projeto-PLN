import re
import nltk

# Baixar recursos do NLTK (garante que o download seja feito corretamente)
def baixar_recursos_nltk():
    nltk.download('punkt')        # Tokenizer necessário
    nltk.download('stopwords')    # Stopwords necessárias
    nltk.download('wordnet')      # Recurso de lematização necessário

# Função para verificar se os pacotes necessários estão baixados
def verificar_e_baixar_recurso(recurso):
    try:
        nltk.data.find(f'tokenizers/{recurso}')  # Verifica se o pacote já foi baixado
        print(f"O recurso '{recurso}' já está disponível.")
    except LookupError:
        print(f"Baixando o recurso '{recurso}'...")
        nltk.download(recurso)

# Baixar recursos necessários
verificar_e_baixar_recurso('punkt')
verificar_e_baixar_recurso('stopwords')
verificar_e_baixar_recurso('wordnet')

# Instanciar o lematizador do NLTK
lemmatizer = nltk.WordNetLemmatizer()

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
    Remove caracteres especiais não-ASCII do texto.
    """
    return re.sub(r'[^\x00-\x7F]+', '', texto)  # Remove caracteres não-ASCII

def tokenizar_texto(texto):
    """
    Tokeniza o texto em palavras utilizando o NLTK.
    """
    return nltk.word_tokenize(texto)

def lematizar_tokens(tokens):
    """
    Lematiza os tokens utilizando o NLTK (WordNetLemmatizer).
    """
    return [lemmatizer.lemmatize(token) for token in tokens]
