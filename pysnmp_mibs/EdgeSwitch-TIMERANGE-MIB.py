#
# PySNMP MIB module EdgeSwitch-TIMERANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ubiquiti/EdgeSwitch-TIMERANGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathTimeRange = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53))
fastPathTimeRange.setRevisions(('2011-01-26 00:00', '2009-09-24 00:00',))
if mibBuilder.loadTexts: fastPathTimeRange.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathTimeRange.setOrganization('Broadcom Inc')
fastPathTimeRangeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1))
class TimeRangeAbsoluteDateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TimeRangePeriodicTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class TimeRangePeriodicDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

timeRangeAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeRangeAdminMode.setStatus('current')
timeRangeIndexNextFree = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRangeIndexNextFree.setStatus('current')
timeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3), )
if mibBuilder.loadTexts: timeRangeTable.setStatus('current')
timeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1), ).setIndexNames((0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeIndex"))
if mibBuilder.loadTexts: timeRangeEntry.setStatus('current')
timeRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: timeRangeIndex.setStatus('current')
timeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeName.setStatus('current')
timeRangeOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("inactive", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRangeOperState.setStatus('current')
timeRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeStatus.setStatus('current')
timeRangeAbsoluteEntryTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4), )
if mibBuilder.loadTexts: timeRangeAbsoluteEntryTable.setStatus('current')
timeRangeAbsoluteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1), ).setIndexNames((0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeIndex"), (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeAbsoluteEntryIndex"))
if mibBuilder.loadTexts: timeRangeAbsoluteEntry.setStatus('current')
timeRangeAbsoluteEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: timeRangeAbsoluteEntryIndex.setStatus('current')
timeRangeAbsoluteStartDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 2), TimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteStartDateAndTime.setStatus('current')
timeRangeAbsoluteEndDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 3), TimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteEndDateAndTime.setStatus('current')
timeRangeAbsoluteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteStatus.setStatus('current')
timeRangePeriodicEntryTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5), )
if mibBuilder.loadTexts: timeRangePeriodicEntryTable.setStatus('current')
timeRangePeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1), ).setIndexNames((0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeIndex"), (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangePeriodicEntryIndex"))
if mibBuilder.loadTexts: timeRangePeriodicEntry.setStatus('current')
timeRangePeriodicEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: timeRangePeriodicEntryIndex.setStatus('current')
timeRangePeriodicFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicFrequency.setStatus('current')
timeRangePeriodicPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicPattern.setStatus('current')
timeRangePeriodicDayMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicDayMask.setStatus('current')
timeRangePeriodicStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 5), TimeRangePeriodicDate()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartDate.setStatus('current')
timeRangePeriodicStartDay = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 6), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartDay.setStatus('current')
timeRangePeriodicStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 7), TimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartTime.setStatus('current')
timeRangePeriodicEndDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 8), TimeRangePeriodicDate()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndDate.setStatus('current')
timeRangePeriodicEndDay = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 9), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndDay.setStatus('current')
timeRangePeriodicEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 10), TimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndTime.setStatus('current')
timeRangePeriodicStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStatus.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-TIMERANGE-MIB", fastPathTimeRange=fastPathTimeRange, timeRangePeriodicPattern=timeRangePeriodicPattern, TimeRangePeriodicTime=TimeRangePeriodicTime, timeRangePeriodicStartTime=timeRangePeriodicStartTime, timeRangePeriodicFrequency=timeRangePeriodicFrequency, timeRangeAbsoluteStartDateAndTime=timeRangeAbsoluteStartDateAndTime, timeRangePeriodicEntryIndex=timeRangePeriodicEntryIndex, timeRangeIndexNextFree=timeRangeIndexNextFree, TimeRangeAbsoluteDateAndTime=TimeRangeAbsoluteDateAndTime, timeRangePeriodicDayMask=timeRangePeriodicDayMask, timeRangeAdminMode=timeRangeAdminMode, timeRangePeriodicStatus=timeRangePeriodicStatus, timeRangePeriodicEntryTable=timeRangePeriodicEntryTable, timeRangeTable=timeRangeTable, fastPathTimeRangeGroup=fastPathTimeRangeGroup, timeRangePeriodicEndDay=timeRangePeriodicEndDay, PYSNMP_MODULE_ID=fastPathTimeRange, timeRangeAbsoluteEntryTable=timeRangeAbsoluteEntryTable, timeRangePeriodicEndTime=timeRangePeriodicEndTime, timeRangeAbsoluteEndDateAndTime=timeRangeAbsoluteEndDateAndTime, timeRangeOperState=timeRangeOperState, timeRangePeriodicStartDate=timeRangePeriodicStartDate, timeRangePeriodicEndDate=timeRangePeriodicEndDate, timeRangeAbsoluteStatus=timeRangeAbsoluteStatus, timeRangePeriodicStartDay=timeRangePeriodicStartDay, timeRangeAbsoluteEntry=timeRangeAbsoluteEntry, timeRangeEntry=timeRangeEntry, TimeRangePeriodicDate=TimeRangePeriodicDate, timeRangeName=timeRangeName, timeRangeStatus=timeRangeStatus, timeRangeAbsoluteEntryIndex=timeRangeAbsoluteEntryIndex, timeRangeIndex=timeRangeIndex, timeRangePeriodicEntry=timeRangePeriodicEntry)
