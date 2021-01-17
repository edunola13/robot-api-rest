# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.manufacters.interfaces.interfaces import ManufacterInterfaceService

from iot_devices.proto.devices_pb2 import Payload
from iot_devices.proto.wrapper import PayloadWrapper

from apps.devices.constants import QUERY_SYNC, QUERY_STATE

from apps.devices.models import Device

from .events import send_signal


class ManufacterInternalService(ManufacterInterfaceService):
    """Manufacter Internal Service."""

    def __init__(self, manufacter):
        self.manufacter = manufacter

    def send(self, device: Device, data: Payload):
        """Este envia a iot_devices el cual conoce y respeta el formato."""
        assert device.is_ready()

        send_signal.send(
            sender=self.__class__,
            device_id=device.external_id,
            data=data
        )

    def receive(self, device_id: str, payload: Payload):
        """
        Este recibe desde iot_devices el cual conoce y respeta el formato.

        Desde este punto arranca la ejecucion de la logica de Hibris IOT.
            - Actualizacion de modelos.
            - Registro de los eventos.
            - Ejecucion de reglas.
        """
        device = Device.objects.get(
            external_id=device_id,
            manufacter=self.manufacter
        )

        if payload.type == Payload.PayloadType.SYNC:
            device.receive_sync(PayloadWrapper(payload))

        # If no ready can receive anything else
        if not device.is_ready():
            return

        if payload.type == Payload.PayloadType.STATE:
            device.receive_state(PayloadWrapper(payload))
