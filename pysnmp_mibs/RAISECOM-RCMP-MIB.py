_H='raisecomRcmpMacAddress'
_G='RAISECOM-RCMP-MIB'
_F='EnableVar'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomCluster,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomCluster')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_F)
raisecomRcmp=ModuleIdentity((1,3,6,1,4,1,8886,1,6,1))
if mibBuilder.loadTexts:raisecomRcmp.setRevisions(('1904-12-21 00:00',))
class _RaisecomRcmpClusterEnable_Type(EnableVar):defaultValue=2
_RaisecomRcmpClusterEnable_Type.__name__=_F
_RaisecomRcmpClusterEnable_Object=MibScalar
raisecomRcmpClusterEnable=_RaisecomRcmpClusterEnable_Object((1,3,6,1,4,1,8886,1,6,1,1),_RaisecomRcmpClusterEnable_Type())
raisecomRcmpClusterEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpClusterEnable.setStatus(_A)
class _RaisecomRcmpIdentity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('member',1),('candidate',2),('commander',3)))
_RaisecomRcmpIdentity_Type.__name__=_D
_RaisecomRcmpIdentity_Object=MibScalar
raisecomRcmpIdentity=_RaisecomRcmpIdentity_Object((1,3,6,1,4,1,8886,1,6,1,2),_RaisecomRcmpIdentity_Type())
raisecomRcmpIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpIdentity.setStatus(_A)
_RaisecomRcmpCommanderMac_Type=MacAddress
_RaisecomRcmpCommanderMac_Object=MibScalar
raisecomRcmpCommanderMac=_RaisecomRcmpCommanderMac_Object((1,3,6,1,4,1,8886,1,6,1,3),_RaisecomRcmpCommanderMac_Type())
raisecomRcmpCommanderMac.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpCommanderMac.setStatus(_A)
class _RaisecomRcmpAutoActiveEnable_Type(EnableVar):defaultValue=2
_RaisecomRcmpAutoActiveEnable_Type.__name__=_F
_RaisecomRcmpAutoActiveEnable_Object=MibScalar
raisecomRcmpAutoActiveEnable=_RaisecomRcmpAutoActiveEnable_Object((1,3,6,1,4,1,8886,1,6,1,4),_RaisecomRcmpAutoActiveEnable_Type())
raisecomRcmpAutoActiveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpAutoActiveEnable.setStatus(_A)
_RaisecomRcmpAutoActiveCommanderMac_Type=MacAddress
_RaisecomRcmpAutoActiveCommanderMac_Object=MibScalar
raisecomRcmpAutoActiveCommanderMac=_RaisecomRcmpAutoActiveCommanderMac_Object((1,3,6,1,4,1,8886,1,6,1,5),_RaisecomRcmpAutoActiveCommanderMac_Type())
raisecomRcmpAutoActiveCommanderMac.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpAutoActiveCommanderMac.setStatus(_A)
_RaisecomRcmpMemberTable_Object=MibTable
raisecomRcmpMemberTable=_RaisecomRcmpMemberTable_Object((1,3,6,1,4,1,8886,1,6,1,6))
if mibBuilder.loadTexts:raisecomRcmpMemberTable.setStatus(_A)
_RaisecomRcmpMemberEntry_Object=MibTableRow
raisecomRcmpMemberEntry=_RaisecomRcmpMemberEntry_Object((1,3,6,1,4,1,8886,1,6,1,6,1))
raisecomRcmpMemberEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:raisecomRcmpMemberEntry.setStatus(_A)
_RaisecomRcmpMacAddress_Type=MacAddress
_RaisecomRcmpMacAddress_Object=MibTableColumn
raisecomRcmpMacAddress=_RaisecomRcmpMacAddress_Object((1,3,6,1,4,1,8886,1,6,1,6,1,1),_RaisecomRcmpMacAddress_Type())
raisecomRcmpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpMacAddress.setStatus(_A)
_RaisecomRcmpHostName_Type=OctetString
_RaisecomRcmpHostName_Object=MibTableColumn
raisecomRcmpHostName=_RaisecomRcmpHostName_Object((1,3,6,1,4,1,8886,1,6,1,6,1,2),_RaisecomRcmpHostName_Type())
raisecomRcmpHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpHostName.setStatus(_A)
_RaisecomRcmpActiveEnable_Type=EnableVar
_RaisecomRcmpActiveEnable_Object=MibTableColumn
raisecomRcmpActiveEnable=_RaisecomRcmpActiveEnable_Object((1,3,6,1,4,1,8886,1,6,1,6,1,3),_RaisecomRcmpActiveEnable_Type())
raisecomRcmpActiveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpActiveEnable.setStatus(_A)
class _RaisecomRcmpOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_RaisecomRcmpOperationState_Type.__name__=_D
_RaisecomRcmpOperationState_Object=MibTableColumn
raisecomRcmpOperationState=_RaisecomRcmpOperationState_Object((1,3,6,1,4,1,8886,1,6,1,6,1,4),_RaisecomRcmpOperationState_Type())
raisecomRcmpOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpOperationState.setStatus(_A)
_RaisecomRcmpUdpPortNumber_Type=Integer32
_RaisecomRcmpUdpPortNumber_Object=MibTableColumn
raisecomRcmpUdpPortNumber=_RaisecomRcmpUdpPortNumber_Object((1,3,6,1,4,1,8886,1,6,1,6,1,5),_RaisecomRcmpUdpPortNumber_Type())
raisecomRcmpUdpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpUdpPortNumber.setStatus(_A)
class _RaisecomRcmpUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RaisecomRcmpUserName_Type.__name__=_E
_RaisecomRcmpUserName_Object=MibTableColumn
raisecomRcmpUserName=_RaisecomRcmpUserName_Object((1,3,6,1,4,1,8886,1,6,1,6,1,6),_RaisecomRcmpUserName_Type())
raisecomRcmpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpUserName.setStatus(_A)
class _RaisecomRcmpPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_RaisecomRcmpPassword_Type.__name__=_E
_RaisecomRcmpPassword_Object=MibTableColumn
raisecomRcmpPassword=_RaisecomRcmpPassword_Object((1,3,6,1,4,1,8886,1,6,1,6,1,7),_RaisecomRcmpPassword_Type())
raisecomRcmpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpPassword.setStatus(_A)
_RaisecomRcmpRowStatus_Type=RowStatus
_RaisecomRcmpRowStatus_Object=MibTableColumn
raisecomRcmpRowStatus=_RaisecomRcmpRowStatus_Object((1,3,6,1,4,1,8886,1,6,1,6,1,8),_RaisecomRcmpRowStatus_Type())
raisecomRcmpRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:raisecomRcmpRowStatus.setStatus(_A)
class _RaisecomRcmpSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,600))
_RaisecomRcmpSessionTimeout_Type.__name__=_D
_RaisecomRcmpSessionTimeout_Object=MibScalar
raisecomRcmpSessionTimeout=_RaisecomRcmpSessionTimeout_Object((1,3,6,1,4,1,8886,1,6,1,7),_RaisecomRcmpSessionTimeout_Type())
raisecomRcmpSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpSessionTimeout.setStatus(_A)
class _RaisecomRcmpMaxSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_RaisecomRcmpMaxSession_Type.__name__=_D
_RaisecomRcmpMaxSession_Object=MibScalar
raisecomRcmpMaxSession=_RaisecomRcmpMaxSession_Object((1,3,6,1,4,1,8886,1,6,1,8),_RaisecomRcmpMaxSession_Type())
raisecomRcmpMaxSession.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpMaxSession.setStatus(_A)
class _RaisecomRcmpMaxSessionPerMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_RaisecomRcmpMaxSessionPerMember_Type.__name__=_D
_RaisecomRcmpMaxSessionPerMember_Object=MibScalar
raisecomRcmpMaxSessionPerMember=_RaisecomRcmpMaxSessionPerMember_Object((1,3,6,1,4,1,8886,1,6,1,9),_RaisecomRcmpMaxSessionPerMember_Type())
raisecomRcmpMaxSessionPerMember.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpMaxSessionPerMember.setStatus(_A)
class _RaisecomRcmpMaxMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_RaisecomRcmpMaxMember_Type.__name__=_D
_RaisecomRcmpMaxMember_Object=MibScalar
raisecomRcmpMaxMember=_RaisecomRcmpMaxMember_Object((1,3,6,1,4,1,8886,1,6,1,10),_RaisecomRcmpMaxMember_Type())
raisecomRcmpMaxMember.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpMaxMember.setStatus(_A)
_RaisecomRcmpID_Type=MacAddress
_RaisecomRcmpID_Object=MibScalar
raisecomRcmpID=_RaisecomRcmpID_Object((1,3,6,1,4,1,8886,1,6,1,11),_RaisecomRcmpID_Type())
raisecomRcmpID.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpID.setStatus(_A)
_RaisecomRcmpStatisticsTotalSession_Type=Counter32
_RaisecomRcmpStatisticsTotalSession_Object=MibScalar
raisecomRcmpStatisticsTotalSession=_RaisecomRcmpStatisticsTotalSession_Object((1,3,6,1,4,1,8886,1,6,1,12),_RaisecomRcmpStatisticsTotalSession_Type())
raisecomRcmpStatisticsTotalSession.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsTotalSession.setStatus(_A)
_RaisecomRcmpStatisticsCurrentSession_Type=Counter32
_RaisecomRcmpStatisticsCurrentSession_Object=MibScalar
raisecomRcmpStatisticsCurrentSession=_RaisecomRcmpStatisticsCurrentSession_Object((1,3,6,1,4,1,8886,1,6,1,13),_RaisecomRcmpStatisticsCurrentSession_Type())
raisecomRcmpStatisticsCurrentSession.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsCurrentSession.setStatus(_A)
_RaisecomRcmpStatisticsMaxSession_Type=Counter32
_RaisecomRcmpStatisticsMaxSession_Object=MibScalar
raisecomRcmpStatisticsMaxSession=_RaisecomRcmpStatisticsMaxSession_Object((1,3,6,1,4,1,8886,1,6,1,14),_RaisecomRcmpStatisticsMaxSession_Type())
raisecomRcmpStatisticsMaxSession.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsMaxSession.setStatus(_A)
_RaisecomRcmpStatisticsTimeoutSession_Type=Counter32
_RaisecomRcmpStatisticsTimeoutSession_Object=MibScalar
raisecomRcmpStatisticsTimeoutSession=_RaisecomRcmpStatisticsTimeoutSession_Object((1,3,6,1,4,1,8886,1,6,1,15),_RaisecomRcmpStatisticsTimeoutSession_Type())
raisecomRcmpStatisticsTimeoutSession.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsTimeoutSession.setStatus(_A)
_RaisecomRcmpStatisticsInPkts_Type=Counter32
_RaisecomRcmpStatisticsInPkts_Object=MibScalar
raisecomRcmpStatisticsInPkts=_RaisecomRcmpStatisticsInPkts_Object((1,3,6,1,4,1,8886,1,6,1,16),_RaisecomRcmpStatisticsInPkts_Type())
raisecomRcmpStatisticsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsInPkts.setStatus(_A)
_RaisecomRcmpStatisticsOutPkts_Type=Counter32
_RaisecomRcmpStatisticsOutPkts_Object=MibScalar
raisecomRcmpStatisticsOutPkts=_RaisecomRcmpStatisticsOutPkts_Object((1,3,6,1,4,1,8886,1,6,1,17),_RaisecomRcmpStatisticsOutPkts_Type())
raisecomRcmpStatisticsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsOutPkts.setStatus(_A)
_RaisecomRcmpStatisticsDiscardPkts_Type=Counter32
_RaisecomRcmpStatisticsDiscardPkts_Object=MibScalar
raisecomRcmpStatisticsDiscardPkts=_RaisecomRcmpStatisticsDiscardPkts_Object((1,3,6,1,4,1,8886,1,6,1,18),_RaisecomRcmpStatisticsDiscardPkts_Type())
raisecomRcmpStatisticsDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsDiscardPkts.setStatus(_A)
_RaisecomRcmpStatisticsErrorPkts_Type=Counter32
_RaisecomRcmpStatisticsErrorPkts_Object=MibScalar
raisecomRcmpStatisticsErrorPkts=_RaisecomRcmpStatisticsErrorPkts_Object((1,3,6,1,4,1,8886,1,6,1,19),_RaisecomRcmpStatisticsErrorPkts_Type())
raisecomRcmpStatisticsErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpStatisticsErrorPkts.setStatus(_A)
_RaisecomRcmpDefaultVlan_Type=Integer32
_RaisecomRcmpDefaultVlan_Object=MibScalar
raisecomRcmpDefaultVlan=_RaisecomRcmpDefaultVlan_Object((1,3,6,1,4,1,8886,1,6,1,20),_RaisecomRcmpDefaultVlan_Type())
raisecomRcmpDefaultVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRcmpDefaultVlan.setStatus(_A)
class _RaisecomRcmpClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_RaisecomRcmpClearStatistics_Type.__name__=_D
_RaisecomRcmpClearStatistics_Object=MibScalar
raisecomRcmpClearStatistics=_RaisecomRcmpClearStatistics_Object((1,3,6,1,4,1,8886,1,6,1,21),_RaisecomRcmpClearStatistics_Type())
raisecomRcmpClearStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomRcmpClearStatistics.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'raisecomRcmp':raisecomRcmp,'raisecomRcmpClusterEnable':raisecomRcmpClusterEnable,'raisecomRcmpIdentity':raisecomRcmpIdentity,'raisecomRcmpCommanderMac':raisecomRcmpCommanderMac,'raisecomRcmpAutoActiveEnable':raisecomRcmpAutoActiveEnable,'raisecomRcmpAutoActiveCommanderMac':raisecomRcmpAutoActiveCommanderMac,'raisecomRcmpMemberTable':raisecomRcmpMemberTable,'raisecomRcmpMemberEntry':raisecomRcmpMemberEntry,_H:raisecomRcmpMacAddress,'raisecomRcmpHostName':raisecomRcmpHostName,'raisecomRcmpActiveEnable':raisecomRcmpActiveEnable,'raisecomRcmpOperationState':raisecomRcmpOperationState,'raisecomRcmpUdpPortNumber':raisecomRcmpUdpPortNumber,'raisecomRcmpUserName':raisecomRcmpUserName,'raisecomRcmpPassword':raisecomRcmpPassword,'raisecomRcmpRowStatus':raisecomRcmpRowStatus,'raisecomRcmpSessionTimeout':raisecomRcmpSessionTimeout,'raisecomRcmpMaxSession':raisecomRcmpMaxSession,'raisecomRcmpMaxSessionPerMember':raisecomRcmpMaxSessionPerMember,'raisecomRcmpMaxMember':raisecomRcmpMaxMember,'raisecomRcmpID':raisecomRcmpID,'raisecomRcmpStatisticsTotalSession':raisecomRcmpStatisticsTotalSession,'raisecomRcmpStatisticsCurrentSession':raisecomRcmpStatisticsCurrentSession,'raisecomRcmpStatisticsMaxSession':raisecomRcmpStatisticsMaxSession,'raisecomRcmpStatisticsTimeoutSession':raisecomRcmpStatisticsTimeoutSession,'raisecomRcmpStatisticsInPkts':raisecomRcmpStatisticsInPkts,'raisecomRcmpStatisticsOutPkts':raisecomRcmpStatisticsOutPkts,'raisecomRcmpStatisticsDiscardPkts':raisecomRcmpStatisticsDiscardPkts,'raisecomRcmpStatisticsErrorPkts':raisecomRcmpStatisticsErrorPkts,'raisecomRcmpDefaultVlan':raisecomRcmpDefaultVlan,'raisecomRcmpClearStatistics':raisecomRcmpClearStatistics})