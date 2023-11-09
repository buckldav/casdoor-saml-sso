## SAML Setup

1. docker-compose

```bash
docker compose up -d --build
```

2. Master (Identity Provider, IDP)

```
# master database

casdoor=# SELECT name,client_id,client_secret,enable_auto_signin,redirect_uris,saml_reply_url,enable_saml_compress FROM application;
     name     |      client_id       |              client_secret               | enable_auto_signin |           redirect_uris           |        saml_reply_url         | enable_saml_compress
--------------+----------------------+------------------------------------------+--------------------+-----------------------------------+-------------------------------+----------------------
 app-built-in | 676ab8b646ecc0eba7e2 | f194aa437bff81a6e94629a5d9b167080c5c52ef | f                  | ["http://localhost:8001/api/acs"] | http://localhost:8001/api/acs | f
```

SAML Metadata (app-built-in on master)

```xml
<EntityDescriptor xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="http://localhost:8000">
  <IDPSSODescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <KeyDescriptor use="signing">
      <KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">
        <X509Data xmlns="http://www.w3.org/2000/09/xmldsig#">
          <X509Certificate xmlns="http://www.w3.org/2000/09/xmldsig#">MIIE3TCCAsWgAwIBAgIDAeJAMA0GCSqGSIb3DQEBCwUAMCgxDjAMBgNVBAoTBWFkbWluMRYwFAYDVQQDEw1jZXJ0LWJ1aWx0LWluMB4XDTIzMTEwOTIwMjcyOVoXDTQzMTEwOTIwMjcyOVowKDEOMAwGA1UEChMFYWRtaW4xFjAUBgNVBAMTDWNlcnQtYnVpbHQtaW4wggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCpviBJPffAAjbMxceFxcMmhhgOGTXWTeMed4yyD9k1QmNTUQq0fTVHqW20HfIHu4YHFE4dw9AImFvTTnvSjC6hZPbFtLrTW/qOYI3bqZvsKXlsOxs1a3LYWctljxZ50JoMzBoEyUG7O5p3vMmzLR9v7YaAvFq0Xt180XHunutw3zg2R9F5w4eh+GW884Ux9jb1TcV23yxb3kyyBZu8ZwvaIS9ga+ckGRhGf/ReK954SIxNatZ/7hV0csrxvXW+bl2WPxoLD3qn3AYjRnuhGbLwd8PiJ8lW1E9lnniDp9v8WP4elxQG3edh56Sv8sdAkvVDVz3p0wdmFJKUIDS9sGGv2RLkCBNwGm+WRudxaV09GVjPmgTV/LzmX1VJA+WAobv9n3xpDK1dYfVDFBanlT3+QsiaZ/vn/vJ4bibRzeqtXONMqxVMI/1fO8Yk7IHFU060p4F1G7rK9qq0cbWLscpJDwy49vmJUkwBJmoSjolydz3d42i775yMlGv57jplTIQppTg/UFYj7oUCYpj5HtVM+DdaH+QRa8w1zAxD71Il/rvvgxf+2GmpX7Gr4tUHWuQXAJhHvoToaJZ/YReAUqri7tZ8l5zaBct/bWnmW/rRa16Fe/DfMmTkuYBRqdhL3WPBRqbII7qa/QZMXfhZAX/JY3KgmmfIZwp1pDFC0m2CyQIDAQABoxAwDjAMBgNVHRMBAf8EAjAAMA0GCSqGSIb3DQEBCwUAA4ICAQCeXiZ0aujqQM176xaRiIjvwiE5WdIsMKGlBWu25jdkbt/MC/aWPJLMzv5yb0t61hhYvIWwpvL7fJ1yXAJcjCBkEWVg/L7S/8mgPC593lP5iDxxDpo36QTW7Jv5aoeN+vlTD2T95yukYvEUJtt56y/oDfW45wiYGe76TSm215xq5d9COe+FEpAFwLWkh/Y77NOtftNDQhhjP/u7bElOl4CCbEYwR/z3DzJjx2MmkpKQh+oYF981oZ24FZoQpVBPFq0GStiDSnRuSo+RX3clTHGPpHzDlaV1zS+fUXDoygHS53IkUxtUJaxGD2Tu3/i+z4Qw8kY0gZqdV8Ul9gTrBkjTSUkX9EP+l19UX0x8tVStUZFjgv6JqTWi9XvZEgnL6qlnvuKRT+C8STBazHwSQMhIrOYiOIL2KQDmYPH8CHvZEpOpjS77bxOoMXNpqIdOweskM7cmEFARTKchckqZvqqJg4OMDJwmVZCXZ4IUULNjVFjZ+y6FL4RFb7JacGf5QgeefTJTG2VDq6aSr4sXrWuZW6cm0zMouQGWFvZ6JMAxLHiPct8Hq7iMCEVM43vXV3WaB4a+Ev7FB+iPe/EbG8YD+Cn25EVoIg+WABdfC3oB9DLLhrTZAy5J9kq5iPU0yEMg5w7PSYuKV2Ok9jbhDGT45xyg1x1ZYKiK4Kio4yWa1g==</X509Certificate>
        </X509Data>
      </KeyInfo>
    </KeyDescriptor>
    <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
    <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>
    <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
    <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="http://localhost:8000/login/saml/authorize/admin/app-built-in"></SingleSignOnService>
    <Attribute Name="Email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" FriendlyName="E-Mail" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"></Attribute>
    <Attribute Name="DisplayName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" FriendlyName="displayName" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"></Attribute>
    <Attribute Name="Name" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" FriendlyName="Name" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"></Attribute>
  </IDPSSODescriptor>
</EntityDescriptor>
```

3. Provider on Single

Use the SAML Metadata listed above.

```
casdoor=# SELECT name,method,client_id,client_secret,category,type FROM provider WHERE name='provider_master_saml';
         name         | method |      client_id       |              client_secret               | category |  type
----------------------+--------+----------------------+------------------------------------------+----------+--------
 provider_master_saml | Normal | 676ab8b646ecc0eba7e2 | f194aa437bff81a6e94629a5d9b167080c5c52ef | SAML     | Custom
```

4. Create User on BOTH Master and Single Instances

Visit `http://localhost:8000/users/` and `http://localhost:8001/users/`. Upload the `user-data/user_init.xlsx` file that contains 1 user with the following credentials:

```
name: test1
password: 123
```

## SAML SSO

https://casdoor.org/docs/how-to-connect/single-sign-on/
