# 📚 Sistema de Biblioteca en Python

Este proyecto implementa un sistema de gestión de biblioteca en Python, utilizando los **cuatro pilares de la Programación Orientada a Objetos (POO)**: **abstracción, encapsulamiento, herencia y polimorfismo**.  

Permite gestionar usuarios, materiales (libros y revistas), préstamos y devoluciones con cálculo automático de penalizaciones por retraso.

---

## 🚀 Cómo ejecutar

1. Clona o descarga este repositorio.  
2. Asegúrate de tener instalado **Python 3.8 o superior**.  
3. Ejecuta el programa con:

```bash
python biblioteca.py
```

---

## 📌 Menú principal

Al ejecutar el programa, verás el siguiente menú:

```
--- Menú Biblioteca ---
1. Agregar usuario
2. Agregar libro
3. Agregar revista
4. Prestar material
5. Devolver material
6. Listar usuarios
7. Listar materiales
8. Listar préstamos
0. Salir
```

---

## 📝 Comandos de ejemplo

### 1. Agregar usuario
```
ID usuario: U001
Nombre: Juan Pérez
```

### 2. Agregar libro
```
ID material: L001
Título: Cien años de soledad
Autor: Gabriel García Márquez
Stock: 2
```

### 3. Agregar revista
```
ID material: R001
Título: National Geographic
Stock: 5
```

### 4. Prestar material
```
ID usuario: U001
ID material: L001
```

### 5. Devolver material
```
ID usuario: U001
ID material: L001
```

El sistema calculará automáticamente la penalización si hubo retraso.

---

## 🎯 Evidencia de los 4 Pilares de la POO

1. **Abstracción**  
   - Se modelan conceptos del mundo real (usuarios, materiales, libros, revistas, préstamos, biblioteca).  
   - Ejemplo: la clase `Material` representa de manera general cualquier recurso de la biblioteca.  

2. **Encapsulamiento**  
   - Los atributos están definidos con guion bajo (`_id_material`, `_stock`, `_usuario`), protegiendo los datos internos.  
   - El acceso se da a través de métodos (`prestar()`, `devolver()`, `mostrar_info()`), no directamente.  

3. **Herencia**  
   - `Libro` y `Revista` heredan de `Material`, reutilizando atributos y métodos comunes.  
   - Ejemplo: ambos heredan `mostrar_info()` pero lo especializan.  

4. **Polimorfismo**  
   - Los métodos `mostrar_info()`, `get_plazo()` y `get_multa_por_dia()` se redefinen en cada subclase (`Libro`, `Revista`) con comportamientos distintos.  
   - Ejemplo: un libro tiene plazo de **14 días** con multa de **$300/día**, mientras que una revista tiene **7 días** con multa de **$200/día**.  

---

## 📖 Ejemplo de ejecución

```
--- Menú Biblioteca ---
1. Agregar usuario
2. Agregar libro
3. Agregar revista
4. Prestar material
5. Devolver material
6. Listar usuarios
7. Listar materiales
8. Listar préstamos
0. Salir
Seleccione una opción: 1
ID usuario: U001
Nombre: Ana Gómez
Usuario agregado.
```

---

## ✅ Conclusión

Este sistema muestra claramente cómo aplicar los principios de la **Programación Orientada a Objetos (POO)** en un caso práctico de gestión de biblioteca, facilitando la escalabilidad y mantenibilidad del código.
