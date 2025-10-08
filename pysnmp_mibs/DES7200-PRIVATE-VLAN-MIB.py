#
# PySNMP MIB module DES7200-PRIVATE-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-PRIVATE-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("DES7200-PRIVATE-VLAN-MIB", mypvlanVlanEntry=mypvlanVlanEntry, mypvlanPortMode=mypvlanPortMode, VlanIndexOrZero=VlanIndexOrZero, mypvlanPortModeGroup=mypvlanPortModeGroup, mypvlanPrivatePortTable=mypvlanPrivatePortTable, mypvlanSVIGroup=mypvlanSVIGroup, mypvlanPrivatePortEntry=mypvlanPrivatePortEntry, mypvlanPromPortGroup=mypvlanPromPortGroup, myPrivateVlanMIB=myPrivateVlanMIB, mypvlanVlanObjects=mypvlanVlanObjects, mypvlanPromPortSecondaryRemap2k=mypvlanPromPortSecondaryRemap2k, mypvlanPromPortSecondaryRemap3k=mypvlanPromPortSecondaryRemap3k, mypvlanSVIMappingEntry=mypvlanSVIMappingEntry, mypvlanMIBObjects=mypvlanMIBObjects, mypvlanSVIMappingVlanIndex=mypvlanSVIMappingVlanIndex, mypvlanPrivatePortGroup=mypvlanPrivatePortGroup, mypvlanPortModeEntry=mypvlanPortModeEntry, mypvlanSVIObjects=mypvlanSVIObjects, VlanIndexBitmap=VlanIndexBitmap, mypvlanPortModeTable=mypvlanPortModeTable, mypvlanPromPortSecondaryRemap=mypvlanPromPortSecondaryRemap, mypvlanVlanAssociatedPrimaryVlan=mypvlanVlanAssociatedPrimaryVlan, mypvlanPrivatePortPrimaryVlan=mypvlanPrivatePortPrimaryVlan, mypvlanMIBGroups=mypvlanMIBGroups, mypvlanPrivatePortPrimaryVlanId=mypvlanPrivatePortPrimaryVlanId, mypvlanVlanGroup=mypvlanVlanGroup, mypvlanMIBCompliances=mypvlanMIBCompliances, mypvlanVlanTable=mypvlanVlanTable, mypvlanVlanPrivateVlanType=mypvlanVlanPrivateVlanType, mypvlanPortObjects=mypvlanPortObjects, PrivateVlanType=PrivateVlanType, mypvlanSVIMappingPrimarySVI=mypvlanSVIMappingPrimarySVI, mypvlanSVIMappingTable=mypvlanSVIMappingTable, mypvlanPromPortEntry=mypvlanPromPortEntry, mypvlanPrivatePortSecondaryVlan=mypvlanPrivatePortSecondaryVlan, mypvlanMIBCompliance=mypvlanMIBCompliance, PYSNMP_MODULE_ID=myPrivateVlanMIB, mypvlanPromPortTable=mypvlanPromPortTable, mypvlanVlanIndex=mypvlanVlanIndex, mypvlanIfAssociatedPrimaryVlan=mypvlanIfAssociatedPrimaryVlan, mypvlanPromPortSecondaryRemap4k=mypvlanPromPortSecondaryRemap4k, mypvlanMIBConformance=mypvlanMIBConformance)
