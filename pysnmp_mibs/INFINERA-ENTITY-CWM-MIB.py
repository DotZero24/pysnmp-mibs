#
# PySNMP MIB module INFINERA-ENTITY-CWM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-CWM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:14 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-CWM-MIB", cwmMIB=cwmMIB, PYSNMP_MODULE_ID=cwmMIB, cwmProvEqptType=cwmProvEqptType, cwmGroup=cwmGroup, cwmCompliances=cwmCompliances, cwmConformance=cwmConformance, cwmEntry=cwmEntry, cwmGroups=cwmGroups, cwmTable=cwmTable, cwmCompliance=cwmCompliance, cwmAssociatedDegree=cwmAssociatedDegree, cwmMoId=cwmMoId)
