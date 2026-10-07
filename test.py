from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

res=run_travel_agent("Plan a 7 days Japan trip from bangalore")
print(res)