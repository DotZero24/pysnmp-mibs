#
# PySNMP MIB module ELTEX-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-BRIDGE-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltexBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 35))
eltexBridgeExtMIB.setRevisions(('2015-11-15 00:00',))
if mibBuilder.loadTexts: eltexBridgeExtMIB.setLastUpdated('201511150000Z')
if mibBuilder.loadTexts: eltexBridgeExtMIB.setOrganization('Eltex Enterprise, Ltd.')
eltexBridgeExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 35, 1))
mibBuilder.exportSymbols("ELTEX-BRIDGE-EXT-MIB", eltexBridgeExtMIB=eltexBridgeExtMIB, eltexBridgeExtMIBObjects=eltexBridgeExtMIBObjects, PYSNMP_MODULE_ID=eltexBridgeExtMIB)
