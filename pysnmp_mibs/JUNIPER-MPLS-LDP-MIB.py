_Ai='jnxMplsLdpSessionDown'
_Ah='jnxMplsLdpSessionUp'
_Ag='jnxMplsLdpPathVectorLimitMismatch'
_Af='jnxMplsLdpInitSesThresholdExceeded'
_Ae='jnxMplsLdpLspLsrXCPointer'
_Ad='jnxMplsLdpLspLsrOutSegmentPointer'
_Ac='jnxMplsLdpLspLsrInSegmentPointer'
_Ab='jnxMplsLdpLspType'
_Aa='jnxMplsLdpLspLabelType'
_AZ='jnxMplsLdpLspFecRowStatus'
_AY='jnxMplsLdpLspFecLastChange'
_AX='jnxMplsLdpLspFecOperStatus'
_AW='jnxMplsFecRowStatus'
_AV='jnxMplsFecStorageType'
_AU='jnxMplsFecAddr'
_AT='jnxMplsFecAddrLength'
_AS='jnxMplsFecAddrFamily'
_AR='jnxMplsFecType'
_AQ='jnxMplsFecIndexNext'
_AP='jnxMplsLdpSesPeerNextHopAddr'
_AO='jnxMplsLdpSesPeerNextHopAddrType'
_AN='jnxMplsLdpSesMaxPduLength'
_AM='jnxMplsLdpSesKeepAliveHoldTimeRem'
_AL='jnxMplsLdpSesProtocolVersion'
_AK='jnxMplsLdpSesStateLastChange'
_AJ='jnxMplsLdpHelloAdjType'
_AI='jnxMplsLdpHelloAdjHoldTimeRem'
_AH='jnxMplsLdpPeerLabelDistMethod'
_AG='jnxMplsLdpPeerLastChange'
_AF='jnxMplsLdpShutdownNotifSent'
_AE='jnxMplsLdpShutdownNotifReceived'
_AD='jnxMplsLdpKeepAliveTimerExpErrors'
_AC='jnxMplsLdpMalformedTlvValueErrors'
_AB='jnxMplsLdpBadTlvLengthErrors'
_AA='jnxMplsLdpBadMessageLengthErrors'
_A9='jnxMplsLdpBadPduLengthErrors'
_A8='jnxMplsLdpBadLdpIdentifierErrors'
_A7='jnxMplsLdpSesRejectedLRErrors'
_A6='jnxMplsLdpSesRejectedMaxPduErrors'
_A5='jnxMplsLdpSesRejectedAdErrors'
_A4='jnxMplsLdpSesRejectedNoHelloErrors'
_A3='jnxMplsLdpAttemptedSessions'
_A2='jnxMplsLdpEntityRowStatus'
_A1='jnxMplsLdpEntityStorageType'
_A0='jnxMplsLdpEntityDiscontinuityTime'
_z='jnxMplsLdpEntityLabelType'
_y='jnxMplsLdpEntityTargetPeerAddr'
_x='jnxMplsLdpEntityTargetPeerAddrType'
_w='jnxMplsLdpEntityTargetPeer'
_v='jnxMplsLdpEntityHopCountLimit'
_u='jnxMplsLdpEntityLabelRetentionMode'
_t='jnxMplsLdpEntityLabelDistMethod'
_s='jnxMplsLdpEntityHelloHoldTimer'
_r='jnxMplsLdpEntityKeepAliveHoldTimer'
_q='jnxMplsLdpEntityMaxPduLength'
_p='jnxMplsLdpEntityUdpDscPort'
_o='jnxMplsLdpEntityTcpDscPort'
_n='jnxMplsLdpEntityOperStatus'
_m='jnxMplsLdpEntityAdminStatus'
_l='jnxMplsLdpEntityProtocolVersion'
_k='jnxMplsLdpEntityIndexNext'
_j='jnxMplsLdpEntityLastChange'
_i='jnxMplsLdpLsrLoopDetectionCapable'
_h='jnxMplsLdpLsrId'
_g='jnxMplsLdpSesStatsEntry'
_f='jnxMplsLdpSessionEntry'
_e='jnxMplsLdpEntityStatsEntry'
_d='jnxMplsLdpSesPeerAddrIndex'
_c='jnxMplsLdpHelloAdjIndex'
_b='seconds'
_a='octets'
_Z='unknown'
_Y='TruthValue'
_X='jnxMplsLdpLsrGroup'
_W='jnxMplsLdpNotificationsGroup'
_V='jnxMplsLdpLspGroup'
_U='jnxMplsLdpGeneralGroup'
_T='jnxMplsLdpPeerPathVectorLimit'
_S='jnxMplsLdpEntityPathVectorLimit'
_R='jnxMplsLdpEntityInitSesThreshold'
_Q='jnxMplsFecIndex'
_P='jnxMplsLdpLspLabel'
_O='jnxMplsLdpLspIfIndex'
_N='InetPortNumber'
_M='jnxMplsLdpSesStatsUnkTlvErrors'
_L='jnxMplsLdpSesStatsUnkMesTypeErrors'
_K='jnxMplsLdpSesDiscontinuityTime'
_J='jnxMplsLdpSesState'
_I='jnxMplsLdpPeerLdpId'
_H='jnxMplsLdpEntityIndex'
_G='jnxMplsLdpEntityLdpId'
_F='not-accessible'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='current'
_A='JUNIPER-MPLS-LDP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_N)
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
MplsLabel,MplsLabelDistributionMethod,MplsLdpIdentifier,MplsLdpLabelType,MplsLspType,MplsLsrIdentifier,MplsRetentionMode=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLabel','MplsLabelDistributionMethod','MplsLdpIdentifier','MplsLdpLabelType','MplsLspType','MplsLsrIdentifier','MplsRetentionMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TimeInterval','TimeStamp',_Y)
jnxMplsLdpMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,36))
if mibBuilder.loadTexts:jnxMplsLdpMIB.setRevisions(('2006-05-16 12:00',))
_JnxMplsLdpObjects_ObjectIdentity=ObjectIdentity
jnxMplsLdpObjects=_JnxMplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,36,1))
_JnxMplsLdpLsrObjects_ObjectIdentity=ObjectIdentity
jnxMplsLdpLsrObjects=_JnxMplsLdpLsrObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,36,1,1))
_JnxMplsLdpLsrId_Type=MplsLsrIdentifier
_JnxMplsLdpLsrId_Object=MibScalar
jnxMplsLdpLsrId=_JnxMplsLdpLsrId_Object((1,3,6,1,4,1,2636,3,36,1,1,1),_JnxMplsLdpLsrId_Type())
jnxMplsLdpLsrId.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLsrId.setStatus(_B)
class _JnxMplsLdpLsrLoopDetectionCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('other',2),('hopCount',3),('pathVector',4),('hopCountAndPathVector',5)))
_JnxMplsLdpLsrLoopDetectionCapable_Type.__name__=_D
_JnxMplsLdpLsrLoopDetectionCapable_Object=MibScalar
jnxMplsLdpLsrLoopDetectionCapable=_JnxMplsLdpLsrLoopDetectionCapable_Object((1,3,6,1,4,1,2636,3,36,1,1,2),_JnxMplsLdpLsrLoopDetectionCapable_Type())
jnxMplsLdpLsrLoopDetectionCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLsrLoopDetectionCapable.setStatus(_B)
_JnxMplsLdpEntityObjects_ObjectIdentity=ObjectIdentity
jnxMplsLdpEntityObjects=_JnxMplsLdpEntityObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,36,1,2))
_JnxMplsLdpEntityLastChange_Type=TimeStamp
_JnxMplsLdpEntityLastChange_Object=MibScalar
jnxMplsLdpEntityLastChange=_JnxMplsLdpEntityLastChange_Object((1,3,6,1,4,1,2636,3,36,1,2,1),_JnxMplsLdpEntityLastChange_Type())
jnxMplsLdpEntityLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityLastChange.setStatus(_B)
class _JnxMplsLdpEntityIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JnxMplsLdpEntityIndexNext_Type.__name__=_E
_JnxMplsLdpEntityIndexNext_Object=MibScalar
jnxMplsLdpEntityIndexNext=_JnxMplsLdpEntityIndexNext_Object((1,3,6,1,4,1,2636,3,36,1,2,2),_JnxMplsLdpEntityIndexNext_Type())
jnxMplsLdpEntityIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityIndexNext.setStatus(_B)
_JnxMplsLdpEntityTable_Object=MibTable
jnxMplsLdpEntityTable=_JnxMplsLdpEntityTable_Object((1,3,6,1,4,1,2636,3,36,1,2,3))
if mibBuilder.loadTexts:jnxMplsLdpEntityTable.setStatus(_B)
_JnxMplsLdpEntityEntry_Object=MibTableRow
jnxMplsLdpEntityEntry=_JnxMplsLdpEntityEntry_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1))
jnxMplsLdpEntityEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:jnxMplsLdpEntityEntry.setStatus(_B)
_JnxMplsLdpEntityLdpId_Type=MplsLdpIdentifier
_JnxMplsLdpEntityLdpId_Object=MibTableColumn
jnxMplsLdpEntityLdpId=_JnxMplsLdpEntityLdpId_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,1),_JnxMplsLdpEntityLdpId_Type())
jnxMplsLdpEntityLdpId.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpEntityLdpId.setStatus(_B)
class _JnxMplsLdpEntityIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JnxMplsLdpEntityIndex_Type.__name__=_E
_JnxMplsLdpEntityIndex_Object=MibTableColumn
jnxMplsLdpEntityIndex=_JnxMplsLdpEntityIndex_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,2),_JnxMplsLdpEntityIndex_Type())
jnxMplsLdpEntityIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpEntityIndex.setStatus(_B)
class _JnxMplsLdpEntityProtocolVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxMplsLdpEntityProtocolVersion_Type.__name__=_D
_JnxMplsLdpEntityProtocolVersion_Object=MibTableColumn
jnxMplsLdpEntityProtocolVersion=_JnxMplsLdpEntityProtocolVersion_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,3),_JnxMplsLdpEntityProtocolVersion_Type())
jnxMplsLdpEntityProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityProtocolVersion.setStatus(_B)
class _JnxMplsLdpEntityAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_JnxMplsLdpEntityAdminStatus_Type.__name__=_D
_JnxMplsLdpEntityAdminStatus_Object=MibTableColumn
jnxMplsLdpEntityAdminStatus=_JnxMplsLdpEntityAdminStatus_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,4),_JnxMplsLdpEntityAdminStatus_Type())
jnxMplsLdpEntityAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityAdminStatus.setStatus(_B)
class _JnxMplsLdpEntityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('enabled',2),('disabled',3)))
_JnxMplsLdpEntityOperStatus_Type.__name__=_D
_JnxMplsLdpEntityOperStatus_Object=MibTableColumn
jnxMplsLdpEntityOperStatus=_JnxMplsLdpEntityOperStatus_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,5),_JnxMplsLdpEntityOperStatus_Type())
jnxMplsLdpEntityOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityOperStatus.setStatus(_B)
class _JnxMplsLdpEntityTcpDscPort_Type(InetPortNumber):defaultValue=646
_JnxMplsLdpEntityTcpDscPort_Type.__name__=_N
_JnxMplsLdpEntityTcpDscPort_Object=MibTableColumn
jnxMplsLdpEntityTcpDscPort=_JnxMplsLdpEntityTcpDscPort_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,6),_JnxMplsLdpEntityTcpDscPort_Type())
jnxMplsLdpEntityTcpDscPort.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityTcpDscPort.setStatus(_B)
class _JnxMplsLdpEntityUdpDscPort_Type(InetPortNumber):defaultValue=646
_JnxMplsLdpEntityUdpDscPort_Type.__name__=_N
_JnxMplsLdpEntityUdpDscPort_Object=MibTableColumn
jnxMplsLdpEntityUdpDscPort=_JnxMplsLdpEntityUdpDscPort_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,7),_JnxMplsLdpEntityUdpDscPort_Type())
jnxMplsLdpEntityUdpDscPort.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityUdpDscPort.setStatus(_B)
class _JnxMplsLdpEntityMaxPduLength_Type(Unsigned32):defaultValue=4096;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,65535))
_JnxMplsLdpEntityMaxPduLength_Type.__name__=_E
_JnxMplsLdpEntityMaxPduLength_Object=MibTableColumn
jnxMplsLdpEntityMaxPduLength=_JnxMplsLdpEntityMaxPduLength_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,8),_JnxMplsLdpEntityMaxPduLength_Type())
jnxMplsLdpEntityMaxPduLength.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityMaxPduLength.setStatus(_B)
if mibBuilder.loadTexts:jnxMplsLdpEntityMaxPduLength.setUnits(_a)
class _JnxMplsLdpEntityKeepAliveHoldTimer_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxMplsLdpEntityKeepAliveHoldTimer_Type.__name__=_D
_JnxMplsLdpEntityKeepAliveHoldTimer_Object=MibTableColumn
jnxMplsLdpEntityKeepAliveHoldTimer=_JnxMplsLdpEntityKeepAliveHoldTimer_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,9),_JnxMplsLdpEntityKeepAliveHoldTimer_Type())
jnxMplsLdpEntityKeepAliveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityKeepAliveHoldTimer.setStatus(_B)
if mibBuilder.loadTexts:jnxMplsLdpEntityKeepAliveHoldTimer.setUnits(_b)
class _JnxMplsLdpEntityHelloHoldTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JnxMplsLdpEntityHelloHoldTimer_Type.__name__=_D
_JnxMplsLdpEntityHelloHoldTimer_Object=MibTableColumn
jnxMplsLdpEntityHelloHoldTimer=_JnxMplsLdpEntityHelloHoldTimer_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,10),_JnxMplsLdpEntityHelloHoldTimer_Type())
jnxMplsLdpEntityHelloHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityHelloHoldTimer.setStatus(_B)
if mibBuilder.loadTexts:jnxMplsLdpEntityHelloHoldTimer.setUnits(_b)
class _JnxMplsLdpEntityInitSesThreshold_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_JnxMplsLdpEntityInitSesThreshold_Type.__name__=_D
_JnxMplsLdpEntityInitSesThreshold_Object=MibTableColumn
jnxMplsLdpEntityInitSesThreshold=_JnxMplsLdpEntityInitSesThreshold_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,11),_JnxMplsLdpEntityInitSesThreshold_Type())
jnxMplsLdpEntityInitSesThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityInitSesThreshold.setStatus(_B)
_JnxMplsLdpEntityLabelDistMethod_Type=MplsLabelDistributionMethod
_JnxMplsLdpEntityLabelDistMethod_Object=MibTableColumn
jnxMplsLdpEntityLabelDistMethod=_JnxMplsLdpEntityLabelDistMethod_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,12),_JnxMplsLdpEntityLabelDistMethod_Type())
jnxMplsLdpEntityLabelDistMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityLabelDistMethod.setStatus(_B)
_JnxMplsLdpEntityLabelRetentionMode_Type=MplsRetentionMode
_JnxMplsLdpEntityLabelRetentionMode_Object=MibTableColumn
jnxMplsLdpEntityLabelRetentionMode=_JnxMplsLdpEntityLabelRetentionMode_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,13),_JnxMplsLdpEntityLabelRetentionMode_Type())
jnxMplsLdpEntityLabelRetentionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityLabelRetentionMode.setStatus(_B)
class _JnxMplsLdpEntityPathVectorLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JnxMplsLdpEntityPathVectorLimit_Type.__name__=_D
_JnxMplsLdpEntityPathVectorLimit_Object=MibTableColumn
jnxMplsLdpEntityPathVectorLimit=_JnxMplsLdpEntityPathVectorLimit_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,14),_JnxMplsLdpEntityPathVectorLimit_Type())
jnxMplsLdpEntityPathVectorLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityPathVectorLimit.setStatus(_B)
class _JnxMplsLdpEntityHopCountLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JnxMplsLdpEntityHopCountLimit_Type.__name__=_D
_JnxMplsLdpEntityHopCountLimit_Object=MibTableColumn
jnxMplsLdpEntityHopCountLimit=_JnxMplsLdpEntityHopCountLimit_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,15),_JnxMplsLdpEntityHopCountLimit_Type())
jnxMplsLdpEntityHopCountLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityHopCountLimit.setStatus(_B)
class _JnxMplsLdpEntityTargetPeer_Type(TruthValue):defaultValue=2
_JnxMplsLdpEntityTargetPeer_Type.__name__=_Y
_JnxMplsLdpEntityTargetPeer_Object=MibTableColumn
jnxMplsLdpEntityTargetPeer=_JnxMplsLdpEntityTargetPeer_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,16),_JnxMplsLdpEntityTargetPeer_Type())
jnxMplsLdpEntityTargetPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityTargetPeer.setStatus(_B)
_JnxMplsLdpEntityTargetPeerAddrType_Type=InetAddressType
_JnxMplsLdpEntityTargetPeerAddrType_Object=MibTableColumn
jnxMplsLdpEntityTargetPeerAddrType=_JnxMplsLdpEntityTargetPeerAddrType_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,17),_JnxMplsLdpEntityTargetPeerAddrType_Type())
jnxMplsLdpEntityTargetPeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityTargetPeerAddrType.setStatus(_B)
_JnxMplsLdpEntityTargetPeerAddr_Type=InetAddress
_JnxMplsLdpEntityTargetPeerAddr_Object=MibTableColumn
jnxMplsLdpEntityTargetPeerAddr=_JnxMplsLdpEntityTargetPeerAddr_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,18),_JnxMplsLdpEntityTargetPeerAddr_Type())
jnxMplsLdpEntityTargetPeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityTargetPeerAddr.setStatus(_B)
_JnxMplsLdpEntityLabelType_Type=MplsLdpLabelType
_JnxMplsLdpEntityLabelType_Object=MibTableColumn
jnxMplsLdpEntityLabelType=_JnxMplsLdpEntityLabelType_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,19),_JnxMplsLdpEntityLabelType_Type())
jnxMplsLdpEntityLabelType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityLabelType.setStatus(_B)
_JnxMplsLdpEntityDiscontinuityTime_Type=TimeStamp
_JnxMplsLdpEntityDiscontinuityTime_Object=MibTableColumn
jnxMplsLdpEntityDiscontinuityTime=_JnxMplsLdpEntityDiscontinuityTime_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,20),_JnxMplsLdpEntityDiscontinuityTime_Type())
jnxMplsLdpEntityDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityDiscontinuityTime.setStatus(_B)
_JnxMplsLdpEntityStorageType_Type=StorageType
_JnxMplsLdpEntityStorageType_Object=MibTableColumn
jnxMplsLdpEntityStorageType=_JnxMplsLdpEntityStorageType_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,21),_JnxMplsLdpEntityStorageType_Type())
jnxMplsLdpEntityStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityStorageType.setStatus(_B)
_JnxMplsLdpEntityRowStatus_Type=RowStatus
_JnxMplsLdpEntityRowStatus_Object=MibTableColumn
jnxMplsLdpEntityRowStatus=_JnxMplsLdpEntityRowStatus_Object((1,3,6,1,4,1,2636,3,36,1,2,3,1,22),_JnxMplsLdpEntityRowStatus_Type())
jnxMplsLdpEntityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpEntityRowStatus.setStatus(_B)
_JnxMplsLdpEntityStatsTable_Object=MibTable
jnxMplsLdpEntityStatsTable=_JnxMplsLdpEntityStatsTable_Object((1,3,6,1,4,1,2636,3,36,1,2,4))
if mibBuilder.loadTexts:jnxMplsLdpEntityStatsTable.setStatus(_B)
_JnxMplsLdpEntityStatsEntry_Object=MibTableRow
jnxMplsLdpEntityStatsEntry=_JnxMplsLdpEntityStatsEntry_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1))
if mibBuilder.loadTexts:jnxMplsLdpEntityStatsEntry.setStatus(_B)
_JnxMplsLdpAttemptedSessions_Type=Counter32
_JnxMplsLdpAttemptedSessions_Object=MibTableColumn
jnxMplsLdpAttemptedSessions=_JnxMplsLdpAttemptedSessions_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,1),_JnxMplsLdpAttemptedSessions_Type())
jnxMplsLdpAttemptedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpAttemptedSessions.setStatus(_B)
_JnxMplsLdpSesRejectedNoHelloErrors_Type=Counter32
_JnxMplsLdpSesRejectedNoHelloErrors_Object=MibTableColumn
jnxMplsLdpSesRejectedNoHelloErrors=_JnxMplsLdpSesRejectedNoHelloErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,2),_JnxMplsLdpSesRejectedNoHelloErrors_Type())
jnxMplsLdpSesRejectedNoHelloErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesRejectedNoHelloErrors.setStatus(_B)
_JnxMplsLdpSesRejectedAdErrors_Type=Counter32
_JnxMplsLdpSesRejectedAdErrors_Object=MibTableColumn
jnxMplsLdpSesRejectedAdErrors=_JnxMplsLdpSesRejectedAdErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,3),_JnxMplsLdpSesRejectedAdErrors_Type())
jnxMplsLdpSesRejectedAdErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesRejectedAdErrors.setStatus(_B)
_JnxMplsLdpSesRejectedMaxPduErrors_Type=Counter32
_JnxMplsLdpSesRejectedMaxPduErrors_Object=MibTableColumn
jnxMplsLdpSesRejectedMaxPduErrors=_JnxMplsLdpSesRejectedMaxPduErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,4),_JnxMplsLdpSesRejectedMaxPduErrors_Type())
jnxMplsLdpSesRejectedMaxPduErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesRejectedMaxPduErrors.setStatus(_B)
_JnxMplsLdpSesRejectedLRErrors_Type=Counter32
_JnxMplsLdpSesRejectedLRErrors_Object=MibTableColumn
jnxMplsLdpSesRejectedLRErrors=_JnxMplsLdpSesRejectedLRErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,5),_JnxMplsLdpSesRejectedLRErrors_Type())
jnxMplsLdpSesRejectedLRErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesRejectedLRErrors.setStatus(_B)
_JnxMplsLdpBadLdpIdentifierErrors_Type=Counter32
_JnxMplsLdpBadLdpIdentifierErrors_Object=MibTableColumn
jnxMplsLdpBadLdpIdentifierErrors=_JnxMplsLdpBadLdpIdentifierErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,6),_JnxMplsLdpBadLdpIdentifierErrors_Type())
jnxMplsLdpBadLdpIdentifierErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpBadLdpIdentifierErrors.setStatus(_B)
_JnxMplsLdpBadPduLengthErrors_Type=Counter32
_JnxMplsLdpBadPduLengthErrors_Object=MibTableColumn
jnxMplsLdpBadPduLengthErrors=_JnxMplsLdpBadPduLengthErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,7),_JnxMplsLdpBadPduLengthErrors_Type())
jnxMplsLdpBadPduLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpBadPduLengthErrors.setStatus(_B)
_JnxMplsLdpBadMessageLengthErrors_Type=Counter32
_JnxMplsLdpBadMessageLengthErrors_Object=MibTableColumn
jnxMplsLdpBadMessageLengthErrors=_JnxMplsLdpBadMessageLengthErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,8),_JnxMplsLdpBadMessageLengthErrors_Type())
jnxMplsLdpBadMessageLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpBadMessageLengthErrors.setStatus(_B)
_JnxMplsLdpBadTlvLengthErrors_Type=Counter32
_JnxMplsLdpBadTlvLengthErrors_Object=MibTableColumn
jnxMplsLdpBadTlvLengthErrors=_JnxMplsLdpBadTlvLengthErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,9),_JnxMplsLdpBadTlvLengthErrors_Type())
jnxMplsLdpBadTlvLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpBadTlvLengthErrors.setStatus(_B)
_JnxMplsLdpMalformedTlvValueErrors_Type=Counter32
_JnxMplsLdpMalformedTlvValueErrors_Object=MibTableColumn
jnxMplsLdpMalformedTlvValueErrors=_JnxMplsLdpMalformedTlvValueErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,10),_JnxMplsLdpMalformedTlvValueErrors_Type())
jnxMplsLdpMalformedTlvValueErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpMalformedTlvValueErrors.setStatus(_B)
_JnxMplsLdpKeepAliveTimerExpErrors_Type=Counter32
_JnxMplsLdpKeepAliveTimerExpErrors_Object=MibTableColumn
jnxMplsLdpKeepAliveTimerExpErrors=_JnxMplsLdpKeepAliveTimerExpErrors_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,11),_JnxMplsLdpKeepAliveTimerExpErrors_Type())
jnxMplsLdpKeepAliveTimerExpErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpKeepAliveTimerExpErrors.setStatus(_B)
_JnxMplsLdpShutdownNotifReceived_Type=Counter32
_JnxMplsLdpShutdownNotifReceived_Object=MibTableColumn
jnxMplsLdpShutdownNotifReceived=_JnxMplsLdpShutdownNotifReceived_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,12),_JnxMplsLdpShutdownNotifReceived_Type())
jnxMplsLdpShutdownNotifReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpShutdownNotifReceived.setStatus(_B)
_JnxMplsLdpShutdownNotifSent_Type=Counter32
_JnxMplsLdpShutdownNotifSent_Object=MibTableColumn
jnxMplsLdpShutdownNotifSent=_JnxMplsLdpShutdownNotifSent_Object((1,3,6,1,4,1,2636,3,36,1,2,4,1,13),_JnxMplsLdpShutdownNotifSent_Type())
jnxMplsLdpShutdownNotifSent.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpShutdownNotifSent.setStatus(_B)
_JnxMplsLdpSessionObjects_ObjectIdentity=ObjectIdentity
jnxMplsLdpSessionObjects=_JnxMplsLdpSessionObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,36,1,3))
_JnxMplsLdpPeerLastChange_Type=TimeStamp
_JnxMplsLdpPeerLastChange_Object=MibScalar
jnxMplsLdpPeerLastChange=_JnxMplsLdpPeerLastChange_Object((1,3,6,1,4,1,2636,3,36,1,3,1),_JnxMplsLdpPeerLastChange_Type())
jnxMplsLdpPeerLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpPeerLastChange.setStatus(_B)
_JnxMplsLdpPeerTable_Object=MibTable
jnxMplsLdpPeerTable=_JnxMplsLdpPeerTable_Object((1,3,6,1,4,1,2636,3,36,1,3,2))
if mibBuilder.loadTexts:jnxMplsLdpPeerTable.setStatus(_B)
_JnxMplsLdpPeerEntry_Object=MibTableRow
jnxMplsLdpPeerEntry=_JnxMplsLdpPeerEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,2,1))
jnxMplsLdpPeerEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:jnxMplsLdpPeerEntry.setStatus(_B)
_JnxMplsLdpPeerLdpId_Type=MplsLdpIdentifier
_JnxMplsLdpPeerLdpId_Object=MibTableColumn
jnxMplsLdpPeerLdpId=_JnxMplsLdpPeerLdpId_Object((1,3,6,1,4,1,2636,3,36,1,3,2,1,1),_JnxMplsLdpPeerLdpId_Type())
jnxMplsLdpPeerLdpId.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpPeerLdpId.setStatus(_B)
_JnxMplsLdpPeerLabelDistMethod_Type=MplsLabelDistributionMethod
_JnxMplsLdpPeerLabelDistMethod_Object=MibTableColumn
jnxMplsLdpPeerLabelDistMethod=_JnxMplsLdpPeerLabelDistMethod_Object((1,3,6,1,4,1,2636,3,36,1,3,2,1,2),_JnxMplsLdpPeerLabelDistMethod_Type())
jnxMplsLdpPeerLabelDistMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpPeerLabelDistMethod.setStatus(_B)
class _JnxMplsLdpPeerPathVectorLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JnxMplsLdpPeerPathVectorLimit_Type.__name__=_D
_JnxMplsLdpPeerPathVectorLimit_Object=MibTableColumn
jnxMplsLdpPeerPathVectorLimit=_JnxMplsLdpPeerPathVectorLimit_Object((1,3,6,1,4,1,2636,3,36,1,3,2,1,3),_JnxMplsLdpPeerPathVectorLimit_Type())
jnxMplsLdpPeerPathVectorLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpPeerPathVectorLimit.setStatus(_B)
_JnxMplsLdpSessionTable_Object=MibTable
jnxMplsLdpSessionTable=_JnxMplsLdpSessionTable_Object((1,3,6,1,4,1,2636,3,36,1,3,3))
if mibBuilder.loadTexts:jnxMplsLdpSessionTable.setStatus(_B)
_JnxMplsLdpSessionEntry_Object=MibTableRow
jnxMplsLdpSessionEntry=_JnxMplsLdpSessionEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1))
if mibBuilder.loadTexts:jnxMplsLdpSessionEntry.setStatus(_B)
_JnxMplsLdpSesStateLastChange_Type=TimeStamp
_JnxMplsLdpSesStateLastChange_Object=MibTableColumn
jnxMplsLdpSesStateLastChange=_JnxMplsLdpSesStateLastChange_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1,1),_JnxMplsLdpSesStateLastChange_Type())
jnxMplsLdpSesStateLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesStateLastChange.setStatus(_B)
class _JnxMplsLdpSesState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonexistent',1),('initialized',2),('openrec',3),('opensent',4),('operational',5)))
_JnxMplsLdpSesState_Type.__name__=_D
_JnxMplsLdpSesState_Object=MibTableColumn
jnxMplsLdpSesState=_JnxMplsLdpSesState_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1,2),_JnxMplsLdpSesState_Type())
jnxMplsLdpSesState.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesState.setStatus(_B)
class _JnxMplsLdpSesProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxMplsLdpSesProtocolVersion_Type.__name__=_D
_JnxMplsLdpSesProtocolVersion_Object=MibTableColumn
jnxMplsLdpSesProtocolVersion=_JnxMplsLdpSesProtocolVersion_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1,3),_JnxMplsLdpSesProtocolVersion_Type())
jnxMplsLdpSesProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesProtocolVersion.setStatus(_B)
_JnxMplsLdpSesKeepAliveHoldTimeRem_Type=TimeInterval
_JnxMplsLdpSesKeepAliveHoldTimeRem_Object=MibTableColumn
jnxMplsLdpSesKeepAliveHoldTimeRem=_JnxMplsLdpSesKeepAliveHoldTimeRem_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1,4),_JnxMplsLdpSesKeepAliveHoldTimeRem_Type())
jnxMplsLdpSesKeepAliveHoldTimeRem.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesKeepAliveHoldTimeRem.setStatus(_B)
class _JnxMplsLdpSesMaxPduLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxMplsLdpSesMaxPduLength_Type.__name__=_E
_JnxMplsLdpSesMaxPduLength_Object=MibTableColumn
jnxMplsLdpSesMaxPduLength=_JnxMplsLdpSesMaxPduLength_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1,5),_JnxMplsLdpSesMaxPduLength_Type())
jnxMplsLdpSesMaxPduLength.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesMaxPduLength.setStatus(_B)
if mibBuilder.loadTexts:jnxMplsLdpSesMaxPduLength.setUnits(_a)
_JnxMplsLdpSesDiscontinuityTime_Type=TimeStamp
_JnxMplsLdpSesDiscontinuityTime_Object=MibTableColumn
jnxMplsLdpSesDiscontinuityTime=_JnxMplsLdpSesDiscontinuityTime_Object((1,3,6,1,4,1,2636,3,36,1,3,3,1,6),_JnxMplsLdpSesDiscontinuityTime_Type())
jnxMplsLdpSesDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesDiscontinuityTime.setStatus(_B)
_JnxMplsLdpSesStatsTable_Object=MibTable
jnxMplsLdpSesStatsTable=_JnxMplsLdpSesStatsTable_Object((1,3,6,1,4,1,2636,3,36,1,3,4))
if mibBuilder.loadTexts:jnxMplsLdpSesStatsTable.setStatus(_B)
_JnxMplsLdpSesStatsEntry_Object=MibTableRow
jnxMplsLdpSesStatsEntry=_JnxMplsLdpSesStatsEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,4,1))
if mibBuilder.loadTexts:jnxMplsLdpSesStatsEntry.setStatus(_B)
_JnxMplsLdpSesStatsUnkMesTypeErrors_Type=Counter32
_JnxMplsLdpSesStatsUnkMesTypeErrors_Object=MibTableColumn
jnxMplsLdpSesStatsUnkMesTypeErrors=_JnxMplsLdpSesStatsUnkMesTypeErrors_Object((1,3,6,1,4,1,2636,3,36,1,3,4,1,1),_JnxMplsLdpSesStatsUnkMesTypeErrors_Type())
jnxMplsLdpSesStatsUnkMesTypeErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesStatsUnkMesTypeErrors.setStatus(_B)
_JnxMplsLdpSesStatsUnkTlvErrors_Type=Counter32
_JnxMplsLdpSesStatsUnkTlvErrors_Object=MibTableColumn
jnxMplsLdpSesStatsUnkTlvErrors=_JnxMplsLdpSesStatsUnkTlvErrors_Object((1,3,6,1,4,1,2636,3,36,1,3,4,1,2),_JnxMplsLdpSesStatsUnkTlvErrors_Type())
jnxMplsLdpSesStatsUnkTlvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesStatsUnkTlvErrors.setStatus(_B)
_JnxMplsLdpHelloAdjacencyObjects_ObjectIdentity=ObjectIdentity
jnxMplsLdpHelloAdjacencyObjects=_JnxMplsLdpHelloAdjacencyObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,36,1,3,5))
_JnxMplsLdpHelloAdjacencyTable_Object=MibTable
jnxMplsLdpHelloAdjacencyTable=_JnxMplsLdpHelloAdjacencyTable_Object((1,3,6,1,4,1,2636,3,36,1,3,5,1))
if mibBuilder.loadTexts:jnxMplsLdpHelloAdjacencyTable.setStatus(_B)
_JnxMplsLdpHelloAdjacencyEntry_Object=MibTableRow
jnxMplsLdpHelloAdjacencyEntry=_JnxMplsLdpHelloAdjacencyEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,5,1,1))
jnxMplsLdpHelloAdjacencyEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_c))
if mibBuilder.loadTexts:jnxMplsLdpHelloAdjacencyEntry.setStatus(_B)
class _JnxMplsLdpHelloAdjIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JnxMplsLdpHelloAdjIndex_Type.__name__=_E
_JnxMplsLdpHelloAdjIndex_Object=MibTableColumn
jnxMplsLdpHelloAdjIndex=_JnxMplsLdpHelloAdjIndex_Object((1,3,6,1,4,1,2636,3,36,1,3,5,1,1,1),_JnxMplsLdpHelloAdjIndex_Type())
jnxMplsLdpHelloAdjIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpHelloAdjIndex.setStatus(_B)
_JnxMplsLdpHelloAdjHoldTimeRem_Type=TimeInterval
_JnxMplsLdpHelloAdjHoldTimeRem_Object=MibTableColumn
jnxMplsLdpHelloAdjHoldTimeRem=_JnxMplsLdpHelloAdjHoldTimeRem_Object((1,3,6,1,4,1,2636,3,36,1,3,5,1,1,2),_JnxMplsLdpHelloAdjHoldTimeRem_Type())
jnxMplsLdpHelloAdjHoldTimeRem.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpHelloAdjHoldTimeRem.setStatus(_B)
class _JnxMplsLdpHelloAdjType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),('targeted',2)))
_JnxMplsLdpHelloAdjType_Type.__name__=_D
_JnxMplsLdpHelloAdjType_Object=MibTableColumn
jnxMplsLdpHelloAdjType=_JnxMplsLdpHelloAdjType_Object((1,3,6,1,4,1,2636,3,36,1,3,5,1,1,3),_JnxMplsLdpHelloAdjType_Type())
jnxMplsLdpHelloAdjType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpHelloAdjType.setStatus(_B)
_JnxMplsLdpLspTable_Object=MibTable
jnxMplsLdpLspTable=_JnxMplsLdpLspTable_Object((1,3,6,1,4,1,2636,3,36,1,3,6))
if mibBuilder.loadTexts:jnxMplsLdpLspTable.setStatus(_B)
_JnxMplsLdpLspEntry_Object=MibTableRow
jnxMplsLdpLspEntry=_JnxMplsLdpLspEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1))
jnxMplsLdpLspEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:jnxMplsLdpLspEntry.setStatus(_B)
_JnxMplsLdpLspIfIndex_Type=InterfaceIndex
_JnxMplsLdpLspIfIndex_Object=MibTableColumn
jnxMplsLdpLspIfIndex=_JnxMplsLdpLspIfIndex_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,1),_JnxMplsLdpLspIfIndex_Type())
jnxMplsLdpLspIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpLspIfIndex.setStatus(_B)
_JnxMplsLdpLspLabel_Type=MplsLabel
_JnxMplsLdpLspLabel_Object=MibTableColumn
jnxMplsLdpLspLabel=_JnxMplsLdpLspLabel_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,2),_JnxMplsLdpLspLabel_Type())
jnxMplsLdpLspLabel.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpLspLabel.setStatus(_B)
_JnxMplsLdpLspLabelType_Type=MplsLdpLabelType
_JnxMplsLdpLspLabelType_Object=MibTableColumn
jnxMplsLdpLspLabelType=_JnxMplsLdpLspLabelType_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,3),_JnxMplsLdpLspLabelType_Type())
jnxMplsLdpLspLabelType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspLabelType.setStatus(_B)
_JnxMplsLdpLspType_Type=MplsLspType
_JnxMplsLdpLspType_Object=MibTableColumn
jnxMplsLdpLspType=_JnxMplsLdpLspType_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,4),_JnxMplsLdpLspType_Type())
jnxMplsLdpLspType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspType.setStatus(_B)
_JnxMplsLdpLspLsrInSegmentPointer_Type=RowPointer
_JnxMplsLdpLspLsrInSegmentPointer_Object=MibTableColumn
jnxMplsLdpLspLsrInSegmentPointer=_JnxMplsLdpLspLsrInSegmentPointer_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,5),_JnxMplsLdpLspLsrInSegmentPointer_Type())
jnxMplsLdpLspLsrInSegmentPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspLsrInSegmentPointer.setStatus(_B)
_JnxMplsLdpLspLsrOutSegmentPointer_Type=RowPointer
_JnxMplsLdpLspLsrOutSegmentPointer_Object=MibTableColumn
jnxMplsLdpLspLsrOutSegmentPointer=_JnxMplsLdpLspLsrOutSegmentPointer_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,6),_JnxMplsLdpLspLsrOutSegmentPointer_Type())
jnxMplsLdpLspLsrOutSegmentPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspLsrOutSegmentPointer.setStatus(_B)
_JnxMplsLdpLspLsrXCPointer_Type=RowPointer
_JnxMplsLdpLspLsrXCPointer_Object=MibTableColumn
jnxMplsLdpLspLsrXCPointer=_JnxMplsLdpLspLsrXCPointer_Object((1,3,6,1,4,1,2636,3,36,1,3,6,1,7),_JnxMplsLdpLspLsrXCPointer_Type())
jnxMplsLdpLspLsrXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspLsrXCPointer.setStatus(_B)
_JnxMplsFecObjects_ObjectIdentity=ObjectIdentity
jnxMplsFecObjects=_JnxMplsFecObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,36,1,3,7))
class _JnxMplsFecIndexNext_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JnxMplsFecIndexNext_Type.__name__=_E
_JnxMplsFecIndexNext_Object=MibScalar
jnxMplsFecIndexNext=_JnxMplsFecIndexNext_Object((1,3,6,1,4,1,2636,3,36,1,3,7,1),_JnxMplsFecIndexNext_Type())
jnxMplsFecIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecIndexNext.setStatus(_B)
_JnxMplsFecTable_Object=MibTable
jnxMplsFecTable=_JnxMplsFecTable_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2))
if mibBuilder.loadTexts:jnxMplsFecTable.setStatus(_B)
_JnxMplsFecEntry_Object=MibTableRow
jnxMplsFecEntry=_JnxMplsFecEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1))
jnxMplsFecEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:jnxMplsFecEntry.setStatus(_B)
class _JnxMplsFecIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JnxMplsFecIndex_Type.__name__=_E
_JnxMplsFecIndex_Object=MibTableColumn
jnxMplsFecIndex=_JnxMplsFecIndex_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,1),_JnxMplsFecIndex_Type())
jnxMplsFecIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsFecIndex.setStatus(_B)
class _JnxMplsFecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('prefix',1),('hostAddress',2)))
_JnxMplsFecType_Type.__name__=_D
_JnxMplsFecType_Object=MibTableColumn
jnxMplsFecType=_JnxMplsFecType_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,2),_JnxMplsFecType_Type())
jnxMplsFecType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecType.setStatus(_B)
class _JnxMplsFecAddrLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JnxMplsFecAddrLength_Type.__name__=_D
_JnxMplsFecAddrLength_Object=MibTableColumn
jnxMplsFecAddrLength=_JnxMplsFecAddrLength_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,3),_JnxMplsFecAddrLength_Type())
jnxMplsFecAddrLength.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecAddrLength.setStatus(_B)
_JnxMplsFecAddrFamily_Type=InetAddressType
_JnxMplsFecAddrFamily_Object=MibTableColumn
jnxMplsFecAddrFamily=_JnxMplsFecAddrFamily_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,4),_JnxMplsFecAddrFamily_Type())
jnxMplsFecAddrFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecAddrFamily.setStatus(_B)
_JnxMplsFecAddr_Type=InetAddress
_JnxMplsFecAddr_Object=MibTableColumn
jnxMplsFecAddr=_JnxMplsFecAddr_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,5),_JnxMplsFecAddr_Type())
jnxMplsFecAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecAddr.setStatus(_B)
_JnxMplsFecStorageType_Type=StorageType
_JnxMplsFecStorageType_Object=MibTableColumn
jnxMplsFecStorageType=_JnxMplsFecStorageType_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,6),_JnxMplsFecStorageType_Type())
jnxMplsFecStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecStorageType.setStatus(_B)
_JnxMplsFecRowStatus_Type=RowStatus
_JnxMplsFecRowStatus_Object=MibTableColumn
jnxMplsFecRowStatus=_JnxMplsFecRowStatus_Object((1,3,6,1,4,1,2636,3,36,1,3,7,2,1,7),_JnxMplsFecRowStatus_Type())
jnxMplsFecRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsFecRowStatus.setStatus(_B)
_JnxMplsLdpLspFecTable_Object=MibTable
jnxMplsLdpLspFecTable=_JnxMplsLdpLspFecTable_Object((1,3,6,1,4,1,2636,3,36,1,3,8))
if mibBuilder.loadTexts:jnxMplsLdpLspFecTable.setStatus(_B)
_JnxMplsLdpLspFecEntry_Object=MibTableRow
jnxMplsLdpLspFecEntry=_JnxMplsLdpLspFecEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,8,1))
jnxMplsLdpLspFecEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_O),(0,_A,_P),(0,_A,_Q))
if mibBuilder.loadTexts:jnxMplsLdpLspFecEntry.setStatus(_B)
class _JnxMplsLdpLspFecOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('inUse',2),('notInUse',3)))
_JnxMplsLdpLspFecOperStatus_Type.__name__=_D
_JnxMplsLdpLspFecOperStatus_Object=MibTableColumn
jnxMplsLdpLspFecOperStatus=_JnxMplsLdpLspFecOperStatus_Object((1,3,6,1,4,1,2636,3,36,1,3,8,1,1),_JnxMplsLdpLspFecOperStatus_Type())
jnxMplsLdpLspFecOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspFecOperStatus.setStatus(_B)
_JnxMplsLdpLspFecLastChange_Type=TimeStamp
_JnxMplsLdpLspFecLastChange_Object=MibTableColumn
jnxMplsLdpLspFecLastChange=_JnxMplsLdpLspFecLastChange_Object((1,3,6,1,4,1,2636,3,36,1,3,8,1,2),_JnxMplsLdpLspFecLastChange_Type())
jnxMplsLdpLspFecLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspFecLastChange.setStatus(_B)
_JnxMplsLdpLspFecRowStatus_Type=RowStatus
_JnxMplsLdpLspFecRowStatus_Object=MibTableColumn
jnxMplsLdpLspFecRowStatus=_JnxMplsLdpLspFecRowStatus_Object((1,3,6,1,4,1,2636,3,36,1,3,8,1,3),_JnxMplsLdpLspFecRowStatus_Type())
jnxMplsLdpLspFecRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpLspFecRowStatus.setStatus(_B)
_JnxMplsLdpSesPeerAddrTable_Object=MibTable
jnxMplsLdpSesPeerAddrTable=_JnxMplsLdpSesPeerAddrTable_Object((1,3,6,1,4,1,2636,3,36,1,3,9))
if mibBuilder.loadTexts:jnxMplsLdpSesPeerAddrTable.setStatus(_B)
_JnxMplsLdpSesPeerAddrEntry_Object=MibTableRow
jnxMplsLdpSesPeerAddrEntry=_JnxMplsLdpSesPeerAddrEntry_Object((1,3,6,1,4,1,2636,3,36,1,3,9,1))
jnxMplsLdpSesPeerAddrEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_d))
if mibBuilder.loadTexts:jnxMplsLdpSesPeerAddrEntry.setStatus(_B)
class _JnxMplsLdpSesPeerAddrIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_JnxMplsLdpSesPeerAddrIndex_Type.__name__=_E
_JnxMplsLdpSesPeerAddrIndex_Object=MibTableColumn
jnxMplsLdpSesPeerAddrIndex=_JnxMplsLdpSesPeerAddrIndex_Object((1,3,6,1,4,1,2636,3,36,1,3,9,1,1),_JnxMplsLdpSesPeerAddrIndex_Type())
jnxMplsLdpSesPeerAddrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxMplsLdpSesPeerAddrIndex.setStatus(_B)
_JnxMplsLdpSesPeerNextHopAddrType_Type=InetAddressType
_JnxMplsLdpSesPeerNextHopAddrType_Object=MibTableColumn
jnxMplsLdpSesPeerNextHopAddrType=_JnxMplsLdpSesPeerNextHopAddrType_Object((1,3,6,1,4,1,2636,3,36,1,3,9,1,2),_JnxMplsLdpSesPeerNextHopAddrType_Type())
jnxMplsLdpSesPeerNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesPeerNextHopAddrType.setStatus(_B)
_JnxMplsLdpSesPeerNextHopAddr_Type=InetAddress
_JnxMplsLdpSesPeerNextHopAddr_Object=MibTableColumn
jnxMplsLdpSesPeerNextHopAddr=_JnxMplsLdpSesPeerNextHopAddr_Object((1,3,6,1,4,1,2636,3,36,1,3,9,1,3),_JnxMplsLdpSesPeerNextHopAddr_Type())
jnxMplsLdpSesPeerNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxMplsLdpSesPeerNextHopAddr.setStatus(_B)
_JnxMplsLdpNotifications_ObjectIdentity=ObjectIdentity
jnxMplsLdpNotifications=_JnxMplsLdpNotifications_ObjectIdentity((1,3,6,1,4,1,2636,3,36,2))
_JnxMplsLdpNotificationPrefix_ObjectIdentity=ObjectIdentity
jnxMplsLdpNotificationPrefix=_JnxMplsLdpNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2636,3,36,2,0))
_JnxMplsLdpConformance_ObjectIdentity=ObjectIdentity
jnxMplsLdpConformance=_JnxMplsLdpConformance_ObjectIdentity((1,3,6,1,4,1,2636,3,36,3))
_JnxMplsLdpGroups_ObjectIdentity=ObjectIdentity
jnxMplsLdpGroups=_JnxMplsLdpGroups_ObjectIdentity((1,3,6,1,4,1,2636,3,36,3,1))
_JnxMplsLdpCompliances_ObjectIdentity=ObjectIdentity
jnxMplsLdpCompliances=_JnxMplsLdpCompliances_ObjectIdentity((1,3,6,1,4,1,2636,3,36,3,2))
jnxMplsLdpEntityEntry.registerAugmentions((_A,_e))
jnxMplsLdpEntityStatsEntry.setIndexNames(*jnxMplsLdpEntityEntry.getIndexNames())
jnxMplsLdpPeerEntry.registerAugmentions((_A,_f))
jnxMplsLdpSessionEntry.setIndexNames(*jnxMplsLdpPeerEntry.getIndexNames())
jnxMplsLdpPeerEntry.registerAugmentions((_A,_g))
jnxMplsLdpSesStatsEntry.setIndexNames(*jnxMplsLdpPeerEntry.getIndexNames())
jnxMplsLdpGeneralGroup=ObjectGroup((1,3,6,1,4,1,2636,3,36,3,1,1))
jnxMplsLdpGeneralGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_R),(_A,_t),(_A,_u),(_A,_S),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_T),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_J),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_K),(_A,_L),(_A,_M),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:jnxMplsLdpGeneralGroup.setStatus(_B)
jnxMplsLdpLspGroup=ObjectGroup((1,3,6,1,4,1,2636,3,36,3,1,2))
jnxMplsLdpLspGroup.setObjects(*((_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:jnxMplsLdpLspGroup.setStatus(_B)
jnxMplsLdpLsrGroup=ObjectGroup((1,3,6,1,4,1,2636,3,36,3,1,3))
jnxMplsLdpLsrGroup.setObjects(*((_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:jnxMplsLdpLsrGroup.setStatus(_B)
jnxMplsLdpInitSesThresholdExceeded=NotificationType((1,3,6,1,4,1,2636,3,36,2,0,1))
jnxMplsLdpInitSesThresholdExceeded.setObjects((_A,_R))
if mibBuilder.loadTexts:jnxMplsLdpInitSesThresholdExceeded.setStatus(_B)
jnxMplsLdpPathVectorLimitMismatch=NotificationType((1,3,6,1,4,1,2636,3,36,2,0,2))
jnxMplsLdpPathVectorLimitMismatch.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:jnxMplsLdpPathVectorLimitMismatch.setStatus(_B)
jnxMplsLdpSessionUp=NotificationType((1,3,6,1,4,1,2636,3,36,2,0,3))
jnxMplsLdpSessionUp.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:jnxMplsLdpSessionUp.setStatus(_B)
jnxMplsLdpSessionDown=NotificationType((1,3,6,1,4,1,2636,3,36,2,0,4))
jnxMplsLdpSessionDown.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:jnxMplsLdpSessionDown.setStatus(_B)
jnxMplsLdpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,2636,3,36,3,1,4))
jnxMplsLdpNotificationsGroup.setObjects(*((_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai)))
if mibBuilder.loadTexts:jnxMplsLdpNotificationsGroup.setStatus(_B)
jnxMplsLdpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,2636,3,36,3,2,1))
jnxMplsLdpModuleFullCompliance.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:jnxMplsLdpModuleFullCompliance.setStatus(_B)
jnxMplsLdpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,2636,3,36,3,2,2))
jnxMplsLdpModuleReadOnlyCompliance.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:jnxMplsLdpModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'jnxMplsLdpMIB':jnxMplsLdpMIB,'jnxMplsLdpObjects':jnxMplsLdpObjects,'jnxMplsLdpLsrObjects':jnxMplsLdpLsrObjects,_h:jnxMplsLdpLsrId,_i:jnxMplsLdpLsrLoopDetectionCapable,'jnxMplsLdpEntityObjects':jnxMplsLdpEntityObjects,_j:jnxMplsLdpEntityLastChange,_k:jnxMplsLdpEntityIndexNext,'jnxMplsLdpEntityTable':jnxMplsLdpEntityTable,'jnxMplsLdpEntityEntry':jnxMplsLdpEntityEntry,_G:jnxMplsLdpEntityLdpId,_H:jnxMplsLdpEntityIndex,_l:jnxMplsLdpEntityProtocolVersion,_m:jnxMplsLdpEntityAdminStatus,_n:jnxMplsLdpEntityOperStatus,_o:jnxMplsLdpEntityTcpDscPort,_p:jnxMplsLdpEntityUdpDscPort,_q:jnxMplsLdpEntityMaxPduLength,_r:jnxMplsLdpEntityKeepAliveHoldTimer,_s:jnxMplsLdpEntityHelloHoldTimer,_R:jnxMplsLdpEntityInitSesThreshold,_t:jnxMplsLdpEntityLabelDistMethod,_u:jnxMplsLdpEntityLabelRetentionMode,_S:jnxMplsLdpEntityPathVectorLimit,_v:jnxMplsLdpEntityHopCountLimit,_w:jnxMplsLdpEntityTargetPeer,_x:jnxMplsLdpEntityTargetPeerAddrType,_y:jnxMplsLdpEntityTargetPeerAddr,_z:jnxMplsLdpEntityLabelType,_A0:jnxMplsLdpEntityDiscontinuityTime,_A1:jnxMplsLdpEntityStorageType,_A2:jnxMplsLdpEntityRowStatus,'jnxMplsLdpEntityStatsTable':jnxMplsLdpEntityStatsTable,_e:jnxMplsLdpEntityStatsEntry,_A3:jnxMplsLdpAttemptedSessions,_A4:jnxMplsLdpSesRejectedNoHelloErrors,_A5:jnxMplsLdpSesRejectedAdErrors,_A6:jnxMplsLdpSesRejectedMaxPduErrors,_A7:jnxMplsLdpSesRejectedLRErrors,_A8:jnxMplsLdpBadLdpIdentifierErrors,_A9:jnxMplsLdpBadPduLengthErrors,_AA:jnxMplsLdpBadMessageLengthErrors,_AB:jnxMplsLdpBadTlvLengthErrors,_AC:jnxMplsLdpMalformedTlvValueErrors,_AD:jnxMplsLdpKeepAliveTimerExpErrors,_AE:jnxMplsLdpShutdownNotifReceived,_AF:jnxMplsLdpShutdownNotifSent,'jnxMplsLdpSessionObjects':jnxMplsLdpSessionObjects,_AG:jnxMplsLdpPeerLastChange,'jnxMplsLdpPeerTable':jnxMplsLdpPeerTable,'jnxMplsLdpPeerEntry':jnxMplsLdpPeerEntry,_I:jnxMplsLdpPeerLdpId,_AH:jnxMplsLdpPeerLabelDistMethod,_T:jnxMplsLdpPeerPathVectorLimit,'jnxMplsLdpSessionTable':jnxMplsLdpSessionTable,_f:jnxMplsLdpSessionEntry,_AK:jnxMplsLdpSesStateLastChange,_J:jnxMplsLdpSesState,_AL:jnxMplsLdpSesProtocolVersion,_AM:jnxMplsLdpSesKeepAliveHoldTimeRem,_AN:jnxMplsLdpSesMaxPduLength,_K:jnxMplsLdpSesDiscontinuityTime,'jnxMplsLdpSesStatsTable':jnxMplsLdpSesStatsTable,_g:jnxMplsLdpSesStatsEntry,_L:jnxMplsLdpSesStatsUnkMesTypeErrors,_M:jnxMplsLdpSesStatsUnkTlvErrors,'jnxMplsLdpHelloAdjacencyObjects':jnxMplsLdpHelloAdjacencyObjects,'jnxMplsLdpHelloAdjacencyTable':jnxMplsLdpHelloAdjacencyTable,'jnxMplsLdpHelloAdjacencyEntry':jnxMplsLdpHelloAdjacencyEntry,_c:jnxMplsLdpHelloAdjIndex,_AI:jnxMplsLdpHelloAdjHoldTimeRem,_AJ:jnxMplsLdpHelloAdjType,'jnxMplsLdpLspTable':jnxMplsLdpLspTable,'jnxMplsLdpLspEntry':jnxMplsLdpLspEntry,_O:jnxMplsLdpLspIfIndex,_P:jnxMplsLdpLspLabel,_Aa:jnxMplsLdpLspLabelType,_Ab:jnxMplsLdpLspType,_Ac:jnxMplsLdpLspLsrInSegmentPointer,_Ad:jnxMplsLdpLspLsrOutSegmentPointer,_Ae:jnxMplsLdpLspLsrXCPointer,'jnxMplsFecObjects':jnxMplsFecObjects,_AQ:jnxMplsFecIndexNext,'jnxMplsFecTable':jnxMplsFecTable,'jnxMplsFecEntry':jnxMplsFecEntry,_Q:jnxMplsFecIndex,_AR:jnxMplsFecType,_AT:jnxMplsFecAddrLength,_AS:jnxMplsFecAddrFamily,_AU:jnxMplsFecAddr,_AV:jnxMplsFecStorageType,_AW:jnxMplsFecRowStatus,'jnxMplsLdpLspFecTable':jnxMplsLdpLspFecTable,'jnxMplsLdpLspFecEntry':jnxMplsLdpLspFecEntry,_AX:jnxMplsLdpLspFecOperStatus,_AY:jnxMplsLdpLspFecLastChange,_AZ:jnxMplsLdpLspFecRowStatus,'jnxMplsLdpSesPeerAddrTable':jnxMplsLdpSesPeerAddrTable,'jnxMplsLdpSesPeerAddrEntry':jnxMplsLdpSesPeerAddrEntry,_d:jnxMplsLdpSesPeerAddrIndex,_AO:jnxMplsLdpSesPeerNextHopAddrType,_AP:jnxMplsLdpSesPeerNextHopAddr,'jnxMplsLdpNotifications':jnxMplsLdpNotifications,'jnxMplsLdpNotificationPrefix':jnxMplsLdpNotificationPrefix,_Af:jnxMplsLdpInitSesThresholdExceeded,_Ag:jnxMplsLdpPathVectorLimitMismatch,_Ah:jnxMplsLdpSessionUp,_Ai:jnxMplsLdpSessionDown,'jnxMplsLdpConformance':jnxMplsLdpConformance,'jnxMplsLdpGroups':jnxMplsLdpGroups,_U:jnxMplsLdpGeneralGroup,_V:jnxMplsLdpLspGroup,_X:jnxMplsLdpLsrGroup,_W:jnxMplsLdpNotificationsGroup,'jnxMplsLdpCompliances':jnxMplsLdpCompliances,'jnxMplsLdpModuleFullCompliance':jnxMplsLdpModuleFullCompliance,'jnxMplsLdpModuleReadOnlyCompliance':jnxMplsLdpModuleReadOnlyCompliance})