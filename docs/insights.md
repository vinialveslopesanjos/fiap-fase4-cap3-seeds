# Insights — Classificação de grãos Seeds

## Melhor modelo

- **Modelo escolhido:** `random_forest` com ajuste via GridSearchCV.
- **F1 / acurácia:** F1 ponderado 0.9192 e acurácia 0.9206 no conjunto de teste.
- **Por que venceu:** o Random Forest capturou relações não lineares entre área, perímetro, comprimento, largura e assimetria dos grãos. Ele superou KNN, SVM, Naive Bayes e Regressão Logística no F1 ponderado, mantendo bom equilíbrio entre as três variedades.

## Contexto cooperativa

A classificação automática ajuda cooperativas de pequeno porte a reduzir erro humano e tempo de triagem de grãos Kama, Rosa e Canadian. Em vez de depender apenas de inspeção visual, o modelo usa medidas morfológicas para sugerir a variedade provável e padronizar a separação dos lotes.

## Interpretação da matriz de confusão

- Canadian teve melhor desempenho: 21 acertos em 21 amostras de teste.
- Rosa teve 20 acertos em 21 amostras.
- Kama foi a classe mais difícil: 17 acertos em 21 amostras, com confusão pontual com Canadian e Rosa.

## Limitações

- O dataset tem apenas 210 amostras, o que limita a generalização.
- As medidas foram coletadas em ambiente controlado; dados reais de cooperativa podem ter ruído de sensores, lotes misturados e variação por safra.
- Algumas variáveis morfológicas são correlacionadas, então novos testes com validação cruzada e dados externos seriam importantes antes de uso produtivo.

## Próximos passos

- Coletar novos lotes de grãos em condições reais.
- Validar o modelo com safras diferentes.
- Criar uma interface simples para upload de medições e retorno da classe prevista.
- Registrar previsões erradas para retreinamento periódico.
