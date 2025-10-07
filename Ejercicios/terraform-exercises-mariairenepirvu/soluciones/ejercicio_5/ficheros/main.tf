module "mipirvu05" {
  source                        = "./modules/mipirvu05"
  existent_resource_group_name = var.existent_resource_group_name
  vnet_name                    = var.vnet_name
  vnet_address_space           = var.vnet_address_space
  location                     = var.location
  owner_tag                    = var.owner_tag
  environment_tag              = var.environment_tag
  vnet_tags                    = var.vnet_tags
}
