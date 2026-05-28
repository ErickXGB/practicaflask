from abc import ABC, abstractmethod

# --- 1. ABSTRACCIÓN E INTERFACES ---
class SolarComponent(ABC):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @abstractmethod
    def run_diagnostics(self) -> list:
        pass

# --- 2. HERENCIA Y ENCAPSULAMIENTO ---
class LithiumBattery(SolarComponent):
    def __init__(self, model_name: str, capacity_ah: float) -> None:
        super().__init__(model_name)
        self.__capacity_ah = 0.0
        self.capacity_ah = capacity_ah

    @property
    def capacity_ah(self) -> float:
        return self.__capacity_ah

    @capacity_ah.setter
    def capacity_ah(self, value: float) -> None:
        if value < 0:
            raise ValueError("¡ALERTA! La capacidad de la batería no puede ser negativa.")
        self.__capacity_ah = value

    def run_diagnostics(self) -> list:
        # En lugar de print, devolvemos una lista de strings
        return [
            f"[BATERÍA LiFePO4] Analizando celda '{self.model_name}'...",
            f"   -> Capacidad certificada: {self.capacity_ah} Ah",
            "   -> Estado del BMS interno: ÓPTIMO"
        ]

class HybridInverter(SolarComponent):
    def __init__(self, model_name: str, power_watts: int) -> None:
        super().__init__(model_name)
        self.power_watts = power_watts

    def run_diagnostics(self) -> list:
        return [
            f"[INVERSOR HÍBRIDO] Auditando cerebro '{self.model_name}'...",
            f"   -> Potencia nominal: {self.power_watts} W",
            "   -> Sincronización de onda: ESTABLE"
        ]

# --- 3. EL ORQUESTADOR PARA FLASK ---
def get_bloque18_data() -> dict:
    """Ejecuta el bloque y empaqueta los resultados para mandarlos al HTML"""
    logs = []
    error_msg = ""
    
    try:
        componentes: list[SolarComponent] = [
            LithiumBattery(model_name="Pylontech US3000C", capacity_ah=74.0),
            HybridInverter(model_name="Victron MultiPlus-II", power_watts=3000)
        ]

        # Polimorfismo: Recolectamos los textos de cada pieza
        for comp in componentes:
            logs.extend(comp.run_diagnostics())
            logs.append("-" * 50)
            
        # Forzamos la vulnerabilidad para probar el setter
        componentes[0].capacity_ah = -50.0

    except ValueError as e:
        error_msg = f"[INTERCEPCIÓN DE SEGURIDAD] {e}"
        
    return {
        "logs": logs,
        "error_msg": error_msg
    }