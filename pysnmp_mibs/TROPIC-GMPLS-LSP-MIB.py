_An='tnGmplsMoveLspFromGroup'
_Am='tnGmplsMoveLspToGroup'
_Al='tnGmplsLspNextIndexGroup'
_Ak='tnGmplsLspSncpMgmtGroup'
_Aj='tnGmplsLspToPortGroup'
_Ai='tnGmplsLspTransactionGroup'
_Ah='tnGmplsLspExcludeGroup'
_Ag='tnGmplsLspAHopGroup'
_Af='tnGmplsLspCHopGroup'
_Ae='tnGmplsLspFlowGroup'
_Ad='tnGmplsLspGroup'
_Ac='tnGmplsLspObjsGroup'
_Ab='tnGmplsMoveLspFromRowStatus'
_Aa='tnGmplsMoveLspFromCmd'
_AZ='tnGmplsMoveLspFromLinks'
_AY='tnGmplsMoveLspToRowStatus'
_AX='tnGmplsMoveLspToCmd'
_AW='tnGmplsLspNextIndex'
_AV='tnGmplsLspSncpRowStatus'
_AU='tnGmplsLspSncpState'
_AT='tnGmplsLspSncpCmd'
_AS='tnGmplsLspName'
_AR='tnGmplsLspTransactionState'
_AQ='tnGmplsLspTransaction'
_AP='tnGmplsLspExcludeDBLink'
_AO='tnGmplsLspExcludeTELink'
_AN='tnGmplsLspExcludeSubnodeId'
_AM='tnGmplsLspAHopOutResource'
_AL='tnGmplsLspAHopInResource'
_AK='tnGmplsLspAHopSubnodeId'
_AJ='tnGmplsLspCHopOutResource'
_AI='tnGmplsLspCHopInResource'
_AH='tnGmplsLspCHopSubnodeId'
_AG='tnGmplsLspFlowId'
_AF='tnGmplsLspFlowState'
_AE='tnGmplsLspLatencyViolation'
_AD='tnGmplsLspQoSViolation'
_AC='tnGmplsLspOptFsbltyViolation'
_AB='tnGmplsLspColorViolation'
_AA='tnGmplsLspSRGViolation'
_A9='tnGmplsLspReversionState'
_A8='tnGmplsLspProtectionStateSpare'
_A7='tnGmplsLspProtectionStateMain'
_A6='tnGmplsLspActions'
_A5='tnGmplsLspMaxHopsConstraint'
_A4='tnGmplsLspLatencyThreshold'
_A3='tnGmplsLspDiversityLspList'
_A2='tnGmplsLspAdminStatus'
_A1='tnGmplsLspConnectionType'
_A0='tnGmplsLspExcludeAnyAffinity'
_z='tnGmplsLspIncludeAnyAffinity'
_y='tnGmplsLspReversionMode'
_x='tnGmplsLspProtectionType'
_w='tnGmplsLspTrafficType'
_v='tnGmplsLspDirectionType'
_u='tnGmplsLspHoldingPrio'
_t='tnGmplsLspSetupPrio'
_s='tnGmplsLspDestLsrId'
_r='tnGmplsLspEgressResource'
_q='tnGmplsLspIngressResource'
_p='tnGmplsLspDescr'
_o='tnGmplsLspAttributeTotal'
_n='tnGmplsMoveLspFromSrcLspId'
_m='tnGmplsMoveLspToSrcLspId'
_l='tnGmplsLspNextIndexTableIndex'
_k='tnGmplsLspSncpDirection'
_j='tnGmplsLspSncpCtpResource'
_i='tnGmplsLspSrcLsrId'
_h='tnGmplsLspLTPSrcLspId'
_g='tnGmplsLspDBLinkIfId'
_f='commit'
_e='tnGmplsLspTransactionSrcLspId'
_d='tnGmplsLspExcludeIndex'
_c='tnGmplsLspExcludeSrcLspId'
_b='tnGmplsLspAHopIndex'
_a='tnGmplsLspAHopRouteType'
_Z='tnGmplsLspAHopSrcLspId'
_Y='tnGmplsLspCHopIndex'
_X='tnGmplsLspCHopRouteType'
_W='tnGmplsLspCHopSrcLspId'
_V='backupSpare'
_U='tnGmplsLspFlowType'
_T='tnGmplsLspFlowSrcLspId'
_S='moveToSpareBackup'
_R='moveToMainBackup'
_Q='moveToInactiveBackup'
_P='moveToSpareNominal'
_O='moveToMainNominal'
_N='tnGmplsLspSrcLspId'
_M='OctetString'
_L='backupInactive'
_K='spare'
_J='main'
_I='none'
_H='na'
_G='Unsigned32'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='TROPIC-GMPLS-LSP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
tnGmplsMIBModules,tnGmplsObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnGmplsMIBModules','tnGmplsObjs')
tnGmplsLspMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,6,3))
if mibBuilder.loadTexts:tnGmplsLspMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2013-08-29 00:00'))
class AluWdmGmplsLspProtectionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('undefined',1),('normal',2),('failed',3),('noBackup',4),('restored',5),('restoredNoBackup',6),('apeInProgress',7),('failedButConnected',8),('restoring',9),('failedNoReroutePossible',10),('prepareSoftReroute',11),('softReroutingInProgress',12)))
_TnGmplsLspMIB_ObjectIdentity=ObjectIdentity
tnGmplsLspMIB=_TnGmplsLspMIB_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,3))
_TnGmplsLspObjs_ObjectIdentity=ObjectIdentity
tnGmplsLspObjs=_TnGmplsLspObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,3,1))
_TnGmplsLspAttributeTotal_Type=Integer32
_TnGmplsLspAttributeTotal_Object=MibScalar
tnGmplsLspAttributeTotal=_TnGmplsLspAttributeTotal_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,1),_TnGmplsLspAttributeTotal_Type())
tnGmplsLspAttributeTotal.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspAttributeTotal.setStatus(_A)
_TnGmplsLspTable_Object=MibTable
tnGmplsLspTable=_TnGmplsLspTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2))
if mibBuilder.loadTexts:tnGmplsLspTable.setStatus(_A)
_TnGmplsLspEntry_Object=MibTableRow
tnGmplsLspEntry=_TnGmplsLspEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1))
tnGmplsLspEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:tnGmplsLspEntry.setStatus(_A)
_TnGmplsLspSrcLspId_Type=Unsigned32
_TnGmplsLspSrcLspId_Object=MibTableColumn
tnGmplsLspSrcLspId=_TnGmplsLspSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,1),_TnGmplsLspSrcLspId_Type())
tnGmplsLspSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspSrcLspId.setStatus(_A)
_TnGmplsLspDescr_Type=DisplayString
_TnGmplsLspDescr_Object=MibTableColumn
tnGmplsLspDescr=_TnGmplsLspDescr_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,2),_TnGmplsLspDescr_Type())
tnGmplsLspDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspDescr.setStatus(_A)
_TnGmplsLspIngressResource_Type=DisplayString
_TnGmplsLspIngressResource_Object=MibTableColumn
tnGmplsLspIngressResource=_TnGmplsLspIngressResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,3),_TnGmplsLspIngressResource_Type())
tnGmplsLspIngressResource.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspIngressResource.setStatus(_A)
_TnGmplsLspEgressResource_Type=DisplayString
_TnGmplsLspEgressResource_Object=MibTableColumn
tnGmplsLspEgressResource=_TnGmplsLspEgressResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,4),_TnGmplsLspEgressResource_Type())
tnGmplsLspEgressResource.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspEgressResource.setStatus(_A)
_TnGmplsLspDestLsrId_Type=Unsigned32
_TnGmplsLspDestLsrId_Object=MibTableColumn
tnGmplsLspDestLsrId=_TnGmplsLspDestLsrId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,5),_TnGmplsLspDestLsrId_Type())
tnGmplsLspDestLsrId.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspDestLsrId.setStatus(_A)
class _TnGmplsLspSetupPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TnGmplsLspSetupPrio_Type.__name__=_D
_TnGmplsLspSetupPrio_Object=MibTableColumn
tnGmplsLspSetupPrio=_TnGmplsLspSetupPrio_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,6),_TnGmplsLspSetupPrio_Type())
tnGmplsLspSetupPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspSetupPrio.setStatus(_A)
class _TnGmplsLspHoldingPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TnGmplsLspHoldingPrio_Type.__name__=_D
_TnGmplsLspHoldingPrio_Object=MibTableColumn
tnGmplsLspHoldingPrio=_TnGmplsLspHoldingPrio_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,7),_TnGmplsLspHoldingPrio_Type())
tnGmplsLspHoldingPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspHoldingPrio.setStatus(_A)
class _TnGmplsLspDirectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('bidirectional',1))
_TnGmplsLspDirectionType_Type.__name__=_D
_TnGmplsLspDirectionType_Object=MibTableColumn
tnGmplsLspDirectionType=_TnGmplsLspDirectionType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,8),_TnGmplsLspDirectionType_Type())
tnGmplsLspDirectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspDirectionType.setStatus(_A)
class _TnGmplsLspTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('och',8))
_TnGmplsLspTrafficType_Type.__name__=_D
_TnGmplsLspTrafficType_Object=MibTableColumn
tnGmplsLspTrafficType=_TnGmplsLspTrafficType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,9),_TnGmplsLspTrafficType_Type())
tnGmplsLspTrafficType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspTrafficType.setStatus(_A)
class _TnGmplsLspProtectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,6,7)));namedValues=NamedValues(*(('unprotected',1),('sbr',2),('guaranteed',3),('osncp',6),('oprc',7)))
_TnGmplsLspProtectionType_Type.__name__=_D
_TnGmplsLspProtectionType_Object=MibTableColumn
tnGmplsLspProtectionType=_TnGmplsLspProtectionType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,10),_TnGmplsLspProtectionType_Type())
tnGmplsLspProtectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspProtectionType.setStatus(_A)
class _TnGmplsLspReversionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_TnGmplsLspReversionMode_Type.__name__=_D
_TnGmplsLspReversionMode_Object=MibTableColumn
tnGmplsLspReversionMode=_TnGmplsLspReversionMode_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,11),_TnGmplsLspReversionMode_Type())
tnGmplsLspReversionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspReversionMode.setStatus(_A)
class _TnGmplsLspIncludeAnyAffinity_Type(Unsigned32):defaultValue=0
_TnGmplsLspIncludeAnyAffinity_Type.__name__=_G
_TnGmplsLspIncludeAnyAffinity_Object=MibTableColumn
tnGmplsLspIncludeAnyAffinity=_TnGmplsLspIncludeAnyAffinity_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,12),_TnGmplsLspIncludeAnyAffinity_Type())
tnGmplsLspIncludeAnyAffinity.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspIncludeAnyAffinity.setStatus(_A)
class _TnGmplsLspExcludeAnyAffinity_Type(Unsigned32):defaultValue=0
_TnGmplsLspExcludeAnyAffinity_Type.__name__=_G
_TnGmplsLspExcludeAnyAffinity_Object=MibTableColumn
tnGmplsLspExcludeAnyAffinity=_TnGmplsLspExcludeAnyAffinity_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,13),_TnGmplsLspExcludeAnyAffinity_Type())
tnGmplsLspExcludeAnyAffinity.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspExcludeAnyAffinity.setStatus(_A)
class _TnGmplsLspConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('spc',1))
_TnGmplsLspConnectionType_Type.__name__=_D
_TnGmplsLspConnectionType_Object=MibTableColumn
tnGmplsLspConnectionType=_TnGmplsLspConnectionType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,14),_TnGmplsLspConnectionType_Type())
tnGmplsLspConnectionType.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspConnectionType.setStatus(_A)
class _TnGmplsLspAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_TnGmplsLspAdminStatus_Type.__name__=_D
_TnGmplsLspAdminStatus_Object=MibTableColumn
tnGmplsLspAdminStatus=_TnGmplsLspAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,15),_TnGmplsLspAdminStatus_Type())
tnGmplsLspAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspAdminStatus.setStatus(_A)
_TnGmplsLspDiversityLspList_Type=DisplayString
_TnGmplsLspDiversityLspList_Object=MibTableColumn
tnGmplsLspDiversityLspList=_TnGmplsLspDiversityLspList_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,16),_TnGmplsLspDiversityLspList_Type())
tnGmplsLspDiversityLspList.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspDiversityLspList.setStatus(_A)
class _TnGmplsLspLatencyThreshold_Type(Unsigned32):defaultValue=0
_TnGmplsLspLatencyThreshold_Type.__name__=_G
_TnGmplsLspLatencyThreshold_Object=MibTableColumn
tnGmplsLspLatencyThreshold=_TnGmplsLspLatencyThreshold_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,17),_TnGmplsLspLatencyThreshold_Type())
tnGmplsLspLatencyThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspLatencyThreshold.setStatus(_A)
class _TnGmplsLspMaxHopsConstraint_Type(Unsigned32):defaultValue=0
_TnGmplsLspMaxHopsConstraint_Type.__name__=_G
_TnGmplsLspMaxHopsConstraint_Object=MibTableColumn
tnGmplsLspMaxHopsConstraint=_TnGmplsLspMaxHopsConstraint_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,18),_TnGmplsLspMaxHopsConstraint_Type())
tnGmplsLspMaxHopsConstraint.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspMaxHopsConstraint.setStatus(_A)
class _TnGmplsLspActions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_TnGmplsLspActions_Type.__name__=_D
_TnGmplsLspActions_Object=MibTableColumn
tnGmplsLspActions=_TnGmplsLspActions_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,19),_TnGmplsLspActions_Type())
tnGmplsLspActions.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspActions.setStatus(_A)
_TnGmplsLspProtectionStateMain_Type=AluWdmGmplsLspProtectionState
_TnGmplsLspProtectionStateMain_Object=MibTableColumn
tnGmplsLspProtectionStateMain=_TnGmplsLspProtectionStateMain_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,20),_TnGmplsLspProtectionStateMain_Type())
tnGmplsLspProtectionStateMain.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspProtectionStateMain.setStatus(_A)
_TnGmplsLspProtectionStateSpare_Type=AluWdmGmplsLspProtectionState
_TnGmplsLspProtectionStateSpare_Object=MibTableColumn
tnGmplsLspProtectionStateSpare=_TnGmplsLspProtectionStateSpare_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,21),_TnGmplsLspProtectionStateSpare_Type())
tnGmplsLspProtectionStateSpare.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspProtectionStateSpare.setStatus(_A)
class _TnGmplsLspReversionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*(('nA',1),('rTR',2),('notRTR',3),('revBlocked',4),('revPreempt',5),('mainNASpareNA',6),('mainNASpareRTR',7),('mainNASpareNotRTR',8),('mainNASpareRevBlocked',9),('mainNASpareRevPreempt',10),('mainRTRSpareNA',11),('mainRTRSpareRTR',12),('mainRTRSpareNotRTR',13),('mainRTRSpareRevBlocked',14),('mainRTRSpareRevPreempt',15),('mainNotRTRSpareNA',16),('mainNotRTRSpareRTR',17),('mainNotRTRSpareNotRTR',18),('mainNotRTRSpareRevBlocked',19),('mainNotRTRSpareRevPreempt',20),('mainRevBlockedSpareNA',21),('mainRevBlockedSpareRTR',22),('mainRevBlockedSpareNotRTR',23),('mainRevBlockedSpareRevBlocked',24),('mainRevBlockedSpareRevPreempt',25),('mainRevPreemptSpareNA',26),('mainRevPreemptSpareRTR',27),('mainRevPreemptSpareNotRTR',28),('mainRevPreemptSpareRevBlocked',29),('mainRevPreemptSpareRevPreempt',30)))
_TnGmplsLspReversionState_Type.__name__=_D
_TnGmplsLspReversionState_Object=MibTableColumn
tnGmplsLspReversionState=_TnGmplsLspReversionState_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,22),_TnGmplsLspReversionState_Type())
tnGmplsLspReversionState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspReversionState.setStatus(_A)
_TnGmplsLspSRGViolation_Type=TruthValue
_TnGmplsLspSRGViolation_Object=MibTableColumn
tnGmplsLspSRGViolation=_TnGmplsLspSRGViolation_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,23),_TnGmplsLspSRGViolation_Type())
tnGmplsLspSRGViolation.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspSRGViolation.setStatus(_A)
_TnGmplsLspColorViolation_Type=TruthValue
_TnGmplsLspColorViolation_Object=MibTableColumn
tnGmplsLspColorViolation=_TnGmplsLspColorViolation_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,24),_TnGmplsLspColorViolation_Type())
tnGmplsLspColorViolation.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspColorViolation.setStatus(_A)
_TnGmplsLspOptFsbltyViolation_Type=TruthValue
_TnGmplsLspOptFsbltyViolation_Object=MibTableColumn
tnGmplsLspOptFsbltyViolation=_TnGmplsLspOptFsbltyViolation_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,25),_TnGmplsLspOptFsbltyViolation_Type())
tnGmplsLspOptFsbltyViolation.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspOptFsbltyViolation.setStatus(_A)
_TnGmplsLspQoSViolation_Type=TruthValue
_TnGmplsLspQoSViolation_Object=MibTableColumn
tnGmplsLspQoSViolation=_TnGmplsLspQoSViolation_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,26),_TnGmplsLspQoSViolation_Type())
tnGmplsLspQoSViolation.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspQoSViolation.setStatus(_A)
_TnGmplsLspLatencyViolation_Type=TruthValue
_TnGmplsLspLatencyViolation_Object=MibTableColumn
tnGmplsLspLatencyViolation=_TnGmplsLspLatencyViolation_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,2,1,27),_TnGmplsLspLatencyViolation_Type())
tnGmplsLspLatencyViolation.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspLatencyViolation.setStatus(_A)
_TnGmplsLspFlowTable_Object=MibTable
tnGmplsLspFlowTable=_TnGmplsLspFlowTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,3))
if mibBuilder.loadTexts:tnGmplsLspFlowTable.setStatus(_A)
_TnGmplsLspFlowEntry_Object=MibTableRow
tnGmplsLspFlowEntry=_TnGmplsLspFlowEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,3,1))
tnGmplsLspFlowEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:tnGmplsLspFlowEntry.setStatus(_A)
_TnGmplsLspFlowSrcLspId_Type=Unsigned32
_TnGmplsLspFlowSrcLspId_Object=MibTableColumn
tnGmplsLspFlowSrcLspId=_TnGmplsLspFlowSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,3,1,1),_TnGmplsLspFlowSrcLspId_Type())
tnGmplsLspFlowSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspFlowSrcLspId.setStatus(_A)
class _TnGmplsLspFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),('backupMain',3),(_V,4),(_L,5)))
_TnGmplsLspFlowType_Type.__name__=_D
_TnGmplsLspFlowType_Object=MibTableColumn
tnGmplsLspFlowType=_TnGmplsLspFlowType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,3,1,2),_TnGmplsLspFlowType_Type())
tnGmplsLspFlowType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspFlowType.setStatus(_A)
class _TnGmplsLspFlowState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('undef',1),('up',2),('down',3),('degraded',4)))
_TnGmplsLspFlowState_Type.__name__=_D
_TnGmplsLspFlowState_Object=MibTableColumn
tnGmplsLspFlowState=_TnGmplsLspFlowState_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,3,1,3),_TnGmplsLspFlowState_Type())
tnGmplsLspFlowState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspFlowState.setStatus(_A)
_TnGmplsLspFlowId_Type=Unsigned32
_TnGmplsLspFlowId_Object=MibTableColumn
tnGmplsLspFlowId=_TnGmplsLspFlowId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,3,1,4),_TnGmplsLspFlowId_Type())
tnGmplsLspFlowId.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspFlowId.setStatus(_A)
_TnGmplsLspCHopTable_Object=MibTable
tnGmplsLspCHopTable=_TnGmplsLspCHopTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4))
if mibBuilder.loadTexts:tnGmplsLspCHopTable.setStatus(_A)
_TnGmplsLspCHopEntry_Object=MibTableRow
tnGmplsLspCHopEntry=_TnGmplsLspCHopEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1))
tnGmplsLspCHopEntry.setIndexNames((0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:tnGmplsLspCHopEntry.setStatus(_A)
_TnGmplsLspCHopSrcLspId_Type=Unsigned32
_TnGmplsLspCHopSrcLspId_Object=MibTableColumn
tnGmplsLspCHopSrcLspId=_TnGmplsLspCHopSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1,1),_TnGmplsLspCHopSrcLspId_Type())
tnGmplsLspCHopSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspCHopSrcLspId.setStatus(_A)
class _TnGmplsLspCHopRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),('backup',3),(_V,4),(_L,5)))
_TnGmplsLspCHopRouteType_Type.__name__=_D
_TnGmplsLspCHopRouteType_Object=MibTableColumn
tnGmplsLspCHopRouteType=_TnGmplsLspCHopRouteType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1,2),_TnGmplsLspCHopRouteType_Type())
tnGmplsLspCHopRouteType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspCHopRouteType.setStatus(_A)
_TnGmplsLspCHopIndex_Type=Unsigned32
_TnGmplsLspCHopIndex_Object=MibTableColumn
tnGmplsLspCHopIndex=_TnGmplsLspCHopIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1,3),_TnGmplsLspCHopIndex_Type())
tnGmplsLspCHopIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspCHopIndex.setStatus(_A)
_TnGmplsLspCHopSubnodeId_Type=Unsigned32
_TnGmplsLspCHopSubnodeId_Object=MibTableColumn
tnGmplsLspCHopSubnodeId=_TnGmplsLspCHopSubnodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1,4),_TnGmplsLspCHopSubnodeId_Type())
tnGmplsLspCHopSubnodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspCHopSubnodeId.setStatus(_A)
_TnGmplsLspCHopInResource_Type=DisplayString
_TnGmplsLspCHopInResource_Object=MibTableColumn
tnGmplsLspCHopInResource=_TnGmplsLspCHopInResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1,5),_TnGmplsLspCHopInResource_Type())
tnGmplsLspCHopInResource.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspCHopInResource.setStatus(_A)
_TnGmplsLspCHopOutResource_Type=DisplayString
_TnGmplsLspCHopOutResource_Object=MibTableColumn
tnGmplsLspCHopOutResource=_TnGmplsLspCHopOutResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,4,1,6),_TnGmplsLspCHopOutResource_Type())
tnGmplsLspCHopOutResource.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspCHopOutResource.setStatus(_A)
_TnGmplsLspAHopTable_Object=MibTable
tnGmplsLspAHopTable=_TnGmplsLspAHopTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5))
if mibBuilder.loadTexts:tnGmplsLspAHopTable.setStatus(_A)
_TnGmplsLspAHopEntry_Object=MibTableRow
tnGmplsLspAHopEntry=_TnGmplsLspAHopEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1))
tnGmplsLspAHopEntry.setIndexNames((0,_B,_Z),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:tnGmplsLspAHopEntry.setStatus(_A)
_TnGmplsLspAHopSrcLspId_Type=Unsigned32
_TnGmplsLspAHopSrcLspId_Object=MibTableColumn
tnGmplsLspAHopSrcLspId=_TnGmplsLspAHopSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1,1),_TnGmplsLspAHopSrcLspId_Type())
tnGmplsLspAHopSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspAHopSrcLspId.setStatus(_A)
class _TnGmplsLspAHopRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,5)))
_TnGmplsLspAHopRouteType_Type.__name__=_D
_TnGmplsLspAHopRouteType_Object=MibTableColumn
tnGmplsLspAHopRouteType=_TnGmplsLspAHopRouteType_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1,2),_TnGmplsLspAHopRouteType_Type())
tnGmplsLspAHopRouteType.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspAHopRouteType.setStatus(_A)
_TnGmplsLspAHopIndex_Type=Unsigned32
_TnGmplsLspAHopIndex_Object=MibTableColumn
tnGmplsLspAHopIndex=_TnGmplsLspAHopIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1,3),_TnGmplsLspAHopIndex_Type())
tnGmplsLspAHopIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspAHopIndex.setStatus(_A)
_TnGmplsLspAHopSubnodeId_Type=Unsigned32
_TnGmplsLspAHopSubnodeId_Object=MibTableColumn
tnGmplsLspAHopSubnodeId=_TnGmplsLspAHopSubnodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1,4),_TnGmplsLspAHopSubnodeId_Type())
tnGmplsLspAHopSubnodeId.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspAHopSubnodeId.setStatus(_A)
_TnGmplsLspAHopInResource_Type=DisplayString
_TnGmplsLspAHopInResource_Object=MibTableColumn
tnGmplsLspAHopInResource=_TnGmplsLspAHopInResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1,5),_TnGmplsLspAHopInResource_Type())
tnGmplsLspAHopInResource.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspAHopInResource.setStatus(_A)
_TnGmplsLspAHopOutResource_Type=DisplayString
_TnGmplsLspAHopOutResource_Object=MibTableColumn
tnGmplsLspAHopOutResource=_TnGmplsLspAHopOutResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,5,1,6),_TnGmplsLspAHopOutResource_Type())
tnGmplsLspAHopOutResource.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspAHopOutResource.setStatus(_A)
_TnGmplsLspExcludeTable_Object=MibTable
tnGmplsLspExcludeTable=_TnGmplsLspExcludeTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6))
if mibBuilder.loadTexts:tnGmplsLspExcludeTable.setStatus(_A)
_TnGmplsLspExcludeEntry_Object=MibTableRow
tnGmplsLspExcludeEntry=_TnGmplsLspExcludeEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6,1))
tnGmplsLspExcludeEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:tnGmplsLspExcludeEntry.setStatus(_A)
_TnGmplsLspExcludeSrcLspId_Type=Unsigned32
_TnGmplsLspExcludeSrcLspId_Object=MibTableColumn
tnGmplsLspExcludeSrcLspId=_TnGmplsLspExcludeSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6,1,1),_TnGmplsLspExcludeSrcLspId_Type())
tnGmplsLspExcludeSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspExcludeSrcLspId.setStatus(_A)
_TnGmplsLspExcludeIndex_Type=Unsigned32
_TnGmplsLspExcludeIndex_Object=MibTableColumn
tnGmplsLspExcludeIndex=_TnGmplsLspExcludeIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6,1,2),_TnGmplsLspExcludeIndex_Type())
tnGmplsLspExcludeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspExcludeIndex.setStatus(_A)
_TnGmplsLspExcludeSubnodeId_Type=Unsigned32
_TnGmplsLspExcludeSubnodeId_Object=MibTableColumn
tnGmplsLspExcludeSubnodeId=_TnGmplsLspExcludeSubnodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6,1,3),_TnGmplsLspExcludeSubnodeId_Type())
tnGmplsLspExcludeSubnodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspExcludeSubnodeId.setStatus(_A)
_TnGmplsLspExcludeTELink_Type=Unsigned32
_TnGmplsLspExcludeTELink_Object=MibTableColumn
tnGmplsLspExcludeTELink=_TnGmplsLspExcludeTELink_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6,1,4),_TnGmplsLspExcludeTELink_Type())
tnGmplsLspExcludeTELink.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspExcludeTELink.setStatus(_A)
_TnGmplsLspExcludeDBLink_Type=Unsigned32
_TnGmplsLspExcludeDBLink_Object=MibTableColumn
tnGmplsLspExcludeDBLink=_TnGmplsLspExcludeDBLink_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,6,1,5),_TnGmplsLspExcludeDBLink_Type())
tnGmplsLspExcludeDBLink.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspExcludeDBLink.setStatus(_A)
_TnGmplsLspTransactionTable_Object=MibTable
tnGmplsLspTransactionTable=_TnGmplsLspTransactionTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,7))
if mibBuilder.loadTexts:tnGmplsLspTransactionTable.setStatus(_A)
_TnGmplsLspTransactionEntry_Object=MibTableRow
tnGmplsLspTransactionEntry=_TnGmplsLspTransactionEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,7,1))
tnGmplsLspTransactionEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:tnGmplsLspTransactionEntry.setStatus(_A)
_TnGmplsLspTransactionSrcLspId_Type=Unsigned32
_TnGmplsLspTransactionSrcLspId_Object=MibTableColumn
tnGmplsLspTransactionSrcLspId=_TnGmplsLspTransactionSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,7,1,1),_TnGmplsLspTransactionSrcLspId_Type())
tnGmplsLspTransactionSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspTransactionSrcLspId.setStatus(_A)
class _TnGmplsLspTransaction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_f,2),('rollback',3),('delete',4)))
_TnGmplsLspTransaction_Type.__name__=_D
_TnGmplsLspTransaction_Object=MibTableColumn
tnGmplsLspTransaction=_TnGmplsLspTransaction_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,7,1,2),_TnGmplsLspTransaction_Type())
tnGmplsLspTransaction.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspTransaction.setStatus(_A)
class _TnGmplsLspTransactionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_f,2),('pending',3)))
_TnGmplsLspTransactionState_Type.__name__=_D
_TnGmplsLspTransactionState_Object=MibTableColumn
tnGmplsLspTransactionState=_TnGmplsLspTransactionState_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,7,1,3),_TnGmplsLspTransactionState_Type())
tnGmplsLspTransactionState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspTransactionState.setStatus(_A)
_TnGmplsLspToPortTable_Object=MibTable
tnGmplsLspToPortTable=_TnGmplsLspToPortTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,8))
if mibBuilder.loadTexts:tnGmplsLspToPortTable.setStatus(_A)
_TnGmplsLspToPortEntry_Object=MibTableRow
tnGmplsLspToPortEntry=_TnGmplsLspToPortEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,8,1))
tnGmplsLspToPortEntry.setIndexNames((0,_B,_g),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:tnGmplsLspToPortEntry.setStatus(_A)
_TnGmplsLspDBLinkIfId_Type=Unsigned32
_TnGmplsLspDBLinkIfId_Object=MibTableColumn
tnGmplsLspDBLinkIfId=_TnGmplsLspDBLinkIfId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,8,1,1),_TnGmplsLspDBLinkIfId_Type())
tnGmplsLspDBLinkIfId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspDBLinkIfId.setStatus(_A)
_TnGmplsLspLTPSrcLspId_Type=Unsigned32
_TnGmplsLspLTPSrcLspId_Object=MibTableColumn
tnGmplsLspLTPSrcLspId=_TnGmplsLspLTPSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,8,1,2),_TnGmplsLspLTPSrcLspId_Type())
tnGmplsLspLTPSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspLTPSrcLspId.setStatus(_A)
_TnGmplsLspSrcLsrId_Type=Unsigned32
_TnGmplsLspSrcLsrId_Object=MibTableColumn
tnGmplsLspSrcLsrId=_TnGmplsLspSrcLsrId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,8,1,3),_TnGmplsLspSrcLsrId_Type())
tnGmplsLspSrcLsrId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspSrcLsrId.setStatus(_A)
_TnGmplsLspName_Type=DisplayString
_TnGmplsLspName_Object=MibTableColumn
tnGmplsLspName=_TnGmplsLspName_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,8,1,4),_TnGmplsLspName_Type())
tnGmplsLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspName.setStatus(_A)
_TnGmplsLspSncpMgmtTable_Object=MibTable
tnGmplsLspSncpMgmtTable=_TnGmplsLspSncpMgmtTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9))
if mibBuilder.loadTexts:tnGmplsLspSncpMgmtTable.setStatus(_A)
_TnGmplsLspSncpMgmtEntry_Object=MibTableRow
tnGmplsLspSncpMgmtEntry=_TnGmplsLspSncpMgmtEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9,1))
tnGmplsLspSncpMgmtEntry.setIndexNames((0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:tnGmplsLspSncpMgmtEntry.setStatus(_A)
class _TnGmplsLspSncpCtpResource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_TnGmplsLspSncpCtpResource_Type.__name__=_M
_TnGmplsLspSncpCtpResource_Object=MibTableColumn
tnGmplsLspSncpCtpResource=_TnGmplsLspSncpCtpResource_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9,1,1),_TnGmplsLspSncpCtpResource_Type())
tnGmplsLspSncpCtpResource.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspSncpCtpResource.setStatus(_A)
class _TnGmplsLspSncpDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('internal',2)))
_TnGmplsLspSncpDirection_Type.__name__=_D
_TnGmplsLspSncpDirection_Object=MibTableColumn
tnGmplsLspSncpDirection=_TnGmplsLspSncpDirection_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9,1,2),_TnGmplsLspSncpDirection_Type())
tnGmplsLspSncpDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspSncpDirection.setStatus(_A)
class _TnGmplsLspSncpCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('manualMain',2),('manualSpare',3),('forceMain',4),('forceSpare',5),('release',6)))
_TnGmplsLspSncpCmd_Type.__name__=_D
_TnGmplsLspSncpCmd_Object=MibTableColumn
tnGmplsLspSncpCmd=_TnGmplsLspSncpCmd_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9,1,3),_TnGmplsLspSncpCmd_Type())
tnGmplsLspSncpCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspSncpCmd.setStatus(_A)
class _TnGmplsLspSncpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),('mainSelected',2),('spareSelected',3),('mainSelectedSpareFailed',4),('spareSelectedMainFailed',5),('bothFailed',6),('nonUniform',7),('unknown',8)))
_TnGmplsLspSncpState_Type.__name__=_D
_TnGmplsLspSncpState_Object=MibTableColumn
tnGmplsLspSncpState=_TnGmplsLspSncpState_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9,1,4),_TnGmplsLspSncpState_Type())
tnGmplsLspSncpState.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspSncpState.setStatus(_A)
_TnGmplsLspSncpRowStatus_Type=RowStatus
_TnGmplsLspSncpRowStatus_Object=MibTableColumn
tnGmplsLspSncpRowStatus=_TnGmplsLspSncpRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,9,1,5),_TnGmplsLspSncpRowStatus_Type())
tnGmplsLspSncpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsLspSncpRowStatus.setStatus(_A)
_TnGmplsLspNextIndexTable_Object=MibTable
tnGmplsLspNextIndexTable=_TnGmplsLspNextIndexTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,10))
if mibBuilder.loadTexts:tnGmplsLspNextIndexTable.setStatus(_A)
_TnGmplsLspNextIndexEntry_Object=MibTableRow
tnGmplsLspNextIndexEntry=_TnGmplsLspNextIndexEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,10,1))
tnGmplsLspNextIndexEntry.setIndexNames((0,_B,_l))
if mibBuilder.loadTexts:tnGmplsLspNextIndexEntry.setStatus(_A)
_TnGmplsLspNextIndexTableIndex_Type=Unsigned32
_TnGmplsLspNextIndexTableIndex_Object=MibTableColumn
tnGmplsLspNextIndexTableIndex=_TnGmplsLspNextIndexTableIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,10,1,1),_TnGmplsLspNextIndexTableIndex_Type())
tnGmplsLspNextIndexTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsLspNextIndexTableIndex.setStatus(_A)
_TnGmplsLspNextIndex_Type=Unsigned32
_TnGmplsLspNextIndex_Object=MibTableColumn
tnGmplsLspNextIndex=_TnGmplsLspNextIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,10,1,2),_TnGmplsLspNextIndex_Type())
tnGmplsLspNextIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnGmplsLspNextIndex.setStatus(_A)
_TnGmplsMoveLspToTable_Object=MibTable
tnGmplsMoveLspToTable=_TnGmplsMoveLspToTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,11))
if mibBuilder.loadTexts:tnGmplsMoveLspToTable.setStatus(_A)
_TnGmplsMoveLspToEntry_Object=MibTableRow
tnGmplsMoveLspToEntry=_TnGmplsMoveLspToEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,11,1))
tnGmplsMoveLspToEntry.setIndexNames((0,_B,_m))
if mibBuilder.loadTexts:tnGmplsMoveLspToEntry.setStatus(_A)
_TnGmplsMoveLspToSrcLspId_Type=Unsigned32
_TnGmplsMoveLspToSrcLspId_Object=MibTableColumn
tnGmplsMoveLspToSrcLspId=_TnGmplsMoveLspToSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,11,1,1),_TnGmplsMoveLspToSrcLspId_Type())
tnGmplsMoveLspToSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsMoveLspToSrcLspId.setStatus(_A)
class _TnGmplsMoveLspToCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_TnGmplsMoveLspToCmd_Type.__name__=_D
_TnGmplsMoveLspToCmd_Object=MibTableColumn
tnGmplsMoveLspToCmd=_TnGmplsMoveLspToCmd_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,11,1,2),_TnGmplsMoveLspToCmd_Type())
tnGmplsMoveLspToCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsMoveLspToCmd.setStatus(_A)
_TnGmplsMoveLspToRowStatus_Type=RowStatus
_TnGmplsMoveLspToRowStatus_Object=MibTableColumn
tnGmplsMoveLspToRowStatus=_TnGmplsMoveLspToRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,11,1,3),_TnGmplsMoveLspToRowStatus_Type())
tnGmplsMoveLspToRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsMoveLspToRowStatus.setStatus(_A)
_TnGmplsMoveLspFromTable_Object=MibTable
tnGmplsMoveLspFromTable=_TnGmplsMoveLspFromTable_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,12))
if mibBuilder.loadTexts:tnGmplsMoveLspFromTable.setStatus(_A)
_TnGmplsMoveLspFromEntry_Object=MibTableRow
tnGmplsMoveLspFromEntry=_TnGmplsMoveLspFromEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,12,1))
tnGmplsMoveLspFromEntry.setIndexNames((0,_B,_n))
if mibBuilder.loadTexts:tnGmplsMoveLspFromEntry.setStatus(_A)
_TnGmplsMoveLspFromSrcLspId_Type=Unsigned32
_TnGmplsMoveLspFromSrcLspId_Object=MibTableColumn
tnGmplsMoveLspFromSrcLspId=_TnGmplsMoveLspFromSrcLspId_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,12,1,1),_TnGmplsMoveLspFromSrcLspId_Type())
tnGmplsMoveLspFromSrcLspId.setMaxAccess(_F)
if mibBuilder.loadTexts:tnGmplsMoveLspFromSrcLspId.setStatus(_A)
_TnGmplsMoveLspFromLinks_Type=OctetString
_TnGmplsMoveLspFromLinks_Object=MibTableColumn
tnGmplsMoveLspFromLinks=_TnGmplsMoveLspFromLinks_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,12,1,2),_TnGmplsMoveLspFromLinks_Type())
tnGmplsMoveLspFromLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsMoveLspFromLinks.setStatus(_A)
class _TnGmplsMoveLspFromCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('currentMain',2),('currentSpare',3)))
_TnGmplsMoveLspFromCmd_Type.__name__=_D
_TnGmplsMoveLspFromCmd_Object=MibTableColumn
tnGmplsMoveLspFromCmd=_TnGmplsMoveLspFromCmd_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,12,1,3),_TnGmplsMoveLspFromCmd_Type())
tnGmplsMoveLspFromCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsMoveLspFromCmd.setStatus(_A)
_TnGmplsMoveLspFromRowStatus_Type=RowStatus
_TnGmplsMoveLspFromRowStatus_Object=MibTableColumn
tnGmplsMoveLspFromRowStatus=_TnGmplsMoveLspFromRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,3,1,12,1,4),_TnGmplsMoveLspFromRowStatus_Type())
tnGmplsMoveLspFromRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsMoveLspFromRowStatus.setStatus(_A)
_TnGmplsLspConf_ObjectIdentity=ObjectIdentity
tnGmplsLspConf=_TnGmplsLspConf_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,3,3))
_TnGmplsLspGroups_ObjectIdentity=ObjectIdentity
tnGmplsLspGroups=_TnGmplsLspGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,3,3,1))
_TnGmplsLspCompliances_ObjectIdentity=ObjectIdentity
tnGmplsLspCompliances=_TnGmplsLspCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,3,3,2))
tnGmplsLspObjsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,1))
tnGmplsLspObjsGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:tnGmplsLspObjsGroup.setStatus(_A)
tnGmplsLspGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,2))
tnGmplsLspGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:tnGmplsLspGroup.setStatus(_A)
tnGmplsLspFlowGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,3))
tnGmplsLspFlowGroup.setObjects(*((_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:tnGmplsLspFlowGroup.setStatus(_A)
tnGmplsLspCHopGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,4))
tnGmplsLspCHopGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:tnGmplsLspCHopGroup.setStatus(_A)
tnGmplsLspAHopGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,5))
tnGmplsLspAHopGroup.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:tnGmplsLspAHopGroup.setStatus(_A)
tnGmplsLspExcludeGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,6))
tnGmplsLspExcludeGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:tnGmplsLspExcludeGroup.setStatus(_A)
tnGmplsLspTransactionGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,7))
tnGmplsLspTransactionGroup.setObjects(*((_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:tnGmplsLspTransactionGroup.setStatus(_A)
tnGmplsLspToPortGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,8))
tnGmplsLspToPortGroup.setObjects((_B,_AS))
if mibBuilder.loadTexts:tnGmplsLspToPortGroup.setStatus(_A)
tnGmplsLspSncpMgmtGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,9))
tnGmplsLspSncpMgmtGroup.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:tnGmplsLspSncpMgmtGroup.setStatus(_A)
tnGmplsLspNextIndexGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,10))
tnGmplsLspNextIndexGroup.setObjects((_B,_AW))
if mibBuilder.loadTexts:tnGmplsLspNextIndexGroup.setStatus(_A)
tnGmplsMoveLspToGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,11))
tnGmplsMoveLspToGroup.setObjects(*((_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:tnGmplsMoveLspToGroup.setStatus(_A)
tnGmplsMoveLspFromGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,3,3,1,12))
tnGmplsMoveLspFromGroup.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:tnGmplsMoveLspFromGroup.setStatus(_A)
tnGmplsLspCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,1,10,1,3,3,2,1))
tnGmplsLspCompliance.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:tnGmplsLspCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AluWdmGmplsLspProtectionState':AluWdmGmplsLspProtectionState,'tnGmplsLspMibModule':tnGmplsLspMibModule,'tnGmplsLspMIB':tnGmplsLspMIB,'tnGmplsLspObjs':tnGmplsLspObjs,_o:tnGmplsLspAttributeTotal,'tnGmplsLspTable':tnGmplsLspTable,'tnGmplsLspEntry':tnGmplsLspEntry,_N:tnGmplsLspSrcLspId,_p:tnGmplsLspDescr,_q:tnGmplsLspIngressResource,_r:tnGmplsLspEgressResource,_s:tnGmplsLspDestLsrId,_t:tnGmplsLspSetupPrio,_u:tnGmplsLspHoldingPrio,_v:tnGmplsLspDirectionType,_w:tnGmplsLspTrafficType,_x:tnGmplsLspProtectionType,_y:tnGmplsLspReversionMode,_z:tnGmplsLspIncludeAnyAffinity,_A0:tnGmplsLspExcludeAnyAffinity,_A1:tnGmplsLspConnectionType,_A2:tnGmplsLspAdminStatus,_A3:tnGmplsLspDiversityLspList,_A4:tnGmplsLspLatencyThreshold,_A5:tnGmplsLspMaxHopsConstraint,_A6:tnGmplsLspActions,_A7:tnGmplsLspProtectionStateMain,_A8:tnGmplsLspProtectionStateSpare,_A9:tnGmplsLspReversionState,_AA:tnGmplsLspSRGViolation,_AB:tnGmplsLspColorViolation,_AC:tnGmplsLspOptFsbltyViolation,_AD:tnGmplsLspQoSViolation,_AE:tnGmplsLspLatencyViolation,'tnGmplsLspFlowTable':tnGmplsLspFlowTable,'tnGmplsLspFlowEntry':tnGmplsLspFlowEntry,_T:tnGmplsLspFlowSrcLspId,_U:tnGmplsLspFlowType,_AF:tnGmplsLspFlowState,_AG:tnGmplsLspFlowId,'tnGmplsLspCHopTable':tnGmplsLspCHopTable,'tnGmplsLspCHopEntry':tnGmplsLspCHopEntry,_W:tnGmplsLspCHopSrcLspId,_X:tnGmplsLspCHopRouteType,_Y:tnGmplsLspCHopIndex,_AH:tnGmplsLspCHopSubnodeId,_AI:tnGmplsLspCHopInResource,_AJ:tnGmplsLspCHopOutResource,'tnGmplsLspAHopTable':tnGmplsLspAHopTable,'tnGmplsLspAHopEntry':tnGmplsLspAHopEntry,_Z:tnGmplsLspAHopSrcLspId,_a:tnGmplsLspAHopRouteType,_b:tnGmplsLspAHopIndex,_AK:tnGmplsLspAHopSubnodeId,_AL:tnGmplsLspAHopInResource,_AM:tnGmplsLspAHopOutResource,'tnGmplsLspExcludeTable':tnGmplsLspExcludeTable,'tnGmplsLspExcludeEntry':tnGmplsLspExcludeEntry,_c:tnGmplsLspExcludeSrcLspId,_d:tnGmplsLspExcludeIndex,_AN:tnGmplsLspExcludeSubnodeId,_AO:tnGmplsLspExcludeTELink,_AP:tnGmplsLspExcludeDBLink,'tnGmplsLspTransactionTable':tnGmplsLspTransactionTable,'tnGmplsLspTransactionEntry':tnGmplsLspTransactionEntry,_e:tnGmplsLspTransactionSrcLspId,_AQ:tnGmplsLspTransaction,_AR:tnGmplsLspTransactionState,'tnGmplsLspToPortTable':tnGmplsLspToPortTable,'tnGmplsLspToPortEntry':tnGmplsLspToPortEntry,_g:tnGmplsLspDBLinkIfId,_h:tnGmplsLspLTPSrcLspId,_i:tnGmplsLspSrcLsrId,_AS:tnGmplsLspName,'tnGmplsLspSncpMgmtTable':tnGmplsLspSncpMgmtTable,'tnGmplsLspSncpMgmtEntry':tnGmplsLspSncpMgmtEntry,_j:tnGmplsLspSncpCtpResource,_k:tnGmplsLspSncpDirection,_AT:tnGmplsLspSncpCmd,_AU:tnGmplsLspSncpState,_AV:tnGmplsLspSncpRowStatus,'tnGmplsLspNextIndexTable':tnGmplsLspNextIndexTable,'tnGmplsLspNextIndexEntry':tnGmplsLspNextIndexEntry,_l:tnGmplsLspNextIndexTableIndex,_AW:tnGmplsLspNextIndex,'tnGmplsMoveLspToTable':tnGmplsMoveLspToTable,'tnGmplsMoveLspToEntry':tnGmplsMoveLspToEntry,_m:tnGmplsMoveLspToSrcLspId,_AX:tnGmplsMoveLspToCmd,_AY:tnGmplsMoveLspToRowStatus,'tnGmplsMoveLspFromTable':tnGmplsMoveLspFromTable,'tnGmplsMoveLspFromEntry':tnGmplsMoveLspFromEntry,_n:tnGmplsMoveLspFromSrcLspId,_AZ:tnGmplsMoveLspFromLinks,_Aa:tnGmplsMoveLspFromCmd,_Ab:tnGmplsMoveLspFromRowStatus,'tnGmplsLspConf':tnGmplsLspConf,'tnGmplsLspGroups':tnGmplsLspGroups,_Ac:tnGmplsLspObjsGroup,_Ad:tnGmplsLspGroup,_Ae:tnGmplsLspFlowGroup,_Af:tnGmplsLspCHopGroup,_Ag:tnGmplsLspAHopGroup,_Ah:tnGmplsLspExcludeGroup,_Ai:tnGmplsLspTransactionGroup,_Aj:tnGmplsLspToPortGroup,_Ak:tnGmplsLspSncpMgmtGroup,_Al:tnGmplsLspNextIndexGroup,_Am:tnGmplsMoveLspToGroup,_An:tnGmplsMoveLspFromGroup,'tnGmplsLspCompliances':tnGmplsLspCompliances,'tnGmplsLspCompliance':tnGmplsLspCompliance})