from tkinter import *
from tkinter import messagebox
import webbrowser
import random
from tkinter import filedialog
from tkinter.filedialog import  asksaveasfile
from tkinter.filedialog import  askopenfilename
def log():
    '''enn1=StringVar()
    enn2=StringVar()
    user=enn1.get()
    password=enn2.get()
    if user=="the team" and password=="123456":''' 
    op=messagebox.askyesno("Super Market System",
                              "Do you want to log in system")
    if op > 0:
          pro.destroy()
          root=Tk()
          class Super:
              def __init__(self,root):
                  self.root=root
                  self.root.geometry('1520x780+0+0')
                  self.root.title('Super_Market')
                  self.root.resizable(width=False,height=False)
                  self.root.iconbitmap('D:\\market.ico')
                  title=Label(self.root,text='Super Market :Project Management',fg='gold',bg='#030303',font=('tajawal',15))
                  title.pack(fill=X)
                  #__________ÈÞæáíÇÊ___________#
                  self.e7=IntVar()     
                  self.e8=IntVar()     
                  self.e9=IntVar()     
                  self.e10=IntVar()     
                  self.e11=IntVar()     
                  self.e12=IntVar()     
                  self.e13=IntVar()     
                  self.e14=IntVar()     
                  self.e15=IntVar()     
                  self.e16=IntVar()     
                  self.e17=IntVar()     
                  self.e18=IntVar()     
                  self.e19=IntVar()     
                  self.e20=IntVar()     
                  self.e21=IntVar()     
                  self.e22=IntVar()     
                  self.e23=IntVar()     
                  self.e24=IntVar()  
                  #__________ÇÏæÇÊ ãäÒáíÉ________#
                  self.e25=IntVar()     
                  self.e26=IntVar()     
                  self.e27=IntVar()     
                  self.e28=IntVar()     
                  self.e29=IntVar()     
                  self.e30=IntVar()     
                  self.e31=IntVar()     
                  self.e32=IntVar()     
                  self.e33=IntVar()     
                  self.e34=IntVar()     
                  self.e35=IntVar()     
                  self.e36=IntVar()     
                  self.e37=IntVar()     
                  self.e38=IntVar()     
                  self.e39=IntVar()     
                  self.e40=IntVar()     
                  self.e41=IntVar()     
                  self.e42=IntVar()     
                  #___________ÇÏæÇÊ ßåÑÈíÉ_________#
                  self.e43=IntVar()     
                  self.e44=IntVar()     
                  self.e45=IntVar()     
                  self.e46=IntVar()     
                  self.e47=IntVar()     
                  self.e48=IntVar()     
                  self.e49=IntVar()     
                  self.e50=IntVar()     
                  self.e51=IntVar()     
                  self.e52=IntVar()     
                  self.e53=IntVar()     
                  self.e54=IntVar()     
                  self.e55=IntVar()     
                  self.e56=IntVar()     
                  self.e57=IntVar()
                  #____ãÊÛíÑÇÊ ÈíÇäÇÊ ÇáãÔÊÑí______#
                  self.name=StringVar()
                  self.phone=StringVar()
                  self.fatora=StringVar()
                  x=random.randint(1000,9999)
                  self.fatora.set(str(x))
                  #______ãÊÛíÑÇÊ ÇáÍÓÇÈ Çáßáí______#
                  self.bacoliat=StringVar()
                  self.adoat=StringVar()
                  self.kahraba=StringVar()
                  #---------Data--------#
                  F1=Frame(root,bd=2,width=380,height=170,bg='#292421').place(x=1150,y=28)
                  l1=Label(F1,text=" Buyer's data: ",bg='#292421',fg='tomato',font=('tajawal',13,'bold')).place(x=1150,y=30)
                  l2=Label(F1,text=" Buyer's name",bg='#292421',fg='white',font=('tajawal',13,'bold')).place(x=1150,y=60)
                  l3=Label(F1,text=" Buyer's number",bg='#292421',fg='white',font=('tajawal',13,'bold')).place(x=1150,y=100)
                  l4=Label(F1,text=" Fatora's number",bg='#292421',fg='white',font=('tajawal',13,'bold')).place(x=1150,y=140)
                  e1=Entry(F1,justify='center',textvariable=self.name).place(x=1300,y=62)
                  e2=Entry(F1,justify='center',textvariable=self.phone).place(x=1300,y=102)
                  e3=Entry(F1,justify='center',textvariable=self.fatora).place(x=1300,y=142)        
                  #---------Fatora:bill--------#
                  l4=Label(F1,text="Fatora",bg='#292421',fg='gold',font=('tajawal',13,'bold')).place(x=1300,y=170)
                  F2=Frame(root,bd=2,width=380,height=480,bg='white').place(x=1150,y=200)
                  scrol_y= Scrollbar(F2,orient=VERTICAL)              
                  scrol_y.place(x=1150,y=200)
                  self.textarea=Text(F2,yscrollcommand=scrol_y.set,width=50,height=30)
                  scrol_y.config(command=self.textarea.yview)
                  self.textarea.place(x=1168,y=200)
                  #____________Price____________#
                  F3=Frame(root,bd=2,width=680,height=130,bg='#292421').place(x=838,y=650)
                  btn1=Button(F3,text='save fatora',font=('tajawal'),width=10,height=1,bg='#DBA901',command=self.file_save).place(x=1130,y=660)
                  btn2=Button(F3,text='Count',font='tajawal',width=10,height=1,bg='#DBA901',command=self.total).place(x=1388,y=660)
                  btn3=Button(F3,text='Import Fatora',font='tajawal',width=10,height=1,bg='#DBA901',command=self.import_fatora).place(x=1388,y=715)
                  btn4=Button(F3,text='Clear',font='tajawal',width=10,height=1,bg='#DBA901',command=self.clear).place(x=1260,y=660)
                  btn5=Button(F3,text='Exit Program',font='tajawal',width=10,height=1,bg='#DBA901',command=self.iExit).place(x=1260,y=715)
                  btn6=Button(F3,text='search fatora',font=('tajawal'),width=10,height=1,bg='#DBA901',command=self.file_find).place(x=1130,y=715)                
                  btn7=Button(root,text='The legumes',font=('tajawal',13,'bold'),bg='#292421',fg='gold',command=self.legummes).place(x=140,y=30)
                  btn8=Button(root,text='Home Supllies',font=('tajawal',13,'bold'),bg='#292421',fg='gold',command=self.adooat).place(x=560,y=30)
                  btn9=Button(root,text='Electrical Equiment',font=('tajawal',13,'bold'),bg='#292421',fg='gold',command=self.electicc).place(x=960,y=30)
                  l5=Label(F3,text='count of legumes',font=('tajawal',10,'bold'),bg='#292421',fg='gold').place(x=840,y=670)
                  l6=Label(F3,text='count of home supllies ',font=('tajawal',10,'bold'),bg='#292421',fg='gold').place(x=840,y=700)
                  l7=Label(F3,text='count of electrical equip',font=('tajawal',10,'bold'),bg='#292421',fg='gold').place(x=840,y=730)
                  e4=Entry(F3,textvariable=self.bacoliat,width=18).place(x=1000,y=670)
                  e5=Entry(F3,textvariable=self.adoat,width=18).place(x=1000,y=700)
                  e6=Entry(F3,textvariable=self.kahraba,width=18).place(x=1000,y=730)
                  self.welcome()
                  #___________item of legumes______#
                  #___ÇÑÒ__ÈÑÛá__ÝÇÕæáíÇ__ÚÏÓ__ãÚßÑæäÉ__ÝÑíßÉ__ÍãÕ__Ýæá__ãáÍ__ÓßÑ__ÝáÝá ÇÓæÏ__ÝáÝá ÇÍãÑ__áæÈíÇ__ÇáÇÏãÇãí__ÞãÍ
                  #___ÔÚíÑ__ÔæÝÇä__ÏÑÉ
              def legummes(self):
                  F4=Frame(root,bd=2,width=395,height=750,bg='#292421').place(x=1,y=30)
                  l8=Label(F4,text='The legumes',font=('tajawal',13,'bold'),bg='#292421',fg='gold').place(x=140,y=30)
                  l9=Label(F4,text='Rice',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=60)
                  l10=Label(F4,text='Bulgur',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=90)
                  l11=Label(F4,text='Beans',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=130)
                  l12=Label(F4,text='Lentils',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=170)
                  l13=Label(F4,text='Pasta',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=210)
                  l14=Label(F4,text='Freekeh',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=250)
                  l15=Label(F4,text='Chickpeas',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=290)
                  l16=Label(F4,text='Foul',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=330)
                  l17=Label(F4,text='Salt',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=370)
                  l18=Label(F4,text='Sugar',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=410)
                  l19=Label(F4,text='Black Pepper',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=450)
                  l20=Label(F4,text='Red Pepper',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=490)
                  l21=Label(F4,text='Green lobia',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=530)
                  l22=Label(F4,text='White lobia',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=570)
                  l23=Label(F4,text='Wheat',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=610)
                  l24=Label(F4,text='Barley',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=650)
                  l25=Label(F4,text='Oats',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=690)
                  l26=Label(F4,text='Corn',font=('tajawal',11),bg='#292421',fg='tomato').place(x=20,y=730)
                  e7=Entry(F4,width=12,textvariable=self.e7).place(x=220,y=60)
                  e8=Entry(F4,width=12,textvariable=self.e8).place(x=220,y=100)
                  e9=Entry(F4,width=12,textvariable=self.e9).place(x=220,y=140)
                  e10=Entry(F4,width=12,textvariable=self.e10).place(x=220,y=180)
                  e11=Entry(F4,width=12,textvariable=self.e11).place(x=220,y=220)
                  e12=Entry(F4,width=12,textvariable=self.e12).place(x=220,y=260)
                  e13=Entry(F4,width=12,textvariable=self.e13).place(x=220,y=300)
                  e14=Entry(F4,width=12,textvariable=self.e14).place(x=220,y=340)
                  e15=Entry(F4,width=12,textvariable=self.e15).place(x=220,y=380)
                  e16=Entry(F4,width=12,textvariable=self.e16).place(x=220,y=420)
                  e17=Entry(F4,width=12,textvariable=self.e17).place(x=220,y=460)
                  e18=Entry(F4,width=12,textvariable=self.e18).place(x=220,y=500)
                  e19=Entry(F4,width=12,textvariable=self.e20).place(x=220,y=540)
                  e20=Entry(F4,width=12,textvariable=self.e21).place(x=220,y=580)
                  e21=Entry(F4,width=12,textvariable=self.e22).place(x=220,y=620)
                  e22=Entry(F4,width=12,textvariable=self.e23).place(x=220,y=660)
                  e23=Entry(F4,width=12,textvariable=self.e24).place(x=220,y=700)
                  e24=Entry(F4,width=12,textvariable=self.e25).place(x=220,y=740)
                  #_________items of home supllies_____#
                  #___ãÕÝÇÉ__ÕÍä__ßÇÓ__ÇÈÑíÞ__Óßíä__Ôæß__ØäÌÑÉ__ÓáÉ__ãáÇÚÞ__ÕíäíÉ__æÚÇÁ ÇáÎáØ__ÝÊÇÍÉ ÚáÈ__ãÞÔÑÉ
                  #___áæÍ ÇáÊÞØíÚ__ÍÝÇÑÉ__ÓáÉ ÞãÇãÉ__ãäÝÖÉ__ÇßíÇÓ
              def adooat(self):
                  F5=Frame(root,bd=2,width=435,height=750,bg='#292421').place(x=400,y=30)
                  l27=Label(F5,text='Home Supllies',font=('tajawal',13,'bold'),bg='#292421',fg='gold').place(x=560,y=30)
                  l28=Label(F5,text='Colander',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=50)
                  l29=Label(F5,text='Plate',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=90)
                  l30=Label(F5,text='Cup',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=130)
                  l31=Label(F5,text='Kattle',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=170)
                  l32=Label(F5,text='Fork',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=210)
                  l33=Label(F5,text='Knife',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=250)
                  l34=Label(F5,text='A pot',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=290)
                  l35=Label(F5,text='Basket',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=330)
                  l36=Label(F5,text='Spoon',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=370)
                  l37=Label(F5,text='Tray',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=410)
                  l38=Label(F5,text='Mixing Bowl',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=450)
                  l39=Label(F5,text='Can Opener',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=490)
                  l40=Label(F5,text='Peeler',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=530)
                  l41=Label(F5,text='Chopping board',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=570)
                  l42=Label(F5,text='Excavator',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=610)
                  l43=Label(F5,text='Trash Basket',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=650)
                  l44=Label(F5,text='Ashtray',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=690)
                  l45=Label(F5,text='Bags',font=('tajawal',11),bg='#292421',fg='tomato').place(x=440,y=730)
                  e25=Entry(F5,width=12,textvariable=self.e25).place(x=640,y=60)
                  e26=Entry(F5,width=12,textvariable=self.e26).place(x=640,y=100)
                  e27=Entry(F5,width=12,textvariable=self.e27).place(x=640,y=140)
                  e28=Entry(F5,width=12,textvariable=self.e28).place(x=640,y=180)
                  e29=Entry(F5,width=12,textvariable=self.e29).place(x=640,y=220)
                  e30=Entry(F5,width=12,textvariable=self.e30).place(x=640,y=260)
                  e31=Entry(F5,width=12,textvariable=self.e31).place(x=640,y=300)
                  e32=Entry(F5,width=12,textvariable=self.e32).place(x=640,y=340)
                  e33=Entry(F5,width=12,textvariable=self.e33).place(x=640,y=380)
                  e34=Entry(F5,width=12,textvariable=self.e34).place(x=640,y=420)
                  e35=Entry(F5,width=12,textvariable=self.e35).place(x=640,y=460)
                  e36=Entry(F5,width=12,textvariable=self.e36).place(x=640,y=500)
                  e37=Entry(F5,width=12,textvariable=self.e37).place(x=640,y=540)
                  e38=Entry(F5,width=12,textvariable=self.e38).place(x=640,y=580)
                  e39=Entry(F5,width=12,textvariable=self.e39).place(x=640,y=620)
                  e40=Entry(F5,width=12,textvariable=self.e40).place(x=640,y=660)
                  e41=Entry(F5,width=12,textvariable=self.e41).place(x=640,y=700)
                  e42=Entry(F5,width=12,textvariable=self.e42).place(x=640,y=740)
                  #----------items of electrical equiment-------------#
                  #___ãßäÓÉ__ÊáÝÒíæä__ÛÓÇáÉ__ãßÑæíÝ__ÎáÇØ__ÝÑä ÛÇÒ__ãÞáÇÉ ßåÑÈÇÁ__ãÑæÍÉ ÓÞÝ__ãÑæÍÉ ÇÑÖíÉ__ÊáÝÒíæä 32__ÊáÝÒíæä43
                  #___ÝáÊÑ ãÇÁ__ÛÓÇáÉ ÇæÊæ__ãßæÇÉ__ÊáÇÌÉ
              def electicc(self):       
                  F6=Frame(root,bd=2,width=310,height=630,bg='#292421').place(x=838,y=30)
                  l46=Label(F6,text='Electrical Equiment',font=('tajawal',13,'bold'),bg='#292421',fg='gold').place(x=960,y=30)
                  l47=Label(F6,text='Broom',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=50)
                  l48=Label(F6,text='TV',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=90)
                  l49=Label(F6,text='Washing Machine',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=130)
                  l50=Label(F6,text='Microwave',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=170)    
                  l51=Label(F6,text='Blender',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=210)        
                  l52=Label(F6,text='Gas Stove',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=250)
                  l53=Label(F6,text='Electric Pan',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=290)
                  l54=Label(F6,text='Ceiling Fan',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=330)
                  l55=Label(F6,text='Floor Fan',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=370)
                  l56=Label(F6,text='32 TV',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=410)
                  l57=Label(F6,text='43 TV',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=450)
                  l58=Label(F6,text='Water Filter',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=490)
                  l59=Label(F6,text='Auto Washing Machine',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=530)
                  l60=Label(F6,text='Iron',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=570)
                  l61=Label(F6,text='Refrigerator',font=('tajawal',11),bg='#292421',fg='tomato').place(x=840,y=610)
                  e43=Entry(F6,width=12,textvariable=self.e43).place(x=1040,y=60)
                  e44=Entry(F6,width=12,textvariable=self.e44).place(x=1040,y=100)
                  e45=Entry(F6,width=12,textvariable=self.e45).place(x=1040,y=140)
                  e46=Entry(F6,width=12,textvariable=self.e46).place(x=1040,y=180)
                  e47=Entry(F6,width=12,textvariable=self.e47).place(x=1040,y=220)
                  e48=Entry(F6,width=12,textvariable=self.e48).place(x=1040,y=260)
                  e49=Entry(F6,width=12,textvariable=self.e49).place(x=1040,y=300)
                  e50=Entry(F6,width=12,textvariable=self.e50).place(x=1040,y=340)
                  e51=Entry(F6,width=12,textvariable=self.e51).place(x=1040,y=380)
                  e52=Entry(F6,width=12,textvariable=self.e52).place(x=1040,y=420)
                  e53=Entry(F6,width=12,textvariable=self.e53).place(x=1040,y=460)
                  e54=Entry(F6,width=12,textvariable=self.e54).place(x=1040,y=500)
                  e55=Entry(F6,width=12,textvariable=self.e55).place(x=1040,y=540)
                  e56=Entry(F6,width=12,textvariable=self.e56).place(x=1040,y=580)
                  e57=Entry(F6,width=12,textvariable=self.e57).place(x=1040,y=620)
              def total(self):
                  self.price_of_bacolient=(
                  (self.e7.get()*1)+   
                  (self.e8.get()*1.5)+         
                  (self.e9.get()*0.5)+       
                  (self.e10.get()*1)+         
                  (self.e11.get()*1.5)+     
                  (self.e12.get()*2)+        
                  (self.e13.get()*2)+         
                  (self.e14.get()*1)+   
                  (self.e15.get()*1)+     
                  (self.e16.get()*1.5)+       
                  (self.e17.get()*1)+         
                  (self.e18.get()*1.5)+         
                  (self.e19.get()*1)+         
                  (self.e20.get()*1.5)+       
                  (self.e21.get()*1)+         
                  (self.e22.get()*2)+       
                  (self.e23.get()*1)+      
                  (self.e24.get()*2))        
                  self.bacoliat.set(str(self.price_of_bacolient)+"$")
                  self.price_of_adoat=(
                  (self.e25.get()*3)+    
                  (self.e26.get()*50)+         
                  (self.e27.get()*7)+       
                  (self.e28.get()*4)+       
                  (self.e29.get()*15)+     
                  (self.e30.get()*11)+     
                  (self.e31.get()*20)+         
                  (self.e32.get()*10)+    
                  (self.e33.get()*15)+     
                  (self.e34.get()*14)+     
                  (self.e35.get()*23)+         
                  (self.e36.get()*13)+        
                  (self.e37.get()*14)+     
                  (self.e38.get()*15)+       
                  (self.e39.get()*13)+       
                  (self.e40.get()*21)+      
                  (self.e41.get()*10)+      
                  (self.e42.get()*13))
                  self.adoat.set(str(self.price_of_adoat)+" $ ")
                  self.price_of_kahraba=(
                  (self.e43.get()*30)+     
                  (self.e44.get()*140)+
                  (self.e45.get()*300)+
                  (self.e46.get()*40)+      
                  (self.e47.get()*15)+       
                  (self.e48.get()*110)+  
                  (self.e49.get()*20)+      
                  (self.e50.get()*10)+       
                  (self.e51.get()*15)+  
                  (self.e52.get()*140)+     
                  (self.e53.get()*230)+ 
                  (self.e54.get()*130)+         
                  (self.e55.get()*135)+        
                  (self.e56.get()*148)+     
                  (self.e57.get()*155))       
                  self.kahraba.set(str(self.price_of_kahraba)+" $ ")
                  self.all=(self.price_of_bacolient+self.price_of_adoat+self.price_of_kahraba)
                  #-------------------------------#         
              def welcome(self):
                  self.textarea.delete('1.0',END)
                  self.textarea.insert(END,"\t Welcome To Super Market")
                  self.textarea.insert(END,"\n====================================")
                  self.textarea.insert(END,f" \n\t B.NUM  :{self.fatora.get()}")
                  self.textarea.insert(END,f"\n\t NAME   :{self.name.get()}")
                  self.textarea.insert(END,f"\n\t PHONE  :{self.phone.get()}")
                  self.textarea.insert(END,"\n====================================")
                  self.textarea.insert(END,f"\nPurchases\t    number\t       price ")
                  self.textarea.insert(END,"\n====================================")
              def clear(self):
                  self.textarea.delete('1.0',END)
              def import_fatora(self):
                  self.welcome()
                  if self.e7.get()!=0:     
                     self.textarea.insert(END,f"\nRice\t        {self.e7.get()}\t            {self.e7.get()*1}$")
                  if self.e8.get()!=0:     
                     self.textarea.insert(END,f"\nBulgur\t        {self.e8.get()}\t            {self.e8.get()*1.5}$")
                  if self.e9.get()!=0:     
                     self.textarea.insert(END,f"\nBeans\t        {self.e9.get()}\t            {self.e9.get()*0.5}$")
                  if self.e10.get()!=0:     
                     self.textarea.insert(END,f"\nlentils\t        {self.e10.get()}\t            {self.e10.get()*1}$")
                  if self.e11.get()!=0:     
                     self.textarea.insert(END,f"\nPasta\t        {self.e11.get()}\t            {self.e11.get()*1.5}$")
                  if self.e12.get()!=0:     
                     self.textarea.insert(END,f"\nFreekeh\t        {self.e12.get()}\t            {self.e12.get()*2}$")
                  if self.e13.get()!=0:     
                     self.textarea.insert(END,f"\nChickpeas\t      {self.e13.get()}\t            {self.e13.get()*2}$")
                  if self.e14.get()!=0:     
                     self.textarea.insert(END,f"\nFoul\t        {self.e14.get()}\t            {self.e14.get()*1}$")
                  if self.e15.get()!=0:     
                     self.textarea.insert(END,f"\nSalt\t        {self.e15.get()}\t            {self.e15.get()*1}$")
                  if self.e16.get()!=0:     
                     self.textarea.insert(END,f"\nSugar\t        {self.e16.get()}\t            {self.e16.get()*1.5}$")
                  if self.e17.get()!=0:     
                     self.textarea.insert(END,f"\nBlack Pepper\t   {self.e17.get()}\t            {self.e17.get()*1}$")
                  if self.e18.get()!=0:     
                     self.textarea.insert(END,f"\nRed Pepper\t     {self.e18.get()}\t            {self.e18.get()*1.5}$")
                  if self.e19.get()!=0:     
                     self.textarea.insert(END,f"\nGreen Lobia\t    {self.e19.get()}\t            {self.e19.get()*1}$")
                  if self.e20.get()!=0:     
                     self.textarea.insert(END,f"\nWhite Lobia\t    {self.e20.get()}\t            {self.e20.get()*1.5}$")
                  if self.e21.get()!=0:     
                     self.textarea.insert(END,f"\nWheat\t        {self.e21.get()}\t            {self.e21.get()*1}$")
                  if self.e22.get()!=0:     
                     self.textarea.insert(END,f"\nBarley\t        {self.e22.get()}\t            {self.e22.get()*2}$")
                  if self.e23.get()!=0:     
                     self.textarea.insert(END,f"\nOats\t        {self.e23.get()}\t            {self.e23.get()*1}$")
                  if self.e24.get()!=0:     
                     self.textarea.insert(END,f"\nCorn\t        {self.e24.get()}\t            {self.e24.get()*2}$")
                  if self.e25.get()!=0:     
                     self.textarea.insert(END,f"\nColander\t       {self.e25.get()}\t            {self.e25.get()*3}$")
                  if self.e26.get()!=0:     
                     self.textarea.insert(END,f"\nPlate\t        {self.e26.get()}\t            {self.e26.get()*50}$")
                  if self.e27.get()!=0:     
                     self.textarea.insert(END,f"\nCup\t        {self.e27.get()}\t            {self.e27.get()*7}$")
                  if self.e28.get()!=0:     
                     self.textarea.insert(END,f"\nKattle\t        {self.e28.get()}\t            {self.e28.get()*4}$")
                  if self.e29.get()!=0:     
                     self.textarea.insert(END,f"\nFork\t        {self.e29.get()}\t            {self.e29.get()*15}$")
                  if self.e30.get()!=0:     
                     self.textarea.insert(END,f"\nKnife\t        {self.e30.get()}\t            {self.e30.get()*11}$")
                  if self.e31.get()!=0:     
                     self.textarea.insert(END,f"\nA Pot\t        {self.e31.get()}\t            {self.e31.get()*20}$")
                  if self.e32.get()!=0:     
                     self.textarea.insert(END,f"\nBasket\t        {self.e32.get()}\t            {self.e32.get()*10}$")
                  if self.e33.get()!=0:     
                     self.textarea.insert(END,f"\nSpoon\t        {self.e33.get()}\t            {self.e33.get()*15}$")
                  if self.e34.get()!=0:     
                     self.textarea.insert(END,f"\nTray\t        {self.e34.get()}\t            {self.e34.get()*14}$")
                  if self.e35.get()!=0:     
                     self.textarea.insert(END,f"\nMixing Bowl\t    {self.e35.get()}\t            {self.e35.get()*23}$")
                  if self.e36.get()!=0:     
                     self.textarea.insert(END,f"\nCan Opener\t     {self.e36.get()}\t            {self.e36.get()*13}$")
                  if self.e37.get()!=0:     
                     self.textarea.insert(END,f"\nPeeler\t        {self.e37.get()}\t            {self.e37.get()*14}$")
                  if self.e38.get()!=0:     
                     self.textarea.insert(END,f"\nChopping Board\t {self.e38.get()}\t            {self.e38.get()*15}$")
                  if self.e39.get()!=0:     
                     self.textarea.insert(END,f"\nExcavator\t      {self.e39.get()}\t            {self.e39.get()*13}$")
                  if self.e40.get()!=0:     
                     self.textarea.insert(END,f"\nTrash Basket\t   {self.e40.get()}\t             {self.e40.get()*21}$")
                  if self.e41.get()!=0:     
                     self.textarea.insert(END,f"\nAshtray\t        {self.e41.get()}\t            {self.e41.get()*10}$")
                  if self.e42.get()!=0:     
                     self.textarea.insert(END,f"\nBags\t        {self.e42.get()}\t            {self.e42.get()*13}$")
                  if self.e43.get()!=0:     
                     self.textarea.insert(END,f"\nBroom\t        {self.e43.get()}\t            {self.e43.get()*30}$")
                  if self.e44.get()!=0:     
                     self.textarea.insert(END,f"\nTV\t        {self.e44.get()}\t            {self.e44.get()*140}$")
                  if self.e45.get()!=0:     
                     self.textarea.insert(END,f"\nWashing Machine\t{self.e45.get()}\t            {self.e45.get()*300}$")
                  if self.e46.get()!=0:     
                     self.textarea.insert(END,f"\nMicrowave\t      {self.e46.get()}\t            {self.e46.get()*40}$")
                  if self.e47.get()!=0:     
                     self.textarea.insert(END,f"\nBlender\t        {self.e47.get()}\t            {self.e47.get()*15}$")
                  if self.e48.get()!=0:     
                     self.textarea.insert(END,f"\nGas Stove\t      {self.e48.get()}\t            {self.e48.get()*110}$")
                  if self.e49.get()!=0:     
                     self.textarea.insert(END,f"\nElectric Pan\t   {self.e49.get()}\t            {self.e49.get()*20}$")
                  if self.e50.get()!=0:     
                     self.textarea.insert(END,f"\nCeiling Fan\t    {self.e50.get()}\t            {self.e50.get()*10}$")
                  if self.e51.get()!=0:     
                     self.textarea.insert(END,f"\nFloor Fan\t      {self.e51.get()}\t            {self.e51.get()*15}$")
                  if self.e52.get()!=0:     
                     self.textarea.insert(END,f"\n32 TV\t        {self.e52.get()}\t            {self.e52.get()*140}$")
                  if self.e53.get()!=0:     
                     self.textarea.insert(END,f"\n43 TV\t        {self.e53.get()}\t            {self.e53.get()*230}$")
                  if self.e54.get()!=0:     
                     self.textarea.insert(END,f"\nWater Filter\t   {self.e54.get()}\t            {self.e54.get()*130}$")
                  if self.e55.get()!=0:     
                     self.textarea.insert(END,f"\nAuto Washing\t   {self.e55.get()}\t            {self.e55.get()*135}$")
                  if self.e56.get()!=0:     
                     self.textarea.insert(END,f"\nIron\t        {self.e56.get()}\t            {self.e56.get()*148}$")
                  if self.e57.get()!=0:     
                     self.textarea.insert(END,f"\nRefrigerator\t   {self.e57.get()}\t            {self.e57.get()*155}$")  
                     self.textarea.insert(END,"\n====================================")
                     self.textarea.insert(END,f"\n\t               Total: {self.all}$")
                     self.file_save()
              def iExit(self):
                  iExit= messagebox.askyesno("Super Market Programe",
                                             "Do you want to exit ")
                  if iExit >0:
                     self.root.destroy()
                     return          
              def file_save(self):     
                  file_save=messagebox.askyesno("Save Fatora",
                                                "Do you want to save?")
                  if file_save > 0:
                     file_save=asksaveasfile(mode='w',defaultextension=".txt")
                     file_save.write(self.textarea.get(0.0,END))
                     file_save.close()
                     return
              def file_find(self):
                  file_find=filedialog.askopenfilename(initialdir='/')
                  fh=open(file_find,'r')
                  self.read=fh.read()
                  self.textarea.delete('1.0',END)
                  self.textarea.insert(END,self.read)
          Super(root)
          root.mainloop()
          return    
