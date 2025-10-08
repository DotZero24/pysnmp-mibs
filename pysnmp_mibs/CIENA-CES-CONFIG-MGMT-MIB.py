#
# PySNMP MIB module CIENA-CES-CONFIG-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-CES-CONFIG-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity")
cienaCesConfig, cienaCesNotifications = mibBuilder.importSymbols("CIENA-SMI", "cienaCesConfig", "cienaCesNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
cienaCesConfigMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36))
cienaCesConfigMgmtMIB.setRevisions(('2017-06-07 00:00', '2015-02-11 00:00',))
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setOrganization('Ciena Corp.')
class CienaCesConfigMgmtContext(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("cli", 2), ("snmp", 3), ("netconf", 4))

cienaCesConfigMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1))
cienaCesConfigMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1))
cienaCesConfigMgmtMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36))
cienaCesConfigMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0))
cienaCesConfigMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2))
cienaCesConfigMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 1))
cienaCesConfigMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 2))
cienaCesConfigMgmtConfigLastSaved = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastSaved.setStatus('current')
cienaCesConfigMgmtConfigLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastChanged.setStatus('current')
cienaCesConfigMgmtConfigLastContext = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 3), CienaCesConfigMgmtContext()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastContext.setStatus('current')
cienaCesConfigMgmtConfigLastUser = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastUser.setStatus('current')
cienaCesConfigMgmtConfigLastOrigin = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastOrigin.setStatus('current')
cienaCesConfigMgmtConfigSavedNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 1)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastSaved"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigSavedNotification.setStatus('current')
cienaCesConfigMgmtConfigChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 2)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastContext"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastUser"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastOrigin"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigChangeNotification.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-CONFIG-MGMT-MIB", cienaCesConfigMgmtMIBConformance=cienaCesConfigMgmtMIBConformance, cienaCesConfigMgmtConfigSavedNotification=cienaCesConfigMgmtConfigSavedNotification, cienaCesConfigMgmtConfigLastChanged=cienaCesConfigMgmtConfigLastChanged, PYSNMP_MODULE_ID=cienaCesConfigMgmtMIB, cienaCesConfigMgmtMIBCompliances=cienaCesConfigMgmtMIBCompliances, cienaCesConfigMgmtMIBObjects=cienaCesConfigMgmtMIBObjects, cienaCesConfigMgmtMIBNotifications=cienaCesConfigMgmtMIBNotifications, cienaCesConfigMgmtConfigLastUser=cienaCesConfigMgmtConfigLastUser, cienaCesConfigMgmtConfigChangeNotification=cienaCesConfigMgmtConfigChangeNotification, cienaCesConfigMgmtMIB=cienaCesConfigMgmtMIB, cienaCesConfigMgmtConfigLastContext=cienaCesConfigMgmtConfigLastContext, cienaCesConfigMgmtMIBGroups=cienaCesConfigMgmtMIBGroups, cienaCesConfigMgmtMIBNotificationsPrefix=cienaCesConfigMgmtMIBNotificationsPrefix, cienaCesConfigMgmtConfigLastOrigin=cienaCesConfigMgmtConfigLastOrigin, cienaCesConfigMgmtConfigLastSaved=cienaCesConfigMgmtConfigLastSaved, cienaCesConfigMgmt=cienaCesConfigMgmt, CienaCesConfigMgmtContext=CienaCesConfigMgmtContext)
