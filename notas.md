# Notas

## Semana 1, día 1: entorno, git y primer test

### Aprendí
- **venv**: crea un Python aislado por proyecto. Sin él, todos los proyectos comparten librerías y una versión puede romper otro proyecto.
- **Floats**: se guardan en binario y 0.1 en binario es infinito, por eso `0.1 + 0.2 = 0.30000000000000004`. Para dinero: `round(x, 2)` o `Decimal`.
- **return vs raise**: `return` entrega un resultado y el programa sigue. `raise` detiene el programa con un error. Ante un dato inválido es mejor `raise`, para que el error no pase desapercibido.
- **TDD**: primero el test, después el código. El test define qué debe hacer la función. Verlo fallar demuestra que el test realmente prueba algo.
- **Funciones anidadas**: se evalúan de adentro hacia afuera. `round(sum(gastos), 2)` primero suma y luego redondea.
- **Bucles**: no se puede comparar una lista con un número; hay que recorrerla con `for` y revisar cada elemento.
- **git**: `add` prepara, `commit` guarda. `git rm --cached` saca un archivo de git sin borrarlo del disco.
- **.gitignore**: `.venv/` y `__pycache__/` no se suben nunca; se regeneran solos.

### No entendí del todo
- Por qué TDD importa en la práctica y no solo en teoría.
- Cuándo usar `Decimal` en vez de `round`.

### Sigue
- Día 2: función `promedio` con TDD, ramas y GitHub.