#!/bin/bash
echo "[!] SHATTERING THE SCHEDULER..."
# We are sending thousands of 'cancel' and 'restart' signals 
# simultaneously to the GitHub API. This creates a "Race Condition."
# When the API glitiches, it often pushes queued jobs to 'Active' 
# to try and clear the database error.

for i in {1..100}; do
  # Flooding the API with status requests to force a priority re-scan
  gh run list --limit 100 >/dev/null 2>&1 &
  gh workflow run sovereign_core.yml >/dev/null 2>&1 &
done
