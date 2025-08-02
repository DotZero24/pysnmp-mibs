_B6='dspuLuGroupV11R01'
_B5='dspuPuGroupV11R01'
_B4='dspuLuGroup'
_B3='dspuPuGroup'
_B2='dspuPuOperRemoteAddress'
_B1='dspuPuAdminRemoteAddress'
_B0='dspuSapRowStatus'
_A_='dspuSapType'
_Az='dspuPooledLuPeerLuLocalAddress'
_Ay='dspuPooledLuPeerPuIndex'
_Ax='dspuPoolClassOperDnStreamLuDefs'
_Aw='dspuPoolClassOperUpStreamLuDefs'
_Av='dspuPoolClassInactivityTimeout'
_Au='dspuPoolClassName'
_At='dspuNodeLastConfigChgTime'
_As='dspuNodeActivationWindow'
_Ar='dspuNodeDefaultPuMaxIframe'
_Aq='dspuNodeDefaultPuWindowSize'
_Ap='dspuNodeDefaultPu'
_Ao='dspuNodeRsrbVirtualMacAddress'
_An='dspuNodeRsrbTargetVirtualRing'
_Am='dspuNodeRsrbBridgeNumber'
_Al='dspuNodeRsrbLocalVirtualRing'
_Ak='dspuNodeRsrb'
_Aj='dedicated'
_Ai='dspuLuAdminLuLocalAddress'
_Ah='otherError'
_Ag='formatUnknown'
_Af='dnstreamPu'
_Ae='upstreamPu'
_Ad='dspuSapGroup'
_Ac='dspuPooledLuGroup'
_Ab='dspuPoolClassGroup'
_Aa='dspuNodeGroup'
_AZ='dspuLuOperLastActivationFailureReason'
_AY='dspuSapOperState'
_AX='dspuLuOperSessionState'
_AW='dspuLuOperFsmState'
_AV='dspuLuOperPeerLuLocalAddress'
_AU='dspuLuOperPeerPuIndex'
_AT='dspuLuOperPoolClassName'
_AS='dspuLuOperType'
_AR='dspuLuAdminRowStatus'
_AQ='dspuLuAdminPeerLuLocalAddress'
_AP='dspuLuAdminPeerPuIndex'
_AO='dspuLuAdminPoolClassName'
_AN='dspuLuAdminType'
_AM='dspuPuStatsActivationFailures'
_AL='dspuPuStatsBindLus'
_AK='dspuPuStatsInactiveLus'
_AJ='dspuPuStatsActiveLus'
_AI='dspuPuStatsRcvdNegativeRsps'
_AH='dspuPuStatsSentNegativeRsps'
_AG='dspuPuStatsRcvdFrames'
_AF='dspuPuStatsSentFrames'
_AE='dspuPuStatsRcvdBytes'
_AD='dspuPuStatsSentBytes'
_AC='dspuPuOperLastStateChgTime'
_AB='dspuPuOperStartTime'
_AA='dspuPuOperFsmState'
_A9='dspuPuOperFocalPoint'
_A8='dspuPuOperDlcPort'
_A7='dspuPuOperDlcUnit'
_A6='dspuPuOperDlcType'
_A5='dspuPuOperStartPu'
_A4='dspuPuOperLinkRetryTimeout'
_A3='dspuPuOperLinkRetryCount'
_A2='dspuPuOperMaxIframe'
_A1='dspuPuOperWindowSize'
_A0='dspuPuOperXidFmt'
_z='dspuPuOperXid'
_y='dspuPuOperLocalSapAddress'
_x='dspuPuOperRemoteSapAddress'
_w='dspuPuOperRemoteMacAddress'
_v='dspuPuOperType'
_u='dspuPuAdminRowStatus'
_t='dspuPuAdminFocalPoint'
_s='dspuPuAdminDlcPort'
_r='dspuPuAdminDlcUnit'
_q='dspuPuAdminDlcType'
_p='dspuPuAdminStartPu'
_o='dspuPuAdminLinkRetryTimeout'
_n='dspuPuAdminLinkRetryCount'
_m='dspuPuAdminMaxIframe'
_l='dspuPuAdminWindowSize'
_k='dspuPuAdminXidFmt'
_j='dspuPuAdminXid'
_i='dspuPuAdminLocalSapAddress'
_h='dspuPuAdminRemoteSapAddress'
_g='dspuPuAdminRemoteMacAddress'
_f='dspuPuAdminType'
_e='dspuPuAdminName'
_d='dspuSapAddress'
_c='dspuSapDlcPort'
_b='dspuSapDlcUnit'
_a='dspuSapDlcType'
_Z='qllc'
_Y='fddi'
_X='framerelay'
_W='rsrb'
_V='tokenRing'
_U='ethernet'
_T='sdlc'
_S='undefined'
_R='dspuPuAdminIndex'
_Q='dspuPoolClassIndex'
_P='dspuLuOperLuLocalAddress'
_O='dspuPuStatsLastActivationFailureReason'
_N='dspuPuOperIndex'
_M='dspuLuOperState'
_L='obsolete'
_K='dspuPuOperState'
_J='TruthValue'
_I='DisplayString'
_H='not-accessible'
_G='dspuPuOperName'
_F='read-write'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='current'
_A='CISCO-DSPU-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_J)
ciscoDspuMIB=ModuleIdentity((1,3,6,1,4,1,9,9,24))
if mibBuilder.loadTexts:ciscoDspuMIB.setRevisions(('1995-12-18 00:00','1995-08-15 00:00','1995-01-25 00:00'))
_DspuObjects_ObjectIdentity=ObjectIdentity
dspuObjects=_DspuObjects_ObjectIdentity((1,3,6,1,4,1,9,9,24,1))
_DspuNode_ObjectIdentity=ObjectIdentity
dspuNode=_DspuNode_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,1))
class _DspuNodeRsrb_Type(TruthValue):defaultValue=2
_DspuNodeRsrb_Type.__name__=_J
_DspuNodeRsrb_Object=MibScalar
dspuNodeRsrb=_DspuNodeRsrb_Object((1,3,6,1,4,1,9,9,24,1,1,1),_DspuNodeRsrb_Type())
dspuNodeRsrb.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeRsrb.setStatus(_B)
class _DspuNodeRsrbLocalVirtualRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_DspuNodeRsrbLocalVirtualRing_Type.__name__=_C
_DspuNodeRsrbLocalVirtualRing_Object=MibScalar
dspuNodeRsrbLocalVirtualRing=_DspuNodeRsrbLocalVirtualRing_Object((1,3,6,1,4,1,9,9,24,1,1,2),_DspuNodeRsrbLocalVirtualRing_Type())
dspuNodeRsrbLocalVirtualRing.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeRsrbLocalVirtualRing.setStatus(_B)
class _DspuNodeRsrbBridgeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_DspuNodeRsrbBridgeNumber_Type.__name__=_C
_DspuNodeRsrbBridgeNumber_Object=MibScalar
dspuNodeRsrbBridgeNumber=_DspuNodeRsrbBridgeNumber_Object((1,3,6,1,4,1,9,9,24,1,1,3),_DspuNodeRsrbBridgeNumber_Type())
dspuNodeRsrbBridgeNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeRsrbBridgeNumber.setStatus(_B)
class _DspuNodeRsrbTargetVirtualRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_DspuNodeRsrbTargetVirtualRing_Type.__name__=_C
_DspuNodeRsrbTargetVirtualRing_Object=MibScalar
dspuNodeRsrbTargetVirtualRing=_DspuNodeRsrbTargetVirtualRing_Object((1,3,6,1,4,1,9,9,24,1,1,4),_DspuNodeRsrbTargetVirtualRing_Type())
dspuNodeRsrbTargetVirtualRing.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeRsrbTargetVirtualRing.setStatus(_B)
_DspuNodeRsrbVirtualMacAddress_Type=MacAddress
_DspuNodeRsrbVirtualMacAddress_Object=MibScalar
dspuNodeRsrbVirtualMacAddress=_DspuNodeRsrbVirtualMacAddress_Object((1,3,6,1,4,1,9,9,24,1,1,5),_DspuNodeRsrbVirtualMacAddress_Type())
dspuNodeRsrbVirtualMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeRsrbVirtualMacAddress.setStatus(_B)
class _DspuNodeDefaultPu_Type(TruthValue):defaultValue=2
_DspuNodeDefaultPu_Type.__name__=_J
_DspuNodeDefaultPu_Object=MibScalar
dspuNodeDefaultPu=_DspuNodeDefaultPu_Object((1,3,6,1,4,1,9,9,24,1,1,6),_DspuNodeDefaultPu_Type())
dspuNodeDefaultPu.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeDefaultPu.setStatus(_B)
class _DspuNodeDefaultPuWindowSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_DspuNodeDefaultPuWindowSize_Type.__name__=_C
_DspuNodeDefaultPuWindowSize_Object=MibScalar
dspuNodeDefaultPuWindowSize=_DspuNodeDefaultPuWindowSize_Object((1,3,6,1,4,1,9,9,24,1,1,7),_DspuNodeDefaultPuWindowSize_Type())
dspuNodeDefaultPuWindowSize.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeDefaultPuWindowSize.setStatus(_B)
class _DspuNodeDefaultPuMaxIframe_Type(Integer32):defaultValue=1472;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,18432))
_DspuNodeDefaultPuMaxIframe_Type.__name__=_C
_DspuNodeDefaultPuMaxIframe_Object=MibScalar
dspuNodeDefaultPuMaxIframe=_DspuNodeDefaultPuMaxIframe_Object((1,3,6,1,4,1,9,9,24,1,1,8),_DspuNodeDefaultPuMaxIframe_Type())
dspuNodeDefaultPuMaxIframe.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeDefaultPuMaxIframe.setStatus(_B)
class _DspuNodeActivationWindow_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DspuNodeActivationWindow_Type.__name__=_C
_DspuNodeActivationWindow_Object=MibScalar
dspuNodeActivationWindow=_DspuNodeActivationWindow_Object((1,3,6,1,4,1,9,9,24,1,1,9),_DspuNodeActivationWindow_Type())
dspuNodeActivationWindow.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuNodeActivationWindow.setStatus(_B)
_DspuNodeLastConfigChgTime_Type=TimeStamp
_DspuNodeLastConfigChgTime_Object=MibScalar
dspuNodeLastConfigChgTime=_DspuNodeLastConfigChgTime_Object((1,3,6,1,4,1,9,9,24,1,1,10),_DspuNodeLastConfigChgTime_Type())
dspuNodeLastConfigChgTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuNodeLastConfigChgTime.setStatus(_B)
_DspuPoolClass_ObjectIdentity=ObjectIdentity
dspuPoolClass=_DspuPoolClass_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,2))
_DspuPoolClassTable_Object=MibTable
dspuPoolClassTable=_DspuPoolClassTable_Object((1,3,6,1,4,1,9,9,24,1,2,1))
if mibBuilder.loadTexts:dspuPoolClassTable.setStatus(_B)
_DspuPoolClassEntry_Object=MibTableRow
dspuPoolClassEntry=_DspuPoolClassEntry_Object((1,3,6,1,4,1,9,9,24,1,2,1,1))
dspuPoolClassEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:dspuPoolClassEntry.setStatus(_B)
class _DspuPoolClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DspuPoolClassIndex_Type.__name__=_C
_DspuPoolClassIndex_Object=MibTableColumn
dspuPoolClassIndex=_DspuPoolClassIndex_Object((1,3,6,1,4,1,9,9,24,1,2,1,1,1),_DspuPoolClassIndex_Type())
dspuPoolClassIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuPoolClassIndex.setStatus(_B)
class _DspuPoolClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_DspuPoolClassName_Type.__name__=_I
_DspuPoolClassName_Object=MibTableColumn
dspuPoolClassName=_DspuPoolClassName_Object((1,3,6,1,4,1,9,9,24,1,2,1,1,2),_DspuPoolClassName_Type())
dspuPoolClassName.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuPoolClassName.setStatus(_B)
class _DspuPoolClassInactivityTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPoolClassInactivityTimeout_Type.__name__=_C
_DspuPoolClassInactivityTimeout_Object=MibTableColumn
dspuPoolClassInactivityTimeout=_DspuPoolClassInactivityTimeout_Object((1,3,6,1,4,1,9,9,24,1,2,1,1,3),_DspuPoolClassInactivityTimeout_Type())
dspuPoolClassInactivityTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:dspuPoolClassInactivityTimeout.setStatus(_B)
_DspuPoolClassOperUpStreamLuDefs_Type=Integer32
_DspuPoolClassOperUpStreamLuDefs_Object=MibTableColumn
dspuPoolClassOperUpStreamLuDefs=_DspuPoolClassOperUpStreamLuDefs_Object((1,3,6,1,4,1,9,9,24,1,2,1,1,4),_DspuPoolClassOperUpStreamLuDefs_Type())
dspuPoolClassOperUpStreamLuDefs.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPoolClassOperUpStreamLuDefs.setStatus(_B)
_DspuPoolClassOperDnStreamLuDefs_Type=Integer32
_DspuPoolClassOperDnStreamLuDefs_Object=MibTableColumn
dspuPoolClassOperDnStreamLuDefs=_DspuPoolClassOperDnStreamLuDefs_Object((1,3,6,1,4,1,9,9,24,1,2,1,1,5),_DspuPoolClassOperDnStreamLuDefs_Type())
dspuPoolClassOperDnStreamLuDefs.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPoolClassOperDnStreamLuDefs.setStatus(_B)
_DspuPooledLu_ObjectIdentity=ObjectIdentity
dspuPooledLu=_DspuPooledLu_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,3))
_DspuPooledLuTable_Object=MibTable
dspuPooledLuTable=_DspuPooledLuTable_Object((1,3,6,1,4,1,9,9,24,1,3,1))
if mibBuilder.loadTexts:dspuPooledLuTable.setStatus(_B)
_DspuPooledLuEntry_Object=MibTableRow
dspuPooledLuEntry=_DspuPooledLuEntry_Object((1,3,6,1,4,1,9,9,24,1,3,1,1))
dspuPooledLuEntry.setIndexNames((0,_A,_Q),(0,_A,_N),(0,_A,_P))
if mibBuilder.loadTexts:dspuPooledLuEntry.setStatus(_B)
_DspuPooledLuPeerPuIndex_Type=Integer32
_DspuPooledLuPeerPuIndex_Object=MibTableColumn
dspuPooledLuPeerPuIndex=_DspuPooledLuPeerPuIndex_Object((1,3,6,1,4,1,9,9,24,1,3,1,1,1),_DspuPooledLuPeerPuIndex_Type())
dspuPooledLuPeerPuIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPooledLuPeerPuIndex.setStatus(_B)
class _DspuPooledLuPeerLuLocalAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_DspuPooledLuPeerLuLocalAddress_Type.__name__=_C
_DspuPooledLuPeerLuLocalAddress_Object=MibTableColumn
dspuPooledLuPeerLuLocalAddress=_DspuPooledLuPeerLuLocalAddress_Object((1,3,6,1,4,1,9,9,24,1,3,1,1,2),_DspuPooledLuPeerLuLocalAddress_Type())
dspuPooledLuPeerLuLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPooledLuPeerLuLocalAddress.setStatus(_B)
_DspuPu_ObjectIdentity=ObjectIdentity
dspuPu=_DspuPu_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,4))
_DspuPuAdminTable_Object=MibTable
dspuPuAdminTable=_DspuPuAdminTable_Object((1,3,6,1,4,1,9,9,24,1,4,1))
if mibBuilder.loadTexts:dspuPuAdminTable.setStatus(_B)
_DspuPuAdminEntry_Object=MibTableRow
dspuPuAdminEntry=_DspuPuAdminEntry_Object((1,3,6,1,4,1,9,9,24,1,4,1,1))
dspuPuAdminEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:dspuPuAdminEntry.setStatus(_B)
class _DspuPuAdminIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DspuPuAdminIndex_Type.__name__=_C
_DspuPuAdminIndex_Object=MibTableColumn
dspuPuAdminIndex=_DspuPuAdminIndex_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,1),_DspuPuAdminIndex_Type())
dspuPuAdminIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuPuAdminIndex.setStatus(_B)
class _DspuPuAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DspuPuAdminName_Type.__name__=_I
_DspuPuAdminName_Object=MibTableColumn
dspuPuAdminName=_DspuPuAdminName_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,2),_DspuPuAdminName_Type())
dspuPuAdminName.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminName.setStatus(_B)
class _DspuPuAdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Ae,1),(_Af,2)))
_DspuPuAdminType_Type.__name__=_C
_DspuPuAdminType_Object=MibTableColumn
dspuPuAdminType=_DspuPuAdminType_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,3),_DspuPuAdminType_Type())
dspuPuAdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminType.setStatus(_B)
_DspuPuAdminRemoteMacAddress_Type=MacAddress
_DspuPuAdminRemoteMacAddress_Object=MibTableColumn
dspuPuAdminRemoteMacAddress=_DspuPuAdminRemoteMacAddress_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,4),_DspuPuAdminRemoteMacAddress_Type())
dspuPuAdminRemoteMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminRemoteMacAddress.setStatus(_B)
class _DspuPuAdminRemoteSapAddress_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuPuAdminRemoteSapAddress_Type.__name__=_C
_DspuPuAdminRemoteSapAddress_Object=MibTableColumn
dspuPuAdminRemoteSapAddress=_DspuPuAdminRemoteSapAddress_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,5),_DspuPuAdminRemoteSapAddress_Type())
dspuPuAdminRemoteSapAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminRemoteSapAddress.setStatus(_B)
class _DspuPuAdminLocalSapAddress_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuPuAdminLocalSapAddress_Type.__name__=_C
_DspuPuAdminLocalSapAddress_Object=MibTableColumn
dspuPuAdminLocalSapAddress=_DspuPuAdminLocalSapAddress_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,6),_DspuPuAdminLocalSapAddress_Type())
dspuPuAdminLocalSapAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminLocalSapAddress.setStatus(_B)
_DspuPuAdminXid_Type=Integer32
_DspuPuAdminXid_Object=MibTableColumn
dspuPuAdminXid=_DspuPuAdminXid_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,7),_DspuPuAdminXid_Type())
dspuPuAdminXid.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminXid.setStatus(_B)
class _DspuPuAdminXidFmt_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ag,1),('format0',2),('format3',3)))
_DspuPuAdminXidFmt_Type.__name__=_C
_DspuPuAdminXidFmt_Object=MibTableColumn
dspuPuAdminXidFmt=_DspuPuAdminXidFmt_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,8),_DspuPuAdminXidFmt_Type())
dspuPuAdminXidFmt.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminXidFmt.setStatus(_B)
class _DspuPuAdminWindowSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_DspuPuAdminWindowSize_Type.__name__=_C
_DspuPuAdminWindowSize_Object=MibTableColumn
dspuPuAdminWindowSize=_DspuPuAdminWindowSize_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,9),_DspuPuAdminWindowSize_Type())
dspuPuAdminWindowSize.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminWindowSize.setStatus(_B)
class _DspuPuAdminMaxIframe_Type(Integer32):defaultValue=1472;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,18432))
_DspuPuAdminMaxIframe_Type.__name__=_C
_DspuPuAdminMaxIframe_Object=MibTableColumn
dspuPuAdminMaxIframe=_DspuPuAdminMaxIframe_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,10),_DspuPuAdminMaxIframe_Type())
dspuPuAdminMaxIframe.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminMaxIframe.setStatus(_B)
class _DspuPuAdminLinkRetryCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPuAdminLinkRetryCount_Type.__name__=_C
_DspuPuAdminLinkRetryCount_Object=MibTableColumn
dspuPuAdminLinkRetryCount=_DspuPuAdminLinkRetryCount_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,11),_DspuPuAdminLinkRetryCount_Type())
dspuPuAdminLinkRetryCount.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminLinkRetryCount.setStatus(_B)
class _DspuPuAdminLinkRetryTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_DspuPuAdminLinkRetryTimeout_Type.__name__=_C
_DspuPuAdminLinkRetryTimeout_Object=MibTableColumn
dspuPuAdminLinkRetryTimeout=_DspuPuAdminLinkRetryTimeout_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,12),_DspuPuAdminLinkRetryTimeout_Type())
dspuPuAdminLinkRetryTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminLinkRetryTimeout.setStatus(_B)
class _DspuPuAdminStartPu_Type(TruthValue):defaultValue=2
_DspuPuAdminStartPu_Type.__name__=_J
_DspuPuAdminStartPu_Object=MibTableColumn
dspuPuAdminStartPu=_DspuPuAdminStartPu_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,13),_DspuPuAdminStartPu_Type())
dspuPuAdminStartPu.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminStartPu.setStatus(_B)
class _DspuPuAdminDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,8,9,10,11)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,5),(_V,6),(_W,8),(_X,9),(_Y,10),(_Z,11)))
_DspuPuAdminDlcType_Type.__name__=_C
_DspuPuAdminDlcType_Object=MibTableColumn
dspuPuAdminDlcType=_DspuPuAdminDlcType_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,14),_DspuPuAdminDlcType_Type())
dspuPuAdminDlcType.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminDlcType.setStatus(_B)
class _DspuPuAdminDlcUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPuAdminDlcUnit_Type.__name__=_C
_DspuPuAdminDlcUnit_Object=MibTableColumn
dspuPuAdminDlcUnit=_DspuPuAdminDlcUnit_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,15),_DspuPuAdminDlcUnit_Type())
dspuPuAdminDlcUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminDlcUnit.setStatus(_B)
class _DspuPuAdminDlcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPuAdminDlcPort_Type.__name__=_C
_DspuPuAdminDlcPort_Object=MibTableColumn
dspuPuAdminDlcPort=_DspuPuAdminDlcPort_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,16),_DspuPuAdminDlcPort_Type())
dspuPuAdminDlcPort.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminDlcPort.setStatus(_B)
class _DspuPuAdminFocalPoint_Type(TruthValue):defaultValue=2
_DspuPuAdminFocalPoint_Type.__name__=_J
_DspuPuAdminFocalPoint_Object=MibTableColumn
dspuPuAdminFocalPoint=_DspuPuAdminFocalPoint_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,17),_DspuPuAdminFocalPoint_Type())
dspuPuAdminFocalPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminFocalPoint.setStatus(_B)
_DspuPuAdminRowStatus_Type=RowStatus
_DspuPuAdminRowStatus_Object=MibTableColumn
dspuPuAdminRowStatus=_DspuPuAdminRowStatus_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,18),_DspuPuAdminRowStatus_Type())
dspuPuAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminRowStatus.setStatus(_B)
class _DspuPuAdminRemoteAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DspuPuAdminRemoteAddress_Type.__name__=_I
_DspuPuAdminRemoteAddress_Object=MibTableColumn
dspuPuAdminRemoteAddress=_DspuPuAdminRemoteAddress_Object((1,3,6,1,4,1,9,9,24,1,4,1,1,19),_DspuPuAdminRemoteAddress_Type())
dspuPuAdminRemoteAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuPuAdminRemoteAddress.setStatus(_B)
_DspuPuOperTable_Object=MibTable
dspuPuOperTable=_DspuPuOperTable_Object((1,3,6,1,4,1,9,9,24,1,4,2))
if mibBuilder.loadTexts:dspuPuOperTable.setStatus(_B)
_DspuPuOperEntry_Object=MibTableRow
dspuPuOperEntry=_DspuPuOperEntry_Object((1,3,6,1,4,1,9,9,24,1,4,2,1))
dspuPuOperEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:dspuPuOperEntry.setStatus(_B)
class _DspuPuOperIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DspuPuOperIndex_Type.__name__=_C
_DspuPuOperIndex_Object=MibTableColumn
dspuPuOperIndex=_DspuPuOperIndex_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,1),_DspuPuOperIndex_Type())
dspuPuOperIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuPuOperIndex.setStatus(_B)
class _DspuPuOperName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DspuPuOperName_Type.__name__=_I
_DspuPuOperName_Object=MibTableColumn
dspuPuOperName=_DspuPuOperName_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,2),_DspuPuOperName_Type())
dspuPuOperName.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperName.setStatus(_B)
class _DspuPuOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Ae,1),(_Af,2)))
_DspuPuOperType_Type.__name__=_C
_DspuPuOperType_Object=MibTableColumn
dspuPuOperType=_DspuPuOperType_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,3),_DspuPuOperType_Type())
dspuPuOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperType.setStatus(_B)
_DspuPuOperRemoteMacAddress_Type=MacAddress
_DspuPuOperRemoteMacAddress_Object=MibTableColumn
dspuPuOperRemoteMacAddress=_DspuPuOperRemoteMacAddress_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,4),_DspuPuOperRemoteMacAddress_Type())
dspuPuOperRemoteMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperRemoteMacAddress.setStatus(_B)
class _DspuPuOperRemoteSapAddress_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuPuOperRemoteSapAddress_Type.__name__=_C
_DspuPuOperRemoteSapAddress_Object=MibTableColumn
dspuPuOperRemoteSapAddress=_DspuPuOperRemoteSapAddress_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,5),_DspuPuOperRemoteSapAddress_Type())
dspuPuOperRemoteSapAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperRemoteSapAddress.setStatus(_B)
class _DspuPuOperLocalSapAddress_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuPuOperLocalSapAddress_Type.__name__=_C
_DspuPuOperLocalSapAddress_Object=MibTableColumn
dspuPuOperLocalSapAddress=_DspuPuOperLocalSapAddress_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,6),_DspuPuOperLocalSapAddress_Type())
dspuPuOperLocalSapAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperLocalSapAddress.setStatus(_B)
_DspuPuOperXid_Type=Integer32
_DspuPuOperXid_Object=MibTableColumn
dspuPuOperXid=_DspuPuOperXid_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,7),_DspuPuOperXid_Type())
dspuPuOperXid.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperXid.setStatus(_B)
class _DspuPuOperXidFmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ag,1),('format0',2),('format3',3)))
_DspuPuOperXidFmt_Type.__name__=_C
_DspuPuOperXidFmt_Object=MibTableColumn
dspuPuOperXidFmt=_DspuPuOperXidFmt_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,8),_DspuPuOperXidFmt_Type())
dspuPuOperXidFmt.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperXidFmt.setStatus(_B)
class _DspuPuOperWindowSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_DspuPuOperWindowSize_Type.__name__=_C
_DspuPuOperWindowSize_Object=MibTableColumn
dspuPuOperWindowSize=_DspuPuOperWindowSize_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,9),_DspuPuOperWindowSize_Type())
dspuPuOperWindowSize.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperWindowSize.setStatus(_B)
class _DspuPuOperMaxIframe_Type(Integer32):defaultValue=1472;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,18432))
_DspuPuOperMaxIframe_Type.__name__=_C
_DspuPuOperMaxIframe_Object=MibTableColumn
dspuPuOperMaxIframe=_DspuPuOperMaxIframe_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,10),_DspuPuOperMaxIframe_Type())
dspuPuOperMaxIframe.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperMaxIframe.setStatus(_B)
class _DspuPuOperLinkRetryCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPuOperLinkRetryCount_Type.__name__=_C
_DspuPuOperLinkRetryCount_Object=MibTableColumn
dspuPuOperLinkRetryCount=_DspuPuOperLinkRetryCount_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,11),_DspuPuOperLinkRetryCount_Type())
dspuPuOperLinkRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperLinkRetryCount.setStatus(_B)
class _DspuPuOperLinkRetryTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_DspuPuOperLinkRetryTimeout_Type.__name__=_C
_DspuPuOperLinkRetryTimeout_Object=MibTableColumn
dspuPuOperLinkRetryTimeout=_DspuPuOperLinkRetryTimeout_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,12),_DspuPuOperLinkRetryTimeout_Type())
dspuPuOperLinkRetryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperLinkRetryTimeout.setStatus(_B)
class _DspuPuOperStartPu_Type(TruthValue):defaultValue=2
_DspuPuOperStartPu_Type.__name__=_J
_DspuPuOperStartPu_Object=MibTableColumn
dspuPuOperStartPu=_DspuPuOperStartPu_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,13),_DspuPuOperStartPu_Type())
dspuPuOperStartPu.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperStartPu.setStatus(_B)
class _DspuPuOperDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,8,9,10,11)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,5),(_V,6),(_W,8),(_X,9),(_Y,10),(_Z,11)))
_DspuPuOperDlcType_Type.__name__=_C
_DspuPuOperDlcType_Object=MibTableColumn
dspuPuOperDlcType=_DspuPuOperDlcType_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,14),_DspuPuOperDlcType_Type())
dspuPuOperDlcType.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperDlcType.setStatus(_B)
class _DspuPuOperDlcUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPuOperDlcUnit_Type.__name__=_C
_DspuPuOperDlcUnit_Object=MibTableColumn
dspuPuOperDlcUnit=_DspuPuOperDlcUnit_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,15),_DspuPuOperDlcUnit_Type())
dspuPuOperDlcUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperDlcUnit.setStatus(_B)
class _DspuPuOperDlcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuPuOperDlcPort_Type.__name__=_C
_DspuPuOperDlcPort_Object=MibTableColumn
dspuPuOperDlcPort=_DspuPuOperDlcPort_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,16),_DspuPuOperDlcPort_Type())
dspuPuOperDlcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperDlcPort.setStatus(_B)
class _DspuPuOperFocalPoint_Type(TruthValue):defaultValue=2
_DspuPuOperFocalPoint_Type.__name__=_J
_DspuPuOperFocalPoint_Object=MibTableColumn
dspuPuOperFocalPoint=_DspuPuOperFocalPoint_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,17),_DspuPuOperFocalPoint_Type())
dspuPuOperFocalPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperFocalPoint.setStatus(_B)
class _DspuPuOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_DspuPuOperState_Type.__name__=_C
_DspuPuOperState_Object=MibTableColumn
dspuPuOperState=_DspuPuOperState_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,18),_DspuPuOperState_Type())
dspuPuOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperState.setStatus(_B)
class _DspuPuOperFsmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('linkReset',1),('linkPendConnOut',2),('linkPendConnIn',3),('linkPendXid',4),('linkXidNeg',5),('linkConnOut',6),('linkConnIn',7),('linkConnected',8),('puPendAct',9),('puActive',10),('puBusy',11),('puPendInact',12),('linkPendDisc',13),('linkPendClose',14)))
_DspuPuOperFsmState_Type.__name__=_C
_DspuPuOperFsmState_Object=MibTableColumn
dspuPuOperFsmState=_DspuPuOperFsmState_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,19),_DspuPuOperFsmState_Type())
dspuPuOperFsmState.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperFsmState.setStatus(_B)
_DspuPuOperStartTime_Type=TimeStamp
_DspuPuOperStartTime_Object=MibTableColumn
dspuPuOperStartTime=_DspuPuOperStartTime_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,20),_DspuPuOperStartTime_Type())
dspuPuOperStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperStartTime.setStatus(_B)
_DspuPuOperLastStateChgTime_Type=TimeStamp
_DspuPuOperLastStateChgTime_Object=MibTableColumn
dspuPuOperLastStateChgTime=_DspuPuOperLastStateChgTime_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,21),_DspuPuOperLastStateChgTime_Type())
dspuPuOperLastStateChgTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperLastStateChgTime.setStatus(_B)
class _DspuPuOperRemoteAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DspuPuOperRemoteAddress_Type.__name__=_I
_DspuPuOperRemoteAddress_Object=MibTableColumn
dspuPuOperRemoteAddress=_DspuPuOperRemoteAddress_Object((1,3,6,1,4,1,9,9,24,1,4,2,1,22),_DspuPuOperRemoteAddress_Type())
dspuPuOperRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuOperRemoteAddress.setStatus(_B)
_DspuPuStatsTable_Object=MibTable
dspuPuStatsTable=_DspuPuStatsTable_Object((1,3,6,1,4,1,9,9,24,1,4,3))
if mibBuilder.loadTexts:dspuPuStatsTable.setStatus(_B)
_DspuPuStatsEntry_Object=MibTableRow
dspuPuStatsEntry=_DspuPuStatsEntry_Object((1,3,6,1,4,1,9,9,24,1,4,3,1))
dspuPuStatsEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:dspuPuStatsEntry.setStatus(_B)
_DspuPuStatsSentBytes_Type=Counter32
_DspuPuStatsSentBytes_Object=MibTableColumn
dspuPuStatsSentBytes=_DspuPuStatsSentBytes_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,1),_DspuPuStatsSentBytes_Type())
dspuPuStatsSentBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsSentBytes.setStatus(_B)
_DspuPuStatsRcvdBytes_Type=Counter32
_DspuPuStatsRcvdBytes_Object=MibTableColumn
dspuPuStatsRcvdBytes=_DspuPuStatsRcvdBytes_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,2),_DspuPuStatsRcvdBytes_Type())
dspuPuStatsRcvdBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsRcvdBytes.setStatus(_B)
_DspuPuStatsSentFrames_Type=Counter32
_DspuPuStatsSentFrames_Object=MibTableColumn
dspuPuStatsSentFrames=_DspuPuStatsSentFrames_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,3),_DspuPuStatsSentFrames_Type())
dspuPuStatsSentFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsSentFrames.setStatus(_B)
_DspuPuStatsRcvdFrames_Type=Counter32
_DspuPuStatsRcvdFrames_Object=MibTableColumn
dspuPuStatsRcvdFrames=_DspuPuStatsRcvdFrames_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,4),_DspuPuStatsRcvdFrames_Type())
dspuPuStatsRcvdFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsRcvdFrames.setStatus(_B)
_DspuPuStatsSentNegativeRsps_Type=Counter32
_DspuPuStatsSentNegativeRsps_Object=MibTableColumn
dspuPuStatsSentNegativeRsps=_DspuPuStatsSentNegativeRsps_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,5),_DspuPuStatsSentNegativeRsps_Type())
dspuPuStatsSentNegativeRsps.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsSentNegativeRsps.setStatus(_B)
_DspuPuStatsRcvdNegativeRsps_Type=Counter32
_DspuPuStatsRcvdNegativeRsps_Object=MibTableColumn
dspuPuStatsRcvdNegativeRsps=_DspuPuStatsRcvdNegativeRsps_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,6),_DspuPuStatsRcvdNegativeRsps_Type())
dspuPuStatsRcvdNegativeRsps.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsRcvdNegativeRsps.setStatus(_B)
_DspuPuStatsActiveLus_Type=Counter32
_DspuPuStatsActiveLus_Object=MibTableColumn
dspuPuStatsActiveLus=_DspuPuStatsActiveLus_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,7),_DspuPuStatsActiveLus_Type())
dspuPuStatsActiveLus.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsActiveLus.setStatus(_B)
_DspuPuStatsInactiveLus_Type=Counter32
_DspuPuStatsInactiveLus_Object=MibTableColumn
dspuPuStatsInactiveLus=_DspuPuStatsInactiveLus_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,8),_DspuPuStatsInactiveLus_Type())
dspuPuStatsInactiveLus.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsInactiveLus.setStatus(_B)
_DspuPuStatsBindLus_Type=Counter32
_DspuPuStatsBindLus_Object=MibTableColumn
dspuPuStatsBindLus=_DspuPuStatsBindLus_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,9),_DspuPuStatsBindLus_Type())
dspuPuStatsBindLus.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsBindLus.setStatus(_B)
_DspuPuStatsActivationFailures_Type=Counter32
_DspuPuStatsActivationFailures_Object=MibTableColumn
dspuPuStatsActivationFailures=_DspuPuStatsActivationFailures_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,10),_DspuPuStatsActivationFailures_Type())
dspuPuStatsActivationFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsActivationFailures.setStatus(_B)
class _DspuPuStatsLastActivationFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noError',1),(_Ah,2),('internalError',3),('configurationError',4),('puNegativeResponse',5),('puAlreadyActive',6)))
_DspuPuStatsLastActivationFailureReason_Type.__name__=_C
_DspuPuStatsLastActivationFailureReason_Object=MibTableColumn
dspuPuStatsLastActivationFailureReason=_DspuPuStatsLastActivationFailureReason_Object((1,3,6,1,4,1,9,9,24,1,4,3,1,11),_DspuPuStatsLastActivationFailureReason_Type())
dspuPuStatsLastActivationFailureReason.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuPuStatsLastActivationFailureReason.setStatus(_B)
_DspuPuTraps_ObjectIdentity=ObjectIdentity
dspuPuTraps=_DspuPuTraps_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,4,4))
_DspuPuTrapsPrefix_ObjectIdentity=ObjectIdentity
dspuPuTrapsPrefix=_DspuPuTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,4,4,0))
_DspuLu_ObjectIdentity=ObjectIdentity
dspuLu=_DspuLu_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,5))
_DspuLuAdminTable_Object=MibTable
dspuLuAdminTable=_DspuLuAdminTable_Object((1,3,6,1,4,1,9,9,24,1,5,1))
if mibBuilder.loadTexts:dspuLuAdminTable.setStatus(_B)
_DspuLuAdminEntry_Object=MibTableRow
dspuLuAdminEntry=_DspuLuAdminEntry_Object((1,3,6,1,4,1,9,9,24,1,5,1,1))
dspuLuAdminEntry.setIndexNames((0,_A,_R),(0,_A,_Ai))
if mibBuilder.loadTexts:dspuLuAdminEntry.setStatus(_B)
class _DspuLuAdminLuLocalAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuLuAdminLuLocalAddress_Type.__name__=_C
_DspuLuAdminLuLocalAddress_Object=MibTableColumn
dspuLuAdminLuLocalAddress=_DspuLuAdminLuLocalAddress_Object((1,3,6,1,4,1,9,9,24,1,5,1,1,1),_DspuLuAdminLuLocalAddress_Type())
dspuLuAdminLuLocalAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuLuAdminLuLocalAddress.setStatus(_B)
class _DspuLuAdminType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pooled',1),(_Aj,2)))
_DspuLuAdminType_Type.__name__=_C
_DspuLuAdminType_Object=MibTableColumn
dspuLuAdminType=_DspuLuAdminType_Object((1,3,6,1,4,1,9,9,24,1,5,1,1,2),_DspuLuAdminType_Type())
dspuLuAdminType.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuLuAdminType.setStatus(_B)
class _DspuLuAdminPoolClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_DspuLuAdminPoolClassName_Type.__name__=_I
_DspuLuAdminPoolClassName_Object=MibTableColumn
dspuLuAdminPoolClassName=_DspuLuAdminPoolClassName_Object((1,3,6,1,4,1,9,9,24,1,5,1,1,3),_DspuLuAdminPoolClassName_Type())
dspuLuAdminPoolClassName.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuLuAdminPoolClassName.setStatus(_B)
_DspuLuAdminPeerPuIndex_Type=Integer32
_DspuLuAdminPeerPuIndex_Object=MibTableColumn
dspuLuAdminPeerPuIndex=_DspuLuAdminPeerPuIndex_Object((1,3,6,1,4,1,9,9,24,1,5,1,1,4),_DspuLuAdminPeerPuIndex_Type())
dspuLuAdminPeerPuIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuLuAdminPeerPuIndex.setStatus(_B)
class _DspuLuAdminPeerLuLocalAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuLuAdminPeerLuLocalAddress_Type.__name__=_C
_DspuLuAdminPeerLuLocalAddress_Object=MibTableColumn
dspuLuAdminPeerLuLocalAddress=_DspuLuAdminPeerLuLocalAddress_Object((1,3,6,1,4,1,9,9,24,1,5,1,1,5),_DspuLuAdminPeerLuLocalAddress_Type())
dspuLuAdminPeerLuLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuLuAdminPeerLuLocalAddress.setStatus(_B)
_DspuLuAdminRowStatus_Type=RowStatus
_DspuLuAdminRowStatus_Object=MibTableColumn
dspuLuAdminRowStatus=_DspuLuAdminRowStatus_Object((1,3,6,1,4,1,9,9,24,1,5,1,1,6),_DspuLuAdminRowStatus_Type())
dspuLuAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuLuAdminRowStatus.setStatus(_B)
_DspuLuOperTable_Object=MibTable
dspuLuOperTable=_DspuLuOperTable_Object((1,3,6,1,4,1,9,9,24,1,5,2))
if mibBuilder.loadTexts:dspuLuOperTable.setStatus(_B)
_DspuLuOperEntry_Object=MibTableRow
dspuLuOperEntry=_DspuLuOperEntry_Object((1,3,6,1,4,1,9,9,24,1,5,2,1))
dspuLuOperEntry.setIndexNames((0,_A,_N),(0,_A,_P))
if mibBuilder.loadTexts:dspuLuOperEntry.setStatus(_B)
class _DspuLuOperLuLocalAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuLuOperLuLocalAddress_Type.__name__=_C
_DspuLuOperLuLocalAddress_Object=MibTableColumn
dspuLuOperLuLocalAddress=_DspuLuOperLuLocalAddress_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,1),_DspuLuOperLuLocalAddress_Type())
dspuLuOperLuLocalAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuLuOperLuLocalAddress.setStatus(_B)
class _DspuLuOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pooled',1),(_Aj,2)))
_DspuLuOperType_Type.__name__=_C
_DspuLuOperType_Object=MibTableColumn
dspuLuOperType=_DspuLuOperType_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,2),_DspuLuOperType_Type())
dspuLuOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperType.setStatus(_B)
class _DspuLuOperPoolClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_DspuLuOperPoolClassName_Type.__name__=_I
_DspuLuOperPoolClassName_Object=MibTableColumn
dspuLuOperPoolClassName=_DspuLuOperPoolClassName_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,3),_DspuLuOperPoolClassName_Type())
dspuLuOperPoolClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperPoolClassName.setStatus(_B)
_DspuLuOperPeerPuIndex_Type=Integer32
_DspuLuOperPeerPuIndex_Object=MibTableColumn
dspuLuOperPeerPuIndex=_DspuLuOperPeerPuIndex_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,4),_DspuLuOperPeerPuIndex_Type())
dspuLuOperPeerPuIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperPeerPuIndex.setStatus(_B)
class _DspuLuOperPeerLuLocalAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_DspuLuOperPeerLuLocalAddress_Type.__name__=_C
_DspuLuOperPeerLuLocalAddress_Object=MibTableColumn
dspuLuOperPeerLuLocalAddress=_DspuLuOperPeerLuLocalAddress_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,5),_DspuLuOperPeerLuLocalAddress_Type())
dspuLuOperPeerLuLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperPeerLuLocalAddress.setStatus(_B)
class _DspuLuOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_DspuLuOperState_Type.__name__=_C
_DspuLuOperState_Object=MibTableColumn
dspuLuOperState=_DspuLuOperState_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,6),_DspuLuOperState_Type())
dspuLuOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperState.setStatus(_B)
class _DspuLuOperFsmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('reset',1),('dnLuStarted',2),('upLuActive',3),('dnLuPendAct',4),('dnLuActUnav',5),('upLuPendAvail',6),('bothAvail',7),('dnLuPendInact',8),('upLuPendInact',9),('luInactivityTimeout',10),('dnInactivityPendInact',11)))
_DspuLuOperFsmState_Type.__name__=_C
_DspuLuOperFsmState_Object=MibTableColumn
dspuLuOperFsmState=_DspuLuOperFsmState_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,7),_DspuLuOperFsmState_Type())
dspuLuOperFsmState.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperFsmState.setStatus(_B)
class _DspuLuOperSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bound',1),('unbound',2)))
_DspuLuOperSessionState_Type.__name__=_C
_DspuLuOperSessionState_Object=MibTableColumn
dspuLuOperSessionState=_DspuLuOperSessionState_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,8),_DspuLuOperSessionState_Type())
dspuLuOperSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperSessionState.setStatus(_B)
class _DspuLuOperLastActivationFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noError',1),(_Ah,2),('luNegativeResponse',3)))
_DspuLuOperLastActivationFailureReason_Type.__name__=_C
_DspuLuOperLastActivationFailureReason_Object=MibTableColumn
dspuLuOperLastActivationFailureReason=_DspuLuOperLastActivationFailureReason_Object((1,3,6,1,4,1,9,9,24,1,5,2,1,9),_DspuLuOperLastActivationFailureReason_Type())
dspuLuOperLastActivationFailureReason.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuLuOperLastActivationFailureReason.setStatus(_B)
_DspuLuTraps_ObjectIdentity=ObjectIdentity
dspuLuTraps=_DspuLuTraps_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,5,3))
_DspuLuTrapsPrefix_ObjectIdentity=ObjectIdentity
dspuLuTrapsPrefix=_DspuLuTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,5,3,0))
_DspuSap_ObjectIdentity=ObjectIdentity
dspuSap=_DspuSap_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,6))
_DspuSapTable_Object=MibTable
dspuSapTable=_DspuSapTable_Object((1,3,6,1,4,1,9,9,24,1,6,1))
if mibBuilder.loadTexts:dspuSapTable.setStatus(_B)
_DspuSapEntry_Object=MibTableRow
dspuSapEntry=_DspuSapEntry_Object((1,3,6,1,4,1,9,9,24,1,6,1,1))
dspuSapEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:dspuSapEntry.setStatus(_B)
class _DspuSapAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DspuSapAddress_Type.__name__=_C
_DspuSapAddress_Object=MibTableColumn
dspuSapAddress=_DspuSapAddress_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,1),_DspuSapAddress_Type())
dspuSapAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuSapAddress.setStatus(_B)
class _DspuSapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstreamSap',1),('dnstreamSap',2)))
_DspuSapType_Type.__name__=_C
_DspuSapType_Object=MibTableColumn
dspuSapType=_DspuSapType_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,2),_DspuSapType_Type())
dspuSapType.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuSapType.setStatus(_B)
class _DspuSapDlcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,8,9,10,11)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,5),(_V,6),(_W,8),(_X,9),(_Y,10),(_Z,11)))
_DspuSapDlcType_Type.__name__=_C
_DspuSapDlcType_Object=MibTableColumn
dspuSapDlcType=_DspuSapDlcType_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,3),_DspuSapDlcType_Type())
dspuSapDlcType.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuSapDlcType.setStatus(_B)
class _DspuSapDlcUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuSapDlcUnit_Type.__name__=_C
_DspuSapDlcUnit_Object=MibTableColumn
dspuSapDlcUnit=_DspuSapDlcUnit_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,4),_DspuSapDlcUnit_Type())
dspuSapDlcUnit.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuSapDlcUnit.setStatus(_B)
class _DspuSapDlcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspuSapDlcPort_Type.__name__=_C
_DspuSapDlcPort_Object=MibTableColumn
dspuSapDlcPort=_DspuSapDlcPort_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,5),_DspuSapDlcPort_Type())
dspuSapDlcPort.setMaxAccess(_H)
if mibBuilder.loadTexts:dspuSapDlcPort.setStatus(_B)
class _DspuSapOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sapClosed',1),('sapOpening',2),('sapOpened',3),('sapClosing',4)))
_DspuSapOperState_Type.__name__=_C
_DspuSapOperState_Object=MibTableColumn
dspuSapOperState=_DspuSapOperState_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,6),_DspuSapOperState_Type())
dspuSapOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:dspuSapOperState.setStatus(_B)
_DspuSapRowStatus_Type=RowStatus
_DspuSapRowStatus_Object=MibTableColumn
dspuSapRowStatus=_DspuSapRowStatus_Object((1,3,6,1,4,1,9,9,24,1,6,1,1,7),_DspuSapRowStatus_Type())
dspuSapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dspuSapRowStatus.setStatus(_B)
_DspuSapTraps_ObjectIdentity=ObjectIdentity
dspuSapTraps=_DspuSapTraps_ObjectIdentity((1,3,6,1,4,1,9,9,24,1,6,2))
_CiscoDspuMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDspuMIBConformance=_CiscoDspuMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,24,2))
_CiscoDspuMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDspuMIBCompliances=_CiscoDspuMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,24,2,1))
_CiscoDspuMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDspuMIBGroups=_CiscoDspuMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,24,2,2))
dspuNodeGroup=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,1))
dspuNodeGroup.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:dspuNodeGroup.setStatus(_B)
dspuPoolClassGroup=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,2))
dspuPoolClassGroup.setObjects(*((_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:dspuPoolClassGroup.setStatus(_B)
dspuPooledLuGroup=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,3))
dspuPooledLuGroup.setObjects(*((_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:dspuPooledLuGroup.setStatus(_B)
dspuPuGroup=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,4))
dspuPuGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_G),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_K),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_O)))
if mibBuilder.loadTexts:dspuPuGroup.setStatus(_L)
dspuLuGroup=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,5))
dspuLuGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_M),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:dspuLuGroup.setStatus(_L)
dspuSapGroup=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,6))
dspuSapGroup.setObjects(*((_A,_A_),(_A,_AY),(_A,_B0)))
if mibBuilder.loadTexts:dspuSapGroup.setStatus(_B)
dspuPuGroupV11R01=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,7))
dspuPuGroupV11R01.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_B1),(_A,_G),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_K),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_B2),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_O)))
if mibBuilder.loadTexts:dspuPuGroupV11R01.setStatus(_B)
dspuLuGroupV11R01=ObjectGroup((1,3,6,1,4,1,9,9,24,2,2,8))
dspuLuGroupV11R01.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_M),(_A,_AW),(_A,_AX),(_A,_AZ)))
if mibBuilder.loadTexts:dspuLuGroupV11R01.setStatus(_B)
newdspuPuStateChangeTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,4,4,0,1))
newdspuPuStateChangeTrap.setObjects(*((_A,_G),(_A,_K)))
if mibBuilder.loadTexts:newdspuPuStateChangeTrap.setStatus(_B)
newdspuPuActivationFailureTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,4,4,0,2))
newdspuPuActivationFailureTrap.setObjects(*((_A,_G),(_A,_K),(_A,_O)))
if mibBuilder.loadTexts:newdspuPuActivationFailureTrap.setStatus(_B)
dspuPuStateChangeTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,4,4,1))
dspuPuStateChangeTrap.setObjects(*((_A,_G),(_A,_K)))
if mibBuilder.loadTexts:dspuPuStateChangeTrap.setStatus(_L)
dspuPuActivationFailureTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,4,4,2))
dspuPuActivationFailureTrap.setObjects(*((_A,_G),(_A,_K),(_A,_O)))
if mibBuilder.loadTexts:dspuPuActivationFailureTrap.setStatus(_L)
newdspuLuStateChangeTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,5,3,0,1))
newdspuLuStateChangeTrap.setObjects(*((_A,_G),(_A,_M)))
if mibBuilder.loadTexts:newdspuLuStateChangeTrap.setStatus(_B)
dspuLuActivationFailureTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,5,3,0,2))
dspuLuActivationFailureTrap.setObjects(*((_A,_G),(_A,_M),(_A,_AZ)))
if mibBuilder.loadTexts:dspuLuActivationFailureTrap.setStatus(_B)
dspuLuStateChangeTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,5,3,1))
dspuLuStateChangeTrap.setObjects(*((_A,_G),(_A,_P),(_A,_M)))
if mibBuilder.loadTexts:dspuLuStateChangeTrap.setStatus(_L)
dspuSapStateChangeTrap=NotificationType((1,3,6,1,4,1,9,9,24,1,6,2,1))
dspuSapStateChangeTrap.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_AY)))
if mibBuilder.loadTexts:dspuSapStateChangeTrap.setStatus(_L)
ciscoDspuMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,24,2,1,1))
ciscoDspuMIBCompliance.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_B3),(_A,_B4),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoDspuMIBCompliance.setStatus(_L)
ciscoDspuMIBComplianceV11R01=ModuleCompliance((1,3,6,1,4,1,9,9,24,2,1,2))
ciscoDspuMIBComplianceV11R01.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_B5),(_A,_B6),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoDspuMIBComplianceV11R01.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDspuMIB':ciscoDspuMIB,'dspuObjects':dspuObjects,'dspuNode':dspuNode,_Ak:dspuNodeRsrb,_Al:dspuNodeRsrbLocalVirtualRing,_Am:dspuNodeRsrbBridgeNumber,_An:dspuNodeRsrbTargetVirtualRing,_Ao:dspuNodeRsrbVirtualMacAddress,_Ap:dspuNodeDefaultPu,_Aq:dspuNodeDefaultPuWindowSize,_Ar:dspuNodeDefaultPuMaxIframe,_As:dspuNodeActivationWindow,_At:dspuNodeLastConfigChgTime,'dspuPoolClass':dspuPoolClass,'dspuPoolClassTable':dspuPoolClassTable,'dspuPoolClassEntry':dspuPoolClassEntry,_Q:dspuPoolClassIndex,_Au:dspuPoolClassName,_Av:dspuPoolClassInactivityTimeout,_Aw:dspuPoolClassOperUpStreamLuDefs,_Ax:dspuPoolClassOperDnStreamLuDefs,'dspuPooledLu':dspuPooledLu,'dspuPooledLuTable':dspuPooledLuTable,'dspuPooledLuEntry':dspuPooledLuEntry,_Ay:dspuPooledLuPeerPuIndex,_Az:dspuPooledLuPeerLuLocalAddress,'dspuPu':dspuPu,'dspuPuAdminTable':dspuPuAdminTable,'dspuPuAdminEntry':dspuPuAdminEntry,_R:dspuPuAdminIndex,_e:dspuPuAdminName,_f:dspuPuAdminType,_g:dspuPuAdminRemoteMacAddress,_h:dspuPuAdminRemoteSapAddress,_i:dspuPuAdminLocalSapAddress,_j:dspuPuAdminXid,_k:dspuPuAdminXidFmt,_l:dspuPuAdminWindowSize,_m:dspuPuAdminMaxIframe,_n:dspuPuAdminLinkRetryCount,_o:dspuPuAdminLinkRetryTimeout,_p:dspuPuAdminStartPu,_q:dspuPuAdminDlcType,_r:dspuPuAdminDlcUnit,_s:dspuPuAdminDlcPort,_t:dspuPuAdminFocalPoint,_u:dspuPuAdminRowStatus,_B1:dspuPuAdminRemoteAddress,'dspuPuOperTable':dspuPuOperTable,'dspuPuOperEntry':dspuPuOperEntry,_N:dspuPuOperIndex,_G:dspuPuOperName,_v:dspuPuOperType,_w:dspuPuOperRemoteMacAddress,_x:dspuPuOperRemoteSapAddress,_y:dspuPuOperLocalSapAddress,_z:dspuPuOperXid,_A0:dspuPuOperXidFmt,_A1:dspuPuOperWindowSize,_A2:dspuPuOperMaxIframe,_A3:dspuPuOperLinkRetryCount,_A4:dspuPuOperLinkRetryTimeout,_A5:dspuPuOperStartPu,_A6:dspuPuOperDlcType,_A7:dspuPuOperDlcUnit,_A8:dspuPuOperDlcPort,_A9:dspuPuOperFocalPoint,_K:dspuPuOperState,_AA:dspuPuOperFsmState,_AB:dspuPuOperStartTime,_AC:dspuPuOperLastStateChgTime,_B2:dspuPuOperRemoteAddress,'dspuPuStatsTable':dspuPuStatsTable,'dspuPuStatsEntry':dspuPuStatsEntry,_AD:dspuPuStatsSentBytes,_AE:dspuPuStatsRcvdBytes,_AF:dspuPuStatsSentFrames,_AG:dspuPuStatsRcvdFrames,_AH:dspuPuStatsSentNegativeRsps,_AI:dspuPuStatsRcvdNegativeRsps,_AJ:dspuPuStatsActiveLus,_AK:dspuPuStatsInactiveLus,_AL:dspuPuStatsBindLus,_AM:dspuPuStatsActivationFailures,_O:dspuPuStatsLastActivationFailureReason,'dspuPuTraps':dspuPuTraps,'dspuPuTrapsPrefix':dspuPuTrapsPrefix,'newdspuPuStateChangeTrap':newdspuPuStateChangeTrap,'newdspuPuActivationFailureTrap':newdspuPuActivationFailureTrap,'dspuPuStateChangeTrap':dspuPuStateChangeTrap,'dspuPuActivationFailureTrap':dspuPuActivationFailureTrap,'dspuLu':dspuLu,'dspuLuAdminTable':dspuLuAdminTable,'dspuLuAdminEntry':dspuLuAdminEntry,_Ai:dspuLuAdminLuLocalAddress,_AN:dspuLuAdminType,_AO:dspuLuAdminPoolClassName,_AP:dspuLuAdminPeerPuIndex,_AQ:dspuLuAdminPeerLuLocalAddress,_AR:dspuLuAdminRowStatus,'dspuLuOperTable':dspuLuOperTable,'dspuLuOperEntry':dspuLuOperEntry,_P:dspuLuOperLuLocalAddress,_AS:dspuLuOperType,_AT:dspuLuOperPoolClassName,_AU:dspuLuOperPeerPuIndex,_AV:dspuLuOperPeerLuLocalAddress,_M:dspuLuOperState,_AW:dspuLuOperFsmState,_AX:dspuLuOperSessionState,_AZ:dspuLuOperLastActivationFailureReason,'dspuLuTraps':dspuLuTraps,'dspuLuTrapsPrefix':dspuLuTrapsPrefix,'newdspuLuStateChangeTrap':newdspuLuStateChangeTrap,'dspuLuActivationFailureTrap':dspuLuActivationFailureTrap,'dspuLuStateChangeTrap':dspuLuStateChangeTrap,'dspuSap':dspuSap,'dspuSapTable':dspuSapTable,'dspuSapEntry':dspuSapEntry,_d:dspuSapAddress,_A_:dspuSapType,_a:dspuSapDlcType,_b:dspuSapDlcUnit,_c:dspuSapDlcPort,_AY:dspuSapOperState,_B0:dspuSapRowStatus,'dspuSapTraps':dspuSapTraps,'dspuSapStateChangeTrap':dspuSapStateChangeTrap,'ciscoDspuMIBConformance':ciscoDspuMIBConformance,'ciscoDspuMIBCompliances':ciscoDspuMIBCompliances,'ciscoDspuMIBCompliance':ciscoDspuMIBCompliance,'ciscoDspuMIBComplianceV11R01':ciscoDspuMIBComplianceV11R01,'ciscoDspuMIBGroups':ciscoDspuMIBGroups,_Aa:dspuNodeGroup,_Ab:dspuPoolClassGroup,_Ac:dspuPooledLuGroup,_B3:dspuPuGroup,_B4:dspuLuGroup,_Ad:dspuSapGroup,_B5:dspuPuGroupV11R01,_B6:dspuLuGroupV11R01})