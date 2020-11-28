# Skateboard API
This is a API for fetching random skateboard tricks. 

1. [Usage](#usage)
2. [api/v1/basic](#api-v1-basic)
3. [api/v1/advanced](#api-v1-advanced)
4. [api/v1/insane](#api-v1-insane)
5. [TODOs](#todos)


## Usage
Install requirements:
```sh
pip3 install -r requirements.txt
```

Then run the api:
```sh
python3 app.py
```

Finally, run the frontend:
```sh
python3 -m http.server
```
Should now be available at [localhost:8000](http://localhost:8000).

## api/v1/basic
Includes only one trick combination
```
api/v1/basic/flip
api/v1/basic/grind
api/v1/basic/manual
```

#### Example response
```json
# /flip
{
  "payload": "FS Pop-shuvit"
}

# grind
{
  "payload": "BS Blunt"
}

# manual
{
  "payload": "Nollie Nosemanual"
}
```

## api/v1/advanced
Includes two trick combinations
```
api/v1/advanced/flip 
api/v1/advanced/grind
api/v1/advanced/manual
```

#### Example response
```json
# /flip
{
  "payload": "Fakie FS 180 Varialflip"
}

# grind
{
  "payload": "Nollie BS 180 Noseslide"
}

# manual
{
  "payload": "Fakie 180 Nosemanual"
}
```

## api/v1/insane
Includes three or more trick combinations
```
api/v1/insane/flip
api/v1/insane/grind
api/v1/insane/manual
```

#### Example response
```json
# /flip
{
  "payload": "Switch BS 360 Inward pressureflip"
}

# grind
{
  "payload": "FS 360 Fingerflip FS Willie"
}

# manual
{
  "payload": " FS 180 Hardflip Manual"
}
```

## TODOs
- [ ] Advanced endpoint can be very insane sometimes! :shrug: