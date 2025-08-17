from collections import deque

class Notas:
    def ingresoNotas(self):
        self.listaNotas=deque()
        print("--Ingresao de notas--")
        while True:   
            try:        
                nota=int(input("Ingrese su nota: "))
                self.listaNotas.append(nota)
                otraNota=input("Desea continuar? SI-NO: ").upper()
                if otraNota!="SI":
                    break  
            except ValueError:
                print("Ingrese un valor valido")    
        return self.listaNotas
    
    def calculoNotas(self):
        cantPares=0 #contador de numeros pares
        sumaNotas=0 #suma de todos los datos ingresados
        ultimaNota=self.listaNotas[-1]
        self.salidaNotas=deque()
        while len(self.listaNotas)>0:
            self.calculoNotas=self.listaNotas.pop()
            self.salidaNotas.append(self.calculoNotas)

        for nota in self.salidaNotas:
            sumaNotas += nota
            if(nota%2==0):
                cantPares += 1
        
        #calculo de promedio de datos ingresados
        promNotas=sumaNotas/len(self.salidaNotas)
        
        #Salida de datos
        print("---Salida de notas---")        
        print("Notas: {}" .format(self.salidaNotas))  
        print(f"Cantidad de numeros pares: {cantPares}")
        print(f"El promedio es: {promNotas}")
        print(f"Ultimo dato ingresado: {ultimaNota}")

notas=Notas()
notas.ingresoNotas()
notas.calculoNotas()