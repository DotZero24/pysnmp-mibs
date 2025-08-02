_AU='qtechIPSecTrapGroup'
_AT='qtechIPSecTrapObjectGroup'
_AS='qtechIPSecGlobalStatsGroup'
_AR='qtechIPSecTrafficTableGroup'
_AQ='qtechIPSecSaGroup'
_AP='qtechIPSecTunnelStatGroup'
_AO='qtechIPSecTunnelTableGroup'
_AN='qtechIPSecTunnelStop'
_AM='qtechIPSecTunnelStart'
_AL='qtechIPSecSpiValue'
_AK='qtechIPSecSeqNum'
_AJ='qtechIPSecMapName'
_AI='qtechIPSecGlobalOutSpeed'
_AH='qtechIPSecGlobalOutDrops'
_AG='qtechIPSecGlobalOutPkts'
_AF='qtechIPSecGlobalOutOctets'
_AE='qtechIPSecGlobalInSpeed'
_AD='qtechIPSecGlobalInDrops'
_AC='qtechIPSecGlobalInPkts'
_AB='qtechIPSecGlobalInOctets'
_AA='qtechIPSecGlobalActiveSas'
_A9='qtechIPSecGlobalActiveTunnels'
_A8='qtechIPSecTrafficRemoteHostname'
_A7='qtechIPSecTrafficRemotePort'
_A6='qtechIPSecTrafficRemoteProtocol'
_A5='qtechIPSecTrafficRemoteAddr2'
_A4='qtechIPSecTrafficRemoteAddr1'
_A3='qtechIPSecTrafficRemoteType'
_A2='qtechIPSecTrafficLocalHostname'
_A1='qtechIPSecTrafficLocalPort'
_A0='qtechIPSecTrafficLocalProtocol'
_z='qtechIPSecTrafficLocalAddr2'
_y='qtechIPSecTrafficLocalAddr1'
_x='qtechIPSecTrafficLocalType'
_w='qtechIPSecSaStatus'
_v='qtechIPSecSaAuthAlgo'
_u='qtechIPSecSaEncryptAlgo'
_t='qtechIPSecSaProtocol'
_s='qtechIPSecSaValue'
_r='qtechIPSecSaDirection'
_q='qtechIPSecTunOutDropPkts'
_p='qtechIPSecTunOutSpeed'
_o='qtechIPSecTunOutPkts'
_n='qtechIPSecTunOutUncompOctets'
_m='qtechIPSecTunOutOctets'
_l='qtechIPSecTunInDropPkts'
_k='qtechIPSecTunInSpeed'
_j='qtechIPSecTunInPkts'
_i='qtechIPSecTunInDecompOctets'
_h='qtechIPSecTunInOctets'
_g='qtechIPSecTunStatus'
_f='qtechIPSecTunOutSaEspAuthAlgo'
_e='qtechIPSecTunOutSaAhAuthAlgo'
_d='qtechIPSecTunOutSaEncryptAlgo'
_c='qtechIPSecTunDiffHellmanGrp'
_b='qtechIPSecTunInSaEspAuthAlgo'
_a='qtechIPSecTunInSaAhAuthAlgo'
_Z='qtechIPSecTunInSaEncryptAlgo'
_Y='qtechIPSecTunCurrentSaInstances'
_X='qtechIPSecTunTotalRefreshes'
_W='qtechIPSecTunRemainSize'
_V='qtechIPSecTunRemainTime'
_U='qtechIPSecTunInitiator'
_T='qtechIPSecTunEncapMode'
_S='qtechIPSecTunKeyType'
_R='qtechIPSecTunIKETunnelIndex'
_Q='invalidAlg'
_P='invalidMode'
_O='Unsigned32'
_N='qtechIPSecTunActiveTime'
_M='qtechIPSecTunLifeTime'
_L='qtechIPSecTunLifeSize'
_K='accessible-for-notify'
_J='not-accessible'
_I='qtechIPSecTunRemoteHostname'
_H='qtechIPSecTunLocalHostname'
_G='qtechIPSecTunLocalAddr'
_F='none'
_E='qtechIPSecTunRemoteAddr'
_D='Integer32'
_C='read-only'
_B='QTECH-IPSEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
qtechIPSecMonitor=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,94))
if mibBuilder.loadTexts:qtechIPSecMonitor.setRevisions(('2011-02-17 00:00',))
class QtechDiffHellmanGrp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*((_F,0),('modp768',1),('modp1024',2),(_P,2147483647)))
class QtechEncapMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('tunnel',1),('transport',2),(_P,2147483647)))
class QtechEncryptAlgo(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,12,128,2147483647)));namedValues=NamedValues(*((_F,0),('desCbc',2),('threedesCbc',3),('aesCbc',12),('sm1Cbc',128),(_Q,2147483647)))
class QtechAuthAlgo(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,2147483647)));namedValues=NamedValues(*((_F,0),('md5',1),('sha',2),(_Q,2147483647)))
class QtechSaProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('reserved',0),('isakmp',1),('ah',2),('esp',3)))
class QtechTunnelProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,17,50,51)));namedValues=NamedValues(*((_F,0),('icmp',1),('igmp',2),('ip',4),('tcp',6),('udp',17),('esp',50),('ah',51)))
class QtechTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ipv4Addr',1),('ipv4AddrSubnet',2),('ipv6Addr',3),('ipv6AddrSubnet',4),('ipv4AddrRange',5),('ipv6AddrRange',6)))
class QtechIPSecNegoType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('ike',1),('manual',2),('invalidType',2147483647)))
class QtechIPSecTunnelState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('establishing',1),('active',2),('expiring',3)))
_QtechIPSecObjects_ObjectIdentity=ObjectIdentity
qtechIPSecObjects=_QtechIPSecObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,1))
_QtechIPSecTunnelTable_Object=MibTable
qtechIPSecTunnelTable=_QtechIPSecTunnelTable_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1))
if mibBuilder.loadTexts:qtechIPSecTunnelTable.setStatus(_A)
_QtechIPSecTunnelEntry_Object=MibTableRow
qtechIPSecTunnelEntry=_QtechIPSecTunnelEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1))
qtechIPSecTunnelEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechIPSecTunnelEntry.setStatus(_A)
class _QtechIPSecTunIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecTunIfIndex_Type.__name__=_D
_QtechIPSecTunIfIndex_Object=MibTableColumn
qtechIPSecTunIfIndex=_QtechIPSecTunIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,1),_QtechIPSecTunIfIndex_Type())
qtechIPSecTunIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechIPSecTunIfIndex.setStatus(_A)
class _QtechIPSecTunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecTunIndex_Type.__name__=_D
_QtechIPSecTunIndex_Object=MibTableColumn
qtechIPSecTunIndex=_QtechIPSecTunIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,2),_QtechIPSecTunIndex_Type())
qtechIPSecTunIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechIPSecTunIndex.setStatus(_A)
class _QtechIPSecTunIKETunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecTunIKETunnelIndex_Type.__name__=_D
_QtechIPSecTunIKETunnelIndex_Object=MibTableColumn
qtechIPSecTunIKETunnelIndex=_QtechIPSecTunIKETunnelIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,3),_QtechIPSecTunIKETunnelIndex_Type())
qtechIPSecTunIKETunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunIKETunnelIndex.setStatus(_A)
_QtechIPSecTunLocalAddr_Type=IpAddress
_QtechIPSecTunLocalAddr_Object=MibTableColumn
qtechIPSecTunLocalAddr=_QtechIPSecTunLocalAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,4),_QtechIPSecTunLocalAddr_Type())
qtechIPSecTunLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunLocalAddr.setStatus(_A)
_QtechIPSecTunRemoteAddr_Type=IpAddress
_QtechIPSecTunRemoteAddr_Object=MibTableColumn
qtechIPSecTunRemoteAddr=_QtechIPSecTunRemoteAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,5),_QtechIPSecTunRemoteAddr_Type())
qtechIPSecTunRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunRemoteAddr.setStatus(_A)
_QtechIPSecTunLocalHostname_Type=DisplayString
_QtechIPSecTunLocalHostname_Object=MibTableColumn
qtechIPSecTunLocalHostname=_QtechIPSecTunLocalHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,6),_QtechIPSecTunLocalHostname_Type())
qtechIPSecTunLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunLocalHostname.setStatus(_A)
_QtechIPSecTunRemoteHostname_Type=DisplayString
_QtechIPSecTunRemoteHostname_Object=MibTableColumn
qtechIPSecTunRemoteHostname=_QtechIPSecTunRemoteHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,7),_QtechIPSecTunRemoteHostname_Type())
qtechIPSecTunRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunRemoteHostname.setStatus(_A)
_QtechIPSecTunKeyType_Type=QtechIPSecNegoType
_QtechIPSecTunKeyType_Object=MibTableColumn
qtechIPSecTunKeyType=_QtechIPSecTunKeyType_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,8),_QtechIPSecTunKeyType_Type())
qtechIPSecTunKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunKeyType.setStatus(_A)
_QtechIPSecTunEncapMode_Type=QtechEncapMode
_QtechIPSecTunEncapMode_Object=MibTableColumn
qtechIPSecTunEncapMode=_QtechIPSecTunEncapMode_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,9),_QtechIPSecTunEncapMode_Type())
qtechIPSecTunEncapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunEncapMode.setStatus(_A)
class _QtechIPSecTunInitiator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('local',1),('remote',2),(_F,2147483647)))
_QtechIPSecTunInitiator_Type.__name__=_D
_QtechIPSecTunInitiator_Object=MibTableColumn
qtechIPSecTunInitiator=_QtechIPSecTunInitiator_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,10),_QtechIPSecTunInitiator_Type())
qtechIPSecTunInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInitiator.setStatus(_A)
class _QtechIPSecTunLifeSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecTunLifeSize_Type.__name__=_D
_QtechIPSecTunLifeSize_Object=MibTableColumn
qtechIPSecTunLifeSize=_QtechIPSecTunLifeSize_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,11),_QtechIPSecTunLifeSize_Type())
qtechIPSecTunLifeSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunLifeSize.setStatus(_A)
class _QtechIPSecTunLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecTunLifeTime_Type.__name__=_D
_QtechIPSecTunLifeTime_Object=MibTableColumn
qtechIPSecTunLifeTime=_QtechIPSecTunLifeTime_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,12),_QtechIPSecTunLifeTime_Type())
qtechIPSecTunLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunLifeTime.setStatus(_A)
class _QtechIPSecTunRemainTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSecTunRemainTime_Type.__name__=_D
_QtechIPSecTunRemainTime_Object=MibTableColumn
qtechIPSecTunRemainTime=_QtechIPSecTunRemainTime_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,13),_QtechIPSecTunRemainTime_Type())
qtechIPSecTunRemainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunRemainTime.setStatus(_A)
class _QtechIPSecTunActiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSecTunActiveTime_Type.__name__=_D
_QtechIPSecTunActiveTime_Object=MibTableColumn
qtechIPSecTunActiveTime=_QtechIPSecTunActiveTime_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,14),_QtechIPSecTunActiveTime_Type())
qtechIPSecTunActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunActiveTime.setStatus(_A)
class _QtechIPSecTunCreateTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSecTunCreateTime_Type.__name__=_D
_QtechIPSecTunCreateTime_Object=MibTableColumn
qtechIPSecTunCreateTime=_QtechIPSecTunCreateTime_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,15),_QtechIPSecTunCreateTime_Type())
qtechIPSecTunCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunCreateTime.setStatus(_A)
class _QtechIPSecTunRemainSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIPSecTunRemainSize_Type.__name__=_D
_QtechIPSecTunRemainSize_Object=MibTableColumn
qtechIPSecTunRemainSize=_QtechIPSecTunRemainSize_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,16),_QtechIPSecTunRemainSize_Type())
qtechIPSecTunRemainSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunRemainSize.setStatus(_A)
_QtechIPSecTunTotalRefreshes_Type=Counter32
_QtechIPSecTunTotalRefreshes_Object=MibTableColumn
qtechIPSecTunTotalRefreshes=_QtechIPSecTunTotalRefreshes_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,17),_QtechIPSecTunTotalRefreshes_Type())
qtechIPSecTunTotalRefreshes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunTotalRefreshes.setStatus(_A)
_QtechIPSecTunCurrentSaInstances_Type=Gauge32
_QtechIPSecTunCurrentSaInstances_Object=MibTableColumn
qtechIPSecTunCurrentSaInstances=_QtechIPSecTunCurrentSaInstances_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,18),_QtechIPSecTunCurrentSaInstances_Type())
qtechIPSecTunCurrentSaInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunCurrentSaInstances.setStatus(_A)
_QtechIPSecTunInSaEncryptAlgo_Type=QtechEncryptAlgo
_QtechIPSecTunInSaEncryptAlgo_Object=MibTableColumn
qtechIPSecTunInSaEncryptAlgo=_QtechIPSecTunInSaEncryptAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,19),_QtechIPSecTunInSaEncryptAlgo_Type())
qtechIPSecTunInSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInSaEncryptAlgo.setStatus(_A)
_QtechIPSecTunInSaAhAuthAlgo_Type=QtechAuthAlgo
_QtechIPSecTunInSaAhAuthAlgo_Object=MibTableColumn
qtechIPSecTunInSaAhAuthAlgo=_QtechIPSecTunInSaAhAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,20),_QtechIPSecTunInSaAhAuthAlgo_Type())
qtechIPSecTunInSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInSaAhAuthAlgo.setStatus(_A)
_QtechIPSecTunInSaEspAuthAlgo_Type=QtechAuthAlgo
_QtechIPSecTunInSaEspAuthAlgo_Object=MibTableColumn
qtechIPSecTunInSaEspAuthAlgo=_QtechIPSecTunInSaEspAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,21),_QtechIPSecTunInSaEspAuthAlgo_Type())
qtechIPSecTunInSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInSaEspAuthAlgo.setStatus(_A)
_QtechIPSecTunDiffHellmanGrp_Type=QtechDiffHellmanGrp
_QtechIPSecTunDiffHellmanGrp_Object=MibTableColumn
qtechIPSecTunDiffHellmanGrp=_QtechIPSecTunDiffHellmanGrp_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,22),_QtechIPSecTunDiffHellmanGrp_Type())
qtechIPSecTunDiffHellmanGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunDiffHellmanGrp.setStatus(_A)
_QtechIPSecTunOutSaEncryptAlgo_Type=QtechEncryptAlgo
_QtechIPSecTunOutSaEncryptAlgo_Object=MibTableColumn
qtechIPSecTunOutSaEncryptAlgo=_QtechIPSecTunOutSaEncryptAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,23),_QtechIPSecTunOutSaEncryptAlgo_Type())
qtechIPSecTunOutSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutSaEncryptAlgo.setStatus(_A)
_QtechIPSecTunOutSaAhAuthAlgo_Type=QtechAuthAlgo
_QtechIPSecTunOutSaAhAuthAlgo_Object=MibTableColumn
qtechIPSecTunOutSaAhAuthAlgo=_QtechIPSecTunOutSaAhAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,24),_QtechIPSecTunOutSaAhAuthAlgo_Type())
qtechIPSecTunOutSaAhAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutSaAhAuthAlgo.setStatus(_A)
_QtechIPSecTunOutSaEspAuthAlgo_Type=QtechAuthAlgo
_QtechIPSecTunOutSaEspAuthAlgo_Object=MibTableColumn
qtechIPSecTunOutSaEspAuthAlgo=_QtechIPSecTunOutSaEspAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,25),_QtechIPSecTunOutSaEspAuthAlgo_Type())
qtechIPSecTunOutSaEspAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutSaEspAuthAlgo.setStatus(_A)
_QtechIPSecTunMapName_Type=DisplayString
_QtechIPSecTunMapName_Object=MibTableColumn
qtechIPSecTunMapName=_QtechIPSecTunMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,26),_QtechIPSecTunMapName_Type())
qtechIPSecTunMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunMapName.setStatus(_A)
class _QtechIPSecTunSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecTunSeqNum_Type.__name__=_D
_QtechIPSecTunSeqNum_Object=MibTableColumn
qtechIPSecTunSeqNum=_QtechIPSecTunSeqNum_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,27),_QtechIPSecTunSeqNum_Type())
qtechIPSecTunSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunSeqNum.setStatus(_A)
_QtechIPSecTunStatus_Type=QtechIPSecTunnelState
_QtechIPSecTunStatus_Object=MibTableColumn
qtechIPSecTunStatus=_QtechIPSecTunStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,1,1,28),_QtechIPSecTunStatus_Type())
qtechIPSecTunStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechIPSecTunStatus.setStatus(_A)
_QtechIPSecTunnelStatTable_Object=MibTable
qtechIPSecTunnelStatTable=_QtechIPSecTunnelStatTable_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2))
if mibBuilder.loadTexts:qtechIPSecTunnelStatTable.setStatus(_A)
_QtechIPSecTunnelStatEntry_Object=MibTableRow
qtechIPSecTunnelStatEntry=_QtechIPSecTunnelStatEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1))
qtechIPSecTunnelStatEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechIPSecTunnelStatEntry.setStatus(_A)
_QtechIPSecTunInOctets_Type=Counter64
_QtechIPSecTunInOctets_Object=MibTableColumn
qtechIPSecTunInOctets=_QtechIPSecTunInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,1),_QtechIPSecTunInOctets_Type())
qtechIPSecTunInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInOctets.setStatus(_A)
_QtechIPSecTunInDecompOctets_Type=Counter64
_QtechIPSecTunInDecompOctets_Object=MibTableColumn
qtechIPSecTunInDecompOctets=_QtechIPSecTunInDecompOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,2),_QtechIPSecTunInDecompOctets_Type())
qtechIPSecTunInDecompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInDecompOctets.setStatus(_A)
_QtechIPSecTunInPkts_Type=Counter64
_QtechIPSecTunInPkts_Object=MibTableColumn
qtechIPSecTunInPkts=_QtechIPSecTunInPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,3),_QtechIPSecTunInPkts_Type())
qtechIPSecTunInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInPkts.setStatus(_A)
_QtechIPSecTunInSpeed_Type=Counter64
_QtechIPSecTunInSpeed_Object=MibTableColumn
qtechIPSecTunInSpeed=_QtechIPSecTunInSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,4),_QtechIPSecTunInSpeed_Type())
qtechIPSecTunInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInSpeed.setStatus(_A)
_QtechIPSecTunInDropPkts_Type=Counter64
_QtechIPSecTunInDropPkts_Object=MibTableColumn
qtechIPSecTunInDropPkts=_QtechIPSecTunInDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,5),_QtechIPSecTunInDropPkts_Type())
qtechIPSecTunInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunInDropPkts.setStatus(_A)
_QtechIPSecTunOutOctets_Type=Counter64
_QtechIPSecTunOutOctets_Object=MibTableColumn
qtechIPSecTunOutOctets=_QtechIPSecTunOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,6),_QtechIPSecTunOutOctets_Type())
qtechIPSecTunOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutOctets.setStatus(_A)
_QtechIPSecTunOutUncompOctets_Type=Counter64
_QtechIPSecTunOutUncompOctets_Object=MibTableColumn
qtechIPSecTunOutUncompOctets=_QtechIPSecTunOutUncompOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,7),_QtechIPSecTunOutUncompOctets_Type())
qtechIPSecTunOutUncompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutUncompOctets.setStatus(_A)
_QtechIPSecTunOutPkts_Type=Counter64
_QtechIPSecTunOutPkts_Object=MibTableColumn
qtechIPSecTunOutPkts=_QtechIPSecTunOutPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,8),_QtechIPSecTunOutPkts_Type())
qtechIPSecTunOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutPkts.setStatus(_A)
_QtechIPSecTunOutSpeed_Type=Counter64
_QtechIPSecTunOutSpeed_Object=MibTableColumn
qtechIPSecTunOutSpeed=_QtechIPSecTunOutSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,9),_QtechIPSecTunOutSpeed_Type())
qtechIPSecTunOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutSpeed.setStatus(_A)
_QtechIPSecTunOutDropPkts_Type=Counter64
_QtechIPSecTunOutDropPkts_Object=MibTableColumn
qtechIPSecTunOutDropPkts=_QtechIPSecTunOutDropPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,2,1,10),_QtechIPSecTunOutDropPkts_Type())
qtechIPSecTunOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTunOutDropPkts.setStatus(_A)
_QtechIPSecSaTable_Object=MibTable
qtechIPSecSaTable=_QtechIPSecSaTable_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3))
if mibBuilder.loadTexts:qtechIPSecSaTable.setStatus(_A)
_QtechIPSecSaEntry_Object=MibTableRow
qtechIPSecSaEntry=_QtechIPSecSaEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1))
qtechIPSecSaEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechIPSecSaEntry.setStatus(_A)
class _QtechIPSecSaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechIPSecSaIndex_Type.__name__=_D
_QtechIPSecSaIndex_Object=MibTableColumn
qtechIPSecSaIndex=_QtechIPSecSaIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,1),_QtechIPSecSaIndex_Type())
qtechIPSecSaIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechIPSecSaIndex.setStatus(_A)
class _QtechIPSecSaDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_QtechIPSecSaDirection_Type.__name__=_D
_QtechIPSecSaDirection_Object=MibTableColumn
qtechIPSecSaDirection=_QtechIPSecSaDirection_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,2),_QtechIPSecSaDirection_Type())
qtechIPSecSaDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecSaDirection.setStatus(_A)
class _QtechIPSecSaValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_QtechIPSecSaValue_Type.__name__=_O
_QtechIPSecSaValue_Object=MibTableColumn
qtechIPSecSaValue=_QtechIPSecSaValue_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,3),_QtechIPSecSaValue_Type())
qtechIPSecSaValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecSaValue.setStatus(_A)
_QtechIPSecSaProtocol_Type=QtechSaProtocol
_QtechIPSecSaProtocol_Object=MibTableColumn
qtechIPSecSaProtocol=_QtechIPSecSaProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,4),_QtechIPSecSaProtocol_Type())
qtechIPSecSaProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecSaProtocol.setStatus(_A)
_QtechIPSecSaEncryptAlgo_Type=QtechEncryptAlgo
_QtechIPSecSaEncryptAlgo_Object=MibTableColumn
qtechIPSecSaEncryptAlgo=_QtechIPSecSaEncryptAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,5),_QtechIPSecSaEncryptAlgo_Type())
qtechIPSecSaEncryptAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecSaEncryptAlgo.setStatus(_A)
_QtechIPSecSaAuthAlgo_Type=QtechAuthAlgo
_QtechIPSecSaAuthAlgo_Object=MibTableColumn
qtechIPSecSaAuthAlgo=_QtechIPSecSaAuthAlgo_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,6),_QtechIPSecSaAuthAlgo_Type())
qtechIPSecSaAuthAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecSaAuthAlgo.setStatus(_A)
_QtechIPSecSaStatus_Type=QtechIPSecTunnelState
_QtechIPSecSaStatus_Object=MibTableColumn
qtechIPSecSaStatus=_QtechIPSecSaStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,3,1,7),_QtechIPSecSaStatus_Type())
qtechIPSecSaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecSaStatus.setStatus(_A)
_QtechIPSecTrafficTable_Object=MibTable
qtechIPSecTrafficTable=_QtechIPSecTrafficTable_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4))
if mibBuilder.loadTexts:qtechIPSecTrafficTable.setStatus(_A)
_QtechIPSecTrafficEntry_Object=MibTableRow
qtechIPSecTrafficEntry=_QtechIPSecTrafficEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1))
qtechIPSecTrafficEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechIPSecTrafficEntry.setStatus(_A)
_QtechIPSecTrafficLocalType_Type=QtechTrafficType
_QtechIPSecTrafficLocalType_Object=MibTableColumn
qtechIPSecTrafficLocalType=_QtechIPSecTrafficLocalType_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,1),_QtechIPSecTrafficLocalType_Type())
qtechIPSecTrafficLocalType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficLocalType.setStatus(_A)
_QtechIPSecTrafficLocalAddr1_Type=IpAddress
_QtechIPSecTrafficLocalAddr1_Object=MibTableColumn
qtechIPSecTrafficLocalAddr1=_QtechIPSecTrafficLocalAddr1_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,2),_QtechIPSecTrafficLocalAddr1_Type())
qtechIPSecTrafficLocalAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficLocalAddr1.setStatus(_A)
_QtechIPSecTrafficLocalAddr2_Type=IpAddress
_QtechIPSecTrafficLocalAddr2_Object=MibTableColumn
qtechIPSecTrafficLocalAddr2=_QtechIPSecTrafficLocalAddr2_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,3),_QtechIPSecTrafficLocalAddr2_Type())
qtechIPSecTrafficLocalAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficLocalAddr2.setStatus(_A)
_QtechIPSecTrafficLocalProtocol_Type=QtechTunnelProtocol
_QtechIPSecTrafficLocalProtocol_Object=MibTableColumn
qtechIPSecTrafficLocalProtocol=_QtechIPSecTrafficLocalProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,4),_QtechIPSecTrafficLocalProtocol_Type())
qtechIPSecTrafficLocalProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficLocalProtocol.setStatus(_A)
class _QtechIPSecTrafficLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechIPSecTrafficLocalPort_Type.__name__=_D
_QtechIPSecTrafficLocalPort_Object=MibTableColumn
qtechIPSecTrafficLocalPort=_QtechIPSecTrafficLocalPort_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,5),_QtechIPSecTrafficLocalPort_Type())
qtechIPSecTrafficLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficLocalPort.setStatus(_A)
_QtechIPSecTrafficLocalHostname_Type=DisplayString
_QtechIPSecTrafficLocalHostname_Object=MibTableColumn
qtechIPSecTrafficLocalHostname=_QtechIPSecTrafficLocalHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,6),_QtechIPSecTrafficLocalHostname_Type())
qtechIPSecTrafficLocalHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficLocalHostname.setStatus(_A)
_QtechIPSecTrafficRemoteType_Type=QtechTrafficType
_QtechIPSecTrafficRemoteType_Object=MibTableColumn
qtechIPSecTrafficRemoteType=_QtechIPSecTrafficRemoteType_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,7),_QtechIPSecTrafficRemoteType_Type())
qtechIPSecTrafficRemoteType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficRemoteType.setStatus(_A)
_QtechIPSecTrafficRemoteAddr1_Type=IpAddress
_QtechIPSecTrafficRemoteAddr1_Object=MibTableColumn
qtechIPSecTrafficRemoteAddr1=_QtechIPSecTrafficRemoteAddr1_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,8),_QtechIPSecTrafficRemoteAddr1_Type())
qtechIPSecTrafficRemoteAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficRemoteAddr1.setStatus(_A)
_QtechIPSecTrafficRemoteAddr2_Type=IpAddress
_QtechIPSecTrafficRemoteAddr2_Object=MibTableColumn
qtechIPSecTrafficRemoteAddr2=_QtechIPSecTrafficRemoteAddr2_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,9),_QtechIPSecTrafficRemoteAddr2_Type())
qtechIPSecTrafficRemoteAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficRemoteAddr2.setStatus(_A)
_QtechIPSecTrafficRemoteProtocol_Type=QtechTunnelProtocol
_QtechIPSecTrafficRemoteProtocol_Object=MibTableColumn
qtechIPSecTrafficRemoteProtocol=_QtechIPSecTrafficRemoteProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,10),_QtechIPSecTrafficRemoteProtocol_Type())
qtechIPSecTrafficRemoteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficRemoteProtocol.setStatus(_A)
class _QtechIPSecTrafficRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QtechIPSecTrafficRemotePort_Type.__name__=_D
_QtechIPSecTrafficRemotePort_Object=MibTableColumn
qtechIPSecTrafficRemotePort=_QtechIPSecTrafficRemotePort_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,11),_QtechIPSecTrafficRemotePort_Type())
qtechIPSecTrafficRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficRemotePort.setStatus(_A)
_QtechIPSecTrafficRemoteHostname_Type=DisplayString
_QtechIPSecTrafficRemoteHostname_Object=MibTableColumn
qtechIPSecTrafficRemoteHostname=_QtechIPSecTrafficRemoteHostname_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,4,1,12),_QtechIPSecTrafficRemoteHostname_Type())
qtechIPSecTrafficRemoteHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecTrafficRemoteHostname.setStatus(_A)
_QtechIPSecGlobalStats_ObjectIdentity=ObjectIdentity
qtechIPSecGlobalStats=_QtechIPSecGlobalStats_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,1,5))
_QtechIPSecGlobalActiveTunnels_Type=Gauge32
_QtechIPSecGlobalActiveTunnels_Object=MibScalar
qtechIPSecGlobalActiveTunnels=_QtechIPSecGlobalActiveTunnels_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,1),_QtechIPSecGlobalActiveTunnels_Type())
qtechIPSecGlobalActiveTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalActiveTunnels.setStatus(_A)
_QtechIPSecGlobalActiveSas_Type=Gauge32
_QtechIPSecGlobalActiveSas_Object=MibScalar
qtechIPSecGlobalActiveSas=_QtechIPSecGlobalActiveSas_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,2),_QtechIPSecGlobalActiveSas_Type())
qtechIPSecGlobalActiveSas.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalActiveSas.setStatus(_A)
_QtechIPSecGlobalInOctets_Type=Counter64
_QtechIPSecGlobalInOctets_Object=MibScalar
qtechIPSecGlobalInOctets=_QtechIPSecGlobalInOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,3),_QtechIPSecGlobalInOctets_Type())
qtechIPSecGlobalInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalInOctets.setStatus(_A)
_QtechIPSecGlobalInPkts_Type=Counter64
_QtechIPSecGlobalInPkts_Object=MibScalar
qtechIPSecGlobalInPkts=_QtechIPSecGlobalInPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,4),_QtechIPSecGlobalInPkts_Type())
qtechIPSecGlobalInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalInPkts.setStatus(_A)
_QtechIPSecGlobalInSpeed_Type=Counter64
_QtechIPSecGlobalInSpeed_Object=MibScalar
qtechIPSecGlobalInSpeed=_QtechIPSecGlobalInSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,5),_QtechIPSecGlobalInSpeed_Type())
qtechIPSecGlobalInSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalInSpeed.setStatus(_A)
_QtechIPSecGlobalInDrops_Type=Counter64
_QtechIPSecGlobalInDrops_Object=MibScalar
qtechIPSecGlobalInDrops=_QtechIPSecGlobalInDrops_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,6),_QtechIPSecGlobalInDrops_Type())
qtechIPSecGlobalInDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalInDrops.setStatus(_A)
_QtechIPSecGlobalOutOctets_Type=Counter64
_QtechIPSecGlobalOutOctets_Object=MibScalar
qtechIPSecGlobalOutOctets=_QtechIPSecGlobalOutOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,7),_QtechIPSecGlobalOutOctets_Type())
qtechIPSecGlobalOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalOutOctets.setStatus(_A)
_QtechIPSecGlobalOutPkts_Type=Counter64
_QtechIPSecGlobalOutPkts_Object=MibScalar
qtechIPSecGlobalOutPkts=_QtechIPSecGlobalOutPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,8),_QtechIPSecGlobalOutPkts_Type())
qtechIPSecGlobalOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalOutPkts.setStatus(_A)
_QtechIPSecGlobalOutSpeed_Type=Counter64
_QtechIPSecGlobalOutSpeed_Object=MibScalar
qtechIPSecGlobalOutSpeed=_QtechIPSecGlobalOutSpeed_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,9),_QtechIPSecGlobalOutSpeed_Type())
qtechIPSecGlobalOutSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalOutSpeed.setStatus(_A)
_QtechIPSecGlobalOutDrops_Type=Counter64
_QtechIPSecGlobalOutDrops_Object=MibScalar
qtechIPSecGlobalOutDrops=_QtechIPSecGlobalOutDrops_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,5,10),_QtechIPSecGlobalOutDrops_Type())
qtechIPSecGlobalOutDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPSecGlobalOutDrops.setStatus(_A)
_QtechIPSecTrapObject_ObjectIdentity=ObjectIdentity
qtechIPSecTrapObject=_QtechIPSecTrapObject_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,1,6))
_QtechIPSecMapName_Type=DisplayString
_QtechIPSecMapName_Object=MibScalar
qtechIPSecMapName=_QtechIPSecMapName_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,6,1),_QtechIPSecMapName_Type())
qtechIPSecMapName.setMaxAccess(_K)
if mibBuilder.loadTexts:qtechIPSecMapName.setStatus(_A)
_QtechIPSecSeqNum_Type=Integer32
_QtechIPSecSeqNum_Object=MibScalar
qtechIPSecSeqNum=_QtechIPSecSeqNum_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,6,2),_QtechIPSecSeqNum_Type())
qtechIPSecSeqNum.setMaxAccess(_K)
if mibBuilder.loadTexts:qtechIPSecSeqNum.setStatus(_A)
_QtechIPSecSpiValue_Type=Integer32
_QtechIPSecSpiValue_Object=MibScalar
qtechIPSecSpiValue=_QtechIPSecSpiValue_Object((1,3,6,1,4,1,27514,1,1,10,2,94,1,6,3),_QtechIPSecSpiValue_Type())
qtechIPSecSpiValue.setMaxAccess(_K)
if mibBuilder.loadTexts:qtechIPSecSpiValue.setStatus(_A)
_QtechIPSecTrap_ObjectIdentity=ObjectIdentity
qtechIPSecTrap=_QtechIPSecTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,1,7))
_QtechIPSecNotifications_ObjectIdentity=ObjectIdentity
qtechIPSecNotifications=_QtechIPSecNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,1,7,1))
_QtechIPSecConformance_ObjectIdentity=ObjectIdentity
qtechIPSecConformance=_QtechIPSecConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,2))
_QtechIPSecCompliances_ObjectIdentity=ObjectIdentity
qtechIPSecCompliances=_QtechIPSecCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,2,1))
_QtechIPSecGroups_ObjectIdentity=ObjectIdentity
qtechIPSecGroups=_QtechIPSecGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,94,2,2))
qtechIPSecTunnelTableGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,1))
qtechIPSecTunnelTableGroup.setObjects(*((_B,_R),(_B,_G),(_B,_E),(_B,_H),(_B,_I),(_B,_S),(_B,_T),(_B,_U),(_B,_L),(_B,_M),(_B,_V),(_B,_N),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:qtechIPSecTunnelTableGroup.setStatus(_A)
qtechIPSecTunnelStatGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,2))
qtechIPSecTunnelStatGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:qtechIPSecTunnelStatGroup.setStatus(_A)
qtechIPSecSaGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,3))
qtechIPSecSaGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qtechIPSecSaGroup.setStatus(_A)
qtechIPSecTrafficTableGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,4))
qtechIPSecTrafficTableGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:qtechIPSecTrafficTableGroup.setStatus(_A)
qtechIPSecGlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,5))
qtechIPSecGlobalStatsGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:qtechIPSecGlobalStatsGroup.setStatus(_A)
qtechIPSecTrapObjectGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,6))
qtechIPSecTrapObjectGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:qtechIPSecTrapObjectGroup.setStatus(_A)
qtechIPSecTunnelStart=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,94,1,7,1,1))
qtechIPSecTunnelStart.setObjects(*((_B,_G),(_B,_E),(_B,_H),(_B,_I),(_B,_M),(_B,_L)))
if mibBuilder.loadTexts:qtechIPSecTunnelStart.setStatus(_A)
qtechIPSecTunnelStop=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,94,1,7,1,2))
qtechIPSecTunnelStop.setObjects(*((_B,_G),(_B,_E),(_B,_H),(_B,_I),(_B,_N)))
if mibBuilder.loadTexts:qtechIPSecTunnelStop.setStatus(_A)
qtechIPSecTrapGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,94,2,2,7))
qtechIPSecTrapGroup.setObjects(*((_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:qtechIPSecTrapGroup.setStatus(_A)
qtechIPSecCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,94,2,1,1))
qtechIPSecCompliance.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:qtechIPSecCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QtechDiffHellmanGrp':QtechDiffHellmanGrp,'QtechEncapMode':QtechEncapMode,'QtechEncryptAlgo':QtechEncryptAlgo,'QtechAuthAlgo':QtechAuthAlgo,'QtechSaProtocol':QtechSaProtocol,'QtechTunnelProtocol':QtechTunnelProtocol,'QtechTrafficType':QtechTrafficType,'QtechIPSecNegoType':QtechIPSecNegoType,'QtechIPSecTunnelState':QtechIPSecTunnelState,'qtechIPSecMonitor':qtechIPSecMonitor,'qtechIPSecObjects':qtechIPSecObjects,'qtechIPSecTunnelTable':qtechIPSecTunnelTable,'qtechIPSecTunnelEntry':qtechIPSecTunnelEntry,'qtechIPSecTunIfIndex':qtechIPSecTunIfIndex,'qtechIPSecTunIndex':qtechIPSecTunIndex,_R:qtechIPSecTunIKETunnelIndex,_G:qtechIPSecTunLocalAddr,_E:qtechIPSecTunRemoteAddr,_H:qtechIPSecTunLocalHostname,_I:qtechIPSecTunRemoteHostname,_S:qtechIPSecTunKeyType,_T:qtechIPSecTunEncapMode,_U:qtechIPSecTunInitiator,_L:qtechIPSecTunLifeSize,_M:qtechIPSecTunLifeTime,_V:qtechIPSecTunRemainTime,_N:qtechIPSecTunActiveTime,'qtechIPSecTunCreateTime':qtechIPSecTunCreateTime,_W:qtechIPSecTunRemainSize,_X:qtechIPSecTunTotalRefreshes,_Y:qtechIPSecTunCurrentSaInstances,_Z:qtechIPSecTunInSaEncryptAlgo,_a:qtechIPSecTunInSaAhAuthAlgo,_b:qtechIPSecTunInSaEspAuthAlgo,_c:qtechIPSecTunDiffHellmanGrp,_d:qtechIPSecTunOutSaEncryptAlgo,_e:qtechIPSecTunOutSaAhAuthAlgo,_f:qtechIPSecTunOutSaEspAuthAlgo,'qtechIPSecTunMapName':qtechIPSecTunMapName,'qtechIPSecTunSeqNum':qtechIPSecTunSeqNum,_g:qtechIPSecTunStatus,'qtechIPSecTunnelStatTable':qtechIPSecTunnelStatTable,'qtechIPSecTunnelStatEntry':qtechIPSecTunnelStatEntry,_h:qtechIPSecTunInOctets,_i:qtechIPSecTunInDecompOctets,_j:qtechIPSecTunInPkts,_k:qtechIPSecTunInSpeed,_l:qtechIPSecTunInDropPkts,_m:qtechIPSecTunOutOctets,_n:qtechIPSecTunOutUncompOctets,_o:qtechIPSecTunOutPkts,_p:qtechIPSecTunOutSpeed,_q:qtechIPSecTunOutDropPkts,'qtechIPSecSaTable':qtechIPSecSaTable,'qtechIPSecSaEntry':qtechIPSecSaEntry,'qtechIPSecSaIndex':qtechIPSecSaIndex,_r:qtechIPSecSaDirection,_s:qtechIPSecSaValue,_t:qtechIPSecSaProtocol,_u:qtechIPSecSaEncryptAlgo,_v:qtechIPSecSaAuthAlgo,_w:qtechIPSecSaStatus,'qtechIPSecTrafficTable':qtechIPSecTrafficTable,'qtechIPSecTrafficEntry':qtechIPSecTrafficEntry,_x:qtechIPSecTrafficLocalType,_y:qtechIPSecTrafficLocalAddr1,_z:qtechIPSecTrafficLocalAddr2,_A0:qtechIPSecTrafficLocalProtocol,_A1:qtechIPSecTrafficLocalPort,_A2:qtechIPSecTrafficLocalHostname,_A3:qtechIPSecTrafficRemoteType,_A4:qtechIPSecTrafficRemoteAddr1,_A5:qtechIPSecTrafficRemoteAddr2,_A6:qtechIPSecTrafficRemoteProtocol,_A7:qtechIPSecTrafficRemotePort,_A8:qtechIPSecTrafficRemoteHostname,'qtechIPSecGlobalStats':qtechIPSecGlobalStats,_A9:qtechIPSecGlobalActiveTunnels,_AA:qtechIPSecGlobalActiveSas,_AB:qtechIPSecGlobalInOctets,_AC:qtechIPSecGlobalInPkts,_AE:qtechIPSecGlobalInSpeed,_AD:qtechIPSecGlobalInDrops,_AF:qtechIPSecGlobalOutOctets,_AG:qtechIPSecGlobalOutPkts,_AI:qtechIPSecGlobalOutSpeed,_AH:qtechIPSecGlobalOutDrops,'qtechIPSecTrapObject':qtechIPSecTrapObject,_AJ:qtechIPSecMapName,_AK:qtechIPSecSeqNum,_AL:qtechIPSecSpiValue,'qtechIPSecTrap':qtechIPSecTrap,'qtechIPSecNotifications':qtechIPSecNotifications,_AM:qtechIPSecTunnelStart,_AN:qtechIPSecTunnelStop,'qtechIPSecConformance':qtechIPSecConformance,'qtechIPSecCompliances':qtechIPSecCompliances,'qtechIPSecCompliance':qtechIPSecCompliance,'qtechIPSecGroups':qtechIPSecGroups,_AO:qtechIPSecTunnelTableGroup,_AP:qtechIPSecTunnelStatGroup,_AQ:qtechIPSecSaGroup,_AR:qtechIPSecTrafficTableGroup,_AS:qtechIPSecGlobalStatsGroup,_AT:qtechIPSecTrapObjectGroup,_AU:qtechIPSecTrapGroup})