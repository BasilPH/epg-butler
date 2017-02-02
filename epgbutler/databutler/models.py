from django.db import models
import json
from django.conf import settings
import os


# Create your models here.
class Program(object):
    def __init__(self, id, title, events):
        self.id = id
        self.events = events or []
        self.title = title


def get_programs():
    return [Program(1, 'Tennis AU Final', [[1485678720, 'R. Federer, loses the game with a forehand Unforced Error.'],
                                           [1485678968, 'R. Nadal, loses the game with a backhand Forced Error.'],
                                           [1485679206, 'R. Federer, loses the game with a backhand Forced Error.'],
                                           [1485679427, 'R. Nadal, loses the game with a backhand Forced Error.'],
                                           [1485679573, 'R. Federer, loses the game with a forehand Forced Error.'],
                                           [1485679764, 'R. Nadal, loses the game with a forehand Forced Error.'],
                                           [1485680205, 'R. Federer, wins the game with an ace.'],
                                           [1485680441, 'R. Nadal, wins the game with a forehand Winner.'],
                                           [1485680651, 'R. Federer, wins the set with an ace.'],
                                           [1485681021, 'R. Nadal, wins the game with an ace.'],
                                           [1485681859, 'R. Federer, loses the game with a backhand Forced Error.'],
                                           [1485682701, 'R. Federer, wins the game with a forehand Winner.'],
                                           [1485682855, 'R. Federer, loses the game with a backhand Forced Error.'],
                                           [1485683059, 'R. Federer, wins the game with a forehand Winner.'],
                                           [1485683199, 'R. Federer, loses the set with a forehand Forced Error.'],
                                           [1485683736, 'R. Nadal, loses the game with a forehand Forced Error.'],
                                           [1485684176, 'R. Federer, wins the game with an ace.'],
                                           [1485684800, 'R. Nadal, wins the game with a forehand Winner.'],
                                           [1485684894, 'R. Federer, wins the game with a forehand Winner.'],
                                           [1485685639, 'R. Federer, wins the set with a backhand Volley Winner.'],
                                           [1485686052, 'R. Federer, loses the game with a forehand Unforced Error.'],
                                           [1485686232, 'R. Federer, wins the game with a backhand Winner.'],
                                           [1485686444, 'R. Federer, loses the game with a forehand Forced Error.'],
                                           [1485687150, 'R. Nadal, wins the game with a forehand Winner.'],
                                           [1485687508, 'R. Federer, wins the game with an ace.'],
                                           [1485687643, 'R. Nadal, wins the game with an ace.'],
                                           [1485687911, 'R. Nadal, loses the game with a forehand Forced Error.'],
                                           [1485688036, 'R. Federer, loses the set with a backhand Unforced Error.'],
                                           [1485689180, 'R. Federer, loses the game with a forehand Unforced Error.'],
                                           [1485689317, 'R. Federer, wins the game with a backhand Winner.'],
                                           [1485689830, 'R. Federer, loses the game with a backhand Forced Error.'],
                                           [1485689988, 'R. Nadal, loses the game with a backhand Unforced Error.'],
                                           [1485690645, 'R. Federer, wins the game with an ace.'],
                                           [1485691647, 'R. Federer, wins the match with a forehand Winner.']]),
            Program(2, 'Hockey Cup', [[1485974640, 'Herzlich Willkommen '],
                                      [1485975000, 'Genf jagt den ersten Titel seit 1972 '],
                                      [1485975300, 'Für einen Tag die Sorgen aus der Liga ausblenden '],
                                      [1485976440, 'Gleich geht es los'],
                                      [1485976560, 'Das Spiel beginnt'],
                                      [1485976680, 'Die erste Chance'],
                                      [1485976980, 'Genf mit einem guten Schuss auf das Tor'],
                                      [1485977280, "Shore's Schuss knapp am Tor vorbei"],
                                      [1485977400, 'Grosschance für Kloten'],
                                      [1485977460,
                                       'Genoway mit einem kapitalen Fehlpass. Er spielt hinter dem Tor blind '
                                       'zurück, wodurch Spaling an die Scheibe kommt. Dieser spielt auf Gerbe, der '
                                       'ungehindert einschieben kann.TOR '],
                                      [1485977580,
                                       'Der Ausgleich folgt sogleich. Sanguinetti zieht bei einem Konter vom linken '
                                       'Flügel ab. Dem Torhüter kann bei diesem Präzisionsschuss kein Vorwurf '
                                       'gemacht werden.\xa0TOR '],
                                      [1485977700, 'Kloten versucht nachzudoppeln'],
                                      [1485977760, 'Das 2. Drittel startet'],
                                      [1485977880, 'Simek vergibt vor Gerber'],
                                      [1485978060,
                                       '2 Minuten Genf-Servette: Vukovic (Haken)Die 1. Strafe des Spiels ist '
                                       'Tatsache. Vukovic hakt beim Gegenspieler ein und muss in die Kühlbox.'],
                                      [1485978060, 'Kloten verpasst die Führung'],
                                      [1485978120,
                                       'Und gleich noch eine Strafe. Dieses Mal muss Sheppard für 2 Minuten '
                                       'raus.\xa02 Minuten Kloten: Sheppard (Haken)'],
                                      [1485978240,
                                       'Antonietti zieht von der blauen Linie ab. Aus dem Getümmel fällt der '
                                       'abgewehrte Schuss vor die Füsse von Simek, der nur noch einschieben '
                                       'muss.TOR '],
                                      [1485978540,
                                       'Cunti versucht sich durchzusetzen, was ihm jedoch nicht gelingt. Die '
                                       'Scheibe gelangt aber zu Hollenstein, der präzise auf Ramholt spielt, '
                                       'welcher seinen 1. Saisontreffer erzielt.TOR '],
                                      [1485978540, 'Kay Schweri im Interview'],
                                      [1485978600,
                                       'Kloten kann die Vorteile erst gegen Ende des Drittels ausnützen'],
                                      [1485978660,
                                       '2 Minuten Genf-Servette: Jacquemet (Haken)Mit Jacquemet muss erneut ein '
                                       'Genfer 2 Minuten auf die Strafbank.'],
                                      [1485978900,
                                       'Praplan setzt sich auf dem linken Flügel gegen Löffel durch, zieht in die '
                                       'Mitte und schiesst ein.TOR '],
                                      [1485978900, 'Schlussdrittel'],
                                      [1485979200,
                                       '2 Minuten Kloten: M.Gerber (Stockschlag)Gerber erhält eine Strafe. Leone '
                                       'geht für seinen Torhüter raus.'],
                                      [1485979320, 'Luca Cunti über das 1. Drittel'],
                                      [1485979440,
                                       'Das ist die Entscheidung. Leone kann nach einem Zuspiel von Obrist alleine '
                                       'auf Mayer zulaufen und versenkt die Scheibe im Tor.TOR '],
                                      [1485979440,
                                       'Mit einem Traumpass spielt Ramholt Bieber frei. Dieser verwertet eiskalt in '
                                       'die rechte obere Ecke.TOR '],
                                      [1485979620,
                                       '2 Minuten Genf-Servette: Almond (Crosscheck)Almond begeht ein Foul in der '
                                       'offensiven Zone und muss darum für 2 Minuten raus.'],
                                      [1485979980, 'Genf versucht es ein letztes Mal'],
                                      [1485980040,
                                       'Kurz vor Schluss muss noch je 1 Spieler auf die Strafbank.2 Minuten '
                                       'Genf-Servette: J.Wick (Übertriebene Härte)'],
                                      [1485980040, '2 Minuten Kloten: Harlacher (Übertriebene Härte)'],
                                      [1485981300, 'Erneut ein ausgeglichenes Drittel'],
                                      [1485981420, 'Juraj Simek im Interview'],
                                      [1485982440, ''],
                                      [1485984360, 'Kloten gewinnt den Schweizer Eishockey-Cup!'],
                                      [1485984540, 'Matthias Bieber über den Sieg'],
                                      [1485984600, 'Vincent Praplan im Interview'],
                                      [1485985080, 'Die Pokalübergabe ']])]


class Friend(object):
    def __init__(self, id, name, events):
        self.id = id
        self.events = events or []
        self.name = name


def get_friends():
    with open(os.path.join(settings.BASE_DIR, 'databutler/data/channel_switch_dump.json')) as f:
        events = json.load(f)

    return [Friend(1, 'Markus', events)]
