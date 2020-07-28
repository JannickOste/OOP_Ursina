from Engine import Engine


class App(Engine):
    def __init__(self):
        """
            Todo list:
                [Entitys]:
                - Create interfaces for entitys
                - Dedicated entity spawner.
                [Player actions]:
                - Check out jumping speed
                - Add player freezing.
                [Interface]
                - Add interface system.
                - Add message system.
                [World]:
                - Add objects spawner.
                [Actions]:
                - Add action handler
                [Misc]:
                - Improve function readability
                - Add documentations
                - Check why app.application.asset_folder disables load instead of loading custom folder.
                probably more...
        """

        """
            Update list:
                0.01 / 28/07/2020:
                    [Project]:
                    - Restructured files & converted to OOP.
                    - Added Settings loader.
                    
                    [Player]:
                    - Added Jumping
                    - Added running
                    
        """
        super(App, self).__init__(self)

        self._init_components()
        self.run()


if __name__ == '__main__':
    App()
