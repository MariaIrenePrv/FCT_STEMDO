variable "vnet_name" {
  description = "Nombre de la VNet"
  type        = string
}

variable "address_space" {
  description = "Espacio de direcciones IP para la VNet"
  type        = list(string)
}

variable "subnet_names" {
  description = "Lista de nombres de subredes"
  type        = list(string)
}

variable "subnet_prefixes" {
  description = "Lista de prefijos CIDR para las subredes"
  type        = list(string)
}

variable "location" {
  description = "Ubicación del recurso"
  type        = string
}

variable "resource_group_name" {
  description = "Nombre del grupo de recursos"
  type        = string
}
