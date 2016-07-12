import screen


class popup(screen.screen):
    def __init__(self, msg):
        self.msg = msg
        screen.screen.__init__(
            self,
            dict.fromkeys(
                ['x', 'X', 'exit', 'Exit', 'EXIT'],
                self.MakeExit
            )
        )

    def __str__(self):
        return str(self.msg)
