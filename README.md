# Cartpole-Deep-RL

Dieses Repository demonstriert Deep Q-Learning (DQN) am Beispiel der CartPole-v1-Umgebung mit Stable Baselines3.

## Projektübersicht

Enthaltene Dateien:

- `cartpole.py`  
  Startet das Training eines DQN-Agenten auf CartPole. Speichert das Modell in `dqn_cartpole_model.zip`.

- `cartpole_gui.py`  
  Startet das Spiel mit visueller Darstellung. Zeigt die Aktionen des Agenten in Echtzeit.

- `cartpole_gui_use_model.py`  
  Lädt ein bestehendes Modell (`dqn_cartpole_model.zip`) und spielt CartPole automatisch.

- `dqn_cartpole_model.zip`  
  Gespeichertes Modell, erzeugt mit Stable Baselines3.

- `requirements.txt`  
  Enthält alle Python-Abhängigkeiten zur Installation.

## Installation

1. **Python-Version**: Getestet mit Python 3.12

2. **Virtuelle Umgebung erstellen (empfohlen)**

   **Linux/macOS**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

### Modell trainieren
```bash
python cartpole.py
```

### Modell mit GUI testen
```bash
python cartpole_gui_use_model.py
```

### Optionale Visualisierung (mit `cartpole_gui.py`)
```bash
python cartpole_gui.py
```

## Anforderungen (requirements.txt)

```txt
gymnasium==0.29.1
stable-baselines3==2.2.1
torch>=2.0.0
numpy>=1.24.0
```

Installierbar mit:
```bash
pip install -r requirements.txt
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Frei verwendbar für nicht-kommerzielle Zwecke, Lehre und Forschung.
