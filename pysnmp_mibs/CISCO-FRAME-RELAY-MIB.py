_BT='ciscoFrConnMIBGroup'
_BS='ciscoFrFragMIBGroup'
_BR='ciscoFrElmiMIBGroup1'
_BQ='ciscoExtCircuitMIBGroup1'
_BP='ciscoFrElmiMIBGroup'
_BO='ciscoFrMIBGroupRev1'
_BN='ciscoFrMIBGroup'
_BM='cfrExtCircuitRcvPktRate'
_BL='cfrExtCircuitRcvDataRate'
_BK='cfrExtCircuitTxPktRate'
_BJ='cfrExtCircuitTxDataRate'
_BI='cfrConnClpBit'
_BH='cfrConnDeBit'
_BG='cfrConnEfciBit'
_BF='cfrConnFrSscsDlci'
_BE='cfrConnServiceTranslation'
_BD='cfrConnSegment2Vci'
_BC='cfrConnSegment2Vpi'
_BB='cfrConnSegment2Name'
_BA='cfrConnSegment1Dlci'
_B9='cfrConnSegment1VCGroup'
_B8='cfrConnSegment1Name'
_B7='cfrConnState'
_B6='cfrConnID'
_B5='cfrConnName'
_B4='cfrFragInterleavedOutPkts'
_B3='cfrFragSeqMissedPkts'
_B2='cfrFragUnexpectedBBitSetPkts'
_B1='cfrFragOutOfSeqFragPkts'
_B0='cfrFragTimeoutsIn'
_A_='cfrFragDroppedFragmentedOutPkts'
_Az='cfrFragDroppedReAssembledInPkts'
_Ay='cfrFragPreOutOctets'
_Ax='cfrFragPreOutPkts'
_Aw='cfrFragAssembledInOctets'
_Av='cfrFragAssembledInPkts'
_Au='cfrFragNotOutOctets'
_At='cfrFragNotInOctets'
_As='cfrFragNotOutPkts'
_Ar='cfrFragNotInPkts'
_Aq='cfrFragOutOctets'
_Ap='cfrFragInOctets'
_Ao='cfrFragOutPkts'
_An='cfrFragInPkts'
_Am='cfrFragType'
_Al='cfrFragSize'
_Ak='cfrElmiLinkStatus'
_Aj='cfrExtCircuitShapeAdapting'
_Ai='cfrExtCircuitShapeActive'
_Ah='cfrExtCircuitShapeBytesDelay'
_Ag='cfrExtCircuitShapePktsDelay'
_Af='cfrExtCircuitShapeBytes'
_Ae='cfrExtCircuitShapePkts'
_Ad='cfrExtCircuitShapeByteIncrement'
_Ac='cfrExtCircuitShapeInterval'
_Ab='cfrExtCircuitShapeByteLimit'
_Aa='cfrMapPayloadCompress'
_AZ='cfrExtCircuitEntry'
_AY='cfrCircuitEntry'
_AX='cfrLmiEntry'
_AW='ciscoExtCircuitMIBGroup'
_AV='obsolete'
_AU='cfrElmiNeighborDeviceName'
_AT='cfrElmiNeighborPlatformName'
_AS='cfrElmiNeighborVendorName'
_AR='cfrElmiNeighborIfIndex'
_AQ='cfrElmiNeighborIpAddress'
_AP='cfrElmiNeighborArStatus'
_AO='cfrElmiRemoteStatus'
_AN='cfrElmiArStatus'
_AM='cfrElmiIpAddr'
_AL='cfrExtCircuitBandwidth'
_AK='cfrExtCircuitBcastByteOuts'
_AJ='cfrExtCircuitBcastPktOuts'
_AI='cfrExtCircuitMinThruputIn'
_AH='cfrExtCircuitMinThruputOut'
_AG='cfrExtCircuitBECNOuts'
_AF='cfrExtCircuitFECNOuts'
_AE='cfrMapPayloadCompressType'
_AD='cfrMapRtpHdrCompress'
_AC='cfrSvcMinThruputIn'
_AB='cfrSvcMinThruputOut'
_AA='inapplicable'
_A9='ifIndex'
_A8='IF-MIB'
_A7='ciscoFrSvcMIBGroup'
_A6='ciscoFrMapMIBGroup'
_A5='ciscoFrTsMIBGroup'
_A4='ciscoFrCircuitMIBGroup'
_A3='ciscoFrLmiMIBGroup'
_A2='cfrExtCircuitUncompressOuts'
_A1='cfrExtCircuitUncompressIns'
_A0='cfrSvcIdleTime'
_z='cfrSvcExcessBurstIn'
_y='cfrSvcCommitBurstIn'
_x='cfrSvcThroughputIn'
_w='cfrSvcAddrRemote'
_v='cfrSvcAddrLocal'
_u='cfrMapTcpHdrCompress'
_t='cfrMapBroadcast'
_s='cfrMapEncaps'
_r='cfrMapType'
_q='cfrMapAddress'
_p='cfrMapProtocol'
_o='cfrCircuitType'
_n='cfrCircuitDropPktsOuts'
_m='cfrCircuitDEouts'
_l='cfrCircuitDEins'
_k='cfrLmiT392Dce'
_j='cfrLmiN393Dce'
_i='cfrLmiN392Dce'
_h='cfrLmiStatusEnqTimeouts'
_g='cfrLmiStatusTimeouts'
_f='cfrLmiUpdateStatusOuts'
_e='cfrLmiUpdateStatusIns'
_d='cfrLmiStatusOuts'
_c='cfrLmiStatusIns'
_b='cfrLmiEnquiryOuts'
_a='cfrLmiEnquiryIns'
_Z='cfrLmiLinkType'
_Y='cfrLmiLinkstatus'
_X='disabled'
_W='enabled'
_V='OctetString'
_U='cfrExtCircuitRoutedIf'
_T='cfrExtCircuitRoutedDlci'
_S='cfrExtCircuitMulticast'
_R='cfrExtCircuitCreateType'
_Q='cfrExtCircuitMapStatus'
_P='cfrExtCircuitSubifIndex'
_O='cfrExtCircuitIfType'
_N='cfrExtCircuitIfName'
_M='cfrMapIndex'
_L='frCircuitIfIndex'
_K='frCircuitDlci'
_J='bits per second'
_I='messages'
_H='deprecated'
_G='RFC1315-MIB'
_F='octets'
_E='packets'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-FRAME-RELAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_A8,'InterfaceIndex',_A9)
frCircuitDlci,frCircuitEntry,frCircuitIfIndex,frDlcmiEntry=mibBuilder.importSymbols(_G,_K,'frCircuitEntry',_L,'frDlcmiEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoFrameRelayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,49))
if mibBuilder.loadTexts:ciscoFrameRelayMIB.setRevisions(('2000-10-13 00:00','2000-05-22 00:00','2000-05-16 00:00','2000-04-26 00:00','1999-08-21 00:00','1996-08-15 00:00'))
class DlciNumber(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
class CfrMapProtocols(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7,10,11,12,13,16,18,22,25,37,38,39,40,47,48,49,53,63,74,83,999)));namedValues=NamedValues(*(('arp',1),('serialArp',6),('ip',7),('xns',10),('novell',11),('apollo',12),('vines',13),('appletalk',16),('ieeeSpanning',18),('decnet',22),('clns',25),('rsrb',37),('bridge',38),('stun',39),('frArp',40),('uncompressedTcp',47),('compressedTcp',48),('llc2',49),('frSwitch',53),('dlsw',63),('nhrp',74),('compressedRtp',83),('wildcard',999)))
_CiscoFrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFrMIBObjects=_CiscoFrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,49,1))
_CfrLmiObjs_ObjectIdentity=ObjectIdentity
cfrLmiObjs=_CfrLmiObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,1))
_CfrLmiTable_Object=MibTable
cfrLmiTable=_CfrLmiTable_Object((1,3,6,1,4,1,9,9,49,1,1,1))
if mibBuilder.loadTexts:cfrLmiTable.setStatus(_B)
_CfrLmiEntry_Object=MibTableRow
cfrLmiEntry=_CfrLmiEntry_Object((1,3,6,1,4,1,9,9,49,1,1,1,1))
if mibBuilder.loadTexts:cfrLmiEntry.setStatus(_B)
class _CfrLmiLinkstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CfrLmiLinkstatus_Type.__name__=_D
_CfrLmiLinkstatus_Object=MibTableColumn
cfrLmiLinkstatus=_CfrLmiLinkstatus_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,1),_CfrLmiLinkstatus_Type())
cfrLmiLinkstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiLinkstatus.setStatus(_B)
class _CfrLmiLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('nni',3)))
_CfrLmiLinkType_Type.__name__=_D
_CfrLmiLinkType_Object=MibTableColumn
cfrLmiLinkType=_CfrLmiLinkType_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,2),_CfrLmiLinkType_Type())
cfrLmiLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiLinkType.setStatus(_B)
_CfrLmiEnquiryIns_Type=Counter32
_CfrLmiEnquiryIns_Object=MibTableColumn
cfrLmiEnquiryIns=_CfrLmiEnquiryIns_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,3),_CfrLmiEnquiryIns_Type())
cfrLmiEnquiryIns.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiEnquiryIns.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiEnquiryIns.setUnits(_I)
_CfrLmiEnquiryOuts_Type=Counter32
_CfrLmiEnquiryOuts_Object=MibTableColumn
cfrLmiEnquiryOuts=_CfrLmiEnquiryOuts_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,4),_CfrLmiEnquiryOuts_Type())
cfrLmiEnquiryOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiEnquiryOuts.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiEnquiryOuts.setUnits(_I)
_CfrLmiStatusIns_Type=Counter32
_CfrLmiStatusIns_Object=MibTableColumn
cfrLmiStatusIns=_CfrLmiStatusIns_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,5),_CfrLmiStatusIns_Type())
cfrLmiStatusIns.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiStatusIns.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiStatusIns.setUnits(_I)
_CfrLmiStatusOuts_Type=Counter32
_CfrLmiStatusOuts_Object=MibTableColumn
cfrLmiStatusOuts=_CfrLmiStatusOuts_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,6),_CfrLmiStatusOuts_Type())
cfrLmiStatusOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiStatusOuts.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiStatusOuts.setUnits(_I)
_CfrLmiUpdateStatusIns_Type=Counter32
_CfrLmiUpdateStatusIns_Object=MibTableColumn
cfrLmiUpdateStatusIns=_CfrLmiUpdateStatusIns_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,7),_CfrLmiUpdateStatusIns_Type())
cfrLmiUpdateStatusIns.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiUpdateStatusIns.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiUpdateStatusIns.setUnits(_I)
_CfrLmiUpdateStatusOuts_Type=Counter32
_CfrLmiUpdateStatusOuts_Object=MibTableColumn
cfrLmiUpdateStatusOuts=_CfrLmiUpdateStatusOuts_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,8),_CfrLmiUpdateStatusOuts_Type())
cfrLmiUpdateStatusOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiUpdateStatusOuts.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiUpdateStatusOuts.setUnits(_I)
_CfrLmiStatusTimeouts_Type=Counter32
_CfrLmiStatusTimeouts_Object=MibTableColumn
cfrLmiStatusTimeouts=_CfrLmiStatusTimeouts_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,9),_CfrLmiStatusTimeouts_Type())
cfrLmiStatusTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiStatusTimeouts.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiStatusTimeouts.setUnits('times')
_CfrLmiStatusEnqTimeouts_Type=Counter32
_CfrLmiStatusEnqTimeouts_Object=MibTableColumn
cfrLmiStatusEnqTimeouts=_CfrLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,10),_CfrLmiStatusEnqTimeouts_Type())
cfrLmiStatusEnqTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiStatusEnqTimeouts.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiStatusEnqTimeouts.setUnits('times')
class _CfrLmiN392Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CfrLmiN392Dce_Type.__name__=_D
_CfrLmiN392Dce_Object=MibTableColumn
cfrLmiN392Dce=_CfrLmiN392Dce_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,11),_CfrLmiN392Dce_Type())
cfrLmiN392Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiN392Dce.setStatus(_B)
class _CfrLmiN393Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CfrLmiN393Dce_Type.__name__=_D
_CfrLmiN393Dce_Object=MibTableColumn
cfrLmiN393Dce=_CfrLmiN393Dce_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,12),_CfrLmiN393Dce_Type())
cfrLmiN393Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiN393Dce.setStatus(_B)
class _CfrLmiT392Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CfrLmiT392Dce_Type.__name__=_D
_CfrLmiT392Dce_Object=MibTableColumn
cfrLmiT392Dce=_CfrLmiT392Dce_Object((1,3,6,1,4,1,9,9,49,1,1,1,1,13),_CfrLmiT392Dce_Type())
cfrLmiT392Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrLmiT392Dce.setStatus(_B)
if mibBuilder.loadTexts:cfrLmiT392Dce.setUnits('seconds')
_CfrCircuitObjs_ObjectIdentity=ObjectIdentity
cfrCircuitObjs=_CfrCircuitObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,2))
_CfrCircuitTable_Object=MibTable
cfrCircuitTable=_CfrCircuitTable_Object((1,3,6,1,4,1,9,9,49,1,2,1))
if mibBuilder.loadTexts:cfrCircuitTable.setStatus(_B)
_CfrCircuitEntry_Object=MibTableRow
cfrCircuitEntry=_CfrCircuitEntry_Object((1,3,6,1,4,1,9,9,49,1,2,1,1))
if mibBuilder.loadTexts:cfrCircuitEntry.setStatus(_B)
_CfrCircuitDEins_Type=Counter32
_CfrCircuitDEins_Object=MibTableColumn
cfrCircuitDEins=_CfrCircuitDEins_Object((1,3,6,1,4,1,9,9,49,1,2,1,1,1),_CfrCircuitDEins_Type())
cfrCircuitDEins.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrCircuitDEins.setStatus(_B)
if mibBuilder.loadTexts:cfrCircuitDEins.setUnits(_E)
_CfrCircuitDEouts_Type=Counter32
_CfrCircuitDEouts_Object=MibTableColumn
cfrCircuitDEouts=_CfrCircuitDEouts_Object((1,3,6,1,4,1,9,9,49,1,2,1,1,2),_CfrCircuitDEouts_Type())
cfrCircuitDEouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrCircuitDEouts.setStatus(_B)
if mibBuilder.loadTexts:cfrCircuitDEouts.setUnits(_E)
_CfrCircuitDropPktsOuts_Type=Counter32
_CfrCircuitDropPktsOuts_Object=MibTableColumn
cfrCircuitDropPktsOuts=_CfrCircuitDropPktsOuts_Object((1,3,6,1,4,1,9,9,49,1,2,1,1,3),_CfrCircuitDropPktsOuts_Type())
cfrCircuitDropPktsOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrCircuitDropPktsOuts.setStatus(_B)
if mibBuilder.loadTexts:cfrCircuitDropPktsOuts.setUnits(_E)
class _CfrCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('svc',2)))
_CfrCircuitType_Type.__name__=_D
_CfrCircuitType_Object=MibTableColumn
cfrCircuitType=_CfrCircuitType_Object((1,3,6,1,4,1,9,9,49,1,2,1,1,4),_CfrCircuitType_Type())
cfrCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrCircuitType.setStatus(_B)
_CfrExtCircuitTable_Object=MibTable
cfrExtCircuitTable=_CfrExtCircuitTable_Object((1,3,6,1,4,1,9,9,49,1,2,2))
if mibBuilder.loadTexts:cfrExtCircuitTable.setStatus(_B)
_CfrExtCircuitEntry_Object=MibTableRow
cfrExtCircuitEntry=_CfrExtCircuitEntry_Object((1,3,6,1,4,1,9,9,49,1,2,2,1))
if mibBuilder.loadTexts:cfrExtCircuitEntry.setStatus(_B)
_CfrExtCircuitIfName_Type=DisplayString
_CfrExtCircuitIfName_Object=MibTableColumn
cfrExtCircuitIfName=_CfrExtCircuitIfName_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,1),_CfrExtCircuitIfName_Type())
cfrExtCircuitIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitIfName.setStatus(_B)
class _CfrExtCircuitIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mainInterface',1),('pointToPoint',2),('multipoint',3)))
_CfrExtCircuitIfType_Type.__name__=_D
_CfrExtCircuitIfType_Object=MibTableColumn
cfrExtCircuitIfType=_CfrExtCircuitIfType_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,2),_CfrExtCircuitIfType_Type())
cfrExtCircuitIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitIfType.setStatus(_B)
_CfrExtCircuitSubifIndex_Type=InterfaceIndex
_CfrExtCircuitSubifIndex_Object=MibTableColumn
cfrExtCircuitSubifIndex=_CfrExtCircuitSubifIndex_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,3),_CfrExtCircuitSubifIndex_Type())
cfrExtCircuitSubifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitSubifIndex.setStatus(_B)
class _CfrExtCircuitMapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_CfrExtCircuitMapStatus_Type.__name__=_D
_CfrExtCircuitMapStatus_Object=MibTableColumn
cfrExtCircuitMapStatus=_CfrExtCircuitMapStatus_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,4),_CfrExtCircuitMapStatus_Type())
cfrExtCircuitMapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitMapStatus.setStatus(_B)
class _CfrExtCircuitCreateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_CfrExtCircuitCreateType_Type.__name__=_D
_CfrExtCircuitCreateType_Object=MibTableColumn
cfrExtCircuitCreateType=_CfrExtCircuitCreateType_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,5),_CfrExtCircuitCreateType_Type())
cfrExtCircuitCreateType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitCreateType.setStatus(_B)
_CfrExtCircuitMulticast_Type=TruthValue
_CfrExtCircuitMulticast_Object=MibTableColumn
cfrExtCircuitMulticast=_CfrExtCircuitMulticast_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,6),_CfrExtCircuitMulticast_Type())
cfrExtCircuitMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitMulticast.setStatus(_B)
_CfrExtCircuitRoutedDlci_Type=DlciNumber
_CfrExtCircuitRoutedDlci_Object=MibTableColumn
cfrExtCircuitRoutedDlci=_CfrExtCircuitRoutedDlci_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,7),_CfrExtCircuitRoutedDlci_Type())
cfrExtCircuitRoutedDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitRoutedDlci.setStatus(_B)
_CfrExtCircuitRoutedIf_Type=InterfaceIndex
_CfrExtCircuitRoutedIf_Object=MibTableColumn
cfrExtCircuitRoutedIf=_CfrExtCircuitRoutedIf_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,8),_CfrExtCircuitRoutedIf_Type())
cfrExtCircuitRoutedIf.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitRoutedIf.setStatus(_B)
_CfrExtCircuitUncompressIns_Type=Counter32
_CfrExtCircuitUncompressIns_Object=MibTableColumn
cfrExtCircuitUncompressIns=_CfrExtCircuitUncompressIns_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,9),_CfrExtCircuitUncompressIns_Type())
cfrExtCircuitUncompressIns.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitUncompressIns.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitUncompressIns.setUnits(_F)
_CfrExtCircuitUncompressOuts_Type=Counter32
_CfrExtCircuitUncompressOuts_Object=MibTableColumn
cfrExtCircuitUncompressOuts=_CfrExtCircuitUncompressOuts_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,10),_CfrExtCircuitUncompressOuts_Type())
cfrExtCircuitUncompressOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitUncompressOuts.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitUncompressOuts.setUnits(_F)
_CfrExtCircuitFECNOuts_Type=Counter32
_CfrExtCircuitFECNOuts_Object=MibTableColumn
cfrExtCircuitFECNOuts=_CfrExtCircuitFECNOuts_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,11),_CfrExtCircuitFECNOuts_Type())
cfrExtCircuitFECNOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitFECNOuts.setStatus(_B)
_CfrExtCircuitBECNOuts_Type=Counter32
_CfrExtCircuitBECNOuts_Object=MibTableColumn
cfrExtCircuitBECNOuts=_CfrExtCircuitBECNOuts_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,12),_CfrExtCircuitBECNOuts_Type())
cfrExtCircuitBECNOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitBECNOuts.setStatus(_B)
class _CfrExtCircuitMinThruputOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_CfrExtCircuitMinThruputOut_Type.__name__=_D
_CfrExtCircuitMinThruputOut_Object=MibTableColumn
cfrExtCircuitMinThruputOut=_CfrExtCircuitMinThruputOut_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,13),_CfrExtCircuitMinThruputOut_Type())
cfrExtCircuitMinThruputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitMinThruputOut.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitMinThruputOut.setUnits(_J)
class _CfrExtCircuitMinThruputIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_CfrExtCircuitMinThruputIn_Type.__name__=_D
_CfrExtCircuitMinThruputIn_Object=MibTableColumn
cfrExtCircuitMinThruputIn=_CfrExtCircuitMinThruputIn_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,14),_CfrExtCircuitMinThruputIn_Type())
cfrExtCircuitMinThruputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitMinThruputIn.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitMinThruputIn.setUnits(_J)
_CfrExtCircuitBcastPktOuts_Type=Counter32
_CfrExtCircuitBcastPktOuts_Object=MibTableColumn
cfrExtCircuitBcastPktOuts=_CfrExtCircuitBcastPktOuts_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,15),_CfrExtCircuitBcastPktOuts_Type())
cfrExtCircuitBcastPktOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitBcastPktOuts.setStatus(_B)
_CfrExtCircuitBcastByteOuts_Type=Counter32
_CfrExtCircuitBcastByteOuts_Object=MibTableColumn
cfrExtCircuitBcastByteOuts=_CfrExtCircuitBcastByteOuts_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,16),_CfrExtCircuitBcastByteOuts_Type())
cfrExtCircuitBcastByteOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitBcastByteOuts.setStatus(_B)
class _CfrExtCircuitBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CfrExtCircuitBandwidth_Type.__name__=_D
_CfrExtCircuitBandwidth_Object=MibTableColumn
cfrExtCircuitBandwidth=_CfrExtCircuitBandwidth_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,17),_CfrExtCircuitBandwidth_Type())
cfrExtCircuitBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitBandwidth.setUnits(_J)
class _CfrExtCircuitShapeByteLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,2147483647))
_CfrExtCircuitShapeByteLimit_Type.__name__=_D
_CfrExtCircuitShapeByteLimit_Object=MibTableColumn
cfrExtCircuitShapeByteLimit=_CfrExtCircuitShapeByteLimit_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,18),_CfrExtCircuitShapeByteLimit_Type())
cfrExtCircuitShapeByteLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeByteLimit.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitShapeByteLimit.setUnits(_F)
class _CfrExtCircuitShapeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,125))
_CfrExtCircuitShapeInterval_Type.__name__=_D
_CfrExtCircuitShapeInterval_Object=MibTableColumn
cfrExtCircuitShapeInterval=_CfrExtCircuitShapeInterval_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,19),_CfrExtCircuitShapeInterval_Type())
cfrExtCircuitShapeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeInterval.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitShapeInterval.setUnits('milliseconds')
class _CfrExtCircuitShapeByteIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,2147483647))
_CfrExtCircuitShapeByteIncrement_Type.__name__=_D
_CfrExtCircuitShapeByteIncrement_Object=MibTableColumn
cfrExtCircuitShapeByteIncrement=_CfrExtCircuitShapeByteIncrement_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,20),_CfrExtCircuitShapeByteIncrement_Type())
cfrExtCircuitShapeByteIncrement.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeByteIncrement.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitShapeByteIncrement.setUnits(_F)
_CfrExtCircuitShapePkts_Type=Counter32
_CfrExtCircuitShapePkts_Object=MibTableColumn
cfrExtCircuitShapePkts=_CfrExtCircuitShapePkts_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,21),_CfrExtCircuitShapePkts_Type())
cfrExtCircuitShapePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapePkts.setStatus(_B)
_CfrExtCircuitShapeBytes_Type=Counter32
_CfrExtCircuitShapeBytes_Object=MibTableColumn
cfrExtCircuitShapeBytes=_CfrExtCircuitShapeBytes_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,22),_CfrExtCircuitShapeBytes_Type())
cfrExtCircuitShapeBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeBytes.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitShapeBytes.setUnits(_F)
_CfrExtCircuitShapePktsDelay_Type=Counter32
_CfrExtCircuitShapePktsDelay_Object=MibTableColumn
cfrExtCircuitShapePktsDelay=_CfrExtCircuitShapePktsDelay_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,23),_CfrExtCircuitShapePktsDelay_Type())
cfrExtCircuitShapePktsDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapePktsDelay.setStatus(_B)
_CfrExtCircuitShapeBytesDelay_Type=Counter32
_CfrExtCircuitShapeBytesDelay_Object=MibTableColumn
cfrExtCircuitShapeBytesDelay=_CfrExtCircuitShapeBytesDelay_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,24),_CfrExtCircuitShapeBytesDelay_Type())
cfrExtCircuitShapeBytesDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeBytesDelay.setStatus(_B)
if mibBuilder.loadTexts:cfrExtCircuitShapeBytesDelay.setUnits(_F)
_CfrExtCircuitShapeActive_Type=TruthValue
_CfrExtCircuitShapeActive_Object=MibTableColumn
cfrExtCircuitShapeActive=_CfrExtCircuitShapeActive_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,25),_CfrExtCircuitShapeActive_Type())
cfrExtCircuitShapeActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeActive.setStatus(_B)
class _CfrExtCircuitShapeAdapting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('becn',2),('foreSight',3)))
_CfrExtCircuitShapeAdapting_Type.__name__=_D
_CfrExtCircuitShapeAdapting_Object=MibTableColumn
cfrExtCircuitShapeAdapting=_CfrExtCircuitShapeAdapting_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,26),_CfrExtCircuitShapeAdapting_Type())
cfrExtCircuitShapeAdapting.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitShapeAdapting.setStatus(_B)
class _CfrExtCircuitTxDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_CfrExtCircuitTxDataRate_Type.__name__=_D
_CfrExtCircuitTxDataRate_Object=MibTableColumn
cfrExtCircuitTxDataRate=_CfrExtCircuitTxDataRate_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,27),_CfrExtCircuitTxDataRate_Type())
cfrExtCircuitTxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitTxDataRate.setStatus(_B)
class _CfrExtCircuitTxPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_CfrExtCircuitTxPktRate_Type.__name__=_D
_CfrExtCircuitTxPktRate_Object=MibTableColumn
cfrExtCircuitTxPktRate=_CfrExtCircuitTxPktRate_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,28),_CfrExtCircuitTxPktRate_Type())
cfrExtCircuitTxPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitTxPktRate.setStatus(_B)
class _CfrExtCircuitRcvDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_CfrExtCircuitRcvDataRate_Type.__name__=_D
_CfrExtCircuitRcvDataRate_Object=MibTableColumn
cfrExtCircuitRcvDataRate=_CfrExtCircuitRcvDataRate_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,29),_CfrExtCircuitRcvDataRate_Type())
cfrExtCircuitRcvDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitRcvDataRate.setStatus(_B)
class _CfrExtCircuitRcvPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_CfrExtCircuitRcvPktRate_Type.__name__=_D
_CfrExtCircuitRcvPktRate_Object=MibTableColumn
cfrExtCircuitRcvPktRate=_CfrExtCircuitRcvPktRate_Object((1,3,6,1,4,1,9,9,49,1,2,2,1,30),_CfrExtCircuitRcvPktRate_Type())
cfrExtCircuitRcvPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrExtCircuitRcvPktRate.setStatus(_B)
_CfrMapObjs_ObjectIdentity=ObjectIdentity
cfrMapObjs=_CfrMapObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,3))
_CfrMapTable_Object=MibTable
cfrMapTable=_CfrMapTable_Object((1,3,6,1,4,1,9,9,49,1,3,1))
if mibBuilder.loadTexts:cfrMapTable.setStatus(_B)
_CfrMapEntry_Object=MibTableRow
cfrMapEntry=_CfrMapEntry_Object((1,3,6,1,4,1,9,9,49,1,3,1,1))
cfrMapEntry.setIndexNames((0,_G,_L),(0,_G,_K),(0,_A,_M))
if mibBuilder.loadTexts:cfrMapEntry.setStatus(_B)
class _CfrMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_CfrMapIndex_Type.__name__=_D
_CfrMapIndex_Object=MibTableColumn
cfrMapIndex=_CfrMapIndex_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,1),_CfrMapIndex_Type())
cfrMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapIndex.setStatus(_B)
_CfrMapProtocol_Type=CfrMapProtocols
_CfrMapProtocol_Object=MibTableColumn
cfrMapProtocol=_CfrMapProtocol_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,2),_CfrMapProtocol_Type())
cfrMapProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapProtocol.setStatus(_B)
class _CfrMapAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CfrMapAddress_Type.__name__=_V
_CfrMapAddress_Object=MibTableColumn
cfrMapAddress=_CfrMapAddress_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,3),_CfrMapAddress_Type())
cfrMapAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapAddress.setStatus(_B)
class _CfrMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('svc',3)))
_CfrMapType_Type.__name__=_D
_CfrMapType_Object=MibTableColumn
cfrMapType=_CfrMapType_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,4),_CfrMapType_Type())
cfrMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapType.setStatus(_B)
class _CfrMapEncaps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('cisco',2)))
_CfrMapEncaps_Type.__name__=_D
_CfrMapEncaps_Object=MibTableColumn
cfrMapEncaps=_CfrMapEncaps_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,5),_CfrMapEncaps_Type())
cfrMapEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapEncaps.setStatus(_B)
_CfrMapBroadcast_Type=TruthValue
_CfrMapBroadcast_Object=MibTableColumn
cfrMapBroadcast=_CfrMapBroadcast_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,6),_CfrMapBroadcast_Type())
cfrMapBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapBroadcast.setStatus(_B)
_CfrMapPayloadCompress_Type=TruthValue
_CfrMapPayloadCompress_Object=MibTableColumn
cfrMapPayloadCompress=_CfrMapPayloadCompress_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,7),_CfrMapPayloadCompress_Type())
cfrMapPayloadCompress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapPayloadCompress.setStatus(_H)
class _CfrMapTcpHdrCompress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),('passive',2),('active',3)))
_CfrMapTcpHdrCompress_Type.__name__=_D
_CfrMapTcpHdrCompress_Object=MibTableColumn
cfrMapTcpHdrCompress=_CfrMapTcpHdrCompress_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,8),_CfrMapTcpHdrCompress_Type())
cfrMapTcpHdrCompress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapTcpHdrCompress.setStatus(_B)
class _CfrMapRtpHdrCompress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),('passive',2),('active',3)))
_CfrMapRtpHdrCompress_Type.__name__=_D
_CfrMapRtpHdrCompress_Object=MibTableColumn
cfrMapRtpHdrCompress=_CfrMapRtpHdrCompress_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,9),_CfrMapRtpHdrCompress_Type())
cfrMapRtpHdrCompress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapRtpHdrCompress.setStatus(_B)
class _CfrMapPayloadCompressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AA,1),('cisco',2),('frf9Software',3),('frf9Hardware',4)))
_CfrMapPayloadCompressType_Type.__name__=_D
_CfrMapPayloadCompressType_Object=MibTableColumn
cfrMapPayloadCompressType=_CfrMapPayloadCompressType_Object((1,3,6,1,4,1,9,9,49,1,3,1,1,10),_CfrMapPayloadCompressType_Type())
cfrMapPayloadCompressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrMapPayloadCompressType.setStatus(_B)
_CfrSvcObjs_ObjectIdentity=ObjectIdentity
cfrSvcObjs=_CfrSvcObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,4))
_CfrSvcTable_Object=MibTable
cfrSvcTable=_CfrSvcTable_Object((1,3,6,1,4,1,9,9,49,1,4,1))
if mibBuilder.loadTexts:cfrSvcTable.setStatus(_B)
_CfrSvcEntry_Object=MibTableRow
cfrSvcEntry=_CfrSvcEntry_Object((1,3,6,1,4,1,9,9,49,1,4,1,1))
cfrSvcEntry.setIndexNames((0,_G,_L),(0,_G,_K))
if mibBuilder.loadTexts:cfrSvcEntry.setStatus(_B)
class _CfrSvcAddrLocal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CfrSvcAddrLocal_Type.__name__=_V
_CfrSvcAddrLocal_Object=MibTableColumn
cfrSvcAddrLocal=_CfrSvcAddrLocal_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,1),_CfrSvcAddrLocal_Type())
cfrSvcAddrLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcAddrLocal.setStatus(_B)
class _CfrSvcAddrRemote_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CfrSvcAddrRemote_Type.__name__=_V
_CfrSvcAddrRemote_Object=MibTableColumn
cfrSvcAddrRemote=_CfrSvcAddrRemote_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,2),_CfrSvcAddrRemote_Type())
cfrSvcAddrRemote.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcAddrRemote.setStatus(_B)
class _CfrSvcThroughputIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_CfrSvcThroughputIn_Type.__name__=_D
_CfrSvcThroughputIn_Object=MibTableColumn
cfrSvcThroughputIn=_CfrSvcThroughputIn_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,3),_CfrSvcThroughputIn_Type())
cfrSvcThroughputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcThroughputIn.setStatus(_B)
if mibBuilder.loadTexts:cfrSvcThroughputIn.setUnits(_J)
class _CfrSvcMinThruputOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_CfrSvcMinThruputOut_Type.__name__=_D
_CfrSvcMinThruputOut_Object=MibTableColumn
cfrSvcMinThruputOut=_CfrSvcMinThruputOut_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,4),_CfrSvcMinThruputOut_Type())
cfrSvcMinThruputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcMinThruputOut.setStatus(_H)
if mibBuilder.loadTexts:cfrSvcMinThruputOut.setUnits(_J)
class _CfrSvcMinThruputIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_CfrSvcMinThruputIn_Type.__name__=_D
_CfrSvcMinThruputIn_Object=MibTableColumn
cfrSvcMinThruputIn=_CfrSvcMinThruputIn_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,5),_CfrSvcMinThruputIn_Type())
cfrSvcMinThruputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcMinThruputIn.setStatus(_H)
if mibBuilder.loadTexts:cfrSvcMinThruputIn.setUnits(_J)
class _CfrSvcCommitBurstIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_CfrSvcCommitBurstIn_Type.__name__=_D
_CfrSvcCommitBurstIn_Object=MibTableColumn
cfrSvcCommitBurstIn=_CfrSvcCommitBurstIn_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,6),_CfrSvcCommitBurstIn_Type())
cfrSvcCommitBurstIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcCommitBurstIn.setStatus(_B)
class _CfrSvcExcessBurstIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,2440000))
_CfrSvcExcessBurstIn_Type.__name__=_D
_CfrSvcExcessBurstIn_Object=MibTableColumn
cfrSvcExcessBurstIn=_CfrSvcExcessBurstIn_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,7),_CfrSvcExcessBurstIn_Type())
cfrSvcExcessBurstIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcExcessBurstIn.setStatus(_B)
_CfrSvcIdleTime_Type=Integer32
_CfrSvcIdleTime_Object=MibTableColumn
cfrSvcIdleTime=_CfrSvcIdleTime_Object((1,3,6,1,4,1,9,9,49,1,4,1,1,8),_CfrSvcIdleTime_Type())
cfrSvcIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrSvcIdleTime.setStatus(_B)
if mibBuilder.loadTexts:cfrSvcIdleTime.setUnits('seconds')
_CfrElmiObjs_ObjectIdentity=ObjectIdentity
cfrElmiObjs=_CfrElmiObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,5))
_CfrElmiIpAddr_Type=IpAddress
_CfrElmiIpAddr_Object=MibScalar
cfrElmiIpAddr=_CfrElmiIpAddr_Object((1,3,6,1,4,1,9,9,49,1,5,1),_CfrElmiIpAddr_Type())
cfrElmiIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiIpAddr.setStatus(_B)
_CfrElmiTable_Object=MibTable
cfrElmiTable=_CfrElmiTable_Object((1,3,6,1,4,1,9,9,49,1,5,2))
if mibBuilder.loadTexts:cfrElmiTable.setStatus(_B)
_CfrElmiEntry_Object=MibTableRow
cfrElmiEntry=_CfrElmiEntry_Object((1,3,6,1,4,1,9,9,49,1,5,2,1))
cfrElmiEntry.setIndexNames((0,_A8,_A9))
if mibBuilder.loadTexts:cfrElmiEntry.setStatus(_B)
class _CfrElmiLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CfrElmiLinkStatus_Type.__name__=_D
_CfrElmiLinkStatus_Object=MibTableColumn
cfrElmiLinkStatus=_CfrElmiLinkStatus_Object((1,3,6,1,4,1,9,9,49,1,5,2,1,1),_CfrElmiLinkStatus_Type())
cfrElmiLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiLinkStatus.setStatus(_B)
class _CfrElmiArStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CfrElmiArStatus_Type.__name__=_D
_CfrElmiArStatus_Object=MibTableColumn
cfrElmiArStatus=_CfrElmiArStatus_Object((1,3,6,1,4,1,9,9,49,1,5,2,1,2),_CfrElmiArStatus_Type())
cfrElmiArStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiArStatus.setStatus(_B)
class _CfrElmiRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CfrElmiRemoteStatus_Type.__name__=_D
_CfrElmiRemoteStatus_Object=MibTableColumn
cfrElmiRemoteStatus=_CfrElmiRemoteStatus_Object((1,3,6,1,4,1,9,9,49,1,5,2,1,3),_CfrElmiRemoteStatus_Type())
cfrElmiRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiRemoteStatus.setStatus(_B)
_CfrElmiNeighborTable_Object=MibTable
cfrElmiNeighborTable=_CfrElmiNeighborTable_Object((1,3,6,1,4,1,9,9,49,1,5,3))
if mibBuilder.loadTexts:cfrElmiNeighborTable.setStatus(_B)
_CfrElmiNeighborEntry_Object=MibTableRow
cfrElmiNeighborEntry=_CfrElmiNeighborEntry_Object((1,3,6,1,4,1,9,9,49,1,5,3,1))
cfrElmiNeighborEntry.setIndexNames((0,_A8,_A9))
if mibBuilder.loadTexts:cfrElmiNeighborEntry.setStatus(_B)
class _CfrElmiNeighborArStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notsupported',1),(_W,2),(_X,3)))
_CfrElmiNeighborArStatus_Type.__name__=_D
_CfrElmiNeighborArStatus_Object=MibTableColumn
cfrElmiNeighborArStatus=_CfrElmiNeighborArStatus_Object((1,3,6,1,4,1,9,9,49,1,5,3,1,1),_CfrElmiNeighborArStatus_Type())
cfrElmiNeighborArStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiNeighborArStatus.setStatus(_B)
_CfrElmiNeighborIpAddress_Type=IpAddress
_CfrElmiNeighborIpAddress_Object=MibTableColumn
cfrElmiNeighborIpAddress=_CfrElmiNeighborIpAddress_Object((1,3,6,1,4,1,9,9,49,1,5,3,1,2),_CfrElmiNeighborIpAddress_Type())
cfrElmiNeighborIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiNeighborIpAddress.setStatus(_B)
_CfrElmiNeighborIfIndex_Type=InterfaceIndex
_CfrElmiNeighborIfIndex_Object=MibTableColumn
cfrElmiNeighborIfIndex=_CfrElmiNeighborIfIndex_Object((1,3,6,1,4,1,9,9,49,1,5,3,1,3),_CfrElmiNeighborIfIndex_Type())
cfrElmiNeighborIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiNeighborIfIndex.setStatus(_B)
_CfrElmiNeighborVendorName_Type=DisplayString
_CfrElmiNeighborVendorName_Object=MibTableColumn
cfrElmiNeighborVendorName=_CfrElmiNeighborVendorName_Object((1,3,6,1,4,1,9,9,49,1,5,3,1,4),_CfrElmiNeighborVendorName_Type())
cfrElmiNeighborVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiNeighborVendorName.setStatus(_B)
_CfrElmiNeighborPlatformName_Type=DisplayString
_CfrElmiNeighborPlatformName_Object=MibTableColumn
cfrElmiNeighborPlatformName=_CfrElmiNeighborPlatformName_Object((1,3,6,1,4,1,9,9,49,1,5,3,1,5),_CfrElmiNeighborPlatformName_Type())
cfrElmiNeighborPlatformName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiNeighborPlatformName.setStatus(_B)
_CfrElmiNeighborDeviceName_Type=DisplayString
_CfrElmiNeighborDeviceName_Object=MibTableColumn
cfrElmiNeighborDeviceName=_CfrElmiNeighborDeviceName_Object((1,3,6,1,4,1,9,9,49,1,5,3,1,6),_CfrElmiNeighborDeviceName_Type())
cfrElmiNeighborDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrElmiNeighborDeviceName.setStatus(_B)
_CfrFragObjs_ObjectIdentity=ObjectIdentity
cfrFragObjs=_CfrFragObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,6))
_CfrFragTable_Object=MibTable
cfrFragTable=_CfrFragTable_Object((1,3,6,1,4,1,9,9,49,1,6,1))
if mibBuilder.loadTexts:cfrFragTable.setStatus(_B)
_CfrFragEntry_Object=MibTableRow
cfrFragEntry=_CfrFragEntry_Object((1,3,6,1,4,1,9,9,49,1,6,1,1))
cfrFragEntry.setIndexNames((0,_G,_L),(0,_G,_K))
if mibBuilder.loadTexts:cfrFragEntry.setStatus(_B)
class _CfrFragSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1600))
_CfrFragSize_Type.__name__=_D
_CfrFragSize_Object=MibTableColumn
cfrFragSize=_CfrFragSize_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,1),_CfrFragSize_Type())
cfrFragSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragSize.setStatus(_B)
if mibBuilder.loadTexts:cfrFragSize.setUnits(_F)
_CfrFragType_Type=DisplayString
_CfrFragType_Object=MibTableColumn
cfrFragType=_CfrFragType_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,2),_CfrFragType_Type())
cfrFragType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragType.setStatus(_B)
_CfrFragInPkts_Type=Counter32
_CfrFragInPkts_Object=MibTableColumn
cfrFragInPkts=_CfrFragInPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,3),_CfrFragInPkts_Type())
cfrFragInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragInPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragInPkts.setUnits(_E)
_CfrFragOutPkts_Type=Counter32
_CfrFragOutPkts_Object=MibTableColumn
cfrFragOutPkts=_CfrFragOutPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,4),_CfrFragOutPkts_Type())
cfrFragOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragOutPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragOutPkts.setUnits(_E)
_CfrFragInOctets_Type=Counter32
_CfrFragInOctets_Object=MibTableColumn
cfrFragInOctets=_CfrFragInOctets_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,5),_CfrFragInOctets_Type())
cfrFragInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragInOctets.setStatus(_B)
if mibBuilder.loadTexts:cfrFragInOctets.setUnits(_F)
_CfrFragOutOctets_Type=Counter32
_CfrFragOutOctets_Object=MibTableColumn
cfrFragOutOctets=_CfrFragOutOctets_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,6),_CfrFragOutOctets_Type())
cfrFragOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragOutOctets.setStatus(_B)
if mibBuilder.loadTexts:cfrFragOutOctets.setUnits(_F)
_CfrFragNotInPkts_Type=Counter32
_CfrFragNotInPkts_Object=MibTableColumn
cfrFragNotInPkts=_CfrFragNotInPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,7),_CfrFragNotInPkts_Type())
cfrFragNotInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragNotInPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragNotInPkts.setUnits(_E)
_CfrFragNotOutPkts_Type=Counter32
_CfrFragNotOutPkts_Object=MibTableColumn
cfrFragNotOutPkts=_CfrFragNotOutPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,8),_CfrFragNotOutPkts_Type())
cfrFragNotOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragNotOutPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragNotOutPkts.setUnits(_E)
_CfrFragNotInOctets_Type=Counter32
_CfrFragNotInOctets_Object=MibTableColumn
cfrFragNotInOctets=_CfrFragNotInOctets_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,9),_CfrFragNotInOctets_Type())
cfrFragNotInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragNotInOctets.setStatus(_B)
if mibBuilder.loadTexts:cfrFragNotInOctets.setUnits(_F)
_CfrFragNotOutOctets_Type=Counter32
_CfrFragNotOutOctets_Object=MibTableColumn
cfrFragNotOutOctets=_CfrFragNotOutOctets_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,10),_CfrFragNotOutOctets_Type())
cfrFragNotOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragNotOutOctets.setStatus(_B)
if mibBuilder.loadTexts:cfrFragNotOutOctets.setUnits(_F)
_CfrFragAssembledInPkts_Type=Counter32
_CfrFragAssembledInPkts_Object=MibTableColumn
cfrFragAssembledInPkts=_CfrFragAssembledInPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,11),_CfrFragAssembledInPkts_Type())
cfrFragAssembledInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragAssembledInPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragAssembledInPkts.setUnits(_E)
_CfrFragAssembledInOctets_Type=Counter32
_CfrFragAssembledInOctets_Object=MibTableColumn
cfrFragAssembledInOctets=_CfrFragAssembledInOctets_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,12),_CfrFragAssembledInOctets_Type())
cfrFragAssembledInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragAssembledInOctets.setStatus(_B)
if mibBuilder.loadTexts:cfrFragAssembledInOctets.setUnits(_F)
_CfrFragPreOutPkts_Type=Counter32
_CfrFragPreOutPkts_Object=MibTableColumn
cfrFragPreOutPkts=_CfrFragPreOutPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,13),_CfrFragPreOutPkts_Type())
cfrFragPreOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragPreOutPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragPreOutPkts.setUnits(_E)
_CfrFragPreOutOctets_Type=Counter32
_CfrFragPreOutOctets_Object=MibTableColumn
cfrFragPreOutOctets=_CfrFragPreOutOctets_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,14),_CfrFragPreOutOctets_Type())
cfrFragPreOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragPreOutOctets.setStatus(_B)
if mibBuilder.loadTexts:cfrFragPreOutOctets.setUnits(_F)
_CfrFragDroppedReAssembledInPkts_Type=Counter32
_CfrFragDroppedReAssembledInPkts_Object=MibTableColumn
cfrFragDroppedReAssembledInPkts=_CfrFragDroppedReAssembledInPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,15),_CfrFragDroppedReAssembledInPkts_Type())
cfrFragDroppedReAssembledInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragDroppedReAssembledInPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragDroppedReAssembledInPkts.setUnits(_E)
_CfrFragDroppedFragmentedOutPkts_Type=Counter32
_CfrFragDroppedFragmentedOutPkts_Object=MibTableColumn
cfrFragDroppedFragmentedOutPkts=_CfrFragDroppedFragmentedOutPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,16),_CfrFragDroppedFragmentedOutPkts_Type())
cfrFragDroppedFragmentedOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragDroppedFragmentedOutPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragDroppedFragmentedOutPkts.setUnits(_E)
class _CfrFragTimeoutsIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CfrFragTimeoutsIn_Type.__name__=_D
_CfrFragTimeoutsIn_Object=MibTableColumn
cfrFragTimeoutsIn=_CfrFragTimeoutsIn_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,17),_CfrFragTimeoutsIn_Type())
cfrFragTimeoutsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragTimeoutsIn.setStatus(_B)
_CfrFragOutOfSeqFragPkts_Type=Counter32
_CfrFragOutOfSeqFragPkts_Object=MibTableColumn
cfrFragOutOfSeqFragPkts=_CfrFragOutOfSeqFragPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,18),_CfrFragOutOfSeqFragPkts_Type())
cfrFragOutOfSeqFragPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragOutOfSeqFragPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragOutOfSeqFragPkts.setUnits(_E)
_CfrFragUnexpectedBBitSetPkts_Type=Counter32
_CfrFragUnexpectedBBitSetPkts_Object=MibTableColumn
cfrFragUnexpectedBBitSetPkts=_CfrFragUnexpectedBBitSetPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,19),_CfrFragUnexpectedBBitSetPkts_Type())
cfrFragUnexpectedBBitSetPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragUnexpectedBBitSetPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragUnexpectedBBitSetPkts.setUnits(_E)
_CfrFragSeqMissedPkts_Type=Counter32
_CfrFragSeqMissedPkts_Object=MibTableColumn
cfrFragSeqMissedPkts=_CfrFragSeqMissedPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,20),_CfrFragSeqMissedPkts_Type())
cfrFragSeqMissedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragSeqMissedPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragSeqMissedPkts.setUnits(_E)
_CfrFragInterleavedOutPkts_Type=Counter32
_CfrFragInterleavedOutPkts_Object=MibTableColumn
cfrFragInterleavedOutPkts=_CfrFragInterleavedOutPkts_Object((1,3,6,1,4,1,9,9,49,1,6,1,1,21),_CfrFragInterleavedOutPkts_Type())
cfrFragInterleavedOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrFragInterleavedOutPkts.setStatus(_B)
if mibBuilder.loadTexts:cfrFragInterleavedOutPkts.setUnits(_E)
_CfrConnectionObjs_ObjectIdentity=ObjectIdentity
cfrConnectionObjs=_CfrConnectionObjs_ObjectIdentity((1,3,6,1,4,1,9,9,49,1,7))
_CfrConnectionTable_Object=MibTable
cfrConnectionTable=_CfrConnectionTable_Object((1,3,6,1,4,1,9,9,49,1,7,1))
if mibBuilder.loadTexts:cfrConnectionTable.setStatus(_B)
_CfrConnectionEntry_Object=MibTableRow
cfrConnectionEntry=_CfrConnectionEntry_Object((1,3,6,1,4,1,9,9,49,1,7,1,1))
cfrConnectionEntry.setIndexNames((0,_G,_L),(0,_G,_K))
if mibBuilder.loadTexts:cfrConnectionEntry.setStatus(_B)
_CfrConnName_Type=DisplayString
_CfrConnName_Object=MibTableColumn
cfrConnName=_CfrConnName_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,1),_CfrConnName_Type())
cfrConnName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnName.setStatus(_B)
class _CfrConnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_CfrConnID_Type.__name__=_D
_CfrConnID_Object=MibTableColumn
cfrConnID=_CfrConnID_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,2),_CfrConnID_Type())
cfrConnID.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnID.setStatus(_B)
_CfrConnState_Type=DisplayString
_CfrConnState_Object=MibTableColumn
cfrConnState=_CfrConnState_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,3),_CfrConnState_Type())
cfrConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnState.setStatus(_B)
_CfrConnSegment1Name_Type=DisplayString
_CfrConnSegment1Name_Object=MibTableColumn
cfrConnSegment1Name=_CfrConnSegment1Name_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,4),_CfrConnSegment1Name_Type())
cfrConnSegment1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnSegment1Name.setStatus(_B)
_CfrConnSegment1VCGroup_Type=DisplayString
_CfrConnSegment1VCGroup_Object=MibTableColumn
cfrConnSegment1VCGroup=_CfrConnSegment1VCGroup_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,5),_CfrConnSegment1VCGroup_Type())
cfrConnSegment1VCGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnSegment1VCGroup.setStatus(_B)
_CfrConnSegment1Dlci_Type=DlciNumber
_CfrConnSegment1Dlci_Object=MibTableColumn
cfrConnSegment1Dlci=_CfrConnSegment1Dlci_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,6),_CfrConnSegment1Dlci_Type())
cfrConnSegment1Dlci.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnSegment1Dlci.setStatus(_B)
_CfrConnSegment2Name_Type=DisplayString
_CfrConnSegment2Name_Object=MibTableColumn
cfrConnSegment2Name=_CfrConnSegment2Name_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,7),_CfrConnSegment2Name_Type())
cfrConnSegment2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnSegment2Name.setStatus(_B)
class _CfrConnSegment2Vpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CfrConnSegment2Vpi_Type.__name__=_D
_CfrConnSegment2Vpi_Object=MibTableColumn
cfrConnSegment2Vpi=_CfrConnSegment2Vpi_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,8),_CfrConnSegment2Vpi_Type())
cfrConnSegment2Vpi.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnSegment2Vpi.setStatus(_B)
class _CfrConnSegment2Vci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CfrConnSegment2Vci_Type.__name__=_D
_CfrConnSegment2Vci_Object=MibTableColumn
cfrConnSegment2Vci=_CfrConnSegment2Vci_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,9),_CfrConnSegment2Vci_Type())
cfrConnSegment2Vci.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnSegment2Vci.setStatus(_B)
class _CfrConnServiceTranslation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('serviceTranslationEnabled',1),('serviceTranslationNotEnabled',2)))
_CfrConnServiceTranslation_Type.__name__=_D
_CfrConnServiceTranslation_Object=MibTableColumn
cfrConnServiceTranslation=_CfrConnServiceTranslation_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,10),_CfrConnServiceTranslation_Type())
cfrConnServiceTranslation.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnServiceTranslation.setStatus(_B)
_CfrConnFrSscsDlci_Type=DlciNumber
_CfrConnFrSscsDlci_Object=MibTableColumn
cfrConnFrSscsDlci=_CfrConnFrSscsDlci_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,11),_CfrConnFrSscsDlci_Type())
cfrConnFrSscsDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnFrSscsDlci.setStatus(_B)
class _CfrConnEfciBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mapFecn',1),('notMapFecn',2)))
_CfrConnEfciBit_Type.__name__=_D
_CfrConnEfciBit_Object=MibTableColumn
cfrConnEfciBit=_CfrConnEfciBit_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,12),_CfrConnEfciBit_Type())
cfrConnEfciBit.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnEfciBit.setStatus(_B)
class _CfrConnDeBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noMapClp',1),('mapClp',2),('setDe0',3),('setDe1',4)))
_CfrConnDeBit_Type.__name__=_D
_CfrConnDeBit_Object=MibTableColumn
cfrConnDeBit=_CfrConnDeBit_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,13),_CfrConnDeBit_Type())
cfrConnDeBit.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnDeBit.setStatus(_B)
class _CfrConnClpBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('setClpTo0AndCopyDeToFrsscsDe',1),('setClpTo1AndCopyDeToFrsscsDe',2),('copyDeToFrsscsDeAndClp',3),('copyDeToClp',4),('setClp1',5),('setClp0',6)))
_CfrConnClpBit_Type.__name__=_D
_CfrConnClpBit_Object=MibTableColumn
cfrConnClpBit=_CfrConnClpBit_Object((1,3,6,1,4,1,9,9,49,1,7,1,1,14),_CfrConnClpBit_Type())
cfrConnClpBit.setMaxAccess(_C)
if mibBuilder.loadTexts:cfrConnClpBit.setStatus(_B)
_CiscoFrMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFrMIBConformance=_CiscoFrMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,49,3))
_CiscoFrMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFrMIBCompliances=_CiscoFrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,49,3,1))
_CiscoFrMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFrMIBGroups=_CiscoFrMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,49,3,2))
frDlcmiEntry.registerAugmentions((_A,_AX))
cfrLmiEntry.setIndexNames(*frDlcmiEntry.getIndexNames())
frCircuitEntry.registerAugmentions((_A,_AY))
cfrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
frCircuitEntry.registerAugmentions((_A,_AZ))
cfrExtCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
ciscoFrMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,1))
ciscoFrMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_Aa),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_AB),(_A,_AC),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoFrMIBGroup.setStatus(_H)
ciscoFrMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,2))
ciscoFrMIBGroupRev1.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A1),(_A,_A2),(_A,_M),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_AD),(_A,_AE),(_A,_v),(_A,_w),(_A,_x),(_A,_AB),(_A,_AC),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoFrMIBGroupRev1.setStatus(_H)
ciscoFrLmiMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,3))
ciscoFrLmiMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoFrLmiMIBGroup.setStatus(_B)
ciscoFrCircuitMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,4))
ciscoFrCircuitMIBGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoFrCircuitMIBGroup.setStatus(_B)
ciscoExtCircuitMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,5))
ciscoExtCircuitMIBGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A1),(_A,_A2),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:ciscoExtCircuitMIBGroup.setStatus(_H)
ciscoFrTsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,6))
ciscoFrTsMIBGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:ciscoFrTsMIBGroup.setStatus(_B)
ciscoFrMapMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,7))
ciscoFrMapMIBGroup.setObjects(*((_A,_M),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoFrMapMIBGroup.setStatus(_B)
ciscoFrSvcMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,8))
ciscoFrSvcMIBGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoFrSvcMIBGroup.setStatus(_B)
ciscoFrElmiMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,9))
ciscoFrElmiMIBGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:ciscoFrElmiMIBGroup.setStatus(_H)
ciscoFrElmiMIBGroup1=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,10))
ciscoFrElmiMIBGroup1.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_Ak)))
if mibBuilder.loadTexts:ciscoFrElmiMIBGroup1.setStatus(_B)
ciscoFrFragMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,11))
ciscoFrFragMIBGroup.setObjects(*((_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4)))
if mibBuilder.loadTexts:ciscoFrFragMIBGroup.setStatus(_B)
ciscoFrConnMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,12))
ciscoFrConnMIBGroup.setObjects(*((_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI)))
if mibBuilder.loadTexts:ciscoFrConnMIBGroup.setStatus(_B)
ciscoExtCircuitMIBGroup1=ObjectGroup((1,3,6,1,4,1,9,9,49,3,2,13))
ciscoExtCircuitMIBGroup1.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A1),(_A,_A2),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM)))
if mibBuilder.loadTexts:ciscoExtCircuitMIBGroup1.setStatus(_B)
ciscoFrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,49,3,1,1))
ciscoFrMIBCompliance.setObjects((_A,_BN))
if mibBuilder.loadTexts:ciscoFrMIBCompliance.setStatus(_AV)
ciscoFrMIBCompliancesRev1=ModuleCompliance((1,3,6,1,4,1,9,9,49,3,1,2))
ciscoFrMIBCompliancesRev1.setObjects((_A,_BO))
if mibBuilder.loadTexts:ciscoFrMIBCompliancesRev1.setStatus(_AV)
ciscoFrMIBCompliancesRev2=ModuleCompliance((1,3,6,1,4,1,9,9,49,3,1,3))
ciscoFrMIBCompliancesRev2.setObjects(*((_A,_A3),(_A,_A4),(_A,_AW),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:ciscoFrMIBCompliancesRev2.setStatus(_AV)
ciscoFrMIBCompliancesRev3=ModuleCompliance((1,3,6,1,4,1,9,9,49,3,1,4))
ciscoFrMIBCompliancesRev3.setObjects(*((_A,_A3),(_A,_A4),(_A,_AW),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_BP)))
if mibBuilder.loadTexts:ciscoFrMIBCompliancesRev3.setStatus(_H)
ciscoFrMIBCompliancesRev4=ModuleCompliance((1,3,6,1,4,1,9,9,49,3,1,5))
ciscoFrMIBCompliancesRev4.setObjects(*((_A,_A3),(_A,_A4),(_A,_BQ),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_BR),(_A,_BS),(_A,_BT)))
if mibBuilder.loadTexts:ciscoFrMIBCompliancesRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DlciNumber':DlciNumber,'CfrMapProtocols':CfrMapProtocols,'ciscoFrameRelayMIB':ciscoFrameRelayMIB,'ciscoFrMIBObjects':ciscoFrMIBObjects,'cfrLmiObjs':cfrLmiObjs,'cfrLmiTable':cfrLmiTable,_AX:cfrLmiEntry,_Y:cfrLmiLinkstatus,_Z:cfrLmiLinkType,_a:cfrLmiEnquiryIns,_b:cfrLmiEnquiryOuts,_c:cfrLmiStatusIns,_d:cfrLmiStatusOuts,_e:cfrLmiUpdateStatusIns,_f:cfrLmiUpdateStatusOuts,_g:cfrLmiStatusTimeouts,_h:cfrLmiStatusEnqTimeouts,_i:cfrLmiN392Dce,_j:cfrLmiN393Dce,_k:cfrLmiT392Dce,'cfrCircuitObjs':cfrCircuitObjs,'cfrCircuitTable':cfrCircuitTable,_AY:cfrCircuitEntry,_l:cfrCircuitDEins,_m:cfrCircuitDEouts,_n:cfrCircuitDropPktsOuts,_o:cfrCircuitType,'cfrExtCircuitTable':cfrExtCircuitTable,_AZ:cfrExtCircuitEntry,_N:cfrExtCircuitIfName,_O:cfrExtCircuitIfType,_P:cfrExtCircuitSubifIndex,_Q:cfrExtCircuitMapStatus,_R:cfrExtCircuitCreateType,_S:cfrExtCircuitMulticast,_T:cfrExtCircuitRoutedDlci,_U:cfrExtCircuitRoutedIf,_A1:cfrExtCircuitUncompressIns,_A2:cfrExtCircuitUncompressOuts,_AF:cfrExtCircuitFECNOuts,_AG:cfrExtCircuitBECNOuts,_AH:cfrExtCircuitMinThruputOut,_AI:cfrExtCircuitMinThruputIn,_AJ:cfrExtCircuitBcastPktOuts,_AK:cfrExtCircuitBcastByteOuts,_AL:cfrExtCircuitBandwidth,_Ab:cfrExtCircuitShapeByteLimit,_Ac:cfrExtCircuitShapeInterval,_Ad:cfrExtCircuitShapeByteIncrement,_Ae:cfrExtCircuitShapePkts,_Af:cfrExtCircuitShapeBytes,_Ag:cfrExtCircuitShapePktsDelay,_Ah:cfrExtCircuitShapeBytesDelay,_Ai:cfrExtCircuitShapeActive,_Aj:cfrExtCircuitShapeAdapting,_BJ:cfrExtCircuitTxDataRate,_BK:cfrExtCircuitTxPktRate,_BL:cfrExtCircuitRcvDataRate,_BM:cfrExtCircuitRcvPktRate,'cfrMapObjs':cfrMapObjs,'cfrMapTable':cfrMapTable,'cfrMapEntry':cfrMapEntry,_M:cfrMapIndex,_p:cfrMapProtocol,_q:cfrMapAddress,_r:cfrMapType,_s:cfrMapEncaps,_t:cfrMapBroadcast,_Aa:cfrMapPayloadCompress,_u:cfrMapTcpHdrCompress,_AD:cfrMapRtpHdrCompress,_AE:cfrMapPayloadCompressType,'cfrSvcObjs':cfrSvcObjs,'cfrSvcTable':cfrSvcTable,'cfrSvcEntry':cfrSvcEntry,_v:cfrSvcAddrLocal,_w:cfrSvcAddrRemote,_x:cfrSvcThroughputIn,_AB:cfrSvcMinThruputOut,_AC:cfrSvcMinThruputIn,_y:cfrSvcCommitBurstIn,_z:cfrSvcExcessBurstIn,_A0:cfrSvcIdleTime,'cfrElmiObjs':cfrElmiObjs,_AM:cfrElmiIpAddr,'cfrElmiTable':cfrElmiTable,'cfrElmiEntry':cfrElmiEntry,_Ak:cfrElmiLinkStatus,_AN:cfrElmiArStatus,_AO:cfrElmiRemoteStatus,'cfrElmiNeighborTable':cfrElmiNeighborTable,'cfrElmiNeighborEntry':cfrElmiNeighborEntry,_AP:cfrElmiNeighborArStatus,_AQ:cfrElmiNeighborIpAddress,_AR:cfrElmiNeighborIfIndex,_AS:cfrElmiNeighborVendorName,_AT:cfrElmiNeighborPlatformName,_AU:cfrElmiNeighborDeviceName,'cfrFragObjs':cfrFragObjs,'cfrFragTable':cfrFragTable,'cfrFragEntry':cfrFragEntry,_Al:cfrFragSize,_Am:cfrFragType,_An:cfrFragInPkts,_Ao:cfrFragOutPkts,_Ap:cfrFragInOctets,_Aq:cfrFragOutOctets,_Ar:cfrFragNotInPkts,_As:cfrFragNotOutPkts,_At:cfrFragNotInOctets,_Au:cfrFragNotOutOctets,_Av:cfrFragAssembledInPkts,_Aw:cfrFragAssembledInOctets,_Ax:cfrFragPreOutPkts,_Ay:cfrFragPreOutOctets,_Az:cfrFragDroppedReAssembledInPkts,_A_:cfrFragDroppedFragmentedOutPkts,_B0:cfrFragTimeoutsIn,_B1:cfrFragOutOfSeqFragPkts,_B2:cfrFragUnexpectedBBitSetPkts,_B3:cfrFragSeqMissedPkts,_B4:cfrFragInterleavedOutPkts,'cfrConnectionObjs':cfrConnectionObjs,'cfrConnectionTable':cfrConnectionTable,'cfrConnectionEntry':cfrConnectionEntry,_B5:cfrConnName,_B6:cfrConnID,_B7:cfrConnState,_B8:cfrConnSegment1Name,_B9:cfrConnSegment1VCGroup,_BA:cfrConnSegment1Dlci,_BB:cfrConnSegment2Name,_BC:cfrConnSegment2Vpi,_BD:cfrConnSegment2Vci,_BE:cfrConnServiceTranslation,_BF:cfrConnFrSscsDlci,_BG:cfrConnEfciBit,_BH:cfrConnDeBit,_BI:cfrConnClpBit,'ciscoFrMIBConformance':ciscoFrMIBConformance,'ciscoFrMIBCompliances':ciscoFrMIBCompliances,'ciscoFrMIBCompliance':ciscoFrMIBCompliance,'ciscoFrMIBCompliancesRev1':ciscoFrMIBCompliancesRev1,'ciscoFrMIBCompliancesRev2':ciscoFrMIBCompliancesRev2,'ciscoFrMIBCompliancesRev3':ciscoFrMIBCompliancesRev3,'ciscoFrMIBCompliancesRev4':ciscoFrMIBCompliancesRev4,'ciscoFrMIBGroups':ciscoFrMIBGroups,_BN:ciscoFrMIBGroup,_BO:ciscoFrMIBGroupRev1,_A3:ciscoFrLmiMIBGroup,_A4:ciscoFrCircuitMIBGroup,_AW:ciscoExtCircuitMIBGroup,_A5:ciscoFrTsMIBGroup,_A6:ciscoFrMapMIBGroup,_A7:ciscoFrSvcMIBGroup,_BP:ciscoFrElmiMIBGroup,_BR:ciscoFrElmiMIBGroup1,_BS:ciscoFrFragMIBGroup,_BT:ciscoFrConnMIBGroup,_BQ:ciscoExtCircuitMIBGroup1})