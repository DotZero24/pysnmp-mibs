#
# PySNMP MIB module CISCO-CABLE-METERING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-CABLE-METERING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
ciscoCableMeteringMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 424))
ciscoCableMeteringMIB.setRevisions(('2009-10-13 00:00', '2009-05-18 00:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoCableMeteringMIB.setLastUpdated('200910130000Z')
if mibBuilder.loadTexts: ciscoCableMeteringMIB.setOrganization('Cisco Systems, Inc.')
class CcmtrStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("success", 2), ("deviceFull", 3), ("writeError", 4), ("fileNotExist", 5), ("connectionTimeout", 6), ("dataIncomplete", 7))

class CcmtrCollectionServer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

ciscoCableMeteringMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 0))
ciscoCableMeteringMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 1))
ccmtrMeteringConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1))
ccmtrMetering = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2))
ccmtrCollectionType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("local", 2), ("stream", 3), ("ipdr", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionType.setStatus('current')
ccmtrCollectionFilesystem = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionFilesystem.setStatus('current')
ccmtrCollectionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3), )
if mibBuilder.loadTexts: ccmtrCollectionTable.setStatus('current')
ccmtrCollectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-CABLE-METERING-MIB", "ccmtrCollectionID"))
if mibBuilder.loadTexts: ccmtrCollectionEntry.setStatus('current')
ccmtrCollectionID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 1), CcmtrCollectionServer())
if mibBuilder.loadTexts: ccmtrCollectionID.setStatus('current')
ccmtrCollectionIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmtrCollectionIpAddrType.setStatus('current')
ccmtrCollectionIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmtrCollectionIpAddress.setStatus('current')
ccmtrCollectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmtrCollectionPort.setStatus('current')
ccmtrCollectionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccmtrCollectionRowStatus.setStatus('current')
ccmtrCollectionInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 1440)).clone(30)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionInterval.setStatus('deprecated')
ccmtrCollectionRetries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionRetries.setStatus('current')
ccmtrCollectionSecure = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionSecure.setStatus('current')
ccmtrCollectionCpeList = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionCpeList.setStatus('current')
ccmtrCollectionAggregate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionAggregate.setStatus('current')
ccmtrCollectionSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionSrcIfIndex.setStatus('current')
ccmtrCollectionRevInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(30)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionRevInterval.setStatus('current')
ccmtrCollectionDataPerSession = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionDataPerSession.setStatus('current')
ccmtrCollectionDataTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(8, 500)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrCollectionDataTimer.setStatus('current')
ccmtrCollectionStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 1), CcmtrStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmtrCollectionStatus.setStatus('current')
ccmtrCollectionDestination = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmtrCollectionDestination.setStatus('current')
ccmtrCollectionTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccmtrCollectionTimestamp.setStatus('current')
ccmtrMeteringNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 424, 1, 2, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccmtrMeteringNotifEnable.setStatus('current')
ccmtrCollectionNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 424, 0, 1)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionStatus"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDestination"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionTimestamp"))
if mibBuilder.loadTexts: ccmtrCollectionNotification.setStatus('current')
ciscoCableMeteringMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 3))
ciscoCableMeteringMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 1))
ciscoCableMeteringMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2))
ciscoCableMeteringCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 1, 1)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrMeteringObjGroup"), ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringNotifCtrlGroup"), ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableMeteringCompliance = ciscoCableMeteringCompliance.setStatus('deprecated')
ciscoCableMeteringComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 1, 2)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrMeteringNotifCtrlGroup"), ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringNotifGroup"), ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringObjGroupRev1"), ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringSrcIntfObjGroup"), ("CISCO-CABLE-METERING-MIB", "ccmtrMeteringRateCtrlObjGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableMeteringComplianceRev1 = ciscoCableMeteringComplianceRev1.setStatus('current')
ccmtrMeteringObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 1)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionType"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionFilesystem"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddrType"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddress"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionPort"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionInterval"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRetries"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionSecure"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRowStatus"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionCpeList"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionAggregate"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionStatus"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDestination"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmtrMeteringObjGroup = ccmtrMeteringObjGroup.setStatus('deprecated')
ccmtrMeteringNotifCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 2)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrMeteringNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmtrMeteringNotifCtrlGroup = ccmtrMeteringNotifCtrlGroup.setStatus('current')
ccmtrMeteringNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 3)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmtrMeteringNotifGroup = ccmtrMeteringNotifGroup.setStatus('current')
ccmtrMeteringObjGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 4)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionType"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionFilesystem"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddrType"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionIpAddress"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionPort"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRowStatus"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRetries"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionSecure"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionCpeList"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionAggregate"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionRevInterval"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionStatus"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDestination"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmtrMeteringObjGroupRev1 = ccmtrMeteringObjGroupRev1.setStatus('current')
ccmtrMeteringSrcIntfObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 5)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionSrcIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmtrMeteringSrcIntfObjGroup = ccmtrMeteringSrcIntfObjGroup.setStatus('current')
ccmtrMeteringRateCtrlObjGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 424, 3, 2, 6)).setObjects(("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDataPerSession"), ("CISCO-CABLE-METERING-MIB", "ccmtrCollectionDataTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccmtrMeteringRateCtrlObjGroup = ccmtrMeteringRateCtrlObjGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CABLE-METERING-MIB", ccmtrCollectionID=ccmtrCollectionID, ccmtrCollectionRevInterval=ccmtrCollectionRevInterval, ccmtrMeteringObjGroupRev1=ccmtrMeteringObjGroupRev1, CcmtrStatus=CcmtrStatus, ccmtrCollectionPort=ccmtrCollectionPort, ccmtrMeteringNotifEnable=ccmtrMeteringNotifEnable, CcmtrCollectionServer=CcmtrCollectionServer, ciscoCableMeteringMIB=ciscoCableMeteringMIB, PYSNMP_MODULE_ID=ciscoCableMeteringMIB, ccmtrCollectionTable=ccmtrCollectionTable, ccmtrCollectionEntry=ccmtrCollectionEntry, ccmtrCollectionIpAddrType=ccmtrCollectionIpAddrType, ccmtrCollectionDataPerSession=ccmtrCollectionDataPerSession, ccmtrMeteringNotifGroup=ccmtrMeteringNotifGroup, ccmtrCollectionNotification=ccmtrCollectionNotification, ccmtrMeteringRateCtrlObjGroup=ccmtrMeteringRateCtrlObjGroup, ccmtrCollectionTimestamp=ccmtrCollectionTimestamp, ccmtrMeteringNotifCtrlGroup=ccmtrMeteringNotifCtrlGroup, ciscoCableMeteringMIBNotifs=ciscoCableMeteringMIBNotifs, ccmtrCollectionCpeList=ccmtrCollectionCpeList, ccmtrCollectionDataTimer=ccmtrCollectionDataTimer, ccmtrCollectionRowStatus=ccmtrCollectionRowStatus, ccmtrMeteringObjGroup=ccmtrMeteringObjGroup, ccmtrCollectionAggregate=ccmtrCollectionAggregate, ccmtrCollectionStatus=ccmtrCollectionStatus, ccmtrMetering=ccmtrMetering, ccmtrCollectionDestination=ccmtrCollectionDestination, ciscoCableMeteringMIBGroups=ciscoCableMeteringMIBGroups, ccmtrMeteringSrcIntfObjGroup=ccmtrMeteringSrcIntfObjGroup, ciscoCableMeteringComplianceRev1=ciscoCableMeteringComplianceRev1, ccmtrCollectionSrcIfIndex=ccmtrCollectionSrcIfIndex, ciscoCableMeteringMIBConformance=ciscoCableMeteringMIBConformance, ccmtrCollectionType=ccmtrCollectionType, ciscoCableMeteringCompliance=ciscoCableMeteringCompliance, ccmtrCollectionIpAddress=ccmtrCollectionIpAddress, ccmtrCollectionInterval=ccmtrCollectionInterval, ciscoCableMeteringMIBCompliances=ciscoCableMeteringMIBCompliances, ccmtrCollectionFilesystem=ccmtrCollectionFilesystem, ccmtrCollectionRetries=ccmtrCollectionRetries, ciscoCableMeteringMIBObjects=ciscoCableMeteringMIBObjects, ccmtrMeteringConfig=ccmtrMeteringConfig, ccmtrCollectionSecure=ccmtrCollectionSecure)
