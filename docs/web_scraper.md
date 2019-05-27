**MEGALOTIS OpenCV-SAPPHIRE repo for scripts**
======
_created by_ László Bogár, Tamás Németh, Zoltán Németh, Márton Porkoláb, Lilla Tóth

## **Project documentation**

We have been creating a program that is able to detect and modify shapes and text on images. This repository is a container of all the Python scripts that have been used for the above mentioned OpenCV project by MEGALOTIS-SAPPHIRE project team.<br/>

List of available scripts, their definitions, and short descriptions:


- image download with web scraper

 `downloadimages(query)`<br/>

The 'web_scraper.py' command can be executed in command line. It takes four obligatory arguments as input to implement them into downloadimages(query) function that are able to download images around a given topic and users are able to download as many images as they want. To implement this function, users have to give the following arguments: -k <keyword, as the topic> -n <number of downloading images>. If users need more help, they can use -h/--help argument after 'web_scraper.py' command. The extensions of the downloaded files are .jpg. The command generate a folder called 'download' and each query will be saved in different subfolders with the names of the pre-given keywords.<br/>