<div align="center">

# EmuTi

</div>

> Software para testear NRG de una maquina

- [Guia Primer Uso](#guia-primer-uso)
- [Manual de Usuario](#manual-usuario)


---

### Guia Primer Uso

1. #### Requerimientos del Sistema

    Se necesita tener python version mayor o igual a 3.8.10

2. #### Obtener el repositorio

    Existen dos maneras:

    - Clonar el repositorio por medio de SSH o HTTPS

    - Descargar el .zip (luego descomprimirlo)

3. #### Instalación del entorno virtual

    - En caso de no tener permisos
        ```bash
        powershell -ExecutionPolicy Bypass -File .\setup.ps1
        ```

4. #### Ejecutar el programa

    - Ejecutar el archivo main.py
        ```bash
        python main.py
        ```

---

## Manual Usuario

| **Pantalla Principal** | **Elegir Archivo** |
| :---: | :---: |
| ![Alt text](/assets/img/image.png) |  ![Alt text](/assets/img/image-1.png) |

Seleccionamos un excel con el siguiente formato. (Tenes un excel base como ejemplo en la carpeta **assets**)

| SIMBOLO | SIMBOLO | SIMBOLO | SIMBOLO | SIMBOLO | R1 | R2 | R3 | R4 | R5 |
| ------- | ------- | ------- | ------- | ------- | -- | -- | -- | -- | -- |
| FG      | FG      | FG      | FG      | FG      | 23 | 24 | 31 | 9  | 4  |
| FG      | FG      | FG      | FG      | FG      | 13 | 6  | 13 | 27 | 12 |


