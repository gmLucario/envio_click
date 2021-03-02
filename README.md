# EndPoints Ejercicios vacante

## UP Project
At envio_click/
```sh
sudo up_containers.sh
```

## STOP Project
At envio_click/
```sh
sudo kill_containers.sh
```

## Useful links
Description | Link 
--- | --- 
MONGO | http://127.0.0.1:20048/
SWAGGER_DOC | http://127.0.0.1:8000/docs


## Run Tests
At envio_click/
```sh
pytest
```


## Ejercicios
- A1: ```src/handlers/section_a.py->get_vowels_summary```
- A2: X
- A3: ```src/tests/test_vowels.py```
- B2:

    Se optó por MongoDB y serían tres modelos

        Primer modelo: truck (TruckSchema) ** almacenar

        Un catálogo de camiones

        - motor_serial: str                     - Será usado como id (numero serie motor)
        - branch: str                           - Informativo

        Segundo modelo: truc_details (TruckDetailsSchema)

        Detalles del camion conducido

        - truck_motor_serial: str               - Numero serie motor
        - init_date: datetime                   - Fecha fue asignado
        - end_date: datetime                    - Fecha límite poder usarlo

        Tercer modelo: worker (WorkerSchema) ** almacenar

        Almacenar información del trabajador así como de los camiones que tiene
        asignados y el que conduce

        - curp: str                             - Será usado como id
        - fullname: str                         - Informativo
        - assigned_trucks: List[str]            - Lista de numeros de motor
        - driving_truck: TruckDetailsSchema     - Información del camion manejado

- B3
    Se puede hacer un CRON para eliminar el driving_truck a los conductores, si 
    ya se venció
    Validaciones usuales: asiganr solo camiones del catálogo, 

- C1:
    1. remover la subscripción cuando se caduce la subscripción

- C2:
    1. Flake8 arrojó de líneas muy largas. Por el nombre de las variables no podría reducirse mucho.
    En ocasiones es mejor tener variables largas pero entendibles
    2. Se usó [wily](https://wily.readthedocs.io/en/latest/?badge=latest#) para el análisis de complejidad:

        2.1 Cyclomatic Complexity: 4-7 en promedio

        2.2 Maintainability Index: 67 en promedio

    El princiopal cambio que buscaría sería reducir el número de loops, de momento


## Principales herramientas
- FastAPI
- Pydantic
- uvicorn
- AsyncIOMotorClient
- docker y docker-compose
- git 


## Requirements
```sh
assets/requirements.txt
```