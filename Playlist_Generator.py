import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def fetch_movie_data(movie_url):
    try:
        response = requests.get(movie_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch content from {movie_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def fetch_logo_urls(logo_url):
    try:
        response = requests.get(logo_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch content from {logo_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_m3u_file(movie_url, logo_url, output_file='playlist.m3u'):
    base_url = urljoin(movie_url, '')

    movie_data = fetch_movie_data(movie_url)
    logo_data = fetch_logo_urls(logo_url)

    if movie_data is not None and logo_data is not None:
        movie_soup = BeautifulSoup(movie_data, 'html.parser')
        logo_soup = BeautifulSoup(logo_data, 'html.parser')

        with open(output_file, 'w', encoding='utf-8') as m3u_file:
            m3u_file.write("#EXTM3U\n")

            for a_tag in movie_soup.find_all('a', href=True):
                movie_name = os.path.splitext(a_tag.text.strip())[0]  # Remove file extension
                movie_file = urljoin(base_url, a_tag['href'])
                logo_file = find_logo(logo_soup, movie_name)

                m3u_file.write(f'#EXTINF:-1 tvg-logo="{urljoin(logo_url, movie_name + ".jpg")}" group-title="Movies",{movie_name}\n')
                m3u_file.write(f"#EXTVLCOPT:network-caching=1000\n")  # Optional VLC network caching setting
                m3u_file.write(f"{movie_file}\n")
                m3u_file.write('\n')

        print(f"M3U file '{output_file}' generated successfully.")

def find_logo(logo_soup, movie_name):
    # Adjust this function based on the actual structure of your logo data
    for img_tag in logo_soup.find_all('img', alt=True):
        if movie_name.lower() in img_tag['alt'].lower():
            return img_tag['src']
    return None

# Example usage:
movie_url = 'https://server4.newtamilmovies.in/assets1/2021TamiliMovies/'
logo_url = 'https://server4.newtamilmovies.in/assets1/2021MoviesPoster/'
generate_m3u_file(movie_url, logo_url)
