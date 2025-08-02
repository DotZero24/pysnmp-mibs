_Au='ciscoWanFrPortServiceQueueGroup'
_At='ciscoWanFrPortsUsedGroup'
_As='ciscoWanFrPortDs0InDs1Group'
_Ar='ciscoWanFrPortSvcGroup'
_Aq='ciscoWanFrPortStatsGroup'
_Ap='ciscoWanFrPortStateGroup'
_Ao='ciscoWanFrPortConfGroup'
_An='frPortsUsedLine'
_Am='portBytesDiscXceedDEThresh'
_Al='portBytesDiscXceedQueFull'
_Ak='portQBwInc'
_Aj='portEgresDEThresh'
_Ai='portEgresECNThresh'
_Ah='portEgresQDepth'
_Ag='rcvPortBytesDiscXceedDEThresh'
_Af='xmtPortBytesDiscXceedDEThresh'
_Ae='xmtPortFramesDiscXceedDEThresh'
_Ad='rcvPortBytesDE'
_Ac='xmtPortBytesDE'
_Ab='xmtPortFramesDE'
_Aa='rcvPortFramesDiscard'
_AZ='rcvFramesDiscOverrun'
_AY='rcvFramesDiscNoChan'
_AX='portClrButton'
_AW='xmtBufNotAvailable'
_AV='xmtPortKbpsAIR'
_AU='xmtFramesUnderrun'
_AT='xmtFramesAbort'
_AS='xmtPortBytesDuringLMIAlarm'
_AR='xmtPortFramesDuringLMIAlarm'
_AQ='xmtPortBytesDiscXceedQDepth'
_AP='xmtPortFramesDiscXceedQDepth'
_AO='xmtPortFramesBECN'
_AN='xmtPortFramesFECN'
_AM='xmtPortBytes'
_AL='xmtPortFrames'
_AK='rcvBufNotAvailable'
_AJ='rcvPortKbpsAIR'
_AI='rcvPortFramesDiscXceedDEThresh'
_AH='rcvPortFramesTaggedDE'
_AG='rcvPortFramesTaggedBECN'
_AF='rcvPortFramesTaggedFECN'
_AE='rcvLastUnknownDLCI'
_AD='rcvFramesUnknownDLCI'
_AC='rcvFramesAbort'
_AB='rcvFramesDiscIllegalHeader'
_AA='rcvFramesDiscIllegalLen'
_A9='rcvFramesDiscAlignmentError'
_A8='rcvFramesDiscCRCError'
_A7='rcvPortFramesBECN'
_A6='rcvPortFramesFECN'
_A5='rcvPortFramesDE'
_A4='rcvPortBytes'
_A3='rcvPortFrames'
_A2='portEgrPercentUtil'
_A1='portIngrPercentUtil'
_A0='portOversubscribed'
_z='portSignallingState'
_y='portState'
_x='portNextAvailable'
_w='portsUsedLine8'
_v='portsUsedLine7'
_u='portsUsedLine6'
_t='portsUsedLine5'
_s='portsUsedLine4'
_r='portsUsedLine3'
_q='portsUsedLine2'
_p='portsUsedLine1'
_o='portEgrSvcBandW'
_n='portIngrSvcBandW'
_m='portDeleteSvcs'
_l='portSvcDlciHigh'
_k='portSvcDlciLow'
_j='portSvcLcnHigh'
_i='portSvcLcnLow'
_h='portSvcShareLcn'
_g='portSvcInUse'
_f='portSvcStatus'
_e='portOverSubEnable'
_d='portFileId'
_c='portFrameChkSumType'
_b='portHeaderLen'
_a='portM32EgrQueueThresh'
_Z='portEnhancedSIW'
_Y='portBERTEnable'
_X='portType'
_W='portAdmin'
_V='portSpeed'
_U='portEqueueServiceRatio'
_T='portFlagsBetweenFrames'
_S='portDs0Speed'
_R='portDs0ConfigBitMap'
_Q='portRowStatus'
_P='portLineNum'
_O='statePortNum'
_N='cntPortNum'
_M='portServiceQueueNo'
_L='frServPortNum'
_K='frPortsUsedLineIndex'
_J='portNum'
_I='enable'
_H='disable'
_G='Bytes'
_F='Frames'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-WAN-FR-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frPort,frPortCnf,frPortCnt,frPortServiceQueGrp=mibBuilder.importSymbols('BASIS-MIB','frPort','frPortCnf','frPortCnt','frPortServiceQueGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanFrPortMIB=ModuleIdentity((1,3,6,1,4,1,351,150,44))
if mibBuilder.loadTexts:ciscoWanFrPortMIB.setRevisions(('2002-10-17 00:00',))
_FrPortCnfPortGrp_ObjectIdentity=ObjectIdentity
frPortCnfPortGrp=_FrPortCnfPortGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,1,1))
_FrPortCnfPortGrpTable_Object=MibTable
frPortCnfPortGrpTable=_FrPortCnfPortGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1))
if mibBuilder.loadTexts:frPortCnfPortGrpTable.setStatus(_A)
_FrPortCnfPortGrpEntry_Object=MibTableRow
frPortCnfPortGrpEntry=_FrPortCnfPortGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1))
frPortCnfPortGrpEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:frPortCnfPortGrpEntry.setStatus(_A)
class _PortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortNum_Type.__name__=_D
_PortNum_Object=MibTableColumn
portNum=_PortNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,1),_PortNum_Type())
portNum.setMaxAccess(_C)
if mibBuilder.loadTexts:portNum.setStatus(_A)
class _PortLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortLineNum_Type.__name__=_D
_PortLineNum_Object=MibTableColumn
portLineNum=_PortLineNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,2),_PortLineNum_Type())
portLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:portLineNum.setStatus(_A)
class _PortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_PortRowStatus_Type.__name__=_D
_PortRowStatus_Object=MibTableColumn
portRowStatus=_PortRowStatus_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,3),_PortRowStatus_Type())
portRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portRowStatus.setStatus(_A)
class _PortDs0ConfigBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortDs0ConfigBitMap_Type.__name__=_D
_PortDs0ConfigBitMap_Object=MibTableColumn
portDs0ConfigBitMap=_PortDs0ConfigBitMap_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,4),_PortDs0ConfigBitMap_Type())
portDs0ConfigBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:portDs0ConfigBitMap.setStatus(_A)
class _PortDs0Speed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('speed56k',1),('speed64k',2),('unUsed',3)))
_PortDs0Speed_Type.__name__=_D
_PortDs0Speed_Object=MibTableColumn
portDs0Speed=_PortDs0Speed_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,5),_PortDs0Speed_Type())
portDs0Speed.setMaxAccess(_E)
if mibBuilder.loadTexts:portDs0Speed.setStatus(_A)
class _PortFlagsBetweenFrames_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_PortFlagsBetweenFrames_Type.__name__=_D
_PortFlagsBetweenFrames_Object=MibTableColumn
portFlagsBetweenFrames=_PortFlagsBetweenFrames_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,6),_PortFlagsBetweenFrames_Type())
portFlagsBetweenFrames.setMaxAccess(_E)
if mibBuilder.loadTexts:portFlagsBetweenFrames.setStatus(_A)
class _PortEqueueServiceRatio_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PortEqueueServiceRatio_Type.__name__=_D
_PortEqueueServiceRatio_Object=MibTableColumn
portEqueueServiceRatio=_PortEqueueServiceRatio_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,7),_PortEqueueServiceRatio_Type())
portEqueueServiceRatio.setMaxAccess(_E)
if mibBuilder.loadTexts:portEqueueServiceRatio.setStatus(_A)
_PortSpeed_Type=Integer32
_PortSpeed_Object=MibTableColumn
portSpeed=_PortSpeed_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,8),_PortSpeed_Type())
portSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portSpeed.setStatus(_A)
if mibBuilder.loadTexts:portSpeed.setUnits('kbps')
class _PortAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('write-Only',3)))
_PortAdmin_Type.__name__=_D
_PortAdmin_Object=MibTableColumn
portAdmin=_PortAdmin_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,9),_PortAdmin_Type())
portAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:portAdmin.setStatus(_A)
class _PortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('frame-relay',1),('frFUNI',2),('frame-forward',3)))
_PortType_Type.__name__=_D
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,10),_PortType_Type())
portType.setMaxAccess(_E)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortSvcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PortSvcStatus_Type.__name__=_D
_PortSvcStatus_Object=MibTableColumn
portSvcStatus=_PortSvcStatus_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,11),_PortSvcStatus_Type())
portSvcStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portSvcStatus.setStatus(_A)
class _PortSvcInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-use',1),('in-use',2)))
_PortSvcInUse_Type.__name__=_D
_PortSvcInUse_Object=MibTableColumn
portSvcInUse=_PortSvcInUse_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,12),_PortSvcInUse_Type())
portSvcInUse.setMaxAccess(_E)
if mibBuilder.loadTexts:portSvcInUse.setStatus(_A)
class _PortSvcShareLcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port-based',1),('card-based',2)))
_PortSvcShareLcn_Type.__name__=_D
_PortSvcShareLcn_Object=MibTableColumn
portSvcShareLcn=_PortSvcShareLcn_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,13),_PortSvcShareLcn_Type())
portSvcShareLcn.setMaxAccess(_C)
if mibBuilder.loadTexts:portSvcShareLcn.setStatus(_A)
class _PortSvcLcnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4015))
_PortSvcLcnLow_Type.__name__=_D
_PortSvcLcnLow_Object=MibTableColumn
portSvcLcnLow=_PortSvcLcnLow_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,14),_PortSvcLcnLow_Type())
portSvcLcnLow.setMaxAccess(_C)
if mibBuilder.loadTexts:portSvcLcnLow.setStatus(_A)
class _PortSvcLcnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4015))
_PortSvcLcnHigh_Type.__name__=_D
_PortSvcLcnHigh_Object=MibTableColumn
portSvcLcnHigh=_PortSvcLcnHigh_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,15),_PortSvcLcnHigh_Type())
portSvcLcnHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:portSvcLcnHigh.setStatus(_A)
class _PortSvcDlciLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_PortSvcDlciLow_Type.__name__=_D
_PortSvcDlciLow_Object=MibTableColumn
portSvcDlciLow=_PortSvcDlciLow_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,16),_PortSvcDlciLow_Type())
portSvcDlciLow.setMaxAccess(_C)
if mibBuilder.loadTexts:portSvcDlciLow.setStatus(_A)
class _PortSvcDlciHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_PortSvcDlciHigh_Type.__name__=_D
_PortSvcDlciHigh_Object=MibTableColumn
portSvcDlciHigh=_PortSvcDlciHigh_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,17),_PortSvcDlciHigh_Type())
portSvcDlciHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:portSvcDlciHigh.setStatus(_A)
class _PortDeleteSvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('other',2)))
_PortDeleteSvcs_Type.__name__=_D
_PortDeleteSvcs_Object=MibTableColumn
portDeleteSvcs=_PortDeleteSvcs_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,18),_PortDeleteSvcs_Type())
portDeleteSvcs.setMaxAccess(_E)
if mibBuilder.loadTexts:portDeleteSvcs.setStatus(_A)
_PortIngrSvcBandW_Type=Integer32
_PortIngrSvcBandW_Object=MibTableColumn
portIngrSvcBandW=_PortIngrSvcBandW_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,19),_PortIngrSvcBandW_Type())
portIngrSvcBandW.setMaxAccess(_C)
if mibBuilder.loadTexts:portIngrSvcBandW.setStatus(_A)
_PortEgrSvcBandW_Type=Integer32
_PortEgrSvcBandW_Object=MibTableColumn
portEgrSvcBandW=_PortEgrSvcBandW_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,20),_PortEgrSvcBandW_Type())
portEgrSvcBandW.setMaxAccess(_C)
if mibBuilder.loadTexts:portEgrSvcBandW.setStatus(_A)
class _PortBERTEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PortBERTEnable_Type.__name__=_D
_PortBERTEnable_Object=MibTableColumn
portBERTEnable=_PortBERTEnable_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,21),_PortBERTEnable_Type())
portBERTEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:portBERTEnable.setStatus(_A)
class _PortEnhancedSIW_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PortEnhancedSIW_Type.__name__=_D
_PortEnhancedSIW_Object=MibTableColumn
portEnhancedSIW=_PortEnhancedSIW_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,22),_PortEnhancedSIW_Type())
portEnhancedSIW.setMaxAccess(_E)
if mibBuilder.loadTexts:portEnhancedSIW.setStatus(_A)
class _PortM32EgrQueueThresh_Type(Integer32):defaultValue=6000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6000))
_PortM32EgrQueueThresh_Type.__name__=_D
_PortM32EgrQueueThresh_Object=MibTableColumn
portM32EgrQueueThresh=_PortM32EgrQueueThresh_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,23),_PortM32EgrQueueThresh_Type())
portM32EgrQueueThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:portM32EgrQueueThresh.setStatus(_A)
if mibBuilder.loadTexts:portM32EgrQueueThresh.setUnits('bytes')
class _PortHeaderLen_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoOctets',1),('fourOctets',2)))
_PortHeaderLen_Type.__name__=_D
_PortHeaderLen_Object=MibTableColumn
portHeaderLen=_PortHeaderLen_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,24),_PortHeaderLen_Type())
portHeaderLen.setMaxAccess(_E)
if mibBuilder.loadTexts:portHeaderLen.setStatus(_A)
if mibBuilder.loadTexts:portHeaderLen.setUnits('Octets')
class _PortFrameChkSumType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc16',1),('crc32',2)))
_PortFrameChkSumType_Type.__name__=_D
_PortFrameChkSumType_Object=MibTableColumn
portFrameChkSumType=_PortFrameChkSumType_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,25),_PortFrameChkSumType_Type())
portFrameChkSumType.setMaxAccess(_E)
if mibBuilder.loadTexts:portFrameChkSumType.setStatus(_A)
class _PortFileId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortFileId_Type.__name__=_D
_PortFileId_Object=MibTableColumn
portFileId=_PortFileId_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,26),_PortFileId_Type())
portFileId.setMaxAccess(_E)
if mibBuilder.loadTexts:portFileId.setStatus(_A)
class _PortOverSubEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_PortOverSubEnable_Type.__name__=_D
_PortOverSubEnable_Object=MibTableColumn
portOverSubEnable=_PortOverSubEnable_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,1,1,27),_PortOverSubEnable_Type())
portOverSubEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:portOverSubEnable.setStatus(_A)
class _PortsUsedLine1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine1_Type.__name__=_D
_PortsUsedLine1_Object=MibScalar
portsUsedLine1=_PortsUsedLine1_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,2),_PortsUsedLine1_Type())
portsUsedLine1.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine1.setStatus(_A)
class _PortsUsedLine2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine2_Type.__name__=_D
_PortsUsedLine2_Object=MibScalar
portsUsedLine2=_PortsUsedLine2_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,3),_PortsUsedLine2_Type())
portsUsedLine2.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine2.setStatus(_A)
class _PortsUsedLine3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine3_Type.__name__=_D
_PortsUsedLine3_Object=MibScalar
portsUsedLine3=_PortsUsedLine3_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,4),_PortsUsedLine3_Type())
portsUsedLine3.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine3.setStatus(_A)
class _PortsUsedLine4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine4_Type.__name__=_D
_PortsUsedLine4_Object=MibScalar
portsUsedLine4=_PortsUsedLine4_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,5),_PortsUsedLine4_Type())
portsUsedLine4.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine4.setStatus(_A)
class _PortNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_PortNextAvailable_Type.__name__=_D
_PortNextAvailable_Object=MibScalar
portNextAvailable=_PortNextAvailable_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,6),_PortNextAvailable_Type())
portNextAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:portNextAvailable.setStatus(_A)
class _PortsUsedLine5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine5_Type.__name__=_D
_PortsUsedLine5_Object=MibScalar
portsUsedLine5=_PortsUsedLine5_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,7),_PortsUsedLine5_Type())
portsUsedLine5.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine5.setStatus(_A)
class _PortsUsedLine6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine6_Type.__name__=_D
_PortsUsedLine6_Object=MibScalar
portsUsedLine6=_PortsUsedLine6_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,8),_PortsUsedLine6_Type())
portsUsedLine6.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine6.setStatus(_A)
class _PortsUsedLine7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine7_Type.__name__=_D
_PortsUsedLine7_Object=MibScalar
portsUsedLine7=_PortsUsedLine7_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,9),_PortsUsedLine7_Type())
portsUsedLine7.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine7.setStatus(_A)
class _PortsUsedLine8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortsUsedLine8_Type.__name__=_D
_PortsUsedLine8_Object=MibScalar
portsUsedLine8=_PortsUsedLine8_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,10),_PortsUsedLine8_Type())
portsUsedLine8.setMaxAccess(_C)
if mibBuilder.loadTexts:portsUsedLine8.setStatus(_A)
_FrPortsUsedLineGrpTable_Object=MibTable
frPortsUsedLineGrpTable=_FrPortsUsedLineGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,11))
if mibBuilder.loadTexts:frPortsUsedLineGrpTable.setStatus(_A)
_FrPortsUsedLineGrpEntry_Object=MibTableRow
frPortsUsedLineGrpEntry=_FrPortsUsedLineGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,11,1))
frPortsUsedLineGrpEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:frPortsUsedLineGrpEntry.setStatus(_A)
class _FrPortsUsedLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,56))
_FrPortsUsedLineIndex_Type.__name__=_D
_FrPortsUsedLineIndex_Object=MibTableColumn
frPortsUsedLineIndex=_FrPortsUsedLineIndex_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,11,1,1),_FrPortsUsedLineIndex_Type())
frPortsUsedLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frPortsUsedLineIndex.setStatus(_A)
class _FrPortsUsedLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FrPortsUsedLine_Type.__name__=_D
_FrPortsUsedLine_Object=MibTableColumn
frPortsUsedLine=_FrPortsUsedLine_Object((1,3,6,1,4,1,351,110,5,1,1,1,1,11,1,2),_FrPortsUsedLine_Type())
frPortsUsedLine.setMaxAccess(_C)
if mibBuilder.loadTexts:frPortsUsedLine.setStatus(_A)
_FrPortServiceQueGrpTable_Object=MibTable
frPortServiceQueGrpTable=_FrPortServiceQueGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1))
if mibBuilder.loadTexts:frPortServiceQueGrpTable.setStatus(_A)
_FrPortServiceQueGrpEntry_Object=MibTableRow
frPortServiceQueGrpEntry=_FrPortServiceQueGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1))
frPortServiceQueGrpEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:frPortServiceQueGrpEntry.setStatus(_A)
class _FrServPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrServPortNum_Type.__name__=_D
_FrServPortNum_Object=MibTableColumn
frServPortNum=_FrServPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,1),_FrServPortNum_Type())
frServPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:frServPortNum.setStatus(_A)
class _PortServiceQueueNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('highpriorityQ',1),('rtVBRQ',2),('nrtVBRandABRQ',3),('uBRQ',4),('queue5',5),('queue6',6),('queue7',7),('queue8',8)))
_PortServiceQueueNo_Type.__name__=_D
_PortServiceQueueNo_Object=MibTableColumn
portServiceQueueNo=_PortServiceQueueNo_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,2),_PortServiceQueueNo_Type())
portServiceQueueNo.setMaxAccess(_E)
if mibBuilder.loadTexts:portServiceQueueNo.setStatus(_A)
class _PortEgresQDepth_Type(Integer32):defaultValue=1048575;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_PortEgresQDepth_Type.__name__=_D
_PortEgresQDepth_Object=MibTableColumn
portEgresQDepth=_PortEgresQDepth_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,3),_PortEgresQDepth_Type())
portEgresQDepth.setMaxAccess(_E)
if mibBuilder.loadTexts:portEgresQDepth.setStatus(_A)
class _PortEgresECNThresh_Type(Integer32):defaultValue=104857;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_PortEgresECNThresh_Type.__name__=_D
_PortEgresECNThresh_Object=MibTableColumn
portEgresECNThresh=_PortEgresECNThresh_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,4),_PortEgresECNThresh_Type())
portEgresECNThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:portEgresECNThresh.setStatus(_A)
class _PortEgresDEThresh_Type(Integer32):defaultValue=524287;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2097151))
_PortEgresDEThresh_Type.__name__=_D
_PortEgresDEThresh_Object=MibTableColumn
portEgresDEThresh=_PortEgresDEThresh_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,5),_PortEgresDEThresh_Type())
portEgresDEThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:portEgresDEThresh.setStatus(_A)
class _PortQBwInc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_PortQBwInc_Type.__name__=_D
_PortQBwInc_Object=MibTableColumn
portQBwInc=_PortQBwInc_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,6),_PortQBwInc_Type())
portQBwInc.setMaxAccess(_C)
if mibBuilder.loadTexts:portQBwInc.setStatus(_A)
_PortBytesDiscXceedQueFull_Type=Counter32
_PortBytesDiscXceedQueFull_Object=MibTableColumn
portBytesDiscXceedQueFull=_PortBytesDiscXceedQueFull_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,7),_PortBytesDiscXceedQueFull_Type())
portBytesDiscXceedQueFull.setMaxAccess(_C)
if mibBuilder.loadTexts:portBytesDiscXceedQueFull.setStatus(_A)
if mibBuilder.loadTexts:portBytesDiscXceedQueFull.setUnits(_G)
_PortBytesDiscXceedDEThresh_Type=Counter32
_PortBytesDiscXceedDEThresh_Object=MibTableColumn
portBytesDiscXceedDEThresh=_PortBytesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,1,1,4,1,1,8),_PortBytesDiscXceedDEThresh_Type())
portBytesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:portBytesDiscXceedDEThresh.setStatus(_A)
if mibBuilder.loadTexts:portBytesDiscXceedDEThresh.setUnits(_G)
_FrPortCntPortGrp_ObjectIdentity=ObjectIdentity
frPortCntPortGrp=_FrPortCntPortGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,2,1))
_FrPortCntPortGrpTable_Object=MibTable
frPortCntPortGrpTable=_FrPortCntPortGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1))
if mibBuilder.loadTexts:frPortCntPortGrpTable.setStatus(_A)
_FrPortCntPortGrpEntry_Object=MibTableRow
frPortCntPortGrpEntry=_FrPortCntPortGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1))
frPortCntPortGrpEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:frPortCntPortGrpEntry.setStatus(_A)
class _CntPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CntPortNum_Type.__name__=_D
_CntPortNum_Object=MibTableColumn
cntPortNum=_CntPortNum_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,1),_CntPortNum_Type())
cntPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cntPortNum.setStatus(_A)
_RcvPortFrames_Type=Counter32
_RcvPortFrames_Object=MibTableColumn
rcvPortFrames=_RcvPortFrames_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,2),_RcvPortFrames_Type())
rcvPortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFrames.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFrames.setUnits(_F)
_RcvPortBytes_Type=Counter32
_RcvPortBytes_Object=MibTableColumn
rcvPortBytes=_RcvPortBytes_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,3),_RcvPortBytes_Type())
rcvPortBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortBytes.setStatus(_A)
if mibBuilder.loadTexts:rcvPortBytes.setUnits(_G)
_RcvPortFramesDE_Type=Counter32
_RcvPortFramesDE_Object=MibTableColumn
rcvPortFramesDE=_RcvPortFramesDE_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,4),_RcvPortFramesDE_Type())
rcvPortFramesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesDE.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesDE.setUnits(_F)
_RcvPortFramesFECN_Type=Counter32
_RcvPortFramesFECN_Object=MibTableColumn
rcvPortFramesFECN=_RcvPortFramesFECN_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,5),_RcvPortFramesFECN_Type())
rcvPortFramesFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesFECN.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesFECN.setUnits(_F)
_RcvPortFramesBECN_Type=Counter32
_RcvPortFramesBECN_Object=MibTableColumn
rcvPortFramesBECN=_RcvPortFramesBECN_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,6),_RcvPortFramesBECN_Type())
rcvPortFramesBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesBECN.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesBECN.setUnits(_F)
_RcvFramesDiscCRCError_Type=Counter32
_RcvFramesDiscCRCError_Object=MibTableColumn
rcvFramesDiscCRCError=_RcvFramesDiscCRCError_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,7),_RcvFramesDiscCRCError_Type())
rcvFramesDiscCRCError.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscCRCError.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscCRCError.setUnits(_F)
_RcvFramesDiscAlignmentError_Type=Counter32
_RcvFramesDiscAlignmentError_Object=MibTableColumn
rcvFramesDiscAlignmentError=_RcvFramesDiscAlignmentError_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,8),_RcvFramesDiscAlignmentError_Type())
rcvFramesDiscAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscAlignmentError.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscAlignmentError.setUnits(_F)
_RcvFramesDiscIllegalLen_Type=Counter32
_RcvFramesDiscIllegalLen_Object=MibTableColumn
rcvFramesDiscIllegalLen=_RcvFramesDiscIllegalLen_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,9),_RcvFramesDiscIllegalLen_Type())
rcvFramesDiscIllegalLen.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscIllegalLen.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscIllegalLen.setUnits(_F)
_RcvFramesDiscIllegalHeader_Type=Counter32
_RcvFramesDiscIllegalHeader_Object=MibTableColumn
rcvFramesDiscIllegalHeader=_RcvFramesDiscIllegalHeader_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,10),_RcvFramesDiscIllegalHeader_Type())
rcvFramesDiscIllegalHeader.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscIllegalHeader.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscIllegalHeader.setUnits(_F)
_RcvFramesAbort_Type=Counter32
_RcvFramesAbort_Object=MibTableColumn
rcvFramesAbort=_RcvFramesAbort_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,11),_RcvFramesAbort_Type())
rcvFramesAbort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesAbort.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesAbort.setUnits(_F)
_RcvFramesUnknownDLCI_Type=Counter32
_RcvFramesUnknownDLCI_Object=MibTableColumn
rcvFramesUnknownDLCI=_RcvFramesUnknownDLCI_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,12),_RcvFramesUnknownDLCI_Type())
rcvFramesUnknownDLCI.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesUnknownDLCI.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesUnknownDLCI.setUnits(_F)
_RcvLastUnknownDLCI_Type=Integer32
_RcvLastUnknownDLCI_Object=MibTableColumn
rcvLastUnknownDLCI=_RcvLastUnknownDLCI_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,13),_RcvLastUnknownDLCI_Type())
rcvLastUnknownDLCI.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvLastUnknownDLCI.setStatus(_A)
_RcvPortFramesTaggedFECN_Type=Counter32
_RcvPortFramesTaggedFECN_Object=MibTableColumn
rcvPortFramesTaggedFECN=_RcvPortFramesTaggedFECN_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,14),_RcvPortFramesTaggedFECN_Type())
rcvPortFramesTaggedFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesTaggedFECN.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesTaggedFECN.setUnits(_F)
_RcvPortFramesTaggedBECN_Type=Counter32
_RcvPortFramesTaggedBECN_Object=MibTableColumn
rcvPortFramesTaggedBECN=_RcvPortFramesTaggedBECN_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,15),_RcvPortFramesTaggedBECN_Type())
rcvPortFramesTaggedBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesTaggedBECN.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesTaggedBECN.setUnits(_F)
_RcvPortFramesTaggedDE_Type=Counter32
_RcvPortFramesTaggedDE_Object=MibTableColumn
rcvPortFramesTaggedDE=_RcvPortFramesTaggedDE_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,16),_RcvPortFramesTaggedDE_Type())
rcvPortFramesTaggedDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesTaggedDE.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesTaggedDE.setUnits(_F)
_RcvPortFramesDiscXceedDEThresh_Type=Counter32
_RcvPortFramesDiscXceedDEThresh_Object=MibTableColumn
rcvPortFramesDiscXceedDEThresh=_RcvPortFramesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,17),_RcvPortFramesDiscXceedDEThresh_Type())
rcvPortFramesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesDiscXceedDEThresh.setStatus(_A)
if mibBuilder.loadTexts:rcvPortFramesDiscXceedDEThresh.setUnits(_F)
_RcvPortKbpsAIR_Type=Integer32
_RcvPortKbpsAIR_Object=MibTableColumn
rcvPortKbpsAIR=_RcvPortKbpsAIR_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,18),_RcvPortKbpsAIR_Type())
rcvPortKbpsAIR.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortKbpsAIR.setStatus(_A)
if mibBuilder.loadTexts:rcvPortKbpsAIR.setUnits('kbps')
_RcvBufNotAvailable_Type=Counter32
_RcvBufNotAvailable_Object=MibTableColumn
rcvBufNotAvailable=_RcvBufNotAvailable_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,19),_RcvBufNotAvailable_Type())
rcvBufNotAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvBufNotAvailable.setStatus(_A)
_XmtPortFrames_Type=Counter32
_XmtPortFrames_Object=MibTableColumn
xmtPortFrames=_XmtPortFrames_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,20),_XmtPortFrames_Type())
xmtPortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFrames.setStatus(_A)
if mibBuilder.loadTexts:xmtPortFrames.setUnits(_F)
_XmtPortBytes_Type=Counter32
_XmtPortBytes_Object=MibTableColumn
xmtPortBytes=_XmtPortBytes_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,21),_XmtPortBytes_Type())
xmtPortBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortBytes.setStatus(_A)
if mibBuilder.loadTexts:xmtPortBytes.setUnits(_G)
_XmtPortFramesFECN_Type=Counter32
_XmtPortFramesFECN_Object=MibTableColumn
xmtPortFramesFECN=_XmtPortFramesFECN_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,22),_XmtPortFramesFECN_Type())
xmtPortFramesFECN.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFramesFECN.setStatus(_A)
if mibBuilder.loadTexts:xmtPortFramesFECN.setUnits(_F)
_XmtPortFramesBECN_Type=Counter32
_XmtPortFramesBECN_Object=MibTableColumn
xmtPortFramesBECN=_XmtPortFramesBECN_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,23),_XmtPortFramesBECN_Type())
xmtPortFramesBECN.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFramesBECN.setStatus(_A)
if mibBuilder.loadTexts:xmtPortFramesBECN.setUnits(_F)
_XmtPortFramesDiscXceedQDepth_Type=Counter32
_XmtPortFramesDiscXceedQDepth_Object=MibTableColumn
xmtPortFramesDiscXceedQDepth=_XmtPortFramesDiscXceedQDepth_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,24),_XmtPortFramesDiscXceedQDepth_Type())
xmtPortFramesDiscXceedQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFramesDiscXceedQDepth.setStatus(_A)
if mibBuilder.loadTexts:xmtPortFramesDiscXceedQDepth.setUnits(_F)
_XmtPortBytesDiscXceedQDepth_Type=Counter32
_XmtPortBytesDiscXceedQDepth_Object=MibTableColumn
xmtPortBytesDiscXceedQDepth=_XmtPortBytesDiscXceedQDepth_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,25),_XmtPortBytesDiscXceedQDepth_Type())
xmtPortBytesDiscXceedQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortBytesDiscXceedQDepth.setStatus(_A)
if mibBuilder.loadTexts:xmtPortBytesDiscXceedQDepth.setUnits(_G)
_XmtPortFramesDuringLMIAlarm_Type=Counter32
_XmtPortFramesDuringLMIAlarm_Object=MibTableColumn
xmtPortFramesDuringLMIAlarm=_XmtPortFramesDuringLMIAlarm_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,26),_XmtPortFramesDuringLMIAlarm_Type())
xmtPortFramesDuringLMIAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFramesDuringLMIAlarm.setStatus(_A)
if mibBuilder.loadTexts:xmtPortFramesDuringLMIAlarm.setUnits(_F)
_XmtPortBytesDuringLMIAlarm_Type=Counter32
_XmtPortBytesDuringLMIAlarm_Object=MibTableColumn
xmtPortBytesDuringLMIAlarm=_XmtPortBytesDuringLMIAlarm_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,27),_XmtPortBytesDuringLMIAlarm_Type())
xmtPortBytesDuringLMIAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortBytesDuringLMIAlarm.setStatus(_A)
if mibBuilder.loadTexts:xmtPortBytesDuringLMIAlarm.setUnits(_G)
_XmtFramesAbort_Type=Counter32
_XmtFramesAbort_Object=MibTableColumn
xmtFramesAbort=_XmtFramesAbort_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,28),_XmtFramesAbort_Type())
xmtFramesAbort.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesAbort.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesAbort.setUnits(_F)
_XmtFramesUnderrun_Type=Counter32
_XmtFramesUnderrun_Object=MibTableColumn
xmtFramesUnderrun=_XmtFramesUnderrun_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,29),_XmtFramesUnderrun_Type())
xmtFramesUnderrun.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtFramesUnderrun.setStatus(_A)
if mibBuilder.loadTexts:xmtFramesUnderrun.setUnits(_F)
_XmtPortKbpsAIR_Type=Integer32
_XmtPortKbpsAIR_Object=MibTableColumn
xmtPortKbpsAIR=_XmtPortKbpsAIR_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,30),_XmtPortKbpsAIR_Type())
xmtPortKbpsAIR.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortKbpsAIR.setStatus(_A)
if mibBuilder.loadTexts:xmtPortKbpsAIR.setUnits('Kbps')
_XmtBufNotAvailable_Type=Counter32
_XmtBufNotAvailable_Object=MibTableColumn
xmtBufNotAvailable=_XmtBufNotAvailable_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,31),_XmtBufNotAvailable_Type())
xmtBufNotAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtBufNotAvailable.setStatus(_A)
class _PortClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_PortClrButton_Type.__name__=_D
_PortClrButton_Object=MibTableColumn
portClrButton=_PortClrButton_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,32),_PortClrButton_Type())
portClrButton.setMaxAccess(_E)
if mibBuilder.loadTexts:portClrButton.setStatus(_A)
_RcvFramesDiscNoChan_Type=Counter32
_RcvFramesDiscNoChan_Object=MibTableColumn
rcvFramesDiscNoChan=_RcvFramesDiscNoChan_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,33),_RcvFramesDiscNoChan_Type())
rcvFramesDiscNoChan.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscNoChan.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscNoChan.setUnits(_F)
_RcvFramesDiscOverrun_Type=Counter32
_RcvFramesDiscOverrun_Object=MibTableColumn
rcvFramesDiscOverrun=_RcvFramesDiscOverrun_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,34),_RcvFramesDiscOverrun_Type())
rcvFramesDiscOverrun.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvFramesDiscOverrun.setStatus(_A)
if mibBuilder.loadTexts:rcvFramesDiscOverrun.setUnits(_F)
_RcvPortFramesDiscard_Type=Counter32
_RcvPortFramesDiscard_Object=MibTableColumn
rcvPortFramesDiscard=_RcvPortFramesDiscard_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,35),_RcvPortFramesDiscard_Type())
rcvPortFramesDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortFramesDiscard.setStatus(_A)
_XmtPortFramesDE_Type=Counter32
_XmtPortFramesDE_Object=MibTableColumn
xmtPortFramesDE=_XmtPortFramesDE_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,36),_XmtPortFramesDE_Type())
xmtPortFramesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFramesDE.setStatus(_A)
_XmtPortBytesDE_Type=Counter32
_XmtPortBytesDE_Object=MibTableColumn
xmtPortBytesDE=_XmtPortBytesDE_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,37),_XmtPortBytesDE_Type())
xmtPortBytesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortBytesDE.setStatus(_A)
_RcvPortBytesDE_Type=Counter32
_RcvPortBytesDE_Object=MibTableColumn
rcvPortBytesDE=_RcvPortBytesDE_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,38),_RcvPortBytesDE_Type())
rcvPortBytesDE.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortBytesDE.setStatus(_A)
_XmtPortFramesDiscXceedDEThresh_Type=Counter32
_XmtPortFramesDiscXceedDEThresh_Object=MibTableColumn
xmtPortFramesDiscXceedDEThresh=_XmtPortFramesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,39),_XmtPortFramesDiscXceedDEThresh_Type())
xmtPortFramesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortFramesDiscXceedDEThresh.setStatus(_A)
_XmtPortBytesDiscXceedDEThresh_Type=Counter32
_XmtPortBytesDiscXceedDEThresh_Object=MibTableColumn
xmtPortBytesDiscXceedDEThresh=_XmtPortBytesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,40),_XmtPortBytesDiscXceedDEThresh_Type())
xmtPortBytesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:xmtPortBytesDiscXceedDEThresh.setStatus(_A)
_RcvPortBytesDiscXceedDEThresh_Type=Counter32
_RcvPortBytesDiscXceedDEThresh_Object=MibTableColumn
rcvPortBytesDiscXceedDEThresh=_RcvPortBytesDiscXceedDEThresh_Object((1,3,6,1,4,1,351,110,5,1,1,2,1,1,1,41),_RcvPortBytesDiscXceedDEThresh_Type())
rcvPortBytesDiscXceedDEThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcvPortBytesDiscXceedDEThresh.setStatus(_A)
_FrPortStateGrp_ObjectIdentity=ObjectIdentity
frPortStateGrp=_FrPortStateGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,1,1,3))
_FrPortStateGrpTable_Object=MibTable
frPortStateGrpTable=_FrPortStateGrpTable_Object((1,3,6,1,4,1,351,110,5,1,1,3,1))
if mibBuilder.loadTexts:frPortStateGrpTable.setStatus(_A)
_FrPortStateGrpEntry_Object=MibTableRow
frPortStateGrpEntry=_FrPortStateGrpEntry_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1))
frPortStateGrpEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:frPortStateGrpEntry.setStatus(_A)
class _StatePortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_StatePortNum_Type.__name__=_D
_StatePortNum_Object=MibTableColumn
statePortNum=_StatePortNum_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1,1),_StatePortNum_Type())
statePortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:statePortNum.setStatus(_A)
class _PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('notConfigured',1),('active',2),('remoteLoopback',3),('failedDueToLine',4),('failedDueToSignalling',5),('inactive',6),('inBert',7),('farEndRemoteLoopback',8),('latchDS0DropFeLoop',9),('latchDS0LineFeLoop',10),('latchOcuFeLoop',11),('latchCsuFeLoop',12),('latchDsuFeLoop',13),('latchHL96FeLoop',14),('v54PolynomialFeLoop',15)))
_PortState_Type.__name__=_D
_PortState_Object=MibTableColumn
portState=_PortState_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1,2),_PortState_Type())
portState.setMaxAccess(_C)
if mibBuilder.loadTexts:portState.setStatus(_A)
class _PortSignallingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_PortSignallingState_Type.__name__=_D
_PortSignallingState_Object=MibTableColumn
portSignallingState=_PortSignallingState_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1,3),_PortSignallingState_Type())
portSignallingState.setMaxAccess(_C)
if mibBuilder.loadTexts:portSignallingState.setStatus(_A)
class _PortOversubscribed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_PortOversubscribed_Type.__name__=_D
_PortOversubscribed_Object=MibTableColumn
portOversubscribed=_PortOversubscribed_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1,4),_PortOversubscribed_Type())
portOversubscribed.setMaxAccess(_C)
if mibBuilder.loadTexts:portOversubscribed.setStatus(_A)
class _PortIngrPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PortIngrPercentUtil_Type.__name__=_D
_PortIngrPercentUtil_Object=MibTableColumn
portIngrPercentUtil=_PortIngrPercentUtil_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1,5),_PortIngrPercentUtil_Type())
portIngrPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:portIngrPercentUtil.setStatus(_A)
class _PortEgrPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PortEgrPercentUtil_Type.__name__=_D
_PortEgrPercentUtil_Object=MibTableColumn
portEgrPercentUtil=_PortEgrPercentUtil_Object((1,3,6,1,4,1,351,110,5,1,1,3,1,1,6),_PortEgrPercentUtil_Type())
portEgrPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:portEgrPercentUtil.setStatus(_A)
_CiscoWanFrPortMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanFrPortMIBConformance=_CiscoWanFrPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,44,2))
_CiscoWanFrPortMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanFrPortMIBGroups=_CiscoWanFrPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,44,2,1))
_CiscoWanFrPortMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanFrPortMIBCompliances=_CiscoWanFrPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,44,2,2))
ciscoWanFrPortConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,1))
ciscoWanFrPortConfGroup.setObjects(*((_B,_J),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciscoWanFrPortConfGroup.setStatus(_A)
ciscoWanFrPortSvcGroup=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,2))
ciscoWanFrPortSvcGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoWanFrPortSvcGroup.setStatus(_A)
ciscoWanFrPortDs0InDs1Group=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,3))
ciscoWanFrPortDs0InDs1Group.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoWanFrPortDs0InDs1Group.setStatus(_A)
ciscoWanFrPortStateGroup=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,4))
ciscoWanFrPortStateGroup.setObjects(*((_B,_O),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoWanFrPortStateGroup.setStatus(_A)
ciscoWanFrPortStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,5))
ciscoWanFrPortStatsGroup.setObjects(*((_B,_N),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:ciscoWanFrPortStatsGroup.setStatus(_A)
ciscoWanFrPortServiceQueueGroup=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,6))
ciscoWanFrPortServiceQueueGroup.setObjects(*((_B,_L),(_B,_M),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:ciscoWanFrPortServiceQueueGroup.setStatus(_A)
ciscoWanFrPortsUsedGroup=ObjectGroup((1,3,6,1,4,1,351,150,44,2,1,7))
ciscoWanFrPortsUsedGroup.setObjects(*((_B,_K),(_B,_An)))
if mibBuilder.loadTexts:ciscoWanFrPortsUsedGroup.setStatus(_A)
ciscoWanFrPortCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,44,2,2,1))
ciscoWanFrPortCompliance.setObjects(*((_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:ciscoWanFrPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frPortCnfPortGrp':frPortCnfPortGrp,'frPortCnfPortGrpTable':frPortCnfPortGrpTable,'frPortCnfPortGrpEntry':frPortCnfPortGrpEntry,_J:portNum,_P:portLineNum,_Q:portRowStatus,_R:portDs0ConfigBitMap,_S:portDs0Speed,_T:portFlagsBetweenFrames,_U:portEqueueServiceRatio,_V:portSpeed,_W:portAdmin,_X:portType,_f:portSvcStatus,_g:portSvcInUse,_h:portSvcShareLcn,_i:portSvcLcnLow,_j:portSvcLcnHigh,_k:portSvcDlciLow,_l:portSvcDlciHigh,_m:portDeleteSvcs,_n:portIngrSvcBandW,_o:portEgrSvcBandW,_Y:portBERTEnable,_Z:portEnhancedSIW,_a:portM32EgrQueueThresh,_b:portHeaderLen,_c:portFrameChkSumType,_d:portFileId,_e:portOverSubEnable,_p:portsUsedLine1,_q:portsUsedLine2,_r:portsUsedLine3,_s:portsUsedLine4,_x:portNextAvailable,_t:portsUsedLine5,_u:portsUsedLine6,_v:portsUsedLine7,_w:portsUsedLine8,'frPortsUsedLineGrpTable':frPortsUsedLineGrpTable,'frPortsUsedLineGrpEntry':frPortsUsedLineGrpEntry,_K:frPortsUsedLineIndex,_An:frPortsUsedLine,'frPortServiceQueGrpTable':frPortServiceQueGrpTable,'frPortServiceQueGrpEntry':frPortServiceQueGrpEntry,_L:frServPortNum,_M:portServiceQueueNo,_Ah:portEgresQDepth,_Ai:portEgresECNThresh,_Aj:portEgresDEThresh,_Ak:portQBwInc,_Al:portBytesDiscXceedQueFull,_Am:portBytesDiscXceedDEThresh,'frPortCntPortGrp':frPortCntPortGrp,'frPortCntPortGrpTable':frPortCntPortGrpTable,'frPortCntPortGrpEntry':frPortCntPortGrpEntry,_N:cntPortNum,_A3:rcvPortFrames,_A4:rcvPortBytes,_A5:rcvPortFramesDE,_A6:rcvPortFramesFECN,_A7:rcvPortFramesBECN,_A8:rcvFramesDiscCRCError,_A9:rcvFramesDiscAlignmentError,_AA:rcvFramesDiscIllegalLen,_AB:rcvFramesDiscIllegalHeader,_AC:rcvFramesAbort,_AD:rcvFramesUnknownDLCI,_AE:rcvLastUnknownDLCI,_AF:rcvPortFramesTaggedFECN,_AG:rcvPortFramesTaggedBECN,_AH:rcvPortFramesTaggedDE,_AI:rcvPortFramesDiscXceedDEThresh,_AJ:rcvPortKbpsAIR,_AK:rcvBufNotAvailable,_AL:xmtPortFrames,_AM:xmtPortBytes,_AN:xmtPortFramesFECN,_AO:xmtPortFramesBECN,_AP:xmtPortFramesDiscXceedQDepth,_AQ:xmtPortBytesDiscXceedQDepth,_AR:xmtPortFramesDuringLMIAlarm,_AS:xmtPortBytesDuringLMIAlarm,_AT:xmtFramesAbort,_AU:xmtFramesUnderrun,_AV:xmtPortKbpsAIR,_AW:xmtBufNotAvailable,_AX:portClrButton,_AY:rcvFramesDiscNoChan,_AZ:rcvFramesDiscOverrun,_Aa:rcvPortFramesDiscard,_Ab:xmtPortFramesDE,_Ac:xmtPortBytesDE,_Ad:rcvPortBytesDE,_Ae:xmtPortFramesDiscXceedDEThresh,_Af:xmtPortBytesDiscXceedDEThresh,_Ag:rcvPortBytesDiscXceedDEThresh,'frPortStateGrp':frPortStateGrp,'frPortStateGrpTable':frPortStateGrpTable,'frPortStateGrpEntry':frPortStateGrpEntry,_O:statePortNum,_y:portState,_z:portSignallingState,_A0:portOversubscribed,_A1:portIngrPercentUtil,_A2:portEgrPercentUtil,'ciscoWanFrPortMIB':ciscoWanFrPortMIB,'ciscoWanFrPortMIBConformance':ciscoWanFrPortMIBConformance,'ciscoWanFrPortMIBGroups':ciscoWanFrPortMIBGroups,_Ao:ciscoWanFrPortConfGroup,_Ar:ciscoWanFrPortSvcGroup,_As:ciscoWanFrPortDs0InDs1Group,_Ap:ciscoWanFrPortStateGroup,_Aq:ciscoWanFrPortStatsGroup,_Au:ciscoWanFrPortServiceQueueGroup,_At:ciscoWanFrPortsUsedGroup,'ciscoWanFrPortMIBCompliances':ciscoWanFrPortMIBCompliances,'ciscoWanFrPortCompliance':ciscoWanFrPortCompliance})