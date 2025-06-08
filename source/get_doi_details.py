from rdflib import Graph, URIRef, Literal, DCTERMS, SDO


dois = [
    # "https://doi.org/10.1002/ajb2.1538" ,
    # "https://doi.org/10.1002/ece3.7544" ,
    # "https://doi.org/10.1007/978-1-4684-7747-4_8" ,
    # "https://doi.org/10.1007/978-3-662-04931-0" ,
    # "https://doi.org/10.1007/978-94-007-1242-3_13" ,
    # "https://doi.org/10.1007/BF00121013" ,
    # "https://doi.org/10.1007/BF00195081" ,
    # "https://doi.org/10.1007/BF00317209" ,
    # "https://doi.org/10.1007/BF00386231" ,
    # "https://doi.org/10.1007/BF02803249" ,
    # "https://doi.org/10.1007/BF02858770" ,
    # "https://doi.org/10.1007/s00442-006-0523-z" ,
    # "https://doi.org/10.1007/s004420000624" ,
    # "https://doi.org/10.1007/s004420050337" ,
    # "https://doi.org/10.1007/s11284-010-0712-4" ,
    # "https://doi.org/10.1016/B978-0-12-380868-4.00004-1" ,
    # "https://doi.org/10.1016/S0034-4257(02)00010-X" ,
    # "https://doi.org/10.1016/S0169-5347(03)00061-2" ,
    # "https://doi.org/10.1016/j.ecoinf.2021.101232" ,
    # "https://doi.org/10.1016/j.plantsci.2012.05.009" ,
    # "https://doi.org/10.1016/j.ppees.2007.01.001" ,
    # "https://doi.org/10.1016/j.ppees.2019.125497" ,
    # "https://doi.org/10.1016/j.scitotenv.2015.04.002" ,
    # "https://doi.org/10.1016/j.tplants.2010.10.003" ,
    # "https://doi.org/10.1016/j.tree.2022.11.002" ,
    # "https://doi.org/10.1017/CBO9780511845727" ,
    # "https://doi.org/10.1017/S0960258510000267" ,

    # "https://doi.org/10.1023/A1009875226637" ,  # broken

    # "https://doi.org/10.1038/282424a0" ,
    # "https://doi.org/10.1038/nature02403" ,
    # "https://doi.org/10.1038/s41467-022-32545-0" ,
    # "https://doi.org/10.1038/s41597-019-0189-0" ,
    # "https://doi.org/10.1038/sdata.2018.135" ,
    # "https://doi.org/10.1046/j.1365-2435.2001.00522.x" ,
    # "https://doi.org/10.1046/j.1365-3040.2002.00891.x" ,
    # "https://doi.org/10.1046/j.1442-9993.2001.01154.x" ,
    # "https://doi.org/10.1046/j.1469-8137.2003.00765.x" ,
    # "https://doi.org/10.1071/9780643109865" ,
    # "https://doi.org/10.1071/BT02124" ,
    # "https://doi.org/10.1071/BT06106" ,
    # "https://doi.org/10.1071/BT11284" ,
    # "https://doi.org/10.1071/BT12225" ,
    # "https://doi.org/10.1071/BT20048" ,
    # "https://doi.org/10.1071/BT9900255" ,
    # "https://doi.org/10.1071/FP05298" ,
    # "https://doi.org/10.1079/SSR2003150" ,
    # "https://doi.org/10.1079/SSR2005209" ,
    # "https://doi.org/10.1080/014311697216810" ,
    # "https://doi.org/10.1080/014311697217387" ,
    # "https://doi.org/10.1080/07352689.2017.1364209" ,
    # "https://doi.org/10.1080/07352689.2020.1768465" ,
    # "https://doi.org/10.1086/319579" ,
    # "https://doi.org/10.1086/670400" ,
    # "https://doi.org/10.1093/jexbot/51.345.659" ,
    # "https://doi.org/10.1093/jxb/erp117" ,
    # "https://doi.org/10.1093/pcp/pcv155" ,
    # "https://doi.org/10.1094/PHI-I-2004-0330-01" ,
    # "https://doi.org/10.1111/1365-2745.12035" ,
    # "https://doi.org/10.1111/geb.12346" ,
    # "https://doi.org/10.1111/geb.13065" ,
    # "https://doi.org/10.1111/j.1365-2435.2010.01826.x" ,
    # "https://doi.org/10.1111/j.1365-2699.2012.02773.x" ,
    # "https://doi.org/10.1111/j.1365-2745.2007.01302.x" ,
    # "https://doi.org/10.1111/j.1469-8137.1991.tb00035.x" ,
    # "https://doi.org/10.1111/j.1469-8137.2010.03439.x" ,
    # "https://doi.org/10.1111/j.1654-1103.2003.tb02160.x" ,
    # "https://doi.org/10.1111/j.1654-1103.2012.01434.x" ,
    # "https://doi.org/10.1111/jbi.14375" ,
    # "https://doi.org/10.1111/jipb.12534" ,
    # "https://doi.org/10.1111/jvs.12375" ,
    # "https://doi.org/10.1111/nph.12001" ,
    # "https://doi.org/10.1111/nph.12253" ,
    # "https://doi.org/10.1111/nph.14982" ,
    # "https://doi.org/10.1111/nph.15480" ,
    # "https://doi.org/10.1111/nph.15502" ,
    # "https://doi.org/10.1111/nph.16793" ,
    # "https://doi.org/10.1111/oik.03886" ,
    # "https://doi.org/10.1139/x87-131" ,
    # "https://doi.org/10.1201/b10812" ,

    # "https://doi.org/10.13140/2.1.2761.5367" ,  # error

    # "https://doi.org/10.1890/0012-9658%281997%29078%5B2542%3ALPOWSI%5D2.0.CO%3B2" ,

    # "https://doi.org/10.1890/12-0621.1" ,
    # "https://doi.org/10.2307/1217034" ,
    # "https://doi.org/10.2307/1932458" ,
    # "https://doi.org/10.2307/1938268" ,

    # "https://doi.org/10.2307/2441319" ,  # None

    "https://doi.org/10.2307/3236276" ,
    "https://doi.org/10.3389/fpls.2013.00056" ,
    "https://doi.org/10.3732/ajb.0900178" ,
    "https://doi.org/10.4236/ajps.2013.45A005" ,

    "https://doi.org/10.48373/0PWD-C575" ,
]

g = Graph()

f = open("dois.2.ttl", "w")

for doi in dois:
    iri = URIRef(doi.replace("https://doi.org/", "http://dx.doi.org/"))
    g2 = Graph().parse(doi)
    title = g2.value(subject=iri, predicate=DCTERMS.title)
    print(doi)
    print(title)
    g.add((
        iri,
        SDO.name,
        title
    ))

    f.write(g.serialize(format="longturtle"))