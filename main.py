import pandas as pd

# Datei umbenennen
data = pd.read_csv('test_daten_3.csv')

# Funktionen für Datenbereinigung
def religion_bereinigen(religion):
    religion = str(religion).lower()
    religionen_zu_bereinigen = [
        (['ev', 'evan', 'ev.', 'evang.', 'evan.', 'evangelisch', 'luth', 'Luth.', 'ev.-luth.', 'Lut.', 'ev. l.',
          'protestant.', 'prot', 'protest.', 'pro.', 'prot.', 'ev.diss.', 'REF.', 'bapt.', 'Baptist'], 'evangelisch'),
        (['kath', 'rk', 'Kath.', 'rk.', 'röm.kath.', 'r.kath.', 'rkath.', 'Cath', 'R. Kath', 'cath.', 'R.Kath', 'R.K.', 'R. Kath.', 'k',
          'gk', 'gr.kath', 'gr.kath.', 'Gr.k', 'griech.-kath.', 'Gr. Kath.', 'Gr. Kath',
          'Gr. Kath', 'griech.-kath.', 'Gr. Kath.', 'Gr.k', 'gr.kath.', 'gr.kath', 'gk'], 'katholisch'),
        (['jud', 'jud.', 'Jude', 'jued.', 'Jüd.', 'isr', 'Heb.', 'Israel', 'isreal.', 'hebr', 'hebr.', 'mos.', 'mos', 'mosaisch',
          'Isr.'], 'jüdisch'),
        (['keine', 'gottlos', 'ohne', 'diss.', 'DIS.', 'G.G.', 'GG'], 'keine'),
        (['g.o.', 'gr.orthodox', 'Gr. Orth.', 'gr.orth.', 'Gr. Ort.', 'Gr.Or.', 'gr.ort.', 'gr.-orth.', 'gr.orthod.', 'R.Orth.', ''], 'orthodox'),
        (['Moslem', 'isl', 'Islam', 'moham.', 'moh.', 'moh'], 'muslimisch'),
        (['2', '-', 'm', 'Gr.', 'Ggt.'], 'unbekannt'),
        (['w.l.', 'Ned.'], 'sonstige')
    ]


    for arguments, value in religionen_zu_bereinigen:
        if any(argument in religion for argument in arguments):
            return value

    return 'ohne Angabe'


def geschlecht_bereinigen(geschlecht):
    geschlecht = str(geschlecht).lower()
    geschlechter_zu_bereinigen = [
        (['wg', 'f', ' w'], 'w'),
        ([' m'], 'm'),
        (['(?)', '24', '2  1/2'], 'unbekannt')
    ]
    for arguments, value in geschlechter_zu_bereinigen:
        if any(argument in geschlecht for argument in arguments):
            return value
    return 'ohne Angabe'


def familienstand_bereinigen(familienstand):
    familienstand = str(familienstand).lower()
    familienstaende_zu_bereinigen = [
        (['gesch', 'gesch.', ' gesch', 'dv'], 'geschieden'),
        (['Ww', 'Wwe', 'Wwer', 'Ww.', 'Wwe.', 'wd', 'Viuva', 'Viuvo', 'Verw'], 'verwitwet'),
        (['led', 'leggggggd', 'led.', ' led', 'ledig', 's', 'solteiro', 'lel', 'solteira'], 'ledig'),
        (['verh', 'ver', 'berh', 'verh.', ' verh', 'm', 'casado', 'casada', 'Ehefrau'], 'verheiratet'),
        (['getr.', 'getrennt'], 'getrennt lebend'),
        (['(?)', '[?]', '?', '23.03.1914', '02.11.1881', '28.12.1912', '01.06.1906', '21'], 'unbekannt')
    ]
    for arguments, value in familienstaende_zu_bereinigen:
        if any(argument in familienstand for argument in arguments):
            return value

    return 'ohne Angabe'


