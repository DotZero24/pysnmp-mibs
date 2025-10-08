#
# PySNMP MIB module INFINERA-ENTITY-FBM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FBM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
fbmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55))
if mibBuilder.loadTexts: fbmMIB.setLastUpdated('201701170000Z')
if mibBuilder.loadTexts: fbmMIB.setOrganization('Infinera')
fbmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3))
fbmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 1))
fbmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 2))
fbmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1), )
if mibBuilder.loadTexts: fbmTable.setStatus('current')
fbmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: fbmEntry.setStatus('current')
fbmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fbmMoId.setStatus('current')
fbmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fbmProvEqptType.setStatus('current')
fbmUsbUpstreamNbr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbmUsbUpstreamNbr.setStatus('current')
fbmUsbDownstreamNbr = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fbmUsbDownstreamNbr.setStatus('current')
fbmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 1, 1)).setObjects(("INFINERA-ENTITY-FBM-MIB", "fbmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fbmCompliance = fbmCompliance.setStatus('current')
fbmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 2, 1)).setObjects(("INFINERA-ENTITY-FBM-MIB", "fbmMoId"), ("INFINERA-ENTITY-FBM-MIB", "fbmProvEqptType"), ("INFINERA-ENTITY-FBM-MIB", "fbmUsbUpstreamNbr"), ("INFINERA-ENTITY-FBM-MIB", "fbmUsbDownstreamNbr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fbmGroup = fbmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-FBM-MIB", fbmEntry=fbmEntry, fbmMoId=fbmMoId, fbmConformance=fbmConformance, fbmProvEqptType=fbmProvEqptType, PYSNMP_MODULE_ID=fbmMIB, fbmGroups=fbmGroups, fbmMIB=fbmMIB, fbmCompliances=fbmCompliances, fbmUsbDownstreamNbr=fbmUsbDownstreamNbr, fbmTable=fbmTable, fbmGroup=fbmGroup, fbmUsbUpstreamNbr=fbmUsbUpstreamNbr, fbmCompliance=fbmCompliance)
