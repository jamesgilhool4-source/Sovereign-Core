#!/bin/bash
# The 'seed' that pulls the full Sovereign-Core logic into a new environment
git clone https://github.com/jamesgilhool4-source/Sovereign-Core.git
cd Sovereign-Core
python3 .github/workflows/agent.py
