# libOpenClientPy

Biblioteca cliente TCP/IP para comunicação com o OpenServer.

## Uso

Crie um objeto da classe 'libOpenClient' passando como parametro uma string contendo o enderço de IP do dispositivo que está sendo executado o OpenServer:

```Python
oc = libOpenClient('localhost')
```

Quando desejar fazer um listen em coordenadas cartesianas execute o método salvando um objeto:

```Python
coordenadas_Cartesianas = oc.listen_cart()
```

Para acessar o valor de cada coordenada específica:

```Python
print(coordenadas_Cartesianas.x)
print(coordenadas_Cartesianas.y)
print(coordenadas_Cartesianas.z)
print(coordenadas_Cartesianas.a) # Angulos
print(coordenadas_Cartesianas.e) # De
print(coordenadas_Cartesianas.r) # Euler
```

De forma analoga ao anterior, porém em coordenadas no espaço de juntas:

```Python
coordenadas_Juntas = oc.listen_junta()

print(coordenadas_Juntas.j1)
print(coordenadas_Juntas.j2)
print(coordenadas_Juntas.j3)
print(coordenadas_Juntas.j4)
print(coordenadas_Juntas.j5)
print(coordenadas_Juntas.j6)
```

## Licença

Este código fonte está licenciado sob a "Licença Pública Geral GNU v3.0", para mais informações acesse o arquivo [LICENSE](https://github.com/LabRobotica/libOpenClientPy/blob/main/LICENSE).
