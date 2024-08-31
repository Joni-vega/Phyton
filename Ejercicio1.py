identificacion = {}
loop = 1

while loop == 1:
    nombre = str(input("Ingrese nombre y apellido: "))
    Domicilio = input("Ingrese direccion: ")
    categoria = input("Normal(1), Jubilado(2) ")
    estado_Act = int(input("Ingresee el estado actual del medidor: "))
    estado_Ant = int(input("Ingrese el estado anterior del medidor: "))
    precioKv = float(input("Precio KV: "))
    estado = estado_Act - estado_Ant
  
    if categoria == 1:
        valor = estado * precioKv
        total = valor
    else:
        valor = estado * precioKv
        total = valor * 0.25
    
    identificacion [nombre] = {"kw_Consumidos": estado , "Total_a_pagar":total}
    loop = int(input ("Continuar cargando datos(1), Parar de cargar(0) "))

print(identificacion)
