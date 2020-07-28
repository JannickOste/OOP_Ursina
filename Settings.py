import json


class Settings(object):
    def __init__(self, app):
        self.config = json.load(open("assets/settings.json", "r"))
        self.__init_settings(app=app)

    def __init_settings(self, app):
        print("[Starting settings utilization]")
        for key, values in self.config.items():
            load_model = app
            if "." in key:
                for val in key.split("."):
                    if not hasattr(load_model, val):
                        load_model = None
                        break
                    else:
                        load_model = getattr(load_model, val)

            if load_model is None:
                print(f"App has no attribute {key}")
                continue

            for item_key, item_value in values.items():
                # If a deeper set is required fetch deeper set obj if available
                if "." in item_key:
                    for val in item_key.split(".")[0:len(item_key.split("."))-1]:
                        if hasattr(load_model, val):
                            load_model = getattr(load_model, val)

                if not hasattr(load_model, (item_key if "." not in item_key else item_key.split(".")[-1])):
                    print(f"App->{key} has no attribute {item_key}")
                    continue

                setattr(load_model, item_key, item_value)

