#
# PySNMP MIB module INFINERA-ENTITY-LMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-LMM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-LMM-MIB", lmmCompliance=lmmCompliance, lmmEntry=lmmEntry, lmmMoId=lmmMoId, lmmAssociatedDegree=lmmAssociatedDegree, PYSNMP_MODULE_ID=lmmMIB, lmmGroup=lmmGroup, lmmProvSerialNumber=lmmProvSerialNumber, lmmCompliances=lmmCompliances, lmmProvEqptType=lmmProvEqptType, lmmTable=lmmTable, lmmGroups=lmmGroups, lmmMIB=lmmMIB, lmmConformance=lmmConformance)
