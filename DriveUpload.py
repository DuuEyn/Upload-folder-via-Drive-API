import os

from Authentication.auth import OAuthCall
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def upload_file():
  service = build("drive", "v3", credentials=OAuthCall(SCOPES))

  #Path of the folder where the files to be uploaded are located.
  folder_path = "folder-path"

  #Gets the name of the folder.
  folder_name = os.path.basename(folder_path)

  #Creates the folder metadata that will be passed through the API call.
  folder_metadata = {
    "name": folder_name,
    "mimeType": "application/vnd.google-apps.folder",
  }

  #Creates a folder in Google Drive with the same name as the source.
  folder = service.files().create(
    body = folder_metadata,
    fields = "id",
  ).execute()

  #Iterates through each file in source folder.
  for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    #Creates the file metadata for upload.
    file_metadata = {
        "name": file,
        "parents": [folder.get("id")],
    }
    
    try:
      print(f"\nUploading the file {file}")
      media = MediaFileUpload(file_path, resumable=True)
  
      #Calls the files.create() method to upload the file to Google Drive.
      service.files().create(
          body=file_metadata,
          media_body=media,
      ).execute()
      print(f"{file} uploaded.")

    except Exception as error:
      print(f"An error occurred: {error}")


if __name__ == "__main__":
  upload_file()
