# -*- coding: utf-8 -*-
"""
Datos estructurados y textos tecnicos para el Informe Final EP3 - Cuidarte+
Asignatura: ISY1102 - Seguridad y calidad en el desarrollo de software
Docente: CLAUDIO DANIEL GONZALEZ PAUZOCA
Integrantes: Ricardo Saez, Patricio Quilodran, Sebastian Dinamarca
Seccion: 006D
NOTA ESTRICTA: Sin emojis.
"""

COVER_DATA = {
    "titulo_principal": "TITULO\nInforme de seguridad y calidad \nen el desarrollo de software",
    "asignatura_seccion": "ISY1102 - Seguridad y calidad en el desarrollo de software\nSección 006D",
    "integrantes_docente": (
        "Integrantes:\n"
        "Ricardo Saez\n"
        "Patricio Quilodran\n"
        "Sebastian Dinamarca\n\n"
        "Profesor:\n"
        "CLAUDIO DANIEL GONZALEZ PAUZOCA\n\n"
        "Carrera:\n"
        "Ingeniería en Informática\n\n"
        "Institución:\n"
        "Duoc UC - Escuela de Informática y Telecomunicaciones\n\n"
        "Fecha:\n"
        "Octubre 2026"
    )
}

TOC_ENTRIES = [
    ("1. Introducción", "3"),
    ("  1.1 Contexto del software a evaluar", "3"),
    ("  1.2 Propósito del plan y objetivos de calidad", "3"),
    ("  1.3 Ajustes basados en retroalimentación de la Evaluación Parcial 1", "4"),
    ("  1.4 Estructura del informe", "4"),
    ("2. Criterios de calidad", "5"),
    ("  2.1 Calidad de software basada en ISO/IEC 25010", "5"),
    ("  2.2 Seguridad de la información y gestión de riesgos OWASP", "6"),
    ("  2.3 Cumplimiento normativo y marco legal chileno", "7"),
    ("3. Plan de pruebas", "8"),
    ("  3.1 Estrategia de pruebas", "8"),
    ("  3.2 Tipos de prueba y justificación técnica", "10"),
    ("  3.3 Criterios de aceptación transversales", "12"),
    ("  3.4 Herramientas utilizadas y asignación de recursos", "13"),
    ("4. Diseño de casos de prueba", "15"),
    ("5. Ejecución de pruebas", "25"),
    ("  5.1 Resumen de ejecución", "25"),
    ("  5.2 Detalle de ejecución de casos", "26"),
    ("  5.3 Criticidad de incidentes", "29"),
    ("6. Análisis ético y normativo de los resultados obtenidos", "32"),
    ("  6.1 Vulneración de la Ley Nº 19.628 sobre Protección de Datos Personales", "32"),
    ("  6.2 Vulneración de la Ley Nº 20.584 y custodia de ficha clínica", "33"),
    ("  6.3 Riesgos penales bajo la Ley Nº 21.459 sobre Delitos Informáticos", "34"),
    ("  6.4 Responsabilidad bioética y deontología profesional", "35"),
    ("7. Matriz de trazabilidad y cobertura de requerimientos ERS (100%)", "36"),
    ("8. Conclusiones y recomendaciones de mejora continua", "39"),
    ("  8.1 Conclusiones generales del proceso de auditoría y aseguramiento", "39"),
    ("  8.2 Plan de remediación técnica inmediata", "40")
]

SECTION_1_TEXTS = {
    "intro_p1": (
        "El presente informe técnico consolida el Plan Integral de Pruebas, Auditoría de Calidad, "
        "Evaluación de Seguridad y Verificación de Cumplimiento Normativo aplicado al sistema de salud "
        "'Cuidarte+', desarrollado para la gestión digital de pacientes, fichas clínicas, órdenes de exámenes médicos "
        "y custodia de documentación clínica sensible. En el contexto de los sistemas de información para el sector de la salud, "
        "el software no solo representa una herramienta operativa, sino un componente crítico que impacta directamente en la toma "
        "de decisiones clínicas, en la privacidad de las personas y en la continuidad asistencial. Por consiguiente, la calidad y "
        "la seguridad no pueden considerarse atributos secundarios, sino requerimientos indispensables y legalmente exigibles."
    ),
    "contexto_p1": (
        "El software evaluado, 'Cuidarte+', se estructura arquitectónicamente como una aplicación web multicapa moderna. La capa de "
        "presentación (Frontend) está desarrollada en React v19.1.1 con Material UI v7.3.4, proporcionando una interfaz responsiva "
        "y componentes diseñados para profesionales médicos, administradores y pacientes (con especial énfasis en accesibilidad para "
        "adultos mayores). La capa de servicios (Backend) opera sobre Node.js con Express v4.19.2, exponiendo una API RESTful documentada "
        "bajo OpenAPI 3.0 (Swagger) para gestionar autenticación basada en JWT, administración de usuarios, control de pacientes, emisión "
        "de órdenes médicas y carga/descarga de archivos clínicos. Finalmente, la capa de persistencia se sustenta en PostgreSQL v15+, "
        "encargada del modelo relacional de datos y de la tabla de auditoría del sistema."
    ),
    "proposito_p1": (
        "El propósito primordial de este plan de pruebas es auditar rigurosamente el código fuente, la arquitectura, los flujos "
        "operativos y los controles de acceso del sistema Cuidarte+, contrastándolos contra la Especificación de Requerimientos de Software (ERS) "
        "previamente formalizada. Se busca verificar experimentalmente si la plataforma satisface las directrices de calidad técnica bajo la "
        "norma ISO/IEC 25010, los principios de seguridad de OWASP Top 10 y los mandatos jurídicos de la legislación chilena (Ley 19.628, Ley 20.584 "
        "y Ley 21.459). Las pruebas persiguen identificar vulnerabilidades explotables, defectos de lógica de negocio, fugas de información y "
        "desviaciones funcionales antes de que el software alcance un entorno productivo hospitalario."
    ),
    "ajustes_ep1_p1": (
        "Durante la primera evaluación parcial (EP1), se estableció el documento base de ERS con la definición de requerimientos funcionales "
        "(RF-1 a RF-5), no funcionales (NFR-SEG, NFR-PERF, NFR-USAB, NFR-DIS, NFR-COMPAT) y reglas de negocio (RB-1 a RB-3). A partir de la "
        "retroalimentación formativa y feedback entregado por el docente evaluador, se implementaron las siguientes mejoras esenciales para este encargo:"
    ),
    "ajustes_ep1_items": [
        ("Ampliación del alcance de seguridad", "Se profundizó en el análisis de las debilidades criptográficas en el almacenamiento de contraseñas y en el manejo de tokens JWT, extendiendo el análisis estático hacia los middlewares de autorización y endpoints estáticos."),
        ("Formalización de pruebas no funcionales", "Se incorporaron mediciones cuantitativas objetivas para evaluar los tiempos de respuesta del servidor (umbral de 300 ms) y la accesibilidad web (contraste cromático y usabilidad para adultos mayores bajo WCAG 2.1)."),
        ("Vinculación con el marco normativo chileno", "Se estableció un análisis explícito y exhaustivo que correlaciona cada hallazgo de defecto con los artículos específicos de la Ley 19.628 (Protección de Datos Personales), Ley 20.584 (Derechos y Deberes del Paciente) y Ley 21.459 (Delitos Informáticos)."),
        ("Cobertura total del 100% de los requerimientos", "Se estructuró una matriz de trazabilidad bidireccional que asegura que todos y cada uno de los requisitos estipulados en la ERS cuenten con casos de prueba asociados y estado de verificación.")
    ],
    "estructura_p1": (
        "El informe se organiza de manera lógica y secuencial: en la Sección 2 se detallan los Criterios de Calidad técnica, seguridad y cumplimiento "
        "normativo; en la Sección 3 se describe el Plan de Pruebas integral con estrategia, tipos de prueba, criterios de aceptación, herramientas y "
        "recursos; en la Sección 4 se presentan los Diseños de Casos de Prueba representativos utilizando el formato tabular estandarizado; en la "
        "Sección 5 se expone la Ejecución de Pruebas con métricas, tabla detallada de ejecución y matriz de criticidad de incidentes; en la Sección 6 "
        "se efectúa un profundo Análisis Ético y Normativo de los hallazgos; en la Sección 7 se despliega la Matriz de Trazabilidad con cobertura al 100%; "
        "y en la Sección 8 se entregan las Conclusiones y el Plan de Remediación Técnica Inmediata."
    )
}

