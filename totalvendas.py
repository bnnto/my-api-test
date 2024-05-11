import requests

link = 'https://f2c534c1-42ba-45cf-a978-dcc63b6ef89c-00-2gyau2ihr2wg6.picard.replit.dev/pegarvendas'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())
dicionario = requisicao.json()
print(dicionario['total_vendas'])