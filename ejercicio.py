import pymongo


if __name__=="__main__":
    print("Ejercicio demostrativo")
    #-*-*-*Conexión con mongodb-*-*-*
    connection=pymongo.MongoClient("mongodb://127.0.0.1:27017")
    
    #-*-*-*Base de datos de mongo-*-*-*-*
    database=connection["nplCurso"]
    
    #-*-*-*-*Obtener datos-*-*-*-*
    '''collection=database["continentes"]
    result=collection.find()
    print("DATA".center(40,"♦"))
    
    for tmp in result:
        print()
        print(tmp["continente"])'''
        
    #-*-*-*-*Insertar los datos-*-*-*-*
    collection=database["continentes"]
    continente={
        "continente":"America",
        "paises":[{"nombre":"México", "idioma":"Español"}]
    }
    result=collection.insert_one(continente)
    print(result)
    
    