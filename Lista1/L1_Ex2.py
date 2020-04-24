n1 = int( input ("Digite a primeira nota do aluno: "))

p1 = int( input ("Digite o peso da primeira nota do aluno: "))

n2 = int( input ("Digite a segunda nota do aluno: "))

p2 = int( input ("Digite o peso da segunda nota do aluno: "))

n3 = int( input ("Digite a terceira nota do aluno: "))

p3 = int( input ("Digite o peso da terceira nota do aluno: "))

print("Media Ponderada do aluno= {}". format(((n1*p1) + (n2*p2) + (n3*p3)) / (p1+p2+p3)))
