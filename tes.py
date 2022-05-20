import tkinter
from turtle import pen

list = []
with open('testcase5.txt') as data:
    line = data.readlines()
    for i in line:
        list.append(i)


listKedua = []
for i in list:
    listKedua.append(i.split())


jumlahTitik = listKedua[0][0]
koordinat = listKedua[1:]


window = tkinter.Tk()
window.title('pertemuan 9')

cnv = tkinter.Canvas(window, width=1000, height=700)
cnv.pack()


for i in range(int(jumlahTitik)):
    var = koordinat[i]
    print(var)
    x = int(var[0])
    y = int(var[1])
    cnv.create_oval(x, y, x+20, y+20, fill='red')
    cnv.create_text(x, y, text=str(i))

koordinat.sort(key=lambda a: int(a[0]))



indeks = 0
while indeks < int(jumlahTitik)-1:
    titikPertama = koordinat[indeks]
    titikKedua = koordinat[indeks+1]
    cnv.create_line(int(titikPertama[0]),int(titikPertama[1]),int(titikKedua[0]),int(titikKedua[1]))
    indeks += 1


window.mainloop()
