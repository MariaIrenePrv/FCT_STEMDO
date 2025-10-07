# Proveedor Azure 
provider "azurerm" {
  features {} # Requerido por el proveedor 
}

# Saca información sobre un resource group
data "azurerm_resource_group" "rg" {
  name = var.existent_resource_group_name # Variable resource group
}

# Creación Virtual Network 
resource "azurerm_virtual_network" "vnet" {
  name                = var.vnet_name 
  location            = var.location
  resource_group_name = data.azurerm_resource_group.rg.name
  address_space       = var.vnet_address_space
}
