# Cargill Family Communication Analysis Framework

This repository documents the project framework, dataset design, analysis prompts, scoring model, and governance rules for a multi-platform AI review of family communication patterns.

It is designed to support a consistent analysis across:
- OpenAI ChatGPT
- X Grok
- Google Gemini

The central principle is **Family First** with a structured **Family Table Priority Model** focused on child stability, role clarity, and communication boundaries.

## Included files
- `index.md` — GitHub Pages home page
- `README.md` — repository overview
- `_config.yml` — GitHub Pages configuration
- `assets/style.css` — optional GitHub Pages custom styling
- `templates/packet_common.json` — normalized AI input packet template
- `templates/standard_prompt.txt` — standard analysis prompt
- `templates/scoring_instructions.txt` — shared scoring criteria
- `templates/output_template.md` — standard output format
- `templates/messages_master.csv` — normalized message dataset template
- `templates/conversations_master.csv` — normalized conversation template
- `templates/participants_master.csv` — participant template
- `templates/incidents_master.csv` — incident template

## Project goals
1. Normalize communications from multiple threads into one structured dataset
2. Run the same framework across three AI platforms
3. Compare findings without biasing one platform over another
4. Keep the analysis centered on the best interest of the children
5. Clarify communication roles, boundaries, and influence patterns

## Suggested repo structure
```text
/
├── index.md
├── README.md
├── _config.yml
├── assets/
│   └── style.css
└── templates/
    ├── packet_common.json
    ├── standard_prompt.txt
    ├── scoring_instructions.txt
    ├── output_template.md
    ├── participants_master.csv
    ├── conversations_master.csv
    ├── messages_master.csv
    └── incidents_master.csv
```

## Publishing to GitHub Pages
1. Create a new GitHub repository
2. Upload these files to the repo root
3. In GitHub, go to **Settings > Pages**
4. Under **Build and deployment**, choose **Deploy from a branch**
5. Select the main branch and the root folder
6. Save

GitHub will publish the site using `index.md`.