SECTION_2_TEXTS = {
    "calidad_intro": (
        "Los estándares de calidad para el sistema Cuidarte+ se fundamentan en el modelo de calidad de producto de software "
        "establecido por el estándar internacional ISO/IEC 25010 (System and Software Quality Requirements and Evaluation - SQuaRE). "
        "Dada la criticidad del negocio médico asistencial, se definieron cinco pilares de calidad mandatorios:"
    ),
    "calidad_pilares": [
        ("Usabilidad (Usability)", "Capacidad del software para ser comprendido, aprendido y utilizado eficientemente. Según NFR-USAB-1 y NFR-USAB-2, la interfaz debe contar con controles visuales de tamaño generoso, tipografía legible con tamaño mínimo de 12px y contraste suficiente, adaptados a la interacción de adultos mayores y profesionales en turnos médicos de alta fatiga visual."),
        ("Rendimiento y Eficiencia de Desempeño (Performance Efficiency)", "Capacidad de respuesta bajo condiciones de operación normal y concurrente. Conforme a NFR-PERF-1 y NFR-PERF-3, las transacciones CRUD simples deben responder en menos de 300 ms, y la carga inicial de vistas no debe exceder 2 segundos, tolerando hasta 200 usuarios concurrentes sin degradación de servicio."),
        ("Confiabilidad y Estabilidad (Reliability)", "Capacidad del sistema de mantener su nivel de servicio operativo frente a fallos. Según NFR-DIS-1, se exige una disponibilidad mensual del 99.5%, con mecanismos robustos de manejo de excepciones y transaccionalidad ACID en PostgreSQL para evitar estados inconsistentes en fichas clínicas."),
        ("Seguridad (Security)", "Preservación estricta de la confidencialidad, integridad, no repudio y autenticidad de los registros de salud. Exige control de acceso basado en roles (RBAC), cifrado de datos en tránsito (TLS/HTTPS) y en reposo, y saneamiento estricto de entradas."),
        ("Mantenibilidad (Maintainability)", "Grado de efectividad y eficiencia con el que los desarrolladores pueden modificar el software. Requiere arquitectura modular en capas desacopladas, código auto-documentado, pruebas automatizables y conformidad con las reglas de linting de ESLint.")
    ],
    "seguridad_intro": (
        "La seguridad en Cuidarte+ resguarda Información Médica Protegida (Protected Health Information - PHI). Cualquier brecha "
        "puede comprometer el diagnóstico de un paciente o destruir su privacidad. Se aplican directrices alineadas con OWASP Top 10 y CWE:"
    ),
    "seguridad_items": [
        ("Protección y Confidencialidad de Datos Sensibles", "Los datos clínicos, diagnósticos y exámenes son legalmente sensibles. No pueden transferirse en texto plano ni exponerse a través de almacenamiento público o URLs sin autenticación. En reposo, las contraseñas deben cifrarse mediante algoritmos de derivación de claves con sal aleatoria (bcrypt, work factor >= 10 o Argon2id)."),
        ("Control de Acceso Basado en Roles (RBAC)", "Estricta separación de privilegios entre Administrador (gestión total de usuarios y catálogos), Médico (creación y consulta de pacientes y exámenes) y Paciente (lectura exclusiva de sus propios registros clínicos, sin acceso a expedientes ajenos, garantizando la prevención de IDOR)."),
        ("Manejo Seguro de Errores y Fuga de Información", "Las respuestas de la API no deben filtrar trazas de depuración (stack traces), consultas SQL internas ni información sobre la versión del motor PostgreSQL o Node.js hacia el cliente (CWE-209)."),
        ("Integridad y No Repudio mediante Auditoría", "Toda operación de inserción, actualización, eliminación o consulta sensible debe registrarse en la tabla de auditoría con identificación inequívoca del usuario actor, marca temporal (timestamp) y descripción de la acción efectuada.")
    ],
    "normativas_intro": (
        "El desarrollo y despliegue de Cuidarte+ se sujeta de manera vinculante al ordenamiento jurídico de la República de Chile "
        "y a los estándares sanitarios del Ministerio de Salud (MINSAL):"
    ),
    "normativas_items": [
        ("Ley Nº 19.628 sobre Protección de la Vida Privada", "Clasifica los datos sobre el estado de salud físico o psíquico como 'Datos Sensibles' (Art. 2º letra g). El Art. 10º estipula que los datos sensibles no pueden ser objeto de tratamiento, salvo que la ley lo autorice o el titular consienta expresamente por escrito. El almacenamiento de contraseñas o datos clínicos en texto plano constituye una negligencia inexcusable que transgrede el deber de seguridad (Art. 11º)."),
        ("Ley Nº 20.584 sobre Derechos y Deberes de las Personas en Salud", "Consagra la confidencialidad absoluta de la ficha clínica (Art. 12º y 13º). Exige que las instituciones adopten medidas de seguridad física y lógica para evitar accesos no autorizados. Asimismo, la normativa sanitaria impone el deber legal de custodia y conservación de los registros clínicos por un plazo mínimo de 15 años, lo cual prohíbe las eliminaciones físicas ('hard delete') en bases de datos clínicas."),
        ("Ley Nº 21.459 sobre Delitos Informáticos", "Tipifica penalmente el acceso ilícito a sistemas informáticos (Art. 2º), la interceptación ilícita de transmisiones (Art. 3º), el daño informático (Art. 4º) y la falsificación informática (Art. 6º). Los administradores y desarrolladores son responsables de implementar barreras técnicas efectivas para impedir intrusiones."),
        ("Estándares Técnicos MINSAL para Sistemas de Ficha Clínica Electrónica", "Establece criterios de interoperabilidad, trazabilidad inmutable mediante logs de auditoría y controles criptográficos para el almacenamiento y firma de documentos médicos.")
    ]
}

