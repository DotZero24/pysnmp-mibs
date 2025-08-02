_Ae='fsIPSec2TrapGroup'
_Ad='fsIPSec2TrapObjectGroup'
_Ac='fsIPSec2GlobalStatsGroup'
_Ab='fsIPSec2TrafficTableGroup'
_Aa='fsIPSec2SaGroup'
_AZ='fsIPSec2TunnelStatGroup'
_AY='fsIPSec2TunnelTableGroup'
_AX='fsIPSec2TunnelStop'
_AW='fsIPSec2TunnelStart'
_AV='fsIPSec2SpiValue'
_AU='fsIPSec2SeqNum'
_AT='fsIPSec2MapName'
_AS='fsIPSec2GlobalOutDrops'
_AR='fsIPSec2GlobalOutSpeed'
_AQ='fsIPSec2GlobalOutPkts'
_AP='fsIPSec2GlobalOutOctets'
_AO='fsIPSec2GlobalInDrops'
_AN='fsIPSec2GlobalInSpeed'
_AM='fsIPSec2GlobalInPkts'
_AL='fsIPSec2GlobalInOctets'
_AK='fsIPSec2GlobalActiveSas'
_AJ='fsIPSec2GlobalActiveTunnels'
_AI='fsIPSec2TrafficRemoteHostname'
_AH='fsIPSec2TrafficRemoteProtocol'
_AG='fsIPSec2TrafficRemoteType'
_AF='fsIPSec2TrafficLocalHostname'
_AE='fsIPSec2SaStatus'
_AD='fsIPSec2SaAuthAlgo'
_AC='fsIPSec2SaEncryptAlgo'
_AB='fsIPSec2SaProtocol'
_AA='fsIPSec2SaValue'
_A9='fsIPSec2SaDirection'
_A8='fsIPSec2TunStatus'
_A7='fsIPSec2TunSeqNum'
_A6='fsIPSec2TunMapName'
_A5='fsIPSec2TunOutSaEspAuthAlgo'
_A4='fsIPSec2TunOutSaAhAuthAlgo'
_A3='fsIPSec2TunOutSaEncryptAlgo'
_A2='fsIPSec2TunDiffHellmanGrp'
_A1='fsIPSec2TunInSaEspAuthAlgo'
_A0='fsIPSec2TunInSaAhAuthAlgo'
_z='fsIPSec2TunInSaEncryptAlgo'
_y='fsIPSec2TunCurrentSaInstances'
_x='fsIPSec2TunTotalRefreshes'
_w='fsIPSec2TunRemainSize'
_v='fsIPSec2TunCreateTime'
_u='fsIPSec2TunActiveTime'
_t='fsIPSec2TunRemainTime'
_s='fsIPSec2TunLifeTime'
_r='fsIPSec2TunLifeSize'
_q='fsIPSec2TunInitiator'
_p='fsIPSec2TunEncapMode'
_o='fsIPSec2TunKeyType'
_n='fsIPSec2TunRemoteHostname'
_m='fsIPSec2TunLocalHostname'
_l='fsIPSec2TunLocalAddr'
_k='fsIPSec2TunnelTrafficIndex'
_j='fsIPSec2TunIndex'
_i='expiring'
_h='active'
_g='establishing'
_f='invalidAlg'
_e='invalidMode'
_d='invalidType'
_c='manual'
_b='Unsigned32'
_a='fsIPSec2TunOutDropPkts'
_Z='fsIPSec2TunOutSpeed'
_Y='fsIPSec2TunOutPkts'
_X='fsIPSec2TunOutUncompOctets'
_W='fsIPSec2TunOutOctets'
_V='fsIPSec2TunInDropPkts'
_U='fsIPSec2TunInSpeed'
_T='fsIPSec2TunInPkts'
_S='fsIPSec2TunInDecompOctets'
_R='fsIPSec2TunInOctets'
_Q='accessible-for-notify'
_P='fsIPSec2SaIndex'
_O='none'
_N='fsIPSec2TrafficRemotePort'
_M='fsIPSec2TrafficRemoteAddr2'
_L='fsIPSec2TrafficRemoteAddr1'
_K='fsIPSec2TrafficLocalPort'
_J='fsIPSec2TrafficLocalAddr2'
_I='fsIPSec2TrafficLocalAddr1'
_H='fsIPSec2TrafficLocalProtocol'
_G='fsIPSec2TrafficLocalType'
_F='fsIPSec2TunRemoteAddr'
_E='fsIPSec2TunIfIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='FS-IPSEC2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_b,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
fsIPSec2MibModule=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,108))
class FSIPSecNegoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ike',1),(_c,2),(_d,2147483647)))
class FSEncapMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('tunnel',1),('transport',2),(_e,2147483647)))
class FSEncryptAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,12,128,2147483647)));namedValues=NamedValues(*((_O,0),('desCbc',2),('threedesCbc',3),('aesCbc',12),('sm1Cbc',128),(_f,2147483647)))
class FSAuthAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,2147483647)));namedValues=NamedValues(*((_O,0),('md5',2),('sha',3),(_f,2147483647)))
class FSDiffHellmanGrp(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('modp768',1),('modp1024',2),(_e,2147483647)))
class FSIPSecTunnelState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3)))
class FSSaProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('reserved',0),('isakmp',1),('ah',2),('esp',3)))
class FSTrafficType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ipv4Addr',1),('ipv4AddrSubnet',2),('ipv6Addr',3),('ipv6AddrSubnet',4),('ipv4AddrRange',5),('ipv6AddrRange',6)))
class FSIPSec2NegoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ike',1),(_c,2),(_d,2147483647)))
class FSIPSec2TunnelState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3)))
_FsIPSec2Objects_ObjectIdentity=ObjectIdentity
fsIPSec2Objects=_FsIPSec2Objects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,1))
_FsIPSec2TunnelTable_Object=MibTable
fsIPSec2TunnelTable=_FsIPSec2TunnelTable_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1))
if mibBuilder.loadTexts:fsIPSec2TunnelTable.setStatus(_B)
_FsIPSec2TunnelEntry_Object=MibTableRow
fsIPSec2TunnelEntry=_FsIPSec2TunnelEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1))
fsIPSec2TunnelEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:fsIPSec2TunnelEntry.setStatus(_B)
class _FsIPSec2TunIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunIfIndex_Type.__name__=_D
_FsIPSec2TunIfIndex_Object=MibTableColumn
fsIPSec2TunIfIndex=_FsIPSec2TunIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,1),_FsIPSec2TunIfIndex_Type())
fsIPSec2TunIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunIfIndex.setStatus(_B)
_FsIPSec2TunnelTrafficIndex_Type=Integer32
_FsIPSec2TunnelTrafficIndex_Object=MibTableColumn
fsIPSec2TunnelTrafficIndex=_FsIPSec2TunnelTrafficIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,2),_FsIPSec2TunnelTrafficIndex_Type())
fsIPSec2TunnelTrafficIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunnelTrafficIndex.setStatus(_B)
class _FsIPSec2TunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunIndex_Type.__name__=_D
_FsIPSec2TunIndex_Object=MibTableColumn
fsIPSec2TunIndex=_FsIPSec2TunIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,3),_FsIPSec2TunIndex_Type())
fsIPSec2TunIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunIndex.setStatus(_B)
class _FsIPSec2TunIKETunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunIKETunnelIndex_Type.__name__=_D
_FsIPSec2TunIKETunnelIndex_Object=MibTableColumn
fsIPSec2TunIKETunnelIndex=_FsIPSec2TunIKETunnelIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,5),_FsIPSec2TunIKETunnelIndex_Type())
fsIPSec2TunIKETunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunIKETunnelIndex.setStatus(_B)
_FsIPSec2TunnelAhOutSaIndex_Type=Integer32
_FsIPSec2TunnelAhOutSaIndex_Object=MibTableColumn
fsIPSec2TunnelAhOutSaIndex=_FsIPSec2TunnelAhOutSaIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,6),_FsIPSec2TunnelAhOutSaIndex_Type())
fsIPSec2TunnelAhOutSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunnelAhOutSaIndex.setStatus(_B)
class _FsIPSec2TunnelAhInSaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunnelAhInSaIndex_Type.__name__=_D
_FsIPSec2TunnelAhInSaIndex_Object=MibTableColumn
fsIPSec2TunnelAhInSaIndex=_FsIPSec2TunnelAhInSaIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,7),_FsIPSec2TunnelAhInSaIndex_Type())
fsIPSec2TunnelAhInSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunnelAhInSaIndex.setStatus(_B)
class _FsIPSec2TunnelEspOutSaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunnelEspOutSaIndex_Type.__name__=_D
_FsIPSec2TunnelEspOutSaIndex_Object=MibTableColumn
fsIPSec2TunnelEspOutSaIndex=_FsIPSec2TunnelEspOutSaIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,8),_FsIPSec2TunnelEspOutSaIndex_Type())
fsIPSec2TunnelEspOutSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunnelEspOutSaIndex.setStatus(_B)
_FsIPSec2TunnelEspInSaIndex_Type=Integer32
_FsIPSec2TunnelEspInSaIndex_Object=MibTableColumn
fsIPSec2TunnelEspInSaIndex=_FsIPSec2TunnelEspInSaIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,9),_FsIPSec2TunnelEspInSaIndex_Type())
fsIPSec2TunnelEspInSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunnelEspInSaIndex.setStatus(_B)
_FsIPSec2TunLocalAddr_Type=IpAddress
_FsIPSec2TunLocalAddr_Object=MibTableColumn
fsIPSec2TunLocalAddr=_FsIPSec2TunLocalAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,10),_FsIPSec2TunLocalAddr_Type())
fsIPSec2TunLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunLocalAddr.setStatus(_B)
_FsIPSec2TunRemoteAddr_Type=IpAddress
_FsIPSec2TunRemoteAddr_Object=MibTableColumn
fsIPSec2TunRemoteAddr=_FsIPSec2TunRemoteAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,11),_FsIPSec2TunRemoteAddr_Type())
fsIPSec2TunRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunRemoteAddr.setStatus(_B)
_FsIPSec2TunLocalHostname_Type=DisplayString
_FsIPSec2TunLocalHostname_Object=MibTableColumn
fsIPSec2TunLocalHostname=_FsIPSec2TunLocalHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,12),_FsIPSec2TunLocalHostname_Type())
fsIPSec2TunLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunLocalHostname.setStatus(_B)
_FsIPSec2TunRemoteHostname_Type=DisplayString
_FsIPSec2TunRemoteHostname_Object=MibTableColumn
fsIPSec2TunRemoteHostname=_FsIPSec2TunRemoteHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,13),_FsIPSec2TunRemoteHostname_Type())
fsIPSec2TunRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunRemoteHostname.setStatus(_B)
_FsIPSec2TunKeyType_Type=FSIPSec2NegoType
_FsIPSec2TunKeyType_Object=MibTableColumn
fsIPSec2TunKeyType=_FsIPSec2TunKeyType_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,14),_FsIPSec2TunKeyType_Type())
fsIPSec2TunKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunKeyType.setStatus(_B)
_FsIPSec2TunEncapMode_Type=FSEncapMode
_FsIPSec2TunEncapMode_Object=MibTableColumn
fsIPSec2TunEncapMode=_FsIPSec2TunEncapMode_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,15),_FsIPSec2TunEncapMode_Type())
fsIPSec2TunEncapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunEncapMode.setStatus(_B)
class _FsIPSec2TunInitiator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('local',1),('remote',2),(_O,2147483647)))
_FsIPSec2TunInitiator_Type.__name__=_D
_FsIPSec2TunInitiator_Object=MibTableColumn
fsIPSec2TunInitiator=_FsIPSec2TunInitiator_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,16),_FsIPSec2TunInitiator_Type())
fsIPSec2TunInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInitiator.setStatus(_B)
class _FsIPSec2TunLifeSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunLifeSize_Type.__name__=_D
_FsIPSec2TunLifeSize_Object=MibTableColumn
fsIPSec2TunLifeSize=_FsIPSec2TunLifeSize_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,17),_FsIPSec2TunLifeSize_Type())
fsIPSec2TunLifeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunLifeSize.setStatus(_B)
class _FsIPSec2TunLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunLifeTime_Type.__name__=_D
_FsIPSec2TunLifeTime_Object=MibTableColumn
fsIPSec2TunLifeTime=_FsIPSec2TunLifeTime_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,18),_FsIPSec2TunLifeTime_Type())
fsIPSec2TunLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunLifeTime.setStatus(_B)
class _FsIPSec2TunRemainTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSec2TunRemainTime_Type.__name__=_D
_FsIPSec2TunRemainTime_Object=MibTableColumn
fsIPSec2TunRemainTime=_FsIPSec2TunRemainTime_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,19),_FsIPSec2TunRemainTime_Type())
fsIPSec2TunRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunRemainTime.setStatus(_B)
class _FsIPSec2TunActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSec2TunActiveTime_Type.__name__=_D
_FsIPSec2TunActiveTime_Object=MibTableColumn
fsIPSec2TunActiveTime=_FsIPSec2TunActiveTime_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,20),_FsIPSec2TunActiveTime_Type())
fsIPSec2TunActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunActiveTime.setStatus(_B)
_FsIPSec2TunCreateTime_Type=TimeStamp
_FsIPSec2TunCreateTime_Object=MibTableColumn
fsIPSec2TunCreateTime=_FsIPSec2TunCreateTime_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,21),_FsIPSec2TunCreateTime_Type())
fsIPSec2TunCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunCreateTime.setStatus(_B)
class _FsIPSec2TunRemainSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSec2TunRemainSize_Type.__name__=_D
_FsIPSec2TunRemainSize_Object=MibTableColumn
fsIPSec2TunRemainSize=_FsIPSec2TunRemainSize_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,23),_FsIPSec2TunRemainSize_Type())
fsIPSec2TunRemainSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunRemainSize.setStatus(_B)
_FsIPSec2TunTotalRefreshes_Type=Counter32
_FsIPSec2TunTotalRefreshes_Object=MibTableColumn
fsIPSec2TunTotalRefreshes=_FsIPSec2TunTotalRefreshes_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,24),_FsIPSec2TunTotalRefreshes_Type())
fsIPSec2TunTotalRefreshes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunTotalRefreshes.setStatus(_B)
_FsIPSec2TunCurrentSaInstances_Type=Gauge32
_FsIPSec2TunCurrentSaInstances_Object=MibTableColumn
fsIPSec2TunCurrentSaInstances=_FsIPSec2TunCurrentSaInstances_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,25),_FsIPSec2TunCurrentSaInstances_Type())
fsIPSec2TunCurrentSaInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunCurrentSaInstances.setStatus(_B)
_FsIPSec2TunInSaEncryptAlgo_Type=FSEncryptAlgo
_FsIPSec2TunInSaEncryptAlgo_Object=MibTableColumn
fsIPSec2TunInSaEncryptAlgo=_FsIPSec2TunInSaEncryptAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,26),_FsIPSec2TunInSaEncryptAlgo_Type())
fsIPSec2TunInSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInSaEncryptAlgo.setStatus(_B)
_FsIPSec2TunInSaAhAuthAlgo_Type=FSAuthAlgo
_FsIPSec2TunInSaAhAuthAlgo_Object=MibTableColumn
fsIPSec2TunInSaAhAuthAlgo=_FsIPSec2TunInSaAhAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,27),_FsIPSec2TunInSaAhAuthAlgo_Type())
fsIPSec2TunInSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInSaAhAuthAlgo.setStatus(_B)
_FsIPSec2TunInSaEspAuthAlgo_Type=FSAuthAlgo
_FsIPSec2TunInSaEspAuthAlgo_Object=MibTableColumn
fsIPSec2TunInSaEspAuthAlgo=_FsIPSec2TunInSaEspAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,28),_FsIPSec2TunInSaEspAuthAlgo_Type())
fsIPSec2TunInSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInSaEspAuthAlgo.setStatus(_B)
_FsIPSec2TunDiffHellmanGrp_Type=FSDiffHellmanGrp
_FsIPSec2TunDiffHellmanGrp_Object=MibTableColumn
fsIPSec2TunDiffHellmanGrp=_FsIPSec2TunDiffHellmanGrp_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,29),_FsIPSec2TunDiffHellmanGrp_Type())
fsIPSec2TunDiffHellmanGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunDiffHellmanGrp.setStatus(_B)
_FsIPSec2TunOutSaEncryptAlgo_Type=FSEncryptAlgo
_FsIPSec2TunOutSaEncryptAlgo_Object=MibTableColumn
fsIPSec2TunOutSaEncryptAlgo=_FsIPSec2TunOutSaEncryptAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,30),_FsIPSec2TunOutSaEncryptAlgo_Type())
fsIPSec2TunOutSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutSaEncryptAlgo.setStatus(_B)
_FsIPSec2TunOutSaAhAuthAlgo_Type=FSAuthAlgo
_FsIPSec2TunOutSaAhAuthAlgo_Object=MibTableColumn
fsIPSec2TunOutSaAhAuthAlgo=_FsIPSec2TunOutSaAhAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,31),_FsIPSec2TunOutSaAhAuthAlgo_Type())
fsIPSec2TunOutSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutSaAhAuthAlgo.setStatus(_B)
_FsIPSec2TunOutSaEspAuthAlgo_Type=FSAuthAlgo
_FsIPSec2TunOutSaEspAuthAlgo_Object=MibTableColumn
fsIPSec2TunOutSaEspAuthAlgo=_FsIPSec2TunOutSaEspAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,32),_FsIPSec2TunOutSaEspAuthAlgo_Type())
fsIPSec2TunOutSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutSaEspAuthAlgo.setStatus(_B)
_FsIPSec2TunMapName_Type=DisplayString
_FsIPSec2TunMapName_Object=MibTableColumn
fsIPSec2TunMapName=_FsIPSec2TunMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,33),_FsIPSec2TunMapName_Type())
fsIPSec2TunMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunMapName.setStatus(_B)
class _FsIPSec2TunSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2TunSeqNum_Type.__name__=_D
_FsIPSec2TunSeqNum_Object=MibTableColumn
fsIPSec2TunSeqNum=_FsIPSec2TunSeqNum_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,34),_FsIPSec2TunSeqNum_Type())
fsIPSec2TunSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunSeqNum.setStatus(_B)
_FsIPSec2TunStatus_Type=FSIPSec2TunnelState
_FsIPSec2TunStatus_Object=MibTableColumn
fsIPSec2TunStatus=_FsIPSec2TunStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,1,1,35),_FsIPSec2TunStatus_Type())
fsIPSec2TunStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsIPSec2TunStatus.setStatus(_B)
_FsIPSec2TunnelStatTable_Object=MibTable
fsIPSec2TunnelStatTable=_FsIPSec2TunnelStatTable_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2))
if mibBuilder.loadTexts:fsIPSec2TunnelStatTable.setStatus(_B)
_FsIPSec2TunnelStatEntry_Object=MibTableRow
fsIPSec2TunnelStatEntry=_FsIPSec2TunnelStatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1))
fsIPSec2TunnelStatEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:fsIPSec2TunnelStatEntry.setStatus(_B)
_FsIPSec2TunInOctets_Type=Counter64
_FsIPSec2TunInOctets_Object=MibTableColumn
fsIPSec2TunInOctets=_FsIPSec2TunInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,1),_FsIPSec2TunInOctets_Type())
fsIPSec2TunInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInOctets.setStatus(_B)
_FsIPSec2TunInDecompOctets_Type=Counter64
_FsIPSec2TunInDecompOctets_Object=MibTableColumn
fsIPSec2TunInDecompOctets=_FsIPSec2TunInDecompOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,2),_FsIPSec2TunInDecompOctets_Type())
fsIPSec2TunInDecompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInDecompOctets.setStatus(_B)
_FsIPSec2TunInPkts_Type=Counter64
_FsIPSec2TunInPkts_Object=MibTableColumn
fsIPSec2TunInPkts=_FsIPSec2TunInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,3),_FsIPSec2TunInPkts_Type())
fsIPSec2TunInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInPkts.setStatus(_B)
_FsIPSec2TunInSpeed_Type=Counter64
_FsIPSec2TunInSpeed_Object=MibTableColumn
fsIPSec2TunInSpeed=_FsIPSec2TunInSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,4),_FsIPSec2TunInSpeed_Type())
fsIPSec2TunInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInSpeed.setStatus(_B)
_FsIPSec2TunInDropPkts_Type=Counter64
_FsIPSec2TunInDropPkts_Object=MibTableColumn
fsIPSec2TunInDropPkts=_FsIPSec2TunInDropPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,5),_FsIPSec2TunInDropPkts_Type())
fsIPSec2TunInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunInDropPkts.setStatus(_B)
_FsIPSec2TunOutOctets_Type=Counter64
_FsIPSec2TunOutOctets_Object=MibTableColumn
fsIPSec2TunOutOctets=_FsIPSec2TunOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,6),_FsIPSec2TunOutOctets_Type())
fsIPSec2TunOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutOctets.setStatus(_B)
_FsIPSec2TunOutUncompOctets_Type=Counter64
_FsIPSec2TunOutUncompOctets_Object=MibTableColumn
fsIPSec2TunOutUncompOctets=_FsIPSec2TunOutUncompOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,7),_FsIPSec2TunOutUncompOctets_Type())
fsIPSec2TunOutUncompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutUncompOctets.setStatus(_B)
_FsIPSec2TunOutPkts_Type=Counter64
_FsIPSec2TunOutPkts_Object=MibTableColumn
fsIPSec2TunOutPkts=_FsIPSec2TunOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,8),_FsIPSec2TunOutPkts_Type())
fsIPSec2TunOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutPkts.setStatus(_B)
_FsIPSec2TunOutSpeed_Type=Counter64
_FsIPSec2TunOutSpeed_Object=MibTableColumn
fsIPSec2TunOutSpeed=_FsIPSec2TunOutSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,9),_FsIPSec2TunOutSpeed_Type())
fsIPSec2TunOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutSpeed.setStatus(_B)
_FsIPSec2TunOutDropPkts_Type=Counter64
_FsIPSec2TunOutDropPkts_Object=MibTableColumn
fsIPSec2TunOutDropPkts=_FsIPSec2TunOutDropPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,2,1,10),_FsIPSec2TunOutDropPkts_Type())
fsIPSec2TunOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TunOutDropPkts.setStatus(_B)
_FsIPSec2SaTable_Object=MibTable
fsIPSec2SaTable=_FsIPSec2SaTable_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3))
if mibBuilder.loadTexts:fsIPSec2SaTable.setStatus(_B)
_FsIPSec2SaEntry_Object=MibTableRow
fsIPSec2SaEntry=_FsIPSec2SaEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1))
fsIPSec2SaEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:fsIPSec2SaEntry.setStatus(_B)
class _FsIPSec2SaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSec2SaIndex_Type.__name__=_D
_FsIPSec2SaIndex_Object=MibTableColumn
fsIPSec2SaIndex=_FsIPSec2SaIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,1),_FsIPSec2SaIndex_Type())
fsIPSec2SaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaIndex.setStatus(_B)
class _FsIPSec2SaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_FsIPSec2SaDirection_Type.__name__=_D
_FsIPSec2SaDirection_Object=MibTableColumn
fsIPSec2SaDirection=_FsIPSec2SaDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,2),_FsIPSec2SaDirection_Type())
fsIPSec2SaDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaDirection.setStatus(_B)
class _FsIPSec2SaValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsIPSec2SaValue_Type.__name__=_b
_FsIPSec2SaValue_Object=MibTableColumn
fsIPSec2SaValue=_FsIPSec2SaValue_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,3),_FsIPSec2SaValue_Type())
fsIPSec2SaValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaValue.setStatus(_B)
_FsIPSec2SaProtocol_Type=FSSaProtocol
_FsIPSec2SaProtocol_Object=MibTableColumn
fsIPSec2SaProtocol=_FsIPSec2SaProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,4),_FsIPSec2SaProtocol_Type())
fsIPSec2SaProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaProtocol.setStatus(_B)
_FsIPSec2SaEncryptAlgo_Type=FSEncryptAlgo
_FsIPSec2SaEncryptAlgo_Object=MibTableColumn
fsIPSec2SaEncryptAlgo=_FsIPSec2SaEncryptAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,5),_FsIPSec2SaEncryptAlgo_Type())
fsIPSec2SaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaEncryptAlgo.setStatus(_B)
_FsIPSec2SaAuthAlgo_Type=FSAuthAlgo
_FsIPSec2SaAuthAlgo_Object=MibTableColumn
fsIPSec2SaAuthAlgo=_FsIPSec2SaAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,6),_FsIPSec2SaAuthAlgo_Type())
fsIPSec2SaAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaAuthAlgo.setStatus(_B)
_FsIPSec2SaStatus_Type=FSIPSec2TunnelState
_FsIPSec2SaStatus_Object=MibTableColumn
fsIPSec2SaStatus=_FsIPSec2SaStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,3,1,7),_FsIPSec2SaStatus_Type())
fsIPSec2SaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2SaStatus.setStatus(_B)
_FsIPSec2TrafficTable_Object=MibTable
fsIPSec2TrafficTable=_FsIPSec2TrafficTable_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4))
if mibBuilder.loadTexts:fsIPSec2TrafficTable.setStatus(_B)
_FsIPSec2TrafficEntry_Object=MibTableRow
fsIPSec2TrafficEntry=_FsIPSec2TrafficEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1))
fsIPSec2TrafficEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:fsIPSec2TrafficEntry.setStatus(_B)
_FsIPSec2TrafficIndex_Type=Integer32
_FsIPSec2TrafficIndex_Object=MibTableColumn
fsIPSec2TrafficIndex=_FsIPSec2TrafficIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,1),_FsIPSec2TrafficIndex_Type())
fsIPSec2TrafficIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficIndex.setStatus(_B)
_FsIPSec2TrafficLocalType_Type=FSTrafficType
_FsIPSec2TrafficLocalType_Object=MibTableColumn
fsIPSec2TrafficLocalType=_FsIPSec2TrafficLocalType_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,2),_FsIPSec2TrafficLocalType_Type())
fsIPSec2TrafficLocalType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficLocalType.setStatus(_B)
_FsIPSec2TrafficLocalAddr1_Type=IpAddress
_FsIPSec2TrafficLocalAddr1_Object=MibTableColumn
fsIPSec2TrafficLocalAddr1=_FsIPSec2TrafficLocalAddr1_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,3),_FsIPSec2TrafficLocalAddr1_Type())
fsIPSec2TrafficLocalAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficLocalAddr1.setStatus(_B)
_FsIPSec2TrafficLocalAddr2_Type=IpAddress
_FsIPSec2TrafficLocalAddr2_Object=MibTableColumn
fsIPSec2TrafficLocalAddr2=_FsIPSec2TrafficLocalAddr2_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,4),_FsIPSec2TrafficLocalAddr2_Type())
fsIPSec2TrafficLocalAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficLocalAddr2.setStatus(_B)
class _FsIPSec2TrafficLocalProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsIPSec2TrafficLocalProtocol_Type.__name__=_D
_FsIPSec2TrafficLocalProtocol_Object=MibTableColumn
fsIPSec2TrafficLocalProtocol=_FsIPSec2TrafficLocalProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,5),_FsIPSec2TrafficLocalProtocol_Type())
fsIPSec2TrafficLocalProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficLocalProtocol.setStatus(_B)
class _FsIPSec2TrafficLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIPSec2TrafficLocalPort_Type.__name__=_D
_FsIPSec2TrafficLocalPort_Object=MibTableColumn
fsIPSec2TrafficLocalPort=_FsIPSec2TrafficLocalPort_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,6),_FsIPSec2TrafficLocalPort_Type())
fsIPSec2TrafficLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficLocalPort.setStatus(_B)
_FsIPSec2TrafficLocalHostname_Type=DisplayString
_FsIPSec2TrafficLocalHostname_Object=MibTableColumn
fsIPSec2TrafficLocalHostname=_FsIPSec2TrafficLocalHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,7),_FsIPSec2TrafficLocalHostname_Type())
fsIPSec2TrafficLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficLocalHostname.setStatus(_B)
_FsIPSec2TrafficRemoteType_Type=FSTrafficType
_FsIPSec2TrafficRemoteType_Object=MibTableColumn
fsIPSec2TrafficRemoteType=_FsIPSec2TrafficRemoteType_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,8),_FsIPSec2TrafficRemoteType_Type())
fsIPSec2TrafficRemoteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficRemoteType.setStatus(_B)
_FsIPSec2TrafficRemoteAddr1_Type=IpAddress
_FsIPSec2TrafficRemoteAddr1_Object=MibTableColumn
fsIPSec2TrafficRemoteAddr1=_FsIPSec2TrafficRemoteAddr1_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,9),_FsIPSec2TrafficRemoteAddr1_Type())
fsIPSec2TrafficRemoteAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficRemoteAddr1.setStatus(_B)
_FsIPSec2TrafficRemoteAddr2_Type=IpAddress
_FsIPSec2TrafficRemoteAddr2_Object=MibTableColumn
fsIPSec2TrafficRemoteAddr2=_FsIPSec2TrafficRemoteAddr2_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,10),_FsIPSec2TrafficRemoteAddr2_Type())
fsIPSec2TrafficRemoteAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficRemoteAddr2.setStatus(_B)
class _FsIPSec2TrafficRemoteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsIPSec2TrafficRemoteProtocol_Type.__name__=_D
_FsIPSec2TrafficRemoteProtocol_Object=MibTableColumn
fsIPSec2TrafficRemoteProtocol=_FsIPSec2TrafficRemoteProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,11),_FsIPSec2TrafficRemoteProtocol_Type())
fsIPSec2TrafficRemoteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficRemoteProtocol.setStatus(_B)
class _FsIPSec2TrafficRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIPSec2TrafficRemotePort_Type.__name__=_D
_FsIPSec2TrafficRemotePort_Object=MibTableColumn
fsIPSec2TrafficRemotePort=_FsIPSec2TrafficRemotePort_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,12),_FsIPSec2TrafficRemotePort_Type())
fsIPSec2TrafficRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficRemotePort.setStatus(_B)
_FsIPSec2TrafficRemoteHostname_Type=DisplayString
_FsIPSec2TrafficRemoteHostname_Object=MibTableColumn
fsIPSec2TrafficRemoteHostname=_FsIPSec2TrafficRemoteHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,4,1,13),_FsIPSec2TrafficRemoteHostname_Type())
fsIPSec2TrafficRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2TrafficRemoteHostname.setStatus(_B)
_FsIPSec2GlobalStats_ObjectIdentity=ObjectIdentity
fsIPSec2GlobalStats=_FsIPSec2GlobalStats_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,1,5))
_FsIPSec2GlobalActiveTunnels_Type=Gauge32
_FsIPSec2GlobalActiveTunnels_Object=MibScalar
fsIPSec2GlobalActiveTunnels=_FsIPSec2GlobalActiveTunnels_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,1),_FsIPSec2GlobalActiveTunnels_Type())
fsIPSec2GlobalActiveTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalActiveTunnels.setStatus(_B)
_FsIPSec2GlobalActiveSas_Type=Gauge32
_FsIPSec2GlobalActiveSas_Object=MibScalar
fsIPSec2GlobalActiveSas=_FsIPSec2GlobalActiveSas_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,2),_FsIPSec2GlobalActiveSas_Type())
fsIPSec2GlobalActiveSas.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalActiveSas.setStatus(_B)
_FsIPSec2GlobalInOctets_Type=Counter64
_FsIPSec2GlobalInOctets_Object=MibScalar
fsIPSec2GlobalInOctets=_FsIPSec2GlobalInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,3),_FsIPSec2GlobalInOctets_Type())
fsIPSec2GlobalInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalInOctets.setStatus(_B)
_FsIPSec2GlobalInPkts_Type=Counter64
_FsIPSec2GlobalInPkts_Object=MibScalar
fsIPSec2GlobalInPkts=_FsIPSec2GlobalInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,4),_FsIPSec2GlobalInPkts_Type())
fsIPSec2GlobalInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalInPkts.setStatus(_B)
_FsIPSec2GlobalInSpeed_Type=Counter64
_FsIPSec2GlobalInSpeed_Object=MibScalar
fsIPSec2GlobalInSpeed=_FsIPSec2GlobalInSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,5),_FsIPSec2GlobalInSpeed_Type())
fsIPSec2GlobalInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalInSpeed.setStatus(_B)
_FsIPSec2GlobalInDrops_Type=Counter64
_FsIPSec2GlobalInDrops_Object=MibScalar
fsIPSec2GlobalInDrops=_FsIPSec2GlobalInDrops_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,6),_FsIPSec2GlobalInDrops_Type())
fsIPSec2GlobalInDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalInDrops.setStatus(_B)
_FsIPSec2GlobalOutOctets_Type=Counter64
_FsIPSec2GlobalOutOctets_Object=MibScalar
fsIPSec2GlobalOutOctets=_FsIPSec2GlobalOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,7),_FsIPSec2GlobalOutOctets_Type())
fsIPSec2GlobalOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalOutOctets.setStatus(_B)
_FsIPSec2GlobalOutPkts_Type=Counter64
_FsIPSec2GlobalOutPkts_Object=MibScalar
fsIPSec2GlobalOutPkts=_FsIPSec2GlobalOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,8),_FsIPSec2GlobalOutPkts_Type())
fsIPSec2GlobalOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalOutPkts.setStatus(_B)
_FsIPSec2GlobalOutSpeed_Type=Counter64
_FsIPSec2GlobalOutSpeed_Object=MibScalar
fsIPSec2GlobalOutSpeed=_FsIPSec2GlobalOutSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,9),_FsIPSec2GlobalOutSpeed_Type())
fsIPSec2GlobalOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalOutSpeed.setStatus(_B)
_FsIPSec2GlobalOutDrops_Type=Counter64
_FsIPSec2GlobalOutDrops_Object=MibScalar
fsIPSec2GlobalOutDrops=_FsIPSec2GlobalOutDrops_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,5,10),_FsIPSec2GlobalOutDrops_Type())
fsIPSec2GlobalOutDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSec2GlobalOutDrops.setStatus(_B)
_FsIPSec2TrapObject_ObjectIdentity=ObjectIdentity
fsIPSec2TrapObject=_FsIPSec2TrapObject_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,1,6))
_FsIPSec2MapName_Type=DisplayString
_FsIPSec2MapName_Object=MibScalar
fsIPSec2MapName=_FsIPSec2MapName_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,6,1),_FsIPSec2MapName_Type())
fsIPSec2MapName.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsIPSec2MapName.setStatus(_B)
_FsIPSec2SeqNum_Type=Integer32
_FsIPSec2SeqNum_Object=MibScalar
fsIPSec2SeqNum=_FsIPSec2SeqNum_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,6,2),_FsIPSec2SeqNum_Type())
fsIPSec2SeqNum.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsIPSec2SeqNum.setStatus(_B)
_FsIPSec2SpiValue_Type=Integer32
_FsIPSec2SpiValue_Object=MibScalar
fsIPSec2SpiValue=_FsIPSec2SpiValue_Object((1,3,6,1,4,1,52642,1,1,10,2,108,1,6,3),_FsIPSec2SpiValue_Type())
fsIPSec2SpiValue.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsIPSec2SpiValue.setStatus(_B)
_FsIPSec2Trap_ObjectIdentity=ObjectIdentity
fsIPSec2Trap=_FsIPSec2Trap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,1,7))
_FsIPSec2Notifications_ObjectIdentity=ObjectIdentity
fsIPSec2Notifications=_FsIPSec2Notifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,1,7,1))
_FsIPSec2Conformance_ObjectIdentity=ObjectIdentity
fsIPSec2Conformance=_FsIPSec2Conformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,2))
_FsIPSec2Compliances_ObjectIdentity=ObjectIdentity
fsIPSec2Compliances=_FsIPSec2Compliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,2,1))
_FsIPSec2Groups_ObjectIdentity=ObjectIdentity
fsIPSec2Groups=_FsIPSec2Groups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,108,2,2))
fsIPSec2TunnelTableGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,1))
fsIPSec2TunnelTableGroup.setObjects(*((_A,_E),(_A,_l),(_A,_F),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:fsIPSec2TunnelTableGroup.setStatus(_B)
fsIPSec2TunnelStatGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,2))
fsIPSec2TunnelStatGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:fsIPSec2TunnelStatGroup.setStatus(_B)
fsIPSec2SaGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,3))
fsIPSec2SaGroup.setObjects(*((_A,_P),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:fsIPSec2SaGroup.setStatus(_B)
fsIPSec2TrafficTableGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,4))
fsIPSec2TrafficTableGroup.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:fsIPSec2TrafficTableGroup.setStatus(_B)
fsIPSec2GlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,5))
fsIPSec2GlobalStatsGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:fsIPSec2GlobalStatsGroup.setStatus(_B)
fsIPSec2TrapObjectGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,6))
fsIPSec2TrapObjectGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:fsIPSec2TrapObjectGroup.setStatus(_B)
fsIPSec2TunnelStart=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,108,1,7,1,1))
fsIPSec2TunnelStart.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:fsIPSec2TunnelStart.setStatus(_B)
fsIPSec2TunnelStop=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,108,1,7,1,2))
fsIPSec2TunnelStop.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:fsIPSec2TunnelStop.setStatus(_B)
fsIPSec2TrapGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,108,2,2,7))
fsIPSec2TrapGroup.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:fsIPSec2TrapGroup.setStatus(_B)
fsIPSec2Compliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,108,2,1,1))
fsIPSec2Compliance.setObjects(*((_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:fsIPSec2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FSIPSecNegoType':FSIPSecNegoType,'FSEncapMode':FSEncapMode,'FSEncryptAlgo':FSEncryptAlgo,'FSAuthAlgo':FSAuthAlgo,'FSDiffHellmanGrp':FSDiffHellmanGrp,'FSIPSecTunnelState':FSIPSecTunnelState,'FSSaProtocol':FSSaProtocol,'FSTrafficType':FSTrafficType,'FSIPSec2NegoType':FSIPSec2NegoType,'FSIPSec2TunnelState':FSIPSec2TunnelState,'fsIPSec2MibModule':fsIPSec2MibModule,'fsIPSec2Objects':fsIPSec2Objects,'fsIPSec2TunnelTable':fsIPSec2TunnelTable,'fsIPSec2TunnelEntry':fsIPSec2TunnelEntry,_E:fsIPSec2TunIfIndex,_k:fsIPSec2TunnelTrafficIndex,_j:fsIPSec2TunIndex,'fsIPSec2TunIKETunnelIndex':fsIPSec2TunIKETunnelIndex,'fsIPSec2TunnelAhOutSaIndex':fsIPSec2TunnelAhOutSaIndex,'fsIPSec2TunnelAhInSaIndex':fsIPSec2TunnelAhInSaIndex,'fsIPSec2TunnelEspOutSaIndex':fsIPSec2TunnelEspOutSaIndex,'fsIPSec2TunnelEspInSaIndex':fsIPSec2TunnelEspInSaIndex,_l:fsIPSec2TunLocalAddr,_F:fsIPSec2TunRemoteAddr,_m:fsIPSec2TunLocalHostname,_n:fsIPSec2TunRemoteHostname,_o:fsIPSec2TunKeyType,_p:fsIPSec2TunEncapMode,_q:fsIPSec2TunInitiator,_r:fsIPSec2TunLifeSize,_s:fsIPSec2TunLifeTime,_t:fsIPSec2TunRemainTime,_u:fsIPSec2TunActiveTime,_v:fsIPSec2TunCreateTime,_w:fsIPSec2TunRemainSize,_x:fsIPSec2TunTotalRefreshes,_y:fsIPSec2TunCurrentSaInstances,_z:fsIPSec2TunInSaEncryptAlgo,_A0:fsIPSec2TunInSaAhAuthAlgo,_A1:fsIPSec2TunInSaEspAuthAlgo,_A2:fsIPSec2TunDiffHellmanGrp,_A3:fsIPSec2TunOutSaEncryptAlgo,_A4:fsIPSec2TunOutSaAhAuthAlgo,_A5:fsIPSec2TunOutSaEspAuthAlgo,_A6:fsIPSec2TunMapName,_A7:fsIPSec2TunSeqNum,_A8:fsIPSec2TunStatus,'fsIPSec2TunnelStatTable':fsIPSec2TunnelStatTable,'fsIPSec2TunnelStatEntry':fsIPSec2TunnelStatEntry,_R:fsIPSec2TunInOctets,_S:fsIPSec2TunInDecompOctets,_T:fsIPSec2TunInPkts,_U:fsIPSec2TunInSpeed,_V:fsIPSec2TunInDropPkts,_W:fsIPSec2TunOutOctets,_X:fsIPSec2TunOutUncompOctets,_Y:fsIPSec2TunOutPkts,_Z:fsIPSec2TunOutSpeed,_a:fsIPSec2TunOutDropPkts,'fsIPSec2SaTable':fsIPSec2SaTable,'fsIPSec2SaEntry':fsIPSec2SaEntry,_P:fsIPSec2SaIndex,_A9:fsIPSec2SaDirection,_AA:fsIPSec2SaValue,_AB:fsIPSec2SaProtocol,_AC:fsIPSec2SaEncryptAlgo,_AD:fsIPSec2SaAuthAlgo,_AE:fsIPSec2SaStatus,'fsIPSec2TrafficTable':fsIPSec2TrafficTable,'fsIPSec2TrafficEntry':fsIPSec2TrafficEntry,'fsIPSec2TrafficIndex':fsIPSec2TrafficIndex,_G:fsIPSec2TrafficLocalType,_I:fsIPSec2TrafficLocalAddr1,_J:fsIPSec2TrafficLocalAddr2,_H:fsIPSec2TrafficLocalProtocol,_K:fsIPSec2TrafficLocalPort,_AF:fsIPSec2TrafficLocalHostname,_AG:fsIPSec2TrafficRemoteType,_L:fsIPSec2TrafficRemoteAddr1,_M:fsIPSec2TrafficRemoteAddr2,_AH:fsIPSec2TrafficRemoteProtocol,_N:fsIPSec2TrafficRemotePort,_AI:fsIPSec2TrafficRemoteHostname,'fsIPSec2GlobalStats':fsIPSec2GlobalStats,_AJ:fsIPSec2GlobalActiveTunnels,_AK:fsIPSec2GlobalActiveSas,_AL:fsIPSec2GlobalInOctets,_AM:fsIPSec2GlobalInPkts,_AN:fsIPSec2GlobalInSpeed,_AO:fsIPSec2GlobalInDrops,_AP:fsIPSec2GlobalOutOctets,_AQ:fsIPSec2GlobalOutPkts,_AR:fsIPSec2GlobalOutSpeed,_AS:fsIPSec2GlobalOutDrops,'fsIPSec2TrapObject':fsIPSec2TrapObject,_AT:fsIPSec2MapName,_AU:fsIPSec2SeqNum,_AV:fsIPSec2SpiValue,'fsIPSec2Trap':fsIPSec2Trap,'fsIPSec2Notifications':fsIPSec2Notifications,_AW:fsIPSec2TunnelStart,_AX:fsIPSec2TunnelStop,'fsIPSec2Conformance':fsIPSec2Conformance,'fsIPSec2Compliances':fsIPSec2Compliances,'fsIPSec2Compliance':fsIPSec2Compliance,'fsIPSec2Groups':fsIPSec2Groups,_AY:fsIPSec2TunnelTableGroup,_AZ:fsIPSec2TunnelStatGroup,_Aa:fsIPSec2SaGroup,_Ab:fsIPSec2TrafficTableGroup,_Ac:fsIPSec2GlobalStatsGroup,_Ad:fsIPSec2TrapObjectGroup,_Ae:fsIPSec2TrapGroup})