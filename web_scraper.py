from google_images_download import google_images_download
import argparse

parser = argparse.ArgumentParser(description='Download images.')
parser.add_argument('-k', '--keywords', help='delimited list input', type=str, nargs= '+')
parser.add_argument('-n', '--number_of_images', help='number of downloading images', type=str, nargs=1)      
args = parser.parse_args()
response = google_images_download.googleimagesdownload()  
search_queries = args.keywords
y = args.number_of_images
x = int(y[0])
  
def downloadimages(query): 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit": x, 
                 "print_urls":False, 
                 "size": "medium", 
                 "aspect_ratio": "panoramic"}
    try: 
        path = response.download(arguments) #this is a tuple
    
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit": x, 
                     "print_urls":False,  
                     "size": "medium"} 
        try: 
            response.download(arguments)  
        except: 
            pass

for query in search_queries: 
    downloadimages(query)
    