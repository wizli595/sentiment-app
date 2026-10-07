# Grille de décision : faut-il vraiment un modèle ?

## Les quatre critères

| Lettre | Critère | La question à se poser |
| --- | --- | --- |
| (a) | Données étiquetées | A-t-on des exemples annotés, ou peut-on en produire à faible coût ? |
| (b) | Vérifiabilité | La réponse doit-elle être tracée jusqu'à une source ou une règle ? |
| (c) | Coût par requête | Combien d'appels par jour, et que coûte chacun ? |
| (d) | Conséquence d'une erreur | Que se passe-t-il concrètement quand le système se trompe ? |

## L'arbre de choix

Parcourir les questions dans l'ordre ; la première réponse « oui » donne l'approche.

1. La logique est-elle connue, stable, et doit-elle rester explicable ? → **règles métier**
2. Dispose-t-on de données étiquetées pour une tâche répétitive ? → **machine learning**
3. La réponse doit-elle être tirée de documents existants et citée ? → **RAG**
4. Sinon, et seulement sinon → **modèle génératif seul**

On ne saute jamais directement à la dernière ligne : c'est l'option la plus
coûteuse et la moins vérifiable.

## Coût et vérifiabilité comparés

| Approche | Coût par requête | Vérifiabilité |
| --- | --- | --- |
| Règles métier | quasi nul | totale, la règle est lisible |
| Machine learning | très faible | moyenne, on explique par les exemples |
| RAG | moyen | bonne, la source est citée |
| Génératif seul | élevé | faible, d'où la relecture humaine |
