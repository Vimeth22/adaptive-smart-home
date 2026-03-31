# Adaptive Smart Environment Controller

A Python-based **Autonomous Energy Management System (AEMS)** that controls AC compressor power using **Mamdani Fuzzy Logic**.

Instead of a simple ON/OFF thermostat, this project computes a smooth output from **0% to 100%** based on:
- Ambient temperature
- Relative humidity
- Active occupancy

## What This Project Includes

- `fuzzy_logic_engine.py`: Core fuzzy inference engine (`FuzzyACEngine`)
- `app.py`: Streamlit dashboard with real-time controls and XAI charts
- `simulator.py`: CLI benchmark runner and visualization helper
- `requirements.txt`: Python dependencies

## Quick Start

### 1) Clone and enter the repository

```bash
git clone https://github.com/Vimeth22/adaptive-smart-home.git
cd adaptive-smart-home
```

### 2) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r FuzzySmartHome/requirements.txt
```

## How to Run

Run all commands from the repository root (`adaptive-smart-home/`).

### Option A: Streamlit Dashboard (Recommended)

```bash
python FuzzySmartHome/app.py
```

or

```bash
streamlit run FuzzySmartHome/app.py
```

Then open:
- `http://localhost:8501`

### Option B: CLI Simulator

```bash
python FuzzySmartHome/simulator.py
```

This runs predefined benchmark scenarios and (on local desktop environments) shows Matplotlib visualizations.

## Methodology (Mamdani FIS)

1. **Fuzzification**: Convert crisp inputs into membership degrees.
2. **Rule Evaluation**: Apply fuzzy IF-THEN rules.
3. **Aggregation**: Combine all active rule outputs.
4. **Defuzzification (Centroid)**: Produce a crisp AC power command.

## Example Scenario

Input:
- Temperature: `35°C`
- Humidity: `85%`
- Occupancy: `9`

Expected behavior:
- High/maximum cooling command due to hot, humid, high-load conditions.

## Troubleshooting

- **Blank plots in Streamlit**: ensure the latest `app.py` is pulled and run from the repo root.
- **No GUI plot window in simulator**: this can happen in headless environments; run on a local desktop session.
- **Missing modules**: reinstall with:

```bash
pip install -r FuzzySmartHome/requirements.txt
```

## Project Structure

```text
adaptive-smart-home/
├── FuzzySmartHome/
│   ├── app.py
│   ├── fuzzy_logic_engine.py
│   ├── simulator.py
│   ├── requirements.txt
│   └── README.md
├── .devcontainer/
└── .gitignore
```

## License

MIT License.

