import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ___________________________________________________
# Variaveis de controle
CSV_FILE = "assinantes_neostream.csv"
SEED = 2
TEST_GROUP_SIZE = 0.2
N_CROSS_VALIDATION_SPLITS = 5

def get_model():
  # ___________________________________________________
  # Carregamento do dataset e definição das variaveis alvo e preditoras:

  assinantes_df = pd.read_csv(CSV_FILE)

  assinantes_df.drop_duplicates()
  assinantes_df = assinantes_df.dropna(subset=["churn"])

  x = assinantes_df.drop(columns=["churn"])
  target = assinantes_df["churn"]

  # ___________________________________________________
  # Declaração de variaveis de controle
  COL_numericas = [
      "tempo_assinatura_meses",
      "uso_medio_semanal_horas",
      "numero_reclamacoes",
  ]
  COL_categoricas = [
      "plano",
      "metodo_pagamento",
      "dispositivo_principal"
  ]

  # ___________________________________________________
  # Definição de variáveis preditoras (X) e alvo (target)
  X = assinantes_df.drop(columns=["churn", "cliente_id", "ltv_alto"]) if "cliente_id" in assinantes_df.columns else assinantes_df.drop(columns=["churn"])
  y = assinantes_df["churn"]

  # ___________________________________________________
  # Divisão dos casos de treino e teste
  x_train, x_test, y_train, y_test = train_test_split(
      x, y,
      test_size=TEST_GROUP_SIZE,
      stratify=y,
      random_state=SEED
  )

  # ___________________________________________________
  # Declaração dos preprocessadores e pipeline
  preparador_colunas = ColumnTransformer(
      transformers=[
          ("num", StandardScaler(), COL_numericas),
          ("cat", OneHotEncoder(handle_unknown='ignore'), COL_categoricas),
      ]
  )

  pipeline_base = Pipeline(
      steps=[
          ("preprocessor", preparador_colunas),
          ("classifier", LogisticRegression(random_state=SEED))
      ]
  )

  # ___________________________________________________
  # Busca dos melhores parametros
  param_grid = {"classifier__C": [0.01, 0.1, 1, 10, 100]}

  grid_search = GridSearchCV(
      estimator=pipeline_base,
      param_grid=param_grid,
      cv=N_CROSS_VALIDATION_SPLITS,
      scoring="accuracy"
  )
  grid_search.fit(x_train, y_train)

  # Resultado da busca:
  pipeline_final = grid_search.best_estimator_

  # ___________________________________________________
  # Avaliação do modelo nos casos de teste
  y_pred = pipeline_final.predict(x_test)
  acuracia_teste = accuracy_score(y_test, y_pred)

  print("==================================================")
  print("RELATÓRIO DE DESEMPENHO - PIPELINE FINAL DE CHURN")
  print("==================================================\n")
  print(f"Melhores Hiperparâmetros encontrados: {grid_search.best_params_}")
  print(f"Melhor Score de Validação Cruzada: {grid_search.best_score_:.4f}")
  print(f"Acurácia Final no Conjunto de Teste: {acuracia_teste:.4f}\n")
  
  return pipeline_final

if __name__ == "__main__":
  get_model()
