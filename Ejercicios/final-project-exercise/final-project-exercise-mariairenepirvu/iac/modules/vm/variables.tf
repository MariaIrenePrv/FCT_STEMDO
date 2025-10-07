variable "vm_name" {
  description = "Nombre de la máquina virtual"
  type        = string
}

variable "resource_group_name" {
  description = "Nombre del resource group"
  type        = string
}

variable "location" {
  description = "Ubicación de los recursos"
  type        = string
}

variable "subnet_id" {
  description = "ID de la subred donde se conectará la VM"
  type        = string
}

variable "public_ip_enabled" {
  description = "VM IP pública"
  type        = bool
}

variable "vm_size" {
  description = "Tamaño de la VM (SKU)"
  type        = string
}

variable "ssh_public_key_path" {
  description = "Ruta al archivo de la clave pública SSH"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}
