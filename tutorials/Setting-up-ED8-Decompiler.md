# ED8 Decompiler
ED8 Decompiler is a powerful tool made by [Ouroboros](https://github.com/Ouroboros) (an actual developer, that's his name!) to edit script files in CS3/CS4/Reverie (called ED85). Scripts files contain the logic describing events, crafts, minigames, etc, and are located in the "data\scripts\ani\dat_en" folder of English games.
However the installation could be a bit troublesome to newcomers who don't have a prior knowledge of how Python works, so this small guide will attempt to help you set up an environment to use the tool. There is also the [wiki of the Falcom repository](https://github.com/Ouroboros/Falcom/wiki/Decompiler2-ED8-Usage) that contains instructions in English, but I find them a bit lacking, thus why I am writing the present guide. \
Also this guide will focus on ED84 (Cold Steel IV) but other games follow the same logic.

# Setting up your environment
First, make sure you have Python version 3.10 or a superior version installed to your computer. If you never installed Python, please grab the installer [here](https://www.python.org/downloads/).
Once Python is installed, you will need to get ED8 Decompiler. Start by downloading the folder called "Decompiler2" in the [Falcom repository](https://github.com/Ouroboros/Falcom):
![image](https://user-images.githubusercontent.com/69110695/186164696-d20fcad9-b8dd-4bde-94cc-bf2960997092.png)\
Create a new folder on your machine, called for example "Decompiler", and extract Decompiler2 inside it:
![image](https://user-images.githubusercontent.com/69110695/186166699-37993081-8358-43e2-8917-87f768bb4c85.png)

You will also need a few libraries, which are available [here](https://github.com/Ouroboros/PyLibs)\
Extract PyLibs in the Decompiler folder where Decompiler2 is located:\
![image](https://user-images.githubusercontent.com/69110695/186167377-5578605b-9629-4cb3-a6b6-bf6b51bca095.png)

Next, put the [decompile.bat](https://github.com/Trails-Research-Group/Doc/releases/download/v0.0/decompile.bat) and [recompile.bat](https://github.com/Trails-Research-Group/Doc/releases/download/v0.0/recompile.bat) files we provide inside the Decompiler directory:
![image](https://user-images.githubusercontent.com/69110695/186172877-ec0675df-81ba-4dae-9657-509a6853a94a.png)\
Your environment is now technically set, minus a few packages that you might need and that we will take care in the following section.

# Decompiling a .dat file
Grab a dat file, for example, scripts/ani/chr000.dat, and put it in the Decompiler directory.
![image](https://user-images.githubusercontent.com/69110695/186176366-e69e3cc8-6d63-4bed-88a3-43f0dc455f39.png)

Then, drag and drop your dat file onto decompile.bat. It might show something like this:
![image](https://user-images.githubusercontent.com/69110695/186174405-a23e3350-bf80-413a-ab4e-a06e35554b8b.png)\
This means you still have a few packages to install. To do so, type "pip install <package_name>" in the console; on the above screenshot, <package_name> is to be replaced with "aiohttp". So it gives: pip install aiohttp:

![image](https://user-images.githubusercontent.com/69110695/186177599-d97d20a1-a72f-4926-a45c-6b21ff5f033e.png)

It will install the corresponding package. Do that until all missing packages are installed and you can finally decompile a .dat file succesfully. Then the console will look like this:\
![image](https://user-images.githubusercontent.com/69110695/186176063-1732ab5c-045b-4215-937f-6dde2c396b20.png)

# The whole process of decompiling/recompiling:
![DecompGuide](https://user-images.githubusercontent.com/69110695/186179044-4b9acdb0-eab1-457e-a7a9-221455721ba9.gif)

# Recompiling a .dat file
After decompiling the dat file, you obtained a .py file that appeared inside the Decompiler directory. Do whatever script editing you want to do, then when you are finished, drag and drop the .py onto recompile.bat.
It should generate a new dat file, that you can put at its original place inside the game directory.







