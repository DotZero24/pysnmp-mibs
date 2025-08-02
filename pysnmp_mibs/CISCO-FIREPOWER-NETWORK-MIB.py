_K='cfprNetworkSanNeighborsInstanceId'
_J='cfprNetworkSanNeighborEntryInstanceId'
_I='cfprNetworkOperLevelInstanceId'
_H='cfprNetworkLanNeighborsInstanceId'
_G='cfprNetworkLanNeighborEntryInstanceId'
_F='cfprNetworkIfStatsInstanceId'
_E='cfprNetworkElementInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-NETWORK-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprEquipmentSensorThresholdStatus,CfprMgmtAdminState,CfprNetworkElementOperability,CfprNetworkIfStatsType,CfprNetworkIfStatsUnits,CfprNetworkInventoryStatus,CfprNetworkSamConfigStatus,CfprNetworkSwitchId,CfprNetworkVlanCountStatus=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprEquipmentSensorThresholdStatus','CfprMgmtAdminState','CfprNetworkElementOperability','CfprNetworkIfStatsType','CfprNetworkIfStatsUnits','CfprNetworkInventoryStatus','CfprNetworkSamConfigStatus','CfprNetworkSwitchId','CfprNetworkVlanCountStatus')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprNetworkObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,52))
_CfprNetworkElementTable_Object=MibTable
cfprNetworkElementTable=_CfprNetworkElementTable_Object((1,3,6,1,4,1,9,9,826,1,52,1))
if mibBuilder.loadTexts:cfprNetworkElementTable.setStatus(_A)
_CfprNetworkElementEntry_Object=MibTableRow
cfprNetworkElementEntry=_CfprNetworkElementEntry_Object((1,3,6,1,4,1,9,9,826,1,52,1,1))
cfprNetworkElementEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprNetworkElementEntry.setStatus(_A)
_CfprNetworkElementInstanceId_Type=CfprManagedObjectId
_CfprNetworkElementInstanceId_Object=MibTableColumn
cfprNetworkElementInstanceId=_CfprNetworkElementInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,1),_CfprNetworkElementInstanceId_Type())
cfprNetworkElementInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkElementInstanceId.setStatus(_A)
_CfprNetworkElementDn_Type=CfprManagedObjectDn
_CfprNetworkElementDn_Object=MibTableColumn
cfprNetworkElementDn=_CfprNetworkElementDn_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,2),_CfprNetworkElementDn_Type())
cfprNetworkElementDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementDn.setStatus(_A)
_CfprNetworkElementRn_Type=SnmpAdminString
_CfprNetworkElementRn_Object=MibTableColumn
cfprNetworkElementRn=_CfprNetworkElementRn_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,3),_CfprNetworkElementRn_Type())
cfprNetworkElementRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementRn.setStatus(_A)
_CfprNetworkElementAdminInbandIfState_Type=CfprMgmtAdminState
_CfprNetworkElementAdminInbandIfState_Object=MibTableColumn
cfprNetworkElementAdminInbandIfState=_CfprNetworkElementAdminInbandIfState_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,4),_CfprNetworkElementAdminInbandIfState_Type())
cfprNetworkElementAdminInbandIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementAdminInbandIfState.setStatus(_A)
_CfprNetworkElementDiffMemory_Type=Gauge32
_CfprNetworkElementDiffMemory_Object=MibTableColumn
cfprNetworkElementDiffMemory=_CfprNetworkElementDiffMemory_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,5),_CfprNetworkElementDiffMemory_Type())
cfprNetworkElementDiffMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementDiffMemory.setStatus(_A)
_CfprNetworkElementExpectedMemory_Type=Gauge32
_CfprNetworkElementExpectedMemory_Object=MibTableColumn
cfprNetworkElementExpectedMemory=_CfprNetworkElementExpectedMemory_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,6),_CfprNetworkElementExpectedMemory_Type())
cfprNetworkElementExpectedMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementExpectedMemory.setStatus(_A)
_CfprNetworkElementFltAggr_Type=Unsigned64
_CfprNetworkElementFltAggr_Object=MibTableColumn
cfprNetworkElementFltAggr=_CfprNetworkElementFltAggr_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,7),_CfprNetworkElementFltAggr_Type())
cfprNetworkElementFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementFltAggr.setStatus(_A)
_CfprNetworkElementId_Type=CfprNetworkSwitchId
_CfprNetworkElementId_Object=MibTableColumn
cfprNetworkElementId=_CfprNetworkElementId_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,8),_CfprNetworkElementId_Type())
cfprNetworkElementId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementId.setStatus(_A)
_CfprNetworkElementInbandIfGw_Type=InetAddressIPv4
_CfprNetworkElementInbandIfGw_Object=MibTableColumn
cfprNetworkElementInbandIfGw=_CfprNetworkElementInbandIfGw_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,9),_CfprNetworkElementInbandIfGw_Type())
cfprNetworkElementInbandIfGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementInbandIfGw.setStatus(_A)
_CfprNetworkElementInbandIfIp_Type=InetAddressIPv4
_CfprNetworkElementInbandIfIp_Object=MibTableColumn
cfprNetworkElementInbandIfIp=_CfprNetworkElementInbandIfIp_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,10),_CfprNetworkElementInbandIfIp_Type())
cfprNetworkElementInbandIfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementInbandIfIp.setStatus(_A)
_CfprNetworkElementInbandIfMask_Type=InetAddressIPv4
_CfprNetworkElementInbandIfMask_Object=MibTableColumn
cfprNetworkElementInbandIfMask=_CfprNetworkElementInbandIfMask_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,11),_CfprNetworkElementInbandIfMask_Type())
cfprNetworkElementInbandIfMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementInbandIfMask.setStatus(_A)
_CfprNetworkElementInbandIfVnet_Type=Gauge32
_CfprNetworkElementInbandIfVnet_Object=MibTableColumn
cfprNetworkElementInbandIfVnet=_CfprNetworkElementInbandIfVnet_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,12),_CfprNetworkElementInbandIfVnet_Type())
cfprNetworkElementInbandIfVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementInbandIfVnet.setStatus(_A)
_CfprNetworkElementInventoryStatus_Type=CfprNetworkInventoryStatus
_CfprNetworkElementInventoryStatus_Object=MibTableColumn
cfprNetworkElementInventoryStatus=_CfprNetworkElementInventoryStatus_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,13),_CfprNetworkElementInventoryStatus_Type())
cfprNetworkElementInventoryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementInventoryStatus.setStatus(_A)
_CfprNetworkElementModel_Type=SnmpAdminString
_CfprNetworkElementModel_Object=MibTableColumn
cfprNetworkElementModel=_CfprNetworkElementModel_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,14),_CfprNetworkElementModel_Type())
cfprNetworkElementModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementModel.setStatus(_A)
_CfprNetworkElementOobIfGw_Type=InetAddressIPv4
_CfprNetworkElementOobIfGw_Object=MibTableColumn
cfprNetworkElementOobIfGw=_CfprNetworkElementOobIfGw_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,15),_CfprNetworkElementOobIfGw_Type())
cfprNetworkElementOobIfGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementOobIfGw.setStatus(_A)
_CfprNetworkElementOobIfIp_Type=InetAddressIPv4
_CfprNetworkElementOobIfIp_Object=MibTableColumn
cfprNetworkElementOobIfIp=_CfprNetworkElementOobIfIp_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,16),_CfprNetworkElementOobIfIp_Type())
cfprNetworkElementOobIfIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementOobIfIp.setStatus(_A)
_CfprNetworkElementOobIfMask_Type=InetAddressIPv4
_CfprNetworkElementOobIfMask_Object=MibTableColumn
cfprNetworkElementOobIfMask=_CfprNetworkElementOobIfMask_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,17),_CfprNetworkElementOobIfMask_Type())
cfprNetworkElementOobIfMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementOobIfMask.setStatus(_A)
_CfprNetworkElementOperability_Type=CfprNetworkElementOperability
_CfprNetworkElementOperability_Object=MibTableColumn
cfprNetworkElementOperability=_CfprNetworkElementOperability_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,18),_CfprNetworkElementOperability_Type())
cfprNetworkElementOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementOperability.setStatus(_A)
_CfprNetworkElementRevision_Type=SnmpAdminString
_CfprNetworkElementRevision_Object=MibTableColumn
cfprNetworkElementRevision=_CfprNetworkElementRevision_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,19),_CfprNetworkElementRevision_Type())
cfprNetworkElementRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementRevision.setStatus(_A)
_CfprNetworkElementSerial_Type=SnmpAdminString
_CfprNetworkElementSerial_Object=MibTableColumn
cfprNetworkElementSerial=_CfprNetworkElementSerial_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,20),_CfprNetworkElementSerial_Type())
cfprNetworkElementSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementSerial.setStatus(_A)
_CfprNetworkElementThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprNetworkElementThermal_Object=MibTableColumn
cfprNetworkElementThermal=_CfprNetworkElementThermal_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,21),_CfprNetworkElementThermal_Type())
cfprNetworkElementThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementThermal.setStatus(_A)
_CfprNetworkElementTotalMemory_Type=Gauge32
_CfprNetworkElementTotalMemory_Object=MibTableColumn
cfprNetworkElementTotalMemory=_CfprNetworkElementTotalMemory_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,22),_CfprNetworkElementTotalMemory_Type())
cfprNetworkElementTotalMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementTotalMemory.setStatus(_A)
_CfprNetworkElementVendor_Type=SnmpAdminString
_CfprNetworkElementVendor_Object=MibTableColumn
cfprNetworkElementVendor=_CfprNetworkElementVendor_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,23),_CfprNetworkElementVendor_Type())
cfprNetworkElementVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementVendor.setStatus(_A)
_CfprNetworkElementIcapCount_Type=Gauge32
_CfprNetworkElementIcapCount_Object=MibTableColumn
cfprNetworkElementIcapCount=_CfprNetworkElementIcapCount_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,24),_CfprNetworkElementIcapCount_Type())
cfprNetworkElementIcapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementIcapCount.setStatus(_A)
_CfprNetworkElementIcapCountString_Type=SnmpAdminString
_CfprNetworkElementIcapCountString_Object=MibTableColumn
cfprNetworkElementIcapCountString=_CfprNetworkElementIcapCountString_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,25),_CfprNetworkElementIcapCountString_Type())
cfprNetworkElementIcapCountString.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementIcapCountString.setStatus(_A)
_CfprNetworkElementMaxIcapCount_Type=Gauge32
_CfprNetworkElementMaxIcapCount_Object=MibTableColumn
cfprNetworkElementMaxIcapCount=_CfprNetworkElementMaxIcapCount_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,26),_CfprNetworkElementMaxIcapCount_Type())
cfprNetworkElementMaxIcapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementMaxIcapCount.setStatus(_A)
_CfprNetworkElementMaxVcapCount_Type=Gauge32
_CfprNetworkElementMaxVcapCount_Object=MibTableColumn
cfprNetworkElementMaxVcapCount=_CfprNetworkElementMaxVcapCount_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,27),_CfprNetworkElementMaxVcapCount_Type())
cfprNetworkElementMaxVcapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementMaxVcapCount.setStatus(_A)
_CfprNetworkElementSamConfigStatus_Type=CfprNetworkSamConfigStatus
_CfprNetworkElementSamConfigStatus_Object=MibTableColumn
cfprNetworkElementSamConfigStatus=_CfprNetworkElementSamConfigStatus_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,28),_CfprNetworkElementSamConfigStatus_Type())
cfprNetworkElementSamConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementSamConfigStatus.setStatus(_A)
_CfprNetworkElementVcapCount_Type=Gauge32
_CfprNetworkElementVcapCount_Object=MibTableColumn
cfprNetworkElementVcapCount=_CfprNetworkElementVcapCount_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,29),_CfprNetworkElementVcapCount_Type())
cfprNetworkElementVcapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementVcapCount.setStatus(_A)
_CfprNetworkElementVcapCountString_Type=SnmpAdminString
_CfprNetworkElementVcapCountString_Object=MibTableColumn
cfprNetworkElementVcapCountString=_CfprNetworkElementVcapCountString_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,30),_CfprNetworkElementVcapCountString_Type())
cfprNetworkElementVcapCountString.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementVcapCountString.setStatus(_A)
_CfprNetworkElementVid_Type=SnmpAdminString
_CfprNetworkElementVid_Object=MibTableColumn
cfprNetworkElementVid=_CfprNetworkElementVid_Object((1,3,6,1,4,1,9,9,826,1,52,1,1,31),_CfprNetworkElementVid_Type())
cfprNetworkElementVid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkElementVid.setStatus(_A)
_CfprNetworkIfStatsTable_Object=MibTable
cfprNetworkIfStatsTable=_CfprNetworkIfStatsTable_Object((1,3,6,1,4,1,9,9,826,1,52,2))
if mibBuilder.loadTexts:cfprNetworkIfStatsTable.setStatus(_A)
_CfprNetworkIfStatsEntry_Object=MibTableRow
cfprNetworkIfStatsEntry=_CfprNetworkIfStatsEntry_Object((1,3,6,1,4,1,9,9,826,1,52,2,1))
cfprNetworkIfStatsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprNetworkIfStatsEntry.setStatus(_A)
_CfprNetworkIfStatsInstanceId_Type=CfprManagedObjectId
_CfprNetworkIfStatsInstanceId_Object=MibTableColumn
cfprNetworkIfStatsInstanceId=_CfprNetworkIfStatsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,1),_CfprNetworkIfStatsInstanceId_Type())
cfprNetworkIfStatsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkIfStatsInstanceId.setStatus(_A)
_CfprNetworkIfStatsDn_Type=CfprManagedObjectDn
_CfprNetworkIfStatsDn_Object=MibTableColumn
cfprNetworkIfStatsDn=_CfprNetworkIfStatsDn_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,2),_CfprNetworkIfStatsDn_Type())
cfprNetworkIfStatsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkIfStatsDn.setStatus(_A)
_CfprNetworkIfStatsRn_Type=SnmpAdminString
_CfprNetworkIfStatsRn_Object=MibTableColumn
cfprNetworkIfStatsRn=_CfprNetworkIfStatsRn_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,3),_CfprNetworkIfStatsRn_Type())
cfprNetworkIfStatsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkIfStatsRn.setStatus(_A)
_CfprNetworkIfStatsOut_Type=Unsigned64
_CfprNetworkIfStatsOut_Object=MibTableColumn
cfprNetworkIfStatsOut=_CfprNetworkIfStatsOut_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,4),_CfprNetworkIfStatsOut_Type())
cfprNetworkIfStatsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkIfStatsOut.setStatus(_A)
_CfprNetworkIfStatsRin_Type=Unsigned64
_CfprNetworkIfStatsRin_Object=MibTableColumn
cfprNetworkIfStatsRin=_CfprNetworkIfStatsRin_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,5),_CfprNetworkIfStatsRin_Type())
cfprNetworkIfStatsRin.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkIfStatsRin.setStatus(_A)
_CfprNetworkIfStatsType_Type=CfprNetworkIfStatsType
_CfprNetworkIfStatsType_Object=MibTableColumn
cfprNetworkIfStatsType=_CfprNetworkIfStatsType_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,6),_CfprNetworkIfStatsType_Type())
cfprNetworkIfStatsType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkIfStatsType.setStatus(_A)
_CfprNetworkIfStatsUnits_Type=CfprNetworkIfStatsUnits
_CfprNetworkIfStatsUnits_Object=MibTableColumn
cfprNetworkIfStatsUnits=_CfprNetworkIfStatsUnits_Object((1,3,6,1,4,1,9,9,826,1,52,2,1,7),_CfprNetworkIfStatsUnits_Type())
cfprNetworkIfStatsUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkIfStatsUnits.setStatus(_A)
_CfprNetworkLanNeighborEntryTable_Object=MibTable
cfprNetworkLanNeighborEntryTable=_CfprNetworkLanNeighborEntryTable_Object((1,3,6,1,4,1,9,9,826,1,52,3))
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryTable.setStatus(_A)
_CfprNetworkLanNeighborEntryEntry_Object=MibTableRow
cfprNetworkLanNeighborEntryEntry=_CfprNetworkLanNeighborEntryEntry_Object((1,3,6,1,4,1,9,9,826,1,52,3,1))
cfprNetworkLanNeighborEntryEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryEntry.setStatus(_A)
_CfprNetworkLanNeighborEntryInstanceId_Type=CfprManagedObjectId
_CfprNetworkLanNeighborEntryInstanceId_Object=MibTableColumn
cfprNetworkLanNeighborEntryInstanceId=_CfprNetworkLanNeighborEntryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,1),_CfprNetworkLanNeighborEntryInstanceId_Type())
cfprNetworkLanNeighborEntryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryInstanceId.setStatus(_A)
_CfprNetworkLanNeighborEntryDn_Type=CfprManagedObjectDn
_CfprNetworkLanNeighborEntryDn_Object=MibTableColumn
cfprNetworkLanNeighborEntryDn=_CfprNetworkLanNeighborEntryDn_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,2),_CfprNetworkLanNeighborEntryDn_Type())
cfprNetworkLanNeighborEntryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryDn.setStatus(_A)
_CfprNetworkLanNeighborEntryRn_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryRn_Object=MibTableColumn
cfprNetworkLanNeighborEntryRn=_CfprNetworkLanNeighborEntryRn_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,3),_CfprNetworkLanNeighborEntryRn_Type())
cfprNetworkLanNeighborEntryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryRn.setStatus(_A)
_CfprNetworkLanNeighborEntryCapabilities_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryCapabilities_Object=MibTableColumn
cfprNetworkLanNeighborEntryCapabilities=_CfprNetworkLanNeighborEntryCapabilities_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,4),_CfprNetworkLanNeighborEntryCapabilities_Type())
cfprNetworkLanNeighborEntryCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryCapabilities.setStatus(_A)
_CfprNetworkLanNeighborEntryDeviceId_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryDeviceId_Object=MibTableColumn
cfprNetworkLanNeighborEntryDeviceId=_CfprNetworkLanNeighborEntryDeviceId_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,5),_CfprNetworkLanNeighborEntryDeviceId_Type())
cfprNetworkLanNeighborEntryDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryDeviceId.setStatus(_A)
_CfprNetworkLanNeighborEntryFiPortDn_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryFiPortDn_Object=MibTableColumn
cfprNetworkLanNeighborEntryFiPortDn=_CfprNetworkLanNeighborEntryFiPortDn_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,6),_CfprNetworkLanNeighborEntryFiPortDn_Type())
cfprNetworkLanNeighborEntryFiPortDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryFiPortDn.setStatus(_A)
_CfprNetworkLanNeighborEntryIpV4Address_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryIpV4Address_Object=MibTableColumn
cfprNetworkLanNeighborEntryIpV4Address=_CfprNetworkLanNeighborEntryIpV4Address_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,7),_CfprNetworkLanNeighborEntryIpV4Address_Type())
cfprNetworkLanNeighborEntryIpV4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryIpV4Address.setStatus(_A)
_CfprNetworkLanNeighborEntryIpV4MgmtAddress_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryIpV4MgmtAddress_Object=MibTableColumn
cfprNetworkLanNeighborEntryIpV4MgmtAddress=_CfprNetworkLanNeighborEntryIpV4MgmtAddress_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,8),_CfprNetworkLanNeighborEntryIpV4MgmtAddress_Type())
cfprNetworkLanNeighborEntryIpV4MgmtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryIpV4MgmtAddress.setStatus(_A)
_CfprNetworkLanNeighborEntryLocalInterface_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryLocalInterface_Object=MibTableColumn
cfprNetworkLanNeighborEntryLocalInterface=_CfprNetworkLanNeighborEntryLocalInterface_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,9),_CfprNetworkLanNeighborEntryLocalInterface_Type())
cfprNetworkLanNeighborEntryLocalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryLocalInterface.setStatus(_A)
_CfprNetworkLanNeighborEntryNativeVlan_Type=Gauge32
_CfprNetworkLanNeighborEntryNativeVlan_Object=MibTableColumn
cfprNetworkLanNeighborEntryNativeVlan=_CfprNetworkLanNeighborEntryNativeVlan_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,10),_CfprNetworkLanNeighborEntryNativeVlan_Type())
cfprNetworkLanNeighborEntryNativeVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryNativeVlan.setStatus(_A)
_CfprNetworkLanNeighborEntryPlatform_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryPlatform_Object=MibTableColumn
cfprNetworkLanNeighborEntryPlatform=_CfprNetworkLanNeighborEntryPlatform_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,11),_CfprNetworkLanNeighborEntryPlatform_Type())
cfprNetworkLanNeighborEntryPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryPlatform.setStatus(_A)
_CfprNetworkLanNeighborEntryRemoteInterface_Type=SnmpAdminString
_CfprNetworkLanNeighborEntryRemoteInterface_Object=MibTableColumn
cfprNetworkLanNeighborEntryRemoteInterface=_CfprNetworkLanNeighborEntryRemoteInterface_Object((1,3,6,1,4,1,9,9,826,1,52,3,1,12),_CfprNetworkLanNeighborEntryRemoteInterface_Type())
cfprNetworkLanNeighborEntryRemoteInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborEntryRemoteInterface.setStatus(_A)
_CfprNetworkLanNeighborsTable_Object=MibTable
cfprNetworkLanNeighborsTable=_CfprNetworkLanNeighborsTable_Object((1,3,6,1,4,1,9,9,826,1,52,4))
if mibBuilder.loadTexts:cfprNetworkLanNeighborsTable.setStatus(_A)
_CfprNetworkLanNeighborsEntry_Object=MibTableRow
cfprNetworkLanNeighborsEntry=_CfprNetworkLanNeighborsEntry_Object((1,3,6,1,4,1,9,9,826,1,52,4,1))
cfprNetworkLanNeighborsEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprNetworkLanNeighborsEntry.setStatus(_A)
_CfprNetworkLanNeighborsInstanceId_Type=CfprManagedObjectId
_CfprNetworkLanNeighborsInstanceId_Object=MibTableColumn
cfprNetworkLanNeighborsInstanceId=_CfprNetworkLanNeighborsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,4,1,1),_CfprNetworkLanNeighborsInstanceId_Type())
cfprNetworkLanNeighborsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkLanNeighborsInstanceId.setStatus(_A)
_CfprNetworkLanNeighborsDn_Type=CfprManagedObjectDn
_CfprNetworkLanNeighborsDn_Object=MibTableColumn
cfprNetworkLanNeighborsDn=_CfprNetworkLanNeighborsDn_Object((1,3,6,1,4,1,9,9,826,1,52,4,1,2),_CfprNetworkLanNeighborsDn_Type())
cfprNetworkLanNeighborsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborsDn.setStatus(_A)
_CfprNetworkLanNeighborsRn_Type=SnmpAdminString
_CfprNetworkLanNeighborsRn_Object=MibTableColumn
cfprNetworkLanNeighborsRn=_CfprNetworkLanNeighborsRn_Object((1,3,6,1,4,1,9,9,826,1,52,4,1,3),_CfprNetworkLanNeighborsRn_Type())
cfprNetworkLanNeighborsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkLanNeighborsRn.setStatus(_A)
_CfprNetworkOperLevelTable_Object=MibTable
cfprNetworkOperLevelTable=_CfprNetworkOperLevelTable_Object((1,3,6,1,4,1,9,9,826,1,52,5))
if mibBuilder.loadTexts:cfprNetworkOperLevelTable.setStatus(_A)
_CfprNetworkOperLevelEntry_Object=MibTableRow
cfprNetworkOperLevelEntry=_CfprNetworkOperLevelEntry_Object((1,3,6,1,4,1,9,9,826,1,52,5,1))
cfprNetworkOperLevelEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprNetworkOperLevelEntry.setStatus(_A)
_CfprNetworkOperLevelInstanceId_Type=CfprManagedObjectId
_CfprNetworkOperLevelInstanceId_Object=MibTableColumn
cfprNetworkOperLevelInstanceId=_CfprNetworkOperLevelInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,1),_CfprNetworkOperLevelInstanceId_Type())
cfprNetworkOperLevelInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkOperLevelInstanceId.setStatus(_A)
_CfprNetworkOperLevelDn_Type=CfprManagedObjectDn
_CfprNetworkOperLevelDn_Object=MibTableColumn
cfprNetworkOperLevelDn=_CfprNetworkOperLevelDn_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,2),_CfprNetworkOperLevelDn_Type())
cfprNetworkOperLevelDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelDn.setStatus(_A)
_CfprNetworkOperLevelRn_Type=SnmpAdminString
_CfprNetworkOperLevelRn_Object=MibTableColumn
cfprNetworkOperLevelRn=_CfprNetworkOperLevelRn_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,3),_CfprNetworkOperLevelRn_Type())
cfprNetworkOperLevelRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelRn.setStatus(_A)
_CfprNetworkOperLevelId_Type=CfprNetworkSwitchId
_CfprNetworkOperLevelId_Object=MibTableColumn
cfprNetworkOperLevelId=_CfprNetworkOperLevelId_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,4),_CfprNetworkOperLevelId_Type())
cfprNetworkOperLevelId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelId.setStatus(_A)
_CfprNetworkOperLevelMaxPrimaryVlanCount_Type=Gauge32
_CfprNetworkOperLevelMaxPrimaryVlanCount_Object=MibTableColumn
cfprNetworkOperLevelMaxPrimaryVlanCount=_CfprNetworkOperLevelMaxPrimaryVlanCount_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,5),_CfprNetworkOperLevelMaxPrimaryVlanCount_Type())
cfprNetworkOperLevelMaxPrimaryVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelMaxPrimaryVlanCount.setStatus(_A)
_CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type=Gauge32
_CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object=MibTableColumn
cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount=_CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,6),_CfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount_Type())
cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount.setStatus(_A)
_CfprNetworkOperLevelMaxSecondaryVlanCount_Type=Gauge32
_CfprNetworkOperLevelMaxSecondaryVlanCount_Object=MibTableColumn
cfprNetworkOperLevelMaxSecondaryVlanCount=_CfprNetworkOperLevelMaxSecondaryVlanCount_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,7),_CfprNetworkOperLevelMaxSecondaryVlanCount_Type())
cfprNetworkOperLevelMaxSecondaryVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelMaxSecondaryVlanCount.setStatus(_A)
_CfprNetworkOperLevelPrimaryVlanCount_Type=Gauge32
_CfprNetworkOperLevelPrimaryVlanCount_Object=MibTableColumn
cfprNetworkOperLevelPrimaryVlanCount=_CfprNetworkOperLevelPrimaryVlanCount_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,8),_CfprNetworkOperLevelPrimaryVlanCount_Type())
cfprNetworkOperLevelPrimaryVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelPrimaryVlanCount.setStatus(_A)
_CfprNetworkOperLevelPrimaryVlanCountStatus_Type=CfprNetworkVlanCountStatus
_CfprNetworkOperLevelPrimaryVlanCountStatus_Object=MibTableColumn
cfprNetworkOperLevelPrimaryVlanCountStatus=_CfprNetworkOperLevelPrimaryVlanCountStatus_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,9),_CfprNetworkOperLevelPrimaryVlanCountStatus_Type())
cfprNetworkOperLevelPrimaryVlanCountStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelPrimaryVlanCountStatus.setStatus(_A)
_CfprNetworkOperLevelSecondaryVlanCount_Type=Gauge32
_CfprNetworkOperLevelSecondaryVlanCount_Object=MibTableColumn
cfprNetworkOperLevelSecondaryVlanCount=_CfprNetworkOperLevelSecondaryVlanCount_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,10),_CfprNetworkOperLevelSecondaryVlanCount_Type())
cfprNetworkOperLevelSecondaryVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelSecondaryVlanCount.setStatus(_A)
_CfprNetworkOperLevelSecondaryVlanCountStatus_Type=CfprNetworkVlanCountStatus
_CfprNetworkOperLevelSecondaryVlanCountStatus_Object=MibTableColumn
cfprNetworkOperLevelSecondaryVlanCountStatus=_CfprNetworkOperLevelSecondaryVlanCountStatus_Object((1,3,6,1,4,1,9,9,826,1,52,5,1,11),_CfprNetworkOperLevelSecondaryVlanCountStatus_Type())
cfprNetworkOperLevelSecondaryVlanCountStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkOperLevelSecondaryVlanCountStatus.setStatus(_A)
_CfprNetworkSanNeighborEntryTable_Object=MibTable
cfprNetworkSanNeighborEntryTable=_CfprNetworkSanNeighborEntryTable_Object((1,3,6,1,4,1,9,9,826,1,52,6))
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryTable.setStatus(_A)
_CfprNetworkSanNeighborEntryEntry_Object=MibTableRow
cfprNetworkSanNeighborEntryEntry=_CfprNetworkSanNeighborEntryEntry_Object((1,3,6,1,4,1,9,9,826,1,52,6,1))
cfprNetworkSanNeighborEntryEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryEntry.setStatus(_A)
_CfprNetworkSanNeighborEntryInstanceId_Type=CfprManagedObjectId
_CfprNetworkSanNeighborEntryInstanceId_Object=MibTableColumn
cfprNetworkSanNeighborEntryInstanceId=_CfprNetworkSanNeighborEntryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,1),_CfprNetworkSanNeighborEntryInstanceId_Type())
cfprNetworkSanNeighborEntryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryInstanceId.setStatus(_A)
_CfprNetworkSanNeighborEntryDn_Type=CfprManagedObjectDn
_CfprNetworkSanNeighborEntryDn_Object=MibTableColumn
cfprNetworkSanNeighborEntryDn=_CfprNetworkSanNeighborEntryDn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,2),_CfprNetworkSanNeighborEntryDn_Type())
cfprNetworkSanNeighborEntryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryDn.setStatus(_A)
_CfprNetworkSanNeighborEntryRn_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryRn_Object=MibTableColumn
cfprNetworkSanNeighborEntryRn=_CfprNetworkSanNeighborEntryRn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,3),_CfprNetworkSanNeighborEntryRn_Type())
cfprNetworkSanNeighborEntryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryRn.setStatus(_A)
_CfprNetworkSanNeighborEntryFabricMgmtAddr_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryFabricMgmtAddr_Object=MibTableColumn
cfprNetworkSanNeighborEntryFabricMgmtAddr=_CfprNetworkSanNeighborEntryFabricMgmtAddr_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,4),_CfprNetworkSanNeighborEntryFabricMgmtAddr_Type())
cfprNetworkSanNeighborEntryFabricMgmtAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryFabricMgmtAddr.setStatus(_A)
_CfprNetworkSanNeighborEntryFabricNwwn_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryFabricNwwn_Object=MibTableColumn
cfprNetworkSanNeighborEntryFabricNwwn=_CfprNetworkSanNeighborEntryFabricNwwn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,5),_CfprNetworkSanNeighborEntryFabricNwwn_Type())
cfprNetworkSanNeighborEntryFabricNwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryFabricNwwn.setStatus(_A)
_CfprNetworkSanNeighborEntryFabricPwwn_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryFabricPwwn_Object=MibTableColumn
cfprNetworkSanNeighborEntryFabricPwwn=_CfprNetworkSanNeighborEntryFabricPwwn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,6),_CfprNetworkSanNeighborEntryFabricPwwn_Type())
cfprNetworkSanNeighborEntryFabricPwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryFabricPwwn.setStatus(_A)
_CfprNetworkSanNeighborEntryFiPortDn_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryFiPortDn_Object=MibTableColumn
cfprNetworkSanNeighborEntryFiPortDn=_CfprNetworkSanNeighborEntryFiPortDn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,7),_CfprNetworkSanNeighborEntryFiPortDn_Type())
cfprNetworkSanNeighborEntryFiPortDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryFiPortDn.setStatus(_A)
_CfprNetworkSanNeighborEntryLocalInterface_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryLocalInterface_Object=MibTableColumn
cfprNetworkSanNeighborEntryLocalInterface=_CfprNetworkSanNeighborEntryLocalInterface_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,8),_CfprNetworkSanNeighborEntryLocalInterface_Type())
cfprNetworkSanNeighborEntryLocalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryLocalInterface.setStatus(_A)
_CfprNetworkSanNeighborEntryMyNwwn_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryMyNwwn_Object=MibTableColumn
cfprNetworkSanNeighborEntryMyNwwn=_CfprNetworkSanNeighborEntryMyNwwn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,9),_CfprNetworkSanNeighborEntryMyNwwn_Type())
cfprNetworkSanNeighborEntryMyNwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryMyNwwn.setStatus(_A)
_CfprNetworkSanNeighborEntryMyPwwn_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryMyPwwn_Object=MibTableColumn
cfprNetworkSanNeighborEntryMyPwwn=_CfprNetworkSanNeighborEntryMyPwwn_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,10),_CfprNetworkSanNeighborEntryMyPwwn_Type())
cfprNetworkSanNeighborEntryMyPwwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryMyPwwn.setStatus(_A)
_CfprNetworkSanNeighborEntryPortVsan_Type=SnmpAdminString
_CfprNetworkSanNeighborEntryPortVsan_Object=MibTableColumn
cfprNetworkSanNeighborEntryPortVsan=_CfprNetworkSanNeighborEntryPortVsan_Object((1,3,6,1,4,1,9,9,826,1,52,6,1,11),_CfprNetworkSanNeighborEntryPortVsan_Type())
cfprNetworkSanNeighborEntryPortVsan.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborEntryPortVsan.setStatus(_A)
_CfprNetworkSanNeighborsTable_Object=MibTable
cfprNetworkSanNeighborsTable=_CfprNetworkSanNeighborsTable_Object((1,3,6,1,4,1,9,9,826,1,52,7))
if mibBuilder.loadTexts:cfprNetworkSanNeighborsTable.setStatus(_A)
_CfprNetworkSanNeighborsEntry_Object=MibTableRow
cfprNetworkSanNeighborsEntry=_CfprNetworkSanNeighborsEntry_Object((1,3,6,1,4,1,9,9,826,1,52,7,1))
cfprNetworkSanNeighborsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprNetworkSanNeighborsEntry.setStatus(_A)
_CfprNetworkSanNeighborsInstanceId_Type=CfprManagedObjectId
_CfprNetworkSanNeighborsInstanceId_Object=MibTableColumn
cfprNetworkSanNeighborsInstanceId=_CfprNetworkSanNeighborsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,52,7,1,1),_CfprNetworkSanNeighborsInstanceId_Type())
cfprNetworkSanNeighborsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNetworkSanNeighborsInstanceId.setStatus(_A)
_CfprNetworkSanNeighborsDn_Type=CfprManagedObjectDn
_CfprNetworkSanNeighborsDn_Object=MibTableColumn
cfprNetworkSanNeighborsDn=_CfprNetworkSanNeighborsDn_Object((1,3,6,1,4,1,9,9,826,1,52,7,1,2),_CfprNetworkSanNeighborsDn_Type())
cfprNetworkSanNeighborsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborsDn.setStatus(_A)
_CfprNetworkSanNeighborsRn_Type=SnmpAdminString
_CfprNetworkSanNeighborsRn_Object=MibTableColumn
cfprNetworkSanNeighborsRn=_CfprNetworkSanNeighborsRn_Object((1,3,6,1,4,1,9,9,826,1,52,7,1,3),_CfprNetworkSanNeighborsRn_Type())
cfprNetworkSanNeighborsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNetworkSanNeighborsRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprNetworkObjects':cfprNetworkObjects,'cfprNetworkElementTable':cfprNetworkElementTable,'cfprNetworkElementEntry':cfprNetworkElementEntry,_E:cfprNetworkElementInstanceId,'cfprNetworkElementDn':cfprNetworkElementDn,'cfprNetworkElementRn':cfprNetworkElementRn,'cfprNetworkElementAdminInbandIfState':cfprNetworkElementAdminInbandIfState,'cfprNetworkElementDiffMemory':cfprNetworkElementDiffMemory,'cfprNetworkElementExpectedMemory':cfprNetworkElementExpectedMemory,'cfprNetworkElementFltAggr':cfprNetworkElementFltAggr,'cfprNetworkElementId':cfprNetworkElementId,'cfprNetworkElementInbandIfGw':cfprNetworkElementInbandIfGw,'cfprNetworkElementInbandIfIp':cfprNetworkElementInbandIfIp,'cfprNetworkElementInbandIfMask':cfprNetworkElementInbandIfMask,'cfprNetworkElementInbandIfVnet':cfprNetworkElementInbandIfVnet,'cfprNetworkElementInventoryStatus':cfprNetworkElementInventoryStatus,'cfprNetworkElementModel':cfprNetworkElementModel,'cfprNetworkElementOobIfGw':cfprNetworkElementOobIfGw,'cfprNetworkElementOobIfIp':cfprNetworkElementOobIfIp,'cfprNetworkElementOobIfMask':cfprNetworkElementOobIfMask,'cfprNetworkElementOperability':cfprNetworkElementOperability,'cfprNetworkElementRevision':cfprNetworkElementRevision,'cfprNetworkElementSerial':cfprNetworkElementSerial,'cfprNetworkElementThermal':cfprNetworkElementThermal,'cfprNetworkElementTotalMemory':cfprNetworkElementTotalMemory,'cfprNetworkElementVendor':cfprNetworkElementVendor,'cfprNetworkElementIcapCount':cfprNetworkElementIcapCount,'cfprNetworkElementIcapCountString':cfprNetworkElementIcapCountString,'cfprNetworkElementMaxIcapCount':cfprNetworkElementMaxIcapCount,'cfprNetworkElementMaxVcapCount':cfprNetworkElementMaxVcapCount,'cfprNetworkElementSamConfigStatus':cfprNetworkElementSamConfigStatus,'cfprNetworkElementVcapCount':cfprNetworkElementVcapCount,'cfprNetworkElementVcapCountString':cfprNetworkElementVcapCountString,'cfprNetworkElementVid':cfprNetworkElementVid,'cfprNetworkIfStatsTable':cfprNetworkIfStatsTable,'cfprNetworkIfStatsEntry':cfprNetworkIfStatsEntry,_F:cfprNetworkIfStatsInstanceId,'cfprNetworkIfStatsDn':cfprNetworkIfStatsDn,'cfprNetworkIfStatsRn':cfprNetworkIfStatsRn,'cfprNetworkIfStatsOut':cfprNetworkIfStatsOut,'cfprNetworkIfStatsRin':cfprNetworkIfStatsRin,'cfprNetworkIfStatsType':cfprNetworkIfStatsType,'cfprNetworkIfStatsUnits':cfprNetworkIfStatsUnits,'cfprNetworkLanNeighborEntryTable':cfprNetworkLanNeighborEntryTable,'cfprNetworkLanNeighborEntryEntry':cfprNetworkLanNeighborEntryEntry,_G:cfprNetworkLanNeighborEntryInstanceId,'cfprNetworkLanNeighborEntryDn':cfprNetworkLanNeighborEntryDn,'cfprNetworkLanNeighborEntryRn':cfprNetworkLanNeighborEntryRn,'cfprNetworkLanNeighborEntryCapabilities':cfprNetworkLanNeighborEntryCapabilities,'cfprNetworkLanNeighborEntryDeviceId':cfprNetworkLanNeighborEntryDeviceId,'cfprNetworkLanNeighborEntryFiPortDn':cfprNetworkLanNeighborEntryFiPortDn,'cfprNetworkLanNeighborEntryIpV4Address':cfprNetworkLanNeighborEntryIpV4Address,'cfprNetworkLanNeighborEntryIpV4MgmtAddress':cfprNetworkLanNeighborEntryIpV4MgmtAddress,'cfprNetworkLanNeighborEntryLocalInterface':cfprNetworkLanNeighborEntryLocalInterface,'cfprNetworkLanNeighborEntryNativeVlan':cfprNetworkLanNeighborEntryNativeVlan,'cfprNetworkLanNeighborEntryPlatform':cfprNetworkLanNeighborEntryPlatform,'cfprNetworkLanNeighborEntryRemoteInterface':cfprNetworkLanNeighborEntryRemoteInterface,'cfprNetworkLanNeighborsTable':cfprNetworkLanNeighborsTable,'cfprNetworkLanNeighborsEntry':cfprNetworkLanNeighborsEntry,_H:cfprNetworkLanNeighborsInstanceId,'cfprNetworkLanNeighborsDn':cfprNetworkLanNeighborsDn,'cfprNetworkLanNeighborsRn':cfprNetworkLanNeighborsRn,'cfprNetworkOperLevelTable':cfprNetworkOperLevelTable,'cfprNetworkOperLevelEntry':cfprNetworkOperLevelEntry,_I:cfprNetworkOperLevelInstanceId,'cfprNetworkOperLevelDn':cfprNetworkOperLevelDn,'cfprNetworkOperLevelRn':cfprNetworkOperLevelRn,'cfprNetworkOperLevelId':cfprNetworkOperLevelId,'cfprNetworkOperLevelMaxPrimaryVlanCount':cfprNetworkOperLevelMaxPrimaryVlanCount,'cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount':cfprNetworkOperLevelMaxSecVlanPerPrimaryVlanCount,'cfprNetworkOperLevelMaxSecondaryVlanCount':cfprNetworkOperLevelMaxSecondaryVlanCount,'cfprNetworkOperLevelPrimaryVlanCount':cfprNetworkOperLevelPrimaryVlanCount,'cfprNetworkOperLevelPrimaryVlanCountStatus':cfprNetworkOperLevelPrimaryVlanCountStatus,'cfprNetworkOperLevelSecondaryVlanCount':cfprNetworkOperLevelSecondaryVlanCount,'cfprNetworkOperLevelSecondaryVlanCountStatus':cfprNetworkOperLevelSecondaryVlanCountStatus,'cfprNetworkSanNeighborEntryTable':cfprNetworkSanNeighborEntryTable,'cfprNetworkSanNeighborEntryEntry':cfprNetworkSanNeighborEntryEntry,_J:cfprNetworkSanNeighborEntryInstanceId,'cfprNetworkSanNeighborEntryDn':cfprNetworkSanNeighborEntryDn,'cfprNetworkSanNeighborEntryRn':cfprNetworkSanNeighborEntryRn,'cfprNetworkSanNeighborEntryFabricMgmtAddr':cfprNetworkSanNeighborEntryFabricMgmtAddr,'cfprNetworkSanNeighborEntryFabricNwwn':cfprNetworkSanNeighborEntryFabricNwwn,'cfprNetworkSanNeighborEntryFabricPwwn':cfprNetworkSanNeighborEntryFabricPwwn,'cfprNetworkSanNeighborEntryFiPortDn':cfprNetworkSanNeighborEntryFiPortDn,'cfprNetworkSanNeighborEntryLocalInterface':cfprNetworkSanNeighborEntryLocalInterface,'cfprNetworkSanNeighborEntryMyNwwn':cfprNetworkSanNeighborEntryMyNwwn,'cfprNetworkSanNeighborEntryMyPwwn':cfprNetworkSanNeighborEntryMyPwwn,'cfprNetworkSanNeighborEntryPortVsan':cfprNetworkSanNeighborEntryPortVsan,'cfprNetworkSanNeighborsTable':cfprNetworkSanNeighborsTable,'cfprNetworkSanNeighborsEntry':cfprNetworkSanNeighborsEntry,_K:cfprNetworkSanNeighborsInstanceId,'cfprNetworkSanNeighborsDn':cfprNetworkSanNeighborsDn,'cfprNetworkSanNeighborsRn':cfprNetworkSanNeighborsRn})