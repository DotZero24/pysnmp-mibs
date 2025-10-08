#
# PySNMP MIB module AFFIRMED-EMS-SNMP-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/microsoft/AFFIRMED-EMS-SNMP-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
affirmedAlarmDetails, affirmedAlarmSeqId, affirmedAlarmChassisName, affirmedAlarmSeverity, affirmedAlarmDateTime, affirmedAlarmRefSeqId, affirmedAlarmSourceId = mibBuilder.importSymbols("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails", "affirmedAlarmSeqId", "affirmedAlarmChassisName", "affirmedAlarmSeverity", "affirmedAlarmDateTime", "affirmedAlarmRefSeqId", "affirmedAlarmSourceId")
affirmedSnmp, affirmedSnmpNotifications = mibBuilder.importSymbols("AFFIRMED-SNMP-MIB", "affirmedSnmp", "affirmedSnmpNotifications")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AFFIRMED-EMS-SNMP-TRAP-MIB", affirmedSnmpTrapsScalars=affirmedSnmpTrapsScalars, affirmedSnmpTrapsNotificationObjects=affirmedSnmpTrapsNotificationObjects, PYSNMP_MODULE_ID=affirmedSnmpTraps, emsDBReplicationLagBehind=emsDBReplicationLagBehind, emsDBReplicationDown=emsDBReplicationDown, affirmedSnmpTrapsNotifications=affirmedSnmpTrapsNotifications, affirmedSnmpTrapsNotificationPrefix=affirmedSnmpTrapsNotificationPrefix, affirmedSnmpTrapsTables=affirmedSnmpTrapsTables, affirmedSnmpTraps=affirmedSnmpTraps)
