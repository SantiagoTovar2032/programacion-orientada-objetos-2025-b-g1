"""
Sistema de Gestión de Inventario de Hogar
Main module - Punto de entrada de la aplicación
"""
import json
import os
from typing import List, Dict, Any
from datetime import datetime

from entities.objetos_hogar import (
    Electrodomestico, Herramienta, Ropa, Mueble, UtensilioCocina, ArticuloLimpieza
)
from entities.categorias import Categoria, EstadoConservacion

class Habitacion:
    """Representa una habitación con sus objetos (composición)"""
    
    def __init__(self, nombre: str, metros_cuadrados: float):
        self._nombre = nombre
        self._metros_cuadrados = metros_cuadrados
        self._objetos: List[ObjetoHogar] = []
    
    def agregar_objeto(self, objeto: ObjetoHogar):
        """Agrega un objeto a la habitación"""
        self._objetos.append(objeto)
    
    @property
    def objetos(self) -> List[ObjetoHogar]:
        return self._objetos.copy()
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    def obtener_valor_total(self) -> float:
        """Calcula el valor total de todos los objetos en la habitación"""
        return sum(obj.calcular_valor_actual() for obj in self._objetos)
    
    def obtener_inventario(self) -> List[Dict[str, Any]]:
        """Retorna inventario detallado de la habitación"""
        return [obj.obtener_informacion() for obj in self._objetos]

class Casa:
    """Representa la casa completa con todas sus habitaciones"""
    
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion
        self._habitaciones: List[Habitacion] = []
    
    def agregar_habitacion(self, habitacion: Habitacion):
        """Agrega una habitación a la casa"""
        self._habitaciones.append(habitacion)
    
    def obtener_inventario_completo(self) -> Dict[str, Any]:
        """Genera inventario completo de la casa"""
        inventario = {
            "casa": {
                "nombre": self._nombre,
                "direccion": self._direccion,
                "total_habitaciones": len(self._habitaciones),
                "fecha_inventario": datetime.now().isoformat()
            },
            "habitaciones": {}
        }
        
        for habitacion in self._habitaciones:
            inventario["habitaciones"][habitacion.nombre] = {
                "metros_cuadrados": habitacion._metros_cuadrados,
                "valor_total": habitacion.obtener_valor_total(),
                "total_objetos": len(habitacion.objetos),
                "objetos": habitacion.obtener_inventario()
            }
        
        return inventario
    
    def generar_reporte_financiero(self) -> Dict[str, Any]:
        """Genera un reporte financiero del inventario"""
        total_valor_original = 0
        total_valor_actual = 0
        categorias_valor = {}
        
        for habitacion in self._habitaciones:
            for obj in habitacion.objetos:
                total_valor_original += obj.valor_estimado
                total_valor_actual += obj.calcular_valor_actual()
                
                categoria = obj.categoria.value
                if categoria not in categorias_valor:
                    categorias_valor[categoria] = {"original": 0, "actual": 0}
                
                categorias_valor[categoria]["original"] += obj.valor_estimado
                categorias_valor[categoria]["actual"] += obj.calcular_valor_actual()
        
        return {
            "resumen_financiero": {
                "valor_total_original": round(total_valor_original, 2),
                "valor_total_actual": round(total_valor_actual, 2),
                "depreciacion_total": round(total_valor_original - total_valor_actual, 2),
                "porcentaje_depreciacion": round(
                    ((total_valor_original - total_valor_actual) / total_valor_original * 100) 
                    if total_valor_original > 0 else 0, 2
                )
            },
            "valor_por_categoria": categorias_valor
        }

class GestorArchivos:
    """Maneja la lectura y escritura de archivos"""
    
    @staticmethod
    def guardar_inventario_json(inventario: Dict[str, Any], archivo: str):
        """Guarda el inventario en formato JSON"""
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(inventario, f, indent=2, ensure_ascii=False)
            print(f"✓ Inventario guardado en {archivo}")
        except Exception as e:
            print(f"✗ Error guardando archivo: {e}")
    
    @staticmethod
    def cargar_inventario_json(archivo: str) -> Dict[str, Any]:
        """Carga inventario desde archivo JSON"""
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"✗ Archivo {archivo} no encontrado")
            return {}
        except Exception as e:
            print(f"✗ Error cargando archivo: {e}")
            return {}

