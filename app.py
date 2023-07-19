import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# importar os dataframes
df_bp = pd.read_csv('data/business_performance.csv')
df_bp.drop('Unnamed: 0', axis=1, inplace=True)

df_cp = pd.read_csv('data/crossprice.csv')
df_pe = pd.read_csv('data/product_elasticity.csv')


####### LAYOUT STREAMLIT ########
st.set_page_config(layout='wide')
st.header('Elasticidade de Preço dos Produtos')

tab1, tab2, tab3 = st.tabs(
    ['Elasticidade de Preço dos Produtos', 'Business Performance', 'Elasticidade Cruzada'])

with tab1:
    tab4, tab5 = st.tabs(['Grafico', 'Dataframe'])

    with tab4:
        st.header('Gráfico')
        df_pe['ranking'] = df_pe.loc[:, 'price_elasticity'].rank(
            ascending=True).astype(int)
        df_elasticity = df_pe.reset_index(drop=True)
        fig, ax = plt.subplots()
        plt.figure(figsize=(12, 6))
        ax.hlines(y=df_elasticity['ranking'], xmin=0,
                  xmax=df_elasticity['price_elasticity'], alpha=0.5)

        for name, p in zip(df_elasticity['name'], df_elasticity['ranking']):
            ax.text(4, p, name)

        # Add Elasticity Labels
        for x, y, s in zip(df_elasticity['price_elasticity'], df_elasticity['ranking'], df_elasticity['price_elasticity']):
            ax.text(x, y, round(s, 2), horizontalalignment='right' if x < 0 else 'left',
                    verticalalignment='center',
                    fontdict={'color': 'red' if x < 0 else 'green', 'size': 10})

        plt.gca().set(ylabel='Ranking Number', xlabel='Price Elasticity')
        plt.title('Price Elasticity', fontdict={'size': 13})
        plt.grid(linestyle='--')

        st.pyplot(fig)

    with tab5:
        st.header('Dataframe')
        df_order_elasticity = df_pe[['ranking', 'name', 'price_elasticity']].sort_values(
            by='price_elasticity', ascending=False)
        df_order_elasticity = df_order_elasticity.set_index('ranking')
        st.dataframe(df_order_elasticity, use_container_width=True)

with tab2:
    # Apresentar Business Performance
    st.header('Business Performance')
    df_bp = df_bp.set_index('name')
    st.dataframe(df_bp, use_container_width=True)

with tab3:
    # Apresentar Elasticidade Cruzada
    st.header('Elasticidade Cruzada')
    df_cp = df_cp.set_index('name')
    st.dataframe(df_cp, use_container_width=True)
