#
# PySNMP MIB module INFINERA-ENTITY-PASSIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-PASSIVE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
commonEquipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonEquipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
passiveMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2))
passiveMIB.setRevisions(('2017-01-08 00:00',))
if mibBuilder.loadTexts: passiveMIB.setLastUpdated('201708010000Z')
if mibBuilder.loadTexts: passiveMIB.setOrganization('INFINERA')
passiveConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3))
passiveCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 1))
passiveGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 2))
passiveTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1), )
if mibBuilder.loadTexts: passiveTable.setStatus('current')
passiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: passiveEntry.setStatus('current')
passiveMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: passiveMoId.setStatus('current')
passiveProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: passiveProvEqptType.setStatus('current')
passiveLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: passiveLabel.setStatus('current')
passiveProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: passiveProvSerialNumber.setStatus('current')
passiveNumSystemPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: passiveNumSystemPorts.setStatus('current')
passiveNumLinePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: passiveNumLinePorts.setStatus('current')
passiveCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 1, 1)).setObjects(("INFINERA-ENTITY-PASSIVE-MIB", "passiveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    passiveCompliance = passiveCompliance.setStatus('current')
passiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 9, 2, 3, 2, 1)).setObjects(("INFINERA-ENTITY-PASSIVE-MIB", "passiveMoId"), ("INFINERA-ENTITY-PASSIVE-MIB", "passiveProvEqptType"), ("INFINERA-ENTITY-PASSIVE-MIB", "passiveLabel"), ("INFINERA-ENTITY-PASSIVE-MIB", "passiveProvSerialNumber"), ("INFINERA-ENTITY-PASSIVE-MIB", "passiveNumSystemPorts"), ("INFINERA-ENTITY-PASSIVE-MIB", "passiveNumLinePorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    passiveGroup = passiveGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-PASSIVE-MIB", passiveMoId=passiveMoId, passiveProvEqptType=passiveProvEqptType, passiveProvSerialNumber=passiveProvSerialNumber, passiveEntry=passiveEntry, passiveGroups=passiveGroups, passiveMIB=passiveMIB, passiveConformance=passiveConformance, passiveLabel=passiveLabel, passiveGroup=passiveGroup, passiveNumSystemPorts=passiveNumSystemPorts, passiveNumLinePorts=passiveNumLinePorts, PYSNMP_MODULE_ID=passiveMIB, passiveTable=passiveTable, passiveCompliances=passiveCompliances, passiveCompliance=passiveCompliance)
