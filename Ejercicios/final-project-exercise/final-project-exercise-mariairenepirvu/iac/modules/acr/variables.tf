variable "acr_name" {
  description = "Nombre del Azure Container Registry"
  type        = string
}

variable "resource_group_name" {
  description = "Nombre del grupo de recursos"
  type        = string
}

variable "location" {
  description = "Ubicación del recurso"
  type        = string
}

variable "acr_sku" {
  description = "SKU del ACR"
  type        = string
  default     = "Basic"
}
