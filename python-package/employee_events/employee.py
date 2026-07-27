# Import the QueryBase class
from .query_base import QueryBase
import pandas as pd

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self) -> list:
        
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        query = """
        SELECT 
            first_name || ' ' || last_name AS full_name,
            employee_id
        FROM employee
        ORDER BY last_name, first_name;
        """
        
        # Call the inherited self.query() method from QueryMixin 
        rows = self.query(query)
        # Return structured tuples containing text, value
        return [(str(row[0]), str(row[1])) for row in rows]

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id: int) -> list:
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        query = f"""
        SELECT first_name || ' ' || last_name AS full_name
        FROM {self.name}
        WHERE {self.name}_id = {id};
        """
        
        # Call the inherited self.query() method from QueryMixin
        return self.query(query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id):

        query = f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """
        
        # Call the inherited self.pandas_query() method from QueryMixin
        return self.pandas_query(query)
