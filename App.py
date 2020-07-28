from Engine import Engine


class App(Engine):
    def __init__(self):
        """
            Todo list:
                - Finish jumping method.
                - Improve function readability
                - Add documentations
                - Check why app.application.asset_folder disables load instead of loading custom folder.
                - Create interfaces for entitys
                - Dedicated entity spawner.
                - better walking.
        """
        super(App, self).__init__(self)

        self._init_components()
        self.run()


if __name__ == '__main__':
    App()
