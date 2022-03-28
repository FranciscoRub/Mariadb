import bd
from modelo import Slangs


def crear_registro():
    
    slang = input("Slang: ")
    significado = input("Significado: ")
    x= Slangs(None,slang,significado)
    bd.session.add(x)
    bd.session.commit()
    print("Nuevo slang","(",x,")""guardado con exito.")


def consultar_registro():
    SLANG=bd.session.query(Slangs).all()
    print(SLANG)

def eliminar_registro():
    consultar_registro()
    Elimreg=input("\n ID de Registro que desea eliminar: ")
    Elimreg = bd.session.query(Slangs).filter_by(ID=Elimreg).first()
    bd.session.delete(Elimreg)
    bd.session.commit()
    consultar_registro()
def editar_registro():
    consultar_registro()
    Editregistro = (input("\n ID de Slang que desea editar: "))
    x=bd.session.query(Slangs).get(Editregistro)
    print("--------SELECCIÓN--------\nSlang: ",x.SLANG,"\nSignificado: ",x.SIGNIFICADO)
    print("---------EDITAR---------")
    x.SLANG = input("Nuevo slang: ")
    x.SIGNIFICADO = input("significado: ")
    print("Slang editado con exito")
    bd.session.commit()
    x= bd.session.query(Slangs).first()
    consultar_registro()
def mostrar_slangs():
    slang=bd.session.query(Slangs).order_by(Slangs.SLANG,Slangs.ID)
    for slang in slang:
        print(slang.ID,slang.SLANG)
    slang =input("\n\nID de Slang que desea consultar: ")
    x=bd.session.query(Slangs).get(slang)
    print("\nslang: ",x.SLANG,"\nsignificado: ",x.SIGNIFICADO)
    
   
    

def run():
    #QUITAR ASTIRISTICOS PARA NO GENERAR UNA TABLA VACIA 
    #qxopa = Slangs(1,'Que xopa','Saludo')
    #bd.session.add(qxopa)
    #bd.session.commit()
    #print(qxopa.ID)
    
    #mopri = Slangs(2, 'Mopri','Amigo cercano')
    #bd.session.add(mopri)
    #bd.session.commit()
    #print(mopri.ID)

    #rantan = Slangs(3, 'Rantan','Bastante')
    #bd.session.add(rantan)
    #bd.session.commit()
    #print(rantan.ID)
    
    print("--------------------------Diccionario de Slang Panameño-------------------------")
menuprincipal = int(input("--Menú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente\n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n Elija una opción: "))


while menuprincipal !=6:
    if menuprincipal == 1:
        crear_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 2:
        editar_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 3:
        eliminar_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==4:
        consultar_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==5:
        mostrar_slangs()
        menuprincipal==input("preciones Enter para seguir: ")
    else:
        print("Por favor digite una opción válida")
        
    menuprincipal = int(input("\n\n\nMenú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente \n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n"))

    
    
if __name__ == '__main__':
    bd.Base.metadata.create_all(bd.engine)
    run()


