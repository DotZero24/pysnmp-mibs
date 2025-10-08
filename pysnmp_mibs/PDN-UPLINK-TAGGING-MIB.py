#
# PySNMP MIB module PDN-UPLINK-TAGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-UPLINK-TAGGING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PDN-UPLINK-TAGGING-MIB", pdn48UltBaseVlanTag=pdn48UltBaseVlanTag, pdnUplinkTaggingObjectsR2=pdnUplinkTaggingObjectsR2, pdnUplinkTaggingCompliances=pdnUplinkTaggingCompliances, ultIndex=ultIndex, PYSNMP_MODULE_ID=pdnUplinkTagging, pdn24UltBaseVlanTag=pdn24UltBaseVlanTag, pdn48PortUpLinkTaggingGroup=pdn48PortUpLinkTaggingGroup, pdnUplinkTagging=pdnUplinkTagging, pdnUplinkTaggingGroups=pdnUplinkTaggingGroups, pdnUplinkTaggingDeprecatedGroup=pdnUplinkTaggingDeprecatedGroup, pdnGenUltBaseVlanTag=pdnGenUltBaseVlanTag, pdn24PortUpLinkTaggingGroup=pdn24PortUpLinkTaggingGroup, pdnUplinkTaggingObjects=pdnUplinkTaggingObjects, pdnUplinkTaggingConformance=pdnUplinkTaggingConformance, upLinkTaggingDeprecatedGroup=upLinkTaggingDeprecatedGroup, ultBaseVlanTag=ultBaseVlanTag, pdnUltIndex=pdnUltIndex)