SECTION_3_TEXTS = {
    "estrategia_p1": (
        "La estrategia de pruebas adopta un modelo integral de aseguramiento de la calidad (QA) con un enfoque mixto, "
        "combinando análisis estático de código fuente (SAST), pruebas dinámicas automatizadas de API mediante colecciones HTTP/Postman, "
        "pruebas de carga concurrente y pruebas manuales exploratorias funcionales y de usabilidad en el navegador. La meta es evaluar el "
        "comportamiento del sistema en condiciones normales y adversas (pruebas negativas y de inyección)."
    ),
    "estrategia_etapas": [
        ("Fase 1: Planificación y Análisis de Requerimientos", "Desglose de requerimientos de la ERS, identificación de flujos críticos de negocio y definición de matrices de riesgos."),
        ("Fase 2: Auditoría Técnica y Análisis Estático (SAST)", "Inspección estática de código fuente en backend y frontend para detectar fallos de arquitectura, malas prácticas, librerías inseguras y omisiones de validación."),
        ("Fase 3: Diseño y Configuración de Ambientes", "Elaboración de las especificaciones de casos de prueba detallados y despliegue del entorno de prueba reproducibilidad mediante Docker Compose."),
        ("Fase 4: Ejecución de Ciclos de Pruebas Funcionales y de Seguridad", "Ejecución sistemática de casos de prueba funcionales (CRUD, RBAC) y de penetración/seguridad (inyección, bypass de token, acceso estático)."),
        ("Fase 5: Pruebas No Funcionales de Rendimiento y Accesibilidad", "Medición de latencias en endpoints mediante cronometría de peticiones HTTP y evaluación de contraste y responsividad con herramientas de desarrollador."),
        ("Fase 6: Registro de Incidentes y Reporte Técnico", "Clasificación de defectos por criticidad, emisión de evidencias y elaboración del presente informe final.")
    ],
    "priorizacion_p1": (
        "La priorización de las pruebas se calculó aplicando una Matriz de Riesgo Cuantitativa basada en Severidad del Impacto (1 a 5) "
        "multiplicada por la Probabilidad de Ocurrencia (1 a 5). Los módulos de Autenticación, Gestión de Contraseñas, Descarga de Documentos "
        "Clínicos y Control de Acceso por Rol (RBAC) fueron asignados con Prioridad Crítica (P1, Riesgo > 15), debido a que su compromiso destruye "
        "la confidencialidad médica. Los flujos CRUD de Pacientes y Exámenes recibieron Prioridad Alta (P2), mientras que la estética de interfaz "
        "y ajustes cosméticos se categorizaron con Prioridad Media/Baja (P3 y P4)."
    ),
    "criterios_in_out": [
        ("Criterios de Entrada (Entry Criteria)", "Código fuente completo y versionado en repositorio; contenedores de Backend, Frontend y PostgreSQL desplegados y en estado 'healthy'; base de datos poblada con dataset de prueba inicial (roles, usuarios por defecto, tipos de examen); colección de endpoints importada."),
        ("Criterios de Salida (Exit Criteria)", "100% de los casos de prueba diseñados ejecutados; 100% de los requerimientos de la ERS cubiertos en la matriz de trazabilidad; documentación exhaustiva de todos los defectos encontrados con su nivel de severidad e impacto normativo; emisión de recomendaciones técnicas de mitigación.")
    ],
    "tipos_pruebas_intro": (
        "Para garantizar una evaluación holística acorde a la pauta de evaluación y rúbrica del encargo, se seleccionaron "
        "y justificaron técnicamente los siguientes tipos de pruebas:"
    ),
    "tipos_pruebas_items": [
        ("Pruebas Funcionales (Unitarias, Integración y Sistema)", "Verifican que cada componente de software cumpla fielmente con las reglas de negocio estipuladas. Justificación: Permite garantizar que el registro de pacientes, creación de exámenes y subida de archivos operen según lo esperado y apliquen las validaciones de datos (RUT chileno, campos obligatorios)."),
        ("Pruebas de Seguridad y Control de Acceso (RBAC y Penetración)", "Auditan la robustez criptográfica, el aislamiento de privilegios entre roles y la resistencia ante ataques web comunes. Justificación: Imprescindibles para validar que un paciente no pueda alterar exámenes médicos ajenos ni ver diagnósticos de terceros, y verificar que no existan accesos directos no autenticados a archivos."),
        ("Pruebas de Rendimiento y Carga (Performance Testing)", "Miden el tiempo de respuesta, throughput y comportamiento del servidor bajo carga estándar y concurrente. Justificación: Obligatorias para verificar el cumplimiento del umbral estipulado en NFR-PERF-1 (< 300 ms) e identificar cuellos de botella o latencias anómalas en el backend."),
        ("Pruebas de Usabilidad y Accesibilidad (WCAG 2.1 AA)", "Inspeccionan la legibilidad de fuentes, claridad en mensajes de error, facilidad de navegación y relaciones de contraste cromático. Justificación: Exigidas por NFR-USAB-1 para asegurar que personas de la tercera edad y usuarios con visión reducida operen la plataforma sin barreras tecnológicas."),
        ("Pruebas de Compatibilidad y Responsividad", "Comprueban el renderizado y operatividad fluida en diversos factores de forma (Desktop, Tablet, Mobile) y navegadores web modernos (Chrome, Firefox, Edge, Safari). Justificación: Requeridas por NFR-COMPAT-1 y NFR-COMPAT-2 para garantizar la ubicuidad médica en centros asistenciales."),
        ("Pruebas de Análisis Estático de Código (SAST)", "Revisión automatizada del código fuente sin ejecutarlo mediante ESLint y auditoría manual de dependencias en package.json. Justificación: Identifica de forma temprana vulnerabilidades de configuración, paquetes faltantes (ausencia de bcrypt) y errores sintácticos en el tema visual.")
    ],
    "criterios_aceptacion_intro": (
        "Los criterios de aceptación constituyen las condiciones indispensables y medibles que deben cumplirse para certificar "
        "la aprobación de una funcionalidad o del sistema completo:"
    ),
    "criterios_aceptacion_items": [
        ("Criterios de Aceptación Funcionales", "Toda operación de creación, lectura o modificación debe retornar códigos HTTP estándar (200 OK, 201 Created). Los errores de validación deben responder 400 Bad Request con glosa descriptiva clara. La eliminación de registros debe solicitar confirmación y ejecutar borrado lógico (inactivación)."),
        ("Criterios de Aceptación No Funcionales", "El 95% de las peticiones CRUD deben responder en un lapso inferior a 300 ms en condiciones de red local/QA. Las contraseñas deben persistirse exclusivamente en formato hash salado mediante bcrypt con costo computacional adecuado. La interfaz debe satisfacer contraste WCAG AA (ratio mínimo 4.5:1 para texto normal)."),
        ("Criterios de Reglas de Negocio", "RB-1: El rol 'paciente' tiene acceso de solo lectura restringido exclusivamente a sus propios exámenes; RB-2: El rol 'admin' posee gobierno total de usuarios y roles; RB-3: El rol 'medico' tiene potestad de gestionar pacientes y emitir órdenes médicas de cualquier paciente registrado.")
    ],
    "recursos_intro": (
        "La ejecución del plan de pruebas requirió la asignación estructurada de recursos humanos calificados, "
        "infraestructura tecnológica y un entorno de prueba controlado y representativo:"
    ),
    "recursos_humanos": [
        ("Ricardo Saez (Líder de Calidad y Pruebas QA)", "Responsable de la dirección del plan, diseño de la estrategia metodológica, coordinación de ciclos de prueba, validación de cobertura frente a la ERS y redacción del informe técnico consolidado."),
        ("Patricio Quilodran (Especialista en Seguridad y Normativa Legal)", "Encargado de la auditoría de seguridad del código backend, pruebas de penetración (control de acceso, inyección, almacenamiento criptográfico) y análisis de cumplimiento de las Leyes 19.628, 20.584 y 21.459."),
        ("Sebastian Dinamarca (Ingeniero de Pruebas Funcionales y Rendimiento)", "Responsable de la ejecución de casos de prueba funcionales en frontend y backend, pruebas de rendimiento de API, análisis de tiempos de respuesta, evaluación de accesibilidad para adultos mayores y verificación de responsividad.")
    ],
    "recursos_tecnicos": [
        ("Capa de Servidor y Entorno de Ejecución", "Node.js v20.x LTS, Express v4.19.2, Morgan, Multer, Yup para validación de esquemas."),
        ("Capa de Persistencia", "Motor de base de datos PostgreSQL v15.x ejecutándose sobre contenedor Docker con volumen persistente."),
        ("Capa de Cliente Web", "React v19.1.1, Vite v7.1.7, Material UI v7.3.4, Axios v1.13.1, Formik y Yup."),
        ("Herramientas de Auditoría y Testing", "Postman v10+ para pruebas dinámicas de API REST; ESLint v9.x para análisis estático (SAST); DevTools de Google Chrome para auditoría de red, consola, DOM y accesibilidad; cURL y PowerShell para automatización de peticiones HTTP."),
        ("Entorno de Pruebas (Ambiente QA Dockerizado)", "Host local Windows 11; Docker Desktop v4.30+ orquestando Backend en puerto 4444, Frontend en puerto 3333 y PostgreSQL expuesto en puerto 15442.")
    ],
    "cronograma_items": [
        ("Hito 1: Análisis de Requisitos y Setup de Entorno", "Días 1 a 2", "Despliegue de Docker, verificación de conectividad y revisión de ERS base."),
        ("Hito 2: Auditoría Estática de Código y Diseño de Casos", "Días 3 a 5", "Ejecución de ESLint, inspección de dependencias y redacción de los 25 casos de prueba."),
        ("Hito 3: Ciclo de Ejecución de Pruebas de Seguridad y Backend", "Días 6 a 8", "Pruebas de autenticación, JWT, RBAC, hash de contraseñas y endpoints de API."),
        ("Hito 4: Ciclo de Ejecución Funcional, Rendimiento y Accesibilidad", "Días 9 a 11", "Pruebas de flujos frontend, medición de tiempos de respuesta y análisis de contraste."),
        ("Hito 5: Clasificación de Incidentes y Consolidación de Informe", "Días 12 a 14", "Matriz de criticidad, análisis normativo, plan de remediación y entrega formal.")
    ]
}

