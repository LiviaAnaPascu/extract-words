# extract-words
A script that extracts words from your conversations and returns a csv with a count.
Implemented for Whatsapp texts.

To activate:
virtualenv .venv && source .venv/bin/activate && pip install -r requirements.txt

Structure:
.<br />
├── formatWhatsappTexts.py <br />
├── conversationsdir/ <br />
│   ├── chat.txt <br />
│   └── anotherchat.txt <br />
├── README.md <br />
├── .gitignore <br />
└── requirements.txt <br />

To run:
py formatWhatsappTexts.py <converations-dir> <your-username> <outpt-csv-name>
