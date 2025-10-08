#
# PySNMP MIB module INFINERA-ENTITY-MPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-MPC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:59 2025
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
mpcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50))
if mibBuilder.loadTexts: mpcMIB.setLastUpdated('201501080000Z')
if mibBuilder.loadTexts: mpcMIB.setOrganization('INFINERA')
mpcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3))
mpcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 1))
mpcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 2))
mpcTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1), )
if mibBuilder.loadTexts: mpcTable.setStatus('current')
mpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: mpcEntry.setStatus('current')
mpcProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 1), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpcProvEqptType.setStatus('current')
mpcProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpcProvSerialNumber.setStatus('current')
mpcLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpcLabel.setStatus('current')
mpcConnectedPassiveEqptList = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpcConnectedPassiveEqptList.setStatus('current')
mpcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 1, 1)).setObjects(("INFINERA-ENTITY-MPC-MIB", "mpcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpcCompliance = mpcCompliance.setStatus('current')
mpcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 50, 3, 2, 1)).setObjects(("INFINERA-ENTITY-MPC-MIB", "mpcProvEqptType"), ("INFINERA-ENTITY-MPC-MIB", "mpcProvSerialNumber"), ("INFINERA-ENTITY-MPC-MIB", "mpcLabel"), ("INFINERA-ENTITY-MPC-MIB", "mpcConnectedPassiveEqptList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpcGroup = mpcGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-MPC-MIB", mpcProvEqptType=mpcProvEqptType, mpcGroup=mpcGroup, mpcTable=mpcTable, mpcLabel=mpcLabel, mpcCompliances=mpcCompliances, mpcConformance=mpcConformance, mpcEntry=mpcEntry, mpcConnectedPassiveEqptList=mpcConnectedPassiveEqptList, mpcCompliance=mpcCompliance, PYSNMP_MODULE_ID=mpcMIB, mpcProvSerialNumber=mpcProvSerialNumber, mpcGroups=mpcGroups, mpcMIB=mpcMIB)
