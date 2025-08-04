# A2AJ Canadian Legal Data

Last updated: 2025-08-04

Maintainer: [Access to Algorithmic Justice (A2AJ)](https://a2aj.ca)

## Overview

This repository provides tools and documentation for accessing Canadian legal data through multiple open access / open source 
channels. The project builds on an earlier [version](https://huggingface.co/datasets/refugee-law-lab/canadian-legal-data) that 
was maintained by the [Refugee Law Lab (RLL)](https://refugeelab.ca/) and is now maintained by [A2AJ](https://a2aj.ca/), a 
research project co-hosted by York University's Osgoode Hall Law School and Toronto Metropolitan University's Lincoln Alexander 
School of Law. The data is intended to support empirical legal research, legal-tech prototyping, and language-model 
pre-training in the public interest—especially work that advances access to justice for marginalised and low-income communities.

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

### Court Decisions (116,734 cases)

| Code   | Court / Tribunal                         | Coverage Period            | Cases   |
|--------|------------------------------------------|----------------------------|---------|
| SCC    | Supreme Court of Canada                  | 1877-01-15 – 2025-07-31 | 10,845 |
| FCA    | Federal Court of Appeal                  | 2001-02-01 – 2025-08-01 | 7,580 |
| ONCA   | Ontario Court of Appeal                  | 2007-01-02 – 2025-08-01 | 16,951 |
| FC     | Federal Court                            | 2001-02-01 – 2025-08-01 | 34,256 |
| TCC    | Tax Court of Canada                      | 2003-01-21 – 2025-07-30 | 7,918 |
| CMAC   | Court Martial Appeal Court               | 2001-01-19 – 2025-06-17 | 147 |
| SST    | Social Security Tribunal                 | 2013-03-08 – 2025-12-16 | 16,338 |
| RAD    | Refugee Appeal Division (IRB)            | 2013-02-19 – 2024-07-22 | 14,022 |
| RPD    | Refugee Protection Division (IRB)        | 2002-07-16 – 2020-12-14 | 6,729 |
| RLLR   | Refugee Law Lab Reporter (RPD, IRB)      | 2019-01-07 – 2023-12-29 | 898 |
| CHRT   | Canadian Human Rights Tribunal           | 2003-01-10 – 2025-07-16 | 1,050 |

### Federal Legislation & Regulations (5,757 documents)

| Code            | Type                      | Coverage Period            | Documents |
|-----------------|---------------------------|----------------------------|-----------|
| LEGISLATION-FED | Federal Statutes          | 1870-05-12 – 2025-06-26 | 954 |
| REGULATIONS-FED | Federal Regulations       | 1945-12-21 – 2025-07-16 | 4,803 |

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
