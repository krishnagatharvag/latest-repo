


class First():
    def _first_method(self):
        print("this is first method")

class Second(First):
    def second_method(self):
        print(f"this is second method")
        self.first_method

