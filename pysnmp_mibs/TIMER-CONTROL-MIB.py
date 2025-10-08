#
# PySNMP MIB module TIMER-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/TIMER-CONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ng700smartswitch, = mibBuilder.importSymbols("NETGEAR-REF-MIB", "ng700smartswitch")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
timerControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 11, 1025))
timerControl.setRevisions(('2009-12-02 00:00',))
if mibBuilder.loadTexts: timerControl.setLastUpdated('200912020000Z')
if mibBuilder.loadTexts: timerControl.setOrganization('Netgear')
class TimeHoursMinutes(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class DateYearMonthDay(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

timerCtrlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1))
timerCtrlModeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 1))
timerCtrlGlobalMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timerCtrlGlobalMode.setStatus('current')
timerCtrlSchdlTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2), )
if mibBuilder.loadTexts: timerCtrlSchdlTable.setStatus('current')
timerCtrlSchdlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1), ).setIndexNames((0, "TIMER-CONTROL-MIB", "timerCtrlSchdlIndex"))
if mibBuilder.loadTexts: timerCtrlSchdlEntry.setStatus('current')
timerCtrlSchdlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)))
if mibBuilder.loadTexts: timerCtrlSchdlIndex.setStatus('current')
timerCtrlSchdlName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlName.setStatus('current')
timerCtrlSchdlRecurring = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("invalid", 0), ("daily", 1), ("weekly", 2), ("monthly", 3), ("yearly", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlRecurring.setStatus('current')
timerCtrlSchdlMonthFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlMonthFreq.setStatus('current')
timerCtrlSchdlWeekDay = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlWeekDay.setStatus('current')
timerCtrlSchdlMonthDayAcc = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 37))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlMonthDayAcc.setStatus('current')
timerCtrlSchdlTimeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 7), TimeHoursMinutes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlTimeStart.setStatus('current')
timerCtrlSchdlTimeStop = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 8), TimeHoursMinutes()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlTimeStop.setStatus('current')
timerCtrlSchdlDateStart = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 9), DateYearMonthDay()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlDateStart.setStatus('current')
timerCtrlSchdlDateStop = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 10), DateYearMonthDay()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlDateStop.setStatus('current')
timerCtrlSchdlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timerCtrlSchdlRowStatus.setStatus('current')
timerCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 3)).setObjects(("TIMER-CONTROL-MIB", "timerCtrlGlobalMode"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlName"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlRecurring"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlMonthFreq"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlWeekDay"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlMonthDayAcc"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlTimeStart"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlTimeStop"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlDateStart"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlDateStop"), ("TIMER-CONTROL-MIB", "timerCtrlSchdlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    timerCtrlGroup = timerCtrlGroup.setStatus('current')
mibBuilder.exportSymbols("TIMER-CONTROL-MIB", timerCtrlSchdlDateStart=timerCtrlSchdlDateStart, timerCtrlSchdlName=timerCtrlSchdlName, timerCtrlSchdlWeekDay=timerCtrlSchdlWeekDay, timerCtrlGlobalMode=timerCtrlGlobalMode, timerControl=timerControl, PYSNMP_MODULE_ID=timerControl, timerCtrlSchdlTimeStart=timerCtrlSchdlTimeStart, timerCtrlSchdlMonthDayAcc=timerCtrlSchdlMonthDayAcc, timerCtrlSchdlRowStatus=timerCtrlSchdlRowStatus, timerCtrlGroup=timerCtrlGroup, DateYearMonthDay=DateYearMonthDay, timerCtrlSchdlIndex=timerCtrlSchdlIndex, timerCtrlSchdlDateStop=timerCtrlSchdlDateStop, timerCtrlObjects=timerCtrlObjects, timerCtrlSchdlTimeStop=timerCtrlSchdlTimeStop, timerCtrlSchdlEntry=timerCtrlSchdlEntry, timerCtrlSchdlTable=timerCtrlSchdlTable, timerCtrlModeGroup=timerCtrlModeGroup, timerCtrlSchdlRecurring=timerCtrlSchdlRecurring, TimeHoursMinutes=TimeHoursMinutes, timerCtrlSchdlMonthFreq=timerCtrlSchdlMonthFreq)
