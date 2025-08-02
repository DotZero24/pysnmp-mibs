_O='mwApVpnClientInfoTableIndex'
_N='mwApCertificateTableIndex'
_M='mwApConnectivityTableIndex'
_L='mwApSwapTableIndex'
_K='mwApip2controllerMapTableIndex'
_J='mwAp2controllerMapTableIndex'
_I='mwApTableIndex'
_H='Integer32'
_G='not-accessible'
_F='MERU-CONFIG-AP-MIB'
_E='DisplayString'
_D='read-write'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlAlarmState,MwlApDiscoveryState,MwlApHwType,MwlApIndoorOutdoorType,MwlApIpAssignmentType,MwlAvailabilityStatus,MwlCertRequestStatus,MwlCertificateStatus,MwlDiscoveryOrder,MwlEnableDisableOption,MwlLedMode,MwlOnOffSwitch,MwlOperationalState,MwlPowerSupply,MwlVpnAuthenticationStatus,MwlVpnAuthenticationType,MwlVpnConnectivityStatus,MwlVpnMode=mibBuilder.importSymbols('MERU-TC','MwlAlarmState','MwlApDiscoveryState','MwlApHwType','MwlApIndoorOutdoorType','MwlApIpAssignmentType','MwlAvailabilityStatus','MwlCertRequestStatus','MwlCertificateStatus','MwlDiscoveryOrder','MwlEnableDisableOption','MwlLedMode','MwlOnOffSwitch','MwlOperationalState','MwlPowerSupply','MwlVpnAuthenticationStatus','MwlVpnAuthenticationType','MwlVpnConnectivityStatus','MwlVpnMode')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigAp=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,2))
_MwApTable_Object=MibTable
mwApTable=_MwApTable_Object((1,3,6,1,4,1,15983,1,1,4,2,1))
if mibBuilder.loadTexts:mwApTable.setStatus(_A)
_MwApEntry_Object=MibTableRow
mwApEntry=_MwApEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1))
mwApEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:mwApEntry.setStatus(_A)
_MwApTableIndex_Type=Integer32
_MwApTableIndex_Object=MibTableColumn
mwApTableIndex=_MwApTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,1),_MwApTableIndex_Type())
mwApTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwApTableIndex.setStatus(_A)
class _MwApDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_MwApDescr_Type.__name__=_E
_MwApDescr_Object=MibTableColumn
mwApDescr=_MwApDescr_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,2),_MwApDescr_Type())
mwApDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApDescr.setStatus(_A)
class _MwApFloor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwApFloor_Type.__name__=_E
_MwApFloor_Object=MibTableColumn
mwApFloor=_MwApFloor_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,3),_MwApFloor_Type())
mwApFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApFloor.setStatus(_A)
_MwApNodeId_Type=Unsigned32
_MwApNodeId_Object=MibTableColumn
mwApNodeId=_MwApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,4),_MwApNodeId_Type())
mwApNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApNodeId.setStatus(_A)
class _MwApContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwApContact_Type.__name__=_E
_MwApContact_Object=MibTableColumn
mwApContact=_MwApContact_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,6),_MwApContact_Type())
mwApContact.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApContact.setStatus(_A)
_MwApLedMode_Type=MwlLedMode
_MwApLedMode_Object=MibTableColumn
mwApLedMode=_MwApLedMode_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,7),_MwApLedMode_Type())
mwApLedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApLedMode.setStatus(_A)
class _MwApLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwApLocation_Type.__name__=_E
_MwApLocation_Object=MibTableColumn
mwApLocation=_MwApLocation_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,8),_MwApLocation_Type())
mwApLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApLocation.setStatus(_A)
class _MwApBuilding_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwApBuilding_Type.__name__=_E
_MwApBuilding_Object=MibTableColumn
mwApBuilding=_MwApBuilding_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,9),_MwApBuilding_Type())
mwApBuilding.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApBuilding.setStatus(_A)
_MwApParentId_Type=Unsigned32
_MwApParentId_Object=MibTableColumn
mwApParentId=_MwApParentId_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,10),_MwApParentId_Type())
mwApParentId.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApParentId.setStatus(_A)
class _MwApInitScript_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwApInitScript_Type.__name__=_E
_MwApInitScript_Object=MibTableColumn
mwApInitScript=_MwApInitScript_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,11),_MwApInitScript_Type())
mwApInitScript.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApInitScript.setStatus(_A)
_MwApEncryption_Type=MwlOnOffSwitch
_MwApEncryption_Object=MibTableColumn
mwApEncryption=_MwApEncryption_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,12),_MwApEncryption_Type())
mwApEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApEncryption.setStatus(_A)
_MwApSerialNumber_Type=MacAddress
_MwApSerialNumber_Object=MibTableColumn
mwApSerialNumber=_MwApSerialNumber_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,13),_MwApSerialNumber_Type())
mwApSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApSerialNumber.setStatus(_A)
_MwApIndoorOutdoor_Type=MwlApIndoorOutdoorType
_MwApIndoorOutdoor_Object=MibTableColumn
mwApIndoorOutdoor=_MwApIndoorOutdoor_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,14),_MwApIndoorOutdoor_Type())
mwApIndoorOutdoor.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApIndoorOutdoor.setStatus(_A)
_MwApLinkProbingDuration_Type=Unsigned32
_MwApLinkProbingDuration_Object=MibTableColumn
mwApLinkProbingDuration=_MwApLinkProbingDuration_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,16),_MwApLinkProbingDuration_Type())
mwApLinkProbingDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApLinkProbingDuration.setStatus(_A)
_MwApUpTime_Type=TimeTicks
_MwApUpTime_Object=MibTableColumn
mwApUpTime=_MwApUpTime_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,17),_MwApUpTime_Type())
mwApUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApUpTime.setStatus(_A)
_MwApHwRev_Type=DisplayString
_MwApHwRev_Object=MibTableColumn
mwApHwRev=_MwApHwRev_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,18),_MwApHwRev_Type())
mwApHwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApHwRev.setStatus(_A)
_MwApHwType_Type=MwlApHwType
_MwApHwType_Object=MibTableColumn
mwApHwType=_MwApHwType_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,19),_MwApHwType_Type())
mwApHwType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApHwType.setStatus(_A)
_MwApParentMac_Type=MacAddress
_MwApParentMac_Object=MibTableColumn
mwApParentMac=_MwApParentMac_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,20),_MwApParentMac_Type())
mwApParentMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApParentMac.setStatus(_A)
_MwApAlarmState_Type=MwlAlarmState
_MwApAlarmState_Object=MibTableColumn
mwApAlarmState=_MwApAlarmState_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,21),_MwApAlarmState_Type())
mwApAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAlarmState.setStatus(_A)
_MwApBootVersion_Type=DisplayString
_MwApBootVersion_Object=MibTableColumn
mwApBootVersion=_MwApBootVersion_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,22),_MwApBootVersion_Type())
mwApBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApBootVersion.setStatus(_A)
_MwApFPGAVersion_Type=DisplayString
_MwApFPGAVersion_Object=MibTableColumn
mwApFPGAVersion=_MwApFPGAVersion_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,23),_MwApFPGAVersion_Type())
mwApFPGAVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApFPGAVersion.setStatus(_A)
_MwApRuntimeVersion_Type=DisplayString
_MwApRuntimeVersion_Object=MibTableColumn
mwApRuntimeVersion=_MwApRuntimeVersion_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,24),_MwApRuntimeVersion_Type())
mwApRuntimeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApRuntimeVersion.setStatus(_A)
_MwApOperationalState_Type=MwlOperationalState
_MwApOperationalState_Object=MibTableColumn
mwApOperationalState=_MwApOperationalState_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,26),_MwApOperationalState_Type())
mwApOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApOperationalState.setStatus(_A)
_MwApAvailabilityStatus_Type=MwlAvailabilityStatus
_MwApAvailabilityStatus_Object=MibTableColumn
mwApAvailabilityStatus=_MwApAvailabilityStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,27),_MwApAvailabilityStatus_Type())
mwApAvailabilityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAvailabilityStatus.setStatus(_A)
_MwApRuntimeDiscoveryOrder_Type=MwlApDiscoveryState
_MwApRuntimeDiscoveryOrder_Object=MibTableColumn
mwApRuntimeDiscoveryOrder=_MwApRuntimeDiscoveryOrder_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,28),_MwApRuntimeDiscoveryOrder_Type())
mwApRuntimeDiscoveryOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApRuntimeDiscoveryOrder.setStatus(_A)
_MwApPowerSupplyType_Type=MwlPowerSupply
_MwApPowerSupplyType_Object=MibTableColumn
mwApPowerSupplyType=_MwApPowerSupplyType_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,29),_MwApPowerSupplyType_Type())
mwApPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApPowerSupplyType.setStatus(_A)
class _MwApKeepAliveTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_MwApKeepAliveTimeout_Type.__name__=_H
_MwApKeepAliveTimeout_Object=MibTableColumn
mwApKeepAliveTimeout=_MwApKeepAliveTimeout_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,30),_MwApKeepAliveTimeout_Type())
mwApKeepAliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApKeepAliveTimeout.setStatus(_A)
_MwApVlanName_Type=DisplayString
_MwApVlanName_Object=MibTableColumn
mwApVlanName=_MwApVlanName_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,38),_MwApVlanName_Type())
mwApVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVlanName.setStatus(_A)
_MwApIpAddress_Type=IpAddress
_MwApIpAddress_Object=MibTableColumn
mwApIpAddress=_MwApIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,39),_MwApIpAddress_Type())
mwApIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApIpAddress.setStatus(_A)
_MwApRowStatus_Type=RowStatus
_MwApRowStatus_Object=MibTableColumn
mwApRowStatus=_MwApRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,1,1,56),_MwApRowStatus_Type())
mwApRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApRowStatus.setStatus(_A)
_MwAp2controllerMapTable_Object=MibTable
mwAp2controllerMapTable=_MwAp2controllerMapTable_Object((1,3,6,1,4,1,15983,1,1,4,2,2))
if mibBuilder.loadTexts:mwAp2controllerMapTable.setStatus(_A)
_MwAp2controllerMapEntry_Object=MibTableRow
mwAp2controllerMapEntry=_MwAp2controllerMapEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,2,1))
mwAp2controllerMapEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:mwAp2controllerMapEntry.setStatus(_A)
_MwAp2controllerMapTableIndex_Type=Integer32
_MwAp2controllerMapTableIndex_Object=MibTableColumn
mwAp2controllerMapTableIndex=_MwAp2controllerMapTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,2,1,1),_MwAp2controllerMapTableIndex_Type())
mwAp2controllerMapTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwAp2controllerMapTableIndex.setStatus(_A)
_MwAp2controllerMapApMac_Type=MacAddress
_MwAp2controllerMapApMac_Object=MibTableColumn
mwAp2controllerMapApMac=_MwAp2controllerMapApMac_Object((1,3,6,1,4,1,15983,1,1,4,2,2,1,2),_MwAp2controllerMapApMac_Type())
mwAp2controllerMapApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:mwAp2controllerMapApMac.setStatus(_A)
_MwAp2controllerMapDestinationController_Type=DisplayString
_MwAp2controllerMapDestinationController_Object=MibTableColumn
mwAp2controllerMapDestinationController=_MwAp2controllerMapDestinationController_Object((1,3,6,1,4,1,15983,1,1,4,2,2,1,3),_MwAp2controllerMapDestinationController_Type())
mwAp2controllerMapDestinationController.setMaxAccess(_C)
if mibBuilder.loadTexts:mwAp2controllerMapDestinationController.setStatus(_A)
_MwAp2controllerMapRowStatus_Type=RowStatus
_MwAp2controllerMapRowStatus_Object=MibTableColumn
mwAp2controllerMapRowStatus=_MwAp2controllerMapRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,2,1,4),_MwAp2controllerMapRowStatus_Type())
mwAp2controllerMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwAp2controllerMapRowStatus.setStatus(_A)
_MwApip2controllerMapTable_Object=MibTable
mwApip2controllerMapTable=_MwApip2controllerMapTable_Object((1,3,6,1,4,1,15983,1,1,4,2,3))
if mibBuilder.loadTexts:mwApip2controllerMapTable.setStatus(_A)
_MwApip2controllerMapEntry_Object=MibTableRow
mwApip2controllerMapEntry=_MwApip2controllerMapEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,3,1))
mwApip2controllerMapEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:mwApip2controllerMapEntry.setStatus(_A)
_MwApip2controllerMapTableIndex_Type=Integer32
_MwApip2controllerMapTableIndex_Object=MibTableColumn
mwApip2controllerMapTableIndex=_MwApip2controllerMapTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,3,1,1),_MwApip2controllerMapTableIndex_Type())
mwApip2controllerMapTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwApip2controllerMapTableIndex.setStatus(_A)
_MwApip2controllerMapApSubnetIp_Type=IpAddress
_MwApip2controllerMapApSubnetIp_Object=MibTableColumn
mwApip2controllerMapApSubnetIp=_MwApip2controllerMapApSubnetIp_Object((1,3,6,1,4,1,15983,1,1,4,2,3,1,2),_MwApip2controllerMapApSubnetIp_Type())
mwApip2controllerMapApSubnetIp.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApip2controllerMapApSubnetIp.setStatus(_A)
_MwApip2controllerMapApSubnetMask_Type=IpAddress
_MwApip2controllerMapApSubnetMask_Object=MibTableColumn
mwApip2controllerMapApSubnetMask=_MwApip2controllerMapApSubnetMask_Object((1,3,6,1,4,1,15983,1,1,4,2,3,1,3),_MwApip2controllerMapApSubnetMask_Type())
mwApip2controllerMapApSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApip2controllerMapApSubnetMask.setStatus(_A)
_MwApip2controllerMapDestinationController_Type=DisplayString
_MwApip2controllerMapDestinationController_Object=MibTableColumn
mwApip2controllerMapDestinationController=_MwApip2controllerMapDestinationController_Object((1,3,6,1,4,1,15983,1,1,4,2,3,1,4),_MwApip2controllerMapDestinationController_Type())
mwApip2controllerMapDestinationController.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApip2controllerMapDestinationController.setStatus(_A)
_MwApip2controllerMapRowStatus_Type=RowStatus
_MwApip2controllerMapRowStatus_Object=MibTableColumn
mwApip2controllerMapRowStatus=_MwApip2controllerMapRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,3,1,5),_MwApip2controllerMapRowStatus_Type())
mwApip2controllerMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApip2controllerMapRowStatus.setStatus(_A)
_MwApSwapTable_Object=MibTable
mwApSwapTable=_MwApSwapTable_Object((1,3,6,1,4,1,15983,1,1,4,2,4))
if mibBuilder.loadTexts:mwApSwapTable.setStatus(_A)
_MwApSwapEntry_Object=MibTableRow
mwApSwapEntry=_MwApSwapEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,4,1))
mwApSwapEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:mwApSwapEntry.setStatus(_A)
_MwApSwapTableIndex_Type=Integer32
_MwApSwapTableIndex_Object=MibTableColumn
mwApSwapTableIndex=_MwApSwapTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,4,1,1),_MwApSwapTableIndex_Type())
mwApSwapTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwApSwapTableIndex.setStatus(_A)
_MwApSwapNewApMac_Type=MacAddress
_MwApSwapNewApMac_Object=MibTableColumn
mwApSwapNewApMac=_MwApSwapNewApMac_Object((1,3,6,1,4,1,15983,1,1,4,2,4,1,2),_MwApSwapNewApMac_Type())
mwApSwapNewApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApSwapNewApMac.setStatus(_A)
_MwApSwapCurrentApMac_Type=MacAddress
_MwApSwapCurrentApMac_Object=MibTableColumn
mwApSwapCurrentApMac=_MwApSwapCurrentApMac_Object((1,3,6,1,4,1,15983,1,1,4,2,4,1,3),_MwApSwapCurrentApMac_Type())
mwApSwapCurrentApMac.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApSwapCurrentApMac.setStatus(_A)
_MwApSwapRowStatus_Type=RowStatus
_MwApSwapRowStatus_Object=MibTableColumn
mwApSwapRowStatus=_MwApSwapRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,4,1,4),_MwApSwapRowStatus_Type())
mwApSwapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApSwapRowStatus.setStatus(_A)
_MwApConnectivityTable_Object=MibTable
mwApConnectivityTable=_MwApConnectivityTable_Object((1,3,6,1,4,1,15983,1,1,4,2,5))
if mibBuilder.loadTexts:mwApConnectivityTable.setStatus(_A)
_MwApConnectivityEntry_Object=MibTableRow
mwApConnectivityEntry=_MwApConnectivityEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1))
mwApConnectivityEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:mwApConnectivityEntry.setStatus(_A)
_MwApConnectivityTableIndex_Type=Integer32
_MwApConnectivityTableIndex_Object=MibTableColumn
mwApConnectivityTableIndex=_MwApConnectivityTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,1),_MwApConnectivityTableIndex_Type())
mwApConnectivityTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwApConnectivityTableIndex.setStatus(_A)
_MwApConnectivityWncIp_Type=IpAddress
_MwApConnectivityWncIp_Object=MibTableColumn
mwApConnectivityWncIp=_MwApConnectivityWncIp_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,2),_MwApConnectivityWncIp_Type())
mwApConnectivityWncIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityWncIp.setStatus(_A)
class _MwApConnectivityHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MwApConnectivityHostName_Type.__name__=_E
_MwApConnectivityHostName_Object=MibTableColumn
mwApConnectivityHostName=_MwApConnectivityHostName_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,3),_MwApConnectivityHostName_Type())
mwApConnectivityHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityHostName.setStatus(_A)
_MwApConnectivityPrimaryDns_Type=IpAddress
_MwApConnectivityPrimaryDns_Object=MibTableColumn
mwApConnectivityPrimaryDns=_MwApConnectivityPrimaryDns_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,4),_MwApConnectivityPrimaryDns_Type())
mwApConnectivityPrimaryDns.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityPrimaryDns.setStatus(_A)
class _MwApConnectivityWncHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MwApConnectivityWncHostName_Type.__name__=_E
_MwApConnectivityWncHostName_Object=MibTableColumn
mwApConnectivityWncHostName=_MwApConnectivityWncHostName_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,5),_MwApConnectivityWncHostName_Type())
mwApConnectivityWncHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityWncHostName.setStatus(_A)
_MwApConnectivityAssignedType_Type=MwlApIpAssignmentType
_MwApConnectivityAssignedType_Object=MibTableColumn
mwApConnectivityAssignedType=_MwApConnectivityAssignedType_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,6),_MwApConnectivityAssignedType_Type())
mwApConnectivityAssignedType.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityAssignedType.setStatus(_A)
_MwApConnectivitySecondaryDns_Type=IpAddress
_MwApConnectivitySecondaryDns_Object=MibTableColumn
mwApConnectivitySecondaryDns=_MwApConnectivitySecondaryDns_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,7),_MwApConnectivitySecondaryDns_Type())
mwApConnectivitySecondaryDns.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivitySecondaryDns.setStatus(_A)
_MwApConnectivityWncDomainName_Type=DisplayString
_MwApConnectivityWncDomainName_Object=MibTableColumn
mwApConnectivityWncDomainName=_MwApConnectivityWncDomainName_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,8),_MwApConnectivityWncDomainName_Type())
mwApConnectivityWncDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityWncDomainName.setStatus(_A)
_MwApConnectivityConfigureIpAddr_Type=IpAddress
_MwApConnectivityConfigureIpAddr_Object=MibTableColumn
mwApConnectivityConfigureIpAddr=_MwApConnectivityConfigureIpAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,9),_MwApConnectivityConfigureIpAddr_Type())
mwApConnectivityConfigureIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityConfigureIpAddr.setStatus(_A)
_MwApConnectivityConfigureNetMask_Type=IpAddress
_MwApConnectivityConfigureNetMask_Object=MibTableColumn
mwApConnectivityConfigureNetMask=_MwApConnectivityConfigureNetMask_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,10),_MwApConnectivityConfigureNetMask_Type())
mwApConnectivityConfigureNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityConfigureNetMask.setStatus(_A)
_MwApConnectivityConfigureGatewayAddr_Type=IpAddress
_MwApConnectivityConfigureGatewayAddr_Object=MibTableColumn
mwApConnectivityConfigureGatewayAddr=_MwApConnectivityConfigureGatewayAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,11),_MwApConnectivityConfigureGatewayAddr_Type())
mwApConnectivityConfigureGatewayAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityConfigureGatewayAddr.setStatus(_A)
_MwApConnectivityConfiguredDiscoveryOrder_Type=MwlDiscoveryOrder
_MwApConnectivityConfiguredDiscoveryOrder_Object=MibTableColumn
mwApConnectivityConfiguredDiscoveryOrder=_MwApConnectivityConfiguredDiscoveryOrder_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,12),_MwApConnectivityConfiguredDiscoveryOrder_Type())
mwApConnectivityConfiguredDiscoveryOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApConnectivityConfiguredDiscoveryOrder.setStatus(_A)
_MwApConnectivityNodeId_Type=Integer32
_MwApConnectivityNodeId_Object=MibTableColumn
mwApConnectivityNodeId=_MwApConnectivityNodeId_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,13),_MwApConnectivityNodeId_Type())
mwApConnectivityNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityNodeId.setStatus(_A)
_MwApConnectivityNodeName_Type=DisplayString
_MwApConnectivityNodeName_Object=MibTableColumn
mwApConnectivityNodeName=_MwApConnectivityNodeName_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,14),_MwApConnectivityNodeName_Type())
mwApConnectivityNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityNodeName.setStatus(_A)
_MwApConnectivityDomainName_Type=DisplayString
_MwApConnectivityDomainName_Object=MibTableColumn
mwApConnectivityDomainName=_MwApConnectivityDomainName_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,15),_MwApConnectivityDomainName_Type())
mwApConnectivityDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityDomainName.setStatus(_A)
_MwApConnectivityRuntimeDns1_Type=IpAddress
_MwApConnectivityRuntimeDns1_Object=MibTableColumn
mwApConnectivityRuntimeDns1=_MwApConnectivityRuntimeDns1_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,16),_MwApConnectivityRuntimeDns1_Type())
mwApConnectivityRuntimeDns1.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns1.setStatus(_A)
_MwApConnectivityRuntimeDns2_Type=IpAddress
_MwApConnectivityRuntimeDns2_Object=MibTableColumn
mwApConnectivityRuntimeDns2=_MwApConnectivityRuntimeDns2_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,17),_MwApConnectivityRuntimeDns2_Type())
mwApConnectivityRuntimeDns2.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns2.setStatus(_A)
_MwApConnectivityRuntimeDns3_Type=IpAddress
_MwApConnectivityRuntimeDns3_Object=MibTableColumn
mwApConnectivityRuntimeDns3=_MwApConnectivityRuntimeDns3_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,18),_MwApConnectivityRuntimeDns3_Type())
mwApConnectivityRuntimeDns3.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns3.setStatus(_A)
_MwApConnectivityRuntimeDns4_Type=IpAddress
_MwApConnectivityRuntimeDns4_Object=MibTableColumn
mwApConnectivityRuntimeDns4=_MwApConnectivityRuntimeDns4_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,19),_MwApConnectivityRuntimeDns4_Type())
mwApConnectivityRuntimeDns4.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns4.setStatus(_A)
_MwApConnectivityRuntimeDns5_Type=IpAddress
_MwApConnectivityRuntimeDns5_Object=MibTableColumn
mwApConnectivityRuntimeDns5=_MwApConnectivityRuntimeDns5_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,20),_MwApConnectivityRuntimeDns5_Type())
mwApConnectivityRuntimeDns5.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns5.setStatus(_A)
_MwApConnectivityRuntimeDns6_Type=IpAddress
_MwApConnectivityRuntimeDns6_Object=MibTableColumn
mwApConnectivityRuntimeDns6=_MwApConnectivityRuntimeDns6_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,21),_MwApConnectivityRuntimeDns6_Type())
mwApConnectivityRuntimeDns6.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns6.setStatus(_A)
_MwApConnectivityRuntimeDns7_Type=IpAddress
_MwApConnectivityRuntimeDns7_Object=MibTableColumn
mwApConnectivityRuntimeDns7=_MwApConnectivityRuntimeDns7_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,22),_MwApConnectivityRuntimeDns7_Type())
mwApConnectivityRuntimeDns7.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns7.setStatus(_A)
_MwApConnectivityRuntimeDns8_Type=IpAddress
_MwApConnectivityRuntimeDns8_Object=MibTableColumn
mwApConnectivityRuntimeDns8=_MwApConnectivityRuntimeDns8_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,23),_MwApConnectivityRuntimeDns8_Type())
mwApConnectivityRuntimeDns8.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDns8.setStatus(_A)
_MwApConnectivityRuntimeIpAddr_Type=IpAddress
_MwApConnectivityRuntimeIpAddr_Object=MibTableColumn
mwApConnectivityRuntimeIpAddr=_MwApConnectivityRuntimeIpAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,24),_MwApConnectivityRuntimeIpAddr_Type())
mwApConnectivityRuntimeIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeIpAddr.setStatus(_A)
_MwApConnectivityRuntimeNetMask_Type=IpAddress
_MwApConnectivityRuntimeNetMask_Object=MibTableColumn
mwApConnectivityRuntimeNetMask=_MwApConnectivityRuntimeNetMask_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,25),_MwApConnectivityRuntimeNetMask_Type())
mwApConnectivityRuntimeNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeNetMask.setStatus(_A)
_MwApConnectivityRuntimeGatewayAddr_Type=IpAddress
_MwApConnectivityRuntimeGatewayAddr_Object=MibTableColumn
mwApConnectivityRuntimeGatewayAddr=_MwApConnectivityRuntimeGatewayAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,26),_MwApConnectivityRuntimeGatewayAddr_Type())
mwApConnectivityRuntimeGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeGatewayAddr.setStatus(_A)
_MwApConnectivityRuntimeDiscoveryState_Type=MwlApDiscoveryState
_MwApConnectivityRuntimeDiscoveryState_Object=MibTableColumn
mwApConnectivityRuntimeDiscoveryState=_MwApConnectivityRuntimeDiscoveryState_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,27),_MwApConnectivityRuntimeDiscoveryState_Type())
mwApConnectivityRuntimeDiscoveryState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeDiscoveryState.setStatus(_A)
_MwApConnectivityVPNState_Type=MwlEnableDisableOption
_MwApConnectivityVPNState_Object=MibTableColumn
mwApConnectivityVPNState=_MwApConnectivityVPNState_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,28),_MwApConnectivityVPNState_Type())
mwApConnectivityVPNState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityVPNState.setStatus(_A)
_MwApConnectivityVPNAuthMethod_Type=MwlVpnAuthenticationType
_MwApConnectivityVPNAuthMethod_Object=MibTableColumn
mwApConnectivityVPNAuthMethod=_MwApConnectivityVPNAuthMethod_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,29),_MwApConnectivityVPNAuthMethod_Type())
mwApConnectivityVPNAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityVPNAuthMethod.setStatus(_A)
_MwApConnectivityWncTunnelIp_Type=IpAddress
_MwApConnectivityWncTunnelIp_Object=MibTableColumn
mwApConnectivityWncTunnelIp=_MwApConnectivityWncTunnelIp_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,30),_MwApConnectivityWncTunnelIp_Type())
mwApConnectivityWncTunnelIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityWncTunnelIp.setStatus(_A)
_MwApConnectivityRuntimeTunnelIpAddr_Type=IpAddress
_MwApConnectivityRuntimeTunnelIpAddr_Object=MibTableColumn
mwApConnectivityRuntimeTunnelIpAddr=_MwApConnectivityRuntimeTunnelIpAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,31),_MwApConnectivityRuntimeTunnelIpAddr_Type())
mwApConnectivityRuntimeTunnelIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityRuntimeTunnelIpAddr.setStatus(_A)
_MwApConnectivityVpnServerIp_Type=IpAddress
_MwApConnectivityVpnServerIp_Object=MibTableColumn
mwApConnectivityVpnServerIp=_MwApConnectivityVpnServerIp_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,32),_MwApConnectivityVpnServerIp_Type())
mwApConnectivityVpnServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityVpnServerIp.setStatus(_A)
class _MwApConnectivityVpnServerHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MwApConnectivityVpnServerHostName_Type.__name__=_E
_MwApConnectivityVpnServerHostName_Object=MibTableColumn
mwApConnectivityVpnServerHostName=_MwApConnectivityVpnServerHostName_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,33),_MwApConnectivityVpnServerHostName_Type())
mwApConnectivityVpnServerHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityVpnServerHostName.setStatus(_A)
_MwApConnectivityVpnServerPort_Type=Unsigned32
_MwApConnectivityVpnServerPort_Object=MibTableColumn
mwApConnectivityVpnServerPort=_MwApConnectivityVpnServerPort_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,34),_MwApConnectivityVpnServerPort_Type())
mwApConnectivityVpnServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityVpnServerPort.setStatus(_A)
_MwApConnectivityVPNStatus_Type=MwlVpnMode
_MwApConnectivityVPNStatus_Object=MibTableColumn
mwApConnectivityVPNStatus=_MwApConnectivityVPNStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,5,1,35),_MwApConnectivityVPNStatus_Type())
mwApConnectivityVPNStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApConnectivityVPNStatus.setStatus(_A)
_MwApCertificateTable_Object=MibTable
mwApCertificateTable=_MwApCertificateTable_Object((1,3,6,1,4,1,15983,1,1,4,2,6))
if mibBuilder.loadTexts:mwApCertificateTable.setStatus(_A)
_MwApCertificateEntry_Object=MibTableRow
mwApCertificateEntry=_MwApCertificateEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1))
mwApCertificateEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:mwApCertificateEntry.setStatus(_A)
_MwApCertificateTableIndex_Type=Integer32
_MwApCertificateTableIndex_Object=MibTableColumn
mwApCertificateTableIndex=_MwApCertificateTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,1),_MwApCertificateTableIndex_Type())
mwApCertificateTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwApCertificateTableIndex.setStatus(_A)
_MwApCertificateNodeId_Type=Integer32
_MwApCertificateNodeId_Object=MibTableColumn
mwApCertificateNodeId=_MwApCertificateNodeId_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,2),_MwApCertificateNodeId_Type())
mwApCertificateNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateNodeId.setStatus(_A)
_MwApCertificateNodeName_Type=DisplayString
_MwApCertificateNodeName_Object=MibTableColumn
mwApCertificateNodeName=_MwApCertificateNodeName_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,3),_MwApCertificateNodeName_Type())
mwApCertificateNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateNodeName.setStatus(_A)
_MwApCertificateSerialNumber_Type=MacAddress
_MwApCertificateSerialNumber_Object=MibTableColumn
mwApCertificateSerialNumber=_MwApCertificateSerialNumber_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,4),_MwApCertificateSerialNumber_Type())
mwApCertificateSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateSerialNumber.setStatus(_A)
_MwApCertificateOperationalState_Type=MwlOperationalState
_MwApCertificateOperationalState_Object=MibTableColumn
mwApCertificateOperationalState=_MwApCertificateOperationalState_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,5),_MwApCertificateOperationalState_Type())
mwApCertificateOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateOperationalState.setStatus(_A)
_MwApCertificateAvailabilityStatus_Type=MwlAvailabilityStatus
_MwApCertificateAvailabilityStatus_Object=MibTableColumn
mwApCertificateAvailabilityStatus=_MwApCertificateAvailabilityStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,6),_MwApCertificateAvailabilityStatus_Type())
mwApCertificateAvailabilityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateAvailabilityStatus.setStatus(_A)
_MwApCertificateStatus_Type=MwlCertificateStatus
_MwApCertificateStatus_Object=MibTableColumn
mwApCertificateStatus=_MwApCertificateStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,7),_MwApCertificateStatus_Type())
mwApCertificateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateStatus.setStatus(_A)
_MwApCertificateApCertReqStatus_Type=MwlCertRequestStatus
_MwApCertificateApCertReqStatus_Object=MibTableColumn
mwApCertificateApCertReqStatus=_MwApCertificateApCertReqStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,8),_MwApCertificateApCertReqStatus_Type())
mwApCertificateApCertReqStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateApCertReqStatus.setStatus(_A)
_MwApCertificateCertificateAuthority_Type=DisplayString
_MwApCertificateCertificateAuthority_Object=MibTableColumn
mwApCertificateCertificateAuthority=_MwApCertificateCertificateAuthority_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,9),_MwApCertificateCertificateAuthority_Type())
mwApCertificateCertificateAuthority.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateCertificateAuthority.setStatus(_A)
_MwApCertificateValidity_Type=DateAndTime
_MwApCertificateValidity_Object=MibTableColumn
mwApCertificateValidity=_MwApCertificateValidity_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,10),_MwApCertificateValidity_Type())
mwApCertificateValidity.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateValidity.setStatus(_A)
_MwApCertificateApHwType_Type=MwlApHwType
_MwApCertificateApHwType_Object=MibTableColumn
mwApCertificateApHwType=_MwApCertificateApHwType_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,11),_MwApCertificateApHwType_Type())
mwApCertificateApHwType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApCertificateApHwType.setStatus(_A)
_MwApCertificateRowStatus_Type=RowStatus
_MwApCertificateRowStatus_Object=MibTableColumn
mwApCertificateRowStatus=_MwApCertificateRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,6,1,20),_MwApCertificateRowStatus_Type())
mwApCertificateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwApCertificateRowStatus.setStatus(_A)
_MwApVpnClientInfoTable_Object=MibTable
mwApVpnClientInfoTable=_MwApVpnClientInfoTable_Object((1,3,6,1,4,1,15983,1,1,4,2,7))
if mibBuilder.loadTexts:mwApVpnClientInfoTable.setStatus(_A)
_MwApVpnClientInfoEntry_Object=MibTableRow
mwApVpnClientInfoEntry=_MwApVpnClientInfoEntry_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1))
mwApVpnClientInfoEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:mwApVpnClientInfoEntry.setStatus(_A)
_MwApVpnClientInfoTableIndex_Type=Integer32
_MwApVpnClientInfoTableIndex_Object=MibTableColumn
mwApVpnClientInfoTableIndex=_MwApVpnClientInfoTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,1),_MwApVpnClientInfoTableIndex_Type())
mwApVpnClientInfoTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwApVpnClientInfoTableIndex.setStatus(_A)
_MwApVpnClientInfoNodeId_Type=Integer32
_MwApVpnClientInfoNodeId_Object=MibTableColumn
mwApVpnClientInfoNodeId=_MwApVpnClientInfoNodeId_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,2),_MwApVpnClientInfoNodeId_Type())
mwApVpnClientInfoNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoNodeId.setStatus(_A)
_MwApVpnClientInfoNodeName_Type=DisplayString
_MwApVpnClientInfoNodeName_Object=MibTableColumn
mwApVpnClientInfoNodeName=_MwApVpnClientInfoNodeName_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,3),_MwApVpnClientInfoNodeName_Type())
mwApVpnClientInfoNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoNodeName.setStatus(_A)
_MwApVpnClientInfoApMac_Type=MacAddress
_MwApVpnClientInfoApMac_Object=MibTableColumn
mwApVpnClientInfoApMac=_MwApVpnClientInfoApMac_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,4),_MwApVpnClientInfoApMac_Type())
mwApVpnClientInfoApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoApMac.setStatus(_A)
_MwApVpnClientInfoTunnelIpAddr_Type=IpAddress
_MwApVpnClientInfoTunnelIpAddr_Object=MibTableColumn
mwApVpnClientInfoTunnelIpAddr=_MwApVpnClientInfoTunnelIpAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,5),_MwApVpnClientInfoTunnelIpAddr_Type())
mwApVpnClientInfoTunnelIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoTunnelIpAddr.setStatus(_A)
_MwApVpnClientInfoRealIpAddr_Type=IpAddress
_MwApVpnClientInfoRealIpAddr_Object=MibTableColumn
mwApVpnClientInfoRealIpAddr=_MwApVpnClientInfoRealIpAddr_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,6),_MwApVpnClientInfoRealIpAddr_Type())
mwApVpnClientInfoRealIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoRealIpAddr.setStatus(_A)
_MwApVpnClientInfoVpnConnectivityStatus_Type=MwlVpnConnectivityStatus
_MwApVpnClientInfoVpnConnectivityStatus_Object=MibTableColumn
mwApVpnClientInfoVpnConnectivityStatus=_MwApVpnClientInfoVpnConnectivityStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,7),_MwApVpnClientInfoVpnConnectivityStatus_Type())
mwApVpnClientInfoVpnConnectivityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoVpnConnectivityStatus.setStatus(_A)
_MwApVpnClientInfoVpnAuthenticationStatus_Type=MwlVpnAuthenticationStatus
_MwApVpnClientInfoVpnAuthenticationStatus_Object=MibTableColumn
mwApVpnClientInfoVpnAuthenticationStatus=_MwApVpnClientInfoVpnAuthenticationStatus_Object((1,3,6,1,4,1,15983,1,1,4,2,7,1,8),_MwApVpnClientInfoVpnAuthenticationStatus_Type())
mwApVpnClientInfoVpnAuthenticationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApVpnClientInfoVpnAuthenticationStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mwConfigAp':mwConfigAp,'mwApTable':mwApTable,'mwApEntry':mwApEntry,_I:mwApTableIndex,'mwApDescr':mwApDescr,'mwApFloor':mwApFloor,'mwApNodeId':mwApNodeId,'mwApContact':mwApContact,'mwApLedMode':mwApLedMode,'mwApLocation':mwApLocation,'mwApBuilding':mwApBuilding,'mwApParentId':mwApParentId,'mwApInitScript':mwApInitScript,'mwApEncryption':mwApEncryption,'mwApSerialNumber':mwApSerialNumber,'mwApIndoorOutdoor':mwApIndoorOutdoor,'mwApLinkProbingDuration':mwApLinkProbingDuration,'mwApUpTime':mwApUpTime,'mwApHwRev':mwApHwRev,'mwApHwType':mwApHwType,'mwApParentMac':mwApParentMac,'mwApAlarmState':mwApAlarmState,'mwApBootVersion':mwApBootVersion,'mwApFPGAVersion':mwApFPGAVersion,'mwApRuntimeVersion':mwApRuntimeVersion,'mwApOperationalState':mwApOperationalState,'mwApAvailabilityStatus':mwApAvailabilityStatus,'mwApRuntimeDiscoveryOrder':mwApRuntimeDiscoveryOrder,'mwApPowerSupplyType':mwApPowerSupplyType,'mwApKeepAliveTimeout':mwApKeepAliveTimeout,'mwApVlanName':mwApVlanName,'mwApIpAddress':mwApIpAddress,'mwApRowStatus':mwApRowStatus,'mwAp2controllerMapTable':mwAp2controllerMapTable,'mwAp2controllerMapEntry':mwAp2controllerMapEntry,_J:mwAp2controllerMapTableIndex,'mwAp2controllerMapApMac':mwAp2controllerMapApMac,'mwAp2controllerMapDestinationController':mwAp2controllerMapDestinationController,'mwAp2controllerMapRowStatus':mwAp2controllerMapRowStatus,'mwApip2controllerMapTable':mwApip2controllerMapTable,'mwApip2controllerMapEntry':mwApip2controllerMapEntry,_K:mwApip2controllerMapTableIndex,'mwApip2controllerMapApSubnetIp':mwApip2controllerMapApSubnetIp,'mwApip2controllerMapApSubnetMask':mwApip2controllerMapApSubnetMask,'mwApip2controllerMapDestinationController':mwApip2controllerMapDestinationController,'mwApip2controllerMapRowStatus':mwApip2controllerMapRowStatus,'mwApSwapTable':mwApSwapTable,'mwApSwapEntry':mwApSwapEntry,_L:mwApSwapTableIndex,'mwApSwapNewApMac':mwApSwapNewApMac,'mwApSwapCurrentApMac':mwApSwapCurrentApMac,'mwApSwapRowStatus':mwApSwapRowStatus,'mwApConnectivityTable':mwApConnectivityTable,'mwApConnectivityEntry':mwApConnectivityEntry,_M:mwApConnectivityTableIndex,'mwApConnectivityWncIp':mwApConnectivityWncIp,'mwApConnectivityHostName':mwApConnectivityHostName,'mwApConnectivityPrimaryDns':mwApConnectivityPrimaryDns,'mwApConnectivityWncHostName':mwApConnectivityWncHostName,'mwApConnectivityAssignedType':mwApConnectivityAssignedType,'mwApConnectivitySecondaryDns':mwApConnectivitySecondaryDns,'mwApConnectivityWncDomainName':mwApConnectivityWncDomainName,'mwApConnectivityConfigureIpAddr':mwApConnectivityConfigureIpAddr,'mwApConnectivityConfigureNetMask':mwApConnectivityConfigureNetMask,'mwApConnectivityConfigureGatewayAddr':mwApConnectivityConfigureGatewayAddr,'mwApConnectivityConfiguredDiscoveryOrder':mwApConnectivityConfiguredDiscoveryOrder,'mwApConnectivityNodeId':mwApConnectivityNodeId,'mwApConnectivityNodeName':mwApConnectivityNodeName,'mwApConnectivityDomainName':mwApConnectivityDomainName,'mwApConnectivityRuntimeDns1':mwApConnectivityRuntimeDns1,'mwApConnectivityRuntimeDns2':mwApConnectivityRuntimeDns2,'mwApConnectivityRuntimeDns3':mwApConnectivityRuntimeDns3,'mwApConnectivityRuntimeDns4':mwApConnectivityRuntimeDns4,'mwApConnectivityRuntimeDns5':mwApConnectivityRuntimeDns5,'mwApConnectivityRuntimeDns6':mwApConnectivityRuntimeDns6,'mwApConnectivityRuntimeDns7':mwApConnectivityRuntimeDns7,'mwApConnectivityRuntimeDns8':mwApConnectivityRuntimeDns8,'mwApConnectivityRuntimeIpAddr':mwApConnectivityRuntimeIpAddr,'mwApConnectivityRuntimeNetMask':mwApConnectivityRuntimeNetMask,'mwApConnectivityRuntimeGatewayAddr':mwApConnectivityRuntimeGatewayAddr,'mwApConnectivityRuntimeDiscoveryState':mwApConnectivityRuntimeDiscoveryState,'mwApConnectivityVPNState':mwApConnectivityVPNState,'mwApConnectivityVPNAuthMethod':mwApConnectivityVPNAuthMethod,'mwApConnectivityWncTunnelIp':mwApConnectivityWncTunnelIp,'mwApConnectivityRuntimeTunnelIpAddr':mwApConnectivityRuntimeTunnelIpAddr,'mwApConnectivityVpnServerIp':mwApConnectivityVpnServerIp,'mwApConnectivityVpnServerHostName':mwApConnectivityVpnServerHostName,'mwApConnectivityVpnServerPort':mwApConnectivityVpnServerPort,'mwApConnectivityVPNStatus':mwApConnectivityVPNStatus,'mwApCertificateTable':mwApCertificateTable,'mwApCertificateEntry':mwApCertificateEntry,_N:mwApCertificateTableIndex,'mwApCertificateNodeId':mwApCertificateNodeId,'mwApCertificateNodeName':mwApCertificateNodeName,'mwApCertificateSerialNumber':mwApCertificateSerialNumber,'mwApCertificateOperationalState':mwApCertificateOperationalState,'mwApCertificateAvailabilityStatus':mwApCertificateAvailabilityStatus,'mwApCertificateStatus':mwApCertificateStatus,'mwApCertificateApCertReqStatus':mwApCertificateApCertReqStatus,'mwApCertificateCertificateAuthority':mwApCertificateCertificateAuthority,'mwApCertificateValidity':mwApCertificateValidity,'mwApCertificateApHwType':mwApCertificateApHwType,'mwApCertificateRowStatus':mwApCertificateRowStatus,'mwApVpnClientInfoTable':mwApVpnClientInfoTable,'mwApVpnClientInfoEntry':mwApVpnClientInfoEntry,_O:mwApVpnClientInfoTableIndex,'mwApVpnClientInfoNodeId':mwApVpnClientInfoNodeId,'mwApVpnClientInfoNodeName':mwApVpnClientInfoNodeName,'mwApVpnClientInfoApMac':mwApVpnClientInfoApMac,'mwApVpnClientInfoTunnelIpAddr':mwApVpnClientInfoTunnelIpAddr,'mwApVpnClientInfoRealIpAddr':mwApVpnClientInfoRealIpAddr,'mwApVpnClientInfoVpnConnectivityStatus':mwApVpnClientInfoVpnConnectivityStatus,'mwApVpnClientInfoVpnAuthenticationStatus':mwApVpnClientInfoVpnAuthenticationStatus})