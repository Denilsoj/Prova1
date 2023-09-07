preco = float(input("Informe o preço do produto")) 
preco_imposto = preco * 1.10
preco_total = preco + preco_imposto

if preco_total >= 100: 
    print("O produto está caro")
else:
    print("O produto está em um bom preço")

    