```https://github.com/gseganzerla/mlops.git``` -> backend (api)

`https://github.com/gseganzerla/mlops-front.git` -> frontned

Montar e iniciar containers

```docker compose up -d --build```



# Montar Imagem

```docker build -t node/front:latest .```

# Iniciar Container
### (Modificar portas se necessario)
```docker run -p 8080:8080  node/front:latest``` 