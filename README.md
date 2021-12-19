# ocrapi

##Env

```
Use python3.8
```

##How to run tests

```
cd ocrapi
pytest --alluredir=allure_results -v tests/
```

##How to see the report

```
Install allure to your system
https://docs.qameta.io/allure/#_installing_a_commandline
```

```
cd ocrapi
allure serve allure_results
```
