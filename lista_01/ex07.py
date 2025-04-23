"""
Determinar se um aluno esta ou nao aprovado, conecidas as notas dos quatro bimestres,
sendo a media de aprovacao igual a 6.0."""

notas_aluno = list(
    map(float, input("Digite as notas do aluno(separadas por virgula): ").split(","))
)


media_bimestre = sum(notas_aluno) / len(notas_aluno)
print(media_bimestre)

if media_bimestre < 6.0:
    print("Aluno reprovado por nota.")
else:
    print("Aluno aprovado.")
