_l='myIgmpSnoopingMIBGroup'
_k='mySNIgmpQueryResponeTime'
_j='mySNIgmpGDAConfigStatus'
_i='mySNIgmpGDAConfigType'
_h='mySNIgmpGDAConfigIfIndex'
_g='mySNIgmpFilteringMaxGroups'
_f='mySNIgmpFilteringProfile'
_e='mySNIgmpMrLearnStatus'
_d='mySNIgmpSvglProfile'
_c='mySNIgmpSvglVID'
_b='mySNIgmpGDATrunkMemberAction'
_a='mySNIgmpGDAPortMemberAction'
_Z='mySNIgmpGDANumber'
_Y='mySNIgmpPortRouterProfile'
_X='mySNIgmpPortRouterState'
_W='mySNIgmpSrcIpCheckEntryStatus'
_V='mySNIgmpSrcIpCheckSrcIpAddr'
_U='mySNIgmpSourceIpCheckDefIp'
_T='mySNIgmpSourceIpCheck'
_S='mySNIgmpSourcePortCheck'
_R='mySNIgmpWorkingMode'
_Q='mySNIgmpGDAConfigAddr'
_P='mySNIgmpGDAConfigVID'
_O='mySNPortIndex'
_N='mySNIgmpMrLearnVID'
_M='mySNIgmpGDAAddr'
_L='mySNIgmpGDAVID'
_K='mySNIgmpPortIndex'
_J='mySNIgmpPortRouterVID'
_I='mandatory'
_H='mySNIgmpSrcIpCheckMultiIpAddr'
_G='mySNIgmpSrcIpCheckVID'
_F='EnabledStatus'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='current'
_A='DES7200-IGMP-SNOOPING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myIgmpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,8))
if mibBuilder.loadTexts:myIgmpSnoopingMIB.setRevisions(('2002-03-20 00:00',))
_MyIgmpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
myIgmpSnoopingMIBObjects=_MyIgmpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,8,1))
class _MySNIgmpWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('svgl',2),('ivgl',3),('ivgl-svgl',4)))
_MySNIgmpWorkingMode_Type.__name__=_E
_MySNIgmpWorkingMode_Object=MibScalar
mySNIgmpWorkingMode=_MySNIgmpWorkingMode_Object((1,3,6,1,4,1,171,10,97,2,8,1,1),_MySNIgmpWorkingMode_Type())
mySNIgmpWorkingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpWorkingMode.setStatus(_B)
class _MySNIgmpSourcePortCheck_Type(EnabledStatus):defaultValue=2
_MySNIgmpSourcePortCheck_Type.__name__=_F
_MySNIgmpSourcePortCheck_Object=MibScalar
mySNIgmpSourcePortCheck=_MySNIgmpSourcePortCheck_Object((1,3,6,1,4,1,171,10,97,2,8,1,2),_MySNIgmpSourcePortCheck_Type())
mySNIgmpSourcePortCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpSourcePortCheck.setStatus(_B)
class _MySNIgmpSourceIpCheck_Type(EnabledStatus):defaultValue=2
_MySNIgmpSourceIpCheck_Type.__name__=_F
_MySNIgmpSourceIpCheck_Object=MibScalar
mySNIgmpSourceIpCheck=_MySNIgmpSourceIpCheck_Object((1,3,6,1,4,1,171,10,97,2,8,1,3),_MySNIgmpSourceIpCheck_Type())
mySNIgmpSourceIpCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpSourceIpCheck.setStatus(_B)
_MySNIgmpSourceIpCheckDefIp_Type=IpAddress
_MySNIgmpSourceIpCheckDefIp_Object=MibScalar
mySNIgmpSourceIpCheckDefIp=_MySNIgmpSourceIpCheckDefIp_Object((1,3,6,1,4,1,171,10,97,2,8,1,4),_MySNIgmpSourceIpCheckDefIp_Type())
mySNIgmpSourceIpCheckDefIp.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpSourceIpCheckDefIp.setStatus(_B)
_MySNIgmpSrcIpCheckTable_Object=MibTable
mySNIgmpSrcIpCheckTable=_MySNIgmpSrcIpCheckTable_Object((1,3,6,1,4,1,171,10,97,2,8,1,5))
if mibBuilder.loadTexts:mySNIgmpSrcIpCheckTable.setStatus(_B)
_MySNIgmpSrcIpCheckEntry_Object=MibTableRow
mySNIgmpSrcIpCheckEntry=_MySNIgmpSrcIpCheckEntry_Object((1,3,6,1,4,1,171,10,97,2,8,1,5,1))
mySNIgmpSrcIpCheckEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:mySNIgmpSrcIpCheckEntry.setStatus(_B)
_MySNIgmpSrcIpCheckVID_Type=VlanId
_MySNIgmpSrcIpCheckVID_Object=MibTableColumn
mySNIgmpSrcIpCheckVID=_MySNIgmpSrcIpCheckVID_Object((1,3,6,1,4,1,171,10,97,2,8,1,5,1,1),_MySNIgmpSrcIpCheckVID_Type())
mySNIgmpSrcIpCheckVID.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpSrcIpCheckVID.setStatus(_B)
_MySNIgmpSrcIpCheckMultiIpAddr_Type=IpAddress
_MySNIgmpSrcIpCheckMultiIpAddr_Object=MibTableColumn
mySNIgmpSrcIpCheckMultiIpAddr=_MySNIgmpSrcIpCheckMultiIpAddr_Object((1,3,6,1,4,1,171,10,97,2,8,1,5,1,2),_MySNIgmpSrcIpCheckMultiIpAddr_Type())
mySNIgmpSrcIpCheckMultiIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpSrcIpCheckMultiIpAddr.setStatus(_B)
_MySNIgmpSrcIpCheckSrcIpAddr_Type=IpAddress
_MySNIgmpSrcIpCheckSrcIpAddr_Object=MibTableColumn
mySNIgmpSrcIpCheckSrcIpAddr=_MySNIgmpSrcIpCheckSrcIpAddr_Object((1,3,6,1,4,1,171,10,97,2,8,1,5,1,3),_MySNIgmpSrcIpCheckSrcIpAddr_Type())
mySNIgmpSrcIpCheckSrcIpAddr.setMaxAccess('read-create')
if mibBuilder.loadTexts:mySNIgmpSrcIpCheckSrcIpAddr.setStatus(_B)
class _MySNIgmpSrcIpCheckEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('delete',2)))
_MySNIgmpSrcIpCheckEntryStatus_Type.__name__=_E
_MySNIgmpSrcIpCheckEntryStatus_Object=MibTableColumn
mySNIgmpSrcIpCheckEntryStatus=_MySNIgmpSrcIpCheckEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,8,1,5,1,4),_MySNIgmpSrcIpCheckEntryStatus_Type())
mySNIgmpSrcIpCheckEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpSrcIpCheckEntryStatus.setStatus(_B)
_MySNIgmpPortTable_Object=MibTable
mySNIgmpPortTable=_MySNIgmpPortTable_Object((1,3,6,1,4,1,171,10,97,2,8,1,6))
if mibBuilder.loadTexts:mySNIgmpPortTable.setStatus(_I)
_MySNIgmpPortEntry_Object=MibTableRow
mySNIgmpPortEntry=_MySNIgmpPortEntry_Object((1,3,6,1,4,1,171,10,97,2,8,1,6,1))
mySNIgmpPortEntry.setIndexNames((0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:mySNIgmpPortEntry.setStatus(_I)
_MySNIgmpPortRouterVID_Type=VlanId
_MySNIgmpPortRouterVID_Object=MibTableColumn
mySNIgmpPortRouterVID=_MySNIgmpPortRouterVID_Object((1,3,6,1,4,1,171,10,97,2,8,1,6,1,1),_MySNIgmpPortRouterVID_Type())
mySNIgmpPortRouterVID.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpPortRouterVID.setStatus(_B)
_MySNIgmpPortIndex_Type=IfIndex
_MySNIgmpPortIndex_Object=MibTableColumn
mySNIgmpPortIndex=_MySNIgmpPortIndex_Object((1,3,6,1,4,1,171,10,97,2,8,1,6,1,2),_MySNIgmpPortIndex_Type())
mySNIgmpPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpPortIndex.setStatus(_I)
class _MySNIgmpPortRouterState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mrnone',1),('mrstatic',2),('mrdynamic',3)))
_MySNIgmpPortRouterState_Type.__name__=_E
_MySNIgmpPortRouterState_Object=MibTableColumn
mySNIgmpPortRouterState=_MySNIgmpPortRouterState_Object((1,3,6,1,4,1,171,10,97,2,8,1,6,1,3),_MySNIgmpPortRouterState_Type())
mySNIgmpPortRouterState.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpPortRouterState.setStatus(_B)
_MySNIgmpPortRouterProfile_Type=Unsigned32
_MySNIgmpPortRouterProfile_Object=MibTableColumn
mySNIgmpPortRouterProfile=_MySNIgmpPortRouterProfile_Object((1,3,6,1,4,1,171,10,97,2,8,1,6,1,4),_MySNIgmpPortRouterProfile_Type())
mySNIgmpPortRouterProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpPortRouterProfile.setStatus(_B)
_MySNIgmpGDANumber_Type=Unsigned32
_MySNIgmpGDANumber_Object=MibScalar
mySNIgmpGDANumber=_MySNIgmpGDANumber_Object((1,3,6,1,4,1,171,10,97,2,8,1,7),_MySNIgmpGDANumber_Type())
mySNIgmpGDANumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDANumber.setStatus(_B)
_MySNIgmpGDATable_Object=MibTable
mySNIgmpGDATable=_MySNIgmpGDATable_Object((1,3,6,1,4,1,171,10,97,2,8,1,8))
if mibBuilder.loadTexts:mySNIgmpGDATable.setStatus(_B)
_MySNIgmpGDAEntry_Object=MibTableRow
mySNIgmpGDAEntry=_MySNIgmpGDAEntry_Object((1,3,6,1,4,1,171,10,97,2,8,1,8,1))
mySNIgmpGDAEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:mySNIgmpGDAEntry.setStatus(_B)
_MySNIgmpGDAVID_Type=VlanId
_MySNIgmpGDAVID_Object=MibTableColumn
mySNIgmpGDAVID=_MySNIgmpGDAVID_Object((1,3,6,1,4,1,171,10,97,2,8,1,8,1,1),_MySNIgmpGDAVID_Type())
mySNIgmpGDAVID.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAVID.setStatus(_B)
_MySNIgmpGDAAddr_Type=IpAddress
_MySNIgmpGDAAddr_Object=MibTableColumn
mySNIgmpGDAAddr=_MySNIgmpGDAAddr_Object((1,3,6,1,4,1,171,10,97,2,8,1,8,1,2),_MySNIgmpGDAAddr_Type())
mySNIgmpGDAAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAAddr.setStatus(_B)
_MySNIgmpGDAPortMemberAction_Type=MemberMap
_MySNIgmpGDAPortMemberAction_Object=MibTableColumn
mySNIgmpGDAPortMemberAction=_MySNIgmpGDAPortMemberAction_Object((1,3,6,1,4,1,171,10,97,2,8,1,8,1,3),_MySNIgmpGDAPortMemberAction_Type())
mySNIgmpGDAPortMemberAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpGDAPortMemberAction.setStatus(_B)
_MySNIgmpGDATrunkMemberAction_Type=MemberMap
_MySNIgmpGDATrunkMemberAction_Object=MibTableColumn
mySNIgmpGDATrunkMemberAction=_MySNIgmpGDATrunkMemberAction_Object((1,3,6,1,4,1,171,10,97,2,8,1,8,1,4),_MySNIgmpGDATrunkMemberAction_Type())
mySNIgmpGDATrunkMemberAction.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpGDATrunkMemberAction.setStatus(_B)
_MySNIgmpSvglVID_Type=Integer32
_MySNIgmpSvglVID_Object=MibScalar
mySNIgmpSvglVID=_MySNIgmpSvglVID_Object((1,3,6,1,4,1,171,10,97,2,8,1,9),_MySNIgmpSvglVID_Type())
mySNIgmpSvglVID.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpSvglVID.setStatus(_B)
_MySNIgmpSvglProfile_Type=Unsigned32
_MySNIgmpSvglProfile_Object=MibScalar
mySNIgmpSvglProfile=_MySNIgmpSvglProfile_Object((1,3,6,1,4,1,171,10,97,2,8,1,10),_MySNIgmpSvglProfile_Type())
mySNIgmpSvglProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpSvglProfile.setStatus(_B)
_MySNIgmpMrLearnTable_Object=MibTable
mySNIgmpMrLearnTable=_MySNIgmpMrLearnTable_Object((1,3,6,1,4,1,171,10,97,2,8,1,11))
if mibBuilder.loadTexts:mySNIgmpMrLearnTable.setStatus(_B)
_MySNIgmpMrLearnEntry_Object=MibTableRow
mySNIgmpMrLearnEntry=_MySNIgmpMrLearnEntry_Object((1,3,6,1,4,1,171,10,97,2,8,1,11,1))
mySNIgmpMrLearnEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:mySNIgmpMrLearnEntry.setStatus(_B)
_MySNIgmpMrLearnVID_Type=VlanId
_MySNIgmpMrLearnVID_Object=MibTableColumn
mySNIgmpMrLearnVID=_MySNIgmpMrLearnVID_Object((1,3,6,1,4,1,171,10,97,2,8,1,11,1,1),_MySNIgmpMrLearnVID_Type())
mySNIgmpMrLearnVID.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpMrLearnVID.setStatus(_B)
class _MySNIgmpMrLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('pim-dvmrp',2)))
_MySNIgmpMrLearnStatus_Type.__name__=_E
_MySNIgmpMrLearnStatus_Object=MibTableColumn
mySNIgmpMrLearnStatus=_MySNIgmpMrLearnStatus_Object((1,3,6,1,4,1,171,10,97,2,8,1,11,1,2),_MySNIgmpMrLearnStatus_Type())
mySNIgmpMrLearnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpMrLearnStatus.setStatus(_B)
_MySNIgmpPortFilteringTable_Object=MibTable
mySNIgmpPortFilteringTable=_MySNIgmpPortFilteringTable_Object((1,3,6,1,4,1,171,10,97,2,8,1,12))
if mibBuilder.loadTexts:mySNIgmpPortFilteringTable.setStatus(_B)
_MySNIgmpPortFilteringEntry_Object=MibTableRow
mySNIgmpPortFilteringEntry=_MySNIgmpPortFilteringEntry_Object((1,3,6,1,4,1,171,10,97,2,8,1,12,1))
mySNIgmpPortFilteringEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:mySNIgmpPortFilteringEntry.setStatus(_B)
_MySNPortIndex_Type=IfIndex
_MySNPortIndex_Object=MibTableColumn
mySNPortIndex=_MySNPortIndex_Object((1,3,6,1,4,1,171,10,97,2,8,1,12,1,1),_MySNPortIndex_Type())
mySNPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNPortIndex.setStatus(_B)
_MySNIgmpFilteringProfile_Type=Unsigned32
_MySNIgmpFilteringProfile_Object=MibTableColumn
mySNIgmpFilteringProfile=_MySNIgmpFilteringProfile_Object((1,3,6,1,4,1,171,10,97,2,8,1,12,1,2),_MySNIgmpFilteringProfile_Type())
mySNIgmpFilteringProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpFilteringProfile.setStatus(_B)
_MySNIgmpFilteringMaxGroups_Type=Unsigned32
_MySNIgmpFilteringMaxGroups_Object=MibTableColumn
mySNIgmpFilteringMaxGroups=_MySNIgmpFilteringMaxGroups_Object((1,3,6,1,4,1,171,10,97,2,8,1,12,1,3),_MySNIgmpFilteringMaxGroups_Type())
mySNIgmpFilteringMaxGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpFilteringMaxGroups.setStatus(_B)
_MySNIgmpGDAConfigTable_Object=MibTable
mySNIgmpGDAConfigTable=_MySNIgmpGDAConfigTable_Object((1,3,6,1,4,1,171,10,97,2,8,1,13))
if mibBuilder.loadTexts:mySNIgmpGDAConfigTable.setStatus(_B)
_MySNIgmpGDAConfigEntry_Object=MibTableRow
mySNIgmpGDAConfigEntry=_MySNIgmpGDAConfigEntry_Object((1,3,6,1,4,1,171,10,97,2,8,1,13,1))
mySNIgmpGDAConfigEntry.setIndexNames((0,_A,_P),(0,_A,_Q))
if mibBuilder.loadTexts:mySNIgmpGDAConfigEntry.setStatus(_B)
_MySNIgmpGDAConfigVID_Type=VlanId
_MySNIgmpGDAConfigVID_Object=MibTableColumn
mySNIgmpGDAConfigVID=_MySNIgmpGDAConfigVID_Object((1,3,6,1,4,1,171,10,97,2,8,1,13,1,1),_MySNIgmpGDAConfigVID_Type())
mySNIgmpGDAConfigVID.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAConfigVID.setStatus(_B)
_MySNIgmpGDAConfigAddr_Type=IpAddress
_MySNIgmpGDAConfigAddr_Object=MibTableColumn
mySNIgmpGDAConfigAddr=_MySNIgmpGDAConfigAddr_Object((1,3,6,1,4,1,171,10,97,2,8,1,13,1,2),_MySNIgmpGDAConfigAddr_Type())
mySNIgmpGDAConfigAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAConfigAddr.setStatus(_B)
_MySNIgmpGDAConfigIfIndex_Type=IfIndex
_MySNIgmpGDAConfigIfIndex_Object=MibTableColumn
mySNIgmpGDAConfigIfIndex=_MySNIgmpGDAConfigIfIndex_Object((1,3,6,1,4,1,171,10,97,2,8,1,13,1,3),_MySNIgmpGDAConfigIfIndex_Type())
mySNIgmpGDAConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAConfigIfIndex.setStatus(_B)
class _MySNIgmpGDAConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('null',1),('static',2),('dynamic',3),('mrouter',4)))
_MySNIgmpGDAConfigType_Type.__name__=_E
_MySNIgmpGDAConfigType_Object=MibTableColumn
mySNIgmpGDAConfigType=_MySNIgmpGDAConfigType_Object((1,3,6,1,4,1,171,10,97,2,8,1,13,1,4),_MySNIgmpGDAConfigType_Type())
mySNIgmpGDAConfigType.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAConfigType.setStatus(_B)
class _MySNIgmpGDAConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_MySNIgmpGDAConfigStatus_Type.__name__=_E
_MySNIgmpGDAConfigStatus_Object=MibTableColumn
mySNIgmpGDAConfigStatus=_MySNIgmpGDAConfigStatus_Object((1,3,6,1,4,1,171,10,97,2,8,1,13,1,5),_MySNIgmpGDAConfigStatus_Type())
mySNIgmpGDAConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mySNIgmpGDAConfigStatus.setStatus(_B)
_MySNIgmpQueryResponeTime_Type=Unsigned32
_MySNIgmpQueryResponeTime_Object=MibScalar
mySNIgmpQueryResponeTime=_MySNIgmpQueryResponeTime_Object((1,3,6,1,4,1,171,10,97,2,8,1,14),_MySNIgmpQueryResponeTime_Type())
mySNIgmpQueryResponeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mySNIgmpQueryResponeTime.setStatus(_B)
_MyIgmpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
myIgmpSnoopingMIBConformance=_MyIgmpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,8,2))
_MyIgmpSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
myIgmpSnoopingMIBCompliances=_MyIgmpSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,8,2,1))
_MyIgmpSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
myIgmpSnoopingMIBGroups=_MyIgmpSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,8,2,2))
myIgmpSnoopingMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,8,2,2,1))
myIgmpSnoopingMIBGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_G),(_A,_H),(_A,_V),(_A,_W),(_A,_J),(_A,_K),(_A,_X),(_A,_Y),(_A,_Z),(_A,_L),(_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_N),(_A,_e),(_A,_O),(_A,_f),(_A,_g),(_A,_P),(_A,_Q),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:myIgmpSnoopingMIBGroup.setStatus(_B)
myIgmpSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,8,2,1,1))
myIgmpSnoopingMIBCompliance.setObjects((_A,_l))
if mibBuilder.loadTexts:myIgmpSnoopingMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'myIgmpSnoopingMIB':myIgmpSnoopingMIB,'myIgmpSnoopingMIBObjects':myIgmpSnoopingMIBObjects,_R:mySNIgmpWorkingMode,_S:mySNIgmpSourcePortCheck,_T:mySNIgmpSourceIpCheck,_U:mySNIgmpSourceIpCheckDefIp,'mySNIgmpSrcIpCheckTable':mySNIgmpSrcIpCheckTable,'mySNIgmpSrcIpCheckEntry':mySNIgmpSrcIpCheckEntry,_G:mySNIgmpSrcIpCheckVID,_H:mySNIgmpSrcIpCheckMultiIpAddr,_V:mySNIgmpSrcIpCheckSrcIpAddr,_W:mySNIgmpSrcIpCheckEntryStatus,'mySNIgmpPortTable':mySNIgmpPortTable,'mySNIgmpPortEntry':mySNIgmpPortEntry,_J:mySNIgmpPortRouterVID,_K:mySNIgmpPortIndex,_X:mySNIgmpPortRouterState,_Y:mySNIgmpPortRouterProfile,_Z:mySNIgmpGDANumber,'mySNIgmpGDATable':mySNIgmpGDATable,'mySNIgmpGDAEntry':mySNIgmpGDAEntry,_L:mySNIgmpGDAVID,_M:mySNIgmpGDAAddr,_a:mySNIgmpGDAPortMemberAction,_b:mySNIgmpGDATrunkMemberAction,_c:mySNIgmpSvglVID,_d:mySNIgmpSvglProfile,'mySNIgmpMrLearnTable':mySNIgmpMrLearnTable,'mySNIgmpMrLearnEntry':mySNIgmpMrLearnEntry,_N:mySNIgmpMrLearnVID,_e:mySNIgmpMrLearnStatus,'mySNIgmpPortFilteringTable':mySNIgmpPortFilteringTable,'mySNIgmpPortFilteringEntry':mySNIgmpPortFilteringEntry,_O:mySNPortIndex,_f:mySNIgmpFilteringProfile,_g:mySNIgmpFilteringMaxGroups,'mySNIgmpGDAConfigTable':mySNIgmpGDAConfigTable,'mySNIgmpGDAConfigEntry':mySNIgmpGDAConfigEntry,_P:mySNIgmpGDAConfigVID,_Q:mySNIgmpGDAConfigAddr,_h:mySNIgmpGDAConfigIfIndex,_i:mySNIgmpGDAConfigType,_j:mySNIgmpGDAConfigStatus,_k:mySNIgmpQueryResponeTime,'myIgmpSnoopingMIBConformance':myIgmpSnoopingMIBConformance,'myIgmpSnoopingMIBCompliances':myIgmpSnoopingMIBCompliances,'myIgmpSnoopingMIBCompliance':myIgmpSnoopingMIBCompliance,'myIgmpSnoopingMIBGroups':myIgmpSnoopingMIBGroups,_l:myIgmpSnoopingMIBGroup})