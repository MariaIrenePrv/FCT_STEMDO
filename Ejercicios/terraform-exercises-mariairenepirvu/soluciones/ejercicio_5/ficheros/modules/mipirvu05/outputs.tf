output "vnet_id" {
  description = "ID de la Virtual Network"
  value       = azurerm_virtual_network.vnet.id
}

output "vnet_name" {
  description = "Nombre de la Virtual Network"
  value       = azurerm_virtual_network.vnet.name
}
