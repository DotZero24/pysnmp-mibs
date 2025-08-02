_BL='objectGroupDef'
_BK='externalPortDefSourceProfile'
_BJ='externalPortDefMinChromDisperRcv'
_BI='externalPortDefMaxPmdRcv'
_BH='externalPortDefMaxOptPowerRcv'
_BG='externalPortDefMinOptPowerRcv'
_BF='externalPortDefMinOsnrRcv'
_BE='externalPortDefChromDisperTx'
_BD='externalPortDefPmdTransmit'
_BC='externalPortDefOsnrTransmit'
_BB='externalPortDefOpticalPowerTx'
_BA='externalPortDefFrameFormat'
_B9='externalPortDefLineCoding'
_B8='externalPortDefFecType'
_B7='externalPortDefMaxBitErrorRate'
_B6='externalPortDefMaxChromDisperRcv'
_B5='externalPortDefBitrate'
_B4='externalPortDefFarEndLocation'
_B3='externalPortDefAlias'
_B2='externalPortDefChannelBandwith'
_B1='externalPortDefTransmitChannel'
_B0='externalPortDefType'
_A_='externalPortDefRowStatus'
_Az='connectionDefType'
_Ay='connectionDefRowStatus'
_Ax='virtualPortDefEqlzAdmin'
_Aw='virtualPortDefAdmin'
_Av='virtualPortDefAlias'
_Au='virtualPortDefType'
_At='virtualPortDefChannelBand'
_As='virtualPortDefRowStatus'
_Ar='physicalPortDefAdmin'
_Aq='physicalPortDefType'
_Ap='physicalPortDefRowStatus'
_Ao='crossConnectionDefType'
_An='crossOpticalLineDefTunnelAid'
_Am='crossOpticalLineDefAlias'
_Al='crossOpticalLineDefCrsType'
_Ak='crossOpticalLineDefConn'
_Aj='crossOpticalLineDefRedLineState'
_Ai='crossOpticalLineDefRowStatus'
_Ah='crossConnectionDefTunnelAid'
_Ag='crossConnectionDefPathNode'
_Af='crossConnectionDefAlias'
_Ae='crossConnectionDefConn'
_Ad='crossConnectionDefRedLineState'
_Ac='crossConnectionDefAdmin'
_Ab='crossConnectionDefRowStatus'
_Aa='0.1 dB/min'
_AZ='entityShelfConnSlotNo'
_AY='entityShelfConnShelfNo'
_AX='entityShelfConnPortNo'
_AW='entityShelfConnExtNo'
_AV='entityShelfConnClassName'
_AU='entityOpticalMuxSlotNo'
_AT='entityOpticalMuxShelfNo'
_AS='entityOpticalMuxPortNo'
_AR='entityOpticalMuxExtNo'
_AQ='entityOpticalMuxClassName'
_AP='entityOptLineClassName'
_AO='entityFfpSlotNo'
_AN='entityFfpShelfNo'
_AM='entityFfpPortNo'
_AL='entityFfpExtNo'
_AK='entityFfpClassName'
_AJ='entityExternalPortSlotNo'
_AI='entityExternalPortShelfNo'
_AH='entityExternalPortPortNo'
_AG='entityExternalPortExtNo'
_AF='entityExternalPortClassName'
_AE='entityCrsOptLineToIndexNo4'
_AD='entityCrsOptLineToIndexNo3'
_AC='entityCrsOptLineToIndexNo2'
_AB='entityCrsOptLineToIndexNo1'
_AA='entityCrsOptLineToClassName'
_A9='entityCrsOptLineFromIndexNo4'
_A8='entityCrsOptLineFromIndexNo3'
_A7='entityCrsOptLineFromIndexNo2'
_A6='entityCrsOptLineFromIndexNo1'
_A5='entityCrsOptLineFromClassName'
_A4='entityCrsOptLineClassName'
_A3='entityCrossDcnSlotNo'
_A2='entityCrossDcnShelfNo'
_A1='entityCrossDcnPortNo'
_A0='entityCrossDcnExtNo'
_z='entityCrossDcnClassName'
_y='entityCrossConnToSlotNo'
_x='entityCrossConnToShelfNo'
_w='entityCrossConnToPortNo'
_v='entityCrossConnToExtNo'
_u='entityCrossConnToClassName'
_t='entityCrossConnFromSlotNo'
_s='entityCrossConnFromShelfNo'
_r='entityCrossConnFromPortNo'
_q='entityCrossConnFromExtNo'
_p='entityCrossConnFromClassName'
_o='entityCrossConnClassName'
_n='entityContainerSlotNo'
_m='entityContainerShelfNo'
_l='entityContainerPortNo'
_k='entityContainerExtNo'
_j='entityContainerClassName'
_i='entityConnectionClassName'
_h='entityTerminPointIndexNo4'
_g='entityTerminPointIndexNo3'
_f='entityTerminPointIndexNo2'
_e='entityTerminPointIndexNo1'
_d='entityTerminPointClassName'
_c='ps/nm'
_b='entityOptLineIndexNo1'
_a='entityDcnSlotNo'
_Z='entityDcnShelfNo'
_Y='entityDcnPortNo'
_X='entityDcnExtNo'
_W='entityDcnClassName'
_V='ms'
_U='entityFacilitySlotNo'
_T='entityFacilityShelfNo'
_S='entityFacilityPortNo'
_R='entityFacilityExtNo'
_Q='entityFacilityClassName'
_P='entityEqptSlotNo'
_O='entityEqptShelfNo'
_N='entityEqptPortNo'
_M='entityEqptExtNo'
_L='entityEqptClassName'
_K='0.1 dB'
_J='0.1 dBm'
_I='s'
_H='%'
_G='Integer32'
_F='ADVA-FSPR7-DEF-MIB'
_E='OctetString'
_D='Unsigned32'
_C='ADVA-FSPR7-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entityConnectionClassName,entityContainerClassName,entityContainerExtNo,entityContainerPortNo,entityContainerShelfNo,entityContainerSlotNo,entityCrossConnClassName,entityCrossConnFromClassName,entityCrossConnFromExtNo,entityCrossConnFromPortNo,entityCrossConnFromShelfNo,entityCrossConnFromSlotNo,entityCrossConnToClassName,entityCrossConnToExtNo,entityCrossConnToPortNo,entityCrossConnToShelfNo,entityCrossConnToSlotNo,entityCrossDcnClassName,entityCrossDcnExtNo,entityCrossDcnPortNo,entityCrossDcnShelfNo,entityCrossDcnSlotNo,entityCrsOptLineClassName,entityCrsOptLineFromClassName,entityCrsOptLineFromIndexNo1,entityCrsOptLineFromIndexNo2,entityCrsOptLineFromIndexNo3,entityCrsOptLineFromIndexNo4,entityCrsOptLineToClassName,entityCrsOptLineToIndexNo1,entityCrsOptLineToIndexNo2,entityCrsOptLineToIndexNo3,entityCrsOptLineToIndexNo4,entityDcnClassName,entityDcnExtNo,entityDcnPortNo,entityDcnShelfNo,entityDcnSlotNo,entityEqptClassName,entityEqptExtNo,entityEqptPortNo,entityEqptShelfNo,entityEqptSlotNo,entityExternalPortClassName,entityExternalPortExtNo,entityExternalPortPortNo,entityExternalPortShelfNo,entityExternalPortSlotNo,entityFacilityClassName,entityFacilityExtNo,entityFacilityPortNo,entityFacilityShelfNo,entityFacilitySlotNo,entityFfpClassName,entityFfpExtNo,entityFfpPortNo,entityFfpShelfNo,entityFfpSlotNo,entityOptLineClassName,entityOptLineIndexNo1,entityOpticalMuxClassName,entityOpticalMuxExtNo,entityOpticalMuxPortNo,entityOpticalMuxShelfNo,entityOpticalMuxSlotNo,entityShelfConnClassName,entityShelfConnExtNo,entityShelfConnPortNo,entityShelfConnShelfNo,entityShelfConnSlotNo,entityTerminPointClassName,entityTerminPointIndexNo1,entityTerminPointIndexNo2,entityTerminPointIndexNo3,entityTerminPointIndexNo4=mibBuilder.importSymbols(_C,_i,_j,_k,_l,_m,_n,_o,_p,_q,_r,_s,_t,_u,_v,_w,_x,_y,_z,_A0,_A1,_A2,_A3,_A4,_A5,_A6,_A7,_A8,_A9,_AA,_AB,_AC,_AD,_AE,_W,_X,_Y,_Z,_a,_L,_M,_N,_O,_P,_AF,_AG,_AH,_AI,_AJ,_Q,_R,_S,_T,_U,_AK,_AL,_AM,_AN,_AO,_AP,_b,_AQ,_AR,_AS,_AT,_AU,_AV,_AW,_AX,_AY,_AZ,_d,_e,_f,_g,_h)
ApsRevertMode,ApsType,FfpType,FspR7APSCommand,FspR7AdminState,FspR7AlsMode,FspR7AseTabOpr,FspR7AutoThresReset,FspR7BERThreshold,FspR7BERThresholdSection,FspR7Baund,FspR7BidirectionalChannel,FspR7Bitrate,FspR7CapInventory,FspR7ChannelBandwidth,FspR7ChannelIdentifier,FspR7ChannelSpacing,FspR7CodeGain,FspR7Conn,FspR7ConnectorType,FspR7CpAuthType,FspR7DCFiberType,FspR7DeploymentScenario,FspR7DisableEnable,FspR7DispersionCompensation,FspR7DispersionConfig,FspR7DispersionModes,FspR7EdfaOutputPowerRating,FspR7EnableDisable,FspR7EqlzAdminState,FspR7ErrorFwdMode,FspR7FecType,FspR7FiberBrand,FspR7FiberDetect,FspR7FlowControlMode,FspR7ForceConfig,FspR7FrameFormat,FspR7FunctionCrs,FspR7Gain,FspR7GainRange,FspR7IPv6Type,FspR7InitEqualization,FspR7InterfaceType,FspR7InvertTelemetryInputLogic,FspR7IpMode,FspR7IpType,FspR7LacpMode,FspR7LacpTimeout,FspR7LagPortType,FspR7LaneGroupInventory,FspR7LaserDelayTimer,FspR7LaserForcedOperation,FspR7LineCoding,FspR7LossAttenuation,FspR7ManualAuto,FspR7Mapping,FspR7MaxBitErrorRate,FspR7MuxMethod,FspR7NdpCleanup,FspR7NoYes,FspR7NumberOfChannels,FspR7NumberOfChannelsProv,FspR7OptUpdate,FspR7OpticalBand,FspR7OpticalFiberType,FspR7OpticalGroup,FspR7OpticalInterfaceReach,FspR7OpticalSubBand,FspR7OpuPayloadType,FspR7OscUsage,FspR7OspfMode,FspR7OtdrPeriod,FspR7PRBSTest,FspR7PathNode,FspR7PlugDataRate,FspR7PmReset,FspR7PortBehaviour,FspR7PortMode,FspR7PortRole,FspR7PrbsPmReset,FspR7ProtectionType,FspR7PsuOutputPower,FspR7RedLinedState,FspR7RlsMan,FspR7RoadmNumber,FspR7RowStatus,FspR7Scrambling,FspR7SingleFiberLocation,FspR7SnmpHexString,FspR7SnmpLongString,FspR7Stuff,FspR7SupplyType,FspR7TelemetryOutput,FspR7TifOutputReset,FspR7TiltSet,FspR7Topology,FspR7TrafficDirection,FspR7TransmissionMode,FspR7TurnupConfig,FspR7TxOffOnTm,FspR7TypeConnection,FspR7TypeCrs,FspR7Unsigned32Caps,FspR7UntaggedFrames,FspR7VoaMode,FspR7XfpDecisionThres,FspR7YesNo=mibBuilder.importSymbols('ADVA-FSPR7-TC-MIB','ApsRevertMode','ApsType','FfpType','FspR7APSCommand','FspR7AdminState','FspR7AlsMode','FspR7AseTabOpr','FspR7AutoThresReset','FspR7BERThreshold','FspR7BERThresholdSection','FspR7Baund','FspR7BidirectionalChannel','FspR7Bitrate','FspR7CapInventory','FspR7ChannelBandwidth','FspR7ChannelIdentifier','FspR7ChannelSpacing','FspR7CodeGain','FspR7Conn','FspR7ConnectorType','FspR7CpAuthType','FspR7DCFiberType','FspR7DeploymentScenario','FspR7DisableEnable','FspR7DispersionCompensation','FspR7DispersionConfig','FspR7DispersionModes','FspR7EdfaOutputPowerRating','FspR7EnableDisable','FspR7EqlzAdminState','FspR7ErrorFwdMode','FspR7FecType','FspR7FiberBrand','FspR7FiberDetect','FspR7FlowControlMode','FspR7ForceConfig','FspR7FrameFormat','FspR7FunctionCrs','FspR7Gain','FspR7GainRange','FspR7IPv6Type','FspR7InitEqualization','FspR7InterfaceType','FspR7InvertTelemetryInputLogic','FspR7IpMode','FspR7IpType','FspR7LacpMode','FspR7LacpTimeout','FspR7LagPortType','FspR7LaneGroupInventory','FspR7LaserDelayTimer','FspR7LaserForcedOperation','FspR7LineCoding','FspR7LossAttenuation','FspR7ManualAuto','FspR7Mapping','FspR7MaxBitErrorRate','FspR7MuxMethod','FspR7NdpCleanup','FspR7NoYes','FspR7NumberOfChannels','FspR7NumberOfChannelsProv','FspR7OptUpdate','FspR7OpticalBand','FspR7OpticalFiberType','FspR7OpticalGroup','FspR7OpticalInterfaceReach','FspR7OpticalSubBand','FspR7OpuPayloadType','FspR7OscUsage','FspR7OspfMode','FspR7OtdrPeriod','FspR7PRBSTest','FspR7PathNode','FspR7PlugDataRate','FspR7PmReset','FspR7PortBehaviour','FspR7PortMode','FspR7PortRole','FspR7PrbsPmReset','FspR7ProtectionType','FspR7PsuOutputPower','FspR7RedLinedState','FspR7RlsMan','FspR7RoadmNumber','FspR7RowStatus','FspR7Scrambling','FspR7SingleFiberLocation','FspR7SnmpHexString','FspR7SnmpLongString','FspR7Stuff','FspR7SupplyType','FspR7TelemetryOutput','FspR7TifOutputReset','FspR7TiltSet','FspR7Topology','FspR7TrafficDirection','FspR7TransmissionMode','FspR7TurnupConfig','FspR7TxOffOnTm','FspR7TypeConnection','FspR7TypeCrs','FspR7Unsigned32Caps','FspR7UntaggedFrames','FspR7VoaMode','FspR7XfpDecisionThres','FspR7YesNo')
ApsDirection,ApsHoldoffTime,EnableState,EthDuplexMode,FspR7EquipmentType,LoopConfig,OhTerminationLevel,OtnPayloadType,OtnTcmLevel,ProtectionMech,SonetTimingSource,SonetTraceForm,TimMode,VirtualContainerType,fspR7=mibBuilder.importSymbols('ADVA-MIB','ApsDirection','ApsHoldoffTime','EnableState','EthDuplexMode','FspR7EquipmentType','LoopConfig','OhTerminationLevel','OtnPayloadType','OtnTcmLevel','ProtectionMech','SonetTimingSource','SonetTraceForm','TimMode','VirtualContainerType','fspR7')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
advaFspR7Def=ModuleIdentity((1,3,6,1,4,1,2544,1,11,10))
if mibBuilder.loadTexts:advaFspR7Def.setRevisions(('2014-10-15 00:00','2014-09-29 00:00','2013-12-04 00:00','2013-08-20 00:00','2011-05-22 00:00'))
_ManagementDef_ObjectIdentity=ObjectIdentity
managementDef=_ManagementDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3))
_SpecificMgmtDef_ObjectIdentity=ObjectIdentity
specificMgmtDef=_SpecificMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,2))
_CrossConnectionDefTable_Object=MibTable
crossConnectionDefTable=_CrossConnectionDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6))
if mibBuilder.loadTexts:crossConnectionDefTable.setStatus(_A)
_CrossConnectionDefEntry_Object=MibTableRow
crossConnectionDefEntry=_CrossConnectionDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1))
crossConnectionDefEntry.setIndexNames((0,_C,_s),(0,_C,_t),(0,_C,_r),(0,_C,_q),(0,_C,_p),(0,_C,_x),(0,_C,_y),(0,_C,_w),(0,_C,_v),(0,_C,_u),(0,_C,_o))
if mibBuilder.loadTexts:crossConnectionDefEntry.setStatus(_A)
_CrossConnectionDefRowStatus_Type=FspR7RowStatus
_CrossConnectionDefRowStatus_Object=MibTableColumn
crossConnectionDefRowStatus=_CrossConnectionDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,1),_CrossConnectionDefRowStatus_Type())
crossConnectionDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefRowStatus.setStatus(_A)
_CrossConnectionDefAdmin_Type=FspR7AdminState
_CrossConnectionDefAdmin_Object=MibTableColumn
crossConnectionDefAdmin=_CrossConnectionDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,2),_CrossConnectionDefAdmin_Type())
crossConnectionDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefAdmin.setStatus(_A)
_CrossConnectionDefRedLineState_Type=FspR7RedLinedState
_CrossConnectionDefRedLineState_Object=MibTableColumn
crossConnectionDefRedLineState=_CrossConnectionDefRedLineState_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,3),_CrossConnectionDefRedLineState_Type())
crossConnectionDefRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefRedLineState.setStatus(_A)
_CrossConnectionDefConn_Type=FspR7Conn
_CrossConnectionDefConn_Object=MibTableColumn
crossConnectionDefConn=_CrossConnectionDefConn_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,4),_CrossConnectionDefConn_Type())
crossConnectionDefConn.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefConn.setStatus(_A)
_CrossConnectionDefAlias_Type=SnmpAdminString
_CrossConnectionDefAlias_Object=MibTableColumn
crossConnectionDefAlias=_CrossConnectionDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,5),_CrossConnectionDefAlias_Type())
crossConnectionDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefAlias.setStatus(_A)
_CrossConnectionDefPathNode_Type=FspR7PathNode
_CrossConnectionDefPathNode_Object=MibTableColumn
crossConnectionDefPathNode=_CrossConnectionDefPathNode_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,6),_CrossConnectionDefPathNode_Type())
crossConnectionDefPathNode.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefPathNode.setStatus(_A)
_CrossConnectionDefTunnelAid_Type=SnmpAdminString
_CrossConnectionDefTunnelAid_Object=MibTableColumn
crossConnectionDefTunnelAid=_CrossConnectionDefTunnelAid_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,7),_CrossConnectionDefTunnelAid_Type())
crossConnectionDefTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefTunnelAid.setStatus(_A)
_CrossConnectionDefType_Type=FspR7InterfaceType
_CrossConnectionDefType_Object=MibTableColumn
crossConnectionDefType=_CrossConnectionDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,8),_CrossConnectionDefType_Type())
crossConnectionDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefType.setStatus(_A)
_CrossConnectionDefCrsFunction_Type=FspR7FunctionCrs
_CrossConnectionDefCrsFunction_Object=MibTableColumn
crossConnectionDefCrsFunction=_CrossConnectionDefCrsFunction_Object((1,3,6,1,4,1,2544,1,11,10,3,2,6,1,9),_CrossConnectionDefCrsFunction_Type())
crossConnectionDefCrsFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionDefCrsFunction.setStatus(_A)
_CrossOpticalLineDefTable_Object=MibTable
crossOpticalLineDefTable=_CrossOpticalLineDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7))
if mibBuilder.loadTexts:crossOpticalLineDefTable.setStatus(_A)
_CrossOpticalLineDefEntry_Object=MibTableRow
crossOpticalLineDefEntry=_CrossOpticalLineDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1))
crossOpticalLineDefEntry.setIndexNames((0,_C,_A6),(0,_C,_A7),(0,_C,_A8),(0,_C,_A9),(0,_C,_A5),(0,_C,_AB),(0,_C,_AC),(0,_C,_AD),(0,_C,_AE),(0,_C,_AA),(0,_C,_A4))
if mibBuilder.loadTexts:crossOpticalLineDefEntry.setStatus(_A)
_CrossOpticalLineDefRowStatus_Type=FspR7RowStatus
_CrossOpticalLineDefRowStatus_Object=MibTableColumn
crossOpticalLineDefRowStatus=_CrossOpticalLineDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1,1),_CrossOpticalLineDefRowStatus_Type())
crossOpticalLineDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineDefRowStatus.setStatus(_A)
_CrossOpticalLineDefRedLineState_Type=FspR7RedLinedState
_CrossOpticalLineDefRedLineState_Object=MibTableColumn
crossOpticalLineDefRedLineState=_CrossOpticalLineDefRedLineState_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1,2),_CrossOpticalLineDefRedLineState_Type())
crossOpticalLineDefRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineDefRedLineState.setStatus(_A)
_CrossOpticalLineDefConn_Type=FspR7Conn
_CrossOpticalLineDefConn_Object=MibTableColumn
crossOpticalLineDefConn=_CrossOpticalLineDefConn_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1,3),_CrossOpticalLineDefConn_Type())
crossOpticalLineDefConn.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineDefConn.setStatus(_A)
_CrossOpticalLineDefCrsType_Type=FspR7TypeCrs
_CrossOpticalLineDefCrsType_Object=MibTableColumn
crossOpticalLineDefCrsType=_CrossOpticalLineDefCrsType_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1,4),_CrossOpticalLineDefCrsType_Type())
crossOpticalLineDefCrsType.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineDefCrsType.setStatus(_A)
_CrossOpticalLineDefAlias_Type=SnmpAdminString
_CrossOpticalLineDefAlias_Object=MibTableColumn
crossOpticalLineDefAlias=_CrossOpticalLineDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1,5),_CrossOpticalLineDefAlias_Type())
crossOpticalLineDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineDefAlias.setStatus(_A)
_CrossOpticalLineDefTunnelAid_Type=SnmpAdminString
_CrossOpticalLineDefTunnelAid_Object=MibTableColumn
crossOpticalLineDefTunnelAid=_CrossOpticalLineDefTunnelAid_Object((1,3,6,1,4,1,2544,1,11,10,3,2,7,1,6),_CrossOpticalLineDefTunnelAid_Type())
crossOpticalLineDefTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineDefTunnelAid.setStatus(_A)
_EndOfCrossOpticalLineDefTable_Type=Integer32
_EndOfCrossOpticalLineDefTable_Object=MibScalar
endOfCrossOpticalLineDefTable=_EndOfCrossOpticalLineDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,2,8),_EndOfCrossOpticalLineDefTable_Type())
endOfCrossOpticalLineDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfCrossOpticalLineDefTable.setStatus(_A)
_CrossDcnDefTable_Object=MibTable
crossDcnDefTable=_CrossDcnDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,2,9))
if mibBuilder.loadTexts:crossDcnDefTable.setStatus(_A)
_CrossDcnDefEntry_Object=MibTableRow
crossDcnDefEntry=_CrossDcnDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,2,9,1))
crossDcnDefEntry.setIndexNames((0,_C,_A2),(0,_C,_A3),(0,_C,_A1),(0,_C,_A0),(0,_C,_z))
if mibBuilder.loadTexts:crossDcnDefEntry.setStatus(_A)
_CrossDcnDefRowStatus_Type=RowStatus
_CrossDcnDefRowStatus_Object=MibTableColumn
crossDcnDefRowStatus=_CrossDcnDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,2,9,1,1),_CrossDcnDefRowStatus_Type())
crossDcnDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnDefRowStatus.setStatus(_A)
_CrossDcnDefType_Type=FspR7TypeConnection
_CrossDcnDefType_Object=MibTableColumn
crossDcnDefType=_CrossDcnDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,2,9,1,2),_CrossDcnDefType_Type())
crossDcnDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnDefType.setStatus(_A)
_CrossDcnDefLink_Type=SnmpAdminString
_CrossDcnDefLink_Object=MibTableColumn
crossDcnDefLink=_CrossDcnDefLink_Object((1,3,6,1,4,1,2544,1,11,10,3,2,9,1,3),_CrossDcnDefLink_Type())
crossDcnDefLink.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnDefLink.setStatus(_A)
_CrossDcnDefEcc_Type=SnmpAdminString
_CrossDcnDefEcc_Object=MibTableColumn
crossDcnDefEcc=_CrossDcnDefEcc_Object((1,3,6,1,4,1,2544,1,11,10,3,2,9,1,4),_CrossDcnDefEcc_Type())
crossDcnDefEcc.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnDefEcc.setStatus(_A)
_EndOfCrossDcnDefTable_Type=Integer32
_EndOfCrossDcnDefTable_Object=MibScalar
endOfCrossDcnDefTable=_EndOfCrossDcnDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,2,10),_EndOfCrossDcnDefTable_Type())
endOfCrossDcnDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfCrossDcnDefTable.setStatus(_A)
_EndOfSpecificMgmtDef_Type=Integer32
_EndOfSpecificMgmtDef_Object=MibScalar
endOfSpecificMgmtDef=_EndOfSpecificMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,2,10000),_EndOfSpecificMgmtDef_Type())
endOfSpecificMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfSpecificMgmtDef.setStatus(_A)
_EqptMgmtDef_ObjectIdentity=ObjectIdentity
eqptMgmtDef=_EqptMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,3))
_ShelfDefTable_Object=MibTable
shelfDefTable=_ShelfDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1))
if mibBuilder.loadTexts:shelfDefTable.setStatus(_A)
_ShelfDefEntry_Object=MibTableRow
shelfDefEntry=_ShelfDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1))
shelfDefEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_N),(0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:shelfDefEntry.setStatus(_A)
_ShelfDefRowStatus_Type=RowStatus
_ShelfDefRowStatus_Object=MibTableColumn
shelfDefRowStatus=_ShelfDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,1),_ShelfDefRowStatus_Type())
shelfDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefRowStatus.setStatus(_A)
_ShelfDefPsuOutputPower_Type=FspR7PsuOutputPower
_ShelfDefPsuOutputPower_Object=MibTableColumn
shelfDefPsuOutputPower=_ShelfDefPsuOutputPower_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,2),_ShelfDefPsuOutputPower_Type())
shelfDefPsuOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefPsuOutputPower.setStatus(_A)
_ShelfDefType_Type=FspR7EquipmentType
_ShelfDefType_Object=MibTableColumn
shelfDefType=_ShelfDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,3),_ShelfDefType_Type())
shelfDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefType.setStatus(_A)
_ShelfDefRack_Type=SnmpAdminString
_ShelfDefRack_Object=MibTableColumn
shelfDefRack=_ShelfDefRack_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,4),_ShelfDefRack_Type())
shelfDefRack.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefRack.setStatus(_A)
_ShelfDefSupply_Type=FspR7SupplyType
_ShelfDefSupply_Object=MibTableColumn
shelfDefSupply=_ShelfDefSupply_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,5),_ShelfDefSupply_Type())
shelfDefSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefSupply.setStatus(_A)
_ShelfDefBandProvision_Type=FspR7OpticalBand
_ShelfDefBandProvision_Object=MibTableColumn
shelfDefBandProvision=_ShelfDefBandProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,6),_ShelfDefBandProvision_Type())
shelfDefBandProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefBandProvision.setStatus(_A)
_ShelfDefAdmin_Type=FspR7AdminState
_ShelfDefAdmin_Object=MibTableColumn
shelfDefAdmin=_ShelfDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,7),_ShelfDefAdmin_Type())
shelfDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefAdmin.setStatus(_A)
class _ShelfDefRackNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ShelfDefRackNumber_Type.__name__=_D
_ShelfDefRackNumber_Object=MibTableColumn
shelfDefRackNumber=_ShelfDefRackNumber_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,8),_ShelfDefRackNumber_Type())
shelfDefRackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefRackNumber.setStatus(_A)
class _ShelfDefRackOrder_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,45))
_ShelfDefRackOrder_Type.__name__=_D
_ShelfDefRackOrder_Object=MibTableColumn
shelfDefRackOrder=_ShelfDefRackOrder_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,9),_ShelfDefRackOrder_Type())
shelfDefRackOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefRackOrder.setStatus(_A)
_ShelfDefAlias_Type=SnmpAdminString
_ShelfDefAlias_Object=MibTableColumn
shelfDefAlias=_ShelfDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,10),_ShelfDefAlias_Type())
shelfDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefAlias.setStatus(_A)
class _ShelfDefSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_ShelfDefSlot_Type.__name__=_D
_ShelfDefSlot_Object=MibTableColumn
shelfDefSlot=_ShelfDefSlot_Object((1,3,6,1,4,1,2544,1,11,10,3,3,1,1,11),_ShelfDefSlot_Type())
shelfDefSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfDefSlot.setStatus(_A)
_EndOfShelfDefTable_Type=Integer32
_EndOfShelfDefTable_Object=MibScalar
endOfShelfDefTable=_EndOfShelfDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,2),_EndOfShelfDefTable_Type())
endOfShelfDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfShelfDefTable.setStatus(_A)
_FanDefTable_Object=MibTable
fanDefTable=_FanDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3))
if mibBuilder.loadTexts:fanDefTable.setStatus(_A)
_FanDefEntry_Object=MibTableRow
fanDefEntry=_FanDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3,1))
fanDefEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_N),(0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:fanDefEntry.setStatus(_A)
_FanDefRowStatus_Type=RowStatus
_FanDefRowStatus_Object=MibTableColumn
fanDefRowStatus=_FanDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3,1,1),_FanDefRowStatus_Type())
fanDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanDefRowStatus.setStatus(_A)
_FanDefAdmin_Type=FspR7AdminState
_FanDefAdmin_Object=MibTableColumn
fanDefAdmin=_FanDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3,1,2),_FanDefAdmin_Type())
fanDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:fanDefAdmin.setStatus(_A)
_FanDefType_Type=FspR7EquipmentType
_FanDefType_Object=MibTableColumn
fanDefType=_FanDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3,1,3),_FanDefType_Type())
fanDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:fanDefType.setStatus(_A)
_FanDefAlias_Type=SnmpAdminString
_FanDefAlias_Object=MibTableColumn
fanDefAlias=_FanDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3,1,4),_FanDefAlias_Type())
fanDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fanDefAlias.setStatus(_A)
_FanDefOutputReset_Type=FspR7TifOutputReset
_FanDefOutputReset_Object=MibTableColumn
fanDefOutputReset=_FanDefOutputReset_Object((1,3,6,1,4,1,2544,1,11,10,3,3,3,1,5),_FanDefOutputReset_Type())
fanDefOutputReset.setMaxAccess(_B)
if mibBuilder.loadTexts:fanDefOutputReset.setStatus(_A)
_EndOfFanDefTable_Type=Integer32
_EndOfFanDefTable_Object=MibScalar
endOfFanDefTable=_EndOfFanDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,4),_EndOfFanDefTable_Type())
endOfFanDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFanDefTable.setStatus(_A)
_PlugDefTable_Object=MibTable
plugDefTable=_PlugDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5))
if mibBuilder.loadTexts:plugDefTable.setStatus(_A)
_PlugDefEntry_Object=MibTableRow
plugDefEntry=_PlugDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1))
plugDefEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_N),(0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:plugDefEntry.setStatus(_A)
_PlugDefRowStatus_Type=RowStatus
_PlugDefRowStatus_Object=MibTableColumn
plugDefRowStatus=_PlugDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,1),_PlugDefRowStatus_Type())
plugDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefRowStatus.setStatus(_A)
_PlugDefConnector_Type=FspR7ConnectorType
_PlugDefConnector_Object=MibTableColumn
plugDefConnector=_PlugDefConnector_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,2),_PlugDefConnector_Type())
plugDefConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefConnector.setStatus(_A)
_PlugDefType_Type=FspR7EquipmentType
_PlugDefType_Object=MibTableColumn
plugDefType=_PlugDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,3),_PlugDefType_Type())
plugDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefType.setStatus(_A)
_PlugDefReach_Type=FspR7OpticalInterfaceReach
_PlugDefReach_Object=MibTableColumn
plugDefReach=_PlugDefReach_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,4),_PlugDefReach_Type())
plugDefReach.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefReach.setStatus(_A)
class _PlugDefLoopbackAttenuation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_PlugDefLoopbackAttenuation_Type.__name__=_D
_PlugDefLoopbackAttenuation_Object=MibTableColumn
plugDefLoopbackAttenuation=_PlugDefLoopbackAttenuation_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,5),_PlugDefLoopbackAttenuation_Type())
plugDefLoopbackAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefLoopbackAttenuation.setStatus(_A)
if mibBuilder.loadTexts:plugDefLoopbackAttenuation.setUnits(_K)
_PlugDefTransmitChannel_Type=FspR7ChannelIdentifier
_PlugDefTransmitChannel_Object=MibTableColumn
plugDefTransmitChannel=_PlugDefTransmitChannel_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,6),_PlugDefTransmitChannel_Type())
plugDefTransmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefTransmitChannel.setStatus(_A)
_PlugDefAlias_Type=SnmpAdminString
_PlugDefAlias_Object=MibTableColumn
plugDefAlias=_PlugDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,7),_PlugDefAlias_Type())
plugDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefAlias.setStatus(_A)
_PlugDefLaneGroup_Type=FspR7LaneGroupInventory
_PlugDefLaneGroup_Object=MibTableColumn
plugDefLaneGroup=_PlugDefLaneGroup_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,8),_PlugDefLaneGroup_Type())
plugDefLaneGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefLaneGroup.setStatus(_A)
_PlugDefMaxDataRate_Type=FspR7PlugDataRate
_PlugDefMaxDataRate_Object=MibTableColumn
plugDefMaxDataRate=_PlugDefMaxDataRate_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,9),_PlugDefMaxDataRate_Type())
plugDefMaxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefMaxDataRate.setStatus(_A)
_PlugDefThirdPartyUsage_Type=EnableState
_PlugDefThirdPartyUsage_Object=MibTableColumn
plugDefThirdPartyUsage=_PlugDefThirdPartyUsage_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,10),_PlugDefThirdPartyUsage_Type())
plugDefThirdPartyUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefThirdPartyUsage.setStatus(_A)
_PlugDefAdmin_Type=FspR7AdminState
_PlugDefAdmin_Object=MibTableColumn
plugDefAdmin=_PlugDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,11),_PlugDefAdmin_Type())
plugDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefAdmin.setStatus(_A)
_PlugDefBidirectionalChannel_Type=FspR7BidirectionalChannel
_PlugDefBidirectionalChannel_Object=MibTableColumn
plugDefBidirectionalChannel=_PlugDefBidirectionalChannel_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,12),_PlugDefBidirectionalChannel_Type())
plugDefBidirectionalChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefBidirectionalChannel.setStatus(_A)
_PlugDefChannelSpacingProvision_Type=FspR7ChannelSpacing
_PlugDefChannelSpacingProvision_Object=MibTableColumn
plugDefChannelSpacingProvision=_PlugDefChannelSpacingProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,5,1,13),_PlugDefChannelSpacingProvision_Type())
plugDefChannelSpacingProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:plugDefChannelSpacingProvision.setStatus(_A)
_EndOfPlugDefTable_Type=Integer32
_EndOfPlugDefTable_Object=MibScalar
endOfPlugDefTable=_EndOfPlugDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,6),_EndOfPlugDefTable_Type())
endOfPlugDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPlugDefTable.setStatus(_A)
_ModuleDefTable_Object=MibTable
moduleDefTable=_ModuleDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7))
if mibBuilder.loadTexts:moduleDefTable.setStatus(_A)
_ModuleDefEntry_Object=MibTableRow
moduleDefEntry=_ModuleDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1))
moduleDefEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_N),(0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:moduleDefEntry.setStatus(_A)
_ModuleDefRowStatus_Type=RowStatus
_ModuleDefRowStatus_Object=MibTableColumn
moduleDefRowStatus=_ModuleDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,1),_ModuleDefRowStatus_Type())
moduleDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefRowStatus.setStatus(_A)
_ModuleDefPsuOutputPower_Type=FspR7PsuOutputPower
_ModuleDefPsuOutputPower_Object=MibTableColumn
moduleDefPsuOutputPower=_ModuleDefPsuOutputPower_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,2),_ModuleDefPsuOutputPower_Type())
moduleDefPsuOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefPsuOutputPower.setStatus(_A)
_ModuleDefPower_Type=FspR7EdfaOutputPowerRating
_ModuleDefPower_Object=MibTableColumn
moduleDefPower=_ModuleDefPower_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,3),_ModuleDefPower_Type())
moduleDefPower.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefPower.setStatus(_A)
_ModuleDefReach_Type=FspR7OpticalInterfaceReach
_ModuleDefReach_Object=MibTableColumn
moduleDefReach=_ModuleDefReach_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,4),_ModuleDefReach_Type())
moduleDefReach.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefReach.setStatus(_A)
_ModuleDefInitEqlz_Type=FspR7InitEqualization
_ModuleDefInitEqlz_Object=MibTableColumn
moduleDefInitEqlz=_ModuleDefInitEqlz_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,5),_ModuleDefInitEqlz_Type())
moduleDefInitEqlz.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefInitEqlz.setStatus(_A)
_ModuleDefLanAid_Type=SnmpAdminString
_ModuleDefLanAid_Object=MibTableColumn
moduleDefLanAid=_ModuleDefLanAid_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,6),_ModuleDefLanAid_Type())
moduleDefLanAid.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefLanAid.setStatus(_A)
_ModuleDefType_Type=FspR7EquipmentType
_ModuleDefType_Object=MibTableColumn
moduleDefType=_ModuleDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,7),_ModuleDefType_Type())
moduleDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefType.setStatus(_A)
_ModuleDefMapping_Type=FspR7Mapping
_ModuleDefMapping_Object=MibTableColumn
moduleDefMapping=_ModuleDefMapping_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,8),_ModuleDefMapping_Type())
moduleDefMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefMapping.setStatus(_A)
_ModuleDefGainRange_Type=FspR7GainRange
_ModuleDefGainRange_Object=MibTableColumn
moduleDefGainRange=_ModuleDefGainRange_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,9),_ModuleDefGainRange_Type())
moduleDefGainRange.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefGainRange.setStatus(_A)
_ModuleDefSfProvision_Type=FspR7SingleFiberLocation
_ModuleDefSfProvision_Object=MibTableColumn
moduleDefSfProvision=_ModuleDefSfProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,10),_ModuleDefSfProvision_Type())
moduleDefSfProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefSfProvision.setStatus(_A)
_ModuleDefCapabilityLevelProvision_Type=FspR7CapInventory
_ModuleDefCapabilityLevelProvision_Object=MibTableColumn
moduleDefCapabilityLevelProvision=_ModuleDefCapabilityLevelProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,11),_ModuleDefCapabilityLevelProvision_Type())
moduleDefCapabilityLevelProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefCapabilityLevelProvision.setStatus(_A)
_ModuleDefDCFiberType_Type=FspR7DCFiberType
_ModuleDefDCFiberType_Object=MibTableColumn
moduleDefDCFiberType=_ModuleDefDCFiberType_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,12),_ModuleDefDCFiberType_Type())
moduleDefDCFiberType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefDCFiberType.setStatus(_A)
_ModuleDefChannelsProvision_Type=FspR7NumberOfChannelsProv
_ModuleDefChannelsProvision_Object=MibTableColumn
moduleDefChannelsProvision=_ModuleDefChannelsProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,13),_ModuleDefChannelsProvision_Type())
moduleDefChannelsProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefChannelsProvision.setStatus(_A)
_ModuleDefFiberDetect_Type=FspR7FiberDetect
_ModuleDefFiberDetect_Object=MibTableColumn
moduleDefFiberDetect=_ModuleDefFiberDetect_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,14),_ModuleDefFiberDetect_Type())
moduleDefFiberDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefFiberDetect.setStatus(_A)
_ModuleDefSupply_Type=FspR7SupplyType
_ModuleDefSupply_Object=MibTableColumn
moduleDefSupply=_ModuleDefSupply_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,15),_ModuleDefSupply_Type())
moduleDefSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefSupply.setStatus(_A)
_ModuleDefGroup_Type=FspR7OpticalGroup
_ModuleDefGroup_Object=MibTableColumn
moduleDefGroup=_ModuleDefGroup_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,16),_ModuleDefGroup_Type())
moduleDefGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefGroup.setStatus(_A)
_ModuleDefDeploy_Type=FspR7DeploymentScenario
_ModuleDefDeploy_Object=MibTableColumn
moduleDefDeploy=_ModuleDefDeploy_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,17),_ModuleDefDeploy_Type())
moduleDefDeploy.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefDeploy.setStatus(_A)
class _ModuleDefLagSysPrio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ModuleDefLagSysPrio_Type.__name__=_D
_ModuleDefLagSysPrio_Object=MibTableColumn
moduleDefLagSysPrio=_ModuleDefLagSysPrio_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,18),_ModuleDefLagSysPrio_Type())
moduleDefLagSysPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefLagSysPrio.setStatus(_A)
_ModuleDefTransmitChannel_Type=FspR7ChannelIdentifier
_ModuleDefTransmitChannel_Object=MibTableColumn
moduleDefTransmitChannel=_ModuleDefTransmitChannel_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,19),_ModuleDefTransmitChannel_Type())
moduleDefTransmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefTransmitChannel.setStatus(_A)
_ModuleDefBand_Type=FspR7OpticalBand
_ModuleDefBand_Object=MibTableColumn
moduleDefBand=_ModuleDefBand_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,20),_ModuleDefBand_Type())
moduleDefBand.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefBand.setStatus(_A)
_ModuleDefTrafficDirection_Type=FspR7TrafficDirection
_ModuleDefTrafficDirection_Object=MibTableColumn
moduleDefTrafficDirection=_ModuleDefTrafficDirection_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,21),_ModuleDefTrafficDirection_Type())
moduleDefTrafficDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefTrafficDirection.setStatus(_A)
_ModuleDefIpAddr_Type=IpAddress
_ModuleDefIpAddr_Object=MibTableColumn
moduleDefIpAddr=_ModuleDefIpAddr_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,22),_ModuleDefIpAddr_Type())
moduleDefIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefIpAddr.setStatus(_A)
_ModuleDefDispersionCompensation_Type=FspR7DispersionCompensation
_ModuleDefDispersionCompensation_Object=MibTableColumn
moduleDefDispersionCompensation=_ModuleDefDispersionCompensation_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,23),_ModuleDefDispersionCompensation_Type())
moduleDefDispersionCompensation.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefDispersionCompensation.setStatus(_A)
_ModuleDefActivateDetect_Type=FspR7YesNo
_ModuleDefActivateDetect_Object=MibTableColumn
moduleDefActivateDetect=_ModuleDefActivateDetect_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,24),_ModuleDefActivateDetect_Type())
moduleDefActivateDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefActivateDetect.setStatus(_A)
_ModuleDefOscUsage_Type=FspR7OscUsage
_ModuleDefOscUsage_Object=MibTableColumn
moduleDefOscUsage=_ModuleDefOscUsage_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,25),_ModuleDefOscUsage_Type())
moduleDefOscUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefOscUsage.setStatus(_A)
_ModuleDefAdmin_Type=FspR7AdminState
_ModuleDefAdmin_Object=MibTableColumn
moduleDefAdmin=_ModuleDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,26),_ModuleDefAdmin_Type())
moduleDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefAdmin.setStatus(_A)
_ModuleDefScrambling_Type=FspR7Scrambling
_ModuleDefScrambling_Object=MibTableColumn
moduleDefScrambling=_ModuleDefScrambling_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,27),_ModuleDefScrambling_Type())
moduleDefScrambling.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefScrambling.setStatus(_A)
_ModuleDefChannelsNumber_Type=FspR7NumberOfChannels
_ModuleDefChannelsNumber_Object=MibTableColumn
moduleDefChannelsNumber=_ModuleDefChannelsNumber_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,28),_ModuleDefChannelsNumber_Type())
moduleDefChannelsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefChannelsNumber.setStatus(_A)
_ModuleDefChannelSpacingProvision_Type=FspR7ChannelSpacing
_ModuleDefChannelSpacingProvision_Object=MibTableColumn
moduleDefChannelSpacingProvision=_ModuleDefChannelSpacingProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,29),_ModuleDefChannelSpacingProvision_Type())
moduleDefChannelSpacingProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefChannelSpacingProvision.setStatus(_A)
_ModuleDefMode_Type=FspR7TransmissionMode
_ModuleDefMode_Object=MibTableColumn
moduleDefMode=_ModuleDefMode_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,30),_ModuleDefMode_Type())
moduleDefMode.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefMode.setStatus(_A)
_ModuleDefSubBandProvision_Type=FspR7OpticalSubBand
_ModuleDefSubBandProvision_Object=MibTableColumn
moduleDefSubBandProvision=_ModuleDefSubBandProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,31),_ModuleDefSubBandProvision_Type())
moduleDefSubBandProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefSubBandProvision.setStatus(_A)
_ModuleDefAlias_Type=SnmpAdminString
_ModuleDefAlias_Object=MibTableColumn
moduleDefAlias=_ModuleDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,32),_ModuleDefAlias_Type())
moduleDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefAlias.setStatus(_A)
_ModuleDefFiberType_Type=FspR7OpticalFiberType
_ModuleDefFiberType_Object=MibTableColumn
moduleDefFiberType=_ModuleDefFiberType_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,33),_ModuleDefFiberType_Type())
moduleDefFiberType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefFiberType.setStatus(_A)
_ModuleDefChannelSpacing_Type=FspR7ChannelSpacing
_ModuleDefChannelSpacing_Object=MibTableColumn
moduleDefChannelSpacing=_ModuleDefChannelSpacing_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,34),_ModuleDefChannelSpacing_Type())
moduleDefChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefChannelSpacing.setStatus(_A)
_ModuleDefOutputReset_Type=FspR7TifOutputReset
_ModuleDefOutputReset_Object=MibTableColumn
moduleDefOutputReset=_ModuleDefOutputReset_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,35),_ModuleDefOutputReset_Type())
moduleDefOutputReset.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefOutputReset.setStatus(_A)
_ModuleDefRoadmNumber_Type=FspR7RoadmNumber
_ModuleDefRoadmNumber_Object=MibTableColumn
moduleDefRoadmNumber=_ModuleDefRoadmNumber_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,36),_ModuleDefRoadmNumber_Type())
moduleDefRoadmNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefRoadmNumber.setStatus(_A)
_ModuleDefTopology_Type=FspR7Topology
_ModuleDefTopology_Object=MibTableColumn
moduleDefTopology=_ModuleDefTopology_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,37),_ModuleDefTopology_Type())
moduleDefTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefTopology.setStatus(_A)
_ModuleDefForceConfig_Type=FspR7ForceConfig
_ModuleDefForceConfig_Object=MibTableColumn
moduleDefForceConfig=_ModuleDefForceConfig_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,38),_ModuleDefForceConfig_Type())
moduleDefForceConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefForceConfig.setStatus(_A)
_ModuleDefMuxMethod_Type=FspR7MuxMethod
_ModuleDefMuxMethod_Object=MibTableColumn
moduleDefMuxMethod=_ModuleDefMuxMethod_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,39),_ModuleDefMuxMethod_Type())
moduleDefMuxMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefMuxMethod.setStatus(_A)
_ModuleDefNdpCleanup_Type=FspR7NdpCleanup
_ModuleDefNdpCleanup_Object=MibTableColumn
moduleDefNdpCleanup=_ModuleDefNdpCleanup_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,40),_ModuleDefNdpCleanup_Type())
moduleDefNdpCleanup.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefNdpCleanup.setStatus(_A)
_ModuleDefRstp_Type=FspR7EnableDisable
_ModuleDefRstp_Object=MibTableColumn
moduleDefRstp=_ModuleDefRstp_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,41),_ModuleDefRstp_Type())
moduleDefRstp.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefRstp.setStatus(_A)
_ModuleDefRemoteReset_Type=FspR7RlsMan
_ModuleDefRemoteReset_Object=MibTableColumn
moduleDefRemoteReset=_ModuleDefRemoteReset_Object((1,3,6,1,4,1,2544,1,11,10,3,3,7,1,42),_ModuleDefRemoteReset_Type())
moduleDefRemoteReset.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleDefRemoteReset.setStatus(_A)
_EndOfModuleDefTable_Type=Integer32
_EndOfModuleDefTable_Object=MibScalar
endOfModuleDefTable=_EndOfModuleDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,3,8),_EndOfModuleDefTable_Type())
endOfModuleDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfModuleDefTable.setStatus(_A)
_EndOfEqptMgmtDef_Type=Integer32
_EndOfEqptMgmtDef_Object=MibScalar
endOfEqptMgmtDef=_EndOfEqptMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,3,10000),_EndOfEqptMgmtDef_Type())
endOfEqptMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEqptMgmtDef.setStatus(_A)
_FacilityMgmtDef_ObjectIdentity=ObjectIdentity
facilityMgmtDef=_FacilityMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,4))
_PhysicalPortDefTable_Object=MibTable
physicalPortDefTable=_PhysicalPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1))
if mibBuilder.loadTexts:physicalPortDefTable.setStatus(_A)
_PhysicalPortDefEntry_Object=MibTableRow
physicalPortDefEntry=_PhysicalPortDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1))
physicalPortDefEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_S),(0,_C,_R),(0,_C,_Q))
if mibBuilder.loadTexts:physicalPortDefEntry.setStatus(_A)
_PhysicalPortDefRowStatus_Type=RowStatus
_PhysicalPortDefRowStatus_Object=MibTableColumn
physicalPortDefRowStatus=_PhysicalPortDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,1),_PhysicalPortDefRowStatus_Type())
physicalPortDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefRowStatus.setStatus(_A)
_PhysicalPortDefType_Type=FspR7InterfaceType
_PhysicalPortDefType_Object=MibTableColumn
physicalPortDefType=_PhysicalPortDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,2),_PhysicalPortDefType_Type())
physicalPortDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefType.setStatus(_A)
_PhysicalPortDefAdmin_Type=FspR7AdminState
_PhysicalPortDefAdmin_Object=MibTableColumn
physicalPortDefAdmin=_PhysicalPortDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,3),_PhysicalPortDefAdmin_Type())
physicalPortDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefAdmin.setStatus(_A)
_PhysicalPortDefAlias_Type=SnmpAdminString
_PhysicalPortDefAlias_Object=MibTableColumn
physicalPortDefAlias=_PhysicalPortDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,4),_PhysicalPortDefAlias_Type())
physicalPortDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefAlias.setStatus(_A)
_PhysicalPortDefAlsMode_Type=FspR7AlsMode
_PhysicalPortDefAlsMode_Object=MibTableColumn
physicalPortDefAlsMode=_PhysicalPortDefAlsMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,5),_PhysicalPortDefAlsMode_Type())
physicalPortDefAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefAlsMode.setStatus(_A)
_PhysicalPortDefAutoThresReset_Type=FspR7AutoThresReset
_PhysicalPortDefAutoThresReset_Object=MibTableColumn
physicalPortDefAutoThresReset=_PhysicalPortDefAutoThresReset_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,6),_PhysicalPortDefAutoThresReset_Type())
physicalPortDefAutoThresReset.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefAutoThresReset.setStatus(_A)
_PhysicalPortDefAutonegotiation_Type=EnableState
_PhysicalPortDefAutonegotiation_Object=MibTableColumn
physicalPortDefAutonegotiation=_PhysicalPortDefAutonegotiation_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,7),_PhysicalPortDefAutonegotiation_Type())
physicalPortDefAutonegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefAutonegotiation.setStatus(_A)
_PhysicalPortDefBehaviour_Type=FspR7PortBehaviour
_PhysicalPortDefBehaviour_Object=MibTableColumn
physicalPortDefBehaviour=_PhysicalPortDefBehaviour_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,8),_PhysicalPortDefBehaviour_Type())
physicalPortDefBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefBehaviour.setStatus(_A)
_PhysicalPortDefDispertionConfig_Type=FspR7DispersionConfig
_PhysicalPortDefDispertionConfig_Object=MibTableColumn
physicalPortDefDispertionConfig=_PhysicalPortDefDispertionConfig_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,9),_PhysicalPortDefDispertionConfig_Type())
physicalPortDefDispertionConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefDispertionConfig.setStatus(_A)
class _PhysicalPortDefDispersionSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50000,50000))
_PhysicalPortDefDispersionSetting_Type.__name__=_G
_PhysicalPortDefDispersionSetting_Object=MibTableColumn
physicalPortDefDispersionSetting=_PhysicalPortDefDispersionSetting_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,10),_PhysicalPortDefDispersionSetting_Type())
physicalPortDefDispersionSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefDispersionSetting.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefDispersionSetting.setUnits(_c)
_PhysicalPortDefDispersionMode_Type=FspR7DispersionModes
_PhysicalPortDefDispersionMode_Object=MibTableColumn
physicalPortDefDispersionMode=_PhysicalPortDefDispersionMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,11),_PhysicalPortDefDispersionMode_Type())
physicalPortDefDispersionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefDispersionMode.setStatus(_A)
_PhysicalPortDefChannelProv_Type=FspR7ChannelIdentifier
_PhysicalPortDefChannelProv_Object=MibTableColumn
physicalPortDefChannelProv=_PhysicalPortDefChannelProv_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,12),_PhysicalPortDefChannelProv_Type())
physicalPortDefChannelProv.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefChannelProv.setStatus(_A)
_PhysicalPortDefWdmRxChannel_Type=FspR7ChannelIdentifier
_PhysicalPortDefWdmRxChannel_Object=MibTableColumn
physicalPortDefWdmRxChannel=_PhysicalPortDefWdmRxChannel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,13),_PhysicalPortDefWdmRxChannel_Type())
physicalPortDefWdmRxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefWdmRxChannel.setStatus(_A)
_PhysicalPortDefCodeGain_Type=FspR7CodeGain
_PhysicalPortDefCodeGain_Object=MibTableColumn
physicalPortDefCodeGain=_PhysicalPortDefCodeGain_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,14),_PhysicalPortDefCodeGain_Type())
physicalPortDefCodeGain.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefCodeGain.setStatus(_A)
_PhysicalPortDefXfpDecisionThres_Type=FspR7XfpDecisionThres
_PhysicalPortDefXfpDecisionThres_Object=MibTableColumn
physicalPortDefXfpDecisionThres=_PhysicalPortDefXfpDecisionThres_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,15),_PhysicalPortDefXfpDecisionThres_Type())
physicalPortDefXfpDecisionThres.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefXfpDecisionThres.setStatus(_A)
_PhysicalPortDefDisparityCorrection_Type=EnableState
_PhysicalPortDefDisparityCorrection_Object=MibTableColumn
physicalPortDefDisparityCorrection=_PhysicalPortDefDisparityCorrection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,16),_PhysicalPortDefDisparityCorrection_Type())
physicalPortDefDisparityCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefDisparityCorrection.setStatus(_A)
_PhysicalPortDefEqlzAdmin_Type=FspR7EqlzAdminState
_PhysicalPortDefEqlzAdmin_Object=MibTableColumn
physicalPortDefEqlzAdmin=_PhysicalPortDefEqlzAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,17),_PhysicalPortDefEqlzAdmin_Type())
physicalPortDefEqlzAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefEqlzAdmin.setStatus(_A)
_PhysicalPortDefErrorForwarding_Type=FspR7ErrorFwdMode
_PhysicalPortDefErrorForwarding_Object=MibTableColumn
physicalPortDefErrorForwarding=_PhysicalPortDefErrorForwarding_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,18),_PhysicalPortDefErrorForwarding_Type())
physicalPortDefErrorForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefErrorForwarding.setStatus(_A)
_PhysicalPortDefFecType_Type=FspR7FecType
_PhysicalPortDefFecType_Object=MibTableColumn
physicalPortDefFecType=_PhysicalPortDefFecType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,19),_PhysicalPortDefFecType_Type())
physicalPortDefFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefFecType.setStatus(_A)
_PhysicalPortDefFarEndCommunication_Type=FspR7YesNo
_PhysicalPortDefFarEndCommunication_Object=MibTableColumn
physicalPortDefFarEndCommunication=_PhysicalPortDefFarEndCommunication_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,20),_PhysicalPortDefFarEndCommunication_Type())
physicalPortDefFarEndCommunication.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefFarEndCommunication.setStatus(_A)
_PhysicalPortDefFlowControl_Type=FspR7FlowControlMode
_PhysicalPortDefFlowControl_Object=MibTableColumn
physicalPortDefFlowControl=_PhysicalPortDefFlowControl_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,21),_PhysicalPortDefFlowControl_Type())
physicalPortDefFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefFlowControl.setStatus(_A)
_PhysicalPortDefForceLaserOn_Type=FspR7LaserForcedOperation
_PhysicalPortDefForceLaserOn_Object=MibTableColumn
physicalPortDefForceLaserOn=_PhysicalPortDefForceLaserOn_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,22),_PhysicalPortDefForceLaserOn_Type())
physicalPortDefForceLaserOn.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefForceLaserOn.setStatus(_A)
_PhysicalPortDefInhibitSwitchToProt_Type=FspR7YesNo
_PhysicalPortDefInhibitSwitchToProt_Object=MibTableColumn
physicalPortDefInhibitSwitchToProt=_PhysicalPortDefInhibitSwitchToProt_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,23),_PhysicalPortDefInhibitSwitchToProt_Type())
physicalPortDefInhibitSwitchToProt.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefInhibitSwitchToProt.setStatus(_A)
_PhysicalPortDefInhibitSwitchToWork_Type=FspR7YesNo
_PhysicalPortDefInhibitSwitchToWork_Object=MibTableColumn
physicalPortDefInhibitSwitchToWork=_PhysicalPortDefInhibitSwitchToWork_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,24),_PhysicalPortDefInhibitSwitchToWork_Type())
physicalPortDefInhibitSwitchToWork.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefInhibitSwitchToWork.setStatus(_A)
_PhysicalPortDefLaneChannelSetting_Type=FspR7ChannelIdentifier
_PhysicalPortDefLaneChannelSetting_Object=MibTableColumn
physicalPortDefLaneChannelSetting=_PhysicalPortDefLaneChannelSetting_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,25),_PhysicalPortDefLaneChannelSetting_Type())
physicalPortDefLaneChannelSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLaneChannelSetting.setStatus(_A)
_PhysicalPortDefLoopConfig_Type=LoopConfig
_PhysicalPortDefLoopConfig_Object=MibTableColumn
physicalPortDefLoopConfig=_PhysicalPortDefLoopConfig_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,26),_PhysicalPortDefLoopConfig_Type())
physicalPortDefLoopConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLoopConfig.setStatus(_A)
_PhysicalPortDefLaserDelayTimer_Type=FspR7LaserDelayTimer
_PhysicalPortDefLaserDelayTimer_Object=MibTableColumn
physicalPortDefLaserDelayTimer=_PhysicalPortDefLaserDelayTimer_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,27),_PhysicalPortDefLaserDelayTimer_Type())
physicalPortDefLaserDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLaserDelayTimer.setStatus(_A)
class _PhysicalPortDefLaserOffTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_PhysicalPortDefLaserOffTimer_Type.__name__=_D
_PhysicalPortDefLaserOffTimer_Object=MibTableColumn
physicalPortDefLaserOffTimer=_PhysicalPortDefLaserOffTimer_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,28),_PhysicalPortDefLaserOffTimer_Type())
physicalPortDefLaserOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLaserOffTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefLaserOffTimer.setUnits(_V)
class _PhysicalPortDefLaserOnTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_PhysicalPortDefLaserOnTimer_Type.__name__=_D
_PhysicalPortDefLaserOnTimer_Object=MibTableColumn
physicalPortDefLaserOnTimer=_PhysicalPortDefLaserOnTimer_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,29),_PhysicalPortDefLaserOnTimer_Type())
physicalPortDefLaserOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLaserOnTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefLaserOnTimer.setUnits(_V)
_PhysicalPortDefLaserOffDelayFunction_Type=EnableState
_PhysicalPortDefLaserOffDelayFunction_Object=MibTableColumn
physicalPortDefLaserOffDelayFunction=_PhysicalPortDefLaserOffDelayFunction_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,30),_PhysicalPortDefLaserOffDelayFunction_Type())
physicalPortDefLaserOffDelayFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLaserOffDelayFunction.setStatus(_A)
_PhysicalPortDefAutoPTassignment_Type=FspR7ManualAuto
_PhysicalPortDefAutoPTassignment_Object=MibTableColumn
physicalPortDefAutoPTassignment=_PhysicalPortDefAutoPTassignment_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,31),_PhysicalPortDefAutoPTassignment_Type())
physicalPortDefAutoPTassignment.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefAutoPTassignment.setStatus(_A)
_PhysicalPortDefTributarySlotMethod_Type=FspR7ManualAuto
_PhysicalPortDefTributarySlotMethod_Object=MibTableColumn
physicalPortDefTributarySlotMethod=_PhysicalPortDefTributarySlotMethod_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,32),_PhysicalPortDefTributarySlotMethod_Type())
physicalPortDefTributarySlotMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTributarySlotMethod.setStatus(_A)
_PhysicalPortDefInitiateEqualization_Type=FspR7InitEqualization
_PhysicalPortDefInitiateEqualization_Object=MibTableColumn
physicalPortDefInitiateEqualization=_PhysicalPortDefInitiateEqualization_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,33),_PhysicalPortDefInitiateEqualization_Type())
physicalPortDefInitiateEqualization.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefInitiateEqualization.setStatus(_A)
_PhysicalPortDefLossAttenuation_Type=FspR7LossAttenuation
_PhysicalPortDefLossAttenuation_Object=MibTableColumn
physicalPortDefLossAttenuation=_PhysicalPortDefLossAttenuation_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,34),_PhysicalPortDefLossAttenuation_Type())
physicalPortDefLossAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLossAttenuation.setStatus(_A)
class _PhysicalPortDefOpticalSetPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,50))
_PhysicalPortDefOpticalSetPoint_Type.__name__=_G
_PhysicalPortDefOpticalSetPoint_Object=MibTableColumn
physicalPortDefOpticalSetPoint=_PhysicalPortDefOpticalSetPoint_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,35),_PhysicalPortDefOpticalSetPoint_Type())
physicalPortDefOpticalSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefOpticalSetPoint.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefOpticalSetPoint.setUnits(_J)
_PhysicalPortDefDataLayerPmReset_Type=FspR7PmReset
_PhysicalPortDefDataLayerPmReset_Object=MibTableColumn
physicalPortDefDataLayerPmReset=_PhysicalPortDefDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,36),_PhysicalPortDefDataLayerPmReset_Type())
physicalPortDefDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefDataLayerPmReset.setStatus(_A)
_PhysicalPortDefPrbsPmReset_Type=FspR7PrbsPmReset
_PhysicalPortDefPrbsPmReset_Object=MibTableColumn
physicalPortDefPrbsPmReset=_PhysicalPortDefPrbsPmReset_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,37),_PhysicalPortDefPrbsPmReset_Type())
physicalPortDefPrbsPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefPrbsPmReset.setStatus(_A)
_PhysicalPortDefTestPrbsRcvMode_Type=FspR7PRBSTest
_PhysicalPortDefTestPrbsRcvMode_Object=MibTableColumn
physicalPortDefTestPrbsRcvMode=_PhysicalPortDefTestPrbsRcvMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,38),_PhysicalPortDefTestPrbsRcvMode_Type())
physicalPortDefTestPrbsRcvMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTestPrbsRcvMode.setStatus(_A)
_PhysicalPortDefTestPrbsTrmtMode_Type=FspR7PRBSTest
_PhysicalPortDefTestPrbsTrmtMode_Object=MibTableColumn
physicalPortDefTestPrbsTrmtMode=_PhysicalPortDefTestPrbsTrmtMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,39),_PhysicalPortDefTestPrbsTrmtMode_Type())
physicalPortDefTestPrbsTrmtMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTestPrbsTrmtMode.setStatus(_A)
_PhysicalPortDefSwitchCommand_Type=FspR7APSCommand
_PhysicalPortDefSwitchCommand_Object=MibTableColumn
physicalPortDefSwitchCommand=_PhysicalPortDefSwitchCommand_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,40),_PhysicalPortDefSwitchCommand_Type())
physicalPortDefSwitchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSwitchCommand.setStatus(_A)
_PhysicalPortDefOpuPayloadType_Type=FspR7OpuPayloadType
_PhysicalPortDefOpuPayloadType_Object=MibTableColumn
physicalPortDefOpuPayloadType=_PhysicalPortDefOpuPayloadType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,41),_PhysicalPortDefOpuPayloadType_Type())
physicalPortDefOpuPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefOpuPayloadType.setStatus(_A)
_PhysicalPortDefSigDegThresSonetLine_Type=FspR7BERThreshold
_PhysicalPortDefSigDegThresSonetLine_Object=MibTableColumn
physicalPortDefSigDegThresSonetLine=_PhysicalPortDefSigDegThresSonetLine_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,42),_PhysicalPortDefSigDegThresSonetLine_Type())
physicalPortDefSigDegThresSonetLine.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresSonetLine.setStatus(_A)
class _PhysicalPortDefSigDegThresSdhMs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresSdhMs_Type.__name__=_D
_PhysicalPortDefSigDegThresSdhMs_Object=MibTableColumn
physicalPortDefSigDegThresSdhMs=_PhysicalPortDefSigDegThresSdhMs_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,43),_PhysicalPortDefSigDegThresSdhMs_Type())
physicalPortDefSigDegThresSdhMs.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresSdhMs.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresSdhMs.setUnits(_H)
class _PhysicalPortDefSigDegThresOtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresOtu_Type.__name__=_G
_PhysicalPortDefSigDegThresOtu_Object=MibTableColumn
physicalPortDefSigDegThresOtu=_PhysicalPortDefSigDegThresOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,44),_PhysicalPortDefSigDegThresOtu_Type())
physicalPortDefSigDegThresOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOtu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOtu.setUnits(_H)
class _PhysicalPortDefSigDegThresOdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresOdu_Type.__name__=_G
_PhysicalPortDefSigDegThresOdu_Object=MibTableColumn
physicalPortDefSigDegThresOdu=_PhysicalPortDefSigDegThresOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,45),_PhysicalPortDefSigDegThresOdu_Type())
physicalPortDefSigDegThresOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOdu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOdu.setUnits(_H)
class _PhysicalPortDefSigDegThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_PhysicalPortDefSigDegThreshold_Type.__name__=_D
_PhysicalPortDefSigDegThreshold_Object=MibTableColumn
physicalPortDefSigDegThreshold=_PhysicalPortDefSigDegThreshold_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,46),_PhysicalPortDefSigDegThreshold_Type())
physicalPortDefSigDegThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThreshold.setStatus(_A)
class _PhysicalPortDefSigDegPcslThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegPcslThreshold_Type.__name__=_D
_PhysicalPortDefSigDegPcslThreshold_Object=MibTableColumn
physicalPortDefSigDegPcslThreshold=_PhysicalPortDefSigDegPcslThreshold_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,47),_PhysicalPortDefSigDegPcslThreshold_Type())
physicalPortDefSigDegPcslThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPcslThreshold.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPcslThreshold.setUnits(_H)
_PhysicalPortDefSigDegThresSonetSection_Type=FspR7BERThresholdSection
_PhysicalPortDefSigDegThresSonetSection_Object=MibTableColumn
physicalPortDefSigDegThresSonetSection=_PhysicalPortDefSigDegThresSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,48),_PhysicalPortDefSigDegThresSonetSection_Type())
physicalPortDefSigDegThresSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresSonetSection.setStatus(_A)
class _PhysicalPortDefSigDegThresSdhSection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresSdhSection_Type.__name__=_D
_PhysicalPortDefSigDegThresSdhSection_Object=MibTableColumn
physicalPortDefSigDegThresSdhSection=_PhysicalPortDefSigDegThresSdhSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,49),_PhysicalPortDefSigDegThresSdhSection_Type())
physicalPortDefSigDegThresSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresSdhSection.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresSdhSection.setUnits(_H)
class _PhysicalPortDefSigDegThresOduTcmA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresOduTcmA_Type.__name__=_G
_PhysicalPortDefSigDegThresOduTcmA_Object=MibTableColumn
physicalPortDefSigDegThresOduTcmA=_PhysicalPortDefSigDegThresOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,50),_PhysicalPortDefSigDegThresOduTcmA_Type())
physicalPortDefSigDegThresOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOduTcmA.setUnits(_H)
class _PhysicalPortDefSigDegThresOduTcmB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresOduTcmB_Type.__name__=_G
_PhysicalPortDefSigDegThresOduTcmB_Object=MibTableColumn
physicalPortDefSigDegThresOduTcmB=_PhysicalPortDefSigDegThresOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,51),_PhysicalPortDefSigDegThresOduTcmB_Type())
physicalPortDefSigDegThresOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOduTcmB.setUnits(_H)
class _PhysicalPortDefSigDegThresOduTcmC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PhysicalPortDefSigDegThresOduTcmC_Type.__name__=_G
_PhysicalPortDefSigDegThresOduTcmC_Object=MibTableColumn
physicalPortDefSigDegThresOduTcmC=_PhysicalPortDefSigDegThresOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,52),_PhysicalPortDefSigDegThresOduTcmC_Type())
physicalPortDefSigDegThresOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegThresOduTcmC.setUnits(_H)
class _PhysicalPortDefSignalDegradePeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSignalDegradePeriod_Type.__name__=_D
_PhysicalPortDefSignalDegradePeriod_Object=MibTableColumn
physicalPortDefSignalDegradePeriod=_PhysicalPortDefSignalDegradePeriod_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,53),_PhysicalPortDefSignalDegradePeriod_Type())
physicalPortDefSignalDegradePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSignalDegradePeriod.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSignalDegradePeriod.setUnits(_I)
class _PhysicalPortDefSigDegPeriodOdu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSigDegPeriodOdu_Type.__name__=_D
_PhysicalPortDefSigDegPeriodOdu_Object=MibTableColumn
physicalPortDefSigDegPeriodOdu=_PhysicalPortDefSigDegPeriodOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,54),_PhysicalPortDefSigDegPeriodOdu_Type())
physicalPortDefSigDegPeriodOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOdu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOdu.setUnits(_I)
class _PhysicalPortDefSigDegPeriodOtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSigDegPeriodOtu_Type.__name__=_D
_PhysicalPortDefSigDegPeriodOtu_Object=MibTableColumn
physicalPortDefSigDegPeriodOtu=_PhysicalPortDefSigDegPeriodOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,55),_PhysicalPortDefSigDegPeriodOtu_Type())
physicalPortDefSigDegPeriodOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOtu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOtu.setUnits(_I)
class _PhysicalPortDefSigDegPeriodIntegration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_PhysicalPortDefSigDegPeriodIntegration_Type.__name__=_D
_PhysicalPortDefSigDegPeriodIntegration_Object=MibTableColumn
physicalPortDefSigDegPeriodIntegration=_PhysicalPortDefSigDegPeriodIntegration_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,56),_PhysicalPortDefSigDegPeriodIntegration_Type())
physicalPortDefSigDegPeriodIntegration.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodIntegration.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodIntegration.setUnits(_I)
class _PhysicalPortDefSigDegPeriodSdhSection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSigDegPeriodSdhSection_Type.__name__=_D
_PhysicalPortDefSigDegPeriodSdhSection_Object=MibTableColumn
physicalPortDefSigDegPeriodSdhSection=_PhysicalPortDefSigDegPeriodSdhSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,57),_PhysicalPortDefSigDegPeriodSdhSection_Type())
physicalPortDefSigDegPeriodSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodSdhSection.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodSdhSection.setUnits(_I)
class _PhysicalPortDefSigDegPeriodOduTcmA_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSigDegPeriodOduTcmA_Type.__name__=_D
_PhysicalPortDefSigDegPeriodOduTcmA_Object=MibTableColumn
physicalPortDefSigDegPeriodOduTcmA=_PhysicalPortDefSigDegPeriodOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,58),_PhysicalPortDefSigDegPeriodOduTcmA_Type())
physicalPortDefSigDegPeriodOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOduTcmA.setUnits(_I)
class _PhysicalPortDefSigDegPeriodOduTcmB_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSigDegPeriodOduTcmB_Type.__name__=_D
_PhysicalPortDefSigDegPeriodOduTcmB_Object=MibTableColumn
physicalPortDefSigDegPeriodOduTcmB=_PhysicalPortDefSigDegPeriodOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,59),_PhysicalPortDefSigDegPeriodOduTcmB_Type())
physicalPortDefSigDegPeriodOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOduTcmB.setUnits(_I)
class _PhysicalPortDefSigDegPeriodOduTcmC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PhysicalPortDefSigDegPeriodOduTcmC_Type.__name__=_D
_PhysicalPortDefSigDegPeriodOduTcmC_Object=MibTableColumn
physicalPortDefSigDegPeriodOduTcmC=_PhysicalPortDefSigDegPeriodOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,60),_PhysicalPortDefSigDegPeriodOduTcmC_Type())
physicalPortDefSigDegPeriodOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefSigDegPeriodOduTcmC.setUnits(_I)
_PhysicalPortDefOtnStuffing_Type=FspR7Stuff
_PhysicalPortDefOtnStuffing_Object=MibTableColumn
physicalPortDefOtnStuffing=_PhysicalPortDefOtnStuffing_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,61),_PhysicalPortDefOtnStuffing_Type())
physicalPortDefOtnStuffing.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefOtnStuffing.setStatus(_A)
_PhysicalPortDefTcmALevel_Type=OtnTcmLevel
_PhysicalPortDefTcmALevel_Object=MibTableColumn
physicalPortDefTcmALevel=_PhysicalPortDefTcmALevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,62),_PhysicalPortDefTcmALevel_Type())
physicalPortDefTcmALevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTcmALevel.setStatus(_A)
_PhysicalPortDefTcmBLevel_Type=OtnTcmLevel
_PhysicalPortDefTcmBLevel_Object=MibTableColumn
physicalPortDefTcmBLevel=_PhysicalPortDefTcmBLevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,63),_PhysicalPortDefTcmBLevel_Type())
physicalPortDefTcmBLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTcmBLevel.setStatus(_A)
_PhysicalPortDefTcmCLevel_Type=OtnTcmLevel
_PhysicalPortDefTcmCLevel_Object=MibTableColumn
physicalPortDefTcmCLevel=_PhysicalPortDefTcmCLevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,64),_PhysicalPortDefTcmCLevel_Type())
physicalPortDefTcmCLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTcmCLevel.setStatus(_A)
_PhysicalPortDefTerminationLevel_Type=OhTerminationLevel
_PhysicalPortDefTerminationLevel_Object=MibTableColumn
physicalPortDefTerminationLevel=_PhysicalPortDefTerminationLevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,65),_PhysicalPortDefTerminationLevel_Type())
physicalPortDefTerminationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTerminationLevel.setStatus(_A)
_PhysicalPortDefTimingSource_Type=SonetTimingSource
_PhysicalPortDefTimingSource_Object=MibTableColumn
physicalPortDefTimingSource=_PhysicalPortDefTimingSource_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,66),_PhysicalPortDefTimingSource_Type())
physicalPortDefTimingSource.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimingSource.setStatus(_A)
_PhysicalPortDefTimModeOdu_Type=TimMode
_PhysicalPortDefTimModeOdu_Object=MibTableColumn
physicalPortDefTimModeOdu=_PhysicalPortDefTimModeOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,67),_PhysicalPortDefTimModeOdu_Type())
physicalPortDefTimModeOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimModeOdu.setStatus(_A)
_PhysicalPortDefTimModeOtu_Type=TimMode
_PhysicalPortDefTimModeOtu_Object=MibTableColumn
physicalPortDefTimModeOtu=_PhysicalPortDefTimModeOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,68),_PhysicalPortDefTimModeOtu_Type())
physicalPortDefTimModeOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimModeOtu.setStatus(_A)
_PhysicalPortDefTimModeSonetSection_Type=TimMode
_PhysicalPortDefTimModeSonetSection_Object=MibTableColumn
physicalPortDefTimModeSonetSection=_PhysicalPortDefTimModeSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,69),_PhysicalPortDefTimModeSonetSection_Type())
physicalPortDefTimModeSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimModeSonetSection.setStatus(_A)
_PhysicalPortDefTimModeOduTcmA_Type=TimMode
_PhysicalPortDefTimModeOduTcmA_Object=MibTableColumn
physicalPortDefTimModeOduTcmA=_PhysicalPortDefTimModeOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,70),_PhysicalPortDefTimModeOduTcmA_Type())
physicalPortDefTimModeOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimModeOduTcmA.setStatus(_A)
_PhysicalPortDefTimModeOduTcmB_Type=TimMode
_PhysicalPortDefTimModeOduTcmB_Object=MibTableColumn
physicalPortDefTimModeOduTcmB=_PhysicalPortDefTimModeOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,71),_PhysicalPortDefTimModeOduTcmB_Type())
physicalPortDefTimModeOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimModeOduTcmB.setStatus(_A)
_PhysicalPortDefTimModeOduTcmC_Type=TimMode
_PhysicalPortDefTimModeOduTcmC_Object=MibTableColumn
physicalPortDefTimModeOduTcmC=_PhysicalPortDefTimModeOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,72),_PhysicalPortDefTimModeOduTcmC_Type())
physicalPortDefTimModeOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTimModeOduTcmC.setStatus(_A)
_PhysicalPortDefTraceFormSonetSection_Type=SonetTraceForm
_PhysicalPortDefTraceFormSonetSection_Object=MibTableColumn
physicalPortDefTraceFormSonetSection=_PhysicalPortDefTraceFormSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,73),_PhysicalPortDefTraceFormSonetSection_Type())
physicalPortDefTraceFormSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceFormSonetSection.setStatus(_A)
class _PhysicalPortDefTraceExpectedSonetSection_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_PhysicalPortDefTraceExpectedSonetSection_Type.__name__=_E
_PhysicalPortDefTraceExpectedSonetSection_Object=MibTableColumn
physicalPortDefTraceExpectedSonetSection=_PhysicalPortDefTraceExpectedSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,74),_PhysicalPortDefTraceExpectedSonetSection_Type())
physicalPortDefTraceExpectedSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceExpectedSonetSection.setStatus(_A)
class _PhysicalPortDefTraceTransmitSonetSection_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_PhysicalPortDefTraceTransmitSonetSection_Type.__name__=_E
_PhysicalPortDefTraceTransmitSonetSection_Object=MibTableColumn
physicalPortDefTraceTransmitSonetSection=_PhysicalPortDefTraceTransmitSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,75),_PhysicalPortDefTraceTransmitSonetSection_Type())
physicalPortDefTraceTransmitSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitSonetSection.setStatus(_A)
class _PhysicalPortDefTraceExpectedOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceExpectedOtu_Type.__name__=_E
_PhysicalPortDefTraceExpectedOtu_Object=MibTableColumn
physicalPortDefTraceExpectedOtu=_PhysicalPortDefTraceExpectedOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,76),_PhysicalPortDefTraceExpectedOtu_Type())
physicalPortDefTraceExpectedOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceExpectedOtu.setStatus(_A)
class _PhysicalPortDefTraceTransmitSapiOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitSapiOtu_Type.__name__=_E
_PhysicalPortDefTraceTransmitSapiOtu_Object=MibTableColumn
physicalPortDefTraceTransmitSapiOtu=_PhysicalPortDefTraceTransmitSapiOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,77),_PhysicalPortDefTraceTransmitSapiOtu_Type())
physicalPortDefTraceTransmitSapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitSapiOtu.setStatus(_A)
class _PhysicalPortDefTraceTransmitDapiOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitDapiOtu_Type.__name__=_E
_PhysicalPortDefTraceTransmitDapiOtu_Object=MibTableColumn
physicalPortDefTraceTransmitDapiOtu=_PhysicalPortDefTraceTransmitDapiOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,78),_PhysicalPortDefTraceTransmitDapiOtu_Type())
physicalPortDefTraceTransmitDapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitDapiOtu.setStatus(_A)
class _PhysicalPortDefTraceTransmitOpspOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PhysicalPortDefTraceTransmitOpspOtu_Type.__name__=_E
_PhysicalPortDefTraceTransmitOpspOtu_Object=MibTableColumn
physicalPortDefTraceTransmitOpspOtu=_PhysicalPortDefTraceTransmitOpspOtu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,79),_PhysicalPortDefTraceTransmitOpspOtu_Type())
physicalPortDefTraceTransmitOpspOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitOpspOtu.setStatus(_A)
class _PhysicalPortDefTraceExpectedOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceExpectedOdu_Type.__name__=_E
_PhysicalPortDefTraceExpectedOdu_Object=MibTableColumn
physicalPortDefTraceExpectedOdu=_PhysicalPortDefTraceExpectedOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,80),_PhysicalPortDefTraceExpectedOdu_Type())
physicalPortDefTraceExpectedOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceExpectedOdu.setStatus(_A)
class _PhysicalPortDefTraceTransmitSapiOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitSapiOdu_Type.__name__=_E
_PhysicalPortDefTraceTransmitSapiOdu_Object=MibTableColumn
physicalPortDefTraceTransmitSapiOdu=_PhysicalPortDefTraceTransmitSapiOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,81),_PhysicalPortDefTraceTransmitSapiOdu_Type())
physicalPortDefTraceTransmitSapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitSapiOdu.setStatus(_A)
class _PhysicalPortDefTraceTransmitDapiOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitDapiOdu_Type.__name__=_E
_PhysicalPortDefTraceTransmitDapiOdu_Object=MibTableColumn
physicalPortDefTraceTransmitDapiOdu=_PhysicalPortDefTraceTransmitDapiOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,82),_PhysicalPortDefTraceTransmitDapiOdu_Type())
physicalPortDefTraceTransmitDapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitDapiOdu.setStatus(_A)
class _PhysicalPortDefTraceTransmitOpspOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PhysicalPortDefTraceTransmitOpspOdu_Type.__name__=_E
_PhysicalPortDefTraceTransmitOpspOdu_Object=MibTableColumn
physicalPortDefTraceTransmitOpspOdu=_PhysicalPortDefTraceTransmitOpspOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,83),_PhysicalPortDefTraceTransmitOpspOdu_Type())
physicalPortDefTraceTransmitOpspOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitOpspOdu.setStatus(_A)
class _PhysicalPortDefTraceExpectedOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceExpectedOduTcmA_Type.__name__=_E
_PhysicalPortDefTraceExpectedOduTcmA_Object=MibTableColumn
physicalPortDefTraceExpectedOduTcmA=_PhysicalPortDefTraceExpectedOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,84),_PhysicalPortDefTraceExpectedOduTcmA_Type())
physicalPortDefTraceExpectedOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceExpectedOduTcmA.setStatus(_A)
class _PhysicalPortDefTraceTransmitSapiOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitSapiOduTcmA_Type.__name__=_E
_PhysicalPortDefTraceTransmitSapiOduTcmA_Object=MibTableColumn
physicalPortDefTraceTransmitSapiOduTcmA=_PhysicalPortDefTraceTransmitSapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,85),_PhysicalPortDefTraceTransmitSapiOduTcmA_Type())
physicalPortDefTraceTransmitSapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitSapiOduTcmA.setStatus(_A)
class _PhysicalPortDefTraceTransmitDapiOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitDapiOduTcmA_Type.__name__=_E
_PhysicalPortDefTraceTransmitDapiOduTcmA_Object=MibTableColumn
physicalPortDefTraceTransmitDapiOduTcmA=_PhysicalPortDefTraceTransmitDapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,86),_PhysicalPortDefTraceTransmitDapiOduTcmA_Type())
physicalPortDefTraceTransmitDapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitDapiOduTcmA.setStatus(_A)
class _PhysicalPortDefTraceTransmitOpspOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PhysicalPortDefTraceTransmitOpspOduTcmA_Type.__name__=_E
_PhysicalPortDefTraceTransmitOpspOduTcmA_Object=MibTableColumn
physicalPortDefTraceTransmitOpspOduTcmA=_PhysicalPortDefTraceTransmitOpspOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,87),_PhysicalPortDefTraceTransmitOpspOduTcmA_Type())
physicalPortDefTraceTransmitOpspOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitOpspOduTcmA.setStatus(_A)
class _PhysicalPortDefTraceExpectedOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceExpectedOduTcmB_Type.__name__=_E
_PhysicalPortDefTraceExpectedOduTcmB_Object=MibTableColumn
physicalPortDefTraceExpectedOduTcmB=_PhysicalPortDefTraceExpectedOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,88),_PhysicalPortDefTraceExpectedOduTcmB_Type())
physicalPortDefTraceExpectedOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceExpectedOduTcmB.setStatus(_A)
class _PhysicalPortDefTraceTransmitSapiOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitSapiOduTcmB_Type.__name__=_E
_PhysicalPortDefTraceTransmitSapiOduTcmB_Object=MibTableColumn
physicalPortDefTraceTransmitSapiOduTcmB=_PhysicalPortDefTraceTransmitSapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,89),_PhysicalPortDefTraceTransmitSapiOduTcmB_Type())
physicalPortDefTraceTransmitSapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitSapiOduTcmB.setStatus(_A)
class _PhysicalPortDefTraceTransmitDapiOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitDapiOduTcmB_Type.__name__=_E
_PhysicalPortDefTraceTransmitDapiOduTcmB_Object=MibTableColumn
physicalPortDefTraceTransmitDapiOduTcmB=_PhysicalPortDefTraceTransmitDapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,90),_PhysicalPortDefTraceTransmitDapiOduTcmB_Type())
physicalPortDefTraceTransmitDapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitDapiOduTcmB.setStatus(_A)
class _PhysicalPortDefTraceTransmitOpspOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PhysicalPortDefTraceTransmitOpspOduTcmB_Type.__name__=_E
_PhysicalPortDefTraceTransmitOpspOduTcmB_Object=MibTableColumn
physicalPortDefTraceTransmitOpspOduTcmB=_PhysicalPortDefTraceTransmitOpspOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,91),_PhysicalPortDefTraceTransmitOpspOduTcmB_Type())
physicalPortDefTraceTransmitOpspOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitOpspOduTcmB.setStatus(_A)
class _PhysicalPortDefTraceExpectedOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceExpectedOduTcmC_Type.__name__=_E
_PhysicalPortDefTraceExpectedOduTcmC_Object=MibTableColumn
physicalPortDefTraceExpectedOduTcmC=_PhysicalPortDefTraceExpectedOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,92),_PhysicalPortDefTraceExpectedOduTcmC_Type())
physicalPortDefTraceExpectedOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceExpectedOduTcmC.setStatus(_A)
class _PhysicalPortDefTraceTransmitSapiOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitSapiOduTcmC_Type.__name__=_E
_PhysicalPortDefTraceTransmitSapiOduTcmC_Object=MibTableColumn
physicalPortDefTraceTransmitSapiOduTcmC=_PhysicalPortDefTraceTransmitSapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,93),_PhysicalPortDefTraceTransmitSapiOduTcmC_Type())
physicalPortDefTraceTransmitSapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitSapiOduTcmC.setStatus(_A)
class _PhysicalPortDefTraceTransmitDapiOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PhysicalPortDefTraceTransmitDapiOduTcmC_Type.__name__=_E
_PhysicalPortDefTraceTransmitDapiOduTcmC_Object=MibTableColumn
physicalPortDefTraceTransmitDapiOduTcmC=_PhysicalPortDefTraceTransmitDapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,94),_PhysicalPortDefTraceTransmitDapiOduTcmC_Type())
physicalPortDefTraceTransmitDapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitDapiOduTcmC.setStatus(_A)
class _PhysicalPortDefTraceTransmitOpspOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PhysicalPortDefTraceTransmitOpspOduTcmC_Type.__name__=_E
_PhysicalPortDefTraceTransmitOpspOduTcmC_Object=MibTableColumn
physicalPortDefTraceTransmitOpspOduTcmC=_PhysicalPortDefTraceTransmitOpspOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,95),_PhysicalPortDefTraceTransmitOpspOduTcmC_Type())
physicalPortDefTraceTransmitOpspOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTraceTransmitOpspOduTcmC.setStatus(_A)
_PhysicalPortDefTurnupConfig_Type=FspR7TurnupConfig
_PhysicalPortDefTurnupConfig_Object=MibTableColumn
physicalPortDefTurnupConfig=_PhysicalPortDefTurnupConfig_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,96),_PhysicalPortDefTurnupConfig_Type())
physicalPortDefTurnupConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTurnupConfig.setStatus(_A)
_PhysicalPortDefTxOffDelay_Type=FspR7EnableDisable
_PhysicalPortDefTxOffDelay_Object=MibTableColumn
physicalPortDefTxOffDelay=_PhysicalPortDefTxOffDelay_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,97),_PhysicalPortDefTxOffDelay_Type())
physicalPortDefTxOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTxOffDelay.setStatus(_A)
_PhysicalPortDefVoaMode_Type=FspR7VoaMode
_PhysicalPortDefVoaMode_Object=MibTableColumn
physicalPortDefVoaMode=_PhysicalPortDefVoaMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,98),_PhysicalPortDefVoaMode_Type())
physicalPortDefVoaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefVoaMode.setStatus(_A)
class _PhysicalPortDefVoaSetpoint_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PhysicalPortDefVoaSetpoint_Type.__name__=_D
_PhysicalPortDefVoaSetpoint_Object=MibTableColumn
physicalPortDefVoaSetpoint=_PhysicalPortDefVoaSetpoint_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,99),_PhysicalPortDefVoaSetpoint_Type())
physicalPortDefVoaSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefVoaSetpoint.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefVoaSetpoint.setUnits(_K)
class _PhysicalPortDefLagPrio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhysicalPortDefLagPrio_Type.__name__=_D
_PhysicalPortDefLagPrio_Object=MibTableColumn
physicalPortDefLagPrio=_PhysicalPortDefLagPrio_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,100),_PhysicalPortDefLagPrio_Type())
physicalPortDefLagPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefLagPrio.setStatus(_A)
class _PhysicalPortDefMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_PhysicalPortDefMaxFrameSize_Type.__name__=_D
_PhysicalPortDefMaxFrameSize_Object=MibTableColumn
physicalPortDefMaxFrameSize=_PhysicalPortDefMaxFrameSize_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,101),_PhysicalPortDefMaxFrameSize_Type())
physicalPortDefMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefMaxFrameSize.setStatus(_A)
_PhysicalPortDefPayload_Type=OtnPayloadType
_PhysicalPortDefPayload_Object=MibTableColumn
physicalPortDefPayload=_PhysicalPortDefPayload_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,102),_PhysicalPortDefPayload_Type())
physicalPortDefPayload.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefPayload.setStatus(_A)
_PhysicalPortDefPortMode_Type=FspR7PortMode
_PhysicalPortDefPortMode_Object=MibTableColumn
physicalPortDefPortMode=_PhysicalPortDefPortMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,103),_PhysicalPortDefPortMode_Type())
physicalPortDefPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefPortMode.setStatus(_A)
_PhysicalPortDefPortRole_Type=FspR7PortRole
_PhysicalPortDefPortRole_Object=MibTableColumn
physicalPortDefPortRole=_PhysicalPortDefPortRole_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,104),_PhysicalPortDefPortRole_Type())
physicalPortDefPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefPortRole.setStatus(_A)
class _PhysicalPortDefPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PhysicalPortDefPriority_Type.__name__=_D
_PhysicalPortDefPriority_Object=MibTableColumn
physicalPortDefPriority=_PhysicalPortDefPriority_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,105),_PhysicalPortDefPriority_Type())
physicalPortDefPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefPriority.setStatus(_A)
class _PhysicalPortDefPvid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_PhysicalPortDefPvid_Type.__name__=_D
_PhysicalPortDefPvid_Object=MibTableColumn
physicalPortDefPvid=_PhysicalPortDefPvid_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,106),_PhysicalPortDefPvid_Type())
physicalPortDefPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefPvid.setStatus(_A)
_PhysicalPortDefStagType_Type=FspR7SnmpHexString
_PhysicalPortDefStagType_Object=MibTableColumn
physicalPortDefStagType=_PhysicalPortDefStagType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,107),_PhysicalPortDefStagType_Type())
physicalPortDefStagType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefStagType.setStatus(_A)
_PhysicalPortDefUtag_Type=FspR7UntaggedFrames
_PhysicalPortDefUtag_Object=MibTableColumn
physicalPortDefUtag=_PhysicalPortDefUtag_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,108),_PhysicalPortDefUtag_Type())
physicalPortDefUtag.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefUtag.setStatus(_A)
_PhysicalPortDefVethAid_Type=SnmpAdminString
_PhysicalPortDefVethAid_Object=MibTableColumn
physicalPortDefVethAid=_PhysicalPortDefVethAid_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,109),_PhysicalPortDefVethAid_Type())
physicalPortDefVethAid.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefVethAid.setStatus(_A)
_PhysicalPortDefRedLineState_Type=FspR7RedLinedState
_PhysicalPortDefRedLineState_Object=MibTableColumn
physicalPortDefRedLineState=_PhysicalPortDefRedLineState_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,110),_PhysicalPortDefRedLineState_Type())
physicalPortDefRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefRedLineState.setStatus(_A)
_PhysicalPortDefTunnelAid_Type=SnmpAdminString
_PhysicalPortDefTunnelAid_Object=MibTableColumn
physicalPortDefTunnelAid=_PhysicalPortDefTunnelAid_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,111),_PhysicalPortDefTunnelAid_Type())
physicalPortDefTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTunnelAid.setStatus(_A)
_PhysicalPortDefRateLimit_Type=FspR7DisableEnable
_PhysicalPortDefRateLimit_Object=MibTableColumn
physicalPortDefRateLimit=_PhysicalPortDefRateLimit_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,112),_PhysicalPortDefRateLimit_Type())
physicalPortDefRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefRateLimit.setStatus(_A)
_PhysicalPortDefTxOffOnTm_Type=FspR7TxOffOnTm
_PhysicalPortDefTxOffOnTm_Object=MibTableColumn
physicalPortDefTxOffOnTm=_PhysicalPortDefTxOffOnTm_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,113),_PhysicalPortDefTxOffOnTm_Type())
physicalPortDefTxOffOnTm.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTxOffOnTm.setStatus(_A)
class _PhysicalPortDefTxOffTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_PhysicalPortDefTxOffTimer_Type.__name__=_D
_PhysicalPortDefTxOffTimer_Object=MibTableColumn
physicalPortDefTxOffTimer=_PhysicalPortDefTxOffTimer_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,114),_PhysicalPortDefTxOffTimer_Type())
physicalPortDefTxOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTxOffTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefTxOffTimer.setUnits(_V)
class _PhysicalPortDefTxOnTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_PhysicalPortDefTxOnTimer_Type.__name__=_D
_PhysicalPortDefTxOnTimer_Object=MibTableColumn
physicalPortDefTxOnTimer=_PhysicalPortDefTxOnTimer_Object((1,3,6,1,4,1,2544,1,11,10,3,4,1,1,115),_PhysicalPortDefTxOnTimer_Type())
physicalPortDefTxOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortDefTxOnTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortDefTxOnTimer.setUnits(_V)
_VirtualPortDefTable_Object=MibTable
virtualPortDefTable=_VirtualPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2))
if mibBuilder.loadTexts:virtualPortDefTable.setStatus(_A)
_VirtualPortDefEntry_Object=MibTableRow
virtualPortDefEntry=_VirtualPortDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1))
virtualPortDefEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_S),(0,_C,_R),(0,_C,_Q))
if mibBuilder.loadTexts:virtualPortDefEntry.setStatus(_A)
_VirtualPortDefRowStatus_Type=RowStatus
_VirtualPortDefRowStatus_Object=MibTableColumn
virtualPortDefRowStatus=_VirtualPortDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,1),_VirtualPortDefRowStatus_Type())
virtualPortDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefRowStatus.setStatus(_A)
_VirtualPortDefChannelBand_Type=FspR7ChannelBandwidth
_VirtualPortDefChannelBand_Object=MibTableColumn
virtualPortDefChannelBand=_VirtualPortDefChannelBand_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,2),_VirtualPortDefChannelBand_Type())
virtualPortDefChannelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefChannelBand.setStatus(_A)
_VirtualPortDefType_Type=FspR7InterfaceType
_VirtualPortDefType_Object=MibTableColumn
virtualPortDefType=_VirtualPortDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,3),_VirtualPortDefType_Type())
virtualPortDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefType.setStatus(_A)
_VirtualPortDefAlias_Type=SnmpAdminString
_VirtualPortDefAlias_Object=MibTableColumn
virtualPortDefAlias=_VirtualPortDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,4),_VirtualPortDefAlias_Type())
virtualPortDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefAlias.setStatus(_A)
_VirtualPortDefAdmin_Type=FspR7AdminState
_VirtualPortDefAdmin_Object=MibTableColumn
virtualPortDefAdmin=_VirtualPortDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,5),_VirtualPortDefAdmin_Type())
virtualPortDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefAdmin.setStatus(_A)
_VirtualPortDefEqlzAdmin_Type=FspR7EqlzAdminState
_VirtualPortDefEqlzAdmin_Object=MibTableColumn
virtualPortDefEqlzAdmin=_VirtualPortDefEqlzAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,6),_VirtualPortDefEqlzAdmin_Type())
virtualPortDefEqlzAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefEqlzAdmin.setStatus(_A)
_VirtualPortDefInitEqlz_Type=FspR7InitEqualization
_VirtualPortDefInitEqlz_Object=MibTableColumn
virtualPortDefInitEqlz=_VirtualPortDefInitEqlz_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,7),_VirtualPortDefInitEqlz_Type())
virtualPortDefInitEqlz.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefInitEqlz.setStatus(_A)
_VirtualPortDefLacpMode_Type=FspR7LacpMode
_VirtualPortDefLacpMode_Object=MibTableColumn
virtualPortDefLacpMode=_VirtualPortDefLacpMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,8),_VirtualPortDefLacpMode_Type())
virtualPortDefLacpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefLacpMode.setStatus(_A)
_VirtualPortDefLacpTimeout_Type=FspR7LacpTimeout
_VirtualPortDefLacpTimeout_Object=MibTableColumn
virtualPortDefLacpTimeout=_VirtualPortDefLacpTimeout_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,9),_VirtualPortDefLacpTimeout_Type())
virtualPortDefLacpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefLacpTimeout.setStatus(_A)
class _VirtualPortDefLagActivePorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_VirtualPortDefLagActivePorts_Type.__name__=_D
_VirtualPortDefLagActivePorts_Object=MibTableColumn
virtualPortDefLagActivePorts=_VirtualPortDefLagActivePorts_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,10),_VirtualPortDefLagActivePorts_Type())
virtualPortDefLagActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefLagActivePorts.setStatus(_A)
class _VirtualPortDefMaxFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_VirtualPortDefMaxFrameSize_Type.__name__=_D
_VirtualPortDefMaxFrameSize_Object=MibTableColumn
virtualPortDefMaxFrameSize=_VirtualPortDefMaxFrameSize_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,11),_VirtualPortDefMaxFrameSize_Type())
virtualPortDefMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefMaxFrameSize.setStatus(_A)
_VirtualPortDefPortMode_Type=FspR7PortMode
_VirtualPortDefPortMode_Object=MibTableColumn
virtualPortDefPortMode=_VirtualPortDefPortMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,12),_VirtualPortDefPortMode_Type())
virtualPortDefPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefPortMode.setStatus(_A)
_VirtualPortDefDataLayerPmReset_Type=FspR7PmReset
_VirtualPortDefDataLayerPmReset_Object=MibTableColumn
virtualPortDefDataLayerPmReset=_VirtualPortDefDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,13),_VirtualPortDefDataLayerPmReset_Type())
virtualPortDefDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefDataLayerPmReset.setStatus(_A)
_VirtualPortDefPortRole_Type=FspR7PortRole
_VirtualPortDefPortRole_Object=MibTableColumn
virtualPortDefPortRole=_VirtualPortDefPortRole_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,14),_VirtualPortDefPortRole_Type())
virtualPortDefPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefPortRole.setStatus(_A)
_VirtualPortDefLagPortType_Type=FspR7LagPortType
_VirtualPortDefLagPortType_Object=MibTableColumn
virtualPortDefLagPortType=_VirtualPortDefLagPortType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,15),_VirtualPortDefLagPortType_Type())
virtualPortDefLagPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefLagPortType.setStatus(_A)
class _VirtualPortDefPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VirtualPortDefPriority_Type.__name__=_D
_VirtualPortDefPriority_Object=MibTableColumn
virtualPortDefPriority=_VirtualPortDefPriority_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,16),_VirtualPortDefPriority_Type())
virtualPortDefPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefPriority.setStatus(_A)
class _VirtualPortDefPvid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_VirtualPortDefPvid_Type.__name__=_D
_VirtualPortDefPvid_Object=MibTableColumn
virtualPortDefPvid=_VirtualPortDefPvid_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,17),_VirtualPortDefPvid_Type())
virtualPortDefPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefPvid.setStatus(_A)
_VirtualPortDefRevertiveMode_Type=ApsRevertMode
_VirtualPortDefRevertiveMode_Object=MibTableColumn
virtualPortDefRevertiveMode=_VirtualPortDefRevertiveMode_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,18),_VirtualPortDefRevertiveMode_Type())
virtualPortDefRevertiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefRevertiveMode.setStatus(_A)
_VirtualPortDefStagType_Type=FspR7SnmpHexString
_VirtualPortDefStagType_Object=MibTableColumn
virtualPortDefStagType=_VirtualPortDefStagType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,19),_VirtualPortDefStagType_Type())
virtualPortDefStagType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefStagType.setStatus(_A)
_VirtualPortDefUtag_Type=FspR7UntaggedFrames
_VirtualPortDefUtag_Object=MibTableColumn
virtualPortDefUtag=_VirtualPortDefUtag_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,20),_VirtualPortDefUtag_Type())
virtualPortDefUtag.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefUtag.setStatus(_A)
_VirtualPortDefBundle_Type=FspR7SnmpLongString
_VirtualPortDefBundle_Object=MibTableColumn
virtualPortDefBundle=_VirtualPortDefBundle_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,21),_VirtualPortDefBundle_Type())
virtualPortDefBundle.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefBundle.setStatus(_A)
_VirtualPortDefSwitchCommand_Type=FspR7APSCommand
_VirtualPortDefSwitchCommand_Object=MibTableColumn
virtualPortDefSwitchCommand=_VirtualPortDefSwitchCommand_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,22),_VirtualPortDefSwitchCommand_Type())
virtualPortDefSwitchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSwitchCommand.setStatus(_A)
_VirtualPortDefInhibitSwitchToWork_Type=FspR7YesNo
_VirtualPortDefInhibitSwitchToWork_Object=MibTableColumn
virtualPortDefInhibitSwitchToWork=_VirtualPortDefInhibitSwitchToWork_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,23),_VirtualPortDefInhibitSwitchToWork_Type())
virtualPortDefInhibitSwitchToWork.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefInhibitSwitchToWork.setStatus(_A)
_VirtualPortDefInhibitSwitchToProt_Type=FspR7YesNo
_VirtualPortDefInhibitSwitchToProt_Object=MibTableColumn
virtualPortDefInhibitSwitchToProt=_VirtualPortDefInhibitSwitchToProt_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,24),_VirtualPortDefInhibitSwitchToProt_Type())
virtualPortDefInhibitSwitchToProt.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefInhibitSwitchToProt.setStatus(_A)
_VirtualPortDefOduTribPortNo_Type=SnmpAdminString
_VirtualPortDefOduTribPortNo_Object=MibTableColumn
virtualPortDefOduTribPortNo=_VirtualPortDefOduTribPortNo_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,25),_VirtualPortDefOduTribPortNo_Type())
virtualPortDefOduTribPortNo.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefOduTribPortNo.setStatus(_A)
_VirtualPortDefOduTribTimeSlottNo_Type=SnmpAdminString
_VirtualPortDefOduTribTimeSlottNo_Object=MibTableColumn
virtualPortDefOduTribTimeSlottNo=_VirtualPortDefOduTribTimeSlottNo_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,26),_VirtualPortDefOduTribTimeSlottNo_Type())
virtualPortDefOduTribTimeSlottNo.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefOduTribTimeSlottNo.setStatus(_A)
class _VirtualPortDefSigDegThresOdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VirtualPortDefSigDegThresOdu_Type.__name__=_G
_VirtualPortDefSigDegThresOdu_Object=MibTableColumn
virtualPortDefSigDegThresOdu=_VirtualPortDefSigDegThresOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,27),_VirtualPortDefSigDegThresOdu_Type())
virtualPortDefSigDegThresOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOdu.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOdu.setUnits(_H)
class _VirtualPortDefSigDegPeriodOdu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_VirtualPortDefSigDegPeriodOdu_Type.__name__=_D
_VirtualPortDefSigDegPeriodOdu_Object=MibTableColumn
virtualPortDefSigDegPeriodOdu=_VirtualPortDefSigDegPeriodOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,28),_VirtualPortDefSigDegPeriodOdu_Type())
virtualPortDefSigDegPeriodOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOdu.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOdu.setUnits(_I)
class _VirtualPortDefTraceExpectedOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceExpectedOdu_Type.__name__=_E
_VirtualPortDefTraceExpectedOdu_Object=MibTableColumn
virtualPortDefTraceExpectedOdu=_VirtualPortDefTraceExpectedOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,29),_VirtualPortDefTraceExpectedOdu_Type())
virtualPortDefTraceExpectedOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceExpectedOdu.setStatus(_A)
class _VirtualPortDefTraceTransmitSapiOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitSapiOdu_Type.__name__=_E
_VirtualPortDefTraceTransmitSapiOdu_Object=MibTableColumn
virtualPortDefTraceTransmitSapiOdu=_VirtualPortDefTraceTransmitSapiOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,30),_VirtualPortDefTraceTransmitSapiOdu_Type())
virtualPortDefTraceTransmitSapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitSapiOdu.setStatus(_A)
class _VirtualPortDefTraceTransmitDapiOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitDapiOdu_Type.__name__=_E
_VirtualPortDefTraceTransmitDapiOdu_Object=MibTableColumn
virtualPortDefTraceTransmitDapiOdu=_VirtualPortDefTraceTransmitDapiOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,31),_VirtualPortDefTraceTransmitDapiOdu_Type())
virtualPortDefTraceTransmitDapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitDapiOdu.setStatus(_A)
class _VirtualPortDefTraceTransmitOpspOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VirtualPortDefTraceTransmitOpspOdu_Type.__name__=_E
_VirtualPortDefTraceTransmitOpspOdu_Object=MibTableColumn
virtualPortDefTraceTransmitOpspOdu=_VirtualPortDefTraceTransmitOpspOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,32),_VirtualPortDefTraceTransmitOpspOdu_Type())
virtualPortDefTraceTransmitOpspOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitOpspOdu.setStatus(_A)
_VirtualPortDefTimModeOdu_Type=TimMode
_VirtualPortDefTimModeOdu_Object=MibTableColumn
virtualPortDefTimModeOdu=_VirtualPortDefTimModeOdu_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,33),_VirtualPortDefTimModeOdu_Type())
virtualPortDefTimModeOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTimModeOdu.setStatus(_A)
class _VirtualPortDefSigDegThresOduTcmA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VirtualPortDefSigDegThresOduTcmA_Type.__name__=_G
_VirtualPortDefSigDegThresOduTcmA_Object=MibTableColumn
virtualPortDefSigDegThresOduTcmA=_VirtualPortDefSigDegThresOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,34),_VirtualPortDefSigDegThresOduTcmA_Type())
virtualPortDefSigDegThresOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOduTcmA.setUnits(_H)
class _VirtualPortDefSigDegPeriodOduTcmA_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_VirtualPortDefSigDegPeriodOduTcmA_Type.__name__=_D
_VirtualPortDefSigDegPeriodOduTcmA_Object=MibTableColumn
virtualPortDefSigDegPeriodOduTcmA=_VirtualPortDefSigDegPeriodOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,35),_VirtualPortDefSigDegPeriodOduTcmA_Type())
virtualPortDefSigDegPeriodOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOduTcmA.setUnits(_I)
class _VirtualPortDefSigDegThresOduTcmB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VirtualPortDefSigDegThresOduTcmB_Type.__name__=_G
_VirtualPortDefSigDegThresOduTcmB_Object=MibTableColumn
virtualPortDefSigDegThresOduTcmB=_VirtualPortDefSigDegThresOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,36),_VirtualPortDefSigDegThresOduTcmB_Type())
virtualPortDefSigDegThresOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOduTcmB.setUnits(_H)
class _VirtualPortDefSigDegPeriodOduTcmB_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_VirtualPortDefSigDegPeriodOduTcmB_Type.__name__=_D
_VirtualPortDefSigDegPeriodOduTcmB_Object=MibTableColumn
virtualPortDefSigDegPeriodOduTcmB=_VirtualPortDefSigDegPeriodOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,37),_VirtualPortDefSigDegPeriodOduTcmB_Type())
virtualPortDefSigDegPeriodOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOduTcmB.setUnits(_I)
class _VirtualPortDefSigDegThresOduTcmC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VirtualPortDefSigDegThresOduTcmC_Type.__name__=_G
_VirtualPortDefSigDegThresOduTcmC_Object=MibTableColumn
virtualPortDefSigDegThresOduTcmC=_VirtualPortDefSigDegThresOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,38),_VirtualPortDefSigDegThresOduTcmC_Type())
virtualPortDefSigDegThresOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegThresOduTcmC.setUnits(_H)
class _VirtualPortDefSigDegPeriodOduTcmC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_VirtualPortDefSigDegPeriodOduTcmC_Type.__name__=_D
_VirtualPortDefSigDegPeriodOduTcmC_Object=MibTableColumn
virtualPortDefSigDegPeriodOduTcmC=_VirtualPortDefSigDegPeriodOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,39),_VirtualPortDefSigDegPeriodOduTcmC_Type())
virtualPortDefSigDegPeriodOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefSigDegPeriodOduTcmC.setUnits(_I)
_VirtualPortDefTcmALevel_Type=OtnTcmLevel
_VirtualPortDefTcmALevel_Object=MibTableColumn
virtualPortDefTcmALevel=_VirtualPortDefTcmALevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,40),_VirtualPortDefTcmALevel_Type())
virtualPortDefTcmALevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTcmALevel.setStatus(_A)
_VirtualPortDefTcmBLevel_Type=OtnTcmLevel
_VirtualPortDefTcmBLevel_Object=MibTableColumn
virtualPortDefTcmBLevel=_VirtualPortDefTcmBLevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,41),_VirtualPortDefTcmBLevel_Type())
virtualPortDefTcmBLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTcmBLevel.setStatus(_A)
_VirtualPortDefTcmCLevel_Type=OtnTcmLevel
_VirtualPortDefTcmCLevel_Object=MibTableColumn
virtualPortDefTcmCLevel=_VirtualPortDefTcmCLevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,42),_VirtualPortDefTcmCLevel_Type())
virtualPortDefTcmCLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTcmCLevel.setStatus(_A)
class _VirtualPortDefTraceTransmitSapiOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitSapiOduTcmA_Type.__name__=_E
_VirtualPortDefTraceTransmitSapiOduTcmA_Object=MibTableColumn
virtualPortDefTraceTransmitSapiOduTcmA=_VirtualPortDefTraceTransmitSapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,43),_VirtualPortDefTraceTransmitSapiOduTcmA_Type())
virtualPortDefTraceTransmitSapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitSapiOduTcmA.setStatus(_A)
class _VirtualPortDefTraceTransmitDapiOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitDapiOduTcmA_Type.__name__=_E
_VirtualPortDefTraceTransmitDapiOduTcmA_Object=MibTableColumn
virtualPortDefTraceTransmitDapiOduTcmA=_VirtualPortDefTraceTransmitDapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,44),_VirtualPortDefTraceTransmitDapiOduTcmA_Type())
virtualPortDefTraceTransmitDapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitDapiOduTcmA.setStatus(_A)
class _VirtualPortDefTraceTransmitOpspOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VirtualPortDefTraceTransmitOpspOduTcmA_Type.__name__=_E
_VirtualPortDefTraceTransmitOpspOduTcmA_Object=MibTableColumn
virtualPortDefTraceTransmitOpspOduTcmA=_VirtualPortDefTraceTransmitOpspOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,45),_VirtualPortDefTraceTransmitOpspOduTcmA_Type())
virtualPortDefTraceTransmitOpspOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitOpspOduTcmA.setStatus(_A)
class _VirtualPortDefTraceExpectedOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceExpectedOduTcmA_Type.__name__=_E
_VirtualPortDefTraceExpectedOduTcmA_Object=MibTableColumn
virtualPortDefTraceExpectedOduTcmA=_VirtualPortDefTraceExpectedOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,46),_VirtualPortDefTraceExpectedOduTcmA_Type())
virtualPortDefTraceExpectedOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceExpectedOduTcmA.setStatus(_A)
_VirtualPortDefTimModeOduTcmA_Type=TimMode
_VirtualPortDefTimModeOduTcmA_Object=MibTableColumn
virtualPortDefTimModeOduTcmA=_VirtualPortDefTimModeOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,47),_VirtualPortDefTimModeOduTcmA_Type())
virtualPortDefTimModeOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTimModeOduTcmA.setStatus(_A)
class _VirtualPortDefTraceExpectedOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceExpectedOduTcmB_Type.__name__=_E
_VirtualPortDefTraceExpectedOduTcmB_Object=MibTableColumn
virtualPortDefTraceExpectedOduTcmB=_VirtualPortDefTraceExpectedOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,48),_VirtualPortDefTraceExpectedOduTcmB_Type())
virtualPortDefTraceExpectedOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceExpectedOduTcmB.setStatus(_A)
class _VirtualPortDefTraceTransmitSapiOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitSapiOduTcmB_Type.__name__=_E
_VirtualPortDefTraceTransmitSapiOduTcmB_Object=MibTableColumn
virtualPortDefTraceTransmitSapiOduTcmB=_VirtualPortDefTraceTransmitSapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,49),_VirtualPortDefTraceTransmitSapiOduTcmB_Type())
virtualPortDefTraceTransmitSapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitSapiOduTcmB.setStatus(_A)
class _VirtualPortDefTraceTransmitDapiOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitDapiOduTcmB_Type.__name__=_E
_VirtualPortDefTraceTransmitDapiOduTcmB_Object=MibTableColumn
virtualPortDefTraceTransmitDapiOduTcmB=_VirtualPortDefTraceTransmitDapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,50),_VirtualPortDefTraceTransmitDapiOduTcmB_Type())
virtualPortDefTraceTransmitDapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitDapiOduTcmB.setStatus(_A)
class _VirtualPortDefTraceTransmitOpspOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VirtualPortDefTraceTransmitOpspOduTcmB_Type.__name__=_E
_VirtualPortDefTraceTransmitOpspOduTcmB_Object=MibTableColumn
virtualPortDefTraceTransmitOpspOduTcmB=_VirtualPortDefTraceTransmitOpspOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,51),_VirtualPortDefTraceTransmitOpspOduTcmB_Type())
virtualPortDefTraceTransmitOpspOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitOpspOduTcmB.setStatus(_A)
_VirtualPortDefTimModeOduTcmB_Type=TimMode
_VirtualPortDefTimModeOduTcmB_Object=MibTableColumn
virtualPortDefTimModeOduTcmB=_VirtualPortDefTimModeOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,52),_VirtualPortDefTimModeOduTcmB_Type())
virtualPortDefTimModeOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTimModeOduTcmB.setStatus(_A)
class _VirtualPortDefTraceExpectedOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceExpectedOduTcmC_Type.__name__=_E
_VirtualPortDefTraceExpectedOduTcmC_Object=MibTableColumn
virtualPortDefTraceExpectedOduTcmC=_VirtualPortDefTraceExpectedOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,53),_VirtualPortDefTraceExpectedOduTcmC_Type())
virtualPortDefTraceExpectedOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceExpectedOduTcmC.setStatus(_A)
class _VirtualPortDefTraceTransmitSapiOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitSapiOduTcmC_Type.__name__=_E
_VirtualPortDefTraceTransmitSapiOduTcmC_Object=MibTableColumn
virtualPortDefTraceTransmitSapiOduTcmC=_VirtualPortDefTraceTransmitSapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,54),_VirtualPortDefTraceTransmitSapiOduTcmC_Type())
virtualPortDefTraceTransmitSapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitSapiOduTcmC.setStatus(_A)
class _VirtualPortDefTraceTransmitDapiOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_VirtualPortDefTraceTransmitDapiOduTcmC_Type.__name__=_E
_VirtualPortDefTraceTransmitDapiOduTcmC_Object=MibTableColumn
virtualPortDefTraceTransmitDapiOduTcmC=_VirtualPortDefTraceTransmitDapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,55),_VirtualPortDefTraceTransmitDapiOduTcmC_Type())
virtualPortDefTraceTransmitDapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitDapiOduTcmC.setStatus(_A)
class _VirtualPortDefTraceTransmitOpspOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VirtualPortDefTraceTransmitOpspOduTcmC_Type.__name__=_E
_VirtualPortDefTraceTransmitOpspOduTcmC_Object=MibTableColumn
virtualPortDefTraceTransmitOpspOduTcmC=_VirtualPortDefTraceTransmitOpspOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,56),_VirtualPortDefTraceTransmitOpspOduTcmC_Type())
virtualPortDefTraceTransmitOpspOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTraceTransmitOpspOduTcmC.setStatus(_A)
_VirtualPortDefTimModeOduTcmC_Type=TimMode
_VirtualPortDefTimModeOduTcmC_Object=MibTableColumn
virtualPortDefTimModeOduTcmC=_VirtualPortDefTimModeOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,57),_VirtualPortDefTimModeOduTcmC_Type())
virtualPortDefTimModeOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTimModeOduTcmC.setStatus(_A)
_VirtualPortDefTerminationLevel_Type=OhTerminationLevel
_VirtualPortDefTerminationLevel_Object=MibTableColumn
virtualPortDefTerminationLevel=_VirtualPortDefTerminationLevel_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,58),_VirtualPortDefTerminationLevel_Type())
virtualPortDefTerminationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTerminationLevel.setStatus(_A)
_VirtualPortDefLoopConfig_Type=LoopConfig
_VirtualPortDefLoopConfig_Object=MibTableColumn
virtualPortDefLoopConfig=_VirtualPortDefLoopConfig_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,59),_VirtualPortDefLoopConfig_Type())
virtualPortDefLoopConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefLoopConfig.setStatus(_A)
_VirtualPortDefVcType_Type=VirtualContainerType
_VirtualPortDefVcType_Object=MibTableColumn
virtualPortDefVcType=_VirtualPortDefVcType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,60),_VirtualPortDefVcType_Type())
virtualPortDefVcType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefVcType.setStatus(_A)
_VirtualPortDefCir_Type=Unsigned32
_VirtualPortDefCir_Object=MibTableColumn
virtualPortDefCir=_VirtualPortDefCir_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,61),_VirtualPortDefCir_Type())
virtualPortDefCir.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefCir.setStatus(_A)
if mibBuilder.loadTexts:virtualPortDefCir.setUnits('Mbps')
_VirtualPortDefOpuPayloadType_Type=FspR7OpuPayloadType
_VirtualPortDefOpuPayloadType_Object=MibTableColumn
virtualPortDefOpuPayloadType=_VirtualPortDefOpuPayloadType_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,62),_VirtualPortDefOpuPayloadType_Type())
virtualPortDefOpuPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefOpuPayloadType.setStatus(_A)
_VirtualPortDefOtnStuffing_Type=FspR7Stuff
_VirtualPortDefOtnStuffing_Object=MibTableColumn
virtualPortDefOtnStuffing=_VirtualPortDefOtnStuffing_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,63),_VirtualPortDefOtnStuffing_Type())
virtualPortDefOtnStuffing.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefOtnStuffing.setStatus(_A)
_VirtualPortDefRedLineState_Type=FspR7RedLinedState
_VirtualPortDefRedLineState_Object=MibTableColumn
virtualPortDefRedLineState=_VirtualPortDefRedLineState_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,64),_VirtualPortDefRedLineState_Type())
virtualPortDefRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefRedLineState.setStatus(_A)
_VirtualPortDefTunnelAid_Type=SnmpAdminString
_VirtualPortDefTunnelAid_Object=MibTableColumn
virtualPortDefTunnelAid=_VirtualPortDefTunnelAid_Object((1,3,6,1,4,1,2544,1,11,10,3,4,2,1,65),_VirtualPortDefTunnelAid_Type())
virtualPortDefTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortDefTunnelAid.setStatus(_A)
_EndOfVirtualPortDefTable_Type=Integer32
_EndOfVirtualPortDefTable_Object=MibScalar
endOfVirtualPortDefTable=_EndOfVirtualPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,4,3),_EndOfVirtualPortDefTable_Type())
endOfVirtualPortDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfVirtualPortDefTable.setStatus(_A)
_EndOfFacilityMgmtDef_Type=Integer32
_EndOfFacilityMgmtDef_Object=MibScalar
endOfFacilityMgmtDef=_EndOfFacilityMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,4,10000),_EndOfFacilityMgmtDef_Type())
endOfFacilityMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFacilityMgmtDef.setStatus(_A)
_DcnMgmtDef_ObjectIdentity=ObjectIdentity
dcnMgmtDef=_DcnMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,5))
_LinkDefTable_Object=MibTable
linkDefTable=_LinkDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1))
if mibBuilder.loadTexts:linkDefTable.setStatus(_A)
_LinkDefEntry_Object=MibTableRow
linkDefEntry=_LinkDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1))
linkDefEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_Y),(0,_C,_X),(0,_C,_W))
if mibBuilder.loadTexts:linkDefEntry.setStatus(_A)
_LinkDefRowStatus_Type=RowStatus
_LinkDefRowStatus_Object=MibTableColumn
linkDefRowStatus=_LinkDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,1),_LinkDefRowStatus_Type())
linkDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefRowStatus.setStatus(_A)
_LinkDefType_Type=FspR7InterfaceType
_LinkDefType_Object=MibTableColumn
linkDefType=_LinkDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,2),_LinkDefType_Type())
linkDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefType.setStatus(_A)
_LinkDefAdmin_Type=FspR7AdminState
_LinkDefAdmin_Object=MibTableColumn
linkDefAdmin=_LinkDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,3),_LinkDefAdmin_Type())
linkDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefAdmin.setStatus(_A)
_LinkDefAlias_Type=SnmpAdminString
_LinkDefAlias_Object=MibTableColumn
linkDefAlias=_LinkDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,4),_LinkDefAlias_Type())
linkDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefAlias.setStatus(_A)
_LinkDefAuthString_Type=SnmpAdminString
_LinkDefAuthString_Object=MibTableColumn
linkDefAuthString=_LinkDefAuthString_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,5),_LinkDefAuthString_Type())
linkDefAuthString.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefAuthString.setStatus(_A)
_LinkDefProxyArp_Type=FspR7NoYes
_LinkDefProxyArp_Object=MibTableColumn
linkDefProxyArp=_LinkDefProxyArp_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,6),_LinkDefProxyArp_Type())
linkDefProxyArp.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefProxyArp.setStatus(_A)
_LinkDefOspf_Type=FspR7OspfMode
_LinkDefOspf_Object=MibTableColumn
linkDefOspf=_LinkDefOspf_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,7),_LinkDefOspf_Type())
linkDefOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefOspf.setStatus(_A)
_LinkDefBaud_Type=FspR7Baund
_LinkDefBaud_Object=MibTableColumn
linkDefBaud=_LinkDefBaud_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,8),_LinkDefBaud_Type())
linkDefBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefBaud.setStatus(_A)
_LinkDefAuthType_Type=FspR7CpAuthType
_LinkDefAuthType_Object=MibTableColumn
linkDefAuthType=_LinkDefAuthType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,9),_LinkDefAuthType_Type())
linkDefAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefAuthType.setStatus(_A)
_LinkDefIpType_Type=FspR7IpType
_LinkDefIpType_Object=MibTableColumn
linkDefIpType=_LinkDefIpType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,10),_LinkDefIpType_Type())
linkDefIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefIpType.setStatus(_A)
class _LinkDefMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LinkDefMetric_Type.__name__=_D
_LinkDefMetric_Object=MibTableColumn
linkDefMetric=_LinkDefMetric_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,11),_LinkDefMetric_Type())
linkDefMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefMetric.setStatus(_A)
_LinkDefAreaAid_Type=SnmpAdminString
_LinkDefAreaAid_Object=MibTableColumn
linkDefAreaAid=_LinkDefAreaAid_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,12),_LinkDefAreaAid_Type())
linkDefAreaAid.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefAreaAid.setStatus(_A)
_LinkDefNearEndIp_Type=IpAddress
_LinkDefNearEndIp_Object=MibTableColumn
linkDefNearEndIp=_LinkDefNearEndIp_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,13),_LinkDefNearEndIp_Type())
linkDefNearEndIp.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefNearEndIp.setStatus(_A)
class _LinkDefBitrate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,13702))
_LinkDefBitrate_Type.__name__=_D
_LinkDefBitrate_Object=MibTableColumn
linkDefBitrate=_LinkDefBitrate_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,14),_LinkDefBitrate_Type())
linkDefBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefBitrate.setStatus(_A)
if mibBuilder.loadTexts:linkDefBitrate.setUnits('kbps')
_LinkDefIPv6Type_Type=FspR7IPv6Type
_LinkDefIPv6Type_Object=MibTableColumn
linkDefIPv6Type=_LinkDefIPv6Type_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,15),_LinkDefIPv6Type_Type())
linkDefIPv6Type.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefIPv6Type.setStatus(_A)
_LinkDefNendIPv6_Type=SnmpAdminString
_LinkDefNendIPv6_Object=MibTableColumn
linkDefNendIPv6=_LinkDefNendIPv6_Object((1,3,6,1,4,1,2544,1,11,10,3,5,1,1,16),_LinkDefNendIPv6_Type())
linkDefNendIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDefNendIPv6.setStatus(_A)
_EndOfLinkDefTable_Type=Integer32
_EndOfLinkDefTable_Object=MibScalar
endOfLinkDefTable=_EndOfLinkDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,2),_EndOfLinkDefTable_Type())
endOfLinkDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfLinkDefTable.setStatus(_A)
_ScDefTable_Object=MibTable
scDefTable=_ScDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3))
if mibBuilder.loadTexts:scDefTable.setStatus(_A)
_ScDefEntry_Object=MibTableRow
scDefEntry=_ScDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1))
scDefEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_Y),(0,_C,_X),(0,_C,_W))
if mibBuilder.loadTexts:scDefEntry.setStatus(_A)
_ScDefRowStatus_Type=RowStatus
_ScDefRowStatus_Object=MibTableColumn
scDefRowStatus=_ScDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,1),_ScDefRowStatus_Type())
scDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefRowStatus.setStatus(_A)
_ScDefType_Type=FspR7InterfaceType
_ScDefType_Object=MibTableColumn
scDefType=_ScDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,2),_ScDefType_Type())
scDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefType.setStatus(_A)
_ScDefAdmin_Type=FspR7AdminState
_ScDefAdmin_Object=MibTableColumn
scDefAdmin=_ScDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,3),_ScDefAdmin_Type())
scDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAdmin.setStatus(_A)
_ScDefAlias_Type=SnmpAdminString
_ScDefAlias_Object=MibTableColumn
scDefAlias=_ScDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,4),_ScDefAlias_Type())
scDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAlias.setStatus(_A)
_ScDefAuthString_Type=SnmpAdminString
_ScDefAuthString_Object=MibTableColumn
scDefAuthString=_ScDefAuthString_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,5),_ScDefAuthString_Type())
scDefAuthString.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAuthString.setStatus(_A)
_ScDefOspf_Type=FspR7OspfMode
_ScDefOspf_Object=MibTableColumn
scDefOspf=_ScDefOspf_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,6),_ScDefOspf_Type())
scDefOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefOspf.setStatus(_A)
_ScDefAuthType_Type=FspR7CpAuthType
_ScDefAuthType_Object=MibTableColumn
scDefAuthType=_ScDefAuthType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,7),_ScDefAuthType_Type())
scDefAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAuthType.setStatus(_A)
_ScDefIpType_Type=FspR7IpType
_ScDefIpType_Object=MibTableColumn
scDefIpType=_ScDefIpType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,8),_ScDefIpType_Type())
scDefIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefIpType.setStatus(_A)
class _ScDefMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ScDefMetric_Type.__name__=_D
_ScDefMetric_Object=MibTableColumn
scDefMetric=_ScDefMetric_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,9),_ScDefMetric_Type())
scDefMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefMetric.setStatus(_A)
_ScDefAreaAid_Type=SnmpAdminString
_ScDefAreaAid_Object=MibTableColumn
scDefAreaAid=_ScDefAreaAid_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,10),_ScDefAreaAid_Type())
scDefAreaAid.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAreaAid.setStatus(_A)
_ScDefAlsMode_Type=FspR7AlsMode
_ScDefAlsMode_Object=MibTableColumn
scDefAlsMode=_ScDefAlsMode_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,11),_ScDefAlsMode_Type())
scDefAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAlsMode.setStatus(_A)
_ScDefSigDegThresReceiver_Type=Unsigned32
_ScDefSigDegThresReceiver_Object=MibTableColumn
scDefSigDegThresReceiver=_ScDefSigDegThresReceiver_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,12),_ScDefSigDegThresReceiver_Type())
scDefSigDegThresReceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefSigDegThresReceiver.setStatus(_A)
if mibBuilder.loadTexts:scDefSigDegThresReceiver.setUnits(_K)
_ScDefAutonegotiation_Type=EnableState
_ScDefAutonegotiation_Object=MibTableColumn
scDefAutonegotiation=_ScDefAutonegotiation_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,13),_ScDefAutonegotiation_Type())
scDefAutonegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAutonegotiation.setStatus(_A)
_ScDefBitrate_Type=FspR7Bitrate
_ScDefBitrate_Object=MibTableColumn
scDefBitrate=_ScDefBitrate_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,14),_ScDefBitrate_Type())
scDefBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefBitrate.setStatus(_A)
_ScDefDuplex_Type=EthDuplexMode
_ScDefDuplex_Object=MibTableColumn
scDefDuplex=_ScDefDuplex_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,15),_ScDefDuplex_Type())
scDefDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefDuplex.setStatus(_A)
class _ScDefAttGradientTh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_ScDefAttGradientTh_Type.__name__=_D
_ScDefAttGradientTh_Object=MibTableColumn
scDefAttGradientTh=_ScDefAttGradientTh_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,16),_ScDefAttGradientTh_Type())
scDefAttGradientTh.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefAttGradientTh.setStatus(_A)
if mibBuilder.loadTexts:scDefAttGradientTh.setUnits(_Aa)
_ScDefIpAddr_Type=IpAddress
_ScDefIpAddr_Object=MibTableColumn
scDefIpAddr=_ScDefIpAddr_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,17),_ScDefIpAddr_Type())
scDefIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefIpAddr.setStatus(_A)
_ScDefLanAid_Type=SnmpAdminString
_ScDefLanAid_Object=MibTableColumn
scDefLanAid=_ScDefLanAid_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,18),_ScDefLanAid_Type())
scDefLanAid.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefLanAid.setStatus(_A)
_ScDefIpMask_Type=IpAddress
_ScDefIpMask_Object=MibTableColumn
scDefIpMask=_ScDefIpMask_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,19),_ScDefIpMask_Type())
scDefIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefIpMask.setStatus(_A)
_ScDefDataLayerPmReset_Type=FspR7PmReset
_ScDefDataLayerPmReset_Object=MibTableColumn
scDefDataLayerPmReset=_ScDefDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,20),_ScDefDataLayerPmReset_Type())
scDefDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefDataLayerPmReset.setStatus(_A)
class _ScDefPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ScDefPriority_Type.__name__=_D
_ScDefPriority_Object=MibTableColumn
scDefPriority=_ScDefPriority_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,21),_ScDefPriority_Type())
scDefPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefPriority.setStatus(_A)
_ScDefIPv6_Type=SnmpAdminString
_ScDefIPv6_Object=MibTableColumn
scDefIPv6=_ScDefIPv6_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,22),_ScDefIPv6_Type())
scDefIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefIPv6.setStatus(_A)
class _ScDefIPv6PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_ScDefIPv6PrefixLen_Type.__name__=_D
_ScDefIPv6PrefixLen_Object=MibTableColumn
scDefIPv6PrefixLen=_ScDefIPv6PrefixLen_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,23),_ScDefIPv6PrefixLen_Type())
scDefIPv6PrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefIPv6PrefixLen.setStatus(_A)
_ScDefIpMode_Type=FspR7IpMode
_ScDefIpMode_Object=MibTableColumn
scDefIpMode=_ScDefIpMode_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,24),_ScDefIpMode_Type())
scDefIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefIpMode.setStatus(_A)
_ScDefGatewayProxyArp_Type=FspR7EnableDisable
_ScDefGatewayProxyArp_Object=MibTableColumn
scDefGatewayProxyArp=_ScDefGatewayProxyArp_Object((1,3,6,1,4,1,2544,1,11,10,3,5,3,1,25),_ScDefGatewayProxyArp_Type())
scDefGatewayProxyArp.setMaxAccess(_B)
if mibBuilder.loadTexts:scDefGatewayProxyArp.setStatus(_A)
_EndOfScDefTable_Type=Integer32
_EndOfScDefTable_Object=MibScalar
endOfScDefTable=_EndOfScDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,4),_EndOfScDefTable_Type())
endOfScDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfScDefTable.setStatus(_A)
_LanDefTable_Object=MibTable
lanDefTable=_LanDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5))
if mibBuilder.loadTexts:lanDefTable.setStatus(_A)
_LanDefEntry_Object=MibTableRow
lanDefEntry=_LanDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1))
lanDefEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_Y),(0,_C,_X),(0,_C,_W))
if mibBuilder.loadTexts:lanDefEntry.setStatus(_A)
_LanDefRowStatus_Type=RowStatus
_LanDefRowStatus_Object=MibTableColumn
lanDefRowStatus=_LanDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,1),_LanDefRowStatus_Type())
lanDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefRowStatus.setStatus(_A)
_LanDefType_Type=FspR7InterfaceType
_LanDefType_Object=MibTableColumn
lanDefType=_LanDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,2),_LanDefType_Type())
lanDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefType.setStatus(_A)
_LanDefAdmin_Type=FspR7AdminState
_LanDefAdmin_Object=MibTableColumn
lanDefAdmin=_LanDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,3),_LanDefAdmin_Type())
lanDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefAdmin.setStatus(_A)
_LanDefAlias_Type=SnmpAdminString
_LanDefAlias_Object=MibTableColumn
lanDefAlias=_LanDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,4),_LanDefAlias_Type())
lanDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefAlias.setStatus(_A)
_LanDefAuthString_Type=SnmpAdminString
_LanDefAuthString_Object=MibTableColumn
lanDefAuthString=_LanDefAuthString_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,5),_LanDefAuthString_Type())
lanDefAuthString.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefAuthString.setStatus(_A)
_LanDefOspf_Type=FspR7OspfMode
_LanDefOspf_Object=MibTableColumn
lanDefOspf=_LanDefOspf_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,6),_LanDefOspf_Type())
lanDefOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefOspf.setStatus(_A)
_LanDefAuthType_Type=FspR7CpAuthType
_LanDefAuthType_Object=MibTableColumn
lanDefAuthType=_LanDefAuthType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,7),_LanDefAuthType_Type())
lanDefAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefAuthType.setStatus(_A)
_LanDefIpType_Type=FspR7IpType
_LanDefIpType_Object=MibTableColumn
lanDefIpType=_LanDefIpType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,8),_LanDefIpType_Type())
lanDefIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefIpType.setStatus(_A)
class _LanDefMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LanDefMetric_Type.__name__=_D
_LanDefMetric_Object=MibTableColumn
lanDefMetric=_LanDefMetric_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,9),_LanDefMetric_Type())
lanDefMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefMetric.setStatus(_A)
_LanDefAreaAid_Type=SnmpAdminString
_LanDefAreaAid_Object=MibTableColumn
lanDefAreaAid=_LanDefAreaAid_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,10),_LanDefAreaAid_Type())
lanDefAreaAid.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefAreaAid.setStatus(_A)
_LanDefIpAddr_Type=IpAddress
_LanDefIpAddr_Object=MibTableColumn
lanDefIpAddr=_LanDefIpAddr_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,11),_LanDefIpAddr_Type())
lanDefIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefIpAddr.setStatus(_A)
_LanDefIpMask_Type=IpAddress
_LanDefIpMask_Object=MibTableColumn
lanDefIpMask=_LanDefIpMask_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,12),_LanDefIpMask_Type())
lanDefIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefIpMask.setStatus(_A)
class _LanDefPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LanDefPriority_Type.__name__=_D
_LanDefPriority_Object=MibTableColumn
lanDefPriority=_LanDefPriority_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,13),_LanDefPriority_Type())
lanDefPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefPriority.setStatus(_A)
_LanDefIPv6_Type=SnmpAdminString
_LanDefIPv6_Object=MibTableColumn
lanDefIPv6=_LanDefIPv6_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,14),_LanDefIPv6_Type())
lanDefIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefIPv6.setStatus(_A)
class _LanDefIPv6PrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_LanDefIPv6PrefixLen_Type.__name__=_D
_LanDefIPv6PrefixLen_Object=MibTableColumn
lanDefIPv6PrefixLen=_LanDefIPv6PrefixLen_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,15),_LanDefIPv6PrefixLen_Type())
lanDefIPv6PrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefIPv6PrefixLen.setStatus(_A)
_LanDefIpMode_Type=FspR7IpMode
_LanDefIpMode_Object=MibTableColumn
lanDefIpMode=_LanDefIpMode_Object((1,3,6,1,4,1,2544,1,11,10,3,5,5,1,16),_LanDefIpMode_Type())
lanDefIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lanDefIpMode.setStatus(_A)
_EndOfLanDefTable_Type=Integer32
_EndOfLanDefTable_Object=MibScalar
endOfLanDefTable=_EndOfLanDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,6),_EndOfLanDefTable_Type())
endOfLanDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfLanDefTable.setStatus(_A)
_EccDefTable_Object=MibTable
eccDefTable=_EccDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7))
if mibBuilder.loadTexts:eccDefTable.setStatus(_A)
_EccDefEntry_Object=MibTableRow
eccDefEntry=_EccDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1))
eccDefEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_Y),(0,_C,_X),(0,_C,_W))
if mibBuilder.loadTexts:eccDefEntry.setStatus(_A)
_EccDefRowStatus_Type=RowStatus
_EccDefRowStatus_Object=MibTableColumn
eccDefRowStatus=_EccDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1,1),_EccDefRowStatus_Type())
eccDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eccDefRowStatus.setStatus(_A)
_EccDefType_Type=FspR7InterfaceType
_EccDefType_Object=MibTableColumn
eccDefType=_EccDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1,2),_EccDefType_Type())
eccDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:eccDefType.setStatus(_A)
_EccDefAdmin_Type=FspR7AdminState
_EccDefAdmin_Object=MibTableColumn
eccDefAdmin=_EccDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1,3),_EccDefAdmin_Type())
eccDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:eccDefAdmin.setStatus(_A)
_EccDefAlias_Type=SnmpAdminString
_EccDefAlias_Object=MibTableColumn
eccDefAlias=_EccDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1,4),_EccDefAlias_Type())
eccDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:eccDefAlias.setStatus(_A)
_EccDefLanAid_Type=SnmpAdminString
_EccDefLanAid_Object=MibTableColumn
eccDefLanAid=_EccDefLanAid_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1,5),_EccDefLanAid_Type())
eccDefLanAid.setMaxAccess(_B)
if mibBuilder.loadTexts:eccDefLanAid.setStatus(_A)
class _EccDefExternalVid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_EccDefExternalVid_Type.__name__=_D
_EccDefExternalVid_Object=MibTableColumn
eccDefExternalVid=_EccDefExternalVid_Object((1,3,6,1,4,1,2544,1,11,10,3,5,7,1,6),_EccDefExternalVid_Type())
eccDefExternalVid.setMaxAccess(_B)
if mibBuilder.loadTexts:eccDefExternalVid.setStatus(_A)
_EndOfEccDefTable_Type=Integer32
_EndOfEccDefTable_Object=MibScalar
endOfEccDefTable=_EndOfEccDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,5,8),_EndOfEccDefTable_Type())
endOfEccDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEccDefTable.setStatus(_A)
_EndOfDcnMgmtDef_Type=Integer32
_EndOfDcnMgmtDef_Object=MibScalar
endOfDcnMgmtDef=_EndOfDcnMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,5,10000),_EndOfDcnMgmtDef_Type())
endOfDcnMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfDcnMgmtDef.setStatus(_A)
_OpticalMuxMgmtDef_ObjectIdentity=ObjectIdentity
opticalMuxMgmtDef=_OpticalMuxMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,6))
_OpticalMuxDefTable_Object=MibTable
opticalMuxDefTable=_OpticalMuxDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1))
if mibBuilder.loadTexts:opticalMuxDefTable.setStatus(_A)
_OpticalMuxDefEntry_Object=MibTableRow
opticalMuxDefEntry=_OpticalMuxDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1))
opticalMuxDefEntry.setIndexNames((0,_C,_AT),(0,_C,_AU),(0,_C,_AS),(0,_C,_AR),(0,_C,_AQ))
if mibBuilder.loadTexts:opticalMuxDefEntry.setStatus(_A)
_OpticalMuxDefRowStatus_Type=RowStatus
_OpticalMuxDefRowStatus_Object=MibTableColumn
opticalMuxDefRowStatus=_OpticalMuxDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,1),_OpticalMuxDefRowStatus_Type())
opticalMuxDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefRowStatus.setStatus(_A)
class _OpticalMuxDefPumpPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(115,138))
_OpticalMuxDefPumpPower_Type.__name__=_G
_OpticalMuxDefPumpPower_Object=MibTableColumn
opticalMuxDefPumpPower=_OpticalMuxDefPumpPower_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,2),_OpticalMuxDefPumpPower_Type())
opticalMuxDefPumpPower.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefPumpPower.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefPumpPower.setUnits('0.2 dBm')
_OpticalMuxDefInhibitSwitchToWork_Type=FspR7YesNo
_OpticalMuxDefInhibitSwitchToWork_Object=MibTableColumn
opticalMuxDefInhibitSwitchToWork=_OpticalMuxDefInhibitSwitchToWork_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,3),_OpticalMuxDefInhibitSwitchToWork_Type())
opticalMuxDefInhibitSwitchToWork.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefInhibitSwitchToWork.setStatus(_A)
_OpticalMuxDefForceLaserOn_Type=FspR7LaserForcedOperation
_OpticalMuxDefForceLaserOn_Object=MibTableColumn
opticalMuxDefForceLaserOn=_OpticalMuxDefForceLaserOn_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,4),_OpticalMuxDefForceLaserOn_Type())
opticalMuxDefForceLaserOn.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefForceLaserOn.setStatus(_A)
_OpticalMuxDefAseTabCreation_Type=FspR7AseTabOpr
_OpticalMuxDefAseTabCreation_Object=MibTableColumn
opticalMuxDefAseTabCreation=_OpticalMuxDefAseTabCreation_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,5),_OpticalMuxDefAseTabCreation_Type())
opticalMuxDefAseTabCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefAseTabCreation.setStatus(_A)
class _OpticalMuxDefOpticalSetPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,50))
_OpticalMuxDefOpticalSetPoint_Type.__name__=_G
_OpticalMuxDefOpticalSetPoint_Object=MibTableColumn
opticalMuxDefOpticalSetPoint=_OpticalMuxDefOpticalSetPoint_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,6),_OpticalMuxDefOpticalSetPoint_Type())
opticalMuxDefOpticalSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefOpticalSetPoint.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefOpticalSetPoint.setUnits(_J)
_OpticalMuxDefInitiateEqualization_Type=FspR7InitEqualization
_OpticalMuxDefInitiateEqualization_Object=MibTableColumn
opticalMuxDefInitiateEqualization=_OpticalMuxDefInitiateEqualization_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,7),_OpticalMuxDefInitiateEqualization_Type())
opticalMuxDefInitiateEqualization.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefInitiateEqualization.setStatus(_A)
class _OpticalMuxDefTilt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,0))
_OpticalMuxDefTilt_Type.__name__=_G
_OpticalMuxDefTilt_Object=MibTableColumn
opticalMuxDefTilt=_OpticalMuxDefTilt_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,8),_OpticalMuxDefTilt_Type())
opticalMuxDefTilt.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefTilt.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefTilt.setUnits(_K)
class _OpticalMuxDefOscOpticalSetpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,50))
_OpticalMuxDefOscOpticalSetpoint_Type.__name__=_G
_OpticalMuxDefOscOpticalSetpoint_Object=MibTableColumn
opticalMuxDefOscOpticalSetpoint=_OpticalMuxDefOscOpticalSetpoint_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,9),_OpticalMuxDefOscOpticalSetpoint_Type())
opticalMuxDefOscOpticalSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefOscOpticalSetpoint.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefOscOpticalSetpoint.setUnits(_J)
class _OpticalMuxDefOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_OpticalMuxDefOffset_Type.__name__=_G
_OpticalMuxDefOffset_Object=MibTableColumn
opticalMuxDefOffset=_OpticalMuxDefOffset_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,10),_OpticalMuxDefOffset_Type())
opticalMuxDefOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefOffset.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefOffset.setUnits(_K)
_OpticalMuxDefSwitchCommand_Type=FspR7APSCommand
_OpticalMuxDefSwitchCommand_Object=MibTableColumn
opticalMuxDefSwitchCommand=_OpticalMuxDefSwitchCommand_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,11),_OpticalMuxDefSwitchCommand_Type())
opticalMuxDefSwitchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefSwitchCommand.setStatus(_A)
_OpticalMuxDefAlsMode_Type=FspR7AlsMode
_OpticalMuxDefAlsMode_Object=MibTableColumn
opticalMuxDefAlsMode=_OpticalMuxDefAlsMode_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,12),_OpticalMuxDefAlsMode_Type())
opticalMuxDefAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefAlsMode.setStatus(_A)
_OpticalMuxDefType_Type=FspR7InterfaceType
_OpticalMuxDefType_Object=MibTableColumn
opticalMuxDefType=_OpticalMuxDefType_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,13),_OpticalMuxDefType_Type())
opticalMuxDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefType.setStatus(_A)
class _OpticalMuxDefAttenuationGradient_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_OpticalMuxDefAttenuationGradient_Type.__name__=_D
_OpticalMuxDefAttenuationGradient_Object=MibTableColumn
opticalMuxDefAttenuationGradient=_OpticalMuxDefAttenuationGradient_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,14),_OpticalMuxDefAttenuationGradient_Type())
opticalMuxDefAttenuationGradient.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefAttenuationGradient.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefAttenuationGradient.setUnits(_Aa)
_OpticalMuxDefInhibitSwitchToProt_Type=FspR7YesNo
_OpticalMuxDefInhibitSwitchToProt_Object=MibTableColumn
opticalMuxDefInhibitSwitchToProt=_OpticalMuxDefInhibitSwitchToProt_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,15),_OpticalMuxDefInhibitSwitchToProt_Type())
opticalMuxDefInhibitSwitchToProt.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefInhibitSwitchToProt.setStatus(_A)
class _OpticalMuxDefVariableGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,350))
_OpticalMuxDefVariableGain_Type.__name__=_D
_OpticalMuxDefVariableGain_Object=MibTableColumn
opticalMuxDefVariableGain=_OpticalMuxDefVariableGain_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,16),_OpticalMuxDefVariableGain_Type())
opticalMuxDefVariableGain.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefVariableGain.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefVariableGain.setUnits(_K)
_OpticalMuxDefAdmin_Type=FspR7AdminState
_OpticalMuxDefAdmin_Object=MibTableColumn
opticalMuxDefAdmin=_OpticalMuxDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,17),_OpticalMuxDefAdmin_Type())
opticalMuxDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefAdmin.setStatus(_A)
_OpticalMuxDefTimePeriod_Type=FspR7OtdrPeriod
_OpticalMuxDefTimePeriod_Object=MibTableColumn
opticalMuxDefTimePeriod=_OpticalMuxDefTimePeriod_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,18),_OpticalMuxDefTimePeriod_Type())
opticalMuxDefTimePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefTimePeriod.setStatus(_A)
_OpticalMuxDefSigDegThresReceiver_Type=Unsigned32
_OpticalMuxDefSigDegThresReceiver_Object=MibTableColumn
opticalMuxDefSigDegThresReceiver=_OpticalMuxDefSigDegThresReceiver_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,19),_OpticalMuxDefSigDegThresReceiver_Type())
opticalMuxDefSigDegThresReceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefSigDegThresReceiver.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefSigDegThresReceiver.setUnits(_K)
_OpticalMuxDefAlias_Type=SnmpAdminString
_OpticalMuxDefAlias_Object=MibTableColumn
opticalMuxDefAlias=_OpticalMuxDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,20),_OpticalMuxDefAlias_Type())
opticalMuxDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefAlias.setStatus(_A)
_OpticalMuxDefDataLayerPmReset_Type=FspR7PmReset
_OpticalMuxDefDataLayerPmReset_Object=MibTableColumn
opticalMuxDefDataLayerPmReset=_OpticalMuxDefDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,21),_OpticalMuxDefDataLayerPmReset_Type())
opticalMuxDefDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefDataLayerPmReset.setStatus(_A)
_OpticalMuxDefGain_Type=FspR7Gain
_OpticalMuxDefGain_Object=MibTableColumn
opticalMuxDefGain=_OpticalMuxDefGain_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,22),_OpticalMuxDefGain_Type())
opticalMuxDefGain.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefGain.setStatus(_A)
_OpticalMuxDefEdfaPwrOut_Type=FspR7EdfaOutputPowerRating
_OpticalMuxDefEdfaPwrOut_Object=MibTableColumn
opticalMuxDefEdfaPwrOut=_OpticalMuxDefEdfaPwrOut_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,23),_OpticalMuxDefEdfaPwrOut_Type())
opticalMuxDefEdfaPwrOut.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefEdfaPwrOut.setStatus(_A)
class _OpticalMuxDefVoaSetpoint_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_OpticalMuxDefVoaSetpoint_Type.__name__=_D
_OpticalMuxDefVoaSetpoint_Object=MibTableColumn
opticalMuxDefVoaSetpoint=_OpticalMuxDefVoaSetpoint_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,24),_OpticalMuxDefVoaSetpoint_Type())
opticalMuxDefVoaSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefVoaSetpoint.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefVoaSetpoint.setUnits(_K)
_OpticalMuxDefFiberBrand_Type=FspR7FiberBrand
_OpticalMuxDefFiberBrand_Object=MibTableColumn
opticalMuxDefFiberBrand=_OpticalMuxDefFiberBrand_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,25),_OpticalMuxDefFiberBrand_Type())
opticalMuxDefFiberBrand.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefFiberBrand.setStatus(_A)
_OpticalMuxDefTiltSet_Type=FspR7TiltSet
_OpticalMuxDefTiltSet_Object=MibTableColumn
opticalMuxDefTiltSet=_OpticalMuxDefTiltSet_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,26),_OpticalMuxDefTiltSet_Type())
opticalMuxDefTiltSet.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefTiltSet.setStatus(_A)
_OpticalMuxDefForceFwdAsePilotOn_Type=FspR7LaserForcedOperation
_OpticalMuxDefForceFwdAsePilotOn_Object=MibTableColumn
opticalMuxDefForceFwdAsePilotOn=_OpticalMuxDefForceFwdAsePilotOn_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,27),_OpticalMuxDefForceFwdAsePilotOn_Type())
opticalMuxDefForceFwdAsePilotOn.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefForceFwdAsePilotOn.setStatus(_A)
_OpticalMuxDefBandProvision_Type=FspR7OpticalBand
_OpticalMuxDefBandProvision_Object=MibTableColumn
opticalMuxDefBandProvision=_OpticalMuxDefBandProvision_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,28),_OpticalMuxDefBandProvision_Type())
opticalMuxDefBandProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefBandProvision.setStatus(_A)
class _OpticalMuxDefOffsetHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,210))
_OpticalMuxDefOffsetHigh_Type.__name__=_G
_OpticalMuxDefOffsetHigh_Object=MibTableColumn
opticalMuxDefOffsetHigh=_OpticalMuxDefOffsetHigh_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,29),_OpticalMuxDefOffsetHigh_Type())
opticalMuxDefOffsetHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefOffsetHigh.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefOffsetHigh.setUnits(_J)
class _OpticalMuxDefOffsetLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,210))
_OpticalMuxDefOffsetLow_Type.__name__=_G
_OpticalMuxDefOffsetLow_Object=MibTableColumn
opticalMuxDefOffsetLow=_OpticalMuxDefOffsetLow_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,30),_OpticalMuxDefOffsetLow_Type())
opticalMuxDefOffsetLow.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefOffsetLow.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxDefOffsetLow.setUnits(_J)
_OpticalMuxDefOptUpdate_Type=FspR7OptUpdate
_OpticalMuxDefOptUpdate_Object=MibTableColumn
opticalMuxDefOptUpdate=_OpticalMuxDefOptUpdate_Object((1,3,6,1,4,1,2544,1,11,10,3,6,1,1,31),_OpticalMuxDefOptUpdate_Type())
opticalMuxDefOptUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxDefOptUpdate.setStatus(_A)
_EndOfOpticalMuxDefTable_Type=Integer32
_EndOfOpticalMuxDefTable_Object=MibScalar
endOfOpticalMuxDefTable=_EndOfOpticalMuxDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,6,2),_EndOfOpticalMuxDefTable_Type())
endOfOpticalMuxDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalMuxDefTable.setStatus(_A)
_EndOfOpticalMuxMgmtDef_Type=Integer32
_EndOfOpticalMuxMgmtDef_Object=MibScalar
endOfOpticalMuxMgmtDef=_EndOfOpticalMuxMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,6,10000),_EndOfOpticalMuxMgmtDef_Type())
endOfOpticalMuxMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalMuxMgmtDef.setStatus(_A)
_ShelfConnMgmtDef_ObjectIdentity=ObjectIdentity
shelfConnMgmtDef=_ShelfConnMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,7))
_ShelfConnDefTable_Object=MibTable
shelfConnDefTable=_ShelfConnDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,7,1))
if mibBuilder.loadTexts:shelfConnDefTable.setStatus(_A)
_ShelfConnDefEntry_Object=MibTableRow
shelfConnDefEntry=_ShelfConnDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,7,1,1))
shelfConnDefEntry.setIndexNames((0,_C,_AY),(0,_C,_AZ),(0,_C,_AX),(0,_C,_AW),(0,_C,_AV))
if mibBuilder.loadTexts:shelfConnDefEntry.setStatus(_A)
_ShelfConnDefRowStatus_Type=RowStatus
_ShelfConnDefRowStatus_Object=MibTableColumn
shelfConnDefRowStatus=_ShelfConnDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,7,1,1,1),_ShelfConnDefRowStatus_Type())
shelfConnDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnDefRowStatus.setStatus(_A)
_ShelfConnDefAdmin_Type=FspR7AdminState
_ShelfConnDefAdmin_Object=MibTableColumn
shelfConnDefAdmin=_ShelfConnDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,3,7,1,1,2),_ShelfConnDefAdmin_Type())
shelfConnDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnDefAdmin.setStatus(_A)
_ShelfConnDefAlias_Type=SnmpAdminString
_ShelfConnDefAlias_Object=MibTableColumn
shelfConnDefAlias=_ShelfConnDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,7,1,1,3),_ShelfConnDefAlias_Type())
shelfConnDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnDefAlias.setStatus(_A)
_ShelfConnDefFacilityType_Type=FspR7InterfaceType
_ShelfConnDefFacilityType_Object=MibTableColumn
shelfConnDefFacilityType=_ShelfConnDefFacilityType_Object((1,3,6,1,4,1,2544,1,11,10,3,7,1,1,4),_ShelfConnDefFacilityType_Type())
shelfConnDefFacilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnDefFacilityType.setStatus(_A)
_EndOfShelfConnDefTable_Type=Integer32
_EndOfShelfConnDefTable_Object=MibScalar
endOfShelfConnDefTable=_EndOfShelfConnDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,7,2),_EndOfShelfConnDefTable_Type())
endOfShelfConnDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfShelfConnDefTable.setStatus(_A)
_EndOfShelfConnMgmtDef_Type=Integer32
_EndOfShelfConnMgmtDef_Object=MibScalar
endOfShelfConnMgmtDef=_EndOfShelfConnMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,7,10000),_EndOfShelfConnMgmtDef_Type())
endOfShelfConnMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfShelfConnMgmtDef.setStatus(_A)
_EnvMgmtDef_ObjectIdentity=ObjectIdentity
envMgmtDef=_EnvMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,8))
_EnvPortDefTable_Object=MibTable
envPortDefTable=_EnvPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1))
if mibBuilder.loadTexts:envPortDefTable.setStatus(_A)
_EnvPortDefEntry_Object=MibTableRow
envPortDefEntry=_EnvPortDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1))
envPortDefEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_N),(0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:envPortDefEntry.setStatus(_A)
_EnvPortDefRowStatus_Type=RowStatus
_EnvPortDefRowStatus_Object=MibTableColumn
envPortDefRowStatus=_EnvPortDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1,1),_EnvPortDefRowStatus_Type())
envPortDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortDefRowStatus.setStatus(_A)
_EnvPortDefTelemetry_Type=FspR7TelemetryOutput
_EnvPortDefTelemetry_Object=MibTableColumn
envPortDefTelemetry=_EnvPortDefTelemetry_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1,2),_EnvPortDefTelemetry_Type())
envPortDefTelemetry.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortDefTelemetry.setStatus(_A)
_EnvPortDefFacilityType_Type=FspR7InterfaceType
_EnvPortDefFacilityType_Object=MibTableColumn
envPortDefFacilityType=_EnvPortDefFacilityType_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1,3),_EnvPortDefFacilityType_Type())
envPortDefFacilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortDefFacilityType.setStatus(_A)
_EnvPortDefTifAlarmType_Type=SnmpAdminString
_EnvPortDefTifAlarmType_Object=MibTableColumn
envPortDefTifAlarmType=_EnvPortDefTifAlarmType_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1,4),_EnvPortDefTifAlarmType_Type())
envPortDefTifAlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortDefTifAlarmType.setStatus(_A)
_EnvPortDefTifAlarmMessage_Type=SnmpAdminString
_EnvPortDefTifAlarmMessage_Object=MibTableColumn
envPortDefTifAlarmMessage=_EnvPortDefTifAlarmMessage_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1,5),_EnvPortDefTifAlarmMessage_Type())
envPortDefTifAlarmMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortDefTifAlarmMessage.setStatus(_A)
_EnvPortDefInvertTifInputLogic_Type=FspR7InvertTelemetryInputLogic
_EnvPortDefInvertTifInputLogic_Object=MibTableColumn
envPortDefInvertTifInputLogic=_EnvPortDefInvertTifInputLogic_Object((1,3,6,1,4,1,2544,1,11,10,3,8,1,1,6),_EnvPortDefInvertTifInputLogic_Type())
envPortDefInvertTifInputLogic.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortDefInvertTifInputLogic.setStatus(_A)
_EndOfEnvPortDefTable_Type=Integer32
_EndOfEnvPortDefTable_Object=MibScalar
endOfEnvPortDefTable=_EndOfEnvPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,8,2),_EndOfEnvPortDefTable_Type())
endOfEnvPortDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEnvPortDefTable.setStatus(_A)
_EndOfEnvMgmtDef_Type=Integer32
_EndOfEnvMgmtDef_Object=MibScalar
endOfEnvMgmtDef=_EndOfEnvMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,8,10000),_EndOfEnvMgmtDef_Type())
endOfEnvMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEnvMgmtDef.setStatus(_A)
_ContainerMgmtDef_ObjectIdentity=ObjectIdentity
containerMgmtDef=_ContainerMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,9))
_ContainerDefTable_Object=MibTable
containerDefTable=_ContainerDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,9,1))
if mibBuilder.loadTexts:containerDefTable.setStatus(_A)
_ContainerDefEntry_Object=MibTableRow
containerDefEntry=_ContainerDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,9,1,1))
containerDefEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_l),(0,_C,_k),(0,_C,_j))
if mibBuilder.loadTexts:containerDefEntry.setStatus(_A)
_ContainerDefRowStatus_Type=RowStatus
_ContainerDefRowStatus_Object=MibTableColumn
containerDefRowStatus=_ContainerDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,9,1,1,1),_ContainerDefRowStatus_Type())
containerDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:containerDefRowStatus.setStatus(_A)
_ContainerDefFacilityType_Type=FspR7InterfaceType
_ContainerDefFacilityType_Object=MibTableColumn
containerDefFacilityType=_ContainerDefFacilityType_Object((1,3,6,1,4,1,2544,1,11,10,3,9,1,1,2),_ContainerDefFacilityType_Type())
containerDefFacilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:containerDefFacilityType.setStatus(_A)
_EndOfContainerDefTable_Type=Integer32
_EndOfContainerDefTable_Object=MibScalar
endOfContainerDefTable=_EndOfContainerDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,9,2),_EndOfContainerDefTable_Type())
endOfContainerDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfContainerDefTable.setStatus(_A)
_EndOfContainerMgmtDef_Type=Integer32
_EndOfContainerMgmtDef_Object=MibScalar
endOfContainerMgmtDef=_EndOfContainerMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,9,10000),_EndOfContainerMgmtDef_Type())
endOfContainerMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfContainerMgmtDef.setStatus(_A)
_OpticalLineMgmtDef_ObjectIdentity=ObjectIdentity
opticalLineMgmtDef=_OpticalLineMgmtDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,3,10))
_OpticalLineDefTable_Object=MibTable
opticalLineDefTable=_OpticalLineDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1))
if mibBuilder.loadTexts:opticalLineDefTable.setStatus(_A)
_OpticalLineDefEntry_Object=MibTableRow
opticalLineDefEntry=_OpticalLineDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1,1))
opticalLineDefEntry.setIndexNames((0,_C,_b),(0,_C,_b),(0,_C,_b),(0,_C,_b),(0,_C,_AP))
if mibBuilder.loadTexts:opticalLineDefEntry.setStatus(_A)
_OpticalLineDefRowStatus_Type=RowStatus
_OpticalLineDefRowStatus_Object=MibTableColumn
opticalLineDefRowStatus=_OpticalLineDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1,1,1),_OpticalLineDefRowStatus_Type())
opticalLineDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineDefRowStatus.setStatus(_A)
_OpticalLineDefTxLineAttenuation_Type=Integer32
_OpticalLineDefTxLineAttenuation_Object=MibTableColumn
opticalLineDefTxLineAttenuation=_OpticalLineDefTxLineAttenuation_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1,1,2),_OpticalLineDefTxLineAttenuation_Type())
opticalLineDefTxLineAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineDefTxLineAttenuation.setStatus(_A)
if mibBuilder.loadTexts:opticalLineDefTxLineAttenuation.setUnits(_K)
_OpticalLineDefRxLineAttenuation_Type=Integer32
_OpticalLineDefRxLineAttenuation_Object=MibTableColumn
opticalLineDefRxLineAttenuation=_OpticalLineDefRxLineAttenuation_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1,1,3),_OpticalLineDefRxLineAttenuation_Type())
opticalLineDefRxLineAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineDefRxLineAttenuation.setStatus(_A)
if mibBuilder.loadTexts:opticalLineDefRxLineAttenuation.setUnits(_K)
_OpticalLineDefAlias_Type=SnmpAdminString
_OpticalLineDefAlias_Object=MibTableColumn
opticalLineDefAlias=_OpticalLineDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1,1,4),_OpticalLineDefAlias_Type())
opticalLineDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineDefAlias.setStatus(_A)
_OpticalLineDefFarEndLocation_Type=SnmpAdminString
_OpticalLineDefFarEndLocation_Object=MibTableColumn
opticalLineDefFarEndLocation=_OpticalLineDefFarEndLocation_Object((1,3,6,1,4,1,2544,1,11,10,3,10,1,1,5),_OpticalLineDefFarEndLocation_Type())
opticalLineDefFarEndLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineDefFarEndLocation.setStatus(_A)
_EndOfOpticalLineDefTable_Type=Integer32
_EndOfOpticalLineDefTable_Object=MibScalar
endOfOpticalLineDefTable=_EndOfOpticalLineDefTable_Object((1,3,6,1,4,1,2544,1,11,10,3,10,2),_EndOfOpticalLineDefTable_Type())
endOfOpticalLineDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalLineDefTable.setStatus(_A)
_EndOfOpticalLineMgmtDef_Type=Integer32
_EndOfOpticalLineMgmtDef_Object=MibScalar
endOfOpticalLineMgmtDef=_EndOfOpticalLineMgmtDef_Object((1,3,6,1,4,1,2544,1,11,10,3,10,10000),_EndOfOpticalLineMgmtDef_Type())
endOfOpticalLineMgmtDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalLineMgmtDef.setStatus(_A)
_PerformanceDef_ObjectIdentity=ObjectIdentity
performanceDef=_PerformanceDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,6))
_PerformanceFacilityDef_ObjectIdentity=ObjectIdentity
performanceFacilityDef=_PerformanceFacilityDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,6,4))
_PerformanceFacilityThresholdDef_ObjectIdentity=ObjectIdentity
performanceFacilityThresholdDef=_PerformanceFacilityThresholdDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,6,4,1))
_OptThresholdConfigDefTable_Object=MibTable
optThresholdConfigDefTable=_OptThresholdConfigDefTable_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,1))
if mibBuilder.loadTexts:optThresholdConfigDefTable.setStatus(_A)
_OptThresholdConfigDefEntry_Object=MibTableRow
optThresholdConfigDefEntry=_OptThresholdConfigDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,1,1))
optThresholdConfigDefEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_S),(0,_C,_R),(0,_C,_Q))
if mibBuilder.loadTexts:optThresholdConfigDefEntry.setStatus(_A)
class _OptThresholdConfigDefLowConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,300))
_OptThresholdConfigDefLowConfig_Type.__name__=_G
_OptThresholdConfigDefLowConfig_Object=MibTableColumn
optThresholdConfigDefLowConfig=_OptThresholdConfigDefLowConfig_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,1,1,1),_OptThresholdConfigDefLowConfig_Type())
optThresholdConfigDefLowConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:optThresholdConfigDefLowConfig.setStatus(_A)
if mibBuilder.loadTexts:optThresholdConfigDefLowConfig.setUnits(_J)
class _OptThresholdConfigDefHighConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,300))
_OptThresholdConfigDefHighConfig_Type.__name__=_G
_OptThresholdConfigDefHighConfig_Object=MibTableColumn
optThresholdConfigDefHighConfig=_OptThresholdConfigDefHighConfig_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,1,1,2),_OptThresholdConfigDefHighConfig_Type())
optThresholdConfigDefHighConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:optThresholdConfigDefHighConfig.setStatus(_A)
if mibBuilder.loadTexts:optThresholdConfigDefHighConfig.setUnits(_J)
_OprThresholdConfigDefTable_Object=MibTable
oprThresholdConfigDefTable=_OprThresholdConfigDefTable_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,2))
if mibBuilder.loadTexts:oprThresholdConfigDefTable.setStatus(_A)
_OprThresholdConfigDefEntry_Object=MibTableRow
oprThresholdConfigDefEntry=_OprThresholdConfigDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,2,1))
oprThresholdConfigDefEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_S),(0,_C,_R),(0,_C,_Q))
if mibBuilder.loadTexts:oprThresholdConfigDefEntry.setStatus(_A)
class _OprThresholdConfigDefLowConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-450,260))
_OprThresholdConfigDefLowConfig_Type.__name__=_G
_OprThresholdConfigDefLowConfig_Object=MibTableColumn
oprThresholdConfigDefLowConfig=_OprThresholdConfigDefLowConfig_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,2,1,1),_OprThresholdConfigDefLowConfig_Type())
oprThresholdConfigDefLowConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:oprThresholdConfigDefLowConfig.setStatus(_A)
if mibBuilder.loadTexts:oprThresholdConfigDefLowConfig.setUnits(_J)
class _OprThresholdConfigDefHighConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-450,260))
_OprThresholdConfigDefHighConfig_Type.__name__=_G
_OprThresholdConfigDefHighConfig_Object=MibTableColumn
oprThresholdConfigDefHighConfig=_OprThresholdConfigDefHighConfig_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,2,1,2),_OprThresholdConfigDefHighConfig_Type())
oprThresholdConfigDefHighConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:oprThresholdConfigDefHighConfig.setStatus(_A)
if mibBuilder.loadTexts:oprThresholdConfigDefHighConfig.setUnits(_J)
_EndOfOprThresholdConfigDefTable_Type=Integer32
_EndOfOprThresholdConfigDefTable_Object=MibScalar
endOfOprThresholdConfigDefTable=_EndOfOprThresholdConfigDefTable_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,3),_EndOfOprThresholdConfigDefTable_Type())
endOfOprThresholdConfigDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOprThresholdConfigDefTable.setStatus(_A)
_EndOfPerformanceFacilityThresholdDef_Type=Integer32
_EndOfPerformanceFacilityThresholdDef_Object=MibScalar
endOfPerformanceFacilityThresholdDef=_EndOfPerformanceFacilityThresholdDef_Object((1,3,6,1,4,1,2544,1,11,10,6,4,1,10000),_EndOfPerformanceFacilityThresholdDef_Type())
endOfPerformanceFacilityThresholdDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPerformanceFacilityThresholdDef.setStatus(_A)
_FeatureSpecificDef_ObjectIdentity=ObjectIdentity
featureSpecificDef=_FeatureSpecificDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,7))
_FiberMapDef_ObjectIdentity=ObjectIdentity
fiberMapDef=_FiberMapDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,7,1))
_TerminationPointDefTable_Object=MibTable
terminationPointDefTable=_TerminationPointDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,1,1))
if mibBuilder.loadTexts:terminationPointDefTable.setStatus(_A)
_TerminationPointDefEntry_Object=MibTableRow
terminationPointDefEntry=_TerminationPointDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,7,1,1,1))
terminationPointDefEntry.setIndexNames((0,_C,_e),(0,_C,_f),(0,_C,_g),(0,_C,_h),(0,_C,_d))
if mibBuilder.loadTexts:terminationPointDefEntry.setStatus(_A)
_TerminationPointDefRowStatus_Type=RowStatus
_TerminationPointDefRowStatus_Object=MibTableColumn
terminationPointDefRowStatus=_TerminationPointDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,7,1,1,1,1),_TerminationPointDefRowStatus_Type())
terminationPointDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointDefRowStatus.setStatus(_A)
_TerminationPointDefAdmin_Type=FspR7AdminState
_TerminationPointDefAdmin_Object=MibTableColumn
terminationPointDefAdmin=_TerminationPointDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,7,1,1,1,2),_TerminationPointDefAdmin_Type())
terminationPointDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointDefAdmin.setStatus(_A)
_TerminationPointDefFiberDetect_Type=FspR7FiberDetect
_TerminationPointDefFiberDetect_Object=MibTableColumn
terminationPointDefFiberDetect=_TerminationPointDefFiberDetect_Object((1,3,6,1,4,1,2544,1,11,10,7,1,1,1,3),_TerminationPointDefFiberDetect_Type())
terminationPointDefFiberDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointDefFiberDetect.setStatus(_A)
_TerminationPointDefAlias_Type=SnmpAdminString
_TerminationPointDefAlias_Object=MibTableColumn
terminationPointDefAlias=_TerminationPointDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,7,1,1,1,4),_TerminationPointDefAlias_Type())
terminationPointDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointDefAlias.setStatus(_A)
_ConnectionDefTable_Object=MibTable
connectionDefTable=_ConnectionDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,1,2))
if mibBuilder.loadTexts:connectionDefTable.setStatus(_A)
_ConnectionDefEntry_Object=MibTableRow
connectionDefEntry=_ConnectionDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,7,1,2,1))
connectionDefEntry.setIndexNames((0,_C,_e),(0,_C,_f),(0,_C,_g),(0,_C,_h),(0,_C,_d),(0,_C,_e),(0,_C,_f),(0,_C,_g),(0,_C,_h),(0,_C,_d),(0,_C,_i))
if mibBuilder.loadTexts:connectionDefEntry.setStatus(_A)
_ConnectionDefRowStatus_Type=FspR7RowStatus
_ConnectionDefRowStatus_Object=MibTableColumn
connectionDefRowStatus=_ConnectionDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,7,1,2,1,1),_ConnectionDefRowStatus_Type())
connectionDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionDefRowStatus.setStatus(_A)
_ConnectionDefType_Type=FspR7TypeConnection
_ConnectionDefType_Object=MibTableColumn
connectionDefType=_ConnectionDefType_Object((1,3,6,1,4,1,2544,1,11,10,7,1,2,1,2),_ConnectionDefType_Type())
connectionDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionDefType.setStatus(_A)
_EndOfConnectionDefTable_Type=Integer32
_EndOfConnectionDefTable_Object=MibScalar
endOfConnectionDefTable=_EndOfConnectionDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,1,3),_EndOfConnectionDefTable_Type())
endOfConnectionDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfConnectionDefTable.setStatus(_A)
_EndOfFiberMapDef_Type=Integer32
_EndOfFiberMapDef_Object=MibScalar
endOfFiberMapDef=_EndOfFiberMapDef_Object((1,3,6,1,4,1,2544,1,11,10,7,1,10000),_EndOfFiberMapDef_Type())
endOfFiberMapDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFiberMapDef.setStatus(_A)
_EciDef_ObjectIdentity=ObjectIdentity
eciDef=_EciDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,7,3))
_ExternalPortDefTable_Object=MibTable
externalPortDefTable=_ExternalPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1))
if mibBuilder.loadTexts:externalPortDefTable.setStatus(_A)
_ExternalPortDefEntry_Object=MibTableRow
externalPortDefEntry=_ExternalPortDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1))
externalPortDefEntry.setIndexNames((0,_C,_AI),(0,_C,_AJ),(0,_C,_AH),(0,_C,_AG),(0,_C,_AF))
if mibBuilder.loadTexts:externalPortDefEntry.setStatus(_A)
_ExternalPortDefRowStatus_Type=FspR7RowStatus
_ExternalPortDefRowStatus_Object=MibTableColumn
externalPortDefRowStatus=_ExternalPortDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,1),_ExternalPortDefRowStatus_Type())
externalPortDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefRowStatus.setStatus(_A)
_ExternalPortDefType_Type=FspR7InterfaceType
_ExternalPortDefType_Object=MibTableColumn
externalPortDefType=_ExternalPortDefType_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,2),_ExternalPortDefType_Type())
externalPortDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefType.setStatus(_A)
_ExternalPortDefTransmitChannel_Type=FspR7ChannelIdentifier
_ExternalPortDefTransmitChannel_Object=MibTableColumn
externalPortDefTransmitChannel=_ExternalPortDefTransmitChannel_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,3),_ExternalPortDefTransmitChannel_Type())
externalPortDefTransmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefTransmitChannel.setStatus(_A)
_ExternalPortDefChannelBandwith_Type=FspR7ChannelBandwidth
_ExternalPortDefChannelBandwith_Object=MibTableColumn
externalPortDefChannelBandwith=_ExternalPortDefChannelBandwith_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,4),_ExternalPortDefChannelBandwith_Type())
externalPortDefChannelBandwith.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefChannelBandwith.setStatus(_A)
_ExternalPortDefAlias_Type=SnmpAdminString
_ExternalPortDefAlias_Object=MibTableColumn
externalPortDefAlias=_ExternalPortDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,5),_ExternalPortDefAlias_Type())
externalPortDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefAlias.setStatus(_A)
_ExternalPortDefFarEndLocation_Type=SnmpAdminString
_ExternalPortDefFarEndLocation_Object=MibTableColumn
externalPortDefFarEndLocation=_ExternalPortDefFarEndLocation_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,6),_ExternalPortDefFarEndLocation_Type())
externalPortDefFarEndLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefFarEndLocation.setStatus(_A)
_ExternalPortDefBitrate_Type=Unsigned32
_ExternalPortDefBitrate_Object=MibTableColumn
externalPortDefBitrate=_ExternalPortDefBitrate_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,7),_ExternalPortDefBitrate_Type())
externalPortDefBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefBitrate.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefBitrate.setUnits('Mbps')
_ExternalPortDefFecType_Type=FspR7FecType
_ExternalPortDefFecType_Object=MibTableColumn
externalPortDefFecType=_ExternalPortDefFecType_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,8),_ExternalPortDefFecType_Type())
externalPortDefFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefFecType.setStatus(_A)
_ExternalPortDefLineCoding_Type=FspR7LineCoding
_ExternalPortDefLineCoding_Object=MibTableColumn
externalPortDefLineCoding=_ExternalPortDefLineCoding_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,9),_ExternalPortDefLineCoding_Type())
externalPortDefLineCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefLineCoding.setStatus(_A)
_ExternalPortDefFrameFormat_Type=FspR7FrameFormat
_ExternalPortDefFrameFormat_Object=MibTableColumn
externalPortDefFrameFormat=_ExternalPortDefFrameFormat_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,10),_ExternalPortDefFrameFormat_Type())
externalPortDefFrameFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefFrameFormat.setStatus(_A)
class _ExternalPortDefOpticalPowerTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9900,600))
_ExternalPortDefOpticalPowerTx_Type.__name__=_G
_ExternalPortDefOpticalPowerTx_Object=MibTableColumn
externalPortDefOpticalPowerTx=_ExternalPortDefOpticalPowerTx_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,11),_ExternalPortDefOpticalPowerTx_Type())
externalPortDefOpticalPowerTx.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefOpticalPowerTx.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefOpticalPowerTx.setUnits(_J)
class _ExternalPortDefOsnrTransmit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,58))
_ExternalPortDefOsnrTransmit_Type.__name__=_D
_ExternalPortDefOsnrTransmit_Object=MibTableColumn
externalPortDefOsnrTransmit=_ExternalPortDefOsnrTransmit_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,12),_ExternalPortDefOsnrTransmit_Type())
externalPortDefOsnrTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefOsnrTransmit.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefOsnrTransmit.setUnits('dB')
class _ExternalPortDefPmdTransmit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_ExternalPortDefPmdTransmit_Type.__name__=_D
_ExternalPortDefPmdTransmit_Object=MibTableColumn
externalPortDefPmdTransmit=_ExternalPortDefPmdTransmit_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,13),_ExternalPortDefPmdTransmit_Type())
externalPortDefPmdTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefPmdTransmit.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefPmdTransmit.setUnits('ps')
class _ExternalPortDefChromDisperTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60000,60000))
_ExternalPortDefChromDisperTx_Type.__name__=_G
_ExternalPortDefChromDisperTx_Object=MibTableColumn
externalPortDefChromDisperTx=_ExternalPortDefChromDisperTx_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,14),_ExternalPortDefChromDisperTx_Type())
externalPortDefChromDisperTx.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefChromDisperTx.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefChromDisperTx.setUnits(_c)
class _ExternalPortDefMinOsnrRcv_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,58))
_ExternalPortDefMinOsnrRcv_Type.__name__=_D
_ExternalPortDefMinOsnrRcv_Object=MibTableColumn
externalPortDefMinOsnrRcv=_ExternalPortDefMinOsnrRcv_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,15),_ExternalPortDefMinOsnrRcv_Type())
externalPortDefMinOsnrRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMinOsnrRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefMinOsnrRcv.setUnits('dB')
class _ExternalPortDefMinOptPowerRcv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2500,0))
_ExternalPortDefMinOptPowerRcv_Type.__name__=_G
_ExternalPortDefMinOptPowerRcv_Object=MibTableColumn
externalPortDefMinOptPowerRcv=_ExternalPortDefMinOptPowerRcv_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,16),_ExternalPortDefMinOptPowerRcv_Type())
externalPortDefMinOptPowerRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMinOptPowerRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefMinOptPowerRcv.setUnits(_J)
class _ExternalPortDefMaxOptPowerRcv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,1000))
_ExternalPortDefMaxOptPowerRcv_Type.__name__=_G
_ExternalPortDefMaxOptPowerRcv_Object=MibTableColumn
externalPortDefMaxOptPowerRcv=_ExternalPortDefMaxOptPowerRcv_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,17),_ExternalPortDefMaxOptPowerRcv_Type())
externalPortDefMaxOptPowerRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMaxOptPowerRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefMaxOptPowerRcv.setUnits(_J)
class _ExternalPortDefMaxPmdRcv_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_ExternalPortDefMaxPmdRcv_Type.__name__=_D
_ExternalPortDefMaxPmdRcv_Object=MibTableColumn
externalPortDefMaxPmdRcv=_ExternalPortDefMaxPmdRcv_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,18),_ExternalPortDefMaxPmdRcv_Type())
externalPortDefMaxPmdRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMaxPmdRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefMaxPmdRcv.setUnits('ps')
class _ExternalPortDefMinChromDisperRcv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60000,60000))
_ExternalPortDefMinChromDisperRcv_Type.__name__=_G
_ExternalPortDefMinChromDisperRcv_Object=MibTableColumn
externalPortDefMinChromDisperRcv=_ExternalPortDefMinChromDisperRcv_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,19),_ExternalPortDefMinChromDisperRcv_Type())
externalPortDefMinChromDisperRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMinChromDisperRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefMinChromDisperRcv.setUnits(_c)
class _ExternalPortDefMaxChromDisperRcv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60000,60000))
_ExternalPortDefMaxChromDisperRcv_Type.__name__=_G
_ExternalPortDefMaxChromDisperRcv_Object=MibTableColumn
externalPortDefMaxChromDisperRcv=_ExternalPortDefMaxChromDisperRcv_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,20),_ExternalPortDefMaxChromDisperRcv_Type())
externalPortDefMaxChromDisperRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMaxChromDisperRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortDefMaxChromDisperRcv.setUnits(_c)
_ExternalPortDefMaxBitErrorRate_Type=FspR7MaxBitErrorRate
_ExternalPortDefMaxBitErrorRate_Object=MibTableColumn
externalPortDefMaxBitErrorRate=_ExternalPortDefMaxBitErrorRate_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,21),_ExternalPortDefMaxBitErrorRate_Type())
externalPortDefMaxBitErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefMaxBitErrorRate.setStatus(_A)
_ExternalPortDefSourceProfile_Type=SnmpAdminString
_ExternalPortDefSourceProfile_Object=MibTableColumn
externalPortDefSourceProfile=_ExternalPortDefSourceProfile_Object((1,3,6,1,4,1,2544,1,11,10,7,3,1,1,22),_ExternalPortDefSourceProfile_Type())
externalPortDefSourceProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortDefSourceProfile.setStatus(_A)
_EndOfExternalPortDefTable_Type=Integer32
_EndOfExternalPortDefTable_Object=MibScalar
endOfExternalPortDefTable=_EndOfExternalPortDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,3,2),_EndOfExternalPortDefTable_Type())
endOfExternalPortDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfExternalPortDefTable.setStatus(_A)
_EndOfEciDef_Type=Integer32
_EndOfEciDef_Object=MibScalar
endOfEciDef=_EndOfEciDef_Object((1,3,6,1,4,1,2544,1,11,10,7,3,10000),_EndOfEciDef_Type())
endOfEciDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEciDef.setStatus(_A)
_ChangeServiceDef_ObjectIdentity=ObjectIdentity
changeServiceDef=_ChangeServiceDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,7,5))
_ChangePhysicalPortServiceDefTable_Object=MibTable
changePhysicalPortServiceDefTable=_ChangePhysicalPortServiceDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1))
if mibBuilder.loadTexts:changePhysicalPortServiceDefTable.setStatus(_A)
_ChangePhysicalPortServiceDefEntry_Object=MibTableRow
changePhysicalPortServiceDefEntry=_ChangePhysicalPortServiceDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1))
changePhysicalPortServiceDefEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_S),(0,_C,_R),(0,_C,_Q))
if mibBuilder.loadTexts:changePhysicalPortServiceDefEntry.setStatus(_A)
_ChangePhysicalPortServiceDefRowStatus_Type=RowStatus
_ChangePhysicalPortServiceDefRowStatus_Object=MibTableColumn
changePhysicalPortServiceDefRowStatus=_ChangePhysicalPortServiceDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,1),_ChangePhysicalPortServiceDefRowStatus_Type())
changePhysicalPortServiceDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefRowStatus.setStatus(_A)
_ChangePhysicalPortServiceDefType_Type=FspR7InterfaceType
_ChangePhysicalPortServiceDefType_Object=MibTableColumn
changePhysicalPortServiceDefType=_ChangePhysicalPortServiceDefType_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,2),_ChangePhysicalPortServiceDefType_Type())
changePhysicalPortServiceDefType.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefType.setStatus(_A)
_ChangePhysicalPortServiceDefAdmin_Type=FspR7AdminState
_ChangePhysicalPortServiceDefAdmin_Object=MibTableColumn
changePhysicalPortServiceDefAdmin=_ChangePhysicalPortServiceDefAdmin_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,3),_ChangePhysicalPortServiceDefAdmin_Type())
changePhysicalPortServiceDefAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefAdmin.setStatus(_A)
_ChangePhysicalPortServiceDefAlias_Type=SnmpAdminString
_ChangePhysicalPortServiceDefAlias_Object=MibTableColumn
changePhysicalPortServiceDefAlias=_ChangePhysicalPortServiceDefAlias_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,4),_ChangePhysicalPortServiceDefAlias_Type())
changePhysicalPortServiceDefAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefAlias.setStatus(_A)
_ChangePhysicalPortServiceDefAlsMode_Type=FspR7AlsMode
_ChangePhysicalPortServiceDefAlsMode_Object=MibTableColumn
changePhysicalPortServiceDefAlsMode=_ChangePhysicalPortServiceDefAlsMode_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,5),_ChangePhysicalPortServiceDefAlsMode_Type())
changePhysicalPortServiceDefAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefAlsMode.setStatus(_A)
_ChangePhysicalPortServiceDefBehaviour_Type=FspR7PortBehaviour
_ChangePhysicalPortServiceDefBehaviour_Object=MibTableColumn
changePhysicalPortServiceDefBehaviour=_ChangePhysicalPortServiceDefBehaviour_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,6),_ChangePhysicalPortServiceDefBehaviour_Type())
changePhysicalPortServiceDefBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefBehaviour.setStatus(_A)
class _ChangePhysicalPortServiceDefDispersionSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50000,50000))
_ChangePhysicalPortServiceDefDispersionSetting_Type.__name__=_G
_ChangePhysicalPortServiceDefDispersionSetting_Object=MibTableColumn
changePhysicalPortServiceDefDispersionSetting=_ChangePhysicalPortServiceDefDispersionSetting_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,7),_ChangePhysicalPortServiceDefDispersionSetting_Type())
changePhysicalPortServiceDefDispersionSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefDispersionSetting.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefDispersionSetting.setUnits(_c)
_ChangePhysicalPortServiceDefDispersionMode_Type=FspR7DispersionModes
_ChangePhysicalPortServiceDefDispersionMode_Object=MibTableColumn
changePhysicalPortServiceDefDispersionMode=_ChangePhysicalPortServiceDefDispersionMode_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,8),_ChangePhysicalPortServiceDefDispersionMode_Type())
changePhysicalPortServiceDefDispersionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefDispersionMode.setStatus(_A)
_ChangePhysicalPortServiceDefChannelProv_Type=FspR7ChannelIdentifier
_ChangePhysicalPortServiceDefChannelProv_Object=MibTableColumn
changePhysicalPortServiceDefChannelProv=_ChangePhysicalPortServiceDefChannelProv_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,9),_ChangePhysicalPortServiceDefChannelProv_Type())
changePhysicalPortServiceDefChannelProv.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefChannelProv.setStatus(_A)
_ChangePhysicalPortServiceDefWdmRxChannel_Type=FspR7ChannelIdentifier
_ChangePhysicalPortServiceDefWdmRxChannel_Object=MibTableColumn
changePhysicalPortServiceDefWdmRxChannel=_ChangePhysicalPortServiceDefWdmRxChannel_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,10),_ChangePhysicalPortServiceDefWdmRxChannel_Type())
changePhysicalPortServiceDefWdmRxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefWdmRxChannel.setStatus(_A)
_ChangePhysicalPortServiceDefCodeGain_Type=FspR7CodeGain
_ChangePhysicalPortServiceDefCodeGain_Object=MibTableColumn
changePhysicalPortServiceDefCodeGain=_ChangePhysicalPortServiceDefCodeGain_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,11),_ChangePhysicalPortServiceDefCodeGain_Type())
changePhysicalPortServiceDefCodeGain.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefCodeGain.setStatus(_A)
_ChangePhysicalPortServiceDefXfpDecisionThres_Type=FspR7XfpDecisionThres
_ChangePhysicalPortServiceDefXfpDecisionThres_Object=MibTableColumn
changePhysicalPortServiceDefXfpDecisionThres=_ChangePhysicalPortServiceDefXfpDecisionThres_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,12),_ChangePhysicalPortServiceDefXfpDecisionThres_Type())
changePhysicalPortServiceDefXfpDecisionThres.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefXfpDecisionThres.setStatus(_A)
_ChangePhysicalPortServiceDefDisparityCorrection_Type=EnableState
_ChangePhysicalPortServiceDefDisparityCorrection_Object=MibTableColumn
changePhysicalPortServiceDefDisparityCorrection=_ChangePhysicalPortServiceDefDisparityCorrection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,13),_ChangePhysicalPortServiceDefDisparityCorrection_Type())
changePhysicalPortServiceDefDisparityCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefDisparityCorrection.setStatus(_A)
_ChangePhysicalPortServiceDefEqlzAdmin_Type=FspR7EqlzAdminState
_ChangePhysicalPortServiceDefEqlzAdmin_Object=MibTableColumn
changePhysicalPortServiceDefEqlzAdmin=_ChangePhysicalPortServiceDefEqlzAdmin_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,14),_ChangePhysicalPortServiceDefEqlzAdmin_Type())
changePhysicalPortServiceDefEqlzAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefEqlzAdmin.setStatus(_A)
_ChangePhysicalPortServiceDefErrorForwarding_Type=FspR7ErrorFwdMode
_ChangePhysicalPortServiceDefErrorForwarding_Object=MibTableColumn
changePhysicalPortServiceDefErrorForwarding=_ChangePhysicalPortServiceDefErrorForwarding_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,15),_ChangePhysicalPortServiceDefErrorForwarding_Type())
changePhysicalPortServiceDefErrorForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefErrorForwarding.setStatus(_A)
_ChangePhysicalPortServiceDefFecType_Type=FspR7FecType
_ChangePhysicalPortServiceDefFecType_Object=MibTableColumn
changePhysicalPortServiceDefFecType=_ChangePhysicalPortServiceDefFecType_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,16),_ChangePhysicalPortServiceDefFecType_Type())
changePhysicalPortServiceDefFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefFecType.setStatus(_A)
_ChangePhysicalPortServiceDefFarEndCommunication_Type=FspR7YesNo
_ChangePhysicalPortServiceDefFarEndCommunication_Object=MibTableColumn
changePhysicalPortServiceDefFarEndCommunication=_ChangePhysicalPortServiceDefFarEndCommunication_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,17),_ChangePhysicalPortServiceDefFarEndCommunication_Type())
changePhysicalPortServiceDefFarEndCommunication.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefFarEndCommunication.setStatus(_A)
_ChangePhysicalPortServiceDefFlowControl_Type=FspR7FlowControlMode
_ChangePhysicalPortServiceDefFlowControl_Object=MibTableColumn
changePhysicalPortServiceDefFlowControl=_ChangePhysicalPortServiceDefFlowControl_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,18),_ChangePhysicalPortServiceDefFlowControl_Type())
changePhysicalPortServiceDefFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefFlowControl.setStatus(_A)
_ChangePhysicalPortServiceDefLaneChannelSetting_Type=FspR7ChannelIdentifier
_ChangePhysicalPortServiceDefLaneChannelSetting_Object=MibTableColumn
changePhysicalPortServiceDefLaneChannelSetting=_ChangePhysicalPortServiceDefLaneChannelSetting_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,19),_ChangePhysicalPortServiceDefLaneChannelSetting_Type())
changePhysicalPortServiceDefLaneChannelSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaneChannelSetting.setStatus(_A)
_ChangePhysicalPortServiceDefLaserDelayTimer_Type=FspR7LaserDelayTimer
_ChangePhysicalPortServiceDefLaserDelayTimer_Object=MibTableColumn
changePhysicalPortServiceDefLaserDelayTimer=_ChangePhysicalPortServiceDefLaserDelayTimer_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,20),_ChangePhysicalPortServiceDefLaserDelayTimer_Type())
changePhysicalPortServiceDefLaserDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaserDelayTimer.setStatus(_A)
class _ChangePhysicalPortServiceDefLaserOffTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_ChangePhysicalPortServiceDefLaserOffTimer_Type.__name__=_D
_ChangePhysicalPortServiceDefLaserOffTimer_Object=MibTableColumn
changePhysicalPortServiceDefLaserOffTimer=_ChangePhysicalPortServiceDefLaserOffTimer_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,21),_ChangePhysicalPortServiceDefLaserOffTimer_Type())
changePhysicalPortServiceDefLaserOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaserOffTimer.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaserOffTimer.setUnits(_V)
class _ChangePhysicalPortServiceDefLaserOnTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_ChangePhysicalPortServiceDefLaserOnTimer_Type.__name__=_D
_ChangePhysicalPortServiceDefLaserOnTimer_Object=MibTableColumn
changePhysicalPortServiceDefLaserOnTimer=_ChangePhysicalPortServiceDefLaserOnTimer_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,22),_ChangePhysicalPortServiceDefLaserOnTimer_Type())
changePhysicalPortServiceDefLaserOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaserOnTimer.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaserOnTimer.setUnits(_V)
_ChangePhysicalPortServiceDefLaserOffDelayFunction_Type=EnableState
_ChangePhysicalPortServiceDefLaserOffDelayFunction_Object=MibTableColumn
changePhysicalPortServiceDefLaserOffDelayFunction=_ChangePhysicalPortServiceDefLaserOffDelayFunction_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,23),_ChangePhysicalPortServiceDefLaserOffDelayFunction_Type())
changePhysicalPortServiceDefLaserOffDelayFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefLaserOffDelayFunction.setStatus(_A)
_ChangePhysicalPortServiceDefAutoPTassignment_Type=FspR7ManualAuto
_ChangePhysicalPortServiceDefAutoPTassignment_Object=MibTableColumn
changePhysicalPortServiceDefAutoPTassignment=_ChangePhysicalPortServiceDefAutoPTassignment_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,24),_ChangePhysicalPortServiceDefAutoPTassignment_Type())
changePhysicalPortServiceDefAutoPTassignment.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefAutoPTassignment.setStatus(_A)
_ChangePhysicalPortServiceDefTributarySlotMethod_Type=FspR7ManualAuto
_ChangePhysicalPortServiceDefTributarySlotMethod_Object=MibTableColumn
changePhysicalPortServiceDefTributarySlotMethod=_ChangePhysicalPortServiceDefTributarySlotMethod_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,25),_ChangePhysicalPortServiceDefTributarySlotMethod_Type())
changePhysicalPortServiceDefTributarySlotMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTributarySlotMethod.setStatus(_A)
class _ChangePhysicalPortServiceDefOpticalSetPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,50))
_ChangePhysicalPortServiceDefOpticalSetPoint_Type.__name__=_G
_ChangePhysicalPortServiceDefOpticalSetPoint_Object=MibTableColumn
changePhysicalPortServiceDefOpticalSetPoint=_ChangePhysicalPortServiceDefOpticalSetPoint_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,26),_ChangePhysicalPortServiceDefOpticalSetPoint_Type())
changePhysicalPortServiceDefOpticalSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefOpticalSetPoint.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefOpticalSetPoint.setUnits(_J)
_ChangePhysicalPortServiceDefOpuPayloadType_Type=FspR7OpuPayloadType
_ChangePhysicalPortServiceDefOpuPayloadType_Object=MibTableColumn
changePhysicalPortServiceDefOpuPayloadType=_ChangePhysicalPortServiceDefOpuPayloadType_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,27),_ChangePhysicalPortServiceDefOpuPayloadType_Type())
changePhysicalPortServiceDefOpuPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefOpuPayloadType.setStatus(_A)
_ChangePhysicalPortServiceDefSigDegThresSonetLine_Type=FspR7BERThreshold
_ChangePhysicalPortServiceDefSigDegThresSonetLine_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresSonetLine=_ChangePhysicalPortServiceDefSigDegThresSonetLine_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,28),_ChangePhysicalPortServiceDefSigDegThresSonetLine_Type())
changePhysicalPortServiceDefSigDegThresSonetLine.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresSonetLine.setStatus(_A)
class _ChangePhysicalPortServiceDefSigDegThresSdhMs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresSdhMs_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegThresSdhMs_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresSdhMs=_ChangePhysicalPortServiceDefSigDegThresSdhMs_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,29),_ChangePhysicalPortServiceDefSigDegThresSdhMs_Type())
changePhysicalPortServiceDefSigDegThresSdhMs.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresSdhMs.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresSdhMs.setUnits(_H)
class _ChangePhysicalPortServiceDefSigDegThresOtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresOtu_Type.__name__=_G
_ChangePhysicalPortServiceDefSigDegThresOtu_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresOtu=_ChangePhysicalPortServiceDefSigDegThresOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,30),_ChangePhysicalPortServiceDefSigDegThresOtu_Type())
changePhysicalPortServiceDefSigDegThresOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOtu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOtu.setUnits(_H)
class _ChangePhysicalPortServiceDefSigDegThresOdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresOdu_Type.__name__=_G
_ChangePhysicalPortServiceDefSigDegThresOdu_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresOdu=_ChangePhysicalPortServiceDefSigDegThresOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,31),_ChangePhysicalPortServiceDefSigDegThresOdu_Type())
changePhysicalPortServiceDefSigDegThresOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOdu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOdu.setUnits(_H)
class _ChangePhysicalPortServiceDefSigDegThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_ChangePhysicalPortServiceDefSigDegThreshold_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegThreshold_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThreshold=_ChangePhysicalPortServiceDefSigDegThreshold_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,32),_ChangePhysicalPortServiceDefSigDegThreshold_Type())
changePhysicalPortServiceDefSigDegThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThreshold.setStatus(_A)
class _ChangePhysicalPortServiceDefSigDegPcslThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegPcslThreshold_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPcslThreshold_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPcslThreshold=_ChangePhysicalPortServiceDefSigDegPcslThreshold_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,33),_ChangePhysicalPortServiceDefSigDegPcslThreshold_Type())
changePhysicalPortServiceDefSigDegPcslThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPcslThreshold.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPcslThreshold.setUnits(_H)
_ChangePhysicalPortServiceDefSigDegThresSonetSection_Type=FspR7BERThresholdSection
_ChangePhysicalPortServiceDefSigDegThresSonetSection_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresSonetSection=_ChangePhysicalPortServiceDefSigDegThresSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,34),_ChangePhysicalPortServiceDefSigDegThresSonetSection_Type())
changePhysicalPortServiceDefSigDegThresSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresSonetSection.setStatus(_A)
class _ChangePhysicalPortServiceDefSigDegThresSdhSection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresSdhSection_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegThresSdhSection_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresSdhSection=_ChangePhysicalPortServiceDefSigDegThresSdhSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,35),_ChangePhysicalPortServiceDefSigDegThresSdhSection_Type())
changePhysicalPortServiceDefSigDegThresSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresSdhSection.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresSdhSection.setUnits(_H)
class _ChangePhysicalPortServiceDefSigDegThresOduTcmA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresOduTcmA_Type.__name__=_G
_ChangePhysicalPortServiceDefSigDegThresOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresOduTcmA=_ChangePhysicalPortServiceDefSigDegThresOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,36),_ChangePhysicalPortServiceDefSigDegThresOduTcmA_Type())
changePhysicalPortServiceDefSigDegThresOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOduTcmA.setUnits(_H)
class _ChangePhysicalPortServiceDefSigDegThresOduTcmB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresOduTcmB_Type.__name__=_G
_ChangePhysicalPortServiceDefSigDegThresOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresOduTcmB=_ChangePhysicalPortServiceDefSigDegThresOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,37),_ChangePhysicalPortServiceDefSigDegThresOduTcmB_Type())
changePhysicalPortServiceDefSigDegThresOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOduTcmB.setUnits(_H)
class _ChangePhysicalPortServiceDefSigDegThresOduTcmC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ChangePhysicalPortServiceDefSigDegThresOduTcmC_Type.__name__=_G
_ChangePhysicalPortServiceDefSigDegThresOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefSigDegThresOduTcmC=_ChangePhysicalPortServiceDefSigDegThresOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,38),_ChangePhysicalPortServiceDefSigDegThresOduTcmC_Type())
changePhysicalPortServiceDefSigDegThresOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegThresOduTcmC.setUnits(_H)
class _ChangePhysicalPortServiceDefSignalDegradePeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSignalDegradePeriod_Type.__name__=_D
_ChangePhysicalPortServiceDefSignalDegradePeriod_Object=MibTableColumn
changePhysicalPortServiceDefSignalDegradePeriod=_ChangePhysicalPortServiceDefSignalDegradePeriod_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,39),_ChangePhysicalPortServiceDefSignalDegradePeriod_Type())
changePhysicalPortServiceDefSignalDegradePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSignalDegradePeriod.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSignalDegradePeriod.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodOdu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSigDegPeriodOdu_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodOdu_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOdu=_ChangePhysicalPortServiceDefSigDegPeriodOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,40),_ChangePhysicalPortServiceDefSigDegPeriodOdu_Type())
changePhysicalPortServiceDefSigDegPeriodOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOdu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOdu.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodOtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSigDegPeriodOtu_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodOtu_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOtu=_ChangePhysicalPortServiceDefSigDegPeriodOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,41),_ChangePhysicalPortServiceDefSigDegPeriodOtu_Type())
changePhysicalPortServiceDefSigDegPeriodOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOtu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOtu.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodIntegration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ChangePhysicalPortServiceDefSigDegPeriodIntegration_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodIntegration_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodIntegration=_ChangePhysicalPortServiceDefSigDegPeriodIntegration_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,42),_ChangePhysicalPortServiceDefSigDegPeriodIntegration_Type())
changePhysicalPortServiceDefSigDegPeriodIntegration.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodIntegration.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodIntegration.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodSdhSection=_ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,43),_ChangePhysicalPortServiceDefSigDegPeriodSdhSection_Type())
changePhysicalPortServiceDefSigDegPeriodSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodSdhSection.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodSdhSection.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOduTcmA=_ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,44),_ChangePhysicalPortServiceDefSigDegPeriodOduTcmA_Type())
changePhysicalPortServiceDefSigDegPeriodOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOduTcmA.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOduTcmB=_ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,45),_ChangePhysicalPortServiceDefSigDegPeriodOduTcmB_Type())
changePhysicalPortServiceDefSigDegPeriodOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOduTcmB.setUnits(_I)
class _ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Type.__name__=_D
_ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefSigDegPeriodOduTcmC=_ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,46),_ChangePhysicalPortServiceDefSigDegPeriodOduTcmC_Type())
changePhysicalPortServiceDefSigDegPeriodOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefSigDegPeriodOduTcmC.setUnits(_I)
_ChangePhysicalPortServiceDefOtnStuffing_Type=FspR7Stuff
_ChangePhysicalPortServiceDefOtnStuffing_Object=MibTableColumn
changePhysicalPortServiceDefOtnStuffing=_ChangePhysicalPortServiceDefOtnStuffing_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,47),_ChangePhysicalPortServiceDefOtnStuffing_Type())
changePhysicalPortServiceDefOtnStuffing.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefOtnStuffing.setStatus(_A)
_ChangePhysicalPortServiceDefTcmALevel_Type=OtnTcmLevel
_ChangePhysicalPortServiceDefTcmALevel_Object=MibTableColumn
changePhysicalPortServiceDefTcmALevel=_ChangePhysicalPortServiceDefTcmALevel_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,48),_ChangePhysicalPortServiceDefTcmALevel_Type())
changePhysicalPortServiceDefTcmALevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTcmALevel.setStatus(_A)
_ChangePhysicalPortServiceDefTcmBLevel_Type=OtnTcmLevel
_ChangePhysicalPortServiceDefTcmBLevel_Object=MibTableColumn
changePhysicalPortServiceDefTcmBLevel=_ChangePhysicalPortServiceDefTcmBLevel_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,49),_ChangePhysicalPortServiceDefTcmBLevel_Type())
changePhysicalPortServiceDefTcmBLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTcmBLevel.setStatus(_A)
_ChangePhysicalPortServiceDefTcmCLevel_Type=OtnTcmLevel
_ChangePhysicalPortServiceDefTcmCLevel_Object=MibTableColumn
changePhysicalPortServiceDefTcmCLevel=_ChangePhysicalPortServiceDefTcmCLevel_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,50),_ChangePhysicalPortServiceDefTcmCLevel_Type())
changePhysicalPortServiceDefTcmCLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTcmCLevel.setStatus(_A)
_ChangePhysicalPortServiceDefTerminationLevel_Type=OhTerminationLevel
_ChangePhysicalPortServiceDefTerminationLevel_Object=MibTableColumn
changePhysicalPortServiceDefTerminationLevel=_ChangePhysicalPortServiceDefTerminationLevel_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,51),_ChangePhysicalPortServiceDefTerminationLevel_Type())
changePhysicalPortServiceDefTerminationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTerminationLevel.setStatus(_A)
_ChangePhysicalPortServiceDefTimingSource_Type=SonetTimingSource
_ChangePhysicalPortServiceDefTimingSource_Object=MibTableColumn
changePhysicalPortServiceDefTimingSource=_ChangePhysicalPortServiceDefTimingSource_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,52),_ChangePhysicalPortServiceDefTimingSource_Type())
changePhysicalPortServiceDefTimingSource.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimingSource.setStatus(_A)
_ChangePhysicalPortServiceDefTimModeOdu_Type=TimMode
_ChangePhysicalPortServiceDefTimModeOdu_Object=MibTableColumn
changePhysicalPortServiceDefTimModeOdu=_ChangePhysicalPortServiceDefTimModeOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,53),_ChangePhysicalPortServiceDefTimModeOdu_Type())
changePhysicalPortServiceDefTimModeOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimModeOdu.setStatus(_A)
_ChangePhysicalPortServiceDefTimModeOtu_Type=TimMode
_ChangePhysicalPortServiceDefTimModeOtu_Object=MibTableColumn
changePhysicalPortServiceDefTimModeOtu=_ChangePhysicalPortServiceDefTimModeOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,54),_ChangePhysicalPortServiceDefTimModeOtu_Type())
changePhysicalPortServiceDefTimModeOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimModeOtu.setStatus(_A)
_ChangePhysicalPortServiceDefTimModeSonetSection_Type=TimMode
_ChangePhysicalPortServiceDefTimModeSonetSection_Object=MibTableColumn
changePhysicalPortServiceDefTimModeSonetSection=_ChangePhysicalPortServiceDefTimModeSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,55),_ChangePhysicalPortServiceDefTimModeSonetSection_Type())
changePhysicalPortServiceDefTimModeSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimModeSonetSection.setStatus(_A)
_ChangePhysicalPortServiceDefTimModeOduTcmA_Type=TimMode
_ChangePhysicalPortServiceDefTimModeOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefTimModeOduTcmA=_ChangePhysicalPortServiceDefTimModeOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,56),_ChangePhysicalPortServiceDefTimModeOduTcmA_Type())
changePhysicalPortServiceDefTimModeOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimModeOduTcmA.setStatus(_A)
_ChangePhysicalPortServiceDefTimModeOduTcmB_Type=TimMode
_ChangePhysicalPortServiceDefTimModeOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefTimModeOduTcmB=_ChangePhysicalPortServiceDefTimModeOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,57),_ChangePhysicalPortServiceDefTimModeOduTcmB_Type())
changePhysicalPortServiceDefTimModeOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimModeOduTcmB.setStatus(_A)
_ChangePhysicalPortServiceDefTimModeOduTcmC_Type=TimMode
_ChangePhysicalPortServiceDefTimModeOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefTimModeOduTcmC=_ChangePhysicalPortServiceDefTimModeOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,58),_ChangePhysicalPortServiceDefTimModeOduTcmC_Type())
changePhysicalPortServiceDefTimModeOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTimModeOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceDefTraceFormSonetSection_Type=SonetTraceForm
_ChangePhysicalPortServiceDefTraceFormSonetSection_Object=MibTableColumn
changePhysicalPortServiceDefTraceFormSonetSection=_ChangePhysicalPortServiceDefTraceFormSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,59),_ChangePhysicalPortServiceDefTraceFormSonetSection_Type())
changePhysicalPortServiceDefTraceFormSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceFormSonetSection.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceExpectedSonetSection_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_ChangePhysicalPortServiceDefTraceExpectedSonetSection_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceExpectedSonetSection_Object=MibTableColumn
changePhysicalPortServiceDefTraceExpectedSonetSection=_ChangePhysicalPortServiceDefTraceExpectedSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,60),_ChangePhysicalPortServiceDefTraceExpectedSonetSection_Type())
changePhysicalPortServiceDefTraceExpectedSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceExpectedSonetSection.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitSonetSection_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_ChangePhysicalPortServiceDefTraceTransmitSonetSection_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitSonetSection_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitSonetSection=_ChangePhysicalPortServiceDefTraceTransmitSonetSection_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,61),_ChangePhysicalPortServiceDefTraceTransmitSonetSection_Type())
changePhysicalPortServiceDefTraceTransmitSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitSonetSection.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceExpectedOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceExpectedOtu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceExpectedOtu_Object=MibTableColumn
changePhysicalPortServiceDefTraceExpectedOtu=_ChangePhysicalPortServiceDefTraceExpectedOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,62),_ChangePhysicalPortServiceDefTraceExpectedOtu_Type())
changePhysicalPortServiceDefTraceExpectedOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceExpectedOtu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOtu=_ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,63),_ChangePhysicalPortServiceDefTraceTransmitSapiOtu_Type())
changePhysicalPortServiceDefTraceTransmitSapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitSapiOtu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOtu=_ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,64),_ChangePhysicalPortServiceDefTraceTransmitDapiOtu_Type())
changePhysicalPortServiceDefTraceTransmitDapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitDapiOtu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOtu=_ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,65),_ChangePhysicalPortServiceDefTraceTransmitOpspOtu_Type())
changePhysicalPortServiceDefTraceTransmitOpspOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitOpspOtu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceExpectedOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceExpectedOdu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceExpectedOdu_Object=MibTableColumn
changePhysicalPortServiceDefTraceExpectedOdu=_ChangePhysicalPortServiceDefTraceExpectedOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,66),_ChangePhysicalPortServiceDefTraceExpectedOdu_Type())
changePhysicalPortServiceDefTraceExpectedOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceExpectedOdu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOdu=_ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,67),_ChangePhysicalPortServiceDefTraceTransmitSapiOdu_Type())
changePhysicalPortServiceDefTraceTransmitSapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitSapiOdu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOdu=_ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,68),_ChangePhysicalPortServiceDefTraceTransmitDapiOdu_Type())
changePhysicalPortServiceDefTraceTransmitDapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitDapiOdu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOdu=_ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,69),_ChangePhysicalPortServiceDefTraceTransmitOpspOdu_Type())
changePhysicalPortServiceDefTraceTransmitOpspOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitOpspOdu.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefTraceExpectedOduTcmA=_ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,70),_ChangePhysicalPortServiceDefTraceExpectedOduTcmA_Type())
changePhysicalPortServiceDefTraceExpectedOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceExpectedOduTcmA.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOduTcmA=_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,71),_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmA_Type())
changePhysicalPortServiceDefTraceTransmitSapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitSapiOduTcmA.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOduTcmA=_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,72),_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmA_Type())
changePhysicalPortServiceDefTraceTransmitDapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitDapiOduTcmA.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOduTcmA=_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,73),_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmA_Type())
changePhysicalPortServiceDefTraceTransmitOpspOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitOpspOduTcmA.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefTraceExpectedOduTcmB=_ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,74),_ChangePhysicalPortServiceDefTraceExpectedOduTcmB_Type())
changePhysicalPortServiceDefTraceExpectedOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceExpectedOduTcmB.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOduTcmB=_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,75),_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmB_Type())
changePhysicalPortServiceDefTraceTransmitSapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitSapiOduTcmB.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOduTcmB=_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,76),_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmB_Type())
changePhysicalPortServiceDefTraceTransmitDapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitDapiOduTcmB.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOduTcmB=_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,77),_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmB_Type())
changePhysicalPortServiceDefTraceTransmitOpspOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitOpspOduTcmB.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefTraceExpectedOduTcmC=_ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,78),_ChangePhysicalPortServiceDefTraceExpectedOduTcmC_Type())
changePhysicalPortServiceDefTraceExpectedOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceExpectedOduTcmC.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitSapiOduTcmC=_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,79),_ChangePhysicalPortServiceDefTraceTransmitSapiOduTcmC_Type())
changePhysicalPortServiceDefTraceTransmitSapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitSapiOduTcmC.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitDapiOduTcmC=_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,80),_ChangePhysicalPortServiceDefTraceTransmitDapiOduTcmC_Type())
changePhysicalPortServiceDefTraceTransmitDapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitDapiOduTcmC.setStatus(_A)
class _ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Type.__name__=_E
_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Object=MibTableColumn
changePhysicalPortServiceDefTraceTransmitOpspOduTcmC=_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,81),_ChangePhysicalPortServiceDefTraceTransmitOpspOduTcmC_Type())
changePhysicalPortServiceDefTraceTransmitOpspOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTraceTransmitOpspOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceDefTxOffDelay_Type=FspR7EnableDisable
_ChangePhysicalPortServiceDefTxOffDelay_Object=MibTableColumn
changePhysicalPortServiceDefTxOffDelay=_ChangePhysicalPortServiceDefTxOffDelay_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,82),_ChangePhysicalPortServiceDefTxOffDelay_Type())
changePhysicalPortServiceDefTxOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefTxOffDelay.setStatus(_A)
_ChangePhysicalPortServiceDefVoaMode_Type=FspR7VoaMode
_ChangePhysicalPortServiceDefVoaMode_Object=MibTableColumn
changePhysicalPortServiceDefVoaMode=_ChangePhysicalPortServiceDefVoaMode_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,83),_ChangePhysicalPortServiceDefVoaMode_Type())
changePhysicalPortServiceDefVoaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefVoaMode.setStatus(_A)
class _ChangePhysicalPortServiceDefVoaSetpoint_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_ChangePhysicalPortServiceDefVoaSetpoint_Type.__name__=_D
_ChangePhysicalPortServiceDefVoaSetpoint_Object=MibTableColumn
changePhysicalPortServiceDefVoaSetpoint=_ChangePhysicalPortServiceDefVoaSetpoint_Object((1,3,6,1,4,1,2544,1,11,10,7,5,1,1,84),_ChangePhysicalPortServiceDefVoaSetpoint_Type())
changePhysicalPortServiceDefVoaSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceDefVoaSetpoint.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceDefVoaSetpoint.setUnits(_K)
_EndOfChangePhysicalPortServiceDefTable_Type=Integer32
_EndOfChangePhysicalPortServiceDefTable_Object=MibScalar
endOfChangePhysicalPortServiceDefTable=_EndOfChangePhysicalPortServiceDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,5,2),_EndOfChangePhysicalPortServiceDefTable_Type())
endOfChangePhysicalPortServiceDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfChangePhysicalPortServiceDefTable.setStatus(_A)
_EndOfChangeServiceDef_Type=Integer32
_EndOfChangeServiceDef_Object=MibScalar
endOfChangeServiceDef=_EndOfChangeServiceDef_Object((1,3,6,1,4,1,2544,1,11,10,7,5,10000),_EndOfChangeServiceDef_Type())
endOfChangeServiceDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfChangeServiceDef.setStatus(_A)
_ProtectionDef_ObjectIdentity=ObjectIdentity
protectionDef=_ProtectionDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,7,6))
_FfpDefTable_Object=MibTable
ffpDefTable=_FfpDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2))
if mibBuilder.loadTexts:ffpDefTable.setStatus(_A)
_FfpDefEntry_Object=MibTableRow
ffpDefEntry=_FfpDefEntry_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1))
ffpDefEntry.setIndexNames((0,_C,_AN),(0,_C,_AO),(0,_C,_AM),(0,_C,_AL),(0,_C,_AK))
if mibBuilder.loadTexts:ffpDefEntry.setStatus(_A)
_FfpDefRowStatus_Type=RowStatus
_FfpDefRowStatus_Object=MibTableColumn
ffpDefRowStatus=_FfpDefRowStatus_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,1),_FfpDefRowStatus_Type())
ffpDefRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefRowStatus.setStatus(_A)
_FfpDefCreationMethod_Type=FfpType
_FfpDefCreationMethod_Object=MibTableColumn
ffpDefCreationMethod=_FfpDefCreationMethod_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,2),_FfpDefCreationMethod_Type())
ffpDefCreationMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefCreationMethod.setStatus(_A)
_FfpDefSDswitching_Type=EnableState
_FfpDefSDswitching_Object=MibTableColumn
ffpDefSDswitching=_FfpDefSDswitching_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,3),_FfpDefSDswitching_Type())
ffpDefSDswitching.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefSDswitching.setStatus(_A)
_FfpDefHoldOffTime_Type=ApsHoldoffTime
_FfpDefHoldOffTime_Object=MibTableColumn
ffpDefHoldOffTime=_FfpDefHoldOffTime_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,4),_FfpDefHoldOffTime_Type())
ffpDefHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefHoldOffTime.setStatus(_A)
_FfpDefProtectionMech_Type=ProtectionMech
_FfpDefProtectionMech_Object=MibTableColumn
ffpDefProtectionMech=_FfpDefProtectionMech_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,5),_FfpDefProtectionMech_Type())
ffpDefProtectionMech.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefProtectionMech.setStatus(_A)
_FfpDefWorkingAid_Type=SnmpAdminString
_FfpDefWorkingAid_Object=MibTableColumn
ffpDefWorkingAid=_FfpDefWorkingAid_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,6),_FfpDefWorkingAid_Type())
ffpDefWorkingAid.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefWorkingAid.setStatus(_A)
_FfpDefProtectionAid_Type=SnmpAdminString
_FfpDefProtectionAid_Object=MibTableColumn
ffpDefProtectionAid=_FfpDefProtectionAid_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,7),_FfpDefProtectionAid_Type())
ffpDefProtectionAid.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefProtectionAid.setStatus(_A)
_FfpDefSignalDegradeSwitching_Type=EnableState
_FfpDefSignalDegradeSwitching_Object=MibTableColumn
ffpDefSignalDegradeSwitching=_FfpDefSignalDegradeSwitching_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,8),_FfpDefSignalDegradeSwitching_Type())
ffpDefSignalDegradeSwitching.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefSignalDegradeSwitching.setStatus(_A)
_FfpDefSignalFailureSwitching_Type=EnableState
_FfpDefSignalFailureSwitching_Object=MibTableColumn
ffpDefSignalFailureSwitching=_FfpDefSignalFailureSwitching_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,9),_FfpDefSignalFailureSwitching_Type())
ffpDefSignalFailureSwitching.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefSignalFailureSwitching.setStatus(_A)
_FfpDefFarEndIp_Type=IpAddress
_FfpDefFarEndIp_Object=MibTableColumn
ffpDefFarEndIp=_FfpDefFarEndIp_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,10),_FfpDefFarEndIp_Type())
ffpDefFarEndIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefFarEndIp.setStatus(_A)
_FfpDefPeerAid_Type=SnmpAdminString
_FfpDefPeerAid_Object=MibTableColumn
ffpDefPeerAid=_FfpDefPeerAid_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,11),_FfpDefPeerAid_Type())
ffpDefPeerAid.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefPeerAid.setStatus(_A)
_FfpDefApsType_Type=ApsType
_FfpDefApsType_Object=MibTableColumn
ffpDefApsType=_FfpDefApsType_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,12),_FfpDefApsType_Type())
ffpDefApsType.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefApsType.setStatus(_A)
_FfpDefRevertMode_Type=ApsRevertMode
_FfpDefRevertMode_Object=MibTableColumn
ffpDefRevertMode=_FfpDefRevertMode_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,13),_FfpDefRevertMode_Type())
ffpDefRevertMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefRevertMode.setStatus(_A)
class _FfpDefWaitToRestore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,12))
_FfpDefWaitToRestore_Type.__name__=_D
_FfpDefWaitToRestore_Object=MibTableColumn
ffpDefWaitToRestore=_FfpDefWaitToRestore_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,14),_FfpDefWaitToRestore_Type())
ffpDefWaitToRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:ffpDefWaitToRestore.setUnits('min')
_FfpDefDirection_Type=ApsDirection
_FfpDefDirection_Object=MibTableColumn
ffpDefDirection=_FfpDefDirection_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,15),_FfpDefDirection_Type())
ffpDefDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefDirection.setStatus(_A)
_FfpDefProtectionType_Type=FspR7ProtectionType
_FfpDefProtectionType_Object=MibTableColumn
ffpDefProtectionType=_FfpDefProtectionType_Object((1,3,6,1,4,1,2544,1,11,10,7,6,2,1,16),_FfpDefProtectionType_Type())
ffpDefProtectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpDefProtectionType.setStatus(_A)
_EndOfFfpDefTable_Type=Integer32
_EndOfFfpDefTable_Object=MibScalar
endOfFfpDefTable=_EndOfFfpDefTable_Object((1,3,6,1,4,1,2544,1,11,10,7,6,3),_EndOfFfpDefTable_Type())
endOfFfpDefTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFfpDefTable.setStatus(_A)
_EndOfProtectionDef_Type=Integer32
_EndOfProtectionDef_Object=MibScalar
endOfProtectionDef=_EndOfProtectionDef_Object((1,3,6,1,4,1,2544,1,11,10,7,6,10000),_EndOfProtectionDef_Type())
endOfProtectionDef.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfProtectionDef.setStatus(_A)
_ConformanceDef_ObjectIdentity=ObjectIdentity
conformanceDef=_ConformanceDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,10))
_CompliancesDef_ObjectIdentity=ObjectIdentity
compliancesDef=_CompliancesDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,10,1))
_GroupsDef_ObjectIdentity=ObjectIdentity
groupsDef=_GroupsDef_ObjectIdentity((1,3,6,1,4,1,2544,1,11,10,10,2))
objectGroupDef=ObjectGroup((1,3,6,1,4,1,2544,1,11,10,10,2,1))
objectGroupDef.setObjects(*((_F,_Ab),(_F,_Ac),(_F,_Ad),(_F,_Ae),(_F,_Af),(_F,_Ag),(_F,_Ah),(_F,_Ai),(_F,_Aj),(_F,_Ak),(_F,_Al),(_F,_Am),(_F,_An),(_F,_Ao),(_F,_Ap),(_F,_Aq),(_F,_Ar),(_F,_As),(_F,_At),(_F,_Au),(_F,_Av),(_F,_Aw),(_F,_Ax),(_F,_Ay),(_F,_Az),(_F,_A_),(_F,_B0),(_F,_B1),(_F,_B2),(_F,_B3),(_F,_B4),(_F,_B5),(_F,_B6),(_F,_B7),(_F,_B8),(_F,_B9),(_F,_BA),(_F,_BB),(_F,_BC),(_F,_BD),(_F,_BE),(_F,_BF),(_F,_BG),(_F,_BH),(_F,_BI),(_F,_BJ),(_F,_BK)))
if mibBuilder.loadTexts:objectGroupDef.setStatus(_A)
complianceDef=ModuleCompliance((1,3,6,1,4,1,2544,1,11,10,10,1,1))
complianceDef.setObjects((_F,_BL))
if mibBuilder.loadTexts:complianceDef.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'advaFspR7Def':advaFspR7Def,'managementDef':managementDef,'specificMgmtDef':specificMgmtDef,'crossConnectionDefTable':crossConnectionDefTable,'crossConnectionDefEntry':crossConnectionDefEntry,_Ab:crossConnectionDefRowStatus,_Ac:crossConnectionDefAdmin,_Ad:crossConnectionDefRedLineState,_Ae:crossConnectionDefConn,_Af:crossConnectionDefAlias,_Ag:crossConnectionDefPathNode,_Ah:crossConnectionDefTunnelAid,_Ao:crossConnectionDefType,'crossConnectionDefCrsFunction':crossConnectionDefCrsFunction,'crossOpticalLineDefTable':crossOpticalLineDefTable,'crossOpticalLineDefEntry':crossOpticalLineDefEntry,_Ai:crossOpticalLineDefRowStatus,_Aj:crossOpticalLineDefRedLineState,_Ak:crossOpticalLineDefConn,_Al:crossOpticalLineDefCrsType,_Am:crossOpticalLineDefAlias,_An:crossOpticalLineDefTunnelAid,'endOfCrossOpticalLineDefTable':endOfCrossOpticalLineDefTable,'crossDcnDefTable':crossDcnDefTable,'crossDcnDefEntry':crossDcnDefEntry,'crossDcnDefRowStatus':crossDcnDefRowStatus,'crossDcnDefType':crossDcnDefType,'crossDcnDefLink':crossDcnDefLink,'crossDcnDefEcc':crossDcnDefEcc,'endOfCrossDcnDefTable':endOfCrossDcnDefTable,'endOfSpecificMgmtDef':endOfSpecificMgmtDef,'eqptMgmtDef':eqptMgmtDef,'shelfDefTable':shelfDefTable,'shelfDefEntry':shelfDefEntry,'shelfDefRowStatus':shelfDefRowStatus,'shelfDefPsuOutputPower':shelfDefPsuOutputPower,'shelfDefType':shelfDefType,'shelfDefRack':shelfDefRack,'shelfDefSupply':shelfDefSupply,'shelfDefBandProvision':shelfDefBandProvision,'shelfDefAdmin':shelfDefAdmin,'shelfDefRackNumber':shelfDefRackNumber,'shelfDefRackOrder':shelfDefRackOrder,'shelfDefAlias':shelfDefAlias,'shelfDefSlot':shelfDefSlot,'endOfShelfDefTable':endOfShelfDefTable,'fanDefTable':fanDefTable,'fanDefEntry':fanDefEntry,'fanDefRowStatus':fanDefRowStatus,'fanDefAdmin':fanDefAdmin,'fanDefType':fanDefType,'fanDefAlias':fanDefAlias,'fanDefOutputReset':fanDefOutputReset,'endOfFanDefTable':endOfFanDefTable,'plugDefTable':plugDefTable,'plugDefEntry':plugDefEntry,'plugDefRowStatus':plugDefRowStatus,'plugDefConnector':plugDefConnector,'plugDefType':plugDefType,'plugDefReach':plugDefReach,'plugDefLoopbackAttenuation':plugDefLoopbackAttenuation,'plugDefTransmitChannel':plugDefTransmitChannel,'plugDefAlias':plugDefAlias,'plugDefLaneGroup':plugDefLaneGroup,'plugDefMaxDataRate':plugDefMaxDataRate,'plugDefThirdPartyUsage':plugDefThirdPartyUsage,'plugDefAdmin':plugDefAdmin,'plugDefBidirectionalChannel':plugDefBidirectionalChannel,'plugDefChannelSpacingProvision':plugDefChannelSpacingProvision,'endOfPlugDefTable':endOfPlugDefTable,'moduleDefTable':moduleDefTable,'moduleDefEntry':moduleDefEntry,'moduleDefRowStatus':moduleDefRowStatus,'moduleDefPsuOutputPower':moduleDefPsuOutputPower,'moduleDefPower':moduleDefPower,'moduleDefReach':moduleDefReach,'moduleDefInitEqlz':moduleDefInitEqlz,'moduleDefLanAid':moduleDefLanAid,'moduleDefType':moduleDefType,'moduleDefMapping':moduleDefMapping,'moduleDefGainRange':moduleDefGainRange,'moduleDefSfProvision':moduleDefSfProvision,'moduleDefCapabilityLevelProvision':moduleDefCapabilityLevelProvision,'moduleDefDCFiberType':moduleDefDCFiberType,'moduleDefChannelsProvision':moduleDefChannelsProvision,'moduleDefFiberDetect':moduleDefFiberDetect,'moduleDefSupply':moduleDefSupply,'moduleDefGroup':moduleDefGroup,'moduleDefDeploy':moduleDefDeploy,'moduleDefLagSysPrio':moduleDefLagSysPrio,'moduleDefTransmitChannel':moduleDefTransmitChannel,'moduleDefBand':moduleDefBand,'moduleDefTrafficDirection':moduleDefTrafficDirection,'moduleDefIpAddr':moduleDefIpAddr,'moduleDefDispersionCompensation':moduleDefDispersionCompensation,'moduleDefActivateDetect':moduleDefActivateDetect,'moduleDefOscUsage':moduleDefOscUsage,'moduleDefAdmin':moduleDefAdmin,'moduleDefScrambling':moduleDefScrambling,'moduleDefChannelsNumber':moduleDefChannelsNumber,'moduleDefChannelSpacingProvision':moduleDefChannelSpacingProvision,'moduleDefMode':moduleDefMode,'moduleDefSubBandProvision':moduleDefSubBandProvision,'moduleDefAlias':moduleDefAlias,'moduleDefFiberType':moduleDefFiberType,'moduleDefChannelSpacing':moduleDefChannelSpacing,'moduleDefOutputReset':moduleDefOutputReset,'moduleDefRoadmNumber':moduleDefRoadmNumber,'moduleDefTopology':moduleDefTopology,'moduleDefForceConfig':moduleDefForceConfig,'moduleDefMuxMethod':moduleDefMuxMethod,'moduleDefNdpCleanup':moduleDefNdpCleanup,'moduleDefRstp':moduleDefRstp,'moduleDefRemoteReset':moduleDefRemoteReset,'endOfModuleDefTable':endOfModuleDefTable,'endOfEqptMgmtDef':endOfEqptMgmtDef,'facilityMgmtDef':facilityMgmtDef,'physicalPortDefTable':physicalPortDefTable,'physicalPortDefEntry':physicalPortDefEntry,_Ap:physicalPortDefRowStatus,_Aq:physicalPortDefType,_Ar:physicalPortDefAdmin,'physicalPortDefAlias':physicalPortDefAlias,'physicalPortDefAlsMode':physicalPortDefAlsMode,'physicalPortDefAutoThresReset':physicalPortDefAutoThresReset,'physicalPortDefAutonegotiation':physicalPortDefAutonegotiation,'physicalPortDefBehaviour':physicalPortDefBehaviour,'physicalPortDefDispertionConfig':physicalPortDefDispertionConfig,'physicalPortDefDispersionSetting':physicalPortDefDispersionSetting,'physicalPortDefDispersionMode':physicalPortDefDispersionMode,'physicalPortDefChannelProv':physicalPortDefChannelProv,'physicalPortDefWdmRxChannel':physicalPortDefWdmRxChannel,'physicalPortDefCodeGain':physicalPortDefCodeGain,'physicalPortDefXfpDecisionThres':physicalPortDefXfpDecisionThres,'physicalPortDefDisparityCorrection':physicalPortDefDisparityCorrection,'physicalPortDefEqlzAdmin':physicalPortDefEqlzAdmin,'physicalPortDefErrorForwarding':physicalPortDefErrorForwarding,'physicalPortDefFecType':physicalPortDefFecType,'physicalPortDefFarEndCommunication':physicalPortDefFarEndCommunication,'physicalPortDefFlowControl':physicalPortDefFlowControl,'physicalPortDefForceLaserOn':physicalPortDefForceLaserOn,'physicalPortDefInhibitSwitchToProt':physicalPortDefInhibitSwitchToProt,'physicalPortDefInhibitSwitchToWork':physicalPortDefInhibitSwitchToWork,'physicalPortDefLaneChannelSetting':physicalPortDefLaneChannelSetting,'physicalPortDefLoopConfig':physicalPortDefLoopConfig,'physicalPortDefLaserDelayTimer':physicalPortDefLaserDelayTimer,'physicalPortDefLaserOffTimer':physicalPortDefLaserOffTimer,'physicalPortDefLaserOnTimer':physicalPortDefLaserOnTimer,'physicalPortDefLaserOffDelayFunction':physicalPortDefLaserOffDelayFunction,'physicalPortDefAutoPTassignment':physicalPortDefAutoPTassignment,'physicalPortDefTributarySlotMethod':physicalPortDefTributarySlotMethod,'physicalPortDefInitiateEqualization':physicalPortDefInitiateEqualization,'physicalPortDefLossAttenuation':physicalPortDefLossAttenuation,'physicalPortDefOpticalSetPoint':physicalPortDefOpticalSetPoint,'physicalPortDefDataLayerPmReset':physicalPortDefDataLayerPmReset,'physicalPortDefPrbsPmReset':physicalPortDefPrbsPmReset,'physicalPortDefTestPrbsRcvMode':physicalPortDefTestPrbsRcvMode,'physicalPortDefTestPrbsTrmtMode':physicalPortDefTestPrbsTrmtMode,'physicalPortDefSwitchCommand':physicalPortDefSwitchCommand,'physicalPortDefOpuPayloadType':physicalPortDefOpuPayloadType,'physicalPortDefSigDegThresSonetLine':physicalPortDefSigDegThresSonetLine,'physicalPortDefSigDegThresSdhMs':physicalPortDefSigDegThresSdhMs,'physicalPortDefSigDegThresOtu':physicalPortDefSigDegThresOtu,'physicalPortDefSigDegThresOdu':physicalPortDefSigDegThresOdu,'physicalPortDefSigDegThreshold':physicalPortDefSigDegThreshold,'physicalPortDefSigDegPcslThreshold':physicalPortDefSigDegPcslThreshold,'physicalPortDefSigDegThresSonetSection':physicalPortDefSigDegThresSonetSection,'physicalPortDefSigDegThresSdhSection':physicalPortDefSigDegThresSdhSection,'physicalPortDefSigDegThresOduTcmA':physicalPortDefSigDegThresOduTcmA,'physicalPortDefSigDegThresOduTcmB':physicalPortDefSigDegThresOduTcmB,'physicalPortDefSigDegThresOduTcmC':physicalPortDefSigDegThresOduTcmC,'physicalPortDefSignalDegradePeriod':physicalPortDefSignalDegradePeriod,'physicalPortDefSigDegPeriodOdu':physicalPortDefSigDegPeriodOdu,'physicalPortDefSigDegPeriodOtu':physicalPortDefSigDegPeriodOtu,'physicalPortDefSigDegPeriodIntegration':physicalPortDefSigDegPeriodIntegration,'physicalPortDefSigDegPeriodSdhSection':physicalPortDefSigDegPeriodSdhSection,'physicalPortDefSigDegPeriodOduTcmA':physicalPortDefSigDegPeriodOduTcmA,'physicalPortDefSigDegPeriodOduTcmB':physicalPortDefSigDegPeriodOduTcmB,'physicalPortDefSigDegPeriodOduTcmC':physicalPortDefSigDegPeriodOduTcmC,'physicalPortDefOtnStuffing':physicalPortDefOtnStuffing,'physicalPortDefTcmALevel':physicalPortDefTcmALevel,'physicalPortDefTcmBLevel':physicalPortDefTcmBLevel,'physicalPortDefTcmCLevel':physicalPortDefTcmCLevel,'physicalPortDefTerminationLevel':physicalPortDefTerminationLevel,'physicalPortDefTimingSource':physicalPortDefTimingSource,'physicalPortDefTimModeOdu':physicalPortDefTimModeOdu,'physicalPortDefTimModeOtu':physicalPortDefTimModeOtu,'physicalPortDefTimModeSonetSection':physicalPortDefTimModeSonetSection,'physicalPortDefTimModeOduTcmA':physicalPortDefTimModeOduTcmA,'physicalPortDefTimModeOduTcmB':physicalPortDefTimModeOduTcmB,'physicalPortDefTimModeOduTcmC':physicalPortDefTimModeOduTcmC,'physicalPortDefTraceFormSonetSection':physicalPortDefTraceFormSonetSection,'physicalPortDefTraceExpectedSonetSection':physicalPortDefTraceExpectedSonetSection,'physicalPortDefTraceTransmitSonetSection':physicalPortDefTraceTransmitSonetSection,'physicalPortDefTraceExpectedOtu':physicalPortDefTraceExpectedOtu,'physicalPortDefTraceTransmitSapiOtu':physicalPortDefTraceTransmitSapiOtu,'physicalPortDefTraceTransmitDapiOtu':physicalPortDefTraceTransmitDapiOtu,'physicalPortDefTraceTransmitOpspOtu':physicalPortDefTraceTransmitOpspOtu,'physicalPortDefTraceExpectedOdu':physicalPortDefTraceExpectedOdu,'physicalPortDefTraceTransmitSapiOdu':physicalPortDefTraceTransmitSapiOdu,'physicalPortDefTraceTransmitDapiOdu':physicalPortDefTraceTransmitDapiOdu,'physicalPortDefTraceTransmitOpspOdu':physicalPortDefTraceTransmitOpspOdu,'physicalPortDefTraceExpectedOduTcmA':physicalPortDefTraceExpectedOduTcmA,'physicalPortDefTraceTransmitSapiOduTcmA':physicalPortDefTraceTransmitSapiOduTcmA,'physicalPortDefTraceTransmitDapiOduTcmA':physicalPortDefTraceTransmitDapiOduTcmA,'physicalPortDefTraceTransmitOpspOduTcmA':physicalPortDefTraceTransmitOpspOduTcmA,'physicalPortDefTraceExpectedOduTcmB':physicalPortDefTraceExpectedOduTcmB,'physicalPortDefTraceTransmitSapiOduTcmB':physicalPortDefTraceTransmitSapiOduTcmB,'physicalPortDefTraceTransmitDapiOduTcmB':physicalPortDefTraceTransmitDapiOduTcmB,'physicalPortDefTraceTransmitOpspOduTcmB':physicalPortDefTraceTransmitOpspOduTcmB,'physicalPortDefTraceExpectedOduTcmC':physicalPortDefTraceExpectedOduTcmC,'physicalPortDefTraceTransmitSapiOduTcmC':physicalPortDefTraceTransmitSapiOduTcmC,'physicalPortDefTraceTransmitDapiOduTcmC':physicalPortDefTraceTransmitDapiOduTcmC,'physicalPortDefTraceTransmitOpspOduTcmC':physicalPortDefTraceTransmitOpspOduTcmC,'physicalPortDefTurnupConfig':physicalPortDefTurnupConfig,'physicalPortDefTxOffDelay':physicalPortDefTxOffDelay,'physicalPortDefVoaMode':physicalPortDefVoaMode,'physicalPortDefVoaSetpoint':physicalPortDefVoaSetpoint,'physicalPortDefLagPrio':physicalPortDefLagPrio,'physicalPortDefMaxFrameSize':physicalPortDefMaxFrameSize,'physicalPortDefPayload':physicalPortDefPayload,'physicalPortDefPortMode':physicalPortDefPortMode,'physicalPortDefPortRole':physicalPortDefPortRole,'physicalPortDefPriority':physicalPortDefPriority,'physicalPortDefPvid':physicalPortDefPvid,'physicalPortDefStagType':physicalPortDefStagType,'physicalPortDefUtag':physicalPortDefUtag,'physicalPortDefVethAid':physicalPortDefVethAid,'physicalPortDefRedLineState':physicalPortDefRedLineState,'physicalPortDefTunnelAid':physicalPortDefTunnelAid,'physicalPortDefRateLimit':physicalPortDefRateLimit,'physicalPortDefTxOffOnTm':physicalPortDefTxOffOnTm,'physicalPortDefTxOffTimer':physicalPortDefTxOffTimer,'physicalPortDefTxOnTimer':physicalPortDefTxOnTimer,'virtualPortDefTable':virtualPortDefTable,'virtualPortDefEntry':virtualPortDefEntry,_As:virtualPortDefRowStatus,_At:virtualPortDefChannelBand,_Au:virtualPortDefType,_Av:virtualPortDefAlias,_Aw:virtualPortDefAdmin,_Ax:virtualPortDefEqlzAdmin,'virtualPortDefInitEqlz':virtualPortDefInitEqlz,'virtualPortDefLacpMode':virtualPortDefLacpMode,'virtualPortDefLacpTimeout':virtualPortDefLacpTimeout,'virtualPortDefLagActivePorts':virtualPortDefLagActivePorts,'virtualPortDefMaxFrameSize':virtualPortDefMaxFrameSize,'virtualPortDefPortMode':virtualPortDefPortMode,'virtualPortDefDataLayerPmReset':virtualPortDefDataLayerPmReset,'virtualPortDefPortRole':virtualPortDefPortRole,'virtualPortDefLagPortType':virtualPortDefLagPortType,'virtualPortDefPriority':virtualPortDefPriority,'virtualPortDefPvid':virtualPortDefPvid,'virtualPortDefRevertiveMode':virtualPortDefRevertiveMode,'virtualPortDefStagType':virtualPortDefStagType,'virtualPortDefUtag':virtualPortDefUtag,'virtualPortDefBundle':virtualPortDefBundle,'virtualPortDefSwitchCommand':virtualPortDefSwitchCommand,'virtualPortDefInhibitSwitchToWork':virtualPortDefInhibitSwitchToWork,'virtualPortDefInhibitSwitchToProt':virtualPortDefInhibitSwitchToProt,'virtualPortDefOduTribPortNo':virtualPortDefOduTribPortNo,'virtualPortDefOduTribTimeSlottNo':virtualPortDefOduTribTimeSlottNo,'virtualPortDefSigDegThresOdu':virtualPortDefSigDegThresOdu,'virtualPortDefSigDegPeriodOdu':virtualPortDefSigDegPeriodOdu,'virtualPortDefTraceExpectedOdu':virtualPortDefTraceExpectedOdu,'virtualPortDefTraceTransmitSapiOdu':virtualPortDefTraceTransmitSapiOdu,'virtualPortDefTraceTransmitDapiOdu':virtualPortDefTraceTransmitDapiOdu,'virtualPortDefTraceTransmitOpspOdu':virtualPortDefTraceTransmitOpspOdu,'virtualPortDefTimModeOdu':virtualPortDefTimModeOdu,'virtualPortDefSigDegThresOduTcmA':virtualPortDefSigDegThresOduTcmA,'virtualPortDefSigDegPeriodOduTcmA':virtualPortDefSigDegPeriodOduTcmA,'virtualPortDefSigDegThresOduTcmB':virtualPortDefSigDegThresOduTcmB,'virtualPortDefSigDegPeriodOduTcmB':virtualPortDefSigDegPeriodOduTcmB,'virtualPortDefSigDegThresOduTcmC':virtualPortDefSigDegThresOduTcmC,'virtualPortDefSigDegPeriodOduTcmC':virtualPortDefSigDegPeriodOduTcmC,'virtualPortDefTcmALevel':virtualPortDefTcmALevel,'virtualPortDefTcmBLevel':virtualPortDefTcmBLevel,'virtualPortDefTcmCLevel':virtualPortDefTcmCLevel,'virtualPortDefTraceTransmitSapiOduTcmA':virtualPortDefTraceTransmitSapiOduTcmA,'virtualPortDefTraceTransmitDapiOduTcmA':virtualPortDefTraceTransmitDapiOduTcmA,'virtualPortDefTraceTransmitOpspOduTcmA':virtualPortDefTraceTransmitOpspOduTcmA,'virtualPortDefTraceExpectedOduTcmA':virtualPortDefTraceExpectedOduTcmA,'virtualPortDefTimModeOduTcmA':virtualPortDefTimModeOduTcmA,'virtualPortDefTraceExpectedOduTcmB':virtualPortDefTraceExpectedOduTcmB,'virtualPortDefTraceTransmitSapiOduTcmB':virtualPortDefTraceTransmitSapiOduTcmB,'virtualPortDefTraceTransmitDapiOduTcmB':virtualPortDefTraceTransmitDapiOduTcmB,'virtualPortDefTraceTransmitOpspOduTcmB':virtualPortDefTraceTransmitOpspOduTcmB,'virtualPortDefTimModeOduTcmB':virtualPortDefTimModeOduTcmB,'virtualPortDefTraceExpectedOduTcmC':virtualPortDefTraceExpectedOduTcmC,'virtualPortDefTraceTransmitSapiOduTcmC':virtualPortDefTraceTransmitSapiOduTcmC,'virtualPortDefTraceTransmitDapiOduTcmC':virtualPortDefTraceTransmitDapiOduTcmC,'virtualPortDefTraceTransmitOpspOduTcmC':virtualPortDefTraceTransmitOpspOduTcmC,'virtualPortDefTimModeOduTcmC':virtualPortDefTimModeOduTcmC,'virtualPortDefTerminationLevel':virtualPortDefTerminationLevel,'virtualPortDefLoopConfig':virtualPortDefLoopConfig,'virtualPortDefVcType':virtualPortDefVcType,'virtualPortDefCir':virtualPortDefCir,'virtualPortDefOpuPayloadType':virtualPortDefOpuPayloadType,'virtualPortDefOtnStuffing':virtualPortDefOtnStuffing,'virtualPortDefRedLineState':virtualPortDefRedLineState,'virtualPortDefTunnelAid':virtualPortDefTunnelAid,'endOfVirtualPortDefTable':endOfVirtualPortDefTable,'endOfFacilityMgmtDef':endOfFacilityMgmtDef,'dcnMgmtDef':dcnMgmtDef,'linkDefTable':linkDefTable,'linkDefEntry':linkDefEntry,'linkDefRowStatus':linkDefRowStatus,'linkDefType':linkDefType,'linkDefAdmin':linkDefAdmin,'linkDefAlias':linkDefAlias,'linkDefAuthString':linkDefAuthString,'linkDefProxyArp':linkDefProxyArp,'linkDefOspf':linkDefOspf,'linkDefBaud':linkDefBaud,'linkDefAuthType':linkDefAuthType,'linkDefIpType':linkDefIpType,'linkDefMetric':linkDefMetric,'linkDefAreaAid':linkDefAreaAid,'linkDefNearEndIp':linkDefNearEndIp,'linkDefBitrate':linkDefBitrate,'linkDefIPv6Type':linkDefIPv6Type,'linkDefNendIPv6':linkDefNendIPv6,'endOfLinkDefTable':endOfLinkDefTable,'scDefTable':scDefTable,'scDefEntry':scDefEntry,'scDefRowStatus':scDefRowStatus,'scDefType':scDefType,'scDefAdmin':scDefAdmin,'scDefAlias':scDefAlias,'scDefAuthString':scDefAuthString,'scDefOspf':scDefOspf,'scDefAuthType':scDefAuthType,'scDefIpType':scDefIpType,'scDefMetric':scDefMetric,'scDefAreaAid':scDefAreaAid,'scDefAlsMode':scDefAlsMode,'scDefSigDegThresReceiver':scDefSigDegThresReceiver,'scDefAutonegotiation':scDefAutonegotiation,'scDefBitrate':scDefBitrate,'scDefDuplex':scDefDuplex,'scDefAttGradientTh':scDefAttGradientTh,'scDefIpAddr':scDefIpAddr,'scDefLanAid':scDefLanAid,'scDefIpMask':scDefIpMask,'scDefDataLayerPmReset':scDefDataLayerPmReset,'scDefPriority':scDefPriority,'scDefIPv6':scDefIPv6,'scDefIPv6PrefixLen':scDefIPv6PrefixLen,'scDefIpMode':scDefIpMode,'scDefGatewayProxyArp':scDefGatewayProxyArp,'endOfScDefTable':endOfScDefTable,'lanDefTable':lanDefTable,'lanDefEntry':lanDefEntry,'lanDefRowStatus':lanDefRowStatus,'lanDefType':lanDefType,'lanDefAdmin':lanDefAdmin,'lanDefAlias':lanDefAlias,'lanDefAuthString':lanDefAuthString,'lanDefOspf':lanDefOspf,'lanDefAuthType':lanDefAuthType,'lanDefIpType':lanDefIpType,'lanDefMetric':lanDefMetric,'lanDefAreaAid':lanDefAreaAid,'lanDefIpAddr':lanDefIpAddr,'lanDefIpMask':lanDefIpMask,'lanDefPriority':lanDefPriority,'lanDefIPv6':lanDefIPv6,'lanDefIPv6PrefixLen':lanDefIPv6PrefixLen,'lanDefIpMode':lanDefIpMode,'endOfLanDefTable':endOfLanDefTable,'eccDefTable':eccDefTable,'eccDefEntry':eccDefEntry,'eccDefRowStatus':eccDefRowStatus,'eccDefType':eccDefType,'eccDefAdmin':eccDefAdmin,'eccDefAlias':eccDefAlias,'eccDefLanAid':eccDefLanAid,'eccDefExternalVid':eccDefExternalVid,'endOfEccDefTable':endOfEccDefTable,'endOfDcnMgmtDef':endOfDcnMgmtDef,'opticalMuxMgmtDef':opticalMuxMgmtDef,'opticalMuxDefTable':opticalMuxDefTable,'opticalMuxDefEntry':opticalMuxDefEntry,'opticalMuxDefRowStatus':opticalMuxDefRowStatus,'opticalMuxDefPumpPower':opticalMuxDefPumpPower,'opticalMuxDefInhibitSwitchToWork':opticalMuxDefInhibitSwitchToWork,'opticalMuxDefForceLaserOn':opticalMuxDefForceLaserOn,'opticalMuxDefAseTabCreation':opticalMuxDefAseTabCreation,'opticalMuxDefOpticalSetPoint':opticalMuxDefOpticalSetPoint,'opticalMuxDefInitiateEqualization':opticalMuxDefInitiateEqualization,'opticalMuxDefTilt':opticalMuxDefTilt,'opticalMuxDefOscOpticalSetpoint':opticalMuxDefOscOpticalSetpoint,'opticalMuxDefOffset':opticalMuxDefOffset,'opticalMuxDefSwitchCommand':opticalMuxDefSwitchCommand,'opticalMuxDefAlsMode':opticalMuxDefAlsMode,'opticalMuxDefType':opticalMuxDefType,'opticalMuxDefAttenuationGradient':opticalMuxDefAttenuationGradient,'opticalMuxDefInhibitSwitchToProt':opticalMuxDefInhibitSwitchToProt,'opticalMuxDefVariableGain':opticalMuxDefVariableGain,'opticalMuxDefAdmin':opticalMuxDefAdmin,'opticalMuxDefTimePeriod':opticalMuxDefTimePeriod,'opticalMuxDefSigDegThresReceiver':opticalMuxDefSigDegThresReceiver,'opticalMuxDefAlias':opticalMuxDefAlias,'opticalMuxDefDataLayerPmReset':opticalMuxDefDataLayerPmReset,'opticalMuxDefGain':opticalMuxDefGain,'opticalMuxDefEdfaPwrOut':opticalMuxDefEdfaPwrOut,'opticalMuxDefVoaSetpoint':opticalMuxDefVoaSetpoint,'opticalMuxDefFiberBrand':opticalMuxDefFiberBrand,'opticalMuxDefTiltSet':opticalMuxDefTiltSet,'opticalMuxDefForceFwdAsePilotOn':opticalMuxDefForceFwdAsePilotOn,'opticalMuxDefBandProvision':opticalMuxDefBandProvision,'opticalMuxDefOffsetHigh':opticalMuxDefOffsetHigh,'opticalMuxDefOffsetLow':opticalMuxDefOffsetLow,'opticalMuxDefOptUpdate':opticalMuxDefOptUpdate,'endOfOpticalMuxDefTable':endOfOpticalMuxDefTable,'endOfOpticalMuxMgmtDef':endOfOpticalMuxMgmtDef,'shelfConnMgmtDef':shelfConnMgmtDef,'shelfConnDefTable':shelfConnDefTable,'shelfConnDefEntry':shelfConnDefEntry,'shelfConnDefRowStatus':shelfConnDefRowStatus,'shelfConnDefAdmin':shelfConnDefAdmin,'shelfConnDefAlias':shelfConnDefAlias,'shelfConnDefFacilityType':shelfConnDefFacilityType,'endOfShelfConnDefTable':endOfShelfConnDefTable,'endOfShelfConnMgmtDef':endOfShelfConnMgmtDef,'envMgmtDef':envMgmtDef,'envPortDefTable':envPortDefTable,'envPortDefEntry':envPortDefEntry,'envPortDefRowStatus':envPortDefRowStatus,'envPortDefTelemetry':envPortDefTelemetry,'envPortDefFacilityType':envPortDefFacilityType,'envPortDefTifAlarmType':envPortDefTifAlarmType,'envPortDefTifAlarmMessage':envPortDefTifAlarmMessage,'envPortDefInvertTifInputLogic':envPortDefInvertTifInputLogic,'endOfEnvPortDefTable':endOfEnvPortDefTable,'endOfEnvMgmtDef':endOfEnvMgmtDef,'containerMgmtDef':containerMgmtDef,'containerDefTable':containerDefTable,'containerDefEntry':containerDefEntry,'containerDefRowStatus':containerDefRowStatus,'containerDefFacilityType':containerDefFacilityType,'endOfContainerDefTable':endOfContainerDefTable,'endOfContainerMgmtDef':endOfContainerMgmtDef,'opticalLineMgmtDef':opticalLineMgmtDef,'opticalLineDefTable':opticalLineDefTable,'opticalLineDefEntry':opticalLineDefEntry,'opticalLineDefRowStatus':opticalLineDefRowStatus,'opticalLineDefTxLineAttenuation':opticalLineDefTxLineAttenuation,'opticalLineDefRxLineAttenuation':opticalLineDefRxLineAttenuation,'opticalLineDefAlias':opticalLineDefAlias,'opticalLineDefFarEndLocation':opticalLineDefFarEndLocation,'endOfOpticalLineDefTable':endOfOpticalLineDefTable,'endOfOpticalLineMgmtDef':endOfOpticalLineMgmtDef,'performanceDef':performanceDef,'performanceFacilityDef':performanceFacilityDef,'performanceFacilityThresholdDef':performanceFacilityThresholdDef,'optThresholdConfigDefTable':optThresholdConfigDefTable,'optThresholdConfigDefEntry':optThresholdConfigDefEntry,'optThresholdConfigDefLowConfig':optThresholdConfigDefLowConfig,'optThresholdConfigDefHighConfig':optThresholdConfigDefHighConfig,'oprThresholdConfigDefTable':oprThresholdConfigDefTable,'oprThresholdConfigDefEntry':oprThresholdConfigDefEntry,'oprThresholdConfigDefLowConfig':oprThresholdConfigDefLowConfig,'oprThresholdConfigDefHighConfig':oprThresholdConfigDefHighConfig,'endOfOprThresholdConfigDefTable':endOfOprThresholdConfigDefTable,'endOfPerformanceFacilityThresholdDef':endOfPerformanceFacilityThresholdDef,'featureSpecificDef':featureSpecificDef,'fiberMapDef':fiberMapDef,'terminationPointDefTable':terminationPointDefTable,'terminationPointDefEntry':terminationPointDefEntry,'terminationPointDefRowStatus':terminationPointDefRowStatus,'terminationPointDefAdmin':terminationPointDefAdmin,'terminationPointDefFiberDetect':terminationPointDefFiberDetect,'terminationPointDefAlias':terminationPointDefAlias,'connectionDefTable':connectionDefTable,'connectionDefEntry':connectionDefEntry,_Ay:connectionDefRowStatus,_Az:connectionDefType,'endOfConnectionDefTable':endOfConnectionDefTable,'endOfFiberMapDef':endOfFiberMapDef,'eciDef':eciDef,'externalPortDefTable':externalPortDefTable,'externalPortDefEntry':externalPortDefEntry,_A_:externalPortDefRowStatus,_B0:externalPortDefType,_B1:externalPortDefTransmitChannel,_B2:externalPortDefChannelBandwith,_B3:externalPortDefAlias,_B4:externalPortDefFarEndLocation,_B5:externalPortDefBitrate,_B8:externalPortDefFecType,_B9:externalPortDefLineCoding,_BA:externalPortDefFrameFormat,_BB:externalPortDefOpticalPowerTx,_BC:externalPortDefOsnrTransmit,_BD:externalPortDefPmdTransmit,_BE:externalPortDefChromDisperTx,_BF:externalPortDefMinOsnrRcv,_BG:externalPortDefMinOptPowerRcv,_BH:externalPortDefMaxOptPowerRcv,_BI:externalPortDefMaxPmdRcv,_BJ:externalPortDefMinChromDisperRcv,_B6:externalPortDefMaxChromDisperRcv,_B7:externalPortDefMaxBitErrorRate,_BK:externalPortDefSourceProfile,'endOfExternalPortDefTable':endOfExternalPortDefTable,'endOfEciDef':endOfEciDef,'changeServiceDef':changeServiceDef,'changePhysicalPortServiceDefTable':changePhysicalPortServiceDefTable,'changePhysicalPortServiceDefEntry':changePhysicalPortServiceDefEntry,'changePhysicalPortServiceDefRowStatus':changePhysicalPortServiceDefRowStatus,'changePhysicalPortServiceDefType':changePhysicalPortServiceDefType,'changePhysicalPortServiceDefAdmin':changePhysicalPortServiceDefAdmin,'changePhysicalPortServiceDefAlias':changePhysicalPortServiceDefAlias,'changePhysicalPortServiceDefAlsMode':changePhysicalPortServiceDefAlsMode,'changePhysicalPortServiceDefBehaviour':changePhysicalPortServiceDefBehaviour,'changePhysicalPortServiceDefDispersionSetting':changePhysicalPortServiceDefDispersionSetting,'changePhysicalPortServiceDefDispersionMode':changePhysicalPortServiceDefDispersionMode,'changePhysicalPortServiceDefChannelProv':changePhysicalPortServiceDefChannelProv,'changePhysicalPortServiceDefWdmRxChannel':changePhysicalPortServiceDefWdmRxChannel,'changePhysicalPortServiceDefCodeGain':changePhysicalPortServiceDefCodeGain,'changePhysicalPortServiceDefXfpDecisionThres':changePhysicalPortServiceDefXfpDecisionThres,'changePhysicalPortServiceDefDisparityCorrection':changePhysicalPortServiceDefDisparityCorrection,'changePhysicalPortServiceDefEqlzAdmin':changePhysicalPortServiceDefEqlzAdmin,'changePhysicalPortServiceDefErrorForwarding':changePhysicalPortServiceDefErrorForwarding,'changePhysicalPortServiceDefFecType':changePhysicalPortServiceDefFecType,'changePhysicalPortServiceDefFarEndCommunication':changePhysicalPortServiceDefFarEndCommunication,'changePhysicalPortServiceDefFlowControl':changePhysicalPortServiceDefFlowControl,'changePhysicalPortServiceDefLaneChannelSetting':changePhysicalPortServiceDefLaneChannelSetting,'changePhysicalPortServiceDefLaserDelayTimer':changePhysicalPortServiceDefLaserDelayTimer,'changePhysicalPortServiceDefLaserOffTimer':changePhysicalPortServiceDefLaserOffTimer,'changePhysicalPortServiceDefLaserOnTimer':changePhysicalPortServiceDefLaserOnTimer,'changePhysicalPortServiceDefLaserOffDelayFunction':changePhysicalPortServiceDefLaserOffDelayFunction,'changePhysicalPortServiceDefAutoPTassignment':changePhysicalPortServiceDefAutoPTassignment,'changePhysicalPortServiceDefTributarySlotMethod':changePhysicalPortServiceDefTributarySlotMethod,'changePhysicalPortServiceDefOpticalSetPoint':changePhysicalPortServiceDefOpticalSetPoint,'changePhysicalPortServiceDefOpuPayloadType':changePhysicalPortServiceDefOpuPayloadType,'changePhysicalPortServiceDefSigDegThresSonetLine':changePhysicalPortServiceDefSigDegThresSonetLine,'changePhysicalPortServiceDefSigDegThresSdhMs':changePhysicalPortServiceDefSigDegThresSdhMs,'changePhysicalPortServiceDefSigDegThresOtu':changePhysicalPortServiceDefSigDegThresOtu,'changePhysicalPortServiceDefSigDegThresOdu':changePhysicalPortServiceDefSigDegThresOdu,'changePhysicalPortServiceDefSigDegThreshold':changePhysicalPortServiceDefSigDegThreshold,'changePhysicalPortServiceDefSigDegPcslThreshold':changePhysicalPortServiceDefSigDegPcslThreshold,'changePhysicalPortServiceDefSigDegThresSonetSection':changePhysicalPortServiceDefSigDegThresSonetSection,'changePhysicalPortServiceDefSigDegThresSdhSection':changePhysicalPortServiceDefSigDegThresSdhSection,'changePhysicalPortServiceDefSigDegThresOduTcmA':changePhysicalPortServiceDefSigDegThresOduTcmA,'changePhysicalPortServiceDefSigDegThresOduTcmB':changePhysicalPortServiceDefSigDegThresOduTcmB,'changePhysicalPortServiceDefSigDegThresOduTcmC':changePhysicalPortServiceDefSigDegThresOduTcmC,'changePhysicalPortServiceDefSignalDegradePeriod':changePhysicalPortServiceDefSignalDegradePeriod,'changePhysicalPortServiceDefSigDegPeriodOdu':changePhysicalPortServiceDefSigDegPeriodOdu,'changePhysicalPortServiceDefSigDegPeriodOtu':changePhysicalPortServiceDefSigDegPeriodOtu,'changePhysicalPortServiceDefSigDegPeriodIntegration':changePhysicalPortServiceDefSigDegPeriodIntegration,'changePhysicalPortServiceDefSigDegPeriodSdhSection':changePhysicalPortServiceDefSigDegPeriodSdhSection,'changePhysicalPortServiceDefSigDegPeriodOduTcmA':changePhysicalPortServiceDefSigDegPeriodOduTcmA,'changePhysicalPortServiceDefSigDegPeriodOduTcmB':changePhysicalPortServiceDefSigDegPeriodOduTcmB,'changePhysicalPortServiceDefSigDegPeriodOduTcmC':changePhysicalPortServiceDefSigDegPeriodOduTcmC,'changePhysicalPortServiceDefOtnStuffing':changePhysicalPortServiceDefOtnStuffing,'changePhysicalPortServiceDefTcmALevel':changePhysicalPortServiceDefTcmALevel,'changePhysicalPortServiceDefTcmBLevel':changePhysicalPortServiceDefTcmBLevel,'changePhysicalPortServiceDefTcmCLevel':changePhysicalPortServiceDefTcmCLevel,'changePhysicalPortServiceDefTerminationLevel':changePhysicalPortServiceDefTerminationLevel,'changePhysicalPortServiceDefTimingSource':changePhysicalPortServiceDefTimingSource,'changePhysicalPortServiceDefTimModeOdu':changePhysicalPortServiceDefTimModeOdu,'changePhysicalPortServiceDefTimModeOtu':changePhysicalPortServiceDefTimModeOtu,'changePhysicalPortServiceDefTimModeSonetSection':changePhysicalPortServiceDefTimModeSonetSection,'changePhysicalPortServiceDefTimModeOduTcmA':changePhysicalPortServiceDefTimModeOduTcmA,'changePhysicalPortServiceDefTimModeOduTcmB':changePhysicalPortServiceDefTimModeOduTcmB,'changePhysicalPortServiceDefTimModeOduTcmC':changePhysicalPortServiceDefTimModeOduTcmC,'changePhysicalPortServiceDefTraceFormSonetSection':changePhysicalPortServiceDefTraceFormSonetSection,'changePhysicalPortServiceDefTraceExpectedSonetSection':changePhysicalPortServiceDefTraceExpectedSonetSection,'changePhysicalPortServiceDefTraceTransmitSonetSection':changePhysicalPortServiceDefTraceTransmitSonetSection,'changePhysicalPortServiceDefTraceExpectedOtu':changePhysicalPortServiceDefTraceExpectedOtu,'changePhysicalPortServiceDefTraceTransmitSapiOtu':changePhysicalPortServiceDefTraceTransmitSapiOtu,'changePhysicalPortServiceDefTraceTransmitDapiOtu':changePhysicalPortServiceDefTraceTransmitDapiOtu,'changePhysicalPortServiceDefTraceTransmitOpspOtu':changePhysicalPortServiceDefTraceTransmitOpspOtu,'changePhysicalPortServiceDefTraceExpectedOdu':changePhysicalPortServiceDefTraceExpectedOdu,'changePhysicalPortServiceDefTraceTransmitSapiOdu':changePhysicalPortServiceDefTraceTransmitSapiOdu,'changePhysicalPortServiceDefTraceTransmitDapiOdu':changePhysicalPortServiceDefTraceTransmitDapiOdu,'changePhysicalPortServiceDefTraceTransmitOpspOdu':changePhysicalPortServiceDefTraceTransmitOpspOdu,'changePhysicalPortServiceDefTraceExpectedOduTcmA':changePhysicalPortServiceDefTraceExpectedOduTcmA,'changePhysicalPortServiceDefTraceTransmitSapiOduTcmA':changePhysicalPortServiceDefTraceTransmitSapiOduTcmA,'changePhysicalPortServiceDefTraceTransmitDapiOduTcmA':changePhysicalPortServiceDefTraceTransmitDapiOduTcmA,'changePhysicalPortServiceDefTraceTransmitOpspOduTcmA':changePhysicalPortServiceDefTraceTransmitOpspOduTcmA,'changePhysicalPortServiceDefTraceExpectedOduTcmB':changePhysicalPortServiceDefTraceExpectedOduTcmB,'changePhysicalPortServiceDefTraceTransmitSapiOduTcmB':changePhysicalPortServiceDefTraceTransmitSapiOduTcmB,'changePhysicalPortServiceDefTraceTransmitDapiOduTcmB':changePhysicalPortServiceDefTraceTransmitDapiOduTcmB,'changePhysicalPortServiceDefTraceTransmitOpspOduTcmB':changePhysicalPortServiceDefTraceTransmitOpspOduTcmB,'changePhysicalPortServiceDefTraceExpectedOduTcmC':changePhysicalPortServiceDefTraceExpectedOduTcmC,'changePhysicalPortServiceDefTraceTransmitSapiOduTcmC':changePhysicalPortServiceDefTraceTransmitSapiOduTcmC,'changePhysicalPortServiceDefTraceTransmitDapiOduTcmC':changePhysicalPortServiceDefTraceTransmitDapiOduTcmC,'changePhysicalPortServiceDefTraceTransmitOpspOduTcmC':changePhysicalPortServiceDefTraceTransmitOpspOduTcmC,'changePhysicalPortServiceDefTxOffDelay':changePhysicalPortServiceDefTxOffDelay,'changePhysicalPortServiceDefVoaMode':changePhysicalPortServiceDefVoaMode,'changePhysicalPortServiceDefVoaSetpoint':changePhysicalPortServiceDefVoaSetpoint,'endOfChangePhysicalPortServiceDefTable':endOfChangePhysicalPortServiceDefTable,'endOfChangeServiceDef':endOfChangeServiceDef,'protectionDef':protectionDef,'ffpDefTable':ffpDefTable,'ffpDefEntry':ffpDefEntry,'ffpDefRowStatus':ffpDefRowStatus,'ffpDefCreationMethod':ffpDefCreationMethod,'ffpDefSDswitching':ffpDefSDswitching,'ffpDefHoldOffTime':ffpDefHoldOffTime,'ffpDefProtectionMech':ffpDefProtectionMech,'ffpDefWorkingAid':ffpDefWorkingAid,'ffpDefProtectionAid':ffpDefProtectionAid,'ffpDefSignalDegradeSwitching':ffpDefSignalDegradeSwitching,'ffpDefSignalFailureSwitching':ffpDefSignalFailureSwitching,'ffpDefFarEndIp':ffpDefFarEndIp,'ffpDefPeerAid':ffpDefPeerAid,'ffpDefApsType':ffpDefApsType,'ffpDefRevertMode':ffpDefRevertMode,'ffpDefWaitToRestore':ffpDefWaitToRestore,'ffpDefDirection':ffpDefDirection,'ffpDefProtectionType':ffpDefProtectionType,'endOfFfpDefTable':endOfFfpDefTable,'endOfProtectionDef':endOfProtectionDef,'conformanceDef':conformanceDef,'compliancesDef':compliancesDef,'complianceDef':complianceDef,'groupsDef':groupsDef,_BL:objectGroupDef})