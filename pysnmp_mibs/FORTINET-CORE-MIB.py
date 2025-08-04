#
# PySNMP MIB module FORTINET-CORE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fortinet/FORTINET-CORE-MIB
# Produced by pysmi-1.1.12 at Mon Aug  4 16:48:03 2025
# On host macmini.vegmond.io platform Darwin version 24.5.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAddressPrefixLength")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Integer32, enterprises, Gauge32, ModuleIdentity, TimeTicks, NotificationType, Counter32, Bits, IpAddress, iso, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Integer32", "enterprises", "Gauge32", "ModuleIdentity", "TimeTicks", "NotificationType", "Counter32", "Bits", "IpAddress", "iso", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fortinet = ModuleIdentity((1, 3, 6, 1, 4, 1, 12356))
fortinet.setRevisions(('2021-11-15 00:00', '2020-01-30 00:00', '2018-12-05 00:00', '2018-11-05 00:00', '2016-09-30 00:00', '2016-05-24 00:00', '2015-01-14 00:00', '2014-12-10 00:00', '2014-04-10 00:00', '2014-03-22 00:00', '2012-05-09 00:00', '2012-04-23 00:00', '2011-12-23 00:00', '2011-04-25 00:00', '2010-05-14 00:00', '2009-05-20 00:00', '2008-11-19 00:00', '2008-10-21 00:00', '2008-06-25 00:00', '2008-06-16 00:00', '2008-04-17 00:00',))
if mibBuilder.loadTexts: fortinet.setLastUpdated('202111150000Z')
if mibBuilder.loadTexts: fortinet.setOrganization('Fortinet Technologies, Inc.')
class FnBoolState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class FnLanguage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("english", 1), ("simplifiedChinese", 2), ("japanese", 3), ("korean", 4), ("spanish", 5), ("traditionalChinese", 6), ("french", 7), ("portuguese", 8), ("undefined", 255))

class FnIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FnSessionProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 41, 46, 47, 50, 51, 89, 103, 108, 255))
    namedValues = NamedValues(("ip", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("ipv6", 41), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("ospf", 89), ("pim", 103), ("comp", 108), ("raw", 255))

fnCoreMib = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100))
fnCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1))
fnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 1))
fnSysSerial = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnSysSerial.setStatus('current')
fnMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2))
fnMgmtLanguage = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 1), FnLanguage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnMgmtLanguage.setStatus('current')
fnAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100))
fnAdminNumber = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminNumber.setStatus('current')
fnAdminTable = MibTable((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2), )
if mibBuilder.loadTexts: fnAdminTable.setStatus('current')
fnAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1), ).setIndexNames((0, "FORTINET-CORE-MIB", "fnAdminIndex"))
if mibBuilder.loadTexts: fnAdminEntry.setStatus('current')
fnAdminIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fnAdminIndex.setStatus('current')
fnAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminName.setStatus('current')
fnAdminAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminAddrType.setStatus('current')
fnAdminAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminAddr.setStatus('current')
fnAdminMask = MibTableColumn((1, 3, 6, 1, 4, 1, 12356, 100, 1, 2, 100, 2, 1, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fnAdminMask.setStatus('current')
fnTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3))
fnTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0))
fnTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1))
fnGenTrapMsg = MibScalar((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fnGenTrapMsg.setStatus('current')
fnTrapCpuThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 101)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapCpuThreshold.setStatus('current')
fnTrapMemThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 102)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapMemThreshold.setStatus('current')
fnTrapLogDiskThreshold = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 103)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapLogDiskThreshold.setStatus('current')
fnTrapTempHigh = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 104)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapTempHigh.setStatus('current')
fnTrapVoltageOutOfRange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 105)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapVoltageOutOfRange.setStatus('current')
fnTrapPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 106)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapPowerSupplyFailure.setStatus('current')
fnTrapAmcIfBypassMode = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 107)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapAmcIfBypassMode.setStatus('current')
fnTrapFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 108)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapFanFailure.setStatus('current')
fnTrapIfEnterBypassMode = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 109)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapIfEnterBypassMode.setStatus('current')
fnTrapIfExitBypassMode = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 110)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapIfExitBypassMode.setStatus('current')
fnTrapIpChange = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 201)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: fnTrapIpChange.setStatus('current')
fnTrapTest = NotificationType((1, 3, 6, 1, 4, 1, 12356, 100, 1, 3, 0, 999)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: fnTrapTest.setStatus('current')
fnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12356, 100, 10))
fnSystemComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 1)).setObjects(("FORTINET-CORE-MIB", "fnSysSerial"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnSystemComplianceGroup = fnSystemComplianceGroup.setStatus('current')
fnMgmtComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 2)).setObjects(("FORTINET-CORE-MIB", "fnMgmtLanguage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnMgmtComplianceGroup = fnMgmtComplianceGroup.setStatus('current')
fnAdminComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 3)).setObjects(("FORTINET-CORE-MIB", "fnAdminNumber"), ("FORTINET-CORE-MIB", "fnAdminName"), ("FORTINET-CORE-MIB", "fnAdminAddrType"), ("FORTINET-CORE-MIB", "fnAdminAddr"), ("FORTINET-CORE-MIB", "fnAdminMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnAdminComplianceGroup = fnAdminComplianceGroup.setStatus('current')
fnTrapsComplianceGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 4)).setObjects(("FORTINET-CORE-MIB", "fnTrapCpuThreshold"), ("FORTINET-CORE-MIB", "fnTrapMemThreshold"), ("FORTINET-CORE-MIB", "fnTrapLogDiskThreshold"), ("FORTINET-CORE-MIB", "fnTrapTempHigh"), ("FORTINET-CORE-MIB", "fnTrapVoltageOutOfRange"), ("FORTINET-CORE-MIB", "fnTrapPowerSupplyFailure"), ("FORTINET-CORE-MIB", "fnTrapAmcIfBypassMode"), ("FORTINET-CORE-MIB", "fnTrapIfEnterBypassMode"), ("FORTINET-CORE-MIB", "fnTrapIfExitBypassMode"), ("FORTINET-CORE-MIB", "fnTrapFanFailure"), ("FORTINET-CORE-MIB", "fnTrapIpChange"), ("FORTINET-CORE-MIB", "fnTrapTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnTrapsComplianceGroup = fnTrapsComplianceGroup.setStatus('current')
fnNotifObjectsComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12356, 100, 10, 5)).setObjects(("FORTINET-CORE-MIB", "fnGenTrapMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnNotifObjectsComplianceGroup = fnNotifObjectsComplianceGroup.setStatus('current')
fnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12356, 100, 10, 100)).setObjects(("FORTINET-CORE-MIB", "fnSystemComplianceGroup"), ("FORTINET-CORE-MIB", "fnMgmtComplianceGroup"), ("FORTINET-CORE-MIB", "fnAdminComplianceGroup"), ("FORTINET-CORE-MIB", "fnTrapsComplianceGroup"), ("FORTINET-CORE-MIB", "fnNotifObjectsComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fnMIBCompliance = fnMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("FORTINET-CORE-MIB", fnAdminTable=fnAdminTable, fnAdmin=fnAdmin, fnNotifObjectsComplianceGroup=fnNotifObjectsComplianceGroup, fnAdminName=fnAdminName, fnTrapIfExitBypassMode=fnTrapIfExitBypassMode, fnMgmtLanguage=fnMgmtLanguage, FnIndex=FnIndex, fnMgmtComplianceGroup=fnMgmtComplianceGroup, fnSysSerial=fnSysSerial, fnTrapAmcIfBypassMode=fnTrapAmcIfBypassMode, fnTrapMemThreshold=fnTrapMemThreshold, fnAdminAddr=fnAdminAddr, fnMIBConformance=fnMIBConformance, fnCommon=fnCommon, fortinet=fortinet, PYSNMP_MODULE_ID=fortinet, fnSystemComplianceGroup=fnSystemComplianceGroup, fnSystem=fnSystem, fnTrapsComplianceGroup=fnTrapsComplianceGroup, fnTrapIfEnterBypassMode=fnTrapIfEnterBypassMode, fnTrapsPrefix=fnTrapsPrefix, fnAdminEntry=fnAdminEntry, fnGenTrapMsg=fnGenTrapMsg, FnLanguage=FnLanguage, fnTrapCpuThreshold=fnTrapCpuThreshold, fnTrapObjects=fnTrapObjects, fnMgmt=fnMgmt, fnTrapIpChange=fnTrapIpChange, fnAdminNumber=fnAdminNumber, fnCoreMib=fnCoreMib, fnTraps=fnTraps, fnAdminComplianceGroup=fnAdminComplianceGroup, FnSessionProto=FnSessionProto, fnMIBCompliance=fnMIBCompliance, fnTrapLogDiskThreshold=fnTrapLogDiskThreshold, FnBoolState=FnBoolState, fnAdminAddrType=fnAdminAddrType, fnTrapPowerSupplyFailure=fnTrapPowerSupplyFailure, fnTrapTest=fnTrapTest, fnTrapVoltageOutOfRange=fnTrapVoltageOutOfRange, fnAdminIndex=fnAdminIndex, fnTrapFanFailure=fnTrapFanFailure, fnTrapTempHigh=fnTrapTempHigh, fnAdminMask=fnAdminMask)
