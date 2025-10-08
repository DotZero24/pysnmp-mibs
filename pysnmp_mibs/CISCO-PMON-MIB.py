#
# PySNMP MIB module CISCO-PMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-PMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoInterfaceIndexList, = mibBuilder.importSymbols("CISCO-TC", "CiscoInterfaceIndexList")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPmonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 779))
ciscoPmonMIB.setRevisions(('2012-01-03 00:00',))
if mibBuilder.loadTexts: ciscoPmonMIB.setLastUpdated('201201030000Z')
if mibBuilder.loadTexts: ciscoPmonMIB.setOrganization('Cisco Systems, Inc.')
ciscoPmonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 0))
ciscoPmonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 1))
ciscoPmonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2))
ciscoPmonStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1))
ciscoPmonPortGroupStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsTable.setStatus('current')
ciscoPmonPortGroupStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupStatsType"), (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupIndex"))
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsEntry.setStatus('current')
ciscoPmonPortGroupStatsType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("errPktsFromPort", 1), ("errPktsToXbar", 2), ("errPktsFromXbar", 3))))
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsType.setStatus('current')
ciscoPmonPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ciscoPmonPortGroupIndex.setStatus('current')
ciscoPmonPortGroupIfIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 3), CiscoInterfaceIndexList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPmonPortGroupIfIndexList.setStatus('current')
ciscoPmonPortGroupStatsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsValue.setStatus('current')
ciscoPmonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1))
ciscoPmonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2))
ciscoPmonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1, 1)).setObjects(("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPmonMIBCompliance = ciscoPmonMIBCompliance.setStatus('current')
ciscoPmonPortGroupStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2, 1)).setObjects(("CISCO-PMON-MIB", "ciscoPmonPortGroupIfIndexList"), ("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPmonPortGroupStatsGroup = ciscoPmonPortGroupStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PMON-MIB", ciscoPmonPortGroupStatsGroup=ciscoPmonPortGroupStatsGroup, ciscoPmonMIBCompliances=ciscoPmonMIBCompliances, ciscoPmonPortGroupStatsTable=ciscoPmonPortGroupStatsTable, ciscoPmonStatsMIBObjects=ciscoPmonStatsMIBObjects, ciscoPmonMIBNotifs=ciscoPmonMIBNotifs, ciscoPmonMIB=ciscoPmonMIB, ciscoPmonMIBConformance=ciscoPmonMIBConformance, ciscoPmonMIBObjects=ciscoPmonMIBObjects, ciscoPmonPortGroupIfIndexList=ciscoPmonPortGroupIfIndexList, ciscoPmonMIBGroups=ciscoPmonMIBGroups, PYSNMP_MODULE_ID=ciscoPmonMIB, ciscoPmonPortGroupStatsType=ciscoPmonPortGroupStatsType, ciscoPmonPortGroupIndex=ciscoPmonPortGroupIndex, ciscoPmonMIBCompliance=ciscoPmonMIBCompliance, ciscoPmonPortGroupStatsEntry=ciscoPmonPortGroupStatsEntry, ciscoPmonPortGroupStatsValue=ciscoPmonPortGroupStatsValue)
