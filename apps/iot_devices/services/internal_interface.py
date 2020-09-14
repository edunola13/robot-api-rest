# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.conf import settings

from commons.connection.mqtt.client import ClientMqtt

from apps.manufacters.interfaces.internal.events import receive_signal


#
# This services know how send and receive from physic devices
# Strategies could be added by type
#
class InternalInterfaceService():

    def send_mqtt(self, device_id, data):
        connect_info = {
            'MQTT_USERNAME': settings.MQTT_SERVERS_IOT,
            'MQTT_PASSWORD': settings.MQTT_PASSWORD_IOT,
            'MQTT_HOST': settings.MQTT_HOST_IOT,
            'MQTT_PORT': settings.MQTT_PORT_IOT,
            'MQTT_KEEP_ALIVE': settings.MQTT_KEEP_ALIVE_IOT
        }

        self.client = ClientMqtt(connect_info)
        self.client.loop()

        self.client.publish_wait(
            'client/{}/sub/'.format(device_id),
            json.dumps(data)
        )

    def receive_mqtt(self, topic, payload):
        topic_splitted = topic.split("/")
        if len(topic_splitted) < 3:
            # Ignore
            return

        device_id = topic_splitted[1]
        method = topic_splitted[2]

        if method == "pub":
            receive_signal.send(
                sender=self.__class__,
                manufacter_id=settings.INTERNAL_MANUFACTER,
                device_id=device_id,
                data=payload
            )
        if method == "sub":
            # Escucharia lo que yo mando
            pass
