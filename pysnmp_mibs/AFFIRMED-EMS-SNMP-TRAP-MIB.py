#
# PySNMP MIB module AFFIRMED-EMS-SNMP-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/microsoft/AFFIRMED-EMS-SNMP-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
affirmedAlarmChassisName, affirmedAlarmDetails, affirmedAlarmSeverity, affirmedAlarmSeqId, affirmedAlarmRefSeqId, affirmedAlarmSourceId, affirmedAlarmDateTime = mibBuilder.importSymbols("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName", "affirmedAlarmDetails", "affirmedAlarmSeverity", "affirmedAlarmSeqId", "affirmedAlarmRefSeqId", "affirmedAlarmSourceId", "affirmedAlarmDateTime")
affirmedSnmpNotifications, affirmedSnmp = mibBuilder.importSymbols("AFFIRMED-SNMP-MIB", "affirmedSnmpNotifications", "affirmedSnmp")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
affirmedSnmpTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5))
if mibBuilder.loadTexts: affirmedSnmpTraps.setLastUpdated('201105160000Z')
if mibBuilder.loadTexts: affirmedSnmpTraps.setOrganization('Affired Networks, Inc.')
affirmedSnmpTrapsScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 1))
affirmedSnmpTrapsTables = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 2))
affirmedSnmpTrapsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3))
affirmedSnmpTrapsNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 0))
affirmedSnmpTrapsNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 1))
emsDBReplicationDown = NotificationType((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 0, 1)).setObjects(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"))
if mibBuilder.loadTexts: emsDBReplicationDown.setStatus('current')
emsDBReplicationLagBehind = NotificationType((1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 0, 2)).setObjects(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"), ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"))
if mibBuilder.loadTexts: emsDBReplicationLagBehind.setStatus('current')
mibBuilder.exportSymbols("AFFIRMED-EMS-SNMP-TRAP-MIB", emsDBReplicationLagBehind=emsDBReplicationLagBehind, emsDBReplicationDown=emsDBReplicationDown, PYSNMP_MODULE_ID=affirmedSnmpTraps, affirmedSnmpTrapsNotificationObjects=affirmedSnmpTrapsNotificationObjects, affirmedSnmpTrapsNotificationPrefix=affirmedSnmpTrapsNotificationPrefix, affirmedSnmpTraps=affirmedSnmpTraps, affirmedSnmpTrapsTables=affirmedSnmpTrapsTables, affirmedSnmpTrapsNotifications=affirmedSnmpTrapsNotifications, affirmedSnmpTrapsScalars=affirmedSnmpTrapsScalars)
