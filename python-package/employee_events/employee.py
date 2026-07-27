# Import the QueryBase class
#### YOUR CODE HERE
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
#### YOUR CODE HERE
import sqlite3
import pandas as pd
from pathlib import Path


# Dynamically calculate the absolute path to the database file in this package
DB_PATH = Path(__file__).resolve().parent / "employee_events.db"

# Define a subclass of QueryBase
# called Employee
#### YOUR CODE HERE
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    #### YOUR CODE HERE
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
    def names(self) -> list:
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        #### YOUR CODE HERE
        query = """
        SELECT 
            first_name || ' ' || last_name AS full_name,
            employee_id
        FROM employee
        ORDER BY last_name, first_name;
        """
        
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            # If the base class loop expects (text, value), swap the order here:
            return [(str(row[0]), str(row[1])) for row in rows]
        
        

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
    def username(self, id: int) -> list:
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        #### YOUR CODE HERE
        query = f"""
        SELECT first_name || ' ' || last_name AS full_name
        FROM {self.name}
        WHERE {self.name}_id = ?;
        """
        
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            return cursor.fetchall()

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):

        # query = f"""
        #             SELECT SUM(positive_events) positive_events
        #                  , SUM(negative_events) negative_events
        #             FROM {self.name}
        #             JOIN employee_events
        #                 USING({self.name}_id)
        #             WHERE {self.name}.{self.name}_id = {id}
        #         """
        query = f"""
            SELECT SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM employee_events
            WHERE employee_id = {id}
        """
        
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query(query, conn)
        return df
