terraform {
  backend "azurerm" {
    resource_group_name  = "rg-mipirvu-dvfinlab"
    storage_account_name = "stamipirvudvfinlab"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
