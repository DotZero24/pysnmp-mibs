_A4='vmVlanCreationGroup'
_A3='vmMembershipGroup'
_A2='vmVmpsChange'
_A1='vmVlanCreationMode'
_A0='vmMembershipSummaryExtPorts'
_z='vmVoiceVlanCdpVerifyEnable'
_y='vmMembershipSummaryMember2kPorts'
_x='vmVoiceVlanId'
_w='vmVlans4k'
_v='vmVlans3k'
_u='vmVlans2k'
_t='vmNotificationsEnabled'
_s='vmInsufficientResources'
_r='vmVQPWrongVersion'
_q='vmVQPWrongDomain'
_p='vmVQPDenied'
_o='vmVQPShutdown'
_n='vmVmpsChanges'
_m='vmVQPResponses'
_l='vmVQPQueries'
_k='vmVmpsRowStatus'
_j='vmVmpsPrimary'
_i='vmVmpsCurrent'
_h='vmVmpsReconfirmResult'
_g='vmVmpsReconfirmInterval'
_f='vmVmpsReconfirm'
_e='vmVmpsRetries'
_d='vmVmpsVQPVersion'
_c='vmMembershipPortRangeIndex'
_b='not-accessible'
_a='read-create'
_Z='vmMembershipExtGroup'
_Y='vmMembershipGroup2'
_X='vmVlans'
_W='vmMembershipSummaryMemberPorts'
_V='vmMembershipSummaryVlanIndex'
_U='ifIndex'
_T='IF-MIB'
_S='vmVoiceVlanExtGroup'
_R='vmPortStatus'
_Q='vmVlanType'
_P='vmVlan'
_O='vmVmpsIpAddress'
_N='vmVoiceVlanGroup'
_M='vmStatusGroup'
_L='vm1kVlanGroup'
_K='vmMembershipGroup3'
_J='vm4kVlanGroup'
_I='OctetString'
_H='vmVQPNotificationsGroup'
_G='vmVQPClientGroup'
_F='deprecated'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-VLAN-MEMBERSHIP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPortList,CiscoPortListRange=mibBuilder.importSymbols('CISCO-TC','CiscoPortList','CiscoPortListRange')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
ifIndex,=mibBuilder.importSymbols(_T,_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ciscoVlanMembershipMIB=ModuleIdentity((1,3,6,1,4,1,9,9,68))
if mibBuilder.loadTexts:ciscoVlanMembershipMIB.setRevisions(('2007-12-14 00:00','2004-07-16 00:00','2004-04-07 00:00','2003-10-10 00:00','2003-06-05 00:00','2002-03-28 00:00','2001-05-01 00:00','2001-01-30 00:00','2000-01-06 00:00','1999-01-18 00:00','1996-12-06 00:00'))
_CiscoVlanMembershipMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVlanMembershipMIBObjects=_CiscoVlanMembershipMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,68,1))
_VmVmps_ObjectIdentity=ObjectIdentity
vmVmps=_VmVmps_ObjectIdentity((1,3,6,1,4,1,9,9,68,1,1))
_VmVmpsVQPVersion_Type=Integer32
_VmVmpsVQPVersion_Object=MibScalar
vmVmpsVQPVersion=_VmVmpsVQPVersion_Object((1,3,6,1,4,1,9,9,68,1,1,1),_VmVmpsVQPVersion_Type())
vmVmpsVQPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVmpsVQPVersion.setStatus(_B)
class _VmVmpsRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VmVmpsRetries_Type.__name__=_E
_VmVmpsRetries_Object=MibScalar
vmVmpsRetries=_VmVmpsRetries_Object((1,3,6,1,4,1,9,9,68,1,1,2),_VmVmpsRetries_Type())
vmVmpsRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVmpsRetries.setStatus(_B)
class _VmVmpsReconfirmInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_VmVmpsReconfirmInterval_Type.__name__=_E
_VmVmpsReconfirmInterval_Object=MibScalar
vmVmpsReconfirmInterval=_VmVmpsReconfirmInterval_Object((1,3,6,1,4,1,9,9,68,1,1,3),_VmVmpsReconfirmInterval_Type())
vmVmpsReconfirmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVmpsReconfirmInterval.setStatus(_B)
if mibBuilder.loadTexts:vmVmpsReconfirmInterval.setUnits('Minutes')
class _VmVmpsReconfirm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ready',1),('execute',2)))
_VmVmpsReconfirm_Type.__name__=_E
_VmVmpsReconfirm_Object=MibScalar
vmVmpsReconfirm=_VmVmpsReconfirm_Object((1,3,6,1,4,1,9,9,68,1,1,4),_VmVmpsReconfirm_Type())
vmVmpsReconfirm.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVmpsReconfirm.setStatus(_B)
class _VmVmpsReconfirmResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('inProgress',2),('success',3),('noResponse',4),('noVmps',5),('noDynamicPort',6),('noHostConnected',7)))
_VmVmpsReconfirmResult_Type.__name__=_E
_VmVmpsReconfirmResult_Object=MibScalar
vmVmpsReconfirmResult=_VmVmpsReconfirmResult_Object((1,3,6,1,4,1,9,9,68,1,1,5),_VmVmpsReconfirmResult_Type())
vmVmpsReconfirmResult.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVmpsReconfirmResult.setStatus(_B)
_VmVmpsCurrent_Type=IpAddress
_VmVmpsCurrent_Object=MibScalar
vmVmpsCurrent=_VmVmpsCurrent_Object((1,3,6,1,4,1,9,9,68,1,1,6),_VmVmpsCurrent_Type())
vmVmpsCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVmpsCurrent.setStatus(_B)
_VmVmpsTable_Object=MibTable
vmVmpsTable=_VmVmpsTable_Object((1,3,6,1,4,1,9,9,68,1,1,7))
if mibBuilder.loadTexts:vmVmpsTable.setStatus(_B)
_VmVmpsEntry_Object=MibTableRow
vmVmpsEntry=_VmVmpsEntry_Object((1,3,6,1,4,1,9,9,68,1,1,7,1))
vmVmpsEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:vmVmpsEntry.setStatus(_B)
_VmVmpsIpAddress_Type=IpAddress
_VmVmpsIpAddress_Object=MibTableColumn
vmVmpsIpAddress=_VmVmpsIpAddress_Object((1,3,6,1,4,1,9,9,68,1,1,7,1,1),_VmVmpsIpAddress_Type())
vmVmpsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVmpsIpAddress.setStatus(_B)
_VmVmpsPrimary_Type=TruthValue
_VmVmpsPrimary_Object=MibTableColumn
vmVmpsPrimary=_VmVmpsPrimary_Object((1,3,6,1,4,1,9,9,68,1,1,7,1,2),_VmVmpsPrimary_Type())
vmVmpsPrimary.setMaxAccess(_a)
if mibBuilder.loadTexts:vmVmpsPrimary.setStatus(_B)
_VmVmpsRowStatus_Type=RowStatus
_VmVmpsRowStatus_Object=MibTableColumn
vmVmpsRowStatus=_VmVmpsRowStatus_Object((1,3,6,1,4,1,9,9,68,1,1,7,1,3),_VmVmpsRowStatus_Type())
vmVmpsRowStatus.setMaxAccess(_a)
if mibBuilder.loadTexts:vmVmpsRowStatus.setStatus(_B)
_VmMembership_ObjectIdentity=ObjectIdentity
vmMembership=_VmMembership_ObjectIdentity((1,3,6,1,4,1,9,9,68,1,2))
_VmMembershipSummaryTable_Object=MibTable
vmMembershipSummaryTable=_VmMembershipSummaryTable_Object((1,3,6,1,4,1,9,9,68,1,2,1))
if mibBuilder.loadTexts:vmMembershipSummaryTable.setStatus(_B)
_VmMembershipSummaryEntry_Object=MibTableRow
vmMembershipSummaryEntry=_VmMembershipSummaryEntry_Object((1,3,6,1,4,1,9,9,68,1,2,1,1))
vmMembershipSummaryEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:vmMembershipSummaryEntry.setStatus(_B)
_VmMembershipSummaryVlanIndex_Type=VlanIndex
_VmMembershipSummaryVlanIndex_Object=MibTableColumn
vmMembershipSummaryVlanIndex=_VmMembershipSummaryVlanIndex_Object((1,3,6,1,4,1,9,9,68,1,2,1,1,1),_VmMembershipSummaryVlanIndex_Type())
vmMembershipSummaryVlanIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:vmMembershipSummaryVlanIndex.setStatus(_B)
class _VmMembershipSummaryMemberPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VmMembershipSummaryMemberPorts_Type.__name__=_I
_VmMembershipSummaryMemberPorts_Object=MibTableColumn
vmMembershipSummaryMemberPorts=_VmMembershipSummaryMemberPorts_Object((1,3,6,1,4,1,9,9,68,1,2,1,1,2),_VmMembershipSummaryMemberPorts_Type())
vmMembershipSummaryMemberPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMembershipSummaryMemberPorts.setStatus(_F)
_VmMembershipSummaryMember2kPorts_Type=CiscoPortList
_VmMembershipSummaryMember2kPorts_Object=MibTableColumn
vmMembershipSummaryMember2kPorts=_VmMembershipSummaryMember2kPorts_Object((1,3,6,1,4,1,9,9,68,1,2,1,1,3),_VmMembershipSummaryMember2kPorts_Type())
vmMembershipSummaryMember2kPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMembershipSummaryMember2kPorts.setStatus(_B)
_VmMembershipTable_Object=MibTable
vmMembershipTable=_VmMembershipTable_Object((1,3,6,1,4,1,9,9,68,1,2,2))
if mibBuilder.loadTexts:vmMembershipTable.setStatus(_B)
_VmMembershipEntry_Object=MibTableRow
vmMembershipEntry=_VmMembershipEntry_Object((1,3,6,1,4,1,9,9,68,1,2,2,1))
vmMembershipEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:vmMembershipEntry.setStatus(_B)
class _VmVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('multiVlan',3)))
_VmVlanType_Type.__name__=_E
_VmVlanType_Object=MibTableColumn
vmVlanType=_VmVlanType_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,1),_VmVlanType_Type())
vmVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlanType.setStatus(_B)
class _VmVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VmVlan_Type.__name__=_E
_VmVlan_Object=MibTableColumn
vmVlan=_VmVlan_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,2),_VmVlan_Type())
vmVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlan.setStatus(_B)
class _VmPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('active',2),('shutdown',3)))
_VmPortStatus_Type.__name__=_E
_VmPortStatus_Object=MibTableColumn
vmPortStatus=_VmPortStatus_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,3),_VmPortStatus_Type())
vmPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmPortStatus.setStatus(_B)
class _VmVlans_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VmVlans_Type.__name__=_I
_VmVlans_Object=MibTableColumn
vmVlans=_VmVlans_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,4),_VmVlans_Type())
vmVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlans.setStatus(_B)
class _VmVlans2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VmVlans2k_Type.__name__=_I
_VmVlans2k_Object=MibTableColumn
vmVlans2k=_VmVlans2k_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,5),_VmVlans2k_Type())
vmVlans2k.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlans2k.setStatus(_B)
class _VmVlans3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VmVlans3k_Type.__name__=_I
_VmVlans3k_Object=MibTableColumn
vmVlans3k=_VmVlans3k_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,6),_VmVlans3k_Type())
vmVlans3k.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlans3k.setStatus(_B)
class _VmVlans4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VmVlans4k_Type.__name__=_I
_VmVlans4k_Object=MibTableColumn
vmVlans4k=_VmVlans4k_Object((1,3,6,1,4,1,9,9,68,1,2,2,1,7),_VmVlans4k_Type())
vmVlans4k.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlans4k.setStatus(_B)
_VmMembershipSummaryExtTable_Object=MibTable
vmMembershipSummaryExtTable=_VmMembershipSummaryExtTable_Object((1,3,6,1,4,1,9,9,68,1,2,3))
if mibBuilder.loadTexts:vmMembershipSummaryExtTable.setStatus(_B)
_VmMembershipSummaryExtEntry_Object=MibTableRow
vmMembershipSummaryExtEntry=_VmMembershipSummaryExtEntry_Object((1,3,6,1,4,1,9,9,68,1,2,3,1))
vmMembershipSummaryExtEntry.setIndexNames((0,_A,_V),(0,_A,_c))
if mibBuilder.loadTexts:vmMembershipSummaryExtEntry.setStatus(_B)
_VmMembershipPortRangeIndex_Type=CiscoPortListRange
_VmMembershipPortRangeIndex_Object=MibTableColumn
vmMembershipPortRangeIndex=_VmMembershipPortRangeIndex_Object((1,3,6,1,4,1,9,9,68,1,2,3,1,1),_VmMembershipPortRangeIndex_Type())
vmMembershipPortRangeIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:vmMembershipPortRangeIndex.setStatus(_B)
_VmMembershipSummaryExtPorts_Type=CiscoPortList
_VmMembershipSummaryExtPorts_Object=MibTableColumn
vmMembershipSummaryExtPorts=_VmMembershipSummaryExtPorts_Object((1,3,6,1,4,1,9,9,68,1,2,3,1,2),_VmMembershipSummaryExtPorts_Type())
vmMembershipSummaryExtPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMembershipSummaryExtPorts.setStatus(_B)
class _VmVlanCreationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('manual',2)))
_VmVlanCreationMode_Type.__name__=_E
_VmVlanCreationMode_Object=MibScalar
vmVlanCreationMode=_VmVlanCreationMode_Object((1,3,6,1,4,1,9,9,68,1,2,4),_VmVlanCreationMode_Type())
vmVlanCreationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVlanCreationMode.setStatus(_B)
_VmStatistics_ObjectIdentity=ObjectIdentity
vmStatistics=_VmStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,68,1,3))
_VmVQPQueries_Type=Counter32
_VmVQPQueries_Object=MibScalar
vmVQPQueries=_VmVQPQueries_Object((1,3,6,1,4,1,9,9,68,1,3,1),_VmVQPQueries_Type())
vmVQPQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVQPQueries.setStatus(_B)
_VmVQPResponses_Type=Counter32
_VmVQPResponses_Object=MibScalar
vmVQPResponses=_VmVQPResponses_Object((1,3,6,1,4,1,9,9,68,1,3,2),_VmVQPResponses_Type())
vmVQPResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVQPResponses.setStatus(_B)
_VmVmpsChanges_Type=Counter32
_VmVmpsChanges_Object=MibScalar
vmVmpsChanges=_VmVmpsChanges_Object((1,3,6,1,4,1,9,9,68,1,3,3),_VmVmpsChanges_Type())
vmVmpsChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVmpsChanges.setStatus(_B)
_VmVQPShutdown_Type=Counter32
_VmVQPShutdown_Object=MibScalar
vmVQPShutdown=_VmVQPShutdown_Object((1,3,6,1,4,1,9,9,68,1,3,4),_VmVQPShutdown_Type())
vmVQPShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVQPShutdown.setStatus(_B)
_VmVQPDenied_Type=Counter32
_VmVQPDenied_Object=MibScalar
vmVQPDenied=_VmVQPDenied_Object((1,3,6,1,4,1,9,9,68,1,3,5),_VmVQPDenied_Type())
vmVQPDenied.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVQPDenied.setStatus(_B)
_VmVQPWrongDomain_Type=Counter32
_VmVQPWrongDomain_Object=MibScalar
vmVQPWrongDomain=_VmVQPWrongDomain_Object((1,3,6,1,4,1,9,9,68,1,3,6),_VmVQPWrongDomain_Type())
vmVQPWrongDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVQPWrongDomain.setStatus(_B)
_VmVQPWrongVersion_Type=Counter32
_VmVQPWrongVersion_Object=MibScalar
vmVQPWrongVersion=_VmVQPWrongVersion_Object((1,3,6,1,4,1,9,9,68,1,3,7),_VmVQPWrongVersion_Type())
vmVQPWrongVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vmVQPWrongVersion.setStatus(_B)
_VmInsufficientResources_Type=Counter32
_VmInsufficientResources_Object=MibScalar
vmInsufficientResources=_VmInsufficientResources_Object((1,3,6,1,4,1,9,9,68,1,3,8),_VmInsufficientResources_Type())
vmInsufficientResources.setMaxAccess(_C)
if mibBuilder.loadTexts:vmInsufficientResources.setStatus(_B)
_VmStatus_ObjectIdentity=ObjectIdentity
vmStatus=_VmStatus_ObjectIdentity((1,3,6,1,4,1,9,9,68,1,4))
_VmNotificationsEnabled_Type=TruthValue
_VmNotificationsEnabled_Object=MibScalar
vmNotificationsEnabled=_VmNotificationsEnabled_Object((1,3,6,1,4,1,9,9,68,1,4,1),_VmNotificationsEnabled_Type())
vmNotificationsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:vmNotificationsEnabled.setStatus(_B)
_VmVoiceVlan_ObjectIdentity=ObjectIdentity
vmVoiceVlan=_VmVoiceVlan_ObjectIdentity((1,3,6,1,4,1,9,9,68,1,5))
_VmVoiceVlanTable_Object=MibTable
vmVoiceVlanTable=_VmVoiceVlanTable_Object((1,3,6,1,4,1,9,9,68,1,5,1))
if mibBuilder.loadTexts:vmVoiceVlanTable.setStatus(_B)
_VmVoiceVlanEntry_Object=MibTableRow
vmVoiceVlanEntry=_VmVoiceVlanEntry_Object((1,3,6,1,4,1,9,9,68,1,5,1,1))
vmVoiceVlanEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:vmVoiceVlanEntry.setStatus(_B)
class _VmVoiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_VmVoiceVlanId_Type.__name__=_E
_VmVoiceVlanId_Object=MibTableColumn
vmVoiceVlanId=_VmVoiceVlanId_Object((1,3,6,1,4,1,9,9,68,1,5,1,1,1),_VmVoiceVlanId_Type())
vmVoiceVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVoiceVlanId.setStatus(_B)
_VmVoiceVlanCdpVerifyEnable_Type=TruthValue
_VmVoiceVlanCdpVerifyEnable_Object=MibTableColumn
vmVoiceVlanCdpVerifyEnable=_VmVoiceVlanCdpVerifyEnable_Object((1,3,6,1,4,1,9,9,68,1,5,1,1,2),_VmVoiceVlanCdpVerifyEnable_Type())
vmVoiceVlanCdpVerifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVoiceVlanCdpVerifyEnable.setStatus(_B)
_VmNotifications_ObjectIdentity=ObjectIdentity
vmNotifications=_VmNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,68,2))
_VmNotificationsPrefix_ObjectIdentity=ObjectIdentity
vmNotificationsPrefix=_VmNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,68,2,0))
_VmMIBConformance_ObjectIdentity=ObjectIdentity
vmMIBConformance=_VmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,68,3))
_VmMIBCompliances_ObjectIdentity=ObjectIdentity
vmMIBCompliances=_VmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,68,3,1))
_VmMIBGroups_ObjectIdentity=ObjectIdentity
vmMIBGroups=_VmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,68,3,2))
vmMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,1))
vmMembershipGroup.setObjects(*((_A,_W),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vmMembershipGroup.setStatus(_F)
vmVQPClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,2))
vmVQPClientGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_O),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:vmVQPClientGroup.setStatus(_B)
vmStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,4))
vmStatusGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:vmStatusGroup.setStatus(_B)
vmMembershipGroup2=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,5))
vmMembershipGroup2.setObjects(*((_A,_W),(_A,_P),(_A,_X),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vmMembershipGroup2.setStatus(_F)
vm4kVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,6))
vm4kVlanGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:vm4kVlanGroup.setStatus(_B)
vmVoiceVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,7))
vmVoiceVlanGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:vmVoiceVlanGroup.setStatus(_B)
vm1kVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,8))
vm1kVlanGroup.setObjects((_A,_X))
if mibBuilder.loadTexts:vm1kVlanGroup.setStatus(_B)
vmMembershipGroup3=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,9))
vmMembershipGroup3.setObjects(*((_A,_y),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:vmMembershipGroup3.setStatus(_B)
vmVoiceVlanExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,10))
vmVoiceVlanExtGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:vmVoiceVlanExtGroup.setStatus(_B)
vmMembershipExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,11))
vmMembershipExtGroup.setObjects((_A,_A0))
if mibBuilder.loadTexts:vmMembershipExtGroup.setStatus(_B)
vmVlanCreationGroup=ObjectGroup((1,3,6,1,4,1,9,9,68,3,2,12))
vmVlanCreationGroup.setObjects((_A,_A1))
if mibBuilder.loadTexts:vmVlanCreationGroup.setStatus(_B)
vmVmpsChange=NotificationType((1,3,6,1,4,1,9,9,68,2,0,1))
vmVmpsChange.setObjects((_A,_O))
if mibBuilder.loadTexts:vmVmpsChange.setStatus(_B)
vmVQPNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,68,3,2,3))
vmVQPNotificationsGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:vmVQPNotificationsGroup.setStatus(_B)
vmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,1))
vmMIBCompliance.setObjects(*((_A,_A3),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:vmMIBCompliance.setStatus('obsolete')
vmMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,2))
vmMIBCompliance2.setObjects(*((_A,_Y),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:vmMIBCompliance2.setStatus(_F)
vmMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,3))
vmMIBCompliance3.setObjects(*((_A,_Y),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:vmMIBCompliance3.setStatus(_F)
vmMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,4))
vmMIBCompliance4.setObjects(*((_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_J),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:vmMIBCompliance4.setStatus(_F)
vmMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,5))
vmMIBCompliance5.setObjects(*((_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_J),(_A,_M),(_A,_N),(_A,_S)))
if mibBuilder.loadTexts:vmMIBCompliance5.setStatus(_F)
vmMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,6))
vmMIBCompliance6.setObjects(*((_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_J),(_A,_M),(_A,_N),(_A,_S),(_A,_Z)))
if mibBuilder.loadTexts:vmMIBCompliance6.setStatus(_F)
vmMIBCompliance7=ModuleCompliance((1,3,6,1,4,1,9,9,68,3,1,7))
vmMIBCompliance7.setObjects(*((_A,_K),(_A,_G),(_A,_H),(_A,_L),(_A,_J),(_A,_M),(_A,_N),(_A,_S),(_A,_Z),(_A,_A4)))
if mibBuilder.loadTexts:vmMIBCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoVlanMembershipMIB':ciscoVlanMembershipMIB,'ciscoVlanMembershipMIBObjects':ciscoVlanMembershipMIBObjects,'vmVmps':vmVmps,_d:vmVmpsVQPVersion,_e:vmVmpsRetries,_g:vmVmpsReconfirmInterval,_f:vmVmpsReconfirm,_h:vmVmpsReconfirmResult,_i:vmVmpsCurrent,'vmVmpsTable':vmVmpsTable,'vmVmpsEntry':vmVmpsEntry,_O:vmVmpsIpAddress,_j:vmVmpsPrimary,_k:vmVmpsRowStatus,'vmMembership':vmMembership,'vmMembershipSummaryTable':vmMembershipSummaryTable,'vmMembershipSummaryEntry':vmMembershipSummaryEntry,_V:vmMembershipSummaryVlanIndex,_W:vmMembershipSummaryMemberPorts,_y:vmMembershipSummaryMember2kPorts,'vmMembershipTable':vmMembershipTable,'vmMembershipEntry':vmMembershipEntry,_Q:vmVlanType,_P:vmVlan,_R:vmPortStatus,_X:vmVlans,_u:vmVlans2k,_v:vmVlans3k,_w:vmVlans4k,'vmMembershipSummaryExtTable':vmMembershipSummaryExtTable,'vmMembershipSummaryExtEntry':vmMembershipSummaryExtEntry,_c:vmMembershipPortRangeIndex,_A0:vmMembershipSummaryExtPorts,_A1:vmVlanCreationMode,'vmStatistics':vmStatistics,_l:vmVQPQueries,_m:vmVQPResponses,_n:vmVmpsChanges,_o:vmVQPShutdown,_p:vmVQPDenied,_q:vmVQPWrongDomain,_r:vmVQPWrongVersion,_s:vmInsufficientResources,'vmStatus':vmStatus,_t:vmNotificationsEnabled,'vmVoiceVlan':vmVoiceVlan,'vmVoiceVlanTable':vmVoiceVlanTable,'vmVoiceVlanEntry':vmVoiceVlanEntry,_x:vmVoiceVlanId,_z:vmVoiceVlanCdpVerifyEnable,'vmNotifications':vmNotifications,'vmNotificationsPrefix':vmNotificationsPrefix,_A2:vmVmpsChange,'vmMIBConformance':vmMIBConformance,'vmMIBCompliances':vmMIBCompliances,'vmMIBCompliance':vmMIBCompliance,'vmMIBCompliance2':vmMIBCompliance2,'vmMIBCompliance3':vmMIBCompliance3,'vmMIBCompliance4':vmMIBCompliance4,'vmMIBCompliance5':vmMIBCompliance5,'vmMIBCompliance6':vmMIBCompliance6,'vmMIBCompliance7':vmMIBCompliance7,'vmMIBGroups':vmMIBGroups,_A3:vmMembershipGroup,_G:vmVQPClientGroup,_H:vmVQPNotificationsGroup,_M:vmStatusGroup,_Y:vmMembershipGroup2,_J:vm4kVlanGroup,_N:vmVoiceVlanGroup,_L:vm1kVlanGroup,_K:vmMembershipGroup3,_S:vmVoiceVlanExtGroup,_Z:vmMembershipExtGroup,_A4:vmVlanCreationGroup})