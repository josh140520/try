import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import seaborn as sns
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

# Sample data
data = sns.load_dataset("iris")

# Create a Seaborn plot
sns.set(style="whitegrid")
fig, ax = plt.subplots()
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=data, ax=ax)
plt.title("Seaborn Scatter Plot in Kivy")

# Kivy App
class SeabornKivyApp(App):
    def build(self):
        # Create a box layout
        layout = BoxLayout(orientation='vertical')

        # Embed the Seaborn plot in the Kivy app using FigureCanvasKivyAgg
        canvas = FigureCanvasKivyAgg(plt.gcf())
        layout.add_widget(canvas)

        return layout

if __name__ == '__main__':
    SeabornKivyApp().run()
