output "acr_login_server" {
  description = "URL del login del ACR"
  value       = azurerm_container_registry.acr.login_server
}

output "acr_id" {
  description = "ID del ACR"
  value       = azurerm_container_registry.acr.id
}
