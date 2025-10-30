terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

# App Node 1
resource "local_file" "node1" {
  content  = "App Node 1 créé - Agent Sentinel"
  filename = "${path.module}/app-node1.txt"
}

# App Node 2
resource "local_file" "node2" {
  content  = "App Node 2 créé - Agent Sentinel"
  filename = "${path.module}/app-node2.txt"
}

# Monitoring Node (héberge Vault)
resource "local_file" "monitoring_node" {
  content  = "Monitoring Node créé - Vault + Supervision"
  filename = "${path.module}/monitoring-node.txt"
}


# Output d'une IP fictive (localhost)
output "node_ip" {
  value = "127.0.0.1"
}
