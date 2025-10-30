#!/bin/bash
set -e

echo "=== 🚀 Initialisation de Vault en mode développement ==="
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# Lance Vault en arrière-plan (mode dev)
pkill vault 2>/dev/null || true
nohup vault server -dev -dev-root-token-id="root" > /tmp/vault.log 2>&1 &

sleep 5

echo "✅ Vault démarré sur $VAULT_ADDR"
vault status || true

# Crée quelques secrets
vault kv put secret/ssh password="SuperMotDePasse!"
vault kv put secret/api token="azerty123"

# Vérifie qu'ils existent
vault kv list secret
vault kv get secret/ssh
