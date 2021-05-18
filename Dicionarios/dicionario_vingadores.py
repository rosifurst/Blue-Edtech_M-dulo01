vingadores = {"Chris Evans": "Capitão América",
"Mark Ruffalo": "Hulk",
"Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor",
"Robert Downey Jr": "Homem de Ferro",
"Scarlett Johansson": "Viúva Negra"
}

print(vingadores)

if "Mark Ruffalo" in vingadores:
    print("Mark Rufallo está no dicionário!")
else:
    print("Não está no dicionário.")

print(vingadores.get("Mark Ruffalo"))