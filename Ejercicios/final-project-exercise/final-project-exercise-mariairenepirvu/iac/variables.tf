variable "resource_group" {
  description = "Nombre del resource group"
  type        = string
}

variable "location" {
  description = "Ubicación de los recursos"
  default     = "westeurope"
}

variable "admin_username" {
  description = "Usuario administrador de las VMs"
  type        = string
}

variable "admin_password" {
  description = "Contraseña del usuario administrador"
  type        = string
  sensitive   = true
}

variable "name" {
  description = "Nombre base"
  type        = string
}

variable "acr_name" {
  description = "Nombre del Azure Container Registry"
  type        = string
}

variable "acr_sku" {
  description = "SKU del ACR"
  type        = string
  default     = "Basic"
}

