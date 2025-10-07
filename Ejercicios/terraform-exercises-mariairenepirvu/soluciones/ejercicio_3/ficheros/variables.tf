variable "existent_resource_group_name" {
  description = "Nombre del resource group ya existente"
  type        = string
}

variable "vnet_name" {
  description = "Nombre de la Virtual Network"
  type        = string
}

variable "vnet_address_space" {
  description = "Dirección CIDR de la VNet"
  type        = list(string)
}

variable "location" {
  description = "Región de Azure para desplegar la VNet"
  type        = string
  default     = "West Europe"
}

variable "owner_tag" {
  description = "Describe el propietario de la VNet"
  type        = string
}

variable "environment_tag" {
  description = "Describe el entorno de la VNet"
  type        = string
}

variable "vnet_tags" {
  description = "Describe los tags adicionales que se aplicarán a la VNet"
  type        = map(string)
  default     = {}
}
