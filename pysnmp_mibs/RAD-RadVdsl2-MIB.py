#
# PySNMP MIB module RAD-RadVdsl2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rad/RAD-RadVdsl2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:10:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifAlias, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifAlias", "ifIndex")
alarmEventLogDescription, alarmEventReason, alarmEventLogAlarmOrEventId, alarmEventLogSeverity, alarmEventLogSourceName, alarmEventLogDateAndTime = mibBuilder.importSymbols("RAD-GEN-MIB", "alarmEventLogDescription", "alarmEventReason", "alarmEventLogAlarmOrEventId", "alarmEventLogSeverity", "alarmEventLogSourceName", "alarmEventLogDateAndTime")
diverseIfWanGen, = mibBuilder.importSymbols("RAD-SMI-MIB", "diverseIfWanGen")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vdsl2If = ModuleIdentity((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19))
if mibBuilder.loadTexts: vdsl2If.setLastUpdated('201504021753Z')
if mibBuilder.loadTexts: vdsl2If.setOrganization('RAD Data Communications Ltd.')
vdsl2Events = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 0))
vdsl2Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1))
vdsl2IfNotifVarbindTable = MibTable((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2), )
if mibBuilder.loadTexts: vdsl2IfNotifVarbindTable.setStatus('current')
vdsl2IfNotifVarbindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RAD-RadVdsl2-MIB", "vdsl2SideIdx"))
if mibBuilder.loadTexts: vdsl2IfNotifVarbindEntry.setStatus('current')
vdsl2SideIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("nearEnd", 2), ("farEnd", 3))))
if mibBuilder.loadTexts: vdsl2SideIdx.setStatus('current')
vdsl2LinkDownReason = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("lossOfFraming", 1), ("lossOfSignal", 2), ("lossOfPower", 3), ("initFailure", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vdsl2LinkDownReason.setStatus('current')
vdsl2LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 19, 0, 1)).setObjects(("RAD-GEN-MIB", "alarmEventLogSourceName"), ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"), ("RAD-GEN-MIB", "alarmEventLogDescription"), ("RAD-GEN-MIB", "alarmEventLogSeverity"), ("RAD-GEN-MIB", "alarmEventLogDateAndTime"), ("RAD-GEN-MIB", "alarmEventReason"), ("IF-MIB", "ifAlias"), ("RAD-RadVdsl2-MIB", "vdsl2LinkDownReason"))
if mibBuilder.loadTexts: vdsl2LinkDown.setStatus('current')
mibBuilder.exportSymbols("RAD-RadVdsl2-MIB", vdsl2IfNotifVarbindEntry=vdsl2IfNotifVarbindEntry, vdsl2Events=vdsl2Events, PYSNMP_MODULE_ID=vdsl2If, vdsl2If=vdsl2If, vdsl2IfNotifVarbindTable=vdsl2IfNotifVarbindTable, vdsl2LinkDownReason=vdsl2LinkDownReason, vdsl2SideIdx=vdsl2SideIdx, vdsl2LinkDown=vdsl2LinkDown, vdsl2Objects=vdsl2Objects)
