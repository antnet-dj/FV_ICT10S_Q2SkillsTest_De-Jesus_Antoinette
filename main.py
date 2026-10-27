
from pyscript import document, display

nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.002602),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998403163),
    "Ne": ("Neon", 10, 20.1797),
    "P": ("Phosphorus", 15, 30.973761998),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90447),
    "Xe": ("Xenon", 54, 131.293),
    "At": ("Astatine", 85, 210),
    "Rn": ("Radon", 86, 222),
    "Ts": ("Tennessine", 117, 293),
    "Og": ("Oganesson", 118, 294),
}

def search_element(e):
    el = document.getElementById("symbol").value

    el_display = nonmetals.get(
        el,
        ("Element not found", "N/A", "N/A")
    )

    document.getElementById("output").innerHTML = f"""
    <b>Symbol:</b> {el} <br>
    <b>Element:</b> {el_display[0]} <br>
    <b>Atomic Number:</b> {el_display[1]} <br>
    <b>Atomic Mass:</b> {el_display[2]} <br>
    """

# references: 
# https://sciencenotes.org/list-nonmetals/
# https://periodictable.com/Properties/A/AtomicMass.an.html