#
# PySNMP MIB module HP-ICF-PRIVATEVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-PRIVATEVLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
VlanId, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "dot1qVlanStaticEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfPrivateVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114))
hpicfPrivateVlan.setRevisions(('2015-04-22 00:00',))
if mibBuilder.loadTexts: hpicfPrivateVlan.setLastUpdated('201504220000Z')
if mibBuilder.loadTexts: hpicfPrivateVlan.setOrganization('HP Networking')
class PrivateVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notAPrivateVLAN", 1), ("primary", 2), ("isolated", 3), ("community", 4))

hpicfPrivateVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1))
hpicfPrivateVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1))
hpicfPrivateVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfPrivateVlanTable.setStatus('current')
hpicfPrivateVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanEntry"))
hpicfPrivateVlanEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfPrivateVlanEntry.setStatus('current')
hpicfPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 1, 1, 1), PrivateVlanType().clone('notAPrivateVLAN')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPrivateVlanType.setStatus('current')
hpicfPrivateVlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfPrivateVlanMappingTable.setStatus('current')
hpicfPrivateVlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1), ).setIndexNames((0, "HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanPrimary"))
if mibBuilder.loadTexts: hpicfPrivateVlanMappingEntry.setStatus('current')
hpicfPrivateVlanPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: hpicfPrivateVlanPrimary.setStatus('current')
hpicfPrivateVlanIsolated = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanIsolated.setStatus('current')
hpicfPrivateVlanCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 3), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanCommunity.setStatus('current')
hpicfPrivateVlanMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfPrivateVlanMappingRowStatus.setStatus('current')
hpicfPrivateVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2))
hpicfPrivateVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1))
hpicfPrivateVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2))
hpicfPVlanTableCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 1)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanTableGroup"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanTableCompliance = hpicfPVlanTableCompliance.setStatus('current')
hpicfPVlanMappingTblCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 1, 2)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPVlanMappingTableGroup"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPVlanMappingTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanMappingTblCompliance = hpicfPVlanMappingTblCompliance.setStatus('current')
hpicfPrivateVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 1)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPrivateVlanTableGroup = hpicfPrivateVlanTableGroup.setStatus('current')
hpicfPVlanMappingTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114, 2, 2, 2)).setObjects(("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanIsolated"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanCommunity"), ("HP-ICF-PRIVATEVLAN-MIB", "hpicfPrivateVlanMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPVlanMappingTableGroup = hpicfPVlanMappingTableGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-PRIVATEVLAN-MIB", hpicfPrivateVlanObjects=hpicfPrivateVlanObjects, hpicfPrivateVlanCompliances=hpicfPrivateVlanCompliances, hpicfPVlanMappingTblCompliance=hpicfPVlanMappingTblCompliance, hpicfPrivateVlanMappingEntry=hpicfPrivateVlanMappingEntry, hpicfPrivateVlanTableGroup=hpicfPrivateVlanTableGroup, hpicfPrivateVlanTable=hpicfPrivateVlanTable, hpicfPrivateVlanType=hpicfPrivateVlanType, hpicfPrivateVlanPrimary=hpicfPrivateVlanPrimary, hpicfPVlanTableCompliance=hpicfPVlanTableCompliance, hpicfPrivateVlanMappingTable=hpicfPrivateVlanMappingTable, hpicfPrivateVlan=hpicfPrivateVlan, hpicfPrivateVlanEntry=hpicfPrivateVlanEntry, hpicfPrivateVlanIsolated=hpicfPrivateVlanIsolated, hpicfPrivateVlanCommunity=hpicfPrivateVlanCommunity, hpicfPrivateVlanConfig=hpicfPrivateVlanConfig, PrivateVlanType=PrivateVlanType, hpicfPVlanMappingTableGroup=hpicfPVlanMappingTableGroup, hpicfPrivateVlanGroup=hpicfPrivateVlanGroup, hpicfPrivateVlanMappingRowStatus=hpicfPrivateVlanMappingRowStatus, hpicfPrivateVlanConformance=hpicfPrivateVlanConformance, PYSNMP_MODULE_ID=hpicfPrivateVlan)
