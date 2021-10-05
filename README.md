# EXAMPLES #
## Build API ###

```
docker build -t you_name .
```

**Run API**
```
docker run --rm -ti -d -p 5000:5000 -v $(pwd)/src/api/:/application you_name
```

