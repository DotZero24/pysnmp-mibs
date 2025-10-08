#
# PySNMP MIB module RBN-MPLS-L3VPN-STD-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-MPLS-L3VPN-STD-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
MplsL3VpnRtType, mplsL3VpnVrfName, MplsL3VpnRouteDistinguisher = mibBuilder.importSymbols("MPLS-L3VPN-STD-MIB", "MplsL3VpnRtType", "mplsL3VpnVrfName", "MplsL3VpnRouteDistinguisher")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnMplsL3VpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 51))
rbnMplsL3VpnMIB.setRevisions(('2009-05-30 00:00',))
if mibBuilder.loadTexts: rbnMplsL3VpnMIB.setLastUpdated('200905300000Z')
if mibBuilder.loadTexts: rbnMplsL3VpnMIB.setOrganization('RedBack Networks, Inc.')
rbnMplsL3VpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1))
rbnMplsL3VpnConf = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1))
rbnMplsL3VpnConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 51, 2))
rbnMplsL3VpnVrfRTTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1), )
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRTTable.setStatus('current')
rbnMplsL3VpnVrfRTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1), ).setIndexNames((0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"), (0, "RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTAddrFamily"), (0, "RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTType"), (0, "RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTIndex"))
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRTEntry.setStatus('current')
rbnMplsL3VpnVrfRTAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRTAddrFamily.setStatus('current')
rbnMplsL3VpnVrfRTType = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 2), MplsL3VpnRtType())
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRTType.setStatus('current')
rbnMplsL3VpnVrfRTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRTIndex.setStatus('current')
rbnMplsL3VpnVrfRT = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 4), MplsL3VpnRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRT.setStatus('current')
rbnMplsL3VpnVrfRTDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 51, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnMplsL3VpnVrfRTDescr.setStatus('current')
rbnMplsL3VpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 1))
rbnMplsL3VpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 2))
rbnMplsL3VpnModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 2, 1)).setObjects(("RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMplsL3VpnModuleCompliance = rbnMplsL3VpnModuleCompliance.setStatus('current')
rbnMplsL3VpnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 51, 2, 1, 1)).setObjects(("RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRT"), ("RBN-MPLS-L3VPN-STD-EXT-MIB", "rbnMplsL3VpnVrfRTDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMplsL3VpnGroup = rbnMplsL3VpnGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-MPLS-L3VPN-STD-EXT-MIB", rbnMplsL3VpnMIB=rbnMplsL3VpnMIB, rbnMplsL3VpnConformance=rbnMplsL3VpnConformance, rbnMplsL3VpnVrfRTEntry=rbnMplsL3VpnVrfRTEntry, rbnMplsL3VpnVrfRT=rbnMplsL3VpnVrfRT, rbnMplsL3VpnModuleCompliance=rbnMplsL3VpnModuleCompliance, rbnMplsL3VpnVrfRTDescr=rbnMplsL3VpnVrfRTDescr, rbnMplsL3VpnVrfRTIndex=rbnMplsL3VpnVrfRTIndex, rbnMplsL3VpnGroups=rbnMplsL3VpnGroups, rbnMplsL3VpnObjects=rbnMplsL3VpnObjects, PYSNMP_MODULE_ID=rbnMplsL3VpnMIB, rbnMplsL3VpnVrfRTTable=rbnMplsL3VpnVrfRTTable, rbnMplsL3VpnVrfRTAddrFamily=rbnMplsL3VpnVrfRTAddrFamily, rbnMplsL3VpnConf=rbnMplsL3VpnConf, rbnMplsL3VpnVrfRTType=rbnMplsL3VpnVrfRTType, rbnMplsL3VpnGroup=rbnMplsL3VpnGroup, rbnMplsL3VpnCompliances=rbnMplsL3VpnCompliances)
