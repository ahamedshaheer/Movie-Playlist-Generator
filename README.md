<!DOCTYPE html>
<html lang="en">

<body>

<h1>Movie Playlist Generator</h1>

<p>This Python script allows you to generate an M3U playlist file for a collection of movies, including their corresponding logo URLs. The script utilizes web scraping techniques to extract movie information and logo URLs from provided URLs.</p>

<h2>Dependencies</h2>

<p>Make sure you have the following Python libraries installed:</p>

<pre><code>pip install requests beautifulsoup4
</code></pre>

<h2>Usage</h2>

<ol>
  <li>Import the required modules:</li>

  <pre><code>import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
  </code></pre>

  <li>Define the functions:</li>

  <ul>
    <li><code>fetch_movie_data(movie_url)</code>: Fetches HTML content from the specified movie URL.</li>
    <li><code>fetch_logo_urls(logo_url)</code>: Fetches HTML content from the specified logo URL.</li>
    <li><code>generate_m3u_file(movie_url, logo_url, output_file='playlist.m3u')</code>: Generates an M3U playlist file containing movie information and corresponding logo URLs.</li>
    <li><code>find_logo(logo_soup, movie_name)</code>: Finds the logo URL based on the movie name in the logo HTML content.</li>
  </ul>

  <li>Example usage:</li>

  <pre><code>movie_url = 'provide movie url here'
logo_url = 'provide logo url here'
generate_m3u_file(movie_url, logo_url)
  </code></pre>
</ol>

<p>Replace <code>'provide movie url here'</code> and <code>'provide logo url here'</code> with the actual URLs you want to use.</p>

<p><strong>Note:</strong> Ensure that the provided URLs are valid and the web pages' structure matches the script's expectations for successful scraping.</p>

<h2>Running the Script</h2>

<p>Execute the script in a Python environment. For example:</p>

<pre><code>python script_name.py
</code></pre>

<p>Replace <code>script_name.py</code> with the actual name of your Python script file.</p>

<p>The generated M3U file (<code>playlist.m3u</code> by default) will contain entries for each movie, including metadata such as the movie name, logo URL, and video URL. Adjust the script or the <code>find_logo</code> function as needed based on the structure of the web pages you are scraping.</p>

<p>Feel free to customize the script further to suit your specific requirements.</p>

</body>
</html>
