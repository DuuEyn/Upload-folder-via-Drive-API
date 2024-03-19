<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<div align="center">
<h3 align="center">Folder upload via Drive API</h3>

  <p align="center">
    Uploads a folder and its contents to Google Drive via Drive API 
    <br />
    <a href="https://github.com/DuuEyn/Upload-folder-via-Drive-API
"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DuuEyn/Upload-folder-via-Drive-API
">View Repo</a>
    ·
    <a href="https://github.com/DuuEyn/Upload-folder-via-Drive-API
/issues">Report Bug</a>
    ·
    <a href="https://github.com/DuuEyn/Upload-folder-via-Drive-API
/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<br />
<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br />



<!-- ABOUT THE PROJECT -->
## About The Project

Creates a folder in Google Drive with the same name as the source folder. The script iterates through the source folder and uploads each file to the created folder in Google Drive.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* Enable <a href="https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com"><strong>Google Drive API</strong></a> in the Google Cloud project
* Configure the <a href="https://developers.google.com/drive/api/quickstart/python#configure_the_oauth_consent_screen"><strong>OAuth consent screen</strong></a>
* Create a Web App OAuth credential by following these steps:
  1. Go to the <a href="https://console.developers.google.com/apis/credentials"><strong>Credentials page</strong></a> of your Google Cloud project.
  2. Click <strong>Create credentials > OAuth client ID</strong>.
  3. Select the <strong>Web application</strong> application type.
  4. Name your OAuth 2.0 client, set a `redirect URI` and click <strong>Create</strong>.
  5. Download the JSON file and rename it as `client_secret.json`.

* Install the following Google Client libraries for Python:
  ```sh
  pip install --upgrade google-api-python-client google-auth-oauthlib
  ``` 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DuuEyn/Upload-folder-via-Drive-API
   ```
2. Replace the `client_secret.json` file inside the `Authentication` folder with JSON file generated for your project.
3. Replace the `redirect_uri` in the `OAuthCall` function inside `Authentication/auth.py` with the same one inside `client_secret.json`
4. In the `upload_file` function of `DriveUpload.py`, Specify the path of the folder that needs to be uploaded in `folder_path`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This script can be utilized to automate the upload of folders from the local device to Google Drive without using Google Drive for desktop or manually uploading via Drive's web interface.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

DuuEyn - iddiche@gmail.com

Project Link: [https://github.com/DuuEyn/Upload-folder-via-Drive-API](https://github.com/DuuEyn/Upload-folder-via-Drive-API)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Othnieldrew's README template](https://github.com/othneildrew/Best-README-Template)
* [Google Drive API's Python quickstart guide](https://developers.google.com/drive/api/quickstart/python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DuuEyn/Upload-folder-via-Drive-API.svg?style=for-the-badge
[contributors-url]: https://github.com/DuuEyn/Upload-folder-via-Drive-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DuuEyn/Upload-folder-via-Drive-API.svg?style=for-the-badge
[forks-url]: https://github.com/DuuEyn/Upload-folder-via-Drive-API/network/members
[stars-shield]: https://img.shields.io/github/stars/DuuEyn/Upload-folder-via-Drive-API.svg?style=for-the-badge
[stars-url]: https://github.com/DuuEyn/Upload-folder-via-Drive-API/stargazers
[issues-shield]: https://img.shields.io/github/issues/DuuEyn/Upload-folder-via-Drive-API.svg?style=for-the-badge
[issues-url]: https://github.com/DuuEyn/Upload-folder-via-Drive-API/issues
[license-shield]: https://img.shields.io/github/license/DuuEyn/Upload-folder-via-Drive-API.svg?style=for-the-badge
[license-url]: https://github.com/DuuEyn/Upload-folder-via-Drive-API/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ian-dewaine-diche-69406a2bb
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
