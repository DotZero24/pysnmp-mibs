#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-SNMP-NOTIFICATION-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
snmpNotifyFilterEntry, = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpNotificationExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 408))
ciscoSnmpNotificationExtMIB.setRevisions(('2004-05-12 00:00',))
if mibBuilder.loadTexts: ciscoSnmpNotificationExtMIB.setLastUpdated('200405120000Z')
if mibBuilder.loadTexts: ciscoSnmpNotificationExtMIB.setOrganization('Cisco Systems, Inc.')
csneMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 0))
csneMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 1))
csneMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2))
csneNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1))
csneSnmpNotifyFilterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1), )
if mibBuilder.loadTexts: csneSnmpNotifyFilterTable.setStatus('current')
csneSnmpNotifyFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1), )
snmpNotifyFilterEntry.registerAugmentions(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneSnmpNotifyFilterEntry"))
csneSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())
if mibBuilder.loadTexts: csneSnmpNotifyFilterEntry.setStatus('current')
csneFilterAdminTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 1), Unsigned32().clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csneFilterAdminTimer.setStatus('current')
csneFilterOperTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csneFilterOperTimer.setStatus('current')
csneFilterTimerUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("seconds", 1), ("minutes", 2), ("hours", 3))).clone('minutes')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csneFilterTimerUnit.setStatus('current')
csneMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1))
csneMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2))
csneMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1, 1)).setObjects(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneNotifyFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csneMIBCompliance = csneMIBCompliance.setStatus('current')
csneNotifyFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2, 1)).setObjects(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterOperTimer"), ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterAdminTimer"), ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterTimerUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csneNotifyFilterGroup = csneNotifyFilterGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-EXT-MIB", csneSnmpNotifyFilterTable=csneSnmpNotifyFilterTable, csneFilterTimerUnit=csneFilterTimerUnit, csneMIBConform=csneMIBConform, csneNotifyObjects=csneNotifyObjects, csneMIBGroups=csneMIBGroups, csneMIBObjects=csneMIBObjects, csneFilterOperTimer=csneFilterOperTimer, csneMIBNotifs=csneMIBNotifs, csneSnmpNotifyFilterEntry=csneSnmpNotifyFilterEntry, csneMIBCompliance=csneMIBCompliance, csneNotifyFilterGroup=csneNotifyFilterGroup, PYSNMP_MODULE_ID=ciscoSnmpNotificationExtMIB, csneFilterAdminTimer=csneFilterAdminTimer, ciscoSnmpNotificationExtMIB=ciscoSnmpNotificationExtMIB, csneMIBCompliances=csneMIBCompliances)
