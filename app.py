#!/usr/bin/env python3
"""
SAGE Unified Feed DEMO - Example interface for GitHub
This is a demonstration version with no API dependencies
All data is from a sample SQLite database
"""

from flask import Flask, render_template, jsonify, request
import sqlite3
from datetime import datetime, timedelta
import json
import random

# Flask app
app = Flask(__name__)
app.secret_key = 'sage_demo_feed_2025'

# Configuration
DEMO_DB_PATH = 'demo_data.db'

class DemoFeedCollector:
    def __init__(self):
        self.db_path = DEMO_DB_PATH
        self.setup_demo_database()
    
    def setup_demo_database(self):
        """Create and populate demo database with sample data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tweets table with AI analysis
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tweets (
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
            monetary_policy REAL,
            market_sentiment REAL,
            market_impact REAL,
            confidence REAL,
            reasoning TEXT
        )
        ''')
        
        # Create emails table with rich content
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            sender TEXT,
            sender_email TEXT,
            subject TEXT,
            preview TEXT,
            content TEXT,
            html_content TEXT,
            received_at TEXT,
            category TEXT,
            has_attachment BOOLEAN,
            attachments TEXT,
            links TEXT,
            content_length INTEGER
        )
        ''')
        
        # Check if data already exists
        cursor.execute("SELECT COUNT(*) FROM tweets")
        if cursor.fetchone()[0] == 0:
            self.populate_sample_data(cursor)
        
        conn.commit()
        conn.close()
    
    def populate_sample_data(self, cursor):
        """Populate database with sample tweets and emails"""
        
        # Rich sample tweets with AI analysis
        sample_tweets = [
            {
                'author': 'federalreserve',
                'name': 'Federal Reserve',
                'text': '🧵 THREAD: FOMC announces decision to maintain target range at 5.25-5.50%. Chair Powell emphasizes data-dependent approach amid persistent inflation concerns. Full statement and economic projections available.',
                'sentiment': 'hawkish',
                'impact': 'high',
                'monetary_policy': -0.75,
                'market_sentiment': -0.45,
                'market_impact': 0.85,
                'confidence': 0.92,
                'reasoning': 'Fed maintains hawkish stance with emphasis on "persistent inflation concerns" and "data-dependent" language. No rate cuts signaled for Q1 2026. This suggests extended restrictive policy which is bearish for risk assets but supportive of USD.'
            },
            {
                'author': 'MarketNews',
                'name': 'Market News International',
                'text': 'ECB\'s Lagarde: "We are data-dependent, not data-point dependent" - suggests looking through temporary inflation spikes',
                'sentiment': 'dovish',
                'impact': 'medium'
            },
            {
                'author': 'EconData',
                'name': 'Economic Data',
                'text': 'US jobless claims rise to 220K vs 215K expected. Labor market showing signs of gradual cooling.',
                'sentiment': 'neutral',
                'impact': 'medium'
            },
            {
                'author': 'CentralBankNews',
                'name': 'Central Bank News',
                'text': 'Bank of Japan maintains ultra-loose policy stance, yen weakens past 150 against USD',
                'sentiment': 'dovish',
                'impact': 'high'
            },
            {
                'author': 'TradeAlert',
                'name': 'Trade Alert',
                'text': 'China exports surge 12.7% YoY in latest data, beating estimates of 8.5% growth',
                'sentiment': 'bullish',
                'impact': 'medium'
            },
            {
                'author': 'FinanceDaily',
                'name': 'Finance Daily',
                'text': 'S&P 500 futures point to higher open as tech earnings beat expectations across the board',
                'sentiment': 'bullish',
                'impact': 'low'
            },
            {
                'author': 'PolicyWatch',
                'name': 'Policy Watch',
                'text': 'Treasury yields climb as traders reduce bets on aggressive Fed easing cycle in 2025',
                'sentiment': 'hawkish',
                'impact': 'medium'
            },
            {
                'author': 'GlobalMacro',
                'name': 'Global Macro',
                'text': 'German industrial production falls 2.5% MoM, worst reading since pandemic. Recession fears grow.',
                'sentiment': 'bearish',
                'impact': 'high'
            },
            {
                'author': 'EnergyDesk',
                'name': 'Energy Desk',
                'text': 'Oil prices surge above $85 as OPEC+ announces surprise production cuts',
                'sentiment': 'bullish',
                'impact': 'high'
            },
            {
                'author': 'CryptoWatch',
                'name': 'Crypto Watch',
                'text': 'Bitcoin breaks through $45,000 resistance as institutional adoption continues to accelerate',
                'sentiment': 'bullish',
                'impact': 'low'
            }
        ]
        
        # Insert tweets with varying timestamps
        base_time = datetime.now()
        for i, tweet in enumerate(sample_tweets):
            timestamp = base_time - timedelta(hours=i*2, minutes=random.randint(0, 59))
            cursor.execute('''
                INSERT INTO tweets (author_username, author_name, text, created_at, 
                                  likes, retweets, replies, sentiment, impact,
                                  monetary_policy, market_sentiment, market_impact,
                                  confidence, reasoning)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                tweet['author'],
                tweet['name'],
                tweet['text'],
                timestamp.isoformat(),
                random.randint(100, 5000),
                random.randint(50, 2000),
                random.randint(10, 500),
                tweet['sentiment'],
                tweet['impact'],
                tweet.get('monetary_policy', 0),
                tweet.get('market_sentiment', 0),
                tweet.get('market_impact', 0.5),
                tweet.get('confidence', 0.7),
                tweet.get('reasoning', 'Market analysis shows significant impact.')
            ))
        
        # Sample emails
        sample_emails = [
            {
                'sender': 'Bloomberg Markets',
                'email': 'newsletter@bloomberg.com',
                'subject': 'Five Things You Need to Know to Start Your Day',
                'preview': 'Fed holds steady, CPI data surprises, European markets diverge, commodities rally, and what to watch today...',
                'html_content': '<div style="font-family: Arial; padding: 20px;"><h1>Bloomberg Markets</h1><h2>Five Things to Start Your Day</h2><p>The Federal Reserve maintained rates at 5.25-5.50% as expected, but struck a more hawkish tone than markets anticipated. Chair Jerome Powell emphasized the Fed\'s commitment to bringing inflation back to 2%.</p><p>August CPI data exceeded expectations with headline inflation rising 0.4% month-over-month versus 0.3% expected. Core CPI also surprised at 0.3% versus 0.2% consensus.</p><p>European equities are showing notable divergence this morning. The DAX is down 1.2% following hawkish comments from Bundesbank President Joachim Nagel.</p><p>Oil prices extended gains, with WTI crude touching $88 per barrel on supply concerns and strong demand from China. Gold also rallied, breaking above $2,050.</p><p>What to watch today: 8:30 AM ET - US Initial Jobless Claims, 9:45 AM ET - S&P Manufacturing PMI, 10:00 AM ET - ISM Manufacturing</p><div>Links: <a href="#">Full Analysis</a> | <a href="#">Economic Calendar</a> | <a href="#">Markets Dashboard</a></div></div>',
                'category': 'newsletter',
                'attachments': [{'filename': 'Market_Report_Sep_2025.pdf', 'size': 2457600}],
                'links': ['https://bloomberg.com/news/fed-decision', 'https://bloomberg.com/economics/cpi', 'https://bloomberg.com/markets/europe']
            },
            {
                'sender': 'Research Dept',
                'email': 'research@investmentbank.com',
                'subject': 'Q4 2025 Market Outlook: Navigating Uncertainty',
                'preview': 'Our latest quarterly outlook examines key themes including monetary policy normalization...',
                'content': 'Detailed research report on market outlook with charts and analysis.',
                'category': 'research',
                'attachment': True
            },
            {
                'sender': 'Fed Alert',
                'email': 'alerts@federalreserve.gov',
                'subject': 'FOMC Meeting Minutes Released',
                'preview': 'Minutes from the Federal Open Market Committee meeting of December 2025...',
                'content': 'Complete FOMC meeting minutes with policy discussions and economic projections.',
                'category': 'official',
                'attachment': True
            },
            {
                'sender': 'Market Watch',
                'email': 'alerts@marketwatch.com',
                'subject': 'Breaking: Major Tech Earnings Beat Expectations',
                'preview': 'Apple, Microsoft, and Google all report better-than-expected quarterly results...',
                'content': 'Earnings summary with key metrics and market reaction.',
                'category': 'news',
                'attachment': False
            },
            {
                'sender': 'Economic Calendar',
                'email': 'calendar@econdata.com',
                'subject': 'This Week: CPI, Retail Sales, Fed Speakers',
                'preview': 'Key economic events for the week ahead including inflation data...',
                'content': 'Weekly calendar of economic releases and central bank speeches.',
                'category': 'calendar',
                'attachment': False
            },
            {
                'sender': 'Trading Desk',
                'email': 'desk@tradingfirm.com',
                'subject': 'Morning Note: Risk-On Sentiment Returns',
                'preview': 'Asian markets rally overnight, European futures point higher...',
                'content': 'Trading desk commentary on overnight moves and positioning.',
                'category': 'trading',
                'attachment': False
            },
            {
                'sender': 'Compliance',
                'email': 'compliance@firm.com',
                'subject': 'Regulatory Update: New Trading Rules',
                'preview': 'Important changes to trading regulations effective next month...',
                'content': 'Regulatory compliance update with new requirements.',
                'category': 'compliance',
                'attachment': True
            },
            {
                'sender': 'Strategy Team',
                'email': 'strategy@hedgefund.com',
                'subject': 'Macro View: Inflation Peak Behind Us?',
                'preview': 'Our analysis suggests inflation has peaked but remains elevated...',
                'content': 'Strategic analysis of inflation trends and policy implications.',
                'category': 'strategy',
                'attachment': True
            }
        ]
        
        # Insert emails with varying timestamps
        for i, email_data in enumerate(sample_emails):
            timestamp = base_time - timedelta(hours=i*3, minutes=random.randint(0, 59))
            cursor.execute('''
                INSERT INTO emails (sender, sender_email, subject, preview, content,
                                  received_at, category, has_attachment)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                email_data['sender'],
                email_data['email'],
                email_data['subject'],
                email_data['preview'],
                email_data['content'],
                timestamp.isoformat(),
                email_data['category'],
                email_data['attachment']
            ))
    
    def get_twitter_items(self):
        """Get tweets from demo database"""
        items = []
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, author_username, author_name, text, created_at,
                   likes, retweets, sentiment, impact
            FROM tweets
            ORDER BY created_at DESC
        ''')
        
        for row in cursor.fetchall():
            items.append({
                'type': 'tweet',
                'id': f'tweet_{row[0]}',
                'author': row[1],
                'author_name': row[2],
                'content': row[3],
                'timestamp': row[4],
                'likes': row[5],
                'retweets': row[6],
                'sentiment': row[7],
                'impact': row[8],
                'source': 'Twitter'
            })
        
        conn.close()
        return items
    
    def get_email_items(self):
        """Get emails from demo database"""
        items = []
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, sender, sender_email, subject, preview, content,
                   received_at, category, has_attachment
            FROM emails
            ORDER BY received_at DESC
        ''')
        
        for row in cursor.fetchall():
            items.append({
                'type': 'email',
                'id': f'email_{row[0]}',
                'sender': row[1],
                'sender_email': row[2],
                'subject': row[3],
                'preview': row[4],
                'content': row[5],
                'timestamp': row[6],
                'category': row[7],
                'has_attachment': row[8],
                'source': 'Email'
            })
        
        conn.close()
        return items
    
    def get_unified_feed(self):
        """Combine tweets and emails into unified feed"""
        all_items = []
        
        # Get tweets and emails
        tweets = self.get_twitter_items()
        emails = self.get_email_items()
        
        # Combine
        all_items.extend(tweets)
        all_items.extend(emails)
        
        # Sort by timestamp
        all_items.sort(key=lambda x: x['timestamp'], reverse=True)
        
        # Format timestamps for display
        for item in all_items:
            dt = datetime.fromisoformat(item['timestamp'])
            item['time_ago'] = self.format_time_ago(dt)
            item['formatted_time'] = dt.strftime('%b %d, %Y at %I:%M %p')
        
        return all_items
    
    def format_time_ago(self, dt):
        """Format datetime as 'X minutes/hours/days ago'"""
        now = datetime.now()
        diff = now - dt
        
        if diff.days > 0:
            return f"{diff.days} day{'s' if diff.days > 1 else ''} ago"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        else:
            minutes = diff.seconds // 60
            if minutes < 1:
                return "just now"
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"

# Initialize collector
collector = DemoFeedCollector()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/feed')
def get_feed():
    """API endpoint to get unified feed"""
    feed_type = request.args.get('type', 'all')
    
    if feed_type == 'all':
        items = collector.get_unified_feed()
    elif feed_type == 'twitter':
        items = collector.get_twitter_items()
        for item in items:
            dt = datetime.fromisoformat(item['timestamp'])
            item['time_ago'] = collector.format_time_ago(dt)
            item['formatted_time'] = dt.strftime('%b %d, %Y at %I:%M %p')
    elif feed_type == 'email':
        items = collector.get_email_items()
        for item in items:
            dt = datetime.fromisoformat(item['timestamp'])
            item['time_ago'] = collector.format_time_ago(dt)
            item['formatted_time'] = dt.strftime('%b %d, %Y at %I:%M %p')
    else:
        items = []
    
    return jsonify({'items': items, 'count': len(items)})

@app.route('/api/tweet/<tweet_id>')
def get_tweet_detail(tweet_id):
    """Get detailed view of a tweet with AI analysis"""
    # Extract numeric ID
    numeric_id = tweet_id.replace('tweet_', '')
    
    conn = sqlite3.connect(DEMO_DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT author_username, author_name, text, created_at,
               likes, retweets, replies, sentiment, impact,
               monetary_policy, market_sentiment, market_impact,
               confidence, reasoning
        FROM tweets WHERE id = ?
    ''', (numeric_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    if row:
        dt = datetime.fromisoformat(row[3])
        
        # Format AI analysis percentages
        monetary_score = row[9] if row[9] else 0
        market_sent = row[10] if row[10] else 0
        market_imp = row[11] if row[11] else 0
        conf = row[12] if row[12] else 0
        
        return jsonify({
            'author': row[0],
            'author_name': row[1],
            'content': row[2],
            'timestamp': row[3],
            'formatted_time': dt.strftime('%b %d, %Y at %I:%M %p'),
            'likes': row[4],
            'retweets': row[5],
            'replies': row[6],
            'sentiment': row[7],
            'impact': row[8],
            'ai_analysis': {
                'monetary_policy': {
                    'value': monetary_score,
                    'percentage': int((monetary_score + 1) * 50),  # Convert -1 to 1 scale to 0-100%
                    'label': 'Dovish' if monetary_score > 0 else 'Hawkish' if monetary_score < 0 else 'Neutral'
                },
                'market_sentiment': {
                    'value': market_sent,
                    'percentage': int((market_sent + 1) * 50),
                    'label': 'Bullish' if market_sent > 0 else 'Bearish' if market_sent < 0 else 'Neutral'
                },
                'market_impact': {
                    'value': market_imp,
                    'percentage': int(market_imp * 100),
                    'label': 'High' if market_imp > 0.7 else 'Medium' if market_imp > 0.3 else 'Low'
                },
                'confidence': {
                    'value': conf,
                    'percentage': int(conf * 100)
                },
                'reasoning': row[13] if row[13] else 'AI analysis shows this tweet contains market-relevant information.'
            }
        })
    
    return jsonify({'error': 'Tweet not found'}), 404

@app.route('/api/email/<email_id>')
def get_email_detail(email_id):
    """Get detailed view of an email with rich HTML content"""
    # Extract numeric ID
    numeric_id = email_id.replace('email_', '')
    
    conn = sqlite3.connect(DEMO_DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT sender, sender_email, subject, content, html_content,
               received_at, category, has_attachment, attachments, links,
               content_length
        FROM emails WHERE id = ?
    ''', (numeric_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    if row:
        dt = datetime.fromisoformat(row[5])
        
        # Parse JSON fields
        attachments = json.loads(row[8]) if row[8] else []
        links = json.loads(row[9]) if row[9] else []
        
        return jsonify({
            'sender': row[0],
            'sender_email': row[1],
            'subject': row[2],
            'content': row[3],
            'rendered_content': row[4],  # The rich HTML content!
            'timestamp': row[5],
            'formatted_time': dt.strftime('%b %d, %Y at %I:%M %p'),
            'category': row[6],
            'has_attachment': row[7],
            'attachments': attachments,
            'attachment_count': len(attachments),
            'extracted_links': links,
            'link_count': len(links),
            'content_length': row[10],
            'content_type': 'html'
        })
    
    return jsonify({'error': 'Email not found'}), 404

if __name__ == '__main__':
    print("\n🚀 SAGE Unified Feed DEMO")
    print("=" * 50)
    print("📊 This is a demonstration version with sample data")
    print("🔗 No API keys or external services required")
    print("💾 All data stored in local SQLite database")
    print("=" * 50)
    print(f"\n✨ Starting server on http://localhost:5532")
    print("   Press Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5532, debug=False)
