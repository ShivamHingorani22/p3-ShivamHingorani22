# P3. Final Project - Simple Moving Average (SMA) Calculator
By: Shivam Hingorani

As described in my Project Proposal, the SMA Calculator calculates the Simple Moving Average for a given stock's closing price and creates a graph of the same of the same over a requested trading period.

The SMA Calculator relies on a number of libraries to function.  As such, it is necessary that any users of the tool resolve the dependencies within their environment before running the SMA Calculator.  This can be done by navigating to the tool's repository, launching the desired environment (virtual environments are highly recommended), and running ```pip -r requirements.txt```.  This will install all required libraries to the user's environment.

The SMA Calculator has a number of possible input parameters, though not all of them are required.  They are as follows: 
* **Symbol (```-s```):** the ticker of stock whose SMA you wish to calculate. *(required)*
* **Period (```-p```):** the data period over which to analyze the stock. Options include ```'1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd'```, and ```'max'```.  *(not required; defaults to ```'1y'```)*
* **Window (```-w```):** the number of periods to include in the SMA. *(not required; defaults to ```20```)*
* **Consumer (```-c```):** the consumer for whom to format the output. Options include ```'human'``` (opens SMA chart in browser) and ```'machine'``` (stores CSV file in tool's repository). *(not required; defaults to ```'human'```)