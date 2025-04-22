class Smartphone:
    def __init__(self, brand, model, price, battery_level):
        self.brand = brand # Brand name
        self.model = model # Model name
        self.price = price # Price in dollars
        self.apps = []  # List to store installed apps
        self.is_on = False  # State of the smartphone (on/off)
        self.battery_level = battery_level
    

    def power_on(self):
        """Power on the smartphone."""
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is powered on.")
        elif self.is_on:
            print(f"{self.brand} {self.model} is already on.")
        else:
            print(f"{self.brand} {self.model} is off.")

    def install_app(self, app_name):
        """Install an app on the smartphone."""
        if self.is_on:
            self.apps.append(app_name)
            print(f"{app_name} has been installed on {self.brand} {self.model}.")
        else:
            print(f"Cannot install {app_name}. {self.brand} {self.model} is off.")

    def use_app(self, app_name):
        """Use an installed app."""
        if self.is_on:
            if app_name in self.apps:
                print(f"Using {app_name} on {self.brand} {self.model}.")
            else:
                print(f"{app_name} is not installed on {self.brand} {self.model}.")
        else:
            print(f"Cannot use {app_name}. {self.brand} {self.model} is off.")

    def display_info(self):
        """Display smartphone information."""
        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Installed Apps: {', '.join(self.apps) if self.apps else 'None'}")
        print(f"Power Status: {'On' if self.is_on else 'Off'}")
    

class GamingPhone(Smartphone):
    """A specialized smartphone for gaming."""
    def __init__(self, brand, model, gpu, battery_level):
        super().__init__(brand, model)
        self.gpu = gpu
        self.battery_level = battery_level
        self.game_mode = False

    def activate_game_mode(self):
        """Activate gaming mode."""
        if self.is_on and self.battery_level > 20:
            self.game_mode = True
            print(f"Gaming mode activated on {self.brand} {self.model}.")
        else:
            print("Cannot activate gaming mode")

    def play_game(self, game_name):
        """Play a game."""
        if self.is_on and self.game_mode:
            print(f"Playing {game_name} on {self.brand} {self.model}.")
            return
        else:
            print(f"Cannot play {game_name}. Gaming mode is not activated or battery is low.")
            return
            

    def display_info(self):
        """Display gaming phone information."""
        super().display_info()
        print(f"GPU: {self.gpu}")
        print(f"Battery Level: {self.battery_level}%")
        print(f"Gaming Mode: {'On' if self.game_mode else 'Off'}")
    
if __name__ == "__main__":
    # Regular smartphone
    phone = Smartphone("Apple", "iPhone 15")
    phone.power_toggle()
    phone.install_app("Maps")
    phone.use_app("Maps")
    phone.display_info()
    
    # Gaming phone
    game_phone = GamingPhone("ASUS", "ROG Phone", "Adreno 740")
    game_phone.power_toggle()
    game_phone.install_app("PUBG")
    game_phone.activate_game_mode()
    game_phone.play_game("PUBG")
    game_phone.display_info()