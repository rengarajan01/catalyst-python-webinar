import csv
from collections import Counter, defaultdict
import json
from io import StringIO

class NewGraph:
    def __init__(self):
        pass
    def generate_graph(self, csv_file):
        # Read data from CSV
        data = []
        csvfile = StringIO(csv_file.read().decode('utf-8'))
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        # with open(csv_file, newline='') as csvfile:
        #     reader = csv.DictReader(csv_file)
        #     for row in reader:
        #         data.append(row)

        # Helper function to extract data
        def get_column(data, column_name):
            return [row[column_name] for row in data]

        # Lead Source Distribution
        lead_sources = get_column(data, 'Lead Source')
        lead_source_counts = Counter(lead_sources)
        lead_source_distribution = dict(lead_source_counts)

        # Company Representation
        companies = get_column(data, 'Company')
        company_counts = Counter(companies).most_common(10)
        top_companies = dict(company_counts)

        # Email Domain Analysis
        emails = get_column(data, 'Email')
        email_domains = [email.split('@')[1] for email in emails]
        email_domain_counts = Counter(email_domains).most_common(10)
        top_email_domains = dict(email_domain_counts)

        # Lead Source per Company for Top Companies
        top_companies_list = [company for company, count in company_counts]
        company_lead_sources = defaultdict(lambda: Counter())
        for row in data:
            if row['Company'] in top_companies_list:
                company_lead_sources[row['Company']][row['Lead Source']] += 1

        lead_source_per_company = {
            company: dict(sources) for company, sources in company_lead_sources.items()
        }

        # Distribution of Contacts per Company
        contacts_per_company = list(company_counts)

        # Prepare data for front-end
        output_data = {
            "lead_source_distribution": lead_source_distribution,
            "top_companies": top_companies,
            "top_email_domains": top_email_domains,
            "lead_source_per_company": lead_source_per_company,
            "contacts_per_company": contacts_per_company
        }

        return output_data

        # Save the data to a JSON file
        # with open('output_data.json', 'w') as jsonfile:
        #     json.dump(output_data, jsonfile, indent=4)

        # print("Data has been extracted and saved to 'output_data.json'.")
