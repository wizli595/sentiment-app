# Fiche de cadrage (exemple corrigé) : Tri des courriels de support

> Exemple rempli, pour calibrer le niveau attendu : une à trois phrases par rubrique, les critères cités par leur lettre.

## Besoin en une phrase (obligatoire)

Router automatiquement chaque courriel de support vers l'équipe compétente (facturation, technique, compte) au lieu d'un tri manuel le matin.

## Utilisateur final (obligatoire)

Les agents du support, qui reçoivent directement les courriels de leur périmètre au lieu de piocher dans une boîte commune.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) Trois ans d'historique de courriels déjà classés par les agents fournissent des dizaines de milliers d'exemples étiquetés gratuits. (c) Plusieurs centaines de courriels par jour : un classifieur entraîné coûte une fraction de centime par courriel. (d) Un courriel mal routé est simplement re-routé par l'agent, sans conséquence grave.

## Données nécessaires et leur origine (obligatoire)

L'historique des courriels avec l'équipe qui les a traités, exporté de l'outil de ticketing, anonymisé avant usage : adresses, signatures et pièces jointes retirées.

## Métrique de succès et seuil d'acceptation (obligatoire)

Exactitude de routage mesurée sur un jeu de test de 2 000 courriels tenus à l'écart : acceptation à partir de 0,85, le tri manuel actuel étant estimé à 0,92.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un courriel mal routé attend quelques heures de plus avant d'être re-routé. Chaque agent peut requalifier un courriel d'un clic, et ces requalifications alimentent le réentraînement mensuel.

## Risques éthiques ou de confidentialité (obligatoire)

Les courriels contiennent des données personnelles : anonymisation avant stockage, conservation limitée à douze mois, et aucun envoi à un service externe.

## Approche écartée et pourquoi (facultatif)

Les règles par mots-clés : les premiers essais plafonnaient à 70 pour cent d'exactitude, car le vocabulaire des clients déborde toute liste de mots-clés maintenue à la main.
