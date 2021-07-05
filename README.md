# extract-words
A script that extracts words from your conversations and returns a csv with a count

To activate:
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

Structure:
.
├── formatWhatsAppTexts.py
├── conversationsdir/
│   ├── chat.txt
│   └── anotherchat.txt
├── README.md
├── .gitignore
└── requirements.txt

python hello.py <converations-dir> <your-username> <outpt-csv-name>
