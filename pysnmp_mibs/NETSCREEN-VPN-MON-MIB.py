_I='active'
_H='inactive'
_G='nsVpnMonIndex'
_F='NETSCREEN-VPN-MON-MIB'
_E='DisplayString'
_D='reserved'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVpn,netscreenVpnMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVpn','netscreenVpnMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
netscreenVpnMonMibModule=ModuleIdentity((1,3,6,1,4,1,3224,4,0,1))
if mibBuilder.loadTexts:netscreenVpnMonMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2000-08-27 00:00'))
_NetscreenVpnMon_ObjectIdentity=ObjectIdentity
netscreenVpnMon=_NetscreenVpnMon_ObjectIdentity((1,3,6,1,4,1,3224,4,1))
_NsVpnMonTable_Object=MibTable
nsVpnMonTable=_NsVpnMonTable_Object((1,3,6,1,4,1,3224,4,1,1))
if mibBuilder.loadTexts:nsVpnMonTable.setStatus(_A)
_NsVpnMonEntry_Object=MibTableRow
nsVpnMonEntry=_NsVpnMonEntry_Object((1,3,6,1,4,1,3224,4,1,1,1))
nsVpnMonEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nsVpnMonEntry.setStatus(_A)
class _NsVpnMonIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnMonIndex_Type.__name__=_C
_NsVpnMonIndex_Object=MibTableColumn
nsVpnMonIndex=_NsVpnMonIndex_Object((1,3,6,1,4,1,3224,4,1,1,1,1),_NsVpnMonIndex_Type())
nsVpnMonIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonIndex.setStatus(_A)
_NsVpnMonInPlyId_Type=Integer32
_NsVpnMonInPlyId_Object=MibTableColumn
nsVpnMonInPlyId=_NsVpnMonInPlyId_Object((1,3,6,1,4,1,3224,4,1,1,1,2),_NsVpnMonInPlyId_Type())
nsVpnMonInPlyId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonInPlyId.setStatus(_A)
_NsVpnMonOutPlyId_Type=Integer32
_NsVpnMonOutPlyId_Object=MibTableColumn
nsVpnMonOutPlyId=_NsVpnMonOutPlyId_Object((1,3,6,1,4,1,3224,4,1,1,1,3),_NsVpnMonOutPlyId_Type())
nsVpnMonOutPlyId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonOutPlyId.setStatus(_A)
class _NsVpnMonVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnMonVpnName_Type.__name__=_E
_NsVpnMonVpnName_Object=MibTableColumn
nsVpnMonVpnName=_NsVpnMonVpnName_Object((1,3,6,1,4,1,3224,4,1,1,1,4),_NsVpnMonVpnName_Type())
nsVpnMonVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonVpnName.setStatus(_A)
class _NsVpnMonVsysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVpnMonVsysName_Type.__name__=_E
_NsVpnMonVsysName_Object=MibTableColumn
nsVpnMonVsysName=_NsVpnMonVsysName_Object((1,3,6,1,4,1,3224,4,1,1,1,5),_NsVpnMonVsysName_Type())
nsVpnMonVsysName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonVsysName.setStatus(_A)
class _NsVpnMonTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('proto-isakmp',1),('proto-ipsec-ah',2),('proto-ipsec-esp',3),('proto-ipcomp',4)))
_NsVpnMonTunnelType_Type.__name__=_C
_NsVpnMonTunnelType_Object=MibTableColumn
nsVpnMonTunnelType=_NsVpnMonTunnelType_Object((1,3,6,1,4,1,3224,4,1,1,1,6),_NsVpnMonTunnelType_Type())
nsVpnMonTunnelType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonTunnelType.setStatus(_A)
class _NsVpnMonEspEncAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,20,21)));namedValues=NamedValues(*((_D,0),('esp-des-iv64',1),('esp-des',2),('esp-3des',3),('esp-rc5',4),('esp-idea',5),('esp-cast',6),('esp-blowfish',7),('esp-3idea',8),('esp-des-iv32',9),('esp-rc4',10),('esp-null',11),('esp-aes',12),('esp-aes192',20),('esp-aes256',21)))
_NsVpnMonEspEncAlg_Type.__name__=_C
_NsVpnMonEspEncAlg_Object=MibTableColumn
nsVpnMonEspEncAlg=_NsVpnMonEspEncAlg_Object((1,3,6,1,4,1,3224,4,1,1,1,7),_NsVpnMonEspEncAlg_Type())
nsVpnMonEspEncAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonEspEncAlg.setStatus(_A)
class _NsVpnMonEspAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('hmac-md5',1),('hmac-sha',2),('des-mac',3),('ipdk',4)))
_NsVpnMonEspAuthAlg_Type.__name__=_C
_NsVpnMonEspAuthAlg_Object=MibTableColumn
nsVpnMonEspAuthAlg=_NsVpnMonEspAuthAlg_Object((1,3,6,1,4,1,3224,4,1,1,1,8),_NsVpnMonEspAuthAlg_Type())
nsVpnMonEspAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonEspAuthAlg.setStatus(_A)
class _NsVpnMonAhAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*((_D,0),('ah-md5',2),('ah-sha',3),('ah-des',4)))
_NsVpnMonAhAlg_Type.__name__=_C
_NsVpnMonAhAlg_Object=MibTableColumn
nsVpnMonAhAlg=_NsVpnMonAhAlg_Object((1,3,6,1,4,1,3224,4,1,1,1,9),_NsVpnMonAhAlg_Type())
nsVpnMonAhAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonAhAlg.setStatus(_A)
class _NsVpnMonKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('manual',0),('auto-ike',1)))
_NsVpnMonKeyType_Type.__name__=_C
_NsVpnMonKeyType_Object=MibTableColumn
nsVpnMonKeyType=_NsVpnMonKeyType_Object((1,3,6,1,4,1,3224,4,1,1,1,10),_NsVpnMonKeyType_Type())
nsVpnMonKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonKeyType.setStatus(_A)
class _NsVpnMonP1Auth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unused',0),('preshared-key',1),('dss-Signature',2),('rsa-Signature',3),('rsa-Encryption1',4),('rsa-Encryption2',5)))
_NsVpnMonP1Auth_Type.__name__=_C
_NsVpnMonP1Auth_Object=MibTableColumn
nsVpnMonP1Auth=_NsVpnMonP1Auth_Object((1,3,6,1,4,1,3224,4,1,1,1,11),_NsVpnMonP1Auth_Type())
nsVpnMonP1Auth.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonP1Auth.setStatus(_A)
class _NsVpnMonVpnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('dialup',1),('site-to-site',2)))
_NsVpnMonVpnType_Type.__name__=_C
_NsVpnMonVpnType_Object=MibTableColumn
nsVpnMonVpnType=_NsVpnMonVpnType_Object((1,3,6,1,4,1,3224,4,1,1,1,12),_NsVpnMonVpnType_Type())
nsVpnMonVpnType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonVpnType.setStatus(_A)
_NsVpnMonRmtGwIp_Type=IpAddress
_NsVpnMonRmtGwIp_Object=MibTableColumn
nsVpnMonRmtGwIp=_NsVpnMonRmtGwIp_Object((1,3,6,1,4,1,3224,4,1,1,1,13),_NsVpnMonRmtGwIp_Type())
nsVpnMonRmtGwIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonRmtGwIp.setStatus(_A)
_NsVpnMonRmtGwId_Type=DisplayString
_NsVpnMonRmtGwId_Object=MibTableColumn
nsVpnMonRmtGwId=_NsVpnMonRmtGwId_Object((1,3,6,1,4,1,3224,4,1,1,1,14),_NsVpnMonRmtGwId_Type())
nsVpnMonRmtGwId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonRmtGwId.setStatus(_A)
_NsVpnMonMyGwIp_Type=IpAddress
_NsVpnMonMyGwIp_Object=MibTableColumn
nsVpnMonMyGwIp=_NsVpnMonMyGwIp_Object((1,3,6,1,4,1,3224,4,1,1,1,15),_NsVpnMonMyGwIp_Type())
nsVpnMonMyGwIp.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonMyGwIp.setStatus(_A)
_NsVpnMonMyGwId_Type=DisplayString
_NsVpnMonMyGwId_Object=MibTableColumn
nsVpnMonMyGwId=_NsVpnMonMyGwId_Object((1,3,6,1,4,1,3224,4,1,1,1,16),_NsVpnMonMyGwId_Type())
nsVpnMonMyGwId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonMyGwId.setStatus(_A)
_NsVpnMonOutSpi_Type=Integer32
_NsVpnMonOutSpi_Object=MibTableColumn
nsVpnMonOutSpi=_NsVpnMonOutSpi_Object((1,3,6,1,4,1,3224,4,1,1,1,17),_NsVpnMonOutSpi_Type())
nsVpnMonOutSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonOutSpi.setStatus(_A)
_NsVpnMonInSpi_Type=Integer32
_NsVpnMonInSpi_Object=MibTableColumn
nsVpnMonInSpi=_NsVpnMonInSpi_Object((1,3,6,1,4,1,3224,4,1,1,1,18),_NsVpnMonInSpi_Type())
nsVpnMonInSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonInSpi.setStatus(_A)
class _NsVpnMonMonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NsVpnMonMonState_Type.__name__=_C
_NsVpnMonMonState_Object=MibTableColumn
nsVpnMonMonState=_NsVpnMonMonState_Object((1,3,6,1,4,1,3224,4,1,1,1,19),_NsVpnMonMonState_Type())
nsVpnMonMonState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonMonState.setStatus(_A)
class _NsVpnMonTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_NsVpnMonTunnelState_Type.__name__=_C
_NsVpnMonTunnelState_Object=MibTableColumn
nsVpnMonTunnelState=_NsVpnMonTunnelState_Object((1,3,6,1,4,1,3224,4,1,1,1,20),_NsVpnMonTunnelState_Type())
nsVpnMonTunnelState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonTunnelState.setStatus(_A)
class _NsVpnMonP1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsVpnMonP1State_Type.__name__=_C
_NsVpnMonP1State_Object=MibTableColumn
nsVpnMonP1State=_NsVpnMonP1State_Object((1,3,6,1,4,1,3224,4,1,1,1,21),_NsVpnMonP1State_Type())
nsVpnMonP1State.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonP1State.setStatus(_A)
_NsVpnMonP1LifeTime_Type=Integer32
_NsVpnMonP1LifeTime_Object=MibTableColumn
nsVpnMonP1LifeTime=_NsVpnMonP1LifeTime_Object((1,3,6,1,4,1,3224,4,1,1,1,22),_NsVpnMonP1LifeTime_Type())
nsVpnMonP1LifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonP1LifeTime.setStatus(_A)
class _NsVpnMonP2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_NsVpnMonP2State_Type.__name__=_C
_NsVpnMonP2State_Object=MibTableColumn
nsVpnMonP2State=_NsVpnMonP2State_Object((1,3,6,1,4,1,3224,4,1,1,1,23),_NsVpnMonP2State_Type())
nsVpnMonP2State.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonP2State.setStatus(_A)
_NsVpnMonP2LifeTime_Type=Integer32
_NsVpnMonP2LifeTime_Object=MibTableColumn
nsVpnMonP2LifeTime=_NsVpnMonP2LifeTime_Object((1,3,6,1,4,1,3224,4,1,1,1,24),_NsVpnMonP2LifeTime_Type())
nsVpnMonP2LifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonP2LifeTime.setStatus(_A)
_NsVpnMonP2LifeBytes_Type=Integer32
_NsVpnMonP2LifeBytes_Object=MibTableColumn
nsVpnMonP2LifeBytes=_NsVpnMonP2LifeBytes_Object((1,3,6,1,4,1,3224,4,1,1,1,25),_NsVpnMonP2LifeBytes_Type())
nsVpnMonP2LifeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonP2LifeBytes.setStatus(_A)
_NsVpnMonDelayAvg_Type=Integer32
_NsVpnMonDelayAvg_Object=MibTableColumn
nsVpnMonDelayAvg=_NsVpnMonDelayAvg_Object((1,3,6,1,4,1,3224,4,1,1,1,26),_NsVpnMonDelayAvg_Type())
nsVpnMonDelayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonDelayAvg.setStatus(_A)
_NsVpnMonDelayLast_Type=Integer32
_NsVpnMonDelayLast_Object=MibTableColumn
nsVpnMonDelayLast=_NsVpnMonDelayLast_Object((1,3,6,1,4,1,3224,4,1,1,1,27),_NsVpnMonDelayLast_Type())
nsVpnMonDelayLast.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonDelayLast.setStatus(_A)
_NsVpnMonAvail_Type=Integer32
_NsVpnMonAvail_Object=MibTableColumn
nsVpnMonAvail=_NsVpnMonAvail_Object((1,3,6,1,4,1,3224,4,1,1,1,28),_NsVpnMonAvail_Type())
nsVpnMonAvail.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonAvail.setStatus(_A)
_NsVpnMonSaId_Type=Integer32
_NsVpnMonSaId_Object=MibTableColumn
nsVpnMonSaId=_NsVpnMonSaId_Object((1,3,6,1,4,1,3224,4,1,1,1,29),_NsVpnMonSaId_Type())
nsVpnMonSaId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonSaId.setStatus(_A)
_NsVpnMonGroupId_Type=Integer32
_NsVpnMonGroupId_Object=MibTableColumn
nsVpnMonGroupId=_NsVpnMonGroupId_Object((1,3,6,1,4,1,3224,4,1,1,1,30),_NsVpnMonGroupId_Type())
nsVpnMonGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonGroupId.setStatus(_A)
_NsVpnMonUsrId_Type=Integer32
_NsVpnMonUsrId_Object=MibTableColumn
nsVpnMonUsrId=_NsVpnMonUsrId_Object((1,3,6,1,4,1,3224,4,1,1,1,31),_NsVpnMonUsrId_Type())
nsVpnMonUsrId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonUsrId.setStatus(_A)
_NsVpnMonStartSessRequestTime_Type=TimeTicks
_NsVpnMonStartSessRequestTime_Object=MibTableColumn
nsVpnMonStartSessRequestTime=_NsVpnMonStartSessRequestTime_Object((1,3,6,1,4,1,3224,4,1,1,1,32),_NsVpnMonStartSessRequestTime_Type())
nsVpnMonStartSessRequestTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonStartSessRequestTime.setStatus(_A)
_NsVpnMonStartSessEstTime_Type=TimeTicks
_NsVpnMonStartSessEstTime_Object=MibTableColumn
nsVpnMonStartSessEstTime=_NsVpnMonStartSessEstTime_Object((1,3,6,1,4,1,3224,4,1,1,1,33),_NsVpnMonStartSessEstTime_Type())
nsVpnMonStartSessEstTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonStartSessEstTime.setStatus(_A)
_NsVpnMonEndSessTime_Type=TimeTicks
_NsVpnMonEndSessTime_Object=MibTableColumn
nsVpnMonEndSessTime=_NsVpnMonEndSessTime_Object((1,3,6,1,4,1,3224,4,1,1,1,34),_NsVpnMonEndSessTime_Type())
nsVpnMonEndSessTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonEndSessTime.setStatus(_A)
_NsVpnMonBytesIn_Type=Counter32
_NsVpnMonBytesIn_Object=MibTableColumn
nsVpnMonBytesIn=_NsVpnMonBytesIn_Object((1,3,6,1,4,1,3224,4,1,1,1,35),_NsVpnMonBytesIn_Type())
nsVpnMonBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonBytesIn.setStatus(_A)
_NsVpnMonBytesOut_Type=Counter32
_NsVpnMonBytesOut_Object=MibTableColumn
nsVpnMonBytesOut=_NsVpnMonBytesOut_Object((1,3,6,1,4,1,3224,4,1,1,1,36),_NsVpnMonBytesOut_Type())
nsVpnMonBytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonBytesOut.setStatus(_A)
_NsVpnMonPacketsIn_Type=Counter32
_NsVpnMonPacketsIn_Object=MibTableColumn
nsVpnMonPacketsIn=_NsVpnMonPacketsIn_Object((1,3,6,1,4,1,3224,4,1,1,1,37),_NsVpnMonPacketsIn_Type())
nsVpnMonPacketsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonPacketsIn.setStatus(_A)
_NsVpnMonPacketsOut_Type=Counter32
_NsVpnMonPacketsOut_Object=MibTableColumn
nsVpnMonPacketsOut=_NsVpnMonPacketsOut_Object((1,3,6,1,4,1,3224,4,1,1,1,38),_NsVpnMonPacketsOut_Type())
nsVpnMonPacketsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonPacketsOut.setStatus(_A)
_NsVpnMonIfIndex_Type=Integer32
_NsVpnMonIfIndex_Object=MibTableColumn
nsVpnMonIfIndex=_NsVpnMonIfIndex_Object((1,3,6,1,4,1,3224,4,1,1,1,39),_NsVpnMonIfIndex_Type())
nsVpnMonIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonIfIndex.setStatus(_A)
_NsVpnMonUpdateTime_Type=TimeTicks
_NsVpnMonUpdateTime_Object=MibTableColumn
nsVpnMonUpdateTime=_NsVpnMonUpdateTime_Object((1,3,6,1,4,1,3224,4,1,1,1,40),_NsVpnMonUpdateTime_Type())
nsVpnMonUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonUpdateTime.setStatus(_A)
class _NsVpnMonDN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NsVpnMonDN_Type.__name__=_E
_NsVpnMonDN_Object=MibTableColumn
nsVpnMonDN=_NsVpnMonDN_Object((1,3,6,1,4,1,3224,4,1,1,1,41),_NsVpnMonDN_Type())
nsVpnMonDN.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonDN.setStatus(_A)
class _NsVpnMonIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVpnMonIfInfo_Type.__name__=_C
_NsVpnMonIfInfo_Object=MibTableColumn
nsVpnMonIfInfo=_NsVpnMonIfInfo_Object((1,3,6,1,4,1,3224,4,1,1,1,42),_NsVpnMonIfInfo_Type())
nsVpnMonIfInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVpnMonIfInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'netscreenVpnMonMibModule':netscreenVpnMonMibModule,'netscreenVpnMon':netscreenVpnMon,'nsVpnMonTable':nsVpnMonTable,'nsVpnMonEntry':nsVpnMonEntry,_G:nsVpnMonIndex,'nsVpnMonInPlyId':nsVpnMonInPlyId,'nsVpnMonOutPlyId':nsVpnMonOutPlyId,'nsVpnMonVpnName':nsVpnMonVpnName,'nsVpnMonVsysName':nsVpnMonVsysName,'nsVpnMonTunnelType':nsVpnMonTunnelType,'nsVpnMonEspEncAlg':nsVpnMonEspEncAlg,'nsVpnMonEspAuthAlg':nsVpnMonEspAuthAlg,'nsVpnMonAhAlg':nsVpnMonAhAlg,'nsVpnMonKeyType':nsVpnMonKeyType,'nsVpnMonP1Auth':nsVpnMonP1Auth,'nsVpnMonVpnType':nsVpnMonVpnType,'nsVpnMonRmtGwIp':nsVpnMonRmtGwIp,'nsVpnMonRmtGwId':nsVpnMonRmtGwId,'nsVpnMonMyGwIp':nsVpnMonMyGwIp,'nsVpnMonMyGwId':nsVpnMonMyGwId,'nsVpnMonOutSpi':nsVpnMonOutSpi,'nsVpnMonInSpi':nsVpnMonInSpi,'nsVpnMonMonState':nsVpnMonMonState,'nsVpnMonTunnelState':nsVpnMonTunnelState,'nsVpnMonP1State':nsVpnMonP1State,'nsVpnMonP1LifeTime':nsVpnMonP1LifeTime,'nsVpnMonP2State':nsVpnMonP2State,'nsVpnMonP2LifeTime':nsVpnMonP2LifeTime,'nsVpnMonP2LifeBytes':nsVpnMonP2LifeBytes,'nsVpnMonDelayAvg':nsVpnMonDelayAvg,'nsVpnMonDelayLast':nsVpnMonDelayLast,'nsVpnMonAvail':nsVpnMonAvail,'nsVpnMonSaId':nsVpnMonSaId,'nsVpnMonGroupId':nsVpnMonGroupId,'nsVpnMonUsrId':nsVpnMonUsrId,'nsVpnMonStartSessRequestTime':nsVpnMonStartSessRequestTime,'nsVpnMonStartSessEstTime':nsVpnMonStartSessEstTime,'nsVpnMonEndSessTime':nsVpnMonEndSessTime,'nsVpnMonBytesIn':nsVpnMonBytesIn,'nsVpnMonBytesOut':nsVpnMonBytesOut,'nsVpnMonPacketsIn':nsVpnMonPacketsIn,'nsVpnMonPacketsOut':nsVpnMonPacketsOut,'nsVpnMonIfIndex':nsVpnMonIfIndex,'nsVpnMonUpdateTime':nsVpnMonUpdateTime,'nsVpnMonDN':nsVpnMonDN,'nsVpnMonIfInfo':nsVpnMonIfInfo})