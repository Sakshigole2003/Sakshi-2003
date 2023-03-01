from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

# functions


def reset():
    textReceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_sabji.set('0')
    e_kabab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_tea.set('0')
    e_coffee.set('0')
    e_milk.set('0')
    e_lassi.set('0')
    e_faluda.set('0')
    e_jaljeera.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_colddrinks.set('0')

    e_chocolate.set('0')
    e_butterscotch.set('0')
    e_oreo.set('0')
    e_kitkat.set('0')
    e_redvelvet.set('0')
    e_blackforest.set('0')
    e_vanilla.set('0')
    e_strawberry.set('0')
    e_pineapple.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textkabab.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)

    texttea.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textmilk.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textchocolate.config(state=DISABLED)
    textbutterscotch.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textredvelvet.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textstrawberry.config(state=DISABLED)
    textpineapple.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='69Gbw57E0CgIWQROUA3kcj8LtxTqsyZJXzvde4YKPopmhn2flarwcBMWfZy4FmhAxUdjnGabSYJg7iLo'
            url='https://www.fast2sms.com/dev/bulk'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')

        root2=Toplevel()

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')
        
        logoImage=PhotoImage(file='sender.png')
        label=Label(root2,image=logoImage,bg='red4')
        label.pack(pady=5)

    

        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')
        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
        if costofcakesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE
                          ,command=send_msg)
        sendButton.pack(pady=5)
    
        root2.mainloop()

def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')


def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')

        if e_daal.get()!='0':
            textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')

        if e_fish.get()!='0':
            textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 30}\n\n')

        if e_kabab.get() != '0':
            textReceipt.insert(END, f'Kabab:\t\t\t{int(e_kabab.get()) * 50}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 100}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 40}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 120}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

        if e_tea.get() != '0':
            textReceipt.insert(END, f'Tea:\t\t\t{int(e_tea.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_milk.get() != '0':
            textReceipt.insert(END, f'Milk:\t\t\t{int(e_milk.get()) * 80}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 30}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 40}\n\n')

        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 60}\n\n')

        if e_roohafza.get() != '0':
            textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 20}\n\n')

        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 50}\n\n')

        if e_colddrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_colddrinks.get()) * 80}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Choclate:\t\t\t{int(e_chocolate.get()) * 400}\n\n')

        if e_butterscotch.get() != '0':
            textReceipt.insert(END, f'Butterscotch:\t\t\t{int(e_butterscotch.get()) * 300}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'oreo:\t\t\t{int(e_oreo.get()) * 500}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 450}\n\n')

        if e_redvelvet.get() != '0':
            textReceipt.insert(END, f'Red Velvet:\t\t\t{int(e_redvelvet.get()) * 800}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 620}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 700}\n\n')

        if e_strawberry.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 550}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_roti.get())
        item2=int(e_daal.get())
        item3=int(e_fish.get())
        item4 = int(e_sabji.get())
        item5 = int(e_kabab.get())
        item6 = int(e_chawal.get())
        item7 = int(e_mutton.get())
        item8 = int(e_paneer.get())
        item9 = int(e_chicken.get())

        item10 = int(e_tea.get())
        item11 = int(e_coffee.get())
        item12 = int(e_milk.get())
        item13 = int(e_lassi.get())
        item14 = int(e_faluda.get())
        item15 = int(e_jaljeera.get())
        item16 = int(e_roohafza.get())
        item17 = int(e_shikanji.get())
        item18 = int(e_colddrinks.get())

        item19 = int(e_chocolate.get())
        item20 = int(e_butterscotch.get())
        item21 = int(e_oreo.get())
        item22 = int(e_kitkat.get())
        item23 = int(e_redvelvet.get())
        item24 = int(e_blackforest.get())
        item25 = int(e_vanilla.get())
        item26 = int(e_strawberry.get())
        item27 = int(e_pineapple.get())

        priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) \
                    + (item8 * 100) + (item9 * 120)

        priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 80)

        priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

        costoffoodvar.set(str(priceofFood)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        costofcakesvar.set(str(priceofCakes)+ ' Rs')

        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')


def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def sabji():
    if var4.get()==1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')

def kabab():
    if var5.get()==1:
        textkabab.config(state=NORMAL)
        textkabab.delete(0,END)
        textkabab.focus()
    else:
        textkabab.config(state=DISABLED)
        e_kabab.set('0')

def chawal():
    if var6.get()==1:
        textchawal.config(state=NORMAL)
        textchawal.delete(0,END)
        textchawal.focus()
    else:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')

def mutton():
    if var7.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')

def paneer():
    if var8.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def chicken():
    if var9.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def tea():
    if var10.get()==1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')

def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def milk():
    if var12.get()==1:
        textmilk.config(state=NORMAL)
        textmilk.delete(0,END)
        textmilk.focus()
    else:
        textmilk.config(state=DISABLED)
        e_milk.set('0')

def lassi():
    if var13.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def faluda():
    if var14.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')

def jaljeera():
    if var15.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

def roohafza():
    if var16.get()==1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')

def shikanji():
    if var17.get()==1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')

def colddrinks():
    if var18.get()==1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.delete(0,END)
        textcolddrinks.focus()
    else:
        textcolddrinks.config(state=DISABLED)
        e_colddrinks.set('0')


def chocolate():
    if var19.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')

def butterscotch():
    if var20.get()==1:
        textbutterscotch.config(state=NORMAL)
        textbutterscotch.delete(0,END)
        textbutterscotch.focus()
    else:
        textbutterscotch.config(state=DISABLED)
        e_butterscotch.set('0')

def oreo():
    if var21.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def kitkat():
    if var22.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def redvelvet():
    if var23.get()==1:
        textredvelvet.config(state=NORMAL)
        textredvelvet.delete(0,END)
        textredvelvet.focus()
    else:
        textredvelvet.config(state=DISABLED)
        e_redvelvet.set('0')

def blackforest():
    if var24.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def vanilla():
    if var25.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')

def strawberry():
    if var26.get()==1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.delete(0,END)
        textstrawberry.focus()
    else:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')

def pineapple():
    if var27.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


root=Tk()

root.geometry('1270x690+0+0')
root.title('Restaurant Management System by Sakshi')
root.config(bg='firebrick4')


topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='RESTAURANT MANAGEMENT SYSTEM',font=("arial 30 bold"),fg='yellow',bd=9,bg='red4')
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4',width=42)
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font="arial 19 bold",bd=10,relief=RIDGE,fg='red4',bg='white')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font="arial 19 bold",bd=10,relief=RIDGE,fg='red4',bg='white')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font="arial 19 bold",bd=10,relief=RIDGE,fg='red4',bg='white')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_sabji=StringVar()
e_kabab=StringVar()
e_chawal=StringVar()
e_mutton=StringVar()
e_paneer=StringVar()
e_chicken=StringVar()

