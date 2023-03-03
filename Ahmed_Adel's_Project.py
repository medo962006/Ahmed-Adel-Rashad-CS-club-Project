import telebot
from telebot import types 

TOKEN = '6013941134:AAGAymdQ0VQFKtBpmCJNluVPhS_Iua-WZRk'
ABOUT_TEXT = """This bot is designed by Ahmed Adel, It can reply with links from youtube specifically related to Turtle Projects"""
bot = telebot.TeleBot(TOKEN)
def generate_buttons(bts_names, markup):
    for button in bts_names:
        markup.add(types.KeyboardButton(button))
    return markup
@bot.message_handler(commands=['start'])
def send_hello(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)  
    markup = generate_buttons(["""Ahmed Adel's designs""",'Fortify Solutions','Raza Zaidi','Tech with tim','Neural Nine','Code_champ3827'],markup)
    message = bot.reply_to(message, "choose a channel to watch from",
                 reply_markup=markup)
    bot.register_next_step_handler(message,video_choose)
def image_provider(message,text,imagelink):
    if message.text==text:
        chat_id = message.chat.id
        medias = [imagelink]
        url = medias[0]
        bot.send_photo(chat_id=chat_id,photo=url)
def video_channels(message,text,function,*argv):
       markup = types.ReplyKeyboardMarkup(row_width=2)
       buttons=[]
       for arg in argv:
              buttons.append(arg)
       if message.text==text:
              markup=generate_buttons(buttons,markup)
              guess = bot.reply_to(message, 
                             "here are the designs, choose one: ",
                             reply_markup=markup)
       bot.register_next_step_handler(message,function)
def video_choose(message):
       video_channels(message,"Ahmed Adel's designs",AhmedAdelDesigns,'star Fractal','Tree','circles','circle Fractal','spiral triangle','spiral web')
       video_channels(message,"Fortify Solutions",Fortify_Solutions,'Vibrate Circle','python turtle in pycharm','3d cube','working clock','change background images','stopwatch','star')
       video_channels(message,"Raza Zaidi",Raza_Zaidi,'Spirographic','Triangles','Drawing art with python','drawing pickachu in python')
       video_channels(message,"Tech with tim",Tech_with_tim,'turtle racing','introduction to turtle','shapes and fills','key presses and events','Fractal art','Drawing with mouse')
       video_channels(message,"Neural Nine",Neural_Nine,'Graphical Python Programming')
       video_channels(message,"Code_champ3827",Code_champ3827,'emoji','star','amazing design','shinchan')
       bot.register_next_step_handler(message,send_hello)
def linkProvider(message,text,link):
       markup=types.ReplyKeyboardMarkup(row_width=2)
       if message.text==text:
           guess = bot.reply_to(message, 
                             "Here is the link for my special design: "+message.text+" "+link ,
                             reply_markup=markup)
def AhmedAdelDesigns(message):
    image_provider(message,"star Fractal","https://ibb.co/XYF3G18")
    image_provider(message,"Tree","https://ibb.co/3N8wVjM")
    image_provider(message,"circles","https://ibb.co/8PZbNwD")
    image_provider(message,"circle Fractal","https://ibb.co/zrk2pKt")
    image_provider(message,"spiral triangle","https://ibb.co/fG9ND8s")
    image_provider(message,"spiral web","https://ibb.co/b3Z3zXx")
def Fortify_Solutions(message):
    
    linkProvider(message,"Vibrate Circle"," https://www.youtube.com/watch?v=N1SXaowmTEM&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=1")
    linkProvider(message,"python turtle in pycharm","  https://www.youtube.com/watch?v=ZPSRwUci3CM&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=2")
    linkProvider(message,"3d cube"," https://www.youtube.com/watch?v=Be4bWO629oE&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=5")
    linkProvider(message,"working clock"," https://www.youtube.com/watch?v=w7VhJ-YYm2A&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=6")
    linkProvider(message,"change background images"," https://www.youtube.com/watch?v=W65wNAWWRKE&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=8")
    linkProvider(message,"stopwatch"," https://www.youtube.com/watch?v=zid03m-hxu8&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=10")
    linkProvider(message,"star"," https://www.youtube.com/watch?v=a-Hv9Q7_OxU&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg&index=12")
def Raza_Zaidi(message):
    
    linkProvider(message,"Spirographic","https://www.youtube.com/watch?v=ogsRn1XSy5c")
    linkProvider(message,"Triangles","https://www.youtube.com/watch?v=t7TLi36tfqQ&list=PL_qZhs4wgnWOqFeo6-O99RInK3Wz5s8hi&index=2")
    linkProvider(message,"Drawing art with python"," https://www.youtube.com/watch?v=EXDFEJGuwno&list=PL_qZhs4wgnWOqFeo6-O99RInK3Wz5s8hi&index=3")
    linkProvider(message,"drawing pickachu with python"," https://www.youtube.com/watch?v=em2pOt80fjg")

def Tech_with_tim(message):
    
    linkProvider(message,"turtle racing","https://www.youtube.com/watch?v=gQP0geNsO4A")
    linkProvider(message,"introduction to turtle","https://www.youtube.com/watch?v=p7CiFhiTdvY")
    linkProvider(message,"key presses and events","https://www.youtube.com/watch?v=hPnZqWSRNZI")
    linkProvider(message,"shapes and fills","https://www.youtube.com/watch?v=KmziL1djFkQ")
    linkProvider(message,"Fractal art","https://www.youtube.com/watch?v=_ABdBoW4DV8")
    linkProvider(message,"Drawing with mouse"," https://www.youtube.com/watch?v=HRKQlEfEMCA")
def Neural_Nine(message):

    linkProvider(message,"Graphical Python Programming","  https://www.youtube.com/watch?v=xoKKzncO8Xo")
def Code_champ3827(message):

    linkProvider(message,"emoji","https://www.youtube.com/shorts/s8pkIaipvVA")
    linkProvider(message,"star","https://www.youtube.com/shorts/fIYzTIjJdT4")
    linkProvider(message,"amazing design"," https://www.youtube.com/shorts/fy35WwjFg74")
    linkProvider(message,"shinchan", "https://www.youtube.com/shorts/JqS5NJV2chk")

bot.infinity_polling()