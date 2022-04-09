
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.models import ColorPicker, Spinner, RangeSlider,CustomJS
from bokeh.layouts import row, column


#Données de base
x = [1,2,3,4,5,6]
y = [15,16,15,15,17,18]

data = ColumnDataSource(data = {'x':x,'y':y})

#Construction du graphe
plt = figure(title = "Application avec des couleurs",y_range=(12, 20))

points = plt.circle(x='x',y='y', source =data,fill_color='yellow',line_color='red',size = 15, fill_alpha = 0.5)

#Création des widgets

picker1 = ColorPicker(title="Couleur de ligne",color=points.glyph.line_color)
picker1.js_link('color', points.glyph, 'line_color')

picker2 = ColorPicker(title="Couleur de remplissage",color=points.glyph.fill_color)
picker2.js_link('color', points.glyph, 'fill_color')

spinner1 = Spinner(title="Taille des cercles", low=0,high=60, step=5, value=points.glyph.size) 
#Lier le spinner pour que cela modifie la taille des cercle
spinner1.js_link("value", points.glyph, "size") #Relier l'attribut value du spinner au glyphe points, en modifiant la propriété size. 


spinner2 = Spinner(title="Transparence", low=0,high=1, step=0.1, value=points.glyph.fill_alpha) 
spinner2.js_link("value", points.glyph, "fill_alpha") 

range_slider = RangeSlider(start=0, end=20, value=(plt.y_range.start,plt.y_range.end), step=1, title="Borne de l'axe des ordonnées")
range_slider.js_link("value",plt.y_range,"start",attr_selector=0)
range_slider.js_link("value",plt.y_range,"end",attr_selector=1)
#Construction du layout

layout = row(plt, column (picker1, spinner1,picker2,spinner2,range_slider))
show(layout)