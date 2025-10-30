Mise en place d'une infrastructure via Terraform (Infrastructure as code)

# Nova Sentinel - Phase 3 (Version Localhost)

## Objectif
Automatiser le déploiement complet de l'environnement Nova Sentinel sur une VM unique.

## Pipeline
1. **Terraform** simule la création des nœuds.
2. **Ansible** configure le système local.
3. **Vault** gère les secrets sensibles.
4. **Git** assure la traçabilité.

## Commande principale
```bash
./deploy.sh


##Synthèse – Phase Sentinel

1. Exécution de l’agent Sentinel :
Le script script.py a été exécuté automatiquement sur les App Nodes (dans notre cas, sur le localhost). Il collecte les informations système, CPU, mémoire, disque, réseau, et sécurité.

2. Collecte des rapports :
Les rapports JSON et Markdown sont générés dans le dossier reports/. Ils représentent les données collectées et sont assimilés au Monitoring Node.

3. Scénario d’audit :
Un test a été réalisé avec la création d’un fichier SUID /tmp/suspicious_suid et d’un utilisateur UID 500 (testuser).
Le script Sentinel a correctement détecté ces anomalies et les a listées dans le rapport sentinel_report.md.

4. Conclusion :
L’audit Sentinel fonctionne correctement.
Les rapports sont collectés et lisibles.
Le mécanisme d’audit permet de repérer rapidement les éléments suspects (permissions dangereuses, utilisateurs anormaux, ports ouverts).

Améliorations possibles :

Automatiser l’envoi des rapports vers un tableau de bord (Monitoring Node réel).

Ajouter des alertes en cas d’anomalie critique.

Intégrer un chiffrement des rapports ou un transfert sécurisé via Vault.
