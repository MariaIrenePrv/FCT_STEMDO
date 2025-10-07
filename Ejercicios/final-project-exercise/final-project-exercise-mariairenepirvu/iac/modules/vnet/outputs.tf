output "vnet_id" {
  description = "ID de la VNet"
  value       = azurerm_virtual_network.vnet.id
}

output "subnet_ids" {
  description = "Lista de IDs de las subredes"
  value       = [for s in azurerm_subnet.subnets : s.id]
}

output "vnet_name" {
  value = azurerm_virtual_network.vnet.name
}