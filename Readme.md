# Data Enginner Proyects
> Este repo es para trabajar con proyectos de data engineer adicionas de su ruta adicional agregado los casos de uso mas comunes en esta area

## Prerequisitos
> Para efectuar los siguientes codigos se necesita lo siguientes items: 
* Docker
* Visual Code o ide de su preferencia
* python

## Servicios Utilizados
 * [Airflow](./Airflow/)
 * [Kafka](./kafka/)
 * [Postgres](./PG/)
 * [Spark](./Spark/)
 * [Steamlit](./Steamlit/)
 * [Files](./src/)

## Arquitectura Utilizada
![Arquitetura](./src/Arquitectura.svg)

### Instalador de componentes
Se encuenta un archivo makefile para simplicar la vida a la hora de levantar la infraestrutura

1. Levantar el servicio de kafka con el siguiente comando 
``` bash
make kaf_up
```
2. Levantar la Base de Datos

``` bash
make pg_go
```
3. Levantar Spark

``` bash
make spk_build
```

``` bash
make spk_up
```
4. Levantar Aiflow

``` bash
make afl_up
```

5. Levantar Streamlit

``` bash
make streamlit_up
```

Para mas intrucciones ver el video End to End en el siguiente enlace: 
    - []




