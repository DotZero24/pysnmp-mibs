#
# PySNMP MIB module INFINERA-ENTITY-CWM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-CWM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:53 2025
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
cwmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57))
if mibBuilder.loadTexts: cwmMIB.setLastUpdated('201505100000Z')
if mibBuilder.loadTexts: cwmMIB.setOrganization('Infinera')
cwmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3))
cwmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 1))
cwmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 2))
cwmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1), )
if mibBuilder.loadTexts: cwmTable.setStatus('current')
cwmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cwmEntry.setStatus('current')
cwmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmMoId.setStatus('current')
cwmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmProvEqptType.setStatus('current')
cwmAssociatedDegree = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmAssociatedDegree.setStatus('current')
cwmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 1, 1)).setObjects(("INFINERA-ENTITY-CWM-MIB", "cwmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmCompliance = cwmCompliance.setStatus('current')
cwmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 2, 1)).setObjects(("INFINERA-ENTITY-CWM-MIB", "cwmMoId"), ("INFINERA-ENTITY-CWM-MIB", "cwmProvEqptType"), ("INFINERA-ENTITY-CWM-MIB", "cwmAssociatedDegree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmGroup = cwmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-CWM-MIB", cwmMoId=cwmMoId, cwmAssociatedDegree=cwmAssociatedDegree, cwmConformance=cwmConformance, cwmMIB=cwmMIB, cwmGroups=cwmGroups, cwmEntry=cwmEntry, cwmProvEqptType=cwmProvEqptType, cwmTable=cwmTable, cwmCompliance=cwmCompliance, cwmGroup=cwmGroup, PYSNMP_MODULE_ID=cwmMIB, cwmCompliances=cwmCompliances)
