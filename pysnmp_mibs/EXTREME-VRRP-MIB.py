#
# PySNMP MIB module EXTREME-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-VRRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
vrrpOperVrId, = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperVrId")
extremeVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 49))
extremeVrrpMIB.setRevisions(('2016-01-04 00:00',))
if mibBuilder.loadTexts: extremeVrrpMIB.setLastUpdated('201601040000Z')
if mibBuilder.loadTexts: extremeVrrpMIB.setOrganization('Extreme Networks, Inc.')
extremeVrrpOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 49, 1))
extremeVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 49, 2))
extremeVrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 49, 1, 1), )
if mibBuilder.loadTexts: extremeVrrpOperTable.setStatus('current')
extremeVrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 49, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"))
if mibBuilder.loadTexts: extremeVrrpOperEntry.setStatus('current')
extremeVrrpFabricRoutingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 49, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVrrpFabricRoutingMode.setStatus('current')
extremeVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 1))
extremeVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 2))
extremeVrrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 1, 1)).setObjects(("EXTREME-VRRP-MIB", "extremeVrrpOperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    extremeVrrpMIBCompliance = extremeVrrpMIBCompliance.setStatus('current')
extremeVrrpOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1916, 1, 49, 2, 2, 1)).setObjects(("EXTREME-VRRP-MIB", "extremeVrrpFabricRoutingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    extremeVrrpOperGroup = extremeVrrpOperGroup.setStatus('current')
mibBuilder.exportSymbols("EXTREME-VRRP-MIB", extremeVrrpOperations=extremeVrrpOperations, extremeVrrpOperGroup=extremeVrrpOperGroup, PYSNMP_MODULE_ID=extremeVrrpMIB, extremeVrrpFabricRoutingMode=extremeVrrpFabricRoutingMode, extremeVrrpOperEntry=extremeVrrpOperEntry, extremeVrrpMIB=extremeVrrpMIB, extremeVrrpConformance=extremeVrrpConformance, extremeVrrpMIBCompliances=extremeVrrpMIBCompliances, extremeVrrpOperTable=extremeVrrpOperTable, extremeVrrpMIBCompliance=extremeVrrpMIBCompliance, extremeVrrpMIBGroups=extremeVrrpMIBGroups)
