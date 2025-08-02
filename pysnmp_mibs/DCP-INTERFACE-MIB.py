_AG='dcpInterfaceTrxTableGroupV2'
_AF='dcpInterfaceTrxTableGroupV1'
_AE='dcpInterfaceTableGroupV2'
_AD='dcpInterfaceTableGroupV1'
_AC='dcpInterfaceTrxLanesTxBias'
_AB='dcpInterfaceTrxLanesRxSensitivity'
_AA='dcpInterfaceTrxLanesTxPower'
_A9='dcpInterfaceTrxLanesRxPower'
_A8='dcpInterfaceTrxLanesName'
_A7='dcpInterfaceTrxStateOfPolarizationROC'
_A6='dcpInterfacePortMode'
_A5='dcpInterfacePortType'
_A4='dcpInterfaceTrxLanesIndex'
_A3='dcpInterfaceTrxIndex'
_A2='dcpInterfaceIndex'
_A1='dcpInterfaceTrxLanesTableGroupV1'
_A0='dcpInterfaceTrxQmargin'
_z='dcpInterfaceTrxQvalue'
_y='dcpInterfaceTrxPostFecBerExponent'
_x='dcpInterfaceTrxPostFecBerMantissa'
_w='dcpInterfaceTrxUncorrectedBerExponent'
_v='dcpInterfaceTrxUncorrectedBerMantissa'
_u='dcpInterfaceTrxPreFecBerAvgExponent'
_t='dcpInterfaceTrxPreFecBerAvgMantissa'
_s='dcpInterfaceTrxPreFecBerExponent'
_r='dcpInterfaceTrxPreFecBerMantissa'
_q='dcpInterfaceTrxPolarizationDependentLoss'
_p='dcpInterfaceTrxDiffGroupDelay'
_o='dcpInterfaceTrxChromaticDispersion'
_n='dcpInterfaceTrxOsnr'
_m='dcpInterfaceTrxCertified'
_l='dcpInterfaceTrxPulseShaping'
_k='dcpInterfaceTrxFec'
_j='dcpInterfaceTrxBandwidth'
_i='dcpInterfaceTrxModulationType'
_h='dcpInterfaceTrxRxLosThreshold'
_g='dcpInterfaceTrxRxSensitivity'
_f='dcpInterfaceTrxTxBias'
_e='dcpInterfaceTrxTxPower'
_d='dcpInterfaceTrxSignalRxPower'
_c='dcpInterfaceTrxTotalRxPower'
_b='dcpInterfaceTrxGridSpacing'
_a='dcpInterfaceTrxWantedFrequency'
_Z='dcpInterfaceTrxActualFrequency'
_Y='dcpInterfaceTrxChannelId'
_X='dcpInterfaceTrxWavelength'
_W='dcpInterfaceTrxTemperatureHighAlarmThreshold'
_V='dcpInterfaceTrxTemperatureHighWarningThreshold'
_U='dcpInterfaceTrxTemperature'
_T='dcpInterfaceTrxLanes'
_S='dcpInterfaceDescription'
_R='deprecated'
_Q='not-accessible'
_P='DisplayString'
_O='dcpInterfaceTableGroupV3'
_N='dcpInterfaceWavelength'
_M='dcpInterfaceChannelId'
_L='dcpInterfaceFormat'
_K='dcpInterfaceAlarm'
_J='dcpInterfaceStatus'
_I='dcpInterfaceTxPower'
_H='dcpInterfaceRxPower'
_G='dcpInterfaceName'
_F='Unsigned32'
_E='dcpInterfaceTrxName'
_D='Integer32'
_C='read-only'
_B='current'
_A='DCP-INTERFACE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dcpGeneric,=mibBuilder.importSymbols('DCP-MIB','dcpGeneric')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention')
InterfacePortMode,InterfaceStatus,ItuPerceivedSeverity,OpticalPower1Decimal=mibBuilder.importSymbols('SO-TC-MIB','InterfacePortMode','InterfaceStatus','ItuPerceivedSeverity','OpticalPower1Decimal')
dcpInterface=ModuleIdentity((1,3,6,1,4,1,30826,2,2,1))
if mibBuilder.loadTexts:dcpInterface.setRevisions(('2023-07-03 04:00','2023-07-01 10:00','2022-12-16 12:00','2022-03-18 13:00','2021-02-25 12:00','2019-10-29 15:00','2018-10-08 14:44'))
_DcpInterfaceObjects_ObjectIdentity=ObjectIdentity
dcpInterfaceObjects=_DcpInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,1))
_DcpInterfaceTable_Object=MibTable
dcpInterfaceTable=_DcpInterfaceTable_Object((1,3,6,1,4,1,30826,2,2,1,1,1))
if mibBuilder.loadTexts:dcpInterfaceTable.setStatus(_B)
_DcpInterfaceEntry_Object=MibTableRow
dcpInterfaceEntry=_DcpInterfaceEntry_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1))
dcpInterfaceEntry.setIndexNames((0,_A,_A2))
if mibBuilder.loadTexts:dcpInterfaceEntry.setStatus(_B)
class _DcpInterfaceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpInterfaceIndex_Type.__name__=_F
_DcpInterfaceIndex_Object=MibTableColumn
dcpInterfaceIndex=_DcpInterfaceIndex_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,1),_DcpInterfaceIndex_Type())
dcpInterfaceIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:dcpInterfaceIndex.setStatus(_B)
_DcpInterfaceName_Type=DisplayString
_DcpInterfaceName_Object=MibTableColumn
dcpInterfaceName=_DcpInterfaceName_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,2),_DcpInterfaceName_Type())
dcpInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceName.setStatus(_B)
_DcpInterfaceRxPower_Type=OpticalPower1Decimal
_DcpInterfaceRxPower_Object=MibTableColumn
dcpInterfaceRxPower=_DcpInterfaceRxPower_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,3),_DcpInterfaceRxPower_Type())
dcpInterfaceRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceRxPower.setStatus(_B)
_DcpInterfaceTxPower_Type=OpticalPower1Decimal
_DcpInterfaceTxPower_Object=MibTableColumn
dcpInterfaceTxPower=_DcpInterfaceTxPower_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,4),_DcpInterfaceTxPower_Type())
dcpInterfaceTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTxPower.setStatus(_B)
_DcpInterfaceStatus_Type=InterfaceStatus
_DcpInterfaceStatus_Object=MibTableColumn
dcpInterfaceStatus=_DcpInterfaceStatus_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,5),_DcpInterfaceStatus_Type())
dcpInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceStatus.setStatus(_B)
_DcpInterfaceAlarm_Type=ItuPerceivedSeverity
_DcpInterfaceAlarm_Object=MibTableColumn
dcpInterfaceAlarm=_DcpInterfaceAlarm_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,6),_DcpInterfaceAlarm_Type())
dcpInterfaceAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceAlarm.setStatus(_B)
_DcpInterfaceFormat_Type=DisplayString
_DcpInterfaceFormat_Object=MibTableColumn
dcpInterfaceFormat=_DcpInterfaceFormat_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,7),_DcpInterfaceFormat_Type())
dcpInterfaceFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceFormat.setStatus(_B)
_DcpInterfaceWavelength_Type=DisplayString
_DcpInterfaceWavelength_Object=MibTableColumn
dcpInterfaceWavelength=_DcpInterfaceWavelength_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,8),_DcpInterfaceWavelength_Type())
dcpInterfaceWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceWavelength.setStatus(_B)
_DcpInterfaceChannelId_Type=DisplayString
_DcpInterfaceChannelId_Object=MibTableColumn
dcpInterfaceChannelId=_DcpInterfaceChannelId_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,9),_DcpInterfaceChannelId_Type())
dcpInterfaceChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceChannelId.setStatus(_B)
class _DcpInterfaceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DcpInterfaceDescription_Type.__name__=_P
_DcpInterfaceDescription_Object=MibTableColumn
dcpInterfaceDescription=_DcpInterfaceDescription_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,10),_DcpInterfaceDescription_Type())
dcpInterfaceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceDescription.setStatus(_B)
class _DcpInterfacePortType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DcpInterfacePortType_Type.__name__=_P
_DcpInterfacePortType_Object=MibTableColumn
dcpInterfacePortType=_DcpInterfacePortType_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,11),_DcpInterfacePortType_Type())
dcpInterfacePortType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfacePortType.setStatus(_B)
_DcpInterfacePortMode_Type=InterfacePortMode
_DcpInterfacePortMode_Object=MibTableColumn
dcpInterfacePortMode=_DcpInterfacePortMode_Object((1,3,6,1,4,1,30826,2,2,1,1,1,1,12),_DcpInterfacePortMode_Type())
dcpInterfacePortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfacePortMode.setStatus(_B)
_DcpInterfaceMIBCompliance_ObjectIdentity=ObjectIdentity
dcpInterfaceMIBCompliance=_DcpInterfaceMIBCompliance_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,2))
_DcpInterfaceMIBGroups_ObjectIdentity=ObjectIdentity
dcpInterfaceMIBGroups=_DcpInterfaceMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,2,1))
_DcpInterfaceMIBCompliances_ObjectIdentity=ObjectIdentity
dcpInterfaceMIBCompliances=_DcpInterfaceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,2,2))
_DcpInterfaceTrxMIBGroups_ObjectIdentity=ObjectIdentity
dcpInterfaceTrxMIBGroups=_DcpInterfaceTrxMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,2,3))
_DcpInterfaceTrxLanesMIBGroups_ObjectIdentity=ObjectIdentity
dcpInterfaceTrxLanesMIBGroups=_DcpInterfaceTrxLanesMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,2,4))
_DcpInterfaceTrxObjects_ObjectIdentity=ObjectIdentity
dcpInterfaceTrxObjects=_DcpInterfaceTrxObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,3))
_DcpInterfaceTrxTable_Object=MibTable
dcpInterfaceTrxTable=_DcpInterfaceTrxTable_Object((1,3,6,1,4,1,30826,2,2,1,3,1))
if mibBuilder.loadTexts:dcpInterfaceTrxTable.setStatus(_B)
_DcpInterfaceTrxEntry_Object=MibTableRow
dcpInterfaceTrxEntry=_DcpInterfaceTrxEntry_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1))
dcpInterfaceTrxEntry.setIndexNames((0,_A,_A3))
if mibBuilder.loadTexts:dcpInterfaceTrxEntry.setStatus(_B)
class _DcpInterfaceTrxIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpInterfaceTrxIndex_Type.__name__=_F
_DcpInterfaceTrxIndex_Object=MibTableColumn
dcpInterfaceTrxIndex=_DcpInterfaceTrxIndex_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,1),_DcpInterfaceTrxIndex_Type())
dcpInterfaceTrxIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:dcpInterfaceTrxIndex.setStatus(_B)
_DcpInterfaceTrxName_Type=DisplayString
_DcpInterfaceTrxName_Object=MibTableColumn
dcpInterfaceTrxName=_DcpInterfaceTrxName_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,2),_DcpInterfaceTrxName_Type())
dcpInterfaceTrxName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxName.setStatus(_B)
_DcpInterfaceTrxLanes_Type=Unsigned32
_DcpInterfaceTrxLanes_Object=MibTableColumn
dcpInterfaceTrxLanes=_DcpInterfaceTrxLanes_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,3),_DcpInterfaceTrxLanes_Type())
dcpInterfaceTrxLanes.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxLanes.setStatus(_B)
_DcpInterfaceTrxTemperature_Type=OpticalPower1Decimal
_DcpInterfaceTrxTemperature_Object=MibTableColumn
dcpInterfaceTrxTemperature=_DcpInterfaceTrxTemperature_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,4),_DcpInterfaceTrxTemperature_Type())
dcpInterfaceTrxTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxTemperature.setStatus(_B)
_DcpInterfaceTrxTemperatureHighWarningThreshold_Type=OpticalPower1Decimal
_DcpInterfaceTrxTemperatureHighWarningThreshold_Object=MibTableColumn
dcpInterfaceTrxTemperatureHighWarningThreshold=_DcpInterfaceTrxTemperatureHighWarningThreshold_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,5),_DcpInterfaceTrxTemperatureHighWarningThreshold_Type())
dcpInterfaceTrxTemperatureHighWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxTemperatureHighWarningThreshold.setStatus(_B)
_DcpInterfaceTrxTemperatureHighAlarmThreshold_Type=OpticalPower1Decimal
_DcpInterfaceTrxTemperatureHighAlarmThreshold_Object=MibTableColumn
dcpInterfaceTrxTemperatureHighAlarmThreshold=_DcpInterfaceTrxTemperatureHighAlarmThreshold_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,6),_DcpInterfaceTrxTemperatureHighAlarmThreshold_Type())
dcpInterfaceTrxTemperatureHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxTemperatureHighAlarmThreshold.setStatus(_B)
_DcpInterfaceTrxWavelength_Type=DisplayString
_DcpInterfaceTrxWavelength_Object=MibTableColumn
dcpInterfaceTrxWavelength=_DcpInterfaceTrxWavelength_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,7),_DcpInterfaceTrxWavelength_Type())
dcpInterfaceTrxWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxWavelength.setStatus(_B)
_DcpInterfaceTrxChannelId_Type=DisplayString
_DcpInterfaceTrxChannelId_Object=MibTableColumn
dcpInterfaceTrxChannelId=_DcpInterfaceTrxChannelId_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,8),_DcpInterfaceTrxChannelId_Type())
dcpInterfaceTrxChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxChannelId.setStatus(_B)
_DcpInterfaceTrxActualFrequency_Type=OpticalPower1Decimal
_DcpInterfaceTrxActualFrequency_Object=MibTableColumn
dcpInterfaceTrxActualFrequency=_DcpInterfaceTrxActualFrequency_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,9),_DcpInterfaceTrxActualFrequency_Type())
dcpInterfaceTrxActualFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxActualFrequency.setStatus(_B)
_DcpInterfaceTrxWantedFrequency_Type=OpticalPower1Decimal
_DcpInterfaceTrxWantedFrequency_Object=MibTableColumn
dcpInterfaceTrxWantedFrequency=_DcpInterfaceTrxWantedFrequency_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,10),_DcpInterfaceTrxWantedFrequency_Type())
dcpInterfaceTrxWantedFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxWantedFrequency.setStatus(_B)
_DcpInterfaceTrxGridSpacing_Type=OpticalPower1Decimal
_DcpInterfaceTrxGridSpacing_Object=MibTableColumn
dcpInterfaceTrxGridSpacing=_DcpInterfaceTrxGridSpacing_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,11),_DcpInterfaceTrxGridSpacing_Type())
dcpInterfaceTrxGridSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxGridSpacing.setStatus(_B)
_DcpInterfaceTrxTotalRxPower_Type=OpticalPower1Decimal
_DcpInterfaceTrxTotalRxPower_Object=MibTableColumn
dcpInterfaceTrxTotalRxPower=_DcpInterfaceTrxTotalRxPower_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,12),_DcpInterfaceTrxTotalRxPower_Type())
dcpInterfaceTrxTotalRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxTotalRxPower.setStatus(_B)
_DcpInterfaceTrxSignalRxPower_Type=OpticalPower1Decimal
_DcpInterfaceTrxSignalRxPower_Object=MibTableColumn
dcpInterfaceTrxSignalRxPower=_DcpInterfaceTrxSignalRxPower_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,13),_DcpInterfaceTrxSignalRxPower_Type())
dcpInterfaceTrxSignalRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxSignalRxPower.setStatus(_B)
_DcpInterfaceTrxTxPower_Type=OpticalPower1Decimal
_DcpInterfaceTrxTxPower_Object=MibTableColumn
dcpInterfaceTrxTxPower=_DcpInterfaceTrxTxPower_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,14),_DcpInterfaceTrxTxPower_Type())
dcpInterfaceTrxTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxTxPower.setStatus(_B)
_DcpInterfaceTrxTxBias_Type=OpticalPower1Decimal
_DcpInterfaceTrxTxBias_Object=MibTableColumn
dcpInterfaceTrxTxBias=_DcpInterfaceTrxTxBias_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,15),_DcpInterfaceTrxTxBias_Type())
dcpInterfaceTrxTxBias.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxTxBias.setStatus(_B)
_DcpInterfaceTrxRxSensitivity_Type=OpticalPower1Decimal
_DcpInterfaceTrxRxSensitivity_Object=MibTableColumn
dcpInterfaceTrxRxSensitivity=_DcpInterfaceTrxRxSensitivity_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,16),_DcpInterfaceTrxRxSensitivity_Type())
dcpInterfaceTrxRxSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxRxSensitivity.setStatus(_B)
_DcpInterfaceTrxRxLosThreshold_Type=OpticalPower1Decimal
_DcpInterfaceTrxRxLosThreshold_Object=MibTableColumn
dcpInterfaceTrxRxLosThreshold=_DcpInterfaceTrxRxLosThreshold_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,17),_DcpInterfaceTrxRxLosThreshold_Type())
dcpInterfaceTrxRxLosThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxRxLosThreshold.setStatus(_B)
_DcpInterfaceTrxModulationType_Type=DisplayString
_DcpInterfaceTrxModulationType_Object=MibTableColumn
dcpInterfaceTrxModulationType=_DcpInterfaceTrxModulationType_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,18),_DcpInterfaceTrxModulationType_Type())
dcpInterfaceTrxModulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxModulationType.setStatus(_B)
_DcpInterfaceTrxBandwidth_Type=Unsigned32
_DcpInterfaceTrxBandwidth_Object=MibTableColumn
dcpInterfaceTrxBandwidth=_DcpInterfaceTrxBandwidth_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,19),_DcpInterfaceTrxBandwidth_Type())
dcpInterfaceTrxBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxBandwidth.setStatus(_B)
_DcpInterfaceTrxFec_Type=DisplayString
_DcpInterfaceTrxFec_Object=MibTableColumn
dcpInterfaceTrxFec=_DcpInterfaceTrxFec_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,20),_DcpInterfaceTrxFec_Type())
dcpInterfaceTrxFec.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxFec.setStatus(_B)
_DcpInterfaceTrxPulseShaping_Type=DisplayString
_DcpInterfaceTrxPulseShaping_Object=MibTableColumn
dcpInterfaceTrxPulseShaping=_DcpInterfaceTrxPulseShaping_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,21),_DcpInterfaceTrxPulseShaping_Type())
dcpInterfaceTrxPulseShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPulseShaping.setStatus(_B)
_DcpInterfaceTrxCertified_Type=DisplayString
_DcpInterfaceTrxCertified_Object=MibTableColumn
dcpInterfaceTrxCertified=_DcpInterfaceTrxCertified_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,22),_DcpInterfaceTrxCertified_Type())
dcpInterfaceTrxCertified.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxCertified.setStatus(_B)
_DcpInterfaceTrxOsnr_Type=OpticalPower1Decimal
_DcpInterfaceTrxOsnr_Object=MibTableColumn
dcpInterfaceTrxOsnr=_DcpInterfaceTrxOsnr_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,23),_DcpInterfaceTrxOsnr_Type())
dcpInterfaceTrxOsnr.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxOsnr.setStatus(_B)
_DcpInterfaceTrxChromaticDispersion_Type=Integer32
_DcpInterfaceTrxChromaticDispersion_Object=MibTableColumn
dcpInterfaceTrxChromaticDispersion=_DcpInterfaceTrxChromaticDispersion_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,24),_DcpInterfaceTrxChromaticDispersion_Type())
dcpInterfaceTrxChromaticDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxChromaticDispersion.setStatus(_B)
_DcpInterfaceTrxDiffGroupDelay_Type=OpticalPower1Decimal
_DcpInterfaceTrxDiffGroupDelay_Object=MibTableColumn
dcpInterfaceTrxDiffGroupDelay=_DcpInterfaceTrxDiffGroupDelay_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,25),_DcpInterfaceTrxDiffGroupDelay_Type())
dcpInterfaceTrxDiffGroupDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxDiffGroupDelay.setStatus(_B)
_DcpInterfaceTrxPolarizationDependentLoss_Type=OpticalPower1Decimal
_DcpInterfaceTrxPolarizationDependentLoss_Object=MibTableColumn
dcpInterfaceTrxPolarizationDependentLoss=_DcpInterfaceTrxPolarizationDependentLoss_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,26),_DcpInterfaceTrxPolarizationDependentLoss_Type())
dcpInterfaceTrxPolarizationDependentLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPolarizationDependentLoss.setStatus(_B)
_DcpInterfaceTrxPreFecBerMantissa_Type=OpticalPower1Decimal
_DcpInterfaceTrxPreFecBerMantissa_Object=MibTableColumn
dcpInterfaceTrxPreFecBerMantissa=_DcpInterfaceTrxPreFecBerMantissa_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,27),_DcpInterfaceTrxPreFecBerMantissa_Type())
dcpInterfaceTrxPreFecBerMantissa.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPreFecBerMantissa.setStatus(_B)
class _DcpInterfaceTrxPreFecBerExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-30,0))
_DcpInterfaceTrxPreFecBerExponent_Type.__name__=_D
_DcpInterfaceTrxPreFecBerExponent_Object=MibTableColumn
dcpInterfaceTrxPreFecBerExponent=_DcpInterfaceTrxPreFecBerExponent_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,28),_DcpInterfaceTrxPreFecBerExponent_Type())
dcpInterfaceTrxPreFecBerExponent.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPreFecBerExponent.setStatus(_B)
_DcpInterfaceTrxPreFecBerAvgMantissa_Type=OpticalPower1Decimal
_DcpInterfaceTrxPreFecBerAvgMantissa_Object=MibTableColumn
dcpInterfaceTrxPreFecBerAvgMantissa=_DcpInterfaceTrxPreFecBerAvgMantissa_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,29),_DcpInterfaceTrxPreFecBerAvgMantissa_Type())
dcpInterfaceTrxPreFecBerAvgMantissa.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPreFecBerAvgMantissa.setStatus(_B)
class _DcpInterfaceTrxPreFecBerAvgExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-30,0))
_DcpInterfaceTrxPreFecBerAvgExponent_Type.__name__=_D
_DcpInterfaceTrxPreFecBerAvgExponent_Object=MibTableColumn
dcpInterfaceTrxPreFecBerAvgExponent=_DcpInterfaceTrxPreFecBerAvgExponent_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,30),_DcpInterfaceTrxPreFecBerAvgExponent_Type())
dcpInterfaceTrxPreFecBerAvgExponent.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPreFecBerAvgExponent.setStatus(_B)
_DcpInterfaceTrxUncorrectedBerMantissa_Type=OpticalPower1Decimal
_DcpInterfaceTrxUncorrectedBerMantissa_Object=MibTableColumn
dcpInterfaceTrxUncorrectedBerMantissa=_DcpInterfaceTrxUncorrectedBerMantissa_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,31),_DcpInterfaceTrxUncorrectedBerMantissa_Type())
dcpInterfaceTrxUncorrectedBerMantissa.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxUncorrectedBerMantissa.setStatus(_B)
class _DcpInterfaceTrxUncorrectedBerExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-30,0))
_DcpInterfaceTrxUncorrectedBerExponent_Type.__name__=_D
_DcpInterfaceTrxUncorrectedBerExponent_Object=MibTableColumn
dcpInterfaceTrxUncorrectedBerExponent=_DcpInterfaceTrxUncorrectedBerExponent_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,32),_DcpInterfaceTrxUncorrectedBerExponent_Type())
dcpInterfaceTrxUncorrectedBerExponent.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxUncorrectedBerExponent.setStatus(_B)
_DcpInterfaceTrxPostFecBerMantissa_Type=OpticalPower1Decimal
_DcpInterfaceTrxPostFecBerMantissa_Object=MibTableColumn
dcpInterfaceTrxPostFecBerMantissa=_DcpInterfaceTrxPostFecBerMantissa_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,33),_DcpInterfaceTrxPostFecBerMantissa_Type())
dcpInterfaceTrxPostFecBerMantissa.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPostFecBerMantissa.setStatus(_B)
class _DcpInterfaceTrxPostFecBerExponent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-30,0))
_DcpInterfaceTrxPostFecBerExponent_Type.__name__=_D
_DcpInterfaceTrxPostFecBerExponent_Object=MibTableColumn
dcpInterfaceTrxPostFecBerExponent=_DcpInterfaceTrxPostFecBerExponent_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,34),_DcpInterfaceTrxPostFecBerExponent_Type())
dcpInterfaceTrxPostFecBerExponent.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxPostFecBerExponent.setStatus(_B)
_DcpInterfaceTrxQvalue_Type=OpticalPower1Decimal
_DcpInterfaceTrxQvalue_Object=MibTableColumn
dcpInterfaceTrxQvalue=_DcpInterfaceTrxQvalue_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,35),_DcpInterfaceTrxQvalue_Type())
dcpInterfaceTrxQvalue.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxQvalue.setStatus(_B)
_DcpInterfaceTrxQmargin_Type=OpticalPower1Decimal
_DcpInterfaceTrxQmargin_Object=MibTableColumn
dcpInterfaceTrxQmargin=_DcpInterfaceTrxQmargin_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,36),_DcpInterfaceTrxQmargin_Type())
dcpInterfaceTrxQmargin.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxQmargin.setStatus(_B)
_DcpInterfaceTrxStateOfPolarizationROC_Type=Unsigned32
_DcpInterfaceTrxStateOfPolarizationROC_Object=MibTableColumn
dcpInterfaceTrxStateOfPolarizationROC=_DcpInterfaceTrxStateOfPolarizationROC_Object((1,3,6,1,4,1,30826,2,2,1,3,1,1,37),_DcpInterfaceTrxStateOfPolarizationROC_Type())
dcpInterfaceTrxStateOfPolarizationROC.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxStateOfPolarizationROC.setStatus(_B)
_DcpInterfaceTrxLanesObjects_ObjectIdentity=ObjectIdentity
dcpInterfaceTrxLanesObjects=_DcpInterfaceTrxLanesObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,1,4))
_DcpInterfaceTrxLanesTable_Object=MibTable
dcpInterfaceTrxLanesTable=_DcpInterfaceTrxLanesTable_Object((1,3,6,1,4,1,30826,2,2,1,4,1))
if mibBuilder.loadTexts:dcpInterfaceTrxLanesTable.setStatus(_B)
_DcpInterfaceTrxLanesEntry_Object=MibTableRow
dcpInterfaceTrxLanesEntry=_DcpInterfaceTrxLanesEntry_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1))
dcpInterfaceTrxLanesEntry.setIndexNames((0,_A,_A4))
if mibBuilder.loadTexts:dcpInterfaceTrxLanesEntry.setStatus(_B)
class _DcpInterfaceTrxLanesIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpInterfaceTrxLanesIndex_Type.__name__=_F
_DcpInterfaceTrxLanesIndex_Object=MibTableColumn
dcpInterfaceTrxLanesIndex=_DcpInterfaceTrxLanesIndex_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1,1),_DcpInterfaceTrxLanesIndex_Type())
dcpInterfaceTrxLanesIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:dcpInterfaceTrxLanesIndex.setStatus(_B)
_DcpInterfaceTrxLanesName_Type=DisplayString
_DcpInterfaceTrxLanesName_Object=MibTableColumn
dcpInterfaceTrxLanesName=_DcpInterfaceTrxLanesName_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1,2),_DcpInterfaceTrxLanesName_Type())
dcpInterfaceTrxLanesName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxLanesName.setStatus(_B)
_DcpInterfaceTrxLanesRxPower_Type=OpticalPower1Decimal
_DcpInterfaceTrxLanesRxPower_Object=MibTableColumn
dcpInterfaceTrxLanesRxPower=_DcpInterfaceTrxLanesRxPower_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1,3),_DcpInterfaceTrxLanesRxPower_Type())
dcpInterfaceTrxLanesRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxLanesRxPower.setStatus(_B)
_DcpInterfaceTrxLanesTxPower_Type=OpticalPower1Decimal
_DcpInterfaceTrxLanesTxPower_Object=MibTableColumn
dcpInterfaceTrxLanesTxPower=_DcpInterfaceTrxLanesTxPower_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1,4),_DcpInterfaceTrxLanesTxPower_Type())
dcpInterfaceTrxLanesTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxLanesTxPower.setStatus(_B)
_DcpInterfaceTrxLanesRxSensitivity_Type=OpticalPower1Decimal
_DcpInterfaceTrxLanesRxSensitivity_Object=MibTableColumn
dcpInterfaceTrxLanesRxSensitivity=_DcpInterfaceTrxLanesRxSensitivity_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1,5),_DcpInterfaceTrxLanesRxSensitivity_Type())
dcpInterfaceTrxLanesRxSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxLanesRxSensitivity.setStatus(_B)
_DcpInterfaceTrxLanesTxBias_Type=OpticalPower1Decimal
_DcpInterfaceTrxLanesTxBias_Object=MibTableColumn
dcpInterfaceTrxLanesTxBias=_DcpInterfaceTrxLanesTxBias_Object((1,3,6,1,4,1,30826,2,2,1,4,1,1,6),_DcpInterfaceTrxLanesTxBias_Type())
dcpInterfaceTrxLanesTxBias.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpInterfaceTrxLanesTxBias.setStatus(_B)
dcpInterfaceTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,1,2,1,1))
dcpInterfaceTableGroupV1.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:dcpInterfaceTableGroupV1.setStatus(_R)
dcpInterfaceTableGroupV2=ObjectGroup((1,3,6,1,4,1,30826,2,2,1,2,1,2))
dcpInterfaceTableGroupV2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_S)))
if mibBuilder.loadTexts:dcpInterfaceTableGroupV2.setStatus(_B)
dcpInterfaceTableGroupV3=ObjectGroup((1,3,6,1,4,1,30826,2,2,1,2,1,3))
dcpInterfaceTableGroupV3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_S),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:dcpInterfaceTableGroupV3.setStatus(_B)
dcpInterfaceTrxTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,1,2,3,1))
dcpInterfaceTrxTableGroupV1.setObjects(*((_A,_E),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:dcpInterfaceTrxTableGroupV1.setStatus(_B)
dcpInterfaceTrxTableGroupV2=ObjectGroup((1,3,6,1,4,1,30826,2,2,1,2,3,2))
dcpInterfaceTrxTableGroupV2.setObjects(*((_A,_E),(_A,_E),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A7)))
if mibBuilder.loadTexts:dcpInterfaceTrxTableGroupV2.setStatus(_B)
dcpInterfaceTrxLanesTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,1,2,4,1))
dcpInterfaceTrxLanesTableGroupV1.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:dcpInterfaceTrxLanesTableGroupV1.setStatus(_B)
dcpInterfaceBasicComplV1=ModuleCompliance((1,3,6,1,4,1,30826,2,2,1,2,2,1))
dcpInterfaceBasicComplV1.setObjects((_A,_AD))
if mibBuilder.loadTexts:dcpInterfaceBasicComplV1.setStatus(_R)
dcpInterfaceBasicComplV2=ModuleCompliance((1,3,6,1,4,1,30826,2,2,1,2,2,2))
dcpInterfaceBasicComplV2.setObjects((_A,_AE))
if mibBuilder.loadTexts:dcpInterfaceBasicComplV2.setStatus(_R)
dcpInterfaceBasicComplV3=ModuleCompliance((1,3,6,1,4,1,30826,2,2,1,2,2,3))
dcpInterfaceBasicComplV3.setObjects((_A,_O))
if mibBuilder.loadTexts:dcpInterfaceBasicComplV3.setStatus(_B)
dcpInterfaceBasicComplV4=ModuleCompliance((1,3,6,1,4,1,30826,2,2,1,2,2,4))
dcpInterfaceBasicComplV4.setObjects(*((_A,_O),(_A,_AF),(_A,_A1)))
if mibBuilder.loadTexts:dcpInterfaceBasicComplV4.setStatus(_B)
dcpInterfaceBasicComplV5=ModuleCompliance((1,3,6,1,4,1,30826,2,2,1,2,2,5))
dcpInterfaceBasicComplV5.setObjects(*((_A,_O),(_A,_AG),(_A,_A1)))
if mibBuilder.loadTexts:dcpInterfaceBasicComplV5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'dcpInterface':dcpInterface,'dcpInterfaceObjects':dcpInterfaceObjects,'dcpInterfaceTable':dcpInterfaceTable,'dcpInterfaceEntry':dcpInterfaceEntry,_A2:dcpInterfaceIndex,_G:dcpInterfaceName,_H:dcpInterfaceRxPower,_I:dcpInterfaceTxPower,_J:dcpInterfaceStatus,_K:dcpInterfaceAlarm,_L:dcpInterfaceFormat,_N:dcpInterfaceWavelength,_M:dcpInterfaceChannelId,_S:dcpInterfaceDescription,_A5:dcpInterfacePortType,_A6:dcpInterfacePortMode,'dcpInterfaceMIBCompliance':dcpInterfaceMIBCompliance,'dcpInterfaceMIBGroups':dcpInterfaceMIBGroups,_AD:dcpInterfaceTableGroupV1,_AE:dcpInterfaceTableGroupV2,_O:dcpInterfaceTableGroupV3,'dcpInterfaceMIBCompliances':dcpInterfaceMIBCompliances,'dcpInterfaceBasicComplV1':dcpInterfaceBasicComplV1,'dcpInterfaceBasicComplV2':dcpInterfaceBasicComplV2,'dcpInterfaceBasicComplV3':dcpInterfaceBasicComplV3,'dcpInterfaceBasicComplV4':dcpInterfaceBasicComplV4,'dcpInterfaceBasicComplV5':dcpInterfaceBasicComplV5,'dcpInterfaceTrxMIBGroups':dcpInterfaceTrxMIBGroups,_AF:dcpInterfaceTrxTableGroupV1,_AG:dcpInterfaceTrxTableGroupV2,'dcpInterfaceTrxLanesMIBGroups':dcpInterfaceTrxLanesMIBGroups,_A1:dcpInterfaceTrxLanesTableGroupV1,'dcpInterfaceTrxObjects':dcpInterfaceTrxObjects,'dcpInterfaceTrxTable':dcpInterfaceTrxTable,'dcpInterfaceTrxEntry':dcpInterfaceTrxEntry,_A3:dcpInterfaceTrxIndex,_E:dcpInterfaceTrxName,_T:dcpInterfaceTrxLanes,_U:dcpInterfaceTrxTemperature,_V:dcpInterfaceTrxTemperatureHighWarningThreshold,_W:dcpInterfaceTrxTemperatureHighAlarmThreshold,_X:dcpInterfaceTrxWavelength,_Y:dcpInterfaceTrxChannelId,_Z:dcpInterfaceTrxActualFrequency,_a:dcpInterfaceTrxWantedFrequency,_b:dcpInterfaceTrxGridSpacing,_c:dcpInterfaceTrxTotalRxPower,_d:dcpInterfaceTrxSignalRxPower,_e:dcpInterfaceTrxTxPower,_f:dcpInterfaceTrxTxBias,_g:dcpInterfaceTrxRxSensitivity,_h:dcpInterfaceTrxRxLosThreshold,_i:dcpInterfaceTrxModulationType,_j:dcpInterfaceTrxBandwidth,_k:dcpInterfaceTrxFec,_l:dcpInterfaceTrxPulseShaping,_m:dcpInterfaceTrxCertified,_n:dcpInterfaceTrxOsnr,_o:dcpInterfaceTrxChromaticDispersion,_p:dcpInterfaceTrxDiffGroupDelay,_q:dcpInterfaceTrxPolarizationDependentLoss,_r:dcpInterfaceTrxPreFecBerMantissa,_s:dcpInterfaceTrxPreFecBerExponent,_t:dcpInterfaceTrxPreFecBerAvgMantissa,_u:dcpInterfaceTrxPreFecBerAvgExponent,_v:dcpInterfaceTrxUncorrectedBerMantissa,_w:dcpInterfaceTrxUncorrectedBerExponent,_x:dcpInterfaceTrxPostFecBerMantissa,_y:dcpInterfaceTrxPostFecBerExponent,_z:dcpInterfaceTrxQvalue,_A0:dcpInterfaceTrxQmargin,_A7:dcpInterfaceTrxStateOfPolarizationROC,'dcpInterfaceTrxLanesObjects':dcpInterfaceTrxLanesObjects,'dcpInterfaceTrxLanesTable':dcpInterfaceTrxLanesTable,'dcpInterfaceTrxLanesEntry':dcpInterfaceTrxLanesEntry,_A4:dcpInterfaceTrxLanesIndex,_A8:dcpInterfaceTrxLanesName,_A9:dcpInterfaceTrxLanesRxPower,_AA:dcpInterfaceTrxLanesTxPower,_AB:dcpInterfaceTrxLanesRxSensitivity,_AC:dcpInterfaceTrxLanesTxBias})