#
# PySNMP MIB module TPT-NGFW-SYSTEM-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-NGFW-SYSTEM-INFO-MIB
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
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
tptNgfwNotifySeverity, tpt_ngfw_objs, tpt_ngfw_eventsV2, tpt_ngfw_groups, tpt_ngfw_compls = mibBuilder.importSymbols("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity", "tpt-ngfw-objs", "tpt-ngfw-eventsV2", "tpt-ngfw-groups", "tpt-ngfw-compls")
tptNgfwSystemInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1))
tptNgfwSystemInfo.setRevisions(('2016-05-25 18:54', '2013-01-03 17:39',))
if mibBuilder.loadTexts: tptNgfwSystemInfo.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tptNgfwSystemInfo.setOrganization('Trend Micro, Inc.')
class FipsState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("crypto", 2), ("full", 3))

class BuildType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("production", 1), ("development", 2))

tptNgfwSystemSerial = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSerial.setStatus('current')
tptNgfwSystemSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSoftwareVersion.setStatus('current')
tptNgfwSystemBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBuildDate.setStatus('current')
tptNgfwSystemBuildType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 4), BuildType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBuildType.setStatus('current')
tptNgfwSystemBuildRevision = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBuildRevision.setStatus('current')
tptNgfwSystemDigitalVaccineVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemDigitalVaccineVersion.setStatus('current')
tptNgfwSystemModel = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemModel.setStatus('current')
tptNgfwSystemHardwareSerial = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemHardwareSerial.setStatus('current')
tptNgfwSystemHardwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemHardwareRevision.setStatus('current')
tptNgfwSystemFailsafeVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemFailsafeVersion.setStatus('current')
tptNgfwSystemBootTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 11), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemBootTime.setStatus('current')
tptNgfwSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemUpTime.setStatus('current')
tptNgfwSystemSmsManaged = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSmsManaged.setStatus('current')
tptNgfwSystemSmsIpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 14), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSmsIpAddressType.setStatus('current')
tptNgfwSystemSmsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 15), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemSmsIpAddress.setStatus('current')
tptNgfwSystemFipsAdminState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 16), FipsState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemFipsAdminState.setStatus('current')
tptNgfwSystemFipsOperState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 17), FipsState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemFipsOperState.setStatus('current')
tptNgfwSystemMasterKeySet = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptNgfwSystemMasterKeySet.setStatus('current')
tptNgfwSystemReadyNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 11)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwSystemReadyNotify.setStatus('current')
tptNgfwSystemShutdownNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 12)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwSystemShutdownNotify.setStatus('current')
tptNgfwSystemSmsNotAuthNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 13)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddressType"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddress"), ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
if mibBuilder.loadTexts: tptNgfwSystemSmsNotAuthNotify.setStatus('current')
tptNgfwSystemInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 1)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSoftwareVersion"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildDate"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildType"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBuildRevision"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemDigitalVaccineVersion"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemModel"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemHardwareSerial"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemHardwareRevision"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFailsafeVersion"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemBootTime"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemUpTime"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsManaged"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddressType"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsIpAddress"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFipsAdminState"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemFipsOperState"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemMasterKeySet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwSystemInfoGroup = tptNgfwSystemInfoGroup.setStatus('current')
tptNgfwSystemNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 9)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemReadyNotify"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemShutdownNotify"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSmsNotAuthNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwSystemNotificationGroup = tptNgfwSystemNotificationGroup.setStatus('current')
tptNgfwSystemInfoCompl = ModuleCompliance((1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 1)).setObjects(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemInfoGroup"), ("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptNgfwSystemInfoCompl = tptNgfwSystemInfoCompl.setStatus('current')
mibBuilder.exportSymbols("TPT-NGFW-SYSTEM-INFO-MIB", tptNgfwSystemInfo=tptNgfwSystemInfo, tptNgfwSystemUpTime=tptNgfwSystemUpTime, tptNgfwSystemSmsNotAuthNotify=tptNgfwSystemSmsNotAuthNotify, tptNgfwSystemFipsAdminState=tptNgfwSystemFipsAdminState, tptNgfwSystemSerial=tptNgfwSystemSerial, FipsState=FipsState, tptNgfwSystemSmsManaged=tptNgfwSystemSmsManaged, tptNgfwSystemBuildType=tptNgfwSystemBuildType, tptNgfwSystemInfoGroup=tptNgfwSystemInfoGroup, tptNgfwSystemBootTime=tptNgfwSystemBootTime, tptNgfwSystemNotificationGroup=tptNgfwSystemNotificationGroup, tptNgfwSystemSoftwareVersion=tptNgfwSystemSoftwareVersion, tptNgfwSystemShutdownNotify=tptNgfwSystemShutdownNotify, tptNgfwSystemInfoCompl=tptNgfwSystemInfoCompl, PYSNMP_MODULE_ID=tptNgfwSystemInfo, tptNgfwSystemDigitalVaccineVersion=tptNgfwSystemDigitalVaccineVersion, tptNgfwSystemBuildRevision=tptNgfwSystemBuildRevision, tptNgfwSystemSmsIpAddressType=tptNgfwSystemSmsIpAddressType, tptNgfwSystemFailsafeVersion=tptNgfwSystemFailsafeVersion, tptNgfwSystemReadyNotify=tptNgfwSystemReadyNotify, tptNgfwSystemModel=tptNgfwSystemModel, tptNgfwSystemBuildDate=tptNgfwSystemBuildDate, tptNgfwSystemHardwareRevision=tptNgfwSystemHardwareRevision, tptNgfwSystemFipsOperState=tptNgfwSystemFipsOperState, tptNgfwSystemSmsIpAddress=tptNgfwSystemSmsIpAddress, tptNgfwSystemHardwareSerial=tptNgfwSystemHardwareSerial, tptNgfwSystemMasterKeySet=tptNgfwSystemMasterKeySet, BuildType=BuildType)
