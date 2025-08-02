_AG='ttdpStatsGroup'
_AF='ttdpBasicGroup'
_AE='ttdpTopoReceivedFrames'
_AD='ttdpTopoSentFrames'
_AC='ttdpLocalFastModeCnt'
_AB='ttdpRemoteFastModeCnt'
_AA='ttdpHelloReceivedFrames'
_A9='ttdpHelloSentFrames'
_A8='ttdpLineRcvState'
_A7='ttdpPeerLineId'
_A6='ttdpActivePhysLinesNb'
_A5='ttdpConfiguredPhysLinesNb'
_A4='ttdpEtbTopoCnt'
_A3='ttdpEtbTopoCntValid'
_A2='ttdpCnEtbnId'
_A1='ttdpSubnetIpMask'
_A0='ttdpSubnetIpAddr'
_z='ttdpSubnetId'
_y='ttdpCnId'
_x='ttdpCnType'
_w='ttdpCstEtbnCnt'
_v='ttdpCstCnCnt'
_u='ttdpCstOrientation'
_t='ttdpCstUuid'
_s='ttdpCstCnt'
_r='ttdpEtbnVectorMacAddr'
_q='ttdpEtbnDirCnt'
_p='ttdpNeighbourMacAddr'
_o='ttdpShorten'
_n='ttdpLengthen'
_m='ttdpConnTableCrc32'
_l='ttdpRemoteInhibit'
_k='ttdpEtbnInhibit'
_j='ttdpEtbnInaugState'
_i='ttdpEtbnNodeRole'
_h='ttdpEtbnIpAddr'
_g='ttdpEtbnOrientation'
_f='ttdpEtbnMacAddr'
_e='ttdpEtbnId'
_d='ttdpEtbnCnt'
_c='ttdpConnTableValid'
_b='ttdpIsAlone'
_a='ttdpNodePosition'
_Z='ttdpLocalEtbnId'
_Y='ttdpLocalEtbnMacAddr'
_X='ttdpEtbId'
_W='ttdpPortState'
_V='ttdpIsEndLink'
_U='ttdpLogicalLinksNb'
_T='ttdpGlobalTopoTimeout'
_S='ttdpTopoTtl'
_R='ttdpFastTimeout'
_Q='ttdpSlowTimeout'
_P='ttdpVersion'
_O='OctetString'
_N='ttdpCnEtbnTableIdx'
_M='ttdpEtbnVectorIdx'
_L='undefined'
_K='ttdpCstCnTableIdx'
_J='ttdpConnectTableIdx'
_I='ttdpPhysicalLinesIdx'
_H='ttdpCstTableIdx'
_G='ttdpEtbnTableIdx'
_F='ttdpLogicalLinksIdx'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='TTDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
iec61375=ModuleIdentity((1,0,61375,2))
if mibBuilder.loadTexts:iec61375.setRevisions(('2016-06-10 00:00',))
class TtdpPhysicalLineId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(45,65,66,67,68)));namedValues=NamedValues(*(('lineNone',45),('lineA',65),('lineB',66),('lineC',67),('lineD',68)))
class TtdpOrientation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('direct',1),('inverse',2),(_L,3)))
class Antivalent2(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('error',0),('false',1),('true',2),(_L,3)))
class TtdpDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dir1',1),('dir2',2)))
_Std_ObjectIdentity=ObjectIdentity
std=_Std_ObjectIdentity((1,0))
_Stdx61375_ObjectIdentity=ObjectIdentity
stdx61375=_Stdx61375_ObjectIdentity((1,0,61375))
_Ttdp_ObjectIdentity=ObjectIdentity
ttdp=_Ttdp_ObjectIdentity((1,0,61375,2,5))
_TtdpObjects_ObjectIdentity=ObjectIdentity
ttdpObjects=_TtdpObjects_ObjectIdentity((1,0,61375,2,5,1))
_TtdpGenInfo_ObjectIdentity=ObjectIdentity
ttdpGenInfo=_TtdpGenInfo_ObjectIdentity((1,0,61375,2,5,1,1))
_TtdpVersion_Type=Unsigned32
_TtdpVersion_Object=MibScalar
ttdpVersion=_TtdpVersion_Object((1,0,61375,2,5,1,1,1),_TtdpVersion_Type())
ttdpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpVersion.setStatus(_A)
_TtdpSlowTimeout_Type=Unsigned32
_TtdpSlowTimeout_Object=MibScalar
ttdpSlowTimeout=_TtdpSlowTimeout_Object((1,0,61375,2,5,1,1,2),_TtdpSlowTimeout_Type())
ttdpSlowTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpSlowTimeout.setStatus(_A)
_TtdpFastTimeout_Type=Unsigned32
_TtdpFastTimeout_Object=MibScalar
ttdpFastTimeout=_TtdpFastTimeout_Object((1,0,61375,2,5,1,1,3),_TtdpFastTimeout_Type())
ttdpFastTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpFastTimeout.setStatus(_A)
_TtdpTopoTtl_Type=Unsigned32
_TtdpTopoTtl_Object=MibScalar
ttdpTopoTtl=_TtdpTopoTtl_Object((1,0,61375,2,5,1,1,4),_TtdpTopoTtl_Type())
ttdpTopoTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpTopoTtl.setStatus(_A)
_TtdpGlobalTopoTimeout_Type=Unsigned32
_TtdpGlobalTopoTimeout_Object=MibScalar
ttdpGlobalTopoTimeout=_TtdpGlobalTopoTimeout_Object((1,0,61375,2,5,1,1,5),_TtdpGlobalTopoTimeout_Type())
ttdpGlobalTopoTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpGlobalTopoTimeout.setStatus(_A)
_TtdpLinksInfo_ObjectIdentity=ObjectIdentity
ttdpLinksInfo=_TtdpLinksInfo_ObjectIdentity((1,0,61375,2,5,1,3))
class _TtdpLogicalLinksNb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2))
_TtdpLogicalLinksNb_Type.__name__=_D
_TtdpLogicalLinksNb_Object=MibScalar
ttdpLogicalLinksNb=_TtdpLogicalLinksNb_Object((1,0,61375,2,5,1,3,1),_TtdpLogicalLinksNb_Type())
ttdpLogicalLinksNb.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLogicalLinksNb.setStatus(_A)
_TtdpLogicalLinksTable_Object=MibTable
ttdpLogicalLinksTable=_TtdpLogicalLinksTable_Object((1,0,61375,2,5,1,3,2))
if mibBuilder.loadTexts:ttdpLogicalLinksTable.setStatus(_A)
_TtdpLogicalLinksEntry_Object=MibTableRow
ttdpLogicalLinksEntry=_TtdpLogicalLinksEntry_Object((1,0,61375,2,5,1,3,2,1))
ttdpLogicalLinksEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ttdpLogicalLinksEntry.setStatus(_A)
_TtdpLogicalLinksIdx_Type=TtdpDirection
_TtdpLogicalLinksIdx_Object=MibTableColumn
ttdpLogicalLinksIdx=_TtdpLogicalLinksIdx_Object((1,0,61375,2,5,1,3,2,1,1),_TtdpLogicalLinksIdx_Type())
ttdpLogicalLinksIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLogicalLinksIdx.setStatus(_A)
class _TtdpConfiguredPhysLinesNb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TtdpConfiguredPhysLinesNb_Type.__name__=_D
_TtdpConfiguredPhysLinesNb_Object=MibTableColumn
ttdpConfiguredPhysLinesNb=_TtdpConfiguredPhysLinesNb_Object((1,0,61375,2,5,1,3,2,1,2),_TtdpConfiguredPhysLinesNb_Type())
ttdpConfiguredPhysLinesNb.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpConfiguredPhysLinesNb.setStatus(_A)
class _TtdpActivePhysLinesNb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_TtdpActivePhysLinesNb_Type.__name__=_D
_TtdpActivePhysLinesNb_Object=MibTableColumn
ttdpActivePhysLinesNb=_TtdpActivePhysLinesNb_Object((1,0,61375,2,5,1,3,2,1,3),_TtdpActivePhysLinesNb_Type())
ttdpActivePhysLinesNb.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpActivePhysLinesNb.setStatus(_A)
_TtdpIsEndLink_Type=TruthValue
_TtdpIsEndLink_Object=MibTableColumn
ttdpIsEndLink=_TtdpIsEndLink_Object((1,0,61375,2,5,1,3,2,1,4),_TtdpIsEndLink_Type())
ttdpIsEndLink.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpIsEndLink.setStatus(_A)
_TtdpPhysicalLinesTable_Object=MibTable
ttdpPhysicalLinesTable=_TtdpPhysicalLinesTable_Object((1,0,61375,2,5,1,3,3))
if mibBuilder.loadTexts:ttdpPhysicalLinesTable.setStatus(_A)
_TtdpPhysicalLinesEntry_Object=MibTableRow
ttdpPhysicalLinesEntry=_TtdpPhysicalLinesEntry_Object((1,0,61375,2,5,1,3,3,1))
ttdpPhysicalLinesEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:ttdpPhysicalLinesEntry.setStatus(_A)
_TtdpPhysicalLinesIdx_Type=TtdpPhysicalLineId
_TtdpPhysicalLinesIdx_Object=MibTableColumn
ttdpPhysicalLinesIdx=_TtdpPhysicalLinesIdx_Object((1,0,61375,2,5,1,3,3,1,1),_TtdpPhysicalLinesIdx_Type())
ttdpPhysicalLinesIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpPhysicalLinesIdx.setStatus(_A)
class _TtdpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('disabled',0),('forwarding',2),('discarding',3)))
_TtdpPortState_Type.__name__=_E
_TtdpPortState_Object=MibTableColumn
ttdpPortState=_TtdpPortState_Object((1,0,61375,2,5,1,3,3,1,2),_TtdpPortState_Type())
ttdpPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpPortState.setStatus(_A)
class _TtdpLineRcvState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lineNotOK',1),('lineOK',2),('notAvailable',3)))
_TtdpLineRcvState_Type.__name__=_E
_TtdpLineRcvState_Object=MibTableColumn
ttdpLineRcvState=_TtdpLineRcvState_Object((1,0,61375,2,5,1,3,3,1,3),_TtdpLineRcvState_Type())
ttdpLineRcvState.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLineRcvState.setStatus(_A)
_TtdpPeerLineId_Type=TtdpPhysicalLineId
_TtdpPeerLineId_Object=MibTableColumn
ttdpPeerLineId=_TtdpPeerLineId_Object((1,0,61375,2,5,1,3,3,1,4),_TtdpPeerLineId_Type())
ttdpPeerLineId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpPeerLineId.setStatus(_A)
_TtdpPhysicalLinesStatsTable_Object=MibTable
ttdpPhysicalLinesStatsTable=_TtdpPhysicalLinesStatsTable_Object((1,0,61375,2,5,1,3,4))
if mibBuilder.loadTexts:ttdpPhysicalLinesStatsTable.setStatus(_A)
_TtdpPhysicalLinesStatsEntry_Object=MibTableRow
ttdpPhysicalLinesStatsEntry=_TtdpPhysicalLinesStatsEntry_Object((1,0,61375,2,5,1,3,4,1))
ttdpPhysicalLinesStatsEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:ttdpPhysicalLinesStatsEntry.setStatus(_A)
_TtdpHelloSentFrames_Type=Integer32
_TtdpHelloSentFrames_Object=MibTableColumn
ttdpHelloSentFrames=_TtdpHelloSentFrames_Object((1,0,61375,2,5,1,3,4,1,1),_TtdpHelloSentFrames_Type())
ttdpHelloSentFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpHelloSentFrames.setStatus(_A)
_TtdpHelloReceivedFrames_Type=Integer32
_TtdpHelloReceivedFrames_Object=MibTableColumn
ttdpHelloReceivedFrames=_TtdpHelloReceivedFrames_Object((1,0,61375,2,5,1,3,4,1,2),_TtdpHelloReceivedFrames_Type())
ttdpHelloReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpHelloReceivedFrames.setStatus(_A)
_TtdpRemoteFastModeCnt_Type=Integer32
_TtdpRemoteFastModeCnt_Object=MibTableColumn
ttdpRemoteFastModeCnt=_TtdpRemoteFastModeCnt_Object((1,0,61375,2,5,1,3,4,1,3),_TtdpRemoteFastModeCnt_Type())
ttdpRemoteFastModeCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpRemoteFastModeCnt.setStatus(_A)
_TtdpLocalFastModeCnt_Type=Integer32
_TtdpLocalFastModeCnt_Object=MibTableColumn
ttdpLocalFastModeCnt=_TtdpLocalFastModeCnt_Object((1,0,61375,2,5,1,3,4,1,4),_TtdpLocalFastModeCnt_Type())
ttdpLocalFastModeCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLocalFastModeCnt.setStatus(_A)
_TtdpTopoInfo_ObjectIdentity=ObjectIdentity
ttdpTopoInfo=_TtdpTopoInfo_ObjectIdentity((1,0,61375,2,5,1,5))
_TtdpLocalEtbnInfo_ObjectIdentity=ObjectIdentity
ttdpLocalEtbnInfo=_TtdpLocalEtbnInfo_ObjectIdentity((1,0,61375,2,5,1,5,1))
class _TtdpEtbId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_TtdpEtbId_Type.__name__=_D
_TtdpEtbId_Object=MibScalar
ttdpEtbId=_TtdpEtbId_Object((1,0,61375,2,5,1,5,1,1),_TtdpEtbId_Type())
ttdpEtbId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbId.setStatus(_A)
_TtdpLocalEtbnMacAddr_Type=MacAddress
_TtdpLocalEtbnMacAddr_Object=MibScalar
ttdpLocalEtbnMacAddr=_TtdpLocalEtbnMacAddr_Object((1,0,61375,2,5,1,5,1,2),_TtdpLocalEtbnMacAddr_Type())
ttdpLocalEtbnMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLocalEtbnMacAddr.setStatus(_A)
class _TtdpLocalEtbnId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdpLocalEtbnId_Type.__name__=_D
_TtdpLocalEtbnId_Object=MibScalar
ttdpLocalEtbnId=_TtdpLocalEtbnId_Object((1,0,61375,2,5,1,5,1,3),_TtdpLocalEtbnId_Type())
ttdpLocalEtbnId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLocalEtbnId.setStatus(_A)
class _TtdpNodePosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('intermediate',0),('extremity1',1),('extremity2',2)))
_TtdpNodePosition_Type.__name__=_E
_TtdpNodePosition_Object=MibScalar
ttdpNodePosition=_TtdpNodePosition_Object((1,0,61375,2,5,1,5,1,4),_TtdpNodePosition_Type())
ttdpNodePosition.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpNodePosition.setStatus(_A)
_TtdpIsAlone_Type=TruthValue
_TtdpIsAlone_Object=MibScalar
ttdpIsAlone=_TtdpIsAlone_Object((1,0,61375,2,5,1,5,1,5),_TtdpIsAlone_Type())
ttdpIsAlone.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpIsAlone.setStatus(_A)
_TtdpConnTableValid_Type=TruthValue
_TtdpConnTableValid_Object=MibScalar
ttdpConnTableValid=_TtdpConnTableValid_Object((1,0,61375,2,5,1,5,1,6),_TtdpConnTableValid_Type())
ttdpConnTableValid.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpConnTableValid.setStatus(_A)
_TtdpEtbTopoCntValid_Type=TruthValue
_TtdpEtbTopoCntValid_Object=MibScalar
ttdpEtbTopoCntValid=_TtdpEtbTopoCntValid_Object((1,0,61375,2,5,1,5,1,7),_TtdpEtbTopoCntValid_Type())
ttdpEtbTopoCntValid.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbTopoCntValid.setStatus(_A)
_TtdpTopoFrameStats_ObjectIdentity=ObjectIdentity
ttdpTopoFrameStats=_TtdpTopoFrameStats_ObjectIdentity((1,0,61375,2,5,1,5,1,8))
_TtdpTopoSentFrames_Type=Integer32
_TtdpTopoSentFrames_Object=MibScalar
ttdpTopoSentFrames=_TtdpTopoSentFrames_Object((1,0,61375,2,5,1,5,1,8,1),_TtdpTopoSentFrames_Type())
ttdpTopoSentFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpTopoSentFrames.setStatus(_A)
_TtdpTopoReceivedFrames_Type=Integer32
_TtdpTopoReceivedFrames_Object=MibScalar
ttdpTopoReceivedFrames=_TtdpTopoReceivedFrames_Object((1,0,61375,2,5,1,5,1,8,2),_TtdpTopoReceivedFrames_Type())
ttdpTopoReceivedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpTopoReceivedFrames.setStatus(_A)
class _TtdpEtbnCnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdpEtbnCnt_Type.__name__=_D
_TtdpEtbnCnt_Object=MibScalar
ttdpEtbnCnt=_TtdpEtbnCnt_Object((1,0,61375,2,5,1,5,2),_TtdpEtbnCnt_Type())
ttdpEtbnCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnCnt.setStatus(_A)
_TtdpEtbnTable_Object=MibTable
ttdpEtbnTable=_TtdpEtbnTable_Object((1,0,61375,2,5,1,5,3))
if mibBuilder.loadTexts:ttdpEtbnTable.setStatus(_A)
_TtdpEtbnEntry_Object=MibTableRow
ttdpEtbnEntry=_TtdpEtbnEntry_Object((1,0,61375,2,5,1,5,3,1))
ttdpEtbnEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ttdpEtbnEntry.setStatus(_A)
class _TtdpEtbnTableIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdpEtbnTableIdx_Type.__name__=_D
_TtdpEtbnTableIdx_Object=MibTableColumn
ttdpEtbnTableIdx=_TtdpEtbnTableIdx_Object((1,0,61375,2,5,1,5,3,1,1),_TtdpEtbnTableIdx_Type())
ttdpEtbnTableIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnTableIdx.setStatus(_A)
class _TtdpEtbnId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_TtdpEtbnId_Type.__name__=_D
_TtdpEtbnId_Object=MibTableColumn
ttdpEtbnId=_TtdpEtbnId_Object((1,0,61375,2,5,1,5,3,1,2),_TtdpEtbnId_Type())
ttdpEtbnId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnId.setStatus(_A)
_TtdpEtbnMacAddr_Type=MacAddress
_TtdpEtbnMacAddr_Object=MibTableColumn
ttdpEtbnMacAddr=_TtdpEtbnMacAddr_Object((1,0,61375,2,5,1,5,3,1,3),_TtdpEtbnMacAddr_Type())
ttdpEtbnMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnMacAddr.setStatus(_A)
_TtdpEtbnOrientation_Type=TtdpOrientation
_TtdpEtbnOrientation_Object=MibTableColumn
ttdpEtbnOrientation=_TtdpEtbnOrientation_Object((1,0,61375,2,5,1,5,3,1,4),_TtdpEtbnOrientation_Type())
ttdpEtbnOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnOrientation.setStatus(_A)
_TtdpEtbnIpAddr_Type=IpAddress
_TtdpEtbnIpAddr_Object=MibTableColumn
ttdpEtbnIpAddr=_TtdpEtbnIpAddr_Object((1,0,61375,2,5,1,5,3,1,5),_TtdpEtbnIpAddr_Type())
ttdpEtbnIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnIpAddr.setStatus(_A)
class _TtdpEtbnNodeRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),('master',1),('backup',2),('notRedundant',3)))
_TtdpEtbnNodeRole_Type.__name__=_E
_TtdpEtbnNodeRole_Object=MibTableColumn
ttdpEtbnNodeRole=_TtdpEtbnNodeRole_Object((1,0,61375,2,5,1,5,3,1,6),_TtdpEtbnNodeRole_Type())
ttdpEtbnNodeRole.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnNodeRole.setStatus(_A)
class _TtdpEtbnInaugState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('init',0),('notInaugurated',1),('inaugurated',2),('readyForInauguration',3)))
_TtdpEtbnInaugState_Type.__name__=_E
_TtdpEtbnInaugState_Object=MibTableColumn
ttdpEtbnInaugState=_TtdpEtbnInaugState_Object((1,0,61375,2,5,1,5,3,1,7),_TtdpEtbnInaugState_Type())
ttdpEtbnInaugState.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnInaugState.setStatus(_A)
_TtdpEtbnInhibit_Type=TruthValue
_TtdpEtbnInhibit_Object=MibTableColumn
ttdpEtbnInhibit=_TtdpEtbnInhibit_Object((1,0,61375,2,5,1,5,3,1,8),_TtdpEtbnInhibit_Type())
ttdpEtbnInhibit.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnInhibit.setStatus(_A)
_TtdpRemoteInhibit_Type=TruthValue
_TtdpRemoteInhibit_Object=MibTableColumn
ttdpRemoteInhibit=_TtdpRemoteInhibit_Object((1,0,61375,2,5,1,5,3,1,9),_TtdpRemoteInhibit_Type())
ttdpRemoteInhibit.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpRemoteInhibit.setStatus(_A)
_TtdpConnTableCrc32_Type=Unsigned32
_TtdpConnTableCrc32_Object=MibTableColumn
ttdpConnTableCrc32=_TtdpConnTableCrc32_Object((1,0,61375,2,5,1,5,3,1,10),_TtdpConnTableCrc32_Type())
ttdpConnTableCrc32.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpConnTableCrc32.setStatus(_A)
_TtdpEtbTopoCnt_Type=Unsigned32
_TtdpEtbTopoCnt_Object=MibTableColumn
ttdpEtbTopoCnt=_TtdpEtbTopoCnt_Object((1,0,61375,2,5,1,5,3,1,11),_TtdpEtbTopoCnt_Type())
ttdpEtbTopoCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbTopoCnt.setStatus(_A)
_TtdpLengthen_Type=Antivalent2
_TtdpLengthen_Object=MibTableColumn
ttdpLengthen=_TtdpLengthen_Object((1,0,61375,2,5,1,5,3,1,12),_TtdpLengthen_Type())
ttdpLengthen.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpLengthen.setStatus(_A)
_TtdpShorten_Type=Antivalent2
_TtdpShorten_Object=MibTableColumn
ttdpShorten=_TtdpShorten_Object((1,0,61375,2,5,1,5,3,1,13),_TtdpShorten_Type())
ttdpShorten.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpShorten.setStatus(_A)
_TtdpConnectTable_Object=MibTable
ttdpConnectTable=_TtdpConnectTable_Object((1,0,61375,2,5,1,5,4))
if mibBuilder.loadTexts:ttdpConnectTable.setStatus(_A)
_TtdpConnectEntry_Object=MibTableRow
ttdpConnectEntry=_TtdpConnectEntry_Object((1,0,61375,2,5,1,5,4,1))
ttdpConnectEntry.setIndexNames((0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:ttdpConnectEntry.setStatus(_A)
_TtdpConnectTableIdx_Type=TtdpDirection
_TtdpConnectTableIdx_Object=MibTableColumn
ttdpConnectTableIdx=_TtdpConnectTableIdx_Object((1,0,61375,2,5,1,5,4,1,1),_TtdpConnectTableIdx_Type())
ttdpConnectTableIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpConnectTableIdx.setStatus(_A)
_TtdpNeighbourMacAddr_Type=MacAddress
_TtdpNeighbourMacAddr_Object=MibTableColumn
ttdpNeighbourMacAddr=_TtdpNeighbourMacAddr_Object((1,0,61375,2,5,1,5,4,1,2),_TtdpNeighbourMacAddr_Type())
ttdpNeighbourMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpNeighbourMacAddr.setStatus(_A)
class _TtdpEtbnDirCnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_TtdpEtbnDirCnt_Type.__name__=_D
_TtdpEtbnDirCnt_Object=MibTableColumn
ttdpEtbnDirCnt=_TtdpEtbnDirCnt_Object((1,0,61375,2,5,1,5,4,1,3),_TtdpEtbnDirCnt_Type())
ttdpEtbnDirCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnDirCnt.setStatus(_A)
_TtdpEtbnVectorTable_Object=MibTable
ttdpEtbnVectorTable=_TtdpEtbnVectorTable_Object((1,0,61375,2,5,1,5,5))
if mibBuilder.loadTexts:ttdpEtbnVectorTable.setStatus(_A)
_TtdpEtbnVectorEntry_Object=MibTableRow
ttdpEtbnVectorEntry=_TtdpEtbnVectorEntry_Object((1,0,61375,2,5,1,5,5,1))
ttdpEtbnVectorEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_M))
if mibBuilder.loadTexts:ttdpEtbnVectorEntry.setStatus(_A)
class _TtdpEtbnVectorIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,62))
_TtdpEtbnVectorIdx_Type.__name__=_D
_TtdpEtbnVectorIdx_Object=MibTableColumn
ttdpEtbnVectorIdx=_TtdpEtbnVectorIdx_Object((1,0,61375,2,5,1,5,5,1,1),_TtdpEtbnVectorIdx_Type())
ttdpEtbnVectorIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnVectorIdx.setStatus(_A)
_TtdpEtbnVectorMacAddr_Type=MacAddress
_TtdpEtbnVectorMacAddr_Object=MibTableColumn
ttdpEtbnVectorMacAddr=_TtdpEtbnVectorMacAddr_Object((1,0,61375,2,5,1,5,5,1,2),_TtdpEtbnVectorMacAddr_Type())
ttdpEtbnVectorMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpEtbnVectorMacAddr.setStatus(_A)
class _TtdpCstCnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_TtdpCstCnt_Type.__name__=_D
_TtdpCstCnt_Object=MibScalar
ttdpCstCnt=_TtdpCstCnt_Object((1,0,61375,2,5,1,5,6),_TtdpCstCnt_Type())
ttdpCstCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstCnt.setStatus(_A)
_TtdpCstTable_Object=MibTable
ttdpCstTable=_TtdpCstTable_Object((1,0,61375,2,5,1,5,7))
if mibBuilder.loadTexts:ttdpCstTable.setStatus(_A)
_TtdpCstEntry_Object=MibTableRow
ttdpCstEntry=_TtdpCstEntry_Object((1,0,61375,2,5,1,5,7,1))
ttdpCstEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ttdpCstEntry.setStatus(_A)
class _TtdpCstTableIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_TtdpCstTableIdx_Type.__name__=_D
_TtdpCstTableIdx_Object=MibTableColumn
ttdpCstTableIdx=_TtdpCstTableIdx_Object((1,0,61375,2,5,1,5,7,1,1),_TtdpCstTableIdx_Type())
ttdpCstTableIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstTableIdx.setStatus(_A)
class _TtdpCstUuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_TtdpCstUuid_Type.__name__=_O
_TtdpCstUuid_Object=MibTableColumn
ttdpCstUuid=_TtdpCstUuid_Object((1,0,61375,2,5,1,5,7,1,2),_TtdpCstUuid_Type())
ttdpCstUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstUuid.setStatus(_A)
_TtdpCstOrientation_Type=TtdpOrientation
_TtdpCstOrientation_Object=MibTableColumn
ttdpCstOrientation=_TtdpCstOrientation_Object((1,0,61375,2,5,1,5,7,1,3),_TtdpCstOrientation_Type())
ttdpCstOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstOrientation.setStatus(_A)
class _TtdpCstCnCnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_TtdpCstCnCnt_Type.__name__=_D
_TtdpCstCnCnt_Object=MibTableColumn
ttdpCstCnCnt=_TtdpCstCnCnt_Object((1,0,61375,2,5,1,5,7,1,4),_TtdpCstCnCnt_Type())
ttdpCstCnCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstCnCnt.setStatus(_A)
class _TtdpCstEtbnCnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_TtdpCstEtbnCnt_Type.__name__=_D
_TtdpCstEtbnCnt_Object=MibTableColumn
ttdpCstEtbnCnt=_TtdpCstEtbnCnt_Object((1,0,61375,2,5,1,5,7,1,5),_TtdpCstEtbnCnt_Type())
ttdpCstEtbnCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstEtbnCnt.setStatus(_A)
_TtdpCstCnTable_Object=MibTable
ttdpCstCnTable=_TtdpCstCnTable_Object((1,0,61375,2,5,1,5,8))
if mibBuilder.loadTexts:ttdpCstCnTable.setStatus(_A)
_TtdpCstCnEntry_Object=MibTableRow
ttdpCstCnEntry=_TtdpCstCnEntry_Object((1,0,61375,2,5,1,5,8,1))
ttdpCstCnEntry.setIndexNames((0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:ttdpCstCnEntry.setStatus(_A)
class _TtdpCstCnTableIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_TtdpCstCnTableIdx_Type.__name__=_D
_TtdpCstCnTableIdx_Object=MibTableColumn
ttdpCstCnTableIdx=_TtdpCstCnTableIdx_Object((1,0,61375,2,5,1,5,8,1,1),_TtdpCstCnTableIdx_Type())
ttdpCstCnTableIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCstCnTableIdx.setStatus(_A)
class _TtdpCnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mvb',1),('notUsed',2),('can',3),('ethernet',4)))
_TtdpCnType_Type.__name__=_E
_TtdpCnType_Object=MibTableColumn
ttdpCnType=_TtdpCnType_Object((1,0,61375,2,5,1,5,8,1,2),_TtdpCnType_Type())
ttdpCnType.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCnType.setStatus(_A)
class _TtdpCnId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_TtdpCnId_Type.__name__=_D
_TtdpCnId_Object=MibTableColumn
ttdpCnId=_TtdpCnId_Object((1,0,61375,2,5,1,5,8,1,3),_TtdpCnId_Type())
ttdpCnId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCnId.setStatus(_A)
class _TtdpSubnetId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdpSubnetId_Type.__name__=_D
_TtdpSubnetId_Object=MibTableColumn
ttdpSubnetId=_TtdpSubnetId_Object((1,0,61375,2,5,1,5,8,1,4),_TtdpSubnetId_Type())
ttdpSubnetId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpSubnetId.setStatus(_A)
_TtdpSubnetIpAddr_Type=IpAddress
_TtdpSubnetIpAddr_Object=MibTableColumn
ttdpSubnetIpAddr=_TtdpSubnetIpAddr_Object((1,0,61375,2,5,1,5,8,1,5),_TtdpSubnetIpAddr_Type())
ttdpSubnetIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpSubnetIpAddr.setStatus(_A)
_TtdpSubnetIpMask_Type=IpAddress
_TtdpSubnetIpMask_Object=MibTableColumn
ttdpSubnetIpMask=_TtdpSubnetIpMask_Object((1,0,61375,2,5,1,5,8,1,6),_TtdpSubnetIpMask_Type())
ttdpSubnetIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpSubnetIpMask.setStatus(_A)
_TtdpCnEtbnTable_Object=MibTable
ttdpCnEtbnTable=_TtdpCnEtbnTable_Object((1,0,61375,2,5,1,5,9))
if mibBuilder.loadTexts:ttdpCnEtbnTable.setStatus(_A)
_TtdpCnEtbnEntry_Object=MibTableRow
ttdpCnEtbnEntry=_TtdpCnEtbnEntry_Object((1,0,61375,2,5,1,5,9,1))
ttdpCnEtbnEntry.setIndexNames((0,_B,_H),(0,_B,_K),(0,_B,_N))
if mibBuilder.loadTexts:ttdpCnEtbnEntry.setStatus(_A)
class _TtdpCnEtbnTableIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdpCnEtbnTableIdx_Type.__name__=_D
_TtdpCnEtbnTableIdx_Object=MibTableColumn
ttdpCnEtbnTableIdx=_TtdpCnEtbnTableIdx_Object((1,0,61375,2,5,1,5,9,1,1),_TtdpCnEtbnTableIdx_Type())
ttdpCnEtbnTableIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCnEtbnTableIdx.setStatus(_A)
class _TtdpCnEtbnId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdpCnEtbnId_Type.__name__=_D
_TtdpCnEtbnId_Object=MibTableColumn
ttdpCnEtbnId=_TtdpCnEtbnId_Object((1,0,61375,2,5,1,5,9,1,2),_TtdpCnEtbnId_Type())
ttdpCnEtbnId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdpCnEtbnId.setStatus(_A)
_TtdpConformance_ObjectIdentity=ObjectIdentity
ttdpConformance=_TtdpConformance_ObjectIdentity((1,0,61375,2,5,2))
ttdpBasicGroup=ObjectGroup((1,0,61375,2,5,2,2))
ttdpBasicGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_F),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_G),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_J),(_B,_p),(_B,_q),(_B,_M),(_B,_r),(_B,_s),(_B,_H),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_K),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_N),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_I),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ttdpBasicGroup.setStatus(_A)
ttdpStatsGroup=ObjectGroup((1,0,61375,2,5,2,3))
ttdpStatsGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:ttdpStatsGroup.setStatus(_A)
ttdpBasicCompliance=ModuleCompliance((1,0,61375,2,5,2,4))
ttdpBasicCompliance.setObjects((_B,_AF))
if mibBuilder.loadTexts:ttdpBasicCompliance.setStatus(_A)
ttdpStatsCompliance=ModuleCompliance((1,0,61375,2,5,2,5))
ttdpStatsCompliance.setObjects((_B,_AG))
if mibBuilder.loadTexts:ttdpStatsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TtdpPhysicalLineId':TtdpPhysicalLineId,'TtdpOrientation':TtdpOrientation,'Antivalent2':Antivalent2,'TtdpDirection':TtdpDirection,'std':std,'stdx61375':stdx61375,'iec61375':iec61375,'ttdp':ttdp,'ttdpObjects':ttdpObjects,'ttdpGenInfo':ttdpGenInfo,_P:ttdpVersion,_Q:ttdpSlowTimeout,_R:ttdpFastTimeout,_S:ttdpTopoTtl,_T:ttdpGlobalTopoTimeout,'ttdpLinksInfo':ttdpLinksInfo,_U:ttdpLogicalLinksNb,'ttdpLogicalLinksTable':ttdpLogicalLinksTable,'ttdpLogicalLinksEntry':ttdpLogicalLinksEntry,_F:ttdpLogicalLinksIdx,_A5:ttdpConfiguredPhysLinesNb,_A6:ttdpActivePhysLinesNb,_V:ttdpIsEndLink,'ttdpPhysicalLinesTable':ttdpPhysicalLinesTable,'ttdpPhysicalLinesEntry':ttdpPhysicalLinesEntry,_I:ttdpPhysicalLinesIdx,_W:ttdpPortState,_A8:ttdpLineRcvState,_A7:ttdpPeerLineId,'ttdpPhysicalLinesStatsTable':ttdpPhysicalLinesStatsTable,'ttdpPhysicalLinesStatsEntry':ttdpPhysicalLinesStatsEntry,_A9:ttdpHelloSentFrames,_AA:ttdpHelloReceivedFrames,_AB:ttdpRemoteFastModeCnt,_AC:ttdpLocalFastModeCnt,'ttdpTopoInfo':ttdpTopoInfo,'ttdpLocalEtbnInfo':ttdpLocalEtbnInfo,_X:ttdpEtbId,_Y:ttdpLocalEtbnMacAddr,_Z:ttdpLocalEtbnId,_a:ttdpNodePosition,_b:ttdpIsAlone,_c:ttdpConnTableValid,_A3:ttdpEtbTopoCntValid,'ttdpTopoFrameStats':ttdpTopoFrameStats,_AD:ttdpTopoSentFrames,_AE:ttdpTopoReceivedFrames,_d:ttdpEtbnCnt,'ttdpEtbnTable':ttdpEtbnTable,'ttdpEtbnEntry':ttdpEtbnEntry,_G:ttdpEtbnTableIdx,_e:ttdpEtbnId,_f:ttdpEtbnMacAddr,_g:ttdpEtbnOrientation,_h:ttdpEtbnIpAddr,_i:ttdpEtbnNodeRole,_j:ttdpEtbnInaugState,_k:ttdpEtbnInhibit,_l:ttdpRemoteInhibit,_m:ttdpConnTableCrc32,_A4:ttdpEtbTopoCnt,_n:ttdpLengthen,_o:ttdpShorten,'ttdpConnectTable':ttdpConnectTable,'ttdpConnectEntry':ttdpConnectEntry,_J:ttdpConnectTableIdx,_p:ttdpNeighbourMacAddr,_q:ttdpEtbnDirCnt,'ttdpEtbnVectorTable':ttdpEtbnVectorTable,'ttdpEtbnVectorEntry':ttdpEtbnVectorEntry,_M:ttdpEtbnVectorIdx,_r:ttdpEtbnVectorMacAddr,_s:ttdpCstCnt,'ttdpCstTable':ttdpCstTable,'ttdpCstEntry':ttdpCstEntry,_H:ttdpCstTableIdx,_t:ttdpCstUuid,_u:ttdpCstOrientation,_v:ttdpCstCnCnt,_w:ttdpCstEtbnCnt,'ttdpCstCnTable':ttdpCstCnTable,'ttdpCstCnEntry':ttdpCstCnEntry,_K:ttdpCstCnTableIdx,_x:ttdpCnType,_y:ttdpCnId,_z:ttdpSubnetId,_A0:ttdpSubnetIpAddr,_A1:ttdpSubnetIpMask,'ttdpCnEtbnTable':ttdpCnEtbnTable,'ttdpCnEtbnEntry':ttdpCnEtbnEntry,_N:ttdpCnEtbnTableIdx,_A2:ttdpCnEtbnId,'ttdpConformance':ttdpConformance,_AF:ttdpBasicGroup,_AG:ttdpStatsGroup,'ttdpBasicCompliance':ttdpBasicCompliance,'ttdpStatsCompliance':ttdpStatsCompliance})