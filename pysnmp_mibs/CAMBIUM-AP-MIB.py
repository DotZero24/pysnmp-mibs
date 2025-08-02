_K='read-write'
_J='cambiumMeshClientMACAddressIndex'
_I='cambiumWlanIndex'
_H='cambiumClientMACAddressIndex'
_G='cambiumRadioIndex'
_F='cambiumAPMACAddress'
_E='Integer32'
_D='CAMBIUM-AP-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','TextualConvention')
cnPilotMIB=ModuleIdentity((1,3,6,1,4,1,17713,22))
if mibBuilder.loadTexts:cnPilotMIB.setRevisions(('2015-09-09 12:38',))
_Cambium_ObjectIdentity=ObjectIdentity
cambium=_Cambium_ObjectIdentity((1,3,6,1,4,1,17713))
_CambiumStateGroup_ObjectIdentity=ObjectIdentity
cambiumStateGroup=_CambiumStateGroup_ObjectIdentity((1,3,6,1,4,1,17713,22,1))
_CambiumAccessPointTable_Object=MibTable
cambiumAccessPointTable=_CambiumAccessPointTable_Object((1,3,6,1,4,1,17713,22,1,1))
if mibBuilder.loadTexts:cambiumAccessPointTable.setStatus(_A)
_CambiumAccessPointEntry_Object=MibTableRow
cambiumAccessPointEntry=_CambiumAccessPointEntry_Object((1,3,6,1,4,1,17713,22,1,1,1))
cambiumAccessPointEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:cambiumAccessPointEntry.setStatus(_A)
_CambiumAPMACAddress_Type=MacAddress
_CambiumAPMACAddress_Object=MibTableColumn
cambiumAPMACAddress=_CambiumAPMACAddress_Object((1,3,6,1,4,1,17713,22,1,1,1,1),_CambiumAPMACAddress_Type())
cambiumAPMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPMACAddress.setStatus(_A)
class _CambiumAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumAPName_Type.__name__=_C
_CambiumAPName_Object=MibTableColumn
cambiumAPName=_CambiumAPName_Object((1,3,6,1,4,1,17713,22,1,1,1,2),_CambiumAPName_Type())
cambiumAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPName.setStatus(_A)
class _CambiumAPIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumAPIPAddress_Type.__name__=_C
_CambiumAPIPAddress_Object=MibTableColumn
cambiumAPIPAddress=_CambiumAPIPAddress_Object((1,3,6,1,4,1,17713,22,1,1,1,3),_CambiumAPIPAddress_Type())
cambiumAPIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPIPAddress.setStatus(_A)
class _CambiumAPSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumAPSerialNum_Type.__name__=_C
_CambiumAPSerialNum_Object=MibTableColumn
cambiumAPSerialNum=_CambiumAPSerialNum_Object((1,3,6,1,4,1,17713,22,1,1,1,4),_CambiumAPSerialNum_Type())
cambiumAPSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPSerialNum.setStatus(_A)
class _CambiumAPModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumAPModel_Type.__name__=_C
_CambiumAPModel_Object=MibTableColumn
cambiumAPModel=_CambiumAPModel_Object((1,3,6,1,4,1,17713,22,1,1,1,5),_CambiumAPModel_Type())
cambiumAPModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPModel.setStatus(_A)
_CambiumAPCPUUtilization_Type=Integer32
_CambiumAPCPUUtilization_Object=MibTableColumn
cambiumAPCPUUtilization=_CambiumAPCPUUtilization_Object((1,3,6,1,4,1,17713,22,1,1,1,6),_CambiumAPCPUUtilization_Type())
cambiumAPCPUUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPCPUUtilization.setStatus(_A)
_CambiumAPMemoryFree_Type=Integer32
_CambiumAPMemoryFree_Object=MibTableColumn
cambiumAPMemoryFree=_CambiumAPMemoryFree_Object((1,3,6,1,4,1,17713,22,1,1,1,7),_CambiumAPMemoryFree_Type())
cambiumAPMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPMemoryFree.setStatus(_A)
class _CambiumAPSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumAPSWVersion_Type.__name__=_C
_CambiumAPSWVersion_Object=MibTableColumn
cambiumAPSWVersion=_CambiumAPSWVersion_Object((1,3,6,1,4,1,17713,22,1,1,1,8),_CambiumAPSWVersion_Type())
cambiumAPSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPSWVersion.setStatus(_A)
_CambiumAPUptime_Type=TimeTicks
_CambiumAPUptime_Object=MibTableColumn
cambiumAPUptime=_CambiumAPUptime_Object((1,3,6,1,4,1,17713,22,1,1,1,9),_CambiumAPUptime_Type())
cambiumAPUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPUptime.setStatus(_A)
class _CambiumAPHWType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumAPHWType_Type.__name__=_C
_CambiumAPHWType_Object=MibTableColumn
cambiumAPHWType=_CambiumAPHWType_Object((1,3,6,1,4,1,17713,22,1,1,1,10),_CambiumAPHWType_Type())
cambiumAPHWType.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPHWType.setStatus(_A)
class _CambiumAPRegulatory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumAPRegulatory_Type.__name__=_C
_CambiumAPRegulatory_Object=MibTableColumn
cambiumAPRegulatory=_CambiumAPRegulatory_Object((1,3,6,1,4,1,17713,22,1,1,1,11),_CambiumAPRegulatory_Type())
cambiumAPRegulatory.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPRegulatory.setStatus(_A)
class _CambiumAPCnmConstaus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumAPCnmConstaus_Type.__name__=_C
_CambiumAPCnmConstaus_Object=MibTableColumn
cambiumAPCnmConstaus=_CambiumAPCnmConstaus_Object((1,3,6,1,4,1,17713,22,1,1,1,12),_CambiumAPCnmConstaus_Type())
cambiumAPCnmConstaus.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPCnmConstaus.setStatus(_A)
class _CambiumAPCnmAccID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumAPCnmAccID_Type.__name__=_C
_CambiumAPCnmAccID_Object=MibTableColumn
cambiumAPCnmAccID=_CambiumAPCnmAccID_Object((1,3,6,1,4,1,17713,22,1,1,1,13),_CambiumAPCnmAccID_Type())
cambiumAPCnmAccID.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPCnmAccID.setStatus(_A)
_CambiumAPTotalClients_Type=Integer32
_CambiumAPTotalClients_Object=MibTableColumn
cambiumAPTotalClients=_CambiumAPTotalClients_Object((1,3,6,1,4,1,17713,22,1,1,1,14),_CambiumAPTotalClients_Type())
cambiumAPTotalClients.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPTotalClients.setStatus(_A)
class _CambiumAPCheckUpgradeStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumAPCheckUpgradeStatus_Type.__name__=_C
_CambiumAPCheckUpgradeStatus_Object=MibTableColumn
cambiumAPCheckUpgradeStatus=_CambiumAPCheckUpgradeStatus_Object((1,3,6,1,4,1,17713,22,1,1,1,15),_CambiumAPCheckUpgradeStatus_Type())
cambiumAPCheckUpgradeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumAPCheckUpgradeStatus.setStatus(_A)
_CambiumRadioTable_Object=MibTable
cambiumRadioTable=_CambiumRadioTable_Object((1,3,6,1,4,1,17713,22,1,2))
if mibBuilder.loadTexts:cambiumRadioTable.setStatus(_A)
_CambiumRadioEntry_Object=MibTableRow
cambiumRadioEntry=_CambiumRadioEntry_Object((1,3,6,1,4,1,17713,22,1,2,1))
cambiumRadioEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:cambiumRadioEntry.setStatus(_A)
_CambiumRadioIndex_Type=Integer32
_CambiumRadioIndex_Object=MibTableColumn
cambiumRadioIndex=_CambiumRadioIndex_Object((1,3,6,1,4,1,17713,22,1,2,1,1),_CambiumRadioIndex_Type())
cambiumRadioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioIndex.setStatus(_A)
_CambiumRadioMACAddress_Type=MacAddress
_CambiumRadioMACAddress_Object=MibTableColumn
cambiumRadioMACAddress=_CambiumRadioMACAddress_Object((1,3,6,1,4,1,17713,22,1,2,1,2),_CambiumRadioMACAddress_Type())
cambiumRadioMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioMACAddress.setStatus(_A)
class _CambiumRadioBandType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumRadioBandType_Type.__name__=_C
_CambiumRadioBandType_Object=MibTableColumn
cambiumRadioBandType=_CambiumRadioBandType_Object((1,3,6,1,4,1,17713,22,1,2,1,3),_CambiumRadioBandType_Type())
cambiumRadioBandType.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioBandType.setStatus(_A)
_CambiumRadioWlan_Type=Integer32
_CambiumRadioWlan_Object=MibTableColumn
cambiumRadioWlan=_CambiumRadioWlan_Object((1,3,6,1,4,1,17713,22,1,2,1,4),_CambiumRadioWlan_Type())
cambiumRadioWlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioWlan.setStatus(_A)
_CambiumRadioNumClients_Type=Integer32
_CambiumRadioNumClients_Object=MibTableColumn
cambiumRadioNumClients=_CambiumRadioNumClients_Object((1,3,6,1,4,1,17713,22,1,2,1,5),_CambiumRadioNumClients_Type())
cambiumRadioNumClients.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioNumClients.setStatus(_A)
class _CambiumRadioChannel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumRadioChannel_Type.__name__=_C
_CambiumRadioChannel_Object=MibTableColumn
cambiumRadioChannel=_CambiumRadioChannel_Object((1,3,6,1,4,1,17713,22,1,2,1,6),_CambiumRadioChannel_Type())
cambiumRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioChannel.setStatus(_A)
class _CambiumRadioChannelWidth_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumRadioChannelWidth_Type.__name__=_C
_CambiumRadioChannelWidth_Object=MibTableColumn
cambiumRadioChannelWidth=_CambiumRadioChannelWidth_Object((1,3,6,1,4,1,17713,22,1,2,1,7),_CambiumRadioChannelWidth_Type())
cambiumRadioChannelWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioChannelWidth.setStatus(_A)
_CambiumRadioTransmitPower_Type=Integer32
_CambiumRadioTransmitPower_Object=MibTableColumn
cambiumRadioTransmitPower=_CambiumRadioTransmitPower_Object((1,3,6,1,4,1,17713,22,1,2,1,8),_CambiumRadioTransmitPower_Type())
cambiumRadioTransmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioTransmitPower.setStatus(_A)
_CambiumRadioTotalTxPackets_Type=Counter32
_CambiumRadioTotalTxPackets_Object=MibTableColumn
cambiumRadioTotalTxPackets=_CambiumRadioTotalTxPackets_Object((1,3,6,1,4,1,17713,22,1,2,1,9),_CambiumRadioTotalTxPackets_Type())
cambiumRadioTotalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioTotalTxPackets.setStatus(_A)
_CambiumRadioTotalRxPackets_Type=Counter32
_CambiumRadioTotalRxPackets_Object=MibTableColumn
cambiumRadioTotalRxPackets=_CambiumRadioTotalRxPackets_Object((1,3,6,1,4,1,17713,22,1,2,1,10),_CambiumRadioTotalRxPackets_Type())
cambiumRadioTotalRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioTotalRxPackets.setStatus(_A)
_CambiumRadioTxDataBytes_Type=Counter32
_CambiumRadioTxDataBytes_Object=MibTableColumn
cambiumRadioTxDataBytes=_CambiumRadioTxDataBytes_Object((1,3,6,1,4,1,17713,22,1,2,1,11),_CambiumRadioTxDataBytes_Type())
cambiumRadioTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioTxDataBytes.setStatus(_A)
_CambiumRadioRxDataBytes_Type=Counter32
_CambiumRadioRxDataBytes_Object=MibTableColumn
cambiumRadioRxDataBytes=_CambiumRadioRxDataBytes_Object((1,3,6,1,4,1,17713,22,1,2,1,12),_CambiumRadioRxDataBytes_Type())
cambiumRadioRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioRxDataBytes.setStatus(_A)
class _CambiumRadioState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumRadioState_Type.__name__=_C
_CambiumRadioState_Object=MibTableColumn
cambiumRadioState=_CambiumRadioState_Object((1,3,6,1,4,1,17713,22,1,2,1,13),_CambiumRadioState_Type())
cambiumRadioState.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioState.setStatus(_A)
_CambiumRadioDfsStatus_Type=Integer32
_CambiumRadioDfsStatus_Object=MibTableColumn
cambiumRadioDfsStatus=_CambiumRadioDfsStatus_Object((1,3,6,1,4,1,17713,22,1,2,1,14),_CambiumRadioDfsStatus_Type())
cambiumRadioDfsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioDfsStatus.setStatus(_A)
_CambiumRadioDfsDetect_Type=Integer32
_CambiumRadioDfsDetect_Object=MibTableColumn
cambiumRadioDfsDetect=_CambiumRadioDfsDetect_Object((1,3,6,1,4,1,17713,22,1,2,1,15),_CambiumRadioDfsDetect_Type())
cambiumRadioDfsDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioDfsDetect.setStatus(_A)
class _CambiumRadioNoiseFloor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumRadioNoiseFloor_Type.__name__=_C
_CambiumRadioNoiseFloor_Object=MibTableColumn
cambiumRadioNoiseFloor=_CambiumRadioNoiseFloor_Object((1,3,6,1,4,1,17713,22,1,2,1,16),_CambiumRadioNoiseFloor_Type())
cambiumRadioNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioNoiseFloor.setStatus(_A)
class _CambiumRadioInterference_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumRadioInterference_Type.__name__=_C
_CambiumRadioInterference_Object=MibTableColumn
cambiumRadioInterference=_CambiumRadioInterference_Object((1,3,6,1,4,1,17713,22,1,2,1,17),_CambiumRadioInterference_Type())
cambiumRadioInterference.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioInterference.setStatus(_A)
class _CambiumRadioAirtime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumRadioAirtime_Type.__name__=_C
_CambiumRadioAirtime_Object=MibTableColumn
cambiumRadioAirtime=_CambiumRadioAirtime_Object((1,3,6,1,4,1,17713,22,1,2,1,18),_CambiumRadioAirtime_Type())
cambiumRadioAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumRadioAirtime.setStatus(_A)
_CambiumClientTable_Object=MibTable
cambiumClientTable=_CambiumClientTable_Object((1,3,6,1,4,1,17713,22,1,3))
if mibBuilder.loadTexts:cambiumClientTable.setStatus(_A)
_CambiumClientEntry_Object=MibTableRow
cambiumClientEntry=_CambiumClientEntry_Object((1,3,6,1,4,1,17713,22,1,3,1))
cambiumClientEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:cambiumClientEntry.setStatus(_A)
_CambiumClientMACAddressIndex_Type=Integer32
_CambiumClientMACAddressIndex_Object=MibTableColumn
cambiumClientMACAddressIndex=_CambiumClientMACAddressIndex_Object((1,3,6,1,4,1,17713,22,1,3,1,1),_CambiumClientMACAddressIndex_Type())
cambiumClientMACAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientMACAddressIndex.setStatus(_A)
_CambiumClientMACAddress_Type=MacAddress
_CambiumClientMACAddress_Object=MibTableColumn
cambiumClientMACAddress=_CambiumClientMACAddress_Object((1,3,6,1,4,1,17713,22,1,3,1,2),_CambiumClientMACAddress_Type())
cambiumClientMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientMACAddress.setStatus(_A)
class _CambiumClientIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumClientIPAddress_Type.__name__=_C
_CambiumClientIPAddress_Object=MibTableColumn
cambiumClientIPAddress=_CambiumClientIPAddress_Object((1,3,6,1,4,1,17713,22,1,3,1,3),_CambiumClientIPAddress_Type())
cambiumClientIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientIPAddress.setStatus(_A)
class _CambiumClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumClientName_Type.__name__=_C
_CambiumClientName_Object=MibTableColumn
cambiumClientName=_CambiumClientName_Object((1,3,6,1,4,1,17713,22,1,3,1,4),_CambiumClientName_Type())
cambiumClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientName.setStatus(_A)
class _CambiumClientSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumClientSsid_Type.__name__=_C
_CambiumClientSsid_Object=MibTableColumn
cambiumClientSsid=_CambiumClientSsid_Object((1,3,6,1,4,1,17713,22,1,3,1,5),_CambiumClientSsid_Type())
cambiumClientSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientSsid.setStatus(_A)
class _CambiumClientVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumClientVendorName_Type.__name__=_C
_CambiumClientVendorName_Object=MibTableColumn
cambiumClientVendorName=_CambiumClientVendorName_Object((1,3,6,1,4,1,17713,22,1,3,1,6),_CambiumClientVendorName_Type())
cambiumClientVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientVendorName.setStatus(_A)
class _CambiumClientHwmode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumClientHwmode_Type.__name__=_C
_CambiumClientHwmode_Object=MibTableColumn
cambiumClientHwmode=_CambiumClientHwmode_Object((1,3,6,1,4,1,17713,22,1,3,1,7),_CambiumClientHwmode_Type())
cambiumClientHwmode.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientHwmode.setStatus(_A)
_CambiumClientRadioIndex_Type=Integer32
_CambiumClientRadioIndex_Object=MibTableColumn
cambiumClientRadioIndex=_CambiumClientRadioIndex_Object((1,3,6,1,4,1,17713,22,1,3,1,8),_CambiumClientRadioIndex_Type())
cambiumClientRadioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientRadioIndex.setStatus(_A)
_CambiumClientWlan_Type=Integer32
_CambiumClientWlan_Object=MibTableColumn
cambiumClientWlan=_CambiumClientWlan_Object((1,3,6,1,4,1,17713,22,1,3,1,9),_CambiumClientWlan_Type())
cambiumClientWlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientWlan.setStatus(_A)
_CambiumClientVlan_Type=Integer32
_CambiumClientVlan_Object=MibTableColumn
cambiumClientVlan=_CambiumClientVlan_Object((1,3,6,1,4,1,17713,22,1,3,1,10),_CambiumClientVlan_Type())
cambiumClientVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientVlan.setStatus(_A)
_CambiumClientSNR_Type=Integer32
_CambiumClientSNR_Object=MibTableColumn
cambiumClientSNR=_CambiumClientSNR_Object((1,3,6,1,4,1,17713,22,1,3,1,11),_CambiumClientSNR_Type())
cambiumClientSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientSNR.setStatus(_A)
class _CambiumClientTxRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumClientTxRate_Type.__name__=_C
_CambiumClientTxRate_Object=MibTableColumn
cambiumClientTxRate=_CambiumClientTxRate_Object((1,3,6,1,4,1,17713,22,1,3,1,12),_CambiumClientTxRate_Type())
cambiumClientTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientTxRate.setStatus(_A)
_CambiumClientTotalTxPackets_Type=Counter32
_CambiumClientTotalTxPackets_Object=MibTableColumn
cambiumClientTotalTxPackets=_CambiumClientTotalTxPackets_Object((1,3,6,1,4,1,17713,22,1,3,1,13),_CambiumClientTotalTxPackets_Type())
cambiumClientTotalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientTotalTxPackets.setStatus(_A)
_CambiumClientTxDataBytes_Type=Counter32
_CambiumClientTxDataBytes_Object=MibTableColumn
cambiumClientTxDataBytes=_CambiumClientTxDataBytes_Object((1,3,6,1,4,1,17713,22,1,3,1,14),_CambiumClientTxDataBytes_Type())
cambiumClientTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientTxDataBytes.setStatus(_A)
_CambiumClientTotalRxPackets_Type=Counter32
_CambiumClientTotalRxPackets_Object=MibTableColumn
cambiumClientTotalRxPackets=_CambiumClientTotalRxPackets_Object((1,3,6,1,4,1,17713,22,1,3,1,15),_CambiumClientTotalRxPackets_Type())
cambiumClientTotalRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientTotalRxPackets.setStatus(_A)
_CambiumClientRxDataBytes_Type=Counter32
_CambiumClientRxDataBytes_Object=MibTableColumn
cambiumClientRxDataBytes=_CambiumClientRxDataBytes_Object((1,3,6,1,4,1,17713,22,1,3,1,16),_CambiumClientRxDataBytes_Type())
cambiumClientRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumClientRxDataBytes.setStatus(_A)
_CambiumWlanTable_Object=MibTable
cambiumWlanTable=_CambiumWlanTable_Object((1,3,6,1,4,1,17713,22,1,4))
if mibBuilder.loadTexts:cambiumWlanTable.setStatus(_A)
_CambiumWlanEntry_Object=MibTableRow
cambiumWlanEntry=_CambiumWlanEntry_Object((1,3,6,1,4,1,17713,22,1,4,1))
cambiumWlanEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:cambiumWlanEntry.setStatus(_A)
_CambiumWlanIndex_Type=Integer32
_CambiumWlanIndex_Object=MibTableColumn
cambiumWlanIndex=_CambiumWlanIndex_Object((1,3,6,1,4,1,17713,22,1,4,1,1),_CambiumWlanIndex_Type())
cambiumWlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanIndex.setStatus(_A)
class _CambiumWlanSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumWlanSsid_Type.__name__=_C
_CambiumWlanSsid_Object=MibTableColumn
cambiumWlanSsid=_CambiumWlanSsid_Object((1,3,6,1,4,1,17713,22,1,4,1,2),_CambiumWlanSsid_Type())
cambiumWlanSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanSsid.setStatus(_A)
class _CambiumWlanBand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumWlanBand_Type.__name__=_C
_CambiumWlanBand_Object=MibTableColumn
cambiumWlanBand=_CambiumWlanBand_Object((1,3,6,1,4,1,17713,22,1,4,1,3),_CambiumWlanBand_Type())
cambiumWlanBand.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanBand.setStatus(_A)
_CambiumWlanVlan_Type=Integer32
_CambiumWlanVlan_Object=MibTableColumn
cambiumWlanVlan=_CambiumWlanVlan_Object((1,3,6,1,4,1,17713,22,1,4,1,4),_CambiumWlanVlan_Type())
cambiumWlanVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanVlan.setStatus(_A)
class _CambiumWlanSecurity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumWlanSecurity_Type.__name__=_C
_CambiumWlanSecurity_Object=MibTableColumn
cambiumWlanSecurity=_CambiumWlanSecurity_Object((1,3,6,1,4,1,17713,22,1,4,1,5),_CambiumWlanSecurity_Type())
cambiumWlanSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanSecurity.setStatus(_A)
class _CambiumWlanGuestAccess_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumWlanGuestAccess_Type.__name__=_C
_CambiumWlanGuestAccess_Object=MibTableColumn
cambiumWlanGuestAccess=_CambiumWlanGuestAccess_Object((1,3,6,1,4,1,17713,22,1,4,1,6),_CambiumWlanGuestAccess_Type())
cambiumWlanGuestAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanGuestAccess.setStatus(_A)
_CambiumWlanNumClients_Type=Integer32
_CambiumWlanNumClients_Object=MibTableColumn
cambiumWlanNumClients=_CambiumWlanNumClients_Object((1,3,6,1,4,1,17713,22,1,4,1,7),_CambiumWlanNumClients_Type())
cambiumWlanNumClients.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanNumClients.setStatus(_A)
_CambiumWlanTotalTxPackets_Type=Counter32
_CambiumWlanTotalTxPackets_Object=MibTableColumn
cambiumWlanTotalTxPackets=_CambiumWlanTotalTxPackets_Object((1,3,6,1,4,1,17713,22,1,4,1,8),_CambiumWlanTotalTxPackets_Type())
cambiumWlanTotalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanTotalTxPackets.setStatus(_A)
_CambiumWlanTxDataBytes_Type=Counter32
_CambiumWlanTxDataBytes_Object=MibTableColumn
cambiumWlanTxDataBytes=_CambiumWlanTxDataBytes_Object((1,3,6,1,4,1,17713,22,1,4,1,9),_CambiumWlanTxDataBytes_Type())
cambiumWlanTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanTxDataBytes.setStatus(_A)
_CambiumWlanTotalRxPackets_Type=Counter32
_CambiumWlanTotalRxPackets_Object=MibTableColumn
cambiumWlanTotalRxPackets=_CambiumWlanTotalRxPackets_Object((1,3,6,1,4,1,17713,22,1,4,1,10),_CambiumWlanTotalRxPackets_Type())
cambiumWlanTotalRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanTotalRxPackets.setStatus(_A)
_CambiumWlanRxDataBytes_Type=Counter32
_CambiumWlanRxDataBytes_Object=MibTableColumn
cambiumWlanRxDataBytes=_CambiumWlanRxDataBytes_Object((1,3,6,1,4,1,17713,22,1,4,1,11),_CambiumWlanRxDataBytes_Type())
cambiumWlanRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumWlanRxDataBytes.setStatus(_A)
_CambiumMeshClientTable_Object=MibTable
cambiumMeshClientTable=_CambiumMeshClientTable_Object((1,3,6,1,4,1,17713,22,1,5))
if mibBuilder.loadTexts:cambiumMeshClientTable.setStatus(_A)
_CambiumMeshClientEntry_Object=MibTableRow
cambiumMeshClientEntry=_CambiumMeshClientEntry_Object((1,3,6,1,4,1,17713,22,1,5,1))
cambiumMeshClientEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cambiumMeshClientEntry.setStatus(_A)
_CambiumMeshClientMACAddressIndex_Type=Integer32
_CambiumMeshClientMACAddressIndex_Object=MibTableColumn
cambiumMeshClientMACAddressIndex=_CambiumMeshClientMACAddressIndex_Object((1,3,6,1,4,1,17713,22,1,5,1,1),_CambiumMeshClientMACAddressIndex_Type())
cambiumMeshClientMACAddressIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientMACAddressIndex.setStatus(_A)
_CambiumMeshClientMACAddress_Type=MacAddress
_CambiumMeshClientMACAddress_Object=MibTableColumn
cambiumMeshClientMACAddress=_CambiumMeshClientMACAddress_Object((1,3,6,1,4,1,17713,22,1,5,1,2),_CambiumMeshClientMACAddress_Type())
cambiumMeshClientMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientMACAddress.setStatus(_A)
_CambiumMeshClientBaseMACAddress_Type=MacAddress
_CambiumMeshClientBaseMACAddress_Object=MibTableColumn
cambiumMeshClientBaseMACAddress=_CambiumMeshClientBaseMACAddress_Object((1,3,6,1,4,1,17713,22,1,5,1,3),_CambiumMeshClientBaseMACAddress_Type())
cambiumMeshClientBaseMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientBaseMACAddress.setStatus(_A)
class _CambiumMeshClientIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumMeshClientIPAddress_Type.__name__=_C
_CambiumMeshClientIPAddress_Object=MibTableColumn
cambiumMeshClientIPAddress=_CambiumMeshClientIPAddress_Object((1,3,6,1,4,1,17713,22,1,5,1,4),_CambiumMeshClientIPAddress_Type())
cambiumMeshClientIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientIPAddress.setStatus(_A)
class _CambiumMeshClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumMeshClientName_Type.__name__=_C
_CambiumMeshClientName_Object=MibTableColumn
cambiumMeshClientName=_CambiumMeshClientName_Object((1,3,6,1,4,1,17713,22,1,5,1,5),_CambiumMeshClientName_Type())
cambiumMeshClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientName.setStatus(_A)
class _CambiumMeshClientSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumMeshClientSsid_Type.__name__=_C
_CambiumMeshClientSsid_Object=MibTableColumn
cambiumMeshClientSsid=_CambiumMeshClientSsid_Object((1,3,6,1,4,1,17713,22,1,5,1,6),_CambiumMeshClientSsid_Type())
cambiumMeshClientSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientSsid.setStatus(_A)
class _CambiumMeshClientRadioBand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumMeshClientRadioBand_Type.__name__=_C
_CambiumMeshClientRadioBand_Object=MibTableColumn
cambiumMeshClientRadioBand=_CambiumMeshClientRadioBand_Object((1,3,6,1,4,1,17713,22,1,5,1,7),_CambiumMeshClientRadioBand_Type())
cambiumMeshClientRadioBand.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientRadioBand.setStatus(_A)
_CambiumMeshClientSNR_Type=Integer32
_CambiumMeshClientSNR_Object=MibTableColumn
cambiumMeshClientSNR=_CambiumMeshClientSNR_Object((1,3,6,1,4,1,17713,22,1,5,1,8),_CambiumMeshClientSNR_Type())
cambiumMeshClientSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientSNR.setStatus(_A)
_CambiumMeshClientRSSI_Type=Integer32
_CambiumMeshClientRSSI_Object=MibTableColumn
cambiumMeshClientRSSI=_CambiumMeshClientRSSI_Object((1,3,6,1,4,1,17713,22,1,5,1,9),_CambiumMeshClientRSSI_Type())
cambiumMeshClientRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientRSSI.setStatus(_A)
class _CambiumMeshClientStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumMeshClientStatus_Type.__name__=_C
_CambiumMeshClientStatus_Object=MibTableColumn
cambiumMeshClientStatus=_CambiumMeshClientStatus_Object((1,3,6,1,4,1,17713,22,1,5,1,10),_CambiumMeshClientStatus_Type())
cambiumMeshClientStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientStatus.setStatus(_A)
class _CambiumMeshClientDataRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CambiumMeshClientDataRate_Type.__name__=_C
_CambiumMeshClientDataRate_Object=MibTableColumn
cambiumMeshClientDataRate=_CambiumMeshClientDataRate_Object((1,3,6,1,4,1,17713,22,1,5,1,11),_CambiumMeshClientDataRate_Type())
cambiumMeshClientDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientDataRate.setStatus(_A)
_CambiumMeshClientTotalTxPackets_Type=Counter32
_CambiumMeshClientTotalTxPackets_Object=MibTableColumn
cambiumMeshClientTotalTxPackets=_CambiumMeshClientTotalTxPackets_Object((1,3,6,1,4,1,17713,22,1,5,1,12),_CambiumMeshClientTotalTxPackets_Type())
cambiumMeshClientTotalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientTotalTxPackets.setStatus(_A)
_CambiumMeshClientTxDataBytes_Type=Counter32
_CambiumMeshClientTxDataBytes_Object=MibTableColumn
cambiumMeshClientTxDataBytes=_CambiumMeshClientTxDataBytes_Object((1,3,6,1,4,1,17713,22,1,5,1,13),_CambiumMeshClientTxDataBytes_Type())
cambiumMeshClientTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientTxDataBytes.setStatus(_A)
_CambiumMeshClientTotalRxPackets_Type=Counter32
_CambiumMeshClientTotalRxPackets_Object=MibTableColumn
cambiumMeshClientTotalRxPackets=_CambiumMeshClientTotalRxPackets_Object((1,3,6,1,4,1,17713,22,1,5,1,14),_CambiumMeshClientTotalRxPackets_Type())
cambiumMeshClientTotalRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientTotalRxPackets.setStatus(_A)
_CambiumMeshClientRxDataBytes_Type=Counter32
_CambiumMeshClientRxDataBytes_Object=MibTableColumn
cambiumMeshClientRxDataBytes=_CambiumMeshClientRxDataBytes_Object((1,3,6,1,4,1,17713,22,1,5,1,15),_CambiumMeshClientRxDataBytes_Type())
cambiumMeshClientRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cambiumMeshClientRxDataBytes.setStatus(_A)
class _CambiumAPSetIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CambiumAPSetIPAddress_Type.__name__=_C
_CambiumAPSetIPAddress_Object=MibScalar
cambiumAPSetIPAddress=_CambiumAPSetIPAddress_Object((1,3,6,1,4,1,17713,22,1,6),_CambiumAPSetIPAddress_Type())
cambiumAPSetIPAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:cambiumAPSetIPAddress.setStatus(_A)
class _CambiumAPReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CambiumAPReboot_Type.__name__=_E
_CambiumAPReboot_Object=MibScalar
cambiumAPReboot=_CambiumAPReboot_Object((1,3,6,1,4,1,17713,22,1,7),_CambiumAPReboot_Type())
cambiumAPReboot.setMaxAccess(_K)
if mibBuilder.loadTexts:cambiumAPReboot.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cambium':cambium,'cnPilotMIB':cnPilotMIB,'cambiumStateGroup':cambiumStateGroup,'cambiumAccessPointTable':cambiumAccessPointTable,'cambiumAccessPointEntry':cambiumAccessPointEntry,_F:cambiumAPMACAddress,'cambiumAPName':cambiumAPName,'cambiumAPIPAddress':cambiumAPIPAddress,'cambiumAPSerialNum':cambiumAPSerialNum,'cambiumAPModel':cambiumAPModel,'cambiumAPCPUUtilization':cambiumAPCPUUtilization,'cambiumAPMemoryFree':cambiumAPMemoryFree,'cambiumAPSWVersion':cambiumAPSWVersion,'cambiumAPUptime':cambiumAPUptime,'cambiumAPHWType':cambiumAPHWType,'cambiumAPRegulatory':cambiumAPRegulatory,'cambiumAPCnmConstaus':cambiumAPCnmConstaus,'cambiumAPCnmAccID':cambiumAPCnmAccID,'cambiumAPTotalClients':cambiumAPTotalClients,'cambiumAPCheckUpgradeStatus':cambiumAPCheckUpgradeStatus,'cambiumRadioTable':cambiumRadioTable,'cambiumRadioEntry':cambiumRadioEntry,_G:cambiumRadioIndex,'cambiumRadioMACAddress':cambiumRadioMACAddress,'cambiumRadioBandType':cambiumRadioBandType,'cambiumRadioWlan':cambiumRadioWlan,'cambiumRadioNumClients':cambiumRadioNumClients,'cambiumRadioChannel':cambiumRadioChannel,'cambiumRadioChannelWidth':cambiumRadioChannelWidth,'cambiumRadioTransmitPower':cambiumRadioTransmitPower,'cambiumRadioTotalTxPackets':cambiumRadioTotalTxPackets,'cambiumRadioTotalRxPackets':cambiumRadioTotalRxPackets,'cambiumRadioTxDataBytes':cambiumRadioTxDataBytes,'cambiumRadioRxDataBytes':cambiumRadioRxDataBytes,'cambiumRadioState':cambiumRadioState,'cambiumRadioDfsStatus':cambiumRadioDfsStatus,'cambiumRadioDfsDetect':cambiumRadioDfsDetect,'cambiumRadioNoiseFloor':cambiumRadioNoiseFloor,'cambiumRadioInterference':cambiumRadioInterference,'cambiumRadioAirtime':cambiumRadioAirtime,'cambiumClientTable':cambiumClientTable,'cambiumClientEntry':cambiumClientEntry,_H:cambiumClientMACAddressIndex,'cambiumClientMACAddress':cambiumClientMACAddress,'cambiumClientIPAddress':cambiumClientIPAddress,'cambiumClientName':cambiumClientName,'cambiumClientSsid':cambiumClientSsid,'cambiumClientVendorName':cambiumClientVendorName,'cambiumClientHwmode':cambiumClientHwmode,'cambiumClientRadioIndex':cambiumClientRadioIndex,'cambiumClientWlan':cambiumClientWlan,'cambiumClientVlan':cambiumClientVlan,'cambiumClientSNR':cambiumClientSNR,'cambiumClientTxRate':cambiumClientTxRate,'cambiumClientTotalTxPackets':cambiumClientTotalTxPackets,'cambiumClientTxDataBytes':cambiumClientTxDataBytes,'cambiumClientTotalRxPackets':cambiumClientTotalRxPackets,'cambiumClientRxDataBytes':cambiumClientRxDataBytes,'cambiumWlanTable':cambiumWlanTable,'cambiumWlanEntry':cambiumWlanEntry,_I:cambiumWlanIndex,'cambiumWlanSsid':cambiumWlanSsid,'cambiumWlanBand':cambiumWlanBand,'cambiumWlanVlan':cambiumWlanVlan,'cambiumWlanSecurity':cambiumWlanSecurity,'cambiumWlanGuestAccess':cambiumWlanGuestAccess,'cambiumWlanNumClients':cambiumWlanNumClients,'cambiumWlanTotalTxPackets':cambiumWlanTotalTxPackets,'cambiumWlanTxDataBytes':cambiumWlanTxDataBytes,'cambiumWlanTotalRxPackets':cambiumWlanTotalRxPackets,'cambiumWlanRxDataBytes':cambiumWlanRxDataBytes,'cambiumMeshClientTable':cambiumMeshClientTable,'cambiumMeshClientEntry':cambiumMeshClientEntry,_J:cambiumMeshClientMACAddressIndex,'cambiumMeshClientMACAddress':cambiumMeshClientMACAddress,'cambiumMeshClientBaseMACAddress':cambiumMeshClientBaseMACAddress,'cambiumMeshClientIPAddress':cambiumMeshClientIPAddress,'cambiumMeshClientName':cambiumMeshClientName,'cambiumMeshClientSsid':cambiumMeshClientSsid,'cambiumMeshClientRadioBand':cambiumMeshClientRadioBand,'cambiumMeshClientSNR':cambiumMeshClientSNR,'cambiumMeshClientRSSI':cambiumMeshClientRSSI,'cambiumMeshClientStatus':cambiumMeshClientStatus,'cambiumMeshClientDataRate':cambiumMeshClientDataRate,'cambiumMeshClientTotalTxPackets':cambiumMeshClientTotalTxPackets,'cambiumMeshClientTxDataBytes':cambiumMeshClientTxDataBytes,'cambiumMeshClientTotalRxPackets':cambiumMeshClientTotalRxPackets,'cambiumMeshClientRxDataBytes':cambiumMeshClientRxDataBytes,'cambiumAPSetIPAddress':cambiumAPSetIPAddress,'cambiumAPReboot':cambiumAPReboot})