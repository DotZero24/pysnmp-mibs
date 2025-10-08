#
# PySNMP MIB module OS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-SNMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
adva, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "adva")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 2544, 7))
osSnmp.setRevisions(('2020-12-09 00:00',))
if mibBuilder.loadTexts: osSnmp.setLastUpdated('202012090000Z')
if mibBuilder.loadTexts: osSnmp.setOrganization('MRV Communications, Inc.')
osSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 2544, 7, 100))
osSnmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 1))
osSnmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 2))
osSnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1))
osSnmpCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 2544, 7, 2))
osSnmpChangeSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: osSnmpChangeSourceAddress.setStatus('current')
osSnmpChangeV2Community = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: osSnmpChangeV2Community.setStatus('current')
osSnmpChangeV3User = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: osSnmpChangeV3User.setStatus('current')
osSnmpChangeCliUser = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: osSnmpChangeCliUser.setStatus('current')
osSnmpChangeCliCommand = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: osSnmpChangeCliCommand.setStatus('current')
osSnmpChangeCliNodeName = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: osSnmpChangeCliNodeName.setStatus('current')
osSnmpAlarmMangerMode = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osSnmpAlarmMangerMode.setStatus('current')
osSnmpChangeLogMode = MibScalar((1, 3, 6, 1, 4, 1, 629, 2544, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osSnmpChangeLogMode.setStatus('current')
osSnmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 1, 1)).setObjects(("OS-SNMP-MIB", "osSnmpMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osSnmpMIBCompliance = osSnmpMIBCompliance.setStatus('current')
osSnmpMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 2, 1)).setObjects(("OS-SNMP-MIB", "osSnmpChangeSourceAddress"), ("OS-SNMP-MIB", "osSnmpChangeV2Community"), ("OS-SNMP-MIB", "osSnmpChangeV3User"), ("OS-SNMP-MIB", "osSnmpChangeCliUser"), ("OS-SNMP-MIB", "osSnmpChangeCliCommand"), ("OS-SNMP-MIB", "osSnmpChangeCliNodeName"), ("OS-SNMP-MIB", "osSnmpAlarmMangerMode"), ("OS-SNMP-MIB", "osSnmpChangeLogMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osSnmpMandatoryGroup = osSnmpMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-SNMP-MIB", osSnmpChangeV2Community=osSnmpChangeV2Community, osSnmpMIBCompliance=osSnmpMIBCompliance, osSnmp=osSnmp, osSnmpChangeLogMode=osSnmpChangeLogMode, osSnmpChangeCliCommand=osSnmpChangeCliCommand, osSnmpMIBCompliances=osSnmpMIBCompliances, osSnmpChangeCliNodeName=osSnmpChangeCliNodeName, osSnmpCfg=osSnmpCfg, osSnmpMandatoryGroup=osSnmpMandatoryGroup, osSnmpChangeV3User=osSnmpChangeV3User, PYSNMP_MODULE_ID=osSnmp, osSnmpChangeSourceAddress=osSnmpChangeSourceAddress, osSnmpChangeCliUser=osSnmpChangeCliUser, osSnmpAlarmMangerMode=osSnmpAlarmMangerMode, osSnmpConformance=osSnmpConformance, osSnmpNotificationObjects=osSnmpNotificationObjects, osSnmpMIBGroups=osSnmpMIBGroups)
