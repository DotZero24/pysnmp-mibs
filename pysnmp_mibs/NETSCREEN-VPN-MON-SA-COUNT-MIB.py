#
# PySNMP MIB module NETSCREEN-VPN-MON-SA-COUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netscreen/NETSCREEN-VPN-MON-SA-COUNT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netscreenVpn, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn")
netscreenVpnMon, = mibBuilder.importSymbols("NETSCREEN-VPN-MON-MIB", "netscreenVpnMon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NETSCREEN-VPN-MON-SA-COUNT-MIB", nsVpnMonSACountTotal=nsVpnMonSACountTotal, nsVpnMonSACountAct=nsVpnMonSACountAct, nsVpnMonSACountInTotal=nsVpnMonSACountInTotal, nsVpnMonSACountOutAct=nsVpnMonSACountOutAct, nsVpnMonSACountInAct=nsVpnMonSACountInAct, nsVpnMonSACountOutTotal=nsVpnMonSACountOutTotal, nsVpnMonSACountType=nsVpnMonSACountType, nsVpnMonSACountEntry=nsVpnMonSACountEntry, nsVpnMonSACountTable=nsVpnMonSACountTable)
