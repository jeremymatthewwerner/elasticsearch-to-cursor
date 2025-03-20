# Cursor Configuration for Elasticsearch

This directory contains configuration files and setup instructions for developing Elasticsearch using Cursor editor instead of IntelliJ IDEA.

## Setup Instructions

1. Install Cursor from [cursor.sh](https://cursor.sh)
2. Install required extensions:
   - Extension Pack for Java
   - Gradle for Java
   - Spring Boot Extension Pack (if working with Spring components)
3. Configure JDK settings
4. Set up Gradle integration

## Required Extensions

The following VS Code extensions are required for Java development in Cursor:

- **Extension Pack for Java**: Includes Java language support, debugger, test runner, Maven support, and project manager
- **Gradle for Java**: Essential for working with Gradle build system
- **Spring Boot Extension Pack**: Required for Spring Boot development (if applicable)

## JDK Configuration

Ensure your JDK is properly configured in Cursor's settings.json:

```json
{
  "java.jdt.ls.java.home": "/path/to/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/path/to/jdk-17",
      "default": true
    }
  ]
}
```

## Gradle Integration

Elasticsearch uses Gradle for build configuration. Cursor supports Gradle through the Gradle for Java extension.

### Gradle Wrapper

The project uses Gradle Wrapper which will automatically download and use the correct Gradle version. No additional configuration is needed.

## Code Style and Formatting

Elasticsearch uses the Eclipse formatter for code style. To maintain consistent formatting:

1. Install the "Checkstyle for Java" extension
2. Configure it to use the Elasticsearch checkstyle configuration

## Debugging and Running

Use the Run and Debug sidebar panel to start debugging sessions. You can also execute Gradle tasks from the terminal.

## Migration Notes

This configuration aims to provide equivalent functionality to the IntelliJ setup while leveraging Cursor's AI-powered features for Java development.

Key differences from IntelliJ:
- Uses VS Code extensions instead of IntelliJ plugins
- Gradle integration through VS Code Gradle extension
- Different keyboard shortcuts and UI layout
- AI-powered code completion and generation