def about1(): 
    messagebox.showinfo("Super Market Project",
                        "The Devlopers are: \n"
                        "1.Mohamed Wael Amin Abd Alhamid Shaheen\n"
                        "2.Abd Alrahman Hesham Abo Alfath Shousha\n"
                        "3.Salma Osama Ahmed Mohamed Alsayed\n"
                        "4.Somaia Moustafa Abd Alaziz AlKhadrawy \n"
                        "5.Mymana Hussein Abd AlHamid Hussein")                                                              
def about2():
    messagebox.showinfo("Project overview",
                        "Super Market Project In Tkinter python")
def Exit():
    Exit=messagebox.askyesno("Super Market Programe",
                              "Do you want to exit ?")
    if Exit >0:
       pro.destroy()
       return    
def Open1():
    webbrowser.open_new(u1)
def Open2():
    webbrowser.open_new(u2)
def Open3():
    webbrowser.open_new(u3)             
pro=Tk()
pro.configure(background = 'white') 
pro.resizable(width=False,height=False)
pro.geometry('800x450+280+50')
pro.title("SUPERMARKET")
pro.iconbitmap('D:\\icone.ico')
photo=PhotoImage(file="D:\\store.png")
imo = Label(pro,image=photo).place(x=200,y=80)
FF1=Frame(pro, width=230,height=420,bg='#292421').place(x=570, y=30)
ll1=Label(pro,text='Super Market System',fg='gold',bg='black',font=('tajwal',16,'bold')).pack(fill=X)
tt1=Label(FF1,text='Super Market System',bg='#292421',fg='white',font=('tajwal',12,'bold')).place(x=602,y=40)
tt2=Label(FF1,text='Devoloped by The Team',bg='#292421',fg='white',font=('tajwal',12,'bold')).place(x=602,y=80)
tt3=Label(FF1,text='Contact Us',bg='#292421',fg='white',font=('tajwal',12,'bold')).place(x=602,y=120)

