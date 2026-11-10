import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import numpy_financial as npf

# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title="Calculadora de Juros",
    layout="wide"
)

pd.set_option("display.float_format", "{:.2f}".format)


# FUNÇÃO DE CÁLCULO

def calcular_investimento(capital_inicial, taxa_anual, anos, aporte_mensal):

    # Taxa anual em decimal
    txa = taxa_anual / 100

    # Taxa mensal equivalente para juros compostos
    i = (1 + txa) ** (1 / 12) - 1

    # Taxa mensal nominal para juros simples
    ism = txa / 12

    # Número de meses
    t = anos * 12

    # Meses do investimento
    meses = list(range(t + 1))

    # --------------------------------------------------------
    # Cálculos
    # --------------------------------------------------------

    total_investido = [
        capital_inicial + aporte_mensal * n
        for n in meses
    ]

    simples = [
        (
            (capital_inicial + capital_inicial * ism * n)
            + (aporte_mensal * n)
            + (aporte_mensal * ism * (n * (n - 1) / 2))
        )
        for n in meses
    ]

    composto = [
        (
            capital_inicial * (1 + i) ** n
            + aporte_mensal * (((1 + i) ** n - 1) / i)
            if i != 0
            else capital_inicial + aporte_mensal * n
        )
        for n in meses
    ]

    juros_simples = [
        simples[n] - total_investido[n]
        for n in range(len(meses))
    ]

    juros_compostos = [
        composto[n] - total_investido[n]
        for n in range(len(meses))
    ]

    # DataFrame

    df = pd.DataFrame({
        "Mês": meses,
        "Total investido": total_investido,
        "Simples": simples,
        "Composto": composto,
        "Total juros (Simples)": juros_simples,
        "Total juros (Composto)": juros_compostos
    })

    return df, i, ism


# SIDEBAR

st.sidebar.title("Parâmetros")

st.sidebar.markdown(
    "Configure os parâmetros abaixo para simular a evolução "
    "do seu investimento."
)

capital_inicial = st.sidebar.number_input(
    "Capital inicial (R$)",
    min_value=0.0,
    value=10000.0,
    step=500.0,
    format="%.2f"
)

taxa_anual = st.sidebar.number_input(
    "Taxa de juros anual (%)",
    min_value=0.0,
    value=10.0,
    step=0.5,
    format="%.2f"
)

anos = st.sidebar.number_input(
    "Período (anos)",
    min_value=1,
    max_value=100,
    value=10,
    step=1
)

aporte_mensal = st.sidebar.number_input(
    "Aporte mensal (R$)",
    min_value=0.0,
    value=1000.0,
    step=100.0,
    format="%.2f"
)

st.sidebar.markdown("---")

calcular = st.sidebar.button(
    "Calcular simulação",
    use_container_width=True
)


# TÍTULO

st.title("Simulador de Investimentos")

st.markdown(
    """
    Compare a evolução de um investimento utilizando **juros simples**
    e **juros compostos**, considerando capital inicial e aportes mensais.
    """
)


# CÁLCULO

df, taxa_mensal_composta, taxa_mensal_simples = calcular_investimento(
    capital_inicial,
    taxa_anual,
    anos,
    aporte_mensal
)


# RESULTADOS

valor_investido_final = df["Total investido"].iloc[-1]
valor_simples_final = df["Simples"].iloc[-1]
valor_composto_final = df["Composto"].iloc[-1]

juros_simples_final = df["Total juros (Simples)"].iloc[-1]
juros_compostos_final = df["Total juros (Composto)"].iloc[-1]

aporte_total = aporte_mensal * (anos * 12)

retorno_percentual_composto = ((valor_composto_final - valor_investido_final) / valor_investido_final) * 100
retorno_percentual_simples = ((valor_simples_final - valor_investido_final) / valor_investido_final) * 100

fluxos = []

for meses in range(anos * 12 + 1):

    if meses == 0:
        fluxo = -capital_inicial

    elif meses < anos * 12:
        fluxo = -aporte_mensal

    else:
        fluxo = -aporte_mensal + valor_composto_final

    fluxos.append(fluxo)

tir_mensal = npf.irr(fluxos)

tir_anual = (1 + tir_mensal) ** 12 - 1

tir_mp = tir_mensal * 100