e_tea=StringVar()
e_coffee=StringVar()
e_milk=StringVar()
e_lassi=StringVar()
e_faluda=StringVar()
e_jaljeera=StringVar()
e_roohafza=StringVar()
e_shikanji=StringVar()
e_colddrinks=StringVar()

e_chocolate=StringVar()
e_butterscotch=StringVar()
e_oreo=StringVar()
e_kitkat=StringVar()
e_redvelvet=StringVar()
e_blackforest=StringVar()
e_vanilla=StringVar()
e_strawberry=StringVar()
e_pineapple=StringVar()


costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()



e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_sabji.set('0')
e_kabab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_paneer.set('0')
e_chicken.set('0')

e_tea.set('0')
e_coffee.set('0')
e_milk.set('0')
e_lassi.set('0')
e_faluda.set('0')
e_jaljeera.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_colddrinks.set('0')

e_chocolate.set('0')
e_butterscotch.set('0')
e_oreo.set('0')
e_kitkat.set('0')
e_redvelvet.set('0')
e_blackforest.set('0')
e_vanilla.set('0')
e_strawberry.set('0')
e_pineapple.set('0')


#food

roti=Checkbutton(foodFrame,text='Roti',font="arial 18 bold",onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font="arial 18 bold",onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font="arial 18 bold",onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji',font="arial 18 bold",onvalue=1,offvalue=0,variable=var4,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kabab=Checkbutton(foodFrame,text='Kabab',font="arial 18 bold",onvalue=1,offvalue=0,variable=var5,command=kabab)
kabab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodFrame,text='Chawal',font="arial 18 bold",onvalue=1,offvalue=0,variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',font="arial 18 bold",onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font="arial 18 bold",onvalue=1,offvalue=0,variable=var8,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font="arial 18 bold",onvalue=1,offvalue=0,variable=var9,command=chicken)
chicken.grid(row=8,column=0,sticky=W)


#Entry fields for Food Items

textroti=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=3,column=1)

textkabab=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_kabab)
textkabab.grid(row=4,column=1)

textchawal=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_chawal)
textchawal.grid(row=5,column=1)

textmutton=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textpaneer=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=7,column=1)

textchicken=Entry(foodFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=8,column=1)

# drinks

tea=Checkbutton(drinksFrame,text='Tea',font="arial 18 bold",onvalue=1,offvalue=0,variable=var10,command=tea)
tea.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font="arial 18 bold",onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

milk=Checkbutton(drinksFrame,text='Milk',font="arial 18 bold",onvalue=1,offvalue=0,variable=var12,command=milk)
milk.grid(row=2,column=0,sticky=W)

lassi=Checkbutton(drinksFrame,text='Lassi',font="arial 18 bold",onvalue=1,offvalue=0,variable=var13,command=lassi)
lassi.grid(row=3,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font="arial 18 bold",onvalue=1,offvalue=0,variable=var14,command=faluda)
faluda.grid(row=4,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font="arial 18 bold",onvalue=1,offvalue=0,variable=var15,command=jaljeera)
jaljeera.grid(row=5,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Roohafza',font="arial 18 bold",onvalue=1,offvalue=0,variable=var16,command=roohafza)
roohafza.grid(row=6,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font="arial 18 bold",onvalue=1,offvalue=0,variable=var17,command=shikanji)
shikanji.grid(row=7,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold Drinks',font="arial 18 bold",onvalue=1,offvalue=0,variable=var18,command=colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)

# Entry fields for drinks items

texttea=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=0,column=1) 

textcoffee=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textmilk=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_milk)
textmilk.grid(row=2,column=1) 

