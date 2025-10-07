# Readme Ejercicio semanal de Terraform

## Introducción

Este repositorio contiene las soluciones para el **ejercicio semanal** de Terraform. El objetivo principal es desarrollar un módulo que permita desplegar una infraestructura en Microsoft Azure y automatizar su uso mediante workflows de GitHub Actions.

⚠️ **Importante:**
- Nunca incluyas **secretos** en texto plano en tus soluciones. Utiliza mecanismos seguros como los secretos de GitHub para almacenar y acceder a información sensible.
- Recuerda siempre ejecutar `terraform destroy` al finalizar las pruebas para evitar costes innecesarios.
- Usa un archivo `.gitignore` para evitar subir archivos innecesarios o con información sensible.

---
## Objetivos

1. Desarrollar un módulo de Terraform que implemente:
    - Múltiples máquinas virtuales configuradas mediante un mapa de objetos.
    - Un balanceador de carga para distribuir tráfico entre las máquinas virtuales.
    - Elementos de red necesarios para completar la solución.
2. Documentar el módulo en un archivo `README.md` con instrucciones detalladas de uso.
3. Crear un segundo repositorio de GitHub con:
    - Workflows de GitHub Actions para ejecutar automáticamente `terraform plan` y `terraform apply`.
    - Opcionalmente, permitir la ejecución manual de `plan/apply/destroy`.
4. Incluir un ejemplo funcional del módulo en el segundo repositorio.

## Estructura del Repositorio
La estructura de las carpetas de soluciones debe seguir el siguiente formato:

```
soluciones/
├── modulo-weekly-exercise/
│   ├── README.md         # Documentación del módulo de Terraform.
│   ├── main.tf           # Configuración principal del módulo.
│   ├── variables.tf      # Variables utilizadas por el módulo.
│   ├── outputs.tf        # Salidas del módulo.
│   ├── examples/         # Ejemplo(s) de uso del módulo.
│   │   └── example.tf    # Configuración de ejemplo.
│   ├── .gitignore        # Configuración para excluir archivos sensibles.
│   └── terraform.lock.hcl
└── workflows/
    ├── README.md         # Guía para los workflows de GitHub Actions.
    ├── plan-pr.yaml      # Workflow para ejecutar terraform plan en PRs.
    ├── apply-main.yaml   # Workflow para ejecutar terraform apply en merges.
    └── manual-exec.yaml  # Workflow para ejecuciones manuales.

```
## Pautas para Entregables

1. **Documentación:** Cada carpeta debe incluir un archivo `README.md` con pasos detallados de implementación.
2. **Seguridad:** Excluye secretos de los archivos visibles. Usa `.gitignore` y secretos de GitHub.
3. **Código:** Sigue buenas prácticas de Terraform (nombres descriptivos, modularidad, etc.).
4. **Pruebas:** Finaliza todas las pruebas con `terraform destroy`.
