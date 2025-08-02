_AI='qtechIgmpSnoopingMIBGroup2'
_AH='qtechIgmpSnoopingMIBGroup'
_AG='qtechIgmpSnoopingMulticastWlan'
_AF='qtechIgmpSnoopingGDAIfxAction'
_AE='qtechIgmpSnoopingFastleave'
_AD='qtechIgmpSnoopingReportSuppress'
_AC='qtechIgmpSnoopingQueryResponeTime'
_AB='qtechIgmpSnoopingFilteringMaxGroups'
_AA='qtechIgmpSnoopingFilteringProfile'
_A9='qtechIgmpSnoopingMrLearnStatus'
_A8='qtechIgmpSnoopingSvglProfile'
_A7='qtechIgmpSnoopingSvglVID'
_A6='qtechIgmpSnoopingVlanStatusStatus'
_A5='qtechIgmpSnoopingGDAPortMemberAction'
_A4='qtechIgmpSnoopingGDANumber'
_A3='qtechIgmpSnoopingWorkingMode'
_A2='qtechSNIgmpQueryResponeTime'
_A1='qtechSNIgmpGDAConfigStatus'
_A0='qtechSNIgmpGDAConfigType'
_z='qtechSNIgmpGDAConfigIfIndex'
_y='qtechSNIgmpFilteringMaxGroups'
_x='qtechSNIgmpFilteringProfile'
_w='qtechSNIgmpMrLearnStatus'
_v='qtechSNIgmpSvglProfile'
_u='qtechSNIgmpSvglVID'
_t='qtechSNIgmpGDATrunkMemberAction'
_s='qtechSNIgmpGDAPortMemberAction'
_r='qtechSNIgmpGDANumber'
_q='qtechSNIgmpPortRouterProfile'
_p='qtechSNIgmpPortRouterState'
_o='qtechSNIgmpSrcIpCheckEntryStatus'
_n='qtechSNIgmpSrcIpCheckSrcIpAddr'
_m='qtechSNIgmpSourceIpCheckDefIp'
_l='qtechSNIgmpSourceIpCheck'
_k='qtechSNIgmpSourcePortCheck'
_j='qtechSNIgmpWorkingMode'
_i='pim-dvmrp'
_h='disable'
_g='read-create'
_f='ivgl-svgl'
_e='qtechIgmpSnoopingGDAIfx'
_d='qtechIgmpSnoopingGDAGrp'
_c='qtechIgsmpSnoopingGDASrc'
_b='qtechIgmpSnoopingGDANewOutVID'
_a='qtechIgmpSnoopingGDANewInVID'
_Z='qtechIgmpSnoopingGDAConfigIfIndex'
_Y='qtechIgmpSnoopingGDAConfigAddr'
_X='qtechIgmpSnoopingGDAConfigVID'
_W='qtechIgmpSnoopingportIndex'
_V='qtechIgmpSnoopingMrLearnVID'
_U='qtechIgmpSnoopingVlanStatusVID'
_T='qtechIgmpSnoopingGDAAddr'
_S='qtechIgmpSnoopingGDAVID'
_R='qtechSNIgmpGDAConfigAddr'
_Q='qtechSNIgmpGDAConfigVID'
_P='qtechSNPortIndex'
_O='qtechSNIgmpMrLearnVID'
_N='qtechSNIgmpGDAAddr'
_M='qtechSNIgmpGDAVID'
_L='qtechSNIgmpPortIndex'
_K='qtechSNIgmpPortRouterVID'
_J='qtechSNIgmpSrcIpCheckMultiIpAddr'
_I='qtechSNIgmpSrcIpCheckVID'
_H='disabled'
_G='EnabledStatus'
_F='Integer32'
_E='read-only'
_D='read-write'
_C='current'
_B='deprecated'
_A='QTECH-IGMP-SNOOPING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,MemberMap=mibBuilder.importSymbols('QTECH-TC','IfIndex','MemberMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
qtechIgmpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,8))
if mibBuilder.loadTexts:qtechIgmpSnoopingMIB.setRevisions(('2009-10-22 00:00','2002-03-20 00:00'))
_QtechIgmpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
qtechIgmpSnoopingMIBObjects=_QtechIgmpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,8,1))
class _QtechSNIgmpWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('svgl',2),('ivgl',3),(_f,4)))
_QtechSNIgmpWorkingMode_Type.__name__=_F
_QtechSNIgmpWorkingMode_Object=MibScalar
qtechSNIgmpWorkingMode=_QtechSNIgmpWorkingMode_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,1),_QtechSNIgmpWorkingMode_Type())
qtechSNIgmpWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpWorkingMode.setStatus(_B)
class _QtechSNIgmpSourcePortCheck_Type(EnabledStatus):defaultValue=2
_QtechSNIgmpSourcePortCheck_Type.__name__=_G
_QtechSNIgmpSourcePortCheck_Object=MibScalar
qtechSNIgmpSourcePortCheck=_QtechSNIgmpSourcePortCheck_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,2),_QtechSNIgmpSourcePortCheck_Type())
qtechSNIgmpSourcePortCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpSourcePortCheck.setStatus(_B)
class _QtechSNIgmpSourceIpCheck_Type(EnabledStatus):defaultValue=2
_QtechSNIgmpSourceIpCheck_Type.__name__=_G
_QtechSNIgmpSourceIpCheck_Object=MibScalar
qtechSNIgmpSourceIpCheck=_QtechSNIgmpSourceIpCheck_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,3),_QtechSNIgmpSourceIpCheck_Type())
qtechSNIgmpSourceIpCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpSourceIpCheck.setStatus(_B)
_QtechSNIgmpSourceIpCheckDefIp_Type=IpAddress
_QtechSNIgmpSourceIpCheckDefIp_Object=MibScalar
qtechSNIgmpSourceIpCheckDefIp=_QtechSNIgmpSourceIpCheckDefIp_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,4),_QtechSNIgmpSourceIpCheckDefIp_Type())
qtechSNIgmpSourceIpCheckDefIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpSourceIpCheckDefIp.setStatus(_B)
_QtechSNIgmpSrcIpCheckTable_Object=MibTable
qtechSNIgmpSrcIpCheckTable=_QtechSNIgmpSrcIpCheckTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,5))
if mibBuilder.loadTexts:qtechSNIgmpSrcIpCheckTable.setStatus(_B)
_QtechSNIgmpSrcIpCheckEntry_Object=MibTableRow
qtechSNIgmpSrcIpCheckEntry=_QtechSNIgmpSrcIpCheckEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,5,1))
qtechSNIgmpSrcIpCheckEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:qtechSNIgmpSrcIpCheckEntry.setStatus(_B)
_QtechSNIgmpSrcIpCheckVID_Type=VlanId
_QtechSNIgmpSrcIpCheckVID_Object=MibTableColumn
qtechSNIgmpSrcIpCheckVID=_QtechSNIgmpSrcIpCheckVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,5,1,1),_QtechSNIgmpSrcIpCheckVID_Type())
qtechSNIgmpSrcIpCheckVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpSrcIpCheckVID.setStatus(_B)
_QtechSNIgmpSrcIpCheckMultiIpAddr_Type=IpAddress
_QtechSNIgmpSrcIpCheckMultiIpAddr_Object=MibTableColumn
qtechSNIgmpSrcIpCheckMultiIpAddr=_QtechSNIgmpSrcIpCheckMultiIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,5,1,2),_QtechSNIgmpSrcIpCheckMultiIpAddr_Type())
qtechSNIgmpSrcIpCheckMultiIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpSrcIpCheckMultiIpAddr.setStatus(_B)
_QtechSNIgmpSrcIpCheckSrcIpAddr_Type=IpAddress
_QtechSNIgmpSrcIpCheckSrcIpAddr_Object=MibTableColumn
qtechSNIgmpSrcIpCheckSrcIpAddr=_QtechSNIgmpSrcIpCheckSrcIpAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,5,1,3),_QtechSNIgmpSrcIpCheckSrcIpAddr_Type())
qtechSNIgmpSrcIpCheckSrcIpAddr.setMaxAccess(_g)
if mibBuilder.loadTexts:qtechSNIgmpSrcIpCheckSrcIpAddr.setStatus(_B)
class _QtechSNIgmpSrcIpCheckEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('delete',2)))
_QtechSNIgmpSrcIpCheckEntryStatus_Type.__name__=_F
_QtechSNIgmpSrcIpCheckEntryStatus_Object=MibTableColumn
qtechSNIgmpSrcIpCheckEntryStatus=_QtechSNIgmpSrcIpCheckEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,5,1,4),_QtechSNIgmpSrcIpCheckEntryStatus_Type())
qtechSNIgmpSrcIpCheckEntryStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:qtechSNIgmpSrcIpCheckEntryStatus.setStatus(_B)
_QtechSNIgmpPortTable_Object=MibTable
qtechSNIgmpPortTable=_QtechSNIgmpPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,6))
if mibBuilder.loadTexts:qtechSNIgmpPortTable.setStatus(_B)
_QtechSNIgmpPortEntry_Object=MibTableRow
qtechSNIgmpPortEntry=_QtechSNIgmpPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,6,1))
qtechSNIgmpPortEntry.setIndexNames((0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:qtechSNIgmpPortEntry.setStatus(_B)
_QtechSNIgmpPortRouterVID_Type=VlanId
_QtechSNIgmpPortRouterVID_Object=MibTableColumn
qtechSNIgmpPortRouterVID=_QtechSNIgmpPortRouterVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,6,1,1),_QtechSNIgmpPortRouterVID_Type())
qtechSNIgmpPortRouterVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpPortRouterVID.setStatus(_B)
_QtechSNIgmpPortIndex_Type=IfIndex
_QtechSNIgmpPortIndex_Object=MibTableColumn
qtechSNIgmpPortIndex=_QtechSNIgmpPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,6,1,2),_QtechSNIgmpPortIndex_Type())
qtechSNIgmpPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpPortIndex.setStatus(_B)
class _QtechSNIgmpPortRouterState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mrnone',1),('mrstatic',2),('mrdynamic',3)))
_QtechSNIgmpPortRouterState_Type.__name__=_F
_QtechSNIgmpPortRouterState_Object=MibTableColumn
qtechSNIgmpPortRouterState=_QtechSNIgmpPortRouterState_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,6,1,3),_QtechSNIgmpPortRouterState_Type())
qtechSNIgmpPortRouterState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpPortRouterState.setStatus(_B)
_QtechSNIgmpPortRouterProfile_Type=Unsigned32
_QtechSNIgmpPortRouterProfile_Object=MibTableColumn
qtechSNIgmpPortRouterProfile=_QtechSNIgmpPortRouterProfile_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,6,1,4),_QtechSNIgmpPortRouterProfile_Type())
qtechSNIgmpPortRouterProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpPortRouterProfile.setStatus(_B)
_QtechSNIgmpGDANumber_Type=Unsigned32
_QtechSNIgmpGDANumber_Object=MibScalar
qtechSNIgmpGDANumber=_QtechSNIgmpGDANumber_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,7),_QtechSNIgmpGDANumber_Type())
qtechSNIgmpGDANumber.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDANumber.setStatus(_B)
_QtechSNIgmpGDATable_Object=MibTable
qtechSNIgmpGDATable=_QtechSNIgmpGDATable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,8))
if mibBuilder.loadTexts:qtechSNIgmpGDATable.setStatus(_B)
_QtechSNIgmpGDAEntry_Object=MibTableRow
qtechSNIgmpGDAEntry=_QtechSNIgmpGDAEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,8,1))
qtechSNIgmpGDAEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:qtechSNIgmpGDAEntry.setStatus(_B)
_QtechSNIgmpGDAVID_Type=VlanId
_QtechSNIgmpGDAVID_Object=MibTableColumn
qtechSNIgmpGDAVID=_QtechSNIgmpGDAVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,8,1,1),_QtechSNIgmpGDAVID_Type())
qtechSNIgmpGDAVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAVID.setStatus(_B)
_QtechSNIgmpGDAAddr_Type=IpAddress
_QtechSNIgmpGDAAddr_Object=MibTableColumn
qtechSNIgmpGDAAddr=_QtechSNIgmpGDAAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,8,1,2),_QtechSNIgmpGDAAddr_Type())
qtechSNIgmpGDAAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAAddr.setStatus(_B)
_QtechSNIgmpGDAPortMemberAction_Type=MemberMap
_QtechSNIgmpGDAPortMemberAction_Object=MibTableColumn
qtechSNIgmpGDAPortMemberAction=_QtechSNIgmpGDAPortMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,8,1,3),_QtechSNIgmpGDAPortMemberAction_Type())
qtechSNIgmpGDAPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpGDAPortMemberAction.setStatus(_B)
_QtechSNIgmpGDATrunkMemberAction_Type=MemberMap
_QtechSNIgmpGDATrunkMemberAction_Object=MibTableColumn
qtechSNIgmpGDATrunkMemberAction=_QtechSNIgmpGDATrunkMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,8,1,4),_QtechSNIgmpGDATrunkMemberAction_Type())
qtechSNIgmpGDATrunkMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpGDATrunkMemberAction.setStatus(_B)
_QtechSNIgmpSvglVID_Type=Integer32
_QtechSNIgmpSvglVID_Object=MibScalar
qtechSNIgmpSvglVID=_QtechSNIgmpSvglVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,9),_QtechSNIgmpSvglVID_Type())
qtechSNIgmpSvglVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpSvglVID.setStatus(_B)
_QtechSNIgmpSvglProfile_Type=Unsigned32
_QtechSNIgmpSvglProfile_Object=MibScalar
qtechSNIgmpSvglProfile=_QtechSNIgmpSvglProfile_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,10),_QtechSNIgmpSvglProfile_Type())
qtechSNIgmpSvglProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpSvglProfile.setStatus(_B)
_QtechSNIgmpMrLearnTable_Object=MibTable
qtechSNIgmpMrLearnTable=_QtechSNIgmpMrLearnTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,11))
if mibBuilder.loadTexts:qtechSNIgmpMrLearnTable.setStatus(_B)
_QtechSNIgmpMrLearnEntry_Object=MibTableRow
qtechSNIgmpMrLearnEntry=_QtechSNIgmpMrLearnEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,11,1))
qtechSNIgmpMrLearnEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:qtechSNIgmpMrLearnEntry.setStatus(_B)
_QtechSNIgmpMrLearnVID_Type=VlanId
_QtechSNIgmpMrLearnVID_Object=MibTableColumn
qtechSNIgmpMrLearnVID=_QtechSNIgmpMrLearnVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,11,1,1),_QtechSNIgmpMrLearnVID_Type())
qtechSNIgmpMrLearnVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpMrLearnVID.setStatus(_B)
class _QtechSNIgmpMrLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_QtechSNIgmpMrLearnStatus_Type.__name__=_F
_QtechSNIgmpMrLearnStatus_Object=MibTableColumn
qtechSNIgmpMrLearnStatus=_QtechSNIgmpMrLearnStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,11,1,2),_QtechSNIgmpMrLearnStatus_Type())
qtechSNIgmpMrLearnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpMrLearnStatus.setStatus(_B)
_QtechSNIgmpPortFilteringTable_Object=MibTable
qtechSNIgmpPortFilteringTable=_QtechSNIgmpPortFilteringTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,12))
if mibBuilder.loadTexts:qtechSNIgmpPortFilteringTable.setStatus(_B)
_QtechSNIgmpPortFilteringEntry_Object=MibTableRow
qtechSNIgmpPortFilteringEntry=_QtechSNIgmpPortFilteringEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,12,1))
qtechSNIgmpPortFilteringEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:qtechSNIgmpPortFilteringEntry.setStatus(_B)
_QtechSNPortIndex_Type=IfIndex
_QtechSNPortIndex_Object=MibTableColumn
qtechSNPortIndex=_QtechSNPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,12,1,1),_QtechSNPortIndex_Type())
qtechSNPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNPortIndex.setStatus(_B)
_QtechSNIgmpFilteringProfile_Type=Unsigned32
_QtechSNIgmpFilteringProfile_Object=MibTableColumn
qtechSNIgmpFilteringProfile=_QtechSNIgmpFilteringProfile_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,12,1,2),_QtechSNIgmpFilteringProfile_Type())
qtechSNIgmpFilteringProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpFilteringProfile.setStatus(_B)
_QtechSNIgmpFilteringMaxGroups_Type=Unsigned32
_QtechSNIgmpFilteringMaxGroups_Object=MibTableColumn
qtechSNIgmpFilteringMaxGroups=_QtechSNIgmpFilteringMaxGroups_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,12,1,3),_QtechSNIgmpFilteringMaxGroups_Type())
qtechSNIgmpFilteringMaxGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpFilteringMaxGroups.setStatus(_B)
_QtechSNIgmpGDAConfigTable_Object=MibTable
qtechSNIgmpGDAConfigTable=_QtechSNIgmpGDAConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13))
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigTable.setStatus(_B)
_QtechSNIgmpGDAConfigEntry_Object=MibTableRow
qtechSNIgmpGDAConfigEntry=_QtechSNIgmpGDAConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13,1))
qtechSNIgmpGDAConfigEntry.setIndexNames((0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigEntry.setStatus(_B)
_QtechSNIgmpGDAConfigVID_Type=VlanId
_QtechSNIgmpGDAConfigVID_Object=MibTableColumn
qtechSNIgmpGDAConfigVID=_QtechSNIgmpGDAConfigVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13,1,1),_QtechSNIgmpGDAConfigVID_Type())
qtechSNIgmpGDAConfigVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigVID.setStatus(_B)
_QtechSNIgmpGDAConfigAddr_Type=IpAddress
_QtechSNIgmpGDAConfigAddr_Object=MibTableColumn
qtechSNIgmpGDAConfigAddr=_QtechSNIgmpGDAConfigAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13,1,2),_QtechSNIgmpGDAConfigAddr_Type())
qtechSNIgmpGDAConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigAddr.setStatus(_B)
_QtechSNIgmpGDAConfigIfIndex_Type=IfIndex
_QtechSNIgmpGDAConfigIfIndex_Object=MibTableColumn
qtechSNIgmpGDAConfigIfIndex=_QtechSNIgmpGDAConfigIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13,1,3),_QtechSNIgmpGDAConfigIfIndex_Type())
qtechSNIgmpGDAConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigIfIndex.setStatus(_B)
class _QtechSNIgmpGDAConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('null',1),('static',2),('dynamic',3),('mrouter',4)))
_QtechSNIgmpGDAConfigType_Type.__name__=_F
_QtechSNIgmpGDAConfigType_Object=MibTableColumn
qtechSNIgmpGDAConfigType=_QtechSNIgmpGDAConfigType_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13,1,4),_QtechSNIgmpGDAConfigType_Type())
qtechSNIgmpGDAConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigType.setStatus(_B)
class _QtechSNIgmpGDAConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_QtechSNIgmpGDAConfigStatus_Type.__name__=_F
_QtechSNIgmpGDAConfigStatus_Object=MibTableColumn
qtechSNIgmpGDAConfigStatus=_QtechSNIgmpGDAConfigStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,13,1,5),_QtechSNIgmpGDAConfigStatus_Type())
qtechSNIgmpGDAConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechSNIgmpGDAConfigStatus.setStatus(_B)
_QtechSNIgmpQueryResponeTime_Type=Unsigned32
_QtechSNIgmpQueryResponeTime_Object=MibScalar
qtechSNIgmpQueryResponeTime=_QtechSNIgmpQueryResponeTime_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,14),_QtechSNIgmpQueryResponeTime_Type())
qtechSNIgmpQueryResponeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSNIgmpQueryResponeTime.setStatus(_B)
class _QtechIgmpSnoopingWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('svgl',2),('ivgl',3),(_f,4)))
_QtechIgmpSnoopingWorkingMode_Type.__name__=_F
_QtechIgmpSnoopingWorkingMode_Object=MibScalar
qtechIgmpSnoopingWorkingMode=_QtechIgmpSnoopingWorkingMode_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,15),_QtechIgmpSnoopingWorkingMode_Type())
qtechIgmpSnoopingWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingWorkingMode.setStatus(_C)
_QtechIgmpSnoopingGDANumber_Type=Unsigned32
_QtechIgmpSnoopingGDANumber_Object=MibScalar
qtechIgmpSnoopingGDANumber=_QtechIgmpSnoopingGDANumber_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,16),_QtechIgmpSnoopingGDANumber_Type())
qtechIgmpSnoopingGDANumber.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDANumber.setStatus(_C)
_QtechIgmpSnoopingGDATable_Object=MibTable
qtechIgmpSnoopingGDATable=_QtechIgmpSnoopingGDATable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,17))
if mibBuilder.loadTexts:qtechIgmpSnoopingGDATable.setStatus(_C)
_QtechIgmpSnoopingGDAEntry_Object=MibTableRow
qtechIgmpSnoopingGDAEntry=_QtechIgmpSnoopingGDAEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,17,1))
qtechIgmpSnoopingGDAEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAEntry.setStatus(_C)
_QtechIgmpSnoopingGDAVID_Type=VlanId
_QtechIgmpSnoopingGDAVID_Object=MibTableColumn
qtechIgmpSnoopingGDAVID=_QtechIgmpSnoopingGDAVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,17,1,1),_QtechIgmpSnoopingGDAVID_Type())
qtechIgmpSnoopingGDAVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAVID.setStatus(_C)
_QtechIgmpSnoopingGDAAddr_Type=IpAddress
_QtechIgmpSnoopingGDAAddr_Object=MibTableColumn
qtechIgmpSnoopingGDAAddr=_QtechIgmpSnoopingGDAAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,17,1,2),_QtechIgmpSnoopingGDAAddr_Type())
qtechIgmpSnoopingGDAAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAAddr.setStatus(_C)
_QtechIgmpSnoopingGDAPortMemberAction_Type=MemberMap
_QtechIgmpSnoopingGDAPortMemberAction_Object=MibTableColumn
qtechIgmpSnoopingGDAPortMemberAction=_QtechIgmpSnoopingGDAPortMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,17,1,3),_QtechIgmpSnoopingGDAPortMemberAction_Type())
qtechIgmpSnoopingGDAPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAPortMemberAction.setStatus(_C)
_QtechIgmpSnoopingVlanStatusTable_Object=MibTable
qtechIgmpSnoopingVlanStatusTable=_QtechIgmpSnoopingVlanStatusTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,18))
if mibBuilder.loadTexts:qtechIgmpSnoopingVlanStatusTable.setStatus(_C)
_QtechIgmpSnoopingVlanStatusEntry_Object=MibTableRow
qtechIgmpSnoopingVlanStatusEntry=_QtechIgmpSnoopingVlanStatusEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,18,1))
qtechIgmpSnoopingVlanStatusEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:qtechIgmpSnoopingVlanStatusEntry.setStatus(_C)
_QtechIgmpSnoopingVlanStatusVID_Type=VlanId
_QtechIgmpSnoopingVlanStatusVID_Object=MibTableColumn
qtechIgmpSnoopingVlanStatusVID=_QtechIgmpSnoopingVlanStatusVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,18,1,1),_QtechIgmpSnoopingVlanStatusVID_Type())
qtechIgmpSnoopingVlanStatusVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingVlanStatusVID.setStatus(_C)
_QtechIgmpSnoopingVlanStatusStatus_Type=EnabledStatus
_QtechIgmpSnoopingVlanStatusStatus_Object=MibTableColumn
qtechIgmpSnoopingVlanStatusStatus=_QtechIgmpSnoopingVlanStatusStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,18,1,2),_QtechIgmpSnoopingVlanStatusStatus_Type())
qtechIgmpSnoopingVlanStatusStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingVlanStatusStatus.setStatus(_C)
_QtechIgmpSnoopingSvglVID_Type=Integer32
_QtechIgmpSnoopingSvglVID_Object=MibScalar
qtechIgmpSnoopingSvglVID=_QtechIgmpSnoopingSvglVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,19),_QtechIgmpSnoopingSvglVID_Type())
qtechIgmpSnoopingSvglVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingSvglVID.setStatus(_C)
_QtechIgmpSnoopingSvglProfile_Type=Unsigned32
_QtechIgmpSnoopingSvglProfile_Object=MibScalar
qtechIgmpSnoopingSvglProfile=_QtechIgmpSnoopingSvglProfile_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,20),_QtechIgmpSnoopingSvglProfile_Type())
qtechIgmpSnoopingSvglProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingSvglProfile.setStatus(_C)
_QtechIgmpSnoopingMrLearnTable_Object=MibTable
qtechIgmpSnoopingMrLearnTable=_QtechIgmpSnoopingMrLearnTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,21))
if mibBuilder.loadTexts:qtechIgmpSnoopingMrLearnTable.setStatus(_C)
_QtechIgmpSnoopingMrLearnEntry_Object=MibTableRow
qtechIgmpSnoopingMrLearnEntry=_QtechIgmpSnoopingMrLearnEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,21,1))
qtechIgmpSnoopingMrLearnEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:qtechIgmpSnoopingMrLearnEntry.setStatus(_C)
_QtechIgmpSnoopingMrLearnVID_Type=VlanId
_QtechIgmpSnoopingMrLearnVID_Object=MibTableColumn
qtechIgmpSnoopingMrLearnVID=_QtechIgmpSnoopingMrLearnVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,21,1,1),_QtechIgmpSnoopingMrLearnVID_Type())
qtechIgmpSnoopingMrLearnVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingMrLearnVID.setStatus(_C)
class _QtechIgmpSnoopingMrLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_QtechIgmpSnoopingMrLearnStatus_Type.__name__=_F
_QtechIgmpSnoopingMrLearnStatus_Object=MibTableColumn
qtechIgmpSnoopingMrLearnStatus=_QtechIgmpSnoopingMrLearnStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,21,1,2),_QtechIgmpSnoopingMrLearnStatus_Type())
qtechIgmpSnoopingMrLearnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingMrLearnStatus.setStatus(_C)
_QtechIgmpSnoopingPortFilteringTable_Object=MibTable
qtechIgmpSnoopingPortFilteringTable=_QtechIgmpSnoopingPortFilteringTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,22))
if mibBuilder.loadTexts:qtechIgmpSnoopingPortFilteringTable.setStatus(_C)
_QtechIgmpSnoopingPortFilteringEntry_Object=MibTableRow
qtechIgmpSnoopingPortFilteringEntry=_QtechIgmpSnoopingPortFilteringEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,22,1))
qtechIgmpSnoopingPortFilteringEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:qtechIgmpSnoopingPortFilteringEntry.setStatus(_C)
_QtechIgmpSnoopingportIndex_Type=IfIndex
_QtechIgmpSnoopingportIndex_Object=MibTableColumn
qtechIgmpSnoopingportIndex=_QtechIgmpSnoopingportIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,22,1,1),_QtechIgmpSnoopingportIndex_Type())
qtechIgmpSnoopingportIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingportIndex.setStatus(_C)
_QtechIgmpSnoopingFilteringProfile_Type=Unsigned32
_QtechIgmpSnoopingFilteringProfile_Object=MibTableColumn
qtechIgmpSnoopingFilteringProfile=_QtechIgmpSnoopingFilteringProfile_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,22,1,2),_QtechIgmpSnoopingFilteringProfile_Type())
qtechIgmpSnoopingFilteringProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingFilteringProfile.setStatus(_C)
_QtechIgmpSnoopingFilteringMaxGroups_Type=Unsigned32
_QtechIgmpSnoopingFilteringMaxGroups_Object=MibTableColumn
qtechIgmpSnoopingFilteringMaxGroups=_QtechIgmpSnoopingFilteringMaxGroups_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,22,1,3),_QtechIgmpSnoopingFilteringMaxGroups_Type())
qtechIgmpSnoopingFilteringMaxGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingFilteringMaxGroups.setStatus(_C)
_QtechIgmpSnoopingGDAConfigTable_Object=MibTable
qtechIgmpSnoopingGDAConfigTable=_QtechIgmpSnoopingGDAConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,23))
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAConfigTable.setStatus(_C)
_QtechIgmpSnoopingGDAConfigEntry_Object=MibTableRow
qtechIgmpSnoopingGDAConfigEntry=_QtechIgmpSnoopingGDAConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,23,1))
qtechIgmpSnoopingGDAConfigEntry.setIndexNames((0,_A,_X),(0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAConfigEntry.setStatus(_C)
_QtechIgmpSnoopingGDAConfigVID_Type=VlanId
_QtechIgmpSnoopingGDAConfigVID_Object=MibTableColumn
qtechIgmpSnoopingGDAConfigVID=_QtechIgmpSnoopingGDAConfigVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,23,1,1),_QtechIgmpSnoopingGDAConfigVID_Type())
qtechIgmpSnoopingGDAConfigVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAConfigVID.setStatus(_C)
_QtechIgmpSnoopingGDAConfigAddr_Type=IpAddress
_QtechIgmpSnoopingGDAConfigAddr_Object=MibTableColumn
qtechIgmpSnoopingGDAConfigAddr=_QtechIgmpSnoopingGDAConfigAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,23,1,2),_QtechIgmpSnoopingGDAConfigAddr_Type())
qtechIgmpSnoopingGDAConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAConfigAddr.setStatus(_C)
_QtechIgmpSnoopingGDAConfigIfIndex_Type=IfIndex
_QtechIgmpSnoopingGDAConfigIfIndex_Object=MibTableColumn
qtechIgmpSnoopingGDAConfigIfIndex=_QtechIgmpSnoopingGDAConfigIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,23,1,3),_QtechIgmpSnoopingGDAConfigIfIndex_Type())
qtechIgmpSnoopingGDAConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAConfigIfIndex.setStatus(_C)
_QtechIgmpSnoopingQueryResponeTime_Type=Unsigned32
_QtechIgmpSnoopingQueryResponeTime_Object=MibScalar
qtechIgmpSnoopingQueryResponeTime=_QtechIgmpSnoopingQueryResponeTime_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,24),_QtechIgmpSnoopingQueryResponeTime_Type())
qtechIgmpSnoopingQueryResponeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingQueryResponeTime.setStatus(_C)
_QtechIgmpSnoopingReportSuppress_Type=TruthValue
_QtechIgmpSnoopingReportSuppress_Object=MibScalar
qtechIgmpSnoopingReportSuppress=_QtechIgmpSnoopingReportSuppress_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,25),_QtechIgmpSnoopingReportSuppress_Type())
qtechIgmpSnoopingReportSuppress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingReportSuppress.setStatus(_C)
_QtechIgmpSnoopingFastleave_Type=TruthValue
_QtechIgmpSnoopingFastleave_Object=MibScalar
qtechIgmpSnoopingFastleave=_QtechIgmpSnoopingFastleave_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,26),_QtechIgmpSnoopingFastleave_Type())
qtechIgmpSnoopingFastleave.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingFastleave.setStatus(_C)
_QtechIgmpSnoopingGDANewTable_Object=MibTable
qtechIgmpSnoopingGDANewTable=_QtechIgmpSnoopingGDANewTable_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27))
if mibBuilder.loadTexts:qtechIgmpSnoopingGDANewTable.setStatus(_C)
_QtechIgmpSnoopingGDANewEntry_Object=MibTableRow
qtechIgmpSnoopingGDANewEntry=_QtechIgmpSnoopingGDANewEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1))
qtechIgmpSnoopingGDANewEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c),(0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:qtechIgmpSnoopingGDANewEntry.setStatus(_C)
_QtechIgmpSnoopingGDANewInVID_Type=VlanId
_QtechIgmpSnoopingGDANewInVID_Object=MibTableColumn
qtechIgmpSnoopingGDANewInVID=_QtechIgmpSnoopingGDANewInVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1,1),_QtechIgmpSnoopingGDANewInVID_Type())
qtechIgmpSnoopingGDANewInVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDANewInVID.setStatus(_C)
_QtechIgmpSnoopingGDANewOutVID_Type=VlanId
_QtechIgmpSnoopingGDANewOutVID_Object=MibTableColumn
qtechIgmpSnoopingGDANewOutVID=_QtechIgmpSnoopingGDANewOutVID_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1,2),_QtechIgmpSnoopingGDANewOutVID_Type())
qtechIgmpSnoopingGDANewOutVID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDANewOutVID.setStatus(_C)
_QtechIgsmpSnoopingGDASrc_Type=IpAddress
_QtechIgsmpSnoopingGDASrc_Object=MibTableColumn
qtechIgsmpSnoopingGDASrc=_QtechIgsmpSnoopingGDASrc_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1,3),_QtechIgsmpSnoopingGDASrc_Type())
qtechIgsmpSnoopingGDASrc.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgsmpSnoopingGDASrc.setStatus(_C)
_QtechIgmpSnoopingGDAGrp_Type=IpAddress
_QtechIgmpSnoopingGDAGrp_Object=MibTableColumn
qtechIgmpSnoopingGDAGrp=_QtechIgmpSnoopingGDAGrp_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1,4),_QtechIgmpSnoopingGDAGrp_Type())
qtechIgmpSnoopingGDAGrp.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAGrp.setStatus(_C)
_QtechIgmpSnoopingGDAIfx_Type=IfIndex
_QtechIgmpSnoopingGDAIfx_Object=MibTableColumn
qtechIgmpSnoopingGDAIfx=_QtechIgmpSnoopingGDAIfx_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1,5),_QtechIgmpSnoopingGDAIfx_Type())
qtechIgmpSnoopingGDAIfx.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAIfx.setStatus(_C)
_QtechIgmpSnoopingGDAIfxAction_Type=Integer32
_QtechIgmpSnoopingGDAIfxAction_Object=MibTableColumn
qtechIgmpSnoopingGDAIfxAction=_QtechIgmpSnoopingGDAIfxAction_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,27,1,6),_QtechIgmpSnoopingGDAIfxAction_Type())
qtechIgmpSnoopingGDAIfxAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingGDAIfxAction.setStatus(_C)
class _QtechIgmpSnoopingMulticastWlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('enable',1)))
_QtechIgmpSnoopingMulticastWlan_Type.__name__=_F
_QtechIgmpSnoopingMulticastWlan_Object=MibScalar
qtechIgmpSnoopingMulticastWlan=_QtechIgmpSnoopingMulticastWlan_Object((1,3,6,1,4,1,27514,1,1,10,2,8,1,28),_QtechIgmpSnoopingMulticastWlan_Type())
qtechIgmpSnoopingMulticastWlan.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpSnoopingMulticastWlan.setStatus(_C)
_QtechIgmpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
qtechIgmpSnoopingMIBConformance=_QtechIgmpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,8,2))
_QtechIgmpSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
qtechIgmpSnoopingMIBCompliances=_QtechIgmpSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,8,2,1))
_QtechIgmpSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
qtechIgmpSnoopingMIBGroups=_QtechIgmpSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,8,2,2))
qtechIgmpSnoopingMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,8,2,2,1))
qtechIgmpSnoopingMIBGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_I),(_A,_J),(_A,_n),(_A,_o),(_A,_K),(_A,_L),(_A,_p),(_A,_q),(_A,_r),(_A,_M),(_A,_N),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_O),(_A,_w),(_A,_P),(_A,_x),(_A,_y),(_A,_Q),(_A,_R),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:qtechIgmpSnoopingMIBGroup.setStatus(_B)
qtechIgmpSnoopingMIBGroup2=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,8,2,2,2))
qtechIgmpSnoopingMIBGroup2.setObjects(*((_A,_A3),(_A,_A4),(_A,_S),(_A,_T),(_A,_A5),(_A,_U),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_V),(_A,_A9),(_A,_W),(_A,_AA),(_A,_AB),(_A,_X),(_A,_Y),(_A,_Z),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:qtechIgmpSnoopingMIBGroup2.setStatus(_C)
qtechIgmpSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,8,2,1,1))
qtechIgmpSnoopingMIBCompliance.setObjects((_A,_AH))
if mibBuilder.loadTexts:qtechIgmpSnoopingMIBCompliance.setStatus(_B)
qtechIgmpSnoopingMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,8,2,1,2))
qtechIgmpSnoopingMIBCompliance2.setObjects((_A,_AI))
if mibBuilder.loadTexts:qtechIgmpSnoopingMIBCompliance2.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'qtechIgmpSnoopingMIB':qtechIgmpSnoopingMIB,'qtechIgmpSnoopingMIBObjects':qtechIgmpSnoopingMIBObjects,_j:qtechSNIgmpWorkingMode,_k:qtechSNIgmpSourcePortCheck,_l:qtechSNIgmpSourceIpCheck,_m:qtechSNIgmpSourceIpCheckDefIp,'qtechSNIgmpSrcIpCheckTable':qtechSNIgmpSrcIpCheckTable,'qtechSNIgmpSrcIpCheckEntry':qtechSNIgmpSrcIpCheckEntry,_I:qtechSNIgmpSrcIpCheckVID,_J:qtechSNIgmpSrcIpCheckMultiIpAddr,_n:qtechSNIgmpSrcIpCheckSrcIpAddr,_o:qtechSNIgmpSrcIpCheckEntryStatus,'qtechSNIgmpPortTable':qtechSNIgmpPortTable,'qtechSNIgmpPortEntry':qtechSNIgmpPortEntry,_K:qtechSNIgmpPortRouterVID,_L:qtechSNIgmpPortIndex,_p:qtechSNIgmpPortRouterState,_q:qtechSNIgmpPortRouterProfile,_r:qtechSNIgmpGDANumber,'qtechSNIgmpGDATable':qtechSNIgmpGDATable,'qtechSNIgmpGDAEntry':qtechSNIgmpGDAEntry,_M:qtechSNIgmpGDAVID,_N:qtechSNIgmpGDAAddr,_s:qtechSNIgmpGDAPortMemberAction,_t:qtechSNIgmpGDATrunkMemberAction,_u:qtechSNIgmpSvglVID,_v:qtechSNIgmpSvglProfile,'qtechSNIgmpMrLearnTable':qtechSNIgmpMrLearnTable,'qtechSNIgmpMrLearnEntry':qtechSNIgmpMrLearnEntry,_O:qtechSNIgmpMrLearnVID,_w:qtechSNIgmpMrLearnStatus,'qtechSNIgmpPortFilteringTable':qtechSNIgmpPortFilteringTable,'qtechSNIgmpPortFilteringEntry':qtechSNIgmpPortFilteringEntry,_P:qtechSNPortIndex,_x:qtechSNIgmpFilteringProfile,_y:qtechSNIgmpFilteringMaxGroups,'qtechSNIgmpGDAConfigTable':qtechSNIgmpGDAConfigTable,'qtechSNIgmpGDAConfigEntry':qtechSNIgmpGDAConfigEntry,_Q:qtechSNIgmpGDAConfigVID,_R:qtechSNIgmpGDAConfigAddr,_z:qtechSNIgmpGDAConfigIfIndex,_A0:qtechSNIgmpGDAConfigType,_A1:qtechSNIgmpGDAConfigStatus,_A2:qtechSNIgmpQueryResponeTime,_A3:qtechIgmpSnoopingWorkingMode,_A4:qtechIgmpSnoopingGDANumber,'qtechIgmpSnoopingGDATable':qtechIgmpSnoopingGDATable,'qtechIgmpSnoopingGDAEntry':qtechIgmpSnoopingGDAEntry,_S:qtechIgmpSnoopingGDAVID,_T:qtechIgmpSnoopingGDAAddr,_A5:qtechIgmpSnoopingGDAPortMemberAction,'qtechIgmpSnoopingVlanStatusTable':qtechIgmpSnoopingVlanStatusTable,'qtechIgmpSnoopingVlanStatusEntry':qtechIgmpSnoopingVlanStatusEntry,_U:qtechIgmpSnoopingVlanStatusVID,_A6:qtechIgmpSnoopingVlanStatusStatus,_A7:qtechIgmpSnoopingSvglVID,_A8:qtechIgmpSnoopingSvglProfile,'qtechIgmpSnoopingMrLearnTable':qtechIgmpSnoopingMrLearnTable,'qtechIgmpSnoopingMrLearnEntry':qtechIgmpSnoopingMrLearnEntry,_V:qtechIgmpSnoopingMrLearnVID,_A9:qtechIgmpSnoopingMrLearnStatus,'qtechIgmpSnoopingPortFilteringTable':qtechIgmpSnoopingPortFilteringTable,'qtechIgmpSnoopingPortFilteringEntry':qtechIgmpSnoopingPortFilteringEntry,_W:qtechIgmpSnoopingportIndex,_AA:qtechIgmpSnoopingFilteringProfile,_AB:qtechIgmpSnoopingFilteringMaxGroups,'qtechIgmpSnoopingGDAConfigTable':qtechIgmpSnoopingGDAConfigTable,'qtechIgmpSnoopingGDAConfigEntry':qtechIgmpSnoopingGDAConfigEntry,_X:qtechIgmpSnoopingGDAConfigVID,_Y:qtechIgmpSnoopingGDAConfigAddr,_Z:qtechIgmpSnoopingGDAConfigIfIndex,_AC:qtechIgmpSnoopingQueryResponeTime,_AD:qtechIgmpSnoopingReportSuppress,_AE:qtechIgmpSnoopingFastleave,'qtechIgmpSnoopingGDANewTable':qtechIgmpSnoopingGDANewTable,'qtechIgmpSnoopingGDANewEntry':qtechIgmpSnoopingGDANewEntry,_a:qtechIgmpSnoopingGDANewInVID,_b:qtechIgmpSnoopingGDANewOutVID,_c:qtechIgsmpSnoopingGDASrc,_d:qtechIgmpSnoopingGDAGrp,_e:qtechIgmpSnoopingGDAIfx,_AF:qtechIgmpSnoopingGDAIfxAction,_AG:qtechIgmpSnoopingMulticastWlan,'qtechIgmpSnoopingMIBConformance':qtechIgmpSnoopingMIBConformance,'qtechIgmpSnoopingMIBCompliances':qtechIgmpSnoopingMIBCompliances,'qtechIgmpSnoopingMIBCompliance':qtechIgmpSnoopingMIBCompliance,'qtechIgmpSnoopingMIBCompliance2':qtechIgmpSnoopingMIBCompliance2,'qtechIgmpSnoopingMIBGroups':qtechIgmpSnoopingMIBGroups,_AH:qtechIgmpSnoopingMIBGroup,_AI:qtechIgmpSnoopingMIBGroup2})