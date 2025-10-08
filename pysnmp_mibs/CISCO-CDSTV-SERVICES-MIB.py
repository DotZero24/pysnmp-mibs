#
# PySNMP MIB module CISCO-CDSTV-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-CDSTV-SERVICES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-CDSTV-SERVICES-MIB", ciscoCdstvServicesMIBGroups=ciscoCdstvServicesMIBGroups, cdstvServiceUp=cdstvServiceUp, ciscoCdstvServicesMIBObjects=ciscoCdstvServicesMIBObjects, cdstvServicesMonitorIndex=cdstvServicesMonitorIndex, ciscoCdstvServicesMIB=ciscoCdstvServicesMIB, ciscoCdstvServicesMIBCompliances=ciscoCdstvServicesMIBCompliances, ciscoCdstvServicesMIBNotifEnableObjectGroup=ciscoCdstvServicesMIBNotifEnableObjectGroup, cdstvServicesMonitorTableEntry=cdstvServicesMonitorTableEntry, PYSNMP_MODULE_ID=ciscoCdstvServicesMIB, cdstvServiceTrapsEnable=cdstvServiceTrapsEnable, cdstvServiceDownNotifEnable=cdstvServiceDownNotifEnable, ciscoCdstvServicesMIBNotifs=ciscoCdstvServicesMIBNotifs, cdstvServiceStatus=cdstvServiceStatus, cdstvServiceDown=cdstvServiceDown, ciscoCdstvServicesMIBNotificationGroup=ciscoCdstvServicesMIBNotificationGroup, cdstvServiceUpNotifEnable=cdstvServiceUpNotifEnable, ciscoCdstvServicesMIBMainObjectGroup=ciscoCdstvServicesMIBMainObjectGroup, cdstvServicesMonitorTable=cdstvServicesMonitorTable, ciscoCdstvServicesMIBConform=ciscoCdstvServicesMIBConform, ciscoCdstvServicesMIBCompliance=ciscoCdstvServicesMIBCompliance, cdstvServiceName=cdstvServiceName)
