# GUIA INTEGRAL DEL PROYECTO, DESPLIEGUE Y DEFENSA DE EVALUACION PARCIAL 3
# SISTEMA DE GESTION DE EXAMENES MEDICOS CUIDARTE+
# ASIGNATURA: ISY1102 - SEGURIDAD Y CALIDAD EN EL DESARROLLO DE SOFTWARE
# PROFESOR: CLAUDIO DANIEL GONZALEZ PAUZOCA
# SECCION: 006D
# INTEGRANTES: RICARDO SAEZ, PATRICIO QUILODRAN, SEBASTIAN DINAMARCA
# NOTA: DOCUMENTO REDACTADO SIN EMOJIS.

---

## 1. RESUMEN EJECUTIVO DEL PROYECTO CUIDARTE+

### 1.1 Proposito y Contexto del Sistema
Cuidarte+ es una plataforma web desarrollada para centros medicos asistenciales orientada a la gestion integral de pacientes, emision de ordenes de examenes medicos, carga y descarga de documentos clinicos adjuntos (PDF, JPG, PNG) y registro inmutable de auditoria de acciones criticas.

El sistema fue concebido para operar bajo tres roles principales de usuarios con privilegios diferenciados:
1. Administrador (admin): Gestion integral de usuarios, asignacion y modificacion de roles, supervision del sistema y consulta exclusiva de la bitacora de auditoria.
2. Medico (medico): Registro y edicion de fichas de pacientes, emision de ordenes de examenes medicos, adjuncion de documentos clinicos y consulta de antecedentes de cualquier paciente registrado.
3. Paciente (paciente): Consulta exclusiva de sus propios examenes medicos y descarga de sus respectivos informes y documentos adjuntos. Posee permisos estrictos de solo lectura sobre su propio expediente, sin posibilidad de ver datos de terceros.

### 1.2 Arquitectura Tecnologica
El software adopta una arquitectura desacoplada cliente-servidor distribuida en tres capas:
- Capa de Presentacion (Frontend): Desarrollada en React v19.1.1 con Vite v7.1.7. Emplea la libreria Material UI v7.3.4 y Tailwind CSS v3.4.14 para una interfaz responsiva, accesible para adultos mayores y modular mediante React Router DOM v7.
- Capa de Logica de Negocio (Backend): API RESTful desarrollada sobre Node.js y Express v4.19.2. Gestiona autenticacion basada en JSON Web Tokens (JWT), validacion de esquemas de datos con Yup, subida de archivos en memoria con Multer y documentacion interactiva bajo el estandar OpenAPI 3.0 (Swagger UI).
- Capa de Persistencia (Base de Datos): Motor relacional PostgreSQL v15+ que almacena usuarios, roles, pacientes, tipos de examen, examenes medicos, documentos clinicos y la tabla de auditoria transaccional.
- Orquestacion: Docker y Docker Compose para levantar de forma reproducibilidad e inmediata toda la infraestructura de base de datos, backend y frontend.

---

## 2. GUIA PASO A PASO: COMO LEVANTAR EL PROYECTO

### 2.1 Requisitos Previos en el Equipo
Para levantar y ejecutar el proyecto se requiere tener instalado en el sistema:
- Docker Desktop (con motor Docker y Docker Compose activos).
- Node.js v18 o superior (recomendado Node.js v20 LTS) y gestor de paquetes npm (en caso de ejecucion manual).
- Navegador web moderno (Google Chrome, Mozilla Firefox, Microsoft Edge o Safari).
- Cliente de base de datos opcional (DBeaver, pgAdmin) o extension de VS Code para PostgreSQL.

### 2.2 Despliegue Automatizado mediante Docker Compose (Metodo Recomendado)
Este metodo es el mas rapido y asegura que todos los servicios se comuniquen en la misma red con las variables de entorno preconfiguradas:

1. Abrir una consola de comandos (PowerShell o CMD) y situarse en la raiz del codigo fuente:
   ```bash
   cd "c:\Users\ricar\Downloads\Caso semestral\CodigoFuenteB"
   ```

2. Ejecutar el comando de construccion y levantamiento en segundo plano:
   ```bash
   docker-compose up -d --build
   ```

3. Verificar que los tres contenedores esten en estado operativo ('running' / 'healthy'):
   ```bash
   docker-compose ps
   ```

