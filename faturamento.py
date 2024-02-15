import json

# Abre e carrega os dados na variavel dados
with open("dados.json") as f:
    dados = json.load(f)

faturamento = [] #Lista para armazenar os valores de faturamento
for d in dados:
    valor = d["valor"]
    if valor > 0:
        faturamento.append(valor)

# menor faturamento ocorrido
menor = min(faturamento)

# maior faturamento ocorrido
maior = max(faturamento)

# Calcula a média de faturamento
media = sum(faturamento) / len(faturamento)

dias_acima_da_media = 0

# soma se o valor for maior que a média
for valor in faturamento:
    if valor > media:
        dias_acima_da_media += 1
        
#resultados
print(f"O menor faturamento ocorrido foi de: R$ {menor:.2f}")
print(f"O maior faturamento ocorrido foi de: R$ {maior:.2f}")
print(f"Em {dias_acima_da_media} dias o faturamento foi maior que a media mensal.")