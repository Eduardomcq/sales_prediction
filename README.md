# PREVISÃO DE VENDAS - LOJAS ROSSMANN

![rossmann](/img/rossmann.jpg "Image Title")

## Introdução

Neste projeto foi desenvolvido um modelo para a previsão de vendas de um conjunto de lojas da cadeia de farmácias Rossmann. Nosso objetivo neste projeto foi realizar a previsão da receita que as lojas presentes no conjunto de dados iria gerar nas seis semana (42 dias) subsequentes ao término do período de coleta de dados. 

Um pouco sobre a Rossmann:

A Rossamann é uma rede de drogarias com operação na Európa (sendo seus maiores mercados a Alemanha, Polônia e República Checa). Atualmente a Rossmann possui cerca de 400 lojas e 56.000 empregados, em 2019 as lojas da Rossmann faturaram aproximadamente 10 bilhões de euros.

Sobre os dados:

Neste projeto foi utilizado o conjunto de dados disponíveis on-line, publicamente, no [Kaglle](https://www.kaggle.com/c/rossmann-store-sales). Este conjunto de dados possui o faturamento diário de 1115 lojas entre 2013 e 2015. Junto ao faturamento (variável que queremos prever) estão incluídas algumas variáveis referentes a características próprias de cada uma das lojas, como, distância dos concorrentes, tamanho da loja, variedade de itens, etc. Além disso também estão presentes no banco de dados informações referentes aos dias de operações das lojas, como por exemplo a indicação de datas de férias escolares, feriádos nacionais ocorrência de promoções nas lojas etc.

## Modelos Estudados

Para a resolução deste problema optamos por comparar inicialmente os modelos: Regressão Linear, Árvore de Decisão, Random Forest e XGBoost. Os modelos foram treinados nos conjuntos de dados com os seus parâmetros em default. A partir desta análise inicial foi escolhido o modelo com melhor performance para passar pelo ajuste fino dos Hyperparâmetros. Abaixo demonstro os resultados obtidos nesta primeiro parte de validação dos modelos escolhidos:
