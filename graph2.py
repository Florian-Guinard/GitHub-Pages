from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from matplotlib.pyplot import xlabel
import pandas as pd
from bokeh.models.widgets import Tabs, Panel
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.embed import autoload_static


donnees = pd.read_csv("all_stocks_5yr.csv")
df_apple = donnees.loc[donnees.Name=='AAPL'].copy()

df_apple['date'] = pd.to_datetime(df_apple['date'])
print(df_apple)
donnees = ColumnDataSource(df_apple)


#Création des figures
p1 = figure(title = "Valeur de fermeture en fonction de la valeur d'ouverture d'APPLE",
    x_axis_label= "Valeur d'ouverture", y_axis_label="Valeur de cloture")
p1.diamond(x = 'open',y = 'close',source = donnees,color='red')

outilsurvol1 = HoverTool(
    tooltips=[( 'Ouverture','@open'),( 'Fermeture', '@close' ),("Date","@date{%F}")],
    formatters={
        '@date' : 'datetime'})

p1.add_tools(outilsurvol1)

p2 = figure(title = "Valeur de fermeture en fonction de la valeur d'ouverture d'APPLE",
    x_axis_label= "Valeur minimale", y_axis_label="Valeur maximale")
    
p2.diamond(x = 'low',y = 'high',source = donnees,color='red')

outilsurvol2 = HoverTool(
    tooltips=[( 'Min','@low'),( 'Maw', '@high' ),("Date","@date{%F}")],
    formatters={
        '@date' : 'datetime'})

p2.add_tools(outilsurvol1)

tab1 = Panel(child=p1, title="Ouverture vs Fermeture")
tab2 = Panel(child=p2, title="Min vs Max")
tabs = Tabs(tabs = [tab1, tab2])

show(tabs)


js, tag = autoload_static(p1, CDN, "'C:\\Users\\Florian\\Documents\\Universite\\M1\\S2\\mongodb\\GitHub-Pages\\js1.html'")
print(js)
print(tag)
print("\n")
js2, tag2 = autoload_static(tabs, CDN, "'C:\\Users\\Florian\\Documents\\Universite\\M1\\S2\\mongodb\\GitHub-Pages\\js2.html'")
print(js2)
print(tag2)