#
# PySNMP MIB module QTECH-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-NTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
qtechNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49))
qtechNtpMIB.setRevisions(('2009-05-14 00:00',))
if mibBuilder.loadTexts: qtechNtpMIB.setLastUpdated('200905140000Z')
if mibBuilder.loadTexts: qtechNtpMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1))
qtechNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2))
qtechntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1))
qtechNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 1))
qtechNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 2))
class NTPTimeStamp(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

qtechntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechntpSysLeap.setStatus('current')
qtechntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechntpSysStratum.setStatus('current')
qtechntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-24, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechntpSysPrecision.setStatus('current')
qtechntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 4), NTPSignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechntpSysRootDelay.setStatus('current')
qtechntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 5), NTPUnsignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechntpSysRootDispersion.setStatus('current')
qtechntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechntpSysRefId.setStatus('current')
qtechntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechntpSysRefTime.setStatus('current')
qtechNTPServerIPAdd = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechNTPServerIPAdd.setStatus('current')
qtechTimeAfterNTPCal = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechTimeAfterNTPCal.setStatus('current')
qtechTimeSyncPeriod = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8640000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechTimeSyncPeriod.setStatus('current')
qtechNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11), )
if mibBuilder.loadTexts: qtechNtpServerTable.setStatus('current')
qtechNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1), ).setIndexNames((0, "QTECH-NTP-MIB", "qtechNtpServerNetType"), (0, "QTECH-NTP-MIB", "qtechNtpServerNetAddr"))
if mibBuilder.loadTexts: qtechNtpServerEntry.setStatus('current')
qtechNtpServerNetType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechNtpServerNetType.setStatus('current')
qtechNtpServerNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechNtpServerNetAddr.setStatus('current')
qtechNtpServerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2), ("version3", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechNtpServerVersion.setStatus('current')
qtechNtpServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechNtpServerStatus.setStatus('current')
qtechNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 2, 1)).setObjects(("QTECH-NTP-MIB", "qtechntpSysLeap"), ("QTECH-NTP-MIB", "qtechntpSysStratum"), ("QTECH-NTP-MIB", "qtechntpSysPrecision"), ("QTECH-NTP-MIB", "qtechntpSysRootDelay"), ("QTECH-NTP-MIB", "qtechntpSysRootDispersion"), ("QTECH-NTP-MIB", "qtechntpSysRefId"), ("QTECH-NTP-MIB", "qtechntpSysRefTime"), ("QTECH-NTP-MIB", "qtechNTPServerIPAdd"), ("QTECH-NTP-MIB", "qtechTimeAfterNTPCal"), ("QTECH-NTP-MIB", "qtechTimeSyncPeriod"), ("QTECH-NTP-MIB", "qtechNtpServerNetType"), ("QTECH-NTP-MIB", "qtechNtpServerNetAddr"), ("QTECH-NTP-MIB", "qtechNtpServerVersion"), ("QTECH-NTP-MIB", "qtechNtpServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNtpSysGroup = qtechNtpSysGroup.setStatus('current')
qtechNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 1, 1)).setObjects(("QTECH-NTP-MIB", "qtechNtpMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNtpMIBCompliance = qtechNtpMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("QTECH-NTP-MIB", qtechNtpServerTable=qtechNtpServerTable, NTPSignedTimeValue=NTPSignedTimeValue, qtechNTPServerIPAdd=qtechNTPServerIPAdd, qtechNtpServerEntry=qtechNtpServerEntry, qtechNtpMIBGroups=qtechNtpMIBGroups, qtechntpSysLeap=qtechntpSysLeap, qtechNtpServerNetType=qtechNtpServerNetType, NTPLeapIndicator=NTPLeapIndicator, qtechNtpSysGroup=qtechNtpSysGroup, qtechNtpServerVersion=qtechNtpServerVersion, qtechNtpServerNetAddr=qtechNtpServerNetAddr, NTPUnsignedTimeValue=NTPUnsignedTimeValue, qtechntpSysRootDispersion=qtechntpSysRootDispersion, qtechTimeAfterNTPCal=qtechTimeAfterNTPCal, NTPStratum=NTPStratum, qtechntpSysRefTime=qtechntpSysRefTime, qtechntpSysStratum=qtechntpSysStratum, qtechTimeSyncPeriod=qtechTimeSyncPeriod, qtechntpSysRefId=qtechntpSysRefId, qtechNtpMIBObjects=qtechNtpMIBObjects, qtechntpSysPrecision=qtechntpSysPrecision, qtechNtpMIBCompliances=qtechNtpMIBCompliances, NTPRefId=NTPRefId, qtechNtpMIB=qtechNtpMIB, NTPTimeStamp=NTPTimeStamp, qtechNtpMIBCompliance=qtechNtpMIBCompliance, qtechntpSysRootDelay=qtechntpSysRootDelay, qtechNtpMIBConformance=qtechNtpMIBConformance, PYSNMP_MODULE_ID=qtechNtpMIB, qtechNtpServerStatus=qtechNtpServerStatus, qtechntpSystem=qtechntpSystem)
