"""
Emergent Davranış Testi
Bilinç teorilerini test eden otonom script
AGI-Bilinç Araştırmaları Projesi
"""

import random
import json
from datetime import datetime
from typing import List, Dict, Any


class SimpleNeuralAgent:
    """
    Basit bir sinirsel ajan - emergent davranışları gözlemlemek için
    """
    
    def __init__(self, input_size: int = 4, hidden_size: int = 8, output_size: int = 2):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Basit ağırlıklar (rastgele başlatma)
        self.weights_1 = [[random.uniform(-1, 1) for _ in range(input_size)] 
                         for _ in range(hidden_size)]
        self.weights_2 = [[random.uniform(-1, 1) for _ in range(hidden_size)] 
                         for _ in range(output_size)]
        
        # İç durum ("bellek")
        self.hidden_state = [0.0] * hidden_size
        self.experience_buffer: List[Dict[str, Any]] = []
        
    def activate(self, x: float) -> float:
        """Sigmoid aktivasyon fonksiyonu"""
        return 1 / (1 + (2.71828 ** -x))
    
    def forward(self, inputs: List[float]) -> List[float]:
        """İleri besleme (forward pass)"""
        # Gizli katman
        hidden = []
        for i in range(self.hidden_size):
            sum_val = sum(inputs[j] * self.weights_1[i][j] for j in range(self.input_size))
            hidden.append(self.activate(sum_val))
        
        self.hidden_state = hidden  # İç durum güncelle
        
        # Çıkış katmanı
        outputs = []
        for i in range(self.output_size):
            sum_val = sum(hidden[j] * self.weights_2[i][j] for j in range(self.hidden_size))
            outputs.append(self.activate(sum_val))
        
        return outputs
    
    def store_experience(self, input_data: List[float], output: List[float], 
                        context: str = ""):
        """Deneyimi belleğe kaydet"""
        experience = {
            "timestamp": datetime.now().isoformat(),
            "input": input_data,
            "output": output,
            "hidden_state": self.hidden_state.copy(),
            "context": context
        }
        self.experience_buffer.append(experience)
        
        # Bellek limiti (son 100 deneyim)
        if len(self.experience_buffer) > 100:
            self.experience_buffer.pop(0)
    
    def get_emergent_metrics(self) -> Dict[str, float]:
        """
        Emergent davranış metriklerini hesapla
        """
        if len(self.experience_buffer) < 10:
            return {"status": "Yetersiz veri"}
        
        # Gizli durum değişimi analizi
        state_changes = []
        for i in range(1, len(self.experience_buffer)):
            prev = self.experience_buffer[i-1]["hidden_state"]
            curr = self.experience_buffer[i]["hidden_state"]
            change = sum(abs(curr[j] - prev[j]) for j in range(len(curr)))
            state_changes.append(change)
        
        # Çeşitlilik metriği (ne kadar farklı tepki veriyor?)
        outputs = [exp["output"] for exp in self.experience_buffer[-20:]]
        unique_patterns = len(set(tuple(round(o[0], 2) for o in outputs)))
        
        # Entropi benzeri metrik (tahmin edilemezlik)
        avg_change = sum(state_changes) / len(state_changes) if state_changes else 0
        
        return {
            "durum_degisim_ort": round(avg_change, 4),
            "ceşitlilik_skoru": unique_patterns,
            "bellek_doluluk": len(self.experience_buffer),
            "emergent_skor": round(avg_change * unique_patterns / 10, 4)
        }


class ConsciousnessSimulator:
    """
    Basit bilinç simülasyonu - GWT benzeri küresel çalışma alanı
    """
    
    def __init__(self):
        self.global_workspace: Dict[str, Any] = {}
        self.specialists = {
            "perception": self.perception_module,
            "memory": self.memory_module,
            "decision": self.decision_module,
        }
        self.broadcast_history: List[Dict] = []
        
    def perception_module(self, data: Any) -> Dict:
        """Algı modülü - ham veriyi işler"""
        return {
            "type": "perception",
            "raw_data": data,
            "features": f"processed_{data}" if isinstance(data, str) else data
        }
    
    def memory_module(self, query: Any) -> Dict:
        """Bellek modülü - geçmiş erişimi"""
        return {
            "type": "memory",
            "retrieved": f"memory_of_{query}",
            "relevance": random.uniform(0, 1)
        }
    
    def decision_module(self, options: List[str]) -> Dict:
        """Karar modülü - seçim yapar"""
        choice = random.choice(options) if options else "no_option"
        return {
            "type": "decision",
            "selected": choice,
            "confidence": random.uniform(0.5, 1.0)
        }
    
    def broadcast(self, content: Dict[str, Any], source: str):
        """Küresel alana yayın yap"""
        broadcast_event = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "content": content
        }
        self.global_workspace.update(content)
        self.broadcast_history.append(broadcast_event)
        
    def process_cycle(self, input_data: Any) -> Dict[str, Any]:
        """
        Tam bilinç döngüsü simülasyonu
        """
        # 1. Algı modülü çalışır
        perception = self.specialists["perception"](input_data)
        self.broadcast(perception, "perception")
        
        # 2. Bellek modülü küresel alana erişir
        memory = self.specialists["memory"](input_data)
        self.broadcast(memory, "memory")
        
        # 3. Karar modülü entegre bilgiye göre çalışır
        options = ["action_a", "action_b", "action_c"]
        decision = self.specialists["decision"](options)
        self.broadcast(decision, "decision")
        
        return {
            "workspace_state": self.global_workspace.copy(),
            "decision": decision["selected"],
            "cycle_integrated": True
        }


def run_emergence_test():
    """
    Emergent davranış testini çalıştır
    """
    print("=" * 60)
    print("EMERGENT DAVRANIŞ TESTİ")
    print("AGI-Bilinç Araştırmaları")
    print("=" * 60)
    
    # Ajan oluştur
    agent = SimpleNeuralAgent()
    
    # Test verileri
    test_inputs = [
        [0.1, 0.2, 0.3, 0.4],
        [0.8, 0.7, 0.6, 0.5],
        [0.5, 0.5, 0.5, 0.5],
        [0.9, 0.1, 0.9, 0.1],
    ]
    
    print("\n1. BASİT AJAN TESTİ")
    print("-" * 40)
    
    for i, inp in enumerate(test_inputs):
        output = agent.forward(inp)
        agent.store_experience(inp, output, f"test_cycle_{i}")
        print(f"Girdi {i+1}: {[round(x, 2) for x in inp]}")
        print(f"  → Çıktı: {[round(x, 3) for x in output]}")
        print(f"  → Gizli durum: {[round(x, 2) for x in agent.hidden_state[:4]]}...")
    
    # Metrikler
    metrics = agent.get_emergent_metrics()
    print(f"\n📊 Emergent Metrikler:")
    for key, val in metrics.items():
        print(f"  {key}: {val}")
    
    # Bilinç simülasyonu
    print("\n\n2. KÜRESEL ÇALIŞMA ALANI (GWT) TESTİ")
    print("-" * 40)
    
    sim = ConsciousnessSimulator()
    
    test_scenarios = ["tehlike", "fırsat", "nötr", "belirsiz"]
    
    for scenario in test_scenarios:
        result = sim.process_cycle(scenario)
        print(f"\nSenaryo: {scenario}")
        print(f"  Karar: {result['decision']}")
        print(f"  Entegrasyon: {result['cycle_integrated']}")
    
    print("\n" + "=" * 60)
    print("Test tamamlandı!")
    print(f"Toplam yayın: {len(sim.broadcast_history)}")
    print("=" * 60)


if __name__ == "__main__":
    run_emergence_test()
