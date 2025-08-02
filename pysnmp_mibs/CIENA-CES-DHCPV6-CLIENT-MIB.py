_f='cienaCesDhcpv6LdraVsSubVlan'
_e='cienaCesDhcpv6LdraRidStringPort'
_d='cienaCesDhcpv6LdraIntidStringPort'
_c='cienaCesDhcpv6ClientSessStatsMgmtIntfIndex'
_b='unknown'
_a='cienaCesDhcpv6ClientSessMgmtIntfIndex'
_Z='cienaCesDhcpv6OptionCodeIndex'
_Y='inactive'
_X='active'
_W='cienaCesDhcpv6LdraPort'
_V='deprecated'
_U='cienaCesDhcpv6LdraMplsInterface'
_T='cienaCesDhcpv6LdraVsPort'
_S='cienaCesDhcpv6LdraVsVlan'
_R='unTrust'
_Q='dualRoleTrust'
_P='serverTrust'
_O='clientTrust'
_N='client'
_M='Unsigned32'
_L='cienaCesDhcpv6LdraMplsId'
_K='seconds'
_J='CienaStatsClear'
_I='cienaCesDhcpv6LdraVlan'
_H='DisplayString'
_G='read-write'
_F='not-accessible'
_E='read-create'
_D='Integer32'
_C='CIENA-CES-DHCPV6-CLIENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
CienaGlobalState,CienaStatsClear=mibBuilder.importSymbols('CIENA-TC','CienaGlobalState',_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
cienaCesDhcpv6ClientMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,30))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientMIB.setRevisions(('2017-09-12 00:00','2016-06-21 00:00','2016-01-19 00:00','2015-11-02 00:00','2015-08-06 00:00','2013-10-17 00:00','2013-09-24 00:00','2013-07-19 00:00','2013-02-11 19:00','2013-02-11 00:00','2013-02-08 00:00','2012-11-15 00:00'))
_CienaCesDhcpv6ClientMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6ClientMIBObjects=_CienaCesDhcpv6ClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,1))
_CienaCesDhcpv6Client_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6Client=_CienaCesDhcpv6Client_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,1,1))
_CienaCesDhcpv6AdminState_Type=CienaGlobalState
_CienaCesDhcpv6AdminState_Object=MibScalar
cienaCesDhcpv6AdminState=_CienaCesDhcpv6AdminState_Object((1,3,6,1,4,1,1271,2,1,30,1,1,1),_CienaCesDhcpv6AdminState_Type())
cienaCesDhcpv6AdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6AdminState.setStatus(_A)
class _CienaCesDhcpv6IfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CienaCesDhcpv6IfName_Type.__name__=_H
_CienaCesDhcpv6IfName_Object=MibScalar
cienaCesDhcpv6IfName=_CienaCesDhcpv6IfName_Object((1,3,6,1,4,1,1271,2,1,30,1,1,2),_CienaCesDhcpv6IfName_Type())
cienaCesDhcpv6IfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6IfName.setStatus(_A)
_CienaCesDhcpv6RapidCommitState_Type=CienaGlobalState
_CienaCesDhcpv6RapidCommitState_Object=MibScalar
cienaCesDhcpv6RapidCommitState=_CienaCesDhcpv6RapidCommitState_Object((1,3,6,1,4,1,1271,2,1,30,1,1,3),_CienaCesDhcpv6RapidCommitState_Type())
cienaCesDhcpv6RapidCommitState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6RapidCommitState.setStatus(_A)
class _CienaCesDhcpv6PrefLifetimeReq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CienaCesDhcpv6PrefLifetimeReq_Type.__name__=_D
_CienaCesDhcpv6PrefLifetimeReq_Object=MibScalar
cienaCesDhcpv6PrefLifetimeReq=_CienaCesDhcpv6PrefLifetimeReq_Object((1,3,6,1,4,1,1271,2,1,30,1,1,5),_CienaCesDhcpv6PrefLifetimeReq_Type())
cienaCesDhcpv6PrefLifetimeReq.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6PrefLifetimeReq.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDhcpv6PrefLifetimeReq.setUnits(_K)
class _CienaCesDhcpv6ValidLifetimeReq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CienaCesDhcpv6ValidLifetimeReq_Type.__name__=_D
_CienaCesDhcpv6ValidLifetimeReq_Object=MibScalar
cienaCesDhcpv6ValidLifetimeReq=_CienaCesDhcpv6ValidLifetimeReq_Object((1,3,6,1,4,1,1271,2,1,30,1,1,6),_CienaCesDhcpv6ValidLifetimeReq_Type())
cienaCesDhcpv6ValidLifetimeReq.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ValidLifetimeReq.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDhcpv6ValidLifetimeReq.setUnits(_K)
_CienaCesDhcpv6ClientOptionTable_Object=MibTable
cienaCesDhcpv6ClientOptionTable=_CienaCesDhcpv6ClientOptionTable_Object((1,3,6,1,4,1,1271,2,1,30,1,1,7))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientOptionTable.setStatus(_A)
_CienaCesDhcpv6ClientOptionEntry_Object=MibTableRow
cienaCesDhcpv6ClientOptionEntry=_CienaCesDhcpv6ClientOptionEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,1,7,1))
cienaCesDhcpv6ClientOptionEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientOptionEntry.setStatus(_A)
class _CienaCesDhcpv6OptionCodeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6OptionCodeIndex_Type.__name__=_D
_CienaCesDhcpv6OptionCodeIndex_Object=MibTableColumn
cienaCesDhcpv6OptionCodeIndex=_CienaCesDhcpv6OptionCodeIndex_Object((1,3,6,1,4,1,1271,2,1,30,1,1,7,1,1),_CienaCesDhcpv6OptionCodeIndex_Type())
cienaCesDhcpv6OptionCodeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6OptionCodeIndex.setStatus(_A)
_CienaCesDhcpv6OptionDesc_Type=DisplayString
_CienaCesDhcpv6OptionDesc_Object=MibTableColumn
cienaCesDhcpv6OptionDesc=_CienaCesDhcpv6OptionDesc_Object((1,3,6,1,4,1,1271,2,1,30,1,1,7,1,2),_CienaCesDhcpv6OptionDesc_Type())
cienaCesDhcpv6OptionDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6OptionDesc.setStatus(_A)
class _CienaCesDhcpv6OptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CienaCesDhcpv6OptionCode_Type.__name__=_D
_CienaCesDhcpv6OptionCode_Object=MibTableColumn
cienaCesDhcpv6OptionCode=_CienaCesDhcpv6OptionCode_Object((1,3,6,1,4,1,1271,2,1,30,1,1,7,1,3),_CienaCesDhcpv6OptionCode_Type())
cienaCesDhcpv6OptionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6OptionCode.setStatus(_A)
_CienaCesDhcpv6OptionState_Type=CienaGlobalState
_CienaCesDhcpv6OptionState_Object=MibTableColumn
cienaCesDhcpv6OptionState=_CienaCesDhcpv6OptionState_Object((1,3,6,1,4,1,1271,2,1,30,1,1,7,1,4),_CienaCesDhcpv6OptionState_Type())
cienaCesDhcpv6OptionState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6OptionState.setStatus(_A)
_CienaCesDhcpv6ClientSessTable_Object=MibTable
cienaCesDhcpv6ClientSessTable=_CienaCesDhcpv6ClientSessTable_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessTable.setStatus(_A)
_CienaCesDhcpv6ClientSessEntry_Object=MibTableRow
cienaCesDhcpv6ClientSessEntry=_CienaCesDhcpv6ClientSessEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1))
cienaCesDhcpv6ClientSessEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessEntry.setStatus(_A)
class _CienaCesDhcpv6ClientSessMgmtIntfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6ClientSessMgmtIntfIndex_Type.__name__=_D
_CienaCesDhcpv6ClientSessMgmtIntfIndex_Object=MibTableColumn
cienaCesDhcpv6ClientSessMgmtIntfIndex=_CienaCesDhcpv6ClientSessMgmtIntfIndex_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,1),_CienaCesDhcpv6ClientSessMgmtIntfIndex_Type())
cienaCesDhcpv6ClientSessMgmtIntfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessMgmtIntfIndex.setStatus(_A)
class _CienaCesDhcpv6ClientSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,99)));namedValues=NamedValues(*(('disabled',1),('init',2),('bound',3),('renewing',4),('rebinding',5),('solicit',6),('request',7),('reconfigure',8),(_b,99)))
_CienaCesDhcpv6ClientSessState_Type.__name__=_D
_CienaCesDhcpv6ClientSessState_Object=MibTableColumn
cienaCesDhcpv6ClientSessState=_CienaCesDhcpv6ClientSessState_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,2),_CienaCesDhcpv6ClientSessState_Type())
cienaCesDhcpv6ClientSessState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessState.setStatus(_A)
class _CienaCesDhcpv6ClientSessAutoConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('none',1),('stateless',2),('stateful',3),(_b,99)))
_CienaCesDhcpv6ClientSessAutoConfigState_Type.__name__=_D
_CienaCesDhcpv6ClientSessAutoConfigState_Object=MibTableColumn
cienaCesDhcpv6ClientSessAutoConfigState=_CienaCesDhcpv6ClientSessAutoConfigState_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,3),_CienaCesDhcpv6ClientSessAutoConfigState_Type())
cienaCesDhcpv6ClientSessAutoConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessAutoConfigState.setStatus(_A)
_CienaCesDhcpv6ClientSessUpTime_Type=Integer32
_CienaCesDhcpv6ClientSessUpTime_Object=MibTableColumn
cienaCesDhcpv6ClientSessUpTime=_CienaCesDhcpv6ClientSessUpTime_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,4),_CienaCesDhcpv6ClientSessUpTime_Type())
cienaCesDhcpv6ClientSessUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessUpTime.setStatus(_A)
_CienaCesDhcpv6ClientSessPrefLifetime_Type=Integer32
_CienaCesDhcpv6ClientSessPrefLifetime_Object=MibTableColumn
cienaCesDhcpv6ClientSessPrefLifetime=_CienaCesDhcpv6ClientSessPrefLifetime_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,5),_CienaCesDhcpv6ClientSessPrefLifetime_Type())
cienaCesDhcpv6ClientSessPrefLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessPrefLifetime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessPrefLifetime.setUnits(_K)
_CienaCesDhcpv6ClientSessValidLifetime_Type=Integer32
_CienaCesDhcpv6ClientSessValidLifetime_Object=MibTableColumn
cienaCesDhcpv6ClientSessValidLifetime=_CienaCesDhcpv6ClientSessValidLifetime_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,6),_CienaCesDhcpv6ClientSessValidLifetime_Type())
cienaCesDhcpv6ClientSessValidLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessValidLifetime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessValidLifetime.setUnits(_K)
_CienaCesDhcpv6ClientSessLeaseExpire_Type=Integer32
_CienaCesDhcpv6ClientSessLeaseExpire_Object=MibTableColumn
cienaCesDhcpv6ClientSessLeaseExpire=_CienaCesDhcpv6ClientSessLeaseExpire_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,7),_CienaCesDhcpv6ClientSessLeaseExpire_Type())
cienaCesDhcpv6ClientSessLeaseExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessLeaseExpire.setStatus(_A)
_CienaCesDhcpv6ClientSessClientId_Type=DisplayString
_CienaCesDhcpv6ClientSessClientId_Object=MibTableColumn
cienaCesDhcpv6ClientSessClientId=_CienaCesDhcpv6ClientSessClientId_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,8),_CienaCesDhcpv6ClientSessClientId_Type())
cienaCesDhcpv6ClientSessClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessClientId.setStatus(_A)
_CienaCesDhcpv6ClientSessServerIpAddrType_Type=InetAddressType
_CienaCesDhcpv6ClientSessServerIpAddrType_Object=MibTableColumn
cienaCesDhcpv6ClientSessServerIpAddrType=_CienaCesDhcpv6ClientSessServerIpAddrType_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,9),_CienaCesDhcpv6ClientSessServerIpAddrType_Type())
cienaCesDhcpv6ClientSessServerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessServerIpAddrType.setStatus(_A)
_CienaCesDhcpv6ClientSessServerIpAddr_Type=InetAddress
_CienaCesDhcpv6ClientSessServerIpAddr_Object=MibTableColumn
cienaCesDhcpv6ClientSessServerIpAddr=_CienaCesDhcpv6ClientSessServerIpAddr_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,10),_CienaCesDhcpv6ClientSessServerIpAddr_Type())
cienaCesDhcpv6ClientSessServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessServerIpAddr.setStatus(_A)
_CienaCesDhcpv6ClientSessServerId_Type=DisplayString
_CienaCesDhcpv6ClientSessServerId_Object=MibTableColumn
cienaCesDhcpv6ClientSessServerId=_CienaCesDhcpv6ClientSessServerId_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,11),_CienaCesDhcpv6ClientSessServerId_Type())
cienaCesDhcpv6ClientSessServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessServerId.setStatus(_A)
_CienaCesDhcpv6ClientSessT1Time_Type=Integer32
_CienaCesDhcpv6ClientSessT1Time_Object=MibTableColumn
cienaCesDhcpv6ClientSessT1Time=_CienaCesDhcpv6ClientSessT1Time_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,12),_CienaCesDhcpv6ClientSessT1Time_Type())
cienaCesDhcpv6ClientSessT1Time.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessT1Time.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessT1Time.setUnits(_K)
_CienaCesDhcpv6ClientSessT2Time_Type=Integer32
_CienaCesDhcpv6ClientSessT2Time_Object=MibTableColumn
cienaCesDhcpv6ClientSessT2Time=_CienaCesDhcpv6ClientSessT2Time_Object((1,3,6,1,4,1,1271,2,1,30,1,1,8,1,13),_CienaCesDhcpv6ClientSessT2Time_Type())
cienaCesDhcpv6ClientSessT2Time.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessT2Time.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessT2Time.setUnits(_K)
_CienaCesDhcpv6ClientSessStatsTable_Object=MibTable
cienaCesDhcpv6ClientSessStatsTable=_CienaCesDhcpv6ClientSessStatsTable_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsTable.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsEntry_Object=MibTableRow
cienaCesDhcpv6ClientSessStatsEntry=_CienaCesDhcpv6ClientSessStatsEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1))
cienaCesDhcpv6ClientSessStatsEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsEntry.setStatus(_A)
class _CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Type.__name__=_D
_CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsMgmtIntfIndex=_CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,1),_CienaCesDhcpv6ClientSessStatsMgmtIntfIndex_Type())
cienaCesDhcpv6ClientSessStatsMgmtIntfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsMgmtIntfIndex.setStatus(_A)
class _CienaCesDhcpv6ClientSessStatsClear_Type(CienaStatsClear):defaultValue=0
_CienaCesDhcpv6ClientSessStatsClear_Type.__name__=_J
_CienaCesDhcpv6ClientSessStatsClear_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsClear=_CienaCesDhcpv6ClientSessStatsClear_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,2),_CienaCesDhcpv6ClientSessStatsClear_Type())
cienaCesDhcpv6ClientSessStatsClear.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsClear.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsPktsRx_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsPktsRx_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsPktsRx=_CienaCesDhcpv6ClientSessStatsPktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,3),_CienaCesDhcpv6ClientSessStatsPktsRx_Type())
cienaCesDhcpv6ClientSessStatsPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsPktsRx.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsReply_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsReply_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsReply=_CienaCesDhcpv6ClientSessStatsReply_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,4),_CienaCesDhcpv6ClientSessStatsReply_Type())
cienaCesDhcpv6ClientSessStatsReply.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsReply.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsAdvert_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsAdvert_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsAdvert=_CienaCesDhcpv6ClientSessStatsAdvert_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,5),_CienaCesDhcpv6ClientSessStatsAdvert_Type())
cienaCesDhcpv6ClientSessStatsAdvert.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsAdvert.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsRecfg_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsRecfg_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsRecfg=_CienaCesDhcpv6ClientSessStatsRecfg_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,6),_CienaCesDhcpv6ClientSessStatsRecfg_Type())
cienaCesDhcpv6ClientSessStatsRecfg.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsRecfg.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsInvalid_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsInvalid_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsInvalid=_CienaCesDhcpv6ClientSessStatsInvalid_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,7),_CienaCesDhcpv6ClientSessStatsInvalid_Type())
cienaCesDhcpv6ClientSessStatsInvalid.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsInvalid.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsPktsTx_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsPktsTx_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsPktsTx=_CienaCesDhcpv6ClientSessStatsPktsTx_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,8),_CienaCesDhcpv6ClientSessStatsPktsTx_Type())
cienaCesDhcpv6ClientSessStatsPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsPktsTx.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsSolicit_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsSolicit_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsSolicit=_CienaCesDhcpv6ClientSessStatsSolicit_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,9),_CienaCesDhcpv6ClientSessStatsSolicit_Type())
cienaCesDhcpv6ClientSessStatsSolicit.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsSolicit.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsRequest_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsRequest_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsRequest=_CienaCesDhcpv6ClientSessStatsRequest_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,10),_CienaCesDhcpv6ClientSessStatsRequest_Type())
cienaCesDhcpv6ClientSessStatsRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsRequest.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsConfirm_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsConfirm_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsConfirm=_CienaCesDhcpv6ClientSessStatsConfirm_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,11),_CienaCesDhcpv6ClientSessStatsConfirm_Type())
cienaCesDhcpv6ClientSessStatsConfirm.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsConfirm.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsRenew_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsRenew_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsRenew=_CienaCesDhcpv6ClientSessStatsRenew_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,12),_CienaCesDhcpv6ClientSessStatsRenew_Type())
cienaCesDhcpv6ClientSessStatsRenew.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsRenew.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsRebind_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsRebind_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsRebind=_CienaCesDhcpv6ClientSessStatsRebind_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,13),_CienaCesDhcpv6ClientSessStatsRebind_Type())
cienaCesDhcpv6ClientSessStatsRebind.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsRebind.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsInfoReq_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsInfoReq_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsInfoReq=_CienaCesDhcpv6ClientSessStatsInfoReq_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,14),_CienaCesDhcpv6ClientSessStatsInfoReq_Type())
cienaCesDhcpv6ClientSessStatsInfoReq.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsInfoReq.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsRelease_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsRelease_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsRelease=_CienaCesDhcpv6ClientSessStatsRelease_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,15),_CienaCesDhcpv6ClientSessStatsRelease_Type())
cienaCesDhcpv6ClientSessStatsRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsRelease.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsDecline_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsDecline_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsDecline=_CienaCesDhcpv6ClientSessStatsDecline_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,16),_CienaCesDhcpv6ClientSessStatsDecline_Type())
cienaCesDhcpv6ClientSessStatsDecline.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsDecline.setStatus(_A)
_CienaCesDhcpv6ClientSessStatsTxFail_Type=Gauge32
_CienaCesDhcpv6ClientSessStatsTxFail_Object=MibTableColumn
cienaCesDhcpv6ClientSessStatsTxFail=_CienaCesDhcpv6ClientSessStatsTxFail_Object((1,3,6,1,4,1,1271,2,1,30,1,1,9,1,17),_CienaCesDhcpv6ClientSessStatsTxFail_Type())
cienaCesDhcpv6ClientSessStatsTxFail.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6ClientSessStatsTxFail.setStatus(_A)
_CienaCesDhcpv6RelayAgent_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6RelayAgent=_CienaCesDhcpv6RelayAgent_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,1,2))
_CienaCesDhcpv6RelayAgentGlobalAttrs_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6RelayAgentGlobalAttrs=_CienaCesDhcpv6RelayAgentGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,1,2,1))
_CienaCesDhcpv6LdraState_Type=CienaGlobalState
_CienaCesDhcpv6LdraState_Object=MibScalar
cienaCesDhcpv6LdraState=_CienaCesDhcpv6LdraState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,1),_CienaCesDhcpv6LdraState_Type())
cienaCesDhcpv6LdraState.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraState.setStatus(_A)
class _CienaCesDhcpv6LdraInterfaceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('slotAndPort',1),('slotAndPortAndVlan',2),('intidString',3)))
_CienaCesDhcpv6LdraInterfaceId_Type.__name__=_D
_CienaCesDhcpv6LdraInterfaceId_Object=MibScalar
cienaCesDhcpv6LdraInterfaceId=_CienaCesDhcpv6LdraInterfaceId_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,2),_CienaCesDhcpv6LdraInterfaceId_Type())
cienaCesDhcpv6LdraInterfaceId.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraInterfaceId.setStatus(_A)
class _CienaCesDhcpv6LdraRemoteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('macAddress',1),('hostName',2),('ridString',3)))
_CienaCesDhcpv6LdraRemoteId_Type.__name__=_D
_CienaCesDhcpv6LdraRemoteId_Object=MibScalar
cienaCesDhcpv6LdraRemoteId=_CienaCesDhcpv6LdraRemoteId_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,3),_CienaCesDhcpv6LdraRemoteId_Type())
cienaCesDhcpv6LdraRemoteId.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRemoteId.setStatus(_A)
class _CienaCesDhcpv6LdraRemoteIdOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CienaCesDhcpv6LdraRemoteIdOption_Type.__name__=_D
_CienaCesDhcpv6LdraRemoteIdOption_Object=MibScalar
cienaCesDhcpv6LdraRemoteIdOption=_CienaCesDhcpv6LdraRemoteIdOption_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,4),_CienaCesDhcpv6LdraRemoteIdOption_Type())
cienaCesDhcpv6LdraRemoteIdOption.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRemoteIdOption.setStatus(_A)
class _CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Type.__name__=_M
_CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Object=MibScalar
cienaCesDhcpv6LdraRemoteIdEnterpriseNo=_CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,5),_CienaCesDhcpv6LdraRemoteIdEnterpriseNo_Type())
cienaCesDhcpv6LdraRemoteIdEnterpriseNo.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRemoteIdEnterpriseNo.setStatus(_A)
_CienaCesDhcpv6LdraForward_Type=Counter32
_CienaCesDhcpv6LdraForward_Object=MibScalar
cienaCesDhcpv6LdraForward=_CienaCesDhcpv6LdraForward_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,6),_CienaCesDhcpv6LdraForward_Type())
cienaCesDhcpv6LdraForward.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraForward.setStatus(_A)
_CienaCesDhcpv6LdraRelayed_Type=Counter32
_CienaCesDhcpv6LdraRelayed_Object=MibScalar
cienaCesDhcpv6LdraRelayed=_CienaCesDhcpv6LdraRelayed_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,7),_CienaCesDhcpv6LdraRelayed_Type())
cienaCesDhcpv6LdraRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRelayed.setStatus(_A)
_CienaCesDhcpv6LdraDropped_Type=Counter32
_CienaCesDhcpv6LdraDropped_Object=MibScalar
cienaCesDhcpv6LdraDropped=_CienaCesDhcpv6LdraDropped_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,8),_CienaCesDhcpv6LdraDropped_Type())
cienaCesDhcpv6LdraDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraDropped.setStatus(_A)
class _CienaCesDhcpv6LdraGlobalStatsClear_Type(CienaStatsClear):defaultValue=0
_CienaCesDhcpv6LdraGlobalStatsClear_Type.__name__=_J
_CienaCesDhcpv6LdraGlobalStatsClear_Object=MibScalar
cienaCesDhcpv6LdraGlobalStatsClear=_CienaCesDhcpv6LdraGlobalStatsClear_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,9),_CienaCesDhcpv6LdraGlobalStatsClear_Type())
cienaCesDhcpv6LdraGlobalStatsClear.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraGlobalStatsClear.setStatus(_A)
_CienaCesDhcpv6LdraNotForRelay_Type=Counter32
_CienaCesDhcpv6LdraNotForRelay_Object=MibScalar
cienaCesDhcpv6LdraNotForRelay=_CienaCesDhcpv6LdraNotForRelay_Object((1,3,6,1,4,1,1271,2,1,30,1,2,1,10),_CienaCesDhcpv6LdraNotForRelay_Type())
cienaCesDhcpv6LdraNotForRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraNotForRelay.setStatus(_A)
_CienaCesDhcpv6LdraStateTable_Object=MibTable
cienaCesDhcpv6LdraStateTable=_CienaCesDhcpv6LdraStateTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,2))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraStateTable.setStatus(_A)
_CienaCesDhcpv6LdraStateEntry_Object=MibTableRow
cienaCesDhcpv6LdraStateEntry=_CienaCesDhcpv6LdraStateEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,2,1))
cienaCesDhcpv6LdraStateEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraStateEntry.setStatus(_A)
class _CienaCesDhcpv6LdraVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_CienaCesDhcpv6LdraVlan_Type.__name__=_D
_CienaCesDhcpv6LdraVlan_Object=MibTableColumn
cienaCesDhcpv6LdraVlan=_CienaCesDhcpv6LdraVlan_Object((1,3,6,1,4,1,1271,2,1,30,1,2,2,1,1),_CienaCesDhcpv6LdraVlan_Type())
cienaCesDhcpv6LdraVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVlan.setStatus(_A)
_CienaCesDhcpv6LdraAdminState_Type=CienaGlobalState
_CienaCesDhcpv6LdraAdminState_Object=MibTableColumn
cienaCesDhcpv6LdraAdminState=_CienaCesDhcpv6LdraAdminState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,2,1,2),_CienaCesDhcpv6LdraAdminState_Type())
cienaCesDhcpv6LdraAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraAdminState.setStatus(_A)
_CienaCesDhcpv6LdraOperState_Type=CienaGlobalState
_CienaCesDhcpv6LdraOperState_Object=MibTableColumn
cienaCesDhcpv6LdraOperState=_CienaCesDhcpv6LdraOperState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,2,1,3),_CienaCesDhcpv6LdraOperState_Type())
cienaCesDhcpv6LdraOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraOperState.setStatus(_A)
_CienaCesDhcpv6LdraRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraRowStatus=_CienaCesDhcpv6LdraRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,2,1,4),_CienaCesDhcpv6LdraRowStatus_Type())
cienaCesDhcpv6LdraRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraTrustTable_Object=MibTable
cienaCesDhcpv6LdraTrustTable=_CienaCesDhcpv6LdraTrustTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,3))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraTrustTable.setStatus(_V)
_CienaCesDhcpv6LdraTrustEntry_Object=MibTableRow
cienaCesDhcpv6LdraTrustEntry=_CienaCesDhcpv6LdraTrustEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,3,1))
cienaCesDhcpv6LdraTrustEntry.setIndexNames((0,_C,_I),(0,_C,_W))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraTrustEntry.setStatus(_V)
class _CienaCesDhcpv6LdraPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6LdraPort_Type.__name__=_D
_CienaCesDhcpv6LdraPort_Object=MibTableColumn
cienaCesDhcpv6LdraPort=_CienaCesDhcpv6LdraPort_Object((1,3,6,1,4,1,1271,2,1,30,1,2,3,1,1),_CienaCesDhcpv6LdraPort_Type())
cienaCesDhcpv6LdraPort.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraPort.setStatus(_A)
class _CienaCesDhcpv6LdraTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_CienaCesDhcpv6LdraTrustMode_Type.__name__=_D
_CienaCesDhcpv6LdraTrustMode_Object=MibTableColumn
cienaCesDhcpv6LdraTrustMode=_CienaCesDhcpv6LdraTrustMode_Object((1,3,6,1,4,1,1271,2,1,30,1,2,3,1,2),_CienaCesDhcpv6LdraTrustMode_Type())
cienaCesDhcpv6LdraTrustMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraTrustMode.setStatus(_V)
_CienaCesDhcpv6LdraStatsTable_Object=MibTable
cienaCesDhcpv6LdraStatsTable=_CienaCesDhcpv6LdraStatsTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraStatsTable.setStatus(_A)
_CienaCesDhcpv6LdraStatsEntry_Object=MibTableRow
cienaCesDhcpv6LdraStatsEntry=_CienaCesDhcpv6LdraStatsEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1))
cienaCesDhcpv6LdraStatsEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraStatsEntry.setStatus(_A)
_CienaCesDhcpv6LdraPktsForRelay_Type=Counter32
_CienaCesDhcpv6LdraPktsForRelay_Object=MibTableColumn
cienaCesDhcpv6LdraPktsForRelay=_CienaCesDhcpv6LdraPktsForRelay_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,1),_CienaCesDhcpv6LdraPktsForRelay_Type())
cienaCesDhcpv6LdraPktsForRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraPktsForRelay.setStatus(_A)
_CienaCesDhcpv6LdraRelayedClient_Type=Counter32
_CienaCesDhcpv6LdraRelayedClient_Object=MibTableColumn
cienaCesDhcpv6LdraRelayedClient=_CienaCesDhcpv6LdraRelayedClient_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,2),_CienaCesDhcpv6LdraRelayedClient_Type())
cienaCesDhcpv6LdraRelayedClient.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRelayedClient.setStatus(_A)
_CienaCesDhcpv6LdraRelayedServer_Type=Counter32
_CienaCesDhcpv6LdraRelayedServer_Object=MibTableColumn
cienaCesDhcpv6LdraRelayedServer=_CienaCesDhcpv6LdraRelayedServer_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,3),_CienaCesDhcpv6LdraRelayedServer_Type())
cienaCesDhcpv6LdraRelayedServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRelayedServer.setStatus(_A)
_CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Type=Counter32
_CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Object=MibTableColumn
cienaCesDhcpv6LdraUntrustedClientPortPktsRx=_CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,4),_CienaCesDhcpv6LdraUntrustedClientPortPktsRx_Type())
cienaCesDhcpv6LdraUntrustedClientPortPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraUntrustedClientPortPktsRx.setStatus(_A)
_CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Type=Counter32
_CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Object=MibTableColumn
cienaCesDhcpv6LdraUntrustedServerPortPktsRx=_CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,5),_CienaCesDhcpv6LdraUntrustedServerPortPktsRx_Type())
cienaCesDhcpv6LdraUntrustedServerPortPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraUntrustedServerPortPktsRx.setStatus(_A)
_CienaCesDhcpv6LdraFailedValidationPktDrop_Type=Counter32
_CienaCesDhcpv6LdraFailedValidationPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraFailedValidationPktDrop=_CienaCesDhcpv6LdraFailedValidationPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,6),_CienaCesDhcpv6LdraFailedValidationPktDrop_Type())
cienaCesDhcpv6LdraFailedValidationPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraFailedValidationPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraInvalidConfigPktDrop_Type=Counter32
_CienaCesDhcpv6LdraInvalidConfigPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraInvalidConfigPktDrop=_CienaCesDhcpv6LdraInvalidConfigPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,7),_CienaCesDhcpv6LdraInvalidConfigPktDrop_Type())
cienaCesDhcpv6LdraInvalidConfigPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraInvalidConfigPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraExceededHopCountPktDrop_Type=Counter32
_CienaCesDhcpv6LdraExceededHopCountPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraExceededHopCountPktDrop=_CienaCesDhcpv6LdraExceededHopCountPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,8),_CienaCesDhcpv6LdraExceededHopCountPktDrop_Type())
cienaCesDhcpv6LdraExceededHopCountPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraExceededHopCountPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraExceedMTUPktDrop_Type=Counter32
_CienaCesDhcpv6LdraExceedMTUPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraExceedMTUPktDrop=_CienaCesDhcpv6LdraExceedMTUPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,9),_CienaCesDhcpv6LdraExceedMTUPktDrop_Type())
cienaCesDhcpv6LdraExceedMTUPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraExceedMTUPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraNoTrustedServerPktDrop_Type=Counter32
_CienaCesDhcpv6LdraNoTrustedServerPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraNoTrustedServerPktDrop=_CienaCesDhcpv6LdraNoTrustedServerPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,10),_CienaCesDhcpv6LdraNoTrustedServerPktDrop_Type())
cienaCesDhcpv6LdraNoTrustedServerPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraNoTrustedServerPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraNoTrustedClientPktDrop_Type=Counter32
_CienaCesDhcpv6LdraNoTrustedClientPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraNoTrustedClientPktDrop=_CienaCesDhcpv6LdraNoTrustedClientPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,11),_CienaCesDhcpv6LdraNoTrustedClientPktDrop_Type())
cienaCesDhcpv6LdraNoTrustedClientPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraNoTrustedClientPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Type=Counter32
_CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop=_CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,12),_CienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop_Type())
cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraGeneralErrors_Type=Counter32
_CienaCesDhcpv6LdraGeneralErrors_Object=MibTableColumn
cienaCesDhcpv6LdraGeneralErrors=_CienaCesDhcpv6LdraGeneralErrors_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,13),_CienaCesDhcpv6LdraGeneralErrors_Type())
cienaCesDhcpv6LdraGeneralErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraGeneralErrors.setStatus(_A)
class _CienaCesDhcpv6LdraStatsClear_Type(CienaStatsClear):defaultValue=0
_CienaCesDhcpv6LdraStatsClear_Type.__name__=_J
_CienaCesDhcpv6LdraStatsClear_Object=MibTableColumn
cienaCesDhcpv6LdraStatsClear=_CienaCesDhcpv6LdraStatsClear_Object((1,3,6,1,4,1,1271,2,1,30,1,2,4,1,14),_CienaCesDhcpv6LdraStatsClear_Type())
cienaCesDhcpv6LdraStatsClear.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraStatsClear.setStatus(_A)
_CienaCesDhcpv6LdraIntidStringTable_Object=MibTable
cienaCesDhcpv6LdraIntidStringTable=_CienaCesDhcpv6LdraIntidStringTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,5))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraIntidStringTable.setStatus(_A)
_CienaCesDhcpv6LdraIntidStringEntry_Object=MibTableRow
cienaCesDhcpv6LdraIntidStringEntry=_CienaCesDhcpv6LdraIntidStringEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,5,1))
cienaCesDhcpv6LdraIntidStringEntry.setIndexNames((0,_C,_I),(0,_C,_d))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraIntidStringEntry.setStatus(_A)
class _CienaCesDhcpv6LdraIntidStringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6LdraIntidStringPort_Type.__name__=_D
_CienaCesDhcpv6LdraIntidStringPort_Object=MibTableColumn
cienaCesDhcpv6LdraIntidStringPort=_CienaCesDhcpv6LdraIntidStringPort_Object((1,3,6,1,4,1,1271,2,1,30,1,2,5,1,1),_CienaCesDhcpv6LdraIntidStringPort_Type())
cienaCesDhcpv6LdraIntidStringPort.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraIntidStringPort.setStatus(_A)
class _CienaCesDhcpv6LdraIntidString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaCesDhcpv6LdraIntidString_Type.__name__=_H
_CienaCesDhcpv6LdraIntidString_Object=MibTableColumn
cienaCesDhcpv6LdraIntidString=_CienaCesDhcpv6LdraIntidString_Object((1,3,6,1,4,1,1271,2,1,30,1,2,5,1,2),_CienaCesDhcpv6LdraIntidString_Type())
cienaCesDhcpv6LdraIntidString.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraIntidString.setStatus(_A)
_CienaCesDhcpv6LdraIntidStringRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraIntidStringRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraIntidStringRowStatus=_CienaCesDhcpv6LdraIntidStringRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,5,1,3),_CienaCesDhcpv6LdraIntidStringRowStatus_Type())
cienaCesDhcpv6LdraIntidStringRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraIntidStringRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraRidStringTable_Object=MibTable
cienaCesDhcpv6LdraRidStringTable=_CienaCesDhcpv6LdraRidStringTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,6))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRidStringTable.setStatus(_A)
_CienaCesDhcpv6LdraRidStringEntry_Object=MibTableRow
cienaCesDhcpv6LdraRidStringEntry=_CienaCesDhcpv6LdraRidStringEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,6,1))
cienaCesDhcpv6LdraRidStringEntry.setIndexNames((0,_C,_I),(0,_C,_e))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRidStringEntry.setStatus(_A)
class _CienaCesDhcpv6LdraRidStringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6LdraRidStringPort_Type.__name__=_D
_CienaCesDhcpv6LdraRidStringPort_Object=MibTableColumn
cienaCesDhcpv6LdraRidStringPort=_CienaCesDhcpv6LdraRidStringPort_Object((1,3,6,1,4,1,1271,2,1,30,1,2,6,1,1),_CienaCesDhcpv6LdraRidStringPort_Type())
cienaCesDhcpv6LdraRidStringPort.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRidStringPort.setStatus(_A)
class _CienaCesDhcpv6LdraRidString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaCesDhcpv6LdraRidString_Type.__name__=_H
_CienaCesDhcpv6LdraRidString_Object=MibTableColumn
cienaCesDhcpv6LdraRidString=_CienaCesDhcpv6LdraRidString_Object((1,3,6,1,4,1,1271,2,1,30,1,2,6,1,2),_CienaCesDhcpv6LdraRidString_Type())
cienaCesDhcpv6LdraRidString.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRidString.setStatus(_A)
_CienaCesDhcpv6LdraRidStringRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraRidStringRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraRidStringRowStatus=_CienaCesDhcpv6LdraRidStringRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,6,1,3),_CienaCesDhcpv6LdraRidStringRowStatus_Type())
cienaCesDhcpv6LdraRidStringRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraRidStringRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraExtTrustTable_Object=MibTable
cienaCesDhcpv6LdraExtTrustTable=_CienaCesDhcpv6LdraExtTrustTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,7))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraExtTrustTable.setStatus(_A)
_CienaCesDhcpv6LdraExtTrustEntry_Object=MibTableRow
cienaCesDhcpv6LdraExtTrustEntry=_CienaCesDhcpv6LdraExtTrustEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,7,1))
cienaCesDhcpv6LdraExtTrustEntry.setIndexNames((0,_C,_I),(0,_C,_W))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraExtTrustEntry.setStatus(_A)
class _CienaCesDhcpv6LdraExtPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CienaCesDhcpv6LdraExtPortState_Type.__name__=_D
_CienaCesDhcpv6LdraExtPortState_Object=MibTableColumn
cienaCesDhcpv6LdraExtPortState=_CienaCesDhcpv6LdraExtPortState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,7,1,1),_CienaCesDhcpv6LdraExtPortState_Type())
cienaCesDhcpv6LdraExtPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraExtPortState.setStatus(_A)
class _CienaCesDhcpv6LdraExtTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_CienaCesDhcpv6LdraExtTrustMode_Type.__name__=_D
_CienaCesDhcpv6LdraExtTrustMode_Object=MibTableColumn
cienaCesDhcpv6LdraExtTrustMode=_CienaCesDhcpv6LdraExtTrustMode_Object((1,3,6,1,4,1,1271,2,1,30,1,2,7,1,2),_CienaCesDhcpv6LdraExtTrustMode_Type())
cienaCesDhcpv6LdraExtTrustMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraExtTrustMode.setStatus(_A)
_CienaCesDhcpv6LdraVsStateTable_Object=MibTable
cienaCesDhcpv6LdraVsStateTable=_CienaCesDhcpv6LdraVsStateTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsStateTable.setStatus(_A)
_CienaCesDhcpv6LdraVsStateEntry_Object=MibTableRow
cienaCesDhcpv6LdraVsStateEntry=_CienaCesDhcpv6LdraVsStateEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8,1))
cienaCesDhcpv6LdraVsStateEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsStateEntry.setStatus(_A)
class _CienaCesDhcpv6LdraVsVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_CienaCesDhcpv6LdraVsVlan_Type.__name__=_D
_CienaCesDhcpv6LdraVsVlan_Object=MibTableColumn
cienaCesDhcpv6LdraVsVlan=_CienaCesDhcpv6LdraVsVlan_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8,1,1),_CienaCesDhcpv6LdraVsVlan_Type())
cienaCesDhcpv6LdraVsVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsVlan.setStatus(_A)
class _CienaCesDhcpv6LdraVsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CienaCesDhcpv6LdraVsName_Type.__name__=_H
_CienaCesDhcpv6LdraVsName_Object=MibTableColumn
cienaCesDhcpv6LdraVsName=_CienaCesDhcpv6LdraVsName_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8,1,2),_CienaCesDhcpv6LdraVsName_Type())
cienaCesDhcpv6LdraVsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsName.setStatus(_A)
_CienaCesDhcpv6LdraVsAdminState_Type=CienaGlobalState
_CienaCesDhcpv6LdraVsAdminState_Object=MibTableColumn
cienaCesDhcpv6LdraVsAdminState=_CienaCesDhcpv6LdraVsAdminState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8,1,3),_CienaCesDhcpv6LdraVsAdminState_Type())
cienaCesDhcpv6LdraVsAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsAdminState.setStatus(_A)
_CienaCesDhcpv6LdraVsOperState_Type=CienaGlobalState
_CienaCesDhcpv6LdraVsOperState_Object=MibTableColumn
cienaCesDhcpv6LdraVsOperState=_CienaCesDhcpv6LdraVsOperState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8,1,4),_CienaCesDhcpv6LdraVsOperState_Type())
cienaCesDhcpv6LdraVsOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsOperState.setStatus(_A)
_CienaCesDhcpv6LdraVsRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraVsRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraVsRowStatus=_CienaCesDhcpv6LdraVsRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,8,1,5),_CienaCesDhcpv6LdraVsRowStatus_Type())
cienaCesDhcpv6LdraVsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraVsTrustTable_Object=MibTable
cienaCesDhcpv6LdraVsTrustTable=_CienaCesDhcpv6LdraVsTrustTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,9))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsTrustTable.setStatus(_A)
_CienaCesDhcpv6LdraVsTrustEntry_Object=MibTableRow
cienaCesDhcpv6LdraVsTrustEntry=_CienaCesDhcpv6LdraVsTrustEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,9,1))
cienaCesDhcpv6LdraVsTrustEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_f))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsTrustEntry.setStatus(_A)
class _CienaCesDhcpv6LdraVsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDhcpv6LdraVsPort_Type.__name__=_D
_CienaCesDhcpv6LdraVsPort_Object=MibTableColumn
cienaCesDhcpv6LdraVsPort=_CienaCesDhcpv6LdraVsPort_Object((1,3,6,1,4,1,1271,2,1,30,1,2,9,1,1),_CienaCesDhcpv6LdraVsPort_Type())
cienaCesDhcpv6LdraVsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsPort.setStatus(_A)
class _CienaCesDhcpv6LdraVsSubVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_CienaCesDhcpv6LdraVsSubVlan_Type.__name__=_D
_CienaCesDhcpv6LdraVsSubVlan_Object=MibTableColumn
cienaCesDhcpv6LdraVsSubVlan=_CienaCesDhcpv6LdraVsSubVlan_Object((1,3,6,1,4,1,1271,2,1,30,1,2,9,1,2),_CienaCesDhcpv6LdraVsSubVlan_Type())
cienaCesDhcpv6LdraVsSubVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsSubVlan.setStatus(_A)
class _CienaCesDhcpv6LdraVsPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CienaCesDhcpv6LdraVsPortState_Type.__name__=_D
_CienaCesDhcpv6LdraVsPortState_Object=MibTableColumn
cienaCesDhcpv6LdraVsPortState=_CienaCesDhcpv6LdraVsPortState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,9,1,3),_CienaCesDhcpv6LdraVsPortState_Type())
cienaCesDhcpv6LdraVsPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsPortState.setStatus(_A)
class _CienaCesDhcpv6LdraVsTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_CienaCesDhcpv6LdraVsTrustMode_Type.__name__=_D
_CienaCesDhcpv6LdraVsTrustMode_Object=MibTableColumn
cienaCesDhcpv6LdraVsTrustMode=_CienaCesDhcpv6LdraVsTrustMode_Object((1,3,6,1,4,1,1271,2,1,30,1,2,9,1,4),_CienaCesDhcpv6LdraVsTrustMode_Type())
cienaCesDhcpv6LdraVsTrustMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsTrustMode.setStatus(_A)
_CienaCesDhcpv6LdraVsStatsTable_Object=MibTable
cienaCesDhcpv6LdraVsStatsTable=_CienaCesDhcpv6LdraVsStatsTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsStatsTable.setStatus(_A)
_CienaCesDhcpv6LdraVsStatsEntry_Object=MibTableRow
cienaCesDhcpv6LdraVsStatsEntry=_CienaCesDhcpv6LdraVsStatsEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1))
cienaCesDhcpv6LdraVsStatsEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsStatsEntry.setStatus(_A)
_CienaCesDhcpv6LdraVsPktsForRelay_Type=Counter32
_CienaCesDhcpv6LdraVsPktsForRelay_Object=MibTableColumn
cienaCesDhcpv6LdraVsPktsForRelay=_CienaCesDhcpv6LdraVsPktsForRelay_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,1),_CienaCesDhcpv6LdraVsPktsForRelay_Type())
cienaCesDhcpv6LdraVsPktsForRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsPktsForRelay.setStatus(_A)
_CienaCesDhcpv6LdraVsRelayedClient_Type=Counter32
_CienaCesDhcpv6LdraVsRelayedClient_Object=MibTableColumn
cienaCesDhcpv6LdraVsRelayedClient=_CienaCesDhcpv6LdraVsRelayedClient_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,2),_CienaCesDhcpv6LdraVsRelayedClient_Type())
cienaCesDhcpv6LdraVsRelayedClient.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRelayedClient.setStatus(_A)
_CienaCesDhcpv6LdraVsRelayedServer_Type=Counter32
_CienaCesDhcpv6LdraVsRelayedServer_Object=MibTableColumn
cienaCesDhcpv6LdraVsRelayedServer=_CienaCesDhcpv6LdraVsRelayedServer_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,3),_CienaCesDhcpv6LdraVsRelayedServer_Type())
cienaCesDhcpv6LdraVsRelayedServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRelayedServer.setStatus(_A)
_CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Type=Counter32
_CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Object=MibTableColumn
cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx=_CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,4),_CienaCesDhcpv6LdraVsUntrustedClientPortPktsRx_Type())
cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx.setStatus(_A)
_CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Type=Counter32
_CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Object=MibTableColumn
cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx=_CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,5),_CienaCesDhcpv6LdraVsUntrustedServerPortPktsRx_Type())
cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx.setStatus(_A)
_CienaCesDhcpv6LdraVsFailedValidationPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsFailedValidationPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsFailedValidationPktDrop=_CienaCesDhcpv6LdraVsFailedValidationPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,6),_CienaCesDhcpv6LdraVsFailedValidationPktDrop_Type())
cienaCesDhcpv6LdraVsFailedValidationPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsFailedValidationPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsInvalidConfigPktDrop=_CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,7),_CienaCesDhcpv6LdraVsInvalidConfigPktDrop_Type())
cienaCesDhcpv6LdraVsInvalidConfigPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsInvalidConfigPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsExceededHopCountPktDrop=_CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,8),_CienaCesDhcpv6LdraVsExceededHopCountPktDrop_Type())
cienaCesDhcpv6LdraVsExceededHopCountPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsExceededHopCountPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsExceedMTUPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsExceedMTUPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsExceedMTUPktDrop=_CienaCesDhcpv6LdraVsExceedMTUPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,9),_CienaCesDhcpv6LdraVsExceedMTUPktDrop_Type())
cienaCesDhcpv6LdraVsExceedMTUPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsExceedMTUPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsNoTrustedServerPktDrop=_CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,10),_CienaCesDhcpv6LdraVsNoTrustedServerPktDrop_Type())
cienaCesDhcpv6LdraVsNoTrustedServerPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsNoTrustedServerPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsNoTrustedClientPktDrop=_CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,11),_CienaCesDhcpv6LdraVsNoTrustedClientPktDrop_Type())
cienaCesDhcpv6LdraVsNoTrustedClientPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsNoTrustedClientPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Type=Counter32
_CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop=_CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,12),_CienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop_Type())
cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraVsGeneralErrors_Type=Counter32
_CienaCesDhcpv6LdraVsGeneralErrors_Object=MibTableColumn
cienaCesDhcpv6LdraVsGeneralErrors=_CienaCesDhcpv6LdraVsGeneralErrors_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,13),_CienaCesDhcpv6LdraVsGeneralErrors_Type())
cienaCesDhcpv6LdraVsGeneralErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsGeneralErrors.setStatus(_A)
class _CienaCesDhcpv6LdraVsStatsClear_Type(CienaStatsClear):defaultValue=0
_CienaCesDhcpv6LdraVsStatsClear_Type.__name__=_J
_CienaCesDhcpv6LdraVsStatsClear_Object=MibTableColumn
cienaCesDhcpv6LdraVsStatsClear=_CienaCesDhcpv6LdraVsStatsClear_Object((1,3,6,1,4,1,1271,2,1,30,1,2,10,1,14),_CienaCesDhcpv6LdraVsStatsClear_Type())
cienaCesDhcpv6LdraVsStatsClear.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsStatsClear.setStatus(_A)
_CienaCesDhcpv6LdraVsIntidStringTable_Object=MibTable
cienaCesDhcpv6LdraVsIntidStringTable=_CienaCesDhcpv6LdraVsIntidStringTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,11))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsIntidStringTable.setStatus(_A)
_CienaCesDhcpv6LdraVsIntidStringEntry_Object=MibTableRow
cienaCesDhcpv6LdraVsIntidStringEntry=_CienaCesDhcpv6LdraVsIntidStringEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,11,1))
cienaCesDhcpv6LdraVsIntidStringEntry.setIndexNames((0,_C,_I),(0,_C,_T))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsIntidStringEntry.setStatus(_A)
class _CienaCesDhcpv6LdraVsIntidString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaCesDhcpv6LdraVsIntidString_Type.__name__=_H
_CienaCesDhcpv6LdraVsIntidString_Object=MibTableColumn
cienaCesDhcpv6LdraVsIntidString=_CienaCesDhcpv6LdraVsIntidString_Object((1,3,6,1,4,1,1271,2,1,30,1,2,11,1,1),_CienaCesDhcpv6LdraVsIntidString_Type())
cienaCesDhcpv6LdraVsIntidString.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsIntidString.setStatus(_A)
_CienaCesDhcpv6LdraVsIntidStringRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraVsIntidStringRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraVsIntidStringRowStatus=_CienaCesDhcpv6LdraVsIntidStringRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,11,1,2),_CienaCesDhcpv6LdraVsIntidStringRowStatus_Type())
cienaCesDhcpv6LdraVsIntidStringRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsIntidStringRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraVsRidStringTable_Object=MibTable
cienaCesDhcpv6LdraVsRidStringTable=_CienaCesDhcpv6LdraVsRidStringTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,12))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRidStringTable.setStatus(_A)
_CienaCesDhcpv6LdraVsRidStringEntry_Object=MibTableRow
cienaCesDhcpv6LdraVsRidStringEntry=_CienaCesDhcpv6LdraVsRidStringEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,12,1))
cienaCesDhcpv6LdraVsRidStringEntry.setIndexNames((0,_C,_I),(0,_C,_T))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRidStringEntry.setStatus(_A)
class _CienaCesDhcpv6LdraVsRidString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaCesDhcpv6LdraVsRidString_Type.__name__=_H
_CienaCesDhcpv6LdraVsRidString_Object=MibTableColumn
cienaCesDhcpv6LdraVsRidString=_CienaCesDhcpv6LdraVsRidString_Object((1,3,6,1,4,1,1271,2,1,30,1,2,12,1,1),_CienaCesDhcpv6LdraVsRidString_Type())
cienaCesDhcpv6LdraVsRidString.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRidString.setStatus(_A)
_CienaCesDhcpv6LdraVsRidStringRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraVsRidStringRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraVsRidStringRowStatus=_CienaCesDhcpv6LdraVsRidStringRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,12,1,2),_CienaCesDhcpv6LdraVsRidStringRowStatus_Type())
cienaCesDhcpv6LdraVsRidStringRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraVsRidStringRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraMplsStateTable_Object=MibTable
cienaCesDhcpv6LdraMplsStateTable=_CienaCesDhcpv6LdraMplsStateTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsStateTable.setStatus(_A)
_CienaCesDhcpv6LdraMplsStateEntry_Object=MibTableRow
cienaCesDhcpv6LdraMplsStateEntry=_CienaCesDhcpv6LdraMplsStateEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13,1))
cienaCesDhcpv6LdraMplsStateEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsStateEntry.setStatus(_A)
class _CienaCesDhcpv6LdraMplsId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1677215))
_CienaCesDhcpv6LdraMplsId_Type.__name__=_M
_CienaCesDhcpv6LdraMplsId_Object=MibTableColumn
cienaCesDhcpv6LdraMplsId=_CienaCesDhcpv6LdraMplsId_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13,1,1),_CienaCesDhcpv6LdraMplsId_Type())
cienaCesDhcpv6LdraMplsId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsId.setStatus(_A)
class _CienaCesDhcpv6LdraMplsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CienaCesDhcpv6LdraMplsName_Type.__name__=_H
_CienaCesDhcpv6LdraMplsName_Object=MibTableColumn
cienaCesDhcpv6LdraMplsName=_CienaCesDhcpv6LdraMplsName_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13,1,2),_CienaCesDhcpv6LdraMplsName_Type())
cienaCesDhcpv6LdraMplsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsName.setStatus(_A)
_CienaCesDhcpv6LdraMplsAdminState_Type=CienaGlobalState
_CienaCesDhcpv6LdraMplsAdminState_Object=MibTableColumn
cienaCesDhcpv6LdraMplsAdminState=_CienaCesDhcpv6LdraMplsAdminState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13,1,3),_CienaCesDhcpv6LdraMplsAdminState_Type())
cienaCesDhcpv6LdraMplsAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsAdminState.setStatus(_A)
_CienaCesDhcpv6LdraMplsOperState_Type=CienaGlobalState
_CienaCesDhcpv6LdraMplsOperState_Object=MibTableColumn
cienaCesDhcpv6LdraMplsOperState=_CienaCesDhcpv6LdraMplsOperState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13,1,4),_CienaCesDhcpv6LdraMplsOperState_Type())
cienaCesDhcpv6LdraMplsOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsOperState.setStatus(_A)
_CienaCesDhcpv6LdraMplsRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraMplsRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraMplsRowStatus=_CienaCesDhcpv6LdraMplsRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,13,1,5),_CienaCesDhcpv6LdraMplsRowStatus_Type())
cienaCesDhcpv6LdraMplsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraMplsTrustTable_Object=MibTable
cienaCesDhcpv6LdraMplsTrustTable=_CienaCesDhcpv6LdraMplsTrustTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,14))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsTrustTable.setStatus(_A)
_CienaCesDhcpv6LdraMplsTrustEntry_Object=MibTableRow
cienaCesDhcpv6LdraMplsTrustEntry=_CienaCesDhcpv6LdraMplsTrustEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,14,1))
cienaCesDhcpv6LdraMplsTrustEntry.setIndexNames((0,_C,_L),(0,_C,_U))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsTrustEntry.setStatus(_A)
class _CienaCesDhcpv6LdraMplsInterface_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CienaCesDhcpv6LdraMplsInterface_Type.__name__=_M
_CienaCesDhcpv6LdraMplsInterface_Object=MibTableColumn
cienaCesDhcpv6LdraMplsInterface=_CienaCesDhcpv6LdraMplsInterface_Object((1,3,6,1,4,1,1271,2,1,30,1,2,14,1,1),_CienaCesDhcpv6LdraMplsInterface_Type())
cienaCesDhcpv6LdraMplsInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsInterface.setStatus(_A)
class _CienaCesDhcpv6LdraMplsVcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CienaCesDhcpv6LdraMplsVcName_Type.__name__=_H
_CienaCesDhcpv6LdraMplsVcName_Object=MibTableColumn
cienaCesDhcpv6LdraMplsVcName=_CienaCesDhcpv6LdraMplsVcName_Object((1,3,6,1,4,1,1271,2,1,30,1,2,14,1,2),_CienaCesDhcpv6LdraMplsVcName_Type())
cienaCesDhcpv6LdraMplsVcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsVcName.setStatus(_A)
class _CienaCesDhcpv6LdraMplsInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_CienaCesDhcpv6LdraMplsInterfaceState_Type.__name__=_D
_CienaCesDhcpv6LdraMplsInterfaceState_Object=MibTableColumn
cienaCesDhcpv6LdraMplsInterfaceState=_CienaCesDhcpv6LdraMplsInterfaceState_Object((1,3,6,1,4,1,1271,2,1,30,1,2,14,1,3),_CienaCesDhcpv6LdraMplsInterfaceState_Type())
cienaCesDhcpv6LdraMplsInterfaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsInterfaceState.setStatus(_A)
class _CienaCesDhcpv6LdraMplsTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_CienaCesDhcpv6LdraMplsTrustMode_Type.__name__=_D
_CienaCesDhcpv6LdraMplsTrustMode_Object=MibTableColumn
cienaCesDhcpv6LdraMplsTrustMode=_CienaCesDhcpv6LdraMplsTrustMode_Object((1,3,6,1,4,1,1271,2,1,30,1,2,14,1,4),_CienaCesDhcpv6LdraMplsTrustMode_Type())
cienaCesDhcpv6LdraMplsTrustMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsTrustMode.setStatus(_A)
_CienaCesDhcpv6LdraMplsStatsTable_Object=MibTable
cienaCesDhcpv6LdraMplsStatsTable=_CienaCesDhcpv6LdraMplsStatsTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsStatsTable.setStatus(_A)
_CienaCesDhcpv6LdraMplsStatsEntry_Object=MibTableRow
cienaCesDhcpv6LdraMplsStatsEntry=_CienaCesDhcpv6LdraMplsStatsEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1))
cienaCesDhcpv6LdraMplsStatsEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsStatsEntry.setStatus(_A)
_CienaCesDhcpv6LdraMplsPktsForRelay_Type=Counter32
_CienaCesDhcpv6LdraMplsPktsForRelay_Object=MibTableColumn
cienaCesDhcpv6LdraMplsPktsForRelay=_CienaCesDhcpv6LdraMplsPktsForRelay_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,1),_CienaCesDhcpv6LdraMplsPktsForRelay_Type())
cienaCesDhcpv6LdraMplsPktsForRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsPktsForRelay.setStatus(_A)
_CienaCesDhcpv6LdraMplsRelayedClient_Type=Counter32
_CienaCesDhcpv6LdraMplsRelayedClient_Object=MibTableColumn
cienaCesDhcpv6LdraMplsRelayedClient=_CienaCesDhcpv6LdraMplsRelayedClient_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,2),_CienaCesDhcpv6LdraMplsRelayedClient_Type())
cienaCesDhcpv6LdraMplsRelayedClient.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRelayedClient.setStatus(_A)
_CienaCesDhcpv6LdraMplsRelayedServer_Type=Counter32
_CienaCesDhcpv6LdraMplsRelayedServer_Object=MibTableColumn
cienaCesDhcpv6LdraMplsRelayedServer=_CienaCesDhcpv6LdraMplsRelayedServer_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,3),_CienaCesDhcpv6LdraMplsRelayedServer_Type())
cienaCesDhcpv6LdraMplsRelayedServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRelayedServer.setStatus(_A)
_CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Type=Counter32
_CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Object=MibTableColumn
cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx=_CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,4),_CienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx_Type())
cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx.setStatus(_A)
_CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Type=Counter32
_CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Object=MibTableColumn
cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx=_CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,5),_CienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx_Type())
cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx.setStatus(_A)
_CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsFailedValidationPktDrop=_CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,6),_CienaCesDhcpv6LdraMplsFailedValidationPktDrop_Type())
cienaCesDhcpv6LdraMplsFailedValidationPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsFailedValidationPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsInvalidConfigPktDrop=_CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,7),_CienaCesDhcpv6LdraMplsInvalidConfigPktDrop_Type())
cienaCesDhcpv6LdraMplsInvalidConfigPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsInvalidConfigPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsExceededHopCountPktDrop=_CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,8),_CienaCesDhcpv6LdraMplsExceededHopCountPktDrop_Type())
cienaCesDhcpv6LdraMplsExceededHopCountPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsExceededHopCountPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsExceedMTUPktDrop=_CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,9),_CienaCesDhcpv6LdraMplsExceedMTUPktDrop_Type())
cienaCesDhcpv6LdraMplsExceedMTUPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsExceedMTUPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop=_CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,10),_CienaCesDhcpv6LdraMplsNoTrustedServerPktDrop_Type())
cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop=_CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,11),_CienaCesDhcpv6LdraMplsNoTrustedClientPktDrop_Type())
cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Type=Counter32
_CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Object=MibTableColumn
cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop=_CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,12),_CienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop_Type())
cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop.setStatus(_A)
_CienaCesDhcpv6LdraMplsGeneralErrors_Type=Counter32
_CienaCesDhcpv6LdraMplsGeneralErrors_Object=MibTableColumn
cienaCesDhcpv6LdraMplsGeneralErrors=_CienaCesDhcpv6LdraMplsGeneralErrors_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,13),_CienaCesDhcpv6LdraMplsGeneralErrors_Type())
cienaCesDhcpv6LdraMplsGeneralErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsGeneralErrors.setStatus(_A)
class _CienaCesDhcpv6LdraMplsStatsClear_Type(CienaStatsClear):defaultValue=0
_CienaCesDhcpv6LdraMplsStatsClear_Type.__name__=_J
_CienaCesDhcpv6LdraMplsStatsClear_Object=MibTableColumn
cienaCesDhcpv6LdraMplsStatsClear=_CienaCesDhcpv6LdraMplsStatsClear_Object((1,3,6,1,4,1,1271,2,1,30,1,2,15,1,14),_CienaCesDhcpv6LdraMplsStatsClear_Type())
cienaCesDhcpv6LdraMplsStatsClear.setMaxAccess(_G)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsStatsClear.setStatus(_A)
_CienaCesDhcpv6LdraMplsIntidStringTable_Object=MibTable
cienaCesDhcpv6LdraMplsIntidStringTable=_CienaCesDhcpv6LdraMplsIntidStringTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,16))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsIntidStringTable.setStatus(_A)
_CienaCesDhcpv6LdraMplsIntidStringEntry_Object=MibTableRow
cienaCesDhcpv6LdraMplsIntidStringEntry=_CienaCesDhcpv6LdraMplsIntidStringEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,16,1))
cienaCesDhcpv6LdraMplsIntidStringEntry.setIndexNames((0,_C,_L),(0,_C,_U))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsIntidStringEntry.setStatus(_A)
class _CienaCesDhcpv6LdraMplsIntidString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaCesDhcpv6LdraMplsIntidString_Type.__name__=_H
_CienaCesDhcpv6LdraMplsIntidString_Object=MibTableColumn
cienaCesDhcpv6LdraMplsIntidString=_CienaCesDhcpv6LdraMplsIntidString_Object((1,3,6,1,4,1,1271,2,1,30,1,2,16,1,1),_CienaCesDhcpv6LdraMplsIntidString_Type())
cienaCesDhcpv6LdraMplsIntidString.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsIntidString.setStatus(_A)
_CienaCesDhcpv6LdraMplsIntidStringRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraMplsIntidStringRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraMplsIntidStringRowStatus=_CienaCesDhcpv6LdraMplsIntidStringRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,16,1,2),_CienaCesDhcpv6LdraMplsIntidStringRowStatus_Type())
cienaCesDhcpv6LdraMplsIntidStringRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsIntidStringRowStatus.setStatus(_A)
_CienaCesDhcpv6LdraMplsRidStringTable_Object=MibTable
cienaCesDhcpv6LdraMplsRidStringTable=_CienaCesDhcpv6LdraMplsRidStringTable_Object((1,3,6,1,4,1,1271,2,1,30,1,2,17))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRidStringTable.setStatus(_A)
_CienaCesDhcpv6LdraMplsRidStringEntry_Object=MibTableRow
cienaCesDhcpv6LdraMplsRidStringEntry=_CienaCesDhcpv6LdraMplsRidStringEntry_Object((1,3,6,1,4,1,1271,2,1,30,1,2,17,1))
cienaCesDhcpv6LdraMplsRidStringEntry.setIndexNames((0,_C,_L),(0,_C,_U))
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRidStringEntry.setStatus(_A)
class _CienaCesDhcpv6LdraMplsRidString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CienaCesDhcpv6LdraMplsRidString_Type.__name__=_H
_CienaCesDhcpv6LdraMplsRidString_Object=MibTableColumn
cienaCesDhcpv6LdraMplsRidString=_CienaCesDhcpv6LdraMplsRidString_Object((1,3,6,1,4,1,1271,2,1,30,1,2,17,1,1),_CienaCesDhcpv6LdraMplsRidString_Type())
cienaCesDhcpv6LdraMplsRidString.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRidString.setStatus(_A)
_CienaCesDhcpv6LdraMplsRidStringRowStatus_Type=RowStatus
_CienaCesDhcpv6LdraMplsRidStringRowStatus_Object=MibTableColumn
cienaCesDhcpv6LdraMplsRidStringRowStatus=_CienaCesDhcpv6LdraMplsRidStringRowStatus_Object((1,3,6,1,4,1,1271,2,1,30,1,2,17,1,2),_CienaCesDhcpv6LdraMplsRidStringRowStatus_Type())
cienaCesDhcpv6LdraMplsRidStringRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDhcpv6LdraMplsRidStringRowStatus.setStatus(_A)
_CienaCesDhcpv6ClientMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6ClientMIBConformance=_CienaCesDhcpv6ClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,2))
_CienaCesDhcpv6ClientMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6ClientMIBCompliances=_CienaCesDhcpv6ClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,2,1))
_CienaCesDhcpv6ClientMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6ClientMIBGroups=_CienaCesDhcpv6ClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,30,2,2))
_CienaCesDhcpv6ClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6ClientMIBNotificationPrefix=_CienaCesDhcpv6ClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,30))
_CienaCesDhcpv6ClientMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesDhcpv6ClientMIBNotifications=_CienaCesDhcpv6ClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,30,0))
mibBuilder.exportSymbols(_C,**{'cienaCesDhcpv6ClientMIB':cienaCesDhcpv6ClientMIB,'cienaCesDhcpv6ClientMIBObjects':cienaCesDhcpv6ClientMIBObjects,'cienaCesDhcpv6Client':cienaCesDhcpv6Client,'cienaCesDhcpv6AdminState':cienaCesDhcpv6AdminState,'cienaCesDhcpv6IfName':cienaCesDhcpv6IfName,'cienaCesDhcpv6RapidCommitState':cienaCesDhcpv6RapidCommitState,'cienaCesDhcpv6PrefLifetimeReq':cienaCesDhcpv6PrefLifetimeReq,'cienaCesDhcpv6ValidLifetimeReq':cienaCesDhcpv6ValidLifetimeReq,'cienaCesDhcpv6ClientOptionTable':cienaCesDhcpv6ClientOptionTable,'cienaCesDhcpv6ClientOptionEntry':cienaCesDhcpv6ClientOptionEntry,_Z:cienaCesDhcpv6OptionCodeIndex,'cienaCesDhcpv6OptionDesc':cienaCesDhcpv6OptionDesc,'cienaCesDhcpv6OptionCode':cienaCesDhcpv6OptionCode,'cienaCesDhcpv6OptionState':cienaCesDhcpv6OptionState,'cienaCesDhcpv6ClientSessTable':cienaCesDhcpv6ClientSessTable,'cienaCesDhcpv6ClientSessEntry':cienaCesDhcpv6ClientSessEntry,_a:cienaCesDhcpv6ClientSessMgmtIntfIndex,'cienaCesDhcpv6ClientSessState':cienaCesDhcpv6ClientSessState,'cienaCesDhcpv6ClientSessAutoConfigState':cienaCesDhcpv6ClientSessAutoConfigState,'cienaCesDhcpv6ClientSessUpTime':cienaCesDhcpv6ClientSessUpTime,'cienaCesDhcpv6ClientSessPrefLifetime':cienaCesDhcpv6ClientSessPrefLifetime,'cienaCesDhcpv6ClientSessValidLifetime':cienaCesDhcpv6ClientSessValidLifetime,'cienaCesDhcpv6ClientSessLeaseExpire':cienaCesDhcpv6ClientSessLeaseExpire,'cienaCesDhcpv6ClientSessClientId':cienaCesDhcpv6ClientSessClientId,'cienaCesDhcpv6ClientSessServerIpAddrType':cienaCesDhcpv6ClientSessServerIpAddrType,'cienaCesDhcpv6ClientSessServerIpAddr':cienaCesDhcpv6ClientSessServerIpAddr,'cienaCesDhcpv6ClientSessServerId':cienaCesDhcpv6ClientSessServerId,'cienaCesDhcpv6ClientSessT1Time':cienaCesDhcpv6ClientSessT1Time,'cienaCesDhcpv6ClientSessT2Time':cienaCesDhcpv6ClientSessT2Time,'cienaCesDhcpv6ClientSessStatsTable':cienaCesDhcpv6ClientSessStatsTable,'cienaCesDhcpv6ClientSessStatsEntry':cienaCesDhcpv6ClientSessStatsEntry,_c:cienaCesDhcpv6ClientSessStatsMgmtIntfIndex,'cienaCesDhcpv6ClientSessStatsClear':cienaCesDhcpv6ClientSessStatsClear,'cienaCesDhcpv6ClientSessStatsPktsRx':cienaCesDhcpv6ClientSessStatsPktsRx,'cienaCesDhcpv6ClientSessStatsReply':cienaCesDhcpv6ClientSessStatsReply,'cienaCesDhcpv6ClientSessStatsAdvert':cienaCesDhcpv6ClientSessStatsAdvert,'cienaCesDhcpv6ClientSessStatsRecfg':cienaCesDhcpv6ClientSessStatsRecfg,'cienaCesDhcpv6ClientSessStatsInvalid':cienaCesDhcpv6ClientSessStatsInvalid,'cienaCesDhcpv6ClientSessStatsPktsTx':cienaCesDhcpv6ClientSessStatsPktsTx,'cienaCesDhcpv6ClientSessStatsSolicit':cienaCesDhcpv6ClientSessStatsSolicit,'cienaCesDhcpv6ClientSessStatsRequest':cienaCesDhcpv6ClientSessStatsRequest,'cienaCesDhcpv6ClientSessStatsConfirm':cienaCesDhcpv6ClientSessStatsConfirm,'cienaCesDhcpv6ClientSessStatsRenew':cienaCesDhcpv6ClientSessStatsRenew,'cienaCesDhcpv6ClientSessStatsRebind':cienaCesDhcpv6ClientSessStatsRebind,'cienaCesDhcpv6ClientSessStatsInfoReq':cienaCesDhcpv6ClientSessStatsInfoReq,'cienaCesDhcpv6ClientSessStatsRelease':cienaCesDhcpv6ClientSessStatsRelease,'cienaCesDhcpv6ClientSessStatsDecline':cienaCesDhcpv6ClientSessStatsDecline,'cienaCesDhcpv6ClientSessStatsTxFail':cienaCesDhcpv6ClientSessStatsTxFail,'cienaCesDhcpv6RelayAgent':cienaCesDhcpv6RelayAgent,'cienaCesDhcpv6RelayAgentGlobalAttrs':cienaCesDhcpv6RelayAgentGlobalAttrs,'cienaCesDhcpv6LdraState':cienaCesDhcpv6LdraState,'cienaCesDhcpv6LdraInterfaceId':cienaCesDhcpv6LdraInterfaceId,'cienaCesDhcpv6LdraRemoteId':cienaCesDhcpv6LdraRemoteId,'cienaCesDhcpv6LdraRemoteIdOption':cienaCesDhcpv6LdraRemoteIdOption,'cienaCesDhcpv6LdraRemoteIdEnterpriseNo':cienaCesDhcpv6LdraRemoteIdEnterpriseNo,'cienaCesDhcpv6LdraForward':cienaCesDhcpv6LdraForward,'cienaCesDhcpv6LdraRelayed':cienaCesDhcpv6LdraRelayed,'cienaCesDhcpv6LdraDropped':cienaCesDhcpv6LdraDropped,'cienaCesDhcpv6LdraGlobalStatsClear':cienaCesDhcpv6LdraGlobalStatsClear,'cienaCesDhcpv6LdraNotForRelay':cienaCesDhcpv6LdraNotForRelay,'cienaCesDhcpv6LdraStateTable':cienaCesDhcpv6LdraStateTable,'cienaCesDhcpv6LdraStateEntry':cienaCesDhcpv6LdraStateEntry,_I:cienaCesDhcpv6LdraVlan,'cienaCesDhcpv6LdraAdminState':cienaCesDhcpv6LdraAdminState,'cienaCesDhcpv6LdraOperState':cienaCesDhcpv6LdraOperState,'cienaCesDhcpv6LdraRowStatus':cienaCesDhcpv6LdraRowStatus,'cienaCesDhcpv6LdraTrustTable':cienaCesDhcpv6LdraTrustTable,'cienaCesDhcpv6LdraTrustEntry':cienaCesDhcpv6LdraTrustEntry,_W:cienaCesDhcpv6LdraPort,'cienaCesDhcpv6LdraTrustMode':cienaCesDhcpv6LdraTrustMode,'cienaCesDhcpv6LdraStatsTable':cienaCesDhcpv6LdraStatsTable,'cienaCesDhcpv6LdraStatsEntry':cienaCesDhcpv6LdraStatsEntry,'cienaCesDhcpv6LdraPktsForRelay':cienaCesDhcpv6LdraPktsForRelay,'cienaCesDhcpv6LdraRelayedClient':cienaCesDhcpv6LdraRelayedClient,'cienaCesDhcpv6LdraRelayedServer':cienaCesDhcpv6LdraRelayedServer,'cienaCesDhcpv6LdraUntrustedClientPortPktsRx':cienaCesDhcpv6LdraUntrustedClientPortPktsRx,'cienaCesDhcpv6LdraUntrustedServerPortPktsRx':cienaCesDhcpv6LdraUntrustedServerPortPktsRx,'cienaCesDhcpv6LdraFailedValidationPktDrop':cienaCesDhcpv6LdraFailedValidationPktDrop,'cienaCesDhcpv6LdraInvalidConfigPktDrop':cienaCesDhcpv6LdraInvalidConfigPktDrop,'cienaCesDhcpv6LdraExceededHopCountPktDrop':cienaCesDhcpv6LdraExceededHopCountPktDrop,'cienaCesDhcpv6LdraExceedMTUPktDrop':cienaCesDhcpv6LdraExceedMTUPktDrop,'cienaCesDhcpv6LdraNoTrustedServerPktDrop':cienaCesDhcpv6LdraNoTrustedServerPktDrop,'cienaCesDhcpv6LdraNoTrustedClientPktDrop':cienaCesDhcpv6LdraNoTrustedClientPktDrop,'cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop':cienaCesDhcpv6LdraIPv6FragBadExtHdrPktDrop,'cienaCesDhcpv6LdraGeneralErrors':cienaCesDhcpv6LdraGeneralErrors,'cienaCesDhcpv6LdraStatsClear':cienaCesDhcpv6LdraStatsClear,'cienaCesDhcpv6LdraIntidStringTable':cienaCesDhcpv6LdraIntidStringTable,'cienaCesDhcpv6LdraIntidStringEntry':cienaCesDhcpv6LdraIntidStringEntry,_d:cienaCesDhcpv6LdraIntidStringPort,'cienaCesDhcpv6LdraIntidString':cienaCesDhcpv6LdraIntidString,'cienaCesDhcpv6LdraIntidStringRowStatus':cienaCesDhcpv6LdraIntidStringRowStatus,'cienaCesDhcpv6LdraRidStringTable':cienaCesDhcpv6LdraRidStringTable,'cienaCesDhcpv6LdraRidStringEntry':cienaCesDhcpv6LdraRidStringEntry,_e:cienaCesDhcpv6LdraRidStringPort,'cienaCesDhcpv6LdraRidString':cienaCesDhcpv6LdraRidString,'cienaCesDhcpv6LdraRidStringRowStatus':cienaCesDhcpv6LdraRidStringRowStatus,'cienaCesDhcpv6LdraExtTrustTable':cienaCesDhcpv6LdraExtTrustTable,'cienaCesDhcpv6LdraExtTrustEntry':cienaCesDhcpv6LdraExtTrustEntry,'cienaCesDhcpv6LdraExtPortState':cienaCesDhcpv6LdraExtPortState,'cienaCesDhcpv6LdraExtTrustMode':cienaCesDhcpv6LdraExtTrustMode,'cienaCesDhcpv6LdraVsStateTable':cienaCesDhcpv6LdraVsStateTable,'cienaCesDhcpv6LdraVsStateEntry':cienaCesDhcpv6LdraVsStateEntry,_S:cienaCesDhcpv6LdraVsVlan,'cienaCesDhcpv6LdraVsName':cienaCesDhcpv6LdraVsName,'cienaCesDhcpv6LdraVsAdminState':cienaCesDhcpv6LdraVsAdminState,'cienaCesDhcpv6LdraVsOperState':cienaCesDhcpv6LdraVsOperState,'cienaCesDhcpv6LdraVsRowStatus':cienaCesDhcpv6LdraVsRowStatus,'cienaCesDhcpv6LdraVsTrustTable':cienaCesDhcpv6LdraVsTrustTable,'cienaCesDhcpv6LdraVsTrustEntry':cienaCesDhcpv6LdraVsTrustEntry,_T:cienaCesDhcpv6LdraVsPort,_f:cienaCesDhcpv6LdraVsSubVlan,'cienaCesDhcpv6LdraVsPortState':cienaCesDhcpv6LdraVsPortState,'cienaCesDhcpv6LdraVsTrustMode':cienaCesDhcpv6LdraVsTrustMode,'cienaCesDhcpv6LdraVsStatsTable':cienaCesDhcpv6LdraVsStatsTable,'cienaCesDhcpv6LdraVsStatsEntry':cienaCesDhcpv6LdraVsStatsEntry,'cienaCesDhcpv6LdraVsPktsForRelay':cienaCesDhcpv6LdraVsPktsForRelay,'cienaCesDhcpv6LdraVsRelayedClient':cienaCesDhcpv6LdraVsRelayedClient,'cienaCesDhcpv6LdraVsRelayedServer':cienaCesDhcpv6LdraVsRelayedServer,'cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx':cienaCesDhcpv6LdraVsUntrustedClientPortPktsRx,'cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx':cienaCesDhcpv6LdraVsUntrustedServerPortPktsRx,'cienaCesDhcpv6LdraVsFailedValidationPktDrop':cienaCesDhcpv6LdraVsFailedValidationPktDrop,'cienaCesDhcpv6LdraVsInvalidConfigPktDrop':cienaCesDhcpv6LdraVsInvalidConfigPktDrop,'cienaCesDhcpv6LdraVsExceededHopCountPktDrop':cienaCesDhcpv6LdraVsExceededHopCountPktDrop,'cienaCesDhcpv6LdraVsExceedMTUPktDrop':cienaCesDhcpv6LdraVsExceedMTUPktDrop,'cienaCesDhcpv6LdraVsNoTrustedServerPktDrop':cienaCesDhcpv6LdraVsNoTrustedServerPktDrop,'cienaCesDhcpv6LdraVsNoTrustedClientPktDrop':cienaCesDhcpv6LdraVsNoTrustedClientPktDrop,'cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop':cienaCesDhcpv6LdraVsIPv6FragBadExtHdrPktDrop,'cienaCesDhcpv6LdraVsGeneralErrors':cienaCesDhcpv6LdraVsGeneralErrors,'cienaCesDhcpv6LdraVsStatsClear':cienaCesDhcpv6LdraVsStatsClear,'cienaCesDhcpv6LdraVsIntidStringTable':cienaCesDhcpv6LdraVsIntidStringTable,'cienaCesDhcpv6LdraVsIntidStringEntry':cienaCesDhcpv6LdraVsIntidStringEntry,'cienaCesDhcpv6LdraVsIntidString':cienaCesDhcpv6LdraVsIntidString,'cienaCesDhcpv6LdraVsIntidStringRowStatus':cienaCesDhcpv6LdraVsIntidStringRowStatus,'cienaCesDhcpv6LdraVsRidStringTable':cienaCesDhcpv6LdraVsRidStringTable,'cienaCesDhcpv6LdraVsRidStringEntry':cienaCesDhcpv6LdraVsRidStringEntry,'cienaCesDhcpv6LdraVsRidString':cienaCesDhcpv6LdraVsRidString,'cienaCesDhcpv6LdraVsRidStringRowStatus':cienaCesDhcpv6LdraVsRidStringRowStatus,'cienaCesDhcpv6LdraMplsStateTable':cienaCesDhcpv6LdraMplsStateTable,'cienaCesDhcpv6LdraMplsStateEntry':cienaCesDhcpv6LdraMplsStateEntry,_L:cienaCesDhcpv6LdraMplsId,'cienaCesDhcpv6LdraMplsName':cienaCesDhcpv6LdraMplsName,'cienaCesDhcpv6LdraMplsAdminState':cienaCesDhcpv6LdraMplsAdminState,'cienaCesDhcpv6LdraMplsOperState':cienaCesDhcpv6LdraMplsOperState,'cienaCesDhcpv6LdraMplsRowStatus':cienaCesDhcpv6LdraMplsRowStatus,'cienaCesDhcpv6LdraMplsTrustTable':cienaCesDhcpv6LdraMplsTrustTable,'cienaCesDhcpv6LdraMplsTrustEntry':cienaCesDhcpv6LdraMplsTrustEntry,_U:cienaCesDhcpv6LdraMplsInterface,'cienaCesDhcpv6LdraMplsVcName':cienaCesDhcpv6LdraMplsVcName,'cienaCesDhcpv6LdraMplsInterfaceState':cienaCesDhcpv6LdraMplsInterfaceState,'cienaCesDhcpv6LdraMplsTrustMode':cienaCesDhcpv6LdraMplsTrustMode,'cienaCesDhcpv6LdraMplsStatsTable':cienaCesDhcpv6LdraMplsStatsTable,'cienaCesDhcpv6LdraMplsStatsEntry':cienaCesDhcpv6LdraMplsStatsEntry,'cienaCesDhcpv6LdraMplsPktsForRelay':cienaCesDhcpv6LdraMplsPktsForRelay,'cienaCesDhcpv6LdraMplsRelayedClient':cienaCesDhcpv6LdraMplsRelayedClient,'cienaCesDhcpv6LdraMplsRelayedServer':cienaCesDhcpv6LdraMplsRelayedServer,'cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx':cienaCesDhcpv6LdraMplsUntrustedClientInterfacePktsRx,'cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx':cienaCesDhcpv6LdraMplsUntrustedServerInterfacePktsRx,'cienaCesDhcpv6LdraMplsFailedValidationPktDrop':cienaCesDhcpv6LdraMplsFailedValidationPktDrop,'cienaCesDhcpv6LdraMplsInvalidConfigPktDrop':cienaCesDhcpv6LdraMplsInvalidConfigPktDrop,'cienaCesDhcpv6LdraMplsExceededHopCountPktDrop':cienaCesDhcpv6LdraMplsExceededHopCountPktDrop,'cienaCesDhcpv6LdraMplsExceedMTUPktDrop':cienaCesDhcpv6LdraMplsExceedMTUPktDrop,'cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop':cienaCesDhcpv6LdraMplsNoTrustedServerPktDrop,'cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop':cienaCesDhcpv6LdraMplsNoTrustedClientPktDrop,'cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop':cienaCesDhcpv6LdraMplsIPv6FragBadExtHdrPktDrop,'cienaCesDhcpv6LdraMplsGeneralErrors':cienaCesDhcpv6LdraMplsGeneralErrors,'cienaCesDhcpv6LdraMplsStatsClear':cienaCesDhcpv6LdraMplsStatsClear,'cienaCesDhcpv6LdraMplsIntidStringTable':cienaCesDhcpv6LdraMplsIntidStringTable,'cienaCesDhcpv6LdraMplsIntidStringEntry':cienaCesDhcpv6LdraMplsIntidStringEntry,'cienaCesDhcpv6LdraMplsIntidString':cienaCesDhcpv6LdraMplsIntidString,'cienaCesDhcpv6LdraMplsIntidStringRowStatus':cienaCesDhcpv6LdraMplsIntidStringRowStatus,'cienaCesDhcpv6LdraMplsRidStringTable':cienaCesDhcpv6LdraMplsRidStringTable,'cienaCesDhcpv6LdraMplsRidStringEntry':cienaCesDhcpv6LdraMplsRidStringEntry,'cienaCesDhcpv6LdraMplsRidString':cienaCesDhcpv6LdraMplsRidString,'cienaCesDhcpv6LdraMplsRidStringRowStatus':cienaCesDhcpv6LdraMplsRidStringRowStatus,'cienaCesDhcpv6ClientMIBConformance':cienaCesDhcpv6ClientMIBConformance,'cienaCesDhcpv6ClientMIBCompliances':cienaCesDhcpv6ClientMIBCompliances,'cienaCesDhcpv6ClientMIBGroups':cienaCesDhcpv6ClientMIBGroups,'cienaCesDhcpv6ClientMIBNotificationPrefix':cienaCesDhcpv6ClientMIBNotificationPrefix,'cienaCesDhcpv6ClientMIBNotifications':cienaCesDhcpv6ClientMIBNotifications})