textlassi=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=3,column=1) 

textfaluda=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=4,column=1) 

textjaljeera=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=5,column=1)

textroohafza=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=6,column=1)

textshikanji=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=7,column=1) 

textcolddrinks=Entry(drinksFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_colddrinks)
textcolddrinks.grid(row=8,column=1) 

# cakes

chocolate=Checkbutton(cakesFrame,text='Chocolate',font="arial 18 bold",onvalue=1,offvalue=0,variable=var19,command=chocolate)
chocolate.grid(row=0,column=0,sticky=W)

butterscotch=Checkbutton(cakesFrame,text='Butterscotch',font="arial 18 bold",onvalue=1,offvalue=0,variable=var20,command=butterscotch)
butterscotch.grid(row=1,column=0,sticky=W)

oreo=Checkbutton(cakesFrame,text='Oreo',font="arial 18 bold",onvalue=1,offvalue=0,variable=var21,command=oreo)
oreo.grid(row=2,column=0,sticky=W)

kitkat=Checkbutton(cakesFrame,text='Kitkat',font="arial 18 bold",onvalue=1,offvalue=0,variable=var22,command=kitkat)
kitkat.grid(row=3,column=0,sticky=W)

redvelvet=Checkbutton(cakesFrame,text='Red Velvet',font="arial 18 bold",onvalue=1,offvalue=0,variable=var23,command=redvelvet)
redvelvet.grid(row=4,column=0,sticky=W)

blackforest=Checkbutton(cakesFrame,text='Black Forest',font="arial 18 bold",onvalue=1,offvalue=0,variable=var24,command=blackforest)
blackforest.grid(row=5,column=0,sticky=W)

vanilla=Checkbutton(cakesFrame,text='Vanilla',font="arial 18 bold",onvalue=1,offvalue=0,variable=var25,command=vanilla)
vanilla.grid(row=6,column=0,sticky=W)

strawberry=Checkbutton(cakesFrame,text='Strawberry',font="arial 18 bold",onvalue=1,offvalue=0,variable=var26,command=strawberry)
strawberry.grid(row=7,column=0,sticky=W)

pineapple=Checkbutton(cakesFrame,text='Pineapple',font="arial 18 bold",onvalue=1,offvalue=0,variable=var27,command=pineapple)
pineapple.grid(row=8,column=0,sticky=W)

# entry fields for cakes items

textchocolate=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=0,column=1) 

textbutterscotch=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_butterscotch)
textbutterscotch.grid(row=1,column=1)

textoreo=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=2,column=1) 

textkitkat=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=3,column=1) 

textredvelvet=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_redvelvet)
textredvelvet.grid(row=4,column=1) 

textblackforest=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=5,column=1) 

textvanilla=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=6,column=1) 

textstrawberry=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_strawberry)
textstrawberry.grid(row=7,column=1) 

textpineapple=Entry(cakesFrame,font="arial 18 bold",bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=8,column=1) 

# costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font="arial 16 bold",bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font="arial 16 bold",bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=85)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font="arial 16 bold",bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font="arial 16 bold",bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=85)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font="arial 16 bold",bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font="arial 16 bold",bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=85)

labelSubtotal=Label(costFrame,text='Sub Total',font="arial 16 bold",bg='firebrick4',fg='white')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costFrame,font="arial 16 bold",bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3,padx=50)

labelServiceTax=Label(costFrame,text='Service Tax',font="arial 16 bold",bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font="arial 16 bold",bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=50)

labelTotalCost=Label(costFrame,text='Total Cost',font="arial 16 bold",bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font="arial 16 bold",bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=50)

# buttons

buttonTotal=Button(buttonFrame,text='Total',font="arial 14 bold",fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font="arial 14 bold",fg='white',bg='red4',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font="arial 14 bold",fg='white',bg='red4',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font="arial 14 bold",fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font="arial 14 bold",fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

# text area for receipt

textReceipt=Text(receiptFrame,font="arial 12 bold",bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

# calculator
operator=''  #7+9
def buttonClick(numbers):  #+
    global operator
    operator=operator+numbers #7+
    calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorfield.delete(0,END)

def answer():
    global operator
    result=str(eval(operator)) 
    calculatorfield.delete(0,END)   
    calculatorfield.insert(0,result)
    operator=''


calculatorfield=Entry(calculatorFrame,font="arial 16 bold",width=32,bd=4)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font="arial 16 bold",fg='yellow',bg='red4',bd=6,width=6,
command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font="arial 16 bold",fg='red4',bg='white',bd=6,width=6,
command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)


root.mainloop()