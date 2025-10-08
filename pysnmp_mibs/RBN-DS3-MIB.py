#
# PySNMP MIB module RBN-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-DS3-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dsx3ConfigEntry, = mibBuilder.importSymbols("DS3-MIB", "dsx3ConfigEntry")
RbnAlarmPerceivedSeverity, RbnAlarmServiceAffecting = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmPerceivedSeverity", "RbnAlarmServiceAffecting")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RBN-DS3-MIB", PYSNMP_MODULE_ID=rbnDS3MIB, rbnDsx3ConfigEntry=rbnDsx3ConfigEntry, rbnDS3MIB=rbnDS3MIB, rbnDsx3AlarmSeverity=rbnDsx3AlarmSeverity, rbnDsx3AlarmServiceAffecting=rbnDsx3AlarmServiceAffecting, rbnDs3MIBConformance=rbnDs3MIBConformance, rbnDs3MIBCompliances=rbnDs3MIBCompliances, rbnDs3Group=rbnDs3Group, rbnDs3MIBGroups=rbnDs3MIBGroups, rbnDs3MIBObjects=rbnDs3MIBObjects, rbnDs3MIBCompliance=rbnDs3MIBCompliance, rbnDsx3ConfigTable=rbnDsx3ConfigTable)
