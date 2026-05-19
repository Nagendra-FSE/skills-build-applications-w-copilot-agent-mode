# OctoFit Tracker Backend

This backend is a Django project built for the OctoFit Tracker app.

## Setup

```bash
python3 -m venv /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv
source /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
pip install -r /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/requirements.txt
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py migrate
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py createsuperuser
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

## Structure

- `octofit_tracker/`: Django project settings and URL configuration
- `tracker/`: app containing user profiles, activity tracking, teams, leaderboards, and workout suggestions
