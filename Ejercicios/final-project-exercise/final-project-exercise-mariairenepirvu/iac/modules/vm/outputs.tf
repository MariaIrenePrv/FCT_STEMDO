output "vm_id" {
  description = "ID de la máquina virtual"
  value       = azurerm_linux_virtual_machine.vm.id
}

output "public_ip_address" {
  description = "IP pública de la VM"
  value       = var.public_ip_enabled ? azurerm_public_ip.vm_public_ip[0].ip_address : null
}

output "private_ip_address" {
  description = "IP privada de la VM"
  value       = azurerm_network_interface.nic.private_ip_address
}
