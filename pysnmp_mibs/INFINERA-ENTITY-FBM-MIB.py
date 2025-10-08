#
# PySNMP MIB module INFINERA-ENTITY-FBM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FBM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-FBM-MIB", fbmGroups=fbmGroups, fbmUsbUpstreamNbr=fbmUsbUpstreamNbr, PYSNMP_MODULE_ID=fbmMIB, fbmMIB=fbmMIB, fbmGroup=fbmGroup, fbmCompliance=fbmCompliance, fbmTable=fbmTable, fbmCompliances=fbmCompliances, fbmProvEqptType=fbmProvEqptType, fbmEntry=fbmEntry, fbmConformance=fbmConformance, fbmUsbDownstreamNbr=fbmUsbDownstreamNbr, fbmMoId=fbmMoId)
