_BN='voiceSpeedDialDigits'
_BM='portThreshIndex'
_BL='portThreshRlpIndex'
_BK='rlpThreshRlpIndex'
_BJ='voiceStatsPortIndex'
_BI='voiceStatsRlpIndex'
_BH='ds0aStatsChannelIndex'
_BG='ds0aStatsPortIndex'
_BF='ds0aStatsRlpIndex'
_BE='t1StatsPortIndex'
_BD='t1StatsRlpIndex'
_BC='x25RxPortIndex'
_BB='x25RxRlpIndex'
_BA='x25TxPortIndex'
_B9='x25TxRlpIndex'
_B8='frStatsPortIndex'
_B7='frStatsRlpIndex'
_B6='portStatsIndex'
_B5='portStatsRlpIndex'
_B4='rlpStatsIndex'
_B3='portPinPort'
_B2='portPinRlp'
_B1='nlLlc2OrigConnectionSequence'
_B0='nlLlc2TermConnectionSequence'
_A_='nlLocalSubscriberRedirIndex'
_Az='nlLocalSubscriberRouteIndex'
_Ay='nlIfVoiceInterface'
_Ax='nlIfIpSecondaryAddrSequence'
_Aw='receive-only'
_Av='ipxInterfaceNumber'
_Au='ipxServConfigServName'
_At='ipxServConfigServiceType'
_As='ipxStaticRouteConfigNetNum'
_Ar='ipxStaticRouteConfigCircIndex'
_Aq='originated'
_Ap='terminated'
_Ao='400000000001'
_An='nlIfLlc2FrFormat'
_Am='nlIfLlc2FrDLCI'
_Al='nlIfLlc2FrPort'
_Ak='nlIfLlc2FrRlp'
_Aj='nlIfLlc2LANPort'
_Ai='nlIfLlc2LANRlp'
_Ah='propVirtual'
_Ag='iso88025TokenRing'
_Af='iso88023Csmacd'
_Ae='ethernetCsmacd'
_Ad='rfc877x25'
_Ac='portVoiceOperPortIndex'
_Ab='portVoiceOperRlpIndex'
_Aa='very-high'
_AZ='loop-start'
_AY='portVoiceAdminPortIndex'
_AX='portVoiceAdminRlpIndex'
_AW='minus22p5db'
_AV='minus15db'
_AU='minus7p5db'
_AT='x533-655ft'
_AS='x399-533ft'
_AR='x266-399ft'
_AQ='x133-266ft'
_AP='000000000000'
_AO='two-way-simultaneous'
_AN='two-way-alternate'
_AM='half-duplex'
_AL='full-duplex'
_AK='bsciDevOperDeviceUnitID'
_AJ='bsciDevOperControlUnitID'
_AI='always-active'
_AH='bsciDevAdminDeviceUnitID'
_AG='bsciDevAdminControlUnitID'
_AF='bsciSubscrOperSequence'
_AE='bsciSubscrAdminSequence'
_AD='none-8bit'
_AC='even-7bit'
_AB='portFrBackupGroup'
_AA='portFrBackupDLCI'
_A9='portFrBackupPort'
_A8='portFrBackupRLP'
_A7='portDLCIIndex'
_A6='portDLCIPortIndex'
_A5='portDLCIRlpIndex'
_A4='portFrPortIndex'
_A3='portFrRlpIndex'
_A2='universal'
_A1='operational'
_A0='configured'
_z='rlpIndex'
_y='tpAdrIdx'
_x='nsNTNeigh'
_w='nsNTNode'
_v='nsNodNum'
_u='PhysAddress'
_t='DisplayString'
_s='nlIfIpInterface'
_r='ethernet'
_q='llc2'
_p='frameRelay'
_o='sdlc'
_n='other'
_m='all'
_l='nlIfPhyPort'
_k='nlLlc2HostIndex'
_j='nlLlc2HostGroup'
_i='nlLocalSubscriberId'
_h='not-applicable'
_g='dtmf'
_f='bps-64000'
_e='bps-32000'
_d='bps-8000'
_c='bps-4800'
_b='hpad'
_a='tpad'
_Z='TimeInterval'
_Y='MacAddress'
_X='sdlcLSAddress'
_W='voice'
_V='00000000'
_U='e1'
_T='rs530'
_S='IpAddress'
_R='rs449'
_Q='x21'
_P='t1'
_O='v35'
_N='rs232'
_M='enabled'
_L='none'
_K='disabled'
_J='OctetString'
_I='nlIfPort'
_H='nlIfRlp'
_G='yes'
_F='no'
_E='NETLINK-SPECIFIC-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_S,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_t,_Y,_u,'RowStatus','TextualConvention',_Z)
class NlSubscriberAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SnaDLC_ObjectIdentity=ObjectIdentity
snaDLC=_SnaDLC_ObjectIdentity((1,3,6,1,2,1,41))
_Sdlc_ObjectIdentity=ObjectIdentity
sdlc=_Sdlc_ObjectIdentity((1,3,6,1,2,1,41,1))
_SdlcLSGroup_ObjectIdentity=ObjectIdentity
sdlcLSGroup=_SdlcLSGroup_ObjectIdentity((1,3,6,1,2,1,41,1,2))
_SdlcLSAdminTable_ObjectIdentity=ObjectIdentity
sdlcLSAdminTable=_SdlcLSAdminTable_ObjectIdentity((1,3,6,1,2,1,41,1,2,1))
_SdlcLSAdminEntry_ObjectIdentity=ObjectIdentity
sdlcLSAdminEntry=_SdlcLSAdminEntry_ObjectIdentity((1,3,6,1,2,1,41,1,2,1,1))
class _SdlcLSAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SdlcLSAddress_Type.__name__=_B
_SdlcLSAddress_Object=MibScalar
sdlcLSAddress=_SdlcLSAddress_Object((1,3,6,1,2,1,41,1,2,1,1,1),_SdlcLSAddress_Type())
sdlcLSAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sdlcLSAddress.setStatus(_A)
_Netlink_ObjectIdentity=ObjectIdentity
netlink=_Netlink_ObjectIdentity((1,3,6,1,4,1,173))
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,173,6))
_Netstat_ObjectIdentity=ObjectIdentity
netstat=_Netstat_ObjectIdentity((1,3,6,1,4,1,173,6,1))
_NsMaxNeigh_Type=Integer32
_NsMaxNeigh_Object=MibScalar
nsMaxNeigh=_NsMaxNeigh_Object((1,3,6,1,4,1,173,6,1,1),_NsMaxNeigh_Type())
nsMaxNeigh.setMaxAccess(_C)
if mibBuilder.loadTexts:nsMaxNeigh.setStatus(_A)
_NsThisNode_Type=Integer32
_NsThisNode_Object=MibScalar
nsThisNode=_NsThisNode_Object((1,3,6,1,4,1,173,6,1,2),_NsThisNode_Type())
nsThisNode.setMaxAccess(_C)
if mibBuilder.loadTexts:nsThisNode.setStatus(_A)
_NsNodTable_Object=MibTable
nsNodTable=_NsNodTable_Object((1,3,6,1,4,1,173,6,1,3))
if mibBuilder.loadTexts:nsNodTable.setStatus(_A)
_NsEntry_Object=MibTableRow
nsEntry=_NsEntry_Object((1,3,6,1,4,1,173,6,1,3,1))
nsEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:nsEntry.setStatus(_A)
_NsNodNum_Type=Integer32
_NsNodNum_Object=MibTableColumn
nsNodNum=_NsNodNum_Object((1,3,6,1,4,1,173,6,1,3,1,1),_NsNodNum_Type())
nsNodNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNodNum.setStatus(_A)
_NsStatus_Type=Integer32
_NsStatus_Object=MibTableColumn
nsStatus=_NsStatus_Object((1,3,6,1,4,1,173,6,1,3,1,2),_NsStatus_Type())
nsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nsStatus.setStatus(_A)
_NsNumNeigh_Type=Integer32
_NsNumNeigh_Object=MibTableColumn
nsNumNeigh=_NsNumNeigh_Object((1,3,6,1,4,1,173,6,1,3,1,3),_NsNumNeigh_Type())
nsNumNeigh.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNumNeigh.setStatus(_A)
_NsNeighTable_Object=MibTable
nsNeighTable=_NsNeighTable_Object((1,3,6,1,4,1,173,6,1,4))
if mibBuilder.loadTexts:nsNeighTable.setStatus(_A)
_NsNeighEntry_Object=MibTableRow
nsNeighEntry=_NsNeighEntry_Object((1,3,6,1,4,1,173,6,1,4,1))
nsNeighEntry.setIndexNames((0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:nsNeighEntry.setStatus(_A)
_NsNTNode_Type=Integer32
_NsNTNode_Object=MibTableColumn
nsNTNode=_NsNTNode_Object((1,3,6,1,4,1,173,6,1,4,1,1),_NsNTNode_Type())
nsNTNode.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNTNode.setStatus(_A)
_NsNTNeigh_Type=Integer32
_NsNTNeigh_Object=MibTableColumn
nsNTNeigh=_NsNTNeigh_Object((1,3,6,1,4,1,173,6,1,4,1,2),_NsNTNeigh_Type())
nsNTNeigh.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNTNeigh.setStatus(_A)
class _NsNTNeighStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notConnected',1),('connected',2)))
_NsNTNeighStat_Type.__name__=_B
_NsNTNeighStat_Object=MibTableColumn
nsNTNeighStat=_NsNTNeighStat_Object((1,3,6,1,4,1,173,6,1,4,1,3),_NsNTNeighStat_Type())
nsNTNeighStat.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNTNeighStat.setStatus(_A)
_Local_ObjectIdentity=ObjectIdentity
local=_Local_ObjectIdentity((1,3,6,1,4,1,173,7))
_Node_ObjectIdentity=ObjectIdentity
node=_Node_ObjectIdentity((1,3,6,1,4,1,173,7,1))
_NodeCfgTable_ObjectIdentity=ObjectIdentity
nodeCfgTable=_NodeCfgTable_ObjectIdentity((1,3,6,1,4,1,173,7,1,1))
_NodeAlmTable_ObjectIdentity=ObjectIdentity
nodeAlmTable=_NodeAlmTable_ObjectIdentity((1,3,6,1,4,1,173,7,1,2))
_NodeSNMPGroup_ObjectIdentity=ObjectIdentity
nodeSNMPGroup=_NodeSNMPGroup_ObjectIdentity((1,3,6,1,4,1,173,7,1,3))
class _NodeModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('model1',1),('model2',2),('rackmount',3),('highavail',4),('netfrad',5),('frx4000',6),('ss1800',7)))
_NodeModel_Type.__name__=_B
_NodeModel_Object=MibScalar
nodeModel=_NodeModel_Object((1,3,6,1,4,1,173,7,1,3,1),_NodeModel_Type())
nodeModel.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeModel.setStatus(_A)
_NodeTrapText_Type=DisplayString
_NodeTrapText_Object=MibScalar
nodeTrapText=_NodeTrapText_Object((1,3,6,1,4,1,173,7,1,3,2),_NodeTrapText_Type())
nodeTrapText.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeTrapText.setStatus(_A)
_NodeTrapAdrTable_Object=MibTable
nodeTrapAdrTable=_NodeTrapAdrTable_Object((1,3,6,1,4,1,173,7,1,3,3))
if mibBuilder.loadTexts:nodeTrapAdrTable.setStatus(_A)
_TpAdrEntry_Object=MibTableRow
tpAdrEntry=_TpAdrEntry_Object((1,3,6,1,4,1,173,7,1,3,3,1))
tpAdrEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:tpAdrEntry.setStatus(_A)
_TpAdrIdx_Type=Integer32
_TpAdrIdx_Object=MibTableColumn
tpAdrIdx=_TpAdrIdx_Object((1,3,6,1,4,1,173,7,1,3,3,1,1),_TpAdrIdx_Type())
tpAdrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:tpAdrIdx.setStatus(_A)
_TpAddress_Type=IpAddress
_TpAddress_Object=MibTableColumn
tpAddress=_TpAddress_Object((1,3,6,1,4,1,173,7,1,3,3,1,2),_TpAddress_Type())
tpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAddress.setStatus(_A)
class _TpAdrFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disableTraps',1),('enableTraps',2),('delete',3)))
_TpAdrFlag_Type.__name__=_B
_TpAdrFlag_Object=MibTableColumn
tpAdrFlag=_TpAdrFlag_Object((1,3,6,1,4,1,173,7,1,3,3,1,3),_TpAdrFlag_Type())
tpAdrFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAdrFlag.setStatus(_A)
class _TpAdrSLev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('informational',4)))
_TpAdrSLev_Type.__name__=_B
_TpAdrSLev_Object=MibTableColumn
tpAdrSLev=_TpAdrSLev_Object((1,3,6,1,4,1,173,7,1,3,3,1,4),_TpAdrSLev_Type())
tpAdrSLev.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAdrSLev.setStatus(_A)
_NodeBagTable_ObjectIdentity=ObjectIdentity
nodeBagTable=_NodeBagTable_ObjectIdentity((1,3,6,1,4,1,173,7,1,4))
_Hwcard_ObjectIdentity=ObjectIdentity
hwcard=_Hwcard_ObjectIdentity((1,3,6,1,4,1,173,7,2))
_RlpMaxProtos_Type=Integer32
_RlpMaxProtos_Object=MibScalar
rlpMaxProtos=_RlpMaxProtos_Object((1,3,6,1,4,1,173,7,2,1),_RlpMaxProtos_Type())
rlpMaxProtos.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpMaxProtos.setStatus(_A)
_RlpConfigTable_Object=MibTable
rlpConfigTable=_RlpConfigTable_Object((1,3,6,1,4,1,173,7,2,2))
if mibBuilder.loadTexts:rlpConfigTable.setStatus(_A)
_RlpEntry_Object=MibTableRow
rlpEntry=_RlpEntry_Object((1,3,6,1,4,1,173,7,2,2,1))
rlpEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:rlpEntry.setStatus(_A)
_RlpIndex_Type=Integer32
_RlpIndex_Object=MibTableColumn
rlpIndex=_RlpIndex_Object((1,3,6,1,4,1,173,7,2,2,1,1),_RlpIndex_Type())
rlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpIndex.setStatus(_A)
class _RlpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('installed',1),(_A0,2),('load-failed',3),('loading',4),('ipl-failed',5),('ipl-in-progress',6),('failed',7),(_A1,8),('power-off',9),('power-on',10)))
_RlpStatus_Type.__name__=_B
_RlpStatus_Object=MibTableColumn
rlpStatus=_RlpStatus_Object((1,3,6,1,4,1,173,7,2,2,1,2),_RlpStatus_Type())
rlpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatus.setStatus(_A)
_RlpMemorySize_Type=Integer32
_RlpMemorySize_Object=MibTableColumn
rlpMemorySize=_RlpMemorySize_Object((1,3,6,1,4,1,173,7,2,2,1,3),_RlpMemorySize_Type())
rlpMemorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpMemorySize.setStatus(_A)
class _RlpLIC1Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,11,13)));namedValues=NamedValues(*((_L,1),(_N,2),('rs422',3),(_O,4),('hs-rs232',5),(_Q,6),(_R,7),(_A2,8),(_P,10),(_U,11),(_W,13)))
_RlpLIC1Type_Type.__name__=_B
_RlpLIC1Type_Object=MibTableColumn
rlpLIC1Type=_RlpLIC1Type_Object((1,3,6,1,4,1,173,7,2,2,1,4),_RlpLIC1Type_Type())
rlpLIC1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpLIC1Type.setStatus(_A)
class _RlpLIC2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,10,11,13)));namedValues=NamedValues(*((_L,1),(_N,2),('rs422',3),(_O,4),('hs-rs232',5),(_Q,6),(_R,7),(_A2,8),(_P,10),(_U,11),(_W,13)))
_RlpLIC2Type_Type.__name__=_B
_RlpLIC2Type_Object=MibTableColumn
rlpLIC2Type=_RlpLIC2Type_Object((1,3,6,1,4,1,173,7,2,2,1,5),_RlpLIC2Type_Type())
rlpLIC2Type.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpLIC2Type.setStatus(_A)
_RlpProtocol_Type=OctetString
_RlpProtocol_Object=MibTableColumn
rlpProtocol=_RlpProtocol_Object((1,3,6,1,4,1,173,7,2,2,1,6),_RlpProtocol_Type())
rlpProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:rlpProtocol.setStatus(_A)
class _RlpGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RlpGroupNumber_Type.__name__=_B
_RlpGroupNumber_Object=MibTableColumn
rlpGroupNumber=_RlpGroupNumber_Object((1,3,6,1,4,1,173,7,2,2,1,7),_RlpGroupNumber_Type())
rlpGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpGroupNumber.setStatus(_A)
class _RlpGroupResponsibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_RlpGroupResponsibility_Type.__name__=_B
_RlpGroupResponsibility_Object=MibTableColumn
rlpGroupResponsibility=_RlpGroupResponsibility_Object((1,3,6,1,4,1,173,7,2,2,1,8),_RlpGroupResponsibility_Type())
rlpGroupResponsibility.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpGroupResponsibility.setStatus(_A)
_Port_ObjectIdentity=ObjectIdentity
port=_Port_ObjectIdentity((1,3,6,1,4,1,173,7,3))
_PortX25Group_ObjectIdentity=ObjectIdentity
portX25Group=_PortX25Group_ObjectIdentity((1,3,6,1,4,1,173,7,3,1))
_PortPhyX25AdminTable_Object=MibTable
portPhyX25AdminTable=_PortPhyX25AdminTable_Object((1,3,6,1,4,1,173,7,3,1,1))
if mibBuilder.loadTexts:portPhyX25AdminTable.setStatus(_A)
_PortPhyX25AdminEntry_Object=MibTableRow
portPhyX25AdminEntry=_PortPhyX25AdminEntry_Object((1,3,6,1,4,1,173,7,3,1,1,1))
portPhyX25AdminEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portPhyX25AdminEntry.setStatus(_A)
class _PortPhyX25AdminConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10,11)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10),(_U,11)))
_PortPhyX25AdminConnector_Type.__name__=_B
_PortPhyX25AdminConnector_Object=MibTableColumn
portPhyX25AdminConnector=_PortPhyX25AdminConnector_Object((1,3,6,1,4,1,173,7,3,1,1,1,1),_PortPhyX25AdminConnector_Type())
portPhyX25AdminConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminConnector.setStatus(_A)
class _PortPhyX25AdminSpeed_Type(Integer32):defaultValue=64000
_PortPhyX25AdminSpeed_Type.__name__=_B
_PortPhyX25AdminSpeed_Object=MibTableColumn
portPhyX25AdminSpeed=_PortPhyX25AdminSpeed_Object((1,3,6,1,4,1,173,7,3,1,1,1,2),_PortPhyX25AdminSpeed_Type())
portPhyX25AdminSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminSpeed.setStatus(_A)
class _PortPhyX25AdminGenerateClock_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortPhyX25AdminGenerateClock_Type.__name__=_B
_PortPhyX25AdminGenerateClock_Object=MibTableColumn
portPhyX25AdminGenerateClock=_PortPhyX25AdminGenerateClock_Object((1,3,6,1,4,1,173,7,3,1,1,1,3),_PortPhyX25AdminGenerateClock_Type())
portPhyX25AdminGenerateClock.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminGenerateClock.setStatus(_A)
class _PortPhyX25AdminRcvClockFromDTE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortPhyX25AdminRcvClockFromDTE_Type.__name__=_B
_PortPhyX25AdminRcvClockFromDTE_Object=MibTableColumn
portPhyX25AdminRcvClockFromDTE=_PortPhyX25AdminRcvClockFromDTE_Object((1,3,6,1,4,1,173,7,3,1,1,1,4),_PortPhyX25AdminRcvClockFromDTE_Type())
portPhyX25AdminRcvClockFromDTE.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminRcvClockFromDTE.setStatus(_A)
class _PortPhyX25AdminDialOut_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('dialIn',2),('dialOut',3)))
_PortPhyX25AdminDialOut_Type.__name__=_B
_PortPhyX25AdminDialOut_Object=MibTableColumn
portPhyX25AdminDialOut=_PortPhyX25AdminDialOut_Object((1,3,6,1,4,1,173,7,3,1,1,1,5),_PortPhyX25AdminDialOut_Type())
portPhyX25AdminDialOut.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminDialOut.setStatus(_A)
class _PortPhyX25AdminInactivityTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PortPhyX25AdminInactivityTimer_Type.__name__=_B
_PortPhyX25AdminInactivityTimer_Object=MibTableColumn
portPhyX25AdminInactivityTimer=_PortPhyX25AdminInactivityTimer_Object((1,3,6,1,4,1,173,7,3,1,1,1,6),_PortPhyX25AdminInactivityTimer_Type())
portPhyX25AdminInactivityTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminInactivityTimer.setStatus(_A)
class _PortPhyX25AdminDisconnectTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortPhyX25AdminDisconnectTimer_Type.__name__=_B
_PortPhyX25AdminDisconnectTimer_Object=MibTableColumn
portPhyX25AdminDisconnectTimer=_PortPhyX25AdminDisconnectTimer_Object((1,3,6,1,4,1,173,7,3,1,1,1,7),_PortPhyX25AdminDisconnectTimer_Type())
portPhyX25AdminDisconnectTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminDisconnectTimer.setStatus(_A)
class _PortPhyX25AdminSetupTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortPhyX25AdminSetupTimer_Type.__name__=_B
_PortPhyX25AdminSetupTimer_Object=MibTableColumn
portPhyX25AdminSetupTimer=_PortPhyX25AdminSetupTimer_Object((1,3,6,1,4,1,173,7,3,1,1,1,8),_PortPhyX25AdminSetupTimer_Type())
portPhyX25AdminSetupTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminSetupTimer.setStatus(_A)
class _PortPhyX25AdminTrunkFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortPhyX25AdminTrunkFlag_Type.__name__=_B
_PortPhyX25AdminTrunkFlag_Object=MibTableColumn
portPhyX25AdminTrunkFlag=_PortPhyX25AdminTrunkFlag_Object((1,3,6,1,4,1,173,7,3,1,1,1,9),_PortPhyX25AdminTrunkFlag_Type())
portPhyX25AdminTrunkFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminTrunkFlag.setStatus(_A)
_PortPhyX25AdminTrunkGroup_Type=OctetString
_PortPhyX25AdminTrunkGroup_Object=MibTableColumn
portPhyX25AdminTrunkGroup=_PortPhyX25AdminTrunkGroup_Object((1,3,6,1,4,1,173,7,3,1,1,1,10),_PortPhyX25AdminTrunkGroup_Type())
portPhyX25AdminTrunkGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminTrunkGroup.setStatus(_A)
_PortPhyX25AdminRowStatus_Type=RowStatus
_PortPhyX25AdminRowStatus_Object=MibTableColumn
portPhyX25AdminRowStatus=_PortPhyX25AdminRowStatus_Object((1,3,6,1,4,1,173,7,3,1,1,1,11),_PortPhyX25AdminRowStatus_Type())
portPhyX25AdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portPhyX25AdminRowStatus.setStatus(_A)
_PortPhyX25OperTable_Object=MibTable
portPhyX25OperTable=_PortPhyX25OperTable_Object((1,3,6,1,4,1,173,7,3,1,2))
if mibBuilder.loadTexts:portPhyX25OperTable.setStatus(_A)
_PortPhyX25OperEntry_Object=MibTableRow
portPhyX25OperEntry=_PortPhyX25OperEntry_Object((1,3,6,1,4,1,173,7,3,1,2,1))
portPhyX25OperEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portPhyX25OperEntry.setStatus(_A)
class _PortPhyX25OperConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10,11)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10),(_U,11)))
_PortPhyX25OperConnector_Type.__name__=_B
_PortPhyX25OperConnector_Object=MibTableColumn
portPhyX25OperConnector=_PortPhyX25OperConnector_Object((1,3,6,1,4,1,173,7,3,1,2,1,1),_PortPhyX25OperConnector_Type())
portPhyX25OperConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperConnector.setStatus(_A)
_PortPhyX25OperSpeed_Type=Integer32
_PortPhyX25OperSpeed_Object=MibTableColumn
portPhyX25OperSpeed=_PortPhyX25OperSpeed_Object((1,3,6,1,4,1,173,7,3,1,2,1,2),_PortPhyX25OperSpeed_Type())
portPhyX25OperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperSpeed.setStatus(_A)
class _PortPhyX25OperGenerateClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortPhyX25OperGenerateClock_Type.__name__=_B
_PortPhyX25OperGenerateClock_Object=MibTableColumn
portPhyX25OperGenerateClock=_PortPhyX25OperGenerateClock_Object((1,3,6,1,4,1,173,7,3,1,2,1,3),_PortPhyX25OperGenerateClock_Type())
portPhyX25OperGenerateClock.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperGenerateClock.setStatus(_A)
class _PortPhyX25OperRcvClockFromDTE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortPhyX25OperRcvClockFromDTE_Type.__name__=_B
_PortPhyX25OperRcvClockFromDTE_Object=MibTableColumn
portPhyX25OperRcvClockFromDTE=_PortPhyX25OperRcvClockFromDTE_Object((1,3,6,1,4,1,173,7,3,1,2,1,4),_PortPhyX25OperRcvClockFromDTE_Type())
portPhyX25OperRcvClockFromDTE.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperRcvClockFromDTE.setStatus(_A)
class _PortPhyX25OperDialOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('dialIn',2),('dialOut',3)))
_PortPhyX25OperDialOut_Type.__name__=_B
_PortPhyX25OperDialOut_Object=MibTableColumn
portPhyX25OperDialOut=_PortPhyX25OperDialOut_Object((1,3,6,1,4,1,173,7,3,1,2,1,5),_PortPhyX25OperDialOut_Type())
portPhyX25OperDialOut.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperDialOut.setStatus(_A)
class _PortPhyX25OperInactivityTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PortPhyX25OperInactivityTimer_Type.__name__=_B
_PortPhyX25OperInactivityTimer_Object=MibTableColumn
portPhyX25OperInactivityTimer=_PortPhyX25OperInactivityTimer_Object((1,3,6,1,4,1,173,7,3,1,2,1,6),_PortPhyX25OperInactivityTimer_Type())
portPhyX25OperInactivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperInactivityTimer.setStatus(_A)
class _PortPhyX25OperDisconnectTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortPhyX25OperDisconnectTimer_Type.__name__=_B
_PortPhyX25OperDisconnectTimer_Object=MibTableColumn
portPhyX25OperDisconnectTimer=_PortPhyX25OperDisconnectTimer_Object((1,3,6,1,4,1,173,7,3,1,2,1,7),_PortPhyX25OperDisconnectTimer_Type())
portPhyX25OperDisconnectTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperDisconnectTimer.setStatus(_A)
class _PortPhyX25OperSetupTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortPhyX25OperSetupTimer_Type.__name__=_B
_PortPhyX25OperSetupTimer_Object=MibTableColumn
portPhyX25OperSetupTimer=_PortPhyX25OperSetupTimer_Object((1,3,6,1,4,1,173,7,3,1,2,1,8),_PortPhyX25OperSetupTimer_Type())
portPhyX25OperSetupTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperSetupTimer.setStatus(_A)
class _PortPhyX25OperTrunkFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortPhyX25OperTrunkFlag_Type.__name__=_B
_PortPhyX25OperTrunkFlag_Object=MibTableColumn
portPhyX25OperTrunkFlag=_PortPhyX25OperTrunkFlag_Object((1,3,6,1,4,1,173,7,3,1,2,1,9),_PortPhyX25OperTrunkFlag_Type())
portPhyX25OperTrunkFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperTrunkFlag.setStatus(_A)
_PortPhyX25OperTrunkGroup_Type=OctetString
_PortPhyX25OperTrunkGroup_Object=MibTableColumn
portPhyX25OperTrunkGroup=_PortPhyX25OperTrunkGroup_Object((1,3,6,1,4,1,173,7,3,1,2,1,10),_PortPhyX25OperTrunkGroup_Type())
portPhyX25OperTrunkGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:portPhyX25OperTrunkGroup.setStatus(_A)
_PortLogicalX25AdminTable_Object=MibTable
portLogicalX25AdminTable=_PortLogicalX25AdminTable_Object((1,3,6,1,4,1,173,7,3,1,3))
if mibBuilder.loadTexts:portLogicalX25AdminTable.setStatus(_A)
_PortLogicalX25AdminEntry_Object=MibTableRow
portLogicalX25AdminEntry=_PortLogicalX25AdminEntry_Object((1,3,6,1,4,1,173,7,3,1,3,1))
portLogicalX25AdminEntry.setIndexNames((0,_E,_H),(0,_E,_l),(0,_E,_I))
if mibBuilder.loadTexts:portLogicalX25AdminEntry.setStatus(_A)
class _PortLogicalX25AdminFrDlci_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_PortLogicalX25AdminFrDlci_Type.__name__=_B
_PortLogicalX25AdminFrDlci_Object=MibTableColumn
portLogicalX25AdminFrDlci=_PortLogicalX25AdminFrDlci_Object((1,3,6,1,4,1,173,7,3,1,3,1,1),_PortLogicalX25AdminFrDlci_Type())
portLogicalX25AdminFrDlci.setMaxAccess(_D)
if mibBuilder.loadTexts:portLogicalX25AdminFrDlci.setStatus(_A)
class _PortLogicalX25AdminCxnPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_PortLogicalX25AdminCxnPriority_Type.__name__=_B
_PortLogicalX25AdminCxnPriority_Object=MibTableColumn
portLogicalX25AdminCxnPriority=_PortLogicalX25AdminCxnPriority_Object((1,3,6,1,4,1,173,7,3,1,3,1,2),_PortLogicalX25AdminCxnPriority_Type())
portLogicalX25AdminCxnPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:portLogicalX25AdminCxnPriority.setStatus(_A)
class _PortLogicalX25AdminRfc1490_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('annexG',1),('rfc1490',2)))
_PortLogicalX25AdminRfc1490_Type.__name__=_B
_PortLogicalX25AdminRfc1490_Object=MibTableColumn
portLogicalX25AdminRfc1490=_PortLogicalX25AdminRfc1490_Object((1,3,6,1,4,1,173,7,3,1,3,1,3),_PortLogicalX25AdminRfc1490_Type())
portLogicalX25AdminRfc1490.setMaxAccess(_D)
if mibBuilder.loadTexts:portLogicalX25AdminRfc1490.setStatus(_A)
class _PortLogicalX25AdminBAG_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_PortLogicalX25AdminBAG_Type.__name__=_B
_PortLogicalX25AdminBAG_Object=MibTableColumn
portLogicalX25AdminBAG=_PortLogicalX25AdminBAG_Object((1,3,6,1,4,1,173,7,3,1,3,1,4),_PortLogicalX25AdminBAG_Type())
portLogicalX25AdminBAG.setMaxAccess(_D)
if mibBuilder.loadTexts:portLogicalX25AdminBAG.setStatus(_A)
_PortLogicalX25AdminRowStatus_Type=RowStatus
_PortLogicalX25AdminRowStatus_Object=MibTableColumn
portLogicalX25AdminRowStatus=_PortLogicalX25AdminRowStatus_Object((1,3,6,1,4,1,173,7,3,1,3,1,5),_PortLogicalX25AdminRowStatus_Type())
portLogicalX25AdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portLogicalX25AdminRowStatus.setStatus(_A)
_PortLogicalX25OperTable_Object=MibTable
portLogicalX25OperTable=_PortLogicalX25OperTable_Object((1,3,6,1,4,1,173,7,3,1,4))
if mibBuilder.loadTexts:portLogicalX25OperTable.setStatus(_A)
_PortLogicalX25OperEntry_Object=MibTableRow
portLogicalX25OperEntry=_PortLogicalX25OperEntry_Object((1,3,6,1,4,1,173,7,3,1,4,1))
portLogicalX25OperEntry.setIndexNames((0,_E,_H),(0,_E,_l),(0,_E,_I))
if mibBuilder.loadTexts:portLogicalX25OperEntry.setStatus(_A)
class _PortLogicalX25OperFrDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortLogicalX25OperFrDlci_Type.__name__=_B
_PortLogicalX25OperFrDlci_Object=MibTableColumn
portLogicalX25OperFrDlci=_PortLogicalX25OperFrDlci_Object((1,3,6,1,4,1,173,7,3,1,4,1,1),_PortLogicalX25OperFrDlci_Type())
portLogicalX25OperFrDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:portLogicalX25OperFrDlci.setStatus(_A)
class _PortLogicalX25OperCxnPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_PortLogicalX25OperCxnPriority_Type.__name__=_B
_PortLogicalX25OperCxnPriority_Object=MibTableColumn
portLogicalX25OperCxnPriority=_PortLogicalX25OperCxnPriority_Object((1,3,6,1,4,1,173,7,3,1,4,1,2),_PortLogicalX25OperCxnPriority_Type())
portLogicalX25OperCxnPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:portLogicalX25OperCxnPriority.setStatus(_A)
class _PortLogicalX25OperRfc1490_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('annexG',1),('rfc1490',2)))
_PortLogicalX25OperRfc1490_Type.__name__=_B
_PortLogicalX25OperRfc1490_Object=MibTableColumn
portLogicalX25OperRfc1490=_PortLogicalX25OperRfc1490_Object((1,3,6,1,4,1,173,7,3,1,4,1,3),_PortLogicalX25OperRfc1490_Type())
portLogicalX25OperRfc1490.setMaxAccess(_C)
if mibBuilder.loadTexts:portLogicalX25OperRfc1490.setStatus(_A)
class _PortLogicalX25OperBAG_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PortLogicalX25OperBAG_Type.__name__=_B
_PortLogicalX25OperBAG_Object=MibTableColumn
portLogicalX25OperBAG=_PortLogicalX25OperBAG_Object((1,3,6,1,4,1,173,7,3,1,4,1,4),_PortLogicalX25OperBAG_Type())
portLogicalX25OperBAG.setMaxAccess(_C)
if mibBuilder.loadTexts:portLogicalX25OperBAG.setStatus(_A)
_PortX25AdminTable_Object=MibTable
portX25AdminTable=_PortX25AdminTable_Object((1,3,6,1,4,1,173,7,3,1,5))
if mibBuilder.loadTexts:portX25AdminTable.setStatus(_A)
_PortX25AdminEntry_Object=MibTableRow
portX25AdminEntry=_PortX25AdminEntry_Object((1,3,6,1,4,1,173,7,3,1,5,1))
portX25AdminEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portX25AdminEntry.setStatus(_A)
class _PortX25AdminBlockedFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminBlockedFlag_Type.__name__=_B
_PortX25AdminBlockedFlag_Object=MibTableColumn
portX25AdminBlockedFlag=_PortX25AdminBlockedFlag_Object((1,3,6,1,4,1,173,7,3,1,5,1,1),_PortX25AdminBlockedFlag_Type())
portX25AdminBlockedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminBlockedFlag.setStatus(_A)
class _PortX25AdminFlowCtrlNeg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminFlowCtrlNeg_Type.__name__=_B
_PortX25AdminFlowCtrlNeg_Object=MibTableColumn
portX25AdminFlowCtrlNeg=_PortX25AdminFlowCtrlNeg_Object((1,3,6,1,4,1,173,7,3,1,5,1,2),_PortX25AdminFlowCtrlNeg_Type())
portX25AdminFlowCtrlNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminFlowCtrlNeg.setStatus(_A)
class _PortX25AdminThruptClassNeg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminThruptClassNeg_Type.__name__=_B
_PortX25AdminThruptClassNeg_Object=MibTableColumn
portX25AdminThruptClassNeg=_PortX25AdminThruptClassNeg_Object((1,3,6,1,4,1,173,7,3,1,5,1,3),_PortX25AdminThruptClassNeg_Type())
portX25AdminThruptClassNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminThruptClassNeg.setStatus(_A)
class _PortX25AdminLocChgPrev_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminLocChgPrev_Type.__name__=_B
_PortX25AdminLocChgPrev_Object=MibTableColumn
portX25AdminLocChgPrev=_PortX25AdminLocChgPrev_Object((1,3,6,1,4,1,173,7,3,1,5,1,4),_PortX25AdminLocChgPrev_Type())
portX25AdminLocChgPrev.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminLocChgPrev.setStatus(_A)
class _PortX25AdminRevChgAccpt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminRevChgAccpt_Type.__name__=_B
_PortX25AdminRevChgAccpt_Object=MibTableColumn
portX25AdminRevChgAccpt=_PortX25AdminRevChgAccpt_Object((1,3,6,1,4,1,173,7,3,1,5,1,5),_PortX25AdminRevChgAccpt_Type())
portX25AdminRevChgAccpt.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminRevChgAccpt.setStatus(_A)
class _PortX25AdminFastSelAccpt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminFastSelAccpt_Type.__name__=_B
_PortX25AdminFastSelAccpt_Object=MibTableColumn
portX25AdminFastSelAccpt=_PortX25AdminFastSelAccpt_Object((1,3,6,1,4,1,173,7,3,1,5,1,6),_PortX25AdminFastSelAccpt_Type())
portX25AdminFastSelAccpt.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminFastSelAccpt.setStatus(_A)
class _PortX25AdminInCallBar_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminInCallBar_Type.__name__=_B
_PortX25AdminInCallBar_Object=MibTableColumn
portX25AdminInCallBar=_PortX25AdminInCallBar_Object((1,3,6,1,4,1,173,7,3,1,5,1,7),_PortX25AdminInCallBar_Type())
portX25AdminInCallBar.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminInCallBar.setStatus(_A)
class _PortX25AdminOutCallBar_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminOutCallBar_Type.__name__=_B
_PortX25AdminOutCallBar_Object=MibTableColumn
portX25AdminOutCallBar=_PortX25AdminOutCallBar_Object((1,3,6,1,4,1,173,7,3,1,5,1,8),_PortX25AdminOutCallBar_Type())
portX25AdminOutCallBar.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminOutCallBar.setStatus(_A)
class _PortX25AdminMaxPktSize_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,4096))
_PortX25AdminMaxPktSize_Type.__name__=_B
_PortX25AdminMaxPktSize_Object=MibTableColumn
portX25AdminMaxPktSize=_PortX25AdminMaxPktSize_Object((1,3,6,1,4,1,173,7,3,1,5,1,9),_PortX25AdminMaxPktSize_Type())
portX25AdminMaxPktSize.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminMaxPktSize.setStatus(_A)
class _PortX25AdminDefPktSize_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_PortX25AdminDefPktSize_Type.__name__=_B
_PortX25AdminDefPktSize_Object=MibTableColumn
portX25AdminDefPktSize=_PortX25AdminDefPktSize_Object((1,3,6,1,4,1,173,7,3,1,5,1,10),_PortX25AdminDefPktSize_Type())
portX25AdminDefPktSize.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminDefPktSize.setStatus(_A)
class _PortX25AdminMaxWinSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_PortX25AdminMaxWinSize_Type.__name__=_B
_PortX25AdminMaxWinSize_Object=MibTableColumn
portX25AdminMaxWinSize=_PortX25AdminMaxWinSize_Object((1,3,6,1,4,1,173,7,3,1,5,1,11),_PortX25AdminMaxWinSize_Type())
portX25AdminMaxWinSize.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminMaxWinSize.setStatus(_A)
class _PortX25AdminDefWinSize_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PortX25AdminDefWinSize_Type.__name__=_B
_PortX25AdminDefWinSize_Object=MibTableColumn
portX25AdminDefWinSize=_PortX25AdminDefWinSize_Object((1,3,6,1,4,1,173,7,3,1,5,1,12),_PortX25AdminDefWinSize_Type())
portX25AdminDefWinSize.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminDefWinSize.setStatus(_A)
class _PortX25AdminMaxThruptClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,13))
_PortX25AdminMaxThruptClass_Type.__name__=_B
_PortX25AdminMaxThruptClass_Object=MibTableColumn
portX25AdminMaxThruptClass=_PortX25AdminMaxThruptClass_Object((1,3,6,1,4,1,173,7,3,1,5,1,13),_PortX25AdminMaxThruptClass_Type())
portX25AdminMaxThruptClass.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminMaxThruptClass.setStatus(_A)
class _PortX25AdminCUGPref_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminCUGPref_Type.__name__=_B
_PortX25AdminCUGPref_Object=MibTableColumn
portX25AdminCUGPref=_PortX25AdminCUGPref_Object((1,3,6,1,4,1,173,7,3,1,5,1,14),_PortX25AdminCUGPref_Type())
portX25AdminCUGPref.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminCUGPref.setStatus(_A)
class _PortX25AdminCUGIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PortX25AdminCUGIndex_Type.__name__=_B
_PortX25AdminCUGIndex_Object=MibTableColumn
portX25AdminCUGIndex=_PortX25AdminCUGIndex_Object((1,3,6,1,4,1,173,7,3,1,5,1,15),_PortX25AdminCUGIndex_Type())
portX25AdminCUGIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminCUGIndex.setStatus(_A)
class _PortX25AdminCUGIncAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminCUGIncAccess_Type.__name__=_B
_PortX25AdminCUGIncAccess_Object=MibTableColumn
portX25AdminCUGIncAccess=_PortX25AdminCUGIncAccess_Object((1,3,6,1,4,1,173,7,3,1,5,1,16),_PortX25AdminCUGIncAccess_Type())
portX25AdminCUGIncAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminCUGIncAccess.setStatus(_A)
class _PortX25AdminCUGOutAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25AdminCUGOutAccess_Type.__name__=_B
_PortX25AdminCUGOutAccess_Object=MibTableColumn
portX25AdminCUGOutAccess=_PortX25AdminCUGOutAccess_Object((1,3,6,1,4,1,173,7,3,1,5,1,17),_PortX25AdminCUGOutAccess_Type())
portX25AdminCUGOutAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:portX25AdminCUGOutAccess.setStatus(_A)
_PortX25OperTable_Object=MibTable
portX25OperTable=_PortX25OperTable_Object((1,3,6,1,4,1,173,7,3,1,6))
if mibBuilder.loadTexts:portX25OperTable.setStatus(_A)
_PortX25OperEntry_Object=MibTableRow
portX25OperEntry=_PortX25OperEntry_Object((1,3,6,1,4,1,173,7,3,1,6,1))
portX25OperEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portX25OperEntry.setStatus(_A)
class _PortX25OperBlockedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperBlockedFlag_Type.__name__=_B
_PortX25OperBlockedFlag_Object=MibTableColumn
portX25OperBlockedFlag=_PortX25OperBlockedFlag_Object((1,3,6,1,4,1,173,7,3,1,6,1,1),_PortX25OperBlockedFlag_Type())
portX25OperBlockedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperBlockedFlag.setStatus(_A)
class _PortX25OperFlowCtrlNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperFlowCtrlNeg_Type.__name__=_B
_PortX25OperFlowCtrlNeg_Object=MibTableColumn
portX25OperFlowCtrlNeg=_PortX25OperFlowCtrlNeg_Object((1,3,6,1,4,1,173,7,3,1,6,1,2),_PortX25OperFlowCtrlNeg_Type())
portX25OperFlowCtrlNeg.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperFlowCtrlNeg.setStatus(_A)
class _PortX25OperThruptClassNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperThruptClassNeg_Type.__name__=_B
_PortX25OperThruptClassNeg_Object=MibTableColumn
portX25OperThruptClassNeg=_PortX25OperThruptClassNeg_Object((1,3,6,1,4,1,173,7,3,1,6,1,3),_PortX25OperThruptClassNeg_Type())
portX25OperThruptClassNeg.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperThruptClassNeg.setStatus(_A)
class _PortX25OperLocChgPrev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperLocChgPrev_Type.__name__=_B
_PortX25OperLocChgPrev_Object=MibTableColumn
portX25OperLocChgPrev=_PortX25OperLocChgPrev_Object((1,3,6,1,4,1,173,7,3,1,6,1,4),_PortX25OperLocChgPrev_Type())
portX25OperLocChgPrev.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperLocChgPrev.setStatus(_A)
class _PortX25OperRevChgAccpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperRevChgAccpt_Type.__name__=_B
_PortX25OperRevChgAccpt_Object=MibTableColumn
portX25OperRevChgAccpt=_PortX25OperRevChgAccpt_Object((1,3,6,1,4,1,173,7,3,1,6,1,5),_PortX25OperRevChgAccpt_Type())
portX25OperRevChgAccpt.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperRevChgAccpt.setStatus(_A)
class _PortX25OperFastSelAccpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperFastSelAccpt_Type.__name__=_B
_PortX25OperFastSelAccpt_Object=MibTableColumn
portX25OperFastSelAccpt=_PortX25OperFastSelAccpt_Object((1,3,6,1,4,1,173,7,3,1,6,1,6),_PortX25OperFastSelAccpt_Type())
portX25OperFastSelAccpt.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperFastSelAccpt.setStatus(_A)
class _PortX25OperInCallBar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperInCallBar_Type.__name__=_B
_PortX25OperInCallBar_Object=MibTableColumn
portX25OperInCallBar=_PortX25OperInCallBar_Object((1,3,6,1,4,1,173,7,3,1,6,1,7),_PortX25OperInCallBar_Type())
portX25OperInCallBar.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperInCallBar.setStatus(_A)
class _PortX25OperOutCallBar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperOutCallBar_Type.__name__=_B
_PortX25OperOutCallBar_Object=MibTableColumn
portX25OperOutCallBar=_PortX25OperOutCallBar_Object((1,3,6,1,4,1,173,7,3,1,6,1,8),_PortX25OperOutCallBar_Type())
portX25OperOutCallBar.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperOutCallBar.setStatus(_A)
class _PortX25OperMaxPktSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,4096))
_PortX25OperMaxPktSize_Type.__name__=_B
_PortX25OperMaxPktSize_Object=MibTableColumn
portX25OperMaxPktSize=_PortX25OperMaxPktSize_Object((1,3,6,1,4,1,173,7,3,1,6,1,9),_PortX25OperMaxPktSize_Type())
portX25OperMaxPktSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperMaxPktSize.setStatus(_A)
class _PortX25OperDefPktSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_PortX25OperDefPktSize_Type.__name__=_B
_PortX25OperDefPktSize_Object=MibTableColumn
portX25OperDefPktSize=_PortX25OperDefPktSize_Object((1,3,6,1,4,1,173,7,3,1,6,1,10),_PortX25OperDefPktSize_Type())
portX25OperDefPktSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperDefPktSize.setStatus(_A)
class _PortX25OperMaxWinSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_PortX25OperMaxWinSize_Type.__name__=_B
_PortX25OperMaxWinSize_Object=MibTableColumn
portX25OperMaxWinSize=_PortX25OperMaxWinSize_Object((1,3,6,1,4,1,173,7,3,1,6,1,11),_PortX25OperMaxWinSize_Type())
portX25OperMaxWinSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperMaxWinSize.setStatus(_A)
class _PortX25OperDefWinSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PortX25OperDefWinSize_Type.__name__=_B
_PortX25OperDefWinSize_Object=MibTableColumn
portX25OperDefWinSize=_PortX25OperDefWinSize_Object((1,3,6,1,4,1,173,7,3,1,6,1,12),_PortX25OperDefWinSize_Type())
portX25OperDefWinSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperDefWinSize.setStatus(_A)
class _PortX25OperMaxThruptClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,13))
_PortX25OperMaxThruptClass_Type.__name__=_B
_PortX25OperMaxThruptClass_Object=MibTableColumn
portX25OperMaxThruptClass=_PortX25OperMaxThruptClass_Object((1,3,6,1,4,1,173,7,3,1,6,1,13),_PortX25OperMaxThruptClass_Type())
portX25OperMaxThruptClass.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperMaxThruptClass.setStatus(_A)
class _PortX25OperCUGPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperCUGPref_Type.__name__=_B
_PortX25OperCUGPref_Object=MibTableColumn
portX25OperCUGPref=_PortX25OperCUGPref_Object((1,3,6,1,4,1,173,7,3,1,6,1,14),_PortX25OperCUGPref_Type())
portX25OperCUGPref.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperCUGPref.setStatus(_A)
class _PortX25OperCUGIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PortX25OperCUGIndex_Type.__name__=_B
_PortX25OperCUGIndex_Object=MibTableColumn
portX25OperCUGIndex=_PortX25OperCUGIndex_Object((1,3,6,1,4,1,173,7,3,1,6,1,15),_PortX25OperCUGIndex_Type())
portX25OperCUGIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperCUGIndex.setStatus(_A)
class _PortX25OperCUGIncAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperCUGIncAccess_Type.__name__=_B
_PortX25OperCUGIncAccess_Object=MibTableColumn
portX25OperCUGIncAccess=_PortX25OperCUGIncAccess_Object((1,3,6,1,4,1,173,7,3,1,6,1,16),_PortX25OperCUGIncAccess_Type())
portX25OperCUGIncAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperCUGIncAccess.setStatus(_A)
class _PortX25OperCUGOutAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortX25OperCUGOutAccess_Type.__name__=_B
_PortX25OperCUGOutAccess_Object=MibTableColumn
portX25OperCUGOutAccess=_PortX25OperCUGOutAccess_Object((1,3,6,1,4,1,173,7,3,1,6,1,17),_PortX25OperCUGOutAccess_Type())
portX25OperCUGOutAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:portX25OperCUGOutAccess.setStatus(_A)
_PortFrGroup_ObjectIdentity=ObjectIdentity
portFrGroup=_PortFrGroup_ObjectIdentity((1,3,6,1,4,1,173,7,3,2))
_PortFrConfigTable_Object=MibTable
portFrConfigTable=_PortFrConfigTable_Object((1,3,6,1,4,1,173,7,3,2,1))
if mibBuilder.loadTexts:portFrConfigTable.setStatus(_A)
_PortFrEntry_Object=MibTableRow
portFrEntry=_PortFrEntry_Object((1,3,6,1,4,1,173,7,3,2,1,1))
portFrEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:portFrEntry.setStatus(_A)
_PortFrRlpIndex_Type=Integer32
_PortFrRlpIndex_Object=MibTableColumn
portFrRlpIndex=_PortFrRlpIndex_Object((1,3,6,1,4,1,173,7,3,2,1,1,1),_PortFrRlpIndex_Type())
portFrRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrRlpIndex.setStatus(_A)
_PortFrPortIndex_Type=Integer32
_PortFrPortIndex_Object=MibTableColumn
portFrPortIndex=_PortFrPortIndex_Object((1,3,6,1,4,1,173,7,3,2,1,1,2),_PortFrPortIndex_Type())
portFrPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrPortIndex.setStatus(_A)
class _PortFrBlockedFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrBlockedFlag_Type.__name__=_B
_PortFrBlockedFlag_Object=MibTableColumn
portFrBlockedFlag=_PortFrBlockedFlag_Object((1,3,6,1,4,1,173,7,3,2,1,1,3),_PortFrBlockedFlag_Type())
portFrBlockedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrBlockedFlag.setStatus(_A)
class _PortFrMaxBytesPerFrame_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_PortFrMaxBytesPerFrame_Type.__name__=_B
_PortFrMaxBytesPerFrame_Object=MibTableColumn
portFrMaxBytesPerFrame=_PortFrMaxBytesPerFrame_Object((1,3,6,1,4,1,173,7,3,2,1,1,4),_PortFrMaxBytesPerFrame_Type())
portFrMaxBytesPerFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrMaxBytesPerFrame.setStatus(_A)
class _PortFrT392Timer_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_PortFrT392Timer_Type.__name__=_B
_PortFrT392Timer_Object=MibTableColumn
portFrT392Timer=_PortFrT392Timer_Object((1,3,6,1,4,1,173,7,3,2,1,1,5),_PortFrT392Timer_Type())
portFrT392Timer.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrT392Timer.setStatus(_A)
class _PortFrOutgoingRateControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrOutgoingRateControl_Type.__name__=_B
_PortFrOutgoingRateControl_Object=MibTableColumn
portFrOutgoingRateControl=_PortFrOutgoingRateControl_Object((1,3,6,1,4,1,173,7,3,2,1,1,6),_PortFrOutgoingRateControl_Type())
portFrOutgoingRateControl.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrOutgoingRateControl.setStatus(_A)
class _PortFrBandwidthAllocation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrBandwidthAllocation_Type.__name__=_B
_PortFrBandwidthAllocation_Object=MibTableColumn
portFrBandwidthAllocation=_PortFrBandwidthAllocation_Object((1,3,6,1,4,1,173,7,3,2,1,1,7),_PortFrBandwidthAllocation_Type())
portFrBandwidthAllocation.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrBandwidthAllocation.setStatus(_A)
class _PortFrConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10,11)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10),(_U,11)))
_PortFrConnector_Type.__name__=_B
_PortFrConnector_Object=MibTableColumn
portFrConnector=_PortFrConnector_Object((1,3,6,1,4,1,173,7,3,2,1,1,8),_PortFrConnector_Type())
portFrConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrConnector.setStatus(_A)
class _PortFrLogicalDCE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrLogicalDCE_Type.__name__=_B
_PortFrLogicalDCE_Object=MibTableColumn
portFrLogicalDCE=_PortFrLogicalDCE_Object((1,3,6,1,4,1,173,7,3,2,1,1,9),_PortFrLogicalDCE_Type())
portFrLogicalDCE.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrLogicalDCE.setStatus(_A)
class _PortFrGenClock_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrGenClock_Type.__name__=_B
_PortFrGenClock_Object=MibTableColumn
portFrGenClock=_PortFrGenClock_Object((1,3,6,1,4,1,173,7,3,2,1,1,10),_PortFrGenClock_Type())
portFrGenClock.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrGenClock.setStatus(_A)
class _PortFrRcvClkFrmDTE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrRcvClkFrmDTE_Type.__name__=_B
_PortFrRcvClkFrmDTE_Object=MibTableColumn
portFrRcvClkFrmDTE=_PortFrRcvClkFrmDTE_Object((1,3,6,1,4,1,173,7,3,2,1,1,11),_PortFrRcvClkFrmDTE_Type())
portFrRcvClkFrmDTE.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrRcvClkFrmDTE.setStatus(_A)
class _PortFrLLM_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('lmi',2),('annexd',3)))
_PortFrLLM_Type.__name__=_B
_PortFrLLM_Object=MibTableColumn
portFrLLM=_PortFrLLM_Object((1,3,6,1,4,1,173,7,3,2,1,1,12),_PortFrLLM_Type())
portFrLLM.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrLLM.setStatus(_A)
_PortFrRowStatus_Type=RowStatus
_PortFrRowStatus_Object=MibTableColumn
portFrRowStatus=_PortFrRowStatus_Object((1,3,6,1,4,1,173,7,3,2,1,1,13),_PortFrRowStatus_Type())
portFrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrRowStatus.setStatus(_A)
class _PortFrSpeed_Type(Integer32):defaultValue=64000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,2048000))
_PortFrSpeed_Type.__name__=_B
_PortFrSpeed_Object=MibTableColumn
portFrSpeed=_PortFrSpeed_Object((1,3,6,1,4,1,173,7,3,2,1,1,14),_PortFrSpeed_Type())
portFrSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrSpeed.setStatus(_A)
class _PortFrBackupUseOnly_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrBackupUseOnly_Type.__name__=_B
_PortFrBackupUseOnly_Object=MibTableColumn
portFrBackupUseOnly=_PortFrBackupUseOnly_Object((1,3,6,1,4,1,173,7,3,2,1,1,15),_PortFrBackupUseOnly_Type())
portFrBackupUseOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrBackupUseOnly.setStatus(_A)
_PortDLCIConfigTable_Object=MibTable
portDLCIConfigTable=_PortDLCIConfigTable_Object((1,3,6,1,4,1,173,7,3,2,2))
if mibBuilder.loadTexts:portDLCIConfigTable.setStatus(_A)
_PortDLCIEntry_Object=MibTableRow
portDLCIEntry=_PortDLCIEntry_Object((1,3,6,1,4,1,173,7,3,2,2,1))
portDLCIEntry.setIndexNames((0,_E,_A5),(0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:portDLCIEntry.setStatus(_A)
_PortDLCIRlpIndex_Type=Integer32
_PortDLCIRlpIndex_Object=MibTableColumn
portDLCIRlpIndex=_PortDLCIRlpIndex_Object((1,3,6,1,4,1,173,7,3,2,2,1,1),_PortDLCIRlpIndex_Type())
portDLCIRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDLCIRlpIndex.setStatus(_A)
_PortDLCIPortIndex_Type=Integer32
_PortDLCIPortIndex_Object=MibTableColumn
portDLCIPortIndex=_PortDLCIPortIndex_Object((1,3,6,1,4,1,173,7,3,2,2,1,2),_PortDLCIPortIndex_Type())
portDLCIPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDLCIPortIndex.setStatus(_A)
_PortDLCIIndex_Type=Integer32
_PortDLCIIndex_Object=MibTableColumn
portDLCIIndex=_PortDLCIIndex_Object((1,3,6,1,4,1,173,7,3,2,2,1,3),_PortDLCIIndex_Type())
portDLCIIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDLCIIndex.setStatus(_A)
class _PortDLCIIncomingCIR_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_PortDLCIIncomingCIR_Type.__name__=_B
_PortDLCIIncomingCIR_Object=MibTableColumn
portDLCIIncomingCIR=_PortDLCIIncomingCIR_Object((1,3,6,1,4,1,173,7,3,2,2,1,4),_PortDLCIIncomingCIR_Type())
portDLCIIncomingCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIIncomingCIR.setStatus(_A)
class _PortDLCIOutgoingCIR_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_PortDLCIOutgoingCIR_Type.__name__=_B
_PortDLCIOutgoingCIR_Object=MibTableColumn
portDLCIOutgoingCIR=_PortDLCIOutgoingCIR_Object((1,3,6,1,4,1,173,7,3,2,2,1,5),_PortDLCIOutgoingCIR_Type())
portDLCIOutgoingCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIOutgoingCIR.setStatus(_A)
class _PortDLCIIncomingBc_Type(Integer32):defaultValue=0
_PortDLCIIncomingBc_Type.__name__=_B
_PortDLCIIncomingBc_Object=MibTableColumn
portDLCIIncomingBc=_PortDLCIIncomingBc_Object((1,3,6,1,4,1,173,7,3,2,2,1,6),_PortDLCIIncomingBc_Type())
portDLCIIncomingBc.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIIncomingBc.setStatus(_A)
class _PortDLCIOutgoingBc_Type(Integer32):defaultValue=0
_PortDLCIOutgoingBc_Type.__name__=_B
_PortDLCIOutgoingBc_Object=MibTableColumn
portDLCIOutgoingBc=_PortDLCIOutgoingBc_Object((1,3,6,1,4,1,173,7,3,2,2,1,7),_PortDLCIOutgoingBc_Type())
portDLCIOutgoingBc.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIOutgoingBc.setStatus(_A)
class _PortDLCIIncomingBe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PortDLCIIncomingBe_Type.__name__=_B
_PortDLCIIncomingBe_Object=MibTableColumn
portDLCIIncomingBe=_PortDLCIIncomingBe_Object((1,3,6,1,4,1,173,7,3,2,2,1,8),_PortDLCIIncomingBe_Type())
portDLCIIncomingBe.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIIncomingBe.setStatus(_A)
class _PortDLCIOutgoingBe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_PortDLCIOutgoingBe_Type.__name__=_B
_PortDLCIOutgoingBe_Object=MibTableColumn
portDLCIOutgoingBe=_PortDLCIOutgoingBe_Object((1,3,6,1,4,1,173,7,3,2,2,1,9),_PortDLCIOutgoingBe_Type())
portDLCIOutgoingBe.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIOutgoingBe.setStatus(_A)
class _PortDLCIBecnRecoveryCnt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortDLCIBecnRecoveryCnt_Type.__name__=_B
_PortDLCIBecnRecoveryCnt_Object=MibTableColumn
portDLCIBecnRecoveryCnt=_PortDLCIBecnRecoveryCnt_Object((1,3,6,1,4,1,173,7,3,2,2,1,10),_PortDLCIBecnRecoveryCnt_Type())
portDLCIBecnRecoveryCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIBecnRecoveryCnt.setStatus(_A)
class _PortDLCIPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_PortDLCIPriority_Type.__name__=_B
_PortDLCIPriority_Object=MibTableColumn
portDLCIPriority=_PortDLCIPriority_Object((1,3,6,1,4,1,173,7,3,2,2,1,11),_PortDLCIPriority_Type())
portDLCIPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIPriority.setStatus(_A)
_PortDLCIRowStatus_Type=RowStatus
_PortDLCIRowStatus_Object=MibTableColumn
portDLCIRowStatus=_PortDLCIRowStatus_Object((1,3,6,1,4,1,173,7,3,2,2,1,12),_PortDLCIRowStatus_Type())
portDLCIRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIRowStatus.setStatus(_A)
class _PortDLCIBackupGroup_Type(Integer32):defaultValue=0
_PortDLCIBackupGroup_Type.__name__=_B
_PortDLCIBackupGroup_Object=MibTableColumn
portDLCIBackupGroup=_PortDLCIBackupGroup_Object((1,3,6,1,4,1,173,7,3,2,2,1,13),_PortDLCIBackupGroup_Type())
portDLCIBackupGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIBackupGroup.setStatus(_A)
class _PortDLCIBackupProtEnb_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortDLCIBackupProtEnb_Type.__name__=_B
_PortDLCIBackupProtEnb_Object=MibTableColumn
portDLCIBackupProtEnb=_PortDLCIBackupProtEnb_Object((1,3,6,1,4,1,173,7,3,2,2,1,14),_PortDLCIBackupProtEnb_Type())
portDLCIBackupProtEnb.setMaxAccess(_D)
if mibBuilder.loadTexts:portDLCIBackupProtEnb.setStatus(_A)
_PortFrBackupGroupTable_Object=MibTable
portFrBackupGroupTable=_PortFrBackupGroupTable_Object((1,3,6,1,4,1,173,7,3,2,3))
if mibBuilder.loadTexts:portFrBackupGroupTable.setStatus(_A)
_PortFrBackupEntry_Object=MibTableRow
portFrBackupEntry=_PortFrBackupEntry_Object((1,3,6,1,4,1,173,7,3,2,3,1))
portFrBackupEntry.setIndexNames((0,_E,_A8),(0,_E,_A9),(0,_E,_AA),(0,_E,_AB))
if mibBuilder.loadTexts:portFrBackupEntry.setStatus(_A)
class _PortFrBackupRLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PortFrBackupRLP_Type.__name__=_B
_PortFrBackupRLP_Object=MibTableColumn
portFrBackupRLP=_PortFrBackupRLP_Object((1,3,6,1,4,1,173,7,3,2,3,1,1),_PortFrBackupRLP_Type())
portFrBackupRLP.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrBackupRLP.setStatus(_A)
class _PortFrBackupPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PortFrBackupPort_Type.__name__=_B
_PortFrBackupPort_Object=MibTableColumn
portFrBackupPort=_PortFrBackupPort_Object((1,3,6,1,4,1,173,7,3,2,3,1,2),_PortFrBackupPort_Type())
portFrBackupPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrBackupPort.setStatus(_A)
class _PortFrBackupDLCI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_PortFrBackupDLCI_Type.__name__=_B
_PortFrBackupDLCI_Object=MibTableColumn
portFrBackupDLCI=_PortFrBackupDLCI_Object((1,3,6,1,4,1,173,7,3,2,3,1,3),_PortFrBackupDLCI_Type())
portFrBackupDLCI.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrBackupDLCI.setStatus(_A)
class _PortFrBackupGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortFrBackupGroup_Type.__name__=_B
_PortFrBackupGroup_Object=MibTableColumn
portFrBackupGroup=_PortFrBackupGroup_Object((1,3,6,1,4,1,173,7,3,2,3,1,4),_PortFrBackupGroup_Type())
portFrBackupGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:portFrBackupGroup.setStatus(_A)
class _PortFrBackupWaitTimer_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortFrBackupWaitTimer_Type.__name__=_B
_PortFrBackupWaitTimer_Object=MibTableColumn
portFrBackupWaitTimer=_PortFrBackupWaitTimer_Object((1,3,6,1,4,1,173,7,3,2,3,1,5),_PortFrBackupWaitTimer_Type())
portFrBackupWaitTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrBackupWaitTimer.setStatus(_A)
class _PortFrBackupProtEnab_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortFrBackupProtEnab_Type.__name__=_B
_PortFrBackupProtEnab_Object=MibTableColumn
portFrBackupProtEnab=_PortFrBackupProtEnab_Object((1,3,6,1,4,1,173,7,3,2,3,1,6),_PortFrBackupProtEnab_Type())
portFrBackupProtEnab.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrBackupProtEnab.setStatus(_A)
_PortFrBackupRowStatus_Type=RowStatus
_PortFrBackupRowStatus_Object=MibTableColumn
portFrBackupRowStatus=_PortFrBackupRowStatus_Object((1,3,6,1,4,1,173,7,3,2,3,1,7),_PortFrBackupRowStatus_Type())
portFrBackupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portFrBackupRowStatus.setStatus(_A)
_PortBsciGroup_ObjectIdentity=ObjectIdentity
portBsciGroup=_PortBsciGroup_ObjectIdentity((1,3,6,1,4,1,173,7,3,4))
_PortBsciAdminTable_Object=MibTable
portBsciAdminTable=_PortBsciAdminTable_Object((1,3,6,1,4,1,173,7,3,4,1))
if mibBuilder.loadTexts:portBsciAdminTable.setStatus(_A)
_PortBsciAdminEntry_Object=MibTableRow
portBsciAdminEntry=_PortBsciAdminEntry_Object((1,3,6,1,4,1,173,7,3,4,1,1))
portBsciAdminEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portBsciAdminEntry.setStatus(_A)
class _PortBsciAdminBlockedFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortBsciAdminBlockedFlag_Type.__name__=_B
_PortBsciAdminBlockedFlag_Object=MibTableColumn
portBsciAdminBlockedFlag=_PortBsciAdminBlockedFlag_Object((1,3,6,1,4,1,173,7,3,4,1,1,1),_PortBsciAdminBlockedFlag_Type())
portBsciAdminBlockedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminBlockedFlag.setStatus(_A)
class _PortBsciAdminConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10)))
_PortBsciAdminConnector_Type.__name__=_B
_PortBsciAdminConnector_Object=MibTableColumn
portBsciAdminConnector=_PortBsciAdminConnector_Object((1,3,6,1,4,1,173,7,3,4,1,1,2),_PortBsciAdminConnector_Type())
portBsciAdminConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminConnector.setStatus(_A)
class _PortBsciAdminSpeed_Type(Integer32):defaultValue=9600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,19200))
_PortBsciAdminSpeed_Type.__name__=_B
_PortBsciAdminSpeed_Object=MibTableColumn
portBsciAdminSpeed=_PortBsciAdminSpeed_Object((1,3,6,1,4,1,173,7,3,4,1,1,3),_PortBsciAdminSpeed_Type())
portBsciAdminSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminSpeed.setStatus(_A)
class _PortBsciAdminRetransmitInterval_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_PortBsciAdminRetransmitInterval_Type.__name__=_B
_PortBsciAdminRetransmitInterval_Object=MibTableColumn
portBsciAdminRetransmitInterval=_PortBsciAdminRetransmitInterval_Object((1,3,6,1,4,1,173,7,3,4,1,1,4),_PortBsciAdminRetransmitInterval_Type())
portBsciAdminRetransmitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminRetransmitInterval.setStatus(_A)
class _PortBsciAdminMAXRetransmits_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PortBsciAdminMAXRetransmits_Type.__name__=_B
_PortBsciAdminMAXRetransmits_Object=MibTableColumn
portBsciAdminMAXRetransmits=_PortBsciAdminMAXRetransmits_Object((1,3,6,1,4,1,173,7,3,4,1,1,5),_PortBsciAdminMAXRetransmits_Type())
portBsciAdminMAXRetransmits.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminMAXRetransmits.setStatus(_A)
class _PortBsciAdminMaxBytesPerFrame_Type(Integer32):defaultValue=4105;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,4105))
_PortBsciAdminMaxBytesPerFrame_Type.__name__=_B
_PortBsciAdminMaxBytesPerFrame_Object=MibTableColumn
portBsciAdminMaxBytesPerFrame=_PortBsciAdminMaxBytesPerFrame_Object((1,3,6,1,4,1,173,7,3,4,1,1,6),_PortBsciAdminMaxBytesPerFrame_Type())
portBsciAdminMaxBytesPerFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminMaxBytesPerFrame.setStatus(_A)
class _PortBsciAdminGenerateClock_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminGenerateClock_Type.__name__=_B
_PortBsciAdminGenerateClock_Object=MibTableColumn
portBsciAdminGenerateClock=_PortBsciAdminGenerateClock_Object((1,3,6,1,4,1,173,7,3,4,1,1,7),_PortBsciAdminGenerateClock_Type())
portBsciAdminGenerateClock.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminGenerateClock.setStatus(_A)
class _PortBsciAdminRcvClockFromDTE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminRcvClockFromDTE_Type.__name__=_B
_PortBsciAdminRcvClockFromDTE_Object=MibTableColumn
portBsciAdminRcvClockFromDTE=_PortBsciAdminRcvClockFromDTE_Object((1,3,6,1,4,1,173,7,3,4,1,1,8),_PortBsciAdminRcvClockFromDTE_Type())
portBsciAdminRcvClockFromDTE.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminRcvClockFromDTE.setStatus(_A)
class _PortBsciAdminPadType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_PortBsciAdminPadType_Type.__name__=_B
_PortBsciAdminPadType_Object=MibTableColumn
portBsciAdminPadType=_PortBsciAdminPadType_Object((1,3,6,1,4,1,173,7,3,4,1,1,9),_PortBsciAdminPadType_Type())
portBsciAdminPadType.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminPadType.setStatus(_A)
class _PortBsciAdminUseEBCDIC_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminUseEBCDIC_Type.__name__=_B
_PortBsciAdminUseEBCDIC_Object=MibTableColumn
portBsciAdminUseEBCDIC=_PortBsciAdminUseEBCDIC_Object((1,3,6,1,4,1,173,7,3,4,1,1,10),_PortBsciAdminUseEBCDIC_Type())
portBsciAdminUseEBCDIC.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminUseEBCDIC.setStatus(_A)
class _PortBsciAdminCallInfoInRequestPacket_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminCallInfoInRequestPacket_Type.__name__=_B
_PortBsciAdminCallInfoInRequestPacket_Object=MibTableColumn
portBsciAdminCallInfoInRequestPacket=_PortBsciAdminCallInfoInRequestPacket_Object((1,3,6,1,4,1,173,7,3,4,1,1,11),_PortBsciAdminCallInfoInRequestPacket_Type())
portBsciAdminCallInfoInRequestPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminCallInfoInRequestPacket.setStatus(_A)
class _PortBsciAdminClearVCOnLastDeviceDown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminClearVCOnLastDeviceDown_Type.__name__=_B
_PortBsciAdminClearVCOnLastDeviceDown_Object=MibTableColumn
portBsciAdminClearVCOnLastDeviceDown=_PortBsciAdminClearVCOnLastDeviceDown_Object((1,3,6,1,4,1,173,7,3,4,1,1,12),_PortBsciAdminClearVCOnLastDeviceDown_Type())
portBsciAdminClearVCOnLastDeviceDown.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminClearVCOnLastDeviceDown.setStatus(_A)
class _PortBsciAdminTransTextSupported_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminTransTextSupported_Type.__name__=_B
_PortBsciAdminTransTextSupported_Object=MibTableColumn
portBsciAdminTransTextSupported=_PortBsciAdminTransTextSupported_Object((1,3,6,1,4,1,173,7,3,4,1,1,13),_PortBsciAdminTransTextSupported_Type())
portBsciAdminTransTextSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminTransTextSupported.setStatus(_A)
class _PortBsciAdminEndToEndAck_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminEndToEndAck_Type.__name__=_B
_PortBsciAdminEndToEndAck_Object=MibTableColumn
portBsciAdminEndToEndAck=_PortBsciAdminEndToEndAck_Object((1,3,6,1,4,1,173,7,3,4,1,1,14),_PortBsciAdminEndToEndAck_Type())
portBsciAdminEndToEndAck.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminEndToEndAck.setStatus(_A)
class _PortBsciAdminFullDuplex_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminFullDuplex_Type.__name__=_B
_PortBsciAdminFullDuplex_Object=MibTableColumn
portBsciAdminFullDuplex=_PortBsciAdminFullDuplex_Object((1,3,6,1,4,1,173,7,3,4,1,1,15),_PortBsciAdminFullDuplex_Type())
portBsciAdminFullDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminFullDuplex.setStatus(_A)
class _PortBsciAdminMultidrop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminMultidrop_Type.__name__=_B
_PortBsciAdminMultidrop_Object=MibTableColumn
portBsciAdminMultidrop=_PortBsciAdminMultidrop_Object((1,3,6,1,4,1,173,7,3,4,1,1,16),_PortBsciAdminMultidrop_Type())
portBsciAdminMultidrop.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminMultidrop.setStatus(_A)
class _PortBsciAdminSlowPollRetryCount_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,150))
_PortBsciAdminSlowPollRetryCount_Type.__name__=_B
_PortBsciAdminSlowPollRetryCount_Object=MibTableColumn
portBsciAdminSlowPollRetryCount=_PortBsciAdminSlowPollRetryCount_Object((1,3,6,1,4,1,173,7,3,4,1,1,17),_PortBsciAdminSlowPollRetryCount_Type())
portBsciAdminSlowPollRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminSlowPollRetryCount.setStatus(_A)
class _PortBsciAdminSlowPollRetryFreq_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_PortBsciAdminSlowPollRetryFreq_Type.__name__=_B
_PortBsciAdminSlowPollRetryFreq_Object=MibTableColumn
portBsciAdminSlowPollRetryFreq=_PortBsciAdminSlowPollRetryFreq_Object((1,3,6,1,4,1,173,7,3,4,1,1,18),_PortBsciAdminSlowPollRetryFreq_Type())
portBsciAdminSlowPollRetryFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminSlowPollRetryFreq.setStatus(_A)
class _PortBsciAdminStartSynchChars_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PortBsciAdminStartSynchChars_Type.__name__=_B
_PortBsciAdminStartSynchChars_Object=MibTableColumn
portBsciAdminStartSynchChars=_PortBsciAdminStartSynchChars_Object((1,3,6,1,4,1,173,7,3,4,1,1,19),_PortBsciAdminStartSynchChars_Type())
portBsciAdminStartSynchChars.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminStartSynchChars.setStatus(_A)
class _PortBsciAdminEndPadChars_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_PortBsciAdminEndPadChars_Type.__name__=_B
_PortBsciAdminEndPadChars_Object=MibTableColumn
portBsciAdminEndPadChars=_PortBsciAdminEndPadChars_Object((1,3,6,1,4,1,173,7,3,4,1,1,20),_PortBsciAdminEndPadChars_Type())
portBsciAdminEndPadChars.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminEndPadChars.setStatus(_A)
class _PortBsciAdminPollInterval_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_PortBsciAdminPollInterval_Type.__name__=_B
_PortBsciAdminPollInterval_Object=MibTableColumn
portBsciAdminPollInterval=_PortBsciAdminPollInterval_Object((1,3,6,1,4,1,173,7,3,4,1,1,21),_PortBsciAdminPollInterval_Type())
portBsciAdminPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminPollInterval.setStatus(_A)
class _PortBsciAdminNoResponseTimer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PortBsciAdminNoResponseTimer_Type.__name__=_B
_PortBsciAdminNoResponseTimer_Object=MibTableColumn
portBsciAdminNoResponseTimer=_PortBsciAdminNoResponseTimer_Object((1,3,6,1,4,1,173,7,3,4,1,1,22),_PortBsciAdminNoResponseTimer_Type())
portBsciAdminNoResponseTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminNoResponseTimer.setStatus(_A)
class _PortBsciAdminNoResponseRetryCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortBsciAdminNoResponseRetryCount_Type.__name__=_B
_PortBsciAdminNoResponseRetryCount_Object=MibTableColumn
portBsciAdminNoResponseRetryCount=_PortBsciAdminNoResponseRetryCount_Object((1,3,6,1,4,1,173,7,3,4,1,1,23),_PortBsciAdminNoResponseRetryCount_Type())
portBsciAdminNoResponseRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminNoResponseRetryCount.setStatus(_A)
class _PortBsciAdminErrorRetransmitCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortBsciAdminErrorRetransmitCount_Type.__name__=_B
_PortBsciAdminErrorRetransmitCount_Object=MibTableColumn
portBsciAdminErrorRetransmitCount=_PortBsciAdminErrorRetransmitCount_Object((1,3,6,1,4,1,173,7,3,4,1,1,24),_PortBsciAdminErrorRetransmitCount_Type())
portBsciAdminErrorRetransmitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminErrorRetransmitCount.setStatus(_A)
class _PortBsciAdminNAKRetryCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortBsciAdminNAKRetryCount_Type.__name__=_B
_PortBsciAdminNAKRetryCount_Object=MibTableColumn
portBsciAdminNAKRetryCount=_PortBsciAdminNAKRetryCount_Object((1,3,6,1,4,1,173,7,3,4,1,1,25),_PortBsciAdminNAKRetryCount_Type())
portBsciAdminNAKRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminNAKRetryCount.setStatus(_A)
class _PortBsciAdminBlockCheck_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('crc16',1),('even-lrc',2),('odd-lrc',3)))
_PortBsciAdminBlockCheck_Type.__name__=_B
_PortBsciAdminBlockCheck_Object=MibTableColumn
portBsciAdminBlockCheck=_PortBsciAdminBlockCheck_Object((1,3,6,1,4,1,173,7,3,4,1,1,26),_PortBsciAdminBlockCheck_Type())
portBsciAdminBlockCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminBlockCheck.setStatus(_A)
class _PortBsciAdminDataMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('odd-7bit',1),(_AC,2),(_AD,3)))
_PortBsciAdminDataMode_Type.__name__=_B
_PortBsciAdminDataMode_Object=MibTableColumn
portBsciAdminDataMode=_PortBsciAdminDataMode_Object((1,3,6,1,4,1,173,7,3,4,1,1,27),_PortBsciAdminDataMode_Type())
portBsciAdminDataMode.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminDataMode.setStatus(_A)
_PortBsciAdminRowStatus_Type=RowStatus
_PortBsciAdminRowStatus_Object=MibTableColumn
portBsciAdminRowStatus=_PortBsciAdminRowStatus_Object((1,3,6,1,4,1,173,7,3,4,1,1,28),_PortBsciAdminRowStatus_Type())
portBsciAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminRowStatus.setStatus(_A)
class _PortBsciAdminAnswerNonConfigured_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminAnswerNonConfigured_Type.__name__=_B
_PortBsciAdminAnswerNonConfigured_Object=MibTableColumn
portBsciAdminAnswerNonConfigured=_PortBsciAdminAnswerNonConfigured_Object((1,3,6,1,4,1,173,7,3,4,1,1,29),_PortBsciAdminAnswerNonConfigured_Type())
portBsciAdminAnswerNonConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminAnswerNonConfigured.setStatus(_A)
class _PortBsciAdminActivateConnectionWithoutPoll_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciAdminActivateConnectionWithoutPoll_Type.__name__=_B
_PortBsciAdminActivateConnectionWithoutPoll_Object=MibTableColumn
portBsciAdminActivateConnectionWithoutPoll=_PortBsciAdminActivateConnectionWithoutPoll_Object((1,3,6,1,4,1,173,7,3,4,1,1,30),_PortBsciAdminActivateConnectionWithoutPoll_Type())
portBsciAdminActivateConnectionWithoutPoll.setMaxAccess(_D)
if mibBuilder.loadTexts:portBsciAdminActivateConnectionWithoutPoll.setStatus(_A)
_PortBsciOperTable_Object=MibTable
portBsciOperTable=_PortBsciOperTable_Object((1,3,6,1,4,1,173,7,3,4,2))
if mibBuilder.loadTexts:portBsciOperTable.setStatus(_A)
_PortBsciOperEntry_Object=MibTableRow
portBsciOperEntry=_PortBsciOperEntry_Object((1,3,6,1,4,1,173,7,3,4,2,1))
portBsciOperEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portBsciOperEntry.setStatus(_A)
class _PortBsciOperBlockedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortBsciOperBlockedFlag_Type.__name__=_B
_PortBsciOperBlockedFlag_Object=MibTableColumn
portBsciOperBlockedFlag=_PortBsciOperBlockedFlag_Object((1,3,6,1,4,1,173,7,3,4,2,1,1),_PortBsciOperBlockedFlag_Type())
portBsciOperBlockedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperBlockedFlag.setStatus(_A)
class _PortBsciOperConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10)))
_PortBsciOperConnector_Type.__name__=_B
_PortBsciOperConnector_Object=MibTableColumn
portBsciOperConnector=_PortBsciOperConnector_Object((1,3,6,1,4,1,173,7,3,4,2,1,2),_PortBsciOperConnector_Type())
portBsciOperConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperConnector.setStatus(_A)
_PortBsciOperSpeed_Type=Integer32
_PortBsciOperSpeed_Object=MibTableColumn
portBsciOperSpeed=_PortBsciOperSpeed_Object((1,3,6,1,4,1,173,7,3,4,2,1,3),_PortBsciOperSpeed_Type())
portBsciOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperSpeed.setStatus(_A)
class _PortBsciOperRetransmitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_PortBsciOperRetransmitInterval_Type.__name__=_B
_PortBsciOperRetransmitInterval_Object=MibTableColumn
portBsciOperRetransmitInterval=_PortBsciOperRetransmitInterval_Object((1,3,6,1,4,1,173,7,3,4,2,1,4),_PortBsciOperRetransmitInterval_Type())
portBsciOperRetransmitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperRetransmitInterval.setStatus(_A)
class _PortBsciOperMAXRetransmits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PortBsciOperMAXRetransmits_Type.__name__=_B
_PortBsciOperMAXRetransmits_Object=MibTableColumn
portBsciOperMAXRetransmits=_PortBsciOperMAXRetransmits_Object((1,3,6,1,4,1,173,7,3,4,2,1,5),_PortBsciOperMAXRetransmits_Type())
portBsciOperMAXRetransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperMAXRetransmits.setStatus(_A)
class _PortBsciOperMaxBytesPerFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,4105))
_PortBsciOperMaxBytesPerFrame_Type.__name__=_B
_PortBsciOperMaxBytesPerFrame_Object=MibTableColumn
portBsciOperMaxBytesPerFrame=_PortBsciOperMaxBytesPerFrame_Object((1,3,6,1,4,1,173,7,3,4,2,1,6),_PortBsciOperMaxBytesPerFrame_Type())
portBsciOperMaxBytesPerFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperMaxBytesPerFrame.setStatus(_A)
class _PortBsciOperGenerateClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperGenerateClock_Type.__name__=_B
_PortBsciOperGenerateClock_Object=MibTableColumn
portBsciOperGenerateClock=_PortBsciOperGenerateClock_Object((1,3,6,1,4,1,173,7,3,4,2,1,7),_PortBsciOperGenerateClock_Type())
portBsciOperGenerateClock.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperGenerateClock.setStatus(_A)
class _PortBsciOperRcvClockFromDTE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperRcvClockFromDTE_Type.__name__=_B
_PortBsciOperRcvClockFromDTE_Object=MibTableColumn
portBsciOperRcvClockFromDTE=_PortBsciOperRcvClockFromDTE_Object((1,3,6,1,4,1,173,7,3,4,2,1,8),_PortBsciOperRcvClockFromDTE_Type())
portBsciOperRcvClockFromDTE.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperRcvClockFromDTE.setStatus(_A)
class _PortBsciOperPadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_PortBsciOperPadType_Type.__name__=_B
_PortBsciOperPadType_Object=MibTableColumn
portBsciOperPadType=_PortBsciOperPadType_Object((1,3,6,1,4,1,173,7,3,4,2,1,9),_PortBsciOperPadType_Type())
portBsciOperPadType.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperPadType.setStatus(_A)
class _PortBsciOperUseEBCDIC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperUseEBCDIC_Type.__name__=_B
_PortBsciOperUseEBCDIC_Object=MibTableColumn
portBsciOperUseEBCDIC=_PortBsciOperUseEBCDIC_Object((1,3,6,1,4,1,173,7,3,4,2,1,10),_PortBsciOperUseEBCDIC_Type())
portBsciOperUseEBCDIC.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperUseEBCDIC.setStatus(_A)
class _PortBsciOperCallInfoInRequestPacket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperCallInfoInRequestPacket_Type.__name__=_B
_PortBsciOperCallInfoInRequestPacket_Object=MibTableColumn
portBsciOperCallInfoInRequestPacket=_PortBsciOperCallInfoInRequestPacket_Object((1,3,6,1,4,1,173,7,3,4,2,1,11),_PortBsciOperCallInfoInRequestPacket_Type())
portBsciOperCallInfoInRequestPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperCallInfoInRequestPacket.setStatus(_A)
class _PortBsciOperClearVCOnLastDeviceDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperClearVCOnLastDeviceDown_Type.__name__=_B
_PortBsciOperClearVCOnLastDeviceDown_Object=MibTableColumn
portBsciOperClearVCOnLastDeviceDown=_PortBsciOperClearVCOnLastDeviceDown_Object((1,3,6,1,4,1,173,7,3,4,2,1,12),_PortBsciOperClearVCOnLastDeviceDown_Type())
portBsciOperClearVCOnLastDeviceDown.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperClearVCOnLastDeviceDown.setStatus(_A)
class _PortBsciOperTransTextSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperTransTextSupported_Type.__name__=_B
_PortBsciOperTransTextSupported_Object=MibTableColumn
portBsciOperTransTextSupported=_PortBsciOperTransTextSupported_Object((1,3,6,1,4,1,173,7,3,4,2,1,13),_PortBsciOperTransTextSupported_Type())
portBsciOperTransTextSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperTransTextSupported.setStatus(_A)
class _PortBsciOperEndToEndAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperEndToEndAck_Type.__name__=_B
_PortBsciOperEndToEndAck_Object=MibTableColumn
portBsciOperEndToEndAck=_PortBsciOperEndToEndAck_Object((1,3,6,1,4,1,173,7,3,4,2,1,14),_PortBsciOperEndToEndAck_Type())
portBsciOperEndToEndAck.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperEndToEndAck.setStatus(_A)
class _PortBsciOperFullDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperFullDuplex_Type.__name__=_B
_PortBsciOperFullDuplex_Object=MibTableColumn
portBsciOperFullDuplex=_PortBsciOperFullDuplex_Object((1,3,6,1,4,1,173,7,3,4,2,1,15),_PortBsciOperFullDuplex_Type())
portBsciOperFullDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperFullDuplex.setStatus(_A)
class _PortBsciOperMultidrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperMultidrop_Type.__name__=_B
_PortBsciOperMultidrop_Object=MibTableColumn
portBsciOperMultidrop=_PortBsciOperMultidrop_Object((1,3,6,1,4,1,173,7,3,4,2,1,16),_PortBsciOperMultidrop_Type())
portBsciOperMultidrop.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperMultidrop.setStatus(_A)
class _PortBsciOperSlowPollRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,150))
_PortBsciOperSlowPollRetryCount_Type.__name__=_B
_PortBsciOperSlowPollRetryCount_Object=MibTableColumn
portBsciOperSlowPollRetryCount=_PortBsciOperSlowPollRetryCount_Object((1,3,6,1,4,1,173,7,3,4,2,1,17),_PortBsciOperSlowPollRetryCount_Type())
portBsciOperSlowPollRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperSlowPollRetryCount.setStatus(_A)
class _PortBsciOperSlowPollRetryFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_PortBsciOperSlowPollRetryFreq_Type.__name__=_B
_PortBsciOperSlowPollRetryFreq_Object=MibTableColumn
portBsciOperSlowPollRetryFreq=_PortBsciOperSlowPollRetryFreq_Object((1,3,6,1,4,1,173,7,3,4,2,1,18),_PortBsciOperSlowPollRetryFreq_Type())
portBsciOperSlowPollRetryFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperSlowPollRetryFreq.setStatus(_A)
class _PortBsciOperStartSynchChars_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PortBsciOperStartSynchChars_Type.__name__=_B
_PortBsciOperStartSynchChars_Object=MibTableColumn
portBsciOperStartSynchChars=_PortBsciOperStartSynchChars_Object((1,3,6,1,4,1,173,7,3,4,2,1,19),_PortBsciOperStartSynchChars_Type())
portBsciOperStartSynchChars.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperStartSynchChars.setStatus(_A)
class _PortBsciOperEndPadChars_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_PortBsciOperEndPadChars_Type.__name__=_B
_PortBsciOperEndPadChars_Object=MibTableColumn
portBsciOperEndPadChars=_PortBsciOperEndPadChars_Object((1,3,6,1,4,1,173,7,3,4,2,1,20),_PortBsciOperEndPadChars_Type())
portBsciOperEndPadChars.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperEndPadChars.setStatus(_A)
class _PortBsciOperPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_PortBsciOperPollInterval_Type.__name__=_B
_PortBsciOperPollInterval_Object=MibTableColumn
portBsciOperPollInterval=_PortBsciOperPollInterval_Object((1,3,6,1,4,1,173,7,3,4,2,1,21),_PortBsciOperPollInterval_Type())
portBsciOperPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperPollInterval.setStatus(_A)
class _PortBsciOperNoResponseTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_PortBsciOperNoResponseTimer_Type.__name__=_B
_PortBsciOperNoResponseTimer_Object=MibTableColumn
portBsciOperNoResponseTimer=_PortBsciOperNoResponseTimer_Object((1,3,6,1,4,1,173,7,3,4,2,1,22),_PortBsciOperNoResponseTimer_Type())
portBsciOperNoResponseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperNoResponseTimer.setStatus(_A)
class _PortBsciOperNoResponseRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortBsciOperNoResponseRetryCount_Type.__name__=_B
_PortBsciOperNoResponseRetryCount_Object=MibTableColumn
portBsciOperNoResponseRetryCount=_PortBsciOperNoResponseRetryCount_Object((1,3,6,1,4,1,173,7,3,4,2,1,23),_PortBsciOperNoResponseRetryCount_Type())
portBsciOperNoResponseRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperNoResponseRetryCount.setStatus(_A)
class _PortBsciOperErrorRetransmitCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortBsciOperErrorRetransmitCount_Type.__name__=_B
_PortBsciOperErrorRetransmitCount_Object=MibTableColumn
portBsciOperErrorRetransmitCount=_PortBsciOperErrorRetransmitCount_Object((1,3,6,1,4,1,173,7,3,4,2,1,24),_PortBsciOperErrorRetransmitCount_Type())
portBsciOperErrorRetransmitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperErrorRetransmitCount.setStatus(_A)
class _PortBsciOperNAKRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PortBsciOperNAKRetryCount_Type.__name__=_B
_PortBsciOperNAKRetryCount_Object=MibTableColumn
portBsciOperNAKRetryCount=_PortBsciOperNAKRetryCount_Object((1,3,6,1,4,1,173,7,3,4,2,1,25),_PortBsciOperNAKRetryCount_Type())
portBsciOperNAKRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperNAKRetryCount.setStatus(_A)
class _PortBsciOperBlockCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('crc16',1),('even-lrc',2),('odd-lrc',3)))
_PortBsciOperBlockCheck_Type.__name__=_B
_PortBsciOperBlockCheck_Object=MibTableColumn
portBsciOperBlockCheck=_PortBsciOperBlockCheck_Object((1,3,6,1,4,1,173,7,3,4,2,1,26),_PortBsciOperBlockCheck_Type())
portBsciOperBlockCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperBlockCheck.setStatus(_A)
class _PortBsciOperDataMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('odd-7bit',1),(_AC,2),(_AD,3)))
_PortBsciOperDataMode_Type.__name__=_B
_PortBsciOperDataMode_Object=MibTableColumn
portBsciOperDataMode=_PortBsciOperDataMode_Object((1,3,6,1,4,1,173,7,3,4,2,1,27),_PortBsciOperDataMode_Type())
portBsciOperDataMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperDataMode.setStatus(_A)
class _PortBsciOperAnswerNonConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperAnswerNonConfigured_Type.__name__=_B
_PortBsciOperAnswerNonConfigured_Object=MibTableColumn
portBsciOperAnswerNonConfigured=_PortBsciOperAnswerNonConfigured_Object((1,3,6,1,4,1,173,7,3,4,2,1,28),_PortBsciOperAnswerNonConfigured_Type())
portBsciOperAnswerNonConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperAnswerNonConfigured.setStatus(_A)
class _PortBsciOperActivateConnectionWithoutPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortBsciOperActivateConnectionWithoutPoll_Type.__name__=_B
_PortBsciOperActivateConnectionWithoutPoll_Object=MibTableColumn
portBsciOperActivateConnectionWithoutPoll=_PortBsciOperActivateConnectionWithoutPoll_Object((1,3,6,1,4,1,173,7,3,4,2,1,29),_PortBsciOperActivateConnectionWithoutPoll_Type())
portBsciOperActivateConnectionWithoutPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:portBsciOperActivateConnectionWithoutPoll.setStatus(_A)
_BsciSubscrAdminTable_Object=MibTable
bsciSubscrAdminTable=_BsciSubscrAdminTable_Object((1,3,6,1,4,1,173,7,3,4,3))
if mibBuilder.loadTexts:bsciSubscrAdminTable.setStatus(_A)
_BsciSubscrAdminEntry_Object=MibTableRow
bsciSubscrAdminEntry=_BsciSubscrAdminEntry_Object((1,3,6,1,4,1,173,7,3,4,3,1))
bsciSubscrAdminEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_AE))
if mibBuilder.loadTexts:bsciSubscrAdminEntry.setStatus(_A)
class _BsciSubscrAdminSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BsciSubscrAdminSequence_Type.__name__=_B
_BsciSubscrAdminSequence_Object=MibTableColumn
bsciSubscrAdminSequence=_BsciSubscrAdminSequence_Object((1,3,6,1,4,1,173,7,3,4,3,1,1),_BsciSubscrAdminSequence_Type())
bsciSubscrAdminSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrAdminSequence.setStatus(_A)
_BsciSubscrAdminLocalID_Type=NlSubscriberAddress
_BsciSubscrAdminLocalID_Object=MibTableColumn
bsciSubscrAdminLocalID=_BsciSubscrAdminLocalID_Object((1,3,6,1,4,1,173,7,3,4,3,1,2),_BsciSubscrAdminLocalID_Type())
bsciSubscrAdminLocalID.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminLocalID.setStatus(_A)
_BsciSubscrAdminRemoteID_Type=NlSubscriberAddress
_BsciSubscrAdminRemoteID_Object=MibTableColumn
bsciSubscrAdminRemoteID=_BsciSubscrAdminRemoteID_Object((1,3,6,1,4,1,173,7,3,4,3,1,3),_BsciSubscrAdminRemoteID_Type())
bsciSubscrAdminRemoteID.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminRemoteID.setStatus(_A)
class _BsciSubscrAdminAutocall_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciSubscrAdminAutocall_Type.__name__=_B
_BsciSubscrAdminAutocall_Object=MibTableColumn
bsciSubscrAdminAutocall=_BsciSubscrAdminAutocall_Object((1,3,6,1,4,1,173,7,3,4,3,1,4),_BsciSubscrAdminAutocall_Type())
bsciSubscrAdminAutocall.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminAutocall.setStatus(_A)
class _BsciSubscrAdminAutocallRtyTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,255))
_BsciSubscrAdminAutocallRtyTimer_Type.__name__=_B
_BsciSubscrAdminAutocallRtyTimer_Object=MibTableColumn
bsciSubscrAdminAutocallRtyTimer=_BsciSubscrAdminAutocallRtyTimer_Object((1,3,6,1,4,1,173,7,3,4,3,1,5),_BsciSubscrAdminAutocallRtyTimer_Type())
bsciSubscrAdminAutocallRtyTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminAutocallRtyTimer.setStatus(_A)
class _BsciSubscrAdminAutocallMaxRtry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsciSubscrAdminAutocallMaxRtry_Type.__name__=_B
_BsciSubscrAdminAutocallMaxRtry_Object=MibTableColumn
bsciSubscrAdminAutocallMaxRtry=_BsciSubscrAdminAutocallMaxRtry_Object((1,3,6,1,4,1,173,7,3,4,3,1,6),_BsciSubscrAdminAutocallMaxRtry_Type())
bsciSubscrAdminAutocallMaxRtry.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminAutocallMaxRtry.setStatus(_A)
class _BsciSubscrAdminConnectionID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsciSubscrAdminConnectionID_Type.__name__=_B
_BsciSubscrAdminConnectionID_Object=MibTableColumn
bsciSubscrAdminConnectionID=_BsciSubscrAdminConnectionID_Object((1,3,6,1,4,1,173,7,3,4,3,1,7),_BsciSubscrAdminConnectionID_Type())
bsciSubscrAdminConnectionID.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminConnectionID.setStatus(_A)
_BsciSubscrAdminRowStatus_Type=RowStatus
_BsciSubscrAdminRowStatus_Object=MibTableColumn
bsciSubscrAdminRowStatus=_BsciSubscrAdminRowStatus_Object((1,3,6,1,4,1,173,7,3,4,3,1,8),_BsciSubscrAdminRowStatus_Type())
bsciSubscrAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciSubscrAdminRowStatus.setStatus(_A)
_BsciSubscrOperTable_Object=MibTable
bsciSubscrOperTable=_BsciSubscrOperTable_Object((1,3,6,1,4,1,173,7,3,4,4))
if mibBuilder.loadTexts:bsciSubscrOperTable.setStatus(_A)
_BsciSubscrOperEntry_Object=MibTableRow
bsciSubscrOperEntry=_BsciSubscrOperEntry_Object((1,3,6,1,4,1,173,7,3,4,4,1))
bsciSubscrOperEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_AF))
if mibBuilder.loadTexts:bsciSubscrOperEntry.setStatus(_A)
class _BsciSubscrOperSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_BsciSubscrOperSequence_Type.__name__=_B
_BsciSubscrOperSequence_Object=MibTableColumn
bsciSubscrOperSequence=_BsciSubscrOperSequence_Object((1,3,6,1,4,1,173,7,3,4,4,1,1),_BsciSubscrOperSequence_Type())
bsciSubscrOperSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperSequence.setStatus(_A)
_BsciSubscrOperLocalID_Type=NlSubscriberAddress
_BsciSubscrOperLocalID_Object=MibTableColumn
bsciSubscrOperLocalID=_BsciSubscrOperLocalID_Object((1,3,6,1,4,1,173,7,3,4,4,1,2),_BsciSubscrOperLocalID_Type())
bsciSubscrOperLocalID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperLocalID.setStatus(_A)
_BsciSubscrOperRemoteID_Type=NlSubscriberAddress
_BsciSubscrOperRemoteID_Object=MibTableColumn
bsciSubscrOperRemoteID=_BsciSubscrOperRemoteID_Object((1,3,6,1,4,1,173,7,3,4,4,1,3),_BsciSubscrOperRemoteID_Type())
bsciSubscrOperRemoteID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperRemoteID.setStatus(_A)
class _BsciSubscrOperAutocall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciSubscrOperAutocall_Type.__name__=_B
_BsciSubscrOperAutocall_Object=MibTableColumn
bsciSubscrOperAutocall=_BsciSubscrOperAutocall_Object((1,3,6,1,4,1,173,7,3,4,4,1,4),_BsciSubscrOperAutocall_Type())
bsciSubscrOperAutocall.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperAutocall.setStatus(_A)
class _BsciSubscrOperAutocallRtyTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,255))
_BsciSubscrOperAutocallRtyTimer_Type.__name__=_B
_BsciSubscrOperAutocallRtyTimer_Object=MibTableColumn
bsciSubscrOperAutocallRtyTimer=_BsciSubscrOperAutocallRtyTimer_Object((1,3,6,1,4,1,173,7,3,4,4,1,5),_BsciSubscrOperAutocallRtyTimer_Type())
bsciSubscrOperAutocallRtyTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperAutocallRtyTimer.setStatus(_A)
class _BsciSubscrOperAutocallMaxRtry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsciSubscrOperAutocallMaxRtry_Type.__name__=_B
_BsciSubscrOperAutocallMaxRtry_Object=MibTableColumn
bsciSubscrOperAutocallMaxRtry=_BsciSubscrOperAutocallMaxRtry_Object((1,3,6,1,4,1,173,7,3,4,4,1,6),_BsciSubscrOperAutocallMaxRtry_Type())
bsciSubscrOperAutocallMaxRtry.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperAutocallMaxRtry.setStatus(_A)
class _BsciSubscrOperConnectionID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsciSubscrOperConnectionID_Type.__name__=_B
_BsciSubscrOperConnectionID_Object=MibTableColumn
bsciSubscrOperConnectionID=_BsciSubscrOperConnectionID_Object((1,3,6,1,4,1,173,7,3,4,4,1,7),_BsciSubscrOperConnectionID_Type())
bsciSubscrOperConnectionID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciSubscrOperConnectionID.setStatus(_A)
_BsciDevAdminTable_Object=MibTable
bsciDevAdminTable=_BsciDevAdminTable_Object((1,3,6,1,4,1,173,7,3,4,5))
if mibBuilder.loadTexts:bsciDevAdminTable.setStatus(_A)
_BsciDevAdminEntry_Object=MibTableRow
bsciDevAdminEntry=_BsciDevAdminEntry_Object((1,3,6,1,4,1,173,7,3,4,5,1))
bsciDevAdminEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:bsciDevAdminEntry.setStatus(_A)
class _BsciDevAdminControlUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BsciDevAdminControlUnitID_Type.__name__=_B
_BsciDevAdminControlUnitID_Object=MibTableColumn
bsciDevAdminControlUnitID=_BsciDevAdminControlUnitID_Object((1,3,6,1,4,1,173,7,3,4,5,1,1),_BsciDevAdminControlUnitID_Type())
bsciDevAdminControlUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevAdminControlUnitID.setStatus(_A)
class _BsciDevAdminDeviceUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BsciDevAdminDeviceUnitID_Type.__name__=_B
_BsciDevAdminDeviceUnitID_Object=MibTableColumn
bsciDevAdminDeviceUnitID=_BsciDevAdminDeviceUnitID_Object((1,3,6,1,4,1,173,7,3,4,5,1,2),_BsciDevAdminDeviceUnitID_Type())
bsciDevAdminDeviceUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevAdminDeviceUnitID.setStatus(_A)
class _BsciDevAdminConnectionID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsciDevAdminConnectionID_Type.__name__=_B
_BsciDevAdminConnectionID_Object=MibTableColumn
bsciDevAdminConnectionID=_BsciDevAdminConnectionID_Object((1,3,6,1,4,1,173,7,3,4,5,1,3),_BsciDevAdminConnectionID_Type())
bsciDevAdminConnectionID.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciDevAdminConnectionID.setStatus(_A)
class _BsciDevAdminSingleUserVC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciDevAdminSingleUserVC_Type.__name__=_B
_BsciDevAdminSingleUserVC_Object=MibTableColumn
bsciDevAdminSingleUserVC=_BsciDevAdminSingleUserVC_Object((1,3,6,1,4,1,173,7,3,4,5,1,4),_BsciDevAdminSingleUserVC_Type())
bsciDevAdminSingleUserVC.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciDevAdminSingleUserVC.setStatus(_A)
class _BsciDevAdminTransTextSupported_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciDevAdminTransTextSupported_Type.__name__=_B
_BsciDevAdminTransTextSupported_Object=MibTableColumn
bsciDevAdminTransTextSupported=_BsciDevAdminTransTextSupported_Object((1,3,6,1,4,1,173,7,3,4,5,1,5),_BsciDevAdminTransTextSupported_Type())
bsciDevAdminTransTextSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciDevAdminTransTextSupported.setStatus(_A)
class _BsciDevAdminPrinterAttached_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciDevAdminPrinterAttached_Type.__name__=_B
_BsciDevAdminPrinterAttached_Object=MibTableColumn
bsciDevAdminPrinterAttached=_BsciDevAdminPrinterAttached_Object((1,3,6,1,4,1,173,7,3,4,5,1,6),_BsciDevAdminPrinterAttached_Type())
bsciDevAdminPrinterAttached.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciDevAdminPrinterAttached.setStatus(_A)
_BsciDevAdminRowStatus_Type=RowStatus
_BsciDevAdminRowStatus_Object=MibTableColumn
bsciDevAdminRowStatus=_BsciDevAdminRowStatus_Object((1,3,6,1,4,1,173,7,3,4,5,1,7),_BsciDevAdminRowStatus_Type())
bsciDevAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciDevAdminRowStatus.setStatus(_A)
class _BsciDevAdminDisableStatusRequest_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),(_L,2),(_AI,3)))
_BsciDevAdminDisableStatusRequest_Type.__name__=_B
_BsciDevAdminDisableStatusRequest_Object=MibTableColumn
bsciDevAdminDisableStatusRequest=_BsciDevAdminDisableStatusRequest_Object((1,3,6,1,4,1,173,7,3,4,5,1,8),_BsciDevAdminDisableStatusRequest_Type())
bsciDevAdminDisableStatusRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:bsciDevAdminDisableStatusRequest.setStatus(_A)
_BsciDevOperTable_Object=MibTable
bsciDevOperTable=_BsciDevOperTable_Object((1,3,6,1,4,1,173,7,3,4,6))
if mibBuilder.loadTexts:bsciDevOperTable.setStatus(_A)
_BsciDevOperEntry_Object=MibTableRow
bsciDevOperEntry=_BsciDevOperEntry_Object((1,3,6,1,4,1,173,7,3,4,6,1))
bsciDevOperEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_AJ),(0,_E,_AK))
if mibBuilder.loadTexts:bsciDevOperEntry.setStatus(_A)
class _BsciDevOperControlUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BsciDevOperControlUnitID_Type.__name__=_B
_BsciDevOperControlUnitID_Object=MibTableColumn
bsciDevOperControlUnitID=_BsciDevOperControlUnitID_Object((1,3,6,1,4,1,173,7,3,4,6,1,1),_BsciDevOperControlUnitID_Type())
bsciDevOperControlUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperControlUnitID.setStatus(_A)
class _BsciDevOperDeviceUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_BsciDevOperDeviceUnitID_Type.__name__=_B
_BsciDevOperDeviceUnitID_Object=MibTableColumn
bsciDevOperDeviceUnitID=_BsciDevOperDeviceUnitID_Object((1,3,6,1,4,1,173,7,3,4,6,1,2),_BsciDevOperDeviceUnitID_Type())
bsciDevOperDeviceUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperDeviceUnitID.setStatus(_A)
class _BsciDevOperConnectionID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsciDevOperConnectionID_Type.__name__=_B
_BsciDevOperConnectionID_Object=MibTableColumn
bsciDevOperConnectionID=_BsciDevOperConnectionID_Object((1,3,6,1,4,1,173,7,3,4,6,1,3),_BsciDevOperConnectionID_Type())
bsciDevOperConnectionID.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperConnectionID.setStatus(_A)
class _BsciDevOperSingleUserVC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciDevOperSingleUserVC_Type.__name__=_B
_BsciDevOperSingleUserVC_Object=MibTableColumn
bsciDevOperSingleUserVC=_BsciDevOperSingleUserVC_Object((1,3,6,1,4,1,173,7,3,4,6,1,4),_BsciDevOperSingleUserVC_Type())
bsciDevOperSingleUserVC.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperSingleUserVC.setStatus(_A)
class _BsciDevOperTransTextSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciDevOperTransTextSupported_Type.__name__=_B
_BsciDevOperTransTextSupported_Object=MibTableColumn
bsciDevOperTransTextSupported=_BsciDevOperTransTextSupported_Object((1,3,6,1,4,1,173,7,3,4,6,1,5),_BsciDevOperTransTextSupported_Type())
bsciDevOperTransTextSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperTransTextSupported.setStatus(_A)
class _BsciDevOperPrinterAttached_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BsciDevOperPrinterAttached_Type.__name__=_B
_BsciDevOperPrinterAttached_Object=MibTableColumn
bsciDevOperPrinterAttached=_BsciDevOperPrinterAttached_Object((1,3,6,1,4,1,173,7,3,4,6,1,6),_BsciDevOperPrinterAttached_Type())
bsciDevOperPrinterAttached.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperPrinterAttached.setStatus(_A)
class _BsciDevOperDisableStatusRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),(_L,2),(_AI,3)))
_BsciDevOperDisableStatusRequest_Type.__name__=_B
_BsciDevOperDisableStatusRequest_Object=MibTableColumn
bsciDevOperDisableStatusRequest=_BsciDevOperDisableStatusRequest_Object((1,3,6,1,4,1,173,7,3,4,6,1,7),_BsciDevOperDisableStatusRequest_Type())
bsciDevOperDisableStatusRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:bsciDevOperDisableStatusRequest.setStatus(_A)
_PortSdlcGroup_ObjectIdentity=ObjectIdentity
portSdlcGroup=_PortSdlcGroup_ObjectIdentity((1,3,6,1,4,1,173,7,3,5))
_PortSdlcAdminTable_Object=MibTable
portSdlcAdminTable=_PortSdlcAdminTable_Object((1,3,6,1,4,1,173,7,3,5,1))
if mibBuilder.loadTexts:portSdlcAdminTable.setStatus(_A)
_PortSdlcAdminEntry_Object=MibTableRow
portSdlcAdminEntry=_PortSdlcAdminEntry_Object((1,3,6,1,4,1,173,7,3,5,1,1))
portSdlcAdminEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portSdlcAdminEntry.setStatus(_A)
class _PortSdlcAdminCommit_Type(Integer32):defaultValue=0
_PortSdlcAdminCommit_Type.__name__=_B
_PortSdlcAdminCommit_Object=MibTableColumn
portSdlcAdminCommit=_PortSdlcAdminCommit_Object((1,3,6,1,4,1,173,7,3,5,1,1,1),_PortSdlcAdminCommit_Type())
portSdlcAdminCommit.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminCommit.setStatus('obsolete')
class _PortSdlcAdminMAXRetries_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_PortSdlcAdminMAXRetries_Type.__name__=_B
_PortSdlcAdminMAXRetries_Object=MibTableColumn
portSdlcAdminMAXRetries=_PortSdlcAdminMAXRetries_Object((1,3,6,1,4,1,173,7,3,5,1,1,2),_PortSdlcAdminMAXRetries_Type())
portSdlcAdminMAXRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminMAXRetries.setStatus(_A)
class _PortSdlcAdminMAXOut_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PortSdlcAdminMAXOut_Type.__name__=_B
_PortSdlcAdminMAXOut_Object=MibTableColumn
portSdlcAdminMAXOut=_PortSdlcAdminMAXOut_Object((1,3,6,1,4,1,173,7,3,5,1,1,3),_PortSdlcAdminMAXOut_Type())
portSdlcAdminMAXOut.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminMAXOut.setStatus(_A)
class _PortSdlcAdminPadType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('xpad',1),(_a,2),(_b,3),('npad',4)))
_PortSdlcAdminPadType_Type.__name__=_B
_PortSdlcAdminPadType_Object=MibTableColumn
portSdlcAdminPadType=_PortSdlcAdminPadType_Object((1,3,6,1,4,1,173,7,3,5,1,1,4),_PortSdlcAdminPadType_Type())
portSdlcAdminPadType.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminPadType.setStatus(_A)
class _PortSdlcAdminGenerateClock_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcAdminGenerateClock_Type.__name__=_B
_PortSdlcAdminGenerateClock_Object=MibTableColumn
portSdlcAdminGenerateClock=_PortSdlcAdminGenerateClock_Object((1,3,6,1,4,1,173,7,3,5,1,1,5),_PortSdlcAdminGenerateClock_Type())
portSdlcAdminGenerateClock.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminGenerateClock.setStatus(_A)
class _PortSdlcAdminRcvClockFromDTE_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcAdminRcvClockFromDTE_Type.__name__=_B
_PortSdlcAdminRcvClockFromDTE_Object=MibTableColumn
portSdlcAdminRcvClockFromDTE=_PortSdlcAdminRcvClockFromDTE_Object((1,3,6,1,4,1,173,7,3,5,1,1,6),_PortSdlcAdminRcvClockFromDTE_Type())
portSdlcAdminRcvClockFromDTE.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminRcvClockFromDTE.setStatus(_A)
class _PortSdlcAdminNrz_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcAdminNrz_Type.__name__=_B
_PortSdlcAdminNrz_Object=MibTableColumn
portSdlcAdminNrz=_PortSdlcAdminNrz_Object((1,3,6,1,4,1,173,7,3,5,1,1,7),_PortSdlcAdminNrz_Type())
portSdlcAdminNrz.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminNrz.setStatus(_A)
class _PortSdlcAdminPacketSize_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_PortSdlcAdminPacketSize_Type.__name__=_B
_PortSdlcAdminPacketSize_Object=MibTableColumn
portSdlcAdminPacketSize=_PortSdlcAdminPacketSize_Object((1,3,6,1,4,1,173,7,3,5,1,1,8),_PortSdlcAdminPacketSize_Type())
portSdlcAdminPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminPacketSize.setStatus(_A)
class _PortSdlcAdminDisableRequestDisconnect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcAdminDisableRequestDisconnect_Type.__name__=_B
_PortSdlcAdminDisableRequestDisconnect_Object=MibTableColumn
portSdlcAdminDisableRequestDisconnect=_PortSdlcAdminDisableRequestDisconnect_Object((1,3,6,1,4,1,173,7,3,5,1,1,9),_PortSdlcAdminDisableRequestDisconnect_Type())
portSdlcAdminDisableRequestDisconnect.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminDisableRequestDisconnect.setStatus(_A)
class _PortSdlcAdminLPDASupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('lpda-1',2),('lpda-2',3)))
_PortSdlcAdminLPDASupport_Type.__name__=_B
_PortSdlcAdminLPDASupport_Object=MibTableColumn
portSdlcAdminLPDASupport=_PortSdlcAdminLPDASupport_Object((1,3,6,1,4,1,173,7,3,5,1,1,10),_PortSdlcAdminLPDASupport_Type())
portSdlcAdminLPDASupport.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminLPDASupport.setStatus(_A)
class _PortSdlcAdminConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10)))
_PortSdlcAdminConnector_Type.__name__=_B
_PortSdlcAdminConnector_Object=MibTableColumn
portSdlcAdminConnector=_PortSdlcAdminConnector_Object((1,3,6,1,4,1,173,7,3,5,1,1,11),_PortSdlcAdminConnector_Type())
portSdlcAdminConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminConnector.setStatus(_A)
class _PortSdlcAdminSpeed_Type(Integer32):defaultValue=64000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,2048000))
_PortSdlcAdminSpeed_Type.__name__=_B
_PortSdlcAdminSpeed_Object=MibTableColumn
portSdlcAdminSpeed=_PortSdlcAdminSpeed_Object((1,3,6,1,4,1,173,7,3,5,1,1,12),_PortSdlcAdminSpeed_Type())
portSdlcAdminSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminSpeed.setStatus(_A)
_PortSdlcAdminRowStatus_Type=RowStatus
_PortSdlcAdminRowStatus_Object=MibTableColumn
portSdlcAdminRowStatus=_PortSdlcAdminRowStatus_Object((1,3,6,1,4,1,173,7,3,5,1,1,13),_PortSdlcAdminRowStatus_Type())
portSdlcAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminRowStatus.setStatus(_A)
class _PortSdlcAdminIdleFillChar_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hex-ff',1),('hex-7e',2)))
_PortSdlcAdminIdleFillChar_Type.__name__=_B
_PortSdlcAdminIdleFillChar_Object=MibTableColumn
portSdlcAdminIdleFillChar=_PortSdlcAdminIdleFillChar_Object((1,3,6,1,4,1,173,7,3,5,1,1,14),_PortSdlcAdminIdleFillChar_Type())
portSdlcAdminIdleFillChar.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminIdleFillChar.setStatus(_A)
class _PortSdlcAdminInactivityTimer_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,250))
_PortSdlcAdminInactivityTimer_Type.__name__=_B
_PortSdlcAdminInactivityTimer_Object=MibTableColumn
portSdlcAdminInactivityTimer=_PortSdlcAdminInactivityTimer_Object((1,3,6,1,4,1,173,7,3,5,1,1,15),_PortSdlcAdminInactivityTimer_Type())
portSdlcAdminInactivityTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminInactivityTimer.setStatus(_A)
class _PortSdlcAdminL1Duplex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AL,1),(_AM,2)))
_PortSdlcAdminL1Duplex_Type.__name__=_B
_PortSdlcAdminL1Duplex_Object=MibTableColumn
portSdlcAdminL1Duplex=_PortSdlcAdminL1Duplex_Object((1,3,6,1,4,1,173,7,3,5,1,1,16),_PortSdlcAdminL1Duplex_Type())
portSdlcAdminL1Duplex.setMaxAccess(_D)
if mibBuilder.loadTexts:portSdlcAdminL1Duplex.setStatus(_A)
_PortSdlcOperTable_Object=MibTable
portSdlcOperTable=_PortSdlcOperTable_Object((1,3,6,1,4,1,173,7,3,5,2))
if mibBuilder.loadTexts:portSdlcOperTable.setStatus(_A)
_PortSdlcOperEntry_Object=MibTableRow
portSdlcOperEntry=_PortSdlcOperEntry_Object((1,3,6,1,4,1,173,7,3,5,2,1))
portSdlcOperEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portSdlcOperEntry.setStatus(_A)
_PortSdlcOperCommit_Type=Integer32
_PortSdlcOperCommit_Object=MibTableColumn
portSdlcOperCommit=_PortSdlcOperCommit_Object((1,3,6,1,4,1,173,7,3,5,2,1,1),_PortSdlcOperCommit_Type())
portSdlcOperCommit.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperCommit.setStatus('obsolete')
class _PortSdlcOperMAXRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_PortSdlcOperMAXRetries_Type.__name__=_B
_PortSdlcOperMAXRetries_Object=MibTableColumn
portSdlcOperMAXRetries=_PortSdlcOperMAXRetries_Object((1,3,6,1,4,1,173,7,3,5,2,1,2),_PortSdlcOperMAXRetries_Type())
portSdlcOperMAXRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperMAXRetries.setStatus(_A)
class _PortSdlcOperMAXOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_PortSdlcOperMAXOut_Type.__name__=_B
_PortSdlcOperMAXOut_Object=MibTableColumn
portSdlcOperMAXOut=_PortSdlcOperMAXOut_Object((1,3,6,1,4,1,173,7,3,5,2,1,3),_PortSdlcOperMAXOut_Type())
portSdlcOperMAXOut.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperMAXOut.setStatus(_A)
class _PortSdlcOperPadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('xpad',1),(_a,2),(_b,3),('npad',4)))
_PortSdlcOperPadType_Type.__name__=_B
_PortSdlcOperPadType_Object=MibTableColumn
portSdlcOperPadType=_PortSdlcOperPadType_Object((1,3,6,1,4,1,173,7,3,5,2,1,4),_PortSdlcOperPadType_Type())
portSdlcOperPadType.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperPadType.setStatus(_A)
class _PortSdlcOperGenerateClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcOperGenerateClock_Type.__name__=_B
_PortSdlcOperGenerateClock_Object=MibTableColumn
portSdlcOperGenerateClock=_PortSdlcOperGenerateClock_Object((1,3,6,1,4,1,173,7,3,5,2,1,5),_PortSdlcOperGenerateClock_Type())
portSdlcOperGenerateClock.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperGenerateClock.setStatus(_A)
class _PortSdlcOperRcvClockFromDTE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcOperRcvClockFromDTE_Type.__name__=_B
_PortSdlcOperRcvClockFromDTE_Object=MibTableColumn
portSdlcOperRcvClockFromDTE=_PortSdlcOperRcvClockFromDTE_Object((1,3,6,1,4,1,173,7,3,5,2,1,6),_PortSdlcOperRcvClockFromDTE_Type())
portSdlcOperRcvClockFromDTE.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperRcvClockFromDTE.setStatus(_A)
class _PortSdlcOperNrz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcOperNrz_Type.__name__=_B
_PortSdlcOperNrz_Object=MibTableColumn
portSdlcOperNrz=_PortSdlcOperNrz_Object((1,3,6,1,4,1,173,7,3,5,2,1,7),_PortSdlcOperNrz_Type())
portSdlcOperNrz.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperNrz.setStatus(_A)
class _PortSdlcOperPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4096))
_PortSdlcOperPacketSize_Type.__name__=_B
_PortSdlcOperPacketSize_Object=MibTableColumn
portSdlcOperPacketSize=_PortSdlcOperPacketSize_Object((1,3,6,1,4,1,173,7,3,5,2,1,8),_PortSdlcOperPacketSize_Type())
portSdlcOperPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperPacketSize.setStatus(_A)
class _PortSdlcOperDisableRequestDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortSdlcOperDisableRequestDisconnect_Type.__name__=_B
_PortSdlcOperDisableRequestDisconnect_Object=MibTableColumn
portSdlcOperDisableRequestDisconnect=_PortSdlcOperDisableRequestDisconnect_Object((1,3,6,1,4,1,173,7,3,5,2,1,9),_PortSdlcOperDisableRequestDisconnect_Type())
portSdlcOperDisableRequestDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperDisableRequestDisconnect.setStatus(_A)
class _PortSdlcOperLPDASupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('lpda-1',2),('lpda-2',3)))
_PortSdlcOperLPDASupport_Type.__name__=_B
_PortSdlcOperLPDASupport_Object=MibTableColumn
portSdlcOperLPDASupport=_PortSdlcOperLPDASupport_Object((1,3,6,1,4,1,173,7,3,5,2,1,10),_PortSdlcOperLPDASupport_Type())
portSdlcOperLPDASupport.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperLPDASupport.setStatus(_A)
class _PortSdlcOperConnector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,7,8,10)));namedValues=NamedValues(*((_N,3),(_O,5),(_R,6),(_T,7),(_Q,8),(_P,10)))
_PortSdlcOperConnector_Type.__name__=_B
_PortSdlcOperConnector_Object=MibTableColumn
portSdlcOperConnector=_PortSdlcOperConnector_Object((1,3,6,1,4,1,173,7,3,5,2,1,11),_PortSdlcOperConnector_Type())
portSdlcOperConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperConnector.setStatus(_A)
_PortSdlcOperSpeed_Type=Integer32
_PortSdlcOperSpeed_Object=MibTableColumn
portSdlcOperSpeed=_PortSdlcOperSpeed_Object((1,3,6,1,4,1,173,7,3,5,2,1,12),_PortSdlcOperSpeed_Type())
portSdlcOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperSpeed.setStatus(_A)
class _PortSdlcOperIdleFillChar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hex-ff',1),('hex-7e',2)))
_PortSdlcOperIdleFillChar_Type.__name__=_B
_PortSdlcOperIdleFillChar_Object=MibTableColumn
portSdlcOperIdleFillChar=_PortSdlcOperIdleFillChar_Object((1,3,6,1,4,1,173,7,3,5,2,1,13),_PortSdlcOperIdleFillChar_Type())
portSdlcOperIdleFillChar.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperIdleFillChar.setStatus(_A)
class _PortSdlcOperInactivityTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,250))
_PortSdlcOperInactivityTimer_Type.__name__=_B
_PortSdlcOperInactivityTimer_Object=MibTableColumn
portSdlcOperInactivityTimer=_PortSdlcOperInactivityTimer_Object((1,3,6,1,4,1,173,7,3,5,2,1,14),_PortSdlcOperInactivityTimer_Type())
portSdlcOperInactivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperInactivityTimer.setStatus(_A)
class _PortSdlcOperL1Duplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AL,1),(_AM,2)))
_PortSdlcOperL1Duplex_Type.__name__=_B
_PortSdlcOperL1Duplex_Object=MibTableColumn
portSdlcOperL1Duplex=_PortSdlcOperL1Duplex_Object((1,3,6,1,4,1,173,7,3,5,2,1,15),_PortSdlcOperL1Duplex_Type())
portSdlcOperL1Duplex.setMaxAccess(_C)
if mibBuilder.loadTexts:portSdlcOperL1Duplex.setStatus(_A)
_LSSdlcAdminTable_Object=MibTable
lSSdlcAdminTable=_LSSdlcAdminTable_Object((1,3,6,1,4,1,173,7,3,5,3))
if mibBuilder.loadTexts:lSSdlcAdminTable.setStatus(_A)
_LSSdlcAdminEntry_Object=MibTableRow
lSSdlcAdminEntry=_LSSdlcAdminEntry_Object((1,3,6,1,4,1,173,7,3,5,3,1))
lSSdlcAdminEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:lSSdlcAdminEntry.setStatus(_A)
_LSSdlcAdminLocalSub_Type=NlSubscriberAddress
_LSSdlcAdminLocalSub_Object=MibTableColumn
lSSdlcAdminLocalSub=_LSSdlcAdminLocalSub_Object((1,3,6,1,4,1,173,7,3,5,3,1,1),_LSSdlcAdminLocalSub_Type())
lSSdlcAdminLocalSub.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminLocalSub.setStatus(_A)
_LSSdlcAdminRemoteSub_Type=NlSubscriberAddress
_LSSdlcAdminRemoteSub_Object=MibTableColumn
lSSdlcAdminRemoteSub=_LSSdlcAdminRemoteSub_Object((1,3,6,1,4,1,173,7,3,5,3,1,2),_LSSdlcAdminRemoteSub_Type())
lSSdlcAdminRemoteSub.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminRemoteSub.setStatus(_A)
class _LSSdlcAdminAutoCall_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LSSdlcAdminAutoCall_Type.__name__=_B
_LSSdlcAdminAutoCall_Object=MibTableColumn
lSSdlcAdminAutoCall=_LSSdlcAdminAutoCall_Object((1,3,6,1,4,1,173,7,3,5,3,1,3),_LSSdlcAdminAutoCall_Type())
lSSdlcAdminAutoCall.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminAutoCall.setStatus(_A)
class _LSSdlcAdminRetryTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,225))
_LSSdlcAdminRetryTime_Type.__name__=_B
_LSSdlcAdminRetryTime_Object=MibTableColumn
lSSdlcAdminRetryTime=_LSSdlcAdminRetryTime_Object((1,3,6,1,4,1,173,7,3,5,3,1,4),_LSSdlcAdminRetryTime_Type())
lSSdlcAdminRetryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminRetryTime.setStatus(_A)
class _LSSdlcAdminRetryCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LSSdlcAdminRetryCount_Type.__name__=_B
_LSSdlcAdminRetryCount_Object=MibTableColumn
lSSdlcAdminRetryCount=_LSSdlcAdminRetryCount_Object((1,3,6,1,4,1,173,7,3,5,3,1,5),_LSSdlcAdminRetryCount_Type())
lSSdlcAdminRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminRetryCount.setStatus(_A)
class _LSSdlcAdminLlc2Conversion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LSSdlcAdminLlc2Conversion_Type.__name__=_B
_LSSdlcAdminLlc2Conversion_Object=MibTableColumn
lSSdlcAdminLlc2Conversion=_LSSdlcAdminLlc2Conversion_Object((1,3,6,1,4,1,173,7,3,5,3,1,6),_LSSdlcAdminLlc2Conversion_Type())
lSSdlcAdminLlc2Conversion.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminLlc2Conversion.setStatus(_A)
class _LSSdlcAdminLPDAResourceID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LSSdlcAdminLPDAResourceID_Type.__name__=_B
_LSSdlcAdminLPDAResourceID_Object=MibTableColumn
lSSdlcAdminLPDAResourceID=_LSSdlcAdminLPDAResourceID_Object((1,3,6,1,4,1,173,7,3,5,3,1,7),_LSSdlcAdminLPDAResourceID_Type())
lSSdlcAdminLPDAResourceID.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminLPDAResourceID.setStatus(_A)
_LSSdlcAdminRowStatus_Type=RowStatus
_LSSdlcAdminRowStatus_Object=MibTableColumn
lSSdlcAdminRowStatus=_LSSdlcAdminRowStatus_Object((1,3,6,1,4,1,173,7,3,5,3,1,8),_LSSdlcAdminRowStatus_Type())
lSSdlcAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminRowStatus.setStatus(_A)
class _LSSdlcAdminL2DatMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AN,1),(_AO,2)))
_LSSdlcAdminL2DatMode_Type.__name__=_B
_LSSdlcAdminL2DatMode_Object=MibTableColumn
lSSdlcAdminL2DatMode=_LSSdlcAdminL2DatMode_Object((1,3,6,1,4,1,173,7,3,5,3,1,9),_LSSdlcAdminL2DatMode_Type())
lSSdlcAdminL2DatMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcAdminL2DatMode.setStatus(_A)
_LSSdlcOperTable_Object=MibTable
lSSdlcOperTable=_LSSdlcOperTable_Object((1,3,6,1,4,1,173,7,3,5,4))
if mibBuilder.loadTexts:lSSdlcOperTable.setStatus(_A)
_LSSdlcOperEntry_Object=MibTableRow
lSSdlcOperEntry=_LSSdlcOperEntry_Object((1,3,6,1,4,1,173,7,3,5,4,1))
lSSdlcOperEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:lSSdlcOperEntry.setStatus(_A)
_LSSdlcOperLocalSub_Type=NlSubscriberAddress
_LSSdlcOperLocalSub_Object=MibTableColumn
lSSdlcOperLocalSub=_LSSdlcOperLocalSub_Object((1,3,6,1,4,1,173,7,3,5,4,1,1),_LSSdlcOperLocalSub_Type())
lSSdlcOperLocalSub.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperLocalSub.setStatus(_A)
_LSSdlcOperRemoteSub_Type=NlSubscriberAddress
_LSSdlcOperRemoteSub_Object=MibTableColumn
lSSdlcOperRemoteSub=_LSSdlcOperRemoteSub_Object((1,3,6,1,4,1,173,7,3,5,4,1,2),_LSSdlcOperRemoteSub_Type())
lSSdlcOperRemoteSub.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperRemoteSub.setStatus(_A)
class _LSSdlcOperAutoCall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LSSdlcOperAutoCall_Type.__name__=_B
_LSSdlcOperAutoCall_Object=MibTableColumn
lSSdlcOperAutoCall=_LSSdlcOperAutoCall_Object((1,3,6,1,4,1,173,7,3,5,4,1,3),_LSSdlcOperAutoCall_Type())
lSSdlcOperAutoCall.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperAutoCall.setStatus(_A)
class _LSSdlcOperRetryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,225))
_LSSdlcOperRetryTime_Type.__name__=_B
_LSSdlcOperRetryTime_Object=MibTableColumn
lSSdlcOperRetryTime=_LSSdlcOperRetryTime_Object((1,3,6,1,4,1,173,7,3,5,4,1,4),_LSSdlcOperRetryTime_Type())
lSSdlcOperRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperRetryTime.setStatus(_A)
class _LSSdlcOperRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LSSdlcOperRetryCount_Type.__name__=_B
_LSSdlcOperRetryCount_Object=MibTableColumn
lSSdlcOperRetryCount=_LSSdlcOperRetryCount_Object((1,3,6,1,4,1,173,7,3,5,4,1,5),_LSSdlcOperRetryCount_Type())
lSSdlcOperRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperRetryCount.setStatus(_A)
class _LSSdlcOperLlc2Conversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LSSdlcOperLlc2Conversion_Type.__name__=_B
_LSSdlcOperLlc2Conversion_Object=MibTableColumn
lSSdlcOperLlc2Conversion=_LSSdlcOperLlc2Conversion_Object((1,3,6,1,4,1,173,7,3,5,4,1,6),_LSSdlcOperLlc2Conversion_Type())
lSSdlcOperLlc2Conversion.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperLlc2Conversion.setStatus(_A)
class _LSSdlcOperLPDAResourceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LSSdlcOperLPDAResourceID_Type.__name__=_B
_LSSdlcOperLPDAResourceID_Object=MibTableColumn
lSSdlcOperLPDAResourceID=_LSSdlcOperLPDAResourceID_Object((1,3,6,1,4,1,173,7,3,5,4,1,7),_LSSdlcOperLPDAResourceID_Type())
lSSdlcOperLPDAResourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperLPDAResourceID.setStatus(_A)
class _LSSdlcOperL2DatMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AN,1),(_AO,2)))
_LSSdlcOperL2DatMode_Type.__name__=_B
_LSSdlcOperL2DatMode_Object=MibTableColumn
lSSdlcOperL2DatMode=_LSSdlcOperL2DatMode_Object((1,3,6,1,4,1,173,7,3,5,4,1,8),_LSSdlcOperL2DatMode_Type())
lSSdlcOperL2DatMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcOperL2DatMode.setStatus(_A)
_LSSdlcLlc2AdminTable_Object=MibTable
lSSdlcLlc2AdminTable=_LSSdlcLlc2AdminTable_Object((1,3,6,1,4,1,173,7,3,5,5))
if mibBuilder.loadTexts:lSSdlcLlc2AdminTable.setStatus(_A)
_LSSdlcLlc2AdminEntry_Object=MibTableRow
lSSdlcLlc2AdminEntry=_LSSdlcLlc2AdminEntry_Object((1,3,6,1,4,1,173,7,3,5,5,1))
lSSdlcLlc2AdminEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:lSSdlcLlc2AdminEntry.setStatus(_A)
class _LSSdlcLlc2AdminLocalSap_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,252))
_LSSdlcLlc2AdminLocalSap_Type.__name__=_B
_LSSdlcLlc2AdminLocalSap_Object=MibTableColumn
lSSdlcLlc2AdminLocalSap=_LSSdlcLlc2AdminLocalSap_Object((1,3,6,1,4,1,173,7,3,5,5,1,1),_LSSdlcLlc2AdminLocalSap_Type())
lSSdlcLlc2AdminLocalSap.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLocalSap.setStatus(_A)
class _LSSdlcLlc2AdminLocalMac_Type(PhysAddress):defaultHexValue=_AP
_LSSdlcLlc2AdminLocalMac_Type.__name__=_u
_LSSdlcLlc2AdminLocalMac_Object=MibTableColumn
lSSdlcLlc2AdminLocalMac=_LSSdlcLlc2AdminLocalMac_Object((1,3,6,1,4,1,173,7,3,5,5,1,2),_LSSdlcLlc2AdminLocalMac_Type())
lSSdlcLlc2AdminLocalMac.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLocalMac.setStatus(_A)
class _LSSdlcLlc2AdminIdblk_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LSSdlcLlc2AdminIdblk_Type.__name__=_B
_LSSdlcLlc2AdminIdblk_Object=MibTableColumn
lSSdlcLlc2AdminIdblk=_LSSdlcLlc2AdminIdblk_Object((1,3,6,1,4,1,173,7,3,5,5,1,3),_LSSdlcLlc2AdminIdblk_Type())
lSSdlcLlc2AdminIdblk.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminIdblk.setStatus(_A)
class _LSSdlcLlc2AdminIdnum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_LSSdlcLlc2AdminIdnum_Type.__name__=_B
_LSSdlcLlc2AdminIdnum_Object=MibTableColumn
lSSdlcLlc2AdminIdnum=_LSSdlcLlc2AdminIdnum_Object((1,3,6,1,4,1,173,7,3,5,5,1,4),_LSSdlcLlc2AdminIdnum_Type())
lSSdlcLlc2AdminIdnum.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminIdnum.setStatus(_A)
class _LSSdlcLlc2AdminLanTi_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_LSSdlcLlc2AdminLanTi_Type.__name__=_B
_LSSdlcLlc2AdminLanTi_Object=MibTableColumn
lSSdlcLlc2AdminLanTi=_LSSdlcLlc2AdminLanTi_Object((1,3,6,1,4,1,173,7,3,5,5,1,5),_LSSdlcLlc2AdminLanTi_Type())
lSSdlcLlc2AdminLanTi.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLanTi.setStatus(_A)
class _LSSdlcLlc2AdminLanT1_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_LSSdlcLlc2AdminLanT1_Type.__name__=_B
_LSSdlcLlc2AdminLanT1_Object=MibTableColumn
lSSdlcLlc2AdminLanT1=_LSSdlcLlc2AdminLanT1_Object((1,3,6,1,4,1,173,7,3,5,5,1,6),_LSSdlcLlc2AdminLanT1_Type())
lSSdlcLlc2AdminLanT1.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLanT1.setStatus(_A)
class _LSSdlcLlc2AdminLanT2_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_LSSdlcLlc2AdminLanT2_Type.__name__=_B
_LSSdlcLlc2AdminLanT2_Object=MibTableColumn
lSSdlcLlc2AdminLanT2=_LSSdlcLlc2AdminLanT2_Object((1,3,6,1,4,1,173,7,3,5,5,1,7),_LSSdlcLlc2AdminLanT2_Type())
lSSdlcLlc2AdminLanT2.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLanT2.setStatus(_A)
class _LSSdlcLlc2AdminLanN2_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LSSdlcLlc2AdminLanN2_Type.__name__=_B
_LSSdlcLlc2AdminLanN2_Object=MibTableColumn
lSSdlcLlc2AdminLanN2=_LSSdlcLlc2AdminLanN2_Object((1,3,6,1,4,1,173,7,3,5,5,1,8),_LSSdlcLlc2AdminLanN2_Type())
lSSdlcLlc2AdminLanN2.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLanN2.setStatus(_A)
class _LSSdlcLlc2AdminLanN3_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LSSdlcLlc2AdminLanN3_Type.__name__=_B
_LSSdlcLlc2AdminLanN3_Object=MibTableColumn
lSSdlcLlc2AdminLanN3=_LSSdlcLlc2AdminLanN3_Object((1,3,6,1,4,1,173,7,3,5,5,1,9),_LSSdlcLlc2AdminLanN3_Type())
lSSdlcLlc2AdminLanN3.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLanN3.setStatus(_A)
class _LSSdlcLlc2AdminLanTw_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LSSdlcLlc2AdminLanTw_Type.__name__=_B
_LSSdlcLlc2AdminLanTw_Object=MibTableColumn
lSSdlcLlc2AdminLanTw=_LSSdlcLlc2AdminLanTw_Object((1,3,6,1,4,1,173,7,3,5,5,1,10),_LSSdlcLlc2AdminLanTw_Type())
lSSdlcLlc2AdminLanTw.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminLanTw.setStatus(_A)
class _LSSdlcLlc2AdminBAG_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_LSSdlcLlc2AdminBAG_Type.__name__=_B
_LSSdlcLlc2AdminBAG_Object=MibTableColumn
lSSdlcLlc2AdminBAG=_LSSdlcLlc2AdminBAG_Object((1,3,6,1,4,1,173,7,3,5,5,1,11),_LSSdlcLlc2AdminBAG_Type())
lSSdlcLlc2AdminBAG.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminBAG.setStatus(_A)
class _LSSdlcLlc2AdminPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_LSSdlcLlc2AdminPriority_Type.__name__=_B
_LSSdlcLlc2AdminPriority_Object=MibTableColumn
lSSdlcLlc2AdminPriority=_LSSdlcLlc2AdminPriority_Object((1,3,6,1,4,1,173,7,3,5,5,1,12),_LSSdlcLlc2AdminPriority_Type())
lSSdlcLlc2AdminPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminPriority.setStatus(_A)
_LSSdlcLlc2AdminRowStatus_Type=RowStatus
_LSSdlcLlc2AdminRowStatus_Object=MibTableColumn
lSSdlcLlc2AdminRowStatus=_LSSdlcLlc2AdminRowStatus_Object((1,3,6,1,4,1,173,7,3,5,5,1,13),_LSSdlcLlc2AdminRowStatus_Type())
lSSdlcLlc2AdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminRowStatus.setStatus(_A)
class _LSSdlcLlc2AdminSuppressXID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LSSdlcLlc2AdminSuppressXID_Type.__name__=_B
_LSSdlcLlc2AdminSuppressXID_Object=MibTableColumn
lSSdlcLlc2AdminSuppressXID=_LSSdlcLlc2AdminSuppressXID_Object((1,3,6,1,4,1,173,7,3,5,5,1,14),_LSSdlcLlc2AdminSuppressXID_Type())
lSSdlcLlc2AdminSuppressXID.setMaxAccess(_D)
if mibBuilder.loadTexts:lSSdlcLlc2AdminSuppressXID.setStatus(_A)
_LSSdlcLlc2OperTable_Object=MibTable
lSSdlcLlc2OperTable=_LSSdlcLlc2OperTable_Object((1,3,6,1,4,1,173,7,3,5,6))
if mibBuilder.loadTexts:lSSdlcLlc2OperTable.setStatus(_A)
_LSSdlcLlc2OperEntry_Object=MibTableRow
lSSdlcLlc2OperEntry=_LSSdlcLlc2OperEntry_Object((1,3,6,1,4,1,173,7,3,5,6,1))
lSSdlcLlc2OperEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:lSSdlcLlc2OperEntry.setStatus(_A)
class _LSSdlcLlc2OperLocalSap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,252))
_LSSdlcLlc2OperLocalSap_Type.__name__=_B
_LSSdlcLlc2OperLocalSap_Object=MibTableColumn
lSSdlcLlc2OperLocalSap=_LSSdlcLlc2OperLocalSap_Object((1,3,6,1,4,1,173,7,3,5,6,1,1),_LSSdlcLlc2OperLocalSap_Type())
lSSdlcLlc2OperLocalSap.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLocalSap.setStatus(_A)
_LSSdlcLlc2OperLocalMac_Type=PhysAddress
_LSSdlcLlc2OperLocalMac_Object=MibTableColumn
lSSdlcLlc2OperLocalMac=_LSSdlcLlc2OperLocalMac_Object((1,3,6,1,4,1,173,7,3,5,6,1,2),_LSSdlcLlc2OperLocalMac_Type())
lSSdlcLlc2OperLocalMac.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLocalMac.setStatus(_A)
class _LSSdlcLlc2OperIdblk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LSSdlcLlc2OperIdblk_Type.__name__=_B
_LSSdlcLlc2OperIdblk_Object=MibTableColumn
lSSdlcLlc2OperIdblk=_LSSdlcLlc2OperIdblk_Object((1,3,6,1,4,1,173,7,3,5,6,1,3),_LSSdlcLlc2OperIdblk_Type())
lSSdlcLlc2OperIdblk.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperIdblk.setStatus(_A)
class _LSSdlcLlc2OperIdnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_LSSdlcLlc2OperIdnum_Type.__name__=_B
_LSSdlcLlc2OperIdnum_Object=MibTableColumn
lSSdlcLlc2OperIdnum=_LSSdlcLlc2OperIdnum_Object((1,3,6,1,4,1,173,7,3,5,6,1,4),_LSSdlcLlc2OperIdnum_Type())
lSSdlcLlc2OperIdnum.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperIdnum.setStatus(_A)
class _LSSdlcLlc2OperLanTi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_LSSdlcLlc2OperLanTi_Type.__name__=_B
_LSSdlcLlc2OperLanTi_Object=MibTableColumn
lSSdlcLlc2OperLanTi=_LSSdlcLlc2OperLanTi_Object((1,3,6,1,4,1,173,7,3,5,6,1,5),_LSSdlcLlc2OperLanTi_Type())
lSSdlcLlc2OperLanTi.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLanTi.setStatus(_A)
class _LSSdlcLlc2OperLanT1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_LSSdlcLlc2OperLanT1_Type.__name__=_B
_LSSdlcLlc2OperLanT1_Object=MibTableColumn
lSSdlcLlc2OperLanT1=_LSSdlcLlc2OperLanT1_Object((1,3,6,1,4,1,173,7,3,5,6,1,6),_LSSdlcLlc2OperLanT1_Type())
lSSdlcLlc2OperLanT1.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLanT1.setStatus(_A)
class _LSSdlcLlc2OperLanT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_LSSdlcLlc2OperLanT2_Type.__name__=_B
_LSSdlcLlc2OperLanT2_Object=MibTableColumn
lSSdlcLlc2OperLanT2=_LSSdlcLlc2OperLanT2_Object((1,3,6,1,4,1,173,7,3,5,6,1,7),_LSSdlcLlc2OperLanT2_Type())
lSSdlcLlc2OperLanT2.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLanT2.setStatus(_A)
class _LSSdlcLlc2OperLanN2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LSSdlcLlc2OperLanN2_Type.__name__=_B
_LSSdlcLlc2OperLanN2_Object=MibTableColumn
lSSdlcLlc2OperLanN2=_LSSdlcLlc2OperLanN2_Object((1,3,6,1,4,1,173,7,3,5,6,1,8),_LSSdlcLlc2OperLanN2_Type())
lSSdlcLlc2OperLanN2.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLanN2.setStatus(_A)
class _LSSdlcLlc2OperLanN3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LSSdlcLlc2OperLanN3_Type.__name__=_B
_LSSdlcLlc2OperLanN3_Object=MibTableColumn
lSSdlcLlc2OperLanN3=_LSSdlcLlc2OperLanN3_Object((1,3,6,1,4,1,173,7,3,5,6,1,9),_LSSdlcLlc2OperLanN3_Type())
lSSdlcLlc2OperLanN3.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLanN3.setStatus(_A)
class _LSSdlcLlc2OperLanTw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_LSSdlcLlc2OperLanTw_Type.__name__=_B
_LSSdlcLlc2OperLanTw_Object=MibTableColumn
lSSdlcLlc2OperLanTw=_LSSdlcLlc2OperLanTw_Object((1,3,6,1,4,1,173,7,3,5,6,1,10),_LSSdlcLlc2OperLanTw_Type())
lSSdlcLlc2OperLanTw.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperLanTw.setStatus(_A)
class _LSSdlcLlc2OperBAG_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_LSSdlcLlc2OperBAG_Type.__name__=_B
_LSSdlcLlc2OperBAG_Object=MibTableColumn
lSSdlcLlc2OperBAG=_LSSdlcLlc2OperBAG_Object((1,3,6,1,4,1,173,7,3,5,6,1,11),_LSSdlcLlc2OperBAG_Type())
lSSdlcLlc2OperBAG.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperBAG.setStatus(_A)
class _LSSdlcLlc2OperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_LSSdlcLlc2OperPriority_Type.__name__=_B
_LSSdlcLlc2OperPriority_Object=MibTableColumn
lSSdlcLlc2OperPriority=_LSSdlcLlc2OperPriority_Object((1,3,6,1,4,1,173,7,3,5,6,1,12),_LSSdlcLlc2OperPriority_Type())
lSSdlcLlc2OperPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperPriority.setStatus(_A)
class _LSSdlcLlc2OperSuppressXID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LSSdlcLlc2OperSuppressXID_Type.__name__=_B
_LSSdlcLlc2OperSuppressXID_Object=MibTableColumn
lSSdlcLlc2OperSuppressXID=_LSSdlcLlc2OperSuppressXID_Object((1,3,6,1,4,1,173,7,3,5,6,1,13),_LSSdlcLlc2OperSuppressXID_Type())
lSSdlcLlc2OperSuppressXID.setMaxAccess(_C)
if mibBuilder.loadTexts:lSSdlcLlc2OperSuppressXID.setStatus(_A)
_PortT1Group_ObjectIdentity=ObjectIdentity
portT1Group=_PortT1Group_ObjectIdentity((1,3,6,1,4,1,173,7,3,7))
_PortT1AdminTable_Object=MibTable
portT1AdminTable=_PortT1AdminTable_Object((1,3,6,1,4,1,173,7,3,7,1))
if mibBuilder.loadTexts:portT1AdminTable.setStatus(_A)
_PortT1AdminEntry_Object=MibTableRow
portT1AdminEntry=_PortT1AdminEntry_Object((1,3,6,1,4,1,173,7,3,7,1,1))
portT1AdminEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portT1AdminEntry.setStatus(_A)
class _PortT1AdminBlockedPortFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortT1AdminBlockedPortFlag_Type.__name__=_B
_PortT1AdminBlockedPortFlag_Object=MibTableColumn
portT1AdminBlockedPortFlag=_PortT1AdminBlockedPortFlag_Object((1,3,6,1,4,1,173,7,3,7,1,1,1),_PortT1AdminBlockedPortFlag_Type())
portT1AdminBlockedPortFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminBlockedPortFlag.setStatus(_A)
class _PortT1AdminGenerateClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortT1AdminGenerateClock_Type.__name__=_B
_PortT1AdminGenerateClock_Object=MibTableColumn
portT1AdminGenerateClock=_PortT1AdminGenerateClock_Object((1,3,6,1,4,1,173,7,3,7,1,1,2),_PortT1AdminGenerateClock_Type())
portT1AdminGenerateClock.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminGenerateClock.setStatus(_A)
class _PortT1AdminFramingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullT1',1),('ds0aT1',2)))
_PortT1AdminFramingMode_Type.__name__=_B
_PortT1AdminFramingMode_Object=MibTableColumn
portT1AdminFramingMode=_PortT1AdminFramingMode_Object((1,3,6,1,4,1,173,7,3,7,1,1,3),_PortT1AdminFramingMode_Type())
portT1AdminFramingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminFramingMode.setStatus(_A)
class _PortT1AdminFrameModelSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('d4',1),('esf',2)))
_PortT1AdminFrameModelSelect_Type.__name__=_B
_PortT1AdminFrameModelSelect_Object=MibTableColumn
portT1AdminFrameModelSelect=_PortT1AdminFrameModelSelect_Object((1,3,6,1,4,1,173,7,3,7,1,1,4),_PortT1AdminFrameModelSelect_Type())
portT1AdminFrameModelSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminFrameModelSelect.setStatus(_A)
class _PortT1AdminLineEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('b8zs',1),('ami',2)))
_PortT1AdminLineEncoding_Type.__name__=_B
_PortT1AdminLineEncoding_Object=MibTableColumn
portT1AdminLineEncoding=_PortT1AdminLineEncoding_Object((1,3,6,1,4,1,173,7,3,7,1,1,5),_PortT1AdminLineEncoding_Type())
portT1AdminLineEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminLineEncoding.setStatus(_A)
class _PortT1AdminLineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('zerodb',1),(_AQ,2),(_AR,3),(_AS,4),(_AT,5),(_AU,6),(_AV,7),(_AW,8)))
_PortT1AdminLineBuildOut_Type.__name__=_B
_PortT1AdminLineBuildOut_Object=MibTableColumn
portT1AdminLineBuildOut=_PortT1AdminLineBuildOut_Object((1,3,6,1,4,1,173,7,3,7,1,1,6),_PortT1AdminLineBuildOut_Type())
portT1AdminLineBuildOut.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminLineBuildOut.setStatus(_A)
_PortT1AdminRowStatus_Type=RowStatus
_PortT1AdminRowStatus_Object=MibTableColumn
portT1AdminRowStatus=_PortT1AdminRowStatus_Object((1,3,6,1,4,1,173,7,3,7,1,1,7),_PortT1AdminRowStatus_Type())
portT1AdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminRowStatus.setStatus(_A)
class _PortT1AdminProtocolFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),('bisync',2)))
_PortT1AdminProtocolFraming_Type.__name__=_B
_PortT1AdminProtocolFraming_Object=MibTableColumn
portT1AdminProtocolFraming=_PortT1AdminProtocolFraming_Object((1,3,6,1,4,1,173,7,3,7,1,1,8),_PortT1AdminProtocolFraming_Type())
portT1AdminProtocolFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminProtocolFraming.setStatus(_A)
class _PortT1AdminNRZI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortT1AdminNRZI_Type.__name__=_B
_PortT1AdminNRZI_Object=MibTableColumn
portT1AdminNRZI=_PortT1AdminNRZI_Object((1,3,6,1,4,1,173,7,3,7,1,1,9),_PortT1AdminNRZI_Type())
portT1AdminNRZI.setMaxAccess(_D)
if mibBuilder.loadTexts:portT1AdminNRZI.setStatus(_A)
_PortT1OperTable_Object=MibTable
portT1OperTable=_PortT1OperTable_Object((1,3,6,1,4,1,173,7,3,7,2))
if mibBuilder.loadTexts:portT1OperTable.setStatus(_A)
_PortT1OperEntry_Object=MibTableRow
portT1OperEntry=_PortT1OperEntry_Object((1,3,6,1,4,1,173,7,3,7,2,1))
portT1OperEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:portT1OperEntry.setStatus(_A)
class _PortT1OperBlockedPortFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortT1OperBlockedPortFlag_Type.__name__=_B
_PortT1OperBlockedPortFlag_Object=MibTableColumn
portT1OperBlockedPortFlag=_PortT1OperBlockedPortFlag_Object((1,3,6,1,4,1,173,7,3,7,2,1,1),_PortT1OperBlockedPortFlag_Type())
portT1OperBlockedPortFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperBlockedPortFlag.setStatus(_A)
class _PortT1OperGenerateClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortT1OperGenerateClock_Type.__name__=_B
_PortT1OperGenerateClock_Object=MibTableColumn
portT1OperGenerateClock=_PortT1OperGenerateClock_Object((1,3,6,1,4,1,173,7,3,7,2,1,2),_PortT1OperGenerateClock_Type())
portT1OperGenerateClock.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperGenerateClock.setStatus(_A)
class _PortT1OperFramingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullT1',1),('ds0aT1',2)))
_PortT1OperFramingMode_Type.__name__=_B
_PortT1OperFramingMode_Object=MibTableColumn
portT1OperFramingMode=_PortT1OperFramingMode_Object((1,3,6,1,4,1,173,7,3,7,2,1,3),_PortT1OperFramingMode_Type())
portT1OperFramingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperFramingMode.setStatus(_A)
class _PortT1OperFrameModelSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('d4',1),('esf',2)))
_PortT1OperFrameModelSelect_Type.__name__=_B
_PortT1OperFrameModelSelect_Object=MibTableColumn
portT1OperFrameModelSelect=_PortT1OperFrameModelSelect_Object((1,3,6,1,4,1,173,7,3,7,2,1,4),_PortT1OperFrameModelSelect_Type())
portT1OperFrameModelSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperFrameModelSelect.setStatus(_A)
class _PortT1OperLineEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('b8zs',1),('ami',2)))
_PortT1OperLineEncoding_Type.__name__=_B
_PortT1OperLineEncoding_Object=MibTableColumn
portT1OperLineEncoding=_PortT1OperLineEncoding_Object((1,3,6,1,4,1,173,7,3,7,2,1,5),_PortT1OperLineEncoding_Type())
portT1OperLineEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperLineEncoding.setStatus(_A)
class _PortT1OperLineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('zerodb',1),(_AQ,2),(_AR,3),(_AS,4),(_AT,5),(_AU,6),(_AV,7),(_AW,8)))
_PortT1OperLineBuildOut_Type.__name__=_B
_PortT1OperLineBuildOut_Object=MibTableColumn
portT1OperLineBuildOut=_PortT1OperLineBuildOut_Object((1,3,6,1,4,1,173,7,3,7,2,1,6),_PortT1OperLineBuildOut_Type())
portT1OperLineBuildOut.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperLineBuildOut.setStatus(_A)
class _PortT1OperProtocolFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),('bisync',2)))
_PortT1OperProtocolFraming_Type.__name__=_B
_PortT1OperProtocolFraming_Object=MibTableColumn
portT1OperProtocolFraming=_PortT1OperProtocolFraming_Object((1,3,6,1,4,1,173,7,3,7,2,1,7),_PortT1OperProtocolFraming_Type())
portT1OperProtocolFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperProtocolFraming.setStatus(_A)
class _PortT1OperNRZI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortT1OperNRZI_Type.__name__=_B
_PortT1OperNRZI_Object=MibTableColumn
portT1OperNRZI=_PortT1OperNRZI_Object((1,3,6,1,4,1,173,7,3,7,2,1,8),_PortT1OperNRZI_Type())
portT1OperNRZI.setMaxAccess(_C)
if mibBuilder.loadTexts:portT1OperNRZI.setStatus(_A)
_PortVoiceGroup_ObjectIdentity=ObjectIdentity
portVoiceGroup=_PortVoiceGroup_ObjectIdentity((1,3,6,1,4,1,173,7,3,8))
_PortVoiceAdminTable_Object=MibTable
portVoiceAdminTable=_PortVoiceAdminTable_Object((1,3,6,1,4,1,173,7,3,8,1))
if mibBuilder.loadTexts:portVoiceAdminTable.setStatus(_A)
_PortVoiceAdminEntry_Object=MibTableRow
portVoiceAdminEntry=_PortVoiceAdminEntry_Object((1,3,6,1,4,1,173,7,3,8,1,1))
portVoiceAdminEntry.setIndexNames((0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:portVoiceAdminEntry.setStatus(_A)
_PortVoiceAdminRlpIndex_Type=Integer32
_PortVoiceAdminRlpIndex_Object=MibTableColumn
portVoiceAdminRlpIndex=_PortVoiceAdminRlpIndex_Object((1,3,6,1,4,1,173,7,3,8,1,1,1),_PortVoiceAdminRlpIndex_Type())
portVoiceAdminRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceAdminRlpIndex.setStatus(_A)
_PortVoiceAdminPortIndex_Type=Integer32
_PortVoiceAdminPortIndex_Object=MibTableColumn
portVoiceAdminPortIndex=_PortVoiceAdminPortIndex_Object((1,3,6,1,4,1,173,7,3,8,1,1,2),_PortVoiceAdminPortIndex_Type())
portVoiceAdminPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceAdminPortIndex.setStatus(_A)
class _PortVoiceAdminBlockedFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceAdminBlockedFlag_Type.__name__=_B
_PortVoiceAdminBlockedFlag_Object=MibTableColumn
portVoiceAdminBlockedFlag=_PortVoiceAdminBlockedFlag_Object((1,3,6,1,4,1,173,7,3,8,1,1,3),_PortVoiceAdminBlockedFlag_Type())
portVoiceAdminBlockedFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminBlockedFlag.setStatus(_A)
class _PortVoiceAdminSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4)))
_PortVoiceAdminSpeed_Type.__name__=_B
_PortVoiceAdminSpeed_Object=MibTableColumn
portVoiceAdminSpeed=_PortVoiceAdminSpeed_Object((1,3,6,1,4,1,173,7,3,8,1,1,4),_PortVoiceAdminSpeed_Type())
portVoiceAdminSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminSpeed.setStatus(_A)
class _PortVoiceAdminDTMF_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortVoiceAdminDTMF_Type.__name__=_B
_PortVoiceAdminDTMF_Object=MibTableColumn
portVoiceAdminDTMF=_PortVoiceAdminDTMF_Object((1,3,6,1,4,1,173,7,3,8,1,1,5),_PortVoiceAdminDTMF_Type())
portVoiceAdminDTMF.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminDTMF.setStatus(_A)
class _PortVoiceAdminInterface_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,10,11)));namedValues=NamedValues(*(('em-4w',1),('em-2w',2),(_AZ,3),('ac15-a',4),('ac15-b',6),('em-4w-te',10),('em-2w-te',11)))
_PortVoiceAdminInterface_Type.__name__=_B
_PortVoiceAdminInterface_Object=MibTableColumn
portVoiceAdminInterface=_PortVoiceAdminInterface_Object((1,3,6,1,4,1,173,7,3,8,1,1,6),_PortVoiceAdminInterface_Type())
portVoiceAdminInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminInterface.setStatus(_A)
class _PortVoiceAdminTETimer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortVoiceAdminTETimer_Type.__name__=_B
_PortVoiceAdminTETimer_Object=MibTableColumn
portVoiceAdminTETimer=_PortVoiceAdminTETimer_Object((1,3,6,1,4,1,173,7,3,8,1,1,7),_PortVoiceAdminTETimer_Type())
portVoiceAdminTETimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminTETimer.setStatus(_A)
class _PortVoiceAdminLevelIn_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-22,7))
_PortVoiceAdminLevelIn_Type.__name__=_B
_PortVoiceAdminLevelIn_Object=MibTableColumn
portVoiceAdminLevelIn=_PortVoiceAdminLevelIn_Object((1,3,6,1,4,1,173,7,3,8,1,1,8),_PortVoiceAdminLevelIn_Type())
portVoiceAdminLevelIn.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminLevelIn.setStatus(_A)
class _PortVoiceAdminLevelOut_Type(Integer32):defaultValue=-4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-22,7))
_PortVoiceAdminLevelOut_Type.__name__=_B
_PortVoiceAdminLevelOut_Object=MibTableColumn
portVoiceAdminLevelOut=_PortVoiceAdminLevelOut_Object((1,3,6,1,4,1,173,7,3,8,1,1,9),_PortVoiceAdminLevelOut_Type())
portVoiceAdminLevelOut.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminLevelOut.setStatus(_A)
class _PortVoiceAdminCallTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PortVoiceAdminCallTimer_Type.__name__=_B
_PortVoiceAdminCallTimer_Object=MibTableColumn
portVoiceAdminCallTimer=_PortVoiceAdminCallTimer_Object((1,3,6,1,4,1,173,7,3,8,1,1,10),_PortVoiceAdminCallTimer_Type())
portVoiceAdminCallTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminCallTimer.setStatus(_A)
class _PortVoiceAdminHuntGroup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('a',2),('b',3)))
_PortVoiceAdminHuntGroup_Type.__name__=_B
_PortVoiceAdminHuntGroup_Object=MibTableColumn
portVoiceAdminHuntGroup=_PortVoiceAdminHuntGroup_Object((1,3,6,1,4,1,173,7,3,8,1,1,11),_PortVoiceAdminHuntGroup_Type())
portVoiceAdminHuntGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminHuntGroup.setStatus(_A)
class _PortVoiceAdminLongDialPrefix_Type(OctetString):defaultHexValue='2A';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_PortVoiceAdminLongDialPrefix_Type.__name__=_J
_PortVoiceAdminLongDialPrefix_Object=MibTableColumn
portVoiceAdminLongDialPrefix=_PortVoiceAdminLongDialPrefix_Object((1,3,6,1,4,1,173,7,3,8,1,1,12),_PortVoiceAdminLongDialPrefix_Type())
portVoiceAdminLongDialPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminLongDialPrefix.setStatus(_A)
class _PortVoiceAdminSLTTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PortVoiceAdminSLTTimeout_Type.__name__=_B
_PortVoiceAdminSLTTimeout_Object=MibTableColumn
portVoiceAdminSLTTimeout=_PortVoiceAdminSLTTimeout_Object((1,3,6,1,4,1,173,7,3,8,1,1,13),_PortVoiceAdminSLTTimeout_Type())
portVoiceAdminSLTTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminSLTTimeout.setStatus(_A)
class _PortVoiceAdminLinkDownBusy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceAdminLinkDownBusy_Type.__name__=_B
_PortVoiceAdminLinkDownBusy_Object=MibTableColumn
portVoiceAdminLinkDownBusy=_PortVoiceAdminLinkDownBusy_Object((1,3,6,1,4,1,173,7,3,8,1,1,14),_PortVoiceAdminLinkDownBusy_Type())
portVoiceAdminLinkDownBusy.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminLinkDownBusy.setStatus(_A)
class _PortVoiceAdminFaxSupported_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortVoiceAdminFaxSupported_Type.__name__=_B
_PortVoiceAdminFaxSupported_Object=MibTableColumn
portVoiceAdminFaxSupported=_PortVoiceAdminFaxSupported_Object((1,3,6,1,4,1,173,7,3,8,1,1,15),_PortVoiceAdminFaxSupported_Type())
portVoiceAdminFaxSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminFaxSupported.setStatus(_A)
class _PortVoiceAdminTelephonyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('opx',1),('slt',2),('em',3),('ac15',4)))
_PortVoiceAdminTelephonyType_Type.__name__=_B
_PortVoiceAdminTelephonyType_Object=MibTableColumn
portVoiceAdminTelephonyType=_PortVoiceAdminTelephonyType_Object((1,3,6,1,4,1,173,7,3,8,1,1,16),_PortVoiceAdminTelephonyType_Type())
portVoiceAdminTelephonyType.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminTelephonyType.setStatus(_A)
class _PortVoiceAdminJitter_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_PortVoiceAdminJitter_Type.__name__=_B
_PortVoiceAdminJitter_Object=MibTableColumn
portVoiceAdminJitter=_PortVoiceAdminJitter_Object((1,3,6,1,4,1,173,7,3,8,1,1,17),_PortVoiceAdminJitter_Type())
portVoiceAdminJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminJitter.setStatus(_A)
class _PortVoiceAdminSampleDelay_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortVoiceAdminSampleDelay_Type.__name__=_B
_PortVoiceAdminSampleDelay_Object=MibTableColumn
portVoiceAdminSampleDelay=_PortVoiceAdminSampleDelay_Object((1,3,6,1,4,1,173,7,3,8,1,1,18),_PortVoiceAdminSampleDelay_Type())
portVoiceAdminSampleDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminSampleDelay.setStatus(_A)
class _PortVoiceAdminDialTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_PortVoiceAdminDialTimer_Type.__name__=_B
_PortVoiceAdminDialTimer_Object=MibTableColumn
portVoiceAdminDialTimer=_PortVoiceAdminDialTimer_Object((1,3,6,1,4,1,173,7,3,8,1,1,19),_PortVoiceAdminDialTimer_Type())
portVoiceAdminDialTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminDialTimer.setStatus(_A)
class _PortVoiceAdminAutoDial_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceAdminAutoDial_Type.__name__=_B
_PortVoiceAdminAutoDial_Object=MibTableColumn
portVoiceAdminAutoDial=_PortVoiceAdminAutoDial_Object((1,3,6,1,4,1,173,7,3,8,1,1,20),_PortVoiceAdminAutoDial_Type())
portVoiceAdminAutoDial.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminAutoDial.setStatus(_A)
class _PortVoiceAdminSuppression_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('very-low',1),('low',2),('medium',3),('high',4),(_Aa,5)))
_PortVoiceAdminSuppression_Type.__name__=_B
_PortVoiceAdminSuppression_Object=MibTableColumn
portVoiceAdminSuppression=_PortVoiceAdminSuppression_Object((1,3,6,1,4,1,173,7,3,8,1,1,21),_PortVoiceAdminSuppression_Type())
portVoiceAdminSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminSuppression.setStatus(_A)
class _PortVoiceAdminAutoDialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PortVoiceAdminAutoDialNumber_Type.__name__=_J
_PortVoiceAdminAutoDialNumber_Object=MibTableColumn
portVoiceAdminAutoDialNumber=_PortVoiceAdminAutoDialNumber_Object((1,3,6,1,4,1,173,7,3,8,1,1,22),_PortVoiceAdminAutoDialNumber_Type())
portVoiceAdminAutoDialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminAutoDialNumber.setStatus(_A)
class _PortVoiceAdminAutoPoll_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceAdminAutoPoll_Type.__name__=_B
_PortVoiceAdminAutoPoll_Object=MibTableColumn
portVoiceAdminAutoPoll=_PortVoiceAdminAutoPoll_Object((1,3,6,1,4,1,173,7,3,8,1,1,23),_PortVoiceAdminAutoPoll_Type())
portVoiceAdminAutoPoll.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminAutoPoll.setStatus(_A)
class _PortVoiceAdminAutoPollTimer_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_PortVoiceAdminAutoPollTimer_Type.__name__=_B
_PortVoiceAdminAutoPollTimer_Object=MibTableColumn
portVoiceAdminAutoPollTimer=_PortVoiceAdminAutoPollTimer_Object((1,3,6,1,4,1,173,7,3,8,1,1,24),_PortVoiceAdminAutoPollTimer_Type())
portVoiceAdminAutoPollTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminAutoPollTimer.setStatus(_A)
class _PortVoiceAdminExtDigitsSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('map',1),('user',2)))
_PortVoiceAdminExtDigitsSource_Type.__name__=_B
_PortVoiceAdminExtDigitsSource_Object=MibTableColumn
portVoiceAdminExtDigitsSource=_PortVoiceAdminExtDigitsSource_Object((1,3,6,1,4,1,173,7,3,8,1,1,25),_PortVoiceAdminExtDigitsSource_Type())
portVoiceAdminExtDigitsSource.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminExtDigitsSource.setStatus(_A)
class _PortVoiceAdminNumDigitsDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_PortVoiceAdminNumDigitsDelete_Type.__name__=_B
_PortVoiceAdminNumDigitsDelete_Object=MibTableColumn
portVoiceAdminNumDigitsDelete=_PortVoiceAdminNumDigitsDelete_Object((1,3,6,1,4,1,173,7,3,8,1,1,26),_PortVoiceAdminNumDigitsDelete_Type())
portVoiceAdminNumDigitsDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminNumDigitsDelete.setStatus(_A)
class _PortVoiceAdminForwardDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_PortVoiceAdminForwardDelay_Type.__name__=_B
_PortVoiceAdminForwardDelay_Object=MibTableColumn
portVoiceAdminForwardDelay=_PortVoiceAdminForwardDelay_Object((1,3,6,1,4,1,173,7,3,8,1,1,27),_PortVoiceAdminForwardDelay_Type())
portVoiceAdminForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminForwardDelay.setStatus(_A)
class _PortVoiceAdminForwardedType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('pulse',2)))
_PortVoiceAdminForwardedType_Type.__name__=_B
_PortVoiceAdminForwardedType_Object=MibTableColumn
portVoiceAdminForwardedType=_PortVoiceAdminForwardedType_Object((1,3,6,1,4,1,173,7,3,8,1,1,28),_PortVoiceAdminForwardedType_Type())
portVoiceAdminForwardedType.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminForwardedType.setStatus(_A)
class _PortVoiceAdminForwardedDigits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_m,2),('extended',3)))
_PortVoiceAdminForwardedDigits_Type.__name__=_B
_PortVoiceAdminForwardedDigits_Object=MibTableColumn
portVoiceAdminForwardedDigits=_PortVoiceAdminForwardedDigits_Object((1,3,6,1,4,1,173,7,3,8,1,1,29),_PortVoiceAdminForwardedDigits_Type())
portVoiceAdminForwardedDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminForwardedDigits.setStatus(_A)
class _PortVoiceAdminMakeRatio_Type(Integer32):defaultValue=34;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,80))
_PortVoiceAdminMakeRatio_Type.__name__=_B
_PortVoiceAdminMakeRatio_Object=MibTableColumn
portVoiceAdminMakeRatio=_PortVoiceAdminMakeRatio_Object((1,3,6,1,4,1,173,7,3,8,1,1,30),_PortVoiceAdminMakeRatio_Type())
portVoiceAdminMakeRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminMakeRatio.setStatus(_A)
class _PortVoiceAdminBreakRatio_Type(Integer32):defaultValue=66;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,80))
_PortVoiceAdminBreakRatio_Type.__name__=_B
_PortVoiceAdminBreakRatio_Object=MibTableColumn
portVoiceAdminBreakRatio=_PortVoiceAdminBreakRatio_Object((1,3,6,1,4,1,173,7,3,8,1,1,31),_PortVoiceAdminBreakRatio_Type())
portVoiceAdminBreakRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminBreakRatio.setStatus(_A)
class _PortVoiceAdminDTMFOnDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1000))
_PortVoiceAdminDTMFOnDuration_Type.__name__=_B
_PortVoiceAdminDTMFOnDuration_Object=MibTableColumn
portVoiceAdminDTMFOnDuration=_PortVoiceAdminDTMFOnDuration_Object((1,3,6,1,4,1,173,7,3,8,1,1,32),_PortVoiceAdminDTMFOnDuration_Type())
portVoiceAdminDTMFOnDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminDTMFOnDuration.setStatus(_A)
class _PortVoiceAdminDTMFOffDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1000))
_PortVoiceAdminDTMFOffDuration_Type.__name__=_B
_PortVoiceAdminDTMFOffDuration_Object=MibTableColumn
portVoiceAdminDTMFOffDuration=_PortVoiceAdminDTMFOffDuration_Object((1,3,6,1,4,1,173,7,3,8,1,1,33),_PortVoiceAdminDTMFOffDuration_Type())
portVoiceAdminDTMFOffDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminDTMFOffDuration.setStatus(_A)
class _PortVoiceAdminToneType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('mf',2)))
_PortVoiceAdminToneType_Type.__name__=_B
_PortVoiceAdminToneType_Object=MibTableColumn
portVoiceAdminToneType=_PortVoiceAdminToneType_Object((1,3,6,1,4,1,173,7,3,8,1,1,34),_PortVoiceAdminToneType_Type())
portVoiceAdminToneType.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminToneType.setStatus(_A)
_PortVoiceAdminRowStatus_Type=RowStatus
_PortVoiceAdminRowStatus_Object=MibTableColumn
portVoiceAdminRowStatus=_PortVoiceAdminRowStatus_Object((1,3,6,1,4,1,173,7,3,8,1,1,35),_PortVoiceAdminRowStatus_Type())
portVoiceAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:portVoiceAdminRowStatus.setStatus(_A)
_PortVoiceOperTable_Object=MibTable
portVoiceOperTable=_PortVoiceOperTable_Object((1,3,6,1,4,1,173,7,3,8,2))
if mibBuilder.loadTexts:portVoiceOperTable.setStatus(_A)
_PortVoiceOperEntry_Object=MibTableRow
portVoiceOperEntry=_PortVoiceOperEntry_Object((1,3,6,1,4,1,173,7,3,8,2,1))
portVoiceOperEntry.setIndexNames((0,_E,_Ab),(0,_E,_Ac))
if mibBuilder.loadTexts:portVoiceOperEntry.setStatus(_A)
_PortVoiceOperRlpIndex_Type=Integer32
_PortVoiceOperRlpIndex_Object=MibTableColumn
portVoiceOperRlpIndex=_PortVoiceOperRlpIndex_Object((1,3,6,1,4,1,173,7,3,8,2,1,1),_PortVoiceOperRlpIndex_Type())
portVoiceOperRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperRlpIndex.setStatus(_A)
_PortVoiceOperPortIndex_Type=Integer32
_PortVoiceOperPortIndex_Object=MibTableColumn
portVoiceOperPortIndex=_PortVoiceOperPortIndex_Object((1,3,6,1,4,1,173,7,3,8,2,1,2),_PortVoiceOperPortIndex_Type())
portVoiceOperPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperPortIndex.setStatus(_A)
class _PortVoiceOperBlockedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceOperBlockedFlag_Type.__name__=_B
_PortVoiceOperBlockedFlag_Object=MibTableColumn
portVoiceOperBlockedFlag=_PortVoiceOperBlockedFlag_Object((1,3,6,1,4,1,173,7,3,8,2,1,3),_PortVoiceOperBlockedFlag_Type())
portVoiceOperBlockedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperBlockedFlag.setStatus(_A)
class _PortVoiceOperSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4)))
_PortVoiceOperSpeed_Type.__name__=_B
_PortVoiceOperSpeed_Object=MibTableColumn
portVoiceOperSpeed=_PortVoiceOperSpeed_Object((1,3,6,1,4,1,173,7,3,8,2,1,4),_PortVoiceOperSpeed_Type())
portVoiceOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperSpeed.setStatus(_A)
class _PortVoiceOperDTMF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortVoiceOperDTMF_Type.__name__=_B
_PortVoiceOperDTMF_Object=MibTableColumn
portVoiceOperDTMF=_PortVoiceOperDTMF_Object((1,3,6,1,4,1,173,7,3,8,2,1,5),_PortVoiceOperDTMF_Type())
portVoiceOperDTMF.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperDTMF.setStatus(_A)
class _PortVoiceOperInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,10,11)));namedValues=NamedValues(*(('em-4w',1),('em-2w',2),(_AZ,3),('ac15-a',4),('ac15-b',6),('em-4w-te',10),('em-2w-te',11)))
_PortVoiceOperInterface_Type.__name__=_B
_PortVoiceOperInterface_Object=MibTableColumn
portVoiceOperInterface=_PortVoiceOperInterface_Object((1,3,6,1,4,1,173,7,3,8,2,1,6),_PortVoiceOperInterface_Type())
portVoiceOperInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperInterface.setStatus(_A)
class _PortVoiceOperTETimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortVoiceOperTETimer_Type.__name__=_B
_PortVoiceOperTETimer_Object=MibTableColumn
portVoiceOperTETimer=_PortVoiceOperTETimer_Object((1,3,6,1,4,1,173,7,3,8,2,1,7),_PortVoiceOperTETimer_Type())
portVoiceOperTETimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperTETimer.setStatus(_A)
class _PortVoiceOperLevelIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-22,7))
_PortVoiceOperLevelIn_Type.__name__=_B
_PortVoiceOperLevelIn_Object=MibTableColumn
portVoiceOperLevelIn=_PortVoiceOperLevelIn_Object((1,3,6,1,4,1,173,7,3,8,2,1,8),_PortVoiceOperLevelIn_Type())
portVoiceOperLevelIn.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperLevelIn.setStatus(_A)
class _PortVoiceOperLevelOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-22,7))
_PortVoiceOperLevelOut_Type.__name__=_B
_PortVoiceOperLevelOut_Object=MibTableColumn
portVoiceOperLevelOut=_PortVoiceOperLevelOut_Object((1,3,6,1,4,1,173,7,3,8,2,1,9),_PortVoiceOperLevelOut_Type())
portVoiceOperLevelOut.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperLevelOut.setStatus(_A)
class _PortVoiceOperCallTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_PortVoiceOperCallTimer_Type.__name__=_B
_PortVoiceOperCallTimer_Object=MibTableColumn
portVoiceOperCallTimer=_PortVoiceOperCallTimer_Object((1,3,6,1,4,1,173,7,3,8,2,1,10),_PortVoiceOperCallTimer_Type())
portVoiceOperCallTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperCallTimer.setStatus(_A)
class _PortVoiceOperHuntGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('a',2),('b',3)))
_PortVoiceOperHuntGroup_Type.__name__=_B
_PortVoiceOperHuntGroup_Object=MibTableColumn
portVoiceOperHuntGroup=_PortVoiceOperHuntGroup_Object((1,3,6,1,4,1,173,7,3,8,2,1,11),_PortVoiceOperHuntGroup_Type())
portVoiceOperHuntGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperHuntGroup.setStatus(_A)
class _PortVoiceOperLongDialPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_PortVoiceOperLongDialPrefix_Type.__name__=_J
_PortVoiceOperLongDialPrefix_Object=MibTableColumn
portVoiceOperLongDialPrefix=_PortVoiceOperLongDialPrefix_Object((1,3,6,1,4,1,173,7,3,8,2,1,12),_PortVoiceOperLongDialPrefix_Type())
portVoiceOperLongDialPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperLongDialPrefix.setStatus(_A)
class _PortVoiceOperSLTTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PortVoiceOperSLTTimeout_Type.__name__=_B
_PortVoiceOperSLTTimeout_Object=MibTableColumn
portVoiceOperSLTTimeout=_PortVoiceOperSLTTimeout_Object((1,3,6,1,4,1,173,7,3,8,2,1,13),_PortVoiceOperSLTTimeout_Type())
portVoiceOperSLTTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperSLTTimeout.setStatus(_A)
class _PortVoiceOperLinkDownBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceOperLinkDownBusy_Type.__name__=_B
_PortVoiceOperLinkDownBusy_Object=MibTableColumn
portVoiceOperLinkDownBusy=_PortVoiceOperLinkDownBusy_Object((1,3,6,1,4,1,173,7,3,8,2,1,14),_PortVoiceOperLinkDownBusy_Type())
portVoiceOperLinkDownBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperLinkDownBusy.setStatus(_A)
class _PortVoiceOperFaxSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PortVoiceOperFaxSupported_Type.__name__=_B
_PortVoiceOperFaxSupported_Object=MibTableColumn
portVoiceOperFaxSupported=_PortVoiceOperFaxSupported_Object((1,3,6,1,4,1,173,7,3,8,2,1,15),_PortVoiceOperFaxSupported_Type())
portVoiceOperFaxSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperFaxSupported.setStatus(_A)
class _PortVoiceOperTelephonyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('opx',1),('slt',2),('em',3),('ac15',4)))
_PortVoiceOperTelephonyType_Type.__name__=_B
_PortVoiceOperTelephonyType_Object=MibTableColumn
portVoiceOperTelephonyType=_PortVoiceOperTelephonyType_Object((1,3,6,1,4,1,173,7,3,8,2,1,16),_PortVoiceOperTelephonyType_Type())
portVoiceOperTelephonyType.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperTelephonyType.setStatus(_A)
class _PortVoiceOperJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_PortVoiceOperJitter_Type.__name__=_B
_PortVoiceOperJitter_Object=MibTableColumn
portVoiceOperJitter=_PortVoiceOperJitter_Object((1,3,6,1,4,1,173,7,3,8,2,1,17),_PortVoiceOperJitter_Type())
portVoiceOperJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperJitter.setStatus(_A)
class _PortVoiceOperSampleDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortVoiceOperSampleDelay_Type.__name__=_B
_PortVoiceOperSampleDelay_Object=MibTableColumn
portVoiceOperSampleDelay=_PortVoiceOperSampleDelay_Object((1,3,6,1,4,1,173,7,3,8,2,1,18),_PortVoiceOperSampleDelay_Type())
portVoiceOperSampleDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperSampleDelay.setStatus(_A)
class _PortVoiceOperDialTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_PortVoiceOperDialTimer_Type.__name__=_B
_PortVoiceOperDialTimer_Object=MibTableColumn
portVoiceOperDialTimer=_PortVoiceOperDialTimer_Object((1,3,6,1,4,1,173,7,3,8,2,1,19),_PortVoiceOperDialTimer_Type())
portVoiceOperDialTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperDialTimer.setStatus(_A)
class _PortVoiceOperAutoDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceOperAutoDial_Type.__name__=_B
_PortVoiceOperAutoDial_Object=MibTableColumn
portVoiceOperAutoDial=_PortVoiceOperAutoDial_Object((1,3,6,1,4,1,173,7,3,8,2,1,20),_PortVoiceOperAutoDial_Type())
portVoiceOperAutoDial.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperAutoDial.setStatus(_A)
class _PortVoiceOperSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('very-low',1),('low',2),('medium',3),('high',4),(_Aa,5)))
_PortVoiceOperSuppression_Type.__name__=_B
_PortVoiceOperSuppression_Object=MibTableColumn
portVoiceOperSuppression=_PortVoiceOperSuppression_Object((1,3,6,1,4,1,173,7,3,8,2,1,21),_PortVoiceOperSuppression_Type())
portVoiceOperSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperSuppression.setStatus(_A)
class _PortVoiceOperAutoDialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PortVoiceOperAutoDialNumber_Type.__name__=_J
_PortVoiceOperAutoDialNumber_Object=MibTableColumn
portVoiceOperAutoDialNumber=_PortVoiceOperAutoDialNumber_Object((1,3,6,1,4,1,173,7,3,8,2,1,22),_PortVoiceOperAutoDialNumber_Type())
portVoiceOperAutoDialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperAutoDialNumber.setStatus(_A)
class _PortVoiceOperAutoPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_PortVoiceOperAutoPoll_Type.__name__=_B
_PortVoiceOperAutoPoll_Object=MibTableColumn
portVoiceOperAutoPoll=_PortVoiceOperAutoPoll_Object((1,3,6,1,4,1,173,7,3,8,2,1,23),_PortVoiceOperAutoPoll_Type())
portVoiceOperAutoPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperAutoPoll.setStatus(_A)
class _PortVoiceOperAutoPollTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_PortVoiceOperAutoPollTimer_Type.__name__=_B
_PortVoiceOperAutoPollTimer_Object=MibTableColumn
portVoiceOperAutoPollTimer=_PortVoiceOperAutoPollTimer_Object((1,3,6,1,4,1,173,7,3,8,2,1,24),_PortVoiceOperAutoPollTimer_Type())
portVoiceOperAutoPollTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperAutoPollTimer.setStatus(_A)
class _PortVoiceOperExtDigitsSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('map',1),('user',2)))
_PortVoiceOperExtDigitsSource_Type.__name__=_B
_PortVoiceOperExtDigitsSource_Object=MibTableColumn
portVoiceOperExtDigitsSource=_PortVoiceOperExtDigitsSource_Object((1,3,6,1,4,1,173,7,3,8,2,1,25),_PortVoiceOperExtDigitsSource_Type())
portVoiceOperExtDigitsSource.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperExtDigitsSource.setStatus(_A)
class _PortVoiceOperNumDigitsDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_PortVoiceOperNumDigitsDelete_Type.__name__=_B
_PortVoiceOperNumDigitsDelete_Object=MibTableColumn
portVoiceOperNumDigitsDelete=_PortVoiceOperNumDigitsDelete_Object((1,3,6,1,4,1,173,7,3,8,2,1,26),_PortVoiceOperNumDigitsDelete_Type())
portVoiceOperNumDigitsDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperNumDigitsDelete.setStatus(_A)
class _PortVoiceOperForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_PortVoiceOperForwardDelay_Type.__name__=_B
_PortVoiceOperForwardDelay_Object=MibTableColumn
portVoiceOperForwardDelay=_PortVoiceOperForwardDelay_Object((1,3,6,1,4,1,173,7,3,8,2,1,27),_PortVoiceOperForwardDelay_Type())
portVoiceOperForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperForwardDelay.setStatus(_A)
class _PortVoiceOperForwardedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('pulse',2)))
_PortVoiceOperForwardedType_Type.__name__=_B
_PortVoiceOperForwardedType_Object=MibTableColumn
portVoiceOperForwardedType=_PortVoiceOperForwardedType_Object((1,3,6,1,4,1,173,7,3,8,2,1,28),_PortVoiceOperForwardedType_Type())
portVoiceOperForwardedType.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperForwardedType.setStatus(_A)
class _PortVoiceOperForwardedDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_m,2),('extended',3)))
_PortVoiceOperForwardedDigits_Type.__name__=_B
_PortVoiceOperForwardedDigits_Object=MibTableColumn
portVoiceOperForwardedDigits=_PortVoiceOperForwardedDigits_Object((1,3,6,1,4,1,173,7,3,8,2,1,29),_PortVoiceOperForwardedDigits_Type())
portVoiceOperForwardedDigits.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperForwardedDigits.setStatus(_A)
class _PortVoiceOperMakeRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,80))
_PortVoiceOperMakeRatio_Type.__name__=_B
_PortVoiceOperMakeRatio_Object=MibTableColumn
portVoiceOperMakeRatio=_PortVoiceOperMakeRatio_Object((1,3,6,1,4,1,173,7,3,8,2,1,30),_PortVoiceOperMakeRatio_Type())
portVoiceOperMakeRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperMakeRatio.setStatus(_A)
class _PortVoiceOperBreakRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,80))
_PortVoiceOperBreakRatio_Type.__name__=_B
_PortVoiceOperBreakRatio_Object=MibTableColumn
portVoiceOperBreakRatio=_PortVoiceOperBreakRatio_Object((1,3,6,1,4,1,173,7,3,8,2,1,31),_PortVoiceOperBreakRatio_Type())
portVoiceOperBreakRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperBreakRatio.setStatus(_A)
class _PortVoiceOperDTMFOnDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1000))
_PortVoiceOperDTMFOnDuration_Type.__name__=_B
_PortVoiceOperDTMFOnDuration_Object=MibTableColumn
portVoiceOperDTMFOnDuration=_PortVoiceOperDTMFOnDuration_Object((1,3,6,1,4,1,173,7,3,8,2,1,32),_PortVoiceOperDTMFOnDuration_Type())
portVoiceOperDTMFOnDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperDTMFOnDuration.setStatus(_A)
class _PortVoiceOperDTMFOffDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1000))
_PortVoiceOperDTMFOffDuration_Type.__name__=_B
_PortVoiceOperDTMFOffDuration_Object=MibTableColumn
portVoiceOperDTMFOffDuration=_PortVoiceOperDTMFOffDuration_Object((1,3,6,1,4,1,173,7,3,8,2,1,33),_PortVoiceOperDTMFOffDuration_Type())
portVoiceOperDTMFOffDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperDTMFOffDuration.setStatus(_A)
class _PortVoiceOperToneType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('mf',2)))
_PortVoiceOperToneType_Type.__name__=_B
_PortVoiceOperToneType_Object=MibTableColumn
portVoiceOperToneType=_PortVoiceOperToneType_Object((1,3,6,1,4,1,173,7,3,8,2,1,34),_PortVoiceOperToneType_Type())
portVoiceOperToneType.setMaxAccess(_C)
if mibBuilder.loadTexts:portVoiceOperToneType.setStatus(_A)
_NlInterfaces_ObjectIdentity=ObjectIdentity
nlInterfaces=_NlInterfaces_ObjectIdentity((1,3,6,1,4,1,173,7,4))
_NlIfTable_Object=MibTable
nlIfTable=_NlIfTable_Object((1,3,6,1,4,1,173,7,4,1))
if mibBuilder.loadTexts:nlIfTable.setStatus(_A)
_NlIfEntry_Object=MibTableRow
nlIfEntry=_NlIfEntry_Object((1,3,6,1,4,1,173,7,4,1,1))
nlIfEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:nlIfEntry.setStatus(_A)
_NlIfRlp_Type=Integer32
_NlIfRlp_Object=MibTableColumn
nlIfRlp=_NlIfRlp_Object((1,3,6,1,4,1,173,7,4,1,1,1),_NlIfRlp_Type())
nlIfRlp.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfRlp.setStatus(_A)
_NlIfPort_Type=Integer32
_NlIfPort_Object=MibTableColumn
nlIfPort=_NlIfPort_Object((1,3,6,1,4,1,173,7,4,1,1,2),_NlIfPort_Type())
nlIfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfPort.setStatus(_A)
class _NlIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,200,201,202,203,204,205,206,207,208)));namedValues=NamedValues(*((_n,1),('regular1822',2),('hdh1822',3),('ddnX25',4),(_Ad,5),(_Ae,6),(_Af,7),('iso88024TokenBus',8),(_Ag,9),('iso88026Man',10),('starLan',11),('proteon10Mbit',12),('proteon80Mbit',13),('hyperchannel',14),('fddi',15),('lapb',16),(_o,17),('ds1',18),(_U,19),('basicISDN',20),('primaryISDN',21),('propPointToPointSerial',22),('ppp',23),('softwareLoopback',24),('eon',25),('ethernet3Mbit',26),('nsip',27),('slip',28),('ultra',29),('ds3',30),('sip',31),(_p,32),(_N,33),('para',34),('arcnet',35),('arcnetPlus',36),('atm',37),('miox25',38),('sonet',39),('x25ple',40),('iso88022llc',41),('localTalk',42),('smdsDxi',43),('frameRelayService',44),(_O,45),('hssi',46),('hippi',47),('modem',48),('aal5',49),('sonetPath',50),('sonetVT',51),('smdsIcip',52),(_Ah,53),('propMultiplexor',54),('trunk',200),('async',201),('bsci',202),('logicalPort',203),(_P,204),('ip',205),('ipx',206),(_q,207),(_W,208)))
_NlIfType_Type.__name__=_B
_NlIfType_Object=MibTableColumn
nlIfType=_NlIfType_Object((1,3,6,1,4,1,173,7,4,1,1,3),_NlIfType_Type())
nlIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfType.setStatus(_A)
_NlIfIndex_Type=Integer32
_NlIfIndex_Object=MibTableColumn
nlIfIndex=_NlIfIndex_Object((1,3,6,1,4,1,173,7,4,1,1,4),_NlIfIndex_Type())
nlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfIndex.setStatus(_A)
_NlIfTableIndex_Type=Integer32
_NlIfTableIndex_Object=MibTableColumn
nlIfTableIndex=_NlIfTableIndex_Object((1,3,6,1,4,1,173,7,4,1,1,5),_NlIfTableIndex_Type())
nlIfTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfTableIndex.setStatus(_A)
_NlIfTableOid_Type=ObjectIdentifier
_NlIfTableOid_Object=MibTableColumn
nlIfTableOid=_NlIfTableOid_Object((1,3,6,1,4,1,173,7,4,1,1,6),_NlIfTableOid_Type())
nlIfTableOid.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfTableOid.setStatus(_A)
class _NlIfConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,13)));namedValues=NamedValues(*((_L,2),(_N,3),('v25bis-dial',4),(_O,5),(_R,6),(_T,7),(_Q,8),('csudsu',9),(_P,10),(_U,11),(_W,13)))
_NlIfConnectorType_Type.__name__=_B
_NlIfConnectorType_Object=MibTableColumn
nlIfConnectorType=_NlIfConnectorType_Object((1,3,6,1,4,1,173,7,4,1,1,7),_NlIfConnectorType_Type())
nlIfConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfConnectorType.setStatus(_A)
class _NlIfPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('linkUp',1),('restarting',2),(_A1,3),(_K,4),('disconnect',5),(_A0,6),('dialReady',7),('quiesced',8),('failed',9),('hardwareFault',10),(_n,11),('ipl',12),('na',13),('remoteLoopback',14),('blueAlarm',15),('yellowAlarm',16),('redAlarm',17),('onHook',18),('offHook',19),('dialing',20),('activeVoiceCall',21),('onHookPending',22)))
_NlIfPortStatus_Type.__name__=_B
_NlIfPortStatus_Object=MibTableColumn
nlIfPortStatus=_NlIfPortStatus_Object((1,3,6,1,4,1,173,7,4,1,1,8),_NlIfPortStatus_Type())
nlIfPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfPortStatus.setStatus(_A)
_NlIfPhyPort_Type=Integer32
_NlIfPhyPort_Object=MibTableColumn
nlIfPhyPort=_NlIfPhyPort_Object((1,3,6,1,4,1,173,7,4,1,1,9),_NlIfPhyPort_Type())
nlIfPhyPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfPhyPort.setStatus(_A)
_NlIfLlc2Interfaces_ObjectIdentity=ObjectIdentity
nlIfLlc2Interfaces=_NlIfLlc2Interfaces_ObjectIdentity((1,3,6,1,4,1,173,7,4,2))
_NlIfLlc2LANTable_Object=MibTable
nlIfLlc2LANTable=_NlIfLlc2LANTable_Object((1,3,6,1,4,1,173,7,4,2,1))
if mibBuilder.loadTexts:nlIfLlc2LANTable.setStatus(_A)
_NlIfLlc2LANEntry_Object=MibTableRow
nlIfLlc2LANEntry=_NlIfLlc2LANEntry_Object((1,3,6,1,4,1,173,7,4,2,1,1))
nlIfLlc2LANEntry.setIndexNames((0,_E,_Ai),(0,_E,_Aj))
if mibBuilder.loadTexts:nlIfLlc2LANEntry.setStatus(_A)
_NlIfLlc2LANRlp_Type=Integer32
_NlIfLlc2LANRlp_Object=MibTableColumn
nlIfLlc2LANRlp=_NlIfLlc2LANRlp_Object((1,3,6,1,4,1,173,7,4,2,1,1,1),_NlIfLlc2LANRlp_Type())
nlIfLlc2LANRlp.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2LANRlp.setStatus(_A)
_NlIfLlc2LANPort_Type=Integer32
_NlIfLlc2LANPort_Object=MibTableColumn
nlIfLlc2LANPort=_NlIfLlc2LANPort_Object((1,3,6,1,4,1,173,7,4,2,1,1,2),_NlIfLlc2LANPort_Type())
nlIfLlc2LANPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2LANPort.setStatus(_A)
class _NlIfLlc2LANType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_r,1),('token-ring',2)))
_NlIfLlc2LANType_Type.__name__=_B
_NlIfLlc2LANType_Object=MibTableColumn
nlIfLlc2LANType=_NlIfLlc2LANType_Object((1,3,6,1,4,1,173,7,4,2,1,1,3),_NlIfLlc2LANType_Type())
nlIfLlc2LANType.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2LANType.setStatus(_A)
class _NlIfLlc2LANCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NlIfLlc2LANCard_Type.__name__=_B
_NlIfLlc2LANCard_Object=MibTableColumn
nlIfLlc2LANCard=_NlIfLlc2LANCard_Object((1,3,6,1,4,1,173,7,4,2,1,1,4),_NlIfLlc2LANCard_Type())
nlIfLlc2LANCard.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2LANCard.setStatus(_A)
class _NlIfLlc2LANID_Type(Integer32):defaultValue=4095;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NlIfLlc2LANID_Type.__name__=_B
_NlIfLlc2LANID_Object=MibTableColumn
nlIfLlc2LANID=_NlIfLlc2LANID_Object((1,3,6,1,4,1,173,7,4,2,1,1,5),_NlIfLlc2LANID_Type())
nlIfLlc2LANID.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2LANID.setStatus(_A)
class _NlIfLlc2LANInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NlIfLlc2LANInterface_Type.__name__=_B
_NlIfLlc2LANInterface_Object=MibTableColumn
nlIfLlc2LANInterface=_NlIfLlc2LANInterface_Object((1,3,6,1,4,1,173,7,4,2,1,1,6),_NlIfLlc2LANInterface_Type())
nlIfLlc2LANInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2LANInterface.setStatus(_A)
_NlIfLlc2LANRowStatus_Type=RowStatus
_NlIfLlc2LANRowStatus_Object=MibTableColumn
nlIfLlc2LANRowStatus=_NlIfLlc2LANRowStatus_Object((1,3,6,1,4,1,173,7,4,2,1,1,7),_NlIfLlc2LANRowStatus_Type())
nlIfLlc2LANRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2LANRowStatus.setStatus(_A)
class _NlIfLlc2LANPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_NlIfLlc2LANPriority_Type.__name__=_B
_NlIfLlc2LANPriority_Object=MibTableColumn
nlIfLlc2LANPriority=_NlIfLlc2LANPriority_Object((1,3,6,1,4,1,173,7,4,2,1,1,8),_NlIfLlc2LANPriority_Type())
nlIfLlc2LANPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2LANPriority.setStatus(_A)
class _NlIfLlc2LANBlockedPortFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlIfLlc2LANBlockedPortFlag_Type.__name__=_B
_NlIfLlc2LANBlockedPortFlag_Object=MibTableColumn
nlIfLlc2LANBlockedPortFlag=_NlIfLlc2LANBlockedPortFlag_Object((1,3,6,1,4,1,173,7,4,2,1,1,9),_NlIfLlc2LANBlockedPortFlag_Type())
nlIfLlc2LANBlockedPortFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2LANBlockedPortFlag.setStatus(_A)
_NlIfLlc2FrTable_Object=MibTable
nlIfLlc2FrTable=_NlIfLlc2FrTable_Object((1,3,6,1,4,1,173,7,4,2,2))
if mibBuilder.loadTexts:nlIfLlc2FrTable.setStatus(_A)
_NlIfLlc2FrEntry_Object=MibTableRow
nlIfLlc2FrEntry=_NlIfLlc2FrEntry_Object((1,3,6,1,4,1,173,7,4,2,2,1))
nlIfLlc2FrEntry.setIndexNames((0,_E,_Ak),(0,_E,_Al),(0,_E,_Am),(0,_E,_An))
if mibBuilder.loadTexts:nlIfLlc2FrEntry.setStatus(_A)
class _NlIfLlc2FrRlp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlIfLlc2FrRlp_Type.__name__=_B
_NlIfLlc2FrRlp_Object=MibTableColumn
nlIfLlc2FrRlp=_NlIfLlc2FrRlp_Object((1,3,6,1,4,1,173,7,4,2,2,1,1),_NlIfLlc2FrRlp_Type())
nlIfLlc2FrRlp.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2FrRlp.setStatus(_A)
class _NlIfLlc2FrPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_NlIfLlc2FrPort_Type.__name__=_B
_NlIfLlc2FrPort_Object=MibTableColumn
nlIfLlc2FrPort=_NlIfLlc2FrPort_Object((1,3,6,1,4,1,173,7,4,2,2,1,2),_NlIfLlc2FrPort_Type())
nlIfLlc2FrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2FrPort.setStatus(_A)
class _NlIfLlc2FrDLCI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_NlIfLlc2FrDLCI_Type.__name__=_B
_NlIfLlc2FrDLCI_Object=MibTableColumn
nlIfLlc2FrDLCI=_NlIfLlc2FrDLCI_Object((1,3,6,1,4,1,173,7,4,2,2,1,3),_NlIfLlc2FrDLCI_Type())
nlIfLlc2FrDLCI.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2FrDLCI.setStatus(_A)
class _NlIfLlc2FrFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('native-llc2',1),('tb-8023',2),('srb-8025',3)))
_NlIfLlc2FrFormat_Type.__name__=_B
_NlIfLlc2FrFormat_Object=MibTableColumn
nlIfLlc2FrFormat=_NlIfLlc2FrFormat_Object((1,3,6,1,4,1,173,7,4,2,2,1,4),_NlIfLlc2FrFormat_Type())
nlIfLlc2FrFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2FrFormat.setStatus(_A)
class _NlIfLlc2FrPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_NlIfLlc2FrPriority_Type.__name__=_B
_NlIfLlc2FrPriority_Object=MibTableColumn
nlIfLlc2FrPriority=_NlIfLlc2FrPriority_Object((1,3,6,1,4,1,173,7,4,2,2,1,5),_NlIfLlc2FrPriority_Type())
nlIfLlc2FrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrPriority.setStatus(_A)
class _NlIfLlc2FrBAG_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NlIfLlc2FrBAG_Type.__name__=_B
_NlIfLlc2FrBAG_Object=MibTableColumn
nlIfLlc2FrBAG=_NlIfLlc2FrBAG_Object((1,3,6,1,4,1,173,7,4,2,2,1,6),_NlIfLlc2FrBAG_Type())
nlIfLlc2FrBAG.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrBAG.setStatus(_A)
class _NlIfLlc2FrHostMACAddress_Type(MacAddress):defaultHexValue=_Ao
_NlIfLlc2FrHostMACAddress_Type.__name__=_Y
_NlIfLlc2FrHostMACAddress_Object=MibTableColumn
nlIfLlc2FrHostMACAddress=_NlIfLlc2FrHostMACAddress_Object((1,3,6,1,4,1,173,7,4,2,2,1,7),_NlIfLlc2FrHostMACAddress_Type())
nlIfLlc2FrHostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrHostMACAddress.setStatus(_A)
class _NlIfLlc2FrSessionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Ap,1),(_Aq,2),(_h,3)))
_NlIfLlc2FrSessionType_Type.__name__=_B
_NlIfLlc2FrSessionType_Object=MibTableColumn
nlIfLlc2FrSessionType=_NlIfLlc2FrSessionType_Object((1,3,6,1,4,1,173,7,4,2,2,1,8),_NlIfLlc2FrSessionType_Type())
nlIfLlc2FrSessionType.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrSessionType.setStatus(_A)
class _NlIfLlc2FrLANID_Type(Integer32):defaultValue=4095;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NlIfLlc2FrLANID_Type.__name__=_B
_NlIfLlc2FrLANID_Object=MibTableColumn
nlIfLlc2FrLANID=_NlIfLlc2FrLANID_Object((1,3,6,1,4,1,173,7,4,2,2,1,9),_NlIfLlc2FrLANID_Type())
nlIfLlc2FrLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrLANID.setStatus(_A)
_NlIfLlc2FrInterface_Type=Integer32
_NlIfLlc2FrInterface_Object=MibTableColumn
nlIfLlc2FrInterface=_NlIfLlc2FrInterface_Object((1,3,6,1,4,1,173,7,4,2,2,1,10),_NlIfLlc2FrInterface_Type())
nlIfLlc2FrInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfLlc2FrInterface.setStatus(_A)
_NlIfLlc2FrRowStatus_Type=RowStatus
_NlIfLlc2FrRowStatus_Object=MibTableColumn
nlIfLlc2FrRowStatus=_NlIfLlc2FrRowStatus_Object((1,3,6,1,4,1,173,7,4,2,2,1,11),_NlIfLlc2FrRowStatus_Type())
nlIfLlc2FrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrRowStatus.setStatus(_A)
class _NlIfLlc2FrBlockedPortFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlIfLlc2FrBlockedPortFlag_Type.__name__=_B
_NlIfLlc2FrBlockedPortFlag_Object=MibTableColumn
nlIfLlc2FrBlockedPortFlag=_NlIfLlc2FrBlockedPortFlag_Object((1,3,6,1,4,1,173,7,4,2,2,1,12),_NlIfLlc2FrBlockedPortFlag_Type())
nlIfLlc2FrBlockedPortFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfLlc2FrBlockedPortFlag.setStatus(_A)
_IpxConfig_ObjectIdentity=ObjectIdentity
ipxConfig=_IpxConfig_ObjectIdentity((1,3,6,1,4,1,173,7,4,3))
_IpxConfigRouting_ObjectIdentity=ObjectIdentity
ipxConfigRouting=_IpxConfigRouting_ObjectIdentity((1,3,6,1,4,1,173,7,4,3,1))
_IpxStaticRouteConfigTable_Object=MibTable
ipxStaticRouteConfigTable=_IpxStaticRouteConfigTable_Object((1,3,6,1,4,1,173,7,4,3,1,1))
if mibBuilder.loadTexts:ipxStaticRouteConfigTable.setStatus(_A)
_IpxStaticRouteConfigEntry_Object=MibTableRow
ipxStaticRouteConfigEntry=_IpxStaticRouteConfigEntry_Object((1,3,6,1,4,1,173,7,4,3,1,1,1))
ipxStaticRouteConfigEntry.setIndexNames((0,_E,_Ar),(0,_E,_As))
if mibBuilder.loadTexts:ipxStaticRouteConfigEntry.setStatus(_A)
class _IpxStaticRouteConfigCircIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpxStaticRouteConfigCircIndex_Type.__name__=_B
_IpxStaticRouteConfigCircIndex_Object=MibTableColumn
ipxStaticRouteConfigCircIndex=_IpxStaticRouteConfigCircIndex_Object((1,3,6,1,4,1,173,7,4,3,1,1,1,1),_IpxStaticRouteConfigCircIndex_Type())
ipxStaticRouteConfigCircIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteConfigCircIndex.setStatus(_A)
class _IpxStaticRouteConfigNetNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_IpxStaticRouteConfigNetNum_Type.__name__=_J
_IpxStaticRouteConfigNetNum_Object=MibTableColumn
ipxStaticRouteConfigNetNum=_IpxStaticRouteConfigNetNum_Object((1,3,6,1,4,1,173,7,4,3,1,1,1,2),_IpxStaticRouteConfigNetNum_Type())
ipxStaticRouteConfigNetNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxStaticRouteConfigNetNum.setStatus(_A)
class _IpxStaticRouteConfigRouter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxStaticRouteConfigRouter_Type.__name__=_J
_IpxStaticRouteConfigRouter_Object=MibTableColumn
ipxStaticRouteConfigRouter=_IpxStaticRouteConfigRouter_Object((1,3,6,1,4,1,173,7,4,3,1,1,1,3),_IpxStaticRouteConfigRouter_Type())
ipxStaticRouteConfigRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxStaticRouteConfigRouter.setStatus(_A)
_IpxStaticRouteConfigRowStatus_Type=RowStatus
_IpxStaticRouteConfigRowStatus_Object=MibTableColumn
ipxStaticRouteConfigRowStatus=_IpxStaticRouteConfigRowStatus_Object((1,3,6,1,4,1,173,7,4,3,1,1,1,4),_IpxStaticRouteConfigRowStatus_Type())
ipxStaticRouteConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxStaticRouteConfigRowStatus.setStatus(_A)
_IpxServConfigTable_Object=MibTable
ipxServConfigTable=_IpxServConfigTable_Object((1,3,6,1,4,1,173,7,4,3,1,2))
if mibBuilder.loadTexts:ipxServConfigTable.setStatus(_A)
_IpxServConfigEntry_Object=MibTableRow
ipxServConfigEntry=_IpxServConfigEntry_Object((1,3,6,1,4,1,173,7,4,3,1,2,1))
ipxServConfigEntry.setIndexNames((0,_E,_At),(0,_E,_Au))
if mibBuilder.loadTexts:ipxServConfigEntry.setStatus(_A)
class _IpxServConfigServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpxServConfigServiceType_Type.__name__=_B
_IpxServConfigServiceType_Object=MibTableColumn
ipxServConfigServiceType=_IpxServConfigServiceType_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,1),_IpxServConfigServiceType_Type())
ipxServConfigServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxServConfigServiceType.setStatus(_A)
class _IpxServConfigServName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_IpxServConfigServName_Type.__name__=_J
_IpxServConfigServName_Object=MibTableColumn
ipxServConfigServName=_IpxServConfigServName_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,2),_IpxServConfigServName_Type())
ipxServConfigServName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxServConfigServName.setStatus(_A)
class _IpxServConfigServNetworkAddress_Type(Integer32):defaultValue=1
_IpxServConfigServNetworkAddress_Type.__name__=_B
_IpxServConfigServNetworkAddress_Object=MibTableColumn
ipxServConfigServNetworkAddress=_IpxServConfigServNetworkAddress_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,3),_IpxServConfigServNetworkAddress_Type())
ipxServConfigServNetworkAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigServNetworkAddress.setStatus(_A)
class _IpxServConfigServNodeAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxServConfigServNodeAddress_Type.__name__=_J
_IpxServConfigServNodeAddress_Object=MibTableColumn
ipxServConfigServNodeAddress=_IpxServConfigServNodeAddress_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,4),_IpxServConfigServNodeAddress_Type())
ipxServConfigServNodeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigServNodeAddress.setStatus(_A)
class _IpxServConfigServSocketNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpxServConfigServSocketNumber_Type.__name__=_B
_IpxServConfigServSocketNumber_Object=MibTableColumn
ipxServConfigServSocketNumber=_IpxServConfigServSocketNumber_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,5),_IpxServConfigServSocketNumber_Type())
ipxServConfigServSocketNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigServSocketNumber.setStatus(_A)
class _IpxServConfigInterveningNetworks_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpxServConfigInterveningNetworks_Type.__name__=_B
_IpxServConfigInterveningNetworks_Object=MibTableColumn
ipxServConfigInterveningNetworks=_IpxServConfigInterveningNetworks_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,6),_IpxServConfigInterveningNetworks_Type())
ipxServConfigInterveningNetworks.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigInterveningNetworks.setStatus(_A)
class _IpxServConfigGatewayAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_IpxServConfigGatewayAddress_Type.__name__=_J
_IpxServConfigGatewayAddress_Object=MibTableColumn
ipxServConfigGatewayAddress=_IpxServConfigGatewayAddress_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,7),_IpxServConfigGatewayAddress_Type())
ipxServConfigGatewayAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigGatewayAddress.setStatus(_A)
class _IpxServConfigInterface_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpxServConfigInterface_Type.__name__=_B
_IpxServConfigInterface_Object=MibTableColumn
ipxServConfigInterface=_IpxServConfigInterface_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,8),_IpxServConfigInterface_Type())
ipxServConfigInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigInterface.setStatus(_A)
_IpxServConfigRowStatus_Type=RowStatus
_IpxServConfigRowStatus_Object=MibTableColumn
ipxServConfigRowStatus=_IpxServConfigRowStatus_Object((1,3,6,1,4,1,173,7,4,3,1,2,1,9),_IpxServConfigRowStatus_Type())
ipxServConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxServConfigRowStatus.setStatus(_A)
_IpxConfigInterface_ObjectIdentity=ObjectIdentity
ipxConfigInterface=_IpxConfigInterface_ObjectIdentity((1,3,6,1,4,1,173,7,4,3,2))
_IpxInterfaceTable_Object=MibTable
ipxInterfaceTable=_IpxInterfaceTable_Object((1,3,6,1,4,1,173,7,4,3,2,6))
if mibBuilder.loadTexts:ipxInterfaceTable.setStatus(_A)
_IpxInterfaceEntry_Object=MibTableRow
ipxInterfaceEntry=_IpxInterfaceEntry_Object((1,3,6,1,4,1,173,7,4,3,2,6,1))
ipxInterfaceEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:ipxInterfaceEntry.setStatus(_A)
class _IpxInterfaceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_IpxInterfaceNumber_Type.__name__=_B
_IpxInterfaceNumber_Object=MibTableColumn
ipxInterfaceNumber=_IpxInterfaceNumber_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,1),_IpxInterfaceNumber_Type())
ipxInterfaceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipxInterfaceNumber.setStatus(_A)
class _IpxInterfaceBlockedPortFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfaceBlockedPortFlag_Type.__name__=_B
_IpxInterfaceBlockedPortFlag_Object=MibTableColumn
ipxInterfaceBlockedPortFlag=_IpxInterfaceBlockedPortFlag_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,2),_IpxInterfaceBlockedPortFlag_Type())
ipxInterfaceBlockedPortFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceBlockedPortFlag.setStatus(_A)
class _IpxInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),('eight025',2),('x25',3),('frl',4)))
_IpxInterfaceType_Type.__name__=_B
_IpxInterfaceType_Object=MibTableColumn
ipxInterfaceType=_IpxInterfaceType_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,3),_IpxInterfaceType_Type())
ipxInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceType.setStatus(_A)
class _IpxInterfaceFrameType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('typeII',1),('raw',2),('llc',3),('snap',4)))
_IpxInterfaceFrameType_Type.__name__=_B
_IpxInterfaceFrameType_Object=MibTableColumn
ipxInterfaceFrameType=_IpxInterfaceFrameType_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,4),_IpxInterfaceFrameType_Type())
ipxInterfaceFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceFrameType.setStatus(_A)
class _IpxInterfaceMaxTransUnit_Type(Integer32):defaultValue=4096
_IpxInterfaceMaxTransUnit_Type.__name__=_B
_IpxInterfaceMaxTransUnit_Object=MibTableColumn
ipxInterfaceMaxTransUnit=_IpxInterfaceMaxTransUnit_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,5),_IpxInterfaceMaxTransUnit_Type())
ipxInterfaceMaxTransUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceMaxTransUnit.setStatus(_A)
class _IpxInterfaceNetworkAddress_Type(Integer32):defaultValue=0
_IpxInterfaceNetworkAddress_Type.__name__=_B
_IpxInterfaceNetworkAddress_Object=MibTableColumn
ipxInterfaceNetworkAddress=_IpxInterfaceNetworkAddress_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,6),_IpxInterfaceNetworkAddress_Type())
ipxInterfaceNetworkAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceNetworkAddress.setStatus(_A)
class _IpxInterfaceBandwidthAllocGroup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_IpxInterfaceBandwidthAllocGroup_Type.__name__=_B
_IpxInterfaceBandwidthAllocGroup_Object=MibTableColumn
ipxInterfaceBandwidthAllocGroup=_IpxInterfaceBandwidthAllocGroup_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,7),_IpxInterfaceBandwidthAllocGroup_Type())
ipxInterfaceBandwidthAllocGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceBandwidthAllocGroup.setStatus(_A)
class _IpxInterfacePortDiagEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfacePortDiagEnabled_Type.__name__=_B
_IpxInterfacePortDiagEnabled_Object=MibTableColumn
ipxInterfacePortDiagEnabled=_IpxInterfacePortDiagEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,8),_IpxInterfacePortDiagEnabled_Type())
ipxInterfacePortDiagEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfacePortDiagEnabled.setStatus(_A)
class _IpxInterfaceNetBIOSEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfaceNetBIOSEnabled_Type.__name__=_B
_IpxInterfaceNetBIOSEnabled_Object=MibTableColumn
ipxInterfaceNetBIOSEnabled=_IpxInterfaceNetBIOSEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,9),_IpxInterfaceNetBIOSEnabled_Type())
ipxInterfaceNetBIOSEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceNetBIOSEnabled.setStatus(_A)
class _IpxInterfaceNetBIOSHops_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpxInterfaceNetBIOSHops_Type.__name__=_B
_IpxInterfaceNetBIOSHops_Object=MibTableColumn
ipxInterfaceNetBIOSHops=_IpxInterfaceNetBIOSHops_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,10),_IpxInterfaceNetBIOSHops_Type())
ipxInterfaceNetBIOSHops.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceNetBIOSHops.setStatus(_A)
class _IpxInterfacePeriodicRIPEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfacePeriodicRIPEnabled_Type.__name__=_B
_IpxInterfacePeriodicRIPEnabled_Object=MibTableColumn
ipxInterfacePeriodicRIPEnabled=_IpxInterfacePeriodicRIPEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,11),_IpxInterfacePeriodicRIPEnabled_Type())
ipxInterfacePeriodicRIPEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfacePeriodicRIPEnabled.setStatus(_A)
class _IpxInterfacePeriodicRIPTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpxInterfacePeriodicRIPTimer_Type.__name__=_B
_IpxInterfacePeriodicRIPTimer_Object=MibTableColumn
ipxInterfacePeriodicRIPTimer=_IpxInterfacePeriodicRIPTimer_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,12),_IpxInterfacePeriodicRIPTimer_Type())
ipxInterfacePeriodicRIPTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfacePeriodicRIPTimer.setStatus(_A)
class _IpxInterfacePeriodicSAPEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfacePeriodicSAPEnabled_Type.__name__=_B
_IpxInterfacePeriodicSAPEnabled_Object=MibTableColumn
ipxInterfacePeriodicSAPEnabled=_IpxInterfacePeriodicSAPEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,13),_IpxInterfacePeriodicSAPEnabled_Type())
ipxInterfacePeriodicSAPEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfacePeriodicSAPEnabled.setStatus(_A)
class _IpxInterfacePeriodicSAPTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpxInterfacePeriodicSAPTimer_Type.__name__=_B
_IpxInterfacePeriodicSAPTimer_Object=MibTableColumn
ipxInterfacePeriodicSAPTimer=_IpxInterfacePeriodicSAPTimer_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,14),_IpxInterfacePeriodicSAPTimer_Type())
ipxInterfacePeriodicSAPTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfacePeriodicSAPTimer.setStatus(_A)
class _IpxInterfaceRIPEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfaceRIPEnabled_Type.__name__=_B
_IpxInterfaceRIPEnabled_Object=MibTableColumn
ipxInterfaceRIPEnabled=_IpxInterfaceRIPEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,15),_IpxInterfaceRIPEnabled_Type())
ipxInterfaceRIPEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceRIPEnabled.setStatus(_A)
class _IpxInterfaceRIPAgeTimer_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpxInterfaceRIPAgeTimer_Type.__name__=_B
_IpxInterfaceRIPAgeTimer_Object=MibTableColumn
ipxInterfaceRIPAgeTimer=_IpxInterfaceRIPAgeTimer_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,16),_IpxInterfaceRIPAgeTimer_Type())
ipxInterfaceRIPAgeTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceRIPAgeTimer.setStatus(_A)
class _IpxInterfaceRIPMaxSize_Type(Integer32):defaultValue=446;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(54,446))
_IpxInterfaceRIPMaxSize_Type.__name__=_B
_IpxInterfaceRIPMaxSize_Object=MibTableColumn
ipxInterfaceRIPMaxSize=_IpxInterfaceRIPMaxSize_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,17),_IpxInterfaceRIPMaxSize_Type())
ipxInterfaceRIPMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceRIPMaxSize.setStatus(_A)
class _IpxInterfaceSAPEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfaceSAPEnabled_Type.__name__=_B
_IpxInterfaceSAPEnabled_Object=MibTableColumn
ipxInterfaceSAPEnabled=_IpxInterfaceSAPEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,18),_IpxInterfaceSAPEnabled_Type())
ipxInterfaceSAPEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSAPEnabled.setStatus(_A)
class _IpxInterfaceSAPAgeTimer_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpxInterfaceSAPAgeTimer_Type.__name__=_B
_IpxInterfaceSAPAgeTimer_Object=MibTableColumn
ipxInterfaceSAPAgeTimer=_IpxInterfaceSAPAgeTimer_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,19),_IpxInterfaceSAPAgeTimer_Type())
ipxInterfaceSAPAgeTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSAPAgeTimer.setStatus(_A)
class _IpxInterfaceTransportTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpxInterfaceTransportTime_Type.__name__=_B
_IpxInterfaceTransportTime_Object=MibTableColumn
ipxInterfaceTransportTime=_IpxInterfaceTransportTime_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,20),_IpxInterfaceTransportTime_Type())
ipxInterfaceTransportTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceTransportTime.setStatus(_A)
class _IpxInterfaceSerializationEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfaceSerializationEnabled_Type.__name__=_B
_IpxInterfaceSerializationEnabled_Object=MibTableColumn
ipxInterfaceSerializationEnabled=_IpxInterfaceSerializationEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,21),_IpxInterfaceSerializationEnabled_Type())
ipxInterfaceSerializationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSerializationEnabled.setStatus(_A)
class _IpxInterfaceWatchdogSpoofingEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_IpxInterfaceWatchdogSpoofingEnabled_Type.__name__=_B
_IpxInterfaceWatchdogSpoofingEnabled_Object=MibTableColumn
ipxInterfaceWatchdogSpoofingEnabled=_IpxInterfaceWatchdogSpoofingEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,22),_IpxInterfaceWatchdogSpoofingEnabled_Type())
ipxInterfaceWatchdogSpoofingEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceWatchdogSpoofingEnabled.setStatus(_A)
class _IpxInterfaceLanCardNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_IpxInterfaceLanCardNumber_Type.__name__=_B
_IpxInterfaceLanCardNumber_Object=MibTableColumn
ipxInterfaceLanCardNumber=_IpxInterfaceLanCardNumber_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,23),_IpxInterfaceLanCardNumber_Type())
ipxInterfaceLanCardNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceLanCardNumber.setStatus(_A)
class _IpxInterfaceWanEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_h,3)))
_IpxInterfaceWanEnabled_Type.__name__=_B
_IpxInterfaceWanEnabled_Object=MibTableColumn
ipxInterfaceWanEnabled=_IpxInterfaceWanEnabled_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,24),_IpxInterfaceWanEnabled_Type())
ipxInterfaceWanEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceWanEnabled.setStatus(_A)
class _IpxInterfaceSourceSubscriber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IpxInterfaceSourceSubscriber_Type.__name__=_J
_IpxInterfaceSourceSubscriber_Object=MibTableColumn
ipxInterfaceSourceSubscriber=_IpxInterfaceSourceSubscriber_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,25),_IpxInterfaceSourceSubscriber_Type())
ipxInterfaceSourceSubscriber.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSourceSubscriber.setStatus(_A)
class _IpxInterfaceDestinationSubscriber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IpxInterfaceDestinationSubscriber_Type.__name__=_J
_IpxInterfaceDestinationSubscriber_Object=MibTableColumn
ipxInterfaceDestinationSubscriber=_IpxInterfaceDestinationSubscriber_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,26),_IpxInterfaceDestinationSubscriber_Type())
ipxInterfaceDestinationSubscriber.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceDestinationSubscriber.setStatus(_A)
class _IpxInterfaceSVCRetryTimer_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_IpxInterfaceSVCRetryTimer_Type.__name__=_B
_IpxInterfaceSVCRetryTimer_Object=MibTableColumn
ipxInterfaceSVCRetryTimer=_IpxInterfaceSVCRetryTimer_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,27),_IpxInterfaceSVCRetryTimer_Type())
ipxInterfaceSVCRetryTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSVCRetryTimer.setStatus(_A)
class _IpxInterfaceSVCIdleTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_IpxInterfaceSVCIdleTimer_Type.__name__=_B
_IpxInterfaceSVCIdleTimer_Object=MibTableColumn
ipxInterfaceSVCIdleTimer=_IpxInterfaceSVCIdleTimer_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,28),_IpxInterfaceSVCIdleTimer_Type())
ipxInterfaceSVCIdleTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSVCIdleTimer.setStatus(_A)
class _IpxInterfaceMaxVC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IpxInterfaceMaxVC_Type.__name__=_B
_IpxInterfaceMaxVC_Object=MibTableColumn
ipxInterfaceMaxVC=_IpxInterfaceMaxVC_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,29),_IpxInterfaceMaxVC_Type())
ipxInterfaceMaxVC.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceMaxVC.setStatus(_A)
class _IpxInterfacePVCConnection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_h,3)))
_IpxInterfacePVCConnection_Type.__name__=_B
_IpxInterfacePVCConnection_Object=MibTableColumn
ipxInterfacePVCConnection=_IpxInterfacePVCConnection_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,30),_IpxInterfacePVCConnection_Type())
ipxInterfacePVCConnection.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfacePVCConnection.setStatus(_A)
class _IpxInterfaceSourceCard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IpxInterfaceSourceCard_Type.__name__=_B
_IpxInterfaceSourceCard_Object=MibTableColumn
ipxInterfaceSourceCard=_IpxInterfaceSourceCard_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,31),_IpxInterfaceSourceCard_Type())
ipxInterfaceSourceCard.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSourceCard.setStatus(_A)
class _IpxInterfaceSourcePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IpxInterfaceSourcePort_Type.__name__=_B
_IpxInterfaceSourcePort_Object=MibTableColumn
ipxInterfaceSourcePort=_IpxInterfaceSourcePort_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,32),_IpxInterfaceSourcePort_Type())
ipxInterfaceSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSourcePort.setStatus(_A)
class _IpxInterfaceSourceDLCI_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_IpxInterfaceSourceDLCI_Type.__name__=_B
_IpxInterfaceSourceDLCI_Object=MibTableColumn
ipxInterfaceSourceDLCI=_IpxInterfaceSourceDLCI_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,33),_IpxInterfaceSourceDLCI_Type())
ipxInterfaceSourceDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceSourceDLCI.setStatus(_A)
_IpxInterfaceRowStatus_Type=RowStatus
_IpxInterfaceRowStatus_Object=MibTableColumn
ipxInterfaceRowStatus=_IpxInterfaceRowStatus_Object((1,3,6,1,4,1,173,7,4,3,2,6,1,34),_IpxInterfaceRowStatus_Type())
ipxInterfaceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxInterfaceRowStatus.setStatus(_A)
_IpxConfigNodeDefault_ObjectIdentity=ObjectIdentity
ipxConfigNodeDefault=_IpxConfigNodeDefault_ObjectIdentity((1,3,6,1,4,1,173,7,4,3,3))
_IpxNodeDefaultConfigNetworkAddress_Type=Integer32
_IpxNodeDefaultConfigNetworkAddress_Object=MibScalar
ipxNodeDefaultConfigNetworkAddress=_IpxNodeDefaultConfigNetworkAddress_Object((1,3,6,1,4,1,173,7,4,3,3,1),_IpxNodeDefaultConfigNetworkAddress_Type())
ipxNodeDefaultConfigNetworkAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxNodeDefaultConfigNetworkAddress.setStatus(_A)
class _IpxNodeDefaultConfigRIPSAPGap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_IpxNodeDefaultConfigRIPSAPGap_Type.__name__=_B
_IpxNodeDefaultConfigRIPSAPGap_Object=MibScalar
ipxNodeDefaultConfigRIPSAPGap=_IpxNodeDefaultConfigRIPSAPGap_Object((1,3,6,1,4,1,173,7,4,3,3,2),_IpxNodeDefaultConfigRIPSAPGap_Type())
ipxNodeDefaultConfigRIPSAPGap.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxNodeDefaultConfigRIPSAPGap.setStatus(_A)
class _IpxNodeDefaultConfigRouterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_IpxNodeDefaultConfigRouterName_Type.__name__=_J
_IpxNodeDefaultConfigRouterName_Object=MibScalar
ipxNodeDefaultConfigRouterName=_IpxNodeDefaultConfigRouterName_Object((1,3,6,1,4,1,173,7,4,3,3,3),_IpxNodeDefaultConfigRouterName_Type())
ipxNodeDefaultConfigRouterName.setMaxAccess(_D)
if mibBuilder.loadTexts:ipxNodeDefaultConfigRouterName.setStatus(_A)
_NlIfIpInterfaces_ObjectIdentity=ObjectIdentity
nlIfIpInterfaces=_NlIfIpInterfaces_ObjectIdentity((1,3,6,1,4,1,173,7,4,4))
_NlIfIpTable_Object=MibTable
nlIfIpTable=_NlIfIpTable_Object((1,3,6,1,4,1,173,7,4,4,1))
if mibBuilder.loadTexts:nlIfIpTable.setStatus(_A)
_NlIfIpEntry_Object=MibTableRow
nlIfIpEntry=_NlIfIpEntry_Object((1,3,6,1,4,1,173,7,4,4,1,1))
nlIfIpEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:nlIfIpEntry.setStatus(_A)
class _NlIfIpInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,257))
_NlIfIpInterface_Type.__name__=_B
_NlIfIpInterface_Object=MibTableColumn
nlIfIpInterface=_NlIfIpInterface_Object((1,3,6,1,4,1,173,7,4,4,1,1,1),_NlIfIpInterface_Type())
nlIfIpInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfIpInterface.setStatus(_A)
class _NlIfIpMtu_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_NlIfIpMtu_Type.__name__=_B
_NlIfIpMtu_Object=MibTableColumn
nlIfIpMtu=_NlIfIpMtu_Object((1,3,6,1,4,1,173,7,4,4,1,1,2),_NlIfIpMtu_Type())
nlIfIpMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpMtu.setStatus(_A)
class _NlIfIpNetworkMask_Type(IpAddress):defaultHexValue='FF000000'
_NlIfIpNetworkMask_Type.__name__=_S
_NlIfIpNetworkMask_Object=MibTableColumn
nlIfIpNetworkMask=_NlIfIpNetworkMask_Object((1,3,6,1,4,1,173,7,4,4,1,1,3),_NlIfIpNetworkMask_Type())
nlIfIpNetworkMask.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpNetworkMask.setStatus(_A)
class _NlIfIpRouteMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NlIfIpRouteMetric_Type.__name__=_B
_NlIfIpRouteMetric_Object=MibTableColumn
nlIfIpRouteMetric=_NlIfIpRouteMetric_Object((1,3,6,1,4,1,173,7,4,4,1,1,4),_NlIfIpRouteMetric_Type())
nlIfIpRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpRouteMetric.setStatus(_A)
class _NlIfIpICMPAddRoutes_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlIfIpICMPAddRoutes_Type.__name__=_B
_NlIfIpICMPAddRoutes_Object=MibTableColumn
nlIfIpICMPAddRoutes=_NlIfIpICMPAddRoutes_Object((1,3,6,1,4,1,173,7,4,4,1,1,5),_NlIfIpICMPAddRoutes_Type())
nlIfIpICMPAddRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpICMPAddRoutes.setStatus(_A)
class _NlIfIpRIPDeltaUpdates_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_NlIfIpRIPDeltaUpdates_Type.__name__=_B
_NlIfIpRIPDeltaUpdates_Object=MibTableColumn
nlIfIpRIPDeltaUpdates=_NlIfIpRIPDeltaUpdates_Object((1,3,6,1,4,1,173,7,4,4,1,1,6),_NlIfIpRIPDeltaUpdates_Type())
nlIfIpRIPDeltaUpdates.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpRIPDeltaUpdates.setStatus(_A)
class _NlIfIpRIPFullUpdates_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_NlIfIpRIPFullUpdates_Type.__name__=_B
_NlIfIpRIPFullUpdates_Object=MibTableColumn
nlIfIpRIPFullUpdates=_NlIfIpRIPFullUpdates_Object((1,3,6,1,4,1,173,7,4,4,1,1,7),_NlIfIpRIPFullUpdates_Type())
nlIfIpRIPFullUpdates.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpRIPFullUpdates.setStatus(_A)
class _NlIfIpPriority_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_NlIfIpPriority_Type.__name__=_B
_NlIfIpPriority_Object=MibTableColumn
nlIfIpPriority=_NlIfIpPriority_Object((1,3,6,1,4,1,173,7,4,4,1,1,8),_NlIfIpPriority_Type())
nlIfIpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpPriority.setStatus(_A)
class _NlIfIpBAG_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NlIfIpBAG_Type.__name__=_B
_NlIfIpBAG_Object=MibTableColumn
nlIfIpBAG=_NlIfIpBAG_Object((1,3,6,1,4,1,173,7,4,4,1,1,9),_NlIfIpBAG_Type())
nlIfIpBAG.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpBAG.setStatus(_A)
class _NlIfIpType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,6,7,9,32,53)));namedValues=NamedValues(*((_n,1),(_Ad,5),(_Ae,6),(_Af,7),(_Ag,9),(_p,32),(_Ah,53)))
_NlIfIpType_Type.__name__=_B
_NlIfIpType_Object=MibTableColumn
nlIfIpType=_NlIfIpType_Object((1,3,6,1,4,1,173,7,4,4,1,1,10),_NlIfIpType_Type())
nlIfIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpType.setStatus(_A)
class _NlIfIpSourceAddress_Type(IpAddress):defaultHexValue=_V
_NlIfIpSourceAddress_Type.__name__=_S
_NlIfIpSourceAddress_Object=MibTableColumn
nlIfIpSourceAddress=_NlIfIpSourceAddress_Object((1,3,6,1,4,1,173,7,4,4,1,1,11),_NlIfIpSourceAddress_Type())
nlIfIpSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSourceAddress.setStatus(_A)
class _NlIfIpDestAddress_Type(IpAddress):defaultHexValue=_V
_NlIfIpDestAddress_Type.__name__=_S
_NlIfIpDestAddress_Object=MibTableColumn
nlIfIpDestAddress=_NlIfIpDestAddress_Object((1,3,6,1,4,1,173,7,4,4,1,1,12),_NlIfIpDestAddress_Type())
nlIfIpDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpDestAddress.setStatus(_A)
class _NlIfIpBroadcastAddress_Type(IpAddress):defaultHexValue=_V
_NlIfIpBroadcastAddress_Type.__name__=_S
_NlIfIpBroadcastAddress_Object=MibTableColumn
nlIfIpBroadcastAddress=_NlIfIpBroadcastAddress_Object((1,3,6,1,4,1,173,7,4,4,1,1,13),_NlIfIpBroadcastAddress_Type())
nlIfIpBroadcastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpBroadcastAddress.setStatus(_A)
class _NlIfIpLANCard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NlIfIpLANCard_Type.__name__=_B
_NlIfIpLANCard_Object=MibTableColumn
nlIfIpLANCard=_NlIfIpLANCard_Object((1,3,6,1,4,1,173,7,4,4,1,1,14),_NlIfIpLANCard_Type())
nlIfIpLANCard.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpLANCard.setStatus(_A)
_NlIfIpSourceSub_Type=NlSubscriberAddress
_NlIfIpSourceSub_Object=MibTableColumn
nlIfIpSourceSub=_NlIfIpSourceSub_Object((1,3,6,1,4,1,173,7,4,4,1,1,15),_NlIfIpSourceSub_Type())
nlIfIpSourceSub.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSourceSub.setStatus(_A)
_NlIfIpDestSub_Type=NlSubscriberAddress
_NlIfIpDestSub_Object=MibTableColumn
nlIfIpDestSub=_NlIfIpDestSub_Object((1,3,6,1,4,1,173,7,4,4,1,1,16),_NlIfIpDestSub_Type())
nlIfIpDestSub.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpDestSub.setStatus(_A)
class _NlIfIpSVCRetryTimer_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_NlIfIpSVCRetryTimer_Type.__name__=_B
_NlIfIpSVCRetryTimer_Object=MibTableColumn
nlIfIpSVCRetryTimer=_NlIfIpSVCRetryTimer_Object((1,3,6,1,4,1,173,7,4,4,1,1,17),_NlIfIpSVCRetryTimer_Type())
nlIfIpSVCRetryTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSVCRetryTimer.setStatus(_A)
class _NlIfIpSVCIdleTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_NlIfIpSVCIdleTimer_Type.__name__=_B
_NlIfIpSVCIdleTimer_Object=MibTableColumn
nlIfIpSVCIdleTimer=_NlIfIpSVCIdleTimer_Object((1,3,6,1,4,1,173,7,4,4,1,1,18),_NlIfIpSVCIdleTimer_Type())
nlIfIpSVCIdleTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSVCIdleTimer.setStatus(_A)
class _NlIfIpMaxSVC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlIfIpMaxSVC_Type.__name__=_B
_NlIfIpMaxSVC_Object=MibTableColumn
nlIfIpMaxSVC=_NlIfIpMaxSVC_Object((1,3,6,1,4,1,173,7,4,4,1,1,19),_NlIfIpMaxSVC_Type())
nlIfIpMaxSVC.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpMaxSVC.setStatus(_A)
class _NlIfIpPVCConnection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlIfIpPVCConnection_Type.__name__=_B
_NlIfIpPVCConnection_Object=MibTableColumn
nlIfIpPVCConnection=_NlIfIpPVCConnection_Object((1,3,6,1,4,1,173,7,4,4,1,1,20),_NlIfIpPVCConnection_Type())
nlIfIpPVCConnection.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpPVCConnection.setStatus(_A)
class _NlIfIpSourceRlp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlIfIpSourceRlp_Type.__name__=_B
_NlIfIpSourceRlp_Object=MibTableColumn
nlIfIpSourceRlp=_NlIfIpSourceRlp_Object((1,3,6,1,4,1,173,7,4,4,1,1,21),_NlIfIpSourceRlp_Type())
nlIfIpSourceRlp.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSourceRlp.setStatus(_A)
class _NlIfIpSourcePort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlIfIpSourcePort_Type.__name__=_B
_NlIfIpSourcePort_Object=MibTableColumn
nlIfIpSourcePort=_NlIfIpSourcePort_Object((1,3,6,1,4,1,173,7,4,4,1,1,22),_NlIfIpSourcePort_Type())
nlIfIpSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSourcePort.setStatus(_A)
class _NlIfIpSourceDLCI_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_NlIfIpSourceDLCI_Type.__name__=_B
_NlIfIpSourceDLCI_Object=MibTableColumn
nlIfIpSourceDLCI=_NlIfIpSourceDLCI_Object((1,3,6,1,4,1,173,7,4,4,1,1,23),_NlIfIpSourceDLCI_Type())
nlIfIpSourceDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSourceDLCI.setStatus(_A)
class _NlIfIpRIPSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_M,2),(_Aw,3)))
_NlIfIpRIPSupport_Type.__name__=_B
_NlIfIpRIPSupport_Object=MibTableColumn
nlIfIpRIPSupport=_NlIfIpRIPSupport_Object((1,3,6,1,4,1,173,7,4,4,1,1,24),_NlIfIpRIPSupport_Type())
nlIfIpRIPSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpRIPSupport.setStatus(_A)
class _NlIfIpInverseARP_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_NlIfIpInverseARP_Type.__name__=_B
_NlIfIpInverseARP_Object=MibTableColumn
nlIfIpInverseARP=_NlIfIpInverseARP_Object((1,3,6,1,4,1,173,7,4,4,1,1,25),_NlIfIpInverseARP_Type())
nlIfIpInverseARP.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpInverseARP.setStatus(_A)
class _NlIfIpProxyARP_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_M,2)))
_NlIfIpProxyARP_Type.__name__=_B
_NlIfIpProxyARP_Object=MibTableColumn
nlIfIpProxyARP=_NlIfIpProxyARP_Object((1,3,6,1,4,1,173,7,4,4,1,1,26),_NlIfIpProxyARP_Type())
nlIfIpProxyARP.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpProxyARP.setStatus(_A)
class _NlIfIpUnnumberedIf_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlIfIpUnnumberedIf_Type.__name__=_B
_NlIfIpUnnumberedIf_Object=MibTableColumn
nlIfIpUnnumberedIf=_NlIfIpUnnumberedIf_Object((1,3,6,1,4,1,173,7,4,4,1,1,27),_NlIfIpUnnumberedIf_Type())
nlIfIpUnnumberedIf.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpUnnumberedIf.setStatus(_A)
_NlIfIpRowStatus_Type=RowStatus
_NlIfIpRowStatus_Object=MibTableColumn
nlIfIpRowStatus=_NlIfIpRowStatus_Object((1,3,6,1,4,1,173,7,4,4,1,1,28),_NlIfIpRowStatus_Type())
nlIfIpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpRowStatus.setStatus(_A)
_NlIfIpSecondaryAddrTable_Object=MibTable
nlIfIpSecondaryAddrTable=_NlIfIpSecondaryAddrTable_Object((1,3,6,1,4,1,173,7,4,4,2))
if mibBuilder.loadTexts:nlIfIpSecondaryAddrTable.setStatus(_A)
_NlIfIpSecondaryAddrEntry_Object=MibTableRow
nlIfIpSecondaryAddrEntry=_NlIfIpSecondaryAddrEntry_Object((1,3,6,1,4,1,173,7,4,4,2,1))
nlIfIpSecondaryAddrEntry.setIndexNames((0,_E,_s),(0,_E,_Ax))
if mibBuilder.loadTexts:nlIfIpSecondaryAddrEntry.setStatus(_A)
class _NlIfIpSecondaryAddrSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_NlIfIpSecondaryAddrSequence_Type.__name__=_B
_NlIfIpSecondaryAddrSequence_Object=MibTableColumn
nlIfIpSecondaryAddrSequence=_NlIfIpSecondaryAddrSequence_Object((1,3,6,1,4,1,173,7,4,4,2,1,1),_NlIfIpSecondaryAddrSequence_Type())
nlIfIpSecondaryAddrSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrSequence.setStatus(_A)
class _NlIfIpSecondaryAddrNetworkMask_Type(IpAddress):defaultHexValue=_V
_NlIfIpSecondaryAddrNetworkMask_Type.__name__=_S
_NlIfIpSecondaryAddrNetworkMask_Object=MibTableColumn
nlIfIpSecondaryAddrNetworkMask=_NlIfIpSecondaryAddrNetworkMask_Object((1,3,6,1,4,1,173,7,4,4,2,1,2),_NlIfIpSecondaryAddrNetworkMask_Type())
nlIfIpSecondaryAddrNetworkMask.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrNetworkMask.setStatus(_A)
class _NlIfIpSecondaryAddrRouteMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NlIfIpSecondaryAddrRouteMetric_Type.__name__=_B
_NlIfIpSecondaryAddrRouteMetric_Object=MibTableColumn
nlIfIpSecondaryAddrRouteMetric=_NlIfIpSecondaryAddrRouteMetric_Object((1,3,6,1,4,1,173,7,4,4,2,1,3),_NlIfIpSecondaryAddrRouteMetric_Type())
nlIfIpSecondaryAddrRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrRouteMetric.setStatus(_A)
class _NlIfIpSecondaryAddrSourceAddress_Type(IpAddress):defaultHexValue=_V
_NlIfIpSecondaryAddrSourceAddress_Type.__name__=_S
_NlIfIpSecondaryAddrSourceAddress_Object=MibTableColumn
nlIfIpSecondaryAddrSourceAddress=_NlIfIpSecondaryAddrSourceAddress_Object((1,3,6,1,4,1,173,7,4,4,2,1,4),_NlIfIpSecondaryAddrSourceAddress_Type())
nlIfIpSecondaryAddrSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrSourceAddress.setStatus(_A)
class _NlIfIpSecondaryAddrBroadcastAddress_Type(IpAddress):defaultHexValue=_V
_NlIfIpSecondaryAddrBroadcastAddress_Type.__name__=_S
_NlIfIpSecondaryAddrBroadcastAddress_Object=MibTableColumn
nlIfIpSecondaryAddrBroadcastAddress=_NlIfIpSecondaryAddrBroadcastAddress_Object((1,3,6,1,4,1,173,7,4,4,2,1,5),_NlIfIpSecondaryAddrBroadcastAddress_Type())
nlIfIpSecondaryAddrBroadcastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrBroadcastAddress.setStatus(_A)
class _NlIfIpSecondaryAddrRIPSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_M,2),(_Aw,3)))
_NlIfIpSecondaryAddrRIPSupport_Type.__name__=_B
_NlIfIpSecondaryAddrRIPSupport_Object=MibTableColumn
nlIfIpSecondaryAddrRIPSupport=_NlIfIpSecondaryAddrRIPSupport_Object((1,3,6,1,4,1,173,7,4,4,2,1,6),_NlIfIpSecondaryAddrRIPSupport_Type())
nlIfIpSecondaryAddrRIPSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrRIPSupport.setStatus(_A)
_NlIfIpSecondaryAddrRowStatus_Type=RowStatus
_NlIfIpSecondaryAddrRowStatus_Object=MibTableColumn
nlIfIpSecondaryAddrRowStatus=_NlIfIpSecondaryAddrRowStatus_Object((1,3,6,1,4,1,173,7,4,4,2,1,7),_NlIfIpSecondaryAddrRowStatus_Type())
nlIfIpSecondaryAddrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfIpSecondaryAddrRowStatus.setStatus(_A)
_NlIfVoiceInterfaces_ObjectIdentity=ObjectIdentity
nlIfVoiceInterfaces=_NlIfVoiceInterfaces_ObjectIdentity((1,3,6,1,4,1,173,7,4,5))
_NlIfVoiceTable_Object=MibTable
nlIfVoiceTable=_NlIfVoiceTable_Object((1,3,6,1,4,1,173,7,4,5,1))
if mibBuilder.loadTexts:nlIfVoiceTable.setStatus(_A)
_NlIfVoiceEntry_Object=MibTableRow
nlIfVoiceEntry=_NlIfVoiceEntry_Object((1,3,6,1,4,1,173,7,4,5,1,1))
nlIfVoiceEntry.setIndexNames((0,_E,_Ay))
if mibBuilder.loadTexts:nlIfVoiceEntry.setStatus(_A)
class _NlIfVoiceInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,129))
_NlIfVoiceInterface_Type.__name__=_B
_NlIfVoiceInterface_Object=MibTableColumn
nlIfVoiceInterface=_NlIfVoiceInterface_Object((1,3,6,1,4,1,173,7,4,5,1,1,1),_NlIfVoiceInterface_Type())
nlIfVoiceInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:nlIfVoiceInterface.setStatus(_A)
class _NlIfVoicePeerNodeType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('netlink',1),('act',2)))
_NlIfVoicePeerNodeType_Type.__name__=_B
_NlIfVoicePeerNodeType_Object=MibTableColumn
nlIfVoicePeerNodeType=_NlIfVoicePeerNodeType_Object((1,3,6,1,4,1,173,7,4,5,1,1,2),_NlIfVoicePeerNodeType_Type())
nlIfVoicePeerNodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoicePeerNodeType.setStatus(_A)
class _NlIfVoicePeerNodeNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,61))
_NlIfVoicePeerNodeNumber_Type.__name__=_B
_NlIfVoicePeerNodeNumber_Object=MibTableColumn
nlIfVoicePeerNodeNumber=_NlIfVoicePeerNodeNumber_Object((1,3,6,1,4,1,173,7,4,5,1,1,3),_NlIfVoicePeerNodeNumber_Type())
nlIfVoicePeerNodeNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoicePeerNodeNumber.setStatus(_A)
class _NlIfVoicePeerNodePort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,17))
_NlIfVoicePeerNodePort_Type.__name__=_B
_NlIfVoicePeerNodePort_Object=MibTableColumn
nlIfVoicePeerNodePort=_NlIfVoicePeerNodePort_Object((1,3,6,1,4,1,173,7,4,5,1,1,4),_NlIfVoicePeerNodePort_Type())
nlIfVoicePeerNodePort.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoicePeerNodePort.setStatus(_A)
class _NlIfVoiceLocalNodeNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,61))
_NlIfVoiceLocalNodeNumber_Type.__name__=_B
_NlIfVoiceLocalNodeNumber_Object=MibTableColumn
nlIfVoiceLocalNodeNumber=_NlIfVoiceLocalNodeNumber_Object((1,3,6,1,4,1,173,7,4,5,1,1,5),_NlIfVoiceLocalNodeNumber_Type())
nlIfVoiceLocalNodeNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceLocalNodeNumber.setStatus(_A)
class _NlIfVoiceLocalNodePort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,17))
_NlIfVoiceLocalNodePort_Type.__name__=_B
_NlIfVoiceLocalNodePort_Object=MibTableColumn
nlIfVoiceLocalNodePort=_NlIfVoiceLocalNodePort_Object((1,3,6,1,4,1,173,7,4,5,1,1,6),_NlIfVoiceLocalNodePort_Type())
nlIfVoiceLocalNodePort.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceLocalNodePort.setStatus(_A)
class _NlIfVoiceFrameRelayRlp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlIfVoiceFrameRelayRlp_Type.__name__=_B
_NlIfVoiceFrameRelayRlp_Object=MibTableColumn
nlIfVoiceFrameRelayRlp=_NlIfVoiceFrameRelayRlp_Object((1,3,6,1,4,1,173,7,4,5,1,1,7),_NlIfVoiceFrameRelayRlp_Type())
nlIfVoiceFrameRelayRlp.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceFrameRelayRlp.setStatus(_A)
class _NlIfVoiceFrameRelayPort_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlIfVoiceFrameRelayPort_Type.__name__=_B
_NlIfVoiceFrameRelayPort_Object=MibTableColumn
nlIfVoiceFrameRelayPort=_NlIfVoiceFrameRelayPort_Object((1,3,6,1,4,1,173,7,4,5,1,1,8),_NlIfVoiceFrameRelayPort_Type())
nlIfVoiceFrameRelayPort.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceFrameRelayPort.setStatus(_A)
class _NlIfVoiceFrameRelayDLCI_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_NlIfVoiceFrameRelayDLCI_Type.__name__=_B
_NlIfVoiceFrameRelayDLCI_Object=MibTableColumn
nlIfVoiceFrameRelayDLCI=_NlIfVoiceFrameRelayDLCI_Object((1,3,6,1,4,1,173,7,4,5,1,1,9),_NlIfVoiceFrameRelayDLCI_Type())
nlIfVoiceFrameRelayDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceFrameRelayDLCI.setStatus(_A)
class _NlIfVoiceEnableFragment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlIfVoiceEnableFragment_Type.__name__=_B
_NlIfVoiceEnableFragment_Object=MibTableColumn
nlIfVoiceEnableFragment=_NlIfVoiceEnableFragment_Object((1,3,6,1,4,1,173,7,4,5,1,1,10),_NlIfVoiceEnableFragment_Type())
nlIfVoiceEnableFragment.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceEnableFragment.setStatus(_A)
_NlIfVoiceRowStatus_Type=RowStatus
_NlIfVoiceRowStatus_Object=MibTableColumn
nlIfVoiceRowStatus=_NlIfVoiceRowStatus_Object((1,3,6,1,4,1,173,7,4,5,1,1,11),_NlIfVoiceRowStatus_Type())
nlIfVoiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIfVoiceRowStatus.setStatus(_A)
_Subscriber_ObjectIdentity=ObjectIdentity
subscriber=_Subscriber_ObjectIdentity((1,3,6,1,4,1,173,7,5))
_NlLocalSubscriberTable_Object=MibTable
nlLocalSubscriberTable=_NlLocalSubscriberTable_Object((1,3,6,1,4,1,173,7,5,1))
if mibBuilder.loadTexts:nlLocalSubscriberTable.setStatus(_A)
_NlLocalSubscriberEntry_Object=MibTableRow
nlLocalSubscriberEntry=_NlLocalSubscriberEntry_Object((1,3,6,1,4,1,173,7,5,1,1))
nlLocalSubscriberEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:nlLocalSubscriberEntry.setStatus(_A)
_NlLocalSubscriberId_Type=NlSubscriberAddress
_NlLocalSubscriberId_Object=MibTableColumn
nlLocalSubscriberId=_NlLocalSubscriberId_Object((1,3,6,1,4,1,173,7,5,1,1,1),_NlLocalSubscriberId_Type())
nlLocalSubscriberId.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLocalSubscriberId.setStatus(_A)
class _NlLocalSubscriberName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_NlLocalSubscriberName_Type.__name__=_t
_NlLocalSubscriberName_Object=MibTableColumn
nlLocalSubscriberName=_NlLocalSubscriberName_Object((1,3,6,1,4,1,173,7,5,1,1,2),_NlLocalSubscriberName_Type())
nlLocalSubscriberName.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLocalSubscriberName.setStatus(_A)
class _NlLocalSubscriberAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('round-robin',1),('line-failed',2),('line-busy',3),('least-lcn',4)))
_NlLocalSubscriberAlgorithm_Type.__name__=_B
_NlLocalSubscriberAlgorithm_Object=MibTableColumn
nlLocalSubscriberAlgorithm=_NlLocalSubscriberAlgorithm_Object((1,3,6,1,4,1,173,7,5,1,1,3),_NlLocalSubscriberAlgorithm_Type())
nlLocalSubscriberAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberAlgorithm.setStatus(_A)
class _NlLocalSubscriberSystematicRedirect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlLocalSubscriberSystematicRedirect_Type.__name__=_B
_NlLocalSubscriberSystematicRedirect_Object=MibTableColumn
nlLocalSubscriberSystematicRedirect=_NlLocalSubscriberSystematicRedirect_Object((1,3,6,1,4,1,173,7,5,1,1,4),_NlLocalSubscriberSystematicRedirect_Type())
nlLocalSubscriberSystematicRedirect.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberSystematicRedirect.setStatus(_A)
class _NlLocalSubscriberRedirectBusy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlLocalSubscriberRedirectBusy_Type.__name__=_B
_NlLocalSubscriberRedirectBusy_Object=MibTableColumn
nlLocalSubscriberRedirectBusy=_NlLocalSubscriberRedirectBusy_Object((1,3,6,1,4,1,173,7,5,1,1,5),_NlLocalSubscriberRedirectBusy_Type())
nlLocalSubscriberRedirectBusy.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRedirectBusy.setStatus(_A)
class _NlLocalSubscriberRedirectOO_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlLocalSubscriberRedirectOO_Type.__name__=_B
_NlLocalSubscriberRedirectOO_Object=MibTableColumn
nlLocalSubscriberRedirectOO=_NlLocalSubscriberRedirectOO_Object((1,3,6,1,4,1,173,7,5,1,1,6),_NlLocalSubscriberRedirectOO_Type())
nlLocalSubscriberRedirectOO.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRedirectOO.setStatus(_A)
class _NlLocalSubscriberPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_NlLocalSubscriberPriority_Type.__name__=_B
_NlLocalSubscriberPriority_Object=MibTableColumn
nlLocalSubscriberPriority=_NlLocalSubscriberPriority_Object((1,3,6,1,4,1,173,7,5,1,1,7),_NlLocalSubscriberPriority_Type())
nlLocalSubscriberPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberPriority.setStatus(_A)
_NlLocalSubscriberRowStatus_Type=RowStatus
_NlLocalSubscriberRowStatus_Object=MibTableColumn
nlLocalSubscriberRowStatus=_NlLocalSubscriberRowStatus_Object((1,3,6,1,4,1,173,7,5,1,1,8),_NlLocalSubscriberRowStatus_Type())
nlLocalSubscriberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRowStatus.setStatus(_A)
_NlLocalSubscriberRouteTable_Object=MibTable
nlLocalSubscriberRouteTable=_NlLocalSubscriberRouteTable_Object((1,3,6,1,4,1,173,7,5,2))
if mibBuilder.loadTexts:nlLocalSubscriberRouteTable.setStatus(_A)
_NlLocalSubscriberRouteEntry_Object=MibTableRow
nlLocalSubscriberRouteEntry=_NlLocalSubscriberRouteEntry_Object((1,3,6,1,4,1,173,7,5,2,1))
nlLocalSubscriberRouteEntry.setIndexNames((0,_E,_i),(0,_E,_Az))
if mibBuilder.loadTexts:nlLocalSubscriberRouteEntry.setStatus(_A)
class _NlLocalSubscriberRouteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NlLocalSubscriberRouteIndex_Type.__name__=_B
_NlLocalSubscriberRouteIndex_Object=MibTableColumn
nlLocalSubscriberRouteIndex=_NlLocalSubscriberRouteIndex_Object((1,3,6,1,4,1,173,7,5,2,1,1),_NlLocalSubscriberRouteIndex_Type())
nlLocalSubscriberRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLocalSubscriberRouteIndex.setStatus(_A)
class _NlLocalSubscriberRouteConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_NlLocalSubscriberRouteConf_Type.__name__=_B
_NlLocalSubscriberRouteConf_Object=MibTableColumn
nlLocalSubscriberRouteConf=_NlLocalSubscriberRouteConf_Object((1,3,6,1,4,1,173,7,5,2,1,2),_NlLocalSubscriberRouteConf_Type())
nlLocalSubscriberRouteConf.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLocalSubscriberRouteConf.setStatus(_A)
_NlLocalSubscriberRouteLP_Type=Integer32
_NlLocalSubscriberRouteLP_Object=MibTableColumn
nlLocalSubscriberRouteLP=_NlLocalSubscriberRouteLP_Object((1,3,6,1,4,1,173,7,5,2,1,3),_NlLocalSubscriberRouteLP_Type())
nlLocalSubscriberRouteLP.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRouteLP.setStatus(_A)
_NlLocalSubscriberRoutePort_Type=Integer32
_NlLocalSubscriberRoutePort_Object=MibTableColumn
nlLocalSubscriberRoutePort=_NlLocalSubscriberRoutePort_Object((1,3,6,1,4,1,173,7,5,2,1,4),_NlLocalSubscriberRoutePort_Type())
nlLocalSubscriberRoutePort.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRoutePort.setStatus(_A)
_NlLocalSubscriberRouteRowStatus_Type=RowStatus
_NlLocalSubscriberRouteRowStatus_Object=MibTableColumn
nlLocalSubscriberRouteRowStatus=_NlLocalSubscriberRouteRowStatus_Object((1,3,6,1,4,1,173,7,5,2,1,5),_NlLocalSubscriberRouteRowStatus_Type())
nlLocalSubscriberRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRouteRowStatus.setStatus(_A)
_NlLocalSubscriberRedirTable_Object=MibTable
nlLocalSubscriberRedirTable=_NlLocalSubscriberRedirTable_Object((1,3,6,1,4,1,173,7,5,3))
if mibBuilder.loadTexts:nlLocalSubscriberRedirTable.setStatus(_A)
_NlLocalSubscriberRedirEntry_Object=MibTableRow
nlLocalSubscriberRedirEntry=_NlLocalSubscriberRedirEntry_Object((1,3,6,1,4,1,173,7,5,3,1))
nlLocalSubscriberRedirEntry.setIndexNames((0,_E,_i),(0,_E,_A_))
if mibBuilder.loadTexts:nlLocalSubscriberRedirEntry.setStatus(_A)
class _NlLocalSubscriberRedirIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_NlLocalSubscriberRedirIndex_Type.__name__=_B
_NlLocalSubscriberRedirIndex_Object=MibTableColumn
nlLocalSubscriberRedirIndex=_NlLocalSubscriberRedirIndex_Object((1,3,6,1,4,1,173,7,5,3,1,1),_NlLocalSubscriberRedirIndex_Type())
nlLocalSubscriberRedirIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLocalSubscriberRedirIndex.setStatus(_A)
_NlLocalSubscriberRedirAddr_Type=NlSubscriberAddress
_NlLocalSubscriberRedirAddr_Object=MibTableColumn
nlLocalSubscriberRedirAddr=_NlLocalSubscriberRedirAddr_Object((1,3,6,1,4,1,173,7,5,3,1,2),_NlLocalSubscriberRedirAddr_Type())
nlLocalSubscriberRedirAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRedirAddr.setStatus(_A)
_NlLocalSubscriberRedirRowStatus_Type=RowStatus
_NlLocalSubscriberRedirRowStatus_Object=MibTableColumn
nlLocalSubscriberRedirRowStatus=_NlLocalSubscriberRedirRowStatus_Object((1,3,6,1,4,1,173,7,5,3,1,3),_NlLocalSubscriberRedirRowStatus_Type())
nlLocalSubscriberRedirRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLocalSubscriberRedirRowStatus.setStatus(_A)
_Llc2_ObjectIdentity=ObjectIdentity
llc2=_Llc2_ObjectIdentity((1,3,6,1,4,1,173,7,6))
_NlLlc2HostTable_Object=MibTable
nlLlc2HostTable=_NlLlc2HostTable_Object((1,3,6,1,4,1,173,7,6,1))
if mibBuilder.loadTexts:nlLlc2HostTable.setStatus(_A)
_NlLlc2HostEntry_Object=MibTableRow
nlLlc2HostEntry=_NlLlc2HostEntry_Object((1,3,6,1,4,1,173,7,6,1,1))
nlLlc2HostEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:nlLlc2HostEntry.setStatus(_A)
class _NlLlc2HostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,251))
_NlLlc2HostIndex_Type.__name__=_B
_NlLlc2HostIndex_Object=MibTableColumn
nlLlc2HostIndex=_NlLlc2HostIndex_Object((1,3,6,1,4,1,173,7,6,1,1,1),_NlLlc2HostIndex_Type())
nlLlc2HostIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2HostIndex.setStatus(_A)
class _NlLlc2HostMACAddress_Type(MacAddress):defaultHexValue=_Ao
_NlLlc2HostMACAddress_Type.__name__=_Y
_NlLlc2HostMACAddress_Object=MibTableColumn
nlLlc2HostMACAddress=_NlLlc2HostMACAddress_Object((1,3,6,1,4,1,173,7,6,1,1,2),_NlLlc2HostMACAddress_Type())
nlLlc2HostMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostMACAddress.setStatus(_A)
class _NlLlc2HostSessionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Aq,1),(_Ap,2)))
_NlLlc2HostSessionType_Type.__name__=_B
_NlLlc2HostSessionType_Object=MibTableColumn
nlLlc2HostSessionType=_NlLlc2HostSessionType_Object((1,3,6,1,4,1,173,7,6,1,1,3),_NlLlc2HostSessionType_Type())
nlLlc2HostSessionType.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostSessionType.setStatus(_A)
class _NlLlc2HostT1ReplyTimer_Type(TimeInterval):defaultValue=10;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_NlLlc2HostT1ReplyTimer_Type.__name__=_Z
_NlLlc2HostT1ReplyTimer_Object=MibTableColumn
nlLlc2HostT1ReplyTimer=_NlLlc2HostT1ReplyTimer_Object((1,3,6,1,4,1,173,7,6,1,1,4),_NlLlc2HostT1ReplyTimer_Type())
nlLlc2HostT1ReplyTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostT1ReplyTimer.setStatus(_A)
class _NlLlc2HostT2RecvAckTimer_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_NlLlc2HostT2RecvAckTimer_Type.__name__=_Z
_NlLlc2HostT2RecvAckTimer_Object=MibTableColumn
nlLlc2HostT2RecvAckTimer=_NlLlc2HostT2RecvAckTimer_Object((1,3,6,1,4,1,173,7,6,1,1,5),_NlLlc2HostT2RecvAckTimer_Type())
nlLlc2HostT2RecvAckTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostT2RecvAckTimer.setStatus(_A)
class _NlLlc2HostTiInactivityTimer_Type(TimeInterval):defaultValue=30;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_NlLlc2HostTiInactivityTimer_Type.__name__=_Z
_NlLlc2HostTiInactivityTimer_Object=MibTableColumn
nlLlc2HostTiInactivityTimer=_NlLlc2HostTiInactivityTimer_Object((1,3,6,1,4,1,173,7,6,1,1,6),_NlLlc2HostTiInactivityTimer_Type())
nlLlc2HostTiInactivityTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostTiInactivityTimer.setStatus(_A)
class _NlLlc2HostN3NumberLPDUs_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_NlLlc2HostN3NumberLPDUs_Type.__name__=_B
_NlLlc2HostN3NumberLPDUs_Object=MibTableColumn
nlLlc2HostN3NumberLPDUs=_NlLlc2HostN3NumberLPDUs_Object((1,3,6,1,4,1,173,7,6,1,1,7),_NlLlc2HostN3NumberLPDUs_Type())
nlLlc2HostN3NumberLPDUs.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostN3NumberLPDUs.setStatus(_A)
class _NlLlc2HostTwNumberOutstanding_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_NlLlc2HostTwNumberOutstanding_Type.__name__=_B
_NlLlc2HostTwNumberOutstanding_Object=MibTableColumn
nlLlc2HostTwNumberOutstanding=_NlLlc2HostTwNumberOutstanding_Object((1,3,6,1,4,1,173,7,6,1,1,8),_NlLlc2HostTwNumberOutstanding_Type())
nlLlc2HostTwNumberOutstanding.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostTwNumberOutstanding.setStatus(_A)
class _NlLlc2HostN2ExpiredT1LPDUCount_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NlLlc2HostN2ExpiredT1LPDUCount_Type.__name__=_B
_NlLlc2HostN2ExpiredT1LPDUCount_Object=MibTableColumn
nlLlc2HostN2ExpiredT1LPDUCount=_NlLlc2HostN2ExpiredT1LPDUCount_Object((1,3,6,1,4,1,173,7,6,1,1,9),_NlLlc2HostN2ExpiredT1LPDUCount_Type())
nlLlc2HostN2ExpiredT1LPDUCount.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostN2ExpiredT1LPDUCount.setStatus(_A)
class _NlLlc2HostPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_NlLlc2HostPriority_Type.__name__=_B
_NlLlc2HostPriority_Object=MibTableColumn
nlLlc2HostPriority=_NlLlc2HostPriority_Object((1,3,6,1,4,1,173,7,6,1,1,10),_NlLlc2HostPriority_Type())
nlLlc2HostPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostPriority.setStatus(_A)
class _NlLlc2HostBAG_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NlLlc2HostBAG_Type.__name__=_B
_NlLlc2HostBAG_Object=MibTableColumn
nlLlc2HostBAG=_NlLlc2HostBAG_Object((1,3,6,1,4,1,173,7,6,1,1,11),_NlLlc2HostBAG_Type())
nlLlc2HostBAG.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2HostBAG.setStatus(_A)
_NlLlc2HostRoutingSubscriberId_Type=NlSubscriberAddress
_NlLlc2HostRoutingSubscriberId_Object=MibTableColumn
nlLlc2HostRoutingSubscriberId=_NlLlc2HostRoutingSubscriberId_Object((1,3,6,1,4,1,173,7,6,1,1,12),_NlLlc2HostRoutingSubscriberId_Type())
nlLlc2HostRoutingSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostRoutingSubscriberId.setStatus(_A)
class _NlLlc2HostSrcMACAddressMask_Type(MacAddress):defaultHexValue=_AP
_NlLlc2HostSrcMACAddressMask_Type.__name__=_Y
_NlLlc2HostSrcMACAddressMask_Object=MibTableColumn
nlLlc2HostSrcMACAddressMask=_NlLlc2HostSrcMACAddressMask_Object((1,3,6,1,4,1,173,7,6,1,1,13),_NlLlc2HostSrcMACAddressMask_Type())
nlLlc2HostSrcMACAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostSrcMACAddressMask.setStatus(_A)
class _NlLlc2HostAccess_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lan',1),(_p,2),('tokenRing',3),(_r,4),(_m,5),(_h,6)))
_NlLlc2HostAccess_Type.__name__=_B
_NlLlc2HostAccess_Object=MibTableColumn
nlLlc2HostAccess=_NlLlc2HostAccess_Object((1,3,6,1,4,1,173,7,6,1,1,14),_NlLlc2HostAccess_Type())
nlLlc2HostAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2HostAccess.setStatus(_A)
_NlLlc2HostRowStatus_Type=RowStatus
_NlLlc2HostRowStatus_Object=MibTableColumn
nlLlc2HostRowStatus=_NlLlc2HostRowStatus_Object((1,3,6,1,4,1,173,7,6,1,1,15),_NlLlc2HostRowStatus_Type())
nlLlc2HostRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2HostRowStatus.setStatus(_A)
class _NlLlc2HostInterface_Type(Integer32):defaultValue=300
_NlLlc2HostInterface_Type.__name__=_B
_NlLlc2HostInterface_Object=MibTableColumn
nlLlc2HostInterface=_NlLlc2HostInterface_Object((1,3,6,1,4,1,173,7,6,1,1,16),_NlLlc2HostInterface_Type())
nlLlc2HostInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2HostInterface.setStatus(_A)
class _NlLlc2HostGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NlLlc2HostGroup_Type.__name__=_B
_NlLlc2HostGroup_Object=MibTableColumn
nlLlc2HostGroup=_NlLlc2HostGroup_Object((1,3,6,1,4,1,173,7,6,1,1,17),_NlLlc2HostGroup_Type())
nlLlc2HostGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2HostGroup.setStatus(_A)
_NlLlc2TermConnectionTable_Object=MibTable
nlLlc2TermConnectionTable=_NlLlc2TermConnectionTable_Object((1,3,6,1,4,1,173,7,6,2))
if mibBuilder.loadTexts:nlLlc2TermConnectionTable.setStatus(_A)
_NlLlc2TermConnectionEntry_Object=MibTableRow
nlLlc2TermConnectionEntry=_NlLlc2TermConnectionEntry_Object((1,3,6,1,4,1,173,7,6,2,1))
nlLlc2TermConnectionEntry.setIndexNames((0,_E,_j),(0,_E,_k),(0,_E,_B0))
if mibBuilder.loadTexts:nlLlc2TermConnectionEntry.setStatus(_A)
class _NlLlc2TermConnectionSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NlLlc2TermConnectionSequence_Type.__name__=_B
_NlLlc2TermConnectionSequence_Object=MibTableColumn
nlLlc2TermConnectionSequence=_NlLlc2TermConnectionSequence_Object((1,3,6,1,4,1,173,7,6,2,1,1),_NlLlc2TermConnectionSequence_Type())
nlLlc2TermConnectionSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2TermConnectionSequence.setStatus(_A)
class _NlLlc2TermConnectionHSAP_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,254))
_NlLlc2TermConnectionHSAP_Type.__name__=_B
_NlLlc2TermConnectionHSAP_Object=MibTableColumn
nlLlc2TermConnectionHSAP=_NlLlc2TermConnectionHSAP_Object((1,3,6,1,4,1,173,7,6,2,1,2),_NlLlc2TermConnectionHSAP_Type())
nlLlc2TermConnectionHSAP.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2TermConnectionHSAP.setStatus(_A)
_NlLlc2TermConnectionLocalSubscriberId_Type=NlSubscriberAddress
_NlLlc2TermConnectionLocalSubscriberId_Object=MibTableColumn
nlLlc2TermConnectionLocalSubscriberId=_NlLlc2TermConnectionLocalSubscriberId_Object((1,3,6,1,4,1,173,7,6,2,1,3),_NlLlc2TermConnectionLocalSubscriberId_Type())
nlLlc2TermConnectionLocalSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2TermConnectionLocalSubscriberId.setStatus(_A)
_NlLlc2TermConnectionRemoteSubscriberId_Type=NlSubscriberAddress
_NlLlc2TermConnectionRemoteSubscriberId_Object=MibTableColumn
nlLlc2TermConnectionRemoteSubscriberId=_NlLlc2TermConnectionRemoteSubscriberId_Object((1,3,6,1,4,1,173,7,6,2,1,4),_NlLlc2TermConnectionRemoteSubscriberId_Type())
nlLlc2TermConnectionRemoteSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2TermConnectionRemoteSubscriberId.setStatus(_A)
_NlLlc2TermConnectionRowStatus_Type=RowStatus
_NlLlc2TermConnectionRowStatus_Object=MibTableColumn
nlLlc2TermConnectionRowStatus=_NlLlc2TermConnectionRowStatus_Object((1,3,6,1,4,1,173,7,6,2,1,5),_NlLlc2TermConnectionRowStatus_Type())
nlLlc2TermConnectionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2TermConnectionRowStatus.setStatus(_A)
_NlLlc2OrigConnectionTable_Object=MibTable
nlLlc2OrigConnectionTable=_NlLlc2OrigConnectionTable_Object((1,3,6,1,4,1,173,7,6,3))
if mibBuilder.loadTexts:nlLlc2OrigConnectionTable.setStatus(_A)
_NlLlc2OrigConnectionEntry_Object=MibTableRow
nlLlc2OrigConnectionEntry=_NlLlc2OrigConnectionEntry_Object((1,3,6,1,4,1,173,7,6,3,1))
nlLlc2OrigConnectionEntry.setIndexNames((0,_E,_j),(0,_E,_k),(0,_E,_B1))
if mibBuilder.loadTexts:nlLlc2OrigConnectionEntry.setStatus(_A)
class _NlLlc2OrigConnectionSequence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NlLlc2OrigConnectionSequence_Type.__name__=_B
_NlLlc2OrigConnectionSequence_Object=MibTableColumn
nlLlc2OrigConnectionSequence=_NlLlc2OrigConnectionSequence_Object((1,3,6,1,4,1,173,7,6,3,1,1),_NlLlc2OrigConnectionSequence_Type())
nlLlc2OrigConnectionSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2OrigConnectionSequence.setStatus(_A)
class _NlLlc2OrigConnectionHSAP_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,254))
_NlLlc2OrigConnectionHSAP_Type.__name__=_B
_NlLlc2OrigConnectionHSAP_Object=MibTableColumn
nlLlc2OrigConnectionHSAP=_NlLlc2OrigConnectionHSAP_Object((1,3,6,1,4,1,173,7,6,3,1,2),_NlLlc2OrigConnectionHSAP_Type())
nlLlc2OrigConnectionHSAP.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2OrigConnectionHSAP.setStatus(_A)
class _NlLlc2OrigConnectionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_q,2)))
_NlLlc2OrigConnectionType_Type.__name__=_B
_NlLlc2OrigConnectionType_Object=MibTableColumn
nlLlc2OrigConnectionType=_NlLlc2OrigConnectionType_Object((1,3,6,1,4,1,173,7,6,3,1,3),_NlLlc2OrigConnectionType_Type())
nlLlc2OrigConnectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2OrigConnectionType.setStatus(_A)
_NlLlc2OrigConnectionLocalSubscriberId_Type=NlSubscriberAddress
_NlLlc2OrigConnectionLocalSubscriberId_Object=MibTableColumn
nlLlc2OrigConnectionLocalSubscriberId=_NlLlc2OrigConnectionLocalSubscriberId_Object((1,3,6,1,4,1,173,7,6,3,1,4),_NlLlc2OrigConnectionLocalSubscriberId_Type())
nlLlc2OrigConnectionLocalSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2OrigConnectionLocalSubscriberId.setStatus(_A)
_NlLlc2OrigConnectionRemoteSubscriberId_Type=NlSubscriberAddress
_NlLlc2OrigConnectionRemoteSubscriberId_Object=MibTableColumn
nlLlc2OrigConnectionRemoteSubscriberId=_NlLlc2OrigConnectionRemoteSubscriberId_Object((1,3,6,1,4,1,173,7,6,3,1,5),_NlLlc2OrigConnectionRemoteSubscriberId_Type())
nlLlc2OrigConnectionRemoteSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2OrigConnectionRemoteSubscriberId.setStatus(_A)
class _NlLlc2OrigConnectionIDBLK_Type(Integer32):defaultValue=0
_NlLlc2OrigConnectionIDBLK_Type.__name__=_B
_NlLlc2OrigConnectionIDBLK_Object=MibTableColumn
nlLlc2OrigConnectionIDBLK=_NlLlc2OrigConnectionIDBLK_Object((1,3,6,1,4,1,173,7,6,3,1,6),_NlLlc2OrigConnectionIDBLK_Type())
nlLlc2OrigConnectionIDBLK.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2OrigConnectionIDBLK.setStatus(_A)
class _NlLlc2OrigConnectionIDNUM_Type(Integer32):defaultValue=0
_NlLlc2OrigConnectionIDNUM_Type.__name__=_B
_NlLlc2OrigConnectionIDNUM_Object=MibTableColumn
nlLlc2OrigConnectionIDNUM=_NlLlc2OrigConnectionIDNUM_Object((1,3,6,1,4,1,173,7,6,3,1,7),_NlLlc2OrigConnectionIDNUM_Type())
nlLlc2OrigConnectionIDNUM.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2OrigConnectionIDNUM.setStatus(_A)
class _NlLlc2OrigConnectionMAXDATA_Type(Integer32):defaultValue=0
_NlLlc2OrigConnectionMAXDATA_Type.__name__=_B
_NlLlc2OrigConnectionMAXDATA_Object=MibTableColumn
nlLlc2OrigConnectionMAXDATA=_NlLlc2OrigConnectionMAXDATA_Object((1,3,6,1,4,1,173,7,6,3,1,8),_NlLlc2OrigConnectionMAXDATA_Type())
nlLlc2OrigConnectionMAXDATA.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2OrigConnectionMAXDATA.setStatus(_A)
class _NlLlc2OrigConnectionMAXIN_Type(Integer32):defaultValue=0
_NlLlc2OrigConnectionMAXIN_Type.__name__=_B
_NlLlc2OrigConnectionMAXIN_Object=MibTableColumn
nlLlc2OrigConnectionMAXIN=_NlLlc2OrigConnectionMAXIN_Object((1,3,6,1,4,1,173,7,6,3,1,9),_NlLlc2OrigConnectionMAXIN_Type())
nlLlc2OrigConnectionMAXIN.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2OrigConnectionMAXIN.setStatus(_A)
_NlLlc2OrigConnectionRowStatus_Type=RowStatus
_NlLlc2OrigConnectionRowStatus_Object=MibTableColumn
nlLlc2OrigConnectionRowStatus=_NlLlc2OrigConnectionRowStatus_Object((1,3,6,1,4,1,173,7,6,3,1,10),_NlLlc2OrigConnectionRowStatus_Type())
nlLlc2OrigConnectionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nlLlc2OrigConnectionRowStatus.setStatus(_A)
class _NlLlc2NextHostNumber_Type(Integer32):defaultValue=1
_NlLlc2NextHostNumber_Type.__name__=_B
_NlLlc2NextHostNumber_Object=MibScalar
nlLlc2NextHostNumber=_NlLlc2NextHostNumber_Object((1,3,6,1,4,1,173,7,6,4),_NlLlc2NextHostNumber_Type())
nlLlc2NextHostNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nlLlc2NextHostNumber.setStatus(_A)
_Status_ObjectIdentity=ObjectIdentity
status=_Status_ObjectIdentity((1,3,6,1,4,1,173,7,7))
_PinStatusTable_Object=MibTable
pinStatusTable=_PinStatusTable_Object((1,3,6,1,4,1,173,7,7,4))
if mibBuilder.loadTexts:pinStatusTable.setStatus(_A)
_PortPinEntry_Object=MibTableRow
portPinEntry=_PortPinEntry_Object((1,3,6,1,4,1,173,7,7,4,1))
portPinEntry.setIndexNames((0,_E,_B2),(0,_E,_B3))
if mibBuilder.loadTexts:portPinEntry.setStatus(_A)
_PortPinRlp_Type=Integer32
_PortPinRlp_Object=MibTableColumn
portPinRlp=_PortPinRlp_Object((1,3,6,1,4,1,173,7,7,4,1,1),_PortPinRlp_Type())
portPinRlp.setMaxAccess(_C)
if mibBuilder.loadTexts:portPinRlp.setStatus(_A)
_PortPinPort_Type=Integer32
_PortPinPort_Object=MibTableColumn
portPinPort=_PortPinPort_Object((1,3,6,1,4,1,173,7,7,4,1,2),_PortPinPort_Type())
portPinPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portPinPort.setStatus(_A)
_PortPinStatus_Type=OctetString
_PortPinStatus_Object=MibTableColumn
portPinStatus=_PortPinStatus_Object((1,3,6,1,4,1,173,7,7,4,1,3),_PortPinStatus_Type())
portPinStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portPinStatus.setStatus(_A)
_Statistics_ObjectIdentity=ObjectIdentity
statistics=_Statistics_ObjectIdentity((1,3,6,1,4,1,173,7,8))
_StatGroup_ObjectIdentity=ObjectIdentity
statGroup=_StatGroup_ObjectIdentity((1,3,6,1,4,1,173,7,8,1))
_RlpStatsTable_Object=MibTable
rlpStatsTable=_RlpStatsTable_Object((1,3,6,1,4,1,173,7,8,1,2))
if mibBuilder.loadTexts:rlpStatsTable.setStatus(_A)
_RlpStatsEntry_Object=MibTableRow
rlpStatsEntry=_RlpStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,2,1))
rlpStatsEntry.setIndexNames((0,_E,_B4))
if mibBuilder.loadTexts:rlpStatsEntry.setStatus(_A)
_RlpStatsIndex_Type=Integer32
_RlpStatsIndex_Object=MibTableColumn
rlpStatsIndex=_RlpStatsIndex_Object((1,3,6,1,4,1,173,7,8,1,2,1,1),_RlpStatsIndex_Type())
rlpStatsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsIndex.setStatus(_A)
_RlpStatsQMessages_Type=Counter32
_RlpStatsQMessages_Object=MibTableColumn
rlpStatsQMessages=_RlpStatsQMessages_Object((1,3,6,1,4,1,173,7,8,1,2,1,2),_RlpStatsQMessages_Type())
rlpStatsQMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsQMessages.setStatus(_A)
_RlpStatsUsedBuffers_Type=Counter32
_RlpStatsUsedBuffers_Object=MibTableColumn
rlpStatsUsedBuffers=_RlpStatsUsedBuffers_Object((1,3,6,1,4,1,173,7,8,1,2,1,3),_RlpStatsUsedBuffers_Type())
rlpStatsUsedBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsUsedBuffers.setStatus(_A)
_RlpStatsInFrames_Type=Counter32
_RlpStatsInFrames_Object=MibTableColumn
rlpStatsInFrames=_RlpStatsInFrames_Object((1,3,6,1,4,1,173,7,8,1,2,1,4),_RlpStatsInFrames_Type())
rlpStatsInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsInFrames.setStatus(_A)
_RlpStatsOutFrames_Type=Counter32
_RlpStatsOutFrames_Object=MibTableColumn
rlpStatsOutFrames=_RlpStatsOutFrames_Object((1,3,6,1,4,1,173,7,8,1,2,1,5),_RlpStatsOutFrames_Type())
rlpStatsOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsOutFrames.setStatus(_A)
_RlpStatsFrameRejects_Type=Counter32
_RlpStatsFrameRejects_Object=MibTableColumn
rlpStatsFrameRejects=_RlpStatsFrameRejects_Object((1,3,6,1,4,1,173,7,8,1,2,1,6),_RlpStatsFrameRejects_Type())
rlpStatsFrameRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsFrameRejects.setStatus(_A)
_RlpStatsFrameRetransmits_Type=Counter32
_RlpStatsFrameRetransmits_Object=MibTableColumn
rlpStatsFrameRetransmits=_RlpStatsFrameRetransmits_Object((1,3,6,1,4,1,173,7,8,1,2,1,7),_RlpStatsFrameRetransmits_Type())
rlpStatsFrameRetransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpStatsFrameRetransmits.setStatus(_A)
_PortStatsTable_Object=MibTable
portStatsTable=_PortStatsTable_Object((1,3,6,1,4,1,173,7,8,1,3))
if mibBuilder.loadTexts:portStatsTable.setStatus(_A)
_PortStatsEntry_Object=MibTableRow
portStatsEntry=_PortStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,3,1))
portStatsEntry.setIndexNames((0,_E,_B5),(0,_E,_B6))
if mibBuilder.loadTexts:portStatsEntry.setStatus(_A)
_PortStatsRlpIndex_Type=Integer32
_PortStatsRlpIndex_Object=MibTableColumn
portStatsRlpIndex=_PortStatsRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,3,1,1),_PortStatsRlpIndex_Type())
portStatsRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsRlpIndex.setStatus(_A)
_PortStatsIndex_Type=Integer32
_PortStatsIndex_Object=MibTableColumn
portStatsIndex=_PortStatsIndex_Object((1,3,6,1,4,1,173,7,8,1,3,1,2),_PortStatsIndex_Type())
portStatsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsIndex.setStatus(_A)
_PortStatsInFrames_Type=Counter32
_PortStatsInFrames_Object=MibTableColumn
portStatsInFrames=_PortStatsInFrames_Object((1,3,6,1,4,1,173,7,8,1,3,1,3),_PortStatsInFrames_Type())
portStatsInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsInFrames.setStatus(_A)
_PortStatsOutFrames_Type=Counter32
_PortStatsOutFrames_Object=MibTableColumn
portStatsOutFrames=_PortStatsOutFrames_Object((1,3,6,1,4,1,173,7,8,1,3,1,4),_PortStatsOutFrames_Type())
portStatsOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsOutFrames.setStatus(_A)
_PortStatsFrameRetrans_Type=Counter32
_PortStatsFrameRetrans_Object=MibTableColumn
portStatsFrameRetrans=_PortStatsFrameRetrans_Object((1,3,6,1,4,1,173,7,8,1,3,1,5),_PortStatsFrameRetrans_Type())
portStatsFrameRetrans.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsFrameRetrans.setStatus(_A)
_PortStatsFCSErrors_Type=Counter32
_PortStatsFCSErrors_Object=MibTableColumn
portStatsFCSErrors=_PortStatsFCSErrors_Object((1,3,6,1,4,1,173,7,8,1,3,1,6),_PortStatsFCSErrors_Type())
portStatsFCSErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsFCSErrors.setStatus(_A)
_PortStatsLogicalRejects_Type=Counter32
_PortStatsLogicalRejects_Object=MibTableColumn
portStatsLogicalRejects=_PortStatsLogicalRejects_Object((1,3,6,1,4,1,173,7,8,1,3,1,7),_PortStatsLogicalRejects_Type())
portStatsLogicalRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsLogicalRejects.setStatus(_A)
_PortStatsInPercentUtils_Type=Counter32
_PortStatsInPercentUtils_Object=MibTableColumn
portStatsInPercentUtils=_PortStatsInPercentUtils_Object((1,3,6,1,4,1,173,7,8,1,3,1,8),_PortStatsInPercentUtils_Type())
portStatsInPercentUtils.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsInPercentUtils.setStatus(_A)
_PortStatsOutPercentUtils_Type=Counter32
_PortStatsOutPercentUtils_Object=MibTableColumn
portStatsOutPercentUtils=_PortStatsOutPercentUtils_Object((1,3,6,1,4,1,173,7,8,1,3,1,9),_PortStatsOutPercentUtils_Type())
portStatsOutPercentUtils.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatsOutPercentUtils.setStatus(_A)
_StatFrame_ObjectIdentity=ObjectIdentity
statFrame=_StatFrame_ObjectIdentity((1,3,6,1,4,1,173,7,8,1,4))
_FrStatsTable_Object=MibTable
frStatsTable=_FrStatsTable_Object((1,3,6,1,4,1,173,7,8,1,4,1))
if mibBuilder.loadTexts:frStatsTable.setStatus(_A)
_FrStatsEntry_Object=MibTableRow
frStatsEntry=_FrStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,4,1,1))
frStatsEntry.setIndexNames((0,_E,_B7),(0,_E,_B8))
if mibBuilder.loadTexts:frStatsEntry.setStatus(_A)
_FrStatsRlpIndex_Type=Integer32
_FrStatsRlpIndex_Object=MibTableColumn
frStatsRlpIndex=_FrStatsRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,1),_FrStatsRlpIndex_Type())
frStatsRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsRlpIndex.setStatus(_A)
_FrStatsPortIndex_Type=Integer32
_FrStatsPortIndex_Object=MibTableColumn
frStatsPortIndex=_FrStatsPortIndex_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,2),_FrStatsPortIndex_Type())
frStatsPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsPortIndex.setStatus(_A)
_FrStatsTxDEFrames_Type=Counter32
_FrStatsTxDEFrames_Object=MibTableColumn
frStatsTxDEFrames=_FrStatsTxDEFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,3),_FrStatsTxDEFrames_Type())
frStatsTxDEFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsTxDEFrames.setStatus(_A)
_FrStatsRxDEFrames_Type=Counter32
_FrStatsRxDEFrames_Object=MibTableColumn
frStatsRxDEFrames=_FrStatsRxDEFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,4),_FrStatsRxDEFrames_Type())
frStatsRxDEFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsRxDEFrames.setStatus(_A)
_FrStatsTxFECNFrames_Type=Counter32
_FrStatsTxFECNFrames_Object=MibTableColumn
frStatsTxFECNFrames=_FrStatsTxFECNFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,5),_FrStatsTxFECNFrames_Type())
frStatsTxFECNFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsTxFECNFrames.setStatus(_A)
_FrStatsRxFECNFrames_Type=Counter32
_FrStatsRxFECNFrames_Object=MibTableColumn
frStatsRxFECNFrames=_FrStatsRxFECNFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,6),_FrStatsRxFECNFrames_Type())
frStatsRxFECNFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsRxFECNFrames.setStatus(_A)
_FrStatsTxBECNFrames_Type=Counter32
_FrStatsTxBECNFrames_Object=MibTableColumn
frStatsTxBECNFrames=_FrStatsTxBECNFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,7),_FrStatsTxBECNFrames_Type())
frStatsTxBECNFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsTxBECNFrames.setStatus(_A)
_FrStatsRxBECNFrames_Type=Counter32
_FrStatsRxBECNFrames_Object=MibTableColumn
frStatsRxBECNFrames=_FrStatsRxBECNFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,8),_FrStatsRxBECNFrames_Type())
frStatsRxBECNFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsRxBECNFrames.setStatus(_A)
_FrStatsTxLMIFrames_Type=Counter32
_FrStatsTxLMIFrames_Object=MibTableColumn
frStatsTxLMIFrames=_FrStatsTxLMIFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,9),_FrStatsTxLMIFrames_Type())
frStatsTxLMIFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsTxLMIFrames.setStatus(_A)
_FrStatsRxLMIFrames_Type=Counter32
_FrStatsRxLMIFrames_Object=MibTableColumn
frStatsRxLMIFrames=_FrStatsRxLMIFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,10),_FrStatsRxLMIFrames_Type())
frStatsRxLMIFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsRxLMIFrames.setStatus(_A)
_FrStatsTxANXDFrames_Type=Counter32
_FrStatsTxANXDFrames_Object=MibTableColumn
frStatsTxANXDFrames=_FrStatsTxANXDFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,11),_FrStatsTxANXDFrames_Type())
frStatsTxANXDFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsTxANXDFrames.setStatus(_A)
_FrStatsRxANXDFrames_Type=Counter32
_FrStatsRxANXDFrames_Object=MibTableColumn
frStatsRxANXDFrames=_FrStatsRxANXDFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,12),_FrStatsRxANXDFrames_Type())
frStatsRxANXDFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsRxANXDFrames.setStatus(_A)
_FrStatsTotDiscFrames_Type=Counter32
_FrStatsTotDiscFrames_Object=MibTableColumn
frStatsTotDiscFrames=_FrStatsTotDiscFrames_Object((1,3,6,1,4,1,173,7,8,1,4,1,1,13),_FrStatsTotDiscFrames_Type())
frStatsTotDiscFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:frStatsTotDiscFrames.setStatus(_A)
_X25TxStatsTable_Object=MibTable
x25TxStatsTable=_X25TxStatsTable_Object((1,3,6,1,4,1,173,7,8,1,4,2))
if mibBuilder.loadTexts:x25TxStatsTable.setStatus(_A)
_X25TxStatsEntry_Object=MibTableRow
x25TxStatsEntry=_X25TxStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,4,2,1))
x25TxStatsEntry.setIndexNames((0,_E,_B9),(0,_E,_BA))
if mibBuilder.loadTexts:x25TxStatsEntry.setStatus(_A)
_X25TxRlpIndex_Type=Integer32
_X25TxRlpIndex_Object=MibTableColumn
x25TxRlpIndex=_X25TxRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,1),_X25TxRlpIndex_Type())
x25TxRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxRlpIndex.setStatus(_A)
_X25TxPortIndex_Type=Integer32
_X25TxPortIndex_Object=MibTableColumn
x25TxPortIndex=_X25TxPortIndex_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,2),_X25TxPortIndex_Type())
x25TxPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxPortIndex.setStatus(_A)
_X25TxSABMFrames_Type=Counter32
_X25TxSABMFrames_Object=MibTableColumn
x25TxSABMFrames=_X25TxSABMFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,3),_X25TxSABMFrames_Type())
x25TxSABMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxSABMFrames.setStatus(_A)
_X25TxUAFrames_Type=Counter32
_X25TxUAFrames_Object=MibTableColumn
x25TxUAFrames=_X25TxUAFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,4),_X25TxUAFrames_Type())
x25TxUAFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxUAFrames.setStatus(_A)
_X25TxDISCFrames_Type=Counter32
_X25TxDISCFrames_Object=MibTableColumn
x25TxDISCFrames=_X25TxDISCFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,5),_X25TxDISCFrames_Type())
x25TxDISCFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxDISCFrames.setStatus(_A)
_X25TxDMFrames_Type=Counter32
_X25TxDMFrames_Object=MibTableColumn
x25TxDMFrames=_X25TxDMFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,6),_X25TxDMFrames_Type())
x25TxDMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxDMFrames.setStatus(_A)
_X25TxFRMRFrames_Type=Counter32
_X25TxFRMRFrames_Object=MibTableColumn
x25TxFRMRFrames=_X25TxFRMRFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,7),_X25TxFRMRFrames_Type())
x25TxFRMRFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxFRMRFrames.setStatus(_A)
_X25TxREJFrames_Type=Counter32
_X25TxREJFrames_Object=MibTableColumn
x25TxREJFrames=_X25TxREJFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,8),_X25TxREJFrames_Type())
x25TxREJFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxREJFrames.setStatus(_A)
_X25TxRRFrames_Type=Counter32
_X25TxRRFrames_Object=MibTableColumn
x25TxRRFrames=_X25TxRRFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,9),_X25TxRRFrames_Type())
x25TxRRFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxRRFrames.setStatus(_A)
_X25TxRNRFrames_Type=Counter32
_X25TxRNRFrames_Object=MibTableColumn
x25TxRNRFrames=_X25TxRNRFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,10),_X25TxRNRFrames_Type())
x25TxRNRFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxRNRFrames.setStatus(_A)
_X25TxINFOFrames_Type=Counter32
_X25TxINFOFrames_Object=MibTableColumn
x25TxINFOFrames=_X25TxINFOFrames_Object((1,3,6,1,4,1,173,7,8,1,4,2,1,11),_X25TxINFOFrames_Type())
x25TxINFOFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25TxINFOFrames.setStatus(_A)
_X25RxStatsTable_Object=MibTable
x25RxStatsTable=_X25RxStatsTable_Object((1,3,6,1,4,1,173,7,8,1,4,3))
if mibBuilder.loadTexts:x25RxStatsTable.setStatus(_A)
_X25RxStatsEntry_Object=MibTableRow
x25RxStatsEntry=_X25RxStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,4,3,1))
x25RxStatsEntry.setIndexNames((0,_E,_BB),(0,_E,_BC))
if mibBuilder.loadTexts:x25RxStatsEntry.setStatus(_A)
_X25RxRlpIndex_Type=Integer32
_X25RxRlpIndex_Object=MibTableColumn
x25RxRlpIndex=_X25RxRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,1),_X25RxRlpIndex_Type())
x25RxRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxRlpIndex.setStatus(_A)
_X25RxPortIndex_Type=Integer32
_X25RxPortIndex_Object=MibTableColumn
x25RxPortIndex=_X25RxPortIndex_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,2),_X25RxPortIndex_Type())
x25RxPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxPortIndex.setStatus(_A)
_X25RxSABMFrames_Type=Counter32
_X25RxSABMFrames_Object=MibTableColumn
x25RxSABMFrames=_X25RxSABMFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,3),_X25RxSABMFrames_Type())
x25RxSABMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxSABMFrames.setStatus(_A)
_X25RxUAFrames_Type=Counter32
_X25RxUAFrames_Object=MibTableColumn
x25RxUAFrames=_X25RxUAFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,4),_X25RxUAFrames_Type())
x25RxUAFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxUAFrames.setStatus(_A)
_X25RxDISCFrames_Type=Counter32
_X25RxDISCFrames_Object=MibTableColumn
x25RxDISCFrames=_X25RxDISCFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,5),_X25RxDISCFrames_Type())
x25RxDISCFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxDISCFrames.setStatus(_A)
_X25RxDMFrames_Type=Counter32
_X25RxDMFrames_Object=MibTableColumn
x25RxDMFrames=_X25RxDMFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,6),_X25RxDMFrames_Type())
x25RxDMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxDMFrames.setStatus(_A)
_X25RxFRMRFrames_Type=Counter32
_X25RxFRMRFrames_Object=MibTableColumn
x25RxFRMRFrames=_X25RxFRMRFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,7),_X25RxFRMRFrames_Type())
x25RxFRMRFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxFRMRFrames.setStatus(_A)
_X25RxREJFrames_Type=Counter32
_X25RxREJFrames_Object=MibTableColumn
x25RxREJFrames=_X25RxREJFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,8),_X25RxREJFrames_Type())
x25RxREJFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxREJFrames.setStatus(_A)
_X25RxRRFrames_Type=Counter32
_X25RxRRFrames_Object=MibTableColumn
x25RxRRFrames=_X25RxRRFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,9),_X25RxRRFrames_Type())
x25RxRRFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxRRFrames.setStatus(_A)
_X25RxRNRFrames_Type=Counter32
_X25RxRNRFrames_Object=MibTableColumn
x25RxRNRFrames=_X25RxRNRFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,10),_X25RxRNRFrames_Type())
x25RxRNRFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxRNRFrames.setStatus(_A)
_X25RxINFOFrames_Type=Counter32
_X25RxINFOFrames_Object=MibTableColumn
x25RxINFOFrames=_X25RxINFOFrames_Object((1,3,6,1,4,1,173,7,8,1,4,3,1,11),_X25RxINFOFrames_Type())
x25RxINFOFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:x25RxINFOFrames.setStatus(_A)
_StatBag_ObjectIdentity=ObjectIdentity
statBag=_StatBag_ObjectIdentity((1,3,6,1,4,1,173,7,8,1,5))
_StatIp_ObjectIdentity=ObjectIdentity
statIp=_StatIp_ObjectIdentity((1,3,6,1,4,1,173,7,8,1,6))
_StatT1_ObjectIdentity=ObjectIdentity
statT1=_StatT1_ObjectIdentity((1,3,6,1,4,1,173,7,8,1,7))
_T1StatsTable_Object=MibTable
t1StatsTable=_T1StatsTable_Object((1,3,6,1,4,1,173,7,8,1,7,1))
if mibBuilder.loadTexts:t1StatsTable.setStatus(_A)
_T1StatsEntry_Object=MibTableRow
t1StatsEntry=_T1StatsEntry_Object((1,3,6,1,4,1,173,7,8,1,7,1,1))
t1StatsEntry.setIndexNames((0,_E,_BD),(0,_E,_BE))
if mibBuilder.loadTexts:t1StatsEntry.setStatus(_A)
_T1StatsRlpIndex_Type=Integer32
_T1StatsRlpIndex_Object=MibTableColumn
t1StatsRlpIndex=_T1StatsRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,1),_T1StatsRlpIndex_Type())
t1StatsRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRlpIndex.setStatus(_A)
_T1StatsPortIndex_Type=Integer32
_T1StatsPortIndex_Object=MibTableColumn
t1StatsPortIndex=_T1StatsPortIndex_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,2),_T1StatsPortIndex_Type())
t1StatsPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsPortIndex.setStatus(_A)
_T1StatsRcvFrames_Type=Counter32
_T1StatsRcvFrames_Object=MibTableColumn
t1StatsRcvFrames=_T1StatsRcvFrames_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,3),_T1StatsRcvFrames_Type())
t1StatsRcvFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRcvFrames.setStatus(_A)
_T1StatsXmitFrames_Type=Counter32
_T1StatsXmitFrames_Object=MibTableColumn
t1StatsXmitFrames=_T1StatsXmitFrames_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,4),_T1StatsXmitFrames_Type())
t1StatsXmitFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsXmitFrames.setStatus(_A)
_T1StatsLCVCnt_Type=Counter32
_T1StatsLCVCnt_Object=MibTableColumn
t1StatsLCVCnt=_T1StatsLCVCnt_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,5),_T1StatsLCVCnt_Type())
t1StatsLCVCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsLCVCnt.setStatus(_A)
_T1StatsPCVRErrs_Type=Counter32
_T1StatsPCVRErrs_Object=MibTableColumn
t1StatsPCVRErrs=_T1StatsPCVRErrs_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,6),_T1StatsPCVRErrs_Type())
t1StatsPCVRErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsPCVRErrs.setStatus(_A)
_T1StatsOOSCnt_Type=Counter32
_T1StatsOOSCnt_Object=MibTableColumn
t1StatsOOSCnt=_T1StatsOOSCnt_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,7),_T1StatsOOSCnt_Type())
t1StatsOOSCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsOOSCnt.setStatus(_A)
_T1StatsBlueAlarms_Type=Counter32
_T1StatsBlueAlarms_Object=MibTableColumn
t1StatsBlueAlarms=_T1StatsBlueAlarms_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,8),_T1StatsBlueAlarms_Type())
t1StatsBlueAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsBlueAlarms.setStatus(_A)
_T1StatsYellowAlarms_Type=Counter32
_T1StatsYellowAlarms_Object=MibTableColumn
t1StatsYellowAlarms=_T1StatsYellowAlarms_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,9),_T1StatsYellowAlarms_Type())
t1StatsYellowAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsYellowAlarms.setStatus(_A)
_T1StatsRedAlarms_Type=Counter32
_T1StatsRedAlarms_Object=MibTableColumn
t1StatsRedAlarms=_T1StatsRedAlarms_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,10),_T1StatsRedAlarms_Type())
t1StatsRedAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRedAlarms.setStatus(_A)
_T1StatsRcvUsage_Type=Counter32
_T1StatsRcvUsage_Object=MibTableColumn
t1StatsRcvUsage=_T1StatsRcvUsage_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,11),_T1StatsRcvUsage_Type())
t1StatsRcvUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRcvUsage.setStatus(_A)
_T1StatsXmitUsage_Type=Counter32
_T1StatsXmitUsage_Object=MibTableColumn
t1StatsXmitUsage=_T1StatsXmitUsage_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,12),_T1StatsXmitUsage_Type())
t1StatsXmitUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsXmitUsage.setStatus(_A)
_T1StatsXmitAbortFrames_Type=Counter32
_T1StatsXmitAbortFrames_Object=MibTableColumn
t1StatsXmitAbortFrames=_T1StatsXmitAbortFrames_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,13),_T1StatsXmitAbortFrames_Type())
t1StatsXmitAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsXmitAbortFrames.setStatus(_A)
_T1StatsRcvAbortFrames_Type=Counter32
_T1StatsRcvAbortFrames_Object=MibTableColumn
t1StatsRcvAbortFrames=_T1StatsRcvAbortFrames_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,14),_T1StatsRcvAbortFrames_Type())
t1StatsRcvAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRcvAbortFrames.setStatus(_A)
_T1StatsRcvOverruns_Type=Counter32
_T1StatsRcvOverruns_Object=MibTableColumn
t1StatsRcvOverruns=_T1StatsRcvOverruns_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,15),_T1StatsRcvOverruns_Type())
t1StatsRcvOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRcvOverruns.setStatus(_A)
_T1StatsRcvErrors_Type=Counter32
_T1StatsRcvErrors_Object=MibTableColumn
t1StatsRcvErrors=_T1StatsRcvErrors_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,16),_T1StatsRcvErrors_Type())
t1StatsRcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRcvErrors.setStatus(_A)
_T1StatsRcvChannelErrors_Type=Counter32
_T1StatsRcvChannelErrors_Object=MibTableColumn
t1StatsRcvChannelErrors=_T1StatsRcvChannelErrors_Object((1,3,6,1,4,1,173,7,8,1,7,1,1,17),_T1StatsRcvChannelErrors_Type())
t1StatsRcvChannelErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:t1StatsRcvChannelErrors.setStatus(_A)
_StatDS0A_ObjectIdentity=ObjectIdentity
statDS0A=_StatDS0A_ObjectIdentity((1,3,6,1,4,1,173,7,8,1,8))
_Ds0aStatsTable_Object=MibTable
ds0aStatsTable=_Ds0aStatsTable_Object((1,3,6,1,4,1,173,7,8,1,8,1))
if mibBuilder.loadTexts:ds0aStatsTable.setStatus(_A)
_Ds0aStatsEntry_Object=MibTableRow
ds0aStatsEntry=_Ds0aStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,8,1,1))
ds0aStatsEntry.setIndexNames((0,_E,_BF),(0,_E,_BG),(0,_E,_BH))
if mibBuilder.loadTexts:ds0aStatsEntry.setStatus(_A)
_Ds0aStatsRlpIndex_Type=Integer32
_Ds0aStatsRlpIndex_Object=MibTableColumn
ds0aStatsRlpIndex=_Ds0aStatsRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,1),_Ds0aStatsRlpIndex_Type())
ds0aStatsRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsRlpIndex.setStatus(_A)
_Ds0aStatsPortIndex_Type=Integer32
_Ds0aStatsPortIndex_Object=MibTableColumn
ds0aStatsPortIndex=_Ds0aStatsPortIndex_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,2),_Ds0aStatsPortIndex_Type())
ds0aStatsPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsPortIndex.setStatus(_A)
_Ds0aStatsChannelIndex_Type=Integer32
_Ds0aStatsChannelIndex_Object=MibTableColumn
ds0aStatsChannelIndex=_Ds0aStatsChannelIndex_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,3),_Ds0aStatsChannelIndex_Type())
ds0aStatsChannelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsChannelIndex.setStatus(_A)
_Ds0aStatsXmitFrames_Type=Counter32
_Ds0aStatsXmitFrames_Object=MibTableColumn
ds0aStatsXmitFrames=_Ds0aStatsXmitFrames_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,4),_Ds0aStatsXmitFrames_Type())
ds0aStatsXmitFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsXmitFrames.setStatus(_A)
_Ds0aStatsRcvFrames_Type=Counter32
_Ds0aStatsRcvFrames_Object=MibTableColumn
ds0aStatsRcvFrames=_Ds0aStatsRcvFrames_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,5),_Ds0aStatsRcvFrames_Type())
ds0aStatsRcvFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsRcvFrames.setStatus(_A)
_Ds0aStatsRcvAbortFrames_Type=Counter32
_Ds0aStatsRcvAbortFrames_Object=MibTableColumn
ds0aStatsRcvAbortFrames=_Ds0aStatsRcvAbortFrames_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,6),_Ds0aStatsRcvAbortFrames_Type())
ds0aStatsRcvAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsRcvAbortFrames.setStatus(_A)
_Ds0aStatsRcvOverruns_Type=Counter32
_Ds0aStatsRcvOverruns_Object=MibTableColumn
ds0aStatsRcvOverruns=_Ds0aStatsRcvOverruns_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,7),_Ds0aStatsRcvOverruns_Type())
ds0aStatsRcvOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsRcvOverruns.setStatus(_A)
_Ds0aStatsRcvErrors_Type=Counter32
_Ds0aStatsRcvErrors_Object=MibTableColumn
ds0aStatsRcvErrors=_Ds0aStatsRcvErrors_Object((1,3,6,1,4,1,173,7,8,1,8,1,1,8),_Ds0aStatsRcvErrors_Type())
ds0aStatsRcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ds0aStatsRcvErrors.setStatus(_A)
_StatVoice_ObjectIdentity=ObjectIdentity
statVoice=_StatVoice_ObjectIdentity((1,3,6,1,4,1,173,7,8,1,9))
_VoiceStatsTable_Object=MibTable
voiceStatsTable=_VoiceStatsTable_Object((1,3,6,1,4,1,173,7,8,1,9,1))
if mibBuilder.loadTexts:voiceStatsTable.setStatus(_A)
_VoiceStatsEntry_Object=MibTableRow
voiceStatsEntry=_VoiceStatsEntry_Object((1,3,6,1,4,1,173,7,8,1,9,1,1))
voiceStatsEntry.setIndexNames((0,_E,_BI),(0,_E,_BJ))
if mibBuilder.loadTexts:voiceStatsEntry.setStatus(_A)
_VoiceStatsRlpIndex_Type=Integer32
_VoiceStatsRlpIndex_Object=MibTableColumn
voiceStatsRlpIndex=_VoiceStatsRlpIndex_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,1),_VoiceStatsRlpIndex_Type())
voiceStatsRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsRlpIndex.setStatus(_A)
_VoiceStatsPortIndex_Type=Integer32
_VoiceStatsPortIndex_Object=MibTableColumn
voiceStatsPortIndex=_VoiceStatsPortIndex_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,2),_VoiceStatsPortIndex_Type())
voiceStatsPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsPortIndex.setStatus(_A)
_VoiceStatsRxCalls_Type=Counter32
_VoiceStatsRxCalls_Object=MibTableColumn
voiceStatsRxCalls=_VoiceStatsRxCalls_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,3),_VoiceStatsRxCalls_Type())
voiceStatsRxCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsRxCalls.setStatus(_A)
_VoiceStatsTxCalls_Type=Counter32
_VoiceStatsTxCalls_Object=MibTableColumn
voiceStatsTxCalls=_VoiceStatsTxCalls_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,4),_VoiceStatsTxCalls_Type())
voiceStatsTxCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsTxCalls.setStatus(_A)
_VoiceStatsRxCallsAccepts_Type=Counter32
_VoiceStatsRxCallsAccepts_Object=MibTableColumn
voiceStatsRxCallsAccepts=_VoiceStatsRxCallsAccepts_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,5),_VoiceStatsRxCallsAccepts_Type())
voiceStatsRxCallsAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsRxCallsAccepts.setStatus(_A)
_VoiceStatsTxCallsAccepts_Type=Counter32
_VoiceStatsTxCallsAccepts_Object=MibTableColumn
voiceStatsTxCallsAccepts=_VoiceStatsTxCallsAccepts_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,6),_VoiceStatsTxCallsAccepts_Type())
voiceStatsTxCallsAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsTxCallsAccepts.setStatus(_A)
_VoiceStatsRxClears_Type=Counter32
_VoiceStatsRxClears_Object=MibTableColumn
voiceStatsRxClears=_VoiceStatsRxClears_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,7),_VoiceStatsRxClears_Type())
voiceStatsRxClears.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsRxClears.setStatus(_A)
_VoiceStatsTxClears_Type=Counter32
_VoiceStatsTxClears_Object=MibTableColumn
voiceStatsTxClears=_VoiceStatsTxClears_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,8),_VoiceStatsTxClears_Type())
voiceStatsTxClears.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsTxClears.setStatus(_A)
_VoiceStatsBusyCalls_Type=Counter32
_VoiceStatsBusyCalls_Object=MibTableColumn
voiceStatsBusyCalls=_VoiceStatsBusyCalls_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,9),_VoiceStatsBusyCalls_Type())
voiceStatsBusyCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsBusyCalls.setStatus(_A)
_VoiceStatsCallTimeouts_Type=Counter32
_VoiceStatsCallTimeouts_Object=MibTableColumn
voiceStatsCallTimeouts=_VoiceStatsCallTimeouts_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,10),_VoiceStatsCallTimeouts_Type())
voiceStatsCallTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsCallTimeouts.setStatus(_A)
_VoiceStatsRxCongestions_Type=Counter32
_VoiceStatsRxCongestions_Object=MibTableColumn
voiceStatsRxCongestions=_VoiceStatsRxCongestions_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,11),_VoiceStatsRxCongestions_Type())
voiceStatsRxCongestions.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsRxCongestions.setStatus(_A)
_VoiceStatsTxCongestions_Type=Counter32
_VoiceStatsTxCongestions_Object=MibTableColumn
voiceStatsTxCongestions=_VoiceStatsTxCongestions_Object((1,3,6,1,4,1,173,7,8,1,9,1,1,12),_VoiceStatsTxCongestions_Type())
voiceStatsTxCongestions.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceStatsTxCongestions.setStatus(_A)
_StatThresh_ObjectIdentity=ObjectIdentity
statThresh=_StatThresh_ObjectIdentity((1,3,6,1,4,1,173,7,8,2))
_RlpThreshTable_Object=MibTable
rlpThreshTable=_RlpThreshTable_Object((1,3,6,1,4,1,173,7,8,2,1))
if mibBuilder.loadTexts:rlpThreshTable.setStatus(_A)
_RlpThreshEntry_Object=MibTableRow
rlpThreshEntry=_RlpThreshEntry_Object((1,3,6,1,4,1,173,7,8,2,1,1))
rlpThreshEntry.setIndexNames((0,_E,_BK))
if mibBuilder.loadTexts:rlpThreshEntry.setStatus(_A)
_RlpThreshRlpIndex_Type=Integer32
_RlpThreshRlpIndex_Object=MibTableColumn
rlpThreshRlpIndex=_RlpThreshRlpIndex_Object((1,3,6,1,4,1,173,7,8,2,1,1,1),_RlpThreshRlpIndex_Type())
rlpThreshRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshRlpIndex.setStatus(_A)
_RlpThreshPercntBufInUse_Type=Integer32
_RlpThreshPercntBufInUse_Object=MibTableColumn
rlpThreshPercntBufInUse=_RlpThreshPercntBufInUse_Object((1,3,6,1,4,1,173,7,8,2,1,1,2),_RlpThreshPercntBufInUse_Type())
rlpThreshPercntBufInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshPercntBufInUse.setStatus(_A)
_RlpThreshMsgQueueLen_Type=Integer32
_RlpThreshMsgQueueLen_Object=MibTableColumn
rlpThreshMsgQueueLen=_RlpThreshMsgQueueLen_Object((1,3,6,1,4,1,173,7,8,2,1,1,3),_RlpThreshMsgQueueLen_Type())
rlpThreshMsgQueueLen.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshMsgQueueLen.setStatus(_A)
_RlpThreshRxFramesPerSec_Type=Integer32
_RlpThreshRxFramesPerSec_Object=MibTableColumn
rlpThreshRxFramesPerSec=_RlpThreshRxFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,1,1,4),_RlpThreshRxFramesPerSec_Type())
rlpThreshRxFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshRxFramesPerSec.setStatus(_A)
_RlpThreshTxFramesPerSec_Type=Integer32
_RlpThreshTxFramesPerSec_Object=MibTableColumn
rlpThreshTxFramesPerSec=_RlpThreshTxFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,1,1,5),_RlpThreshTxFramesPerSec_Type())
rlpThreshTxFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshTxFramesPerSec.setStatus(_A)
_RlpThreshRejFramesPerSec_Type=Integer32
_RlpThreshRejFramesPerSec_Object=MibTableColumn
rlpThreshRejFramesPerSec=_RlpThreshRejFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,1,1,6),_RlpThreshRejFramesPerSec_Type())
rlpThreshRejFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshRejFramesPerSec.setStatus(_A)
_RlpThreshRtxFramesPerSec_Type=Integer32
_RlpThreshRtxFramesPerSec_Object=MibTableColumn
rlpThreshRtxFramesPerSec=_RlpThreshRtxFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,1,1,7),_RlpThreshRtxFramesPerSec_Type())
rlpThreshRtxFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:rlpThreshRtxFramesPerSec.setStatus(_A)
_PortThreshTable_Object=MibTable
portThreshTable=_PortThreshTable_Object((1,3,6,1,4,1,173,7,8,2,2))
if mibBuilder.loadTexts:portThreshTable.setStatus(_A)
_PortThreshEntry_Object=MibTableRow
portThreshEntry=_PortThreshEntry_Object((1,3,6,1,4,1,173,7,8,2,2,1))
portThreshEntry.setIndexNames((0,_E,_BL),(0,_E,_BM))
if mibBuilder.loadTexts:portThreshEntry.setStatus(_A)
_PortThreshRlpIndex_Type=Integer32
_PortThreshRlpIndex_Object=MibTableColumn
portThreshRlpIndex=_PortThreshRlpIndex_Object((1,3,6,1,4,1,173,7,8,2,2,1,1),_PortThreshRlpIndex_Type())
portThreshRlpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshRlpIndex.setStatus(_A)
_PortThreshIndex_Type=Integer32
_PortThreshIndex_Object=MibTableColumn
portThreshIndex=_PortThreshIndex_Object((1,3,6,1,4,1,173,7,8,2,2,1,2),_PortThreshIndex_Type())
portThreshIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshIndex.setStatus(_A)
_PortThreshRxFramesPerSec_Type=Integer32
_PortThreshRxFramesPerSec_Object=MibTableColumn
portThreshRxFramesPerSec=_PortThreshRxFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,2,1,3),_PortThreshRxFramesPerSec_Type())
portThreshRxFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshRxFramesPerSec.setStatus(_A)
_PortThreshTxFramesPerSec_Type=Integer32
_PortThreshTxFramesPerSec_Object=MibTableColumn
portThreshTxFramesPerSec=_PortThreshTxFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,2,1,4),_PortThreshTxFramesPerSec_Type())
portThreshTxFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshTxFramesPerSec.setStatus(_A)
_PortThreshRtxFramesPerSec_Type=Integer32
_PortThreshRtxFramesPerSec_Object=MibTableColumn
portThreshRtxFramesPerSec=_PortThreshRtxFramesPerSec_Object((1,3,6,1,4,1,173,7,8,2,2,1,5),_PortThreshRtxFramesPerSec_Type())
portThreshRtxFramesPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshRtxFramesPerSec.setStatus(_A)
_PortThreshFCSErrPerSec_Type=Integer32
_PortThreshFCSErrPerSec_Object=MibTableColumn
portThreshFCSErrPerSec=_PortThreshFCSErrPerSec_Object((1,3,6,1,4,1,173,7,8,2,2,1,6),_PortThreshFCSErrPerSec_Type())
portThreshFCSErrPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshFCSErrPerSec.setStatus(_A)
_PortThreshLogRejPerSec_Type=Integer32
_PortThreshLogRejPerSec_Object=MibTableColumn
portThreshLogRejPerSec=_PortThreshLogRejPerSec_Object((1,3,6,1,4,1,173,7,8,2,2,1,7),_PortThreshLogRejPerSec_Type())
portThreshLogRejPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshLogRejPerSec.setStatus(_A)
_PortThreshTxErrorRatio_Type=Integer32
_PortThreshTxErrorRatio_Object=MibTableColumn
portThreshTxErrorRatio=_PortThreshTxErrorRatio_Object((1,3,6,1,4,1,173,7,8,2,2,1,8),_PortThreshTxErrorRatio_Type())
portThreshTxErrorRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshTxErrorRatio.setStatus(_A)
_PortThreshRxErrorRatio_Type=Integer32
_PortThreshRxErrorRatio_Object=MibTableColumn
portThreshRxErrorRatio=_PortThreshRxErrorRatio_Object((1,3,6,1,4,1,173,7,8,2,2,1,9),_PortThreshRxErrorRatio_Type())
portThreshRxErrorRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshRxErrorRatio.setStatus(_A)
_PortThreshTxPercentUtl_Type=Integer32
_PortThreshTxPercentUtl_Object=MibTableColumn
portThreshTxPercentUtl=_PortThreshTxPercentUtl_Object((1,3,6,1,4,1,173,7,8,2,2,1,10),_PortThreshTxPercentUtl_Type())
portThreshTxPercentUtl.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshTxPercentUtl.setStatus(_A)
_PortThreshRxPercentUtl_Type=Integer32
_PortThreshRxPercentUtl_Object=MibTableColumn
portThreshRxPercentUtl=_PortThreshRxPercentUtl_Object((1,3,6,1,4,1,173,7,8,2,2,1,11),_PortThreshRxPercentUtl_Type())
portThreshRxPercentUtl.setMaxAccess(_C)
if mibBuilder.loadTexts:portThreshRxPercentUtl.setStatus(_A)
_Bridge_ObjectIdentity=ObjectIdentity
bridge=_Bridge_ObjectIdentity((1,3,6,1,4,1,173,7,9))
class _BridgeAdminVirtualLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BridgeAdminVirtualLANID_Type.__name__=_B
_BridgeAdminVirtualLANID_Object=MibScalar
bridgeAdminVirtualLANID=_BridgeAdminVirtualLANID_Object((1,3,6,1,4,1,173,7,9,1),_BridgeAdminVirtualLANID_Type())
bridgeAdminVirtualLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeAdminVirtualLANID.setStatus(_A)
class _BridgeOperVirtualLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BridgeOperVirtualLANID_Type.__name__=_B
_BridgeOperVirtualLANID_Object=MibScalar
bridgeOperVirtualLANID=_BridgeOperVirtualLANID_Object((1,3,6,1,4,1,173,7,9,2),_BridgeOperVirtualLANID_Type())
bridgeOperVirtualLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeOperVirtualLANID.setStatus(_A)
class _BridgeEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BridgeEnabled_Type.__name__=_B
_BridgeEnabled_Object=MibScalar
bridgeEnabled=_BridgeEnabled_Object((1,3,6,1,4,1,173,7,9,3),_BridgeEnabled_Type())
bridgeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeEnabled.setStatus(_A)
class _BridgeMaxSizeForwardingTable_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,65535))
_BridgeMaxSizeForwardingTable_Type.__name__=_B
_BridgeMaxSizeForwardingTable_Object=MibScalar
bridgeMaxSizeForwardingTable=_BridgeMaxSizeForwardingTable_Object((1,3,6,1,4,1,173,7,9,4),_BridgeMaxSizeForwardingTable_Type())
bridgeMaxSizeForwardingTable.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeMaxSizeForwardingTable.setStatus(_A)
class _BridgeIPEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BridgeIPEnabled_Type.__name__=_B
_BridgeIPEnabled_Object=MibScalar
bridgeIPEnabled=_BridgeIPEnabled_Object((1,3,6,1,4,1,173,7,9,5),_BridgeIPEnabled_Type())
bridgeIPEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeIPEnabled.setStatus(_A)
class _BridgeIPXEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BridgeIPXEnabled_Type.__name__=_B
_BridgeIPXEnabled_Object=MibScalar
bridgeIPXEnabled=_BridgeIPXEnabled_Object((1,3,6,1,4,1,173,7,9,6),_BridgeIPXEnabled_Type())
bridgeIPXEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeIPXEnabled.setStatus(_A)
class _BridgeAdminSRBID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BridgeAdminSRBID_Type.__name__=_B
_BridgeAdminSRBID_Object=MibScalar
bridgeAdminSRBID=_BridgeAdminSRBID_Object((1,3,6,1,4,1,173,7,9,7),_BridgeAdminSRBID_Type())
bridgeAdminSRBID.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeAdminSRBID.setStatus(_A)
class _BridgeOperSRBID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_BridgeOperSRBID_Type.__name__=_B
_BridgeOperSRBID_Object=MibScalar
bridgeOperSRBID=_BridgeOperSRBID_Object((1,3,6,1,4,1,173,7,9,8),_BridgeOperSRBID_Type())
bridgeOperSRBID.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeOperSRBID.setStatus(_A)
class _BridgeDefaultEthernetFrameType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type-II',1),('ieee8023',2)))
_BridgeDefaultEthernetFrameType_Type.__name__=_B
_BridgeDefaultEthernetFrameType_Object=MibScalar
bridgeDefaultEthernetFrameType=_BridgeDefaultEthernetFrameType_Object((1,3,6,1,4,1,173,7,9,9),_BridgeDefaultEthernetFrameType_Type())
bridgeDefaultEthernetFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeDefaultEthernetFrameType.setStatus(_A)
_IpNl_ObjectIdentity=ObjectIdentity
ipNl=_IpNl_ObjectIdentity((1,3,6,1,4,1,173,7,11))
class _NlIpDefaultRIPVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ripVersion1',1),('rip1Compatible',2),('ripVersion2',3)))
_NlIpDefaultRIPVersion_Type.__name__=_B
_NlIpDefaultRIPVersion_Object=MibScalar
nlIpDefaultRIPVersion=_NlIpDefaultRIPVersion_Object((1,3,6,1,4,1,173,7,11,1),_NlIpDefaultRIPVersion_Type())
nlIpDefaultRIPVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nlIpDefaultRIPVersion.setStatus(_A)
_Voice_ObjectIdentity=ObjectIdentity
voice=_Voice_ObjectIdentity((1,3,6,1,4,1,173,7,12))
class _VoiceSystemVoiceNodeNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_VoiceSystemVoiceNodeNum_Type.__name__=_B
_VoiceSystemVoiceNodeNum_Object=MibScalar
voiceSystemVoiceNodeNum=_VoiceSystemVoiceNodeNum_Object((1,3,6,1,4,1,173,7,12,1),_VoiceSystemVoiceNodeNum_Type())
voiceSystemVoiceNodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemVoiceNodeNum.setStatus(_A)
class _VoiceSystemRingVolFreq_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('v75-hz-16-66',1),('v80-hz-20-00',2),('v75-hz-25-00',3),('v60-hz-50-00',4),('v75-hz-50-00',5)))
_VoiceSystemRingVolFreq_Type.__name__=_B
_VoiceSystemRingVolFreq_Object=MibScalar
voiceSystemRingVolFreq=_VoiceSystemRingVolFreq_Object((1,3,6,1,4,1,173,7,12,2),_VoiceSystemRingVolFreq_Type())
voiceSystemRingVolFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemRingVolFreq.setStatus(_A)
class _VoiceSystemCountryCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_VoiceSystemCountryCode_Type.__name__=_B
_VoiceSystemCountryCode_Object=MibScalar
voiceSystemCountryCode=_VoiceSystemCountryCode_Object((1,3,6,1,4,1,173,7,12,3),_VoiceSystemCountryCode_Type())
voiceSystemCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemCountryCode.setStatus(_A)
class _VoiceSystemDialDigits_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_VoiceSystemDialDigits_Type.__name__=_B
_VoiceSystemDialDigits_Object=MibScalar
voiceSystemDialDigits=_VoiceSystemDialDigits_Object((1,3,6,1,4,1,173,7,12,4),_VoiceSystemDialDigits_Type())
voiceSystemDialDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemDialDigits.setStatus(_A)
class _VoiceSystemVoiceRatesMin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4)))
_VoiceSystemVoiceRatesMin_Type.__name__=_B
_VoiceSystemVoiceRatesMin_Object=MibScalar
voiceSystemVoiceRatesMin=_VoiceSystemVoiceRatesMin_Object((1,3,6,1,4,1,173,7,12,5),_VoiceSystemVoiceRatesMin_Type())
voiceSystemVoiceRatesMin.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemVoiceRatesMin.setStatus(_A)
class _VoiceSystemVoiceRatesMax_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4)))
_VoiceSystemVoiceRatesMax_Type.__name__=_B
_VoiceSystemVoiceRatesMax_Object=MibScalar
voiceSystemVoiceRatesMax=_VoiceSystemVoiceRatesMax_Object((1,3,6,1,4,1,173,7,12,6),_VoiceSystemVoiceRatesMax_Type())
voiceSystemVoiceRatesMax.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemVoiceRatesMax.setStatus(_A)
class _VoiceSystemExtDialDigits_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_VoiceSystemExtDialDigits_Type.__name__=_B
_VoiceSystemExtDialDigits_Object=MibScalar
voiceSystemExtDialDigits=_VoiceSystemExtDialDigits_Object((1,3,6,1,4,1,173,7,12,7),_VoiceSystemExtDialDigits_Type())
voiceSystemExtDialDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSystemExtDialDigits.setStatus(_A)
_VoiceSpeedDialTable_Object=MibTable
voiceSpeedDialTable=_VoiceSpeedDialTable_Object((1,3,6,1,4,1,173,7,12,8))
if mibBuilder.loadTexts:voiceSpeedDialTable.setStatus(_A)
_VoiceSpeedDialEntry_Object=MibTableRow
voiceSpeedDialEntry=_VoiceSpeedDialEntry_Object((1,3,6,1,4,1,173,7,12,8,1))
voiceSpeedDialEntry.setIndexNames((0,_E,_BN))
if mibBuilder.loadTexts:voiceSpeedDialEntry.setStatus(_A)
class _VoiceSpeedDialDigits_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_VoiceSpeedDialDigits_Type.__name__=_J
_VoiceSpeedDialDigits_Object=MibTableColumn
voiceSpeedDialDigits=_VoiceSpeedDialDigits_Object((1,3,6,1,4,1,173,7,12,8,1,1),_VoiceSpeedDialDigits_Type())
voiceSpeedDialDigits.setMaxAccess(_C)
if mibBuilder.loadTexts:voiceSpeedDialDigits.setStatus(_A)
class _VoiceSpeedDialLongDialMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_VoiceSpeedDialLongDialMap_Type.__name__=_J
_VoiceSpeedDialLongDialMap_Object=MibTableColumn
voiceSpeedDialLongDialMap=_VoiceSpeedDialLongDialMap_Object((1,3,6,1,4,1,173,7,12,8,1,2),_VoiceSpeedDialLongDialMap_Type())
voiceSpeedDialLongDialMap.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSpeedDialLongDialMap.setStatus(_A)
class _VoiceSpeedDialExtDialStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_VoiceSpeedDialExtDialStr_Type.__name__=_J
_VoiceSpeedDialExtDialStr_Object=MibTableColumn
voiceSpeedDialExtDialStr=_VoiceSpeedDialExtDialStr_Object((1,3,6,1,4,1,173,7,12,8,1,3),_VoiceSpeedDialExtDialStr_Type())
voiceSpeedDialExtDialStr.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSpeedDialExtDialStr.setStatus(_A)
_VoiceSpeedDialRowStatus_Type=RowStatus
_VoiceSpeedDialRowStatus_Object=MibTableColumn
voiceSpeedDialRowStatus=_VoiceSpeedDialRowStatus_Object((1,3,6,1,4,1,173,7,12,8,1,4),_VoiceSpeedDialRowStatus_Type())
voiceSpeedDialRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:voiceSpeedDialRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'NlSubscriberAddress':NlSubscriberAddress,'snaDLC':snaDLC,_o:sdlc,'sdlcLSGroup':sdlcLSGroup,'sdlcLSAdminTable':sdlcLSAdminTable,'sdlcLSAdminEntry':sdlcLSAdminEntry,_X:sdlcLSAddress,'netlink':netlink,'network':network,'netstat':netstat,'nsMaxNeigh':nsMaxNeigh,'nsThisNode':nsThisNode,'nsNodTable':nsNodTable,'nsEntry':nsEntry,_v:nsNodNum,'nsStatus':nsStatus,'nsNumNeigh':nsNumNeigh,'nsNeighTable':nsNeighTable,'nsNeighEntry':nsNeighEntry,_w:nsNTNode,_x:nsNTNeigh,'nsNTNeighStat':nsNTNeighStat,'local':local,'node':node,'nodeCfgTable':nodeCfgTable,'nodeAlmTable':nodeAlmTable,'nodeSNMPGroup':nodeSNMPGroup,'nodeModel':nodeModel,'nodeTrapText':nodeTrapText,'nodeTrapAdrTable':nodeTrapAdrTable,'tpAdrEntry':tpAdrEntry,_y:tpAdrIdx,'tpAddress':tpAddress,'tpAdrFlag':tpAdrFlag,'tpAdrSLev':tpAdrSLev,'nodeBagTable':nodeBagTable,'hwcard':hwcard,'rlpMaxProtos':rlpMaxProtos,'rlpConfigTable':rlpConfigTable,'rlpEntry':rlpEntry,_z:rlpIndex,'rlpStatus':rlpStatus,'rlpMemorySize':rlpMemorySize,'rlpLIC1Type':rlpLIC1Type,'rlpLIC2Type':rlpLIC2Type,'rlpProtocol':rlpProtocol,'rlpGroupNumber':rlpGroupNumber,'rlpGroupResponsibility':rlpGroupResponsibility,'port':port,'portX25Group':portX25Group,'portPhyX25AdminTable':portPhyX25AdminTable,'portPhyX25AdminEntry':portPhyX25AdminEntry,'portPhyX25AdminConnector':portPhyX25AdminConnector,'portPhyX25AdminSpeed':portPhyX25AdminSpeed,'portPhyX25AdminGenerateClock':portPhyX25AdminGenerateClock,'portPhyX25AdminRcvClockFromDTE':portPhyX25AdminRcvClockFromDTE,'portPhyX25AdminDialOut':portPhyX25AdminDialOut,'portPhyX25AdminInactivityTimer':portPhyX25AdminInactivityTimer,'portPhyX25AdminDisconnectTimer':portPhyX25AdminDisconnectTimer,'portPhyX25AdminSetupTimer':portPhyX25AdminSetupTimer,'portPhyX25AdminTrunkFlag':portPhyX25AdminTrunkFlag,'portPhyX25AdminTrunkGroup':portPhyX25AdminTrunkGroup,'portPhyX25AdminRowStatus':portPhyX25AdminRowStatus,'portPhyX25OperTable':portPhyX25OperTable,'portPhyX25OperEntry':portPhyX25OperEntry,'portPhyX25OperConnector':portPhyX25OperConnector,'portPhyX25OperSpeed':portPhyX25OperSpeed,'portPhyX25OperGenerateClock':portPhyX25OperGenerateClock,'portPhyX25OperRcvClockFromDTE':portPhyX25OperRcvClockFromDTE,'portPhyX25OperDialOut':portPhyX25OperDialOut,'portPhyX25OperInactivityTimer':portPhyX25OperInactivityTimer,'portPhyX25OperDisconnectTimer':portPhyX25OperDisconnectTimer,'portPhyX25OperSetupTimer':portPhyX25OperSetupTimer,'portPhyX25OperTrunkFlag':portPhyX25OperTrunkFlag,'portPhyX25OperTrunkGroup':portPhyX25OperTrunkGroup,'portLogicalX25AdminTable':portLogicalX25AdminTable,'portLogicalX25AdminEntry':portLogicalX25AdminEntry,'portLogicalX25AdminFrDlci':portLogicalX25AdminFrDlci,'portLogicalX25AdminCxnPriority':portLogicalX25AdminCxnPriority,'portLogicalX25AdminRfc1490':portLogicalX25AdminRfc1490,'portLogicalX25AdminBAG':portLogicalX25AdminBAG,'portLogicalX25AdminRowStatus':portLogicalX25AdminRowStatus,'portLogicalX25OperTable':portLogicalX25OperTable,'portLogicalX25OperEntry':portLogicalX25OperEntry,'portLogicalX25OperFrDlci':portLogicalX25OperFrDlci,'portLogicalX25OperCxnPriority':portLogicalX25OperCxnPriority,'portLogicalX25OperRfc1490':portLogicalX25OperRfc1490,'portLogicalX25OperBAG':portLogicalX25OperBAG,'portX25AdminTable':portX25AdminTable,'portX25AdminEntry':portX25AdminEntry,'portX25AdminBlockedFlag':portX25AdminBlockedFlag,'portX25AdminFlowCtrlNeg':portX25AdminFlowCtrlNeg,'portX25AdminThruptClassNeg':portX25AdminThruptClassNeg,'portX25AdminLocChgPrev':portX25AdminLocChgPrev,'portX25AdminRevChgAccpt':portX25AdminRevChgAccpt,'portX25AdminFastSelAccpt':portX25AdminFastSelAccpt,'portX25AdminInCallBar':portX25AdminInCallBar,'portX25AdminOutCallBar':portX25AdminOutCallBar,'portX25AdminMaxPktSize':portX25AdminMaxPktSize,'portX25AdminDefPktSize':portX25AdminDefPktSize,'portX25AdminMaxWinSize':portX25AdminMaxWinSize,'portX25AdminDefWinSize':portX25AdminDefWinSize,'portX25AdminMaxThruptClass':portX25AdminMaxThruptClass,'portX25AdminCUGPref':portX25AdminCUGPref,'portX25AdminCUGIndex':portX25AdminCUGIndex,'portX25AdminCUGIncAccess':portX25AdminCUGIncAccess,'portX25AdminCUGOutAccess':portX25AdminCUGOutAccess,'portX25OperTable':portX25OperTable,'portX25OperEntry':portX25OperEntry,'portX25OperBlockedFlag':portX25OperBlockedFlag,'portX25OperFlowCtrlNeg':portX25OperFlowCtrlNeg,'portX25OperThruptClassNeg':portX25OperThruptClassNeg,'portX25OperLocChgPrev':portX25OperLocChgPrev,'portX25OperRevChgAccpt':portX25OperRevChgAccpt,'portX25OperFastSelAccpt':portX25OperFastSelAccpt,'portX25OperInCallBar':portX25OperInCallBar,'portX25OperOutCallBar':portX25OperOutCallBar,'portX25OperMaxPktSize':portX25OperMaxPktSize,'portX25OperDefPktSize':portX25OperDefPktSize,'portX25OperMaxWinSize':portX25OperMaxWinSize,'portX25OperDefWinSize':portX25OperDefWinSize,'portX25OperMaxThruptClass':portX25OperMaxThruptClass,'portX25OperCUGPref':portX25OperCUGPref,'portX25OperCUGIndex':portX25OperCUGIndex,'portX25OperCUGIncAccess':portX25OperCUGIncAccess,'portX25OperCUGOutAccess':portX25OperCUGOutAccess,'portFrGroup':portFrGroup,'portFrConfigTable':portFrConfigTable,'portFrEntry':portFrEntry,_A3:portFrRlpIndex,_A4:portFrPortIndex,'portFrBlockedFlag':portFrBlockedFlag,'portFrMaxBytesPerFrame':portFrMaxBytesPerFrame,'portFrT392Timer':portFrT392Timer,'portFrOutgoingRateControl':portFrOutgoingRateControl,'portFrBandwidthAllocation':portFrBandwidthAllocation,'portFrConnector':portFrConnector,'portFrLogicalDCE':portFrLogicalDCE,'portFrGenClock':portFrGenClock,'portFrRcvClkFrmDTE':portFrRcvClkFrmDTE,'portFrLLM':portFrLLM,'portFrRowStatus':portFrRowStatus,'portFrSpeed':portFrSpeed,'portFrBackupUseOnly':portFrBackupUseOnly,'portDLCIConfigTable':portDLCIConfigTable,'portDLCIEntry':portDLCIEntry,_A5:portDLCIRlpIndex,_A6:portDLCIPortIndex,_A7:portDLCIIndex,'portDLCIIncomingCIR':portDLCIIncomingCIR,'portDLCIOutgoingCIR':portDLCIOutgoingCIR,'portDLCIIncomingBc':portDLCIIncomingBc,'portDLCIOutgoingBc':portDLCIOutgoingBc,'portDLCIIncomingBe':portDLCIIncomingBe,'portDLCIOutgoingBe':portDLCIOutgoingBe,'portDLCIBecnRecoveryCnt':portDLCIBecnRecoveryCnt,'portDLCIPriority':portDLCIPriority,'portDLCIRowStatus':portDLCIRowStatus,'portDLCIBackupGroup':portDLCIBackupGroup,'portDLCIBackupProtEnb':portDLCIBackupProtEnb,'portFrBackupGroupTable':portFrBackupGroupTable,'portFrBackupEntry':portFrBackupEntry,_A8:portFrBackupRLP,_A9:portFrBackupPort,_AA:portFrBackupDLCI,_AB:portFrBackupGroup,'portFrBackupWaitTimer':portFrBackupWaitTimer,'portFrBackupProtEnab':portFrBackupProtEnab,'portFrBackupRowStatus':portFrBackupRowStatus,'portBsciGroup':portBsciGroup,'portBsciAdminTable':portBsciAdminTable,'portBsciAdminEntry':portBsciAdminEntry,'portBsciAdminBlockedFlag':portBsciAdminBlockedFlag,'portBsciAdminConnector':portBsciAdminConnector,'portBsciAdminSpeed':portBsciAdminSpeed,'portBsciAdminRetransmitInterval':portBsciAdminRetransmitInterval,'portBsciAdminMAXRetransmits':portBsciAdminMAXRetransmits,'portBsciAdminMaxBytesPerFrame':portBsciAdminMaxBytesPerFrame,'portBsciAdminGenerateClock':portBsciAdminGenerateClock,'portBsciAdminRcvClockFromDTE':portBsciAdminRcvClockFromDTE,'portBsciAdminPadType':portBsciAdminPadType,'portBsciAdminUseEBCDIC':portBsciAdminUseEBCDIC,'portBsciAdminCallInfoInRequestPacket':portBsciAdminCallInfoInRequestPacket,'portBsciAdminClearVCOnLastDeviceDown':portBsciAdminClearVCOnLastDeviceDown,'portBsciAdminTransTextSupported':portBsciAdminTransTextSupported,'portBsciAdminEndToEndAck':portBsciAdminEndToEndAck,'portBsciAdminFullDuplex':portBsciAdminFullDuplex,'portBsciAdminMultidrop':portBsciAdminMultidrop,'portBsciAdminSlowPollRetryCount':portBsciAdminSlowPollRetryCount,'portBsciAdminSlowPollRetryFreq':portBsciAdminSlowPollRetryFreq,'portBsciAdminStartSynchChars':portBsciAdminStartSynchChars,'portBsciAdminEndPadChars':portBsciAdminEndPadChars,'portBsciAdminPollInterval':portBsciAdminPollInterval,'portBsciAdminNoResponseTimer':portBsciAdminNoResponseTimer,'portBsciAdminNoResponseRetryCount':portBsciAdminNoResponseRetryCount,'portBsciAdminErrorRetransmitCount':portBsciAdminErrorRetransmitCount,'portBsciAdminNAKRetryCount':portBsciAdminNAKRetryCount,'portBsciAdminBlockCheck':portBsciAdminBlockCheck,'portBsciAdminDataMode':portBsciAdminDataMode,'portBsciAdminRowStatus':portBsciAdminRowStatus,'portBsciAdminAnswerNonConfigured':portBsciAdminAnswerNonConfigured,'portBsciAdminActivateConnectionWithoutPoll':portBsciAdminActivateConnectionWithoutPoll,'portBsciOperTable':portBsciOperTable,'portBsciOperEntry':portBsciOperEntry,'portBsciOperBlockedFlag':portBsciOperBlockedFlag,'portBsciOperConnector':portBsciOperConnector,'portBsciOperSpeed':portBsciOperSpeed,'portBsciOperRetransmitInterval':portBsciOperRetransmitInterval,'portBsciOperMAXRetransmits':portBsciOperMAXRetransmits,'portBsciOperMaxBytesPerFrame':portBsciOperMaxBytesPerFrame,'portBsciOperGenerateClock':portBsciOperGenerateClock,'portBsciOperRcvClockFromDTE':portBsciOperRcvClockFromDTE,'portBsciOperPadType':portBsciOperPadType,'portBsciOperUseEBCDIC':portBsciOperUseEBCDIC,'portBsciOperCallInfoInRequestPacket':portBsciOperCallInfoInRequestPacket,'portBsciOperClearVCOnLastDeviceDown':portBsciOperClearVCOnLastDeviceDown,'portBsciOperTransTextSupported':portBsciOperTransTextSupported,'portBsciOperEndToEndAck':portBsciOperEndToEndAck,'portBsciOperFullDuplex':portBsciOperFullDuplex,'portBsciOperMultidrop':portBsciOperMultidrop,'portBsciOperSlowPollRetryCount':portBsciOperSlowPollRetryCount,'portBsciOperSlowPollRetryFreq':portBsciOperSlowPollRetryFreq,'portBsciOperStartSynchChars':portBsciOperStartSynchChars,'portBsciOperEndPadChars':portBsciOperEndPadChars,'portBsciOperPollInterval':portBsciOperPollInterval,'portBsciOperNoResponseTimer':portBsciOperNoResponseTimer,'portBsciOperNoResponseRetryCount':portBsciOperNoResponseRetryCount,'portBsciOperErrorRetransmitCount':portBsciOperErrorRetransmitCount,'portBsciOperNAKRetryCount':portBsciOperNAKRetryCount,'portBsciOperBlockCheck':portBsciOperBlockCheck,'portBsciOperDataMode':portBsciOperDataMode,'portBsciOperAnswerNonConfigured':portBsciOperAnswerNonConfigured,'portBsciOperActivateConnectionWithoutPoll':portBsciOperActivateConnectionWithoutPoll,'bsciSubscrAdminTable':bsciSubscrAdminTable,'bsciSubscrAdminEntry':bsciSubscrAdminEntry,_AE:bsciSubscrAdminSequence,'bsciSubscrAdminLocalID':bsciSubscrAdminLocalID,'bsciSubscrAdminRemoteID':bsciSubscrAdminRemoteID,'bsciSubscrAdminAutocall':bsciSubscrAdminAutocall,'bsciSubscrAdminAutocallRtyTimer':bsciSubscrAdminAutocallRtyTimer,'bsciSubscrAdminAutocallMaxRtry':bsciSubscrAdminAutocallMaxRtry,'bsciSubscrAdminConnectionID':bsciSubscrAdminConnectionID,'bsciSubscrAdminRowStatus':bsciSubscrAdminRowStatus,'bsciSubscrOperTable':bsciSubscrOperTable,'bsciSubscrOperEntry':bsciSubscrOperEntry,_AF:bsciSubscrOperSequence,'bsciSubscrOperLocalID':bsciSubscrOperLocalID,'bsciSubscrOperRemoteID':bsciSubscrOperRemoteID,'bsciSubscrOperAutocall':bsciSubscrOperAutocall,'bsciSubscrOperAutocallRtyTimer':bsciSubscrOperAutocallRtyTimer,'bsciSubscrOperAutocallMaxRtry':bsciSubscrOperAutocallMaxRtry,'bsciSubscrOperConnectionID':bsciSubscrOperConnectionID,'bsciDevAdminTable':bsciDevAdminTable,'bsciDevAdminEntry':bsciDevAdminEntry,_AG:bsciDevAdminControlUnitID,_AH:bsciDevAdminDeviceUnitID,'bsciDevAdminConnectionID':bsciDevAdminConnectionID,'bsciDevAdminSingleUserVC':bsciDevAdminSingleUserVC,'bsciDevAdminTransTextSupported':bsciDevAdminTransTextSupported,'bsciDevAdminPrinterAttached':bsciDevAdminPrinterAttached,'bsciDevAdminRowStatus':bsciDevAdminRowStatus,'bsciDevAdminDisableStatusRequest':bsciDevAdminDisableStatusRequest,'bsciDevOperTable':bsciDevOperTable,'bsciDevOperEntry':bsciDevOperEntry,_AJ:bsciDevOperControlUnitID,_AK:bsciDevOperDeviceUnitID,'bsciDevOperConnectionID':bsciDevOperConnectionID,'bsciDevOperSingleUserVC':bsciDevOperSingleUserVC,'bsciDevOperTransTextSupported':bsciDevOperTransTextSupported,'bsciDevOperPrinterAttached':bsciDevOperPrinterAttached,'bsciDevOperDisableStatusRequest':bsciDevOperDisableStatusRequest,'portSdlcGroup':portSdlcGroup,'portSdlcAdminTable':portSdlcAdminTable,'portSdlcAdminEntry':portSdlcAdminEntry,'portSdlcAdminCommit':portSdlcAdminCommit,'portSdlcAdminMAXRetries':portSdlcAdminMAXRetries,'portSdlcAdminMAXOut':portSdlcAdminMAXOut,'portSdlcAdminPadType':portSdlcAdminPadType,'portSdlcAdminGenerateClock':portSdlcAdminGenerateClock,'portSdlcAdminRcvClockFromDTE':portSdlcAdminRcvClockFromDTE,'portSdlcAdminNrz':portSdlcAdminNrz,'portSdlcAdminPacketSize':portSdlcAdminPacketSize,'portSdlcAdminDisableRequestDisconnect':portSdlcAdminDisableRequestDisconnect,'portSdlcAdminLPDASupport':portSdlcAdminLPDASupport,'portSdlcAdminConnector':portSdlcAdminConnector,'portSdlcAdminSpeed':portSdlcAdminSpeed,'portSdlcAdminRowStatus':portSdlcAdminRowStatus,'portSdlcAdminIdleFillChar':portSdlcAdminIdleFillChar,'portSdlcAdminInactivityTimer':portSdlcAdminInactivityTimer,'portSdlcAdminL1Duplex':portSdlcAdminL1Duplex,'portSdlcOperTable':portSdlcOperTable,'portSdlcOperEntry':portSdlcOperEntry,'portSdlcOperCommit':portSdlcOperCommit,'portSdlcOperMAXRetries':portSdlcOperMAXRetries,'portSdlcOperMAXOut':portSdlcOperMAXOut,'portSdlcOperPadType':portSdlcOperPadType,'portSdlcOperGenerateClock':portSdlcOperGenerateClock,'portSdlcOperRcvClockFromDTE':portSdlcOperRcvClockFromDTE,'portSdlcOperNrz':portSdlcOperNrz,'portSdlcOperPacketSize':portSdlcOperPacketSize,'portSdlcOperDisableRequestDisconnect':portSdlcOperDisableRequestDisconnect,'portSdlcOperLPDASupport':portSdlcOperLPDASupport,'portSdlcOperConnector':portSdlcOperConnector,'portSdlcOperSpeed':portSdlcOperSpeed,'portSdlcOperIdleFillChar':portSdlcOperIdleFillChar,'portSdlcOperInactivityTimer':portSdlcOperInactivityTimer,'portSdlcOperL1Duplex':portSdlcOperL1Duplex,'lSSdlcAdminTable':lSSdlcAdminTable,'lSSdlcAdminEntry':lSSdlcAdminEntry,'lSSdlcAdminLocalSub':lSSdlcAdminLocalSub,'lSSdlcAdminRemoteSub':lSSdlcAdminRemoteSub,'lSSdlcAdminAutoCall':lSSdlcAdminAutoCall,'lSSdlcAdminRetryTime':lSSdlcAdminRetryTime,'lSSdlcAdminRetryCount':lSSdlcAdminRetryCount,'lSSdlcAdminLlc2Conversion':lSSdlcAdminLlc2Conversion,'lSSdlcAdminLPDAResourceID':lSSdlcAdminLPDAResourceID,'lSSdlcAdminRowStatus':lSSdlcAdminRowStatus,'lSSdlcAdminL2DatMode':lSSdlcAdminL2DatMode,'lSSdlcOperTable':lSSdlcOperTable,'lSSdlcOperEntry':lSSdlcOperEntry,'lSSdlcOperLocalSub':lSSdlcOperLocalSub,'lSSdlcOperRemoteSub':lSSdlcOperRemoteSub,'lSSdlcOperAutoCall':lSSdlcOperAutoCall,'lSSdlcOperRetryTime':lSSdlcOperRetryTime,'lSSdlcOperRetryCount':lSSdlcOperRetryCount,'lSSdlcOperLlc2Conversion':lSSdlcOperLlc2Conversion,'lSSdlcOperLPDAResourceID':lSSdlcOperLPDAResourceID,'lSSdlcOperL2DatMode':lSSdlcOperL2DatMode,'lSSdlcLlc2AdminTable':lSSdlcLlc2AdminTable,'lSSdlcLlc2AdminEntry':lSSdlcLlc2AdminEntry,'lSSdlcLlc2AdminLocalSap':lSSdlcLlc2AdminLocalSap,'lSSdlcLlc2AdminLocalMac':lSSdlcLlc2AdminLocalMac,'lSSdlcLlc2AdminIdblk':lSSdlcLlc2AdminIdblk,'lSSdlcLlc2AdminIdnum':lSSdlcLlc2AdminIdnum,'lSSdlcLlc2AdminLanTi':lSSdlcLlc2AdminLanTi,'lSSdlcLlc2AdminLanT1':lSSdlcLlc2AdminLanT1,'lSSdlcLlc2AdminLanT2':lSSdlcLlc2AdminLanT2,'lSSdlcLlc2AdminLanN2':lSSdlcLlc2AdminLanN2,'lSSdlcLlc2AdminLanN3':lSSdlcLlc2AdminLanN3,'lSSdlcLlc2AdminLanTw':lSSdlcLlc2AdminLanTw,'lSSdlcLlc2AdminBAG':lSSdlcLlc2AdminBAG,'lSSdlcLlc2AdminPriority':lSSdlcLlc2AdminPriority,'lSSdlcLlc2AdminRowStatus':lSSdlcLlc2AdminRowStatus,'lSSdlcLlc2AdminSuppressXID':lSSdlcLlc2AdminSuppressXID,'lSSdlcLlc2OperTable':lSSdlcLlc2OperTable,'lSSdlcLlc2OperEntry':lSSdlcLlc2OperEntry,'lSSdlcLlc2OperLocalSap':lSSdlcLlc2OperLocalSap,'lSSdlcLlc2OperLocalMac':lSSdlcLlc2OperLocalMac,'lSSdlcLlc2OperIdblk':lSSdlcLlc2OperIdblk,'lSSdlcLlc2OperIdnum':lSSdlcLlc2OperIdnum,'lSSdlcLlc2OperLanTi':lSSdlcLlc2OperLanTi,'lSSdlcLlc2OperLanT1':lSSdlcLlc2OperLanT1,'lSSdlcLlc2OperLanT2':lSSdlcLlc2OperLanT2,'lSSdlcLlc2OperLanN2':lSSdlcLlc2OperLanN2,'lSSdlcLlc2OperLanN3':lSSdlcLlc2OperLanN3,'lSSdlcLlc2OperLanTw':lSSdlcLlc2OperLanTw,'lSSdlcLlc2OperBAG':lSSdlcLlc2OperBAG,'lSSdlcLlc2OperPriority':lSSdlcLlc2OperPriority,'lSSdlcLlc2OperSuppressXID':lSSdlcLlc2OperSuppressXID,'portT1Group':portT1Group,'portT1AdminTable':portT1AdminTable,'portT1AdminEntry':portT1AdminEntry,'portT1AdminBlockedPortFlag':portT1AdminBlockedPortFlag,'portT1AdminGenerateClock':portT1AdminGenerateClock,'portT1AdminFramingMode':portT1AdminFramingMode,'portT1AdminFrameModelSelect':portT1AdminFrameModelSelect,'portT1AdminLineEncoding':portT1AdminLineEncoding,'portT1AdminLineBuildOut':portT1AdminLineBuildOut,'portT1AdminRowStatus':portT1AdminRowStatus,'portT1AdminProtocolFraming':portT1AdminProtocolFraming,'portT1AdminNRZI':portT1AdminNRZI,'portT1OperTable':portT1OperTable,'portT1OperEntry':portT1OperEntry,'portT1OperBlockedPortFlag':portT1OperBlockedPortFlag,'portT1OperGenerateClock':portT1OperGenerateClock,'portT1OperFramingMode':portT1OperFramingMode,'portT1OperFrameModelSelect':portT1OperFrameModelSelect,'portT1OperLineEncoding':portT1OperLineEncoding,'portT1OperLineBuildOut':portT1OperLineBuildOut,'portT1OperProtocolFraming':portT1OperProtocolFraming,'portT1OperNRZI':portT1OperNRZI,'portVoiceGroup':portVoiceGroup,'portVoiceAdminTable':portVoiceAdminTable,'portVoiceAdminEntry':portVoiceAdminEntry,_AX:portVoiceAdminRlpIndex,_AY:portVoiceAdminPortIndex,'portVoiceAdminBlockedFlag':portVoiceAdminBlockedFlag,'portVoiceAdminSpeed':portVoiceAdminSpeed,'portVoiceAdminDTMF':portVoiceAdminDTMF,'portVoiceAdminInterface':portVoiceAdminInterface,'portVoiceAdminTETimer':portVoiceAdminTETimer,'portVoiceAdminLevelIn':portVoiceAdminLevelIn,'portVoiceAdminLevelOut':portVoiceAdminLevelOut,'portVoiceAdminCallTimer':portVoiceAdminCallTimer,'portVoiceAdminHuntGroup':portVoiceAdminHuntGroup,'portVoiceAdminLongDialPrefix':portVoiceAdminLongDialPrefix,'portVoiceAdminSLTTimeout':portVoiceAdminSLTTimeout,'portVoiceAdminLinkDownBusy':portVoiceAdminLinkDownBusy,'portVoiceAdminFaxSupported':portVoiceAdminFaxSupported,'portVoiceAdminTelephonyType':portVoiceAdminTelephonyType,'portVoiceAdminJitter':portVoiceAdminJitter,'portVoiceAdminSampleDelay':portVoiceAdminSampleDelay,'portVoiceAdminDialTimer':portVoiceAdminDialTimer,'portVoiceAdminAutoDial':portVoiceAdminAutoDial,'portVoiceAdminSuppression':portVoiceAdminSuppression,'portVoiceAdminAutoDialNumber':portVoiceAdminAutoDialNumber,'portVoiceAdminAutoPoll':portVoiceAdminAutoPoll,'portVoiceAdminAutoPollTimer':portVoiceAdminAutoPollTimer,'portVoiceAdminExtDigitsSource':portVoiceAdminExtDigitsSource,'portVoiceAdminNumDigitsDelete':portVoiceAdminNumDigitsDelete,'portVoiceAdminForwardDelay':portVoiceAdminForwardDelay,'portVoiceAdminForwardedType':portVoiceAdminForwardedType,'portVoiceAdminForwardedDigits':portVoiceAdminForwardedDigits,'portVoiceAdminMakeRatio':portVoiceAdminMakeRatio,'portVoiceAdminBreakRatio':portVoiceAdminBreakRatio,'portVoiceAdminDTMFOnDuration':portVoiceAdminDTMFOnDuration,'portVoiceAdminDTMFOffDuration':portVoiceAdminDTMFOffDuration,'portVoiceAdminToneType':portVoiceAdminToneType,'portVoiceAdminRowStatus':portVoiceAdminRowStatus,'portVoiceOperTable':portVoiceOperTable,'portVoiceOperEntry':portVoiceOperEntry,_Ab:portVoiceOperRlpIndex,_Ac:portVoiceOperPortIndex,'portVoiceOperBlockedFlag':portVoiceOperBlockedFlag,'portVoiceOperSpeed':portVoiceOperSpeed,'portVoiceOperDTMF':portVoiceOperDTMF,'portVoiceOperInterface':portVoiceOperInterface,'portVoiceOperTETimer':portVoiceOperTETimer,'portVoiceOperLevelIn':portVoiceOperLevelIn,'portVoiceOperLevelOut':portVoiceOperLevelOut,'portVoiceOperCallTimer':portVoiceOperCallTimer,'portVoiceOperHuntGroup':portVoiceOperHuntGroup,'portVoiceOperLongDialPrefix':portVoiceOperLongDialPrefix,'portVoiceOperSLTTimeout':portVoiceOperSLTTimeout,'portVoiceOperLinkDownBusy':portVoiceOperLinkDownBusy,'portVoiceOperFaxSupported':portVoiceOperFaxSupported,'portVoiceOperTelephonyType':portVoiceOperTelephonyType,'portVoiceOperJitter':portVoiceOperJitter,'portVoiceOperSampleDelay':portVoiceOperSampleDelay,'portVoiceOperDialTimer':portVoiceOperDialTimer,'portVoiceOperAutoDial':portVoiceOperAutoDial,'portVoiceOperSuppression':portVoiceOperSuppression,'portVoiceOperAutoDialNumber':portVoiceOperAutoDialNumber,'portVoiceOperAutoPoll':portVoiceOperAutoPoll,'portVoiceOperAutoPollTimer':portVoiceOperAutoPollTimer,'portVoiceOperExtDigitsSource':portVoiceOperExtDigitsSource,'portVoiceOperNumDigitsDelete':portVoiceOperNumDigitsDelete,'portVoiceOperForwardDelay':portVoiceOperForwardDelay,'portVoiceOperForwardedType':portVoiceOperForwardedType,'portVoiceOperForwardedDigits':portVoiceOperForwardedDigits,'portVoiceOperMakeRatio':portVoiceOperMakeRatio,'portVoiceOperBreakRatio':portVoiceOperBreakRatio,'portVoiceOperDTMFOnDuration':portVoiceOperDTMFOnDuration,'portVoiceOperDTMFOffDuration':portVoiceOperDTMFOffDuration,'portVoiceOperToneType':portVoiceOperToneType,'nlInterfaces':nlInterfaces,'nlIfTable':nlIfTable,'nlIfEntry':nlIfEntry,_H:nlIfRlp,_I:nlIfPort,'nlIfType':nlIfType,'nlIfIndex':nlIfIndex,'nlIfTableIndex':nlIfTableIndex,'nlIfTableOid':nlIfTableOid,'nlIfConnectorType':nlIfConnectorType,'nlIfPortStatus':nlIfPortStatus,_l:nlIfPhyPort,'nlIfLlc2Interfaces':nlIfLlc2Interfaces,'nlIfLlc2LANTable':nlIfLlc2LANTable,'nlIfLlc2LANEntry':nlIfLlc2LANEntry,_Ai:nlIfLlc2LANRlp,_Aj:nlIfLlc2LANPort,'nlIfLlc2LANType':nlIfLlc2LANType,'nlIfLlc2LANCard':nlIfLlc2LANCard,'nlIfLlc2LANID':nlIfLlc2LANID,'nlIfLlc2LANInterface':nlIfLlc2LANInterface,'nlIfLlc2LANRowStatus':nlIfLlc2LANRowStatus,'nlIfLlc2LANPriority':nlIfLlc2LANPriority,'nlIfLlc2LANBlockedPortFlag':nlIfLlc2LANBlockedPortFlag,'nlIfLlc2FrTable':nlIfLlc2FrTable,'nlIfLlc2FrEntry':nlIfLlc2FrEntry,_Ak:nlIfLlc2FrRlp,_Al:nlIfLlc2FrPort,_Am:nlIfLlc2FrDLCI,_An:nlIfLlc2FrFormat,'nlIfLlc2FrPriority':nlIfLlc2FrPriority,'nlIfLlc2FrBAG':nlIfLlc2FrBAG,'nlIfLlc2FrHostMACAddress':nlIfLlc2FrHostMACAddress,'nlIfLlc2FrSessionType':nlIfLlc2FrSessionType,'nlIfLlc2FrLANID':nlIfLlc2FrLANID,'nlIfLlc2FrInterface':nlIfLlc2FrInterface,'nlIfLlc2FrRowStatus':nlIfLlc2FrRowStatus,'nlIfLlc2FrBlockedPortFlag':nlIfLlc2FrBlockedPortFlag,'ipxConfig':ipxConfig,'ipxConfigRouting':ipxConfigRouting,'ipxStaticRouteConfigTable':ipxStaticRouteConfigTable,'ipxStaticRouteConfigEntry':ipxStaticRouteConfigEntry,_Ar:ipxStaticRouteConfigCircIndex,_As:ipxStaticRouteConfigNetNum,'ipxStaticRouteConfigRouter':ipxStaticRouteConfigRouter,'ipxStaticRouteConfigRowStatus':ipxStaticRouteConfigRowStatus,'ipxServConfigTable':ipxServConfigTable,'ipxServConfigEntry':ipxServConfigEntry,_At:ipxServConfigServiceType,_Au:ipxServConfigServName,'ipxServConfigServNetworkAddress':ipxServConfigServNetworkAddress,'ipxServConfigServNodeAddress':ipxServConfigServNodeAddress,'ipxServConfigServSocketNumber':ipxServConfigServSocketNumber,'ipxServConfigInterveningNetworks':ipxServConfigInterveningNetworks,'ipxServConfigGatewayAddress':ipxServConfigGatewayAddress,'ipxServConfigInterface':ipxServConfigInterface,'ipxServConfigRowStatus':ipxServConfigRowStatus,'ipxConfigInterface':ipxConfigInterface,'ipxInterfaceTable':ipxInterfaceTable,'ipxInterfaceEntry':ipxInterfaceEntry,_Av:ipxInterfaceNumber,'ipxInterfaceBlockedPortFlag':ipxInterfaceBlockedPortFlag,'ipxInterfaceType':ipxInterfaceType,'ipxInterfaceFrameType':ipxInterfaceFrameType,'ipxInterfaceMaxTransUnit':ipxInterfaceMaxTransUnit,'ipxInterfaceNetworkAddress':ipxInterfaceNetworkAddress,'ipxInterfaceBandwidthAllocGroup':ipxInterfaceBandwidthAllocGroup,'ipxInterfacePortDiagEnabled':ipxInterfacePortDiagEnabled,'ipxInterfaceNetBIOSEnabled':ipxInterfaceNetBIOSEnabled,'ipxInterfaceNetBIOSHops':ipxInterfaceNetBIOSHops,'ipxInterfacePeriodicRIPEnabled':ipxInterfacePeriodicRIPEnabled,'ipxInterfacePeriodicRIPTimer':ipxInterfacePeriodicRIPTimer,'ipxInterfacePeriodicSAPEnabled':ipxInterfacePeriodicSAPEnabled,'ipxInterfacePeriodicSAPTimer':ipxInterfacePeriodicSAPTimer,'ipxInterfaceRIPEnabled':ipxInterfaceRIPEnabled,'ipxInterfaceRIPAgeTimer':ipxInterfaceRIPAgeTimer,'ipxInterfaceRIPMaxSize':ipxInterfaceRIPMaxSize,'ipxInterfaceSAPEnabled':ipxInterfaceSAPEnabled,'ipxInterfaceSAPAgeTimer':ipxInterfaceSAPAgeTimer,'ipxInterfaceTransportTime':ipxInterfaceTransportTime,'ipxInterfaceSerializationEnabled':ipxInterfaceSerializationEnabled,'ipxInterfaceWatchdogSpoofingEnabled':ipxInterfaceWatchdogSpoofingEnabled,'ipxInterfaceLanCardNumber':ipxInterfaceLanCardNumber,'ipxInterfaceWanEnabled':ipxInterfaceWanEnabled,'ipxInterfaceSourceSubscriber':ipxInterfaceSourceSubscriber,'ipxInterfaceDestinationSubscriber':ipxInterfaceDestinationSubscriber,'ipxInterfaceSVCRetryTimer':ipxInterfaceSVCRetryTimer,'ipxInterfaceSVCIdleTimer':ipxInterfaceSVCIdleTimer,'ipxInterfaceMaxVC':ipxInterfaceMaxVC,'ipxInterfacePVCConnection':ipxInterfacePVCConnection,'ipxInterfaceSourceCard':ipxInterfaceSourceCard,'ipxInterfaceSourcePort':ipxInterfaceSourcePort,'ipxInterfaceSourceDLCI':ipxInterfaceSourceDLCI,'ipxInterfaceRowStatus':ipxInterfaceRowStatus,'ipxConfigNodeDefault':ipxConfigNodeDefault,'ipxNodeDefaultConfigNetworkAddress':ipxNodeDefaultConfigNetworkAddress,'ipxNodeDefaultConfigRIPSAPGap':ipxNodeDefaultConfigRIPSAPGap,'ipxNodeDefaultConfigRouterName':ipxNodeDefaultConfigRouterName,'nlIfIpInterfaces':nlIfIpInterfaces,'nlIfIpTable':nlIfIpTable,'nlIfIpEntry':nlIfIpEntry,_s:nlIfIpInterface,'nlIfIpMtu':nlIfIpMtu,'nlIfIpNetworkMask':nlIfIpNetworkMask,'nlIfIpRouteMetric':nlIfIpRouteMetric,'nlIfIpICMPAddRoutes':nlIfIpICMPAddRoutes,'nlIfIpRIPDeltaUpdates':nlIfIpRIPDeltaUpdates,'nlIfIpRIPFullUpdates':nlIfIpRIPFullUpdates,'nlIfIpPriority':nlIfIpPriority,'nlIfIpBAG':nlIfIpBAG,'nlIfIpType':nlIfIpType,'nlIfIpSourceAddress':nlIfIpSourceAddress,'nlIfIpDestAddress':nlIfIpDestAddress,'nlIfIpBroadcastAddress':nlIfIpBroadcastAddress,'nlIfIpLANCard':nlIfIpLANCard,'nlIfIpSourceSub':nlIfIpSourceSub,'nlIfIpDestSub':nlIfIpDestSub,'nlIfIpSVCRetryTimer':nlIfIpSVCRetryTimer,'nlIfIpSVCIdleTimer':nlIfIpSVCIdleTimer,'nlIfIpMaxSVC':nlIfIpMaxSVC,'nlIfIpPVCConnection':nlIfIpPVCConnection,'nlIfIpSourceRlp':nlIfIpSourceRlp,'nlIfIpSourcePort':nlIfIpSourcePort,'nlIfIpSourceDLCI':nlIfIpSourceDLCI,'nlIfIpRIPSupport':nlIfIpRIPSupport,'nlIfIpInverseARP':nlIfIpInverseARP,'nlIfIpProxyARP':nlIfIpProxyARP,'nlIfIpUnnumberedIf':nlIfIpUnnumberedIf,'nlIfIpRowStatus':nlIfIpRowStatus,'nlIfIpSecondaryAddrTable':nlIfIpSecondaryAddrTable,'nlIfIpSecondaryAddrEntry':nlIfIpSecondaryAddrEntry,_Ax:nlIfIpSecondaryAddrSequence,'nlIfIpSecondaryAddrNetworkMask':nlIfIpSecondaryAddrNetworkMask,'nlIfIpSecondaryAddrRouteMetric':nlIfIpSecondaryAddrRouteMetric,'nlIfIpSecondaryAddrSourceAddress':nlIfIpSecondaryAddrSourceAddress,'nlIfIpSecondaryAddrBroadcastAddress':nlIfIpSecondaryAddrBroadcastAddress,'nlIfIpSecondaryAddrRIPSupport':nlIfIpSecondaryAddrRIPSupport,'nlIfIpSecondaryAddrRowStatus':nlIfIpSecondaryAddrRowStatus,'nlIfVoiceInterfaces':nlIfVoiceInterfaces,'nlIfVoiceTable':nlIfVoiceTable,'nlIfVoiceEntry':nlIfVoiceEntry,_Ay:nlIfVoiceInterface,'nlIfVoicePeerNodeType':nlIfVoicePeerNodeType,'nlIfVoicePeerNodeNumber':nlIfVoicePeerNodeNumber,'nlIfVoicePeerNodePort':nlIfVoicePeerNodePort,'nlIfVoiceLocalNodeNumber':nlIfVoiceLocalNodeNumber,'nlIfVoiceLocalNodePort':nlIfVoiceLocalNodePort,'nlIfVoiceFrameRelayRlp':nlIfVoiceFrameRelayRlp,'nlIfVoiceFrameRelayPort':nlIfVoiceFrameRelayPort,'nlIfVoiceFrameRelayDLCI':nlIfVoiceFrameRelayDLCI,'nlIfVoiceEnableFragment':nlIfVoiceEnableFragment,'nlIfVoiceRowStatus':nlIfVoiceRowStatus,'subscriber':subscriber,'nlLocalSubscriberTable':nlLocalSubscriberTable,'nlLocalSubscriberEntry':nlLocalSubscriberEntry,_i:nlLocalSubscriberId,'nlLocalSubscriberName':nlLocalSubscriberName,'nlLocalSubscriberAlgorithm':nlLocalSubscriberAlgorithm,'nlLocalSubscriberSystematicRedirect':nlLocalSubscriberSystematicRedirect,'nlLocalSubscriberRedirectBusy':nlLocalSubscriberRedirectBusy,'nlLocalSubscriberRedirectOO':nlLocalSubscriberRedirectOO,'nlLocalSubscriberPriority':nlLocalSubscriberPriority,'nlLocalSubscriberRowStatus':nlLocalSubscriberRowStatus,'nlLocalSubscriberRouteTable':nlLocalSubscriberRouteTable,'nlLocalSubscriberRouteEntry':nlLocalSubscriberRouteEntry,_Az:nlLocalSubscriberRouteIndex,'nlLocalSubscriberRouteConf':nlLocalSubscriberRouteConf,'nlLocalSubscriberRouteLP':nlLocalSubscriberRouteLP,'nlLocalSubscriberRoutePort':nlLocalSubscriberRoutePort,'nlLocalSubscriberRouteRowStatus':nlLocalSubscriberRouteRowStatus,'nlLocalSubscriberRedirTable':nlLocalSubscriberRedirTable,'nlLocalSubscriberRedirEntry':nlLocalSubscriberRedirEntry,_A_:nlLocalSubscriberRedirIndex,'nlLocalSubscriberRedirAddr':nlLocalSubscriberRedirAddr,'nlLocalSubscriberRedirRowStatus':nlLocalSubscriberRedirRowStatus,_q:llc2,'nlLlc2HostTable':nlLlc2HostTable,'nlLlc2HostEntry':nlLlc2HostEntry,_k:nlLlc2HostIndex,'nlLlc2HostMACAddress':nlLlc2HostMACAddress,'nlLlc2HostSessionType':nlLlc2HostSessionType,'nlLlc2HostT1ReplyTimer':nlLlc2HostT1ReplyTimer,'nlLlc2HostT2RecvAckTimer':nlLlc2HostT2RecvAckTimer,'nlLlc2HostTiInactivityTimer':nlLlc2HostTiInactivityTimer,'nlLlc2HostN3NumberLPDUs':nlLlc2HostN3NumberLPDUs,'nlLlc2HostTwNumberOutstanding':nlLlc2HostTwNumberOutstanding,'nlLlc2HostN2ExpiredT1LPDUCount':nlLlc2HostN2ExpiredT1LPDUCount,'nlLlc2HostPriority':nlLlc2HostPriority,'nlLlc2HostBAG':nlLlc2HostBAG,'nlLlc2HostRoutingSubscriberId':nlLlc2HostRoutingSubscriberId,'nlLlc2HostSrcMACAddressMask':nlLlc2HostSrcMACAddressMask,'nlLlc2HostAccess':nlLlc2HostAccess,'nlLlc2HostRowStatus':nlLlc2HostRowStatus,'nlLlc2HostInterface':nlLlc2HostInterface,_j:nlLlc2HostGroup,'nlLlc2TermConnectionTable':nlLlc2TermConnectionTable,'nlLlc2TermConnectionEntry':nlLlc2TermConnectionEntry,_B0:nlLlc2TermConnectionSequence,'nlLlc2TermConnectionHSAP':nlLlc2TermConnectionHSAP,'nlLlc2TermConnectionLocalSubscriberId':nlLlc2TermConnectionLocalSubscriberId,'nlLlc2TermConnectionRemoteSubscriberId':nlLlc2TermConnectionRemoteSubscriberId,'nlLlc2TermConnectionRowStatus':nlLlc2TermConnectionRowStatus,'nlLlc2OrigConnectionTable':nlLlc2OrigConnectionTable,'nlLlc2OrigConnectionEntry':nlLlc2OrigConnectionEntry,_B1:nlLlc2OrigConnectionSequence,'nlLlc2OrigConnectionHSAP':nlLlc2OrigConnectionHSAP,'nlLlc2OrigConnectionType':nlLlc2OrigConnectionType,'nlLlc2OrigConnectionLocalSubscriberId':nlLlc2OrigConnectionLocalSubscriberId,'nlLlc2OrigConnectionRemoteSubscriberId':nlLlc2OrigConnectionRemoteSubscriberId,'nlLlc2OrigConnectionIDBLK':nlLlc2OrigConnectionIDBLK,'nlLlc2OrigConnectionIDNUM':nlLlc2OrigConnectionIDNUM,'nlLlc2OrigConnectionMAXDATA':nlLlc2OrigConnectionMAXDATA,'nlLlc2OrigConnectionMAXIN':nlLlc2OrigConnectionMAXIN,'nlLlc2OrigConnectionRowStatus':nlLlc2OrigConnectionRowStatus,'nlLlc2NextHostNumber':nlLlc2NextHostNumber,'status':status,'pinStatusTable':pinStatusTable,'portPinEntry':portPinEntry,_B2:portPinRlp,_B3:portPinPort,'portPinStatus':portPinStatus,'statistics':statistics,'statGroup':statGroup,'rlpStatsTable':rlpStatsTable,'rlpStatsEntry':rlpStatsEntry,_B4:rlpStatsIndex,'rlpStatsQMessages':rlpStatsQMessages,'rlpStatsUsedBuffers':rlpStatsUsedBuffers,'rlpStatsInFrames':rlpStatsInFrames,'rlpStatsOutFrames':rlpStatsOutFrames,'rlpStatsFrameRejects':rlpStatsFrameRejects,'rlpStatsFrameRetransmits':rlpStatsFrameRetransmits,'portStatsTable':portStatsTable,'portStatsEntry':portStatsEntry,_B5:portStatsRlpIndex,_B6:portStatsIndex,'portStatsInFrames':portStatsInFrames,'portStatsOutFrames':portStatsOutFrames,'portStatsFrameRetrans':portStatsFrameRetrans,'portStatsFCSErrors':portStatsFCSErrors,'portStatsLogicalRejects':portStatsLogicalRejects,'portStatsInPercentUtils':portStatsInPercentUtils,'portStatsOutPercentUtils':portStatsOutPercentUtils,'statFrame':statFrame,'frStatsTable':frStatsTable,'frStatsEntry':frStatsEntry,_B7:frStatsRlpIndex,_B8:frStatsPortIndex,'frStatsTxDEFrames':frStatsTxDEFrames,'frStatsRxDEFrames':frStatsRxDEFrames,'frStatsTxFECNFrames':frStatsTxFECNFrames,'frStatsRxFECNFrames':frStatsRxFECNFrames,'frStatsTxBECNFrames':frStatsTxBECNFrames,'frStatsRxBECNFrames':frStatsRxBECNFrames,'frStatsTxLMIFrames':frStatsTxLMIFrames,'frStatsRxLMIFrames':frStatsRxLMIFrames,'frStatsTxANXDFrames':frStatsTxANXDFrames,'frStatsRxANXDFrames':frStatsRxANXDFrames,'frStatsTotDiscFrames':frStatsTotDiscFrames,'x25TxStatsTable':x25TxStatsTable,'x25TxStatsEntry':x25TxStatsEntry,_B9:x25TxRlpIndex,_BA:x25TxPortIndex,'x25TxSABMFrames':x25TxSABMFrames,'x25TxUAFrames':x25TxUAFrames,'x25TxDISCFrames':x25TxDISCFrames,'x25TxDMFrames':x25TxDMFrames,'x25TxFRMRFrames':x25TxFRMRFrames,'x25TxREJFrames':x25TxREJFrames,'x25TxRRFrames':x25TxRRFrames,'x25TxRNRFrames':x25TxRNRFrames,'x25TxINFOFrames':x25TxINFOFrames,'x25RxStatsTable':x25RxStatsTable,'x25RxStatsEntry':x25RxStatsEntry,_BB:x25RxRlpIndex,_BC:x25RxPortIndex,'x25RxSABMFrames':x25RxSABMFrames,'x25RxUAFrames':x25RxUAFrames,'x25RxDISCFrames':x25RxDISCFrames,'x25RxDMFrames':x25RxDMFrames,'x25RxFRMRFrames':x25RxFRMRFrames,'x25RxREJFrames':x25RxREJFrames,'x25RxRRFrames':x25RxRRFrames,'x25RxRNRFrames':x25RxRNRFrames,'x25RxINFOFrames':x25RxINFOFrames,'statBag':statBag,'statIp':statIp,'statT1':statT1,'t1StatsTable':t1StatsTable,'t1StatsEntry':t1StatsEntry,_BD:t1StatsRlpIndex,_BE:t1StatsPortIndex,'t1StatsRcvFrames':t1StatsRcvFrames,'t1StatsXmitFrames':t1StatsXmitFrames,'t1StatsLCVCnt':t1StatsLCVCnt,'t1StatsPCVRErrs':t1StatsPCVRErrs,'t1StatsOOSCnt':t1StatsOOSCnt,'t1StatsBlueAlarms':t1StatsBlueAlarms,'t1StatsYellowAlarms':t1StatsYellowAlarms,'t1StatsRedAlarms':t1StatsRedAlarms,'t1StatsRcvUsage':t1StatsRcvUsage,'t1StatsXmitUsage':t1StatsXmitUsage,'t1StatsXmitAbortFrames':t1StatsXmitAbortFrames,'t1StatsRcvAbortFrames':t1StatsRcvAbortFrames,'t1StatsRcvOverruns':t1StatsRcvOverruns,'t1StatsRcvErrors':t1StatsRcvErrors,'t1StatsRcvChannelErrors':t1StatsRcvChannelErrors,'statDS0A':statDS0A,'ds0aStatsTable':ds0aStatsTable,'ds0aStatsEntry':ds0aStatsEntry,_BF:ds0aStatsRlpIndex,_BG:ds0aStatsPortIndex,_BH:ds0aStatsChannelIndex,'ds0aStatsXmitFrames':ds0aStatsXmitFrames,'ds0aStatsRcvFrames':ds0aStatsRcvFrames,'ds0aStatsRcvAbortFrames':ds0aStatsRcvAbortFrames,'ds0aStatsRcvOverruns':ds0aStatsRcvOverruns,'ds0aStatsRcvErrors':ds0aStatsRcvErrors,'statVoice':statVoice,'voiceStatsTable':voiceStatsTable,'voiceStatsEntry':voiceStatsEntry,_BI:voiceStatsRlpIndex,_BJ:voiceStatsPortIndex,'voiceStatsRxCalls':voiceStatsRxCalls,'voiceStatsTxCalls':voiceStatsTxCalls,'voiceStatsRxCallsAccepts':voiceStatsRxCallsAccepts,'voiceStatsTxCallsAccepts':voiceStatsTxCallsAccepts,'voiceStatsRxClears':voiceStatsRxClears,'voiceStatsTxClears':voiceStatsTxClears,'voiceStatsBusyCalls':voiceStatsBusyCalls,'voiceStatsCallTimeouts':voiceStatsCallTimeouts,'voiceStatsRxCongestions':voiceStatsRxCongestions,'voiceStatsTxCongestions':voiceStatsTxCongestions,'statThresh':statThresh,'rlpThreshTable':rlpThreshTable,'rlpThreshEntry':rlpThreshEntry,_BK:rlpThreshRlpIndex,'rlpThreshPercntBufInUse':rlpThreshPercntBufInUse,'rlpThreshMsgQueueLen':rlpThreshMsgQueueLen,'rlpThreshRxFramesPerSec':rlpThreshRxFramesPerSec,'rlpThreshTxFramesPerSec':rlpThreshTxFramesPerSec,'rlpThreshRejFramesPerSec':rlpThreshRejFramesPerSec,'rlpThreshRtxFramesPerSec':rlpThreshRtxFramesPerSec,'portThreshTable':portThreshTable,'portThreshEntry':portThreshEntry,_BL:portThreshRlpIndex,_BM:portThreshIndex,'portThreshRxFramesPerSec':portThreshRxFramesPerSec,'portThreshTxFramesPerSec':portThreshTxFramesPerSec,'portThreshRtxFramesPerSec':portThreshRtxFramesPerSec,'portThreshFCSErrPerSec':portThreshFCSErrPerSec,'portThreshLogRejPerSec':portThreshLogRejPerSec,'portThreshTxErrorRatio':portThreshTxErrorRatio,'portThreshRxErrorRatio':portThreshRxErrorRatio,'portThreshTxPercentUtl':portThreshTxPercentUtl,'portThreshRxPercentUtl':portThreshRxPercentUtl,'bridge':bridge,'bridgeAdminVirtualLANID':bridgeAdminVirtualLANID,'bridgeOperVirtualLANID':bridgeOperVirtualLANID,'bridgeEnabled':bridgeEnabled,'bridgeMaxSizeForwardingTable':bridgeMaxSizeForwardingTable,'bridgeIPEnabled':bridgeIPEnabled,'bridgeIPXEnabled':bridgeIPXEnabled,'bridgeAdminSRBID':bridgeAdminSRBID,'bridgeOperSRBID':bridgeOperSRBID,'bridgeDefaultEthernetFrameType':bridgeDefaultEthernetFrameType,'ipNl':ipNl,'nlIpDefaultRIPVersion':nlIpDefaultRIPVersion,_W:voice,'voiceSystemVoiceNodeNum':voiceSystemVoiceNodeNum,'voiceSystemRingVolFreq':voiceSystemRingVolFreq,'voiceSystemCountryCode':voiceSystemCountryCode,'voiceSystemDialDigits':voiceSystemDialDigits,'voiceSystemVoiceRatesMin':voiceSystemVoiceRatesMin,'voiceSystemVoiceRatesMax':voiceSystemVoiceRatesMax,'voiceSystemExtDialDigits':voiceSystemExtDialDigits,'voiceSpeedDialTable':voiceSpeedDialTable,'voiceSpeedDialEntry':voiceSpeedDialEntry,_BN:voiceSpeedDialDigits,'voiceSpeedDialLongDialMap':voiceSpeedDialLongDialMap,'voiceSpeedDialExtDialStr':voiceSpeedDialExtDialStr,'voiceSpeedDialRowStatus':voiceSpeedDialRowStatus})