## Diagrama de clases



```mermaid
---
config:
  theme: redux-color
  look: classic
  layout: elk
---
classDiagram
    direction TB

    %% Jerarquía de Usuarios
    class Usuario {
        +UUID id
        +String dni
        +String nombre
        +String apellido
        +String email
        +String telefono
        +String contrasena
        +Boolean activo
        +autenticar() Boolean
    }

    class Medico {
        +String registroColegioMedico
        +String firmaDigital
        +realizarAtencion(Paciente, Formulario) AtencionSalud
        +emitirDiagnostico(AtencionSalud, DiagnosticoCIE) Diagnostico
        +solicitarExamen(Paciente, ExamenLaboratorio) void
    }

    class Investigador {
        +String especialidad
        +String orcid
        +crearProyecto() ProyectoInvestigacion
        +analizarCohorte(ProyectoInvestigacion) DataSet
    }

    class Administrador {
        +crearUsuario(Usuario) void
        +asignarPermisos(Usuario, Rol) void
        +configurarParametro(Parametro) void
    }

    Usuario <|-- Medico
    Usuario <|-- Investigador
    Usuario <|-- Administrador

    %% Institución y Proyectos
    class Institucion {
        +UUID id
        +String alias
        +String paisISO
        +JSONB datosContacto
        +vincularProyecto(ProyectoInvestigacion) void
    }

    class ProyectoInvestigacion {
        +UUID id
        +String nombre
        +String nombreCorto
        +Date fechaInicio
        +Date fechaTermino
        +Boolean esMulticentro
        +Boolean esCienciaAbierta
        +Integer cupoPacientes
        +inscribirPaciente(Paciente, ConsentimientoInformado) void
        +agregarInstitucionParticipante(Institucion) void
    }

    %% Paciente y Consentimiento
    class Paciente {
        +UUID uuidAnonimizado
        +Integer codigoInterno
        +String rutDni
        +String nombres
        +String apellidos
        +Date fechaNacimiento
        +String sexo
        +String etnia
        +JSONB datosDemograficos
        +obtenerHistorialClinico() List~AtencionSalud~
        +firmarConsentimiento(ProyectoInvestigacion) ConsentimientoInformado
    }

    class ConsentimientoInformado {
        +UUID id
        +Date fechaFirma
        +Boolean autorizaContacto
        +Boolean autorizaEstudioFarmaceutico
        +Boolean autorizaCienciaAbierta
        +Boolean revocado
        +Date fechaRevocacion
        +String rutaDocumentoPDF
        +validarVigencia() Boolean
        +revocarConsentimiento() void
    }

    %% Atenciones y Formularios Clínicos
    class AtencionSalud {
        +UUID id
        +Date fecha
        +Integer etapaSeguimiento
        +String tipoAtencion
        +JSONB respuestasClinicas
        +registrarDatos(Formulario) void
        +asociarDiagnostico(Diagnostico) void
    }

    class FormularioClinico {
        +UUID id
        +String nombre
        +Integer version
        +String categoria
        +String tipoRegistro
        +JSONB esquemaPreguntas
        +Boolean estaBloqueado
        +renderizarFormulario() View
        +validarEntradas(JSONB) Boolean
    }

    class ExamenLaboratorio {
        +UUID id
        +Date fechaToma
        +String codigoLOINC
        +String componenteAnalizado
        +JSONB resultados
        +cargarResultado(JSONB) void
    }

    %% Diagnósticos y Catálogos
    class Diagnostico {
        +UUID id
        +Date fechaDiagnostico
        +String tipoCriterio
        +String estado
        +String comentarios
    }

    class CatalogoCIE {
        <<Abstract>>
        +String codigo
        +String descripcion
        +obtenerDetalle() String*
    }

    class CIE10 {
        +String clasificacionGeneral
        +obtenerDetalle() String
    }

    class CIEO {
        +String codigoTopografia
        +String codigoMorfologia
        +obtenerDetalle() String
    }

    CatalogoCIE <|-- CIE10
    CatalogoCIE <|-- CIEO

    %% Relaciones y Cardinalidades
    Institucion "1" -- "0..*" ProyectoInvestigacion : es sede principal de
    Institucion "0..*" -- "0..*" ProyectoInvestigacion : participa en (multicéntrico)
    Institucion "1" -- "0..*" Usuario : afilia a

    Investigador "1" -- "0..*" ProyectoInvestigacion : lidera como IP
    ProyectoInvestigacion "1" *-- "0..*" FormularioClinico : define / contiene

    ProyectoInvestigacion "0..*" -- "0..*" Paciente : recluta mediante Protocolo
    Paciente "1" *-- "1..*" ConsentimientoInformado : otorga
    ProyectoInvestigacion "1" -- "0..*" ConsentimientoInformado : rige bajo

    Paciente "1" *-- "0..*" AtencionSalud : recibe
    Medico "1" -- "0..*" AtencionSalud : ejecuta
    ProyectoInvestigacion "1" -- "0..*" AtencionSalud : enmarca

    AtencionSalud "0..*" --> "1" FormularioClinico : estructurada con
    AtencionSalud "1" *-- "0..*" Diagnostico : establece
    Diagnostico "0..*" --> "1" CatalogoCIE : codificado segun

    Paciente "1" *-- "0..*" ExamenLaboratorio : se realiza
    Medico "0..1" -- "0..*" ExamenLaboratorio : solicita / valida
    ProyectoInvestigacion "1" -- "0..*" ExamenLaboratorio : recopila
    ```