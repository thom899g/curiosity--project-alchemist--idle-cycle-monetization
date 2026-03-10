"""
Unified Compute Task Model - Bridges execution models across decentralized networks
"""
import json
import pickle
import hashlib
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta


class TaskType(Enum):
    INFERENCE = "inference"
    TRAINING = "training"
    SIMULATION = "simulation"
    RENDERING = "rendering"
    PROVING = "proving"
    VERIFICATION = "verification"


class ProofScheme(Enum):
    GENSYN = "gensyn"