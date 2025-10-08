#
# PySNMP MIB module CISCO-MGX82XX-CARD-FEATURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-MGX82XX-CARD-FEATURE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-MGX82XX-CARD-FEATURE-MIB", ciscoMgx82xxCardFeatureMIB=ciscoMgx82xxCardFeatureMIB, ascFeatures=ascFeatures, pxmFeatures=pxmFeatures, coreCardCommands=coreCardCommands, vsiControllersAllowed=vsiControllersAllowed, apsCardAttributes=apsCardAttributes, redundancyAllowed=redundancyAllowed, switchCoreCard=switchCoreCard, trkCACEnable=trkCACEnable, pxmCardCacMode=pxmCardCacMode, cmCardFeatureMIBCompliances=cmCardFeatureMIBCompliances, PYSNMP_MODULE_ID=ciscoMgx82xxCardFeatureMIB, cmCardFeatureCompliance=cmCardFeatureCompliance, cmPxmCardFeatureGroup=cmPxmCardFeatureGroup, cmCardFeatureMIBConformance=cmCardFeatureMIBConformance, cmCoreCardFeatureGroup=cmCoreCardFeatureGroup, cmAscCardFeatureGroup=cmAscCardFeatureGroup, cmCardFeatureMIBGroups=cmCardFeatureMIBGroups)
