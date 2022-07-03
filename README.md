# PREVISÃO DE VENDAS - LOJAS ROSSMANN

![rossmann](/img/rossmann.jpg "Logo Rossmann")

## Introdução

Neste projeto foi desenvolvido um modelo para a previsão de vendas de um conjunto de lojas da cadeia de farmácias Rossmann. Nosso objetivo neste projeto foi realizar a previsão da receita que as lojas presentes no conjunto de dados iria gerar nas seis semana (42 dias) subsequentes ao término do período de coleta de dados. 

Um pouco sobre a Rossmann:

A Rossamann é uma rede de drogarias com operação na Európa (sendo seus maiores mercados a Alemanha, Polônia e República Checa). Atualmente a Rossmann possui cerca de 400 lojas e 56.000 empregados, em 2019 as lojas da Rossmann faturaram aproximadamente 10 bilhões de euros.

Sobre os dados:

Neste projeto foi utilizado o conjunto de dados disponíveis on-line, publicamente, no [Kaglle](https://www.kaggle.com/c/rossmann-store-sales). Este conjunto de dados possui o faturamento diário de 1115 lojas entre 2013 e 2015. Junto ao faturamento (variável que queremos prever) estão incluídas algumas variáveis referentes a características próprias de cada uma das lojas, como, distância dos concorrentes, tamanho da loja, variedade de itens, etc. Além disso também estão presentes no banco de dados informações referentes aos dias de operações das lojas, como por exemplo a indicação de datas de férias escolares, feriádos nacionais ocorrência de promoções nas lojas etc.

## Modelos Estudados

Para a resolução deste problema optamos por comparar inicialmente os modelos: Regressão Linear, Árvore de Decisão, Random Forest e XGBoost. Os modelos foram treinados nos conjuntos de dados com os seus parâmetros em default. A partir desta análise inicial foi escolhido o modelo com melhor performance para passar pelo ajuste fino dos Hyperparâmetros. Abaixo demonstro os resultados obtidos nesta primeiro parte de validação dos modelos escolhidos:

![modelos](/img/modelos_treinados.jpg "modelos")

Dentre as métricas adotadas o modelo escolhido para o processo de fine tuning foi o XGBoost. Para o ajuste dos hyperparâmetros fizemos uma busca aleatória dentre um espaço de parâmetros pré-selecionados. O modelo final que chegamos possui o seguinte desempenho:

![modelos](/img/modelo_final.jpg "modelo final")

Abaixo apresento uma análise de desempenho do modelo nas lojas do conjunto de dados de teste, observa-se que para a maior parte das lojas os resultados foram satisfatórios, contudo, para algumas lojas, o modelo não foi tão preciso. Um próximo passo seria estudarmos a possibilidade de gerar um modelo especial para as lojas onde o desempenho do modelo inicial não foi tão satisfatório.

![modelos](/img/MAE_lojas.jpg "Desempenho dos Modelos")

Por fim apresento a previsão final da receita total para os dados de teste em comparação com o valor real, observa-se que as previsões seguem a tendência da série temporal real.





