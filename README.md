## Cómo instalar e inicializar el proyecto

1. Clona el repositorio

```
git clone https://github.com/NbdyKnows/FASTAPI-songs.git
```

2. Crea un entorno virutal con venv

```
python -m venv env
```
_En caso no cuentes con venv, instálalo con:_

```
pip install venv
```

3. Actívalo

```
env\Scripts\Activate
```

4. Instala las dependencias

```
pip install -r requirements.txt.
```

5. No olvides crear la base de datos de forma local y cambiar el archivo db.py en la variable engine por:
   
```
engine = "mysql+pymysql://usuario:contraseña@localhost:puerto-BD)/base_datos"
```

6. Ejecuta el comando `fastapi dev app.py` para iniciar el servidor 
