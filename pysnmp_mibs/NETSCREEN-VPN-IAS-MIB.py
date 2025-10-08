#
# PySNMP MIB module NETSCREEN-VPN-IAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netscreen/NETSCREEN-VPN-IAS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netscreenVpn, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NETSCREEN-VPN-IAS-MIB", nsVpnIasSessXauthUserName=nsVpnIasSessXauthUserName, nsVpnIasType=nsVpnIasType, nsVpnIasSessTable=nsVpnIasSessTable, nsVpnIas=nsVpnIas, nsVpnIasSessIndex=nsVpnIasSessIndex, nsVpnIasEntry=nsVpnIasEntry, nsVpnIasTable=nsVpnIasTable, nsVpnIasSessEntry=nsVpnIasSessEntry, nsVpnIasTotal=nsVpnIasTotal)
