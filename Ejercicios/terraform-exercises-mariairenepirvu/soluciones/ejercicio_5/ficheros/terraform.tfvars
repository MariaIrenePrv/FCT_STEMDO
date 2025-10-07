existent_resource_group_name = "rg-mipirvu-dvfinlab"
vnet_name                    = "vnetmipirvutfexercise05"
vnet_address_space           = ["10.0.0.0/16"]
owner_tag                    = "Irene"
environment_tag              = "dev"
location = "West Europe"
vnet_tags = {
    proyecto = "ejercicios-terraform"
    owner = "Irene 2.0" # Sobreescribe el owner_tag
 
}

