# profilSpillet

Denne korte README beskriver, hvordan du hurtigt kommer i gang med
`profilSpillet`. Projektet er udviklet af Christian Baun og inspireret
af de mange personlighedsanalyser, han har taget under forskellige
arbejdsgivere.

**Formål:** 

- `profilSpillet` hjælper med at gøre personlighedsanalyser
som DISC eller Myers-Briggs (MBTI) mere tilgængelige og sjove, da
analyserne koges ned til blot en overskrift, et profilbillede og en
liste af nogle få egenskaber hos analysanden med tilhørende talværdi fra
1 til 99. Et slags 'bilkort'.\
(se `profile_generator.py`, `profiles.py`). 
Programmet er IKKE testet med DISC profiler, men blot med MBTI profiler fra
[PrinciplesYou](https://principlesyou.com/).

**Eksempel**

![Alan Turings profil genereret af profilSpillet.](profiles/bilkort_alan_turing.png)

**Forudsætninger:** 

- `python3` installeret på systemet. - Det anbefales
at bruge et virtuelt miljø (fx `.venv`).

**Opsætning (hurtig):**

1.  Opret og aktiver et virtuelt miljø (valgfrit, men anbefalet):

``` zsh
python3 -m venv .venv
source .venv/bin/activate
```

2.  Installer afhængigheder:

``` zsh
pip install --upgrade pip
pip install -r requirements.txt
```

3.  Placer dine billeder i mappen `images/` (projektet bruger denne
    mappe til profilbilleder).

4.  Opdater `profiles.py` med nye profiler eller ændringer. Filen
    indeholder strukturen for projektets profiler; tilføj eller rediger
    entries der.

    For at få information fra personlighedstest til profiles.py brugte jeg [Gemini Pro](https://gemini.google.com/app) som assistent. Men man kan gøre det selv.
    Jeg uploaded 10 personlighedsprofiler (.pdf) (udarbejdet med
    [PrinciplesYou](https://principlesyou.com/) ) samt filen profiles.py - og så
    bad jeg Gemini om at udvide profiles.py.

    Prompt:
    "Analyser og udtræk relevante informationer for alle PDF og tilføj deres profil til
    profiles.py"

    OBS: Min Gemini Pro gemmer ikke mine prompts og deler ikke mine informationer. 
    Vær altid bevidst om, hvordan din egen AI assistent fungerer, så du ikke kommer til at dele privat og sensitivt data om dig selv eller andre. 

**Eksempel på profil (Alan Turing):**

Her er et eksempel fra `profiles.py`:

```python
{
    "name": "ALAN TURING",
    "title": "THE CODEBREAKER",
    "image_base_name": "Alan",
    "theme_color": "#00b4d8", # Elektrisk Blå
    "stats": [
        ("LOGIK & MATEMATIK", 100),
        ("INNOVATION", 99),
        ("KRYPTERING", 98),
        ("STAMINA (LØB)", 94),
        ("SOCIAL KONFORMITET", 5)
    ],
    "ability_title": "UNIVERSAL MACHINE",
    "ability_desc": "Kan beregne det umulige og knække enhver kode."
}
```

Hver profil indeholder:
- `name` og `title`: Profilens navn og undertitel.
- `image_base_name`: Filnavn på billedet i `images/`-mappen (uden filendelse; programmet finder `.jpg`, `.png` osv.).
- `theme_color`: En hex-farve til UI-styling.
- `stats`: Liste med egenskaber og værdier (0–100).
- `ability_title` og `ability_desc`: En særlig evne for profilen.

5.  Kør generator / scripts:

``` zsh
python profile_generator.py
# eller kør individuelle scripts direkte med venv-python
./.venv/bin/python profile_generator.py
```

**Tips:** 

- Tjek hvilken Python-tolk der bruges:

``` zsh
which python
python -V
```

-   Hvis du bruger VS Code: vælg interpreter `./.venv/bin/python` via
    Command Palette → "Python: Select Interpreter".

**Git:** 

- Undgå at checke det virtuelle miljø ind. Tilføj følgende
linje til `.gitignore` hvis den ikke allerede findes:

```         
.venv/
```

**Ryd op / slet miljø:**

``` zsh
deactivate
rm -rf .venv
```

**Ændringer til profiler:** 

- Når du har tilføjet billeder, opdater også
`profiles.py` med matchende filnavne og meta-oplysninger for de nye
profiler. - Efter opdateringer kan du køre `profile_generator.py` igen
for at se effekten.
