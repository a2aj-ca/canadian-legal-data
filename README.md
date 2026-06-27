# A2AJ Canadian Legal Data

Last updated: 2026-06-27

Maintainer: [Access to Algorithmic Justice (A2AJ)](https://a2aj.ca)

## Overview

This repository provides tools and documentation for accessing Canadian legal data through multiple open access / open source 
channels. The project builds on an earlier [version](https://huggingface.co/datasets/refugee-law-lab/canadian-legal-data) that 
was maintained by the [Refugee Law Lab (RLL)](https://refugeelab.ca/) and is now maintained by [A2AJ](https://a2aj.ca/), a 
research project co-hosted by York University's Osgoode Hall Law School and Toronto Metropolitan University's Lincoln Alexander 
School of Law. The data is intended to support empirical legal research, legal-tech prototyping, and language-model 
pre-training in the public interest—especially work that advances access to justice for marginalised and low-income communities.

Case law records now include citation network fields (`cases_cited`, `cases_citing`, and `citing_cases_count`), enabling 
citation analysis, precedent mapping, and network-based research across the corpus. See [Citation Network](#citation-network) 
below for details.

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

### Court Decisions (223,224 cases)

| Code   | Court / Tribunal                         | Coverage Period            | Cases   |
|--------|------------------------------------------|----------------------------|---------|
| SCC    | Supreme Court of Canada                  | 1877-01-15 – 2026-06-19 | 10,885 |
| FCA    | Federal Court of Appeal                  | 2001-02-01 – 2026-06-18 | 7,771 |
| BCCA   | British Columbia Court of Appeal         | 1999-01-04 – 2026-06-19 | 14,601 |
| ONCA   | Ontario Court of Appeal                  | 1998-06-08 – 2026-06-19 | 23,930 |
| NSCA   | Nova Scotia Court of Appeal              | 1993-01-04 – 2026-06-18 | 4,729 |
| YKCA   | Yukon Court of Appeal                    | 2000-05-15 – 2026-06-16 | 276 |
| FC     | Federal Court                            | 2001-02-01 – 2026-06-19 | 35,639 |
| TCC    | Tax Court of Canada                      | 2003-01-21 – 2026-06-16 | 8,071 |
| CMAC   | Court Martial Appeal Court               | 2001-01-19 – 2026-05-19 | 154 |
| BCSC   | Supreme Court of British Columbia        | 2000-01-04 – 2026-06-18 | 51,887 |
| NSSC   | Nova Scotia Supreme Court                | 2001-01-04 – 2026-06-16 | 9,179 |
| NSPC   | Nova Scotia Provincial Court             | 2001-01-15 – 2026-06-15 | 1,601 |
| NSFC   | Nova Scotia Family Court                 | 2001-02-02 – 2023-11-06 | 323 |
| NSSM   | Nova Scotia Small Claims Court           | 2001-08-30 – 2026-03-20 | 1,648 |
| CHRT   | Canadian Human Rights Tribunal           | 2003-01-10 – 2026-06-15 | 1,159 |
| CIRB   | Canada Industrial Relations Board        | 1995-12-08 – 2026-05-01 | 1,173 |
| CITT   | Canadian International Trade Tribunal    | 1980-01-01 – 2026-06-18 | 5,429 |
| CT     | Competition Tribunal                     | 2000-02-17 – 2026-06-05 | 624 |
| FPSLREB | Federal Public Sector Labour Relations and Employment Board | 2003-01-03 – 2026-06-16 | 3,430 |
| OHSTC  | Occupational Health and Safety Tribunal Canada | 1992-01-09 – 2025-03-06 | 811 |
| OIC    | Information Commissioner of Canada       | 2019-08-26 – 2026-04-09 | 325 |
| PSDPT  | Public Service Disclosure Protection Tribunal | 2011-06-10 – 2025-05-21 | 29 |
| RAD    | Refugee Appeal Division (IRB)            | 2013-02-19 – 2025-10-23 | 14,156 |
| RPD    | Refugee Protection Division (IRB)        | 2002-07-16 – 2020-12-14 | 6,729 |
| RLLR   | Refugee Law Lab Reporter (RPD, IRB)      | 2019-01-07 – 2024-12-13 | 927 |
| SST    | Social Security Tribunal                 | 2013-03-08 – 2026-05-27 | 17,738 |

### Legislation & Regulations (10,895 documents)

| Code            | Type                      | Coverage Period            | Documents |
|-----------------|---------------------------|----------------------------|-----------|
| LEGISLATION-FED | Federal Statutes          | 1870-05-12 – 2026-05-06 | 962 |
| REGULATIONS-FED | Federal Regulations       | 1945-12-21 – 2026-05-25 | 4,868 |
| LEGISLATION-ON  | Ontario Legislation       | 1986-07-28 – 2026-06-25 | 856 |
| REGULATIONS-ON  | Ontario Regulations       | 1990-12-31 – 2026-06-26 | 2,205 |
| LEGISLATION-BC  | British Columbia Legislation | 1924-12-19 – 2026-05-28 | 588 |
| REGULATIONS-BC  | British Columbia Regulations | 1975-04-22 – 2026-05-11 | 1,416 |

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
| cases_cited_en / cases_cited_fr | list[string] | Neutral citations referenced in the decision's full text (outbound citations) |
| cases_citing_en / cases_citing_fr | list[string] | Cases in the corpus whose full text cites this decision (inbound citations) |
| citing_cases_count | integer | Number of distinct cases in the corpus that cite this decision |
| upstream_license | string | Source license terms |

### Legislation & Regulations

| Field | Type | Description |
|-------|------|-------------|
| dataset | string | LEGISLATION-FED, REGULATIONS-ON |
| citation_en / citation_fr | string | Official citation |
| name_en / name_fr | string | Full title |
| document_date_en / document_date_fr | datetime | Enactment/publication date |
| url_en / url_fr | string | Source URL |
| scraped_timestamp_en / scraped_timestamp_fr | datetime | Scraping timestamp |
| unofficial_text_en / unofficial_text_fr | string | Full text |
| upstream_license | string | Source license terms |

## Citation Network

Case law records include automatically extracted citation network data:

- **cases_cited** (outbound): Unique neutral citations (e.g., `2020 SCC 5`) detected in the decision's full text, listed in 
  order of first appearance, with self-citations excluded. Cited cases are included whether or not they appear in the corpus 
  (e.g., citations to decisions of courts we do not cover). The field is null when there is no text in that language.
- **cases_citing** (inbound): Cases in the corpus whose full text cites this decision's neutral citation. Inbound citations 
  can only be detected for decisions that themselves have a neutral citation, so this field (and `citing_cases_count`) is 
  null for decisions identified only by docket-style citations (e.g., CITT/TCCE dockets) or other non-neutral citations.
- **citing_cases_count**: The number of distinct cases in the corpus that cite this decision. A case citing both the English 
  and French versions of a decision is counted once.

### Citation Network Limitations

- Extraction is based on pattern matching of neutral citations only. Citations using traditional reporters (e.g., 
  `[1999] 2 S.C.R. 817`) are not captured, so decisions pre-dating neutral citations (generally pre-2000) are 
  under-represented in the network, as are tribunals and courts that do not use neutral citations (e.g., CITT/TCCE).
- Inbound citation data (`cases_citing`, `citing_cases_count`) reflects only the corpus: citations from courts, tribunals, 
  or time periods not covered by our datasets are not counted.
- Text extraction artifacts (e.g., OCR or formatting issues) may cause occasional missed or spurious citations.

## Getting Started

1. **For API access**: Review `access-via-api.ipynb` for examples of searching and retrieving specific documents
2. **For bulk analysis**: Use `access-via-hugging-face.ipynb` or `access-via-parquet.ipynb` depending on your needs
3. **For AI integration**: See `access-via-mcp.ipynb` for connecting AI assistants to the legal data
4. **To host your own API/MCP server**: See [a2aj-api-public](https://github.com/a2aj-ca/a2aj-api-public) for open source code and deployment instructions

## Data Quality & Limitations

- **Unofficial Copies**: All texts are unofficial; consult source URLs for authoritative versions
- **Coverage Gaps**: Gaps exist for some courts/tribunals; not all decisions are published on court/tribunal websites
- **Processing**: Automated scraping may introduce formatting artifacts
- **Citation Network**: Citation fields are extracted automatically and are approximate (see Citation Network Limitations above)
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

> Sean Rehaag & Simon Wallace, "A2AJ Canadian Legal Data" (2025), online: GitHub [https://github.com/a2aj-ca/canadian-legal-data](https://github.com/a2aj-ca/canadian-legal-data) (updated 2026).
