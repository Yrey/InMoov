# InMoov

## English version below
## Projet de développement du mimétisme entre une main robotisée InMoov et une main humaine.

### Principe :
La détection des mouvements de la main humaine est réalisée grâce au Leap Motion (https://www.leapmotion.com/). <br />
Le but est de mimer ses mouvements avec une main InMoov créée grâce au design InMoov (http://inmoov.fr/).

La bibliothèque utilisée pour la communication Ordinateur (Python) - Arduino est pyFirmata qui utilise le protocole Firmata.

### Utilisation
  _Charger le code arduino StandardFirmata.ino (disponible dans inmoov/Hand/lib/StandardFirmata/) dans l'arduino.<br />
  _Modifier dans le script python control.py  (disponible dans inmoov/Hand/src/) le port de l'arduino avec celui correspondant à votre configuration.<br />
  _Lancer le script python control.py.
  
### Branchements
A compléter

## English version
## Developpement project aiming to mime human hand moves with an InMoov robotic hand.

### Principle :
The detection of the human hand moves is done with a Leap Motion (https://www.leapmotion.com/). <br />
The aim is to mime those moves with a InMoov hand built thanks to the InMoov designs (http://inmoov.fr/).

The library used to send data between the computer (Python) and the Arduino is pyFirmata which implements the Firmata protocol.

### Use
  _Load the Arduino script StandardFirmata.ino (available in inmoov/Hand/lib/StandardFirmata/) in the Arduino.<br />
  _Modify in the Python script control.py  (available in inmoov/Hand/src/) The Arduino port with the one matching your configuration.<br />
  _Launch the Python script control.py.
  
### Hardware
To complete
