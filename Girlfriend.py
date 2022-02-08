'''File that handles all the girlfriend's internal logic, or the lack of per-se.'''

class GirlfriendProperty:
    label: str
    value: str # Temporary
    def __init__(self, label: str, value: str) -> None:
        pass

    def apply(girlfriend: 'Girlfriend'):
      ...


class HairColor(GirlfriendProperty):
    def __init__(self, value: str) -> None:
        super().__init__('hair_color', value)


class BreastSize(GirlfriendProperty):
      def __init__(self, value: str) -> None:
        super().__init__('breast_size', value)

big_tiddies = BreastSize('91E')

class Girlfriend:
    '''Base Girlfriend class. Used by all your possible girfriends.'''
    ...


