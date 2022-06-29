# libOpenClientPy

Biblioteca cliente TCP/IP para comunicação com o OpenServer.

## Uso

Primeiramente importe a biblioteca:

```Python
import libOpenClient as loc
```

### Conectando ao OpenServer

Crie um objeto da classe ```libOpenClient``` passando como parametro uma string contendo o enderço de IP do dispositivo que está sendo executado o OpenServer:

```Python
oc = loc.libOpenClient('200.128.140.15')
```

Caso você esteja usando o OpenServer nó próprio computador, é possível utilizar o localhost para conectá-lo:

```Python
oc = loc.libOpenClient('localhost')
```

Caso não seja passado algum parâmetro, automáticamente será utilizado o localhost:

```Python
oc = loc.libOpenClient()
```

### Lendo Posição Atual

Quando desejar fazer ler a posição do robô em coordenadas cartesianas execute o método salvando um objeto:

```Python
coordenadas_Cartesianas = oc.le_cart()
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
coordenadas_Juntas = oc.le_junta()

print(coordenadas_Juntas.j1)
print(coordenadas_Juntas.j2)
print(coordenadas_Juntas.j3)
print(coordenadas_Juntas.j4)
print(coordenadas_Juntas.j5)
print(coordenadas_Juntas.j6)
```

### Movimentando o robô

Para movimentar o robô usando coordenadas cartezianas use a função ```escreve_le_cart()``` conforme abaixo:

```Python
oc.escreve_le_cart( 797.07 , 0.0 , 1075.0 , 0.0 , 0.0 , 0.0 )
```

Caso você queira realizar a leitura simultaneamente com a escrita:

```Python
coordenadas_Cartesianas = oc.escreve_le_cart( 797.07 , 0.0 , 1075.0 , 0.0 , 0.0 , 0.0 )
```

De forma análoga, para o espaço de juntas do robô:

```Python
oc.escreve_le_junta(0,0,-90,0,90,0)
```

ou

```Python
coordenadas_Juntas = oc.escreve_le_junta(0,0,-90,0,90,0)
```


## Exemplos

Espaço carteziano:

```Python
import time
import libOpenClient as loc

oc = loc.libOpenClient()

coordenadas_Cartesianas = oc.escreve_le_cart( 800 , 0.0 , 1000 , 0.0 , 0.0 , 0.0 )
print("Posição Atual: ")
print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r) )
print("")
print("")
time.sleep(2)

coordenadas_Cartesianas = oc.le_cart()
print("Posição Atual: ")
print("X: " + str(coordenadas_Cartesianas.x) + "\tY: " +  str(coordenadas_Cartesianas.y) + "\tZ: " +  str(coordenadas_Cartesianas.z) + "\ta: " +  str(coordenadas_Cartesianas.a) + "\te: " +  str(coordenadas_Cartesianas.e) + "\tr: " +  str(coordenadas_Cartesianas.r) )
print("")
print("")
```

Espaço de juntas:

```Python
import time
import libOpenClient as loc

oc = libOpenClient('localhost')

coordenadas_Juntas = oc.escreve_le_junta(0,0,-90,0,90,0)
print("Posição Atual: ")
print("J1: " + str(coordenadas_Juntas.j1) + "\tJ2: " + str(coordenadas_Juntas.j2) + "\tJ3: " + str(coordenadas_Juntas.j3) + "\tJ4: " + str(coordenadas_Juntas.j4) + "\tJ5: " +  str(coordenadas_Juntas.j5) + "\tJ6: " + str(coordenadas_Juntas.j6))
print("")
print("")
time.sleep(2)

coordenadas_Juntas = oc.le_junta()
print("J1: " + str(coordenadas_Juntas.j1) + "\tJ2: " + str(coordenadas_Juntas.j2) + "\tJ3: " + str(coordenadas_Juntas.j3) + "\tJ4: " + str(coordenadas_Juntas.j4) + "\tJ5: " +  str(coordenadas_Juntas.j5) + "\tJ6: " + str(coordenadas_Juntas.j6))
print("")
print("")
```


## Licença

Este código fonte está licenciado sob a "Licença Pública para bibliotecas GNU v3.0", para mais informações acesse o arquivo [LICENSE](https://github.com/LabRobotica/libOpenClientPy/blob/main/LICENSE).
