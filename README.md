# Python Template - Dynamo for Revit

## Description
This repository contains a Python template designed to be used within the Python Script node in Dynamo for Revit workflows.

It includes a collection of libraries frequently utilized in my developments, alongside various methods and classes I sporadically employ. 

The intention is to provide a foundational script that can be adapted and expanded upon for diverse and complex Revit automation tasks.

## Configuration of Python Template in Dynamo for Revit

1. **Locate DynamoSettings.xml File**: Navigate to `%appdata%\Dynamo\Dynamo Core\{version}\`. 
2. **Edit Template Path**: Add or modify the `<PythonTemplateFilePath>` line in the `DynamoSettings.xml` file to:
   ```xml
   <PythonTemplateFilePath>
      <string>C:\Users\CURRENTUSER\AppData\Roaming\Dynamo\Dynamo Core\2.0\PythonTemplate.py</string>
   </PythonTemplateFilePath>
   ```


	***Replace `CURRENTUSER` with your windows username.***

<br>

3. **Create and Save the Template**: Build a Python script with the desired functionality and save it as `PythonTemplate.py` in the `APPDATA location.

## Best Practices
- **Documentation**: Comment your code generously. Explain what each major block or function does, especially if the logic is complex.
- **Error Handling**: Always include error handling to manage and anticipate failures gracefully.
- **Version Control**: Keep track of changes and versions of your scripts, especially as they grow in complexity and number.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
**Maycon Freitas** 

[![Email](/resources/gmail.png)](mailto:maycon.freitas@aecoder.com.br) 
[![LinkedIn](/resources/linkedin.png)](https://www.linkedin.com/in/maycon-freitas/)


Project Link: [https://github.com/mayconrfreitas/dynamo-revit-python-template](https://github.com/mayconrfreitas/dynamo-revit-python-template)