4. Servicios y Puertos Expuestos:
   - Frontend Web (Cliente React): http://localhost:3333
   - Backend API REST (Servidor Express): http://localhost:4444
   - Documentacion Interactiva Swagger UI: http://localhost:4444/docs
   - Base de Datos PostgreSQL: Host 'localhost', Puerto 15442, BD 'cuidarteplus', Usuario 'postgres', Clave 'postgres'.

5. Para detener los contenedores una vez finalizada la sesion:
   ```bash
   docker-compose down
   ```

### 2.3 Despliegue Manual (Sin Docker)
En caso de requerir levantar cada servicio por separado:

1. Base de Datos PostgreSQL:
   - Contar con PostgreSQL corriendo localmente.
   - Crear una base de datos llamada `cuidarteplus`.
   - Ejecutar el script SQL de inicializacion:
     ```bash
     psql -U postgres -d cuidarteplus -f BACKEND/sql/dump-cuidarteplus.sql
     ```

2. Levantar el Backend:
   ```bash
   cd BACKEND
   npm install
   npm run dev
   ```
   El backend iniciara en el puerto configurado en su archivo `.env` (puerto 4444 por defecto).

3. Levantar el Frontend:
   ```bash
   cd FRONTEND
   npm install
   npm run dev
   ```
   El cliente web iniciara en http://localhost:3333 (o el puerto indicado por Vite).

### 2.4 Credenciales de Acceso por Defecto
El dataset de prueba precargado en la base de datos incluye tres usuarios base correspondientes a los tres roles del sistema:

| Rol | Nombre de Usuario | Contrasena | Correo Electronico | Permisos Principales |
|---|---|---|---|---|
| Administrador | admin | admin | admin@cuidarteplus.cl | Acceso total, usuarios, roles, auditoria |
| Medico | medico | medico | medico@cuidarteplus.cl | Registro pacientes, creacion examenes |
| Paciente | paciente | paciente | paciente@cuidarteplus.cl | Lectura exclusiva de sus propios examenes |

---

## 3. RESUMEN DE INFORMACION RELEVANTE DEL INFORME DE CALIDAD Y SEGURIDAD

### 3.1 Metricas Globales del Plan de Pruebas
- Total de casos de prueba formalmente disenados: 25 casos.
- Total de casos ejecutados en el ciclo de aseguramiento: 25 casos (100% de ejecucion).
- Casos aprobados exitosamente (Pass): 14 casos (56.0%).
- Casos fallados por presencia de defecto (Fail): 9 casos (36.0%).
- Casos bloqueados por restriccion de diseno (Blocked): 2 casos (8.0%).
- Cobertura de requerimientos ERS: 100% de cobertura sobre requerimientos funcionales (RF-1 a RF-5), no funcionales (NFR-SEG, PERF, USAB, DIS, COMPAT) y reglas de negocio (RB-1 a RB-3).

### 3.2 Principales Incidentes y Vulnerabilidades Criticas Detectadas

1. Incidente INC-04 (Critico) - Almacenamiento de Contrasenas en Texto Plano:
   - Descripcion: En `BACKEND/src/routes/auth.js` y `users.js`, las contraseñas se insertan y consultan de forma literal (`user.contrasena !== password`). La libreria `bcrypt` ni siquiera forma parte de las dependencias de `package.json`.
   - Impacto: Cualquier acceso a la base de datos o fuga de copias de respaldo expone inmediatamente las credenciales de todo el personal medico y pacientes. Vulneracion directa de NFR-SEG-2 y del deber de seguridad del Art. 11 de la Ley 19.628.

2. Incidente INC-05 (Critico) - Exposicion Publica de Documentos Clinicos:
   - Descripcion: En `BACKEND/src/app.js` existe la linea `app.use("/files/documentos", express.static(uploadsDir));`.
   - Impacto: Permite a cualquier usuario no autenticado descargar archivos medicos privados (informes de biopsias, hemogramas) simplemente adivinando o conociendo el nombre del archivo en la URL, eludiendo todo control de acceso.

3. Incidente INC-06 e INC-07 (Grave) - Inyeccion Intencional de Retardo de 5 Segundos (Latencia):
   - Descripcion: En `BACKEND/src/routes/pacientes.js` y `routes/examenes.js` se encuentra inyectado el middleware `delayMiddleware(5000)`.
   - Impacto: Cada consulta de pacientes o creacion de examen demora mas de 5,000 ms, destruyendo el SLA de rendimiento de NFR-PERF-1 (< 300 ms) y perjudicando la atencion medica oportuna.

