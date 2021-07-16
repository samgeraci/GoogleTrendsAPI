# GoogleTrendsAPI
Proof of concept for google trends API use at Golden Oak Capital LLC

Changing the search_term variable changes the Google Trends search term being looked up. (default value 'Apple Stock')
Changing n changes the zoom level of the local minima and maxima identification with a lower n being more coarse and a higher n being more fine. (default value n = 20)

Program computes local minima and maxima of data received from Google Trends API. It plots data with minima highlighted in red and maxima highlighted in green. Finally, it displays the graph and prints the local minima and maxima with the dates when the occur.
