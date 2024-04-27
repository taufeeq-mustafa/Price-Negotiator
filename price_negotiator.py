import ttkbootstrap as ttk
from sklearn.linear_model import LinearRegression
import numpy as np

game_factors = {
    'FIFA 22': {'popularity': 80, 'development_cost': 50},
    'Call of Duty: Warzone': {'popularity': 90, 'development_cost': 70},
    'Assassin\'s Creed Valhalla': {'popularity': 75, 'development_cost': 60},
    'Cyberpunk 2077': {'popularity': 60, 'development_cost': 100},
    'The Legend of Zelda: Breath of the Wild': {'popularity': 85, 'development_cost': 40},
    'Minecraft': {'popularity': 70, 'development_cost': 30},
    'GTA V': {'popularity': 95, 'development_cost': 80},
    'Among Us': {'popularity': 50, 'development_cost': 10},
    'Fortnite': {'popularity': 85, 'development_cost': 90},
    'Valorant': {'popularity': 60, 'development_cost': 50},
}

def train_regression_model():

    X = []
    y = []
    for game, factors in game_factors.items():
        X.append(list(factors.values())) 
        y.append(game_data[game])
    X = np.array(X)
    y = np.array(y)
    model = LinearRegression()
    model.fit(X, y)
    return model
game_data = {
    'FIFA 22': 50,
    'Call of Duty: Warzone': 52,
    'Assassin\'s Creed Valhalla': 47,
    'Cyberpunk 2077': 43,
    'The Legend of Zelda: Breath of the Wild': 47,
    'Minecraft': 40,
    'GTA V': 55,
    'Among Us': 30,
    'Fortnite': 54,
    'Valorant': 38
}

model = train_regression_model()

def negotiate_action():
    game_name = game_name_entry.get()
    entered_price = float(entered_price_entry.get())  

    factors = game_factors.get(game_name)
    if factors is None:
        text_widget2.insert('end', "Invalid game name\n")
        return

    predicted_price = model.predict([list(factors.values())])[0]
    print(f"Predicted Price: {predicted_price}, Entered Price: {entered_price}")

    if predicted_price > entered_price:
        text_widget2.insert('end', f"Negotiation failed for {game_name}!.\nPlease try with a higher amount.\n")
    else:
        text_widget2.insert('end', f"Negotiation successful for {game_name}!\nYou got yourself a deal\n")

def cancel_action():
    text_widget2.delete(1.0, 'end')
    print("Cancel button clicked")

def show_games_action(text_widget):

    text_widget.delete(1.0, 'end')

    for game, price in game_data.items():
        text_widget.insert('end', f"{game}: ${price}\n")

def open_about_window():
    about_window = ttk.Toplevel(app)
    about_window.title("Linear Regression Info")

    info_text = """
    Linear regression attempts to model the relationship between two variables by fitting a 
    linear equation to observed data. One variable is considered to be an explanatory 
    variable, and the other is considered to be a dependent variable. 
    For example, a modeler might want to relate the weights of individuals to their 
    heights using a linear regression model. A linear regression line has an equation 
    of the form Y = a + bX, where X is the explanatory variable and Y is the 
    dependent variable.

    Practical implementation in our Project 
    We created nested dictionaries where the name of the games and were stored as key 
    and further the values were divided into keys as values with keys being popularity
    and development  and values being their numeric values. The program then extracts
    values from the nested dictionary and allot them t X and Y variables respectively.
    The values are then changed to NumPy arrays for processing. The model for 
    Linear Regression is created, trained on (x) and (y) and returned.

    """

    text_widget_linear_regression = ttk.Text(about_window, height=20, width=80)
    text_widget_linear_regression.insert("1.0", info_text)
    text_widget_linear_regression.pack(pady=15, padx=10)

app = ttk.Window()
app.title("GameStop Price Negotiation")
app.geometry("600x900")
label = ttk.Label(app, text="GameStop Price Negotiator", bootstyle="inverse-primary")
label.pack(pady=10)
label.config(font=("Ariel", 20, "bold"))

name_frame = ttk.Frame(app)
name_frame.pack(pady=5, padx=10)
ttk.Label(name_frame, text="Game Name", bootstyle="dark").pack(side="left", padx=10)
game_name_entry = ttk.Entry(name_frame)
game_name_entry.pack(side="left", fill="x", expand=False, padx=35)

price_frame = ttk.Frame(app)
price_frame.pack(pady=5, padx=10)
ttk.Label(price_frame, text="Price").pack(side="left", padx=35)
entered_price_entry = ttk.Entry(price_frame)
entered_price_entry.pack(side="left", fill="x", expand=False, padx=35)

button_frame = ttk.Frame(app)
button_frame.pack(pady=15, padx=10)
ttk.Button(button_frame, text="Show Games", bootstyle="success-outline", command=lambda: show_games_action(text_widget)).pack(side="left", padx=5)
ttk.Button(button_frame, text="Negotiate", bootstyle="warning-outline", 
           command=negotiate_action).pack(side="left", padx=5)

ttk.Button(button_frame, text="About", bootstyle="info-outline", command=open_about_window).pack(side="left", padx=5)
ttk.Button(button_frame, text="Clear", bootstyle="danger-outline", command=cancel_action).pack(side="left", padx=5)



text_widget = ttk.Text(app, height=10, width=50)
text_widget.pack(pady=15, padx=10)

label = ttk.Label(app, text="Negotiation Window", bootstyle="inverse-success")
label.pack(pady=5)
label.config(font=("Ariel", 16, "bold"))

text_widget2 = ttk.Text(app, height=15, width=50)
text_widget2.pack(pady=15, padx=10)

item_frame = ttk.Frame(app)
item_frame.pack(pady=15, padx=10)

item_frame = ttk.Frame(app)
item_frame.pack(pady=15, padx=10)
app.mainloop()