_J='read-create'
_I='ifIndex'
_H='IF-MIB'
_G='qtechTerminalIndex'
_F='DisplayString'
_E='qtechWlanId'
_D='QTECH-WLAN-FAT-AP-IN-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
qtechApgWlanId,=mibBuilder.importSymbols('QTECH-AC-MGMT-MIB','qtechApgWlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechStandardmibmodule=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,82))
if mibBuilder.loadTexts:qtechStandardmibmodule.setRevisions(('2010-02-28 00:00',))
_QtechStandardTraps_ObjectIdentity=ObjectIdentity
qtechStandardTraps=_QtechStandardTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,0))
_QtechConfigInfoObjects_ObjectIdentity=ObjectIdentity
qtechConfigInfoObjects=_QtechConfigInfoObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,1))
_QtechSysInfoConfig_ObjectIdentity=ObjectIdentity
qtechSysInfoConfig=_QtechSysInfoConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,1,1))
_QtechDomain_Type=DisplayString
_QtechDomain_Object=MibScalar
qtechDomain=_QtechDomain_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,1),_QtechDomain_Type())
qtechDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechDomain.setStatus(_A)
_QtechLayer2Isolate_Type=Integer32
_QtechLayer2Isolate_Object=MibScalar
qtechLayer2Isolate=_QtechLayer2Isolate_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,2),_QtechLayer2Isolate_Type())
qtechLayer2Isolate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechLayer2Isolate.setStatus(_A)
_QtechDosAttackProtect_Type=Integer32
_QtechDosAttackProtect_Object=MibScalar
qtechDosAttackProtect=_QtechDosAttackProtect_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,3),_QtechDosAttackProtect_Type())
qtechDosAttackProtect.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDosAttackProtect.setStatus(_A)
_QtechVlanConfigTable_Object=MibTable
qtechVlanConfigTable=_QtechVlanConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,4))
if mibBuilder.loadTexts:qtechVlanConfigTable.setStatus(_A)
_QtechVlanConfigEntry_Object=MibTableRow
qtechVlanConfigEntry=_QtechVlanConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,4,1))
qtechVlanConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:qtechVlanConfigEntry.setStatus(_A)
_QtechVlanId_Type=Integer32
_QtechVlanId_Object=MibTableColumn
qtechVlanId=_QtechVlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,4,1,1),_QtechVlanId_Type())
qtechVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechVlanId.setStatus(_A)
_QtechSSID_Type=DisplayString
_QtechSSID_Object=MibTableColumn
qtechSSID=_QtechSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,1,4,1,2),_QtechSSID_Type())
qtechSSID.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechSSID.setStatus(_A)
_QtechRadioInfoConfig_ObjectIdentity=ObjectIdentity
qtechRadioInfoConfig=_QtechRadioInfoConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,1,2))
_QtechRadioConfigTable_Object=MibTable
qtechRadioConfigTable=_QtechRadioConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1))
if mibBuilder.loadTexts:qtechRadioConfigTable.setStatus(_A)
_QtechRadioConfigEntry_Object=MibTableRow
qtechRadioConfigEntry=_QtechRadioConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1))
qtechRadioConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:qtechRadioConfigEntry.setStatus(_A)
_QtechSSIDNum_Type=Integer32
_QtechSSIDNum_Object=MibTableColumn
qtechSSIDNum=_QtechSSIDNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,1),_QtechSSIDNum_Type())
qtechSSIDNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSSIDNum.setStatus(_A)
_QtechRadioSecurityMch_Type=Integer32
_QtechRadioSecurityMch_Object=MibTableColumn
qtechRadioSecurityMch=_QtechRadioSecurityMch_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,2),_QtechRadioSecurityMch_Type())
qtechRadioSecurityMch.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRadioSecurityMch.setStatus(_A)
_QtechRadioSecurityParam_Type=DisplayString
_QtechRadioSecurityParam_Object=MibTableColumn
qtechRadioSecurityParam=_QtechRadioSecurityParam_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,3),_QtechRadioSecurityParam_Type())
qtechRadioSecurityParam.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRadioSecurityParam.setStatus(_A)
_QtechRadioQos_Type=Integer32
_QtechRadioQos_Object=MibTableColumn
qtechRadioQos=_QtechRadioQos_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,4),_QtechRadioQos_Type())
qtechRadioQos.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRadioQos.setStatus(_A)
_QtechRtsCtsThreshold_Type=Integer32
_QtechRtsCtsThreshold_Object=MibTableColumn
qtechRtsCtsThreshold=_QtechRtsCtsThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,5),_QtechRtsCtsThreshold_Type())
qtechRtsCtsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechRtsCtsThreshold.setStatus(_A)
_QtechMaxUserPermit_Type=Integer32
_QtechMaxUserPermit_Object=MibTableColumn
qtechMaxUserPermit=_QtechMaxUserPermit_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,6),_QtechMaxUserPermit_Type())
qtechMaxUserPermit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMaxUserPermit.setStatus(_A)
_QtechUserNumOnLine_Type=Integer32
_QtechUserNumOnLine_Object=MibTableColumn
qtechUserNumOnLine=_QtechUserNumOnLine_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,7),_QtechUserNumOnLine_Type())
qtechUserNumOnLine.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUserNumOnLine.setStatus(_A)
_QtechAirInterfaceType_Type=Integer32
_QtechAirInterfaceType_Object=MibTableColumn
qtechAirInterfaceType=_QtechAirInterfaceType_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,8),_QtechAirInterfaceType_Type())
qtechAirInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAirInterfaceType.setStatus(_A)
_QtechChannelMode_Type=Integer32
_QtechChannelMode_Object=MibTableColumn
qtechChannelMode=_QtechChannelMode_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,9),_QtechChannelMode_Type())
qtechChannelMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechChannelMode.setStatus(_A)
_QtechCurrentChannel_Type=Integer32
_QtechCurrentChannel_Object=MibTableColumn
qtechCurrentChannel=_QtechCurrentChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,10),_QtechCurrentChannel_Type())
qtechCurrentChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCurrentChannel.setStatus(_A)
_QtechSNR_Type=Integer32
_QtechSNR_Object=MibTableColumn
qtechSNR=_QtechSNR_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,11),_QtechSNR_Type())
qtechSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSNR.setStatus(_A)
_QtechHoppingTimes_Type=Integer32
_QtechHoppingTimes_Object=MibTableColumn
qtechHoppingTimes=_QtechHoppingTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,12),_QtechHoppingTimes_Type())
qtechHoppingTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechHoppingTimes.setStatus(_A)
_QtechHopDetectItvTime_Type=Integer32
_QtechHopDetectItvTime_Object=MibTableColumn
qtechHopDetectItvTime=_QtechHopDetectItvTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,13),_QtechHopDetectItvTime_Type())
qtechHopDetectItvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechHopDetectItvTime.setStatus(_A)
_QtechPowerMgr_Type=Integer32
_QtechPowerMgr_Object=MibTableColumn
qtechPowerMgr=_QtechPowerMgr_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,14),_QtechPowerMgr_Type())
qtechPowerMgr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPowerMgr.setStatus(_A)
_QtechTxPower_Type=Integer32
_QtechTxPower_Object=MibTableColumn
qtechTxPower=_QtechTxPower_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,2,1,1,15),_QtechTxPower_Type())
qtechTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTxPower.setStatus(_A)
_QtechWapiConfig_ObjectIdentity=ObjectIdentity
qtechWapiConfig=_QtechWapiConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,1,3))
_QtechWapiConfigTable_Object=MibTable
qtechWapiConfigTable=_QtechWapiConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1))
if mibBuilder.loadTexts:qtechWapiConfigTable.setStatus(_A)
_QtechWapiConfigEntry_Object=MibTableRow
qtechWapiConfigEntry=_QtechWapiConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1,1))
qtechWapiConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:qtechWapiConfigEntry.setStatus(_A)
_QtechWlanId_Type=Integer32
_QtechWlanId_Object=MibTableColumn
qtechWlanId=_QtechWlanId_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1,1,1),_QtechWlanId_Type())
qtechWlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechWlanId.setStatus(_A)
_QtechTrustASCfg_Type=Integer32
_QtechTrustASCfg_Object=MibTableColumn
qtechTrustASCfg=_QtechTrustASCfg_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1,1,2),_QtechTrustASCfg_Type())
qtechTrustASCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrustASCfg.setStatus(_A)
_QtechCertType_Type=Integer32
_QtechCertType_Object=MibTableColumn
qtechCertType=_QtechCertType_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1,1,3),_QtechCertType_Type())
qtechCertType.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechCertType.setStatus(_A)
_QtechCertState_Type=Integer32
_QtechCertState_Object=MibTableColumn
qtechCertState=_QtechCertState_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1,1,4),_QtechCertState_Type())
qtechCertState.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechCertState.setStatus(_A)
_QtechCertSetup_Type=Integer32
_QtechCertSetup_Object=MibTableColumn
qtechCertSetup=_QtechCertSetup_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,3,1,1,5),_QtechCertSetup_Type())
qtechCertSetup.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCertSetup.setStatus(_A)
_QtechAdminInfoConfig_ObjectIdentity=ObjectIdentity
qtechAdminInfoConfig=_QtechAdminInfoConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,1,4))
class _QtechAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechAdminName_Type.__name__=_F
_QtechAdminName_Object=MibScalar
qtechAdminName=_QtechAdminName_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,4,1),_QtechAdminName_Type())
qtechAdminName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAdminName.setStatus(_A)
class _QtechAdminPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechAdminPwd_Type.__name__=_F
_QtechAdminPwd_Object=MibScalar
qtechAdminPwd=_QtechAdminPwd_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,4,2),_QtechAdminPwd_Type())
qtechAdminPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAdminPwd.setStatus(_A)
_QtechPollTimeConfig_ObjectIdentity=ObjectIdentity
qtechPollTimeConfig=_QtechPollTimeConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,1,5))
_QtechPollTimeOfLast_Type=TimeTicks
_QtechPollTimeOfLast_Object=MibScalar
qtechPollTimeOfLast=_QtechPollTimeOfLast_Object((1,3,6,1,4,1,27514,1,1,10,2,82,1,5,1),_QtechPollTimeOfLast_Type())
qtechPollTimeOfLast.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechPollTimeOfLast.setStatus(_A)
_QtechPerformanceStatObjects_ObjectIdentity=ObjectIdentity
qtechPerformanceStatObjects=_QtechPerformanceStatObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,2))
_QtechAirIfServiceStat_ObjectIdentity=ObjectIdentity
qtechAirIfServiceStat=_QtechAirIfServiceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,2,1))
_QtechUplinkTotalDataFrameNum_Type=Integer32
_QtechUplinkTotalDataFrameNum_Object=MibScalar
qtechUplinkTotalDataFrameNum=_QtechUplinkTotalDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,1),_QtechUplinkTotalDataFrameNum_Type())
qtechUplinkTotalDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUplinkTotalDataFrameNum.setStatus(_A)
_QtechDownlinkTotalDataFrameNum_Type=Integer32
_QtechDownlinkTotalDataFrameNum_Object=MibScalar
qtechDownlinkTotalDataFrameNum=_QtechDownlinkTotalDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,2),_QtechDownlinkTotalDataFrameNum_Type())
qtechDownlinkTotalDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechDownlinkTotalDataFrameNum.setStatus(_A)
_QtechDownlinkTotalLostDataFrameNum_Type=Integer32
_QtechDownlinkTotalLostDataFrameNum_Object=MibScalar
qtechDownlinkTotalLostDataFrameNum=_QtechDownlinkTotalLostDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,3),_QtechDownlinkTotalLostDataFrameNum_Type())
qtechDownlinkTotalLostDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechDownlinkTotalLostDataFrameNum.setStatus(_A)
_QtechTotalSignalFrameNum_Type=Integer32
_QtechTotalSignalFrameNum_Object=MibScalar
qtechTotalSignalFrameNum=_QtechTotalSignalFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,4),_QtechTotalSignalFrameNum_Type())
qtechTotalSignalFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalSignalFrameNum.setStatus(_A)
_QtechCorrectPkgByteRxByMAC_Type=Integer32
_QtechCorrectPkgByteRxByMAC_Object=MibScalar
qtechCorrectPkgByteRxByMAC=_QtechCorrectPkgByteRxByMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,5),_QtechCorrectPkgByteRxByMAC_Type())
qtechCorrectPkgByteRxByMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechCorrectPkgByteRxByMAC.setStatus(_A)
_QtechPkgByteTxByMAC_Type=Integer32
_QtechPkgByteTxByMAC_Object=MibScalar
qtechPkgByteTxByMAC=_QtechPkgByteTxByMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,6),_QtechPkgByteTxByMAC_Type())
qtechPkgByteTxByMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechPkgByteTxByMAC.setStatus(_A)
_QtechUplinkPortFlow_Type=Integer32
_QtechUplinkPortFlow_Object=MibScalar
qtechUplinkPortFlow=_QtechUplinkPortFlow_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,7),_QtechUplinkPortFlow_Type())
qtechUplinkPortFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUplinkPortFlow.setStatus(_A)
_QtechDownlinkPortFlow_Type=Integer32
_QtechDownlinkPortFlow_Object=MibScalar
qtechDownlinkPortFlow=_QtechDownlinkPortFlow_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,1,8),_QtechDownlinkPortFlow_Type())
qtechDownlinkPortFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechDownlinkPortFlow.setStatus(_A)
_QtechTermServiceStat_ObjectIdentity=ObjectIdentity
qtechTermServiceStat=_QtechTermServiceStat_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,82,2,2))
_QtechTotalUserNum_Type=Integer32
_QtechTotalUserNum_Object=MibScalar
qtechTotalUserNum=_QtechTotalUserNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,1),_QtechTotalUserNum_Type())
qtechTotalUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalUserNum.setStatus(_A)
_QtechUserAccumulateTime_Type=Integer32
_QtechUserAccumulateTime_Object=MibScalar
qtechUserAccumulateTime=_QtechUserAccumulateTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,2),_QtechUserAccumulateTime_Type())
qtechUserAccumulateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUserAccumulateTime.setStatus(_A)
_QtechTermServiceStatSSIDTable_Object=MibTable
qtechTermServiceStatSSIDTable=_QtechTermServiceStatSSIDTable_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34))
if mibBuilder.loadTexts:qtechTermServiceStatSSIDTable.setStatus(_A)
_QtechTermServiceStatSSIDEntry_Object=MibTableRow
qtechTermServiceStatSSIDEntry=_QtechTermServiceStatSSIDEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1))
qtechTermServiceStatSSIDEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:qtechTermServiceStatSSIDEntry.setStatus(_A)
_QtechCorrectPkgByteRxByMACBySSID_Type=Integer32
_QtechCorrectPkgByteRxByMACBySSID_Object=MibTableColumn
qtechCorrectPkgByteRxByMACBySSID=_QtechCorrectPkgByteRxByMACBySSID_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,1),_QtechCorrectPkgByteRxByMACBySSID_Type())
qtechCorrectPkgByteRxByMACBySSID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechCorrectPkgByteRxByMACBySSID.setStatus(_A)
_QtechPkgByteTxByMACBySSID_Type=Integer32
_QtechPkgByteTxByMACBySSID_Object=MibTableColumn
qtechPkgByteTxByMACBySSID=_QtechPkgByteTxByMACBySSID_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,2),_QtechPkgByteTxByMACBySSID_Type())
qtechPkgByteTxByMACBySSID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechPkgByteTxByMACBySSID.setStatus(_A)
_QtechAirIfResUsageRatio_Type=Integer32
_QtechAirIfResUsageRatio_Object=MibTableColumn
qtechAirIfResUsageRatio=_QtechAirIfResUsageRatio_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,3),_QtechAirIfResUsageRatio_Type())
qtechAirIfResUsageRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechAirIfResUsageRatio.setStatus(_A)
_QtechTotalAssociationUserNum_Type=Integer32
_QtechTotalAssociationUserNum_Object=MibTableColumn
qtechTotalAssociationUserNum=_QtechTotalAssociationUserNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,4),_QtechTotalAssociationUserNum_Type())
qtechTotalAssociationUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalAssociationUserNum.setStatus(_A)
_QtechOnlineUserNum_Type=Integer32
_QtechOnlineUserNum_Object=MibTableColumn
qtechOnlineUserNum=_QtechOnlineUserNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,5),_QtechOnlineUserNum_Type())
qtechOnlineUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOnlineUserNum.setStatus(_A)
_QtechUserReqAccessTimes_Type=Integer32
_QtechUserReqAccessTimes_Object=MibTableColumn
qtechUserReqAccessTimes=_QtechUserReqAccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,6),_QtechUserReqAccessTimes_Type())
qtechUserReqAccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUserReqAccessTimes.setStatus(_A)
_QtechResponseReqAccessTimes_Type=Integer32
_QtechResponseReqAccessTimes_Object=MibTableColumn
qtechResponseReqAccessTimes=_QtechResponseReqAccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,7),_QtechResponseReqAccessTimes_Type())
qtechResponseReqAccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechResponseReqAccessTimes.setStatus(_A)
_QtechSuccessAccessTimes_Type=Integer32
_QtechSuccessAccessTimes_Object=MibTableColumn
qtechSuccessAccessTimes=_QtechSuccessAccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,8),_QtechSuccessAccessTimes_Type())
qtechSuccessAccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSuccessAccessTimes.setStatus(_A)
_QtechIneffiLinkVerifyFailTime_Type=Integer32
_QtechIneffiLinkVerifyFailTime_Object=MibTableColumn
qtechIneffiLinkVerifyFailTime=_QtechIneffiLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,9),_QtechIneffiLinkVerifyFailTime_Type())
qtechIneffiLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechIneffiLinkVerifyFailTime.setStatus(_A)
_QtechTimeoutLinkVerifyFailTime_Type=Integer32
_QtechTimeoutLinkVerifyFailTime_Object=MibTableColumn
qtechTimeoutLinkVerifyFailTime=_QtechTimeoutLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,10),_QtechTimeoutLinkVerifyFailTime_Type())
qtechTimeoutLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTimeoutLinkVerifyFailTime.setStatus(_A)
_QtechInefficiencyLinkVerifyFailTime_Type=Integer32
_QtechInefficiencyLinkVerifyFailTime_Object=MibTableColumn
qtechInefficiencyLinkVerifyFailTime=_QtechInefficiencyLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,11),_QtechInefficiencyLinkVerifyFailTime_Type())
qtechInefficiencyLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechInefficiencyLinkVerifyFailTime.setStatus(_A)
_QtechOtherReasonLinkVerifyFailTime_Type=Integer32
_QtechOtherReasonLinkVerifyFailTime_Object=MibTableColumn
qtechOtherReasonLinkVerifyFailTime=_QtechOtherReasonLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,12),_QtechOtherReasonLinkVerifyFailTime_Type())
qtechOtherReasonLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOtherReasonLinkVerifyFailTime.setStatus(_A)
_QtechIneffiAssociationFailTime_Type=Integer32
_QtechIneffiAssociationFailTime_Object=MibTableColumn
qtechIneffiAssociationFailTime=_QtechIneffiAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,13),_QtechIneffiAssociationFailTime_Type())
qtechIneffiAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechIneffiAssociationFailTime.setStatus(_A)
_QtechTimeoutAssociationFailTime_Type=Integer32
_QtechTimeoutAssociationFailTime_Object=MibTableColumn
qtechTimeoutAssociationFailTime=_QtechTimeoutAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,14),_QtechTimeoutAssociationFailTime_Type())
qtechTimeoutAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTimeoutAssociationFailTime.setStatus(_A)
_QtechInefficiencyAssociationFailTime_Type=Integer32
_QtechInefficiencyAssociationFailTime_Object=MibTableColumn
qtechInefficiencyAssociationFailTime=_QtechInefficiencyAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,15),_QtechInefficiencyAssociationFailTime_Type())
qtechInefficiencyAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechInefficiencyAssociationFailTime.setStatus(_A)
_QtechOtherReasonAssociationFailTime_Type=Integer32
_QtechOtherReasonAssociationFailTime_Object=MibTableColumn
qtechOtherReasonAssociationFailTime=_QtechOtherReasonAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,16),_QtechOtherReasonAssociationFailTime_Type())
qtechOtherReasonAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOtherReasonAssociationFailTime.setStatus(_A)
_QtechTotalReassociationAtmptTimes_Type=Integer32
_QtechTotalReassociationAtmptTimes_Object=MibTableColumn
qtechTotalReassociationAtmptTimes=_QtechTotalReassociationAtmptTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,17),_QtechTotalReassociationAtmptTimes_Type())
qtechTotalReassociationAtmptTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalReassociationAtmptTimes.setStatus(_A)
_QtechTotalReassociationSuccessTimes_Type=Integer32
_QtechTotalReassociationSuccessTimes_Object=MibTableColumn
qtechTotalReassociationSuccessTimes=_QtechTotalReassociationSuccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,18),_QtechTotalReassociationSuccessTimes_Type())
qtechTotalReassociationSuccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalReassociationSuccessTimes.setStatus(_A)
_QtechIneffiReassociationFailTime_Type=Integer32
_QtechIneffiReassociationFailTime_Object=MibTableColumn
qtechIneffiReassociationFailTime=_QtechIneffiReassociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,19),_QtechIneffiReassociationFailTime_Type())
qtechIneffiReassociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechIneffiReassociationFailTime.setStatus(_A)
_QtechTimeoutReassociationFailTime_Type=Integer32
_QtechTimeoutReassociationFailTime_Object=MibTableColumn
qtechTimeoutReassociationFailTime=_QtechTimeoutReassociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,20),_QtechTimeoutReassociationFailTime_Type())
qtechTimeoutReassociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTimeoutReassociationFailTime.setStatus(_A)
_QtechInefficiencyReassociationFailTime_Type=Integer32
_QtechInefficiencyReassociationFailTime_Object=MibTableColumn
qtechInefficiencyReassociationFailTime=_QtechInefficiencyReassociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,21),_QtechInefficiencyReassociationFailTime_Type())
qtechInefficiencyReassociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechInefficiencyReassociationFailTime.setStatus(_A)
_QtechOtherReasonReassociationFailTime_Type=Integer32
_QtechOtherReasonReassociationFailTime_Object=MibTableColumn
qtechOtherReasonReassociationFailTime=_QtechOtherReasonReassociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,22),_QtechOtherReasonReassociationFailTime_Type())
qtechOtherReasonReassociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOtherReasonReassociationFailTime.setStatus(_A)
_QtechTotalIdentificationAtmptTimes_Type=Integer32
_QtechTotalIdentificationAtmptTimes_Object=MibTableColumn
qtechTotalIdentificationAtmptTimes=_QtechTotalIdentificationAtmptTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,23),_QtechTotalIdentificationAtmptTimes_Type())
qtechTotalIdentificationAtmptTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalIdentificationAtmptTimes.setStatus(_A)
_QtechTotalIdentificationSuccessTimes_Type=Integer32
_QtechTotalIdentificationSuccessTimes_Object=MibTableColumn
qtechTotalIdentificationSuccessTimes=_QtechTotalIdentificationSuccessTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,24),_QtechTotalIdentificationSuccessTimes_Type())
qtechTotalIdentificationSuccessTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalIdentificationSuccessTimes.setStatus(_A)
_QtechPwdErrorIdentifyFailTime_Type=Integer32
_QtechPwdErrorIdentifyFailTime_Object=MibTableColumn
qtechPwdErrorIdentifyFailTime=_QtechPwdErrorIdentifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,25),_QtechPwdErrorIdentifyFailTime_Type())
qtechPwdErrorIdentifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechPwdErrorIdentifyFailTime.setStatus(_A)
_QtechIneffiIdentificationFailTime_Type=Integer32
_QtechIneffiIdentificationFailTime_Object=MibTableColumn
qtechIneffiIdentificationFailTime=_QtechIneffiIdentificationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,26),_QtechIneffiIdentificationFailTime_Type())
qtechIneffiIdentificationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechIneffiIdentificationFailTime.setStatus(_A)
_QtechTimeoutIdentificationFailTime_Type=Integer32
_QtechTimeoutIdentificationFailTime_Object=MibTableColumn
qtechTimeoutIdentificationFailTime=_QtechTimeoutIdentificationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,27),_QtechTimeoutIdentificationFailTime_Type())
qtechTimeoutIdentificationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTimeoutIdentificationFailTime.setStatus(_A)
_QtechInefficiencyIdentificationFailTime_Type=Integer32
_QtechInefficiencyIdentificationFailTime_Object=MibTableColumn
qtechInefficiencyIdentificationFailTime=_QtechInefficiencyIdentificationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,28),_QtechInefficiencyIdentificationFailTime_Type())
qtechInefficiencyIdentificationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechInefficiencyIdentificationFailTime.setStatus(_A)
_QtechOtherReasonIdentificationFailTime_Type=Integer32
_QtechOtherReasonIdentificationFailTime_Object=MibTableColumn
qtechOtherReasonIdentificationFailTime=_QtechOtherReasonIdentificationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,29),_QtechOtherReasonIdentificationFailTime_Type())
qtechOtherReasonIdentificationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOtherReasonIdentificationFailTime.setStatus(_A)
_QtechTotalRemoveLinkVerifyFailTimes_Type=Integer32
_QtechTotalRemoveLinkVerifyFailTimes_Object=MibTableColumn
qtechTotalRemoveLinkVerifyFailTimes=_QtechTotalRemoveLinkVerifyFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,30),_QtechTotalRemoveLinkVerifyFailTimes_Type())
qtechTotalRemoveLinkVerifyFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalRemoveLinkVerifyFailTimes.setStatus(_A)
_QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Type=Integer32
_QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Object=MibTableColumn
qtechLeaveAPCoverageRemoveLinkVerifyFailTimes=_QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,31),_QtechLeaveAPCoverageRemoveLinkVerifyFailTimes_Type())
qtechLeaveAPCoverageRemoveLinkVerifyFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechLeaveAPCoverageRemoveLinkVerifyFailTimes.setStatus(_A)
_QtechInefficiencyRemoveLinkVerifyFailTime_Type=Integer32
_QtechInefficiencyRemoveLinkVerifyFailTime_Object=MibTableColumn
qtechInefficiencyRemoveLinkVerifyFailTime=_QtechInefficiencyRemoveLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,32),_QtechInefficiencyRemoveLinkVerifyFailTime_Type())
qtechInefficiencyRemoveLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechInefficiencyRemoveLinkVerifyFailTime.setStatus(_A)
_QtechLinkVerifyFailRemoveLinkVerifyFailTime_Type=Integer32
_QtechLinkVerifyFailRemoveLinkVerifyFailTime_Object=MibTableColumn
qtechLinkVerifyFailRemoveLinkVerifyFailTime=_QtechLinkVerifyFailRemoveLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,33),_QtechLinkVerifyFailRemoveLinkVerifyFailTime_Type())
qtechLinkVerifyFailRemoveLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechLinkVerifyFailRemoveLinkVerifyFailTime.setStatus(_A)
_QtechOtherReasonRemoveLinkVerifyFailTime_Type=Integer32
_QtechOtherReasonRemoveLinkVerifyFailTime_Object=MibTableColumn
qtechOtherReasonRemoveLinkVerifyFailTime=_QtechOtherReasonRemoveLinkVerifyFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,34),_QtechOtherReasonRemoveLinkVerifyFailTime_Type())
qtechOtherReasonRemoveLinkVerifyFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOtherReasonRemoveLinkVerifyFailTime.setStatus(_A)
_QtechTotalRemoveLinkAssociationTimes_Type=Integer32
_QtechTotalRemoveLinkAssociationTimes_Object=MibTableColumn
qtechTotalRemoveLinkAssociationTimes=_QtechTotalRemoveLinkAssociationTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,35),_QtechTotalRemoveLinkAssociationTimes_Type())
qtechTotalRemoveLinkAssociationTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalRemoveLinkAssociationTimes.setStatus(_A)
_QtechLeaveAPCoverageRemoveAssociationFailTimes_Type=Integer32
_QtechLeaveAPCoverageRemoveAssociationFailTimes_Object=MibTableColumn
qtechLeaveAPCoverageRemoveAssociationFailTimes=_QtechLeaveAPCoverageRemoveAssociationFailTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,36),_QtechLeaveAPCoverageRemoveAssociationFailTimes_Type())
qtechLeaveAPCoverageRemoveAssociationFailTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechLeaveAPCoverageRemoveAssociationFailTimes.setStatus(_A)
_QtechInefficiencyRemoveAssociationFailTime_Type=Integer32
_QtechInefficiencyRemoveAssociationFailTime_Object=MibTableColumn
qtechInefficiencyRemoveAssociationFailTime=_QtechInefficiencyRemoveAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,37),_QtechInefficiencyRemoveAssociationFailTime_Type())
qtechInefficiencyRemoveAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechInefficiencyRemoveAssociationFailTime.setStatus(_A)
_QtechAssociationFailRemoveAssociationFailTime_Type=Integer32
_QtechAssociationFailRemoveAssociationFailTime_Object=MibTableColumn
qtechAssociationFailRemoveAssociationFailTime=_QtechAssociationFailRemoveAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,38),_QtechAssociationFailRemoveAssociationFailTime_Type())
qtechAssociationFailRemoveAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechAssociationFailRemoveAssociationFailTime.setStatus(_A)
_QtechOtherReasonRemoveAssociationFailTime_Type=Integer32
_QtechOtherReasonRemoveAssociationFailTime_Object=MibTableColumn
qtechOtherReasonRemoveAssociationFailTime=_QtechOtherReasonRemoveAssociationFailTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,34,1,39),_QtechOtherReasonRemoveAssociationFailTime_Type())
qtechOtherReasonRemoveAssociationFailTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechOtherReasonRemoveAssociationFailTime.setStatus(_A)
_QtechUserMacAddrTable_Object=MibTable
qtechUserMacAddrTable=_QtechUserMacAddrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,35))
if mibBuilder.loadTexts:qtechUserMacAddrTable.setStatus(_A)
_QtechUserMacAddrEntry_Object=MibTableRow
qtechUserMacAddrEntry=_QtechUserMacAddrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,35,1))
qtechUserMacAddrEntry.setIndexNames((0,_D,_E),(0,_D,_G))
if mibBuilder.loadTexts:qtechUserMacAddrEntry.setStatus(_A)
_QtechTerminalIndex_Type=Integer32
_QtechTerminalIndex_Object=MibTableColumn
qtechTerminalIndex=_QtechTerminalIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,35,1,1),_QtechTerminalIndex_Type())
qtechTerminalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTerminalIndex.setStatus(_A)
_QtechUserMacAdddr_Type=MacAddress
_QtechUserMacAdddr_Object=MibTableColumn
qtechUserMacAdddr=_QtechUserMacAdddr_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,35,1,2),_QtechUserMacAdddr_Type())
qtechUserMacAdddr.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUserMacAdddr.setStatus(_A)
_QtechTermServiceStatTable_Object=MibTable
qtechTermServiceStatTable=_QtechTermServiceStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36))
if mibBuilder.loadTexts:qtechTermServiceStatTable.setStatus(_A)
_QtechTermServiceStatEntry_Object=MibTableRow
qtechTermServiceStatEntry=_QtechTermServiceStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1))
qtechTermServiceStatEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:qtechTermServiceStatEntry.setStatus(_A)
_QtechTotalReTxFramNum_Type=Integer32
_QtechTotalReTxFramNum_Object=MibTableColumn
qtechTotalReTxFramNum=_QtechTotalReTxFramNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,1),_QtechTotalReTxFramNum_Type())
qtechTotalReTxFramNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalReTxFramNum.setStatus(_A)
_QtechUserOnLineTime_Type=Integer32
_QtechUserOnLineTime_Object=MibTableColumn
qtechUserOnLineTime=_QtechUserOnLineTime_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,2),_QtechUserOnLineTime_Type())
qtechUserOnLineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechUserOnLineTime.setStatus(_A)
_QtechRevDataFrameNum_Type=Integer32
_QtechRevDataFrameNum_Object=MibTableColumn
qtechRevDataFrameNum=_QtechRevDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,3),_QtechRevDataFrameNum_Type())
qtechRevDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechRevDataFrameNum.setStatus(_A)
_QtechRevErrorDataFrameNum_Type=Integer32
_QtechRevErrorDataFrameNum_Object=MibTableColumn
qtechRevErrorDataFrameNum=_QtechRevErrorDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,4),_QtechRevErrorDataFrameNum_Type())
qtechRevErrorDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechRevErrorDataFrameNum.setStatus(_A)
_QtechSendDataFrameNum_Type=Integer32
_QtechSendDataFrameNum_Object=MibTableColumn
qtechSendDataFrameNum=_QtechSendDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,5),_QtechSendDataFrameNum_Type())
qtechSendDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSendDataFrameNum.setStatus(_A)
_QtechSendSuccessDataFrameNum_Type=Integer32
_QtechSendSuccessDataFrameNum_Object=MibTableColumn
qtechSendSuccessDataFrameNum=_QtechSendSuccessDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,6),_QtechSendSuccessDataFrameNum_Type())
qtechSendSuccessDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSendSuccessDataFrameNum.setStatus(_A)
_QtechSendReTxDataFrameNum_Type=Integer32
_QtechSendReTxDataFrameNum_Object=MibTableColumn
qtechSendReTxDataFrameNum=_QtechSendReTxDataFrameNum_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,7),_QtechSendReTxDataFrameNum_Type())
qtechSendReTxDataFrameNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSendReTxDataFrameNum.setStatus(_A)
_QtechAvgSendRate_Type=Integer32
_QtechAvgSendRate_Object=MibTableColumn
qtechAvgSendRate=_QtechAvgSendRate_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,8),_QtechAvgSendRate_Type())
qtechAvgSendRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechAvgSendRate.setStatus(_A)
_QtechAvgReceiveRate_Type=Integer32
_QtechAvgReceiveRate_Object=MibTableColumn
qtechAvgReceiveRate=_QtechAvgReceiveRate_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,9),_QtechAvgReceiveRate_Type())
qtechAvgReceiveRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechAvgReceiveRate.setStatus(_A)
_QtechTotalDataThroughput_Type=Integer32
_QtechTotalDataThroughput_Object=MibTableColumn
qtechTotalDataThroughput=_QtechTotalDataThroughput_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,10),_QtechTotalDataThroughput_Type())
qtechTotalDataThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechTotalDataThroughput.setStatus(_A)
_QtechSignalStrength_Type=Integer32
_QtechSignalStrength_Object=MibTableColumn
qtechSignalStrength=_QtechSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,11),_QtechSignalStrength_Type())
qtechSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechSignalStrength.setStatus(_A)
_QtechNoise_Type=Integer32
_QtechNoise_Object=MibTableColumn
qtechNoise=_QtechNoise_Object((1,3,6,1,4,1,27514,1,1,10,2,82,2,2,36,1,12),_QtechNoise_Type())
qtechNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechNoise.setStatus(_A)
qtechRadioPortTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,82,0,1))
if mibBuilder.loadTexts:qtechRadioPortTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'qtechStandardmibmodule':qtechStandardmibmodule,'qtechStandardTraps':qtechStandardTraps,'qtechRadioPortTrap':qtechRadioPortTrap,'qtechConfigInfoObjects':qtechConfigInfoObjects,'qtechSysInfoConfig':qtechSysInfoConfig,'qtechDomain':qtechDomain,'qtechLayer2Isolate':qtechLayer2Isolate,'qtechDosAttackProtect':qtechDosAttackProtect,'qtechVlanConfigTable':qtechVlanConfigTable,'qtechVlanConfigEntry':qtechVlanConfigEntry,'qtechVlanId':qtechVlanId,'qtechSSID':qtechSSID,'qtechRadioInfoConfig':qtechRadioInfoConfig,'qtechRadioConfigTable':qtechRadioConfigTable,'qtechRadioConfigEntry':qtechRadioConfigEntry,'qtechSSIDNum':qtechSSIDNum,'qtechRadioSecurityMch':qtechRadioSecurityMch,'qtechRadioSecurityParam':qtechRadioSecurityParam,'qtechRadioQos':qtechRadioQos,'qtechRtsCtsThreshold':qtechRtsCtsThreshold,'qtechMaxUserPermit':qtechMaxUserPermit,'qtechUserNumOnLine':qtechUserNumOnLine,'qtechAirInterfaceType':qtechAirInterfaceType,'qtechChannelMode':qtechChannelMode,'qtechCurrentChannel':qtechCurrentChannel,'qtechSNR':qtechSNR,'qtechHoppingTimes':qtechHoppingTimes,'qtechHopDetectItvTime':qtechHopDetectItvTime,'qtechPowerMgr':qtechPowerMgr,'qtechTxPower':qtechTxPower,'qtechWapiConfig':qtechWapiConfig,'qtechWapiConfigTable':qtechWapiConfigTable,'qtechWapiConfigEntry':qtechWapiConfigEntry,_E:qtechWlanId,'qtechTrustASCfg':qtechTrustASCfg,'qtechCertType':qtechCertType,'qtechCertState':qtechCertState,'qtechCertSetup':qtechCertSetup,'qtechAdminInfoConfig':qtechAdminInfoConfig,'qtechAdminName':qtechAdminName,'qtechAdminPwd':qtechAdminPwd,'qtechPollTimeConfig':qtechPollTimeConfig,'qtechPollTimeOfLast':qtechPollTimeOfLast,'qtechPerformanceStatObjects':qtechPerformanceStatObjects,'qtechAirIfServiceStat':qtechAirIfServiceStat,'qtechUplinkTotalDataFrameNum':qtechUplinkTotalDataFrameNum,'qtechDownlinkTotalDataFrameNum':qtechDownlinkTotalDataFrameNum,'qtechDownlinkTotalLostDataFrameNum':qtechDownlinkTotalLostDataFrameNum,'qtechTotalSignalFrameNum':qtechTotalSignalFrameNum,'qtechCorrectPkgByteRxByMAC':qtechCorrectPkgByteRxByMAC,'qtechPkgByteTxByMAC':qtechPkgByteTxByMAC,'qtechUplinkPortFlow':qtechUplinkPortFlow,'qtechDownlinkPortFlow':qtechDownlinkPortFlow,'qtechTermServiceStat':qtechTermServiceStat,'qtechTotalUserNum':qtechTotalUserNum,'qtechUserAccumulateTime':qtechUserAccumulateTime,'qtechTermServiceStatSSIDTable':qtechTermServiceStatSSIDTable,'qtechTermServiceStatSSIDEntry':qtechTermServiceStatSSIDEntry,'qtechCorrectPkgByteRxByMACBySSID':qtechCorrectPkgByteRxByMACBySSID,'qtechPkgByteTxByMACBySSID':qtechPkgByteTxByMACBySSID,'qtechAirIfResUsageRatio':qtechAirIfResUsageRatio,'qtechTotalAssociationUserNum':qtechTotalAssociationUserNum,'qtechOnlineUserNum':qtechOnlineUserNum,'qtechUserReqAccessTimes':qtechUserReqAccessTimes,'qtechResponseReqAccessTimes':qtechResponseReqAccessTimes,'qtechSuccessAccessTimes':qtechSuccessAccessTimes,'qtechIneffiLinkVerifyFailTime':qtechIneffiLinkVerifyFailTime,'qtechTimeoutLinkVerifyFailTime':qtechTimeoutLinkVerifyFailTime,'qtechInefficiencyLinkVerifyFailTime':qtechInefficiencyLinkVerifyFailTime,'qtechOtherReasonLinkVerifyFailTime':qtechOtherReasonLinkVerifyFailTime,'qtechIneffiAssociationFailTime':qtechIneffiAssociationFailTime,'qtechTimeoutAssociationFailTime':qtechTimeoutAssociationFailTime,'qtechInefficiencyAssociationFailTime':qtechInefficiencyAssociationFailTime,'qtechOtherReasonAssociationFailTime':qtechOtherReasonAssociationFailTime,'qtechTotalReassociationAtmptTimes':qtechTotalReassociationAtmptTimes,'qtechTotalReassociationSuccessTimes':qtechTotalReassociationSuccessTimes,'qtechIneffiReassociationFailTime':qtechIneffiReassociationFailTime,'qtechTimeoutReassociationFailTime':qtechTimeoutReassociationFailTime,'qtechInefficiencyReassociationFailTime':qtechInefficiencyReassociationFailTime,'qtechOtherReasonReassociationFailTime':qtechOtherReasonReassociationFailTime,'qtechTotalIdentificationAtmptTimes':qtechTotalIdentificationAtmptTimes,'qtechTotalIdentificationSuccessTimes':qtechTotalIdentificationSuccessTimes,'qtechPwdErrorIdentifyFailTime':qtechPwdErrorIdentifyFailTime,'qtechIneffiIdentificationFailTime':qtechIneffiIdentificationFailTime,'qtechTimeoutIdentificationFailTime':qtechTimeoutIdentificationFailTime,'qtechInefficiencyIdentificationFailTime':qtechInefficiencyIdentificationFailTime,'qtechOtherReasonIdentificationFailTime':qtechOtherReasonIdentificationFailTime,'qtechTotalRemoveLinkVerifyFailTimes':qtechTotalRemoveLinkVerifyFailTimes,'qtechLeaveAPCoverageRemoveLinkVerifyFailTimes':qtechLeaveAPCoverageRemoveLinkVerifyFailTimes,'qtechInefficiencyRemoveLinkVerifyFailTime':qtechInefficiencyRemoveLinkVerifyFailTime,'qtechLinkVerifyFailRemoveLinkVerifyFailTime':qtechLinkVerifyFailRemoveLinkVerifyFailTime,'qtechOtherReasonRemoveLinkVerifyFailTime':qtechOtherReasonRemoveLinkVerifyFailTime,'qtechTotalRemoveLinkAssociationTimes':qtechTotalRemoveLinkAssociationTimes,'qtechLeaveAPCoverageRemoveAssociationFailTimes':qtechLeaveAPCoverageRemoveAssociationFailTimes,'qtechInefficiencyRemoveAssociationFailTime':qtechInefficiencyRemoveAssociationFailTime,'qtechAssociationFailRemoveAssociationFailTime':qtechAssociationFailRemoveAssociationFailTime,'qtechOtherReasonRemoveAssociationFailTime':qtechOtherReasonRemoveAssociationFailTime,'qtechUserMacAddrTable':qtechUserMacAddrTable,'qtechUserMacAddrEntry':qtechUserMacAddrEntry,_G:qtechTerminalIndex,'qtechUserMacAdddr':qtechUserMacAdddr,'qtechTermServiceStatTable':qtechTermServiceStatTable,'qtechTermServiceStatEntry':qtechTermServiceStatEntry,'qtechTotalReTxFramNum':qtechTotalReTxFramNum,'qtechUserOnLineTime':qtechUserOnLineTime,'qtechRevDataFrameNum':qtechRevDataFrameNum,'qtechRevErrorDataFrameNum':qtechRevErrorDataFrameNum,'qtechSendDataFrameNum':qtechSendDataFrameNum,'qtechSendSuccessDataFrameNum':qtechSendSuccessDataFrameNum,'qtechSendReTxDataFrameNum':qtechSendReTxDataFrameNum,'qtechAvgSendRate':qtechAvgSendRate,'qtechAvgReceiveRate':qtechAvgReceiveRate,'qtechTotalDataThroughput':qtechTotalDataThroughput,'qtechSignalStrength':qtechSignalStrength,'qtechNoise':qtechNoise})