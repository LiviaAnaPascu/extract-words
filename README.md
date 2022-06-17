# extract-words
A script that extracts words from your conversations and returns a csv with a count.
Implemented for Whatsapp texts.

<h1>To export chat</h1>
<a href="https://faq.whatsapp.com/android/chats/how-to-save-your-chat-history/?lang=en">https://faq.whatsapp.com/android/chats/how-to-save-your-chat-history/?lang=en</a>

<h1>Format</h1>
Chat should have default format <em>[DD/MM/YYYY, HH.SS.MM] Username: Message<em>

<h1>Structure</h1>
.<br />
├── ▼ python <br />
├──── formatWhatsappTexts.py <br />
├── ▼ requirements <br />
├──── requirements.txt <br />
├── ▼ unittest <br />
├──── ▼ conversations <br />
├────── chat.txt <br />
├────── chat2.txt <br />
├──── unittests.py <br />
├── .gitignore <br />
└── README.md <br />

<h1>To run</h1>
formatWhatsappTexts.exe converations-dir outpt-csv-name your-username
