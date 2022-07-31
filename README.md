# Inventory Tracker

### Created using Python, Django, PostgreSQL, Bootstrap, and HTML

An inventory tracking web application for a logistics company that has CRUD functionality (create inventory items, edit, delete, and view a list of them), as well as an additional feature which is exporting the product data to a CSV file (Excel Spreadsheet). 

## Demo 
https://youtu.be/HdQaV9lVgxg

### Before you run the application, please make sure you have the following tools installed:
**VSCode**: https://code.visualstudio.com/download

**Python 3.7+**: https://www.python.org/downloads/

**pgAdmin 4**: https://www.pgadmin.org/download/

**PostgreSQL**:  https://www.postgresql.org/download/

### How to run the application
   
1. Clone the git repository using the following command: 
   
   `git clone https://github.com/kermali-mehdiya/Shopify-Backend-Dev-Challenge.git`
    
2. Open a terminal / command prompt in the root of the project's folder (folder is called _inventory_manager_)
3. Run the following command to open the project in VSCode: `code .` 
4. Open pgAdmin 4. After setting your master password, you will need to set up a PostgreSQL Database. To do so, please refer to the following links depending on your operating system. Make sure the username is `postgresql` when creating a new user. Also, make sure the name of the database is `InventoryDB`.

**Windows:** https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm

**Linux:** https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL_Linux.htm

**Mac:**
https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/

5. Once connected to the server, go back to VSCode and open a new terminal. 
   Enter the following command: `python3 manage.py runserver`
   
   This will open the application on port `:8000`.
   


  
