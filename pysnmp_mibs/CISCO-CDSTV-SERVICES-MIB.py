#
# PySNMP MIB module CISCO-CDSTV-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CDSTV-SERVICES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoCdstvServicesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 729))
ciscoCdstvServicesMIB.setRevisions(('2010-03-29 00:00',))
if mibBuilder.loadTexts: ciscoCdstvServicesMIB.setLastUpdated('201003290000Z')
if mibBuilder.loadTexts: ciscoCdstvServicesMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvServicesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 0))
ciscoCdstvServicesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 1))
ciscoCdstvServicesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 2))
cdstvServicesMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1), )
if mibBuilder.loadTexts: cdstvServicesMonitorTable.setStatus('current')
cdstvServicesMonitorTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1), ).setIndexNames((0, "CISCO-CDSTV-SERVICES-MIB", "cdstvServicesMonitorIndex"))
if mibBuilder.loadTexts: cdstvServicesMonitorTableEntry.setStatus('current')
cdstvServicesMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cdstvServicesMonitorIndex.setStatus('current')
cdstvServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServiceName.setStatus('current')
cdstvServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdstvServiceStatus.setStatus('current')
cdstvServiceTrapsEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2))
cdstvServiceUpNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServiceUpNotifEnable.setStatus('current')
cdstvServiceDownNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 729, 1, 2, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServiceDownNotifEnable.setStatus('current')
cdstvServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 729, 0, 1)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"))
if mibBuilder.loadTexts: cdstvServiceUp.setStatus('current')
cdstvServiceDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 729, 0, 2)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"))
if mibBuilder.loadTexts: cdstvServiceDown.setStatus('current')
ciscoCdstvServicesMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 1))
ciscoCdstvServicesMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2))
ciscoCdstvServicesMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 1, 1)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBMainObjectGroup"), ("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBNotificationGroup"), ("CISCO-CDSTV-SERVICES-MIB", "ciscoCdstvServicesMIBNotifEnableObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBCompliance = ciscoCdstvServicesMIBCompliance.setStatus('current')
ciscoCdstvServicesMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 1)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceName"), ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBMainObjectGroup = ciscoCdstvServicesMIBMainObjectGroup.setStatus('current')
ciscoCdstvServicesMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 2)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceUp"), ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBNotificationGroup = ciscoCdstvServicesMIBNotificationGroup.setStatus('current')
ciscoCdstvServicesMIBNotifEnableObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 729, 2, 2, 3)).setObjects(("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceUpNotifEnable"), ("CISCO-CDSTV-SERVICES-MIB", "cdstvServiceDownNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvServicesMIBNotifEnableObjectGroup = ciscoCdstvServicesMIBNotifEnableObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-SERVICES-MIB", ciscoCdstvServicesMIBCompliance=ciscoCdstvServicesMIBCompliance, cdstvServicesMonitorTableEntry=cdstvServicesMonitorTableEntry, cdstvServiceDown=cdstvServiceDown, cdstvServicesMonitorIndex=cdstvServicesMonitorIndex, PYSNMP_MODULE_ID=ciscoCdstvServicesMIB, cdstvServiceUpNotifEnable=cdstvServiceUpNotifEnable, ciscoCdstvServicesMIB=ciscoCdstvServicesMIB, cdstvServiceUp=cdstvServiceUp, cdstvServiceDownNotifEnable=cdstvServiceDownNotifEnable, cdstvServicesMonitorTable=cdstvServicesMonitorTable, ciscoCdstvServicesMIBObjects=ciscoCdstvServicesMIBObjects, ciscoCdstvServicesMIBGroups=ciscoCdstvServicesMIBGroups, cdstvServiceName=cdstvServiceName, cdstvServiceTrapsEnable=cdstvServiceTrapsEnable, ciscoCdstvServicesMIBConform=ciscoCdstvServicesMIBConform, ciscoCdstvServicesMIBNotificationGroup=ciscoCdstvServicesMIBNotificationGroup, ciscoCdstvServicesMIBNotifEnableObjectGroup=ciscoCdstvServicesMIBNotifEnableObjectGroup, ciscoCdstvServicesMIBCompliances=ciscoCdstvServicesMIBCompliances, ciscoCdstvServicesMIBMainObjectGroup=ciscoCdstvServicesMIBMainObjectGroup, ciscoCdstvServicesMIBNotifs=ciscoCdstvServicesMIBNotifs, cdstvServiceStatus=cdstvServiceStatus)
