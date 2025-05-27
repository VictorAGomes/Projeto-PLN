# projetopln

Desenvolvimento de um sistema capaz de detectar a semelhança entre dois textos do ponto de vista da autoria.

## Coleta de dados✅
Os dados coletados vêm da fonte [domínio público](http://www.dominiopublico.gov.br/pesquisa/PesquisaObraForm.jsp) e são usados apenas para teste, a ideia é tentar descobrir a partir dos dados as features mais importantes para a comparação.

## Tratamento de dados✅
Para preparar os textos para análise, foram implementadas rotinas de pré-processamento e extração de metadados:

### Limpeza

1. limpeza_texto(texto):
Esta função tem como objetivo principal padronizar e simplificar o conteúdo textual. Ela remove elementos que podem introduzir ruído na análise, como formatação excessiva (quebras de linha, espaços múltiplos), certos tipos de pontuação e variações de capitalização e acentuação, resultando em um texto mais uniforme.

2. limpar_e_tokenizar_texto(texto):
O propósito desta função é transformar o texto bruto em uma sequência estruturada de unidades linguísticas básicas. Primeiro, ela aplica a rotina de limpeza padrão e, em seguida, segmenta o texto em sentenças e, posteriormente, em palavras individuais (tokens), preparando os dados para etapas subsequentes de modelagem ou extração de características.

3. extrair_titulo_autor(nome_arquivo):
Esta função visa extrair informações contextuais importantes (metadados) diretamente dos nomes dos arquivos. Ela é projetada para interpretar a nomenclatura dos arquivos e identificar automaticamente o título da obra e o nome do autor, facilitando a organização e identificação dos textos no corpus.

### Tokenização e Armazenamento

Esta seção do código automatiza o processamento de múltiplos arquivos de texto. Ele opera da seguinte forma:

1. Varredura de Diretório: O script localiza todos os arquivos de texto em uma pasta de entrada especificada (data/txts).
2. Extração de Metadados e Leitura: Para cada arquivo encontrado, ele primeiro extrai o título e o autor usando a função extrair_titulo_autor. Em seguida, o conteúdo textual do arquivo é lido.
3. Segmentação e Tokenização: O texto de cada arquivo é dividido em segmentos menores (aproximadamente frases, usando o ponto final como delimitador). Cada um desses segmentos é então submetido ao processo de limpeza e tokenização (através da função limpar_e_tokenizar_texto), resultando em uma lista de tokens para cada segmento.
4. Estruturação dos Dados: As informações extraídas (título, autor) e os tokens processados (agrupados por segmento) são organizados em uma estrutura de dicionário Python.
5. Armazenamento em JSON: Finalmente, esse dicionário estruturado é salvo como um arquivo JSON em uma pasta de saída (data/textos_processados). Cada arquivo de entrada .txt gera um arquivo .json correspondente, prefixado com "preprocessado_", contendo seus metadados e tokens. Isso facilita o acesso e a utilização posterior dos dados processados.
