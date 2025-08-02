_K='fnVpnDialupIndex'
_J='fnIpSessIndex'
_I='fnVdIndex'
_H='fnUserIndex'
_G='fnAdminIndex'
_F='fnHaStatsIndex'
_E='Integer32'
_D='DisplayString'
_C='FORTINET-MIB-280'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class FnBoolState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
class FnIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class FnOpMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nat',1),('transparent',2)))
class FnHaMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standalone',1),('active-active',2),('active-passive',3)))
class FnHaSchedule(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),('hub',2),('least-connections',3),('round-robin',4),('weighted-round-robin',5),('random',6),('ip-based',7),('ip-port-based',8)))
class FnAdminPerm(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,15,255)));namedValues=NamedValues(*(('read-admin',0),('write-admin',1),('domain-admin',15),('super-admin',255)))
class FnUserAuth(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('radius-single',2),('radius-multiple',3),('ldap',4)))
class FnIfAddrMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('static',1))
class FnSessProto(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,12,17,22,41,46,47,50,51,89,103,108,255)));namedValues=NamedValues(*(('ip',0),('icmp',1),('igmp',2),('ipip',4),('tcp',6),('egp',8),('pup',12),('udp',17),('idp',22),('ipv6',41),('rsvp',46),('gre',47),('esp',50),('ah',51),('ospf',89),('pim',103),('comp',108),('raw',255)))
_Fortinet_ObjectIdentity=ObjectIdentity
fortinet=_Fortinet_ObjectIdentity((1,3,6,1,4,1,12356))
_FnTraps_ObjectIdentity=ObjectIdentity
fnTraps=_FnTraps_ObjectIdentity((1,3,6,1,4,1,12356,0))
_FnSystem_ObjectIdentity=ObjectIdentity
fnSystem=_FnSystem_ObjectIdentity((1,3,6,1,4,1,12356,1))
_FnSysModel_Type=Integer32
_FnSysModel_Object=MibScalar
fnSysModel=_FnSysModel_Object((1,3,6,1,4,1,12356,1,1),_FnSysModel_Type())
fnSysModel.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysModel.setStatus(_A)
class _FnSysSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FnSysSerial_Type.__name__=_D
_FnSysSerial_Object=MibScalar
fnSysSerial=_FnSysSerial_Object((1,3,6,1,4,1,12356,1,2),_FnSysSerial_Type())
fnSysSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysSerial.setStatus(_A)
class _FnSysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FnSysVersion_Type.__name__=_D
_FnSysVersion_Object=MibScalar
fnSysVersion=_FnSysVersion_Object((1,3,6,1,4,1,12356,1,3),_FnSysVersion_Type())
fnSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysVersion.setStatus(_A)
class _FnSysVersionAv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FnSysVersionAv_Type.__name__=_D
_FnSysVersionAv_Object=MibScalar
fnSysVersionAv=_FnSysVersionAv_Object((1,3,6,1,4,1,12356,1,4),_FnSysVersionAv_Type())
fnSysVersionAv.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysVersionAv.setStatus(_A)
class _FnSysVersionNids_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FnSysVersionNids_Type.__name__=_D
_FnSysVersionNids_Object=MibScalar
fnSysVersionNids=_FnSysVersionNids_Object((1,3,6,1,4,1,12356,1,5),_FnSysVersionNids_Type())
fnSysVersionNids.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysVersionNids.setStatus(_A)
_FnSysHaMode_Type=FnHaMode
_FnSysHaMode_Object=MibScalar
fnSysHaMode=_FnSysHaMode_Object((1,3,6,1,4,1,12356,1,6),_FnSysHaMode_Type())
fnSysHaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysHaMode.setStatus(_A)
_FnSysOpMode_Type=FnOpMode
_FnSysOpMode_Object=MibScalar
fnSysOpMode=_FnSysOpMode_Object((1,3,6,1,4,1,12356,1,7),_FnSysOpMode_Type())
fnSysOpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysOpMode.setStatus(_A)
_FnSysCpuUsage_Type=Gauge32
_FnSysCpuUsage_Object=MibScalar
fnSysCpuUsage=_FnSysCpuUsage_Object((1,3,6,1,4,1,12356,1,8),_FnSysCpuUsage_Type())
fnSysCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysCpuUsage.setStatus(_A)
_FnSysMemUsage_Type=Gauge32
_FnSysMemUsage_Object=MibScalar
fnSysMemUsage=_FnSysMemUsage_Object((1,3,6,1,4,1,12356,1,9),_FnSysMemUsage_Type())
fnSysMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysMemUsage.setStatus(_A)
_FnSysSesCount_Type=Gauge32
_FnSysSesCount_Object=MibScalar
fnSysSesCount=_FnSysSesCount_Object((1,3,6,1,4,1,12356,1,10),_FnSysSesCount_Type())
fnSysSesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fnSysSesCount.setStatus(_A)
_FnHa_ObjectIdentity=ObjectIdentity
fnHa=_FnHa_ObjectIdentity((1,3,6,1,4,1,12356,1,100))
_FnHaGroupId_Type=Integer32
_FnHaGroupId_Object=MibScalar
fnHaGroupId=_FnHaGroupId_Object((1,3,6,1,4,1,12356,1,100,1),_FnHaGroupId_Type())
fnHaGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaGroupId.setStatus(_A)
class _FnHaPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FnHaPriority_Type.__name__=_E
_FnHaPriority_Object=MibScalar
fnHaPriority=_FnHaPriority_Object((1,3,6,1,4,1,12356,1,100,2),_FnHaPriority_Type())
fnHaPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaPriority.setStatus(_A)
_FnHaOverride_Type=FnBoolState
_FnHaOverride_Object=MibScalar
fnHaOverride=_FnHaOverride_Object((1,3,6,1,4,1,12356,1,100,3),_FnHaOverride_Type())
fnHaOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaOverride.setStatus(_A)
_FnHaAutoSync_Type=FnBoolState
_FnHaAutoSync_Object=MibScalar
fnHaAutoSync=_FnHaAutoSync_Object((1,3,6,1,4,1,12356,1,100,4),_FnHaAutoSync_Type())
fnHaAutoSync.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaAutoSync.setStatus(_A)
_FnHaSchedule_Type=FnHaSchedule
_FnHaSchedule_Object=MibScalar
fnHaSchedule=_FnHaSchedule_Object((1,3,6,1,4,1,12356,1,100,5),_FnHaSchedule_Type())
fnHaSchedule.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaSchedule.setStatus(_A)
_FnHaStatsTable_Object=MibTable
fnHaStatsTable=_FnHaStatsTable_Object((1,3,6,1,4,1,12356,1,100,6))
if mibBuilder.loadTexts:fnHaStatsTable.setStatus(_A)
_FnHaStatsEntry_Object=MibTableRow
fnHaStatsEntry=_FnHaStatsEntry_Object((1,3,6,1,4,1,12356,1,100,6,1))
fnHaStatsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:fnHaStatsEntry.setStatus(_A)
_FnHaStatsIndex_Type=FnIndex
_FnHaStatsIndex_Object=MibTableColumn
fnHaStatsIndex=_FnHaStatsIndex_Object((1,3,6,1,4,1,12356,1,100,6,1,1),_FnHaStatsIndex_Type())
fnHaStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsIndex.setStatus(_A)
class _FnHaStatsSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FnHaStatsSerial_Type.__name__=_D
_FnHaStatsSerial_Object=MibTableColumn
fnHaStatsSerial=_FnHaStatsSerial_Object((1,3,6,1,4,1,12356,1,100,6,1,2),_FnHaStatsSerial_Type())
fnHaStatsSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsSerial.setStatus(_A)
_FnHaStatsCpuUsage_Type=Gauge32
_FnHaStatsCpuUsage_Object=MibTableColumn
fnHaStatsCpuUsage=_FnHaStatsCpuUsage_Object((1,3,6,1,4,1,12356,1,100,6,1,3),_FnHaStatsCpuUsage_Type())
fnHaStatsCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsCpuUsage.setStatus(_A)
_FnHaStatsMemUsage_Type=Gauge32
_FnHaStatsMemUsage_Object=MibTableColumn
fnHaStatsMemUsage=_FnHaStatsMemUsage_Object((1,3,6,1,4,1,12356,1,100,6,1,4),_FnHaStatsMemUsage_Type())
fnHaStatsMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsMemUsage.setStatus(_A)
_FnHaStatsNetUsage_Type=Gauge32
_FnHaStatsNetUsage_Object=MibTableColumn
fnHaStatsNetUsage=_FnHaStatsNetUsage_Object((1,3,6,1,4,1,12356,1,100,6,1,5),_FnHaStatsNetUsage_Type())
fnHaStatsNetUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsNetUsage.setStatus(_A)
_FnHaStatsSesCount_Type=Gauge32
_FnHaStatsSesCount_Object=MibTableColumn
fnHaStatsSesCount=_FnHaStatsSesCount_Object((1,3,6,1,4,1,12356,1,100,6,1,6),_FnHaStatsSesCount_Type())
fnHaStatsSesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsSesCount.setStatus(_A)
_FnHaStatsPktCount_Type=Counter32
_FnHaStatsPktCount_Object=MibTableColumn
fnHaStatsPktCount=_FnHaStatsPktCount_Object((1,3,6,1,4,1,12356,1,100,6,1,7),_FnHaStatsPktCount_Type())
fnHaStatsPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsPktCount.setStatus(_A)
_FnHaStatsByteCount_Type=Counter32
_FnHaStatsByteCount_Object=MibTableColumn
fnHaStatsByteCount=_FnHaStatsByteCount_Object((1,3,6,1,4,1,12356,1,100,6,1,8),_FnHaStatsByteCount_Type())
fnHaStatsByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsByteCount.setStatus(_A)
_FnHaStatsIdsCount_Type=Counter32
_FnHaStatsIdsCount_Object=MibTableColumn
fnHaStatsIdsCount=_FnHaStatsIdsCount_Object((1,3,6,1,4,1,12356,1,100,6,1,9),_FnHaStatsIdsCount_Type())
fnHaStatsIdsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsIdsCount.setStatus(_A)
_FnHaStatsAvCount_Type=Counter32
_FnHaStatsAvCount_Object=MibTableColumn
fnHaStatsAvCount=_FnHaStatsAvCount_Object((1,3,6,1,4,1,12356,1,100,6,1,10),_FnHaStatsAvCount_Type())
fnHaStatsAvCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fnHaStatsAvCount.setStatus(_A)
_FnAdmin_ObjectIdentity=ObjectIdentity
fnAdmin=_FnAdmin_ObjectIdentity((1,3,6,1,4,1,12356,1,101))
_FnAdminNumber_Type=Integer32
_FnAdminNumber_Object=MibScalar
fnAdminNumber=_FnAdminNumber_Object((1,3,6,1,4,1,12356,1,101,1),_FnAdminNumber_Type())
fnAdminNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fnAdminNumber.setStatus(_A)
_FnAdminTable_Object=MibTable
fnAdminTable=_FnAdminTable_Object((1,3,6,1,4,1,12356,1,101,2))
if mibBuilder.loadTexts:fnAdminTable.setStatus(_A)
_FnAdminEntry_Object=MibTableRow
fnAdminEntry=_FnAdminEntry_Object((1,3,6,1,4,1,12356,1,101,2,1))
fnAdminEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:fnAdminEntry.setStatus(_A)
_FnAdminIndex_Type=FnIndex
_FnAdminIndex_Object=MibTableColumn
fnAdminIndex=_FnAdminIndex_Object((1,3,6,1,4,1,12356,1,101,2,1,1),_FnAdminIndex_Type())
fnAdminIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnAdminIndex.setStatus(_A)
_FnAdminName_Type=DisplayString
_FnAdminName_Object=MibTableColumn
fnAdminName=_FnAdminName_Object((1,3,6,1,4,1,12356,1,101,2,1,2),_FnAdminName_Type())
fnAdminName.setMaxAccess(_B)
if mibBuilder.loadTexts:fnAdminName.setStatus(_A)
_FnAdminAddr_Type=IpAddress
_FnAdminAddr_Object=MibTableColumn
fnAdminAddr=_FnAdminAddr_Object((1,3,6,1,4,1,12356,1,101,2,1,3),_FnAdminAddr_Type())
fnAdminAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fnAdminAddr.setStatus(_A)
_FnAdminMask_Type=IpAddress
_FnAdminMask_Object=MibTableColumn
fnAdminMask=_FnAdminMask_Object((1,3,6,1,4,1,12356,1,101,2,1,4),_FnAdminMask_Type())
fnAdminMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fnAdminMask.setStatus(_A)
_FnAdminPerm_Type=FnAdminPerm
_FnAdminPerm_Object=MibTableColumn
fnAdminPerm=_FnAdminPerm_Object((1,3,6,1,4,1,12356,1,101,2,1,5),_FnAdminPerm_Type())
fnAdminPerm.setMaxAccess(_B)
if mibBuilder.loadTexts:fnAdminPerm.setStatus(_A)
_FnUsers_ObjectIdentity=ObjectIdentity
fnUsers=_FnUsers_ObjectIdentity((1,3,6,1,4,1,12356,1,102))
_FnUserNumber_Type=Integer32
_FnUserNumber_Object=MibScalar
fnUserNumber=_FnUserNumber_Object((1,3,6,1,4,1,12356,1,102,1),_FnUserNumber_Type())
fnUserNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fnUserNumber.setStatus(_A)
_FnUserTable_Object=MibTable
fnUserTable=_FnUserTable_Object((1,3,6,1,4,1,12356,1,102,2))
if mibBuilder.loadTexts:fnUserTable.setStatus(_A)
_FnUserEntry_Object=MibTableRow
fnUserEntry=_FnUserEntry_Object((1,3,6,1,4,1,12356,1,102,2,1))
fnUserEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:fnUserEntry.setStatus(_A)
_FnUserIndex_Type=FnIndex
_FnUserIndex_Object=MibTableColumn
fnUserIndex=_FnUserIndex_Object((1,3,6,1,4,1,12356,1,102,2,1,1),_FnUserIndex_Type())
fnUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnUserIndex.setStatus(_A)
_FnUserName_Type=DisplayString
_FnUserName_Object=MibTableColumn
fnUserName=_FnUserName_Object((1,3,6,1,4,1,12356,1,102,2,1,2),_FnUserName_Type())
fnUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:fnUserName.setStatus(_A)
_FnUserAuth_Type=FnUserAuth
_FnUserAuth_Object=MibTableColumn
fnUserAuth=_FnUserAuth_Object((1,3,6,1,4,1,12356,1,102,2,1,3),_FnUserAuth_Type())
fnUserAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:fnUserAuth.setStatus(_A)
_FnUserState_Type=FnBoolState
_FnUserState_Object=MibTableColumn
fnUserState=_FnUserState_Object((1,3,6,1,4,1,12356,1,102,2,1,4),_FnUserState_Type())
fnUserState.setMaxAccess(_B)
if mibBuilder.loadTexts:fnUserState.setStatus(_A)
_FnOptions_ObjectIdentity=ObjectIdentity
fnOptions=_FnOptions_ObjectIdentity((1,3,6,1,4,1,12356,1,103))
_FnOptIdleTimeout_Type=Integer32
_FnOptIdleTimeout_Object=MibScalar
fnOptIdleTimeout=_FnOptIdleTimeout_Object((1,3,6,1,4,1,12356,1,103,1),_FnOptIdleTimeout_Type())
fnOptIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fnOptIdleTimeout.setStatus(_A)
_FnLogging_ObjectIdentity=ObjectIdentity
fnLogging=_FnLogging_ObjectIdentity((1,3,6,1,4,1,12356,1,104))
_FnLogOption_Type=Integer32
_FnLogOption_Object=MibScalar
fnLogOption=_FnLogOption_Object((1,3,6,1,4,1,12356,1,104,1),_FnLogOption_Type())
fnLogOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fnLogOption.setStatus(_A)
_FnMessages_ObjectIdentity=ObjectIdentity
fnMessages=_FnMessages_ObjectIdentity((1,3,6,1,4,1,12356,1,105))
_FnMesgNumber_Type=Integer32
_FnMesgNumber_Object=MibScalar
fnMesgNumber=_FnMesgNumber_Object((1,3,6,1,4,1,12356,1,105,1),_FnMesgNumber_Type())
fnMesgNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fnMesgNumber.setStatus(_A)
_FnDomains_ObjectIdentity=ObjectIdentity
fnDomains=_FnDomains_ObjectIdentity((1,3,6,1,4,1,12356,2))
_FnVdNumber_Type=Integer32
_FnVdNumber_Object=MibScalar
fnVdNumber=_FnVdNumber_Object((1,3,6,1,4,1,12356,2,1),_FnVdNumber_Type())
fnVdNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVdNumber.setStatus(_A)
_FnVdTable_Object=MibTable
fnVdTable=_FnVdTable_Object((1,3,6,1,4,1,12356,2,2))
if mibBuilder.loadTexts:fnVdTable.setStatus(_A)
_FnVdEntry_Object=MibTableRow
fnVdEntry=_FnVdEntry_Object((1,3,6,1,4,1,12356,2,2,1))
fnVdEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:fnVdEntry.setStatus(_A)
_FnVdIndex_Type=FnIndex
_FnVdIndex_Object=MibTableColumn
fnVdIndex=_FnVdIndex_Object((1,3,6,1,4,1,12356,2,2,1,1),_FnVdIndex_Type())
fnVdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVdIndex.setStatus(_A)
_FnVdName_Type=DisplayString
_FnVdName_Object=MibTableColumn
fnVdName=_FnVdName_Object((1,3,6,1,4,1,12356,2,2,1,2),_FnVdName_Type())
fnVdName.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVdName.setStatus(_A)
_FnIp_ObjectIdentity=ObjectIdentity
fnIp=_FnIp_ObjectIdentity((1,3,6,1,4,1,12356,4))
_FnIpSessTable_Object=MibTable
fnIpSessTable=_FnIpSessTable_Object((1,3,6,1,4,1,12356,4,2))
if mibBuilder.loadTexts:fnIpSessTable.setStatus(_A)
_FnIpSessEntry_Object=MibTableRow
fnIpSessEntry=_FnIpSessEntry_Object((1,3,6,1,4,1,12356,4,2,1))
fnIpSessEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:fnIpSessEntry.setStatus(_A)
_FnIpSessIndex_Type=FnIndex
_FnIpSessIndex_Object=MibTableColumn
fnIpSessIndex=_FnIpSessIndex_Object((1,3,6,1,4,1,12356,4,2,1,1),_FnIpSessIndex_Type())
fnIpSessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessIndex.setStatus(_A)
_FnIpSessProto_Type=FnSessProto
_FnIpSessProto_Object=MibTableColumn
fnIpSessProto=_FnIpSessProto_Object((1,3,6,1,4,1,12356,4,2,1,2),_FnIpSessProto_Type())
fnIpSessProto.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessProto.setStatus(_A)
_FnIpSessFromAddr_Type=IpAddress
_FnIpSessFromAddr_Object=MibTableColumn
fnIpSessFromAddr=_FnIpSessFromAddr_Object((1,3,6,1,4,1,12356,4,2,1,3),_FnIpSessFromAddr_Type())
fnIpSessFromAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessFromAddr.setStatus(_A)
class _FnIpSessFromPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnIpSessFromPort_Type.__name__=_E
_FnIpSessFromPort_Object=MibTableColumn
fnIpSessFromPort=_FnIpSessFromPort_Object((1,3,6,1,4,1,12356,4,2,1,4),_FnIpSessFromPort_Type())
fnIpSessFromPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessFromPort.setStatus(_A)
_FnIpSessToAddr_Type=IpAddress
_FnIpSessToAddr_Object=MibTableColumn
fnIpSessToAddr=_FnIpSessToAddr_Object((1,3,6,1,4,1,12356,4,2,1,5),_FnIpSessToAddr_Type())
fnIpSessToAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessToAddr.setStatus(_A)
class _FnIpSessToPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FnIpSessToPort_Type.__name__=_E
_FnIpSessToPort_Object=MibTableColumn
fnIpSessToPort=_FnIpSessToPort_Object((1,3,6,1,4,1,12356,4,2,1,6),_FnIpSessToPort_Type())
fnIpSessToPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessToPort.setStatus(_A)
_FnIpSessExp_Type=Counter32
_FnIpSessExp_Object=MibTableColumn
fnIpSessExp=_FnIpSessExp_Object((1,3,6,1,4,1,12356,4,2,1,7),_FnIpSessExp_Type())
fnIpSessExp.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpSessExp.setStatus(_A)
_FnVpn_ObjectIdentity=ObjectIdentity
fnVpn=_FnVpn_ObjectIdentity((1,3,6,1,4,1,12356,9))
_FnVpnDialupTable_Object=MibTable
fnVpnDialupTable=_FnVpnDialupTable_Object((1,3,6,1,4,1,12356,9,1))
if mibBuilder.loadTexts:fnVpnDialupTable.setStatus(_A)
_FnVpnDialupEntry_Object=MibTableRow
fnVpnDialupEntry=_FnVpnDialupEntry_Object((1,3,6,1,4,1,12356,9,1,1))
fnVpnDialupEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:fnVpnDialupEntry.setStatus(_A)
_FnVpnDialupIndex_Type=FnIndex
_FnVpnDialupIndex_Object=MibTableColumn
fnVpnDialupIndex=_FnVpnDialupIndex_Object((1,3,6,1,4,1,12356,9,1,1,1),_FnVpnDialupIndex_Type())
fnVpnDialupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupIndex.setStatus(_A)
_FnVpnDialupGateway_Type=IpAddress
_FnVpnDialupGateway_Object=MibTableColumn
fnVpnDialupGateway=_FnVpnDialupGateway_Object((1,3,6,1,4,1,12356,9,1,1,2),_FnVpnDialupGateway_Type())
fnVpnDialupGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupGateway.setStatus(_A)
_FnVpnDialupLifetime_Type=Integer32
_FnVpnDialupLifetime_Object=MibTableColumn
fnVpnDialupLifetime=_FnVpnDialupLifetime_Object((1,3,6,1,4,1,12356,9,1,1,3),_FnVpnDialupLifetime_Type())
fnVpnDialupLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupLifetime.setStatus(_A)
_FnVpnDialupTimeout_Type=Integer32
_FnVpnDialupTimeout_Object=MibTableColumn
fnVpnDialupTimeout=_FnVpnDialupTimeout_Object((1,3,6,1,4,1,12356,9,1,1,4),_FnVpnDialupTimeout_Type())
fnVpnDialupTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupTimeout.setStatus(_A)
_FnVpnDialupSrcBegin_Type=IpAddress
_FnVpnDialupSrcBegin_Object=MibTableColumn
fnVpnDialupSrcBegin=_FnVpnDialupSrcBegin_Object((1,3,6,1,4,1,12356,9,1,1,5),_FnVpnDialupSrcBegin_Type())
fnVpnDialupSrcBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupSrcBegin.setStatus(_A)
_FnVpnDialupSrcEnd_Type=IpAddress
_FnVpnDialupSrcEnd_Object=MibTableColumn
fnVpnDialupSrcEnd=_FnVpnDialupSrcEnd_Object((1,3,6,1,4,1,12356,9,1,1,6),_FnVpnDialupSrcEnd_Type())
fnVpnDialupSrcEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupSrcEnd.setStatus(_A)
_FnVpnDialupDstAddr_Type=IpAddress
_FnVpnDialupDstAddr_Object=MibTableColumn
fnVpnDialupDstAddr=_FnVpnDialupDstAddr_Object((1,3,6,1,4,1,12356,9,1,1,7),_FnVpnDialupDstAddr_Type())
fnVpnDialupDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fnVpnDialupDstAddr.setStatus(_A)
_FnIps_ObjectIdentity=ObjectIdentity
fnIps=_FnIps_ObjectIdentity((1,3,6,1,4,1,12356,12))
_FnIpsSigId_Type=FnIndex
_FnIpsSigId_Object=MibScalar
fnIpsSigId=_FnIpsSigId_Object((1,3,6,1,4,1,12356,12,1),_FnIpsSigId_Type())
fnIpsSigId.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpsSigId.setStatus(_A)
_FnIpsSigSrcIp_Type=IpAddress
_FnIpsSigSrcIp_Object=MibScalar
fnIpsSigSrcIp=_FnIpsSigSrcIp_Object((1,3,6,1,4,1,12356,12,2),_FnIpsSigSrcIp_Type())
fnIpsSigSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fnIpsSigSrcIp.setStatus(_A)
_FnBridge_ObjectIdentity=ObjectIdentity
fnBridge=_FnBridge_ObjectIdentity((1,3,6,1,4,1,12356,15))
_FnBridgeFgtFailure_Type=DisplayString
_FnBridgeFgtFailure_Object=MibScalar
fnBridgeFgtFailure=_FnBridgeFgtFailure_Object((1,3,6,1,4,1,12356,15,1),_FnBridgeFgtFailure_Type())
fnBridgeFgtFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:fnBridgeFgtFailure.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FnBoolState':FnBoolState,'FnIndex':FnIndex,'FnOpMode':FnOpMode,'FnHaMode':FnHaMode,'FnHaSchedule':FnHaSchedule,'FnAdminPerm':FnAdminPerm,'FnUserAuth':FnUserAuth,'FnIfAddrMode':FnIfAddrMode,'FnSessProto':FnSessProto,'fortinet':fortinet,'fnTraps':fnTraps,'fnSystem':fnSystem,'fnSysModel':fnSysModel,'fnSysSerial':fnSysSerial,'fnSysVersion':fnSysVersion,'fnSysVersionAv':fnSysVersionAv,'fnSysVersionNids':fnSysVersionNids,'fnSysHaMode':fnSysHaMode,'fnSysOpMode':fnSysOpMode,'fnSysCpuUsage':fnSysCpuUsage,'fnSysMemUsage':fnSysMemUsage,'fnSysSesCount':fnSysSesCount,'fnHa':fnHa,'fnHaGroupId':fnHaGroupId,'fnHaPriority':fnHaPriority,'fnHaOverride':fnHaOverride,'fnHaAutoSync':fnHaAutoSync,'fnHaSchedule':fnHaSchedule,'fnHaStatsTable':fnHaStatsTable,'fnHaStatsEntry':fnHaStatsEntry,_F:fnHaStatsIndex,'fnHaStatsSerial':fnHaStatsSerial,'fnHaStatsCpuUsage':fnHaStatsCpuUsage,'fnHaStatsMemUsage':fnHaStatsMemUsage,'fnHaStatsNetUsage':fnHaStatsNetUsage,'fnHaStatsSesCount':fnHaStatsSesCount,'fnHaStatsPktCount':fnHaStatsPktCount,'fnHaStatsByteCount':fnHaStatsByteCount,'fnHaStatsIdsCount':fnHaStatsIdsCount,'fnHaStatsAvCount':fnHaStatsAvCount,'fnAdmin':fnAdmin,'fnAdminNumber':fnAdminNumber,'fnAdminTable':fnAdminTable,'fnAdminEntry':fnAdminEntry,_G:fnAdminIndex,'fnAdminName':fnAdminName,'fnAdminAddr':fnAdminAddr,'fnAdminMask':fnAdminMask,'fnAdminPerm':fnAdminPerm,'fnUsers':fnUsers,'fnUserNumber':fnUserNumber,'fnUserTable':fnUserTable,'fnUserEntry':fnUserEntry,_H:fnUserIndex,'fnUserName':fnUserName,'fnUserAuth':fnUserAuth,'fnUserState':fnUserState,'fnOptions':fnOptions,'fnOptIdleTimeout':fnOptIdleTimeout,'fnLogging':fnLogging,'fnLogOption':fnLogOption,'fnMessages':fnMessages,'fnMesgNumber':fnMesgNumber,'fnDomains':fnDomains,'fnVdNumber':fnVdNumber,'fnVdTable':fnVdTable,'fnVdEntry':fnVdEntry,_I:fnVdIndex,'fnVdName':fnVdName,'fnIp':fnIp,'fnIpSessTable':fnIpSessTable,'fnIpSessEntry':fnIpSessEntry,_J:fnIpSessIndex,'fnIpSessProto':fnIpSessProto,'fnIpSessFromAddr':fnIpSessFromAddr,'fnIpSessFromPort':fnIpSessFromPort,'fnIpSessToAddr':fnIpSessToAddr,'fnIpSessToPort':fnIpSessToPort,'fnIpSessExp':fnIpSessExp,'fnVpn':fnVpn,'fnVpnDialupTable':fnVpnDialupTable,'fnVpnDialupEntry':fnVpnDialupEntry,_K:fnVpnDialupIndex,'fnVpnDialupGateway':fnVpnDialupGateway,'fnVpnDialupLifetime':fnVpnDialupLifetime,'fnVpnDialupTimeout':fnVpnDialupTimeout,'fnVpnDialupSrcBegin':fnVpnDialupSrcBegin,'fnVpnDialupSrcEnd':fnVpnDialupSrcEnd,'fnVpnDialupDstAddr':fnVpnDialupDstAddr,'fnIps':fnIps,'fnIpsSigId':fnIpsSigId,'fnIpsSigSrcIp':fnIpsSigSrcIp,'fnBridge':fnBridge,'fnBridgeFgtFailure':fnBridgeFgtFailure})