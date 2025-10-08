#
# PySNMP MIB module CIENA-CES-CONFIG-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-CES-CONFIG-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity")
cienaCesNotifications, cienaCesConfig = mibBuilder.importSymbols("CIENA-SMI", "cienaCesNotifications", "cienaCesConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CIENA-CES-CONFIG-MGMT-MIB", PYSNMP_MODULE_ID=cienaCesConfigMgmtMIB, cienaCesConfigMgmt=cienaCesConfigMgmt, cienaCesConfigMgmtMIBNotificationsPrefix=cienaCesConfigMgmtMIBNotificationsPrefix, cienaCesConfigMgmtMIBGroups=cienaCesConfigMgmtMIBGroups, cienaCesConfigMgmtMIB=cienaCesConfigMgmtMIB, cienaCesConfigMgmtConfigSavedNotification=cienaCesConfigMgmtConfigSavedNotification, cienaCesConfigMgmtMIBNotifications=cienaCesConfigMgmtMIBNotifications, cienaCesConfigMgmtMIBCompliances=cienaCesConfigMgmtMIBCompliances, CienaCesConfigMgmtContext=CienaCesConfigMgmtContext, cienaCesConfigMgmtConfigLastOrigin=cienaCesConfigMgmtConfigLastOrigin, cienaCesConfigMgmtConfigLastContext=cienaCesConfigMgmtConfigLastContext, cienaCesConfigMgmtConfigLastUser=cienaCesConfigMgmtConfigLastUser, cienaCesConfigMgmtConfigChangeNotification=cienaCesConfigMgmtConfigChangeNotification, cienaCesConfigMgmtMIBConformance=cienaCesConfigMgmtMIBConformance, cienaCesConfigMgmtConfigLastChanged=cienaCesConfigMgmtConfigLastChanged, cienaCesConfigMgmtConfigLastSaved=cienaCesConfigMgmtConfigLastSaved, cienaCesConfigMgmtMIBObjects=cienaCesConfigMgmtMIBObjects)
