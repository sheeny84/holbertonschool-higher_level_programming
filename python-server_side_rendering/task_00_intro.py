import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        raise TypeError('template must be a string')
    if not isinstance(attendees, list):
        raise TypeError('attendees must be a list')
    for item in attendees:
        if not isinstance(item, dict):
            raise TypeError('attendees must be a list of dicts')
        
    # Handle empty inputs
    if len(template) == 0:
        raise ValueError('Template is empty, no output files generated.')
    if len(attendees) == 0:
        raise ValueError('No data provided, no output files generated')
    
    count = 0
    for attendee in attendees:
        for key, value in attendee.items():
            if value == None:
                template = template.replace('{' + key + '}', key+":N/A")
            else:
                template = template.replace('{' + key + '}', value)

        # Write to file
        count = count + 1
        file_path = "output_" + str(count) + ".txt"
        print(file_path)
        if os.path.exists(file_path):
            print(f"File {file_path} already exists")
        else:
            with open(file_path, 'w') as f:
                f.write(template)
    