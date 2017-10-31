# IPFS WEBPAGES API

Search API for IPFS webpages

## Add a Register

In order to add a register, go to /add/**name**/**link**/ where **name** is the name of the webpage (can contain spaces) and **link** is the hash of the ipfs link to the content.

## Search for a Register

In order to search for a register, go to /search/**query**/ where query is a word supposed to be in at least one of the Register's names. If no matching register is found, the API will return an empty json **[]**. If one or more Registers are found, they will be returned in a json of objects with two atributes each: name and link.