_Am='callNotificationsGroup'
_Al='callHistoryGroup'
_Ak='callActiveGroup'
_Aj='dialControlGroup'
_Ai='dialCtlPeerCallSetup'
_Ah='dialCtlPeerCallInformation'
_Ag='callHistoryReceiveBytes'
_Af='callHistoryReceivePackets'
_Ae='callHistoryTransmitBytes'
_Ad='callHistoryTransmitPackets'
_Ac='callHistoryChargedUnits'
_Ab='callHistoryDisconnectText'
_Aa='callHistoryRetainTimer'
_AZ='callHistoryTableMaxLength'
_AY='callActiveReceiveBytes'
_AX='callActiveReceivePackets'
_AW='callActiveTransmitBytes'
_AV='callActiveTransmitPackets'
_AU='callActiveChargedUnits'
_AT='callActiveCallState'
_AS='callActiveConnectTime'
_AR='dialCtlPeerStatsLastSetupTime'
_AQ='dialCtlPeerStatsLastDisconnectText'
_AP='dialCtlPeerStatsLastDisconnectCause'
_AO='dialCtlPeerStatsRefuseCalls'
_AN='dialCtlPeerStatsAcceptCalls'
_AM='dialCtlPeerStatsFailCalls'
_AL='dialCtlPeerStatsSuccessCalls'
_AK='dialCtlPeerStatsChargedUnits'
_AJ='dialCtlPeerStatsConnectTime'
_AI='dialCtlPeerCfgStatus'
_AH='dialCtlPeerCfgTrapEnable'
_AG='dialCtlPeerCfgFailureDelay'
_AF='dialCtlPeerCfgRetryDelay'
_AE='dialCtlPeerCfgCallRetries'
_AD='dialCtlPeerCfgCarrierDelay'
_AC='dialCtlPeerCfgMaxDuration'
_AB='dialCtlPeerCfgMinDuration'
_AA='dialCtlPeerCfgInactivityTimer'
_A9='dialCtlPeerCfgPermission'
_A8='dialCtlPeerCfgInfoType'
_A7='dialCtlPeerCfgSpeed'
_A6='dialCtlPeerCfgClosedUserGroup'
_A5='dialCtlPeerCfgSubAddress'
_A4='dialCtlPeerCfgAnswerAddress'
_A3='dialCtlPeerCfgOriginateAddress'
_A2='dialCtlPeerCfgLowerIf'
_A1='dialCtlPeerCfgIfType'
_A0='dialCtlTrapEnable'
_z='dialCtlAcceptMode'
_y='dialCtlPeerStatsEntry'
_x='dialCtlPeerCfgId'
_w='disabled'
_v='enabled'
_u='ifIndex'
_t='InterfaceIndexOrZero'
_s='IANAifType'
_r='callHistoryInfoType'
_q='callHistoryCallOrigin'
_p='callHistoryDisconnectTime'
_o='callHistoryConnectTime'
_n='callHistoryDisconnectCause'
_m='callHistoryLogicalIfIndex'
_l='callHistoryPeerIfIndex'
_k='callHistoryPeerId'
_j='callHistoryPeerSubAddress'
_i='callHistoryPeerAddress'
_h='callActiveInfoType'
_g='callActiveCallOrigin'
_f='callActiveLogicalIfIndex'
_e='callActivePeerIfIndex'
_d='callActivePeerId'
_c='callActivePeerSubAddress'
_b='callActivePeerAddress'
_a='callActiveIndex'
_Z='callActiveSetupTime'
_Y='callback'
_X='answer'
_W='originate'
_V='fax'
_U='packetSwitched'
_T='video'
_S='audio7'
_R='audio31'
_Q='restrictedDigital'
_P='unrestrictedDigital56'
_O='unrestrictedDigital'
_N='speech'
_M='other'
_L='not-accessible'
_K='ifOperStatus'
_J='OctetString'
_I='read-write'
_H='DisplayString'
_G='IF-MIB'
_F='seconds'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='DIAL-CONTROL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB',_s)
InterfaceIndex,InterfaceIndexOrZero,ifIndex,ifOperStatus=mibBuilder.importSymbols(_G,'InterfaceIndex',_t,_u,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TimeStamp')
dialControlMib=ModuleIdentity((1,3,6,1,2,1,10,21))
class AbsoluteCounter32(TextualConvention,Unsigned32):status=_B
_DialControlMibObjects_ObjectIdentity=ObjectIdentity
dialControlMibObjects=_DialControlMibObjects_ObjectIdentity((1,3,6,1,2,1,10,21,1))
_DialCtlConfiguration_ObjectIdentity=ObjectIdentity
dialCtlConfiguration=_DialCtlConfiguration_ObjectIdentity((1,3,6,1,2,1,10,21,1,1))
class _DialCtlAcceptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acceptNone',1),('acceptAll',2),('acceptKnown',3)))
_DialCtlAcceptMode_Type.__name__=_D
_DialCtlAcceptMode_Object=MibScalar
dialCtlAcceptMode=_DialCtlAcceptMode_Object((1,3,6,1,2,1,10,21,1,1,1),_DialCtlAcceptMode_Type())
dialCtlAcceptMode.setMaxAccess(_I)
if mibBuilder.loadTexts:dialCtlAcceptMode.setStatus(_B)
class _DialCtlTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_DialCtlTrapEnable_Type.__name__=_D
_DialCtlTrapEnable_Object=MibScalar
dialCtlTrapEnable=_DialCtlTrapEnable_Object((1,3,6,1,2,1,10,21,1,1,2),_DialCtlTrapEnable_Type())
dialCtlTrapEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:dialCtlTrapEnable.setStatus(_B)
_DialCtlPeer_ObjectIdentity=ObjectIdentity
dialCtlPeer=_DialCtlPeer_ObjectIdentity((1,3,6,1,2,1,10,21,1,2))
_DialCtlPeerCfgTable_Object=MibTable
dialCtlPeerCfgTable=_DialCtlPeerCfgTable_Object((1,3,6,1,2,1,10,21,1,2,1))
if mibBuilder.loadTexts:dialCtlPeerCfgTable.setStatus(_B)
_DialCtlPeerCfgEntry_Object=MibTableRow
dialCtlPeerCfgEntry=_DialCtlPeerCfgEntry_Object((1,3,6,1,2,1,10,21,1,2,1,1))
dialCtlPeerCfgEntry.setIndexNames((0,_A,_x),(0,_G,_u))
if mibBuilder.loadTexts:dialCtlPeerCfgEntry.setStatus(_B)
class _DialCtlPeerCfgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DialCtlPeerCfgId_Type.__name__=_D
_DialCtlPeerCfgId_Object=MibTableColumn
dialCtlPeerCfgId=_DialCtlPeerCfgId_Object((1,3,6,1,2,1,10,21,1,2,1,1,1),_DialCtlPeerCfgId_Type())
dialCtlPeerCfgId.setMaxAccess(_L)
if mibBuilder.loadTexts:dialCtlPeerCfgId.setStatus(_B)
class _DialCtlPeerCfgIfType_Type(IANAifType):defaultValue=1
_DialCtlPeerCfgIfType_Type.__name__=_s
_DialCtlPeerCfgIfType_Object=MibTableColumn
dialCtlPeerCfgIfType=_DialCtlPeerCfgIfType_Object((1,3,6,1,2,1,10,21,1,2,1,1,2),_DialCtlPeerCfgIfType_Type())
dialCtlPeerCfgIfType.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgIfType.setStatus(_B)
class _DialCtlPeerCfgLowerIf_Type(InterfaceIndexOrZero):defaultValue=0
_DialCtlPeerCfgLowerIf_Type.__name__=_t
_DialCtlPeerCfgLowerIf_Object=MibTableColumn
dialCtlPeerCfgLowerIf=_DialCtlPeerCfgLowerIf_Object((1,3,6,1,2,1,10,21,1,2,1,1,3),_DialCtlPeerCfgLowerIf_Type())
dialCtlPeerCfgLowerIf.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgLowerIf.setStatus(_B)
_DialCtlPeerCfgOriginateAddress_Type=DisplayString
_DialCtlPeerCfgOriginateAddress_Object=MibTableColumn
dialCtlPeerCfgOriginateAddress=_DialCtlPeerCfgOriginateAddress_Object((1,3,6,1,2,1,10,21,1,2,1,1,4),_DialCtlPeerCfgOriginateAddress_Type())
dialCtlPeerCfgOriginateAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgOriginateAddress.setStatus(_B)
class _DialCtlPeerCfgAnswerAddress_Type(DisplayString):defaultValue=OctetString('')
_DialCtlPeerCfgAnswerAddress_Type.__name__=_H
_DialCtlPeerCfgAnswerAddress_Object=MibTableColumn
dialCtlPeerCfgAnswerAddress=_DialCtlPeerCfgAnswerAddress_Object((1,3,6,1,2,1,10,21,1,2,1,1,5),_DialCtlPeerCfgAnswerAddress_Type())
dialCtlPeerCfgAnswerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgAnswerAddress.setStatus(_B)
class _DialCtlPeerCfgSubAddress_Type(DisplayString):defaultValue=OctetString('')
_DialCtlPeerCfgSubAddress_Type.__name__=_H
_DialCtlPeerCfgSubAddress_Object=MibTableColumn
dialCtlPeerCfgSubAddress=_DialCtlPeerCfgSubAddress_Object((1,3,6,1,2,1,10,21,1,2,1,1,6),_DialCtlPeerCfgSubAddress_Type())
dialCtlPeerCfgSubAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgSubAddress.setStatus(_B)
class _DialCtlPeerCfgClosedUserGroup_Type(DisplayString):defaultValue=OctetString('')
_DialCtlPeerCfgClosedUserGroup_Type.__name__=_H
_DialCtlPeerCfgClosedUserGroup_Object=MibTableColumn
dialCtlPeerCfgClosedUserGroup=_DialCtlPeerCfgClosedUserGroup_Object((1,3,6,1,2,1,10,21,1,2,1,1,7),_DialCtlPeerCfgClosedUserGroup_Type())
dialCtlPeerCfgClosedUserGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgClosedUserGroup.setStatus(_B)
class _DialCtlPeerCfgSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgSpeed_Type.__name__=_D
_DialCtlPeerCfgSpeed_Object=MibTableColumn
dialCtlPeerCfgSpeed=_DialCtlPeerCfgSpeed_Object((1,3,6,1,2,1,10,21,1,2,1,1,8),_DialCtlPeerCfgSpeed_Type())
dialCtlPeerCfgSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgSpeed.setStatus(_B)
class _DialCtlPeerCfgInfoType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,10)))
_DialCtlPeerCfgInfoType_Type.__name__=_D
_DialCtlPeerCfgInfoType_Object=MibTableColumn
dialCtlPeerCfgInfoType=_DialCtlPeerCfgInfoType_Object((1,3,6,1,2,1,10,21,1,2,1,1,9),_DialCtlPeerCfgInfoType_Type())
dialCtlPeerCfgInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgInfoType.setStatus(_B)
class _DialCtlPeerCfgPermission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),(_X,2),('both',3),(_Y,4),('none',5)))
_DialCtlPeerCfgPermission_Type.__name__=_D
_DialCtlPeerCfgPermission_Object=MibTableColumn
dialCtlPeerCfgPermission=_DialCtlPeerCfgPermission_Object((1,3,6,1,2,1,10,21,1,2,1,1,10),_DialCtlPeerCfgPermission_Type())
dialCtlPeerCfgPermission.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgPermission.setStatus(_B)
class _DialCtlPeerCfgInactivityTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgInactivityTimer_Type.__name__=_D
_DialCtlPeerCfgInactivityTimer_Object=MibTableColumn
dialCtlPeerCfgInactivityTimer=_DialCtlPeerCfgInactivityTimer_Object((1,3,6,1,2,1,10,21,1,2,1,1,11),_DialCtlPeerCfgInactivityTimer_Type())
dialCtlPeerCfgInactivityTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgInactivityTimer.setStatus(_B)
if mibBuilder.loadTexts:dialCtlPeerCfgInactivityTimer.setUnits(_F)
class _DialCtlPeerCfgMinDuration_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgMinDuration_Type.__name__=_D
_DialCtlPeerCfgMinDuration_Object=MibTableColumn
dialCtlPeerCfgMinDuration=_DialCtlPeerCfgMinDuration_Object((1,3,6,1,2,1,10,21,1,2,1,1,12),_DialCtlPeerCfgMinDuration_Type())
dialCtlPeerCfgMinDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgMinDuration.setStatus(_B)
class _DialCtlPeerCfgMaxDuration_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgMaxDuration_Type.__name__=_D
_DialCtlPeerCfgMaxDuration_Object=MibTableColumn
dialCtlPeerCfgMaxDuration=_DialCtlPeerCfgMaxDuration_Object((1,3,6,1,2,1,10,21,1,2,1,1,13),_DialCtlPeerCfgMaxDuration_Type())
dialCtlPeerCfgMaxDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgMaxDuration.setStatus(_B)
class _DialCtlPeerCfgCarrierDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgCarrierDelay_Type.__name__=_D
_DialCtlPeerCfgCarrierDelay_Object=MibTableColumn
dialCtlPeerCfgCarrierDelay=_DialCtlPeerCfgCarrierDelay_Object((1,3,6,1,2,1,10,21,1,2,1,1,14),_DialCtlPeerCfgCarrierDelay_Type())
dialCtlPeerCfgCarrierDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgCarrierDelay.setStatus(_B)
if mibBuilder.loadTexts:dialCtlPeerCfgCarrierDelay.setUnits(_F)
class _DialCtlPeerCfgCallRetries_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgCallRetries_Type.__name__=_D
_DialCtlPeerCfgCallRetries_Object=MibTableColumn
dialCtlPeerCfgCallRetries=_DialCtlPeerCfgCallRetries_Object((1,3,6,1,2,1,10,21,1,2,1,1,15),_DialCtlPeerCfgCallRetries_Type())
dialCtlPeerCfgCallRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgCallRetries.setStatus(_B)
class _DialCtlPeerCfgRetryDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgRetryDelay_Type.__name__=_D
_DialCtlPeerCfgRetryDelay_Object=MibTableColumn
dialCtlPeerCfgRetryDelay=_DialCtlPeerCfgRetryDelay_Object((1,3,6,1,2,1,10,21,1,2,1,1,16),_DialCtlPeerCfgRetryDelay_Type())
dialCtlPeerCfgRetryDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgRetryDelay.setStatus(_B)
if mibBuilder.loadTexts:dialCtlPeerCfgRetryDelay.setUnits(_F)
class _DialCtlPeerCfgFailureDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DialCtlPeerCfgFailureDelay_Type.__name__=_D
_DialCtlPeerCfgFailureDelay_Object=MibTableColumn
dialCtlPeerCfgFailureDelay=_DialCtlPeerCfgFailureDelay_Object((1,3,6,1,2,1,10,21,1,2,1,1,17),_DialCtlPeerCfgFailureDelay_Type())
dialCtlPeerCfgFailureDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgFailureDelay.setStatus(_B)
if mibBuilder.loadTexts:dialCtlPeerCfgFailureDelay.setUnits(_F)
class _DialCtlPeerCfgTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_DialCtlPeerCfgTrapEnable_Type.__name__=_D
_DialCtlPeerCfgTrapEnable_Object=MibTableColumn
dialCtlPeerCfgTrapEnable=_DialCtlPeerCfgTrapEnable_Object((1,3,6,1,2,1,10,21,1,2,1,1,18),_DialCtlPeerCfgTrapEnable_Type())
dialCtlPeerCfgTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgTrapEnable.setStatus(_B)
_DialCtlPeerCfgStatus_Type=RowStatus
_DialCtlPeerCfgStatus_Object=MibTableColumn
dialCtlPeerCfgStatus=_DialCtlPeerCfgStatus_Object((1,3,6,1,2,1,10,21,1,2,1,1,19),_DialCtlPeerCfgStatus_Type())
dialCtlPeerCfgStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dialCtlPeerCfgStatus.setStatus(_B)
_DialCtlPeerStatsTable_Object=MibTable
dialCtlPeerStatsTable=_DialCtlPeerStatsTable_Object((1,3,6,1,2,1,10,21,1,2,2))
if mibBuilder.loadTexts:dialCtlPeerStatsTable.setStatus(_B)
_DialCtlPeerStatsEntry_Object=MibTableRow
dialCtlPeerStatsEntry=_DialCtlPeerStatsEntry_Object((1,3,6,1,2,1,10,21,1,2,2,1))
if mibBuilder.loadTexts:dialCtlPeerStatsEntry.setStatus(_B)
_DialCtlPeerStatsConnectTime_Type=AbsoluteCounter32
_DialCtlPeerStatsConnectTime_Object=MibTableColumn
dialCtlPeerStatsConnectTime=_DialCtlPeerStatsConnectTime_Object((1,3,6,1,2,1,10,21,1,2,2,1,1),_DialCtlPeerStatsConnectTime_Type())
dialCtlPeerStatsConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsConnectTime.setStatus(_B)
if mibBuilder.loadTexts:dialCtlPeerStatsConnectTime.setUnits(_F)
_DialCtlPeerStatsChargedUnits_Type=AbsoluteCounter32
_DialCtlPeerStatsChargedUnits_Object=MibTableColumn
dialCtlPeerStatsChargedUnits=_DialCtlPeerStatsChargedUnits_Object((1,3,6,1,2,1,10,21,1,2,2,1,2),_DialCtlPeerStatsChargedUnits_Type())
dialCtlPeerStatsChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsChargedUnits.setStatus(_B)
_DialCtlPeerStatsSuccessCalls_Type=AbsoluteCounter32
_DialCtlPeerStatsSuccessCalls_Object=MibTableColumn
dialCtlPeerStatsSuccessCalls=_DialCtlPeerStatsSuccessCalls_Object((1,3,6,1,2,1,10,21,1,2,2,1,3),_DialCtlPeerStatsSuccessCalls_Type())
dialCtlPeerStatsSuccessCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsSuccessCalls.setStatus(_B)
_DialCtlPeerStatsFailCalls_Type=AbsoluteCounter32
_DialCtlPeerStatsFailCalls_Object=MibTableColumn
dialCtlPeerStatsFailCalls=_DialCtlPeerStatsFailCalls_Object((1,3,6,1,2,1,10,21,1,2,2,1,4),_DialCtlPeerStatsFailCalls_Type())
dialCtlPeerStatsFailCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsFailCalls.setStatus(_B)
_DialCtlPeerStatsAcceptCalls_Type=AbsoluteCounter32
_DialCtlPeerStatsAcceptCalls_Object=MibTableColumn
dialCtlPeerStatsAcceptCalls=_DialCtlPeerStatsAcceptCalls_Object((1,3,6,1,2,1,10,21,1,2,2,1,5),_DialCtlPeerStatsAcceptCalls_Type())
dialCtlPeerStatsAcceptCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsAcceptCalls.setStatus(_B)
_DialCtlPeerStatsRefuseCalls_Type=AbsoluteCounter32
_DialCtlPeerStatsRefuseCalls_Object=MibTableColumn
dialCtlPeerStatsRefuseCalls=_DialCtlPeerStatsRefuseCalls_Object((1,3,6,1,2,1,10,21,1,2,2,1,6),_DialCtlPeerStatsRefuseCalls_Type())
dialCtlPeerStatsRefuseCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsRefuseCalls.setStatus(_B)
class _DialCtlPeerStatsLastDisconnectCause_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_DialCtlPeerStatsLastDisconnectCause_Type.__name__=_J
_DialCtlPeerStatsLastDisconnectCause_Object=MibTableColumn
dialCtlPeerStatsLastDisconnectCause=_DialCtlPeerStatsLastDisconnectCause_Object((1,3,6,1,2,1,10,21,1,2,2,1,7),_DialCtlPeerStatsLastDisconnectCause_Type())
dialCtlPeerStatsLastDisconnectCause.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsLastDisconnectCause.setStatus(_B)
_DialCtlPeerStatsLastDisconnectText_Type=DisplayString
_DialCtlPeerStatsLastDisconnectText_Object=MibTableColumn
dialCtlPeerStatsLastDisconnectText=_DialCtlPeerStatsLastDisconnectText_Object((1,3,6,1,2,1,10,21,1,2,2,1,8),_DialCtlPeerStatsLastDisconnectText_Type())
dialCtlPeerStatsLastDisconnectText.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsLastDisconnectText.setStatus(_B)
_DialCtlPeerStatsLastSetupTime_Type=TimeStamp
_DialCtlPeerStatsLastSetupTime_Object=MibTableColumn
dialCtlPeerStatsLastSetupTime=_DialCtlPeerStatsLastSetupTime_Object((1,3,6,1,2,1,10,21,1,2,2,1,9),_DialCtlPeerStatsLastSetupTime_Type())
dialCtlPeerStatsLastSetupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dialCtlPeerStatsLastSetupTime.setStatus(_B)
_CallActive_ObjectIdentity=ObjectIdentity
callActive=_CallActive_ObjectIdentity((1,3,6,1,2,1,10,21,1,3))
_CallActiveTable_Object=MibTable
callActiveTable=_CallActiveTable_Object((1,3,6,1,2,1,10,21,1,3,1))
if mibBuilder.loadTexts:callActiveTable.setStatus(_B)
_CallActiveEntry_Object=MibTableRow
callActiveEntry=_CallActiveEntry_Object((1,3,6,1,2,1,10,21,1,3,1,1))
callActiveEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:callActiveEntry.setStatus(_B)
_CallActiveSetupTime_Type=TimeStamp
_CallActiveSetupTime_Object=MibTableColumn
callActiveSetupTime=_CallActiveSetupTime_Object((1,3,6,1,2,1,10,21,1,3,1,1,1),_CallActiveSetupTime_Type())
callActiveSetupTime.setMaxAccess(_L)
if mibBuilder.loadTexts:callActiveSetupTime.setStatus(_B)
class _CallActiveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CallActiveIndex_Type.__name__=_D
_CallActiveIndex_Object=MibTableColumn
callActiveIndex=_CallActiveIndex_Object((1,3,6,1,2,1,10,21,1,3,1,1,2),_CallActiveIndex_Type())
callActiveIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:callActiveIndex.setStatus(_B)
_CallActivePeerAddress_Type=DisplayString
_CallActivePeerAddress_Object=MibTableColumn
callActivePeerAddress=_CallActivePeerAddress_Object((1,3,6,1,2,1,10,21,1,3,1,1,3),_CallActivePeerAddress_Type())
callActivePeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:callActivePeerAddress.setStatus(_B)
_CallActivePeerSubAddress_Type=DisplayString
_CallActivePeerSubAddress_Object=MibTableColumn
callActivePeerSubAddress=_CallActivePeerSubAddress_Object((1,3,6,1,2,1,10,21,1,3,1,1,4),_CallActivePeerSubAddress_Type())
callActivePeerSubAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:callActivePeerSubAddress.setStatus(_B)
class _CallActivePeerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CallActivePeerId_Type.__name__=_D
_CallActivePeerId_Object=MibTableColumn
callActivePeerId=_CallActivePeerId_Object((1,3,6,1,2,1,10,21,1,3,1,1,5),_CallActivePeerId_Type())
callActivePeerId.setMaxAccess(_C)
if mibBuilder.loadTexts:callActivePeerId.setStatus(_B)
class _CallActivePeerIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CallActivePeerIfIndex_Type.__name__=_D
_CallActivePeerIfIndex_Object=MibTableColumn
callActivePeerIfIndex=_CallActivePeerIfIndex_Object((1,3,6,1,2,1,10,21,1,3,1,1,6),_CallActivePeerIfIndex_Type())
callActivePeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callActivePeerIfIndex.setStatus(_B)
_CallActiveLogicalIfIndex_Type=InterfaceIndexOrZero
_CallActiveLogicalIfIndex_Object=MibTableColumn
callActiveLogicalIfIndex=_CallActiveLogicalIfIndex_Object((1,3,6,1,2,1,10,21,1,3,1,1,7),_CallActiveLogicalIfIndex_Type())
callActiveLogicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveLogicalIfIndex.setStatus(_B)
_CallActiveConnectTime_Type=TimeStamp
_CallActiveConnectTime_Object=MibTableColumn
callActiveConnectTime=_CallActiveConnectTime_Object((1,3,6,1,2,1,10,21,1,3,1,1,8),_CallActiveConnectTime_Type())
callActiveConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveConnectTime.setStatus(_B)
class _CallActiveCallState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('connecting',2),('connected',3),('active',4)))
_CallActiveCallState_Type.__name__=_D
_CallActiveCallState_Object=MibTableColumn
callActiveCallState=_CallActiveCallState_Object((1,3,6,1,2,1,10,21,1,3,1,1,9),_CallActiveCallState_Type())
callActiveCallState.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveCallState.setStatus(_B)
class _CallActiveCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_CallActiveCallOrigin_Type.__name__=_D
_CallActiveCallOrigin_Object=MibTableColumn
callActiveCallOrigin=_CallActiveCallOrigin_Object((1,3,6,1,2,1,10,21,1,3,1,1,10),_CallActiveCallOrigin_Type())
callActiveCallOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveCallOrigin.setStatus(_B)
_CallActiveChargedUnits_Type=AbsoluteCounter32
_CallActiveChargedUnits_Object=MibTableColumn
callActiveChargedUnits=_CallActiveChargedUnits_Object((1,3,6,1,2,1,10,21,1,3,1,1,11),_CallActiveChargedUnits_Type())
callActiveChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveChargedUnits.setStatus(_B)
class _CallActiveInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,10)))
_CallActiveInfoType_Type.__name__=_D
_CallActiveInfoType_Object=MibTableColumn
callActiveInfoType=_CallActiveInfoType_Object((1,3,6,1,2,1,10,21,1,3,1,1,12),_CallActiveInfoType_Type())
callActiveInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveInfoType.setStatus(_B)
_CallActiveTransmitPackets_Type=AbsoluteCounter32
_CallActiveTransmitPackets_Object=MibTableColumn
callActiveTransmitPackets=_CallActiveTransmitPackets_Object((1,3,6,1,2,1,10,21,1,3,1,1,13),_CallActiveTransmitPackets_Type())
callActiveTransmitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveTransmitPackets.setStatus(_B)
_CallActiveTransmitBytes_Type=AbsoluteCounter32
_CallActiveTransmitBytes_Object=MibTableColumn
callActiveTransmitBytes=_CallActiveTransmitBytes_Object((1,3,6,1,2,1,10,21,1,3,1,1,14),_CallActiveTransmitBytes_Type())
callActiveTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveTransmitBytes.setStatus(_B)
_CallActiveReceivePackets_Type=AbsoluteCounter32
_CallActiveReceivePackets_Object=MibTableColumn
callActiveReceivePackets=_CallActiveReceivePackets_Object((1,3,6,1,2,1,10,21,1,3,1,1,15),_CallActiveReceivePackets_Type())
callActiveReceivePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveReceivePackets.setStatus(_B)
_CallActiveReceiveBytes_Type=AbsoluteCounter32
_CallActiveReceiveBytes_Object=MibTableColumn
callActiveReceiveBytes=_CallActiveReceiveBytes_Object((1,3,6,1,2,1,10,21,1,3,1,1,16),_CallActiveReceiveBytes_Type())
callActiveReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:callActiveReceiveBytes.setStatus(_B)
_CallHistory_ObjectIdentity=ObjectIdentity
callHistory=_CallHistory_ObjectIdentity((1,3,6,1,2,1,10,21,1,4))
class _CallHistoryTableMaxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CallHistoryTableMaxLength_Type.__name__=_D
_CallHistoryTableMaxLength_Object=MibScalar
callHistoryTableMaxLength=_CallHistoryTableMaxLength_Object((1,3,6,1,2,1,10,21,1,4,1),_CallHistoryTableMaxLength_Type())
callHistoryTableMaxLength.setMaxAccess(_I)
if mibBuilder.loadTexts:callHistoryTableMaxLength.setStatus(_B)
class _CallHistoryRetainTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CallHistoryRetainTimer_Type.__name__=_D
_CallHistoryRetainTimer_Object=MibScalar
callHistoryRetainTimer=_CallHistoryRetainTimer_Object((1,3,6,1,2,1,10,21,1,4,2),_CallHistoryRetainTimer_Type())
callHistoryRetainTimer.setMaxAccess(_I)
if mibBuilder.loadTexts:callHistoryRetainTimer.setStatus(_B)
if mibBuilder.loadTexts:callHistoryRetainTimer.setUnits('minutes')
_CallHistoryTable_Object=MibTable
callHistoryTable=_CallHistoryTable_Object((1,3,6,1,2,1,10,21,1,4,3))
if mibBuilder.loadTexts:callHistoryTable.setStatus(_B)
_CallHistoryEntry_Object=MibTableRow
callHistoryEntry=_CallHistoryEntry_Object((1,3,6,1,2,1,10,21,1,4,3,1))
callHistoryEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:callHistoryEntry.setStatus(_B)
_CallHistoryPeerAddress_Type=DisplayString
_CallHistoryPeerAddress_Object=MibTableColumn
callHistoryPeerAddress=_CallHistoryPeerAddress_Object((1,3,6,1,2,1,10,21,1,4,3,1,1),_CallHistoryPeerAddress_Type())
callHistoryPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryPeerAddress.setStatus(_B)
_CallHistoryPeerSubAddress_Type=DisplayString
_CallHistoryPeerSubAddress_Object=MibTableColumn
callHistoryPeerSubAddress=_CallHistoryPeerSubAddress_Object((1,3,6,1,2,1,10,21,1,4,3,1,2),_CallHistoryPeerSubAddress_Type())
callHistoryPeerSubAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryPeerSubAddress.setStatus(_B)
class _CallHistoryPeerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CallHistoryPeerId_Type.__name__=_D
_CallHistoryPeerId_Object=MibTableColumn
callHistoryPeerId=_CallHistoryPeerId_Object((1,3,6,1,2,1,10,21,1,4,3,1,3),_CallHistoryPeerId_Type())
callHistoryPeerId.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryPeerId.setStatus(_B)
class _CallHistoryPeerIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CallHistoryPeerIfIndex_Type.__name__=_D
_CallHistoryPeerIfIndex_Object=MibTableColumn
callHistoryPeerIfIndex=_CallHistoryPeerIfIndex_Object((1,3,6,1,2,1,10,21,1,4,3,1,4),_CallHistoryPeerIfIndex_Type())
callHistoryPeerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryPeerIfIndex.setStatus(_B)
_CallHistoryLogicalIfIndex_Type=InterfaceIndex
_CallHistoryLogicalIfIndex_Object=MibTableColumn
callHistoryLogicalIfIndex=_CallHistoryLogicalIfIndex_Object((1,3,6,1,2,1,10,21,1,4,3,1,5),_CallHistoryLogicalIfIndex_Type())
callHistoryLogicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryLogicalIfIndex.setStatus(_B)
class _CallHistoryDisconnectCause_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CallHistoryDisconnectCause_Type.__name__=_J
_CallHistoryDisconnectCause_Object=MibTableColumn
callHistoryDisconnectCause=_CallHistoryDisconnectCause_Object((1,3,6,1,2,1,10,21,1,4,3,1,6),_CallHistoryDisconnectCause_Type())
callHistoryDisconnectCause.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryDisconnectCause.setStatus(_B)
_CallHistoryDisconnectText_Type=DisplayString
_CallHistoryDisconnectText_Object=MibTableColumn
callHistoryDisconnectText=_CallHistoryDisconnectText_Object((1,3,6,1,2,1,10,21,1,4,3,1,7),_CallHistoryDisconnectText_Type())
callHistoryDisconnectText.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryDisconnectText.setStatus(_B)
_CallHistoryConnectTime_Type=TimeStamp
_CallHistoryConnectTime_Object=MibTableColumn
callHistoryConnectTime=_CallHistoryConnectTime_Object((1,3,6,1,2,1,10,21,1,4,3,1,8),_CallHistoryConnectTime_Type())
callHistoryConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryConnectTime.setStatus(_B)
_CallHistoryDisconnectTime_Type=TimeStamp
_CallHistoryDisconnectTime_Object=MibTableColumn
callHistoryDisconnectTime=_CallHistoryDisconnectTime_Object((1,3,6,1,2,1,10,21,1,4,3,1,9),_CallHistoryDisconnectTime_Type())
callHistoryDisconnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryDisconnectTime.setStatus(_B)
class _CallHistoryCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_CallHistoryCallOrigin_Type.__name__=_D
_CallHistoryCallOrigin_Object=MibTableColumn
callHistoryCallOrigin=_CallHistoryCallOrigin_Object((1,3,6,1,2,1,10,21,1,4,3,1,10),_CallHistoryCallOrigin_Type())
callHistoryCallOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryCallOrigin.setStatus(_B)
_CallHistoryChargedUnits_Type=AbsoluteCounter32
_CallHistoryChargedUnits_Object=MibTableColumn
callHistoryChargedUnits=_CallHistoryChargedUnits_Object((1,3,6,1,2,1,10,21,1,4,3,1,11),_CallHistoryChargedUnits_Type())
callHistoryChargedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryChargedUnits.setStatus(_B)
class _CallHistoryInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,10)))
_CallHistoryInfoType_Type.__name__=_D
_CallHistoryInfoType_Object=MibTableColumn
callHistoryInfoType=_CallHistoryInfoType_Object((1,3,6,1,2,1,10,21,1,4,3,1,12),_CallHistoryInfoType_Type())
callHistoryInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryInfoType.setStatus(_B)
_CallHistoryTransmitPackets_Type=AbsoluteCounter32
_CallHistoryTransmitPackets_Object=MibTableColumn
callHistoryTransmitPackets=_CallHistoryTransmitPackets_Object((1,3,6,1,2,1,10,21,1,4,3,1,13),_CallHistoryTransmitPackets_Type())
callHistoryTransmitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryTransmitPackets.setStatus(_B)
_CallHistoryTransmitBytes_Type=AbsoluteCounter32
_CallHistoryTransmitBytes_Object=MibTableColumn
callHistoryTransmitBytes=_CallHistoryTransmitBytes_Object((1,3,6,1,2,1,10,21,1,4,3,1,14),_CallHistoryTransmitBytes_Type())
callHistoryTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryTransmitBytes.setStatus(_B)
_CallHistoryReceivePackets_Type=AbsoluteCounter32
_CallHistoryReceivePackets_Object=MibTableColumn
callHistoryReceivePackets=_CallHistoryReceivePackets_Object((1,3,6,1,2,1,10,21,1,4,3,1,15),_CallHistoryReceivePackets_Type())
callHistoryReceivePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryReceivePackets.setStatus(_B)
_CallHistoryReceiveBytes_Type=AbsoluteCounter32
_CallHistoryReceiveBytes_Object=MibTableColumn
callHistoryReceiveBytes=_CallHistoryReceiveBytes_Object((1,3,6,1,2,1,10,21,1,4,3,1,16),_CallHistoryReceiveBytes_Type())
callHistoryReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:callHistoryReceiveBytes.setStatus(_B)
_DialControlMibTrapPrefix_ObjectIdentity=ObjectIdentity
dialControlMibTrapPrefix=_DialControlMibTrapPrefix_ObjectIdentity((1,3,6,1,2,1,10,21,2))
_DialControlMibTraps_ObjectIdentity=ObjectIdentity
dialControlMibTraps=_DialControlMibTraps_ObjectIdentity((1,3,6,1,2,1,10,21,2,0))
_DialControlMibConformance_ObjectIdentity=ObjectIdentity
dialControlMibConformance=_DialControlMibConformance_ObjectIdentity((1,3,6,1,2,1,10,21,3))
_DialControlMibCompliances_ObjectIdentity=ObjectIdentity
dialControlMibCompliances=_DialControlMibCompliances_ObjectIdentity((1,3,6,1,2,1,10,21,3,1))
_DialControlMibGroups_ObjectIdentity=ObjectIdentity
dialControlMibGroups=_DialControlMibGroups_ObjectIdentity((1,3,6,1,2,1,10,21,3,2))
dialCtlPeerCfgEntry.registerAugmentions((_A,_y))
dialCtlPeerStatsEntry.setIndexNames(*dialCtlPeerCfgEntry.getIndexNames())
dialControlGroup=ObjectGroup((1,3,6,1,2,1,10,21,3,2,1))
dialControlGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:dialControlGroup.setStatus(_B)
callActiveGroup=ObjectGroup((1,3,6,1,2,1,10,21,3,2,2))
callActiveGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_AS),(_A,_AT),(_A,_g),(_A,_AU),(_A,_h),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:callActiveGroup.setStatus(_B)
callHistoryGroup=ObjectGroup((1,3,6,1,2,1,10,21,3,2,3))
callHistoryGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_Ab),(_A,_o),(_A,_p),(_A,_q),(_A,_Ac),(_A,_r),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:callHistoryGroup.setStatus(_B)
dialCtlPeerCallInformation=NotificationType((1,3,6,1,2,1,10,21,2,0,1))
dialCtlPeerCallInformation.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_G,_K),(_A,_i),(_A,_j),(_A,_n),(_A,_o),(_A,_p),(_A,_r),(_A,_q)))
if mibBuilder.loadTexts:dialCtlPeerCallInformation.setStatus(_B)
dialCtlPeerCallSetup=NotificationType((1,3,6,1,2,1,10,21,2,0,2))
dialCtlPeerCallSetup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_G,_K),(_A,_b),(_A,_c),(_A,_h),(_A,_g)))
if mibBuilder.loadTexts:dialCtlPeerCallSetup.setStatus(_B)
callNotificationsGroup=NotificationGroup((1,3,6,1,2,1,10,21,3,2,4))
callNotificationsGroup.setObjects(*((_A,_Ah),(_A,_Ai)))
if mibBuilder.loadTexts:callNotificationsGroup.setStatus(_B)
dialControlMibCompliance=ModuleCompliance((1,3,6,1,2,1,10,21,3,1,1))
dialControlMibCompliance.setObjects(*((_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:dialControlMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AbsoluteCounter32':AbsoluteCounter32,'dialControlMib':dialControlMib,'dialControlMibObjects':dialControlMibObjects,'dialCtlConfiguration':dialCtlConfiguration,_z:dialCtlAcceptMode,_A0:dialCtlTrapEnable,'dialCtlPeer':dialCtlPeer,'dialCtlPeerCfgTable':dialCtlPeerCfgTable,'dialCtlPeerCfgEntry':dialCtlPeerCfgEntry,_x:dialCtlPeerCfgId,_A1:dialCtlPeerCfgIfType,_A2:dialCtlPeerCfgLowerIf,_A3:dialCtlPeerCfgOriginateAddress,_A4:dialCtlPeerCfgAnswerAddress,_A5:dialCtlPeerCfgSubAddress,_A6:dialCtlPeerCfgClosedUserGroup,_A7:dialCtlPeerCfgSpeed,_A8:dialCtlPeerCfgInfoType,_A9:dialCtlPeerCfgPermission,_AA:dialCtlPeerCfgInactivityTimer,_AB:dialCtlPeerCfgMinDuration,_AC:dialCtlPeerCfgMaxDuration,_AD:dialCtlPeerCfgCarrierDelay,_AE:dialCtlPeerCfgCallRetries,_AF:dialCtlPeerCfgRetryDelay,_AG:dialCtlPeerCfgFailureDelay,_AH:dialCtlPeerCfgTrapEnable,_AI:dialCtlPeerCfgStatus,'dialCtlPeerStatsTable':dialCtlPeerStatsTable,_y:dialCtlPeerStatsEntry,_AJ:dialCtlPeerStatsConnectTime,_AK:dialCtlPeerStatsChargedUnits,_AL:dialCtlPeerStatsSuccessCalls,_AM:dialCtlPeerStatsFailCalls,_AN:dialCtlPeerStatsAcceptCalls,_AO:dialCtlPeerStatsRefuseCalls,_AP:dialCtlPeerStatsLastDisconnectCause,_AQ:dialCtlPeerStatsLastDisconnectText,_AR:dialCtlPeerStatsLastSetupTime,'callActive':callActive,'callActiveTable':callActiveTable,'callActiveEntry':callActiveEntry,_Z:callActiveSetupTime,_a:callActiveIndex,_b:callActivePeerAddress,_c:callActivePeerSubAddress,_d:callActivePeerId,_e:callActivePeerIfIndex,_f:callActiveLogicalIfIndex,_AS:callActiveConnectTime,_AT:callActiveCallState,_g:callActiveCallOrigin,_AU:callActiveChargedUnits,_h:callActiveInfoType,_AV:callActiveTransmitPackets,_AW:callActiveTransmitBytes,_AX:callActiveReceivePackets,_AY:callActiveReceiveBytes,'callHistory':callHistory,_AZ:callHistoryTableMaxLength,_Aa:callHistoryRetainTimer,'callHistoryTable':callHistoryTable,'callHistoryEntry':callHistoryEntry,_i:callHistoryPeerAddress,_j:callHistoryPeerSubAddress,_k:callHistoryPeerId,_l:callHistoryPeerIfIndex,_m:callHistoryLogicalIfIndex,_n:callHistoryDisconnectCause,_Ab:callHistoryDisconnectText,_o:callHistoryConnectTime,_p:callHistoryDisconnectTime,_q:callHistoryCallOrigin,_Ac:callHistoryChargedUnits,_r:callHistoryInfoType,_Ad:callHistoryTransmitPackets,_Ae:callHistoryTransmitBytes,_Af:callHistoryReceivePackets,_Ag:callHistoryReceiveBytes,'dialControlMibTrapPrefix':dialControlMibTrapPrefix,'dialControlMibTraps':dialControlMibTraps,_Ah:dialCtlPeerCallInformation,_Ai:dialCtlPeerCallSetup,'dialControlMibConformance':dialControlMibConformance,'dialControlMibCompliances':dialControlMibCompliances,'dialControlMibCompliance':dialControlMibCompliance,'dialControlMibGroups':dialControlMibGroups,_Aj:dialControlGroup,_Ak:callActiveGroup,_Al:callHistoryGroup,_Am:callNotificationsGroup})