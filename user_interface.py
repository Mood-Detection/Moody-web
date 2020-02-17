from tkinter import *
import random
import tkinter.filedialog
from PIL import Image, ImageOps


def open_file():
          global open_file_name
          
          image_file_name = tkinter.filedialog.askopenfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
          open_file_name=PhotoImage(file=image_file_name)
          label_1.configure(image=open_file_name)
def original_image ():
          Image.open("C://Users//infinity//AppData//Local//Programs//Python//Python36//upload.png")
          size = (370, 250)
          fit_and_resized_image = ImageOps.fit(original_image, size, Image.ANTIALIAS)


Mood=['Happy','Angry','Fear','Sad','Neutral']
Angry = ['Leafy Green','Walnut','Banana','Greek Yogurt','Cottage Cheese','DarkChocolate','Caramel','Candy','Avocado','Coffee']
Happy= ['Quinoa','Salmon','Mushroom','Grapes','turnip greens']
Fear= ['popcorn','Brinjal','Cucumber','Mandarins','Black Elderberry','BlueBerries']
Sad = ['brazil nut','Fatty fish','Eggs','Pumpkin seeds','Chamomile tea']
Neutral= ['Noodles','Scrambled eggs','Vegetables','Chicken','Daal','Red Bean']

Happy1= {'Quinoa':'(flavonoid in quinoa has a significant anti-depressant effect.)\n(Dishes : Quinoa Pasta)',
              'Salmon':'(Salmon is packed with omega 3 fatty acids,\n which are proven to improve our mood.(Dishes :salmon burger))',
              'Mushroom':'(Vitamin D boosts mood and has anti-depressant qualities.\n Mushrooms have a ton.\n(Dishes :creamy chicken and mushroom,/nmushroom fry, \nChilli mushroom))',
        'Grapes':'(Grapes contain something called resveratrol\n an antioxidant proven to boost mood.)',
    'turnip greens':' (spinach and bok choy,Folic acid deficiencies\n lead to a drop in serotonin levels.\nFolic acid also is good for fetal brain development)'} 

Sad1 = {'brazil nut':'(Brazil nuts are high in selenium.\n Selenium may improve mood by reducing inflammation.\nSelenium is also an antioxidant,which helps prevent cell damage.)',
'Fatty fish':'(Omega-3 is a fatty acid that has a strong relationship with cognitive function as well as mental health.\nOmega-3-rich foods that contain alpha-linolenic acid (ALA) provides two essential fatty acids: \n eicosapentaenoic acid (EPA),and docosahexaenoic acid (DHA).supplementation resulted in reduced levels of anxiety.)\n(Dishes:fry fished,Eat a Salmon Burger, crispy fried fish, fish curry with coconut milk)'
,'Eggs':'(Egg yolks are another great source of vitamin D.\nVitamin D deficiency to mood disorders, such as depression and anxiety.\nEggs also contain tryptophan,which is an amino acid that helps create serotonin.\nSerotonin is a chemical neurotransmitter that helps to regulate mood,sleep, memory, and behavior.)\nDishes:(used in omelte, egg bread, egg and potato curry, egg with tomato, egg sweet)',
'Pumpkin seeds':'(Pumpkin seeds are an excellent source of potassium,\nwhich helps regulate electrolyte balance and manage blood pressure.\nPumpkin seeds are also a good source \nf the mineral zinc)\nDishes:(used in mix vegetables, halva with pumpkin seeds, roasted pumpkin seeds)'
,'Chamomile tea':'(Many people around the world use chamomile tea as an herbal remedy \nbecause of its anti-inflammatory, antibacterial,antioxidant,and relaxant properties\nChamomile tea may be useful in managing anxiety)\nDishes:(tea latte, herb tea, chamomile lavender latte)'}



