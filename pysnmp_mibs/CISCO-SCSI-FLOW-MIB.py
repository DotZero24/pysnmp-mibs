_Ae='ciscoScsiFlowFeatureStatusGroup'
_Ad='ciscoScsiFlowStatsGroup'
_Ac='ciscoScsiFlowInfoGroup'
_Ab='ciscoScsiFlowNotifyGroup'
_Aa='ciscoScsiFlowGroup'
_AZ='ciscoScsiFlowStatsNotify'
_AY='ciscoScsiFlowWrAccNotify'
_AX='ciscoScsiFlowVerifyNotify'
_AW='ciscoScsiFlowStatsTgtCfgStatus'
_AV='ciscoScsiFlowStatsIntrCfgStatus'
_AU='ciscoScsiFlowStatsCfgStatus'
_AT='ciscoScsiFlowWrAccTgtCfgStatus'
_AS='ciscoScsiFlowWrAccIntrCfgStatus'
_AR='ciscoScsiFlowWrAccCfgStatus'
_AQ='ciscoScsiFlowAbts'
_AP='ciscoScsiFlowSenseKeyMiscmpErrs'
_AO='ciscoScsiFlowSenseKeyVolFlowErrs'
_AN='ciscoScsiFlowSenseKeyAbrtCmdErrs'
_AM='ciscoScsiFlowSenseKeyCpAbrtErrs'
_AL='ciscoScsiFlowSenseKeyBlankErrs'
_AK='ciscoScsiFlowSenseKeyDatProtErrs'
_AJ='ciscoScsiFlowSenseKeyUnitAttErrs'
_AI='ciscoScsiFlowSenseKeyIllReqErrs'
_AH='ciscoScsiFlowSenseKeyHwErrs'
_AG='ciscoScsiFlowSenseKeyMedErrs'
_AF='ciscoScsiFlowSenseKeyNotRdyErrs'
_AE='ciscoScsiFlowAcaActiveStatuses'
_AD='ciscoScsiFlowTskSetFulStatuses'
_AC='ciscoScsiFlowStatusResvConfs'
_AB='ciscoScsiFlowBusyStatuses'
_AA='ciscoScsiFlowTxFc2Octets'
_A9='ciscoScsiFlowRxFc2Octets'
_A8='ciscoScsiFlowTxFc2Frames'
_A7='ciscoScsiFlowRxFc2Frames'
_A6='ciscoScsiFlowReqSenses'
_A5='ciscoScsiFlowModeSenses'
_A4='ciscoScsiFlowRdCapacitys'
_A3='ciscoScsiFlowInquirys'
_A2='ciscoScsiFlowRepLuns'
_A1='ciscoScsiFlowTestUnitRdys'
_A0='ciscoScsiFlowWrsActive'
_z='ciscoScsiFlowWrMaxTime'
_y='ciscoScsiFlowWrMinTime'
_x='ciscoScsiFlowWrMaxBlocks'
_w='ciscoScsiFlowWrBlocks'
_v='ciscoScsiFlowWrTimeouts'
_u='ciscoScsiFlowWrFailedIos'
_t='ciscoScsiFlowWrIos'
_s='ciscoScsiFlowRdsActive'
_r='ciscoScsiFlowRdMaxTime'
_q='ciscoScsiFlowRdMinTime'
_p='ciscoScsiFlowRdMaxBlocks'
_o='ciscoScsiFlowRdBlocks'
_n='ciscoScsiFlowRdTimeouts'
_m='ciscoScsiFlowRdFailedIos'
_l='ciscoScsiFlowRdIos'
_k='ciscoScsiFlowTgtVrfStatus'
_j='ciscoScsiFlowTgtLCStatus'
_i='ciscoScsiFlowIntrLCStatus'
_h='ciscoScsiFlowIntrVrfStatus'
_g='ciscoScsiFlowClearStats'
_f='ciscoScsiFlowRowStatus'
_e='ciscoScsiFlowStatsEnabled'
_d='ciscoScsiFlowBufCount'
_c='ciscoScsiFlowWriteAcc'
_b='ciscoScsiFlowAllLuns'
_a='ciscoScsiFlowTargetVsan'
_Z='ciscoScsiFlowIntrVsan'
_Y='ciscoScsiFlowTargetWwn'
_X='ciscoScsiFlowIntrWwn'
_W='ciscoScsiFlowNextIndexAvail'
_V='ciscoScsiFlowLunId'
_U='not-accessible'
_T='statusNotChecked'
_S='cfsTimeout'
_R='cfsError'
_Q='ipcTimeout'
_P='deviceNotOnIlc'
_O='Integer32'
_N='ciscoScsiFlowVerifyReasonCode'
_M='success'
_L='VsanIndex'
_K='ciscoScsiFlowCfgReasonCode'
_J='accessible-for-notify'
_I='TruthValue'
_H='ciscoScsiFlowDeviceType'
_G='ciscoScsiFlowNum'
_F='ciscoScsiFlowId'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='CISCO-SCSI-FLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ScsiLUNOrZero,=mibBuilder.importSymbols('CISCO-SCSI-MIB','ScsiLUNOrZero')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
ciscoScsiFlowMIB=ModuleIdentity((1,3,6,1,4,1,9,9,447))
if mibBuilder.loadTexts:ciscoScsiFlowMIB.setRevisions(('2005-01-06 00:00',))
class CSFlowDeviceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('initiator',1),('target',2)))
class CSFlowVerifyReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_M,1),('noLicense',2),('generalError',3),('notInNameServer',4),('notInFlogiServer',5),(_P,6),('deviceNotScsi',7),('deviceNotInitiator',8),('deviceNotTarget',9),('deviceNotFibreChannel',10),(_Q,11),(_R,12),(_S,13),('portsUnprovisioned',14),('initTargetZonedOut',15),(_T,16),('initNotInNameServer',17),('tgtNotInNameServer',18),('tgtNotInFlogiServer',19)))
class CSFlowCfgReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_M,1),('ipcError',2),(_Q,3),('sfmGenericError',4),('sfcGenericError',5),(_R,6),(_S,7),(_P,8),('lcIpcError',9),('tcamError',10),('ilcAsicDrvError',11),('dppError',12),(_T,13),('sfcDBError',14),('sfcNoSuchFlow',15),('sfcFlowExists',16),('dppNoBuffers',17),('dppNoMemory',18),('dppFlowExists',19)))
class CSFlowFeatureCfgReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('featureCfgFailure',2),('flowVerifFailure',3)))
_CiscoScsiFlowMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoScsiFlowMIBNotifs=_CiscoScsiFlowMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,447,0))
_CiscoScsiFlowMIBObjects_ObjectIdentity=ObjectIdentity
ciscoScsiFlowMIBObjects=_CiscoScsiFlowMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,447,1))
_CsfConfiguration_ObjectIdentity=ObjectIdentity
csfConfiguration=_CsfConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,447,1,1))
class _CiscoScsiFlowNextIndexAvail_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoScsiFlowNextIndexAvail_Type.__name__=_E
_CiscoScsiFlowNextIndexAvail_Object=MibScalar
ciscoScsiFlowNextIndexAvail=_CiscoScsiFlowNextIndexAvail_Object((1,3,6,1,4,1,9,9,447,1,1,1),_CiscoScsiFlowNextIndexAvail_Type())
ciscoScsiFlowNextIndexAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowNextIndexAvail.setStatus(_A)
_CiscoScsiFlowTable_Object=MibTable
ciscoScsiFlowTable=_CiscoScsiFlowTable_Object((1,3,6,1,4,1,9,9,447,1,1,2))
if mibBuilder.loadTexts:ciscoScsiFlowTable.setStatus(_A)
_CiscoScsiFlowEntry_Object=MibTableRow
ciscoScsiFlowEntry=_CiscoScsiFlowEntry_Object((1,3,6,1,4,1,9,9,447,1,1,2,1))
ciscoScsiFlowEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoScsiFlowEntry.setStatus(_A)
class _CiscoScsiFlowId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoScsiFlowId_Type.__name__=_E
_CiscoScsiFlowId_Object=MibTableColumn
ciscoScsiFlowId=_CiscoScsiFlowId_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,1),_CiscoScsiFlowId_Type())
ciscoScsiFlowId.setMaxAccess(_U)
if mibBuilder.loadTexts:ciscoScsiFlowId.setStatus(_A)
_CiscoScsiFlowIntrWwn_Type=FcNameId
_CiscoScsiFlowIntrWwn_Object=MibTableColumn
ciscoScsiFlowIntrWwn=_CiscoScsiFlowIntrWwn_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,2),_CiscoScsiFlowIntrWwn_Type())
ciscoScsiFlowIntrWwn.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowIntrWwn.setStatus(_A)
_CiscoScsiFlowTargetWwn_Type=FcNameId
_CiscoScsiFlowTargetWwn_Object=MibTableColumn
ciscoScsiFlowTargetWwn=_CiscoScsiFlowTargetWwn_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,3),_CiscoScsiFlowTargetWwn_Type())
ciscoScsiFlowTargetWwn.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowTargetWwn.setStatus(_A)
class _CiscoScsiFlowIntrVsan_Type(VsanIndex):defaultValue=1
_CiscoScsiFlowIntrVsan_Type.__name__=_L
_CiscoScsiFlowIntrVsan_Object=MibTableColumn
ciscoScsiFlowIntrVsan=_CiscoScsiFlowIntrVsan_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,4),_CiscoScsiFlowIntrVsan_Type())
ciscoScsiFlowIntrVsan.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowIntrVsan.setStatus(_A)
class _CiscoScsiFlowTargetVsan_Type(VsanIndex):defaultValue=1
_CiscoScsiFlowTargetVsan_Type.__name__=_L
_CiscoScsiFlowTargetVsan_Object=MibTableColumn
ciscoScsiFlowTargetVsan=_CiscoScsiFlowTargetVsan_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,5),_CiscoScsiFlowTargetVsan_Type())
ciscoScsiFlowTargetVsan.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowTargetVsan.setStatus(_A)
class _CiscoScsiFlowAllLuns_Type(TruthValue):defaultValue=1
_CiscoScsiFlowAllLuns_Type.__name__=_I
_CiscoScsiFlowAllLuns_Object=MibTableColumn
ciscoScsiFlowAllLuns=_CiscoScsiFlowAllLuns_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,6),_CiscoScsiFlowAllLuns_Type())
ciscoScsiFlowAllLuns.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowAllLuns.setStatus(_A)
class _CiscoScsiFlowWriteAcc_Type(TruthValue):defaultValue=2
_CiscoScsiFlowWriteAcc_Type.__name__=_I
_CiscoScsiFlowWriteAcc_Object=MibTableColumn
ciscoScsiFlowWriteAcc=_CiscoScsiFlowWriteAcc_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,7),_CiscoScsiFlowWriteAcc_Type())
ciscoScsiFlowWriteAcc.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowWriteAcc.setStatus(_A)
class _CiscoScsiFlowBufCount_Type(Unsigned32):defaultValue=1024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoScsiFlowBufCount_Type.__name__=_E
_CiscoScsiFlowBufCount_Object=MibTableColumn
ciscoScsiFlowBufCount=_CiscoScsiFlowBufCount_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,8),_CiscoScsiFlowBufCount_Type())
ciscoScsiFlowBufCount.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowBufCount.setStatus(_A)
class _CiscoScsiFlowStatsEnabled_Type(TruthValue):defaultValue=2
_CiscoScsiFlowStatsEnabled_Type.__name__=_I
_CiscoScsiFlowStatsEnabled_Object=MibTableColumn
ciscoScsiFlowStatsEnabled=_CiscoScsiFlowStatsEnabled_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,9),_CiscoScsiFlowStatsEnabled_Type())
ciscoScsiFlowStatsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowStatsEnabled.setStatus(_A)
class _CiscoScsiFlowClearStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noop',2)))
_CiscoScsiFlowClearStats_Type.__name__=_O
_CiscoScsiFlowClearStats_Object=MibTableColumn
ciscoScsiFlowClearStats=_CiscoScsiFlowClearStats_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,10),_CiscoScsiFlowClearStats_Type())
ciscoScsiFlowClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowClearStats.setStatus(_A)
_CiscoScsiFlowIntrVrfStatus_Type=CSFlowVerifyReasonCode
_CiscoScsiFlowIntrVrfStatus_Object=MibTableColumn
ciscoScsiFlowIntrVrfStatus=_CiscoScsiFlowIntrVrfStatus_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,11),_CiscoScsiFlowIntrVrfStatus_Type())
ciscoScsiFlowIntrVrfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowIntrVrfStatus.setStatus(_A)
_CiscoScsiFlowTgtVrfStatus_Type=CSFlowVerifyReasonCode
_CiscoScsiFlowTgtVrfStatus_Object=MibTableColumn
ciscoScsiFlowTgtVrfStatus=_CiscoScsiFlowTgtVrfStatus_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,12),_CiscoScsiFlowTgtVrfStatus_Type())
ciscoScsiFlowTgtVrfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowTgtVrfStatus.setStatus(_A)
_CiscoScsiFlowIntrLCStatus_Type=CSFlowVerifyReasonCode
_CiscoScsiFlowIntrLCStatus_Object=MibTableColumn
ciscoScsiFlowIntrLCStatus=_CiscoScsiFlowIntrLCStatus_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,13),_CiscoScsiFlowIntrLCStatus_Type())
ciscoScsiFlowIntrLCStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowIntrLCStatus.setStatus(_A)
_CiscoScsiFlowTgtLCStatus_Type=CSFlowVerifyReasonCode
_CiscoScsiFlowTgtLCStatus_Object=MibTableColumn
ciscoScsiFlowTgtLCStatus=_CiscoScsiFlowTgtLCStatus_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,14),_CiscoScsiFlowTgtLCStatus_Type())
ciscoScsiFlowTgtLCStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowTgtLCStatus.setStatus(_A)
_CiscoScsiFlowRowStatus_Type=RowStatus
_CiscoScsiFlowRowStatus_Object=MibTableColumn
ciscoScsiFlowRowStatus=_CiscoScsiFlowRowStatus_Object((1,3,6,1,4,1,9,9,447,1,1,2,1,15),_CiscoScsiFlowRowStatus_Type())
ciscoScsiFlowRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoScsiFlowRowStatus.setStatus(_A)
class _CiscoScsiFlowNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiscoScsiFlowNum_Type.__name__=_E
_CiscoScsiFlowNum_Object=MibScalar
ciscoScsiFlowNum=_CiscoScsiFlowNum_Object((1,3,6,1,4,1,9,9,447,1,1,3),_CiscoScsiFlowNum_Type())
ciscoScsiFlowNum.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoScsiFlowNum.setStatus(_A)
_CiscoScsiFlowDeviceType_Type=CSFlowDeviceType
_CiscoScsiFlowDeviceType_Object=MibScalar
ciscoScsiFlowDeviceType=_CiscoScsiFlowDeviceType_Object((1,3,6,1,4,1,9,9,447,1,1,4),_CiscoScsiFlowDeviceType_Type())
ciscoScsiFlowDeviceType.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoScsiFlowDeviceType.setStatus(_A)
_CiscoScsiFlowVerifyReasonCode_Type=CSFlowVerifyReasonCode
_CiscoScsiFlowVerifyReasonCode_Object=MibScalar
ciscoScsiFlowVerifyReasonCode=_CiscoScsiFlowVerifyReasonCode_Object((1,3,6,1,4,1,9,9,447,1,1,5),_CiscoScsiFlowVerifyReasonCode_Type())
ciscoScsiFlowVerifyReasonCode.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoScsiFlowVerifyReasonCode.setStatus(_A)
_CiscoScsiFlowCfgReasonCode_Type=CSFlowCfgReasonCode
_CiscoScsiFlowCfgReasonCode_Object=MibScalar
ciscoScsiFlowCfgReasonCode=_CiscoScsiFlowCfgReasonCode_Object((1,3,6,1,4,1,9,9,447,1,1,6),_CiscoScsiFlowCfgReasonCode_Type())
ciscoScsiFlowCfgReasonCode.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoScsiFlowCfgReasonCode.setStatus(_A)
_CsfStats_ObjectIdentity=ObjectIdentity
csfStats=_CsfStats_ObjectIdentity((1,3,6,1,4,1,9,9,447,1,2))
_CiscoScsiFlowStatsTable_Object=MibTable
ciscoScsiFlowStatsTable=_CiscoScsiFlowStatsTable_Object((1,3,6,1,4,1,9,9,447,1,2,1))
if mibBuilder.loadTexts:ciscoScsiFlowStatsTable.setStatus(_A)
_CiscoScsiFlowStatsEntry_Object=MibTableRow
ciscoScsiFlowStatsEntry=_CiscoScsiFlowStatsEntry_Object((1,3,6,1,4,1,9,9,447,1,2,1,1))
ciscoScsiFlowStatsEntry.setIndexNames((0,_B,_F),(0,_B,_V))
if mibBuilder.loadTexts:ciscoScsiFlowStatsEntry.setStatus(_A)
_CiscoScsiFlowLunId_Type=ScsiLUNOrZero
_CiscoScsiFlowLunId_Object=MibTableColumn
ciscoScsiFlowLunId=_CiscoScsiFlowLunId_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,1),_CiscoScsiFlowLunId_Type())
ciscoScsiFlowLunId.setMaxAccess(_U)
if mibBuilder.loadTexts:ciscoScsiFlowLunId.setStatus(_A)
_CiscoScsiFlowRdIos_Type=Counter64
_CiscoScsiFlowRdIos_Object=MibTableColumn
ciscoScsiFlowRdIos=_CiscoScsiFlowRdIos_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,2),_CiscoScsiFlowRdIos_Type())
ciscoScsiFlowRdIos.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdIos.setStatus(_A)
_CiscoScsiFlowRdFailedIos_Type=Counter32
_CiscoScsiFlowRdFailedIos_Object=MibTableColumn
ciscoScsiFlowRdFailedIos=_CiscoScsiFlowRdFailedIos_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,3),_CiscoScsiFlowRdFailedIos_Type())
ciscoScsiFlowRdFailedIos.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdFailedIos.setStatus(_A)
_CiscoScsiFlowRdTimeouts_Type=Counter32
_CiscoScsiFlowRdTimeouts_Object=MibTableColumn
ciscoScsiFlowRdTimeouts=_CiscoScsiFlowRdTimeouts_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,4),_CiscoScsiFlowRdTimeouts_Type())
ciscoScsiFlowRdTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdTimeouts.setStatus(_A)
_CiscoScsiFlowRdBlocks_Type=Counter64
_CiscoScsiFlowRdBlocks_Object=MibTableColumn
ciscoScsiFlowRdBlocks=_CiscoScsiFlowRdBlocks_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,5),_CiscoScsiFlowRdBlocks_Type())
ciscoScsiFlowRdBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdBlocks.setStatus(_A)
_CiscoScsiFlowRdMaxBlocks_Type=Gauge32
_CiscoScsiFlowRdMaxBlocks_Object=MibTableColumn
ciscoScsiFlowRdMaxBlocks=_CiscoScsiFlowRdMaxBlocks_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,6),_CiscoScsiFlowRdMaxBlocks_Type())
ciscoScsiFlowRdMaxBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdMaxBlocks.setStatus(_A)
_CiscoScsiFlowRdMinTime_Type=Gauge32
_CiscoScsiFlowRdMinTime_Object=MibTableColumn
ciscoScsiFlowRdMinTime=_CiscoScsiFlowRdMinTime_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,7),_CiscoScsiFlowRdMinTime_Type())
ciscoScsiFlowRdMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdMinTime.setStatus(_A)
_CiscoScsiFlowRdMaxTime_Type=Gauge32
_CiscoScsiFlowRdMaxTime_Object=MibTableColumn
ciscoScsiFlowRdMaxTime=_CiscoScsiFlowRdMaxTime_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,8),_CiscoScsiFlowRdMaxTime_Type())
ciscoScsiFlowRdMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdMaxTime.setStatus(_A)
_CiscoScsiFlowRdsActive_Type=Gauge32
_CiscoScsiFlowRdsActive_Object=MibTableColumn
ciscoScsiFlowRdsActive=_CiscoScsiFlowRdsActive_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,9),_CiscoScsiFlowRdsActive_Type())
ciscoScsiFlowRdsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdsActive.setStatus(_A)
_CiscoScsiFlowWrIos_Type=Counter64
_CiscoScsiFlowWrIos_Object=MibTableColumn
ciscoScsiFlowWrIos=_CiscoScsiFlowWrIos_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,10),_CiscoScsiFlowWrIos_Type())
ciscoScsiFlowWrIos.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrIos.setStatus(_A)
_CiscoScsiFlowWrFailedIos_Type=Counter32
_CiscoScsiFlowWrFailedIos_Object=MibTableColumn
ciscoScsiFlowWrFailedIos=_CiscoScsiFlowWrFailedIos_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,11),_CiscoScsiFlowWrFailedIos_Type())
ciscoScsiFlowWrFailedIos.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrFailedIos.setStatus(_A)
_CiscoScsiFlowWrTimeouts_Type=Counter32
_CiscoScsiFlowWrTimeouts_Object=MibTableColumn
ciscoScsiFlowWrTimeouts=_CiscoScsiFlowWrTimeouts_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,12),_CiscoScsiFlowWrTimeouts_Type())
ciscoScsiFlowWrTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrTimeouts.setStatus(_A)
_CiscoScsiFlowWrBlocks_Type=Counter64
_CiscoScsiFlowWrBlocks_Object=MibTableColumn
ciscoScsiFlowWrBlocks=_CiscoScsiFlowWrBlocks_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,13),_CiscoScsiFlowWrBlocks_Type())
ciscoScsiFlowWrBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrBlocks.setStatus(_A)
_CiscoScsiFlowWrMaxBlocks_Type=Gauge32
_CiscoScsiFlowWrMaxBlocks_Object=MibTableColumn
ciscoScsiFlowWrMaxBlocks=_CiscoScsiFlowWrMaxBlocks_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,14),_CiscoScsiFlowWrMaxBlocks_Type())
ciscoScsiFlowWrMaxBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrMaxBlocks.setStatus(_A)
_CiscoScsiFlowWrMinTime_Type=Gauge32
_CiscoScsiFlowWrMinTime_Object=MibTableColumn
ciscoScsiFlowWrMinTime=_CiscoScsiFlowWrMinTime_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,15),_CiscoScsiFlowWrMinTime_Type())
ciscoScsiFlowWrMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrMinTime.setStatus(_A)
_CiscoScsiFlowWrMaxTime_Type=Gauge32
_CiscoScsiFlowWrMaxTime_Object=MibTableColumn
ciscoScsiFlowWrMaxTime=_CiscoScsiFlowWrMaxTime_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,16),_CiscoScsiFlowWrMaxTime_Type())
ciscoScsiFlowWrMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrMaxTime.setStatus(_A)
_CiscoScsiFlowWrsActive_Type=Gauge32
_CiscoScsiFlowWrsActive_Object=MibTableColumn
ciscoScsiFlowWrsActive=_CiscoScsiFlowWrsActive_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,17),_CiscoScsiFlowWrsActive_Type())
ciscoScsiFlowWrsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrsActive.setStatus(_A)
_CiscoScsiFlowTestUnitRdys_Type=Counter32
_CiscoScsiFlowTestUnitRdys_Object=MibTableColumn
ciscoScsiFlowTestUnitRdys=_CiscoScsiFlowTestUnitRdys_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,18),_CiscoScsiFlowTestUnitRdys_Type())
ciscoScsiFlowTestUnitRdys.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowTestUnitRdys.setStatus(_A)
_CiscoScsiFlowRepLuns_Type=Counter32
_CiscoScsiFlowRepLuns_Object=MibTableColumn
ciscoScsiFlowRepLuns=_CiscoScsiFlowRepLuns_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,19),_CiscoScsiFlowRepLuns_Type())
ciscoScsiFlowRepLuns.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRepLuns.setStatus(_A)
_CiscoScsiFlowInquirys_Type=Counter32
_CiscoScsiFlowInquirys_Object=MibTableColumn
ciscoScsiFlowInquirys=_CiscoScsiFlowInquirys_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,20),_CiscoScsiFlowInquirys_Type())
ciscoScsiFlowInquirys.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowInquirys.setStatus(_A)
_CiscoScsiFlowRdCapacitys_Type=Counter32
_CiscoScsiFlowRdCapacitys_Object=MibTableColumn
ciscoScsiFlowRdCapacitys=_CiscoScsiFlowRdCapacitys_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,21),_CiscoScsiFlowRdCapacitys_Type())
ciscoScsiFlowRdCapacitys.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRdCapacitys.setStatus(_A)
_CiscoScsiFlowModeSenses_Type=Counter32
_CiscoScsiFlowModeSenses_Object=MibTableColumn
ciscoScsiFlowModeSenses=_CiscoScsiFlowModeSenses_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,22),_CiscoScsiFlowModeSenses_Type())
ciscoScsiFlowModeSenses.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowModeSenses.setStatus(_A)
_CiscoScsiFlowReqSenses_Type=Counter32
_CiscoScsiFlowReqSenses_Object=MibTableColumn
ciscoScsiFlowReqSenses=_CiscoScsiFlowReqSenses_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,23),_CiscoScsiFlowReqSenses_Type())
ciscoScsiFlowReqSenses.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowReqSenses.setStatus(_A)
_CiscoScsiFlowRxFc2Frames_Type=Counter64
_CiscoScsiFlowRxFc2Frames_Object=MibTableColumn
ciscoScsiFlowRxFc2Frames=_CiscoScsiFlowRxFc2Frames_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,24),_CiscoScsiFlowRxFc2Frames_Type())
ciscoScsiFlowRxFc2Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRxFc2Frames.setStatus(_A)
_CiscoScsiFlowTxFc2Frames_Type=Counter64
_CiscoScsiFlowTxFc2Frames_Object=MibTableColumn
ciscoScsiFlowTxFc2Frames=_CiscoScsiFlowTxFc2Frames_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,25),_CiscoScsiFlowTxFc2Frames_Type())
ciscoScsiFlowTxFc2Frames.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowTxFc2Frames.setStatus(_A)
_CiscoScsiFlowRxFc2Octets_Type=Counter64
_CiscoScsiFlowRxFc2Octets_Object=MibTableColumn
ciscoScsiFlowRxFc2Octets=_CiscoScsiFlowRxFc2Octets_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,26),_CiscoScsiFlowRxFc2Octets_Type())
ciscoScsiFlowRxFc2Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowRxFc2Octets.setStatus(_A)
_CiscoScsiFlowTxFc2Octets_Type=Counter64
_CiscoScsiFlowTxFc2Octets_Object=MibTableColumn
ciscoScsiFlowTxFc2Octets=_CiscoScsiFlowTxFc2Octets_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,27),_CiscoScsiFlowTxFc2Octets_Type())
ciscoScsiFlowTxFc2Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowTxFc2Octets.setStatus(_A)
_CiscoScsiFlowBusyStatuses_Type=Counter32
_CiscoScsiFlowBusyStatuses_Object=MibTableColumn
ciscoScsiFlowBusyStatuses=_CiscoScsiFlowBusyStatuses_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,28),_CiscoScsiFlowBusyStatuses_Type())
ciscoScsiFlowBusyStatuses.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowBusyStatuses.setStatus(_A)
_CiscoScsiFlowStatusResvConfs_Type=Counter32
_CiscoScsiFlowStatusResvConfs_Object=MibTableColumn
ciscoScsiFlowStatusResvConfs=_CiscoScsiFlowStatusResvConfs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,29),_CiscoScsiFlowStatusResvConfs_Type())
ciscoScsiFlowStatusResvConfs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowStatusResvConfs.setStatus(_A)
_CiscoScsiFlowTskSetFulStatuses_Type=Counter32
_CiscoScsiFlowTskSetFulStatuses_Object=MibTableColumn
ciscoScsiFlowTskSetFulStatuses=_CiscoScsiFlowTskSetFulStatuses_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,30),_CiscoScsiFlowTskSetFulStatuses_Type())
ciscoScsiFlowTskSetFulStatuses.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowTskSetFulStatuses.setStatus(_A)
_CiscoScsiFlowAcaActiveStatuses_Type=Counter32
_CiscoScsiFlowAcaActiveStatuses_Object=MibTableColumn
ciscoScsiFlowAcaActiveStatuses=_CiscoScsiFlowAcaActiveStatuses_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,31),_CiscoScsiFlowAcaActiveStatuses_Type())
ciscoScsiFlowAcaActiveStatuses.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowAcaActiveStatuses.setStatus(_A)
_CiscoScsiFlowSenseKeyNotRdyErrs_Type=Counter32
_CiscoScsiFlowSenseKeyNotRdyErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyNotRdyErrs=_CiscoScsiFlowSenseKeyNotRdyErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,32),_CiscoScsiFlowSenseKeyNotRdyErrs_Type())
ciscoScsiFlowSenseKeyNotRdyErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyNotRdyErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyMedErrs_Type=Counter32
_CiscoScsiFlowSenseKeyMedErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyMedErrs=_CiscoScsiFlowSenseKeyMedErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,33),_CiscoScsiFlowSenseKeyMedErrs_Type())
ciscoScsiFlowSenseKeyMedErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyMedErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyHwErrs_Type=Counter32
_CiscoScsiFlowSenseKeyHwErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyHwErrs=_CiscoScsiFlowSenseKeyHwErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,34),_CiscoScsiFlowSenseKeyHwErrs_Type())
ciscoScsiFlowSenseKeyHwErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyHwErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyIllReqErrs_Type=Counter32
_CiscoScsiFlowSenseKeyIllReqErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyIllReqErrs=_CiscoScsiFlowSenseKeyIllReqErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,35),_CiscoScsiFlowSenseKeyIllReqErrs_Type())
ciscoScsiFlowSenseKeyIllReqErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyIllReqErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyUnitAttErrs_Type=Counter32
_CiscoScsiFlowSenseKeyUnitAttErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyUnitAttErrs=_CiscoScsiFlowSenseKeyUnitAttErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,36),_CiscoScsiFlowSenseKeyUnitAttErrs_Type())
ciscoScsiFlowSenseKeyUnitAttErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyUnitAttErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyDatProtErrs_Type=Counter32
_CiscoScsiFlowSenseKeyDatProtErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyDatProtErrs=_CiscoScsiFlowSenseKeyDatProtErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,37),_CiscoScsiFlowSenseKeyDatProtErrs_Type())
ciscoScsiFlowSenseKeyDatProtErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyDatProtErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyBlankErrs_Type=Counter32
_CiscoScsiFlowSenseKeyBlankErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyBlankErrs=_CiscoScsiFlowSenseKeyBlankErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,38),_CiscoScsiFlowSenseKeyBlankErrs_Type())
ciscoScsiFlowSenseKeyBlankErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyBlankErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyCpAbrtErrs_Type=Counter32
_CiscoScsiFlowSenseKeyCpAbrtErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyCpAbrtErrs=_CiscoScsiFlowSenseKeyCpAbrtErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,39),_CiscoScsiFlowSenseKeyCpAbrtErrs_Type())
ciscoScsiFlowSenseKeyCpAbrtErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyCpAbrtErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyAbrtCmdErrs_Type=Counter32
_CiscoScsiFlowSenseKeyAbrtCmdErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyAbrtCmdErrs=_CiscoScsiFlowSenseKeyAbrtCmdErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,40),_CiscoScsiFlowSenseKeyAbrtCmdErrs_Type())
ciscoScsiFlowSenseKeyAbrtCmdErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyAbrtCmdErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyVolFlowErrs_Type=Counter32
_CiscoScsiFlowSenseKeyVolFlowErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyVolFlowErrs=_CiscoScsiFlowSenseKeyVolFlowErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,41),_CiscoScsiFlowSenseKeyVolFlowErrs_Type())
ciscoScsiFlowSenseKeyVolFlowErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyVolFlowErrs.setStatus(_A)
_CiscoScsiFlowSenseKeyMiscmpErrs_Type=Counter32
_CiscoScsiFlowSenseKeyMiscmpErrs_Object=MibTableColumn
ciscoScsiFlowSenseKeyMiscmpErrs=_CiscoScsiFlowSenseKeyMiscmpErrs_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,42),_CiscoScsiFlowSenseKeyMiscmpErrs_Type())
ciscoScsiFlowSenseKeyMiscmpErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowSenseKeyMiscmpErrs.setStatus(_A)
_CiscoScsiFlowAbts_Type=Counter32
_CiscoScsiFlowAbts_Object=MibTableColumn
ciscoScsiFlowAbts=_CiscoScsiFlowAbts_Object((1,3,6,1,4,1,9,9,447,1,2,1,1,43),_CiscoScsiFlowAbts_Type())
ciscoScsiFlowAbts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowAbts.setStatus(_A)
_CsfFeatureStatus_ObjectIdentity=ObjectIdentity
csfFeatureStatus=_CsfFeatureStatus_ObjectIdentity((1,3,6,1,4,1,9,9,447,1,3))
_CiscoScsiFlowWrAccStatusTable_Object=MibTable
ciscoScsiFlowWrAccStatusTable=_CiscoScsiFlowWrAccStatusTable_Object((1,3,6,1,4,1,9,9,447,1,3,1))
if mibBuilder.loadTexts:ciscoScsiFlowWrAccStatusTable.setStatus(_A)
_CiscoScsiFlowWrAccStatusEntry_Object=MibTableRow
ciscoScsiFlowWrAccStatusEntry=_CiscoScsiFlowWrAccStatusEntry_Object((1,3,6,1,4,1,9,9,447,1,3,1,1))
ciscoScsiFlowWrAccStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoScsiFlowWrAccStatusEntry.setStatus(_A)
_CiscoScsiFlowWrAccCfgStatus_Type=CSFlowFeatureCfgReasonCode
_CiscoScsiFlowWrAccCfgStatus_Object=MibTableColumn
ciscoScsiFlowWrAccCfgStatus=_CiscoScsiFlowWrAccCfgStatus_Object((1,3,6,1,4,1,9,9,447,1,3,1,1,1),_CiscoScsiFlowWrAccCfgStatus_Type())
ciscoScsiFlowWrAccCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrAccCfgStatus.setStatus(_A)
_CiscoScsiFlowWrAccIntrCfgStatus_Type=CSFlowCfgReasonCode
_CiscoScsiFlowWrAccIntrCfgStatus_Object=MibTableColumn
ciscoScsiFlowWrAccIntrCfgStatus=_CiscoScsiFlowWrAccIntrCfgStatus_Object((1,3,6,1,4,1,9,9,447,1,3,1,1,2),_CiscoScsiFlowWrAccIntrCfgStatus_Type())
ciscoScsiFlowWrAccIntrCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrAccIntrCfgStatus.setStatus(_A)
_CiscoScsiFlowWrAccTgtCfgStatus_Type=CSFlowCfgReasonCode
_CiscoScsiFlowWrAccTgtCfgStatus_Object=MibTableColumn
ciscoScsiFlowWrAccTgtCfgStatus=_CiscoScsiFlowWrAccTgtCfgStatus_Object((1,3,6,1,4,1,9,9,447,1,3,1,1,3),_CiscoScsiFlowWrAccTgtCfgStatus_Type())
ciscoScsiFlowWrAccTgtCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowWrAccTgtCfgStatus.setStatus(_A)
_CiscoScsiFlowStatsStatusTable_Object=MibTable
ciscoScsiFlowStatsStatusTable=_CiscoScsiFlowStatsStatusTable_Object((1,3,6,1,4,1,9,9,447,1,3,2))
if mibBuilder.loadTexts:ciscoScsiFlowStatsStatusTable.setStatus(_A)
_CiscoScsiFlowStatsStatusEntry_Object=MibTableRow
ciscoScsiFlowStatsStatusEntry=_CiscoScsiFlowStatsStatusEntry_Object((1,3,6,1,4,1,9,9,447,1,3,2,1))
ciscoScsiFlowStatsStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoScsiFlowStatsStatusEntry.setStatus(_A)
_CiscoScsiFlowStatsCfgStatus_Type=CSFlowFeatureCfgReasonCode
_CiscoScsiFlowStatsCfgStatus_Object=MibTableColumn
ciscoScsiFlowStatsCfgStatus=_CiscoScsiFlowStatsCfgStatus_Object((1,3,6,1,4,1,9,9,447,1,3,2,1,1),_CiscoScsiFlowStatsCfgStatus_Type())
ciscoScsiFlowStatsCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowStatsCfgStatus.setStatus(_A)
_CiscoScsiFlowStatsIntrCfgStatus_Type=CSFlowCfgReasonCode
_CiscoScsiFlowStatsIntrCfgStatus_Object=MibTableColumn
ciscoScsiFlowStatsIntrCfgStatus=_CiscoScsiFlowStatsIntrCfgStatus_Object((1,3,6,1,4,1,9,9,447,1,3,2,1,2),_CiscoScsiFlowStatsIntrCfgStatus_Type())
ciscoScsiFlowStatsIntrCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowStatsIntrCfgStatus.setStatus(_A)
_CiscoScsiFlowStatsTgtCfgStatus_Type=CSFlowCfgReasonCode
_CiscoScsiFlowStatsTgtCfgStatus_Object=MibTableColumn
ciscoScsiFlowStatsTgtCfgStatus=_CiscoScsiFlowStatsTgtCfgStatus_Object((1,3,6,1,4,1,9,9,447,1,3,2,1,3),_CiscoScsiFlowStatsTgtCfgStatus_Type())
ciscoScsiFlowStatsTgtCfgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiFlowStatsTgtCfgStatus.setStatus(_A)
_CiscoScsiFlowMIBConform_ObjectIdentity=ObjectIdentity
ciscoScsiFlowMIBConform=_CiscoScsiFlowMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,447,2))
_CiscoScsiFlowMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoScsiFlowMIBCompliances=_CiscoScsiFlowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,447,2,1))
_CiscoScsiFlowMIBGroups_ObjectIdentity=ObjectIdentity
ciscoScsiFlowMIBGroups=_CiscoScsiFlowMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,447,2,2))
ciscoScsiFlowGroup=ObjectGroup((1,3,6,1,4,1,9,9,447,2,2,1))
ciscoScsiFlowGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoScsiFlowGroup.setStatus(_A)
ciscoScsiFlowStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,447,2,2,2))
ciscoScsiFlowStatsGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:ciscoScsiFlowStatsGroup.setStatus(_A)
ciscoScsiFlowInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,447,2,2,3))
ciscoScsiFlowInfoGroup.setObjects(*((_B,_G),(_B,_H),(_B,_N),(_B,_K)))
if mibBuilder.loadTexts:ciscoScsiFlowInfoGroup.setStatus(_A)
ciscoScsiFlowFeatureStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,447,2,2,5))
ciscoScsiFlowFeatureStatusGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:ciscoScsiFlowFeatureStatusGroup.setStatus(_A)
ciscoScsiFlowVerifyNotify=NotificationType((1,3,6,1,4,1,9,9,447,0,1))
ciscoScsiFlowVerifyNotify.setObjects(*((_B,_G),(_B,_H),(_B,_N)))
if mibBuilder.loadTexts:ciscoScsiFlowVerifyNotify.setStatus(_A)
ciscoScsiFlowWrAccNotify=NotificationType((1,3,6,1,4,1,9,9,447,0,2))
ciscoScsiFlowWrAccNotify.setObjects(*((_B,_G),(_B,_H),(_B,_K)))
if mibBuilder.loadTexts:ciscoScsiFlowWrAccNotify.setStatus(_A)
ciscoScsiFlowStatsNotify=NotificationType((1,3,6,1,4,1,9,9,447,0,3))
ciscoScsiFlowStatsNotify.setObjects(*((_B,_G),(_B,_H),(_B,_K)))
if mibBuilder.loadTexts:ciscoScsiFlowStatsNotify.setStatus(_A)
ciscoScsiFlowNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,447,2,2,4))
ciscoScsiFlowNotifyGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:ciscoScsiFlowNotifyGroup.setStatus(_A)
ciscoScsiFlowMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,447,2,1,1))
ciscoScsiFlowMIBCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:ciscoScsiFlowMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CSFlowDeviceType':CSFlowDeviceType,'CSFlowVerifyReasonCode':CSFlowVerifyReasonCode,'CSFlowCfgReasonCode':CSFlowCfgReasonCode,'CSFlowFeatureCfgReasonCode':CSFlowFeatureCfgReasonCode,'ciscoScsiFlowMIB':ciscoScsiFlowMIB,'ciscoScsiFlowMIBNotifs':ciscoScsiFlowMIBNotifs,_AX:ciscoScsiFlowVerifyNotify,_AY:ciscoScsiFlowWrAccNotify,_AZ:ciscoScsiFlowStatsNotify,'ciscoScsiFlowMIBObjects':ciscoScsiFlowMIBObjects,'csfConfiguration':csfConfiguration,_W:ciscoScsiFlowNextIndexAvail,'ciscoScsiFlowTable':ciscoScsiFlowTable,'ciscoScsiFlowEntry':ciscoScsiFlowEntry,_F:ciscoScsiFlowId,_X:ciscoScsiFlowIntrWwn,_Y:ciscoScsiFlowTargetWwn,_Z:ciscoScsiFlowIntrVsan,_a:ciscoScsiFlowTargetVsan,_b:ciscoScsiFlowAllLuns,_c:ciscoScsiFlowWriteAcc,_d:ciscoScsiFlowBufCount,_e:ciscoScsiFlowStatsEnabled,_g:ciscoScsiFlowClearStats,_h:ciscoScsiFlowIntrVrfStatus,_k:ciscoScsiFlowTgtVrfStatus,_i:ciscoScsiFlowIntrLCStatus,_j:ciscoScsiFlowTgtLCStatus,_f:ciscoScsiFlowRowStatus,_G:ciscoScsiFlowNum,_H:ciscoScsiFlowDeviceType,_N:ciscoScsiFlowVerifyReasonCode,_K:ciscoScsiFlowCfgReasonCode,'csfStats':csfStats,'ciscoScsiFlowStatsTable':ciscoScsiFlowStatsTable,'ciscoScsiFlowStatsEntry':ciscoScsiFlowStatsEntry,_V:ciscoScsiFlowLunId,_l:ciscoScsiFlowRdIos,_m:ciscoScsiFlowRdFailedIos,_n:ciscoScsiFlowRdTimeouts,_o:ciscoScsiFlowRdBlocks,_p:ciscoScsiFlowRdMaxBlocks,_q:ciscoScsiFlowRdMinTime,_r:ciscoScsiFlowRdMaxTime,_s:ciscoScsiFlowRdsActive,_t:ciscoScsiFlowWrIos,_u:ciscoScsiFlowWrFailedIos,_v:ciscoScsiFlowWrTimeouts,_w:ciscoScsiFlowWrBlocks,_x:ciscoScsiFlowWrMaxBlocks,_y:ciscoScsiFlowWrMinTime,_z:ciscoScsiFlowWrMaxTime,_A0:ciscoScsiFlowWrsActive,_A1:ciscoScsiFlowTestUnitRdys,_A2:ciscoScsiFlowRepLuns,_A3:ciscoScsiFlowInquirys,_A4:ciscoScsiFlowRdCapacitys,_A5:ciscoScsiFlowModeSenses,_A6:ciscoScsiFlowReqSenses,_A7:ciscoScsiFlowRxFc2Frames,_A8:ciscoScsiFlowTxFc2Frames,_A9:ciscoScsiFlowRxFc2Octets,_AA:ciscoScsiFlowTxFc2Octets,_AB:ciscoScsiFlowBusyStatuses,_AC:ciscoScsiFlowStatusResvConfs,_AD:ciscoScsiFlowTskSetFulStatuses,_AE:ciscoScsiFlowAcaActiveStatuses,_AF:ciscoScsiFlowSenseKeyNotRdyErrs,_AG:ciscoScsiFlowSenseKeyMedErrs,_AH:ciscoScsiFlowSenseKeyHwErrs,_AI:ciscoScsiFlowSenseKeyIllReqErrs,_AJ:ciscoScsiFlowSenseKeyUnitAttErrs,_AK:ciscoScsiFlowSenseKeyDatProtErrs,_AL:ciscoScsiFlowSenseKeyBlankErrs,_AM:ciscoScsiFlowSenseKeyCpAbrtErrs,_AN:ciscoScsiFlowSenseKeyAbrtCmdErrs,_AO:ciscoScsiFlowSenseKeyVolFlowErrs,_AP:ciscoScsiFlowSenseKeyMiscmpErrs,_AQ:ciscoScsiFlowAbts,'csfFeatureStatus':csfFeatureStatus,'ciscoScsiFlowWrAccStatusTable':ciscoScsiFlowWrAccStatusTable,'ciscoScsiFlowWrAccStatusEntry':ciscoScsiFlowWrAccStatusEntry,_AR:ciscoScsiFlowWrAccCfgStatus,_AS:ciscoScsiFlowWrAccIntrCfgStatus,_AT:ciscoScsiFlowWrAccTgtCfgStatus,'ciscoScsiFlowStatsStatusTable':ciscoScsiFlowStatsStatusTable,'ciscoScsiFlowStatsStatusEntry':ciscoScsiFlowStatsStatusEntry,_AU:ciscoScsiFlowStatsCfgStatus,_AV:ciscoScsiFlowStatsIntrCfgStatus,_AW:ciscoScsiFlowStatsTgtCfgStatus,'ciscoScsiFlowMIBConform':ciscoScsiFlowMIBConform,'ciscoScsiFlowMIBCompliances':ciscoScsiFlowMIBCompliances,'ciscoScsiFlowMIBCompliance':ciscoScsiFlowMIBCompliance,'ciscoScsiFlowMIBGroups':ciscoScsiFlowMIBGroups,_Aa:ciscoScsiFlowGroup,_Ad:ciscoScsiFlowStatsGroup,_Ac:ciscoScsiFlowInfoGroup,_Ab:ciscoScsiFlowNotifyGroup,_Ae:ciscoScsiFlowFeatureStatusGroup})