bb1=Button(FF1,text='Our account on Facebook',width=26,fg='black',bg='#DBA901',font=('tajwal',11,'bold'),command=Open1).place(x=572,y=170)
bb2=Button(FF1,text='Our account on Telegrame',width=26,fg='black',bg='#DBA901',font=('tajwal',11,'bold'),command=Open2).place(x=572,y=220)
bb3=Button(FF1,text='Our Channel on YouTube',width=26,fg='black',bg='#DBA901',font=('tajwal',11,'bold'),command=Open3).place(x=572,y=270)
bb4=Button(FF1,text='Devolopers overview',width=26,fg='black',bg='#DBA901',font=('tajwal',11,'bold'),command=about1).place(x=572,y=320)
bb5=Button(FF1,text='Project overview',width=26,fg='black',bg='#DBA901',font=('tajwal',11,'bold'),command=about2).place(x=572,y=370)
bb6=Button(FF1,text='Exit the program',width=26,fg='black',bg='#DBA901',font=('tajwal',11,'bold'),command=Exit).place(x=572,y=420)

FF2=Frame(pro, width=570,height=120,bg='#292421').place(x=0, y=330)
photo1=PhotoImage(file="D:\\log.png")
imo1 = Label(pro,image=photo1,bg='#292421').place(x=450,y=330)
ll2=Label(FF2,text='User Name',fg='gold',bg='#292421',font=('tajwal',16,'bold')).place(x=320,y=350)
ll3=Label(FF2,text='Password',fg='gold',bg='#292421',font=('tajwal',16,'bold')).place(x=320,y=400)
enn1=Entry(FF2,font=('tajwal',12),justify='center').place(x=120,y=350)
enn2=Entry(FF2,font=('tajwal',12),justify='center').place(x=120,y=400)
bb7=Button(FF2,text='Login',bg='#DBA901',font=('tajwal',12),width=10,height=4,command=log).place(x=5,y=350)
u1='https:///www.Facebook.com/username'
u2='url-telegram'
u3='url-youtube'
pro.mainloop()