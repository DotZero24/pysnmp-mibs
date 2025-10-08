#
# PySNMP MIB module NETSCREEN-VPN-MON-SA-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-VPN-MON-SA-COUNT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenVpn, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn")
netscreenVpnMon, = mibBuilder.importSymbols("NETSCREEN-VPN-MON-MIB", "netscreenVpnMon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nsVpnMonSACountTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2), )
if mibBuilder.loadTexts: nsVpnMonSACountTable.setStatus('mandatory')
nsVpnMonSACountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1), ).setIndexNames((0, "NETSCREEN-VPN-MON-SA-COUNT-MIB", "nsVpnMonSACountType"))
if mibBuilder.loadTexts: nsVpnMonSACountEntry.setStatus('mandatory')
nsVpnMonSACountType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountType.setStatus('mandatory')
nsVpnMonSACountTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountTotal.setStatus('mandatory')
nsVpnMonSACountAct = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountAct.setStatus('mandatory')
nsVpnMonSACountInTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountInTotal.setStatus('mandatory')
nsVpnMonSACountInAct = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountInAct.setStatus('mandatory')
nsVpnMonSACountOutTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountOutTotal.setStatus('mandatory')
nsVpnMonSACountOutAct = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnMonSACountOutAct.setStatus('mandatory')
mibBuilder.exportSymbols("NETSCREEN-VPN-MON-SA-COUNT-MIB", nsVpnMonSACountTotal=nsVpnMonSACountTotal, nsVpnMonSACountOutTotal=nsVpnMonSACountOutTotal, nsVpnMonSACountType=nsVpnMonSACountType, nsVpnMonSACountTable=nsVpnMonSACountTable, nsVpnMonSACountEntry=nsVpnMonSACountEntry, nsVpnMonSACountAct=nsVpnMonSACountAct, nsVpnMonSACountInTotal=nsVpnMonSACountInTotal, nsVpnMonSACountOutAct=nsVpnMonSACountOutAct, nsVpnMonSACountInAct=nsVpnMonSACountInAct)
