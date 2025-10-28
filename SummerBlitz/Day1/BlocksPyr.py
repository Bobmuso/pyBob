blocks = int(input("Enter the number of blocks: "))
height = 0
topLay = 2
#
while blocks > 0:
    blocks -= topLay
    topLay += 1
    height += 1
#	

print("The height of the pyramid:", height)