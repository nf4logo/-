import easygui
flavor = easygui.enterbox("Waht is your favorite ice cream flavor?",
                          default = 'Vanilla')
easygui.msgbox("You entered "+ flavor)
