<!-- PROJECT SHIELDS -->
<!--
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Remove_shorts</h3>
  <p align="center">
    A generalized solution for pressing alt + F4 when a certain url is activated
</div>



<!-- TABLE OF CONTENTS -->
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
I have seen many people express disgust for youTube Shorts so i decided to code up this project which is really a genealized solution for pressing `alt + f4` if you visit some url. I wanted to make a usefull silly progect with multiple moving parts -- I think this is it.

Here's why:
* To stop wasting your time on youtube shorts.
* To understand the project and concepts like servers and ports.

Of course, this project is not intended to be a solution to any real problems, but i would like to try to keep this as usefull as possible so feel free to send me an email with any issues or  you can do the pull request or issue thing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

These are the modules used to build this project.

* Python (version 3)
* Flask
* Flask_CORS
* PyAutoGUI
* ArgParse


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Flask
  ```sh
  py -m pip install flask
  ```
* Flask_CORS
  ```sh
  py -m pip install flask_cors
  ```
* PyAutoGUI
  ```sh
  py -m pip install pyautogui
  ```
* ArgParse
  ```sh
  py -m pip install argparse
  ```

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/name81190/remove_shorts.git
   ```

2. Install the Extension
    * navigate to [chrome://extensions](chrome://extensions)
    * Turn on developer mode and click `Load unpacked`
    * Select the `kill_shorts` folder.

3. **Optionally** configure the py file to run on computer startup
    * adapt the `autoexe.bat` to your system: <br>
        The current autoexe.bat file is as follows:
        ```bat
        @echo off
        py C:\kill_shorts\server.py
        ```
        However, not everyone uses the py prefix and the directory will not be the same for all users. You should adapt this to your system. Here’s how:

        1. Replace `py` with the command you use to run Python scripts. This could be `python`, `python3`, or `py`, depending on your system.
        2. Replace `C:\kill_shorts\server.py` with the correct path to your `server.py` file.
        our adapted autoexe.bat file might look something like this:

        ```bat
        @echo off
        python3 D:\path\to\your\kill_shorts\server.py
        ```

    * navigate to the `shell:starup` directory by pressing `Win + R`
    * move the py file to that folder. <br>
    The Pyton file will now automaticaly run
    


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
When the extension is installed and the you have ran the autoexe.bat (either manualy or through shell:startup) any attempt to visit a url containing `youtube.com/shorts` will be thwarted via `Alt + F4`.<br>
To adapt the trigger url change the --TRIGGER_URL cmd argument:
```bat
py C:\kill_shorts\server.py --TRIGGER_URL=example
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add automatic running functionality
- [x] Add TRIGGER_URL to alow for diferent purposes
- [x] Upload to GitHub
- [ ] Add shell hiding functionality
- [ ] Fix da bugs
- [ ] Get a life

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

^^^ I copy-pasted that from a template idk what that even means XD
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@name_81190](https://discord.com/users/1172001101562789950) - uniqueandrandomemailname@gmail.com

Project Link: [https://github.com/name81190/remove_shorts](https://github.com/81190/remove_shorts)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [MIT License](https://choosealicense.com/licenses/mit/)
* [Microsoft Copilot](https://copilot.microsoft.com/)
* [README Template](https://github.com/othneildrew/Best-README-Template/tree/master)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/name81190/remove_shorts.svg?style=for-the-badge
[contributors-url]: https://github.com/name81190/remove_shorts/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/name81190/remove_shorts.svg?style=for-the-badge
[forks-url]: https://github.com/name81190/remove_shorts/network/members
[stars-shield]: https://img.shields.io/github/stars/name81190/remove_shorts.svg?style=for-the-badge
[stars-url]: https://github.com/name81190/remove_shorts/stargazers
[issues-shield]: https://img.shields.io/github/issues/name81190/remove_shorts.svg?style=for-the-badge
[issues-url]: https://github.com/name81190/remove_shorts/issues
[license-shield]: https://img.shields.io/github/license/name81190/remove_shorts.svg?style=for-the-badge
[license-url]: https://github.com/name81190/remove_shorts/blob/master/LICENSE.txt