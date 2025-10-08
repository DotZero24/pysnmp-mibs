#
# PySNMP MIB module CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/CONFIG-COPY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
mgmt, = mibBuilder.importSymbols("ZXR10-SMI", "mgmt")
configCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1))
configCopyMIB.setRevisions(('2007-02-01 00:00',))
if mibBuilder.loadTexts: configCopyMIB.setLastUpdated('200702010000Z')
if mibBuilder.loadTexts: configCopyMIB.setOrganization('ZTE Corp.')
class ConfigCopyProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tftp", 1), ("ftp", 2))

class ConfigCopyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("waiting", 1), ("running", 2), ("successful", 3), ("failed", 4))

class ConfigCopyFailCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("badFileName", 2), ("timeout", 3), ("noMem", 4), ("noConfig", 5), ("unsupportedProtocol", 6), ("someConfigApplyFailed", 7))

class ConfigFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("networkFile", 1), ("localFile", 2), ("startupConfig", 3), ("runningConfig", 4))

configCopyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1))
copy = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1))
copyTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1), )
if mibBuilder.loadTexts: copyTable.setStatus('current')
copyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1), ).setIndexNames((0, "CONFIG-COPY-MIB", "copyIndex"))
if mibBuilder.loadTexts: copyEntry.setStatus('current')
copyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: copyIndex.setStatus('current')
copyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 2), ConfigCopyProtocol().clone('ftp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyProtocol.setStatus('current')
copySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 3), ConfigFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copySourceFileType.setStatus('current')
copyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 4), ConfigFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyDestFileType.setStatus('current')
copyServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyServerAddress.setStatus('current')
copySrcFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copySrcFileName.setStatus('current')
copyDstFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyDstFileName.setStatus('current')
copyUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyUserName.setStatus('current')
copyUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyUserPassword.setStatus('current')
copyNotificationOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyNotificationOnCompletion.setStatus('current')
copyState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 11), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copyState.setStatus('current')
copyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copyTimeStarted.setStatus('current')
copyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copyTimeCompleted.setStatus('current')
copyFailCause = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 14), ConfigCopyFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copyFailCause.setStatus('current')
copyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copyEntryRowStatus.setStatus('current')
configCopyMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 2))
copyMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 2, 1))
copyCompletion = NotificationType((1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 2, 1, 1)).setObjects(("CONFIG-COPY-MIB", "copyServerAddress"), ("CONFIG-COPY-MIB", "copySrcFileName"), ("CONFIG-COPY-MIB", "copyState"), ("CONFIG-COPY-MIB", "copyTimeStarted"), ("CONFIG-COPY-MIB", "copyTimeCompleted"), ("CONFIG-COPY-MIB", "copyFailCause"))
if mibBuilder.loadTexts: copyCompletion.setStatus('current')
mibBuilder.exportSymbols("CONFIG-COPY-MIB", copyTimeStarted=copyTimeStarted, copyFailCause=copyFailCause, copyState=copyState, copyNotificationOnCompletion=copyNotificationOnCompletion, ConfigFileType=ConfigFileType, copyMIBTraps=copyMIBTraps, configCopyMIB=configCopyMIB, copyTable=copyTable, copyUserName=copyUserName, configCopyMIBTrapPrefix=configCopyMIBTrapPrefix, PYSNMP_MODULE_ID=configCopyMIB, copyEntry=copyEntry, copySrcFileName=copySrcFileName, configCopyMIBObjects=configCopyMIBObjects, copy=copy, ConfigCopyProtocol=ConfigCopyProtocol, copySourceFileType=copySourceFileType, copyUserPassword=copyUserPassword, copyProtocol=copyProtocol, copyIndex=copyIndex, copyTimeCompleted=copyTimeCompleted, copyServerAddress=copyServerAddress, copyCompletion=copyCompletion, copyDstFileName=copyDstFileName, copyDestFileType=copyDestFileType, ConfigCopyFailCause=ConfigCopyFailCause, ConfigCopyState=ConfigCopyState, copyEntryRowStatus=copyEntryRowStatus)