4. Incidente INC-01 (Grave) - Eliminacion Fisica Destructiva en Vez de Borrado Logico:
   - Descripcion: Los endpoints de eliminacion ejecutan `DELETE FROM usuarios` y `DELETE FROM pacientes`.
   - Impacto: Destruye el historial de salud del paciente e impide auditorias forenses frente a negligencias medicas. Viola el requerimiento ERS de eliminacion logica y la obligacion sanitaria de conservar fichas clinicas por un minimo legal de 15 anos (Ley 20.584 y Decreto 41 MINSAL).

5. Incidente INC-10 (Moderado) - Error de Tipos de Datos en Auditoria de Eliminacion de Usuarios:
   - Descripcion: En `BACKEND/src/routes/users.js` en la ruta `router.delete("/:id")`, se envia `authUser?.nombreUsuario` (cadena de texto) al parametro `$1` de auditoria, el cual es de tipo `BIGINT`, provocando error 22P02 de PostgreSQL.

6. Incidente INC-03 (Moderado) - Medico Bloqueado para Eliminar Examenes:
   - Descripcion: En `routes/examenes.js`, el endpoint `DELETE /:id` exige rol `admin` (`requireRole(req, ["admin"])`), bloqueando a los medicos a pesar de que el requerimiento RF-3.3 les otorga expresamente dicha facultad.

7. Incidente INC-09 (Moderado) - Persistencia de Tokens JWT en localStorage:
   - Descripcion: En `FRONTEND/src/context/AuthContext.jsx`, el token de sesion se guarda en `localStorage.setItem("token", newToken)`.
   - Impacto: Los tokens almacenados en localStorage son vulnerables a ser extraidos mediante vulnerabilidades de Cross-Site Scripting (XSS). La mejor practica exige cookies seguras HttpOnly y SameSite.

### 3.3 Marco Legal y Consecuencias Juridicas
- Ley Nº 19.628: Los datos de salud son 'Datos Sensibles'. El almacenamiento negligente en texto plano o la exposicion pública genera demandas de indemnizacion por dano moral y sanciones de la autoridad de datos personales.
- Ley Nº 20.584: La reserva de la ficha clinica es obligatoria y el borrado fisico esta expresamente prohibido por la exigencia de conservacion minima de 15 anos.
- Ley Nº 21.459: Tipifica delitos de acceso ilicito y dano a datos. Dejar vulnerabilidades conocidas abiertas genera responsabilidad penal para administradores y desarrolladores.

---

## 4. GUIA ESTRATEGICA PARA LA PRESENTACION Y DEFENSA INDIVIDUAL

### 4.1 Estructura del Tiempo de Evaluacion
- Tiempo total asignado: 10 minutos de exposicion grupal + 5 minutos de preguntas individuales del docente.
- Modalidad: La evaluacion es 100% individual. Cada estudiante es evaluado segun su dominio tecnico, claridad conceptual y conocimiento integral del proyecto.

### 4.2 Reparto Recomendado de la Exposicion (10 Minutos)

#### Estudiante 1: Ricardo Saez (Minuto 0:00 a 3:20) - Introduccion, Arquitectura y Estrategia QA
- Apertura: Saludo formal al profesor Claudio Daniel Gonzalez Pauzoca y presentacion del equipo (Seccion 006D).
- Contexto de Cuidarte+: Objetivo del sistema clinico, roles (Admin, Medico, Paciente) y arquitectura tecnologica (React 19, Material UI, Express, PostgreSQL, Docker).
- Enfoque Metodologico del Plan de Pruebas: Explicar el enfoque mixto (analisis estatico SAST con ESLint, pruebas dinamicas de API con Postman, pruebas de rendimiento y pruebas de accesibilidad para la tercera edad).
- Criterios de Calidad: Mencionar el marco ISO/IEC 25010 y los criterios de entrada/salida.
- Metricas Consolidadas: Explicar que se ejecutaron 25 casos con un 56% de aprobacion, 36% de fallas y 8% de bloqueos, dando paso al analisis de seguridad.

