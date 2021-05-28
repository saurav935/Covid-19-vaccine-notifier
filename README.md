# Covid-19-vaccine-notifier


![blue-covid-banner](https://user-images.githubusercontent.com/75733364/119965020-6d6a1d00-bfc7-11eb-8a51-6bc5d8600403.jpg)





Covid-19 vaccine-notifier periodically checks and sends email notifications for available slots for the next 7 days on CoWIN portal in a given area and age.


The CoWin API currently states : "Further, these APIs are subject to a rate limit of 100 API calls per 5 minutes per IP". I tried deploying the Web Application but the API is blocking the request. You can easily run the web application on your machine by following the steps mentioned below.  

Update
I am humbled to see the overwhelming response that this project has received so far. Feel free to create amazing applications on top of this project. Due to my schedule, I won't be able to allot more time to this project. So there won't be any additional commits to this project.

Installing Python
Python is a programming language that is powerful but easy to learn. It is free, platform-independent, and popular among scientists.

Recommended Method: Anaconda
The Anaconda Python distribution is an easily-installable bundle of Python and many of the libraries used throughout this class. Unless you have a good reason not to, we recommend that you use Anaconda.

Mac/Linux users
Download the appropriate version of Anaconda
Follow the instructions on that page to run the installer
Test it out: open a terminal window, and type python, you should see something like
Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
If Anaconda doesn't appear on the first line, you are using a different version of Python. See the troubleshooting section below.

Test out the IPython notebook: open a Terminal window, and type ipython notebook. A new browser window should pop up.
Click New Notebook to create a new notebook file
Update IPython to the newest version by typing conda update ipython at the command line
Windows Users
Download the appropriate version of Anaconda
Follow the instructions on that page to run the installer.
Go to Start and Run Jupyter Notebook.
Click New Notebook, which should open a new page.
Usage
Clone the repository. using ! Git Clone https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability.git

The tool only works with Indian IP addresses so disconnect your VPN if needed.

Enter the command - cd cowin-vaccination-slot-availability/

Install all the dependencies - ! pip3 install -r requirements.txt

Run Anaconda Promt (Run as Administrator) From Start Menu.

Go to your Directory Eg cd C:\Users\lenovo\Desktop\Jupyter Notebooks\2021\Cowin\cowin-vaccination-slot-availability

Run streamlit run app.py

You can now view your Streamlit app in your browser.
