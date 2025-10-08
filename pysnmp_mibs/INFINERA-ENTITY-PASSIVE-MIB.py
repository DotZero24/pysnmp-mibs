#
# PySNMP MIB module INFINERA-ENTITY-PASSIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-PASSIVE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
commonEquipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonEquipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-PASSIVE-MIB", passiveGroups=passiveGroups, passiveCompliance=passiveCompliance, passiveConformance=passiveConformance, passiveCompliances=passiveCompliances, passiveProvSerialNumber=passiveProvSerialNumber, passiveGroup=passiveGroup, PYSNMP_MODULE_ID=passiveMIB, passiveMIB=passiveMIB, passiveMoId=passiveMoId, passiveProvEqptType=passiveProvEqptType, passiveNumSystemPorts=passiveNumSystemPorts, passiveEntry=passiveEntry, passiveNumLinePorts=passiveNumLinePorts, passiveLabel=passiveLabel, passiveTable=passiveTable)
