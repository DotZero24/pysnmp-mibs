#
# PySNMP MIB module PDN-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46))
pdnVlanMIB.setRevisions(('2003-11-12 00:00', '2003-04-24 00:00', '2003-04-11 00:00',))
if mibBuilder.loadTexts: pdnVlanMIB.setLastUpdated('200311120000Z')
if mibBuilder.loadTexts: pdnVlanMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnVlanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 0))
pdnVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1))
pdnVlanAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 2))
pdnVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3))
pdnVlanReservedBlockStart = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 1), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanReservedBlockStart.setStatus('current')
pdnVlanInbandMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 2), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId.setStatus('current')
pdnVlanInbandMgmtVlanId2 = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 3), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId2.setStatus('current')
pdnVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1))
pdnVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2))
pdnVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1, 1)).setObjects(("PDN-VLAN-MIB", "pdnVlanReservedBlockGroup"), ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanMIBCompliance = pdnVlanMIBCompliance.setStatus('current')
pdnVlanObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1))
pdnVlanAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 2))
pdnVlanNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 3))
pdnVlanReservedBlockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 1)).setObjects(("PDN-VLAN-MIB", "pdnVlanReservedBlockStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanReservedBlockGroup = pdnVlanReservedBlockGroup.setStatus('current')
pdnVlanInbandMgmtVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 2)).setObjects(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanInbandMgmtVlanGroup = pdnVlanInbandMgmtVlanGroup.setStatus('current')
pdnVlanInbandMgmtVlan2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 3)).setObjects(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"), ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanInbandMgmtVlan2Group = pdnVlanInbandMgmtVlan2Group.setStatus('current')
mibBuilder.exportSymbols("PDN-VLAN-MIB", pdnVlanReservedBlockStart=pdnVlanReservedBlockStart, pdnVlanInbandMgmtVlanId=pdnVlanInbandMgmtVlanId, pdnVlanAfnGroups=pdnVlanAfnGroups, pdnVlanInbandMgmtVlanGroup=pdnVlanInbandMgmtVlanGroup, pdnVlanCompliances=pdnVlanCompliances, pdnVlanMIBCompliance=pdnVlanMIBCompliance, pdnVlanInbandMgmtVlan2Group=pdnVlanInbandMgmtVlan2Group, pdnVlanObjects=pdnVlanObjects, pdnVlanGroups=pdnVlanGroups, pdnVlanObjGroups=pdnVlanObjGroups, pdnVlanConformance=pdnVlanConformance, pdnVlanInbandMgmtVlanId2=pdnVlanInbandMgmtVlanId2, pdnVlanReservedBlockGroup=pdnVlanReservedBlockGroup, pdnVlanAFNs=pdnVlanAFNs, pdnVlanNtfyGroups=pdnVlanNtfyGroups, pdnVlanNotifications=pdnVlanNotifications, PYSNMP_MODULE_ID=pdnVlanMIB, pdnVlanMIB=pdnVlanMIB)
