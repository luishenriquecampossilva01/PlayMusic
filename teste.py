#Lambda Expressions

#Estrutura
# minha_funcao lambda parametro: expressão

imposto = 0.3

#função tradicional
def preco_imposto(preco):
    return preco * (1+ imposto)
print(preco_imposto(100))

#função lambda
preco_imposto2 = lambda preco: preco * (1+imposto)

print(preco_imposto2(100))