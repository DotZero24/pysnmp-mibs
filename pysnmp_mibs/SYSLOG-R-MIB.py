#
# PySNMP MIB module SYSLOG-R-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rad/SYSLOG-R-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:42:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
radExperimental, = mibBuilder.importSymbols("RAD-SMI-MIB", "radExperimental")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "StorageType", "TextualConvention")
syslogMIBR = ModuleIdentity((1, 3, 6, 1, 4, 1, 164, 20, 14))
if mibBuilder.loadTexts: syslogMIBR.setLastUpdated('201403051512Z')
if mibBuilder.loadTexts: syslogMIBR.setOrganization('RAD Data Communications Ltd.')
class SyslogRoles(TextualConvention, Bits):
    reference = 'The Syslog Protocol [RFCPROT] sec. 3. '
    status = 'current'
    namedValues = NamedValues(("sender", 0), ("receiver", 1), ("relay", 2))

class SyslogService(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SyslogEncapsulation(TextualConvention, Integer32):
    reference = 'Transmission of syslog messages over UDP [RFCUDPX], TLS Transport Mapping for Syslog [RFCTLSX], Reliable Delivery for syslog [RFCBEEP]. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("none", 2), ("tls", 3), ("beep", 4))

syslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20, 14, 0))
syslogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20, 14, 1))
syslogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20, 14, 3))
syslogSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 1))
syslogDefaultService = MibScalar((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 1, 1), SyslogService().clone('514')).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogDefaultService.setStatus('current')
syslogDefaultEncapsulation = MibScalar((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 1, 2), SyslogEncapsulation().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogDefaultEncapsulation.setStatus('current')
syslogControlTable = MibTable((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2), )
if mibBuilder.loadTexts: syslogControlTable.setStatus('current')
syslogControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1), ).setIndexNames((0, "SYSLOG-R-MIB", "syslogControlIndex"))
if mibBuilder.loadTexts: syslogControlEntry.setStatus('current')
syslogControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: syslogControlIndex.setStatus('current')
syslogControlDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlDescr.setStatus('current')
syslogControlRoles = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 3), SyslogRoles()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlRoles.setStatus('current')
syslogControlBindAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlBindAddrType.setStatus('current')
syslogControlBindAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlBindAddr.setStatus('current')
syslogControlService = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 6), SyslogService()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlService.setStatus('current')
syslogControlEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 7), SyslogEncapsulation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlEncapsulation.setStatus('current')
syslogControlMaxMessageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlMaxMessageSize.setStatus('current')
syslogControlConfFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 9), SnmpAdminString().clone('/etc/syslog.conf')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlConfFileName.setStatus('current')
syslogControlStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlStorageType.setStatus('current')
syslogControlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlRowStatus.setStatus('current')
syslogControlAccountingType = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 13), Bits().clone(namedValues=NamedValues(("shell", 0), ("system", 1), ("commands", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: syslogControlAccountingType.setStatus('current')
syslogOperationsTable = MibTable((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3), )
if mibBuilder.loadTexts: syslogOperationsTable.setStatus('current')
syslogOperationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1), )
syslogControlEntry.registerAugmentions(("SYSLOG-R-MIB", "syslogOperationsEntry"))
syslogOperationsEntry.setIndexNames(*syslogControlEntry.getIndexNames())
if mibBuilder.loadTexts: syslogOperationsEntry.setStatus('current')
syslogOperationsMsgsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsMsgsReceived.setStatus('current')
syslogOperationsMsgsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsMsgsTransmitted.setStatus('current')
syslogOperationsMsgsRelayed = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsMsgsRelayed.setStatus('current')
syslogOperationsMsgsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsMsgsDropped.setStatus('current')
syslogOperationsMsgsMalFormed = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsMsgsMalFormed.setStatus('current')
syslogOperationsMsgsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsMsgsDiscarded.setStatus('current')
syslogOperationsLastMsgRecdTime = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsLastMsgRecdTime.setStatus('current')
syslogOperationsLastMsgTransmittedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsLastMsgTransmittedTime.setStatus('current')
syslogOperationsStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsStartTime.setStatus('current')
syslogOperationsLastError = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsLastError.setStatus('current')
syslogOperationsLastErrorTime = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsLastErrorTime.setStatus('current')
syslogOperationsRunIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsRunIndex.setStatus('current')
syslogOperationsCounterDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsCounterDiscontinuityTime.setStatus('current')
syslogOperationsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("started", 2), ("suspended", 3), ("stopped", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogOperationsStatus.setStatus('current')
syslogStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 164, 20, 14, 0, 1)).setObjects(("SYSLOG-R-MIB", "syslogControlDescr"), ("SYSLOG-R-MIB", "syslogControlRoles"), ("SYSLOG-R-MIB", "syslogControlBindAddrType"), ("SYSLOG-R-MIB", "syslogControlBindAddr"), ("SYSLOG-R-MIB", "syslogControlService"), ("SYSLOG-R-MIB", "syslogControlEncapsulation"), ("SYSLOG-R-MIB", "syslogControlConfFileName"), ("SYSLOG-R-MIB", "syslogOperationsStatus"))
if mibBuilder.loadTexts: syslogStatusChanged.setStatus('current')
syslogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1))
syslogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2))
syslogDefaultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 1)).setObjects(("SYSLOG-R-MIB", "syslogDefaultService"), ("SYSLOG-R-MIB", "syslogDefaultEncapsulation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogDefaultGroup = syslogDefaultGroup.setStatus('current')
syslogOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 2)).setObjects(("SYSLOG-R-MIB", "syslogOperationsMsgsReceived"), ("SYSLOG-R-MIB", "syslogOperationsMsgsTransmitted"), ("SYSLOG-R-MIB", "syslogOperationsMsgsRelayed"), ("SYSLOG-R-MIB", "syslogOperationsMsgsDropped"), ("SYSLOG-R-MIB", "syslogOperationsMsgsMalFormed"), ("SYSLOG-R-MIB", "syslogOperationsMsgsDiscarded"), ("SYSLOG-R-MIB", "syslogOperationsLastMsgRecdTime"), ("SYSLOG-R-MIB", "syslogOperationsLastMsgTransmittedTime"), ("SYSLOG-R-MIB", "syslogOperationsStartTime"), ("SYSLOG-R-MIB", "syslogOperationsLastError"), ("SYSLOG-R-MIB", "syslogOperationsLastErrorTime"), ("SYSLOG-R-MIB", "syslogOperationsRunIndex"), ("SYSLOG-R-MIB", "syslogOperationsCounterDiscontinuityTime"), ("SYSLOG-R-MIB", "syslogOperationsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogOperationsGroup = syslogOperationsGroup.setStatus('current')
syslogControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 3)).setObjects(("SYSLOG-R-MIB", "syslogControlDescr"), ("SYSLOG-R-MIB", "syslogControlRoles"), ("SYSLOG-R-MIB", "syslogControlBindAddrType"), ("SYSLOG-R-MIB", "syslogControlBindAddr"), ("SYSLOG-R-MIB", "syslogControlEncapsulation"), ("SYSLOG-R-MIB", "syslogControlService"), ("SYSLOG-R-MIB", "syslogControlMaxMessageSize"), ("SYSLOG-R-MIB", "syslogControlConfFileName"), ("SYSLOG-R-MIB", "syslogControlStorageType"), ("SYSLOG-R-MIB", "syslogControlRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogControlGroup = syslogControlGroup.setStatus('current')
syslogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 4)).setObjects(("SYSLOG-R-MIB", "syslogStatusChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogNotificationGroup = syslogNotificationGroup.setStatus('current')
syslogFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 1)).setObjects(("SYSLOG-R-MIB", "syslogNotificationGroup"), ("SYSLOG-R-MIB", "syslogDefaultGroup"), ("SYSLOG-R-MIB", "syslogOperationsGroup"), ("SYSLOG-R-MIB", "syslogControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogFullCompliance1 = syslogFullCompliance1.setStatus('current')
syslogFullCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 2)).setObjects(("SYSLOG-R-MIB", "syslogDefaultGroup"), ("SYSLOG-R-MIB", "syslogOperationsGroup"), ("SYSLOG-R-MIB", "syslogControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogFullCompliance2 = syslogFullCompliance2.setStatus('current')
syslogReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 3)).setObjects(("SYSLOG-R-MIB", "syslogNotificationGroup"), ("SYSLOG-R-MIB", "syslogDefaultGroup"), ("SYSLOG-R-MIB", "syslogOperationsGroup"), ("SYSLOG-R-MIB", "syslogControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogReadOnlyCompliance1 = syslogReadOnlyCompliance1.setStatus('current')
syslogReadOnlyCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 4)).setObjects(("SYSLOG-R-MIB", "syslogDefaultGroup"), ("SYSLOG-R-MIB", "syslogOperationsGroup"), ("SYSLOG-R-MIB", "syslogControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogReadOnlyCompliance2 = syslogReadOnlyCompliance2.setStatus('current')
syslogNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 5)).setObjects(("SYSLOG-R-MIB", "syslogNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogNotificationCompliance = syslogNotificationCompliance.setStatus('current')
mibBuilder.exportSymbols("SYSLOG-R-MIB", SyslogService=SyslogService, syslogOperationsMsgsReceived=syslogOperationsMsgsReceived, syslogFullCompliance2=syslogFullCompliance2, syslogOperationsLastMsgTransmittedTime=syslogOperationsLastMsgTransmittedTime, SyslogEncapsulation=SyslogEncapsulation, syslogControlRoles=syslogControlRoles, syslogOperationsMsgsMalFormed=syslogOperationsMsgsMalFormed, syslogDefaultService=syslogDefaultService, syslogNotifications=syslogNotifications, syslogControlBindAddrType=syslogControlBindAddrType, syslogReadOnlyCompliance2=syslogReadOnlyCompliance2, syslogOperationsCounterDiscontinuityTime=syslogOperationsCounterDiscontinuityTime, syslogOperationsEntry=syslogOperationsEntry, syslogDefaultGroup=syslogDefaultGroup, syslogSystem=syslogSystem, syslogControlConfFileName=syslogControlConfFileName, syslogOperationsMsgsTransmitted=syslogOperationsMsgsTransmitted, syslogControlStorageType=syslogControlStorageType, syslogControlIndex=syslogControlIndex, syslogNotificationGroup=syslogNotificationGroup, syslogOperationsLastError=syslogOperationsLastError, syslogControlEncapsulation=syslogControlEncapsulation, syslogOperationsStatus=syslogOperationsStatus, syslogReadOnlyCompliance1=syslogReadOnlyCompliance1, syslogFullCompliance1=syslogFullCompliance1, syslogStatusChanged=syslogStatusChanged, syslogControlTable=syslogControlTable, syslogObjects=syslogObjects, syslogControlDescr=syslogControlDescr, syslogOperationsGroup=syslogOperationsGroup, syslogControlBindAddr=syslogControlBindAddr, PYSNMP_MODULE_ID=syslogMIBR, syslogOperationsLastErrorTime=syslogOperationsLastErrorTime, syslogControlEntry=syslogControlEntry, syslogControlService=syslogControlService, syslogOperationsStartTime=syslogOperationsStartTime, syslogMIBR=syslogMIBR, syslogOperationsTable=syslogOperationsTable, syslogOperationsMsgsRelayed=syslogOperationsMsgsRelayed, syslogConformance=syslogConformance, syslogNotificationCompliance=syslogNotificationCompliance, syslogOperationsLastMsgRecdTime=syslogOperationsLastMsgRecdTime, syslogGroups=syslogGroups, syslogOperationsMsgsDiscarded=syslogOperationsMsgsDiscarded, syslogOperationsRunIndex=syslogOperationsRunIndex, syslogControlAccountingType=syslogControlAccountingType, syslogCompliances=syslogCompliances, syslogOperationsMsgsDropped=syslogOperationsMsgsDropped, syslogControlMaxMessageSize=syslogControlMaxMessageSize, SyslogRoles=SyslogRoles, syslogControlRowStatus=syslogControlRowStatus, syslogControlGroup=syslogControlGroup, syslogDefaultEncapsulation=syslogDefaultEncapsulation)
