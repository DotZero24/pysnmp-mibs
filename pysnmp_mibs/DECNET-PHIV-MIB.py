_A5='phivAreaNum'
_A4='phivNonBroadcastIndex'
_A3='phivLineIndex'
_A2='phivAdjAddr'
_A1='phivAdjNodeCircuitIndex'
_A0='routing-layer-complete'
_z='routing-layer-verify'
_y='routing-layer-initialize'
_x='data-link-start'
_w='circuit-rejected'
_v='initializing'
_u='phivAdjCircuitIndex'
_t='phivCountersIndex'
_s='phivEthLinkIndex'
_r='inactive'
_q='active'
_p='phivControlCircuitIndex'
_o='phivDDCMPLineCountIndex'
_n='phivDDCMPCircuitIndex'
_m='ddcmp-dmc'
_l='ddcmp-tributary'
_k='ddcmp-control'
_j='ddcmp-point'
_i='running'
_h='failed'
_g='synchronizing'
_f='triggering'
_e='dumping'
_d='loading'
_c='cleared'
_b='service'
_a='phivLevel1RouteNodeAddr'
_Z='phivEndCountHostNodeID'
_Y='phivEndRemoteHostNodeID'
_X='restricted'
_W='ethernet'
_V='looping'
_U='reflecting'
_T='starting'
_S='reset'
_R='phivCircuitIndex'
_Q='nonrouting-IV'
_P='routing-IV'
_O='nonrouting-III'
_N='routing-III'
_M='on'
_L='OctetString'
_K='area'
_J='off'
_I='other'
_H='DisplayString'
_G='obsolete'
_F='DECNET-PHIV-MIB'
_E='read-write'
_D='PhivCounter'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
class PhivAddr(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class PhivCounter(Integer32):0
class InterfaceIndex(Integer32):0
_Phiv_ObjectIdentity=ObjectIdentity
phiv=_Phiv_ObjectIdentity((1,3,6,1,2,1,18))
_PhivSystem_ObjectIdentity=ObjectIdentity
phivSystem=_PhivSystem_ObjectIdentity((1,3,6,1,2,1,18,1))
class _PhivSystemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_J,2),('shut',3),(_X,4)))
_PhivSystemState_Type.__name__=_C
_PhivSystemState_Object=MibScalar
phivSystemState=_PhivSystemState_Object((1,3,6,1,2,1,18,1,1),_PhivSystemState_Type())
phivSystemState.setMaxAccess(_E)
if mibBuilder.loadTexts:phivSystemState.setStatus(_A)
class _PhivExecIdent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PhivExecIdent_Type.__name__=_H
_PhivExecIdent_Object=MibScalar
phivExecIdent=_PhivExecIdent_Object((1,3,6,1,2,1,18,1,2),_PhivExecIdent_Type())
phivExecIdent.setMaxAccess(_E)
if mibBuilder.loadTexts:phivExecIdent.setStatus(_A)
_PhivManagement_ObjectIdentity=ObjectIdentity
phivManagement=_PhivManagement_ObjectIdentity((1,3,6,1,2,1,18,2))
class _PhivMgmtMgmtVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PhivMgmtMgmtVers_Type.__name__=_H
_PhivMgmtMgmtVers_Object=MibScalar
phivMgmtMgmtVers=_PhivMgmtMgmtVers_Object((1,3,6,1,2,1,18,2,1),_PhivMgmtMgmtVers_Type())
phivMgmtMgmtVers.setMaxAccess(_B)
if mibBuilder.loadTexts:phivMgmtMgmtVers.setStatus(_A)
_Session_ObjectIdentity=ObjectIdentity
session=_Session_ObjectIdentity((1,3,6,1,2,1,18,3))
class _PhivSessionSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_PhivSessionSystemName_Type.__name__=_H
_PhivSessionSystemName_Object=MibScalar
phivSessionSystemName=_PhivSessionSystemName_Object((1,3,6,1,2,1,18,3,1),_PhivSessionSystemName_Type())
phivSessionSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:phivSessionSystemName.setStatus(_A)
class _PhivSessionInTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivSessionInTimer_Type.__name__=_C
_PhivSessionInTimer_Object=MibScalar
phivSessionInTimer=_PhivSessionInTimer_Object((1,3,6,1,2,1,18,3,2),_PhivSessionInTimer_Type())
phivSessionInTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivSessionInTimer.setStatus(_A)
class _PhivSessionOutTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivSessionOutTimer_Type.__name__=_C
_PhivSessionOutTimer_Object=MibScalar
phivSessionOutTimer=_PhivSessionOutTimer_Object((1,3,6,1,2,1,18,3,3),_PhivSessionOutTimer_Type())
phivSessionOutTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivSessionOutTimer.setStatus(_A)
_End_ObjectIdentity=ObjectIdentity
end=_End_ObjectIdentity((1,3,6,1,2,1,18,4))
_PhivEndRemoteTable_Object=MibTable
phivEndRemoteTable=_PhivEndRemoteTable_Object((1,3,6,1,2,1,18,4,1))
if mibBuilder.loadTexts:phivEndRemoteTable.setStatus(_A)
_PhivEndRemoteEntry_Object=MibTableRow
phivEndRemoteEntry=_PhivEndRemoteEntry_Object((1,3,6,1,2,1,18,4,1,1))
phivEndRemoteEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:phivEndRemoteEntry.setStatus(_A)
_PhivEndRemoteHostNodeID_Type=PhivAddr
_PhivEndRemoteHostNodeID_Object=MibTableColumn
phivEndRemoteHostNodeID=_PhivEndRemoteHostNodeID_Object((1,3,6,1,2,1,18,4,1,1,1),_PhivEndRemoteHostNodeID_Type())
phivEndRemoteHostNodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndRemoteHostNodeID.setStatus(_A)
class _PhivEndRemoteState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_J,2),('shut',3),(_X,4)))
_PhivEndRemoteState_Type.__name__=_C
_PhivEndRemoteState_Object=MibTableColumn
phivEndRemoteState=_PhivEndRemoteState_Object((1,3,6,1,2,1,18,4,1,1,2),_PhivEndRemoteState_Type())
phivEndRemoteState.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndRemoteState.setStatus(_A)
class _PhivEndCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivEndCircuitIndex_Type.__name__=_C
_PhivEndCircuitIndex_Object=MibTableColumn
phivEndCircuitIndex=_PhivEndCircuitIndex_Object((1,3,6,1,2,1,18,4,1,1,3),_PhivEndCircuitIndex_Type())
phivEndCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCircuitIndex.setStatus(_A)
class _PhivEndActiveLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndActiveLinks_Type.__name__=_C
_PhivEndActiveLinks_Object=MibTableColumn
phivEndActiveLinks=_PhivEndActiveLinks_Object((1,3,6,1,2,1,18,4,1,1,4),_PhivEndActiveLinks_Type())
phivEndActiveLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndActiveLinks.setStatus(_A)
class _PhivEndDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndDelay_Type.__name__=_C
_PhivEndDelay_Object=MibTableColumn
phivEndDelay=_PhivEndDelay_Object((1,3,6,1,2,1,18,4,1,1,5),_PhivEndDelay_Type())
phivEndDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndDelay.setStatus(_A)
_PhivEndCountTable_Object=MibTable
phivEndCountTable=_PhivEndCountTable_Object((1,3,6,1,2,1,18,4,2))
if mibBuilder.loadTexts:phivEndCountTable.setStatus(_A)
_PhivEndCountEntry_Object=MibTableRow
phivEndCountEntry=_PhivEndCountEntry_Object((1,3,6,1,2,1,18,4,2,1))
phivEndCountEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:phivEndCountEntry.setStatus(_A)
_PhivEndCountHostNodeID_Type=PhivAddr
_PhivEndCountHostNodeID_Object=MibTableColumn
phivEndCountHostNodeID=_PhivEndCountHostNodeID_Object((1,3,6,1,2,1,18,4,2,1,1),_PhivEndCountHostNodeID_Type())
phivEndCountHostNodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountHostNodeID.setStatus(_A)
class _PhivEndCountSecsLastZeroed_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndCountSecsLastZeroed_Type.__name__=_D
_PhivEndCountSecsLastZeroed_Object=MibTableColumn
phivEndCountSecsLastZeroed=_PhivEndCountSecsLastZeroed_Object((1,3,6,1,2,1,18,4,2,1,2),_PhivEndCountSecsLastZeroed_Type())
phivEndCountSecsLastZeroed.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountSecsLastZeroed.setStatus(_A)
class _PhivEndCountUsrBytesRec_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountUsrBytesRec_Type.__name__=_D
_PhivEndCountUsrBytesRec_Object=MibTableColumn
phivEndCountUsrBytesRec=_PhivEndCountUsrBytesRec_Object((1,3,6,1,2,1,18,4,2,1,3),_PhivEndCountUsrBytesRec_Type())
phivEndCountUsrBytesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountUsrBytesRec.setStatus(_A)
class _PhivEndCountUsrBytesSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountUsrBytesSent_Type.__name__=_D
_PhivEndCountUsrBytesSent_Object=MibTableColumn
phivEndCountUsrBytesSent=_PhivEndCountUsrBytesSent_Object((1,3,6,1,2,1,18,4,2,1,4),_PhivEndCountUsrBytesSent_Type())
phivEndCountUsrBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountUsrBytesSent.setStatus(_A)
class _PhivEndUCountUsrMessRec_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndUCountUsrMessRec_Type.__name__=_D
_PhivEndUCountUsrMessRec_Object=MibTableColumn
phivEndUCountUsrMessRec=_PhivEndUCountUsrMessRec_Object((1,3,6,1,2,1,18,4,2,1,5),_PhivEndUCountUsrMessRec_Type())
phivEndUCountUsrMessRec.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndUCountUsrMessRec.setStatus(_A)
class _PhivEndCountUsrMessSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountUsrMessSent_Type.__name__=_D
_PhivEndCountUsrMessSent_Object=MibTableColumn
phivEndCountUsrMessSent=_PhivEndCountUsrMessSent_Object((1,3,6,1,2,1,18,4,2,1,6),_PhivEndCountUsrMessSent_Type())
phivEndCountUsrMessSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountUsrMessSent.setStatus(_A)
class _PhivEndCountTotalBytesRec_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountTotalBytesRec_Type.__name__=_D
_PhivEndCountTotalBytesRec_Object=MibTableColumn
phivEndCountTotalBytesRec=_PhivEndCountTotalBytesRec_Object((1,3,6,1,2,1,18,4,2,1,7),_PhivEndCountTotalBytesRec_Type())
phivEndCountTotalBytesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountTotalBytesRec.setStatus(_A)
class _PhivEndCountTotalBytesSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountTotalBytesSent_Type.__name__=_D
_PhivEndCountTotalBytesSent_Object=MibTableColumn
phivEndCountTotalBytesSent=_PhivEndCountTotalBytesSent_Object((1,3,6,1,2,1,18,4,2,1,8),_PhivEndCountTotalBytesSent_Type())
phivEndCountTotalBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountTotalBytesSent.setStatus(_A)
class _PhivEndCountTotalMessRec_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountTotalMessRec_Type.__name__=_D
_PhivEndCountTotalMessRec_Object=MibTableColumn
phivEndCountTotalMessRec=_PhivEndCountTotalMessRec_Object((1,3,6,1,2,1,18,4,2,1,9),_PhivEndCountTotalMessRec_Type())
phivEndCountTotalMessRec.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountTotalMessRec.setStatus(_A)
class _PhivEndCountTotalMessSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivEndCountTotalMessSent_Type.__name__=_D
_PhivEndCountTotalMessSent_Object=MibTableColumn
phivEndCountTotalMessSent=_PhivEndCountTotalMessSent_Object((1,3,6,1,2,1,18,4,2,1,10),_PhivEndCountTotalMessSent_Type())
phivEndCountTotalMessSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountTotalMessSent.setStatus(_A)
class _PhivEndCountConnectsRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndCountConnectsRecd_Type.__name__=_D
_PhivEndCountConnectsRecd_Object=MibTableColumn
phivEndCountConnectsRecd=_PhivEndCountConnectsRecd_Object((1,3,6,1,2,1,18,4,2,1,11),_PhivEndCountConnectsRecd_Type())
phivEndCountConnectsRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountConnectsRecd.setStatus(_A)
class _PhivEndCountConnectsSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndCountConnectsSent_Type.__name__=_D
_PhivEndCountConnectsSent_Object=MibTableColumn
phivEndCountConnectsSent=_PhivEndCountConnectsSent_Object((1,3,6,1,2,1,18,4,2,1,12),_PhivEndCountConnectsSent_Type())
phivEndCountConnectsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountConnectsSent.setStatus(_A)
class _PhivEndCountReponseTimeouts_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndCountReponseTimeouts_Type.__name__=_D
_PhivEndCountReponseTimeouts_Object=MibTableColumn
phivEndCountReponseTimeouts=_PhivEndCountReponseTimeouts_Object((1,3,6,1,2,1,18,4,2,1,13),_PhivEndCountReponseTimeouts_Type())
phivEndCountReponseTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountReponseTimeouts.setStatus(_A)
class _PhivEndCountRecdConnectResErrs_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndCountRecdConnectResErrs_Type.__name__=_D
_PhivEndCountRecdConnectResErrs_Object=MibTableColumn
phivEndCountRecdConnectResErrs=_PhivEndCountRecdConnectResErrs_Object((1,3,6,1,2,1,18,4,2,1,14),_PhivEndCountRecdConnectResErrs_Type())
phivEndCountRecdConnectResErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndCountRecdConnectResErrs.setStatus(_A)
class _PhivEndMaxLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivEndMaxLinks_Type.__name__=_C
_PhivEndMaxLinks_Object=MibScalar
phivEndMaxLinks=_PhivEndMaxLinks_Object((1,3,6,1,2,1,18,4,3),_PhivEndMaxLinks_Type())
phivEndMaxLinks.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndMaxLinks.setStatus(_A)
class _PhivEndNSPVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PhivEndNSPVers_Type.__name__=_H
_PhivEndNSPVers_Object=MibScalar
phivEndNSPVers=_PhivEndNSPVers_Object((1,3,6,1,2,1,18,4,4),_PhivEndNSPVers_Type())
phivEndNSPVers.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEndNSPVers.setStatus(_A)
class _PhivEndRetransmitFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivEndRetransmitFactor_Type.__name__=_C
_PhivEndRetransmitFactor_Object=MibScalar
phivEndRetransmitFactor=_PhivEndRetransmitFactor_Object((1,3,6,1,2,1,18,4,5),_PhivEndRetransmitFactor_Type())
phivEndRetransmitFactor.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndRetransmitFactor.setStatus(_A)
class _PhivEndDelayFact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PhivEndDelayFact_Type.__name__=_C
_PhivEndDelayFact_Object=MibScalar
phivEndDelayFact=_PhivEndDelayFact_Object((1,3,6,1,2,1,18,4,6),_PhivEndDelayFact_Type())
phivEndDelayFact.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndDelayFact.setStatus(_A)
class _PhivEndDelayWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PhivEndDelayWeight_Type.__name__=_C
_PhivEndDelayWeight_Object=MibScalar
phivEndDelayWeight=_PhivEndDelayWeight_Object((1,3,6,1,2,1,18,4,7),_PhivEndDelayWeight_Type())
phivEndDelayWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndDelayWeight.setStatus(_A)
class _PhivEndInactivityTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivEndInactivityTimer_Type.__name__=_C
_PhivEndInactivityTimer_Object=MibScalar
phivEndInactivityTimer=_PhivEndInactivityTimer_Object((1,3,6,1,2,1,18,4,8),_PhivEndInactivityTimer_Type())
phivEndInactivityTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndInactivityTimer.setStatus(_A)
class _PhivEndCountZeroCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_S,2)))
_PhivEndCountZeroCount_Type.__name__=_C
_PhivEndCountZeroCount_Object=MibScalar
phivEndCountZeroCount=_PhivEndCountZeroCount_Object((1,3,6,1,2,1,18,4,9),_PhivEndCountZeroCount_Type())
phivEndCountZeroCount.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndCountZeroCount.setStatus(_A)
class _PhivEndMaxLinksActive_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivEndMaxLinksActive_Type.__name__=_D
_PhivEndMaxLinksActive_Object=MibScalar
phivEndMaxLinksActive=_PhivEndMaxLinksActive_Object((1,3,6,1,2,1,18,4,10),_PhivEndMaxLinksActive_Type())
phivEndMaxLinksActive.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEndMaxLinksActive.setStatus(_A)
_Routing_ObjectIdentity=ObjectIdentity
routing=_Routing_ObjectIdentity((1,3,6,1,2,1,18,5))
class _PhivRouteBroadcastRouteTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivRouteBroadcastRouteTimer_Type.__name__=_C
_PhivRouteBroadcastRouteTimer_Object=MibScalar
phivRouteBroadcastRouteTimer=_PhivRouteBroadcastRouteTimer_Object((1,3,6,1,2,1,18,5,1),_PhivRouteBroadcastRouteTimer_Type())
phivRouteBroadcastRouteTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteBroadcastRouteTimer.setStatus(_A)
class _PhivRouteBuffSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivRouteBuffSize_Type.__name__=_C
_PhivRouteBuffSize_Object=MibScalar
phivRouteBuffSize=_PhivRouteBuffSize_Object((1,3,6,1,2,1,18,5,2),_PhivRouteBuffSize_Type())
phivRouteBuffSize.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteBuffSize.setStatus(_A)
class _PhivRouteRoutingVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PhivRouteRoutingVers_Type.__name__=_H
_PhivRouteRoutingVers_Object=MibScalar
phivRouteRoutingVers=_PhivRouteRoutingVers_Object((1,3,6,1,2,1,18,5,3),_PhivRouteRoutingVers_Type())
phivRouteRoutingVers.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteRoutingVers.setStatus(_A)
class _PhivRouteMaxAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_PhivRouteMaxAddr_Type.__name__=_C
_PhivRouteMaxAddr_Object=MibScalar
phivRouteMaxAddr=_PhivRouteMaxAddr_Object((1,3,6,1,2,1,18,5,4),_PhivRouteMaxAddr_Type())
phivRouteMaxAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxAddr.setStatus(_A)
class _PhivRouteMaxBdcastNonRouters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivRouteMaxBdcastNonRouters_Type.__name__=_C
_PhivRouteMaxBdcastNonRouters_Object=MibScalar
phivRouteMaxBdcastNonRouters=_PhivRouteMaxBdcastNonRouters_Object((1,3,6,1,2,1,18,5,5),_PhivRouteMaxBdcastNonRouters_Type())
phivRouteMaxBdcastNonRouters.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxBdcastNonRouters.setStatus(_A)
class _PhivRouteMaxBdcastRouters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivRouteMaxBdcastRouters_Type.__name__=_C
_PhivRouteMaxBdcastRouters_Object=MibScalar
phivRouteMaxBdcastRouters=_PhivRouteMaxBdcastRouters_Object((1,3,6,1,2,1,18,5,6),_PhivRouteMaxBdcastRouters_Type())
phivRouteMaxBdcastRouters.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxBdcastRouters.setStatus(_A)
class _PhivRouteMaxBuffs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivRouteMaxBuffs_Type.__name__=_C
_PhivRouteMaxBuffs_Object=MibScalar
phivRouteMaxBuffs=_PhivRouteMaxBuffs_Object((1,3,6,1,2,1,18,5,7),_PhivRouteMaxBuffs_Type())
phivRouteMaxBuffs.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxBuffs.setStatus(_A)
class _PhivRouteMaxCircuits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivRouteMaxCircuits_Type.__name__=_C
_PhivRouteMaxCircuits_Object=MibScalar
phivRouteMaxCircuits=_PhivRouteMaxCircuits_Object((1,3,6,1,2,1,18,5,8),_PhivRouteMaxCircuits_Type())
phivRouteMaxCircuits.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxCircuits.setStatus(_A)
class _PhivRouteMaxCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1022))
_PhivRouteMaxCost_Type.__name__=_C
_PhivRouteMaxCost_Object=MibScalar
phivRouteMaxCost=_PhivRouteMaxCost_Object((1,3,6,1,2,1,18,5,9),_PhivRouteMaxCost_Type())
phivRouteMaxCost.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxCost.setStatus(_A)
class _PhivRouteMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PhivRouteMaxHops_Type.__name__=_C
_PhivRouteMaxHops_Object=MibScalar
phivRouteMaxHops=_PhivRouteMaxHops_Object((1,3,6,1,2,1,18,5,10),_PhivRouteMaxHops_Type())
phivRouteMaxHops.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxHops.setStatus(_A)
class _PhivRouteMaxVisits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_PhivRouteMaxVisits_Type.__name__=_C
_PhivRouteMaxVisits_Object=MibScalar
phivRouteMaxVisits=_PhivRouteMaxVisits_Object((1,3,6,1,2,1,18,5,11),_PhivRouteMaxVisits_Type())
phivRouteMaxVisits.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxVisits.setStatus(_A)
class _PhivRouteRoutingTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivRouteRoutingTimer_Type.__name__=_C
_PhivRouteRoutingTimer_Object=MibScalar
phivRouteRoutingTimer=_PhivRouteRoutingTimer_Object((1,3,6,1,2,1,18,5,12),_PhivRouteRoutingTimer_Type())
phivRouteRoutingTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteRoutingTimer.setStatus(_A)
class _PhivRouteSegBuffSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivRouteSegBuffSize_Type.__name__=_C
_PhivRouteSegBuffSize_Object=MibScalar
phivRouteSegBuffSize=_PhivRouteSegBuffSize_Object((1,3,6,1,2,1,18,5,13),_PhivRouteSegBuffSize_Type())
phivRouteSegBuffSize.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteSegBuffSize.setStatus(_A)
class _PhivRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_K,3),(_P,4),(_Q,5)))
_PhivRouteType_Type.__name__=_C
_PhivRouteType_Object=MibScalar
phivRouteType=_PhivRouteType_Object((1,3,6,1,2,1,18,5,14),_PhivRouteType_Type())
phivRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteType.setStatus(_G)
class _PhivRouteCountAgedPktLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivRouteCountAgedPktLoss_Type.__name__=_D
_PhivRouteCountAgedPktLoss_Object=MibScalar
phivRouteCountAgedPktLoss=_PhivRouteCountAgedPktLoss_Object((1,3,6,1,2,1,18,5,15),_PhivRouteCountAgedPktLoss_Type())
phivRouteCountAgedPktLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountAgedPktLoss.setStatus(_A)
class _PhivRouteCountNodeUnrPktLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivRouteCountNodeUnrPktLoss_Type.__name__=_D
_PhivRouteCountNodeUnrPktLoss_Object=MibScalar
phivRouteCountNodeUnrPktLoss=_PhivRouteCountNodeUnrPktLoss_Object((1,3,6,1,2,1,18,5,16),_PhivRouteCountNodeUnrPktLoss_Type())
phivRouteCountNodeUnrPktLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountNodeUnrPktLoss.setStatus(_A)
class _PhivRouteCountOutRngePktLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivRouteCountOutRngePktLoss_Type.__name__=_D
_PhivRouteCountOutRngePktLoss_Object=MibScalar
phivRouteCountOutRngePktLoss=_PhivRouteCountOutRngePktLoss_Object((1,3,6,1,2,1,18,5,17),_PhivRouteCountOutRngePktLoss_Type())
phivRouteCountOutRngePktLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountOutRngePktLoss.setStatus(_A)
class _PhivRouteCountOverSzePktLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivRouteCountOverSzePktLoss_Type.__name__=_D
_PhivRouteCountOverSzePktLoss_Object=MibScalar
phivRouteCountOverSzePktLoss=_PhivRouteCountOverSzePktLoss_Object((1,3,6,1,2,1,18,5,18),_PhivRouteCountOverSzePktLoss_Type())
phivRouteCountOverSzePktLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountOverSzePktLoss.setStatus(_A)
class _PhivRouteCountPacketFmtErr_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivRouteCountPacketFmtErr_Type.__name__=_D
_PhivRouteCountPacketFmtErr_Object=MibScalar
phivRouteCountPacketFmtErr=_PhivRouteCountPacketFmtErr_Object((1,3,6,1,2,1,18,5,19),_PhivRouteCountPacketFmtErr_Type())
phivRouteCountPacketFmtErr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountPacketFmtErr.setStatus(_A)
class _PhivRouteCountPtlRteUpdtLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivRouteCountPtlRteUpdtLoss_Type.__name__=_D
_PhivRouteCountPtlRteUpdtLoss_Object=MibScalar
phivRouteCountPtlRteUpdtLoss=_PhivRouteCountPtlRteUpdtLoss_Object((1,3,6,1,2,1,18,5,20),_PhivRouteCountPtlRteUpdtLoss_Type())
phivRouteCountPtlRteUpdtLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountPtlRteUpdtLoss.setStatus(_A)
class _PhivRouteCountVerifReject_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivRouteCountVerifReject_Type.__name__=_D
_PhivRouteCountVerifReject_Object=MibScalar
phivRouteCountVerifReject=_PhivRouteCountVerifReject_Object((1,3,6,1,2,1,18,5,21),_PhivRouteCountVerifReject_Type())
phivRouteCountVerifReject.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteCountVerifReject.setStatus(_A)
_PhivLevel1RouteTable_Object=MibTable
phivLevel1RouteTable=_PhivLevel1RouteTable_Object((1,3,6,1,2,1,18,5,22))
if mibBuilder.loadTexts:phivLevel1RouteTable.setStatus(_A)
_PhivLevel1RouteEntry_Object=MibTableRow
phivLevel1RouteEntry=_PhivLevel1RouteEntry_Object((1,3,6,1,2,1,18,5,22,1))
phivLevel1RouteEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:phivLevel1RouteEntry.setStatus(_A)
_PhivLevel1RouteNodeAddr_Type=PhivAddr
_PhivLevel1RouteNodeAddr_Object=MibTableColumn
phivLevel1RouteNodeAddr=_PhivLevel1RouteNodeAddr_Object((1,3,6,1,2,1,18,5,22,1,1),_PhivLevel1RouteNodeAddr_Type())
phivLevel1RouteNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLevel1RouteNodeAddr.setStatus(_A)
class _PhivLevel1RouteCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivLevel1RouteCircuitIndex_Type.__name__=_C
_PhivLevel1RouteCircuitIndex_Object=MibTableColumn
phivLevel1RouteCircuitIndex=_PhivLevel1RouteCircuitIndex_Object((1,3,6,1,2,1,18,5,22,1,2),_PhivLevel1RouteCircuitIndex_Type())
phivLevel1RouteCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLevel1RouteCircuitIndex.setStatus(_A)
class _PhivLevel1RouteCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivLevel1RouteCost_Type.__name__=_C
_PhivLevel1RouteCost_Object=MibTableColumn
phivLevel1RouteCost=_PhivLevel1RouteCost_Object((1,3,6,1,2,1,18,5,22,1,3),_PhivLevel1RouteCost_Type())
phivLevel1RouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLevel1RouteCost.setStatus(_A)
class _PhivLevel1RouteHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivLevel1RouteHops_Type.__name__=_C
_PhivLevel1RouteHops_Object=MibTableColumn
phivLevel1RouteHops=_PhivLevel1RouteHops_Object((1,3,6,1,2,1,18,5,22,1,4),_PhivLevel1RouteHops_Type())
phivLevel1RouteHops.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLevel1RouteHops.setStatus(_A)
_PhivLevel1RouteNextNode_Type=PhivAddr
_PhivLevel1RouteNextNode_Object=MibTableColumn
phivLevel1RouteNextNode=_PhivLevel1RouteNextNode_Object((1,3,6,1,2,1,18,5,22,1,5),_PhivLevel1RouteNextNode_Type())
phivLevel1RouteNextNode.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLevel1RouteNextNode.setStatus(_A)
class _PhivRouteCountZeroCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_S,2)))
_PhivRouteCountZeroCount_Type.__name__=_C
_PhivRouteCountZeroCount_Object=MibScalar
phivRouteCountZeroCount=_PhivRouteCountZeroCount_Object((1,3,6,1,2,1,18,5,23),_PhivRouteCountZeroCount_Type())
phivRouteCountZeroCount.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteCountZeroCount.setStatus(_A)
_PhivRouteSystemAddr_Type=PhivAddr
_PhivRouteSystemAddr_Object=MibScalar
phivRouteSystemAddr=_PhivRouteSystemAddr_Object((1,3,6,1,2,1,18,5,24),_PhivRouteSystemAddr_Type())
phivRouteSystemAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivRouteSystemAddr.setStatus(_G)
class _PhivRouteRoutingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_K,3),(_P,4),(_Q,5)))
_PhivRouteRoutingType_Type.__name__=_C
_PhivRouteRoutingType_Object=MibScalar
phivRouteRoutingType=_PhivRouteRoutingType_Object((1,3,6,1,2,1,18,5,25),_PhivRouteRoutingType_Type())
phivRouteRoutingType.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteRoutingType.setStatus(_A)
_PhivRouteSystemAddress_Type=PhivAddr
_PhivRouteSystemAddress_Object=MibScalar
phivRouteSystemAddress=_PhivRouteSystemAddress_Object((1,3,6,1,2,1,18,5,26),_PhivRouteSystemAddress_Type())
phivRouteSystemAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteSystemAddress.setStatus(_A)
_Circuit_ObjectIdentity=ObjectIdentity
circuit=_Circuit_ObjectIdentity((1,3,6,1,2,1,18,6))
_PhivCircuitParametersTable_Object=MibTable
phivCircuitParametersTable=_PhivCircuitParametersTable_Object((1,3,6,1,2,1,18,6,1))
if mibBuilder.loadTexts:phivCircuitParametersTable.setStatus(_A)
_PhivCircuitParametersEntry_Object=MibTableRow
phivCircuitParametersEntry=_PhivCircuitParametersEntry_Object((1,3,6,1,2,1,18,6,1,1))
phivCircuitParametersEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:phivCircuitParametersEntry.setStatus(_A)
class _PhivCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivCircuitIndex_Type.__name__=_C
_PhivCircuitIndex_Object=MibTableColumn
phivCircuitIndex=_PhivCircuitIndex_Object((1,3,6,1,2,1,18,6,1,1,1),_PhivCircuitIndex_Type())
phivCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitIndex.setStatus(_A)
_PhivCircuitLineIndex_Type=InterfaceIndex
_PhivCircuitLineIndex_Object=MibTableColumn
phivCircuitLineIndex=_PhivCircuitLineIndex_Object((1,3,6,1,2,1,18,6,1,1,2),_PhivCircuitLineIndex_Type())
phivCircuitLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitLineIndex.setStatus(_A)
class _PhivCircuitCommonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_J,2),(_b,3),(_c,4)))
_PhivCircuitCommonState_Type.__name__=_C
_PhivCircuitCommonState_Object=MibTableColumn
phivCircuitCommonState=_PhivCircuitCommonState_Object((1,3,6,1,2,1,18,6,1,1,3),_PhivCircuitCommonState_Type())
phivCircuitCommonState.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitCommonState.setStatus(_A)
class _PhivCircuitCommonSubState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_d,4),(_e,5),(_f,6),('autoservice',7),('autoloading',8),('autodumping',9),('autotriggering',10),(_g,11),(_h,12),(_i,13)))
_PhivCircuitCommonSubState_Type.__name__=_C
_PhivCircuitCommonSubState_Object=MibTableColumn
phivCircuitCommonSubState=_PhivCircuitCommonSubState_Object((1,3,6,1,2,1,18,6,1,1,4),_PhivCircuitCommonSubState_Type())
phivCircuitCommonSubState.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCommonSubState.setStatus(_A)
class _PhivCircuitCommonName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PhivCircuitCommonName_Type.__name__=_H
_PhivCircuitCommonName_Object=MibTableColumn
phivCircuitCommonName=_PhivCircuitCommonName_Object((1,3,6,1,2,1,18,6,1,1,5),_PhivCircuitCommonName_Type())
phivCircuitCommonName.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCommonName.setStatus(_A)
class _PhivCircuitExecRecallTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCircuitExecRecallTimer_Type.__name__=_C
_PhivCircuitExecRecallTimer_Object=MibTableColumn
phivCircuitExecRecallTimer=_PhivCircuitExecRecallTimer_Object((1,3,6,1,2,1,18,6,1,1,6),_PhivCircuitExecRecallTimer_Type())
phivCircuitExecRecallTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitExecRecallTimer.setStatus(_A)
class _PhivCircuitCommonType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,14,15)));namedValues=NamedValues(*((_j,1),(_k,2),(_l,3),('x25',4),(_m,5),(_W,6),('ci',7),('qp2-dte20',8),('bisync',9),(_I,14),('fddi',15)))
_PhivCircuitCommonType_Type.__name__=_C
_PhivCircuitCommonType_Object=MibTableColumn
phivCircuitCommonType=_PhivCircuitCommonType_Object((1,3,6,1,2,1,18,6,1,1,7),_PhivCircuitCommonType_Type())
phivCircuitCommonType.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCommonType.setStatus(_A)
class _PhivCircuitService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_PhivCircuitService_Type.__name__=_C
_PhivCircuitService_Object=MibTableColumn
phivCircuitService=_PhivCircuitService_Object((1,3,6,1,2,1,18,6,1,1,8),_PhivCircuitService_Type())
phivCircuitService.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitService.setStatus(_A)
class _PhivCircuitExecCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_PhivCircuitExecCost_Type.__name__=_C
_PhivCircuitExecCost_Object=MibTableColumn
phivCircuitExecCost=_PhivCircuitExecCost_Object((1,3,6,1,2,1,18,6,1,1,9),_PhivCircuitExecCost_Type())
phivCircuitExecCost.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitExecCost.setStatus(_A)
class _PhivCircuitExecHelloTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_PhivCircuitExecHelloTimer_Type.__name__=_C
_PhivCircuitExecHelloTimer_Object=MibTableColumn
phivCircuitExecHelloTimer=_PhivCircuitExecHelloTimer_Object((1,3,6,1,2,1,18,6,1,1,10),_PhivCircuitExecHelloTimer_Type())
phivCircuitExecHelloTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitExecHelloTimer.setStatus(_A)
_PhivCircuitCountTable_Object=MibTable
phivCircuitCountTable=_PhivCircuitCountTable_Object((1,3,6,1,2,1,18,6,2))
if mibBuilder.loadTexts:phivCircuitCountTable.setStatus(_A)
_PhivCircuitCountEntry_Object=MibTableRow
phivCircuitCountEntry=_PhivCircuitCountEntry_Object((1,3,6,1,2,1,18,6,2,1))
phivCircuitCountEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:phivCircuitCountEntry.setStatus(_A)
class _PhivCircuitCountSecLastZeroed_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCircuitCountSecLastZeroed_Type.__name__=_D
_PhivCircuitCountSecLastZeroed_Object=MibTableColumn
phivCircuitCountSecLastZeroed=_PhivCircuitCountSecLastZeroed_Object((1,3,6,1,2,1,18,6,2,1,1),_PhivCircuitCountSecLastZeroed_Type())
phivCircuitCountSecLastZeroed.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountSecLastZeroed.setStatus(_A)
class _PhivCircuitCountTermPacketsRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountTermPacketsRecd_Type.__name__=_D
_PhivCircuitCountTermPacketsRecd_Object=MibTableColumn
phivCircuitCountTermPacketsRecd=_PhivCircuitCountTermPacketsRecd_Object((1,3,6,1,2,1,18,6,2,1,2),_PhivCircuitCountTermPacketsRecd_Type())
phivCircuitCountTermPacketsRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountTermPacketsRecd.setStatus(_A)
class _PhivCircuitCountOriginPackSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountOriginPackSent_Type.__name__=_D
_PhivCircuitCountOriginPackSent_Object=MibTableColumn
phivCircuitCountOriginPackSent=_PhivCircuitCountOriginPackSent_Object((1,3,6,1,2,1,18,6,2,1,3),_PhivCircuitCountOriginPackSent_Type())
phivCircuitCountOriginPackSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountOriginPackSent.setStatus(_A)
class _PhivCircuitCountTermCongLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCircuitCountTermCongLoss_Type.__name__=_D
_PhivCircuitCountTermCongLoss_Object=MibTableColumn
phivCircuitCountTermCongLoss=_PhivCircuitCountTermCongLoss_Object((1,3,6,1,2,1,18,6,2,1,4),_PhivCircuitCountTermCongLoss_Type())
phivCircuitCountTermCongLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountTermCongLoss.setStatus(_A)
class _PhivCircuitCountCorruptLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivCircuitCountCorruptLoss_Type.__name__=_D
_PhivCircuitCountCorruptLoss_Object=MibTableColumn
phivCircuitCountCorruptLoss=_PhivCircuitCountCorruptLoss_Object((1,3,6,1,2,1,18,6,2,1,5),_PhivCircuitCountCorruptLoss_Type())
phivCircuitCountCorruptLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountCorruptLoss.setStatus(_A)
class _PhivCircuitCountTransitPksRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountTransitPksRecd_Type.__name__=_D
_PhivCircuitCountTransitPksRecd_Object=MibTableColumn
phivCircuitCountTransitPksRecd=_PhivCircuitCountTransitPksRecd_Object((1,3,6,1,2,1,18,6,2,1,6),_PhivCircuitCountTransitPksRecd_Type())
phivCircuitCountTransitPksRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountTransitPksRecd.setStatus(_A)
class _PhivCircuitCountTransitPkSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountTransitPkSent_Type.__name__=_D
_PhivCircuitCountTransitPkSent_Object=MibTableColumn
phivCircuitCountTransitPkSent=_PhivCircuitCountTransitPkSent_Object((1,3,6,1,2,1,18,6,2,1,7),_PhivCircuitCountTransitPkSent_Type())
phivCircuitCountTransitPkSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountTransitPkSent.setStatus(_A)
class _PhivCircuitCountTransitCongestLoss_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCircuitCountTransitCongestLoss_Type.__name__=_D
_PhivCircuitCountTransitCongestLoss_Object=MibTableColumn
phivCircuitCountTransitCongestLoss=_PhivCircuitCountTransitCongestLoss_Object((1,3,6,1,2,1,18,6,2,1,8),_PhivCircuitCountTransitCongestLoss_Type())
phivCircuitCountTransitCongestLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountTransitCongestLoss.setStatus(_A)
class _PhivCircuitCountCircuitDown_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivCircuitCountCircuitDown_Type.__name__=_D
_PhivCircuitCountCircuitDown_Object=MibTableColumn
phivCircuitCountCircuitDown=_PhivCircuitCountCircuitDown_Object((1,3,6,1,2,1,18,6,2,1,9),_PhivCircuitCountCircuitDown_Type())
phivCircuitCountCircuitDown.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountCircuitDown.setStatus(_A)
class _PhivCircuitCountInitFailure_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivCircuitCountInitFailure_Type.__name__=_D
_PhivCircuitCountInitFailure_Object=MibTableColumn
phivCircuitCountInitFailure=_PhivCircuitCountInitFailure_Object((1,3,6,1,2,1,18,6,2,1,10),_PhivCircuitCountInitFailure_Type())
phivCircuitCountInitFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountInitFailure.setStatus(_A)
class _PhivCircuitCountAdjDown_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountAdjDown_Type.__name__=_D
_PhivCircuitCountAdjDown_Object=MibTableColumn
phivCircuitCountAdjDown=_PhivCircuitCountAdjDown_Object((1,3,6,1,2,1,18,6,2,1,11),_PhivCircuitCountAdjDown_Type())
phivCircuitCountAdjDown.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountAdjDown.setStatus(_A)
class _PhivCircuitCountPeakAdj_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCircuitCountPeakAdj_Type.__name__=_D
_PhivCircuitCountPeakAdj_Object=MibTableColumn
phivCircuitCountPeakAdj=_PhivCircuitCountPeakAdj_Object((1,3,6,1,2,1,18,6,2,1,12),_PhivCircuitCountPeakAdj_Type())
phivCircuitCountPeakAdj.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountPeakAdj.setStatus(_A)
class _PhivCircuitCountBytesRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountBytesRecd_Type.__name__=_D
_PhivCircuitCountBytesRecd_Object=MibTableColumn
phivCircuitCountBytesRecd=_PhivCircuitCountBytesRecd_Object((1,3,6,1,2,1,18,6,2,1,13),_PhivCircuitCountBytesRecd_Type())
phivCircuitCountBytesRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountBytesRecd.setStatus(_A)
class _PhivCircuitCountBytesSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountBytesSent_Type.__name__=_D
_PhivCircuitCountBytesSent_Object=MibTableColumn
phivCircuitCountBytesSent=_PhivCircuitCountBytesSent_Object((1,3,6,1,2,1,18,6,2,1,14),_PhivCircuitCountBytesSent_Type())
phivCircuitCountBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountBytesSent.setStatus(_A)
class _PhivCircuitCountDataBlocksRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountDataBlocksRecd_Type.__name__=_D
_PhivCircuitCountDataBlocksRecd_Object=MibTableColumn
phivCircuitCountDataBlocksRecd=_PhivCircuitCountDataBlocksRecd_Object((1,3,6,1,2,1,18,6,2,1,15),_PhivCircuitCountDataBlocksRecd_Type())
phivCircuitCountDataBlocksRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountDataBlocksRecd.setStatus(_A)
class _PhivCircuitCountDataBlocksSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCircuitCountDataBlocksSent_Type.__name__=_D
_PhivCircuitCountDataBlocksSent_Object=MibTableColumn
phivCircuitCountDataBlocksSent=_PhivCircuitCountDataBlocksSent_Object((1,3,6,1,2,1,18,6,2,1,16),_PhivCircuitCountDataBlocksSent_Type())
phivCircuitCountDataBlocksSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountDataBlocksSent.setStatus(_A)
class _PhivCircuitCountUsrBuffUnav_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCircuitCountUsrBuffUnav_Type.__name__=_D
_PhivCircuitCountUsrBuffUnav_Object=MibTableColumn
phivCircuitCountUsrBuffUnav=_PhivCircuitCountUsrBuffUnav_Object((1,3,6,1,2,1,18,6,2,1,17),_PhivCircuitCountUsrBuffUnav_Type())
phivCircuitCountUsrBuffUnav.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCircuitCountUsrBuffUnav.setStatus(_A)
_PhivCircuitOrigQueueLimit_Type=Integer32
_PhivCircuitOrigQueueLimit_Object=MibScalar
phivCircuitOrigQueueLimit=_PhivCircuitOrigQueueLimit_Object((1,3,6,1,2,1,18,6,3),_PhivCircuitOrigQueueLimit_Type())
phivCircuitOrigQueueLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitOrigQueueLimit.setStatus(_A)
class _PhivCircuitCountZeroCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_S,2)))
_PhivCircuitCountZeroCount_Type.__name__=_C
_PhivCircuitCountZeroCount_Object=MibScalar
phivCircuitCountZeroCount=_PhivCircuitCountZeroCount_Object((1,3,6,1,2,1,18,6,4),_PhivCircuitCountZeroCount_Type())
phivCircuitCountZeroCount.setMaxAccess(_E)
if mibBuilder.loadTexts:phivCircuitCountZeroCount.setStatus(_A)
_Ddcmp_ObjectIdentity=ObjectIdentity
ddcmp=_Ddcmp_ObjectIdentity((1,3,6,1,2,1,18,7))
_PhivDDCMPCircuitParametersTable_Object=MibTable
phivDDCMPCircuitParametersTable=_PhivDDCMPCircuitParametersTable_Object((1,3,6,1,2,1,18,7,1))
if mibBuilder.loadTexts:phivDDCMPCircuitParametersTable.setStatus(_A)
_PhivDDCMPCircuitParametersEntry_Object=MibTableRow
phivDDCMPCircuitParametersEntry=_PhivDDCMPCircuitParametersEntry_Object((1,3,6,1,2,1,18,7,1,1))
phivDDCMPCircuitParametersEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:phivDDCMPCircuitParametersEntry.setStatus(_A)
class _PhivDDCMPCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivDDCMPCircuitIndex_Type.__name__=_C
_PhivDDCMPCircuitIndex_Object=MibTableColumn
phivDDCMPCircuitIndex=_PhivDDCMPCircuitIndex_Object((1,3,6,1,2,1,18,7,1,1,1),_PhivDDCMPCircuitIndex_Type())
phivDDCMPCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitIndex.setStatus(_A)
_PhivDDCMPCircuitAdjNodeAddr_Type=PhivAddr
_PhivDDCMPCircuitAdjNodeAddr_Object=MibTableColumn
phivDDCMPCircuitAdjNodeAddr=_PhivDDCMPCircuitAdjNodeAddr_Object((1,3,6,1,2,1,18,7,1,1,2),_PhivDDCMPCircuitAdjNodeAddr_Type())
phivDDCMPCircuitAdjNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitAdjNodeAddr.setStatus(_A)
class _PhivDDCMPCircuitTributary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitTributary_Type.__name__=_C
_PhivDDCMPCircuitTributary_Object=MibTableColumn
phivDDCMPCircuitTributary=_PhivDDCMPCircuitTributary_Object((1,3,6,1,2,1,18,7,1,1,3),_PhivDDCMPCircuitTributary_Type())
phivDDCMPCircuitTributary.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitTributary.setStatus(_A)
_PhivDDCMPCircuitCountTable_Object=MibTable
phivDDCMPCircuitCountTable=_PhivDDCMPCircuitCountTable_Object((1,3,6,1,2,1,18,7,2))
if mibBuilder.loadTexts:phivDDCMPCircuitCountTable.setStatus(_A)
_PhivDDCMPCircuitCountEntry_Object=MibTableRow
phivDDCMPCircuitCountEntry=_PhivDDCMPCircuitCountEntry_Object((1,3,6,1,2,1,18,7,2,1))
phivDDCMPCircuitCountEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:phivDDCMPCircuitCountEntry.setStatus(_A)
class _PhivDDCMPCircuitErrorsInbd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitErrorsInbd_Type.__name__=_D
_PhivDDCMPCircuitErrorsInbd_Object=MibTableColumn
phivDDCMPCircuitErrorsInbd=_PhivDDCMPCircuitErrorsInbd_Object((1,3,6,1,2,1,18,7,2,1,1),_PhivDDCMPCircuitErrorsInbd_Type())
phivDDCMPCircuitErrorsInbd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitErrorsInbd.setStatus(_A)
class _PhivDDCMPCircuitErrorsOutbd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitErrorsOutbd_Type.__name__=_D
_PhivDDCMPCircuitErrorsOutbd_Object=MibTableColumn
phivDDCMPCircuitErrorsOutbd=_PhivDDCMPCircuitErrorsOutbd_Object((1,3,6,1,2,1,18,7,2,1,2),_PhivDDCMPCircuitErrorsOutbd_Type())
phivDDCMPCircuitErrorsOutbd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitErrorsOutbd.setStatus(_A)
class _PhivDDCMPCircuitRmteReplyTimeouts_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitRmteReplyTimeouts_Type.__name__=_D
_PhivDDCMPCircuitRmteReplyTimeouts_Object=MibTableColumn
phivDDCMPCircuitRmteReplyTimeouts=_PhivDDCMPCircuitRmteReplyTimeouts_Object((1,3,6,1,2,1,18,7,2,1,3),_PhivDDCMPCircuitRmteReplyTimeouts_Type())
phivDDCMPCircuitRmteReplyTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitRmteReplyTimeouts.setStatus(_A)
class _PhivDDCMPCircuitLocalReplyTimeouts_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitLocalReplyTimeouts_Type.__name__=_D
_PhivDDCMPCircuitLocalReplyTimeouts_Object=MibTableColumn
phivDDCMPCircuitLocalReplyTimeouts=_PhivDDCMPCircuitLocalReplyTimeouts_Object((1,3,6,1,2,1,18,7,2,1,4),_PhivDDCMPCircuitLocalReplyTimeouts_Type())
phivDDCMPCircuitLocalReplyTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitLocalReplyTimeouts.setStatus(_A)
class _PhivDDCMPCircuitRmteBuffErrors_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitRmteBuffErrors_Type.__name__=_D
_PhivDDCMPCircuitRmteBuffErrors_Object=MibTableColumn
phivDDCMPCircuitRmteBuffErrors=_PhivDDCMPCircuitRmteBuffErrors_Object((1,3,6,1,2,1,18,7,2,1,5),_PhivDDCMPCircuitRmteBuffErrors_Type())
phivDDCMPCircuitRmteBuffErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitRmteBuffErrors.setStatus(_A)
class _PhivDDCMPCircuitLocalBuffErrors_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitLocalBuffErrors_Type.__name__=_D
_PhivDDCMPCircuitLocalBuffErrors_Object=MibTableColumn
phivDDCMPCircuitLocalBuffErrors=_PhivDDCMPCircuitLocalBuffErrors_Object((1,3,6,1,2,1,18,7,2,1,6),_PhivDDCMPCircuitLocalBuffErrors_Type())
phivDDCMPCircuitLocalBuffErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitLocalBuffErrors.setStatus(_A)
class _PhivDDCMPCircuitSelectIntervalsElap_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivDDCMPCircuitSelectIntervalsElap_Type.__name__=_D
_PhivDDCMPCircuitSelectIntervalsElap_Object=MibTableColumn
phivDDCMPCircuitSelectIntervalsElap=_PhivDDCMPCircuitSelectIntervalsElap_Object((1,3,6,1,2,1,18,7,2,1,7),_PhivDDCMPCircuitSelectIntervalsElap_Type())
phivDDCMPCircuitSelectIntervalsElap.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitSelectIntervalsElap.setStatus(_A)
class _PhivDDCMPCircuitSelectTimeouts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPCircuitSelectTimeouts_Type.__name__=_C
_PhivDDCMPCircuitSelectTimeouts_Object=MibTableColumn
phivDDCMPCircuitSelectTimeouts=_PhivDDCMPCircuitSelectTimeouts_Object((1,3,6,1,2,1,18,7,2,1,8),_PhivDDCMPCircuitSelectTimeouts_Type())
phivDDCMPCircuitSelectTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPCircuitSelectTimeouts.setStatus(_A)
_PhivDDCMPLineCountTable_Object=MibTable
phivDDCMPLineCountTable=_PhivDDCMPLineCountTable_Object((1,3,6,1,2,1,18,7,3))
if mibBuilder.loadTexts:phivDDCMPLineCountTable.setStatus(_A)
_PhivDDCMPLineCountEntry_Object=MibTableRow
phivDDCMPLineCountEntry=_PhivDDCMPLineCountEntry_Object((1,3,6,1,2,1,18,7,3,1))
phivDDCMPLineCountEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:phivDDCMPLineCountEntry.setStatus(_A)
_PhivDDCMPLineCountIndex_Type=InterfaceIndex
_PhivDDCMPLineCountIndex_Object=MibTableColumn
phivDDCMPLineCountIndex=_PhivDDCMPLineCountIndex_Object((1,3,6,1,2,1,18,7,3,1,1),_PhivDDCMPLineCountIndex_Type())
phivDDCMPLineCountIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPLineCountIndex.setStatus(_A)
class _PhivDDCMPLineCountDataErrsIn_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPLineCountDataErrsIn_Type.__name__=_D
_PhivDDCMPLineCountDataErrsIn_Object=MibTableColumn
phivDDCMPLineCountDataErrsIn=_PhivDDCMPLineCountDataErrsIn_Object((1,3,6,1,2,1,18,7,3,1,2),_PhivDDCMPLineCountDataErrsIn_Type())
phivDDCMPLineCountDataErrsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPLineCountDataErrsIn.setStatus(_A)
class _PhivDDCMPLineCountRmteStationErrs_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPLineCountRmteStationErrs_Type.__name__=_D
_PhivDDCMPLineCountRmteStationErrs_Object=MibTableColumn
phivDDCMPLineCountRmteStationErrs=_PhivDDCMPLineCountRmteStationErrs_Object((1,3,6,1,2,1,18,7,3,1,3),_PhivDDCMPLineCountRmteStationErrs_Type())
phivDDCMPLineCountRmteStationErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPLineCountRmteStationErrs.setStatus(_A)
class _PhivDDCMPLineCountLocalStationErrs_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivDDCMPLineCountLocalStationErrs_Type.__name__=_D
_PhivDDCMPLineCountLocalStationErrs_Object=MibTableColumn
phivDDCMPLineCountLocalStationErrs=_PhivDDCMPLineCountLocalStationErrs_Object((1,3,6,1,2,1,18,7,3,1,4),_PhivDDCMPLineCountLocalStationErrs_Type())
phivDDCMPLineCountLocalStationErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:phivDDCMPLineCountLocalStationErrs.setStatus(_A)
_Control_ObjectIdentity=ObjectIdentity
control=_Control_ObjectIdentity((1,3,6,1,2,1,18,8))
class _PhivControlSchedTimer_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,65535))
_PhivControlSchedTimer_Type.__name__=_C
_PhivControlSchedTimer_Object=MibScalar
phivControlSchedTimer=_PhivControlSchedTimer_Object((1,3,6,1,2,1,18,8,1),_PhivControlSchedTimer_Type())
phivControlSchedTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivControlSchedTimer.setStatus(_A)
class _PhivControlDeadTimer_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivControlDeadTimer_Type.__name__=_C
_PhivControlDeadTimer_Object=MibScalar
phivControlDeadTimer=_PhivControlDeadTimer_Object((1,3,6,1,2,1,18,8,2),_PhivControlDeadTimer_Type())
phivControlDeadTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivControlDeadTimer.setStatus(_A)
class _PhivControlDelayTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivControlDelayTimer_Type.__name__=_C
_PhivControlDelayTimer_Object=MibScalar
phivControlDelayTimer=_PhivControlDelayTimer_Object((1,3,6,1,2,1,18,8,3),_PhivControlDelayTimer_Type())
phivControlDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivControlDelayTimer.setStatus(_A)
class _PhivControlStreamTimer_Type(Integer32):defaultValue=6000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivControlStreamTimer_Type.__name__=_C
_PhivControlStreamTimer_Object=MibScalar
phivControlStreamTimer=_PhivControlStreamTimer_Object((1,3,6,1,2,1,18,8,4),_PhivControlStreamTimer_Type())
phivControlStreamTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivControlStreamTimer.setStatus(_A)
_PhivControlParametersTable_Object=MibTable
phivControlParametersTable=_PhivControlParametersTable_Object((1,3,6,1,2,1,18,8,5))
if mibBuilder.loadTexts:phivControlParametersTable.setStatus(_A)
_PhivControlParametersEntry_Object=MibTableRow
phivControlParametersEntry=_PhivControlParametersEntry_Object((1,3,6,1,2,1,18,8,5,1))
phivControlParametersEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:phivControlParametersEntry.setStatus(_A)
class _PhivControlCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivControlCircuitIndex_Type.__name__=_C
_PhivControlCircuitIndex_Object=MibTableColumn
phivControlCircuitIndex=_PhivControlCircuitIndex_Object((1,3,6,1,2,1,18,8,5,1,1),_PhivControlCircuitIndex_Type())
phivControlCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivControlCircuitIndex.setStatus(_A)
class _PhivControlBabbleTimer_Type(Integer32):defaultValue=6000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivControlBabbleTimer_Type.__name__=_C
_PhivControlBabbleTimer_Object=MibTableColumn
phivControlBabbleTimer=_PhivControlBabbleTimer_Object((1,3,6,1,2,1,18,8,5,1,2),_PhivControlBabbleTimer_Type())
phivControlBabbleTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlBabbleTimer.setStatus(_A)
class _PhivControlMaxBuffs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_PhivControlMaxBuffs_Type.__name__=_C
_PhivControlMaxBuffs_Object=MibTableColumn
phivControlMaxBuffs=_PhivControlMaxBuffs_Object((1,3,6,1,2,1,18,8,5,1,3),_PhivControlMaxBuffs_Type())
phivControlMaxBuffs.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlMaxBuffs.setStatus(_A)
class _PhivControlMaxTransmits_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PhivControlMaxTransmits_Type.__name__=_C
_PhivControlMaxTransmits_Object=MibTableColumn
phivControlMaxTransmits=_PhivControlMaxTransmits_Object((1,3,6,1,2,1,18,8,5,1,4),_PhivControlMaxTransmits_Type())
phivControlMaxTransmits.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlMaxTransmits.setStatus(_A)
class _PhivControlDyingBase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivControlDyingBase_Type.__name__=_C
_PhivControlDyingBase_Object=MibTableColumn
phivControlDyingBase=_PhivControlDyingBase_Object((1,3,6,1,2,1,18,8,5,1,5),_PhivControlDyingBase_Type())
phivControlDyingBase.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlDyingBase.setStatus(_A)
class _PhivControlDyingIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivControlDyingIncrement_Type.__name__=_C
_PhivControlDyingIncrement_Object=MibTableColumn
phivControlDyingIncrement=_PhivControlDyingIncrement_Object((1,3,6,1,2,1,18,8,5,1,6),_PhivControlDyingIncrement_Type())
phivControlDyingIncrement.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlDyingIncrement.setStatus(_A)
class _PhivControlDeadThreshold_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivControlDeadThreshold_Type.__name__=_C
_PhivControlDeadThreshold_Object=MibTableColumn
phivControlDeadThreshold=_PhivControlDeadThreshold_Object((1,3,6,1,2,1,18,8,5,1,7),_PhivControlDeadThreshold_Type())
phivControlDeadThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlDeadThreshold.setStatus(_A)
class _PhivControlDyingThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivControlDyingThreshold_Type.__name__=_C
_PhivControlDyingThreshold_Object=MibTableColumn
phivControlDyingThreshold=_PhivControlDyingThreshold_Object((1,3,6,1,2,1,18,8,5,1,8),_PhivControlDyingThreshold_Type())
phivControlDyingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlDyingThreshold.setStatus(_A)
class _PhivControlInactTreshold_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivControlInactTreshold_Type.__name__=_C
_PhivControlInactTreshold_Object=MibTableColumn
phivControlInactTreshold=_PhivControlInactTreshold_Object((1,3,6,1,2,1,18,8,5,1,9),_PhivControlInactTreshold_Type())
phivControlInactTreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlInactTreshold.setStatus(_A)
class _PhivControlPollingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('automatic',1),(_q,2),(_r,3),('dying',4),('dead',5)))
_PhivControlPollingState_Type.__name__=_C
_PhivControlPollingState_Object=MibTableColumn
phivControlPollingState=_PhivControlPollingState_Object((1,3,6,1,2,1,18,8,5,1,10),_PhivControlPollingState_Type())
phivControlPollingState.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlPollingState.setStatus(_A)
class _PhivControlPollingSubState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_q,1),(_r,2),('dying',3),('dead',4)))
_PhivControlPollingSubState_Type.__name__=_C
_PhivControlPollingSubState_Object=MibTableColumn
phivControlPollingSubState=_PhivControlPollingSubState_Object((1,3,6,1,2,1,18,8,5,1,11),_PhivControlPollingSubState_Type())
phivControlPollingSubState.setMaxAccess(_B)
if mibBuilder.loadTexts:phivControlPollingSubState.setStatus(_A)
class _PhivControlTransTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivControlTransTimer_Type.__name__=_C
_PhivControlTransTimer_Object=MibTableColumn
phivControlTransTimer=_PhivControlTransTimer_Object((1,3,6,1,2,1,18,8,5,1,12),_PhivControlTransTimer_Type())
phivControlTransTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:phivControlTransTimer.setStatus(_A)
_Ethernet_ObjectIdentity=ObjectIdentity
ethernet=_Ethernet_ObjectIdentity((1,3,6,1,2,1,18,9))
_PhivEthLinkParametersTable_Object=MibTable
phivEthLinkParametersTable=_PhivEthLinkParametersTable_Object((1,3,6,1,2,1,18,9,1))
if mibBuilder.loadTexts:phivEthLinkParametersTable.setStatus(_A)
_PhivEthLinkParametersEntry_Object=MibTableRow
phivEthLinkParametersEntry=_PhivEthLinkParametersEntry_Object((1,3,6,1,2,1,18,9,1,1))
phivEthLinkParametersEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:phivEthLinkParametersEntry.setStatus(_A)
class _PhivEthLinkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivEthLinkIndex_Type.__name__=_C
_PhivEthLinkIndex_Object=MibTableColumn
phivEthLinkIndex=_PhivEthLinkIndex_Object((1,3,6,1,2,1,18,9,1,1,1),_PhivEthLinkIndex_Type())
phivEthLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEthLinkIndex.setStatus(_A)
_PhivEthDesigRouterNodeAddr_Type=PhivAddr
_PhivEthDesigRouterNodeAddr_Object=MibTableColumn
phivEthDesigRouterNodeAddr=_PhivEthDesigRouterNodeAddr_Object((1,3,6,1,2,1,18,9,1,1,2),_PhivEthDesigRouterNodeAddr_Type())
phivEthDesigRouterNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEthDesigRouterNodeAddr.setStatus(_A)
class _PhivEthMaxRouters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivEthMaxRouters_Type.__name__=_C
_PhivEthMaxRouters_Object=MibTableColumn
phivEthMaxRouters=_PhivEthMaxRouters_Object((1,3,6,1,2,1,18,9,1,1,3),_PhivEthMaxRouters_Type())
phivEthMaxRouters.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEthMaxRouters.setStatus(_A)
class _PhivEthRouterPri_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PhivEthRouterPri_Type.__name__=_C
_PhivEthRouterPri_Object=MibTableColumn
phivEthRouterPri=_PhivEthRouterPri_Object((1,3,6,1,2,1,18,9,1,1,4),_PhivEthRouterPri_Type())
phivEthRouterPri.setMaxAccess(_E)
if mibBuilder.loadTexts:phivEthRouterPri.setStatus(_A)
class _PhivEthHardwareAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_PhivEthHardwareAddr_Type.__name__=_L
_PhivEthHardwareAddr_Object=MibTableColumn
phivEthHardwareAddr=_PhivEthHardwareAddr_Object((1,3,6,1,2,1,18,9,1,1,5),_PhivEthHardwareAddr_Type())
phivEthHardwareAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivEthHardwareAddr.setStatus(_A)
_Counters_ObjectIdentity=ObjectIdentity
counters=_Counters_ObjectIdentity((1,3,6,1,2,1,18,10))
_PhivCountersCountTable_Object=MibTable
phivCountersCountTable=_PhivCountersCountTable_Object((1,3,6,1,2,1,18,10,1))
if mibBuilder.loadTexts:phivCountersCountTable.setStatus(_A)
_PhivCountersCountEntry_Object=MibTableRow
phivCountersCountEntry=_PhivCountersCountEntry_Object((1,3,6,1,2,1,18,10,1,1))
phivCountersCountEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:phivCountersCountEntry.setStatus(_A)
_PhivCountersIndex_Type=InterfaceIndex
_PhivCountersIndex_Object=MibTableColumn
phivCountersIndex=_PhivCountersIndex_Object((1,3,6,1,2,1,18,10,1,1,1),_PhivCountersIndex_Type())
phivCountersIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersIndex.setStatus(_A)
class _PhivCountersCountBytesRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountBytesRecd_Type.__name__=_D
_PhivCountersCountBytesRecd_Object=MibTableColumn
phivCountersCountBytesRecd=_PhivCountersCountBytesRecd_Object((1,3,6,1,2,1,18,10,1,1,2),_PhivCountersCountBytesRecd_Type())
phivCountersCountBytesRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountBytesRecd.setStatus(_A)
class _PhivCountersCountBytesSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountBytesSent_Type.__name__=_D
_PhivCountersCountBytesSent_Object=MibTableColumn
phivCountersCountBytesSent=_PhivCountersCountBytesSent_Object((1,3,6,1,2,1,18,10,1,1,3),_PhivCountersCountBytesSent_Type())
phivCountersCountBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountBytesSent.setStatus(_A)
class _PhivCountersCountDataBlocksRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountDataBlocksRecd_Type.__name__=_D
_PhivCountersCountDataBlocksRecd_Object=MibTableColumn
phivCountersCountDataBlocksRecd=_PhivCountersCountDataBlocksRecd_Object((1,3,6,1,2,1,18,10,1,1,4),_PhivCountersCountDataBlocksRecd_Type())
phivCountersCountDataBlocksRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountDataBlocksRecd.setStatus(_G)
class _PhivCountersCountDataBlocksSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountDataBlocksSent_Type.__name__=_D
_PhivCountersCountDataBlocksSent_Object=MibTableColumn
phivCountersCountDataBlocksSent=_PhivCountersCountDataBlocksSent_Object((1,3,6,1,2,1,18,10,1,1,5),_PhivCountersCountDataBlocksSent_Type())
phivCountersCountDataBlocksSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountDataBlocksSent.setStatus(_G)
class _PhivCountersCountEthUsrBuffUnav_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountEthUsrBuffUnav_Type.__name__=_D
_PhivCountersCountEthUsrBuffUnav_Object=MibTableColumn
phivCountersCountEthUsrBuffUnav=_PhivCountersCountEthUsrBuffUnav_Object((1,3,6,1,2,1,18,10,1,1,6),_PhivCountersCountEthUsrBuffUnav_Type())
phivCountersCountEthUsrBuffUnav.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountEthUsrBuffUnav.setStatus(_A)
class _PhivCountersCountMcastBytesRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountMcastBytesRecd_Type.__name__=_D
_PhivCountersCountMcastBytesRecd_Object=MibTableColumn
phivCountersCountMcastBytesRecd=_PhivCountersCountMcastBytesRecd_Object((1,3,6,1,2,1,18,10,1,1,7),_PhivCountersCountMcastBytesRecd_Type())
phivCountersCountMcastBytesRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountMcastBytesRecd.setStatus(_A)
class _PhivCountersCountDataBlksRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountDataBlksRecd_Type.__name__=_D
_PhivCountersCountDataBlksRecd_Object=MibTableColumn
phivCountersCountDataBlksRecd=_PhivCountersCountDataBlksRecd_Object((1,3,6,1,2,1,18,10,1,1,8),_PhivCountersCountDataBlksRecd_Type())
phivCountersCountDataBlksRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountDataBlksRecd.setStatus(_A)
class _PhivCountersCountDataBlksSent_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountDataBlksSent_Type.__name__=_D
_PhivCountersCountDataBlksSent_Object=MibTableColumn
phivCountersCountDataBlksSent=_PhivCountersCountDataBlksSent_Object((1,3,6,1,2,1,18,10,1,1,9),_PhivCountersCountDataBlksSent_Type())
phivCountersCountDataBlksSent.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountDataBlksSent.setStatus(_A)
class _PhivCountersCountMcastBlksRecd_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountMcastBlksRecd_Type.__name__=_D
_PhivCountersCountMcastBlksRecd_Object=MibTableColumn
phivCountersCountMcastBlksRecd=_PhivCountersCountMcastBlksRecd_Object((1,3,6,1,2,1,18,10,1,1,10),_PhivCountersCountMcastBlksRecd_Type())
phivCountersCountMcastBlksRecd.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountMcastBlksRecd.setStatus(_A)
class _PhivCountersCountBlksSentDef_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountBlksSentDef_Type.__name__=_D
_PhivCountersCountBlksSentDef_Object=MibTableColumn
phivCountersCountBlksSentDef=_PhivCountersCountBlksSentDef_Object((1,3,6,1,2,1,18,10,1,1,11),_PhivCountersCountBlksSentDef_Type())
phivCountersCountBlksSentDef.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountBlksSentDef.setStatus(_A)
class _PhivCountersCountBlksSentSingleCol_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountBlksSentSingleCol_Type.__name__=_D
_PhivCountersCountBlksSentSingleCol_Object=MibTableColumn
phivCountersCountBlksSentSingleCol=_PhivCountersCountBlksSentSingleCol_Object((1,3,6,1,2,1,18,10,1,1,12),_PhivCountersCountBlksSentSingleCol_Type())
phivCountersCountBlksSentSingleCol.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountBlksSentSingleCol.setStatus(_A)
class _PhivCountersCountBlksSentMultCol_Type(PhivCounter):subtypeSpec=PhivCounter.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PhivCountersCountBlksSentMultCol_Type.__name__=_D
_PhivCountersCountBlksSentMultCol_Object=MibTableColumn
phivCountersCountBlksSentMultCol=_PhivCountersCountBlksSentMultCol_Object((1,3,6,1,2,1,18,10,1,1,13),_PhivCountersCountBlksSentMultCol_Type())
phivCountersCountBlksSentMultCol.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountBlksSentMultCol.setStatus(_A)
class _PhivCountersCountSendFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountSendFailure_Type.__name__=_C
_PhivCountersCountSendFailure_Object=MibTableColumn
phivCountersCountSendFailure=_PhivCountersCountSendFailure_Object((1,3,6,1,2,1,18,10,1,1,14),_PhivCountersCountSendFailure_Type())
phivCountersCountSendFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountSendFailure.setStatus(_A)
class _PhivCountersCountCollDetectFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountCollDetectFailure_Type.__name__=_C
_PhivCountersCountCollDetectFailure_Object=MibTableColumn
phivCountersCountCollDetectFailure=_PhivCountersCountCollDetectFailure_Object((1,3,6,1,2,1,18,10,1,1,15),_PhivCountersCountCollDetectFailure_Type())
phivCountersCountCollDetectFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountCollDetectFailure.setStatus(_A)
class _PhivCountersCountReceiveFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountReceiveFailure_Type.__name__=_C
_PhivCountersCountReceiveFailure_Object=MibTableColumn
phivCountersCountReceiveFailure=_PhivCountersCountReceiveFailure_Object((1,3,6,1,2,1,18,10,1,1,16),_PhivCountersCountReceiveFailure_Type())
phivCountersCountReceiveFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountReceiveFailure.setStatus(_A)
class _PhivCountersCountUnrecFrameDest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountUnrecFrameDest_Type.__name__=_C
_PhivCountersCountUnrecFrameDest_Object=MibTableColumn
phivCountersCountUnrecFrameDest=_PhivCountersCountUnrecFrameDest_Object((1,3,6,1,2,1,18,10,1,1,17),_PhivCountersCountUnrecFrameDest_Type())
phivCountersCountUnrecFrameDest.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountUnrecFrameDest.setStatus(_A)
class _PhivCountersCountDataOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountDataOver_Type.__name__=_C
_PhivCountersCountDataOver_Object=MibTableColumn
phivCountersCountDataOver=_PhivCountersCountDataOver_Object((1,3,6,1,2,1,18,10,1,1,18),_PhivCountersCountDataOver_Type())
phivCountersCountDataOver.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountDataOver.setStatus(_A)
class _PhivCountersCountSysBuffUnav_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountSysBuffUnav_Type.__name__=_C
_PhivCountersCountSysBuffUnav_Object=MibTableColumn
phivCountersCountSysBuffUnav=_PhivCountersCountSysBuffUnav_Object((1,3,6,1,2,1,18,10,1,1,19),_PhivCountersCountSysBuffUnav_Type())
phivCountersCountSysBuffUnav.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountSysBuffUnav.setStatus(_A)
class _PhivCountersCountUsrBuffUnav_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivCountersCountUsrBuffUnav_Type.__name__=_C
_PhivCountersCountUsrBuffUnav_Object=MibTableColumn
phivCountersCountUsrBuffUnav=_PhivCountersCountUsrBuffUnav_Object((1,3,6,1,2,1,18,10,1,1,20),_PhivCountersCountUsrBuffUnav_Type())
phivCountersCountUsrBuffUnav.setMaxAccess(_B)
if mibBuilder.loadTexts:phivCountersCountUsrBuffUnav.setStatus(_A)
_Adjacency_ObjectIdentity=ObjectIdentity
adjacency=_Adjacency_ObjectIdentity((1,3,6,1,2,1,18,11))
_PhivAdjTable_Object=MibTable
phivAdjTable=_PhivAdjTable_Object((1,3,6,1,2,1,18,11,1))
if mibBuilder.loadTexts:phivAdjTable.setStatus(_G)
_PhivAdjEntry_Object=MibTableRow
phivAdjEntry=_PhivAdjEntry_Object((1,3,6,1,2,1,18,11,1,1))
phivAdjEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:phivAdjEntry.setStatus(_G)
_PhivAdjCircuitIndex_Type=Integer32
_PhivAdjCircuitIndex_Object=MibTableColumn
phivAdjCircuitIndex=_PhivAdjCircuitIndex_Object((1,3,6,1,2,1,18,11,1,1,1),_PhivAdjCircuitIndex_Type())
phivAdjCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjCircuitIndex.setStatus(_G)
_PhivAdjNodeAddr_Type=PhivAddr
_PhivAdjNodeAddr_Object=MibTableColumn
phivAdjNodeAddr=_PhivAdjNodeAddr_Object((1,3,6,1,2,1,18,11,1,1,2),_PhivAdjNodeAddr_Type())
phivAdjNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeAddr.setStatus(_G)
_PhivAdjBlockSize_Type=Integer32
_PhivAdjBlockSize_Object=MibTableColumn
phivAdjBlockSize=_PhivAdjBlockSize_Object((1,3,6,1,2,1,18,11,1,1,3),_PhivAdjBlockSize_Type())
phivAdjBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjBlockSize.setStatus(_G)
class _PhivAdjListenTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivAdjListenTimer_Type.__name__=_C
_PhivAdjListenTimer_Object=MibTableColumn
phivAdjListenTimer=_PhivAdjListenTimer_Object((1,3,6,1,2,1,18,11,1,1,4),_PhivAdjListenTimer_Type())
phivAdjListenTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjListenTimer.setStatus(_G)
class _PhivAdjCircuitEtherServPhysAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_PhivAdjCircuitEtherServPhysAddr_Type.__name__=_L
_PhivAdjCircuitEtherServPhysAddr_Object=MibTableColumn
phivAdjCircuitEtherServPhysAddr=_PhivAdjCircuitEtherServPhysAddr_Object((1,3,6,1,2,1,18,11,1,1,5),_PhivAdjCircuitEtherServPhysAddr_Type())
phivAdjCircuitEtherServPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjCircuitEtherServPhysAddr.setStatus(_G)
class _PhivAdjType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_K,3),(_P,4),(_Q,5)))
_PhivAdjType_Type.__name__=_C
_PhivAdjType_Object=MibTableColumn
phivAdjType=_PhivAdjType_Object((1,3,6,1,2,1,18,11,1,1,6),_PhivAdjType_Type())
phivAdjType.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjType.setStatus(_G)
class _PhivAdjState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_v,1),('up',2),('run',3),(_w,4),(_x,5),(_y,6),(_z,7),(_A0,8),(_J,9),('halt',10)))
_PhivAdjState_Type.__name__=_C
_PhivAdjState_Object=MibTableColumn
phivAdjState=_PhivAdjState_Object((1,3,6,1,2,1,18,11,1,1,7),_PhivAdjState_Type())
phivAdjState.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjState.setStatus(_G)
class _PhivAdjPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivAdjPriority_Type.__name__=_C
_PhivAdjPriority_Object=MibTableColumn
phivAdjPriority=_PhivAdjPriority_Object((1,3,6,1,2,1,18,11,1,1,8),_PhivAdjPriority_Type())
phivAdjPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjPriority.setStatus(_G)
class _PhivAdjExecListenTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivAdjExecListenTimer_Type.__name__=_C
_PhivAdjExecListenTimer_Object=MibTableColumn
phivAdjExecListenTimer=_PhivAdjExecListenTimer_Object((1,3,6,1,2,1,18,11,1,1,9),_PhivAdjExecListenTimer_Type())
phivAdjExecListenTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjExecListenTimer.setStatus(_G)
_PhivAdjNodeTable_Object=MibTable
phivAdjNodeTable=_PhivAdjNodeTable_Object((1,3,6,1,2,1,18,11,2))
if mibBuilder.loadTexts:phivAdjNodeTable.setStatus(_A)
_PhivAdjNodeEntry_Object=MibTableRow
phivAdjNodeEntry=_PhivAdjNodeEntry_Object((1,3,6,1,2,1,18,11,2,1))
phivAdjNodeEntry.setIndexNames((0,_F,_A1),(0,_F,_A2))
if mibBuilder.loadTexts:phivAdjNodeEntry.setStatus(_A)
class _PhivAdjNodeCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivAdjNodeCircuitIndex_Type.__name__=_C
_PhivAdjNodeCircuitIndex_Object=MibTableColumn
phivAdjNodeCircuitIndex=_PhivAdjNodeCircuitIndex_Object((1,3,6,1,2,1,18,11,2,1,1),_PhivAdjNodeCircuitIndex_Type())
phivAdjNodeCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeCircuitIndex.setStatus(_A)
_PhivAdjAddr_Type=PhivAddr
_PhivAdjAddr_Object=MibTableColumn
phivAdjAddr=_PhivAdjAddr_Object((1,3,6,1,2,1,18,11,2,1,2),_PhivAdjAddr_Type())
phivAdjAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjAddr.setStatus(_A)
_PhivAdjNodeBlockSize_Type=Integer32
_PhivAdjNodeBlockSize_Object=MibTableColumn
phivAdjNodeBlockSize=_PhivAdjNodeBlockSize_Object((1,3,6,1,2,1,18,11,2,1,3),_PhivAdjNodeBlockSize_Type())
phivAdjNodeBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeBlockSize.setStatus(_A)
class _PhivAdjNodeListenTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivAdjNodeListenTimer_Type.__name__=_C
_PhivAdjNodeListenTimer_Object=MibTableColumn
phivAdjNodeListenTimer=_PhivAdjNodeListenTimer_Object((1,3,6,1,2,1,18,11,2,1,4),_PhivAdjNodeListenTimer_Type())
phivAdjNodeListenTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeListenTimer.setStatus(_A)
class _PhivAdjNodeCircuitEtherServPhysAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_PhivAdjNodeCircuitEtherServPhysAddr_Type.__name__=_L
_PhivAdjNodeCircuitEtherServPhysAddr_Object=MibTableColumn
phivAdjNodeCircuitEtherServPhysAddr=_PhivAdjNodeCircuitEtherServPhysAddr_Object((1,3,6,1,2,1,18,11,2,1,5),_PhivAdjNodeCircuitEtherServPhysAddr_Type())
phivAdjNodeCircuitEtherServPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeCircuitEtherServPhysAddr.setStatus(_A)
class _PhivAdjNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_K,3),(_P,4),(_Q,5)))
_PhivAdjNodeType_Type.__name__=_C
_PhivAdjNodeType_Object=MibTableColumn
phivAdjNodeType=_PhivAdjNodeType_Object((1,3,6,1,2,1,18,11,2,1,6),_PhivAdjNodeType_Type())
phivAdjNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeType.setStatus(_A)
class _PhivAdjNodeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_v,1),('up',2),('run',3),(_w,4),(_x,5),(_y,6),(_z,7),(_A0,8),(_J,9),('halt',10)))
_PhivAdjNodeState_Type.__name__=_C
_PhivAdjNodeState_Object=MibTableColumn
phivAdjNodeState=_PhivAdjNodeState_Object((1,3,6,1,2,1,18,11,2,1,7),_PhivAdjNodeState_Type())
phivAdjNodeState.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodeState.setStatus(_A)
class _PhivAdjNodePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivAdjNodePriority_Type.__name__=_C
_PhivAdjNodePriority_Object=MibTableColumn
phivAdjNodePriority=_PhivAdjNodePriority_Object((1,3,6,1,2,1,18,11,2,1,8),_PhivAdjNodePriority_Type())
phivAdjNodePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAdjNodePriority.setStatus(_A)
_Line_ObjectIdentity=ObjectIdentity
line=_Line_ObjectIdentity((1,3,6,1,2,1,18,12))
_PhivLineTable_Object=MibTable
phivLineTable=_PhivLineTable_Object((1,3,6,1,2,1,18,12,1))
if mibBuilder.loadTexts:phivLineTable.setStatus(_A)
_PhivLineEntry_Object=MibTableRow
phivLineEntry=_PhivLineEntry_Object((1,3,6,1,2,1,18,12,1,1))
phivLineEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:phivLineEntry.setStatus(_A)
_PhivLineIndex_Type=InterfaceIndex
_PhivLineIndex_Object=MibTableColumn
phivLineIndex=_PhivLineIndex_Object((1,3,6,1,2,1,18,12,1,1,1),_PhivLineIndex_Type())
phivLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineIndex.setStatus(_A)
class _PhivLineName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PhivLineName_Type.__name__=_H
_PhivLineName_Object=MibTableColumn
phivLineName=_PhivLineName_Object((1,3,6,1,2,1,18,12,1,1,2),_PhivLineName_Type())
phivLineName.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineName.setStatus(_A)
class _PhivLineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_J,2),(_b,3),(_c,4)))
_PhivLineState_Type.__name__=_C
_PhivLineState_Object=MibTableColumn
phivLineState=_PhivLineState_Object((1,3,6,1,2,1,18,12,1,1,3),_PhivLineState_Type())
phivLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineState.setStatus(_A)
class _PhivLineSubstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_d,4),(_e,5),(_f,6),('auto-service',7),('auto-loading',8),('auto-dumping',9),('auto-triggering',10),(_g,11),(_h,12),(_i,13)))
_PhivLineSubstate_Type.__name__=_C
_PhivLineSubstate_Object=MibTableColumn
phivLineSubstate=_PhivLineSubstate_Object((1,3,6,1,2,1,18,12,1,1,4),_PhivLineSubstate_Type())
phivLineSubstate.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineSubstate.setStatus(_A)
class _PhivLineService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_I,4)))
_PhivLineService_Type.__name__=_C
_PhivLineService_Object=MibTableColumn
phivLineService=_PhivLineService_Object((1,3,6,1,2,1,18,12,1,1,5),_PhivLineService_Type())
phivLineService.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineService.setStatus(_A)
class _PhivLineDevice_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PhivLineDevice_Type.__name__=_H
_PhivLineDevice_Object=MibTableColumn
phivLineDevice=_PhivLineDevice_Object((1,3,6,1,2,1,18,12,1,1,6),_PhivLineDevice_Type())
phivLineDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineDevice.setStatus(_A)
class _PhivLineReceiveBuffs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PhivLineReceiveBuffs_Type.__name__=_C
_PhivLineReceiveBuffs_Object=MibTableColumn
phivLineReceiveBuffs=_PhivLineReceiveBuffs_Object((1,3,6,1,2,1,18,12,1,1,7),_PhivLineReceiveBuffs_Type())
phivLineReceiveBuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineReceiveBuffs.setStatus(_A)
class _PhivLineProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,14,15)));namedValues=NamedValues(*((_j,1),(_k,2),(_l,3),('reserved',4),(_m,5),('olapb',6),(_W,7),('ci',8),('qp2',9),(_I,14),('fddi',15)))
_PhivLineProtocol_Type.__name__=_C
_PhivLineProtocol_Object=MibTableColumn
phivLineProtocol=_PhivLineProtocol_Object((1,3,6,1,2,1,18,12,1,1,8),_PhivLineProtocol_Type())
phivLineProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineProtocol.setStatus(_A)
class _PhivLineServiceTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivLineServiceTimer_Type.__name__=_C
_PhivLineServiceTimer_Object=MibTableColumn
phivLineServiceTimer=_PhivLineServiceTimer_Object((1,3,6,1,2,1,18,12,1,1,9),_PhivLineServiceTimer_Type())
phivLineServiceTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineServiceTimer.setStatus(_A)
class _PhivLineMaxBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivLineMaxBlock_Type.__name__=_C
_PhivLineMaxBlock_Object=MibTableColumn
phivLineMaxBlock=_PhivLineMaxBlock_Object((1,3,6,1,2,1,18,12,1,1,10),_PhivLineMaxBlock_Type())
phivLineMaxBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:phivLineMaxBlock.setStatus(_A)
_NonBroadcastLine_ObjectIdentity=ObjectIdentity
nonBroadcastLine=_NonBroadcastLine_ObjectIdentity((1,3,6,1,2,1,18,14))
_PhivNonBroadcastTable_Object=MibTable
phivNonBroadcastTable=_PhivNonBroadcastTable_Object((1,3,6,1,2,1,18,14,1))
if mibBuilder.loadTexts:phivNonBroadcastTable.setStatus(_A)
_PhivNonBroadcastEntry_Object=MibTableRow
phivNonBroadcastEntry=_PhivNonBroadcastEntry_Object((1,3,6,1,2,1,18,14,1,1))
phivNonBroadcastEntry.setIndexNames((0,_F,_A4))
if mibBuilder.loadTexts:phivNonBroadcastEntry.setStatus(_A)
_PhivNonBroadcastIndex_Type=InterfaceIndex
_PhivNonBroadcastIndex_Object=MibTableColumn
phivNonBroadcastIndex=_PhivNonBroadcastIndex_Object((1,3,6,1,2,1,18,14,1,1,1),_PhivNonBroadcastIndex_Type())
phivNonBroadcastIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivNonBroadcastIndex.setStatus(_A)
class _PhivNonBroadcastController_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('loopback',2),(_I,3)))
_PhivNonBroadcastController_Type.__name__=_C
_PhivNonBroadcastController_Object=MibTableColumn
phivNonBroadcastController=_PhivNonBroadcastController_Object((1,3,6,1,2,1,18,14,1,1,2),_PhivNonBroadcastController_Type())
phivNonBroadcastController.setMaxAccess(_B)
if mibBuilder.loadTexts:phivNonBroadcastController.setStatus(_A)
class _PhivNonBroadcastDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('half',2)))
_PhivNonBroadcastDuplex_Type.__name__=_C
_PhivNonBroadcastDuplex_Object=MibTableColumn
phivNonBroadcastDuplex=_PhivNonBroadcastDuplex_Object((1,3,6,1,2,1,18,14,1,1,3),_PhivNonBroadcastDuplex_Type())
phivNonBroadcastDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivNonBroadcastDuplex.setStatus(_A)
class _PhivNonBroadcastClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('external',1),('internal',2),(_I,3)))
_PhivNonBroadcastClock_Type.__name__=_C
_PhivNonBroadcastClock_Object=MibTableColumn
phivNonBroadcastClock=_PhivNonBroadcastClock_Object((1,3,6,1,2,1,18,14,1,1,4),_PhivNonBroadcastClock_Type())
phivNonBroadcastClock.setMaxAccess(_B)
if mibBuilder.loadTexts:phivNonBroadcastClock.setStatus(_A)
class _PhivNonBroadcastRetransmitTimer_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivNonBroadcastRetransmitTimer_Type.__name__=_C
_PhivNonBroadcastRetransmitTimer_Object=MibTableColumn
phivNonBroadcastRetransmitTimer=_PhivNonBroadcastRetransmitTimer_Object((1,3,6,1,2,1,18,14,1,1,5),_PhivNonBroadcastRetransmitTimer_Type())
phivNonBroadcastRetransmitTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:phivNonBroadcastRetransmitTimer.setStatus(_A)
_Area_ObjectIdentity=ObjectIdentity
area=_Area_ObjectIdentity((1,3,6,1,2,1,18,15))
_PhivAreaTable_Object=MibTable
phivAreaTable=_PhivAreaTable_Object((1,3,6,1,2,1,18,15,1))
if mibBuilder.loadTexts:phivAreaTable.setStatus(_A)
_PhivAreaEntry_Object=MibTableRow
phivAreaEntry=_PhivAreaEntry_Object((1,3,6,1,2,1,18,15,1,1))
phivAreaEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:phivAreaEntry.setStatus(_A)
class _PhivAreaNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_PhivAreaNum_Type.__name__=_C
_PhivAreaNum_Object=MibTableColumn
phivAreaNum=_PhivAreaNum_Object((1,3,6,1,2,1,18,15,1,1,1),_PhivAreaNum_Type())
phivAreaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAreaNum.setStatus(_A)
class _PhivAreaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5)));namedValues=NamedValues(*(('reachable',4),('unreachable',5)))
_PhivAreaState_Type.__name__=_C
_PhivAreaState_Object=MibTableColumn
phivAreaState=_PhivAreaState_Object((1,3,6,1,2,1,18,15,1,1,2),_PhivAreaState_Type())
phivAreaState.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAreaState.setStatus(_A)
_PhivAreaCost_Type=Gauge32
_PhivAreaCost_Object=MibTableColumn
phivAreaCost=_PhivAreaCost_Object((1,3,6,1,2,1,18,15,1,1,3),_PhivAreaCost_Type())
phivAreaCost.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAreaCost.setStatus(_A)
class _PhivAreaHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PhivAreaHops_Type.__name__=_C
_PhivAreaHops_Object=MibTableColumn
phivAreaHops=_PhivAreaHops_Object((1,3,6,1,2,1,18,15,1,1,4),_PhivAreaHops_Type())
phivAreaHops.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAreaHops.setStatus(_A)
_PhivAreaNextNode_Type=PhivAddr
_PhivAreaNextNode_Object=MibTableColumn
phivAreaNextNode=_PhivAreaNextNode_Object((1,3,6,1,2,1,18,15,1,1,5),_PhivAreaNextNode_Type())
phivAreaNextNode.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAreaNextNode.setStatus(_A)
class _PhivAreaCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PhivAreaCircuitIndex_Type.__name__=_C
_PhivAreaCircuitIndex_Object=MibTableColumn
phivAreaCircuitIndex=_PhivAreaCircuitIndex_Object((1,3,6,1,2,1,18,15,1,1,6),_PhivAreaCircuitIndex_Type())
phivAreaCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:phivAreaCircuitIndex.setStatus(_A)
class _PhivAreaMaxCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1022))
_PhivAreaMaxCost_Type.__name__=_C
_PhivAreaMaxCost_Object=MibScalar
phivAreaMaxCost=_PhivAreaMaxCost_Object((1,3,6,1,2,1,18,15,2),_PhivAreaMaxCost_Type())
phivAreaMaxCost.setMaxAccess(_E)
if mibBuilder.loadTexts:phivAreaMaxCost.setStatus(_A)
class _PhivAreaMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PhivAreaMaxHops_Type.__name__=_C
_PhivAreaMaxHops_Object=MibScalar
phivAreaMaxHops=_PhivAreaMaxHops_Object((1,3,6,1,2,1,18,15,3),_PhivAreaMaxHops_Type())
phivAreaMaxHops.setMaxAccess(_E)
if mibBuilder.loadTexts:phivAreaMaxHops.setStatus(_A)
class _PhivRouteMaxArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_PhivRouteMaxArea_Type.__name__=_C
_PhivRouteMaxArea_Object=MibScalar
phivRouteMaxArea=_PhivRouteMaxArea_Object((1,3,6,1,2,1,18,15,4),_PhivRouteMaxArea_Type())
phivRouteMaxArea.setMaxAccess(_E)
if mibBuilder.loadTexts:phivRouteMaxArea.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'PhivAddr':PhivAddr,_D:PhivCounter,'InterfaceIndex':InterfaceIndex,'phiv':phiv,'phivSystem':phivSystem,'phivSystemState':phivSystemState,'phivExecIdent':phivExecIdent,'phivManagement':phivManagement,'phivMgmtMgmtVers':phivMgmtMgmtVers,'session':session,'phivSessionSystemName':phivSessionSystemName,'phivSessionInTimer':phivSessionInTimer,'phivSessionOutTimer':phivSessionOutTimer,'end':end,'phivEndRemoteTable':phivEndRemoteTable,'phivEndRemoteEntry':phivEndRemoteEntry,_Y:phivEndRemoteHostNodeID,'phivEndRemoteState':phivEndRemoteState,'phivEndCircuitIndex':phivEndCircuitIndex,'phivEndActiveLinks':phivEndActiveLinks,'phivEndDelay':phivEndDelay,'phivEndCountTable':phivEndCountTable,'phivEndCountEntry':phivEndCountEntry,_Z:phivEndCountHostNodeID,'phivEndCountSecsLastZeroed':phivEndCountSecsLastZeroed,'phivEndCountUsrBytesRec':phivEndCountUsrBytesRec,'phivEndCountUsrBytesSent':phivEndCountUsrBytesSent,'phivEndUCountUsrMessRec':phivEndUCountUsrMessRec,'phivEndCountUsrMessSent':phivEndCountUsrMessSent,'phivEndCountTotalBytesRec':phivEndCountTotalBytesRec,'phivEndCountTotalBytesSent':phivEndCountTotalBytesSent,'phivEndCountTotalMessRec':phivEndCountTotalMessRec,'phivEndCountTotalMessSent':phivEndCountTotalMessSent,'phivEndCountConnectsRecd':phivEndCountConnectsRecd,'phivEndCountConnectsSent':phivEndCountConnectsSent,'phivEndCountReponseTimeouts':phivEndCountReponseTimeouts,'phivEndCountRecdConnectResErrs':phivEndCountRecdConnectResErrs,'phivEndMaxLinks':phivEndMaxLinks,'phivEndNSPVers':phivEndNSPVers,'phivEndRetransmitFactor':phivEndRetransmitFactor,'phivEndDelayFact':phivEndDelayFact,'phivEndDelayWeight':phivEndDelayWeight,'phivEndInactivityTimer':phivEndInactivityTimer,'phivEndCountZeroCount':phivEndCountZeroCount,'phivEndMaxLinksActive':phivEndMaxLinksActive,'routing':routing,'phivRouteBroadcastRouteTimer':phivRouteBroadcastRouteTimer,'phivRouteBuffSize':phivRouteBuffSize,'phivRouteRoutingVers':phivRouteRoutingVers,'phivRouteMaxAddr':phivRouteMaxAddr,'phivRouteMaxBdcastNonRouters':phivRouteMaxBdcastNonRouters,'phivRouteMaxBdcastRouters':phivRouteMaxBdcastRouters,'phivRouteMaxBuffs':phivRouteMaxBuffs,'phivRouteMaxCircuits':phivRouteMaxCircuits,'phivRouteMaxCost':phivRouteMaxCost,'phivRouteMaxHops':phivRouteMaxHops,'phivRouteMaxVisits':phivRouteMaxVisits,'phivRouteRoutingTimer':phivRouteRoutingTimer,'phivRouteSegBuffSize':phivRouteSegBuffSize,'phivRouteType':phivRouteType,'phivRouteCountAgedPktLoss':phivRouteCountAgedPktLoss,'phivRouteCountNodeUnrPktLoss':phivRouteCountNodeUnrPktLoss,'phivRouteCountOutRngePktLoss':phivRouteCountOutRngePktLoss,'phivRouteCountOverSzePktLoss':phivRouteCountOverSzePktLoss,'phivRouteCountPacketFmtErr':phivRouteCountPacketFmtErr,'phivRouteCountPtlRteUpdtLoss':phivRouteCountPtlRteUpdtLoss,'phivRouteCountVerifReject':phivRouteCountVerifReject,'phivLevel1RouteTable':phivLevel1RouteTable,'phivLevel1RouteEntry':phivLevel1RouteEntry,_a:phivLevel1RouteNodeAddr,'phivLevel1RouteCircuitIndex':phivLevel1RouteCircuitIndex,'phivLevel1RouteCost':phivLevel1RouteCost,'phivLevel1RouteHops':phivLevel1RouteHops,'phivLevel1RouteNextNode':phivLevel1RouteNextNode,'phivRouteCountZeroCount':phivRouteCountZeroCount,'phivRouteSystemAddr':phivRouteSystemAddr,'phivRouteRoutingType':phivRouteRoutingType,'phivRouteSystemAddress':phivRouteSystemAddress,'circuit':circuit,'phivCircuitParametersTable':phivCircuitParametersTable,'phivCircuitParametersEntry':phivCircuitParametersEntry,_R:phivCircuitIndex,'phivCircuitLineIndex':phivCircuitLineIndex,'phivCircuitCommonState':phivCircuitCommonState,'phivCircuitCommonSubState':phivCircuitCommonSubState,'phivCircuitCommonName':phivCircuitCommonName,'phivCircuitExecRecallTimer':phivCircuitExecRecallTimer,'phivCircuitCommonType':phivCircuitCommonType,'phivCircuitService':phivCircuitService,'phivCircuitExecCost':phivCircuitExecCost,'phivCircuitExecHelloTimer':phivCircuitExecHelloTimer,'phivCircuitCountTable':phivCircuitCountTable,'phivCircuitCountEntry':phivCircuitCountEntry,'phivCircuitCountSecLastZeroed':phivCircuitCountSecLastZeroed,'phivCircuitCountTermPacketsRecd':phivCircuitCountTermPacketsRecd,'phivCircuitCountOriginPackSent':phivCircuitCountOriginPackSent,'phivCircuitCountTermCongLoss':phivCircuitCountTermCongLoss,'phivCircuitCountCorruptLoss':phivCircuitCountCorruptLoss,'phivCircuitCountTransitPksRecd':phivCircuitCountTransitPksRecd,'phivCircuitCountTransitPkSent':phivCircuitCountTransitPkSent,'phivCircuitCountTransitCongestLoss':phivCircuitCountTransitCongestLoss,'phivCircuitCountCircuitDown':phivCircuitCountCircuitDown,'phivCircuitCountInitFailure':phivCircuitCountInitFailure,'phivCircuitCountAdjDown':phivCircuitCountAdjDown,'phivCircuitCountPeakAdj':phivCircuitCountPeakAdj,'phivCircuitCountBytesRecd':phivCircuitCountBytesRecd,'phivCircuitCountBytesSent':phivCircuitCountBytesSent,'phivCircuitCountDataBlocksRecd':phivCircuitCountDataBlocksRecd,'phivCircuitCountDataBlocksSent':phivCircuitCountDataBlocksSent,'phivCircuitCountUsrBuffUnav':phivCircuitCountUsrBuffUnav,'phivCircuitOrigQueueLimit':phivCircuitOrigQueueLimit,'phivCircuitCountZeroCount':phivCircuitCountZeroCount,'ddcmp':ddcmp,'phivDDCMPCircuitParametersTable':phivDDCMPCircuitParametersTable,'phivDDCMPCircuitParametersEntry':phivDDCMPCircuitParametersEntry,_n:phivDDCMPCircuitIndex,'phivDDCMPCircuitAdjNodeAddr':phivDDCMPCircuitAdjNodeAddr,'phivDDCMPCircuitTributary':phivDDCMPCircuitTributary,'phivDDCMPCircuitCountTable':phivDDCMPCircuitCountTable,'phivDDCMPCircuitCountEntry':phivDDCMPCircuitCountEntry,'phivDDCMPCircuitErrorsInbd':phivDDCMPCircuitErrorsInbd,'phivDDCMPCircuitErrorsOutbd':phivDDCMPCircuitErrorsOutbd,'phivDDCMPCircuitRmteReplyTimeouts':phivDDCMPCircuitRmteReplyTimeouts,'phivDDCMPCircuitLocalReplyTimeouts':phivDDCMPCircuitLocalReplyTimeouts,'phivDDCMPCircuitRmteBuffErrors':phivDDCMPCircuitRmteBuffErrors,'phivDDCMPCircuitLocalBuffErrors':phivDDCMPCircuitLocalBuffErrors,'phivDDCMPCircuitSelectIntervalsElap':phivDDCMPCircuitSelectIntervalsElap,'phivDDCMPCircuitSelectTimeouts':phivDDCMPCircuitSelectTimeouts,'phivDDCMPLineCountTable':phivDDCMPLineCountTable,'phivDDCMPLineCountEntry':phivDDCMPLineCountEntry,_o:phivDDCMPLineCountIndex,'phivDDCMPLineCountDataErrsIn':phivDDCMPLineCountDataErrsIn,'phivDDCMPLineCountRmteStationErrs':phivDDCMPLineCountRmteStationErrs,'phivDDCMPLineCountLocalStationErrs':phivDDCMPLineCountLocalStationErrs,'control':control,'phivControlSchedTimer':phivControlSchedTimer,'phivControlDeadTimer':phivControlDeadTimer,'phivControlDelayTimer':phivControlDelayTimer,'phivControlStreamTimer':phivControlStreamTimer,'phivControlParametersTable':phivControlParametersTable,'phivControlParametersEntry':phivControlParametersEntry,_p:phivControlCircuitIndex,'phivControlBabbleTimer':phivControlBabbleTimer,'phivControlMaxBuffs':phivControlMaxBuffs,'phivControlMaxTransmits':phivControlMaxTransmits,'phivControlDyingBase':phivControlDyingBase,'phivControlDyingIncrement':phivControlDyingIncrement,'phivControlDeadThreshold':phivControlDeadThreshold,'phivControlDyingThreshold':phivControlDyingThreshold,'phivControlInactTreshold':phivControlInactTreshold,'phivControlPollingState':phivControlPollingState,'phivControlPollingSubState':phivControlPollingSubState,'phivControlTransTimer':phivControlTransTimer,_W:ethernet,'phivEthLinkParametersTable':phivEthLinkParametersTable,'phivEthLinkParametersEntry':phivEthLinkParametersEntry,_s:phivEthLinkIndex,'phivEthDesigRouterNodeAddr':phivEthDesigRouterNodeAddr,'phivEthMaxRouters':phivEthMaxRouters,'phivEthRouterPri':phivEthRouterPri,'phivEthHardwareAddr':phivEthHardwareAddr,'counters':counters,'phivCountersCountTable':phivCountersCountTable,'phivCountersCountEntry':phivCountersCountEntry,_t:phivCountersIndex,'phivCountersCountBytesRecd':phivCountersCountBytesRecd,'phivCountersCountBytesSent':phivCountersCountBytesSent,'phivCountersCountDataBlocksRecd':phivCountersCountDataBlocksRecd,'phivCountersCountDataBlocksSent':phivCountersCountDataBlocksSent,'phivCountersCountEthUsrBuffUnav':phivCountersCountEthUsrBuffUnav,'phivCountersCountMcastBytesRecd':phivCountersCountMcastBytesRecd,'phivCountersCountDataBlksRecd':phivCountersCountDataBlksRecd,'phivCountersCountDataBlksSent':phivCountersCountDataBlksSent,'phivCountersCountMcastBlksRecd':phivCountersCountMcastBlksRecd,'phivCountersCountBlksSentDef':phivCountersCountBlksSentDef,'phivCountersCountBlksSentSingleCol':phivCountersCountBlksSentSingleCol,'phivCountersCountBlksSentMultCol':phivCountersCountBlksSentMultCol,'phivCountersCountSendFailure':phivCountersCountSendFailure,'phivCountersCountCollDetectFailure':phivCountersCountCollDetectFailure,'phivCountersCountReceiveFailure':phivCountersCountReceiveFailure,'phivCountersCountUnrecFrameDest':phivCountersCountUnrecFrameDest,'phivCountersCountDataOver':phivCountersCountDataOver,'phivCountersCountSysBuffUnav':phivCountersCountSysBuffUnav,'phivCountersCountUsrBuffUnav':phivCountersCountUsrBuffUnav,'adjacency':adjacency,'phivAdjTable':phivAdjTable,'phivAdjEntry':phivAdjEntry,_u:phivAdjCircuitIndex,'phivAdjNodeAddr':phivAdjNodeAddr,'phivAdjBlockSize':phivAdjBlockSize,'phivAdjListenTimer':phivAdjListenTimer,'phivAdjCircuitEtherServPhysAddr':phivAdjCircuitEtherServPhysAddr,'phivAdjType':phivAdjType,'phivAdjState':phivAdjState,'phivAdjPriority':phivAdjPriority,'phivAdjExecListenTimer':phivAdjExecListenTimer,'phivAdjNodeTable':phivAdjNodeTable,'phivAdjNodeEntry':phivAdjNodeEntry,_A1:phivAdjNodeCircuitIndex,_A2:phivAdjAddr,'phivAdjNodeBlockSize':phivAdjNodeBlockSize,'phivAdjNodeListenTimer':phivAdjNodeListenTimer,'phivAdjNodeCircuitEtherServPhysAddr':phivAdjNodeCircuitEtherServPhysAddr,'phivAdjNodeType':phivAdjNodeType,'phivAdjNodeState':phivAdjNodeState,'phivAdjNodePriority':phivAdjNodePriority,'line':line,'phivLineTable':phivLineTable,'phivLineEntry':phivLineEntry,_A3:phivLineIndex,'phivLineName':phivLineName,'phivLineState':phivLineState,'phivLineSubstate':phivLineSubstate,'phivLineService':phivLineService,'phivLineDevice':phivLineDevice,'phivLineReceiveBuffs':phivLineReceiveBuffs,'phivLineProtocol':phivLineProtocol,'phivLineServiceTimer':phivLineServiceTimer,'phivLineMaxBlock':phivLineMaxBlock,'nonBroadcastLine':nonBroadcastLine,'phivNonBroadcastTable':phivNonBroadcastTable,'phivNonBroadcastEntry':phivNonBroadcastEntry,_A4:phivNonBroadcastIndex,'phivNonBroadcastController':phivNonBroadcastController,'phivNonBroadcastDuplex':phivNonBroadcastDuplex,'phivNonBroadcastClock':phivNonBroadcastClock,'phivNonBroadcastRetransmitTimer':phivNonBroadcastRetransmitTimer,_K:area,'phivAreaTable':phivAreaTable,'phivAreaEntry':phivAreaEntry,_A5:phivAreaNum,'phivAreaState':phivAreaState,'phivAreaCost':phivAreaCost,'phivAreaHops':phivAreaHops,'phivAreaNextNode':phivAreaNextNode,'phivAreaCircuitIndex':phivAreaCircuitIndex,'phivAreaMaxCost':phivAreaMaxCost,'phivAreaMaxHops':phivAreaMaxHops,'phivRouteMaxArea':phivRouteMaxArea})