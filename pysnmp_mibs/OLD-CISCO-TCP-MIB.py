#
# PySNMP MIB module OLD-CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/OLD-CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tcpConnRemAddress, tcpConnLocalAddress, tcpConnRemPort, tcpConnLocalPort = mibBuilder.importSymbols("TCP-MIB", "tcpConnRemAddress", "tcpConnLocalAddress", "tcpConnRemPort", "tcpConnLocalPort")
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
mibBuilder.exportSymbols("OLD-CISCO-TCP-MIB", loctcpConnInPkts=loctcpConnInPkts, loctcpConnElapsed=loctcpConnElapsed, loctcpConnInBytes=loctcpConnInBytes, ltcp=ltcp, ltcpConnEntry=ltcpConnEntry, ltcpConnTable=ltcpConnTable, loctcpConnOutBytes=loctcpConnOutBytes, loctcpConnOutPkts=loctcpConnOutPkts)
