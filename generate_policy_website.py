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

#header {
  text-align: center;
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

#policy-text {
  font-size: 3em;
}

.discord-link {
    display: block;
    margin-top: 10px;
}

#new-policy-button {
  margin-top: 30px;
  font-size: 2em;
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
    <title>Policy Selector</title>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div id="header">
        <h1>JOIN THE PARTY - CELEBRATE</h1>
        <div>
            Things can only get better. But which things do you want to see better?
        </div>
    </div>
    <div class="policy">
        <p id="policy-text" class="full-width-text"></p>
        <p id="more" class="full-width-text">
            <a class="discord-link" href="https://discord.com/invite/vqME6WsPd7" target="_blank">Do you agree with this policy? Continue the conversation on Discord</a>
            <button id="new-policy-button">Show Another Policy</button>
        </p>
    </div>
</body>
</html>
'''
    # Write to HTML file
    os.makedirs('website', exist_ok=True)
    output_file = 'website/policies.html'
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
