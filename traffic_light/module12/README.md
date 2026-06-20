# Module 12: Cleanup and Enhancements

In this module we will take a look at some general cleanup to the code.

We will also briefly discuss ideas for expanding the traffic light project.

## Docker

### Environment Variables

The `docker-compose.yml` file repeated the database username, password, as well as some other fields between containers.
While our project is not that large, it still would be beneficial to consolidate these shared variables into a single
maintainable location.

In the [docker](./docker) directory we create a `.env` file.  This is a central location where we can store some of
our values that are used throughout the `docker-compose.yml` is is shown below

```dotenv
DB_HOST=postgres
DB_NAME=traffic_light
DB_USER=postgres
DB_PASS=postgres
MQTT_HOST=mosquitto
```

Now, we can simply reference those values in the `docker-compose.yml` as shown below

```dockerfile
MQTT_HOST: ${MQTT_HOST}
DB_HOST: ${DB_HOST}
DB_NAME: ${DB_NAME}
DB_USER: ${DB_USER}
DB_PASS: ${DB_PASS}
```

### Health Check

Our API contains a "/api/health" endpoint.  We can use this with Docker to ensure the container is "healthy", we add
the `healthcheck` below.

```dockerfile
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5000/api/health"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 10s
```

This means that Docker will run `curl -f http://localhost:5000/api/health` inside the container, every 30 seconds. If no
response is received during the specified timeout of 5 seconds then Docker will retry 3 times before marking the unhealthy as
shown below.

First, we may see that the container is still starting and that the health check isn't active quite yet.

```text
82b11cb49ffd   docker-api            "python app.py"       49 seconds ago   Up 48 seconds (health: starting)                traffic-api
```

Then the container may flip to health

```text
82b11cb49ffd   docker-api             "python app.py"      About a minute ago   Up About a minute (unhealthy)               traffic-api
```

Why would our container be unhealthy?  We are expecting a non-error HTTP status (4xx/5xx) from the server.  However, we
are executing `curl` to get the status.  That does not exist on the container... we can either install it as part of the 
image or take another approach.

Given that at this point we only need `curl` as a health check there is no reason to install it in our container.  

Instead, we can use Python for our check.  Updating our health check to be

```dockerfile
test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"]
```

Now, we can use `docker ps` to check the status of our container and see that it is showing `(healthy)`

```text
db0b2b82e1bd   docker-api                 "python app.py"          35 seconds ago   Up 30 seconds (healthy)
```

## Python

Although our Python program is relatively small, there are still some tweaks we can make.

### Specify HTTP Methods

Our code uses the `@app.route` decorator to specify endpoints as seen below.

```python
@app.route('/health')
```

The framework defaults to the `GET` method which is what we are using.  However, it can make the code more readable to
explicitly list the valid methods.

```python
@app.route('/health', methods=['GET'])
```

Now our intention is clear and we can support other methods as necessary.

### Do not hardcode the database password

We've made changes to specify the password in the `.env` file for Docker.  We retrieve the password for the database
with `os.getenv` but we provide a default value.  This will usually be flagged by security scanners and linters as a
hardcoded password.

```python
'password': os.getenv('DB_PASS',  'postgres'),
```

A simple change for us

```python
'password': os.getenv('DB_PASS'),
```

### Use a mqtt-host 

Instead of constantly having to update our source code, let us start using a `mqtt-host` parameter in `traffic_light.py`

We add the parser argument

```python
    parser.add_argument(
        "--mqtt-host",
        default="localhost",
        metavar="HOST",
        help="Hostname or IP of the MQTT broker (default: localhost)",
    )
```

Then we make use of it

```python
    sm = TrafficLightMachine(mqtt_host=args.mqtt_host)
```

Now we can easily pass in the Docker host system

## JavaScript Changes

A few tweaks to the JavaScript code as well

### Await our initial loads

We call our `loadHistory` and `loadStats` 

```javascript
loadHistory();
loadStats();
```

It is appropriate to use `await` for these

```javascript
await loadHistory();
await loadStats();
```

### Refreshing data

We are making calls without necessarily handling the returned promise.  

```javascript
setInterval(() => { loadHistory(); loadStats(); }, 30_000);
```

We can either handle the promise by using `.then()` 

```javascript
setInterval(() => { loadHistory().then(r => {}); loadStats().then(r => {}); }, 30_000);
```

We can also use `await` as we did previously.

```javascript
setInterval(async () => { await loadHistory(); await loadStats(); }, 30_000);
```

### Using globalThis

We can move away from the use of `window`

```javascript
const mqttClient = mqtt.connect(`ws://${window.location.hostname}:9001`, {
```

Instead, we use `globalThis`

```javascript
const mqttClient = mqtt.connect(`ws://${globalThis.location.hostname}:9001`, {
```