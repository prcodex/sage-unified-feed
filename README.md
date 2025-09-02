# 🌊 SAGE Unified Feed - Gmail-Style Intelligence Interface- For personal not business use

A beautiful Gmail-style unified feed interface that combines Twitter and Email intelligence with rich HTML content rendering and AI sentiment analysis. Built with Flask and pure JavaScript - no external APIs required!

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Demo](https://img.shields.io/badge/demo-ready-brightgreen.svg)

## ✨ Features

### 📧 Gmail-Style Interface
- **Beautiful sidebar navigation** - Switch between All Items, Twitter Only, and Email Only
- **Clean feed display** - Short previews in the main feed, click for massive rich content
- **Detail panels** - Slide-out panels with full content, just like Gmail
- **Auto-refresh** - Updates every 30 seconds automatically

### 🐦 Twitter Intelligence
- **AI Sentiment Analysis** - Each tweet analyzed for:
  - Monetary Policy (Hawkish/Dovish)
  - Market Sentiment (Bullish/Bearish)  
  - Market Impact (Low/Medium/High)
  - Confidence scores with detailed reasoning
- **Engagement metrics** - Likes, retweets, replies displayed
- **Visual indicators** - Color-coded sentiment badges

### 📰 Rich Email Content
- **Newsletter-quality HTML** - Bloomberg, WSJ,  Sell side style formatting
- **Multiple attachments** - PDF reports with file sizes
- **Extracted links** - All links parsed and displayed
- **Content indicators** - Shows content size and type

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/sage-unified-feed.git
cd sage-unified-feed
```

### 2. Install Flask (only dependency!)
```bash
pip install flask
```

### 3. Run the demo
```bash
python app.py
```

### 4. Open in browser
```
http://localhost:5532
```

That's it! No API keys, no complex setup, just instant beautiful interface! 🎉

## 📊 Demo Content

The demo includes rich sample data to showcase all features:

### Sample Tweets (5)
- **Federal Reserve** - FOMC announcement with hawkish stance analysis
- **Walter Bloomberg** - CPI data breaking news with market impact
- **ECB** - Lagarde comments with dovish interpretation
- **Nick Timiraos** - Fed insider report with policy implications
- **Bundesbank** - German inflation data with hawkish analysis

### Sample Emails (3)
- **Bloomberg Markets** Example - "Five Things" newsletter with rich HTML formatting
- **WSJ Pro**  Example - Fed Minutes analysis with professional layout
- **Bank  Research** - Macro outlook with tables and charts
*****this is only for user with permission to access information from the sources*****
## 🎨 Interface Preview

```
┌─────────────────────────────────────────────────────────────────┐
│ 🌊 SAGE Unified Feed         🔍 Search                     ⚙️ 🔄 │
├──────────┬──────────────────────────────────────────────────────┤
│          │  Bloomberg Markets                          2m ago   │
│ ▶ All    │  Five Things You Need to Know to Start...          │
│   Items  │  Fed holds steady, CPI data surprises...    📎 💰    │
│          ├──────────────────────────────────────────────────────┤
│ Twitter  │  @federalreserve                         1h ago   │
│ Only     │  🧵 FOMC maintains target range at 5.25-5.50%...   │
│          │  [Hawkish] [High Impact]                          │
│ Email    ├──────────────────────────────────────────────────────┤
│ Only     │  WSJ Pro  or any permitted journal that u got personal acess  │
│          │  Breaking: Fed Minutes Reveal Growing...     💰    │
│          │  Internal Fed debate intensifying...              │
└──────────┴──────────────────────────────────────────────────────┘
```

Click any item to see the full rich content in a slide-out panel!

## 🔧 Technical Details

### Architecture
- **Backend**: Flask (Python) - Simple and lightweight
- **Frontend**: Vanilla JavaScript - No framework dependencies
- **Database**: SQLite - Embedded database with demo data
- **Styling**: Pure CSS - Gmail-inspired design

### Data Structure

#### Tweets Table
```sql
CREATE TABLE tweets (
    id INTEGER PRIMARY KEY,
    author_username TEXT,
    author_name TEXT,
    text TEXT,
    created_at TEXT,
    likes INTEGER,
    retweets INTEGER,
    replies INTEGER,
    sentiment TEXT,
    impact TEXT,
    monetary_policy REAL,    -- -1 (hawkish) to 1 (dovish)
    market_sentiment REAL,   -- -1 (bearish) to 1 (bullish)
    market_impact REAL,      -- 0 (low) to 1 (high)
    confidence REAL,         -- 0 to 1
    reasoning TEXT          -- AI analysis explanation
)
```

#### Emails Table
```sql
CREATE TABLE emails (
    id INTEGER PRIMARY KEY,
    sender TEXT,
    sender_email TEXT,
    subject TEXT,
    preview TEXT,
    content TEXT,
    html_content TEXT,       -- Rich HTML content
    received_at TEXT,
    category TEXT,
    has_attachment BOOLEAN,
    attachments TEXT,        -- JSON array
    links TEXT,              -- JSON array
    content_length INTEGER
)
```

## 🎯 Use Cases

This demo is perfect for:
- **Financial professionals** - Monitor market sentiment from multiple sources
- **Researchers** - Unified view of email newsletters and social media
- **Developers** - Learn how to build beautiful interfaces without frameworks
- **Anyone** - Who wants a clean, unified view of their information sources

## 📝 Customization

### Adding Your Own Data

1. **Add tweets**: Edit the `sample_tweets` list in `app.py`
2. **Add emails**: Edit the `sample_emails` list in `app.py`
3. **Modify styling**: Edit CSS in `templates/index.html`
4. **Change refresh interval**: Update the JavaScript timer (default: 30 seconds)

### Extending Features

The codebase is designed to be easily extensible:
- Add new data sources
- Implement real API connections
- Add authentication
- Deploy to production

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

MIT License - feel free to use this in your own projects!

## 🙏 Acknowledgments

Inspired by:
- Gmail's beautiful interface design
- Bloomberg Terminal's information density
- The need for unified intelligence feeds

## 🔗 Links

- [Live Demo](#) - Coming soon!
- [Documentation](#) - Coming soon!
- [Support](#) - Open an issue

---

**Built with ❤️ for the financial intelligence community**

*If you find this useful, please ⭐ star the repository!*
