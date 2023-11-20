import os
import requests
import random
import ctypes
import time

# Set your Pixabay API key
pixabay_api_key = "38417398-353b6532b754cec48c6982d2a"

# Folder to store downloaded images
download_folder = "D:\\PLACEMENT PREPARE\\python\\image-downloader\\x"


# Function to fetch images from Pixabay and store them in the download folder
def fetch_and_store_pixabay_images(query, num_images=10):
    try:
        # Make a request to the Pixabay API
        api_url = f"https://pixabay.com/api/?key={pixabay_api_key}&q={query}&image_type=photo&per_page={num_images}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for non-200 HTTP status codes

        data = response.json()
        if "hits" in data:
            image_urls = [hit["largeImageURL"] for hit in data["hits"]]
            # Create the download folder if it doesn't exist
            os.makedirs(download_folder, exist_ok=True)
            # Download and save images to the download folder
            for i, image_url in enumerate(image_urls):
                try:
                    response = requests.get(image_url)
                    response.raise_for_status()
                    image_path = os.path.join(download_folder, f"image_{i}.jpg")
                    with open(image_path, "wb") as f:
                        f.write(response.content)
                except requests.exceptions.RequestException as e:
                    print(f"Request error while downloading image {i}:", e)
                except Exception as e:
                    print(f"An error occurred while downloading image {i}:", e)
        else:
            print("No 'hits' key in API response.")
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
# Replace "YOUR_PIXABAY_API_KEY" with your Pixabay API key and specify your desired query and the number of images to fetch.
# fetch_and_store_pixabay_images("nature", num_images=10)

fetch_and_store_pixabay_images("suit",num_images=10)