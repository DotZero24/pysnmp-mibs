_Ba='snaMgtToolsRtmGroup'
_BZ='snaPu20Group'
_BY='snaSessionGroup'
_BX='snaLuGroup'
_BW='snaNodeGroup'
_BV='snaLuRtmAvgRspTime'
_BU='snaLuRtmLastRspTime'
_BT='snaLuRtmNumTrans'
_BS='snaLuRtmObjRange'
_BR='snaLuRtmObjPercent'
_BQ='snaLuRtmOverFlows'
_BP='snaLuRtmCounter4'
_BO='snaLuRtmCounter3'
_BN='snaLuRtmCounter2'
_BM='snaLuRtmCounter1'
_BL='snaLuRtmBoundary4'
_BK='snaLuRtmBoundary3'
_BJ='snaLuRtmBoundary2'
_BI='snaLuRtmBoundary1'
_BH='snaLuRtmDef'
_BG='snaLuRtmStateTime'
_BF='snaLuRtmState'
_BE='snaPu20StatsBindLus'
_BD='snaPu20StatsInActLus'
_BC='snaPu20StatsActLus'
_BB='snaPu20StatsReceivedNegativeResps'
_BA='snaPu20StatsSentNegativeResps'
_B9='snaPu20StatsReceivedPius'
_B8='snaPu20StatsSentPius'
_B7='snaPu20StatsReceivedBytes'
_B6='snaPu20StatsSentBytes'
_B5='snaLuSessnStatsReceivedNegativeResps'
_B4='snaLuSessnStatsSentNegativeResps'
_B3='snaLuSessnStatsReceivedRus'
_B2='snaLuSessnStatsSentRus'
_B1='snaLuSessnStatsReceivedBytes'
_B0='snaLuSessnStatsSentBytes'
_A_='snaLuSessnLinkIndex'
_Az='snaLuSessnUnbindType'
_Ay='snaLuSessnTerminationRu'
_Ax='snaLuSessnAdminState'
_Aw='snaLuSessnActiveTime'
_Av='snaLuSessnRcvPacingSize'
_Au='snaLuSessnSndPacingSize'
_At='snaLuSessnMaxRcvRuSize'
_As='snaLuSessnMaxSndRuSize'
_Ar='snaLuOperSessnCount'
_Aq='snaLuOperTerm'
_Ap='snaLuOperDisplayModel'
_Ao='snaLuOperLocalAddress'
_An='snaLuOperDepType'
_Am='snaLuOperType'
_Al='snaLuAdminRowStatus'
_Ak='snaLuAdminTerm'
_Aj='snaLuAdminDisplayModel'
_Ai='snaLuAdminLocalAddress'
_Ah='snaLuAdminDepType'
_Ag='snaLuAdminType'
_Af='snaLuAdminSnaName'
_Ae='snaLuAdminName'
_Ad='snaNodeLinkOperTableLastChange'
_Ac='snaNodeLinkOperMaxPiu'
_Ab='snaNodeLinkOperSpecific'
_Aa='snaNodeLinkAdminTableLastChange'
_AZ='snaNodeLinkAdminRowStatus'
_AY='snaNodeLinkAdminMaxPiu'
_AX='snaNodeLinkAdminSpecific'
_AW='snaNodeOperTableLastChange'
_AV='snaNodeOperActFailures'
_AU='snaNodeOperLastStateChange'
_AT='snaNodeOperStartTime'
_AS='snaNodeOperHostSscpId'
_AR='snaNodeOperStopMethod'
_AQ='snaNodeOperHostDescription'
_AP='snaNodeOperMaxLu'
_AO='snaNodeOperLuTermDefault'
_AN='snaNodeOperEnablingMethod'
_AM='snaNodeOperIdNum'
_AL='snaNodeOperBlockNum'
_AK='snaNodeOperXidFormat'
_AJ='snaNodeOperType'
_AI='snaNodeAdminTableLastChange'
_AH='snaNodeAdminRowStatus'
_AG='snaNodeAdminState'
_AF='snaNodeAdminStopMethod'
_AE='snaNodeAdminHostDescription'
_AD='snaNodeAdminMaxLu'
_AC='snaNodeAdminLuTermDefault'
_AB='snaNodeAdminEnablingMethod'
_AA='snaNodeAdminIdNum'
_A9='snaNodeAdminBlockNum'
_A8='snaNodeAdminXidFormat'
_A7='snaNodeAdminType'
_A6='snaNodeAdminName'
_A5='snaLuSessnStatsEntry'
_A4='snaLuOperEntry'
_A3='snaNodeLinkOperEntry'
_A2='snaNodeOperEntry'
_A1='snaLuRtmLuIndex'
_A0='snaLuRtmPuIndex'
_z='unbound'
_y='dynamic'
_x='model5B'
_w='model5A'
_v='model4B'
_u='model4A'
_t='model3B'
_s='model3A'
_r='model2B'
_q='model2A'
_p='invalid'
_o='independent'
_n='dependent'
_m='snaNodeLinkAdminIndex'
_l='normal'
_k='onlyMS'
_j='demand'
_i='startup'
_h='format3'
_g='format1'
_f='format0'
_e='networkNode'
_d='endNode'
_c='snaLuSessnSenseData'
_b='snaLuSessnOperState'
_a='snaLuSessnRemoteLuName'
_Z='snaLuSessnLocalApplName'
_Y='snaLuOperState'
_X='snaLuOperSnaName'
_W='snaLuOperName'
_V='snaNodeOperActFailureReason'
_U='snaLuSessnIndex'
_T='snaLuSessnRluIndex'
_S='snaLuAdminLuIndex'
_R='active'
_Q='inactive'
_P='snaNodeOperState'
_O='snaNodeOperName'
_N='poweroff'
_M='rshutd'
_L='termself'
_K='unbind'
_J='not-accessible'
_I='snaNodeAdminIndex'
_H='OctetString'
_G='other'
_F='DisplayString'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='SNA-NAU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,InstancePointer,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_F,'InstancePointer','PhysAddress','RowStatus','TextualConvention','TimeStamp')
snanauMIB=ModuleIdentity((1,3,6,1,2,1,34))
_SnanauObjects_ObjectIdentity=ObjectIdentity
snanauObjects=_SnanauObjects_ObjectIdentity((1,3,6,1,2,1,34,1))
_SnaNode_ObjectIdentity=ObjectIdentity
snaNode=_SnaNode_ObjectIdentity((1,3,6,1,2,1,34,1,1))
_SnaNodeAdminTable_Object=MibTable
snaNodeAdminTable=_SnaNodeAdminTable_Object((1,3,6,1,2,1,34,1,1,1))
if mibBuilder.loadTexts:snaNodeAdminTable.setStatus(_A)
_SnaNodeAdminEntry_Object=MibTableRow
snaNodeAdminEntry=_SnaNodeAdminEntry_Object((1,3,6,1,2,1,34,1,1,1,1))
snaNodeAdminEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:snaNodeAdminEntry.setStatus(_A)
_SnaNodeAdminIndex_Type=Integer32
_SnaNodeAdminIndex_Object=MibTableColumn
snaNodeAdminIndex=_SnaNodeAdminIndex_Object((1,3,6,1,2,1,34,1,1,1,1,1),_SnaNodeAdminIndex_Type())
snaNodeAdminIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snaNodeAdminIndex.setStatus(_A)
class _SnaNodeAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SnaNodeAdminName_Type.__name__=_F
_SnaNodeAdminName_Object=MibTableColumn
snaNodeAdminName=_SnaNodeAdminName_Object((1,3,6,1,2,1,34,1,1,1,1,2),_SnaNodeAdminName_Type())
snaNodeAdminName.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminName.setStatus(_A)
class _SnaNodeAdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('pu10',2),('pu20',3),('t21len',4),(_d,5),(_e,6)))
_SnaNodeAdminType_Type.__name__=_D
_SnaNodeAdminType_Object=MibTableColumn
snaNodeAdminType=_SnaNodeAdminType_Object((1,3,6,1,2,1,34,1,1,1,1,3),_SnaNodeAdminType_Type())
snaNodeAdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminType.setStatus(_A)
class _SnaNodeAdminXidFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3)))
_SnaNodeAdminXidFormat_Type.__name__=_D
_SnaNodeAdminXidFormat_Object=MibTableColumn
snaNodeAdminXidFormat=_SnaNodeAdminXidFormat_Object((1,3,6,1,2,1,34,1,1,1,1,4),_SnaNodeAdminXidFormat_Type())
snaNodeAdminXidFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminXidFormat.setStatus(_A)
class _SnaNodeAdminBlockNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SnaNodeAdminBlockNum_Type.__name__=_F
_SnaNodeAdminBlockNum_Object=MibTableColumn
snaNodeAdminBlockNum=_SnaNodeAdminBlockNum_Object((1,3,6,1,2,1,34,1,1,1,1,5),_SnaNodeAdminBlockNum_Type())
snaNodeAdminBlockNum.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminBlockNum.setStatus(_A)
class _SnaNodeAdminIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_SnaNodeAdminIdNum_Type.__name__=_F
_SnaNodeAdminIdNum_Object=MibTableColumn
snaNodeAdminIdNum=_SnaNodeAdminIdNum_Object((1,3,6,1,2,1,34,1,1,1,1,6),_SnaNodeAdminIdNum_Type())
snaNodeAdminIdNum.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminIdNum.setStatus(_A)
class _SnaNodeAdminEnablingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_i,2),(_j,3),(_k,4)))
_SnaNodeAdminEnablingMethod_Type.__name__=_D
_SnaNodeAdminEnablingMethod_Object=MibTableColumn
snaNodeAdminEnablingMethod=_SnaNodeAdminEnablingMethod_Object((1,3,6,1,2,1,34,1,1,1,1,7),_SnaNodeAdminEnablingMethod_Type())
snaNodeAdminEnablingMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminEnablingMethod.setStatus(_A)
class _SnaNodeAdminLuTermDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_SnaNodeAdminLuTermDefault_Type.__name__=_D
_SnaNodeAdminLuTermDefault_Object=MibTableColumn
snaNodeAdminLuTermDefault=_SnaNodeAdminLuTermDefault_Object((1,3,6,1,2,1,34,1,1,1,1,8),_SnaNodeAdminLuTermDefault_Type())
snaNodeAdminLuTermDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminLuTermDefault.setStatus(_A)
_SnaNodeAdminMaxLu_Type=Integer32
_SnaNodeAdminMaxLu_Object=MibTableColumn
snaNodeAdminMaxLu=_SnaNodeAdminMaxLu_Object((1,3,6,1,2,1,34,1,1,1,1,9),_SnaNodeAdminMaxLu_Type())
snaNodeAdminMaxLu.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminMaxLu.setStatus(_A)
class _SnaNodeAdminHostDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SnaNodeAdminHostDescription_Type.__name__=_F
_SnaNodeAdminHostDescription_Object=MibTableColumn
snaNodeAdminHostDescription=_SnaNodeAdminHostDescription_Object((1,3,6,1,2,1,34,1,1,1,1,10),_SnaNodeAdminHostDescription_Type())
snaNodeAdminHostDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminHostDescription.setStatus(_A)
class _SnaNodeAdminStopMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_l,2),('immed',3),('force',4)))
_SnaNodeAdminStopMethod_Type.__name__=_D
_SnaNodeAdminStopMethod_Object=MibTableColumn
snaNodeAdminStopMethod=_SnaNodeAdminStopMethod_Object((1,3,6,1,2,1,34,1,1,1,1,11),_SnaNodeAdminStopMethod_Type())
snaNodeAdminStopMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminStopMethod.setStatus(_A)
class _SnaNodeAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_SnaNodeAdminState_Type.__name__=_D
_SnaNodeAdminState_Object=MibTableColumn
snaNodeAdminState=_SnaNodeAdminState_Object((1,3,6,1,2,1,34,1,1,1,1,12),_SnaNodeAdminState_Type())
snaNodeAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminState.setStatus(_A)
_SnaNodeAdminRowStatus_Type=RowStatus
_SnaNodeAdminRowStatus_Object=MibTableColumn
snaNodeAdminRowStatus=_SnaNodeAdminRowStatus_Object((1,3,6,1,2,1,34,1,1,1,1,13),_SnaNodeAdminRowStatus_Type())
snaNodeAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeAdminRowStatus.setStatus(_A)
_SnaNodeAdminTableLastChange_Type=TimeStamp
_SnaNodeAdminTableLastChange_Object=MibScalar
snaNodeAdminTableLastChange=_SnaNodeAdminTableLastChange_Object((1,3,6,1,2,1,34,1,1,2),_SnaNodeAdminTableLastChange_Type())
snaNodeAdminTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeAdminTableLastChange.setStatus(_A)
_SnaNodeOperTable_Object=MibTable
snaNodeOperTable=_SnaNodeOperTable_Object((1,3,6,1,2,1,34,1,1,3))
if mibBuilder.loadTexts:snaNodeOperTable.setStatus(_A)
_SnaNodeOperEntry_Object=MibTableRow
snaNodeOperEntry=_SnaNodeOperEntry_Object((1,3,6,1,2,1,34,1,1,3,1))
if mibBuilder.loadTexts:snaNodeOperEntry.setStatus(_A)
class _SnaNodeOperName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SnaNodeOperName_Type.__name__=_F
_SnaNodeOperName_Object=MibTableColumn
snaNodeOperName=_SnaNodeOperName_Object((1,3,6,1,2,1,34,1,1,3,1,1),_SnaNodeOperName_Type())
snaNodeOperName.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperName.setStatus(_A)
class _SnaNodeOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('pu10',2),('pu20',3),('t21LEN',4),(_d,5),(_e,6)))
_SnaNodeOperType_Type.__name__=_D
_SnaNodeOperType_Object=MibTableColumn
snaNodeOperType=_SnaNodeOperType_Object((1,3,6,1,2,1,34,1,1,3,1,2),_SnaNodeOperType_Type())
snaNodeOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperType.setStatus(_A)
class _SnaNodeOperXidFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_g,2),(_h,3)))
_SnaNodeOperXidFormat_Type.__name__=_D
_SnaNodeOperXidFormat_Object=MibTableColumn
snaNodeOperXidFormat=_SnaNodeOperXidFormat_Object((1,3,6,1,2,1,34,1,1,3,1,3),_SnaNodeOperXidFormat_Type())
snaNodeOperXidFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperXidFormat.setStatus(_A)
class _SnaNodeOperBlockNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SnaNodeOperBlockNum_Type.__name__=_F
_SnaNodeOperBlockNum_Object=MibTableColumn
snaNodeOperBlockNum=_SnaNodeOperBlockNum_Object((1,3,6,1,2,1,34,1,1,3,1,4),_SnaNodeOperBlockNum_Type())
snaNodeOperBlockNum.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperBlockNum.setStatus(_A)
class _SnaNodeOperIdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_SnaNodeOperIdNum_Type.__name__=_F
_SnaNodeOperIdNum_Object=MibTableColumn
snaNodeOperIdNum=_SnaNodeOperIdNum_Object((1,3,6,1,2,1,34,1,1,3,1,5),_SnaNodeOperIdNum_Type())
snaNodeOperIdNum.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperIdNum.setStatus(_A)
class _SnaNodeOperEnablingMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_i,2),(_j,3),(_k,4)))
_SnaNodeOperEnablingMethod_Type.__name__=_D
_SnaNodeOperEnablingMethod_Object=MibTableColumn
snaNodeOperEnablingMethod=_SnaNodeOperEnablingMethod_Object((1,3,6,1,2,1,34,1,1,3,1,6),_SnaNodeOperEnablingMethod_Type())
snaNodeOperEnablingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperEnablingMethod.setStatus(_A)
class _SnaNodeOperLuTermDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_SnaNodeOperLuTermDefault_Type.__name__=_D
_SnaNodeOperLuTermDefault_Object=MibTableColumn
snaNodeOperLuTermDefault=_SnaNodeOperLuTermDefault_Object((1,3,6,1,2,1,34,1,1,3,1,7),_SnaNodeOperLuTermDefault_Type())
snaNodeOperLuTermDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperLuTermDefault.setStatus(_A)
_SnaNodeOperMaxLu_Type=Integer32
_SnaNodeOperMaxLu_Object=MibTableColumn
snaNodeOperMaxLu=_SnaNodeOperMaxLu_Object((1,3,6,1,2,1,34,1,1,3,1,8),_SnaNodeOperMaxLu_Type())
snaNodeOperMaxLu.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperMaxLu.setStatus(_A)
class _SnaNodeOperHostDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SnaNodeOperHostDescription_Type.__name__=_F
_SnaNodeOperHostDescription_Object=MibTableColumn
snaNodeOperHostDescription=_SnaNodeOperHostDescription_Object((1,3,6,1,2,1,34,1,1,3,1,9),_SnaNodeOperHostDescription_Type())
snaNodeOperHostDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperHostDescription.setStatus(_A)
class _SnaNodeOperStopMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_l,2),('immed',3),('force',4)))
_SnaNodeOperStopMethod_Type.__name__=_D
_SnaNodeOperStopMethod_Object=MibTableColumn
snaNodeOperStopMethod=_SnaNodeOperStopMethod_Object((1,3,6,1,2,1,34,1,1,3,1,10),_SnaNodeOperStopMethod_Type())
snaNodeOperStopMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperStopMethod.setStatus(_A)
class _SnaNodeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),('waiting',3),('stopping',4)))
_SnaNodeOperState_Type.__name__=_D
_SnaNodeOperState_Object=MibTableColumn
snaNodeOperState=_SnaNodeOperState_Object((1,3,6,1,2,1,34,1,1,3,1,11),_SnaNodeOperState_Type())
snaNodeOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperState.setStatus(_A)
class _SnaNodeOperHostSscpId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_SnaNodeOperHostSscpId_Type.__name__=_H
_SnaNodeOperHostSscpId_Object=MibTableColumn
snaNodeOperHostSscpId=_SnaNodeOperHostSscpId_Object((1,3,6,1,2,1,34,1,1,3,1,12),_SnaNodeOperHostSscpId_Type())
snaNodeOperHostSscpId.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperHostSscpId.setStatus(_A)
_SnaNodeOperStartTime_Type=TimeStamp
_SnaNodeOperStartTime_Object=MibTableColumn
snaNodeOperStartTime=_SnaNodeOperStartTime_Object((1,3,6,1,2,1,34,1,1,3,1,13),_SnaNodeOperStartTime_Type())
snaNodeOperStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperStartTime.setStatus(_A)
_SnaNodeOperLastStateChange_Type=TimeStamp
_SnaNodeOperLastStateChange_Object=MibTableColumn
snaNodeOperLastStateChange=_SnaNodeOperLastStateChange_Object((1,3,6,1,2,1,34,1,1,3,1,14),_SnaNodeOperLastStateChange_Type())
snaNodeOperLastStateChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperLastStateChange.setStatus(_A)
_SnaNodeOperActFailures_Type=Counter32
_SnaNodeOperActFailures_Object=MibTableColumn
snaNodeOperActFailures=_SnaNodeOperActFailures_Object((1,3,6,1,2,1,34,1,1,3,1,15),_SnaNodeOperActFailures_Type())
snaNodeOperActFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperActFailures.setStatus(_A)
class _SnaNodeOperActFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('linkFailure',2),('noResources',3),('badConfiguration',4),('internalError',5)))
_SnaNodeOperActFailureReason_Type.__name__=_D
_SnaNodeOperActFailureReason_Object=MibTableColumn
snaNodeOperActFailureReason=_SnaNodeOperActFailureReason_Object((1,3,6,1,2,1,34,1,1,3,1,16),_SnaNodeOperActFailureReason_Type())
snaNodeOperActFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperActFailureReason.setStatus(_A)
_SnaNodeOperTableLastChange_Type=TimeStamp
_SnaNodeOperTableLastChange_Object=MibScalar
snaNodeOperTableLastChange=_SnaNodeOperTableLastChange_Object((1,3,6,1,2,1,34,1,1,4),_SnaNodeOperTableLastChange_Type())
snaNodeOperTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeOperTableLastChange.setStatus(_A)
_SnaPu20StatsTable_Object=MibTable
snaPu20StatsTable=_SnaPu20StatsTable_Object((1,3,6,1,2,1,34,1,1,5))
if mibBuilder.loadTexts:snaPu20StatsTable.setStatus(_A)
_SnaPu20StatsEntry_Object=MibTableRow
snaPu20StatsEntry=_SnaPu20StatsEntry_Object((1,3,6,1,2,1,34,1,1,5,1))
snaPu20StatsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:snaPu20StatsEntry.setStatus(_A)
_SnaPu20StatsSentBytes_Type=Counter32
_SnaPu20StatsSentBytes_Object=MibTableColumn
snaPu20StatsSentBytes=_SnaPu20StatsSentBytes_Object((1,3,6,1,2,1,34,1,1,5,1,1),_SnaPu20StatsSentBytes_Type())
snaPu20StatsSentBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsSentBytes.setStatus(_A)
_SnaPu20StatsReceivedBytes_Type=Counter32
_SnaPu20StatsReceivedBytes_Object=MibTableColumn
snaPu20StatsReceivedBytes=_SnaPu20StatsReceivedBytes_Object((1,3,6,1,2,1,34,1,1,5,1,2),_SnaPu20StatsReceivedBytes_Type())
snaPu20StatsReceivedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsReceivedBytes.setStatus(_A)
_SnaPu20StatsSentPius_Type=Counter32
_SnaPu20StatsSentPius_Object=MibTableColumn
snaPu20StatsSentPius=_SnaPu20StatsSentPius_Object((1,3,6,1,2,1,34,1,1,5,1,3),_SnaPu20StatsSentPius_Type())
snaPu20StatsSentPius.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsSentPius.setStatus(_A)
_SnaPu20StatsReceivedPius_Type=Counter32
_SnaPu20StatsReceivedPius_Object=MibTableColumn
snaPu20StatsReceivedPius=_SnaPu20StatsReceivedPius_Object((1,3,6,1,2,1,34,1,1,5,1,4),_SnaPu20StatsReceivedPius_Type())
snaPu20StatsReceivedPius.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsReceivedPius.setStatus(_A)
_SnaPu20StatsSentNegativeResps_Type=Counter32
_SnaPu20StatsSentNegativeResps_Object=MibTableColumn
snaPu20StatsSentNegativeResps=_SnaPu20StatsSentNegativeResps_Object((1,3,6,1,2,1,34,1,1,5,1,5),_SnaPu20StatsSentNegativeResps_Type())
snaPu20StatsSentNegativeResps.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsSentNegativeResps.setStatus(_A)
_SnaPu20StatsReceivedNegativeResps_Type=Counter32
_SnaPu20StatsReceivedNegativeResps_Object=MibTableColumn
snaPu20StatsReceivedNegativeResps=_SnaPu20StatsReceivedNegativeResps_Object((1,3,6,1,2,1,34,1,1,5,1,6),_SnaPu20StatsReceivedNegativeResps_Type())
snaPu20StatsReceivedNegativeResps.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsReceivedNegativeResps.setStatus(_A)
_SnaPu20StatsActLus_Type=Gauge32
_SnaPu20StatsActLus_Object=MibTableColumn
snaPu20StatsActLus=_SnaPu20StatsActLus_Object((1,3,6,1,2,1,34,1,1,5,1,7),_SnaPu20StatsActLus_Type())
snaPu20StatsActLus.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsActLus.setStatus(_A)
_SnaPu20StatsInActLus_Type=Gauge32
_SnaPu20StatsInActLus_Object=MibTableColumn
snaPu20StatsInActLus=_SnaPu20StatsInActLus_Object((1,3,6,1,2,1,34,1,1,5,1,8),_SnaPu20StatsInActLus_Type())
snaPu20StatsInActLus.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsInActLus.setStatus(_A)
_SnaPu20StatsBindLus_Type=Gauge32
_SnaPu20StatsBindLus_Object=MibTableColumn
snaPu20StatsBindLus=_SnaPu20StatsBindLus_Object((1,3,6,1,2,1,34,1,1,5,1,9),_SnaPu20StatsBindLus_Type())
snaPu20StatsBindLus.setMaxAccess(_C)
if mibBuilder.loadTexts:snaPu20StatsBindLus.setStatus(_A)
_SnaNodeLinkAdminTable_Object=MibTable
snaNodeLinkAdminTable=_SnaNodeLinkAdminTable_Object((1,3,6,1,2,1,34,1,1,6))
if mibBuilder.loadTexts:snaNodeLinkAdminTable.setStatus(_A)
_SnaNodeLinkAdminEntry_Object=MibTableRow
snaNodeLinkAdminEntry=_SnaNodeLinkAdminEntry_Object((1,3,6,1,2,1,34,1,1,6,1))
snaNodeLinkAdminEntry.setIndexNames((0,_B,_I),(0,_B,_m))
if mibBuilder.loadTexts:snaNodeLinkAdminEntry.setStatus(_A)
_SnaNodeLinkAdminIndex_Type=Integer32
_SnaNodeLinkAdminIndex_Object=MibTableColumn
snaNodeLinkAdminIndex=_SnaNodeLinkAdminIndex_Object((1,3,6,1,2,1,34,1,1,6,1,1),_SnaNodeLinkAdminIndex_Type())
snaNodeLinkAdminIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snaNodeLinkAdminIndex.setStatus(_A)
_SnaNodeLinkAdminSpecific_Type=InstancePointer
_SnaNodeLinkAdminSpecific_Object=MibTableColumn
snaNodeLinkAdminSpecific=_SnaNodeLinkAdminSpecific_Object((1,3,6,1,2,1,34,1,1,6,1,2),_SnaNodeLinkAdminSpecific_Type())
snaNodeLinkAdminSpecific.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeLinkAdminSpecific.setStatus(_A)
_SnaNodeLinkAdminMaxPiu_Type=Integer32
_SnaNodeLinkAdminMaxPiu_Object=MibTableColumn
snaNodeLinkAdminMaxPiu=_SnaNodeLinkAdminMaxPiu_Object((1,3,6,1,2,1,34,1,1,6,1,3),_SnaNodeLinkAdminMaxPiu_Type())
snaNodeLinkAdminMaxPiu.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeLinkAdminMaxPiu.setStatus(_A)
_SnaNodeLinkAdminRowStatus_Type=RowStatus
_SnaNodeLinkAdminRowStatus_Object=MibTableColumn
snaNodeLinkAdminRowStatus=_SnaNodeLinkAdminRowStatus_Object((1,3,6,1,2,1,34,1,1,6,1,4),_SnaNodeLinkAdminRowStatus_Type())
snaNodeLinkAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snaNodeLinkAdminRowStatus.setStatus(_A)
_SnaNodeLinkAdminTableLastChange_Type=TimeStamp
_SnaNodeLinkAdminTableLastChange_Object=MibScalar
snaNodeLinkAdminTableLastChange=_SnaNodeLinkAdminTableLastChange_Object((1,3,6,1,2,1,34,1,1,7),_SnaNodeLinkAdminTableLastChange_Type())
snaNodeLinkAdminTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeLinkAdminTableLastChange.setStatus(_A)
_SnaNodeLinkOperTable_Object=MibTable
snaNodeLinkOperTable=_SnaNodeLinkOperTable_Object((1,3,6,1,2,1,34,1,1,8))
if mibBuilder.loadTexts:snaNodeLinkOperTable.setStatus(_A)
_SnaNodeLinkOperEntry_Object=MibTableRow
snaNodeLinkOperEntry=_SnaNodeLinkOperEntry_Object((1,3,6,1,2,1,34,1,1,8,1))
if mibBuilder.loadTexts:snaNodeLinkOperEntry.setStatus(_A)
_SnaNodeLinkOperSpecific_Type=InstancePointer
_SnaNodeLinkOperSpecific_Object=MibTableColumn
snaNodeLinkOperSpecific=_SnaNodeLinkOperSpecific_Object((1,3,6,1,2,1,34,1,1,8,1,1),_SnaNodeLinkOperSpecific_Type())
snaNodeLinkOperSpecific.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeLinkOperSpecific.setStatus(_A)
_SnaNodeLinkOperMaxPiu_Type=Integer32
_SnaNodeLinkOperMaxPiu_Object=MibTableColumn
snaNodeLinkOperMaxPiu=_SnaNodeLinkOperMaxPiu_Object((1,3,6,1,2,1,34,1,1,8,1,2),_SnaNodeLinkOperMaxPiu_Type())
snaNodeLinkOperMaxPiu.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeLinkOperMaxPiu.setStatus(_A)
_SnaNodeLinkOperTableLastChange_Type=TimeStamp
_SnaNodeLinkOperTableLastChange_Object=MibScalar
snaNodeLinkOperTableLastChange=_SnaNodeLinkOperTableLastChange_Object((1,3,6,1,2,1,34,1,1,9),_SnaNodeLinkOperTableLastChange_Type())
snaNodeLinkOperTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:snaNodeLinkOperTableLastChange.setStatus(_A)
_SnaNodeTraps_ObjectIdentity=ObjectIdentity
snaNodeTraps=_SnaNodeTraps_ObjectIdentity((1,3,6,1,2,1,34,1,1,10))
_SnaLu_ObjectIdentity=ObjectIdentity
snaLu=_SnaLu_ObjectIdentity((1,3,6,1,2,1,34,1,2))
_SnaLuAdminTable_Object=MibTable
snaLuAdminTable=_SnaLuAdminTable_Object((1,3,6,1,2,1,34,1,2,1))
if mibBuilder.loadTexts:snaLuAdminTable.setStatus(_A)
_SnaLuAdminEntry_Object=MibTableRow
snaLuAdminEntry=_SnaLuAdminEntry_Object((1,3,6,1,2,1,34,1,2,1,1))
snaLuAdminEntry.setIndexNames((0,_B,_I),(0,_B,_S))
if mibBuilder.loadTexts:snaLuAdminEntry.setStatus(_A)
_SnaLuAdminLuIndex_Type=Integer32
_SnaLuAdminLuIndex_Object=MibTableColumn
snaLuAdminLuIndex=_SnaLuAdminLuIndex_Object((1,3,6,1,2,1,34,1,2,1,1,1),_SnaLuAdminLuIndex_Type())
snaLuAdminLuIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snaLuAdminLuIndex.setStatus(_A)
class _SnaLuAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_SnaLuAdminName_Type.__name__=_F
_SnaLuAdminName_Object=MibTableColumn
snaLuAdminName=_SnaLuAdminName_Object((1,3,6,1,2,1,34,1,2,1,1,2),_SnaLuAdminName_Type())
snaLuAdminName.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminName.setStatus(_A)
class _SnaLuAdminSnaName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_SnaLuAdminSnaName_Type.__name__=_F
_SnaLuAdminSnaName_Object=MibTableColumn
snaLuAdminSnaName=_SnaLuAdminSnaName_Object((1,3,6,1,2,1,34,1,2,1,1,3),_SnaLuAdminSnaName_Type())
snaLuAdminSnaName.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminSnaName.setStatus(_A)
class _SnaLuAdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),('lu0',2),('lu1',3),('lu2',4),('lu3',5),('lu4',6),('lu62',7),('lu7',8)))
_SnaLuAdminType_Type.__name__=_D
_SnaLuAdminType_Object=MibTableColumn
snaLuAdminType=_SnaLuAdminType_Object((1,3,6,1,2,1,34,1,2,1,1,4),_SnaLuAdminType_Type())
snaLuAdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminType.setStatus(_A)
class _SnaLuAdminDepType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_SnaLuAdminDepType_Type.__name__=_D
_SnaLuAdminDepType_Object=MibTableColumn
snaLuAdminDepType=_SnaLuAdminDepType_Object((1,3,6,1,2,1,34,1,2,1,1,5),_SnaLuAdminDepType_Type())
snaLuAdminDepType.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminDepType.setStatus(_A)
class _SnaLuAdminLocalAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SnaLuAdminLocalAddress_Type.__name__=_H
_SnaLuAdminLocalAddress_Object=MibTableColumn
snaLuAdminLocalAddress=_SnaLuAdminLocalAddress_Object((1,3,6,1,2,1,34,1,2,1,1,6),_SnaLuAdminLocalAddress_Type())
snaLuAdminLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminLocalAddress.setStatus(_A)
class _SnaLuAdminDisplayModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7),(_w,8),(_x,9),(_y,10)))
_SnaLuAdminDisplayModel_Type.__name__=_D
_SnaLuAdminDisplayModel_Object=MibTableColumn
snaLuAdminDisplayModel=_SnaLuAdminDisplayModel_Object((1,3,6,1,2,1,34,1,2,1,1,7),_SnaLuAdminDisplayModel_Type())
snaLuAdminDisplayModel.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminDisplayModel.setStatus(_A)
class _SnaLuAdminTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_SnaLuAdminTerm_Type.__name__=_D
_SnaLuAdminTerm_Object=MibTableColumn
snaLuAdminTerm=_SnaLuAdminTerm_Object((1,3,6,1,2,1,34,1,2,1,1,8),_SnaLuAdminTerm_Type())
snaLuAdminTerm.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminTerm.setStatus(_A)
_SnaLuAdminRowStatus_Type=RowStatus
_SnaLuAdminRowStatus_Object=MibTableColumn
snaLuAdminRowStatus=_SnaLuAdminRowStatus_Object((1,3,6,1,2,1,34,1,2,1,1,9),_SnaLuAdminRowStatus_Type())
snaLuAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snaLuAdminRowStatus.setStatus(_A)
_SnaLuOperTable_Object=MibTable
snaLuOperTable=_SnaLuOperTable_Object((1,3,6,1,2,1,34,1,2,2))
if mibBuilder.loadTexts:snaLuOperTable.setStatus(_A)
_SnaLuOperEntry_Object=MibTableRow
snaLuOperEntry=_SnaLuOperEntry_Object((1,3,6,1,2,1,34,1,2,2,1))
if mibBuilder.loadTexts:snaLuOperEntry.setStatus(_A)
class _SnaLuOperName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_SnaLuOperName_Type.__name__=_F
_SnaLuOperName_Object=MibTableColumn
snaLuOperName=_SnaLuOperName_Object((1,3,6,1,2,1,34,1,2,2,1,1),_SnaLuOperName_Type())
snaLuOperName.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperName.setStatus(_A)
class _SnaLuOperSnaName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_SnaLuOperSnaName_Type.__name__=_F
_SnaLuOperSnaName_Object=MibTableColumn
snaLuOperSnaName=_SnaLuOperSnaName_Object((1,3,6,1,2,1,34,1,2,2,1,2),_SnaLuOperSnaName_Type())
snaLuOperSnaName.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperSnaName.setStatus(_A)
class _SnaLuOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),('lu0',2),('lu1',3),('lu2',4),('lu3',5),('lu4',6),('lu62',7),('lu7',8)))
_SnaLuOperType_Type.__name__=_D
_SnaLuOperType_Object=MibTableColumn
snaLuOperType=_SnaLuOperType_Object((1,3,6,1,2,1,34,1,2,2,1,3),_SnaLuOperType_Type())
snaLuOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperType.setStatus(_A)
class _SnaLuOperDepType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_SnaLuOperDepType_Type.__name__=_D
_SnaLuOperDepType_Object=MibTableColumn
snaLuOperDepType=_SnaLuOperDepType_Object((1,3,6,1,2,1,34,1,2,2,1,4),_SnaLuOperDepType_Type())
snaLuOperDepType.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperDepType.setStatus(_A)
class _SnaLuOperLocalAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SnaLuOperLocalAddress_Type.__name__=_H
_SnaLuOperLocalAddress_Object=MibTableColumn
snaLuOperLocalAddress=_SnaLuOperLocalAddress_Object((1,3,6,1,2,1,34,1,2,2,1,5),_SnaLuOperLocalAddress_Type())
snaLuOperLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperLocalAddress.setStatus(_A)
class _SnaLuOperDisplayModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7),(_w,8),(_x,9),(_y,10)))
_SnaLuOperDisplayModel_Type.__name__=_D
_SnaLuOperDisplayModel_Object=MibTableColumn
snaLuOperDisplayModel=_SnaLuOperDisplayModel_Object((1,3,6,1,2,1,34,1,2,2,1,6),_SnaLuOperDisplayModel_Type())
snaLuOperDisplayModel.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperDisplayModel.setStatus(_A)
class _SnaLuOperTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_SnaLuOperTerm_Type.__name__=_D
_SnaLuOperTerm_Object=MibTableColumn
snaLuOperTerm=_SnaLuOperTerm_Object((1,3,6,1,2,1,34,1,2,2,1,7),_SnaLuOperTerm_Type())
snaLuOperTerm.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperTerm.setStatus(_A)
class _SnaLuOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_SnaLuOperState_Type.__name__=_D
_SnaLuOperState_Object=MibTableColumn
snaLuOperState=_SnaLuOperState_Object((1,3,6,1,2,1,34,1,2,2,1,8),_SnaLuOperState_Type())
snaLuOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperState.setStatus(_A)
_SnaLuOperSessnCount_Type=Gauge32
_SnaLuOperSessnCount_Object=MibTableColumn
snaLuOperSessnCount=_SnaLuOperSessnCount_Object((1,3,6,1,2,1,34,1,2,2,1,9),_SnaLuOperSessnCount_Type())
snaLuOperSessnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuOperSessnCount.setStatus(_A)
_SnaLuSessnTable_Object=MibTable
snaLuSessnTable=_SnaLuSessnTable_Object((1,3,6,1,2,1,34,1,2,3))
if mibBuilder.loadTexts:snaLuSessnTable.setStatus(_A)
_SnaLuSessnEntry_Object=MibTableRow
snaLuSessnEntry=_SnaLuSessnEntry_Object((1,3,6,1,2,1,34,1,2,3,1))
snaLuSessnEntry.setIndexNames((0,_B,_I),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:snaLuSessnEntry.setStatus(_A)
_SnaLuSessnRluIndex_Type=Integer32
_SnaLuSessnRluIndex_Object=MibTableColumn
snaLuSessnRluIndex=_SnaLuSessnRluIndex_Object((1,3,6,1,2,1,34,1,2,3,1,1),_SnaLuSessnRluIndex_Type())
snaLuSessnRluIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnRluIndex.setStatus(_A)
_SnaLuSessnIndex_Type=Integer32
_SnaLuSessnIndex_Object=MibTableColumn
snaLuSessnIndex=_SnaLuSessnIndex_Object((1,3,6,1,2,1,34,1,2,3,1,2),_SnaLuSessnIndex_Type())
snaLuSessnIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnIndex.setStatus(_A)
class _SnaLuSessnLocalApplName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_SnaLuSessnLocalApplName_Type.__name__=_F
_SnaLuSessnLocalApplName_Object=MibTableColumn
snaLuSessnLocalApplName=_SnaLuSessnLocalApplName_Object((1,3,6,1,2,1,34,1,2,3,1,3),_SnaLuSessnLocalApplName_Type())
snaLuSessnLocalApplName.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnLocalApplName.setStatus(_A)
class _SnaLuSessnRemoteLuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_SnaLuSessnRemoteLuName_Type.__name__=_F
_SnaLuSessnRemoteLuName_Object=MibTableColumn
snaLuSessnRemoteLuName=_SnaLuSessnRemoteLuName_Object((1,3,6,1,2,1,34,1,2,3,1,4),_SnaLuSessnRemoteLuName_Type())
snaLuSessnRemoteLuName.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnRemoteLuName.setStatus(_A)
class _SnaLuSessnMaxSndRuSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_SnaLuSessnMaxSndRuSize_Type.__name__=_D
_SnaLuSessnMaxSndRuSize_Object=MibTableColumn
snaLuSessnMaxSndRuSize=_SnaLuSessnMaxSndRuSize_Object((1,3,6,1,2,1,34,1,2,3,1,5),_SnaLuSessnMaxSndRuSize_Type())
snaLuSessnMaxSndRuSize.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnMaxSndRuSize.setStatus(_A)
class _SnaLuSessnMaxRcvRuSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_SnaLuSessnMaxRcvRuSize_Type.__name__=_D
_SnaLuSessnMaxRcvRuSize_Object=MibTableColumn
snaLuSessnMaxRcvRuSize=_SnaLuSessnMaxRcvRuSize_Object((1,3,6,1,2,1,34,1,2,3,1,6),_SnaLuSessnMaxRcvRuSize_Type())
snaLuSessnMaxRcvRuSize.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnMaxRcvRuSize.setStatus(_A)
class _SnaLuSessnSndPacingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_SnaLuSessnSndPacingSize_Type.__name__=_D
_SnaLuSessnSndPacingSize_Object=MibTableColumn
snaLuSessnSndPacingSize=_SnaLuSessnSndPacingSize_Object((1,3,6,1,2,1,34,1,2,3,1,7),_SnaLuSessnSndPacingSize_Type())
snaLuSessnSndPacingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnSndPacingSize.setStatus(_A)
class _SnaLuSessnRcvPacingSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_SnaLuSessnRcvPacingSize_Type.__name__=_D
_SnaLuSessnRcvPacingSize_Object=MibTableColumn
snaLuSessnRcvPacingSize=_SnaLuSessnRcvPacingSize_Object((1,3,6,1,2,1,34,1,2,3,1,8),_SnaLuSessnRcvPacingSize_Type())
snaLuSessnRcvPacingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnRcvPacingSize.setStatus(_A)
_SnaLuSessnActiveTime_Type=TimeStamp
_SnaLuSessnActiveTime_Object=MibTableColumn
snaLuSessnActiveTime=_SnaLuSessnActiveTime_Object((1,3,6,1,2,1,34,1,2,3,1,9),_SnaLuSessnActiveTime_Type())
snaLuSessnActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnActiveTime.setStatus(_A)
class _SnaLuSessnAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_z,1),('bound',3)))
_SnaLuSessnAdminState_Type.__name__=_D
_SnaLuSessnAdminState_Object=MibTableColumn
snaLuSessnAdminState=_SnaLuSessnAdminState_Object((1,3,6,1,2,1,34,1,2,3,1,10),_SnaLuSessnAdminState_Type())
snaLuSessnAdminState.setMaxAccess('read-write')
if mibBuilder.loadTexts:snaLuSessnAdminState.setStatus(_A)
class _SnaLuSessnOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_z,1),('pendingBind',2),('bound',3),('pendingUnbind',4)))
_SnaLuSessnOperState_Type.__name__=_D
_SnaLuSessnOperState_Object=MibTableColumn
snaLuSessnOperState=_SnaLuSessnOperState_Object((1,3,6,1,2,1,34,1,2,3,1,11),_SnaLuSessnOperState_Type())
snaLuSessnOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnOperState.setStatus(_A)
class _SnaLuSessnSenseData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnaLuSessnSenseData_Type.__name__=_H
_SnaLuSessnSenseData_Object=MibTableColumn
snaLuSessnSenseData=_SnaLuSessnSenseData_Object((1,3,6,1,2,1,34,1,2,3,1,12),_SnaLuSessnSenseData_Type())
snaLuSessnSenseData.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnSenseData.setStatus(_A)
class _SnaLuSessnTerminationRu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('bindFailure',2),(_K,3)))
_SnaLuSessnTerminationRu_Type.__name__=_D
_SnaLuSessnTerminationRu_Object=MibTableColumn
snaLuSessnTerminationRu=_SnaLuSessnTerminationRu_Object((1,3,6,1,2,1,34,1,2,3,1,13),_SnaLuSessnTerminationRu_Type())
snaLuSessnTerminationRu.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnTerminationRu.setStatus(_A)
class _SnaLuSessnUnbindType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_SnaLuSessnUnbindType_Type.__name__=_H
_SnaLuSessnUnbindType_Object=MibTableColumn
snaLuSessnUnbindType=_SnaLuSessnUnbindType_Object((1,3,6,1,2,1,34,1,2,3,1,14),_SnaLuSessnUnbindType_Type())
snaLuSessnUnbindType.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnUnbindType.setStatus(_A)
_SnaLuSessnLinkIndex_Type=Integer32
_SnaLuSessnLinkIndex_Object=MibTableColumn
snaLuSessnLinkIndex=_SnaLuSessnLinkIndex_Object((1,3,6,1,2,1,34,1,2,3,1,15),_SnaLuSessnLinkIndex_Type())
snaLuSessnLinkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnLinkIndex.setStatus(_A)
_SnaLuSessnStatsTable_Object=MibTable
snaLuSessnStatsTable=_SnaLuSessnStatsTable_Object((1,3,6,1,2,1,34,1,2,4))
if mibBuilder.loadTexts:snaLuSessnStatsTable.setStatus(_A)
_SnaLuSessnStatsEntry_Object=MibTableRow
snaLuSessnStatsEntry=_SnaLuSessnStatsEntry_Object((1,3,6,1,2,1,34,1,2,4,1))
if mibBuilder.loadTexts:snaLuSessnStatsEntry.setStatus(_A)
_SnaLuSessnStatsSentBytes_Type=Counter32
_SnaLuSessnStatsSentBytes_Object=MibTableColumn
snaLuSessnStatsSentBytes=_SnaLuSessnStatsSentBytes_Object((1,3,6,1,2,1,34,1,2,4,1,1),_SnaLuSessnStatsSentBytes_Type())
snaLuSessnStatsSentBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnStatsSentBytes.setStatus(_A)
_SnaLuSessnStatsReceivedBytes_Type=Counter32
_SnaLuSessnStatsReceivedBytes_Object=MibTableColumn
snaLuSessnStatsReceivedBytes=_SnaLuSessnStatsReceivedBytes_Object((1,3,6,1,2,1,34,1,2,4,1,2),_SnaLuSessnStatsReceivedBytes_Type())
snaLuSessnStatsReceivedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnStatsReceivedBytes.setStatus(_A)
_SnaLuSessnStatsSentRus_Type=Counter32
_SnaLuSessnStatsSentRus_Object=MibTableColumn
snaLuSessnStatsSentRus=_SnaLuSessnStatsSentRus_Object((1,3,6,1,2,1,34,1,2,4,1,3),_SnaLuSessnStatsSentRus_Type())
snaLuSessnStatsSentRus.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnStatsSentRus.setStatus(_A)
_SnaLuSessnStatsReceivedRus_Type=Counter32
_SnaLuSessnStatsReceivedRus_Object=MibTableColumn
snaLuSessnStatsReceivedRus=_SnaLuSessnStatsReceivedRus_Object((1,3,6,1,2,1,34,1,2,4,1,4),_SnaLuSessnStatsReceivedRus_Type())
snaLuSessnStatsReceivedRus.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnStatsReceivedRus.setStatus(_A)
_SnaLuSessnStatsSentNegativeResps_Type=Counter32
_SnaLuSessnStatsSentNegativeResps_Object=MibTableColumn
snaLuSessnStatsSentNegativeResps=_SnaLuSessnStatsSentNegativeResps_Object((1,3,6,1,2,1,34,1,2,4,1,5),_SnaLuSessnStatsSentNegativeResps_Type())
snaLuSessnStatsSentNegativeResps.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnStatsSentNegativeResps.setStatus(_A)
_SnaLuSessnStatsReceivedNegativeResps_Type=Counter32
_SnaLuSessnStatsReceivedNegativeResps_Object=MibTableColumn
snaLuSessnStatsReceivedNegativeResps=_SnaLuSessnStatsReceivedNegativeResps_Object((1,3,6,1,2,1,34,1,2,4,1,6),_SnaLuSessnStatsReceivedNegativeResps_Type())
snaLuSessnStatsReceivedNegativeResps.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuSessnStatsReceivedNegativeResps.setStatus(_A)
_SnaLuTraps_ObjectIdentity=ObjectIdentity
snaLuTraps=_SnaLuTraps_ObjectIdentity((1,3,6,1,2,1,34,1,2,5))
_SnaMgtTools_ObjectIdentity=ObjectIdentity
snaMgtTools=_SnaMgtTools_ObjectIdentity((1,3,6,1,2,1,34,1,3))
_SnaLuRtmTable_Object=MibTable
snaLuRtmTable=_SnaLuRtmTable_Object((1,3,6,1,2,1,34,1,3,1))
if mibBuilder.loadTexts:snaLuRtmTable.setStatus(_A)
_SnaLuRtmEntry_Object=MibTableRow
snaLuRtmEntry=_SnaLuRtmEntry_Object((1,3,6,1,2,1,34,1,3,1,1))
snaLuRtmEntry.setIndexNames((0,_B,_A0),(0,_B,_A1))
if mibBuilder.loadTexts:snaLuRtmEntry.setStatus(_A)
_SnaLuRtmPuIndex_Type=Integer32
_SnaLuRtmPuIndex_Object=MibTableColumn
snaLuRtmPuIndex=_SnaLuRtmPuIndex_Object((1,3,6,1,2,1,34,1,3,1,1,1),_SnaLuRtmPuIndex_Type())
snaLuRtmPuIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snaLuRtmPuIndex.setStatus(_A)
_SnaLuRtmLuIndex_Type=Integer32
_SnaLuRtmLuIndex_Object=MibTableColumn
snaLuRtmLuIndex=_SnaLuRtmLuIndex_Object((1,3,6,1,2,1,34,1,3,1,1,2),_SnaLuRtmLuIndex_Type())
snaLuRtmLuIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snaLuRtmLuIndex.setStatus(_A)
class _SnaLuRtmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_SnaLuRtmState_Type.__name__=_D
_SnaLuRtmState_Object=MibTableColumn
snaLuRtmState=_SnaLuRtmState_Object((1,3,6,1,2,1,34,1,3,1,1,3),_SnaLuRtmState_Type())
snaLuRtmState.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmState.setStatus(_A)
_SnaLuRtmStateTime_Type=TimeStamp
_SnaLuRtmStateTime_Object=MibTableColumn
snaLuRtmStateTime=_SnaLuRtmStateTime_Object((1,3,6,1,2,1,34,1,3,1,1,4),_SnaLuRtmStateTime_Type())
snaLuRtmStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmStateTime.setStatus(_A)
class _SnaLuRtmDef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('firstChar',1),('kb',2),('cdeb',3)))
_SnaLuRtmDef_Type.__name__=_D
_SnaLuRtmDef_Object=MibTableColumn
snaLuRtmDef=_SnaLuRtmDef_Object((1,3,6,1,2,1,34,1,3,1,1,5),_SnaLuRtmDef_Type())
snaLuRtmDef.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmDef.setStatus(_A)
_SnaLuRtmBoundary1_Type=Integer32
_SnaLuRtmBoundary1_Object=MibTableColumn
snaLuRtmBoundary1=_SnaLuRtmBoundary1_Object((1,3,6,1,2,1,34,1,3,1,1,6),_SnaLuRtmBoundary1_Type())
snaLuRtmBoundary1.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmBoundary1.setStatus(_A)
_SnaLuRtmBoundary2_Type=Integer32
_SnaLuRtmBoundary2_Object=MibTableColumn
snaLuRtmBoundary2=_SnaLuRtmBoundary2_Object((1,3,6,1,2,1,34,1,3,1,1,7),_SnaLuRtmBoundary2_Type())
snaLuRtmBoundary2.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmBoundary2.setStatus(_A)
_SnaLuRtmBoundary3_Type=Integer32
_SnaLuRtmBoundary3_Object=MibTableColumn
snaLuRtmBoundary3=_SnaLuRtmBoundary3_Object((1,3,6,1,2,1,34,1,3,1,1,8),_SnaLuRtmBoundary3_Type())
snaLuRtmBoundary3.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmBoundary3.setStatus(_A)
_SnaLuRtmBoundary4_Type=Integer32
_SnaLuRtmBoundary4_Object=MibTableColumn
snaLuRtmBoundary4=_SnaLuRtmBoundary4_Object((1,3,6,1,2,1,34,1,3,1,1,9),_SnaLuRtmBoundary4_Type())
snaLuRtmBoundary4.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmBoundary4.setStatus(_A)
_SnaLuRtmCounter1_Type=Counter32
_SnaLuRtmCounter1_Object=MibTableColumn
snaLuRtmCounter1=_SnaLuRtmCounter1_Object((1,3,6,1,2,1,34,1,3,1,1,10),_SnaLuRtmCounter1_Type())
snaLuRtmCounter1.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmCounter1.setStatus(_A)
_SnaLuRtmCounter2_Type=Counter32
_SnaLuRtmCounter2_Object=MibTableColumn
snaLuRtmCounter2=_SnaLuRtmCounter2_Object((1,3,6,1,2,1,34,1,3,1,1,11),_SnaLuRtmCounter2_Type())
snaLuRtmCounter2.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmCounter2.setStatus(_A)
_SnaLuRtmCounter3_Type=Counter32
_SnaLuRtmCounter3_Object=MibTableColumn
snaLuRtmCounter3=_SnaLuRtmCounter3_Object((1,3,6,1,2,1,34,1,3,1,1,12),_SnaLuRtmCounter3_Type())
snaLuRtmCounter3.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmCounter3.setStatus(_A)
_SnaLuRtmCounter4_Type=Counter32
_SnaLuRtmCounter4_Object=MibTableColumn
snaLuRtmCounter4=_SnaLuRtmCounter4_Object((1,3,6,1,2,1,34,1,3,1,1,13),_SnaLuRtmCounter4_Type())
snaLuRtmCounter4.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmCounter4.setStatus(_A)
_SnaLuRtmOverFlows_Type=Counter32
_SnaLuRtmOverFlows_Object=MibTableColumn
snaLuRtmOverFlows=_SnaLuRtmOverFlows_Object((1,3,6,1,2,1,34,1,3,1,1,14),_SnaLuRtmOverFlows_Type())
snaLuRtmOverFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmOverFlows.setStatus(_A)
_SnaLuRtmObjPercent_Type=Integer32
_SnaLuRtmObjPercent_Object=MibTableColumn
snaLuRtmObjPercent=_SnaLuRtmObjPercent_Object((1,3,6,1,2,1,34,1,3,1,1,15),_SnaLuRtmObjPercent_Type())
snaLuRtmObjPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmObjPercent.setStatus(_A)
class _SnaLuRtmObjRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('range1',2),('range2',3),('range3',4),('range4',5),('range5',6)))
_SnaLuRtmObjRange_Type.__name__=_D
_SnaLuRtmObjRange_Object=MibTableColumn
snaLuRtmObjRange=_SnaLuRtmObjRange_Object((1,3,6,1,2,1,34,1,3,1,1,16),_SnaLuRtmObjRange_Type())
snaLuRtmObjRange.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmObjRange.setStatus(_A)
_SnaLuRtmNumTrans_Type=Integer32
_SnaLuRtmNumTrans_Object=MibTableColumn
snaLuRtmNumTrans=_SnaLuRtmNumTrans_Object((1,3,6,1,2,1,34,1,3,1,1,17),_SnaLuRtmNumTrans_Type())
snaLuRtmNumTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmNumTrans.setStatus(_A)
_SnaLuRtmLastRspTime_Type=Integer32
_SnaLuRtmLastRspTime_Object=MibTableColumn
snaLuRtmLastRspTime=_SnaLuRtmLastRspTime_Object((1,3,6,1,2,1,34,1,3,1,1,18),_SnaLuRtmLastRspTime_Type())
snaLuRtmLastRspTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmLastRspTime.setStatus(_A)
_SnaLuRtmAvgRspTime_Type=Integer32
_SnaLuRtmAvgRspTime_Object=MibTableColumn
snaLuRtmAvgRspTime=_SnaLuRtmAvgRspTime_Object((1,3,6,1,2,1,34,1,3,1,1,19),_SnaLuRtmAvgRspTime_Type())
snaLuRtmAvgRspTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snaLuRtmAvgRspTime.setStatus(_A)
_SnanauConformance_ObjectIdentity=ObjectIdentity
snanauConformance=_SnanauConformance_ObjectIdentity((1,3,6,1,2,1,34,2))
_SnanauCompliances_ObjectIdentity=ObjectIdentity
snanauCompliances=_SnanauCompliances_ObjectIdentity((1,3,6,1,2,1,34,2,1))
_SnanauGroups_ObjectIdentity=ObjectIdentity
snanauGroups=_SnanauGroups_ObjectIdentity((1,3,6,1,2,1,34,2,2))
snaNodeAdminEntry.registerAugmentions((_B,_A2))
snaNodeOperEntry.setIndexNames(*snaNodeAdminEntry.getIndexNames())
snaNodeLinkAdminEntry.registerAugmentions((_B,_A3))
snaNodeLinkOperEntry.setIndexNames(*snaNodeLinkAdminEntry.getIndexNames())
snaLuAdminEntry.registerAugmentions((_B,_A4))
snaLuOperEntry.setIndexNames(*snaLuAdminEntry.getIndexNames())
snaLuSessnEntry.registerAugmentions((_B,_A5))
snaLuSessnStatsEntry.setIndexNames(*snaLuSessnEntry.getIndexNames())
snaNodeGroup=ObjectGroup((1,3,6,1,2,1,34,2,2,1))
snaNodeGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_O),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_P),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_V),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:snaNodeGroup.setStatus(_A)
snaLuGroup=ObjectGroup((1,3,6,1,2,1,34,2,2,2))
snaLuGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_W),(_B,_X),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Y),(_B,_Ar)))
if mibBuilder.loadTexts:snaLuGroup.setStatus(_A)
snaSessionGroup=ObjectGroup((1,3,6,1,2,1,34,2,2,3))
snaSessionGroup.setObjects(*((_B,_T),(_B,_U),(_B,_Z),(_B,_a),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_b),(_B,_c),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5)))
if mibBuilder.loadTexts:snaSessionGroup.setStatus(_A)
snaPu20Group=ObjectGroup((1,3,6,1,2,1,34,2,2,4))
snaPu20Group.setObjects(*((_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE)))
if mibBuilder.loadTexts:snaPu20Group.setStatus(_A)
snaMgtToolsRtmGroup=ObjectGroup((1,3,6,1,2,1,34,2,2,5))
snaMgtToolsRtmGroup.setObjects(*((_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV)))
if mibBuilder.loadTexts:snaMgtToolsRtmGroup.setStatus(_A)
snaNodeStateChangeTrap=NotificationType((1,3,6,1,2,1,34,1,1,10,1))
snaNodeStateChangeTrap.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:snaNodeStateChangeTrap.setStatus(_A)
snaNodeActFailTrap=NotificationType((1,3,6,1,2,1,34,1,1,10,2))
snaNodeActFailTrap.setObjects(*((_B,_O),(_B,_P),(_B,_V)))
if mibBuilder.loadTexts:snaNodeActFailTrap.setStatus(_A)
snaLuStateChangeTrap=NotificationType((1,3,6,1,2,1,34,1,2,5,1))
snaLuStateChangeTrap.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:snaLuStateChangeTrap.setStatus(_A)
snaLuSessnBindFailTrap=NotificationType((1,3,6,1,2,1,34,1,2,5,2))
snaLuSessnBindFailTrap.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:snaLuSessnBindFailTrap.setStatus(_A)
snanauCompliance=ModuleCompliance((1,3,6,1,2,1,34,2,1,1))
snanauCompliance.setObjects(*((_B,_BW),(_B,_BX),(_B,_BY),(_B,_BZ),(_B,_Ba)))
if mibBuilder.loadTexts:snanauCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'snanauMIB':snanauMIB,'snanauObjects':snanauObjects,'snaNode':snaNode,'snaNodeAdminTable':snaNodeAdminTable,'snaNodeAdminEntry':snaNodeAdminEntry,_I:snaNodeAdminIndex,_A6:snaNodeAdminName,_A7:snaNodeAdminType,_A8:snaNodeAdminXidFormat,_A9:snaNodeAdminBlockNum,_AA:snaNodeAdminIdNum,_AB:snaNodeAdminEnablingMethod,_AC:snaNodeAdminLuTermDefault,_AD:snaNodeAdminMaxLu,_AE:snaNodeAdminHostDescription,_AF:snaNodeAdminStopMethod,_AG:snaNodeAdminState,_AH:snaNodeAdminRowStatus,_AI:snaNodeAdminTableLastChange,'snaNodeOperTable':snaNodeOperTable,_A2:snaNodeOperEntry,_O:snaNodeOperName,_AJ:snaNodeOperType,_AK:snaNodeOperXidFormat,_AL:snaNodeOperBlockNum,_AM:snaNodeOperIdNum,_AN:snaNodeOperEnablingMethod,_AO:snaNodeOperLuTermDefault,_AP:snaNodeOperMaxLu,_AQ:snaNodeOperHostDescription,_AR:snaNodeOperStopMethod,_P:snaNodeOperState,_AS:snaNodeOperHostSscpId,_AT:snaNodeOperStartTime,_AU:snaNodeOperLastStateChange,_AV:snaNodeOperActFailures,_V:snaNodeOperActFailureReason,_AW:snaNodeOperTableLastChange,'snaPu20StatsTable':snaPu20StatsTable,'snaPu20StatsEntry':snaPu20StatsEntry,_B6:snaPu20StatsSentBytes,_B7:snaPu20StatsReceivedBytes,_B8:snaPu20StatsSentPius,_B9:snaPu20StatsReceivedPius,_BA:snaPu20StatsSentNegativeResps,_BB:snaPu20StatsReceivedNegativeResps,_BC:snaPu20StatsActLus,_BD:snaPu20StatsInActLus,_BE:snaPu20StatsBindLus,'snaNodeLinkAdminTable':snaNodeLinkAdminTable,'snaNodeLinkAdminEntry':snaNodeLinkAdminEntry,_m:snaNodeLinkAdminIndex,_AX:snaNodeLinkAdminSpecific,_AY:snaNodeLinkAdminMaxPiu,_AZ:snaNodeLinkAdminRowStatus,_Aa:snaNodeLinkAdminTableLastChange,'snaNodeLinkOperTable':snaNodeLinkOperTable,_A3:snaNodeLinkOperEntry,_Ab:snaNodeLinkOperSpecific,_Ac:snaNodeLinkOperMaxPiu,_Ad:snaNodeLinkOperTableLastChange,'snaNodeTraps':snaNodeTraps,'snaNodeStateChangeTrap':snaNodeStateChangeTrap,'snaNodeActFailTrap':snaNodeActFailTrap,'snaLu':snaLu,'snaLuAdminTable':snaLuAdminTable,'snaLuAdminEntry':snaLuAdminEntry,_S:snaLuAdminLuIndex,_Ae:snaLuAdminName,_Af:snaLuAdminSnaName,_Ag:snaLuAdminType,_Ah:snaLuAdminDepType,_Ai:snaLuAdminLocalAddress,_Aj:snaLuAdminDisplayModel,_Ak:snaLuAdminTerm,_Al:snaLuAdminRowStatus,'snaLuOperTable':snaLuOperTable,_A4:snaLuOperEntry,_W:snaLuOperName,_X:snaLuOperSnaName,_Am:snaLuOperType,_An:snaLuOperDepType,_Ao:snaLuOperLocalAddress,_Ap:snaLuOperDisplayModel,_Aq:snaLuOperTerm,_Y:snaLuOperState,_Ar:snaLuOperSessnCount,'snaLuSessnTable':snaLuSessnTable,'snaLuSessnEntry':snaLuSessnEntry,_T:snaLuSessnRluIndex,_U:snaLuSessnIndex,_Z:snaLuSessnLocalApplName,_a:snaLuSessnRemoteLuName,_As:snaLuSessnMaxSndRuSize,_At:snaLuSessnMaxRcvRuSize,_Au:snaLuSessnSndPacingSize,_Av:snaLuSessnRcvPacingSize,_Aw:snaLuSessnActiveTime,_Ax:snaLuSessnAdminState,_b:snaLuSessnOperState,_c:snaLuSessnSenseData,_Ay:snaLuSessnTerminationRu,_Az:snaLuSessnUnbindType,_A_:snaLuSessnLinkIndex,'snaLuSessnStatsTable':snaLuSessnStatsTable,_A5:snaLuSessnStatsEntry,_B0:snaLuSessnStatsSentBytes,_B1:snaLuSessnStatsReceivedBytes,_B2:snaLuSessnStatsSentRus,_B3:snaLuSessnStatsReceivedRus,_B4:snaLuSessnStatsSentNegativeResps,_B5:snaLuSessnStatsReceivedNegativeResps,'snaLuTraps':snaLuTraps,'snaLuStateChangeTrap':snaLuStateChangeTrap,'snaLuSessnBindFailTrap':snaLuSessnBindFailTrap,'snaMgtTools':snaMgtTools,'snaLuRtmTable':snaLuRtmTable,'snaLuRtmEntry':snaLuRtmEntry,_A0:snaLuRtmPuIndex,_A1:snaLuRtmLuIndex,_BF:snaLuRtmState,_BG:snaLuRtmStateTime,_BH:snaLuRtmDef,_BI:snaLuRtmBoundary1,_BJ:snaLuRtmBoundary2,_BK:snaLuRtmBoundary3,_BL:snaLuRtmBoundary4,_BM:snaLuRtmCounter1,_BN:snaLuRtmCounter2,_BO:snaLuRtmCounter3,_BP:snaLuRtmCounter4,_BQ:snaLuRtmOverFlows,_BR:snaLuRtmObjPercent,_BS:snaLuRtmObjRange,_BT:snaLuRtmNumTrans,_BU:snaLuRtmLastRspTime,_BV:snaLuRtmAvgRspTime,'snanauConformance':snanauConformance,'snanauCompliances':snanauCompliances,'snanauCompliance':snanauCompliance,'snanauGroups':snanauGroups,_BW:snaNodeGroup,_BX:snaLuGroup,_BY:snaSessionGroup,_BZ:snaPu20Group,_Ba:snaMgtToolsRtmGroup})