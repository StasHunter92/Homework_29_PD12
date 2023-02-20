# Курс 6. Домашняя работа SkyPRO PD 12
______________________________________
### Урок 29. Сериализаторы и вьюсеты
______________________________________

**Критерии выполнения:**

:white_check_mark: Работа с пользователями реализована через GenericView из DRF - 
ListApiView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

:white_check_mark: При выводе списка пользователей используется встроенная пагинация DRF

:white_check_mark: API для модели Location реализовано с использованием ViewSet и Router

:white_check_mark: В проекте используются Serializers

:white_check_mark: Все фильтры выполнены с использованием lookup's

:white_check_mark: Типы данных в JSON отдаются корректно

:white_check_mark: Методы из спецификации работают
______________________________________
**Примечания:**

:negative_squared_cross_mark: Заполнение базы через `raw_data/import_data.py` происходит не полностью, 
ManyToMany заполнялись вручную