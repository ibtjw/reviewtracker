# Review Tracker

A simple web service written in Python to extract reviews from a url and return the results in JSON.

```
[
  {
    "author": "Vincent",
    "content": "Apparently, the idea is to find some reason to deny you funding (in my case, too many hard inquiries despite a very good credit score) after being on hold for some time and then hook you up with someone who will help you remove them (for a fee, of course).",
    "date": "Reviewed in July 2021",
    "loan_type": "Small Business Loan",
    "location": "Cheswick,  PA",
    "stars": "1 of 5 stars",
    "title": "It is a scam"
  }
  ....
]
```

# Setup

1. Clone the repository and setup the virtual environment

```
git clone https://github.com/ibtjw/reviewtracker.git
cd reviewtracker
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the service

```
flask run
```

# Test

Test a url with the format `url=https ...`
```
curl -X POST http://127.0.0.1:5000/reviews -d 'url=https://www.lendingtree.com/reviews/business/seek-capital/65175902'
```

Run tests
```
python -m pytest tests/ -v
```