# Rapport de Performance du Modèle SmartPrice

## 4. Description du Modèle

Le modèle actuellement implémenté dans le projet est un **RandomForestRegressor** (Régression par Forêts Aléatoires), utilisant les trois variables explicatives suivantes :
*   **RM** (Nombre de pièces)
*   **DIS** (Distance aux centres d'emplois)
*   **LSTAT** (Statut socio-économique)

Le choix du **RandomForestRegressor** (remplaçant la régression linéaire initiale) se justifie par :
1.  **Gestion de la non-linéarité** : Capable de capturer des relations complexes entre les variables que la régression linéaire ne voit pas.
2.  **Robustesse** : Moins sensible aux valeurs aberrantes (outliers) grâce au principe de moyenne sur plusieurs arbres.
3.  **Performance accrue** : Offre généralement une meilleure précision (RMSE plus fiable) sur ce type de données immobilières.
4.  **Flexibilité** : Ne nécessite pas de transformation lourde des données (comme la normalisation stricte) comparé à des modèles linéaires.

Le modèle a été entraîné sur une division **80% (entraînement) / 20% (test)** du dataset.

### Paramètres du Modèle (Importance des Variables)
Contrairement à une régression linéaire qui possède des coefficients fixes (+/-) et un intercept, le RandomForest calcule l'**importance** (poids relatif) de chaque variable dans la construction des arbres.

*   **Importance de LSTAT** : 0.5612
*   **Importance de RM** : 0.3131
*   **Importance de DIS** : 0.1257
*   **Intercept** : *Non applicable pour un modèle de Forêts Aléatoires (la prédiction est la moyenne des feuilles des arbres).*

________________________________________

## 5. Métriques d’Évaluation

Comme il s’agit d’une problématique de régression, les métriques calculées sur le jeu de test sont :

*   **MAE (Mean Absolute Error)** : 3.0847
*   **MSE (Mean Squared Error)** : 14.0487
*   **RMSE (Root Mean Squared Error)** : 3.7482

### Analyse :
*   **MAE** : Le modèle commet en moyenne une erreur d'environ **3 080 $** sur ses prédictions.
*   **RMSE** : La RMSE de 3.75 montre que les grandes erreurs restent contrôlées.
*   **Conclusion** : Les performances montrent que la combinaison **RM–DIS–LSTAT** exploitée par le **RandomForest** fournit un modèle très cohérent et fiable pour ce mini-projet, surpassant généralement une approche linéaire simple.