Neutral1= {'Noodles':'Noodles(a complete protein, which means that it contains all nine amino acids that the body needs.)\n(Dishes :Kelp noodles,Shirataki noodles)',
          'Scrambled eggs':'(It is low in fat and even lower in\ncholesterol, making it a great supplement)\n(Dishes :cheese Scrambled eggs, Mushroom Scrambled eggs)',
          'Vegetables':'Vegetables( vegetables are a good source of vitamins and minerals, including folate, vitamin C and potassium.\nThey are an excellent source of dietary fibre,\nwhich can help to maintain a healthy gut and prevent constipation and other digestion problems.\nA diet high in fibre can also reduce your risk of bowel cancer.)\n(Dishes :mix vegetables,chicken vegetables)',
          'Chicken':'Chicken(Chicken has a very high protein content,\nwhich plays a very important role in sustaining our muscles)\n(Dishes :ginger chicken, chicken karahi)',
          'Daal':'Daal (Eat dal and you can keep away every digestive issue during summer--both constipation and diarrhoea.\nThe reason behind this is that lentils are full of dietary fibre)\n(Dishes :masoor mong daal, lentil soup)',
          'Red Bean':'(Beans contain aminowhich are the protein building blocks \nthat the body uses to heal and to make new tissues,\nsuch as bone, muscle, hair, skin, and blood. \nProtein is an essential nutrient.)\n(Dishes :red bean curry with lamb, red bean with rice)'}


Angry1= {'Leafy Green':'(Eat plenty of dopamine building food.\n They could make big difference in your anger mood to happy mood.)\n(Dishes :leafy greens curry with mushroom, \nleafy green chicken, leafy greens with onion and walnut,\n leafy green salad with apples and toamatoes)',
        'Walnut':'(Walnuts have long been celebrated for containing\nomega-3 fatty acids,\a nutrient involved in many brain functions essential\n for a good mood)\n(Dishes :walnet pie, walnut crumb cake)'
        ,'Banana':'(A banana is an edible fruit botanically\na berry produced by several kinds of large\nherbaceous flowering plants in the genus Musa,\nstrongly help to reduce anger)\n(Dishes :banoffee pie, banana bread, banana balls)'
        ,'Greek Yogurt':'(Plain Greek yogurt is a nutrient-packed snack that has many health benefits)\n (Dishes:Plain Greek Yogurt, Use with Rice '
        ,'Cottage Cheese':' (Cottage cheese is a fresh cheese curd product with a mild flavor.)\n(Dishes :cottage cheese triangle, mince and cottage cheese pulao,\n strawberry cottage cheesecake)'
        ,'Dark Chocolate':'(Dark black chocolate is a form of chocolate containing cocoa solids,\ncocoa butter and sugar, without the milk found in milk chocolate.\nIt reduces anger mood immediately)'
        ,'Caramel':' (Caramel is a medium to dark-orange confectionery product \nmade by heating a variety of sugars)\n(Dishes :Caramel Popcorn, cream caramel pudding, caramel crunch ice cream)'
        ,'Candy':'(Candy, also called sweets or lollies,\nis a confection that features sugar as a principal ingredient.)\n(Candies :Sweet candy, Chocolate eclair)'
        ,'Avocado':'(The fruit of the plant, also called an \nis botanically a large berry containing a single large seed)\n(Dishes :raita, avacado mushroom toast)'
        ,'Coffee':'(Coffee is a brewed drink prepared from roasted coffee beans,\nthe seeds of berries from certain Coffea species)\n(Dishes :creamy coffee,coffee with cinnamon, cold coffee)'}

Fear1={'Popcorn':'(The tempting smell of cooking popcorn is a more effective advert than any drawn sign.\nIt was ideal for eating while watching a movie – \nyou can eat it with your hands and it wont distract you from watching)\n(Dishes: Salty Popcorn,Cramel Popcorn)'
      ,'Brinjal':' (PREVENTS CANCER Antioxidants are one of the human body’s \nbest defenses against diseases like cancer.\n(Dishes : Brinjal Pakora, Vegetables)'
      ,'Cucumber':'(Cucumbers,are especially rich in beneficial antioxidants\n that may reduce the risk of cancer and heart,\nlung and autoimmune disease)\n(Dishes :Cucumber Salad)'
      ,'Mandarins':'(Mandarins dissolve the blockages caused by the fears and lead fears out.\n They are perfect lightning conductors.\n Mandarins are strong and fast, but the effect is not long-lasting.)'
      ,'Black Elderberry':'(Black Elderberry is able to dissolve negative energies.\nOf course,this also includes fears, and\nin particular fears about the future.)'
      ,'BlueBerries':'(Blueberries bring good mood, stability, enthusiasm, \nlightness, and well-being through the strong activation of the heart)'
      ,}
