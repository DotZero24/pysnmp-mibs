_s='schCtpGroup'
_r='schCtpPassBandStatusList'
_q='schCtpPassBandList'
_p='schCtpCarrierList'
_o='schCtpFlexOptChnlList'
_n='schCtpRxSchPowerOffset'
_m='schCtpAssocTeIntfList'
_l='schCtpOpticalSignal'
_k='schCtpSupportingCarrGrpList'
_j='schCtpSupportingCarrierList'
_i='schCtpFreqSlotList'
_h='schCtpIntraSchCarRipple'
_g='schCtpShutterState'
_f='schCtpIntraSchCarrierRippleThreshold'
_e='schCtpTargetOpr'
_d='schCtpMonitoringMode'
_c='schCtpRecievedTTI'
_b='schCtpTransmitTTI'
_a='schCtpExpectedTTI'
_Z='schCtpPowerOffset'
_Y='schCtpAssociatedClientSCHCTP'
_X='schCtpSupportingCircuitIdList'
_W='schCtpOffsetOverride'
_V='schCtpOffset'
_U='schCtpInstalledSuperChannelNum'
_T='schCtpFrequencySlotPlanType'
_S='schCtpChannelPlanType'
_R='schCtpInstalledEncoding'
_Q='schCtpInstalledModulation'
_P='schCtpCarrierGroupMode'
_O='schCtpAggregrateRate'
_N='schCtpSpectralBandWidth'
_M='schCtpProvEncoding'
_L='schCtpProvModulation'
_K='schCtpProvSuperChannelNum'
_J='schCtpPmHistStatsEnable'
_I='read-create'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='schCtpProvBaudRate'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-SCHCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,FloatHundredths,FloatTenths,InfnCarrierType,InfnChannelPlanType,InfnEnableDisable,InfnEncoding,InfnFrequencySlotPlanType,InfnModulation,InfnMonitoringMode,InfnOpticalRate,InfnOpticalSignal,InfnProvBaudRate,InfnReporting,InfnShutterState,InfnSuperChannelNumber,InfnTimReptMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','FloatTenths','InfnCarrierType','InfnChannelPlanType','InfnEnableDisable','InfnEncoding','InfnFrequencySlotPlanType','InfnModulation','InfnMonitoringMode','InfnOpticalRate','InfnOpticalSignal','InfnProvBaudRate','InfnReporting','InfnShutterState','InfnSuperChannelNumber','InfnTimReptMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
schCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,50))
if mibBuilder.loadTexts:schCtpMIB.setRevisions(('2013-09-05 00:00',))
_SchCtpTable_Object=MibTable
schCtpTable=_SchCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1))
if mibBuilder.loadTexts:schCtpTable.setStatus(_A)
_SchCtpEntry_Object=MibTableRow
schCtpEntry=_SchCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1))
schCtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:schCtpEntry.setStatus(_A)
_SchCtpCarrierGroupMode_Type=InfnCarrierType
_SchCtpCarrierGroupMode_Object=MibTableColumn
schCtpCarrierGroupMode=_SchCtpCarrierGroupMode_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,1),_SchCtpCarrierGroupMode_Type())
schCtpCarrierGroupMode.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpCarrierGroupMode.setStatus(_A)
_SchCtpAssociatedClientSCHCTP_Type=DisplayString
_SchCtpAssociatedClientSCHCTP_Object=MibTableColumn
schCtpAssociatedClientSCHCTP=_SchCtpAssociatedClientSCHCTP_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,2),_SchCtpAssociatedClientSCHCTP_Type())
schCtpAssociatedClientSCHCTP.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpAssociatedClientSCHCTP.setStatus(_A)
class _SchCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SchCtpPmHistStatsEnable_Type.__name__=_H
_SchCtpPmHistStatsEnable_Object=MibTableColumn
schCtpPmHistStatsEnable=_SchCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,3),_SchCtpPmHistStatsEnable_Type())
schCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpPmHistStatsEnable.setStatus(_A)
_SchCtpProvSuperChannelNum_Type=InfnSuperChannelNumber
_SchCtpProvSuperChannelNum_Object=MibTableColumn
schCtpProvSuperChannelNum=_SchCtpProvSuperChannelNum_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,4),_SchCtpProvSuperChannelNum_Type())
schCtpProvSuperChannelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpProvSuperChannelNum.setStatus(_A)
_SchCtpProvModulation_Type=InfnModulation
_SchCtpProvModulation_Object=MibTableColumn
schCtpProvModulation=_SchCtpProvModulation_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,5),_SchCtpProvModulation_Type())
schCtpProvModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpProvModulation.setStatus(_A)
_SchCtpProvEncoding_Type=InfnEncoding
_SchCtpProvEncoding_Object=MibTableColumn
schCtpProvEncoding=_SchCtpProvEncoding_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,6),_SchCtpProvEncoding_Type())
schCtpProvEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpProvEncoding.setStatus(_A)
_SchCtpSpectralBandWidth_Type=Integer32
_SchCtpSpectralBandWidth_Object=MibTableColumn
schCtpSpectralBandWidth=_SchCtpSpectralBandWidth_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,7),_SchCtpSpectralBandWidth_Type())
schCtpSpectralBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpSpectralBandWidth.setStatus(_A)
_SchCtpAggregrateRate_Type=InfnOpticalRate
_SchCtpAggregrateRate_Object=MibTableColumn
schCtpAggregrateRate=_SchCtpAggregrateRate_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,8),_SchCtpAggregrateRate_Type())
schCtpAggregrateRate.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpAggregrateRate.setStatus(_A)
_SchCtpChannelPlanType_Type=InfnChannelPlanType
_SchCtpChannelPlanType_Object=MibTableColumn
schCtpChannelPlanType=_SchCtpChannelPlanType_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,9),_SchCtpChannelPlanType_Type())
schCtpChannelPlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpChannelPlanType.setStatus(_A)
_SchCtpFrequencySlotPlanType_Type=InfnFrequencySlotPlanType
_SchCtpFrequencySlotPlanType_Object=MibTableColumn
schCtpFrequencySlotPlanType=_SchCtpFrequencySlotPlanType_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,10),_SchCtpFrequencySlotPlanType_Type())
schCtpFrequencySlotPlanType.setMaxAccess(_I)
if mibBuilder.loadTexts:schCtpFrequencySlotPlanType.setStatus(_A)
_SchCtpInstalledSuperChannelNum_Type=InfnSuperChannelNumber
_SchCtpInstalledSuperChannelNum_Object=MibTableColumn
schCtpInstalledSuperChannelNum=_SchCtpInstalledSuperChannelNum_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,11),_SchCtpInstalledSuperChannelNum_Type())
schCtpInstalledSuperChannelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpInstalledSuperChannelNum.setStatus(_A)
_SchCtpInstalledModulation_Type=InfnModulation
_SchCtpInstalledModulation_Object=MibTableColumn
schCtpInstalledModulation=_SchCtpInstalledModulation_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,12),_SchCtpInstalledModulation_Type())
schCtpInstalledModulation.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpInstalledModulation.setStatus(_A)
_SchCtpInstalledEncoding_Type=InfnEncoding
_SchCtpInstalledEncoding_Object=MibTableColumn
schCtpInstalledEncoding=_SchCtpInstalledEncoding_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,13),_SchCtpInstalledEncoding_Type())
schCtpInstalledEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpInstalledEncoding.setStatus(_A)
_SchCtpOffset_Type=FloatHundredths
_SchCtpOffset_Object=MibTableColumn
schCtpOffset=_SchCtpOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,14),_SchCtpOffset_Type())
schCtpOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpOffset.setStatus(_A)
_SchCtpOffsetOverride_Type=InfnEnableDisable
_SchCtpOffsetOverride_Object=MibTableColumn
schCtpOffsetOverride=_SchCtpOffsetOverride_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,15),_SchCtpOffsetOverride_Type())
schCtpOffsetOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpOffsetOverride.setStatus(_A)
_SchCtpPowerOffset_Type=FloatArbitraryPrecision
_SchCtpPowerOffset_Object=MibTableColumn
schCtpPowerOffset=_SchCtpPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,16),_SchCtpPowerOffset_Type())
schCtpPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpPowerOffset.setStatus(_A)
_SchCtpSupportingCircuitIdList_Type=DisplayString
_SchCtpSupportingCircuitIdList_Object=MibTableColumn
schCtpSupportingCircuitIdList=_SchCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,17),_SchCtpSupportingCircuitIdList_Type())
schCtpSupportingCircuitIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpSupportingCircuitIdList.setStatus(_A)
_SchCtpExpectedTTI_Type=DisplayString
_SchCtpExpectedTTI_Object=MibTableColumn
schCtpExpectedTTI=_SchCtpExpectedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,18),_SchCtpExpectedTTI_Type())
schCtpExpectedTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpExpectedTTI.setStatus(_A)
_SchCtpTransmitTTI_Type=DisplayString
_SchCtpTransmitTTI_Object=MibTableColumn
schCtpTransmitTTI=_SchCtpTransmitTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,19),_SchCtpTransmitTTI_Type())
schCtpTransmitTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpTransmitTTI.setStatus(_A)
_SchCtpRecievedTTI_Type=DisplayString
_SchCtpRecievedTTI_Object=MibTableColumn
schCtpRecievedTTI=_SchCtpRecievedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,20),_SchCtpRecievedTTI_Type())
schCtpRecievedTTI.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpRecievedTTI.setStatus(_A)
_SchCtpMonitoringMode_Type=InfnMonitoringMode
_SchCtpMonitoringMode_Object=MibTableColumn
schCtpMonitoringMode=_SchCtpMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,21),_SchCtpMonitoringMode_Type())
schCtpMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpMonitoringMode.setStatus(_A)
_SchCtpTargetOpr_Type=FloatTenths
_SchCtpTargetOpr_Object=MibTableColumn
schCtpTargetOpr=_SchCtpTargetOpr_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,22),_SchCtpTargetOpr_Type())
schCtpTargetOpr.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpTargetOpr.setStatus(_A)
_SchCtpIntraSchCarrierRippleThreshold_Type=FloatTenths
_SchCtpIntraSchCarrierRippleThreshold_Object=MibTableColumn
schCtpIntraSchCarrierRippleThreshold=_SchCtpIntraSchCarrierRippleThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,23),_SchCtpIntraSchCarrierRippleThreshold_Type())
schCtpIntraSchCarrierRippleThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpIntraSchCarrierRippleThreshold.setStatus(_A)
_SchCtpShutterState_Type=InfnShutterState
_SchCtpShutterState_Object=MibTableColumn
schCtpShutterState=_SchCtpShutterState_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,24),_SchCtpShutterState_Type())
schCtpShutterState.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpShutterState.setStatus(_A)
_SchCtpIntraSchCarRipple_Type=InfnReporting
_SchCtpIntraSchCarRipple_Object=MibTableColumn
schCtpIntraSchCarRipple=_SchCtpIntraSchCarRipple_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,25),_SchCtpIntraSchCarRipple_Type())
schCtpIntraSchCarRipple.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpIntraSchCarRipple.setStatus(_A)
_SchCtpFreqSlotList_Type=DisplayString
_SchCtpFreqSlotList_Object=MibTableColumn
schCtpFreqSlotList=_SchCtpFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,26),_SchCtpFreqSlotList_Type())
schCtpFreqSlotList.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpFreqSlotList.setStatus(_A)
_SchCtpSupportingCarrierList_Type=DisplayString
_SchCtpSupportingCarrierList_Object=MibTableColumn
schCtpSupportingCarrierList=_SchCtpSupportingCarrierList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,27),_SchCtpSupportingCarrierList_Type())
schCtpSupportingCarrierList.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpSupportingCarrierList.setStatus(_A)
_SchCtpProvBaudRate_Type=InfnProvBaudRate
_SchCtpProvBaudRate_Object=MibTableColumn
schCtpProvBaudRate=_SchCtpProvBaudRate_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,28),_SchCtpProvBaudRate_Type())
schCtpProvBaudRate.setMaxAccess(_I)
if mibBuilder.loadTexts:schCtpProvBaudRate.setStatus(_A)
_SchCtpSupportingCarrGrpList_Type=DisplayString
_SchCtpSupportingCarrGrpList_Object=MibTableColumn
schCtpSupportingCarrGrpList=_SchCtpSupportingCarrGrpList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,29),_SchCtpSupportingCarrGrpList_Type())
schCtpSupportingCarrGrpList.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpSupportingCarrGrpList.setStatus(_A)
_SchCtpOpticalSignal_Type=InfnOpticalSignal
_SchCtpOpticalSignal_Object=MibTableColumn
schCtpOpticalSignal=_SchCtpOpticalSignal_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,30),_SchCtpOpticalSignal_Type())
schCtpOpticalSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpOpticalSignal.setStatus(_A)
_SchCtpAssocTeIntfList_Type=DisplayString
_SchCtpAssocTeIntfList_Object=MibTableColumn
schCtpAssocTeIntfList=_SchCtpAssocTeIntfList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,31),_SchCtpAssocTeIntfList_Type())
schCtpAssocTeIntfList.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpAssocTeIntfList.setStatus(_A)
_SchCtpRxSchPowerOffset_Type=FloatArbitraryPrecision
_SchCtpRxSchPowerOffset_Object=MibTableColumn
schCtpRxSchPowerOffset=_SchCtpRxSchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,32),_SchCtpRxSchPowerOffset_Type())
schCtpRxSchPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpRxSchPowerOffset.setStatus(_A)
_SchCtpFlexOptChnlList_Type=DisplayString
_SchCtpFlexOptChnlList_Object=MibTableColumn
schCtpFlexOptChnlList=_SchCtpFlexOptChnlList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,33),_SchCtpFlexOptChnlList_Type())
schCtpFlexOptChnlList.setMaxAccess(_D)
if mibBuilder.loadTexts:schCtpFlexOptChnlList.setStatus(_A)
_SchCtpCarrierList_Type=DisplayString
_SchCtpCarrierList_Object=MibTableColumn
schCtpCarrierList=_SchCtpCarrierList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,34),_SchCtpCarrierList_Type())
schCtpCarrierList.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpCarrierList.setStatus(_A)
_SchCtpPassBandList_Type=DisplayString
_SchCtpPassBandList_Object=MibTableColumn
schCtpPassBandList=_SchCtpPassBandList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,35),_SchCtpPassBandList_Type())
schCtpPassBandList.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpPassBandList.setStatus(_A)
_SchCtpPassBandStatusList_Type=DisplayString
_SchCtpPassBandStatusList_Object=MibTableColumn
schCtpPassBandStatusList=_SchCtpPassBandStatusList_Object((1,3,6,1,4,1,21296,2,2,2,2,50,1,1,36),_SchCtpPassBandStatusList_Type())
schCtpPassBandStatusList.setMaxAccess(_C)
if mibBuilder.loadTexts:schCtpPassBandStatusList.setStatus(_A)
_SchCtpConformance_ObjectIdentity=ObjectIdentity
schCtpConformance=_SchCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,50,3))
_SchCtpCompliances_ObjectIdentity=ObjectIdentity
schCtpCompliances=_SchCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,50,3,1))
_SchCtpGroups_ObjectIdentity=ObjectIdentity
schCtpGroups=_SchCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,50,3,2))
schCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,50,3,2,1))
schCtpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_E),(_B,_k),(_B,_E),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:schCtpGroup.setStatus(_A)
schCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,50,3,1,1))
schCtpCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:schCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'schCtpMIB':schCtpMIB,'schCtpTable':schCtpTable,'schCtpEntry':schCtpEntry,_P:schCtpCarrierGroupMode,_Y:schCtpAssociatedClientSCHCTP,_J:schCtpPmHistStatsEnable,_K:schCtpProvSuperChannelNum,_L:schCtpProvModulation,_M:schCtpProvEncoding,_N:schCtpSpectralBandWidth,_O:schCtpAggregrateRate,_S:schCtpChannelPlanType,_T:schCtpFrequencySlotPlanType,_U:schCtpInstalledSuperChannelNum,_Q:schCtpInstalledModulation,_R:schCtpInstalledEncoding,_V:schCtpOffset,_W:schCtpOffsetOverride,_Z:schCtpPowerOffset,_X:schCtpSupportingCircuitIdList,_a:schCtpExpectedTTI,_b:schCtpTransmitTTI,_c:schCtpRecievedTTI,_d:schCtpMonitoringMode,_e:schCtpTargetOpr,_f:schCtpIntraSchCarrierRippleThreshold,_g:schCtpShutterState,_h:schCtpIntraSchCarRipple,_i:schCtpFreqSlotList,_j:schCtpSupportingCarrierList,_E:schCtpProvBaudRate,_k:schCtpSupportingCarrGrpList,_l:schCtpOpticalSignal,_m:schCtpAssocTeIntfList,_n:schCtpRxSchPowerOffset,_o:schCtpFlexOptChnlList,_p:schCtpCarrierList,_q:schCtpPassBandList,_r:schCtpPassBandStatusList,'schCtpConformance':schCtpConformance,'schCtpCompliances':schCtpCompliances,'schCtpCompliance':schCtpCompliance,'schCtpGroups':schCtpGroups,_s:schCtpGroup})