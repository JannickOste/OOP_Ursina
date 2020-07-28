from ursina import held_keys


class ActionHandler:
    def __init__(self, app):
        self.app = app
        self.key_actions = {
            "z": "PLAYER_MOVE:FORWARD",
            "s": "PLAYER_MOVE:BACK",
            "q": "PLAYER_MOVE:LEFT",
            "d": "PLAYER_MOVE:RIGHT"
        }

    def update(self):
        for key, action in self.key_actions.items():
            held_key_dict = dict(held_keys)

            if key in held_key_dict.keys() and held_key_dict[key] == 1:
                self.get_action(action)

    def get_action(self, action):
        action_type, args = action.split(":")

        if action_type == "PLAYER_MOVE":
            pass