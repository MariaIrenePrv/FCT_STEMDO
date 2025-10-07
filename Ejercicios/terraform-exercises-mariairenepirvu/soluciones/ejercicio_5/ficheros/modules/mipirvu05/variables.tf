variable "existent_resource_group_name" {
  description = "Nombre del resource group ya existente"
  type        = string
}

variable "vnet_name" {
  description = "Nombre de la Virtual Network"
  type        = string
  validation {
    condition     = regex("^vnet[a-z]{3,}tfexercise[0-9]{2,}$", var.vnet_name) != null
    error_message = "El nombre debe comenzar por 'vnt' seguido de más de dos caracteres contenido en el rango `[a-z]` y que termine por `tfexercise` seguido de al menos dos dígitos numéricos. "
  }
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
  nullable    = false
}

variable "environment_tag" {
  description = "Describe el entorno de la VNet"
  type        = string
  nullable    = false

  validation {
    condition     = contains(["DEV","PRO","TES","PRE"], upper(var.environment_tag))
    error_message = "Introduce un entorno válido (dev, pro, tes o pre)."
  }
}

variable "vnet_tags" {
  description = "Describe los tags adicionales que se aplicarán a la VNet"
  type        = map(string)
  default     = {}
  nullable    = false

  validation {
    condition     = alltrue([
      for val in values(var.vnet_tags) :
      val != null && trimspace(val) != ""
    ])
    error_message = "Todos los valores de las tags deben estar rellenados."
  }
}
