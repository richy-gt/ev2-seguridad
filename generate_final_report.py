# -*- coding: utf-8 -*-
"""
Script de generacion del Informe Final EP3 en formato Word (.docx)
Cumple estrictamente con la pauta y rubrica de evaluacion de ISY1102.
Utiliza EXACTAMENTE el estilo, estilos y diseno de EP3_ISY1102_Estudiante_Formato_Informe.docx.
Integrantes: Ricardo Saez, Patricio Quilodran, Sebastian Dinamarca
Profesor: CLAUDIO DANIEL GONZALEZ PAUZOCA
Seccion: 006D
NOTA: ESTRICTAMENTE SIN EMOJIS.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

import build_report_data as data

def set_cell_background(cell, fill_hex):
    """Aplica sombreado hexadecimal a una celda de tabla."""
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('shd'):
            tcPr.remove(child)
    if fill_hex and fill_hex.upper() != 'NONE':
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex.upper()}"/>')
        tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    """Aplica margenes internos en dxa (twips)."""
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('tcMar'):
            tcPr.remove(child)
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    """Configura bordes formales y elegantes para la tabla."""
    tblPr = table._tbl.tblPr
    for child in list(tblPr):
        if child.tag.endswith('tblBorders'):
            tblPr.remove(child)
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def format_cell_text(cell, text, bold=False, italic=False, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, color_rgb=None):
    """Formatea el parrafo principal de una celda con tipografia Arial."""
    p = cell.paragraphs[0]
    p.text = ""
    p.alignment = align
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size_pt)
    r.bold = bold
    r.italic = italic
    if color_rgb:
        r.font.color.rgb = color_rgb
    else:
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def insert_element_before_sectpr(doc, element):
    """Inserta un elemento XML (parrafo o tabla) antes del sectPr final del documento."""
    body = doc.element.body
    sectPr = body.xpath('w:sectPr')[0]
    body.insert(body.index(sectPr), element)

def add_doc_heading_1(doc, text):
    p = doc.add_paragraph(style='Heading 1')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(14)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 0, 0)
    insert_element_before_sectpr(doc, p._p)
    return p

def add_doc_heading_2(doc, text):
    p = doc.add_paragraph(style='Heading 2')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 0, 0)
    insert_element_before_sectpr(doc, p._p)
    return p

def add_doc_heading_3(doc, text):
    p = doc.add_paragraph(style='Normal')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 0, 0)
    insert_element_before_sectpr(doc, p._p)
    return p

def add_doc_paragraph(doc, text, bold_prefix=None, space_after=6, space_before=0, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph(style='Normal')
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(11)
        r_pre.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0, 0, 0)
    insert_element_before_sectpr(doc, p._p)
    return p

def add_doc_bullet(doc, bold_prefix, text, space_after=3):
    p = doc.add_paragraph(style='List Paragraph')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.25
    r_pre = p.add_run(bold_prefix + ": ")
    r_pre.font.name = "Arial"
    r_pre.font.size = Pt(10.5)
    r_pre.bold = True
    r_pre.font.color.rgb = RGBColor(0, 0, 0)
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(10.5)
    r.font.color.rgb = RGBColor(0, 0, 0)
    insert_element_before_sectpr(doc, p._p)
    return p

def create_case_design_table(doc, case_info):
    """Crea una tabla de diseno de caso de prueba idéntica al formato Tabla 0 del documento base."""
    tbl = doc.add_table(rows=14, cols=3)
    tbl.style = 'Grid Table 4'
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl, color="B0C4DE", sz="4")
    
    # R0: Headers
    format_cell_text(tbl.rows[0].cells[0], "ID", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl.rows[0].cells[1], "NOMBRE", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl.rows[0].cells[2], "REQUERIMIENTO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)
    
    # R1: Data R0
    format_cell_text(tbl.rows[1].cells[0], case_info["id"], bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl.rows[1].cells[1], case_info["nombre"], bold=False, size_pt=9.5)
    format_cell_text(tbl.rows[1].cells[2], case_info["requerimiento"], bold=False, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl.rows[1].cells:
        set_cell_margins(c, 100, 100, 120, 120)

    # Pairs of (Section Title, Content)
    sections = [
        (2, 3, "DESCRIPCIÓN", case_info["descripcion"]),
        (4, 5, "PRECONDICIONES", case_info["precondiciones"]),
        (6, 7, "PASOS", case_info["pasos"]),
        (8, 9, "RESULTADO ESPERADO", case_info["resultado_esperado"]),
        (10, 11, "CRITERIO DE ACEPTACIÓN", case_info["criterio_aceptacion"]),
        (12, 13, "DATOS DE PRUEBA", case_info["datos_prueba"])
    ]

    for title_row_idx, content_row_idx, title_text, content_text in sections:
        # Title row: merge 3 cells
        t_row = tbl.rows[title_row_idx]
        merged_title_cell = t_row.cells[0]
        merged_title_cell.merge(t_row.cells[2])
        format_cell_text(merged_title_cell, title_text, bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.LEFT)
        set_cell_background(merged_title_cell, "E8E8E8")
        set_cell_margins(merged_title_cell, 80, 80, 120, 120)

        # Content row: merge 3 cells
        c_row = tbl.rows[content_row_idx]
        merged_content_cell = c_row.cells[0]
        merged_content_cell.merge(c_row.cells[2])
        format_cell_text(merged_content_cell, content_text, bold=False, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.LEFT)
        set_cell_margins(merged_content_cell, 100, 100, 120, 120)

    insert_element_before_sectpr(doc, tbl._tbl)
    
    # Espacio tras la tabla
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(4)
    p_spacer.paragraph_format.space_after = Pt(8)
    insert_element_before_sectpr(doc, p_spacer._p)
    return tbl

def build_full_report():
    print("Iniciando construccion del informe Word EP3...")
    base_path = "EP3_ISY1102_Estudiante_Formato_Informe.docx"
    output_path = "EP3_ISY1102_Informe_Final_CuidartePlus.docx"
    
    doc = docx.Document(base_path)
    body = doc.element.body
    
    # 1. Modificar portada
    print("Actualizando portada institucional...")
    p13 = doc.paragraphs[13]
    p13.text = data.COVER_DATA["asignatura_seccion"]
    for r in p13.runs:
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0, 0, 0)
    if len(p13.runs) > 0:
        p13.runs[0].bold = True

    p15 = doc.paragraphs[15]
    p15.text = data.COVER_DATA["integrantes_docente"]
    for r in p15.runs:
        r.font.name = "Arial"
        r.font.size = Pt(10.5)
        r.font.color.rgb = RGBColor(0, 0, 0)
    if len(p15.runs) > 0:
        p15.runs[0].bold = True

    # 2. Modificar contenido del Indice (TOC sdt)
    print("Actualizando entradas del indice analitico...")
    for child in body:
        if child.tag.endswith('sdt'):
            # Buscar parrafos dentro de sdtContent
            p_list = child.findall('.//' + qn('w:p'))
            # Mantener el primer parrafo si dice INDICE, luego actualizar
            for idx, p_el in enumerate(p_list):
                p_obj = docx.text.paragraph.Paragraph(p_el, doc)
                if idx < len(data.TOC_ENTRIES):
                    title, page = data.TOC_ENTRIES[idx]
                    p_obj.text = f"{title}\t{page}"
                    p_obj.paragraph_format.space_before = Pt(1)
                    p_obj.paragraph_format.space_after = Pt(1)
                    for r in p_obj.runs:
                        r.font.name = "Arial"
                        r.font.size = Pt(10)
                        r.font.color.rgb = RGBColor(0, 0, 0)

    # 3. Eliminar elementos de plantilla desde el indice hasta antes de sectPr
    print("Limpiando textos instructivos y tablas de ejemplo de la plantilla...")
    while len(body) > 24:
        body.remove(body[23])

    # 4. Construccion de Secciones del Informe
    print("Construyendo Seccion 1: Introduccion...")
    add_doc_heading_1(doc, "1. Introducción")
    add_doc_paragraph(doc, data.SECTION_1_TEXTS["intro_p1"])
    
    add_doc_heading_2(doc, "1.1 Contexto del software a evaluar")
    add_doc_paragraph(doc, data.SECTION_1_TEXTS["contexto_p1"])
    
    add_doc_heading_2(doc, "1.2 Propósito del plan y objetivos de calidad")
    add_doc_paragraph(doc, data.SECTION_1_TEXTS["proposito_p1"])
    
    add_doc_heading_2(doc, "1.3 Ajustes basados en la retroalimentación de la Evaluación Parcial 1 (EP1)")
    add_doc_paragraph(doc, data.SECTION_1_TEXTS["ajustes_ep1_p1"])
    for item_title, item_desc in data.SECTION_1_TEXTS["ajustes_ep1_items"]:
        add_doc_bullet(doc, item_title, item_desc)
        
    add_doc_heading_2(doc, "1.4 Estructura del informe")
    add_doc_paragraph(doc, data.SECTION_1_TEXTS["estructura_p1"])

    print("Construyendo Seccion 2: Criterios de calidad...")
    add_doc_heading_1(doc, "2. Criterios de calidad")
    add_doc_heading_2(doc, "2.1 Calidad de software basada en ISO/IEC 25010")
    add_doc_paragraph(doc, data.SECTION_2_TEXTS["calidad_intro"])
    for pilar_title, pilar_desc in data.SECTION_2_TEXTS["calidad_pilares"]:
        add_doc_bullet(doc, pilar_title, pilar_desc)
        
    add_doc_heading_2(doc, "2.2 Seguridad de la información y gestión de riesgos OWASP")
    add_doc_paragraph(doc, data.SECTION_2_TEXTS["seguridad_intro"])
    for seg_title, seg_desc in data.SECTION_2_TEXTS["seguridad_items"]:
        add_doc_bullet(doc, seg_title, seg_desc)
        
    add_doc_heading_2(doc, "2.3 Cumplimiento normativo y marco legal chileno")
    add_doc_paragraph(doc, data.SECTION_2_TEXTS["normativas_intro"])
    for norm_title, norm_desc in data.SECTION_2_TEXTS["normativas_items"]:
        add_doc_bullet(doc, norm_title, norm_desc)

    print("Construyendo Seccion 3: Plan de pruebas...")
    add_doc_heading_1(doc, "3. Plan de pruebas")
    add_doc_heading_2(doc, "3.1 Estrategia de pruebas")
    add_doc_paragraph(doc, data.SECTION_3_TEXTS["estrategia_p1"])
    
    add_doc_heading_3(doc, "3.1.1 Etapas del proceso de pruebas")
    for etapa_title, etapa_desc in data.SECTION_3_TEXTS["estrategia_etapas"]:
        add_doc_bullet(doc, etapa_title, etapa_desc)
        
    add_doc_heading_3(doc, "3.1.2 Priorización de pruebas y gestión de riesgos")
    add_doc_paragraph(doc, data.SECTION_3_TEXTS["priorizacion_p1"])
    
    add_doc_heading_3(doc, "3.1.3 Criterios de entrada y criterios de salida")
    for crit_title, crit_desc in data.SECTION_3_TEXTS["criterios_in_out"]:
        add_doc_bullet(doc, crit_title, crit_desc)

    add_doc_heading_2(doc, "3.2 Tipos de prueba y justificación técnica")
    add_doc_paragraph(doc, data.SECTION_3_TEXTS["tipos_pruebas_intro"])
    for tipo_title, tipo_desc in data.SECTION_3_TEXTS["tipos_pruebas_items"]:
        add_doc_bullet(doc, tipo_title, tipo_desc)

    add_doc_heading_2(doc, "3.3 Criterios de aceptación transversales")
    add_doc_paragraph(doc, data.SECTION_3_TEXTS["criterios_aceptacion_intro"])
    for ca_title, ca_desc in data.SECTION_3_TEXTS["criterios_aceptacion_items"]:
        add_doc_bullet(doc, ca_title, ca_desc)

    add_doc_heading_2(doc, "3.4 Herramientas utilizadas y asignación de recursos")
    add_doc_paragraph(doc, data.SECTION_3_TEXTS["recursos_intro"])
    
    add_doc_heading_3(doc, "3.4.1 Recursos humanos y roles asignados")
    for rh_name, rh_desc in data.SECTION_3_TEXTS["recursos_humanos"]:
        add_doc_bullet(doc, rh_name, rh_desc)
        
    add_doc_heading_3(doc, "3.4.2 Recursos técnicos e infraestructura")
    for rt_name, rt_desc in data.SECTION_3_TEXTS["recursos_tecnicos"]:
        add_doc_bullet(doc, rt_name, rt_desc)
        
    add_doc_heading_3(doc, "3.4.3 Cronograma de actividades del ciclo de pruebas")
    tbl_crono = doc.add_table(rows=len(data.SECTION_3_TEXTS["cronograma_items"]) + 1, cols=3)
    tbl_crono.style = 'Grid Table 4'
    set_table_borders(tbl_crono, color="B0C4DE", sz="4")
    format_cell_text(tbl_crono.rows[0].cells[0], "HITO / ACTIVIDAD", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_crono.rows[0].cells[1], "PLAZO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_crono.rows[0].cells[2], "ENTREGABLE / ALCANCE", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl_crono.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)
    for r_i, (c_hito, c_plazo, c_entregable) in enumerate(data.SECTION_3_TEXTS["cronograma_items"], start=1):
        format_cell_text(tbl_crono.rows[r_i].cells[0], c_hito, bold=True, size_pt=9)
        format_cell_text(tbl_crono.rows[r_i].cells[1], c_plazo, bold=False, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_crono.rows[r_i].cells[2], c_entregable, bold=False, size_pt=9)
        for c in tbl_crono.rows[r_i].cells:
            set_cell_margins(c, 80, 80, 100, 100)
    insert_element_before_sectpr(doc, tbl_crono._tbl)

    print("Construyendo Seccion 4: Diseno de casos de prueba...")
    add_doc_heading_1(doc, "4. Diseño de casos de prueba")
    add_doc_paragraph(
        doc,
        "A continuación se presenta el diseño detallado de los casos de prueba representativos estructurados bajo el estándar tabular "
        "requerido. Los casos abarcan requerimientos funcionales críticos (autenticación, gestión de pacientes, creación de exámenes, "
        "subida de documentos y eliminación de usuarios) y requerimientos no funcionales (rendimiento, almacenamiento criptográfico, "
        "control de acceso a documentos clínicos, accesibilidad para la tercera edad y compatibilidad multidispositivo):"
    )
    for c_info in data.CASES_DESIGN:
        create_case_design_table(doc, c_info)

    print("Construyendo Seccion 5: Ejecucion de pruebas...")
    add_doc_heading_1(doc, "5. Ejecución de pruebas")
    
    add_doc_heading_2(doc, "5.1 Resumen de ejecución")
    add_doc_paragraph(
        doc,
        "El ciclo de ejecución de pruebas se llevó a cabo sobre el entorno containerizado y local de Cuidarte+. "
        "Se ejecutaron el 100% de los casos planificados, alcanzando una tasa de aprobación del 56% (14 casos) y evidenciando "
        "una tasa de fallo y bloqueo del 44% (9 fallos directos y 2 casos bloqueados por dependencias de acceso). A continuación se resumen las métricas consolidadas:"
    )
    
    # Tabla resumen metricas
    tbl_metricas = doc.add_table(rows=6, cols=3)
    tbl_metricas.style = 'Grid Table 4'
    set_table_borders(tbl_metricas, color="B0C4DE", sz="4")
    format_cell_text(tbl_metricas.rows[0].cells[0], "INDICADOR DE EJECUCIÓN", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_metricas.rows[0].cells[1], "CANTIDAD", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_metricas.rows[0].cells[2], "PORCENTAJE (%)", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl_metricas.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)
        
    metricas_rows = [
        ("Total de casos de prueba diseñados", str(data.SECTION_5_SUMMARY["total_disenados"]), "100.0%"),
        ("Total de casos ejecutados", str(data.SECTION_5_SUMMARY["total_ejecutados"]), "100.0%"),
        ("Casos aprobados exitosamente (Pass)", str(data.SECTION_5_SUMMARY["pasaron"]), data.SECTION_5_SUMMARY["porcentaje_aprobacion"]),
        ("Casos fallados por defecto (Fail)", str(data.SECTION_5_SUMMARY["fallaron"]), data.SECTION_5_SUMMARY["porcentaje_fallo"]),
        ("Casos bloqueados o con restricción indebida (Blocked)", str(data.SECTION_5_SUMMARY["bloqueados"]), data.SECTION_5_SUMMARY["porcentaje_bloqueo"])
    ]
    for r_i, (m_ind, m_cant, m_pct) in enumerate(metricas_rows, start=1):
        format_cell_text(tbl_metricas.rows[r_i].cells[0], m_ind, bold=True if r_i <= 2 else False, size_pt=9.5)
        format_cell_text(tbl_metricas.rows[r_i].cells[1], m_cant, bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_metricas.rows[r_i].cells[2], m_pct, bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        for c in tbl_metricas.rows[r_i].cells:
            set_cell_margins(c, 80, 80, 100, 100)
    insert_element_before_sectpr(doc, tbl_metricas._tbl)
    
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(4)
    p_sp.paragraph_format.space_after = Pt(8)
    insert_element_before_sectpr(doc, p_sp._p)

    add_doc_heading_2(doc, "5.2 Detalle de ejecución de casos")
    add_doc_paragraph(
        doc,
        "La siguiente tabla consolida la ejecución caso a caso, registrando el identificador, nombre de la prueba, "
        "el resultado obtenido y la evidencia técnica recopilada durante los ciclos de prueba (conforme a la estructura oficial de la Tabla 1):"
    )
    
    # Tabla Detalle Ejecucion (Table 1)
    tbl_exec = doc.add_table(rows=len(data.EXECUTION_DETAILS) + 3, cols=4)
    tbl_exec.style = 'Grid Table 4'
    set_table_borders(tbl_exec, color="B0C4DE", sz="4")
    
    # R0: Headers
    format_cell_text(tbl_exec.rows[0].cells[0], "CASO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_exec.rows[0].cells[1], "DESCRIPCIÓN", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_exec.rows[0].cells[2], "RESULTADO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_exec.rows[0].cells[3], "EVIDENCIA TÉCNICA", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl_exec.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)

    # R1: Categoria 1: Pruebas Funcionales
    tbl_exec.rows[1].cells[0].merge(tbl_exec.rows[1].cells[3])
    format_cell_text(tbl_exec.rows[1].cells[0], "PRUEBAS FUNCIONALES (MÓDULOS CRUD Y REGLAS DE NEGOCIO)", bold=True, size_pt=9.5)
    set_cell_background(tbl_exec.rows[1].cells[0], "E8E8E8")
    set_cell_margins(tbl_exec.rows[1].cells[0], 80, 80, 120, 120)
    
    row_cursor = 2
    for c_id, c_desc, c_res, c_evi in data.EXECUTION_DETAILS[:14]:
        format_cell_text(tbl_exec.rows[row_cursor].cells[0], c_id, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_exec.rows[row_cursor].cells[1], c_desc, bold=False, size_pt=9)
        res_color = RGBColor(0, 128, 0) if "Aprobado" in c_res else RGBColor(178, 34, 34)
        format_cell_text(tbl_exec.rows[row_cursor].cells[2], c_res, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=res_color)
        format_cell_text(tbl_exec.rows[row_cursor].cells[3], c_evi, bold=False, size_pt=8.5)
        for c in tbl_exec.rows[row_cursor].cells:
            set_cell_margins(c, 60, 60, 80, 80)
        row_cursor += 1

    # Categoria 2: Pruebas No Funcionales y Seguridad
    tbl_exec.rows[row_cursor].cells[0].merge(tbl_exec.rows[row_cursor].cells[3])
    format_cell_text(tbl_exec.rows[row_cursor].cells[0], "PRUEBAS NO FUNCIONALES, SEGURIDAD, RENDIMIENTO Y ACCESIBILIDAD", bold=True, size_pt=9.5)
    set_cell_background(tbl_exec.rows[row_cursor].cells[0], "E8E8E8")
    set_cell_margins(tbl_exec.rows[row_cursor].cells[0], 80, 80, 120, 120)
    row_cursor += 1

    for c_id, c_desc, c_res, c_evi in data.EXECUTION_DETAILS[14:]:
        format_cell_text(tbl_exec.rows[row_cursor].cells[0], c_id, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_exec.rows[row_cursor].cells[1], c_desc, bold=False, size_pt=9)
        res_color = RGBColor(0, 128, 0) if "Aprobado" in c_res else RGBColor(178, 34, 34)
        format_cell_text(tbl_exec.rows[row_cursor].cells[2], c_res, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=res_color)
        format_cell_text(tbl_exec.rows[row_cursor].cells[3], c_evi, bold=False, size_pt=8.5)
        for c in tbl_exec.rows[row_cursor].cells:
            set_cell_margins(c, 60, 60, 80, 80)
        row_cursor += 1

    insert_element_before_sectpr(doc, tbl_exec._tbl)

    p_sp2 = doc.add_paragraph()
    p_sp2.paragraph_format.space_before = Pt(4)
    p_sp2.paragraph_format.space_after = Pt(8)
    insert_element_before_sectpr(doc, p_sp2._p)

    add_doc_heading_2(doc, "5.3 Criticidad de incidentes")
    add_doc_paragraph(
        doc,
        "Para calificar objetivamente la severidad de los defectos identificados en el sistema Cuidarte+, "
        "se aplicó la escala de medición estandarizada del negocio (Tabla 2 del formato base). Cada incidente detectado "
        "se evalúa en función del nivel de impacto que provoca sobre la integridad, confidencialidad, disponibilidad y "
        "cumplimiento legal de los datos clínicos de los pacientes:"
    )

    # Tabla 2: Escala de Criticidad
    tbl_escala = doc.add_table(rows=len(data.SEVERITY_SCALE) + 1, cols=4)
    tbl_escala.style = 'Grid Table 4'
    set_table_borders(tbl_escala, color="B0C4DE", sz="4")
    
    format_cell_text(tbl_escala.rows[0].cells[0], "NIVEL", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_escala.rows[0].cells[1], "DESCRIPCIÓN DEL CRITERIO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_escala.rows[0].cells[2], "IMPACTO ASOCIADO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_escala.rows[0].cells[3], "ACCIÓN REQUERIDA", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl_escala.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)

    color_map = {
        "CRITICO": "FF0000",
        "GRAVE": "FFC000",
        "MODERADO": "FFFF00",
        "LEVE": "FFFFFF"
    }

    for r_i, (s_nivel, s_desc, s_imp, s_acc) in enumerate(data.SEVERITY_SCALE, start=1):
        cell_0 = tbl_escala.rows[r_i].cells[0]
        format_cell_text(cell_0, s_nivel, bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_background(cell_0, color_map.get(s_nivel, "FFFFFF"))
        
        format_cell_text(tbl_escala.rows[r_i].cells[1], s_desc, bold=False, size_pt=9)
        format_cell_text(tbl_escala.rows[r_i].cells[2], s_imp, bold=False, size_pt=9)
        format_cell_text(tbl_escala.rows[r_i].cells[3], s_acc, bold=False, size_pt=9)
        for c in tbl_escala.rows[r_i].cells:
            set_cell_margins(c, 80, 80, 100, 100)
    insert_element_before_sectpr(doc, tbl_escala._tbl)

    p_sp3 = doc.add_paragraph()
    p_sp3.paragraph_format.space_before = Pt(4)
    p_sp3.paragraph_format.space_after = Pt(8)
    insert_element_before_sectpr(doc, p_sp3._p)

    add_doc_paragraph(
        doc,
        "A continuación se presenta la matriz de incidentes identificados durante la ejecución de las pruebas "
        "(conforme a la Tabla 3 oficial), detallando el caso de prueba origen, descripción técnica del defecto, "
        "el resultado obtenido y su nivel de criticidad asignado con su correspondiente código cromático de alerta:"
    )

    # Tabla 3: Incidentes Identificados
    tbl_inc = doc.add_table(rows=len(data.INCIDENTS_IDENTIFIED) + 3, cols=4)
    tbl_inc.style = 'Grid Table 4'
    set_table_borders(tbl_inc, color="B0C4DE", sz="4")
    
    format_cell_text(tbl_inc.rows[0].cells[0], "CASO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_inc.rows[0].cells[1], "DESCRIPCIÓN DEL DEFECTO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_inc.rows[0].cells[2], "RESULTADO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_inc.rows[0].cells[3], "IMPACTO", bold=True, size_pt=9.5, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl_inc.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)

    # Categoria Funcionales
    tbl_inc.rows[1].cells[0].merge(tbl_inc.rows[1].cells[3])
    format_cell_text(tbl_inc.rows[1].cells[0], "INCIDENTES EN PRUEBAS FUNCIONALES", bold=True, size_pt=9.5)
    set_cell_background(tbl_inc.rows[1].cells[0], "E8E8E8")
    set_cell_margins(tbl_inc.rows[1].cells[0], 80, 80, 120, 120)

    cur_row = 2
    for inc_id, cp_id, inc_desc, inc_res, inc_imp in data.INCIDENTS_IDENTIFIED[:3]:
        format_cell_text(tbl_inc.rows[cur_row].cells[0], f"{inc_id} ({cp_id})", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_inc.rows[cur_row].cells[1], inc_desc, bold=False, size_pt=9)
        format_cell_text(tbl_inc.rows[cur_row].cells[2], inc_res, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=RGBColor(178, 34, 34))
        
        cell_imp = tbl_inc.rows[cur_row].cells[3]
        format_cell_text(cell_imp, inc_imp, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_background(cell_imp, color_map.get(inc_imp, "FFFFFF"))
        for c in tbl_inc.rows[cur_row].cells:
            set_cell_margins(c, 70, 70, 90, 90)
        cur_row += 1

    # Categoria No Funcionales
    tbl_inc.rows[cur_row].cells[0].merge(tbl_inc.rows[cur_row].cells[3])
    format_cell_text(tbl_inc.rows[cur_row].cells[0], "INCIDENTES EN PRUEBAS NO FUNCIONALES Y SEGURIDAD", bold=True, size_pt=9.5)
    set_cell_background(tbl_inc.rows[cur_row].cells[0], "E8E8E8")
    set_cell_margins(tbl_inc.rows[cur_row].cells[0], 80, 80, 120, 120)
    cur_row += 1

    for inc_id, cp_id, inc_desc, inc_res, inc_imp in data.INCIDENTS_IDENTIFIED[3:]:
        format_cell_text(tbl_inc.rows[cur_row].cells[0], f"{inc_id} ({cp_id})", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_inc.rows[cur_row].cells[1], inc_desc, bold=False, size_pt=9)
        format_cell_text(tbl_inc.rows[cur_row].cells[2], inc_res, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=RGBColor(178, 34, 34))
        
        cell_imp = tbl_inc.rows[cur_row].cells[3]
        format_cell_text(cell_imp, inc_imp, bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_background(cell_imp, color_map.get(inc_imp, "FFFFFF"))
        for c in tbl_inc.rows[cur_row].cells:
            set_cell_margins(c, 70, 70, 90, 90)
        cur_row += 1

    insert_element_before_sectpr(doc, tbl_inc._tbl)

    print("Construyendo Seccion 6: Analisis etico y normativo...")
    add_doc_heading_1(doc, "6. Análisis ético y normativo de los resultados obtenidos")
    add_doc_paragraph(doc, data.SECTION_6_TEXTS["etico_intro"])
    
    add_doc_heading_2(doc, "6.1 Vulneración de la Ley Nº 19.628 sobre Protección de la Vida Privada")
    add_doc_paragraph(doc, data.SECTION_6_TEXTS["ley_19628"])
    
    add_doc_heading_2(doc, "6.2 Vulneración de la Ley Nº 20.584 y deber legal de custodia de ficha clínica")
    add_doc_paragraph(doc, data.SECTION_6_TEXTS["ley_20584"])
    
    add_doc_heading_2(doc, "6.3 Riesgos penales bajo la Ley Nº 21.459 sobre Delitos Informáticos")
    add_doc_paragraph(doc, data.SECTION_6_TEXTS["ley_21459"])
    
    add_doc_heading_2(doc, "6.4 Responsabilidad bioética y deontología profesional en ingeniería de software")
    add_doc_paragraph(doc, data.SECTION_6_TEXTS["deontologia"])

    print("Construyendo Seccion 7: Matriz de trazabilidad y cobertura (100%)...")
    add_doc_heading_1(doc, "7. Matriz de trazabilidad y cobertura de requerimientos ERS (100%)")
    add_doc_paragraph(
        doc,
        "La siguiente matriz demuestra la cobertura total (100%) del plan de pruebas sobre la totalidad de requerimientos funcionales, "
        "no funcionales y reglas de negocio descritos en el documento de Especificación de Requerimientos de Software (ERS), "
        "vinculando cada ítem con el caso de prueba ejecutado, su estado y el estándar técnico o legal que lo fundamenta:"
    )

    tbl_matriz = doc.add_table(rows=len(data.TRACEABILITY_MATRIX) + 1, cols=5)
    tbl_matriz.style = 'Grid Table 4'
    set_table_borders(tbl_matriz, color="B0C4DE", sz="4")
    
    format_cell_text(tbl_matriz.rows[0].cells[0], "REQ ERS", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_matriz.rows[0].cells[1], "DESCRIPCIÓN DEL REQUERIMIENTO", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_matriz.rows[0].cells[2], "CASO ASOCIADO", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_matriz.rows[0].cells[3], "ESTADO QA", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    format_cell_text(tbl_matriz.rows[0].cells[4], "ESTÁNDAR / NORMATIVA", bold=True, size_pt=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in tbl_matriz.rows[0].cells:
        set_cell_background(c, "E8E8E8")
        set_cell_margins(c, 100, 100, 120, 120)

    for r_i, (m_req, m_desc, m_cp, m_est, m_norm) in enumerate(data.TRACEABILITY_MATRIX, start=1):
        format_cell_text(tbl_matriz.rows[r_i].cells[0], m_req, bold=True, size_pt=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell_text(tbl_matriz.rows[r_i].cells[1], m_desc, bold=False, size_pt=8.5)
        format_cell_text(tbl_matriz.rows[r_i].cells[2], m_cp, bold=False, size_pt=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        
        st_color = RGBColor(0, 128, 0) if "Aprobado" in m_est else RGBColor(178, 34, 34)
        format_cell_text(tbl_matriz.rows[r_i].cells[3], m_est, bold=True, size_pt=8.5, align=WD_ALIGN_PARAGRAPH.CENTER, color_rgb=st_color)
        format_cell_text(tbl_matriz.rows[r_i].cells[4], m_norm, bold=False, size_pt=8)
        for c in tbl_matriz.rows[r_i].cells:
            set_cell_margins(c, 50, 50, 70, 70)
    insert_element_before_sectpr(doc, tbl_matriz._tbl)

    print("Construyendo Seccion 8: Conclusiones y recomendaciones de remediacion...")
    add_doc_heading_1(doc, "8. Conclusiones y recomendaciones de mejora continua")
    
    add_doc_heading_2(doc, "8.1 Conclusiones generales del proceso de aseguramiento")
    add_doc_paragraph(doc, data.SECTION_8_TEXTS["conclusiones_p1"])
    add_doc_paragraph(doc, data.SECTION_8_TEXTS["conclusiones_p2"])
    
    add_doc_heading_2(doc, "8.2 Plan de remediación técnica inmediata")
    add_doc_paragraph(doc, data.SECTION_8_TEXTS["remediacion_intro"])
    for paso_titulo, paso_detalle in data.SECTION_8_TEXTS["remediacion_pasos"]:
        add_doc_bullet(doc, paso_titulo, paso_detalle, space_after=5)

    # Guardar documento
    print(f"Guardando documento final en {output_path}...")
    doc.save(output_path)
    print("Documento guardado con exito.")
    return output_path

if __name__ == "__main__":
    build_full_report()
