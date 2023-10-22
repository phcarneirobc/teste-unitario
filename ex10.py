def inverter_string(texto):
    texto_invertido = texto[::-1]
    return texto_invertido

string_original = "ROGERIO ELETRICISTA"
string_original2 = "Subi no Onibus"


string_invertida = inverter_string(string_original)
string_invertida2 = inverter_string(string_original2)


print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
print(f"String original: {string_original2}")
print(f"String invertida: {string_invertida2}")
