from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Draw the cat plot and save it
cat_plot = draw_cat_plot()
cat_plot.savefig('catplot.png')

# Draw the heat map and save it
heat_map = draw_heat_map()
heat_map.savefig('heatmap.png')
