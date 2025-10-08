#
# PySNMP MIB module HPVCMODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPVCMODULE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, ifOutErrors, InterfaceIndex, ifInErrors = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifOutErrors", "InterfaceIndex", "ifInErrors")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, zeroDotZero, enterprises, NotificationType, Integer32, Bits, Unsigned32, mib_2, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "zeroDotZero", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "mib-2", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowPointer", "TextualConvention")
TransportAddressType, TransportAddress = mibBuilder.importSymbols("TRANSPORT-ADDRESS-MIB", "TransportAddressType", "TransportAddress")
vcModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3))
vcModuleMIB.setRevisions(('2020-04-14 00:00', '2019-01-29 00:00', '2016-03-21 00:00', '2014-01-29 00:00', '2013-11-07 00:00', '2012-09-22 00:00', '2012-08-19 00:00', '2011-02-01 00:00', '2009-02-18 00:00', '2008-10-08 00:00',))
if mibBuilder.loadTexts: vcModuleMIB.setLastUpdated('202004140000Z')
if mibBuilder.loadTexts: vcModuleMIB.setOrganization('Hewlett Packard Enterprise')
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
hpSysMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5))
hpEmbeddedServerMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7))
hpModuleMgmtProc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5))
virtualConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2))
vcModuleMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1))
vcModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1))
class VcModuleRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unintegrated", 1), ("primaryProtected", 2), ("primaryUnprotected", 3), ("standby", 4), ("other", 5))

class VcEnclosureRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("primary", 2), ("secondary", 3))

class VcModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vcModuleEnet", 1), ("vcModuleFC", 2), ("vcModuleOther", 3))

vcModuleDomainName = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainName.setStatus('current')
vcModuleRole = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 2), VcModuleRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleRole.setStatus('current')
vcModuleDomainPrimaryAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 3), TransportAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddressType.setStatus('current')
vcModuleDomainPrimaryAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 4), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddress.setStatus('current')
vcModuleEnclosureRole = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 5), VcEnclosureRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleEnclosureRole.setStatus('current')
vcModuleDomainPrimaryAddressIpv6 = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 7), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddressIpv6.setStatus('current')
vcSwitchMemParityErrorCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcSwitchMemParityErrorCount.setStatus('current')
vcSwitchMemParityErrorNonCorrectableCount = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcSwitchMemParityErrorNonCorrectableCount.setStatus('current')
class VcModulePortBpduLoopStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("loop-detected", 2))

class VcModulePortProtectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("pause-flood-detected", 2), ("in-pause-condition", 3))

vcModulePortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6), )
if mibBuilder.loadTexts: vcModulePortTable.setStatus('current')
vcModulePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1), ).setIndexNames((0, "HPVCMODULE-MIB", "vcModulePort"))
if mibBuilder.loadTexts: vcModulePortEntry.setStatus('current')
vcModulePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModulePort.setStatus('current')
vcModulePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModulePortIfIndex.setStatus('current')
vcModulePortBpduLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 3), VcModulePortBpduLoopStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModulePortBpduLoopStatus.setStatus('current')
vcModulePortProtectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 6, 1, 4), VcModulePortProtectionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModulePortProtectionStatus.setStatus('current')
vcModuleMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2))
vcModuleMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0))
vcModuleMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 1))
vcModuleDomainRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleRole"))
if mibBuilder.loadTexts: vcModuleDomainRoleChange.setStatus('current')
vcSwitchMemParityErrorEvent = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 2)).setObjects(("HPVCMODULE-MIB", "vcSwitchMemParityErrorCount"))
if mibBuilder.loadTexts: vcSwitchMemParityErrorEvent.setStatus('current')
vcSwitchMemParityErrorNonCorrectableEvent = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 3)).setObjects(("HPVCMODULE-MIB", "vcSwitchMemParityErrorNonCorrectableCount"), ("HPVCMODULE-MIB", "cpqHoFwVerLocation"))
if mibBuilder.loadTexts: vcSwitchMemParityErrorNonCorrectableEvent.setStatus('current')
vcModPortInputUtilizationUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortInputUtilizationUp.setStatus('current')
vcModPortInputUtilizationDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortInputUtilizationDown.setStatus('current')
vcModPortOutputUtilizationUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortOutputUtilizationUp.setStatus('current')
vcModPortOutputUtilizationDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortOutputUtilizationDown.setStatus('current')
vcModPortInputErrorsUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 15)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: vcModPortInputErrorsUp.setStatus('current')
vcModPortInputErrorsDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 16)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: vcModPortInputErrorsDown.setStatus('current')
vcModPortOutputErrorsUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 17)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifOutErrors"))
if mibBuilder.loadTexts: vcModPortOutputErrorsUp.setStatus('current')
vcModPortOutputErrorsDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 18)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifOutErrors"))
if mibBuilder.loadTexts: vcModPortOutputErrorsDown.setStatus('current')
vcModPortBpduLoopDetected = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 19)).setObjects(("IF-MIB", "ifIndex"), ("HPVCMODULE-MIB", "vcModulePort"), ("HPVCMODULE-MIB", "vcModulePortBpduLoopStatus"))
if mibBuilder.loadTexts: vcModPortBpduLoopDetected.setStatus('current')
vcModPortBpduLoopCleared = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 20)).setObjects(("IF-MIB", "ifIndex"), ("HPVCMODULE-MIB", "vcModulePort"), ("HPVCMODULE-MIB", "vcModulePortBpduLoopStatus"))
if mibBuilder.loadTexts: vcModPortBpduLoopCleared.setStatus('current')
vcModPortProtectionConditionDetected = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 21)).setObjects(("IF-MIB", "ifIndex"), ("HPVCMODULE-MIB", "vcModulePort"), ("HPVCMODULE-MIB", "vcModulePortProtectionStatus"))
if mibBuilder.loadTexts: vcModPortProtectionConditionDetected.setStatus('current')
vcModPortProtectionConditionCleared = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 22)).setObjects(("IF-MIB", "ifIndex"), ("HPVCMODULE-MIB", "vcModulePort"), ("HPVCMODULE-MIB", "vcModulePortProtectionStatus"))
if mibBuilder.loadTexts: vcModPortProtectionConditionCleared.setStatus('current')
vcModuleMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3))
vcModuleMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1))
vcModuleMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2))
vcModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleGroup"), ("HPVCMODULE-MIB", "vcModPortThresholdNotificationsGroup"), ("HPVCMODULE-MIB", "vcModPortStatusNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleMIBCompliance = vcModuleMIBCompliance.setStatus('deprecated')
vcModuleMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 2)).setObjects(("HPVCMODULE-MIB", "vcModuleGroup"), ("HPVCMODULE-MIB", "vcModPortThresholdNotificationsGroup"), ("HPVCMODULE-MIB", "vcModPortStatusNotificationsGroup"), ("HPVCMODULE-MIB", "vcModuleGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleMIBCompliance2 = vcModuleMIBCompliance2.setStatus('current')
vcModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleDomainName"), ("HPVCMODULE-MIB", "vcModuleRole"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressIpv6"), ("HPVCMODULE-MIB", "vcSwitchMemParityErrorCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleGroup = vcModuleGroup.setStatus('deprecated')
vcModPortThresholdNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 2)).setObjects(("HPVCMODULE-MIB", "vcModPortInputUtilizationUp"), ("HPVCMODULE-MIB", "vcModPortInputUtilizationDown"), ("HPVCMODULE-MIB", "vcModPortOutputUtilizationUp"), ("HPVCMODULE-MIB", "vcModPortOutputUtilizationDown"), ("HPVCMODULE-MIB", "vcModPortInputErrorsUp"), ("HPVCMODULE-MIB", "vcModPortInputErrorsDown"), ("HPVCMODULE-MIB", "vcModPortOutputErrorsUp"), ("HPVCMODULE-MIB", "vcModPortOutputErrorsDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModPortThresholdNotificationsGroup = vcModPortThresholdNotificationsGroup.setStatus('current')
vcModPortStatusNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 3)).setObjects(("HPVCMODULE-MIB", "vcModPortBpduLoopDetected"), ("HPVCMODULE-MIB", "vcModPortBpduLoopCleared"), ("HPVCMODULE-MIB", "vcModPortProtectionConditionDetected"), ("HPVCMODULE-MIB", "vcModPortProtectionConditionCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModPortStatusNotificationsGroup = vcModPortStatusNotificationsGroup.setStatus('current')
vcModuleGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 4)).setObjects(("HPVCMODULE-MIB", "vcModuleDomainName"), ("HPVCMODULE-MIB", "vcModuleRole"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressIpv6"), ("HPVCMODULE-MIB", "vcSwitchMemParityErrorCount"), ("HPVCMODULE-MIB", "vcSwitchMemParityErrorNonCorrectableCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleGroup2 = vcModuleGroup2.setStatus('current')
mibBuilder.exportSymbols("HPVCMODULE-MIB", vcModPortBpduLoopCleared=vcModPortBpduLoopCleared, vcModuleMIBNotificationObjects=vcModuleMIBNotificationObjects, vcModPortOutputUtilizationUp=vcModPortOutputUtilizationUp, vcModulePortEntry=vcModulePortEntry, vcModuleMIBGroups=vcModuleMIBGroups, vcModuleMIBObjects=vcModuleMIBObjects, vcModPortStatusNotificationsGroup=vcModPortStatusNotificationsGroup, vcModulePortProtectionStatus=vcModulePortProtectionStatus, vcModulePortIfIndex=vcModulePortIfIndex, vcModuleMIBNotificationPrefix=vcModuleMIBNotificationPrefix, vcModPortInputErrorsDown=vcModPortInputErrorsDown, vcModPortProtectionConditionCleared=vcModPortProtectionConditionCleared, vcModuleMIBCompliances=vcModuleMIBCompliances, vcModulePort=vcModulePort, VcModulePortBpduLoopStatus=VcModulePortBpduLoopStatus, vcModuleRole=vcModuleRole, vcModuleDomainName=vcModuleDomainName, VcEnclosureRole=VcEnclosureRole, vcModuleGroup=vcModuleGroup, hpSysMgt=hpSysMgt, vcModuleMIB=vcModuleMIB, virtualConnect=virtualConnect, VcModuleRole=VcModuleRole, vcModuleMIBConformance=vcModuleMIBConformance, hpEmbeddedServerMgt=hpEmbeddedServerMgt, vcModPortOutputErrorsDown=vcModPortOutputErrorsDown, vcModuleObjects=vcModuleObjects, vcModPortBpduLoopDetected=vcModPortBpduLoopDetected, vcModuleDomainPrimaryAddress=vcModuleDomainPrimaryAddress, vcModuleEnclosureRole=vcModuleEnclosureRole, vcModPortOutputErrorsUp=vcModPortOutputErrorsUp, vcModulePortBpduLoopStatus=vcModulePortBpduLoopStatus, hp=hp, VcModulePortProtectionStatus=VcModulePortProtectionStatus, vcModuleMIBNotifications=vcModuleMIBNotifications, vcModPortProtectionConditionDetected=vcModPortProtectionConditionDetected, vcModuleGroup2=vcModuleGroup2, vcSwitchMemParityErrorCount=vcSwitchMemParityErrorCount, vcModPortInputUtilizationUp=vcModPortInputUtilizationUp, vcSwitchMemParityErrorNonCorrectableCount=vcSwitchMemParityErrorNonCorrectableCount, vcSwitchMemParityErrorNonCorrectableEvent=vcSwitchMemParityErrorNonCorrectableEvent, VcModuleType=VcModuleType, PYSNMP_MODULE_ID=vcModuleMIB, vcModuleMIBCompliance2=vcModuleMIBCompliance2, vcModPortThresholdNotificationsGroup=vcModPortThresholdNotificationsGroup, vcModuleDomainPrimaryAddressIpv6=vcModuleDomainPrimaryAddressIpv6, vcModuleMIBCompliance=vcModuleMIBCompliance, vcModPortOutputUtilizationDown=vcModPortOutputUtilizationDown, hpModuleMgmtProc=hpModuleMgmtProc, vcModuleDomainPrimaryAddressType=vcModuleDomainPrimaryAddressType, vcModuleDomainRoleChange=vcModuleDomainRoleChange, vcModPortInputErrorsUp=vcModPortInputErrorsUp, vcModulePortTable=vcModulePortTable, vcSwitchMemParityErrorEvent=vcSwitchMemParityErrorEvent, vcModPortInputUtilizationDown=vcModPortInputUtilizationDown)
