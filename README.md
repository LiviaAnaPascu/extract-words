# extract-words
A script that extracts words from your conversations and returns a csv with a count

To activate:
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

Structure:
.<br />
├── formatWhatsAppTexts.py <br />
├── conversationsdir/ <br />
│   ├── chat.txt <br />
│   └── anotherchat.txt <br />
├── README.md <br />
├── .gitignore <br />
└── requirements.txt <br />

python hello.py <converations-dir> <your-username> <outpt-csv-name>
