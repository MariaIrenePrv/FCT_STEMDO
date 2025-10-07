variable "existent_resource_group_name" {
  type = string
}

variable "vnet_name" {
  type = string
}

variable "vnet_address_space" {
  type = list(string)
}

variable "location" {
  type = string
}

variable "owner_tag" {
  type = string
}

variable "environment_tag" {
  type = string
}

variable "vnet_tags" {
  type = map(string)
}
