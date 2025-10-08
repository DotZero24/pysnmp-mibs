#
# PySNMP MIB module ZYXEL-EXTERNAL-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-EXTERNAL-ALARM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelExternalAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25))
if mibBuilder.loadTexts: zyxelExternalAlarm.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelExternalAlarm.setOrganization('Enterprise Solution ZyXEL')
zyxelExternalAlarmTrapInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1))
zyxelExternalAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2))
zyExternalAlarmTrapAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyExternalAlarmTrapAlarmId.setStatus('current')
zyExternalAlarmDetect = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2, 1)).setObjects(("ZYXEL-EXTERNAL-ALARM-MIB", "zyExternalAlarmTrapAlarmId"))
if mibBuilder.loadTexts: zyExternalAlarmDetect.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-EXTERNAL-ALARM-MIB", zyxelExternalAlarmTrapInfoObjects=zyxelExternalAlarmTrapInfoObjects, zyExternalAlarmDetect=zyExternalAlarmDetect, PYSNMP_MODULE_ID=zyxelExternalAlarm, zyExternalAlarmTrapAlarmId=zyExternalAlarmTrapAlarmId, zyxelExternalAlarmNotifications=zyxelExternalAlarmNotifications, zyxelExternalAlarm=zyxelExternalAlarm)
