Environment:
- Window 10, intel core i5-7200U ram 8Gb, HDD 1T
- Python version:: 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]
- Pandas version:: 0.25.1

Prepare:
- email_template.json: an email template that have some placeholders like {{TITLE}}, {{FIRST_NAME}}, {{LAST_NAME}} that need to be filled with customer information.
- customers.csv: csv file that store customer information 

How to run: <br>
python send_email.py "path to template.json" "path to customer.csv" "path to output email" "path to error.csv"
Example: <br>
python send_email.py email_template.json customers.csv output_emails/ error.csv.


Output:
- User without email will be store in error.csv (same format with customers.csv).
- Combine of customers.csv and email_template.json will be store at output_emails folder.
