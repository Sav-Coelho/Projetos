import numpy as np
import streamlit as sr
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as fig
import numpy as ny

sr.title('Portfolio Analysis Dashboard')

ativos = sr.text_input('Escolha os ativos do seu portfolio',"ITUB4.SA,GGBR4.SA,PETR4.SA")

benchmark = sr.text_input('Escolha seu benchmark','^BVSP')

inicio = sr.date_input('Qual o período de analíse?',value=pd.to_datetime('2024-01-02'))

dados = yf.download(ativos,start=inicio)['Adj Close']

ret_s = dados.pct_change(1)

ret_cum = (ret_s + 1).cumprod() - 1

ret_cum_mean = ret_cum.mean(axis=1)

dados_benchmark = yf.download(benchmark,start=inicio)['Adj Close']

bench_ret = dados_benchmark.pct_change(1)

bench_cum = (bench_ret + 1).cumprod() - 1

pesos = (ny.ones(len(ret_s.cov()))/len(ret_s.cov()))

desvio = (pesos.dot(ret_s.cov()).dot(pesos)) ** 1/2

sr.subheader('Portfólio vs Índice do Benchmark')

gra = pd.concat([bench_cum,ret_cum_mean],axis=1)
gra.columns = ['Desempenho Bencmark','Desempenho Portfolio']
sr.line_chart(data=gra)

sr.subheader('Risco do Portfolio')
print(desvio)

sr.subheader('Risco do Benchmark')
print(bench_ret.std())

sr.subheader('Composição do Portfolio')

plt,ax = fig.subplots()
ax.pie(pesos,labels=dados.columns,autopct='%1.1f%%',textprops={'color':'white'})

sr.pyplot(plt)


