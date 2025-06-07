import pandas as pd
from sklearn.cluster import KMeans

def clustering_kmeans(data, n_clusters=3, random_state=42):
    """
    Aplica o algoritmo KMeans para clusterização dos dados.

    Parâmetros:
        data (array-like): Dados de entrada para clusterização.
        n_clusters (int): Número de clusters.
        random_state (int): Semente para reprodutibilidade.

    Retorna:
        labels (np.ndarray): Rótulos dos clusters atribuídos a cada ponto.
        kmeans (KMeans): Objeto KMeans treinado.
    """

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(data)
    labels = kmeans.labels_
    return labels, kmeans

if __name__ == "__main__":
    # Lê o arquivo CSV atualizado
    df = pd.read_csv("data/caps_processados/resultados.csv")
    
    # Seleciona as colunas numéricas para clusterização
    features = [
        "ttr", "score_ttr", "num_types", "num_tokens",
        "hapax_legomena", "proporcao_hapax",
        "score_diversidade", "score_palavras_unicas",
        "proporcao_conectivos", "similaridade_media",
        "coesao_score", "num_conectivos", "num_sentencas"
    ]
    X = df[features].values

    # Aplica o KMeans
    labels, modelo = clustering_kmeans(X, n_clusters=3)

    # Adiciona os rótulos ao DataFrame e salva o resultado
    df["cluster"] = labels
    df.to_csv("resultados_com_clusters.csv", index=False)
    print("Clusterização concluída. Resultados salvos em 'resultados_com_clusters.csv'.")