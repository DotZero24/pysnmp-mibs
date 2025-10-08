#
# PySNMP MIB module RBN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-DS1-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
RbnAlarmPerceivedSeverity, RbnAlarmServiceAffecting = mibBuilder.importSymbols("RBN-ALARM-TC", "RbnAlarmPerceivedSeverity", "RbnAlarmServiceAffecting")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RBN-DS1-MIB", rbnDs1MIBObjects=rbnDs1MIBObjects, rbnDs1MIBCompliance=rbnDs1MIBCompliance, rbnDs1MIBGroups=rbnDs1MIBGroups, rbnDsx1ConfigEntry=rbnDsx1ConfigEntry, rbnDs1MIBConformance=rbnDs1MIBConformance, rbnDsx1ConfigTable=rbnDsx1ConfigTable, rbnDsx1AlarmServiceAffecting=rbnDsx1AlarmServiceAffecting, rbnDS1MIB=rbnDS1MIB, rbnDs1Group=rbnDs1Group, PYSNMP_MODULE_ID=rbnDS1MIB, rbnDsx1AlarmSeverity=rbnDsx1AlarmSeverity, rbnDs1MIBCompliances=rbnDs1MIBCompliances)
