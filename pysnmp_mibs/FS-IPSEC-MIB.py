_AU='fsIPSecTrapGroup'
_AT='fsIPSecTrapObjectGroup'
_AS='fsIPSecGlobalStatsGroup'
_AR='fsIPSecTrafficTableGroup'
_AQ='fsIPSecSaGroup'
_AP='fsIPSecTunnelStatGroup'
_AO='fsIPSecTunnelTableGroup'
_AN='fsIPSecTunnelStop'
_AM='fsIPSecTunnelStart'
_AL='fsIPSecSpiValue'
_AK='fsIPSecSeqNum'
_AJ='fsIPSecMapName'
_AI='fsIPSecGlobalOutSpeed'
_AH='fsIPSecGlobalOutDrops'
_AG='fsIPSecGlobalOutPkts'
_AF='fsIPSecGlobalOutOctets'
_AE='fsIPSecGlobalInSpeed'
_AD='fsIPSecGlobalInDrops'
_AC='fsIPSecGlobalInPkts'
_AB='fsIPSecGlobalInOctets'
_AA='fsIPSecGlobalActiveSas'
_A9='fsIPSecGlobalActiveTunnels'
_A8='fsIPSecTrafficRemoteHostname'
_A7='fsIPSecTrafficRemotePort'
_A6='fsIPSecTrafficRemoteProtocol'
_A5='fsIPSecTrafficRemoteAddr2'
_A4='fsIPSecTrafficRemoteAddr1'
_A3='fsIPSecTrafficRemoteType'
_A2='fsIPSecTrafficLocalHostname'
_A1='fsIPSecTrafficLocalPort'
_A0='fsIPSecTrafficLocalProtocol'
_z='fsIPSecTrafficLocalAddr2'
_y='fsIPSecTrafficLocalAddr1'
_x='fsIPSecTrafficLocalType'
_w='fsIPSecSaStatus'
_v='fsIPSecSaAuthAlgo'
_u='fsIPSecSaEncryptAlgo'
_t='fsIPSecSaProtocol'
_s='fsIPSecSaValue'
_r='fsIPSecSaDirection'
_q='fsIPSecTunOutDropPkts'
_p='fsIPSecTunOutSpeed'
_o='fsIPSecTunOutPkts'
_n='fsIPSecTunOutUncompOctets'
_m='fsIPSecTunOutOctets'
_l='fsIPSecTunInDropPkts'
_k='fsIPSecTunInSpeed'
_j='fsIPSecTunInPkts'
_i='fsIPSecTunInDecompOctets'
_h='fsIPSecTunInOctets'
_g='fsIPSecTunStatus'
_f='fsIPSecTunOutSaEspAuthAlgo'
_e='fsIPSecTunOutSaAhAuthAlgo'
_d='fsIPSecTunOutSaEncryptAlgo'
_c='fsIPSecTunDiffHellmanGrp'
_b='fsIPSecTunInSaEspAuthAlgo'
_a='fsIPSecTunInSaAhAuthAlgo'
_Z='fsIPSecTunInSaEncryptAlgo'
_Y='fsIPSecTunCurrentSaInstances'
_X='fsIPSecTunTotalRefreshes'
_W='fsIPSecTunRemainSize'
_V='fsIPSecTunRemainTime'
_U='fsIPSecTunInitiator'
_T='fsIPSecTunEncapMode'
_S='fsIPSecTunKeyType'
_R='fsIPSecTunIKETunnelIndex'
_Q='invalidAlg'
_P='invalidMode'
_O='Unsigned32'
_N='fsIPSecTunActiveTime'
_M='fsIPSecTunLifeTime'
_L='fsIPSecTunLifeSize'
_K='accessible-for-notify'
_J='not-accessible'
_I='fsIPSecTunRemoteHostname'
_H='fsIPSecTunLocalHostname'
_G='fsIPSecTunLocalAddr'
_F='none'
_E='fsIPSecTunRemoteAddr'
_D='Integer32'
_C='read-only'
_B='FS-IPSEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
fsIPSecMonitor=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,94))
if mibBuilder.loadTexts:fsIPSecMonitor.setRevisions(('2011-02-17 00:00',))
class FSDiffHellmanGrp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*((_F,0),('modp768',1),('modp1024',2),(_P,2147483647)))
class FSEncapMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('tunnel',1),('transport',2),(_P,2147483647)))
class FSEncryptAlgo(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,12,128,2147483647)));namedValues=NamedValues(*((_F,0),('desCbc',2),('threedesCbc',3),('aesCbc',12),('sm1Cbc',128),(_Q,2147483647)))
class FSAuthAlgo(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*((_F,0),('md5',1),('sha',2),(_Q,2147483647)))
class FSSaProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('reserved',0),('isakmp',1),('ah',2),('esp',3)))
class FSTunnelProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,17,50,51)));namedValues=NamedValues(*((_F,0),('icmp',1),('igmp',2),('ip',4),('tcp',6),('udp',17),('esp',50),('ah',51)))
class FSTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ipv4Addr',1),('ipv4AddrSubnet',2),('ipv6Addr',3),('ipv6AddrSubnet',4),('ipv4AddrRange',5),('ipv6AddrRange',6)))
class FSIPSecNegoType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ike',1),('manual',2),('invalidType',2147483647)))
class FSIPSecTunnelState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('establishing',1),('active',2),('expiring',3)))
_FsIPSecObjects_ObjectIdentity=ObjectIdentity
fsIPSecObjects=_FsIPSecObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,1))
_FsIPSecTunnelTable_Object=MibTable
fsIPSecTunnelTable=_FsIPSecTunnelTable_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1))
if mibBuilder.loadTexts:fsIPSecTunnelTable.setStatus(_A)
_FsIPSecTunnelEntry_Object=MibTableRow
fsIPSecTunnelEntry=_FsIPSecTunnelEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1))
fsIPSecTunnelEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsIPSecTunnelEntry.setStatus(_A)
class _FsIPSecTunIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecTunIfIndex_Type.__name__=_D
_FsIPSecTunIfIndex_Object=MibTableColumn
fsIPSecTunIfIndex=_FsIPSecTunIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,1),_FsIPSecTunIfIndex_Type())
fsIPSecTunIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsIPSecTunIfIndex.setStatus(_A)
class _FsIPSecTunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecTunIndex_Type.__name__=_D
_FsIPSecTunIndex_Object=MibTableColumn
fsIPSecTunIndex=_FsIPSecTunIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,2),_FsIPSecTunIndex_Type())
fsIPSecTunIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsIPSecTunIndex.setStatus(_A)
class _FsIPSecTunIKETunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecTunIKETunnelIndex_Type.__name__=_D
_FsIPSecTunIKETunnelIndex_Object=MibTableColumn
fsIPSecTunIKETunnelIndex=_FsIPSecTunIKETunnelIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,3),_FsIPSecTunIKETunnelIndex_Type())
fsIPSecTunIKETunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunIKETunnelIndex.setStatus(_A)
_FsIPSecTunLocalAddr_Type=IpAddress
_FsIPSecTunLocalAddr_Object=MibTableColumn
fsIPSecTunLocalAddr=_FsIPSecTunLocalAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,4),_FsIPSecTunLocalAddr_Type())
fsIPSecTunLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunLocalAddr.setStatus(_A)
_FsIPSecTunRemoteAddr_Type=IpAddress
_FsIPSecTunRemoteAddr_Object=MibTableColumn
fsIPSecTunRemoteAddr=_FsIPSecTunRemoteAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,5),_FsIPSecTunRemoteAddr_Type())
fsIPSecTunRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunRemoteAddr.setStatus(_A)
_FsIPSecTunLocalHostname_Type=DisplayString
_FsIPSecTunLocalHostname_Object=MibTableColumn
fsIPSecTunLocalHostname=_FsIPSecTunLocalHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,6),_FsIPSecTunLocalHostname_Type())
fsIPSecTunLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunLocalHostname.setStatus(_A)
_FsIPSecTunRemoteHostname_Type=DisplayString
_FsIPSecTunRemoteHostname_Object=MibTableColumn
fsIPSecTunRemoteHostname=_FsIPSecTunRemoteHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,7),_FsIPSecTunRemoteHostname_Type())
fsIPSecTunRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunRemoteHostname.setStatus(_A)
_FsIPSecTunKeyType_Type=FSIPSecNegoType
_FsIPSecTunKeyType_Object=MibTableColumn
fsIPSecTunKeyType=_FsIPSecTunKeyType_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,8),_FsIPSecTunKeyType_Type())
fsIPSecTunKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunKeyType.setStatus(_A)
_FsIPSecTunEncapMode_Type=FSEncapMode
_FsIPSecTunEncapMode_Object=MibTableColumn
fsIPSecTunEncapMode=_FsIPSecTunEncapMode_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,9),_FsIPSecTunEncapMode_Type())
fsIPSecTunEncapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunEncapMode.setStatus(_A)
class _FsIPSecTunInitiator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('local',1),('remote',2),(_F,2147483647)))
_FsIPSecTunInitiator_Type.__name__=_D
_FsIPSecTunInitiator_Object=MibTableColumn
fsIPSecTunInitiator=_FsIPSecTunInitiator_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,10),_FsIPSecTunInitiator_Type())
fsIPSecTunInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInitiator.setStatus(_A)
class _FsIPSecTunLifeSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecTunLifeSize_Type.__name__=_D
_FsIPSecTunLifeSize_Object=MibTableColumn
fsIPSecTunLifeSize=_FsIPSecTunLifeSize_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,11),_FsIPSecTunLifeSize_Type())
fsIPSecTunLifeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunLifeSize.setStatus(_A)
class _FsIPSecTunLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecTunLifeTime_Type.__name__=_D
_FsIPSecTunLifeTime_Object=MibTableColumn
fsIPSecTunLifeTime=_FsIPSecTunLifeTime_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,12),_FsIPSecTunLifeTime_Type())
fsIPSecTunLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunLifeTime.setStatus(_A)
class _FsIPSecTunRemainTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSecTunRemainTime_Type.__name__=_D
_FsIPSecTunRemainTime_Object=MibTableColumn
fsIPSecTunRemainTime=_FsIPSecTunRemainTime_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,13),_FsIPSecTunRemainTime_Type())
fsIPSecTunRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunRemainTime.setStatus(_A)
class _FsIPSecTunActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSecTunActiveTime_Type.__name__=_D
_FsIPSecTunActiveTime_Object=MibTableColumn
fsIPSecTunActiveTime=_FsIPSecTunActiveTime_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,14),_FsIPSecTunActiveTime_Type())
fsIPSecTunActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunActiveTime.setStatus(_A)
class _FsIPSecTunCreateTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSecTunCreateTime_Type.__name__=_D
_FsIPSecTunCreateTime_Object=MibTableColumn
fsIPSecTunCreateTime=_FsIPSecTunCreateTime_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,15),_FsIPSecTunCreateTime_Type())
fsIPSecTunCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunCreateTime.setStatus(_A)
class _FsIPSecTunRemainSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsIPSecTunRemainSize_Type.__name__=_D
_FsIPSecTunRemainSize_Object=MibTableColumn
fsIPSecTunRemainSize=_FsIPSecTunRemainSize_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,16),_FsIPSecTunRemainSize_Type())
fsIPSecTunRemainSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunRemainSize.setStatus(_A)
_FsIPSecTunTotalRefreshes_Type=Counter32
_FsIPSecTunTotalRefreshes_Object=MibTableColumn
fsIPSecTunTotalRefreshes=_FsIPSecTunTotalRefreshes_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,17),_FsIPSecTunTotalRefreshes_Type())
fsIPSecTunTotalRefreshes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunTotalRefreshes.setStatus(_A)
_FsIPSecTunCurrentSaInstances_Type=Gauge32
_FsIPSecTunCurrentSaInstances_Object=MibTableColumn
fsIPSecTunCurrentSaInstances=_FsIPSecTunCurrentSaInstances_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,18),_FsIPSecTunCurrentSaInstances_Type())
fsIPSecTunCurrentSaInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunCurrentSaInstances.setStatus(_A)
_FsIPSecTunInSaEncryptAlgo_Type=FSEncryptAlgo
_FsIPSecTunInSaEncryptAlgo_Object=MibTableColumn
fsIPSecTunInSaEncryptAlgo=_FsIPSecTunInSaEncryptAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,19),_FsIPSecTunInSaEncryptAlgo_Type())
fsIPSecTunInSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInSaEncryptAlgo.setStatus(_A)
_FsIPSecTunInSaAhAuthAlgo_Type=FSAuthAlgo
_FsIPSecTunInSaAhAuthAlgo_Object=MibTableColumn
fsIPSecTunInSaAhAuthAlgo=_FsIPSecTunInSaAhAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,20),_FsIPSecTunInSaAhAuthAlgo_Type())
fsIPSecTunInSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInSaAhAuthAlgo.setStatus(_A)
_FsIPSecTunInSaEspAuthAlgo_Type=FSAuthAlgo
_FsIPSecTunInSaEspAuthAlgo_Object=MibTableColumn
fsIPSecTunInSaEspAuthAlgo=_FsIPSecTunInSaEspAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,21),_FsIPSecTunInSaEspAuthAlgo_Type())
fsIPSecTunInSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInSaEspAuthAlgo.setStatus(_A)
_FsIPSecTunDiffHellmanGrp_Type=FSDiffHellmanGrp
_FsIPSecTunDiffHellmanGrp_Object=MibTableColumn
fsIPSecTunDiffHellmanGrp=_FsIPSecTunDiffHellmanGrp_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,22),_FsIPSecTunDiffHellmanGrp_Type())
fsIPSecTunDiffHellmanGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunDiffHellmanGrp.setStatus(_A)
_FsIPSecTunOutSaEncryptAlgo_Type=FSEncryptAlgo
_FsIPSecTunOutSaEncryptAlgo_Object=MibTableColumn
fsIPSecTunOutSaEncryptAlgo=_FsIPSecTunOutSaEncryptAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,23),_FsIPSecTunOutSaEncryptAlgo_Type())
fsIPSecTunOutSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutSaEncryptAlgo.setStatus(_A)
_FsIPSecTunOutSaAhAuthAlgo_Type=FSAuthAlgo
_FsIPSecTunOutSaAhAuthAlgo_Object=MibTableColumn
fsIPSecTunOutSaAhAuthAlgo=_FsIPSecTunOutSaAhAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,24),_FsIPSecTunOutSaAhAuthAlgo_Type())
fsIPSecTunOutSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutSaAhAuthAlgo.setStatus(_A)
_FsIPSecTunOutSaEspAuthAlgo_Type=FSAuthAlgo
_FsIPSecTunOutSaEspAuthAlgo_Object=MibTableColumn
fsIPSecTunOutSaEspAuthAlgo=_FsIPSecTunOutSaEspAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,25),_FsIPSecTunOutSaEspAuthAlgo_Type())
fsIPSecTunOutSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutSaEspAuthAlgo.setStatus(_A)
_FsIPSecTunMapName_Type=DisplayString
_FsIPSecTunMapName_Object=MibTableColumn
fsIPSecTunMapName=_FsIPSecTunMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,26),_FsIPSecTunMapName_Type())
fsIPSecTunMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunMapName.setStatus(_A)
class _FsIPSecTunSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecTunSeqNum_Type.__name__=_D
_FsIPSecTunSeqNum_Object=MibTableColumn
fsIPSecTunSeqNum=_FsIPSecTunSeqNum_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,27),_FsIPSecTunSeqNum_Type())
fsIPSecTunSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunSeqNum.setStatus(_A)
_FsIPSecTunStatus_Type=FSIPSecTunnelState
_FsIPSecTunStatus_Object=MibTableColumn
fsIPSecTunStatus=_FsIPSecTunStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,1,1,28),_FsIPSecTunStatus_Type())
fsIPSecTunStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsIPSecTunStatus.setStatus(_A)
_FsIPSecTunnelStatTable_Object=MibTable
fsIPSecTunnelStatTable=_FsIPSecTunnelStatTable_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2))
if mibBuilder.loadTexts:fsIPSecTunnelStatTable.setStatus(_A)
_FsIPSecTunnelStatEntry_Object=MibTableRow
fsIPSecTunnelStatEntry=_FsIPSecTunnelStatEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1))
fsIPSecTunnelStatEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsIPSecTunnelStatEntry.setStatus(_A)
_FsIPSecTunInOctets_Type=Counter64
_FsIPSecTunInOctets_Object=MibTableColumn
fsIPSecTunInOctets=_FsIPSecTunInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,1),_FsIPSecTunInOctets_Type())
fsIPSecTunInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInOctets.setStatus(_A)
_FsIPSecTunInDecompOctets_Type=Counter64
_FsIPSecTunInDecompOctets_Object=MibTableColumn
fsIPSecTunInDecompOctets=_FsIPSecTunInDecompOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,2),_FsIPSecTunInDecompOctets_Type())
fsIPSecTunInDecompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInDecompOctets.setStatus(_A)
_FsIPSecTunInPkts_Type=Counter64
_FsIPSecTunInPkts_Object=MibTableColumn
fsIPSecTunInPkts=_FsIPSecTunInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,3),_FsIPSecTunInPkts_Type())
fsIPSecTunInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInPkts.setStatus(_A)
_FsIPSecTunInSpeed_Type=Counter64
_FsIPSecTunInSpeed_Object=MibTableColumn
fsIPSecTunInSpeed=_FsIPSecTunInSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,4),_FsIPSecTunInSpeed_Type())
fsIPSecTunInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInSpeed.setStatus(_A)
_FsIPSecTunInDropPkts_Type=Counter64
_FsIPSecTunInDropPkts_Object=MibTableColumn
fsIPSecTunInDropPkts=_FsIPSecTunInDropPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,5),_FsIPSecTunInDropPkts_Type())
fsIPSecTunInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunInDropPkts.setStatus(_A)
_FsIPSecTunOutOctets_Type=Counter64
_FsIPSecTunOutOctets_Object=MibTableColumn
fsIPSecTunOutOctets=_FsIPSecTunOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,6),_FsIPSecTunOutOctets_Type())
fsIPSecTunOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutOctets.setStatus(_A)
_FsIPSecTunOutUncompOctets_Type=Counter64
_FsIPSecTunOutUncompOctets_Object=MibTableColumn
fsIPSecTunOutUncompOctets=_FsIPSecTunOutUncompOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,7),_FsIPSecTunOutUncompOctets_Type())
fsIPSecTunOutUncompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutUncompOctets.setStatus(_A)
_FsIPSecTunOutPkts_Type=Counter64
_FsIPSecTunOutPkts_Object=MibTableColumn
fsIPSecTunOutPkts=_FsIPSecTunOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,8),_FsIPSecTunOutPkts_Type())
fsIPSecTunOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutPkts.setStatus(_A)
_FsIPSecTunOutSpeed_Type=Counter64
_FsIPSecTunOutSpeed_Object=MibTableColumn
fsIPSecTunOutSpeed=_FsIPSecTunOutSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,9),_FsIPSecTunOutSpeed_Type())
fsIPSecTunOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutSpeed.setStatus(_A)
_FsIPSecTunOutDropPkts_Type=Counter64
_FsIPSecTunOutDropPkts_Object=MibTableColumn
fsIPSecTunOutDropPkts=_FsIPSecTunOutDropPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,2,1,10),_FsIPSecTunOutDropPkts_Type())
fsIPSecTunOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTunOutDropPkts.setStatus(_A)
_FsIPSecSaTable_Object=MibTable
fsIPSecSaTable=_FsIPSecSaTable_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3))
if mibBuilder.loadTexts:fsIPSecSaTable.setStatus(_A)
_FsIPSecSaEntry_Object=MibTableRow
fsIPSecSaEntry=_FsIPSecSaEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1))
fsIPSecSaEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsIPSecSaEntry.setStatus(_A)
class _FsIPSecSaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsIPSecSaIndex_Type.__name__=_D
_FsIPSecSaIndex_Object=MibTableColumn
fsIPSecSaIndex=_FsIPSecSaIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,1),_FsIPSecSaIndex_Type())
fsIPSecSaIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsIPSecSaIndex.setStatus(_A)
class _FsIPSecSaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_FsIPSecSaDirection_Type.__name__=_D
_FsIPSecSaDirection_Object=MibTableColumn
fsIPSecSaDirection=_FsIPSecSaDirection_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,2),_FsIPSecSaDirection_Type())
fsIPSecSaDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecSaDirection.setStatus(_A)
class _FsIPSecSaValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsIPSecSaValue_Type.__name__=_O
_FsIPSecSaValue_Object=MibTableColumn
fsIPSecSaValue=_FsIPSecSaValue_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,3),_FsIPSecSaValue_Type())
fsIPSecSaValue.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecSaValue.setStatus(_A)
_FsIPSecSaProtocol_Type=FSSaProtocol
_FsIPSecSaProtocol_Object=MibTableColumn
fsIPSecSaProtocol=_FsIPSecSaProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,4),_FsIPSecSaProtocol_Type())
fsIPSecSaProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecSaProtocol.setStatus(_A)
_FsIPSecSaEncryptAlgo_Type=FSEncryptAlgo
_FsIPSecSaEncryptAlgo_Object=MibTableColumn
fsIPSecSaEncryptAlgo=_FsIPSecSaEncryptAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,5),_FsIPSecSaEncryptAlgo_Type())
fsIPSecSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecSaEncryptAlgo.setStatus(_A)
_FsIPSecSaAuthAlgo_Type=FSAuthAlgo
_FsIPSecSaAuthAlgo_Object=MibTableColumn
fsIPSecSaAuthAlgo=_FsIPSecSaAuthAlgo_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,6),_FsIPSecSaAuthAlgo_Type())
fsIPSecSaAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecSaAuthAlgo.setStatus(_A)
_FsIPSecSaStatus_Type=FSIPSecTunnelState
_FsIPSecSaStatus_Object=MibTableColumn
fsIPSecSaStatus=_FsIPSecSaStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,3,1,7),_FsIPSecSaStatus_Type())
fsIPSecSaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecSaStatus.setStatus(_A)
_FsIPSecTrafficTable_Object=MibTable
fsIPSecTrafficTable=_FsIPSecTrafficTable_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4))
if mibBuilder.loadTexts:fsIPSecTrafficTable.setStatus(_A)
_FsIPSecTrafficEntry_Object=MibTableRow
fsIPSecTrafficEntry=_FsIPSecTrafficEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1))
fsIPSecTrafficEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsIPSecTrafficEntry.setStatus(_A)
_FsIPSecTrafficLocalType_Type=FSTrafficType
_FsIPSecTrafficLocalType_Object=MibTableColumn
fsIPSecTrafficLocalType=_FsIPSecTrafficLocalType_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,1),_FsIPSecTrafficLocalType_Type())
fsIPSecTrafficLocalType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficLocalType.setStatus(_A)
_FsIPSecTrafficLocalAddr1_Type=IpAddress
_FsIPSecTrafficLocalAddr1_Object=MibTableColumn
fsIPSecTrafficLocalAddr1=_FsIPSecTrafficLocalAddr1_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,2),_FsIPSecTrafficLocalAddr1_Type())
fsIPSecTrafficLocalAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficLocalAddr1.setStatus(_A)
_FsIPSecTrafficLocalAddr2_Type=IpAddress
_FsIPSecTrafficLocalAddr2_Object=MibTableColumn
fsIPSecTrafficLocalAddr2=_FsIPSecTrafficLocalAddr2_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,3),_FsIPSecTrafficLocalAddr2_Type())
fsIPSecTrafficLocalAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficLocalAddr2.setStatus(_A)
_FsIPSecTrafficLocalProtocol_Type=FSTunnelProtocol
_FsIPSecTrafficLocalProtocol_Object=MibTableColumn
fsIPSecTrafficLocalProtocol=_FsIPSecTrafficLocalProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,4),_FsIPSecTrafficLocalProtocol_Type())
fsIPSecTrafficLocalProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficLocalProtocol.setStatus(_A)
class _FsIPSecTrafficLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIPSecTrafficLocalPort_Type.__name__=_D
_FsIPSecTrafficLocalPort_Object=MibTableColumn
fsIPSecTrafficLocalPort=_FsIPSecTrafficLocalPort_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,5),_FsIPSecTrafficLocalPort_Type())
fsIPSecTrafficLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficLocalPort.setStatus(_A)
_FsIPSecTrafficLocalHostname_Type=DisplayString
_FsIPSecTrafficLocalHostname_Object=MibTableColumn
fsIPSecTrafficLocalHostname=_FsIPSecTrafficLocalHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,6),_FsIPSecTrafficLocalHostname_Type())
fsIPSecTrafficLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficLocalHostname.setStatus(_A)
_FsIPSecTrafficRemoteType_Type=FSTrafficType
_FsIPSecTrafficRemoteType_Object=MibTableColumn
fsIPSecTrafficRemoteType=_FsIPSecTrafficRemoteType_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,7),_FsIPSecTrafficRemoteType_Type())
fsIPSecTrafficRemoteType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficRemoteType.setStatus(_A)
_FsIPSecTrafficRemoteAddr1_Type=IpAddress
_FsIPSecTrafficRemoteAddr1_Object=MibTableColumn
fsIPSecTrafficRemoteAddr1=_FsIPSecTrafficRemoteAddr1_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,8),_FsIPSecTrafficRemoteAddr1_Type())
fsIPSecTrafficRemoteAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficRemoteAddr1.setStatus(_A)
_FsIPSecTrafficRemoteAddr2_Type=IpAddress
_FsIPSecTrafficRemoteAddr2_Object=MibTableColumn
fsIPSecTrafficRemoteAddr2=_FsIPSecTrafficRemoteAddr2_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,9),_FsIPSecTrafficRemoteAddr2_Type())
fsIPSecTrafficRemoteAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficRemoteAddr2.setStatus(_A)
_FsIPSecTrafficRemoteProtocol_Type=FSTunnelProtocol
_FsIPSecTrafficRemoteProtocol_Object=MibTableColumn
fsIPSecTrafficRemoteProtocol=_FsIPSecTrafficRemoteProtocol_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,10),_FsIPSecTrafficRemoteProtocol_Type())
fsIPSecTrafficRemoteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficRemoteProtocol.setStatus(_A)
class _FsIPSecTrafficRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsIPSecTrafficRemotePort_Type.__name__=_D
_FsIPSecTrafficRemotePort_Object=MibTableColumn
fsIPSecTrafficRemotePort=_FsIPSecTrafficRemotePort_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,11),_FsIPSecTrafficRemotePort_Type())
fsIPSecTrafficRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficRemotePort.setStatus(_A)
_FsIPSecTrafficRemoteHostname_Type=DisplayString
_FsIPSecTrafficRemoteHostname_Object=MibTableColumn
fsIPSecTrafficRemoteHostname=_FsIPSecTrafficRemoteHostname_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,4,1,12),_FsIPSecTrafficRemoteHostname_Type())
fsIPSecTrafficRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecTrafficRemoteHostname.setStatus(_A)
_FsIPSecGlobalStats_ObjectIdentity=ObjectIdentity
fsIPSecGlobalStats=_FsIPSecGlobalStats_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,1,5))
_FsIPSecGlobalActiveTunnels_Type=Gauge32
_FsIPSecGlobalActiveTunnels_Object=MibScalar
fsIPSecGlobalActiveTunnels=_FsIPSecGlobalActiveTunnels_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,1),_FsIPSecGlobalActiveTunnels_Type())
fsIPSecGlobalActiveTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalActiveTunnels.setStatus(_A)
_FsIPSecGlobalActiveSas_Type=Gauge32
_FsIPSecGlobalActiveSas_Object=MibScalar
fsIPSecGlobalActiveSas=_FsIPSecGlobalActiveSas_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,2),_FsIPSecGlobalActiveSas_Type())
fsIPSecGlobalActiveSas.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalActiveSas.setStatus(_A)
_FsIPSecGlobalInOctets_Type=Counter64
_FsIPSecGlobalInOctets_Object=MibScalar
fsIPSecGlobalInOctets=_FsIPSecGlobalInOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,3),_FsIPSecGlobalInOctets_Type())
fsIPSecGlobalInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalInOctets.setStatus(_A)
_FsIPSecGlobalInPkts_Type=Counter64
_FsIPSecGlobalInPkts_Object=MibScalar
fsIPSecGlobalInPkts=_FsIPSecGlobalInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,4),_FsIPSecGlobalInPkts_Type())
fsIPSecGlobalInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalInPkts.setStatus(_A)
_FsIPSecGlobalInSpeed_Type=Counter64
_FsIPSecGlobalInSpeed_Object=MibScalar
fsIPSecGlobalInSpeed=_FsIPSecGlobalInSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,5),_FsIPSecGlobalInSpeed_Type())
fsIPSecGlobalInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalInSpeed.setStatus(_A)
_FsIPSecGlobalInDrops_Type=Counter64
_FsIPSecGlobalInDrops_Object=MibScalar
fsIPSecGlobalInDrops=_FsIPSecGlobalInDrops_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,6),_FsIPSecGlobalInDrops_Type())
fsIPSecGlobalInDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalInDrops.setStatus(_A)
_FsIPSecGlobalOutOctets_Type=Counter64
_FsIPSecGlobalOutOctets_Object=MibScalar
fsIPSecGlobalOutOctets=_FsIPSecGlobalOutOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,7),_FsIPSecGlobalOutOctets_Type())
fsIPSecGlobalOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalOutOctets.setStatus(_A)
_FsIPSecGlobalOutPkts_Type=Counter64
_FsIPSecGlobalOutPkts_Object=MibScalar
fsIPSecGlobalOutPkts=_FsIPSecGlobalOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,8),_FsIPSecGlobalOutPkts_Type())
fsIPSecGlobalOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalOutPkts.setStatus(_A)
_FsIPSecGlobalOutSpeed_Type=Counter64
_FsIPSecGlobalOutSpeed_Object=MibScalar
fsIPSecGlobalOutSpeed=_FsIPSecGlobalOutSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,9),_FsIPSecGlobalOutSpeed_Type())
fsIPSecGlobalOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalOutSpeed.setStatus(_A)
_FsIPSecGlobalOutDrops_Type=Counter64
_FsIPSecGlobalOutDrops_Object=MibScalar
fsIPSecGlobalOutDrops=_FsIPSecGlobalOutDrops_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,5,10),_FsIPSecGlobalOutDrops_Type())
fsIPSecGlobalOutDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPSecGlobalOutDrops.setStatus(_A)
_FsIPSecTrapObject_ObjectIdentity=ObjectIdentity
fsIPSecTrapObject=_FsIPSecTrapObject_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,1,6))
_FsIPSecMapName_Type=DisplayString
_FsIPSecMapName_Object=MibScalar
fsIPSecMapName=_FsIPSecMapName_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,6,1),_FsIPSecMapName_Type())
fsIPSecMapName.setMaxAccess(_K)
if mibBuilder.loadTexts:fsIPSecMapName.setStatus(_A)
_FsIPSecSeqNum_Type=Integer32
_FsIPSecSeqNum_Object=MibScalar
fsIPSecSeqNum=_FsIPSecSeqNum_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,6,2),_FsIPSecSeqNum_Type())
fsIPSecSeqNum.setMaxAccess(_K)
if mibBuilder.loadTexts:fsIPSecSeqNum.setStatus(_A)
_FsIPSecSpiValue_Type=Integer32
_FsIPSecSpiValue_Object=MibScalar
fsIPSecSpiValue=_FsIPSecSpiValue_Object((1,3,6,1,4,1,52642,1,1,10,2,94,1,6,3),_FsIPSecSpiValue_Type())
fsIPSecSpiValue.setMaxAccess(_K)
if mibBuilder.loadTexts:fsIPSecSpiValue.setStatus(_A)
_FsIPSecTrap_ObjectIdentity=ObjectIdentity
fsIPSecTrap=_FsIPSecTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,1,7))
_FsIPSecNotifications_ObjectIdentity=ObjectIdentity
fsIPSecNotifications=_FsIPSecNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,1,7,1))
_FsIPSecConformance_ObjectIdentity=ObjectIdentity
fsIPSecConformance=_FsIPSecConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,2))
_FsIPSecCompliances_ObjectIdentity=ObjectIdentity
fsIPSecCompliances=_FsIPSecCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,2,1))
_FsIPSecGroups_ObjectIdentity=ObjectIdentity
fsIPSecGroups=_FsIPSecGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,94,2,2))
fsIPSecTunnelTableGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,1))
fsIPSecTunnelTableGroup.setObjects(*((_B,_R),(_B,_G),(_B,_E),(_B,_H),(_B,_I),(_B,_S),(_B,_T),(_B,_U),(_B,_L),(_B,_M),(_B,_V),(_B,_N),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:fsIPSecTunnelTableGroup.setStatus(_A)
fsIPSecTunnelStatGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,2))
fsIPSecTunnelStatGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:fsIPSecTunnelStatGroup.setStatus(_A)
fsIPSecSaGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,3))
fsIPSecSaGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:fsIPSecSaGroup.setStatus(_A)
fsIPSecTrafficTableGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,4))
fsIPSecTrafficTableGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:fsIPSecTrafficTableGroup.setStatus(_A)
fsIPSecGlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,5))
fsIPSecGlobalStatsGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:fsIPSecGlobalStatsGroup.setStatus(_A)
fsIPSecTrapObjectGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,6))
fsIPSecTrapObjectGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:fsIPSecTrapObjectGroup.setStatus(_A)
fsIPSecTunnelStart=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,94,1,7,1,1))
fsIPSecTunnelStart.setObjects(*((_B,_G),(_B,_E),(_B,_H),(_B,_I),(_B,_M),(_B,_L)))
if mibBuilder.loadTexts:fsIPSecTunnelStart.setStatus(_A)
fsIPSecTunnelStop=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,94,1,7,1,2))
fsIPSecTunnelStop.setObjects(*((_B,_G),(_B,_E),(_B,_H),(_B,_I),(_B,_N)))
if mibBuilder.loadTexts:fsIPSecTunnelStop.setStatus(_A)
fsIPSecTrapGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,94,2,2,7))
fsIPSecTrapGroup.setObjects(*((_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:fsIPSecTrapGroup.setStatus(_A)
fsIPSecCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,94,2,1,1))
fsIPSecCompliance.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:fsIPSecCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FSDiffHellmanGrp':FSDiffHellmanGrp,'FSEncapMode':FSEncapMode,'FSEncryptAlgo':FSEncryptAlgo,'FSAuthAlgo':FSAuthAlgo,'FSSaProtocol':FSSaProtocol,'FSTunnelProtocol':FSTunnelProtocol,'FSTrafficType':FSTrafficType,'FSIPSecNegoType':FSIPSecNegoType,'FSIPSecTunnelState':FSIPSecTunnelState,'fsIPSecMonitor':fsIPSecMonitor,'fsIPSecObjects':fsIPSecObjects,'fsIPSecTunnelTable':fsIPSecTunnelTable,'fsIPSecTunnelEntry':fsIPSecTunnelEntry,'fsIPSecTunIfIndex':fsIPSecTunIfIndex,'fsIPSecTunIndex':fsIPSecTunIndex,_R:fsIPSecTunIKETunnelIndex,_G:fsIPSecTunLocalAddr,_E:fsIPSecTunRemoteAddr,_H:fsIPSecTunLocalHostname,_I:fsIPSecTunRemoteHostname,_S:fsIPSecTunKeyType,_T:fsIPSecTunEncapMode,_U:fsIPSecTunInitiator,_L:fsIPSecTunLifeSize,_M:fsIPSecTunLifeTime,_V:fsIPSecTunRemainTime,_N:fsIPSecTunActiveTime,'fsIPSecTunCreateTime':fsIPSecTunCreateTime,_W:fsIPSecTunRemainSize,_X:fsIPSecTunTotalRefreshes,_Y:fsIPSecTunCurrentSaInstances,_Z:fsIPSecTunInSaEncryptAlgo,_a:fsIPSecTunInSaAhAuthAlgo,_b:fsIPSecTunInSaEspAuthAlgo,_c:fsIPSecTunDiffHellmanGrp,_d:fsIPSecTunOutSaEncryptAlgo,_e:fsIPSecTunOutSaAhAuthAlgo,_f:fsIPSecTunOutSaEspAuthAlgo,'fsIPSecTunMapName':fsIPSecTunMapName,'fsIPSecTunSeqNum':fsIPSecTunSeqNum,_g:fsIPSecTunStatus,'fsIPSecTunnelStatTable':fsIPSecTunnelStatTable,'fsIPSecTunnelStatEntry':fsIPSecTunnelStatEntry,_h:fsIPSecTunInOctets,_i:fsIPSecTunInDecompOctets,_j:fsIPSecTunInPkts,_k:fsIPSecTunInSpeed,_l:fsIPSecTunInDropPkts,_m:fsIPSecTunOutOctets,_n:fsIPSecTunOutUncompOctets,_o:fsIPSecTunOutPkts,_p:fsIPSecTunOutSpeed,_q:fsIPSecTunOutDropPkts,'fsIPSecSaTable':fsIPSecSaTable,'fsIPSecSaEntry':fsIPSecSaEntry,'fsIPSecSaIndex':fsIPSecSaIndex,_r:fsIPSecSaDirection,_s:fsIPSecSaValue,_t:fsIPSecSaProtocol,_u:fsIPSecSaEncryptAlgo,_v:fsIPSecSaAuthAlgo,_w:fsIPSecSaStatus,'fsIPSecTrafficTable':fsIPSecTrafficTable,'fsIPSecTrafficEntry':fsIPSecTrafficEntry,_x:fsIPSecTrafficLocalType,_y:fsIPSecTrafficLocalAddr1,_z:fsIPSecTrafficLocalAddr2,_A0:fsIPSecTrafficLocalProtocol,_A1:fsIPSecTrafficLocalPort,_A2:fsIPSecTrafficLocalHostname,_A3:fsIPSecTrafficRemoteType,_A4:fsIPSecTrafficRemoteAddr1,_A5:fsIPSecTrafficRemoteAddr2,_A6:fsIPSecTrafficRemoteProtocol,_A7:fsIPSecTrafficRemotePort,_A8:fsIPSecTrafficRemoteHostname,'fsIPSecGlobalStats':fsIPSecGlobalStats,_A9:fsIPSecGlobalActiveTunnels,_AA:fsIPSecGlobalActiveSas,_AB:fsIPSecGlobalInOctets,_AC:fsIPSecGlobalInPkts,_AE:fsIPSecGlobalInSpeed,_AD:fsIPSecGlobalInDrops,_AF:fsIPSecGlobalOutOctets,_AG:fsIPSecGlobalOutPkts,_AI:fsIPSecGlobalOutSpeed,_AH:fsIPSecGlobalOutDrops,'fsIPSecTrapObject':fsIPSecTrapObject,_AJ:fsIPSecMapName,_AK:fsIPSecSeqNum,_AL:fsIPSecSpiValue,'fsIPSecTrap':fsIPSecTrap,'fsIPSecNotifications':fsIPSecNotifications,_AM:fsIPSecTunnelStart,_AN:fsIPSecTunnelStop,'fsIPSecConformance':fsIPSecConformance,'fsIPSecCompliances':fsIPSecCompliances,'fsIPSecCompliance':fsIPSecCompliance,'fsIPSecGroups':fsIPSecGroups,_AO:fsIPSecTunnelTableGroup,_AP:fsIPSecTunnelStatGroup,_AQ:fsIPSecSaGroup,_AR:fsIPSecTrafficTableGroup,_AS:fsIPSecGlobalStatsGroup,_AT:fsIPSecTrapObjectGroup,_AU:fsIPSecTrapGroup})