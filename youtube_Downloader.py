from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download('C:/Users/Milind/Downloads/data_science_lecture')
    except:
        print('An error has occured')
    print('Download is completed successfully.')

link = 'https://www.youtube.com/watch?v=4GzAwnjVTqc' #input("Enter the Youtube Video Url : ")
Download(link)