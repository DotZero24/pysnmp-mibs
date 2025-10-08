#
# PySNMP MIB module CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnEntry, = mibBuilder.importSymbols("TCP-MIB", "tcpConnEntry")
ciscoTcpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 6))
ciscoTcpMIB.setRevisions(('2001-11-12 00:00', '1996-12-03 00:00', '1994-07-21 00:00',))
if mibBuilder.loadTexts: ciscoTcpMIB.setLastUpdated('200111120000Z')
if mibBuilder.loadTexts: ciscoTcpMIB.setOrganization('Cisco Systems, Inc.')
ciscoTcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 1))
ciscoTcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1), )
if mibBuilder.loadTexts: ciscoTcpConnTable.setStatus('current')
ciscoTcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1), )
tcpConnEntry.registerAugmentions(("CISCO-TCP-MIB", "ciscoTcpConnEntry"))
ciscoTcpConnEntry.setIndexNames(*tcpConnEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoTcpConnEntry.setStatus('current')
ciscoTcpConnInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnInBytes.setStatus('current')
ciscoTcpConnOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnOutBytes.setStatus('current')
ciscoTcpConnInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnInPkts.setStatus('current')
ciscoTcpConnOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnOutPkts.setStatus('current')
ciscoTcpConnElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnElapsed.setStatus('current')
ciscoTcpConnSRTT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 6), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnSRTT.setStatus('current')
ciscoTcpConnRetransPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnRetransPkts.setStatus('current')
ciscoTcpConnFastRetransPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnFastRetransPkts.setStatus('current')
ciscoTcpConnRto = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 9), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnRto.setStatus('current')
ciscoTcpMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 2))
ciscoTcpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 3))
ciscoTcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1))
ciscoTcpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2))
ciscoTcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1, 1)).setObjects(("CISCO-TCP-MIB", "ciscoTcpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBCompliance = ciscoTcpMIBCompliance.setStatus('deprecated')
ciscoTcpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1, 2)).setObjects(("CISCO-TCP-MIB", "ciscoTcpMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBComplianceRev1 = ciscoTcpMIBComplianceRev1.setStatus('current')
ciscoTcpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 1)).setObjects(("CISCO-TCP-MIB", "ciscoTcpConnInBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnOutBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnInPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnOutPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnElapsed"), ("CISCO-TCP-MIB", "ciscoTcpConnSRTT"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBGroup = ciscoTcpMIBGroup.setStatus('deprecated')
ciscoTcpMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 2)).setObjects(("CISCO-TCP-MIB", "ciscoTcpConnInBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnOutBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnInPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnOutPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnElapsed"), ("CISCO-TCP-MIB", "ciscoTcpConnSRTT"), ("CISCO-TCP-MIB", "ciscoTcpConnRto"), ("CISCO-TCP-MIB", "ciscoTcpConnRetransPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnFastRetransPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBGroupRev1 = ciscoTcpMIBGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-TCP-MIB", ciscoTcpMIBObjects=ciscoTcpMIBObjects, ciscoTcpConnEntry=ciscoTcpConnEntry, ciscoTcpConnOutPkts=ciscoTcpConnOutPkts, ciscoTcpMIB=ciscoTcpMIB, ciscoTcpConnRetransPkts=ciscoTcpConnRetransPkts, ciscoTcpConnInBytes=ciscoTcpConnInBytes, ciscoTcpMIBTraps=ciscoTcpMIBTraps, ciscoTcpConnOutBytes=ciscoTcpConnOutBytes, PYSNMP_MODULE_ID=ciscoTcpMIB, ciscoTcpMIBGroup=ciscoTcpMIBGroup, ciscoTcpMIBComplianceRev1=ciscoTcpMIBComplianceRev1, ciscoTcpConnRto=ciscoTcpConnRto, ciscoTcpMIBCompliance=ciscoTcpMIBCompliance, ciscoTcpMIBGroupRev1=ciscoTcpMIBGroupRev1, ciscoTcpConnSRTT=ciscoTcpConnSRTT, ciscoTcpMIBGroups=ciscoTcpMIBGroups, ciscoTcpConnElapsed=ciscoTcpConnElapsed, ciscoTcpMIBCompliances=ciscoTcpMIBCompliances, ciscoTcpConnTable=ciscoTcpConnTable, ciscoTcpConnFastRetransPkts=ciscoTcpConnFastRetransPkts, ciscoTcpMIBConformance=ciscoTcpMIBConformance, ciscoTcpConnInPkts=ciscoTcpConnInPkts)
