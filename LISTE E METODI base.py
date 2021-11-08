
# LISTE 
# le liste sono contenitenitori di DATI
# per creare una lista si utilizzano le parentesi quadrate []
# a differenza delle stringhe, sono mutevoli
# possiedono moltissimi metodi e possiamo estrarne delle parti attraverso lo slicing

lista_spesa= ["uova", "latte", "pane", "miele", "cioccolata"]
print(lista_spesa)


#SLICING
#se voglio stampare solo "uova" che ha indice zero, faccio:
print(lista_spesa[0])
#se invece ad es voglio stampare i primi 3 elementi:
print(lista_spesa[0:3])
#se voglio solo ultimo 
print(lista_spesa[-1])

# LISTA DI LISTE (lista che contiene altre liste) devo creare una lista madre.
#es: Metto 2 liste nella lista madre 
lista_madre= [["uova", "latte", "pane", "miele", "cioccolata"], [1,3,5]]
#se voglio ottenere la 1a delle due liste
print(lista_madre[0])
#se voglio ottenere la 2a 
print(lista_madre[1])
#se voglio ottenere il numero 3
print(lista_madre[1][1])
#se nella lista 1 voglio prendere da latte a miele 
print(lista_madre[0][1:4])

# le liste sono MUTABILI, cioè possiamo cambiare i loro elementi all'interno
#se voglio cambiare uova con pasta 
lista_spesa[0]="pasta"
print(lista_spesa)

# FUNZIONE LEN
# ci dice di quanti elementi è compsta una lista
print (len(lista_spesa))

# Metodo APPEND
# ci permette di aggiungere elementi alla nostra lista 
lista_spesa.append("arance")
print (lista_spesa)

# REMOVE
# rimuoviamo un elemento dalla lista
lista_spesa.remove("pane")
print (lista_spesa)

# POP
# elimina l'ultimo elemento di una lista 
lista_spesa.pop()
print (lista_spesa)

# INSERT
# inseriamo un determinato elemento in una posizione specifica della nostra lista, ad un indice specifico
#es: se vogliamo inserire all'indice num 1 la stringa "biscotti":
lista_spesa.insert(1, "biscotti")
print(lista_spesa)

# REVERSE
# ci permette di invertire completamente gli elementi di una lista 
lista_spesa.reverse() 
print(lista_spesa)

# IN
# serve per capire se un elemento è presente o meno in una lista 
print("spinaci" in lista_spesa) #il risultato è false
print("cioccolata" in lista_spesa) #il risultato è true

# SORT
# Serve per ordinare degli elementi all'interno di una lista. es dei numeri in ordine crescente o delle lettere 
numeri_a_caso=[1, 7, 46, 25, 39]
numeri_a_caso.sort()
print(numeri_a_caso)

# CLEAR
# elimina completamente il contenuto di una lista 
lista_spesa.clear()
print (lista_spesa)


