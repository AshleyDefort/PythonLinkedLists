#!/usr/bin/env python
# coding: utf-8

# # Listas Enlazadas en Python🐍
# Ashley Mercado Defort - NRC:2442
# 
# ## ¿Cuáles son los métodos de las listas propias de Python y para qué se usan?
# Python tiene una serie de métodos integrados que se pueden usar en las listas. A continuación, se presenta una lista de los métodos de las listas de Python y sus usos:
# 
# - **append()**: Agrega un elemento al final de la lista.
# - **clear()**: Elimina todos los elementos de la lista.
# - **copy()**: Devuelve una copia de la lista.
# - **count()**: Devuelve el número de elementos con el valor especificado.
# - **extend()**: Agrega los elementos de una lista (o cualquier iterable) al final de la lista actual.
# - **index()**: Devuelve el índice del primer elemento con el valor especificado.
# - **insert()**: Agrega un elemento en la posición especificada.
# - **pop()**: Elimina el elemento en la posición especificada.
# - **remove()**: Elimina el primer elemento con el valor especificado.
# - **reverse()**: Invierte el orden de la lista.
# - **sort()**: Ordena la lista.
# 
# ## Implementación de una clase nodo y una clase lista enlazada con sus respectivos métodos
# > **Nota🗒️**: En el siguiente código se crea la clase Node (Cada elemento que conformará la lista) y la clase LinkedList. En la clase Node, solo se encuentra el constructor de la clase donde se definen los atrinutos value (dato) y next (apuntador al siguiente nodo). En la clase LinkedList se definen 9 métodos que permiten realizar distintas operaciones con la lista enlazada.

# In[5]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Revisa si la lista esta vacia
    def isEmpty(self):
        return self.head is None

    #Inserta un elemento al inicio de la lista
    def insertAtBeginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    #Inserta un elemento al final de la lista
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #Elimina un nodo de la lista
    def delete(self, value):
        if self.isEmpty():
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    #Busca un elemento en la lista
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    #Ordena la lista usando el método de ordenamiento burbuja
    def sort(self):
        if self.isEmpty() or self.head.next is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.value > current.next.value:
                    # Intercambiar los valores de los nodos
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    #Inserta un elemento en la lista de forma ordenada
    def insertOrdered(self, value):
        new_node = Node(value)

        if self.isEmpty() or value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    #Invierte la lista
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    #Muestra los elementos de la lista
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements
