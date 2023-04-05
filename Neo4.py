from flask import Flask, current_app

from neo4j import GraphDatabase

app = Flask(__name__)

uri = 'bolt://54.85.253.216:7687'
username = 'neo4j'
password = 'routines-limb-judges'

def init_driver(uri, username, password):
    current_app.driver = GraphDatabase.driver(uri,auth=(username, password))
    
    current_app.driver.verify_connectivity()
    
    return current_app.driver
    
def close_driver():
    if current_app.driver != None:
        current_app.driver.close()
        current_app.driver = None
        
        return current_app.driver
        
def run_query():
    with current_app.driver.session() as session:
        result = session.run(
            "MATCH (p:Person {name: $name}) RETURN p",
            name = "Tom Hanks")
        for record in result:
            print (record)
            
with app.app_context():
    init_driver(uri, username, password)
    run_query()
    close_driver()


