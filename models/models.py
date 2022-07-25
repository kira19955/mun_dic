# -*- coding: utf-8 -*-
from odoo import models, fields, api


class datosGenerales(models.Model):
    _name = 'datosgenerales'

    name = fields.Char(string="Nombre")
    # departamento = fields.Many2one()
    tipo_de_peticion = fields.Selection(
        string='Tipo de peticion',
        selection=[('m', 'Memo'),
                   ('o', 'Oficio'),
                   ('t', 'Telefonico'),
                   ('p', 'Personal'), ])

    # TOMA LA FECHA Y LA HORA DE FORMA AUTOMATICA DEL SERVIDOR
    fecha_hora = fields.Datetime(string="Fecha y Hora",
                                 default=lambda self: fields.Datetime.now(), readonly=True)
    # TOMA EL USUARIO QUE SE LOGUEA
    recibe = fields.Many2one('res.users', 'Recibe', default=lambda self: self.env.user, readonly=True)

    solitudes_ids = fields.One2many(
        comodel_name='solicitudes',
        inverse_name='solicitud_id',
        string='Solitudes')


class solicitudes(models.Model):
    _name = 'solicitudes'

    serie = fields.Char(string="Serie")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    inventario = fields.Char(string="Inventario")
    descripcion = fields.Text(string="Descripcion")
    ubicacion = fields.Char(string="Ubicacion")
    ext = fields.Char(string="Ext")
    equipo = fields.Many2one(comodel_name="tipo_de_equipo")
    situacion = fields.Many2one(comodel_name="situacion")
    tipo_solicitud = fields.Selection([('computo', 'Computo'),
                                       ('telefonia', 'Telefonia'),
                                       ('redes', 'Redes'),
                                       ('sistemas', 'Sistemas'),
                                       ('diseño', 'Diseño'),
                                       ('prestamos', 'Prestamos'),
                                       ('administracion', 'Administracion')],
                                      string="Tipo de Solicitud")
    solicitud_id = fields.Many2one(comodel_name="datosgenerales")
    responsable = fields.Many2one(comodel_name="res.users")

class TipoDeMantenimiento(models.Model):
        _name = 'tipo_de_mantenimiento'

        name = fields.Char(string="Descripción")

class mantenimiento(models.Model):
        _name = 'mantenimiento'

        name = fields.Char(string="Descripción")
        tipo = fields.Many2one(comodel_name="tipo_de_mantenimiento")
        costo = fields.Char(string="Costo")

class TipoDeEquipo(models.Model):
        _name = 'tipo_de_equipo'
        _description = 'Catalogo de los diferentes tipos de equipos que hay'

        name = fields.Char(string="Descripción")

class Situacion(models.Model):
        _name = 'situacion'
        _description = 'Catalogo de los diferentes tipos de situacion'

        name = fields.Char(string="Descripción")

class CentroDeServicios(models.Model):
        _name = 'centro_de_servicios'
        _description = 'Catalogo de centro de servicios'

        name = fields.Char(string="Descripción")
        tel = fields.Char(string="Teléfono")
        direccion = fields.Char(string="Dirección")


        """
        FALTAN LOS MODELOS DE CATALOGO DE MATERIAL Y 
        CATALOGO DE UNIDAD DE MEDIDA, PARA CUESTIONES DE INVENTARIO 
        CHECAR EL MODULO DE INVENTARIO DE ODOO Y VER COMO FUNCIONA
        """
