#
# PySNMP MIB module CISCO-VSAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VSAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, VsanIndex = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId", "VsanIndex")
CiscoMilliSeconds, ListIndex, ListIndexOrZero = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds", "ListIndex", "ListIndexOrZero")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
ciscoVsanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 282))
ciscoVsanMIB.setRevisions(('2006-02-06 00:00', '2005-12-07 00:00', '2005-10-07 00:00', '2005-06-07 00:00', '2004-02-18 00:00', '2003-12-02 00:00', '2003-05-07 00:00', '2003-04-23 00:00', '2002-12-18 00:00', '2002-11-04 00:00', '2002-09-23 00:00',))
if mibBuilder.loadTexts: ciscoVsanMIB.setLastUpdated('200602060000Z')
if mibBuilder.loadTexts: ciscoVsanMIB.setOrganization('Cisco Systems Inc. ')
ciscoVsanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1))
vsanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 3))
vsanConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1))
vsanMembership = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2))
vsanNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3))
vsanFcConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4))
vsanStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 5))
vsanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0))
class VsanMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fibreChannel", 1), ("ethernet", 2), ("infiniband", 3), ("other", 4))

class VsanAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("suspended", 2))

class VsanOperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class VsanLoadBalancingType(TextualConvention, Integer32):
    reference = 'For more information on OX_ID, refer to Fibre Channel Switch Fabric 2 (FC-SW2) section 5.8.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("srcIdDestId", 1), ("srcIdDestIdOxId", 2))

vsanNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanNumber.setStatus('current')
vsanLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanLastChange.setStatus('current')
vsanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3), )
if mibBuilder.loadTexts: vsanTable.setStatus('current')
vsanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: vsanEntry.setStatus('current')
vsanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 1), VsanIndex())
if mibBuilder.loadTexts: vsanIndex.setStatus('current')
vsanName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanName.setStatus('current')
vsanMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 3), VsanMediaType().clone('fibreChannel')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanMediaType.setStatus('current')
vsanAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 4), VsanAdminState().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanAdminState.setStatus('current')
vsanMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(2112)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanMtu.setStatus('current')
vsanLoadBalancingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 6), VsanLoadBalancingType().clone('srcIdDestIdOxId')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanLoadBalancingType.setStatus('current')
vsanInterOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanInterOperMode.setStatus('deprecated')
vsanOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 8), VsanOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanOperState.setStatus('current')
vsanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanRowStatus.setStatus('current')
vsanInterOperValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanInterOperValue.setStatus('current')
vsanInorderDelivery = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanInorderDelivery.setStatus('current')
vsanNetworkDropLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 12), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(500, 60000)).clone(2000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanNetworkDropLatency.setStatus('current')
notifyVsanIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 4), VsanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notifyVsanIndex.setStatus('current')
vsanDenyUnknownWwn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanDenyUnknownWwn.setStatus('current')
vsanWwnListNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanWwnListNumber.setStatus('current')
vsanWwnListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3), )
if mibBuilder.loadTexts: vsanWwnListTable.setStatus('current')
vsanWwnListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanWwnListIndex"), (0, "CISCO-VSAN-MIB", "vsanWwnListWwnIndex"))
if mibBuilder.loadTexts: vsanWwnListEntry.setStatus('current')
vsanWwnListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 1), ListIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vsanWwnListIndex.setStatus('current')
vsanWwnListWwnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vsanWwnListWwnIndex.setStatus('current')
vsanWwnListWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 3), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanWwnListWwn.setStatus('current')
vsanWwnListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanWwnListRowStatus.setStatus('current')
vsanIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanIfNumber.setStatus('current')
vsanIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5), )
if mibBuilder.loadTexts: vsanIfTable.setStatus('current')
vsanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vsanIfEntry.setStatus('current')
vsanIfVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1, 1), VsanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanIfVsan.setStatus('current')
vsanIfDenyList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1, 2), ListIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanIfDenyList.setStatus('current')
vsanDynamicListNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanDynamicListNumber.setStatus('current')
vsanDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7), )
if mibBuilder.loadTexts: vsanDynamicTable.setStatus('current')
vsanDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanWwnListIndex"))
if mibBuilder.loadTexts: vsanDynamicEntry.setStatus('current')
vsanDynamicVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1, 1), VsanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanDynamicVsan.setStatus('current')
vsanDynamicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanDynamicRowStatus.setStatus('current')
vsanMembershipSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8), )
if mibBuilder.loadTexts: vsanMembershipSummaryTable.setStatus('current')
vsanMembershipSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-VSAN-MIB", "vsanMembershipSummaryInterface"))
if mibBuilder.loadTexts: vsanMembershipSummaryEntry.setStatus('current')
vsanMembershipSummaryInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanMembershipSummaryInterface.setStatus('current')
vsanMembershipSummaryIntfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanMembershipSummaryIntfType.setStatus('current')
fcTimerRatov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 1), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(10000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcTimerRatov.setStatus('current')
fcTimerEdtov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 2), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(1000, 100000)).clone(2000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcTimerEdtov.setStatus('current')
fcTimerFstov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 3), CiscoMilliSeconds()).setUnits('msec').setMaxAccess("readonly")
if mibBuilder.loadTexts: fcTimerFstov.setStatus('current')
fcTimerDstov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 4), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(5000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcTimerDstov.setStatus('current')
fcNetworkDropLatency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 5), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(500, 60000)).clone(2000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNetworkDropLatency.setStatus('current')
fcSwitchDropLatency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 6), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(0, 60000)).clone(500)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcSwitchDropLatency.setStatus('current')
fcInorderDelivery = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcInorderDelivery.setStatus('current')
vsanFcTimerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8), )
if mibBuilder.loadTexts: vsanFcTimerTable.setStatus('current')
vsanFcTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1), )
vsanEntry.registerAugmentions(("CISCO-VSAN-MIB", "vsanFcTimerEntry"))
vsanFcTimerEntry.setIndexNames(*vsanEntry.getIndexNames())
if mibBuilder.loadTexts: vsanFcTimerEntry.setStatus('current')
vsanFcTimerForceFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 1), Bits().clone(namedValues=NamedValues(("ratov", 0), ("edtov", 1), ("dstov", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerForceFlag.setStatus('current')
vsanFcTimerRatov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 2), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(10000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerRatov.setStatus('current')
vsanFcTimerEdtov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 3), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(1000, 100000)).clone(2000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerEdtov.setStatus('current')
vsanFcTimerDstov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 4), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(5000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerDstov.setStatus('current')
vsanFcTimerFstov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 5), CiscoMilliSeconds()).setUnits('msec').setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanFcTimerFstov.setStatus('current')
vsanFcFeElementName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 5, 1), FcNameId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanFcFeElementName.setStatus('current')
vsanStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0, 1)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanOperState"))
if mibBuilder.loadTexts: vsanStatusChange.setStatus('current')
vsanPortMembershipChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0, 2)).setObjects(("CISCO-VSAN-MIB", "vsanFcFeElementName"), ("IF-MIB", "ifIndex"), ("CISCO-VSAN-MIB", "notifyVsanIndex"))
if mibBuilder.loadTexts: vsanPortMembershipChange.setStatus('current')
vsanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1))
vsanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2))
vsanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 1)).setObjects(("CISCO-VSAN-MIB", "vsanGroup"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroup"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance = vsanMIBCompliance.setStatus('deprecated')
vsanMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 2)).setObjects(("CISCO-VSAN-MIB", "vsanGroup"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroup"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance1 = vsanMIBCompliance1.setStatus('deprecated')
vsanMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 3)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev1"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroup"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance2 = vsanMIBCompliance2.setStatus('deprecated')
vsanMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 4)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev1"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance3 = vsanMIBCompliance3.setStatus('deprecated')
vsanMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 5)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev2"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance4 = vsanMIBCompliance4.setStatus('deprecated')
vsanMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 6)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev2"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanMembershipSummaryGroupRev1"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance5 = vsanMIBCompliance5.setStatus('deprecated')
vsanMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 7)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev2"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanMembershipSummaryGroupRev1"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance6 = vsanMIBCompliance6.setStatus('deprecated')
vsanMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 8)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev3"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanMembershipSummaryGroupRev1"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance7 = vsanMIBCompliance7.setStatus('current')
vsanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 1)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanInterOperMode"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroup = vsanGroup.setStatus('deprecated')
vsanMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 3)).setObjects(("CISCO-VSAN-MIB", "vsanDenyUnknownWwn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMembershipGroup = vsanMembershipGroup.setStatus('current')
vsanStaticMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 4)).setObjects(("CISCO-VSAN-MIB", "vsanIfNumber"), ("CISCO-VSAN-MIB", "vsanIfVsan"), ("CISCO-VSAN-MIB", "vsanIfDenyList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanStaticMembershipGroup = vsanStaticMembershipGroup.setStatus('current')
vsanWWNListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 5)).setObjects(("CISCO-VSAN-MIB", "vsanWwnListNumber"), ("CISCO-VSAN-MIB", "vsanWwnListWwn"), ("CISCO-VSAN-MIB", "vsanWwnListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanWWNListGroup = vsanWWNListGroup.setStatus('current')
vsanDynamicMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 6)).setObjects(("CISCO-VSAN-MIB", "vsanDynamicListNumber"), ("CISCO-VSAN-MIB", "vsanDynamicVsan"), ("CISCO-VSAN-MIB", "vsanDynamicRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanDynamicMembershipGroup = vsanDynamicMembershipGroup.setStatus('current')
vsanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 7)).setObjects(("CISCO-VSAN-MIB", "vsanStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanNotificationGroup = vsanNotificationGroup.setStatus('deprecated')
vsanFcTimerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 8)).setObjects(("CISCO-VSAN-MIB", "fcTimerRatov"), ("CISCO-VSAN-MIB", "fcTimerEdtov"), ("CISCO-VSAN-MIB", "fcTimerFstov"), ("CISCO-VSAN-MIB", "fcTimerDstov"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanFcTimerGroup = vsanFcTimerGroup.setStatus('deprecated')
vsanFcLatencyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 9)).setObjects(("CISCO-VSAN-MIB", "fcNetworkDropLatency"), ("CISCO-VSAN-MIB", "fcSwitchDropLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanFcLatencyGroup = vsanFcLatencyGroup.setStatus('current')
vsanVsanMembershipSummaryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 10)).setObjects(("CISCO-VSAN-MIB", "vsanMembershipSummaryInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanVsanMembershipSummaryGroup = vsanVsanMembershipSummaryGroup.setStatus('current')
vsanGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 11)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "vsanInterOperValue"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroupRev1 = vsanGroupRev1.setStatus('deprecated')
vsanFcTimerGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 12)).setObjects(("CISCO-VSAN-MIB", "fcTimerRatov"), ("CISCO-VSAN-MIB", "fcTimerEdtov"), ("CISCO-VSAN-MIB", "fcTimerDstov"), ("CISCO-VSAN-MIB", "fcTimerFstov"), ("CISCO-VSAN-MIB", "vsanFcTimerForceFlag"), ("CISCO-VSAN-MIB", "vsanFcTimerRatov"), ("CISCO-VSAN-MIB", "vsanFcTimerEdtov"), ("CISCO-VSAN-MIB", "vsanFcTimerDstov"), ("CISCO-VSAN-MIB", "vsanFcTimerFstov"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanFcTimerGroupRev1 = vsanFcTimerGroupRev1.setStatus('current')
vsanGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 13)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "vsanInterOperValue"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"), ("CISCO-VSAN-MIB", "vsanInorderDelivery"), ("CISCO-VSAN-MIB", "vsanNetworkDropLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroupRev2 = vsanGroupRev2.setStatus('deprecated')
vsanMembershipSummaryGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 14)).setObjects(("CISCO-VSAN-MIB", "vsanMembershipSummaryIntfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMembershipSummaryGroupRev1 = vsanMembershipSummaryGroupRev1.setStatus('current')
vsanNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 15)).setObjects(("CISCO-VSAN-MIB", "vsanStatusChange"), ("CISCO-VSAN-MIB", "vsanPortMembershipChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanNotificationGroupRev1 = vsanNotificationGroupRev1.setStatus('current')
vsanGroupRev3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 16)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "vsanInterOperValue"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"), ("CISCO-VSAN-MIB", "vsanInorderDelivery"), ("CISCO-VSAN-MIB", "vsanNetworkDropLatency"), ("CISCO-VSAN-MIB", "vsanFcFeElementName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroupRev3 = vsanGroupRev3.setStatus('current')
mibBuilder.exportSymbols("CISCO-VSAN-MIB", vsanMIBCompliance4=vsanMIBCompliance4, vsanFcTimerEdtov=vsanFcTimerEdtov, vsanWwnListNumber=vsanWwnListNumber, vsanStats=vsanStats, PYSNMP_MODULE_ID=ciscoVsanMIB, vsanFcTimerGroupRev1=vsanFcTimerGroupRev1, vsanFcTimerForceFlag=vsanFcTimerForceFlag, vsanWwnListRowStatus=vsanWwnListRowStatus, vsanNumber=vsanNumber, fcTimerEdtov=fcTimerEdtov, vsanMembership=vsanMembership, vsanDenyUnknownWwn=vsanDenyUnknownWwn, vsanMIBCompliance=vsanMIBCompliance, vsanFcTimerEntry=vsanFcTimerEntry, vsanTable=vsanTable, vsanGroup=vsanGroup, vsanMIBCompliance2=vsanMIBCompliance2, vsanStatusChange=vsanStatusChange, vsanDynamicEntry=vsanDynamicEntry, ciscoVsanMIBObjects=ciscoVsanMIBObjects, vsanNetworkDropLatency=vsanNetworkDropLatency, vsanDynamicVsan=vsanDynamicVsan, vsanInorderDelivery=vsanInorderDelivery, VsanMediaType=VsanMediaType, vsanPortMembershipChange=vsanPortMembershipChange, vsanIndex=vsanIndex, vsanMembershipSummaryGroupRev1=vsanMembershipSummaryGroupRev1, vsanGroupRev3=vsanGroupRev3, VsanLoadBalancingType=VsanLoadBalancingType, vsanFcTimerDstov=vsanFcTimerDstov, vsanFcTimerTable=vsanFcTimerTable, vsanMembershipGroup=vsanMembershipGroup, vsanMediaType=vsanMediaType, vsanFcTimerFstov=vsanFcTimerFstov, vsanMtu=vsanMtu, vsanMIBCompliance1=vsanMIBCompliance1, vsanMIBConformance=vsanMIBConformance, vsanWwnListWwnIndex=vsanWwnListWwnIndex, vsanFcLatencyGroup=vsanFcLatencyGroup, vsanWwnListEntry=vsanWwnListEntry, vsanRowStatus=vsanRowStatus, vsanStaticMembershipGroup=vsanStaticMembershipGroup, vsanNotifications=vsanNotifications, vsanMembershipSummaryInterface=vsanMembershipSummaryInterface, vsanWwnListIndex=vsanWwnListIndex, vsanWwnListWwn=vsanWwnListWwn, vsanOperState=vsanOperState, vsanGroupRev1=vsanGroupRev1, vsanMIBCompliance3=vsanMIBCompliance3, vsanNotificationGroup=vsanNotificationGroup, vsanAdminState=vsanAdminState, vsanWWNListGroup=vsanWWNListGroup, vsanName=vsanName, fcNetworkDropLatency=fcNetworkDropLatency, vsanMembershipSummaryTable=vsanMembershipSummaryTable, vsanIfDenyList=vsanIfDenyList, vsanMIBCompliance5=vsanMIBCompliance5, vsanNotificationGroupRev1=vsanNotificationGroupRev1, vsanFcFeElementName=vsanFcFeElementName, vsanMIBCompliance6=vsanMIBCompliance6, fcInorderDelivery=fcInorderDelivery, vsanLoadBalancingType=vsanLoadBalancingType, vsanMIBGroups=vsanMIBGroups, vsanEntry=vsanEntry, vsanMIBCompliance7=vsanMIBCompliance7, vsanMembershipSummaryIntfType=vsanMembershipSummaryIntfType, VsanAdminState=VsanAdminState, vsanDynamicRowStatus=vsanDynamicRowStatus, VsanOperationalState=VsanOperationalState, vsanMIBCompliances=vsanMIBCompliances, vsanIfVsan=vsanIfVsan, vsanLastChange=vsanLastChange, vsanWwnListTable=vsanWwnListTable, vsanInterOperMode=vsanInterOperMode, vsanDynamicMembershipGroup=vsanDynamicMembershipGroup, fcSwitchDropLatency=fcSwitchDropLatency, vsanIfTable=vsanIfTable, vsanMembershipSummaryEntry=vsanMembershipSummaryEntry, vsanFcTimerRatov=vsanFcTimerRatov, vsanFcTimerGroup=vsanFcTimerGroup, vsanIfEntry=vsanIfEntry, fcTimerRatov=fcTimerRatov, ciscoVsanMIB=ciscoVsanMIB, vsanNotification=vsanNotification, vsanInterOperValue=vsanInterOperValue, vsanGroupRev2=vsanGroupRev2, vsanConfiguration=vsanConfiguration, vsanFcConfiguration=vsanFcConfiguration, vsanIfNumber=vsanIfNumber, vsanVsanMembershipSummaryGroup=vsanVsanMembershipSummaryGroup, fcTimerDstov=fcTimerDstov, fcTimerFstov=fcTimerFstov, notifyVsanIndex=notifyVsanIndex, vsanDynamicListNumber=vsanDynamicListNumber, vsanDynamicTable=vsanDynamicTable)
