_AQ='jnxSvcServIdiceGroup'
_AP='jnxSvcFlowTableAggStatsGroup'
_AO='jnxSvcServidProtInsUriErrNoRes'
_AN='jnxSvcServidProtInsErrParseTx'
_AM='jnxSvcServidProtInsUriErrTooLong'
_AL='jnxSvcServidProtInsUriErrProcess'
_AK='jnxSvcTransactionHttpIdleFreed'
_AJ='jnxSvcTransactionHttpFreed'
_AI='jnxSvcTransactionHttpMaximum'
_AH='jnxSvcTransactionHttpCreated'
_AG='jnxSvcTransactionWapIdleFreed'
_AF='jnxSvcTransactionWapFreed'
_AE='jnxSvcTransactionWapMaximum'
_AD='jnxSvcTransactionWapCreated'
_AC='jnxSvcServIdProtInsFailCfgState'
_AB='jnxSvcServIdHeadExFailCfgState'
_AA='jnxSvcServIdErrHTTPTxn'
_A9='jnxSvcServIdErrWAPTxn'
_A8='jnxSvcServIdWAPInvalidTxn'
_A7='jnxSvcServIdPktTcpMalform'
_A6='jnxSvcServIdProtInsWapUriMtch'
_A5='jnxSvcServIdProtInsWapUri'
_A4='jnxSvcServIdProtInsHttpUriMtch'
_A3='jnxSvcServIdProtInsHttpUri'
_A2='jnxSvcServIdProtInsFlowProtIdent'
_A1='jnxSvcServIdProtInsFlowInsp'
_A0='jnxSvcServIdProtInsByte'
_z='jnxSvcServIdProtInsPkt'
_y='jnxSvcServIdProtFlow'
_x='jnxSvcServIdHeadExWapProtoReq'
_w='jnxSvcServIdHeadExHttpProtoReq'
_v='jnxSvcServIdHeadExProtoReq'
_u='jnxSvcServIdHeadExFlowMtch'
_t='jnxSvcServIdHeadExFlow'
_s='jnxSvcServIdHeadExByte'
_r='jnxSvcServIdHeadExPkt'
_q='jnxSvcServIdErrByte'
_p='jnxSvcServIdErrPkt'
_o='jnxSvcServIdByte'
_n='jnxSvcServIdPkt'
_m='jnxSvcAggFlowUdpByteErr'
_l='jnxSvcAggFlowUdpByte'
_k='jnxSvcAggFlowUdpPktErrBadFlow'
_j='jnxSvcAggFlowUdpPktErr'
_i='jnxSvcAggFlowUdpPkt'
_h='jnxSvcAggFlowTcpByteErr'
_g='jnxSvcAggFlowTcpByte'
_f='jnxSvcAggFlowTcpPktErrBadFlow'
_e='jnxSvcAggFlowTcpPktErr'
_d='jnxSvcAggFlowTcpPkt'
_c='jnxSvcAggFlowIcmpByteErr'
_b='jnxSvcAggFlowIcmpByte'
_a='jnxSvcAggFlowIcmpPktErrBadFlow'
_Z='jnxSvcAggFlowIcmpPktErr'
_Y='jnxSvcAggFlowIcmpPkt'
_X='jnxSvcAggFlowByteErr'
_W='jnxSvcAggFlowByte'
_V='jnxSvcAggFlowPktErr'
_U='jnxSvcAggFlowPkt'
_T='jnxSvcAggFlowUdpIdleFreed'
_S='jnxSvcAggFlowUdpFreed'
_R='jnxSvcAggFlowUdpCreated'
_Q='jnxSvcAggFlowUdpMaximum'
_P='jnxSvcAggFlowUdp'
_O='jnxSvcAggFlowTcpIdleFreed'
_N='jnxSvcAggFlowTcpFreed'
_M='jnxSvcAggFlowTcpCreated'
_L='jnxSvcAggFlowTcpMaximum'
_K='jnxSvcAggFlowTcp'
_J='jnxSvcAggFlowIdleFreed'
_I='jnxSvcAggFlowFreed'
_H='jnxSvcAggFlowCreated'
_G='jnxSvcAggFlowMaximum'
_F='jnxSvcAggFlow'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='JUNIPER-Services-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxServicesInfoMib=ModuleIdentity((1,3,6,1,4,1,2636,3,27))
if mibBuilder.loadTexts:jnxServicesInfoMib.setRevisions(('2004-01-30 00:00',))
_JnxSvcFlowTableAggStatsTable_Object=MibTable
jnxSvcFlowTableAggStatsTable=_JnxSvcFlowTableAggStatsTable_Object((1,3,6,1,4,1,2636,3,27,1))
if mibBuilder.loadTexts:jnxSvcFlowTableAggStatsTable.setStatus(_A)
_JnxSvcFlowTableAggStatsEntry_Object=MibTableRow
jnxSvcFlowTableAggStatsEntry=_JnxSvcFlowTableAggStatsEntry_Object((1,3,6,1,4,1,2636,3,27,1,1))
jnxSvcFlowTableAggStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:jnxSvcFlowTableAggStatsEntry.setStatus(_A)
_JnxSvcAggFlow_Type=Gauge32
_JnxSvcAggFlow_Object=MibTableColumn
jnxSvcAggFlow=_JnxSvcAggFlow_Object((1,3,6,1,4,1,2636,3,27,1,1,1),_JnxSvcAggFlow_Type())
jnxSvcAggFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlow.setStatus(_A)
_JnxSvcAggFlowMaximum_Type=Gauge32
_JnxSvcAggFlowMaximum_Object=MibTableColumn
jnxSvcAggFlowMaximum=_JnxSvcAggFlowMaximum_Object((1,3,6,1,4,1,2636,3,27,1,1,2),_JnxSvcAggFlowMaximum_Type())
jnxSvcAggFlowMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowMaximum.setStatus(_A)
_JnxSvcAggFlowCreated_Type=Counter64
_JnxSvcAggFlowCreated_Object=MibTableColumn
jnxSvcAggFlowCreated=_JnxSvcAggFlowCreated_Object((1,3,6,1,4,1,2636,3,27,1,1,3),_JnxSvcAggFlowCreated_Type())
jnxSvcAggFlowCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowCreated.setStatus(_A)
_JnxSvcAggFlowFreed_Type=Counter64
_JnxSvcAggFlowFreed_Object=MibTableColumn
jnxSvcAggFlowFreed=_JnxSvcAggFlowFreed_Object((1,3,6,1,4,1,2636,3,27,1,1,4),_JnxSvcAggFlowFreed_Type())
jnxSvcAggFlowFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowFreed.setStatus(_A)
_JnxSvcAggFlowIdleFreed_Type=Counter64
_JnxSvcAggFlowIdleFreed_Object=MibTableColumn
jnxSvcAggFlowIdleFreed=_JnxSvcAggFlowIdleFreed_Object((1,3,6,1,4,1,2636,3,27,1,1,5),_JnxSvcAggFlowIdleFreed_Type())
jnxSvcAggFlowIdleFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowIdleFreed.setStatus(_A)
_JnxSvcAggFlowTcp_Type=Gauge32
_JnxSvcAggFlowTcp_Object=MibTableColumn
jnxSvcAggFlowTcp=_JnxSvcAggFlowTcp_Object((1,3,6,1,4,1,2636,3,27,1,1,6),_JnxSvcAggFlowTcp_Type())
jnxSvcAggFlowTcp.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcp.setStatus(_A)
_JnxSvcAggFlowTcpMaximum_Type=Gauge32
_JnxSvcAggFlowTcpMaximum_Object=MibTableColumn
jnxSvcAggFlowTcpMaximum=_JnxSvcAggFlowTcpMaximum_Object((1,3,6,1,4,1,2636,3,27,1,1,7),_JnxSvcAggFlowTcpMaximum_Type())
jnxSvcAggFlowTcpMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpMaximum.setStatus(_A)
_JnxSvcAggFlowTcpCreated_Type=Counter64
_JnxSvcAggFlowTcpCreated_Object=MibTableColumn
jnxSvcAggFlowTcpCreated=_JnxSvcAggFlowTcpCreated_Object((1,3,6,1,4,1,2636,3,27,1,1,8),_JnxSvcAggFlowTcpCreated_Type())
jnxSvcAggFlowTcpCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpCreated.setStatus(_A)
_JnxSvcAggFlowTcpFreed_Type=Counter64
_JnxSvcAggFlowTcpFreed_Object=MibTableColumn
jnxSvcAggFlowTcpFreed=_JnxSvcAggFlowTcpFreed_Object((1,3,6,1,4,1,2636,3,27,1,1,9),_JnxSvcAggFlowTcpFreed_Type())
jnxSvcAggFlowTcpFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpFreed.setStatus(_A)
_JnxSvcAggFlowTcpIdleFreed_Type=Counter64
_JnxSvcAggFlowTcpIdleFreed_Object=MibTableColumn
jnxSvcAggFlowTcpIdleFreed=_JnxSvcAggFlowTcpIdleFreed_Object((1,3,6,1,4,1,2636,3,27,1,1,10),_JnxSvcAggFlowTcpIdleFreed_Type())
jnxSvcAggFlowTcpIdleFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpIdleFreed.setStatus(_A)
_JnxSvcAggFlowUdp_Type=Gauge32
_JnxSvcAggFlowUdp_Object=MibTableColumn
jnxSvcAggFlowUdp=_JnxSvcAggFlowUdp_Object((1,3,6,1,4,1,2636,3,27,1,1,11),_JnxSvcAggFlowUdp_Type())
jnxSvcAggFlowUdp.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdp.setStatus(_A)
_JnxSvcAggFlowUdpMaximum_Type=Gauge32
_JnxSvcAggFlowUdpMaximum_Object=MibTableColumn
jnxSvcAggFlowUdpMaximum=_JnxSvcAggFlowUdpMaximum_Object((1,3,6,1,4,1,2636,3,27,1,1,12),_JnxSvcAggFlowUdpMaximum_Type())
jnxSvcAggFlowUdpMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpMaximum.setStatus(_A)
_JnxSvcAggFlowUdpCreated_Type=Counter64
_JnxSvcAggFlowUdpCreated_Object=MibTableColumn
jnxSvcAggFlowUdpCreated=_JnxSvcAggFlowUdpCreated_Object((1,3,6,1,4,1,2636,3,27,1,1,13),_JnxSvcAggFlowUdpCreated_Type())
jnxSvcAggFlowUdpCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpCreated.setStatus(_A)
_JnxSvcAggFlowUdpFreed_Type=Counter64
_JnxSvcAggFlowUdpFreed_Object=MibTableColumn
jnxSvcAggFlowUdpFreed=_JnxSvcAggFlowUdpFreed_Object((1,3,6,1,4,1,2636,3,27,1,1,14),_JnxSvcAggFlowUdpFreed_Type())
jnxSvcAggFlowUdpFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpFreed.setStatus(_A)
_JnxSvcAggFlowUdpIdleFreed_Type=Counter64
_JnxSvcAggFlowUdpIdleFreed_Object=MibTableColumn
jnxSvcAggFlowUdpIdleFreed=_JnxSvcAggFlowUdpIdleFreed_Object((1,3,6,1,4,1,2636,3,27,1,1,15),_JnxSvcAggFlowUdpIdleFreed_Type())
jnxSvcAggFlowUdpIdleFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpIdleFreed.setStatus(_A)
_JnxSvcAggFlowPkt_Type=Counter64
_JnxSvcAggFlowPkt_Object=MibTableColumn
jnxSvcAggFlowPkt=_JnxSvcAggFlowPkt_Object((1,3,6,1,4,1,2636,3,27,1,1,16),_JnxSvcAggFlowPkt_Type())
jnxSvcAggFlowPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowPkt.setStatus(_A)
_JnxSvcAggFlowPktErr_Type=Counter64
_JnxSvcAggFlowPktErr_Object=MibTableColumn
jnxSvcAggFlowPktErr=_JnxSvcAggFlowPktErr_Object((1,3,6,1,4,1,2636,3,27,1,1,17),_JnxSvcAggFlowPktErr_Type())
jnxSvcAggFlowPktErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowPktErr.setStatus(_A)
_JnxSvcAggFlowByte_Type=Counter64
_JnxSvcAggFlowByte_Object=MibTableColumn
jnxSvcAggFlowByte=_JnxSvcAggFlowByte_Object((1,3,6,1,4,1,2636,3,27,1,1,18),_JnxSvcAggFlowByte_Type())
jnxSvcAggFlowByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowByte.setStatus(_A)
_JnxSvcAggFlowByteErr_Type=Counter64
_JnxSvcAggFlowByteErr_Object=MibTableColumn
jnxSvcAggFlowByteErr=_JnxSvcAggFlowByteErr_Object((1,3,6,1,4,1,2636,3,27,1,1,19),_JnxSvcAggFlowByteErr_Type())
jnxSvcAggFlowByteErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowByteErr.setStatus(_A)
_JnxSvcAggFlowIcmpPkt_Type=Counter64
_JnxSvcAggFlowIcmpPkt_Object=MibTableColumn
jnxSvcAggFlowIcmpPkt=_JnxSvcAggFlowIcmpPkt_Object((1,3,6,1,4,1,2636,3,27,1,1,20),_JnxSvcAggFlowIcmpPkt_Type())
jnxSvcAggFlowIcmpPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowIcmpPkt.setStatus(_A)
_JnxSvcAggFlowIcmpPktErr_Type=Counter64
_JnxSvcAggFlowIcmpPktErr_Object=MibTableColumn
jnxSvcAggFlowIcmpPktErr=_JnxSvcAggFlowIcmpPktErr_Object((1,3,6,1,4,1,2636,3,27,1,1,21),_JnxSvcAggFlowIcmpPktErr_Type())
jnxSvcAggFlowIcmpPktErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowIcmpPktErr.setStatus(_A)
_JnxSvcAggFlowIcmpPktErrBadFlow_Type=Counter64
_JnxSvcAggFlowIcmpPktErrBadFlow_Object=MibTableColumn
jnxSvcAggFlowIcmpPktErrBadFlow=_JnxSvcAggFlowIcmpPktErrBadFlow_Object((1,3,6,1,4,1,2636,3,27,1,1,22),_JnxSvcAggFlowIcmpPktErrBadFlow_Type())
jnxSvcAggFlowIcmpPktErrBadFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowIcmpPktErrBadFlow.setStatus(_A)
_JnxSvcAggFlowIcmpByte_Type=Counter64
_JnxSvcAggFlowIcmpByte_Object=MibTableColumn
jnxSvcAggFlowIcmpByte=_JnxSvcAggFlowIcmpByte_Object((1,3,6,1,4,1,2636,3,27,1,1,23),_JnxSvcAggFlowIcmpByte_Type())
jnxSvcAggFlowIcmpByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowIcmpByte.setStatus(_A)
_JnxSvcAggFlowIcmpByteErr_Type=Counter64
_JnxSvcAggFlowIcmpByteErr_Object=MibTableColumn
jnxSvcAggFlowIcmpByteErr=_JnxSvcAggFlowIcmpByteErr_Object((1,3,6,1,4,1,2636,3,27,1,1,24),_JnxSvcAggFlowIcmpByteErr_Type())
jnxSvcAggFlowIcmpByteErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowIcmpByteErr.setStatus(_A)
_JnxSvcAggFlowTcpPkt_Type=Counter64
_JnxSvcAggFlowTcpPkt_Object=MibTableColumn
jnxSvcAggFlowTcpPkt=_JnxSvcAggFlowTcpPkt_Object((1,3,6,1,4,1,2636,3,27,1,1,25),_JnxSvcAggFlowTcpPkt_Type())
jnxSvcAggFlowTcpPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpPkt.setStatus(_A)
_JnxSvcAggFlowTcpPktErr_Type=Counter64
_JnxSvcAggFlowTcpPktErr_Object=MibTableColumn
jnxSvcAggFlowTcpPktErr=_JnxSvcAggFlowTcpPktErr_Object((1,3,6,1,4,1,2636,3,27,1,1,26),_JnxSvcAggFlowTcpPktErr_Type())
jnxSvcAggFlowTcpPktErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpPktErr.setStatus(_A)
_JnxSvcAggFlowTcpPktErrBadFlow_Type=Counter64
_JnxSvcAggFlowTcpPktErrBadFlow_Object=MibTableColumn
jnxSvcAggFlowTcpPktErrBadFlow=_JnxSvcAggFlowTcpPktErrBadFlow_Object((1,3,6,1,4,1,2636,3,27,1,1,27),_JnxSvcAggFlowTcpPktErrBadFlow_Type())
jnxSvcAggFlowTcpPktErrBadFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpPktErrBadFlow.setStatus(_A)
_JnxSvcAggFlowTcpByte_Type=Counter64
_JnxSvcAggFlowTcpByte_Object=MibTableColumn
jnxSvcAggFlowTcpByte=_JnxSvcAggFlowTcpByte_Object((1,3,6,1,4,1,2636,3,27,1,1,28),_JnxSvcAggFlowTcpByte_Type())
jnxSvcAggFlowTcpByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpByte.setStatus(_A)
_JnxSvcAggFlowTcpByteErr_Type=Counter64
_JnxSvcAggFlowTcpByteErr_Object=MibTableColumn
jnxSvcAggFlowTcpByteErr=_JnxSvcAggFlowTcpByteErr_Object((1,3,6,1,4,1,2636,3,27,1,1,29),_JnxSvcAggFlowTcpByteErr_Type())
jnxSvcAggFlowTcpByteErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowTcpByteErr.setStatus(_A)
_JnxSvcAggFlowUdpPkt_Type=Counter64
_JnxSvcAggFlowUdpPkt_Object=MibTableColumn
jnxSvcAggFlowUdpPkt=_JnxSvcAggFlowUdpPkt_Object((1,3,6,1,4,1,2636,3,27,1,1,30),_JnxSvcAggFlowUdpPkt_Type())
jnxSvcAggFlowUdpPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpPkt.setStatus(_A)
_JnxSvcAggFlowUdpPktErr_Type=Counter64
_JnxSvcAggFlowUdpPktErr_Object=MibTableColumn
jnxSvcAggFlowUdpPktErr=_JnxSvcAggFlowUdpPktErr_Object((1,3,6,1,4,1,2636,3,27,1,1,31),_JnxSvcAggFlowUdpPktErr_Type())
jnxSvcAggFlowUdpPktErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpPktErr.setStatus(_A)
_JnxSvcAggFlowUdpPktErrBadFlow_Type=Counter64
_JnxSvcAggFlowUdpPktErrBadFlow_Object=MibTableColumn
jnxSvcAggFlowUdpPktErrBadFlow=_JnxSvcAggFlowUdpPktErrBadFlow_Object((1,3,6,1,4,1,2636,3,27,1,1,32),_JnxSvcAggFlowUdpPktErrBadFlow_Type())
jnxSvcAggFlowUdpPktErrBadFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpPktErrBadFlow.setStatus(_A)
_JnxSvcAggFlowUdpByte_Type=Counter64
_JnxSvcAggFlowUdpByte_Object=MibTableColumn
jnxSvcAggFlowUdpByte=_JnxSvcAggFlowUdpByte_Object((1,3,6,1,4,1,2636,3,27,1,1,33),_JnxSvcAggFlowUdpByte_Type())
jnxSvcAggFlowUdpByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpByte.setStatus(_A)
_JnxSvcAggFlowUdpByteErr_Type=Counter64
_JnxSvcAggFlowUdpByteErr_Object=MibTableColumn
jnxSvcAggFlowUdpByteErr=_JnxSvcAggFlowUdpByteErr_Object((1,3,6,1,4,1,2636,3,27,1,1,34),_JnxSvcAggFlowUdpByteErr_Type())
jnxSvcAggFlowUdpByteErr.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcAggFlowUdpByteErr.setStatus(_A)
_JnxSvcServIdTable_Object=MibTable
jnxSvcServIdTable=_JnxSvcServIdTable_Object((1,3,6,1,4,1,2636,3,27,2))
if mibBuilder.loadTexts:jnxSvcServIdTable.setStatus(_A)
_JnxSvcServIdTableEntry_Object=MibTableRow
jnxSvcServIdTableEntry=_JnxSvcServIdTableEntry_Object((1,3,6,1,4,1,2636,3,27,2,1))
jnxSvcServIdTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:jnxSvcServIdTableEntry.setStatus(_A)
_JnxSvcServIdPkt_Type=Counter64
_JnxSvcServIdPkt_Object=MibTableColumn
jnxSvcServIdPkt=_JnxSvcServIdPkt_Object((1,3,6,1,4,1,2636,3,27,2,1,1),_JnxSvcServIdPkt_Type())
jnxSvcServIdPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdPkt.setStatus(_A)
_JnxSvcServIdByte_Type=Counter64
_JnxSvcServIdByte_Object=MibTableColumn
jnxSvcServIdByte=_JnxSvcServIdByte_Object((1,3,6,1,4,1,2636,3,27,2,1,2),_JnxSvcServIdByte_Type())
jnxSvcServIdByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdByte.setStatus(_A)
_JnxSvcServIdErrPkt_Type=Counter64
_JnxSvcServIdErrPkt_Object=MibTableColumn
jnxSvcServIdErrPkt=_JnxSvcServIdErrPkt_Object((1,3,6,1,4,1,2636,3,27,2,1,3),_JnxSvcServIdErrPkt_Type())
jnxSvcServIdErrPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdErrPkt.setStatus(_A)
_JnxSvcServIdErrByte_Type=Counter64
_JnxSvcServIdErrByte_Object=MibTableColumn
jnxSvcServIdErrByte=_JnxSvcServIdErrByte_Object((1,3,6,1,4,1,2636,3,27,2,1,4),_JnxSvcServIdErrByte_Type())
jnxSvcServIdErrByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdErrByte.setStatus(_A)
_JnxSvcServIdHeadExPkt_Type=Counter64
_JnxSvcServIdHeadExPkt_Object=MibTableColumn
jnxSvcServIdHeadExPkt=_JnxSvcServIdHeadExPkt_Object((1,3,6,1,4,1,2636,3,27,2,1,5),_JnxSvcServIdHeadExPkt_Type())
jnxSvcServIdHeadExPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExPkt.setStatus(_A)
_JnxSvcServIdHeadExByte_Type=Counter64
_JnxSvcServIdHeadExByte_Object=MibTableColumn
jnxSvcServIdHeadExByte=_JnxSvcServIdHeadExByte_Object((1,3,6,1,4,1,2636,3,27,2,1,6),_JnxSvcServIdHeadExByte_Type())
jnxSvcServIdHeadExByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExByte.setStatus(_A)
_JnxSvcServIdHeadExFlow_Type=Counter64
_JnxSvcServIdHeadExFlow_Object=MibTableColumn
jnxSvcServIdHeadExFlow=_JnxSvcServIdHeadExFlow_Object((1,3,6,1,4,1,2636,3,27,2,1,7),_JnxSvcServIdHeadExFlow_Type())
jnxSvcServIdHeadExFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExFlow.setStatus(_A)
_JnxSvcServIdHeadExFlowMtch_Type=Counter64
_JnxSvcServIdHeadExFlowMtch_Object=MibTableColumn
jnxSvcServIdHeadExFlowMtch=_JnxSvcServIdHeadExFlowMtch_Object((1,3,6,1,4,1,2636,3,27,2,1,8),_JnxSvcServIdHeadExFlowMtch_Type())
jnxSvcServIdHeadExFlowMtch.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExFlowMtch.setStatus(_A)
_JnxSvcServIdHeadExProtoReq_Type=Counter64
_JnxSvcServIdHeadExProtoReq_Object=MibTableColumn
jnxSvcServIdHeadExProtoReq=_JnxSvcServIdHeadExProtoReq_Object((1,3,6,1,4,1,2636,3,27,2,1,13),_JnxSvcServIdHeadExProtoReq_Type())
jnxSvcServIdHeadExProtoReq.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExProtoReq.setStatus(_A)
_JnxSvcServIdHeadExHttpProtoReq_Type=Counter64
_JnxSvcServIdHeadExHttpProtoReq_Object=MibTableColumn
jnxSvcServIdHeadExHttpProtoReq=_JnxSvcServIdHeadExHttpProtoReq_Object((1,3,6,1,4,1,2636,3,27,2,1,14),_JnxSvcServIdHeadExHttpProtoReq_Type())
jnxSvcServIdHeadExHttpProtoReq.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExHttpProtoReq.setStatus(_A)
_JnxSvcServIdHeadExWapProtoReq_Type=Counter64
_JnxSvcServIdHeadExWapProtoReq_Object=MibTableColumn
jnxSvcServIdHeadExWapProtoReq=_JnxSvcServIdHeadExWapProtoReq_Object((1,3,6,1,4,1,2636,3,27,2,1,15),_JnxSvcServIdHeadExWapProtoReq_Type())
jnxSvcServIdHeadExWapProtoReq.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExWapProtoReq.setStatus(_A)
_JnxSvcServIdProtFlow_Type=Gauge32
_JnxSvcServIdProtFlow_Object=MibTableColumn
jnxSvcServIdProtFlow=_JnxSvcServIdProtFlow_Object((1,3,6,1,4,1,2636,3,27,2,1,16),_JnxSvcServIdProtFlow_Type())
jnxSvcServIdProtFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtFlow.setStatus(_A)
_JnxSvcServIdProtInsPkt_Type=Counter64
_JnxSvcServIdProtInsPkt_Object=MibTableColumn
jnxSvcServIdProtInsPkt=_JnxSvcServIdProtInsPkt_Object((1,3,6,1,4,1,2636,3,27,2,1,17),_JnxSvcServIdProtInsPkt_Type())
jnxSvcServIdProtInsPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsPkt.setStatus(_A)
_JnxSvcServIdProtInsByte_Type=Counter64
_JnxSvcServIdProtInsByte_Object=MibTableColumn
jnxSvcServIdProtInsByte=_JnxSvcServIdProtInsByte_Object((1,3,6,1,4,1,2636,3,27,2,1,18),_JnxSvcServIdProtInsByte_Type())
jnxSvcServIdProtInsByte.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsByte.setStatus(_A)
_JnxSvcServIdProtInsFlowInsp_Type=Counter64
_JnxSvcServIdProtInsFlowInsp_Object=MibTableColumn
jnxSvcServIdProtInsFlowInsp=_JnxSvcServIdProtInsFlowInsp_Object((1,3,6,1,4,1,2636,3,27,2,1,19),_JnxSvcServIdProtInsFlowInsp_Type())
jnxSvcServIdProtInsFlowInsp.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsFlowInsp.setStatus(_A)
_JnxSvcServIdProtInsFlowProtIdent_Type=Counter64
_JnxSvcServIdProtInsFlowProtIdent_Object=MibTableColumn
jnxSvcServIdProtInsFlowProtIdent=_JnxSvcServIdProtInsFlowProtIdent_Object((1,3,6,1,4,1,2636,3,27,2,1,20),_JnxSvcServIdProtInsFlowProtIdent_Type())
jnxSvcServIdProtInsFlowProtIdent.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsFlowProtIdent.setStatus(_A)
_JnxSvcServIdProtInsHttpUri_Type=Counter64
_JnxSvcServIdProtInsHttpUri_Object=MibTableColumn
jnxSvcServIdProtInsHttpUri=_JnxSvcServIdProtInsHttpUri_Object((1,3,6,1,4,1,2636,3,27,2,1,24),_JnxSvcServIdProtInsHttpUri_Type())
jnxSvcServIdProtInsHttpUri.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsHttpUri.setStatus(_A)
_JnxSvcServIdProtInsHttpUriMtch_Type=Counter64
_JnxSvcServIdProtInsHttpUriMtch_Object=MibTableColumn
jnxSvcServIdProtInsHttpUriMtch=_JnxSvcServIdProtInsHttpUriMtch_Object((1,3,6,1,4,1,2636,3,27,2,1,25),_JnxSvcServIdProtInsHttpUriMtch_Type())
jnxSvcServIdProtInsHttpUriMtch.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsHttpUriMtch.setStatus(_A)
_JnxSvcServIdProtInsWapUri_Type=Counter64
_JnxSvcServIdProtInsWapUri_Object=MibTableColumn
jnxSvcServIdProtInsWapUri=_JnxSvcServIdProtInsWapUri_Object((1,3,6,1,4,1,2636,3,27,2,1,26),_JnxSvcServIdProtInsWapUri_Type())
jnxSvcServIdProtInsWapUri.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsWapUri.setStatus(_A)
_JnxSvcServIdProtInsWapUriMtch_Type=Counter64
_JnxSvcServIdProtInsWapUriMtch_Object=MibTableColumn
jnxSvcServIdProtInsWapUriMtch=_JnxSvcServIdProtInsWapUriMtch_Object((1,3,6,1,4,1,2636,3,27,2,1,27),_JnxSvcServIdProtInsWapUriMtch_Type())
jnxSvcServIdProtInsWapUriMtch.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsWapUriMtch.setStatus(_A)
_JnxSvcServIdPktTcpMalform_Type=Counter64
_JnxSvcServIdPktTcpMalform_Object=MibTableColumn
jnxSvcServIdPktTcpMalform=_JnxSvcServIdPktTcpMalform_Object((1,3,6,1,4,1,2636,3,27,2,1,28),_JnxSvcServIdPktTcpMalform_Type())
jnxSvcServIdPktTcpMalform.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdPktTcpMalform.setStatus(_A)
_JnxSvcServIdWAPInvalidTxn_Type=Counter64
_JnxSvcServIdWAPInvalidTxn_Object=MibTableColumn
jnxSvcServIdWAPInvalidTxn=_JnxSvcServIdWAPInvalidTxn_Object((1,3,6,1,4,1,2636,3,27,2,1,29),_JnxSvcServIdWAPInvalidTxn_Type())
jnxSvcServIdWAPInvalidTxn.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdWAPInvalidTxn.setStatus(_A)
_JnxSvcServIdErrWAPTxn_Type=Counter64
_JnxSvcServIdErrWAPTxn_Object=MibTableColumn
jnxSvcServIdErrWAPTxn=_JnxSvcServIdErrWAPTxn_Object((1,3,6,1,4,1,2636,3,27,2,1,30),_JnxSvcServIdErrWAPTxn_Type())
jnxSvcServIdErrWAPTxn.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdErrWAPTxn.setStatus(_A)
_JnxSvcServIdErrHTTPTxn_Type=Counter64
_JnxSvcServIdErrHTTPTxn_Object=MibTableColumn
jnxSvcServIdErrHTTPTxn=_JnxSvcServIdErrHTTPTxn_Object((1,3,6,1,4,1,2636,3,27,2,1,31),_JnxSvcServIdErrHTTPTxn_Type())
jnxSvcServIdErrHTTPTxn.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdErrHTTPTxn.setStatus(_A)
_JnxSvcServIdHeadExFailCfgState_Type=Counter64
_JnxSvcServIdHeadExFailCfgState_Object=MibTableColumn
jnxSvcServIdHeadExFailCfgState=_JnxSvcServIdHeadExFailCfgState_Object((1,3,6,1,4,1,2636,3,27,2,1,32),_JnxSvcServIdHeadExFailCfgState_Type())
jnxSvcServIdHeadExFailCfgState.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdHeadExFailCfgState.setStatus(_A)
_JnxSvcServIdProtInsFailCfgState_Type=Counter64
_JnxSvcServIdProtInsFailCfgState_Object=MibTableColumn
jnxSvcServIdProtInsFailCfgState=_JnxSvcServIdProtInsFailCfgState_Object((1,3,6,1,4,1,2636,3,27,2,1,33),_JnxSvcServIdProtInsFailCfgState_Type())
jnxSvcServIdProtInsFailCfgState.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServIdProtInsFailCfgState.setStatus(_A)
_JnxSvcTransactionWapCreated_Type=Counter64
_JnxSvcTransactionWapCreated_Object=MibTableColumn
jnxSvcTransactionWapCreated=_JnxSvcTransactionWapCreated_Object((1,3,6,1,4,1,2636,3,27,2,1,34),_JnxSvcTransactionWapCreated_Type())
jnxSvcTransactionWapCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionWapCreated.setStatus(_A)
_JnxSvcTransactionWapMaximum_Type=Gauge32
_JnxSvcTransactionWapMaximum_Object=MibTableColumn
jnxSvcTransactionWapMaximum=_JnxSvcTransactionWapMaximum_Object((1,3,6,1,4,1,2636,3,27,2,1,35),_JnxSvcTransactionWapMaximum_Type())
jnxSvcTransactionWapMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionWapMaximum.setStatus(_A)
_JnxSvcTransactionWapFreed_Type=Counter64
_JnxSvcTransactionWapFreed_Object=MibTableColumn
jnxSvcTransactionWapFreed=_JnxSvcTransactionWapFreed_Object((1,3,6,1,4,1,2636,3,27,2,1,36),_JnxSvcTransactionWapFreed_Type())
jnxSvcTransactionWapFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionWapFreed.setStatus(_A)
_JnxSvcTransactionWapIdleFreed_Type=Counter64
_JnxSvcTransactionWapIdleFreed_Object=MibTableColumn
jnxSvcTransactionWapIdleFreed=_JnxSvcTransactionWapIdleFreed_Object((1,3,6,1,4,1,2636,3,27,2,1,37),_JnxSvcTransactionWapIdleFreed_Type())
jnxSvcTransactionWapIdleFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionWapIdleFreed.setStatus(_A)
_JnxSvcTransactionHttpCreated_Type=Counter64
_JnxSvcTransactionHttpCreated_Object=MibTableColumn
jnxSvcTransactionHttpCreated=_JnxSvcTransactionHttpCreated_Object((1,3,6,1,4,1,2636,3,27,2,1,38),_JnxSvcTransactionHttpCreated_Type())
jnxSvcTransactionHttpCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionHttpCreated.setStatus(_A)
_JnxSvcTransactionHttpMaximum_Type=Gauge32
_JnxSvcTransactionHttpMaximum_Object=MibTableColumn
jnxSvcTransactionHttpMaximum=_JnxSvcTransactionHttpMaximum_Object((1,3,6,1,4,1,2636,3,27,2,1,39),_JnxSvcTransactionHttpMaximum_Type())
jnxSvcTransactionHttpMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionHttpMaximum.setStatus(_A)
_JnxSvcTransactionHttpFreed_Type=Counter64
_JnxSvcTransactionHttpFreed_Object=MibTableColumn
jnxSvcTransactionHttpFreed=_JnxSvcTransactionHttpFreed_Object((1,3,6,1,4,1,2636,3,27,2,1,40),_JnxSvcTransactionHttpFreed_Type())
jnxSvcTransactionHttpFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionHttpFreed.setStatus(_A)
_JnxSvcTransactionHttpIdleFreed_Type=Counter64
_JnxSvcTransactionHttpIdleFreed_Object=MibTableColumn
jnxSvcTransactionHttpIdleFreed=_JnxSvcTransactionHttpIdleFreed_Object((1,3,6,1,4,1,2636,3,27,2,1,41),_JnxSvcTransactionHttpIdleFreed_Type())
jnxSvcTransactionHttpIdleFreed.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcTransactionHttpIdleFreed.setStatus(_A)
_JnxSvcServidProtInsUriErrProcess_Type=Counter64
_JnxSvcServidProtInsUriErrProcess_Object=MibTableColumn
jnxSvcServidProtInsUriErrProcess=_JnxSvcServidProtInsUriErrProcess_Object((1,3,6,1,4,1,2636,3,27,2,1,42),_JnxSvcServidProtInsUriErrProcess_Type())
jnxSvcServidProtInsUriErrProcess.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServidProtInsUriErrProcess.setStatus(_A)
_JnxSvcServidProtInsUriErrTooLong_Type=Counter64
_JnxSvcServidProtInsUriErrTooLong_Object=MibTableColumn
jnxSvcServidProtInsUriErrTooLong=_JnxSvcServidProtInsUriErrTooLong_Object((1,3,6,1,4,1,2636,3,27,2,1,43),_JnxSvcServidProtInsUriErrTooLong_Type())
jnxSvcServidProtInsUriErrTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServidProtInsUriErrTooLong.setStatus(_A)
_JnxSvcServidProtInsErrParseTx_Type=Counter64
_JnxSvcServidProtInsErrParseTx_Object=MibTableColumn
jnxSvcServidProtInsErrParseTx=_JnxSvcServidProtInsErrParseTx_Object((1,3,6,1,4,1,2636,3,27,2,1,44),_JnxSvcServidProtInsErrParseTx_Type())
jnxSvcServidProtInsErrParseTx.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServidProtInsErrParseTx.setStatus(_A)
_JnxSvcServidProtInsUriErrNoRes_Type=Counter64
_JnxSvcServidProtInsUriErrNoRes_Object=MibTableColumn
jnxSvcServidProtInsUriErrNoRes=_JnxSvcServidProtInsUriErrNoRes_Object((1,3,6,1,4,1,2636,3,27,2,1,45),_JnxSvcServidProtInsUriErrNoRes_Type())
jnxSvcServidProtInsUriErrNoRes.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSvcServidProtInsUriErrNoRes.setStatus(_A)
_JnxSvcMIBConformance_ObjectIdentity=ObjectIdentity
jnxSvcMIBConformance=_JnxSvcMIBConformance_ObjectIdentity((1,3,6,1,4,1,2636,3,27,20))
_JnxSvcMIBCompliances_ObjectIdentity=ObjectIdentity
jnxSvcMIBCompliances=_JnxSvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2636,3,27,20,1))
_JnxSvcMIBGroups_ObjectIdentity=ObjectIdentity
jnxSvcMIBGroups=_JnxSvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,2636,3,27,20,2))
jnxSvcFlowTableAggStatsGroup=ObjectGroup((1,3,6,1,4,1,2636,3,27,20,2,1))
jnxSvcFlowTableAggStatsGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:jnxSvcFlowTableAggStatsGroup.setStatus(_A)
jnxSvcServIdiceGroup=ObjectGroup((1,3,6,1,4,1,2636,3,27,20,2,2))
jnxSvcServIdiceGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:jnxSvcServIdiceGroup.setStatus(_A)
jnxSvcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2636,3,27,20,1,1))
jnxSvcMIBCompliance.setObjects(*((_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:jnxSvcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'jnxServicesInfoMib':jnxServicesInfoMib,'jnxSvcFlowTableAggStatsTable':jnxSvcFlowTableAggStatsTable,'jnxSvcFlowTableAggStatsEntry':jnxSvcFlowTableAggStatsEntry,_F:jnxSvcAggFlow,_G:jnxSvcAggFlowMaximum,_H:jnxSvcAggFlowCreated,_I:jnxSvcAggFlowFreed,_J:jnxSvcAggFlowIdleFreed,_K:jnxSvcAggFlowTcp,_L:jnxSvcAggFlowTcpMaximum,_M:jnxSvcAggFlowTcpCreated,_N:jnxSvcAggFlowTcpFreed,_O:jnxSvcAggFlowTcpIdleFreed,_P:jnxSvcAggFlowUdp,_Q:jnxSvcAggFlowUdpMaximum,_R:jnxSvcAggFlowUdpCreated,_S:jnxSvcAggFlowUdpFreed,_T:jnxSvcAggFlowUdpIdleFreed,_U:jnxSvcAggFlowPkt,_V:jnxSvcAggFlowPktErr,_W:jnxSvcAggFlowByte,_X:jnxSvcAggFlowByteErr,_Y:jnxSvcAggFlowIcmpPkt,_Z:jnxSvcAggFlowIcmpPktErr,_a:jnxSvcAggFlowIcmpPktErrBadFlow,_b:jnxSvcAggFlowIcmpByte,_c:jnxSvcAggFlowIcmpByteErr,_d:jnxSvcAggFlowTcpPkt,_e:jnxSvcAggFlowTcpPktErr,_f:jnxSvcAggFlowTcpPktErrBadFlow,_g:jnxSvcAggFlowTcpByte,_h:jnxSvcAggFlowTcpByteErr,_i:jnxSvcAggFlowUdpPkt,_j:jnxSvcAggFlowUdpPktErr,_k:jnxSvcAggFlowUdpPktErrBadFlow,_l:jnxSvcAggFlowUdpByte,_m:jnxSvcAggFlowUdpByteErr,'jnxSvcServIdTable':jnxSvcServIdTable,'jnxSvcServIdTableEntry':jnxSvcServIdTableEntry,_n:jnxSvcServIdPkt,_o:jnxSvcServIdByte,_p:jnxSvcServIdErrPkt,_q:jnxSvcServIdErrByte,_r:jnxSvcServIdHeadExPkt,_s:jnxSvcServIdHeadExByte,_t:jnxSvcServIdHeadExFlow,_u:jnxSvcServIdHeadExFlowMtch,_v:jnxSvcServIdHeadExProtoReq,_w:jnxSvcServIdHeadExHttpProtoReq,_x:jnxSvcServIdHeadExWapProtoReq,_y:jnxSvcServIdProtFlow,_z:jnxSvcServIdProtInsPkt,_A0:jnxSvcServIdProtInsByte,_A1:jnxSvcServIdProtInsFlowInsp,_A2:jnxSvcServIdProtInsFlowProtIdent,_A3:jnxSvcServIdProtInsHttpUri,_A4:jnxSvcServIdProtInsHttpUriMtch,_A5:jnxSvcServIdProtInsWapUri,_A6:jnxSvcServIdProtInsWapUriMtch,_A7:jnxSvcServIdPktTcpMalform,_A8:jnxSvcServIdWAPInvalidTxn,_A9:jnxSvcServIdErrWAPTxn,_AA:jnxSvcServIdErrHTTPTxn,_AB:jnxSvcServIdHeadExFailCfgState,_AC:jnxSvcServIdProtInsFailCfgState,_AD:jnxSvcTransactionWapCreated,_AE:jnxSvcTransactionWapMaximum,_AF:jnxSvcTransactionWapFreed,_AG:jnxSvcTransactionWapIdleFreed,_AH:jnxSvcTransactionHttpCreated,_AI:jnxSvcTransactionHttpMaximum,_AJ:jnxSvcTransactionHttpFreed,_AK:jnxSvcTransactionHttpIdleFreed,_AL:jnxSvcServidProtInsUriErrProcess,_AM:jnxSvcServidProtInsUriErrTooLong,_AN:jnxSvcServidProtInsErrParseTx,_AO:jnxSvcServidProtInsUriErrNoRes,'jnxSvcMIBConformance':jnxSvcMIBConformance,'jnxSvcMIBCompliances':jnxSvcMIBCompliances,'jnxSvcMIBCompliance':jnxSvcMIBCompliance,'jnxSvcMIBGroups':jnxSvcMIBGroups,_AP:jnxSvcFlowTableAggStatsGroup,_AQ:jnxSvcServIdiceGroup})