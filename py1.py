from cgitb import text
import tkinter as tk
import math

# base case / terminal condition => jika lvl == curlvl


def gambar_segitiga(cnv, lvl, curlvl, panjang, titikA):
    if lvl < curlvl:
        return 
    if curlvl == 1:
        cnv.create_text(titikA[0], titikA[1])
        Bx = math.cos( math.radians(60) ) * panjang
        By = math.sin( math.radians(60) ) * panjang
        cnv.create_text(titikA[0] + Bx, titikA[1] + By)

        Cx = math.cos( math.radians(120) ) * panjang
        Cy = math.sin( math.radians(120) ) * panjang
        cnv.create_text(titikA[0] + Cx, titikA[1] + Cy)

        cnv.create_line(titikA[0], titikA[1], titikA[0]+Bx, titikA[1]+By)
        cnv.create_line(titikA[0], titikA[1], titikA[0]+Cx, titikA[1]+Cy)
        cnv.create_line(titikA[0]+Bx, titikA[1]+By, titikA[0]+Cx, titikA[1]+Cy)

    if curlvl < lvl :
        # sisi kanan
        Ax2 = math.cos( math.radians(60) ) * (panjang /3)
        Ay2 = math.sin( math.radians(60) ) * (panjang /3)
        cnv.create_text(titikA[0] + Ax2, titikA[1] + Ay2)

        Bx2 = math.cos(math.radians(0)) * (panjang /3)
        By2 = math.sin(math.radians(0)) * (panjang /3)
        cnv.create_text((titikA[0]+Ax2) + Bx2, (titikA[1]+Ay2) + By2)
        cnv.create_line(titikA[0]+ Ax2, titikA[1]+ Ay2, (titikA[0]+Ax2)+Bx2, (titikA[1]+Ay2)+By2)

        Cx2 = math.cos(math.radians(240)) * (panjang /3)
        Cy2 = math.sin(math.radians(240)) * (panjang /3)
        cnv.create_text((titikA[0]+Bx) + Cx2, (titikA[1]+By) + Cy2)
        cnv.create_line((titikA[0]+Ax2)+Bx2, (titikA[1]+Ay2)+By2,(titikA[0]+Bx) + Cx2, (titikA[1]+By) + Cy2)

        # sisi kiri
        Ax3 = math.cos( math.radians(120) ) * (panjang /3)
        Ay3 = math.sin( math.radians(120) ) * (panjang /3) 
        cnv.create_text(titikA[0] + Ax3, titikA[1] + Ay3)

        Bx3 = math.cos(math.radians(180)) * (panjang /3)
        By3 = math.sin(math.radians(180)) * (panjang /3)
        cnv.create_text((titikA[0] + Ax3) + Bx3, (titikA[1] + Ay3) + By3)
        cnv.create_line(titikA[0]+ Ax3, titikA[1]+ Ay3, (titikA[0]+Ax3)+Bx3, (titikA[1]+Ay3)+By3)

        Cx3 = math.cos(math.radians(300)) * (panjang /3)
        Cy3 = math.sin(math.radians(300)) * (panjang /3)
        cnv.create_text((titikA[0]+Cx) + Cx3, (titikA[1]+Cy) + Cy3)
        cnv.create_line((titikA[0]+Ax3)+Bx3, (titikA[1]+Ay3)+By3,(titikA[0]+Cx) + Cx3, (titikA[1]+Cy) + Cy3)

        # sisi bawah
        Ax4 = math.cos( math.radians(180) ) * (panjang /3)
        Ay4 = math.sin( math.radians(180) ) * (panjang /3)
        cnv.create_text((titikA[0] + Bx)+Ax4, (titikA[1] + By)+Ay4)

        Cx4 = math.cos( math.radians(120) ) * (panjang /3)
        Cy4 = math.sin( math.radians(120) ) * (panjang /3)
        cnv.create_text(((titikA[0] + Bx)+Ax4)+Cx4, ((titikA[1] + By)+Ay4)+Cy4)
        cnv.create_line((titikA[0] + Bx)+Ax4, (titikA[1] + By)+Ay4,((titikA[0] + Bx)+Ax4)+Cx4, ((titikA[1] + By)+Ay4)+Cy4)

        Bx4 = math.cos( math.radians(0) ) * (panjang /3)
        By4 = math.sin( math.radians(0) ) * (panjang /3)
        cnv.create_text((titikA[0] + Cx)+Bx4, (titikA[1] + Cy)+By4)
        cnv.create_line(((titikA[0] + Bx)+Ax4)+Cx4, ((titikA[1] + By)+Ay4)+Cy4,(titikA[0] + Cx)+Bx4, (titikA[1] + Cy)+By4)

    if lvl>=3:
        # sisi kanan dalam bagian atas
        Ax5 = math.cos(math.radians(0)) * (panjang /9)
        Ay5 = math.sin(math.radians(0)) * (panjang /9)
        cnv.create_text((titikA[0]+Ax2) +Ax5, (titikA[1]+Ay2)+Ay5)

        Bx5 = math.cos(math.radians(300)) * (panjang /9)
        By5 = math.sin(math.radians(300)) * (panjang /9)
        cnv.create_text(((titikA[0]+Ax2) + Ax5)+Bx5, ((titikA[1]+Ay2) + Ay5)+By5)
        cnv.create_line((titikA[0]+Ax2) +Ax5, (titikA[1]+Ay2)+Ay5,((titikA[0]+Ax2) + Ax5)+Bx5, ((titikA[1]+Ay2) + Ay5)+By5)

        Cx5 = math.cos(math.radians(180)) * (panjang /9)
        Cy5 = math.sin(math.radians(180)) * (panjang /9)
        cnv.create_text(((titikA[0]+Ax2)+Bx2) +Cx5, ((titikA[1]+Ay2)+By2) +Cy5)
        cnv.create_line(((titikA[0]+Ax2) + Ax5)+Bx5, ((titikA[1]+Ay2) + Ay5)+By5,((titikA[0]+Ax2)+Bx2) +Cx5, ((titikA[1]+Ay2)+By2) +Cy5)

        # sisi kanan dalam bagian kanan
        Ax6 = math.cos(math.radians(120)) * (panjang /9)
        Ay6 = math.sin(math.radians(120)) * (panjang /9)
        cnv.create_text(((titikA[0]+Ax2) + Bx2)+Ax6, ((titikA[1]+Ay2) + By2)+Ay6)

        Bx6 = math.cos(math.radians(60)) * (panjang /9)
        By6 = math.sin(math.radians(60)) * (panjang /9)
        cnv.create_text((((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6, (((titikA[1]+Ay2) + By2)+Ay6)+By6)

        Cx6 = math.cos(math.radians(300)) * (panjang /9)
        Cy6 = math.sin(math.radians(300)) * (panjang /9)
        cnv.create_text(((titikA[0]+Bx) + Cx2)+Cx6, ((titikA[1]+By) + Cy2)+Cy6)

        cnv.create_line(((titikA[0]+Ax2) + Bx2)+Ax6, ((titikA[1]+Ay2) + By2)+Ay6,(((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6, (((titikA[1]+Ay2) + By2)+Ay6)+By6)
        cnv.create_line((((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6, (((titikA[1]+Ay2) + By2)+Ay6)+By6,((titikA[0]+Bx) + Cx2)+Cx6, ((titikA[1]+By) + Cy2)+Cy6)

        # sisi bawah bagian dalam kanan
        Ax7 = math.cos( math.radians(120) ) * (panjang /9)
        Ay7 = math.sin( math.radians(120) ) * (panjang /9)
        cnv.create_text(((titikA[0] + Bx)+Ax4)+Ax7, ((titikA[1] + By)+Ay4)+Ay7)

        Bx7 = math.cos( math.radians(60) ) * (panjang /9)
        By7 = math.sin( math.radians(60) ) * (panjang /9)
        cnv.create_text((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7, (((titikA[1] + By)+Ay4)+Ay7)+By7)

        Cx7 = math.cos( math.radians(300) ) * (panjang /9)
        Cy7 = math.sin( math.radians(300) ) * (panjang /9)
        cnv.create_text((((titikA[0] + Bx)+Ax4)+Cx4)+Cx7, (((titikA[1] + By)+Ay4)+Cy4)+Cy7)

        cnv.create_line(((titikA[0] + Bx)+Ax4)+Ax7, ((titikA[1] + By)+Ay4)+Ay7, (((titikA[0] + Bx)+Ax4)+Ax7)+Bx7, (((titikA[1] + By)+Ay4)+Ay7)+By7)
        cnv.create_line((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7, (((titikA[1] + By)+Ay4)+Ay7)+By7, (((titikA[0] + Bx)+Ax4)+Cx4)+Cx7, (((titikA[1] + By)+Ay4)+Cy4)+Cy7)


        # sisi dalam bagian bawah kiri
        Ax8 = math.cos( math.radians(60) ) * (panjang /9)
        Ay8 = math.sin( math.radians(60) ) * (panjang /9)
        cnv.create_text(((titikA[0] + Cx)+Bx4)+Ax8, ((titikA[1] + Cy)+By4)+Ay8)

        Bx8 = math.cos( math.radians(120) ) * (panjang /9)
        By8 = math.sin( math.radians(120) ) * (panjang /9)
        cnv.create_text((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8, (((titikA[1] + Cy)+By4)+Ay8)+By8)


        Cx8 = math.cos( math.radians(240) ) * (panjang /9)
        Cy8 = math.sin( math.radians(240) ) * (panjang /9)
        cnv.create_text((((titikA[0] + Bx)+Ax4)+Cx4)+Cx8, (((titikA[1] + By)+Ay4)+Cy4)+Cy8)

        cnv.create_line(((titikA[0] + Cx)+Bx4)+Ax8, ((titikA[1] + Cy)+By4)+Ay8, (((titikA[0] + Cx)+Bx4)+Ax8)+Bx8, (((titikA[1] + Cy)+By4)+Ay8)+By8)
        cnv.create_line((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8, (((titikA[1] + Cy)+By4)+Ay8)+By8, (((titikA[0] + Bx)+Ax4)+Cx4)+Cx8, (((titikA[1] + By)+Ay4)+Cy4)+Cy8)

        # sisi dalam bagian kiri atas
        Ax9 = math.cos( math.radians(180) ) * (panjang /9)
        Ay9 = math.sin( math.radians(180) ) * (panjang /9) 
        cnv.create_text((titikA[0] + Ax3)+Ax9, (titikA[1] + Ay3)+Ay9)

        Bx9 = math.cos( math.radians(240) ) * (panjang /9)
        By9 = math.sin( math.radians(240) ) * (panjang /9) 
        cnv.create_text(((titikA[0] + Ax3)+Ax9)+Bx9, ((titikA[1] + Ay3)+Ay9)+By9)

        Cx9 = math.cos(math.radians(0)) * (panjang /9)
        Cy9 = math.sin(math.radians(0)) * (panjang /9)
        cnv.create_text(((titikA[0] + Ax3) + Bx3)+Cx9, ((titikA[1] + Ay3) + By3)+Cy9)
        
        cnv.create_line((titikA[0] + Ax3)+Ax9, (titikA[1] + Ay3)+Ay9, ((titikA[0] + Ax3)+Ax9)+Bx9, ((titikA[1] + Ay3)+Ay9)+By9)
        cnv.create_line(((titikA[0] + Ax3)+Ax9)+Bx9, ((titikA[1] + Ay3)+Ay9)+By9, ((titikA[0] + Ax3) + Bx3)+Cx9, ((titikA[1] + Ay3) + By3)+Cy9)

        # sisi kiri bagian dalam bawah
        Ax10 = math.cos(math.radians(60)) * (panjang /9)
        Ay10 = math.sin(math.radians(60)) * (panjang /9)
        cnv.create_text(((titikA[0] + Ax3) + Bx3)+Ax10, ((titikA[1] + Ay3) + By3)+Ay10)

        Bx10 = math.cos(math.radians(120)) * (panjang /9)
        By10 = math.sin(math.radians(120)) * (panjang /9)
        cnv.create_text((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10, (((titikA[1] + Ay3) + By3)+Ay10)+By10)

        Cx10 = math.cos(math.radians(240)) * (panjang /9)
        Cy10 = math.sin(math.radians(240)) * (panjang /9)
        cnv.create_text(((titikA[0]+Cx) + Cx3)+Cx10, ((titikA[1]+Cy) + Cy3)+Cy10)

        cnv.create_line(((titikA[0] + Ax3) + Bx3)+Ax10, ((titikA[1] + Ay3) + By3)+Ay10, (((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10, (((titikA[1] + Ay3) + By3)+Ay10)+By10)
        cnv.create_line((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10, (((titikA[1] + Ay3) + By3)+Ay10)+By10, ((titikA[0]+Cx) + Cx3)+Cx10, ((titikA[1]+Cy) + Cy3)+Cy10)

   
    if lvl >= 4 :
        # sisi dalam kanan bagian kiri
        Ax11 = math.cos(math.radians(300)) * (panjang /27)
        Ay11 = math.sin(math.radians(300)) * (panjang /27)
        cnv.create_text(((titikA[0]+Ax2) +Ax5)+Ax11, ((titikA[1]+Ay2)+Ay5)+Ay11)

        Bx11 = math.cos(math.radians(240)) * (panjang /27)
        By11 = math.sin(math.radians(240)) * (panjang /27)
        cnv.create_text((((titikA[0]+Ax2) +Ax5)+Ax11)+Bx11, (((titikA[1]+Ay2)+Ay5)+Ay11)+By11)

        Cx11 = math.cos(math.radians(120)) * (panjang /27)
        Cy11 = math.sin(math.radians(120)) * (panjang /27)
        cnv.create_text((((titikA[0]+Ax2) + Ax5)+Bx5)+Cx11, (((titikA[1]+Ay2) + Ay5)+By5)+Cy11)

        cnv.create_line(((titikA[0]+Ax2) +Ax5)+Ax11, ((titikA[1]+Ay2)+Ay5)+Ay11, (((titikA[0]+Ax2) +Ax5)+Ax11)+Bx11, (((titikA[1]+Ay2)+Ay5)+Ay11)+By11)
        cnv.create_line((((titikA[0]+Ax2) +Ax5)+Ax11)+Bx11, (((titikA[1]+Ay2)+Ay5)+Ay11)+By11, (((titikA[0]+Ax2) + Ax5)+Bx5)+Cx11, (((titikA[1]+Ay2) + Ay5)+By5)+Cy11)

        # sisi dalam kanan bagian kanan
        Ax12 = math.cos(math.radians(60)) * (panjang /27)
        Ay12 = math.sin(math.radians(60)) * (panjang /27)
        cnv.create_text((((titikA[0]+Ax2) + Ax5)+Bx5)+Ax12, (((titikA[1]+Ay2) + Ay5)+By5)+Ay12)

        Bx12 = math.cos(math.radians(0)) * (panjang /27)
        By12 = math.sin(math.radians(0)) * (panjang /27)
        cnv.create_text(((((titikA[0]+Ax2) + Ax5)+Bx5)+Ax12)+Bx12, ((((titikA[1]+Ay2) + Ay5)+By5)+Ay12)+By12)

        Cx12 = math.cos(math.radians(240)) * (panjang /27)
        Cy12 = math.sin(math.radians(240)) * (panjang /27)
        cnv.create_text((((titikA[0]+Ax2)+Bx2) +Cx5)+Cx12, (((titikA[1]+Ay2)+By2) +Cy5)+Cy12)
        
        cnv.create_line((((titikA[0]+Ax2) + Ax5)+Bx5)+Ax12, (((titikA[1]+Ay2) + Ay5)+By5)+Ay12, ((((titikA[0]+Ax2) + Ax5)+Bx5)+Ax12)+Bx12, ((((titikA[1]+Ay2) + Ay5)+By5)+Ay12)+By12)
        cnv.create_line(((((titikA[0]+Ax2) + Ax5)+Bx5)+Ax12)+Bx12, ((((titikA[1]+Ay2) + Ay5)+By5)+Ay12)+By12, (((titikA[0]+Ax2)+Bx2) +Cx5)+Cx12, (((titikA[1]+Ay2)+By2) +Cy5)+Cy12)

        # sisi kanan ke 2 bagian kiri
        Ax13 = math.cos(math.radians(60)) * (panjang /27)
        Ay13 = math.sin(math.radians(60)) * (panjang /27)
        cnv.create_text((((titikA[0]+Ax2) + Bx2)+Ax6)+Ax13, (((titikA[1]+Ay2) + By2)+Ay6)+Ay13)

        Bx13 = math.cos(math.radians(0)) * (panjang /27)
        By13 = math.sin(math.radians(0)) * (panjang /27)
        cnv.create_text(((((titikA[0]+Ax2) + Bx2)+Ax6)+Ax13)+Bx13, ((((titikA[1]+Ay2) + By2)+Ay6)+Ay13)+By13)

        Cx13 = math.cos(math.radians(240)) * (panjang /27)
        Cy13 = math.sin(math.radians(240)) * (panjang /27)
        cnv.create_text(((((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6)+Cx13, ((((titikA[1]+Ay2) + By2)+Ay6)+By6)+Cy13)

        cnv.create_line((((titikA[0]+Ax2) + Bx2)+Ax6)+Ax13, (((titikA[1]+Ay2) + By2)+Ay6)+Ay13, ((((titikA[0]+Ax2) + Bx2)+Ax6)+Ax13)+Bx13, ((((titikA[1]+Ay2) + By2)+Ay6)+Ay13)+By13)
        cnv.create_line(((((titikA[0]+Ax2) + Bx2)+Ax6)+Ax13)+Bx13, ((((titikA[1]+Ay2) + By2)+Ay6)+Ay13)+By13, ((((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6)+Cx13, ((((titikA[1]+Ay2) + By2)+Ay6)+By6)+Cy13)


        # sisi kanan bagian kiri
        Ax14 = math.cos(math.radians(0)) * (panjang /27)
        Ay14 = math.sin(math.radians(0)) * (panjang /27)
        cnv.create_text((((titikA[0]+Bx) + Cx2)+Cx6)+Ax14, (((titikA[1]+By) + Cy2)+Cy6)+Ay14)

        Bx14 = math.cos(math.radians(60)) * (panjang /27)
        By14 = math.sin(math.radians(60)) * (panjang /27)
        cnv.create_text(((((titikA[0]+Bx) + Cx2)+Cx6)+Ax14)+Bx14, ((((titikA[1]+By) + Cy2)+Cy6)+Ay14)+By14)

        Cx14 = math.cos(math.radians(180)) * (panjang /27)
        Cy14 = math.sin(math.radians(180)) * (panjang /27)
        cnv.create_text(((((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6)+Cx14, ((((titikA[1]+Ay2) + By2)+Ay6)+By6)+Cy14)

        cnv.create_line((((titikA[0]+Bx) + Cx2)+Cx6)+Ax14, (((titikA[1]+By) + Cy2)+Cy6)+Ay14, ((((titikA[0]+Bx) + Cx2)+Cx6)+Ax14)+Bx14, ((((titikA[1]+By) + Cy2)+Cy6)+Ay14)+By14)
        cnv.create_line(((((titikA[0]+Bx) + Cx2)+Cx6)+Ax14)+Bx14, ((((titikA[1]+By) + Cy2)+Cy6)+Ay14)+By14, ((((titikA[0]+Ax2) + Bx2)+Ax6)+Bx6)+Cx14, ((((titikA[1]+Ay2) + By2)+Ay6)+By6)+Cy14)

        # sisi bawah
        Ax15 = math.cos( math.radians(60) ) * (panjang /27)
        Ay15 = math.sin( math.radians(60) ) * (panjang /27)
        cnv.create_text((((titikA[0] + Bx)+Ax4)+Ax7)+Ax15, (((titikA[1] + By)+Ay4)+Ay7)+Ay15)

        Bx15 = math.cos( math.radians(0) ) * (panjang /27)
        By15 = math.sin( math.radians(0) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Bx)+Ax4)+Ax7)+Ax15)+Bx15, ((((titikA[1] + By)+Ay4)+Ay7)+Ay15)+By15)

        Cx15 = math.cos( math.radians(240) ) * (panjang /27)
        Cy15 = math.sin( math.radians(240) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Cx15, ((((titikA[1] + By)+Ay4)+Ay7)+By7)+Cy15)

        cnv.create_line((((titikA[0] + Bx)+Ax4)+Ax7)+Ax15, (((titikA[1] + By)+Ay4)+Ay7)+Ay15, ((((titikA[0] + Bx)+Ax4)+Ax7)+Ax15)+Bx15, ((((titikA[1] + By)+Ay4)+Ay7)+Ay15)+By15)
        cnv.create_line(((((titikA[0] + Bx)+Ax4)+Ax7)+Ax15)+Bx15, ((((titikA[1] + By)+Ay4)+Ay7)+Ay15)+By15, ((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Cx15, ((((titikA[1] + By)+Ay4)+Ay7)+By7)+Cy15)

        # sisi bawah bagian kanan
        Ax16 = math.cos( math.radians(180) ) * (panjang /27)
        Ay16 = math.sin( math.radians(180) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Ax16, ((((titikA[1] + By)+Ay4)+Ay7)+By7)+Ay16)

        Bx16 = math.cos( math.radians(120) ) * (panjang /27)
        By16 = math.sin( math.radians(120) ) * (panjang /27)
        cnv.create_text((((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Ax16)+Bx16, (((((titikA[1] + By)+Ay4)+Ay7)+By7)+Ay16)+By16)

        Cx16 = math.cos( math.radians(0) ) * (panjang /27)
        Cy16 = math.sin( math.radians(0) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Bx)+Ax4)+Cx4)+Cx7)+Cx16, ((((titikA[1] + By)+Ay4)+Cy4)+Cy7)+Cy16)

        cnv.create_line(((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Ax16, ((((titikA[1] + By)+Ay4)+Ay7)+By7)+Ay16, (((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Ax16)+Bx16, (((((titikA[1] + By)+Ay4)+Ay7)+By7)+Ay16)+By16)
        cnv.create_line((((((titikA[0] + Bx)+Ax4)+Ax7)+Bx7)+Ax16)+Bx16, (((((titikA[1] + By)+Ay4)+Ay7)+By7)+Ay16)+By16, ((((titikA[0] + Bx)+Ax4)+Cx4)+Cx7)+Cx16, ((((titikA[1] + By)+Ay4)+Cy4)+Cy7)+Cy16)

        # sisi bawah bagian kiri
        Ax17 = math.cos( math.radians(120) ) * (panjang /27)
        Ay17 = math.sin( math.radians(120) ) * (panjang /27)
        cnv.create_text((((titikA[0] + Cx)+Bx4)+Ax8)+Ax17, (((titikA[1] + Cy)+By4)+Ay8)+Ay17)

        Bx17 = math.cos( math.radians(180) ) * (panjang /27)
        By17 = math.sin( math.radians(180) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Cx)+Bx4)+Ax8)+Ax17)+Bx17, ((((titikA[1] + Cy)+By4)+Ay8)+Ay17)+By17)

        Cx17 = math.cos( math.radians(300) ) * (panjang /27)
        Cy17 = math.sin( math.radians(300) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Cx17, ((((titikA[1] + Cy)+By4)+Ay8)+By8)+Cy17)

        cnv.create_line((((titikA[0] + Cx)+Bx4)+Ax8)+Ax17, (((titikA[1] + Cy)+By4)+Ay8)+Ay17, ((((titikA[0] + Cx)+Bx4)+Ax8)+Ax17)+Bx17, ((((titikA[1] + Cy)+By4)+Ay8)+Ay17)+By17)
        cnv.create_line(((((titikA[0] + Cx)+Bx4)+Ax8)+Ax17)+Bx17, ((((titikA[1] + Cy)+By4)+Ay8)+Ay17)+By17, ((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Cx17, ((((titikA[1] + Cy)+By4)+Ay8)+By8)+Cy17)


        # sisi bagian bawah kiri
        Ax18 = math.cos( math.radians(0) ) * (panjang /27)
        Ay18 = math.sin( math.radians(0) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Ax18, ((((titikA[1] + Cy)+By4)+Ay8)+By8)+Ay18)

        Bx18 = math.cos( math.radians(60) ) * (panjang /27)
        By18 = math.sin( math.radians(60) ) * (panjang /27)
        cnv.create_text((((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Ax18)+Bx18, (((((titikA[1] + Cy)+By4)+Ay8)+By8)+Ay18)+By18)

        Cx18 = math.cos( math.radians(180) ) * (panjang /27)
        Cy18 = math.sin( math.radians(180) ) * (panjang /27)
        cnv.create_text(((((titikA[0] + Bx)+Ax4)+Cx4)+Cx8)+Cx18, ((((titikA[1] + By)+Ay4)+Cy4)+Cy8)+Cy18)

        cnv.create_line(((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Ax18, ((((titikA[1] + Cy)+By4)+Ay8)+By8)+Ay18, (((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Ax18)+Bx18, (((((titikA[1] + Cy)+By4)+Ay8)+By8)+Ay18)+By18)
        cnv.create_line((((((titikA[0] + Cx)+Bx4)+Ax8)+Bx8)+Ax18)+Bx18, (((((titikA[1] + Cy)+By4)+Ay8)+By8)+Ay18)+By18, ((((titikA[0] + Bx)+Ax4)+Cx4)+Cx8)+Cx18, ((((titikA[1] + By)+Ay4)+Cy4)+Cy8)+Cy18)

        # sisi kiri bagian kanan
        Ax19 = math.cos( math.radians(240) ) * (panjang /27)
        Ay19 = math.sin( math.radians(240) ) * (panjang /27) 
        cnv.create_text(((titikA[0] + Ax3)+Ax9)+Ax19, ((titikA[1] + Ay3)+Ay9)+Ay19)

        Bx19 = math.cos( math.radians(300) ) * (panjang /27)
        By19 = math.sin( math.radians(300) ) * (panjang /27) 
        cnv.create_text((((titikA[0] + Ax3)+Ax9)+Ax19)+Bx19, (((titikA[1] + Ay3)+Ay9)+Ay19)+By19)

        
        Cx19 = math.cos( math.radians(60) ) * (panjang /27)
        Cy19 = math.sin( math.radians(60) ) * (panjang /27) 
        cnv.create_text((((titikA[0] + Ax3)+Ax9)+Bx9)+Cx19, (((titikA[1] + Ay3)+Ay9)+By9)+Cy19)

        cnv.create_line(((titikA[0] + Ax3)+Ax9)+Ax19, ((titikA[1] + Ay3)+Ay9)+Ay19, (((titikA[0] + Ax3)+Ax9)+Ax19)+Bx19, (((titikA[1] + Ay3)+Ay9)+Ay19)+By19)
        cnv.create_line((((titikA[0] + Ax3)+Ax9)+Ax19)+Bx19, (((titikA[1] + Ay3)+Ay9)+Ay19)+By19, (((titikA[0] + Ax3)+Ax9)+Bx9)+Cx19, (((titikA[1] + Ay3)+Ay9)+By9)+Cy19)

        # sisi kiri bagian kanan
        Ax20 = math.cos(math.radians(300)) * (panjang /27)
        Ay20 = math.sin(math.radians(300)) * (panjang /27)
        cnv.create_text((((titikA[0] + Ax3) + Bx3)+Cx9)+Ax20, (((titikA[1] + Ay3) + By3)+Cy9)+Ay20)

        Bx20 = math.cos(math.radians(240)) * (panjang /27)
        By20 = math.sin(math.radians(240)) * (panjang /27)
        cnv.create_text(((((titikA[0] + Ax3) + Bx3)+Cx9)+Ax20)+Bx20, ((((titikA[1] + Ay3) + By3)+Cy9)+Ay20)+By20)
        
        Cx20 = math.cos( math.radians(120) ) * (panjang /27)
        Cy20 = math.sin( math.radians(120) ) * (panjang /27) 
        cnv.create_text((((titikA[0] + Ax3)+Ax9)+Bx9)+Cx20, (((titikA[1] + Ay3)+Ay9)+By9)+Cy20)

        cnv.create_line((((titikA[0] + Ax3) + Bx3)+Cx9)+Ax20, (((titikA[1] + Ay3) + By3)+Cy9)+Ay20, ((((titikA[0] + Ax3) + Bx3)+Cx9)+Ax20)+Bx20, ((((titikA[1] + Ay3) + By3)+Cy9)+Ay20)+By20)
        cnv.create_line(((((titikA[0] + Ax3) + Bx3)+Cx9)+Ax20)+Bx20, ((((titikA[1] + Ay3) + By3)+Cy9)+Ay20)+By20, (((titikA[0] + Ax3)+Ax9)+Bx9)+Cx20, (((titikA[1] + Ay3)+Ay9)+By9)+Cy20)

        # sisi kiri bagian kiri
        Ax21 = math.cos(math.radians(120)) * (panjang /27)
        Ay21 = math.sin(math.radians(120)) * (panjang /27)
        cnv.create_text((((titikA[0] + Ax3) + Bx3)+Ax10)+Ax21, (((titikA[1] + Ay3) + By3)+Ay10)+Ay21)

        Bx21 = math.cos(math.radians(180)) * (panjang /27)
        By21 = math.sin(math.radians(180)) * (panjang /27)
        cnv.create_text(((((titikA[0] + Ax3) + Bx3)+Ax10)+Ax21)+Bx21, ((((titikA[1] + Ay3) + By3)+Ay10)+Ay21)+By21)

        Cx21 = math.cos(math.radians(300)) * (panjang /27)
        Cy21 = math.sin(math.radians(300)) * (panjang /27)
        cnv.create_text(((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Cx21, ((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Cy21)

        cnv.create_line((((titikA[0] + Ax3) + Bx3)+Ax10)+Ax21, (((titikA[1] + Ay3) + By3)+Ay10)+Ay21, ((((titikA[0] + Ax3) + Bx3)+Ax10)+Ax21)+Bx21, ((((titikA[1] + Ay3) + By3)+Ay10)+Ay21)+By21)
        cnv.create_line(((((titikA[0] + Ax3) + Bx3)+Ax10)+Ax21)+Bx21, ((((titikA[1] + Ay3) + By3)+Ay10)+Ay21)+By21, ((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Cx21, ((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Cy21)

        # sisi kiri bagian kiri bawah
        Ax22 = math.cos(math.radians(0)) * (panjang /27)
        Ay22 = math.sin(math.radians(0)) * (panjang /27)
        cnv.create_text(((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Ax22, ((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Ay22)

        Bx22 = math.cos(math.radians(60)) * (panjang /27)
        By22 = math.sin(math.radians(60)) * (panjang /27)
        cnv.create_text((((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Ax22)+Bx22, (((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Ay22)+By22)

        Cx22 = math.cos(math.radians(180)) * (panjang /27)
        Cy22 = math.sin(math.radians(180)) * (panjang /27)
        cnv.create_text((((titikA[0]+Cx) + Cx3)+Cx10)+Cx22, (((titikA[1]+Cy) + Cy3)+Cy10)+Cy22)

        cnv.create_line(((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Ax22, ((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Ay22, (((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Ax22)+Bx22, (((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Ay22)+By22)
        cnv.create_line((((((titikA[0] + Ax3) + Bx3)+Ax10)+Bx10)+Ax22)+Bx22, (((((titikA[1] + Ay3) + By3)+Ay10)+By10)+Ay22)+By22, (((titikA[0]+Cx) + Cx3)+Cx10)+Cx22, (((titikA[1]+Cy) + Cy3)+Cy10)+Cy22)

   
    
lvl = int(input('masukkan level: '))


window = tk.Tk()

cnv = tk.Canvas(window, width=1000, height=500)
cnv.pack()

panjang = 350

Ax = 550
Ay = 50


gambar_segitiga(cnv, lvl, 1, panjang, (Ax, Ay))
window.mainloop()

