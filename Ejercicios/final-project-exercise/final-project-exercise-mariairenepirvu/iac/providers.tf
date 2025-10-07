provider "azurerm" {
  features {}
}

provider "tls" {
}

terraform {
  required_version = ">= 1.5.0"
}
