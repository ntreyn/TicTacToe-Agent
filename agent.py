

class computer_agent():
    def __init__(self, n, m):
        self.name = n
        self.mark = m

    def turn(self, env):
        return env.sample_action()

    def wins(self):
        print(self.name + " wins!")
