#
# PySNMP MIB module NETGEAR-RADLAN-rlInventoryEnt-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-rlInventoryEnt-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class UnitIfindexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unit", 0), ("ifindex", 1))

rlInventoryEntTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 17, 217), )
if mibBuilder.loadTexts: rlInventoryEntTable.setStatus('current')
rlInventoryEntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1), ).setIndexNames((0, "NETGEAR-RADLAN-rlInventoryEnt-MIB", "rlInventoryEntUnitOrIfindex"), (0, "NETGEAR-RADLAN-rlInventoryEnt-MIB", "rlInventoryEntUnitIfindexID"))
if mibBuilder.loadTexts: rlInventoryEntEntry.setStatus('current')
rlInventoryEntUnitOrIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 1), UnitIfindexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setStatus('current')
rlInventoryEntUnitIfindexID = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setStatus('current')
rlInventoryEntVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntVendorID.setStatus('current')
rlInventoryEntPID = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntPID.setStatus('current')
rlInventoryEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntName.setStatus('current')
rlInventoryEntDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntDescription.setStatus('current')
rlInventoryEntSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setStatus('current')
rlInventoryEntUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 217, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-rlInventoryEnt-MIB", rlInventoryEntUnitNum=rlInventoryEntUnitNum, rlInventoryEntPID=rlInventoryEntPID, rlInventoryEntTable=rlInventoryEntTable, rlInventoryEntVendorID=rlInventoryEntVendorID, rlInventoryEntEntry=rlInventoryEntEntry, rlInventoryEntDescription=rlInventoryEntDescription, rlInventoryEntSerialNumber=rlInventoryEntSerialNumber, rlInventoryEntName=rlInventoryEntName, rlInventoryEntUnitIfindexID=rlInventoryEntUnitIfindexID, UnitIfindexType=UnitIfindexType, rlInventoryEntUnitOrIfindex=rlInventoryEntUnitOrIfindex)
