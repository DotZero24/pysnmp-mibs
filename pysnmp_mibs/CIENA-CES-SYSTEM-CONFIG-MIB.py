#
# PySNMP MIB module CIENA-CES-SYSTEM-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-CES-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaGlobalMacAddress, cienaGlobalSeverity = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress", "cienaGlobalSeverity")
cienaCesNotifications, cienaCesConfig = mibBuilder.importSymbols("CIENA-SMI", "cienaCesNotifications", "cienaCesConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CIENA-CES-SYSTEM-CONFIG-MIB", cienaCesSystemConfigMIB=cienaCesSystemConfigMIB, cienaCesCommandFileHost=cienaCesCommandFileHost, cienaCesSystemConfigMIBConformance=cienaCesSystemConfigMIBConformance, cienaCesCommandFileFailedNotification=cienaCesCommandFileFailedNotification, cienaCesSystemConfigFileName=cienaCesSystemConfigFileName, FileName=FileName, cienaCesSystemConfigErrStr=cienaCesSystemConfigErrStr, cienaCesCommandFileCompletedNotification=cienaCesCommandFileCompletedNotification, PYSNMP_MODULE_ID=cienaCesSystemConfigMIB, cienaCesCommandFileName=cienaCesCommandFileName, cienaCesSystemConfigNotifAttrs=cienaCesSystemConfigNotifAttrs, cienaCesSystemConfigMIBNotificationPrefix=cienaCesSystemConfigMIBNotificationPrefix, cienaCesSystemConfigMIBObjects=cienaCesSystemConfigMIBObjects, cienaCesSystemConfigErrLineNum=cienaCesSystemConfigErrLineNum, cienaCesSystemConfigMIBNotifications=cienaCesSystemConfigMIBNotifications, cienaCesSystemConfigMIBGroups=cienaCesSystemConfigMIBGroups, cienaCesSystemConfigErrLinesTotal=cienaCesSystemConfigErrLinesTotal, cienaCesSystemConfigCompliances=cienaCesSystemConfigCompliances, cienaCesImproperCmdInConfigFile=cienaCesImproperCmdInConfigFile, cienaCesCommandFileError=cienaCesCommandFileError)
