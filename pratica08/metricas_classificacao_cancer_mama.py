
import numpy as np
from sklearn.datasets import load_breast_cancer # Importar o dataset de câncer de mama
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import warnings

# Ignorar warnings que podem aparecer devido à convergência do modelo
warnings.filterwarnings("ignore")

def calcular_e_comparar_metricas_cancer_mama():
    """
    Carrega o dataset de câncer de mama, treina um modelo simples e
    calcula/compara métricas de classificação.
    """
    print("--- Comparação de Métricas de Classificação em IA (Câncer de Mama) ---")

    # 1. Carregar o dataset de câncer de mama
    cancer = load_breast_cancer()
    X = cancer.data   # Características (features)
    y_true = cancer.target # Rótulos verdadeiros (0 para maligno, 1 para benigno)

    print(f"Dataset de Câncer de Mama carregado:")
    print(f"  - {X.shape[0]} amostras, {X.shape[1]} features.")
    print(f"  - Classes: {cancer.target_names} (0: {cancer.target_names[0]}, 1: {cancer.target_names[1]})")
    print(f"  - Exemplo de uma amostra (primeira): {X[0][:5]}...") # Mostra as 5 primeiras features

    # Dividir os dados em conjuntos de treinamento e teste
    # test_size=0.3 significa que 30% dos dados serão para teste
    # random_state=42 garante que a divisão seja a mesma sempre que você rodar
    X_train, X_test, y_train, y_test = train_test_split(X, y_true, test_size=0.3, random_state=42)

    print(f"\nDivisão dos dados:")
    print(f"  - Conjunto de treinamento (X_train, y_train): {X_train.shape[0]} amostras")
    print(f"  - Conjunto de teste (X_test, y_test): {X_test.shape[0]} amostras")

    # 2. Treinar um modelo de classificação simples (Regressão Logística)
    # Este é um modelo de exemplo para gerar previsões
    model = LogisticRegression(solver='liblinear', random_state=42) # 'liblinear' é um bom solver para datasets menores
    model.fit(X_train, y_train)

    # 3. Obter as previsões do modelo no conjunto de teste
    y_pred = model.predict(X_test) # Previsões das classes (0 ou 1)
    # y_prob_positive_class: Probabilidades da classe positiva (1 - benigno)
    y_prob_positive_class = model.predict_proba(X_test)[:, 1]

    print("\n--- Métricas de Classificação Calculadas ---")

    # 4. Calcular as métricas

    # Precisão (Accuracy): (TP + TN) / Total
    # Porcentagem total de previsões corretas (tanto positivos quanto negativos).
    accuracy = accuracy_score(y_test, y_pred)
    print(f"1. Precisão (Accuracy): {accuracy:.4f}")
    print("   - Porcentagem total de previsões corretas.")

    # Precisão (Precision): TP / (TP + FP)
    # Das vezes que o modelo previu 'Positivo' (Câncer Benigno), quantas estavam corretas?
    # Aqui, a classe positiva (pos_label=1) é "Benigno" (não câncer).
    # Se a classe positiva fosse "Maligno" (câncer), o pos_label seria 0.
    precision = precision_score(y_test, y_pred, pos_label=1)
    print(f"2. Precisão (Precision): {precision:.4f}")
    print("   - Dos casos que o modelo previu como BENIGNO, quantos realmente eram BENIGNOS.")
    print("   - Importante quando o custo de um FALSO POSITIVO é alto.")

    # Recall (Sensibilidade): TP / (TP + FN)
    # Das amostras que realmente são 'Positivas' (Câncer Benigno), quantas o modelo identificou?
    recall = recall_score(y_test, y_pred, pos_label=1)
    print(f"3. Recall: {recall:.4f}")
    print("   - Dos casos que eram BENIGNOS (reais), quantos o modelo identificou como BENIGNOS.")
    print("   - Importante quando o custo de um FALSO NEGATIVO é alto.")

    # F1-Score: 2 * (Precision * Recall) / (Precision + Recall)
    # Média harmônica entre Precision e Recall. Bom quando há um balanço entre ambos.
    f1 = f1_score(y_test, y_pred, pos_label=1)
    print(f"4. F1-Score: {f1:.4f}")
    print("   - Combina Precision e Recall, útil quando você quer um equilíbrio entre eles.")

    # AUC-ROC (Area Under the Receiver Operating Characteristic Curve)
    # Mede a capacidade do modelo de distinguir entre classes.
    # Requer as probabilidades da classe positiva. Um valor próximo de 1 é excelente.
    auc_roc = roc_auc_score(y_test, y_prob_positive_class)
    print(f"5. AUC-ROC: {auc_roc:.4f}")
    print("   - Capacidade do modelo de distinguir entre as classes. Valor mais próximo de 1 é melhor.")


    print("\n--- Interpretação Rápida ---")
    print("Em problemas de câncer de mama, geralmente preferimos um ALTO RECALL para a classe de câncer (Maligno).")
    print("Isso significa minimizar FALSOS NEGATIVOS (dizer que não é câncer quando é).")
    print("Para o dataset de câncer de mama do sklearn, a classe 0 é maligno e a 1 é benigno.")
    print("As métricas acima (Precision, Recall, F1) foram calculadas para a classe POSITIVA (Benigno).")
    print("\nSe quisermos focar em detectar maligno (classe 0) com ALTO RECALL:")
    # Recalculando recall para a classe 0 (maligno)
    recall_maligno = recall_score(y_test, y_pred, pos_label=0)
    print(f"  - Recall para Maligno (classe 0): {recall_maligno:.4f}")

# --- Execução principal ---
if __name__ == "__main__":
    calcular_e_comparar_metricas_cancer_mama()
    