#
# PySNMP MIB module FS-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-NTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fsNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49))
fsNtpMIB.setRevisions(('2009-05-14 00:00',))
if mibBuilder.loadTexts: fsNtpMIB.setLastUpdated('200905140000Z')
if mibBuilder.loadTexts: fsNtpMIB.setOrganization('FS.COM Inc..')
fsNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1))
fsNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2))
fsntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1))
fsNtpMIBTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 2))
fsNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 1))
fsNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 2))
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

fsntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsntpSysLeap.setStatus('current')
fsntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsntpSysStratum.setStatus('current')
fsntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-24, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsntpSysPrecision.setStatus('current')
fsntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 4), NTPSignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsntpSysRootDelay.setStatus('current')
fsntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 5), NTPUnsignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsntpSysRootDispersion.setStatus('current')
fsntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsntpSysRefId.setStatus('current')
fsntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsntpSysRefTime.setStatus('current')
fsNTPServerIPAdd = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsNTPServerIPAdd.setStatus('current')
fsTimeAfterNTPCal = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsTimeAfterNTPCal.setStatus('current')
fsTimeSyncPeriod = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8640000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsTimeSyncPeriod.setStatus('current')
fsNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11), )
if mibBuilder.loadTexts: fsNtpServerTable.setStatus('current')
fsNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1), ).setIndexNames((0, "FS-NTP-MIB", "fsNtpServerNetType"), (0, "FS-NTP-MIB", "fsNtpServerNetAddr"))
if mibBuilder.loadTexts: fsNtpServerEntry.setStatus('current')
fsNtpServerNetType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsNtpServerNetType.setStatus('current')
fsNtpServerNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsNtpServerNetAddr.setStatus('current')
fsNtpServerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version1", 1), ("version2", 2), ("version3", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsNtpServerVersion.setStatus('current')
fsNtpServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsNtpServerStatus.setStatus('current')
fsntpSysState = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("unsynchronized", 0), ("synchronized", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsntpSysState.setStatus('current')
fsNtpStatussyncTrap = NotificationType((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 2, 1)).setObjects(("FS-NTP-MIB", "fsntpSysState"))
if mibBuilder.loadTexts: fsNtpStatussyncTrap.setStatus('current')
fsNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 2, 1)).setObjects(("FS-NTP-MIB", "fsntpSysLeap"), ("FS-NTP-MIB", "fsntpSysStratum"), ("FS-NTP-MIB", "fsntpSysPrecision"), ("FS-NTP-MIB", "fsntpSysRootDelay"), ("FS-NTP-MIB", "fsntpSysRootDispersion"), ("FS-NTP-MIB", "fsntpSysRefId"), ("FS-NTP-MIB", "fsntpSysRefTime"), ("FS-NTP-MIB", "fsNTPServerIPAdd"), ("FS-NTP-MIB", "fsTimeAfterNTPCal"), ("FS-NTP-MIB", "fsTimeSyncPeriod"), ("FS-NTP-MIB", "fsNtpServerNetType"), ("FS-NTP-MIB", "fsNtpServerNetAddr"), ("FS-NTP-MIB", "fsNtpServerVersion"), ("FS-NTP-MIB", "fsNtpServerStatus"), ("FS-NTP-MIB", "fsntpSysState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNtpSysGroup = fsNtpSysGroup.setStatus('current')
fsNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 1, 1)).setObjects(("FS-NTP-MIB", "fsNtpMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNtpMIBCompliance = fsNtpMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("FS-NTP-MIB", NTPTimeStamp=NTPTimeStamp, PYSNMP_MODULE_ID=fsNtpMIB, fsNtpServerEntry=fsNtpServerEntry, fsNtpMIBCompliances=fsNtpMIBCompliances, fsNtpServerNetAddr=fsNtpServerNetAddr, fsNtpStatussyncTrap=fsNtpStatussyncTrap, fsntpSysRefId=fsntpSysRefId, NTPStratum=NTPStratum, fsNtpSysGroup=fsNtpSysGroup, NTPUnsignedTimeValue=NTPUnsignedTimeValue, fsNtpMIBObjects=fsNtpMIBObjects, fsntpSysRootDispersion=fsntpSysRootDispersion, fsNTPServerIPAdd=fsNTPServerIPAdd, fsNtpMIBTrap=fsNtpMIBTrap, fsntpSysStratum=fsntpSysStratum, fsntpSysRefTime=fsntpSysRefTime, fsNtpMIBConformance=fsNtpMIBConformance, fsNtpMIB=fsNtpMIB, fsntpSystem=fsntpSystem, NTPLeapIndicator=NTPLeapIndicator, fsNtpServerNetType=fsNtpServerNetType, fsNtpServerVersion=fsNtpServerVersion, fsNtpMIBGroups=fsNtpMIBGroups, fsTimeAfterNTPCal=fsTimeAfterNTPCal, NTPSignedTimeValue=NTPSignedTimeValue, fsNtpMIBCompliance=fsNtpMIBCompliance, fsntpSysPrecision=fsntpSysPrecision, fsntpSysLeap=fsntpSysLeap, NTPRefId=NTPRefId, fsntpSysRootDelay=fsntpSysRootDelay, fsTimeSyncPeriod=fsTimeSyncPeriod, fsNtpServerTable=fsNtpServerTable, fsNtpServerStatus=fsNtpServerStatus, fsntpSysState=fsntpSysState)
