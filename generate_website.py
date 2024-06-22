import os
import csv

# Read policies from CSV file
def read_policies_from_csv():
    policies = []
    with open('policies.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Ensure row is not empty
                policies.append(row[0])
    return policies

policies = read_policies_from_csv()

# Convert the list to a JavaScript array format
policies_js_array = ', '.join(f'"{policy}"' for policy in policies)

# Reading the file
file_path = 'websites_queue.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse the file and store the data
entries = []
for line in lines:
    line = line.strip()
    parts = line.split(', ')
    
    if len(parts) == 3:
        area, party, url = parts
    elif len(parts) == 4:
        area = f"{parts[0]}, {parts[1]}"
        party = parts[2]
        url = parts[3]
    entries.append((area, party, url))

# Sort entries alphabetically by area
entries.sort(key=lambda x: x[0])

def generate_javascript():
    # JavaScript content
    js_content = f"""
document.addEventListener("DOMContentLoaded", function() {{
    const policies = [{policies_js_array}];
    const policyTextElement = document.getElementById("policy-text");
    const newPolicyButton = document.getElementById("new-policy-button");

    function setRandomPolicy() {{
        const randomPolicy = policies[Math.floor(Math.random() * policies.length)];
        policyTextElement.textContent = randomPolicy;
    }}

    newPolicyButton.addEventListener("click", setRandomPolicy);

    // Set initial random policy
    setRandomPolicy();
}});
"""
    # Write to JS file
    with open('website/script.js', 'w') as file:
        file.write(js_content)

def generate_style():
    # CSS content
    css_content = '''
body {
    font-family: 'Quicksand', sans-serif;
    margin: 0;
    padding: 20px;
    line-height: 1.6;
    background-color: #f4f4f4;
}

h1 {
    font-size: 2.5em;
    color: #333;
}

.policy {
    width: 100%;
    margin: 20px 0;
    padding: 20px;
    border: 1px solid #ddd;
    background-color: #f9f9f9;
    position: -webkit-sticky; /* Safari */
    position: sticky;
    top: 0;
    z-index: 1000;
    background-color: #fff;
}

.policy p {
    font-size: 1.5em;
    line-height: 1.4;
}

.full-width-text {
    font-size: 2em;
    font-weight: bold;
    text-align: center;
}

.discord-link {
    display: block;
    margin-top: 10px;
}

.area-list {
    margin-bottom: 20px;
}

.area-list a {
    text-decoration: none;
    margin-right: 10px;
    color: #007BFF;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
}

h3 {
    margin-top: 20px;
}

.fixed-width {
    width: 150px;
}
'''
    # Write to CSS file
    with open('website/styles.css', 'w') as file:
        file.write(css_content)

def generate_html():
    # Creating the HTML content
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Party Websites</title>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <h1>JOIN THE INDEPENDENCE DAY PARTY - VOTE - CELEBRATE</h1>
    <p>Welcome to the Independence Day Party's website directory. Below you will find links to various political party websites across different constituencies.</p>
    <div class="policy">
        <p><strong>Do you agree with this policy?</strong></p>
        <p id="policy-text" class="full-width-text"></p>
        <button id="new-policy-button">Show Another Policy</button>
        <a class="discord-link" href="https://discord.gg/your-discord-link" target="_blank">Continue the conversation on Discord</a>
    </div>
    <div class="area-list">
        <!-- Area links will be dynamically inserted here -->
    </div>
    <!-- Area tables will be dynamically inserted here -->
</body>
</html>
'''
    # Add the list of areas with anchor links
    areas = sorted(set(entry[0] for entry in entries))
    area_links = ''.join(f'<a href="#{area.lower().replace(" ", "_")}">{area}</a>\n' for area in areas)
    
    # Insert area links into the HTML content
    html_content = html_content.replace('<!-- Area links will be dynamically inserted here -->', area_links)
    
    # Add the tables for each area
    area_tables = ''
    current_area = None
    for area, party, url in entries:
        anchor_name = area.lower().replace(' ', '_')
        
        # Adding area as h3 if it's a new area
        if area != current_area:
            if current_area is not None:
                area_tables += '</table>\n'
            current_area = area
            area_tables += f'<h3 id="{anchor_name}">{area}</h3>\n<table>\n<tr><th class="fixed-width">Party</th><th>Website</th></tr>'

        # Adding party and URL in a table row
        area_tables += f'<tr><td class="fixed-width">{party}</td><td><a href="{url}" target="_blank">{url}</a></td></tr>\n'

    area_tables += '</table>\n'
    html_content = html_content.replace('<!-- Area tables will be dynamically inserted here -->', area_tables)
    
    # Write to HTML file
    os.makedirs('website', exist_ok=True)
    output_file = 'website/index.html'
    with open(output_file, 'w') as file:
        file.write(html_content)

def generate_all():
    generate_javascript()
    generate_style()
    generate_html()
    print("All files have been generated.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "javascript":
            generate_javascript()
        elif command == "style":
            generate_style()
        elif command == "html":
            generate_html()
        else:
            print("Unknown command. Use 'javascript', 'style', or 'html'.")
    else:
        generate_all()
