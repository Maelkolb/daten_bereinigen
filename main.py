import pandas as pd

# Datei umbenennen
data = pd.read_csv('daten.csv')

# Funktionen für Datenbereinigung
def religion_bereinigen(religion):
    religion = str(religion).lower()
    religionen_zu_bereinigen = [
        (['ev', 'evan', 'ev.', 'evang.', 'evan.', 'evangelisch'], 'evangelisch'),
        (['kath', 'rk', 'Kath.', 'rk.', 'röm.kath.', 'r.kath.', 'rkath.', 'Cath', 'R. Kath', 'cath.', 'R.Kath', 'R.K.', 'R. Kath.', 'k'], 'römisch-katholisch'),
        (['jud', 'jud.', 'Jude', 'jued.', 'Jüd.', 'isr', 'Heb.', 'Israel', 'isreal.', 'hebr', 'hebr.', 'mos.', 'mos'], 'jüdisch'),
        (['gk', 'gr.kath', 'gr.kath.', 'Gr.k', 'griech.-kath.', 'Gr. Kath.', 'Gr. Kath'], 'griechisch-katholisch'),
        (['luth', 'Luth.', 'ev.-luth.', 'Lut.', 'ev. l.'], 'evangelisch-lutherisch'),
        (['protestant.', 'prot', 'protest.', 'pro.', 'prot.'], 'protestantisch'),
        (['REF.'], 'reformiert'),
        (['keine', 'gottlos', 'ohne', 'diss.', 'ev.diss.', 'DIS.', 'G.G.', 'GG'], 'konfessionslos'),
        (['g.o.', 'gr.orthodox', 'Gr. Orth.', 'gr.orth.', 'Gr. Ort.', 'Gr.Or.', 'gr.ort.', 'gr.-orth.', 'gr.orthod.'], 'griechisch-orthodox'),
        (['bapt.', 'Baptist'], 'baptistisch'),
        (['Gr. Kath', 'griech.-kath.', 'Gr. Kath.', 'Gr.k', 'gr.kath.', 'gr.kath', 'gk'], 'griechisch-katholisch'),
        (['Moslem', 'isl', 'Islam', 'moham.', 'moh.'], 'muslimisch')
    ]

    for arguments, value in religionen_zu_bereinigen:
        if any(argument in religion for argument in arguments):
            return value

    return religion

def geschlecht_bereinigen(geschlecht):
    geschlecht = str(geschlecht).lower()
    pass

# Daten bereinigen
data['Religion'] = data['Religion'].apply(religion_bereinigen)

# Bereinigte Daten in neue CSV-Datei
data.to_csv('religion_normisiert.csv', index=False, encoding='utf-8-sig')