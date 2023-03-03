from ApiAeza import aeza

token = aeza.AuthAeza('YOUR-API-KEY')

print(token.get_balance())
print(token.get_api_key())
print(token.invoice_card(100))
