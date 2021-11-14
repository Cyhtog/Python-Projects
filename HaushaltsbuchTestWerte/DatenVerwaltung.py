import json


class DatenVerwaltung():
    ausgabenDatenListe = []
    ausgabenMonatlichWiederholtDatenListe = []
    ausgabenJaehrlichWiederholtDatenListe = []

    def datenLaden(self):
        json_file1 = open("ausgaben.json", "r")
        inhalt = json_file1.read()
        DatenVerwaltung.ausgabenDatenListe = json.loads(inhalt)
        json_file1.close()

        json_file2 = open("ausgabenWiederholt.json", "r")
        inhalt = json_file2.read()
        DatenVerwaltung.ausgabenMonatlichWiederholtDatenListe = json.loads(inhalt)
        json_file2.close()

        json_file3 = open("ausgabenJaehrlichWiederholt.json", "r")
        inhalt = json_file3.read()
        DatenVerwaltung.ausgabenJaehrlichWiederholtDatenListe = json.loads(inhalt)
        json_file3.close()

    def datenSpeichern(self):

        into_json_string1 = json.dumps(DatenVerwaltung.ausgabenDatenListe)
        json_file1 = open("ausgaben.json", "w")
        json_file1.write(into_json_string1)
        json_file1.close()

        into_json_string2 = json.dumps(DatenVerwaltung.ausgabenMonatlichWiederholtDatenListe)
        json_file2 = open("ausgabenWiederholt.json", "w")
        json_file2.write(into_json_string2)
        json_file2.close()

        into_json_string3 = json.dumps(DatenVerwaltung.ausgabenJaehrlichWiederholtDatenListe)
        json_file3 = open("ausgabenJaehrlichWiederholt.json", "w")
        json_file3.write(into_json_string3)
        json_file3.close()