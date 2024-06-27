from django.shortcuts import render
from django.http import HttpResponseRedirect    
from .models import Usuario, Genero

from .forms import GeneroForm   

# Create your views here.

def index (request):
    usuarios=Usuario.objects.all()
    #context={"usuarios":usuarios}
    context = {
        'usuarios' : usuarios
    }
    return render(request, 'usuarios/index.html',context)


def crud (request):
    usuarios=Usuario.objects.all()
    context = {
        'usuarios' : usuarios
    }
    return render(request, 'usuarios/usuarios_list.html',context)



def usuariosAdd (request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context = {
            'generos' : generos
        }
        return render(request, 'usuarios/usuarios_add.html',context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"      

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Usuario.objects.create (rut=rut, nombre=nombre, 
        apellido_paterno=aPaterno, apellido_materno=aMaterno,
        fecha_nacimiento=fechaNac, id_genero=objGenero,
        telefono=telefono, email=email, direccion=direccion, activo=1)
        
        obj.save()
        context={'mensaje':"Datos almacenados de manera correcta"}
        return render(request, 'usuarios/usuarios_add.html',context)

def usuarios_del (request,pk):
    context = {}
    try:
        Usuario=Usuario.objects.get(rut=pk)
        Usuario.delete()

        mensaje="Datos eliminados de manera correcta"
        usuarios=Usuario.objects.all()
        context = {
            'usuarios' : usuarios, 'mensaje' : mensaje
        }
        return render(request, 'usuarios/usuarios_list.html',context)
    except:
        mensaje="Error, Rut no existe"
        usuarios=Usuario.objects.all()
        context = {
            'usuarios' : usuarios, 'mensaje' : mensaje
        }
        return render(request, 'usuarios/usuarios_list.html',context)
    
def usuarios_findEdit (request,pk):
    if pk != "":
        Usuario=Usuario.objects.get(rut=pk)
        generos=Genero.objects.all()
        
        print(type(Usuario.id_genero.genero))
        context = {
            'Usuario' : Usuario, 'generos' : generos
        }
        if Usuario:
            return render(request, 'usuarios/usuarios_edit.html',context)
        else:
            mensaje="Error, Rut no existe"
            return render(request, 'usuarios/usuarios_list.html',context)

def usuariosUpdate (request):
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"   

        objGenero=Genero.objects.get(id_genero = genero)

        Usuario = Usuario()
        Usuario.rut = rut
        Usuario.nombre = nombre
        Usuario.apellido_paterno = aPaterno
        Usuario.apellido_materno = aMaterno
        Usuario.fecha_nacimiento = fechaNac
        Usuario.id_genero=objGenero
        Usuario.telefono = telefono
        Usuario.email = email
        Usuario.direccion = direccion
        Usuario.activo = 1
        Usuario.save()

        generos=Genero.objects.all()
        context = {
            'Usuario' : Usuario, 'generos' : generos, 'mensaje' : "Datos actualizados correctamente"
        }
        return render(request, 'usuarios/usuarios_edit.html',context)
    else:
        usuarios=Usuario.objects.all()
        context = {
            'usuarios' : usuarios 
        }
        return render(request, 'usuarios/usuarios_list.html',context)

def crud_generos(request):
    generos=Genero.objects.all()
    context = {
        'generos' : generos
    }
    return render(request, 'usuarios/generos_list.html',context)



def generosAdd(request):
    if request.method == "POST":    
        form = GeneroForm(request.POST)
        if form.is_valid():  # Corrected: Added parentheses to is_valid
            form.save()
            context = {
                'mensaje': "OK",
                'form': form
            }
            return render(request, 'usuarios/generos_add.html', context)
    else:
        form = GeneroForm()  # Corrected: Assigned a new instance of GeneroForm to form
        context = {
            'form': form
        }
        return render(request, 'usuarios/generos_add.html', context)



def generos_del (request,pk):
    mensajes = []
    errores = []

    generos=Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context = {}

        if genero:
            genero.delete()

            mensaje="Datos eliminados de manera correcta"
            usuarios=Usuario.objects.all()
            context = {
                'generos' : generos, 'mensaje' : mensajes, 'errores' : errores
            }
            return render(request, 'usuarios/generos_list.html',context)
    except:
        mensaje="Error, id no existe"
        generos=Genero.objects.all()
        context = {
            'generos' : generos, 'mensaje' : mensaje
        }
        return render(request, 'usuarios/generos_list.html',context)



def generos_edit (request,pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context = {}

        if genero:
            if request.method == "POST":    
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                context = {
                    'mensaje': "OK",
                    'form': form,
                    'genero' : genero
                }
                return render(request, 'usuarios/generos_edit.html', context)
            else:
                form = GeneroForm(instance=genero)  # Corrected: Assigned a new instance of GeneroForm to form
                context = {
                    'mensaje': "",
                    'form': form,
                    'genero' : genero
                }
                return render(request, 'usuarios/generos_edit.html', context)
    except:
        mensaje="Error, id no existe"
        generos=Genero.objects.all()
        context = {
            'generos' : generos, 'mensaje' : mensaje
        }
        return render(request, 'usuarios/generos_list.html',context)
