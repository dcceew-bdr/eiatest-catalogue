from rdflib import Graph, URIRef, RDFS
import httpx

concepts = [
    "http://purl.obolibrary.org/obo/AGRO_00000301" ,
    "http://purl.obolibrary.org/obo/APOLLO_SV_00000445" ,
    "http://purl.obolibrary.org/obo/APO_0000100" ,
    "http://purl.obolibrary.org/obo/BTO_0001181" ,
    "http://purl.obolibrary.org/obo/CARO_0000043" ,
    "http://purl.obolibrary.org/obo/CHEBI_30050" ,
    "http://purl.obolibrary.org/obo/CHEBI_10545" ,
    "http://purl.obolibrary.org/obo/CHEBI_15377" ,
    "http://purl.obolibrary.org/obo/CHEBI_16130" ,
    "http://purl.obolibrary.org/obo/CHEBI_16526" ,
    "http://purl.obolibrary.org/obo/CHEBI_16646" ,
    "http://purl.obolibrary.org/obo/CHEBI_18059" ,
    "http://purl.obolibrary.org/obo/CHEBI_18230" ,
    "http://purl.obolibrary.org/obo/CHEBI_18248" ,
    "http://purl.obolibrary.org/obo/CHEBI_18291" ,
    "http://purl.obolibrary.org/obo/CHEBI_18422" ,
    "http://purl.obolibrary.org/obo/CHEBI_22984" ,
    "http://purl.obolibrary.org/obo/CHEBI_23044" ,
    "http://purl.obolibrary.org/obo/CHEBI_23116" ,
    "http://purl.obolibrary.org/obo/CHEBI_24127" ,
    "http://purl.obolibrary.org/obo/CHEBI_24527" ,
    "http://purl.obolibrary.org/obo/CHEBI_24866" ,
    "http://purl.obolibrary.org/obo/CHEBI_25107" ,
    "http://purl.obolibrary.org/obo/CHEBI_25491" ,
    "http://purl.obolibrary.org/obo/CHEBI_25555" ,
    "http://purl.obolibrary.org/obo/CHEBI_25944" ,
    "http://purl.obolibrary.org/obo/CHEBI_26195" ,
    "http://purl.obolibrary.org/obo/CHEBI_26216" ,
    "http://purl.obolibrary.org/obo/CHEBI_26708" ,
    "http://purl.obolibrary.org/obo/CHEBI_26833" ,
    "http://purl.obolibrary.org/obo/CHEBI_26848" ,
    "http://purl.obolibrary.org/obo/CHEBI_27027" ,
    "http://purl.obolibrary.org/obo/CHEBI_27325" ,
    "http://purl.obolibrary.org/obo/CHEBI_27363" ,
    "http://purl.obolibrary.org/obo/CHEBI_27560" ,
    "http://purl.obolibrary.org/obo/CHEBI_27568" ,
    "http://purl.obolibrary.org/obo/CHEBI_27573" ,
    "http://purl.obolibrary.org/obo/CHEBI_27594" ,
    "http://purl.obolibrary.org/obo/CHEBI_27638" ,
    "http://purl.obolibrary.org/obo/CHEBI_27888" ,
    "http://purl.obolibrary.org/obo/CHEBI_28017" ,
    "http://purl.obolibrary.org/obo/CHEBI_28073" ,
    "http://purl.obolibrary.org/obo/CHEBI_28112" ,
    "http://purl.obolibrary.org/obo/CHEBI_28659" ,
    "http://purl.obolibrary.org/obo/CHEBI_28685" ,
    "http://purl.obolibrary.org/obo/CHEBI_28694" ,
    "http://purl.obolibrary.org/obo/CHEBI_28966" ,
    "http://purl.obolibrary.org/obo/CHEBI_28984" ,
    "http://purl.obolibrary.org/obo/CHEBI_30778" ,
    "http://purl.obolibrary.org/obo/CHEBI_33233" ,
    "http://purl.obolibrary.org/obo/CHEBI_33284" ,
    "http://purl.obolibrary.org/obo/CHEBI_33292" ,
    "http://purl.obolibrary.org/obo/CHEBI_33815" ,
    "http://purl.obolibrary.org/obo/CHEBI_33853" ,
    "http://purl.obolibrary.org/obo/CHEBI_33937" ,
    "http://purl.obolibrary.org/obo/CHEBI_35255" ,
    "http://purl.obolibrary.org/obo/CHEBI_35381" ,
    "http://purl.obolibrary.org/obo/CHEBI_36005" ,
    "http://purl.obolibrary.org/obo/CHEBI_36080" ,
    "http://purl.obolibrary.org/obo/CHEBI_36233" ,
    "http://purl.obolibrary.org/obo/CHEBI_36928" ,
    "http://purl.obolibrary.org/obo/CHEBI_36934" ,
    "http://purl.obolibrary.org/obo/CHEBI_53276" ,
    "http://purl.obolibrary.org/obo/CHEBI_53725" ,
    "http://purl.obolibrary.org/obo/CHEBI_59163" ,
    "http://purl.obolibrary.org/obo/CHEBI_62967" ,
    "http://purl.obolibrary.org/obo/CHEBI_6457" ,
    "http://purl.obolibrary.org/obo/CHEBI_76413" ,
    "http://purl.obolibrary.org/obo/CHEBI_77853" ,
    "http://purl.obolibrary.org/obo/CHMO_0001097" ,
    "http://purl.obolibrary.org/obo/CHMO_0001473" ,
    "http://purl.obolibrary.org/obo/CIDO_0000900" ,
    "http://purl.obolibrary.org/obo/CL_0000000" ,
    "http://purl.obolibrary.org/obo/CL_0002371" ,
    "http://purl.obolibrary.org/obo/CMO_0002169" ,
    "http://purl.obolibrary.org/obo/CO_715_0000007" ,
    "http://purl.obolibrary.org/obo/CO_715_0000011" ,
    "http://purl.obolibrary.org/obo/ECOCORE_00000022" ,
    "http://purl.obolibrary.org/obo/ECOCORE_00000146" ,
    "http://purl.obolibrary.org/obo/ENVO_00000015" ,
    "http://purl.obolibrary.org/obo/ENVO_00000020" ,
    "http://purl.obolibrary.org/obo/ENVO_00000022" ,
    "http://purl.obolibrary.org/obo/ENVO_00000023" ,
    "http://purl.obolibrary.org/obo/ENVO_00000033" ,
    "http://purl.obolibrary.org/obo/ENVO_00000035" ,
    "http://purl.obolibrary.org/obo/ENVO_00000044" ,
    "http://purl.obolibrary.org/obo/ENVO_00000045" ,
    "http://purl.obolibrary.org/obo/ENVO_00000054" ,
    "http://purl.obolibrary.org/obo/ENVO_00000063" ,
    "http://purl.obolibrary.org/obo/ENVO_00000090" ,
    "http://purl.obolibrary.org/obo/ENVO_00000112" ,
    "http://purl.obolibrary.org/obo/ENVO_00000133" ,
    "http://purl.obolibrary.org/obo/ENVO_00000134" ,
    "http://purl.obolibrary.org/obo/ENVO_00000135" ,
    "http://purl.obolibrary.org/obo/ENVO_00000147" ,
    "http://purl.obolibrary.org/obo/ENVO_00000149" ,
    "http://purl.obolibrary.org/obo/ENVO_00000150" ,
    "http://purl.obolibrary.org/obo/ENVO_00000170" ,
    "http://purl.obolibrary.org/obo/ENVO_00000176" ,
    "http://purl.obolibrary.org/obo/ENVO_00000223" ,
    "http://purl.obolibrary.org/obo/ENVO_00000241" ,
    "http://purl.obolibrary.org/obo/ENVO_00000255" ,
    "http://purl.obolibrary.org/obo/ENVO_00000291" ,
    "http://purl.obolibrary.org/obo/ENVO_00000292" ,
    "http://purl.obolibrary.org/obo/ENVO_00000309" ,
    "http://purl.obolibrary.org/obo/ENVO_00000546" ,
    "http://purl.obolibrary.org/obo/ENVO_00001998" ,
    "http://purl.obolibrary.org/obo/ENVO_00002000" ,
    "http://purl.obolibrary.org/obo/ENVO_00002005" ,
    "http://purl.obolibrary.org/obo/ENVO_00002006" ,
    "http://purl.obolibrary.org/obo/ENVO_00002019" ,
    "http://purl.obolibrary.org/obo/ENVO_00002036" ,
    "http://purl.obolibrary.org/obo/ENVO_00002040" ,
    "http://purl.obolibrary.org/obo/ENVO_00002149" ,
    "http://purl.obolibrary.org/obo/ENVO_00002150" ,
    "http://purl.obolibrary.org/obo/ENVO_00002229" ,
    "http://purl.obolibrary.org/obo/ENVO_00002261" ,
    "http://purl.obolibrary.org/obo/ENVO_00002982" ,
    "http://purl.obolibrary.org/obo/ENVO_00003031" ,
    "http://purl.obolibrary.org/obo/ENVO_00005774" ,
    "http://purl.obolibrary.org/obo/ENVO_00005778" ,
    "http://purl.obolibrary.org/obo/ENVO_00005801" ,
    "http://purl.obolibrary.org/obo/ENVO_00010504" ,
    "http://purl.obolibrary.org/obo/ENVO_01000000" ,
    "http://purl.obolibrary.org/obo/ENVO_01000006" ,
    "http://purl.obolibrary.org/obo/ENVO_01000016" ,
    "http://purl.obolibrary.org/obo/ENVO_01000017" ,
    "http://purl.obolibrary.org/obo/ENVO_01000063" ,
    "http://purl.obolibrary.org/obo/ENVO_01000113" ,
    "http://purl.obolibrary.org/obo/ENVO_01000155" ,
    "http://purl.obolibrary.org/obo/ENVO_01000203" ,
    "http://purl.obolibrary.org/obo/ENVO_01000207" ,
    "http://purl.obolibrary.org/obo/ENVO_01000267" ,
    "http://purl.obolibrary.org/obo/ENVO_01000281" ,
    "http://purl.obolibrary.org/obo/ENVO_01000313" ,
    "http://purl.obolibrary.org/obo/ENVO_01000320" ,
    "http://purl.obolibrary.org/obo/ENVO_01000323" ,
    "http://purl.obolibrary.org/obo/ENVO_01000325" ,
    "http://purl.obolibrary.org/obo/ENVO_01000336" ,
    "http://purl.obolibrary.org/obo/ENVO_01000342" ,
    "http://purl.obolibrary.org/obo/ENVO_01000355" ,
    "http://purl.obolibrary.org/obo/ENVO_01000406" ,
    "http://purl.obolibrary.org/obo/ENVO_01000431" ,
    "http://purl.obolibrary.org/obo/ENVO_01000435" ,
    "http://purl.obolibrary.org/obo/ENVO_01000451" ,
    "http://purl.obolibrary.org/obo/ENVO_01000540" ,
    "http://purl.obolibrary.org/obo/ENVO_01000560" ,
    "http://purl.obolibrary.org/obo/ENVO_01000620" ,
    "http://purl.obolibrary.org/obo/ENVO_01000621" ,
    "http://purl.obolibrary.org/obo/ENVO_01000628" ,
    "http://purl.obolibrary.org/obo/ENVO_01000629" ,
    "http://purl.obolibrary.org/obo/ENVO_01000646" ,
    "http://purl.obolibrary.org/obo/ENVO_01000677" ,
    "http://purl.obolibrary.org/obo/ENVO_01000691" ,
    "http://purl.obolibrary.org/obo/ENVO_01000705" ,
    "http://purl.obolibrary.org/obo/ENVO_01000706" ,
    "http://purl.obolibrary.org/obo/ENVO_01000710" ,
    "http://purl.obolibrary.org/obo/ENVO_01000739" ,
    "http://purl.obolibrary.org/obo/ENVO_01000770" ,
    "http://purl.obolibrary.org/obo/ENVO_01000772" ,
    "http://purl.obolibrary.org/obo/ENVO_01000786" ,
    "http://purl.obolibrary.org/obo/ENVO_01000787" ,
    "http://purl.obolibrary.org/obo/ENVO_01000789" ,
    "http://purl.obolibrary.org/obo/ENVO_01000791" ,
    "http://purl.obolibrary.org/obo/ENVO_01000793" ,
    "http://purl.obolibrary.org/obo/ENVO_01000817" ,
    "http://purl.obolibrary.org/obo/ENVO_01000819" ,
    "http://purl.obolibrary.org/obo/ENVO_01000820" ,
    "http://purl.obolibrary.org/obo/ENVO_01000830" ,
    "http://purl.obolibrary.org/obo/ENVO_01000839" ,
    "http://purl.obolibrary.org/obo/ENVO_01000876" ,
    "http://purl.obolibrary.org/obo/ENVO_01000903" ,
    "http://purl.obolibrary.org/obo/ENVO_01001023" ,
    "http://purl.obolibrary.org/obo/ENVO_01001026" ,
    "http://purl.obolibrary.org/obo/ENVO_01001078" ,
    "http://purl.obolibrary.org/obo/ENVO_01001082" ,
    "http://purl.obolibrary.org/obo/ENVO_01001103" ,
    "http://purl.obolibrary.org/obo/ENVO_01001110" ,
    "http://purl.obolibrary.org/obo/ENVO_01001125" ,
    "http://purl.obolibrary.org/obo/ENVO_01001177" ,
    "http://purl.obolibrary.org/obo/ENVO_01001239" ,
    "http://purl.obolibrary.org/obo/ENVO_01001242" ,
    "http://purl.obolibrary.org/obo/ENVO_01001243" ,
    "http://purl.obolibrary.org/obo/ENVO_01001248" ,
    "http://purl.obolibrary.org/obo/ENVO_01001330" ,
    "http://purl.obolibrary.org/obo/ENVO_01001346" ,
    "http://purl.obolibrary.org/obo/ENVO_01001357" ,
    "http://purl.obolibrary.org/obo/ENVO_01001864" ,
    "http://purl.obolibrary.org/obo/ENVO_02000090" ,
    "http://purl.obolibrary.org/obo/ENVO_02500001" ,
    "http://purl.obolibrary.org/obo/ENVO_02500003" ,
    "http://purl.obolibrary.org/obo/ENVO_02500004" ,
    "http://purl.obolibrary.org/obo/ENVO_02500005" ,
    "http://purl.obolibrary.org/obo/ENVO_02500030" ,
    "http://purl.obolibrary.org/obo/ENVO_02500032" ,
    "http://purl.obolibrary.org/obo/ENVO_02500033" ,
    "http://purl.obolibrary.org/obo/ENVO_02500034" ,
    "http://purl.obolibrary.org/obo/ENVO_02500035" ,
    "http://purl.obolibrary.org/obo/ENVO_02500036" ,
    "http://purl.obolibrary.org/obo/ENVO_02500037" ,
    "http://purl.obolibrary.org/obo/ENVO_02500041" ,
    "http://purl.obolibrary.org/obo/ENVO_03000033" ,
    "http://purl.obolibrary.org/obo/ENVO_03501347" ,
    "http://purl.obolibrary.org/obo/ENVO_09200012" ,
    "http://purl.obolibrary.org/obo/ENVO_1000745" ,
    "http://purl.obolibrary.org/obo/ENVO_2000004" ,
    "http://purl.obolibrary.org/obo/ENVO_2000016" ,
    "http://purl.obolibrary.org/obo/ENVO_21001214" ,
    "http://purl.obolibrary.org/obo/ERO_0000441" ,
    "http://purl.obolibrary.org/obo/ERO_0000583" ,
    "http://purl.obolibrary.org/obo/ERO_0000585" ,
    "http://purl.obolibrary.org/obo/ExO_0000012" ,
    "http://purl.obolibrary.org/obo/ExO_0000054" ,
    "http://purl.obolibrary.org/obo/ExO_0000113" ,
    "http://purl.obolibrary.org/obo/FBcv_0000161" ,
    "http://purl.obolibrary.org/obo/FBcv_0003167" ,
    "http://purl.obolibrary.org/obo/GSSO_005261" ,
    "http://purl.obolibrary.org/obo/HP_0012531" ,
    "http://purl.obolibrary.org/obo/IDOMAL_0002362" ,
    "http://purl.obolibrary.org/obo/ID_0000022" ,
    "http://purl.obolibrary.org/obo/ID_0000053" ,
    "http://purl.obolibrary.org/obo/NCBITaxon_40674" ,
    "http://purl.obolibrary.org/obo/NCBITaxon_58023" ,
    "http://purl.obolibrary.org/obo/NCBITaxon_7088" ,
    "http://purl.obolibrary.org/obo/NCBITaxon_9989" ,
    "http://purl.obolibrary.org/obo/OBI_0000272" ,
    "http://purl.obolibrary.org/obo/OBI_0000789" ,
    "http://purl.obolibrary.org/obo/OBI_0000818" ,
    "http://purl.obolibrary.org/obo/OBI_0100026" ,
    "http://purl.obolibrary.org/obo/OBI_0302893" ,
    "http://purl.obolibrary.org/obo/OBI_0666666" ,
    "http://purl.obolibrary.org/obo/OGSF_0000000" ,
    "http://purl.obolibrary.org/obo/OMIT_0002433" ,
    "http://purl.obolibrary.org/obo/OMIT_0027643" ,
    "http://purl.obolibrary.org/obo/RBO_00000017" ,
    "http://purl.obolibrary.org/obo/REX_0000001" ,
    "http://purl.obolibrary.org/obo/SOY_0001385" ,
    "http://purl.obolibrary.org/obo/SOY_0001419" ,
    "http://purl.obolibrary.org/obo/SOY_0001637" ,
    "http://purl.obolibrary.org/obo/SOY_0001993" ,
    "http://purl.obolibrary.org/obo/TRAK_0001442" ,
    "http://purl.obolibrary.org/obo/UBERON_0000178" ,
    "http://purl.obolibrary.org/obo/VT_0001256" ,
]

for concept in concepts:
    ont = concept.split("/")[-1].split("_")[0]
    url = f"https://ontobee.org/ontology/rdf/{ont}?iri={concept}"

    try:
        g = Graph().parse(url, format="xml")
        label = g.value(subject=URIRef(concept), predicate=RDFS.label)
        print(f"<{concept}> schema:name \"{label}\" .")
    except:
        pass

