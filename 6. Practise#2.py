import easygui
name = easygui.enterbox("Please enter your name:")
addr = easygui.enterbox("Please enter your street address:")
city = easygui.enterbox("Please enter your city:")
state = easygui.enterbox("Please enter your state:")
zipcode = easygui.enterbox("Please enter your zip code:")
easygui.msgbox(name + "\n" + addr + "\n" + city + ", " + state + "\n" + zipcode)
