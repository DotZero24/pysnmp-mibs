#
# PySNMP MIB module EXTREME-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-VRRP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("EXTREME-VRRP-MIB", extremeVrrpOperTable=extremeVrrpOperTable, extremeVrrpMIB=extremeVrrpMIB, extremeVrrpMIBGroups=extremeVrrpMIBGroups, extremeVrrpMIBCompliance=extremeVrrpMIBCompliance, extremeVrrpOperGroup=extremeVrrpOperGroup, PYSNMP_MODULE_ID=extremeVrrpMIB, extremeVrrpFabricRoutingMode=extremeVrrpFabricRoutingMode, extremeVrrpConformance=extremeVrrpConformance, extremeVrrpOperations=extremeVrrpOperations, extremeVrrpOperEntry=extremeVrrpOperEntry, extremeVrrpMIBCompliances=extremeVrrpMIBCompliances)
