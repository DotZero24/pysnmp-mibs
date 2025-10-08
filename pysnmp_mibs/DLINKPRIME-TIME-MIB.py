#
# PySNMP MIB module DLINKPRIME-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-TIME-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
dlinkPrimeTimeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 23))
dlinkPrimeTimeMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeTimeMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeTimeMIB.setOrganization('D-Link Corp.')
class DlinkTimeSummerTimeValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

dpTimeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 0))
dpTimeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 1))
dpTimeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 2))
dpTimeGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 1))
dpTimeSntpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSntpEnabled.setStatus('current')
dpTimeSntpPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 99999)).clone(720)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSntpPollInterval.setStatus('current')
dpTimeClock = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2))
dpTimeManagedClock = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeManagedClock.setStatus('current')
dpTimeCurrentTimeSource = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sntp", 1), ("noTimeSource", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpTimeCurrentTimeSource.setStatus('current')
dpTimeCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpTimeCurrentTime.setStatus('current')
dpTimeSummerTime = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4))
dpTimeSummerTimeAutoSwitchMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("date", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSummerTimeAutoSwitchMode.setStatus('current')
dpTimeSummerTimeTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-779, 839))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSummerTimeTimeZone.setStatus('current')
dpTimeSummerTimeStart = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 3), DlinkTimeSummerTimeValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSummerTimeStart.setStatus('current')
dpTimeSummerTimeEnd = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 4), DlinkTimeSummerTimeValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSummerTimeEnd.setStatus('current')
dpTimeSummerTimeOffset = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(30, 30), ValueRangeConstraint(60, 60), ValueRangeConstraint(90, 90), ValueRangeConstraint(120, 120), )).clone(60)).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSummerTimeOffset.setStatus('current')
dpTimeServer = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3))
dpTimeSntpServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTimeSntpServerAddr.setStatus('current')
dpTimeSntpServerStratum = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpTimeSntpServerStratum.setStatus('current')
dpTimeSntpServerVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpTimeSntpServerVersion.setStatus('current')
dpTimeSntpServerLastReceive = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dpTimeSntpServerLastReceive.setStatus('current')
dpTimeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 1))
dpTimeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 1, 1)).setObjects(("DLINKPRIME-TIME-MIB", "dpTimeSysInfoGroup"), ("DLINKPRIME-TIME-MIB", "dpTimeClockGroup"), ("DLINKPRIME-TIME-MIB", "dpTimeSntpGroup"), ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTimeCompliance = dpTimeCompliance.setStatus('current')
dpTimeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2))
dpTimeSysInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 1)).setObjects(("DLINKPRIME-TIME-MIB", "dpTimeCurrentTimeSource"), ("DLINKPRIME-TIME-MIB", "dpTimeCurrentTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTimeSysInfoGroup = dpTimeSysInfoGroup.setStatus('current')
dpTimeClockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 2)).setObjects(("DLINKPRIME-TIME-MIB", "dpTimeManagedClock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTimeClockGroup = dpTimeClockGroup.setStatus('current')
dpTimeSntpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 3)).setObjects(("DLINKPRIME-TIME-MIB", "dpTimeSntpEnabled"), ("DLINKPRIME-TIME-MIB", "dpTimeSntpPollInterval"), ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerAddr"), ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerStratum"), ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerVersion"), ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerLastReceive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTimeSntpGroup = dpTimeSntpGroup.setStatus('current')
dpTimeSummerTimeCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 4)).setObjects(("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeAutoSwitchMode"), ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeTimeZone"), ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeStart"), ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeEnd"), ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeOffset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTimeSummerTimeCfgGroup = dpTimeSummerTimeCfgGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-TIME-MIB", dpTimeSummerTimeAutoSwitchMode=dpTimeSummerTimeAutoSwitchMode, dpTimeClock=dpTimeClock, dpTimeCurrentTime=dpTimeCurrentTime, dpTimeSntpServerVersion=dpTimeSntpServerVersion, dpTimeServer=dpTimeServer, dpTimeSntpEnabled=dpTimeSntpEnabled, dpTimeSummerTime=dpTimeSummerTime, dpTimeClockGroup=dpTimeClockGroup, dpTimeSntpServerAddr=dpTimeSntpServerAddr, dlinkPrimeTimeMIB=dlinkPrimeTimeMIB, dpTimeSummerTimeCfgGroup=dpTimeSummerTimeCfgGroup, dpTimeSummerTimeStart=dpTimeSummerTimeStart, dpTimeSntpServerStratum=dpTimeSntpServerStratum, dpTimeSntpServerLastReceive=dpTimeSntpServerLastReceive, dpTimeSysInfoGroup=dpTimeSysInfoGroup, dpTimeSummerTimeTimeZone=dpTimeSummerTimeTimeZone, PYSNMP_MODULE_ID=dlinkPrimeTimeMIB, dpTimeMIBConformance=dpTimeMIBConformance, dpTimeMIBObjects=dpTimeMIBObjects, dpTimeSummerTimeEnd=dpTimeSummerTimeEnd, dpTimeSummerTimeOffset=dpTimeSummerTimeOffset, dpTimeManagedClock=dpTimeManagedClock, dpTimeCompliances=dpTimeCompliances, dpTimeSntpGroup=dpTimeSntpGroup, dpTimeMIBNotifications=dpTimeMIBNotifications, DlinkTimeSummerTimeValue=DlinkTimeSummerTimeValue, dpTimeCompliance=dpTimeCompliance, dpTimeSntpPollInterval=dpTimeSntpPollInterval, dpTimeGroups=dpTimeGroups, dpTimeGeneral=dpTimeGeneral, dpTimeCurrentTimeSource=dpTimeCurrentTimeSource)
