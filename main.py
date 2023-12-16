import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class GraphApp(App):
    def build(self):
        # Create a Kivy layout
        layout = BoxLayout(orientation='vertical')

        # Create a Matplotlib figure and axis
        fig, ax = plt.subplots()

        # Generate some example data
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        # Plot the data
        ax.plot(x, y, marker='o')

        # Set labels and title
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Matplotlib Graph in Kivy')

        # Add the Matplotlib figure to the Kivy layout
        layout.add_widget(FigureCanvasKivyAgg(fig))

        return layout

if __name__ == '__main__':
    GraphApp().run()
