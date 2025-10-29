provider "vsphere" {
  # Configuration du provider
}

resource "vsphere_virtual_machine" "app1" {
  name             = "app-node1"
#  resource_pool_id = "ID_DU_RESOURCE_POOL"     # à remplacer
#  datastore_id     = "ID_DU_DATASTORE"         # à remplacer
  guest_id         = "ubuntu64Guest"           # type d'OS invité
  num_cpus         = 2
  memory           = 2048

  network_interface {
    network_id   = "ID_DU_RESEAU"              # à remplacer
    adapter_type = "vmxnet3"
  }

  disk {
    label            = "disk0"
    size             = 20
    thin_provisioned = true
  }

  cdrom {
    datastore_id = "ID_DU_DATASTORE"           # à remplacer
    path         = "ubuntu-22.04.iso"          # image ISO dans ton datastore
  }

  # Personnalisation via cloud-init (création de l'utilisateur sam)
  extra_config = {
    "guestinfo.userdata" = <<-EOF
      #cloud-config
      users:
        - name: sam
          passwd: $(openssl passwd -6 a)
          shell: /bin/bash
          sudo: ALL=(ALL) NOPASSWD:ALL
      chpasswd:
        expire: false
    EOF
    "guestinfo.userdata.encoding" = "base64"
  }
}

output "app1_ip" {
  value = "192.168.198.143"
}
