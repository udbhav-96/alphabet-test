# Program to create a calculator

# Program to Show how to create a switch
# import kivy module
import kivy
    
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
    
# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# for making multiple bttons to arranging
# them we are using this
from kivy.uix.gridlayout import GridLayout

# for the size of window
from kivy.config import Config

# Setting size to resizable
Config.set('graphics', 'resizable', 1)
## Config.set('graphics', 'width', '400')
## Config.set('graphics', 'height', '400')

# Creating Layout class
class CalcGridLayout(GridLayout):

    # Function called when equals is pressed
    """
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(alphabet_test))
            except Exception:
                self.display.text = "This Error"
    """
    def calculate(self, calculation):
        user_input = calculation        
        if calculation:
            try:
                if len(user_input) == 7:                    
                    list_order = int(user_input[0])
                    first_dir = user_input[1]
                    first_dir_no = int(user_input[2:4])
                    second_dir = user_input[4]
                    second_dir_no = int(user_input[5:7])
                    
                elif len(user_input) == 6:
                    if user_input[3].isdigit() and user_input[4].isalpha():
                        list_order = int(user_input[0])
                        first_dir = user_input[1]
                        first_dir_no = int(user_input[2:4])
                        second_dir = user_input[4]
                        second_dir_no = int(user_input[5])
                        
                    elif user_input[4].isdigit() and user_input[3].isalpha():
                        list_order = int(user_input[0])
                        first_dir = user_input[1]
                        first_dir_no = int(user_input[2])
                        second_dir = user_input[3]
                        second_dir_no = int(user_input[4:5])
                        
                else:
                    list_order = int(user_input[0])
                    first_dir = user_input[1]
                    first_dir_no = int(user_input[2])
                    second_dir = user_input[3]
                    second_dir_no = int(user_input[4])
                """print(list_order)
                print(first_dir)
                print(first_dir_no)
                print(second_dir)
                print(second_dir_no)"""
                l_forword = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                l_reverse = l_forword[::-1]
                #-------------------------------------------
                list_first_half = l_forword[0:13]
                list_second_half = l_forword[13:26]
                list_first_half_reversed = l_forword[0:13][::-1]
                list_second_half_reversed = l_forword[13:26][::-1]
                #-------------------------------------------
                f_half_reversed = list_first_half_reversed + list_second_half
                s_half_reversed = list_first_half + list_second_half_reversed
                both_reverse = list_first_half_reversed + list_second_half_reversed
                #-------------------------------------------

                # For Forword Order Series -------------------------------
                if list_order == 1:
                    if (first_dir == "L") and (second_dir == "R"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_forword[total-1]
                            self.display.text = letter
                            
                    elif(first_dir == "R") and (second_dir == "L"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_forword[(27-total)-1]
                            self.display.text = letter
                            
                    elif (first_dir == "L") and (second_dir == "L"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_forword[total-1]
                            self.display.text = letter
                            
                    elif (first_dir == "R") and (second_dir == "R"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_forword[(27-total)-1]
                            self.display.text = letter
                            
                # For Reverse Order Series -----------------------------------
                elif list_order == 2:
                    if (first_dir == "L") and (second_dir == "R"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_reverse[total-1]
                            self.display.text = letter
                            
                    elif(first_dir == "R") and (second_dir == "L"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_reverse[(27-total)-1]
                            self.display.text = letter
                            
                    elif (first_dir == "L") and (second_dir == "L"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_reverse[total-1]
                            self.display.text = letter
                            
                    elif (first_dir == "R") and (second_dir == "R"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = l_reverse[(27-total)-1]
                            self.display.text = letter
                            
                #  For First Half Reverse Order        
                elif list_order == 3:
                    if (first_dir == "L") and (second_dir == "R"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = f_half_reversed[total-1]
                            self.display.text = letter
                            
                    elif(first_dir == "R") and (second_dir == "L"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = f_half_reversed[(27-total)-1]
                            self.display.text = letter
                            
                    elif (first_dir == "L") and (second_dir == "L"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = f_half_reversed[total-1]
                            self.display.text = letter
                            
                    elif (first_dir == "R") and (second_dir == "R"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = f_half_reversed[(27-total)-1]
                            self.display.text = letter

                # For Second Reverse Order
                elif list_order == 4:
                    if (first_dir == "L") and (second_dir == "R"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = s_half_reversed[total-1]
                            self.display.text = letter
                            
                    elif(first_dir == "R") and (second_dir == "L"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = s_half_reversed[(27-total)-1]
                            self.display.text = letter
                            
                    elif (first_dir == "L") and (second_dir == "L"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = s_half_reversed[total-1]
                            self.display.text = letter
                            
                    elif (first_dir == "R") and (second_dir == "R"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = s_half_reversed[(27-total)-1]
                            self.display.text = letter

                # Both reverse order 
                elif list_order == 5:
                    if (first_dir == "L") and (second_dir == "R"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = both_reverse[total-1]
                            self.display.text = letter
                            
                    elif(first_dir == "R") and (second_dir == "L"):
                        total = first_dir_no + second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = both_reverse[(27-total)-1]
                            self.display.text = letter
                            
                    elif (first_dir == "L") and (second_dir == "L"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = both_reverse[total-1]
                            self.display.text = letter
                            
                    elif (first_dir == "R") and (second_dir == "R"):
                        total = first_dir_no - second_dir_no
                        if (total <=0) or (total >=27):
                            self.display.text = "Our Of Range"
                        else:
                            letter = both_reverse[(27-total)-1]
                            self.display.text = letter
                        
                else:
                    self.display.text = "Error"
            except Exception:
                self.display.text = "Error"

# Creating App class
class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

# creating object and running it
calcApp = CalculatorApp()
calcApp.run()
