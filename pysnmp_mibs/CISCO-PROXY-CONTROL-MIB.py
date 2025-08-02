_AG='cProxyCallHistoryGroup'
_AF='cProxyCallActiveGroup'
_AE='cProxyCallHistoryTxT120Bytes'
_AD='cProxyCallHistoryTxT120Packets'
_AC='cProxyCallHistoryRxT120Bytes'
_AB='cProxyCallHistoryRxT120Packets'
_AA='cProxyCallHistoryTxVideoBytes'
_A9='cProxyCallHistoryTxVideoPackets'
_A8='cProxyCallHistoryRxVideoBytes'
_A7='cProxyCallHistoryRxVideoPackets'
_A6='cProxyCallHistoryTxAudioBytes'
_A5='cProxyCallHistoryTxAudioPackets'
_A4='cProxyCallHistoryRxAudioBytes'
_A3='cProxyCallHistoryRxAudioPackets'
_A2='cProxyCallHistoryVideoCoderRate'
_A1='cProxyCallHistoryAudioCoderRate'
_A0='cProxyCallHistoryActualBandwidth'
_z='cProxyCallHistoryRequestBandwidth'
_y='cProxyCallHistoryEndpointVendor'
_x='cProxyCallHistoryEndpointType'
_w='cProxyCallHistoryT120TCPPort4'
_v='cProxyCallHistoryT120TCPPort3'
_u='cProxyCallHistoryT120TCPPort2'
_t='cProxyCallHistoryT120TCPPort1'
_s='cProxyCallHistoryVideoUDPPort'
_r='cProxyCallHistoryAudioUDPPort'
_q='cProxyCallHistoryRemoteIPAddress'
_p='cProxyCallHistoryConnectionId'
_o='cProxyCallActiveTxT120Bytes'
_n='cProxyCallActiveTxT120Packets'
_m='cProxyCallActiveRxT120Bytes'
_l='cProxyCallActiveRxT120Packets'
_k='cProxyCallActiveTxVideoBytes'
_j='cProxyCallActiveTxVideoPackets'
_i='cProxyCallActiveRxVideoBytes'
_h='cProxyCallActiveRxVideoPackets'
_g='cProxyCallActiveTxAudioBytes'
_f='cProxyCallActiveTxAudioPackets'
_e='cProxyCallActiveRxAudioBytes'
_d='cProxyCallActiveRxAudioPackets'
_c='cProxyCallActiveVideoCoderRate'
_b='cProxyCallActiveAudioCoderRate'
_a='cProxyCallActiveActualBandwidth'
_Z='cProxyCallActiveRequestBandwidth'
_Y='cProxyCallActiveEndpointVendor'
_X='cProxyCallActiveEndpointType'
_W='cProxyCallActiveT120TCPPort4'
_V='cProxyCallActiveT120TCPPort3'
_U='cProxyCallActiveT120TCPPort2'
_T='cProxyCallActiveT120TCPPort1'
_S='cProxyCallActiveVideoUDPPort'
_R='cProxyCallActiveAudioUDPPort'
_Q='cProxyCallActiveRemoteIPAddress'
_P='cProxyCallActiveConnectionId'
_O='is11172'
_N='nonStandard'
_M='callActiveSetupTime'
_L='callActiveIndex'
_K='cCallHistoryIndex'
_J='CISCO-DIAL-CONTROL-MIB'
_I='other'
_H='DIAL-CONTROL-MIB'
_G='kilobits per second'
_F='bytes'
_E='packets'
_D='Integer32'
_C='read-only'
_B='CISCO-PROXY-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_J,_K)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CvcGUid,=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcGUid')
AbsoluteCounter32,callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_H,'AbsoluteCounter32',_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoProxyControlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,57))
if mibBuilder.loadTexts:ciscoProxyControlMIB.setRevisions(('2009-02-11 00:00','2006-03-12 00:00','2005-03-06 00:00','2000-02-04 00:00'))
class CProxyEndptType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('proxy',1),('gateway',2)))
class CProxyAudioCodec(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_I,0),(_N,1),('g711Alawr64k',2),('g711Alawr56k',3),('g711Ulawr64k',4),('g711Ulawr56k',5),('g722r64k',6),('g722r56k',7),('g722r48k',8),('g7231',9),('g728',10),('g729',11),('g729AnnexA',12),(_O,13),('is13818',14),('g729AnnexB',15),('g729AnnexAB',16),('g729AnnexC',17),('gsmFullRate',18),('gsmHalfRate',19),('gsmEnhancedFullRate',20),('gsmAmrNb',21),('iLBC',22),('iSAC',23)))
class CProxyVideoCodec(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_N,1),('h261',2),('h262',3),('h263',4),(_O,5)))
_CiscoProxyControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoProxyControlMIBObjects=_CiscoProxyControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,57,1))
_CProxyCallActive_ObjectIdentity=ObjectIdentity
cProxyCallActive=_CProxyCallActive_ObjectIdentity((1,3,6,1,4,1,9,10,57,1,1))
_CProxyCallActiveTable_Object=MibTable
cProxyCallActiveTable=_CProxyCallActiveTable_Object((1,3,6,1,4,1,9,10,57,1,1,1))
if mibBuilder.loadTexts:cProxyCallActiveTable.setStatus(_A)
_CProxyCallActiveEntry_Object=MibTableRow
cProxyCallActiveEntry=_CProxyCallActiveEntry_Object((1,3,6,1,4,1,9,10,57,1,1,1,1))
cProxyCallActiveEntry.setIndexNames((0,_H,_M),(0,_H,_L))
if mibBuilder.loadTexts:cProxyCallActiveEntry.setStatus(_A)
_CProxyCallActiveConnectionId_Type=CvcGUid
_CProxyCallActiveConnectionId_Object=MibTableColumn
cProxyCallActiveConnectionId=_CProxyCallActiveConnectionId_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,1),_CProxyCallActiveConnectionId_Type())
cProxyCallActiveConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveConnectionId.setStatus(_A)
_CProxyCallActiveRemoteIPAddress_Type=IpAddress
_CProxyCallActiveRemoteIPAddress_Object=MibTableColumn
cProxyCallActiveRemoteIPAddress=_CProxyCallActiveRemoteIPAddress_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,2),_CProxyCallActiveRemoteIPAddress_Type())
cProxyCallActiveRemoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRemoteIPAddress.setStatus(_A)
class _CProxyCallActiveAudioUDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveAudioUDPPort_Type.__name__=_D
_CProxyCallActiveAudioUDPPort_Object=MibTableColumn
cProxyCallActiveAudioUDPPort=_CProxyCallActiveAudioUDPPort_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,3),_CProxyCallActiveAudioUDPPort_Type())
cProxyCallActiveAudioUDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveAudioUDPPort.setStatus(_A)
class _CProxyCallActiveVideoUDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveVideoUDPPort_Type.__name__=_D
_CProxyCallActiveVideoUDPPort_Object=MibTableColumn
cProxyCallActiveVideoUDPPort=_CProxyCallActiveVideoUDPPort_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,4),_CProxyCallActiveVideoUDPPort_Type())
cProxyCallActiveVideoUDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveVideoUDPPort.setStatus(_A)
class _CProxyCallActiveT120TCPPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveT120TCPPort1_Type.__name__=_D
_CProxyCallActiveT120TCPPort1_Object=MibTableColumn
cProxyCallActiveT120TCPPort1=_CProxyCallActiveT120TCPPort1_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,5),_CProxyCallActiveT120TCPPort1_Type())
cProxyCallActiveT120TCPPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveT120TCPPort1.setStatus(_A)
class _CProxyCallActiveT120TCPPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveT120TCPPort2_Type.__name__=_D
_CProxyCallActiveT120TCPPort2_Object=MibTableColumn
cProxyCallActiveT120TCPPort2=_CProxyCallActiveT120TCPPort2_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,6),_CProxyCallActiveT120TCPPort2_Type())
cProxyCallActiveT120TCPPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveT120TCPPort2.setStatus(_A)
class _CProxyCallActiveT120TCPPort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveT120TCPPort3_Type.__name__=_D
_CProxyCallActiveT120TCPPort3_Object=MibTableColumn
cProxyCallActiveT120TCPPort3=_CProxyCallActiveT120TCPPort3_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,7),_CProxyCallActiveT120TCPPort3_Type())
cProxyCallActiveT120TCPPort3.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveT120TCPPort3.setStatus(_A)
class _CProxyCallActiveT120TCPPort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveT120TCPPort4_Type.__name__=_D
_CProxyCallActiveT120TCPPort4_Object=MibTableColumn
cProxyCallActiveT120TCPPort4=_CProxyCallActiveT120TCPPort4_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,8),_CProxyCallActiveT120TCPPort4_Type())
cProxyCallActiveT120TCPPort4.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveT120TCPPort4.setStatus(_A)
_CProxyCallActiveEndpointType_Type=CProxyEndptType
_CProxyCallActiveEndpointType_Object=MibTableColumn
cProxyCallActiveEndpointType=_CProxyCallActiveEndpointType_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,9),_CProxyCallActiveEndpointType_Type())
cProxyCallActiveEndpointType.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveEndpointType.setStatus(_A)
class _CProxyCallActiveEndpointVendor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallActiveEndpointVendor_Type.__name__=_D
_CProxyCallActiveEndpointVendor_Object=MibTableColumn
cProxyCallActiveEndpointVendor=_CProxyCallActiveEndpointVendor_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,10),_CProxyCallActiveEndpointVendor_Type())
cProxyCallActiveEndpointVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveEndpointVendor.setStatus(_A)
class _CProxyCallActiveRequestBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CProxyCallActiveRequestBandwidth_Type.__name__=_D
_CProxyCallActiveRequestBandwidth_Object=MibTableColumn
cProxyCallActiveRequestBandwidth=_CProxyCallActiveRequestBandwidth_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,11),_CProxyCallActiveRequestBandwidth_Type())
cProxyCallActiveRequestBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRequestBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRequestBandwidth.setUnits(_G)
class _CProxyCallActiveActualBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CProxyCallActiveActualBandwidth_Type.__name__=_D
_CProxyCallActiveActualBandwidth_Object=MibTableColumn
cProxyCallActiveActualBandwidth=_CProxyCallActiveActualBandwidth_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,12),_CProxyCallActiveActualBandwidth_Type())
cProxyCallActiveActualBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveActualBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveActualBandwidth.setUnits(_G)
_CProxyCallActiveAudioCoderRate_Type=CProxyAudioCodec
_CProxyCallActiveAudioCoderRate_Object=MibTableColumn
cProxyCallActiveAudioCoderRate=_CProxyCallActiveAudioCoderRate_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,13),_CProxyCallActiveAudioCoderRate_Type())
cProxyCallActiveAudioCoderRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveAudioCoderRate.setStatus(_A)
_CProxyCallActiveVideoCoderRate_Type=CProxyVideoCodec
_CProxyCallActiveVideoCoderRate_Object=MibTableColumn
cProxyCallActiveVideoCoderRate=_CProxyCallActiveVideoCoderRate_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,14),_CProxyCallActiveVideoCoderRate_Type())
cProxyCallActiveVideoCoderRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveVideoCoderRate.setStatus(_A)
_CProxyCallActiveRxAudioPackets_Type=AbsoluteCounter32
_CProxyCallActiveRxAudioPackets_Object=MibTableColumn
cProxyCallActiveRxAudioPackets=_CProxyCallActiveRxAudioPackets_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,15),_CProxyCallActiveRxAudioPackets_Type())
cProxyCallActiveRxAudioPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRxAudioPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRxAudioPackets.setUnits(_E)
_CProxyCallActiveRxAudioBytes_Type=AbsoluteCounter32
_CProxyCallActiveRxAudioBytes_Object=MibTableColumn
cProxyCallActiveRxAudioBytes=_CProxyCallActiveRxAudioBytes_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,16),_CProxyCallActiveRxAudioBytes_Type())
cProxyCallActiveRxAudioBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRxAudioBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRxAudioBytes.setUnits(_F)
_CProxyCallActiveTxAudioPackets_Type=AbsoluteCounter32
_CProxyCallActiveTxAudioPackets_Object=MibTableColumn
cProxyCallActiveTxAudioPackets=_CProxyCallActiveTxAudioPackets_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,17),_CProxyCallActiveTxAudioPackets_Type())
cProxyCallActiveTxAudioPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveTxAudioPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveTxAudioPackets.setUnits(_E)
_CProxyCallActiveTxAudioBytes_Type=AbsoluteCounter32
_CProxyCallActiveTxAudioBytes_Object=MibTableColumn
cProxyCallActiveTxAudioBytes=_CProxyCallActiveTxAudioBytes_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,18),_CProxyCallActiveTxAudioBytes_Type())
cProxyCallActiveTxAudioBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveTxAudioBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveTxAudioBytes.setUnits(_F)
_CProxyCallActiveRxVideoPackets_Type=AbsoluteCounter32
_CProxyCallActiveRxVideoPackets_Object=MibTableColumn
cProxyCallActiveRxVideoPackets=_CProxyCallActiveRxVideoPackets_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,19),_CProxyCallActiveRxVideoPackets_Type())
cProxyCallActiveRxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRxVideoPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRxVideoPackets.setUnits(_E)
_CProxyCallActiveRxVideoBytes_Type=AbsoluteCounter32
_CProxyCallActiveRxVideoBytes_Object=MibTableColumn
cProxyCallActiveRxVideoBytes=_CProxyCallActiveRxVideoBytes_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,20),_CProxyCallActiveRxVideoBytes_Type())
cProxyCallActiveRxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRxVideoBytes.setUnits(_F)
_CProxyCallActiveTxVideoPackets_Type=AbsoluteCounter32
_CProxyCallActiveTxVideoPackets_Object=MibTableColumn
cProxyCallActiveTxVideoPackets=_CProxyCallActiveTxVideoPackets_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,21),_CProxyCallActiveTxVideoPackets_Type())
cProxyCallActiveTxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveTxVideoPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveTxVideoPackets.setUnits(_E)
_CProxyCallActiveTxVideoBytes_Type=AbsoluteCounter32
_CProxyCallActiveTxVideoBytes_Object=MibTableColumn
cProxyCallActiveTxVideoBytes=_CProxyCallActiveTxVideoBytes_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,22),_CProxyCallActiveTxVideoBytes_Type())
cProxyCallActiveTxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveTxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveTxVideoBytes.setUnits(_F)
_CProxyCallActiveRxT120Packets_Type=AbsoluteCounter32
_CProxyCallActiveRxT120Packets_Object=MibTableColumn
cProxyCallActiveRxT120Packets=_CProxyCallActiveRxT120Packets_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,23),_CProxyCallActiveRxT120Packets_Type())
cProxyCallActiveRxT120Packets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRxT120Packets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRxT120Packets.setUnits(_E)
_CProxyCallActiveRxT120Bytes_Type=AbsoluteCounter32
_CProxyCallActiveRxT120Bytes_Object=MibTableColumn
cProxyCallActiveRxT120Bytes=_CProxyCallActiveRxT120Bytes_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,24),_CProxyCallActiveRxT120Bytes_Type())
cProxyCallActiveRxT120Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveRxT120Bytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveRxT120Bytes.setUnits(_F)
_CProxyCallActiveTxT120Packets_Type=AbsoluteCounter32
_CProxyCallActiveTxT120Packets_Object=MibTableColumn
cProxyCallActiveTxT120Packets=_CProxyCallActiveTxT120Packets_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,25),_CProxyCallActiveTxT120Packets_Type())
cProxyCallActiveTxT120Packets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveTxT120Packets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveTxT120Packets.setUnits(_E)
_CProxyCallActiveTxT120Bytes_Type=AbsoluteCounter32
_CProxyCallActiveTxT120Bytes_Object=MibTableColumn
cProxyCallActiveTxT120Bytes=_CProxyCallActiveTxT120Bytes_Object((1,3,6,1,4,1,9,10,57,1,1,1,1,26),_CProxyCallActiveTxT120Bytes_Type())
cProxyCallActiveTxT120Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallActiveTxT120Bytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallActiveTxT120Bytes.setUnits(_F)
_CProxyCallHistory_ObjectIdentity=ObjectIdentity
cProxyCallHistory=_CProxyCallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,57,1,2))
_CProxyCallHistoryTable_Object=MibTable
cProxyCallHistoryTable=_CProxyCallHistoryTable_Object((1,3,6,1,4,1,9,10,57,1,2,1))
if mibBuilder.loadTexts:cProxyCallHistoryTable.setStatus(_A)
_CProxyCallHistoryEntry_Object=MibTableRow
cProxyCallHistoryEntry=_CProxyCallHistoryEntry_Object((1,3,6,1,4,1,9,10,57,1,2,1,1))
cProxyCallHistoryEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cProxyCallHistoryEntry.setStatus(_A)
_CProxyCallHistoryConnectionId_Type=CvcGUid
_CProxyCallHistoryConnectionId_Object=MibTableColumn
cProxyCallHistoryConnectionId=_CProxyCallHistoryConnectionId_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,1),_CProxyCallHistoryConnectionId_Type())
cProxyCallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryConnectionId.setStatus(_A)
_CProxyCallHistoryRemoteIPAddress_Type=IpAddress
_CProxyCallHistoryRemoteIPAddress_Object=MibTableColumn
cProxyCallHistoryRemoteIPAddress=_CProxyCallHistoryRemoteIPAddress_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,2),_CProxyCallHistoryRemoteIPAddress_Type())
cProxyCallHistoryRemoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRemoteIPAddress.setStatus(_A)
class _CProxyCallHistoryAudioUDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryAudioUDPPort_Type.__name__=_D
_CProxyCallHistoryAudioUDPPort_Object=MibTableColumn
cProxyCallHistoryAudioUDPPort=_CProxyCallHistoryAudioUDPPort_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,3),_CProxyCallHistoryAudioUDPPort_Type())
cProxyCallHistoryAudioUDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryAudioUDPPort.setStatus(_A)
class _CProxyCallHistoryVideoUDPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryVideoUDPPort_Type.__name__=_D
_CProxyCallHistoryVideoUDPPort_Object=MibTableColumn
cProxyCallHistoryVideoUDPPort=_CProxyCallHistoryVideoUDPPort_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,4),_CProxyCallHistoryVideoUDPPort_Type())
cProxyCallHistoryVideoUDPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryVideoUDPPort.setStatus(_A)
class _CProxyCallHistoryT120TCPPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryT120TCPPort1_Type.__name__=_D
_CProxyCallHistoryT120TCPPort1_Object=MibTableColumn
cProxyCallHistoryT120TCPPort1=_CProxyCallHistoryT120TCPPort1_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,5),_CProxyCallHistoryT120TCPPort1_Type())
cProxyCallHistoryT120TCPPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryT120TCPPort1.setStatus(_A)
class _CProxyCallHistoryT120TCPPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryT120TCPPort2_Type.__name__=_D
_CProxyCallHistoryT120TCPPort2_Object=MibTableColumn
cProxyCallHistoryT120TCPPort2=_CProxyCallHistoryT120TCPPort2_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,6),_CProxyCallHistoryT120TCPPort2_Type())
cProxyCallHistoryT120TCPPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryT120TCPPort2.setStatus(_A)
class _CProxyCallHistoryT120TCPPort3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryT120TCPPort3_Type.__name__=_D
_CProxyCallHistoryT120TCPPort3_Object=MibTableColumn
cProxyCallHistoryT120TCPPort3=_CProxyCallHistoryT120TCPPort3_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,7),_CProxyCallHistoryT120TCPPort3_Type())
cProxyCallHistoryT120TCPPort3.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryT120TCPPort3.setStatus(_A)
class _CProxyCallHistoryT120TCPPort4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryT120TCPPort4_Type.__name__=_D
_CProxyCallHistoryT120TCPPort4_Object=MibTableColumn
cProxyCallHistoryT120TCPPort4=_CProxyCallHistoryT120TCPPort4_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,8),_CProxyCallHistoryT120TCPPort4_Type())
cProxyCallHistoryT120TCPPort4.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryT120TCPPort4.setStatus(_A)
_CProxyCallHistoryEndpointType_Type=CProxyEndptType
_CProxyCallHistoryEndpointType_Object=MibTableColumn
cProxyCallHistoryEndpointType=_CProxyCallHistoryEndpointType_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,9),_CProxyCallHistoryEndpointType_Type())
cProxyCallHistoryEndpointType.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryEndpointType.setStatus(_A)
class _CProxyCallHistoryEndpointVendor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CProxyCallHistoryEndpointVendor_Type.__name__=_D
_CProxyCallHistoryEndpointVendor_Object=MibTableColumn
cProxyCallHistoryEndpointVendor=_CProxyCallHistoryEndpointVendor_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,10),_CProxyCallHistoryEndpointVendor_Type())
cProxyCallHistoryEndpointVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryEndpointVendor.setStatus(_A)
class _CProxyCallHistoryRequestBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CProxyCallHistoryRequestBandwidth_Type.__name__=_D
_CProxyCallHistoryRequestBandwidth_Object=MibTableColumn
cProxyCallHistoryRequestBandwidth=_CProxyCallHistoryRequestBandwidth_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,11),_CProxyCallHistoryRequestBandwidth_Type())
cProxyCallHistoryRequestBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRequestBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRequestBandwidth.setUnits(_G)
class _CProxyCallHistoryActualBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CProxyCallHistoryActualBandwidth_Type.__name__=_D
_CProxyCallHistoryActualBandwidth_Object=MibTableColumn
cProxyCallHistoryActualBandwidth=_CProxyCallHistoryActualBandwidth_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,12),_CProxyCallHistoryActualBandwidth_Type())
cProxyCallHistoryActualBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryActualBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryActualBandwidth.setUnits(_G)
_CProxyCallHistoryAudioCoderRate_Type=CProxyAudioCodec
_CProxyCallHistoryAudioCoderRate_Object=MibTableColumn
cProxyCallHistoryAudioCoderRate=_CProxyCallHistoryAudioCoderRate_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,13),_CProxyCallHistoryAudioCoderRate_Type())
cProxyCallHistoryAudioCoderRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryAudioCoderRate.setStatus(_A)
_CProxyCallHistoryVideoCoderRate_Type=CProxyVideoCodec
_CProxyCallHistoryVideoCoderRate_Object=MibTableColumn
cProxyCallHistoryVideoCoderRate=_CProxyCallHistoryVideoCoderRate_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,14),_CProxyCallHistoryVideoCoderRate_Type())
cProxyCallHistoryVideoCoderRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryVideoCoderRate.setStatus(_A)
_CProxyCallHistoryRxAudioPackets_Type=AbsoluteCounter32
_CProxyCallHistoryRxAudioPackets_Object=MibTableColumn
cProxyCallHistoryRxAudioPackets=_CProxyCallHistoryRxAudioPackets_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,15),_CProxyCallHistoryRxAudioPackets_Type())
cProxyCallHistoryRxAudioPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRxAudioPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRxAudioPackets.setUnits(_E)
_CProxyCallHistoryRxAudioBytes_Type=AbsoluteCounter32
_CProxyCallHistoryRxAudioBytes_Object=MibTableColumn
cProxyCallHistoryRxAudioBytes=_CProxyCallHistoryRxAudioBytes_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,16),_CProxyCallHistoryRxAudioBytes_Type())
cProxyCallHistoryRxAudioBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRxAudioBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRxAudioBytes.setUnits(_F)
_CProxyCallHistoryTxAudioPackets_Type=AbsoluteCounter32
_CProxyCallHistoryTxAudioPackets_Object=MibTableColumn
cProxyCallHistoryTxAudioPackets=_CProxyCallHistoryTxAudioPackets_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,17),_CProxyCallHistoryTxAudioPackets_Type())
cProxyCallHistoryTxAudioPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryTxAudioPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryTxAudioPackets.setUnits(_E)
_CProxyCallHistoryTxAudioBytes_Type=AbsoluteCounter32
_CProxyCallHistoryTxAudioBytes_Object=MibTableColumn
cProxyCallHistoryTxAudioBytes=_CProxyCallHistoryTxAudioBytes_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,18),_CProxyCallHistoryTxAudioBytes_Type())
cProxyCallHistoryTxAudioBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryTxAudioBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryTxAudioBytes.setUnits(_F)
_CProxyCallHistoryRxVideoPackets_Type=AbsoluteCounter32
_CProxyCallHistoryRxVideoPackets_Object=MibTableColumn
cProxyCallHistoryRxVideoPackets=_CProxyCallHistoryRxVideoPackets_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,19),_CProxyCallHistoryRxVideoPackets_Type())
cProxyCallHistoryRxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRxVideoPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRxVideoPackets.setUnits(_E)
_CProxyCallHistoryRxVideoBytes_Type=AbsoluteCounter32
_CProxyCallHistoryRxVideoBytes_Object=MibTableColumn
cProxyCallHistoryRxVideoBytes=_CProxyCallHistoryRxVideoBytes_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,20),_CProxyCallHistoryRxVideoBytes_Type())
cProxyCallHistoryRxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRxVideoBytes.setUnits(_F)
_CProxyCallHistoryTxVideoPackets_Type=AbsoluteCounter32
_CProxyCallHistoryTxVideoPackets_Object=MibTableColumn
cProxyCallHistoryTxVideoPackets=_CProxyCallHistoryTxVideoPackets_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,21),_CProxyCallHistoryTxVideoPackets_Type())
cProxyCallHistoryTxVideoPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryTxVideoPackets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryTxVideoPackets.setUnits(_E)
_CProxyCallHistoryTxVideoBytes_Type=AbsoluteCounter32
_CProxyCallHistoryTxVideoBytes_Object=MibTableColumn
cProxyCallHistoryTxVideoBytes=_CProxyCallHistoryTxVideoBytes_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,22),_CProxyCallHistoryTxVideoBytes_Type())
cProxyCallHistoryTxVideoBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryTxVideoBytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryTxVideoBytes.setUnits(_F)
_CProxyCallHistoryRxT120Packets_Type=AbsoluteCounter32
_CProxyCallHistoryRxT120Packets_Object=MibTableColumn
cProxyCallHistoryRxT120Packets=_CProxyCallHistoryRxT120Packets_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,23),_CProxyCallHistoryRxT120Packets_Type())
cProxyCallHistoryRxT120Packets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRxT120Packets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRxT120Packets.setUnits(_E)
_CProxyCallHistoryRxT120Bytes_Type=AbsoluteCounter32
_CProxyCallHistoryRxT120Bytes_Object=MibTableColumn
cProxyCallHistoryRxT120Bytes=_CProxyCallHistoryRxT120Bytes_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,24),_CProxyCallHistoryRxT120Bytes_Type())
cProxyCallHistoryRxT120Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryRxT120Bytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryRxT120Bytes.setUnits(_F)
_CProxyCallHistoryTxT120Packets_Type=AbsoluteCounter32
_CProxyCallHistoryTxT120Packets_Object=MibTableColumn
cProxyCallHistoryTxT120Packets=_CProxyCallHistoryTxT120Packets_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,25),_CProxyCallHistoryTxT120Packets_Type())
cProxyCallHistoryTxT120Packets.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryTxT120Packets.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryTxT120Packets.setUnits(_E)
_CProxyCallHistoryTxT120Bytes_Type=AbsoluteCounter32
_CProxyCallHistoryTxT120Bytes_Object=MibTableColumn
cProxyCallHistoryTxT120Bytes=_CProxyCallHistoryTxT120Bytes_Object((1,3,6,1,4,1,9,10,57,1,2,1,1,26),_CProxyCallHistoryTxT120Bytes_Type())
cProxyCallHistoryTxT120Bytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cProxyCallHistoryTxT120Bytes.setStatus(_A)
if mibBuilder.loadTexts:cProxyCallHistoryTxT120Bytes.setUnits(_F)
_CiscoProxyControlMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoProxyControlMIBNotificationPrefix=_CiscoProxyControlMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,57,2))
_CiscoProxyControlMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoProxyControlMIBNotifications=_CiscoProxyControlMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,57,2,0))
_CiscoProxyControlMIBConformance_ObjectIdentity=ObjectIdentity
ciscoProxyControlMIBConformance=_CiscoProxyControlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,57,3))
_CiscoProxyControlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoProxyControlMIBCompliances=_CiscoProxyControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,57,3,1))
_CiscoProxyControlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoProxyControlMIBGroups=_CiscoProxyControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,57,3,2))
cProxyCallActiveGroup=ObjectGroup((1,3,6,1,4,1,9,10,57,3,2,1))
cProxyCallActiveGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:cProxyCallActiveGroup.setStatus(_A)
cProxyCallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,57,3,2,2))
cProxyCallHistoryGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:cProxyCallHistoryGroup.setStatus(_A)
ciscoProxyControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,57,3,1,1))
ciscoProxyControlMIBCompliance.setObjects(*((_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ciscoProxyControlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CProxyEndptType':CProxyEndptType,'CProxyAudioCodec':CProxyAudioCodec,'CProxyVideoCodec':CProxyVideoCodec,'ciscoProxyControlMIB':ciscoProxyControlMIB,'ciscoProxyControlMIBObjects':ciscoProxyControlMIBObjects,'cProxyCallActive':cProxyCallActive,'cProxyCallActiveTable':cProxyCallActiveTable,'cProxyCallActiveEntry':cProxyCallActiveEntry,_P:cProxyCallActiveConnectionId,_Q:cProxyCallActiveRemoteIPAddress,_R:cProxyCallActiveAudioUDPPort,_S:cProxyCallActiveVideoUDPPort,_T:cProxyCallActiveT120TCPPort1,_U:cProxyCallActiveT120TCPPort2,_V:cProxyCallActiveT120TCPPort3,_W:cProxyCallActiveT120TCPPort4,_X:cProxyCallActiveEndpointType,_Y:cProxyCallActiveEndpointVendor,_Z:cProxyCallActiveRequestBandwidth,_a:cProxyCallActiveActualBandwidth,_b:cProxyCallActiveAudioCoderRate,_c:cProxyCallActiveVideoCoderRate,_d:cProxyCallActiveRxAudioPackets,_e:cProxyCallActiveRxAudioBytes,_f:cProxyCallActiveTxAudioPackets,_g:cProxyCallActiveTxAudioBytes,_h:cProxyCallActiveRxVideoPackets,_i:cProxyCallActiveRxVideoBytes,_j:cProxyCallActiveTxVideoPackets,_k:cProxyCallActiveTxVideoBytes,_l:cProxyCallActiveRxT120Packets,_m:cProxyCallActiveRxT120Bytes,_n:cProxyCallActiveTxT120Packets,_o:cProxyCallActiveTxT120Bytes,'cProxyCallHistory':cProxyCallHistory,'cProxyCallHistoryTable':cProxyCallHistoryTable,'cProxyCallHistoryEntry':cProxyCallHistoryEntry,_p:cProxyCallHistoryConnectionId,_q:cProxyCallHistoryRemoteIPAddress,_r:cProxyCallHistoryAudioUDPPort,_s:cProxyCallHistoryVideoUDPPort,_t:cProxyCallHistoryT120TCPPort1,_u:cProxyCallHistoryT120TCPPort2,_v:cProxyCallHistoryT120TCPPort3,_w:cProxyCallHistoryT120TCPPort4,_x:cProxyCallHistoryEndpointType,_y:cProxyCallHistoryEndpointVendor,_z:cProxyCallHistoryRequestBandwidth,_A0:cProxyCallHistoryActualBandwidth,_A1:cProxyCallHistoryAudioCoderRate,_A2:cProxyCallHistoryVideoCoderRate,_A3:cProxyCallHistoryRxAudioPackets,_A4:cProxyCallHistoryRxAudioBytes,_A5:cProxyCallHistoryTxAudioPackets,_A6:cProxyCallHistoryTxAudioBytes,_A7:cProxyCallHistoryRxVideoPackets,_A8:cProxyCallHistoryRxVideoBytes,_A9:cProxyCallHistoryTxVideoPackets,_AA:cProxyCallHistoryTxVideoBytes,_AB:cProxyCallHistoryRxT120Packets,_AC:cProxyCallHistoryRxT120Bytes,_AD:cProxyCallHistoryTxT120Packets,_AE:cProxyCallHistoryTxT120Bytes,'ciscoProxyControlMIBNotificationPrefix':ciscoProxyControlMIBNotificationPrefix,'ciscoProxyControlMIBNotifications':ciscoProxyControlMIBNotifications,'ciscoProxyControlMIBConformance':ciscoProxyControlMIBConformance,'ciscoProxyControlMIBCompliances':ciscoProxyControlMIBCompliances,'ciscoProxyControlMIBCompliance':ciscoProxyControlMIBCompliance,'ciscoProxyControlMIBGroups':ciscoProxyControlMIBGroups,_AF:cProxyCallActiveGroup,_AG:cProxyCallHistoryGroup})