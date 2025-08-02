_o='vRtrMplsIfStatEntry'
_n='vRtrMplsLspStatEntry'
_m='vRtrMplsLspName'
_l='read-write'
_k='vRtrMplsLspStatsLspName'
_j='vRtrMplsLspStatsSenderAddr'
_i='vRtrMplsLspStatsSenderAddrType'
_h='vRtrMplsLspStatsType'
_g='TmnxMplsLabelOwner'
_f='vRtrMplsStaticSvcLabel'
_e='vRtrMplsStaticLSPLabel'
_d='vRtrMplsLabelType'
_c='minutes'
_b='TmnxMplsLspBgpRSVPLSPTunState'
_a='mega-bits per second'
_Z='dynamic'
_Y='vRtrMplsLspIndex'
_X='static'
_W='vRtrIfIndex'
_V='TmnxRsvpDSTEClassType'
_U='TmnxMplsTpGlobalID'
_T='TNamedItemOrEmpty'
_S='TmnxMplsLspAddrType'
_R='none'
_Q='TmnxMplsTpNodeID'
_P='MplsLabel'
_O='InetAddress'
_N='TmnxAdminState'
_M='not-accessible'
_L='seconds'
_K='tnSysSwitchId'
_J='TROPIC-SYSTEM-MIB'
_I='vRtrID'
_H='Integer32'
_G='TN-VRTR-MIB'
_F='TN-MPLS-MIB'
_E='TruthValue'
_D='Unsigned32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressType')
MplsLSPID,MplsLabel=mibBuilder.importSymbols('MPLS-LSR-MIB','MplsLSPID',_P)
MplsTunnelIndex,mplsTunnelARHopEntry,mplsTunnelIndex,mplsTunnelIngressLSRId,mplsTunnelInstance=mibBuilder.importSymbols('MPLS-TE-MIB','MplsTunnelIndex','mplsTunnelARHopEntry','mplsTunnelIndex','mplsTunnelIngressLSRId','mplsTunnelInstance')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeInterval','TimeStamp',_E)
TLNamedItemOrEmpty,TNamedItem,TNamedItemOrEmpty,TmnxActionType,TmnxAdminState,TmnxMplsTpGlobalID,TmnxMplsTpNodeID,TmnxOperState,TmnxRsvpDSTEClassType,TmnxVRtrMplsLspID=mibBuilder.importSymbols('TN-TC-MIB','TLNamedItemOrEmpty','TNamedItem',_T,'TmnxActionType',_N,_U,_Q,'TmnxOperState',_V,'TmnxVRtrMplsLspID')
vRtrID,vRtrIfIndex=mibBuilder.importSymbols(_G,_I,_W)
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_J,_K)
tnMplsMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,6))
if mibBuilder.loadTexts:tnMplsMIBModule.setRevisions(('2015-09-29 00:00','2015-05-29 00:00','2015-04-30 00:00','2011-02-01 00:00','2009-02-28 00:00','2008-07-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-03-23 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-01-15 00:00','2003-08-15 00:00','2000-09-07 00:00','2000-08-14 00:00'))
class TmnxMplsLabelOwner(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,0),('rsvp',1),('tldp',2),('ildp',3),('svcmgr',4),('bgp',5),('mirror',6),(_X,7),('vprn',8)))
class TmnxMplsOperDownReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('operUp',0),('adminDown',1),('noResources',2),('systemIpDown',3),('iomFailure',4),('clearDown',5)))
class TmnxMplsLspBgpRSVPLSPTunState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
class TmnxMplsLspAddrType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('nodeId',2)))
_TnMplsObjs_ObjectIdentity=ObjectIdentity
tnMplsObjs=_TnMplsObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,6))
_VRtrMplsLspTable_Object=MibTable
vRtrMplsLspTable=_VRtrMplsLspTable_Object((1,3,6,1,4,1,7483,6,1,2,6,1))
if mibBuilder.loadTexts:vRtrMplsLspTable.setStatus(_A)
_VRtrMplsLspEntry_Object=MibTableRow
vRtrMplsLspEntry=_VRtrMplsLspEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1))
vRtrMplsLspEntry.setIndexNames((0,_J,_K),(0,_G,_I),(0,_F,_Y))
if mibBuilder.loadTexts:vRtrMplsLspEntry.setStatus(_A)
_VRtrMplsLspIndex_Type=TmnxVRtrMplsLspID
_VRtrMplsLspIndex_Object=MibTableColumn
vRtrMplsLspIndex=_VRtrMplsLspIndex_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,1),_VRtrMplsLspIndex_Type())
vRtrMplsLspIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:vRtrMplsLspIndex.setStatus(_A)
_VRtrMplsLspRowStatus_Type=RowStatus
_VRtrMplsLspRowStatus_Object=MibTableColumn
vRtrMplsLspRowStatus=_VRtrMplsLspRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,2),_VRtrMplsLspRowStatus_Type())
vRtrMplsLspRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspRowStatus.setStatus(_A)
_VRtrMplsLspLastChange_Type=TimeStamp
_VRtrMplsLspLastChange_Object=MibTableColumn
vRtrMplsLspLastChange=_VRtrMplsLspLastChange_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,3),_VRtrMplsLspLastChange_Type())
vRtrMplsLspLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspLastChange.setStatus(_A)
_VRtrMplsLspName_Type=TLNamedItemOrEmpty
_VRtrMplsLspName_Object=MibTableColumn
vRtrMplsLspName=_VRtrMplsLspName_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,4),_VRtrMplsLspName_Type())
vRtrMplsLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspName.setStatus(_A)
class _VRtrMplsLspAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsLspAdminState_Type.__name__=_N
_VRtrMplsLspAdminState_Object=MibTableColumn
vRtrMplsLspAdminState=_VRtrMplsLspAdminState_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,5),_VRtrMplsLspAdminState_Type())
vRtrMplsLspAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspAdminState.setStatus(_A)
_VRtrMplsLspOperState_Type=TmnxOperState
_VRtrMplsLspOperState_Object=MibTableColumn
vRtrMplsLspOperState=_VRtrMplsLspOperState_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,6),_VRtrMplsLspOperState_Type())
vRtrMplsLspOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspOperState.setStatus(_A)
_VRtrMplsLspFromAddr_Type=IpAddress
_VRtrMplsLspFromAddr_Object=MibTableColumn
vRtrMplsLspFromAddr=_VRtrMplsLspFromAddr_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,7),_VRtrMplsLspFromAddr_Type())
vRtrMplsLspFromAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFromAddr.setStatus(_A)
_VRtrMplsLspToAddr_Type=IpAddress
_VRtrMplsLspToAddr_Object=MibTableColumn
vRtrMplsLspToAddr=_VRtrMplsLspToAddr_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,8),_VRtrMplsLspToAddr_Type())
vRtrMplsLspToAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspToAddr.setStatus(_A)
class _VRtrMplsLspType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),(_Z,2),(_X,3),('bypassOnly',4),('p2mpLsp',5),('p2mpAuto',6),('mplsTp',7)))
_VRtrMplsLspType_Type.__name__=_H
_VRtrMplsLspType_Object=MibTableColumn
vRtrMplsLspType=_VRtrMplsLspType_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,9),_VRtrMplsLspType_Type())
vRtrMplsLspType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspType.setStatus(_A)
class _VRtrMplsLspOutSegIndx_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VRtrMplsLspOutSegIndx_Type.__name__=_H
_VRtrMplsLspOutSegIndx_Object=MibTableColumn
vRtrMplsLspOutSegIndx=_VRtrMplsLspOutSegIndx_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,10),_VRtrMplsLspOutSegIndx_Type())
vRtrMplsLspOutSegIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspOutSegIndx.setStatus(_A)
class _VRtrMplsLspRetryTimer_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_VRtrMplsLspRetryTimer_Type.__name__=_D
_VRtrMplsLspRetryTimer_Object=MibTableColumn
vRtrMplsLspRetryTimer=_VRtrMplsLspRetryTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,11),_VRtrMplsLspRetryTimer_Type())
vRtrMplsLspRetryTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspRetryTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsLspRetryTimer.setUnits(_L)
class _VRtrMplsLspRetryLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_VRtrMplsLspRetryLimit_Type.__name__=_D
_VRtrMplsLspRetryLimit_Object=MibTableColumn
vRtrMplsLspRetryLimit=_VRtrMplsLspRetryLimit_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,12),_VRtrMplsLspRetryLimit_Type())
vRtrMplsLspRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspRetryLimit.setStatus(_A)
class _VRtrMplsLspMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrMplsLspMetric_Type.__name__=_D
_VRtrMplsLspMetric_Object=MibTableColumn
vRtrMplsLspMetric=_VRtrMplsLspMetric_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,13),_VRtrMplsLspMetric_Type())
vRtrMplsLspMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspMetric.setStatus(_A)
class _VRtrMplsLspDecrementTtl_Type(TruthValue):defaultValue=1
_VRtrMplsLspDecrementTtl_Type.__name__=_E
_VRtrMplsLspDecrementTtl_Object=MibTableColumn
vRtrMplsLspDecrementTtl=_VRtrMplsLspDecrementTtl_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,14),_VRtrMplsLspDecrementTtl_Type())
vRtrMplsLspDecrementTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspDecrementTtl.setStatus(_A)
class _VRtrMplsLspCspf_Type(TruthValue):defaultValue=2
_VRtrMplsLspCspf_Type.__name__=_E
_VRtrMplsLspCspf_Object=MibTableColumn
vRtrMplsLspCspf=_VRtrMplsLspCspf_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,15),_VRtrMplsLspCspf_Type())
vRtrMplsLspCspf.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspCspf.setStatus(_A)
class _VRtrMplsLspFastReroute_Type(TruthValue):defaultValue=2
_VRtrMplsLspFastReroute_Type.__name__=_E
_VRtrMplsLspFastReroute_Object=MibTableColumn
vRtrMplsLspFastReroute=_VRtrMplsLspFastReroute_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,16),_VRtrMplsLspFastReroute_Type())
vRtrMplsLspFastReroute.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFastReroute.setStatus(_A)
class _VRtrMplsLspFRHopLimit_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VRtrMplsLspFRHopLimit_Type.__name__=_D
_VRtrMplsLspFRHopLimit_Object=MibTableColumn
vRtrMplsLspFRHopLimit=_VRtrMplsLspFRHopLimit_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,17),_VRtrMplsLspFRHopLimit_Type())
vRtrMplsLspFRHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFRHopLimit.setStatus(_A)
class _VRtrMplsLspFRBandwidth_Type(Unsigned32):defaultValue=0
_VRtrMplsLspFRBandwidth_Type.__name__=_D
_VRtrMplsLspFRBandwidth_Object=MibTableColumn
vRtrMplsLspFRBandwidth=_VRtrMplsLspFRBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,18),_VRtrMplsLspFRBandwidth_Type())
vRtrMplsLspFRBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFRBandwidth.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsLspFRBandwidth.setUnits(_a)
class _VRtrMplsLspClassOfService_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrMplsLspClassOfService_Type.__name__=_T
_VRtrMplsLspClassOfService_Object=MibTableColumn
vRtrMplsLspClassOfService=_VRtrMplsLspClassOfService_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,19),_VRtrMplsLspClassOfService_Type())
vRtrMplsLspClassOfService.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspClassOfService.setStatus(_A)
class _VRtrMplsLspSetupPriority_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VRtrMplsLspSetupPriority_Type.__name__=_D
_VRtrMplsLspSetupPriority_Object=MibTableColumn
vRtrMplsLspSetupPriority=_VRtrMplsLspSetupPriority_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,20),_VRtrMplsLspSetupPriority_Type())
vRtrMplsLspSetupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspSetupPriority.setStatus(_A)
class _VRtrMplsLspHoldPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VRtrMplsLspHoldPriority_Type.__name__=_D
_VRtrMplsLspHoldPriority_Object=MibTableColumn
vRtrMplsLspHoldPriority=_VRtrMplsLspHoldPriority_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,21),_VRtrMplsLspHoldPriority_Type())
vRtrMplsLspHoldPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspHoldPriority.setStatus(_A)
class _VRtrMplsLspRecord_Type(TruthValue):defaultValue=1
_VRtrMplsLspRecord_Type.__name__=_E
_VRtrMplsLspRecord_Object=MibTableColumn
vRtrMplsLspRecord=_VRtrMplsLspRecord_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,22),_VRtrMplsLspRecord_Type())
vRtrMplsLspRecord.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspRecord.setStatus(_A)
class _VRtrMplsLspPreference_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VRtrMplsLspPreference_Type.__name__=_D
_VRtrMplsLspPreference_Object=MibTableColumn
vRtrMplsLspPreference=_VRtrMplsLspPreference_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,23),_VRtrMplsLspPreference_Type())
vRtrMplsLspPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspPreference.setStatus(_A)
class _VRtrMplsLspBandwidth_Type(Integer32):defaultValue=0
_VRtrMplsLspBandwidth_Type.__name__=_H
_VRtrMplsLspBandwidth_Object=MibTableColumn
vRtrMplsLspBandwidth=_VRtrMplsLspBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,24),_VRtrMplsLspBandwidth_Type())
vRtrMplsLspBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspBandwidth.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsLspBandwidth.setUnits(_a)
class _VRtrMplsLspBwProtect_Type(TruthValue):defaultValue=2
_VRtrMplsLspBwProtect_Type.__name__=_E
_VRtrMplsLspBwProtect_Object=MibTableColumn
vRtrMplsLspBwProtect=_VRtrMplsLspBwProtect_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,25),_VRtrMplsLspBwProtect_Type())
vRtrMplsLspBwProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspBwProtect.setStatus(_A)
class _VRtrMplsLspHopLimit_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,255))
_VRtrMplsLspHopLimit_Type.__name__=_D
_VRtrMplsLspHopLimit_Object=MibTableColumn
vRtrMplsLspHopLimit=_VRtrMplsLspHopLimit_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,26),_VRtrMplsLspHopLimit_Type())
vRtrMplsLspHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspHopLimit.setStatus(_A)
class _VRtrMplsLspNegotiatedMTU_Type(Unsigned32):defaultValue=0
_VRtrMplsLspNegotiatedMTU_Type.__name__=_D
_VRtrMplsLspNegotiatedMTU_Object=MibTableColumn
vRtrMplsLspNegotiatedMTU=_VRtrMplsLspNegotiatedMTU_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,27),_VRtrMplsLspNegotiatedMTU_Type())
vRtrMplsLspNegotiatedMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspNegotiatedMTU.setStatus(_A)
class _VRtrMplsLspRsvpResvStyle_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('se',1),('ff',2)))
_VRtrMplsLspRsvpResvStyle_Type.__name__=_H
_VRtrMplsLspRsvpResvStyle_Object=MibTableColumn
vRtrMplsLspRsvpResvStyle=_VRtrMplsLspRsvpResvStyle_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,28),_VRtrMplsLspRsvpResvStyle_Type())
vRtrMplsLspRsvpResvStyle.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspRsvpResvStyle.setStatus(_A)
class _VRtrMplsLspRsvpAdspec_Type(TruthValue):defaultValue=2
_VRtrMplsLspRsvpAdspec_Type.__name__=_E
_VRtrMplsLspRsvpAdspec_Object=MibTableColumn
vRtrMplsLspRsvpAdspec=_VRtrMplsLspRsvpAdspec_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,29),_VRtrMplsLspRsvpAdspec_Type())
vRtrMplsLspRsvpAdspec.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspRsvpAdspec.setStatus(_A)
class _VRtrMplsLspFRMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneToOneBackup',1),('facilityBackup',2)))
_VRtrMplsLspFRMethod_Type.__name__=_H
_VRtrMplsLspFRMethod_Object=MibTableColumn
vRtrMplsLspFRMethod=_VRtrMplsLspFRMethod_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,30),_VRtrMplsLspFRMethod_Type())
vRtrMplsLspFRMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFRMethod.setStatus(_A)
class _VRtrMplsLspFRNodeProtect_Type(TruthValue):defaultValue=1
_VRtrMplsLspFRNodeProtect_Type.__name__=_E
_VRtrMplsLspFRNodeProtect_Object=MibTableColumn
vRtrMplsLspFRNodeProtect=_VRtrMplsLspFRNodeProtect_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,31),_VRtrMplsLspFRNodeProtect_Type())
vRtrMplsLspFRNodeProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFRNodeProtect.setStatus(_A)
class _VRtrMplsLspAdminGroupInclude_Type(Unsigned32):defaultValue=0
_VRtrMplsLspAdminGroupInclude_Type.__name__=_D
_VRtrMplsLspAdminGroupInclude_Object=MibTableColumn
vRtrMplsLspAdminGroupInclude=_VRtrMplsLspAdminGroupInclude_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,32),_VRtrMplsLspAdminGroupInclude_Type())
vRtrMplsLspAdminGroupInclude.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspAdminGroupInclude.setStatus(_A)
class _VRtrMplsLspAdminGroupExclude_Type(Unsigned32):defaultValue=0
_VRtrMplsLspAdminGroupExclude_Type.__name__=_D
_VRtrMplsLspAdminGroupExclude_Object=MibTableColumn
vRtrMplsLspAdminGroupExclude=_VRtrMplsLspAdminGroupExclude_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,33),_VRtrMplsLspAdminGroupExclude_Type())
vRtrMplsLspAdminGroupExclude.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspAdminGroupExclude.setStatus(_A)
class _VRtrMplsLspAdaptive_Type(TruthValue):defaultValue=1
_VRtrMplsLspAdaptive_Type.__name__=_E
_VRtrMplsLspAdaptive_Object=MibTableColumn
vRtrMplsLspAdaptive=_VRtrMplsLspAdaptive_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,34),_VRtrMplsLspAdaptive_Type())
vRtrMplsLspAdaptive.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspAdaptive.setStatus(_A)
class _VRtrMplsLspInheritance_Type(Unsigned32):defaultValue=0
_VRtrMplsLspInheritance_Type.__name__=_D
_VRtrMplsLspInheritance_Object=MibTableColumn
vRtrMplsLspInheritance=_VRtrMplsLspInheritance_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,35),_VRtrMplsLspInheritance_Type())
vRtrMplsLspInheritance.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspInheritance.setStatus(_A)
class _VRtrMplsLspOptimizeTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrMplsLspOptimizeTimer_Type.__name__=_D
_VRtrMplsLspOptimizeTimer_Object=MibTableColumn
vRtrMplsLspOptimizeTimer=_VRtrMplsLspOptimizeTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,36),_VRtrMplsLspOptimizeTimer_Type())
vRtrMplsLspOptimizeTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspOptimizeTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsLspOptimizeTimer.setUnits(_L)
_VRtrMplsLspOperFastReroute_Type=TruthValue
_VRtrMplsLspOperFastReroute_Object=MibTableColumn
vRtrMplsLspOperFastReroute=_VRtrMplsLspOperFastReroute_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,37),_VRtrMplsLspOperFastReroute_Type())
vRtrMplsLspOperFastReroute.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspOperFastReroute.setStatus(_A)
class _VRtrMplsLspFRObject_Type(TruthValue):defaultValue=1
_VRtrMplsLspFRObject_Type.__name__=_E
_VRtrMplsLspFRObject_Object=MibTableColumn
vRtrMplsLspFRObject=_VRtrMplsLspFRObject_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,38),_VRtrMplsLspFRObject_Type())
vRtrMplsLspFRObject.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFRObject.setStatus(_A)
class _VRtrMplsLspHoldTimer_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_VRtrMplsLspHoldTimer_Type.__name__=_D
_VRtrMplsLspHoldTimer_Object=MibTableColumn
vRtrMplsLspHoldTimer=_VRtrMplsLspHoldTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,39),_VRtrMplsLspHoldTimer_Type())
vRtrMplsLspHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsLspHoldTimer.setUnits(_L)
class _VRtrMplsLspCspfTeMetricEnabled_Type(TruthValue):defaultValue=2
_VRtrMplsLspCspfTeMetricEnabled_Type.__name__=_E
_VRtrMplsLspCspfTeMetricEnabled_Object=MibTableColumn
vRtrMplsLspCspfTeMetricEnabled=_VRtrMplsLspCspfTeMetricEnabled_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,40),_VRtrMplsLspCspfTeMetricEnabled_Type())
vRtrMplsLspCspfTeMetricEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspCspfTeMetricEnabled.setStatus(_A)
class _VRtrMplsLspP2mpId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_VRtrMplsLspP2mpId_Type.__name__=_D
_VRtrMplsLspP2mpId_Object=MibTableColumn
vRtrMplsLspP2mpId=_VRtrMplsLspP2mpId_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,41),_VRtrMplsLspP2mpId_Type())
vRtrMplsLspP2mpId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspP2mpId.setStatus(_A)
class _VRtrMplsLspClassType_Type(TmnxRsvpDSTEClassType):defaultValue=0
_VRtrMplsLspClassType_Type.__name__=_V
_VRtrMplsLspClassType_Object=MibTableColumn
vRtrMplsLspClassType=_VRtrMplsLspClassType_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,42),_VRtrMplsLspClassType_Type())
vRtrMplsLspClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspClassType.setStatus(_A)
_VRtrMplsLspOperMetric_Type=Unsigned32
_VRtrMplsLspOperMetric_Object=MibTableColumn
vRtrMplsLspOperMetric=_VRtrMplsLspOperMetric_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,43),_VRtrMplsLspOperMetric_Type())
vRtrMplsLspOperMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspOperMetric.setStatus(_A)
class _VRtrMplsLspLdpOverRsvpInclude_Type(TruthValue):defaultValue=1
_VRtrMplsLspLdpOverRsvpInclude_Type.__name__=_E
_VRtrMplsLspLdpOverRsvpInclude_Object=MibTableColumn
vRtrMplsLspLdpOverRsvpInclude=_VRtrMplsLspLdpOverRsvpInclude_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,44),_VRtrMplsLspLdpOverRsvpInclude_Type())
vRtrMplsLspLdpOverRsvpInclude.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspLdpOverRsvpInclude.setStatus(_A)
class _VRtrMplsLspLeastFill_Type(TruthValue):defaultValue=2
_VRtrMplsLspLeastFill_Type.__name__=_E
_VRtrMplsLspLeastFill_Object=MibTableColumn
vRtrMplsLspLeastFill=_VRtrMplsLspLeastFill_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,45),_VRtrMplsLspLeastFill_Type())
vRtrMplsLspLeastFill.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspLeastFill.setStatus(_A)
class _VRtrMplsLspVprnAutoBindInclude_Type(TruthValue):defaultValue=1
_VRtrMplsLspVprnAutoBindInclude_Type.__name__=_E
_VRtrMplsLspVprnAutoBindInclude_Object=MibTableColumn
vRtrMplsLspVprnAutoBindInclude=_VRtrMplsLspVprnAutoBindInclude_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,46),_VRtrMplsLspVprnAutoBindInclude_Type())
vRtrMplsLspVprnAutoBindInclude.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspVprnAutoBindInclude.setStatus(_A)
class _VRtrMplsLspMainCTRetryLimit_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_VRtrMplsLspMainCTRetryLimit_Type.__name__=_D
_VRtrMplsLspMainCTRetryLimit_Object=MibTableColumn
vRtrMplsLspMainCTRetryLimit=_VRtrMplsLspMainCTRetryLimit_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,47),_VRtrMplsLspMainCTRetryLimit_Type())
vRtrMplsLspMainCTRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspMainCTRetryLimit.setStatus(_A)
class _VRtrMplsLspIgpShortcut_Type(TruthValue):defaultValue=1
_VRtrMplsLspIgpShortcut_Type.__name__=_E
_VRtrMplsLspIgpShortcut_Object=MibTableColumn
vRtrMplsLspIgpShortcut=_VRtrMplsLspIgpShortcut_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,48),_VRtrMplsLspIgpShortcut_Type())
vRtrMplsLspIgpShortcut.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspIgpShortcut.setStatus(_A)
_VRtrMplsLspOriginTemplate_Type=TNamedItemOrEmpty
_VRtrMplsLspOriginTemplate_Object=MibTableColumn
vRtrMplsLspOriginTemplate=_VRtrMplsLspOriginTemplate_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,49),_VRtrMplsLspOriginTemplate_Type())
vRtrMplsLspOriginTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspOriginTemplate.setStatus(_A)
class _VRtrMplsLspAutoBandwidth_Type(TruthValue):defaultValue=2
_VRtrMplsLspAutoBandwidth_Type.__name__=_E
_VRtrMplsLspAutoBandwidth_Object=MibTableColumn
vRtrMplsLspAutoBandwidth=_VRtrMplsLspAutoBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,50),_VRtrMplsLspAutoBandwidth_Type())
vRtrMplsLspAutoBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspAutoBandwidth.setStatus(_A)
class _VRtrMplsLspCspfToFirstLoose_Type(TruthValue):defaultValue=2
_VRtrMplsLspCspfToFirstLoose_Type.__name__=_E
_VRtrMplsLspCspfToFirstLoose_Object=MibTableColumn
vRtrMplsLspCspfToFirstLoose=_VRtrMplsLspCspfToFirstLoose_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,51),_VRtrMplsLspCspfToFirstLoose_Type())
vRtrMplsLspCspfToFirstLoose.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspCspfToFirstLoose.setStatus(_A)
class _VRtrMplsLspPropAdminGroup_Type(TruthValue):defaultValue=2
_VRtrMplsLspPropAdminGroup_Type.__name__=_E
_VRtrMplsLspPropAdminGroup_Object=MibTableColumn
vRtrMplsLspPropAdminGroup=_VRtrMplsLspPropAdminGroup_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,52),_VRtrMplsLspPropAdminGroup_Type())
vRtrMplsLspPropAdminGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspPropAdminGroup.setStatus(_A)
class _VRtrMplsLspBgpShortcut_Type(TruthValue):defaultValue=1
_VRtrMplsLspBgpShortcut_Type.__name__=_E
_VRtrMplsLspBgpShortcut_Object=MibTableColumn
vRtrMplsLspBgpShortcut=_VRtrMplsLspBgpShortcut_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,53),_VRtrMplsLspBgpShortcut_Type())
vRtrMplsLspBgpShortcut.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspBgpShortcut.setStatus(_A)
class _VRtrMplsLspBgpTransportTunnel_Type(TmnxMplsLspBgpRSVPLSPTunState):defaultValue=1
_VRtrMplsLspBgpTransportTunnel_Type.__name__=_b
_VRtrMplsLspBgpTransportTunnel_Object=MibTableColumn
vRtrMplsLspBgpTransportTunnel=_VRtrMplsLspBgpTransportTunnel_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,54),_VRtrMplsLspBgpTransportTunnel_Type())
vRtrMplsLspBgpTransportTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspBgpTransportTunnel.setStatus(_A)
_VRtrMplsLspSwitchStbyPath_Type=TmnxActionType
_VRtrMplsLspSwitchStbyPath_Object=MibTableColumn
vRtrMplsLspSwitchStbyPath=_VRtrMplsLspSwitchStbyPath_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,55),_VRtrMplsLspSwitchStbyPath_Type())
vRtrMplsLspSwitchStbyPath.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspSwitchStbyPath.setStatus(_A)
_VRtrMplsLspSwitchStbyPathIndex_Type=MplsTunnelIndex
_VRtrMplsLspSwitchStbyPathIndex_Object=MibTableColumn
vRtrMplsLspSwitchStbyPathIndex=_VRtrMplsLspSwitchStbyPathIndex_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,56),_VRtrMplsLspSwitchStbyPathIndex_Type())
vRtrMplsLspSwitchStbyPathIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspSwitchStbyPathIndex.setStatus(_A)
class _VRtrMplsLspSwitchStbyPathForce_Type(TruthValue):defaultValue=2
_VRtrMplsLspSwitchStbyPathForce_Type.__name__=_E
_VRtrMplsLspSwitchStbyPathForce_Object=MibTableColumn
vRtrMplsLspSwitchStbyPathForce=_VRtrMplsLspSwitchStbyPathForce_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,57),_VRtrMplsLspSwitchStbyPathForce_Type())
vRtrMplsLspSwitchStbyPathForce.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspSwitchStbyPathForce.setStatus(_A)
_VRtrMplsLspExcludeNodeAddrType_Type=InetAddressType
_VRtrMplsLspExcludeNodeAddrType_Object=MibTableColumn
vRtrMplsLspExcludeNodeAddrType=_VRtrMplsLspExcludeNodeAddrType_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,58),_VRtrMplsLspExcludeNodeAddrType_Type())
vRtrMplsLspExcludeNodeAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspExcludeNodeAddrType.setStatus(_A)
class _VRtrMplsLspExcludeNodeAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_VRtrMplsLspExcludeNodeAddr_Type.__name__=_O
_VRtrMplsLspExcludeNodeAddr_Object=MibTableColumn
vRtrMplsLspExcludeNodeAddr=_VRtrMplsLspExcludeNodeAddr_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,59),_VRtrMplsLspExcludeNodeAddr_Type())
vRtrMplsLspExcludeNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspExcludeNodeAddr.setStatus(_A)
class _VRtrMplsLspIgpShortcutLfaType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_R,0),('lfaProtect',1),('lfaOnly',2)))
_VRtrMplsLspIgpShortcutLfaType_Type.__name__=_H
_VRtrMplsLspIgpShortcutLfaType_Object=MibTableColumn
vRtrMplsLspIgpShortcutLfaType=_VRtrMplsLspIgpShortcutLfaType_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,60),_VRtrMplsLspIgpShortcutLfaType_Type())
vRtrMplsLspIgpShortcutLfaType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspIgpShortcutLfaType.setStatus(_A)
class _VRtrMplsLspToAddrType_Type(TmnxMplsLspAddrType):defaultValue=1
_VRtrMplsLspToAddrType_Type.__name__=_S
_VRtrMplsLspToAddrType_Object=MibTableColumn
vRtrMplsLspToAddrType=_VRtrMplsLspToAddrType_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,61),_VRtrMplsLspToAddrType_Type())
vRtrMplsLspToAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspToAddrType.setStatus(_A)
class _VRtrMplsLspFromAddrType_Type(TmnxMplsLspAddrType):defaultValue=1
_VRtrMplsLspFromAddrType_Type.__name__=_S
_VRtrMplsLspFromAddrType_Object=MibTableColumn
vRtrMplsLspFromAddrType=_VRtrMplsLspFromAddrType_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,62),_VRtrMplsLspFromAddrType_Type())
vRtrMplsLspFromAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFromAddrType.setStatus(_A)
class _VRtrMplsLspToNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_VRtrMplsLspToNodeId_Type.__name__=_Q
_VRtrMplsLspToNodeId_Object=MibTableColumn
vRtrMplsLspToNodeId=_VRtrMplsLspToNodeId_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,63),_VRtrMplsLspToNodeId_Type())
vRtrMplsLspToNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspToNodeId.setStatus(_A)
class _VRtrMplsLspFromNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_VRtrMplsLspFromNodeId_Type.__name__=_Q
_VRtrMplsLspFromNodeId_Object=MibTableColumn
vRtrMplsLspFromNodeId=_VRtrMplsLspFromNodeId_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,64),_VRtrMplsLspFromNodeId_Type())
vRtrMplsLspFromNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspFromNodeId.setStatus(_A)
class _VRtrMplsLspDestGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_VRtrMplsLspDestGlobalId_Type.__name__=_U
_VRtrMplsLspDestGlobalId_Object=MibTableColumn
vRtrMplsLspDestGlobalId=_VRtrMplsLspDestGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,65),_VRtrMplsLspDestGlobalId_Type())
vRtrMplsLspDestGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspDestGlobalId.setStatus(_A)
class _VRtrMplsLspDestTunnelNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,61440))
_VRtrMplsLspDestTunnelNum_Type.__name__=_D
_VRtrMplsLspDestTunnelNum_Object=MibTableColumn
vRtrMplsLspDestTunnelNum=_VRtrMplsLspDestTunnelNum_Object((1,3,6,1,4,1,7483,6,1,2,6,1,1,66),_VRtrMplsLspDestTunnelNum_Type())
vRtrMplsLspDestTunnelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspDestTunnelNum.setStatus(_A)
_VRtrMplsLspStatTable_Object=MibTable
vRtrMplsLspStatTable=_VRtrMplsLspStatTable_Object((1,3,6,1,4,1,7483,6,1,2,6,2))
if mibBuilder.loadTexts:vRtrMplsLspStatTable.setStatus(_A)
_VRtrMplsLspStatEntry_Object=MibTableRow
vRtrMplsLspStatEntry=_VRtrMplsLspStatEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1))
if mibBuilder.loadTexts:vRtrMplsLspStatEntry.setStatus(_A)
_VRtrMplsLspOctets_Type=Counter64
_VRtrMplsLspOctets_Object=MibTableColumn
vRtrMplsLspOctets=_VRtrMplsLspOctets_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,1),_VRtrMplsLspOctets_Type())
vRtrMplsLspOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspOctets.setStatus(_A)
_VRtrMplsLspPackets_Type=Counter64
_VRtrMplsLspPackets_Object=MibTableColumn
vRtrMplsLspPackets=_VRtrMplsLspPackets_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,2),_VRtrMplsLspPackets_Type())
vRtrMplsLspPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspPackets.setStatus(_A)
_VRtrMplsLspAge_Type=TimeInterval
_VRtrMplsLspAge_Object=MibTableColumn
vRtrMplsLspAge=_VRtrMplsLspAge_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,3),_VRtrMplsLspAge_Type())
vRtrMplsLspAge.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspAge.setStatus(_A)
_VRtrMplsLspTimeUp_Type=TimeInterval
_VRtrMplsLspTimeUp_Object=MibTableColumn
vRtrMplsLspTimeUp=_VRtrMplsLspTimeUp_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,4),_VRtrMplsLspTimeUp_Type())
vRtrMplsLspTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspTimeUp.setStatus(_A)
_VRtrMplsLspTimeDown_Type=TimeInterval
_VRtrMplsLspTimeDown_Object=MibTableColumn
vRtrMplsLspTimeDown=_VRtrMplsLspTimeDown_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,5),_VRtrMplsLspTimeDown_Type())
vRtrMplsLspTimeDown.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspTimeDown.setStatus(_A)
_VRtrMplsLspPrimaryTimeUp_Type=TimeInterval
_VRtrMplsLspPrimaryTimeUp_Object=MibTableColumn
vRtrMplsLspPrimaryTimeUp=_VRtrMplsLspPrimaryTimeUp_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,6),_VRtrMplsLspPrimaryTimeUp_Type())
vRtrMplsLspPrimaryTimeUp.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspPrimaryTimeUp.setStatus(_A)
_VRtrMplsLspTransitions_Type=Counter32
_VRtrMplsLspTransitions_Object=MibTableColumn
vRtrMplsLspTransitions=_VRtrMplsLspTransitions_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,7),_VRtrMplsLspTransitions_Type())
vRtrMplsLspTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspTransitions.setStatus(_A)
_VRtrMplsLspLastTransition_Type=TimeInterval
_VRtrMplsLspLastTransition_Object=MibTableColumn
vRtrMplsLspLastTransition=_VRtrMplsLspLastTransition_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,8),_VRtrMplsLspLastTransition_Type())
vRtrMplsLspLastTransition.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspLastTransition.setStatus(_A)
_VRtrMplsLspPathChanges_Type=Counter32
_VRtrMplsLspPathChanges_Object=MibTableColumn
vRtrMplsLspPathChanges=_VRtrMplsLspPathChanges_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,9),_VRtrMplsLspPathChanges_Type())
vRtrMplsLspPathChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspPathChanges.setStatus(_A)
_VRtrMplsLspLastPathChange_Type=TimeInterval
_VRtrMplsLspLastPathChange_Object=MibTableColumn
vRtrMplsLspLastPathChange=_VRtrMplsLspLastPathChange_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,10),_VRtrMplsLspLastPathChange_Type())
vRtrMplsLspLastPathChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspLastPathChange.setStatus(_A)
_VRtrMplsLspConfiguredPaths_Type=Integer32
_VRtrMplsLspConfiguredPaths_Object=MibTableColumn
vRtrMplsLspConfiguredPaths=_VRtrMplsLspConfiguredPaths_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,11),_VRtrMplsLspConfiguredPaths_Type())
vRtrMplsLspConfiguredPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspConfiguredPaths.setStatus(_A)
_VRtrMplsLspStandbyPaths_Type=Integer32
_VRtrMplsLspStandbyPaths_Object=MibTableColumn
vRtrMplsLspStandbyPaths=_VRtrMplsLspStandbyPaths_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,12),_VRtrMplsLspStandbyPaths_Type())
vRtrMplsLspStandbyPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspStandbyPaths.setStatus(_A)
_VRtrMplsLspOperationalPaths_Type=Integer32
_VRtrMplsLspOperationalPaths_Object=MibTableColumn
vRtrMplsLspOperationalPaths=_VRtrMplsLspOperationalPaths_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,13),_VRtrMplsLspOperationalPaths_Type())
vRtrMplsLspOperationalPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspOperationalPaths.setStatus(_A)
_VRtrMplsLspConfP2mpInstances_Type=Gauge32
_VRtrMplsLspConfP2mpInstances_Object=MibTableColumn
vRtrMplsLspConfP2mpInstances=_VRtrMplsLspConfP2mpInstances_Object((1,3,6,1,4,1,7483,6,1,2,6,2,1,14),_VRtrMplsLspConfP2mpInstances_Type())
vRtrMplsLspConfP2mpInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspConfP2mpInstances.setStatus(_A)
_VRtrMplsGeneralTable_Object=MibTable
vRtrMplsGeneralTable=_VRtrMplsGeneralTable_Object((1,3,6,1,4,1,7483,6,1,2,6,7))
if mibBuilder.loadTexts:vRtrMplsGeneralTable.setStatus(_A)
_VRtrMplsGeneralEntry_Object=MibTableRow
vRtrMplsGeneralEntry=_VRtrMplsGeneralEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1))
vRtrMplsGeneralEntry.setIndexNames((0,_J,_K),(0,_G,_I))
if mibBuilder.loadTexts:vRtrMplsGeneralEntry.setStatus(_A)
_VRtrMplsGeneralLastChange_Type=TimeStamp
_VRtrMplsGeneralLastChange_Object=MibTableColumn
vRtrMplsGeneralLastChange=_VRtrMplsGeneralLastChange_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,1),_VRtrMplsGeneralLastChange_Type())
vRtrMplsGeneralLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsGeneralLastChange.setStatus(_A)
class _VRtrMplsGeneralAdminState_Type(TmnxAdminState):defaultValue=2
_VRtrMplsGeneralAdminState_Type.__name__=_N
_VRtrMplsGeneralAdminState_Object=MibTableColumn
vRtrMplsGeneralAdminState=_VRtrMplsGeneralAdminState_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,2),_VRtrMplsGeneralAdminState_Type())
vRtrMplsGeneralAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralAdminState.setStatus(_A)
_VRtrMplsGeneralOperState_Type=TmnxOperState
_VRtrMplsGeneralOperState_Object=MibTableColumn
vRtrMplsGeneralOperState=_VRtrMplsGeneralOperState_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,3),_VRtrMplsGeneralOperState_Type())
vRtrMplsGeneralOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsGeneralOperState.setStatus(_A)
class _VRtrMplsGeneralPropagateTtl_Type(TruthValue):defaultValue=1
_VRtrMplsGeneralPropagateTtl_Type.__name__=_E
_VRtrMplsGeneralPropagateTtl_Object=MibTableColumn
vRtrMplsGeneralPropagateTtl=_VRtrMplsGeneralPropagateTtl_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,4),_VRtrMplsGeneralPropagateTtl_Type())
vRtrMplsGeneralPropagateTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralPropagateTtl.setStatus(_A)
class _VRtrMplsGeneralTE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('bgp',2),('bgpigp',3)))
_VRtrMplsGeneralTE_Type.__name__=_H
_VRtrMplsGeneralTE_Object=MibTableColumn
vRtrMplsGeneralTE=_VRtrMplsGeneralTE_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,5),_VRtrMplsGeneralTE_Type())
vRtrMplsGeneralTE.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralTE.setStatus(_A)
_VRtrMplsGeneralNewLspIndex_Type=TestAndIncr
_VRtrMplsGeneralNewLspIndex_Object=MibTableColumn
vRtrMplsGeneralNewLspIndex=_VRtrMplsGeneralNewLspIndex_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,6),_VRtrMplsGeneralNewLspIndex_Type())
vRtrMplsGeneralNewLspIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralNewLspIndex.setStatus(_A)
class _VRtrMplsGeneralOptimizeTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrMplsGeneralOptimizeTimer_Type.__name__=_D
_VRtrMplsGeneralOptimizeTimer_Object=MibTableColumn
vRtrMplsGeneralOptimizeTimer=_VRtrMplsGeneralOptimizeTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,7),_VRtrMplsGeneralOptimizeTimer_Type())
vRtrMplsGeneralOptimizeTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralOptimizeTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGeneralOptimizeTimer.setUnits(_L)
class _VRtrMplsGeneralFRObject_Type(TruthValue):defaultValue=1
_VRtrMplsGeneralFRObject_Type.__name__=_E
_VRtrMplsGeneralFRObject_Object=MibTableColumn
vRtrMplsGeneralFRObject=_VRtrMplsGeneralFRObject_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,8),_VRtrMplsGeneralFRObject_Type())
vRtrMplsGeneralFRObject.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralFRObject.setStatus(_A)
class _VRtrMplsGeneralResignalTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,10080))
_VRtrMplsGeneralResignalTimer_Type.__name__=_D
_VRtrMplsGeneralResignalTimer_Object=MibTableColumn
vRtrMplsGeneralResignalTimer=_VRtrMplsGeneralResignalTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,9),_VRtrMplsGeneralResignalTimer_Type())
vRtrMplsGeneralResignalTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralResignalTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGeneralResignalTimer.setUnits(_c)
class _VRtrMplsGeneralHoldTimer_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_VRtrMplsGeneralHoldTimer_Type.__name__=_D
_VRtrMplsGeneralHoldTimer_Object=MibTableColumn
vRtrMplsGeneralHoldTimer=_VRtrMplsGeneralHoldTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,10),_VRtrMplsGeneralHoldTimer_Type())
vRtrMplsGeneralHoldTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGeneralHoldTimer.setUnits(_L)
class _VRtrMplsGeneralDynamicBypass_Type(TruthValue):defaultValue=1
_VRtrMplsGeneralDynamicBypass_Type.__name__=_E
_VRtrMplsGeneralDynamicBypass_Object=MibTableColumn
vRtrMplsGeneralDynamicBypass=_VRtrMplsGeneralDynamicBypass_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,11),_VRtrMplsGeneralDynamicBypass_Type())
vRtrMplsGeneralDynamicBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralDynamicBypass.setStatus(_A)
_VRtrMplsGeneralNextResignal_Type=Unsigned32
_VRtrMplsGeneralNextResignal_Object=MibTableColumn
vRtrMplsGeneralNextResignal=_VRtrMplsGeneralNextResignal_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,12),_VRtrMplsGeneralNextResignal_Type())
vRtrMplsGeneralNextResignal.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsGeneralNextResignal.setStatus(_A)
_VRtrMplsGeneralOperDownReason_Type=TmnxMplsOperDownReasonCode
_VRtrMplsGeneralOperDownReason_Object=MibTableColumn
vRtrMplsGeneralOperDownReason=_VRtrMplsGeneralOperDownReason_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,13),_VRtrMplsGeneralOperDownReason_Type())
vRtrMplsGeneralOperDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsGeneralOperDownReason.setStatus(_A)
class _VRtrMplsGeneralSrlgFrr_Type(TruthValue):defaultValue=2
_VRtrMplsGeneralSrlgFrr_Type.__name__=_E
_VRtrMplsGeneralSrlgFrr_Object=MibTableColumn
vRtrMplsGeneralSrlgFrr=_VRtrMplsGeneralSrlgFrr_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,14),_VRtrMplsGeneralSrlgFrr_Type())
vRtrMplsGeneralSrlgFrr.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralSrlgFrr.setStatus(_A)
class _VRtrMplsGeneralSrlgFrrStrict_Type(TruthValue):defaultValue=2
_VRtrMplsGeneralSrlgFrrStrict_Type.__name__=_E
_VRtrMplsGeneralSrlgFrrStrict_Object=MibTableColumn
vRtrMplsGeneralSrlgFrrStrict=_VRtrMplsGeneralSrlgFrrStrict_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,15),_VRtrMplsGeneralSrlgFrrStrict_Type())
vRtrMplsGeneralSrlgFrrStrict.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralSrlgFrrStrict.setStatus(_A)
_VRtrMplsGeneralNewP2mpInstIndex_Type=TestAndIncr
_VRtrMplsGeneralNewP2mpInstIndex_Object=MibTableColumn
vRtrMplsGeneralNewP2mpInstIndex=_VRtrMplsGeneralNewP2mpInstIndex_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,16),_VRtrMplsGeneralNewP2mpInstIndex_Type())
vRtrMplsGeneralNewP2mpInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralNewP2mpInstIndex.setStatus(_A)
class _VRtrMplsGeneralLeastFillMinThd_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VRtrMplsGeneralLeastFillMinThd_Type.__name__=_D
_VRtrMplsGeneralLeastFillMinThd_Object=MibTableColumn
vRtrMplsGeneralLeastFillMinThd=_VRtrMplsGeneralLeastFillMinThd_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,17),_VRtrMplsGeneralLeastFillMinThd_Type())
vRtrMplsGeneralLeastFillMinThd.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralLeastFillMinThd.setStatus(_A)
class _VRtrMplsGenLeastFillReoptiThd_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VRtrMplsGenLeastFillReoptiThd_Type.__name__=_D
_VRtrMplsGenLeastFillReoptiThd_Object=MibTableColumn
vRtrMplsGenLeastFillReoptiThd=_VRtrMplsGenLeastFillReoptiThd_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,18),_VRtrMplsGenLeastFillReoptiThd_Type())
vRtrMplsGenLeastFillReoptiThd.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGenLeastFillReoptiThd.setStatus(_A)
class _VRtrMplsGeneralUseSrlgDB_Type(TruthValue):defaultValue=2
_VRtrMplsGeneralUseSrlgDB_Type.__name__=_E
_VRtrMplsGeneralUseSrlgDB_Object=MibTableColumn
vRtrMplsGeneralUseSrlgDB=_VRtrMplsGeneralUseSrlgDB_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,19),_VRtrMplsGeneralUseSrlgDB_Type())
vRtrMplsGeneralUseSrlgDB.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralUseSrlgDB.setStatus(_A)
class _VRtrMplsGeneralP2mpResigTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,10080))
_VRtrMplsGeneralP2mpResigTimer_Type.__name__=_D
_VRtrMplsGeneralP2mpResigTimer_Object=MibTableColumn
vRtrMplsGeneralP2mpResigTimer=_VRtrMplsGeneralP2mpResigTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,20),_VRtrMplsGeneralP2mpResigTimer_Type())
vRtrMplsGeneralP2mpResigTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralP2mpResigTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGeneralP2mpResigTimer.setUnits(_c)
_VRtrMplsGeneralP2mpNextResignal_Type=Unsigned32
_VRtrMplsGeneralP2mpNextResignal_Object=MibTableColumn
vRtrMplsGeneralP2mpNextResignal=_VRtrMplsGeneralP2mpNextResignal_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,21),_VRtrMplsGeneralP2mpNextResignal_Type())
vRtrMplsGeneralP2mpNextResignal.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsGeneralP2mpNextResignal.setStatus(_A)
class _VRtrMplsGeneralSecFastRetryTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_VRtrMplsGeneralSecFastRetryTimer_Type.__name__=_D
_VRtrMplsGeneralSecFastRetryTimer_Object=MibTableColumn
vRtrMplsGeneralSecFastRetryTimer=_VRtrMplsGeneralSecFastRetryTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,22),_VRtrMplsGeneralSecFastRetryTimer_Type())
vRtrMplsGeneralSecFastRetryTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralSecFastRetryTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGeneralSecFastRetryTimer.setUnits(_L)
class _VRtrMplsGeneralShortTTLPropLocal_Type(TruthValue):defaultValue=1
_VRtrMplsGeneralShortTTLPropLocal_Type.__name__=_E
_VRtrMplsGeneralShortTTLPropLocal_Object=MibTableColumn
vRtrMplsGeneralShortTTLPropLocal=_VRtrMplsGeneralShortTTLPropLocal_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,23),_VRtrMplsGeneralShortTTLPropLocal_Type())
vRtrMplsGeneralShortTTLPropLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralShortTTLPropLocal.setStatus(_A)
class _VRtrMplsGeneralShortTTLPropTrans_Type(TruthValue):defaultValue=1
_VRtrMplsGeneralShortTTLPropTrans_Type.__name__=_E
_VRtrMplsGeneralShortTTLPropTrans_Object=MibTableColumn
vRtrMplsGeneralShortTTLPropTrans=_VRtrMplsGeneralShortTTLPropTrans_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,24),_VRtrMplsGeneralShortTTLPropTrans_Type())
vRtrMplsGeneralShortTTLPropTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralShortTTLPropTrans.setStatus(_A)
class _VRtrMplsGeneralStaticLspFRTimer_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_VRtrMplsGeneralStaticLspFRTimer_Type.__name__=_D
_VRtrMplsGeneralStaticLspFRTimer_Object=MibTableColumn
vRtrMplsGeneralStaticLspFRTimer=_VRtrMplsGeneralStaticLspFRTimer_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,25),_VRtrMplsGeneralStaticLspFRTimer_Type())
vRtrMplsGeneralStaticLspFRTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralStaticLspFRTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGeneralStaticLspFRTimer.setUnits(_L)
class _VRtrMplsGeneralAutoBWDefSampMul_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,511))
_VRtrMplsGeneralAutoBWDefSampMul_Type.__name__=_D
_VRtrMplsGeneralAutoBWDefSampMul_Object=MibTableColumn
vRtrMplsGeneralAutoBWDefSampMul=_VRtrMplsGeneralAutoBWDefSampMul_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,26),_VRtrMplsGeneralAutoBWDefSampMul_Type())
vRtrMplsGeneralAutoBWDefSampMul.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralAutoBWDefSampMul.setStatus(_A)
class _VRtrMplsGeneralAutoBWDefAdjMul_Type(Unsigned32):defaultValue=288;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_VRtrMplsGeneralAutoBWDefAdjMul_Type.__name__=_D
_VRtrMplsGeneralAutoBWDefAdjMul_Object=MibTableColumn
vRtrMplsGeneralAutoBWDefAdjMul=_VRtrMplsGeneralAutoBWDefAdjMul_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,27),_VRtrMplsGeneralAutoBWDefAdjMul_Type())
vRtrMplsGeneralAutoBWDefAdjMul.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralAutoBWDefAdjMul.setStatus(_A)
class _VRtrMplsGeneralExpBackoffRetry_Type(TruthValue):defaultValue=2
_VRtrMplsGeneralExpBackoffRetry_Type.__name__=_E
_VRtrMplsGeneralExpBackoffRetry_Object=MibTableColumn
vRtrMplsGeneralExpBackoffRetry=_VRtrMplsGeneralExpBackoffRetry_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,28),_VRtrMplsGeneralExpBackoffRetry_Type())
vRtrMplsGeneralExpBackoffRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralExpBackoffRetry.setStatus(_A)
class _VRtrMplsGeneralCspfOnLooseHop_Type(TruthValue):defaultValue=2
_VRtrMplsGeneralCspfOnLooseHop_Type.__name__=_E
_VRtrMplsGeneralCspfOnLooseHop_Object=MibTableColumn
vRtrMplsGeneralCspfOnLooseHop=_VRtrMplsGeneralCspfOnLooseHop_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,29),_VRtrMplsGeneralCspfOnLooseHop_Type())
vRtrMplsGeneralCspfOnLooseHop.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralCspfOnLooseHop.setStatus(_A)
class _VRtrMplsGeneralP2PMaxByPassAssoc_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,131072))
_VRtrMplsGeneralP2PMaxByPassAssoc_Type.__name__=_D
_VRtrMplsGeneralP2PMaxByPassAssoc_Object=MibTableColumn
vRtrMplsGeneralP2PMaxByPassAssoc=_VRtrMplsGeneralP2PMaxByPassAssoc_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,30),_VRtrMplsGeneralP2PMaxByPassAssoc_Type())
vRtrMplsGeneralP2PMaxByPassAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGeneralP2PMaxByPassAssoc.setStatus(_A)
class _VRtrMplsGenP2pActPathFastRetry_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_VRtrMplsGenP2pActPathFastRetry_Type.__name__=_D
_VRtrMplsGenP2pActPathFastRetry_Object=MibTableColumn
vRtrMplsGenP2pActPathFastRetry=_VRtrMplsGenP2pActPathFastRetry_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,31),_VRtrMplsGenP2pActPathFastRetry_Type())
vRtrMplsGenP2pActPathFastRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGenP2pActPathFastRetry.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGenP2pActPathFastRetry.setUnits(_L)
class _VRtrMplsGenP2mpS2lFastRetry_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_VRtrMplsGenP2mpS2lFastRetry_Type.__name__=_D
_VRtrMplsGenP2mpS2lFastRetry_Object=MibTableColumn
vRtrMplsGenP2mpS2lFastRetry=_VRtrMplsGenP2mpS2lFastRetry_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,32),_VRtrMplsGenP2mpS2lFastRetry_Type())
vRtrMplsGenP2mpS2lFastRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGenP2mpS2lFastRetry.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGenP2mpS2lFastRetry.setUnits(_L)
class _VRtrMplsGenLspInitRetryTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_VRtrMplsGenLspInitRetryTimeout_Type.__name__=_D
_VRtrMplsGenLspInitRetryTimeout_Object=MibTableColumn
vRtrMplsGenLspInitRetryTimeout=_VRtrMplsGenLspInitRetryTimeout_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,33),_VRtrMplsGenLspInitRetryTimeout_Type())
vRtrMplsGenLspInitRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsGenLspInitRetryTimeout.setStatus(_A)
if mibBuilder.loadTexts:vRtrMplsGenLspInitRetryTimeout.setUnits(_L)
class _VRtrMplsLoggerEventBundling_Type(TruthValue):defaultValue=2
_VRtrMplsLoggerEventBundling_Type.__name__=_E
_VRtrMplsLoggerEventBundling_Object=MibTableColumn
vRtrMplsLoggerEventBundling=_VRtrMplsLoggerEventBundling_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,34),_VRtrMplsLoggerEventBundling_Type())
vRtrMplsLoggerEventBundling.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLoggerEventBundling.setStatus(_A)
_VRtrMplsGenIssuMplsLockdown_Type=TruthValue
_VRtrMplsGenIssuMplsLockdown_Object=MibTableColumn
vRtrMplsGenIssuMplsLockdown=_VRtrMplsGenIssuMplsLockdown_Object((1,3,6,1,4,1,7483,6,1,2,6,7,1,39),_VRtrMplsGenIssuMplsLockdown_Type())
vRtrMplsGenIssuMplsLockdown.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsGenIssuMplsLockdown.setStatus(_A)
_VRtrMplsIfTable_Object=MibTable
vRtrMplsIfTable=_VRtrMplsIfTable_Object((1,3,6,1,4,1,7483,6,1,2,6,9))
if mibBuilder.loadTexts:vRtrMplsIfTable.setStatus(_A)
_VRtrMplsIfEntry_Object=MibTableRow
vRtrMplsIfEntry=_VRtrMplsIfEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,9,1))
vRtrMplsIfEntry.setIndexNames((0,_J,_K),(0,_G,_I),(0,_G,_W))
if mibBuilder.loadTexts:vRtrMplsIfEntry.setStatus(_A)
class _VRtrMplsIfAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsIfAdminState_Type.__name__=_N
_VRtrMplsIfAdminState_Object=MibTableColumn
vRtrMplsIfAdminState=_VRtrMplsIfAdminState_Object((1,3,6,1,4,1,7483,6,1,2,6,9,1,1),_VRtrMplsIfAdminState_Type())
vRtrMplsIfAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsIfAdminState.setStatus(_A)
_VRtrMplsIfOperState_Type=TmnxOperState
_VRtrMplsIfOperState_Object=MibTableColumn
vRtrMplsIfOperState=_VRtrMplsIfOperState_Object((1,3,6,1,4,1,7483,6,1,2,6,9,1,2),_VRtrMplsIfOperState_Type())
vRtrMplsIfOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsIfOperState.setStatus(_A)
class _VRtrMplsIfAdminGroup_Type(Unsigned32):defaultValue=0
_VRtrMplsIfAdminGroup_Type.__name__=_D
_VRtrMplsIfAdminGroup_Object=MibTableColumn
vRtrMplsIfAdminGroup=_VRtrMplsIfAdminGroup_Object((1,3,6,1,4,1,7483,6,1,2,6,9,1,3),_VRtrMplsIfAdminGroup_Type())
vRtrMplsIfAdminGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsIfAdminGroup.setStatus(_A)
class _VRtrMplsIfTeMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777215))
_VRtrMplsIfTeMetric_Type.__name__=_D
_VRtrMplsIfTeMetric_Object=MibTableColumn
vRtrMplsIfTeMetric=_VRtrMplsIfTeMetric_Object((1,3,6,1,4,1,7483,6,1,2,6,9,1,4),_VRtrMplsIfTeMetric_Type())
vRtrMplsIfTeMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsIfTeMetric.setStatus(_A)
_VRtrMplsIfStatTable_Object=MibTable
vRtrMplsIfStatTable=_VRtrMplsIfStatTable_Object((1,3,6,1,4,1,7483,6,1,2,6,10))
if mibBuilder.loadTexts:vRtrMplsIfStatTable.setStatus(_A)
_VRtrMplsIfStatEntry_Object=MibTableRow
vRtrMplsIfStatEntry=_VRtrMplsIfStatEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,10,1))
if mibBuilder.loadTexts:vRtrMplsIfStatEntry.setStatus(_A)
_VRtrMplsIfTxPktCount_Type=Counter64
_VRtrMplsIfTxPktCount_Object=MibTableColumn
vRtrMplsIfTxPktCount=_VRtrMplsIfTxPktCount_Object((1,3,6,1,4,1,7483,6,1,2,6,10,1,1),_VRtrMplsIfTxPktCount_Type())
vRtrMplsIfTxPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsIfTxPktCount.setStatus(_A)
_VRtrMplsIfRxPktCount_Type=Counter64
_VRtrMplsIfRxPktCount_Object=MibTableColumn
vRtrMplsIfRxPktCount=_VRtrMplsIfRxPktCount_Object((1,3,6,1,4,1,7483,6,1,2,6,10,1,2),_VRtrMplsIfRxPktCount_Type())
vRtrMplsIfRxPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsIfRxPktCount.setStatus(_A)
_VRtrMplsIfTxOctetCount_Type=Counter64
_VRtrMplsIfTxOctetCount_Object=MibTableColumn
vRtrMplsIfTxOctetCount=_VRtrMplsIfTxOctetCount_Object((1,3,6,1,4,1,7483,6,1,2,6,10,1,3),_VRtrMplsIfTxOctetCount_Type())
vRtrMplsIfTxOctetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsIfTxOctetCount.setStatus(_A)
_VRtrMplsIfRxOctetCount_Type=Counter64
_VRtrMplsIfRxOctetCount_Object=MibTableColumn
vRtrMplsIfRxOctetCount=_VRtrMplsIfRxOctetCount_Object((1,3,6,1,4,1,7483,6,1,2,6,10,1,4),_VRtrMplsIfRxOctetCount_Type())
vRtrMplsIfRxOctetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsIfRxOctetCount.setStatus(_A)
_VRtrMplsLabelRangeTable_Object=MibTable
vRtrMplsLabelRangeTable=_VRtrMplsLabelRangeTable_Object((1,3,6,1,4,1,7483,6,1,2,6,17))
if mibBuilder.loadTexts:vRtrMplsLabelRangeTable.setStatus(_A)
_VRtrMplsLabelRangeEntry_Object=MibTableRow
vRtrMplsLabelRangeEntry=_VRtrMplsLabelRangeEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,17,1))
vRtrMplsLabelRangeEntry.setIndexNames((0,_J,_K),(0,_G,_I),(0,_F,_d))
if mibBuilder.loadTexts:vRtrMplsLabelRangeEntry.setStatus(_A)
class _VRtrMplsLabelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('staticLsp',1),('staticSvc',2),(_Z,3)))
_VRtrMplsLabelType_Type.__name__=_H
_VRtrMplsLabelType_Object=MibTableColumn
vRtrMplsLabelType=_VRtrMplsLabelType_Object((1,3,6,1,4,1,7483,6,1,2,6,17,1,1),_VRtrMplsLabelType_Type())
vRtrMplsLabelType.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsLabelType.setStatus(_A)
_VRtrMplsLabelRangeMin_Type=Unsigned32
_VRtrMplsLabelRangeMin_Object=MibTableColumn
vRtrMplsLabelRangeMin=_VRtrMplsLabelRangeMin_Object((1,3,6,1,4,1,7483,6,1,2,6,17,1,2),_VRtrMplsLabelRangeMin_Type())
vRtrMplsLabelRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLabelRangeMin.setStatus(_A)
_VRtrMplsLabelRangeMax_Type=Unsigned32
_VRtrMplsLabelRangeMax_Object=MibTableColumn
vRtrMplsLabelRangeMax=_VRtrMplsLabelRangeMax_Object((1,3,6,1,4,1,7483,6,1,2,6,17,1,3),_VRtrMplsLabelRangeMax_Type())
vRtrMplsLabelRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLabelRangeMax.setStatus(_A)
_VRtrMplsLabelRangeAging_Type=Unsigned32
_VRtrMplsLabelRangeAging_Object=MibTableColumn
vRtrMplsLabelRangeAging=_VRtrMplsLabelRangeAging_Object((1,3,6,1,4,1,7483,6,1,2,6,17,1,4),_VRtrMplsLabelRangeAging_Type())
vRtrMplsLabelRangeAging.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLabelRangeAging.setStatus(_A)
_VRtrMplsLabelRangeAvailable_Type=Unsigned32
_VRtrMplsLabelRangeAvailable_Object=MibTableColumn
vRtrMplsLabelRangeAvailable=_VRtrMplsLabelRangeAvailable_Object((1,3,6,1,4,1,7483,6,1,2,6,17,1,5),_VRtrMplsLabelRangeAvailable_Type())
vRtrMplsLabelRangeAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLabelRangeAvailable.setStatus(_A)
_VRtrMplsStaticLSPLabelTable_Object=MibTable
vRtrMplsStaticLSPLabelTable=_VRtrMplsStaticLSPLabelTable_Object((1,3,6,1,4,1,7483,6,1,2,6,18))
if mibBuilder.loadTexts:vRtrMplsStaticLSPLabelTable.setStatus(_A)
_VRtrMplsStaticLSPLabelEntry_Object=MibTableRow
vRtrMplsStaticLSPLabelEntry=_VRtrMplsStaticLSPLabelEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,18,1))
vRtrMplsStaticLSPLabelEntry.setIndexNames((0,_J,_K),(0,_G,_I),(0,_F,_e))
if mibBuilder.loadTexts:vRtrMplsStaticLSPLabelEntry.setStatus(_A)
class _VRtrMplsStaticLSPLabel_Type(MplsLabel):subtypeSpec=MplsLabel.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,262112))
_VRtrMplsStaticLSPLabel_Type.__name__=_P
_VRtrMplsStaticLSPLabel_Object=MibTableColumn
vRtrMplsStaticLSPLabel=_VRtrMplsStaticLSPLabel_Object((1,3,6,1,4,1,7483,6,1,2,6,18,1,1),_VRtrMplsStaticLSPLabel_Type())
vRtrMplsStaticLSPLabel.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsStaticLSPLabel.setStatus(_A)
_VRtrMplsStaticLSPLabelOwner_Type=TmnxMplsLabelOwner
_VRtrMplsStaticLSPLabelOwner_Object=MibTableColumn
vRtrMplsStaticLSPLabelOwner=_VRtrMplsStaticLSPLabelOwner_Object((1,3,6,1,4,1,7483,6,1,2,6,18,1,2),_VRtrMplsStaticLSPLabelOwner_Type())
vRtrMplsStaticLSPLabelOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsStaticLSPLabelOwner.setStatus(_A)
_VRtrMplsStaticSvcLabelTable_Object=MibTable
vRtrMplsStaticSvcLabelTable=_VRtrMplsStaticSvcLabelTable_Object((1,3,6,1,4,1,7483,6,1,2,6,19))
if mibBuilder.loadTexts:vRtrMplsStaticSvcLabelTable.setStatus(_A)
_VRtrMplsStaticSvcLabelEntry_Object=MibTableRow
vRtrMplsStaticSvcLabelEntry=_VRtrMplsStaticSvcLabelEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,19,1))
vRtrMplsStaticSvcLabelEntry.setIndexNames((0,_J,_K),(0,_G,_I),(0,_F,_f))
if mibBuilder.loadTexts:vRtrMplsStaticSvcLabelEntry.setStatus(_A)
class _VRtrMplsStaticSvcLabel_Type(MplsLabel):subtypeSpec=MplsLabel.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,262112))
_VRtrMplsStaticSvcLabel_Type.__name__=_P
_VRtrMplsStaticSvcLabel_Object=MibTableColumn
vRtrMplsStaticSvcLabel=_VRtrMplsStaticSvcLabel_Object((1,3,6,1,4,1,7483,6,1,2,6,19,1,1),_VRtrMplsStaticSvcLabel_Type())
vRtrMplsStaticSvcLabel.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsStaticSvcLabel.setStatus(_A)
class _VRtrMplsStaticSvcLabelOwner_Type(TmnxMplsLabelOwner):defaultValue=0
_VRtrMplsStaticSvcLabelOwner_Type.__name__=_g
_VRtrMplsStaticSvcLabelOwner_Object=MibTableColumn
vRtrMplsStaticSvcLabelOwner=_VRtrMplsStaticSvcLabelOwner_Object((1,3,6,1,4,1,7483,6,1,2,6,19,1,2),_VRtrMplsStaticSvcLabelOwner_Type())
vRtrMplsStaticSvcLabelOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsStaticSvcLabelOwner.setStatus(_A)
_VRtrMplsLspStatsTblLastChgd_Type=TimeStamp
_VRtrMplsLspStatsTblLastChgd_Object=MibScalar
vRtrMplsLspStatsTblLastChgd=_VRtrMplsLspStatsTblLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,6,37),_VRtrMplsLspStatsTblLastChgd_Type())
vRtrMplsLspStatsTblLastChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspStatsTblLastChgd.setStatus(_A)
_VRtrMplsLspStatsTable_Object=MibTable
vRtrMplsLspStatsTable=_VRtrMplsLspStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,6,38))
if mibBuilder.loadTexts:vRtrMplsLspStatsTable.setStatus(_A)
_VRtrMplsLspStatsEntry_Object=MibTableRow
vRtrMplsLspStatsEntry=_VRtrMplsLspStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1))
vRtrMplsLspStatsEntry.setIndexNames((0,_J,_K),(0,_G,_I),(0,_F,_h),(0,_F,_i),(0,_F,_j),(0,_F,_k))
if mibBuilder.loadTexts:vRtrMplsLspStatsEntry.setStatus(_A)
class _VRtrMplsLspStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('egress',0),('ingress',1)))
_VRtrMplsLspStatsType_Type.__name__=_H
_VRtrMplsLspStatsType_Object=MibTableColumn
vRtrMplsLspStatsType=_VRtrMplsLspStatsType_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,1),_VRtrMplsLspStatsType_Type())
vRtrMplsLspStatsType.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsLspStatsType.setStatus(_A)
_VRtrMplsLspStatsSenderAddrType_Type=InetAddressType
_VRtrMplsLspStatsSenderAddrType_Object=MibTableColumn
vRtrMplsLspStatsSenderAddrType=_VRtrMplsLspStatsSenderAddrType_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,2),_VRtrMplsLspStatsSenderAddrType_Type())
vRtrMplsLspStatsSenderAddrType.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsLspStatsSenderAddrType.setStatus(_A)
class _VRtrMplsLspStatsSenderAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrMplsLspStatsSenderAddr_Type.__name__=_O
_VRtrMplsLspStatsSenderAddr_Object=MibTableColumn
vRtrMplsLspStatsSenderAddr=_VRtrMplsLspStatsSenderAddr_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,3),_VRtrMplsLspStatsSenderAddr_Type())
vRtrMplsLspStatsSenderAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsLspStatsSenderAddr.setStatus(_A)
_VRtrMplsLspStatsLspName_Type=TNamedItem
_VRtrMplsLspStatsLspName_Object=MibTableColumn
vRtrMplsLspStatsLspName=_VRtrMplsLspStatsLspName_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,4),_VRtrMplsLspStatsLspName_Type())
vRtrMplsLspStatsLspName.setMaxAccess(_M)
if mibBuilder.loadTexts:vRtrMplsLspStatsLspName.setStatus(_A)
_VRtrMplsLspStatsRowStatus_Type=RowStatus
_VRtrMplsLspStatsRowStatus_Object=MibTableColumn
vRtrMplsLspStatsRowStatus=_VRtrMplsLspStatsRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,5),_VRtrMplsLspStatsRowStatus_Type())
vRtrMplsLspStatsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspStatsRowStatus.setStatus(_A)
_VRtrMplsLspStatsLastChanged_Type=TimeStamp
_VRtrMplsLspStatsLastChanged_Object=MibTableColumn
vRtrMplsLspStatsLastChanged=_VRtrMplsLspStatsLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,6),_VRtrMplsLspStatsLastChanged_Type())
vRtrMplsLspStatsLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspStatsLastChanged.setStatus(_A)
class _VRtrMplsLspStatsCollectStats_Type(TruthValue):defaultValue=2
_VRtrMplsLspStatsCollectStats_Type.__name__=_E
_VRtrMplsLspStatsCollectStats_Object=MibTableColumn
vRtrMplsLspStatsCollectStats=_VRtrMplsLspStatsCollectStats_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,7),_VRtrMplsLspStatsCollectStats_Type())
vRtrMplsLspStatsCollectStats.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspStatsCollectStats.setStatus(_A)
class _VRtrMplsLspStatsAccntingPolicy_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,99))
_VRtrMplsLspStatsAccntingPolicy_Type.__name__=_D
_VRtrMplsLspStatsAccntingPolicy_Object=MibTableColumn
vRtrMplsLspStatsAccntingPolicy=_VRtrMplsLspStatsAccntingPolicy_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,8),_VRtrMplsLspStatsAccntingPolicy_Type())
vRtrMplsLspStatsAccntingPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspStatsAccntingPolicy.setStatus(_A)
class _VRtrMplsLspStatsAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrMplsLspStatsAdminState_Type.__name__=_N
_VRtrMplsLspStatsAdminState_Object=MibTableColumn
vRtrMplsLspStatsAdminState=_VRtrMplsLspStatsAdminState_Object((1,3,6,1,4,1,7483,6,1,2,6,38,1,9),_VRtrMplsLspStatsAdminState_Type())
vRtrMplsLspStatsAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMplsLspStatsAdminState.setStatus(_A)
_VRtrMplsSystemConfigTable_Object=MibTable
vRtrMplsSystemConfigTable=_VRtrMplsSystemConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,6,45))
if mibBuilder.loadTexts:vRtrMplsSystemConfigTable.setStatus(_A)
_VRtrMplsSystemConfigEntry_Object=MibTableRow
vRtrMplsSystemConfigEntry=_VRtrMplsSystemConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,45,1))
vRtrMplsSystemConfigEntry.setIndexNames((0,_J,_K),(0,_G,_I))
if mibBuilder.loadTexts:vRtrMplsSystemConfigEntry.setStatus(_A)
class _VRtrMplsLabelMaxStaticLspLabels_Type(Unsigned32):defaultValue=2016;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262112))
_VRtrMplsLabelMaxStaticLspLabels_Type.__name__=_D
_VRtrMplsLabelMaxStaticLspLabels_Object=MibTableColumn
vRtrMplsLabelMaxStaticLspLabels=_VRtrMplsLabelMaxStaticLspLabels_Object((1,3,6,1,4,1,7483,6,1,2,6,45,1,1),_VRtrMplsLabelMaxStaticLspLabels_Type())
vRtrMplsLabelMaxStaticLspLabels.setMaxAccess(_l)
if mibBuilder.loadTexts:vRtrMplsLabelMaxStaticLspLabels.setStatus(_A)
class _VRtrMplsLabelMaxStaticSvcLabels_Type(Unsigned32):defaultValue=16384;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262112))
_VRtrMplsLabelMaxStaticSvcLabels_Type.__name__=_D
_VRtrMplsLabelMaxStaticSvcLabels_Object=MibTableColumn
vRtrMplsLabelMaxStaticSvcLabels=_VRtrMplsLabelMaxStaticSvcLabels_Object((1,3,6,1,4,1,7483,6,1,2,6,45,1,2),_VRtrMplsLabelMaxStaticSvcLabels_Type())
vRtrMplsLabelMaxStaticSvcLabels.setMaxAccess(_l)
if mibBuilder.loadTexts:vRtrMplsLabelMaxStaticSvcLabels.setStatus(_A)
_VRtrMplsLspNameTable_Object=MibTable
vRtrMplsLspNameTable=_VRtrMplsLspNameTable_Object((1,3,6,1,4,1,7483,6,1,2,6,46))
if mibBuilder.loadTexts:vRtrMplsLspNameTable.setStatus(_A)
_VRtrMplsLspNameEntry_Object=MibTableRow
vRtrMplsLspNameEntry=_VRtrMplsLspNameEntry_Object((1,3,6,1,4,1,7483,6,1,2,6,46,1))
vRtrMplsLspNameEntry.setIndexNames((0,_J,_K),(0,_G,_I),(1,_F,_m))
if mibBuilder.loadTexts:vRtrMplsLspNameEntry.setStatus(_A)
_VRtrMplsLspNameIndex_Type=TmnxVRtrMplsLspID
_VRtrMplsLspNameIndex_Object=MibTableColumn
vRtrMplsLspNameIndex=_VRtrMplsLspNameIndex_Object((1,3,6,1,4,1,7483,6,1,2,6,46,1,1),_VRtrMplsLspNameIndex_Type())
vRtrMplsLspNameIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspNameIndex.setStatus(_A)
_VRtrMplsLspScalar1_Type=Unsigned32
_VRtrMplsLspScalar1_Object=MibScalar
vRtrMplsLspScalar1=_VRtrMplsLspScalar1_Object((1,3,6,1,4,1,7483,6,1,2,6,101),_VRtrMplsLspScalar1_Type())
vRtrMplsLspScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspScalar1.setStatus(_A)
_VRtrMplsLspScalar2_Type=Unsigned32
_VRtrMplsLspScalar2_Object=MibScalar
vRtrMplsLspScalar2=_VRtrMplsLspScalar2_Object((1,3,6,1,4,1,7483,6,1,2,6,102),_VRtrMplsLspScalar2_Type())
vRtrMplsLspScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsLspScalar2.setStatus(_A)
vRtrMplsLspEntry.registerAugmentions((_F,_n))
vRtrMplsLspStatEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())
vRtrMplsIfEntry.registerAugmentions((_F,_o))
vRtrMplsIfStatEntry.setIndexNames(*vRtrMplsIfEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{_g:TmnxMplsLabelOwner,'TmnxMplsOperDownReasonCode':TmnxMplsOperDownReasonCode,_b:TmnxMplsLspBgpRSVPLSPTunState,_S:TmnxMplsLspAddrType,'tnMplsMIBModule':tnMplsMIBModule,'tnMplsObjs':tnMplsObjs,'vRtrMplsLspTable':vRtrMplsLspTable,'vRtrMplsLspEntry':vRtrMplsLspEntry,_Y:vRtrMplsLspIndex,'vRtrMplsLspRowStatus':vRtrMplsLspRowStatus,'vRtrMplsLspLastChange':vRtrMplsLspLastChange,_m:vRtrMplsLspName,'vRtrMplsLspAdminState':vRtrMplsLspAdminState,'vRtrMplsLspOperState':vRtrMplsLspOperState,'vRtrMplsLspFromAddr':vRtrMplsLspFromAddr,'vRtrMplsLspToAddr':vRtrMplsLspToAddr,'vRtrMplsLspType':vRtrMplsLspType,'vRtrMplsLspOutSegIndx':vRtrMplsLspOutSegIndx,'vRtrMplsLspRetryTimer':vRtrMplsLspRetryTimer,'vRtrMplsLspRetryLimit':vRtrMplsLspRetryLimit,'vRtrMplsLspMetric':vRtrMplsLspMetric,'vRtrMplsLspDecrementTtl':vRtrMplsLspDecrementTtl,'vRtrMplsLspCspf':vRtrMplsLspCspf,'vRtrMplsLspFastReroute':vRtrMplsLspFastReroute,'vRtrMplsLspFRHopLimit':vRtrMplsLspFRHopLimit,'vRtrMplsLspFRBandwidth':vRtrMplsLspFRBandwidth,'vRtrMplsLspClassOfService':vRtrMplsLspClassOfService,'vRtrMplsLspSetupPriority':vRtrMplsLspSetupPriority,'vRtrMplsLspHoldPriority':vRtrMplsLspHoldPriority,'vRtrMplsLspRecord':vRtrMplsLspRecord,'vRtrMplsLspPreference':vRtrMplsLspPreference,'vRtrMplsLspBandwidth':vRtrMplsLspBandwidth,'vRtrMplsLspBwProtect':vRtrMplsLspBwProtect,'vRtrMplsLspHopLimit':vRtrMplsLspHopLimit,'vRtrMplsLspNegotiatedMTU':vRtrMplsLspNegotiatedMTU,'vRtrMplsLspRsvpResvStyle':vRtrMplsLspRsvpResvStyle,'vRtrMplsLspRsvpAdspec':vRtrMplsLspRsvpAdspec,'vRtrMplsLspFRMethod':vRtrMplsLspFRMethod,'vRtrMplsLspFRNodeProtect':vRtrMplsLspFRNodeProtect,'vRtrMplsLspAdminGroupInclude':vRtrMplsLspAdminGroupInclude,'vRtrMplsLspAdminGroupExclude':vRtrMplsLspAdminGroupExclude,'vRtrMplsLspAdaptive':vRtrMplsLspAdaptive,'vRtrMplsLspInheritance':vRtrMplsLspInheritance,'vRtrMplsLspOptimizeTimer':vRtrMplsLspOptimizeTimer,'vRtrMplsLspOperFastReroute':vRtrMplsLspOperFastReroute,'vRtrMplsLspFRObject':vRtrMplsLspFRObject,'vRtrMplsLspHoldTimer':vRtrMplsLspHoldTimer,'vRtrMplsLspCspfTeMetricEnabled':vRtrMplsLspCspfTeMetricEnabled,'vRtrMplsLspP2mpId':vRtrMplsLspP2mpId,'vRtrMplsLspClassType':vRtrMplsLspClassType,'vRtrMplsLspOperMetric':vRtrMplsLspOperMetric,'vRtrMplsLspLdpOverRsvpInclude':vRtrMplsLspLdpOverRsvpInclude,'vRtrMplsLspLeastFill':vRtrMplsLspLeastFill,'vRtrMplsLspVprnAutoBindInclude':vRtrMplsLspVprnAutoBindInclude,'vRtrMplsLspMainCTRetryLimit':vRtrMplsLspMainCTRetryLimit,'vRtrMplsLspIgpShortcut':vRtrMplsLspIgpShortcut,'vRtrMplsLspOriginTemplate':vRtrMplsLspOriginTemplate,'vRtrMplsLspAutoBandwidth':vRtrMplsLspAutoBandwidth,'vRtrMplsLspCspfToFirstLoose':vRtrMplsLspCspfToFirstLoose,'vRtrMplsLspPropAdminGroup':vRtrMplsLspPropAdminGroup,'vRtrMplsLspBgpShortcut':vRtrMplsLspBgpShortcut,'vRtrMplsLspBgpTransportTunnel':vRtrMplsLspBgpTransportTunnel,'vRtrMplsLspSwitchStbyPath':vRtrMplsLspSwitchStbyPath,'vRtrMplsLspSwitchStbyPathIndex':vRtrMplsLspSwitchStbyPathIndex,'vRtrMplsLspSwitchStbyPathForce':vRtrMplsLspSwitchStbyPathForce,'vRtrMplsLspExcludeNodeAddrType':vRtrMplsLspExcludeNodeAddrType,'vRtrMplsLspExcludeNodeAddr':vRtrMplsLspExcludeNodeAddr,'vRtrMplsLspIgpShortcutLfaType':vRtrMplsLspIgpShortcutLfaType,'vRtrMplsLspToAddrType':vRtrMplsLspToAddrType,'vRtrMplsLspFromAddrType':vRtrMplsLspFromAddrType,'vRtrMplsLspToNodeId':vRtrMplsLspToNodeId,'vRtrMplsLspFromNodeId':vRtrMplsLspFromNodeId,'vRtrMplsLspDestGlobalId':vRtrMplsLspDestGlobalId,'vRtrMplsLspDestTunnelNum':vRtrMplsLspDestTunnelNum,'vRtrMplsLspStatTable':vRtrMplsLspStatTable,_n:vRtrMplsLspStatEntry,'vRtrMplsLspOctets':vRtrMplsLspOctets,'vRtrMplsLspPackets':vRtrMplsLspPackets,'vRtrMplsLspAge':vRtrMplsLspAge,'vRtrMplsLspTimeUp':vRtrMplsLspTimeUp,'vRtrMplsLspTimeDown':vRtrMplsLspTimeDown,'vRtrMplsLspPrimaryTimeUp':vRtrMplsLspPrimaryTimeUp,'vRtrMplsLspTransitions':vRtrMplsLspTransitions,'vRtrMplsLspLastTransition':vRtrMplsLspLastTransition,'vRtrMplsLspPathChanges':vRtrMplsLspPathChanges,'vRtrMplsLspLastPathChange':vRtrMplsLspLastPathChange,'vRtrMplsLspConfiguredPaths':vRtrMplsLspConfiguredPaths,'vRtrMplsLspStandbyPaths':vRtrMplsLspStandbyPaths,'vRtrMplsLspOperationalPaths':vRtrMplsLspOperationalPaths,'vRtrMplsLspConfP2mpInstances':vRtrMplsLspConfP2mpInstances,'vRtrMplsGeneralTable':vRtrMplsGeneralTable,'vRtrMplsGeneralEntry':vRtrMplsGeneralEntry,'vRtrMplsGeneralLastChange':vRtrMplsGeneralLastChange,'vRtrMplsGeneralAdminState':vRtrMplsGeneralAdminState,'vRtrMplsGeneralOperState':vRtrMplsGeneralOperState,'vRtrMplsGeneralPropagateTtl':vRtrMplsGeneralPropagateTtl,'vRtrMplsGeneralTE':vRtrMplsGeneralTE,'vRtrMplsGeneralNewLspIndex':vRtrMplsGeneralNewLspIndex,'vRtrMplsGeneralOptimizeTimer':vRtrMplsGeneralOptimizeTimer,'vRtrMplsGeneralFRObject':vRtrMplsGeneralFRObject,'vRtrMplsGeneralResignalTimer':vRtrMplsGeneralResignalTimer,'vRtrMplsGeneralHoldTimer':vRtrMplsGeneralHoldTimer,'vRtrMplsGeneralDynamicBypass':vRtrMplsGeneralDynamicBypass,'vRtrMplsGeneralNextResignal':vRtrMplsGeneralNextResignal,'vRtrMplsGeneralOperDownReason':vRtrMplsGeneralOperDownReason,'vRtrMplsGeneralSrlgFrr':vRtrMplsGeneralSrlgFrr,'vRtrMplsGeneralSrlgFrrStrict':vRtrMplsGeneralSrlgFrrStrict,'vRtrMplsGeneralNewP2mpInstIndex':vRtrMplsGeneralNewP2mpInstIndex,'vRtrMplsGeneralLeastFillMinThd':vRtrMplsGeneralLeastFillMinThd,'vRtrMplsGenLeastFillReoptiThd':vRtrMplsGenLeastFillReoptiThd,'vRtrMplsGeneralUseSrlgDB':vRtrMplsGeneralUseSrlgDB,'vRtrMplsGeneralP2mpResigTimer':vRtrMplsGeneralP2mpResigTimer,'vRtrMplsGeneralP2mpNextResignal':vRtrMplsGeneralP2mpNextResignal,'vRtrMplsGeneralSecFastRetryTimer':vRtrMplsGeneralSecFastRetryTimer,'vRtrMplsGeneralShortTTLPropLocal':vRtrMplsGeneralShortTTLPropLocal,'vRtrMplsGeneralShortTTLPropTrans':vRtrMplsGeneralShortTTLPropTrans,'vRtrMplsGeneralStaticLspFRTimer':vRtrMplsGeneralStaticLspFRTimer,'vRtrMplsGeneralAutoBWDefSampMul':vRtrMplsGeneralAutoBWDefSampMul,'vRtrMplsGeneralAutoBWDefAdjMul':vRtrMplsGeneralAutoBWDefAdjMul,'vRtrMplsGeneralExpBackoffRetry':vRtrMplsGeneralExpBackoffRetry,'vRtrMplsGeneralCspfOnLooseHop':vRtrMplsGeneralCspfOnLooseHop,'vRtrMplsGeneralP2PMaxByPassAssoc':vRtrMplsGeneralP2PMaxByPassAssoc,'vRtrMplsGenP2pActPathFastRetry':vRtrMplsGenP2pActPathFastRetry,'vRtrMplsGenP2mpS2lFastRetry':vRtrMplsGenP2mpS2lFastRetry,'vRtrMplsGenLspInitRetryTimeout':vRtrMplsGenLspInitRetryTimeout,'vRtrMplsLoggerEventBundling':vRtrMplsLoggerEventBundling,'vRtrMplsGenIssuMplsLockdown':vRtrMplsGenIssuMplsLockdown,'vRtrMplsIfTable':vRtrMplsIfTable,'vRtrMplsIfEntry':vRtrMplsIfEntry,'vRtrMplsIfAdminState':vRtrMplsIfAdminState,'vRtrMplsIfOperState':vRtrMplsIfOperState,'vRtrMplsIfAdminGroup':vRtrMplsIfAdminGroup,'vRtrMplsIfTeMetric':vRtrMplsIfTeMetric,'vRtrMplsIfStatTable':vRtrMplsIfStatTable,_o:vRtrMplsIfStatEntry,'vRtrMplsIfTxPktCount':vRtrMplsIfTxPktCount,'vRtrMplsIfRxPktCount':vRtrMplsIfRxPktCount,'vRtrMplsIfTxOctetCount':vRtrMplsIfTxOctetCount,'vRtrMplsIfRxOctetCount':vRtrMplsIfRxOctetCount,'vRtrMplsLabelRangeTable':vRtrMplsLabelRangeTable,'vRtrMplsLabelRangeEntry':vRtrMplsLabelRangeEntry,_d:vRtrMplsLabelType,'vRtrMplsLabelRangeMin':vRtrMplsLabelRangeMin,'vRtrMplsLabelRangeMax':vRtrMplsLabelRangeMax,'vRtrMplsLabelRangeAging':vRtrMplsLabelRangeAging,'vRtrMplsLabelRangeAvailable':vRtrMplsLabelRangeAvailable,'vRtrMplsStaticLSPLabelTable':vRtrMplsStaticLSPLabelTable,'vRtrMplsStaticLSPLabelEntry':vRtrMplsStaticLSPLabelEntry,_e:vRtrMplsStaticLSPLabel,'vRtrMplsStaticLSPLabelOwner':vRtrMplsStaticLSPLabelOwner,'vRtrMplsStaticSvcLabelTable':vRtrMplsStaticSvcLabelTable,'vRtrMplsStaticSvcLabelEntry':vRtrMplsStaticSvcLabelEntry,_f:vRtrMplsStaticSvcLabel,'vRtrMplsStaticSvcLabelOwner':vRtrMplsStaticSvcLabelOwner,'vRtrMplsLspStatsTblLastChgd':vRtrMplsLspStatsTblLastChgd,'vRtrMplsLspStatsTable':vRtrMplsLspStatsTable,'vRtrMplsLspStatsEntry':vRtrMplsLspStatsEntry,_h:vRtrMplsLspStatsType,_i:vRtrMplsLspStatsSenderAddrType,_j:vRtrMplsLspStatsSenderAddr,_k:vRtrMplsLspStatsLspName,'vRtrMplsLspStatsRowStatus':vRtrMplsLspStatsRowStatus,'vRtrMplsLspStatsLastChanged':vRtrMplsLspStatsLastChanged,'vRtrMplsLspStatsCollectStats':vRtrMplsLspStatsCollectStats,'vRtrMplsLspStatsAccntingPolicy':vRtrMplsLspStatsAccntingPolicy,'vRtrMplsLspStatsAdminState':vRtrMplsLspStatsAdminState,'vRtrMplsSystemConfigTable':vRtrMplsSystemConfigTable,'vRtrMplsSystemConfigEntry':vRtrMplsSystemConfigEntry,'vRtrMplsLabelMaxStaticLspLabels':vRtrMplsLabelMaxStaticLspLabels,'vRtrMplsLabelMaxStaticSvcLabels':vRtrMplsLabelMaxStaticSvcLabels,'vRtrMplsLspNameTable':vRtrMplsLspNameTable,'vRtrMplsLspNameEntry':vRtrMplsLspNameEntry,'vRtrMplsLspNameIndex':vRtrMplsLspNameIndex,'vRtrMplsLspScalar1':vRtrMplsLspScalar1,'vRtrMplsLspScalar2':vRtrMplsLspScalar2})