module "vnet_vm" {
  source              = "./modules/vnet"
  vnet_name           = "vnet-vms"
  resource_group_name = var.resource_group
  location            = var.location
  address_space       = ["10.0.0.0/16"]
  subnet_prefixes     = ["10.0.1.0/24"]
  subnet_names        = ["subnet-vm"]
}

module "vnet_k8s" {
  source              = "./modules/vnet"
  vnet_name           = "vnet-aks"
  resource_group_name = var.resource_group
  location            = var.location
  address_space       = ["10.1.0.0/16"]
  subnet_prefixes     = ["10.1.1.0/24"]
  subnet_names        = ["subnet-aks"]
}

module "vm_bbdd" {
  source              = "./modules/vm"
  vm_name             = "vm-bbdd"
  location            = var.location
  resource_group_name = var.resource_group
  subnet_id           = module.vnet_vm.subnet_ids[0]
  public_ip_enabled   = false
  vm_size             = "Standard_B1ms"
}

module "vm_backup" {
  source              = "./modules/vm"
  vm_name             = "vm-backup"
  vm_size             = "Standard_B1ms"
  public_ip_enabled   = true
  subnet_id           = module.vnet_vm.subnet_ids[0]
  resource_group_name = var.resource_group
  location            = var.location
}

module "acr" {
  source              = "./modules/acr"
  acr_name            = var.acr_name
  resource_group_name = var.resource_group
  location            = var.location
  acr_sku             = var.acr_sku
}

module "aks" {
  source              = "./modules/aks"
  aks_name            = "aks-cluster"
  location            = var.location
  resource_group_name = var.resource_group
}

resource "azurerm_virtual_network_peering" "aks_to_vms" {
  name                         = "aks-to-vms"
  resource_group_name          = var.resource_group
  virtual_network_name         = module.vnet_k8s.vnet_name
  remote_virtual_network_id    = module.vnet_vm.vnet_id
  allow_forwarded_traffic      = true
  allow_virtual_network_access = true
}

resource "azurerm_virtual_network_peering" "vms_to_aks" {
  name                         = "vms-to-aks"
  resource_group_name          = var.resource_group
  virtual_network_name         = module.vnet_vm.vnet_name
  remote_virtual_network_id    = module.vnet_k8s.vnet_id
  allow_forwarded_traffic      = true
  allow_virtual_network_access = true
}
