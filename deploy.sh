#!/bin/bash
set -e
echo "===  DÉPLOIEMENT NOVA SENTINEL COMPLET (LOCALHOST) ==="

# Terraform
cd test
terraform init -input=false
terraform apply -auto-approve

# Ansible
cd ../ansible
ansible-playbook -i inventory.ini setup.yml

# Vault
cd ../vault
./init.sh

echo " Déploiement complet terminé avec succès !"
