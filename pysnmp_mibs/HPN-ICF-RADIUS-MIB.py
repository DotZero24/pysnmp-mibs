_j='hpnicfRadiusSchAccGroupName'
_i='hpnicfRadiusSchAuthGroupName'
_h='hpnicfRdSecondaryAccUdpPort'
_g='hpnicfRdSecondaryAccVpnName'
_f='hpnicfRdSecondaryAccIpAddr'
_e='hpnicfRdSecondaryAccIpAddrType'
_d='hpnicfRdSecondaryAuthUdpPort'
_c='hpnicfRdSecondaryAuthVpnName'
_b='hpnicfRdSecondaryAuthIpAddr'
_a='hpnicfRdSecondaryAuthIpAddrType'
_Z='extended'
_Y='portal'
_X='iphotel'
_W='standard'
_V='deprecated'
_U='Unsigned32'
_T='radiusAuthServerIndex'
_S='radiusAccServerIndex'
_R='hpnicfRdAccGroupName'
_Q='hpnicfRdGroupName'
_P='radiusAccServerAddress'
_O='radiusAccClientServerPortNumber'
_N='radiusAuthServerAddress'
_M='radiusAuthClientServerPortNumber'
_L='hpnicfRadiusServerFirstTrapTime'
_K='block'
_J='active'
_I='RADIUS-ACC-CLIENT-MIB'
_H='RADIUS-AUTH-CLIENT-MIB'
_G='not-accessible'
_F='read-only'
_E='DisplayString'
_D='HPN-ICF-RADIUS-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
radiusAccClientServerPortNumber,radiusAccServerAddress,radiusAccServerIndex=mibBuilder.importSymbols(_I,_O,_P,_S)
radiusAuthClientServerPortNumber,radiusAuthServerAddress,radiusAuthServerIndex=mibBuilder.importSymbols(_H,_M,_N,_T)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_U,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfRadius=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13))
if mibBuilder.loadTexts:hpnicfRadius.setRevisions(('2014-06-07 18:00',))
_HpnicfRdObjects_ObjectIdentity=ObjectIdentity
hpnicfRdObjects=_HpnicfRdObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,1))
_HpnicfRdInfoTable_Object=MibTable
hpnicfRdInfoTable=_HpnicfRdInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1))
if mibBuilder.loadTexts:hpnicfRdInfoTable.setStatus(_A)
_HpnicfRdInfoEntry_Object=MibTableRow
hpnicfRdInfoEntry=_HpnicfRdInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1))
hpnicfRdInfoEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:hpnicfRdInfoEntry.setStatus(_A)
class _HpnicfRdGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfRdGroupName_Type.__name__=_E
_HpnicfRdGroupName_Object=MibTableColumn
hpnicfRdGroupName=_HpnicfRdGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,1),_HpnicfRdGroupName_Type())
hpnicfRdGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdGroupName.setStatus(_A)
_HpnicfRdPrimAuthIp_Type=IpAddress
_HpnicfRdPrimAuthIp_Object=MibTableColumn
hpnicfRdPrimAuthIp=_HpnicfRdPrimAuthIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,2),_HpnicfRdPrimAuthIp_Type())
hpnicfRdPrimAuthIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAuthIp.setStatus(_V)
_HpnicfRdPrimUdpPort_Type=Integer32
_HpnicfRdPrimUdpPort_Object=MibTableColumn
hpnicfRdPrimUdpPort=_HpnicfRdPrimUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,3),_HpnicfRdPrimUdpPort_Type())
hpnicfRdPrimUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimUdpPort.setStatus(_A)
class _HpnicfRdPrimState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfRdPrimState_Type.__name__=_C
_HpnicfRdPrimState_Object=MibTableColumn
hpnicfRdPrimState=_HpnicfRdPrimState_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,4),_HpnicfRdPrimState_Type())
hpnicfRdPrimState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimState.setStatus(_A)
_HpnicfRdSecAuthIp_Type=IpAddress
_HpnicfRdSecAuthIp_Object=MibTableColumn
hpnicfRdSecAuthIp=_HpnicfRdSecAuthIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,5),_HpnicfRdSecAuthIp_Type())
hpnicfRdSecAuthIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAuthIp.setStatus(_V)
_HpnicfRdSecUdpPort_Type=Integer32
_HpnicfRdSecUdpPort_Object=MibTableColumn
hpnicfRdSecUdpPort=_HpnicfRdSecUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,6),_HpnicfRdSecUdpPort_Type())
hpnicfRdSecUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecUdpPort.setStatus(_A)
class _HpnicfRdSecState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfRdSecState_Type.__name__=_C
_HpnicfRdSecState_Object=MibTableColumn
hpnicfRdSecState=_HpnicfRdSecState_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,7),_HpnicfRdSecState_Type())
hpnicfRdSecState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecState.setStatus(_A)
class _HpnicfRdKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfRdKey_Type.__name__=_E
_HpnicfRdKey_Object=MibTableColumn
hpnicfRdKey=_HpnicfRdKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,8),_HpnicfRdKey_Type())
hpnicfRdKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdKey.setStatus(_A)
_HpnicfRdRetry_Type=Integer32
_HpnicfRdRetry_Object=MibTableColumn
hpnicfRdRetry=_HpnicfRdRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,9),_HpnicfRdRetry_Type())
hpnicfRdRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdRetry.setStatus(_A)
_HpnicfRdTimeout_Type=Integer32
_HpnicfRdTimeout_Object=MibTableColumn
hpnicfRdTimeout=_HpnicfRdTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,10),_HpnicfRdTimeout_Type())
hpnicfRdTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdTimeout.setStatus(_A)
_HpnicfRdPrimAuthIpAddrType_Type=InetAddressType
_HpnicfRdPrimAuthIpAddrType_Object=MibTableColumn
hpnicfRdPrimAuthIpAddrType=_HpnicfRdPrimAuthIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,11),_HpnicfRdPrimAuthIpAddrType_Type())
hpnicfRdPrimAuthIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAuthIpAddrType.setStatus(_A)
_HpnicfRdPrimAuthIpAddr_Type=InetAddress
_HpnicfRdPrimAuthIpAddr_Object=MibTableColumn
hpnicfRdPrimAuthIpAddr=_HpnicfRdPrimAuthIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,12),_HpnicfRdPrimAuthIpAddr_Type())
hpnicfRdPrimAuthIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAuthIpAddr.setStatus(_A)
_HpnicfRdSecAuthIpAddrType_Type=InetAddressType
_HpnicfRdSecAuthIpAddrType_Object=MibTableColumn
hpnicfRdSecAuthIpAddrType=_HpnicfRdSecAuthIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,13),_HpnicfRdSecAuthIpAddrType_Type())
hpnicfRdSecAuthIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAuthIpAddrType.setStatus(_A)
_HpnicfRdSecAuthIpAddr_Type=InetAddress
_HpnicfRdSecAuthIpAddr_Object=MibTableColumn
hpnicfRdSecAuthIpAddr=_HpnicfRdSecAuthIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,14),_HpnicfRdSecAuthIpAddr_Type())
hpnicfRdSecAuthIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAuthIpAddr.setStatus(_A)
class _HpnicfRdServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4)))
_HpnicfRdServerType_Type.__name__=_C
_HpnicfRdServerType_Object=MibTableColumn
hpnicfRdServerType=_HpnicfRdServerType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,15),_HpnicfRdServerType_Type())
hpnicfRdServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdServerType.setStatus(_A)
class _HpnicfRdQuietTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfRdQuietTime_Type.__name__=_C
_HpnicfRdQuietTime_Object=MibTableColumn
hpnicfRdQuietTime=_HpnicfRdQuietTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,16),_HpnicfRdQuietTime_Type())
hpnicfRdQuietTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdQuietTime.setStatus(_A)
class _HpnicfRdUserNameFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('withoutdomain',1),('withdomain',2),('keeporignal',3)))
_HpnicfRdUserNameFormat_Type.__name__=_C
_HpnicfRdUserNameFormat_Object=MibTableColumn
hpnicfRdUserNameFormat=_HpnicfRdUserNameFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,17),_HpnicfRdUserNameFormat_Type())
hpnicfRdUserNameFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdUserNameFormat.setStatus(_A)
_HpnicfRdRowStatus_Type=RowStatus
_HpnicfRdRowStatus_Object=MibTableColumn
hpnicfRdRowStatus=_HpnicfRdRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,18),_HpnicfRdRowStatus_Type())
hpnicfRdRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdRowStatus.setStatus(_A)
class _HpnicfRdSecKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfRdSecKey_Type.__name__=_E
_HpnicfRdSecKey_Object=MibTableColumn
hpnicfRdSecKey=_HpnicfRdSecKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,19),_HpnicfRdSecKey_Type())
hpnicfRdSecKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecKey.setStatus(_A)
class _HpnicfRdPrimVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfRdPrimVpnName_Type.__name__=_E
_HpnicfRdPrimVpnName_Object=MibTableColumn
hpnicfRdPrimVpnName=_HpnicfRdPrimVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,20),_HpnicfRdPrimVpnName_Type())
hpnicfRdPrimVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimVpnName.setStatus(_A)
class _HpnicfRdSecVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfRdSecVpnName_Type.__name__=_E
_HpnicfRdSecVpnName_Object=MibTableColumn
hpnicfRdSecVpnName=_HpnicfRdSecVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,21),_HpnicfRdSecVpnName_Type())
hpnicfRdSecVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecVpnName.setStatus(_A)
_HpnicfRdAuthNasIpAddrType_Type=InetAddressType
_HpnicfRdAuthNasIpAddrType_Object=MibTableColumn
hpnicfRdAuthNasIpAddrType=_HpnicfRdAuthNasIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,22),_HpnicfRdAuthNasIpAddrType_Type())
hpnicfRdAuthNasIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAuthNasIpAddrType.setStatus(_A)
_HpnicfRdAuthNasIpAddr_Type=IpAddress
_HpnicfRdAuthNasIpAddr_Object=MibTableColumn
hpnicfRdAuthNasIpAddr=_HpnicfRdAuthNasIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,23),_HpnicfRdAuthNasIpAddr_Type())
hpnicfRdAuthNasIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAuthNasIpAddr.setStatus(_A)
_HpnicfRdAuthNasIpv6Addr_Type=Ipv6Address
_HpnicfRdAuthNasIpv6Addr_Object=MibTableColumn
hpnicfRdAuthNasIpv6Addr=_HpnicfRdAuthNasIpv6Addr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,1,1,24),_HpnicfRdAuthNasIpv6Addr_Type())
hpnicfRdAuthNasIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAuthNasIpv6Addr.setStatus(_A)
_HpnicfRdAccInfoTable_Object=MibTable
hpnicfRdAccInfoTable=_HpnicfRdAccInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2))
if mibBuilder.loadTexts:hpnicfRdAccInfoTable.setStatus(_A)
_HpnicfRdAccInfoEntry_Object=MibTableRow
hpnicfRdAccInfoEntry=_HpnicfRdAccInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1))
hpnicfRdAccInfoEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:hpnicfRdAccInfoEntry.setStatus(_A)
class _HpnicfRdAccGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfRdAccGroupName_Type.__name__=_E
_HpnicfRdAccGroupName_Object=MibTableColumn
hpnicfRdAccGroupName=_HpnicfRdAccGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,1),_HpnicfRdAccGroupName_Type())
hpnicfRdAccGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdAccGroupName.setStatus(_A)
_HpnicfRdPrimAccIpAddrType_Type=InetAddressType
_HpnicfRdPrimAccIpAddrType_Object=MibTableColumn
hpnicfRdPrimAccIpAddrType=_HpnicfRdPrimAccIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,2),_HpnicfRdPrimAccIpAddrType_Type())
hpnicfRdPrimAccIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAccIpAddrType.setStatus(_A)
_HpnicfRdPrimAccIpAddr_Type=InetAddress
_HpnicfRdPrimAccIpAddr_Object=MibTableColumn
hpnicfRdPrimAccIpAddr=_HpnicfRdPrimAccIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,3),_HpnicfRdPrimAccIpAddr_Type())
hpnicfRdPrimAccIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAccIpAddr.setStatus(_A)
_HpnicfRdPrimAccUdpPort_Type=Integer32
_HpnicfRdPrimAccUdpPort_Object=MibTableColumn
hpnicfRdPrimAccUdpPort=_HpnicfRdPrimAccUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,4),_HpnicfRdPrimAccUdpPort_Type())
hpnicfRdPrimAccUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAccUdpPort.setStatus(_A)
class _HpnicfRdPrimAccState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfRdPrimAccState_Type.__name__=_C
_HpnicfRdPrimAccState_Object=MibTableColumn
hpnicfRdPrimAccState=_HpnicfRdPrimAccState_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,5),_HpnicfRdPrimAccState_Type())
hpnicfRdPrimAccState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAccState.setStatus(_A)
_HpnicfRdSecAccIpAddrType_Type=InetAddressType
_HpnicfRdSecAccIpAddrType_Object=MibTableColumn
hpnicfRdSecAccIpAddrType=_HpnicfRdSecAccIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,6),_HpnicfRdSecAccIpAddrType_Type())
hpnicfRdSecAccIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAccIpAddrType.setStatus(_A)
_HpnicfRdSecAccIpAddr_Type=InetAddress
_HpnicfRdSecAccIpAddr_Object=MibTableColumn
hpnicfRdSecAccIpAddr=_HpnicfRdSecAccIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,7),_HpnicfRdSecAccIpAddr_Type())
hpnicfRdSecAccIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAccIpAddr.setStatus(_A)
_HpnicfRdSecAccUdpPort_Type=Integer32
_HpnicfRdSecAccUdpPort_Object=MibTableColumn
hpnicfRdSecAccUdpPort=_HpnicfRdSecAccUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,8),_HpnicfRdSecAccUdpPort_Type())
hpnicfRdSecAccUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAccUdpPort.setStatus(_A)
class _HpnicfRdSecAccState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfRdSecAccState_Type.__name__=_C
_HpnicfRdSecAccState_Object=MibTableColumn
hpnicfRdSecAccState=_HpnicfRdSecAccState_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,9),_HpnicfRdSecAccState_Type())
hpnicfRdSecAccState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAccState.setStatus(_A)
class _HpnicfRdAccKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfRdAccKey_Type.__name__=_E
_HpnicfRdAccKey_Object=MibTableColumn
hpnicfRdAccKey=_HpnicfRdAccKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,10),_HpnicfRdAccKey_Type())
hpnicfRdAccKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccKey.setStatus(_A)
_HpnicfRdAccRetry_Type=Integer32
_HpnicfRdAccRetry_Object=MibTableColumn
hpnicfRdAccRetry=_HpnicfRdAccRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,11),_HpnicfRdAccRetry_Type())
hpnicfRdAccRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccRetry.setStatus(_A)
_HpnicfRdAccTimeout_Type=Integer32
_HpnicfRdAccTimeout_Object=MibTableColumn
hpnicfRdAccTimeout=_HpnicfRdAccTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,12),_HpnicfRdAccTimeout_Type())
hpnicfRdAccTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccTimeout.setStatus(_A)
class _HpnicfRdAccServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4)))
_HpnicfRdAccServerType_Type.__name__=_C
_HpnicfRdAccServerType_Object=MibTableColumn
hpnicfRdAccServerType=_HpnicfRdAccServerType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,13),_HpnicfRdAccServerType_Type())
hpnicfRdAccServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccServerType.setStatus(_A)
class _HpnicfRdAccQuietTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfRdAccQuietTime_Type.__name__=_C
_HpnicfRdAccQuietTime_Object=MibTableColumn
hpnicfRdAccQuietTime=_HpnicfRdAccQuietTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,14),_HpnicfRdAccQuietTime_Type())
hpnicfRdAccQuietTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccQuietTime.setStatus(_A)
class _HpnicfRdAccFailureAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('reject',2)))
_HpnicfRdAccFailureAction_Type.__name__=_C
_HpnicfRdAccFailureAction_Object=MibTableColumn
hpnicfRdAccFailureAction=_HpnicfRdAccFailureAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,15),_HpnicfRdAccFailureAction_Type())
hpnicfRdAccFailureAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccFailureAction.setStatus(_A)
class _HpnicfRdAccRealTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HpnicfRdAccRealTime_Type.__name__=_C
_HpnicfRdAccRealTime_Object=MibTableColumn
hpnicfRdAccRealTime=_HpnicfRdAccRealTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,16),_HpnicfRdAccRealTime_Type())
hpnicfRdAccRealTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccRealTime.setStatus(_A)
class _HpnicfRdAccRealTimeRetry_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfRdAccRealTimeRetry_Type.__name__=_C
_HpnicfRdAccRealTimeRetry_Object=MibTableColumn
hpnicfRdAccRealTimeRetry=_HpnicfRdAccRealTimeRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,17),_HpnicfRdAccRealTimeRetry_Type())
hpnicfRdAccRealTimeRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccRealTimeRetry.setStatus(_A)
_HpnicfRdAccSaveStopPktEnable_Type=TruthValue
_HpnicfRdAccSaveStopPktEnable_Object=MibTableColumn
hpnicfRdAccSaveStopPktEnable=_HpnicfRdAccSaveStopPktEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,18),_HpnicfRdAccSaveStopPktEnable_Type())
hpnicfRdAccSaveStopPktEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccSaveStopPktEnable.setStatus(_A)
class _HpnicfRdAccStopRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_HpnicfRdAccStopRetry_Type.__name__=_C
_HpnicfRdAccStopRetry_Object=MibTableColumn
hpnicfRdAccStopRetry=_HpnicfRdAccStopRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,19),_HpnicfRdAccStopRetry_Type())
hpnicfRdAccStopRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccStopRetry.setStatus(_A)
class _HpnicfRdAccDataFlowUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('byte',1),('kiloByte',2),('megaByte',3),('gigaByte',4)))
_HpnicfRdAccDataFlowUnit_Type.__name__=_C
_HpnicfRdAccDataFlowUnit_Object=MibTableColumn
hpnicfRdAccDataFlowUnit=_HpnicfRdAccDataFlowUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,20),_HpnicfRdAccDataFlowUnit_Type())
hpnicfRdAccDataFlowUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccDataFlowUnit.setStatus(_A)
class _HpnicfRdAccPacketUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onePacket',1),('kiloPacket',2),('megaPacket',3),('gigaPacket',4)))
_HpnicfRdAccPacketUnit_Type.__name__=_C
_HpnicfRdAccPacketUnit_Object=MibTableColumn
hpnicfRdAccPacketUnit=_HpnicfRdAccPacketUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,21),_HpnicfRdAccPacketUnit_Type())
hpnicfRdAccPacketUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccPacketUnit.setStatus(_A)
_HpnicfRdAccRowStatus_Type=RowStatus
_HpnicfRdAccRowStatus_Object=MibTableColumn
hpnicfRdAccRowStatus=_HpnicfRdAccRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,22),_HpnicfRdAccRowStatus_Type())
hpnicfRdAccRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccRowStatus.setStatus(_A)
_HpnicfRdAcctOnEnable_Type=TruthValue
_HpnicfRdAcctOnEnable_Object=MibTableColumn
hpnicfRdAcctOnEnable=_HpnicfRdAcctOnEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,23),_HpnicfRdAcctOnEnable_Type())
hpnicfRdAcctOnEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAcctOnEnable.setStatus(_A)
class _HpnicfRdAcctOnSendTimes_Type(Integer32):defaultValue=50
_HpnicfRdAcctOnSendTimes_Type.__name__=_C
_HpnicfRdAcctOnSendTimes_Object=MibTableColumn
hpnicfRdAcctOnSendTimes=_HpnicfRdAcctOnSendTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,24),_HpnicfRdAcctOnSendTimes_Type())
hpnicfRdAcctOnSendTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAcctOnSendTimes.setStatus(_A)
class _HpnicfRdAcctOnSendInterval_Type(Integer32):defaultValue=3
_HpnicfRdAcctOnSendInterval_Type.__name__=_C
_HpnicfRdAcctOnSendInterval_Object=MibTableColumn
hpnicfRdAcctOnSendInterval=_HpnicfRdAcctOnSendInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,25),_HpnicfRdAcctOnSendInterval_Type())
hpnicfRdAcctOnSendInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAcctOnSendInterval.setStatus(_A)
class _HpnicfRdSecAccKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfRdSecAccKey_Type.__name__=_E
_HpnicfRdSecAccKey_Object=MibTableColumn
hpnicfRdSecAccKey=_HpnicfRdSecAccKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,26),_HpnicfRdSecAccKey_Type())
hpnicfRdSecAccKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAccKey.setStatus(_A)
class _HpnicfRdPrimAccVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfRdPrimAccVpnName_Type.__name__=_E
_HpnicfRdPrimAccVpnName_Object=MibTableColumn
hpnicfRdPrimAccVpnName=_HpnicfRdPrimAccVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,27),_HpnicfRdPrimAccVpnName_Type())
hpnicfRdPrimAccVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdPrimAccVpnName.setStatus(_A)
class _HpnicfRdSecAccVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfRdSecAccVpnName_Type.__name__=_E
_HpnicfRdSecAccVpnName_Object=MibTableColumn
hpnicfRdSecAccVpnName=_HpnicfRdSecAccVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,28),_HpnicfRdSecAccVpnName_Type())
hpnicfRdSecAccVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecAccVpnName.setStatus(_A)
_HpnicfRdAccNasIpAddrType_Type=InetAddressType
_HpnicfRdAccNasIpAddrType_Object=MibTableColumn
hpnicfRdAccNasIpAddrType=_HpnicfRdAccNasIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,29),_HpnicfRdAccNasIpAddrType_Type())
hpnicfRdAccNasIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccNasIpAddrType.setStatus(_A)
_HpnicfRdAccNasIpAddr_Type=IpAddress
_HpnicfRdAccNasIpAddr_Object=MibTableColumn
hpnicfRdAccNasIpAddr=_HpnicfRdAccNasIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,30),_HpnicfRdAccNasIpAddr_Type())
hpnicfRdAccNasIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccNasIpAddr.setStatus(_A)
_HpnicfRdAccNasIpv6Addr_Type=Ipv6Address
_HpnicfRdAccNasIpv6Addr_Object=MibTableColumn
hpnicfRdAccNasIpv6Addr=_HpnicfRdAccNasIpv6Addr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,2,1,31),_HpnicfRdAccNasIpv6Addr_Type())
hpnicfRdAccNasIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdAccNasIpv6Addr.setStatus(_A)
_HpnicfRadiusGlobalConfig_ObjectIdentity=ObjectIdentity
hpnicfRadiusGlobalConfig=_HpnicfRadiusGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,1,3))
class _HpnicfRadiusAuthErrThreshold_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfRadiusAuthErrThreshold_Type.__name__=_U
_HpnicfRadiusAuthErrThreshold_Object=MibScalar
hpnicfRadiusAuthErrThreshold=_HpnicfRadiusAuthErrThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,3,1),_HpnicfRadiusAuthErrThreshold_Type())
hpnicfRadiusAuthErrThreshold.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfRadiusAuthErrThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRadiusAuthErrThreshold.setUnits('percentage')
_HpnicfRdSecondaryAuthServerTable_Object=MibTable
hpnicfRdSecondaryAuthServerTable=_HpnicfRdSecondaryAuthServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4))
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthServerTable.setStatus(_A)
_HpnicfRdSecondaryAuthServerEntry_Object=MibTableRow
hpnicfRdSecondaryAuthServerEntry=_HpnicfRdSecondaryAuthServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1))
hpnicfRdSecondaryAuthServerEntry.setIndexNames((0,_D,_Q),(0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthServerEntry.setStatus(_A)
_HpnicfRdSecondaryAuthIpAddrType_Type=InetAddressType
_HpnicfRdSecondaryAuthIpAddrType_Object=MibTableColumn
hpnicfRdSecondaryAuthIpAddrType=_HpnicfRdSecondaryAuthIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,1),_HpnicfRdSecondaryAuthIpAddrType_Type())
hpnicfRdSecondaryAuthIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthIpAddrType.setStatus(_A)
_HpnicfRdSecondaryAuthIpAddr_Type=InetAddress
_HpnicfRdSecondaryAuthIpAddr_Object=MibTableColumn
hpnicfRdSecondaryAuthIpAddr=_HpnicfRdSecondaryAuthIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,2),_HpnicfRdSecondaryAuthIpAddr_Type())
hpnicfRdSecondaryAuthIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthIpAddr.setStatus(_A)
class _HpnicfRdSecondaryAuthVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfRdSecondaryAuthVpnName_Type.__name__=_E
_HpnicfRdSecondaryAuthVpnName_Object=MibTableColumn
hpnicfRdSecondaryAuthVpnName=_HpnicfRdSecondaryAuthVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,3),_HpnicfRdSecondaryAuthVpnName_Type())
hpnicfRdSecondaryAuthVpnName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthVpnName.setStatus(_A)
class _HpnicfRdSecondaryAuthUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfRdSecondaryAuthUdpPort_Type.__name__=_C
_HpnicfRdSecondaryAuthUdpPort_Object=MibTableColumn
hpnicfRdSecondaryAuthUdpPort=_HpnicfRdSecondaryAuthUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,4),_HpnicfRdSecondaryAuthUdpPort_Type())
hpnicfRdSecondaryAuthUdpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthUdpPort.setStatus(_A)
class _HpnicfRdSecondaryAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfRdSecondaryAuthState_Type.__name__=_C
_HpnicfRdSecondaryAuthState_Object=MibTableColumn
hpnicfRdSecondaryAuthState=_HpnicfRdSecondaryAuthState_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,5),_HpnicfRdSecondaryAuthState_Type())
hpnicfRdSecondaryAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthState.setStatus(_A)
class _HpnicfRdSecondaryAuthKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfRdSecondaryAuthKey_Type.__name__=_E
_HpnicfRdSecondaryAuthKey_Object=MibTableColumn
hpnicfRdSecondaryAuthKey=_HpnicfRdSecondaryAuthKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,6),_HpnicfRdSecondaryAuthKey_Type())
hpnicfRdSecondaryAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthKey.setStatus(_A)
_HpnicfRdSecondaryAuthRowStatus_Type=RowStatus
_HpnicfRdSecondaryAuthRowStatus_Object=MibTableColumn
hpnicfRdSecondaryAuthRowStatus=_HpnicfRdSecondaryAuthRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,4,1,7),_HpnicfRdSecondaryAuthRowStatus_Type())
hpnicfRdSecondaryAuthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecondaryAuthRowStatus.setStatus(_A)
_HpnicfRdSecondaryAccServerTable_Object=MibTable
hpnicfRdSecondaryAccServerTable=_HpnicfRdSecondaryAccServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5))
if mibBuilder.loadTexts:hpnicfRdSecondaryAccServerTable.setStatus(_A)
_HpnicfRdSecondaryAccServerEntry_Object=MibTableRow
hpnicfRdSecondaryAccServerEntry=_HpnicfRdSecondaryAccServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1))
hpnicfRdSecondaryAccServerEntry.setIndexNames((0,_D,_R),(0,_D,_e),(0,_D,_f),(0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:hpnicfRdSecondaryAccServerEntry.setStatus(_A)
_HpnicfRdSecondaryAccIpAddrType_Type=InetAddressType
_HpnicfRdSecondaryAccIpAddrType_Object=MibTableColumn
hpnicfRdSecondaryAccIpAddrType=_HpnicfRdSecondaryAccIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,1),_HpnicfRdSecondaryAccIpAddrType_Type())
hpnicfRdSecondaryAccIpAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccIpAddrType.setStatus(_A)
_HpnicfRdSecondaryAccIpAddr_Type=InetAddress
_HpnicfRdSecondaryAccIpAddr_Object=MibTableColumn
hpnicfRdSecondaryAccIpAddr=_HpnicfRdSecondaryAccIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,2),_HpnicfRdSecondaryAccIpAddr_Type())
hpnicfRdSecondaryAccIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccIpAddr.setStatus(_A)
class _HpnicfRdSecondaryAccVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfRdSecondaryAccVpnName_Type.__name__=_E
_HpnicfRdSecondaryAccVpnName_Object=MibTableColumn
hpnicfRdSecondaryAccVpnName=_HpnicfRdSecondaryAccVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,3),_HpnicfRdSecondaryAccVpnName_Type())
hpnicfRdSecondaryAccVpnName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccVpnName.setStatus(_A)
class _HpnicfRdSecondaryAccUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfRdSecondaryAccUdpPort_Type.__name__=_C
_HpnicfRdSecondaryAccUdpPort_Object=MibTableColumn
hpnicfRdSecondaryAccUdpPort=_HpnicfRdSecondaryAccUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,4),_HpnicfRdSecondaryAccUdpPort_Type())
hpnicfRdSecondaryAccUdpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccUdpPort.setStatus(_A)
class _HpnicfRdSecondaryAccState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_HpnicfRdSecondaryAccState_Type.__name__=_C
_HpnicfRdSecondaryAccState_Object=MibTableColumn
hpnicfRdSecondaryAccState=_HpnicfRdSecondaryAccState_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,5),_HpnicfRdSecondaryAccState_Type())
hpnicfRdSecondaryAccState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccState.setStatus(_A)
class _HpnicfRdSecondaryAccKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfRdSecondaryAccKey_Type.__name__=_E
_HpnicfRdSecondaryAccKey_Object=MibTableColumn
hpnicfRdSecondaryAccKey=_HpnicfRdSecondaryAccKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,6),_HpnicfRdSecondaryAccKey_Type())
hpnicfRdSecondaryAccKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccKey.setStatus(_A)
_HpnicfRdSecondaryAccRowStatus_Type=RowStatus
_HpnicfRdSecondaryAccRowStatus_Object=MibTableColumn
hpnicfRdSecondaryAccRowStatus=_HpnicfRdSecondaryAccRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,1,5,1,7),_HpnicfRdSecondaryAccRowStatus_Type())
hpnicfRdSecondaryAccRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRdSecondaryAccRowStatus.setStatus(_A)
_HpnicfRadiusAccounting_ObjectIdentity=ObjectIdentity
hpnicfRadiusAccounting=_HpnicfRadiusAccounting_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,2))
_HpnicfRadiusAccClient_ObjectIdentity=ObjectIdentity
hpnicfRadiusAccClient=_HpnicfRadiusAccClient_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1))
_HpnicfRadiusAccServerTable_Object=MibTable
hpnicfRadiusAccServerTable=_HpnicfRadiusAccServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1))
if mibBuilder.loadTexts:hpnicfRadiusAccServerTable.setStatus(_A)
_HpnicfRadiusAccServerEntry_Object=MibTableRow
hpnicfRadiusAccServerEntry=_HpnicfRadiusAccServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1))
hpnicfRadiusAccServerEntry.setIndexNames((0,_I,_S))
if mibBuilder.loadTexts:hpnicfRadiusAccServerEntry.setStatus(_A)
_HpnicfRadiusAccClientStartRequests_Type=Counter32
_HpnicfRadiusAccClientStartRequests_Object=MibTableColumn
hpnicfRadiusAccClientStartRequests=_HpnicfRadiusAccClientStartRequests_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1,1),_HpnicfRadiusAccClientStartRequests_Type())
hpnicfRadiusAccClientStartRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAccClientStartRequests.setStatus(_A)
_HpnicfRadiusAccClientStartResponses_Type=Counter32
_HpnicfRadiusAccClientStartResponses_Object=MibTableColumn
hpnicfRadiusAccClientStartResponses=_HpnicfRadiusAccClientStartResponses_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1,2),_HpnicfRadiusAccClientStartResponses_Type())
hpnicfRadiusAccClientStartResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAccClientStartResponses.setStatus(_A)
_HpnicfRadiusAccClientInterimRequests_Type=Counter32
_HpnicfRadiusAccClientInterimRequests_Object=MibTableColumn
hpnicfRadiusAccClientInterimRequests=_HpnicfRadiusAccClientInterimRequests_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1,3),_HpnicfRadiusAccClientInterimRequests_Type())
hpnicfRadiusAccClientInterimRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAccClientInterimRequests.setStatus(_A)
_HpnicfRadiusAccClientInterimResponses_Type=Counter32
_HpnicfRadiusAccClientInterimResponses_Object=MibTableColumn
hpnicfRadiusAccClientInterimResponses=_HpnicfRadiusAccClientInterimResponses_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1,4),_HpnicfRadiusAccClientInterimResponses_Type())
hpnicfRadiusAccClientInterimResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAccClientInterimResponses.setStatus(_A)
_HpnicfRadiusAccClientStopRequests_Type=Counter32
_HpnicfRadiusAccClientStopRequests_Object=MibTableColumn
hpnicfRadiusAccClientStopRequests=_HpnicfRadiusAccClientStopRequests_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1,5),_HpnicfRadiusAccClientStopRequests_Type())
hpnicfRadiusAccClientStopRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAccClientStopRequests.setStatus(_A)
_HpnicfRadiusAccClientStopResponses_Type=Counter32
_HpnicfRadiusAccClientStopResponses_Object=MibTableColumn
hpnicfRadiusAccClientStopResponses=_HpnicfRadiusAccClientStopResponses_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,2,1,1,1,6),_HpnicfRadiusAccClientStopResponses_Type())
hpnicfRadiusAccClientStopResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAccClientStopResponses.setStatus(_A)
_HpnicfRadiusServerTrap_ObjectIdentity=ObjectIdentity
hpnicfRadiusServerTrap=_HpnicfRadiusServerTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,3))
_HpnicfRadiusServerTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfRadiusServerTrapPrefix=_HpnicfRadiusServerTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,3,0))
_HpnicfRadiusAuthenticating_ObjectIdentity=ObjectIdentity
hpnicfRadiusAuthenticating=_HpnicfRadiusAuthenticating_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,4))
_HpnicfRadiusAuthClient_ObjectIdentity=ObjectIdentity
hpnicfRadiusAuthClient=_HpnicfRadiusAuthClient_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,4,1))
_HpnicfRadiusAuthServerTable_Object=MibTable
hpnicfRadiusAuthServerTable=_HpnicfRadiusAuthServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,4,1,1))
if mibBuilder.loadTexts:hpnicfRadiusAuthServerTable.setStatus(_A)
_HpnicfRadiusAuthServerEntry_Object=MibTableRow
hpnicfRadiusAuthServerEntry=_HpnicfRadiusAuthServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,4,1,1,1))
hpnicfRadiusAuthServerEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:hpnicfRadiusAuthServerEntry.setStatus(_A)
_HpnicfRadiusAuthFailureTimes_Type=Counter32
_HpnicfRadiusAuthFailureTimes_Object=MibTableColumn
hpnicfRadiusAuthFailureTimes=_HpnicfRadiusAuthFailureTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,4,1,1,1,1),_HpnicfRadiusAuthFailureTimes_Type())
hpnicfRadiusAuthFailureTimes.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAuthFailureTimes.setStatus(_A)
_HpnicfRadiusAuthTimeoutTimes_Type=Counter32
_HpnicfRadiusAuthTimeoutTimes_Object=MibTableColumn
hpnicfRadiusAuthTimeoutTimes=_HpnicfRadiusAuthTimeoutTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,4,1,1,1,2),_HpnicfRadiusAuthTimeoutTimes_Type())
hpnicfRadiusAuthTimeoutTimes.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAuthTimeoutTimes.setStatus(_A)
_HpnicfRadiusAuthRejectTimes_Type=Counter32
_HpnicfRadiusAuthRejectTimes_Object=MibTableColumn
hpnicfRadiusAuthRejectTimes=_HpnicfRadiusAuthRejectTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,4,1,1,1,3),_HpnicfRadiusAuthRejectTimes_Type())
hpnicfRadiusAuthRejectTimes.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusAuthRejectTimes.setStatus(_A)
_HpnicfRadiusExtend_ObjectIdentity=ObjectIdentity
hpnicfRadiusExtend=_HpnicfRadiusExtend_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,5))
_HpnicfRadiusExtendObjects_ObjectIdentity=ObjectIdentity
hpnicfRadiusExtendObjects=_HpnicfRadiusExtendObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,5,1))
_HpnicfRadiusExtendTables_ObjectIdentity=ObjectIdentity
hpnicfRadiusExtendTables=_HpnicfRadiusExtendTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2))
_HpnicfRadiusSchAuthTable_Object=MibTable
hpnicfRadiusSchAuthTable=_HpnicfRadiusSchAuthTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1))
if mibBuilder.loadTexts:hpnicfRadiusSchAuthTable.setStatus(_A)
_HpnicfRadiusSchAuthEntry_Object=MibTableRow
hpnicfRadiusSchAuthEntry=_HpnicfRadiusSchAuthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1))
hpnicfRadiusSchAuthEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:hpnicfRadiusSchAuthEntry.setStatus(_A)
_HpnicfRadiusSchAuthGroupName_Type=DisplayString
_HpnicfRadiusSchAuthGroupName_Object=MibTableColumn
hpnicfRadiusSchAuthGroupName=_HpnicfRadiusSchAuthGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,1),_HpnicfRadiusSchAuthGroupName_Type())
hpnicfRadiusSchAuthGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthGroupName.setStatus(_A)
_HpnicfRadiusSchAuthPrimIpAddr_Type=IpAddress
_HpnicfRadiusSchAuthPrimIpAddr_Object=MibTableColumn
hpnicfRadiusSchAuthPrimIpAddr=_HpnicfRadiusSchAuthPrimIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,2),_HpnicfRadiusSchAuthPrimIpAddr_Type())
hpnicfRadiusSchAuthPrimIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthPrimIpAddr.setStatus(_A)
class _HpnicfRadiusSchAuthPrimUdpPort_Type(Integer32):defaultValue=1812
_HpnicfRadiusSchAuthPrimUdpPort_Type.__name__=_C
_HpnicfRadiusSchAuthPrimUdpPort_Object=MibTableColumn
hpnicfRadiusSchAuthPrimUdpPort=_HpnicfRadiusSchAuthPrimUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,3),_HpnicfRadiusSchAuthPrimUdpPort_Type())
hpnicfRadiusSchAuthPrimUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthPrimUdpPort.setStatus(_A)
_HpnicfRadiusSchAuthPrimKey_Type=DisplayString
_HpnicfRadiusSchAuthPrimKey_Object=MibTableColumn
hpnicfRadiusSchAuthPrimKey=_HpnicfRadiusSchAuthPrimKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,4),_HpnicfRadiusSchAuthPrimKey_Type())
hpnicfRadiusSchAuthPrimKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthPrimKey.setStatus(_A)
_HpnicfRadiusSchAuthSecIpAddr_Type=IpAddress
_HpnicfRadiusSchAuthSecIpAddr_Object=MibTableColumn
hpnicfRadiusSchAuthSecIpAddr=_HpnicfRadiusSchAuthSecIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,5),_HpnicfRadiusSchAuthSecIpAddr_Type())
hpnicfRadiusSchAuthSecIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthSecIpAddr.setStatus(_A)
class _HpnicfRadiusSchAuthSecUdpPort_Type(Integer32):defaultValue=1812
_HpnicfRadiusSchAuthSecUdpPort_Type.__name__=_C
_HpnicfRadiusSchAuthSecUdpPort_Object=MibTableColumn
hpnicfRadiusSchAuthSecUdpPort=_HpnicfRadiusSchAuthSecUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,6),_HpnicfRadiusSchAuthSecUdpPort_Type())
hpnicfRadiusSchAuthSecUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthSecUdpPort.setStatus(_A)
_HpnicfRadiusSchAuthSecKey_Type=DisplayString
_HpnicfRadiusSchAuthSecKey_Object=MibTableColumn
hpnicfRadiusSchAuthSecKey=_HpnicfRadiusSchAuthSecKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,7),_HpnicfRadiusSchAuthSecKey_Type())
hpnicfRadiusSchAuthSecKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthSecKey.setStatus(_A)
_HpnicfRadiusSchAuthRowStatus_Type=RowStatus
_HpnicfRadiusSchAuthRowStatus_Object=MibTableColumn
hpnicfRadiusSchAuthRowStatus=_HpnicfRadiusSchAuthRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,1,1,8),_HpnicfRadiusSchAuthRowStatus_Type())
hpnicfRadiusSchAuthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAuthRowStatus.setStatus(_A)
_HpnicfRadiusSchAccTable_Object=MibTable
hpnicfRadiusSchAccTable=_HpnicfRadiusSchAccTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2))
if mibBuilder.loadTexts:hpnicfRadiusSchAccTable.setStatus(_A)
_HpnicfRadiusSchAccEntry_Object=MibTableRow
hpnicfRadiusSchAccEntry=_HpnicfRadiusSchAccEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1))
hpnicfRadiusSchAccEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:hpnicfRadiusSchAccEntry.setStatus(_A)
_HpnicfRadiusSchAccGroupName_Type=DisplayString
_HpnicfRadiusSchAccGroupName_Object=MibTableColumn
hpnicfRadiusSchAccGroupName=_HpnicfRadiusSchAccGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,1),_HpnicfRadiusSchAccGroupName_Type())
hpnicfRadiusSchAccGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRadiusSchAccGroupName.setStatus(_A)
_HpnicfRadiusSchAccPrimIpAddr_Type=IpAddress
_HpnicfRadiusSchAccPrimIpAddr_Object=MibTableColumn
hpnicfRadiusSchAccPrimIpAddr=_HpnicfRadiusSchAccPrimIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,2),_HpnicfRadiusSchAccPrimIpAddr_Type())
hpnicfRadiusSchAccPrimIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccPrimIpAddr.setStatus(_A)
class _HpnicfRadiusSchAccPrimUdpPort_Type(Integer32):defaultValue=1813
_HpnicfRadiusSchAccPrimUdpPort_Type.__name__=_C
_HpnicfRadiusSchAccPrimUdpPort_Object=MibTableColumn
hpnicfRadiusSchAccPrimUdpPort=_HpnicfRadiusSchAccPrimUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,3),_HpnicfRadiusSchAccPrimUdpPort_Type())
hpnicfRadiusSchAccPrimUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccPrimUdpPort.setStatus(_A)
_HpnicfRadiusSchAccPrimKey_Type=DisplayString
_HpnicfRadiusSchAccPrimKey_Object=MibTableColumn
hpnicfRadiusSchAccPrimKey=_HpnicfRadiusSchAccPrimKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,4),_HpnicfRadiusSchAccPrimKey_Type())
hpnicfRadiusSchAccPrimKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccPrimKey.setStatus(_A)
_HpnicfRadiusSchAccSecIpAddr_Type=IpAddress
_HpnicfRadiusSchAccSecIpAddr_Object=MibTableColumn
hpnicfRadiusSchAccSecIpAddr=_HpnicfRadiusSchAccSecIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,5),_HpnicfRadiusSchAccSecIpAddr_Type())
hpnicfRadiusSchAccSecIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccSecIpAddr.setStatus(_A)
class _HpnicfRadiusSchAccSecUdpPort_Type(Integer32):defaultValue=1813
_HpnicfRadiusSchAccSecUdpPort_Type.__name__=_C
_HpnicfRadiusSchAccSecUdpPort_Object=MibTableColumn
hpnicfRadiusSchAccSecUdpPort=_HpnicfRadiusSchAccSecUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,6),_HpnicfRadiusSchAccSecUdpPort_Type())
hpnicfRadiusSchAccSecUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccSecUdpPort.setStatus(_A)
_HpnicfRadiusSchAccSecKey_Type=DisplayString
_HpnicfRadiusSchAccSecKey_Object=MibTableColumn
hpnicfRadiusSchAccSecKey=_HpnicfRadiusSchAccSecKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,7),_HpnicfRadiusSchAccSecKey_Type())
hpnicfRadiusSchAccSecKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccSecKey.setStatus(_A)
_HpnicfRadiusSchAccRowStatus_Type=RowStatus
_HpnicfRadiusSchAccRowStatus_Object=MibTableColumn
hpnicfRadiusSchAccRowStatus=_HpnicfRadiusSchAccRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,5,2,2,1,8),_HpnicfRadiusSchAccRowStatus_Type())
hpnicfRadiusSchAccRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRadiusSchAccRowStatus.setStatus(_A)
_HpnicfRadiusExtendTraps_ObjectIdentity=ObjectIdentity
hpnicfRadiusExtendTraps=_HpnicfRadiusExtendTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,5,3))
_HpnicfRadiusStatistic_ObjectIdentity=ObjectIdentity
hpnicfRadiusStatistic=_HpnicfRadiusStatistic_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,6))
_HpnicfRadiusStatAccReq_Type=Counter64
_HpnicfRadiusStatAccReq_Object=MibScalar
hpnicfRadiusStatAccReq=_HpnicfRadiusStatAccReq_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,6,1),_HpnicfRadiusStatAccReq_Type())
hpnicfRadiusStatAccReq.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusStatAccReq.setStatus(_A)
_HpnicfRadiusStatAccAck_Type=Counter64
_HpnicfRadiusStatAccAck_Object=MibScalar
hpnicfRadiusStatAccAck=_HpnicfRadiusStatAccAck_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,6,2),_HpnicfRadiusStatAccAck_Type())
hpnicfRadiusStatAccAck.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusStatAccAck.setStatus(_A)
_HpnicfRadiusStatLogoutReq_Type=Counter64
_HpnicfRadiusStatLogoutReq_Object=MibScalar
hpnicfRadiusStatLogoutReq=_HpnicfRadiusStatLogoutReq_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,6,3),_HpnicfRadiusStatLogoutReq_Type())
hpnicfRadiusStatLogoutReq.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusStatLogoutReq.setStatus(_A)
_HpnicfRadiusStatLogoutAck_Type=Counter64
_HpnicfRadiusStatLogoutAck_Object=MibScalar
hpnicfRadiusStatLogoutAck=_HpnicfRadiusStatLogoutAck_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,6,4),_HpnicfRadiusStatLogoutAck_Type())
hpnicfRadiusStatLogoutAck.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRadiusStatLogoutAck.setStatus(_A)
_HpnicfRadiusServerTrapVarObjects_ObjectIdentity=ObjectIdentity
hpnicfRadiusServerTrapVarObjects=_HpnicfRadiusServerTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,13,7))
_HpnicfRadiusServerFirstTrapTime_Type=TimeTicks
_HpnicfRadiusServerFirstTrapTime_Object=MibScalar
hpnicfRadiusServerFirstTrapTime=_HpnicfRadiusServerFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,13,7,1),_HpnicfRadiusServerFirstTrapTime_Type())
hpnicfRadiusServerFirstTrapTime.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfRadiusServerFirstTrapTime.setStatus(_A)
hpnicfRadiusAuthServerUpTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,13,3,0,1))
hpnicfRadiusAuthServerUpTrap.setObjects(*((_H,_N),(_H,_M),(_D,_L)))
if mibBuilder.loadTexts:hpnicfRadiusAuthServerUpTrap.setStatus(_A)
hpnicfRadiusAccServerUpTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,13,3,0,2))
hpnicfRadiusAccServerUpTrap.setObjects(*((_I,_P),(_I,_O),(_D,_L)))
if mibBuilder.loadTexts:hpnicfRadiusAccServerUpTrap.setStatus(_A)
hpnicfRadiusAuthErrTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,13,3,0,3))
hpnicfRadiusAuthErrTrap.setObjects(*((_H,_N),(_H,_M)))
if mibBuilder.loadTexts:hpnicfRadiusAuthErrTrap.setStatus(_A)
hpnicfRadiusAuthServerDownTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,13,3,1))
hpnicfRadiusAuthServerDownTrap.setObjects(*((_H,_N),(_H,_M),(_D,_L)))
if mibBuilder.loadTexts:hpnicfRadiusAuthServerDownTrap.setStatus(_A)
hpnicfRadiusAccServerDownTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,13,3,2))
hpnicfRadiusAccServerDownTrap.setObjects(*((_I,_P),(_I,_O),(_D,_L)))
if mibBuilder.loadTexts:hpnicfRadiusAccServerDownTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfRadius':hpnicfRadius,'hpnicfRdObjects':hpnicfRdObjects,'hpnicfRdInfoTable':hpnicfRdInfoTable,'hpnicfRdInfoEntry':hpnicfRdInfoEntry,_Q:hpnicfRdGroupName,'hpnicfRdPrimAuthIp':hpnicfRdPrimAuthIp,'hpnicfRdPrimUdpPort':hpnicfRdPrimUdpPort,'hpnicfRdPrimState':hpnicfRdPrimState,'hpnicfRdSecAuthIp':hpnicfRdSecAuthIp,'hpnicfRdSecUdpPort':hpnicfRdSecUdpPort,'hpnicfRdSecState':hpnicfRdSecState,'hpnicfRdKey':hpnicfRdKey,'hpnicfRdRetry':hpnicfRdRetry,'hpnicfRdTimeout':hpnicfRdTimeout,'hpnicfRdPrimAuthIpAddrType':hpnicfRdPrimAuthIpAddrType,'hpnicfRdPrimAuthIpAddr':hpnicfRdPrimAuthIpAddr,'hpnicfRdSecAuthIpAddrType':hpnicfRdSecAuthIpAddrType,'hpnicfRdSecAuthIpAddr':hpnicfRdSecAuthIpAddr,'hpnicfRdServerType':hpnicfRdServerType,'hpnicfRdQuietTime':hpnicfRdQuietTime,'hpnicfRdUserNameFormat':hpnicfRdUserNameFormat,'hpnicfRdRowStatus':hpnicfRdRowStatus,'hpnicfRdSecKey':hpnicfRdSecKey,'hpnicfRdPrimVpnName':hpnicfRdPrimVpnName,'hpnicfRdSecVpnName':hpnicfRdSecVpnName,'hpnicfRdAuthNasIpAddrType':hpnicfRdAuthNasIpAddrType,'hpnicfRdAuthNasIpAddr':hpnicfRdAuthNasIpAddr,'hpnicfRdAuthNasIpv6Addr':hpnicfRdAuthNasIpv6Addr,'hpnicfRdAccInfoTable':hpnicfRdAccInfoTable,'hpnicfRdAccInfoEntry':hpnicfRdAccInfoEntry,_R:hpnicfRdAccGroupName,'hpnicfRdPrimAccIpAddrType':hpnicfRdPrimAccIpAddrType,'hpnicfRdPrimAccIpAddr':hpnicfRdPrimAccIpAddr,'hpnicfRdPrimAccUdpPort':hpnicfRdPrimAccUdpPort,'hpnicfRdPrimAccState':hpnicfRdPrimAccState,'hpnicfRdSecAccIpAddrType':hpnicfRdSecAccIpAddrType,'hpnicfRdSecAccIpAddr':hpnicfRdSecAccIpAddr,'hpnicfRdSecAccUdpPort':hpnicfRdSecAccUdpPort,'hpnicfRdSecAccState':hpnicfRdSecAccState,'hpnicfRdAccKey':hpnicfRdAccKey,'hpnicfRdAccRetry':hpnicfRdAccRetry,'hpnicfRdAccTimeout':hpnicfRdAccTimeout,'hpnicfRdAccServerType':hpnicfRdAccServerType,'hpnicfRdAccQuietTime':hpnicfRdAccQuietTime,'hpnicfRdAccFailureAction':hpnicfRdAccFailureAction,'hpnicfRdAccRealTime':hpnicfRdAccRealTime,'hpnicfRdAccRealTimeRetry':hpnicfRdAccRealTimeRetry,'hpnicfRdAccSaveStopPktEnable':hpnicfRdAccSaveStopPktEnable,'hpnicfRdAccStopRetry':hpnicfRdAccStopRetry,'hpnicfRdAccDataFlowUnit':hpnicfRdAccDataFlowUnit,'hpnicfRdAccPacketUnit':hpnicfRdAccPacketUnit,'hpnicfRdAccRowStatus':hpnicfRdAccRowStatus,'hpnicfRdAcctOnEnable':hpnicfRdAcctOnEnable,'hpnicfRdAcctOnSendTimes':hpnicfRdAcctOnSendTimes,'hpnicfRdAcctOnSendInterval':hpnicfRdAcctOnSendInterval,'hpnicfRdSecAccKey':hpnicfRdSecAccKey,'hpnicfRdPrimAccVpnName':hpnicfRdPrimAccVpnName,'hpnicfRdSecAccVpnName':hpnicfRdSecAccVpnName,'hpnicfRdAccNasIpAddrType':hpnicfRdAccNasIpAddrType,'hpnicfRdAccNasIpAddr':hpnicfRdAccNasIpAddr,'hpnicfRdAccNasIpv6Addr':hpnicfRdAccNasIpv6Addr,'hpnicfRadiusGlobalConfig':hpnicfRadiusGlobalConfig,'hpnicfRadiusAuthErrThreshold':hpnicfRadiusAuthErrThreshold,'hpnicfRdSecondaryAuthServerTable':hpnicfRdSecondaryAuthServerTable,'hpnicfRdSecondaryAuthServerEntry':hpnicfRdSecondaryAuthServerEntry,_a:hpnicfRdSecondaryAuthIpAddrType,_b:hpnicfRdSecondaryAuthIpAddr,_c:hpnicfRdSecondaryAuthVpnName,_d:hpnicfRdSecondaryAuthUdpPort,'hpnicfRdSecondaryAuthState':hpnicfRdSecondaryAuthState,'hpnicfRdSecondaryAuthKey':hpnicfRdSecondaryAuthKey,'hpnicfRdSecondaryAuthRowStatus':hpnicfRdSecondaryAuthRowStatus,'hpnicfRdSecondaryAccServerTable':hpnicfRdSecondaryAccServerTable,'hpnicfRdSecondaryAccServerEntry':hpnicfRdSecondaryAccServerEntry,_e:hpnicfRdSecondaryAccIpAddrType,_f:hpnicfRdSecondaryAccIpAddr,_g:hpnicfRdSecondaryAccVpnName,_h:hpnicfRdSecondaryAccUdpPort,'hpnicfRdSecondaryAccState':hpnicfRdSecondaryAccState,'hpnicfRdSecondaryAccKey':hpnicfRdSecondaryAccKey,'hpnicfRdSecondaryAccRowStatus':hpnicfRdSecondaryAccRowStatus,'hpnicfRadiusAccounting':hpnicfRadiusAccounting,'hpnicfRadiusAccClient':hpnicfRadiusAccClient,'hpnicfRadiusAccServerTable':hpnicfRadiusAccServerTable,'hpnicfRadiusAccServerEntry':hpnicfRadiusAccServerEntry,'hpnicfRadiusAccClientStartRequests':hpnicfRadiusAccClientStartRequests,'hpnicfRadiusAccClientStartResponses':hpnicfRadiusAccClientStartResponses,'hpnicfRadiusAccClientInterimRequests':hpnicfRadiusAccClientInterimRequests,'hpnicfRadiusAccClientInterimResponses':hpnicfRadiusAccClientInterimResponses,'hpnicfRadiusAccClientStopRequests':hpnicfRadiusAccClientStopRequests,'hpnicfRadiusAccClientStopResponses':hpnicfRadiusAccClientStopResponses,'hpnicfRadiusServerTrap':hpnicfRadiusServerTrap,'hpnicfRadiusServerTrapPrefix':hpnicfRadiusServerTrapPrefix,'hpnicfRadiusAuthServerUpTrap':hpnicfRadiusAuthServerUpTrap,'hpnicfRadiusAccServerUpTrap':hpnicfRadiusAccServerUpTrap,'hpnicfRadiusAuthErrTrap':hpnicfRadiusAuthErrTrap,'hpnicfRadiusAuthServerDownTrap':hpnicfRadiusAuthServerDownTrap,'hpnicfRadiusAccServerDownTrap':hpnicfRadiusAccServerDownTrap,'hpnicfRadiusAuthenticating':hpnicfRadiusAuthenticating,'hpnicfRadiusAuthClient':hpnicfRadiusAuthClient,'hpnicfRadiusAuthServerTable':hpnicfRadiusAuthServerTable,'hpnicfRadiusAuthServerEntry':hpnicfRadiusAuthServerEntry,'hpnicfRadiusAuthFailureTimes':hpnicfRadiusAuthFailureTimes,'hpnicfRadiusAuthTimeoutTimes':hpnicfRadiusAuthTimeoutTimes,'hpnicfRadiusAuthRejectTimes':hpnicfRadiusAuthRejectTimes,'hpnicfRadiusExtend':hpnicfRadiusExtend,'hpnicfRadiusExtendObjects':hpnicfRadiusExtendObjects,'hpnicfRadiusExtendTables':hpnicfRadiusExtendTables,'hpnicfRadiusSchAuthTable':hpnicfRadiusSchAuthTable,'hpnicfRadiusSchAuthEntry':hpnicfRadiusSchAuthEntry,_i:hpnicfRadiusSchAuthGroupName,'hpnicfRadiusSchAuthPrimIpAddr':hpnicfRadiusSchAuthPrimIpAddr,'hpnicfRadiusSchAuthPrimUdpPort':hpnicfRadiusSchAuthPrimUdpPort,'hpnicfRadiusSchAuthPrimKey':hpnicfRadiusSchAuthPrimKey,'hpnicfRadiusSchAuthSecIpAddr':hpnicfRadiusSchAuthSecIpAddr,'hpnicfRadiusSchAuthSecUdpPort':hpnicfRadiusSchAuthSecUdpPort,'hpnicfRadiusSchAuthSecKey':hpnicfRadiusSchAuthSecKey,'hpnicfRadiusSchAuthRowStatus':hpnicfRadiusSchAuthRowStatus,'hpnicfRadiusSchAccTable':hpnicfRadiusSchAccTable,'hpnicfRadiusSchAccEntry':hpnicfRadiusSchAccEntry,_j:hpnicfRadiusSchAccGroupName,'hpnicfRadiusSchAccPrimIpAddr':hpnicfRadiusSchAccPrimIpAddr,'hpnicfRadiusSchAccPrimUdpPort':hpnicfRadiusSchAccPrimUdpPort,'hpnicfRadiusSchAccPrimKey':hpnicfRadiusSchAccPrimKey,'hpnicfRadiusSchAccSecIpAddr':hpnicfRadiusSchAccSecIpAddr,'hpnicfRadiusSchAccSecUdpPort':hpnicfRadiusSchAccSecUdpPort,'hpnicfRadiusSchAccSecKey':hpnicfRadiusSchAccSecKey,'hpnicfRadiusSchAccRowStatus':hpnicfRadiusSchAccRowStatus,'hpnicfRadiusExtendTraps':hpnicfRadiusExtendTraps,'hpnicfRadiusStatistic':hpnicfRadiusStatistic,'hpnicfRadiusStatAccReq':hpnicfRadiusStatAccReq,'hpnicfRadiusStatAccAck':hpnicfRadiusStatAccAck,'hpnicfRadiusStatLogoutReq':hpnicfRadiusStatLogoutReq,'hpnicfRadiusStatLogoutAck':hpnicfRadiusStatLogoutAck,'hpnicfRadiusServerTrapVarObjects':hpnicfRadiusServerTrapVarObjects,_L:hpnicfRadiusServerFirstTrapTime})