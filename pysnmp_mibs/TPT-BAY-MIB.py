#
# PySNMP MIB module TPT-BAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-BAY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, tpt_tpa_unkparams, tpt_tpa_eventsV2 = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs", "tpt-tpa-unkparams", "tpt-tpa-eventsV2")
tpt_slot_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17)).setLabel("tpt-slot-objs")
tpt_slot_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_slot_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_slot_objs.setOrganization('Trend Micro, Inc.')
class SlotStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("empty", 0), ("active", 1), ("error", 2))

class SlotEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("insert", 0), ("remove", 1))

class SlotModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("type-12-port-1g-copper", 1), ("type-12-port-1g-sfp", 2), ("type-8-port-10g-sfp", 3), ("type-2-port-40g-sfp", 4), ("type-6100", 5), ("type-5100", 6), ("type-2500", 7), ("type-1400", 8), ("type-660", 9), ("type-330", 10), ("type-110", 11), ("type-10", 12), ("type-empty", 13), ("type-8-port-1g-copper-bypass", 14), ("type-4-port-1g-sfp-sr-bypass", 15), ("type-4-port-1g-sfp-lr-bypass", 16), ("type-4-port-10g-sfp-sr-bypass", 17), ("type-4-port-10g-sfp-lr-bypass", 18))

slotTempTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1), )
if mibBuilder.loadTexts: slotTempTable.setStatus('current')
slotTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1), ).setIndexNames((0, "TPT-BAY-MIB", "slotTempIndex"))
if mibBuilder.loadTexts: slotTempEntry.setStatus('current')
slotTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: slotTempIndex.setStatus('current')
slotName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotName.setStatus('current')
slotModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleName.setStatus('current')
slotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 4), SlotStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotStatus.setStatus('current')
slotModuleSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleSerialNum.setStatus('current')
slotModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 6), SlotModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleType.setStatus('current')
tptSlotDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 281), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotDeviceID.setStatus('current')
tptSlotID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 282), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotID.setStatus('current')
tptSlotEvent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 283), SlotEvent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptSlotEvent.setStatus('current')
tptSlotChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 54)).setObjects(("TPT-BAY-MIB", "tptSlotDeviceID"), ("TPT-BAY-MIB", "tptSlotID"), ("TPT-BAY-MIB", "tptSlotEvent"))
if mibBuilder.loadTexts: tptSlotChangeNotify.setStatus('current')
mibBuilder.exportSymbols("TPT-BAY-MIB", slotModuleType=slotModuleType, SlotEvent=SlotEvent, slotTempEntry=slotTempEntry, slotTempIndex=slotTempIndex, slotTempTable=slotTempTable, slotName=slotName, slotModuleName=slotModuleName, tptSlotChangeNotify=tptSlotChangeNotify, SlotModuleType=SlotModuleType, tptSlotDeviceID=tptSlotDeviceID, slotStatus=slotStatus, tptSlotEvent=tptSlotEvent, SlotStatus=SlotStatus, tpt_slot_objs=tpt_slot_objs, slotModuleSerialNum=slotModuleSerialNum, PYSNMP_MODULE_ID=tpt_slot_objs, tptSlotID=tptSlotID)
