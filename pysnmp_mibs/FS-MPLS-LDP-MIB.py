_F='mplsFecIndex'
_E='FS-MPLS-LDP-MIB'
_D='InetAddressPrefixLength'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,=mibBuilder.importSymbols('FS-TC','ConfigStatus')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_D,'InetAddressType','InetPortNumber')
MplsLdpIdentifier,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLdpIdentifier')
AreaID,DesignatedRouterPriority,HelloRange,PositiveInteger,RouterID,Status=mibBuilder.importSymbols('OSPF-MIB','AreaID','DesignatedRouterPriority','HelloRange','PositiveInteger','RouterID','Status')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsMplsLdpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,99))
if mibBuilder.loadTexts:fsMplsLdpMIB.setRevisions(('2011-05-15 00:00',))
_FsMplsLdpMIBObjects_ObjectIdentity=ObjectIdentity
fsMplsLdpMIBObjects=_FsMplsLdpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,99,1))
_FsMplsLdpObjects_ObjectIdentity=ObjectIdentity
fsMplsLdpObjects=_FsMplsLdpObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,99,1,1))
_FsMplsLdpMplsGernalMibObjects_ObjectIdentity=ObjectIdentity
fsMplsLdpMplsGernalMibObjects=_FsMplsLdpMplsGernalMibObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1))
_MplsLdpThreadName_Type=SnmpAdminString
_MplsLdpThreadName_Object=MibScalar
mplsLdpThreadName=_MplsLdpThreadName_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,1),_MplsLdpThreadName_Type())
mplsLdpThreadName.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLdpThreadName.setStatus(_A)
_MplsLdpSessionUpCount_Type=Integer32
_MplsLdpSessionUpCount_Object=MibScalar
mplsLdpSessionUpCount=_MplsLdpSessionUpCount_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,2),_MplsLdpSessionUpCount_Type())
mplsLdpSessionUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLdpSessionUpCount.setStatus(_A)
_MplsLdpSessionCreatCount_Type=Integer32
_MplsLdpSessionCreatCount_Object=MibScalar
mplsLdpSessionCreatCount=_MplsLdpSessionCreatCount_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,3),_MplsLdpSessionCreatCount_Type())
mplsLdpSessionCreatCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLdpSessionCreatCount.setStatus(_A)
_MplsLdpSessionDownCount_Type=Integer32
_MplsLdpSessionDownCount_Object=MibScalar
mplsLdpSessionDownCount=_MplsLdpSessionDownCount_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,4),_MplsLdpSessionDownCount_Type())
mplsLdpSessionDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLdpSessionDownCount.setStatus(_A)
_MplsLdpSessionDownCauseByInf_Type=Integer32
_MplsLdpSessionDownCauseByInf_Object=MibScalar
mplsLdpSessionDownCauseByInf=_MplsLdpSessionDownCauseByInf_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,5),_MplsLdpSessionDownCauseByInf_Type())
mplsLdpSessionDownCauseByInf.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLdpSessionDownCauseByInf.setStatus(_A)
_FsMplsLdpFecTable_Object=MibTable
fsMplsLdpFecTable=_FsMplsLdpFecTable_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6))
if mibBuilder.loadTexts:fsMplsLdpFecTable.setStatus(_A)
_FsMplsLdpFecEntry_Object=MibTableRow
fsMplsLdpFecEntry=_FsMplsLdpFecEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1))
fsMplsLdpFecEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fsMplsLdpFecEntry.setStatus(_A)
_MplsFecIndex_Type=Integer32
_MplsFecIndex_Object=MibTableColumn
mplsFecIndex=_MplsFecIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,1),_MplsFecIndex_Type())
mplsFecIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mplsFecIndex.setStatus(_A)
class _MplsFecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('prefix',1),('hostAddress',2)))
_MplsFecType_Type.__name__=_C
_MplsFecType_Object=MibTableColumn
mplsFecType=_MplsFecType_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,2),_MplsFecType_Type())
mplsFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecType.setStatus(_A)
_MplsFecAddrType_Type=InetAddressType
_MplsFecAddrType_Object=MibTableColumn
mplsFecAddrType=_MplsFecAddrType_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,3),_MplsFecAddrType_Type())
mplsFecAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecAddrType.setStatus(_A)
_MplsFecAddr_Type=InetAddress
_MplsFecAddr_Object=MibTableColumn
mplsFecAddr=_MplsFecAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,4),_MplsFecAddr_Type())
mplsFecAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecAddr.setStatus(_A)
class _MplsFecAddrPrefixLength_Type(InetAddressPrefixLength):defaultValue=0
_MplsFecAddrPrefixLength_Type.__name__=_D
_MplsFecAddrPrefixLength_Object=MibTableColumn
mplsFecAddrPrefixLength=_MplsFecAddrPrefixLength_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,5),_MplsFecAddrPrefixLength_Type())
mplsFecAddrPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecAddrPrefixLength.setStatus(_A)
class _MplsFecStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('route',1),('nonroute',2)))
_MplsFecStatus_Type.__name__=_C
_MplsFecStatus_Object=MibTableColumn
mplsFecStatus=_MplsFecStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,6),_MplsFecStatus_Type())
mplsFecStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecStatus.setStatus(_A)
_MplsFecLspActivity_Type=TruthValue
_MplsFecLspActivity_Object=MibTableColumn
mplsFecLspActivity=_MplsFecLspActivity_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,7),_MplsFecLspActivity_Type())
mplsFecLspActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecLspActivity.setStatus(_A)
_MplsFecLspDisconnect_Type=TruthValue
_MplsFecLspDisconnect_Object=MibTableColumn
mplsFecLspDisconnect=_MplsFecLspDisconnect_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,8),_MplsFecLspDisconnect_Type())
mplsFecLspDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecLspDisconnect.setStatus(_A)
class _MplsFecLspDisconnectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sessionDown',1),('nhChng',2),('other',3)))
_MplsFecLspDisconnectType_Type.__name__=_C
_MplsFecLspDisconnectType_Object=MibTableColumn
mplsFecLspDisconnectType=_MplsFecLspDisconnectType_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,9),_MplsFecLspDisconnectType_Type())
mplsFecLspDisconnectType.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecLspDisconnectType.setStatus(_A)
_MplsFecSession_Type=MplsLdpIdentifier
_MplsFecSession_Object=MibTableColumn
mplsFecSession=_MplsFecSession_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,10),_MplsFecSession_Type())
mplsFecSession.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecSession.setStatus(_A)
class _MplsLdpSessionCloseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67)));namedValues=NamedValues(*(('none',0),('backoff',1),('hello_timer_expired',2),('peer_holddown_time_expired',3),('keepalive_timer_expired',4),('peer_keepalive_time_expired',5),('bad_ldp_identifier',6),('peer_recv_bad_ldp_identifier',7),('bad_protocol_version',8),('peer_recv_bad_protocol_version',9),('peer_recv_bad_pdu_length',10),('peer_recv_bad_message_length',11),('peer_recv_bad_tlv_length',12),('malformed_tlv_value',13),('peer_recv_malformed_tlv_value',14),('peer_shutdown',15),('session_rejected_no_hello',16),('peer_rejected_no_hello',17),('session_rejected_parameters_advertisement_mode',18),('peer_rejected_advertisement_mode',19),('session_rejected_parameters_max_pdu_length',20),('peer_rejected_max_pdu_length',21),('peer_rejected_parameters_label_range',22),('session_rejected_bad_keepalive_time',23),('peer_rejected_bad_keepalive_time',24),('internal_error',25),('peer_internal_error',26),('event_unlawful',27),('passive_wait_init_or_keepalive_expired',28),('peer_unknown_message_type',29),('peer_unknown_tlv_type',30),('tcp_connection_closed_by_peer',31),('no_ip_routing',32),('nsr_recover_fail',33),('session_has_no_other_adj',34),('session_connect_fail',35),('session_count_has_reach_max_count',36),('session_send_msg_fail',37),('session_md5_password_changed',38),('fsm_process_fail',39),('session_init_fail',40),('add_ftn_or_ilm_fail',41),('close_instance_close',42),('close_msg_proto_version_error',43),('close_session_backoff_callback_but_no_active_adj',44),('close_recv_bad_msg',45),('user_cleared_session_manually',46),('ldp_unconfigured_globally',47),('ldp_disabled_on_interface',48),('no_enough_memory',49),('ldp_global_config_change',50),('interface_vrf_changed',51),('ldp_router_id_changed',52),('interface_down',53),('recv_bad_length_msg',54),('recv_bad_tlv_len',55),('recv_malformed_tlv',56),('recv_internal_error',57),('recv_bad_pdu_length',58),('tcp_connect_not_correct',59),('nsm_client_close',60),('process_label_mapping_fail',61),('targeted_session_unconfigured',62),('switchover_process_gr',63),('local_host_process_gr',64),('reload_command',65),('te_interface_disabled_targeted_session',66),('targeted_hellos_no_longer_accepted',67)))
_MplsLdpSessionCloseType_Type.__name__=_C
_MplsLdpSessionCloseType_Object=MibTableColumn
mplsLdpSessionCloseType=_MplsLdpSessionCloseType_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,11),_MplsLdpSessionCloseType_Type())
mplsLdpSessionCloseType.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLdpSessionCloseType.setStatus(_A)
_MplsFecIngressBytes_Type=Integer32
_MplsFecIngressBytes_Object=MibTableColumn
mplsFecIngressBytes=_MplsFecIngressBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,12),_MplsFecIngressBytes_Type())
mplsFecIngressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecIngressBytes.setStatus(_A)
_MplsFecIngressPackets_Type=Integer32
_MplsFecIngressPackets_Object=MibTableColumn
mplsFecIngressPackets=_MplsFecIngressPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,13),_MplsFecIngressPackets_Type())
mplsFecIngressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecIngressPackets.setStatus(_A)
_MplsFecTransmitBytes_Type=Integer32
_MplsFecTransmitBytes_Object=MibTableColumn
mplsFecTransmitBytes=_MplsFecTransmitBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,14),_MplsFecTransmitBytes_Type())
mplsFecTransmitBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecTransmitBytes.setStatus(_A)
_MplsFecTransmitPackets_Type=Integer32
_MplsFecTransmitPackets_Object=MibTableColumn
mplsFecTransmitPackets=_MplsFecTransmitPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,1,6,1,15),_MplsFecTransmitPackets_Type())
mplsFecTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsFecTransmitPackets.setStatus(_A)
_FsMplsLdpConfigMibObjects_ObjectIdentity=ObjectIdentity
fsMplsLdpConfigMibObjects=_FsMplsLdpConfigMibObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,99,1,1,2))
_FsMplsLdpConformance_ObjectIdentity=ObjectIdentity
fsMplsLdpConformance=_FsMplsLdpConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,99,1,2))
mibBuilder.exportSymbols(_E,**{'fsMplsLdpMIB':fsMplsLdpMIB,'fsMplsLdpMIBObjects':fsMplsLdpMIBObjects,'fsMplsLdpObjects':fsMplsLdpObjects,'fsMplsLdpMplsGernalMibObjects':fsMplsLdpMplsGernalMibObjects,'mplsLdpThreadName':mplsLdpThreadName,'mplsLdpSessionUpCount':mplsLdpSessionUpCount,'mplsLdpSessionCreatCount':mplsLdpSessionCreatCount,'mplsLdpSessionDownCount':mplsLdpSessionDownCount,'mplsLdpSessionDownCauseByInf':mplsLdpSessionDownCauseByInf,'fsMplsLdpFecTable':fsMplsLdpFecTable,'fsMplsLdpFecEntry':fsMplsLdpFecEntry,_F:mplsFecIndex,'mplsFecType':mplsFecType,'mplsFecAddrType':mplsFecAddrType,'mplsFecAddr':mplsFecAddr,'mplsFecAddrPrefixLength':mplsFecAddrPrefixLength,'mplsFecStatus':mplsFecStatus,'mplsFecLspActivity':mplsFecLspActivity,'mplsFecLspDisconnect':mplsFecLspDisconnect,'mplsFecLspDisconnectType':mplsFecLspDisconnectType,'mplsFecSession':mplsFecSession,'mplsLdpSessionCloseType':mplsLdpSessionCloseType,'mplsFecIngressBytes':mplsFecIngressBytes,'mplsFecIngressPackets':mplsFecIngressPackets,'mplsFecTransmitBytes':mplsFecTransmitBytes,'mplsFecTransmitPackets':mplsFecTransmitPackets,'fsMplsLdpConfigMibObjects':fsMplsLdpConfigMibObjects,'fsMplsLdpConformance':fsMplsLdpConformance})