list_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_2 = list_1[:]
list_2.sort()
list_3 = list_2[:]
list_3.reverse()
print("Lista initiala: ", list_1, "\n","Lista ordonata ascendent:", list_2, "\n", "Lista ordonata descendent:", list_3,
      "\n", "Elementele pare din lista: ", list_2[1::2], "\n", "Elementele impare din lista: ", list_2[::2])

print("Elemente multiplu de 3:" )
for i in list_2:
    if i % 3 == 0:
        print(i)

# sau
print("Elementele din lista divizibile cu 3: ", list_2[2::3])



