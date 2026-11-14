haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

xavfli=0
for x in haroratlar:
    if x<=-18:
        xavfli+=1
print(f"Xavfli o'lchovlar: {xavfli}")

orta=sum(haroratlar)/len(haroratlar)
print(f"O'rtacha harorat: {orta:.2f} C")