def crear_inventario_predefinido() -> Casa:
    """
    Crea el inventario fijo de la casa con todos los objetos predefinidos
    """
    casa = Casa("Casa Familiar Ejemplo", "Calle Principal 123, Ciudad Ejemplo")
    
    # COCINA
    cocina = Habitacion("Cocina", 15.0)
    cocina.agregar_objeto(Electrodomestico(
        "Refrigerador", "Cocina", "Samsung", 350, 
        EstadoConservacion.BUENO, 25000, 24
    ))
    cocina.agregar_objeto(Electrodomestico(
        "Horno Microondas", "Cocina", "LG", 1200,
        EstadoConservacion.EXCELENTE, 8000, 18
    ))
    cocina.agregar_objeto(UtensilioCocina(
        "Juego de Cubiertos", "Cocina", "Acero Inoxidable",
        EstadoConservacion.BUENO, 1500, False
    ))
    cocina.agregar_objeto(UtensilioCocina(
        "Sartén Antiadherente", "Cocina", "Tefal",
        EstadoConservacion.REGULAR, 800, False
    ))
    cocina.agregar_objeto(Mueble(
        "Mesa de Cocina", "Cocina", "Madera", "1.2m x 0.8m",
        EstadoConservacion.BUENO, 4500, "Rústico"
    ))
    casa.agregar_habitacion(cocina)
    
    # SALA
    sala = Habitacion("Sala", 25.0)
    sala.agregar_objeto(Mueble(
        "Sofá 3 Plazas", "Sala", "Cuero Sintético", "2.1m x 0.9m",
        EstadoConservacion.BUENO, 12000, "Moderno"
    ))
    sala.agregar_objeto(Mueble(
        "Mesa de Centro", "Sala", "Cristal y Metal", "1.0m x 0.6m",
        EstadoConservacion.EXCELENTE, 3500, "Contemporáneo"
    ))
    sala.agregar_objeto(Electrodomestico(
        "Televisor 55'", "Sala", "Sony", 180,
        EstadoConservacion.EXCELENTE, 18000, 36
    ))
    sala.agregar_objeto(Mueble(
        "Estantería", "Sala", "Madera MDF", "1.8m x 0.4m",
        EstadoConservacion.BUENO, 2800, "Moderno"
    ))
    casa.agregar_habitacion(sala)
    
    # DORMITORIO PRINCIPAL
    dormitorio = Habitacion("Dormitorio Principal", 18.0)
    dormitorio.agregar_objeto(Mueble(
        "Cama Queen Size", "Dormitorio", "Madera de Roble", "2.0m x 1.6m",
        EstadoConservacion.BUENO, 15000, "Clásico"
    ))
    dormitorio.agregar_objeto(Mueble(
        "Armario Empotrado", "Dormitorio", "Madera", "2.2m x 1.8m",
        EstadoConservacion.BUENO, 8500, "Moderno"
    ))
    dormitorio.agregar_objeto(Ropa(
        "Traje Formal", "Dormitorio", "Lana", "M",
        EstadoConservacion.EXCELENTE, 3000, "Invierno"
    ))
    dormitorio.agregar_objeto(Ropa(
        "Vestido de Noche", "Dormitorio", "Seda", "S",
        EstadoConservacion.BUENO, 2500, "Verano"
    ))
    dormitorio.agregar_objeto(Electrodomestico(
        "Lámpara de Noche", "Dormitorio", "Philips", 15,
        EstadoConservacion.REGULAR, 600, 6
    ))
    casa.agregar_habitacion(dormitorio)
    
    # GARAJE
    garaje = Habitacion("Garaje", 30.0)
    garaje.agregar_objeto(Herramienta(
        "Taladro Percutor", "Garaje", "Metal/Plástico",
        EstadoConservacion.BUENO, 1800, True
    ))
    garaje.agregar_objeto(Herramienta(
        "Juego de Llaves", "Garaje", "Acero Cromado",
        EstadoConservacion.EXCELENTE, 1200, False
    ))
    garaje.agregar_objeto(Herramienta(
        "Escalera Extensible", "Garaje", "Aluminio",
        EstadoConservacion.REGULAR, 3200, False
    ))
    garaje.agregar_objeto(ArticuloLimpieza(
        "Aspiradora", "Garaje", "Pisos/Muebles",
        EstadoConservacion.BUENO, 4500, False
    ))
    garaje.agregar_objeto(ArticuloLimpieza(
        "Juego de Trapos", "Garaje", "Superficies",
        EstadoConservacion.MALO, 300, True
    ))
    casa.agregar_habitacion(garaje)
    
    # BAÑO
    bano = Habitacion("Baño Principal", 8.0)
    bano.agregar_objeto(Mueble(
        "Vanitorio", "Baño", "Mármol Sintético", "1.0m x 0.5m",
        EstadoConservacion.BUENO, 5200, "Moderno"
    ))
    bano.agregar_objeto(ArticuloLimpieza(
        "Juego de Toallas", "Baño", "Textiles",
        EstadoConservacion.BUENO, 800, False
    ))
    bano.agregar_objeto(UtensilioCocina(
        "Espejo Aumento", "Baño", "Vidrio",
        EstadoConservacion.EXCELENTE, 450, False
    ))
    casa.agregar_habitacion(bano)
    
    return casa

