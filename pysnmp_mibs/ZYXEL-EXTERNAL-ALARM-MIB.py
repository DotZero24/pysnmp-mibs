#
# PySNMP MIB module ZYXEL-EXTERNAL-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-EXTERNAL-ALARM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-EXTERNAL-ALARM-MIB", zyExternalAlarmTrapAlarmId=zyExternalAlarmTrapAlarmId, zyExternalAlarmDetect=zyExternalAlarmDetect, zyxelExternalAlarmNotifications=zyxelExternalAlarmNotifications, PYSNMP_MODULE_ID=zyxelExternalAlarm, zyxelExternalAlarmTrapInfoObjects=zyxelExternalAlarmTrapInfoObjects, zyxelExternalAlarm=zyxelExternalAlarm)