def volkszugehoerigkeit_bereinigen(volkszugehoerigkeit):  # noch unvollstaendig (gelbe Felder in Konkordanzliste)
    volkszugehoerigkeit = str(volkszugehoerigkeit).lower()
    volkszugehoerigkeiten_zu_bereinigen = [
        (['german', 'Auslandsdeutsch', 'deutsch', 'Deutsch.','germ.', ' german', 'Germane', 'germanisch', 'Germany'], 'deutsch'),
        ([' russian', 'Russe', 'russian', 'Russin', 'russisch'], 'russisch'),
        (['american'], 'amerikanisch'),
        (['arabian', 'S.A.U.'], 'saudi-arabisch'),
        (['armenian', 'Armenier'], 'armenisch'),
        (['belgian'], 'belgisch'),
        (['Boehme', 'Boehmen', 'bohemian', 'Böhme', 'Böhmen'], 'böhmisch'),
        (['Britisch', 'british'], 'britisch'),
        (['bulgar.', 'bulgarian', 'Bulgarien', 'Bulgarin'], 'bulgarisch'),
        (['Canada', 'canadian'], 'kanadisch'),
        (['China', 'Chinese'], 'chinesisch'),
        (['Croat', 'croat.', 'croate', 'croatian', 'croatien', 'Kroat', 'kroat.', 'Kroate', 'Kroatin', 'Kroatisch'], 'kroatisch'),
        (['cuban'], 'kubanisch'),
        (['Czech.', 'Czeche', 'tschech.', 'Tscheche', 'tschechian', 'Tschechin', 'Tschechisch'], 'tschechisch'),
        (['Daenisch', 'Däne', 'Dänem.', 'Dänemark', 'Dänisch', 'denish'], 'dänisch'),
        (['dutch', 'holl.', 'holland'], 'niederländisch'),
        (['engl', 'engl.', 'England', 'Engländer', 'english'], 'englisch'),  # englisch = britisch??
        (['Este', 'esthonian', 'esthuania', 'esthuanian', 'Estland', 'estonia'], 'estnisch'),
        (['finn.', 'Finnin', 'finnisch', 'finnish', 'Finnl.', 'Finnland'], 'finnisch'),
        (['Flame', 'flemish'], 'flämisch'),
        (['franz.', 'french'], 'französisch'),
        (['greek', 'griech', 'Grieche'], 'griechisch'),
        (['hungarian', 'hungary', 'Magyar', 'Ungar', 'ungar.', 'ungarisch', 'Ungarn'], 'ungarisch'),
        (['Irisch', 'irish'], 'irisch'),
        (['italian', 'Italien'], 'italienisch'),
        (['Japan', 'Japaner', 'Japanerin', 'japanese'], 'japanisch'),
        (['Jugos.', 'jugosl.', 'Jugoslave', 'Jugoslaw.', 'Jugoslawe', 'Jugoslawien', 'Jugoslawin', 'jugoslawisch',
          'yougosl.', 'Yougoslavia', 'Yugoslave'], 'jugoslawisch'),
        (['Katalane', 'span.', 'Spanien', 'Spanier', 'Spanierin', 'spanisch', 'spanish'], 'spanisch'),
        (['latvian', 'lett', 'lett.', 'Lette', 'Lettin', 'Lettland'], 'lettisch'),
        (['Libanon'], 'libanesisch'),
        (['lit.', 'Litauen', 'Litauisch', 'lith', 'Lith.', 'lithuanian', 'lithvian'], 'litauisch'),
        (['Marokko'], 'marokkanisch'),
        (['mexican'], 'mexikanisch'),
        (['norw', 'Norw.', 'norweg.', 'Norwegen'], 'norwegisch'),
        (['oester', 'oesterr.', 'Oesterreich', 'öster.', 'österr.', 'Österreich'], 'österreischisch'),
        (['peruan.'], 'peruanisch'),
        (['philipine', 'philipp.'], 'philippinisch'),
        (['poland', 'Pole', 'Polen', 'Polin', 'polish', 'poln.', 'Polnisch'], 'polnisch'),
        (['roum.', 'roumania', 'roumanian', 'Ruemaen.', 'rum.', 'rumaen.', 'Rumaene', 'Rumaenien', 'Rumän.', 'Rumäne',
          'Rumänien', 'Rumänisch'], 'rumänisch'),
        (['Schwede', 'Schweden', 'schwedisch', 'sweden', 'swedish'], 'schwedisch'),
        (['schweiz', 'schweiz.', 'Schweizer', 'Schweizerin', 'swiss'], 'schweizerisch'),
        (['scotch'], 'schottisch'),
        (['Serbe', 'serbian', 'Serbien'], 'serbisch'),
        (['slov.', 'slovac', 'Slovak', 'slovak.', 'Slovake', 'Slovakei', 'slovakian', 'slovakin', 'slovakisch',
          'Slow.', 'slowak.', 'Slowake', 'Slowakin', 'slowakisch'], 'slowakisch'),
        (['slovenian', 'Slovenin', 'Slowene', 'Slowenien'], 'slowenisch'),
        (['south african'], 'südafrikanisch'),
        (['syrian', 'Syrier'], 'syrisch'),
        (['türk.', 'Türke', 'Türkei', 'Turkey', 'Türkisch', 'turkish'], 'türkisch'),
        (['ukrainian'], 'ukrainisch'),
        (['Venezuela'], 'venezolanisch'),
        (['1', 'ab Cherbourgh gereist', 'gestrichen', 'J.', 'Mischling', 'ohne', 'reist ab Southampton'], 'unbekannt')
    ]

    for arguments, value in volkszugehoerigkeiten_zu_bereinigen:
        if any(argument in volkszugehoerigkeit for argument in arguments):
            return value

    return 'ohne Angabe'