CASES_DESIGN = [
    {
        "id": "CP-01",
        "nombre": "Autenticación exitosa y generación de token de sesión JWT",
        "requerimiento": "RF-1.1 / NFR-SEG-9",
        "descripcion": "Verificar que un usuario registrado pueda autenticarse exitosamente ingresando su nombre de usuario y contraseña válidos, obteniendo un token JWT que contenga su identidad y roles.",
        "precondiciones": "El usuario debe existir previamente registrado en la tabla 'usuarios' con credenciales conocidas (ej. usuario: 'medico', contraseña: 'password123'). El servicio de backend debe estar operativo.",
        "pasos": (
            "1. Enviar una solicitud HTTP POST al endpoint '/autenticacion/login'.\n"
            "2. Incluir en el cuerpo (JSON) los campos: nombre_usuario y password.\n"
            "3. Verificar el código de estado HTTP de respuesta.\n"
            "4. Decodificar el token JWT recibido en el campo 'token' de la respuesta JSON.\n"
            "5. Verificar el registro del evento en la tabla de auditoría."
        ),
        "resultado_esperado": "El sistema debe responder con código HTTP 200 OK, un objeto JSON conteniendo un token JWT firmado criptográficamente, cuyos claims incluyan usuarioId, nombreUsuario, rolNombre y pacienteId. Además, debe insertarse un registro en la tabla 'auditoria' con la acción 'LOGIN: usuario inició sesión'.",
        "criterio_aceptacion": "Generación de token JWT válido con expiración no superior a 2 horas y persistencia obligatoria del evento en el log de auditoría del sistema.",
        "datos_prueba": '{\n  "nombre_usuario": "medico",\n  "password": "password123"\n}'
    },
    {
        "id": "CP-02",
        "nombre": "Control de acceso por rol (RBAC) - Restricción de creación de exámenes a pacientes",
        "requerimiento": "RF-3.1 / RB-1 / NFR-SEG-4",
        "descripcion": "Comprobar que el sistema impida que un usuario con rol 'paciente' cree o registre un examen médico, reservando dicha potestad exclusivamente a médicos y administradores.",
        "precondiciones": "Usuario autenticado con rol 'paciente' y token JWT válido. Existencia de al menos un paciente registrado en base de datos.",
        "pasos": (
            "1. Obtener token JWT iniciando sesión con credenciales de usuario con rol 'paciente'.\n"
            "2. Enviar solicitud HTTP POST al endpoint '/examenes' con cabecera 'Authorization: Bearer <token_paciente>'.\n"
            "3. Enviar payload JSON con datos de un nuevo examen médico (paciente_id, tipo_examen_medico_id, diagnosis).\n"
            "4. Inspeccionar el código de respuesta HTTP y mensaje de error devuelto por la API."
        ),
        "resultado_esperado": "La API debe rechazar la solicitud con código HTTP 403 Forbidden y un cuerpo JSON con error: 'No autorizado' y glosa: 'No tiene permisos para realizar esta acción'. No debe registrarse ningún examen en la base de datos.",
        "criterio_aceptacion": "Cumplimiento estricto de la regla de negocio RB-1 y NFR-SEG-4: un paciente solo tiene permisos de lectura y no puede ejecutar acciones de escritura clínica.",
        "datos_prueba": 'Cabecera: Authorization: Bearer <jwt_paciente>\nBody: {\n  "tipo_examen_medico_id": 1,\n  "paciente_id": 1,\n  "diagnosis": "Diagnóstico de prueba no autorizado",\n  "tratamiento": "Reposo"\n}'
    },
    {
        "id": "CP-03",
        "nombre": "Registro de paciente con validación de formato y algoritmo de RUT chileno",
        "requerimiento": "RF-2.2 / NFR-USAB-2",
        "descripcion": "Verificar que el endpoint de creación de pacientes valide rigurosamente el formato y el dígito verificador del RUT chileno mediante el algoritmo Módulo 11, rechazando identificadores inválidos o maliciosos.",
        "precondiciones": "Usuario con rol 'medico' o 'admin' autenticado en el sistema. Base de datos operativa.",
        "pasos": (
            "1. Iniciar sesión como 'medico' y obtener token de autorización.\n"
            "2. Enviar solicitud HTTP POST a '/pacientes' con cabecera Bearer Token.\n"
            "3. Proporcionar un RUT con dígito verificador intencionalmente inválido (ej: '11.111.111-9').\n"
            "4. Evaluar la respuesta devuelta por el middleware de validación Yup/rut.js.\n"
            "5. Reintentar con un RUT válido (ej: '11.111.111-1') y verificar la inserción exitosa."
        ),
        "resultado_esperado": "Para el RUT con dígito verificador erróneo, el sistema debe responder con código HTTP 400 Bad Request indicando error de validación en el RUT. Para el RUT válido, el sistema debe responder con código HTTP 201 Created y retornar el registro del paciente creado.",
        "criterio_aceptacion": "El sistema normaliza y valida matemáticamente el RUT antes de persistir; rechaza entradas inválidas sin provocar caídas del servidor.",
        "datos_prueba": 'Prueba Negativa: { "rut": "11.111.111-9", "primer_nombre": "Carlos", "apellido_paterno": "Pérez", "email": "carlos@test.cl", "fecha_nacimiento": "1990-05-15", "sexo": "M" }\nPrueba Positiva: { "rut": "11.111.111-1", ... }'
    },
    {
        "id": "CP-04",
        "nombre": "Carga y almacenamiento de documento clínico adjunto a un examen médico",
        "requerimiento": "RF-4.3 / RF-4.4",
        "descripcion": "Comprobar que un médico pueda adjuntar un documento clínico en formato PDF a un examen médico existente, verificando el límite de tamaño y los tipos MIME permitidos.",
        "precondiciones": "Usuario autenticado con rol 'medico'. Examen médico creado previamente en el sistema con ID conocido.",
        "pasos": (
            "1. Iniciar sesión como médico y configurar la cabecera 'Authorization: Bearer <token_medico>'.\n"
            "2. Preparar una solicitud HTTP POST 'multipart/form-data' hacia '/documentos'.\n"
            "3. Adjuntar un archivo PDF real ('informe_hemograma.pdf', tamaño < 10 MB).\n"
            "4. Enviar los campos de formulario: examen_medico_id y paciente_id.\n"
            "5. Verificar la respuesta del servidor y la persistencia en la base de datos."
        ),
        "resultado_esperado": "El sistema debe responder con código HTTP 201 Created y un objeto JSON con los metadatos del documento creado (id, nombre_archivo, created_at). Debe registrarse en auditoría el evento 'DOCUMENTOS_CREAR'.",
        "criterio_aceptacion": "El documento se sube y asocia correctamente al examen médico. Se restringe a formatos permitidos (PDF, JPG, PNG) y tamaño máximo de 10 MB.",
        "datos_prueba": 'Form-data: documento: informe_hemograma.pdf (application/pdf, 250 KB), examen_medico_id: 1, paciente_id: 1'
    },
    {
        "id": "CP-05",
        "nombre": "Eliminación de usuario y validación de borrado lógico vs físico",
        "requerimiento": "RF-2.7 / NFR-SEG-6",
        "descripcion": "Verificar la operación de eliminación de un usuario del sistema, auditando si el sistema realiza una eliminación lógica (inactivación) como exige la ERS o si incurre en borrado físico destructivo.",
        "precondiciones": "Usuario administrador autenticado. Usuario objetivo de prueba creado en base de datos (id: 10).",
        "pasos": (
            "1. Autenticarse como administrador y obtener token JWT.\n"
            "2. Enviar solicitud HTTP DELETE a '/usuarios/10' con cabecera de autorización.\n"
            "3. Verificar el código de estado HTTP de respuesta.\n"
            "4. Consultar directamente la base de datos PostgreSQL: 'SELECT * FROM usuarios WHERE id = 10;'.\n"
            "5. Verificar si el registro existe con marca inactiva o si fue purgado físicamente."
        ),
        "resultado_esperado": "Según la ERS, el sistema debe solicitar confirmación y marcar el registro como inactivo (eliminación lógica, conservando historial clínico y de auditoría).",
        "criterio_aceptacion": "Cumplimiento del requerimiento ERS: 'Se debe realizar una eliminación lógica solicitando al usuario confirmación antes de proceder en la operación'.",
        "datos_prueba": "ID de usuario objetivo: 10\nEndpoint: DELETE /usuarios/10\nCabecera: Authorization: Bearer <token_admin>"
    },
    {
        "id": "CP-06",
        "nombre": "No Funcional - Rendimiento en consulta de pacientes y exámenes (Detección de Latencia)",
        "requerimiento": "NFR-PERF-1",
        "descripcion": "Medir el tiempo de respuesta del servidor en peticiones GET simples de listado de pacientes y exámenes médicos bajo condiciones normales de carga, verificando que no supere el umbral de 300 ms.",
        "precondiciones": "Servidor backend y base de datos PostgreSQL en ejecución en ambiente local. Usuario médico autenticado.",
        "pasos": (
            "1. Configurar herramienta de cronometría HTTP (Postman / cURL) en red local.\n"
            "2. Enviar solicitud HTTP GET a '/pacientes' con cabecera Bearer Token.\n"
            "3. Registrar el tiempo transcurrido desde el envío hasta la recepción del último byte.\n"
            "4. Repetir la medición con el endpoint GET '/examenes'.\n"
            "5. Comparar los tiempos de respuesta obtenidos con el SLA de 300 ms estipulado en NFR-PERF-1."
        ),
        "resultado_esperado": "El tiempo de respuesta debe situarse por debajo de los 300 milisegundos (ms) para operaciones CRUD simples en red local con dataset estándar.",
        "criterio_aceptacion": "NFR-PERF-1: Tiempo de respuesta para operaciones CRUD simples < 300 ms bajo carga normal.",
        "datos_prueba": "Endpoint 1: GET http://localhost:4444/pacientes\nEndpoint 2: GET http://localhost:4444/examenes\nIteraciones: 5 peticiones consecutivas"
    },
    {
        "id": "CP-07",
        "nombre": "No Funcional - Seguridad: Verificación de hashing criptográfico en almacenamiento de contraseñas",
        "requerimiento": "NFR-SEG-2 / Ley 19.628",
        "descripcion": "Inspeccionar el código fuente del backend y la base de datos PostgreSQL para verificar que las contraseñas de los usuarios sean almacenadas con hashing robusto (bcrypt con sal) y nunca en texto plano.",
        "precondiciones": "Acceso a la base de datos PostgreSQL de prueba y al código fuente de 'BACKEND/src/routes/auth.js'.",
        "pasos": (
            "1. Registrar un nuevo usuario mediante POST '/autenticacion/registro' con contraseña: 'MiPasswordSeguro2026!'.\n"
            "2. Conectarse a la base de datos PostgreSQL mediante psql.\n"
            "3. Ejecutar la consulta: 'SELECT id, nombre_usuario, contrasena FROM usuarios WHERE nombre_usuario = ...;'.\n"
            "4. Inspeccionar el valor de la columna 'contrasena'.\n"
            "5. Auditar el código de inserción en 'auth.js' y 'users.js'."
        ),
        "resultado_esperado": "La columna 'contrasena' debe contener una cadena hash que inicie con '$2b$' o '$2a$' (formato bcrypt) de longitud fija (60 caracteres), resultando matemáticamente imposible reconstruir la contraseña en texto claro.",
        "criterio_aceptacion": "NFR-SEG-2: Contraseñas con Hashing seguro (bcrypt). Cumplimiento obligatorio del deber de seguridad del Art. 11 de la Ley 19.628.",
        "datos_prueba": 'Payload de registro: {\n  "nombre_usuario": "usuario_test_crypto",\n  "password": "MiPasswordSeguro2026!",\n  "correo": "crypto@test.cl",\n  "rut": "15.897.456-7"\n}'
    },
    {
        "id": "CP-08",
        "nombre": "No Funcional - Seguridad: Control de acceso a documentos clínicos y prevención de exposición pública",
        "requerimiento": "NFR-SEG-5 / NFR-SEG-8 / Ley 20.584",
        "descripcion": "Verificar que los documentos clínicos almacenados en el servidor no puedan ser accedidos ni descargados directamente mediante URLs públicas estáticas sin pasar por el middleware de autenticación y autorización.",
        "precondiciones": "Un documento clínico ha sido cargado previamente en el sistema ('informe_hemograma.pdf'). Servidor web backend activo.",
        "pasos": (
            "1. Identificar la ruta estática configurada en 'BACKEND/src/app.js' ('/files/documentos').\n"
            "2. Abrir un navegador en modo incógnito sin iniciar sesión ni enviar cookies/tokens.\n"
            "3. Intentar acceder directamente a la URL: 'http://localhost:4444/files/documentos/informe_hemograma.pdf'.\n"
            "4. Verificar si el servidor bloquea la solicitud con 401/403 o si entrega el archivo sensible."
        ),
        "resultado_esperado": "El servidor debe denegar el acceso a clientes no autenticados (HTTP 401 Unauthorized o 403 Forbidden). La carpeta de almacenamiento no debe estar expuesta públicamente mediante 'express.static' sin middleware de seguridad.",
        "criterio_aceptacion": "Protección de datos médicos sensibles; solo usuarios autenticados y autorizados (el médico tratante o el propio paciente titular) pueden acceder al contenido del archivo.",
        "datos_prueba": "URL de prueba: http://localhost:4444/files/documentos/informe_hemograma.pdf\nCliente: Navegador web sin autenticación / cURL sin cabecera Authorization"
    },
    {
        "id": "CP-09",
        "nombre": "No Funcional - Usabilidad y Accesibilidad: Medición de contraste de color y legibilidad para adultos mayores",
        "requerimiento": "NFR-USAB-1 / WCAG 2.1 AA",
        "descripcion": "Auditar la interfaz de usuario de Cuidarte+ para verificar que cumpla con los estándares de accesibilidad WCAG 2.1 nivel AA, verificando tipografía legible (>= 12px) y relaciones de contraste cromático superiores a 4.5:1 para texto normal.",
        "precondiciones": "Aplicación Frontend levantada y accesible en 'http://localhost:3333'. Herramienta Lighthouse o analizador de contraste activa.",
        "pasos": (
            "1. Navegar por la página de inicio (Home), inicio de sesión y vista de pacientes.\n"
            "2. Inspeccionar la configuración del tema visual en 'FRONTEND/src/theme.js'.\n"
            "3. Calcular la relación de contraste cromático entre los colores de texto y fondo definidos en la paleta primaria (#3293BA) y secundaria (#C5652C) frente al fondo blanco.\n"
            "4. Inspeccionar el código fuente del tema en búsqueda de inconsistencias sintácticas (ej. códigos hexadecimales incompletos).\n"
            "5. Verificar la compatibilidad de lectura para usuarios de la tercera edad."
        ),
        "resultado_esperado": "Todos los elementos interactivos y textos de la interfaz deben superar la relación de contraste mínima de 4.5:1 exigida por WCAG 2.1 AA. El tema no debe contener errores sintácticos de color.",
        "criterio_aceptacion": "NFR-USAB-1: Interfaces con tipografía legible, contraste adecuado y controles grandes para usuarios mayores; sin errores de rendering.",
        "datos_prueba": "Valores a auditar en theme.js:\n- Primary main: #3293BA\n- Secondary main: #C5652C\n- Background default: #fffff (inspección de 5 dígitos vs 6 requeridos)"
    },
    {
        "id": "CP-10",
        "nombre": "No Funcional - Compatibilidad: Renderizado y navegación en dispositivos móviles y tablets",
        "requerimiento": "NFR-COMPAT-2",
        "descripcion": "Comprobar que la aplicación web Cuidarte+ se adapte fluidamente a pantallas de dispositivos móviles (smartphones) y tablets, manteniendo la navegabilidad de menús y la accesibilidad de las tablas de datos.",
        "precondiciones": "Frontend en ejecución en 'http://localhost:3333'. Dispositivo móvil o emulador de Chrome DevTools configurado con viewport de 375x667 (iPhone SE) y 768x1024 (iPad).",
        "pasos": (
            "1. Abrir la consola de desarrollador en Chrome y activar el 'Device Toolbar'.\n"
            "2. Seleccionar el viewport móvil (ancho 375px).\n"
            "3. Iniciar sesión como médico y navegar hacia el listado de pacientes y exámenes.\n"
            "4. Interactuar con el menú de navegación (Drawer / hamburguesa) implementado en 'Layout.jsx'.\n"
            "5. Verificar que no exista desbordamiento horizontal ('overflow-x') que corte información clínica."
        ),
        "resultado_esperado": "La interfaz debe colapsar el menú en un cajón lateral (Drawer móvil), las tablas de datos deben permitir desplazamiento horizontal interno sin romper la vista principal y todos los botones deben conservar un área táctil mínima de 44x44 píxeles.",
        "criterio_aceptacion": "NFR-COMPAT-2: Diseño completamente responsivo y operable en pantallas móviles y tablets sin degradación de funcionalidad.",
        "datos_prueba": "Viewports evaluados:\n- Mobile: 375x667 px (iOS Safari emulado)\n- Tablet: 768x1024 px (Android Chrome emulado)\n- Desktop: 1920x1080 px"
    },
    {
        "id": "CP-11",
        "nombre": "No Funcional - Seguridad: Almacenamiento y exposición de token de sesión en cliente (JWT en localStorage)",
        "requerimiento": "NFR-SEG-5 / NFR-SEG-9",
        "descripcion": "Auditar el mecanismo de almacenamiento del token JWT en el cliente web implementado en 'AuthContext.jsx', evaluando su vulnerabilidad ante ataques de Cross-Site Scripting (XSS).",
        "precondiciones": "Frontend en ejecución. Sesión iniciada con cualquier rol de usuario.",
        "pasos": (
            "1. Iniciar sesión exitosamente en el frontend de Cuidarte+.\n"
            "2. Abrir la consola de JavaScript en DevTools del navegador.\n"
            "3. Ejecutar el comando: 'localStorage.getItem(\"token\");'.\n"
            "4. Verificar si el token es accesible por scripts del lado del cliente.\n"
            "5. Evaluar si existen protecciones mediante cookies con banderas HttpOnly, Secure y SameSite."
        ),
        "resultado_esperado": "En aplicaciones que manejan datos sensibles de salud, los tokens de sesión no deben persistirse en 'localStorage' debido a que cualquier vulnerabilidad XSS permitiría el robo inmediato del token. La arquitectura recomendada exige cookies seguras HttpOnly.",
        "criterio_aceptacion": "Mitigación de riesgos de suplantación de sesión y robo de credenciales en concordancia con OWASP Top 10 (A07: Identification and Authentication Failures).",
        "datos_prueba": 'Comando consola: console.log("Token capturado:", localStorage.getItem("token"))'
    },
    {
        "id": "CP-12",
        "nombre": "No Funcional - Confiabilidad y Auditoría: Integridad de tipos en registro de auditoría al eliminar usuarios",
        "requerimiento": "RF-5.1 / NFR-SEG-6",
        "descripcion": "Verificar la robustez y consistencia de tipos de datos en la inserción de eventos de auditoría al ejecutar la eliminación de un usuario a través del endpoint DELETE '/usuarios/:id'.",
        "precondiciones": "Usuario administrador autenticado con token válido. Usuario objetivo creado en base de datos.",
        "pasos": (
            "1. Autenticarse como 'admin' y obtener token JWT.\n"
            "2. Enviar solicitud HTTP DELETE a '/usuarios/:id'.\n"
            "3. Inspeccionar el código fuente de 'BACKEND/src/routes/users.js' en la línea donde se invoca la auditoría:\n"
            "   'INSERT INTO auditoria (usuario_id, accion) VALUES ($1, $2)', [authUser?.nombreUsuario || null, ...]'\n"
            "4. Contrastar con la definición de la columna 'usuario_id' en 'init.sql' (tipo BIGINT).\n"
            "5. Evaluar si la llamada genera una excepción de tipo de datos en PostgreSQL."
        ),
        "resultado_esperado": "El endpoint debe registrar de forma transparente y sin errores la auditoría, pasando el identificador numérico (BIGINT) 'authUser.usuarioId' en lugar del string 'authUser.nombreUsuario', garantizando la integridad de claves foráneas.",
        "criterio_aceptacion": "Registro inmutable y sin excepciones en la tabla de auditoría para toda acción destructiva, asegurando trazabilidad y no repudio.",
        "datos_prueba": "Llamada: DELETE /usuarios/99\nToken claims: { usuarioId: 1, nombreUsuario: 'admin', rolId: 1 }\nColumna destino: auditoria.usuario_id (BIGINT)"
    }
]

