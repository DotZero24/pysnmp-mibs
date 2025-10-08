#
# PySNMP MIB module DES7200-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DES7200-PRIVATE-VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
myPrivateVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44))
myPrivateVlanMIB.setRevisions(('2009-03-01 00:00',))
if mibBuilder.loadTexts: myPrivateVlanMIB.setLastUpdated('200903230000Z')
if mibBuilder.loadTexts: myPrivateVlanMIB.setOrganization('D-Link Crop.')
class PrivateVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("primary", 2), ("isolated", 3), ("community", 4))

class VlanIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanIndexBitmap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

mypvlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1))
mypvlanVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1))
mypvlanPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2))
mypvlanSVIObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3))
mypvlanVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1), )
if mibBuilder.loadTexts: mypvlanVlanTable.setStatus('current')
mypvlanVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1), ).setIndexNames((0, "DES7200-PRIVATE-VLAN-MIB", "mypvlanVlanIndex"))
if mibBuilder.loadTexts: mypvlanVlanEntry.setStatus('current')
mypvlanVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 1), VlanIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mypvlanVlanIndex.setStatus('current')
mypvlanVlanPrivateVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 2), PrivateVlanType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mypvlanVlanPrivateVlanType.setStatus('current')
mypvlanVlanAssociatedPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 3), VlanIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mypvlanVlanAssociatedPrimaryVlan.setStatus('current')
mypvlanIfAssociatedPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mypvlanIfAssociatedPrimaryVlan.setStatus('current')
mypvlanPrivatePortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1), )
if mibBuilder.loadTexts: mypvlanPrivatePortTable.setStatus('current')
mypvlanPrivatePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mypvlanPrivatePortEntry.setStatus('current')
mypvlanPrivatePortPrimaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1, 1), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPrivatePortPrimaryVlan.setStatus('current')
mypvlanPrivatePortSecondaryVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 1, 1, 2), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPrivatePortSecondaryVlan.setStatus('current')
mypvlanPromPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2), )
if mibBuilder.loadTexts: mypvlanPromPortTable.setStatus('current')
mypvlanPromPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mypvlanPromPortEntry.setStatus('current')
mypvlanPrivatePortPrimaryVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 1), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPrivatePortPrimaryVlanId.setStatus('current')
mypvlanPromPortSecondaryRemap = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap.setStatus('current')
mypvlanPromPortSecondaryRemap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap2k.setStatus('current')
mypvlanPromPortSecondaryRemap3k = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap3k.setStatus('current')
mypvlanPromPortSecondaryRemap4k = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPromPortSecondaryRemap4k.setStatus('current')
mypvlanPortModeTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3), )
if mibBuilder.loadTexts: mypvlanPortModeTable.setStatus('current')
mypvlanPortModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mypvlanPortModeEntry.setStatus('current')
mypvlanPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonPrivateVlan", 1), ("host", 2), ("promiscuous", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanPortMode.setStatus('current')
mypvlanSVIMappingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1), )
if mibBuilder.loadTexts: mypvlanSVIMappingTable.setStatus('current')
mypvlanSVIMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1), ).setIndexNames((0, "DES7200-PRIVATE-VLAN-MIB", "mypvlanSVIMappingVlanIndex"))
if mibBuilder.loadTexts: mypvlanSVIMappingEntry.setStatus('current')
mypvlanSVIMappingVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1, 1), VlanIndexOrZero())
if mibBuilder.loadTexts: mypvlanSVIMappingVlanIndex.setStatus('current')
mypvlanSVIMappingPrimarySVI = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 1, 3, 1, 1, 2), VlanIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mypvlanSVIMappingPrimarySVI.setStatus('current')
mypvlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2))
mypvlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 1))
mypvlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2))
mypvlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 1, 1)).setObjects(("DES7200-PRIVATE-VLAN-MIB", "mypvlanVlanGroup"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPrivatePortGroup"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPromPortGroup"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPortModeGroup"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanSVIGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanMIBCompliance = mypvlanMIBCompliance.setStatus('current')
mypvlanVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 1)).setObjects(("DES7200-PRIVATE-VLAN-MIB", "mypvlanVlanIndex"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanVlanPrivateVlanType"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanVlanAssociatedPrimaryVlan"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanIfAssociatedPrimaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanVlanGroup = mypvlanVlanGroup.setStatus('current')
mypvlanPrivatePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 2)).setObjects(("DES7200-PRIVATE-VLAN-MIB", "mypvlanPrivatePortPrimaryVlan"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPrivatePortSecondaryVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanPrivatePortGroup = mypvlanPrivatePortGroup.setStatus('current')
mypvlanPromPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 3)).setObjects(("DES7200-PRIVATE-VLAN-MIB", "mypvlanPrivatePortPrimaryVlan"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap2k"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap3k"), ("DES7200-PRIVATE-VLAN-MIB", "mypvlanPromPortSecondaryRemap4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanPromPortGroup = mypvlanPromPortGroup.setStatus('current')
mypvlanPortModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 4)).setObjects(("DES7200-PRIVATE-VLAN-MIB", "mypvlanPortMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanPortModeGroup = mypvlanPortModeGroup.setStatus('current')
mypvlanSVIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 44, 2, 2, 5)).setObjects(("DES7200-PRIVATE-VLAN-MIB", "mypvlanSVIMappingPrimarySVI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mypvlanSVIGroup = mypvlanSVIGroup.setStatus('current')
mibBuilder.exportSymbols("DES7200-PRIVATE-VLAN-MIB", mypvlanPromPortEntry=mypvlanPromPortEntry, mypvlanIfAssociatedPrimaryVlan=mypvlanIfAssociatedPrimaryVlan, mypvlanMIBGroups=mypvlanMIBGroups, mypvlanSVIMappingTable=mypvlanSVIMappingTable, mypvlanMIBObjects=mypvlanMIBObjects, mypvlanPortModeTable=mypvlanPortModeTable, mypvlanVlanEntry=mypvlanVlanEntry, mypvlanMIBCompliances=mypvlanMIBCompliances, mypvlanVlanAssociatedPrimaryVlan=mypvlanVlanAssociatedPrimaryVlan, mypvlanSVIMappingVlanIndex=mypvlanSVIMappingVlanIndex, mypvlanSVIObjects=mypvlanSVIObjects, VlanIndexBitmap=VlanIndexBitmap, mypvlanPromPortSecondaryRemap4k=mypvlanPromPortSecondaryRemap4k, mypvlanPrivatePortEntry=mypvlanPrivatePortEntry, PrivateVlanType=PrivateVlanType, mypvlanPromPortSecondaryRemap3k=mypvlanPromPortSecondaryRemap3k, mypvlanPrivatePortSecondaryVlan=mypvlanPrivatePortSecondaryVlan, mypvlanMIBCompliance=mypvlanMIBCompliance, mypvlanPromPortSecondaryRemap2k=mypvlanPromPortSecondaryRemap2k, mypvlanVlanPrivateVlanType=mypvlanVlanPrivateVlanType, mypvlanPrivatePortPrimaryVlanId=mypvlanPrivatePortPrimaryVlanId, mypvlanPortMode=mypvlanPortMode, mypvlanPortModeGroup=mypvlanPortModeGroup, mypvlanVlanIndex=mypvlanVlanIndex, PYSNMP_MODULE_ID=myPrivateVlanMIB, mypvlanPromPortSecondaryRemap=mypvlanPromPortSecondaryRemap, mypvlanPrivatePortPrimaryVlan=mypvlanPrivatePortPrimaryVlan, mypvlanSVIMappingPrimarySVI=mypvlanSVIMappingPrimarySVI, mypvlanVlanGroup=mypvlanVlanGroup, mypvlanPrivatePortTable=mypvlanPrivatePortTable, mypvlanSVIGroup=mypvlanSVIGroup, mypvlanPromPortTable=mypvlanPromPortTable, mypvlanPromPortGroup=mypvlanPromPortGroup, mypvlanSVIMappingEntry=mypvlanSVIMappingEntry, mypvlanMIBConformance=mypvlanMIBConformance, VlanIndexOrZero=VlanIndexOrZero, myPrivateVlanMIB=myPrivateVlanMIB, mypvlanVlanObjects=mypvlanVlanObjects, mypvlanPortObjects=mypvlanPortObjects, mypvlanPortModeEntry=mypvlanPortModeEntry, mypvlanPrivatePortGroup=mypvlanPrivatePortGroup, mypvlanVlanTable=mypvlanVlanTable)
