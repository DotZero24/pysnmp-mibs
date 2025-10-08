#
# PySNMP MIB module RADLAN-rlInventoryEnt-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/RADLAN-rlInventoryEnt-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class UnitIfindexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unit", 0), ("ifindex", 1))

rlInventoryEntTable = MibTable((1, 3, 6, 1, 4, 1, 89, 217), )
if mibBuilder.loadTexts: rlInventoryEntTable.setStatus('current')
rlInventoryEntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 217, 1), ).setIndexNames((0, "RADLAN-rlInventoryEnt-MIB", "rlInventoryEntUnitOrIfindex"), (0, "RADLAN-rlInventoryEnt-MIB", "rlInventoryEntUnitIfindexID"))
if mibBuilder.loadTexts: rlInventoryEntEntry.setStatus('current')
rlInventoryEntUnitOrIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 1), UnitIfindexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitOrIfindex.setStatus('current')
rlInventoryEntUnitIfindexID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitIfindexID.setStatus('current')
rlInventoryEntVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntVendorID.setStatus('current')
rlInventoryEntPID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntPID.setStatus('current')
rlInventoryEntName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntName.setStatus('current')
rlInventoryEntDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntDescription.setStatus('current')
rlInventoryEntSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntSerialNumber.setStatus('current')
rlInventoryEntUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 217, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlInventoryEntUnitNum.setStatus('current')
mibBuilder.exportSymbols("RADLAN-rlInventoryEnt-MIB", rlInventoryEntUnitIfindexID=rlInventoryEntUnitIfindexID, rlInventoryEntVendorID=rlInventoryEntVendorID, rlInventoryEntName=rlInventoryEntName, rlInventoryEntTable=rlInventoryEntTable, rlInventoryEntSerialNumber=rlInventoryEntSerialNumber, rlInventoryEntEntry=rlInventoryEntEntry, UnitIfindexType=UnitIfindexType, rlInventoryEntUnitNum=rlInventoryEntUnitNum, rlInventoryEntDescription=rlInventoryEntDescription, rlInventoryEntUnitOrIfindex=rlInventoryEntUnitOrIfindex, rlInventoryEntPID=rlInventoryEntPID)
