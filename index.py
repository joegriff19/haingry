# Import Packages and other files for app
from app import app, server #NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import random
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import date
today = date.today()

# padding for the page content
CONTENT_STYLE = {
   "margin-left": "2rem",
   "margin-right": "2rem",
   "padding": "2rem 1rem",
}

# Index Page Layout
colors = {
    'background': '#ffffff',
    'text': '#0000CD'
}

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# define sidebar layout
app.layout = html.Div([
   dcc.Location(id="url"),
   content
])

# index page layout
index_layout = html.Div(
    children=[
            html.Header(
                children=[
                    html.Br(),
                    html.Div(children="🤤", style={"fontSize": "85px"}),
                    html.Div(children="the hangry app", style={"fontSize": "75px"}),
                    html.Div(children="powered by JI (Joe's Intelligence)", style={"fontSize": "30px"}),
                    html.Br(),
                ],
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'background': colors['background']
                }
            ),
            html.Div(children="Let's decide what to eat so you dont get hangry!"),
            html.Br(),
            html.Div([
                    "First question: how hangry are you at the moment?",
                    dcc.Dropdown(['A little bit', 'Very', "I might rip someone's head off"],
                    id='dropdown')]),
            html.Br(),
            html.Div(id='question-response'),
            html.Br(),
            html.Div(id='question-response2'),
            html.Div(),
            html.Div(id='question-response3'),
            html.Div(),
            html.Div(id='question-response4'),

    ], style={'textAlign': 'center',
              # 'width': '50%',
              # 'align-items': 'center', 'justify-content': 'center'
              }
)


# CREATE LISTS
american = ['Farm Bar', 'SALT burger', 'Park and Field', 'Au Cheval', 'Small Cheval','Lakefront Restaurant Theatre',
            'Gemini', 'Hutch', 'LuxBar', 'Gilt Bar', 'Rocks', 'The Whale', "Twin Anchor's", 'Kirkwood']
asian = ['Sushi san', 'Jinsei Motto', 'Cho Sun Ok', "Penny's", "Andy's Thai", 'Silver Spoon Thai', 'Gorilla Sushi',
         'Tac Quick', 'Happy Lamb Hot Pot']
bagel = ['Taste of New York', 'Gotham', 'Chicago Bagel Authority', 'The Bagelers']
chicken = ["GG's", "Parson's", "Cane's", "Harold's", 'Honey Butter Fried Chicken']
italian = ['Topo Gigio', 'Gioia Ristorante', 'Alla Vita', 'Lardon', 'Mia Francesca', 'Forno Rosso', 'Little Italy',
           'Eataly', 'Frasca', "Sal's"]
latino = ['Los 3 Panchos', 'Broken English', 'La Bendición Tamales', 'Bocadillo Market', 'Ba Ba Reeba', 'Bien Me Sabe',
          'Barrio', 'Los Comales', 'La Vaca', 'Tanta', 'Barcocina', 'Broken English', 'Boquería', 'Cruz Blanca',
          'Jibaritos', 'El Nuevo Mexicano', 'Tango Sur / Bodega Sur', 'Tuco and Blondie', 'Old Pueblo Cantina',
          'Pilsen Yards', 'Rica Arepa', "Mima's Taste of Cuba", 'Salsa Picante (Birria)',
          'Las Tablas', '90 Miles Cuban', 'S & T Steak & Tostada']
pizza = ['Art of Pizza', 'Dry Hop', "Robert's Pizza", 'Piccolo Sogno', 'Homeslice', "Ranalli's", 'Bonci',
         "Lou Malnati's", "Vito & Nick's", "Giordano's"]
salad = ['Sweetgreen', 'Doms']
sandwich = ['BARI', "D'amato's", 'Alpine', "Johnnie's", 'Potbelly', "JJ's"]
something = ['Avli', 'Athenian Room', "Andro's Taverna", 'Smoke Daddy', 'District Brew Yards', "AJ's", 'Poke Poke',
             'Pleasant House Pub', "Cleo's", 'Prost', 'The Globe', 'Four Moon Tavern', 'Sheffield', 'Galway Arms',
             'Demera', 'Tesfa', "Dom's", 'Bodega Sur', 'Tango Sur', 'Aba']
idk = american + asian + bagel + chicken + italian + latino + pizza + salad + sandwich + something


# page callback
@app.callback(
    Output('page-content', 'children',),
    [Input('url', 'pathname',)]
)
def render_page_content(pathname):
    if pathname == '/':
        return index_layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
       [
           html.H1("404: Not found", className="text-danger"),
           html.Hr(),
           html.P(f"The pathname {pathname} was not recognised..."),
       ]
    )


# dropdown callback
@app.callback(
    Output('question-response', 'children'),
    Input('dropdown', 'value')
)
def update_output(value):
    if value == 'A little bit':
        return 'Bueno! ', 'What kind of food do you want?', dcc.Dropdown(['American', 'Asian', 'Bagel', 'Chicken', 'Italian', 'Mexican / Spanish / Latino', 'Pizza', 'Salad', 'Sandwich', 'Something Fun and Different', 'I dont know'], id='dropdown2')
    if value == 'Very':
        return 'Ok! ', 'What kind of food do you want?', dcc.Dropdown(['American', 'Asian', 'Bagel', 'Chicken', 'Italian', 'Mexican / Spanish / Latino', 'Pizza', 'Salad', 'Sandwich', 'Something Fun and Different', 'I dont know'], id='dropdown2')
    if value == "I might rip someone's head off":
        return 'Scheiße! ', 'What kind of food do you want?', dcc.Dropdown(['American', 'Asian', 'Bagel', 'Chicken', 'Italian', 'Mexican / Spanish / Latino', 'Pizza', 'Salad', 'Sandwich', 'Something Fun and Different', 'I dont know'], id='dropdown2')

# # dropdown2 callback
# @app.callback(
#     Output('question-response2', 'children'),
#     Input('dropdown2', 'value')
# )
# def update_output(value):
#     if value is not None:
#         return 'How do you want to get your food?', dcc.Dropdown(['I need food delivered', 'I can pick up food', 'I want to eat out'], id='dropdown3')

# dropdown2 callback
@app.callback(
    Output('question-response2', 'children'),
    Input('dropdown2', 'value')
)
def update_output(value):
    if value == 'American':
        return 'The solution to your hanger is: ', random.choice(american), '!'
    if value == 'Asian':
        return 'The solution to your hanger is: ', random.choice(asian), '!'
    if value == 'Bagel':
        return 'The solution to your hanger is: ', random.choice(bagel), '!'
    if value == 'Chicken':
        return 'The solution to your hanger is: ', random.choice(chicken), '!'
    if value == 'Italian':
        return 'The solution to your hanger is: ', random.choice(italian), '!'
    if value == 'Mexican / Spanish / Latino':
        return 'The solution to your hanger is: ', random.choice(latino), '!'
    if value == 'Pizza':
        return 'The solution to your hanger is: ', random.choice(italian), '!'
    if value == 'Salad':
        return 'The solution to your hanger is: ', random.choice(salad), '!'
    if value == 'Sandwich':
        return 'The solution to your hanger is: ', random.choice(sandwich), '!'
    if value == 'Something Fun and Different':
        return 'The solution to your hanger is: ', random.choice(something), '!'
    if value == 'I dont know':
        return 'The solution to your hanger is: ', random.choice(idk), '!'
