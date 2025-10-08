#
# PySNMP MIB module HP-ICF-PRIVATEVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-PRIVATEVLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
VlanId, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "dot1qVlanStaticEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HP-ICF-PRIVATEVLAN-MIB", hpicfPrivateVlanCompliances=hpicfPrivateVlanCompliances, hpicfPrivateVlanObjects=hpicfPrivateVlanObjects, hpicfPrivateVlanType=hpicfPrivateVlanType, hpicfPrivateVlanMappingEntry=hpicfPrivateVlanMappingEntry, hpicfPrivateVlanTable=hpicfPrivateVlanTable, hpicfPrivateVlanEntry=hpicfPrivateVlanEntry, PYSNMP_MODULE_ID=hpicfPrivateVlan, hpicfPrivateVlanGroup=hpicfPrivateVlanGroup, PrivateVlanType=PrivateVlanType, hpicfPrivateVlanConfig=hpicfPrivateVlanConfig, hpicfPrivateVlanCommunity=hpicfPrivateVlanCommunity, hpicfPrivateVlanPrimary=hpicfPrivateVlanPrimary, hpicfPrivateVlanConformance=hpicfPrivateVlanConformance, hpicfPrivateVlanMappingTable=hpicfPrivateVlanMappingTable, hpicfPrivateVlanTableGroup=hpicfPrivateVlanTableGroup, hpicfPrivateVlanMappingRowStatus=hpicfPrivateVlanMappingRowStatus, hpicfPVlanMappingTblCompliance=hpicfPVlanMappingTblCompliance, hpicfPVlanMappingTableGroup=hpicfPVlanMappingTableGroup, hpicfPVlanTableCompliance=hpicfPVlanTableCompliance, hpicfPrivateVlan=hpicfPrivateVlan, hpicfPrivateVlanIsolated=hpicfPrivateVlanIsolated)
