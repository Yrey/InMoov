# InMoov

#### --English version below--
## Projet de développement du mimétisme entre une main robotisée InMoov et une main humaine.

### Principe :
La détection des mouvements de la main humaine est réalisée grâce au Leap Motion (https://www.leapmotion.com/). <br />
Le but est de mimer ses mouvements avec une main InMoov créée grâce au design InMoov (http://inmoov.fr/).

La bibliothèque utilisée pour la communication Ordinateur (Python) - Arduino est pyFirmata qui utilise le protocole Firmata.

### Utilisation
#### Contrôle de la main
  _Brancher la carte arduino et le Leap Motion<br />
  _Lancer le service leapd<br />
  _Charger le code arduino StandardFirmata.ino (disponible dans inmoov/Hand/lib/StandardFirmata/) dans l'arduino.<br />
  _Modifier dans le script python control.py  (disponible dans inmoov/Hand/src/) le port de l'arduino avec celui correspondant à votre configuration.<br />
  _Lancer le script python control.py.
  
#### Visualisation des commandes
  _Brancher le Leap Motion<br />
  _Lancer le service leapd<br />
  _Lancer le script python display.py.

### Branchements
Les branchements des servos sont fais comme ci-dessous : <br />
    _pouce => digital pin 2 <br />
    _index => digital pin 3 <br />
    _majeur=> digital pin 4 <br />
    _annulaire => digital pin 5 <br />
    _auriculaire => digital pin 6 <br />
    _poignet => digital pin 10 <br /> <br />

#### --English version--
## Developpement project aiming to mime human hand moves with an InMoov robotic hand.

### Principle :
The detection of the human hand moves is done with a Leap Motion (https://www.leapmotion.com/). <br />
The aim is to mime those moves with a InMoov hand built thanks to the InMoov designs (http://inmoov.fr/).

The library used to send data between the computer (Python) and the Arduino is pyFirmata which implements the Firmata protocol.

### Use
#### Control of the hand
  _Connect the Arduino board and the Leap Motion<br />
  _Launch the service leapd<br />
  _Load the Arduino script StandardFirmata.ino (available in inmoov/Hand/lib/StandardFirmata/) in the Arduino.<br />
  _Modify in the Python script control.py  (available in inmoov/Hand/src/) The Arduino port with the one matching your configuration.<br />
  _Launch the Python script control.py.
  
#### Display the commands
  _Connect the Leap Motion<br />
  _Launch the service leapd<br />
  _Launch the Python script display.py.
  
### Hardware
The connections of the servos are made as below: <br />
    _thumb => digital pin 2 <br />
    _index => digital pin 3 <br />
    _middle => digital pin 4 <br />
    _ring => digital pin 5 <br />
    _pinky => digital pin 6 <br />
    _wrist => digital pin 10 
