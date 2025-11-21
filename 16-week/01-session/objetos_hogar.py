"""
Módulo con las implementaciones específicas de objetos del hogar.
"""
from .categorias import ObjetoHogar, Categoria, EstadoConservacion
from typing import Dict, Any, List
from datetime import datetime, timedelta

class Electrodomestico(ObjetoHogar):
    """Representa electrodomésticos del hogar"""
    
    def __init__(self, nombre: str, ubicacion: str, marca: str, 
                 potencia_w: float, estado: EstadoConservacion = EstadoConservacion.BUENO,
                 valor_estimado: float = 0.0, garantia_meses: int = 12):
        super().__init__(nombre, Categoria.ELECTRONICOS, ubicacion, estado, valor_estimado)
        self._marca = marca
        self._potencia_w = potencia_w
        self._garantia_meses = garantia_meses
    
    def calcular_valor_actual(self) -> float:
        """Calcula valor con depreciación del 15% anual"""
        años_uso = 2  # Simulado
        depreciacion = 0.15 * años_uso
        return max(0, self._valor_estimado * (1 - depreciacion))
    
    def obtener_informacion(self) -> Dict[str, Any]:
        return {
            "tipo": "Electrodoméstico",
            "nombre": self._nombre,
            "marca": self._marca,
            "categoria": self._categoria.value,
            "ubicacion": self._ubicacion,
            "estado": self._estado.value,
            "potencia_w": self._potencia_w,
            "valor_original": self._valor_estimado,
            "valor_actual": self.calcular_valor_actual(),
            "garantia_meses": self._garantia_meses
        }

class Herramienta(ObjetoHogar):
    """Representa herramientas del hogar"""
    
    def __init__(self, nombre: str, ubicacion: str, material: str,
                 estado: EstadoConservacion = EstadoConservacion.BUENO,
                 valor_estimado: float = 0.0, es_electrica: bool = False):
        super().__init__(nombre, Categoria.HERRAMIENTAS, ubicacion, estado, valor_estimado)
        self._material = material
        self._es_electrica = es_electrica
    
    def calcular_valor_actual(self) -> float:
        """Herramientas se deprecian menos - 8% anual"""
        años_uso = 3  # Simulado
        depreciacion = 0.08 * años_uso
        return max(0, self._valor_estimado * (1 - depreciacion))
    
    def obtener_informacion(self) -> Dict[str, Any]:
        return {
            "tipo": "Herramienta",
            "nombre": self._nombre,
            "material": self._material,
            "categoria": self._categoria.value,
            "ubicacion": self._ubicacion,
            "estado": self._estado.value,
            "electrica": self._es_electrica,
            "valor_original": self._valor_estimado,
            "valor_actual": self.calcular_valor_actual()
        }

class Ropa(ObjetoHogar):
    """Representa prendas de vestir"""
    
    def __init__(self, nombre: str, ubicacion: str, tela: str, talla: str,
                 estado: EstadoConservacion = EstadoConservacion.BUENO,
                 valor_estimado: float = 0.0, temporada: str = "Todo el año"):
        super().__init__(nombre, Categoria.ROPA, ubicacion, estado, valor_estimado)
        self._tela = tela
        self._talla = talla
        self._temporada = temporada
    
    def calcular_valor_actual(self) -> float:
        """La ropa se deprecia rápido - 30% anual"""
        años_uso = 1  # Simulado
        depreciacion = 0.3 * años_uso
        return max(0, self._valor_estimado * (1 - depreciacion))
    
    def obtener_informacion(self) -> Dict[str, Any]:
        return {
            "tipo": "Ropa",
            "nombre": self._nombre,
            "tela": self._tela,
            "talla": self._talla,
            "categoria": self._categoria.value,
            "ubicacion": self._ubicacion,
            "estado": self._estado.value,
            "temporada": self._temporada,
            "valor_original": self._valor_estimado,
            "valor_actual": self.calcular_valor_actual()
        }

class Mueble(ObjetoHogar):
    """Representa muebles del hogar"""
    
    def __init__(self, nombre: str, ubicacion: str, material: str, 
                 dimensiones: str, estado: EstadoConservacion = EstadoConservacion.BUENO,
                 valor_estimado: float = 0.0, estilo: str = "Moderno"):
        super().__init__(nombre, Categoria.MUEBLES, ubicacion, estado, valor_estimado)
        self._material = material
        self._dimensiones = dimensiones
        self._estilo = estilo
    
    def calcular_valor_actual(self) -> float:
        """Muebles de buena calidad pueden mantener valor"""
        años_uso = 4  # Simulado
        if self._material.lower() in ["madera solida", "roble", "caoba"]:
            depreciacion = 0.05 * años_uso  # Sólo 5% anual
        else:
            depreciacion = 0.1 * años_uso  # 10% anual
        return max(0, self._valor_estimado * (1 - depreciacion))
    
    def obtener_informacion(self) -> Dict[str, Any]:
        return {
            "tipo": "Mueble",
            "nombre": self._nombre,
            "material": self._material,
            "dimensiones": self._dimensiones,
            "categoria": self._categoria.value,
            "ubicacion": self._ubicacion,
            "estado": self._estado.value,
            "estilo": self._estilo,
            "valor_original": self._valor_estimado,
            "valor_actual": self.calcular_valor_actual()
        }

class UtensilioCocina(ObjetoHogar):
    """Representa utensilios de cocina"""
    
    def __init__(self, nombre: str, ubicacion: str, material: str,
                 estado: EstadoConservacion = EstadoConservacion.BUENO,
                 valor_estimado: float = 0.0, es_afilable: bool = False):
        super().__init__(nombre, Categoria.COCINA, ubicacion, estado, valor_estimado)
        self._material = material
        self._es_afilable = es_afilable
    
    def calcular_valor_actual(self) -> float:
        """Utensilios se deprecian moderadamente"""
        años_uso = 2  # Simulado
        depreciacion = 0.12 * años_uso
        return max(0, self._valor_estimado * (1 - depreciacion))
    
    def obtener_informacion(self) -> Dict[str, Any]:
        return {
            "tipo": "Utensilio Cocina",
            "nombre": self._nombre,
            "material": self._material,
            "categoria": self._categoria.value,
            "ubicacion": self._ubicacion,
            "estado": self._estado.value,
            "afilable": self._es_afilable,
            "valor_original": self._valor_estimado,
            "valor_actual": self.calcular_valor_actual()
        }

class ArticuloLimpieza(ObjetoHogar):
    """Representa artículos de limpieza"""
    
    def __init__(self, nombre: str, ubicacion: str, tipo_limpieza: str,
                 estado: EstadoConservacion = EstadoConservacion.BUENO,
                 valor_estimado: float = 0.0, es_desechable: bool = False):
        super().__init__(nombre, Categoria.LIMPIEZA, ubicacion, estado, valor_estimado)
        self._tipo_limpieza = tipo_limpieza
        self._es_desechable = es_desechable
    
    def calcular_valor_actual(self) -> float:
        """Artículos de limpieza pierden valor rápido"""
        años_uso = 1  # Simulado
        depreciacion = 0.4 * años_uso
        return max(0, self._valor_estimado * (1 - depreciacion))
    
    def obtener_informacion(self) -> Dict[str, Any]:
        return {
            "tipo": "Artículo Limpieza",
            "nombre": self._nombre,
            "tipo_limpieza": self._tipo_limpieza,
            "categoria": self._categoria.value,
            "ubicacion": self._ubicacion,
            "estado": self._estado.value,
            "desechable": self._es_desechable,
            "valor_original": self._valor_estimado,
            "valor_actual": self.calcular_valor_actual()
        }