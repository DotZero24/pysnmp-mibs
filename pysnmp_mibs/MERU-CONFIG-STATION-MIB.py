_H='mwStationIpaddressTableIndex'
_G='not-accessible'
_F='mwStationTableIndex'
_E='MERU-CONFIG-STATION-MIB'
_D='DisplayString'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlAddressAssignmentType,MwlApIfModeType,MwlDeviceType,MwlIpMode,MwlIpv6AddrType,MwlL2SecurityMode,MwlVpnStatus=mibBuilder.importSymbols('MERU-TC','MwlAddressAssignmentType','MwlApIfModeType','MwlDeviceType','MwlIpMode','MwlIpv6AddrType','MwlL2SecurityMode','MwlVpnStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigStation=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,4))
_MwStationTable_Object=MibTable
mwStationTable=_MwStationTable_Object((1,3,6,1,4,1,15983,1,1,4,4,1))
if mibBuilder.loadTexts:mwStationTable.setStatus(_A)
_MwStationEntry_Object=MibTableRow
mwStationEntry=_MwStationEntry_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1))
mwStationEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mwStationEntry.setStatus(_A)
_MwStationTableIndex_Type=Integer32
_MwStationTableIndex_Object=MibTableColumn
mwStationTableIndex=_MwStationTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,1),_MwStationTableIndex_Type())
mwStationTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwStationTableIndex.setStatus(_A)
_MwStationMacAddress_Type=MacAddress
_MwStationMacAddress_Object=MibTableColumn
mwStationMacAddress=_MwStationMacAddress_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,2),_MwStationMacAddress_Type())
mwStationMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationMacAddress.setStatus(_A)
_MwStationIpv6Address_Type=Ipv6Address
_MwStationIpv6Address_Object=MibTableColumn
mwStationIpv6Address=_MwStationIpv6Address_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,3),_MwStationIpv6Address_Type())
mwStationIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationIpv6Address.setStatus(_A)
_MwStationAp_Type=Integer32
_MwStationAp_Object=MibTableColumn
mwStationAp=_MwStationAp_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,4),_MwStationAp_Type())
mwStationAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationAp.setStatus(_A)
_MwStationApName_Type=DisplayString
_MwStationApName_Object=MibTableColumn
mwStationApName=_MwStationApName_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,5),_MwStationApName_Type())
mwStationApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationApName.setStatus(_A)
_MwStationL3State_Type=MwlVpnStatus
_MwStationL3State_Object=MibTableColumn
mwStationL3State=_MwStationL3State_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,6),_MwStationL3State_Type())
mwStationL3State.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationL3State.setStatus(_A)
_MwStationVlanTag_Type=Unsigned32
_MwStationVlanTag_Object=MibTableColumn
mwStationVlanTag=_MwStationVlanTag_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,7),_MwStationVlanTag_Type())
mwStationVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationVlanTag.setStatus(_A)
_MwStationAuthUser_Type=DisplayString
_MwStationAuthUser_Object=MibTableColumn
mwStationAuthUser=_MwStationAuthUser_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,8),_MwStationAuthUser_Type())
mwStationAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationAuthUser.setStatus(_A)
class _MwStationVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwStationVlanName_Type.__name__=_D
_MwStationVlanName_Object=MibTableColumn
mwStationVlanName=_MwStationVlanName_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,9),_MwStationVlanName_Type())
mwStationVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationVlanName.setStatus(_A)
_MwStationRadioType_Type=MwlApIfModeType
_MwStationRadioType_Object=MibTableColumn
mwStationRadioType=_MwStationRadioType_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,10),_MwStationRadioType_Type())
mwStationRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationRadioType.setStatus(_A)
_MwStationL2ModeState_Type=MwlL2SecurityMode
_MwStationL2ModeState_Object=MibTableColumn
mwStationL2ModeState=_MwStationL2ModeState_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,11),_MwStationL2ModeState_Type())
mwStationL2ModeState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationL2ModeState.setStatus(_A)
_MwStationCurrentRssi_Type=Integer32
_MwStationCurrentRssi_Object=MibTableColumn
mwStationCurrentRssi=_MwStationCurrentRssi_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,12),_MwStationCurrentRssi_Type())
mwStationCurrentRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationCurrentRssi.setStatus(_A)
_MwStationTxThroughput_Type=Unsigned32
_MwStationTxThroughput_Object=MibTableColumn
mwStationTxThroughput=_MwStationTxThroughput_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,13),_MwStationTxThroughput_Type())
mwStationTxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationTxThroughput.setStatus(_A)
_MwStationRxThroughput_Type=Unsigned32
_MwStationRxThroughput_Object=MibTableColumn
mwStationRxThroughput=_MwStationRxThroughput_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,14),_MwStationRxThroughput_Type())
mwStationRxThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationRxThroughput.setStatus(_A)
_MwStationLossPercentage_Type=Integer32
_MwStationLossPercentage_Object=MibTableColumn
mwStationLossPercentage=_MwStationLossPercentage_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,15),_MwStationLossPercentage_Type())
mwStationLossPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationLossPercentage.setStatus(_A)
_MwStationAddrAssignmentType_Type=MwlAddressAssignmentType
_MwStationAddrAssignmentType_Object=MibTableColumn
mwStationAddrAssignmentType=_MwStationAddrAssignmentType_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,16),_MwStationAddrAssignmentType_Type())
mwStationAddrAssignmentType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationAddrAssignmentType.setStatus(_A)
_MwStationChannelUtilization_Type=Counter64
_MwStationChannelUtilization_Object=MibTableColumn
mwStationChannelUtilization=_MwStationChannelUtilization_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,17),_MwStationChannelUtilization_Type())
mwStationChannelUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationChannelUtilization.setStatus(_A)
_MwStationVirtualPort_Type=MacAddress
_MwStationVirtualPort_Object=MibTableColumn
mwStationVirtualPort=_MwStationVirtualPort_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,18),_MwStationVirtualPort_Type())
mwStationVirtualPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationVirtualPort.setStatus(_A)
_MwStationDeviceType_Type=MwlDeviceType
_MwStationDeviceType_Object=MibTableColumn
mwStationDeviceType=_MwStationDeviceType_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,20),_MwStationDeviceType_Type())
mwStationDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationDeviceType.setStatus(_A)
class _MwStationFilterId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MwStationFilterId_Type.__name__=_D
_MwStationFilterId_Object=MibTableColumn
mwStationFilterId=_MwStationFilterId_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,21),_MwStationFilterId_Type())
mwStationFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationFilterId.setStatus(_A)
_MwStationFpDeviceType_Type=DisplayString
_MwStationFpDeviceType_Object=MibTableColumn
mwStationFpDeviceType=_MwStationFpDeviceType_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,22),_MwStationFpDeviceType_Type())
mwStationFpDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationFpDeviceType.setStatus(_A)
_MwStationFpOsType_Type=DisplayString
_MwStationFpOsType_Object=MibTableColumn
mwStationFpOsType=_MwStationFpOsType_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,23),_MwStationFpOsType_Type())
mwStationFpOsType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationFpOsType.setStatus(_A)
_MwStationIpMode_Type=MwlIpMode
_MwStationIpMode_Object=MibTableColumn
mwStationIpMode=_MwStationIpMode_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,24),_MwStationIpMode_Type())
mwStationIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationIpMode.setStatus(_A)
class _MwStationVlanPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwStationVlanPoolName_Type.__name__=_D
_MwStationVlanPoolName_Object=MibTableColumn
mwStationVlanPoolName=_MwStationVlanPoolName_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,25),_MwStationVlanPoolName_Type())
mwStationVlanPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationVlanPoolName.setStatus(_A)
_MwStationRowStatus_Type=RowStatus
_MwStationRowStatus_Object=MibTableColumn
mwStationRowStatus=_MwStationRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,4,1,1,34),_MwStationRowStatus_Type())
mwStationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationRowStatus.setStatus(_A)
_MwStationIpaddressTable_Object=MibTable
mwStationIpaddressTable=_MwStationIpaddressTable_Object((1,3,6,1,4,1,15983,1,1,4,4,2))
if mibBuilder.loadTexts:mwStationIpaddressTable.setStatus(_A)
_MwStationIpaddressEntry_Object=MibTableRow
mwStationIpaddressEntry=_MwStationIpaddressEntry_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1))
mwStationIpaddressEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:mwStationIpaddressEntry.setStatus(_A)
_MwStationIpaddressTableIndex_Type=Integer32
_MwStationIpaddressTableIndex_Object=MibTableColumn
mwStationIpaddressTableIndex=_MwStationIpaddressTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,1),_MwStationIpaddressTableIndex_Type())
mwStationIpaddressTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwStationIpaddressTableIndex.setStatus(_A)
_MwStationIpaddressMacAddress_Type=MacAddress
_MwStationIpaddressMacAddress_Object=MibTableColumn
mwStationIpaddressMacAddress=_MwStationIpaddressMacAddress_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,2),_MwStationIpaddressMacAddress_Type())
mwStationIpaddressMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationIpaddressMacAddress.setStatus(_A)
_MwStationIpaddressIpAddress_Type=Ipv6Address
_MwStationIpaddressIpAddress_Object=MibTableColumn
mwStationIpaddressIpAddress=_MwStationIpaddressIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,3),_MwStationIpaddressIpAddress_Type())
mwStationIpaddressIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationIpaddressIpAddress.setStatus(_A)
_MwStationIpaddressAddrAssignmentType_Type=MwlAddressAssignmentType
_MwStationIpaddressAddrAssignmentType_Object=MibTableColumn
mwStationIpaddressAddrAssignmentType=_MwStationIpaddressAddrAssignmentType_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,4),_MwStationIpaddressAddrAssignmentType_Type())
mwStationIpaddressAddrAssignmentType.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationIpaddressAddrAssignmentType.setStatus(_A)
_MwStationIpaddressVirtualAddress_Type=MacAddress
_MwStationIpaddressVirtualAddress_Object=MibTableColumn
mwStationIpaddressVirtualAddress=_MwStationIpaddressVirtualAddress_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,5),_MwStationIpaddressVirtualAddress_Type())
mwStationIpaddressVirtualAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationIpaddressVirtualAddress.setStatus(_A)
_MwStationIpaddressIpv6AddrType_Type=MwlIpv6AddrType
_MwStationIpaddressIpv6AddrType_Object=MibTableColumn
mwStationIpaddressIpv6AddrType=_MwStationIpaddressIpv6AddrType_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,6),_MwStationIpaddressIpv6AddrType_Type())
mwStationIpaddressIpv6AddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwStationIpaddressIpv6AddrType.setStatus(_A)
_MwStationIpaddressRowStatus_Type=RowStatus
_MwStationIpaddressRowStatus_Object=MibTableColumn
mwStationIpaddressRowStatus=_MwStationIpaddressRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,4,2,1,7),_MwStationIpaddressRowStatus_Type())
mwStationIpaddressRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mwStationIpaddressRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mwConfigStation':mwConfigStation,'mwStationTable':mwStationTable,'mwStationEntry':mwStationEntry,_F:mwStationTableIndex,'mwStationMacAddress':mwStationMacAddress,'mwStationIpv6Address':mwStationIpv6Address,'mwStationAp':mwStationAp,'mwStationApName':mwStationApName,'mwStationL3State':mwStationL3State,'mwStationVlanTag':mwStationVlanTag,'mwStationAuthUser':mwStationAuthUser,'mwStationVlanName':mwStationVlanName,'mwStationRadioType':mwStationRadioType,'mwStationL2ModeState':mwStationL2ModeState,'mwStationCurrentRssi':mwStationCurrentRssi,'mwStationTxThroughput':mwStationTxThroughput,'mwStationRxThroughput':mwStationRxThroughput,'mwStationLossPercentage':mwStationLossPercentage,'mwStationAddrAssignmentType':mwStationAddrAssignmentType,'mwStationChannelUtilization':mwStationChannelUtilization,'mwStationVirtualPort':mwStationVirtualPort,'mwStationDeviceType':mwStationDeviceType,'mwStationFilterId':mwStationFilterId,'mwStationFpDeviceType':mwStationFpDeviceType,'mwStationFpOsType':mwStationFpOsType,'mwStationIpMode':mwStationIpMode,'mwStationVlanPoolName':mwStationVlanPoolName,'mwStationRowStatus':mwStationRowStatus,'mwStationIpaddressTable':mwStationIpaddressTable,'mwStationIpaddressEntry':mwStationIpaddressEntry,_H:mwStationIpaddressTableIndex,'mwStationIpaddressMacAddress':mwStationIpaddressMacAddress,'mwStationIpaddressIpAddress':mwStationIpaddressIpAddress,'mwStationIpaddressAddrAssignmentType':mwStationIpaddressAddrAssignmentType,'mwStationIpaddressVirtualAddress':mwStationIpaddressVirtualAddress,'mwStationIpaddressIpv6AddrType':mwStationIpaddressIpv6AddrType,'mwStationIpaddressRowStatus':mwStationIpaddressRowStatus})