#
# PySNMP MIB module TPT-NGFW-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-NGFW-LOGGING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:27 2025
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
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
tpt_ngfw_groups, tpt_ngfw_objs, tpt_ngfw_params, tpt_ngfw_eventsV2, tpt_ngfw_compls, Severity = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tpt-ngfw-groups", "tpt-ngfw-objs", "tpt-ngfw-params", "tpt-ngfw-eventsV2", "tpt-ngfw-compls", "Severity")
tptNgfwSystemSerial, = mibBuilder.importSymbols("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial")
tptNgfwLogging = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 5))
tptNgfwLogging.setRevisions(('2016-05-25 18:54', '2013-03-13 12:00',))
if mibBuilder.loadTexts: tptNgfwLogging.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tptNgfwLogging.setOrganization('Trend Micro, Inc.')
class AuditLogResult(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("success", 1), ("failed", 2))

class AuditLogCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("undefined", 1), ("general", 2), ("login", 3), ("logout", 4), ("user", 5), ("time", 6), ("policy", 7), ("update", 8), ("boot", 9), ("report", 10), ("host", 11), ("cfg", 12), ("device", 13), ("sms", 14), ("server", 15), ("segment", 16), ("license", 17), ("ha", 18), ("monitor", 19), ("ipFilter", 20), ("connTable", 21), ("hostComm", 22), ("tse", 23), ("cf", 24))

tptNgfwSysLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 15)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyHost"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"))
if mibBuilder.loadTexts: tptNgfwSysLogNotify.setStatus('current')
tptNgfwLogNotifyTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 60), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifyTime.setStatus('current')
tptNgfwLogNotifyHost = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 61), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifyHost.setStatus('current')
tptNgfwLogNotifySource = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 62), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifySource.setStatus('current')
tptNgfwLogNotifySeverity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 63), Severity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifySeverity.setStatus('current')
tptNgfwLogNotifyText = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 64), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwLogNotifyText.setStatus('current')
tptNgfwAuditLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 16)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyAccess"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddrType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddr"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyCategory"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyResult"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyUser"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyMessage"))
if mibBuilder.loadTexts: tptNgfwAuditLogNotify.setStatus('current')
tptNgfwAuditLogNotifyAccess = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 65), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyAccess.setStatus('current')
tptNgfwAuditLogNotifyType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 66), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyType.setStatus('current')
tptNgfwAuditLogNotifyIpAddrType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 67), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyIpAddrType.setStatus('current')
tptNgfwAuditLogNotifyIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 68), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyIpAddr.setStatus('current')
tptNgfwAuditLogNotifyCategory = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 69), AuditLogCategory()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyCategory.setStatus('current')
tptNgfwAuditLogNotifyResult = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 70), AuditLogResult()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyResult.setStatus('current')
tptNgfwAuditLogNotifyUser = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 71), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyUser.setStatus('current')
tptNgfwAuditLogNotifyMessage = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 72), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptNgfwAuditLogNotifyMessage.setStatus('current')
tptNgfwVpnLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 17)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"))
if mibBuilder.loadTexts: tptNgfwVpnLogNotify.setStatus('current')
tptNgfwLoggingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 9)).setObjects(("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyHost"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyAccess"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddrType"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddr"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyCategory"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyResult"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyUser"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwLoggingGroup = tptNgfwLoggingGroup.setStatus('current')
tptNgfwLoggingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 10)).setObjects(("TPT-NGFW-LOGGING-MIB", "tptNgfwSysLogNotify"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotify"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwVpnLogNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwLoggingNotificationGroup = tptNgfwLoggingNotificationGroup.setStatus('current')
tptNgfwLoggingCompl = ModuleCompliance((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 3)).setObjects(("TPT-NGFW-LOGGING-MIB", "tptNgfwLoggingGroup"), ("TPT-NGFW-LOGGING-MIB", "tptNgfwLoggingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwLoggingCompl = tptNgfwLoggingCompl.setStatus('current')
mibBuilder.exportSymbols("TPT-NGFW-LOGGING-MIB", tptNgfwLogNotifyHost=tptNgfwLogNotifyHost, tptNgfwLogNotifySource=tptNgfwLogNotifySource, tptNgfwLogging=tptNgfwLogging, tptNgfwAuditLogNotifyMessage=tptNgfwAuditLogNotifyMessage, tptNgfwLoggingCompl=tptNgfwLoggingCompl, tptNgfwAuditLogNotify=tptNgfwAuditLogNotify, tptNgfwAuditLogNotifyAccess=tptNgfwAuditLogNotifyAccess, tptNgfwVpnLogNotify=tptNgfwVpnLogNotify, tptNgfwAuditLogNotifyCategory=tptNgfwAuditLogNotifyCategory, tptNgfwAuditLogNotifyResult=tptNgfwAuditLogNotifyResult, tptNgfwLoggingNotificationGroup=tptNgfwLoggingNotificationGroup, tptNgfwAuditLogNotifyIpAddrType=tptNgfwAuditLogNotifyIpAddrType, AuditLogResult=AuditLogResult, tptNgfwSysLogNotify=tptNgfwSysLogNotify, AuditLogCategory=AuditLogCategory, tptNgfwLoggingGroup=tptNgfwLoggingGroup, tptNgfwLogNotifySeverity=tptNgfwLogNotifySeverity, tptNgfwLogNotifyText=tptNgfwLogNotifyText, tptNgfwAuditLogNotifyUser=tptNgfwAuditLogNotifyUser, tptNgfwAuditLogNotifyIpAddr=tptNgfwAuditLogNotifyIpAddr, PYSNMP_MODULE_ID=tptNgfwLogging, tptNgfwLogNotifyTime=tptNgfwLogNotifyTime, tptNgfwAuditLogNotifyType=tptNgfwAuditLogNotifyType)
