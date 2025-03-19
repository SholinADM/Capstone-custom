import streamlit as st
from PIL import Image

'''
Functions for text generation
'''

def blazer():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Blazer")
            st.text("A blazer is a type of jacket that is more formal than a casual jacket but less formal than a suit jacket. It's often tailored, structured, and can come in various materials like wool, cotton, or linen. Blazers are versatile and can be worn with jeans, chinos, or dress pants.")
            st.subheader("When to wear a blazer:")
            st.markdown("""
                        - Business casual settings (e.g., meetings, office wear without a full suit)
                        - Smart casual events (e.g., dinner dates, parties, social gatherings)
                        - Semi-formal occasions (e.g., weddings, graduations, or networking events)
                        - Travel or presentations when you want to look sharp but not overdressed
                        """)
        with col2:
            image = Image.open('static/blazer_example.jpg')
            st.image(image,use_container_width=True)

def button_shirts():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Button shirts")
            st.text("Sure! A button shirt (or button-down shirt) is a shirt with buttons running down the front, often with a collar and cuffs. It comes in various styles, from formal dress shirts to casual flannels or linen shirts.")
            st.subheader("When to wear a button shirt:")
            st.markdown("""
                        - Formal settings: Wear a crisp, tucked-in button shirt with slacks or a suit for business, interviews, weddings, or formal events. 
                        - Smart casual: Pair a button shirt with chinos or jeans for dinners, dates, or semi-formal gatherings.
                        - Casual: Roll up the sleeves or wear it open over a T-shirt for a relaxed, stylish look.

                        """)
        with col2:
            image = Image.open('static/button_shirt_example.jpg')
            st.image(image,use_container_width=True)

def Denim_jacket():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Denim Jacket")
            st.text("A denim jacket is a casual outerwear piece made from denim fabric, usually with buttons down the front and chest pockets. It's a timeless, rugged staple that adds a cool, laid-back vibe to any outfit. It’s super versatile, and the more you wear it, the better it looks with that worn-in, vintage vibe.")
            st.subheader("When to wear a Denim jacket:")
            st.markdown("""
                        - Casual outings: Great for coffee runs, hanging out with friends, or weekend strolls—pair it with T-shirts, hoodies, or flannels.
                        - Layering piece: Works well over a hoodie or under a heavier coat in colder weather.
                        - Smart casual: Dress it up slightly with chinos and a button shirt or turtleneck for a stylish, modern look.
                        - Transitional seasons: Perfect for spring and fall when you need a light jacket.
                        """)
        with col2:
            image = Image.open('static/Denim_jacket_example.jpg')
            st.image(image,use_container_width=True)

def Hoodie():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Hoodie")
            st.text("A hoodie is a casual, cozy sweatshirt with a hood—often featuring a front pocket (kangaroo pocket) and sometimes a zip-up style. It's all about comfort and laid-back style. They're super versatile and come in different styles—from slim-fit minimalist designs to oversized streetwear vibes.")
            st.subheader("When to wear a hoodie:")
            st.markdown("""
                        - Casual settings: Perfect for lounging, running errands, casual meetups, or traveling. 
                        - Streetwear style: Pair with joggers, jeans, or cargo pants for a cool, urban look—great for everyday wear. 
                        - Layering: Works well under denim jackets, bomber jackets, or even overcoats in colder weather.
                        """)
        with col2:
            image = Image.open('static/Hoodie_example.jpg')
            st.image(image,use_container_width=True)

def Jeans():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Jeans")
            st.text("Jeans are durable pants made from denim, known for their comfort, versatility, and timeless appeal. They come in various cuts like slim, straight, skinny, bootcut, relaxed, and baggy, as well as different washes (light, dark, black, distressed, etc.). Jeans are super adaptable and a core piece in almost every wardrobe.")
            st.subheader("When to wear a Jeans:")
            st.markdown("""
                        - Everyday casual: Jeans are a go-to for daily wear—easy to pair with T-shirts, hoodies, sneakers, or boots. 
                        - Smart casual: Dark-wash or well-fitted jeans can be styled with a button shirt or blazer for a more polished look. 
                        - Workwear (in casual workplaces): In some offices, clean, dark jeans are acceptable as business casual. 
                        - Social outings: Ideal for dates, dinners, concerts, or weekend hangouts—just switch up the top and shoes to match the vibe.
                        """)
        with col2:
            image = Image.open('static/Jean_example.jpg')
            st.image(image,use_container_width=True)

def Long_pants():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Long pant")
            st.text("Long pants (also simply called trousers or pants) refer to any full-length bottoms that cover the legs completely—excluding shorts or cropped styles. They come in many styles, materials, and fits, depending on the occasion. Basically, long pants are a wardrobe essential—more polished than jeans but still versatile depending on the fabric and style.")
            st.subheader("When to wear a long pant:")
            st.markdown("""
                        - Formal & business settings: Dress pants or tailored trousers are perfect for work, meetings, or events—usually paired with button shirts or blazers. 
                        - Smart casual looks: Chinos or slim-fit pants work great with polos, button shirts, or knitwear for a clean, stylish appearance. 
                        - Everyday wear: Cotton or cargo pants offer comfort for day-to-day activities, errands, or casual outings. 
                        - Cold weather: Ideal for keeping warm during fall and winter seasons.
                        """)
        with col2:
            image = Image.open('static/Long_pants.jpg')
            st.image(image,use_container_width=True)

def shorts():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("Short")
            st.text("Shorts are bottoms that cover the upper legs but leave the lower legs exposed—great for warm weather and casual comfort. They come in various styles like denim shorts, cargo shorts, chino shorts, athletic shorts, and tailored shorts. Shorts keep things cool and laid-back, but for more formal or professional occasions, long pants are usually the better call.")
            st.subheader("When to wear a short:")
            st.markdown("""
                        - Hot weather: Perfect for summer, beach days, vacations, or anywhere with a warm climate. 
                        - Casual settings: Great for hanging out, running errands, or relaxing at home—pair with T-shirts, polos, or tank tops. 
                        - Outdoor activities: Athletic or performance shorts are ideal for workouts, sports, hiking, or biking. 
                        - Smart casual: Chino or tailored shorts can work for casual lunches or summer parties when styled with loafers and a neat shirt or polo.
                        """)
        with col2:
            image = Image.open('static/Shorts_example.jpg')
            st.image(image,use_container_width=True)

def tshirt():
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("T-shirt")
            st.text("A T-shirt is a simple, short-sleeved top, usually made of cotton or a cotton blend, shaped like the letter “T.” It’s one of the most versatile and essential pieces in any wardrobe. T-shirts come in different styles like crew neck, V-neck, oversized, slim-fit, graphic tees, and basic solids—easy to dress up or down depending on how you style them.")
            st.subheader("When to wear a T-shirt:")
            st.markdown("""
                        - Everyday casual: Ideal for daily wear—just throw it on with jeans, shorts, or joggers. 
                        - Layering piece: Works great under jackets, hoodies, or overshirts. 
                        - Activewear: Lightweight and breathable T-shirts are perfect for workouts, sports, or outdoor activities. 
                        - Smart casual: A well-fitted, plain T-shirt (especially in neutral colors) can look polished with chinos, loafers, or a blazer.
                        """)
        with col2:
            image = Image.open('static/Tshirt_example.jpg')
            st.image(image,use_container_width=True)
    
def item(index):
        out = [blazer,button_shirts,Denim_jacket,Hoodie,Jeans,Long_pants,shorts,tshirt][index]()
        return out