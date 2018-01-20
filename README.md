# InMoov

## Projet de développement du mimétisme entre une main InMoov et une main humaine.

### Principe :
La détection des mouvements de la main humaine est réaliser grâce au Leap Motion (https://www.leapmotion.com/).
Le but est de mimer ses mouvements avec une main InMoov créée grâce au design InMoov (http://inmoov.fr/).

La bibliothèque utiliser pour la communication Ordinateur (Python) - Arduino est pyFirmata qui utilise le protocole Firmata.

### Utilisation
  _Charger le code arduino StandardFirmata.ino (disponible dans inmoov/Hand/lib/StandardFirmata/) dans l'arduino.
  _Modifier dans le script python control.py  (disponible dans inmoov/Hand/src/) le port de l'arduino avec celui correspondant à votre configuration.
  _Lancer le script python control.py.
  
### Branchements