#randomly mood select
mood_selected=random.choice(Mood)
# conditinaly check mood 
if mood_selected=="Happy":
    # print kr dega Happy
    print(mood_selected)
    #select food from the the happy List  randomly 
    mood_food = random.choice(Happy) #>>> choice(['win', 'lose', 'draw']) 'draw'     # Single random element from a sequence

    #print krwa dia food
    print ("Food Selected ", mood_food)
    # food select hua wo name pass kia dictionary ko jo humy description pass kr dega jo hum n dia hoga food k against
    x = Happy1.get(mood_food)
    print(x)
elif mood_selected=="Angry":
    print(mood_selected)
    mood_food = random.choice(Angry)
    print ("Food Selected ", mood_food)
    x = Angry1.get(mood_food)
    print(x)
elif mood_selected=="Fear":
    print(mood_selected)
    mood_food = random.choice(Fear)
    print ("Food Selected ", mood_food)
    x = Fear1.get(mood_food)
    print(x)
elif mood_selected=="Sad":
    mood_food = random.choice(Sad)
    print(mood_selected)
    print ("Food Selected ", mood_food)
    x = Sad1.get(mood_food)
    print(x)
elif mood_selected=="Neutral":
    mood_food = random.choice(Neutral)
    print(mood_selected)
    print ("Food Selected ", mood_food)
    x = Neutral1.get(mood_food)
    print(x)

          
          
mood=Tk()
mood.title("Food Selection By Mood Detection")

width_win=650
height_win=630

screen_width=mood.winfo_screenwidth()
screen_height=mood.winfo_screenheight()

x_cord = (screen_width/2)-(width_win/2)
y_cord = (screen_height/2)-(height_win/2)

mood.geometry('%dx%d+%d+%d' %(width_win,height_win,x_cord,y_cord-15))

background_image= PhotoImage(file='landscape.png')
background_label=Label(mood, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(mood, bd = 5,bg='red', highlightbackground = "maroon", highlightcolor = "red", highlightthickness = 3)
frame.place(relx=0.5, rely=0.02, relwidth=0.6, relheight=0.1, anchor='n')

label= Label (frame, text='Food Selection By Mood Detection', bg="red",fg="white", font="none 12 bold")
label.place(relwidth=1 , relheight=1)

image_frame=Frame(mood,bd=5, bg='maroon')
image_frame.place(relx=0.5, rely=0.13, relwidth=0.6, relheight=0.35, anchor='n')

open_file_name=PhotoImage(file="C://Users//infinity//AppData//Local//Programs//Python//Python36//upload.png")

label_1=Label(image_frame,image=open_file_name)
label_1.place(relwidth=1,relheight=1)

label_frame=Frame(mood,bd=5, bg='maroon')
label_frame.place(relx=0.5, rely=0.49, relwidth=0.6, relheight=0.1, anchor='n')

label= Label (label_frame, text=mood_selected, bg="red",fg="white", font="none 15 bold")
label.place(relwidth=1 , relheight=1)


label_frame=Frame(mood,bd=5, bg='maroon')
label_frame.place(relx=0.5, rely=0.62, relwidth=0.89, relheight=0.25, anchor='n')

label= Label (label_frame, text="Food:"+mood_food+"\n"+x, bg="red",fg="white", font="none 10 bold")
label.place(relwidth=1 , relheight=1)


btn_frame=Frame(mood)
btn_frame.place(relx=0.3, rely=0.88, relwidth=0.35, relheight=0.1, anchor='n')

button=Button(btn_frame,text="ADD IMAGE",font=30, bg="yellow", fg="red",command=open_file)
button.place(relx=0.5, relheight=1, relwidth=1, anchor='n')

btn_frame=Frame(mood)
btn_frame.place(relx=0.7, rely=0.88, relwidth=0.35, relheight=0.1, anchor='n')

button=Button(btn_frame,text="Detect Mood",font=30, bg="yellow", fg="red")
button.place(relx=0.5, relheight=1, relwidth=1, anchor='n')






mood.mainloop()
