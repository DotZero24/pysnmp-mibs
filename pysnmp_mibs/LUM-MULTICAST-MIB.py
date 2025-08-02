_AK='multicastIgmpPmReset'
_AJ='multicastIgmpPmMembers'
_AI='multicastIgmpPmDropHosts'
_AH='multicastIgmpPmRxIllegalLength'
_AG='multicastIgmpPmRxUnknownType'
_AF='multicastIgmpPmRxChksumErrors'
_AE='multicastIgmpPmTxLeavesV2'
_AD='multicastIgmpPmRxLeavesV2'
_AC='multicastIgmpPmTxQueries'
_AB='multicastIgmpPmRxQueries'
_AA='multicastIgmpPmTxReportsV3'
_A9='multicastIgmpPmTxReportsV2'
_A8='multicastIgmpPmTxReportsV1'
_A7='multicastIgmpPmRxReportsV3'
_A6='multicastIgmpPmRxReportsV2'
_A5='multicastIgmpPmRxReportsV1'
_A4='multicastIgmpPmName'
_A3='multicastForwardingPorts'
_A2='multicastForwardingFwd'
_A1='multicastForwardingVlan'
_A0='multicastForwardingGroup'
_z='multicastForwardingSource'
_y='multicastForwardingInternalReference'
_x='multicastForwardingName'
_w='multicastMembershipReporter'
_v='multicastMembershipType'
_u='multicastMembershipExpiryTime'
_t='multicastMembershipUpTime'
_s='multicastMembershipPorts'
_r='multicastMembershipVlan'
_q='multicastMembershipGroup'
_p='multicastMembershipSource'
_o='multicastMembershipIdentifier'
_n='multicastMembershipInternalReference'
_m='multicastMembershipName'
_l='multicastIfDeleteMembers'
_k='multicastIfForwardingFiltering'
_j='multicastIfMembershipFiltering'
_i='multicastIfNoOfStaticMembers'
_h='multicastIfMembersMax'
_g='multicastIfAssociateStaticMember'
_f='multicastIfRobustness'
_e='multicastIfReservedFlooding'
_d='multicastIfFastLeave'
_c='multicastIfRouterEnable'
_b='multicastIfProtocol'
_a='multicastIfDescr'
_Z='multicastIfName'
_Y='multicastGeneralMulticastMembershipTableSize'
_X='multicastGeneralMulticastIfTableSize'
_W='multicastGeneralStateLastChangeTime'
_V='multicastGeneralLastChangeTime'
_U='IpAddress'
_T='PmReset'
_S='multicastIgmpPmGroupV1'
_R='multicastForwardingGroupV1'
_Q='multicastMembershipGroupV1'
_P='multicastIfGroupV1'
_O='multicastGeneralGroupV1'
_N='multicastIgmpPmIndex'
_M='multicastForwardingIndex'
_L='multicastMembershipIndex'
_K='multicastIfIndex'
_J='DisplayString'
_I='TimeTicks'
_H='Integer32'
_G='EnableDisable'
_F='read-write'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='LUM-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumMulticastMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumMulticastMIB')
CommandString,EnableDisable,MgmtNameString,PmReset=mibBuilder.importSymbols('LUM-TC','CommandString',_G,'MgmtNameString',_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,_U,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_J,'PhysAddress','TextualConvention','TruthValue')
lumMulticastMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,38))
if mibBuilder.loadTexts:lumMulticastMIBModule.setRevisions(('2017-06-15 00:00','2011-05-31 00:00'))
_LumMulticastConfs_ObjectIdentity=ObjectIdentity
lumMulticastConfs=_LumMulticastConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,37,1))
_LumMulticastGroups_ObjectIdentity=ObjectIdentity
lumMulticastGroups=_LumMulticastGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,37,1,1))
_LumMulticastCompl_ObjectIdentity=ObjectIdentity
lumMulticastCompl=_LumMulticastCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,37,1,2))
_LumMulticastMIBObjects_ObjectIdentity=ObjectIdentity
lumMulticastMIBObjects=_LumMulticastMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,37,2))
_MulticastGeneral_ObjectIdentity=ObjectIdentity
multicastGeneral=_MulticastGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,37,2,1))
_MulticastGeneralLastChangeTime_Type=DateAndTime
_MulticastGeneralLastChangeTime_Object=MibScalar
multicastGeneralLastChangeTime=_MulticastGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,37,2,1,1),_MulticastGeneralLastChangeTime_Type())
multicastGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastGeneralLastChangeTime.setStatus(_A)
_MulticastGeneralStateLastChangeTime_Type=DateAndTime
_MulticastGeneralStateLastChangeTime_Object=MibScalar
multicastGeneralStateLastChangeTime=_MulticastGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,37,2,1,2),_MulticastGeneralStateLastChangeTime_Type())
multicastGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastGeneralStateLastChangeTime.setStatus(_A)
_MulticastGeneralMulticastIfTableSize_Type=Unsigned32
_MulticastGeneralMulticastIfTableSize_Object=MibScalar
multicastGeneralMulticastIfTableSize=_MulticastGeneralMulticastIfTableSize_Object((1,3,6,1,4,1,8708,2,37,2,1,3),_MulticastGeneralMulticastIfTableSize_Type())
multicastGeneralMulticastIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastGeneralMulticastIfTableSize.setStatus(_A)
_MulticastGeneralMulticastMembershipTableSize_Type=Unsigned32
_MulticastGeneralMulticastMembershipTableSize_Object=MibScalar
multicastGeneralMulticastMembershipTableSize=_MulticastGeneralMulticastMembershipTableSize_Object((1,3,6,1,4,1,8708,2,37,2,1,4),_MulticastGeneralMulticastMembershipTableSize_Type())
multicastGeneralMulticastMembershipTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastGeneralMulticastMembershipTableSize.setStatus(_A)
_MulticastGeneralMulticastForwardingTableSize_Type=Unsigned32
_MulticastGeneralMulticastForwardingTableSize_Object=MibScalar
multicastGeneralMulticastForwardingTableSize=_MulticastGeneralMulticastForwardingTableSize_Object((1,3,6,1,4,1,8708,2,37,2,1,5),_MulticastGeneralMulticastForwardingTableSize_Type())
multicastGeneralMulticastForwardingTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastGeneralMulticastForwardingTableSize.setStatus(_A)
_MulticastGeneralPmIgmpPortTableSize_Type=Unsigned32
_MulticastGeneralPmIgmpPortTableSize_Object=MibScalar
multicastGeneralPmIgmpPortTableSize=_MulticastGeneralPmIgmpPortTableSize_Object((1,3,6,1,4,1,8708,2,37,2,1,6),_MulticastGeneralPmIgmpPortTableSize_Type())
multicastGeneralPmIgmpPortTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastGeneralPmIgmpPortTableSize.setStatus(_A)
_MulticastIfList_ObjectIdentity=ObjectIdentity
multicastIfList=_MulticastIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,37,2,2))
_MulticastIfTable_Object=MibTable
multicastIfTable=_MulticastIfTable_Object((1,3,6,1,4,1,8708,2,37,2,2,1))
if mibBuilder.loadTexts:multicastIfTable.setStatus(_A)
_MulticastIfEntry_Object=MibTableRow
multicastIfEntry=_MulticastIfEntry_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1))
multicastIfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:multicastIfEntry.setStatus(_A)
class _MulticastIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MulticastIfIndex_Type.__name__=_D
_MulticastIfIndex_Object=MibTableColumn
multicastIfIndex=_MulticastIfIndex_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,1),_MulticastIfIndex_Type())
multicastIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfIndex.setStatus(_A)
_MulticastIfName_Type=MgmtNameString
_MulticastIfName_Object=MibTableColumn
multicastIfName=_MulticastIfName_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,2),_MulticastIfName_Type())
multicastIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfName.setStatus(_A)
class _MulticastIfDescr_Type(DisplayString):defaultValue=OctetString('')
_MulticastIfDescr_Type.__name__=_J
_MulticastIfDescr_Object=MibTableColumn
multicastIfDescr=_MulticastIfDescr_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,3),_MulticastIfDescr_Type())
multicastIfDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfDescr.setStatus(_A)
class _MulticastIfProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('igmp',2)))
_MulticastIfProtocol_Type.__name__=_H
_MulticastIfProtocol_Object=MibTableColumn
multicastIfProtocol=_MulticastIfProtocol_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,4),_MulticastIfProtocol_Type())
multicastIfProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfProtocol.setStatus(_A)
class _MulticastIfRouterEnable_Type(EnableDisable):defaultValue=1
_MulticastIfRouterEnable_Type.__name__=_G
_MulticastIfRouterEnable_Object=MibTableColumn
multicastIfRouterEnable=_MulticastIfRouterEnable_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,5),_MulticastIfRouterEnable_Type())
multicastIfRouterEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfRouterEnable.setStatus(_A)
class _MulticastIfFastLeave_Type(EnableDisable):defaultValue=2
_MulticastIfFastLeave_Type.__name__=_G
_MulticastIfFastLeave_Object=MibTableColumn
multicastIfFastLeave=_MulticastIfFastLeave_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,6),_MulticastIfFastLeave_Type())
multicastIfFastLeave.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfFastLeave.setStatus(_A)
class _MulticastIfRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_MulticastIfRobustness_Type.__name__=_D
_MulticastIfRobustness_Object=MibTableColumn
multicastIfRobustness=_MulticastIfRobustness_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,7),_MulticastIfRobustness_Type())
multicastIfRobustness.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfRobustness.setStatus(_A)
class _MulticastIfReservedFlooding_Type(EnableDisable):defaultValue=2
_MulticastIfReservedFlooding_Type.__name__=_G
_MulticastIfReservedFlooding_Object=MibTableColumn
multicastIfReservedFlooding=_MulticastIfReservedFlooding_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,8),_MulticastIfReservedFlooding_Type())
multicastIfReservedFlooding.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfReservedFlooding.setStatus(_A)
_MulticastIfAssociateStaticMember_Type=CommandString
_MulticastIfAssociateStaticMember_Object=MibTableColumn
multicastIfAssociateStaticMember=_MulticastIfAssociateStaticMember_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,9),_MulticastIfAssociateStaticMember_Type())
multicastIfAssociateStaticMember.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfAssociateStaticMember.setStatus(_A)
class _MulticastIfMembersMax_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_MulticastIfMembersMax_Type.__name__=_D
_MulticastIfMembersMax_Object=MibTableColumn
multicastIfMembersMax=_MulticastIfMembersMax_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,10),_MulticastIfMembersMax_Type())
multicastIfMembersMax.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIfMembersMax.setStatus(_A)
class _MulticastIfNoOfStaticMembers_Type(Unsigned32):defaultValue=0
_MulticastIfNoOfStaticMembers_Type.__name__=_D
_MulticastIfNoOfStaticMembers_Object=MibTableColumn
multicastIfNoOfStaticMembers=_MulticastIfNoOfStaticMembers_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,11),_MulticastIfNoOfStaticMembers_Type())
multicastIfNoOfStaticMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfNoOfStaticMembers.setStatus(_A)
_MulticastIfMembershipFiltering_Type=CommandString
_MulticastIfMembershipFiltering_Object=MibTableColumn
multicastIfMembershipFiltering=_MulticastIfMembershipFiltering_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,12),_MulticastIfMembershipFiltering_Type())
multicastIfMembershipFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfMembershipFiltering.setStatus(_A)
_MulticastIfForwardingFiltering_Type=CommandString
_MulticastIfForwardingFiltering_Object=MibTableColumn
multicastIfForwardingFiltering=_MulticastIfForwardingFiltering_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,13),_MulticastIfForwardingFiltering_Type())
multicastIfForwardingFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfForwardingFiltering.setStatus(_A)
_MulticastIfDeleteMembers_Type=CommandString
_MulticastIfDeleteMembers_Object=MibTableColumn
multicastIfDeleteMembers=_MulticastIfDeleteMembers_Object((1,3,6,1,4,1,8708,2,37,2,2,1,1,15),_MulticastIfDeleteMembers_Type())
multicastIfDeleteMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIfDeleteMembers.setStatus(_A)
_MulticastMembershipList_ObjectIdentity=ObjectIdentity
multicastMembershipList=_MulticastMembershipList_ObjectIdentity((1,3,6,1,4,1,8708,2,37,2,3))
_MulticastMembershipTable_Object=MibTable
multicastMembershipTable=_MulticastMembershipTable_Object((1,3,6,1,4,1,8708,2,37,2,3,1))
if mibBuilder.loadTexts:multicastMembershipTable.setStatus(_A)
_MulticastMembershipEntry_Object=MibTableRow
multicastMembershipEntry=_MulticastMembershipEntry_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1))
multicastMembershipEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:multicastMembershipEntry.setStatus(_A)
class _MulticastMembershipIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MulticastMembershipIndex_Type.__name__=_D
_MulticastMembershipIndex_Object=MibTableColumn
multicastMembershipIndex=_MulticastMembershipIndex_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,1),_MulticastMembershipIndex_Type())
multicastMembershipIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastMembershipIndex.setStatus(_A)
_MulticastMembershipName_Type=MgmtNameString
_MulticastMembershipName_Object=MibTableColumn
multicastMembershipName=_MulticastMembershipName_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,2),_MulticastMembershipName_Type())
multicastMembershipName.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastMembershipName.setStatus(_A)
class _MulticastMembershipInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MulticastMembershipInternalReference_Type.__name__=_D
_MulticastMembershipInternalReference_Object=MibTableColumn
multicastMembershipInternalReference=_MulticastMembershipInternalReference_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,3),_MulticastMembershipInternalReference_Type())
multicastMembershipInternalReference.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastMembershipInternalReference.setStatus(_A)
class _MulticastMembershipIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,21))
_MulticastMembershipIdentifier_Type.__name__=_J
_MulticastMembershipIdentifier_Object=MibTableColumn
multicastMembershipIdentifier=_MulticastMembershipIdentifier_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,4),_MulticastMembershipIdentifier_Type())
multicastMembershipIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastMembershipIdentifier.setStatus(_A)
class _MulticastMembershipSource_Type(IpAddress):defaultHexValue='00000000'
_MulticastMembershipSource_Type.__name__=_U
_MulticastMembershipSource_Object=MibTableColumn
multicastMembershipSource=_MulticastMembershipSource_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,5),_MulticastMembershipSource_Type())
multicastMembershipSource.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastMembershipSource.setStatus(_A)
_MulticastMembershipGroup_Type=IpAddress
_MulticastMembershipGroup_Object=MibTableColumn
multicastMembershipGroup=_MulticastMembershipGroup_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,6),_MulticastMembershipGroup_Type())
multicastMembershipGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastMembershipGroup.setStatus(_A)
class _MulticastMembershipVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MulticastMembershipVlan_Type.__name__=_D
_MulticastMembershipVlan_Object=MibTableColumn
multicastMembershipVlan=_MulticastMembershipVlan_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,7),_MulticastMembershipVlan_Type())
multicastMembershipVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastMembershipVlan.setStatus(_A)
class _MulticastMembershipPorts_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MulticastMembershipPorts_Type.__name__=_D
_MulticastMembershipPorts_Object=MibTableColumn
multicastMembershipPorts=_MulticastMembershipPorts_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,8),_MulticastMembershipPorts_Type())
multicastMembershipPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastMembershipPorts.setStatus(_A)
class _MulticastMembershipUpTime_Type(TimeTicks):defaultValue=0
_MulticastMembershipUpTime_Type.__name__=_I
_MulticastMembershipUpTime_Object=MibTableColumn
multicastMembershipUpTime=_MulticastMembershipUpTime_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,9),_MulticastMembershipUpTime_Type())
multicastMembershipUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastMembershipUpTime.setStatus(_A)
class _MulticastMembershipExpiryTime_Type(TimeTicks):defaultValue=0
_MulticastMembershipExpiryTime_Type.__name__=_I
_MulticastMembershipExpiryTime_Object=MibTableColumn
multicastMembershipExpiryTime=_MulticastMembershipExpiryTime_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,10),_MulticastMembershipExpiryTime_Type())
multicastMembershipExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastMembershipExpiryTime.setStatus(_A)
class _MulticastMembershipType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('dynamic',2)))
_MulticastMembershipType_Type.__name__=_H
_MulticastMembershipType_Object=MibTableColumn
multicastMembershipType=_MulticastMembershipType_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,11),_MulticastMembershipType_Type())
multicastMembershipType.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastMembershipType.setStatus(_A)
_MulticastMembershipReporter_Type=IpAddress
_MulticastMembershipReporter_Object=MibTableColumn
multicastMembershipReporter=_MulticastMembershipReporter_Object((1,3,6,1,4,1,8708,2,37,2,3,1,1,12),_MulticastMembershipReporter_Type())
multicastMembershipReporter.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastMembershipReporter.setStatus(_A)
_MulticastForwardingList_ObjectIdentity=ObjectIdentity
multicastForwardingList=_MulticastForwardingList_ObjectIdentity((1,3,6,1,4,1,8708,2,37,2,4))
_MulticastForwardingTable_Object=MibTable
multicastForwardingTable=_MulticastForwardingTable_Object((1,3,6,1,4,1,8708,2,37,2,4,1))
if mibBuilder.loadTexts:multicastForwardingTable.setStatus(_A)
_MulticastForwardingEntry_Object=MibTableRow
multicastForwardingEntry=_MulticastForwardingEntry_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1))
multicastForwardingEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:multicastForwardingEntry.setStatus(_A)
class _MulticastForwardingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MulticastForwardingIndex_Type.__name__=_D
_MulticastForwardingIndex_Object=MibTableColumn
multicastForwardingIndex=_MulticastForwardingIndex_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,1),_MulticastForwardingIndex_Type())
multicastForwardingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastForwardingIndex.setStatus(_A)
_MulticastForwardingName_Type=MgmtNameString
_MulticastForwardingName_Object=MibTableColumn
multicastForwardingName=_MulticastForwardingName_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,2),_MulticastForwardingName_Type())
multicastForwardingName.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastForwardingName.setStatus(_A)
class _MulticastForwardingInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MulticastForwardingInternalReference_Type.__name__=_D
_MulticastForwardingInternalReference_Object=MibTableColumn
multicastForwardingInternalReference=_MulticastForwardingInternalReference_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,3),_MulticastForwardingInternalReference_Type())
multicastForwardingInternalReference.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastForwardingInternalReference.setStatus(_A)
_MulticastForwardingSource_Type=IpAddress
_MulticastForwardingSource_Object=MibTableColumn
multicastForwardingSource=_MulticastForwardingSource_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,4),_MulticastForwardingSource_Type())
multicastForwardingSource.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastForwardingSource.setStatus(_A)
_MulticastForwardingGroup_Type=IpAddress
_MulticastForwardingGroup_Object=MibTableColumn
multicastForwardingGroup=_MulticastForwardingGroup_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,5),_MulticastForwardingGroup_Type())
multicastForwardingGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastForwardingGroup.setStatus(_A)
class _MulticastForwardingVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MulticastForwardingVlan_Type.__name__=_D
_MulticastForwardingVlan_Object=MibTableColumn
multicastForwardingVlan=_MulticastForwardingVlan_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,6),_MulticastForwardingVlan_Type())
multicastForwardingVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastForwardingVlan.setStatus(_A)
_MulticastForwardingFwd_Type=TruthValue
_MulticastForwardingFwd_Object=MibTableColumn
multicastForwardingFwd=_MulticastForwardingFwd_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,7),_MulticastForwardingFwd_Type())
multicastForwardingFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastForwardingFwd.setStatus(_A)
class _MulticastForwardingPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MulticastForwardingPorts_Type.__name__=_D
_MulticastForwardingPorts_Object=MibTableColumn
multicastForwardingPorts=_MulticastForwardingPorts_Object((1,3,6,1,4,1,8708,2,37,2,4,1,1,8),_MulticastForwardingPorts_Type())
multicastForwardingPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:multicastForwardingPorts.setStatus(_A)
_MulticastIgmpPmList_ObjectIdentity=ObjectIdentity
multicastIgmpPmList=_MulticastIgmpPmList_ObjectIdentity((1,3,6,1,4,1,8708,2,37,2,5))
_MulticastIgmpPmTable_Object=MibTable
multicastIgmpPmTable=_MulticastIgmpPmTable_Object((1,3,6,1,4,1,8708,2,37,2,5,1))
if mibBuilder.loadTexts:multicastIgmpPmTable.setStatus(_A)
_MulticastIgmpPmEntry_Object=MibTableRow
multicastIgmpPmEntry=_MulticastIgmpPmEntry_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1))
multicastIgmpPmEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:multicastIgmpPmEntry.setStatus(_A)
class _MulticastIgmpPmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MulticastIgmpPmIndex_Type.__name__=_D
_MulticastIgmpPmIndex_Object=MibTableColumn
multicastIgmpPmIndex=_MulticastIgmpPmIndex_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,1),_MulticastIgmpPmIndex_Type())
multicastIgmpPmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmIndex.setStatus(_A)
_MulticastIgmpPmName_Type=MgmtNameString
_MulticastIgmpPmName_Object=MibTableColumn
multicastIgmpPmName=_MulticastIgmpPmName_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,2),_MulticastIgmpPmName_Type())
multicastIgmpPmName.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmName.setStatus(_A)
_MulticastIgmpPmRxReportsV1_Type=Gauge32
_MulticastIgmpPmRxReportsV1_Object=MibTableColumn
multicastIgmpPmRxReportsV1=_MulticastIgmpPmRxReportsV1_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,3),_MulticastIgmpPmRxReportsV1_Type())
multicastIgmpPmRxReportsV1.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxReportsV1.setStatus(_A)
_MulticastIgmpPmRxReportsV2_Type=Gauge32
_MulticastIgmpPmRxReportsV2_Object=MibTableColumn
multicastIgmpPmRxReportsV2=_MulticastIgmpPmRxReportsV2_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,4),_MulticastIgmpPmRxReportsV2_Type())
multicastIgmpPmRxReportsV2.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxReportsV2.setStatus(_A)
_MulticastIgmpPmRxReportsV3_Type=Gauge32
_MulticastIgmpPmRxReportsV3_Object=MibTableColumn
multicastIgmpPmRxReportsV3=_MulticastIgmpPmRxReportsV3_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,5),_MulticastIgmpPmRxReportsV3_Type())
multicastIgmpPmRxReportsV3.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxReportsV3.setStatus(_A)
_MulticastIgmpPmTxReportsV1_Type=Gauge32
_MulticastIgmpPmTxReportsV1_Object=MibTableColumn
multicastIgmpPmTxReportsV1=_MulticastIgmpPmTxReportsV1_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,6),_MulticastIgmpPmTxReportsV1_Type())
multicastIgmpPmTxReportsV1.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmTxReportsV1.setStatus(_A)
_MulticastIgmpPmTxReportsV2_Type=Gauge32
_MulticastIgmpPmTxReportsV2_Object=MibTableColumn
multicastIgmpPmTxReportsV2=_MulticastIgmpPmTxReportsV2_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,7),_MulticastIgmpPmTxReportsV2_Type())
multicastIgmpPmTxReportsV2.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmTxReportsV2.setStatus(_A)
_MulticastIgmpPmTxReportsV3_Type=Gauge32
_MulticastIgmpPmTxReportsV3_Object=MibTableColumn
multicastIgmpPmTxReportsV3=_MulticastIgmpPmTxReportsV3_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,8),_MulticastIgmpPmTxReportsV3_Type())
multicastIgmpPmTxReportsV3.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmTxReportsV3.setStatus(_A)
_MulticastIgmpPmRxQueries_Type=Gauge32
_MulticastIgmpPmRxQueries_Object=MibTableColumn
multicastIgmpPmRxQueries=_MulticastIgmpPmRxQueries_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,9),_MulticastIgmpPmRxQueries_Type())
multicastIgmpPmRxQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxQueries.setStatus(_A)
_MulticastIgmpPmTxQueries_Type=Gauge32
_MulticastIgmpPmTxQueries_Object=MibTableColumn
multicastIgmpPmTxQueries=_MulticastIgmpPmTxQueries_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,10),_MulticastIgmpPmTxQueries_Type())
multicastIgmpPmTxQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmTxQueries.setStatus(_A)
_MulticastIgmpPmRxLeavesV2_Type=Gauge32
_MulticastIgmpPmRxLeavesV2_Object=MibTableColumn
multicastIgmpPmRxLeavesV2=_MulticastIgmpPmRxLeavesV2_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,11),_MulticastIgmpPmRxLeavesV2_Type())
multicastIgmpPmRxLeavesV2.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxLeavesV2.setStatus(_A)
_MulticastIgmpPmTxLeavesV2_Type=Gauge32
_MulticastIgmpPmTxLeavesV2_Object=MibTableColumn
multicastIgmpPmTxLeavesV2=_MulticastIgmpPmTxLeavesV2_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,12),_MulticastIgmpPmTxLeavesV2_Type())
multicastIgmpPmTxLeavesV2.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmTxLeavesV2.setStatus(_A)
_MulticastIgmpPmRxChksumErrors_Type=Gauge32
_MulticastIgmpPmRxChksumErrors_Object=MibTableColumn
multicastIgmpPmRxChksumErrors=_MulticastIgmpPmRxChksumErrors_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,13),_MulticastIgmpPmRxChksumErrors_Type())
multicastIgmpPmRxChksumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxChksumErrors.setStatus(_A)
_MulticastIgmpPmRxUnknownType_Type=Gauge32
_MulticastIgmpPmRxUnknownType_Object=MibTableColumn
multicastIgmpPmRxUnknownType=_MulticastIgmpPmRxUnknownType_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,14),_MulticastIgmpPmRxUnknownType_Type())
multicastIgmpPmRxUnknownType.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxUnknownType.setStatus(_A)
_MulticastIgmpPmRxIllegalLength_Type=Gauge32
_MulticastIgmpPmRxIllegalLength_Object=MibTableColumn
multicastIgmpPmRxIllegalLength=_MulticastIgmpPmRxIllegalLength_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,15),_MulticastIgmpPmRxIllegalLength_Type())
multicastIgmpPmRxIllegalLength.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmRxIllegalLength.setStatus(_A)
_MulticastIgmpPmDropHosts_Type=Gauge32
_MulticastIgmpPmDropHosts_Object=MibTableColumn
multicastIgmpPmDropHosts=_MulticastIgmpPmDropHosts_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,16),_MulticastIgmpPmDropHosts_Type())
multicastIgmpPmDropHosts.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmDropHosts.setStatus(_A)
_MulticastIgmpPmMembers_Type=Gauge32
_MulticastIgmpPmMembers_Object=MibTableColumn
multicastIgmpPmMembers=_MulticastIgmpPmMembers_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,17),_MulticastIgmpPmMembers_Type())
multicastIgmpPmMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:multicastIgmpPmMembers.setStatus(_A)
class _MulticastIgmpPmReset_Type(PmReset):defaultValue=1
_MulticastIgmpPmReset_Type.__name__=_T
_MulticastIgmpPmReset_Object=MibTableColumn
multicastIgmpPmReset=_MulticastIgmpPmReset_Object((1,3,6,1,4,1,8708,2,37,2,5,1,1,18),_MulticastIgmpPmReset_Type())
multicastIgmpPmReset.setMaxAccess(_F)
if mibBuilder.loadTexts:multicastIgmpPmReset.setStatus(_A)
multicastGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,37,1,1,1))
multicastGeneralGroupV1.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:multicastGeneralGroupV1.setStatus(_A)
multicastIfGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,37,1,1,2))
multicastIfGroupV1.setObjects(*((_B,_K),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:multicastIfGroupV1.setStatus(_A)
multicastMembershipGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,37,1,1,3))
multicastMembershipGroupV1.setObjects(*((_B,_L),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:multicastMembershipGroupV1.setStatus(_A)
multicastForwardingGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,37,1,1,4))
multicastForwardingGroupV1.setObjects(*((_B,_M),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:multicastForwardingGroupV1.setStatus(_A)
multicastIgmpPmGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,37,1,1,5))
multicastIgmpPmGroupV1.setObjects(*((_B,_N),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:multicastIgmpPmGroupV1.setStatus(_A)
lumMulticastBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,37,1,2,3))
lumMulticastBasicComplV1.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:lumMulticastBasicComplV1.setStatus('deprecated')
lumMulticastBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,37,1,2,4))
lumMulticastBasicComplV2.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:lumMulticastBasicComplV2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumMulticastMIBModule':lumMulticastMIBModule,'lumMulticastConfs':lumMulticastConfs,'lumMulticastGroups':lumMulticastGroups,_O:multicastGeneralGroupV1,_P:multicastIfGroupV1,_Q:multicastMembershipGroupV1,_R:multicastForwardingGroupV1,_S:multicastIgmpPmGroupV1,'lumMulticastCompl':lumMulticastCompl,'lumMulticastBasicComplV1':lumMulticastBasicComplV1,'lumMulticastBasicComplV2':lumMulticastBasicComplV2,'lumMulticastMIBObjects':lumMulticastMIBObjects,'multicastGeneral':multicastGeneral,_V:multicastGeneralLastChangeTime,_W:multicastGeneralStateLastChangeTime,_X:multicastGeneralMulticastIfTableSize,_Y:multicastGeneralMulticastMembershipTableSize,'multicastGeneralMulticastForwardingTableSize':multicastGeneralMulticastForwardingTableSize,'multicastGeneralPmIgmpPortTableSize':multicastGeneralPmIgmpPortTableSize,'multicastIfList':multicastIfList,'multicastIfTable':multicastIfTable,'multicastIfEntry':multicastIfEntry,_K:multicastIfIndex,_Z:multicastIfName,_a:multicastIfDescr,_b:multicastIfProtocol,_c:multicastIfRouterEnable,_d:multicastIfFastLeave,_f:multicastIfRobustness,_e:multicastIfReservedFlooding,_g:multicastIfAssociateStaticMember,_h:multicastIfMembersMax,_i:multicastIfNoOfStaticMembers,_j:multicastIfMembershipFiltering,_k:multicastIfForwardingFiltering,_l:multicastIfDeleteMembers,'multicastMembershipList':multicastMembershipList,'multicastMembershipTable':multicastMembershipTable,'multicastMembershipEntry':multicastMembershipEntry,_L:multicastMembershipIndex,_m:multicastMembershipName,_n:multicastMembershipInternalReference,_o:multicastMembershipIdentifier,_p:multicastMembershipSource,_q:multicastMembershipGroup,_r:multicastMembershipVlan,_s:multicastMembershipPorts,_t:multicastMembershipUpTime,_u:multicastMembershipExpiryTime,_v:multicastMembershipType,_w:multicastMembershipReporter,'multicastForwardingList':multicastForwardingList,'multicastForwardingTable':multicastForwardingTable,'multicastForwardingEntry':multicastForwardingEntry,_M:multicastForwardingIndex,_x:multicastForwardingName,_y:multicastForwardingInternalReference,_z:multicastForwardingSource,_A0:multicastForwardingGroup,_A1:multicastForwardingVlan,_A2:multicastForwardingFwd,_A3:multicastForwardingPorts,'multicastIgmpPmList':multicastIgmpPmList,'multicastIgmpPmTable':multicastIgmpPmTable,'multicastIgmpPmEntry':multicastIgmpPmEntry,_N:multicastIgmpPmIndex,_A4:multicastIgmpPmName,_A5:multicastIgmpPmRxReportsV1,_A6:multicastIgmpPmRxReportsV2,_A7:multicastIgmpPmRxReportsV3,_A8:multicastIgmpPmTxReportsV1,_A9:multicastIgmpPmTxReportsV2,_AA:multicastIgmpPmTxReportsV3,_AB:multicastIgmpPmRxQueries,_AC:multicastIgmpPmTxQueries,_AD:multicastIgmpPmRxLeavesV2,_AE:multicastIgmpPmTxLeavesV2,_AF:multicastIgmpPmRxChksumErrors,_AG:multicastIgmpPmRxUnknownType,_AH:multicastIgmpPmRxIllegalLength,_AI:multicastIgmpPmDropHosts,_AJ:multicastIgmpPmMembers,_AK:multicastIgmpPmReset})