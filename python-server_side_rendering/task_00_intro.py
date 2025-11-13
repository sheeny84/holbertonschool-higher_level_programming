import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print('template must be a string')
        return 0
    if not isinstance(attendees, list):
        print('attendees must be a list')
        return 0
    for item in attendees:
        if not isinstance(item, dict):
            print('attendees must be a list of dicts')
            return 0
        
    # Handle empty inputs
    if len(template) == 0:
        print('Template is empty, no output files generated.')
        return 0
    if len(attendees) == 0:
        print('No data provided, no output files generated')
        return 0
    
    count = 0
    template_orig = template
    for attendee in attendees:
        template = template_orig
        for key, value in attendee.items():
            if value == None:
                template = template.replace('{' + key + '}', key+":N/A")
            else:
                template = template.replace('{' + key + '}', value)

        # Write to file
        count = count + 1
        file_path = "output_" + str(count) + ".txt"
        if os.path.exists(file_path):
            print(f"File {file_path} already exists")
        else:
            with open(file_path, 'w') as f:
                f.write(template)
    
    return 1
    