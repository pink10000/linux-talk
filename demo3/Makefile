CXX = g++
CXXFLAGS = -Wall -lpthread -Wno-unused-variable -fno-omit-frame-pointer
LDFLAGS = -lpthread 

all: backtest1 backtest2

backtest1: backtest1.cpp
	$(CXX) $(CXXFLAGS) -o $@ $< $(LDFLAGS)

backtest2: backtest2.cpp
	$(CXX) $(CXXFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f backtest1 backtest2