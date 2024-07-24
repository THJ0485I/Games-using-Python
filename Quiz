import random

# Data structure to hold the countries and their capitals by continent
quiz_data = {
    "Africa": {
        "Nigeria": "Abuja",
        "Egypt": "Cairo",
        "South Africa": "Pretoria",
        "Kenya": "Nairobi",
        "Ethiopia": "Addis Ababa",
        "Ghana": "Accra",
        "Morocco": "Rabat",
        "Tunisia": "Tunis",
        "Uganda": "Kampala",
        "Algeria": "Algiers"
    },
    "Asia": {
        "China": "Beijing",
        "India": "New Delhi",
        "Japan": "Tokyo",
        "South Korea": "Seoul",
        "Indonesia": "Jakarta",
        "Thailand": "Bangkok",
        "Malaysia": "Kuala Lumpur",
        "Vietnam": "Hanoi",
        "Saudi Arabia": "Riyadh",
        "Turkey": "Ankara"
    },
    "Europe": {
        "United Kingdom": "London",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Poland": "Warsaw"
    },
    "North America": {
        "United States": "Washington, D.C.",
        "Canada": "Ottawa",
        "Mexico": "Mexico City",
        "Cuba": "Havana",
        "Jamaica": "Kingston",
        "Costa Rica": "San José",
        "Panama": "Panama City",
        "Honduras": "Tegucigalpa",
        "Guatemala": "Guatemala City",
        "Belize": "Belmopan"
    },
    "South America": {
        "Brazil": "Brasília",
        "Argentina": "Buenos Aires",
        "Colombia": "Bogotá",
        "Chile": "Santiago",
        "Peru": "Lima",
        "Venezuela": "Caracas",
        "Ecuador": "Quito",
        "Bolivia": "Sucre",
        "Paraguay": "Asunción",
        "Uruguay": "Montevideo"
    },
    "Australia": {
        "Australia": "Canberra",
        "Fiji": "Suva",
        "Papua New Guinea": "Port Moresby",
        "New Zealand": "Wellington",
        "Solomon Islands": "Honiara",
        "Tonga": "Nukuʻalofa",
        "Samoa": "Apia",
        "Vanuatu": "Port Vila",
        "Kiribati": "South Tarawa",
        "Micronesia": "Palikir"
    }
}
def ask_question(continent, countries):
    country = random.choice(list(countries.keys()))
    capital = countries[country]
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {capital}.\n")
        return False

def play_quiz():
    print("Welcome to the Capital Cities Quiz!")
    score = 0

    for continent, countries in quiz_data.items():
        print(f"\nContinent: {continent}")
        for _ in range(3):  # Ask 3 questions per continent
            if ask_question(continent, countries):
                score += 1

    print(f"Your final score is {score} out of {len(quiz_data) * 3}")

if __name__ == "__main__":
    play_quiz()
