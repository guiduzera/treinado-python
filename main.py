# biblioteca utilizada para ler arquivos no geral
import pandas as pd
# biblioteca utilizada para mandar os sms's
from twilio.rest import Client
#
account_sid = "AC0861ec30ec99cb1bbce411f1ce5ed647"
auth_token  = "76614ccb2d5697fde1c9e8e82550bc9b"
client = Client(account_sid, auth_token)

# exemplo de variavel e de um array
mesesAno = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# forma de se percorrer um array no python
for elementos in mesesAno:
    # utilizando o pd para ler um arquivo selecionado e colocando ele dentro de um for
    tabela_vendas = pd.read_excel(f'{elementos}.xlsx')
    # abrindo arquivos de maneira dinamica com o for.
    if (tabela_vendas['Vendas'] > 55000).any():
        # utilizando o .any como um .some para selecionar o elemento com as caracteristicas pedidas no array
        # utilizando o .loc pra localizar alguma linha da tabela como um .filter retornando o valor em foram de tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        faturamento = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mes de {elementos} o vendedor {vendedor} atingiu a meta, com um total de vendas de {faturamento}, parabens!')
        # usando o [] pra acessar alguma coluna da tabela
        message = client.messages.create(
            to="+5584994407369",
            from_="+18048081660",
            body=f"no mes de {elementos} o vendedor {vendedor} atingiu a meta, com um total de vendas de {faturamento}, parabens!")
        print(message.sid)



