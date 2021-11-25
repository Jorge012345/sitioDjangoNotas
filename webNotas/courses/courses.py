class Courses:
    lista=[]
    def __init__(self,request):
        self.request=request
        self.session=request.session
        lista=self.session.get("lista")
        if not lista:
            lista=self.session["lista"]=[]
        else:
            self.lista=lista
       

    def anios_sin_repetir(self, courses):
        self.lista.append(courses.created.year)
    def mostrar(self):
        return self.lista



        