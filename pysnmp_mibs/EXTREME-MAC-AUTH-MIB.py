#
# PySNMP MIB module EXTREME-MAC-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-MAC-AUTH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("EXTREME-MAC-AUTH-MIB", PYSNMP_MODULE_ID=extremeMacAuthMIB, extremeMacAuthClientTable=extremeMacAuthClientTable, extremeMacAuthClientAddress=extremeMacAuthClientAddress, extremeMacAuthClientReauthenticate=extremeMacAuthClientReauthenticate, extremeMacAuthClientInitialize=extremeMacAuthClientInitialize, extremeMacAuthObjects=extremeMacAuthObjects, extremeMacAuthMIB=extremeMacAuthMIB, extremeMacAuthClientEntry=extremeMacAuthClientEntry)
