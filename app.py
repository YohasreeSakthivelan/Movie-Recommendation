import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle
from flask import Flask, render_template, request
import pandas as pd
from io import BytesIO
import base64
 

app = Flask(__name__)
Gross=pickle.load(open('Gross.pkl','rb'))
gbr=pickle.load(open('gbr.pkl','rb'))

@app.route('/')

@app.route('/index')
def index():
	return render_template('index.html')
@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
   return render_template('upload.html')  	

@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Series_Title', inplace=True)
        return render_template("preview.html",df_view = df)	
    
@app.route('/predict')
def predict():
    return render_template('predict.html') 

# Load the model (ensure this path is correct)
 

@app.route('/prediction', methods=['POST'])
def prediction():
        resul = {}  # Default empty dictionary
        result = ''  # Default empty string

        if request.method == 'POST': 
                resul = request.form.to_dict()
                print(resul)

                MOVIE= request.form['movie'] 
                if MOVIE == 'The Shawshank Redemption':
                   choices = '0'
                elif MOVIE == 'The Godfather':
                    choices = '1'
                elif MOVIE == 'The Dark Knight':
                    choices = '2'
                elif MOVIE == 'The Godfather: Part II':
                    choices = '3'
                elif MOVIE == '12 Angry Men':
                    choices = '4'
                elif MOVIE == 'The Lord of the Rings: The Return of the King':
                    choices = '5'
                elif MOVIE == 'Pulp Fiction':
                    choices = '6'
                elif MOVIE == 'Schindler\'s List':
                    choices = '7'
                elif MOVIE == 'Inception':
                    choices = '8'
                elif MOVIE == 'Fight Club':
                    choices = '9'
                elif MOVIE == 'The Lord of the Rings: The Fellowship of the Ring':
                    choices = '10'
                elif MOVIE == 'Forrest Gump':
                    choices = '11'
                elif MOVIE == 'Il buono, il brutto, il cattivo':
                    choices = '12'
                elif MOVIE == 'The Lord of the Rings: The Two Towers':
                    choices = '13'
                elif MOVIE == 'The Matrix':
                    choices = '14'
                elif MOVIE == 'Goodfellas':
                    choices = '15'
                elif MOVIE == 'Star Wars: Episode V - The Empire Strikes Back':
                    choices = '16'
                elif MOVIE == 'One Flew Over the Cuckoo\'s Nest':
                    choices = '17'
                elif MOVIE == 'Hamilton':
                    choices = '18'
                elif MOVIE == 'Gisaengchung':
                    choices = '19'
                elif MOVIE == 'Soorarai Pottru':
                    choices = '20'
                elif MOVIE == 'Interstellar':
                    choices = '21'
                elif MOVIE == 'Cidade de Deus':
                    choices = '22'
                elif MOVIE == 'Sen to Chihiro no kamikakushi':
                    choices = '23'
                elif MOVIE == 'Saving Private Ryan':
                    choices = '24'
                elif MOVIE == 'The Green Mile':
                    choices = '25'
                elif MOVIE == 'La vita è bella':
                    choices = '26'
                elif MOVIE == 'Se7en':
                    choices = '27'
                elif MOVIE == 'The Silence of the Lambs':
                    choices = '28'
                elif MOVIE == 'Star Wars':
                    choices = '29'
                elif MOVIE == 'Seppuku':
                    choices = '30'
                elif MOVIE == 'Shichinin no samurai':
                    choices = '31'
                elif MOVIE == 'It\'s a Wonderful Life':
                    choices = '32'
                elif MOVIE == 'Joker':
                    choices = '33'
                elif MOVIE == 'Whiplash':
                    choices = '34'
                elif MOVIE == 'The Intouchables':
                    choices = '35'
                elif MOVIE == 'The Prestige':
                    choices = '36'
                elif MOVIE == 'The Departed':
                    choices = '37'
                elif MOVIE == 'The Pianist':
                    choices = '38'
                elif MOVIE == 'Gladiator':
                    choices = '39'
                elif MOVIE == 'American History X':
                    choices = '40'
                elif MOVIE == 'The Usual Suspects':
                    choices = '41'
                elif MOVIE == 'Léon':
                    choices = '42'
                elif MOVIE == 'The Lion King':
                    choices = '43'
                elif MOVIE == 'Terminator 2: Judgment Day':
                    choices = '44'
                elif MOVIE == 'Nuovo Cinema Paradiso':
                    choices = '45'
                elif MOVIE == 'Hotaru no haka':
                    choices = '46'
                elif MOVIE == 'Back to the Future':
                    choices = '47'
                elif MOVIE == 'Once Upon a Time in the West':
                    choices = '48'
                elif MOVIE == 'Psycho':
                    choices = '49'
                elif MOVIE == 'Casablanca':
                    choices = '50'
                elif MOVIE == 'Modern Times':
                    choices = '51'
                elif MOVIE == 'City Lights':
                    choices = '52'
                elif MOVIE == 'Capharnaüm':
                    choices = '53'
                elif MOVIE == 'Ayla: The Daughter of War':
                    choices = '54'
                elif MOVIE == 'Vikram Vedha':
                    choices = '55'
                elif MOVIE == 'Kimi no na wa.':
                    choices = '56'
                elif MOVIE == 'Dangal':
                    choices = '57'
                elif MOVIE == 'Spider-Man: Into the Spider-Verse':
                    choices = '58'
                elif MOVIE == 'Avengers: Endgame':
                    choices = '59'
                elif MOVIE == 'Avengers: Infinity War':
                    choices = '60'
                elif MOVIE == 'Coco':
                    choices = '61'
                elif MOVIE == 'Django Unchained':
                    choices = '62'
                elif MOVIE == 'The Dark Knight Rises':
                    choices = '63'
                elif MOVIE == '3 Idiots':
                    choices = '64'
                elif MOVIE == 'Taare Zameen Par':
                    choices = '65'
                elif MOVIE == 'WALL·E':
                    choices = '66'
                elif MOVIE == 'The Lives of Others':
                    choices = '67'
                elif MOVIE == 'Oldeuboi':
                    choices = '68'
                elif MOVIE == 'Memento':
                    choices = '69'
                elif MOVIE == 'Mononoke-hime':
                    choices = '70'
                elif MOVIE == 'Once Upon a Time in America':
                    choices = '71'
                elif MOVIE == 'Raiders of the Lost Ark':
                    choices = '72'
                elif MOVIE == 'The Shining':
                    choices = '73'
                elif MOVIE == 'Apocalypse Now':
                    choices = '74'
                elif MOVIE == 'Alien':
                    choices = '75'
                elif MOVIE == 'Anand':
                    choices = '76'
                elif MOVIE == 'Tengoku to jigoku':
                    choices = '77'
                elif MOVIE == 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb':
                    choices = '78'
                elif MOVIE == 'Witness for the Prosecution':
                    choices = '79'
                elif MOVIE == 'Paths of Glory':
                    choices = '80'
                elif MOVIE == 'Rear Window':
                    choices = '81'
                elif MOVIE == 'Sunset Blvd.':
                    choices = '82'
                elif MOVIE == 'The Great Dictator':
                    choices = '83'
                elif MOVIE == '1917':
                    choices = '84'
                elif MOVIE == 'Tumbbad':
                    choices = '85'
                elif MOVIE == 'Andhadhun':
                    choices = '86'
                elif MOVIE == 'Drishyam':
                    choices = '87'
                elif MOVIE == 'Jagten':
                    choices = '88'
                elif MOVIE == 'Jodaeiye Nader az Simin':
                    choices = '89'
                elif MOVIE == 'Incendies':
                    choices = '90'
                elif MOVIE == 'Miracle in cell NO.7':
                    choices = '91'
                elif MOVIE == 'Babam ve Oglum':
                    choices = '92'
                elif MOVIE == 'Inglourious Basterds':
                    choices = '93'
                elif MOVIE == 'Eternal Sunshine of the Spotless Mind':
                    choices = '94'
                elif MOVIE == 'Amélie':
                    choices = '95'
                elif MOVIE == 'Snatch':
                    choices = '96'
                elif MOVIE == 'Requiem for a Dream':
                    choices = '97'
                elif MOVIE == 'American Beauty':
                    choices = '98'
                elif MOVIE == 'Good Will Hunting':
                    choices = '99'
                elif MOVIE == 'Bacheha-Ye aseman':
                    choices = '100'
                elif MOVIE == 'Toy Story':
                    choices = '101'
                elif MOVIE == 'Braveheart':
                    choices = '102'
                elif MOVIE == 'Reservoir Dogs':
                    choices = '103'
                elif MOVIE == 'Full Metal Jacket':
                    choices = '104'
                elif MOVIE == 'Idi i smotri':
                    choices = '105'
                elif MOVIE == 'Aliens':
                    choices = '106'
                elif MOVIE == 'Amadeus':
                    choices = '107'
                elif MOVIE == 'Scarface':
                    choices = '108'
                elif MOVIE == 'Star Wars: Episode VI - Return of the Jedi':
                    choices = '109'
                elif MOVIE == 'Das Boot':
                    choices = '110'
                elif MOVIE == 'Taxi Driver':
                    choices = '111'
                elif MOVIE == 'The Sting':
                    choices = '112'
                elif MOVIE == 'A Clockwork Orange':
                    choices = '113'
                elif MOVIE == '2001: A Space Odyssey':
                    choices = '114'
                elif MOVIE == 'Per qualche dollaro in più':
                    choices = '115'
                elif MOVIE == 'Lawrence of Arabia':
                    choices = '116'
                elif MOVIE == 'The Apartment':
                    choices = '117'
                elif MOVIE == 'North by Northwest':
                    choices = '118'
                elif MOVIE == 'Vertigo':
                    choices = '119'
                elif MOVIE == 'Singin\' in the Rain':
                    choices = '120'
                elif MOVIE == 'Ikiru':
                    choices = '121'
                elif MOVIE == 'Ladri di biciclette':
                    choices = '122'
                elif MOVIE == 'Double Indemnity':
                    choices = '123'
                elif MOVIE == 'Citizen Kane':
                    choices = '124'
                elif MOVIE == 'M - Eine Stadt sucht einen Mörder':
                    choices = '125'
                elif MOVIE == 'Metropolis':
                    choices = '126'
                elif MOVIE == 'The Kid':
                    choices = '127'
                elif MOVIE == 'Chhichhore':
                    choices = '128'
                elif MOVIE == 'Uri: The Surgical Strike':
                    choices = '129'
                elif MOVIE == 'K.G.F: Chapter 1':
                    choices = '130'
                elif MOVIE == 'Green Book':
                    choices = '131'
                elif MOVIE == 'Three Billboards Outside Ebbing, Missouri':
                    choices = '132'
                elif MOVIE == 'Talvar':
                    choices = '133'
                elif MOVIE == 'Baahubali 2: The Conclusion':
                    choices = '134'
                elif MOVIE == 'Klaus':
                    choices = '135'
                elif MOVIE == 'Queen':
                    choices = '136'
                elif MOVIE == 'Mandariinid':
                    choices = '137'
                elif MOVIE == 'Bhaag Milkha Bhaag':
                    choices = '138'
                elif MOVIE == 'Gangs of Wasseypur':
                    choices = '139'
                elif MOVIE == 'Udaan':
                    choices = '140'
                elif MOVIE == 'Paan Singh Tomar':
                    choices = '141'
                elif MOVIE == 'El secreto de sus ojos':
                    choices = '142'
                elif MOVIE == 'Warrior':
                    choices = '143'
                elif MOVIE == 'Shutter Island':
                    choices = '144'
                elif MOVIE == 'Up':
                    choices = '145'
                elif MOVIE == 'The Wolf of Wall Street':
                    choices = '146'
                elif MOVIE == 'Chak De! India':
                    choices = '147'
                elif MOVIE == 'There Will Be Blood':
                    choices = '148'
                elif MOVIE == 'Pan\'s Labyrinth':
                    choices = '149'
                elif MOVIE == 'Toy Story 3':
                    choices = '150'
                elif MOVIE == 'V for Vendetta':
                    choices = '151'
                elif MOVIE == 'Rang De Basanti':
                    choices = '152'
                elif MOVIE == 'Black':
                    choices = '153'
                elif MOVIE == 'Batman Begins':
                    choices = '154'
                elif MOVIE == 'Swades: We, the People':
                    choices = '155'
                elif MOVIE == 'Der Untergang':
                    choices = '156'
                elif MOVIE == 'Hauru no ugoku shiro':
                    choices = '157'
                elif MOVIE == 'A Beautiful Mind':
                    choices = '158'
                elif MOVIE == 'Hera Pheri':
                    choices = '159'
                elif MOVIE == 'Lock, Stock and Two Smoking Barrels':
                    choices = '160'
                elif MOVIE == 'L.A. Confidential':
                    choices = '161'
                elif MOVIE == 'Eskiya':
                    choices = '162'
                elif MOVIE == 'Heat':
                    choices = '163'
                elif MOVIE == 'Casino':
                    choices = '164'
                elif MOVIE == 'Andaz Apna Apna':
                    choices = '165'
                elif MOVIE == 'Unforgiven':
                    choices = '166'
                elif MOVIE == 'Indiana Jones and the Last Crusade':
                    choices = '167'
                elif MOVIE == 'Dom za vesanje':
                    choices = '168'
                elif MOVIE == 'Tonari no Totoro':
                    choices = '169'
                elif MOVIE == 'Die Hard':
                    choices = '170'
                elif MOVIE == 'Ran':
                    choices = '171'
                elif MOVIE == 'Raging Bull':
                    choices = '172'
                elif MOVIE == 'Stalker':
                    choices = '173'
                elif MOVIE == 'Höstsonaten':
                    choices = '174'
                elif MOVIE == 'The Message':
                    choices = '175'
                elif MOVIE == 'Sholay':
                    choices = '176'
                elif MOVIE == 'Monty Python and the Holy Grail':
                    choices = '177'
                elif MOVIE == 'The Great Escape':
                    choices = '178'
                elif MOVIE == 'To Kill a Mockingbird':
                    choices = '179'
                elif MOVIE == 'Yôjinbô':
                    choices = '180'
                elif MOVIE == 'Judgment at Nuremberg':
                    choices = '181'
                elif MOVIE == 'Some Like It Hot':
                    choices = '182'
                elif MOVIE == 'Smultronstället':
                    choices = '183'
                elif MOVIE == 'Det sjunde inseglet':
                    choices = '184'
                elif MOVIE == 'Du rififi chez les hommes':
                    choices = '185'
                elif MOVIE == 'Dial M for Murder':
                    choices = '186'
                elif MOVIE == 'Tôkyô monogatari':
                    choices = '187'
                elif MOVIE == 'Rashômon':
                    choices = '188'
                elif MOVIE == 'All About Eve':
                    choices = '189'
                elif MOVIE == 'The Treasure of the Sierra Madre':
                    choices = '190'
                elif MOVIE == 'To Be or Not to Be':
                    choices = '191'
                elif MOVIE == 'The Gold Rush':
                    choices = '192'
                elif MOVIE == 'Sherlock Jr.':
                    choices = '193'
                elif MOVIE == 'Portrait de la jeune fille en feu':
                    choices = '194'
                elif MOVIE == 'Pink':
                    choices = '195'
                elif MOVIE == 'Koe no katachi':
                    choices = '196'
                elif MOVIE == 'Contratiempo':
                    choices = '197'
                elif MOVIE == 'Ah-ga-ssi':
                    choices = '198'
                elif MOVIE == 'Mommy':
                    choices = '199'
                elif MOVIE == 'Haider':
                    choices = '200'
                elif MOVIE == 'Logan':
                    choices = '201'
                elif MOVIE == 'Room':
                    choices = '202'
                elif MOVIE == 'Relatos salvajes':
                    choices = '203'
                elif MOVIE == 'Soul':
                    choices = '204'
                elif MOVIE == 'Kis Uykusu':
                    choices = '205'
                elif MOVIE == 'PK':
                    choices = '206'
                elif MOVIE == 'OMG: Oh My God!':
                    choices = '207'
                elif MOVIE == 'The Grand Budapest Hotel':
                    choices = '208'
                elif MOVIE == 'Gone Girl':
                    choices = '209'
                elif MOVIE == 'Ôkami kodomo no Ame to Yuki':
                    choices = '210'
                elif MOVIE == 'Hacksaw Ridge':
                    choices = '211'
                elif MOVIE == 'Inside Out':
                    choices = '212'
                elif MOVIE == 'Barfi!':
                    choices = '213'
                elif MOVIE == '12 Years a Slave':
                    choices = '214'
                elif MOVIE == 'Rush':
                    choices = '215'
                elif MOVIE == 'Ford v Ferrari':
                    choices = '216'
                elif MOVIE == 'Spotlight':
                    choices = '217'
                elif MOVIE == 'Song of the Sea':
                    choices = '218'
                elif MOVIE == 'Kahaani':
                    choices = '219'
                elif MOVIE == 'Zindagi Na Milegi Dobara':
                    choices = '220'
                elif MOVIE == 'Prisoners':
                    choices = '221'
                elif MOVIE == 'Mad Max: Fury Road':
                    choices = '222'
                elif MOVIE == 'A Wednesday':
                    choices = '223'
                elif MOVIE == 'Gran Torino':
                    choices = '224'
                elif MOVIE == 'Harry Potter and the Deathly Hallows: Part 2':
                    choices = '225'
                elif MOVIE == 'Okuribito':
                    choices = '226'
                elif MOVIE == 'Hachi: A Dog\'s Tale':
                    choices = '227'
                elif MOVIE == 'Mary and Max':
                    choices = '228'
                elif MOVIE == 'How to Train Your Dragon':
                    choices = '229'
                elif MOVIE == 'Into the Wild':
                    choices = '230'
                elif MOVIE == 'No Country for Old Men':
                    choices = '231'
                elif MOVIE == 'Lage Raho Munna Bhai':
                    choices = '232'
                elif MOVIE == 'Million Dollar Baby':
                    choices = '233'
                elif MOVIE == 'Hotel Rwanda':
                    choices = '234'
                elif MOVIE == 'Taegukgi hwinalrimyeo':
                    choices = '235'
                elif MOVIE == 'Before Sunset':
                    choices = '236'
                elif MOVIE == 'Munna Bhai M.B.B.S.':
                    choices = '237'
                elif MOVIE == 'Salinui chueok':
                    choices = '238'
                elif MOVIE == 'Dil Chahta Hai':
                    choices = '239'
                elif MOVIE == 'Kill Bill: Vol. 1':
                    choices = '240'
                elif MOVIE == 'Finding Nemo':
                    choices = '241'
                elif MOVIE == 'Catch Me If You Can':
                    choices = '242'
                elif MOVIE == 'Amores perros':
                    choices = '243'
                elif MOVIE == 'Monsters, Inc.':
                    choices = '244'
                elif MOVIE == 'Shin seiki Evangelion Gekijô-ban: Air/Magokoro wo, kimi ni':
                    choices = '245'
                elif MOVIE == 'Lagaan: Once Upon a Time in India':
                    choices = '246'
                elif MOVIE == 'The Sixth Sense':
                    choices = '247'
                elif MOVIE == 'La leggenda del pianista sull\'oceano':
                    choices = '248'
                elif MOVIE == 'The Truman Show':
                    choices = '249'
                elif MOVIE == 'Crna macka, beli macor':
                    choices = '250'
                elif MOVIE == 'The Big Lebowski':
                    choices = '251'
                elif MOVIE == 'Fa yeung nin wah':
                    choices = '252'
                elif MOVIE == 'Trainspotting':
                    choices = '253'
                elif MOVIE == 'Fargo':
                    choices = '254'
                elif MOVIE == 'Underground':
                    choices = '255'
                elif MOVIE == 'La haine':
                    choices = '256'
                elif MOVIE == 'Dilwale Dulhania Le Jayenge':
                    choices = '257'
                elif MOVIE == 'Before Sunrise':
                    choices = '258'
                elif MOVIE == 'Trois couleurs: Rouge':
                    choices = '259'
                elif MOVIE == 'Chung Hing sam lam':
                    choices = '260'
                elif MOVIE == 'Jurassic Park':
                    choices = '261'
                elif MOVIE == 'In the Name of the Father':
                    choices = '262'
                elif MOVIE == 'Ba wang bie ji':
                    choices = '263'
                elif MOVIE == 'Dà hóng denglong gaogao guà':
                    choices = '264'
                elif MOVIE == 'Dead Poets Society':
                    choices = '265'
                elif MOVIE == 'Stand by Me':
                    choices = '266'
                elif MOVIE == 'Platoon':
                    choices = '267'
                elif MOVIE == 'Paris, Texas':
                    choices = '268'
                elif MOVIE == 'Kaze no tani no Naushika':
                    choices = '269'
                elif MOVIE == 'The Thing':
                    choices = '270'
                elif MOVIE == 'Pink Floyd: The Wall':
                    choices = '271'
                elif MOVIE == 'Fitzcarraldo':
                    choices = '272'
                elif MOVIE == 'Fanny och Alexander':
                    choices = '273'
                elif MOVIE == 'Blade Runner':
                    choices = '274'
                elif MOVIE == 'The Elephant Man':
                    choices = '275'
                elif MOVIE == 'Life of Brian':
                    choices = '276'
                elif MOVIE == 'The Deer Hunter':
                    choices = '277'
                elif MOVIE == 'Rocky':
                    choices = '278'
                elif MOVIE == 'Network':
                    choices = '279'
                elif MOVIE == 'Barry Lyndon':
                    choices = '280'
                elif MOVIE == 'Zerkalo':
                    choices = '281'
                elif MOVIE == 'Chinatown':
                    choices = '282'
                elif MOVIE == 'Paper Moon':
                    choices = '283'
                elif MOVIE == 'Viskningar och rop':
                    choices = '284'
                elif MOVIE == 'Solaris':
                    choices = '285'
                elif MOVIE == 'Le samouraï':
                    choices = '286'
                elif MOVIE == 'Cool Hand Luke':
                    choices = '287'
                elif MOVIE == 'Persona':
                    choices = '288'
                elif MOVIE == 'Andrei Rublev':
                    choices = '289'
                elif MOVIE == 'La battaglia di Algeri':
                    choices = '290'
                elif MOVIE == 'El ángel exterminador':
                    choices = '291'
                elif MOVIE == 'What Ever Happened to Baby Jane?':
                    choices = '292'
                elif MOVIE == 'Sanjuro':
                    choices = '293'
                elif MOVIE == 'The Man Who Shot Liberty Valance':
                    choices = '294'
                elif MOVIE == 'Ivanovo detstvo':
                    choices = '295'
                elif MOVIE == 'Jungfrukällan':
                    choices = '296'
                elif MOVIE == 'Inherit the Wind':
                    choices = '297'
                elif MOVIE == 'Les quatre cents coups':
                    choices = '298'
                elif MOVIE == 'Ben-Hur':
                    choices = '299'
                elif MOVIE == 'Kakushi-toride no san-akunin':
                    choices = '300'
                elif MOVIE == 'Le notti di Cabiria':
                    choices = '301'
                elif MOVIE == 'Kumonosu-jô':
                    choices = '302'
                elif MOVIE == 'The Bridge on the River Kwai':
                    choices = '303'
                elif MOVIE == 'On the Waterfront':
                    choices = '304'
                elif MOVIE == 'Le salaire de la peur':
                    choices = '305'
                elif MOVIE == 'Ace in the Hole':
                    choices = '306'
                elif MOVIE == 'White Heat':
                    choices = '307'
                elif MOVIE == 'The Third Man':
                    choices = '308'
                elif MOVIE == 'The Red Shoes':
                    choices = '309'
                elif MOVIE == 'The Shop Around the Corner':
                    choices = '310'
                elif MOVIE == 'Rebecca':
                    choices = '311'
                elif MOVIE == 'Mr. Smith Goes to Washington':
                    choices = '312'
                elif MOVIE == 'Gone with the Wind':
                    choices = '313'
                elif MOVIE == 'La Grande Illusion':
                    choices = '314'
                elif MOVIE == 'It Happened One Night':
                    choices = '315'
                elif MOVIE == 'La passion de Jeanne d\'Arc':
                    choices = '316'
                elif MOVIE == 'The Circus':
                    choices = '317'
                elif MOVIE == 'Sunrise: A Song of Two Humans':
                    choices = '318'
                elif MOVIE == 'The General':
                    choices = '319'
                elif MOVIE == 'Das Cabinet des Dr. Caligari':
                    choices = '320'
                elif MOVIE == 'Badhaai ho':
                    choices = '321'
                elif MOVIE == 'Togo':
                    choices = '322'
                elif MOVIE == 'Airlift':
                    choices = '323'
                elif MOVIE == 'Bajrangi Bhaijaan':
                    choices = '324'
                elif MOVIE == 'Baby':
                    choices = '325'
                elif MOVIE == 'La La Land':
                    choices = '326'
                elif MOVIE == 'Lion':
                    choices = '327'
                elif MOVIE == 'The Martian':
                    choices = '328'
                elif MOVIE == 'Zootopia':
                    choices = '329'
                elif MOVIE == 'Bãhubali: The Beginning':
                    choices = '330'
                elif MOVIE == 'Kaguyahime no monogatari':
                    choices = '331'
                elif MOVIE == 'Wonder':
                    choices = '332'
                elif MOVIE == 'Gully Boy':
                    choices = '333'
                elif MOVIE == 'Special Chabbis':
                    choices = '334'
                elif MOVIE == 'Short Term 12':
                    choices = '335'
                elif MOVIE == 'Serbuan maut 2: Berandal':
                    choices = '336'
                elif MOVIE == 'The Imitation Game':
                    choices = '337'
                elif MOVIE == 'Guardians of the Galaxy':
                    choices = '338'
                elif MOVIE == 'Blade Runner 2049':
                    choices = '339'
                elif MOVIE == 'Her':
                    choices = '340'
                elif MOVIE == 'Bohemian Rhapsody':
                    choices = '341'
                elif MOVIE == 'The Revenant':
                    choices = '342'
                elif MOVIE == 'The Perks of Being a Wallflower':
                    choices = '343'
                elif MOVIE == 'Tropa de Elite 2: O Inimigo Agora é Outro':
                    choices = '344'
                elif MOVIE == 'The King\'s Speech':
                    choices = '345'
                elif MOVIE == 'The Help':
                    choices = '346'
                elif MOVIE == 'Deadpool':
                    choices = '347'
                elif MOVIE == 'Darbareye Elly':
                    choices = '348'
                elif MOVIE == 'Dev.D':
                    choices = '349'
                elif MOVIE == 'Yip Man':
                    choices = '350'
                elif MOVIE == 'My Name Is Khan':
                    choices = '351'
                elif MOVIE == 'Nefes: Vatan Sagolsun':
                    choices = '352'
                elif MOVIE == 'Slumdog Millionaire':
                    choices = '353'
                elif MOVIE == 'Black Swan':
                    choices = '354'
                elif MOVIE == 'Tropa de Elite':
                    choices = '355'
                elif MOVIE == 'The Avengers':
                    choices = '356'
                elif MOVIE == 'Persepolis':
                    choices = '357'
                elif MOVIE == 'Dallas Buyers Club':
                    choices = '358'
                elif MOVIE == 'The Pursuit of Happyness':
                    choices = '359'
                elif MOVIE == 'Blood Diamond':
                    choices = '360'
                elif MOVIE == 'The Bourne Ultimatum':
                    choices = '361'
                elif MOVIE == 'Bin-jip':
                    choices = '362'
                elif MOVIE == 'Sin City':
                    choices = '363'
                elif MOVIE == 'Le scaphandre et le papillon':
                    choices = '364'
                elif MOVIE == 'G.O.R.A.':
                    choices = '365'
                elif MOVIE == 'Ratatouille':
                    choices = '366'
                elif MOVIE == 'Casino Royale':
                    choices = '367'
                elif MOVIE == 'Kill Bill: Vol. 2':
                    choices = '368'
                elif MOVIE == 'Vozvrashchenie':
                    choices = '369'
                elif MOVIE == 'Bom Yeoareum Gaeul Gyeoul Geurigo Bom':
                    choices = '370'
                elif MOVIE == 'Mar adentro':
                    choices = '371'
                elif MOVIE == 'Cinderella Man':
                    choices = '372'
                elif MOVIE == 'Kal Ho Naa Ho':
                    choices = '373'
                elif MOVIE == 'Mou gaan dou':
                    choices = '374'
                elif MOVIE == 'Pirates of the Caribbean: The Curse of the Black Pearl':
                    choices = '375'
                elif MOVIE == 'Big Fish':
                    choices = '376'
                elif MOVIE == 'The Incredibles':
                    choices = '377'
                elif MOVIE == 'Yeopgijeogin geunyeo':
                    choices = '378'
                elif MOVIE == 'Dogville':
                    choices = '379'
                elif MOVIE == 'Vizontele':
                    choices = '380'
                elif MOVIE == 'Donnie Darko':
                    choices = '381'
                elif MOVIE == 'Magnolia':
                    choices = '382'
                elif MOVIE == 'Dancer in the Dark':
                    choices = '383'
                elif MOVIE == 'The Straight Story':
                    choices = '384'
                elif MOVIE == 'Pâfekuto burû':
                    choices = '385'
                elif MOVIE == 'Festen':
                    choices = '386'
                elif MOVIE == 'Central do Brasil':
                    choices = '387'
                elif MOVIE == 'The Iron Giant':
                    choices = '388'
                elif MOVIE == 'Knockin\' on Heaven\'s Door':
                    choices = '389'
                elif MOVIE == 'Sling Blade':
                    choices = '390'
                elif MOVIE == 'Secrets & Lies':
                    choices = '391'
                elif MOVIE == 'Twelve Monkeys':
                    choices = '392'
                elif MOVIE == 'Kôkaku Kidôtai':
                    choices = '393'
                elif MOVIE == 'The Nightmare Before Christmas':
                    choices = '394'
                elif MOVIE == 'Groundhog Day':
                    choices = '395'
                elif MOVIE == 'Bound by Honor':
                    choices = '396'
                elif MOVIE == 'Scent of a Woman':
                    choices = '397'
                elif MOVIE == 'Aladdin':
                    choices = '398'
                elif MOVIE == 'JFK':
                    choices = '399'
                elif MOVIE == 'Beauty and the Beast':
                    choices = '400'
                elif MOVIE == 'Dances with Wolves':
                    choices = '401'
                elif MOVIE == 'Do the Right Thing':
                    choices = '402'
                elif MOVIE == 'Rain Man':
                    choices = '403'
                elif MOVIE == 'Akira':
                    choices = '404'
                elif MOVIE == 'The Princess Bride':
                    choices = '405'
                elif MOVIE == 'Der Himmel über Berlin':
                    choices = '406'
                elif MOVIE == 'Au revoir les enfants':
                    choices = '407'
                elif MOVIE == 'Tenkû no shiro Rapyuta':
                    choices = '408'
                elif MOVIE == 'The Terminator':
                    choices = '409'
                elif MOVIE == 'Gandhi':
                    choices = '410'
                elif MOVIE == 'Kagemusha':
                    choices = '411'
                elif MOVIE == 'Being There':
                    choices = '412'
                elif MOVIE == 'Annie Hall':
                    choices = '413'
                elif MOVIE == 'Jaws':
                    choices = '414'
                elif MOVIE == 'Dog Day Afternoon':
                    choices = '415'
                elif MOVIE == 'Young Frankenstein':
                    choices = '416'
                elif MOVIE == 'Papillon':
                    choices = '417'
                elif MOVIE == 'The Exorcist':
                    choices = '418'
                elif MOVIE == 'Sleuth':
                    choices = '419'
                elif MOVIE == 'The Last Picture Show':
                    choices = '420'
                elif MOVIE == 'Fiddler on the Roof':
                    choices = '421'
                elif MOVIE == 'Il conformista':
                    choices = '422'
                elif MOVIE == 'Butch Cassidy and the Sundance Kid':
                    choices = '423'
                elif MOVIE == 'Rosemary\'s Baby':
                    choices = '424'
                elif MOVIE == 'Planet of the Apes':
                    choices = '425'
                elif MOVIE == 'The Graduate':
                    choices = '426'
                elif MOVIE == 'Who\'s Afraid of Virginia Woolf?':
                    choices = '427'
                elif MOVIE == 'The Sound of Music':
                    choices = '428'
                elif MOVIE == 'Doctor Zhivago':
                    choices = '429'
                elif MOVIE == 'Per un pugno di dollari':
                    choices = '430'
                elif MOVIE == '8½':
                    choices = '431'
                elif MOVIE == 'Vivre sa vie: Film en douze tableaux':
                    choices = '432'
                elif MOVIE == 'The Hustler':
                    choices = '433'
                elif MOVIE == 'La dolce vita':
                    choices = '434'
                elif MOVIE == 'Rio Bravo':
                    choices = '435'
                elif MOVIE == 'Anatomy of a Murder':
                    choices = '436'
                elif MOVIE == 'Touch of Evil':
                    choices = '437'
                elif MOVIE == 'Cat on a Hot Tin Roof':
                    choices = '438'
                elif MOVIE == 'Sweet Smell of Success':
                    choices = '439'
                elif MOVIE == 'The Killing':
                    choices = '440'
                elif MOVIE == 'The Night of the Hunter':
                    choices = '441'
                elif MOVIE == 'La Strada':
                    choices = '442'
                elif MOVIE == 'Les diaboliques':
                    choices = '443'
                elif MOVIE == 'Stalag 17':
                    choices = '444'
                elif MOVIE == 'Roman Holiday':
                    choices = '445'
                elif MOVIE == 'A Streetcar Named Desire':
                    choices = '446'
                elif MOVIE == 'In a Lonely Place':
                    choices = '447'
                elif MOVIE == 'Kind Hearts and Coronets':
                    choices = '448'
                elif MOVIE == 'Rope':
                    choices = '449'
                elif MOVIE == 'Out of the Past':
                    choices = '450'
                elif MOVIE == 'Brief Encounter':
                    choices = '451'
                elif MOVIE == 'Laura':
                    choices = '452'
                elif MOVIE == 'The Best Years of Our Lives':
                    choices = '453'
                elif MOVIE == 'Arsenic and Old Lace':
                    choices = '454'
                elif MOVIE == 'The Maltese Falcon':
                    choices = '455'
                elif MOVIE == 'The Grapes of Wrath':
                    choices = '456'
                elif MOVIE == 'The Wizard of Oz':
                    choices = '457'
                elif MOVIE == 'La règle du jeu':
                    choices = '458'
                elif MOVIE == 'The Thin Man':
                    choices = '459'
                elif MOVIE == 'All Quiet on the Western Front':
                    choices = '460'
                elif MOVIE == 'Bronenosets Potemkin':
                    choices = '461'
                elif MOVIE == 'Knives Out':
                    choices = '462'
                elif MOVIE == 'Dil Bechara':
                    choices = '463'
                elif MOVIE == 'Manbiki kazoku':
                    choices = '464'
                elif MOVIE == 'Marriage Story':
                    choices = '465'
                elif MOVIE == 'Call Me by Your Name':
                    choices = '466'
                elif MOVIE == 'I, Daniel Blake':
                    choices = '467'
                elif MOVIE == 'Isle of Dogs':
                    choices = '468'
                elif MOVIE == 'Hunt for the Wilderpeople':
                    choices = '469'
                elif MOVIE == 'Captain Fantastic':
                    choices = '470'
                elif MOVIE == 'Sing Street':
                    choices = '471'
                elif MOVIE == 'Thor: Ragnarok':
                    choices = '472'
                elif MOVIE == 'Nightcrawler':
                    choices = '473'
                elif MOVIE == 'Jojo Rabbit':
                    choices = '474'
                elif MOVIE == 'Arrival':
                    choices = '475'
                elif MOVIE == 'Star Wars: Episode VII - The Force Awakens':
                    choices = '476'
                elif MOVIE == 'Before Midnight':
                    choices = '477'
                elif MOVIE == 'X-Men: Days of Future Past':
                    choices = '478'
                elif MOVIE == 'Bir Zamanlar Anadolu\'da':
                    choices = '479'
                elif MOVIE == 'The Artist':
                    choices = '480'
                elif MOVIE == 'Edge of Tomorrow':
                    choices = '481'
                elif MOVIE == 'Amour':
                    choices = '482'
                elif MOVIE == 'The Irishman':
                    choices = '483'
                elif MOVIE == 'Un prophète':
                    choices = '484'
                elif MOVIE == 'Moon':
                    choices = '485'
                elif MOVIE == 'Låt den rätte komma in':
                    choices = '486'
                elif MOVIE == 'District 9':
                    choices = '487'
                elif MOVIE == 'The Wrestler':
                    choices = '488'
                elif MOVIE == 'Jab We Met':
                    choices = '489'
                elif MOVIE == 'Boyhood':
                    choices = '490'
                elif MOVIE == '4 luni, 3 saptamâni si 2 zile':
                    choices = '491'
                elif MOVIE == 'Star Trek':
                    choices = '492'
                elif MOVIE == 'In Bruges':
                    choices = '493'
                elif MOVIE == 'The Man from Earth':
                    choices = '494'
                elif MOVIE == 'Letters from Iwo Jima':
                    choices = '495'
                elif MOVIE == 'The Fall':
                    choices = '496'
                elif MOVIE == 'Life of Pi':
                    choices = '497'
                elif MOVIE == 'Fantastic Mr. Fox':
                    choices = '498'
                elif MOVIE == 'C.R.A.Z.Y.':
                    choices = '499'
                elif MOVIE == 'Les choristes':
                    choices = '500'
                elif MOVIE == 'Iron Man':
                    choices = '501'
                elif MOVIE == 'Shaun of the Dead':
                    choices = '502'
                elif MOVIE == 'Gegen die Wand':
                    choices = '503'
                elif MOVIE == 'Mystic River':
                    choices = '504'
                elif MOVIE == 'Harry Potter and the Prisoner of Azkaban':
                    choices = '505'
                elif MOVIE == 'Ying xiong':
                    choices = '506'
                elif MOVIE == 'Hable con ella':
                    choices = '507'
                elif MOVIE == 'No Man\'s Land':
                    choices = '508'
                elif MOVIE == 'Cowboy Bebop: Tengoku no tobira':
                    choices = '509'
                elif MOVIE == 'The Bourne Identity':
                    choices = '510'
                elif MOVIE == 'Nueve reinas':
                    choices = '511'
                elif MOVIE == 'Children of Men':
                    choices = '512'
                elif MOVIE == 'Almost Famous':
                    choices = '513'
                elif MOVIE == 'Mulholland Dr.':
                    choices = '514'
                elif MOVIE == 'Toy Story 2':
                    choices = '515'
                elif MOVIE == 'Boogie Nights':
                    choices = '516'
                elif MOVIE == 'Mimi wo sumaseba':
                    choices = '517'
                elif MOVIE == 'Once Were Warriors':
                    choices = '518'
                elif MOVIE == 'True Romance':
                    choices = '519'
                elif MOVIE == 'Trois couleurs: Bleu':
                    choices = '520'
                elif MOVIE == 'Jûbê ninpûchô':
                    choices = '521'
                elif MOVIE == 'Carlito\'s Way':
                    choices = '522'
                elif MOVIE == 'Edward Scissorhands':
                    choices = '523'
                elif MOVIE == 'My Left Foot: The Story of Christy Brown':
                    choices = '524'
                elif MOVIE == 'Crimes and Misdemeanors':
                    choices = '525'
                elif MOVIE == 'The Untouchables':
                    choices = '526'
                elif MOVIE == 'Hannah and Her Sisters':
                    choices = '527'
                elif MOVIE == 'Brazil':
                    choices = '528'
                elif MOVIE == 'This Is Spinal Tap':
                    choices = '529'
                elif MOVIE == 'A Christmas Story':
                    choices = '530'
                elif MOVIE == 'The Blues Brothers':
                    choices = '531'
                elif MOVIE == 'Manhattan':
                    choices = '532'
                elif MOVIE == 'All That Jazz':
                    choices = '533'
                elif MOVIE == 'Dawn of the Dead':
                    choices = '534'
                elif MOVIE == 'All the President\'s Men':
                    choices = '535'
                elif MOVIE == 'La montaña sagrada':
                    choices = '536'
                elif MOVIE == 'Amarcord':
                    choices = '537'
                elif MOVIE == 'Le charme discret de la bourgeoisie':
                    choices = '538'
                elif MOVIE == 'Aguirre, der Zorn Gottes':
                    choices = '539'
                elif MOVIE == 'Harold and Maude':
                    choices = '540'
                elif MOVIE == 'Patton':
                    choices = '541'
                elif MOVIE == 'The Wild Bunch':
                    choices = '542'
                elif MOVIE == 'Night of the Living Dead':
                    choices = '543'
                elif MOVIE == 'The Lion in Winter':
                    choices = '544'
                elif MOVIE == 'In the Heat of the Night':
                    choices = '545'
                elif MOVIE == 'Charade':
                    choices = '546'
                elif MOVIE == 'The Manchurian Candidate':
                    choices = '547'
                elif MOVIE == 'Spartacus':
                    choices = '548'
                elif MOVIE == 'L\'avventura':
                    choices = '549'
                elif MOVIE == 'Hiroshima mon amour':
                    choices = '550'
                elif MOVIE == 'The Ten Commandments':
                    choices = '551'
                elif MOVIE == 'The Searchers':
                    choices = '552'
                elif MOVIE == 'East of Eden':
                    choices = '553'
                elif MOVIE == 'High Noon':
                    choices = '554'
                elif MOVIE == 'Strangers on a Train':
                    choices = '555'
                elif MOVIE == 'Harvey':
                    choices = '556'
                elif MOVIE == 'Miracle on 34th Street':
                    choices = '557'
                elif MOVIE == 'Notorious':
                    choices = '558'
                elif MOVIE == 'The Big Sleep':
                    choices = '559'
                elif MOVIE == 'The Lost Weekend':
                    choices = '560'
                elif MOVIE == 'The Philadelphia Story':
                    choices = '561'
                elif MOVIE == 'His Girl Friday':
                    choices = '562'
                elif MOVIE == 'The Adventures of Robin Hood':
                    choices = '563'
                elif MOVIE == 'A Night at the Opera':
                    choices = '564'
                elif MOVIE == 'King Kong':
                    choices = '565'
                elif MOVIE == 'Freaks':
                    choices = '566'
                elif MOVIE == 'Nosferatu':
                    choices = '567'
                elif MOVIE == 'The Gentlemen':
                    choices = '568'
                elif MOVIE == 'Raazi':
                    choices = '569'
                elif MOVIE == 'Sound of Metal':
                    choices = '570'
                elif MOVIE == 'Forushande':
                    choices = '571'
                elif MOVIE == 'Dunkirk':
                    choices = '572'
                elif MOVIE == 'Perfetti sconosciuti':
                    choices = '573'
                elif MOVIE == 'Hidden Figures':
                    choices = '574'
                elif MOVIE == 'Paddington 2':
                    choices = '575'
                elif MOVIE == 'Udta Punjab':
                    choices = '576'
                elif MOVIE == 'Kubo and the Two Strings':
                    choices = '577'
                elif MOVIE == 'M.S. Dhoni: The Untold Story':
                    choices = '578'
                elif MOVIE == 'Manchester by the Sea':
                    choices = '579'
                elif MOVIE == 'Under sandet':
                    choices = '580'
                elif MOVIE == 'Rogue One':
                    choices = '581'
                elif MOVIE == 'Captain America: Civil War':
                    choices = '582'
                elif MOVIE == 'The Hateful Eight':
                    choices = '583'
                elif MOVIE == 'Little Women':
                    choices = '584'
                elif MOVIE == 'Loving Vincent':
                    choices = '585'
                elif MOVIE == 'Pride':
                    choices = '586'
                elif MOVIE == 'Le passé':
                    choices = '587'
                elif MOVIE == 'La grande bellezza':
                    choices = '588'
                elif MOVIE == 'The Lunchbox':
                    choices = '589'
                elif MOVIE == 'Vicky Donor':
                    choices = '590'
                elif MOVIE == 'Big Hero 6':
                    choices = '591'
                elif MOVIE == 'About Time':
                    choices = '592'
                elif MOVIE == 'English Vinglish':
                    choices = '593'
                elif MOVIE == 'Kaze tachinu':
                    choices = '594'
                elif MOVIE == 'Toy Story 4':
                    choices = '595'
                elif MOVIE == 'La migliore offerta':
                    choices = '596'
                elif MOVIE == 'Moonrise Kingdom':
                    choices = '597'
                elif MOVIE == 'How to Train Your Dragon 2':
                    choices = '598'
                elif MOVIE == 'The Big Short':
                    choices = '599'
                elif MOVIE == 'Kokuhaku':
                    choices = '600'
                elif MOVIE == 'Ang-ma-reul bo-at-da':
                    choices = '601'
                elif MOVIE == 'The Girl with the Dragon Tattoo':
                    choices = '602'
                elif MOVIE == 'Captain Phillips':
                    choices = '603'
                elif MOVIE == 'Ajeossi':
                    choices = '604'
                elif MOVIE == 'Straight Outta Compton':
                    choices = '605'
                elif MOVIE == 'Madeo':
                    choices = '606'
                elif MOVIE == 'Chugyeokja':
                    choices = '607'
                elif MOVIE == 'The Hobbit: The Desolation of Smaug':
                    choices = '608'
                elif MOVIE == 'Das weiße Band - Eine deutsche Kindergeschichte':
                    choices = '609'
                elif MOVIE == 'Män som hatar kvinnor':
                    choices = '610'
                elif MOVIE == 'The Trial of the Chicago 7':
                    choices = '611'
                elif MOVIE == 'Druk':
                    choices = '612'
                elif MOVIE == 'The Fighter':
                    choices = '613'
                elif MOVIE == 'Taken':
                    choices = '614'
                elif MOVIE == 'The Boy in the Striped Pyjamas':
                    choices = '615'
                elif MOVIE == 'Once':
                    choices = '616'
                elif MOVIE == 'The Hobbit: An Unexpected Journey':
                    choices = '617'
                elif MOVIE == 'Auf der anderen Seite':
                    choices = '618'
                elif MOVIE == 'Atonement':
                    choices = '619'
                elif MOVIE == 'Drive':
                    choices = '620'
                elif MOVIE == 'American Gangster':
                    choices = '621'
                elif MOVIE == 'Avatar':
                    choices = '622'
                elif MOVIE == 'Mr. Nobody':
                    choices = '623'
                elif MOVIE == 'Apocalypto':
                    choices = '624'
                elif MOVIE == 'Little Miss Sunshine':
                    choices = '625'
                elif MOVIE == 'Hot Fuzz':
                    choices = '626'
                elif MOVIE == 'The Curious Case of Benjamin Button':
                    choices = '627'
                elif MOVIE == 'Veer-Zaara':
                    choices = '628'
                elif MOVIE == 'Adams æbler':
                    choices = '629'
                elif MOVIE == 'Pride & Prejudice':
                    choices = '630'
                elif MOVIE == 'The World\'s Fastest Indian':
                    choices = '631'
                elif MOVIE == 'Tôkyô goddofâzâzu':
                    choices = '632'
                elif MOVIE == 'Serenity':
                    choices = '633'
                elif MOVIE == 'Walk the Line':
                    choices = '634'
                elif MOVIE == 'Ondskan':
                    choices = '635'
                elif MOVIE == 'The Notebook':
                    choices = '636'
                elif MOVIE == 'Diarios de motocicleta':
                    choices = '637'
                elif MOVIE == 'Lilja 4-ever':
                    choices = '638'
                elif MOVIE == 'Les triplettes de Belleville':
                    choices = '639'
                elif MOVIE == 'Gongdong gyeongbi guyeok JSA':
                    choices = '640'
                elif MOVIE == 'The Count of Monte Cristo':
                    choices = '641'
                elif MOVIE == 'Waking Life':
                    choices = '642'
                elif MOVIE == 'Remember the Titans':
                    choices = '643'
                elif MOVIE == 'Wo hu cang long':
                    choices = '644'
                elif MOVIE == 'Todo sobre mi madre':
                    choices = '645'
                elif MOVIE == 'Cast Away':
                    choices = '646'
                elif MOVIE == 'The Boondock Saints':
                    choices = '647'
                elif MOVIE == 'The Insider':
                    choices = '648'
                elif MOVIE == 'October Sky':
                    choices = '649'
                elif MOVIE == 'Shrek':
                    choices = '650'
                elif MOVIE == 'Titanic':
                    choices = '651'
                elif MOVIE == 'Hana-bi':
                    choices = '652'
                elif MOVIE == 'Gattaca':
                    choices = '653'
                elif MOVIE == 'The Game':
                    choices = '654'
                elif MOVIE == 'Breaking the Waves':
                    choices = '655'
                elif MOVIE == 'Ed Wood':
                    choices = '656'
                elif MOVIE == 'What\'s Eating Gilbert Grape':
                    choices = '657'
                elif MOVIE == 'Tombstone':
                    choices = '658'
                elif MOVIE == 'The Sandlot':
                    choices = '659'
                elif MOVIE == 'The Remains of the Day':
                    choices = '660'
                elif MOVIE == 'Naked':
                    choices = '661'
                elif MOVIE == 'The Fugitive':
                    choices = '662'
                elif MOVIE == 'A Bronx Tale':
                    choices = '663'
                elif MOVIE == 'Batman: Mask of the Phantasm':
                    choices = '664'
                elif MOVIE == 'Lat sau san taam':
                    choices = '665'
                elif MOVIE == 'Night on Earth':
                    choices = '666'
                elif MOVIE == 'La double vie de Véronique':
                    choices = '667'
                elif MOVIE == 'Boyz n the Hood':
                    choices = '668'
                elif MOVIE == 'Misery':
                    choices = '669'
                elif MOVIE == 'Awakenings':
                    choices = '670'
                elif MOVIE == 'Majo no takkyûbin':
                    choices = '671'
                elif MOVIE == 'Glory':
                    choices = '672'
                elif MOVIE == 'Dip huet seung hung':
                    choices = '673'
                elif MOVIE == 'Back to the Future Part II':
                    choices = '674'
                elif MOVIE == 'Mississippi Burning':
                    choices = '675'
                elif MOVIE == 'Predator':
                    choices = '676'
                elif MOVIE == 'Evil Dead II':
                    choices = '677'
                elif MOVIE == 'Ferris Bueller\'s Day Off':
                    choices = '678'
                elif MOVIE == 'Down by Law':
                    choices = '679'
                elif MOVIE == 'The Goonies':
                    choices = '680'
                elif MOVIE == 'The Color Purple':
                    choices = '681'
                elif MOVIE == 'The Breakfast Club':
                    choices = '682'
                elif MOVIE == 'The Killing Fields':
                    choices = '683'
                elif MOVIE == 'Ghostbusters':
                    choices = '684'
                elif MOVIE == 'The Right Stuff':
                    choices = '685'
                elif MOVIE == 'The King of Comedy':
                    choices = '686'
                elif MOVIE == 'E.T. the Extra-Terrestrial':
                    choices = '687'
                elif MOVIE == 'Kramer vs. Kramer':
                    choices = '688'
                elif MOVIE == 'Days of Heaven':
                    choices = '689'
                elif MOVIE == 'The Outlaw Josey Wales':
                    choices = '690'
                elif MOVIE == 'The Man Who Would Be King':
                    choices = '691'
                elif MOVIE == 'The Conversation':
                    choices = '692'
                elif MOVIE == 'La planète sauvage':
                    choices = '693'
                elif MOVIE == 'The Day of the Jackal':
                    choices = '694'
                elif MOVIE == 'Badlands':
                    choices = '695'
                elif MOVIE == 'Cabaret':
                    choices = '696'
                elif MOVIE == 'Willy Wonka & the Chocolate Factory':
                    choices = '697'
                elif MOVIE == 'Midnight Cowboy':
                    choices = '698'
                elif MOVIE == 'Wait Until Dark':
                    choices = '699'
                elif MOVIE == 'Guess Who\'s Coming to Dinner':
                    choices = '700'
                elif MOVIE == 'Bonnie and Clyde':
                    choices = '701'
                elif MOVIE == 'My Fair Lady':
                    choices = '702'
                elif MOVIE == 'Mary Poppins':
                    choices = '703'
                elif MOVIE == 'The Longest Day':
                    choices = '704'
                elif MOVIE == 'Jules et Jim':
                    choices = '705'
                elif MOVIE == 'The Innocents':
                    choices = '706'
                elif MOVIE == 'À bout de souffle':
                    choices = '707'
                elif MOVIE == 'Red River':
                    choices = '708'
                elif MOVIE == 'Key Largo':
                    choices = '709'
                elif MOVIE == 'To Have and Have Not':
                    choices = '710'
                elif MOVIE == 'Shadow of a Doubt':
                    choices = '711'
                elif MOVIE == 'Stagecoach':
                    choices = '712'
                elif MOVIE == 'The Lady Vanishes':
                    choices = '713'
                elif MOVIE == 'Bringing Up Baby':
                    choices = '714'
                elif MOVIE == 'Bride of Frankenstein':
                    choices = '715'
                elif MOVIE == 'Duck Soup':
                    choices = '716'
                elif MOVIE == 'Scarface: The Shame of the Nation':
                    choices = '717'
                elif MOVIE == 'Frankenstein':
                    choices = '718'
                elif MOVIE == 'Roma':
                    choices = '719'
                elif MOVIE == 'God\'s Own Country':
                    choices = '720'
                elif MOVIE == 'Deadpool 2':
                    choices = '721'
                elif MOVIE == 'Wind River':
                    choices = '722'
                elif MOVIE == 'Get Out':
                    choices = '723'
                elif MOVIE == 'Mission: Impossible - Fallout':
                    choices = '724'
                elif MOVIE == 'En man som heter Ove':
                    choices = '725'
                elif MOVIE == 'What We Do in the Shadows':
                    choices = '726'
                elif MOVIE == 'Omoide no Mânî':
                    choices = '727'
                elif MOVIE == 'The Theory of Everything':
                    choices = '728'
                elif MOVIE == 'Kingsman: The Secret Service':
                    choices = '729'
                elif MOVIE == 'The Fault in Our Stars':
                    choices = '730'
                elif MOVIE == 'Me and Earl and the Dying Girl':
                    choices = '731'
                elif MOVIE == 'Birdman or (The Unexpected Virtue of Ignorance)':
                    choices = '732'
                elif MOVIE == 'La vie d\'Adèle':
                    choices = '733'
                elif MOVIE == 'Kai po che!':
                    choices = '734'
                elif MOVIE == 'The Broken Circle Breakdown':
                    choices = '735'
                elif MOVIE == 'Captain America: The Winter Soldier':
                    choices = '736'
                elif MOVIE == 'Rockstar':
                    choices = '737'
                elif MOVIE == 'Nebraska':
                    choices = '738'
                elif MOVIE == 'Wreck-It Ralph':
                    choices = '739'
                elif MOVIE == 'Le Petit Prince':
                    choices = '740'
                elif MOVIE == 'Detachment':
                    choices = '741'
                elif MOVIE == 'Midnight in Paris':
                    choices = '742'
                elif MOVIE == 'The Lego Movie':
                    choices = '743'
                elif MOVIE == 'Gravity':
                    choices = '744'
                elif MOVIE == 'Star Trek Into Darkness':
                    choices = '745'
                elif MOVIE == 'Beasts of No Nation':
                    choices = '746'
                elif MOVIE == 'The Social Network':
                    choices = '747'
                elif MOVIE == 'X: First Class':
                    choices = '748'
                elif MOVIE == 'The Hangover':
                    choices = '749'
                elif MOVIE == 'Skyfall':
                    choices = '750'
                elif MOVIE == 'Silver Linings Playbook':
                    choices = '751'
                elif MOVIE == 'Argo':
                    choices = '752'
                elif MOVIE == '(500) Days of Summer':
                    choices = '753'
                elif MOVIE == 'Harry Potter and the Deathly Hallows: Part 1':
                    choices = '754'
                elif MOVIE == 'Gake no ue no Ponyo':
                    choices = '755'
                elif MOVIE == 'Frost/Nixon':
                    choices = '756'
                elif MOVIE == 'Papurika':
                    choices = '757'
                elif MOVIE == 'Changeling':
                    choices = '758'
                elif MOVIE == 'Flipped':
                    choices = '759'
                elif MOVIE == 'Toki o kakeru shôjo':
                    choices = '760'
                elif MOVIE == 'Death Note: Desu nôto':
                    choices = '761'
                elif MOVIE == 'This Is England':
                    choices = '762'
                elif MOVIE == 'Ex Machina':
                    choices = '763'
                elif MOVIE == 'Efter brylluppet':
                    choices = '764'
                elif MOVIE == 'The Last King of Scotland':
                    choices = '765'
                elif MOVIE == 'Zodiac':
                    choices = '766'
                elif MOVIE == 'Lucky Number Slevin':
                    choices = '767'
                elif MOVIE == 'Joyeux Noël':
                    choices = '768'
                elif MOVIE == 'Control':
                    choices = '769'
                elif MOVIE == 'Tangled':
                    choices = '770'
                elif MOVIE == 'Zwartboek':
                    choices = '771'
                elif MOVIE == 'Brokeback Mountain':
                    choices = '772'
                elif MOVIE == '3:10 to Yuma':
                    choices = '773'
                elif MOVIE == 'Crash':
                    choices = '774'
                elif MOVIE == 'Kung fu':
                    choices = '775'
                elif MOVIE == 'The Bourne Supremacy':
                    choices = '776'
                elif MOVIE == 'The Machinist':
                    choices = '777'
                elif MOVIE == 'Ray':
                    choices = '778'
                elif MOVIE == 'Lost in Translation':
                    choices = '779'
                elif MOVIE == 'Harry Potter and the Goblet of Fire':
                    choices = '780'
                elif MOVIE == 'Man on Fire':
                    choices = '781'
                elif MOVIE == 'Coraline':
                    choices = '782'
                elif MOVIE == 'The Last Samurai':
                    choices = '783'
                elif MOVIE == 'The Magdalene Sisters':
                    choices = '784'
                elif MOVIE == 'Good Bye Lenin!':
                    choices = '785'
                elif MOVIE == 'In America':
                    choices = '786'
                elif MOVIE == 'I Am Sam':
                    choices = '787'
                elif MOVIE == 'Adaptation.':
                    choices = '788'
                elif MOVIE == 'Black Hawk Down':
                    choices = '789'
                elif MOVIE == 'Road to Perdition':
                    choices = '790'
                elif MOVIE == 'Das Experiment':
                    choices = '791'
                elif MOVIE == 'Billy Elliot':
                    choices = '792'
                elif MOVIE == 'Hedwig and the Angry Inch':
                    choices = '793'
                elif MOVIE == 'Ocean\'s Eleven':
                    choices = '794'
                elif MOVIE == 'Vampire Hunter D: Bloodlust':
                    choices = '795'
                elif MOVIE == 'O Brother, Where Art Thou?':
                    choices = '796'
                elif MOVIE == 'Interstate 60: Episodes of the Road':
                    choices = '797'
                elif MOVIE == 'South Park: Bigger, Longer & Uncut':
                    choices = '798'
                elif MOVIE == 'Office Space':
                    choices = '799'
                elif MOVIE == 'Happiness':
                    choices = '800'
                elif MOVIE == 'Training Day':
                    choices = '801'
                elif MOVIE == 'Rushmore':
                    choices = '802'
                elif MOVIE == 'Abre los ojos':
                    choices = '803'
                elif MOVIE == 'Being John Malkovich':
                    choices = '804'
                elif MOVIE == 'As Good as It Gets':
                    choices = '805'
                elif MOVIE == 'The Fifth Element':
                    choices = '806'
                elif MOVIE == 'Le dîner de cons':
                    choices = '807'
                elif MOVIE == 'Donnie Brasco':
                    choices = '808'
                elif MOVIE == 'Shine':
                    choices = '809'
                elif MOVIE == 'Primal Fear':
                    choices = '810'
                elif MOVIE == 'Hamlet':
                    choices = '811'
                elif MOVIE == 'A Little Princess':
                    choices = '812'
                elif MOVIE == 'Do lok tin si':
                    choices = '813'
                elif MOVIE == 'Il postino':
                    choices = '814'
                elif MOVIE == 'Clerks':
                    choices = '815'
                elif MOVIE == 'Short Cuts':
                    choices = '816'
                elif MOVIE == 'Philadelphia':
                    choices = '817'
                elif MOVIE == 'The Muppet Christmas Carol':
                    choices = '818'
                elif MOVIE == 'Malcolm X':
                    choices = '819'
                elif MOVIE == 'The Last of the Mohicans':
                    choices = '820'
                elif MOVIE == 'Kurenai no buta':
                    choices = '821'
                elif MOVIE == 'Glengarry Glen Ross':
                    choices = '822'
                elif MOVIE == 'A Few Good Men':
                    choices = '823'
                elif MOVIE == 'Fried Green Tomatoes':
                    choices = '824'
                elif MOVIE == 'Barton Fink':
                    choices = '825'
                elif MOVIE == 'Miller\'s Crossing':
                    choices = '826'
                elif MOVIE == 'Who Framed Roger Rabbit':
                    choices = '827'
                elif MOVIE == 'Spoorloos':
                    choices = '828'
                elif MOVIE == 'Withnail & I':
                    choices = '829'
                elif MOVIE == 'The Last Emperor':
                    choices = '830'
                elif MOVIE == 'Empire of the Sun':
                    choices = '831'
                elif MOVIE == 'Der Name der Rose':
                    choices = '832'
                elif MOVIE == 'Blue Velvet':
                    choices = '833'
                elif MOVIE == 'The Purple Rose of Cairo':
                    choices = '834'
                elif MOVIE == 'After Hours':
                    choices = '835'
                elif MOVIE == 'Zelig':
                    choices = '836'
                elif MOVIE == 'The Verdict':
                    choices = '837'
                elif MOVIE == 'Star Trek II: The Wrath of Khan':
                    choices = '838'
                elif MOVIE == 'First Blood':
                    choices = '839'
                elif MOVIE == 'Ordinary People':
                    choices = '840'
                elif MOVIE == 'Airplane!':
                    choices = '841'
                elif MOVIE == 'Rupan sansei: Kariosutoro no shiro':
                    choices = '842'
                elif MOVIE == 'Halloween':
                    choices = '843'
                elif MOVIE == 'Le locataire':
                    choices = '844'
                elif MOVIE == 'Love and Death':
                    choices = '845'
                elif MOVIE == 'The Taking of Pelham One Two Three':
                    choices = '846'
                elif MOVIE == 'Blazing Saddles':
                    choices = '847'
                elif MOVIE == 'Serpico':
                    choices = '848'
                elif MOVIE == 'Enter the Dragon':
                    choices = '849'
                elif MOVIE == 'Deliverance':
                    choices = '850'
                elif MOVIE == 'The French Connection':
                    choices = '851'
                elif MOVIE == 'Dirty Harry':
                    choices = '852'
                elif MOVIE == 'Where Eagles Dare':
                    choices = '853'
                elif MOVIE == 'The Odd Couple':
                    choices = '854'
                elif MOVIE == 'The Dirty Dozen':
                    choices = '855'
                elif MOVIE == 'Belle de jour':
                    choices = '856'
                elif MOVIE == 'A Man for All Seasons':
                    choices = '857'
                elif MOVIE == 'Repulsion':
                    choices = '858'
                elif MOVIE == 'Zulu':
                    choices = '859'
                elif MOVIE == 'Goldfinger':
                    choices = '860'
                elif MOVIE == 'The Birds':
                    choices = '861'
                elif MOVIE == 'Cape Fear':
                    choices = '862'
                elif MOVIE == 'Peeping Tom':
                    choices = '863'
                elif MOVIE == 'The Magnificent Seven':
                    choices = '864'
                elif MOVIE == 'Les yeux sans visage':
                    choices = '865'
                elif MOVIE == 'Invasion of the Body Snatchers':
                    choices = '866'
                elif MOVIE == 'Rebel Without a Cause':
                    choices = '867'
                elif MOVIE == 'The Ladykillers':
                    choices = '868'
                elif MOVIE == 'Sabrina':
                    choices = '869'
                elif MOVIE == 'The Quiet Man':
                    choices = '870'
                elif MOVIE == 'The Day the Earth Stood Still':
                    choices = '871'
                elif MOVIE == 'The African Queen':
                    choices = '872'
                elif MOVIE == 'Gilda':
                    choices = '873'
                elif MOVIE == 'Fantasia':
                    choices = '874'
                elif MOVIE == 'The Invisible Man':
                    choices = '875'
                elif MOVIE == 'Dark Waters':
                    choices = '876'
                elif MOVIE == 'Searching':
                    choices = '877'
                elif MOVIE == 'Once Upon a Time... in Hollywood':
                    choices = '878'
                elif MOVIE == 'Nelyubov':
                    choices = '879'
                elif MOVIE == 'The Florida Project':
                    choices = '880'
                elif MOVIE == 'Just Mercy':
                    choices = '881'
                elif MOVIE == 'Gifted':
                    choices = '882'
                elif MOVIE == 'The Peanut Butter Falcon':
                    choices = '883'
                elif MOVIE == 'Victoria':
                    choices = '884'
                elif MOVIE == 'Mustang':
                    choices = '885'
                elif MOVIE == 'Guardians of the Galaxy Vol. 2':
                    choices = '886'
                elif MOVIE == 'Baby Driver':
                    choices = '887'
                elif MOVIE == 'Only the Brave':
                    choices = '888'
                elif MOVIE == 'Bridge of Spies':
                    choices = '889'
                elif MOVIE == 'Incredibles 2':
                    choices = '890'
                elif MOVIE == 'Moana':
                    choices = '891'
                elif MOVIE == 'Sicario':
                    choices = '892'
                elif MOVIE == 'Creed':
                    choices = '893'
                elif MOVIE == 'Leviafan':
                    choices = '894'
                elif MOVIE == 'Hell or High Water':
                    choices = '895'
                elif MOVIE == 'Philomena':
                    choices = '896'
                elif MOVIE == 'Dawn of the Planet of the Apes':
                    choices = '897'
                elif MOVIE == 'El cuerpo':
                    choices = '898'
                elif MOVIE == 'Serbuan maut':
                    choices = '899'
                elif MOVIE == 'End of Watch':
                    choices = '900'
                elif MOVIE == 'Kari-gurashi no Arietti':
                    choices = '901'
                elif MOVIE == 'A Star Is Born':
                    choices = '902'
                elif MOVIE == 'True Grit':
                    choices = '903'
                elif MOVIE == 'Hævnen':
                    choices = '904'
                elif MOVIE == 'Despicable Me':
                    choices = '905'
                elif MOVIE == '50/50':
                    choices = '906'
                elif MOVIE == 'Kick-Ass':
                    choices = '907'
                elif MOVIE == 'Celda 211':
                    choices = '908'
                elif MOVIE == 'Moneyball':
                    choices = '909'
                elif MOVIE == 'La piel que habito':
                    choices = '910'
                elif MOVIE == 'Zombieland':
                    choices = '911'
                elif MOVIE == 'Die Welle':
                    choices = '912'
                elif MOVIE == 'Sherlock Holmes':
                    choices = '913'
                elif MOVIE == 'The Blind Side':
                    choices = '914'
                elif MOVIE == 'The Visitor':
                    choices = '915'
                elif MOVIE == 'Seven Pounds':
                    choices = '916'
                elif MOVIE == 'Eastern Promises':
                    choices = '917'
                elif MOVIE == 'Stardust':
                    choices = '918'
                elif MOVIE == 'The Secret of Kells':
                    choices = '919'
                elif MOVIE == 'Inside Man':
                    choices = '920'
                elif MOVIE == 'Gone Baby Gone':
                    choices = '921'
                elif MOVIE == 'La Vie En Rose':
                    choices = '922'
                elif MOVIE == 'Huo Yuan Jia':
                    choices = '923'
                elif MOVIE == 'The Illusionist':
                    choices = '924'
                elif MOVIE == 'Dead Man\'s Shoes':
                    choices = '925'
                elif MOVIE == 'Harry Potter and the Half-Blood Prince':
                    choices = '926'
                elif MOVIE == '300':
                    choices = '927'
                elif MOVIE == 'Match Point':
                    choices = '928'
                elif MOVIE == 'Watchmen':
                    choices = '929'
                elif MOVIE == 'Lord of War':
                    choices = '930'
                elif MOVIE == 'Saw':
                    choices = '931'
                elif MOVIE == 'Synecdoche, New York':
                    choices = '932'
                elif MOVIE == 'Mysterious Skin':
                    choices = '933'
                elif MOVIE == 'Jeux d\'enfants':
                    choices = '934'
                elif MOVIE == 'Un long dimanche de fiançailles':
                    choices = '935'
                elif MOVIE == 'The Station Agent':
                    choices = '936'
                elif MOVIE == '21 Grams':
                    choices = '937'
                elif MOVIE == 'Boksuneun naui geot':
                    choices = '938'
                elif MOVIE == 'Finding Neverland':
                    choices = '939'
                elif MOVIE == '25th Hour':
                    choices = '940'
                elif MOVIE == 'The Butterfly Effect':
                    choices = '941'
                elif MOVIE == '28 Days Later...':
                    choices = '942'
                elif MOVIE == 'Batoru rowaiaru':
                    choices = '943'
                elif MOVIE == 'The Royal Tenenbaums':
                    choices = '944'
                elif MOVIE == 'Y tu mamá también':
                    choices = '945'
                elif MOVIE == 'Harry Potter and the Sorcerer\'s Stone':
                    choices = '946'
                elif MOVIE == 'The Others':
                    choices = '947'
                elif MOVIE == 'Blow':
                    choices = '948'
                elif MOVIE == 'Enemy at the Gates':
                    choices = '949'
                elif MOVIE == 'Minority Report':
                    choices = '950'
                elif MOVIE == 'The Hurricane':
                    choices = '951'
                elif MOVIE == 'American Psycho':
                    choices = '952'
                elif MOVIE == 'Lola rennt':
                    choices = '953'
                elif MOVIE == 'The Thin Red Line':
                    choices = '954'
                elif MOVIE == 'Mulan':
                    choices = '955'
                elif MOVIE == 'Fear and Loathing in Las Vegas':
                    choices = '956'
                elif MOVIE == 'Funny Games':
                    choices = '957'
                elif MOVIE == 'Dark City':
                    choices = '958'
                elif MOVIE == 'Sleepers':
                    choices = '959'
                elif MOVIE == 'Lost Highway':
                    choices = '960'
                elif MOVIE == 'Sense and Sensibility':
                    choices = '961'
                elif MOVIE == 'Die Hard: With a Vengeance':
                    choices = '962'
                elif MOVIE == 'Dead Man':
                    choices = '963'
                elif MOVIE == 'The Bridges of Madison County':
                    choices = '964'
                elif MOVIE == 'Trois couleurs: Blanc':
                    choices = '965'
                elif MOVIE == 'Falling Down':
                    choices = '966'
                elif MOVIE == 'Dazed and Confused':
                    choices = '967'
                elif MOVIE == 'My Cousin Vinny':
                    choices = '968'
                elif MOVIE == 'Omohide poro poro':
                    choices = '969'
                elif MOVIE == 'Delicatessen':
                    choices = '970'
                elif MOVIE == 'Home Alone':
                    choices = '971'
                elif MOVIE == 'The Godfather: Part III':
                    choices = '972'
                elif MOVIE == 'When Harry Met Sally...':
                    choices = '973'
                elif MOVIE == 'The Little Mermaid':
                    choices = '974'
                elif MOVIE == 'The Naked Gun: From the Files of Police Squad!':
                    choices = '975'
                elif MOVIE == 'Planes, Trains & Automobiles':
                    choices = '976'
                elif MOVIE == 'Lethal Weapon':
                    choices = '977'
                elif MOVIE == 'Blood Simple':
                    choices = '978'
                elif MOVIE == 'On Golden Pond':
                    choices = '979'
                elif MOVIE == 'Mad Max 2':
                    choices = '980'
                elif MOVIE == 'The Warriors':
                    choices = '981'
                elif MOVIE == 'The Muppet Movie':
                    choices = '982'
                elif MOVIE == 'Escape from Alcatraz':
                    choices = '983'
                elif MOVIE == 'Watership Down':
                    choices = '984'
                elif MOVIE == 'Midnight Express':
                    choices = '985'
                elif MOVIE == 'Close Encounters of the Third Kind':
                    choices = '986'
                elif MOVIE == 'The Long Goodbye':
                    choices = '987'
                elif MOVIE == 'Giù la testa':
                    choices = '988'
                elif MOVIE == 'Kelly\'s Heroes':
                    choices = '989'
                elif MOVIE == 'The Jungle Book':
                    choices = '990'
                elif MOVIE == 'Blowup':
                    choices = '991'
                elif MOVIE == 'A Hard Day\'s Night':
                    choices = '992'
                elif MOVIE == 'Breakfast at Tiffany\'s':
                    choices = '993'  
                
                GENRE = request.form['genre']
                if GENRE == 'Drama':
                    gen = '0'
                elif GENRE == 'Crime, Drama':
                    gen = '1'
                elif GENRE == 'Action, Crime, Drama':
                    gen = '2'
                elif GENRE == 'Action, Adventure, Drama':
                    gen = '3'
                elif GENRE == 'Biography, Drama, History':
                    gen = '4'
                elif GENRE == 'Action, Adventure, Sci-Fi':
                    gen = '5'
                elif GENRE == 'Drama, Romance':
                    gen = '6'
                elif GENRE == 'Western':
                    gen = '7'
                elif GENRE == 'Action, Sci-Fi':
                    gen = '8'
                elif GENRE == 'Biography, Crime, Drama':
                    gen = '9'
                elif GENRE == 'Action, Adventure, Fantasy':
                    gen = '10'
                elif GENRE == 'Comedy, Drama, Thriller':
                    gen = '11'
                elif GENRE == 'Adventure, Drama, Sci-Fi':
                    gen = '12'
                elif GENRE == 'Animation, Adventure, Family':
                    gen = '13'
                elif GENRE == 'Drama, War':
                    gen = '14'
                elif GENRE == 'Crime, Drama, Fantasy':
                    gen = '15'
                elif GENRE == 'Comedy, Drama, Romance':
                    gen = '16'
                elif GENRE == 'Crime, Drama, Mystery':
                    gen = '17'
                elif GENRE == 'Crime, Drama, Thriller':
                    gen = '18'
                elif GENRE == 'Action, Drama, Mystery':
                    gen = '19'
                elif GENRE == 'Drama, Family, Fantasy':
                    gen = '20'
                elif GENRE == 'Drama, Music':
                    gen = '21'
                elif GENRE == 'Biography, Comedy, Drama':
                    gen = '22'
                elif GENRE == 'Drama, Mystery, Sci-Fi':
                    gen = '23'
                elif GENRE == 'Biography, Drama, Music':
                    gen = '24'
                elif GENRE == 'Crime, Mystery, Thriller':
                    gen = '25'
                elif GENRE == 'Animation, Adventure, Drama':
                    gen = '26'
                elif GENRE == 'Animation, Drama, War':
                    gen = '27'
                elif GENRE == 'Adventure, Comedy, Sci-Fi':
                    gen = '28'
                elif GENRE == 'Horror, Mystery, Thriller':
                    gen = '29'
                elif GENRE == 'Drama, Romance, War':
                    gen = '30'
                elif GENRE == 'Comedy, Drama, Family':
                    gen = '31'
                elif GENRE == 'Animation, Drama, Fantasy':
                    gen = '32'
                elif GENRE == 'Action, Biography, Drama':
                    gen = '33'
                elif GENRE == 'Animation, Action, Adventure':
                    gen = '34'
                elif GENRE == 'Drama, Western':
                    gen = '35'
                elif GENRE == 'Action, Adventure':
                    gen = '36'
                elif GENRE == 'Comedy, Drama':
                    gen = '37'
                elif GENRE == 'Drama, Family':
                    gen = '38'
                elif GENRE == 'Drama, Mystery, Thriller':
                    gen = '39'
                elif GENRE == 'Mystery, Thriller':
                    gen = '40'
                elif GENRE == 'Drama, Horror':
                    gen = '41'
                elif GENRE == 'Drama, Mystery, War':
                    gen = '42'
                elif GENRE == 'Horror, Sci-Fi':
                    gen = '43'
                elif GENRE == 'Drama, Musical':
                    gen = '44'
                elif GENRE == 'Comedy':
                    gen = '45'
                elif GENRE == 'Drama, Film-Noir':
                    gen = '46'
                elif GENRE == 'Comedy, Drama, War':
                    gen = '47'
                elif GENRE == 'Drama, Thriller, War':
                    gen = '48'
                elif GENRE == 'Drama, Fantasy, Horror':
                    gen = '49'
                elif GENRE == 'Crime, Drama, Music':
                    gen = '50'
                elif GENRE == 'Adventure, Drama, War':
                    gen = '51'
                elif GENRE == 'Drama, Romance, Sci-Fi':
                    gen = '52'
                elif GENRE == 'Comedy, Romance':
                    gen = '53'
                elif GENRE == 'Comedy, Crime':
                    gen = '54'
                elif GENRE == 'Drama, Family, Sport':
                    gen = '55'
                elif GENRE == 'Animation, Adventure, Comedy':
                    gen = '56'
                elif GENRE == 'Adventure, Drama, Thriller':
                    gen = '57'
                elif GENRE == 'Comedy, Crime, Drama':
                    gen = '58'
                elif GENRE == 'Crime, Drama, Sci-Fi':
                    gen = '59'
                elif GENRE == 'Adventure, Sci-Fi':
                    gen = '60'
                elif GENRE == 'Adventure, Biography, Drama':
                    gen = '61'
                elif GENRE == 'Adventure, Mystery, Thriller':
                    gen = '62'
                elif GENRE == 'Mystery, Romance, Thriller':
                    gen = '63'
                elif GENRE == 'Comedy, Musical, Romance':
                    gen = '64'
                elif GENRE == 'Crime, Drama, Film-Noir':
                    gen = '65'
                elif GENRE == 'Drama, Mystery':
                    gen = '66'
                elif GENRE == 'Drama, Sci-Fi':
                    gen = '67'
                elif GENRE == 'Action, Drama, War':
                    gen = '68'
                elif GENRE == 'Action, Drama':
                    gen = '69'
                elif GENRE == 'Adventure, Comedy, Drama':
                    gen = '70'
                elif GENRE == 'Biography, Drama, Sport':
                    gen = '71'
                elif GENRE == 'Action, Comedy, Crime':
                    gen = '72'
                elif GENRE == 'Action, Biography, Crime':
                    gen = '73'
                elif GENRE == 'Drama, Mystery, Romance':
                    gen = '74'
                elif GENRE == 'Action, Drama, Sport':
                    gen = '75'
                elif GENRE == 'Drama, Fantasy, War':
                    gen = '76'
                elif GENRE == 'Action, Drama, Sci-Fi':
                    gen = '77'
                elif GENRE == 'Biography, Drama':
                    gen = '78'
                elif GENRE == 'Action, Comedy, Romance':
                    gen = '79'
                elif GENRE == 'Animation, Family, Fantasy':
                    gen = '80'
                elif GENRE == 'Action, Thriller':
                    gen = '81'
                elif GENRE == 'Action, Adventure, Comedy':
                    gen = '82'
                elif GENRE == 'Adventure, Comedy, Fantasy':
                    gen = '83'
                elif GENRE == 'Adventure, Drama, History':
                    gen = '84'
                elif GENRE == 'Action, Drama, Thriller':
                    gen = '85'
                elif GENRE == 'Comedy, Music, Romance':
                    gen = '86'
                elif GENRE == 'Drama, Fantasy, History':
                    gen = '87'
                elif GENRE == 'Crime, Thriller':
                    gen = '88'
                elif GENRE == 'Adventure, Drama, Western':
                    gen = '89'
                elif GENRE == 'Comedy, War':
                    gen = '90'
                elif GENRE == 'Drama, Thriller':
                    gen = '91'
                elif GENRE == 'Animation, Drama, Family':
                    gen = '92'
                elif GENRE == 'Drama, Romance, Thriller':
                    gen = '93'
                elif GENRE == 'Comedy, Drama, Musical':
                    gen = '94'
                elif GENRE == 'Comedy, Drama, Fantasy':
                    gen = '95'
                elif GENRE == 'Adventure, Comedy, Crime':
                    gen = '96'
                elif GENRE == 'Adventure, Drama, Fantasy':
                    gen = '97'
                elif GENRE == 'Biography, Drama, Family':
                    gen = '98'
                elif GENRE == 'Animation, Comedy, Drama':
                    gen = '99'
                elif GENRE == 'Drama, Sport':
                    gen = '100'
                elif GENRE == 'Animation, Action, Drama':
                    gen = '101'
                elif GENRE == 'Adventure, Drama, Musical':
                    gen = '102'
                elif GENRE == 'Drama, Music, Romance':
                    gen = '103'
                elif GENRE == 'Comedy, Crime, Romance':
                    gen = '104'
                elif GENRE == 'Comedy, Crime, Sport':
                    gen = '105'
                elif GENRE == 'Drama, History, Romance':
                    gen = '106'
                elif GENRE == 'Adventure, Drama':
                    gen = '107'
                elif GENRE == 'Animation, Adventure, Fantasy':
                    gen = '108'
                elif GENRE == 'Horror, Mystery, Sci-Fi':
                    gen = '109'
                elif GENRE == 'Drama, Fantasy, Music':
                    gen = '110'
                elif GENRE == 'Action, Sci-Fi, Thriller':
                    gen = '111'
                elif GENRE == 'Drama, Fantasy':
                    gen = '112'
                elif GENRE == 'Drama, Horror, Thriller':
                    gen = '113'
                elif GENRE == 'Drama, History':
                    gen = '114'
                elif GENRE == 'Film-Noir, Mystery, Thriller':
                    gen = '115'
                elif GENRE == 'Fantasy, Horror, Mystery':
                    gen = '116'
                elif GENRE == 'Action, Crime, Thriller':
                    gen = '117'
                elif GENRE == 'Comedy, Drama, Music':
                    gen = '118'
                elif GENRE == 'Biography, Drama, Thriller':
                    gen = '119'
                elif GENRE == 'Animation, Biography, Drama':
                    gen = '120'
                elif GENRE == 'Action, Mystery, Thriller':
                    gen = '121'
                elif GENRE == 'Crime, Drama, Romance':
                    gen = '122'
                elif GENRE == 'Action, Adventure, Thriller':
                    gen = '123'
                elif GENRE == 'Crime, Drama, Musical':
                    gen = '124'
                elif GENRE == 'Animation, Crime, Mystery':
                    gen = '125'
                elif GENRE == 'Action, Crime, Comedy':
                    gen = '126'
                elif GENRE == 'Mystery, Sci-Fi, Thriller':
                    gen = '127'
                elif GENRE == 'Animation, Action, Crime':
                    gen = '128'
                elif GENRE == 'Comedy, Fantasy, Romance':
                    gen = '129'
                elif GENRE == 'Drama, History, Thriller':
                    gen = '130'
                elif GENRE == 'Animation, Action, Sci-Fi':
                    gen = '131'
                elif GENRE == 'Adventure, Family, Fantasy':
                    gen = '132'
                elif GENRE == 'Drama, Fantasy, Romance':
                    gen = '133'
                elif GENRE == 'Drama, History, War':
                    gen = '134'
                elif GENRE == 'Adventure, Thriller':
                    gen = '135'
                elif GENRE == 'Horror':
                    gen = '136'
                elif GENRE == 'Drama, Family, Musical':
                    gen = '137'
                elif GENRE == 'Action, Drama, Western':
                    gen = '138'
                elif GENRE == 'Crime, Drama, Horror':
                    gen = '139'
                elif GENRE == 'Drama, Film-Noir, Mystery':
                    gen = '140'
                elif GENRE == 'Comedy, Crime, Thriller':
                    gen = '141'
                elif GENRE == 'Film-Noir, Mystery':
                    gen = '142'
                elif GENRE == 'Comedy, Crime, Mystery':
                    gen = '143'
                elif GENRE == 'Drama, Fantasy, Mystery':
                    gen = '144'
                elif GENRE == 'Comedy, Horror':
                    gen = '145'
                elif GENRE == 'Action, Adventure, History':
                    gen = '146'
                elif GENRE == 'Drama, Music, Mystery':
                    gen = '147'
                elif GENRE == 'Comedy, Music':
                    gen = '148'
                elif GENRE == 'Comedy, Family':
                    gen = '149'
                elif GENRE == 'Drama, Music, Musical':
                    gen = '150'
                elif GENRE == 'Action, Adventure, Horror':
                    gen = '151'
                elif GENRE == 'Action, Adventure, Biography':
                    gen = '152'
                elif GENRE == 'Biography, Drama, War':
                    gen = '153'
                elif GENRE == 'Action, Adventure, Western':
                    gen = '154'
                elif GENRE == 'Horror, Thriller':
                    gen = '155'
                elif GENRE == 'Comedy, Mystery, Romance':
                    gen = '156'
                elif GENRE == 'Drama, Thriller, Western':
                    gen = '157'
                elif GENRE == 'Crime, Film-Noir, Thriller':
                    gen = '158'
                elif GENRE == 'Drama, Film-Noir, Romance':
                    gen = '159'
                elif GENRE == 'Crime, Film-Noir, Mystery':
                    gen = '160'
                elif GENRE == 'Action, Adventure, Romance':
                    gen = '161'
                elif GENRE == 'Comedy, Music, Musical':
                    gen = '162'
                elif GENRE == 'Adventure, Horror, Sci-Fi':
                    gen = '163'
                elif GENRE == 'Fantasy, Horror':
                    gen = '164'
                elif GENRE == 'Action, Drama, History':
                    gen = '165'
                elif GENRE == 'Adventure, Comedy, Family':
                    gen = '166'
                elif GENRE == 'Animation, Biography, Crime':
                    gen = '167'
                elif GENRE == 'Adventure, Biography, Crime':
                    gen = '168'
                elif GENRE == 'Adventure, Fantasy':
                    gen = '169'
                elif GENRE == 'Drama, History, Mystery':
                    gen = '170'
                elif GENRE == 'Action, Comedy, Mystery':
                    gen = '171'
                elif GENRE == 'Adventure, Drama, Romance':
                    gen = '172'
                elif GENRE == 'Drama, Sci-Fi, Thriller':
                    gen = '173'
                elif GENRE == 'Crime, Drama, History':
                    gen = '174'
                elif GENRE == 'Action, Comedy, Fantasy':
                    gen = '175'
                elif GENRE == 'Family, Sci-Fi':
                    gen = '176'
                elif GENRE == 'Adventure, History, War':
                    gen = '177'
                elif GENRE == 'Animation, Sci-Fi':
                    gen = '178'
                elif GENRE == 'Family, Fantasy, Musical':
                    gen = '179'
                elif GENRE == 'Thriller':
                    gen = '180'
                elif GENRE == 'Comedy, Family, Fantasy':
                    gen = '181'
                elif GENRE == 'Adventure, Comedy, Film-Noir':
                    gen = '182'
                elif GENRE == 'Film-Noir, Thriller':
                    gen = '183'
                elif GENRE == 'Comedy, Family, Romance':
                    gen = '184'
                elif GENRE == 'Drama, Horror, Sci-Fi':
                    gen = '185'
                elif GENRE == 'Comedy, Musical, War':
                    gen = '186'
                elif GENRE == 'Biography, Drama, Romance':
                    gen = '187'
                elif GENRE == 'Drama, History, Music':
                    gen = '188'
                elif GENRE == 'Animation, Action, Fantasy':
                    gen = '189'
                elif GENRE == 'Animation, Comedy, Fantasy':
                    gen = '190'
                elif GENRE == 'Comedy, Western':
                    gen = '191'
                elif GENRE == 'Action, Adventure, War':
                    gen = '192'
                elif GENRE == 'Drama, Horror, Mystery':
                    gen = '193'
                elif GENRE == 'Animation, Comedy, Crime':
                    gen = '194'
                elif GENRE == 'Action, Adventure, Crime':
                    gen = '195'
                elif GENRE == 'Action, Adventure, Mystery':
                    gen = '196'
                elif GENRE == 'Action, Adventure, Family':
                    gen = '197'
                elif GENRE == 'Action, Crime, Mystery':
                    gen = '198'
                elif GENRE == 'Animation, Drama, Romance':
                    gen = '199'
                elif GENRE == 'Drama, War, Western':
                    gen = '200'
                elif GENRE == 'Adventure, Comedy, War':
                    gen = '201'

                STAR1 = request.form['star1']
                if STAR1 == 'Tim Robbins':
                    sta1 = '0'
                elif STAR1 == 'Marlon Brando':
                    sta1 = '1'
                elif STAR1 == 'Christian Bale':
                    sta1 = '2'
                elif STAR1 == 'Al Pacino':
                    sta1 = '3'
                elif STAR1 == 'Henry Fonda':
                    sta1 = '4'
                elif STAR1 == 'Elijah Wood':
                    sta1 = '5'
                elif STAR1 == 'John Travolta':
                    sta1 = '6'
                elif STAR1 == 'Liam Neeson':
                    sta1 = '7'
                elif STAR1 == 'Leonardo DiCaprio':
                    sta1 = '8'
                elif STAR1 == 'Brad Pitt':
                    sta1 = '9'
                elif STAR1 == 'Tom Hanks':
                    sta1 = '10'
                elif STAR1 == 'Clint Eastwood':
                    sta1 = '11'
                elif STAR1 == 'Lilly Wachowski':
                    sta1 = '12'
                elif STAR1 == 'Robert De Niro':
                    sta1 = '13'
                elif STAR1 == 'Mark Hamill':
                    sta1 = '14'
                elif STAR1 == 'Jack Nicholson':
                    sta1 = '15'
                elif STAR1 == 'Lin-Manuel Miranda':
                    sta1 = '16'
                elif STAR1 == 'Kang-ho Song':
                    sta1 = '17'
                elif STAR1 == 'Suriya':
                    sta1 = '18'
                elif STAR1 == 'Matthew McConaughey':
                    sta1 = '19'
                elif STAR1 == 'Kátia Lund':
                    sta1 = '20'
                elif STAR1 == 'Daveigh Chase':
                    sta1 = '21'
                elif STAR1 == 'Roberto Benigni':
                    sta1 = '22'
                elif STAR1 == 'Morgan Freeman':
                    sta1 = '23'
                elif STAR1 == 'Jodie Foster':
                    sta1 = '24'
                elif STAR1 == 'Tatsuya Nakadai':
                    sta1 = '25'
                elif STAR1 == 'Toshirô Mifune':
                    sta1 = '26'
                elif STAR1 == 'James Stewart':
                    sta1 = '27'
                elif STAR1 == 'Joaquin Phoenix':
                    sta1 = '28'
                elif STAR1 == 'Miles Teller':
                    sta1 = '29'
                elif STAR1 == 'Éric Toledano':
                    sta1 = '30'
                elif STAR1 == 'Adrien Brody':
                    sta1 = '31'
                elif STAR1 == 'Russell Crowe':
                    sta1 = '32'
                elif STAR1 == 'Edward Norton':
                    sta1 = '33'
                elif STAR1 == 'Kevin Spacey':
                    sta1 = '34'
                elif STAR1 == 'Jean Reno':
                    sta1 = '35'
                elif STAR1 == 'Rob Minkoff':
                    sta1 = '36'
                elif STAR1 == 'Arnold Schwarzenegger':
                    sta1 = '37'
                elif STAR1 == 'Philippe Noiret':
                    sta1 = '38'
                elif STAR1 == 'Tsutomu Tatsumi':
                    sta1 = '39'
                elif STAR1 == 'Michael J. Fox':
                    sta1 = '40'
                elif STAR1 == 'Anthony Perkins':
                    sta1 = '41'
                elif STAR1 == 'Humphrey Bogart':
                    sta1 = '42'
                elif STAR1 == 'Charles Chaplin':
                    sta1 = '43'
                elif STAR1 == 'Zain Al Rafeea':
                    sta1 = '44'
                elif STAR1 == 'Erdem Can':
                    sta1 = '45'
                elif STAR1 == 'Pushkar':
                    sta1 = '46'
                elif STAR1 == 'Ryûnosuke Kamiki':
                    sta1 = '47'
                elif STAR1 == 'Aamir Khan':
                    sta1 = '48'
                elif STAR1 == 'Peter Ramsey':
                    sta1 = '49'
                elif STAR1 == 'Joe Russo':
                    sta1 = '50'
                elif STAR1 == 'Adrian Molina':
                    sta1 = '51'
                elif STAR1 == 'Jamie Foxx':
                    sta1 = '52'
                elif STAR1 == 'Amole Gupte':
                    sta1 = '53'
                elif STAR1 == 'Ben Burtt':
                    sta1 = '54'
                elif STAR1 == 'Ulrich Mühe':
                    sta1 = '55'
                elif STAR1 == 'Choi Min-sik':
                    sta1 = '56'
                elif STAR1 == 'Guy Pearce':
                    sta1 = '57'
                elif STAR1 == 'Yôji Matsuda':
                    sta1 = '58'
                elif STAR1 == 'Harrison Ford':
                    sta1 = '59'
                elif STAR1 == 'Martin Sheen':
                    sta1 = '60'
                elif STAR1 == 'Sigourney Weaver':
                    sta1 = '61'
                elif STAR1 == 'Rajesh Khanna':
                    sta1 = '62'
                elif STAR1 == 'Peter Sellers':
                    sta1 = '63'
                elif STAR1 == 'Tyrone Power':
                    sta1 = '64'
                elif STAR1 == 'Kirk Douglas':
                    sta1 = '65'
                elif STAR1 == 'William Holden':
                    sta1 = '66'
                elif STAR1 == 'Dean-Charles Chapman':
                    sta1 = '67'
                elif STAR1 == 'Anand Gandhi':
                    sta1 = '68'
                elif STAR1 == 'Ayushmann Khurrana':
                    sta1 = '69'
                elif STAR1 == 'Mohanlal':
                    sta1 = '70'
                elif STAR1 == 'Mads Mikkelsen':
                    sta1 = '71'
                elif STAR1 == 'Payman Maadi':
                    sta1 = '72'
                elif STAR1 == 'Lubna Azabal':
                    sta1 = '73'
                elif STAR1 == 'Aras Bulut Iynemli':
                    sta1 = '74'
                elif STAR1 == 'Çetin Tekindor':
                    sta1 = '75'
                elif STAR1 == 'Jim Carrey':
                    sta1 = '76'
                elif STAR1 == 'Audrey Tautou':
                    sta1 = '77'
                elif STAR1 == 'Jason Statham':
                    sta1 = '78'
                elif STAR1 == 'Ellen Burstyn':
                    sta1 = '79'
                elif STAR1 == 'Robin Williams':
                    sta1 = '80'
                elif STAR1 == 'Mohammad Amir Naji':
                    sta1 = '81'
                elif STAR1 == 'Mel Gibson':
                    sta1 = '82'
                elif STAR1 == 'Harvey Keitel':
                    sta1 = '83'
                elif STAR1 == 'Matthew Modine':
                    sta1 = '84'
                elif STAR1 == 'Aleksey Kravchenko':
                    sta1 = '85'
                elif STAR1 == 'F. Murray Abraham':
                    sta1 = '86'
                elif STAR1 == 'Jürgen Prochnow':
                    sta1 = '87'
                elif STAR1 == 'Paul Newman':
                    sta1 = '88'
                elif STAR1 == 'Malcolm McDowell':
                    sta1 = '89'
                elif STAR1 == 'Keir Dullea':
                    sta1 = '90'
                elif STAR1 == 'Peter O\'Toole':
                    sta1 = '91'
                elif STAR1 == 'Jack Lemmon':
                    sta1 = '92'
                elif STAR1 == 'Cary Grant':
                    sta1 = '93'
                elif STAR1 == 'Gene Kelly':
                    sta1 = '94'
                elif STAR1 == 'Takashi Shimura':
                    sta1 = '95'
                elif STAR1 == 'Lamberto Maggiorani':
                    sta1 = '96'
                elif STAR1 == 'Fred MacMurray':
                    sta1 = '97'
                elif STAR1 == 'Orson Welles':
                    sta1 = '98'
                elif STAR1 == 'Peter Lorre':
                    sta1 = '99'
                elif STAR1 == 'Brigitte Helm':
                    sta1 = '100'
                elif STAR1 == 'Sushant Singh Rajput':
                    sta1 = '101'
                elif STAR1 == 'Vicky Kaushal':
                    sta1 = '102'
                elif STAR1 == 'Yash':
                    sta1 = '103'
                elif STAR1 == 'Viggo Mortensen':
                    sta1 = '104'
                elif STAR1 == 'Frances McDormand':
                    sta1 = '105'
                elif STAR1 == 'Irrfan Khan':
                    sta1 = '106'
                elif STAR1 == 'Prabhas':
                    sta1 = '107'
                elif STAR1 == 'Carlos Martínez López':
                    sta1 = '108'
                elif STAR1 == 'Ajay Devgn':
                    sta1 = '109'
                elif STAR1 == 'Kangana Ranaut':
                    sta1 = '110'
                elif STAR1 == 'Lembit Ulfsak':
                    sta1 = '111'
                elif STAR1 == 'Farhan Akhtar':
                    sta1 = '112'
                elif STAR1 == 'Manoj Bajpayee':
                    sta1 = '113'
                elif STAR1 == 'Rajat Barmecha':
                    sta1 = '114'
                elif STAR1 == 'Ricardo Darín':
                    sta1 = '115'
                elif STAR1 == 'Tom Hardy':
                    sta1 = '116'
                elif STAR1 == 'Bob Peterson':
                    sta1 = '117'
                elif STAR1 == 'Shah Rukh Khan':
                    sta1 = '118'
                elif STAR1 == 'Daniel Day-Lewis':
                    sta1 = '119'
                elif STAR1 == 'Ivana Baquero':
                    sta1 = '120'
                elif STAR1 == 'Hugo Weaving':
                    sta1 = '121'
                elif STAR1 == 'Amitabh Bachchan':
                    sta1 = '122'
                elif STAR1 == 'Bruno Ganz':
                    sta1 = '123'
                elif STAR1 == 'Chieko Baishô':
                    sta1 = '124'
                elif STAR1 == 'Akshay Kumar':
                    sta1 = '125'
                elif STAR1 == 'Jason Flemyng':
                    sta1 = '126'
                elif STAR1 == 'Sener Sen':
                    sta1 = '127'
                elif STAR1 == 'Davor Dujmovic':
                    sta1 = '128'
                elif STAR1 == 'Hitoshi Takagi':
                    sta1 = '129'
                elif STAR1 == 'Bruce Willis':
                    sta1 = '130'
                elif STAR1 == 'Alisa Freyndlikh':
                    sta1 = '131'
                elif STAR1 == 'Ingrid Bergman':
                    sta1 = '132'
                elif STAR1 == 'Anthony Quinn':
                    sta1 = '133'
                elif STAR1 == 'Sanjeev Kumar':
                    sta1 = '134'
                elif STAR1 == 'Terry Jones':
                    sta1 = '135'
                elif STAR1 == 'Steve McQueen':
                    sta1 = '136'
                elif STAR1 == 'Gregory Peck':
                    sta1 = '137'
                elif STAR1 == 'Spencer Tracy':
                    sta1 = '138'
                elif STAR1 == 'Marilyn Monroe':
                    sta1 = '139'
                elif STAR1 == 'Victor Sjöström':
                    sta1 = '140'
                elif STAR1 == 'Max von Sydow':
                    sta1 = '141'
                elif STAR1 == 'Jean Servais':
                    sta1 = '142'
                elif STAR1 == 'Ray Milland':
                    sta1 = '143'
                elif STAR1 == 'Chishû Ryû':
                    sta1 = '144'
                elif STAR1 == 'Bette Davis':
                    sta1 = '145'
                elif STAR1 == 'Carole Lombard':
                    sta1 = '146'
                elif STAR1 == 'Buster Keaton':
                    sta1 = '147'
                elif STAR1 == 'Noémie Merlant':
                    sta1 = '148'
                elif STAR1 == 'Taapsee Pannu':
                    sta1 = '149'
                elif STAR1 == 'Miyu Irino':
                    sta1 = '150'
                elif STAR1 == 'Mario Casas':
                    sta1 = '151'
                elif STAR1 == 'Kim Min-hee':
                    sta1 = '152'
                elif STAR1 == 'Anne Dorval':
                    sta1 = '153'
                elif STAR1 == 'Shahid Kapoor':
                    sta1 = '154'
                elif STAR1 == 'Hugh Jackman':
                    sta1 = '155'
                elif STAR1 == 'Brie Larson':
                    sta1 = '156'
                elif STAR1 == 'Darío Grandinetti':
                    sta1 = '157'
                elif STAR1 == 'Kemp Powers':
                    sta1 = '158'
                elif STAR1 == 'Haluk Bilginer':
                    sta1 = '159'
                elif STAR1 == 'Paresh Rawal':
                    sta1 = '160'
                elif STAR1 == 'Ralph Fiennes':
                    sta1 = '161'
                elif STAR1 == 'Ben Affleck':
                    sta1 = '162'
                elif STAR1 == 'Aoi Miyazaki':
                    sta1 = '163'
                elif STAR1 == 'Andrew Garfield':
                    sta1 = '164'
                elif STAR1 == 'Ronnie Del Carmen':
                    sta1 = '165'
                elif STAR1 == 'Ranbir Kapoor':
                    sta1 = '166'
                elif STAR1 == 'Chiwetel Ejiofor':
                    sta1 = '167'
                elif STAR1 == 'Daniel Brühl':
                    sta1 = '168'
                elif STAR1 == 'Matt Damon':
                    sta1 = '169'
                elif STAR1 == 'Mark Ruffalo':
                    sta1 = '170'
                elif STAR1 == 'David Rawle':
                    sta1 = '171'
                elif STAR1 == 'Vidya Balan':
                    sta1 = '172'
                elif STAR1 == 'Hrithik Roshan':
                    sta1 = '173'
                elif STAR1 == 'Anupam Kher':
                    sta1 = '174'
                elif STAR1 == 'Daniel Radcliffe':
                    sta1 = '175'
                elif STAR1 == 'Masahiro Motoki':
                    sta1 = '176'
                elif STAR1 == 'Richard Gere':
                    sta1 = '177'
                elif STAR1 == 'Toni Collette':
                    sta1 = '178'
                elif STAR1 == 'Chris Sanders':
                    sta1 = '179'
                elif STAR1 == 'Emile Hirsch':
                    sta1 = '180'
                elif STAR1 == 'Joel Coen':
                    sta1 = '181'
                elif STAR1 == 'Sanjay Dutt':
                    sta1 = '182'
                elif STAR1 == 'Hilary Swank':
                    sta1 = '183'
                elif STAR1 == 'Don Cheadle':
                    sta1 = '184'
                elif STAR1 == 'Jang Dong-Gun':
                    sta1 = '185'
                elif STAR1 == 'Ethan Hawke':
                    sta1 = '186'
                elif STAR1 == 'Uma Thurman':
                    sta1 = '187'
                elif STAR1 == 'Lee Unkrich':
                    sta1 = '188'
                elif STAR1 == 'Emilio Echevarría':
                    sta1 = '189'
                elif STAR1 == 'David Silverman':
                    sta1 = '190'
                elif STAR1 == 'Kazuya Tsurumaki':
                    sta1 = '191'
                elif STAR1 == 'Tim Roth':
                    sta1 = '192'
                elif STAR1 == 'Bajram Severdzan':
                    sta1 = '193'
                elif STAR1 == 'Ethan Coen':
                    sta1 = '194'
                elif STAR1 == 'Tony Chiu-Wai Leung':
                    sta1 = '195'
                elif STAR1 == 'Ewan McGregor':
                    sta1 = '196'
                elif STAR1 == 'Predrag \'Miki\' Manojlovic':
                    sta1 = '197'
                elif STAR1 == 'Vincent Cassel':
                    sta1 = '198'
                elif STAR1 == 'Irène Jacob':
                    sta1 = '199'
                elif STAR1 == 'Brigitte Lin':
                    sta1 = '200'
                elif STAR1 == 'Sam Neill':
                    sta1 = '201'
                elif STAR1 == 'Leslie Cheung':
                    sta1 = '202'
                elif STAR1 == 'Gong Li':
                    sta1 = '203'
                elif STAR1 == 'Wil Wheaton':
                    sta1 = '204'
                elif STAR1 == 'Charlie Sheen':
                    sta1 = '205'
                elif STAR1 == 'Harry Dean Stanton':
                    sta1 = '206'
                elif STAR1 == 'Sumi Shimamoto':
                    sta1 = '207'
                elif STAR1 == 'Kurt Russell':
                    sta1 = '208'
                elif STAR1 == 'Bob Geldof':
                    sta1 = '209'
                elif STAR1 == 'Klaus Kinski':
                    sta1 = '210'
                elif STAR1 == 'Bertil Guve':
                    sta1 = '211'
                elif STAR1 == 'Anthony Hopkins':
                    sta1 = '212'
                elif STAR1 == 'Graham Chapman':
                    sta1 = '213'
                elif STAR1 == 'Sylvester Stallone':
                    sta1 = '214'
                elif STAR1 == 'Faye Dunaway':
                    sta1 = '215'
                elif STAR1 == 'Ryan O\'Neal':
                    sta1 = '216'
                elif STAR1 == 'Margarita Terekhova':
                    sta1 = '217'
                elif STAR1 == 'Harriet Andersson':
                    sta1 = '218'
                elif STAR1 == 'Natalya Bondarchuk':
                    sta1 = '219'
                elif STAR1 == 'Alain Delon':
                    sta1 = '220'
                elif STAR1 == 'Bibi Andersson':
                    sta1 = '221'
                elif STAR1 == 'Anatoliy Solonitsyn':
                    sta1 = '222'
                elif STAR1 == 'Brahim Hadjadj':
                    sta1 = '223'
                elif STAR1 == 'Silvia Pinal':
                    sta1 = '224'
                elif STAR1 == 'Eduard Abalov':
                    sta1 = '225'
                elif STAR1 == 'Jean-Pierre Léaud':
                    sta1 = '226'
                elif STAR1 == 'Charlton Heston':
                    sta1 = '227'
                elif STAR1 == 'Giulietta Masina':
                    sta1 = '228'
                elif STAR1 == 'Yves Montand':
                    sta1 = '229'
                elif STAR1 == 'James Cagney':
                    sta1 = '230'
                elif STAR1 == 'Emeric Pressburger':
                    sta1 = '231'
                elif STAR1 == 'Margaret Sullavan':
                    sta1 = '232'
                elif STAR1 == 'Laurence Olivier':
                    sta1 = '233'
                elif STAR1 == 'George Cukor':
                    sta1 = '234'
                elif STAR1 == 'Jean Gabin':
                    sta1 = '235'
                elif STAR1 == 'Clark Gable':
                    sta1 = '236'
                elif STAR1 == 'Maria Falconetti':
                    sta1 = '237'
                elif STAR1 == 'George O\'Brien':
                    sta1 = '238'
                elif STAR1 == 'Werner Krauss':
                    sta1 = '239'
                elif STAR1 == 'Willem Dafoe':
                    sta1 = '240'
                elif STAR1 == 'Salman Khan':
                    sta1 = '241'
                elif STAR1 == 'Ryan Gosling':
                    sta1 = '242'
                elif STAR1 == 'Dev Patel':
                    sta1 = '243'
                elif STAR1 == 'Rich Moore':
                    sta1 = '244'
                elif STAR1 == 'Chloë Grace Moretz':
                    sta1 = '245'
                elif STAR1 == 'Jacob Tremblay':
                    sta1 = '246'
                elif STAR1 == 'Vijay Varma':
                    sta1 = '247'
                elif STAR1 == 'Iko Uwais':
                    sta1 = '248'
                elif STAR1 == 'Benedict Cumberbatch':
                    sta1 = '249'
                elif STAR1 == 'Chris Pratt':
                    sta1 = '250'
                elif STAR1 == 'Rami Malek':
                    sta1 = '251'
                elif STAR1 == 'Logan Lerman':
                    sta1 = '252'
                elif STAR1 == 'Wagner Moura':
                    sta1 = '253'
                elif STAR1 == 'Colin Firth':
                    sta1 = '254'
                elif STAR1 == 'Emma Stone':
                    sta1 = '255'
                elif STAR1 == 'Ryan Reynolds':
                    sta1 = '256'
                elif STAR1 == 'Golshifteh Farahani':
                    sta1 = '257'
                elif STAR1 == 'Abhay Deol':
                    sta1 = '258'
                elif STAR1 == 'Donnie Yen':
                    sta1 = '259'
                elif STAR1 == 'Loveleen Tandan':
                    sta1 = '260'
                elif STAR1 == 'Natalie Portman':
                    sta1 = '261'
                elif STAR1 == 'Robert Downey Jr.':
                    sta1 = '262'
                elif STAR1 == 'Marjane Satrapi':
                    sta1 = '263'
                elif STAR1 == 'Will Smith':
                    sta1 = '264'
                elif STAR1 == 'Seung-Yun Lee':
                    sta1 = '265'
                elif STAR1 == 'Quentin Tarantino':
                    sta1 = '266'
                elif STAR1 == 'Laura Obiols':
                    sta1 = '267'
                elif STAR1 == 'Cem Yilmaz':
                    sta1 = '268'
                elif STAR1 == 'Jan Pinkava':
                    sta1 = '269'
                elif STAR1 == 'Daniel Craig':
                    sta1 = '270'
                elif STAR1 == 'Vladimir Garin':
                    sta1 = '271'
                elif STAR1 == 'Ki-duk Kim':
                    sta1 = '272'
                elif STAR1 == 'Javier Bardem':
                    sta1 = '273'
                elif STAR1 == 'Preity Zinta':
                    sta1 = '274'
                elif STAR1 == 'Alan Mak':
                    sta1 = '275'
                elif STAR1 == 'Johnny Depp':
                    sta1 = '276'
                elif STAR1 == 'Craig T. Nelson':
                    sta1 = '277'
                elif STAR1 == 'Tae-Hyun Cha':
                    sta1 = '278'
                elif STAR1 == 'Nicole Kidman':
                    sta1 = '279'
                elif STAR1 == 'Ömer Faruk Sorak':
                    sta1 = '280'
                elif STAR1 == 'Jake Gyllenhaal':
                    sta1 = '281'
                elif STAR1 == 'Tom Cruise':
                    sta1 = '282'
                elif STAR1 == 'Björk':
                    sta1 = '283'
                elif STAR1 == 'Richard Farnsworth':
                    sta1 = '284'
                elif STAR1 == 'Junko Iwao':
                    sta1 = '285'
                elif STAR1 == 'Ulrich Thomsen':
                    sta1 = '286'
                elif STAR1 == 'Fernanda Montenegro':
                    sta1 = '287'
                elif STAR1 == 'Eli Marienthal':
                    sta1 = '288'
                elif STAR1 == 'Til Schweiger':
                    sta1 = '289'
                elif STAR1 == 'Billy Bob Thornton':
                    sta1 = '290'
                elif STAR1 == 'Timothy Spall':
                    sta1 = '291'
                elif STAR1 == 'Atsuko Tanaka':
                    sta1 = '292'
                elif STAR1 == 'Danny Elfman':
                    sta1 = '293'
                elif STAR1 == 'Bill Murray':
                    sta1 = '294'
                elif STAR1 == 'Damian Chapa':
                    sta1 = '295'
                elif STAR1 == 'John Musker':
                    sta1 = '296'
                elif STAR1 == 'Kevin Costner':
                    sta1 = '297'
                elif STAR1 == 'Kirk Wise':
                    sta1 = '298'
                elif STAR1 == 'Danny Aiello':
                    sta1 = '299'
                elif STAR1 == 'Dustin Hoffman':
                    sta1 = '300'
                elif STAR1 == 'Mitsuo Iwata':
                    sta1 = '301'
                elif STAR1 == 'Cary Elwes':
                    sta1 = '302'
                elif STAR1 == 'Gaspard Manesse':
                    sta1 = '303'
                elif STAR1 == 'Mayumi Tanaka':
                    sta1 = '304'
                elif STAR1 == 'Ben Kingsley':
                    sta1 = '305'
                elif STAR1 == 'Woody Allen':
                    sta1 = '306'
                elif STAR1 == 'Roy Scheider':
                    sta1 = '307'
                elif STAR1 == 'Gene Wilder':
                    sta1 = '308'
                elif STAR1 == 'Timothy Bottoms':
                    sta1 = '309'
                elif STAR1 == 'Topol':
                    sta1 = '310'
                elif STAR1 == 'Jean-Louis Trintignant':
                    sta1 = '311'
                elif STAR1 == 'Mia Farrow':
                    sta1 = '312'
                elif STAR1 == 'Elizabeth Taylor':
                    sta1 = '313'
                elif STAR1 == 'Julie Andrews':
                    sta1 = '314'
                elif STAR1 == 'Omar Sharif':
                    sta1 = '315'
                elif STAR1 == 'Marcello Mastroianni':
                    sta1 = '316'
                elif STAR1 == 'Anna Karina':
                    sta1 = '317'
                elif STAR1 == 'John Wayne':
                    sta1 = '318'
                elif STAR1 == 'Burt Lancaster':
                    sta1 = '319'
                elif STAR1 == 'Sterling Hayden':
                    sta1 = '320'
                elif STAR1 == 'Robert Mitchum':
                    sta1 = '321'
                elif STAR1 == 'Simone Signoret':
                    sta1 = '322'
                elif STAR1 == 'Vivien Leigh':
                    sta1 = '323'
                elif STAR1 == 'Dennis Price':
                    sta1 = '324'
                elif STAR1 == 'Celia Johnson':
                    sta1 = '325'
                elif STAR1 == 'Gene Tierney':
                    sta1 = '326'
                elif STAR1 == 'Myrna Loy':
                    sta1 = '327'
                elif STAR1 == 'Marcel Dalio':
                    sta1 = '328'
                elif STAR1 == 'William Powell':
                    sta1 = '329'
                elif STAR1 == 'Lew Ayres':
                    sta1 = '330'
                elif STAR1 == 'Aleksandr Antonov':
                    sta1 = '331'
                elif STAR1 == 'Lily Franky':
                    sta1 = '332'
                elif STAR1 == 'Adam Driver':
                    sta1 = '333'
                elif STAR1 == 'Armie Hammer':
                    sta1 = '334'
                elif STAR1 == 'Bryan Cranston':
                    sta1 = '335'
                elif STAR1 == 'Ferdia Walsh-Peelo':
                    sta1 = '336'
                elif STAR1 == 'Chris Hemsworth':
                    sta1 = '337'
                elif STAR1 == 'Roman Griffin Davis':
                    sta1 = '338'
                elif STAR1 == 'Amy Adams':
                    sta1 = '339'
                elif STAR1 == 'Daisy Ridley':
                    sta1 = '340'
                elif STAR1 == 'Patrick Stewart':
                    sta1 = '341'
                elif STAR1 == 'Muhammet Uzuner':
                    sta1 = '342'
                elif STAR1 == 'Jean Dujardin':
                    sta1 = '343'
                elif STAR1 == 'Tahar Rahim':
                    sta1 = '344'
                elif STAR1 == 'Sam Rockwell':
                    sta1 = '345'
                elif STAR1 == 'Kåre Hedebrant':
                    sta1 = '346'
                elif STAR1 == 'Sharlto Copley':
                    sta1 = '347'
                elif STAR1 == 'Mickey Rourke':
                    sta1 = '348'
                elif STAR1 == 'Ellar Coltrane':
                    sta1 = '349'
                elif STAR1 == 'Anamaria Marinca':
                    sta1 = '350'
                elif STAR1 == 'Chris Pine':
                    sta1 = '351'
                elif STAR1 == 'Colin Farrell':
                    sta1 = '352'
                elif STAR1 == 'David Lee Smith':
                    sta1 = '353'
                elif STAR1 == 'Ken Watanabe':
                    sta1 = '354'
                elif STAR1 == 'Lee Pace':
                    sta1 = '355'
                elif STAR1 == 'Suraj Sharma':
                    sta1 = '356'
                elif STAR1 == 'George Clooney':
                    sta1 = '357'
                elif STAR1 == 'Michel Côté':
                    sta1 = '358'
                elif STAR1 == 'Gérard Jugnot':
                    sta1 = '359'
                elif STAR1 == 'Simon Pegg':
                    sta1 = '360'
                elif STAR1 == 'Birol Ünel':
                    sta1 = '361'
                elif STAR1 == 'Sean Penn':
                    sta1 = '362'
                elif STAR1 == 'Jet Li':
                    sta1 = '363'
                elif STAR1 == 'Rosario Flores':
                    sta1 = '364'
                elif STAR1 == 'Branko Djuric':
                    sta1 = '365'
                elif STAR1 == 'Tensai Okamura':
                    sta1 = '366'
                elif STAR1 == 'Franka Potente':
                    sta1 = '367'
                elif STAR1 == 'Julianne Moore':
                    sta1 = '368'
                elif STAR1 == 'Billy Crudup':
                    sta1 = '369'
                elif STAR1 == 'Naomi Watts':
                    sta1 = '370'
                elif STAR1 == 'Ash Brannon':
                    sta1 = '371'
                elif STAR1 == 'Mark Wahlberg':
                    sta1 = '372'
                elif STAR1 == 'Yoko Honna':
                    sta1 = '373'
                elif STAR1 == 'Rena Owen':
                    sta1 = '374'
                elif STAR1 == 'Christian Slater':
                    sta1 = '375'
                elif STAR1 == 'Juliette Binoche':
                    sta1 = '376'
                elif STAR1 == 'Kôichi Yamadera':
                    sta1 = '377'
                elif STAR1 == 'Martin Landau':
                    sta1 = '378'
                elif STAR1 == 'Jonathan Pryce':
                    sta1 = '379'
                elif STAR1 == 'Rob Reiner':
                    sta1 = '380'
                elif STAR1 == 'Peter Billingsley':
                    sta1 = '381'
                elif STAR1 == 'John Belushi':
                    sta1 = '382'
                elif STAR1 == 'David Emge':
                    sta1 = '383'
                elif STAR1 == 'Alejandro Jodorowsky':
                    sta1 = '384'
                elif STAR1 == 'Magali Noël':
                    sta1 = '385'
                elif STAR1 == 'Fernando Rey':
                    sta1 = '386'
                elif STAR1 == 'Ruth Gordon':
                    sta1 = '387'
                elif STAR1 == 'George C. Scott':
                    sta1 = '388'
                elif STAR1 == 'Duane Jones':
                    sta1 = '389'
                elif STAR1 == 'Sidney Poitier':
                    sta1 = '390'
                elif STAR1 == 'Frank Sinatra':
                    sta1 = '391'
                elif STAR1 == 'Gabriele Ferzetti':
                    sta1 = '392'
                elif STAR1 == 'Emmanuelle Riva':
                    sta1 = '393'
                elif STAR1 == 'James Dean':
                    sta1 = '394'
                elif STAR1 == 'Gary Cooper':
                    sta1 = '395'
                elif STAR1 == 'Farley Granger':
                    sta1 = '396'
                elif STAR1 == 'Edmund Gwenn':
                    sta1 = '397'
                elif STAR1 == 'William Keighley':
                    sta1 = '398'
                elif STAR1 == 'Edmund Goulding':
                    sta1 = '399'
                elif STAR1 == 'Ernest B. Schoedsack':
                    sta1 = '400'
                elif STAR1 == 'Wallace Ford':
                    sta1 = '401'
                elif STAR1 == 'Max Schreck':
                    sta1 = '402'
                elif STAR1 == 'Alia Bhatt':
                    sta1 = '403'
                elif STAR1 == 'Riz Ahmed':
                    sta1 = '404'
                elif STAR1 == 'Shahab Hosseini':
                    sta1 = '405'
                elif STAR1 == 'Fionn Whitehead':
                    sta1 = '406'
                elif STAR1 == 'Giuseppe Battiston':
                    sta1 = '407'
                elif STAR1 == 'Taraji P. Henson':
                    sta1 = '408'
                elif STAR1 == 'Ben Whishaw':
                    sta1 = '409'
                elif STAR1 == 'Charlize Theron':
                    sta1 = '410'
                elif STAR1 == 'Casey Affleck':
                    sta1 = '411'
                elif STAR1 == 'Roland Møller':
                    sta1 = '412'
                elif STAR1 == 'Felicity Jones':
                    sta1 = '413'
                elif STAR1 == 'Samuel L. Jackson':
                    sta1 = '414'
                elif STAR1 == 'Saoirse Ronan':
                    sta1 = '415'
                elif STAR1 == 'Hugh Welchman':
                    sta1 = '416'
                elif STAR1 == 'Bill Nighy':
                    sta1 = '417'
                elif STAR1 == 'Bérénice Bejo':
                    sta1 = '418'
                elif STAR1 == 'Toni Servillo':
                    sta1 = '419'
                elif STAR1 == 'Chris Williams':
                    sta1 = '420'
                elif STAR1 == 'Domhnall Gleeson':
                    sta1 = '421'
                elif STAR1 == 'Sridevi':
                    sta1 = '422'
                elif STAR1 == 'Hideaki Anno':
                    sta1 = '423'
                elif STAR1 == 'Geoffrey Rush':
                    sta1 = '424'
                elif STAR1 == 'Jared Gilman':
                    sta1 = '425'
                elif STAR1 == 'Jay Baruchel':
                    sta1 = '426'
                elif STAR1 == 'Takako Matsu':
                    sta1 = '427'
                elif STAR1 == 'Lee Byung-Hun':
                    sta1 = '428'
                elif STAR1 == 'Won Bin':
                    sta1 = '429'
                elif STAR1 == 'O\'Shea Jackson Jr.':
                    sta1 = '430'
                elif STAR1 == 'Hye-ja Kim':
                    sta1 = '431'
                elif STAR1 == 'Kim Yoon-seok':
                    sta1 = '432'
                elif STAR1 == 'Ian McKellen':
                    sta1 = '433'
                elif STAR1 == 'Christian Friedel':
                    sta1 = '434'
                elif STAR1 == 'Michael Nyqvist':
                    sta1 = '435'
                elif STAR1 == 'Eddie Redmayne':
                    sta1 = '436'
                elif STAR1 == 'Asa Butterfield':
                    sta1 = '437'
                elif STAR1 == 'Glen Hansard':
                    sta1 = '438'
                elif STAR1 == 'Martin Freeman':
                    sta1 = '439'
                elif STAR1 == 'Baki Davrak':
                    sta1 = '440'
                elif STAR1 == 'Keira Knightley':
                    sta1 = '441'
                elif STAR1 == 'Denzel Washington':
                    sta1 = '442'
                elif STAR1 == 'Sam Worthington':
                    sta1 = '443'
                elif STAR1 == 'Jared Leto':
                    sta1 = '444'
                elif STAR1 == 'Gerardo Taracena':
                    sta1 = '445'
                elif STAR1 == 'Valerie Faris':
                    sta1 = '446'
                elif STAR1 == 'Shôgo Furuya':
                    sta1 = '447'
                elif STAR1 == 'Nathan Fillion':
                    sta1 = '448'
                elif STAR1 == 'Andreas Wilson':
                    sta1 = '449'
                elif STAR1 == 'Gena Rowlands':
                    sta1 = '450'
                elif STAR1 == 'Gael García Bernal':
                    sta1 = '451'
                elif STAR1 == 'Oksana Akinshina':
                    sta1 = '452'
                elif STAR1 == 'Michèle Caucheteux':
                    sta1 = '453'
                elif STAR1 == 'Lee Yeong-ae':
                    sta1 = '454'
                elif STAR1 == 'Jim Caviezel':
                    sta1 = '455'
                elif STAR1 == 'Yun-Fat Chow':
                    sta1 = '456'
                elif STAR1 == 'Cecilia Roth':
                    sta1 = '457'
                elif STAR1 == 'Vicky Jenson':
                    sta1 = '458'
                elif STAR1 == 'Takeshi Kitano':
                    sta1 = '459'
                elif STAR1 == 'Michael Douglas':
                    sta1 = '460'
                elif STAR1 == 'Emily Watson':
                    sta1 = '461'
                elif STAR1 == 'Kevin Jarre':
                    sta1 = '462'
                elif STAR1 == 'Tom Guiry':
                    sta1 = '463'
                elif STAR1 == 'David Thewlis':
                    sta1 = '464'
                elif STAR1 == 'Boyd Kirkland':
                    sta1 = '465'
                elif STAR1 == 'Winona Ryder':
                    sta1 = '466'
                elif STAR1 == 'Cuba Gooding Jr.':
                    sta1 = '467'
                elif STAR1 == 'James Caan':
                    sta1 = '468'
                elif STAR1 == 'Kirsten Dunst':
                    sta1 = '469'
                elif STAR1 == 'Matthew Broderick':
                    sta1 = '470'
                elif STAR1 == 'Gene Hackman':
                    sta1 = '471'
                elif STAR1 == 'Bruce Campbell':
                    sta1 = '472'
                elif STAR1 == 'Tom Waits':
                    sta1 = '473'
                elif STAR1 == 'Sean Astin':
                    sta1 = '474'
                elif STAR1 == 'Danny Glover':
                    sta1 = '475'
                elif STAR1 == 'Emilio Estevez':
                    sta1 = '476'
                elif STAR1 == 'Sam Waterston':
                    sta1 = '477'
                elif STAR1 == 'Sam Shepard':
                    sta1 = '478'
                elif STAR1 == 'Henry Thomas':
                    sta1 = '479'
                elif STAR1 == 'Sean Connery':
                    sta1 = '480'
                elif STAR1 == 'Barry Bostwick':
                    sta1 = '481'
                elif STAR1 == 'Edward Fox':
                    sta1 = '482'
                elif STAR1 == 'Liza Minnelli':
                    sta1 = '483'
                elif STAR1 == 'Audrey Hepburn':
                    sta1 = '484'
                elif STAR1 == 'Warren Beatty':
                    sta1 = '485'
                elif STAR1 == 'Andrew Marton':
                    sta1 = '486'
                elif STAR1 == 'Jeanne Moreau':
                    sta1 = '487'
                elif STAR1 == 'Deborah Kerr':
                    sta1 = '488'
                elif STAR1 == 'Jean-Paul Belmondo':
                    sta1 = '489'
                elif STAR1 == 'Arthur Rosson':
                    sta1 = '490'
                elif STAR1 == 'Teresa Wright':
                    sta1 = '491'
                elif STAR1 == 'Margaret Lockwood':
                    sta1 = '492'
                elif STAR1 == 'Katharine Hepburn':
                    sta1 = '493'
                elif STAR1 == 'Boris Karloff':
                    sta1 = '494'
                elif STAR1 == 'Groucho Marx':
                    sta1 = '495'
                elif STAR1 == 'Richard Rosson':
                    sta1 = '496'
                elif STAR1 == 'Colin Clive':
                    sta1 = '497'
                elif STAR1 == 'Yalitza Aparicio':
                    sta1 = '498'
                elif STAR1 == 'Josh O\'Connor':
                    sta1 = '499'
                elif STAR1 == 'Kelsey Asbille':
                    sta1 = '500'
                elif STAR1 == 'Daniel Kaluuya':
                    sta1 = '501'
                elif STAR1 == 'Rolf Lassgård':
                    sta1 = '502'
                elif STAR1 == 'Taika Waititi':
                    sta1 = '503'
                elif STAR1 == 'Hiromasa Yonebayashi':
                    sta1 = '504'
                elif STAR1 == 'Shailene Woodley':
                    sta1 = '505'
                elif STAR1 == 'Thomas Mann':
                    sta1 = '506'
                elif STAR1 == 'Michael Keaton':
                    sta1 = '507'
                elif STAR1 == 'Léa Seydoux':
                    sta1 = '508'
                elif STAR1 == 'Amit Sadh':
                    sta1 = '509'
                elif STAR1 == 'Veerle Baetens':
                    sta1 = '510'
                elif STAR1 == 'Bruce Dern':
                    sta1 = '511'
                elif STAR1 == 'John C. Reilly':
                    sta1 = '512'
                elif STAR1 == 'Jeff Bridges':
                    sta1 = '513'
                elif STAR1 == 'Owen Wilson':
                    sta1 = '514'
                elif STAR1 == 'Phil Lord':
                    sta1 = '515'
                elif STAR1 == 'Sandra Bullock':
                    sta1 = '516'
                elif STAR1 == 'Abraham Attah':
                    sta1 = '517'
                elif STAR1 == 'Jesse Eisenberg':
                    sta1 = '518'
                elif STAR1 == 'James McAvoy':
                    sta1 = '519'
                elif STAR1 == 'Zach Galifianakis':
                    sta1 = '520'
                elif STAR1 == 'Bradley Cooper':
                    sta1 = '521'
                elif STAR1 == 'Zooey Deschanel':
                    sta1 = '522'
                elif STAR1 == 'Cate Blanchett':
                    sta1 = '523'
                elif STAR1 == 'Frank Langella':
                    sta1 = '524'
                elif STAR1 == 'Megumi Hayashibara':
                    sta1 = '525'
                elif STAR1 == 'Angelina Jolie':
                    sta1 = '526'
                elif STAR1 == 'Madeline Carroll':
                    sta1 = '527'
                elif STAR1 == 'Riisa Naka':
                    sta1 = '528'
                elif STAR1 == 'Tatsuya Fujiwara':
                    sta1 = '529'
                elif STAR1 == 'Thomas Turgoose':
                    sta1 = '530'
                elif STAR1 == 'Alicia Vikander':
                    sta1 = '531'
                elif STAR1 == 'Josh Hartnett':
                    sta1 = '532'
                elif STAR1 == 'Diane Kruger':
                    sta1 = '533'
                elif STAR1 == 'Sam Riley':
                    sta1 = '534'
                elif STAR1 == 'Byron Howard':
                    sta1 = '535'
                elif STAR1 == 'Carice van Houten':
                    sta1 = '536'
                elif STAR1 == 'Stephen Chow':
                    sta1 = '537'
                elif STAR1 == 'Dakota Fanning':
                    sta1 = '538'
                elif STAR1 == 'Eileen Walsh':
                    sta1 = '539'
                elif STAR1 == 'Paddy Considine':
                    sta1 = '540'
                elif STAR1 == 'Nicolas Cage':
                    sta1 = '541'
                elif STAR1 == 'Moritz Bleibtreu':
                    sta1 = '542'
                elif STAR1 == 'Jamie Bell':
                    sta1 = '543'
                elif STAR1 == 'John Cameron Mitchell':
                    sta1 = '544'
                elif STAR1 == 'Andrew Philpot':
                    sta1 = '545'
                elif STAR1 == 'James Marsden':
                    sta1 = '546'
                elif STAR1 == 'Trey Parker':
                    sta1 = '547'
                elif STAR1 == 'Ron Livingston':
                    sta1 = '548'
                elif STAR1 == 'Jane Adams':
                    sta1 = '549'
                elif STAR1 == 'Jason Schwartzman':
                    sta1 = '550'
                elif STAR1 == 'Eduardo Noriega':
                    sta1 = '551'
                elif STAR1 == 'John Cusack':
                    sta1 = '552'
                elif STAR1 == 'Thierry Lhermitte':
                    sta1 = '553'
                elif STAR1 == 'Kenneth Branagh':
                    sta1 = '554'
                elif STAR1 == 'Liesel Matthews':
                    sta1 = '555'
                elif STAR1 == 'Leon Lai':
                    sta1 = '556'
                elif STAR1 == 'Massimo Troisi':
                    sta1 = '557'
                elif STAR1 == 'Brian O\'Halloran':
                    sta1 = '558'
                elif STAR1 == 'Andie MacDowell':
                    sta1 = '559'
                elif STAR1 == 'Michael Caine':
                    sta1 = '560'
                elif STAR1 == 'Shûichirô Moriyama':
                    sta1 = '561'
                elif STAR1 == 'Kathy Bates':
                    sta1 = '562'
                elif STAR1 == 'Bob Hoskins':
                    sta1 = '563'
                elif STAR1 == 'Bernard-Pierre Donnadieu':
                    sta1 = '564'
                elif STAR1 == 'Richard E. Grant':
                    sta1 = '565'
                elif STAR1 == 'John Lone':
                    sta1 = '566'
                elif STAR1 == 'Isabella Rossellini':
                    sta1 = '567'
                elif STAR1 == 'Griffin Dunne':
                    sta1 = '568'
                elif STAR1 == 'William Shatner':
                    sta1 = '569'
                elif STAR1 == 'Donald Sutherland':
                    sta1 = '570'
                elif STAR1 == 'David Zucker':
                    sta1 = '571'
                elif STAR1 == 'Yasuo Yamada':
                    sta1 = '572'
                elif STAR1 == 'Donald Pleasence':
                    sta1 = '573'
                elif STAR1 == 'Roman Polanski':
                    sta1 = '574'
                elif STAR1 == 'Walter Matthau':
                    sta1 = '575'
                elif STAR1 == 'Cleavon Little':
                    sta1 = '576'
                elif STAR1 == 'Bruce Lee':
                    sta1 = '577'
                elif STAR1 == 'Jon Voight':
                    sta1 = '578'
                elif STAR1 == 'Richard Burton':
                    sta1 = '579'
                elif STAR1 == 'Lee Marvin':
                    sta1 = '580'
                elif STAR1 == 'Catherine Deneuve':
                    sta1 = '581'
                elif STAR1 == 'Paul Scofield':
                    sta1 = '582'
                elif STAR1 == 'Stanley Baker':
                    sta1 = '583'
                elif STAR1 == 'Rod Taylor':
                    sta1 = '584'
                elif STAR1 == 'Karlheinz Böhm':
                    sta1 = '585'
                elif STAR1 == 'Yul Brynner':
                    sta1 = '586'
                elif STAR1 == 'Pierre Brasseur':
                    sta1 = '587'
                elif STAR1 == 'Kevin McCarthy':
                    sta1 = '588'
                elif STAR1 == 'Alec Guinness':
                    sta1 = '589'
                elif STAR1 == 'Michael Rennie':
                    sta1 = '590'
                elif STAR1 == 'Rita Hayworth':
                    sta1 = '591'
                elif STAR1 == 'Samuel Armstrong':
                    sta1 = '592'
                elif STAR1 == 'Claude Rains':
                    sta1 = '593'
                elif STAR1 == 'John Cho':
                    sta1 = '594'
                elif STAR1 == 'Maryana Spivak':
                    sta1 = '595'
                elif STAR1 == 'Brooklynn Prince':
                    sta1 = '596'
                elif STAR1 == 'Michael B. Jordan':
                    sta1 = '597'
                elif STAR1 == 'Chris Evans':
                    sta1 = '598'
                elif STAR1 == 'Michael Schwartz':
                    sta1 = '599'
                elif STAR1 == 'Laia Costa':
                    sta1 = '600'
                elif STAR1 == 'Günes Sensoy':
                    sta1 = '601'
                elif STAR1 == 'Ansel Elgort':
                    sta1 = '602'
                elif STAR1 == 'Josh Brolin':
                    sta1 = '603'
                elif STAR1 == 'Emily Blunt':
                    sta1 = '604'
                elif STAR1 == 'Aleksey Serebryakov':
                    sta1 = '605'
                elif STAR1 == 'Judi Dench':
                    sta1 = '606'
                elif STAR1 == 'Gary Oldman':
                    sta1 = '607'
                elif STAR1 == 'Jose Coronado':
                    sta1 = '608'
                elif STAR1 == 'Amy Poehler':
                    sta1 = '609'
                elif STAR1 == 'Lady Gaga':
                    sta1 = '610'
                elif STAR1 == 'Mikael Persbrandt':
                    sta1 = '611'
                elif STAR1 == 'Chris Renaud':
                    sta1 = '612'
                elif STAR1 == 'Joseph Gordon-Levitt':
                    sta1 = '613'
                elif STAR1 == 'Aaron Taylor-Johnson':
                    sta1 = '614'
                elif STAR1 == 'Luis Tosar':
                    sta1 = '615'
                elif STAR1 == 'Antonio Banderas':
                    sta1 = '616'
                elif STAR1 == 'Jürgen Vogel':
                    sta1 = '617'
                elif STAR1 == 'Quinton Aaron':
                    sta1 = '618'
                elif STAR1 == 'Richard Jenkins':
                    sta1 = '619'
                elif STAR1 == 'Charlie Cox':
                    sta1 = '620'
                elif STAR1 == 'Nora Twomey':
                    sta1 = '621'
                elif STAR1 == 'Marion Cotillard':
                    sta1 = '622'
                elif STAR1 == 'Gerard Butler':
                    sta1 = '623'
                elif STAR1 == 'Scarlett Johansson':
                    sta1 = '624'
                elif STAR1 == 'Jackie Earle Haley':
                    sta1 = '625'
                elif STAR1 == 'Philip Seymour Hoffman':
                    sta1 = '626'
                elif STAR1 == 'Brady Corbet':
                    sta1 = '627'
                elif STAR1 == 'Guillaume Canet':
                    sta1 = '628'
                elif STAR1 == 'Peter Dinklage':
                    sta1 = '629'
                elif STAR1 == 'J. Mackye Gruber':
                    sta1 = '630'
                elif STAR1 == 'Cillian Murphy':
                    sta1 = '631'
                elif STAR1 == 'Maribel Verdú':
                    sta1 = '632'
                elif STAR1 == 'Jude Law':
                    sta1 = '633'
                elif STAR1 == 'Barry Cook':
                    sta1 = '634'
                elif STAR1 == 'Susanne Lothar':
                    sta1 = '635'
                elif STAR1 == 'Rufus Sewell':
                    sta1 = '636'
                elif STAR1 == 'Bill Pullman':
                    sta1 = '637'
                elif STAR1 == 'Emma Thompson':
                    sta1 = '638'
                elif STAR1 == 'Zbigniew Zamachowski':
                    sta1 = '639'
                elif STAR1 == 'Jason London':
                    sta1 = '640'
                elif STAR1 == 'Joe Pesci':
                    sta1 = '641'
                elif STAR1 == 'Miki Imai':
                    sta1 = '642'
                elif STAR1 == 'Jean-Pierre Jeunet':
                    sta1 = '643'
                elif STAR1 == 'Macaulay Culkin':
                    sta1 = '644'
                elif STAR1 == 'Billy Crystal':
                    sta1 = '645'
                elif STAR1 == 'Leslie Nielsen':
                    sta1 = '646'
                elif STAR1 == 'Steve Martin':
                    sta1 = '647'
                elif STAR1 == 'Michael Beck':
                    sta1 = '648'
                elif STAR1 == 'Jim Henson':
                    sta1 = '649'
                elif STAR1 == 'John Hubley':
                    sta1 = '650'
                elif STAR1 == 'Brad Davis':
                    sta1 = '651'
                elif STAR1 == 'Richard Dreyfuss':
                    sta1 = '652'
                elif STAR1 == 'Elliott Gould':
                    sta1 = '653'
                elif STAR1 == 'Rod Steiger':
                    sta1 = '654'
                elif STAR1 == 'Phil Harris':
                    sta1 = '655'
                elif STAR1 == 'David Hemmings':
                    sta1 = '656'
                elif STAR1 == 'John Lennon':
                    sta1 = '657'
                elif STAR1 == 'Tallulah Bankhead':
                    sta1 = '658'
                elif STAR1 == 'Robert Donat':
                    sta1 = '659'
                
                STAR2 = request.form['star2']
                if STAR2 == 'Morgan Freeman':
                     sta2 = '0'
                elif STAR2 == 'Al Pacino':
                    sta2 = '1'
                elif STAR2 == 'Heath Ledger':
                    sta2 = '2'
                elif STAR2 == 'Robert De Niro':
                    sta2 = '3'
                elif STAR2 == 'Lee J. Cobb':
                    sta2 = '4'
                elif STAR2 == 'Viggo Mortensen':
                    sta2 = '5'
                elif STAR2 == 'Uma Thurman':
                    sta2 = '6'
                elif STAR2 == 'Ralph Fiennes':
                    sta2 = '7'
                elif STAR2 == 'Joseph Gordon-Levitt':
                    sta2 = '8'
                elif STAR2 == 'Edward Norton':
                    sta2 = '9'
                elif STAR2 == 'Ian McKellen':
                    sta2 = '10'
                elif STAR2 == 'Robin Wright':
                    sta2 = '11'
                elif STAR2 == 'Eli Wallach':
                    sta2 = '12'
                elif STAR2 == 'Keanu Reeves':
                    sta2 = '13'
                elif STAR2 == 'Ray Liotta':
                    sta2 = '14'
                elif STAR2 == 'Harrison Ford':
                    sta2 = '15'
                elif STAR2 == 'Louise Fletcher':
                    sta2 = '16'
                elif STAR2 == 'Phillipa Soo':
                    sta2 = '17'
                elif STAR2 == 'Lee Sun-kyun':
                    sta2 = '18'
                elif STAR2 == 'Madhavan':
                    sta2 = '19'
                elif STAR2 == 'Anne Hathaway':
                    sta2 = '20'
                elif STAR2 == 'Alexandre Rodrigues':
                    sta2 = '21'
                elif STAR2 == 'Suzanne Pleshette':
                    sta2 = '22'
                elif STAR2 == 'Matt Damon':
                    sta2 = '23'
                elif STAR2 == 'Michael Clarke Duncan':
                    sta2 = '24'
                elif STAR2 == 'Nicoletta Braschi':
                    sta2 = '25'
                elif STAR2 == 'Brad Pitt':
                    sta2 = '26'
                elif STAR2 == 'Anthony Hopkins':
                    sta2 = '27'
                elif STAR2 == 'Akira Ishihama':
                    sta2 = '28'
                elif STAR2 == 'Takashi Shimura':
                    sta2 = '29'
                elif STAR2 == 'Donna Reed':
                    sta2 = '30'
                elif STAR2 == 'J.K. Simmons':
                    sta2 = '31'
                elif STAR2 == 'François Cluzet':
                    sta2 = '32'
                elif STAR2 == 'Hugh Jackman':
                    sta2 = '33'
                elif STAR2 == 'Thomas Kretschmann':
                    sta2 = '34'
                elif STAR2 == 'Joaquin Phoenix':
                    sta2 = '35'
                elif STAR2 == 'Edward Furlong':
                    sta2 = '36'
                elif STAR2 == 'Gabriel Byrne':
                    sta2 = '37'
                elif STAR2 == 'Gary Oldman':
                    sta2 = '38'
                elif STAR2 == 'Matthew Broderick':
                    sta2 = '39'
                elif STAR2 == 'Linda Hamilton':
                    sta2 = '40'
                elif STAR2 == 'Enzo Cannavale':
                    sta2 = '41'
                elif STAR2 == 'Ayano Shiraishi':
                    sta2 = '42'
                elif STAR2 == 'Christopher Lloyd':
                    sta2 = '43'
                elif STAR2 == 'Charles Bronson':
                    sta2 = '44'
                elif STAR2 == 'Janet Leigh':
                    sta2 = '45'
                elif STAR2 == 'Ingrid Bergman':
                    sta2 = '46'
                elif STAR2 == 'Paulette Goddard':
                    sta2 = '47'
                elif STAR2 == 'Virginia Cherrill':
                    sta2 = '48'
                elif STAR2 == 'Yordanos Shiferaw':
                    sta2 = '49'
                elif STAR2 == 'Çetin Tekindor':
                    sta2 = '50'
                elif STAR2 == 'Mone Kamishiraishi':
                    sta2 = '51'
                elif STAR2 == 'Sakshi Tanwar':
                    sta2 = '52'
                elif STAR2 == 'Rodney Rothman':
                    sta2 = '53'
                elif STAR2 == 'Robert Downey Jr.':
                    sta2 = '54'
                elif STAR2 == 'Anthony Gonzalez':
                    sta2 = '55'
                elif STAR2 == 'Christoph Waltz':
                    sta2 = '56'
                elif STAR2 == 'Tom Hardy':
                    sta2 = '57'
                elif STAR2 == 'Darsheel Safary':
                    sta2 = '58'
                elif STAR2 == 'Elissa Knight':
                    sta2 = '59'
                elif STAR2 == 'Martina Gedeck':
                    sta2 = '60'
                elif STAR2 == 'Yoo Ji-Tae':
                    sta2 = '61'
                elif STAR2 == 'Carrie-Anne Moss':
                    sta2 = '62'
                elif STAR2 == 'Yuriko Ishida':
                    sta2 = '63'
                elif STAR2 == 'James Woods':
                    sta2 = '64'
                elif STAR2 == 'Karen Allen':
                    sta2 = '65'
                elif STAR2 == 'Shelley Duvall':
                    sta2 = '66'
                elif STAR2 == 'Marlon Brando':
                    sta2 = '67'
                elif STAR2 == 'Tom Skerritt':
                    sta2 = '68'
                elif STAR2 == 'Amitabh Bachchan':
                    sta2 = '69'
                elif STAR2 == 'Yutaka Sada':
                    sta2 = '70'
                elif STAR2 == 'George C. Scott':
                    sta2 = '71'
                elif STAR2 == 'Marlene Dietrich':
                    sta2 = '72'
                elif STAR2 == 'Ralph Meeker':
                    sta2 = '73'
                elif STAR2 == 'Grace Kelly':
                    sta2 = '74'
                elif STAR2 == 'Gloria Swanson':
                    sta2 = '75'
                elif STAR2 == 'George MacKay':
                    sta2 = '76'
                elif STAR2 == 'Adesh Prasad':
                    sta2 = '77'
                elif STAR2 == 'Tabu':
                    sta2 = '78'
                elif STAR2 == 'Meena':
                    sta2 = '79'
                elif STAR2 == 'Thomas Bo Larsen':
                    sta2 = '80'
                elif STAR2 == 'Leila Hatami':
                    sta2 = '81'
                elif STAR2 == 'Mélissa Désormeaux-Poulin':
                    sta2 = '82'
                elif STAR2 == 'Nisa Sofiya Aksongur':
                    sta2 = '83'
                elif STAR2 == 'Fikret Kuskan':
                    sta2 = '84'
                elif STAR2 == 'Diane Kruger':
                    sta2 = '85'
                elif STAR2 == 'Kate Winslet':
                    sta2 = '86'
                elif STAR2 == 'Mathieu Kassovitz':
                    sta2 = '87'
                elif STAR2 == 'Jared Leto':
                    sta2 = '88'
                elif STAR2 == 'Annette Bening':
                    sta2 = '89'
                elif STAR2 == 'Amir Farrokh Hashemian':
                    sta2 = '90'
                elif STAR2 == 'Tim Allen':
                    sta2 = '91'
                elif STAR2 == 'Sophie Marceau':
                    sta2 = '92'
                elif STAR2 == 'Tim Roth':
                    sta2 = '93'
                elif STAR2 == 'R. Lee Ermey':
                    sta2 = '94'
                elif STAR2 == 'Olga Mironova':
                    sta2 = '95'
                elif STAR2 == 'Michael Biehn':
                    sta2 = '96'
                elif STAR2 == 'Tom Hulce':
                    sta2 = '97'
                elif STAR2 == 'Michelle Pfeiffer':
                    sta2 = '98'
                elif STAR2 == 'Herbert Grönemeyer':
                    sta2 = '99'
                elif STAR2 == 'Jodie Foster':
                    sta2 = '100'
                elif STAR2 == 'Robert Redford':
                    sta2 = '101'
                elif STAR2 == 'Patrick Magee':
                    sta2 = '102'
                elif STAR2 == 'Gary Lockwood':
                    sta2 = '103'
                elif STAR2 == 'Lee Van Cleef':
                    sta2 = '104'
                elif STAR2 == 'Alec Guinness':
                    sta2 = '105'
                elif STAR2 == 'Shirley MacLaine':
                    sta2 = '106'
                elif STAR2 == 'Eva Marie Saint':
                    sta2 = '107'
                elif STAR2 == 'Kim Novak':
                    sta2 = '108'
                elif STAR2 == 'Gene Kelly':
                    sta2 = '109'
                elif STAR2 == 'Nobuo Kaneko':
                    sta2 = '110'
                elif STAR2 == 'Enzo Staiola':
                    sta2 = '111'
                elif STAR2 == 'Barbara Stanwyck':
                    sta2 = '112'
                elif STAR2 == 'Joseph Cotten':
                    sta2 = '113'
                elif STAR2 == 'Ellen Widmann':
                    sta2 = '114'
                elif STAR2 == 'Alfred Abel':
                    sta2 = '115'
                elif STAR2 == 'Edna Purviance':
                    sta2 = '116'
                elif STAR2 == 'Shraddha Kapoor':
                    sta2 = '117'
                elif STAR2 == 'Paresh Rawal':
                    sta2 = '118'
                elif STAR2 == 'Srinidhi Shetty':
                    sta2 = '119'
                elif STAR2 == 'Mahershala Ali':
                    sta2 = '120'
                elif STAR2 == 'Woody Harrelson':
                    sta2 = '121'
                elif STAR2 == 'Konkona Sen Sharma':
                    sta2 = '122'
                elif STAR2 == 'Rana Daggubati':
                    sta2 = '123'
                elif STAR2 == 'Jason Schwartzman':
                    sta2 = '124'
                elif STAR2 == 'Shriya Saran':
                    sta2 = '125'
                elif STAR2 == 'Rajkummar Rao':
                    sta2 = '126'
                elif STAR2 == 'Elmo Nüganen':
                    sta2 = '127'
                elif STAR2 == 'Sonam Kapoor':
                    sta2 = '128'
                elif STAR2 == 'Richa Chadha':
                    sta2 = '129'
                elif STAR2 == 'Ronit Roy':
                    sta2 = '130'
                elif STAR2 == 'Mahie Gill':
                    sta2 = '131'
                elif STAR2 == 'Soledad Villamil':
                    sta2 = '132'
                elif STAR2 == 'Nick Nolte':
                    sta2 = '133'
                elif STAR2 == 'Emily Mortimer':
                    sta2 = '134'
                elif STAR2 == 'Edward Asner':
                    sta2 = '135'
                elif STAR2 == 'Jonah Hill':
                    sta2 = '136'
                elif STAR2 == 'Vidya Malvade':
                    sta2 = '137'
                elif STAR2 == 'Paul Dano':
                    sta2 = '138'
                elif STAR2 == 'Ariadna Gil':
                    sta2 = '139'
                elif STAR2 == 'Natalie Portman':
                    sta2 = '140'
                elif STAR2 == 'Soha Ali Khan':
                    sta2 = '141'
                elif STAR2 == 'Rani Mukerji':
                    sta2 = '142'
                elif STAR2 == 'Michael Caine':
                    sta2 = '143'
                elif STAR2 == 'Gayatri Joshi':
                    sta2 = '144'
                elif STAR2 == 'Alexandra Maria Lara':
                    sta2 = '145'
                elif STAR2 == 'Takuya Kimura':
                    sta2 = '146'
                elif STAR2 == 'Ed Harris':
                    sta2 = '147'
                elif STAR2 == 'Sunil Shetty':
                    sta2 = '148'
                elif STAR2 == 'Dexter Fletcher':
                    sta2 = '149'
                elif STAR2 == 'Russell Crowe':
                    sta2 = '150'
                elif STAR2 == 'Ugur Yücel':
                    sta2 = '151'
                elif STAR2 == 'Sharon Stone':
                    sta2 = '152'
                elif STAR2 == 'Salman Khan':
                    sta2 = '153'
                elif STAR2 == 'Gene Hackman':
                    sta2 = '154'
                elif STAR2 == 'Sean Connery':
                    sta2 = '155'
                elif STAR2 == 'Bora Todorovic':
                    sta2 = '156'
                elif STAR2 == 'Noriko Hidaka':
                    sta2 = '157'
                elif STAR2 == 'Alan Rickman':
                    sta2 = '158'
                elif STAR2 == 'Akira Terao':
                    sta2 = '159'
                elif STAR2 == 'Cathy Moriarty':
                    sta2 = '160'
                elif STAR2 == 'Aleksandr Kaydanovskiy':
                    sta2 = '161'
                elif STAR2 == 'Liv Ullmann':
                    sta2 = '162'
                elif STAR2 == 'Irene Papas':
                    sta2 = '163'
                elif STAR2 == 'Dharmendra':
                    sta2 = '164'
                elif STAR2 == 'Graham Chapman':
                    sta2 = '165'
                elif STAR2 == 'James Garner':
                    sta2 = '166'
                elif STAR2 == 'John Megna':
                    sta2 = '167'
                elif STAR2 == 'Eijirô Tôno':
                    sta2 = '168'
                elif STAR2 == 'Burt Lancaster':
                    sta2 = '169'
                elif STAR2 == 'Tony Curtis':
                    sta2 = '170'
                elif STAR2 == 'Bibi Andersson':
                    sta2 = '171'
                elif STAR2 == 'Gunnar Björnstrand':
                    sta2 = '172'
                elif STAR2 == 'Carl Möhner':
                    sta2 = '173'
                elif STAR2 == 'Chieko Higashiyama':
                    sta2 = '174'
                elif STAR2 == 'Machiko Kyô':
                    sta2 = '175'
                elif STAR2 == 'Anne Baxter':
                    sta2 = '176'
                elif STAR2 == 'Walter Huston':
                    sta2 = '177'
                elif STAR2 == 'Jack Benny':
                    sta2 = '178'
                elif STAR2 == 'Mack Swain':
                    sta2 = '179'
                elif STAR2 == 'Kathryn McGuire':
                    sta2 = '180'
                elif STAR2 == 'Adèle Haenel':
                    sta2 = '181'
                elif STAR2 == 'Saori Hayami':
                    sta2 = '182'
                elif STAR2 == 'Ana Wagener':
                    sta2 = '183'
                elif STAR2 == 'Jung-woo Ha':
                    sta2 = '184'
                elif STAR2 == 'Antoine Olivier Pilon':
                    sta2 = '185'
                elif STAR2 == 'Patrick Stewart':
                    sta2 = '186'
                elif STAR2 == 'Jacob Tremblay':
                    sta2 = '187'
                elif STAR2 == 'María Marull':
                    sta2 = '188'
                elif STAR2 == 'Jamie Foxx':
                    sta2 = '189'
                elif STAR2 == 'Melisa Sözen':
                    sta2 = '190'
                elif STAR2 == 'Anushka Sharma':
                    sta2 = '191'
                elif STAR2 == 'Akshay Kumar':
                    sta2 = '192'
                elif STAR2 == 'F. Murray Abraham':
                    sta2 = '193'
                elif STAR2 == 'Rosamund Pike':
                    sta2 = '194'
                elif STAR2 == 'Takao Osawa':
                    sta2 = '195'
                elif STAR2 == 'Sam Worthington':
                    sta2 = '196'
                elif STAR2 == 'Amy Poehler':
                    sta2 = '197'
                elif STAR2 == 'Priyanka Chopra':
                    sta2 = '198'
                elif STAR2 == 'Michael Kenneth Williams':
                    sta2 = '199'
                elif STAR2 == 'Chris Hemsworth':
                    sta2 = '200'
                elif STAR2 == 'Christian Bale':
                    sta2 = '201'
                elif STAR2 == 'Michael Keaton':
                    sta2 = '202'
                elif STAR2 == 'Brendan Gleeson':
                    sta2 = '203'
                elif STAR2 == 'Parambrata Chattopadhyay':
                    sta2 = '204'
                elif STAR2 == 'Farhan Akhtar':
                    sta2 = '205'
                elif STAR2 == 'Jake Gyllenhaal':
                    sta2 = '206'
                elif STAR2 == 'Charlize Theron':
                    sta2 = '207'
                elif STAR2 == 'Naseeruddin Shah':
                    sta2 = '208'
                elif STAR2 == 'Bee Vang':
                    sta2 = '209'
                elif STAR2 == 'Emma Watson':
                    sta2 = '210'
                elif STAR2 == 'Ryôko Hirosue':
                    sta2 = '211'
                elif STAR2 == 'Joan Allen':
                    sta2 = '212'
                elif STAR2 == 'Philip Seymour Hoffman':
                    sta2 = '213'
                elif STAR2 == 'Jay Baruchel':
                    sta2 = '214'
                elif STAR2 == 'Vince Vaughn':
                    sta2 = '215'
                elif STAR2 == 'Tommy Lee Jones':
                    sta2 = '216'
                elif STAR2 == 'Arshad Warsi':
                    sta2 = '217'
                elif STAR2 == 'Clint Eastwood':
                    sta2 = '218'
                elif STAR2 == 'Sophie Okonedo':
                    sta2 = '219'
                elif STAR2 == 'Won Bin':
                    sta2 = '220'
                elif STAR2 == 'Julie Delpy':
                    sta2 = '221'
                elif STAR2 == 'Kim Sang-kyung':
                    sta2 = '222'
                elif STAR2 == 'Saif Ali Khan':
                    sta2 = '223'
                elif STAR2 == 'David Carradine':
                    sta2 = '224'
                elif STAR2 == 'Albert Brooks':
                    sta2 = '225'
                elif STAR2 == 'Tom Hanks':
                    sta2 = '226'
                elif STAR2 == 'Gael García Bernal':
                    sta2 = '227'
                elif STAR2 == 'Lee Unkrich':
                    sta2 = '228'
                elif STAR2 == 'Megumi Ogata':
                    sta2 = '229'
                elif STAR2 == 'Raghuvir Yadav':
                    sta2 = '230'
                elif STAR2 == 'Haley Joel Osment':
                    sta2 = '231'
                elif STAR2 == 'Pruitt Taylor Vince':
                    sta2 = '232'
                elif STAR2 == 'Srdjan \'Zika\' Todorovic':
                    sta2 = '233'
                elif STAR2 == 'Jeff Bridges':
                    sta2 = '234'
                elif STAR2 == 'Maggie Cheung':
                    sta2 = '235'
                elif STAR2 == 'Ewen Bremner':
                    sta2 = '236'
                elif STAR2 == 'William H. Macy':
                    sta2 = '237'
                elif STAR2 == 'Lazar Ristovski':
                    sta2 = '238'
                elif STAR2 == 'Hubert Koundé':
                    sta2 = '239'
                elif STAR2 == 'Kajol':
                    sta2 = '240'
                elif STAR2 == 'Jean-Louis Trintignant':
                    sta2 = '241'
                elif STAR2 == 'Takeshi Kaneshiro':
                    sta2 = '242'
                elif STAR2 == 'Laura Dern':
                    sta2 = '243'
                elif STAR2 == 'Pete Postlethwaite':
                    sta2 = '244'
                elif STAR2 == 'Fengyi Zhang':
                    sta2 = '245'
                elif STAR2 == 'Jingwu Ma':
                    sta2 = '246'
                elif STAR2 == 'Robert Sean Leonard':
                    sta2 = '247'
                elif STAR2 == 'River Phoenix':
                    sta2 = '248'
                elif STAR2 == 'Tom Berenger':
                    sta2 = '249'
                elif STAR2 == 'Nastassja Kinski':
                    sta2 = '250'
                elif STAR2 == 'Mahito Tsujimura':
                    sta2 = '251'
                elif STAR2 == 'Wilford Brimley':
                    sta2 = '252'
                elif STAR2 == 'Christine Hargreaves':
                    sta2 = '253'
                elif STAR2 == 'Claudia Cardinale':
                    sta2 = '254'
                elif STAR2 == 'Pernilla Allwin':
                    sta2 = '255'
                elif STAR2 == 'Rutger Hauer':
                    sta2 = '256'
                elif STAR2 == 'John Hurt':
                    sta2 = '257'
                elif STAR2 == 'John Cleese':
                    sta2 = '258'
                elif STAR2 == 'Christopher Walken':
                    sta2 = '259'
                elif STAR2 == 'Talia Shire':
                    sta2 = '260'
                elif STAR2 == 'William Holden':
                    sta2 = '261'
                elif STAR2 == 'Marisa Berenson':
                    sta2 = '262'
                elif STAR2 == 'Filipp Yankovskiy':
                    sta2 = '263'
                elif STAR2 == 'Faye Dunaway':
                    sta2 = '264'
                elif STAR2 == 'Tatum O\'Neal':
                    sta2 = '265'
                elif STAR2 == 'Donatas Banionis':
                    sta2 = '266'
                elif STAR2 == 'François Périer':
                    sta2 = '267'
                elif STAR2 == 'George Kennedy':
                    sta2 = '268'
                elif STAR2 == 'Ivan Lapikov':
                    sta2 = '269'
                elif STAR2 == 'Jean Martin':
                    sta2 = '270'
                elif STAR2 == 'Jacqueline Andere':
                    sta2 = '271'
                elif STAR2 == 'Joan Crawford':
                    sta2 = '272'
                elif STAR2 == 'Tatsuya Nakadai':
                    sta2 = '273'
                elif STAR2 == 'John Wayne':
                    sta2 = '274'
                elif STAR2 == 'Nikolay Burlyaev':
                    sta2 = '275'
                elif STAR2 == 'Birgitta Valberg':
                    sta2 = '276'
                elif STAR2 == 'Fredric March':
                    sta2 = '277'
                elif STAR2 == 'Albert Rémy':
                    sta2 = '278'
                elif STAR2 == 'Jack Hawkins':
                    sta2 = '279'
                elif STAR2 == 'Misa Uehara':
                    sta2 = '280'
                elif STAR2 == 'Minoru Chiaki':
                    sta2 = '281'
                elif STAR2 == 'Karl Malden':
                    sta2 = '282'
                elif STAR2 == 'Charles Vanel':
                    sta2 = '283'
                elif STAR2 == 'Jan Sterling':
                    sta2 = '284'
                elif STAR2 == 'Virginia Mayo':
                    sta2 = '285'
                elif STAR2 == 'Anton Walbrook':
                    sta2 = '286'
                elif STAR2 == 'James Stewart':
                    sta2 = '287'
                elif STAR2 == 'Joan Fontaine':
                    sta2 = '288'
                elif STAR2 == 'Jean Arthur':
                    sta2 = '289'
                elif STAR2 == 'Sam Wood':
                    sta2 = '290'
                elif STAR2 == 'Dita Parlo':
                    sta2 = '291'
                elif STAR2 == 'Claudette Colbert':
                    sta2 = '292'
                elif STAR2 == 'Eugene Silvain':
                    sta2 = '293'
                elif STAR2 == 'Merna Kennedy':
                    sta2 = '294'
                elif STAR2 == 'Janet Gaynor':
                    sta2 = '295'
                elif STAR2 == 'Buster Keaton':
                    sta2 = '296'
                elif STAR2 == 'Conrad Veidt':
                    sta2 = '297'
                elif STAR2 == 'Neena Gupta':
                    sta2 = '298'
                elif STAR2 == 'Julianne Nicholson':
                    sta2 = '299'
                elif STAR2 == 'Nimrat Kaur':
                    sta2 = '300'
                elif STAR2 == 'Harshaali Malhotra':
                    sta2 = '301'
                elif STAR2 == 'Danny Denzongpa':
                    sta2 = '302'
                elif STAR2 == 'Emma Stone':
                    sta2 = '303'
                elif STAR2 == 'Nicole Kidman':
                    sta2 = '304'
                elif STAR2 == 'Jessica Chastain':
                    sta2 = '305'
                elif STAR2 == 'Jared Bush':
                    sta2 = '306'
                elif STAR2 == 'James Caan':
                    sta2 = '307'
                elif STAR2 == 'Owen Wilson':
                    sta2 = '308'
                elif STAR2 == 'Nakul Roshan Sahdev':
                    sta2 = '309'
                elif STAR2 == 'Anupam Kher':
                    sta2 = '310'
                elif STAR2 == 'Frantz Turner':
                    sta2 = '311'
                elif STAR2 == 'Yayan Ruhian':
                    sta2 = '312'
                elif STAR2 == 'Keira Knightley':
                    sta2 = '313'
                elif STAR2 == 'Vin Diesel':
                    sta2 = '314'
                elif STAR2 == 'Ryan Gosling':
                    sta2 = '315'
                elif STAR2 == 'Amy Adams':
                    sta2 = '316'
                elif STAR2 == 'Lucy Boynton':
                    sta2 = '317'
                elif STAR2 == 'Irandhir Santos':
                    sta2 = '318'
                elif STAR2 == 'Geoffrey Rush':
                    sta2 = '319'
                elif STAR2 == 'Viola Davis':
                    sta2 = '320'
                elif STAR2 == 'Morena Baccarin':
                    sta2 = '321'
                elif STAR2 == 'Shahab Hosseini':
                    sta2 = '322'
                elif STAR2 == 'Simon Yam':
                    sta2 = '323'
                elif STAR2 == 'Mete Horozoglu':
                    sta2 = '324'
                elif STAR2 == 'Dev Patel':
                    sta2 = '325'
                elif STAR2 == 'Mila Kunis':
                    sta2 = '326'
                elif STAR2 == 'André Ramiro':
                    sta2 = '327'
                elif STAR2 == 'Chris Evans':
                    sta2 = '328'
                elif STAR2 == 'Chiara Mastroianni':
                    sta2 = '329'
                elif STAR2 == 'Jennifer Garner':
                    sta2 = '330'
                elif STAR2 == 'Thandie Newton':
                    sta2 = '331'
                elif STAR2 == 'Djimon Hounsou':
                    sta2 = '332'
                elif STAR2 == 'Edgar Ramírez':
                    sta2 = '333'
                elif STAR2 == 'Hee Jae':
                    sta2 = '334'
                elif STAR2 == 'Robert Rodriguez':
                    sta2 = '335'
                elif STAR2 == 'Mathieu Amalric':
                    sta2 = '336'
                elif STAR2 == 'Özge Özberk':
                    sta2 = '337'
                elif STAR2 == 'Brad Garrett':
                    sta2 = '338'
                elif STAR2 == 'Eva Green':
                    sta2 = '339'
                elif STAR2 == 'Ivan Dobronravov':
                    sta2 = '340'
                elif STAR2 == 'Yeong-su Oh':
                    sta2 = '341'
                elif STAR2 == 'Belén Rueda':
                    sta2 = '342'
                elif STAR2 == 'Renée Zellweger':
                    sta2 = '343'
                elif STAR2 == 'Shah Rukh Khan':
                    sta2 = '344'
                elif STAR2 == 'Andy Lau':
                    sta2 = '345'
                elif STAR2 == 'Albert Finney':
                    sta2 = '346'
                elif STAR2 == 'Samuel L. Jackson':
                    sta2 = '347'
                elif STAR2 == 'Jun Ji-Hyun':
                    sta2 = '348'
                elif STAR2 == 'Paul Bettany':
                    sta2 = '349'
                elif STAR2 == 'Yilmaz Erdogan':
                    sta2 = '350'
                elif STAR2 == 'Jena Malone':
                    sta2 = '351'
                elif STAR2 == 'Jason Robards':
                    sta2 = '352'
                elif STAR2 == 'Catherine Deneuve':
                    sta2 = '353'
                elif STAR2 == 'Sissy Spacek':
                    sta2 = '354'
                elif STAR2 == 'Rica Matsumoto':
                    sta2 = '355'
                elif STAR2 == 'Henning Moritzen':
                    sta2 = '356'
                elif STAR2 == 'Vinícius de Oliveira':
                    sta2 = '357'
                elif STAR2 == 'Harry Connick Jr.':
                    sta2 = '358'
                elif STAR2 == 'Jan Josef Liefers':
                    sta2 = '359'
                elif STAR2 == 'Dwight Yoakam':
                    sta2 = '360'
                elif STAR2 == 'Brenda Blethyn':
                    sta2 = '361'
                elif STAR2 == 'Madeleine Stowe':
                    sta2 = '362'
                elif STAR2 == 'Iemasa Kayumi':
                    sta2 = '363'
                elif STAR2 == 'Chris Sarandon':
                    sta2 = '364'
                elif STAR2 == 'Andie MacDowell':
                    sta2 = '365'
                elif STAR2 == 'Jesse Borrego':
                    sta2 = '366'
                elif STAR2 == 'Chris O\'Donnell':
                    sta2 = '367'
                elif STAR2 == 'Scott Weinger':
                    sta2 = '368'
                elif STAR2 == 'Paige O\'Hara':
                    sta2 = '369'
                elif STAR2 == 'Mary McDonnell':
                    sta2 = '370'
                elif STAR2 == 'Ossie Davis':
                    sta2 = '371'
                elif STAR2 == 'Tom Cruise':
                    sta2 = '372'
                elif STAR2 == 'Nozomu Sasaki':
                    sta2 = '373'
                elif STAR2 == 'Mandy Patinkin':
                    sta2 = '374'
                elif STAR2 == 'Solveig Dommartin':
                    sta2 = '375'
                elif STAR2 == 'Raphael Fejtö':
                    sta2 = '376'
                elif STAR2 == 'Keiko Yokozawa':
                    sta2 = '377'
                elif STAR2 == 'John Gielgud':
                    sta2 = '378'
                elif STAR2 == 'Tsutomu Yamazaki':
                    sta2 = '379'
                elif STAR2 == 'Diane Keaton':
                    sta2 = '380'
                elif STAR2 == 'Robert Shaw':
                    sta2 = '381'
                elif STAR2 == 'John Cazale':
                    sta2 = '382'
                elif STAR2 == 'Madeline Kahn':
                    sta2 = '383'
                elif STAR2 == 'Dustin Hoffman':
                    sta2 = '384'
                elif STAR2 == 'Max von Sydow':
                    sta2 = '385'
                elif STAR2 == 'Norma Crane':
                    sta2 = '386'
                elif STAR2 == 'Stefania Sandrelli':
                    sta2 = '387'
                elif STAR2 == 'John Cassavetes':
                    sta2 = '388'
                elif STAR2 == 'Roddy McDowall':
                    sta2 = '389'
                elif STAR2 == 'Anne Bancroft':
                    sta2 = '390'
                elif STAR2 == 'Richard Burton':
                    sta2 = '391'
                elif STAR2 == 'Christopher Plummer':
                    sta2 = '392'
                elif STAR2 == 'Julie Christie':
                    sta2 = '393'
                elif STAR2 == 'Gian Maria Volontè':
                    sta2 = '394'
                elif STAR2 == 'Anouk Aimée':
                    sta2 = '395'
                elif STAR2 == 'Sady Rebbot':
                    sta2 = '396'
                elif STAR2 == 'Jackie Gleason':
                    sta2 = '397'
                elif STAR2 == 'Anita Ekberg':
                    sta2 = '398'
                elif STAR2 == 'Dean Martin':
                    sta2 = '399'
                elif STAR2 == 'Lee Remick':
                    sta2 = '400'
                elif STAR2 == 'Orson Welles':
                    sta2 = '401'
                elif STAR2 == 'Paul Newman':
                    sta2 = '402'
                elif STAR2 == 'Coleen Gray':
                    sta2 = '403'
                elif STAR2 == 'Shelley Winters':
                    sta2 = '404'
                elif STAR2 == 'Giulietta Masina':
                    sta2 = '405'
                elif STAR2 == 'Véra Clouzot':
                    sta2 = '406'
                elif STAR2 == 'Don Taylor':
                    sta2 = '407'
                elif STAR2 == 'Audrey Hepburn':
                    sta2 = '408'
                elif STAR2 == 'Gloria Grahame':
                    sta2 = '409'
                elif STAR2 == 'John Dall':
                    sta2 = '410'
                elif STAR2 == 'Jane Greer':
                    sta2 = '411'
                elif STAR2 == 'Trevor Howard':
                    sta2 = '412'
                elif STAR2 == 'Dana Andrews':
                    sta2 = '413'
                elif STAR2 == 'Priscilla Lane':
                    sta2 = '414'
                elif STAR2 == 'Mary Astor':
                    sta2 = '415'
                elif STAR2 == 'Jane Darwell':
                    sta2 = '416'
                elif STAR2 == 'Mervyn LeRoy':
                    sta2 = '417'
                elif STAR2 == 'Nora Gregor':
                    sta2 = '418'
                elif STAR2 == 'Myrna Loy':
                    sta2 = '419'
                elif STAR2 == 'Louis Wolheim':
                    sta2 = '420'
                elif STAR2 == 'Vladimir Barskiy':
                    sta2 = '421'
                elif STAR2 == 'Sanjana Sanghi':
                    sta2 = '422'
                elif STAR2 == 'Sakura Andô':
                    sta2 = '423'
                elif STAR2 == 'Scarlett Johansson':
                    sta2 = '424'
                elif STAR2 == 'Timothée Chalamet':
                    sta2 = '425'
                elif STAR2 == 'Dave Johns':
                    sta2 = '426'
                elif STAR2 == 'Koyu Rankin':
                    sta2 = '427'
                elif STAR2 == 'Julian Dennison':
                    sta2 = '428'
                elif STAR2 == 'Aidan Gillen':
                    sta2 = '429'
                elif STAR2 == 'Tom Hiddleston':
                    sta2 = '430'
                elif STAR2 == 'Rene Russo':
                    sta2 = '431'
                elif STAR2 == 'Thomasin McKenzie':
                    sta2 = '432'
                elif STAR2 == 'Jeremy Renner':
                    sta2 = '433'
                elif STAR2 == 'John Boyega':
                    sta2 = '434'
                elif STAR2 == 'Bérénice Bejo':
                    sta2 = '435'
                elif STAR2 == 'Emily Blunt':
                    sta2 = '436'
                elif STAR2 == 'Emmanuelle Riva':
                    sta2 = '437'
                elif STAR2 == 'Niels Arestrup':
                    sta2 = '438'
                elif STAR2 == 'Kevin Spacey':
                    sta2 = '439'
                elif STAR2 == 'Lina Leandersson':
                    sta2 = '440'
                elif STAR2 == 'David James':
                    sta2 = '441'
                elif STAR2 == 'Marisa Tomei':
                    sta2 = '442'
                elif STAR2 == 'Kareena Kapoor':
                    sta2 = '443'
                elif STAR2 == 'Patricia Arquette':
                    sta2 = '444'
                elif STAR2 == 'Laura Vasiliu':
                    sta2 = '445'
                elif STAR2 == 'Zachary Quinto':
                    sta2 = '446'
                elif STAR2 == 'Tony Todd':
                    sta2 = '447'
                elif STAR2 == 'Kazunari Ninomiya':
                    sta2 = '448'
                elif STAR2 == 'Catinca Untaru':
                    sta2 = '449'
                elif STAR2 == 'Irrfan Khan':
                    sta2 = '450'
                elif STAR2 == 'Meryl Streep':
                    sta2 = '451'
                elif STAR2 == 'Marc-André Grondin':
                    sta2 = '452'
                elif STAR2 == 'François Berléand':
                    sta2 = '453'
                elif STAR2 == 'Gwyneth Paltrow':
                    sta2 = '454'
                elif STAR2 == 'Nick Frost':
                    sta2 = '455'
                elif STAR2 == 'Sibel Kekilli':
                    sta2 = '456'
                elif STAR2 == 'Tim Robbins':
                    sta2 = '457'
                elif STAR2 == 'Tony Chiu-Wai Leung':
                    sta2 = '458'
                elif STAR2 == 'Javier Cámara':
                    sta2 = '459'
                elif STAR2 == 'Rene Bitorajac':
                    sta2 = '460'
                elif STAR2 == 'Hiroyuki Okiura':
                    sta2 = '461'
                elif STAR2 == 'Gastón Pauls':
                    sta2 = '462'
                elif STAR2 == 'Clive Owen':
                    sta2 = '463'
                elif STAR2 == 'Patrick Fugit':
                    sta2 = '464'
                elif STAR2 == 'Laura Harring':
                    sta2 = '465'
                elif STAR2 == 'Julianne Moore':
                    sta2 = '466'
                elif STAR2 == 'Issey Takahashi':
                    sta2 = '467'
                elif STAR2 == 'Temuera Morrison':
                    sta2 = '468'
                elif STAR2 == 'Zbigniew Zamachowski':
                    sta2 = '469'
                elif STAR2 == 'Emi Shinohara':
                    sta2 = '470'
                elif STAR2 == 'Sean Penn':
                    sta2 = '471'
                elif STAR2 == 'Winona Ryder':
                    sta2 = '472'
                elif STAR2 == 'Brenda Fricker':
                    sta2 = '473'
                elif STAR2 == 'Woody Allen':
                    sta2 = '474'
                elif STAR2 == 'Dianne Wiest':
                    sta2 = '475'
                elif STAR2 == 'Kim Greist':
                    sta2 = '476'
                elif STAR2 == 'Michael McKean':
                    sta2 = '477'
                elif STAR2 == 'Melinda Dillon':
                    sta2 = '478'
                elif STAR2 == 'Dan Aykroyd':
                    sta2 = '479'
                elif STAR2 == 'Jessica Lange':
                    sta2 = '480'
                elif STAR2 == 'Ken Foree':
                    sta2 = '481'
                elif STAR2 == 'Horacio Salinas':
                    sta2 = '482'
                elif STAR2 == 'Bruno Zanin':
                    sta2 = '483'
                elif STAR2 == 'Delphine Seyrig':
                    sta2 = '484'
                elif STAR2 == 'Ruy Guerra':
                    sta2 = '485'
                elif STAR2 == 'Bud Cort':
                    sta2 = '486'
                elif STAR2 == 'Ernest Borgnine':
                    sta2 = '487'
                elif STAR2 == 'Judith O\'Dea':
                    sta2 = '488'
                elif STAR2 == 'Katharine Hepburn':
                    sta2 = '489'
                elif STAR2 == 'Rod Steiger':
                    sta2 = '490'
                elif STAR2 == 'Laurence Harvey':
                    sta2 = '491'
                elif STAR2 == 'Laurence Olivier':
                    sta2 = '492'
                elif STAR2 == 'Monica Vitti':
                    sta2 = '493'
                elif STAR2 == 'Eiji Okada':
                    sta2 = '494'
                elif STAR2 == 'Yul Brynner':
                    sta2 = '495'
                elif STAR2 == 'Jeffrey Hunter':
                    sta2 = '496'
                elif STAR2 == 'Raymond Massey':
                    sta2 = '497'
                elif STAR2 == 'Robert Walker':
                    sta2 = '498'
                elif STAR2 == 'Wallace Ford':
                    sta2 = '499'
                elif STAR2 == 'Maureen O\'Hara':
                    sta2 = '500'
                elif STAR2 == 'Lauren Bacall':
                    sta2 = '501'
                elif STAR2 == 'Jane Wyman':
                    sta2 = '502'
                elif STAR2 == 'Rosalind Russell':
                    sta2 = '503'
                elif STAR2 == 'Errol Flynn':
                    sta2 = '504'
                elif STAR2 == 'Groucho Marx':
                    sta2 = '505'
                elif STAR2 == 'Fay Wray':
                    sta2 = '506'
                elif STAR2 == 'Leila Hyams':
                    sta2 = '507'
                elif STAR2 == 'Alexander Granach':
                    sta2 = '508'
                elif STAR2 == 'Charlie Hunnam':
                    sta2 = '509'
                elif STAR2 == 'Vicky Kaushal':
                    sta2 = '510'
                elif STAR2 == 'Olivia Cooke':
                    sta2 = '511'
                elif STAR2 == 'Taraneh Alidoosti':
                    sta2 = '512'
                elif STAR2 == 'Barry Keoghan':
                    sta2 = '513'
                elif STAR2 == 'Anna Foglietta':
                    sta2 = '514'
                elif STAR2 == 'Octavia Spencer':
                    sta2 = '515'
                elif STAR2 == 'Hugh Grant':
                    sta2 = '516'
                elif STAR2 == 'Alia Bhatt':
                    sta2 = '517'
                elif STAR2 == 'Art Parkinson':
                    sta2 = '518'
                elif STAR2 == 'Kiara Advani':
                    sta2 = '519'
                elif STAR2 == 'Michelle Williams':
                    sta2 = '520'
                elif STAR2 == 'Louis Hofmann':
                    sta2 = '521'
                elif STAR2 == 'Diego Luna':
                    sta2 = '522'
                elif STAR2 == 'Kurt Russell':
                    sta2 = '523'
                elif STAR2 == 'Douglas Booth':
                    sta2 = '524'
                elif STAR2 == 'Imelda Staunton':
                    sta2 = '525'
                elif STAR2 == 'Tahar Rahim':
                    sta2 = '526'
                elif STAR2 == 'Carlo Verdone':
                    sta2 = '527'
                elif STAR2 == 'Yami Gautam':
                    sta2 = '528'
                elif STAR2 == 'Ryan Potter':
                    sta2 = '529'
                elif STAR2 == 'Rachel McAdams':
                    sta2 = '530'
                elif STAR2 == 'Adil Hussain':
                    sta2 = '531'
                elif STAR2 == 'Hidetoshi Nishijima':
                    sta2 = '532'
                elif STAR2 == 'Jim Sturgess':
                    sta2 = '533'
                elif STAR2 == 'Kara Hayward':
                    sta2 = '534'
                elif STAR2 == 'Cate Blanchett':
                    sta2 = '535'
                elif STAR2 == 'Steve Carell':
                    sta2 = '536'
                elif STAR2 == 'Yoshino Kimura':
                    sta2 = '537'
                elif STAR2 == 'Choi Min-sik':
                    sta2 = '538'
                elif STAR2 == 'Rooney Mara':
                    sta2 = '539'
                elif STAR2 == 'Barkhad Abdi':
                    sta2 = '540'
                elif STAR2 == 'Sae-ron Kim':
                    sta2 = '541'
                elif STAR2 == 'Corey Hawkins':
                    sta2 = '542'
                elif STAR2 == 'Martin Freeman':
                    sta2 = '543'
                elif STAR2 == 'Ernst Jacobi':
                    sta2 = '544'
                elif STAR2 == 'Noomi Rapace':
                    sta2 = '545'
                elif STAR2 == 'Alex Sharp':
                    sta2 = '546'
                elif STAR2 == 'Maggie Grace':
                    sta2 = '547'
                elif STAR2 == 'David Thewlis':
                    sta2 = '548'
                elif STAR2 == 'Markéta Irglová':
                    sta2 = '549'
                elif STAR2 == 'Nurgül Yesilçay':
                    sta2 = '550'
                elif STAR2 == 'James McAvoy':
                    sta2 = '551'
                elif STAR2 == 'Carey Mulligan':
                    sta2 = '552'
                elif STAR2 == 'Zoe Saldana':
                    sta2 = '553'
                elif STAR2 == 'Sarah Polley':
                    sta2 = '554'
                elif STAR2 == 'Raoul Max Trujillo':
                    sta2 = '555'
                elif STAR2 == 'Preity Zinta':
                    sta2 = '556'
                elif STAR2 == 'Mads Mikkelsen':
                    sta2 = '557'
                elif STAR2 == 'Matthew Macfadyen':
                    sta2 = '558'
                elif STAR2 == 'Diane Ladd':
                    sta2 = '559'
                elif STAR2 == 'Tôru Emori':
                    sta2 = '560'
                elif STAR2 == 'Gina Torres':
                    sta2 = '561'
                elif STAR2 == 'Reese Witherspoon':
                    sta2 = '562'
                elif STAR2 == 'Henrik Lundström':
                    sta2 = '563'
                elif STAR2 == 'Rodrigo De la Serna':
                    sta2 = '564'
                elif STAR2 == 'Artyom Bogucharskiy':
                    sta2 = '565'
                elif STAR2 == 'Jean-Claude Donda':
                    sta2 = '566'
                elif STAR2 == 'Lee Byung-Hun':
                    sta2 = '567'
                elif STAR2 == 'Guy Pearce':
                    sta2 = '568'
                elif STAR2 == 'Trevor Jack Brooks':
                    sta2 = '569'
                elif STAR2 == 'Will Patton':
                    sta2 = '570'
                elif STAR2 == 'Michelle Yeoh':
                    sta2 = '571'
                elif STAR2 == 'Marisa Paredes':
                    sta2 = '572'
                elif STAR2 == 'Helen Hunt':
                    sta2 = '573'
                elif STAR2 == 'Sean Patrick Flanery':
                    sta2 = '574'
                elif STAR2 == 'Chris Cooper':
                    sta2 = '575'
                elif STAR2 == 'Mike Myers':
                    sta2 = '576'
                elif STAR2 == 'Kayoko Kishimoto':
                    sta2 = '577'
                elif STAR2 == 'Deborah Kara Unger':
                    sta2 = '578'
                elif STAR2 == 'Stellan Skarsgård':
                    sta2 = '579'
                elif STAR2 == 'Martin Landau':
                    sta2 = '580'
                elif STAR2 == 'Leonardo DiCaprio':
                    sta2 = '581'
                elif STAR2 == 'Mike Vitar':
                    sta2 = '582'
                elif STAR2 == 'Emma Thompson':
                    sta2 = '583'
                elif STAR2 == 'Lesley Sharp':
                    sta2 = '584'
                elif STAR2 == 'Chazz Palminteri':
                    sta2 = '585'
                elif STAR2 == 'Frank Paur':
                    sta2 = '586'
                elif STAR2 == 'Gena Rowlands':
                    sta2 = '587'
                elif STAR2 == 'Wladyslaw Kowalski':
                    sta2 = '588'
                elif STAR2 == 'Laurence Fishburne':
                    sta2 = '589'
                elif STAR2 == 'Kathy Bates':
                    sta2 = '590'
                elif STAR2 == 'Robin Williams':
                    sta2 = '591'
                elif STAR2 == 'Minami Takayama':
                    sta2 = '592'
                elif STAR2 == 'Denzel Washington':
                    sta2 = '593'
                elif STAR2 == 'Danny Lee':
                    sta2 = '594'
                elif STAR2 == 'Willem Dafoe':
                    sta2 = '595'
                elif STAR2 == 'Carl Weathers':
                    sta2 = '596'
                elif STAR2 == 'Sarah Berry':
                    sta2 = '597'
                elif STAR2 == 'Alan Ruck':
                    sta2 = '598'
                elif STAR2 == 'John Lurie':
                    sta2 = '599'
                elif STAR2 == 'Josh Brolin':
                    sta2 = '600'
                elif STAR2 == 'Whoopi Goldberg':
                    sta2 = '601'
                elif STAR2 == 'Judd Nelson':
                    sta2 = '602'
                elif STAR2 == 'Haing S. Ngor':
                    sta2 = '603'
                elif STAR2 == 'Scott Glenn':
                    sta2 = '604'
                elif STAR2 == 'Jerry Lewis':
                    sta2 = '605'
                elif STAR2 == 'Drew Barrymore':
                    sta2 = '606'
                elif STAR2 == 'Brooke Adams':
                    sta2 = '607'
                elif STAR2 == 'Sondra Locke':
                    sta2 = '608'
                elif STAR2 == 'Jennifer Drake':
                    sta2 = '609'
                elif STAR2 == 'Terence Alexander':
                    sta2 = '610'
                elif STAR2 == 'Michael York':
                    sta2 = '611'
                elif STAR2 == 'Jack Albertson':
                    sta2 = '612'
                elif STAR2 == 'Jon Voight':
                    sta2 = '613'
                elif STAR2 == 'Alan Arkin':
                    sta2 = '614'
                elif STAR2 == 'Sidney Poitier':
                    sta2 = '615'
                elif STAR2 == 'Rex Harrison':
                    sta2 = '616'
                elif STAR2 == 'Dick Van Dyke':
                    sta2 = '617'
                elif STAR2 == 'Gerd Oswald':
                    sta2 = '618'
                elif STAR2 == 'Oskar Werner':
                    sta2 = '619'
                elif STAR2 == 'Peter Wyngarde':
                    sta2 = '620'
                elif STAR2 == 'Jean Seberg':
                    sta2 = '621'
                elif STAR2 == 'Edward G. Robinson':
                    sta2 = '622'
                elif STAR2 == 'Claire Trevor':
                    sta2 = '623'
                elif STAR2 == 'Michael Redgrave':
                    sta2 = '624'
                elif STAR2 == 'Cary Grant':
                    sta2 = '625'
                elif STAR2 == 'Elsa Lanchester':
                    sta2 = '626'
                elif STAR2 == 'Harpo Marx':
                    sta2 = '627'
                elif STAR2 == 'Paul Muni':
                    sta2 = '628'
                elif STAR2 == 'Mae Clarke':
                    sta2 = '629'
                elif STAR2 == 'Marina de Tavira':
                    sta2 = '630'
                elif STAR2 == 'Alec Secareanu':
                    sta2 = '631'
                elif STAR2 == 'Allison Williams':
                    sta2 = '632'
                elif STAR2 == 'Henry Cavill':
                    sta2 = '633'
                elif STAR2 == 'Bahar Pars':
                    sta2 = '634'
                elif STAR2 == 'Jemaine Clement':
                    sta2 = '635'
                elif STAR2 == 'Sara Takatsuki':
                    sta2 = '636'
                elif STAR2 == 'Felicity Jones':
                    sta2 = '637'
                elif STAR2 == 'Taron Egerton':
                    sta2 = '638'
                elif STAR2 == 'Ansel Elgort':
                    sta2 = '639'
                elif STAR2 == 'RJ Cyler':
                    sta2 = '640'
                elif STAR2 == 'Zach Galifianakis':
                    sta2 = '641'
                elif STAR2 == 'Adèle Exarchopoulos':
                    sta2 = '642'
                elif STAR2 == 'Sushant Singh Rajput':
                    sta2 = '643'
                elif STAR2 == 'Johan Heldenbergh':
                    sta2 = '644'
                elif STAR2 == 'Nargis Fakhri':
                    sta2 = '645'
                elif STAR2 == 'Will Forte':
                    sta2 = '646'
                elif STAR2 == 'Jack McBrayer':
                    sta2 = '647'
                elif STAR2 == 'Mackenzie Foy':
                    sta2 = '648'
                elif STAR2 == 'Christina Hendricks':
                    sta2 = '649'
                elif STAR2 == 'Chris Pratt':
                    sta2 = '650'
                elif STAR2 == 'George Clooney':
                    sta2 = '651'
                elif STAR2 == 'Emmanuel Affadzi':
                    sta2 = '652'
                elif STAR2 == 'Andrew Garfield':
                    sta2 = '653'
                elif STAR2 == 'Michael Fassbender':
                    sta2 = '654'
                elif STAR2 == 'Bradley Cooper':
                    sta2 = '655'
                elif STAR2 == 'Javier Bardem':
                    sta2 = '656'
                elif STAR2 == 'Jennifer Lawrence':
                    sta2 = '657'
                elif STAR2 == 'Bryan Cranston':
                    sta2 = '658'
                elif STAR2 == 'Michael Sheen':
                    sta2 = '659'
                elif STAR2 == 'Colm Feore':
                    sta2 = '660'
                elif STAR2 == 'Callan McAuliffe':
                    sta2 = '661'
                elif STAR2 == 'Takuya Ishida':
                    sta2 = '662'
                elif STAR2 == 'Ken\'ichi Matsuyama':
                    sta2 = '663'
                elif STAR2 == 'Stephen Graham':
                    sta2 = '664'
                elif STAR2 == 'Domhnall Gleeson':
                    sta2 = '665'
                elif STAR2 == 'Sidse Babett Knudsen':
                    sta2 = '666'
                elif STAR2 == 'Forest Whitaker':
                    sta2 = '667'
                elif STAR2 == 'Ben Kingsley':
                    sta2 = '668'
                elif STAR2 == 'Benno Fürmann':
                    sta2 = '669'
                elif STAR2 == 'Samantha Morton':
                    sta2 = '670'
                elif STAR2 == 'Mandy Moore':
                    sta2 = '671'
                elif STAR2 == 'Sebastian Koch':
                    sta2 = '672'
                elif STAR2 == 'Sandra Bullock':
                    sta2 = '673'
                elif STAR2 == 'Wah Yuen':
                    sta2 = '674'
                elif STAR2 == 'Franka Potente':
                    sta2 = '675'
                elif STAR2 == 'Jennifer Jason Leigh':
                    sta2 = '676'
                elif STAR2 == 'Regina King':
                    sta2 = '677'
                elif STAR2 == 'Teri Hatcher':
                    sta2 = '678'
                elif STAR2 == 'Ken Watanabe':
                    sta2 = '679'
                elif STAR2 == 'Dorothy Duffy':
                    sta2 = '680'
                elif STAR2 == 'Katrin Saß':
                    sta2 = '681'
                elif STAR2 == 'Ewan McGregor':
                    sta2 = '682'
                elif STAR2 == 'Tyler Hoechlin':
                    sta2 = '683'
                elif STAR2 == 'Christian Berkel':
                    sta2 = '684'
                elif STAR2 == 'Julie Walters':
                    sta2 = '685'
                elif STAR2 == 'Miriam Shor':
                    sta2 = '686'
                elif STAR2 == 'John Rafter Lee':
                    sta2 = '687'
                elif STAR2 == 'Matt Stone':
                    sta2 = '688'
                elif STAR2 == 'Jennifer Aniston':
                    sta2 = '689'
                elif STAR2 == 'Jon Lovitz':
                    sta2 = '690'
                elif STAR2 == 'Ethan Hawke':
                    sta2 = '691'
                elif STAR2 == 'Bill Murray':
                    sta2 = '692'
                elif STAR2 == 'Penélope Cruz':
                    sta2 = '693'
                elif STAR2 == 'Cameron Diaz':
                    sta2 = '694'
                elif STAR2 == 'Milla Jovovich':
                    sta2 = '695'
                elif STAR2 == 'Jacques Villeret':
                    sta2 = '696'
                elif STAR2 == 'Johnny Depp':
                    sta2 = '697'
                elif STAR2 == 'Armin Mueller-Stahl':
                    sta2 = '698'
                elif STAR2 == 'Laura Linney':
                    sta2 = '699'
                elif STAR2 == 'Eleanor Bron':
                    sta2 = '700'
                elif STAR2 == 'Michelle Reis':
                    sta2 = '701'
                elif STAR2 == 'Massimo Troisi':
                    sta2 = '702'
                elif STAR2 == 'Jeff Anderson':
                    sta2 = '703'
                elif STAR2 == 'Kermit the Frog':
                    sta2 = '704'
                elif STAR2 == 'Angela Bassett':
                    sta2 = '705'
                elif STAR2 == 'Tokiko Katô':
                    sta2 = '706'
                elif STAR2 == 'Jack Lemmon':
                    sta2 = '707'
                elif STAR2 == 'Jack Nicholson':
                    sta2 = '708'
                elif STAR2 == 'Jessica Tandy':
                    sta2 = '709'
                elif STAR2 == 'John Turturro':
                    sta2 = '710'
                elif STAR2 == 'Gene Bervoets':
                    sta2 = '711'
                elif STAR2 == 'Paul McGann':
                    sta2 = '712'
                elif STAR2 == 'Joan Chen':
                    sta2 = '713'
                elif STAR2 == 'John Malkovich':
                    sta2 = '714'
                elif STAR2 == 'Christian Slater':
                    sta2 = '715'
                elif STAR2 == 'Kyle MacLachlan':
                    sta2 = '716'
                elif STAR2 == 'Jeff Daniels':
                    sta2 = '717'
                elif STAR2 == 'Rosanna Arquette':
                    sta2 = '718'
                elif STAR2 == 'Mia Farrow':
                    sta2 = '719'
                elif STAR2 == 'Charlotte Rampling':
                    sta2 = '720'
                elif STAR2 == 'Leonard Nimoy':
                    sta2 = '721'
                elif STAR2 == 'Brian Dennehy':
                    sta2 = '722'
                elif STAR2 == 'Mary Tyler Moore':
                    sta2 = '723'
                elif STAR2 == 'Jerry Zucker':
                    sta2 = '724'
                elif STAR2 == 'Eiko Masuyama':
                    sta2 = '725'
                elif STAR2 == 'Jamie Lee Curtis':
                    sta2 = '726'
                elif STAR2 == 'Isabelle Adjani':
                    sta2 = '727'
                elif STAR2 == 'Gene Wilder':
                    sta2 = '728'
                elif STAR2 == 'John Randolph':
                    sta2 = '729'
                elif STAR2 == 'John Saxon':
                    sta2 = '730'
                elif STAR2 == 'Burt Reynolds':
                    sta2 = '731'
                elif STAR2 == 'Roy Scheider':
                    sta2 = '732'
                elif STAR2 == 'Andrew Robinson':
                    sta2 = '733'
                elif STAR2 == 'Walter Matthau':
                    sta2 = '734'
                elif STAR2 == 'Jean Sorel':
                    sta2 = '735'
                elif STAR2 == 'Wendy Hiller':
                    sta2 = '736'
                elif STAR2 == 'Ian Hendry':
                    sta2 = '737'
                elif STAR2 == 'Gert Fröbe':
                    sta2 = '738'
                elif STAR2 == 'Tippi Hedren':
                    sta2 = '739'
                elif STAR2 == 'Robert Mitchum':
                    sta2 = '740'
                elif STAR2 == 'Anna Massey':
                    sta2 = '741'
                elif STAR2 == 'Steve McQueen':
                    sta2 = '742'
                elif STAR2 == 'Alida Valli':
                    sta2 = '743'
                elif STAR2 == 'Dana Wynter':
                    sta2 = '744'
                elif STAR2 == 'Natalie Wood':
                    sta2 = '745'
                elif STAR2 == 'Peter Sellers':
                    sta2 = '746'
                elif STAR2 == 'Patricia Neal':
                    sta2 = '747'
                elif STAR2 == 'Glenn Ford':
                    sta2 = '748'
                elif STAR2 == 'Ford Beebe Jr.':
                    sta2 = '749'
                elif STAR2 == 'Gloria Stuart':
                    sta2 = '750'
                elif STAR2 == 'Debra Messing':
                    sta2 = '751'
                elif STAR2 == 'Aleksey Rozin':
                    sta2 = '752'
                elif STAR2 == 'Bria Vinaite':
                    sta2 = '753'
                elif STAR2 == 'Mckenna Grace':
                    sta2 = '754'
                elif STAR2 == 'Zack Gottsagen':
                    sta2 = '755'
                elif STAR2 == 'Frederick Lau':
                    sta2 = '756'
                elif STAR2 == 'Doga Zeynep Doguslu':
                    sta2 = '757'
                elif STAR2 == 'Jon Bernthal':
                    sta2 = '758'
                elif STAR2 == 'Miles Teller':
                    sta2 = '759'
                elif STAR2 == 'Mark Rylance':
                    sta2 = '760'
                elif STAR2 == 'Holly Hunter':
                    sta2 = '761'
                elif STAR2 == 'Don Hall':
                    sta2 = '762'
                elif STAR2 == 'Sylvester Stallone':
                    sta2 = '763'
                elif STAR2 == 'Elena Lyadova':
                    sta2 = '764'
                elif STAR2 == 'Ben Foster':
                    sta2 = '765'
                elif STAR2 == 'Steve Coogan':
                    sta2 = '766'
                elif STAR2 == 'Keri Russell':
                    sta2 = '767'
                elif STAR2 == 'Hugo Silva':
                    sta2 = '768'
                elif STAR2 == 'Ananda George':
                    sta2 = '769'
                elif STAR2 == 'Michael Peña':
                    sta2 = '770'
                elif STAR2 == 'Mirai Shida':
                    sta2 = '771'
                elif STAR2 == 'Trine Dyrholm':
                    sta2 = '772'
                elif STAR2 == 'Seth Rogen':
                    sta2 = '773'
                elif STAR2 == 'Nicolas Cage':
                    sta2 = '774'
                elif STAR2 == 'Alberto Ammann':
                    sta2 = '775'
                elif STAR2 == 'Elena Anaya':
                    sta2 = '776'
                elif STAR2 == 'Jude Law':
                    sta2 = '777'
                elif STAR2 == 'Haaz Sleiman':
                    sta2 = '778'
                elif STAR2 == 'Rosario Dawson':
                    sta2 = '779'
                elif STAR2 == 'Claire Danes':
                    sta2 = '780'
                elif STAR2 == 'Evan McGuire':
                    sta2 = '781'
                elif STAR2 == 'Sylvie Testud':
                    sta2 = '782'
                elif STAR2 == 'Li Sun':
                    sta2 = '783'
                elif STAR2 == 'Jessica Biel':
                    sta2 = '784'
                elif STAR2 == 'Gary Stretch':
                    sta2 = '785'
                elif STAR2 == 'Lena Headey':
                    sta2 = '786'
                elif STAR2 == 'Jonathan Rhys Meyers':
                    sta2 = '787'
                elif STAR2 == 'Patrick Wilson':
                    sta2 = '788'
                elif STAR2 == 'Leigh Whannell':
                    sta2 = '789'
                elif STAR2 == 'Marion Cotillard':
                    sta2 = '790'
                elif STAR2 == 'Gaspard Ulliel':
                    sta2 = '791'
                elif STAR2 == 'Patricia Clarkson':
                    sta2 = '792'
                elif STAR2 == 'Benicio Del Toro':
                    sta2 = '793'
                elif STAR2 == 'Shin Ha-kyun':
                    sta2 = '794'
                elif STAR2 == 'Barry Pepper':
                    sta2 = '795'
                elif STAR2 == 'Ashton Kutcher':
                    sta2 = '796'
                elif STAR2 == 'Naomie Harris':
                    sta2 = '797'
                elif STAR2 == 'Aki Maeda':
                    sta2 = '798'
                elif STAR2 == 'Rupert Grint':
                    sta2 = '799'
                elif STAR2 == 'Christopher Eccleston':
                    sta2 = '800'
                elif STAR2 == 'Colin Farrell':
                    sta2 = '801'
                elif STAR2 == 'Vicellous Shannon':
                    sta2 = '802'
                elif STAR2 == 'Justin Theroux':
                    sta2 = '803'
                elif STAR2 == 'Moritz Bleibtreu':
                    sta2 = '804'
                elif STAR2 == 'Ming-Na Wen':
                    sta2 = '805'
                elif STAR2 == 'Ulrich Mühe':
                    sta2 = '806'
                elif STAR2 == 'Kiefer Sutherland':
                    sta2 = '807'
                elif STAR2 == 'Kevin Bacon':
                    sta2 = '808'
                elif STAR2 == 'Jeremy Irons':
                    sta2 = '809'
                elif STAR2 == 'Gary Farmer':
                    sta2 = '810'
                elif STAR2 == 'Robert Duvall':
                    sta2 = '811'
                elif STAR2 == 'Wiley Wiggins':
                    sta2 = '812'
                elif STAR2 == 'Toshirô Yanagiba':
                    sta2 = '813'
                elif STAR2 == 'Marie-Laure Dougnac':
                    sta2 = '814'
                elif STAR2 == 'Joe Pesci':
                    sta2 = '815'
                elif STAR2 == 'Meg Ryan':
                    sta2 = '816'
                elif STAR2 == 'Jodi Benson':
                    sta2 = '817'
                elif STAR2 == 'Priscilla Presley':
                    sta2 = '818'
                elif STAR2 == 'John Candy':
                    sta2 = '819'
                elif STAR2 == 'Danny Glover':
                    sta2 = '820'
                elif STAR2 == 'John Getz':
                    sta2 = '821'
                elif STAR2 == 'Henry Fonda':
                    sta2 = '822'
                elif STAR2 == 'Bruce Spence':
                    sta2 = '823'
                elif STAR2 == 'James Remar':
                    sta2 = '824'
                elif STAR2 == 'Frank Oz':
                    sta2 = '825'
                elif STAR2 == 'Patrick McGoohan':
                    sta2 = '826'
                elif STAR2 == 'Irene Miracle':
                    sta2 = '827'
                elif STAR2 == 'François Truffaut':
                    sta2 = '828'
                elif STAR2 == 'Nina van Pallandt':
                    sta2 = '829'
                elif STAR2 == 'James Coburn':
                    sta2 = '830'
                elif STAR2 == 'Telly Savalas':
                    sta2 = '831'
                elif STAR2 == 'Sebastian Cabot':
                    sta2 = '832'
                elif STAR2 == 'Vanessa Redgrave':
                    sta2 = '833'
                elif STAR2 == 'Paul McCartney':
                    sta2 = '834'
                elif STAR2 == 'George Peppard':
                    sta2 = '835'
                elif STAR2 == 'Rock Hudson':
                    sta2 = '836'
                elif STAR2 == 'Montgomery Clift':
                    sta2 = '837'
                elif STAR2 == 'John Hodiak':
                    sta2 = '838'
                elif STAR2 == 'Madeleine Carroll':
                    sta2 = '839'
                
                STAR3 = request.form['star3']
                if STAR3 == 'Bob Gunton':
                    sta3 = '0'
                elif STAR3 == 'James Caan':
                    sta3 = '1'
                elif STAR3 == 'Aaron Eckhart':
                    sta3 = '2'
                elif STAR3 == 'Robert Duvall':
                    sta3 = '3'
                elif STAR3 == 'Martin Balsam':
                    sta3 = '4'
                elif STAR3 == 'Ian McKellen':
                    sta3 = '5'
                elif STAR3 == 'Samuel L. Jackson':
                    sta3 = '6'
                elif STAR3 == 'Ben Kingsley':
                    sta3 = '7'
                elif STAR3 == 'Elliot Page':
                    sta3 = '8'
                elif STAR3 == 'Meat Loaf':
                    sta3 = '9'
                elif STAR3 == 'Orlando Bloom':
                    sta3 = '10'
                elif STAR3 == 'Gary Sinise':
                    sta3 = '11'
                elif STAR3 == 'Lee Van Cleef':
                    sta3 = '12'
                elif STAR3 == 'Viggo Mortensen':
                    sta3 = '13'
                elif STAR3 == 'Laurence Fishburne':
                    sta3 = '14'
                elif STAR3 == 'Joe Pesci':
                    sta3 = '15'
                elif STAR3 == 'Carrie Fisher':
                    sta3 = '16'
                elif STAR3 == 'Michael Berryman':
                    sta3 = '17'
                elif STAR3 == 'Leslie Odom Jr.':
                    sta3 = '18'
                elif STAR3 == 'Cho Yeo-jeong':
                    sta3 = '19'
                elif STAR3 == 'Paresh Rawal':
                    sta3 = '20'
                elif STAR3 == 'Jessica Chastain':
                    sta3 = '21'
                elif STAR3 == 'Leandro Firmino':
                    sta3 = '22'
                elif STAR3 == 'Miyu Irino':
                    sta3 = '23'
                elif STAR3 == 'Tom Sizemore':
                    sta3 = '24'
                elif STAR3 == 'David Morse':
                    sta3 = '25'
                elif STAR3 == 'Giorgio Cantarini':
                    sta3 = '26'
                elif STAR3 == 'Kevin Spacey':
                    sta3 = '27'
                elif STAR3 == 'Lawrence A. Bonney':
                    sta3 = '28'
                elif STAR3 == 'Shima Iwashita':
                    sta3 = '29'
                elif STAR3 == 'Keiko Tsushima':
                    sta3 = '30'
                elif STAR3 == 'Lionel Barrymore':
                    sta3 = '31'
                elif STAR3 == 'Zazie Beetz':
                    sta3 = '32'
                elif STAR3 == 'Melissa Benoist':
                    sta3 = '33'
                elif STAR3 == 'Omar Sy':
                    sta3 = '34'
                elif STAR3 == 'Scarlett Johansson':
                    sta3 = '35'
                elif STAR3 == 'Jack Nicholson':
                    sta3 = '36'
                elif STAR3 == 'Frank Finlay':
                    sta3 = '37'
                elif STAR3 == 'Connie Nielsen':
                    sta3 = '38'
                elif STAR3 == 'Beverly D\'Angelo':
                    sta3 = '39'
                elif STAR3 == 'Chazz Palminteri':
                    sta3 = '40'
                elif STAR3 == 'Natalie Portman':
                    sta3 = '41'
                elif STAR3 == 'Jeremy Irons':
                    sta3 = '42'
                elif STAR3 == 'Edward Furlong':
                    sta3 = '43'
                elif STAR3 == 'Antonella Attili':
                    sta3 = '44'
                elif STAR3 == 'Akemi Yamaguchi':
                    sta3 = '45'
                elif STAR3 == 'Lea Thompson':
                    sta3 = '46'
                elif STAR3 == 'Claudia Cardinale':
                    sta3 = '47'
                elif STAR3 == 'Vera Miles':
                    sta3 = '48'
                elif STAR3 == 'Paul Henreid':
                    sta3 = '49'
                elif STAR3 == 'Henry Bergman':
                    sta3 = '50'
                elif STAR3 == 'Florence Lee':
                    sta3 = '51'
                elif STAR3 == 'Boluwatife Treasure Bankole':
                    sta3 = '52'
                elif STAR3 == 'Ismail Hacioglu':
                    sta3 = '53'
                elif STAR3 == 'Vijay Sethupathi':
                    sta3 = '54'
                elif STAR3 == 'Ryô Narita':
                    sta3 = '55'
                elif STAR3 == 'Fatima Sana Shaikh':
                    sta3 = '56'
                elif STAR3 == 'Shameik Moore':
                    sta3 = '57'
                elif STAR3 == 'Chris Evans':
                    sta3 = '58'
                elif STAR3 == 'Chris Hemsworth':
                    sta3 = '59'
                elif STAR3 == 'Gael García Bernal':
                    sta3 = '60'
                elif STAR3 == 'Leonardo DiCaprio':
                    sta3 = '61'
                elif STAR3 == 'Anne Hathaway':
                    sta3 = '62'
                elif STAR3 == 'Mona Singh':
                    sta3 = '63'
                elif STAR3 == 'Aamir Khan':
                    sta3 = '64'
                elif STAR3 == 'Jeff Garlin':
                    sta3 = '65'
                elif STAR3 == 'Sebastian Koch':
                    sta3 = '66'
                elif STAR3 == 'Kang Hye-jeong':
                    sta3 = '67'
                elif STAR3 == 'Joe Pantoliano':
                    sta3 = '68'
                elif STAR3 == 'Yûko Tanaka':
                    sta3 = '69'
                elif STAR3 == 'Elizabeth McGovern':
                    sta3 = '70'
                elif STAR3 == 'Paul Freeman':
                    sta3 = '71'
                elif STAR3 == 'Danny Lloyd':
                    sta3 = '72'
                elif STAR3 == 'John Hurt':
                    sta3 = '73'
                elif STAR3 == 'Sumita Sanyal':
                    sta3 = '74'
                elif STAR3 == 'Tatsuya Nakadai':
                    sta3 = '75'
                elif STAR3 == 'Sterling Hayden':
                    sta3 = '76'
                elif STAR3 == 'Charles Laughton':
                    sta3 = '77'
                elif STAR3 == 'Adolphe Menjou':
                    sta3 = '78'
                elif STAR3 == 'Wendell Corey':
                    sta3 = '79'
                elif STAR3 == 'Erich von Stroheim':
                    sta3 = '80'
                elif STAR3 == 'Jack Oakie':
                    sta3 = '81'
                elif STAR3 == 'Daniel Mays':
                    sta3 = '82'
                elif STAR3 == 'Sohum Shah':
                    sta3 = '83'
                elif STAR3 == 'Radhika Apte':
                    sta3 = '84'
                elif STAR3 == 'Asha Sharath':
                    sta3 = '85'
                elif STAR3 == 'Annika Wedderkopp':
                    sta3 = '86'
                elif STAR3 == 'Sareh Bayat':
                    sta3 = '87'
                elif STAR3 == 'Maxim Gaudette':
                    sta3 = '88'
                elif STAR3 == 'Deniz Baysal':
                    sta3 = '89'
                elif STAR3 == 'Hümeyra':
                    sta3 = '90'
                elif STAR3 == 'Eli Roth':
                    sta3 = '91'
                elif STAR3 == 'Tom Wilkinson':
                    sta3 = '92'
                elif STAR3 == 'Rufus':
                    sta3 = '93'
                elif STAR3 == 'Benicio Del Toro':
                    sta3 = '94'
                elif STAR3 == 'Jennifer Connelly':
                    sta3 = '95'
                elif STAR3 == 'Thora Birch':
                    sta3 = '96'
                elif STAR3 == 'Ben Affleck':
                    sta3 = '97'
                elif STAR3 == 'Bahare Seddiqi':
                    sta3 = '98'
                elif STAR3 == 'Don Rickles':
                    sta3 = '99'
                elif STAR3 == 'Patrick McGoohan':
                    sta3 = '100'
                elif STAR3 == 'Michael Madsen':
                    sta3 = '101'
                elif STAR3 == 'Vincent D\'Onofrio':
                    sta3 = '102'
                elif STAR3 == 'Liubomiras Laucevicius':
                    sta3 = '103'
                elif STAR3 == 'Carrie Henn':
                    sta3 = '104'
                elif STAR3 == 'Elizabeth Berridge':
                    sta3 = '105'
                elif STAR3 == 'Steven Bauer':
                    sta3 = '106'
                elif STAR3 == 'Klaus Wennemann':
                    sta3 = '107'
                elif STAR3 == 'Cybill Shepherd':
                    sta3 = '108'
                elif STAR3 == 'Robert Shaw':
                    sta3 = '109'
                elif STAR3 == 'Michael Bates':
                    sta3 = '110'
                elif STAR3 == 'William Sylvester':
                    sta3 = '111'
                elif STAR3 == 'Gian Maria Volontè':
                    sta3 = '112'
                elif STAR3 == 'Anthony Quinn':
                    sta3 = '113'
                elif STAR3 == 'Fred MacMurray':
                    sta3 = '114'
                elif STAR3 == 'James Mason':
                    sta3 = '115'
                elif STAR3 == 'Barbara Bel Geddes':
                    sta3 = '116'
                elif STAR3 == 'Donald O\'Connor':
                    sta3 = '117'
                elif STAR3 == 'Shin\'ichi Himori':
                    sta3 = '118'
                elif STAR3 == 'Lianella Carell':
                    sta3 = '119'
                elif STAR3 == 'Edward G. Robinson':
                    sta3 = '120'
                elif STAR3 == 'Dorothy Comingore':
                    sta3 = '121'
                elif STAR3 == 'Inge Landgut':
                    sta3 = '122'
                elif STAR3 == 'Gustav Fröhlich':
                    sta3 = '123'
                elif STAR3 == 'Jackie Coogan':
                    sta3 = '124'
                elif STAR3 == 'Varun Sharma':
                    sta3 = '125'
                elif STAR3 == 'Mohit Raina':
                    sta3 = '126'
                elif STAR3 == 'Ramachandra Raju':
                    sta3 = '127'
                elif STAR3 == 'Linda Cardellini':
                    sta3 = '128'
                elif STAR3 == 'Sam Rockwell':
                    sta3 = '129'
                elif STAR3 == 'Neeraj Kabi':
                    sta3 = '130'
                elif STAR3 == 'Anushka Shetty':
                    sta3 = '131'
                elif STAR3 == 'J.K. Simmons':
                    sta3 = '132'
                elif STAR3 == 'Tabu':
                    sta3 = '133'
                elif STAR3 == 'Lisa Haydon':
                    sta3 = '134'
                elif STAR3 == 'Giorgi Nakashidze':
                    sta3 = '135'
                elif STAR3 == 'Pawan Malhotra':
                    sta3 = '136'
                elif STAR3 == 'Nawazuddin Siddiqui':
                    sta3 = '137'
                elif STAR3 == 'Manjot Singh':
                    sta3 = '138'
                elif STAR3 == 'Rajesh Abhay':
                    sta3 = '139'
                elif STAR3 == 'Pablo Rago':
                    sta3 = '140'
                elif STAR3 == 'Joel Edgerton':
                    sta3 = '141'
                elif STAR3 == 'Mark Ruffalo':
                    sta3 = '142'
                elif STAR3 == 'Jordan Nagai':
                    sta3 = '143'
                elif STAR3 == 'Margot Robbie':
                    sta3 = '144'
                elif STAR3 == 'Sagarika Ghatge':
                    sta3 = '145'
                elif STAR3 == 'Ciarán Hinds':
                    sta3 = '146'
                elif STAR3 == 'Sergi López':
                    sta3 = '147'
                elif STAR3 == 'Joan Cusack':
                    sta3 = '148'
                elif STAR3 == 'Rupert Graves':
                    sta3 = '149'
                elif STAR3 == 'Siddharth':
                    sta3 = '150'
                elif STAR3 == 'Shernaz Patel':
                    sta3 = '151'
                elif STAR3 == 'Ken Watanabe':
                    sta3 = '152'
                elif STAR3 == 'Kishori Ballal':
                    sta3 = '153'
                elif STAR3 == 'Ulrich Matthes':
                    sta3 = '154'
                elif STAR3 == 'Tatsuya Gashûin':
                    sta3 = '155'
                elif STAR3 == 'Nick Moran':
                    sta3 = '156'
                elif STAR3 == 'Guy Pearce':
                    sta3 = '157'
                elif STAR3 == 'Sermin Hürmeriç':
                    sta3 = '158'
                elif STAR3 == 'Val Kilmer':
                    sta3 = '159'
                elif STAR3 == 'Raveena Tandon':
                    sta3 = '160'
                elif STAR3 == 'Morgan Freeman':
                    sta3 = '161'
                elif STAR3 == 'Alison Doody':
                    sta3 = '162'
                elif STAR3 == 'Ljubica Adzovic':
                    sta3 = '163'
                elif STAR3 == 'Chika Sakamoto':
                    sta3 = '164'
                elif STAR3 == 'Bonnie Bedelia':
                    sta3 = '165'
                elif STAR3 == 'Jinpachi Nezu':
                    sta3 = '166'
                elif STAR3 == 'Anatoliy Solonitsyn':
                    sta3 = '167'
                elif STAR3 == 'Lena Nyman':
                    sta3 = '168'
                elif STAR3 == 'Michael Ansara':
                    sta3 = '169'
                elif STAR3 == 'Amitabh Bachchan':
                    sta3 = '170'
                elif STAR3 == 'John Cleese':
                    sta3 = '171'
                elif STAR3 == 'Richard Attenborough':
                    sta3 = '172'
                elif STAR3 == 'Frank Overton':
                    sta3 = '173'
                elif STAR3 == 'Richard Widmark':
                    sta3 = '174'
                elif STAR3 == 'Jack Lemmon':
                    sta3 = '175'
                elif STAR3 == 'Ingrid Thulin':
                    sta3 = '176'
                elif STAR3 == 'Bengt Ekerot':
                    sta3 = '177'
                elif STAR3 == 'Robert Manuel':
                    sta3 = '178'
                elif STAR3 == 'Robert Cummings':
                    sta3 = '179'
                elif STAR3 == 'Sô Yamamura':
                    sta3 = '180'
                elif STAR3 == 'Masayuki Mori':
                    sta3 = '181'
                elif STAR3 == 'George Sanders':
                    sta3 = '182'
                elif STAR3 == 'Tim Holt':
                    sta3 = '183'
                elif STAR3 == 'Robert Stack':
                    sta3 = '184'
                elif STAR3 == 'Tom Murray':
                    sta3 = '185'
                elif STAR3 == 'Joe Keaton':
                    sta3 = '186'
                elif STAR3 == 'Luàna Bajrami':
                    sta3 = '187'
                elif STAR3 == 'Kirti Kulhari':
                    sta3 = '188'
                elif STAR3 == 'Aoi Yûki':
                    sta3 = '189'
                elif STAR3 == 'Jose Coronado':
                    sta3 = '190'
                elif STAR3 == 'Cho Jin-woong':
                    sta3 = '191'
                elif STAR3 == 'Suzanne Clément':
                    sta3 = '192'
                elif STAR3 == 'Shraddha Kapoor':
                    sta3 = '193'
                elif STAR3 == 'Dafne Keen':
                    sta3 = '194'
                elif STAR3 == 'Sean Bridgers':
                    sta3 = '195'
                elif STAR3 == 'Mónica Villa':
                    sta3 = '196'
                elif STAR3 == 'Tina Fey':
                    sta3 = '197'
                elif STAR3 == 'Demet Akbag':
                    sta3 = '198'
                elif STAR3 == 'Sanjay Dutt':
                    sta3 = '199'
                elif STAR3 == 'Mithun Chakraborty':
                    sta3 = '200'
                elif STAR3 == 'Mathieu Amalric':
                    sta3 = '201'
                elif STAR3 == 'Neil Patrick Harris':
                    sta3 = '202'
                elif STAR3 == 'Haru Kuroki':
                    sta3 = '203'
                elif STAR3 == 'Luke Bracey':
                    sta3 = '204'
                elif STAR3 == 'Bill Hader':
                    sta3 = '205'
                elif STAR3 == 'Ileana D\'Cruz':
                    sta3 = '206'
                elif STAR3 == 'Michael Fassbender':
                    sta3 = '207'
                elif STAR3 == 'Olivia Wilde':
                    sta3 = '208'
                elif STAR3 == 'Jon Bernthal':
                    sta3 = '209'
                elif STAR3 == 'Rachel McAdams':
                    sta3 = '210'
                elif STAR3 == 'Lisa Hannigan':
                    sta3 = '211'
                elif STAR3 == 'Indraneil Sengupta':
                    sta3 = '212'
                elif STAR3 == 'Abhay Deol':
                    sta3 = '213'
                elif STAR3 == 'Viola Davis':
                    sta3 = '214'
                elif STAR3 == 'Nicholas Hoult':
                    sta3 = '215'
                elif STAR3 == 'Jimmy Sheirgill':
                    sta3 = '216'
                elif STAR3 == 'Christopher Carley':
                    sta3 = '217'
                elif STAR3 == 'Rupert Grint':
                    sta3 = '218'
                elif STAR3 == 'Tsutomu Yamazaki':
                    sta3 = '219'
                elif STAR3 == 'Cary-Hiroyuki Tagawa':
                    sta3 = '220'
                elif STAR3 == 'Eric Bana':
                    sta3 = '221'
                elif STAR3 == 'Gerard Butler':
                    sta3 = '222'
                elif STAR3 == 'Catherine Keener':
                    sta3 = '223'
                elif STAR3 == 'Javier Bardem':
                    sta3 = '224'
                elif STAR3 == 'Vidya Balan':
                    sta3 = '225'
                elif STAR3 == 'Joaquin Phoenix':
                    sta3 = '226'
                elif STAR3 == 'Eun-ju Lee':
                    sta3 = '227'
                elif STAR3 == 'Vernon Dobtcheff':
                    sta3 = '228'
                elif STAR3 == 'Gracy Singh':
                    sta3 = '229'
                elif STAR3 == 'Roe-ha Kim':
                    sta3 = '230'
                elif STAR3 == 'Akshaye Khanna':
                    sta3 = '231'
                elif STAR3 == 'Daryl Hannah':
                    sta3 = '232'
                elif STAR3 == 'Ellen DeGeneres':
                    sta3 = '233'
                elif STAR3 == 'Christopher Walken':
                    sta3 = '234'
                elif STAR3 == 'Goya Toledo':
                    sta3 = '235'
                elif STAR3 == 'Billy Crystal':
                    sta3 = '236'
                elif STAR3 == 'Megumi Hayashibara':
                    sta3 = '237'
                elif STAR3 == 'Toni Collette':
                    sta3 = '238'
                elif STAR3 == 'Mélanie Thierry':
                    sta3 = '239'
                elif STAR3 == 'Laura Linney':
                    sta3 = '240'
                elif STAR3 == 'Branka Katic':
                    sta3 = '241'
                elif STAR3 == 'John Goodman':
                    sta3 = '242'
                elif STAR3 == 'Ping Lam Siu':
                    sta3 = '243'
                elif STAR3 == 'Jonny Lee Miller':
                    sta3 = '244'
                elif STAR3 == 'Frances McDormand':
                    sta3 = '245'
                elif STAR3 == 'Mirjana Jokovic':
                    sta3 = '246'
                elif STAR3 == 'Saïd Taghmaoui':
                    sta3 = '247'
                elif STAR3 == 'Amrish Puri':
                    sta3 = '248'
                elif STAR3 == 'Andrea Eckert':
                    sta3 = '249'
                elif STAR3 == 'Frédérique Feder':
                    sta3 = '250'
                elif STAR3 == 'Tony Chiu-Wai Leung':
                    sta3 = '251'
                elif STAR3 == 'Jeff Goldblum':
                    sta3 = '252'
                elif STAR3 == 'Alison Crosbie':
                    sta3 = '253'
                elif STAR3 == 'Gong Li':
                    sta3 = '254'
                elif STAR3 == 'Saifei He':
                    sta3 = '255'
                elif STAR3 == 'Ethan Hawke':
                    sta3 = '256'
                elif STAR3 == 'Corey Feldman':
                    sta3 = '257'
                elif STAR3 == 'Willem Dafoe':
                    sta3 = '258'
                elif STAR3 == 'Dean Stockwell':
                    sta3 = '259'
                elif STAR3 == 'Hisako Kyôda':
                    sta3 = '260'
                elif STAR3 == 'Keith David':
                    sta3 = '261'
                elif STAR3 == 'James Laurenson':
                    sta3 = '262'
                elif STAR3 == 'José Lewgoy':
                    sta3 = '263'
                elif STAR3 == 'Kristina Adolphson':
                    sta3 = '264'
                elif STAR3 == 'Sean Young':
                    sta3 = '265'
                elif STAR3 == 'Anne Bancroft':
                    sta3 = '266'
                elif STAR3 == 'Michael Palin':
                    sta3 = '267'
                elif STAR3 == 'John Cazale':
                    sta3 = '268'
                elif STAR3 == 'Burt Young':
                    sta3 = '269'
                elif STAR3 == 'Peter Finch':
                    sta3 = '270'
                elif STAR3 == 'Patrick Magee':
                    sta3 = '271'
                elif STAR3 == 'Ignat Daniltsev':
                    sta3 = '272'
                elif STAR3 == 'John Huston':
                    sta3 = '273'
                elif STAR3 == 'Madeline Kahn':
                    sta3 = '274'
                elif STAR3 == 'Kari Sylwan':
                    sta3 = '275'
                elif STAR3 == 'Jüri Järvet':
                    sta3 = '276'
                elif STAR3 == 'Nathalie Delon':
                    sta3 = '277'
                elif STAR3 == 'Strother Martin':
                    sta3 = '278'
                elif STAR3 == 'Margaretha Krook':
                    sta3 = '279'
                elif STAR3 == 'Nikolay Grinko':
                    sta3 = '280'
                elif STAR3 == 'Yacef Saadi':
                    sta3 = '281'
                elif STAR3 == 'Enrique Rambal':
                    sta3 = '282'
                elif STAR3 == 'Victor Buono':
                    sta3 = '283'
                elif STAR3 == 'Keiju Kobayashi':
                    sta3 = '284'
                elif STAR3 == 'Valentin Zubkov':
                    sta3 = '285'
                elif STAR3 == 'Gunnel Lindblom':
                    sta3 = '286'
                elif STAR3 == 'Gene Kelly':
                    sta3 = '287'
                elif STAR3 == 'Claire Maurier':
                    sta3 = '288'
                elif STAR3 == 'Stephen Boyd':
                    sta3 = '289'
                elif STAR3 == 'Minoru Chiaki':
                    sta3 = '290'
                elif STAR3 == 'Franca Marzi':
                    sta3 = '291'
                elif STAR3 == 'Isuzu Yamada':
                    sta3 = '292'
                elif STAR3 == 'Jack Hawkins':
                    sta3 = '293'
                elif STAR3 == 'Lee J. Cobb':
                    sta3 = '294'
                elif STAR3 == 'Peter van Eyck':
                    sta3 = '295'
                elif STAR3 == 'Robert Arthur':
                    sta3 = '296'
                elif STAR3 == 'Edmond O\'Brien':
                    sta3 = '297'
                elif STAR3 == 'Alida Valli':
                    sta3 = '298'
                elif STAR3 == 'Marius Goring':
                    sta3 = '299'
                elif STAR3 == 'Frank Morgan':
                    sta3 = '300'
                elif STAR3 == 'Claude Rains':
                    sta3 = '301'
                elif STAR3 == 'Clark Gable':
                    sta3 = '302'
                elif STAR3 == 'Pierre Fresnay':
                    sta3 = '303'
                elif STAR3 == 'Walter Connolly':
                    sta3 = '304'
                elif STAR3 == 'André Berley':
                    sta3 = '305'
                elif STAR3 == 'Al Ernest Garcia':
                    sta3 = '306'
                elif STAR3 == 'Margaret Livingston':
                    sta3 = '307'
                elif STAR3 == 'Marion Mack':
                    sta3 = '308'
                elif STAR3 == 'Friedrich Feher':
                    sta3 = '309'
                elif STAR3 == 'Gajraj Rao':
                    sta3 = '310'
                elif STAR3 == 'Christopher Heyerdahl':
                    sta3 = '311'
                elif STAR3 == 'Kumud Mishra':
                    sta3 = '312'
                elif STAR3 == 'Rana Daggubati':
                    sta3 = '313'
                elif STAR3 == 'Rosemarie DeWitt':
                    sta3 = '314'
                elif STAR3 == 'Rooney Mara':
                    sta3 = '315'
                elif STAR3 == 'Kristen Wiig':
                    sta3 = '316'
                elif STAR3 == 'Ginnifer Goodwin':
                    sta3 = '317'
                elif STAR3 == 'Ramya Krishnan':
                    sta3 = '318'
                elif STAR3 == 'Mary Steenburgen':
                    sta3 = '319'
                elif STAR3 == 'Izabela Vidovic':
                    sta3 = '320'
                elif STAR3 == 'Ranveer Singh':
                    sta3 = '321'
                elif STAR3 == 'Manoj Bajpayee':
                    sta3 = '322'
                elif STAR3 == 'John Gallagher Jr.':
                    sta3 = '323'
                elif STAR3 == 'Arifin Putra':
                    sta3 = '324'
                elif STAR3 == 'Matthew Goode':
                    sta3 = '325'
                elif STAR3 == 'Bradley Cooper':
                    sta3 = '326'
                elif STAR3 == 'Ana de Armas':
                    sta3 = '327'
                elif STAR3 == 'Gwilym Lee':
                    sta3 = '328'
                elif STAR3 == 'Will Poulter':
                    sta3 = '329'
                elif STAR3 == 'Ezra Miller':
                    sta3 = '330'
                elif STAR3 == 'André Ramiro':
                    sta3 = '331'
                elif STAR3 == 'Helena Bonham Carter':
                    sta3 = '332'
                elif STAR3 == 'Octavia Spencer':
                    sta3 = '333'
                elif STAR3 == 'T.J. Miller':
                    sta3 = '334'
                elif STAR3 == 'Taraneh Alidoosti':
                    sta3 = '335'
                elif STAR3 == 'Kalki Koechlin':
                    sta3 = '336'
                elif STAR3 == 'Siu-Wong Fan':
                    sta3 = '337'
                elif STAR3 == 'Sheetal Menon':
                    sta3 = '338'
                elif STAR3 == 'Ilker Kizmaz':
                    sta3 = '339'
                elif STAR3 == 'Freida Pinto':
                    sta3 = '340'
                elif STAR3 == 'Vincent Cassel':
                    sta3 = '341'
                elif STAR3 == 'Caio Junqueira':
                    sta3 = '342'
                elif STAR3 == 'Catherine Deneuve':
                    sta3 = '343'
                elif STAR3 == 'Jared Leto':
                    sta3 = '344'
                elif STAR3 == 'Jaden Smith':
                    sta3 = '345'
                elif STAR3 == 'Joan Allen':
                    sta3 = '346'
                elif STAR3 == 'Hyuk-ho Kwon':
                    sta3 = '347'
                elif STAR3 == 'Mickey Rourke':
                    sta3 = '348'
                elif STAR3 == 'Emmanuelle Seigner':
                    sta3 = '349'
                elif STAR3 == 'Ozan Güven':
                    sta3 = '350'
                elif STAR3 == 'Lou Romano':
                    sta3 = '351'
                elif STAR3 == 'Judi Dench':
                    sta3 = '352'
                elif STAR3 == 'Konstantin Lavronenko':
                    sta3 = '353'
                elif STAR3 == 'Jong-ho Kim':
                    sta3 = '354'
                elif STAR3 == 'Lola Dueñas':
                    sta3 = '355'
                elif STAR3 == 'Craig Bierko':
                    sta3 = '356'
                elif STAR3 == 'Saif Ali Khan':
                    sta3 = '357'
                elif STAR3 == 'Billy Crudup':
                    sta3 = '358'
                elif STAR3 == 'Holly Hunter':
                    sta3 = '359'
                elif STAR3 == 'In-mun Kim':
                    sta3 = '360'
                elif STAR3 == 'Lauren Bacall':
                    sta3 = '361'
                elif STAR3 == 'Mary McDonnell':
                    sta3 = '362'
                elif STAR3 == 'Julianne Moore':
                    sta3 = '363'
                elif STAR3 == 'Jane Galloway Heitz':
                    sta3 = '364'
                elif STAR3 == 'Shinpachi Tsuji':
                    sta3 = '365'
                elif STAR3 == 'Thomas Bo Larsen':
                    sta3 = '366'
                elif STAR3 == 'Marília Pêra':
                    sta3 = '367'
                elif STAR3 == 'Jennifer Aniston':
                    sta3 = '368'
                elif STAR3 == 'Thierry van Werveke':
                    sta3 = '369'
                elif STAR3 == 'J.T. Walsh':
                    sta3 = '370'
                elif STAR3 == 'Phyllis Logan':
                    sta3 = '371'
                elif STAR3 == 'Brad Pitt':
                    sta3 = '372'
                elif STAR3 == 'Akio Ôtsuka':
                    sta3 = '373'
                elif STAR3 == 'Catherine O\'Hara':
                    sta3 = '374'
                elif STAR3 == 'Chris Elliott':
                    sta3 = '375'
                elif STAR3 == 'Benjamin Bratt':
                    sta3 = '376'
                elif STAR3 == 'James Rebhorn':
                    sta3 = '377'
                elif STAR3 == 'Robin Williams':
                    sta3 = '378'
                elif STAR3 == 'Robby Benson':
                    sta3 = '379'
                elif STAR3 == 'Graham Greene':
                    sta3 = '380'
                elif STAR3 == 'Ruby Dee':
                    sta3 = '381'
                elif STAR3 == 'Valeria Golino':
                    sta3 = '382'
                elif STAR3 == 'Mami Koyama':
                    sta3 = '383'
                elif STAR3 == 'Robin Wright':
                    sta3 = '384'
                elif STAR3 == 'Otto Sander':
                    sta3 = '385'
                elif STAR3 == 'Francine Racette':
                    sta3 = '386'
                elif STAR3 == 'Kotoe Hatsui':
                    sta3 = '387'
                elif STAR3 == 'Michael Biehn':
                    sta3 = '388'
                elif STAR3 == 'Rohini Hattangadi':
                    sta3 = '389'
                elif STAR3 == 'Ken\'ichi Hagiwara':
                    sta3 = '390'
                elif STAR3 == 'Melvyn Douglas':
                    sta3 = '391'
                elif STAR3 == 'Tony Roberts':
                    sta3 = '392'
                elif STAR3 == 'Richard Dreyfuss':
                    sta3 = '393'
                elif STAR3 == 'Penelope Allen':
                    sta3 = '394'
                elif STAR3 == 'Marty Feldman':
                    sta3 = '395'
                elif STAR3 == 'Victor Jory':
                    sta3 = '396'
                elif STAR3 == 'Linda Blair':
                    sta3 = '397'
                elif STAR3 == 'Alec Cawthorne':
                    sta3 = '398'
                elif STAR3 == 'Leonard Frey':
                    sta3 = '399'
                elif STAR3 == 'Gastone Moschin':
                    sta3 = '400'
                elif STAR3 == 'Katharine Ross':
                    sta3 = '401'
                elif STAR3 == 'Ruth Gordon':
                    sta3 = '402'
                elif STAR3 == 'Kim Hunter':
                    sta3 = '403'
                elif STAR3 == 'George Segal':
                    sta3 = '404'
                elif STAR3 == 'Eleanor Parker':
                    sta3 = '405'
                elif STAR3 == 'Geraldine Chaplin':
                    sta3 = '406'
                elif STAR3 == 'Marianne Koch':
                    sta3 = '407'
                elif STAR3 == 'André S. Labarthe':
                    sta3 = '408'
                elif STAR3 == 'Piper Laurie':
                    sta3 = '409'
                elif STAR3 == 'Anouk Aimée':
                    sta3 = '410'
                elif STAR3 == 'Ricky Nelson':
                    sta3 = '411'
                elif STAR3 == 'Ben Gazzara':
                    sta3 = '412'
                elif STAR3 == 'Janet Leigh':
                    sta3 = '413'
                elif STAR3 == 'Burl Ives':
                    sta3 = '414'
                elif STAR3 == 'Susan Harrison':
                    sta3 = '415'
                elif STAR3 == 'Vince Edwards':
                    sta3 = '416'
                elif STAR3 == 'Lillian Gish':
                    sta3 = '417'
                elif STAR3 == 'Richard Basehart':
                    sta3 = '418'
                elif STAR3 == 'Paul Meurisse':
                    sta3 = '419'
                elif STAR3 == 'Otto Preminger':
                    sta3 = '420'
                elif STAR3 == 'Eddie Albert':
                    sta3 = '421'
                elif STAR3 == 'Frank Lovejoy':
                    sta3 = '422'
                elif STAR3 == 'Valerie Hobson':
                    sta3 = '423'
                elif STAR3 == 'Farley Granger':
                    sta3 = '424'
                elif STAR3 == 'Kirk Douglas':
                    sta3 = '425'
                elif STAR3 == 'Stanley Holloway':
                    sta3 = '426'
                elif STAR3 == 'Clifton Webb':
                    sta3 = '427'
                elif STAR3 == 'Fredric March':
                    sta3 = '428'
                elif STAR3 == 'Raymond Massey':
                    sta3 = '429'
                elif STAR3 == 'Gladys George':
                    sta3 = '430'
                elif STAR3 == 'John Carradine':
                    sta3 = '431'
                elif STAR3 == 'Norman Taurog':
                    sta3 = '432'
                elif STAR3 == 'Paulette Dubost':
                    sta3 = '433'
                elif STAR3 == 'Maureen O\'Sullivan':
                    sta3 = '434'
                elif STAR3 == 'John Wray':
                    sta3 = '435'
                elif STAR3 == 'Grigoriy Aleksandrov':
                    sta3 = '436'
                elif STAR3 == 'Sahil Vaid':
                    sta3 = '437'
                elif STAR3 == 'Kirin Kiki':
                    sta3 = '438'
                elif STAR3 == 'Julia Greer':
                    sta3 = '439'
                elif STAR3 == 'Michael Stuhlbarg':
                    sta3 = '440'
                elif STAR3 == 'Hayley Squires':
                    sta3 = '441'
                elif STAR3 == 'Edward Norton':
                    sta3 = '442'
                elif STAR3 == 'Rima Te Wiata':
                    sta3 = '443'
                elif STAR3 == 'Samantha Isler':
                    sta3 = '444'
                elif STAR3 == 'Maria Doyle Kennedy':
                    sta3 = '445'
                elif STAR3 == 'Cate Blanchett':
                    sta3 = '446'
                elif STAR3 == 'Bill Paxton':
                    sta3 = '447'
                elif STAR3 == 'Forest Whitaker':
                    sta3 = '448'
                elif STAR3 == 'Oscar Isaac':
                    sta3 = '449'
                elif STAR3 == 'Seamus Davey-Fitzpatrick':
                    sta3 = '450'
                elif STAR3 == 'Hugh Jackman':
                    sta3 = '451'
                elif STAR3 == 'Taner Birsel':
                    sta3 = '452'
                elif STAR3 == 'Isabelle Huppert':
                    sta3 = '453'
                elif STAR3 == 'Adel Bencherif':
                    sta3 = '454'
                elif STAR3 == 'Dominique McElligott':
                    sta3 = '455'
                elif STAR3 == 'Per Ragnar':
                    sta3 = '456'
                elif STAR3 == 'Jason Cope':
                    sta3 = '457'
                elif STAR3 == 'Evan Rachel Wood':
                    sta3 = '458'
                elif STAR3 == 'Tarun Arora':
                    sta3 = '459'
                elif STAR3 == 'Vlad Ivanov':
                    sta3 = '460'
                elif STAR3 == 'Simon Pegg':
                    sta3 = '461'
                elif STAR3 == 'John Billingsley':
                    sta3 = '462'
                elif STAR3 == 'Tsuyoshi Ihara':
                    sta3 = '463'
                elif STAR3 == 'Justine Waddell':
                    sta3 = '464'
                elif STAR3 == 'Adil Hussain':
                    sta3 = '465'
                elif STAR3 == 'Bill Murray':
                    sta3 = '466'
                elif STAR3 == 'Danielle Proulx':
                    sta3 = '467'
                elif STAR3 == 'Jean-Baptiste Maunier':
                    sta3 = '468'
                elif STAR3 == 'Terrence Howard':
                    sta3 = '469'
                elif STAR3 == 'Kate Ashfield':
                    sta3 = '470'
                elif STAR3 == 'Güven Kiraç':
                    sta3 = '471'
                elif STAR3 == 'Kevin Bacon':
                    sta3 = '472'
                elif STAR3 == 'Maggie Cheung':
                    sta3 = '473'
                elif STAR3 == 'Darío Grandinetti':
                    sta3 = '474'
                elif STAR3 == 'Filip Sovagovic':
                    sta3 = '475'
                elif STAR3 == 'Yoshiyuki Takei':
                    sta3 = '476'
                elif STAR3 == 'Chris Cooper':
                    sta3 = '477'
                elif STAR3 == 'Graciela Tenenbaum':
                    sta3 = '478'
                elif STAR3 == 'Chiwetel Ejiofor':
                    sta3 = '479'
                elif STAR3 == 'Kate Hudson':
                    sta3 = '480'
                elif STAR3 == 'Justin Theroux':
                    sta3 = '481'
                elif STAR3 == 'Tom Hanks':
                    sta3 = '482'
                elif STAR3 == 'Burt Reynolds':
                    sta3 = '483'
                elif STAR3 == 'Takashi Tachibana':
                    sta3 = '484'
                elif STAR3 == 'Mamaengaroa Kerr-Bell':
                    sta3 = '485'
                elif STAR3 == 'Dennis Hopper':
                    sta3 = '486'
                elif STAR3 == 'Julie Delpy':
                    sta3 = '487'
                elif STAR3 == 'Takeshi Aono':
                    sta3 = '488'
                elif STAR3 == 'Penelope Ann Miller':
                    sta3 = '489'
                elif STAR3 == 'Dianne Wiest':
                    sta3 = '490'
                elif STAR3 == 'Alison Whelan':
                    sta3 = '491'
                elif STAR3 == 'Bill Bernstein':
                    sta3 = '492'
                elif STAR3 == 'Robert De Niro':
                    sta3 = '493'
                elif STAR3 == 'Michael Caine':
                    sta3 = '494'
                elif STAR3 == 'Christopher Guest':
                    sta3 = '495'
                elif STAR3 == 'Darren McGavin':
                    sta3 = '496'
                elif STAR3 == 'Cab Calloway':
                    sta3 = '497'
                elif STAR3 == 'Mariel Hemingway':
                    sta3 = '498'
                elif STAR3 == 'Ann Reinking':
                    sta3 = '499'
                elif STAR3 == 'Scott H. Reiniger':
                    sta3 = '500'
                elif STAR3 == 'Jack Warden':
                    sta3 = '501'
                elif STAR3 == 'Zamira Saunders':
                    sta3 = '502'
                elif STAR3 == 'Pupella Maggio':
                    sta3 = '503'
                elif STAR3 == 'Paul Frankeur':
                    sta3 = '504'
                elif STAR3 == 'Helena Rojo':
                    sta3 = '505'
                elif STAR3 == 'Vivian Pickles':
                    sta3 = '506'
                elif STAR3 == 'Stephen Young':
                    sta3 = '507'
                elif STAR3 == 'Robert Ryan':
                    sta3 = '508'
                elif STAR3 == 'Karl Hardman':
                    sta3 = '509'
                elif STAR3 == 'Anthony Hopkins':
                    sta3 = '510'
                elif STAR3 == 'Warren Oates':
                    sta3 = '511'
                elif STAR3 == 'Walter Matthau':
                    sta3 = '512'
                elif STAR3 == 'Jean Simmons':
                    sta3 = '513'
                elif STAR3 == 'Lea Massari':
                    sta3 = '514'
                elif STAR3 == 'Stella Dassas':
                    sta3 = '515'
                elif STAR3 == 'Anne Baxter':
                    sta3 = '516'
                elif STAR3 == 'Julie Harris':
                    sta3 = '517'
                elif STAR3 == 'Thomas Mitchell':
                    sta3 = '518'
                elif STAR3 == 'Ruth Roman':
                    sta3 = '519'
                elif STAR3 == 'William H. Lynn':
                    sta3 = '520'
                elif STAR3 == 'John Payne':
                    sta3 = '521'
                elif STAR3 == 'John Ridgely':
                    sta3 = '522'
                elif STAR3 == 'Phillip Terry':
                    sta3 = '523'
                elif STAR3 == 'James Stewart':
                    sta3 = '524'
                elif STAR3 == 'Ralph Bellamy':
                    sta3 = '525'
                elif STAR3 == 'Olivia de Havilland':
                    sta3 = '526'
                elif STAR3 == 'Chico Marx':
                    sta3 = '527'
                elif STAR3 == 'Robert Armstrong':
                    sta3 = '528'
                elif STAR3 == 'Olga Baclanova':
                    sta3 = '529'
                elif STAR3 == 'Gustav von Wangenheim':
                    sta3 = '530'
                elif STAR3 == 'Michelle Dockery':
                    sta3 = '531'
                elif STAR3 == 'Rajit Kapoor':
                    sta3 = '532'
                elif STAR3 == 'Paul Raci':
                    sta3 = '533'
                elif STAR3 == 'Babak Karimi':
                    sta3 = '534'
                elif STAR3 == 'Mark Rylance':
                    sta3 = '535'
                elif STAR3 == 'Marco Giallini':
                    sta3 = '536'
                elif STAR3 == 'Janelle Monáe':
                    sta3 = '537'
                elif STAR3 == 'Hugh Bonneville':
                    sta3 = '538'
                elif STAR3 == 'Kareena Kapoor':
                    sta3 = '539'
                elif STAR3 == 'Matthew McConaughey':
                    sta3 = '540'
                elif STAR3 == 'Anupam Kher':
                    sta3 = '541'
                elif STAR3 == 'Kyle Chandler':
                    sta3 = '542'
                elif STAR3 == 'Joel Basman':
                    sta3 = '543'
                elif STAR3 == 'Alan Tudyk':
                    sta3 = '544'
                elif STAR3 == 'Robert Downey Jr.':
                    sta3 = '545'
                elif STAR3 == 'Jennifer Jason Leigh':
                    sta3 = '546'
                elif STAR3 == 'Florence Pugh':
                    sta3 = '547'
                elif STAR3 == 'Jerome Flynn':
                    sta3 = '548'
                elif STAR3 == 'Dominic West':
                    sta3 = '549'
                elif STAR3 == 'Ali Mosaffa':
                    sta3 = '550'
                elif STAR3 == 'Sabrina Ferilli':
                    sta3 = '551'
                elif STAR3 == 'Annu Kapoor':
                    sta3 = '552'
                elif STAR3 == 'Scott Adsit':
                    sta3 = '553'
                elif STAR3 == 'Bill Nighy':
                    sta3 = '554'
                elif STAR3 == 'Mehdi Nebbou':
                    sta3 = '555'
                elif STAR3 == 'Miori Takimoto':
                    sta3 = '556'
                elif STAR3 == 'Annie Potts':
                    sta3 = '557'
                elif STAR3 == 'Sylvia Hoeks':
                    sta3 = '558'
                elif STAR3 == 'Bruce Willis':
                    sta3 = '559'
                elif STAR3 == 'Ryan Gosling':
                    sta3 = '560'
                elif STAR3 == 'Masaki Okada':
                    sta3 = '561'
                elif STAR3 == 'Jeon Gook-Hwan':
                    sta3 = '562'
                elif STAR3 == 'Christopher Plummer':
                    sta3 = '563'
                elif STAR3 == 'Barkhad Abdirahman':
                    sta3 = '564'
                elif STAR3 == 'Tae-hoon Kim':
                    sta3 = '565'
                elif STAR3 == 'Jason Mitchell':
                    sta3 = '566'
                elif STAR3 == 'Jin Goo':
                    sta3 = '567'
                elif STAR3 == 'Yeong-hie Seo':
                    sta3 = '568'
                elif STAR3 == 'Richard Armitage':
                    sta3 = '569'
                elif STAR3 == 'Leonie Benesch':
                    sta3 = '570'
                elif STAR3 == 'Ewa Fröling':
                    sta3 = '571'
                elif STAR3 == 'Sacha Baron Cohen':
                    sta3 = '572'
                elif STAR3 == 'Magnus Millang':
                    sta3 = '573'
                elif STAR3 == 'Amy Adams':
                    sta3 = '574'
                elif STAR3 == 'Famke Janssen':
                    sta3 = '575'
                elif STAR3 == 'Rupert Friend':
                    sta3 = '576'
                elif STAR3 == 'Hugh Walsh':
                    sta3 = '577'
                elif STAR3 == 'Tuncel Kurtiz':
                    sta3 = '578'
                elif STAR3 == 'Brenda Blethyn':
                    sta3 = '579'
                elif STAR3 == 'Bryan Cranston':
                    sta3 = '580'
                elif STAR3 == 'Sigourney Weaver':
                    sta3 = '581'
                elif STAR3 == 'Diane Kruger':
                    sta3 = '582'
                elif STAR3 == 'Dalia Hernández':
                    sta3 = '583'
                elif STAR3 == 'Martin Freeman':
                    sta3 = '584'
                elif STAR3 == 'Tilda Swinton':
                    sta3 = '585'
                elif STAR3 == 'Rani Mukerji':
                    sta3 = '586'
                elif STAR3 == 'Nicolas Bro':
                    sta3 = '587'
                elif STAR3 == 'Iain Rea':
                    sta3 = '588'
                elif STAR3 == 'Yoshiaki Umegaki':
                    sta3 = '589'
                elif STAR3 == 'Gustaf Skarsgård':
                    sta3 = '590'
                elif STAR3 == 'Mía Maestro':
                    sta3 = '591'
                elif STAR3 == 'Pavel Ponomaryov':
                    sta3 = '592'
                elif STAR3 == 'Michel Robin':
                    sta3 = '593'
                elif STAR3 == 'Kang-ho Song':
                    sta3 = '594'
                elif STAR3 == 'Christopher Adamson':
                    sta3 = '595'
                elif STAR3 == 'Lorelei Linklater':
                    sta3 = '596'
                elif STAR3 == 'Wood Harris':
                    sta3 = '597'
                elif STAR3 == 'Ziyi Zhang':
                    sta3 = '598'
                elif STAR3 == 'Candela Peña':
                    sta3 = '599'
                elif STAR3 == 'Paul Sanchez':
                    sta3 = '600'
                elif STAR3 == 'Norman Reedus':
                    sta3 = '601'
                elif STAR3 == 'Laura Dern':
                    sta3 = '602'
                elif STAR3 == 'Eddie Murphy':
                    sta3 = '603'
                elif STAR3 == 'Billy Zane':
                    sta3 = '604'
                elif STAR3 == 'Ren Osugi':
                    sta3 = '605'
                elif STAR3 == 'Jude Law':
                    sta3 = '606'
                elif STAR3 == 'Sean Penn':
                    sta3 = '607'
                elif STAR3 == 'Katrin Cartlidge':
                    sta3 = '608'
                elif STAR3 == 'Sarah Jessica Parker':
                    sta3 = '609'
                elif STAR3 == 'Juliette Lewis':
                    sta3 = '610'
                elif STAR3 == 'Art LaFleur':
                    sta3 = '611'
                elif STAR3 == 'John Haycraft':
                    sta3 = '612'
                elif STAR3 == 'Sela Ward':
                    sta3 = '613'
                elif STAR3 == 'Lillo Brancato':
                    sta3 = '614'
                elif STAR3 == 'Dan Riba':
                    sta3 = '615'
                elif STAR3 == 'Teresa Mo':
                    sta3 = '616'
                elif STAR3 == 'Lisanne Falk':
                    sta3 = '617'
                elif STAR3 == 'Halina Gryglaszewska':
                    sta3 = '618'
                elif STAR3 == 'Hudhail Al-Amir':
                    sta3 = '619'
                elif STAR3 == 'Richard Farnsworth':
                    sta3 = '620'
                elif STAR3 == 'Julie Kavner':
                    sta3 = '621'
                elif STAR3 == 'Rei Sakuma':
                    sta3 = '622'
                elif STAR3 == 'Cary Elwes':
                    sta3 = '623'
                elif STAR3 == 'Sally Yeh':
                    sta3 = '624'
                elif STAR3 == 'Kevin Peter Hall':
                    sta3 = '625'
                elif STAR3 == 'Dan Hicks':
                    sta3 = '626'
                elif STAR3 == 'Mia Sara':
                    sta3 = '627'
                elif STAR3 == 'Roberto Benigni':
                    sta3 = '628'
                elif STAR3 == 'Jeff Cohen':
                    sta3 = '629'
                elif STAR3 == 'Oprah Winfrey':
                    sta3 = '630'
                elif STAR3 == 'Molly Ringwald':
                    sta3 = '631'
                elif STAR3 == 'John Malkovich':
                    sta3 = '632'
                elif STAR3 == 'Ed Harris':
                    sta3 = '633'
                elif STAR3 == 'Diahnne Abbott':
                    sta3 = '634'
                elif STAR3 == 'Peter Coyote':
                    sta3 = '635'
                elif STAR3 == 'Jane Alexander':
                    sta3 = '636'
                elif STAR3 == 'Sam Shepard':
                    sta3 = '637'
                elif STAR3 == 'Chief Dan George':
                    sta3 = '638'
                elif STAR3 == 'Allen Garfield':
                    sta3 = '639'
                elif STAR3 == 'Eric Baugin':
                    sta3 = '640'
                elif STAR3 == 'Michel Auclair':
                    sta3 = '641'
                elif STAR3 == 'Helmut Griem':
                    sta3 = '642'
                elif STAR3 == 'Peter Ostrum':
                    sta3 = '643'
                elif STAR3 == 'Sylvia Miles':
                    sta3 = '644'
                elif STAR3 == 'Richard Crenna':
                    sta3 = '645'
                elif STAR3 == 'Katharine Hepburn':
                    sta3 = '646'
                elif STAR3 == 'Michael J. Pollard':
                    sta3 = '647'
                elif STAR3 == 'David Tomlinson':
                    sta3 = '648'
                elif STAR3 == 'Bernhard Wicki':
                    sta3 = '649'
                elif STAR3 == 'Henri Serre':
                    sta3 = '650'
                elif STAR3 == 'Megs Jenkins':
                    sta3 = '651'
                elif STAR3 == 'Daniel Boulanger':
                    sta3 = '652'
                elif STAR3 == 'Montgomery Clift':
                    sta3 = '653'
                elif STAR3 == 'Walter Brennan':
                    sta3 = '654'
                elif STAR3 == 'Macdonald Carey':
                    sta3 = '655'
                elif STAR3 == 'Andy Devine':
                    sta3 = '656'
                elif STAR3 == 'Paul Lukas':
                    sta3 = '657'
                elif STAR3 == 'Charles Ruggles':
                    sta3 = '658'
                elif STAR3 == 'Colin Clive':
                    sta3 = '659'
                elif STAR3 == 'Ann Dvorak':
                    sta3 = '660'
                elif STAR3 == 'Boris Karloff':
                    sta3 = '661'
                elif STAR3 == 'Diego Cortina Autrey':
                    sta3 = '662'
                elif STAR3 == 'Gemma Jones':
                    sta3 = '663'
                elif STAR3 == 'Morena Baccarin':
                    sta3 = '664'
                elif STAR3 == 'Julia Jones':
                    sta3 = '665'
                elif STAR3 == 'Bradley Whitford':
                    sta3 = '666'
                elif STAR3 == 'Ving Rhames':
                    sta3 = '667'
                elif STAR3 == 'Filip Berg':
                    sta3 = '668'
                elif STAR3 == 'Taika Waititi':
                    sta3 = '669'
                elif STAR3 == 'Kasumi Arimura':
                    sta3 = '670'
                elif STAR3 == 'Tom Prior':
                    sta3 = '671'
                elif STAR3 == 'Nat Wolff':
                    sta3 = '672'
                elif STAR3 == 'Olivia Cooke':
                    sta3 = '673'
                elif STAR3 == 'Salim Kechiouche':
                    sta3 = '674'
                elif STAR3 == 'Rajkummar Rao':
                    sta3 = '675'
                elif STAR3 == 'Nell Cattrysse':
                    sta3 = '676'
                elif STAR3 == 'Shammi Kapoor':
                    sta3 = '677'
                elif STAR3 == 'June Squibb':
                    sta3 = '678'
                elif STAR3 == 'Jane Lynch':
                    sta3 = '679'
                elif STAR3 == 'Marcia Gay Harden':
                    sta3 = '680'
                elif STAR3 == 'Kathy Bates':
                    sta3 = '681'
                elif STAR3 == 'Will Ferrell':
                    sta3 = '682'
                elif STAR3 == 'Zoe Saldana':
                    sta3 = '683'
                elif STAR3 == 'Ricky Adelayitor':
                    sta3 = '684'
                elif STAR3 == 'Justin Timberlake':
                    sta3 = '685'
                elif STAR3 == 'Jennifer Lawrence':
                    sta3 = '686'
                elif STAR3 == 'Justin Bartha':
                    sta3 = '687'
                elif STAR3 == 'Naomie Harris':
                    sta3 = '688'
                elif STAR3 == 'Geoffrey Arend':
                    sta3 = '689'
                elif STAR3 == 'Liam Neeson':
                    sta3 = '690'
                elif STAR3 == 'Katsunosuke Hori':
                    sta3 = '691'
                elif STAR3 == 'Amy Ryan':
                    sta3 = '692'
                elif STAR3 == 'Rebecca De Mornay':
                    sta3 = '693'
                elif STAR3 == 'Mitsutaka Itakura':
                    sta3 = '694'
                elif STAR3 == 'Asaka Seto':
                    sta3 = '695'
                elif STAR3 == 'Jo Hartley':
                    sta3 = '696'
                elif STAR3 == 'Rolf Lassgård':
                    sta3 = '697'
                elif STAR3 == 'Gillian Anderson':
                    sta3 = '698'
                elif STAR3 == 'Guillaume Canet':
                    sta3 = '699'
                elif STAR3 == 'Craig Parkinson':
                    sta3 = '700'
                elif STAR3 == 'Zachary Levi':
                    sta3 = '701'
                elif STAR3 == 'Thom Hoffman':
                    sta3 = '702'
                elif STAR3 == 'Michelle Williams':
                    sta3 = '703'
                elif STAR3 == 'Ben Foster':
                    sta3 = '704'
                elif STAR3 == 'Thandie Newton':
                    sta3 = '705'
                elif STAR3 == 'Qiu Yuen':
                    sta3 = '706'
                elif STAR3 == 'Aitana Sánchez-Gijón':
                    sta3 = '707'
                elif STAR3 == 'Kerry Washington':
                    sta3 = '708'
                elif STAR3 == 'Giovanni Ribisi':
                    sta3 = '709'
                elif STAR3 == 'Dakota Fanning':
                    sta3 = '710'
                elif STAR3 == 'John Hodgman':
                    sta3 = '711'
                elif STAR3 == 'Billy Connolly':
                    sta3 = '712'
                elif STAR3 == 'Nora-Jane Noone':
                    sta3 = '713'
                elif STAR3 == 'Chulpan Khamatova':
                    sta3 = '714'
                elif STAR3 == 'Djimon Hounsou':
                    sta3 = '715'
                elif STAR3 == 'Rob Maxey':
                    sta3 = '716'
                elif STAR3 == 'Oliver Stokowski':
                    sta3 = '717'
                elif STAR3 == 'Jean Heywood':
                    sta3 = '718'
                elif STAR3 == 'Stephen Trask':
                    sta3 = '719'
                elif STAR3 == 'Julia Roberts':
                    sta3 = '720'
                elif STAR3 == 'Pamela Adlon':
                    sta3 = '721'
                elif STAR3 == 'John Turturro':
                    sta3 = '722'
                elif STAR3 == 'Kurt Russell':
                    sta3 = '723'
                elif STAR3 == 'Mary Kay Bergman':
                    sta3 = '724'
                elif STAR3 == 'David Herman':
                    sta3 = '725'
                elif STAR3 == 'Philip Seymour Hoffman':
                    sta3 = '726'
                elif STAR3 == 'Scott Glenn':
                    sta3 = '727'
                elif STAR3 == 'Olivia Williams':
                    sta3 = '728'
                elif STAR3 == 'Chete Lera':
                    sta3 = '729'
                elif STAR3 == 'Greg Kinnear':
                    sta3 = '730'
                elif STAR3 == 'Gary Oldman':
                    sta3 = '731'
                elif STAR3 == 'Francis Huster':
                    sta3 = '732'
                elif STAR3 == 'Justin Braine':
                    sta3 = '733'
                elif STAR3 == 'Derek Jacobi':
                    sta3 = '734'
                elif STAR3 == 'Liam Cunningham':
                    sta3 = '735'
                elif STAR3 == 'Takeshi Kaneshiro':
                    sta3 = '736'
                elif STAR3 == 'Philippe Noiret':
                    sta3 = '737'
                elif STAR3 == 'Marilyn Ghigliotti':
                    sta3 = '738'
                elif STAR3 == 'Tim Robbins':
                    sta3 = '739'
                elif STAR3 == 'Roberta Maxwell':
                    sta3 = '740'
                elif STAR3 == 'Dave Goelz':
                    sta3 = '741'
                elif STAR3 == 'Delroy Lindo':
                    sta3 = '742'
                elif STAR3 == 'Russell Means':
                    sta3 = '743'
                elif STAR3 == 'Bunshi Katsura Vi':
                    sta3 = '744'
                elif STAR3 == 'Alec Baldwin':
                    sta3 = '745'
                elif STAR3 == 'Demi Moore':
                    sta3 = '746'
                elif STAR3 == 'Mary Stuart Masterson':
                    sta3 = '747'
                elif STAR3 == 'Albert Finney':
                    sta3 = '748'
                elif STAR3 == 'Joanna Cassidy':
                    sta3 = '749'
                elif STAR3 == 'Johanna ter Steege':
                    sta3 = '750'
                elif STAR3 == 'Richard Griffiths':
                    sta3 = '751'
                elif STAR3 == 'Peter O\'Toole':
                    sta3 = '752'
                elif STAR3 == 'Miranda Richardson':
                    sta3 = '753'
                elif STAR3 == 'Helmut Qualtinger':
                    sta3 = '754'
                elif STAR3 == 'Danny Aiello':
                    sta3 = '755'
                elif STAR3 == 'Verna Bloom':
                    sta3 = '756'
                elif STAR3 == 'Patrick Horgan':
                    sta3 = '757'
                elif STAR3 == 'DeForest Kelley':
                    sta3 = '758'
                elif STAR3 == 'Judd Hirsch':
                    sta3 = '759'
                elif STAR3 == 'Robert Hays':
                    sta3 = '760'
                elif STAR3 == 'Kiyoshi Kobayashi':
                    sta3 = '761'
                elif STAR3 == 'Tony Moran':
                    sta3 = '762'
                elif STAR3 == 'Georges Adet':
                    sta3 = '763'
                elif STAR3 == 'Slim Pickens':
                    sta3 = '764'
                elif STAR3 == 'Jack Kehoe':
                    sta3 = '765'
                elif STAR3 == 'Jim Kelly':
                    sta3 = '766'
                elif STAR3 == 'Ned Beatty':
                    sta3 = '767'
                elif STAR3 == 'Fernando Rey':
                    sta3 = '768'
                elif STAR3 == 'Harry Guardino':
                    sta3 = '769'
                elif STAR3 == 'Mary Ure':
                    sta3 = '770'
                elif STAR3 == 'John Fiedler':
                    sta3 = '771'
                elif STAR3 == 'Charles Bronson':
                    sta3 = '772'
                elif STAR3 == 'Michel Piccoli':
                    sta3 = '773'
                elif STAR3 == 'John Fraser':
                    sta3 = '774'
                elif STAR3 == 'Ulla Jacobsson':
                    sta3 = '775'
                elif STAR3 == 'Honor Blackman':
                    sta3 = '776'
                elif STAR3 == 'Jessica Tandy':
                    sta3 = '777'
                elif STAR3 == 'Polly Bergen':
                    sta3 = '778'
                elif STAR3 == 'Moira Shearer':
                    sta3 = '779'
                elif STAR3 == 'Juliette Mayniel':
                    sta3 = '780'
                elif STAR3 == 'Larry Gates':
                    sta3 = '781'
                elif STAR3 == 'Sal Mineo':
                    sta3 = '782'
                elif STAR3 == 'Cecil Parker':
                    sta3 = '783'
                elif STAR3 == 'William Holden':
                    sta3 = '784'
                elif STAR3 == 'Barry Fitzgerald':
                    sta3 = '785'
                elif STAR3 == 'Hugh Marlowe':
                    sta3 = '786'
                elif STAR3 == 'Robert Morley':
                    sta3 = '787'
                elif STAR3 == 'George Macready':
                    sta3 = '788'
                elif STAR3 == 'Norman Ferguson':
                    sta3 = '789'
                elif STAR3 == 'William Harrigan':
                    sta3 = '790'
                elif STAR3 == 'Joseph Lee':
                    sta3 = '791'
                elif STAR3 == 'Matvey Novikov':
                    sta3 = '792'
                elif STAR3 == 'Brie Larson':
                    sta3 = '793'
                elif STAR3 == 'Lindsay Duncan':
                    sta3 = '794'
                elif STAR3 == 'Ann Owens':
                    sta3 = '795'
                elif STAR3 == 'Franz Rogowski':
                    sta3 = '796'
                elif STAR3 == 'Tugba Sunguroglu':
                    sta3 = '797'
                elif STAR3 == 'Dave Bautista':
                    sta3 = '798'
                elif STAR3 == 'Jon Hamm':
                    sta3 = '799'
                elif STAR3 == 'Jeff Bridges':
                    sta3 = '800'
                elif STAR3 == 'Alan Alda':
                    sta3 = '801'
                elif STAR3 == 'Sarah Vowell':
                    sta3 = '802'
                elif STAR3 == 'Chris Williams':
                    sta3 = '803'
                elif STAR3 == 'Tessa Thompson':
                    sta3 = '804'
                elif STAR3 == 'Roman Madyanov':
                    sta3 = '805'
                elif STAR3 == 'Sophie Kennedy Clark':
                    sta3 = '806'
                elif STAR3 == 'Andy Serkis':
                    sta3 = '807'
                elif STAR3 == 'Belén Rueda':
                    sta3 = '808'
                elif STAR3 == 'Ray Sahetapy':
                    sta3 = '809'
                elif STAR3 == 'Anna Kendrick':
                    sta3 = '810'
                elif STAR3 == 'Ryûnosuke Kamiki':
                    sta3 = '811'
                elif STAR3 == 'Sam Elliott':
                    sta3 = '812'
                elif STAR3 == 'Matt Damon':
                    sta3 = '813'
                elif STAR3 == 'Markus Rygaard':
                    sta3 = '814'
                elif STAR3 == 'Jason Segel':
                    sta3 = '815'
                elif STAR3 == 'Chloë Grace Moretz':
                    sta3 = '816'
                elif STAR3 == 'Antonio Resines':
                    sta3 = '817'
                elif STAR3 == 'Jonah Hill':
                    sta3 = '818'
                elif STAR3 == 'Jan Cornet':
                    sta3 = '819'
                elif STAR3 == 'Woody Harrelson':
                    sta3 = '820'
                elif STAR3 == 'Max Riemelt':
                    sta3 = '821'
                elif STAR3 == 'Tim McGraw':
                    sta3 = '822'
                elif STAR3 == 'Danai Gurira':
                    sta3 = '823'
                elif STAR3 == 'Armin Mueller-Stahl':
                    sta3 = '824'
                elif STAR3 == 'Sienna Miller':
                    sta3 = '825'
                elif STAR3 == 'Brendan Gleeson':
                    sta3 = '826'
                elif STAR3 == 'Jodie Foster':
                    sta3 = '827'
                elif STAR3 == 'Casey Affleck':
                    sta3 = '828'
                elif STAR3 == 'Pascal Greggory':
                    sta3 = '829'
                elif STAR3 == 'Yong Dong':
                    sta3 = '830'
                elif STAR3 == 'Paul Giamatti':
                    sta3 = '831'
                elif STAR3 == 'Toby Kebbell':
                    sta3 = '832'
                elif STAR3 == 'David Wenham':
                    sta3 = '833'
                elif STAR3 == 'Emily Mortimer':
                    sta3 = '834'
                elif STAR3 == 'Carla Gugino':
                    sta3 = '835'
                elif STAR3 == 'Danny Glover':
                    sta3 = '836'
                elif STAR3 == 'Elisabeth Shue':
                    sta3 = '837'
                elif STAR3 == 'Thibault Verhaeghe':
                    sta3 = '838'
                elif STAR3 == 'Bobby Cannavale':
                    sta3 = '839'
                elif STAR3 == 'Naomi Watts':
                    sta3 = '840'
                elif STAR3 == 'Bae Doona':
                    sta3 = '841'
                elif STAR3 == 'Julie Christie':
                    sta3 = '842'
                elif STAR3 == 'Amy Smart':
                    sta3 = '843'
                elif STAR3 == 'Christopher Eccleston':
                    sta3 = '844'
                elif STAR3 == 'Tarô Yamamoto':
                    sta3 = '845'
                elif STAR3 == 'Anjelica Huston':
                    sta3 = '846'
                elif STAR3 == 'Daniel Giménez Cacho':
                    sta3 = '847'
                elif STAR3 == 'Richard Harris':
                    sta3 = '848'
                elif STAR3 == 'Fionnula Flanagan':
                    sta3 = '849'
                elif STAR3 == 'Franka Potente':
                    sta3 = '850'
                elif STAR3 == 'Joseph Fiennes':
                    sta3 = '851'
                elif STAR3 == 'Samantha Morton':
                    sta3 = '852'
                elif STAR3 == 'Deborah Kara Unger':
                    sta3 = '853'
                elif STAR3 == 'Josh Lucas':
                    sta3 = '854'
                elif STAR3 == 'Herbert Knaup':
                    sta3 = '855'
                elif STAR3 == 'Nick Nolte':
                    sta3 = '856'
                elif STAR3 == 'Tobey Maguire':
                    sta3 = '857'
                elif STAR3 == 'Arno Frisch':
                    sta3 = '858'
                elif STAR3 == 'John Roselius':
                    sta3 = '859'
                elif STAR3 == 'James Fleet':
                    sta3 = '860'
                elif STAR3 == 'Crispin Glover':
                    sta3 = '861'
                elif STAR3 == 'Annie Corley':
                    sta3 = '862'
                elif STAR3 == 'Janusz Gajos':
                    sta3 = '863'
                elif STAR3 == 'Barbara Hershey':
                    sta3 = '864'
                elif STAR3 == 'Ralph Macchio':
                    sta3 = '865'
                elif STAR3 == 'Yoko Honna':
                    sta3 = '866'
                elif STAR3 == 'Dominique Pinon':
                    sta3 = '867'
                elif STAR3 == 'Daniel Stern':
                    sta3 = '868'
                elif STAR3 == 'Andy Garcia':
                    sta3 = '869'
                elif STAR3 == 'Samuel E. Wright':
                    sta3 = '870'
                elif STAR3 == 'O.J. Simpson':
                    sta3 = '871'
                elif STAR3 == 'Laila Robins':
                    sta3 = '872'
                elif STAR3 == 'Gary Busey':
                    sta3 = '873'
                elif STAR3 == 'Jane Fonda':
                    sta3 = '874'
                elif STAR3 == 'Michael Preston':
                    sta3 = '875'
                elif STAR3 == 'Dorsey Wright':
                    sta3 = '876'
                elif STAR3 == 'Jerry Nelson':
                    sta3 = '877'
                elif STAR3 == 'Roberts Blossom':
                    sta3 = '878'
                elif STAR3 == 'Richard Briers':
                    sta3 = '879'
                elif STAR3 == 'Bo Hopkins':
                    sta3 = '880'
                elif STAR3 == 'Teri Garr':
                    sta3 = '881'
                elif STAR3 == 'Romolo Valli':
                    sta3 = '882'
                elif STAR3 == 'Louis Prima':
                    sta3 = '883'
                elif STAR3 == 'Sarah Miles':
                    sta3 = '884'
                elif STAR3 == 'George Harrison':
                    sta3 = '885'
                elif STAR3 == 'Patricia Neal':
                    sta3 = '886'
                elif STAR3 == 'James Dean':
                    sta3 = '887'
                elif STAR3 == 'Deborah Kerr':
                    sta3 = '888'
                elif STAR3 == 'Walter Slezak':
                    sta3 = '889'
                elif STAR3 == 'Lucie Mannheim':
                    sta3 = '890'

                STAR4 = request.form['star4']
                if STAR4 == 'William Sadler':
                    sta4 = '0'
                elif STAR4 == 'Diane Keaton':
                    sta4 = '1'
                elif STAR4 == 'Michael Caine':
                    sta4 = '2'
                elif STAR4 == 'John Fiedler':
                    sta4 = '3'
                elif STAR4 == 'Orlando Bloom':
                    sta4 = '4'
                elif STAR4 == 'Bruce Willis':
                    sta4 = '5'
                elif STAR4 == 'Caroline Goodall':
                    sta4 = '6'
                elif STAR4 == 'Ken Watanabe':
                    sta4 = '7'
                elif STAR4 == 'Zach Grenier':
                    sta4 = '8'
                elif STAR4 == 'Sean Bean':
                    sta4 = '9'
                elif STAR4 == 'Sally Field':
                    sta4 = '10'
                elif STAR4 == 'Aldo Giuffrè':
                    sta4 = '11'
                elif STAR4 == 'Carrie-Anne Moss':
                    sta4 = '12'
                elif STAR4 == 'Lorraine Bracco':
                    sta4 = '13'
                elif STAR4 == 'Billy Dee Williams':
                    sta4 = '14'
                elif STAR4 == 'Peter Brocco':
                    sta4 = '15'
                elif STAR4 == 'Renée Elise Goldsberry':
                    sta4 = '16'
                elif STAR4 == 'Choi Woo-sik':
                    sta4 = '17'
                elif STAR4 == 'Aparna Balamurali':
                    sta4 = '18'
                elif STAR4 == 'Mackenzie Foy':
                    sta4 = '19'
                elif STAR4 == 'Matheus Nachtergaele':
                    sta4 = '20'
                elif STAR4 == 'Rumi Hiiragi':
                    sta4 = '21'
                elif STAR4 == 'Edward Burns':
                    sta4 = '22'
                elif STAR4 == 'Bonnie Hunt':
                    sta4 = '23'
                elif STAR4 == 'Giustino Durano':
                    sta4 = '24'
                elif STAR4 == 'Andrew Kevin Walker':
                    sta4 = '25'
                elif STAR4 == 'Kasi Lemmons':
                    sta4 = '26'
                elif STAR4 == 'Alec Guinness':
                    sta4 = '27'
                elif STAR4 == 'Tetsurô Tanba':
                    sta4 = '28'
                elif STAR4 == 'Yukiko Shimazaki':
                    sta4 = '29'
                elif STAR4 == 'Thomas Mitchell':
                    sta4 = '30'
                elif STAR4 == 'Frances Conroy':
                    sta4 = '31'
                elif STAR4 == 'Paul Reiser':
                    sta4 = '32'
                elif STAR4 == 'Anne Le Ny':
                    sta4 = '33'
                elif STAR4 == 'Mark Wahlberg':
                    sta4 = '34'
                elif STAR4 == 'Emilia Fox':
                    sta4 = '35'
                elif STAR4 == 'Oliver Reed':
                    sta4 = '36'
                elif STAR4 == 'Jennifer Lien':
                    sta4 = '37'
                elif STAR4 == 'Stephen Baldwin':
                    sta4 = '38'
                elif STAR4 == 'Danny Aiello':
                    sta4 = '39'
                elif STAR4 == 'James Earl Jones':
                    sta4 = '40'
                elif STAR4 == 'Robert Patrick':
                    sta4 = '41'
                elif STAR4 == 'Isa Danieli':
                    sta4 = '42'
                elif STAR4 == 'Yoshiko Shinohara':
                    sta4 = '43'
                elif STAR4 == 'Crispin Glover':
                    sta4 = '44'
                elif STAR4 == 'Jason Robards':
                    sta4 = '45'
                elif STAR4 == 'John Gavin':
                    sta4 = '46'
                elif STAR4 == 'Claude Rains':
                    sta4 = '47'
                elif STAR4 == 'Tiny Sandford':
                    sta4 = '48'
                elif STAR4 == 'Harry Myers':
                    sta4 = '49'
                elif STAR4 == 'Kawsar Al Haddad':
                    sta4 = '50'
                elif STAR4 == 'Kyung-jin Lee':
                    sta4 = '51'
                elif STAR4 == 'Shraddha Srinath':
                    sta4 = '52'
                elif STAR4 == 'Aoi Yûki':
                    sta4 = '53'
                elif STAR4 == 'Sanya Malhotra':
                    sta4 = '54'
                elif STAR4 == 'Jake Johnson':
                    sta4 = '55'
                elif STAR4 == 'Mark Ruffalo':
                    sta4 = '56'
                elif STAR4 == 'Benjamin Bratt':
                    sta4 = '57'
                elif STAR4 == 'Kerry Washington':
                    sta4 = '58'
                elif STAR4 == 'Gary Oldman':
                    sta4 = '59'
                elif STAR4 == 'Sharman Joshi':
                    sta4 = '60'
                elif STAR4 == 'Tisca Chopra':
                    sta4 = '61'
                elif STAR4 == 'Fred Willard':
                    sta4 = '62'
                elif STAR4 == 'Ulrich Tukur':
                    sta4 = '63'
                elif STAR4 == 'Kim Byeong-Ok':
                    sta4 = '64'
                elif STAR4 == 'Mark Boone Junior':
                    sta4 = '65'
                elif STAR4 == 'Billy Crudup':
                    sta4 = '66'
                elif STAR4 == 'Treat Williams':
                    sta4 = '67'
                elif STAR4 == 'John Rhys-Davies':
                    sta4 = '68'
                elif STAR4 == 'Scatman Crothers':
                    sta4 = '69'
                elif STAR4 == 'Frederic Forrest':
                    sta4 = '70'
                elif STAR4 == 'Veronica Cartwright':
                    sta4 = '71'
                elif STAR4 == 'Ramesh Deo':
                    sta4 = '72'
                elif STAR4 == 'Kyôko Kagawa':
                    sta4 = '73'
                elif STAR4 == 'Keenan Wynn':
                    sta4 = '74'
                elif STAR4 == 'Elsa Lanchester':
                    sta4 = '75'
                elif STAR4 == 'George Macready':
                    sta4 = '76'
                elif STAR4 == 'Thelma Ritter':
                    sta4 = '77'
                elif STAR4 == 'Nancy Olson':
                    sta4 = '78'
                elif STAR4 == 'Reginald Gardiner':
                    sta4 = '79'
                elif STAR4 == 'Colin Firth':
                    sta4 = '80'
                elif STAR4 == 'Jyoti Malshe':
                    sta4 = '81'
                elif STAR4 == 'Anil Dhawan':
                    sta4 = '82'
                elif STAR4 == 'Ansiba':
                    sta4 = '83'
                elif STAR4 == 'Lasse Fogelstrøm':
                    sta4 = '84'
                elif STAR4 == 'Shahab Hosseini':
                    sta4 = '85'
                elif STAR4 == 'Mustafa Kamel':
                    sta4 = '86'
                elif STAR4 == 'Celile Toyon Uysal':
                    sta4 = '87'
                elif STAR4 == 'Ege Tanman':
                    sta4 = '88'
                elif STAR4 == 'Mélanie Laurent':
                    sta4 = '89'
                elif STAR4 == 'Gerry Robert Byrne':
                    sta4 = '90'
                elif STAR4 == 'Lorella Cravotta':
                    sta4 = '91'
                elif STAR4 == 'Dennis Farina':
                    sta4 = '92'
                elif STAR4 == 'Marlon Wayans':
                    sta4 = '93'
                elif STAR4 == 'Wes Bentley':
                    sta4 = '94'
                elif STAR4 == 'Stellan Skarsgård':
                    sta4 = '95'
                elif STAR4 == 'Nafise Jafar-Mohammadi':
                    sta4 = '96'
                elif STAR4 == 'Jim Varney':
                    sta4 = '97'
                elif STAR4 == 'Angus Macfadyen':
                    sta4 = '98'
                elif STAR4 == 'Chris Penn':
                    sta4 = '99'
                elif STAR4 == 'Adam Baldwin':
                    sta4 = '100'
                elif STAR4 == 'Vladas Bagdonas':
                    sta4 = '101'
                elif STAR4 == 'Roy Dotrice':
                    sta4 = '102'
                elif STAR4 == 'Mary Elizabeth Mastrantonio':
                    sta4 = '103'
                elif STAR4 == 'Hubertus Bengsch':
                    sta4 = '104'
                elif STAR4 == 'Albert Brooks':
                    sta4 = '105'
                elif STAR4 == 'Charles Durning':
                    sta4 = '106'
                elif STAR4 == 'Warren Clarke':
                    sta4 = '107'
                elif STAR4 == 'Daniel Richter':
                    sta4 = '108'
                elif STAR4 == 'Mara Krupp':
                    sta4 = '109'
                elif STAR4 == 'Jack Hawkins':
                    sta4 = '110'
                elif STAR4 == 'Ray Walston':
                    sta4 = '111'
                elif STAR4 == 'Jessie Royce Landis':
                    sta4 = '112'
                elif STAR4 == 'Tom Helmore':
                    sta4 = '113'
                elif STAR4 == 'Debbie Reynolds':
                    sta4 = '114'
                elif STAR4 == 'Haruo Tanaka':
                    sta4 = '115'
                elif STAR4 == 'Elena Altieri':
                    sta4 = '116'
                elif STAR4 == 'Byron Barr':
                    sta4 = '117'
                elif STAR4 == 'Agnes Moorehead':
                    sta4 = '118'
                elif STAR4 == 'Otto Wernicke':
                    sta4 = '119'
                elif STAR4 == 'Rudolf Klein-Rogge':
                    sta4 = '120'
                elif STAR4 == 'Carl Miller':
                    sta4 = '121'
                elif STAR4 == 'Prateik':
                    sta4 = '122'
                elif STAR4 == 'Yami Gautam':
                    sta4 = '123'
                elif STAR4 == 'Archana Jois':
                    sta4 = '124'
                elif STAR4 == 'Sebastian Maniscalco':
                    sta4 = '125'
                elif STAR4 == 'Caleb Landry Jones':
                    sta4 = '126'
                elif STAR4 == 'Sohum Shah':
                    sta4 = '127'
                elif STAR4 == 'Tamannaah Bhatia':
                    sta4 = '128'
                elif STAR4 == 'Rashida Jones':
                    sta4 = '129'
                elif STAR4 == 'Rajat Kapoor':
                    sta4 = '130'
                elif STAR4 == 'Jeffrey Ho':
                    sta4 = '131'
                elif STAR4 == 'Misha Meskhi':
                    sta4 = '132'
                elif STAR4 == 'Art Malik':
                    sta4 = '133'
                elif STAR4 == 'Tigmanshu Dhulia':
                    sta4 = '134'
                elif STAR4 == 'Ram Kapoor':
                    sta4 = '135'
                elif STAR4 == 'Hemendra Dandotiya':
                    sta4 = '136'
                elif STAR4 == 'Carla Quevedo':
                    sta4 = '137'
                elif STAR4 == 'Jennifer Morrison':
                    sta4 = '138'
                elif STAR4 == 'Ben Kingsley':
                    sta4 = '139'
                elif STAR4 == 'John Ratzenberger':
                    sta4 = '140'
                elif STAR4 == 'Matthew McConaughey':
                    sta4 = '141'
                elif STAR4 == 'Shilpa Shukla':
                    sta4 = '142'
                elif STAR4 == 'Martin Stringer':
                    sta4 = '143'
                elif STAR4 == 'Maribel Verdú':
                    sta4 = '144'
                elif STAR4 == 'Ned Beatty':
                    sta4 = '145'
                elif STAR4 == 'Stephen Rea':
                    sta4 = '146'
                elif STAR4 == 'Ayesha Kapoor':
                    sta4 = '147'
                elif STAR4 == 'Liam Neeson':
                    sta4 = '148'
                elif STAR4 == 'Smit Sheth':
                    sta4 = '149'
                elif STAR4 == 'Juliane Köhler':
                    sta4 = '150'
                elif STAR4 == 'Akihiro Miwa':
                    sta4 = '151'
                elif STAR4 == 'Christopher Plummer':
                    sta4 = '152'
                elif STAR4 == 'Tabu':
                    sta4 = '153'
                elif STAR4 == 'Jason Statham':
                    sta4 = '154'
                elif STAR4 == 'Kim Basinger':
                    sta4 = '155'
                elif STAR4 == 'Yesim Salkim':
                    sta4 = '156'
                elif STAR4 == 'Jon Voight':
                    sta4 = '157'
                elif STAR4 == 'James Woods':
                    sta4 = '158'
                elif STAR4 == 'Karisma Kapoor':
                    sta4 = '159'
                elif STAR4 == 'Richard Harris':
                    sta4 = '160'
                elif STAR4 == 'Denholm Elliott':
                    sta4 = '161'
                elif STAR4 == 'Husnija Hasimovic':
                    sta4 = '162'
                elif STAR4 == 'Shigesato Itoi':
                    sta4 = '163'
                elif STAR4 == 'Reginald VelJohnson':
                    sta4 = '164'
                elif STAR4 == 'Daisuke Ryû':
                    sta4 = '165'
                elif STAR4 == 'Frank Vincent':
                    sta4 = '166'
                elif STAR4 == 'Nikolay Grinko':
                    sta4 = '167'
                elif STAR4 == 'Halvar Björk':
                    sta4 = '168'
                elif STAR4 == 'Johnny Sekka':
                    sta4 = '169'
                elif STAR4 == 'Amjad Khan':
                    sta4 = '170'
                elif STAR4 == 'Eric Idle':
                    sta4 = '171'
                elif STAR4 == 'Charles Bronson':
                    sta4 = '172'
                elif STAR4 == 'Rosemary Murphy':
                    sta4 = '173'
                elif STAR4 == 'Yôko Tsukasa':
                    sta4 = '174'
                elif STAR4 == 'Marlene Dietrich':
                    sta4 = '175'
                elif STAR4 == 'George Raft':
                    sta4 = '176'
                elif STAR4 == 'Gunnar Björnstrand':
                    sta4 = '177'
                elif STAR4 == 'Nils Poppe':
                    sta4 = '178'
                elif STAR4 == 'Janine Darcey':
                    sta4 = '179'
                elif STAR4 == 'John Williams':
                    sta4 = '180'
                elif STAR4 == 'Setsuko Hara':
                    sta4 = '181'
                elif STAR4 == 'Takashi Shimura':
                    sta4 = '182'
                elif STAR4 == 'Celeste Holm':
                    sta4 = '183'
                elif STAR4 == 'Bruce Bennett':
                    sta4 = '184'
                elif STAR4 == 'Felix Bressart':
                    sta4 = '185'
                elif STAR4 == 'Henry Bergman':
                    sta4 = '186'
                elif STAR4 == 'Erwin Connelly':
                    sta4 = '187'
                elif STAR4 == 'Valeria Golino':
                    sta4 = '188'
                elif STAR4 == 'Andrea Tariang':
                    sta4 = '189'
                elif STAR4 == 'Kenshô Ono':
                    sta4 = '190'
                elif STAR4 == 'Bárbara Lennie':
                    sta4 = '191'
                elif STAR4 == 'Moon So-Ri':
                    sta4 = '192'
                elif STAR4 == 'Patrick Huard':
                    sta4 = '193'
                elif STAR4 == 'Kay Kay Menon':
                    sta4 = '194'
                elif STAR4 == 'Boyd Holbrook':
                    sta4 = '195'
                elif STAR4 == 'Wendy Crewson':
                    sta4 = '196'
                elif STAR4 == 'Diego Starosta':
                    sta4 = '197'
                elif STAR4 == 'Graham Norton':
                    sta4 = '198'
                elif STAR4 == 'Ayberk Pekcan':
                    sta4 = '199'
                elif STAR4 == 'Boman Irani':
                    sta4 = '200'
                elif STAR4 == 'Mahesh Manjrekar':
                    sta4 = '201'
                elif STAR4 == 'Adrien Brody':
                    sta4 = '202'
                elif STAR4 == 'Tyler Perry':
                    sta4 = '203'
                elif STAR4 == 'Yukito Nishii':
                    sta4 = '204'
                elif STAR4 == 'Teresa Palmer':
                    sta4 = '205'
                elif STAR4 == 'Lewis Black':
                    sta4 = '206'
                elif STAR4 == 'Saurabh Shukla':
                    sta4 = '207'
                elif STAR4 == 'Brad Pitt':
                    sta4 = '208'
                elif STAR4 == 'Alexandra Maria Lara':
                    sta4 = '209'
                elif STAR4 == 'Caitriona Balfe':
                    sta4 = '210'
                elif STAR4 == 'Liev Schreiber':
                    sta4 = '211'
                elif STAR4 == 'Fionnula Flanagan':
                    sta4 = '212'
                elif STAR4 == 'Nawazuddin Siddiqui':
                    sta4 = '213'
                elif STAR4 == 'Katrina Kaif':
                    sta4 = '214'
                elif STAR4 == 'Melissa Leo':
                    sta4 = '215'
                elif STAR4 == 'Zoë Kravitz':
                    sta4 = '216'
                elif STAR4 == 'Aamir Bashir':
                    sta4 = '217'
                elif STAR4 == 'Ahney Her':
                    sta4 = '218'
                elif STAR4 == 'Michael Gambon':
                    sta4 = '219'
                elif STAR4 == 'Kazuko Yoshiyuki':
                    sta4 = '220'
                elif STAR4 == 'Sarah Roemer':
                    sta4 = '221'
                elif STAR4 == 'Barry Humphries':
                    sta4 = '222'
                elif STAR4 == 'Christopher Mintz-Plasse':
                    sta4 = '223'
                elif STAR4 == 'Marcia Gay Harden':
                    sta4 = '224'
                elif STAR4 == 'Josh Brolin':
                    sta4 = '225'
                elif STAR4 == 'Jay Baruchel':
                    sta4 = '226'
                elif STAR4 == 'Xolani Mali':
                    sta4 = '227'
                elif STAR4 == 'Hyeong-jin Kong':
                    sta4 = '228'
                elif STAR4 == 'Louise Lemoine Torrès':
                    sta4 = '229'
                elif STAR4 == 'Sunil Dutt':
                    sta4 = '230'
                elif STAR4 == 'Jae-ho Song':
                    sta4 = '231'
                elif STAR4 == 'Preity Zinta':
                    sta4 = '232'
                elif STAR4 == 'Michael Madsen':
                    sta4 = '233'
                elif STAR4 == 'Alexander Gould':
                    sta4 = '234'
                elif STAR4 == 'Martin Sheen':
                    sta4 = '235'
                elif STAR4 == 'Álvaro Guerrero':
                    sta4 = '236'
                elif STAR4 == 'John Goodman':
                    sta4 = '237'
                elif STAR4 == 'Yûko Miyamura':
                    sta4 = '238'
                elif STAR4 == 'Rachel Shelley':
                    sta4 = '239'
                elif STAR4 == 'Olivia Williams':
                    sta4 = '240'
                elif STAR4 == 'Bill Nunn':
                    sta4 = '241'
                elif STAR4 == 'Noah Emmerich':
                    sta4 = '242'
                elif STAR4 == 'Florijan Ajdini':
                    sta4 = '243'
                elif STAR4 == 'Julianne Moore':
                    sta4 = '244'
                elif STAR4 == 'Tung Cho \'Joe\' Cheung':
                    sta4 = '245'
                elif STAR4 == 'Kevin McKidd':
                    sta4 = '246'
                elif STAR4 == 'Steve Buscemi':
                    sta4 = '247'
                elif STAR4 == 'Slavko Stimac':
                    sta4 = '248'
                elif STAR4 == 'Abdel Ahmed Ghili':
                    sta4 = '249'
                elif STAR4 == 'Farida Jalal':
                    sta4 = '250'
                elif STAR4 == 'Hanno Pöschl':
                    sta4 = '251'
                elif STAR4 == 'Jean-Pierre Lorit':
                    sta4 = '252'
                elif STAR4 == 'Faye Wong':
                    sta4 = '253'
                elif STAR4 == 'Richard Attenborough':
                    sta4 = '254'
                elif STAR4 == 'Philip King':
                    sta4 = '255'
                elif STAR4 == 'You Ge':
                    sta4 = '256'
                elif STAR4 == 'Cuifen Cao':
                    sta4 = '257'
                elif STAR4 == 'Josh Charles':
                    sta4 = '258'
                elif STAR4 == 'Jerry O\'Connell':
                    sta4 = '259'
                elif STAR4 == 'Keith David':
                    sta4 = '260'
                elif STAR4 == 'Aurore Clément':
                    sta4 = '261'
                elif STAR4 == 'Gorô Naya':
                    sta4 = '262'
                elif STAR4 == 'Richard Masur':
                    sta4 = '263'
                elif STAR4 == 'Eleanor David':
                    sta4 = '264'
                elif STAR4 == 'Miguel Ángel Fuentes':
                    sta4 = '265'
                elif STAR4 == 'Börje Ahlstedt':
                    sta4 = '266'
                elif STAR4 == 'Edward James Olmos':
                    sta4 = '267'
                elif STAR4 == 'John Gielgud':
                    sta4 = '268'
                elif STAR4 == 'Terry Gilliam':
                    sta4 = '269'
                elif STAR4 == 'John Savage':
                    sta4 = '270'
                elif STAR4 == 'Carl Weathers':
                    sta4 = '271'
                elif STAR4 == 'Robert Duvall':
                    sta4 = '272'
                elif STAR4 == 'Hardy Krüger':
                    sta4 = '273'
                elif STAR4 == 'Oleg Yankovskiy':
                    sta4 = '274'
                elif STAR4 == 'Perry Lopez':
                    sta4 = '275'
                elif STAR4 == 'John Hillerman':
                    sta4 = '276'
                elif STAR4 == 'Ingrid Thulin':
                    sta4 = '277'
                elif STAR4 == 'Vladislav Dvorzhetskiy':
                    sta4 = '278'
                elif STAR4 == 'Cathy Rosier':
                    sta4 = '279'
                elif STAR4 == 'J.D. Cannon':
                    sta4 = '280'
                elif STAR4 == 'Nikolay Sergeev':
                    sta4 = '281'
                elif STAR4 == 'Samia Kerbash':
                    sta4 = '282'
                elif STAR4 == 'José Baviera':
                    sta4 = '283'
                elif STAR4 == 'Wesley Addy':
                    sta4 = '284'
                elif STAR4 == 'Yûnosuke Itô':
                    sta4 = '285'
                elif STAR4 == 'Lee Marvin':
                    sta4 = '286'
                elif STAR4 == 'Evgeniy Zharikov':
                    sta4 = '287'
                elif STAR4 == 'Birgitta Pettersson':
                    sta4 = '288'
                elif STAR4 == 'Dick York':
                    sta4 = '289'
                elif STAR4 == 'Guy Decomble':
                    sta4 = '290'
                elif STAR4 == 'Haya Harareet':
                    sta4 = '291'
                elif STAR4 == 'Kamatari Fujiwara':
                    sta4 = '292'
                elif STAR4 == 'Dorian Gray':
                    sta4 = '293'
                elif STAR4 == 'Sessue Hayakawa':
                    sta4 = '294'
                elif STAR4 == 'Rod Steiger':
                    sta4 = '295'
                elif STAR4 == 'Folco Lulli':
                    sta4 = '296'
                elif STAR4 == 'Porter Hall':
                    sta4 = '297'
                elif STAR4 == 'Margaret Wycherly':
                    sta4 = '298'
                elif STAR4 == 'Trevor Howard':
                    sta4 = '299'
                elif STAR4 == 'Moira Shearer':
                    sta4 = '300'
                elif STAR4 == 'Joseph Schildkraut':
                    sta4 = '301'
                elif STAR4 == 'Judith Anderson':
                    sta4 = '302'
                elif STAR4 == 'Edward Arnold':
                    sta4 = '303'
                elif STAR4 == 'Vivien Leigh':
                    sta4 = '304'
                elif STAR4 == 'Erich von Stroheim':
                    sta4 = '305'
                elif STAR4 == 'Roscoe Karns':
                    sta4 = '306'
                elif STAR4 == 'Maurice Schutz':
                    sta4 = '307'
                elif STAR4 == 'Harry Crocker':
                    sta4 = '308'
                elif STAR4 == 'Bodil Rosing':
                    sta4 = '309'
                elif STAR4 == 'Glen Cavender':
                    sta4 = '310'
                elif STAR4 == 'Lil Dagover':
                    sta4 = '311'
                elif STAR4 == 'Richard Dormer':
                    sta4 = '312'
                elif STAR4 == 'Prakash Belawadi':
                    sta4 = '313'
                elif STAR4 == 'Kareena Kapoor':
                    sta4 = '314'
                elif STAR4 == 'Taapsee Pannu':
                    sta4 = '315'
                elif STAR4 == 'J.K. Simmons':
                    sta4 = '316'
                elif STAR4 == 'Sunny Pawar':
                    sta4 = '317'
                elif STAR4 == 'Kate Mara':
                    sta4 = '318'
                elif STAR4 == 'Jason Bateman':
                    sta4 = '319'
                elif STAR4 == 'Sathyaraj':
                    sta4 = '320'
                elif STAR4 == 'James Marsden':
                    sta4 = '321'
                elif STAR4 == 'Julia Roberts':
                    sta4 = '322'
                elif STAR4 == 'Vijay Raaz':
                    sta4 = '323'
                elif STAR4 == 'Jimmy Sheirgill':
                    sta4 = '324'
                elif STAR4 == 'Kaitlyn Dever':
                    sta4 = '325'
                elif STAR4 == 'Oka Antara':
                    sta4 = '326'
                elif STAR4 == 'Allen Leech':
                    sta4 = '327'
                elif STAR4 == 'Zoe Saldana':
                    sta4 = '328'
                elif STAR4 == 'Dave Bautista':
                    sta4 = '329'
                elif STAR4 == 'Rooney Mara':
                    sta4 = '330'
                elif STAR4 == 'Ben Hardy':
                    sta4 = '331'
                elif STAR4 == 'Domhnall Gleeson':
                    sta4 = '332'
                elif STAR4 == 'Paul Rudd':
                    sta4 = '333'
                elif STAR4 == 'Milhem Cortaz':
                    sta4 = '334'
                elif STAR4 == 'Derek Jacobi':
                    sta4 = '335'
                elif STAR4 == 'Bryce Dallas Howard':
                    sta4 = '336'
                elif STAR4 == 'Ed Skrein':
                    sta4 = '337'
                elif STAR4 == 'Merila Zare\'i':
                    sta4 = '338'
                elif STAR4 == 'Dibyendu Bhattacharya':
                    sta4 = '339'
                elif STAR4 == 'Ka Tung Lam':
                    sta4 = '340'
                elif STAR4 == 'Katie A. Keane':
                    sta4 = '341'
                elif STAR4 == 'Baris Bagci':
                    sta4 = '342'
                elif STAR4 == 'Winona Ryder':
                    sta4 = '343'
                elif STAR4 == 'Jeremy Renner':
                    sta4 = '344'
                elif STAR4 == 'Gena Rowlands':
                    sta4 = '345'
                elif STAR4 == 'Steve Zahn':
                    sta4 = '346'
                elif STAR4 == 'Brian Howe':
                    sta4 = '347'
                elif STAR4 == 'Kagiso Kuypers':
                    sta4 = '348'
                elif STAR4 == 'Julia Stiles':
                    sta4 = '349'
                elif STAR4 == 'Jin-mo Joo':
                    sta4 = '350'
                elif STAR4 == 'Clive Owen':
                    sta4 = '351'
                elif STAR4 == 'Marie-Josée Croze':
                    sta4 = '352'
                elif STAR4 == 'Safak Sezer':
                    sta4 = '353'
                elif STAR4 == 'Patton Oswalt':
                    sta4 = '354'
                elif STAR4 == 'Jeffrey Wright':
                    sta4 = '355'
                elif STAR4 == 'Daryl Hannah':
                    sta4 = '356'
                elif STAR4 == 'Nataliya Vdovina':
                    sta4 = '357'
                elif STAR4 == 'Kim Young-Min':
                    sta4 = '358'
                elif STAR4 == 'Mabel Rivera':
                    sta4 = '359'
                elif STAR4 == 'Paul Giamatti':
                    sta4 = '360'
                elif STAR4 == 'Jaya Bachchan':
                    sta4 = '361'
                elif STAR4 == 'Anthony Chau-Sang Wong':
                    sta4 = '362'
                elif STAR4 == 'Keira Knightley':
                    sta4 = '363'
                elif STAR4 == 'Jessica Lange':
                    sta4 = '364'
                elif STAR4 == 'Jason Lee':
                    sta4 = '365'
                elif STAR4 == 'Song Wok-suk':
                    sta4 = '366'
                elif STAR4 == 'Harriet Andersson':
                    sta4 = '367'
                elif STAR4 == 'Altan Erkekli':
                    sta4 = '368'
                elif STAR4 == 'Holmes Osborne':
                    sta4 = '369'
                elif STAR4 == 'Philip Seymour Hoffman':
                    sta4 = '370'
                elif STAR4 == 'Peter Stormare':
                    sta4 = '371'
                elif STAR4 == 'Joseph A. Carpenter':
                    sta4 = '372'
                elif STAR4 == 'Masaaki Ôkura':
                    sta4 = '373'
                elif STAR4 == 'Paprika Steen':
                    sta4 = '374'
                elif STAR4 == 'Soia Lira':
                    sta4 = '375'
                elif STAR4 == 'Vin Diesel':
                    sta4 = '376'
                elif STAR4 == 'Moritz Bleibtreu':
                    sta4 = '377'
                elif STAR4 == 'John Ritter':
                    sta4 = '378'
                elif STAR4 == 'Claire Rushbrook':
                    sta4 = '379'
                elif STAR4 == 'Joseph Melito':
                    sta4 = '380'
                elif STAR4 == 'Kôichi Yamadera':
                    sta4 = '381'
                elif STAR4 == 'William Hickey':
                    sta4 = '382'
                elif STAR4 == 'Stephen Tobolowsky':
                    sta4 = '383'
                elif STAR4 == 'Enrique Castillo':
                    sta4 = '384'
                elif STAR4 == 'Gabrielle Anwar':
                    sta4 = '385'
                elif STAR4 == 'Linda Larkin':
                    sta4 = '386'
                elif STAR4 == 'Walter Matthau':
                    sta4 = '387'
                elif STAR4 == 'Jesse Corti':
                    sta4 = '388'
                elif STAR4 == 'Rodney A. Grant':
                    sta4 = '389'
                elif STAR4 == 'Richard Edson':
                    sta4 = '390'
                elif STAR4 == 'Gerald R. Molen':
                    sta4 = '391'
                elif STAR4 == 'Tesshô Genda':
                    sta4 = '392'
                elif STAR4 == 'Chris Sarandon':
                    sta4 = '393'
                elif STAR4 == 'Curt Bois':
                    sta4 = '394'
                elif STAR4 == 'Stanislas Carré de Malberg':
                    sta4 = '395'
                elif STAR4 == 'Minori Terada':
                    sta4 = '396'
                elif STAR4 == 'Paul Winfield':
                    sta4 = '397'
                elif STAR4 == 'Roshan Seth':
                    sta4 = '398'
                elif STAR4 == 'Jinpachi Nezu':
                    sta4 = '399'
                elif STAR4 == 'Jack Warden':
                    sta4 = '400'
                elif STAR4 == 'Carol Kane':
                    sta4 = '401'
                elif STAR4 == 'Lorraine Gary':
                    sta4 = '402'
                elif STAR4 == 'Sully Boyar':
                    sta4 = '403'
                elif STAR4 == 'Peter Boyle':
                    sta4 = '404'
                elif STAR4 == 'Don Gordon':
                    sta4 = '405'
                elif STAR4 == 'Lee J. Cobb':
                    sta4 = '406'
                elif STAR4 == 'John Matthews':
                    sta4 = '407'
                elif STAR4 == 'Ben Johnson':
                    sta4 = '408'
                elif STAR4 == 'Molly Picon':
                    sta4 = '409'
                elif STAR4 == 'Enzo Tarascio':
                    sta4 = '410'
                elif STAR4 == 'Strother Martin':
                    sta4 = '411'
                elif STAR4 == 'Sidney Blackmer':
                    sta4 = '412'
                elif STAR4 == 'Maurice Evans':
                    sta4 = '413'
                elif STAR4 == 'William Daniels':
                    sta4 = '414'
                elif STAR4 == 'Sandy Dennis':
                    sta4 = '415'
                elif STAR4 == 'Richard Haydn':
                    sta4 = '416'
                elif STAR4 == 'Wolfgang Lukschy':
                    sta4 = '417'
                elif STAR4 == 'Sandra Milo':
                    sta4 = '418'
                elif STAR4 == 'Guylaine Schlumberger':
                    sta4 = '419'
                elif STAR4 == 'George C. Scott':
                    sta4 = '420'
                elif STAR4 == 'Yvonne Furneaux':
                    sta4 = '421'
                elif STAR4 == 'Angie Dickinson':
                    sta4 = '422'
                elif STAR4 == 'Arthur O\'Connell':
                    sta4 = '423'
                elif STAR4 == 'Joseph Calleia':
                    sta4 = '424'
                elif STAR4 == 'Jack Carson':
                    sta4 = '425'
                elif STAR4 == 'Martin Milner':
                    sta4 = '426'
                elif STAR4 == 'Jay C. Flippen':
                    sta4 = '427'
                elif STAR4 == 'James Gleason':
                    sta4 = '428'
                elif STAR4 == 'Aldo Silvani':
                    sta4 = '429'
                elif STAR4 == 'Charles Vanel':
                    sta4 = '430'
                elif STAR4 == 'Robert Strauss':
                    sta4 = '431'
                elif STAR4 == 'Hartley Power':
                    sta4 = '432'
                elif STAR4 == 'Karl Malden':
                    sta4 = '433'
                elif STAR4 == 'Carl Benton Reid':
                    sta4 = '434'
                elif STAR4 == 'Joan Greenwood':
                    sta4 = '435'
                elif STAR4 == 'Dick Hogan':
                    sta4 = '436'
                elif STAR4 == 'Rhonda Fleming':
                    sta4 = '437'
                elif STAR4 == 'Joyce Carey':
                    sta4 = '438'
                elif STAR4 == 'Vincent Price':
                    sta4 = '439'
                elif STAR4 == 'Teresa Wright':
                    sta4 = '440'
                elif STAR4 == 'Peter Lorre':
                    sta4 = '441'
                elif STAR4 == 'Charley Grapewin':
                    sta4 = '442'
                elif STAR4 == 'Richard Thorpe':
                    sta4 = '443'
                elif STAR4 == 'Mila Parély':
                    sta4 = '444'
                elif STAR4 == 'Nat Pendleton':
                    sta4 = '445'
                elif STAR4 == 'Arnold Lucy':
                    sta4 = '446'
                elif STAR4 == 'Ivan Bobrov':
                    sta4 = '447'
                elif STAR4 == 'Jamie Lee Curtis':
                    sta4 = '448'
                elif STAR4 == 'Saswata Chatterjee':
                    sta4 = '449'
                elif STAR4 == 'Mayu Matsuoka':
                    sta4 = '450'
                elif STAR4 == 'Azhy Robertson':
                    sta4 = '451'
                elif STAR4 == 'Amira Casar':
                    sta4 = '452'
                elif STAR4 == 'Sharon Percy':
                    sta4 = '453'
                elif STAR4 == 'Bob Balaban':
                    sta4 = '454'
                elif STAR4 == 'Rachel House':
                    sta4 = '455'
                elif STAR4 == 'Annalise Basso':
                    sta4 = '456'
                elif STAR4 == 'Jack Reynor':
                    sta4 = '457'
                elif STAR4 == 'Riz Ahmed':
                    sta4 = '458'
                elif STAR4 == 'Taika Waititi':
                    sta4 = '459'
                elif STAR4 == 'Michael Stuhlbarg':
                    sta4 = '460'
                elif STAR4 == 'Ariane Labed':
                    sta4 = '461'
                elif STAR4 == 'James McAvoy':
                    sta4 = '462'
                elif STAR4 == 'Ahmet Mümtaz Taylan':
                    sta4 = '463'
                elif STAR4 == 'James Cromwell':
                    sta4 = '464'
                elif STAR4 == 'Brendan Gleeson':
                    sta4 = '465'
                elif STAR4 == 'Alexandre Tharaud':
                    sta4 = '466'
                elif STAR4 == 'Harvey Keitel':
                    sta4 = '467'
                elif STAR4 == 'Reda Kateb':
                    sta4 = '468'
                elif STAR4 == 'Rosie Shaw':
                    sta4 = '469'
                elif STAR4 == 'Henrik Dahl':
                    sta4 = '470'
                elif STAR4 == 'Nathalie Boltt':
                    sta4 = '471'
                elif STAR4 == 'Mark Margolis':
                    sta4 = '472'
                elif STAR4 == 'Dara Singh':
                    sta4 = '473'
                elif STAR4 == 'Elijah Smith':
                    sta4 = '474'
                elif STAR4 == 'Alexandru Potocean':
                    sta4 = '475'
                elif STAR4 == 'Leonard Nimoy':
                    sta4 = '476'
                elif STAR4 == 'Elizabeth Berrington':
                    sta4 = '477'
                elif STAR4 == 'Ellen Crawford':
                    sta4 = '478'
                elif STAR4 == 'Ryô Kase':
                    sta4 = '479'
                elif STAR4 == 'Kim Uylenbroek':
                    sta4 = '480'
                elif STAR4 == 'Jason Schwartzman':
                    sta4 = '481'
                elif STAR4 == 'Émile Vallée':
                    sta4 = '482'
                elif STAR4 == 'Kad Merad':
                    sta4 = '483'
                elif STAR4 == 'Jeff Bridges':
                    sta4 = '484'
                elif STAR4 == 'Lucy Davis':
                    sta4 = '485'
                elif STAR4 == 'Zarah Jane McKenzie':
                    sta4 = '486'
                elif STAR4 == 'Emmy Rossum':
                    sta4 = '487'
                elif STAR4 == 'Richard Griffiths':
                    sta4 = '488'
                elif STAR4 == 'Ziyi Zhang':
                    sta4 = '489'
                elif STAR4 == 'Leonor Watling':
                    sta4 = '490'
                elif STAR4 == 'Georges Siatidis':
                    sta4 = '491'
                elif STAR4 == 'Beau Billingslea':
                    sta4 = '492'
                elif STAR4 == 'María Mercedes Villagra':
                    sta4 = '493'
                elif STAR4 == 'Frances McDormand':
                    sta4 = '494'
                elif STAR4 == 'Jeanne Bates':
                    sta4 = '495'
                elif STAR4 == 'Tim Allen':
                    sta4 = '496'
                elif STAR4 == 'Luis Guzmán':
                    sta4 = '497'
                elif STAR4 == 'Shigeru Muroi':
                    sta4 = '498'
                elif STAR4 == 'Julian Arahanga':
                    sta4 = '499'
                elif STAR4 == 'Val Kilmer':
                    sta4 = '500'
                elif STAR4 == 'Benoît Régent':
                    sta4 = '501'
                elif STAR4 == 'Osamu Saka':
                    sta4 = '502'
                elif STAR4 == 'John Leguizamo':
                    sta4 = '503'
                elif STAR4 == 'Anthony Michael Hall':
                    sta4 = '504'
                elif STAR4 == 'Kirsten Sheridan':
                    sta4 = '505'
                elif STAR4 == 'Claire Bloom':
                    sta4 = '506'
                elif STAR4 == 'Charles Martin Smith':
                    sta4 = '507'
                elif STAR4 == 'Barbara Hershey':
                    sta4 = '508'
                elif STAR4 == 'Katherine Helmond':
                    sta4 = '509'
                elif STAR4 == 'Kimberly Stringer':
                    sta4 = '510'
                elif STAR4 == 'Scott Schwartz':
                    sta4 = '511'
                elif STAR4 == 'John Candy':
                    sta4 = '512'
                elif STAR4 == 'Michael Murphy':
                    sta4 = '513'
                elif STAR4 == 'Leland Palmer':
                    sta4 = '514'
                elif STAR4 == 'Gaylen Ross':
                    sta4 = '515'
                elif STAR4 == 'Martin Balsam':
                    sta4 = '516'
                elif STAR4 == 'Juan Ferrara':
                    sta4 = '517'
                elif STAR4 == 'Armando Brancia':
                    sta4 = '518'
                elif STAR4 == 'Bulle Ogier':
                    sta4 = '519'
                elif STAR4 == 'Del Negro':
                    sta4 = '520'
                elif STAR4 == 'Cyril Cusack':
                    sta4 = '521'
                elif STAR4 == 'Michael Strong':
                    sta4 = '522'
                elif STAR4 == 'Edmond O\'Brien':
                    sta4 = '523'
                elif STAR4 == 'Marilyn Eastman':
                    sta4 = '524'
                elif STAR4 == 'John Castle':
                    sta4 = '525'
                elif STAR4 == 'Lee Grant':
                    sta4 = '526'
                elif STAR4 == 'James Coburn':
                    sta4 = '527'
                elif STAR4 == 'Angela Lansbury':
                    sta4 = '528'
                elif STAR4 == 'Charles Laughton':
                    sta4 = '529'
                elif STAR4 == 'Dominique Blanchar':
                    sta4 = '530'
                elif STAR4 == 'Pierre Barbaud':
                    sta4 = '531'
                elif STAR4 == 'Edward G. Robinson':
                    sta4 = '532'
                elif STAR4 == 'Ward Bond':
                    sta4 = '533'
                elif STAR4 == 'Burl Ives':
                    sta4 = '534'
                elif STAR4 == 'Lloyd Bridges':
                    sta4 = '535'
                elif STAR4 == 'Leo G. Carroll':
                    sta4 = '536'
                elif STAR4 == 'Victoria Horne':
                    sta4 = '537'
                elif STAR4 == 'Gene Lockhart':
                    sta4 = '538'
                elif STAR4 == 'Louis Calhern':
                    sta4 = '539'
                elif STAR4 == 'Martha Vickers':
                    sta4 = '540'
                elif STAR4 == 'Howard Da Silva':
                    sta4 = '541'
                elif STAR4 == 'Ruth Hussey':
                    sta4 = '542'
                elif STAR4 == 'Basil Rathbone':
                    sta4 = '543'
                elif STAR4 == 'Harpo Marx':
                    sta4 = '544'
                elif STAR4 == 'Bruce Cabot':
                    sta4 = '545'
                elif STAR4 == 'Roscoe Ates':
                    sta4 = '546'
                elif STAR4 == 'Greta Schröder':
                    sta4 = '547'
                elif STAR4 == 'Jeremy Strong':
                    sta4 = '548'
                elif STAR4 == 'Shishir Sharma':
                    sta4 = '549'
                elif STAR4 == 'Lauren Ridloff':
                    sta4 = '550'
                elif STAR4 == 'Mina Sadati':
                    sta4 = '551'
                elif STAR4 == 'Tom Hardy':
                    sta4 = '552'
                elif STAR4 == 'Edoardo Leo':
                    sta4 = '553'
                elif STAR4 == 'Kevin Costner':
                    sta4 = '554'
                elif STAR4 == 'Sally Hawkins':
                    sta4 = '555'
                elif STAR4 == 'Diljit Dosanjh':
                    sta4 = '556'
                elif STAR4 == 'Ralph Fiennes':
                    sta4 = '557'
                elif STAR4 == 'Disha Patani':
                    sta4 = '558'
                elif STAR4 == 'Lucas Hedges':
                    sta4 = '559'
                elif STAR4 == 'Mikkel Boe Følsgaard':
                    sta4 = '560'
                elif STAR4 == 'Donnie Yen':
                    sta4 = '561'
                elif STAR4 == 'Scarlett Johansson':
                    sta4 = '562'
                elif STAR4 == 'Walton Goggins':
                    sta4 = '563'
                elif STAR4 == 'Eliza Scanlen':
                    sta4 = '564'
                elif STAR4 == 'Robert Gulaczyk':
                    sta4 = '565'
                elif STAR4 == 'Paddy Considine':
                    sta4 = '566'
                elif STAR4 == 'Pauline Burlet':
                    sta4 = '567'
                elif STAR4 == 'Carlo Buccirosso':
                    sta4 = '568'
                elif STAR4 == 'Lillete Dubey':
                    sta4 = '569'
                elif STAR4 == 'Dolly Ahluwalia':
                    sta4 = '570'
                elif STAR4 == 'Jamie Chung':
                    sta4 = '571'
                elif STAR4 == 'Lydia Wilson':
                    sta4 = '572'
                elif STAR4 == 'Priya Anand':
                    sta4 = '573'
                elif STAR4 == 'Masahiko Nishimura':
                    sta4 = '574'
                elif STAR4 == 'Tony Hale':
                    sta4 = '575'
                elif STAR4 == 'Donald Sutherland':
                    sta4 = '576'
                elif STAR4 == 'Bill Murray':
                    sta4 = '577'
                elif STAR4 == 'Craig Ferguson':
                    sta4 = '578'
                elif STAR4 == 'Ho-jin Chun':
                    sta4 = '579'
                elif STAR4 == 'Catherine Keener':
                    sta4 = '580'
                elif STAR4 == 'Hee-won Kim':
                    sta4 = '581'
                elif STAR4 == 'Neil Brown Jr.':
                    sta4 = '582'
                elif STAR4 == 'Je-mun Yun':
                    sta4 = '583'
                elif STAR4 == 'Yoo-Jeong Kim':
                    sta4 = '584'
                elif STAR4 == 'Ken Stott':
                    sta4 = '585'
                elif STAR4 == 'Lena Endre':
                    sta4 = '586'
                elif STAR4 == 'Lars Ranthe':
                    sta4 = '587'
                elif STAR4 == 'Leland Orser':
                    sta4 = '588'
                elif STAR4 == 'Zac Mattoon O\'Brien':
                    sta4 = '589'
                elif STAR4 == 'Gerard Hendrick':
                    sta4 = '590'
                elif STAR4 == 'Andy Serkis':
                    sta4 = '591'
                elif STAR4 == 'Nursel Köse':
                    sta4 = '592'
                elif STAR4 == 'Saoirse Ronan':
                    sta4 = '593'
                elif STAR4 == 'Michelle Rodriguez':
                    sta4 = '594'
                elif STAR4 == 'Linh Dan Pham':
                    sta4 = '595'
                elif STAR4 == 'Rudy Youngblood':
                    sta4 = '596'
                elif STAR4 == 'Greg Kinnear':
                    sta4 = '597'
                elif STAR4 == 'Bill Nighy':
                    sta4 = '598'
                elif STAR4 == 'Julia Ormond':
                    sta4 = '599'
                elif STAR4 == 'Kirron Kher':
                    sta4 = '600'
                elif STAR4 == 'Tessa Mitchell':
                    sta4 = '601'
                elif STAR4 == 'Aya Okamoto':
                    sta4 = '602'
                elif STAR4 == 'Alan Tudyk':
                    sta4 = '603'
                elif STAR4 == 'Linda Zilliacus':
                    sta4 = '604'
                elif STAR4 == 'Ryan Gosling':
                    sta4 = '605'
                elif STAR4 == 'Mercedes Morán':
                    sta4 = '606'
                elif STAR4 == 'Lyubov Agapova':
                    sta4 = '607'
                elif STAR4 == 'Monica Viegas':
                    sta4 = '608'
                elif STAR4 == 'Kim Tae-Woo':
                    sta4 = '609'
                elif STAR4 == 'JB Blanc':
                    sta4 = '610'
                elif STAR4 == 'Wiley Wiggins':
                    sta4 = '611'
                elif STAR4 == 'Ryan Hurst':
                    sta4 = '612'
                elif STAR4 == 'Chen Chang':
                    sta4 = '613'
                elif STAR4 == 'Antonia San Juan':
                    sta4 = '614'
                elif STAR4 == 'Lari White':
                    sta4 = '615'
                elif STAR4 == 'David Della Rocco':
                    sta4 = '616'
                elif STAR4 == 'Diane Venora':
                    sta4 = '617'
                elif STAR4 == 'Chris Owen':
                    sta4 = '618'
                elif STAR4 == 'Cameron Diaz':
                    sta4 = '619'
                elif STAR4 == 'Kathy Bates':
                    sta4 = '620'
                elif STAR4 == 'Susumu Terajima':
                    sta4 = '621'
                elif STAR4 == 'Gore Vidal':
                    sta4 = '622'
                elif STAR4 == 'James Rebhorn':
                    sta4 = '623'
                elif STAR4 == 'Jean-Marc Barr':
                    sta4 = '624'
                elif STAR4 == 'Patricia Arquette':
                    sta4 = '625'
                elif STAR4 == 'Mary Steenburgen':
                    sta4 = '626'
                elif STAR4 == 'Sam Elliott':
                    sta4 = '627'
                elif STAR4 == 'Patrick Renna':
                    sta4 = '628'
                elif STAR4 == 'Christopher Reeve':
                    sta4 = '629'
                elif STAR4 == 'Greg Cruttwell':
                    sta4 = '630'
                elif STAR4 == 'Francis Capra':
                    sta4 = '631'
                elif STAR4 == 'Eric Radomski':
                    sta4 = '632'
                elif STAR4 == 'Philip Chan':
                    sta4 = '633'
                elif STAR4 == 'Alan Randolph Scott':
                    sta4 = '634'
                elif STAR4 == 'Kalina Jedrusik':
                    sta4 = '635'
                elif STAR4 == 'Lloyd Avery II':
                    sta4 = '636'
                elif STAR4 == 'Frances Sternhagen':
                    sta4 = '637'
                elif STAR4 == 'Ruth Nelson':
                    sta4 = '638'
                elif STAR4 == 'Kappei Yamaguchi':
                    sta4 = '639'
                elif STAR4 == 'Morgan Freeman':
                    sta4 = '640'
                elif STAR4 == 'Kong Chu':
                    sta4 = '641'
                elif STAR4 == 'Thomas F. Wilson':
                    sta4 = '642'
                elif STAR4 == 'Brad Dourif':
                    sta4 = '643'
                elif STAR4 == 'Elpidia Carrillo':
                    sta4 = '644'
                elif STAR4 == 'Kassie Wesley DePaiva':
                    sta4 = '645'
                elif STAR4 == 'Jeffrey Jones':
                    sta4 = '646'
                elif STAR4 == 'Nicoletta Braschi':
                    sta4 = '647'
                elif STAR4 == 'Corey Feldman':
                    sta4 = '648'
                elif STAR4 == 'Margaret Avery':
                    sta4 = '649'
                elif STAR4 == 'Ally Sheedy':
                    sta4 = '650'
                elif STAR4 == 'Julian Sands':
                    sta4 = '651'
                elif STAR4 == 'Harold Ramis':
                    sta4 = '652'
                elif STAR4 == 'Dennis Quaid':
                    sta4 = '653'
                elif STAR4 == 'Sandra Bernhard':
                    sta4 = '654'
                elif STAR4 == 'Dee Wallace':
                    sta4 = '655'
                elif STAR4 == 'Justin Henry':
                    sta4 = '656'
                elif STAR4 == 'Linda Manz':
                    sta4 = '657'
                elif STAR4 == 'Bill McKinney':
                    sta4 = '658'
                elif STAR4 == 'Saeed Jaffrey':
                    sta4 = '659'
                elif STAR4 == 'Jean Topart':
                    sta4 = '660'
                elif STAR4 == 'Alan Badel':
                    sta4 = '661'
                elif STAR4 == 'Ramon Bieri':
                    sta4 = '662'
                elif STAR4 == 'Joel Grey':
                    sta4 = '663'
                elif STAR4 == 'Roy Kinnear':
                    sta4 = '664'
                elif STAR4 == 'John McGiver':
                    sta4 = '665'
                elif STAR4 == 'Efrem Zimbalist Jr.':
                    sta4 = '666'
                elif STAR4 == 'Katharine Houghton':
                    sta4 = '667'
                elif STAR4 == 'Gene Hackman':
                    sta4 = '668'
                elif STAR4 == 'Wilfrid Hyde-White':
                    sta4 = '669'
                elif STAR4 == 'Glynis Johns':
                    sta4 = '670'
                elif STAR4 == 'Darryl F. Zanuck':
                    sta4 = '671'
                elif STAR4 == 'Vanna Urbino':
                    sta4 = '672'
                elif STAR4 == 'Michael Redgrave':
                    sta4 = '673'
                elif STAR4 == 'Henri-Jacques Huet':
                    sta4 = '674'
                elif STAR4 == 'Joanne Dru':
                    sta4 = '675'
                elif STAR4 == 'Lionel Barrymore':
                    sta4 = '676'
                elif STAR4 == 'Dolores Moran':
                    sta4 = '677'
                elif STAR4 == 'Henry Travers':
                    sta4 = '678'
                elif STAR4 == 'John Carradine':
                    sta4 = '679'
                elif STAR4 == 'May Whitty':
                    sta4 = '680'
                elif STAR4 == 'Walter Catlett':
                    sta4 = '681'
                elif STAR4 == 'Valerie Hobson':
                    sta4 = '682'
                elif STAR4 == 'Zeppo Marx':
                    sta4 = '683'
                elif STAR4 == 'Karen Morley':
                    sta4 = '684'
                elif STAR4 == 'John Boles':
                    sta4 = '685'
                elif STAR4 == 'Carlos Peralta':
                    sta4 = '686'
                elif STAR4 == 'Ian Hart':
                    sta4 = '687'
                elif STAR4 == 'Julian Dennison':
                    sta4 = '688'
                elif STAR4 == 'Teo Briones':
                    sta4 = '689'
                elif STAR4 == 'Simon Pegg':
                    sta4 = '690'
                elif STAR4 == 'Ida Engvoll':
                    sta4 = '691'
                elif STAR4 == 'Cori Gonzalez-Macuer':
                    sta4 = '692'
                elif STAR4 == 'Nanako Matsushima':
                    sta4 = '693'
                elif STAR4 == 'Sophie Perry':
                    sta4 = '694'
                elif STAR4 == 'Laura Dern':
                    sta4 = '695'
                elif STAR4 == 'Nick Offerman':
                    sta4 = '696'
                elif STAR4 == 'Andrea Riseborough':
                    sta4 = '697'
                elif STAR4 == 'Aurélien Recoing':
                    sta4 = '698'
                elif STAR4 == 'Amrita Puri':
                    sta4 = '699'
                elif STAR4 == 'Geert Van Rampelberg':
                    sta4 = '700'
                elif STAR4 == 'Kumud Mishra':
                    sta4 = '701'
                elif STAR4 == 'Bob Odenkirk':
                    sta4 = '702'
                elif STAR4 == 'Sarah Silverman':
                    sta4 = '703'
                elif STAR4 == 'Marion Cotillard':
                    sta4 = '704'
                elif STAR4 == 'Lucy Liu':
                    sta4 = '705'
                elif STAR4 == 'Kurt Fuller':
                    sta4 = '706'
                elif STAR4 == 'Elizabeth Banks':
                    sta4 = '707'
                elif STAR4 == 'Orto Ignatiussen':
                    sta4 = '708'
                elif STAR4 == 'Benedict Cumberbatch':
                    sta4 = '709'
                elif STAR4 == 'Andrew Adote':
                    sta4 = '710'
                elif STAR4 == 'Kevin Bacon':
                    sta4 = '711'
                elif STAR4 == 'Ed Helms':
                    sta4 = '712'
                elif STAR4 == 'Judi Dench':
                    sta4 = '713'
                elif STAR4 == 'Jacki Weaver':
                    sta4 = '714'
                elif STAR4 == 'Alan Arkin':
                    sta4 = '715'
                elif STAR4 == 'Chloë Grace Moretz':
                    sta4 = '716'
                elif STAR4 == 'Tomoko Yamaguchi':
                    sta4 = '717'
                elif STAR4 == 'Sam Rockwell':
                    sta4 = '718'
                elif STAR4 == 'Tôru Furuya':
                    sta4 = '719'
                elif STAR4 == 'Gattlin Griffith':
                    sta4 = '720'
                elif STAR4 == 'Anthony Edwards':
                    sta4 = '721'
                elif STAR4 == 'Ayami Kakiuchi':
                    sta4 = '722'
                elif STAR4 == 'Yû Kashii':
                    sta4 = '723'
                elif STAR4 == 'Andrew Shim':
                    sta4 = '724'
                elif STAR4 == 'Sonoya Mizuno':
                    sta4 = '725'
                elif STAR4 == 'Neeral Mulchandani':
                    sta4 = '726'
                elif STAR4 == 'Natalie Dessay':
                    sta4 = '727'
                elif STAR4 == 'Donna Murphy':
                    sta4 = '728'
                elif STAR4 == 'Halina Reijn':
                    sta4 = '729'
                elif STAR4 == 'Randy Quaid':
                    sta4 = '730'
                elif STAR4 == 'Logan Lerman':
                    sta4 = '731'
                elif STAR4 == 'Karina Arroyave':
                    sta4 = '732'
                elif STAR4 == 'Siu-Lung Leung':
                    sta4 = '733'
                elif STAR4 == 'Brian Cox':
                    sta4 = '734'
                elif STAR4 == 'John Sharian':
                    sta4 = '735'
                elif STAR4 == 'Clifton Powell':
                    sta4 = '736'
                elif STAR4 == 'Anna Faris':
                    sta4 = '737'
                elif STAR4 == 'Eric Sykes':
                    sta4 = '738'
                elif STAR4 == 'Radha Mitchell':
                    sta4 = '739'
                elif STAR4 == 'Jennifer Saunders':
                    sta4 = '740'
                elif STAR4 == 'William Atherton':
                    sta4 = '741'
                elif STAR4 == 'Anne-Marie Duff':
                    sta4 = '742'
                elif STAR4 == 'Florian Lukas':
                    sta4 = '743'
                elif STAR4 == 'Sarah Bolger':
                    sta4 = '744'
                elif STAR4 == 'Dianne Wiest':
                    sta4 = '745'
                elif STAR4 == 'Tilda Swinton':
                    sta4 = '746'
                elif STAR4 == 'Eric Bana':
                    sta4 = '747'
                elif STAR4 == 'Liam Aiken':
                    sta4 = '748'
                elif STAR4 == 'Wotan Wilke Möhring':
                    sta4 = '749'
                elif STAR4 == 'Jamie Draven':
                    sta4 = '750'
                elif STAR4 == 'Theodore Liscinski':
                    sta4 = '751'
                elif STAR4 == 'Matt Damon':
                    sta4 = '752'
                elif STAR4 == 'Wendee Lee':
                    sta4 = '753'
                elif STAR4 == 'Tim Blake Nelson':
                    sta4 = '754'
                elif STAR4 == 'Matthew Edison':
                    sta4 = '755'
                elif STAR4 == 'Isaac Hayes':
                    sta4 = '756'
                elif STAR4 == 'Ajay Naidu':
                    sta4 = '757'
                elif STAR4 == 'Dylan Baker':
                    sta4 = '758'
                elif STAR4 == 'Tom Berenger':
                    sta4 = '759'
                elif STAR4 == 'Seymour Cassel':
                    sta4 = '760'
                elif STAR4 == 'Fele Martínez':
                    sta4 = '761'
                elif STAR4 == 'John Malkovich':
                    sta4 = '762'
                elif STAR4 == 'Cuba Gooding Jr.':
                    sta4 = '763'
                elif STAR4 == 'Ian Holm':
                    sta4 = '764'
                elif STAR4 == 'Daniel Prévost':
                    sta4 = '765'
                elif STAR4 == 'Bruno Kirby':
                    sta4 = '766'
                elif STAR4 == 'Sonia Todd':
                    sta4 = '767'
                elif STAR4 == 'John Mahoney':
                    sta4 = '768'
                elif STAR4 == 'Kate Winslet':
                    sta4 = '769'
                elif STAR4 == 'Rusty Schwimmer':
                    sta4 = '770'
                elif STAR4 == 'Charlie Yeung':
                    sta4 = '771'
                elif STAR4 == 'Maria Grazia Cucinotta':
                    sta4 = '772'
                elif STAR4 == 'Lisa Spoonauer':
                    sta4 = '773'
                elif STAR4 == 'Bruce Davison':
                    sta4 = '774'
                elif STAR4 == 'Buzz Kilman':
                    sta4 = '775'
                elif STAR4 == 'Miss Piggy':
                    sta4 = '776'
                elif STAR4 == 'Spike Lee':
                    sta4 = '777'
                elif STAR4 == 'Eric Schweig':
                    sta4 = '778'
                elif STAR4 == 'Tsunehiko Kamijô':
                    sta4 = '779'
                elif STAR4 == 'Mary-Louise Parker':
                    sta4 = '780'
                elif STAR4 == 'Judy Davis':
                    sta4 = '781'
                elif STAR4 == 'John Turturro':
                    sta4 = '782'
                elif STAR4 == 'Charles Fleischer':
                    sta4 = '783'
                elif STAR4 == 'Gwen Eckhaus':
                    sta4 = '784'
                elif STAR4 == 'Ralph Brown':
                    sta4 = '785'
                elif STAR4 == 'Ruocheng Ying':
                    sta4 = '786'
                elif STAR4 == 'Nigel Havers':
                    sta4 = '787'
                elif STAR4 == 'Elya Baskin':
                    sta4 = '788'
                elif STAR4 == 'Irving Metzman':
                    sta4 = '789'
                elif STAR4 == 'Tommy Chong':
                    sta4 = '790'
                elif STAR4 == 'John Buckwalter':
                    sta4 = '791'
                elif STAR4 == 'James Mason':
                    sta4 = '792'
                elif STAR4 == 'James Doohan':
                    sta4 = '793'
                elif STAR4 == 'Timothy Hutton':
                    sta4 = '794'
                elif STAR4 == 'Julie Hagerty':
                    sta4 = '795'
                elif STAR4 == 'Makio Inoue':
                    sta4 = '796'
                elif STAR4 == 'Nancy Kyes':
                    sta4 = '797'
                elif STAR4 == 'Jo Van Fleet':
                    sta4 = '798'
                elif STAR4 == 'Frank Adu':
                    sta4 = '799'
                elif STAR4 == 'Hector Elizondo':
                    sta4 = '800'
                elif STAR4 == 'Harvey Korman':
                    sta4 = '801'
                elif STAR4 == 'Biff McGuire':
                    sta4 = '802'
                elif STAR4 == 'Ahna Capri':
                    sta4 = '803'
                elif STAR4 == 'Ronny Cox':
                    sta4 = '804'
                elif STAR4 == 'Tony Lo Bianco':
                    sta4 = '805'
                elif STAR4 == 'Reni Santoni':
                    sta4 = '806'
                elif STAR4 == 'Patrick Wymark':
                    sta4 = '807'
                elif STAR4 == 'Herb Edelman':
                    sta4 = '808'
                elif STAR4 == 'John Cassavetes':
                    sta4 = '809'
                elif STAR4 == 'Geneviève Page':
                    sta4 = '810'
                elif STAR4 == 'Leo McKern':
                    sta4 = '811'
                elif STAR4 == 'James Booth':
                    sta4 = '812'
                elif STAR4 == 'Shirley Eaton':
                    sta4 = '813'
                elif STAR4 == 'Suzanne Pleshette':
                    sta4 = '814'
                elif STAR4 == 'Lori Martin':
                    sta4 = '815'
                elif STAR4 == 'Maxine Audley':
                    sta4 = '816'
                elif STAR4 == 'Eli Wallach':
                    sta4 = '817'
                elif STAR4 == 'Alexandre Rignault':
                    sta4 = '818'
                elif STAR4 == 'King Donovan':
                    sta4 = '819'
                elif STAR4 == 'Jim Backus':
                    sta4 = '820'
                elif STAR4 == 'Herbert Lom':
                    sta4 = '821'
                elif STAR4 == 'Walter Hampden':
                    sta4 = '822'
                elif STAR4 == 'Sam Jaffe':
                    sta4 = '823'
                elif STAR4 == 'Peter Bull':
                    sta4 = '824'
                elif STAR4 == 'David Hand':
                    sta4 = '825'
                elif STAR4 == 'Bill Pullman':
                    sta4 = '826'
                elif STAR4 == 'Michelle La':
                    sta4 = '827'
                elif STAR4 == 'Emile Hirsch':
                    sta4 = '828'
                elif STAR4 == 'Marina Vasileva':
                    sta4 = '829'
                elif STAR4 == 'Christopher Rivera':
                    sta4 = '830'
                elif STAR4 == 'Charlie Pye Jr.':
                    sta4 = '831'
                elif STAR4 == 'Octavia Spencer':
                    sta4 = '832'
                elif STAR4 == 'Dakota Johnson':
                    sta4 = '833'
                elif STAR4 == 'Burak Yigit':
                    sta4 = '834'
                elif STAR4 == 'Elit Iscan':
                    sta4 = '835'
                elif STAR4 == 'Eiza González':
                    sta4 = '836'
                elif STAR4 == 'Jennifer Connelly':
                    sta4 = '837'
                elif STAR4 == 'Amy Ryan':
                    sta4 = '838'
                elif STAR4 == 'Huck Milner':
                    sta4 = '839'
                elif STAR4 == 'Auli\'i Cravalho':
                    sta4 = '840'
                elif STAR4 == 'Jon Bernthal':
                    sta4 = '841'
                elif STAR4 == 'Phylicia Rashad':
                    sta4 = '842'
                elif STAR4 == 'Vladimir Vdovichenkov':
                    sta4 = '843'
                elif STAR4 == 'Gil Birmingham':
                    sta4 = '844'
                elif STAR4 == 'Mare Winningham':
                    sta4 = '845'
                elif STAR4 == 'Kodi Smit-McPhee':
                    sta4 = '846'
                elif STAR4 == 'Aura Garrido':
                    sta4 = '847'
                elif STAR4 == 'Donny Alamsyah':
                    sta4 = '848'
                elif STAR4 == 'America Ferrera':
                    sta4 = '849'
                elif STAR4 == 'Tatsuya Fujiwara':
                    sta4 = '850'
                elif STAR4 == 'Greg Grunberg':
                    sta4 = '851'
                elif STAR4 == 'Hailee Steinfeld':
                    sta4 = '852'
                elif STAR4 == 'Wil Johnson':
                    sta4 = '853'
                elif STAR4 == 'Russell Brand':
                    sta4 = '854'
                elif STAR4 == 'Garrett M. Brown':
                    sta4 = '855'
                elif STAR4 == 'Manuel Morón':
                    sta4 = '856'
                elif STAR4 == 'Marisa Paredes':
                    sta4 = '857'
                elif STAR4 == 'Abigail Breslin':
                    sta4 = '858'
                elif STAR4 == 'Jennifer Ulrich':
                    sta4 = '859'
                elif STAR4 == 'Mark Strong':
                    sta4 = '860'
                elif STAR4 == 'Jae Head':
                    sta4 = '861'
                elif STAR4 == 'Hiam Abbass':
                    sta4 = '862'
                elif STAR4 == 'Michael Ealy':
                    sta4 = '863'
                elif STAR4 == 'Josef Altin':
                    sta4 = '864'
                elif STAR4 == 'Ian McKellen':
                    sta4 = '865'
                elif STAR4 == 'Mick Lally':
                    sta4 = '866'
                elif STAR4 == 'Michelle Monaghan':
                    sta4 = '867'
                elif STAR4 == 'Emmanuelle Seigner':
                    sta4 = '868'
                elif STAR4 == 'Yun Qu':
                    sta4 = '869'
                elif STAR4 == 'Rufus Sewell':
                    sta4 = '870'
                elif STAR4 == 'Stuart Wolfenden':
                    sta4 = '871'
                elif STAR4 == 'Dominic West':
                    sta4 = '872'
                elif STAR4 == 'Matthew Goode':
                    sta4 = '873'
                elif STAR4 == 'Malin Akerman':
                    sta4 = '874'
                elif STAR4 == 'Bridget Moynahan':
                    sta4 = '875'
                elif STAR4 == 'Ken Leung':
                    sta4 = '876'
                elif STAR4 == 'Chase Ellison':
                    sta4 = '877'
                elif STAR4 == 'Joséphine Lebas-Joly':
                    sta4 = '878'
                elif STAR4 == 'Dominique Pinon':
                    sta4 = '879'
                elif STAR4 == 'Paul Benjamin':
                    sta4 = '880'
                elif STAR4 == 'Danny Huston':
                    sta4 = '881'
                elif STAR4 == 'Ji-Eun Lim':
                    sta4 = '882'
                elif STAR4 == 'Rosario Dawson':
                    sta4 = '883'
                elif STAR4 == 'Melora Walters':
                    sta4 = '884'
                elif STAR4 == 'Alex Palmer':
                    sta4 = '885'
                elif STAR4 == 'Takeshi Kitano':
                    sta4 = '886'
                elif STAR4 == 'Ben Stiller':
                    sta4 = '887'
                elif STAR4 == 'Ana López Mercado':
                    sta4 = '888'
                elif STAR4 == 'Maggie Smith':
                    sta4 = '889'
                elif STAR4 == 'Alakina Mann':
                    sta4 = '890'
                elif STAR4 == 'Rachel Griffiths':
                    sta4 = '891'
                elif STAR4 == 'Rachel Weisz':
                    sta4 = '892'
                elif STAR4 == 'Max von Sydow':
                    sta4 = '893'
                elif STAR4 == 'Bill Sage':
                    sta4 = '894'
                elif STAR4 == 'Nina Petri':
                    sta4 = '895'
                elif STAR4 == 'Kirk Acevedo':
                    sta4 = '896'
                elif STAR4 == 'BD Wong':
                    sta4 = '897'
                elif STAR4 == 'Michael Lee Gogin':
                    sta4 = '898'
                elif STAR4 == 'Frank Giering':
                    sta4 = '899'
                elif STAR4 == 'William Hurt':
                    sta4 = '900'
                elif STAR4 == 'Jason Patric':
                    sta4 = '901'
                elif STAR4 == 'Louis Eppolito':
                    sta4 = '902'
                elif STAR4 == 'Tom Wilkinson':
                    sta4 = '903'
                elif STAR4 == 'Graham Greene':
                    sta4 = '904'
                elif STAR4 == 'Lance Henriksen':
                    sta4 = '905'
                elif STAR4 == 'Victor Slezak':
                    sta4 = '906'
                elif STAR4 == 'Jerzy Stuhr':
                    sta4 = '907'
                elif STAR4 == 'Rachel Ticotin':
                    sta4 = '908'
                elif STAR4 == 'Rory Cochrane':
                    sta4 = '909'
                elif STAR4 == 'Mitchell Whitfield':
                    sta4 = '910'
                elif STAR4 == 'Mayumi Izuka':
                    sta4 = '911'
                elif STAR4 == 'Pascal Benezech':
                    sta4 = '912'
                elif STAR4 == 'John Heard':
                    sta4 = '913'
                elif STAR4 == 'Talia Shire':
                    sta4 = '914'
                elif STAR4 == 'Rene Auberjonois':
                    sta4 = '915'
                elif STAR4 == 'Ricardo Montalban':
                    sta4 = '916'
                elif STAR4 == 'Michael McKean':
                    sta4 = '917'
                elif STAR4 == 'Mitchell Ryan':
                    sta4 = '918'
                elif STAR4 == 'Dan Hedaya':
                    sta4 = '919'
                elif STAR4 == 'Doug McKeon':
                    sta4 = '920'
                elif STAR4 == 'Max Phipps':
                    sta4 = '921'
                elif STAR4 == 'Brian Tyler':
                    sta4 = '922'
                elif STAR4 == 'Richard Hunt':
                    sta4 = '923'
                elif STAR4 == 'Jack Thibeau':
                    sta4 = '924'
                elif STAR4 == 'Ralph Richardson':
                    sta4 = '925'
                elif STAR4 == 'Paolo Bonacelli':
                    sta4 = '926'
                elif STAR4 == 'Melinda Dillon':
                    sta4 = '927'
                elif STAR4 == 'Mark Rydell':
                    sta4 = '928'
                elif STAR4 == 'Maria Monti':
                    sta4 = '929'
                elif STAR4 == 'Carroll O\'Connor':
                    sta4 = '930'
                elif STAR4 == 'Bruce Reitherman':
                    sta4 = '931'
                elif STAR4 == 'Ringo Starr':
                    sta4 = '932'
                elif STAR4 == 'Buddy Ebsen':
                    sta4 = '933'
                elif STAR4 == 'Carroll Baker':
                    sta4 = '934'
                elif STAR4 == 'Donna Reed':
                    sta4 = '935'
                elif STAR4 == 'William Bendix':
                    sta4 = '936'
                elif STAR4 == 'Godfrey Tearle':
                    sta4 = '937'
                
                DIRECTOR = request.form['director']
                if DIRECTOR == 'Frank Darabont':
                    dir = '0'
                elif DIRECTOR == 'Francis Ford Coppola':
                    dir = '1'
                elif DIRECTOR == 'Christopher Nolan':
                    dir = '2'
                elif DIRECTOR == 'Sidney Lumet':
                    dir = '3'
                elif DIRECTOR == 'Peter Jackson':
                    dir = '4'
                elif DIRECTOR == 'Quentin Tarantino':
                    dir = '5'
                elif DIRECTOR == 'Steven Spielberg':
                    dir = '6'
                elif DIRECTOR == 'David Fincher':
                    dir = '7'
                elif DIRECTOR == 'Robert Zemeckis':
                    dir = '8'
                elif DIRECTOR == 'Sergio Leone':
                    dir = '9'
                elif DIRECTOR == 'Lana Wachowski':
                    dir = '10'
                elif DIRECTOR == 'Martin Scorsese':
                    dir = '11'
                elif DIRECTOR == 'Irvin Kershner':
                    dir = '12'
                elif DIRECTOR == 'Milos Forman':
                    dir = '13'
                elif DIRECTOR == 'Thomas Kail':
                    dir = '14'
                elif DIRECTOR == 'Bong Joon Ho':
                    dir = '15'
                elif DIRECTOR == 'Sudha Kongara':
                    dir = '16'
                elif DIRECTOR == 'Fernando Meirelles':
                    dir = '17'
                elif DIRECTOR == 'Hayao Miyazaki':
                    dir = '18'
                elif DIRECTOR == 'Roberto Benigni':
                    dir = '19'
                elif DIRECTOR == 'Jonathan Demme':
                    dir = '20'
                elif DIRECTOR == 'George Lucas':
                    dir = '21'
                elif DIRECTOR == 'Masaki Kobayashi':
                    dir = '22'
                elif DIRECTOR == 'Akira Kurosawa':
                    dir = '23'
                elif DIRECTOR == 'Frank Capra':
                    dir = '24'
                elif DIRECTOR == 'Todd Phillips':
                    dir = '25'
                elif DIRECTOR == 'Damien Chazelle':
                    dir = '26'
                elif DIRECTOR == 'Olivier Nakache':
                    dir = '27'
                elif DIRECTOR == 'Roman Polanski':
                    dir = '28'
                elif DIRECTOR == 'Ridley Scott':
                    dir = '29'
                elif DIRECTOR == 'Tony Kaye':
                    dir = '30'
                elif DIRECTOR == 'Bryan Singer':
                    dir = '31'
                elif DIRECTOR == 'Luc Besson':
                    dir = '32'
                elif DIRECTOR == 'Roger Allers':
                    dir = '33'
                elif DIRECTOR == 'James Cameron':
                    dir = '34'
                elif DIRECTOR == 'Giuseppe Tornatore':
                    dir = '35'
                elif DIRECTOR == 'Isao Takahata':
                    dir = '36'
                elif DIRECTOR == 'Alfred Hitchcock':
                    dir = '37'
                elif DIRECTOR == 'Michael Curtiz':
                    dir = '38'
                elif DIRECTOR == 'Charles Chaplin':
                    dir = '39'
                elif DIRECTOR == 'Nadine Labaki':
                    dir = '40'
                elif DIRECTOR == 'Can Ulkay':
                    dir = '41'
                elif DIRECTOR == 'Gayatri':
                    dir = '42'
                elif DIRECTOR == 'Makoto Shinkai':
                    dir = '43'
                elif DIRECTOR == 'Nitesh Tiwari':
                    dir = '44'
                elif DIRECTOR == 'Bob Persichetti':
                    dir = '45'
                elif DIRECTOR == 'Anthony Russo':
                    dir = '46'
                elif DIRECTOR == 'Lee Unkrich':
                    dir = '47'
                elif DIRECTOR == 'Rajkumar Hirani':
                    dir = '48'
                elif DIRECTOR == 'Aamir Khan':
                    dir = '49'
                elif DIRECTOR == 'Andrew Stanton':
                    dir = '50'
                elif DIRECTOR == 'Florian Henckel von Donnersmarck':
                    dir = '51'
                elif DIRECTOR == 'Chan-wook Park':
                    dir = '52'
                elif DIRECTOR == 'Stanley Kubrick':
                    dir = '53'
                elif DIRECTOR == 'Hrishikesh Mukherjee':
                    dir = '54'
                elif DIRECTOR == 'Billy Wilder':
                    dir = '55'
                elif DIRECTOR == 'Sam Mendes':
                    dir = '56'
                elif DIRECTOR == 'Rahi Anil Barve':
                    dir = '57'
                elif DIRECTOR == 'Sriram Raghavan':
                    dir = '58'
                elif DIRECTOR == 'Jeethu Joseph':
                    dir = '59'
                elif DIRECTOR == 'Thomas Vinterberg':
                    dir = '60'
                elif DIRECTOR == 'Asghar Farhadi':
                    dir = '61'
                elif DIRECTOR == 'Denis Villeneuve':
                    dir = '62'
                elif DIRECTOR == 'Mehmet Ada Öztekin':
                    dir = '63'
                elif DIRECTOR == 'Çagan Irmak':
                    dir = '64'
                elif DIRECTOR == 'Michel Gondry':
                    dir = '65'
                elif DIRECTOR == 'Jean-Pierre Jeunet':
                    dir = '66'
                elif DIRECTOR == 'Guy Ritchie':
                    dir = '67'
                elif DIRECTOR == 'Darren Aronofsky':
                    dir = '68'
                elif DIRECTOR == 'Gus Van Sant':
                    dir = '69'
                elif DIRECTOR == 'Majid Majidi':
                    dir = '70'
                elif DIRECTOR == 'John Lasseter':
                    dir = '71'
                elif DIRECTOR == 'Mel Gibson':
                    dir = '72'
                elif DIRECTOR == 'Elem Klimov':
                    dir = '73'
                elif DIRECTOR == 'Brian De Palma':
                    dir = '74'
                elif DIRECTOR == 'Richard Marquand':
                    dir = '75'
                elif DIRECTOR == 'Wolfgang Petersen':
                    dir = '76'
                elif DIRECTOR == 'George Roy Hill':
                    dir = '77'
                elif DIRECTOR == 'David Lean':
                    dir = '78'
                elif DIRECTOR == 'Stanley Donen':
                    dir = '79'
                elif DIRECTOR == 'Vittorio De Sica':
                    dir = '80'
                elif DIRECTOR == 'Orson Welles':
                    dir = '81'
                elif DIRECTOR == 'Fritz Lang':
                    dir = '82'
                elif DIRECTOR == 'Aditya Dhar':
                    dir = '83'
                elif DIRECTOR == 'Prashanth Neel':
                    dir = '84'
                elif DIRECTOR == 'Peter Farrelly':
                    dir = '85'
                elif DIRECTOR == 'Martin McDonagh':
                    dir = '86'
                elif DIRECTOR == 'Meghna Gulzar':
                    dir = '87'
                elif DIRECTOR == 'S.S. Rajamouli':
                    dir = '88'
                elif DIRECTOR == 'Sergio Pablos':
                    dir = '89'
                elif DIRECTOR == 'Nishikant Kamat':
                    dir = '90'
                elif DIRECTOR == 'Vikas Bahl':
                    dir = '91'
                elif DIRECTOR == 'Zaza Urushadze':
                    dir = '92'
                elif DIRECTOR == 'Rakeysh Omprakash Mehra':
                    dir = '93'
                elif DIRECTOR == 'Anurag Kashyap':
                    dir = '94'
                elif DIRECTOR == 'Vikramaditya Motwane':
                    dir = '95'
                elif DIRECTOR == 'Tigmanshu Dhulia':
                    dir = '96'
                elif DIRECTOR == 'Juan José Campanella':
                    dir = '97'
                elif DIRECTOR == 'Gavin O\'Connor':
                    dir = '98'
                elif DIRECTOR == 'Pete Docter':
                    dir = '99'
                elif DIRECTOR == 'Shimit Amin':
                    dir = '100'
                elif DIRECTOR == 'Paul Thomas Anderson':
                    dir = '101'
                elif DIRECTOR == 'Guillermo del Toro':
                    dir = '102'
                elif DIRECTOR == 'James McTeigue':
                    dir = '103'
                elif DIRECTOR == 'Sanjay Leela Bhansali':
                    dir = '104'
                elif DIRECTOR == 'Ashutosh Gowariker':
                    dir = '105'
                elif DIRECTOR == 'Oliver Hirschbiegel':
                    dir = '106'
                elif DIRECTOR == 'Ron Howard':
                    dir = '107'
                elif DIRECTOR == 'Priyadarshan':
                    dir = '108'
                elif DIRECTOR == 'Curtis Hanson':
                    dir = '109'
                elif DIRECTOR == 'Yavuz Turgul':
                    dir = '110'
                elif DIRECTOR == 'Michael Mann':
                    dir = '111'
                elif DIRECTOR == 'Rajkumar Santoshi':
                    dir = '112'
                elif DIRECTOR == 'Clint Eastwood':
                    dir = '113'
                elif DIRECTOR == 'Emir Kusturica':
                    dir = '114'
                elif DIRECTOR == 'John McTiernan':
                    dir = '115'
                elif DIRECTOR == 'Andrei Tarkovsky':
                    dir = '116'
                elif DIRECTOR == 'Ingmar Bergman':
                    dir = '117'
                elif DIRECTOR == 'Moustapha Akkad':
                    dir = '118'
                elif DIRECTOR == 'Ramesh Sippy':
                    dir = '119'
                elif DIRECTOR == 'Terry Gilliam':
                    dir = '120'
                elif DIRECTOR == 'John Sturges':
                    dir = '121'
                elif DIRECTOR == 'Robert Mulligan':
                    dir = '122'
                elif DIRECTOR == 'Stanley Kramer':
                    dir = '123'
                elif DIRECTOR == 'Jules Dassin':
                    dir = '124'
                elif DIRECTOR == 'Yasujirô Ozu':
                    dir = '125'
                elif DIRECTOR == 'Joseph L. Mankiewicz':
                    dir = '126'
                elif DIRECTOR == 'John Huston':
                    dir = '127'
                elif DIRECTOR == 'Ernst Lubitsch':
                    dir = '128'
                elif DIRECTOR == 'Buster Keaton':
                    dir = '129'
                elif DIRECTOR == 'Céline Sciamma':
                    dir = '130'
                elif DIRECTOR == 'Aniruddha Roy Chowdhury':
                    dir = '131'
                elif DIRECTOR == 'Naoko Yamada':
                    dir = '132'
                elif DIRECTOR == 'Oriol Paulo':
                    dir = '133'
                elif DIRECTOR == 'Xavier Dolan':
                    dir = '134'
                elif DIRECTOR == 'Vishal Bhardwaj':
                    dir = '135'
                elif DIRECTOR == 'James Mangold':
                    dir = '136'
                elif DIRECTOR == 'Lenny Abrahamson':
                    dir = '137'
                elif DIRECTOR == 'Damián Szifron':
                    dir = '138'
                elif DIRECTOR == 'Nuri Bilge Ceylan':
                    dir = '139'
                elif DIRECTOR == 'Umesh Shukla':
                    dir = '140'
                elif DIRECTOR == 'Wes Anderson':
                    dir = '141'
                elif DIRECTOR == 'Mamoru Hosoda':
                    dir = '142'
                elif DIRECTOR == 'Anurag Basu':
                    dir = '143'
                elif DIRECTOR == 'Steve McQueen':
                    dir = '144'
                elif DIRECTOR == 'Tom McCarthy':
                    dir = '145'
                elif DIRECTOR == 'Tomm Moore':
                    dir = '146'
                elif DIRECTOR == 'Sujoy Ghosh':
                    dir = '147'
                elif DIRECTOR == 'Zoya Akhtar':
                    dir = '148'
                elif DIRECTOR == 'George Miller':
                    dir = '149'
                elif DIRECTOR == 'Neeraj Pandey':
                    dir = '150'
                elif DIRECTOR == 'David Yates':
                    dir = '151'
                elif DIRECTOR == 'Yôjirô Takita':
                    dir = '152'
                elif DIRECTOR == 'Lasse Hallström':
                    dir = '153'
                elif DIRECTOR == 'Adam Elliot':
                    dir = '154'
                elif DIRECTOR == 'Dean DeBlois':
                    dir = '155'
                elif DIRECTOR == 'Sean Penn':
                    dir = '156'
                elif DIRECTOR == 'Ethan Coen':
                    dir = '157'
                elif DIRECTOR == 'Terry George':
                    dir = '158'
                elif DIRECTOR == 'Je-kyu Kang':
                    dir = '159'
                elif DIRECTOR == 'Richard Linklater':
                    dir = '160'
                elif DIRECTOR == 'Farhan Akhtar':
                    dir = '161'
                elif DIRECTOR == 'Alejandro G. Iñárritu':
                    dir = '162'
                elif DIRECTOR == 'Hideaki Anno':
                    dir = '163'
                elif DIRECTOR == 'M. Night Shyamalan':
                    dir = '164'
                elif DIRECTOR == 'Peter Weir':
                    dir = '165'
                elif DIRECTOR == 'Joel Coen':
                    dir = '166'
                elif DIRECTOR == 'Kar-Wai Wong':
                    dir = '167'
                elif DIRECTOR == 'Danny Boyle':
                    dir = '168'
                elif DIRECTOR == 'Mathieu Kassovitz':
                    dir = '169'
                elif DIRECTOR == 'Aditya Chopra':
                    dir = '170'
                elif DIRECTOR == 'Krzysztof Kieslowski':
                    dir = '171'
                elif DIRECTOR == 'Jim Sheridan':
                    dir = '172'
                elif DIRECTOR == 'Kaige Chen':
                    dir = '173'
                elif DIRECTOR == 'Yimou Zhang':
                    dir = '174'
                elif DIRECTOR == 'Rob Reiner':
                    dir = '175'
                elif DIRECTOR == 'Oliver Stone':
                    dir = '176'
                elif DIRECTOR == 'Wim Wenders':
                    dir = '177'
                elif DIRECTOR == 'John Carpenter':
                    dir = '178'
                elif DIRECTOR == 'Alan Parker':
                    dir = '179'
                elif DIRECTOR == 'Werner Herzog':
                    dir = '180'
                elif DIRECTOR == 'David Lynch':
                    dir = '181'
                elif DIRECTOR == 'Terry Jones':
                    dir = '182'
                elif DIRECTOR == 'Michael Cimino':
                    dir = '183'
                elif DIRECTOR == 'John G. Avildsen':
                    dir = '184'
                elif DIRECTOR == 'Peter Bogdanovich':
                    dir = '185'
                elif DIRECTOR == 'Jean-Pierre Melville':
                    dir = '186'
                elif DIRECTOR == 'Stuart Rosenberg':
                    dir = '187'
                elif DIRECTOR == 'Gillo Pontecorvo':
                    dir = '188'
                elif DIRECTOR == 'Luis Buñuel':
                    dir = '189'
                elif DIRECTOR == 'Robert Aldrich':
                    dir = '190'
                elif DIRECTOR == 'John Ford':
                    dir = '191'
                elif DIRECTOR == 'François Truffaut':
                    dir = '192'
                elif DIRECTOR == 'William Wyler':
                    dir = '193'
                elif DIRECTOR == 'Federico Fellini':
                    dir = '194'
                elif DIRECTOR == 'Elia Kazan':
                    dir = '195'
                elif DIRECTOR == 'Henri-Georges Clouzot':
                    dir = '196'
                elif DIRECTOR == 'Raoul Walsh':
                    dir = '197'
                elif DIRECTOR == 'Carol Reed':
                    dir = '198'
                elif DIRECTOR == 'Michael Powell':
                    dir = '199'
                elif DIRECTOR == 'Victor Fleming':
                    dir = '200'
                elif DIRECTOR == 'Jean Renoir':
                    dir = '201'
                elif DIRECTOR == 'Carl Theodor Dreyer':
                    dir = '202'
                elif DIRECTOR == 'F.W. Murnau':
                    dir = '203'
                elif DIRECTOR == 'Clyde Bruckman':
                    dir = '204'
                elif DIRECTOR == 'Robert Wiene':
                    dir = '205'
                elif DIRECTOR == 'Amit Ravindernath Sharma':
                    dir = '206'
                elif DIRECTOR == 'Ericson Core':
                    dir = '207'
                elif DIRECTOR == 'Raja Menon':
                    dir = '208'
                elif DIRECTOR == 'Kabir Khan':
                    dir = '209'
                elif DIRECTOR == 'Garth Davis':
                    dir = '210'
                elif DIRECTOR == 'Byron Howard':
                    dir = '211'
                elif DIRECTOR == 'Stephen Chbosky':
                    dir = '212'
                elif DIRECTOR == 'Destin Daniel Cretton':
                    dir = '213'
                elif DIRECTOR == 'Gareth Evans':
                    dir = '214'
                elif DIRECTOR == 'Morten Tyldum':
                    dir = '215'
                elif DIRECTOR == 'James Gunn':
                    dir = '216'
                elif DIRECTOR == 'Spike Jonze':
                    dir = '217'
                elif DIRECTOR == 'José Padilha':
                    dir = '218'
                elif DIRECTOR == 'Tom Hooper':
                    dir = '219'
                elif DIRECTOR == 'Tate Taylor':
                    dir = '220'
                elif DIRECTOR == 'Tim Miller':
                    dir = '221'
                elif DIRECTOR == 'Wilson Yip':
                    dir = '222'
                elif DIRECTOR == 'Karan Johar':
                    dir = '223'
                elif DIRECTOR == 'Levent Semerci':
                    dir = '224'
                elif DIRECTOR == 'Joss Whedon':
                    dir = '225'
                elif DIRECTOR == 'Vincent Paronnaud':
                    dir = '226'
                elif DIRECTOR == 'Jean-Marc Vallée':
                    dir = '227'
                elif DIRECTOR == 'Gabriele Muccino':
                    dir = '228'
                elif DIRECTOR == 'Edward Zwick':
                    dir = '229'
                elif DIRECTOR == 'Paul Greengrass':
                    dir = '230'
                elif DIRECTOR == 'Ki-duk Kim':
                    dir = '231'
                elif DIRECTOR == 'Frank Miller':
                    dir = '232'
                elif DIRECTOR == 'Julian Schnabel':
                    dir = '233'
                elif DIRECTOR == 'Ömer Faruk Sorak':
                    dir = '234'
                elif DIRECTOR == 'Brad Bird':
                    dir = '235'
                elif DIRECTOR == 'Martin Campbell':
                    dir = '236'
                elif DIRECTOR == 'Andrey Zvyagintsev':
                    dir = '237'
                elif DIRECTOR == 'Alejandro Amenábar':
                    dir = '238'
                elif DIRECTOR == 'Nikkhil Advani':
                    dir = '239'
                elif DIRECTOR == 'Andrew Lau':
                    dir = '240'
                elif DIRECTOR == 'Gore Verbinski':
                    dir = '241'
                elif DIRECTOR == 'Tim Burton':
                    dir = '242'
                elif DIRECTOR == 'Jae-young Kwak':
                    dir = '243'
                elif DIRECTOR == 'Lars von Trier':
                    dir = '244'
                elif DIRECTOR == 'Yilmaz Erdogan':
                    dir = '245'
                elif DIRECTOR == 'Richard Kelly':
                    dir = '246'
                elif DIRECTOR == 'Satoshi Kon':
                    dir = '247'
                elif DIRECTOR == 'Walter Salles':
                    dir = '248'
                elif DIRECTOR == 'Thomas Jahn':
                    dir = '249'
                elif DIRECTOR == 'Billy Bob Thornton':
                    dir = '250'
                elif DIRECTOR == 'Mike Leigh':
                    dir = '251'
                elif DIRECTOR == 'Mamoru Oshii':
                    dir = '252'
                elif DIRECTOR == 'Henry Selick':
                    dir = '253'
                elif DIRECTOR == 'Harold Ramis':
                    dir = '254'
                elif DIRECTOR == 'Taylor Hackford':
                    dir = '255'
                elif DIRECTOR == 'Martin Brest':
                    dir = '256'
                elif DIRECTOR == 'Ron Clements':
                    dir = '257'
                elif DIRECTOR == 'Gary Trousdale':
                    dir = '258'
                elif DIRECTOR == 'Kevin Costner':
                    dir = '259'
                elif DIRECTOR == 'Spike Lee':
                    dir = '260'
                elif DIRECTOR == 'Barry Levinson':
                    dir = '261'
                elif DIRECTOR == 'Katsuhiro Ôtomo':
                    dir = '262'
                elif DIRECTOR == 'Louis Malle':
                    dir = '263'
                elif DIRECTOR == 'Richard Attenborough':
                    dir = '264'
                elif DIRECTOR == 'Hal Ashby':
                    dir = '265'
                elif DIRECTOR == 'Woody Allen':
                    dir = '266'
                elif DIRECTOR == 'Mel Brooks':
                    dir = '267'
                elif DIRECTOR == 'Franklin J. Schaffner':
                    dir = '268'
                elif DIRECTOR == 'William Friedkin':
                    dir = '269'
                elif DIRECTOR == 'Norman Jewison':
                    dir = '270'
                elif DIRECTOR == 'Bernardo Bertolucci':
                    dir = '271'
                elif DIRECTOR == 'Mike Nichols':
                    dir = '272'
                elif DIRECTOR == 'Robert Wise':
                    dir = '273'
                elif DIRECTOR == 'Jean-Luc Godard':
                    dir = '274'
                elif DIRECTOR == 'Robert Rossen':
                    dir = '275'
                elif DIRECTOR == 'Howard Hawks':
                    dir = '276'
                elif DIRECTOR == 'Otto Preminger':
                    dir = '277'
                elif DIRECTOR == 'Richard Brooks':
                    dir = '278'
                elif DIRECTOR == 'Alexander Mackendrick':
                    dir = '279'
                elif DIRECTOR == 'Charles Laughton':
                    dir = '280'
                elif DIRECTOR == 'Nicholas Ray':
                    dir = '281'
                elif DIRECTOR == 'Robert Hamer':
                    dir = '282'
                elif DIRECTOR == 'Jacques Tourneur':
                    dir = '283'
                elif DIRECTOR == 'W.S. Van Dyke':
                    dir = '284'
                elif DIRECTOR == 'Lewis Milestone':
                    dir = '285'
                elif DIRECTOR == 'Sergei M. Eisenstein':
                    dir = '286'
                elif DIRECTOR == 'Rian Johnson':
                    dir = '287'
                elif DIRECTOR == 'Mukesh Chhabra':
                    dir = '288'
                elif DIRECTOR == 'Hirokazu Koreeda':
                    dir = '289'
                elif DIRECTOR == 'Noah Baumbach':
                    dir = '290'
                elif DIRECTOR == 'Luca Guadagnino':
                    dir = '291'
                elif DIRECTOR == 'Ken Loach':
                    dir = '292'
                elif DIRECTOR == 'Taika Waititi':
                    dir = '293'
                elif DIRECTOR == 'Matt Ross':
                    dir = '294'
                elif DIRECTOR == 'John Carney':
                    dir = '295'
                elif DIRECTOR == 'Dan Gilroy':
                    dir = '296'
                elif DIRECTOR == 'J.J. Abrams':
                    dir = '297'
                elif DIRECTOR == 'Michel Hazanavicius':
                    dir = '298'
                elif DIRECTOR == 'Doug Liman':
                    dir = '299'
                elif DIRECTOR == 'Michael Haneke':
                    dir = '300'
                elif DIRECTOR == 'Jacques Audiard':
                    dir = '301'
                elif DIRECTOR == 'Duncan Jones':
                    dir = '302'
                elif DIRECTOR == 'Tomas Alfredson':
                    dir = '303'
                elif DIRECTOR == 'Neill Blomkamp':
                    dir = '304'
                elif DIRECTOR == 'Imtiaz Ali':
                    dir = '305'
                elif DIRECTOR == 'Cristian Mungiu':
                    dir = '306'
                elif DIRECTOR == 'Richard Schenkman':
                    dir = '307'
                elif DIRECTOR == 'Tarsem Singh':
                    dir = '308'
                elif DIRECTOR == 'Ang Lee':
                    dir = '309'
                elif DIRECTOR == 'Christophe Barratier':
                    dir = '310'
                elif DIRECTOR == 'Jon Favreau':
                    dir = '311'
                elif DIRECTOR == 'Edgar Wright':
                    dir = '312'
                elif DIRECTOR == 'Fatih Akin':
                    dir = '313'
                elif DIRECTOR == 'Alfonso Cuarón':
                    dir = '314'
                elif DIRECTOR == 'Pedro Almodóvar':
                    dir = '315'
                elif DIRECTOR == 'Danis Tanovic':
                    dir = '316'
                elif DIRECTOR == 'Shin\'ichirô Watanabe':
                    dir = '317'
                elif DIRECTOR == 'Fabián Bielinsky':
                    dir = '318'
                elif DIRECTOR == 'Cameron Crowe':
                    dir = '319'
                elif DIRECTOR == 'Yoshifumi Kondô':
                    dir = '320'
                elif DIRECTOR == 'Lee Tamahori':
                    dir = '321'
                elif DIRECTOR == 'Tony Scott':
                    dir = '322'
                elif DIRECTOR == 'Yoshiaki Kawajiri':
                    dir = '323'
                elif DIRECTOR == 'Bob Clark':
                    dir = '324'
                elif DIRECTOR == 'John Landis':
                    dir = '325'
                elif DIRECTOR == 'Bob Fosse':
                    dir = '326'
                elif DIRECTOR == 'George A. Romero':
                    dir = '327'
                elif DIRECTOR == 'Alan J. Pakula':
                    dir = '328'
                elif DIRECTOR == 'Alejandro Jodorowsky':
                    dir = '329'
                elif DIRECTOR == 'Sam Peckinpah':
                    dir = '330'
                elif DIRECTOR == 'Anthony Harvey':
                    dir = '331'
                elif DIRECTOR == 'John Frankenheimer':
                    dir = '332'
                elif DIRECTOR == 'Michelangelo Antonioni':
                    dir = '333'
                elif DIRECTOR == 'Alain Resnais':
                    dir = '334'
                elif DIRECTOR == 'Cecil B. DeMille':
                    dir = '335'
                elif DIRECTOR == 'Fred Zinnemann':
                    dir = '336'
                elif DIRECTOR == 'Henry Koster':
                    dir = '337'
                elif DIRECTOR == 'George Seaton':
                    dir = '338'
                elif DIRECTOR == 'George Cukor':
                    dir = '339'
                elif DIRECTOR == 'Sam Wood':
                    dir = '340'
                elif DIRECTOR == 'Merian C. Cooper':
                    dir = '341'
                elif DIRECTOR == 'Tod Browning':
                    dir = '342'
                elif DIRECTOR == 'Darius Marder':
                    dir = '343'
                elif DIRECTOR == 'Paolo Genovese':
                    dir = '344'
                elif DIRECTOR == 'Theodore Melfi':
                    dir = '345'
                elif DIRECTOR == 'Paul King':
                    dir = '346'
                elif DIRECTOR == 'Abhishek Chaubey':
                    dir = '347'
                elif DIRECTOR == 'Travis Knight':
                    dir = '348'
                elif DIRECTOR == 'Kenneth Lonergan':
                    dir = '349'
                elif DIRECTOR == 'Martin Zandvliet':
                    dir = '350'
                elif DIRECTOR == 'Gareth Edwards':
                    dir = '351'
                elif DIRECTOR == 'Greta Gerwig':
                    dir = '352'
                elif DIRECTOR == 'Dorota Kobiela':
                    dir = '353'
                elif DIRECTOR == 'Matthew Warchus':
                    dir = '354'
                elif DIRECTOR == 'Paolo Sorrentino':
                    dir = '355'
                elif DIRECTOR == 'Ritesh Batra':
                    dir = '356'
                elif DIRECTOR == 'Shoojit Sircar':
                    dir = '357'
                elif DIRECTOR == 'Don Hall':
                    dir = '358'
                elif DIRECTOR == 'Richard Curtis':
                    dir = '359'
                elif DIRECTOR == 'Gauri Shinde':
                    dir = '360'
                elif DIRECTOR == 'Josh Cooley':
                    dir = '361'
                elif DIRECTOR == 'Adam McKay':
                    dir = '362'
                elif DIRECTOR == 'Tetsuya Nakashima':
                    dir = '363'
                elif DIRECTOR == 'Jee-woon Kim':
                    dir = '364'
                elif DIRECTOR == 'Jeong-beom Lee':
                    dir = '365'
                elif DIRECTOR == 'F. Gary Gray':
                    dir = '366'
                elif DIRECTOR == 'Hong-jin Na':
                    dir = '367'
                elif DIRECTOR == 'Niels Arden Oplev':
                    dir = '368'
                elif DIRECTOR == 'Aaron Sorkin':
                    dir = '369'
                elif DIRECTOR == 'David O. Russell':
                    dir = '370'
                elif DIRECTOR == 'Pierre Morel':
                    dir = '371'
                elif DIRECTOR == 'Mark Herman':
                    dir = '372'
                elif DIRECTOR == 'Joe Wright':
                    dir = '373'
                elif DIRECTOR == 'Nicolas Winding Refn':
                    dir = '374'
                elif DIRECTOR == 'Jaco Van Dormael':
                    dir = '375'
                elif DIRECTOR == 'Jonathan Dayton':
                    dir = '376'
                elif DIRECTOR == 'Yash Chopra':
                    dir = '377'
                elif DIRECTOR == 'Anders Thomas Jensen':
                    dir = '378'
                elif DIRECTOR == 'Roger Donaldson':
                    dir = '379'
                elif DIRECTOR == 'Mikael Håfström':
                    dir = '380'
                elif DIRECTOR == 'Nick Cassavetes':
                    dir = '381'
                elif DIRECTOR == 'Lukas Moodysson':
                    dir = '382'
                elif DIRECTOR == 'Sylvain Chomet':
                    dir = '383'
                elif DIRECTOR == 'Kevin Reynolds':
                    dir = '384'
                elif DIRECTOR == 'Boaz Yakin':
                    dir = '385'
                elif DIRECTOR == 'Troy Duffy':
                    dir = '386'
                elif DIRECTOR == 'Joe Johnston':
                    dir = '387'
                elif DIRECTOR == 'Andrew Adamson':
                    dir = '388'
                elif DIRECTOR == 'Takeshi Kitano':
                    dir = '389'
                elif DIRECTOR == 'Andrew Niccol':
                    dir = '390'
                elif DIRECTOR == 'George P. Cosmatos':
                    dir = '391'
                elif DIRECTOR == 'David Mickey Evans':
                    dir = '392'
                elif DIRECTOR == 'James Ivory':
                    dir = '393'
                elif DIRECTOR == 'Andrew Davis':
                    dir = '394'
                elif DIRECTOR == 'Robert De Niro':
                    dir = '395'
                elif DIRECTOR == 'Kevin Altieri':
                    dir = '396'
                elif DIRECTOR == 'John Woo':
                    dir = '397'
                elif DIRECTOR == 'Jim Jarmusch':
                    dir = '398'
                elif DIRECTOR == 'John Singleton':
                    dir = '399'
                elif DIRECTOR == 'Penny Marshall':
                    dir = '400'
                elif DIRECTOR == 'Sam Raimi':
                    dir = '401'
                elif DIRECTOR == 'John Hughes':
                    dir = '402'
                elif DIRECTOR == 'Richard Donner':
                    dir = '403'
                elif DIRECTOR == 'Roland Joffé':
                    dir = '404'
                elif DIRECTOR == 'Ivan Reitman':
                    dir = '405'
                elif DIRECTOR == 'Philip Kaufman':
                    dir = '406'
                elif DIRECTOR == 'Robert Benton':
                    dir = '407'
                elif DIRECTOR == 'Terrence Malick':
                    dir = '408'
                elif DIRECTOR == 'René Laloux':
                    dir = '409'
                elif DIRECTOR == 'Mel Stuart':
                    dir = '410'
                elif DIRECTOR == 'John Schlesinger':
                    dir = '411'
                elif DIRECTOR == 'Terence Young':
                    dir = '412'
                elif DIRECTOR == 'Arthur Penn':
                    dir = '413'
                elif DIRECTOR == 'Robert Stevenson':
                    dir = '414'
                elif DIRECTOR == 'Ken Annakin':
                    dir = '415'
                elif DIRECTOR == 'Jack Clayton':
                    dir = '416'
                elif DIRECTOR == 'James Whale':
                    dir = '417'
                elif DIRECTOR == 'Leo McCarey':
                    dir = '418'
                elif DIRECTOR == 'Francis Lee':
                    dir = '419'
                elif DIRECTOR == 'David Leitch':
                    dir = '420'
                elif DIRECTOR == 'Taylor Sheridan':
                    dir = '421'
                elif DIRECTOR == 'Jordan Peele':
                    dir = '422'
                elif DIRECTOR == 'Christopher McQuarrie':
                    dir = '423'
                elif DIRECTOR == 'Hannes Holm':
                    dir = '424'
                elif DIRECTOR == 'Jemaine Clement':
                    dir = '425'
                elif DIRECTOR == 'James Simone':
                    dir = '426'
                elif DIRECTOR == 'James Marsh':
                    dir = '427'
                elif DIRECTOR == 'Matthew Vaughn':
                    dir = '428'
                elif DIRECTOR == 'Josh Boone':
                    dir = '429'
                elif DIRECTOR == 'Alfonso Gomez-Rejon':
                    dir = '430'
                elif DIRECTOR == 'Abdellatif Kechiche':
                    dir = '431'
                elif DIRECTOR == 'Abhishek Kapoor':
                    dir = '432'
                elif DIRECTOR == 'Felix van Groeningen':
                    dir = '433'
                elif DIRECTOR == 'Alexander Payne':
                    dir = '434'
                elif DIRECTOR == 'Rich Moore':
                    dir = '435'
                elif DIRECTOR == 'Mark Osborne':
                    dir = '436'
                elif DIRECTOR == 'Christopher Miller':
                    dir = '437'
                elif DIRECTOR == 'Cary Joji Fukunaga':
                    dir = '438'
                elif DIRECTOR == 'Ben Affleck':
                    dir = '439'
                elif DIRECTOR == 'Marc Webb':
                    dir = '440'
                elif DIRECTOR == 'Shûsuke Kaneko':
                    dir = '441'
                elif DIRECTOR == 'Shane Meadows':
                    dir = '442'
                elif DIRECTOR == 'Alex Garland':
                    dir = '443'
                elif DIRECTOR == 'Susanne Bier':
                    dir = '444'
                elif DIRECTOR == 'Kevin Macdonald':
                    dir = '445'
                elif DIRECTOR == 'Paul McGuigan':
                    dir = '446'
                elif DIRECTOR == 'Christian Carion':
                    dir = '447'
                elif DIRECTOR == 'Anton Corbijn':
                    dir = '448'
                elif DIRECTOR == 'Nathan Greno':
                    dir = '449'
                elif DIRECTOR == 'Paul Verhoeven':
                    dir = '450'
                elif DIRECTOR == 'Paul Haggis':
                    dir = '451'
                elif DIRECTOR == 'Stephen Chow':
                    dir = '452'
                elif DIRECTOR == 'Brad Anderson':
                    dir = '453'
                elif DIRECTOR == 'Sofia Coppola':
                    dir = '454'
                elif DIRECTOR == 'Mike Newell':
                    dir = '455'
                elif DIRECTOR == 'Peter Mullan':
                    dir = '456'
                elif DIRECTOR == 'Wolfgang Becker':
                    dir = '457'
                elif DIRECTOR == 'Jessie Nelson':
                    dir = '458'
                elif DIRECTOR == 'Stephen Daldry':
                    dir = '459'
                elif DIRECTOR == 'John Cameron Mitchell':
                    dir = '460'
                elif DIRECTOR == 'Steven Soderbergh':
                    dir = '461'
                elif DIRECTOR == 'Bob Gale':
                    dir = '462'
                elif DIRECTOR == 'Trey Parker':
                    dir = '463'
                elif DIRECTOR == 'Mike Judge':
                    dir = '464'
                elif DIRECTOR == 'Todd Solondz':
                    dir = '465'
                elif DIRECTOR == 'Antoine Fuqua':
                    dir = '466'
                elif DIRECTOR == 'James L. Brooks':
                    dir = '467'
                elif DIRECTOR == 'Francis Veber':
                    dir = '468'
                elif DIRECTOR == 'Scott Hicks':
                    dir = '469'
                elif DIRECTOR == 'Gregory Hoblit':
                    dir = '470'
                elif DIRECTOR == 'Kenneth Branagh':
                    dir = '471'
                elif DIRECTOR == 'Michael Radford':
                    dir = '472'
                elif DIRECTOR == 'Kevin Smith':
                    dir = '473'
                elif DIRECTOR == 'Robert Altman':
                    dir = '474'
                elif DIRECTOR == 'Brian Henson':
                    dir = '475'
                elif DIRECTOR == 'James Foley':
                    dir = '476'
                elif DIRECTOR == 'Jon Avnet':
                    dir = '477'
                elif DIRECTOR == 'George Sluizer':
                    dir = '478'
                elif DIRECTOR == 'Bruce Robinson':
                    dir = '479'
                elif DIRECTOR == 'Jean-Jacques Annaud':
                    dir = '480'
                elif DIRECTOR == 'Nicholas Meyer':
                    dir = '481'
                elif DIRECTOR == 'Ted Kotcheff':
                    dir = '482'
                elif DIRECTOR == 'Robert Redford':
                    dir = '483'
                elif DIRECTOR == 'Jim Abrahams':
                    dir = '484'
                elif DIRECTOR == 'Joseph Sargent':
                    dir = '485'
                elif DIRECTOR == 'Robert Clouse':
                    dir = '486'
                elif DIRECTOR == 'John Boorman':
                    dir = '487'
                elif DIRECTOR == 'Don Siegel':
                    dir = '488'
                elif DIRECTOR == 'Brian G. Hutton':
                    dir = '489'
                elif DIRECTOR == 'Gene Saks':
                    dir = '490'
                elif DIRECTOR == 'Cy Endfield':
                    dir = '491'
                elif DIRECTOR == 'Guy Hamilton':
                    dir = '492'
                elif DIRECTOR == 'J. Lee Thompson':
                    dir = '493'
                elif DIRECTOR == 'Georges Franju':
                    dir = '494'
                elif DIRECTOR == 'Charles Vidor':
                    dir = '495'
                elif DIRECTOR == 'James Algar':
                    dir = '496'
                elif DIRECTOR == 'Todd Haynes':
                    dir = '497'
                elif DIRECTOR == 'Aneesh Chaganty':
                    dir = '498'
                elif DIRECTOR == 'Sean Baker':
                    dir = '499'
                elif DIRECTOR == 'Tyler Nilson':
                    dir = '500'
                elif DIRECTOR == 'Sebastian Schipper':
                    dir = '501'
                elif DIRECTOR == 'Deniz Gamze Ergüven':
                    dir = '502'
                elif DIRECTOR == 'Joseph Kosinski':
                    dir = '503'
                elif DIRECTOR == 'Ryan Coogler':
                    dir = '504'
                elif DIRECTOR == 'David Mackenzie':
                    dir = '505'
                elif DIRECTOR == 'Stephen Frears':
                    dir = '506'
                elif DIRECTOR == 'Matt Reeves':
                    dir = '507'
                elif DIRECTOR == 'David Ayer':
                    dir = '508'
                elif DIRECTOR == 'Hiromasa Yonebayashi':
                    dir = '509'
                elif DIRECTOR == 'Bradley Cooper':
                    dir = '510'
                elif DIRECTOR == 'Pierre Coffin':
                    dir = '511'
                elif DIRECTOR == 'Jonathan Levine':
                    dir = '512'
                elif DIRECTOR == 'Daniel Monzón':
                    dir = '513'
                elif DIRECTOR == 'Bennett Miller':
                    dir = '514'
                elif DIRECTOR == 'Ruben Fleischer':
                    dir = '515'
                elif DIRECTOR == 'Dennis Gansel':
                    dir = '516'
                elif DIRECTOR == 'John Lee Hancock':
                    dir = '517'
                elif DIRECTOR == 'David Cronenberg':
                    dir = '518'
                elif DIRECTOR == 'Olivier Dahan':
                    dir = '519'
                elif DIRECTOR == 'Ronny Yu':
                    dir = '520'
                elif DIRECTOR == 'Neil Burger':
                    dir = '521'
                elif DIRECTOR == 'Zack Snyder':
                    dir = '522'
                elif DIRECTOR == 'James Wan':
                    dir = '523'
                elif DIRECTOR == 'Charlie Kaufman':
                    dir = '524'
                elif DIRECTOR == 'Gregg Araki':
                    dir = '525'
                elif DIRECTOR == 'Yann Samuell':
                    dir = '526'
                elif DIRECTOR == 'Marc Forster':
                    dir = '527'
                elif DIRECTOR == 'Eric Bress':
                    dir = '528'
                elif DIRECTOR == 'Kinji Fukasaku':
                    dir = '529'
                elif DIRECTOR == 'Chris Columbus':
                    dir = '530'
                elif DIRECTOR == 'Ted Demme':
                    dir = '531'
                elif DIRECTOR == 'Mary Harron':
                    dir = '532'
                elif DIRECTOR == 'Tom Tykwer':
                    dir = '533'
                elif DIRECTOR == 'Tony Bancroft':
                    dir = '534'
                elif DIRECTOR == 'Alex Proyas':
                    dir = '535'
                elif DIRECTOR == 'Joel Schumacher':
                    dir = '536'
                elif DIRECTOR == 'Jonathan Lynn':
                    dir = '537'
                elif DIRECTOR == 'Marc Caro':
                    dir = '538'
                elif DIRECTOR == 'David Zucker':
                    dir = '539'
                elif DIRECTOR == 'Mark Rydell':
                    dir = '540'
                elif DIRECTOR == 'Walter Hill':
                    dir = '541'
                elif DIRECTOR == 'James Frawley':
                    dir = '542'
                elif DIRECTOR == 'Martin Rosen':
                    dir = '543'
                elif DIRECTOR == 'Wolfgang Reitherman':
                    dir = '544'
                elif DIRECTOR == 'Richard Lester':
                    dir = '545'
                elif DIRECTOR == 'Blake Edwards':
                    dir = '546'
                elif DIRECTOR == 'George Stevens':
                    dir = '547'
                CERTIFICATE = request.form['certificate']
                if CERTIFICATE == 'A':
                    cer = '0'
                elif CERTIFICATE == 'UA':
                    cer = '1'
                elif CERTIFICATE == 'U':
                    cer = '2'
                elif CERTIFICATE == 'PG-13':
                    cer = '3'
                elif CERTIFICATE == 'R':
                    cer = '4'
                elif CERTIFICATE == 'PG':
                    cer = '5'
                elif CERTIFICATE == 'G':
                    cer = '6'
                elif CERTIFICATE == 'Passed':
                    cer = '7'
                elif CERTIFICATE == 'TV-14':
                    cer = '8'
                elif CERTIFICATE == '16':
                    cer = '9'
                elif CERTIFICATE == 'TV-MA':
                    cer = '10'
                elif CERTIFICATE == 'Unrated':
                    cer = '11'
                elif CERTIFICATE == 'GP':
                    cer = '12'
                elif CERTIFICATE == 'Approved':
                    cer = '13'
                elif CERTIFICATE == 'TV-PG':
                    cer = '14'
                elif CERTIFICATE == 'U/A':
                    cer = '15'


                
                IMDB_RATING =float(request.form['rating'])
                NO_OF_VOTES= int(request.form['votes'])
                RUN_TIME = int(request.form['runtime'])
                META_SCORE= float(request.form['score'])
                YEAR = int(request.form['year'])
                model = request.form['model']


                input_variables = pd.DataFrame([[YEAR,MOVIE,GENRE,CERTIFICATE,RUN_TIME,IMDB_RATING,META_SCORE,NO_OF_VOTES,DIRECTOR,STAR1,STAR2,STAR3,STAR4]],
                                               columns=['Released_Year','Series_Title','Genre','Certificate','Runtime','IMDB_Rating','Meta_score','No_of_Votes','Director','Star1','Star2','Star3','Star4'],
                                               index=['input'])
                final_features = input_variables.to_numpy()
                print(final_features)
                print(model)
                
                if model =="Stacking Regressor":
                  prediction =Gross.predict(final_features)
                  print('the prediction',prediction)
                  output = int(prediction[0])
                  result =int(output) * int(output) * int(output)
                  print('result is',result)
                elif model =="Gradient Boosting Regressor":
                  prediction =gbr.predict(final_features)
                  print('prediction',prediction)
                  output = int(prediction[0])

                  result =int(output) * int(output) * int(output)

        return render_template('predict.html',result_prediction=result,model=model)
 
     
@app.route('/chart')
def chart():
	return render_template('chart.html')  

if __name__ == '__main__':
	app.run(debug=True)

                                                        
