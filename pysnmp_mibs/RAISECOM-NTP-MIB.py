#
# PySNMP MIB module RAISECOM-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/RAISECOM-NTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
rcNtp = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44))
rcNtp.setRevisions(('2009-02-09 00:00',))
if mibBuilder.loadTexts: rcNtp.setLastUpdated('200902090000Z')
if mibBuilder.loadTexts: rcNtp.setOrganization('Raisecom Technology Co., Ltd.')
rcNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1))
rcNtpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1))
rcNtpPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2))
rcNtpFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.1"
    status = 'current'
    displayHint = '4d.4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol(Version 3)', RFC-1305, March 1992, Section 3.2.1"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 3.2.1"
    status = 'current'
    displayHint = '2d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 3.2.1"
    status = 'current'
    displayHint = '2d.2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 2.2"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(TextualConvention, OctetString):
    reference = "D.L. Mills, Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.1"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPPollInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-20, 20)

class NTPAssocIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

rcNtpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysLeap.setStatus('current')
rcNtpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcNtpSysStratum.setStatus('current')
rcNtpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysPrecision.setStatus('current')
rcNtpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 4), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysRootDelay.setStatus('current')
rcNtpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 5), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysRootDispersion.setStatus('current')
rcNtpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 6), NTPRefId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcNtpSysRefId.setStatus('current')
rcNtpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysRefTime.setStatus('current')
rcNtpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 8), NTPPollInterval().subtype(subtypeSpec=ValueRangeConstraint(6, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcNtpSysPoll.setStatus('current')
rcNtpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 9), NTPAssocIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysPeer.setStatus('current')
rcNtpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 10), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysClock.setStatus('current')
rcNtpSysClockStatus = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("setByNone", 1), ("setByManual", 2), ("setByTimeProtocol", 3))).clone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysClockStatus.setStatus('current')
rcNtpSysVersion = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2), ("v3", 3))).clone('v3')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcNtpSysVersion.setStatus('deprecated')
rcNtpSysMode = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ntpMaster", 1), ("ntpSlave", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcNtpSysMode.setStatus('current')
rcNtpSysValidServicerIndex = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpSysValidServicerIndex.setStatus('current')
rcNtpPeersVarTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1), )
if mibBuilder.loadTexts: rcNtpPeersVarTable.setStatus('current')
rcNtpPeersVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1), ).setIndexNames((0, "RAISECOM-NTP-MIB", "rcNtpPeersAssocId"))
if mibBuilder.loadTexts: rcNtpPeersVarEntry.setStatus('current')
rcNtpPeersAssocId = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 1), NTPAssocIdentifier())
if mibBuilder.loadTexts: rcNtpPeersAssocId.setStatus('current')
rcNtpPeersConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersConfigured.setStatus('current')
rcNtpPeersPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcNtpPeersPeerAddress.setStatus('current')
rcNtpPeersPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersPeerPort.setStatus('current')
rcNtpPeersHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcNtpPeersHostAddress.setStatus('current')
rcNtpPeersHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersHostPort.setStatus('current')
rcNtpPeersLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 7), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersLeap.setStatus('current')
rcNtpPeersMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcNtpPeersMode.setStatus('current')
rcNtpPeersStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 9), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersStratum.setStatus('current')
rcNtpPeersPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 10), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersPeerPoll.setStatus('current')
rcNtpPeersHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 11), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersHostPoll.setStatus('current')
rcNtpPeersPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersPrecision.setStatus('current')
rcNtpPeersRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 13), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersRootDelay.setStatus('current')
rcNtpPeersRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 14), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersRootDispersion.setStatus('current')
rcNtpPeersRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 15), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersRefId.setStatus('current')
rcNtpPeersRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 16), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersRefTime.setStatus('current')
rcNtpPeersOrgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 17), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersOrgTime.setStatus('current')
rcNtpPeersReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 18), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersReceiveTime.setStatus('current')
rcNtpPeersTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 19), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersTransmitTime.setStatus('current')
rcNtpPeersUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersUpdateTime.setStatus('current')
rcNtpPeersReach = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersReach.setStatus('current')
rcNtpPeersTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersTimer.setStatus('current')
rcNtpPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 23), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersOffset.setStatus('current')
rcNtpPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 24), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersDelay.setStatus('current')
rcNtpPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 25), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersDispersion.setStatus('current')
rcNtpPeersFilterValidEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 26), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpPeersFilterValidEntries.setStatus('current')
rcNtpPeersEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcNtpPeersEntryStatus.setStatus('current')
rcNtpPeersVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 2, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2), ("v3", 3))).clone('v3')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcNtpPeersVersion.setStatus('current')
rcNtpFilterRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3, 1), )
if mibBuilder.loadTexts: rcNtpFilterRegisterTable.setStatus('current')
rcNtpFilterRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3, 1, 1), ).setIndexNames((0, "RAISECOM-NTP-MIB", "rcNtpPeersAssocId"), (0, "RAISECOM-NTP-MIB", "rcNtpFilterIndex"))
if mibBuilder.loadTexts: rcNtpFilterRegisterEntry.setStatus('current')
rcNtpFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: rcNtpFilterIndex.setStatus('current')
rcNtpFilterPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3, 1, 1, 2), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpFilterPeersOffset.setStatus('current')
rcNtpFilterPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3, 1, 1, 3), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpFilterPeersDelay.setStatus('current')
rcNtpFilterPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 44, 1, 3, 1, 1, 4), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rcNtpFilterPeersDispersion.setStatus('current')
mibBuilder.exportSymbols("RAISECOM-NTP-MIB", rcNtpPeersRootDelay=rcNtpPeersRootDelay, NTPSignedTimeValue=NTPSignedTimeValue, rcNtpPeersPeerAddress=rcNtpPeersPeerAddress, rcNtpPeersMode=rcNtpPeersMode, rcNtpPeersRefTime=rcNtpPeersRefTime, rcNtp=rcNtp, rcNtpPeersHostAddress=rcNtpPeersHostAddress, rcNtpSysPeer=rcNtpSysPeer, rcNtpPeersPeerPort=rcNtpPeersPeerPort, PYSNMP_MODULE_ID=rcNtp, rcNtpPeersUpdateTime=rcNtpPeersUpdateTime, rcNtpSystem=rcNtpSystem, rcNtpPeersOrgTime=rcNtpPeersOrgTime, rcNtpFilterIndex=rcNtpFilterIndex, rcNtpFilterPeersDelay=rcNtpFilterPeersDelay, rcNtpSysRefTime=rcNtpSysRefTime, NTPLeapIndicator=NTPLeapIndicator, rcNtpPeersAssocId=rcNtpPeersAssocId, rcNtpSysClockStatus=rcNtpSysClockStatus, rcNtpMIBObjects=rcNtpMIBObjects, rcNtpPeersTimer=rcNtpPeersTimer, rcNtpPeersDispersion=rcNtpPeersDispersion, NTPUnsignedTimeValue=NTPUnsignedTimeValue, rcNtpFilterRegisterEntry=rcNtpFilterRegisterEntry, rcNtpPeersPrecision=rcNtpPeersPrecision, rcNtpPeersVersion=rcNtpPeersVersion, NTPStratum=NTPStratum, rcNtpSysMode=rcNtpSysMode, rcNtpSysLeap=rcNtpSysLeap, rcNtpPeersVarEntry=rcNtpPeersVarEntry, rcNtpSysValidServicerIndex=rcNtpSysValidServicerIndex, rcNtpPeersStratum=rcNtpPeersStratum, rcNtpPeersRootDispersion=rcNtpPeersRootDispersion, rcNtpPeersEntryStatus=rcNtpPeersEntryStatus, rcNtpPeersPeerPoll=rcNtpPeersPeerPoll, rcNtpPeersLeap=rcNtpPeersLeap, rcNtpSysRootDelay=rcNtpSysRootDelay, rcNtpPeersTransmitTime=rcNtpPeersTransmitTime, rcNtpSysClock=rcNtpSysClock, rcNtpPeersVarTable=rcNtpPeersVarTable, NTPAssocIdentifier=NTPAssocIdentifier, rcNtpPeersConfigured=rcNtpPeersConfigured, rcNtpFilterPeersDispersion=rcNtpFilterPeersDispersion, rcNtpSysPoll=rcNtpSysPoll, rcNtpPeersHostPort=rcNtpPeersHostPort, rcNtpPeersReceiveTime=rcNtpPeersReceiveTime, rcNtpPeersFilterValidEntries=rcNtpPeersFilterValidEntries, rcNtpPeersRefId=rcNtpPeersRefId, rcNtpPeers=rcNtpPeers, NTPRefId=NTPRefId, rcNtpSysRefId=rcNtpSysRefId, rcNtpPeersOffset=rcNtpPeersOffset, NTPTimeStamp=NTPTimeStamp, rcNtpSysPrecision=rcNtpSysPrecision, rcNtpPeersReach=rcNtpPeersReach, rcNtpFilterPeersOffset=rcNtpFilterPeersOffset, rcNtpPeersDelay=rcNtpPeersDelay, rcNtpSysStratum=rcNtpSysStratum, rcNtpSysRootDispersion=rcNtpSysRootDispersion, rcNtpSysVersion=rcNtpSysVersion, rcNtpPeersHostPoll=rcNtpPeersHostPoll, rcNtpFilterRegisterTable=rcNtpFilterRegisterTable, NTPPollInterval=NTPPollInterval, rcNtpFilter=rcNtpFilter)
