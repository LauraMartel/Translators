from libraries import *


def transform_word_to_emoji(txt, frame):
    global my_label
    
    list_emojis_1 = ["๐","๐", "๐", "๐คฃ", "๐", "๐", "๐", "๐ฅฐ", "๐", "๐ฅฒ", "๐ค",
        "๐คฉ", "๐ค", "๐", "๐ซก", "๐คจ", "๐", "๐", "๐ฃ", "๐ฎ", "๐ซฅ", "๐ด"]
    list_emojis_2 = ["๐ญ", "๐ฃ", "๐ค", "๐ฒ", "๐ฅ", "๐ง", "๐ข", "๐ฅฎ", "๐ฅ", "๐ซ", "๐",
        "๐ฅฃ", "๐ฅง", "๐ฆ", "๐ฐ", "๐", "๐ช", "๐ฉ", "๐ป"]
    list_emojis_3 = ["โถ", "โต", "โธ", "โน", "โฟ", "โบ", "โด", "โท", "โฐ", "โณ", "โซ", "โ", "โฌ",
            "โญ", "โฎ", "โ", "โฉ", "โ", "โบ", "โ", "โณ", "โฒ", "โฉ", "โฉ", "โฉ", "โฉ", "โฉ", "โฉ", "โฉ", "โฉ", "โฉ"]
    
    for emoji1, emoji2, emoji3 in zip((random.sample(list_emojis_1, 1)), (random.sample(list_emojis_2, 1)), (random.sample(list_emojis_3, 1))):
        emoji_1 = emoji1
        emoji_2 = emoji2
        emoji_3 = emoji3

    # pick a random emoji
    if len(txt.get("1.0",END)) !=0:
        rand_nb = random.randint(0, len((txt.get("1.0",END)).split()))
        word = random.sample((txt.get("1.0",END)).split(), rand_nb)
        my_label = Label(frame)
        my_label.grid_forget()
        my_label.grid(row=1, column=3, sticky=N)
    else:
        print("Enter something")

    # Base on the length of the text gives you an emoji 
    text_1 = f"{emoji_1} Smile-y"
    text_2 = f"{emoji_2} You are hungry"
    text_3 = f"{emoji_3} Why so complicated?!"
    
    if len(word) in range(0, 50):
        my_label.config(text=text_1, font=("Courier", 24))
        return  my_label
    elif len(word) in range(50, 200, 1):
        my_label.config(text=text_2, font=("Courier", 24))
        return my_label
    else:
        my_label.config(text=text_3, font=("Courier", 24))
        return my_label
    
    