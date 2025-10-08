#
# PySNMP MIB module NETSCREEN-VPN-IAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-VPN-IAS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenVpn, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nsVpnIas = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 11))
nsVpnIasTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 11, 1), )
if mibBuilder.loadTexts: nsVpnIasTable.setStatus('mandatory')
nsVpnIasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 11, 1, 1), ).setIndexNames((0, "NETSCREEN-VPN-IAS-MIB", "nsVpnIasType"))
if mibBuilder.loadTexts: nsVpnIasEntry.setStatus('mandatory')
nsVpnIasType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIasType.setStatus('mandatory')
nsVpnIasTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 11, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIasTotal.setStatus('mandatory')
nsVpnIasSessTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 11, 2), )
if mibBuilder.loadTexts: nsVpnIasSessTable.setStatus('mandatory')
nsVpnIasSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 11, 2, 1), ).setIndexNames((0, "NETSCREEN-VPN-IAS-MIB", "nsVpnIasSessIndex"))
if mibBuilder.loadTexts: nsVpnIasSessEntry.setStatus('mandatory')
nsVpnIasSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIasSessIndex.setStatus('mandatory')
nsVpnIasSessXauthUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 11, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIasSessXauthUserName.setStatus('mandatory')
mibBuilder.exportSymbols("NETSCREEN-VPN-IAS-MIB", nsVpnIasSessXauthUserName=nsVpnIasSessXauthUserName, nsVpnIasSessEntry=nsVpnIasSessEntry, nsVpnIasType=nsVpnIasType, nsVpnIasTotal=nsVpnIasTotal, nsVpnIasEntry=nsVpnIasEntry, nsVpnIas=nsVpnIas, nsVpnIasSessTable=nsVpnIasSessTable, nsVpnIasTable=nsVpnIasTable, nsVpnIasSessIndex=nsVpnIasSessIndex)
