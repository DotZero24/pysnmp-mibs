#
# PySNMP MIB module ARUBAWIRED-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBAWIRED-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
arubaWiredConfigurationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20))
arubaWiredConfigurationMIB.setRevisions(('2021-08-10 00:00',))
if mibBuilder.loadTexts: arubaWiredConfigurationMIB.setLastUpdated('202108100000Z')
if mibBuilder.loadTexts: arubaWiredConfigurationMIB.setOrganization('HPE/Aruba Networking Division')
arubaWiredConfigurationNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 0))
arubaWiredConfigurationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1))
arubaWiredConfigurationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2))
class ConfigurationEventMedium(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("checkpoint", 1), ("cli", 2), ("internal", 3), ("rest", 4), ("snmp", 5), ("ztp", 6))

class ConfigurationCopyProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("scp", 1), ("sftp", 2), ("tftp", 3))

class ConfigurationCopyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("waiting", 1), ("running", 2), ("successful", 3), ("failed", 4))

class ConfigurationCopyFailureCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("authenticationFailed", 1), ("badFilename", 2), ("busy", 3), ("invalidConfiguration", 4), ("invalidURL", 5), ("systemNotReady", 6), ("timeout", 7), ("unknown", 8))

class ConfigurationFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("externalFile", 1), ("startupConfiguration", 2), ("runningConfiguration", 3), ("checkpoint", 4))

class ConfigurationFileFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cli", 1), ("json", 2))

arubaWiredConfigurationCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0))
arubaWiredConfigurationCopyTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1), )
if mibBuilder.loadTexts: arubaWiredConfigurationCopyTable.setStatus('current')
arubaWiredConfigurationCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1), ).setIndexNames((0, "ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyIndex"))
if mibBuilder.loadTexts: arubaWiredConfigurationCopyEntry.setStatus('current')
arubaWiredConfigurationCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: arubaWiredConfigurationCopyIndex.setStatus('current')
arubaWiredConfigurationCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 2), ConfigurationFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopySourceFileType.setStatus('current')
arubaWiredConfigurationCopyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 3), ConfigurationFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyDestFileType.setStatus('current')
arubaWiredConfigurationCopyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 4), ConfigurationCopyProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyProtocol.setStatus('current')
arubaWiredConfigurationCheckpointName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCheckpointName.setStatus('current')
arubaWiredConfigurationCopyFileFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 6), ConfigurationFileFormat()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyFileFormat.setStatus('current')
arubaWiredConfigurationCopyFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyFileName.setStatus('current')
arubaWiredConfigurationCopyServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 8), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyServerAddressType.setStatus('current')
arubaWiredConfigurationCopyServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 9), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyServerAddress.setStatus('current')
arubaWiredConfigurationCopyUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyUserName.setStatus('current')
arubaWiredConfigurationCopyUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyUserPassword.setStatus('current')
arubaWiredConfigurationCopyVRFName = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 12), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyVRFName.setStatus('current')
arubaWiredConfigurationCopyNotificationOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyNotificationOnCompletion.setStatus('current')
arubaWiredConfigurationCopyState = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 14), ConfigurationCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyState.setStatus('current')
arubaWiredConfigurationCopyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyTimeStarted.setStatus('current')
arubaWiredConfigurationCopyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyTimeCompleted.setStatus('current')
arubaWiredConfigurationCopyFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 17), ConfigurationCopyFailureCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyFailureCause.setStatus('current')
arubaWiredConfigurationCopyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 0, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arubaWiredConfigurationCopyEntryRowStatus.setStatus('current')
arubaWiredConfigurationChange = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1))
arubaWiredConfigurationChangeNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredConfigurationChangeNotificationEnable.setStatus('current')
arubaWiredConfigurationChangeSource = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1, 2), ConfigurationEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredConfigurationChangeSource.setStatus('current')
arubaWiredConfigurationChangeTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredConfigurationChangeTimestamp.setStatus('current')
arubaWiredConfigurationChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 0, 1)).setObjects(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeSource"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeTimestamp"))
if mibBuilder.loadTexts: arubaWiredConfigurationChangeNotification.setStatus('current')
arubaWiredConfigurationNotificationOnCompletion = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 0, 2)).setObjects(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyServerAddress"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFileName"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyState"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeStarted"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeCompleted"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFailureCause"))
if mibBuilder.loadTexts: arubaWiredConfigurationNotificationOnCompletion.setStatus('current')
arubaWiredConfigurationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 1))
arubaWiredConfigurationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2))
arubaWiredConfigurationScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2, 1)).setObjects(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeNotificationEnable"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeSource"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredConfigurationScalarGroup = arubaWiredConfigurationScalarGroup.setStatus('current')
arubaWiredConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2, 2)).setObjects(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyProtocol"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopySourceFileType"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyDestFileType"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCheckpointName"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFileFormat"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFileName"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyServerAddressType"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyServerAddress"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyUserName"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyUserPassword"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyVRFName"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyNotificationOnCompletion"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyState"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeStarted"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyTimeCompleted"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyFailureCause"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationCopyEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredConfigurationGroup = arubaWiredConfigurationGroup.setStatus('current')
arubaWiredConfigurationNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 2, 3)).setObjects(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationChangeNotification"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationNotificationOnCompletion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredConfigurationNotificationsGroup = arubaWiredConfigurationNotificationsGroup.setStatus('current')
arubaWiredConfigurationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20, 2, 1, 1)).setObjects(("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationScalarGroup"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationGroup"), ("ARUBAWIRED-CONFIG-MIB", "arubaWiredConfigurationNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredConfigurationCompliance = arubaWiredConfigurationCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-CONFIG-MIB", arubaWiredConfigurationCopy=arubaWiredConfigurationCopy, arubaWiredConfigurationChangeNotification=arubaWiredConfigurationChangeNotification, arubaWiredConfigurationMIB=arubaWiredConfigurationMIB, arubaWiredConfigurationCopyProtocol=arubaWiredConfigurationCopyProtocol, arubaWiredConfigurationCopyTable=arubaWiredConfigurationCopyTable, arubaWiredConfigurationCopyUserPassword=arubaWiredConfigurationCopyUserPassword, arubaWiredConfigurationGroups=arubaWiredConfigurationGroups, arubaWiredConfigurationGroup=arubaWiredConfigurationGroup, arubaWiredConfigurationCopyTimeCompleted=arubaWiredConfigurationCopyTimeCompleted, ConfigurationEventMedium=ConfigurationEventMedium, arubaWiredConfigurationCopyTimeStarted=arubaWiredConfigurationCopyTimeStarted, arubaWiredConfigurationCopyServerAddress=arubaWiredConfigurationCopyServerAddress, arubaWiredConfigurationCopyFileName=arubaWiredConfigurationCopyFileName, arubaWiredConfigurationCompliances=arubaWiredConfigurationCompliances, arubaWiredConfigurationCopyFailureCause=arubaWiredConfigurationCopyFailureCause, arubaWiredConfigurationCompliance=arubaWiredConfigurationCompliance, arubaWiredConfigurationConformance=arubaWiredConfigurationConformance, arubaWiredConfigurationObjects=arubaWiredConfigurationObjects, ConfigurationFileFormat=ConfigurationFileFormat, arubaWiredConfigurationChangeSource=arubaWiredConfigurationChangeSource, arubaWiredConfigurationCopySourceFileType=arubaWiredConfigurationCopySourceFileType, arubaWiredConfigurationNotificationOnCompletion=arubaWiredConfigurationNotificationOnCompletion, PYSNMP_MODULE_ID=arubaWiredConfigurationMIB, arubaWiredConfigurationCopyIndex=arubaWiredConfigurationCopyIndex, arubaWiredConfigurationNotificationsGroup=arubaWiredConfigurationNotificationsGroup, arubaWiredConfigurationCopyEntryRowStatus=arubaWiredConfigurationCopyEntryRowStatus, ConfigurationCopyFailureCause=ConfigurationCopyFailureCause, arubaWiredConfigurationCopyState=arubaWiredConfigurationCopyState, ConfigurationFileType=ConfigurationFileType, ConfigurationCopyState=ConfigurationCopyState, ConfigurationCopyProtocol=ConfigurationCopyProtocol, arubaWiredConfigurationCopyNotificationOnCompletion=arubaWiredConfigurationCopyNotificationOnCompletion, arubaWiredConfigurationScalarGroup=arubaWiredConfigurationScalarGroup, arubaWiredConfigurationCopyDestFileType=arubaWiredConfigurationCopyDestFileType, arubaWiredConfigurationCopyServerAddressType=arubaWiredConfigurationCopyServerAddressType, arubaWiredConfigurationCopyUserName=arubaWiredConfigurationCopyUserName, arubaWiredConfigurationCopyEntry=arubaWiredConfigurationCopyEntry, arubaWiredConfigurationCopyVRFName=arubaWiredConfigurationCopyVRFName, arubaWiredConfigurationChangeTimestamp=arubaWiredConfigurationChangeTimestamp, arubaWiredConfigurationCheckpointName=arubaWiredConfigurationCheckpointName, arubaWiredConfigurationChangeNotificationEnable=arubaWiredConfigurationChangeNotificationEnable, arubaWiredConfigurationCopyFileFormat=arubaWiredConfigurationCopyFileFormat, arubaWiredConfigurationChange=arubaWiredConfigurationChange, arubaWiredConfigurationNotifications=arubaWiredConfigurationNotifications)
