#
# PySNMP MIB module RAD-RadVdsl2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rad/RAD-RadVdsl2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifAlias, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifAlias", "ifIndex")
alarmEventLogAlarmOrEventId, alarmEventLogDescription, alarmEventLogSeverity, alarmEventReason, alarmEventLogDateAndTime, alarmEventLogSourceName = mibBuilder.importSymbols("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId", "alarmEventLogDescription", "alarmEventLogSeverity", "alarmEventReason", "alarmEventLogDateAndTime", "alarmEventLogSourceName")
diverseIfWanGen, = mibBuilder.importSymbols("RAD-SMI-MIB", "diverseIfWanGen")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RAD-RadVdsl2-MIB", vdsl2LinkDown=vdsl2LinkDown, vdsl2If=vdsl2If, vdsl2IfNotifVarbindTable=vdsl2IfNotifVarbindTable, vdsl2Objects=vdsl2Objects, vdsl2Events=vdsl2Events, vdsl2SideIdx=vdsl2SideIdx, vdsl2LinkDownReason=vdsl2LinkDownReason, PYSNMP_MODULE_ID=vdsl2If, vdsl2IfNotifVarbindEntry=vdsl2IfNotifVarbindEntry)
