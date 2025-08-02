_e='esAnomalyIcmpReason'
_d='esAnomalyTcpHdrSize'
_c='esAnomalyTcpFragmentReason'
_b='esAnomalyTcpSeq'
_a='esAnomalyTcpFlag'
_Z='esAnomalyTcpFlagReason'
_Y='extremeIpSecurityViolationType'
_X='extremeIpSecurityMacAddress'
_W='extremeIpSecurityIpAddr'
_V='extremeIpSecurityPortIfIndex'
_U='extremeIpSecurityVlanDescr'
_T='extremeIpSecurityVlanIfIndex'
_S='Integer32'
_R='esAnomalyDestL4Port'
_Q='esAnomalySrcL4Port'
_P='esAnomalyIpProto'
_O='DisplayString'
_N='unknown'
_M='esAnomalyDestIpAddr'
_L='esAnomalyDestIpAddrType'
_K='esAnomalySrcIpAddr'
_J='esAnomalySrcIpAddrType'
_I='esAnomalyVlanTag'
_H='esAnomalyDestMacAddress'
_G='esAnomalySrcMacAddress'
_F='esAnomalyVlanDescr'
_E='esAnomalyVlanIfIndex'
_D='esAnomalyPortIfIndex'
_C='accessible-for-notify'
_B='current'
_A='EXTREME-IP-SECURITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','RowStatus','TextualConvention')
extremeIpSecurity=ModuleIdentity((1,3,6,1,4,1,1916,1,34))
class HexOctet(TextualConvention,OctetString):status=_B;displayHint='2x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class VlanTag(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class IpProtocol(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,6,17)));namedValues=NamedValues(*((_N,0),('icmp',1),('tcp',6),('udp',17)))
class TcpFlagAnomalyReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('flagSynAndSrcPort',1),('flagAndSeq',2),('flagFinAndUrgAandPshandSeq',3),('flagSynAndFin',4)))
class IcmpAnomalyReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('icmpOverSize',1),('icmpFragmented',2)))
class TcpFragmentAnomalyReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('tcpHdrLessSize',1),('tcpFragmented',2)))
_ExtremeIpSecurityTraps_ObjectIdentity=ObjectIdentity
extremeIpSecurityTraps=_ExtremeIpSecurityTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,34,1))
_ExtremeIpSecurityTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeIpSecurityTrapsPrefix=_ExtremeIpSecurityTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,34,1,0))
_ExtremeIpSecurityVlanIfIndex_Type=Integer32
_ExtremeIpSecurityVlanIfIndex_Object=MibScalar
extremeIpSecurityVlanIfIndex=_ExtremeIpSecurityVlanIfIndex_Object((1,3,6,1,4,1,1916,1,34,1,1),_ExtremeIpSecurityVlanIfIndex_Type())
extremeIpSecurityVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIpSecurityVlanIfIndex.setStatus(_B)
class _ExtremeIpSecurityVlanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeIpSecurityVlanDescr_Type.__name__=_O
_ExtremeIpSecurityVlanDescr_Object=MibScalar
extremeIpSecurityVlanDescr=_ExtremeIpSecurityVlanDescr_Object((1,3,6,1,4,1,1916,1,34,1,2),_ExtremeIpSecurityVlanDescr_Type())
extremeIpSecurityVlanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIpSecurityVlanDescr.setStatus(_B)
_ExtremeIpSecurityPortIfIndex_Type=Integer32
_ExtremeIpSecurityPortIfIndex_Object=MibScalar
extremeIpSecurityPortIfIndex=_ExtremeIpSecurityPortIfIndex_Object((1,3,6,1,4,1,1916,1,34,1,3),_ExtremeIpSecurityPortIfIndex_Type())
extremeIpSecurityPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIpSecurityPortIfIndex.setStatus(_B)
_ExtremeIpSecurityIpAddr_Type=IpAddress
_ExtremeIpSecurityIpAddr_Object=MibScalar
extremeIpSecurityIpAddr=_ExtremeIpSecurityIpAddr_Object((1,3,6,1,4,1,1916,1,34,1,4),_ExtremeIpSecurityIpAddr_Type())
extremeIpSecurityIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIpSecurityIpAddr.setStatus(_B)
_ExtremeIpSecurityMacAddress_Type=MacAddress
_ExtremeIpSecurityMacAddress_Object=MibScalar
extremeIpSecurityMacAddress=_ExtremeIpSecurityMacAddress_Object((1,3,6,1,4,1,1916,1,34,1,5),_ExtremeIpSecurityMacAddress_Type())
extremeIpSecurityMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIpSecurityMacAddress.setStatus(_B)
class _ExtremeIpSecurityViolationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('rogueDhcpServerPacket',1),('badIpMacBindingInArpPacket',2),('badIpInArpPacket',3),('badMacInArpPacket',4),('bcastSenderIpInArpPacket',5),('bcastTargetIpInArpPacket',6)))
_ExtremeIpSecurityViolationType_Type.__name__=_S
_ExtremeIpSecurityViolationType_Object=MibScalar
extremeIpSecurityViolationType=_ExtremeIpSecurityViolationType_Object((1,3,6,1,4,1,1916,1,34,1,6),_ExtremeIpSecurityViolationType_Type())
extremeIpSecurityViolationType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeIpSecurityViolationType.setStatus(_B)
_ExtremeIpSecurityAnomalyTraps_ObjectIdentity=ObjectIdentity
extremeIpSecurityAnomalyTraps=_ExtremeIpSecurityAnomalyTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,34,2))
_ExtremeIpSecurityAnomalyTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeIpSecurityAnomalyTrapsPrefix=_ExtremeIpSecurityAnomalyTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,34,2,0))
_EsAnomalyPortIfIndex_Type=Integer32
_EsAnomalyPortIfIndex_Object=MibScalar
esAnomalyPortIfIndex=_EsAnomalyPortIfIndex_Object((1,3,6,1,4,1,1916,1,34,2,1),_EsAnomalyPortIfIndex_Type())
esAnomalyPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyPortIfIndex.setStatus(_B)
_EsAnomalyVlanIfIndex_Type=Integer32
_EsAnomalyVlanIfIndex_Object=MibScalar
esAnomalyVlanIfIndex=_EsAnomalyVlanIfIndex_Object((1,3,6,1,4,1,1916,1,34,2,2),_EsAnomalyVlanIfIndex_Type())
esAnomalyVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyVlanIfIndex.setStatus(_B)
class _EsAnomalyVlanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EsAnomalyVlanDescr_Type.__name__=_O
_EsAnomalyVlanDescr_Object=MibScalar
esAnomalyVlanDescr=_EsAnomalyVlanDescr_Object((1,3,6,1,4,1,1916,1,34,2,3),_EsAnomalyVlanDescr_Type())
esAnomalyVlanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyVlanDescr.setStatus(_B)
_EsAnomalySrcMacAddress_Type=MacAddress
_EsAnomalySrcMacAddress_Object=MibScalar
esAnomalySrcMacAddress=_EsAnomalySrcMacAddress_Object((1,3,6,1,4,1,1916,1,34,2,4),_EsAnomalySrcMacAddress_Type())
esAnomalySrcMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalySrcMacAddress.setStatus(_B)
_EsAnomalyDestMacAddress_Type=MacAddress
_EsAnomalyDestMacAddress_Object=MibScalar
esAnomalyDestMacAddress=_EsAnomalyDestMacAddress_Object((1,3,6,1,4,1,1916,1,34,2,5),_EsAnomalyDestMacAddress_Type())
esAnomalyDestMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyDestMacAddress.setStatus(_B)
_EsAnomalySrcIpAddrType_Type=InetAddressType
_EsAnomalySrcIpAddrType_Object=MibScalar
esAnomalySrcIpAddrType=_EsAnomalySrcIpAddrType_Object((1,3,6,1,4,1,1916,1,34,2,6),_EsAnomalySrcIpAddrType_Type())
esAnomalySrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalySrcIpAddrType.setStatus(_B)
_EsAnomalySrcIpAddr_Type=InetAddress
_EsAnomalySrcIpAddr_Object=MibScalar
esAnomalySrcIpAddr=_EsAnomalySrcIpAddr_Object((1,3,6,1,4,1,1916,1,34,2,7),_EsAnomalySrcIpAddr_Type())
esAnomalySrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalySrcIpAddr.setStatus(_B)
_EsAnomalyDestIpAddrType_Type=InetAddressType
_EsAnomalyDestIpAddrType_Object=MibScalar
esAnomalyDestIpAddrType=_EsAnomalyDestIpAddrType_Object((1,3,6,1,4,1,1916,1,34,2,8),_EsAnomalyDestIpAddrType_Type())
esAnomalyDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyDestIpAddrType.setStatus(_B)
_EsAnomalyDestIpAddr_Type=InetAddress
_EsAnomalyDestIpAddr_Object=MibScalar
esAnomalyDestIpAddr=_EsAnomalyDestIpAddr_Object((1,3,6,1,4,1,1916,1,34,2,9),_EsAnomalyDestIpAddr_Type())
esAnomalyDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyDestIpAddr.setStatus(_B)
_EsAnomalyIpProto_Type=IpProtocol
_EsAnomalyIpProto_Object=MibScalar
esAnomalyIpProto=_EsAnomalyIpProto_Object((1,3,6,1,4,1,1916,1,34,2,10),_EsAnomalyIpProto_Type())
esAnomalyIpProto.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyIpProto.setStatus(_B)
_EsAnomalySrcL4Port_Type=InetPortNumber
_EsAnomalySrcL4Port_Object=MibScalar
esAnomalySrcL4Port=_EsAnomalySrcL4Port_Object((1,3,6,1,4,1,1916,1,34,2,11),_EsAnomalySrcL4Port_Type())
esAnomalySrcL4Port.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalySrcL4Port.setStatus(_B)
_EsAnomalyDestL4Port_Type=InetPortNumber
_EsAnomalyDestL4Port_Object=MibScalar
esAnomalyDestL4Port=_EsAnomalyDestL4Port_Object((1,3,6,1,4,1,1916,1,34,2,12),_EsAnomalyDestL4Port_Type())
esAnomalyDestL4Port.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyDestL4Port.setStatus(_B)
_EsAnomalyTcpFlag_Type=HexOctet
_EsAnomalyTcpFlag_Object=MibScalar
esAnomalyTcpFlag=_EsAnomalyTcpFlag_Object((1,3,6,1,4,1,1916,1,34,2,13),_EsAnomalyTcpFlag_Type())
esAnomalyTcpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyTcpFlag.setStatus(_B)
_EsAnomalyTcpSeq_Type=Integer32
_EsAnomalyTcpSeq_Object=MibScalar
esAnomalyTcpSeq=_EsAnomalyTcpSeq_Object((1,3,6,1,4,1,1916,1,34,2,14),_EsAnomalyTcpSeq_Type())
esAnomalyTcpSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyTcpSeq.setStatus(_B)
_EsAnomalyTcpHdrSize_Type=Integer32
_EsAnomalyTcpHdrSize_Object=MibScalar
esAnomalyTcpHdrSize=_EsAnomalyTcpHdrSize_Object((1,3,6,1,4,1,1916,1,34,2,15),_EsAnomalyTcpHdrSize_Type())
esAnomalyTcpHdrSize.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyTcpHdrSize.setStatus(_B)
_EsAnomalyTcpFlagReason_Type=TcpFlagAnomalyReason
_EsAnomalyTcpFlagReason_Object=MibScalar
esAnomalyTcpFlagReason=_EsAnomalyTcpFlagReason_Object((1,3,6,1,4,1,1916,1,34,2,16),_EsAnomalyTcpFlagReason_Type())
esAnomalyTcpFlagReason.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyTcpFlagReason.setStatus(_B)
_EsAnomalyIcmpReason_Type=IcmpAnomalyReason
_EsAnomalyIcmpReason_Object=MibScalar
esAnomalyIcmpReason=_EsAnomalyIcmpReason_Object((1,3,6,1,4,1,1916,1,34,2,17),_EsAnomalyIcmpReason_Type())
esAnomalyIcmpReason.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyIcmpReason.setStatus(_B)
_EsAnomalyVlanTag_Type=VlanTag
_EsAnomalyVlanTag_Object=MibScalar
esAnomalyVlanTag=_EsAnomalyVlanTag_Object((1,3,6,1,4,1,1916,1,34,2,18),_EsAnomalyVlanTag_Type())
esAnomalyVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyVlanTag.setStatus(_B)
_EsAnomalyTcpFragmentReason_Type=TcpFragmentAnomalyReason
_EsAnomalyTcpFragmentReason_Object=MibScalar
esAnomalyTcpFragmentReason=_EsAnomalyTcpFragmentReason_Object((1,3,6,1,4,1,1916,1,34,2,19),_EsAnomalyTcpFragmentReason_Type())
esAnomalyTcpFragmentReason.setMaxAccess(_C)
if mibBuilder.loadTexts:esAnomalyTcpFragmentReason.setStatus(_B)
extremeIpSecurityViolation=NotificationType((1,3,6,1,4,1,1916,1,34,1,0,1))
extremeIpSecurityViolation.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:extremeIpSecurityViolation.setStatus(_B)
extremeIpSecurityAnomalyIpViolation=NotificationType((1,3,6,1,4,1,1916,1,34,2,0,1))
extremeIpSecurityAnomalyIpViolation.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P)))
if mibBuilder.loadTexts:extremeIpSecurityAnomalyIpViolation.setStatus(_B)
extremeIpSecurityAnomalyL4PortViolation=NotificationType((1,3,6,1,4,1,1916,1,34,2,0,2))
extremeIpSecurityAnomalyL4PortViolation.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:extremeIpSecurityAnomalyL4PortViolation.setStatus(_B)
extremeIpSecurityAnomalyTcpFlagViolation=NotificationType((1,3,6,1,4,1,1916,1,34,2,0,3))
extremeIpSecurityAnomalyTcpFlagViolation.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_Q),(_A,_R),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:extremeIpSecurityAnomalyTcpFlagViolation.setStatus(_B)
extremeIpSecurityAnomalyTcpFragmentViolation=NotificationType((1,3,6,1,4,1,1916,1,34,2,0,4))
extremeIpSecurityAnomalyTcpFragmentViolation.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:extremeIpSecurityAnomalyTcpFragmentViolation.setStatus(_B)
extremeIpSecurityAnomalyIcmpViolation=NotificationType((1,3,6,1,4,1,1916,1,34,2,0,5))
extremeIpSecurityAnomalyIcmpViolation.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_e)))
if mibBuilder.loadTexts:extremeIpSecurityAnomalyIcmpViolation.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HexOctet':HexOctet,'VlanTag':VlanTag,'IpProtocol':IpProtocol,'TcpFlagAnomalyReason':TcpFlagAnomalyReason,'IcmpAnomalyReason':IcmpAnomalyReason,'TcpFragmentAnomalyReason':TcpFragmentAnomalyReason,'extremeIpSecurity':extremeIpSecurity,'extremeIpSecurityTraps':extremeIpSecurityTraps,'extremeIpSecurityTrapsPrefix':extremeIpSecurityTrapsPrefix,'extremeIpSecurityViolation':extremeIpSecurityViolation,_T:extremeIpSecurityVlanIfIndex,_U:extremeIpSecurityVlanDescr,_V:extremeIpSecurityPortIfIndex,_W:extremeIpSecurityIpAddr,_X:extremeIpSecurityMacAddress,_Y:extremeIpSecurityViolationType,'extremeIpSecurityAnomalyTraps':extremeIpSecurityAnomalyTraps,'extremeIpSecurityAnomalyTrapsPrefix':extremeIpSecurityAnomalyTrapsPrefix,'extremeIpSecurityAnomalyIpViolation':extremeIpSecurityAnomalyIpViolation,'extremeIpSecurityAnomalyL4PortViolation':extremeIpSecurityAnomalyL4PortViolation,'extremeIpSecurityAnomalyTcpFlagViolation':extremeIpSecurityAnomalyTcpFlagViolation,'extremeIpSecurityAnomalyTcpFragmentViolation':extremeIpSecurityAnomalyTcpFragmentViolation,'extremeIpSecurityAnomalyIcmpViolation':extremeIpSecurityAnomalyIcmpViolation,_D:esAnomalyPortIfIndex,_E:esAnomalyVlanIfIndex,_F:esAnomalyVlanDescr,_G:esAnomalySrcMacAddress,_H:esAnomalyDestMacAddress,_J:esAnomalySrcIpAddrType,_K:esAnomalySrcIpAddr,_L:esAnomalyDestIpAddrType,_M:esAnomalyDestIpAddr,_P:esAnomalyIpProto,_Q:esAnomalySrcL4Port,_R:esAnomalyDestL4Port,_a:esAnomalyTcpFlag,_b:esAnomalyTcpSeq,_d:esAnomalyTcpHdrSize,_Z:esAnomalyTcpFlagReason,_e:esAnomalyIcmpReason,_I:esAnomalyVlanTag,_c:esAnomalyTcpFragmentReason})