tir_ap = tir_anual * 100

# CARDS / KPIs - linha 1

st.subheader("Resumo da simulação")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Capital inicial",
        f"R$ {capital_inicial:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col2:
    st.metric(
        "Total aportado",
        f"R$ {aporte_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

# COMPARAÇÃO - linha 2

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total investido",
        f"R$ {valor_investido_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col2:
    st.metric(
        "Patrimônio — Simples",
        f"R$ {valor_simples_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col3:
    st.metric(
        "Patrimônio — Composto",
        f"R$ {valor_composto_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

# JUROS - linha 3

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Juros simples",
        f"R$ {juros_simples_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col2:
    st.metric(
        "Juros compostos",
        f"R$ {juros_compostos_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col3:
    diferenca = valor_composto_final - valor_simples_final

    st.metric(
        "Vantagem do composto",
        f"R$ {diferenca:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

# RETORNOS - linha 4

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Retorno percentual composto",
        f"{retorno_percentual_composto:,.2f}%".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col2:
    st.metric(
        "Retorno percentual simples",
        f"{retorno_percentual_simples:,.2f}%".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col3:
    st.metric(
        "TIR mensal",
        f"{tir_mp:,.2f} %".replace(",", "X").replace(".", ",").replace("X", ".")
    )

# PARÂMETROS CALCULADOS

with st.expander("Ver parâmetros calculados"):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Taxa anual:**")
        st.write(f"{taxa_anual:.2f}%")

    with col2:
        st.write("**Taxa mensal — simples:**")
        st.write(f"{taxa_mensal_simples * 100:.4f}%")

    with col3:
        st.write("**Taxa mensal — composta:**")
        st.write(f"{taxa_mensal_composta * 100:.4f}%")


# GRÁFICO 1 — EVOLUÇÃO DO PATRIMÔNIO

st.subheader("Evolução do patrimônio")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["Mês"],
        y=df["Simples"],
        mode="lines",
        name="Juros Simples",
        line=dict(
            color="red",
            dash="dash"
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=df["Mês"],
        y=df["Composto"],
        mode="lines",
        name="Juros Compostos",
        line=dict(
            color="black"
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=df["Mês"],
        y=df["Total investido"],
        mode="lines",
        name="Total Investido",
        line=dict(
            color="blue",
            dash="dot"
        )
    )
)

fig.update_layout(
    title="Simples vs. Composto",
    xaxis_title="Tempo (meses)",
    yaxis_title="Patrimônio acumulado (R$)",
    template="plotly_white",
    hovermode="x unified",
    height=550
)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

st.plotly_chart(
    fig,
    use_container_width=True
)


# GRÁFICO 2 — JUROS ACUMULADOS

st.subheader("Evolução dos juros acumulados")

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=df["Mês"],
        y=df["Total juros (Simples)"],
        mode="lines",
        name="Juros Simples",
        line=dict(
            color="red",
            dash="dash"
        )
    )
)

fig1.add_trace(
    go.Scatter(
        x=df["Mês"],
        y=df["Total juros (Composto)"],
        mode="lines",
        name="Juros Compostos",
        line=dict(
            color="black"
        )
    )
)

fig1.update_layout(
    title="Juros acumulados ao longo do tempo",
    xaxis_title="Tempo (meses)",
    yaxis_title="Juros acumulados (R$)",
    template="plotly_white",
    hovermode="x unified",
    height=500
)

fig1.update_xaxes(showgrid=False)
fig1.update_yaxes(showgrid=False)

st.plotly_chart(
    fig1,
    use_container_width=True
)


# TABELA

st.subheader("Dados da simulação")

st.dataframe(
    df.style.format({
        "Total investido": "R$ {:,.2f}",
        "Simples": "R$ {:,.2f}",
        "Composto": "R$ {:,.2f}",
        "Total juros (Simples)": "R$ {:,.2f}",
        "Total juros (Composto)": "R$ {:,.2f}"
    }),
    use_container_width=True,
    height=400
)


# DOWNLOAD

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Baixar dados em CSV",
    data=csv,
    file_name="simulacao_investimento.csv",
    mime="text/csv"
)


# RODAPÉ

st.markdown("---")

st.caption(
    "Simulador desenvolvido com Python, Pandas, Plotly, NumPy Financial e Streamlit."
)