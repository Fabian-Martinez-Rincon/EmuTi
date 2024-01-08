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

### Manual Usuario

| **Pantalla Principal** | **Elegir Archivo** |
| :---: | :---: |
| ![Alt text](/assets/img/image.png) |  ![Alt text](/assets/img/image-1.png) |

Seleccionamos un excel con el siguiente formato. (Tenes un excel base como ejemplo en la carpeta **assets**)

| SIMBOLO | SIMBOLO | SIMBOLO | SIMBOLO | SIMBOLO | R1 | R2 | R3 | R4 | R5 |
| ------- | ------- | ------- | ------- | ------- | -- | -- | -- | -- | -- |
| FG      | FG      | FG      | FG      | FG      | 23 | 24 | 31 | 9  | 4  |
| FG      | FG      | FG      | FG      | FG      | 13 | 6  | 13 | 27 | 12 |


- **SIMBOLO:** Es el simbolo que tiene el rodillo de la maquina.
- **R:** Es el nro que representa el rodillo de la maquina.

Da igual si el excel tiene otros campos, solo es importante que tenga los solicitados.

---

<table>

<tr><td>Pantalla Principal</td><td>Explicación</td></tr>

<tr><td>

![Alt text](/assets/img/image-2.png)
</td><td>

#### Manual

Al dar click, ingresa el primer dato del excel en la ventana definida

#### Automatico

Funciona igual que el manual pero presiona el boton de forma automatica cada **x** tiempo

#### Ventana

Ingresamos el nombre de la ventana en donde queremos ingresar los datos, por ejemplo **Ingrese una combinación** 

#### Indice Nuevo

Durante las pruebas se puede dar que uno quiero no seguir el orden implicito del excel y saltearse jugadas o empezar desde jugadas más avanzadas. Entonces podemos actualizar el indice de la jugada que queremos empezar a probar.

</td></tr>

</table>

### Modo Manual

https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/a1616a21-17e3-4d70-b54b-98c90eedbc7a


### Modo Automatico

https://github.com/Fabian-Martinez-Rincon/EmuTi/assets/55964635/9e3342de-a281-481a-9962-237bc6638854
