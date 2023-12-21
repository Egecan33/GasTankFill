Gas Purchase Optimization Tool

Introduction

This Python tool is designed to help individuals optimize their gas purchases based on economic principles. Using the Economic Order Quantity (EOQ) model, it calculates the most cost-effective amount of gas to purchase each time you visit a gas station. This tool considers factors like the cost to fill a tank, average gas consumption, hourly wage, and the current interest rate to suggest the optimal purchase quantity, aiming to minimize opportunity costs and maximize savings.

Features

Calculates the optimal gas purchase quantity.
Considers personal financial factors like hourly wage and interest rate.
Estimates annual savings and reduced gas station visits.
Prerequisites

Python 3.x installed on your system.

Installation

This project does not require any external libraries. You can clone the repository using:

git clone https://github.com/Egecan33/GasTankFill

Usage

To use the tool, run the main.py script. You will be prompted to enter:

The cost to fully fill your gas tank.
Your hourly wage.
Your preferred currency.
Average duration (in months) a full tank lasts.
Current annual interest rate in your country.
Based on these inputs, the tool will calculate and suggest the optimal amount of gas to buy on each visit to the gas station.


The tool will output:

The calculated optimal gas purchase amount.
The number of gas station visits per year following the strategy.
The estimated time spent at gas stations annually.
The potential savings per year by following this strategy.

Contributing

Contributions to this project are welcome. Please ensure to update tests as appropriate.
