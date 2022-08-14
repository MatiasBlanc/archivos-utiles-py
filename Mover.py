from PIL import Image
import os 

downloadsFolder = "/Users/Matias Blanc/Downloads/"
picturesFolder = "/Users/Matias Blanc/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
        if extension in [".jpg", ".jpeg", ".png", ".svg"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_"+filename, optimize=True, quality=65)
            os.remove(downloadsFolder + filename)
            print(name + ":" + extension)

        if extension in [".mp3", ".wav", ".flac", ".aac", ".m4a"]:
            musicFolder = "/Users/Matias Blanc/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ":" + extension)


        if extension in [".mp4",".avi",".mkv",".mov",".flv",".webm",".mpg",".mpeg",".wmv"]:
            videosFolder = "/Users/Matias Blanc/Videos/"
            os.rename(downloadsFolder + filename, videosFolder + filename)
            print(name + ":" + extension)