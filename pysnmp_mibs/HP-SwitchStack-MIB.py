_A1='hpSwitchStackConfigGroup1'
_A0='hpSwitchStackConfigGroup'
_z='hpSwitchStackMemberPasswordLong'
_y='hpDiscoverStatsSwitchStatus'
_x='hpDiscoverStatsSwitchSystemName'
_w='hpDiscoverStatsSwitchMacAddr'
_v='hpDiscoverStatsSwitchStackName'
_u='hpDiscoverStatsCandidateDeviceType'
_t='hpDiscoverStatsCandidateSystemName'
_s='hpSwitchDiscoveryTransmissionInterval'
_r='hpSwitchDiscoveryAdminStatus'
_q='hpStackStatsMemberOperStatus'
_p='hpStackStatsMemberDeviceType'
_o='hpStackStatsMemberSystemName'
_n='hpStackStatsMemberMacAddr'
_m='hpStackStatsStackingStatus'
_l='hpStackStatsMgmtIpAddr'
_k='hpStackStatsMemberID'
_j='hpStackStatsMembersUnreachable'
_i='hpStackStatsMembersNum'
_h='hpStackStatsName'
_g='hpSwitchStackMemberPassword'
_f='undiscovered'
_e='unusedStatus'
_d='unknownFailure'
_c='remoteFailure'
_b='noReponse'
_a='joined'
_Z='hpDiscoverStatsGroup'
_Y='hpSwitchDiscoverConfigGroup'
_X='hpSwitchStackStatsGroup'
_W='hpSwitchStackMemberEntryStatus'
_V='hpSwitchStackMemberMacAddr'
_U='hpSwitchStackAutoGrab'
_T='hpSwitchStackAutoJoin'
_S='hpSwitchStackPropagate'
_R='hpSwitchStackName'
_Q='hpSwitchStackCommandAddr'
_P='hpSwitchStackAdminStatus'
_O='hpDiscoverStatsSwitchIndex'
_N='hpDiscoverStatsCandidateMacAddr'
_M='hpStackStatsMemberSwitchIndx'
_L='deprecated'
_K='pending'
_J='read-create'
_I='hpSwitchStackMemberSwitchNum'
_H='disable'
_G='enable'
_F='read-write'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='current'
_A='HP-SwitchStack-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpSwitchVirtualStackMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10))
if mibBuilder.loadTexts:hpSwitchVirtualStackMib.setRevisions(('2010-10-29 19:46','2000-11-03 23:44'))
_HpSwitchStackConfig_ObjectIdentity=ObjectIdentity
hpSwitchStackConfig=_HpSwitchStackConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10,1))
class _HpSwitchStackAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('candidate',1),('disabled',2),('member',3),('command',4),(_K,5)))
_HpSwitchStackAdminStatus_Type.__name__=_D
_HpSwitchStackAdminStatus_Object=MibScalar
hpSwitchStackAdminStatus=_HpSwitchStackAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,1,1),_HpSwitchStackAdminStatus_Type())
hpSwitchStackAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchStackAdminStatus.setStatus(_B)
_HpSwitchStackCommandAddr_Type=MacAddress
_HpSwitchStackCommandAddr_Object=MibScalar
hpSwitchStackCommandAddr=_HpSwitchStackCommandAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,1,2),_HpSwitchStackCommandAddr_Type())
hpSwitchStackCommandAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchStackCommandAddr.setStatus(_B)
class _HpSwitchStackName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpSwitchStackName_Type.__name__=_E
_HpSwitchStackName_Object=MibScalar
hpSwitchStackName=_HpSwitchStackName_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,1,3),_HpSwitchStackName_Type())
hpSwitchStackName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchStackName.setStatus(_B)
class _HpSwitchStackPropagate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpSwitchStackPropagate_Type.__name__=_D
_HpSwitchStackPropagate_Object=MibScalar
hpSwitchStackPropagate=_HpSwitchStackPropagate_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,1,4),_HpSwitchStackPropagate_Type())
hpSwitchStackPropagate.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchStackPropagate.setStatus(_B)
class _HpSwitchStackAutoJoin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpSwitchStackAutoJoin_Type.__name__=_D
_HpSwitchStackAutoJoin_Object=MibScalar
hpSwitchStackAutoJoin=_HpSwitchStackAutoJoin_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,1,5),_HpSwitchStackAutoJoin_Type())
hpSwitchStackAutoJoin.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchStackAutoJoin.setStatus(_B)
class _HpSwitchStackAutoGrab_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpSwitchStackAutoGrab_Type.__name__=_D
_HpSwitchStackAutoGrab_Object=MibScalar
hpSwitchStackAutoGrab=_HpSwitchStackAutoGrab_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,1,6),_HpSwitchStackAutoGrab_Type())
hpSwitchStackAutoGrab.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchStackAutoGrab.setStatus(_B)
_HpSwitchStackConfigMemberTable_Object=MibTable
hpSwitchStackConfigMemberTable=_HpSwitchStackConfigMemberTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2))
if mibBuilder.loadTexts:hpSwitchStackConfigMemberTable.setStatus(_B)
_HpSwitchStackConfigMemberEntry_Object=MibTableRow
hpSwitchStackConfigMemberEntry=_HpSwitchStackConfigMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2,1))
hpSwitchStackConfigMemberEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:hpSwitchStackConfigMemberEntry.setStatus(_B)
class _HpSwitchStackMemberSwitchNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpSwitchStackMemberSwitchNum_Type.__name__=_D
_HpSwitchStackMemberSwitchNum_Object=MibTableColumn
hpSwitchStackMemberSwitchNum=_HpSwitchStackMemberSwitchNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2,1,1),_HpSwitchStackMemberSwitchNum_Type())
hpSwitchStackMemberSwitchNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStackMemberSwitchNum.setStatus(_B)
_HpSwitchStackMemberMacAddr_Type=MacAddress
_HpSwitchStackMemberMacAddr_Object=MibTableColumn
hpSwitchStackMemberMacAddr=_HpSwitchStackMemberMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2,1,2),_HpSwitchStackMemberMacAddr_Type())
hpSwitchStackMemberMacAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchStackMemberMacAddr.setStatus(_B)
class _HpSwitchStackMemberPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_HpSwitchStackMemberPassword_Type.__name__=_E
_HpSwitchStackMemberPassword_Object=MibTableColumn
hpSwitchStackMemberPassword=_HpSwitchStackMemberPassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2,1,3),_HpSwitchStackMemberPassword_Type())
hpSwitchStackMemberPassword.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchStackMemberPassword.setStatus(_L)
_HpSwitchStackMemberEntryStatus_Type=RowStatus
_HpSwitchStackMemberEntryStatus_Object=MibTableColumn
hpSwitchStackMemberEntryStatus=_HpSwitchStackMemberEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2,1,4),_HpSwitchStackMemberEntryStatus_Type())
hpSwitchStackMemberEntryStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchStackMemberEntryStatus.setStatus(_B)
class _HpSwitchStackMemberPasswordLong_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1025))
_HpSwitchStackMemberPasswordLong_Type.__name__=_E
_HpSwitchStackMemberPasswordLong_Object=MibTableColumn
hpSwitchStackMemberPasswordLong=_HpSwitchStackMemberPasswordLong_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,2,1,5),_HpSwitchStackMemberPasswordLong_Type())
hpSwitchStackMemberPasswordLong.setMaxAccess(_J)
if mibBuilder.loadTexts:hpSwitchStackMemberPasswordLong.setStatus(_B)
_HpStackStats_ObjectIdentity=ObjectIdentity
hpStackStats=_HpStackStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10,3))
class _HpStackStatsName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpStackStatsName_Type.__name__=_E
_HpStackStatsName_Object=MibScalar
hpStackStatsName=_HpStackStatsName_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,3,1),_HpStackStatsName_Type())
hpStackStatsName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsName.setStatus(_B)
class _HpStackStatsMembersNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpStackStatsMembersNum_Type.__name__=_D
_HpStackStatsMembersNum_Object=MibScalar
hpStackStatsMembersNum=_HpStackStatsMembersNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,3,2),_HpStackStatsMembersNum_Type())
hpStackStatsMembersNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMembersNum.setStatus(_B)
class _HpStackStatsMembersUnreachable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpStackStatsMembersUnreachable_Type.__name__=_D
_HpStackStatsMembersUnreachable_Object=MibScalar
hpStackStatsMembersUnreachable=_HpStackStatsMembersUnreachable_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,3,3),_HpStackStatsMembersUnreachable_Type())
hpStackStatsMembersUnreachable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMembersUnreachable.setStatus(_B)
class _HpStackStatsMemberID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpStackStatsMemberID_Type.__name__=_D
_HpStackStatsMemberID_Object=MibScalar
hpStackStatsMemberID=_HpStackStatsMemberID_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,3,4),_HpStackStatsMemberID_Type())
hpStackStatsMemberID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMemberID.setStatus(_B)
_HpStackStatsMgmtIpAddr_Type=IpAddress
_HpStackStatsMgmtIpAddr_Object=MibScalar
hpStackStatsMgmtIpAddr=_HpStackStatsMgmtIpAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,3,5),_HpStackStatsMgmtIpAddr_Type())
hpStackStatsMgmtIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMgmtIpAddr.setStatus(_B)
class _HpStackStatsStackingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_a,1),(_K,2),(_b,3),('notCommand',4),('stackFull',5),(_c,6),(_d,7),('evicted',8),('commandUp',9),('commandDown',10),(_e,11),(_f,12)))
_HpStackStatsStackingStatus_Type.__name__=_D
_HpStackStatsStackingStatus_Object=MibScalar
hpStackStatsStackingStatus=_HpStackStatsStackingStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,3,6),_HpStackStatsStackingStatus_Type())
hpStackStatsStackingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsStackingStatus.setStatus(_B)
_HpStackStatsMembersTable_Object=MibTable
hpStackStatsMembersTable=_HpStackStatsMembersTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4))
if mibBuilder.loadTexts:hpStackStatsMembersTable.setStatus(_B)
_HpStackStatsMemberEntry_Object=MibTableRow
hpStackStatsMemberEntry=_HpStackStatsMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4,1))
hpStackStatsMemberEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:hpStackStatsMemberEntry.setStatus(_B)
class _HpStackStatsMemberSwitchIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpStackStatsMemberSwitchIndx_Type.__name__=_D
_HpStackStatsMemberSwitchIndx_Object=MibTableColumn
hpStackStatsMemberSwitchIndx=_HpStackStatsMemberSwitchIndx_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4,1,1),_HpStackStatsMemberSwitchIndx_Type())
hpStackStatsMemberSwitchIndx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMemberSwitchIndx.setStatus(_B)
_HpStackStatsMemberMacAddr_Type=MacAddress
_HpStackStatsMemberMacAddr_Object=MibTableColumn
hpStackStatsMemberMacAddr=_HpStackStatsMemberMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4,1,2),_HpStackStatsMemberMacAddr_Type())
hpStackStatsMemberMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMemberMacAddr.setStatus(_B)
class _HpStackStatsMemberSystemName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpStackStatsMemberSystemName_Type.__name__=_E
_HpStackStatsMemberSystemName_Object=MibTableColumn
hpStackStatsMemberSystemName=_HpStackStatsMemberSystemName_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4,1,3),_HpStackStatsMemberSystemName_Type())
hpStackStatsMemberSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMemberSystemName.setStatus(_B)
class _HpStackStatsMemberDeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpStackStatsMemberDeviceType_Type.__name__=_E
_HpStackStatsMemberDeviceType_Object=MibTableColumn
hpStackStatsMemberDeviceType=_HpStackStatsMemberDeviceType_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4,1,4),_HpStackStatsMemberDeviceType_Type())
hpStackStatsMemberDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMemberDeviceType.setStatus(_B)
class _HpStackStatsMemberOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_K,1),(_a,2),(_b,3),('stackingDisabled',4),('invalidPassword',5),('commanderAnotherStack',6),(_c,7),(_d,8),('rejected',9),('memberUp',10),('memberDown',11),('commanderThisStack',12),(_e,13),(_f,14)))
_HpStackStatsMemberOperStatus_Type.__name__=_D
_HpStackStatsMemberOperStatus_Object=MibTableColumn
hpStackStatsMemberOperStatus=_HpStackStatsMemberOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,4,1,5),_HpStackStatsMemberOperStatus_Type())
hpStackStatsMemberOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpStackStatsMemberOperStatus.setStatus(_B)
_HpSwitchDiscoveryConfig_ObjectIdentity=ObjectIdentity
hpSwitchDiscoveryConfig=_HpSwitchDiscoveryConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10,5))
class _HpSwitchDiscoveryAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpSwitchDiscoveryAdminStatus_Type.__name__=_D
_HpSwitchDiscoveryAdminStatus_Object=MibScalar
hpSwitchDiscoveryAdminStatus=_HpSwitchDiscoveryAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,5,1),_HpSwitchDiscoveryAdminStatus_Type())
hpSwitchDiscoveryAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchDiscoveryAdminStatus.setStatus(_B)
class _HpSwitchDiscoveryTransmissionInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_HpSwitchDiscoveryTransmissionInterval_Type.__name__=_D
_HpSwitchDiscoveryTransmissionInterval_Object=MibScalar
hpSwitchDiscoveryTransmissionInterval=_HpSwitchDiscoveryTransmissionInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,5,2),_HpSwitchDiscoveryTransmissionInterval_Type())
hpSwitchDiscoveryTransmissionInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSwitchDiscoveryTransmissionInterval.setStatus(_B)
_HpDiscoverStatsCandidatesTable_Object=MibTable
hpDiscoverStatsCandidatesTable=_HpDiscoverStatsCandidatesTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,6))
if mibBuilder.loadTexts:hpDiscoverStatsCandidatesTable.setStatus(_B)
_HpDiscoverStatsCandidateEntry_Object=MibTableRow
hpDiscoverStatsCandidateEntry=_HpDiscoverStatsCandidateEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,6,1))
hpDiscoverStatsCandidateEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:hpDiscoverStatsCandidateEntry.setStatus(_B)
_HpDiscoverStatsCandidateMacAddr_Type=MacAddress
_HpDiscoverStatsCandidateMacAddr_Object=MibTableColumn
hpDiscoverStatsCandidateMacAddr=_HpDiscoverStatsCandidateMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,6,1,1),_HpDiscoverStatsCandidateMacAddr_Type())
hpDiscoverStatsCandidateMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsCandidateMacAddr.setStatus(_B)
class _HpDiscoverStatsCandidateSystemName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpDiscoverStatsCandidateSystemName_Type.__name__=_E
_HpDiscoverStatsCandidateSystemName_Object=MibTableColumn
hpDiscoverStatsCandidateSystemName=_HpDiscoverStatsCandidateSystemName_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,6,1,2),_HpDiscoverStatsCandidateSystemName_Type())
hpDiscoverStatsCandidateSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsCandidateSystemName.setStatus(_B)
class _HpDiscoverStatsCandidateDeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpDiscoverStatsCandidateDeviceType_Type.__name__=_E
_HpDiscoverStatsCandidateDeviceType_Object=MibTableColumn
hpDiscoverStatsCandidateDeviceType=_HpDiscoverStatsCandidateDeviceType_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,6,1,3),_HpDiscoverStatsCandidateDeviceType_Type())
hpDiscoverStatsCandidateDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsCandidateDeviceType.setStatus(_B)
_HpDiscoverStatsTable_Object=MibTable
hpDiscoverStatsTable=_HpDiscoverStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7))
if mibBuilder.loadTexts:hpDiscoverStatsTable.setStatus(_B)
_HpDiscoverStatsEntry_Object=MibTableRow
hpDiscoverStatsEntry=_HpDiscoverStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7,1))
hpDiscoverStatsEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:hpDiscoverStatsEntry.setStatus(_B)
class _HpDiscoverStatsSwitchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpDiscoverStatsSwitchIndex_Type.__name__=_D
_HpDiscoverStatsSwitchIndex_Object=MibTableColumn
hpDiscoverStatsSwitchIndex=_HpDiscoverStatsSwitchIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7,1,1),_HpDiscoverStatsSwitchIndex_Type())
hpDiscoverStatsSwitchIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsSwitchIndex.setStatus(_B)
class _HpDiscoverStatsSwitchStackName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpDiscoverStatsSwitchStackName_Type.__name__=_E
_HpDiscoverStatsSwitchStackName_Object=MibTableColumn
hpDiscoverStatsSwitchStackName=_HpDiscoverStatsSwitchStackName_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7,1,2),_HpDiscoverStatsSwitchStackName_Type())
hpDiscoverStatsSwitchStackName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsSwitchStackName.setStatus(_B)
_HpDiscoverStatsSwitchMacAddr_Type=MacAddress
_HpDiscoverStatsSwitchMacAddr_Object=MibTableColumn
hpDiscoverStatsSwitchMacAddr=_HpDiscoverStatsSwitchMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7,1,3),_HpDiscoverStatsSwitchMacAddr_Type())
hpDiscoverStatsSwitchMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsSwitchMacAddr.setStatus(_B)
class _HpDiscoverStatsSwitchSystemName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpDiscoverStatsSwitchSystemName_Type.__name__=_E
_HpDiscoverStatsSwitchSystemName_Object=MibTableColumn
hpDiscoverStatsSwitchSystemName=_HpDiscoverStatsSwitchSystemName_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7,1,4),_HpDiscoverStatsSwitchSystemName_Type())
hpDiscoverStatsSwitchSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsSwitchSystemName.setStatus(_B)
class _HpDiscoverStatsSwitchStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_HpDiscoverStatsSwitchStatus_Type.__name__=_E
_HpDiscoverStatsSwitchStatus_Object=MibTableColumn
hpDiscoverStatsSwitchStatus=_HpDiscoverStatsSwitchStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,10,7,1,5),_HpDiscoverStatsSwitchStatus_Type())
hpDiscoverStatsSwitchStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDiscoverStatsSwitchStatus.setStatus(_B)
_HpSwitchVirtualStackMibConformance_ObjectIdentity=ObjectIdentity
hpSwitchVirtualStackMibConformance=_HpSwitchVirtualStackMibConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10,8))
_HpSwitchVirtualStackMibCompliances_ObjectIdentity=ObjectIdentity
hpSwitchVirtualStackMibCompliances=_HpSwitchVirtualStackMibCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10,8,1))
_HpSwitchVirtualStackMibGroups_ObjectIdentity=ObjectIdentity
hpSwitchVirtualStackMibGroups=_HpSwitchVirtualStackMibGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,10,8,2))
hpSwitchStackConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,10,8,2,1))
hpSwitchStackConfigGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_I),(_A,_V),(_A,_g),(_A,_W)))
if mibBuilder.loadTexts:hpSwitchStackConfigGroup.setStatus(_L)
hpSwitchStackStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,10,8,2,2))
hpSwitchStackStatsGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_M),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:hpSwitchStackStatsGroup.setStatus(_B)
hpSwitchDiscoverConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,10,8,2,3))
hpSwitchDiscoverConfigGroup.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:hpSwitchDiscoverConfigGroup.setStatus(_B)
hpDiscoverStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,10,8,2,4))
hpDiscoverStatsGroup.setObjects(*((_A,_N),(_A,_t),(_A,_u),(_A,_O),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:hpDiscoverStatsGroup.setStatus(_B)
hpSwitchStackConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,10,8,2,5))
hpSwitchStackConfigGroup1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_I),(_A,_V),(_A,_z),(_A,_W)))
if mibBuilder.loadTexts:hpSwitchStackConfigGroup1.setStatus(_B)
hpSwitchVirtualStackMibCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,10,8,1,1))
hpSwitchVirtualStackMibCompliance.setObjects(*((_A,_A0),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hpSwitchVirtualStackMibCompliance.setStatus(_L)
hpSwitchVirtualStackMibCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,10,8,1,2))
hpSwitchVirtualStackMibCompliance1.setObjects(*((_A,_A1),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hpSwitchVirtualStackMibCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpSwitchVirtualStackMib':hpSwitchVirtualStackMib,'hpSwitchStackConfig':hpSwitchStackConfig,_P:hpSwitchStackAdminStatus,_Q:hpSwitchStackCommandAddr,_R:hpSwitchStackName,_S:hpSwitchStackPropagate,_T:hpSwitchStackAutoJoin,_U:hpSwitchStackAutoGrab,'hpSwitchStackConfigMemberTable':hpSwitchStackConfigMemberTable,'hpSwitchStackConfigMemberEntry':hpSwitchStackConfigMemberEntry,_I:hpSwitchStackMemberSwitchNum,_V:hpSwitchStackMemberMacAddr,_g:hpSwitchStackMemberPassword,_W:hpSwitchStackMemberEntryStatus,_z:hpSwitchStackMemberPasswordLong,'hpStackStats':hpStackStats,_h:hpStackStatsName,_i:hpStackStatsMembersNum,_j:hpStackStatsMembersUnreachable,_k:hpStackStatsMemberID,_l:hpStackStatsMgmtIpAddr,_m:hpStackStatsStackingStatus,'hpStackStatsMembersTable':hpStackStatsMembersTable,'hpStackStatsMemberEntry':hpStackStatsMemberEntry,_M:hpStackStatsMemberSwitchIndx,_n:hpStackStatsMemberMacAddr,_o:hpStackStatsMemberSystemName,_p:hpStackStatsMemberDeviceType,_q:hpStackStatsMemberOperStatus,'hpSwitchDiscoveryConfig':hpSwitchDiscoveryConfig,_r:hpSwitchDiscoveryAdminStatus,_s:hpSwitchDiscoveryTransmissionInterval,'hpDiscoverStatsCandidatesTable':hpDiscoverStatsCandidatesTable,'hpDiscoverStatsCandidateEntry':hpDiscoverStatsCandidateEntry,_N:hpDiscoverStatsCandidateMacAddr,_t:hpDiscoverStatsCandidateSystemName,_u:hpDiscoverStatsCandidateDeviceType,'hpDiscoverStatsTable':hpDiscoverStatsTable,'hpDiscoverStatsEntry':hpDiscoverStatsEntry,_O:hpDiscoverStatsSwitchIndex,_v:hpDiscoverStatsSwitchStackName,_w:hpDiscoverStatsSwitchMacAddr,_x:hpDiscoverStatsSwitchSystemName,_y:hpDiscoverStatsSwitchStatus,'hpSwitchVirtualStackMibConformance':hpSwitchVirtualStackMibConformance,'hpSwitchVirtualStackMibCompliances':hpSwitchVirtualStackMibCompliances,'hpSwitchVirtualStackMibCompliance':hpSwitchVirtualStackMibCompliance,'hpSwitchVirtualStackMibCompliance1':hpSwitchVirtualStackMibCompliance1,'hpSwitchVirtualStackMibGroups':hpSwitchVirtualStackMibGroups,_A0:hpSwitchStackConfigGroup,_X:hpSwitchStackStatsGroup,_Y:hpSwitchDiscoverConfigGroup,_Z:hpDiscoverStatsGroup,_A1:hpSwitchStackConfigGroup1})