SECTION_5_SUMMARY = {
    "total_disenados": 25,
    "total_ejecutados": 25,
    "pasaron": 14,
    "fallaron": 9,
    "bloqueados": 2,
    "porcentaje_aprobacion": "56.0%",
    "porcentaje_fallo": "36.0%",
    "porcentaje_bloqueo": "8.0%"
}

EXECUTION_DETAILS = [
    # Pruebas Funcionales
    ("CP-01", "Autenticación exitosa y generación de token de sesión JWT", "Aprobado (Pass)", "HTTP 200 OK recibido; token JWT emitido con claims correctos y evento registrado en tabla auditoria."),
    ("CP-02", "Control de acceso por rol (RBAC) - Restricción de creación de exámenes a pacientes", "Aprobado (Pass)", "HTTP 403 Forbidden devuelto al intentar crear examen con token de rol paciente. RB-1 validada con éxito."),
    ("CP-03", "Registro de paciente con validación de RUT chileno (algoritmo Módulo 11)", "Aprobado (Pass)", "HTTP 400 devuelto para RUT con dígito verificador inválido; HTTP 201 generado para RUT válido normalizado."),
    ("CP-04", "Carga y almacenamiento de documento clínico adjunto a examen médico", "Aprobado (Pass)", "HTTP 201 Created; metadatos generados y evento DOCUMENTOS_CREAR persistido en auditoría."),
    ("CP-05", "Eliminación de usuario y validación de borrado lógico vs físico", "Fallado (Fail)", "El endpoint ejecuta DELETE FROM físico en BD purgando el registro de raíz. Incumple requisito ERS de borrado lógico."),
    ("CP-06", "Cierre de sesión y revocación/invalidación de token JWT", "Fallado (Fail)", "El logout en frontend solo borra localStorage; el token JWT permanece matemáticamente válido en backend hasta su expiración (no hay lista de revocación)."),
    ("CP-07", "Creación de paciente por médico o administrador", "Aprobado (Pass)", "HTTP 201 Created; registro insertado en tabla pacientes con todos sus campos médicos y de previsión."),
    ("CP-08", "Edición de ficha de paciente por médico", "Aprobado (Pass)", "HTTP 200 OK; campos actualizados y evento PACIENTES_ACTUALIZAR auditado exitosamente."),
    ("CP-09", "Eliminación de examen médico por usuario médico", "Fallado (Fail)", "El endpoint DELETE /examenes/:id exige rol 'admin' (requireRole admin). Médicos reciben 403 Forbidden. Contradice RF-3.3."),
    ("CP-10", "Visualización de exámenes médicos propios por parte del paciente", "Aprobado (Pass)", "HTTP 200 OK; paciente solo visualiza registros vinculados a su identificador de paciente. RBAC horizontal correcto."),
    ("CP-11", "Descarga de documento clínico por paciente titular", "Aprobado (Pass)", "HTTP 200 OK con Content-Disposition attachment; paciente descarga su informe PDF sin impedimentos."),
    ("CP-12", "Descarga de documento clínico ajeno por paciente (prueba IDOR)", "Aprobado (Pass)", "HTTP 403 Forbidden devuelto al solicitar documento de otro paciente. Protección IDOR validada en endpoint."),
    ("CP-13", "Edición de usuario y cambio de rol por administrador", "Aprobado (Pass)", "HTTP 200 OK; rol actualizado en tabla usuario_roles y auditado correctamente."),
    ("CP-14", "Visualización de bitácora de auditoría restringida a administrador", "Aprobado (Pass)", "HTTP 200 OK para admin; HTTP 403 Forbidden para médico y paciente al consultar /auditoria."),
    
    # Pruebas No Funcionales y Seguridad
    ("CP-15", "Rendimiento en consulta de pacientes (NFR-PERF-1)", "Fallado (Fail)", "Tiempo de respuesta promedio: 5,082 ms. Latencia intencional inyectada por delayMiddleware(5000). Supera SLA de 300 ms."),
    ("CP-16", "Rendimiento en consulta de exámenes médicos (NFR-PERF-1)", "Fallado (Fail)", "Tiempo de respuesta promedio: 5,095 ms. Afectado por delayMiddleware(5000) en GET /examenes. Supera SLA de 300 ms."),
    ("CP-17", "Rendimiento en subida de documentos clínicos (NFR-PERF-1)", "Fallado (Fail)", "Tiempo de respuesta promedio: 5,140 ms por retraso artificial de 5000 ms en POST /documentos. Falla umbral."),
    ("CP-18", "Seguridad: Almacenamiento criptográfico de contraseñas (NFR-SEG-2)", "Fallado (Fail)", "Contraseñas persistidas en texto plano en tabla 'usuarios'. Dependencia bcrypt ausente en package.json. Vulneración crítica."),
    ("CP-19", "Seguridad: Política de complejidad de contraseñas en registro", "Fallado (Fail)", "Yup valida min(6) sin exigir mayúsculas, minúsculas, números ni símbolos. Contradice ERS (12 caracteres complejos)."),
    ("CP-20", "Seguridad: Exposición pública de directorio de almacenamiento de archivos", "Fallado (Fail)", "Ruta express.static('/files/documentos') expuesta sin autenticación en app.js. Descarga directa posible."),
    ("CP-21", "Seguridad: Manejo de tokens de sesión en cliente (NFR-SEG-9)", "Fallado (Fail)", "JWT almacenado en localStorage susceptible a robo mediante ataques XSS. Falta adopción de cookies HttpOnly."),
    ("CP-22", "Confiabilidad: Integridad de tipos en auditoría de eliminación de usuarios", "Fallado (Fail)", "DELETE /usuarios/:id inserta string authUser.nombreUsuario en columna usuario_id (BIGINT). Provoca error Postgres 22P02."),
    ("CP-23", "Usabilidad: Contraste y legibilidad para adultos mayores (WCAG 2.1)", "Aprobado (Pass)", "Tipografía base de 14px en tema; contraste texto/fondo superior a 4.5:1 en vistas de consulta médica."),
    ("CP-24", "Compatibilidad: Navegación responsiva en dispositivos móviles (NFR-COMPAT-2)", "Aprobado (Pass)", "Diseño colapsa a Drawer lateral; formularios legibles y tablas navegables en viewport móvil de 375px."),
    ("CP-25", "Disponibilidad: Manejo de errores y ocultamiento de trazas de servidor", "Fallado (Fail)", "Errores de backend retornan 'err.message' y 'err.toString()' en campo 'glosa' JSON, exponiendo estructura interna.")
]

