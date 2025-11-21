"""
Módulo para las categorías de objetos del hogar.
Define la clase base abstracta y las categorías específicas.
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Any
import json
from datetime import datetime

class Categoria(Enum):
    """Enumeración de categorías disponibles"""
    COCINA = "Cocina"
    HERRAMIENTAS = "Herramientas"
    ELECTRONICOS = "Electrónicos"
    ROPA = "Ropa"
    MUEBLES = "Muebles"
    LIMPIEZA = "Limpieza"

class EstadoConservacion(Enum):
    """Estados de conservación de los objetos"""
    EXCELENTE = "Excelente"
    BUENO = "Bueno"
    REGULAR = "Regular"
    MALO = "Malo"

class ObjetoHogar(ABC):
    """Clase abstracta base para todos los objetos del hogar"""
    
    def __init__(self, nombre: str, categoria: Categoria, ubicacion: str, 
                 estado: EstadoConservacion = EstadoConservacion.BUENO, 
                 valor_estimado: float = 0.0):
        self._nombre = nombre
        self._categoria = categoria
        self._ubicacion = ubicacion
        self._estado = estado
        self._valor_estimado = valor_estimado
        self._fecha_adquisicion = datetime.now()
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def categoria(self) -> Categoria:
        return self._categoria
    
    @property
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @property
    def estado(self) -> EstadoConservacion:
        return self._estado
    
    @property
    def valor_estimado(self) -> float:
        return self._valor_estimado
    
    @abstractmethod
    def calcular_valor_actual(self) -> float:
        """Calcula el valor actual considerando depreciación"""
        pass
    
    @abstractmethod
    def obtener_informacion(self) -> Dict[str, Any]:
        """Retorna información detallada del objeto"""
        pass
    
    def __str__(self) -> str:
        return f"{self._nombre} ({self._categoria.value}) - {self._ubicacion}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._nombre}', {self._categoria}, '{self._ubicacion}')"