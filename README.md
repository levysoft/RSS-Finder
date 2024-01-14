# RSS Finder

## Description
This Python script (`rss_finder.py`) is designed to find RSS or Atom feeds on a given website. It tries multiple strategies, including looking for `<link>` tags in the HTML head that point to a feed, as well as trying common feed URL patterns.

## Requirements
- Python 3
- Libraries: `urllib.parse`, `html5lib`, `feedparser`, `requests`. You can install these libraries using pip:
  ```bash
  pip install html5lib feedparser requests

  or install dependencies:

  `pip install -r requirements.txt`

## Installation
To set up the development environment:

1. Clone the repository:

   `git clone https://github.com/levysoft/RSS-Finder`

2. Enter the project directory:

   `cd RSS-Finder`

3. Create a Python virtual environment:

   `python3 -m venv venv`

4. Activate the virtual environment:

   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install dependencies:

   `pip install -r requirements.txt`

## Usage
To use the script, run it with a single argument: the URL of the website you want to find the feed for. For example:

`python3 rss_finder.py https://example.com`

## How it Works

The script makes a request to the given URL and parses the HTML response. It then searches for <link> elements that point to Atom or RSS feeds. If none are found, it tries appending common feed paths to the base URL to see if any valid feeds exist.

## Attribution
This script is inspired by and based on the autodiscovery functionality found in the RSS aggregator Temboz, specifically in the autodiscovery module: [Temboz Autodiscovery Module](https://github.com/fazalmajid/temboz/blob/master/tembozapp/autodiscovery.py).

## Author
Antonio Troise

## License
This project is released under the MIT License. See the LICENSE file for more details.