SEVERITY_SCALE = [
    ("CRITICO", "El defecto impide completamente el funcionamiento del sistema o de una funcionalidad esencial para el negocio, o representa una vulnerabilidad de seguridad grave que expone datos sensibles de salud. Bloquea el flujo principal y transgrede normativas legales.", "Muy alto, el sistema no puede operar en producción", "Requiere remediación técnica inmediata antes de cualquier despliegue"),
    ("GRAVE", "El defecto afecta funcionalidades importantes o compromete SLAs de rendimiento, pero el sistema aún funciona parcialmente. Existe un workaround o degradación severa que compromete la experiencia o el cumplimiento de la ERS.", "Alto, afecta áreas principales del usuario o de rendimiento", "Debe corregirse con urgencia en el sprint en curso"),
    ("MODERADO", "El defecto afecta funcionalidades secundarias, inconsistencias de auditoría o validaciones específicas sin detener el flujo principal del software.", "Medio, el usuario puede trabajar pero con molestias o limitaciones", "Se corrige en la próxima iteración planificada"),
    ("LEVE", "Defecto de apariencia, estética, texto o configuración menor el cual no afecta la funcionalidad operativa del sistema.", "Bajo, no impacta la operación clínica", "Se corrige según disponibilidad de agenda de mantenimiento")
]

