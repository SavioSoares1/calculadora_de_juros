# Calculadora de Juros e Simulador de Investimentos

Aplicação web desenvolvida em Python e Streamlit para simular a evolução de investimentos, comparar juros simples e compostos e analisar a rentabilidade de uma aplicação ao longo do tempo.

A ferramenta permite personalizar os parâmetros do investimento, acompanhar a evolução do patrimônio por meio de gráficos interativos e visualizar indicadores financeiros, incluindo retorno percentual e Taxa Interna de Retorno (TIR).

# Objetivo do projeto

Desenvolver uma ferramenta interativa para demonstrar o impacto dos juros e dos aportes mensais na formação de patrimônio, facilitando a compreensão da diferença entre juros simples e compostos.

O projeto também tem como objetivo aplicar conceitos de matemática financeira, manipulação de dados e visualização de informações utilizando Python.

# Funcionalidades

Definição do capital inicial;

Personalização da taxa de juros anual;

Definição do período de investimento (em anos);

Configuração de aportes mensais;

Cálculo da evolução mensal do patrimônio;

Comparação entre juros simples e compostos;

Cálculo do total investido e dos juros acumulados;

Cálculo do retorno percentual nos dois cenários;

Cálculo da Taxa Interna de Retorno (TIR) mensal;

Visualização da evolução do patrimônio em gráficos interativos;

Visualização dos juros acumulados ao longo do tempo;

Tabela detalhada com os resultados da simulação;

Exportação dos dados em formato CSV.

# Indicadores financeiros

O dashboard apresenta indicadores que permitem acompanhar e comparar os resultados da simulação.

Indicador

Descrição

Capital inicial

Valor aplicado no início do investimento.

Total aportado

Soma dos aportes mensais realizados.

Total investido

Capital inicial somado aos aportes.

Patrimônio — Simples

Patrimônio acumulado no cenário de juros simples.

Patrimônio — Composto

Patrimônio acumulado no cenário de juros compostos.

Juros simples

Total de juros acumulados no cenário simples.

Juros compostos

Total de juros acumulados no cenário composto.

Vantagem do composto

Diferença entre os patrimônios finais dos dois cenários.

Retorno percentual

Retorno acumulado em relação ao total investido.

TIR mensal

Taxa interna de retorno mensal considerando os fluxos de caixa.

# Visualizações

A aplicação conta com dois gráficos principais, desenvolvidos utilizando Plotly.

1. Evolução do patrimônio

Apresenta a evolução do patrimônio ao longo do período de investimento, comparando três séries:

Juros simples;

Juros compostos;

Total investido (capital inicial + aportes).

O gráfico permite observar como a capitalização dos juros compostos influencia a formação de patrimônio no longo prazo.

2. Evolução dos juros acumulados

Demonstra a evolução dos juros gerados em cada modalidade, permitindo visualizar a diferença entre o crescimento linear e o crescimento composto.

# Tecnologias utilizadas

Python: linguagem principal utilizada no desenvolvimento;

Pandas: manipulação, organização e estruturação dos dados;

Plotly: criação de gráficos interativos;

Streamlit: desenvolvimento da interface web;

NumPy Financial: cálculos financeiros, incluindo a Taxa Interna de Retorno (TIR).

# Possíveis melhorias futuras

Inclusão de inflação e cálculo do retorno real;

Comparação com indicadores de mercado, como CDI e Selic;

Simulação de aportes variáveis e extraordinários;

Comparação entre diferentes cenários de rentabilidade;

Inclusão de taxas, impostos e custos operacionais;

Exportação dos resultados para Excel;

Disponibilização da aplicação em uma plataforma de hospedagem.

# Aprendizados

O desenvolvimento deste projeto proporcionou a aplicação prática de conceitos relacionados a:

Matemática financeira;

Juros simples e compostos;

Fluxos de caixa e Taxa Interna de Retorno;

Manipulação de dados com Pandas;

Visualização de dados com Plotly;

Desenvolvimento de aplicações web com Streamlit;

Construção de indicadores financeiros.

# ⚠️ Disclaimer

Esta aplicação possui finalidade educacional e de simulação. Os resultados são estimativas matemáticas baseadas nos parâmetros informados e não representam recomendação de investimento.

O modelo não considera inflação, impostos, taxas administrativas, custos operacionais ou oscilações de mercado.

👤 Autor

Sávio Soares Braga

⭐ Se este projeto foi útil, considere deixar uma estrela no repositório!
