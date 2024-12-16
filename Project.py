from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurant Billing System")
        title=Label(self.root,text="Restaurant Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.samosa=IntVar()
        self.noodles=IntVar()
        self.chicken_tikka=IntVar()
        self.pakora=IntVar()
        self.chaat=IntVar()
        self.tomato_soup=IntVar()
        self.papad=IntVar()
        self.butter_chicken=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.paneer_masala=IntVar()
        self.palak_paneer=IntVar()
        self.dal=IntVar()
        self.bhature=IntVar()
        self.paneer_tikka=IntVar()
        self.aloo_tikki=IntVar()
        self.dahi_vada=IntVar()
        self.pav_bhaji=IntVar()
        self.bhel=IntVar()
        self.soup=IntVar()
        self.pakora1=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Restaurant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.samosa).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Paneer Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.paneer_tikka).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Chicken Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.chicken_tikka).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Vegetable Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.pakora).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Papdi Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.chaat).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Tomato Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.tomato_soup).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Masala Papad",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.papad).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        grocery=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Butter Chicken",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.butter_chicken).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="White Sauce Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Fried Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.rice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Paneer Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.paneer_masala).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Palak Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.palak_paneer).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Daal",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Chole Bhature",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.bhature).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        hygine=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Noodles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.noodles).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Aloo Tikki Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.aloo_tikki).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Dahi Vada",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.dahi_vada).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.pav_bhaji).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Bhel Puri",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.bhel).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.soup).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Paneer Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.pakora1).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summary",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_grocery=Label(billing_menu,text="Total Main Course Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)


        total_hygine=Label(billing_menu,text="Total Starter Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_snacks=Label(billing_menu,text="Food Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_grocery=Label(billing_menu,text="GST",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)




        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if self.c_name.get== "" or self.phone.get()== "":
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.samosa.get()*20
    self.no=self.paneer_tikka.get()*150
    self.la=self.chicken_tikka.get()*160
    self.ore=self.pakora.get()*20
    self.mu=self.chaat.get()*30
    self.si=self.tomato_soup.get()*60
    self.na=self.papad.get()*15
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(20)+" Rs")

    self.at=self.butter_chicken.get()*150
    self.pa=self.pasta.get()*120
    self.oi=self.paneer_masala.get()*130
    self.ri=self.rice.get()*100
    self.su=self.palak_paneer.get()*100
    self.te=self.bhature.get()*70
    self.da=self.dal.get()*100
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(20)+" Rs")

    self.so=self.noodles.get()*60
    self.sh=self.aloo_tikki.get()*60
    self.cr=self.pav_bhaji.get()*60
    self.lo=self.dahi_vada.get()*50
    self.fo=self.bhel.get()*30
    self.ma=self.soup.get()*80
    self.sa=self.pakora1.get()*20

    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(20)+" Rs")
    self.total_all_bill=(total_snacks_price +total_grocery_price +total_hygine_price +20 +20 +20)
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO ABES LOUNGE\n\tPhone-No.8368******")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.samosa.get()!=0:
        self.txtarea.insert(END,f"Samosa\t\t {self.samosa.get()}\t{self.nu}\n")
    if self.paneer_tikka.get()!=0:
        self.txtarea.insert(END,f"Paneer Tikka\t\t {self.paneer_tikka.get()}\t{self.no}\n")
    if self.chicken_tikka.get()!=0:
        self.txtarea.insert(END,f"Chicken Tikka\t\t {self.chicken_tikka.get()}\t{self.la}\n")
    if self.pakora.get()!=0:
        self.txtarea.insert(END,f"Vegetable Pakora\t\t {self.pakora.get()}\t{self.ore}\n")
    if self.chaat.get()!=0:
        self.txtarea.insert(END,f"Papdi Chaat\t\t {self.chaat.get()}\t{self.mu}\n")
    if self.tomato_soup.get()!=0:
        self.txtarea.insert(END,f"Tomata Soup\t\t {self.tomato_soup.get()}\t{self.si}\n")
    if self.papad.get()!=0:
        self.txtarea.insert(END,f"Masala Papad\t\t {self.papad.get()}\t{self.na}\n")
    if self.butter_chicken.get()!=0:
        self.txtarea.insert(END,f"Butter Chicken\t\t {self.butter_chicken.get()}\t{self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"White Sauce Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get()!=0:
        self.txtarea.insert(END,f"Fried Rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.paneer_masala.get()!=0:
        self.txtarea.insert(END,f"Paneer Masala\t\t {self.paneer_masala.get()}\t{self.oi}\n")
    if self.palak_paneer.get()!=0:
        self.txtarea.insert(END,f"Palak Paneer\t\t {self.palak_paneer.get()}\t{self.su}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.bhature.get()!=0:
        self.txtarea.insert(END,f"Chole Bhature\t\t {self.bhature.get()}\t{self.te}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.so}\n")
    if self.aloo_tikki.get()!=0:
        self.txtarea.insert(END,f"Aloo Tikki Chaat\t\t {self.aloo_tikki.get()}\t{self.sh}\n")
    if self.dahi_vada.get()!=0:
        self.txtarea.insert(END,f"Dahi Vada\t\t {self.dahi_vada.get()}\t{self.lo}\n")
    if self.pav_bhaji.get()!=0:
        self.txtarea.insert(END,f"Pav Bhaji\t\t {self.pav_bhaji.get()}\t{self.cr}\n")
    if self.bhel.get()!=0:
        self.txtarea.insert(END,f"Bhel Puri\t\t {self.bhel.get()}\t{self.fo}\n")
    if self.soup.get()!=0:
        self.txtarea.insert(END,f"Soup\t\t {self.soup.get()}\t{self.ma}\n")
    if self.pakora1.get()!=0:
        self.txtarea.insert(END,f"Paneer Pakora\t\t {self.pakora1.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Food Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total GST: {self.b.get()}\n")

    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.samosa.set(0)
        self.noodles.set(0)
        self.chicken_tikka.set(0)
        self.pakora.set(0)
        self.chaat.set(0)
        self.tomato_soup.set(0)
        self.papad.set(0)
        self.butter_chicken.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.paneer_masala.set(0)
        self.palak_paneer.set(0)
        self.dal.set(0)
        self.bhature.set(0)
        self.paneer_tikka.set(0)
        self.aloo_tikki.set(0)
        self.dahi_vada.set(0)
        self.pav_bhaji.set(0)
        self.bhel.set(0)
        self.soup.set(0)
        self.pakora1.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
