#
# PySNMP MIB module ELTEX-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-BRIDGE-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltexBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 35))
eltexBridgeExtMIB.setRevisions(('2015-11-15 00:00',))
if mibBuilder.loadTexts: eltexBridgeExtMIB.setLastUpdated('201511150000Z')
if mibBuilder.loadTexts: eltexBridgeExtMIB.setOrganization('Eltex Enterprise, Ltd.')
eltexBridgeExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 35, 1))
mibBuilder.exportSymbols("ELTEX-BRIDGE-EXT-MIB", PYSNMP_MODULE_ID=eltexBridgeExtMIB, eltexBridgeExtMIB=eltexBridgeExtMIB, eltexBridgeExtMIBObjects=eltexBridgeExtMIBObjects)
