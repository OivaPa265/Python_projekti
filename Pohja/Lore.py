import textwrap
# fix yo shit
lore =  (" Tervetuloa TXK26K1-B ohjelmisto 1  python peli projektiin tämän pelin ovat tehneet: nimi 1,2,3,4,? "
         " Tässä pelissä pelaat humaloituneena joulupukkina hänen korkea koulu opiskelija aikana metropoliassa."
         "Tehtäväsi on simppeli matkusta ympäri suomea keräämässä kaikenlaisia merkkejä joita voit kiinitää haalareihisi."
         "Keräämäsi merkit näkyvät joulupukki hahmossasi joka näkyy nurkassa ."
         " jotta voit liikua ympäri suomea tarvitset tietysti poltto ainetta, poltto aine on tietystikkin alkoholi.")

wrapper = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)

word_list = wrapper.wrap(text=lore)

def Paheelore():
    return word_list