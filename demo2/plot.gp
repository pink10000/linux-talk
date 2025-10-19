# Gnuplot script to plot PnL data from a pipe to a PNG file

# --- Output Configuration ---
# Set the output format to a high-quality PNG with a larger size
set terminal pngcairo enhanced font "Verdana,10" size 1280,720

# Set the name of the output file.
set output '/data/pnl_plot.png'

# --- Data & Plot Configuration ---
set datafile separator ','
set key autotitle columnheader
set xdata time
set timefmt '%Y-%m-%d'
set title 'TQT Strategy Backtest'
set xlabel 'Date'
set ylabel 'Cumulative PnL'

# --- Plotting Command ---
# Plot data from standard input ('<cat')
plot '<cat' using 1:2 with lines