# Django REST Framework Examples

A comprehensive collection of Django REST Framework (DRF) examples to understand and practice core concepts of DRF with simple, clean code.

This repository is ideal for beginners who want to get hands-on experience with DRF by exploring examples for serializers, views, routers, pagination, versioning, filtering, and more.

---

## ✅ Topics Covered

Each example demonstrates a specific concept of DRF:

- **🧩 Serializers**
  - Basic Serializer and ModelSerializer
  - Nested Serializers
- **🧠 Function-Based Views**
  - Using `@api_view`
  - Return JSONResponse / Response with decorators
- **🏗️ Class-Based Views (APIView)**
  - Inheritance from `APIView`
  - Use of `get`, `post`, `put`, and `delete` methods
- **🔁 Mixins & Generic Views**
  - `ListModelMixin`, `CreateModelMixin`, `RetrieveModelMixin`, etc.
  - Combined with `GenericAPIView`
- **🧰 ViewSets & Routers**
  - `ModelViewSet` with `DefaultRouter` to auto-generate routes
- **🔍 Filtering & Searching**
  - Query parameter filtering
  - `DjangoFilterBackend` integration
  - Search and ordering filters
- **📏 Pagination**
  - Page Number Pagination
  - LimitOffset Pagination
- **🧾 Versioning**
  - URL-based and namespace versioning
- **📄 API Documentation**
  - Swagger / OpenAPI schema generation

---

## 📁 Project Structure

```bash
Django-Rest-Framework/
├── drf_example/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── example_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
