STEPS TO CREATING DATABASE:


For speedy approach just run Neo4J_Database_Insert.py all the required pkl files are in the folder.

To Run From Scratch:
Run : wiki_spider_merge_2.py  - scrapes wikipedia
Run : NCAIS_code_scrapper.py	- scrapes siccode.com
Run : pytext_competitors_and_People.ipynb  - creates people and competitor companies pkl files for nodes, required csv files are provided
Run : Unstructured_Product_Extraction.ipynb - creates product and services nodes
Run : acquired_nodes_creation.ipynb - creates acquired companies nodes, required csv files are provided
Run : NAICS_Codes.ipynb  -  creates NAICS nodes, required xlsx file provided
Run : Financials-2.ipynb  - creates financial data nodes
Run : Social Media.ipynb  - creates social media nodes in cleaned folder and copy paste where 5_Table_Creations.ipynb is located
Run : 5_Table_Creations.ipynb - creates 5 tables for insertion into Neo4J
Run : Neo4J_Database_Insert.ipynb  - inserts data into Neo4j database, password and database location made need to be altered to work with your database

If any questions please email ehoye@eng.ucsd.edu for assistance.
