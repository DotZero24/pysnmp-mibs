_BT='fsFrConnMIBGroup'
_BS='fsFrFragMIBGroup'
_BR='fsFrElmiMIBGroup1'
_BQ='fsExtCircuitMIBGroup1'
_BP='fsFrElmiMIBGroup'
_BO='fsFrMIBGroupRev1'
_BN='fsFrMIBGroup'
_BM='fsfrExtCircuitRcvPktRate'
_BL='fsfrExtCircuitRcvDataRate'
_BK='fsfrExtCircuitTxPktRate'
_BJ='fsfrExtCircuitTxDataRate'
_BI='fsfrConnClpBit'
_BH='fsfrConnDeBit'
_BG='fsfrConnEfciBit'
_BF='fsfrConnFrSscsDlci'
_BE='fsfrConnServiceTranslation'
_BD='fsfrConnSegment2Vci'
_BC='fsfrConnSegment2Vpi'
_BB='fsfrConnSegment2Name'
_BA='fsfrConnSegment1Dlci'
_B9='fsfrConnSegment1VCGroup'
_B8='fsfrConnSegment1Name'
_B7='fsfrConnState'
_B6='fsfrConnID'
_B5='fsfrConnName'
_B4='fsfrFragInterleavedOutPkts'
_B3='fsfrFragSeqMissedPkts'
_B2='fsfrFragUnexpectedBBitSetPkts'
_B1='fsfrFragOutOfSeqFragPkts'
_B0='fsfrFragTimeoutsIn'
_A_='fsfrFragDroppedFragmentedOutPkts'
_Az='fsfrFragDroppedReAssembledInPkts'
_Ay='fsfrFragPreOutOctets'
_Ax='fsfrFragPreOutPkts'
_Aw='fsfrFragAssembledInOctets'
_Av='fsfrFragAssembledInPkts'
_Au='fsfrFragNotOutOctets'
_At='fsfrFragNotInOctets'
_As='fsfrFragNotOutPkts'
_Ar='fsfrFragNotInPkts'
_Aq='fsfrFragOutOctets'
_Ap='fsfrFragInOctets'
_Ao='fsfrFragOutPkts'
_An='fsfrFragInPkts'
_Am='fsfrFragType'
_Al='fsfrFragSize'
_Ak='fsfrElmiLinkStatus'
_Aj='fsfrExtCircuitShapeAdapting'
_Ai='fsfrExtCircuitShapeActive'
_Ah='fsfrExtCircuitShapeBytesDelay'
_Ag='fsfrExtCircuitShapePktsDelay'
_Af='fsfrExtCircuitShapeBytes'
_Ae='fsfrExtCircuitShapePkts'
_Ad='fsfrExtCircuitShapeByteIncrement'
_Ac='fsfrExtCircuitShapeInterval'
_Ab='fsfrExtCircuitShapeByteLimit'
_Aa='fsfrMapPayloadCompress'
_AZ='fsfrExtCircuitEntry'
_AY='fsfrCircuitEntry'
_AX='fsfrLmiEntry'
_AW='fsExtCircuitMIBGroup'
_AV='obsolete'
_AU='fsfrElmiNeighborDeviceName'
_AT='fsfrElmiNeighborPlatformName'
_AS='fsfrElmiNeighborVendorName'
_AR='fsfrElmiNeighborIfIndex'
_AQ='fsfrElmiNeighborIpAddress'
_AP='fsfrElmiNeighborArStatus'
_AO='fsfrElmiRemoteStatus'
_AN='fsfrElmiArStatus'
_AM='fsfrElmiIpAddr'
_AL='fsfrExtCircuitBandwidth'
_AK='fsfrExtCircuitBcastByteOuts'
_AJ='fsfrExtCircuitBcastPktOuts'
_AI='fsfrExtCircuitMinThruputIn'
_AH='fsfrExtCircuitMinThruputOut'
_AG='fsfrExtCircuitBECNOuts'
_AF='fsfrExtCircuitFECNOuts'
_AE='fsfrMapPayloadCompressType'
_AD='fsfrMapRtpHdrCompress'
_AC='fsfrSvcMinThruputIn'
_AB='fsfrSvcMinThruputOut'
_AA='inapplicable'
_A9='ifIndex'
_A8='IF-MIB'
_A7='fsFrSvcMIBGroup'
_A6='fsFrMapMIBGroup'
_A5='fsFrTsMIBGroup'
_A4='fsFrCircuitMIBGroup'
_A3='fsFrLmiMIBGroup'
_A2='fsfrExtCircuitUncompressOuts'
_A1='fsfrExtCircuitUncompressIns'
_A0='fsfrSvcIdleTime'
_z='fsfrSvcExcessBurstIn'
_y='fsfrSvcCommitBurstIn'
_x='fsfrSvcThroughputIn'
_w='fsfrSvcAddrRemote'
_v='fsfrSvcAddrLocal'
_u='fsfrMapTcpHdrCompress'
_t='fsfrMapBroadcast'
_s='fsfrMapEncaps'
_r='fsfrMapType'
_q='fsfrMapAddress'
_p='fsfrMapProtocol'
_o='fsfrCircuitType'
_n='fsfrCircuitDropPktsOuts'
_m='fsfrCircuitDEouts'
_l='fsfrCircuitDEins'
_k='fsfrLmiT392Dce'
_j='fsfrLmiN393Dce'
_i='fsfrLmiN392Dce'
_h='fsfrLmiStatusEnqTimeouts'
_g='fsfrLmiStatusTimeouts'
_f='fsfrLmiUpdateStatusOuts'
_e='fsfrLmiUpdateStatusIns'
_d='fsfrLmiStatusOuts'
_c='fsfrLmiStatusIns'
_b='fsfrLmiEnquiryOuts'
_a='fsfrLmiEnquiryIns'
_Z='fsfrLmiLinkType'
_Y='fsfrLmiLinkstatus'
_X='disabled'
_W='enabled'
_V='OctetString'
_U='fsfrExtCircuitRoutedIf'
_T='fsfrExtCircuitRoutedDlci'
_S='fsfrExtCircuitMulticast'
_R='fsfrExtCircuitCreateType'
_Q='fsfrExtCircuitMapStatus'
_P='fsfrExtCircuitSubifIndex'
_O='fsfrExtCircuitIfType'
_N='fsfrExtCircuitIfName'
_M='fsfrMapIndex'
_L='frCircuitIfIndex'
_K='frCircuitDlci'
_J='bits per second'
_I='messages'
_H='deprecated'
_G='FRAME-RELAY-DTE-MIB'
_F='octets'
_E='packets'
_D='Integer32'
_C='read-only'
_B='current'
_A='FS-FRAME-RELAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
frCircuitDlci,frCircuitEntry,frCircuitIfIndex,frDlcmiEntry=mibBuilder.importSymbols(_G,_K,'frCircuitEntry',_L,'frDlcmiEntry')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_A8,'InterfaceIndex',_A9)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsFrameRelayMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,50))
if mibBuilder.loadTexts:fsFrameRelayMIB.setRevisions(('2000-10-13 00:00','2000-05-22 00:00','2000-05-16 00:00','2009-05-18 00:00','1999-08-21 00:00','1996-08-15 00:00'))
class DlciNumber(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
class FSfrMapProtocols(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7,10,11,12,13,16,18,22,25,37,38,39,40,47,48,49,53,63,74,83,999)));namedValues=NamedValues(*(('arp',1),('serialArp',6),('ip',7),('xns',10),('novell',11),('apollo',12),('vines',13),('appletalk',16),('ieeeSpanning',18),('decnet',22),('clns',25),('rsrb',37),('bridge',38),('stun',39),('frArp',40),('uncompressedTcp',47),('compressedTcp',48),('llc2',49),('frSwitch',53),('dlsw',63),('nhrp',74),('compressedRtp',83),('wildcard',999)))
_FsFrMIBObjects_ObjectIdentity=ObjectIdentity
fsFrMIBObjects=_FsFrMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1))
_FsfrLmiObjs_ObjectIdentity=ObjectIdentity
fsfrLmiObjs=_FsfrLmiObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,1))
_FsfrLmiTable_Object=MibTable
fsfrLmiTable=_FsfrLmiTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1))
if mibBuilder.loadTexts:fsfrLmiTable.setStatus(_B)
_FsfrLmiEntry_Object=MibTableRow
fsfrLmiEntry=_FsfrLmiEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1))
if mibBuilder.loadTexts:fsfrLmiEntry.setStatus(_B)
class _FsfrLmiLinkstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsfrLmiLinkstatus_Type.__name__=_D
_FsfrLmiLinkstatus_Object=MibTableColumn
fsfrLmiLinkstatus=_FsfrLmiLinkstatus_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,1),_FsfrLmiLinkstatus_Type())
fsfrLmiLinkstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiLinkstatus.setStatus(_B)
class _FsfrLmiLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('nni',3)))
_FsfrLmiLinkType_Type.__name__=_D
_FsfrLmiLinkType_Object=MibTableColumn
fsfrLmiLinkType=_FsfrLmiLinkType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,2),_FsfrLmiLinkType_Type())
fsfrLmiLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiLinkType.setStatus(_B)
_FsfrLmiEnquiryIns_Type=Counter32
_FsfrLmiEnquiryIns_Object=MibTableColumn
fsfrLmiEnquiryIns=_FsfrLmiEnquiryIns_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,3),_FsfrLmiEnquiryIns_Type())
fsfrLmiEnquiryIns.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiEnquiryIns.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiEnquiryIns.setUnits(_I)
_FsfrLmiEnquiryOuts_Type=Counter32
_FsfrLmiEnquiryOuts_Object=MibTableColumn
fsfrLmiEnquiryOuts=_FsfrLmiEnquiryOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,4),_FsfrLmiEnquiryOuts_Type())
fsfrLmiEnquiryOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiEnquiryOuts.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiEnquiryOuts.setUnits(_I)
_FsfrLmiStatusIns_Type=Counter32
_FsfrLmiStatusIns_Object=MibTableColumn
fsfrLmiStatusIns=_FsfrLmiStatusIns_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,5),_FsfrLmiStatusIns_Type())
fsfrLmiStatusIns.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiStatusIns.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiStatusIns.setUnits(_I)
_FsfrLmiStatusOuts_Type=Counter32
_FsfrLmiStatusOuts_Object=MibTableColumn
fsfrLmiStatusOuts=_FsfrLmiStatusOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,6),_FsfrLmiStatusOuts_Type())
fsfrLmiStatusOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiStatusOuts.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiStatusOuts.setUnits(_I)
_FsfrLmiUpdateStatusIns_Type=Counter32
_FsfrLmiUpdateStatusIns_Object=MibTableColumn
fsfrLmiUpdateStatusIns=_FsfrLmiUpdateStatusIns_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,7),_FsfrLmiUpdateStatusIns_Type())
fsfrLmiUpdateStatusIns.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiUpdateStatusIns.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiUpdateStatusIns.setUnits(_I)
_FsfrLmiUpdateStatusOuts_Type=Counter32
_FsfrLmiUpdateStatusOuts_Object=MibTableColumn
fsfrLmiUpdateStatusOuts=_FsfrLmiUpdateStatusOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,8),_FsfrLmiUpdateStatusOuts_Type())
fsfrLmiUpdateStatusOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiUpdateStatusOuts.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiUpdateStatusOuts.setUnits(_I)
_FsfrLmiStatusTimeouts_Type=Counter32
_FsfrLmiStatusTimeouts_Object=MibTableColumn
fsfrLmiStatusTimeouts=_FsfrLmiStatusTimeouts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,9),_FsfrLmiStatusTimeouts_Type())
fsfrLmiStatusTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiStatusTimeouts.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiStatusTimeouts.setUnits('times')
_FsfrLmiStatusEnqTimeouts_Type=Counter32
_FsfrLmiStatusEnqTimeouts_Object=MibTableColumn
fsfrLmiStatusEnqTimeouts=_FsfrLmiStatusEnqTimeouts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,10),_FsfrLmiStatusEnqTimeouts_Type())
fsfrLmiStatusEnqTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiStatusEnqTimeouts.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiStatusEnqTimeouts.setUnits('times')
class _FsfrLmiN392Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsfrLmiN392Dce_Type.__name__=_D
_FsfrLmiN392Dce_Object=MibTableColumn
fsfrLmiN392Dce=_FsfrLmiN392Dce_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,11),_FsfrLmiN392Dce_Type())
fsfrLmiN392Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiN392Dce.setStatus(_B)
class _FsfrLmiN393Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsfrLmiN393Dce_Type.__name__=_D
_FsfrLmiN393Dce_Object=MibTableColumn
fsfrLmiN393Dce=_FsfrLmiN393Dce_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,12),_FsfrLmiN393Dce_Type())
fsfrLmiN393Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiN393Dce.setStatus(_B)
class _FsfrLmiT392Dce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_FsfrLmiT392Dce_Type.__name__=_D
_FsfrLmiT392Dce_Object=MibTableColumn
fsfrLmiT392Dce=_FsfrLmiT392Dce_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,1,1,1,13),_FsfrLmiT392Dce_Type())
fsfrLmiT392Dce.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrLmiT392Dce.setStatus(_B)
if mibBuilder.loadTexts:fsfrLmiT392Dce.setUnits('seconds')
_FsfrCircuitObjs_ObjectIdentity=ObjectIdentity
fsfrCircuitObjs=_FsfrCircuitObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,2))
_FsfrCircuitTable_Object=MibTable
fsfrCircuitTable=_FsfrCircuitTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,1))
if mibBuilder.loadTexts:fsfrCircuitTable.setStatus(_B)
_FsfrCircuitEntry_Object=MibTableRow
fsfrCircuitEntry=_FsfrCircuitEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,1,1))
if mibBuilder.loadTexts:fsfrCircuitEntry.setStatus(_B)
_FsfrCircuitDEins_Type=Counter32
_FsfrCircuitDEins_Object=MibTableColumn
fsfrCircuitDEins=_FsfrCircuitDEins_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,1,1,1),_FsfrCircuitDEins_Type())
fsfrCircuitDEins.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrCircuitDEins.setStatus(_B)
if mibBuilder.loadTexts:fsfrCircuitDEins.setUnits(_E)
_FsfrCircuitDEouts_Type=Counter32
_FsfrCircuitDEouts_Object=MibTableColumn
fsfrCircuitDEouts=_FsfrCircuitDEouts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,1,1,2),_FsfrCircuitDEouts_Type())
fsfrCircuitDEouts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrCircuitDEouts.setStatus(_B)
if mibBuilder.loadTexts:fsfrCircuitDEouts.setUnits(_E)
_FsfrCircuitDropPktsOuts_Type=Counter32
_FsfrCircuitDropPktsOuts_Object=MibTableColumn
fsfrCircuitDropPktsOuts=_FsfrCircuitDropPktsOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,1,1,3),_FsfrCircuitDropPktsOuts_Type())
fsfrCircuitDropPktsOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrCircuitDropPktsOuts.setStatus(_B)
if mibBuilder.loadTexts:fsfrCircuitDropPktsOuts.setUnits(_E)
class _FsfrCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('svc',2)))
_FsfrCircuitType_Type.__name__=_D
_FsfrCircuitType_Object=MibTableColumn
fsfrCircuitType=_FsfrCircuitType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,1,1,4),_FsfrCircuitType_Type())
fsfrCircuitType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrCircuitType.setStatus(_B)
_FsfrExtCircuitTable_Object=MibTable
fsfrExtCircuitTable=_FsfrExtCircuitTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2))
if mibBuilder.loadTexts:fsfrExtCircuitTable.setStatus(_B)
_FsfrExtCircuitEntry_Object=MibTableRow
fsfrExtCircuitEntry=_FsfrExtCircuitEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1))
if mibBuilder.loadTexts:fsfrExtCircuitEntry.setStatus(_B)
_FsfrExtCircuitIfName_Type=DisplayString
_FsfrExtCircuitIfName_Object=MibTableColumn
fsfrExtCircuitIfName=_FsfrExtCircuitIfName_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,1),_FsfrExtCircuitIfName_Type())
fsfrExtCircuitIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitIfName.setStatus(_B)
class _FsfrExtCircuitIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mainInterface',1),('pointToPoint',2),('multipoint',3)))
_FsfrExtCircuitIfType_Type.__name__=_D
_FsfrExtCircuitIfType_Object=MibTableColumn
fsfrExtCircuitIfType=_FsfrExtCircuitIfType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,2),_FsfrExtCircuitIfType_Type())
fsfrExtCircuitIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitIfType.setStatus(_B)
_FsfrExtCircuitSubifIndex_Type=InterfaceIndex
_FsfrExtCircuitSubifIndex_Object=MibTableColumn
fsfrExtCircuitSubifIndex=_FsfrExtCircuitSubifIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,3),_FsfrExtCircuitSubifIndex_Type())
fsfrExtCircuitSubifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitSubifIndex.setStatus(_B)
class _FsfrExtCircuitMapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_FsfrExtCircuitMapStatus_Type.__name__=_D
_FsfrExtCircuitMapStatus_Object=MibTableColumn
fsfrExtCircuitMapStatus=_FsfrExtCircuitMapStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,4),_FsfrExtCircuitMapStatus_Type())
fsfrExtCircuitMapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitMapStatus.setStatus(_B)
class _FsfrExtCircuitCreateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_FsfrExtCircuitCreateType_Type.__name__=_D
_FsfrExtCircuitCreateType_Object=MibTableColumn
fsfrExtCircuitCreateType=_FsfrExtCircuitCreateType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,5),_FsfrExtCircuitCreateType_Type())
fsfrExtCircuitCreateType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitCreateType.setStatus(_B)
_FsfrExtCircuitMulticast_Type=TruthValue
_FsfrExtCircuitMulticast_Object=MibTableColumn
fsfrExtCircuitMulticast=_FsfrExtCircuitMulticast_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,6),_FsfrExtCircuitMulticast_Type())
fsfrExtCircuitMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitMulticast.setStatus(_B)
_FsfrExtCircuitRoutedDlci_Type=DlciNumber
_FsfrExtCircuitRoutedDlci_Object=MibTableColumn
fsfrExtCircuitRoutedDlci=_FsfrExtCircuitRoutedDlci_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,7),_FsfrExtCircuitRoutedDlci_Type())
fsfrExtCircuitRoutedDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitRoutedDlci.setStatus(_B)
_FsfrExtCircuitRoutedIf_Type=InterfaceIndex
_FsfrExtCircuitRoutedIf_Object=MibTableColumn
fsfrExtCircuitRoutedIf=_FsfrExtCircuitRoutedIf_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,8),_FsfrExtCircuitRoutedIf_Type())
fsfrExtCircuitRoutedIf.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitRoutedIf.setStatus(_B)
_FsfrExtCircuitUncompressIns_Type=Counter32
_FsfrExtCircuitUncompressIns_Object=MibTableColumn
fsfrExtCircuitUncompressIns=_FsfrExtCircuitUncompressIns_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,9),_FsfrExtCircuitUncompressIns_Type())
fsfrExtCircuitUncompressIns.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitUncompressIns.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitUncompressIns.setUnits(_F)
_FsfrExtCircuitUncompressOuts_Type=Counter32
_FsfrExtCircuitUncompressOuts_Object=MibTableColumn
fsfrExtCircuitUncompressOuts=_FsfrExtCircuitUncompressOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,10),_FsfrExtCircuitUncompressOuts_Type())
fsfrExtCircuitUncompressOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitUncompressOuts.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitUncompressOuts.setUnits(_F)
_FsfrExtCircuitFECNOuts_Type=Counter32
_FsfrExtCircuitFECNOuts_Object=MibTableColumn
fsfrExtCircuitFECNOuts=_FsfrExtCircuitFECNOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,11),_FsfrExtCircuitFECNOuts_Type())
fsfrExtCircuitFECNOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitFECNOuts.setStatus(_B)
_FsfrExtCircuitBECNOuts_Type=Counter32
_FsfrExtCircuitBECNOuts_Object=MibTableColumn
fsfrExtCircuitBECNOuts=_FsfrExtCircuitBECNOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,12),_FsfrExtCircuitBECNOuts_Type())
fsfrExtCircuitBECNOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitBECNOuts.setStatus(_B)
class _FsfrExtCircuitMinThruputOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_FsfrExtCircuitMinThruputOut_Type.__name__=_D
_FsfrExtCircuitMinThruputOut_Object=MibTableColumn
fsfrExtCircuitMinThruputOut=_FsfrExtCircuitMinThruputOut_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,13),_FsfrExtCircuitMinThruputOut_Type())
fsfrExtCircuitMinThruputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitMinThruputOut.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitMinThruputOut.setUnits(_J)
class _FsfrExtCircuitMinThruputIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_FsfrExtCircuitMinThruputIn_Type.__name__=_D
_FsfrExtCircuitMinThruputIn_Object=MibTableColumn
fsfrExtCircuitMinThruputIn=_FsfrExtCircuitMinThruputIn_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,14),_FsfrExtCircuitMinThruputIn_Type())
fsfrExtCircuitMinThruputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitMinThruputIn.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitMinThruputIn.setUnits(_J)
_FsfrExtCircuitBcastPktOuts_Type=Counter32
_FsfrExtCircuitBcastPktOuts_Object=MibTableColumn
fsfrExtCircuitBcastPktOuts=_FsfrExtCircuitBcastPktOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,15),_FsfrExtCircuitBcastPktOuts_Type())
fsfrExtCircuitBcastPktOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitBcastPktOuts.setStatus(_B)
_FsfrExtCircuitBcastByteOuts_Type=Counter32
_FsfrExtCircuitBcastByteOuts_Object=MibTableColumn
fsfrExtCircuitBcastByteOuts=_FsfrExtCircuitBcastByteOuts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,16),_FsfrExtCircuitBcastByteOuts_Type())
fsfrExtCircuitBcastByteOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitBcastByteOuts.setStatus(_B)
class _FsfrExtCircuitBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_FsfrExtCircuitBandwidth_Type.__name__=_D
_FsfrExtCircuitBandwidth_Object=MibTableColumn
fsfrExtCircuitBandwidth=_FsfrExtCircuitBandwidth_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,17),_FsfrExtCircuitBandwidth_Type())
fsfrExtCircuitBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitBandwidth.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitBandwidth.setUnits(_J)
class _FsfrExtCircuitShapeByteLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,2147483647))
_FsfrExtCircuitShapeByteLimit_Type.__name__=_D
_FsfrExtCircuitShapeByteLimit_Object=MibTableColumn
fsfrExtCircuitShapeByteLimit=_FsfrExtCircuitShapeByteLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,18),_FsfrExtCircuitShapeByteLimit_Type())
fsfrExtCircuitShapeByteLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeByteLimit.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitShapeByteLimit.setUnits(_F)
class _FsfrExtCircuitShapeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,125))
_FsfrExtCircuitShapeInterval_Type.__name__=_D
_FsfrExtCircuitShapeInterval_Object=MibTableColumn
fsfrExtCircuitShapeInterval=_FsfrExtCircuitShapeInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,19),_FsfrExtCircuitShapeInterval_Type())
fsfrExtCircuitShapeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeInterval.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitShapeInterval.setUnits('milliseconds')
class _FsfrExtCircuitShapeByteIncrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,2147483647))
_FsfrExtCircuitShapeByteIncrement_Type.__name__=_D
_FsfrExtCircuitShapeByteIncrement_Object=MibTableColumn
fsfrExtCircuitShapeByteIncrement=_FsfrExtCircuitShapeByteIncrement_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,20),_FsfrExtCircuitShapeByteIncrement_Type())
fsfrExtCircuitShapeByteIncrement.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeByteIncrement.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitShapeByteIncrement.setUnits(_F)
_FsfrExtCircuitShapePkts_Type=Counter32
_FsfrExtCircuitShapePkts_Object=MibTableColumn
fsfrExtCircuitShapePkts=_FsfrExtCircuitShapePkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,21),_FsfrExtCircuitShapePkts_Type())
fsfrExtCircuitShapePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapePkts.setStatus(_B)
_FsfrExtCircuitShapeBytes_Type=Counter32
_FsfrExtCircuitShapeBytes_Object=MibTableColumn
fsfrExtCircuitShapeBytes=_FsfrExtCircuitShapeBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,22),_FsfrExtCircuitShapeBytes_Type())
fsfrExtCircuitShapeBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeBytes.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitShapeBytes.setUnits(_F)
_FsfrExtCircuitShapePktsDelay_Type=Counter32
_FsfrExtCircuitShapePktsDelay_Object=MibTableColumn
fsfrExtCircuitShapePktsDelay=_FsfrExtCircuitShapePktsDelay_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,23),_FsfrExtCircuitShapePktsDelay_Type())
fsfrExtCircuitShapePktsDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapePktsDelay.setStatus(_B)
_FsfrExtCircuitShapeBytesDelay_Type=Counter32
_FsfrExtCircuitShapeBytesDelay_Object=MibTableColumn
fsfrExtCircuitShapeBytesDelay=_FsfrExtCircuitShapeBytesDelay_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,24),_FsfrExtCircuitShapeBytesDelay_Type())
fsfrExtCircuitShapeBytesDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeBytesDelay.setStatus(_B)
if mibBuilder.loadTexts:fsfrExtCircuitShapeBytesDelay.setUnits(_F)
_FsfrExtCircuitShapeActive_Type=TruthValue
_FsfrExtCircuitShapeActive_Object=MibTableColumn
fsfrExtCircuitShapeActive=_FsfrExtCircuitShapeActive_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,25),_FsfrExtCircuitShapeActive_Type())
fsfrExtCircuitShapeActive.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeActive.setStatus(_B)
class _FsfrExtCircuitShapeAdapting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('becn',2),('foreSight',3)))
_FsfrExtCircuitShapeAdapting_Type.__name__=_D
_FsfrExtCircuitShapeAdapting_Object=MibTableColumn
fsfrExtCircuitShapeAdapting=_FsfrExtCircuitShapeAdapting_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,26),_FsfrExtCircuitShapeAdapting_Type())
fsfrExtCircuitShapeAdapting.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitShapeAdapting.setStatus(_B)
class _FsfrExtCircuitTxDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_FsfrExtCircuitTxDataRate_Type.__name__=_D
_FsfrExtCircuitTxDataRate_Object=MibTableColumn
fsfrExtCircuitTxDataRate=_FsfrExtCircuitTxDataRate_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,27),_FsfrExtCircuitTxDataRate_Type())
fsfrExtCircuitTxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitTxDataRate.setStatus(_B)
class _FsfrExtCircuitTxPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_FsfrExtCircuitTxPktRate_Type.__name__=_D
_FsfrExtCircuitTxPktRate_Object=MibTableColumn
fsfrExtCircuitTxPktRate=_FsfrExtCircuitTxPktRate_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,28),_FsfrExtCircuitTxPktRate_Type())
fsfrExtCircuitTxPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitTxPktRate.setStatus(_B)
class _FsfrExtCircuitRcvDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_FsfrExtCircuitRcvDataRate_Type.__name__=_D
_FsfrExtCircuitRcvDataRate_Object=MibTableColumn
fsfrExtCircuitRcvDataRate=_FsfrExtCircuitRcvDataRate_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,29),_FsfrExtCircuitRcvDataRate_Type())
fsfrExtCircuitRcvDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitRcvDataRate.setStatus(_B)
class _FsfrExtCircuitRcvPktRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45000000))
_FsfrExtCircuitRcvPktRate_Type.__name__=_D
_FsfrExtCircuitRcvPktRate_Object=MibTableColumn
fsfrExtCircuitRcvPktRate=_FsfrExtCircuitRcvPktRate_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,2,2,1,30),_FsfrExtCircuitRcvPktRate_Type())
fsfrExtCircuitRcvPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrExtCircuitRcvPktRate.setStatus(_B)
_FsfrMapObjs_ObjectIdentity=ObjectIdentity
fsfrMapObjs=_FsfrMapObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,3))
_FsfrMapTable_Object=MibTable
fsfrMapTable=_FsfrMapTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1))
if mibBuilder.loadTexts:fsfrMapTable.setStatus(_B)
_FsfrMapEntry_Object=MibTableRow
fsfrMapEntry=_FsfrMapEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1))
fsfrMapEntry.setIndexNames((0,_G,_L),(0,_G,_K),(0,_A,_M))
if mibBuilder.loadTexts:fsfrMapEntry.setStatus(_B)
class _FsfrMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_FsfrMapIndex_Type.__name__=_D
_FsfrMapIndex_Object=MibTableColumn
fsfrMapIndex=_FsfrMapIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,1),_FsfrMapIndex_Type())
fsfrMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapIndex.setStatus(_B)
_FsfrMapProtocol_Type=FSfrMapProtocols
_FsfrMapProtocol_Object=MibTableColumn
fsfrMapProtocol=_FsfrMapProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,2),_FsfrMapProtocol_Type())
fsfrMapProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapProtocol.setStatus(_B)
class _FsfrMapAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsfrMapAddress_Type.__name__=_V
_FsfrMapAddress_Object=MibTableColumn
fsfrMapAddress=_FsfrMapAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,3),_FsfrMapAddress_Type())
fsfrMapAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapAddress.setStatus(_B)
class _FsfrMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('svc',3)))
_FsfrMapType_Type.__name__=_D
_FsfrMapType_Object=MibTableColumn
fsfrMapType=_FsfrMapType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,4),_FsfrMapType_Type())
fsfrMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapType.setStatus(_B)
class _FsfrMapEncaps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('cisco',2)))
_FsfrMapEncaps_Type.__name__=_D
_FsfrMapEncaps_Object=MibTableColumn
fsfrMapEncaps=_FsfrMapEncaps_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,5),_FsfrMapEncaps_Type())
fsfrMapEncaps.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapEncaps.setStatus(_B)
_FsfrMapBroadcast_Type=TruthValue
_FsfrMapBroadcast_Object=MibTableColumn
fsfrMapBroadcast=_FsfrMapBroadcast_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,6),_FsfrMapBroadcast_Type())
fsfrMapBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapBroadcast.setStatus(_B)
_FsfrMapPayloadCompress_Type=TruthValue
_FsfrMapPayloadCompress_Object=MibTableColumn
fsfrMapPayloadCompress=_FsfrMapPayloadCompress_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,7),_FsfrMapPayloadCompress_Type())
fsfrMapPayloadCompress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapPayloadCompress.setStatus(_H)
class _FsfrMapTcpHdrCompress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),('passive',2),('active',3)))
_FsfrMapTcpHdrCompress_Type.__name__=_D
_FsfrMapTcpHdrCompress_Object=MibTableColumn
fsfrMapTcpHdrCompress=_FsfrMapTcpHdrCompress_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,8),_FsfrMapTcpHdrCompress_Type())
fsfrMapTcpHdrCompress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapTcpHdrCompress.setStatus(_B)
class _FsfrMapRtpHdrCompress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),('passive',2),('active',3)))
_FsfrMapRtpHdrCompress_Type.__name__=_D
_FsfrMapRtpHdrCompress_Object=MibTableColumn
fsfrMapRtpHdrCompress=_FsfrMapRtpHdrCompress_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,9),_FsfrMapRtpHdrCompress_Type())
fsfrMapRtpHdrCompress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapRtpHdrCompress.setStatus(_B)
class _FsfrMapPayloadCompressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AA,1),('cisco',2),('frf9Software',3),('frf9Hardware',4)))
_FsfrMapPayloadCompressType_Type.__name__=_D
_FsfrMapPayloadCompressType_Object=MibTableColumn
fsfrMapPayloadCompressType=_FsfrMapPayloadCompressType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,3,1,1,10),_FsfrMapPayloadCompressType_Type())
fsfrMapPayloadCompressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrMapPayloadCompressType.setStatus(_B)
_FsfrSvcObjs_ObjectIdentity=ObjectIdentity
fsfrSvcObjs=_FsfrSvcObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,4))
_FsfrSvcTable_Object=MibTable
fsfrSvcTable=_FsfrSvcTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1))
if mibBuilder.loadTexts:fsfrSvcTable.setStatus(_B)
_FsfrSvcEntry_Object=MibTableRow
fsfrSvcEntry=_FsfrSvcEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1))
fsfrSvcEntry.setIndexNames((0,_G,_L),(0,_G,_K))
if mibBuilder.loadTexts:fsfrSvcEntry.setStatus(_B)
class _FsfrSvcAddrLocal_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsfrSvcAddrLocal_Type.__name__=_V
_FsfrSvcAddrLocal_Object=MibTableColumn
fsfrSvcAddrLocal=_FsfrSvcAddrLocal_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,1),_FsfrSvcAddrLocal_Type())
fsfrSvcAddrLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcAddrLocal.setStatus(_B)
class _FsfrSvcAddrRemote_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsfrSvcAddrRemote_Type.__name__=_V
_FsfrSvcAddrRemote_Object=MibTableColumn
fsfrSvcAddrRemote=_FsfrSvcAddrRemote_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,2),_FsfrSvcAddrRemote_Type())
fsfrSvcAddrRemote.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcAddrRemote.setStatus(_B)
class _FsfrSvcThroughputIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_FsfrSvcThroughputIn_Type.__name__=_D
_FsfrSvcThroughputIn_Object=MibTableColumn
fsfrSvcThroughputIn=_FsfrSvcThroughputIn_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,3),_FsfrSvcThroughputIn_Type())
fsfrSvcThroughputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcThroughputIn.setStatus(_B)
if mibBuilder.loadTexts:fsfrSvcThroughputIn.setUnits(_J)
class _FsfrSvcMinThruputOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_FsfrSvcMinThruputOut_Type.__name__=_D
_FsfrSvcMinThruputOut_Object=MibTableColumn
fsfrSvcMinThruputOut=_FsfrSvcMinThruputOut_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,4),_FsfrSvcMinThruputOut_Type())
fsfrSvcMinThruputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcMinThruputOut.setStatus(_H)
if mibBuilder.loadTexts:fsfrSvcMinThruputOut.setUnits(_J)
class _FsfrSvcMinThruputIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_FsfrSvcMinThruputIn_Type.__name__=_D
_FsfrSvcMinThruputIn_Object=MibTableColumn
fsfrSvcMinThruputIn=_FsfrSvcMinThruputIn_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,5),_FsfrSvcMinThruputIn_Type())
fsfrSvcMinThruputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcMinThruputIn.setStatus(_H)
if mibBuilder.loadTexts:fsfrSvcMinThruputIn.setUnits(_J)
class _FsfrSvcCommitBurstIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,1544000))
_FsfrSvcCommitBurstIn_Type.__name__=_D
_FsfrSvcCommitBurstIn_Object=MibTableColumn
fsfrSvcCommitBurstIn=_FsfrSvcCommitBurstIn_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,6),_FsfrSvcCommitBurstIn_Type())
fsfrSvcCommitBurstIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcCommitBurstIn.setStatus(_B)
class _FsfrSvcExcessBurstIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,2440000))
_FsfrSvcExcessBurstIn_Type.__name__=_D
_FsfrSvcExcessBurstIn_Object=MibTableColumn
fsfrSvcExcessBurstIn=_FsfrSvcExcessBurstIn_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,7),_FsfrSvcExcessBurstIn_Type())
fsfrSvcExcessBurstIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcExcessBurstIn.setStatus(_B)
_FsfrSvcIdleTime_Type=Integer32
_FsfrSvcIdleTime_Object=MibTableColumn
fsfrSvcIdleTime=_FsfrSvcIdleTime_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,4,1,1,8),_FsfrSvcIdleTime_Type())
fsfrSvcIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrSvcIdleTime.setStatus(_B)
if mibBuilder.loadTexts:fsfrSvcIdleTime.setUnits('seconds')
_FsfrElmiObjs_ObjectIdentity=ObjectIdentity
fsfrElmiObjs=_FsfrElmiObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,5))
_FsfrElmiIpAddr_Type=IpAddress
_FsfrElmiIpAddr_Object=MibScalar
fsfrElmiIpAddr=_FsfrElmiIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,1),_FsfrElmiIpAddr_Type())
fsfrElmiIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiIpAddr.setStatus(_B)
_FsfrElmiTable_Object=MibTable
fsfrElmiTable=_FsfrElmiTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,2))
if mibBuilder.loadTexts:fsfrElmiTable.setStatus(_B)
_FsfrElmiEntry_Object=MibTableRow
fsfrElmiEntry=_FsfrElmiEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,2,1))
fsfrElmiEntry.setIndexNames((0,_A8,_A9))
if mibBuilder.loadTexts:fsfrElmiEntry.setStatus(_B)
class _FsfrElmiLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsfrElmiLinkStatus_Type.__name__=_D
_FsfrElmiLinkStatus_Object=MibTableColumn
fsfrElmiLinkStatus=_FsfrElmiLinkStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,2,1,1),_FsfrElmiLinkStatus_Type())
fsfrElmiLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiLinkStatus.setStatus(_B)
class _FsfrElmiArStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsfrElmiArStatus_Type.__name__=_D
_FsfrElmiArStatus_Object=MibTableColumn
fsfrElmiArStatus=_FsfrElmiArStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,2,1,2),_FsfrElmiArStatus_Type())
fsfrElmiArStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiArStatus.setStatus(_B)
class _FsfrElmiRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsfrElmiRemoteStatus_Type.__name__=_D
_FsfrElmiRemoteStatus_Object=MibTableColumn
fsfrElmiRemoteStatus=_FsfrElmiRemoteStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,2,1,3),_FsfrElmiRemoteStatus_Type())
fsfrElmiRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiRemoteStatus.setStatus(_B)
_FsfrElmiNeighborTable_Object=MibTable
fsfrElmiNeighborTable=_FsfrElmiNeighborTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3))
if mibBuilder.loadTexts:fsfrElmiNeighborTable.setStatus(_B)
_FsfrElmiNeighborEntry_Object=MibTableRow
fsfrElmiNeighborEntry=_FsfrElmiNeighborEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1))
fsfrElmiNeighborEntry.setIndexNames((0,_A8,_A9))
if mibBuilder.loadTexts:fsfrElmiNeighborEntry.setStatus(_B)
class _FsfrElmiNeighborArStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notsupported',1),(_W,2),(_X,3)))
_FsfrElmiNeighborArStatus_Type.__name__=_D
_FsfrElmiNeighborArStatus_Object=MibTableColumn
fsfrElmiNeighborArStatus=_FsfrElmiNeighborArStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1,1),_FsfrElmiNeighborArStatus_Type())
fsfrElmiNeighborArStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiNeighborArStatus.setStatus(_B)
_FsfrElmiNeighborIpAddress_Type=IpAddress
_FsfrElmiNeighborIpAddress_Object=MibTableColumn
fsfrElmiNeighborIpAddress=_FsfrElmiNeighborIpAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1,2),_FsfrElmiNeighborIpAddress_Type())
fsfrElmiNeighborIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiNeighborIpAddress.setStatus(_B)
_FsfrElmiNeighborIfIndex_Type=InterfaceIndex
_FsfrElmiNeighborIfIndex_Object=MibTableColumn
fsfrElmiNeighborIfIndex=_FsfrElmiNeighborIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1,3),_FsfrElmiNeighborIfIndex_Type())
fsfrElmiNeighborIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiNeighborIfIndex.setStatus(_B)
_FsfrElmiNeighborVendorName_Type=DisplayString
_FsfrElmiNeighborVendorName_Object=MibTableColumn
fsfrElmiNeighborVendorName=_FsfrElmiNeighborVendorName_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1,4),_FsfrElmiNeighborVendorName_Type())
fsfrElmiNeighborVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiNeighborVendorName.setStatus(_B)
_FsfrElmiNeighborPlatformName_Type=DisplayString
_FsfrElmiNeighborPlatformName_Object=MibTableColumn
fsfrElmiNeighborPlatformName=_FsfrElmiNeighborPlatformName_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1,5),_FsfrElmiNeighborPlatformName_Type())
fsfrElmiNeighborPlatformName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiNeighborPlatformName.setStatus(_B)
_FsfrElmiNeighborDeviceName_Type=DisplayString
_FsfrElmiNeighborDeviceName_Object=MibTableColumn
fsfrElmiNeighborDeviceName=_FsfrElmiNeighborDeviceName_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,5,3,1,6),_FsfrElmiNeighborDeviceName_Type())
fsfrElmiNeighborDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrElmiNeighborDeviceName.setStatus(_B)
_FsfrFragObjs_ObjectIdentity=ObjectIdentity
fsfrFragObjs=_FsfrFragObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,6))
_FsfrFragTable_Object=MibTable
fsfrFragTable=_FsfrFragTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1))
if mibBuilder.loadTexts:fsfrFragTable.setStatus(_B)
_FsfrFragEntry_Object=MibTableRow
fsfrFragEntry=_FsfrFragEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1))
fsfrFragEntry.setIndexNames((0,_G,_L),(0,_G,_K))
if mibBuilder.loadTexts:fsfrFragEntry.setStatus(_B)
class _FsfrFragSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1600))
_FsfrFragSize_Type.__name__=_D
_FsfrFragSize_Object=MibTableColumn
fsfrFragSize=_FsfrFragSize_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,1),_FsfrFragSize_Type())
fsfrFragSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragSize.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragSize.setUnits(_F)
_FsfrFragType_Type=DisplayString
_FsfrFragType_Object=MibTableColumn
fsfrFragType=_FsfrFragType_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,2),_FsfrFragType_Type())
fsfrFragType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragType.setStatus(_B)
_FsfrFragInPkts_Type=Counter32
_FsfrFragInPkts_Object=MibTableColumn
fsfrFragInPkts=_FsfrFragInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,3),_FsfrFragInPkts_Type())
fsfrFragInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragInPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragInPkts.setUnits(_E)
_FsfrFragOutPkts_Type=Counter32
_FsfrFragOutPkts_Object=MibTableColumn
fsfrFragOutPkts=_FsfrFragOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,4),_FsfrFragOutPkts_Type())
fsfrFragOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragOutPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragOutPkts.setUnits(_E)
_FsfrFragInOctets_Type=Counter32
_FsfrFragInOctets_Object=MibTableColumn
fsfrFragInOctets=_FsfrFragInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,5),_FsfrFragInOctets_Type())
fsfrFragInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragInOctets.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragInOctets.setUnits(_F)
_FsfrFragOutOctets_Type=Counter32
_FsfrFragOutOctets_Object=MibTableColumn
fsfrFragOutOctets=_FsfrFragOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,6),_FsfrFragOutOctets_Type())
fsfrFragOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragOutOctets.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragOutOctets.setUnits(_F)
_FsfrFragNotInPkts_Type=Counter32
_FsfrFragNotInPkts_Object=MibTableColumn
fsfrFragNotInPkts=_FsfrFragNotInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,7),_FsfrFragNotInPkts_Type())
fsfrFragNotInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragNotInPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragNotInPkts.setUnits(_E)
_FsfrFragNotOutPkts_Type=Counter32
_FsfrFragNotOutPkts_Object=MibTableColumn
fsfrFragNotOutPkts=_FsfrFragNotOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,8),_FsfrFragNotOutPkts_Type())
fsfrFragNotOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragNotOutPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragNotOutPkts.setUnits(_E)
_FsfrFragNotInOctets_Type=Counter32
_FsfrFragNotInOctets_Object=MibTableColumn
fsfrFragNotInOctets=_FsfrFragNotInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,9),_FsfrFragNotInOctets_Type())
fsfrFragNotInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragNotInOctets.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragNotInOctets.setUnits(_F)
_FsfrFragNotOutOctets_Type=Counter32
_FsfrFragNotOutOctets_Object=MibTableColumn
fsfrFragNotOutOctets=_FsfrFragNotOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,10),_FsfrFragNotOutOctets_Type())
fsfrFragNotOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragNotOutOctets.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragNotOutOctets.setUnits(_F)
_FsfrFragAssembledInPkts_Type=Counter32
_FsfrFragAssembledInPkts_Object=MibTableColumn
fsfrFragAssembledInPkts=_FsfrFragAssembledInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,11),_FsfrFragAssembledInPkts_Type())
fsfrFragAssembledInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragAssembledInPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragAssembledInPkts.setUnits(_E)
_FsfrFragAssembledInOctets_Type=Counter32
_FsfrFragAssembledInOctets_Object=MibTableColumn
fsfrFragAssembledInOctets=_FsfrFragAssembledInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,12),_FsfrFragAssembledInOctets_Type())
fsfrFragAssembledInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragAssembledInOctets.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragAssembledInOctets.setUnits(_F)
_FsfrFragPreOutPkts_Type=Counter32
_FsfrFragPreOutPkts_Object=MibTableColumn
fsfrFragPreOutPkts=_FsfrFragPreOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,13),_FsfrFragPreOutPkts_Type())
fsfrFragPreOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragPreOutPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragPreOutPkts.setUnits(_E)
_FsfrFragPreOutOctets_Type=Counter32
_FsfrFragPreOutOctets_Object=MibTableColumn
fsfrFragPreOutOctets=_FsfrFragPreOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,14),_FsfrFragPreOutOctets_Type())
fsfrFragPreOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragPreOutOctets.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragPreOutOctets.setUnits(_F)
_FsfrFragDroppedReAssembledInPkts_Type=Counter32
_FsfrFragDroppedReAssembledInPkts_Object=MibTableColumn
fsfrFragDroppedReAssembledInPkts=_FsfrFragDroppedReAssembledInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,15),_FsfrFragDroppedReAssembledInPkts_Type())
fsfrFragDroppedReAssembledInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragDroppedReAssembledInPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragDroppedReAssembledInPkts.setUnits(_E)
_FsfrFragDroppedFragmentedOutPkts_Type=Counter32
_FsfrFragDroppedFragmentedOutPkts_Object=MibTableColumn
fsfrFragDroppedFragmentedOutPkts=_FsfrFragDroppedFragmentedOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,16),_FsfrFragDroppedFragmentedOutPkts_Type())
fsfrFragDroppedFragmentedOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragDroppedFragmentedOutPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragDroppedFragmentedOutPkts.setUnits(_E)
class _FsfrFragTimeoutsIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsfrFragTimeoutsIn_Type.__name__=_D
_FsfrFragTimeoutsIn_Object=MibTableColumn
fsfrFragTimeoutsIn=_FsfrFragTimeoutsIn_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,17),_FsfrFragTimeoutsIn_Type())
fsfrFragTimeoutsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragTimeoutsIn.setStatus(_B)
_FsfrFragOutOfSeqFragPkts_Type=Counter32
_FsfrFragOutOfSeqFragPkts_Object=MibTableColumn
fsfrFragOutOfSeqFragPkts=_FsfrFragOutOfSeqFragPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,18),_FsfrFragOutOfSeqFragPkts_Type())
fsfrFragOutOfSeqFragPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragOutOfSeqFragPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragOutOfSeqFragPkts.setUnits(_E)
_FsfrFragUnexpectedBBitSetPkts_Type=Counter32
_FsfrFragUnexpectedBBitSetPkts_Object=MibTableColumn
fsfrFragUnexpectedBBitSetPkts=_FsfrFragUnexpectedBBitSetPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,19),_FsfrFragUnexpectedBBitSetPkts_Type())
fsfrFragUnexpectedBBitSetPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragUnexpectedBBitSetPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragUnexpectedBBitSetPkts.setUnits(_E)
_FsfrFragSeqMissedPkts_Type=Counter32
_FsfrFragSeqMissedPkts_Object=MibTableColumn
fsfrFragSeqMissedPkts=_FsfrFragSeqMissedPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,20),_FsfrFragSeqMissedPkts_Type())
fsfrFragSeqMissedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragSeqMissedPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragSeqMissedPkts.setUnits(_E)
_FsfrFragInterleavedOutPkts_Type=Counter32
_FsfrFragInterleavedOutPkts_Object=MibTableColumn
fsfrFragInterleavedOutPkts=_FsfrFragInterleavedOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,6,1,1,21),_FsfrFragInterleavedOutPkts_Type())
fsfrFragInterleavedOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrFragInterleavedOutPkts.setStatus(_B)
if mibBuilder.loadTexts:fsfrFragInterleavedOutPkts.setUnits(_E)
_FsfrConnectionObjs_ObjectIdentity=ObjectIdentity
fsfrConnectionObjs=_FsfrConnectionObjs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,1,7))
_FsfrConnectionTable_Object=MibTable
fsfrConnectionTable=_FsfrConnectionTable_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1))
if mibBuilder.loadTexts:fsfrConnectionTable.setStatus(_B)
_FsfrConnectionEntry_Object=MibTableRow
fsfrConnectionEntry=_FsfrConnectionEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1))
fsfrConnectionEntry.setIndexNames((0,_G,_L),(0,_G,_K))
if mibBuilder.loadTexts:fsfrConnectionEntry.setStatus(_B)
_FsfrConnName_Type=DisplayString
_FsfrConnName_Object=MibTableColumn
fsfrConnName=_FsfrConnName_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,1),_FsfrConnName_Type())
fsfrConnName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnName.setStatus(_B)
class _FsfrConnID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_FsfrConnID_Type.__name__=_D
_FsfrConnID_Object=MibTableColumn
fsfrConnID=_FsfrConnID_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,2),_FsfrConnID_Type())
fsfrConnID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnID.setStatus(_B)
_FsfrConnState_Type=DisplayString
_FsfrConnState_Object=MibTableColumn
fsfrConnState=_FsfrConnState_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,3),_FsfrConnState_Type())
fsfrConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnState.setStatus(_B)
_FsfrConnSegment1Name_Type=DisplayString
_FsfrConnSegment1Name_Object=MibTableColumn
fsfrConnSegment1Name=_FsfrConnSegment1Name_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,4),_FsfrConnSegment1Name_Type())
fsfrConnSegment1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnSegment1Name.setStatus(_B)
_FsfrConnSegment1VCGroup_Type=DisplayString
_FsfrConnSegment1VCGroup_Object=MibTableColumn
fsfrConnSegment1VCGroup=_FsfrConnSegment1VCGroup_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,5),_FsfrConnSegment1VCGroup_Type())
fsfrConnSegment1VCGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnSegment1VCGroup.setStatus(_B)
_FsfrConnSegment1Dlci_Type=DlciNumber
_FsfrConnSegment1Dlci_Object=MibTableColumn
fsfrConnSegment1Dlci=_FsfrConnSegment1Dlci_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,6),_FsfrConnSegment1Dlci_Type())
fsfrConnSegment1Dlci.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnSegment1Dlci.setStatus(_B)
_FsfrConnSegment2Name_Type=DisplayString
_FsfrConnSegment2Name_Object=MibTableColumn
fsfrConnSegment2Name=_FsfrConnSegment2Name_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,7),_FsfrConnSegment2Name_Type())
fsfrConnSegment2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnSegment2Name.setStatus(_B)
class _FsfrConnSegment2Vpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_FsfrConnSegment2Vpi_Type.__name__=_D
_FsfrConnSegment2Vpi_Object=MibTableColumn
fsfrConnSegment2Vpi=_FsfrConnSegment2Vpi_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,8),_FsfrConnSegment2Vpi_Type())
fsfrConnSegment2Vpi.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnSegment2Vpi.setStatus(_B)
class _FsfrConnSegment2Vci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_FsfrConnSegment2Vci_Type.__name__=_D
_FsfrConnSegment2Vci_Object=MibTableColumn
fsfrConnSegment2Vci=_FsfrConnSegment2Vci_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,9),_FsfrConnSegment2Vci_Type())
fsfrConnSegment2Vci.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnSegment2Vci.setStatus(_B)
class _FsfrConnServiceTranslation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('serviceTranslationEnabled',1),('serviceTranslationNotEnabled',2)))
_FsfrConnServiceTranslation_Type.__name__=_D
_FsfrConnServiceTranslation_Object=MibTableColumn
fsfrConnServiceTranslation=_FsfrConnServiceTranslation_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,10),_FsfrConnServiceTranslation_Type())
fsfrConnServiceTranslation.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnServiceTranslation.setStatus(_B)
_FsfrConnFrSscsDlci_Type=DlciNumber
_FsfrConnFrSscsDlci_Object=MibTableColumn
fsfrConnFrSscsDlci=_FsfrConnFrSscsDlci_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,11),_FsfrConnFrSscsDlci_Type())
fsfrConnFrSscsDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnFrSscsDlci.setStatus(_B)
class _FsfrConnEfciBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mapFecn',1),('notMapFecn',2)))
_FsfrConnEfciBit_Type.__name__=_D
_FsfrConnEfciBit_Object=MibTableColumn
fsfrConnEfciBit=_FsfrConnEfciBit_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,12),_FsfrConnEfciBit_Type())
fsfrConnEfciBit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnEfciBit.setStatus(_B)
class _FsfrConnDeBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noMapClp',1),('mapClp',2),('setDe0',3),('setDe1',4)))
_FsfrConnDeBit_Type.__name__=_D
_FsfrConnDeBit_Object=MibTableColumn
fsfrConnDeBit=_FsfrConnDeBit_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,13),_FsfrConnDeBit_Type())
fsfrConnDeBit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnDeBit.setStatus(_B)
class _FsfrConnClpBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('setClpTo0AndCopyDeToFrsscsDe',1),('setClpTo1AndCopyDeToFrsscsDe',2),('copyDeToFrsscsDeAndClp',3),('copyDeToClp',4),('setClp1',5),('setClp0',6)))
_FsfrConnClpBit_Type.__name__=_D
_FsfrConnClpBit_Object=MibTableColumn
fsfrConnClpBit=_FsfrConnClpBit_Object((1,3,6,1,4,1,52642,1,1,10,2,50,1,7,1,1,14),_FsfrConnClpBit_Type())
fsfrConnClpBit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsfrConnClpBit.setStatus(_B)
_FsFrMIBConformance_ObjectIdentity=ObjectIdentity
fsFrMIBConformance=_FsFrMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,3))
_FsFrMIBCompliances_ObjectIdentity=ObjectIdentity
fsFrMIBCompliances=_FsFrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,3,1))
_FsFrMIBGroups_ObjectIdentity=ObjectIdentity
fsFrMIBGroups=_FsFrMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,50,3,2))
frDlcmiEntry.registerAugmentions((_A,_AX))
fsfrLmiEntry.setIndexNames(*frDlcmiEntry.getIndexNames())
frCircuitEntry.registerAugmentions((_A,_AY))
fsfrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
frCircuitEntry.registerAugmentions((_A,_AZ))
fsfrExtCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
fsFrMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,1))
fsFrMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_M),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_Aa),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_AB),(_A,_AC),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:fsFrMIBGroup.setStatus(_H)
fsFrMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,2))
fsFrMIBGroupRev1.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A1),(_A,_A2),(_A,_M),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_AD),(_A,_AE),(_A,_v),(_A,_w),(_A,_x),(_A,_AB),(_A,_AC),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:fsFrMIBGroupRev1.setStatus(_H)
fsFrLmiMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,3))
fsFrLmiMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:fsFrLmiMIBGroup.setStatus(_B)
fsFrCircuitMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,4))
fsFrCircuitMIBGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:fsFrCircuitMIBGroup.setStatus(_B)
fsExtCircuitMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,5))
fsExtCircuitMIBGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A1),(_A,_A2),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:fsExtCircuitMIBGroup.setStatus(_H)
fsFrTsMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,6))
fsFrTsMIBGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:fsFrTsMIBGroup.setStatus(_B)
fsFrMapMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,7))
fsFrMapMIBGroup.setObjects(*((_A,_M),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:fsFrMapMIBGroup.setStatus(_B)
fsFrSvcMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,8))
fsFrSvcMIBGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:fsFrSvcMIBGroup.setStatus(_B)
fsFrElmiMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,9))
fsFrElmiMIBGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU)))
if mibBuilder.loadTexts:fsFrElmiMIBGroup.setStatus(_H)
fsFrElmiMIBGroup1=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,10))
fsFrElmiMIBGroup1.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_Ak)))
if mibBuilder.loadTexts:fsFrElmiMIBGroup1.setStatus(_B)
fsFrFragMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,11))
fsFrFragMIBGroup.setObjects(*((_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4)))
if mibBuilder.loadTexts:fsFrFragMIBGroup.setStatus(_B)
fsFrConnMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,12))
fsFrConnMIBGroup.setObjects(*((_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI)))
if mibBuilder.loadTexts:fsFrConnMIBGroup.setStatus(_B)
fsExtCircuitMIBGroup1=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,50,3,2,13))
fsExtCircuitMIBGroup1.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A1),(_A,_A2),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM)))
if mibBuilder.loadTexts:fsExtCircuitMIBGroup1.setStatus(_B)
fsFrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,50,3,1,1))
fsFrMIBCompliance.setObjects((_A,_BN))
if mibBuilder.loadTexts:fsFrMIBCompliance.setStatus(_AV)
fsFrMIBCompliancesRev1=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,50,3,1,2))
fsFrMIBCompliancesRev1.setObjects((_A,_BO))
if mibBuilder.loadTexts:fsFrMIBCompliancesRev1.setStatus(_AV)
fsFrMIBCompliancesRev2=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,50,3,1,3))
fsFrMIBCompliancesRev2.setObjects(*((_A,_A3),(_A,_A4),(_A,_AW),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:fsFrMIBCompliancesRev2.setStatus(_AV)
fsFrMIBCompliancesRev3=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,50,3,1,4))
fsFrMIBCompliancesRev3.setObjects(*((_A,_A3),(_A,_A4),(_A,_AW),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_BP)))
if mibBuilder.loadTexts:fsFrMIBCompliancesRev3.setStatus(_H)
fsFrMIBCompliancesRev4=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,50,3,1,5))
fsFrMIBCompliancesRev4.setObjects(*((_A,_A3),(_A,_A4),(_A,_BQ),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_BR),(_A,_BS),(_A,_BT)))
if mibBuilder.loadTexts:fsFrMIBCompliancesRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DlciNumber':DlciNumber,'FSfrMapProtocols':FSfrMapProtocols,'fsFrameRelayMIB':fsFrameRelayMIB,'fsFrMIBObjects':fsFrMIBObjects,'fsfrLmiObjs':fsfrLmiObjs,'fsfrLmiTable':fsfrLmiTable,_AX:fsfrLmiEntry,_Y:fsfrLmiLinkstatus,_Z:fsfrLmiLinkType,_a:fsfrLmiEnquiryIns,_b:fsfrLmiEnquiryOuts,_c:fsfrLmiStatusIns,_d:fsfrLmiStatusOuts,_e:fsfrLmiUpdateStatusIns,_f:fsfrLmiUpdateStatusOuts,_g:fsfrLmiStatusTimeouts,_h:fsfrLmiStatusEnqTimeouts,_i:fsfrLmiN392Dce,_j:fsfrLmiN393Dce,_k:fsfrLmiT392Dce,'fsfrCircuitObjs':fsfrCircuitObjs,'fsfrCircuitTable':fsfrCircuitTable,_AY:fsfrCircuitEntry,_l:fsfrCircuitDEins,_m:fsfrCircuitDEouts,_n:fsfrCircuitDropPktsOuts,_o:fsfrCircuitType,'fsfrExtCircuitTable':fsfrExtCircuitTable,_AZ:fsfrExtCircuitEntry,_N:fsfrExtCircuitIfName,_O:fsfrExtCircuitIfType,_P:fsfrExtCircuitSubifIndex,_Q:fsfrExtCircuitMapStatus,_R:fsfrExtCircuitCreateType,_S:fsfrExtCircuitMulticast,_T:fsfrExtCircuitRoutedDlci,_U:fsfrExtCircuitRoutedIf,_A1:fsfrExtCircuitUncompressIns,_A2:fsfrExtCircuitUncompressOuts,_AF:fsfrExtCircuitFECNOuts,_AG:fsfrExtCircuitBECNOuts,_AH:fsfrExtCircuitMinThruputOut,_AI:fsfrExtCircuitMinThruputIn,_AJ:fsfrExtCircuitBcastPktOuts,_AK:fsfrExtCircuitBcastByteOuts,_AL:fsfrExtCircuitBandwidth,_Ab:fsfrExtCircuitShapeByteLimit,_Ac:fsfrExtCircuitShapeInterval,_Ad:fsfrExtCircuitShapeByteIncrement,_Ae:fsfrExtCircuitShapePkts,_Af:fsfrExtCircuitShapeBytes,_Ag:fsfrExtCircuitShapePktsDelay,_Ah:fsfrExtCircuitShapeBytesDelay,_Ai:fsfrExtCircuitShapeActive,_Aj:fsfrExtCircuitShapeAdapting,_BJ:fsfrExtCircuitTxDataRate,_BK:fsfrExtCircuitTxPktRate,_BL:fsfrExtCircuitRcvDataRate,_BM:fsfrExtCircuitRcvPktRate,'fsfrMapObjs':fsfrMapObjs,'fsfrMapTable':fsfrMapTable,'fsfrMapEntry':fsfrMapEntry,_M:fsfrMapIndex,_p:fsfrMapProtocol,_q:fsfrMapAddress,_r:fsfrMapType,_s:fsfrMapEncaps,_t:fsfrMapBroadcast,_Aa:fsfrMapPayloadCompress,_u:fsfrMapTcpHdrCompress,_AD:fsfrMapRtpHdrCompress,_AE:fsfrMapPayloadCompressType,'fsfrSvcObjs':fsfrSvcObjs,'fsfrSvcTable':fsfrSvcTable,'fsfrSvcEntry':fsfrSvcEntry,_v:fsfrSvcAddrLocal,_w:fsfrSvcAddrRemote,_x:fsfrSvcThroughputIn,_AB:fsfrSvcMinThruputOut,_AC:fsfrSvcMinThruputIn,_y:fsfrSvcCommitBurstIn,_z:fsfrSvcExcessBurstIn,_A0:fsfrSvcIdleTime,'fsfrElmiObjs':fsfrElmiObjs,_AM:fsfrElmiIpAddr,'fsfrElmiTable':fsfrElmiTable,'fsfrElmiEntry':fsfrElmiEntry,_Ak:fsfrElmiLinkStatus,_AN:fsfrElmiArStatus,_AO:fsfrElmiRemoteStatus,'fsfrElmiNeighborTable':fsfrElmiNeighborTable,'fsfrElmiNeighborEntry':fsfrElmiNeighborEntry,_AP:fsfrElmiNeighborArStatus,_AQ:fsfrElmiNeighborIpAddress,_AR:fsfrElmiNeighborIfIndex,_AS:fsfrElmiNeighborVendorName,_AT:fsfrElmiNeighborPlatformName,_AU:fsfrElmiNeighborDeviceName,'fsfrFragObjs':fsfrFragObjs,'fsfrFragTable':fsfrFragTable,'fsfrFragEntry':fsfrFragEntry,_Al:fsfrFragSize,_Am:fsfrFragType,_An:fsfrFragInPkts,_Ao:fsfrFragOutPkts,_Ap:fsfrFragInOctets,_Aq:fsfrFragOutOctets,_Ar:fsfrFragNotInPkts,_As:fsfrFragNotOutPkts,_At:fsfrFragNotInOctets,_Au:fsfrFragNotOutOctets,_Av:fsfrFragAssembledInPkts,_Aw:fsfrFragAssembledInOctets,_Ax:fsfrFragPreOutPkts,_Ay:fsfrFragPreOutOctets,_Az:fsfrFragDroppedReAssembledInPkts,_A_:fsfrFragDroppedFragmentedOutPkts,_B0:fsfrFragTimeoutsIn,_B1:fsfrFragOutOfSeqFragPkts,_B2:fsfrFragUnexpectedBBitSetPkts,_B3:fsfrFragSeqMissedPkts,_B4:fsfrFragInterleavedOutPkts,'fsfrConnectionObjs':fsfrConnectionObjs,'fsfrConnectionTable':fsfrConnectionTable,'fsfrConnectionEntry':fsfrConnectionEntry,_B5:fsfrConnName,_B6:fsfrConnID,_B7:fsfrConnState,_B8:fsfrConnSegment1Name,_B9:fsfrConnSegment1VCGroup,_BA:fsfrConnSegment1Dlci,_BB:fsfrConnSegment2Name,_BC:fsfrConnSegment2Vpi,_BD:fsfrConnSegment2Vci,_BE:fsfrConnServiceTranslation,_BF:fsfrConnFrSscsDlci,_BG:fsfrConnEfciBit,_BH:fsfrConnDeBit,_BI:fsfrConnClpBit,'fsFrMIBConformance':fsFrMIBConformance,'fsFrMIBCompliances':fsFrMIBCompliances,'fsFrMIBCompliance':fsFrMIBCompliance,'fsFrMIBCompliancesRev1':fsFrMIBCompliancesRev1,'fsFrMIBCompliancesRev2':fsFrMIBCompliancesRev2,'fsFrMIBCompliancesRev3':fsFrMIBCompliancesRev3,'fsFrMIBCompliancesRev4':fsFrMIBCompliancesRev4,'fsFrMIBGroups':fsFrMIBGroups,_BN:fsFrMIBGroup,_BO:fsFrMIBGroupRev1,_A3:fsFrLmiMIBGroup,_A4:fsFrCircuitMIBGroup,_AW:fsExtCircuitMIBGroup,_A5:fsFrTsMIBGroup,_A6:fsFrMapMIBGroup,_A7:fsFrSvcMIBGroup,_BP:fsFrElmiMIBGroup,_BR:fsFrElmiMIBGroup1,_BS:fsFrFragMIBGroup,_BT:fsFrConnMIBGroup,_BQ:fsExtCircuitMIBGroup1})