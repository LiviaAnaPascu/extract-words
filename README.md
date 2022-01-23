# extract-words
A script that extracts words from your conversations and returns a csv with a count

To activate:
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

Structure:
.\n
├── formatWhatsAppTexts.py \n
├── conversationsdir/ \n
│   ├── chat.txt \n
│   └── anotherchat.txt \n
├── README.md \n
├── .gitignore \n
└── requirements.txt \n

python hello.py <converations-dir> <your-username> <outpt-csv-name>
