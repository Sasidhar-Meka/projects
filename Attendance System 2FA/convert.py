import webbrowser

def open_excel_in_google_sheets(excel_file_path):
    # Generate the URL for opening the Excel file in Google Sheets
    url = f"https://docs.google.com/spreadsheets/importxlsx?upload=true&url=file://{excel_file_path}"

    # Open the URL in a web browser
    webbrowser.open(url)

# Example u
excel_file_path = '/home/sasi/Desktop/pro1/May-17-2023.xlsx'
open_excel_in_google_sheets(excel_file_path)