#### Estudiante 2: Patricio Quilodran (Minuto 3:20 a 6:40) - Auditoria de Seguridad y Marco Legal
- Hallazgos de Seguridad Criticos:
  - Explicar el incidente INC-04: Contraseñas en texto plano y ausencia absoluta de `bcrypt` en el backend.
  - Explicar el incidente INC-05: Exposicion publica de `/files/documentos` mediante `express.static` sin requerir token JWT.
  - Explicar el incidente INC-09: Almacenamiento del token en `localStorage` vulnerable a ataques XSS.
- Impacto Legal y Normativo:
  - Ley 19.628: Tratamiento de datos sensibles de salud y transgresion del deber de seguridad (Art. 11).
  - Ley 20.584: Confidencialidad de la ficha clinica y la violacion que representa el borrado fisico ('hard delete') frente a la exigencia de custodia legal minima de 15 anos.
  - Ley 21.459: Delitos informaticos derivados del acceso no autorizado a sistemas sanitarios.
- Principios Bioeticos: El compromiso etico de la ingenieria de software de no comprometer la intimidad ni la salud del paciente.

#### Estudiante 3: Sebastian Dinamarca (Minuto 6:40 a 10:00) - Rendimiento, Incidentes Funcionales y Remediacion
- Rendimiento y Accesibilidad:
  - Explicar el incidente INC-06 e INC-07: Demostracion del middleware de delay (`delayMiddleware(5000)`) que elevo los tiempos de respuesta a mas de 5 segundos, violando el SLA de 300 ms de NFR-PERF-1.
  - Accesibilidad para adultos mayores (NFR-USAB-1): Validacion de fuentes y contraste en Material UI.
- Incidentes Funcionales y de Auditoria:
  - Incidente INC-03: Bloqueo al rol medico para eliminar examenes (contradice RF-3.3).
  - Incidente INC-10: Inconsistencia de tipos en `routes/users.js` al eliminar usuario (string enviado a columna BIGINT).
- Matriz de Trazabilidad y Cobertura: Destacar la cobertura del 100% de los requerimientos de la ERS.
- Plan de Remediacion Inmediata: Explicar los pasos concretos de solucion (instalar bcrypt, remover delayMiddleware, eliminar static de uploads, implementar borrado logico `activo = false`).
- Cierre: Concluir que el software no esta listo para produccion sin estas remediaciones y abrir la ronda de preguntas.

---

## 5. BANCO DE PREGUNTAS CLAVE DEL PROFESOR CLAUDIO GONZALEZ Y RESPUESTAS MODELO

A continuacion se presentan las preguntas mas probables que formulara el docente durante los 5 minutos de defensa individual, junto con la respuesta tecnica esperada:

### Pregunta 1: ¿Por que el almacenamiento de contrasenas en texto plano es una falta critica y que normativa chilena transgrede?
- Respuesta Modelo: "Profesor, almacenar contrasenas en texto plano constituye una falla critica (INC-04) porque cualquier actor con acceso a la base de datos o a un respaldo puede comprometer la totalidad de las cuentas, suplantando identidades de medicos o pacientes. Transgrede el Articulo 11 de la Ley 19.628 sobre Proteccion de Datos Personales, que exige al responsable del banco de datos implementar medidas tecnicas eficaces de seguridad. Tratandose de datos sensibles de salud (Art. 2 letra g y Art. 10), la negligencia tecnica conlleva severas sanciones civiles e infraccionales. La solucion obligatoria es integrar la libreria bcrypt aplicando funciones hash unidireccionales con sal aleatoria y factor de trabajo minimo de 10."

### Pregunta 2: ¿Que implicancia legal tiene ejecutar un 'DELETE' fisico en una base de datos de pacientes o examenes segun la Ley 20.584?
- Respuesta Modelo: "La Ley 20.584 sobre Derechos y Deberes de los Pacientes, en conjunto con el Decreto 41 del MINSAL, exige la reserva absoluta y la conservacion obligatoria de la ficha clinica y sus antecedentes por un plazo minimo de 15 anos. Realizar un 'DELETE FROM' destructivo en PostgreSQL (INC-01) destruye de forma irreversible el historial clinico, impidiendo auditorias medicas forenses ante posibles negligencias o juicios de mala praxis. Para cumplir con la normativa y con la ERS, la solucion tecnica es implementar eliminacion logica agregando un campo 'activo BOOLEAN DEFAULT TRUE' y actualizando su estado mediante UPDATE, preservando intactos los registros y la bitacora de auditoria."

