import requests
from datetime import datetime
from typing import Dict, List, Any

def get_api_coverage(doc_type: str) -> Dict[str, Any]:
    """Get coverage data from A2AJ API."""
    url = f"https://api.a2aj.ca/coverage?doc_type={doc_type}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {doc_type} coverage: {e}")
        return {"results": []}

def format_date(date_str: str) -> str:
    """Format ISO date string to YYYY-MM-DD."""
    if date_str:
        try:
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return "N/A"
    return "N/A"

def generate_readme():
    """Generate README.md for the GitHub repository."""
    
    # Get coverage data from API
    cases_data = get_api_coverage("cases")
    laws_data = get_api_coverage("laws")
    
    # Dataset ordering for cases (matches original script)
    case_order = ["SCC", "FCA", "ONCA", "FC", "TCC", "CMAC", "SST", "RAD", "RPD", "RLLR", "CHRT"]
    
    # Dataset ordering for laws
    law_order = ["LEGISLATION-FED", "REGULATIONS-FED"]
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Process cases data
    cases_by_dataset = {item["dataset"]: item for item in cases_data.get("results", [])}
    case_table_rows = []
    total_cases = 0
    
    for dataset in case_order:
        if dataset in cases_by_dataset:
            item = cases_by_dataset[dataset]
            count = item["number_of_documents"]
            total_cases += count
            first_date = format_date(item["earliest_document_date"])
            last_date = format_date(item["latest_document_date"])
            description = item["description_en"]
            row = f"| {dataset:<6} | {description:<40} | {first_date} – {last_date} | {count:,} |"
            case_table_rows.append(row)
    
    # Process laws data
    laws_by_dataset = {item["dataset"]: item for item in laws_data.get("results", [])}
    law_table_rows = []
    total_laws = 0
    
    for dataset in law_order:
        if dataset in laws_by_dataset:
            item = laws_by_dataset[dataset]
            count = item["number_of_documents"]
            total_laws += count
            first_date = format_date(item["earliest_document_date"])
            last_date = format_date(item["latest_document_date"])
            description = item["description_en"]
            row = f"| {dataset:<15} | {description:<25} | {first_date} – {last_date} | {count:,} |"
            law_table_rows.append(row)
    
    # Generate README content
    readme_content = f"""# A2AJ Canadian Legal Data

Last updated: {today}

Maintainer: [Access to Algorithmic Justice (A2AJ)](https://a2aj.ca)

## Overview

This repository provides tools and documentation for accessing Canadian legal data through multiple opena access / open source channels. The A2AJ Canadian Legal Data project offers access to Canadian court/triunbal decisions, legislation, and regulations through various interfaces designed for different use cases.

## Data Access Methods

### 1. API Access
- **Best for**: Searching specific cases or laws, programmatic queries, real-time access
- **Endpoint**: https://api.a2aj.ca/
- **Documentation**: https://api.a2aj.ca/docs
- **Examples**: See `access-via-api.ipynb`

### 2. Hugging Face Datasets
- **Best for**: Machine learning, bulk analysis, academic research
- **Case Law Dataset**: https://huggingface.co/datasets/a2aj/canadian-case-law
- **Laws Dataset**: https://huggingface.co/datasets/a2aj/canadian-laws
- **Examples**: See `access-via-hugging-face.ipynb`

### 3. Direct Parquet Downloads
- **Best for**: Simple bulk downloads, minimal dependencies
- **Examples**: See `access-via-parquet.ipynb`

### 4. Model Context Protocol (MCP)
- **Best for**: AI agent integration, conversational interfaces
- **Server**: https://api.a2aj.ca/mcp
- **Examples**: See `access-via-mcp.ipynb`

## Dataset Coverage

### Court Decisions ({total_cases:,} cases)

| Code   | Court / Tribunal                         | Coverage Period            | Cases   |
|--------|------------------------------------------|----------------------------|---------|
"""

    for row in case_table_rows:
        readme_content += row + "\n"
    
    readme_content += f"""
### Federal Legislation & Regulations ({total_laws:,} documents)

| Code            | Type                      | Coverage Period            | Documents |
|-----------------|---------------------------|----------------------------|-----------|
"""

    for row in law_table_rows:
        readme_content += row + "\n"
    
    readme_content += """
> Note: Counts are approximate and will drift as datasets are updated.

## Data Fields

### Case Law
| Field | Type | Description |
|-------|------|-------------|
| dataset | string | Court/tribunal abbreviation |
| citation_en / citation_fr | string | Neutral citation |
| citation2_en / citation2_fr | string | Secondary citations |
| name_en / name_fr | string | Case name/style of cause |
| document_date_en / document_date_fr | datetime | Decision date |
| url_en / url_fr | string | Source URL |
| scraped_timestamp_en / scraped_timestamp_fr | datetime | Scraping timestamp |
| unofficial_text_en / unofficial_text_fr | string | Full text |
| upstream_license | string | Source license terms |

### Legislation & Regulations
| Field | Type | Description |
|-------|------|-------------|
| dataset | string | LEGISLATION-FED or REGULATIONS-FED |
| citation_en / citation_fr | string | Official citation |
| name_en / name_fr | string | Full title |
| document_date_en / document_date_fr | datetime | Enactment/publication date |
| url_en / url_fr | string | Source URL |
| scraped_timestamp_en / scraped_timestamp_fr | datetime | Scraping timestamp |
| unofficial_text_en / unofficial_text_fr | string | Full text |
| upstream_license | string | Source license terms |

## Getting Started

1. **For API access**: Review `access-via-api.ipynb` for examples of searching and retrieving specific documents
2. **For bulk analysis**: Use `access-via-hugging-face.ipynb` or `access-via-parquet.ipynb` depending on your needs
3. **For AI integration**: See `access-via-mcp.ipynb` for connecting AI assistants to the legal data

## Data Quality & Limitations

- **Unofficial Copies**: All texts are unofficial; consult source URLs for authoritative versions
- **Coverage Gaps**: Gaps exist for some courts/tribunals; not all decisions are published on court/tribunal websites
- **Processing**: Automated scraping may introduce formatting artifacts
- **Updates**: Data is updated regularly but not in real-time

## Privacy & Ethical Considerations

Court decisions contain sensitive personal information. While all documents are public, bulk access increases privacy risks, particularly for marginalized communities. Users should:

- Comply with applicable privacy laws
- Respect publication bans and court orders
- Consider community impact when developing derivative tools
- Collaborate with community and legal aid organizations where appropriate

## Warranties / Representations

While we make best efforts to ensure the completeness and accuracy of our datasets, we provide no warranties regarding completeness or accuracy. The data were collected through automated processes and may contain errors. Always verify documents against the official source.

## Licensing Information

The code used to create the dataset by the A2AJ and any work on the dataset undertaken by the A2AJ is subject to an open source **MIT license**. 

Users must also comply with upstream licenses found in the `upstream_license` field in the dataset for each document, which reflects the licenses through which the A2AJ obtained the document. These upstream licenses may include limits on commercial use, as well as other limitations. 

The A2AJ is committed to open source methodologies, and we are actively working to obtain more permissive licenses for all data we collect.


## Dataset Curators

* [**Sean Rehaag**](https://www.osgoode.yorku.ca/faculty-and-staff/rehaag-sean) - Co-Director, A2AJ
* [**Simon Wallace**](https://www.torontomu.ca/law/faculty-and-research/faculty/faculty-law/simon-wallace) - Co-Director, A2AJ
* **Contact:** [a2aj@yorku.ca](a2aj@yorku.ca)

---

## Acknowledgments

This research output is supported in part by funding from the **Law Foundation of Ontario** and the **Social Sciences and Humanities Research Council of Canada**, by in-kind compute from the **Digital Research Alliance of Canada** and by administrative support from the **Centre for Refugee Studies**, the **Refugee Law Lab**, and **Osgoode Hall Law School**. We also thank Justice Canada for maintaining the open XML repository of federal laws and regulations.

## Citation

> Sean Rehaag & Simon Wallace, "A2AJ Canadian Legal Data" (2025), online: GitHub [https://github.com/a2aj-ca/canadian-legal-data](https://github.com/a2aj-ca/canadian-legal-data).
"""
    
    # Write README file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"README.md generated successfully!")
    print(f"Total cases: {total_cases:,}")
    print(f"Total laws/regulations: {total_laws:,}")
    print(f"Total documents: {total_cases + total_laws:,}")

if __name__ == "__main__":
    generate_readme()