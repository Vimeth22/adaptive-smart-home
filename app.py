import os
import sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    port = os.environ.get("PORT", "8501")
    sys.argv = [
        "streamlit",
        "run",
        "FuzzySmartHome/app.py",
        "--server.port",
        str(port),
        "--server.address",
        "0.0.0.0",
    ]
    sys.exit(stcli.main())
