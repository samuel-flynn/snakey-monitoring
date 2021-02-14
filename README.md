# snakey-monitoring
A process for monitoring the logs of Satisfactory, the status of SyncLounge, and other systems used by the tunnel snakes.

## Quick Start

## Development Setup
### Install build tools

`python -m venv .venv`

`./.venv/Scripts/activate`

`python -m pip install -r dev-requirements.txt`

### Run the build

`python -m build -sw`

### Install runtime dependencies

1. Run the build at least once

2. `python -m pip install -r snakey_monitoring.egg-info/requires.txt`