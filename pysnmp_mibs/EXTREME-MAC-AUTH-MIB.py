#
# PySNMP MIB module EXTREME-MAC-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-MAC-AUTH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TruthValue, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention")
extremeMacAuthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 44))
if mibBuilder.loadTexts: extremeMacAuthMIB.setLastUpdated('201403040000Z')
if mibBuilder.loadTexts: extremeMacAuthMIB.setOrganization('Extreme Networks, Inc.')
extremeMacAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 44, 1))
extremeMacAuthClientTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1), )
if mibBuilder.loadTexts: extremeMacAuthClientTable.setStatus('current')
extremeMacAuthClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1), ).setIndexNames((0, "EXTREME-MAC-AUTH-MIB", "extremeMacAuthClientAddress"))
if mibBuilder.loadTexts: extremeMacAuthClientEntry.setStatus('current')
extremeMacAuthClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: extremeMacAuthClientAddress.setStatus('current')
extremeMacAuthClientInitialize = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeMacAuthClientInitialize.setStatus('current')
extremeMacAuthClientReauthenticate = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeMacAuthClientReauthenticate.setStatus('current')
mibBuilder.exportSymbols("EXTREME-MAC-AUTH-MIB", extremeMacAuthObjects=extremeMacAuthObjects, extremeMacAuthClientEntry=extremeMacAuthClientEntry, PYSNMP_MODULE_ID=extremeMacAuthMIB, extremeMacAuthClientAddress=extremeMacAuthClientAddress, extremeMacAuthMIB=extremeMacAuthMIB, extremeMacAuthClientTable=extremeMacAuthClientTable, extremeMacAuthClientInitialize=extremeMacAuthClientInitialize, extremeMacAuthClientReauthenticate=extremeMacAuthClientReauthenticate)
