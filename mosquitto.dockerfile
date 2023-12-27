# 使用官方的 Mosquitto 镜像作为基础镜像
FROM eclipse-mosquitto

# 暴露 MQTT 默认端口（1883）
EXPOSE 1883

