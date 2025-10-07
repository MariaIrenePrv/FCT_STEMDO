existent_resource_group_name = "rg-mipirvu-dvfinlab"
vnet_name                    = "vnetmipirvutfexercise04"
vnet_address_space           = ["10.0.0.0/16"]
owner_tag                    = "Irene"
environment_tag              = "dev"
vnet_tags = {
    proyecto = "ejercicios-terraform"
    owner = "Irene 2.0" # Sobreescribe el owner_tag
 
}

