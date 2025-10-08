#
# PySNMP MIB module RBN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-DS1-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
RbnAlarmServiceAffecting, RbnAlarmPerceivedSeverity = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmServiceAffecting", "RbnAlarmPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnDS1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 37))
rbnDS1MIB.setRevisions(('2005-05-09 00:00',))
if mibBuilder.loadTexts: rbnDS1MIB.setLastUpdated('200505090000Z')
if mibBuilder.loadTexts: rbnDS1MIB.setOrganization('RedBack Networks, Inc.')
rbnDs1MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1))
rbnDsx1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1), )
if mibBuilder.loadTexts: rbnDsx1ConfigTable.setStatus('current')
rbnDsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("RBN-DS1-MIB", "rbnDsx1ConfigEntry"))
rbnDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: rbnDsx1ConfigEntry.setStatus('current')
rbnDsx1AlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 1), RbnAlarmPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx1AlarmSeverity.setStatus('current')
rbnDsx1AlarmServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 37, 1, 1, 1, 2), RbnAlarmServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnDsx1AlarmServiceAffecting.setStatus('current')
rbnDs1MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2))
rbnDs1MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1))
rbnDs1MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2))
rbnDs1MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 2, 1)).setObjects(("RBN-DS1-MIB", "rbnDs1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs1MIBCompliance = rbnDs1MIBCompliance.setStatus('current')
rbnDs1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 37, 2, 1, 1)).setObjects(("RBN-DS1-MIB", "rbnDsx1AlarmSeverity"), ("RBN-DS1-MIB", "rbnDsx1AlarmServiceAffecting"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnDs1Group = rbnDs1Group.setStatus('current')
mibBuilder.exportSymbols("RBN-DS1-MIB", rbnDsx1ConfigTable=rbnDsx1ConfigTable, rbnDsx1AlarmSeverity=rbnDsx1AlarmSeverity, rbnDsx1AlarmServiceAffecting=rbnDsx1AlarmServiceAffecting, rbnDs1MIBGroups=rbnDs1MIBGroups, rbnDS1MIB=rbnDS1MIB, rbnDs1Group=rbnDs1Group, rbnDsx1ConfigEntry=rbnDsx1ConfigEntry, rbnDs1MIBConformance=rbnDs1MIBConformance, PYSNMP_MODULE_ID=rbnDS1MIB, rbnDs1MIBCompliances=rbnDs1MIBCompliances, rbnDs1MIBCompliance=rbnDs1MIBCompliance, rbnDs1MIBObjects=rbnDs1MIBObjects)
