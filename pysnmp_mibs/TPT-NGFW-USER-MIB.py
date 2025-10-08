#
# PySNMP MIB module TPT-NGFW-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-NGFW-USER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
tpt_ngfw_groups, tptNgfwNotifySeverity, tpt_ngfw_objs, tpt_ngfw_params, tpt_ngfw_eventsV2, tpt_ngfw_compls = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tpt-ngfw-groups", "tptNgfwNotifySeverity", "tpt-ngfw-objs", "tpt-ngfw-params", "tpt-ngfw-eventsV2", "tpt-ngfw-compls")
tptNgfwSystemSerial, = mibBuilder.importSymbols("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial")
tptNgfwPolicy = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 4))
tptNgfwPolicy.setRevisions(('2016-05-25 18:54', '2013-04-03 12:00',))
if mibBuilder.loadTexts: tptNgfwPolicy.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tptNgfwPolicy.setOrganization('Trend Micro, Inc.')
tptNgfwUserAuthFailNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 18)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthName"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthFailNotifyReason"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthNotifySource"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwUserAuthFailNotify.setStatus('current')
tptNgfwUserAuthLockedAccountNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 19)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthName"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedTime"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthNotifySource"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwUserAuthLockedAccountNotify.setStatus('current')
tptNgfwUserAuthLockedIpNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 20)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedTime"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwUserAuthLockedIpNotify.setStatus('current')
tptNgfwUserAuthName = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 73), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwUserAuthName.setStatus('current')
tptNgfwUserAuthFailNotifyReason = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 74), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwUserAuthFailNotifyReason.setStatus('current')
tptNgfwUserAuthSrcIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 75), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwUserAuthSrcIpAddrType.setStatus('current')
tptNgfwUserAuthSrcIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 76), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwUserAuthSrcIpAddr.setStatus('current')
tptNgfwUserAuthNotifySource = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 77), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwUserAuthNotifySource.setStatus('current')
tptNgfwUserAuthLockedTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 78), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwUserAuthLockedTime.setStatus('current')
tptNgfwUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 11)).setObjects(("TPT-NGFW-USER-MIB", "tptNgfwUserAuthName"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthFailNotifyReason"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddrType"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthSrcIpAddr"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthNotifySource"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwUserGroup = tptNgfwUserGroup.setStatus('current')
tptNgfwUserNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 12)).setObjects(("TPT-NGFW-USER-MIB", "tptNgfwUserAuthFailNotify"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedAccountNotify"), ("TPT-NGFW-USER-MIB", "tptNgfwUserAuthLockedIpNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwUserNotificationGroup = tptNgfwUserNotificationGroup.setStatus('current')
tptNgfwUserCompl = ModuleCompliance((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 5)).setObjects(("TPT-NGFW-USER-MIB", "tptNgfwUserGroup"), ("TPT-NGFW-USER-MIB", "tptNgfwUserNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwUserCompl = tptNgfwUserCompl.setStatus('current')
mibBuilder.exportSymbols("TPT-NGFW-USER-MIB", tptNgfwUserAuthFailNotify=tptNgfwUserAuthFailNotify, tptNgfwUserAuthSrcIpAddr=tptNgfwUserAuthSrcIpAddr, tptNgfwUserAuthName=tptNgfwUserAuthName, tptNgfwUserCompl=tptNgfwUserCompl, tptNgfwUserNotificationGroup=tptNgfwUserNotificationGroup, tptNgfwUserAuthFailNotifyReason=tptNgfwUserAuthFailNotifyReason, tptNgfwUserAuthLockedIpNotify=tptNgfwUserAuthLockedIpNotify, PYSNMP_MODULE_ID=tptNgfwPolicy, tptNgfwUserAuthLockedTime=tptNgfwUserAuthLockedTime, tptNgfwUserAuthSrcIpAddrType=tptNgfwUserAuthSrcIpAddrType, tptNgfwUserGroup=tptNgfwUserGroup, tptNgfwPolicy=tptNgfwPolicy, tptNgfwUserAuthLockedAccountNotify=tptNgfwUserAuthLockedAccountNotify, tptNgfwUserAuthNotifySource=tptNgfwUserAuthNotifySource)
