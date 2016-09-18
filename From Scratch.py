
from kivy.app import App
from kivy.lang import Builder


# MILES_TO_KM = 1.60934


class FromScratch(App):

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('From scratch.kv')
        return self.root

    def increasement(self):
        value = self.get_number()
        value += 1
        self.root.ids.user_input_value.text = str(value)
        self.handle_calculate()

    def decreasement(self):
        value = self.get_number()
        value -= 1
        self.root.ids.user_input_value.text = str(value)
        self.handle_calculate()

    def handle_calculate(self):
        value = self.get_number()
        result = value * 1.60934
        self.root.ids.user_output.text = str(result)

    def get_number(self):

        try:
            value = float(self.root.ids.user_input_value.text)
            return value
        except ValueError:
            return 0


FromScratch().run()
