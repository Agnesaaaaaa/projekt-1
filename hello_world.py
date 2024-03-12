import streamlit as st
import pandas as pd

formatted_text = st.markdown('<h1 style="color: pink; border-bottom: 2px solid lightpink;">ExploreXperience</h1>', unsafe_allow_html=True)

st.write('<span style="color: darkpink;">2.Semester Informatik</span>', unsafe_allow_html=True)

import streamlit as st
import pydeck as pdk


view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1)
r = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=view_state,
    layers=[],
)

st.pydeck_chart(r)


st.markdown('**Gereiste Länder:**')
st.markdown('- ' + '\n- '.join(['Land 1 ', 'Land 2 ', 'Land 3 ']))

st.markdown('**Noch zu erkundigen:**')
st.markdown('1. ' + '\n1. '.join(['Land 1 ', 'Land 2 ', 'Land 3']))

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)


# Checkbox Beispiel
option1 = st.checkbox('Ja')
option2 = st.checkbox('Nein')

# Color Picker Beispiel
color = st.color_picker('Wähle eine Farbe', '#FFC0CB')

# Date Input Beispiel
date = st.date_input('Wähle ein Datum')

# File Uploader Beispiel
uploaded_file = st.file_uploader('Lade eine CSV-Datei hoch', type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

button_clicked = st.button('Reise mit mir!')


import streamlit as st

user_input = st.text_input('Gib dein lieblingsland ein:', 'Hier Text eingeben...')
st.write('Eingegebener Text:', user_input)

import streamlit as st

# Sidebar-Titel in Pink darstellen
st.sidebar.markdown('<h1 style="color: pink;">Kontinente</h1>', unsafe_allow_html=True)

# Radiobuttons in Pink darstellen
selection = st.sidebar.radio(
    label='Gehe zu:',
    options=['Startseite', 'Europa', 'Afrika', 'Nordamerika', 'Südamerika', 'Antarktika']
)

# Länderdaten laden (Beispiel: Liste der Länder und ihrer Hauptstädte)
data = {
    'Land': ['USA', 'Kanada', 'Deutschland', 'Frankreich'],
    'Hauptstadt': ['Washington, D.C.', 'Ottawa', 'Berlin', 'Paris']
}

# Daten in ein DataFrame konvertieren
df = pd.DataFrame(data)

# Tabelle in Streamlit anzeigen
st.write(df)



import streamlit as st
import pandas as pd
import plotly.express as px

# Beispiel-Daten: Liste der besuchten Länder und deren Kontinent
data = {
    'Land': ['USA', 'Kanada', 'Deutschland', 'Frankreich', 'Brasilien', 'Japan', 'Australien'],
    'Kontinent': ['Nordamerika', 'Nordamerika', 'Europa', 'Europa', 'Südamerika', 'Asien', 'Australien']
}

# Daten in ein DataFrame konvertieren
df = pd.DataFrame(data)

# Anzahl der besuchten Länder pro Kontinent zählen
country_counts = df['Kontinent'].value_counts().reset_index()
country_counts.columns = ['Kontinent', 'Anzahl der besuchten Länder']

# Balkendiagramm mit pinker Farbe erstellen
fig = px.bar(country_counts, x='Kontinent', y='Anzahl der besuchten Länder', 
             title='Anzahl der besuchten Länder pro Kontinent', 
             labels={'Kontinent': 'Kontinent', 'Anzahl der besuchten Länder': 'Anzahl der Länder'},
             color_discrete_sequence=['pink'])

# Balkendiagramm in Streamlit anzeigen
st.plotly_chart(fig)


import streamlit as st

# Checkbox für Reiseziel
travel_checkbox = st.checkbox('Ich plane eine Reise')

# Ausgabe basierend auf Checkbox-Status
if travel_checkbox:
    st.write('Wo geht Ihre nächste Reise hin?')
else:
    st.write('Viel Spaß bei Ihren zukünftigen Reiseplänen!')



import streamlit as st
import pandas as pd
import random

# Beispiel-Daten für Reiseziele und Aktivitäten
destinations = pd.DataFrame({
    'Reiseziel': ['Paris', 'Tokyo', 'New York', 'Rom', 'Sydney'],
    'Kontinent': ['Europa', 'Asien', 'Nordamerika', 'Europa', 'Australien'],
    'Aktivität': ['Kultur', 'Essen', 'Shopping', 'Geschichte', 'Abenteuer']
})

# Funktion zum Filtern von Reisezielen basierend auf Aktivitäten
def filter_destinations(selected_activities):
    filtered_destinations = destinations
    for activity in selected_activities:
        filtered_destinations = filtered_destinations[filtered_destinations['Aktivität'] == activity]
    return filtered_destinations['Reiseziel'].tolist()

# Hauptfunktion der Anwendung
def main():
    st.title('Traumurlaub planen')
    
    # Auswahl der Aktivitäten
    selected_activities = st.multiselect('Wählen Sie Ihre bevorzugten Aktivitäten:', destinations['Aktivität'].unique())

    # Filtern von Reisezielen basierend auf ausgewählten Aktivitäten
    filtered_destinations = filter_destinations(selected_activities)

    # Anzeigen der vorgeschlagenen Reiseziele
    if filtered_destinations:
        st.subheader('Vorgeschlagene Reiseziele:')
        for destination in filtered_destinations:
            st.write(destination)
    else:
        st.write('Keine Reiseziele gefunden. Bitte wählen Sie andere Aktivitäten.')

# Anwendung ausführen
if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
import pydeck as pdk

# Beispiel-Daten für Reiseziele
data = pd.DataFrame({
    'Reiseziel': ['Hawaii', 'Bali', 'Paris', 'Tokyo'],
    'Breitengrad': [40.7128, 34.0522, 48.8566, 35.6895],
    'Längengrad': [-74.0060, -118.2437, 2.3522, 139.6917]
})

# Funktion zum Anzeigen der interaktiven Karte
def show_map(data):
    view_state = pdk.ViewState(latitude=data['Breitengrad'].mean(), longitude=data['Längengrad'].mean(), zoom=1)
    layer = pdk.Layer('ScatterplotLayer', data=data, get_position='[Längengrad, Breitengrad]', get_radius=100000, get_color=[255, 0, 0], pickable=True)
    tool_tip = {'html': 'Reiseziel: {Reiseziel}'}
    deck = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9', initial_view_state=view_state, layers=[layer], tooltip=tool_tip)
    st.pydeck_chart(deck)

# Hauptfunktion der Anwendung
def main():
    st.title('Meine Lieblingsreiseziele')

    # Anzeigen der interaktiven Karte
    show_map(data)

# Anwendung ausführen
if __name__ == '__main__':
    main()

# Hauptfunktion der Anwendung
def main():
    # Anzeigen von Text und Foto aus dem Internet
    st.write('Willkommen zu meiner Reiseinspirationsseite!')
    st.image('file:///Users/agnesalekaj/Desktop/urlaub-arbeit.jpg', caption='Bildbeschreibung', use_column_width=True)

# Anwendung ausführen
if __name__ == '__main__':
    main()

# Hauptfunktion der Anwendung
def main():
    st.title('Besondere Orte auf der Welt')

    # Beispiel-Bilder und Zusatzinformationen
    images_info = {
        'Eiffelturm': ('eiffel_tower.jpg', 'Der Eiffelturm ist ein Wahrzeichen von Paris, Frankreich.'),
        'Mount Everest': ('mount_everest.jpg', 'Der Mount Everest ist der höchste Berg der Welt und liegt im Himalaya.'),
        'Great Barrier Reef': ('great_barrier_reef.jpg', 'Das Great Barrier Reef ist das größte Korallenriffsystem der Welt vor der Küste von Queensland, Australien.')
    }

    # Benutzerauswahl für besondere Orte
    selected_place = st.selectbox('Wählen Sie einen besonderen Ort:', list(images_info.keys()))

    # Anzeigen des Modaldialogs, wenn der Benutzer auf die Schaltfläche klickt
    if st.button('Mehr erfahren'):
        show_modal(images_info[selected_place][0], images_info[selected_place][1])

# Anwendung ausführen
if __name__ == '__main__':
    main()