def staatsangehoerigkeit_bereinigen(staatsangehoerigkeit):
    staatsangehoerigkeit = str(staatsangehoerigkeit).lower()
    staatsangehoerigkeiten_zu_bereinigen = [
        ([' Deutsch', ' Germany', 'Aachen', 'Achstetten', 'Arnstorf', 'Bad Homburg', 'Baden', 'Balduinstein',
          'Barmen', 'Bayern', 'Berlin', 'Bochum', 'Brandenburg', 'Braunschweig', 'Bremen', 'Bremerhaven', 'Chemnitz',
          'Deutscch', 'Deutsch', 'Dortmund', 'Drangstedt', 'Dresden', 'Duisburg', 'Düsseldorf', 'Erfurt', 'Erlenbach',
          'Essen', 'Fehrenbruch', 'Feuerbach', 'Frankfurt', 'Germany', 'Germnay', 'Greifswald', 'Greiz', 'Hamburg',
          'Hannover', 'Harz', 'Hemelingen', 'Hessen', 'Hessen-Darmstadt', 'Hessen-Nassau', 'Hildesheim', 'Hof',
          'Hohenlimburg', 'Hohenzollern', 'Karlsruhe', 'Kassel', 'Kiel', 'Kirchweyhe', 'Klein Krotzenburg', 'Köln',
          'Leipzig', 'Lesum', 'Liensfeld b Eutin', 'Lippe Detmold', 'Lippe-Detmold', 'Lohne', 'Lübeck', 'Ludwigshafen',
          'Luebeck', 'Magdeburg', 'Mannheim', 'Marburg', 'Mecklenburg', 'Mecklenburg-Schwerin', 'Mecklenburg-Strelitz',
          'München', 'Münster', 'Münvhen', 'Nauheim', 'Nürnberg', 'Oldenburg', 'Pforzheim', 'Pommern', 'Potsdam',
          'Preussen', 'Rastatt', 'Sachsen', 'Sachsen-Altenburg', 'Sachsen-Anhalt', 'Sachsen-Meiningen', 'Sachsen-Weimar',
          'Sachsen-Weimar-Eisenach', 'Schleswig Holstein', 'Schwarzburg-Sondershausen', 'Sebaldsbrück', 'Stuttgart',
          'Sudwalde', 'Theuma', 'Thüringen', 'Ulm', 'Untertürkheim', 'Vegesack', 'Waldeck', 'Wesermünde', 'Westfalen',
          'Wittenberg', 'Wuerttemberg', 'Wunsdorf', 'Wuppertal', 'Württemberg'], 'Deutschland'),
        ([' Grossbritannien', 'Great Britain', 'Groosbritannien', 'Grossbritannien', 'Großbritannien', 'N. Ireland'],
         'Großbritannien'),
        ([' Kanada', 'Canada', 'Kanada', 'Kanda', 'Montreal, QC', 'New Brunswick', 'Richmond Hill', 'Toronto, Ont.'], 'Kanada'),
        ([' Schweiz', 'Eien', 'Schlieren', 'Schweiz', 'Switzerland', 'Zürich'], 'Schweiz'),
        ([' USA', '"USC, * Detroit;MI"', 'Bronx', 'Brooklyn', 'Chicago', 'Cincinnati', 'Cleveland', 'Dallas', 'Detroit',
           'Eliszabeth', 'Farmingdale', 'Garfield', 'Johnson City', 'Lansford', 'Los Angeles', 'Maywood', 'Merrick', 'Milwaukee',
           'New Haven', 'New York', 'New York City', 'Newark', 'Philadelphia', 'Piqua', 'Rockford', 'Salt lake City', 'U S A', 'Union City',
           'USA', 'USA', 'Whittier', 'Woodmere'], 'USA'),
        (['Aegypten', 'Ägypten'], 'Ägypten'),
        (['Afghanistan'], 'Afghanistan'),
        (['Albanien'], 'Albanien'),
        (['Arabien'], 'Arabien'),
        (['Argentine', 'Argentinien'], 'Argentinien'),
        (['Armenien'], 'Armenien'),
        (['Atzgersdorf', 'Austria', 'Innsbruck', 'Oesterreich', 'Österreich', 'Steiermark', 'Tirol', 'Übr. Österreich', 'Übr.Oesterreich',
          'Übrig. Österreich', 'Ueb. Österreich', 'Uebr. Oesterreich', 'Uebr. Österreich', 'Uebr.Oesterreich', 'Uebrig. Oesterreich',
          'Uebrig.Oesterreich', 'Uebriges Oesterreich', 'Wien'], 'Österreich'),
        (['(?)', 'unbekannt', 'unbestimmt'], 'unbekannt'),
        ([' Without', 'keine', 'keinem Staat angeh.', 'none', 'ohne', 'ohne Nationalität', 'ohne Staatsang.', 'staatenlos',
          'stateless', 'wirhout', 'without'], 'ohne'),
        (['keine Angabe', 'ohne Ang', 'ohne Angabe'], 'keine Angabe'),
        (['Venecuela', 'Venezuela'], 'Venezuela'),
        (['Uruguay', 'Uruquay', 'Uruquay'], 'Uruguay'),
        (['Hungary', 'Magyar', 'Sopron', 'Ungarn', 'Varosloed'], 'Ungarn'),
        (['Ukraine'], 'Ukraine'),
        (['Istambul', 'Tuerkei', 'Türkei', 'Turkey'], 'Türkei'),
        (['C. S. R.', 'C.S.R.', 'CSR', 'CZ-SL', 'Cz-Sl.', 'CZ.-SL.', 'Czechoslovakia', 'Tschechoslawakei', 'Tschechoslowakei',
          'Tschechosolwakei', 'Tschechslowakei', 'Tschechtttttttttttttoslowakei'], 'Tschechoslowakei'),
        (['Thailand'], 'Thailand'),
        (['South Africa', 'Süd Afrika', 'Südafrika', 'Südafrikanische Union', 'Sued Afrika', 'Suedafrika', 'Transvaal'], 'Südafrika'),
        (['Syrien'], 'Syrien'),
        (['Spain', 'Spanien'], 'Spanien'),
        (['Krain', 'Slowenien'], 'Slowenien'),
        (['Stiavnik', 'Zilina'], 'Slowakei'),
        (['Serbien'], 'Serbien'),
        (['Schweden', 'Sweden'], 'Schweden'),
        (['Schottland'], 'Schottland'),
        (['Moskau', 'Russia', 'Russland', 'Rußland'], 'Russland'),
        (['Mercurea', 'Roumania', 'Rumaenien', 'Rumänien', 'Rumänin'], 'Rumänien'),
        (['Portugal'], 'Portugal'),
        (['Poland', 'Polen', 'Posen', 'Warschau', 'Wimsdorf'], 'Polen'),
        (['Philippinen', 'Phillip. Islands'], 'Philippinen'),
        (['Peru'], 'Peru'),
        (['Paraguay', 'Paraquay'], 'Paraguay'),
        (['Panama'], 'Panama'),
        (['Palaestina', 'Palästina', 'Palestina', 'Palestine'], 'Palästina'),
        (['Norway', 'Norwegen'], 'Norwegen'),
        (['Den Haag', 'Holland', 'Netherlands', 'Niederlande'], 'Niederlande'),
        (['Nicaragua'], 'Nicaragua'),
        (['Montenegro'], 'Montenegro'),
        (['Guadalajara', 'Mexico', 'Mexico City', 'Mexiko'], 'Mexiko'),
        (['Macedonien', 'Mazedonien'], 'Mazedonien'),
        (['Marokko'], 'Marokko'),
        (['Luxemburg'], 'Luxemburg'),
        (['Litauen', 'Lith.', 'Lithuania', 'Lithuania/Memelland', 'Lithvia', 'Memel', 'Memelgebiet'], 'Litauen'),
        (['Lichtenstein', 'Liechtenstein'], 'Liechtenstein'),
        (['Liberia'], 'Liberia'),
        (['Libanon'], 'Libanon'),
        (['Latvia', 'Lettland', 'Riga'], 'Lettland'),
        (['Cuba', 'Kuba', 'La Habana'], 'Kuba'),
        (['Croatien', 'Kroatien'], 'Kroatien'),
        (['Columbia', 'Columbien', 'Kolumbien'], 'Kolumbien'),
        (['Jugoslavia', 'Jugoslavien', 'Jugoslawien', 'Yougoslavia', 'Yugoslavia'], 'Jugoslawien'),
        (['Japan'], 'Japan'),
        (['Italien', 'Italy'], 'Italien'),
        (['Island'], 'Island'),
        (['Ireland', 'Irland'], 'Irland'),
        (['Iran'], 'Iran'),
        (['Irak'], 'Irak'),
        (['Sumatra'], 'Indonesien'),
        (['Indien', 'Ost-Indien'], 'Indien'),
        (['Honduras'], 'Honduras'),
        (['Haiti'], 'Haiti'),
        (['Guatemala'], 'Guatemala'),
        (['Greece', 'Griechenland'], 'Griechenland'),
        (['France', 'Frankreich'], 'Frankreich'),
        (['Finland', 'Finnland'], 'Finnland'),
        (['Esthonia', 'Esthuania', 'Estland', 'Estonia', 'Estonian'], 'Estland'),
        (['England', 'London'], 'England'),
        (['El Salvador'], 'El Salvador'),
        (['Ecuador', 'Ekuador', 'Equador'], 'Ecuador'),
        (['Daenemark', 'Dänemark', 'Denmark', 'Kopenhagen'], 'Dänemark'),
        (['Domingo', 'Dominikanische Republik', 'Santo Domingo'], 'Dominikanische Republik'),
        (['Dominica'], 'Dominica'),
        (['Costa Rica'], 'Costa Rica'),
        (['China'], 'China'),
        (['Chile'], 'Chile'),
        (['Boehmen', 'Bohemia', 'Böhmen'], 'Böhmen'),
        (['Bulgaria', 'Bulgarien', 'Bulgary'], 'Bulgarien'),
        (['Brasilien', 'Brazil', 'Salvador', 'San Salvador'], 'Brasilien'),
        (['Bosnien'], 'Bosnien'),
        (['Bolivien'], 'Bolivien'),
        (['Belgien', 'Belgium'], 'Belgien'),
        (['Australia', 'Australien'], 'Australien')

    ]

    for arguments, value in staatsangehoerigkeiten_zu_bereinigen:
        if any(argument in staatsangehoerigkeit for argument in arguments):
            return value

    return 'ohne Angabe'

# Daten bereinigen
data['Religion'] = data['Religion'].apply(religion_bereinigen)
data['Geschl'] = data['Geschl'].apply(geschlecht_bereinigen)
data['Fam_Stand'] = data['Fam_Stand'].apply(familienstand_bereinigen)
data['Volkszugehoerigkeit'] = data('Volkszugehoerigkeit').apply(volkszugehoerigkeit_bereinigen)
data['Staatsangehoerigkeit'] = data('Staatsangehoerigkeit').apply(staatsangehoerigkeit_bereinigen)

# Bereinigte Daten in neue CSV-Datei
data.to_csv('daten_normisiert.csv', index=False, encoding='utf-8-sig')
