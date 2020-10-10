"""Program to create an app in python using kivy library"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    """
    MainApp that needs to be run to instanciate the kivy UI
    """

    def build(self):
        """
        Main function for the layout
        """
        #list of operators
        self.operators = ["+", "-", "*", "/"]
        #last operator, at start will be none
        self.last_operators = None
        #last button that was pressed, at start will be none
        self.last_button = None

        #main layout for the app
        main_layout = BoxLayout(orientation = 'vertical')
        #text that would be displayed
        self.solution = TextInput(multiline = False, readonly = True,
                                    halign = 'right', font_size = 55)
        main_layout.add_widget(self.solution)

        # buttons that are to be displayed
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','C','+'],
        ]

        # creating a layout for the button and binding a function to each
        for btns in buttons:
            horizontal_layout = BoxLayout()
            for btn in btns:
                button = Button(text=btn, pos_hint={'center_x':.5,
                                                    'center_y':.5})
                button.bind(on_press=self.button_on_press)
                horizontal_layout.add_widget(button)
            main_layout.add_widget(horizontal_layout)
        #equals button to calculate the end result
        equal_button = Button(text="=", pos_hint={"center_x": 0.5,
                                                 "center_y": 0.5})
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def button_on_press(self, instance):
        """
        This function binded to the button press events
        """
        current_text = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            # if cancel is hit clear the text
            self.solution.text = ''
        else:
            if current_text and (self.last_operators and
                                button_text in self.operators):
                # there cannot be two operators after a number
                return
            elif current_text == '' and button_text in self.operators:
                # first entry cannot be an operator
                return
            else:
                # update the text as per user's entry
                new_text = current_text + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_operators = self.last_button in self.operators

    def on_solution(self, instance):
        """
        This function will calculate the result when equals is hit
        """
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    MainApp().run() #run the app to get the output
