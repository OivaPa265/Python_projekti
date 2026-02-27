import textwrap

lore =  (" Tervetuloa TXK26K1-B ohjelmisto 1  python peli projektiin tämän pelin ovat tehneet: 1,2,3,4? "
         " Tässä pelissä pelaat humaloituneena joulupukkina hänen korkeakoulu opiskelija aikanaan Metropoliassa."
         "Tehtäväsi on simppeli matkusta ympäri suomea keräämässä kaikenlaisia merkkejä joita voit kiinittää haalareihisi."
         "Keräämäsi merkit näkyvät joulupukki hahmossasi joka näkyy nurkassa ."
         " jotta voisit liikua ympäri suomea tarvitset tietysti poltto ainetta, poltto aine on tietystikkin alkoholi."
         "Onnea matkaan peelaja ja  varo kelaa, kela haluaa sinun alkoholisi. ole varovainen")

wrapper = textwrap.TextWrapper(width=60, break_long_words=False, replace_whitespace=False)

word_list = wrapper.wrap(text=lore)

def paheelore():
    return word_list
