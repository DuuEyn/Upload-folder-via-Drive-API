from Authentication.auth import OAuthCall
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def upload_file():
  service = build("drive", "v3", credentials=OAuthCall(SCOPES))
  file_path = "File-path-including-filename"
  #Splits the filename from the filepath
  file_name = file_path.split("/")[-1]

  #Creates the file metadata for upload.
  #Google Drive attempts to automatically detect a valid mimeType for the uploaded file, if no value is provided.
  #Add a "mimeType" keya-value pair inside file_metadata if needed
  file_metadata = {
      "name": file_name,
      "parents": ["parent-folder-id"],
  }

  try:
      print(f"Uploading the file {file_name}")
      media = MediaFileUpload(file_path, resumable=True)

      #Calls the files.create() method to upload the file to Google Drive.
      file = (
          service.files()
          .create(
              body=file_metadata,
              media_body=media,
          )
          .execute()
      )
      print(f"{file_name} uploaded.")

      #Returns the uploaded file. Can be used on another function.
      return file
    
  except Exception as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  upload_file()
