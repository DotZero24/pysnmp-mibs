#
# PySNMP MIB module CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-TCP-MIB", ciscoTcpMIBGroupRev1=ciscoTcpMIBGroupRev1, ciscoTcpConnEntry=ciscoTcpConnEntry, ciscoTcpMIBConformance=ciscoTcpMIBConformance, ciscoTcpConnInBytes=ciscoTcpConnInBytes, PYSNMP_MODULE_ID=ciscoTcpMIB, ciscoTcpConnOutPkts=ciscoTcpConnOutPkts, ciscoTcpConnElapsed=ciscoTcpConnElapsed, ciscoTcpMIBObjects=ciscoTcpMIBObjects, ciscoTcpMIBComplianceRev1=ciscoTcpMIBComplianceRev1, ciscoTcpConnFastRetransPkts=ciscoTcpConnFastRetransPkts, ciscoTcpMIBCompliances=ciscoTcpMIBCompliances, ciscoTcpConnInPkts=ciscoTcpConnInPkts, ciscoTcpMIB=ciscoTcpMIB, ciscoTcpConnRetransPkts=ciscoTcpConnRetransPkts, ciscoTcpMIBCompliance=ciscoTcpMIBCompliance, ciscoTcpConnRto=ciscoTcpConnRto, ciscoTcpMIBGroups=ciscoTcpMIBGroups, ciscoTcpMIBGroup=ciscoTcpMIBGroup, ciscoTcpConnSRTT=ciscoTcpConnSRTT, ciscoTcpConnOutBytes=ciscoTcpConnOutBytes, ciscoTcpMIBTraps=ciscoTcpMIBTraps, ciscoTcpConnTable=ciscoTcpConnTable)
