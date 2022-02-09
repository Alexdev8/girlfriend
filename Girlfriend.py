"""File that handles all the girlfriend's internal logic, or the lack of per-se."""


class GirlfriendProperty:
    label: str
    value: str  # Temporary

    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value

    def apply(girlfriend: 'Girlfriend'):
        ...

    def get_girlfriend(self):
        print("  ___________\n"
              "/////////////{ >o﹤ }\n"
              "|||||||||||                 |\n"
              "|||||||||O          O  |\n"
              "|||||||        /           /|\n"
              "||||||\       __       /|||\n"
              "||||||||\_______/||||\n"
              "|||||||||||||____|||||||||\n"
              "|||||||||| \ \n"
              "||||||| |  (       (    |     |\n"
              "||||||| |               |     |\n"
              "||||||  |               \ \ \n"
              "/    //                 \\ \ \n"
              "//                    \\ \ \n"
              "//                        \\ \ \n"
              ")/______________\( ,,,)\n"
              "{ >o﹤ }{ >o﹤ }{ >o﹤ }\n"
              "|     |      |     |\n"
              "|     |      |     |\n"
              "(___ |      | ___)\n")
        print("Her name is", self.name)


class HairColor(GirlfriendProperty):
    def __init__(self, value: str) -> None:
        super().__init__('hair_color', value)


class BreastSize(GirlfriendProperty):
    def __init__(self, breast_size: str) -> None:
        super().__init__('breast_size', breast_size)


big_tiddies = BreastSize('91E')


class Girlfriend:
    """Base Girlfriend class. Used by all your possible girlfriends."""
    ...
