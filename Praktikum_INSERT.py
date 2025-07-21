import sqlite3

connect_to_db = sqlite3.connect("Cars.db")

k = connect_to_db.cursor()

k.execute("""
    INSERT INTO TBCars (
        id,
        name,
        brand,
        model,
        price
    )
    VALUES 
        ('101', 'McLaren 750S', 'McLaren', '750S 2025', 350000),
        ('102', 'Porsche 911 Turbo S', 'Porsche', '911 Turbo S 2025', 220000)
        ('103', 'Ferrari 296 GTB', 'Ferrari', '296 GTB 2025', 320000)
""")


connect_to_db.commit()
connect_to_db.close()
