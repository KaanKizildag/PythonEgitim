import sqlite3

class SqlDal:

    def __init__(self,connectionString):
        self.connectionString = connectionString

    def getConnection(self):
        self.connection = sqlite3.connect('Products.db')
    # InnerFunction kullanılabilir.
    def getProducts(self):
        self.getConnection()
        cursor = self.connection.cursor()
        result = cursor.execute('select * from products')
        for i in result:
            print(i)
        self.connection.close()

    def insertProduct(self, name, price):
        self.getConnection()
        cursor = self.connection.cursor()

        query = f"insert into products (name, price) values ('{name}',{price});"
        #cursor.execute(query)
        cursor.executescript(query)

        self.connection.close()



sqlDal = SqlDal('')
name = input('Enter a product name: ')
price = float(input('Enter your product price: '))
sqlDal.insertProduct(name, price)
sqlDal.getProducts()
