#
# PySNMP MIB module TPT-NGFW-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-NGFW-USER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
tptNgfwNotifySeverity, tpt_ngfw_objs, tpt_ngfw_eventsV2, tpt_ngfw_groups, tpt_ngfw_compls, tpt_ngfw_params = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity", "tpt-ngfw-objs", "tpt-ngfw-eventsV2", "tpt-ngfw-groups", "tpt-ngfw-compls", "tpt-ngfw-params")
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
mibBuilder.exportSymbols("TPT-NGFW-USER-MIB", tptNgfwUserAuthSrcIpAddrType=tptNgfwUserAuthSrcIpAddrType, tptNgfwUserGroup=tptNgfwUserGroup, tptNgfwUserAuthNotifySource=tptNgfwUserAuthNotifySource, tptNgfwPolicy=tptNgfwPolicy, tptNgfwUserAuthLockedIpNotify=tptNgfwUserAuthLockedIpNotify, tptNgfwUserAuthLockedTime=tptNgfwUserAuthLockedTime, tptNgfwUserCompl=tptNgfwUserCompl, tptNgfwUserAuthFailNotifyReason=tptNgfwUserAuthFailNotifyReason, tptNgfwUserAuthName=tptNgfwUserAuthName, tptNgfwUserAuthSrcIpAddr=tptNgfwUserAuthSrcIpAddr, PYSNMP_MODULE_ID=tptNgfwPolicy, tptNgfwUserAuthFailNotify=tptNgfwUserAuthFailNotify, tptNgfwUserAuthLockedAccountNotify=tptNgfwUserAuthLockedAccountNotify, tptNgfwUserNotificationGroup=tptNgfwUserNotificationGroup)
