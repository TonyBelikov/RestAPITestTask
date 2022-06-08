import os
"""
File contains required paths
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_DEPLOY = os.path.join(*[BASE_DIR, 'config', 'config.json'])
