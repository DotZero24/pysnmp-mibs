#
# PySNMP MIB module CIENA-CES-SYSTEM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-CES-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaGlobalSeverity, cienaGlobalMacAddress = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity", "cienaGlobalMacAddress")
cienaCesConfig, cienaCesNotifications = mibBuilder.importSymbols("CIENA-SMI", "cienaCesConfig", "cienaCesNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaCesSystemConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14))
cienaCesSystemConfigMIB.setRevisions(('2017-06-07 00:00', '2016-10-28 00:00', '2010-05-10 00:00',))
if mibBuilder.loadTexts: cienaCesSystemConfigMIB.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaCesSystemConfigMIB.setOrganization('Ciena Corp.')
class FileName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

cienaCesSystemConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1))
cienaCesSystemConfigNotifAttrs = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1))
cienaCesSystemConfigMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 14))
cienaCesSystemConfigMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0))
cienaCesSystemConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 3))
cienaCesSystemConfigCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 3, 1))
cienaCesSystemConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 3, 2))
cienaCesSystemConfigFileName = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 1), FileName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesSystemConfigFileName.setStatus('current')
cienaCesSystemConfigErrLineNum = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesSystemConfigErrLineNum.setStatus('current')
cienaCesSystemConfigErrStr = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesSystemConfigErrStr.setStatus('current')
cienaCesSystemConfigErrLinesTotal = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesSystemConfigErrLinesTotal.setStatus('current')
cienaCesCommandFileHost = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesCommandFileHost.setStatus('current')
cienaCesCommandFileName = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 6), FileName()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesCommandFileName.setStatus('current')
cienaCesCommandFileError = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 14, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaCesCommandFileError.setStatus('current')
cienaCesImproperCmdInConfigFile = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0, 1)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesSystemConfigFileName"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesSystemConfigErrLinesTotal"))
if mibBuilder.loadTexts: cienaCesImproperCmdInConfigFile.setStatus('current')
cienaCesCommandFileCompletedNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0, 2)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileHost"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileName"))
if mibBuilder.loadTexts: cienaCesCommandFileCompletedNotification.setStatus('current')
cienaCesCommandFileFailedNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 14, 0, 3)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileHost"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileName"), ("CIENA-CES-SYSTEM-CONFIG-MIB", "cienaCesCommandFileError"))
if mibBuilder.loadTexts: cienaCesCommandFileFailedNotification.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-SYSTEM-CONFIG-MIB", cienaCesCommandFileFailedNotification=cienaCesCommandFileFailedNotification, cienaCesImproperCmdInConfigFile=cienaCesImproperCmdInConfigFile, cienaCesSystemConfigFileName=cienaCesSystemConfigFileName, cienaCesSystemConfigCompliances=cienaCesSystemConfigCompliances, cienaCesCommandFileError=cienaCesCommandFileError, FileName=FileName, cienaCesSystemConfigErrStr=cienaCesSystemConfigErrStr, cienaCesSystemConfigErrLinesTotal=cienaCesSystemConfigErrLinesTotal, cienaCesSystemConfigMIBNotificationPrefix=cienaCesSystemConfigMIBNotificationPrefix, cienaCesSystemConfigErrLineNum=cienaCesSystemConfigErrLineNum, PYSNMP_MODULE_ID=cienaCesSystemConfigMIB, cienaCesCommandFileCompletedNotification=cienaCesCommandFileCompletedNotification, cienaCesSystemConfigNotifAttrs=cienaCesSystemConfigNotifAttrs, cienaCesSystemConfigMIB=cienaCesSystemConfigMIB, cienaCesSystemConfigMIBGroups=cienaCesSystemConfigMIBGroups, cienaCesCommandFileHost=cienaCesCommandFileHost, cienaCesSystemConfigMIBNotifications=cienaCesSystemConfigMIBNotifications, cienaCesSystemConfigMIBConformance=cienaCesSystemConfigMIBConformance, cienaCesSystemConfigMIBObjects=cienaCesSystemConfigMIBObjects, cienaCesCommandFileName=cienaCesCommandFileName)
