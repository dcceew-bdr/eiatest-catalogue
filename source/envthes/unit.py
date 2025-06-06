from rdflib import Graph, Literal
from rdflib.namespace import RDF, RDFS

g = Graph().parse("unit.ttl")
# q = """
#     PREFIX unit: <http://qudt.org/vocab/unit/>
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     PREFIX schema: <https://schema.org/>
#
#     CONSTRUCT {
#         ?c schema:name ?l_nolang
#     }
#     WHERE {
#         ?c
#             a qudt:Unit ;
#             rdfs:label ?l ;
#         .
#
#         BIND (STR(?l) AS ?l_nolang)
#
#         FILTER (LANG(?l) = "en")
#     }
#     """
# g.query(q).serialize(destination="unit-labels.ttl", format="turtle")

old_units = {
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abampere": "Abampere" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abcoulomb": "Abcoulomb" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abcoulombpersquarecentimeter": "Abcoulomb Per Square Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abfarad": "Abfarad" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abfaradpercentimeter": "Abfarad Per Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abhenry": "Abhenry" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abohm": "Abohm" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Absiemen": "Absiemen" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abtesla": "Abtesla" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Abvolt": "Abvolt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#AbvoltSecond": "Abvolt Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#AbvoltperCentimeter": "Abvolt Per Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Ampere": "Ampere" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#AmperePerRadian": "Ampere Per Radian" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#AmperePerSquareMeter": "Ampere Per Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#AmpereTurn": "Ampere Turn" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#AmpereTurnPerMeter": "Ampere Turn Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Becquerel": "Becquerel" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Candela": "Candela" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CandelaPerSquareMeter": "Candela Per Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Centimeter": "Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Centimeterpersecond": "Centimeter Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Centimeterpersecondsquared": "Centimeter Per Secondsquared" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Coulomb": "Coulomb" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CoulombMeter": "Coulomb Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CoulombPerCubicMeter": "Coulomb Per Cubic Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CoulombPerKilogram": "Coulomb Per Kilogram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CoulombPerMeter": "Coulomb Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CoulombPerMole": "Coulomb Per Mole" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CoulombPerSquareMeter": "Coulomb Per Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CubicCentimeter": "Cubic Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CubicMeter": "Cubic Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CubicMeterPerKelvin": "Cubic Meter Per Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CubicMeterPerKilogramSecondSquared": "Cubic Meter Per Kilogram Second Squared" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#CubicMeterPerSecond": "Cubic Meter Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Dyne": "Dyne" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Dynecentimeter": "Dynecentimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Dynepersquarecentimeter": "Dyne Per Square Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Erg": "Erg" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Ergpercubiccentimeter": "Erg Per Cubic Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Ergpersecond": "Erg Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Ergpersquarecentimetersecond": "Erg Per squarecentimeter Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Ergsecond": "Erg Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Farad": "Farad" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#FaradPerMeter": "Farad Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Gauss": "Gauss" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Gilbert": "Gilbert" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Gram": "Gram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Gray": "Gray" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#GrayPerSecond": "Gray Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Henry": "Henry" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#HenryPerMeter": "Henry Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Hertz": "Hertz" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Inversesecondtime": "Inverse Secondtime" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Joule": "Joule" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerCubicMeter": "Joule Per Cubic Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerCubicMeterKelvin": "Joule Per Cubic Meter Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerKelvin": "Joule Per Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerKilogram": "Joule Per Kilogram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerKilogramKelvin": "Joule Per Kilogram Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerKilogramKelvinPerCubicMeter": "Joule Per Kilogram Kelvin Per Cubic Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerKilogramKelvinPerPascal": "Joule Per Kilogram Kelvin Per Pascal" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerMole": "Joule Per Mole" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerMoleKelvin": "Joule Per Mole Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerSquareMeter": "Joule Per Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JoulePerTesla": "Joule Per Tesla" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#JouleSecond": "Joule Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Katal": "Katal" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Kelvin": "Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KelvinPerWatt": "Kelvin Per Watt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Kilogram": "Kilogram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramKelvin": "Kilogram Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramMeterPerSecond": "Kilogram Meter Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramMeterSquared": "Kilogram Meter Squared" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramPerCubicMeter": "Kilogram Per Cubic Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramPerMeter": "Kilogram Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramPerSecond": "Kilogram Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#KilogramPerSquareMeter": "Kilogram Per Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Lumen": "Lumen" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Lux": "Lux" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Maxwell": "Maxwell" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Meter": "Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterKelvin": "Meter Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterKelvinPerWatt": "Meter Kelvin Per Watt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterKilogram": "Meter Kilogram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterPerFarad": "Meter Per Farad" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterPerKelvin": "Meter Per Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterPerSecond": "Meter Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MeterPerSecondSquared": "Meter Per Second Squared" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Mole": "Mole" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MoleKelvin": "Mole Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MolePerCubicMeter": "Mole Per Cubic Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#MolePerKilogram": "Mole Per Kilogram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Newton": "Newton" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#NewtonMeter": "Newton Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#NewtonPerCoulomb": "Newton Per Coulomb" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#NewtonPerKilogram": "Newton Per Kilogram" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#NewtonPerMeter": "Newton Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Oersted": "Oersted" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Oerstedcentimeter": "Oersted Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Ohm": "Ohm" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Pascal": "Pascal" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#PascalSecond": "Pascal Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#PerMole": "Per Mole" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Poise": "Poise" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Radian": "Radian" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#RadianPerSecond": "Radian Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#RadianPerSecondSquared": "Radian Per Second Squared" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Relativepermeability": "Relativepermeability" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Relativepermittivity": "Relativepermittivity" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Second": "Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SecondTime": "Second Time" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SecondTimeSquared": "Second Time Squared" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Siemens": "Siemens" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Sievert": "Sievert" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SquareMeter": "Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SquareMeterKelvin": "Square Meter Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SquareMeterKelvinPerWatt": "Square Meter Kelvin Per Watt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SquareMeterPerKelvin": "Square Meter Per Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SquareMeterPerSecond": "Square Meter Per Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SquareMeterSteradian": "Square Meter Steradian" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Squarecentimeter": "Square Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Squarecentimetersecond": "Squarecentimeter Second" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statampere": "Statampere" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statcoulomb": "Statcoulomb" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statcoulombpersquarecentimeter": "Statcoulomb Per Square Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statfarad": "Statfarad" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Stathenry": "Stathenry" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Stathenrypercentimeter": "Stathenry Per  Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statohm": "Statohm" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statvolt": "Statvolt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Statvoltpercentimeter": "Statvolt Per  Centimeter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Steradian": "Steradian" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Tesla": "Tesla" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Unity": "Unity" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Volt": "Volt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#VoltPerMeter": "Volt Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Watt": "Watt" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#WattPerMeterKelvin": "Watt Per Meter Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#WattPerSquareMeter": "Watt Per Square Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#WattPerSquareMeterKelvin": "Watt Per Square Meter Kelvin" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#WattPerSquareMeterSteradian": "Watt Per Square Meter Steradian" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#WattPerSteradian": "Watt Per Steradian" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#Weber": "Weber" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#ity:AmperePerMeter": "Ampere Per Meter" ,
    "http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#ity:InverseSecondTime    ": "Inverse Second Time" ,
}

for k, v in old_units.items():
    for s in g.subjects(RDFS.label, Literal(v.lower(), lang="en")):
        print(f"{k},{s}")