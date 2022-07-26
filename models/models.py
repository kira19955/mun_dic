# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)




class datosGenerales(models.Model):
    _name = 'datosgenerales'

    name = fields.Char(string="Solicitante")
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
    direccion = fields.Many2one(comodel_name="directorio_municipal.directorio_municipal", string="Direccion")
    unidad = fields.Many2one(comodel_name="directorio_municipal.directorio_municipal", string="Unidad")
    status = fields.Many2one(comodel_name="situacion", default=lambda s: s._default_situacion())

    num_presupuesto = fields.Char(string="Numero de presupuesto", copy=False)

    ##funcion create necesita un decorador
    @api.model
    def create(self, variables):
        logger.info("*** variables{0}".format(variables))
        secuencia = self.env['ir.sequence']
        correlativo = secuencia.next_by_code('secuencia.servicios.dic')
        variables['num_presupuesto'] = correlativo
        return super(datosGenerales, self).create(variables)


    """
    FALTA AGREGAR EL id PARA QUE SEA VISIBLE Y CONSECUTIVO Y EL SE ENTREGA A: 
    """

    @api.model
    def _default_situacion(self):
        """
            funcion que busca en el modulo de situaciones, el stado de no atendida para ser
            el default al crear una solicitud
        """
        return self.env['situacion'].search([('name', '=', 'NO ATENDIDA')], limit=1).id

    def vale_salida(self):
        return self.env.ref('mun_dic.recepcion_equipo').report_action(self)





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
    situacion = fields.Many2one(comodel_name="situacion",default=lambda s: s._default_situacion())
    tipo_solicitud = fields.Selection([('computo', 'Computo'),
                                       ('telefonia', 'Telefonia'),
                                       ('redes', 'Redes'),
                                       ('sistemas', 'Sistemas'),
                                       ('diseño', 'Diseño'),
                                       ('prestamos', 'Prestamos'),
                                       ('administracion', 'Administracion')],
                                      string="Tipo de Solicitud: ", default="computo")
    solicitud_id = fields.Many2one(comodel_name="datosgenerales")
    responsable = fields.Many2one(comodel_name="res.users", domain=lambda self: [('groups_id', 'in', self.env.ref('mun_dic.group_tecnico').id)])
    fch_evento = fields.Date(string="Fecha Evento")
    hora_evento = fields.Char(string="Hora del Evento")
    hora_entrega = fields.Char(string="Hora de Entrega")
    num_presupuesto = fields.Char(string="Numero de presupuesto", copy=False)

    ##funcion create necesita un decorador
    @api.model
    def create(self, variables):
        logger.info("*** variables{0}".format(variables))
        secuencia = self.env['ir.sequence']
        correlativo = secuencia.next_by_code('secuencia.servicios.peticion')
        variables['num_presupuesto'] = correlativo
        return super(solicitudes, self).create(variables)

    """
       FALTA AGREGAR EL id PARA QUE SEA VISIBLE Y CONSECUTIVO
    """

    #AQUI EMPIEZAN LAS FUNCIONES


    @api.model
    def _default_situacion(self):
        """
            funcion que busca en el modulo de situaciones, el stado de no atendida para ser
            el default al crear una solicitud
        """
        return self.env['situacion'].search([('name', '=', 'NO ATENDIDA')], limit=1).id


class TipoDeMantenimiento(models.Model):
        _name = 'tipo_de_mantenimiento'

        name = fields.Char(string="Nombre")

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


