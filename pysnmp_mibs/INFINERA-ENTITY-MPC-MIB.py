#
# PySNMP MIB module INFINERA-ENTITY-MPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-MPC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:27 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-MPC-MIB", mpcProvSerialNumber=mpcProvSerialNumber, mpcGroup=mpcGroup, mpcEntry=mpcEntry, mpcConnectedPassiveEqptList=mpcConnectedPassiveEqptList, mpcCompliance=mpcCompliance, PYSNMP_MODULE_ID=mpcMIB, mpcMIB=mpcMIB, mpcTable=mpcTable, mpcProvEqptType=mpcProvEqptType, mpcLabel=mpcLabel, mpcGroups=mpcGroups, mpcConformance=mpcConformance, mpcCompliances=mpcCompliances)
