# for
alunos = ["fred", "Joao", "Maria","jose"]
for i in alunos:
    print(i)

for i in range(0,10):
    print(i)

# while
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print("dentro do while",i)

i = 0
while i < 10:
    i += 1
    if i == 5:
       pass
    print("dentro do while",i)
else:
    print("Saiu do while")
