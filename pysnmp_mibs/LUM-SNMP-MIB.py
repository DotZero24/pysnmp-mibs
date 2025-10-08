#
# PySNMP MIB module LUM-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-SNMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumModules, lumSnmpMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumSnmpMIB")
CommandString, = mibBuilder.importSymbols("LUM-TC", "CommandString")
SnmpEngineID, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpEngineID")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "StorageType", "DisplayString")
lumSnmpMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 18))
lumSnmpMIBModule.setRevisions(('2018-04-13 00:00', '2017-06-15 00:00', '2014-12-09 00:00', '2008-06-05 00:00', '2004-10-01 00:00', '2004-06-23 00:00', '2003-09-30 00:00', '2002-05-30 00:00',))
if mibBuilder.loadTexts: lumSnmpMIBModule.setLastUpdated('201804130000Z')
if mibBuilder.loadTexts: lumSnmpMIBModule.setOrganization('Infinera Corporation')
lumSnmpConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1))
lumSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1))
lumSnmpCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2))
lumSnmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2))
snmpInformSinkList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1))
snmpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2))
snmpUserList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3))
snmpInformSinkTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1), )
if mibBuilder.loadTexts: snmpInformSinkTable.setStatus('current')
snmpInformSinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1), ).setIndexNames((0, "LUM-SNMP-MIB", "snmpInformSinkIndex"))
if mibBuilder.loadTexts: snmpInformSinkEntry.setStatus('current')
snmpInformSinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInformSinkIndex.setStatus('current')
snmpInformSinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInformSinkName.setStatus('current')
snmpInformSinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpInformSinkAddr.setStatus('current')
snmpInformSinkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpInformSinkPort.setStatus('current')
snmpInformSinkCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpInformSinkCommunity.setStatus('current')
snmpInformSinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpInformSinkRowStatus.setStatus('current')
snmpInformSinkStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpInformSinkStorageType.setStatus('current')
snmpInformSinkAlarmNotifications = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpInformSinkAlarmNotifications.setStatus('current')
snmpInformSinkPerformanceNotifications = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpInformSinkPerformanceNotifications.setStatus('current')
snmpInformSinkOtherNotifications = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpInformSinkOtherNotifications.setStatus('current')
snmpInformSinkMib2Notifications = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpInformSinkMib2Notifications.setStatus('current')
snmpGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralLastChangeTime.setStatus('current')
snmpGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralConfigLastChangeTime.setStatus('current')
snmpGeneralEngineID = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 3), SnmpEngineID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralEngineID.setStatus('current')
snmpGeneralCommunity = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 33)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpGeneralCommunity.setStatus('current')
snmpGeneralInformSinkTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralInformSinkTableSize.setStatus('current')
snmpGeneralUserTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralUserTableSize.setStatus('current')
snmpGeneralResetEngineIDCommand = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 7), CommandString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralResetEngineIDCommand.setStatus('current')
snmpGeneralSecurityPolicy = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("basic", 1), ("authentication", 2), ("authAndPrivacy", 3))).clone('basic')).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpGeneralSecurityPolicy.setStatus('current')
snmpUserTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1), )
if mibBuilder.loadTexts: snmpUserTable.setStatus('current')
snmpUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1), ).setIndexNames((0, "LUM-SNMP-MIB", "snmpUserIndex"))
if mibBuilder.loadTexts: snmpUserEntry.setStatus('current')
snmpUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUserIndex.setStatus('current')
snmpUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('oper')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpUserName.setStatus('current')
snmpUserChangePassword = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 3), CommandString().clone('1234567890')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpUserChangePassword.setStatus('current')
snmpUserEngineId = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 4), SnmpEngineID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpUserEngineId.setStatus('current')
snmpUserAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpUserAuthKey.setStatus('current')
snmpUserPrivKey = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpUserPrivKey.setStatus('current')
snmpUserChangePrivPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 7), CommandString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpUserChangePrivPassword.setStatus('current')
snmpUserPrivProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("aes128", 2))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUserPrivProtocol.setStatus('current')
snmpInformSinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 1)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkIndex"), ("LUM-SNMP-MIB", "snmpInformSinkName"), ("LUM-SNMP-MIB", "snmpInformSinkAddr"), ("LUM-SNMP-MIB", "snmpInformSinkPort"), ("LUM-SNMP-MIB", "snmpInformSinkCommunity"), ("LUM-SNMP-MIB", "snmpInformSinkRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpInformSinkGroup = snmpInformSinkGroup.setStatus('deprecated')
snmpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 2)).setObjects(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGeneralGroup = snmpGeneralGroup.setStatus('deprecated')
snmpGeneralGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 3)).setObjects(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralEngineID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGeneralGroupV2 = snmpGeneralGroupV2.setStatus('deprecated')
snmpUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 4)).setObjects(("LUM-SNMP-MIB", "snmpUserIndex"), ("LUM-SNMP-MIB", "snmpUserName"), ("LUM-SNMP-MIB", "snmpUserChangePassword"), ("LUM-SNMP-MIB", "snmpUserEngineId"), ("LUM-SNMP-MIB", "snmpUserAuthKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpUserGroup = snmpUserGroup.setStatus('deprecated')
snmpGeneralGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 5)).setObjects(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralEngineID"), ("LUM-SNMP-MIB", "snmpGeneralCommunity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGeneralGroupV3 = snmpGeneralGroupV3.setStatus('deprecated')
snmpInformSinkGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 6)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkIndex"), ("LUM-SNMP-MIB", "snmpInformSinkName"), ("LUM-SNMP-MIB", "snmpInformSinkAddr"), ("LUM-SNMP-MIB", "snmpInformSinkPort"), ("LUM-SNMP-MIB", "snmpInformSinkCommunity"), ("LUM-SNMP-MIB", "snmpInformSinkRowStatus"), ("LUM-SNMP-MIB", "snmpInformSinkStorageType"), ("LUM-SNMP-MIB", "snmpInformSinkAlarmNotifications"), ("LUM-SNMP-MIB", "snmpInformSinkPerformanceNotifications"), ("LUM-SNMP-MIB", "snmpInformSinkOtherNotifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpInformSinkGroupV2 = snmpInformSinkGroupV2.setStatus('deprecated')
snmpGeneralGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 7)).setObjects(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralEngineID"), ("LUM-SNMP-MIB", "snmpGeneralCommunity"), ("LUM-SNMP-MIB", "snmpGeneralInformSinkTableSize"), ("LUM-SNMP-MIB", "snmpGeneralUserTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGeneralGroupV4 = snmpGeneralGroupV4.setStatus('deprecated')
snmpInformSinkGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 8)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkIndex"), ("LUM-SNMP-MIB", "snmpInformSinkName"), ("LUM-SNMP-MIB", "snmpInformSinkAddr"), ("LUM-SNMP-MIB", "snmpInformSinkPort"), ("LUM-SNMP-MIB", "snmpInformSinkCommunity"), ("LUM-SNMP-MIB", "snmpInformSinkRowStatus"), ("LUM-SNMP-MIB", "snmpInformSinkStorageType"), ("LUM-SNMP-MIB", "snmpInformSinkAlarmNotifications"), ("LUM-SNMP-MIB", "snmpInformSinkPerformanceNotifications"), ("LUM-SNMP-MIB", "snmpInformSinkOtherNotifications"), ("LUM-SNMP-MIB", "snmpInformSinkMib2Notifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpInformSinkGroupV3 = snmpInformSinkGroupV3.setStatus('current')
snmpGeneralGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 9)).setObjects(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralEngineID"), ("LUM-SNMP-MIB", "snmpGeneralCommunity"), ("LUM-SNMP-MIB", "snmpGeneralInformSinkTableSize"), ("LUM-SNMP-MIB", "snmpGeneralUserTableSize"), ("LUM-SNMP-MIB", "snmpGeneralResetEngineIDCommand"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGeneralGroupV5 = snmpGeneralGroupV5.setStatus('deprecated')
snmpGeneralGroupV6 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 10)).setObjects(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"), ("LUM-SNMP-MIB", "snmpGeneralEngineID"), ("LUM-SNMP-MIB", "snmpGeneralCommunity"), ("LUM-SNMP-MIB", "snmpGeneralInformSinkTableSize"), ("LUM-SNMP-MIB", "snmpGeneralUserTableSize"), ("LUM-SNMP-MIB", "snmpGeneralResetEngineIDCommand"), ("LUM-SNMP-MIB", "snmpGeneralSecurityPolicy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpGeneralGroupV6 = snmpGeneralGroupV6.setStatus('current')
snmpUserGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 11)).setObjects(("LUM-SNMP-MIB", "snmpUserIndex"), ("LUM-SNMP-MIB", "snmpUserName"), ("LUM-SNMP-MIB", "snmpUserChangePassword"), ("LUM-SNMP-MIB", "snmpUserEngineId"), ("LUM-SNMP-MIB", "snmpUserAuthKey"), ("LUM-SNMP-MIB", "snmpUserPrivKey"), ("LUM-SNMP-MIB", "snmpUserChangePrivPassword"), ("LUM-SNMP-MIB", "snmpUserPrivProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpUserGroupV2 = snmpUserGroupV2.setStatus('current')
lumSnmpBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 1)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroup"), ("LUM-SNMP-MIB", "snmpGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV1 = lumSnmpBasicComplV1.setStatus('deprecated')
lumSnmpBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 2)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroup"), ("LUM-SNMP-MIB", "snmpGeneralGroupV2"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV2 = lumSnmpBasicComplV2.setStatus('deprecated')
lumSnmpBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 3)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroup"), ("LUM-SNMP-MIB", "snmpGeneralGroupV2"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV3 = lumSnmpBasicComplV3.setStatus('deprecated')
lumSnmpBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 4)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroup"), ("LUM-SNMP-MIB", "snmpGeneralGroupV3"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV4 = lumSnmpBasicComplV4.setStatus('deprecated')
lumSnmpBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 5)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroupV2"), ("LUM-SNMP-MIB", "snmpGeneralGroupV3"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV5 = lumSnmpBasicComplV5.setStatus('deprecated')
lumSnmpBasicComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 6)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroupV2"), ("LUM-SNMP-MIB", "snmpGeneralGroupV4"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV6 = lumSnmpBasicComplV6.setStatus('deprecated')
lumSnmpBasicComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 7)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"), ("LUM-SNMP-MIB", "snmpGeneralGroupV4"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV7 = lumSnmpBasicComplV7.setStatus('deprecated')
lumSnmpBasicComplV8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 8)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"), ("LUM-SNMP-MIB", "snmpGeneralGroupV5"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV8 = lumSnmpBasicComplV8.setStatus('deprecated')
lumSnmpBasicComplV9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 9)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"), ("LUM-SNMP-MIB", "snmpGeneralGroupV5"), ("LUM-SNMP-MIB", "snmpUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV9 = lumSnmpBasicComplV9.setStatus('deprecated')
lumSnmpBasicComplV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 10)).setObjects(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"), ("LUM-SNMP-MIB", "snmpGeneralGroupV6"), ("LUM-SNMP-MIB", "snmpUserGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumSnmpBasicComplV10 = lumSnmpBasicComplV10.setStatus('current')
mibBuilder.exportSymbols("LUM-SNMP-MIB", snmpGeneral=snmpGeneral, snmpUserChangePrivPassword=snmpUserChangePrivPassword, lumSnmpBasicComplV7=lumSnmpBasicComplV7, snmpInformSinkTable=snmpInformSinkTable, snmpGeneralEngineID=snmpGeneralEngineID, snmpInformSinkList=snmpInformSinkList, snmpUserAuthKey=snmpUserAuthKey, snmpUserGroupV2=snmpUserGroupV2, snmpGeneralSecurityPolicy=snmpGeneralSecurityPolicy, snmpInformSinkMib2Notifications=snmpInformSinkMib2Notifications, lumSnmpBasicComplV1=lumSnmpBasicComplV1, snmpInformSinkEntry=snmpInformSinkEntry, snmpGeneralLastChangeTime=snmpGeneralLastChangeTime, snmpGeneralConfigLastChangeTime=snmpGeneralConfigLastChangeTime, snmpUserPrivKey=snmpUserPrivKey, snmpInformSinkIndex=snmpInformSinkIndex, snmpUserList=snmpUserList, snmpInformSinkAlarmNotifications=snmpInformSinkAlarmNotifications, snmpGeneralGroup=snmpGeneralGroup, snmpInformSinkGroupV3=snmpInformSinkGroupV3, snmpInformSinkCommunity=snmpInformSinkCommunity, snmpGeneralInformSinkTableSize=snmpGeneralInformSinkTableSize, snmpUserChangePassword=snmpUserChangePassword, lumSnmpBasicComplV10=lumSnmpBasicComplV10, snmpGeneralGroupV3=snmpGeneralGroupV3, lumSnmpBasicComplV6=lumSnmpBasicComplV6, snmpGeneralGroupV5=snmpGeneralGroupV5, lumSnmpMIBObjects=lumSnmpMIBObjects, snmpUserPrivProtocol=snmpUserPrivProtocol, snmpGeneralGroupV2=snmpGeneralGroupV2, lumSnmpBasicComplV3=lumSnmpBasicComplV3, lumSnmpConfs=lumSnmpConfs, snmpGeneralCommunity=snmpGeneralCommunity, PYSNMP_MODULE_ID=lumSnmpMIBModule, snmpUserEntry=snmpUserEntry, snmpUserEngineId=snmpUserEngineId, snmpInformSinkAddr=snmpInformSinkAddr, lumSnmpBasicComplV5=lumSnmpBasicComplV5, snmpGeneralUserTableSize=snmpGeneralUserTableSize, snmpGeneralGroupV4=snmpGeneralGroupV4, snmpInformSinkRowStatus=snmpInformSinkRowStatus, snmpInformSinkStorageType=snmpInformSinkStorageType, lumSnmpMIBModule=lumSnmpMIBModule, lumSnmpGroups=lumSnmpGroups, snmpInformSinkPort=snmpInformSinkPort, snmpInformSinkName=snmpInformSinkName, snmpUserIndex=snmpUserIndex, snmpUserGroup=snmpUserGroup, lumSnmpBasicComplV4=lumSnmpBasicComplV4, lumSnmpBasicComplV8=lumSnmpBasicComplV8, snmpGeneralGroupV6=snmpGeneralGroupV6, snmpGeneralResetEngineIDCommand=snmpGeneralResetEngineIDCommand, snmpUserTable=snmpUserTable, snmpInformSinkGroup=snmpInformSinkGroup, lumSnmpBasicComplV9=lumSnmpBasicComplV9, snmpInformSinkGroupV2=snmpInformSinkGroupV2, snmpInformSinkOtherNotifications=snmpInformSinkOtherNotifications, snmpInformSinkPerformanceNotifications=snmpInformSinkPerformanceNotifications, lumSnmpBasicComplV2=lumSnmpBasicComplV2, lumSnmpCompl=lumSnmpCompl, snmpUserName=snmpUserName)