### Pregunta 3: ¿Por que fallaron las pruebas de rendimiento si el motor PostgreSQL y la API Express estaban corriendo en red local?
- Respuesta Modelo: "Las pruebas de rendimiento no fallaron por limitaciones de hardware o sobrecarga de base de datos, sino debido a un defecto de implementacion detectado en el backend: la presencia deliberada de un middleware de retardo llamado 'delayMiddleware(5000)' en los archivos 'routes/pacientes.js', 'routes/examenes.js' y 'routes/documentos.js'. Este middleware ejecuta un setTimeout de 5,000 ms antes de invocar la funcion 'next()', lo que provocaba que peticiones GET simples demoraran un promedio de 5,082 ms, violando directamente el SLA estipulado en NFR-PERF-1 que exige tiempos de respuesta inferiores a 300 ms. Al remover este middleware, los tiempos reales de la API caen por debajo de los 45 ms."

### Pregunta 4: ¿Cual es el riesgo de seguridad de exponer la carpeta de uploads con 'express.static' en un sistema de salud?
- Respuesta Modelo: "La directiva 'app.use(\"/files/documentos\", express.static(uploadsDir))' en 'app.js' (INC-05) convierte el directorio de documentos medicos en un repositorio web publico sin capa de autorizacion. Esto permite que cualquier usuario o atacante externo que conozca o adivine el nombre de un archivo PDF o imagen mediante peticiones GET directas descargue diagnosticos de salud sin pasar por el middleware de verificacion de token JWT. Esto rompe el principio de confidencialidad y facilita ataques de Insecure Direct Object References (IDOR). La remediacion exige remover la ruta estatica y canalizar toda descarga a traves del endpoint controlado 'GET /documentos/:id', donde se verifica que el solicitante sea el medico tratante o el paciente titular."

### Pregunta 5: ¿Por que no es recomendable persistir el token JWT en el 'localStorage' del navegador en aplicaciones clinicas?
- Respuesta Modelo: "El almacenamiento en 'localStorage' (INC-09) es accesible por cualquier script JavaScript que se ejecute en el contexto del origen. Por lo tanto, si la aplicacion sufre una vulnerabilidad de Cross-Site Scripting (XSS), un atacante podria robar silenciosamente el token de sesion de un medico y acceder a todos los registros de pacientes. El estandar de la industria de acuerdo con OWASP y las guias de seguridad web recomienda almacenar los tokens de sesion en cookies con atributos 'HttpOnly' (que impide el acceso desde JavaScript), 'Secure' (solo via HTTPS) y 'SameSite=Strict' (para prevenir ataques CSRF)."

### Pregunta 6: ¿Como se estructuro la matriz de trazabilidad para asegurar el 100% de cobertura de la ERS?
- Respuesta Modelo: "Se mapeo cada uno de los requisitos del documento de ERS entregado en la EP1 contra casos de prueba especificos: desde los requerimientos funcionales RF-1.1 hasta RF-5.1, todos los requerimientos no funcionales (seguridad NFR-SEG-1 a 9, rendimiento NFR-PERF-1 a 3, usabilidad NFR-USAB-1 a 4, disponibilidad NFR-DIS-1 a 2, compatibilidad NFR-COMPAT-1 a 2) y las tres reglas de negocio transversales (RB-1, RB-2 y RB-3). Para cada requisito se indico el caso de prueba ejecutado, su resultado experimental (Pass/Fail) y el estandar tecnico o cuerpo legal chileno aplicable, demostrando rigurosidad metodologica y coherencia tecnica."

---

## 6. CONSEJOS PRACTICOS FINALES PARA OBTENER LA CALIFICACION MAXIMA
1. Dominio de Codigo: Tengan abierto Visual Studio Code con el proyecto `CodigoFuenteB` listo para mostrar en pantalla las lineas exactas de los defectos (ej. la ausencia de bcrypt en `BACKEND/src/routes/auth.js` linea 21, el `delayMiddleware(5000)` en `routes/pacientes.js` linea 38, y el `express.static` en `BACKEND/src/app.js` linea 43).
2. Seguridad en las Respuestas: Respondan con terminologia formal (hashing, sal criptografica, RBAC, IDOR, SLA, ISO/IEC 25010, Ley 19.628, Ley 20.584, Módulo 11).
3. Postura Profesional: Eviten titubeos y mantengan un tono analitico y critico. Demuestren que auditaron el software a fondo y que comprenden el impacto de cada falla en la vida real de los pacientes.
