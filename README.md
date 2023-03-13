# ARBY

ARBY is an Arbitrage Calculator for League of Legends esports competitions.
It evaluates the odds from multiple operators and gives the best possible combinations for guaranteed profit.

How is arbitrage calculated?
(1 / ODDS_A + 1 / ODDS_B) * 100

If the arbitrage equation is lower than 100%, profit is guaranteed.


# RUN
```
pip install -r requirements.txt
python main.py
```