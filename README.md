# 📇 Tarjeta Virtual Interactiva / Digital Business Card

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

Una solución moderna, responsive y elegante para compartir tu perfil profesional, redes sociales y datos de contacto de manera centralizada e interactiva.

---

## 📑 Tabla de Contenidos

- [Características](#-características)
- [Demostración](#-demostración)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso y Personalización](#-uso-y-personalización)
- [Despliegue](#-despliegue)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## ✨ Características

- 📱 **Diseño Responsive & Mobile-First:** Adaptado para visualizarse perfectamente en cualquier dispositivo (smartphones, tablets y desktop).
- 🎨 **Soporte Tema Claro / Oscuro (Dark Mode):** Detección automática de preferencias del sistema o alternador manual.
- 🔗 **Enlaces Directos y Redes Sociales:** Accesos rápidos a GitHub, LinkedIn, Twitter/X, Portfolio, etc.
- ⚡ **Descarga de vCard (.vcf):** Permite a los usuarios guardar tu contacto directamente en su agenda con un solo clic.
- 📲 **Código QR Integrado:** Generación de código QR dinámico para compartir la tarjeta escaneando la pantalla.
- 🚀 **Carga Ultrarrápida:** Optimizado para un rendimiento excelente sin dependencias pesadas.

---

## 🖼 Demostración

*(Añade aquí capturas de pantalla o un GIF animado del proyecto en funcionamiento)*

| Modo Claro | Modo Oscuro |
| :---: | :---: |
| ![Preview Light](./docs/preview-light.png) | ![Preview Dark](./docs/preview-dark.png) |

---

## 🛠 Tecnologías Utilizadas

- **HTML5:** Estructura semántica.
- **CSS3 / Tailwind CSS / Sass:** Estilos modernos, animaciones y diseño responsivo.
- **JavaScript (ES6+):** Interactividad, toggle de tema y lógica de descarga de datos.
- **Iconos:** [FontAwesome](https://fontawesome.com/) / [Lucide Icons](https://lucide.dev/).

---

## 📁 Estructura del Proyecto

```text
tarjeta-virtual/
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   ├── img/
│   │   ├── profile.jpeg
│   │   └── qr-code.png
│   └── vcard/
│       └── contact.vcf
├── docs/
│   ├── preview-light.png
│   └── preview-dark.png
├── index.html
├── README.md
└── LICENSE
```

---

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tarjeta-virtual.git
   ```

2. **Navegar al directorio del proyecto:**
   ```bash
   cd tarjeta-virtual
   ```

3. **Abrir el proyecto:**
   - Puedes abrir directamente `index.html` en tu navegador.
   - O utilizar una extensión de servidor local como **Live Server** en VS Code.

---

## ⚙️ Uso y Personalización

Para adaptar esta tarjeta a tu información personal:

1. **Información Personal:** Abre `index.html` y modifica los textos correspondientes a tu nombre, título profesional y descripción.
2. **Foto de Perfil:** Reemplaza la imagen en `assets/img/profile.jpeg` con tu propia fotografía.
3. **Redes Sociales:** Actualiza los atributos `href` de los enlaces con tus perfiles reales.
4. **vCard:** Modifica el archivo `assets/vcard/contact.vcf` con tus datos de contacto reales para la función de importación.

---

## 🌐 Despliegue

Puedes desplegar este proyecto gratis en plataformas populares:

- **GitHub Pages:**
  1. Ve a `Settings` > `Pages` en tu repositorio.
  2. Selecciona la rama `main` (o `master`) y guarda.
- **Vercel / Netlify:**
  1. Conecta tu cuenta de GitHub.
  2. Importa el repositorio y despliega con un clic.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias para mejorar este proyecto:

1. Haz un **Fork** del proyecto.
2. Crea una rama para tu función (`git checkout -b feature/NuevaFuncion`).
3. Haz **Commit** de tus cambios (`git commit -m 'Añadir NuevaFuncion'`).
4. Haz **Push** a la rama (`git push origin feature/NuevaFuncion`).
5. Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## ✉️ Contacto

- **Nombre:** Tu Nombre
- **Email:** tuemail@ejemplo.com
- **LinkedIn:** [linkedin.com/in/tu-perfil](https://linkedin.com/in/tu-perfil)
- **Sitio Web:** [tuweb.com](https://tuweb.com)