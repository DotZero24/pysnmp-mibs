#
# PySNMP MIB module OLD-CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/OLD-CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnLocalPort, tcpConnRemAddress, tcpConnLocalAddress, tcpConnRemPort = mibBuilder.importSymbols("TCP-MIB", "tcpConnLocalPort", "tcpConnRemAddress", "tcpConnLocalAddress", "tcpConnRemPort")
ltcp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 6))
ltcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 6, 1), )
if mibBuilder.loadTexts: ltcpConnTable.setStatus('deprecated')
ltcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnLocalAddress"), (0, "TCP-MIB", "tcpConnLocalPort"), (0, "TCP-MIB", "tcpConnRemAddress"), (0, "TCP-MIB", "tcpConnRemPort"))
if mibBuilder.loadTexts: ltcpConnEntry.setStatus('deprecated')
loctcpConnInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnInBytes.setStatus('deprecated')
loctcpConnOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnOutBytes.setStatus('deprecated')
loctcpConnInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnInPkts.setStatus('deprecated')
loctcpConnOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnOutPkts.setStatus('deprecated')
loctcpConnElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: loctcpConnElapsed.setStatus('deprecated')
mibBuilder.exportSymbols("OLD-CISCO-TCP-MIB", loctcpConnOutBytes=loctcpConnOutBytes, ltcpConnEntry=ltcpConnEntry, loctcpConnOutPkts=loctcpConnOutPkts, ltcpConnTable=ltcpConnTable, ltcp=ltcp, loctcpConnInBytes=loctcpConnInBytes, loctcpConnInPkts=loctcpConnInPkts, loctcpConnElapsed=loctcpConnElapsed)
