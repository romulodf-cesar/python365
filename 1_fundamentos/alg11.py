# algoritmo 11: leia três notas e mostre a média de um aluno

# que nome que eu coloco na variável
primeira_nota = 0;
primeira_nota = int(input("Digite a nota"))
segunda_nota = int(input("Digite outra nota"))
terceira_nota = int(input("Digite a última nota"))

soma = primeira_nota + segunda_nota + terceira_nota
print(f"A soma é:{soma}")
media = soma/3

print("a média das notas é igual a:"+str(media))
# 80 60 75 = soma ? 215  media ? 71,66
# caso de teste

