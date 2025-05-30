from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class ANSIS(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-05-30 11:52:39.678148
    """

    _NS = Namespace("https://anzsoil.org/def/au/domain/")

    CoarseFragments: URIRef  # ![Coarse fragments - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/CoarseFragments.png)
    Cracks: URIRef  # 
    Cutans: URIRef  # ![Cutans - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Cutans.png)
    Erosion: URIRef  # ![Erosion - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Erosion.png)
    HorizonDesignation: URIRef  # 
    Inundation: URIRef  # ![Inundation - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Inundation.png)
    LandCover: URIRef  # 
    LandManagement: URIRef  # 
    LandSurface: URIRef  # surface landscape features of a site  ![Landsurface - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/LandSurface.png)
    LandUse: URIRef  # 
    Landform: URIRef  # landscape features within which the site is located  ![Landform - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Landform.png)
    LandformElement: URIRef  # Landform element (~40m)
    LandformPattern: URIRef  # Landform pattern (>600m)
    LandscapeEntity: URIRef  # 
    LandsurveySite: URIRef  # A Site established to make observations of landscape entities  ![Site - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Site.png)
    Literal: URIRef  # Generic container class for objects with a 'literal' value (i.e. text-string, number, etc) 
    Microrelief: URIRef  # ![Microrelief - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Microrelief.png)
    Mottles: URIRef  # Mottles and other colour patterns  ![Mottles - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Mottles.png)
    Outcrop: URIRef  # ![Outcrop - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Outcrop.png)
    Pans: URIRef  # ![Pans - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Pans.png)
    Pores: URIRef  # ![Pores - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Pores.png)
    Roots: URIRef  # ![Roots - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Roots.png)
    Segregations: URIRef  # ![Segregations - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Segregations.png)
    SiteType: URIRef  # Type of land survey site e.g. monitoring, opportunistic, farm, pedology
    SiteVisit: URIRef  # A visit to a designated site, for the purpose of taking samples, making observations, and other activities  ![Sitevisit - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/SiteVisit.png)
    SoilBody: URIRef  # part of the soil cover that is delineated at a scale useful for an application, and is homogeneous with regard to properties and/or spatial patterns.  ![Soilbody - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/SoilBody.png) 
    SoilClassification: URIRef  # 
    SoilColour: URIRef  # 
    SoilHorizon: URIRef  # soil layer which is compositionally and/or structurally homogeneous, delineated by pedological boundaries  ![Soillayer - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Soillayer.png)
    SoilHorizonR: URIRef  # 
    SoilLayer: URIRef  # region within a soil body usually observed as a specified depth interval within a profile  ![Soillayer - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Soillayer.png)
    SoilOrder: URIRef  # 
    SoilPlasticity: URIRef  # 
    SoilProfile: URIRef  # A soil profile is a vertical section of a soil from the soil surface through all its horizons to parent material, other consolidated substrate material or selected depth in unconsolidated material.  ![Soilprofile - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/SoilProfile.png)
    SoilSample: URIRef  # Sample of soil or soil entity  Sample is a key class in the context of observations. The sample is an intermediate object, which is intended to be representative of the entity that we wish to characterize. The relationship of the sample to the ultimate entity-of-interest is recorded through the following properties: <br/> - `sosa:isSampleOf` to indicate the entity that this sample represents <br/> - `ansis:component` (if necessary) to indicate which component of the entity the observation related to, such as coarse-fragments or mottles <br/> - `ansis:relatedProfile` to indicate the 'profile' where it is taken (this may be a formal, complete profile, or an informal profile such as a shallow auger or shovel location) <br/> - `ansis:depth-lower` + `ansis:depth-upper` (if necessary) to indicate the precise depth range within the profile where the sample was taken  ![Sample - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Sample.png)
    SoilSite: URIRef  # A site where samples, observations, and treatments of soil are carried out.  ![Site - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Site.png)
    SoilStrength: URIRef  # ![Soilstrength - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/SoilStrength.png)
    SoilStructure: URIRef  # Soil structure or pedality  ![Soilstructure - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/SoilStructure.png)
    SoilSuborder: URIRef  # 
    SoilSurface: URIRef  # the surface of the soil body  ![Soilsurface - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/SoilSurface.png)
    StreamChannel: URIRef  # Stream channel details  ![Streamchannel - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/StreamChannel.png)
    Substrate: URIRef  # observed or inferred materials and masses of earth or rock that do not show pedological development. They are not soils, but typically underlie them. The substrate includes the R horizon and that part of the C horizon that shows no pedological development, but excludes the solum, buried soil horizons (including D horizons), and pans. The substrate beneath a soil profile may or may not be the parent material of the soil.  ![Substrate - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Substrate.png)
    Treatment: URIRef  # Intervention or treatment  ![Actuation - class diagram](https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/fig/Actuation.png)
    abundance: URIRef  # abundance of items
    agent: URIRef  # agent of geomorphological or biotic activity
    aggradation: URIRef  # aggradation presence
    alteration: URIRef  # type of alteration
    analyte: URIRef  # chemical species measured
    aspect: URIRef  # direction or azimuth that a terrain surface faces
    carbon: URIRef  # 
    cementation: URIRef  # degree of cementation
    chemistry: URIRef  # 
    classification: URIRef  # classification of the soil body or profile
    colour: URIRef  # 
    component: URIRef  # type of component element
    confidence: URIRef  # confidence in assessment
    continuity: URIRef  # continuity of linear or planar elements
    contrast: URIRef  # degree of colour contrast
    degree: URIRef  # degree or severity or intensity of phenomenon
    density: URIRef  # mass per unit volume of a substance
    depth: URIRef  # depth from local surface of entity
    designation: URIRef  # designation of soil horizon with the sequence composing the Profile or Soil Body soil horizon designation
    development: URIRef  # degree of development of element
    diameter: URIRef  # thickness or width of round object
    directionality: URIRef  # network directionality
    distance: URIRef  # spatial separation of objects
    distinctness: URIRef  # distinctness of boundary
    distribution: URIRef  # spatial arrangement of items
    disturbance: URIRef  # disturbance of site
    drainage: URIRef  # 
    duration: URIRef  # temporal extent of event or phenomenon
    elevation: URIRef  # elevation of element above a datum (usually MSL)
    fabric: URIRef  # fabric of soil element
    frequency: URIRef  # temporal frequency of event or phenomenon
    genesis: URIRef  # formation process for material
    geomorphologyMode: URIRef  # mode of geomorphological activity
    geomorphologyStatus: URIRef  # status of geomorphological activity
    grade: URIRef  # grade or degree of development of structure
    hasCoarseFragments: URIRef  # link to description of coarse fragments
    hasCracks: URIRef  # link to description of cracks
    hasCutans: URIRef  # link to description of cutans
    hasErosion: URIRef  # link to description of erosion
    hasInundation: URIRef  # link to description of inundation
    hasLandCover: URIRef  # land cover around this entity
    hasLandManagement: URIRef  # land management around this entity
    hasLandSurface: URIRef  # land surface at this entity
    hasLandUse: URIRef  # land use around this entity
    hasLandform: URIRef  # landform around this entity
    hasLandformElement: URIRef  # landform element around this entity (<20m)
    hasLandformPattern: URIRef  # landform pattern around this entity (>600m)
    hasMicrorelief: URIRef  # link to description of microrelief at the site
    hasMottles: URIRef  # link to description of mottles and other colour patterns
    hasOutcrop: URIRef  # link to description of rock outcrop at this entity
    hasPans: URIRef  # link to description of pans
    hasPores: URIRef  # 
    hasRoots: URIRef  # link to description of roots
    hasSegregations: URIRef  # 
    hasStreamChannel: URIRef  # link to description of stream channel occurrence
    hasSubstrate: URIRef  # link to description of substrate substrate at this entity
    height: URIRef  # vertical extent of element
    integration: URIRef  # integration of stream channel network
    length: URIRef  # linear extent - larger dimension
    lithology: URIRef  # lithological type of material
    mapSheet: URIRef  # map-sheet on which this location is found
    material: URIRef  # material or composition of entity or element
    pH: URIRef  # alkalinity of material
    pattern: URIRef  # spatial pattern of channels or other linear element
    permeability: URIRef  # rate of flow of liquid through the material
    physical: URIRef  # 
    plasticity: URIRef  # capability of being formed or molded
    porosity: URIRef  # proportion of void space in material
    proportions: URIRef  # relative proportions of the components
    purpose: URIRef  # purpose of or reason for activity
    relatedActivity: URIRef  # link to an activity related to this context
    relatedHorizon: URIRef  # related soil horizon within a soil body or sample, or associated with a contact
    relatedLandsurveySite: URIRef  # link to a land survey site related to this context
    relatedLayer: URIRef  # related soil layer within a soil body or profile
    relatedProfile: URIRef  # link to a soil profile related to this context
    relatedProject: URIRef  # link to project that supported this activity
    relatedSample: URIRef  # link to a sample related to this context
    relatedSite: URIRef  # link to a soil site related to this context
    relatedSoilBody: URIRef  # link to a soil body related to this context
    relatedSoilSurface: URIRef  # soil surface of this entity
    relief: URIRef  # amount of vertical variation of the landform
    runoff: URIRef  # degree of surface water runoff
    shape: URIRef  # geometry of entity or entity boundary
    size: URIRef  # geometric scale and extent of element
    slope: URIRef  # divergence of surface from horizontal
    spacing: URIRef  # lateral separation of elements
    state: URIRef  # erosion status
    stickiness: URIRef  # adhesiveness or viscosity
    strength: URIRef  # strength of material
    structure: URIRef  # internal arrangement of elements of the material or entity
    texture: URIRef  # material texture, in terms of particle size distribution and component materials
    type: URIRef  # type of ansis soil entity
    underlyingMaterial: URIRef  # 
    value: URIRef  # literal value
    velocity: URIRef  # velocity of entity
    visitor: URIRef  # site visitor, for the purpose of sampling or observation
    waterRepellence: URIRef  # water repellence of material
    width: URIRef  # linear extent - smaller dimension
