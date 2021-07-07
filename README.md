# Password generator

It is a simple password generator, created with Python and PyQT5.  
It is capable to generate passwords with required length and save them into 
files.

![Password generator main window](imgs/pass_gen_screenshot.png)

## Navigation
* [Installation](#installation)
    * [Python](#python)
    * [Windows](#windows)
        * [Notes](#notes)
    * [PyInstaller](#pyinstaller)
* [Releases](#releases)

## Installation

Clone repository with command:
```shell script
git clone https://github.com/IHappyPlant/PasswordGenerator.git
```

Then step into cloned repo with command:
```shell script
cd PasswordGenerator
```

### Python
To install application directly into Python, run command:  
```shell script
python3 setup.py install
```
Installed package will be named ```PasswordGenerator```  
After installation, you can run it using command:
```shell script
python3 -m PasswordGenerator
```

### Windows
In MS Windows you may install package into Python in another way: 
1. ```shell script
    python3 setup.py bdist_msi
    ```
3. ```shell script
    cd dist
    ```
2. Run built installer to install application.  

#### Notes
Windows Defender may block .msi-installer, because it doesn't have 
signed certificate. Just ignore it.

### PyInstaller

You also may build executable file for your OS with PyInstaller.  
For this, you need to do next steps:    
 1. ```shell script
    pip3 install -r requirements.txt pyinstaller
    ```
 2. ```shell script
    pyinstaller password_generator/__main__.py
    ```
## Releases

You can also download created executable files for MS Windows and 
Debian/Ubuntu from releases.
