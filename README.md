# coding-assignment-dlo
Basic CLI application which generates DLO authenticated urls. To install run:
```bash
poetry install
```

To see the cli commands run:
```bash
poetry run url-generator --help
```

The app has two commands, `get-client-url` and `get-professional-url`. For more
information relating to the individual commands run e.g:

```bash
poetry run url-generator get-professional-url --help
```

The signature of the commands is the same. In order to get a professional url run:
```bash
poetry run url-generator get-professional-url catalogue
    --user-id <USER_ID> \
    --secret-key <DLO_KEY> \
    --base-url <BASE_URL>
```

The command will print the generated url which can then be copied into a browser.
Try this in incognito/ private mode to ensure the authentication works.
Check the `--help` function for the permitted routes which can be generated. If 
`secret-key` is not provided, the app retrieves the value from the `DLO_KEY` env 
variable. The `base-url` parameter defaults to `https://ca-isnaitic.minddistrict.dev`.


Github actions used to perform static analysis and some basic unit tests.
