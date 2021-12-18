# REST API for Chemistry

Server uses Python/Flask to run.

## To start:
```
source venv/bin/activate
python3 chemapi.py
```

## API Calls
``` chemapi/ or / ``` : Returns entire JSON data for all atoms. <br>
``` chemapi/atoms/ ``` : Returns all atom name. <br>

``` chemapi/symbols/ ``` : Returns all atom symbols. <br>

``` chemapi/groupblocks/ ``` : Returns all group blocks in JSON data.

``` chemapi/atoms/properties/ ``` : Returns all properties an atom an have.

``` chemapi/<string:atom-name>/ ``` : Returns atom properties for a given atom. <br>
+ For example: ``` chemapi/hydrogen/ ```

``` chemapi/<string:atom-name>/<string:property>/ ``` : Returns an atom property for a given atom. <br>
+ For example: ``` chemapi/hydrogen/oxidationStates```

``` chemapi/atoms/<string:groupblock> ``` : Returns all atom names in a given group block.
+ For example: ``` chemapi/atoms/metal/ ```
