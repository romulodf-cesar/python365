# ----------ENTRADA----------
# # ler o nome do aluno
# ler o número da turma
# ler três notas
# ----------PROCESSAMENTO----------
# calcular a media
# verificar status (média >= 70 é aprovado)
# ----------SAÍDA----------
# mostrar a soma das notas
# mostrar a média das notas
# mostrar se foi "aprovado" ou "reprovado"
nome=input("qual seu nome?")
turma=input("qual a sua turma?")
nota1=float(input("qual sua primeira nota?"))
nota2=float(input("qual sua segunda nota?"))
nota3=float(input("qual sua terceira nota?"))
media=(nota1+nota2+nota3)/3
print(f"olá {nome}")
print(f"sua turma é {turma}")
print(f"sua média é {media}")
if media>=70:
    print(f"parabens {nome}, voce passou!")
else:
    print(f"que pena {nome}, você não passou!")


# 10 pontos -  Felipe, Vitor,Kaike

