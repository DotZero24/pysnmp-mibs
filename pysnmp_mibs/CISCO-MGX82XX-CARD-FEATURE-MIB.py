#
# PySNMP MIB module CISCO-MGX82XX-CARD-FEATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-MGX82XX-CARD-FEATURE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:29:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgx82xxCardFeatureMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 74))
ciscoMgx82xxCardFeatureMIB.setRevisions(('2003-05-05 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setLastUpdated('200305050000Z')
if mibBuilder.loadTexts: ciscoMgx82xxCardFeatureMIB.setOrganization('Cisco Systems, Inc.')
ascFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 5))
pxmFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 15))
coreCardCommands = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 20))
vsiControllersAllowed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsiControllersAllowed.setStatus('current')
apsCardAttributes = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsCardAttributes.setStatus('current')
trkCACEnable = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkCACEnable.setStatus('current')
pxmCardCacMode = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 15, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pcrBasedCac", 1), ("scrBasedCac", 2))).clone('pcrBasedCac')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pxmCardCacMode.setStatus('current')
redundancyAllowed = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redNotAllowed", 1), ("redAllowed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: redundancyAllowed.setStatus('current')
switchCoreCard = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 20, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noAction", 1), ("doswitchcc", 2), ("instswitchcc", 3), ("fallbackswitchcc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: switchCoreCard.setStatus('current')
cmCardFeatureMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2))
cmCardFeatureMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1))
cmCardFeatureMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2))
cmCardFeatureCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 2, 1)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmPxmCardFeatureGroup"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmAscCardFeatureGroup"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "cmCoreCardFeatureGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmCardFeatureCompliance = cmCardFeatureCompliance.setStatus('current')
cmPxmCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 1)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "vsiControllersAllowed"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "apsCardAttributes"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "trkCACEnable"), ("CISCO-MGX82XX-CARD-FEATURE-MIB", "pxmCardCacMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPxmCardFeatureGroup = cmPxmCardFeatureGroup.setStatus('current')
cmAscCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 2)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "redundancyAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAscCardFeatureGroup = cmAscCardFeatureGroup.setStatus('current')
cmCoreCardFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 74, 2, 1, 3)).setObjects(("CISCO-MGX82XX-CARD-FEATURE-MIB", "switchCoreCard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmCoreCardFeatureGroup = cmCoreCardFeatureGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-CARD-FEATURE-MIB", PYSNMP_MODULE_ID=ciscoMgx82xxCardFeatureMIB, switchCoreCard=switchCoreCard, trkCACEnable=trkCACEnable, cmCardFeatureMIBGroups=cmCardFeatureMIBGroups, vsiControllersAllowed=vsiControllersAllowed, cmCardFeatureMIBCompliances=cmCardFeatureMIBCompliances, ascFeatures=ascFeatures, cmCardFeatureCompliance=cmCardFeatureCompliance, cmAscCardFeatureGroup=cmAscCardFeatureGroup, coreCardCommands=coreCardCommands, pxmFeatures=pxmFeatures, ciscoMgx82xxCardFeatureMIB=ciscoMgx82xxCardFeatureMIB, pxmCardCacMode=pxmCardCacMode, cmCardFeatureMIBConformance=cmCardFeatureMIBConformance, apsCardAttributes=apsCardAttributes, redundancyAllowed=redundancyAllowed, cmPxmCardFeatureGroup=cmPxmCardFeatureGroup, cmCoreCardFeatureGroup=cmCoreCardFeatureGroup)
