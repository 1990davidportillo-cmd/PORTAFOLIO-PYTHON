def devolver_distintos(num1,num2,num3):
    suuma = num1 + num2 + num3
    lista = [num1,num2,num3]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        return sorted(lista)[1]

print(devolver_distintos(8,3,12))