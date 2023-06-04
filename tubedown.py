from fastapi import FastAPI, HTTPException
from pytube import YouTube

app = FastAPI()

@app.get("/download")
async def download_video(url: str = "https://youtube.com/shorts/8E5Pxn5AVGE?feature=share"):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # Download the video to the current working directory
        stream.download()

        return {"message": "Video downloaded successfully!"}
    except KeyError:
        raise HTTPException(status_code=400, detail="Error: Video is not available or cannot be downloaded")
    except ValueError:
        raise HTTPException(status_code=400, detail="Error: Invalid URL")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error downloading video: " + str(e))
