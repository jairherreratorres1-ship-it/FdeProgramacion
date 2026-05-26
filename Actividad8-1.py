nombres = ["Ana", "Luis", "Carlos", "Marta", "Jorge"]
precios = [10.5, 20.0, 15.75, 8.25, 12.0]
cantidades = [2, 1, 3, 4, 2]

total = 0

for nombre,precio,cantidad in zip(nombres, precios, cantidades):
    subtotal = precio * cantidad
    total += subtotal
    print(f"{nombre}: {cantidad} x {precio}")

print(f"Total: {total}")