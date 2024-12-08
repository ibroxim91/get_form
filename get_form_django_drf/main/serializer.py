from rest_framework import serializers

class DynamicKeySerializer(serializers.Serializer):
    def to_internal_value(self, data):
        if not isinstance(data, dict):
            raise serializers.ValidationError("Ожидался объект JSON.")

        validated_data = {}
        for key, value in data.items():
            # Пример: проверка типа значения
            if isinstance(value, str) and len(value) > 0:
                validated_data[key] = value
            else:
                raise serializers.ValidationError(f"Invalid value  for '{key}' ")
        
        return validated_data

    def to_representation(self, instance):
        return instance
