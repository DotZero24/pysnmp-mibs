#
# PySNMP MIB module INFINERA-ENTITY-LMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-LMM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
lmmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41))
if mibBuilder.loadTexts: lmmMIB.setLastUpdated('201501080000Z')
if mibBuilder.loadTexts: lmmMIB.setOrganization('INFINERA')
lmmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3))
lmmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 1))
lmmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 2))
lmmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1), )
if mibBuilder.loadTexts: lmmTable.setStatus('current')
lmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: lmmEntry.setStatus('current')
lmmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lmmMoId.setStatus('current')
lmmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lmmProvEqptType.setStatus('current')
lmmProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lmmProvSerialNumber.setStatus('current')
lmmAssociatedDegree = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lmmAssociatedDegree.setStatus('current')
lmmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 1, 1)).setObjects(("INFINERA-ENTITY-LMM-MIB", "lmmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lmmCompliance = lmmCompliance.setStatus('current')
lmmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 41, 3, 2, 1)).setObjects(("INFINERA-ENTITY-LMM-MIB", "lmmMoId"), ("INFINERA-ENTITY-LMM-MIB", "lmmProvEqptType"), ("INFINERA-ENTITY-LMM-MIB", "lmmProvSerialNumber"), ("INFINERA-ENTITY-LMM-MIB", "lmmAssociatedDegree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lmmGroup = lmmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-LMM-MIB", lmmMoId=lmmMoId, lmmProvSerialNumber=lmmProvSerialNumber, lmmCompliance=lmmCompliance, lmmGroup=lmmGroup, PYSNMP_MODULE_ID=lmmMIB, lmmConformance=lmmConformance, lmmCompliances=lmmCompliances, lmmProvEqptType=lmmProvEqptType, lmmGroups=lmmGroups, lmmAssociatedDegree=lmmAssociatedDegree, lmmTable=lmmTable, lmmEntry=lmmEntry, lmmMIB=lmmMIB)
