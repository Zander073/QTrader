# QTrader
Final project for machine learning class (CMSI 5350). 

A deep reinforcement learning agent that uses deep deterministic policy gradient (DDPG) to learn a stock trading strategy.

# Understanding DDPG and the Problem
1. Before jumping into the code, I highly recommend navigating to the repository's "doc" section where there is a detailed explanation on reinforcement learning and DDPG. Visit https://github.com/Zander073/QTrader/tree/main/docs for my detailed explanation of DDPG. For further reading on DDPG and deep reinforcement learning, visit OpenAI's Deep RL resource: https://spinningup.openai.com/en/latest/

2. Because the agent is attempting to learn some kind of policy for trading, I recommend learning more about stock trading if you do not know much about it already. There is a brief explanation on this problem in the final report within the doc section of this repository. For more information on stock trading, visit Investopedia's guide: https://www.investopedia.com/stock-trading-4689660

3. If you are interested in training your own DDPG agent with different parameters I recommend you use a GPU if you have on already or you can use Google's CoLab cloud based environment for training. They have free GPU's you can use for training. For more information on training in Google's CoLab, visit: https://www.tutorialspoint.com/google_colab/google_colab_using_free_gpu.htm and https://research.google.com/colaboratory/faq.html

# Getting Ready to Run the Project
  # If interested in training yourself:
  1. If you already have a Google account go to https://colab.research.google.com/ and create a new notebook. 
  2. Once your new notebook is created, navigate to 'file' -> 'upload notebook' and look up this repository by pasting the following link into the URL      input area: https://github.com/Zander073/QTrader and then enter.
  3. Click on 'src/QTrader.ipynb'
  4. You will need to configuration file so go to https://github.com/Zander073/QTrader, click the green 'Code' button and then press downlaod zip. From this zip file you will need to extract the config.py file.
  5. Once you have the config.py file, enter it into your Google CoLab session. 
  6. Now run! You can alter the training and environment parameters in the config file. You will need to restart the runtime everytime you change the configuration file. 
  
  # If not interested in training yourself and want to experiment with this prewritten code:
  1. Navigate to your command prompt. 
  2. If you do not have Jupyter Notebook installed, install it using the pip package manager:
     ```pip install notebook```
  3. Navigate to a section in your command prompt where you want the project to exist. 
  4. Clone the repository: ```git clone https://github.com/Zander073/QTrader.git```
  5. Once the repository has successfully been cloned, launch the project by entering the following in the command prompt: ```jupyter notebook```
  6. You can now run the code! To end your session, go to 'file' -> 'save' or press 'command'+'s'