def mostrar_inventario_consola(casa: Casa):
    """Muestra el inventario completo en la consola"""
    print("=" * 80)
    print("SISTEMA DE GESTIÓN DE INVENTARIO DE HOGAR")
    print("=" * 80)
    print(f"Casa: {casa._nombre}")
    print(f"Dirección: {casa._direccion}")
    print(f"Total habitaciones: {len(casa._habitaciones)}")
    print("=" * 80)
    
    inventario = casa.obtener_inventario_completo()
    reporte_financiero = casa.generar_reporte_financiero()
    
    for habitacion_nombre, datos_habitacion in inventario["habitaciones"].items():
        print(f"\n🏠 HABITACIÓN: {habitacion_nombre.upper()}")
        print(f"  Metros cuadrados: {datos_habitacion['metros_cuadrados']}m²")
        print(f"  Total objetos: {datos_habitacion['total_objetos']}")
        print(f"  Valor total: ${datos_habitacion['valor_total']:,.2f}")
        print("  " + "-" * 50)
        
        for obj in datos_habitacion["objetos"]:
            print(f"  • {obj['nombre']} ({obj['tipo']})")
            print(f"    Estado: {obj['estado']} | Valor actual: ${obj['valor_actual']:,.2f}")
    
    # Mostrar reporte financiero
    print("\n" + "=" * 80)
    print("📊 REPORTE FINANCIERO DEL INVENTARIO")
    print("=" * 80)
    resumen = reporte_financiero["resumen_financiero"]
    print(f"Valor total original: ${resumen['valor_total_original']:,.2f}")
    print(f"Valor total actual: ${resumen['valor_total_actual']:,.2f}")
    print(f"Depreciación total: ${resumen['depreciacion_total']:,.2f}")
    print(f"Porcentaje de depreciación: {resumen['porcentaje_depreciacion']}%")
    
    print("\nVALOR POR CATEGORÍA:")
    for categoria, valores in reporte_financiero["valor_por_categoria"].items():
        print(f"  {categoria}:")
        print(f"    Original: ${valores['original']:,.2f}")
        print(f"    Actual: ${valores['actual']:,.2f}")

def main():
    """Función principal del programa"""
    try:
        # Crear inventario predefinido
        casa = crear_inventario_predefinido()
        
        # Mostrar en consola
        mostrar_inventario_consola(casa)
        
        # Guardar en archivo JSON
        inventario_completo = casa.obtener_inventario_completo()
        reporte_financiero = casa.generar_reporte_financiero()
        
        # Combinar ambos reportes
        reporte_completo = {
            "inventario": inventario_completo,
            "analisis_financiero": reporte_financiero
        }
        
        # Asegurar que existe el directorio data
        os.makedirs('data', exist_ok=True)
        
        # Guardar archivos
        GestorArchivos.guardar_inventario_json(
            reporte_completo, 'data/inventario_completo.json'
        )
        
        print(f"\n✅ Inventario procesado exitosamente!")
        print(f"📁 Archivo guardado: data/inventario_completo.json")
        
    except Exception as e:
        print(f"❌ Error en el sistema: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()