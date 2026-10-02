
from random import choice

capital = "Mumbai is it's Capital"

bird = "Hariyal is the State Bird"

flower = "Jarul is the state Flower"

song = "'Jay Jay Maharashtra Maza' is the State Song"


def randomfunfacts():
    funfacts = [
        "Lonar Crater Lake: It is a massive saltwater lake in Buldhana created by a meteorite impact over 50,000 years ago. The lake has a unique ecosystem and is one of the world's only basalt rock craters.",
        "Shani Shingnapur's Doorless Houses: This famous village in Ahmednagar district features houses, shops, and even banks without any doors or locks. Locals believe the deity Shani protects them from theft.",
        "The Largest Highway Network: Maharashtra possesses the longest state highway network in India. It accounts for nearly 20% of the entire country's highway connectivity.",
        "Navi Mumbai's Modern Footprint: Designed in 1971 to help handle Mumbai's massive population growth, it has evolved into one of the largest planned townships in the entire world."
    ]

    index = choice("0123")
    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfacts()
