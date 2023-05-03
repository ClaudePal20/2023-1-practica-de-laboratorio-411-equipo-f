#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
import Incremento
import DailyScrum
import ProductBacklog
class SprintDesarrollo(ProductBacklog):
	__metaclass__ = ABCMeta
	@classmethod
	def getEtapas(self):
		"""@ReturnType void"""
		pass
	@classmethod
	def setEtapas(self, aEtapas):
		self.___etapas = aEtapas
	@classmethod
	def __init__(self):
		self.___etapas = None
		"""@AttributeType int"""
		self.___reuniones = None
		"""@AttributeType int"""
		self.___busqueda_de_mejoras = None
		# @AssociationType Incremento
		# @AssociationKind Composition
		self.___reportesDiarios = None
		# @AssociationType DailyScrum
		# @AssociationMultiplicity 1
		self.___equipo = None
		self.___tiempos = None

