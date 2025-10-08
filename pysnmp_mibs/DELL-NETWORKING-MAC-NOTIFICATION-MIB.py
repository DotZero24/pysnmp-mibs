#
# PySNMP MIB module DELL-NETWORKING-MAC-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-MAC-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
dellNetMacNotifMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 28))
dellNetMacNotifMib.setRevisions(('2017-01-01 12:00',))
if mibBuilder.loadTexts: dellNetMacNotifMib.setLastUpdated('201701011200Z')
if mibBuilder.loadTexts: dellNetMacNotifMib.setOrganization('Dell Inc')
dellNetMacNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1))
dellNetMacNotificationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 1))
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: macAddress.setStatus('current')
vlanId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 3), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vlanId.setStatus('current')
portId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: portId.setStatus('current')
newPortId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: newPortId.setStatus('current')
timeStamp = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 6), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: timeStamp.setStatus('current')
message = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 7), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: message.setStatus('current')
macLearnNotification = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 1, 1)).setObjects(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macAddress"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "vlanId"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "portId"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "timeStamp"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "message"))
if mibBuilder.loadTexts: macLearnNotification.setStatus('current')
macMoveNotification = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 1, 2)).setObjects(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macAddress"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "vlanId"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "portId"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "newPortId"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "timeStamp"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "message"))
if mibBuilder.loadTexts: macMoveNotification.setStatus('current')
dellNetMacMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 28, 2))
dellNetMacMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 1))
dellNetMacMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 2))
dellNetMacMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 1, 1)).setObjects(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "dellNetMacNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetMacMibCompliance = dellNetMacMibCompliance.setStatus('current')
dellNetMacNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 2, 1)).setObjects(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macLearnNotification"), ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macMoveNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetMacNotificationGroup = dellNetMacNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-MAC-NOTIFICATION-MIB", dellNetMacNotificationGroup=dellNetMacNotificationGroup, dellNetMacNotificationTraps=dellNetMacNotificationTraps, portId=portId, dellNetMacMibCompliance=dellNetMacMibCompliance, macMoveNotification=macMoveNotification, macLearnNotification=macLearnNotification, newPortId=newPortId, dellNetMacNotificationObjects=dellNetMacNotificationObjects, vlanId=vlanId, dellNetMacMibCompliances=dellNetMacMibCompliances, macAddress=macAddress, dellNetMacMibConformance=dellNetMacMibConformance, timeStamp=timeStamp, message=message, dellNetMacNotifMib=dellNetMacNotifMib, dellNetMacMibGroups=dellNetMacMibGroups, PYSNMP_MODULE_ID=dellNetMacNotifMib)