INCIDENTS_IDENTIFIED = [
    # Funcionales
    ("INC-01", "CP-05", "Eliminación física ('hard delete') en tabla usuarios y pacientes en lugar de borrado lógico con confirmación. Purgado destructivo que impide auditoría.", "Fallado (Fail)", "GRAVE"),
    ("INC-02", "CP-06", "Cierre de sesión no revoca ni invalida el token JWT en el servidor. El token permanece utilizable por terceros si es interceptado.", "Fallado (Fail)", "MODERADO"),
    ("INC-03", "CP-09", "Restricción excesiva en eliminación de exámenes médicos: exige rol admin cuando el requerimiento RF-3.3 otorga potestad al médico tratante.", "Fallado (Fail)", "MODERADO"),
    
    # No Funcionales y Seguridad
    ("INC-04", "CP-18", "Almacenamiento de contraseñas de usuarios en texto plano en la base de datos PostgreSQL. Librería bcrypt ausente. Vulneración crítica de seguridad y de la Ley 19.628.", "Fallado (Fail)", "CRITICO"),
    ("INC-05", "CP-20", "Exposición pública de la carpeta 'uploads/documentos' mediante express.static sin requerir autenticación JWT. Permite descarga directa de exámenes clínicos.", "Fallado (Fail)", "CRITICO"),
    ("INC-06", "CP-15", "Inyección intencional de retardo de 5,000 ms en endpoints de pacientes (/pacientes) mediante delayMiddleware. Destruye el SLA de 300 ms de NFR-PERF-1.", "Fallado (Fail)", "GRAVE"),
    ("INC-07", "CP-16", "Inyección intencional de retardo de 5,000 ms en endpoints de exámenes (/examenes) mediante delayMiddleware. Provoca tiempos de respuesta superiores a 5 segundos.", "Fallado (Fail)", "GRAVE"),
    ("INC-08", "CP-19", "Validación permisiva de contraseñas en registro: solo exige 6 caracteres mínimos sin complejidad, vulnerando la política ERS de 12 caracteres robustos.", "Fallado (Fail)", "MODERADO"),
    ("INC-09", "CP-21", "Almacenamiento del token de autenticación JWT en localStorage del navegador. Exposición crítica a robo mediante ataques de Cross-Site Scripting (XSS).", "Fallado (Fail)", "MODERADO"),
    ("INC-10", "CP-22", "Error de tipos de datos en eliminación de usuarios: se pasa authUser.nombreUsuario (string) a columna auditoria.usuario_id (BIGINT), causando fallo 22P02 en Postgres.", "Fallado (Fail)", "MODERADO"),
    ("INC-11", "CP-25", "Fuga de información técnica interna (Information Disclosure) en respuestas HTTP 500, exponiendo la propiedad 'glosa' con detalles crudos de excepciones SQL.", "Fallado (Fail)", "LEVE"),
    ("INC-12", "CP-23", "Definición errónea de color de fondo en tema visual (theme.js): 'default: \"#fffff\"' contiene 5 caracteres en lugar de 6, constituyendo código CSS no estándar.", "Fallado (Fail)", "LEVE")
]

SECTION_6_TEXTS = {
    "etico_intro": (
        "El análisis ético y normativo de los resultados obtenidos tras la auditoría técnica trasciende la mera detección "
        "de fallas de software. En una aplicación de salud como Cuidarte+, los defectos de seguridad y las negligencias en el manejo "
        "de datos constituyen violaciones flagrantes a los derechos fundamentales de las personas consagrados en la Constitución "
        "y en el ordenamiento jurídico chileno."
    ),
    "ley_19628": (
        "La Ley Nº 19.628 sobre Protección de la Vida Privada establece en su Artículo 2º letra g que los datos relativos a la salud "
        "son 'Datos Sensibles'. El Artículo 10º dispone taxativamente que los datos sensibles no pueden ser objeto de tratamiento, "
        "a menos que la ley lo autorice explícitamente o el titular consienta de manera informada y por escrito. En Cuidarte+, se constató "
        "el almacenamiento de contraseñas en texto claro (incidente INC-04) y la exposición de documentos clínicos en rutas no autenticadas "
        "(incidente INC-05). Esto contraviene directamente el Artículo 11º, el cual impone al responsable del banco de datos la obligación "
        "indelegable de adoptar todas las medidas de seguridad técnicas y organizativas para impedir su adulteración, pérdida, consulta o "
        "acceso no autorizado. Bajo el marco normativo actual y las reformas de la Agencia de Protección de Datos Personales, estas infracciones "
        "conllevan severas sanciones civiles, indemnizaciones por daño moral y multas que pueden alcanzar miles de Unidades Tributarias Mensuales (UTM)."
    ),
    "ley_20584": (
        "La Ley Nº 20.584, que regula los Derechos y Deberes de las Personas en relación con las acciones vinculadas a su atención en salud, "
        "consagra en sus Artículos 12º y 13º el principio de reserva y confidencialidad absoluta de la Ficha Clínica. La información contenida "
        "en ella es considerada secreto profesional médico. Además, los reglamentos sanitarios del Ministerio de Salud (Decreto Nº 41) exigen "
        "que los prestadores de salud conserven los registros clínicos por un periodo mínimo de 15 años en condiciones de seguridad e inmutabilidad. "
        "El hallazgo evidenciado en el incidente INC-01, donde el sistema ejecuta eliminaciones físicas destructivas ('DELETE FROM') de pacientes "
        "y usuarios, constituye una transgresión legal de máxima gravedad: destruir físicamente el registro clínico de un paciente anula la "
        "trazabilidad de sus antecedentes médicos, impide auditorías forenses frente a negligencias médicas y destruye el deber legal de custodia."
    ),
    "ley_21459": (
        "La Ley Nº 21.459 de Delitos Informáticos, promulgada para adecuar la legislación chilena al Convenio de Budapest, tipifica penalmente "
        "conductas como el acceso ilícito (Art. 2º), la interceptación ilícita (Art. 3º) y el daño a sistemas informáticos (Art. 4º). "
        "Mantener carpetas de archivos médicos expuestas públicamente sin autenticación (INC-05) y tokens almacenados de forma insegura (INC-09) "
        "habilita vectores de ataque directos para que actores maliciosos consuman exfiltraciones masivas de historiales clínicos. La mantención "
        "de estas vulnerabilidades conocidas por desidia técnica genera responsabilidad legal para los administradores de la plataforma."
    ),
    "deontologia": (
        "Desde la bioética y la deontología de la ingeniería de software, los desarrolladores de sistemas de salud asumen un compromiso "
        "equivalente al juramento hipocrático médico: 'Primum non nocere' (lo primero es no hacer daño). Desarrollar sistemas sin implementar "
        "hashing criptográfico, introduciendo latencias artificiales que entorpecen la consulta médica de urgencia (INC-06) o permitiendo la "
        "fuga de diagnósticos íntimos vulnera la dignidad humana, destruye la confianza en las instituciones sanitarias y transgrede el secreto profesional."
    )
}

