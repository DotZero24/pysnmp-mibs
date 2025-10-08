#
# PySNMP MIB module PDN-UPLINK-TAGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-UPLINK-TAGGING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnUplinkTagging = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37))
pdnUplinkTagging.setRevisions(('2003-03-12 00:00', '2002-05-15 00:00',))
if mibBuilder.loadTexts: pdnUplinkTagging.setLastUpdated('200303120000Z')
if mibBuilder.loadTexts: pdnUplinkTagging.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnUplinkTaggingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 1))
pdnUplinkTaggingObjectsR2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3))
pdnUltIndex = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnUltIndex.setStatus('current')
pdnGenUltBaseVlanTag = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 2), VlanId().clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnGenUltBaseVlanTag.setStatus('current')
pdn48UltBaseVlanTag = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ultBase16", 1), ("ultBase512", 2), ("ultBase1024", 3), ("ultBase1536", 4), ("ultBase2048", 5), ("ultBase2560", 6), ("ultBase3072", 7), ("ultBase3584", 8))).clone('ultBase16')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdn48UltBaseVlanTag.setStatus('current')
pdn24UltBaseVlanTag = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("ultBase16", 1), ("ultBase256", 2), ("ultBase512", 3), ("ultBase768", 4), ("ultBase1024", 5), ("ultBase1280", 6), ("ultBase1536", 7), ("ultBase1792", 8), ("ultBase2048", 9), ("ultBase2304", 10), ("ultBase2560", 11), ("ultBase2816", 12), ("ultBase3072", 13), ("ultBase3328", 14), ("ultBase3584", 15), ("ultBase3840", 16))).clone('ultBase16')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdn24UltBaseVlanTag.setStatus('current')
ultBaseVlanTag = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ultBase16", 1), ("ultBase512", 2), ("ultBase1024", 3), ("ultBase1536", 4), ("ultBase2048", 5), ("ultBase2560", 6), ("ultBase3072", 7), ("ultBase3584", 8))).clone('ultBase16')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ultBaseVlanTag.setStatus('deprecated')
ultIndex = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ultIndex.setStatus('deprecated')
pdnUplinkTaggingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2))
pdnUplinkTaggingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 1))
pdnUplinkTaggingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 2))
pdnUplinkTaggingDeprecatedGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 3))
pdn48PortUpLinkTaggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 1, 1)).setObjects(("PDN-UPLINK-TAGGING-MIB", "pdnUltIndex"), ("PDN-UPLINK-TAGGING-MIB", "pdnGenUltBaseVlanTag"), ("PDN-UPLINK-TAGGING-MIB", "pdn48UltBaseVlanTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdn48PortUpLinkTaggingGroup = pdn48PortUpLinkTaggingGroup.setStatus('current')
pdn24PortUpLinkTaggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 1, 2)).setObjects(("PDN-UPLINK-TAGGING-MIB", "pdnUltIndex"), ("PDN-UPLINK-TAGGING-MIB", "pdnGenUltBaseVlanTag"), ("PDN-UPLINK-TAGGING-MIB", "pdn24UltBaseVlanTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdn24PortUpLinkTaggingGroup = pdn24PortUpLinkTaggingGroup.setStatus('current')
upLinkTaggingDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 37, 2, 3, 1)).setObjects(("PDN-UPLINK-TAGGING-MIB", "ultBaseVlanTag"), ("PDN-UPLINK-TAGGING-MIB", "ultIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upLinkTaggingDeprecatedGroup = upLinkTaggingDeprecatedGroup.setStatus('deprecated')
mibBuilder.exportSymbols("PDN-UPLINK-TAGGING-MIB", pdnUplinkTagging=pdnUplinkTagging, pdnUltIndex=pdnUltIndex, pdn24PortUpLinkTaggingGroup=pdn24PortUpLinkTaggingGroup, PYSNMP_MODULE_ID=pdnUplinkTagging, pdnUplinkTaggingObjectsR2=pdnUplinkTaggingObjectsR2, pdnUplinkTaggingCompliances=pdnUplinkTaggingCompliances, pdnUplinkTaggingObjects=pdnUplinkTaggingObjects, ultBaseVlanTag=ultBaseVlanTag, pdn48PortUpLinkTaggingGroup=pdn48PortUpLinkTaggingGroup, ultIndex=ultIndex, pdn24UltBaseVlanTag=pdn24UltBaseVlanTag, pdnGenUltBaseVlanTag=pdnGenUltBaseVlanTag, pdnUplinkTaggingConformance=pdnUplinkTaggingConformance, pdnUplinkTaggingGroups=pdnUplinkTaggingGroups, pdnUplinkTaggingDeprecatedGroup=pdnUplinkTaggingDeprecatedGroup, pdn48UltBaseVlanTag=pdn48UltBaseVlanTag, upLinkTaggingDeprecatedGroup=upLinkTaggingDeprecatedGroup)
