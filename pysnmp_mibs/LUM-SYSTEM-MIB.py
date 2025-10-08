#
# PySNMP MIB module LUM-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumModules, lumSystemMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumSystemMIB")
FaultStatus, OnOff, CommandString, Platform, EnableDisable = mibBuilder.importSymbols("LUM-TC", "FaultStatus", "OnOff", "CommandString", "Platform", "EnableDisable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TestAndIncr, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TestAndIncr", "DisplayString")
lumSystemMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 4))
lumSystemMIBModule.setRevisions(('2018-12-21 00:00', '2018-09-28 00:00', '2017-12-08 00:00', '2017-06-15 00:00', '2016-11-30 00:00', '2016-06-14 00:00', '2014-05-16 00:00', '2013-11-15 00:00', '2010-08-03 00:00', '2008-08-05 00:00', '2005-09-14 00:00', '2004-10-01 00:00', '2004-06-30 00:00', '2004-05-26 00:00', '2003-08-03 00:00', '2002-12-13 00:00', '2002-04-18 00:00', '2002-01-11 00:00', '2001-08-14 00:00', '2001-07-26 00:00', '2001-04-26 00:00',))
if mibBuilder.loadTexts: lumSystemMIBModule.setLastUpdated('201812210000Z')
if mibBuilder.loadTexts: lumSystemMIBModule.setOrganization('Infinera Corporation')
lumSystemConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1))
lumSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1))
lumSystemCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2))
lumSystemMinimalGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3))
lumSystemMinimalCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4))
lumSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2))
sysGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1))
sysNode = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2))
sysHostList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3))
sysTime = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4))
sysLogList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5))
sysUserList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6))
sysRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7))
sysLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8))
sysTacacs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9))
sysAudit = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 10))
sysSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11))
sysManager = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12))
sysGeneralTestAndIncr = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysGeneralTestAndIncr.setStatus('current')
sysGeneralMibSpecVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysGeneralMibSpecVersion.setStatus('current')
sysGeneralMibImplVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysGeneralMibImplVersion.setStatus('current')
sysGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysGeneralLastChangeTime.setStatus('current')
sysGeneralTest = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysGeneralTest.setStatus('deprecated')
sysGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysGeneralConfigLastChangeTime.setStatus('current')
sysGeneralLoginRecords = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysGeneralLoginRecords.setStatus('current')
sysGeneralUserTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysGeneralUserTableSize.setStatus('current')
sysGeneralWriteTest = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysGeneralWriteTest.setStatus('current')
sysNodeName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('localhost.localdomain')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeName.setStatus('current')
sysNodeContact = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeContact.setStatus('current')
sysNodeLocation = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeLocation.setStatus('current')
sysNodeObjectId = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNodeObjectId.setStatus('current')
sysNodePrimaryNameServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodePrimaryNameServer.setStatus('current')
sysNodeRunLevel = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("undefined", 0), ("halt", 1), ("single", 2), ("normal", 3), ("reboot", 4))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeRunLevel.setStatus('deprecated')
sysNodeSecondaryNameServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeSecondaryNameServer.setStatus('current')
sysNodeUptime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNodeUptime.setStatus('current')
sysNodeNeType = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeNeType.setStatus('current')
sysNodeNeUserName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeNeUserName.setStatus('current')
sysNodeNeDistinguishedName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeNeDistinguishedName.setStatus('current')
sysNodeBootTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNodeBootTime.setStatus('current')
sysNodeLocale = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('C')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeLocale.setStatus('current')
sysNodeVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNodeVersion.setStatus('current')
sysNodeCLLI = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeCLLI.setStatus('current')
sysNodeFIC = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeFIC.setStatus('current')
sysNodeTID = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNodeTID.setStatus('current')
sysNodeLatitude = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeLatitude.setStatus('current')
sysNodeLongitude = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 2, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNodeLongitude.setStatus('current')
sysHostTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1), )
if mibBuilder.loadTexts: sysHostTable.setStatus('current')
sysHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1), ).setIndexNames((0, "LUM-SYSTEM-MIB", "sysHostIndex"))
if mibBuilder.loadTexts: sysHostEntry.setStatus('current')
sysHostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHostIndex.setStatus('current')
sysHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sysHostIpAddress.setStatus('current')
sysHostNames = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sysHostNames.setStatus('current')
sysHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 3, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sysHostRowStatus.setStatus('current')
sysUserTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1), )
if mibBuilder.loadTexts: sysUserTable.setStatus('current')
sysUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1), ).setIndexNames((0, "LUM-SYSTEM-MIB", "sysUserIndex"))
if mibBuilder.loadTexts: sysUserEntry.setStatus('current')
sysUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserIndex.setStatus('current')
sysUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sysUserName.setStatus('current')
sysUserPasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('1234567890')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysUserPasswd.setStatus('deprecated')
sysUserDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserDescr.setStatus('current')
sysUserLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserLastChangeTime.setStatus('deprecated')
sysUserExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserExpireTime.setStatus('deprecated')
sysUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sysUserRowStatus.setStatus('deprecated')
sysUserProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('operator')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserProfile.setStatus('current')
sysUserUid = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserUid.setStatus('current')
sysUserChangePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 10), CommandString().clone('1234567890')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysUserChangePassword.setStatus('current')
sysUserClearPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 11), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysUserClearPassword.setStatus('current')
sysUserDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 12), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysUserDisable.setStatus('current')
sysUserEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 13), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysUserEnable.setStatus('current')
sysUserMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 6, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUserMode.setStatus('current')
sysTimeLocal = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTimeLocal.setStatus('current')
sysTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('CET')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTimeZone.setStatus('current')
sysTimePrimaryServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTimePrimaryServer.setStatus('deprecated')
sysTimeSecondaryServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTimeSecondaryServer.setStatus('deprecated')
sysTimeChangeLocalTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 5), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTimeChangeLocalTime.setStatus('current')
sysTimePrimaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 6), IpAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTimePrimaryIpAddress.setStatus('current')
sysTimeSecondaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 4, 7), IpAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysTimeSecondaryIpAddress.setStatus('current')
sysLogTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1), )
if mibBuilder.loadTexts: sysLogTable.setStatus('deprecated')
sysLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1), ).setIndexNames((0, "LUM-SYSTEM-MIB", "sysLogIndex"))
if mibBuilder.loadTexts: sysLogEntry.setStatus('deprecated')
sysLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLogIndex.setStatus('deprecated')
sysLogSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLogSelection.setStatus('deprecated')
sysLogAction = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLogAction.setStatus('deprecated')
sysLogRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 5, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLogRowStatus.setStatus('deprecated')
sysRadiusPrimaryServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusPrimaryServer.setStatus('deprecated')
sysRadiusPrimarySecret = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('1234567890')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusPrimarySecret.setStatus('current')
sysRadiusSecondaryServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusSecondaryServer.setStatus('deprecated')
sysRadiusSecondarySecret = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('1234567890')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusSecondarySecret.setStatus('current')
sysRadiusPrimaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 5), IpAddress().clone('0.0.0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusPrimaryIpAddress.setStatus('current')
sysRadiusSecondaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 6), IpAddress().clone('0.0.0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusSecondaryIpAddress.setStatus('current')
sysRadiusPrimaryPort = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1812)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusPrimaryPort.setStatus('current')
sysRadiusSecondaryPort = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1812)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusSecondaryPort.setStatus('current')
sysRadiusDefaultUserProfile = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 7, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysRadiusDefaultUserProfile.setStatus('current')
sysLicenseExpireDate = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseExpireDate.setStatus('current')
sysLicenseCustomer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseCustomer.setStatus('current')
sysLicenseExpiresSoon = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 3), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseExpiresSoon.setStatus('current')
sysLicenseExpired = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 4), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseExpired.setStatus('current')
sysLicenseExpiredCause = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("missing", 1), ("invalid", 2), ("corrupt", 3), ("expired", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseExpiredCause.setStatus('current')
sysLicenseFeatureEws = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("demo", 3), ("corrupt", 4), ("expired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseFeatureEws.setStatus('current')
sysLicenseFeatureOspf = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("demo", 3), ("corrupt", 4), ("expired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseFeatureOspf.setStatus('current')
sysLicenseFeatureSnmp = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("demo", 3), ("corrupt", 4), ("expired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseFeatureSnmp.setStatus('current')
sysLicenseFeatureGmpls = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("demo", 3), ("corrupt", 4), ("expired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseFeatureGmpls.setStatus('current')
sysLicenseFeatureRudb = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("demo", 3), ("corrupt", 4), ("expired", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseFeatureRudb.setStatus('current')
sysLicenseInstallLicenseFile = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 8, 11), CommandString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLicenseInstallLicenseFile.setStatus('current')
sysTacacsPrimaryServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTacacsPrimaryServer.setStatus('deprecated')
sysTacacsSecondaryServer = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTacacsSecondaryServer.setStatus('deprecated')
sysTacacsSecret = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('1234567890')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTacacsSecret.setStatus('current')
sysTacacsSecondarySecret = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('1234567890')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTacacsSecondarySecret.setStatus('current')
sysTacacsPrimaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 5), IpAddress().clone('0.0.0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTacacsPrimaryIpAddress.setStatus('current')
sysTacacsSecondaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 9, 6), IpAddress().clone('0.0.0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysTacacsSecondaryIpAddress.setStatus('current')
sysSecurityLocalConsoleAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("bootdisabled", 3))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityLocalConsoleAccess.setStatus('current')
sysSecurityChangeLocalConsoleAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 2), CommandString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityChangeLocalConsoleAccess.setStatus('current')
sysSecurityIpTablesStatus = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unavailable", 1), ("unsecure", 2), ("secure", 3))).clone('unavailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityIpTablesStatus.setStatus('current')
sysSecurityLocalCraftAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 4), EnableDisable().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysSecurityLocalCraftAccess.setStatus('current')
sysSecurityChangeLocalCraftAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 5), CommandString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityChangeLocalCraftAccess.setStatus('current')
sysSecurityAuthenticationOrder = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("localFirst", 1), ("remoteFirst", 2), ("strictRemoteFirst", 3))).clone('strictRemoteFirst')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityAuthenticationOrder.setStatus('current')
sysSecurityFileSystemAccessRestrictions = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 7), EnableDisable().clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityFileSystemAccessRestrictions.setStatus('current')
sysSecurityCUFrontICNPortAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 8), EnableDisable().clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityCUFrontICNPortAccess.setStatus('current')
sysSecurityChangeCUFrontICNPortAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 9), CommandString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityChangeCUFrontICNPortAccess.setStatus('current')
sysSecuritySubrackICNPortAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 10), EnableDisable().clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecuritySubrackICNPortAccess.setStatus('current')
sysSecurityChangeSubrackICNPortAccess = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 11), CommandString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityChangeSubrackICNPortAccess.setStatus('current')
sysSecurityMgmtAccessProofOfConnStatus = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("connected", 1), ("disconnected", 2))).clone('disconnected')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityMgmtAccessProofOfConnStatus.setStatus('current')
sysSecurityMgmtAccessProofOfConnectivity = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 720)).clone(120)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityMgmtAccessProofOfConnectivity.setStatus('current')
sysSecurityAutoEnableBlockedMgmtPorts = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 14), OnOff().clone('on')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityAutoEnableBlockedMgmtPorts.setStatus('current')
sysSecurityBlockedMgmtPortsUnblocked = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 11, 15), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityBlockedMgmtPortsUnblocked.setStatus('current')
sysManagerName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysManagerName.setStatus('current')
sysManagerIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysManagerIPAddress.setStatus('current')
sysManagerPolicyName = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysManagerPolicyName.setStatus('current')
sysManagerPlatform = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 2, 2, 12, 4), Platform().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysManagerPlatform.setStatus('current')
sysGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 1)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralTestAndIncr"), ("LUM-SYSTEM-MIB", "sysGeneralMibSpecVersion"), ("LUM-SYSTEM-MIB", "sysGeneralMibImplVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroup = sysGeneralGroup.setStatus('deprecated')
sysNodeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 2)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeRunLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroup = sysNodeGroup.setStatus('deprecated')
sysHostListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 3)).setObjects(("LUM-SYSTEM-MIB", "sysHostIndex"), ("LUM-SYSTEM-MIB", "sysHostIpAddress"), ("LUM-SYSTEM-MIB", "sysHostNames"), ("LUM-SYSTEM-MIB", "sysHostRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysHostListGroup = sysHostListGroup.setStatus('current')
sysTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 4)).setObjects(("LUM-SYSTEM-MIB", "sysTimeLocal"), ("LUM-SYSTEM-MIB", "sysTimeZone"), ("LUM-SYSTEM-MIB", "sysTimePrimaryServer"), ("LUM-SYSTEM-MIB", "sysTimeSecondaryServer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTimeGroup = sysTimeGroup.setStatus('deprecated')
sysLogListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 5)).setObjects(("LUM-SYSTEM-MIB", "sysLogIndex"), ("LUM-SYSTEM-MIB", "sysLogSelection"), ("LUM-SYSTEM-MIB", "sysLogAction"), ("LUM-SYSTEM-MIB", "sysLogRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysLogListGroup = sysLogListGroup.setStatus('deprecated')
sysGeneralGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 6)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroupV2 = sysGeneralGroupV2.setStatus('deprecated')
sysNodeGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 7)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeRunLevel"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV2 = sysNodeGroupV2.setStatus('deprecated')
sysUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 8)).setObjects(("LUM-SYSTEM-MIB", "sysUserIndex"), ("LUM-SYSTEM-MIB", "sysUserName"), ("LUM-SYSTEM-MIB", "sysUserPasswd"), ("LUM-SYSTEM-MIB", "sysUserDescr"), ("LUM-SYSTEM-MIB", "sysUserLastChangeTime"), ("LUM-SYSTEM-MIB", "sysUserExpireTime"), ("LUM-SYSTEM-MIB", "sysUserRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysUserGroup = sysUserGroup.setStatus('deprecated')
sysNodeGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 9)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeRunLevel"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeUptime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV3 = sysNodeGroupV3.setStatus('deprecated')
sysGeneralGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 10)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroupV3 = sysGeneralGroupV3.setStatus('current')
sysNodeGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 11)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeRunLevel"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeUptime"), ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeNeType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV4 = sysNodeGroupV4.setStatus('deprecated')
sysGeneralGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 12)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralTest"), ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroupV4 = sysGeneralGroupV4.setStatus('deprecated')
sysNodeGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 15)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeUptime"), ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeNeType"), ("LUM-SYSTEM-MIB", "sysNodeBootTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV5 = sysNodeGroupV5.setStatus('deprecated')
sysRadiusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 16)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimaryServer"), ("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryServer"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusGroup = sysRadiusGroup.setStatus('deprecated')
sysNodeGroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 17)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeUptime"), ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeNeType"), ("LUM-SYSTEM-MIB", "sysNodeBootTime"), ("LUM-SYSTEM-MIB", "sysNodeLocale"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV6 = sysNodeGroupV6.setStatus('deprecated')
sysTimeGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 18)).setObjects(("LUM-SYSTEM-MIB", "sysTimeLocal"), ("LUM-SYSTEM-MIB", "sysTimeZone"), ("LUM-SYSTEM-MIB", "sysTimePrimaryServer"), ("LUM-SYSTEM-MIB", "sysTimeSecondaryServer"), ("LUM-SYSTEM-MIB", "sysTimeChangeLocalTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTimeGroupV2 = sysTimeGroupV2.setStatus('deprecated')
sysLicenseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 19)).setObjects(("LUM-SYSTEM-MIB", "sysLicenseExpireDate"), ("LUM-SYSTEM-MIB", "sysLicenseCustomer"), ("LUM-SYSTEM-MIB", "sysLicenseExpiresSoon"), ("LUM-SYSTEM-MIB", "sysLicenseExpired"), ("LUM-SYSTEM-MIB", "sysLicenseExpiredCause"), ("LUM-SYSTEM-MIB", "sysLicenseFeatureEws"), ("LUM-SYSTEM-MIB", "sysLicenseFeatureEws"), ("LUM-SYSTEM-MIB", "sysLicenseFeatureOspf"), ("LUM-SYSTEM-MIB", "sysLicenseFeatureSnmp"), ("LUM-SYSTEM-MIB", "sysLicenseFeatureGmpls"), ("LUM-SYSTEM-MIB", "sysLicenseFeatureRudb"), ("LUM-SYSTEM-MIB", "sysLicenseInstallLicenseFile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysLicenseGroup = sysLicenseGroup.setStatus('current')
sysTacacsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 20)).setObjects(("LUM-SYSTEM-MIB", "sysTacacsPrimaryServer"), ("LUM-SYSTEM-MIB", "sysTacacsSecondaryServer"), ("LUM-SYSTEM-MIB", "sysTacacsSecret"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTacacsGroup = sysTacacsGroup.setStatus('deprecated')
sysUserGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 21)).setObjects(("LUM-SYSTEM-MIB", "sysUserIndex"), ("LUM-SYSTEM-MIB", "sysUserName"), ("LUM-SYSTEM-MIB", "sysUserDescr"), ("LUM-SYSTEM-MIB", "sysUserProfile"), ("LUM-SYSTEM-MIB", "sysUserUid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysUserGroupV2 = sysUserGroupV2.setStatus('current')
sysGeneralGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 22)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralTest"), ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralLoginRecords"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroupV5 = sysGeneralGroupV5.setStatus('deprecated')
sysUserGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 23)).setObjects(("LUM-SYSTEM-MIB", "sysUserIndex"), ("LUM-SYSTEM-MIB", "sysUserName"), ("LUM-SYSTEM-MIB", "sysUserDescr"), ("LUM-SYSTEM-MIB", "sysUserProfile"), ("LUM-SYSTEM-MIB", "sysUserUid"), ("LUM-SYSTEM-MIB", "sysUserChangePassword"), ("LUM-SYSTEM-MIB", "sysUserClearPassword"), ("LUM-SYSTEM-MIB", "sysUserDisable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysUserGroupV3 = sysUserGroupV3.setStatus('deprecated')
sysTacacsGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 24)).setObjects(("LUM-SYSTEM-MIB", "sysTacacsPrimaryServer"), ("LUM-SYSTEM-MIB", "sysTacacsSecondaryServer"), ("LUM-SYSTEM-MIB", "sysTacacsSecret"), ("LUM-SYSTEM-MIB", "sysTacacsSecondarySecret"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTacacsGroupV2 = sysTacacsGroupV2.setStatus('deprecated')
sysGeneralGroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 25)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralTest"), ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralLoginRecords"), ("LUM-SYSTEM-MIB", "sysGeneralUserTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroupV6 = sysGeneralGroupV6.setStatus('deprecated')
sysUserGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 26)).setObjects(("LUM-SYSTEM-MIB", "sysUserIndex"), ("LUM-SYSTEM-MIB", "sysUserName"), ("LUM-SYSTEM-MIB", "sysUserDescr"), ("LUM-SYSTEM-MIB", "sysUserProfile"), ("LUM-SYSTEM-MIB", "sysUserUid"), ("LUM-SYSTEM-MIB", "sysUserChangePassword"), ("LUM-SYSTEM-MIB", "sysUserClearPassword"), ("LUM-SYSTEM-MIB", "sysUserDisable"), ("LUM-SYSTEM-MIB", "sysUserMode"), ("LUM-SYSTEM-MIB", "sysUserEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysUserGroupV4 = sysUserGroupV4.setStatus('current')
sysSecurityGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 27)).setObjects(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysSecurityGroupV1 = sysSecurityGroupV1.setStatus('deprecated')
sysNodeGroupV7 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 28)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeUptime"), ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeNeType"), ("LUM-SYSTEM-MIB", "sysNodeBootTime"), ("LUM-SYSTEM-MIB", "sysNodeLocale"), ("LUM-SYSTEM-MIB", "sysNodeVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV7 = sysNodeGroupV7.setStatus('deprecated')
sysTacacsGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 29)).setObjects(("LUM-SYSTEM-MIB", "sysTacacsSecret"), ("LUM-SYSTEM-MIB", "sysTacacsSecondarySecret"), ("LUM-SYSTEM-MIB", "sysTacacsPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysTacacsSecondaryIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTacacsGroupV3 = sysTacacsGroupV3.setStatus('current')
sysRadiusGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 30)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusGroupV2 = sysRadiusGroupV2.setStatus('deprecated')
sysTimeGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 31)).setObjects(("LUM-SYSTEM-MIB", "sysTimeLocal"), ("LUM-SYSTEM-MIB", "sysTimeZone"), ("LUM-SYSTEM-MIB", "sysTimeChangeLocalTime"), ("LUM-SYSTEM-MIB", "sysTimePrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysTimeSecondaryIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTimeGroupV3 = sysTimeGroupV3.setStatus('current')
sysSecurityGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 32)).setObjects(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysSecurityGroupV2 = sysSecurityGroupV2.setStatus('deprecated')
sysRadiusGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 33)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusGroupV3 = sysRadiusGroupV3.setStatus('deprecated')
sysRadiusGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 34)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"), ("LUM-SYSTEM-MIB", "sysRadiusDefaultUserProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusGroupV4 = sysRadiusGroupV4.setStatus('current')
sysGeneralGroupV7 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 35)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralLoginRecords"), ("LUM-SYSTEM-MIB", "sysGeneralUserTableSize"), ("LUM-SYSTEM-MIB", "sysGeneralWriteTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralGroupV7 = sysGeneralGroupV7.setStatus('current')
sysSecurityGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 36)).setObjects(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"), ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysSecurityGroupV3 = sysSecurityGroupV3.setStatus('deprecated')
sysNodeGroupV8 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 37)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeObjectId"), ("LUM-SYSTEM-MIB", "sysNodePrimaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeSecondaryNameServer"), ("LUM-SYSTEM-MIB", "sysNodeUptime"), ("LUM-SYSTEM-MIB", "sysNodeNeDistinguishedName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeNeType"), ("LUM-SYSTEM-MIB", "sysNodeBootTime"), ("LUM-SYSTEM-MIB", "sysNodeLocale"), ("LUM-SYSTEM-MIB", "sysNodeVersion"), ("LUM-SYSTEM-MIB", "sysNodeCLLI"), ("LUM-SYSTEM-MIB", "sysNodeFIC"), ("LUM-SYSTEM-MIB", "sysNodeTID"), ("LUM-SYSTEM-MIB", "sysNodeLatitude"), ("LUM-SYSTEM-MIB", "sysNodeLongitude"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeGroupV8 = sysNodeGroupV8.setStatus('current')
sysSecurityGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 38)).setObjects(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"), ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"), ("LUM-SYSTEM-MIB", "sysSecurityFileSystemAccessRestrictions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysSecurityGroupV4 = sysSecurityGroupV4.setStatus('deprecated')
sysSecurityGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 39)).setObjects(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"), ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"), ("LUM-SYSTEM-MIB", "sysSecurityFileSystemAccessRestrictions"), ("LUM-SYSTEM-MIB", "sysSecurityCUFrontICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeCUFrontICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecuritySubrackICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeSubrackICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnStatus"), ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnectivity"), ("LUM-SYSTEM-MIB", "sysSecurityAutoEnableBlockedMgmtPorts"), ("LUM-SYSTEM-MIB", "sysSecurityBlockedMgmtPortsUnblocked"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysSecurityGroupV5 = sysSecurityGroupV5.setStatus('deprecated')
sysSecurityGroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 40)).setObjects(("LUM-SYSTEM-MIB", "sysSecurityLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalConsoleAccess"), ("LUM-SYSTEM-MIB", "sysSecurityLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeLocalCraftAccess"), ("LUM-SYSTEM-MIB", "sysSecurityIpTablesStatus"), ("LUM-SYSTEM-MIB", "sysSecurityAuthenticationOrder"), ("LUM-SYSTEM-MIB", "sysSecurityFileSystemAccessRestrictions"), ("LUM-SYSTEM-MIB", "sysSecurityCUFrontICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeCUFrontICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecuritySubrackICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecurityChangeSubrackICNPortAccess"), ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnStatus"), ("LUM-SYSTEM-MIB", "sysSecurityMgmtAccessProofOfConnectivity"), ("LUM-SYSTEM-MIB", "sysSecurityAutoEnableBlockedMgmtPorts"), ("LUM-SYSTEM-MIB", "sysSecurityBlockedMgmtPortsUnblocked"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysSecurityGroupV6 = sysSecurityGroupV6.setStatus('current')
sysManagerGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 1, 41)).setObjects(("LUM-SYSTEM-MIB", "sysManagerName"), ("LUM-SYSTEM-MIB", "sysManagerIPAddress"), ("LUM-SYSTEM-MIB", "sysManagerPolicyName"), ("LUM-SYSTEM-MIB", "sysManagerPlatform"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysManagerGroupV1 = sysManagerGroupV1.setStatus('current')
lumSystemBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 1)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroup"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysLogListGroup"), ("LUM-SYSTEM-MIB", "sysHostListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV1 = lumSystemBasicComplV1.setStatus('deprecated')
lumSystemBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 2)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV2"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV2 = lumSystemBasicComplV2.setStatus('deprecated')
lumSystemBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 3)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV2"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV2"), ("LUM-SYSTEM-MIB", "sysUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV3 = lumSystemBasicComplV3.setStatus('deprecated')
lumSystemBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 4)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV2"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV4 = lumSystemBasicComplV4.setStatus('deprecated')
lumSystemBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 5)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV3"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV5 = lumSystemBasicComplV5.setStatus('deprecated')
lumSystemBasicComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 6)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV3"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV4"), ("LUM-SYSTEM-MIB", "sysUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV6 = lumSystemBasicComplV6.setStatus('deprecated')
lumSystemBasicComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 7)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV5"), ("LUM-SYSTEM-MIB", "sysUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV7 = lumSystemBasicComplV7.setStatus('deprecated')
lumSystemBasicComplV8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 8)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV5"), ("LUM-SYSTEM-MIB", "sysUserGroup"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV8 = lumSystemBasicComplV8.setStatus('deprecated')
lumSystemBasicComplV9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 9)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"), ("LUM-SYSTEM-MIB", "sysTimeGroup"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysUserGroup"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV9 = lumSystemBasicComplV9.setStatus('deprecated')
lumSystemBasicComplV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 10)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV10 = lumSystemBasicComplV10.setStatus('deprecated')
lumSystemBasicComplV11 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 11)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV11 = lumSystemBasicComplV11.setStatus('deprecated')
lumSystemBasicComplV12 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 12)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV4"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroup"), ("LUM-SYSTEM-MIB", "sysUserGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV12 = lumSystemBasicComplV12.setStatus('deprecated')
lumSystemBasicComplV13 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 13)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV5"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroup"), ("LUM-SYSTEM-MIB", "sysUserGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV13 = lumSystemBasicComplV13.setStatus('deprecated')
lumSystemBasicComplV14 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 14)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"), ("LUM-SYSTEM-MIB", "sysUserGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV14 = lumSystemBasicComplV14.setStatus('deprecated')
lumSystemBasicComplV15 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 15)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV15 = lumSystemBasicComplV15.setStatus('deprecated')
lumSystemBasicComplV16 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 16)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV6"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV16 = lumSystemBasicComplV16.setStatus('deprecated')
lumSystemBasicComplV17 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 17)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeGroupV7"), ("LUM-SYSTEM-MIB", "sysRadiusGroup"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV2"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV17 = lumSystemBasicComplV17.setStatus('deprecated')
lumSystemBasicComplV18 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 18)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV7"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV2"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV18 = lumSystemBasicComplV18.setStatus('deprecated')
lumSystemBasicComplV19 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 19)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV7"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV2"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV19 = lumSystemBasicComplV19.setStatus('deprecated')
lumSystemBasicComplV20 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 20)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV7"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV3"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV20 = lumSystemBasicComplV20.setStatus('deprecated')
lumSystemBasicComplV21 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 21)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV6"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV7"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV21 = lumSystemBasicComplV21.setStatus('deprecated')
lumSystemBasicComplV22 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 22)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV7"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV22 = lumSystemBasicComplV22.setStatus('deprecated')
lumSystemBasicComplV23 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 23)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV8"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV23 = lumSystemBasicComplV23.setStatus('deprecated')
lumSystemBasicComplV24 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 24)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV8"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV24 = lumSystemBasicComplV24.setStatus('deprecated')
lumSystemBasicComplV25 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 25)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV8"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV25 = lumSystemBasicComplV25.setStatus('deprecated')
lumSystemBasicComplV26 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 26)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV8"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV26 = lumSystemBasicComplV26.setStatus('deprecated')
lumSystemBasicComplV27 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 27)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV8"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV27 = lumSystemBasicComplV27.setStatus('deprecated')
lumSystemBasicComplV28 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 2, 28)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralGroupV7"), ("LUM-SYSTEM-MIB", "sysTimeGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeGroupV8"), ("LUM-SYSTEM-MIB", "sysRadiusGroupV4"), ("LUM-SYSTEM-MIB", "sysLicenseGroup"), ("LUM-SYSTEM-MIB", "sysTacacsGroupV3"), ("LUM-SYSTEM-MIB", "sysUserGroupV4"), ("LUM-SYSTEM-MIB", "sysSecurityGroupV6"), ("LUM-SYSTEM-MIB", "sysManagerGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemBasicComplV28 = lumSystemBasicComplV28.setStatus('current')
sysGeneralMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 1)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralLastChangeTime"), ("LUM-SYSTEM-MIB", "sysGeneralConfigLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysGeneralMinimalGroupV1 = sysGeneralMinimalGroupV1.setStatus('current')
sysNodeMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 2)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeBootTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeMinimalGroupV1 = sysNodeMinimalGroupV1.setStatus('deprecated')
sysTimeMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 3)).setObjects(("LUM-SYSTEM-MIB", "sysTimeLocal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTimeMinimalGroupV1 = sysTimeMinimalGroupV1.setStatus('deprecated')
sysNodeMinimalGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 4)).setObjects(("LUM-SYSTEM-MIB", "sysNodeName"), ("LUM-SYSTEM-MIB", "sysNodeNeUserName"), ("LUM-SYSTEM-MIB", "sysNodeLocation"), ("LUM-SYSTEM-MIB", "sysNodeContact"), ("LUM-SYSTEM-MIB", "sysNodeBootTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysNodeMinimalGroupV2 = sysNodeMinimalGroupV2.setStatus('current')
sysTimeMinimalGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 5)).setObjects(("LUM-SYSTEM-MIB", "sysTimeLocal"), ("LUM-SYSTEM-MIB", "sysTimeZone"), ("LUM-SYSTEM-MIB", "sysTimePrimaryServer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTimeMinimalGroupV2 = sysTimeMinimalGroupV2.setStatus('deprecated')
sysRadiusMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 6)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimaryServer"), ("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryServer"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusMinimalGroupV1 = sysRadiusMinimalGroupV1.setStatus('deprecated')
sysTimeMinimalGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 7)).setObjects(("LUM-SYSTEM-MIB", "sysTimeLocal"), ("LUM-SYSTEM-MIB", "sysTimeZone"), ("LUM-SYSTEM-MIB", "sysTimePrimaryIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysTimeMinimalGroupV3 = sysTimeMinimalGroupV3.setStatus('current')
sysRadiusMinimalGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 8)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusMinimalGroupV2 = sysRadiusMinimalGroupV2.setStatus('deprecated')
sysRadiusMinimalGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 9)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusMinimalGroupV3 = sysRadiusMinimalGroupV3.setStatus('deprecated')
sysRadiusMinimalGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 3, 10)).setObjects(("LUM-SYSTEM-MIB", "sysRadiusPrimarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusSecondarySecret"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryIpAddress"), ("LUM-SYSTEM-MIB", "sysRadiusPrimaryPort"), ("LUM-SYSTEM-MIB", "sysRadiusSecondaryPort"), ("LUM-SYSTEM-MIB", "sysRadiusDefaultUserProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysRadiusMinimalGroupV4 = sysRadiusMinimalGroupV4.setStatus('current')
lumSystemMinimalComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 1)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV1 = lumSystemMinimalComplV1.setStatus('deprecated')
lumSystemMinimalComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 2)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV2 = lumSystemMinimalComplV2.setStatus('deprecated')
lumSystemMinimalComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 3)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV2"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"), ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV3 = lumSystemMinimalComplV3.setStatus('deprecated')
lumSystemMinimalComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 4)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"), ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV4 = lumSystemMinimalComplV4.setStatus('deprecated')
lumSystemMinimalComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 5)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"), ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV5 = lumSystemMinimalComplV5.setStatus('deprecated')
lumSystemMinimalComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 6)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"), ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV6 = lumSystemMinimalComplV6.setStatus('current')
lumSystemMinimalComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 2, 1, 4, 7)).setObjects(("LUM-SYSTEM-MIB", "sysGeneralMinimalGroupV1"), ("LUM-SYSTEM-MIB", "sysTimeMinimalGroupV3"), ("LUM-SYSTEM-MIB", "sysNodeMinimalGroupV2"), ("LUM-SYSTEM-MIB", "sysRadiusMinimalGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSystemMinimalComplV7 = lumSystemMinimalComplV7.setStatus('current')
mibBuilder.exportSymbols("LUM-SYSTEM-MIB", sysNodeName=sysNodeName, sysLicenseExpired=sysLicenseExpired, sysTacacsPrimaryServer=sysTacacsPrimaryServer, sysNodeGroupV3=sysNodeGroupV3, sysHostEntry=sysHostEntry, sysNodeSecondaryNameServer=sysNodeSecondaryNameServer, sysSecurityGroupV3=sysSecurityGroupV3, lumSystemBasicComplV5=lumSystemBasicComplV5, sysRadiusMinimalGroupV3=sysRadiusMinimalGroupV3, lumSystemBasicComplV10=lumSystemBasicComplV10, sysGeneralGroupV6=sysGeneralGroupV6, sysUserGroupV2=sysUserGroupV2, sysUserEnable=sysUserEnable, sysNodeGroupV4=sysNodeGroupV4, lumSystemBasicComplV9=lumSystemBasicComplV9, lumSystemBasicComplV20=lumSystemBasicComplV20, sysLicenseFeatureOspf=sysLicenseFeatureOspf, sysGeneralTestAndIncr=sysGeneralTestAndIncr, lumSystemBasicComplV3=lumSystemBasicComplV3, sysNodeMinimalGroupV1=sysNodeMinimalGroupV1, lumSystemBasicComplV2=lumSystemBasicComplV2, sysNode=sysNode, sysTimeZone=sysTimeZone, sysNodeGroupV6=sysNodeGroupV6, lumSystemMinimalComplV2=lumSystemMinimalComplV2, sysNodeLongitude=sysNodeLongitude, lumSystemBasicComplV15=lumSystemBasicComplV15, sysLogListGroup=sysLogListGroup, sysSecurityGroupV6=sysSecurityGroupV6, sysLogIndex=sysLogIndex, sysRadiusMinimalGroupV2=sysRadiusMinimalGroupV2, sysNodeTID=sysNodeTID, lumSystemBasicComplV13=lumSystemBasicComplV13, sysNodeObjectId=sysNodeObjectId, lumSystemBasicComplV14=lumSystemBasicComplV14, sysTimeSecondaryIpAddress=sysTimeSecondaryIpAddress, sysTacacsSecondarySecret=sysTacacsSecondarySecret, sysRadiusGroupV4=sysRadiusGroupV4, sysTimeSecondaryServer=sysTimeSecondaryServer, sysNodeBootTime=sysNodeBootTime, lumSystemBasicComplV27=lumSystemBasicComplV27, sysNodeContact=sysNodeContact, sysUserDisable=sysUserDisable, sysTimeLocal=sysTimeLocal, sysRadiusPrimarySecret=sysRadiusPrimarySecret, sysRadiusSecondaryServer=sysRadiusSecondaryServer, sysTacacsGroup=sysTacacsGroup, lumSystemMinimalCompl=lumSystemMinimalCompl, lumSystemBasicComplV19=lumSystemBasicComplV19, sysManager=sysManager, sysLogList=sysLogList, lumSystemBasicComplV23=lumSystemBasicComplV23, sysNodeGroupV5=sysNodeGroupV5, sysGeneralGroupV5=sysGeneralGroupV5, lumSystemMinimalComplV7=lumSystemMinimalComplV7, sysNodeLocation=sysNodeLocation, lumSystemBasicComplV22=lumSystemBasicComplV22, sysLicenseFeatureGmpls=sysLicenseFeatureGmpls, sysHostRowStatus=sysHostRowStatus, lumSystemBasicComplV4=lumSystemBasicComplV4, lumSystemBasicComplV26=lumSystemBasicComplV26, sysRadius=sysRadius, sysLicenseCustomer=sysLicenseCustomer, sysTacacsGroupV3=sysTacacsGroupV3, sysHostList=sysHostList, sysSecurityChangeLocalCraftAccess=sysSecurityChangeLocalCraftAccess, sysNodeGroupV2=sysNodeGroupV2, PYSNMP_MODULE_ID=lumSystemMIBModule, sysRadiusGroup=sysRadiusGroup, sysTacacsGroupV2=sysTacacsGroupV2, sysRadiusPrimaryServer=sysRadiusPrimaryServer, sysSecurityMgmtAccessProofOfConnectivity=sysSecurityMgmtAccessProofOfConnectivity, lumSystemMinimalGroups=lumSystemMinimalGroups, sysGeneralUserTableSize=sysGeneralUserTableSize, sysGeneralConfigLastChangeTime=sysGeneralConfigLastChangeTime, sysSecurityAutoEnableBlockedMgmtPorts=sysSecurityAutoEnableBlockedMgmtPorts, sysHostNames=sysHostNames, sysGeneralGroupV4=sysGeneralGroupV4, lumSystemBasicComplV28=lumSystemBasicComplV28, sysNodeMinimalGroupV2=sysNodeMinimalGroupV2, sysHostTable=sysHostTable, sysManagerIPAddress=sysManagerIPAddress, lumSystemMIBObjects=lumSystemMIBObjects, lumSystemBasicComplV6=lumSystemBasicComplV6, sysSecurityLocalCraftAccess=sysSecurityLocalCraftAccess, sysGeneral=sysGeneral, sysNodeLocale=sysNodeLocale, sysNodeCLLI=sysNodeCLLI, sysUserProfile=sysUserProfile, sysTacacsPrimaryIpAddress=sysTacacsPrimaryIpAddress, sysTacacsSecret=sysTacacsSecret, sysSecurityChangeSubrackICNPortAccess=sysSecurityChangeSubrackICNPortAccess, sysLicenseGroup=sysLicenseGroup, sysGeneralTest=sysGeneralTest, sysTacacsSecondaryServer=sysTacacsSecondaryServer, sysRadiusPrimaryPort=sysRadiusPrimaryPort, sysGeneralMinimalGroupV1=sysGeneralMinimalGroupV1, sysGeneralWriteTest=sysGeneralWriteTest, sysLicenseFeatureRudb=sysLicenseFeatureRudb, sysTimeMinimalGroupV3=sysTimeMinimalGroupV3, sysUserList=sysUserList, sysLicenseFeatureEws=sysLicenseFeatureEws, sysTimeGroupV2=sysTimeGroupV2, sysHostListGroup=sysHostListGroup, lumSystemBasicComplV11=lumSystemBasicComplV11, sysNodeVersion=sysNodeVersion, sysSecurityGroupV5=sysSecurityGroupV5, lumSystemMinimalComplV4=lumSystemMinimalComplV4, sysNodeNeUserName=sysNodeNeUserName, sysGeneralGroupV3=sysGeneralGroupV3, sysNodeRunLevel=sysNodeRunLevel, sysLicenseFeatureSnmp=sysLicenseFeatureSnmp, sysRadiusMinimalGroupV4=sysRadiusMinimalGroupV4, sysSecurityMgmtAccessProofOfConnStatus=sysSecurityMgmtAccessProofOfConnStatus, lumSystemConfs=lumSystemConfs, sysGeneralGroupV7=sysGeneralGroupV7, lumSystemGroups=lumSystemGroups, sysTimePrimaryIpAddress=sysTimePrimaryIpAddress, sysUserChangePassword=sysUserChangePassword, sysRadiusSecondaryPort=sysRadiusSecondaryPort, sysLicenseInstallLicenseFile=sysLicenseInstallLicenseFile, sysUserLastChangeTime=sysUserLastChangeTime, sysGeneralLastChangeTime=sysGeneralLastChangeTime, lumSystemMIBModule=lumSystemMIBModule, sysNodeNeDistinguishedName=sysNodeNeDistinguishedName, sysUserGroup=sysUserGroup, lumSystemBasicComplV18=lumSystemBasicComplV18, sysUserIndex=sysUserIndex, sysSecurityChangeCUFrontICNPortAccess=sysSecurityChangeCUFrontICNPortAccess, sysAudit=sysAudit, lumSystemMinimalComplV3=lumSystemMinimalComplV3, sysHostIndex=sysHostIndex, sysLicenseExpiresSoon=sysLicenseExpiresSoon, sysUserName=sysUserName, sysGeneralLoginRecords=sysGeneralLoginRecords, sysSecurityGroupV1=sysSecurityGroupV1, sysGeneralMibImplVersion=sysGeneralMibImplVersion, sysSecurityFileSystemAccessRestrictions=sysSecurityFileSystemAccessRestrictions, sysGeneralGroupV2=sysGeneralGroupV2, sysUserEntry=sysUserEntry, lumSystemBasicComplV1=lumSystemBasicComplV1, sysLicenseExpireDate=sysLicenseExpireDate, sysSecuritySubrackICNPortAccess=sysSecuritySubrackICNPortAccess, lumSystemBasicComplV24=lumSystemBasicComplV24, sysLicenseExpiredCause=sysLicenseExpiredCause, sysUserGroupV4=sysUserGroupV4, sysGeneralGroup=sysGeneralGroup, sysRadiusGroupV2=sysRadiusGroupV2, sysNodeUptime=sysNodeUptime, sysTimePrimaryServer=sysTimePrimaryServer, sysNodeNeType=sysNodeNeType, sysRadiusSecondarySecret=sysRadiusSecondarySecret, sysRadiusPrimaryIpAddress=sysRadiusPrimaryIpAddress, sysTimeMinimalGroupV1=sysTimeMinimalGroupV1, sysUserExpireTime=sysUserExpireTime, sysUserGroupV3=sysUserGroupV3, sysLicense=sysLicense, lumSystemMinimalComplV1=lumSystemMinimalComplV1, sysTimeGroup=sysTimeGroup, sysGeneralMibSpecVersion=sysGeneralMibSpecVersion, lumSystemMinimalComplV6=lumSystemMinimalComplV6, sysSecurity=sysSecurity, sysUserPasswd=sysUserPasswd, sysUserTable=sysUserTable, sysTime=sysTime, sysSecurityIpTablesStatus=sysSecurityIpTablesStatus, sysSecurityChangeLocalConsoleAccess=sysSecurityChangeLocalConsoleAccess, sysNodeGroupV8=sysNodeGroupV8, lumSystemBasicComplV16=lumSystemBasicComplV16, sysNodePrimaryNameServer=sysNodePrimaryNameServer, sysUserClearPassword=sysUserClearPassword, sysRadiusMinimalGroupV1=sysRadiusMinimalGroupV1, sysLogEntry=sysLogEntry, sysSecurityCUFrontICNPortAccess=sysSecurityCUFrontICNPortAccess, sysHostIpAddress=sysHostIpAddress, sysNodeFIC=sysNodeFIC, lumSystemBasicComplV25=lumSystemBasicComplV25, sysNodeGroup=sysNodeGroup, lumSystemCompl=lumSystemCompl, sysLogTable=sysLogTable, lumSystemMinimalComplV5=lumSystemMinimalComplV5, lumSystemBasicComplV12=lumSystemBasicComplV12, sysUserDescr=sysUserDescr, lumSystemBasicComplV17=lumSystemBasicComplV17, sysSecurityAuthenticationOrder=sysSecurityAuthenticationOrder, sysUserRowStatus=sysUserRowStatus, sysSecurityGroupV2=sysSecurityGroupV2, sysSecurityBlockedMgmtPortsUnblocked=sysSecurityBlockedMgmtPortsUnblocked, lumSystemBasicComplV7=lumSystemBasicComplV7, sysRadiusSecondaryIpAddress=sysRadiusSecondaryIpAddress, sysLogSelection=sysLogSelection, lumSystemBasicComplV21=lumSystemBasicComplV21, sysTacacsSecondaryIpAddress=sysTacacsSecondaryIpAddress, sysLogRowStatus=sysLogRowStatus, sysTimeMinimalGroupV2=sysTimeMinimalGroupV2, sysManagerPlatform=sysManagerPlatform, sysNodeLatitude=sysNodeLatitude, sysTimeGroupV3=sysTimeGroupV3, sysManagerPolicyName=sysManagerPolicyName, sysNodeGroupV7=sysNodeGroupV7, sysRadiusGroupV3=sysRadiusGroupV3, sysTimeChangeLocalTime=sysTimeChangeLocalTime, sysUserMode=sysUserMode, sysLogAction=sysLogAction, sysRadiusDefaultUserProfile=sysRadiusDefaultUserProfile, sysSecurityGroupV4=sysSecurityGroupV4, sysManagerName=sysManagerName, lumSystemBasicComplV8=lumSystemBasicComplV8, sysUserUid=sysUserUid, sysSecurityLocalConsoleAccess=sysSecurityLocalConsoleAccess, sysTacacs=sysTacacs, sysManagerGroupV1=sysManagerGroupV1)
