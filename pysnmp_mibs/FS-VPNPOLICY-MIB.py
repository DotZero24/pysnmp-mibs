_l='fsVpnCaCertKeyString'
_k='fsVpnCertKeyString'
_j='fsVpnRemoteIdValue'
_i='fsVpnRemoteIdType'
_h='fsVpnRaAddressPoolName'
_g='fsVpnRaUserName'
_f='group14'
_e='group5'
_d='group2'
_c='group1'
_b='hmacsha512'
_a='hmacsha384'
_Z='hmacsha256'
_Y='xcbcmac'
_X='ahproto'
_W='espproto'
_V='fsVpnPolicyName'
_U='keyId'
_T='ipv6'
_S='email'
_R='fqdn'
_Q='ipv4'
_P='aes256'
_O='aes192'
_N='aes128'
_M='tripledescbc'
_L='descbc'
_K='OctetString'
_J='disable'
_I='enable'
_H='read-create'
_G='not-accessible'
_F='DisplayString'
_E='FS-VPNPOLICY-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
fsVpnPolicy=ModuleIdentity((1,3,6,1,4,1,10876,101,1,143))
if mibBuilder.loadTexts:fsVpnPolicy.setRevisions(('2012-09-05 00:00',))
_FsVpnObjects_ObjectIdentity=ObjectIdentity
fsVpnObjects=_FsVpnObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,143,1))
_FsVpnTable_Object=MibTable
fsVpnTable=_FsVpnTable_Object((1,3,6,1,4,1,10876,101,1,143,1,1))
if mibBuilder.loadTexts:fsVpnTable.setStatus(_A)
_FsVpnEntry_Object=MibTableRow
fsVpnEntry=_FsVpnEntry_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1))
fsVpnEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:fsVpnEntry.setStatus(_A)
class _FsVpnPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_FsVpnPolicyName_Type.__name__=_F
_FsVpnPolicyName_Object=MibTableColumn
fsVpnPolicyName=_FsVpnPolicyName_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,1),_FsVpnPolicyName_Type())
fsVpnPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnPolicyName.setStatus(_A)
class _FsVpnPolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ipsecManual',1),('ikePresharedkey',2),('ikeCertificate',3),('xauth',4),('raVpnPresharedKey',5)))
_FsVpnPolicyType_Type.__name__=_C
_FsVpnPolicyType_Object=MibTableColumn
fsVpnPolicyType=_FsVpnPolicyType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,2),_FsVpnPolicyType_Type())
fsVpnPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnPolicyType.setStatus(_A)
class _FsVpnPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsVpnPolicyPriority_Type.__name__=_C
_FsVpnPolicyPriority_Object=MibTableColumn
fsVpnPolicyPriority=_FsVpnPolicyPriority_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,3),_FsVpnPolicyPriority_Type())
fsVpnPolicyPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnPolicyPriority.setStatus(_A)
_FsVpnTunTermAddrType_Type=InetAddressType
_FsVpnTunTermAddrType_Object=MibTableColumn
fsVpnTunTermAddrType=_FsVpnTunTermAddrType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,4),_FsVpnTunTermAddrType_Type())
fsVpnTunTermAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnTunTermAddrType.setStatus(_A)
_FsVpnLocalTunTermAddr_Type=InetAddress
_FsVpnLocalTunTermAddr_Object=MibTableColumn
fsVpnLocalTunTermAddr=_FsVpnLocalTunTermAddr_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,5),_FsVpnLocalTunTermAddr_Type())
fsVpnLocalTunTermAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnLocalTunTermAddr.setStatus(_A)
_FsVpnRemoteTunTermAddr_Type=InetAddress
_FsVpnRemoteTunTermAddr_Object=MibTableColumn
fsVpnRemoteTunTermAddr=_FsVpnRemoteTunTermAddr_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,6),_FsVpnRemoteTunTermAddr_Type())
fsVpnRemoteTunTermAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRemoteTunTermAddr.setStatus(_A)
_FsVpnProtectNetworkType_Type=InetAddressType
_FsVpnProtectNetworkType_Object=MibTableColumn
fsVpnProtectNetworkType=_FsVpnProtectNetworkType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,7),_FsVpnProtectNetworkType_Type())
fsVpnProtectNetworkType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnProtectNetworkType.setStatus(_A)
_FsVpnLocalProtectNetwork_Type=InetAddress
_FsVpnLocalProtectNetwork_Object=MibTableColumn
fsVpnLocalProtectNetwork=_FsVpnLocalProtectNetwork_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,8),_FsVpnLocalProtectNetwork_Type())
fsVpnLocalProtectNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnLocalProtectNetwork.setStatus(_A)
_FsVpnLocalProtectNetworkPrefixLen_Type=InetAddressPrefixLength
_FsVpnLocalProtectNetworkPrefixLen_Object=MibTableColumn
fsVpnLocalProtectNetworkPrefixLen=_FsVpnLocalProtectNetworkPrefixLen_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,9),_FsVpnLocalProtectNetworkPrefixLen_Type())
fsVpnLocalProtectNetworkPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnLocalProtectNetworkPrefixLen.setStatus(_A)
_FsVpnRemoteProtectNetwork_Type=InetAddress
_FsVpnRemoteProtectNetwork_Object=MibTableColumn
fsVpnRemoteProtectNetwork=_FsVpnRemoteProtectNetwork_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,10),_FsVpnRemoteProtectNetwork_Type())
fsVpnRemoteProtectNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRemoteProtectNetwork.setStatus(_A)
_FsVpnRemoteProtectNetworkPrefixLen_Type=InetAddressPrefixLength
_FsVpnRemoteProtectNetworkPrefixLen_Object=MibTableColumn
fsVpnRemoteProtectNetworkPrefixLen=_FsVpnRemoteProtectNetworkPrefixLen_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,11),_FsVpnRemoteProtectNetworkPrefixLen_Type())
fsVpnRemoteProtectNetworkPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRemoteProtectNetworkPrefixLen.setStatus(_A)
class _FsVpnIkeSrcPortRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_FsVpnIkeSrcPortRange_Type.__name__=_F
_FsVpnIkeSrcPortRange_Object=MibTableColumn
fsVpnIkeSrcPortRange=_FsVpnIkeSrcPortRange_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,12),_FsVpnIkeSrcPortRange_Type())
fsVpnIkeSrcPortRange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkeSrcPortRange.setStatus(_A)
class _FsVpnIkeDstPortRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,11))
_FsVpnIkeDstPortRange_Type.__name__=_F
_FsVpnIkeDstPortRange_Object=MibTableColumn
fsVpnIkeDstPortRange=_FsVpnIkeDstPortRange_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,13),_FsVpnIkeDstPortRange_Type())
fsVpnIkeDstPortRange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkeDstPortRange.setStatus(_A)
class _FsVpnSecurityProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,51)));namedValues=NamedValues(*((_W,50),(_X,51)))
_FsVpnSecurityProtocol_Type.__name__=_C
_FsVpnSecurityProtocol_Object=MibTableColumn
fsVpnSecurityProtocol=_FsVpnSecurityProtocol_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,14),_FsVpnSecurityProtocol_Type())
fsVpnSecurityProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnSecurityProtocol.setStatus(_A)
class _FsVpnInboundSpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2147483647))
_FsVpnInboundSpi_Type.__name__=_C
_FsVpnInboundSpi_Object=MibTableColumn
fsVpnInboundSpi=_FsVpnInboundSpi_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,15),_FsVpnInboundSpi_Type())
fsVpnInboundSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnInboundSpi.setStatus(_A)
class _FsVpnOutboundSpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2147483647))
_FsVpnOutboundSpi_Type.__name__=_C
_FsVpnOutboundSpi_Object=MibTableColumn
fsVpnOutboundSpi=_FsVpnOutboundSpi_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,16),_FsVpnOutboundSpi_Type())
fsVpnOutboundSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnOutboundSpi.setStatus(_A)
class _FsVpnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tunnel',1),('transport',2)))
_FsVpnMode_Type.__name__=_C
_FsVpnMode_Object=MibTableColumn
fsVpnMode=_FsVpnMode_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,17),_FsVpnMode_Type())
fsVpnMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnMode.setStatus(_A)
class _FsVpnAuthAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,12,13,14)));namedValues=NamedValues(*(('hmacmd5',1),('hmacsha1',2),(_Y,5),(_Z,12),(_a,13),(_b,14)))
_FsVpnAuthAlgo_Type.__name__=_C
_FsVpnAuthAlgo_Object=MibTableColumn
fsVpnAuthAlgo=_FsVpnAuthAlgo_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,18),_FsVpnAuthAlgo_Type())
fsVpnAuthAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnAuthAlgo.setStatus(_A)
class _FsVpnAhKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsVpnAhKey_Type.__name__=_K
_FsVpnAhKey_Object=MibTableColumn
fsVpnAhKey=_FsVpnAhKey_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,19),_FsVpnAhKey_Type())
fsVpnAhKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnAhKey.setStatus(_A)
class _FsVpnEncrAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,12,13,14)));namedValues=NamedValues(*((_L,4),(_M,5),(_N,12),(_O,13),(_P,14)))
_FsVpnEncrAlgo_Type.__name__=_C
_FsVpnEncrAlgo_Object=MibTableColumn
fsVpnEncrAlgo=_FsVpnEncrAlgo_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,20),_FsVpnEncrAlgo_Type())
fsVpnEncrAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnEncrAlgo.setStatus(_A)
class _FsVpnEspKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsVpnEspKey_Type.__name__=_K
_FsVpnEspKey_Object=MibTableColumn
fsVpnEspKey=_FsVpnEspKey_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,21),_FsVpnEspKey_Type())
fsVpnEspKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnEspKey.setStatus(_A)
class _FsVpnAntiReplay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsVpnAntiReplay_Type.__name__=_C
_FsVpnAntiReplay_Object=MibTableColumn
fsVpnAntiReplay=_FsVpnAntiReplay_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,22),_FsVpnAntiReplay_Type())
fsVpnAntiReplay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnAntiReplay.setStatus(_A)
class _FsVpnPolicyFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*(('filter',1),('apply',3),('bypass',4)))
_FsVpnPolicyFlag_Type.__name__=_C
_FsVpnPolicyFlag_Object=MibTableColumn
fsVpnPolicyFlag=_FsVpnPolicyFlag_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,23),_FsVpnPolicyFlag_Type())
fsVpnPolicyFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnPolicyFlag.setStatus(_A)
class _FsVpnProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,17,50,51,58,9000)));namedValues=NamedValues(*(('icmpv4',1),('tcp',6),('udp',17),(_W,50),(_X,51),('icmpv6',58),('any',9000)))
_FsVpnProtocol_Type.__name__=_C
_FsVpnProtocol_Object=MibTableColumn
fsVpnProtocol=_FsVpnProtocol_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,24),_FsVpnProtocol_Type())
fsVpnProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnProtocol.setStatus(_A)
_FsVpnPolicyIntfIndex_Type=InterfaceIndexOrZero
_FsVpnPolicyIntfIndex_Object=MibTableColumn
fsVpnPolicyIntfIndex=_FsVpnPolicyIntfIndex_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,25),_FsVpnPolicyIntfIndex_Type())
fsVpnPolicyIntfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnPolicyIntfIndex.setStatus(_A)
class _FsVpnIkePhase1HashAlgo_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,12,13,14)));namedValues=NamedValues(*(('md5',1),('sha1',2),('sha256',12),('sha384',13),('sha512',14)))
_FsVpnIkePhase1HashAlgo_Type.__name__=_C
_FsVpnIkePhase1HashAlgo_Object=MibTableColumn
fsVpnIkePhase1HashAlgo=_FsVpnIkePhase1HashAlgo_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,26),_FsVpnIkePhase1HashAlgo_Type())
fsVpnIkePhase1HashAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1HashAlgo.setStatus(_A)
class _FsVpnIkePhase1EncryptionAlgo_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,12,13,14)));namedValues=NamedValues(*((_L,4),(_M,5),(_N,12),(_O,13),(_P,14)))
_FsVpnIkePhase1EncryptionAlgo_Type.__name__=_C
_FsVpnIkePhase1EncryptionAlgo_Object=MibTableColumn
fsVpnIkePhase1EncryptionAlgo=_FsVpnIkePhase1EncryptionAlgo_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,27),_FsVpnIkePhase1EncryptionAlgo_Type())
fsVpnIkePhase1EncryptionAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1EncryptionAlgo.setStatus(_A)
class _FsVpnIkePhase1DHGroup_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,14)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,5),(_f,14)))
_FsVpnIkePhase1DHGroup_Type.__name__=_C
_FsVpnIkePhase1DHGroup_Object=MibTableColumn
fsVpnIkePhase1DHGroup=_FsVpnIkePhase1DHGroup_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,28),_FsVpnIkePhase1DHGroup_Type())
fsVpnIkePhase1DHGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1DHGroup.setStatus(_A)
class _FsVpnIkePhase1LocalIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,9,11)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,5),('dn',9),(_U,11)))
_FsVpnIkePhase1LocalIdType_Type.__name__=_C
_FsVpnIkePhase1LocalIdType_Object=MibTableColumn
fsVpnIkePhase1LocalIdType=_FsVpnIkePhase1LocalIdType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,29),_FsVpnIkePhase1LocalIdType_Type())
fsVpnIkePhase1LocalIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1LocalIdType.setStatus(_A)
_FsVpnIkePhase1LocalIdValue_Type=DisplayString
_FsVpnIkePhase1LocalIdValue_Object=MibTableColumn
fsVpnIkePhase1LocalIdValue=_FsVpnIkePhase1LocalIdValue_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,30),_FsVpnIkePhase1LocalIdValue_Type())
fsVpnIkePhase1LocalIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1LocalIdValue.setStatus(_A)
class _FsVpnIkePhase1PeerIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,9,11)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,5),('dn',9),(_U,11)))
_FsVpnIkePhase1PeerIdType_Type.__name__=_C
_FsVpnIkePhase1PeerIdType_Object=MibTableColumn
fsVpnIkePhase1PeerIdType=_FsVpnIkePhase1PeerIdType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,31),_FsVpnIkePhase1PeerIdType_Type())
fsVpnIkePhase1PeerIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1PeerIdType.setStatus(_A)
_FsVpnIkePhase1PeerIdValue_Type=DisplayString
_FsVpnIkePhase1PeerIdValue_Object=MibTableColumn
fsVpnIkePhase1PeerIdValue=_FsVpnIkePhase1PeerIdValue_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,32),_FsVpnIkePhase1PeerIdValue_Type())
fsVpnIkePhase1PeerIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1PeerIdValue.setStatus(_A)
class _FsVpnIkePhase1LifeTimeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*(('secs',1),('mins',3),('hrs',4),('days',5)))
_FsVpnIkePhase1LifeTimeType_Type.__name__=_C
_FsVpnIkePhase1LifeTimeType_Object=MibTableColumn
fsVpnIkePhase1LifeTimeType=_FsVpnIkePhase1LifeTimeType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,33),_FsVpnIkePhase1LifeTimeType_Type())
fsVpnIkePhase1LifeTimeType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1LifeTimeType.setStatus(_A)
class _FsVpnIkePhase1LifeTime_Type(Integer32):defaultValue=2400
_FsVpnIkePhase1LifeTime_Type.__name__=_C
_FsVpnIkePhase1LifeTime_Object=MibTableColumn
fsVpnIkePhase1LifeTime=_FsVpnIkePhase1LifeTime_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,34),_FsVpnIkePhase1LifeTime_Type())
fsVpnIkePhase1LifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1LifeTime.setStatus(_A)
class _FsVpnIkePhase1Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('main',2),('aggressive',4)))
_FsVpnIkePhase1Mode_Type.__name__=_C
_FsVpnIkePhase1Mode_Object=MibTableColumn
fsVpnIkePhase1Mode=_FsVpnIkePhase1Mode_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,35),_FsVpnIkePhase1Mode_Type())
fsVpnIkePhase1Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase1Mode.setStatus(_A)
class _FsVpnIkePhase2AuthAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,12,13,14)));namedValues=NamedValues(*(('md5',1),('sha',2),(_Y,5),(_Z,12),(_a,13),(_b,14)))
_FsVpnIkePhase2AuthAlgo_Type.__name__=_C
_FsVpnIkePhase2AuthAlgo_Object=MibTableColumn
fsVpnIkePhase2AuthAlgo=_FsVpnIkePhase2AuthAlgo_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,36),_FsVpnIkePhase2AuthAlgo_Type())
fsVpnIkePhase2AuthAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase2AuthAlgo.setStatus(_A)
class _FsVpnIkePhase2EspEncryptionAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_L,4),(_M,5),('null',11),(_N,12),(_O,13),(_P,14),('aesctr128',15),('aesctr192',16),('aesctr256',17)))
_FsVpnIkePhase2EspEncryptionAlgo_Type.__name__=_C
_FsVpnIkePhase2EspEncryptionAlgo_Object=MibTableColumn
fsVpnIkePhase2EspEncryptionAlgo=_FsVpnIkePhase2EspEncryptionAlgo_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,37),_FsVpnIkePhase2EspEncryptionAlgo_Type())
fsVpnIkePhase2EspEncryptionAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase2EspEncryptionAlgo.setStatus(_A)
class _FsVpnIkePhase2LifeTimeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('secs',1),('kb',2),('mins',3),('hrs',4),('days',5)))
_FsVpnIkePhase2LifeTimeType_Type.__name__=_C
_FsVpnIkePhase2LifeTimeType_Object=MibTableColumn
fsVpnIkePhase2LifeTimeType=_FsVpnIkePhase2LifeTimeType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,38),_FsVpnIkePhase2LifeTimeType_Type())
fsVpnIkePhase2LifeTimeType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase2LifeTimeType.setStatus(_A)
class _FsVpnIkePhase2LifeTime_Type(Integer32):defaultValue=800
_FsVpnIkePhase2LifeTime_Type.__name__=_C
_FsVpnIkePhase2LifeTime_Object=MibTableColumn
fsVpnIkePhase2LifeTime=_FsVpnIkePhase2LifeTime_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,39),_FsVpnIkePhase2LifeTime_Type())
fsVpnIkePhase2LifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase2LifeTime.setStatus(_A)
class _FsVpnIkePhase2DHGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5,14)));namedValues=NamedValues(*(('none',0),(_c,1),(_d,2),(_e,5),(_f,14)))
_FsVpnIkePhase2DHGroup_Type.__name__=_C
_FsVpnIkePhase2DHGroup_Object=MibTableColumn
fsVpnIkePhase2DHGroup=_FsVpnIkePhase2DHGroup_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,40),_FsVpnIkePhase2DHGroup_Type())
fsVpnIkePhase2DHGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkePhase2DHGroup.setStatus(_A)
class _FsVpnIkeVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ikev1',1),('ikev2',2)))
_FsVpnIkeVersion_Type.__name__=_C
_FsVpnIkeVersion_Object=MibTableColumn
fsVpnIkeVersion=_FsVpnIkeVersion_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,41),_FsVpnIkeVersion_Type())
fsVpnIkeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnIkeVersion.setStatus(_A)
class _FsVpnCertAlgoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsa',1),('dsa',2)))
_FsVpnCertAlgoType_Type.__name__=_C
_FsVpnCertAlgoType_Object=MibTableColumn
fsVpnCertAlgoType=_FsVpnCertAlgoType_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,42),_FsVpnCertAlgoType_Type())
fsVpnCertAlgoType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCertAlgoType.setStatus(_A)
_FsVpnPolicyRowStatus_Type=RowStatus
_FsVpnPolicyRowStatus_Object=MibTableColumn
fsVpnPolicyRowStatus=_FsVpnPolicyRowStatus_Object((1,3,6,1,4,1,10876,101,1,143,1,1,1,43),_FsVpnPolicyRowStatus_Type())
fsVpnPolicyRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVpnPolicyRowStatus.setStatus(_A)
_FsVpnRaUsersTable_Object=MibTable
fsVpnRaUsersTable=_FsVpnRaUsersTable_Object((1,3,6,1,4,1,10876,101,1,143,1,2))
if mibBuilder.loadTexts:fsVpnRaUsersTable.setStatus(_A)
_FsVpnRaUsersEntry_Object=MibTableRow
fsVpnRaUsersEntry=_FsVpnRaUsersEntry_Object((1,3,6,1,4,1,10876,101,1,143,1,2,1))
fsVpnRaUsersEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:fsVpnRaUsersEntry.setStatus(_A)
class _FsVpnRaUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsVpnRaUserName_Type.__name__=_F
_FsVpnRaUserName_Object=MibTableColumn
fsVpnRaUserName=_FsVpnRaUserName_Object((1,3,6,1,4,1,10876,101,1,143,1,2,1,1),_FsVpnRaUserName_Type())
fsVpnRaUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnRaUserName.setStatus(_A)
class _FsVpnRaUserSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsVpnRaUserSecret_Type.__name__=_F
_FsVpnRaUserSecret_Object=MibTableColumn
fsVpnRaUserSecret=_FsVpnRaUserSecret_Object((1,3,6,1,4,1,10876,101,1,143,1,2,1,2),_FsVpnRaUserSecret_Type())
fsVpnRaUserSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRaUserSecret.setStatus(_A)
_FsVpnRaUserRowStatus_Type=RowStatus
_FsVpnRaUserRowStatus_Object=MibTableColumn
fsVpnRaUserRowStatus=_FsVpnRaUserRowStatus_Object((1,3,6,1,4,1,10876,101,1,143,1,2,1,3),_FsVpnRaUserRowStatus_Type())
fsVpnRaUserRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVpnRaUserRowStatus.setStatus(_A)
_FsVpnRaAddressPoolTable_Object=MibTable
fsVpnRaAddressPoolTable=_FsVpnRaAddressPoolTable_Object((1,3,6,1,4,1,10876,101,1,143,1,3))
if mibBuilder.loadTexts:fsVpnRaAddressPoolTable.setStatus(_A)
_FsVpnRaAddressPoolEntry_Object=MibTableRow
fsVpnRaAddressPoolEntry=_FsVpnRaAddressPoolEntry_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1))
fsVpnRaAddressPoolEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:fsVpnRaAddressPoolEntry.setStatus(_A)
class _FsVpnRaAddressPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsVpnRaAddressPoolName_Type.__name__=_F
_FsVpnRaAddressPoolName_Object=MibTableColumn
fsVpnRaAddressPoolName=_FsVpnRaAddressPoolName_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1,1),_FsVpnRaAddressPoolName_Type())
fsVpnRaAddressPoolName.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnRaAddressPoolName.setStatus(_A)
_FsVpnRaAddressPoolAddrType_Type=InetAddressType
_FsVpnRaAddressPoolAddrType_Object=MibTableColumn
fsVpnRaAddressPoolAddrType=_FsVpnRaAddressPoolAddrType_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1,2),_FsVpnRaAddressPoolAddrType_Type())
fsVpnRaAddressPoolAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRaAddressPoolAddrType.setStatus(_A)
_FsVpnRaAddressPoolStart_Type=InetAddress
_FsVpnRaAddressPoolStart_Object=MibTableColumn
fsVpnRaAddressPoolStart=_FsVpnRaAddressPoolStart_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1,3),_FsVpnRaAddressPoolStart_Type())
fsVpnRaAddressPoolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRaAddressPoolStart.setStatus(_A)
_FsVpnRaAddressPoolEnd_Type=InetAddress
_FsVpnRaAddressPoolEnd_Object=MibTableColumn
fsVpnRaAddressPoolEnd=_FsVpnRaAddressPoolEnd_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1,4),_FsVpnRaAddressPoolEnd_Type())
fsVpnRaAddressPoolEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRaAddressPoolEnd.setStatus(_A)
_FsVpnRaAddressPoolPrefixLen_Type=InetAddressPrefixLength
_FsVpnRaAddressPoolPrefixLen_Object=MibTableColumn
fsVpnRaAddressPoolPrefixLen=_FsVpnRaAddressPoolPrefixLen_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1,5),_FsVpnRaAddressPoolPrefixLen_Type())
fsVpnRaAddressPoolPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRaAddressPoolPrefixLen.setStatus(_A)
_FsVpnRaAddressPoolRowStatus_Type=RowStatus
_FsVpnRaAddressPoolRowStatus_Object=MibTableColumn
fsVpnRaAddressPoolRowStatus=_FsVpnRaAddressPoolRowStatus_Object((1,3,6,1,4,1,10876,101,1,143,1,3,1,6),_FsVpnRaAddressPoolRowStatus_Type())
fsVpnRaAddressPoolRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVpnRaAddressPoolRowStatus.setStatus(_A)
_FsVpnRemoteIdTable_Object=MibTable
fsVpnRemoteIdTable=_FsVpnRemoteIdTable_Object((1,3,6,1,4,1,10876,101,1,143,1,4))
if mibBuilder.loadTexts:fsVpnRemoteIdTable.setStatus(_A)
_FsVpnRemoteIdEntry_Object=MibTableRow
fsVpnRemoteIdEntry=_FsVpnRemoteIdEntry_Object((1,3,6,1,4,1,10876,101,1,143,1,4,1))
fsVpnRemoteIdEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:fsVpnRemoteIdEntry.setStatus(_A)
class _FsVpnRemoteIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,9,11)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,5),('dn',9),(_U,11)))
_FsVpnRemoteIdType_Type.__name__=_C
_FsVpnRemoteIdType_Object=MibTableColumn
fsVpnRemoteIdType=_FsVpnRemoteIdType_Object((1,3,6,1,4,1,10876,101,1,143,1,4,1,1),_FsVpnRemoteIdType_Type())
fsVpnRemoteIdType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnRemoteIdType.setStatus(_A)
_FsVpnRemoteIdValue_Type=DisplayString
_FsVpnRemoteIdValue_Object=MibTableColumn
fsVpnRemoteIdValue=_FsVpnRemoteIdValue_Object((1,3,6,1,4,1,10876,101,1,143,1,4,1,2),_FsVpnRemoteIdValue_Type())
fsVpnRemoteIdValue.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnRemoteIdValue.setStatus(_A)
_FsVpnRemoteIdKey_Type=DisplayString
_FsVpnRemoteIdKey_Object=MibTableColumn
fsVpnRemoteIdKey=_FsVpnRemoteIdKey_Object((1,3,6,1,4,1,10876,101,1,143,1,4,1,3),_FsVpnRemoteIdKey_Type())
fsVpnRemoteIdKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRemoteIdKey.setStatus(_A)
_FsVpnRemoteIdAuthType_Type=Integer32
_FsVpnRemoteIdAuthType_Object=MibTableColumn
fsVpnRemoteIdAuthType=_FsVpnRemoteIdAuthType_Object((1,3,6,1,4,1,10876,101,1,143,1,4,1,4),_FsVpnRemoteIdAuthType_Type())
fsVpnRemoteIdAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRemoteIdAuthType.setStatus(_A)
_FsVpnRemoteIdStatus_Type=RowStatus
_FsVpnRemoteIdStatus_Object=MibTableColumn
fsVpnRemoteIdStatus=_FsVpnRemoteIdStatus_Object((1,3,6,1,4,1,10876,101,1,143,1,4,1,5),_FsVpnRemoteIdStatus_Type())
fsVpnRemoteIdStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVpnRemoteIdStatus.setStatus(_A)
_FsVpnCertInfoTable_Object=MibTable
fsVpnCertInfoTable=_FsVpnCertInfoTable_Object((1,3,6,1,4,1,10876,101,1,143,1,5))
if mibBuilder.loadTexts:fsVpnCertInfoTable.setStatus(_A)
_FsVpnCertInfoEntry_Object=MibTableRow
fsVpnCertInfoEntry=_FsVpnCertInfoEntry_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1))
fsVpnCertInfoEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:fsVpnCertInfoEntry.setStatus(_A)
_FsVpnCertKeyString_Type=DisplayString
_FsVpnCertKeyString_Object=MibTableColumn
fsVpnCertKeyString=_FsVpnCertKeyString_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1,1),_FsVpnCertKeyString_Type())
fsVpnCertKeyString.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnCertKeyString.setStatus(_A)
class _FsVpnCertKeyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsa',1),('dsa',2)))
_FsVpnCertKeyType_Type.__name__=_C
_FsVpnCertKeyType_Object=MibTableColumn
fsVpnCertKeyType=_FsVpnCertKeyType_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1,2),_FsVpnCertKeyType_Type())
fsVpnCertKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCertKeyType.setStatus(_A)
_FsVpnCertKeyFileName_Type=DisplayString
_FsVpnCertKeyFileName_Object=MibTableColumn
fsVpnCertKeyFileName=_FsVpnCertKeyFileName_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1,3),_FsVpnCertKeyFileName_Type())
fsVpnCertKeyFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCertKeyFileName.setStatus(_A)
_FsVpnCertFileName_Type=DisplayString
_FsVpnCertFileName_Object=MibTableColumn
fsVpnCertFileName=_FsVpnCertFileName_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1,4),_FsVpnCertFileName_Type())
fsVpnCertFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCertFileName.setStatus(_A)
class _FsVpnCertEncodeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pem',1),('der',2)))
_FsVpnCertEncodeType_Type.__name__=_C
_FsVpnCertEncodeType_Object=MibTableColumn
fsVpnCertEncodeType=_FsVpnCertEncodeType_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1,5),_FsVpnCertEncodeType_Type())
fsVpnCertEncodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCertEncodeType.setStatus(_A)
_FsVpnCertStatus_Type=RowStatus
_FsVpnCertStatus_Object=MibTableColumn
fsVpnCertStatus=_FsVpnCertStatus_Object((1,3,6,1,4,1,10876,101,1,143,1,5,1,6),_FsVpnCertStatus_Type())
fsVpnCertStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVpnCertStatus.setStatus(_A)
_FsVpnCaCertInfoTable_Object=MibTable
fsVpnCaCertInfoTable=_FsVpnCaCertInfoTable_Object((1,3,6,1,4,1,10876,101,1,143,1,6))
if mibBuilder.loadTexts:fsVpnCaCertInfoTable.setStatus(_A)
_FsVpnCaCertInfoEntry_Object=MibTableRow
fsVpnCaCertInfoEntry=_FsVpnCaCertInfoEntry_Object((1,3,6,1,4,1,10876,101,1,143,1,6,1))
fsVpnCaCertInfoEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:fsVpnCaCertInfoEntry.setStatus(_A)
_FsVpnCaCertKeyString_Type=DisplayString
_FsVpnCaCertKeyString_Object=MibTableColumn
fsVpnCaCertKeyString=_FsVpnCaCertKeyString_Object((1,3,6,1,4,1,10876,101,1,143,1,6,1,1),_FsVpnCaCertKeyString_Type())
fsVpnCaCertKeyString.setMaxAccess(_G)
if mibBuilder.loadTexts:fsVpnCaCertKeyString.setStatus(_A)
_FsVpnCaCertFileName_Type=DisplayString
_FsVpnCaCertFileName_Object=MibTableColumn
fsVpnCaCertFileName=_FsVpnCaCertFileName_Object((1,3,6,1,4,1,10876,101,1,143,1,6,1,2),_FsVpnCaCertFileName_Type())
fsVpnCaCertFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCaCertFileName.setStatus(_A)
class _FsVpnCaCertEncodeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pem',1),('der',2)))
_FsVpnCaCertEncodeType_Type.__name__=_C
_FsVpnCaCertEncodeType_Object=MibTableColumn
fsVpnCaCertEncodeType=_FsVpnCaCertEncodeType_Object((1,3,6,1,4,1,10876,101,1,143,1,6,1,3),_FsVpnCaCertEncodeType_Type())
fsVpnCaCertEncodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnCaCertEncodeType.setStatus(_A)
_FsVpnCaCertStatus_Type=RowStatus
_FsVpnCaCertStatus_Object=MibTableColumn
fsVpnCaCertStatus=_FsVpnCaCertStatus_Object((1,3,6,1,4,1,10876,101,1,143,1,6,1,4),_FsVpnCaCertStatus_Type())
fsVpnCaCertStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVpnCaCertStatus.setStatus(_A)
_FsVpnScalars_ObjectIdentity=ObjectIdentity
fsVpnScalars=_FsVpnScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,143,2))
class _FsVpnGlobalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsVpnGlobalStatus_Type.__name__=_C
_FsVpnGlobalStatus_Object=MibScalar
fsVpnGlobalStatus=_FsVpnGlobalStatus_Object((1,3,6,1,4,1,10876,101,1,143,2,1),_FsVpnGlobalStatus_Type())
fsVpnGlobalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnGlobalStatus.setStatus(_A)
_FsVpnMaxTunnels_Type=Integer32
_FsVpnMaxTunnels_Object=MibScalar
fsVpnMaxTunnels=_FsVpnMaxTunnels_Object((1,3,6,1,4,1,10876,101,1,143,2,2),_FsVpnMaxTunnels_Type())
fsVpnMaxTunnels.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnMaxTunnels.setStatus(_A)
_FsVpnIpPktsIn_Type=Counter32
_FsVpnIpPktsIn_Object=MibScalar
fsVpnIpPktsIn=_FsVpnIpPktsIn_Object((1,3,6,1,4,1,10876,101,1,143,2,3),_FsVpnIpPktsIn_Type())
fsVpnIpPktsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIpPktsIn.setStatus(_A)
_FsVpnIpPktsOut_Type=Counter32
_FsVpnIpPktsOut_Object=MibScalar
fsVpnIpPktsOut=_FsVpnIpPktsOut_Object((1,3,6,1,4,1,10876,101,1,143,2,4),_FsVpnIpPktsOut_Type())
fsVpnIpPktsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIpPktsOut.setStatus(_A)
_FsVpnPktsSecured_Type=Counter32
_FsVpnPktsSecured_Object=MibScalar
fsVpnPktsSecured=_FsVpnPktsSecured_Object((1,3,6,1,4,1,10876,101,1,143,2,5),_FsVpnPktsSecured_Type())
fsVpnPktsSecured.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnPktsSecured.setStatus(_A)
_FsVpnPktsDropped_Type=Counter32
_FsVpnPktsDropped_Object=MibScalar
fsVpnPktsDropped=_FsVpnPktsDropped_Object((1,3,6,1,4,1,10876,101,1,143,2,6),_FsVpnPktsDropped_Type())
fsVpnPktsDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnPktsDropped.setStatus(_A)
_FsVpnIkeSAsActive_Type=Counter32
_FsVpnIkeSAsActive_Object=MibScalar
fsVpnIkeSAsActive=_FsVpnIkeSAsActive_Object((1,3,6,1,4,1,10876,101,1,143,2,7),_FsVpnIkeSAsActive_Type())
fsVpnIkeSAsActive.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIkeSAsActive.setStatus(_A)
_FsVpnIkeNegotiations_Type=Counter32
_FsVpnIkeNegotiations_Object=MibScalar
fsVpnIkeNegotiations=_FsVpnIkeNegotiations_Object((1,3,6,1,4,1,10876,101,1,143,2,8),_FsVpnIkeNegotiations_Type())
fsVpnIkeNegotiations.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIkeNegotiations.setStatus(_A)
_FsVpnIkeRekeys_Type=Counter32
_FsVpnIkeRekeys_Object=MibScalar
fsVpnIkeRekeys=_FsVpnIkeRekeys_Object((1,3,6,1,4,1,10876,101,1,143,2,9),_FsVpnIkeRekeys_Type())
fsVpnIkeRekeys.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIkeRekeys.setStatus(_A)
_FsVpnIkeNegoFailed_Type=Counter32
_FsVpnIkeNegoFailed_Object=MibScalar
fsVpnIkeNegoFailed=_FsVpnIkeNegoFailed_Object((1,3,6,1,4,1,10876,101,1,143,2,10),_FsVpnIkeNegoFailed_Type())
fsVpnIkeNegoFailed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIkeNegoFailed.setStatus(_A)
_FsVpnIPSecSAsActive_Type=Counter32
_FsVpnIPSecSAsActive_Object=MibScalar
fsVpnIPSecSAsActive=_FsVpnIPSecSAsActive_Object((1,3,6,1,4,1,10876,101,1,143,2,11),_FsVpnIPSecSAsActive_Type())
fsVpnIPSecSAsActive.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIPSecSAsActive.setStatus(_A)
_FsVpnIPSecNegotiations_Type=Counter32
_FsVpnIPSecNegotiations_Object=MibScalar
fsVpnIPSecNegotiations=_FsVpnIPSecNegotiations_Object((1,3,6,1,4,1,10876,101,1,143,2,12),_FsVpnIPSecNegotiations_Type())
fsVpnIPSecNegotiations.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIPSecNegotiations.setStatus(_A)
_FsVpnIPSecNegoFailed_Type=Counter32
_FsVpnIPSecNegoFailed_Object=MibScalar
fsVpnIPSecNegoFailed=_FsVpnIPSecNegoFailed_Object((1,3,6,1,4,1,10876,101,1,143,2,13),_FsVpnIPSecNegoFailed_Type())
fsVpnIPSecNegoFailed.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnIPSecNegoFailed.setStatus(_A)
_FsVpnTotalRekeys_Type=Counter32
_FsVpnTotalRekeys_Object=MibScalar
fsVpnTotalRekeys=_FsVpnTotalRekeys_Object((1,3,6,1,4,1,10876,101,1,143,2,14),_FsVpnTotalRekeys_Type())
fsVpnTotalRekeys.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVpnTotalRekeys.setStatus(_A)
class _FsVpnRaServer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_I,1)))
_FsVpnRaServer_Type.__name__=_C
_FsVpnRaServer_Object=MibScalar
fsVpnRaServer=_FsVpnRaServer_Object((1,3,6,1,4,1,10876,101,1,143,2,15),_FsVpnRaServer_Type())
fsVpnRaServer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnRaServer.setStatus(_A)
class _FsVpnDummyPktGen_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsVpnDummyPktGen_Type.__name__=_C
_FsVpnDummyPktGen_Object=MibScalar
fsVpnDummyPktGen=_FsVpnDummyPktGen_Object((1,3,6,1,4,1,10876,101,1,143,2,16),_FsVpnDummyPktGen_Type())
fsVpnDummyPktGen.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnDummyPktGen.setStatus(_A)
class _FsVpnDummyPktParam_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsVpnDummyPktParam_Type.__name__=_C
_FsVpnDummyPktParam_Object=MibScalar
fsVpnDummyPktParam=_FsVpnDummyPktParam_Object((1,3,6,1,4,1,10876,101,1,143,2,17),_FsVpnDummyPktParam_Type())
fsVpnDummyPktParam.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVpnDummyPktParam.setStatus(_A)
class _FsIkeTraceOption_Type(Integer32):defaultValue=0
_FsIkeTraceOption_Type.__name__=_C
_FsIkeTraceOption_Object=MibScalar
fsIkeTraceOption=_FsIkeTraceOption_Object((1,3,6,1,4,1,10876,101,1,143,2,18),_FsIkeTraceOption_Type())
fsIkeTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIkeTraceOption.setStatus(_A)
class _FsIpsecTraceOption_Type(Integer32):defaultValue=0
_FsIpsecTraceOption_Type.__name__=_C
_FsIpsecTraceOption_Object=MibScalar
fsIpsecTraceOption=_FsIpsecTraceOption_Object((1,3,6,1,4,1,10876,101,1,143,2,19),_FsIpsecTraceOption_Type())
fsIpsecTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpsecTraceOption.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsVpnPolicy':fsVpnPolicy,'fsVpnObjects':fsVpnObjects,'fsVpnTable':fsVpnTable,'fsVpnEntry':fsVpnEntry,_V:fsVpnPolicyName,'fsVpnPolicyType':fsVpnPolicyType,'fsVpnPolicyPriority':fsVpnPolicyPriority,'fsVpnTunTermAddrType':fsVpnTunTermAddrType,'fsVpnLocalTunTermAddr':fsVpnLocalTunTermAddr,'fsVpnRemoteTunTermAddr':fsVpnRemoteTunTermAddr,'fsVpnProtectNetworkType':fsVpnProtectNetworkType,'fsVpnLocalProtectNetwork':fsVpnLocalProtectNetwork,'fsVpnLocalProtectNetworkPrefixLen':fsVpnLocalProtectNetworkPrefixLen,'fsVpnRemoteProtectNetwork':fsVpnRemoteProtectNetwork,'fsVpnRemoteProtectNetworkPrefixLen':fsVpnRemoteProtectNetworkPrefixLen,'fsVpnIkeSrcPortRange':fsVpnIkeSrcPortRange,'fsVpnIkeDstPortRange':fsVpnIkeDstPortRange,'fsVpnSecurityProtocol':fsVpnSecurityProtocol,'fsVpnInboundSpi':fsVpnInboundSpi,'fsVpnOutboundSpi':fsVpnOutboundSpi,'fsVpnMode':fsVpnMode,'fsVpnAuthAlgo':fsVpnAuthAlgo,'fsVpnAhKey':fsVpnAhKey,'fsVpnEncrAlgo':fsVpnEncrAlgo,'fsVpnEspKey':fsVpnEspKey,'fsVpnAntiReplay':fsVpnAntiReplay,'fsVpnPolicyFlag':fsVpnPolicyFlag,'fsVpnProtocol':fsVpnProtocol,'fsVpnPolicyIntfIndex':fsVpnPolicyIntfIndex,'fsVpnIkePhase1HashAlgo':fsVpnIkePhase1HashAlgo,'fsVpnIkePhase1EncryptionAlgo':fsVpnIkePhase1EncryptionAlgo,'fsVpnIkePhase1DHGroup':fsVpnIkePhase1DHGroup,'fsVpnIkePhase1LocalIdType':fsVpnIkePhase1LocalIdType,'fsVpnIkePhase1LocalIdValue':fsVpnIkePhase1LocalIdValue,'fsVpnIkePhase1PeerIdType':fsVpnIkePhase1PeerIdType,'fsVpnIkePhase1PeerIdValue':fsVpnIkePhase1PeerIdValue,'fsVpnIkePhase1LifeTimeType':fsVpnIkePhase1LifeTimeType,'fsVpnIkePhase1LifeTime':fsVpnIkePhase1LifeTime,'fsVpnIkePhase1Mode':fsVpnIkePhase1Mode,'fsVpnIkePhase2AuthAlgo':fsVpnIkePhase2AuthAlgo,'fsVpnIkePhase2EspEncryptionAlgo':fsVpnIkePhase2EspEncryptionAlgo,'fsVpnIkePhase2LifeTimeType':fsVpnIkePhase2LifeTimeType,'fsVpnIkePhase2LifeTime':fsVpnIkePhase2LifeTime,'fsVpnIkePhase2DHGroup':fsVpnIkePhase2DHGroup,'fsVpnIkeVersion':fsVpnIkeVersion,'fsVpnCertAlgoType':fsVpnCertAlgoType,'fsVpnPolicyRowStatus':fsVpnPolicyRowStatus,'fsVpnRaUsersTable':fsVpnRaUsersTable,'fsVpnRaUsersEntry':fsVpnRaUsersEntry,_g:fsVpnRaUserName,'fsVpnRaUserSecret':fsVpnRaUserSecret,'fsVpnRaUserRowStatus':fsVpnRaUserRowStatus,'fsVpnRaAddressPoolTable':fsVpnRaAddressPoolTable,'fsVpnRaAddressPoolEntry':fsVpnRaAddressPoolEntry,_h:fsVpnRaAddressPoolName,'fsVpnRaAddressPoolAddrType':fsVpnRaAddressPoolAddrType,'fsVpnRaAddressPoolStart':fsVpnRaAddressPoolStart,'fsVpnRaAddressPoolEnd':fsVpnRaAddressPoolEnd,'fsVpnRaAddressPoolPrefixLen':fsVpnRaAddressPoolPrefixLen,'fsVpnRaAddressPoolRowStatus':fsVpnRaAddressPoolRowStatus,'fsVpnRemoteIdTable':fsVpnRemoteIdTable,'fsVpnRemoteIdEntry':fsVpnRemoteIdEntry,_i:fsVpnRemoteIdType,_j:fsVpnRemoteIdValue,'fsVpnRemoteIdKey':fsVpnRemoteIdKey,'fsVpnRemoteIdAuthType':fsVpnRemoteIdAuthType,'fsVpnRemoteIdStatus':fsVpnRemoteIdStatus,'fsVpnCertInfoTable':fsVpnCertInfoTable,'fsVpnCertInfoEntry':fsVpnCertInfoEntry,_k:fsVpnCertKeyString,'fsVpnCertKeyType':fsVpnCertKeyType,'fsVpnCertKeyFileName':fsVpnCertKeyFileName,'fsVpnCertFileName':fsVpnCertFileName,'fsVpnCertEncodeType':fsVpnCertEncodeType,'fsVpnCertStatus':fsVpnCertStatus,'fsVpnCaCertInfoTable':fsVpnCaCertInfoTable,'fsVpnCaCertInfoEntry':fsVpnCaCertInfoEntry,_l:fsVpnCaCertKeyString,'fsVpnCaCertFileName':fsVpnCaCertFileName,'fsVpnCaCertEncodeType':fsVpnCaCertEncodeType,'fsVpnCaCertStatus':fsVpnCaCertStatus,'fsVpnScalars':fsVpnScalars,'fsVpnGlobalStatus':fsVpnGlobalStatus,'fsVpnMaxTunnels':fsVpnMaxTunnels,'fsVpnIpPktsIn':fsVpnIpPktsIn,'fsVpnIpPktsOut':fsVpnIpPktsOut,'fsVpnPktsSecured':fsVpnPktsSecured,'fsVpnPktsDropped':fsVpnPktsDropped,'fsVpnIkeSAsActive':fsVpnIkeSAsActive,'fsVpnIkeNegotiations':fsVpnIkeNegotiations,'fsVpnIkeRekeys':fsVpnIkeRekeys,'fsVpnIkeNegoFailed':fsVpnIkeNegoFailed,'fsVpnIPSecSAsActive':fsVpnIPSecSAsActive,'fsVpnIPSecNegotiations':fsVpnIPSecNegotiations,'fsVpnIPSecNegoFailed':fsVpnIPSecNegoFailed,'fsVpnTotalRekeys':fsVpnTotalRekeys,'fsVpnRaServer':fsVpnRaServer,'fsVpnDummyPktGen':fsVpnDummyPktGen,'fsVpnDummyPktParam':fsVpnDummyPktParam,'fsIkeTraceOption':fsIkeTraceOption,'fsIpsecTraceOption':fsIpsecTraceOption})