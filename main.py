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


# Daten bereinigen
data['Religion'] = data['Religion'].apply(religion_bereinigen)
data['Geschl'] = data['Geschl'].apply(geschlecht_bereinigen)
data['Fam_Stand'] = data['Fam_Stand'].apply(familienstand_bereinigen)

# Bereinigte Daten in neue CSV-Datei
data.to_csv('daten_normisiert.csv', index=False, encoding='utf-8-sig')
