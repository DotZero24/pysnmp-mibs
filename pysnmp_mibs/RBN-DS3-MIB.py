#
# PySNMP MIB module RBN-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-DS3-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dsx3ConfigEntry, = mibBuilder.importSymbols("DS3-MIB", "dsx3ConfigEntry")
RbnAlarmServiceAffecting, RbnAlarmPerceivedSeverity = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmServiceAffecting", "RbnAlarmPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnDS3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 38))
rbnDS3MIB.setRevisions(('2005-05-09 00:00',))
if mibBuilder.loadTexts: rbnDS3MIB.setLastUpdated('200505090000Z')
if mibBuilder.loadTexts: rbnDS3MIB.setOrganization('RedBack Networks, Inc.')
rbnDs3MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1))
rbnDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1), )
if mibBuilder.loadTexts: rbnDsx3ConfigTable.setStatus('current')
rbnDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1), )
dsx3ConfigEntry.registerAugmentions(("RBN-DS3-MIB", "rbnDsx3ConfigEntry"))
rbnDsx3ConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: rbnDsx3ConfigEntry.setStatus('current')
rbnDsx3AlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 1), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx3AlarmSeverity.setStatus('current')
rbnDsx3AlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 38, 1, 1, 1, 2), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx3AlarmServiceAffecting.setStatus('current')
rbnDs3MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2))
rbnDs3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1))
rbnDs3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2))
rbnDs3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 2, 1)).setObjects(("RBN-DS3-MIB", "rbnDs3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs3MIBCompliance = rbnDs3MIBCompliance.setStatus('current')
rbnDs3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 38, 2, 1, 1)).setObjects(("RBN-DS3-MIB", "rbnDsx3AlarmSeverity"), ("RBN-DS3-MIB", "rbnDsx3AlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs3Group = rbnDs3Group.setStatus('current')
mibBuilder.exportSymbols("RBN-DS3-MIB", rbnDsx3ConfigEntry=rbnDsx3ConfigEntry, rbnDs3MIBGroups=rbnDs3MIBGroups, rbnDsx3AlarmServiceAffecting=rbnDsx3AlarmServiceAffecting, rbnDs3Group=rbnDs3Group, PYSNMP_MODULE_ID=rbnDS3MIB, rbnDs3MIBObjects=rbnDs3MIBObjects, rbnDs3MIBCompliance=rbnDs3MIBCompliance, rbnDs3MIBCompliances=rbnDs3MIBCompliances, rbnDsx3AlarmSeverity=rbnDsx3AlarmSeverity, rbnDs3MIBConformance=rbnDs3MIBConformance, rbnDS3MIB=rbnDS3MIB, rbnDsx3ConfigTable=rbnDsx3ConfigTable)
