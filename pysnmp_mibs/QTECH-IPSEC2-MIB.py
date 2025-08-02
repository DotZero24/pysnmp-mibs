_Ae='qtechIPSec2TrapGroup'
_Ad='qtechIPSec2TrapObjectGroup'
_Ac='qtechIPSec2GlobalStatsGroup'
_Ab='qtechIPSec2TrafficTableGroup'
_Aa='qtechIPSec2SaGroup'
_AZ='qtechIPSec2TunnelStatGroup'
_AY='qtechIPSec2TunnelTableGroup'
_AX='qtechIPSec2TunnelStop'
_AW='qtechIPSec2TunnelStart'
_AV='qtechIPSec2SpiValue'
_AU='qtechIPSec2SeqNum'
_AT='qtechIPSec2MapName'
_AS='qtechIPSec2GlobalOutDrops'
_AR='qtechIPSec2GlobalOutSpeed'
_AQ='qtechIPSec2GlobalOutPkts'
_AP='qtechIPSec2GlobalOutOctets'
_AO='qtechIPSec2GlobalInDrops'
_AN='qtechIPSec2GlobalInSpeed'
_AM='qtechIPSec2GlobalInPkts'
_AL='qtechIPSec2GlobalInOctets'
_AK='qtechIPSec2GlobalActiveSas'
_AJ='qtechIPSec2GlobalActiveTunnels'
_AI='qtechIPSec2TrafficRemoteHostname'
_AH='qtechIPSec2TrafficRemoteProtocol'
_AG='qtechIPSec2TrafficRemoteType'
_AF='qtechIPSec2TrafficLocalHostname'
_AE='qtechIPSec2SaStatus'
_AD='qtechIPSec2SaAuthAlgo'
_AC='qtechIPSec2SaEncryptAlgo'
_AB='qtechIPSec2SaProtocol'
_AA='qtechIPSec2SaValue'
_A9='qtechIPSec2SaDirection'
_A8='qtechIPSec2TunStatus'
_A7='qtechIPSec2TunSeqNum'
_A6='qtechIPSec2TunMapName'
_A5='qtechIPSec2TunOutSaEspAuthAlgo'
_A4='qtechIPSec2TunOutSaAhAuthAlgo'
_A3='qtechIPSec2TunOutSaEncryptAlgo'
_A2='qtechIPSec2TunDiffHellmanGrp'
_A1='qtechIPSec2TunInSaEspAuthAlgo'
_A0='qtechIPSec2TunInSaAhAuthAlgo'
_z='qtechIPSec2TunInSaEncryptAlgo'
_y='qtechIPSec2TunCurrentSaInstances'
_x='qtechIPSec2TunTotalRefreshes'
_w='qtechIPSec2TunRemainSize'
_v='qtechIPSec2TunCreateTime'
_u='qtechIPSec2TunActiveTime'
_t='qtechIPSec2TunRemainTime'
_s='qtechIPSec2TunLifeTime'
_r='qtechIPSec2TunLifeSize'
_q='qtechIPSec2TunInitiator'
_p='qtechIPSec2TunEncapMode'
_o='qtechIPSec2TunKeyType'
_n='qtechIPSec2TunRemoteHostname'
_m='qtechIPSec2TunLocalHostname'
_l='qtechIPSec2TunLocalAddr'
_k='qtechIPSec2TunnelTrafficIndex'
_j='qtechIPSec2TunIndex'
_i='expiring'
_h='active'
_g='establishing'
_f='invalidAlg'
_e='invalidMode'
_d='invalidType'
_c='manual'
_b='Unsigned32'
_a='qtechIPSec2TunOutDropPkts'
_Z='qtechIPSec2TunOutSpeed'
_Y='qtechIPSec2TunOutPkts'
_X='qtechIPSec2TunOutUncompOctets'
_W='qtechIPSec2TunOutOctets'
_V='qtechIPSec2TunInDropPkts'
_U='qtechIPSec2TunInSpeed'
_T='qtechIPSec2TunInPkts'
_S='qtechIPSec2TunInDecompOctets'
_R='qtechIPSec2TunInOctets'
_Q='accessible-for-notify'
_P='qtechIPSec2SaIndex'
_O='none'
_N='qtechIPSec2TrafficRemotePort'
_M='qtechIPSec2TrafficRemoteAddr2'
_L='qtechIPSec2TrafficRemoteAddr1'
_K='qtechIPSec2TrafficLocalPort'
_J='qtechIPSec2TrafficLocalAddr2'
_I='qtechIPSec2TrafficLocalAddr1'
_H='qtechIPSec2TrafficLocalProtocol'
_G='qtechIPSec2TrafficLocalType'
_F='qtechIPSec2TunRemoteAddr'
_E='qtechIPSec2TunIfIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='QTECH-IPSEC2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_b,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
qtechIPSec2MibModule=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,108))
class QtechIPSecNegoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ike',1),(_c,2),(_d,2147483647)))
class QtechEncapMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('tunnel',1),('transport',2),(_e,2147483647)))
class QtechEncryptAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,12,128,2147483647)));namedValues=NamedValues(*((_O,0),('desCbc',2),('threedesCbc',3),('aesCbc',12),('sm1Cbc',128),(_f,2147483647)))
class QtechAuthAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,2147483647)));namedValues=NamedValues(*((_O,0),('md5',2),('sha',3),(_f,2147483647)))
class QtechDiffHellmanGrp(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('modp768',1),('modp1024',2),(_e,2147483647)))
class QtechIPSecTunnelState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3)))
class QtechSaProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('reserved',0),('isakmp',1),('ah',2),('esp',3)))
class QtechTrafficType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ipv4Addr',1),('ipv4AddrSubnet',2),('ipv6Addr',3),('ipv6AddrSubnet',4),('ipv4AddrRange',5),('ipv6AddrRange',6)))
class QtechIPSec2NegoType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ike',1),(_c,2),(_d,2147483647)))
class QtechIPSec2TunnelState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3)))
_QtechIPSec2Objects_ObjectIdentity=ObjectIdentity
qtechIPSec2Objects=_QtechIPSec2Objects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,1))
_QtechIPSec2TunnelTable_Object=MibTable
qtechIPSec2TunnelTable=_QtechIPSec2TunnelTable_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1))
if mibBuilder.loadTexts:qtechIPSec2TunnelTable.setStatus(_B)
_QtechIPSec2TunnelEntry_Object=MibTableRow
qtechIPSec2TunnelEntry=_QtechIPSec2TunnelEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1))
qtechIPSec2TunnelEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:qtechIPSec2TunnelEntry.setStatus(_B)
class _QtechIPSec2TunIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunIfIndex_Type.__name__=_D
_QtechIPSec2TunIfIndex_Object=MibTableColumn
qtechIPSec2TunIfIndex=_QtechIPSec2TunIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,1),_QtechIPSec2TunIfIndex_Type())
qtechIPSec2TunIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunIfIndex.setStatus(_B)
_QtechIPSec2TunnelTrafficIndex_Type=Integer32
_QtechIPSec2TunnelTrafficIndex_Object=MibTableColumn
qtechIPSec2TunnelTrafficIndex=_QtechIPSec2TunnelTrafficIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,2),_QtechIPSec2TunnelTrafficIndex_Type())
qtechIPSec2TunnelTrafficIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunnelTrafficIndex.setStatus(_B)
class _QtechIPSec2TunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunIndex_Type.__name__=_D
_QtechIPSec2TunIndex_Object=MibTableColumn
qtechIPSec2TunIndex=_QtechIPSec2TunIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,3),_QtechIPSec2TunIndex_Type())
qtechIPSec2TunIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunIndex.setStatus(_B)
class _QtechIPSec2TunIKETunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunIKETunnelIndex_Type.__name__=_D
_QtechIPSec2TunIKETunnelIndex_Object=MibTableColumn
qtechIPSec2TunIKETunnelIndex=_QtechIPSec2TunIKETunnelIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,5),_QtechIPSec2TunIKETunnelIndex_Type())
qtechIPSec2TunIKETunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunIKETunnelIndex.setStatus(_B)
_QtechIPSec2TunnelAhOutSaIndex_Type=Integer32
_QtechIPSec2TunnelAhOutSaIndex_Object=MibTableColumn
qtechIPSec2TunnelAhOutSaIndex=_QtechIPSec2TunnelAhOutSaIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,6),_QtechIPSec2TunnelAhOutSaIndex_Type())
qtechIPSec2TunnelAhOutSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunnelAhOutSaIndex.setStatus(_B)
class _QtechIPSec2TunnelAhInSaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunnelAhInSaIndex_Type.__name__=_D
_QtechIPSec2TunnelAhInSaIndex_Object=MibTableColumn
qtechIPSec2TunnelAhInSaIndex=_QtechIPSec2TunnelAhInSaIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,7),_QtechIPSec2TunnelAhInSaIndex_Type())
qtechIPSec2TunnelAhInSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunnelAhInSaIndex.setStatus(_B)
class _QtechIPSec2TunnelEspOutSaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunnelEspOutSaIndex_Type.__name__=_D
_QtechIPSec2TunnelEspOutSaIndex_Object=MibTableColumn
qtechIPSec2TunnelEspOutSaIndex=_QtechIPSec2TunnelEspOutSaIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,8),_QtechIPSec2TunnelEspOutSaIndex_Type())
qtechIPSec2TunnelEspOutSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunnelEspOutSaIndex.setStatus(_B)
_QtechIPSec2TunnelEspInSaIndex_Type=Integer32
_QtechIPSec2TunnelEspInSaIndex_Object=MibTableColumn
qtechIPSec2TunnelEspInSaIndex=_QtechIPSec2TunnelEspInSaIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,9),_QtechIPSec2TunnelEspInSaIndex_Type())
qtechIPSec2TunnelEspInSaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunnelEspInSaIndex.setStatus(_B)
_QtechIPSec2TunLocalAddr_Type=IpAddress
_QtechIPSec2TunLocalAddr_Object=MibTableColumn
qtechIPSec2TunLocalAddr=_QtechIPSec2TunLocalAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,10),_QtechIPSec2TunLocalAddr_Type())
qtechIPSec2TunLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunLocalAddr.setStatus(_B)
_QtechIPSec2TunRemoteAddr_Type=IpAddress
_QtechIPSec2TunRemoteAddr_Object=MibTableColumn
qtechIPSec2TunRemoteAddr=_QtechIPSec2TunRemoteAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,11),_QtechIPSec2TunRemoteAddr_Type())
qtechIPSec2TunRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunRemoteAddr.setStatus(_B)
_QtechIPSec2TunLocalHostname_Type=DisplayString
_QtechIPSec2TunLocalHostname_Object=MibTableColumn
qtechIPSec2TunLocalHostname=_QtechIPSec2TunLocalHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,12),_QtechIPSec2TunLocalHostname_Type())
qtechIPSec2TunLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunLocalHostname.setStatus(_B)
_QtechIPSec2TunRemoteHostname_Type=DisplayString
_QtechIPSec2TunRemoteHostname_Object=MibTableColumn
qtechIPSec2TunRemoteHostname=_QtechIPSec2TunRemoteHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,13),_QtechIPSec2TunRemoteHostname_Type())
qtechIPSec2TunRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunRemoteHostname.setStatus(_B)
_QtechIPSec2TunKeyType_Type=QtechIPSec2NegoType
_QtechIPSec2TunKeyType_Object=MibTableColumn
qtechIPSec2TunKeyType=_QtechIPSec2TunKeyType_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,14),_QtechIPSec2TunKeyType_Type())
qtechIPSec2TunKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunKeyType.setStatus(_B)
_QtechIPSec2TunEncapMode_Type=QtechEncapMode
_QtechIPSec2TunEncapMode_Object=MibTableColumn
qtechIPSec2TunEncapMode=_QtechIPSec2TunEncapMode_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,15),_QtechIPSec2TunEncapMode_Type())
qtechIPSec2TunEncapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunEncapMode.setStatus(_B)
class _QtechIPSec2TunInitiator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('local',1),('remote',2),(_O,2147483647)))
_QtechIPSec2TunInitiator_Type.__name__=_D
_QtechIPSec2TunInitiator_Object=MibTableColumn
qtechIPSec2TunInitiator=_QtechIPSec2TunInitiator_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,16),_QtechIPSec2TunInitiator_Type())
qtechIPSec2TunInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInitiator.setStatus(_B)
class _QtechIPSec2TunLifeSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunLifeSize_Type.__name__=_D
_QtechIPSec2TunLifeSize_Object=MibTableColumn
qtechIPSec2TunLifeSize=_QtechIPSec2TunLifeSize_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,17),_QtechIPSec2TunLifeSize_Type())
qtechIPSec2TunLifeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunLifeSize.setStatus(_B)
class _QtechIPSec2TunLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunLifeTime_Type.__name__=_D
_QtechIPSec2TunLifeTime_Object=MibTableColumn
qtechIPSec2TunLifeTime=_QtechIPSec2TunLifeTime_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,18),_QtechIPSec2TunLifeTime_Type())
qtechIPSec2TunLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunLifeTime.setStatus(_B)
class _QtechIPSec2TunRemainTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSec2TunRemainTime_Type.__name__=_D
_QtechIPSec2TunRemainTime_Object=MibTableColumn
qtechIPSec2TunRemainTime=_QtechIPSec2TunRemainTime_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,19),_QtechIPSec2TunRemainTime_Type())
qtechIPSec2TunRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunRemainTime.setStatus(_B)
class _QtechIPSec2TunActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSec2TunActiveTime_Type.__name__=_D
_QtechIPSec2TunActiveTime_Object=MibTableColumn
qtechIPSec2TunActiveTime=_QtechIPSec2TunActiveTime_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,20),_QtechIPSec2TunActiveTime_Type())
qtechIPSec2TunActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunActiveTime.setStatus(_B)
_QtechIPSec2TunCreateTime_Type=TimeStamp
_QtechIPSec2TunCreateTime_Object=MibTableColumn
qtechIPSec2TunCreateTime=_QtechIPSec2TunCreateTime_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,21),_QtechIPSec2TunCreateTime_Type())
qtechIPSec2TunCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunCreateTime.setStatus(_B)
class _QtechIPSec2TunRemainSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSec2TunRemainSize_Type.__name__=_D
_QtechIPSec2TunRemainSize_Object=MibTableColumn
qtechIPSec2TunRemainSize=_QtechIPSec2TunRemainSize_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,23),_QtechIPSec2TunRemainSize_Type())
qtechIPSec2TunRemainSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunRemainSize.setStatus(_B)
_QtechIPSec2TunTotalRefreshes_Type=Counter32
_QtechIPSec2TunTotalRefreshes_Object=MibTableColumn
qtechIPSec2TunTotalRefreshes=_QtechIPSec2TunTotalRefreshes_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,24),_QtechIPSec2TunTotalRefreshes_Type())
qtechIPSec2TunTotalRefreshes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunTotalRefreshes.setStatus(_B)
_QtechIPSec2TunCurrentSaInstances_Type=Gauge32
_QtechIPSec2TunCurrentSaInstances_Object=MibTableColumn
qtechIPSec2TunCurrentSaInstances=_QtechIPSec2TunCurrentSaInstances_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,25),_QtechIPSec2TunCurrentSaInstances_Type())
qtechIPSec2TunCurrentSaInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunCurrentSaInstances.setStatus(_B)
_QtechIPSec2TunInSaEncryptAlgo_Type=QtechEncryptAlgo
_QtechIPSec2TunInSaEncryptAlgo_Object=MibTableColumn
qtechIPSec2TunInSaEncryptAlgo=_QtechIPSec2TunInSaEncryptAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,26),_QtechIPSec2TunInSaEncryptAlgo_Type())
qtechIPSec2TunInSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInSaEncryptAlgo.setStatus(_B)
_QtechIPSec2TunInSaAhAuthAlgo_Type=QtechAuthAlgo
_QtechIPSec2TunInSaAhAuthAlgo_Object=MibTableColumn
qtechIPSec2TunInSaAhAuthAlgo=_QtechIPSec2TunInSaAhAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,27),_QtechIPSec2TunInSaAhAuthAlgo_Type())
qtechIPSec2TunInSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInSaAhAuthAlgo.setStatus(_B)
_QtechIPSec2TunInSaEspAuthAlgo_Type=QtechAuthAlgo
_QtechIPSec2TunInSaEspAuthAlgo_Object=MibTableColumn
qtechIPSec2TunInSaEspAuthAlgo=_QtechIPSec2TunInSaEspAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,28),_QtechIPSec2TunInSaEspAuthAlgo_Type())
qtechIPSec2TunInSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInSaEspAuthAlgo.setStatus(_B)
_QtechIPSec2TunDiffHellmanGrp_Type=QtechDiffHellmanGrp
_QtechIPSec2TunDiffHellmanGrp_Object=MibTableColumn
qtechIPSec2TunDiffHellmanGrp=_QtechIPSec2TunDiffHellmanGrp_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,29),_QtechIPSec2TunDiffHellmanGrp_Type())
qtechIPSec2TunDiffHellmanGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunDiffHellmanGrp.setStatus(_B)
_QtechIPSec2TunOutSaEncryptAlgo_Type=QtechEncryptAlgo
_QtechIPSec2TunOutSaEncryptAlgo_Object=MibTableColumn
qtechIPSec2TunOutSaEncryptAlgo=_QtechIPSec2TunOutSaEncryptAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,30),_QtechIPSec2TunOutSaEncryptAlgo_Type())
qtechIPSec2TunOutSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutSaEncryptAlgo.setStatus(_B)
_QtechIPSec2TunOutSaAhAuthAlgo_Type=QtechAuthAlgo
_QtechIPSec2TunOutSaAhAuthAlgo_Object=MibTableColumn
qtechIPSec2TunOutSaAhAuthAlgo=_QtechIPSec2TunOutSaAhAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,31),_QtechIPSec2TunOutSaAhAuthAlgo_Type())
qtechIPSec2TunOutSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutSaAhAuthAlgo.setStatus(_B)
_QtechIPSec2TunOutSaEspAuthAlgo_Type=QtechAuthAlgo
_QtechIPSec2TunOutSaEspAuthAlgo_Object=MibTableColumn
qtechIPSec2TunOutSaEspAuthAlgo=_QtechIPSec2TunOutSaEspAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,32),_QtechIPSec2TunOutSaEspAuthAlgo_Type())
qtechIPSec2TunOutSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutSaEspAuthAlgo.setStatus(_B)
_QtechIPSec2TunMapName_Type=DisplayString
_QtechIPSec2TunMapName_Object=MibTableColumn
qtechIPSec2TunMapName=_QtechIPSec2TunMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,33),_QtechIPSec2TunMapName_Type())
qtechIPSec2TunMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunMapName.setStatus(_B)
class _QtechIPSec2TunSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2TunSeqNum_Type.__name__=_D
_QtechIPSec2TunSeqNum_Object=MibTableColumn
qtechIPSec2TunSeqNum=_QtechIPSec2TunSeqNum_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,34),_QtechIPSec2TunSeqNum_Type())
qtechIPSec2TunSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunSeqNum.setStatus(_B)
_QtechIPSec2TunStatus_Type=QtechIPSec2TunnelState
_QtechIPSec2TunStatus_Object=MibTableColumn
qtechIPSec2TunStatus=_QtechIPSec2TunStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,1,1,35),_QtechIPSec2TunStatus_Type())
qtechIPSec2TunStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechIPSec2TunStatus.setStatus(_B)
_QtechIPSec2TunnelStatTable_Object=MibTable
qtechIPSec2TunnelStatTable=_QtechIPSec2TunnelStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2))
if mibBuilder.loadTexts:qtechIPSec2TunnelStatTable.setStatus(_B)
_QtechIPSec2TunnelStatEntry_Object=MibTableRow
qtechIPSec2TunnelStatEntry=_QtechIPSec2TunnelStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1))
qtechIPSec2TunnelStatEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:qtechIPSec2TunnelStatEntry.setStatus(_B)
_QtechIPSec2TunInOctets_Type=Counter64
_QtechIPSec2TunInOctets_Object=MibTableColumn
qtechIPSec2TunInOctets=_QtechIPSec2TunInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,1),_QtechIPSec2TunInOctets_Type())
qtechIPSec2TunInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInOctets.setStatus(_B)
_QtechIPSec2TunInDecompOctets_Type=Counter64
_QtechIPSec2TunInDecompOctets_Object=MibTableColumn
qtechIPSec2TunInDecompOctets=_QtechIPSec2TunInDecompOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,2),_QtechIPSec2TunInDecompOctets_Type())
qtechIPSec2TunInDecompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInDecompOctets.setStatus(_B)
_QtechIPSec2TunInPkts_Type=Counter64
_QtechIPSec2TunInPkts_Object=MibTableColumn
qtechIPSec2TunInPkts=_QtechIPSec2TunInPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,3),_QtechIPSec2TunInPkts_Type())
qtechIPSec2TunInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInPkts.setStatus(_B)
_QtechIPSec2TunInSpeed_Type=Counter64
_QtechIPSec2TunInSpeed_Object=MibTableColumn
qtechIPSec2TunInSpeed=_QtechIPSec2TunInSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,4),_QtechIPSec2TunInSpeed_Type())
qtechIPSec2TunInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInSpeed.setStatus(_B)
_QtechIPSec2TunInDropPkts_Type=Counter64
_QtechIPSec2TunInDropPkts_Object=MibTableColumn
qtechIPSec2TunInDropPkts=_QtechIPSec2TunInDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,5),_QtechIPSec2TunInDropPkts_Type())
qtechIPSec2TunInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunInDropPkts.setStatus(_B)
_QtechIPSec2TunOutOctets_Type=Counter64
_QtechIPSec2TunOutOctets_Object=MibTableColumn
qtechIPSec2TunOutOctets=_QtechIPSec2TunOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,6),_QtechIPSec2TunOutOctets_Type())
qtechIPSec2TunOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutOctets.setStatus(_B)
_QtechIPSec2TunOutUncompOctets_Type=Counter64
_QtechIPSec2TunOutUncompOctets_Object=MibTableColumn
qtechIPSec2TunOutUncompOctets=_QtechIPSec2TunOutUncompOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,7),_QtechIPSec2TunOutUncompOctets_Type())
qtechIPSec2TunOutUncompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutUncompOctets.setStatus(_B)
_QtechIPSec2TunOutPkts_Type=Counter64
_QtechIPSec2TunOutPkts_Object=MibTableColumn
qtechIPSec2TunOutPkts=_QtechIPSec2TunOutPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,8),_QtechIPSec2TunOutPkts_Type())
qtechIPSec2TunOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutPkts.setStatus(_B)
_QtechIPSec2TunOutSpeed_Type=Counter64
_QtechIPSec2TunOutSpeed_Object=MibTableColumn
qtechIPSec2TunOutSpeed=_QtechIPSec2TunOutSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,9),_QtechIPSec2TunOutSpeed_Type())
qtechIPSec2TunOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutSpeed.setStatus(_B)
_QtechIPSec2TunOutDropPkts_Type=Counter64
_QtechIPSec2TunOutDropPkts_Object=MibTableColumn
qtechIPSec2TunOutDropPkts=_QtechIPSec2TunOutDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,2,1,10),_QtechIPSec2TunOutDropPkts_Type())
qtechIPSec2TunOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TunOutDropPkts.setStatus(_B)
_QtechIPSec2SaTable_Object=MibTable
qtechIPSec2SaTable=_QtechIPSec2SaTable_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3))
if mibBuilder.loadTexts:qtechIPSec2SaTable.setStatus(_B)
_QtechIPSec2SaEntry_Object=MibTableRow
qtechIPSec2SaEntry=_QtechIPSec2SaEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1))
qtechIPSec2SaEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:qtechIPSec2SaEntry.setStatus(_B)
class _QtechIPSec2SaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSec2SaIndex_Type.__name__=_D
_QtechIPSec2SaIndex_Object=MibTableColumn
qtechIPSec2SaIndex=_QtechIPSec2SaIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,1),_QtechIPSec2SaIndex_Type())
qtechIPSec2SaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaIndex.setStatus(_B)
class _QtechIPSec2SaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_QtechIPSec2SaDirection_Type.__name__=_D
_QtechIPSec2SaDirection_Object=MibTableColumn
qtechIPSec2SaDirection=_QtechIPSec2SaDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,2),_QtechIPSec2SaDirection_Type())
qtechIPSec2SaDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaDirection.setStatus(_B)
class _QtechIPSec2SaValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechIPSec2SaValue_Type.__name__=_b
_QtechIPSec2SaValue_Object=MibTableColumn
qtechIPSec2SaValue=_QtechIPSec2SaValue_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,3),_QtechIPSec2SaValue_Type())
qtechIPSec2SaValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaValue.setStatus(_B)
_QtechIPSec2SaProtocol_Type=QtechSaProtocol
_QtechIPSec2SaProtocol_Object=MibTableColumn
qtechIPSec2SaProtocol=_QtechIPSec2SaProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,4),_QtechIPSec2SaProtocol_Type())
qtechIPSec2SaProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaProtocol.setStatus(_B)
_QtechIPSec2SaEncryptAlgo_Type=QtechEncryptAlgo
_QtechIPSec2SaEncryptAlgo_Object=MibTableColumn
qtechIPSec2SaEncryptAlgo=_QtechIPSec2SaEncryptAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,5),_QtechIPSec2SaEncryptAlgo_Type())
qtechIPSec2SaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaEncryptAlgo.setStatus(_B)
_QtechIPSec2SaAuthAlgo_Type=QtechAuthAlgo
_QtechIPSec2SaAuthAlgo_Object=MibTableColumn
qtechIPSec2SaAuthAlgo=_QtechIPSec2SaAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,6),_QtechIPSec2SaAuthAlgo_Type())
qtechIPSec2SaAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaAuthAlgo.setStatus(_B)
_QtechIPSec2SaStatus_Type=QtechIPSec2TunnelState
_QtechIPSec2SaStatus_Object=MibTableColumn
qtechIPSec2SaStatus=_QtechIPSec2SaStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,3,1,7),_QtechIPSec2SaStatus_Type())
qtechIPSec2SaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2SaStatus.setStatus(_B)
_QtechIPSec2TrafficTable_Object=MibTable
qtechIPSec2TrafficTable=_QtechIPSec2TrafficTable_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4))
if mibBuilder.loadTexts:qtechIPSec2TrafficTable.setStatus(_B)
_QtechIPSec2TrafficEntry_Object=MibTableRow
qtechIPSec2TrafficEntry=_QtechIPSec2TrafficEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1))
qtechIPSec2TrafficEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:qtechIPSec2TrafficEntry.setStatus(_B)
_QtechIPSec2TrafficIndex_Type=Integer32
_QtechIPSec2TrafficIndex_Object=MibTableColumn
qtechIPSec2TrafficIndex=_QtechIPSec2TrafficIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,1),_QtechIPSec2TrafficIndex_Type())
qtechIPSec2TrafficIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficIndex.setStatus(_B)
_QtechIPSec2TrafficLocalType_Type=QtechTrafficType
_QtechIPSec2TrafficLocalType_Object=MibTableColumn
qtechIPSec2TrafficLocalType=_QtechIPSec2TrafficLocalType_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,2),_QtechIPSec2TrafficLocalType_Type())
qtechIPSec2TrafficLocalType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficLocalType.setStatus(_B)
_QtechIPSec2TrafficLocalAddr1_Type=IpAddress
_QtechIPSec2TrafficLocalAddr1_Object=MibTableColumn
qtechIPSec2TrafficLocalAddr1=_QtechIPSec2TrafficLocalAddr1_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,3),_QtechIPSec2TrafficLocalAddr1_Type())
qtechIPSec2TrafficLocalAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficLocalAddr1.setStatus(_B)
_QtechIPSec2TrafficLocalAddr2_Type=IpAddress
_QtechIPSec2TrafficLocalAddr2_Object=MibTableColumn
qtechIPSec2TrafficLocalAddr2=_QtechIPSec2TrafficLocalAddr2_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,4),_QtechIPSec2TrafficLocalAddr2_Type())
qtechIPSec2TrafficLocalAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficLocalAddr2.setStatus(_B)
class _QtechIPSec2TrafficLocalProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechIPSec2TrafficLocalProtocol_Type.__name__=_D
_QtechIPSec2TrafficLocalProtocol_Object=MibTableColumn
qtechIPSec2TrafficLocalProtocol=_QtechIPSec2TrafficLocalProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,5),_QtechIPSec2TrafficLocalProtocol_Type())
qtechIPSec2TrafficLocalProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficLocalProtocol.setStatus(_B)
class _QtechIPSec2TrafficLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechIPSec2TrafficLocalPort_Type.__name__=_D
_QtechIPSec2TrafficLocalPort_Object=MibTableColumn
qtechIPSec2TrafficLocalPort=_QtechIPSec2TrafficLocalPort_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,6),_QtechIPSec2TrafficLocalPort_Type())
qtechIPSec2TrafficLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficLocalPort.setStatus(_B)
_QtechIPSec2TrafficLocalHostname_Type=DisplayString
_QtechIPSec2TrafficLocalHostname_Object=MibTableColumn
qtechIPSec2TrafficLocalHostname=_QtechIPSec2TrafficLocalHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,7),_QtechIPSec2TrafficLocalHostname_Type())
qtechIPSec2TrafficLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficLocalHostname.setStatus(_B)
_QtechIPSec2TrafficRemoteType_Type=QtechTrafficType
_QtechIPSec2TrafficRemoteType_Object=MibTableColumn
qtechIPSec2TrafficRemoteType=_QtechIPSec2TrafficRemoteType_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,8),_QtechIPSec2TrafficRemoteType_Type())
qtechIPSec2TrafficRemoteType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficRemoteType.setStatus(_B)
_QtechIPSec2TrafficRemoteAddr1_Type=IpAddress
_QtechIPSec2TrafficRemoteAddr1_Object=MibTableColumn
qtechIPSec2TrafficRemoteAddr1=_QtechIPSec2TrafficRemoteAddr1_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,9),_QtechIPSec2TrafficRemoteAddr1_Type())
qtechIPSec2TrafficRemoteAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficRemoteAddr1.setStatus(_B)
_QtechIPSec2TrafficRemoteAddr2_Type=IpAddress
_QtechIPSec2TrafficRemoteAddr2_Object=MibTableColumn
qtechIPSec2TrafficRemoteAddr2=_QtechIPSec2TrafficRemoteAddr2_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,10),_QtechIPSec2TrafficRemoteAddr2_Type())
qtechIPSec2TrafficRemoteAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficRemoteAddr2.setStatus(_B)
class _QtechIPSec2TrafficRemoteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechIPSec2TrafficRemoteProtocol_Type.__name__=_D
_QtechIPSec2TrafficRemoteProtocol_Object=MibTableColumn
qtechIPSec2TrafficRemoteProtocol=_QtechIPSec2TrafficRemoteProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,11),_QtechIPSec2TrafficRemoteProtocol_Type())
qtechIPSec2TrafficRemoteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficRemoteProtocol.setStatus(_B)
class _QtechIPSec2TrafficRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechIPSec2TrafficRemotePort_Type.__name__=_D
_QtechIPSec2TrafficRemotePort_Object=MibTableColumn
qtechIPSec2TrafficRemotePort=_QtechIPSec2TrafficRemotePort_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,12),_QtechIPSec2TrafficRemotePort_Type())
qtechIPSec2TrafficRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficRemotePort.setStatus(_B)
_QtechIPSec2TrafficRemoteHostname_Type=DisplayString
_QtechIPSec2TrafficRemoteHostname_Object=MibTableColumn
qtechIPSec2TrafficRemoteHostname=_QtechIPSec2TrafficRemoteHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,4,1,13),_QtechIPSec2TrafficRemoteHostname_Type())
qtechIPSec2TrafficRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2TrafficRemoteHostname.setStatus(_B)
_QtechIPSec2GlobalStats_ObjectIdentity=ObjectIdentity
qtechIPSec2GlobalStats=_QtechIPSec2GlobalStats_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,1,5))
_QtechIPSec2GlobalActiveTunnels_Type=Gauge32
_QtechIPSec2GlobalActiveTunnels_Object=MibScalar
qtechIPSec2GlobalActiveTunnels=_QtechIPSec2GlobalActiveTunnels_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,1),_QtechIPSec2GlobalActiveTunnels_Type())
qtechIPSec2GlobalActiveTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalActiveTunnels.setStatus(_B)
_QtechIPSec2GlobalActiveSas_Type=Gauge32
_QtechIPSec2GlobalActiveSas_Object=MibScalar
qtechIPSec2GlobalActiveSas=_QtechIPSec2GlobalActiveSas_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,2),_QtechIPSec2GlobalActiveSas_Type())
qtechIPSec2GlobalActiveSas.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalActiveSas.setStatus(_B)
_QtechIPSec2GlobalInOctets_Type=Counter64
_QtechIPSec2GlobalInOctets_Object=MibScalar
qtechIPSec2GlobalInOctets=_QtechIPSec2GlobalInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,3),_QtechIPSec2GlobalInOctets_Type())
qtechIPSec2GlobalInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalInOctets.setStatus(_B)
_QtechIPSec2GlobalInPkts_Type=Counter64
_QtechIPSec2GlobalInPkts_Object=MibScalar
qtechIPSec2GlobalInPkts=_QtechIPSec2GlobalInPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,4),_QtechIPSec2GlobalInPkts_Type())
qtechIPSec2GlobalInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalInPkts.setStatus(_B)
_QtechIPSec2GlobalInSpeed_Type=Counter64
_QtechIPSec2GlobalInSpeed_Object=MibScalar
qtechIPSec2GlobalInSpeed=_QtechIPSec2GlobalInSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,5),_QtechIPSec2GlobalInSpeed_Type())
qtechIPSec2GlobalInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalInSpeed.setStatus(_B)
_QtechIPSec2GlobalInDrops_Type=Counter64
_QtechIPSec2GlobalInDrops_Object=MibScalar
qtechIPSec2GlobalInDrops=_QtechIPSec2GlobalInDrops_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,6),_QtechIPSec2GlobalInDrops_Type())
qtechIPSec2GlobalInDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalInDrops.setStatus(_B)
_QtechIPSec2GlobalOutOctets_Type=Counter64
_QtechIPSec2GlobalOutOctets_Object=MibScalar
qtechIPSec2GlobalOutOctets=_QtechIPSec2GlobalOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,7),_QtechIPSec2GlobalOutOctets_Type())
qtechIPSec2GlobalOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalOutOctets.setStatus(_B)
_QtechIPSec2GlobalOutPkts_Type=Counter64
_QtechIPSec2GlobalOutPkts_Object=MibScalar
qtechIPSec2GlobalOutPkts=_QtechIPSec2GlobalOutPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,8),_QtechIPSec2GlobalOutPkts_Type())
qtechIPSec2GlobalOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalOutPkts.setStatus(_B)
_QtechIPSec2GlobalOutSpeed_Type=Counter64
_QtechIPSec2GlobalOutSpeed_Object=MibScalar
qtechIPSec2GlobalOutSpeed=_QtechIPSec2GlobalOutSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,9),_QtechIPSec2GlobalOutSpeed_Type())
qtechIPSec2GlobalOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalOutSpeed.setStatus(_B)
_QtechIPSec2GlobalOutDrops_Type=Counter64
_QtechIPSec2GlobalOutDrops_Object=MibScalar
qtechIPSec2GlobalOutDrops=_QtechIPSec2GlobalOutDrops_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,5,10),_QtechIPSec2GlobalOutDrops_Type())
qtechIPSec2GlobalOutDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSec2GlobalOutDrops.setStatus(_B)
_QtechIPSec2TrapObject_ObjectIdentity=ObjectIdentity
qtechIPSec2TrapObject=_QtechIPSec2TrapObject_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,1,6))
_QtechIPSec2MapName_Type=DisplayString
_QtechIPSec2MapName_Object=MibScalar
qtechIPSec2MapName=_QtechIPSec2MapName_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,6,1),_QtechIPSec2MapName_Type())
qtechIPSec2MapName.setMaxAccess(_Q)
if mibBuilder.loadTexts:qtechIPSec2MapName.setStatus(_B)
_QtechIPSec2SeqNum_Type=Integer32
_QtechIPSec2SeqNum_Object=MibScalar
qtechIPSec2SeqNum=_QtechIPSec2SeqNum_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,6,2),_QtechIPSec2SeqNum_Type())
qtechIPSec2SeqNum.setMaxAccess(_Q)
if mibBuilder.loadTexts:qtechIPSec2SeqNum.setStatus(_B)
_QtechIPSec2SpiValue_Type=Integer32
_QtechIPSec2SpiValue_Object=MibScalar
qtechIPSec2SpiValue=_QtechIPSec2SpiValue_Object((1,3,6,1,4,1,27514,1,1,10,2,108,1,6,3),_QtechIPSec2SpiValue_Type())
qtechIPSec2SpiValue.setMaxAccess(_Q)
if mibBuilder.loadTexts:qtechIPSec2SpiValue.setStatus(_B)
_QtechIPSec2Trap_ObjectIdentity=ObjectIdentity
qtechIPSec2Trap=_QtechIPSec2Trap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,1,7))
_QtechIPSec2Notifications_ObjectIdentity=ObjectIdentity
qtechIPSec2Notifications=_QtechIPSec2Notifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,1,7,1))
_QtechIPSec2Conformance_ObjectIdentity=ObjectIdentity
qtechIPSec2Conformance=_QtechIPSec2Conformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,2))
_QtechIPSec2Compliances_ObjectIdentity=ObjectIdentity
qtechIPSec2Compliances=_QtechIPSec2Compliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,2,1))
_QtechIPSec2Groups_ObjectIdentity=ObjectIdentity
qtechIPSec2Groups=_QtechIPSec2Groups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,108,2,2))
qtechIPSec2TunnelTableGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,1))
qtechIPSec2TunnelTableGroup.setObjects(*((_A,_E),(_A,_l),(_A,_F),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:qtechIPSec2TunnelTableGroup.setStatus(_B)
qtechIPSec2TunnelStatGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,2))
qtechIPSec2TunnelStatGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:qtechIPSec2TunnelStatGroup.setStatus(_B)
qtechIPSec2SaGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,3))
qtechIPSec2SaGroup.setObjects(*((_A,_P),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:qtechIPSec2SaGroup.setStatus(_B)
qtechIPSec2TrafficTableGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,4))
qtechIPSec2TrafficTableGroup.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:qtechIPSec2TrafficTableGroup.setStatus(_B)
qtechIPSec2GlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,5))
qtechIPSec2GlobalStatsGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:qtechIPSec2GlobalStatsGroup.setStatus(_B)
qtechIPSec2TrapObjectGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,6))
qtechIPSec2TrapObjectGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:qtechIPSec2TrapObjectGroup.setStatus(_B)
qtechIPSec2TunnelStart=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,108,1,7,1,1))
qtechIPSec2TunnelStart.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:qtechIPSec2TunnelStart.setStatus(_B)
qtechIPSec2TunnelStop=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,108,1,7,1,2))
qtechIPSec2TunnelStop.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:qtechIPSec2TunnelStop.setStatus(_B)
qtechIPSec2TrapGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,108,2,2,7))
qtechIPSec2TrapGroup.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:qtechIPSec2TrapGroup.setStatus(_B)
qtechIPSec2Compliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,108,2,1,1))
qtechIPSec2Compliance.setObjects(*((_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:qtechIPSec2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'QtechIPSecNegoType':QtechIPSecNegoType,'QtechEncapMode':QtechEncapMode,'QtechEncryptAlgo':QtechEncryptAlgo,'QtechAuthAlgo':QtechAuthAlgo,'QtechDiffHellmanGrp':QtechDiffHellmanGrp,'QtechIPSecTunnelState':QtechIPSecTunnelState,'QtechSaProtocol':QtechSaProtocol,'QtechTrafficType':QtechTrafficType,'QtechIPSec2NegoType':QtechIPSec2NegoType,'QtechIPSec2TunnelState':QtechIPSec2TunnelState,'qtechIPSec2MibModule':qtechIPSec2MibModule,'qtechIPSec2Objects':qtechIPSec2Objects,'qtechIPSec2TunnelTable':qtechIPSec2TunnelTable,'qtechIPSec2TunnelEntry':qtechIPSec2TunnelEntry,_E:qtechIPSec2TunIfIndex,_k:qtechIPSec2TunnelTrafficIndex,_j:qtechIPSec2TunIndex,'qtechIPSec2TunIKETunnelIndex':qtechIPSec2TunIKETunnelIndex,'qtechIPSec2TunnelAhOutSaIndex':qtechIPSec2TunnelAhOutSaIndex,'qtechIPSec2TunnelAhInSaIndex':qtechIPSec2TunnelAhInSaIndex,'qtechIPSec2TunnelEspOutSaIndex':qtechIPSec2TunnelEspOutSaIndex,'qtechIPSec2TunnelEspInSaIndex':qtechIPSec2TunnelEspInSaIndex,_l:qtechIPSec2TunLocalAddr,_F:qtechIPSec2TunRemoteAddr,_m:qtechIPSec2TunLocalHostname,_n:qtechIPSec2TunRemoteHostname,_o:qtechIPSec2TunKeyType,_p:qtechIPSec2TunEncapMode,_q:qtechIPSec2TunInitiator,_r:qtechIPSec2TunLifeSize,_s:qtechIPSec2TunLifeTime,_t:qtechIPSec2TunRemainTime,_u:qtechIPSec2TunActiveTime,_v:qtechIPSec2TunCreateTime,_w:qtechIPSec2TunRemainSize,_x:qtechIPSec2TunTotalRefreshes,_y:qtechIPSec2TunCurrentSaInstances,_z:qtechIPSec2TunInSaEncryptAlgo,_A0:qtechIPSec2TunInSaAhAuthAlgo,_A1:qtechIPSec2TunInSaEspAuthAlgo,_A2:qtechIPSec2TunDiffHellmanGrp,_A3:qtechIPSec2TunOutSaEncryptAlgo,_A4:qtechIPSec2TunOutSaAhAuthAlgo,_A5:qtechIPSec2TunOutSaEspAuthAlgo,_A6:qtechIPSec2TunMapName,_A7:qtechIPSec2TunSeqNum,_A8:qtechIPSec2TunStatus,'qtechIPSec2TunnelStatTable':qtechIPSec2TunnelStatTable,'qtechIPSec2TunnelStatEntry':qtechIPSec2TunnelStatEntry,_R:qtechIPSec2TunInOctets,_S:qtechIPSec2TunInDecompOctets,_T:qtechIPSec2TunInPkts,_U:qtechIPSec2TunInSpeed,_V:qtechIPSec2TunInDropPkts,_W:qtechIPSec2TunOutOctets,_X:qtechIPSec2TunOutUncompOctets,_Y:qtechIPSec2TunOutPkts,_Z:qtechIPSec2TunOutSpeed,_a:qtechIPSec2TunOutDropPkts,'qtechIPSec2SaTable':qtechIPSec2SaTable,'qtechIPSec2SaEntry':qtechIPSec2SaEntry,_P:qtechIPSec2SaIndex,_A9:qtechIPSec2SaDirection,_AA:qtechIPSec2SaValue,_AB:qtechIPSec2SaProtocol,_AC:qtechIPSec2SaEncryptAlgo,_AD:qtechIPSec2SaAuthAlgo,_AE:qtechIPSec2SaStatus,'qtechIPSec2TrafficTable':qtechIPSec2TrafficTable,'qtechIPSec2TrafficEntry':qtechIPSec2TrafficEntry,'qtechIPSec2TrafficIndex':qtechIPSec2TrafficIndex,_G:qtechIPSec2TrafficLocalType,_I:qtechIPSec2TrafficLocalAddr1,_J:qtechIPSec2TrafficLocalAddr2,_H:qtechIPSec2TrafficLocalProtocol,_K:qtechIPSec2TrafficLocalPort,_AF:qtechIPSec2TrafficLocalHostname,_AG:qtechIPSec2TrafficRemoteType,_L:qtechIPSec2TrafficRemoteAddr1,_M:qtechIPSec2TrafficRemoteAddr2,_AH:qtechIPSec2TrafficRemoteProtocol,_N:qtechIPSec2TrafficRemotePort,_AI:qtechIPSec2TrafficRemoteHostname,'qtechIPSec2GlobalStats':qtechIPSec2GlobalStats,_AJ:qtechIPSec2GlobalActiveTunnels,_AK:qtechIPSec2GlobalActiveSas,_AL:qtechIPSec2GlobalInOctets,_AM:qtechIPSec2GlobalInPkts,_AN:qtechIPSec2GlobalInSpeed,_AO:qtechIPSec2GlobalInDrops,_AP:qtechIPSec2GlobalOutOctets,_AQ:qtechIPSec2GlobalOutPkts,_AR:qtechIPSec2GlobalOutSpeed,_AS:qtechIPSec2GlobalOutDrops,'qtechIPSec2TrapObject':qtechIPSec2TrapObject,_AT:qtechIPSec2MapName,_AU:qtechIPSec2SeqNum,_AV:qtechIPSec2SpiValue,'qtechIPSec2Trap':qtechIPSec2Trap,'qtechIPSec2Notifications':qtechIPSec2Notifications,_AW:qtechIPSec2TunnelStart,_AX:qtechIPSec2TunnelStop,'qtechIPSec2Conformance':qtechIPSec2Conformance,'qtechIPSec2Compliances':qtechIPSec2Compliances,'qtechIPSec2Compliance':qtechIPSec2Compliance,'qtechIPSec2Groups':qtechIPSec2Groups,_AY:qtechIPSec2TunnelTableGroup,_AZ:qtechIPSec2TunnelStatGroup,_Aa:qtechIPSec2SaGroup,_Ab:qtechIPSec2TrafficTableGroup,_Ac:qtechIPSec2GlobalStatsGroup,_Ad:qtechIPSec2TrapObjectGroup,_Ae:qtechIPSec2TrapGroup})