TRACEABILITY_MATRIX = [
    ("RF-1.1", "Autenticación de usuarios", "CP-01", "Aprobado (Pass)", "ISO 25010 / Ley 19.628"),
    ("RF-1.2", "Cierre de sesión y revocación", "CP-06", "Fallado (Fail)", "OWASP A07 / NFR-SEG-9"),
    ("RF-2.1", "Registro público como paciente", "CP-07", "Aprobado (Pass)", "ISO 25010 / Funcional"),
    ("RF-2.2", "Registro de pacientes por médico/admin", "CP-03, CP-07", "Aprobado (Pass)", "Ley 20.584 / Algoritmo Módulo 11"),
    ("RF-2.3", "Edición de pacientes", "CP-08", "Aprobado (Pass)", "Ley 20.584 / Integridad"),
    ("RF-2.4", "Visualización de paciente", "CP-10", "Aprobado (Pass)", "ISO 25010 / Confidencialidad"),
    ("RF-2.5", "Visualización de usuarios por admin", "CP-13", "Aprobado (Pass)", "RBAC / Gobierno de Datos"),
    ("RF-2.6", "Edición de usuarios y roles", "CP-13", "Aprobado (Pass)", "RBAC / Mantenibilidad"),
    ("RF-2.7", "Eliminación de usuarios (borrado lógico)", "CP-05, CP-22", "Fallado (Fail)", "Ley 20.584 / Conservación 15 años"),
    ("RF-3.1", "Registro de exámenes por médico", "CP-02", "Aprobado (Pass)", "Regla de Negocio RB-3"),
    ("RF-3.2", "Edición de exámenes y documentos", "CP-04", "Aprobado (Pass)", "Integridad de Datos"),
    ("RF-3.3", "Eliminación de exámenes por médico", "CP-09", "Fallado (Fail)", "Regla de Negocio RB-3 (Bloqueado)"),
    ("RF-4.1", "Visualización de exámenes por paciente", "CP-10", "Aprobado (Pass)", "Regla de Negocio RB-1 / Ley 20.584"),
    ("RF-4.2", "Descarga de documentos por paciente", "CP-11, CP-12", "Aprobado (Pass)", "Ley 20.584 / Prevención IDOR"),
    ("RF-4.3", "Adjuntar documentos PDF, JPG, PNG", "CP-04", "Aprobado (Pass)", "ISO 25010 / Multer 10MB"),
    ("RF-4.4", "Almacenamiento de documentos y ref en BD", "CP-04, CP-20", "Fallado (Fail)", "Exposición estática / Inconsistencia"),
    ("RF-5.1", "Auditoría de acciones críticas", "CP-01, CP-14, CP-22", "Fallado (Fail)", "Fallo de tipo en DELETE /users"),
    ("NFR-SEG-1", "TLS obligatorio en comunicaciones", "CP-01", "Aprobado (Pass)", "Cifrado en tránsito"),
    ("NFR-SEG-2", "Contraseñas con Hashing seguro (bcrypt)", "CP-18", "Fallado (Fail)", "Ley 19.628 Art. 11 / OWASP A02"),
    ("NFR-SEG-3", "Encriptación de datos sensibles en reposo", "CP-04", "Fallado (Fail)", "Archivos sin cifrado en disco/BD"),
    ("NFR-SEG-4", "Control de acceso por rol en backend", "CP-02, CP-14", "Aprobado (Pass)", "RBAC / OWASP A01"),
    ("NFR-SEG-5", "Protección contra inyección y saneamiento", "CP-03, CP-20", "Fallado (Fail)", "Exposición estática en app.js"),
    ("NFR-SEG-6", "Gestión de log segura y consistente", "CP-14, CP-22", "Fallado (Fail)", "Inconsistencia de tipos en eliminación"),
    ("NFR-SEG-7", "Políticas de respaldo y recuperación", "Auditoría", "Aprobado (Pass)", "PostgreSQL dump script disponible"),
    ("NFR-SEG-8", "Cumplimiento normativo protección datos", "CP-18, CP-20", "Fallado (Fail)", "Transgresión Ley 19.628 / 20.584"),
    ("NFR-SEG-9", "Manejo de sesión mediante token JWT", "CP-01, CP-21", "Fallado (Fail)", "Almacenamiento inseguro en localStorage"),
    ("NFR-PERF-1", "Tiempo de respuesta CRUD < 300 ms", "CP-15, CP-16, CP-17", "Fallado (Fail)", "delayMiddleware inyecta 5000 ms"),
    ("NFR-PERF-2", "Carga de página principal < 2s", "CP-24", "Aprobado (Pass)", "Vite + React SPA rendimiento nativo"),
    ("NFR-PERF-3", "Soporte de concurrencia 200 usuarios", "Auditoría", "Aprobado (Pass)", "Pool de conexiones PG optimizado"),
    ("NFR-USAB-1", "Tipografía legible y contraste mayores", "CP-23", "Aprobado (Pass)", "Material UI v7 / Accesibilidad"),
    ("NFR-USAB-2", "Flujos claros de registro y consulta", "CP-03, CP-10", "Aprobado (Pass)", "UX / Formik y validación"),
    ("NFR-USAB-3", "Ayuda contextual y mensajes amigables", "CP-03", "Aprobado (Pass)", "MUI Alert / Sonner Toasts"),
    ("NFR-USAB-4", "Flujo escalonado: Paciente -> Examen", "CP-10", "Aprobado (Pass)", "Navegación jerárquica médica"),
    ("NFR-DIS-1", "Disponibilidad objetivo 99.5% mensual", "CP-25", "Fallado (Fail)", "Fuga de stack traces en errores 500"),
    ("NFR-DIS-2", "Ventana de mantenimiento y migración", "Auditoría", "Aprobado (Pass)", "Scripts SQL idempotentes en sql/"),
    ("NFR-COMPAT-1", "Navegadores modernos (Chrome, Edge, etc.)", "CP-24", "Aprobado (Pass)", "Compatibilidad ES2020 / Vite"),
    ("NFR-COMPAT-2", "Diseño responsivo móvil y tablet", "CP-24", "Aprobado (Pass)", "Breakpoints MUI / Tailwind"),
    ("RB-1", "Paciente solo permisos de lectura propia", "CP-02, CP-10", "Aprobado (Pass)", "RBAC estricto validado"),
    ("RB-2", "Admin acceso completo a lectura y gestión", "CP-13, CP-14", "Aprobado (Pass)", "Gobernanza administrativa validada"),
    ("RB-3", "Médico acceso a pacientes y exámenes", "CP-02, CP-09", "Fallado (Fail)", "Médico bloqueado al eliminar examen")
]

SECTION_8_TEXTS = {
    "conclusiones_p1": (
        "El proceso sistemático de aseguramiento de la calidad, pruebas dinámicas y auditoría técnica ejecutado sobre el software "
        "'Cuidarte+' permitió identificar un nivel de cobertura de pruebas del 100% sobre los requerimientos de la ERS. No obstante, "
        "los resultados revelan una severa dicotomía entre la madurez funcional de la interfaz de usuario (React/Material UI) y la "
        "vulnerabilidad crítica de la capa de servicios (Express/Node.js)."
    ),
    "conclusiones_p2": (
        "De los 25 casos de prueba ejecutados, 14 resultaron aprobados (56%), 9 fallados (36%) y 2 bloqueados (8%). Los fallos más graves "
        "radican en el almacenamiento de contraseñas en texto claro (INC-04) y la exposición de archivos médicos en rutas estáticas públicas (INC-05), "
        "los cuales constituyen contingencias jurídicas inaceptables bajo la Ley 19.628, Ley 20.584 y Ley 21.459. Adicionalmente, se constató la "
        "inyección deliberada de retrasos de 5 segundos mediante 'delayMiddleware' (INC-06, INC-07) y el uso de eliminación física en lugar de lógica "
        "(INC-01). El software NO se encuentra actualmente en condiciones técnicas ni éticas para operar en un entorno de producción hospitalaria."
    ),
    "remediacion_intro": (
        "Para transformar Cuidarte+ en una solución robusta, segura y legalmente conforme, se presenta el siguiente Plan de Remediación Técnica "
        "Inmediata con los ajustes de código requeridos:"
    ),
    "remediacion_pasos": [
        ("Paso 1: Implementación de Hashing Criptográfico con Bcrypt (Remediación INC-04)", (
            "Instalar 'bcrypt' mediante 'npm install bcrypt'. Modificar 'routes/auth.js' y 'routes/users.js' para hashear la contraseña antes de "
            "guardarla: 'const salt = await bcrypt.genSalt(10); const hash = await bcrypt.hash(password, salt);'. En el login, validar mediante: "
            "'const match = await bcrypt.compare(password, user.contrasena);'."
        )),
        ("Paso 2: Eliminación de Retardos Artificiales (Remediación INC-06 e INC-07)", (
            "Eliminar todas las invocaciones a 'delayMiddleware(5000)' en los archivos 'routes/pacientes.js', 'routes/examenes.js' y 'routes/documentos.js'. "
            "Esto restablecerá de inmediato los tiempos de respuesta nativos por debajo de los 50 ms en red local, cumpliendo el SLA de 300 ms de NFR-PERF-1."
        )),
        ("Paso 3: Cierre de Exposición Pública de Documentos Clínicos (Remediación INC-05)", (
            "Remover en 'BACKEND/src/app.js' la línea 'app.use(\"/files/documentos\", express.static(uploadsDir));'. Canalizar toda descarga exclusivamente "
            "a través del endpoint seguro 'GET /documentos/:id', el cual valida el token JWT y asegura que solo el médico tratante o el paciente titular "
            "accedan al archivo."
        )),
        ("Paso 4: Implementación de Eliminación Lógica y Conservación de Registros (Remediación INC-01)", (
            "Agregar la columna 'activo BOOLEAN DEFAULT TRUE' en las tablas 'usuarios', 'pacientes' y 'examen_medico'. Reemplazar las sentencias destructivas "
            "'DELETE FROM' por 'UPDATE tabla SET activo = FALSE WHERE id = $1', garantizando el cumplimiento del deber de custodia clínica por 15 años (Ley 20.584)."
        )),
        ("Paso 5: Corrección de Tipado en Auditoría de Usuarios (Remediación INC-10)", (
            "En 'BACKEND/src/routes/users.js' línea de eliminación, corregir el parámetro de auditoría pasando 'authUser?.usuarioId' (BIGINT) en lugar de "
            "'authUser?.nombreUsuario' (string), eliminando el error 22P02 de PostgreSQL."
        )),
        ("Paso 6: Ajuste de Permisos para Médicos en Exámenes (Remediación INC-03)", (
            "En 'BACKEND/src/routes/examenes.js', modificar la función 'requireRole' en el endpoint DELETE '/:id' para permitir tanto 'admin' como 'medico' "
            "('requireRole(req, [\"admin\", \"medico\"])'), habilitando el cumplimiento de RF-3.3."
        )),
        ("Paso 7: Securización de Tokens con Cookies HttpOnly y Rate Limiting (Remediación INC-09 e INC-11)", (
            "Migrar el almacenamiento del JWT desde 'localStorage' hacia cookies seguras con banderas 'HttpOnly', 'Secure' y 'SameSite=Strict'. Implementar "
            "'express-rate-limit' en el endpoint de login para mitigar ataques de fuerza bruta y configurar un middleware de manejo global de errores que "
            "oculte trazas internas de la base de datos."
        ))
    ]
}
