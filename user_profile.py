import streamlit as st

form = st.form("my_form")

form.header("Welcome to MatchUP")
form.caption("We want to know all about you!")
firstname = form.text_input("First Name")
lastname = form.text_input("Last Name")

pronouns_list = ['she/her', 'he/him', 'they/them', 'she/they', 'he/they', ]

pronouns = form.multiselect("Pronouns", pronouns_list)
photo = form.file_uploader("Profile photo", type=['png', 'jpg', 'jpeg', 'img', 'heic', 'hevc', 'tiff', 'tif', 'raw', 'webp', 'svp'])
age = form.number_input("Age", min_value=16, max_value=100, value=None)

form.write("I am looking for")
form.checkbox("Advice/Mentorship")
form.checkbox("Share my knowledge")
form.checkbox("Network")

industry_options = ['Aerospace', 'Agriculture', 'Automotive', 'Business', 'Banking', 'Biotechnology', 
                    'Chemicals', 'Construction', 'Consulting', 'Consumer Goods', 'Cybersecurity', 'Defense', 
                    'Education', 'Energy', 'Entertainment', 'Environmental Services', 
                    'Fashion', 'Finance', 'Food and Beverage', 'Government', 'Healthcare', 
                    'Hospitality', 'Information Technology', 'Insurance', 'Logistics', 
                    'Manufacturing', 'Media', 'Mining', 'Nonprofit', 'Pharmaceuticals', 
                    'Private Equity', 'Professional Services', 'Real Estate', 'Retail', 
                    'Technology', 'Telecommunications', 'Tourism', 'Transportation', 'Utilities', 
                    'Venture Capital', 'Waste Management', 'Wholesale']

industry = form.multiselect("Industry", industry_options)
occupation = form.text_input("Current occupation")
company = form.text_input("Company/School")
bio = form.text_area("Tell us about yourself!")

interests_list = ['Reading', 'Traveling', 'Cooking', 'Gardening', 'Photography', 'Music', 
                  'Sports', 'Hiking', 'Art', 'Writing', 'Fitness', 'Technology', 'Video Games', 
                  'Dancing', 'Fishing', 'Crafting', 'Fashion', 'Theater', 'Volunteering', 'Yoga', 
                  'Birdwatching', 'Knitting', 'Painting', 'Cooking', 'Camping', 'Swimming', 
                  'Cycling', 'Running', 'Podcasting', 'Martial Arts', 'Sculpting', 'Surfing', 
                  'Travel Blogging', 'Astronomy', 'Collecting', 'Board Games', 'Wine Tasting', 
                  'Journaling', 'Mindfulness', 'Homebrewing', 'Rock Climbing', 'Pottery', 
                  'Graphic Design', 'Interior Design', 'History', 'Languages', 'Animal Care', 
                  'Motorsports', 'Sailing', 'Scuba Diving', 'Calligraphy', 'Stand-up Comedy']
interests = form.multiselect("Interests", interests_list)

form.form_submit_button("Submit")
