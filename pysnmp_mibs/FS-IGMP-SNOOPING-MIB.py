_AI='fsIgmpSnoopingMIBGroup2'
_AH='fsIgmpSnoopingMIBGroup'
_AG='fsIgmpSnoopingMulticastWlan'
_AF='fsIgmpSnoopingGDAIfxAction'
_AE='fsIgmpSnoopingFastleave'
_AD='fsIgmpSnoopingReportSuppress'
_AC='fsIgmpSnoopingQueryResponeTime'
_AB='fsIgmpSnoopingFilteringMaxGroups'
_AA='fsIgmpSnoopingFilteringProfile'
_A9='fsIgmpSnoopingMrLearnStatus'
_A8='fsIgmpSnoopingSvglProfile'
_A7='fsIgmpSnoopingSvglVID'
_A6='fsIgmpSnoopingVlanStatusStatus'
_A5='fsIgmpSnoopingGDAPortMemberAction'
_A4='fsIgmpSnoopingGDANumber'
_A3='fsIgmpSnoopingWorkingMode'
_A2='fsSNIgmpQueryResponeTime'
_A1='fsSNIgmpGDAConfigStatus'
_A0='fsSNIgmpGDAConfigType'
_z='fsSNIgmpGDAConfigIfIndex'
_y='fsSNIgmpFilteringMaxGroups'
_x='fsSNIgmpFilteringProfile'
_w='fsSNIgmpMrLearnStatus'
_v='fsSNIgmpSvglProfile'
_u='fsSNIgmpSvglVID'
_t='fsSNIgmpGDATrunkMemberAction'
_s='fsSNIgmpGDAPortMemberAction'
_r='fsSNIgmpGDANumber'
_q='fsSNIgmpPortRouterProfile'
_p='fsSNIgmpPortRouterState'
_o='fsSNIgmpSrcIpCheckEntryStatus'
_n='fsSNIgmpSrcIpCheckSrcIpAddr'
_m='fsSNIgmpSourceIpCheckDefIp'
_l='fsSNIgmpSourceIpCheck'
_k='fsSNIgmpSourcePortCheck'
_j='fsSNIgmpWorkingMode'
_i='pim-dvmrp'
_h='disable'
_g='read-create'
_f='ivgl-svgl'
_e='fsIgmpSnoopingGDAIfx'
_d='fsIgmpSnoopingGDAGrp'
_c='fsIgsmpSnoopingGDASrc'
_b='fsIgmpSnoopingGDANewOutVID'
_a='fsIgmpSnoopingGDANewInVID'
_Z='fsIgmpSnoopingGDAConfigIfIndex'
_Y='fsIgmpSnoopingGDAConfigAddr'
_X='fsIgmpSnoopingGDAConfigVID'
_W='fsIgmpSnoopingportIndex'
_V='fsIgmpSnoopingMrLearnVID'
_U='fsIgmpSnoopingVlanStatusVID'
_T='fsIgmpSnoopingGDAAddr'
_S='fsIgmpSnoopingGDAVID'
_R='fsSNIgmpGDAConfigAddr'
_Q='fsSNIgmpGDAConfigVID'
_P='fsSNPortIndex'
_O='fsSNIgmpMrLearnVID'
_N='fsSNIgmpGDAAddr'
_M='fsSNIgmpGDAVID'
_L='fsSNIgmpPortIndex'
_K='fsSNIgmpPortRouterVID'
_J='fsSNIgmpSrcIpCheckMultiIpAddr'
_I='fsSNIgmpSrcIpCheckVID'
_H='disabled'
_G='EnabledStatus'
_F='Integer32'
_E='read-only'
_D='read-write'
_C='current'
_B='deprecated'
_A='FS-IGMP-SNOOPING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,MemberMap=mibBuilder.importSymbols('FS-TC','IfIndex','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fsIgmpSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,8))
if mibBuilder.loadTexts:fsIgmpSnoopingMIB.setRevisions(('2009-10-22 00:00','2002-03-20 00:00'))
_FsIgmpSnoopingMIBObjects_ObjectIdentity=ObjectIdentity
fsIgmpSnoopingMIBObjects=_FsIgmpSnoopingMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,8,1))
class _FsSNIgmpWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('svgl',2),('ivgl',3),(_f,4)))
_FsSNIgmpWorkingMode_Type.__name__=_F
_FsSNIgmpWorkingMode_Object=MibScalar
fsSNIgmpWorkingMode=_FsSNIgmpWorkingMode_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,1),_FsSNIgmpWorkingMode_Type())
fsSNIgmpWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpWorkingMode.setStatus(_B)
class _FsSNIgmpSourcePortCheck_Type(EnabledStatus):defaultValue=2
_FsSNIgmpSourcePortCheck_Type.__name__=_G
_FsSNIgmpSourcePortCheck_Object=MibScalar
fsSNIgmpSourcePortCheck=_FsSNIgmpSourcePortCheck_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,2),_FsSNIgmpSourcePortCheck_Type())
fsSNIgmpSourcePortCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpSourcePortCheck.setStatus(_B)
class _FsSNIgmpSourceIpCheck_Type(EnabledStatus):defaultValue=2
_FsSNIgmpSourceIpCheck_Type.__name__=_G
_FsSNIgmpSourceIpCheck_Object=MibScalar
fsSNIgmpSourceIpCheck=_FsSNIgmpSourceIpCheck_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,3),_FsSNIgmpSourceIpCheck_Type())
fsSNIgmpSourceIpCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpSourceIpCheck.setStatus(_B)
_FsSNIgmpSourceIpCheckDefIp_Type=IpAddress
_FsSNIgmpSourceIpCheckDefIp_Object=MibScalar
fsSNIgmpSourceIpCheckDefIp=_FsSNIgmpSourceIpCheckDefIp_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,4),_FsSNIgmpSourceIpCheckDefIp_Type())
fsSNIgmpSourceIpCheckDefIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpSourceIpCheckDefIp.setStatus(_B)
_FsSNIgmpSrcIpCheckTable_Object=MibTable
fsSNIgmpSrcIpCheckTable=_FsSNIgmpSrcIpCheckTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,5))
if mibBuilder.loadTexts:fsSNIgmpSrcIpCheckTable.setStatus(_B)
_FsSNIgmpSrcIpCheckEntry_Object=MibTableRow
fsSNIgmpSrcIpCheckEntry=_FsSNIgmpSrcIpCheckEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,5,1))
fsSNIgmpSrcIpCheckEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:fsSNIgmpSrcIpCheckEntry.setStatus(_B)
_FsSNIgmpSrcIpCheckVID_Type=VlanId
_FsSNIgmpSrcIpCheckVID_Object=MibTableColumn
fsSNIgmpSrcIpCheckVID=_FsSNIgmpSrcIpCheckVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,5,1,1),_FsSNIgmpSrcIpCheckVID_Type())
fsSNIgmpSrcIpCheckVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpSrcIpCheckVID.setStatus(_B)
_FsSNIgmpSrcIpCheckMultiIpAddr_Type=IpAddress
_FsSNIgmpSrcIpCheckMultiIpAddr_Object=MibTableColumn
fsSNIgmpSrcIpCheckMultiIpAddr=_FsSNIgmpSrcIpCheckMultiIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,5,1,2),_FsSNIgmpSrcIpCheckMultiIpAddr_Type())
fsSNIgmpSrcIpCheckMultiIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpSrcIpCheckMultiIpAddr.setStatus(_B)
_FsSNIgmpSrcIpCheckSrcIpAddr_Type=IpAddress
_FsSNIgmpSrcIpCheckSrcIpAddr_Object=MibTableColumn
fsSNIgmpSrcIpCheckSrcIpAddr=_FsSNIgmpSrcIpCheckSrcIpAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,5,1,3),_FsSNIgmpSrcIpCheckSrcIpAddr_Type())
fsSNIgmpSrcIpCheckSrcIpAddr.setMaxAccess(_g)
if mibBuilder.loadTexts:fsSNIgmpSrcIpCheckSrcIpAddr.setStatus(_B)
class _FsSNIgmpSrcIpCheckEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('delete',2)))
_FsSNIgmpSrcIpCheckEntryStatus_Type.__name__=_F
_FsSNIgmpSrcIpCheckEntryStatus_Object=MibTableColumn
fsSNIgmpSrcIpCheckEntryStatus=_FsSNIgmpSrcIpCheckEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,5,1,4),_FsSNIgmpSrcIpCheckEntryStatus_Type())
fsSNIgmpSrcIpCheckEntryStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:fsSNIgmpSrcIpCheckEntryStatus.setStatus(_B)
_FsSNIgmpPortTable_Object=MibTable
fsSNIgmpPortTable=_FsSNIgmpPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,6))
if mibBuilder.loadTexts:fsSNIgmpPortTable.setStatus(_B)
_FsSNIgmpPortEntry_Object=MibTableRow
fsSNIgmpPortEntry=_FsSNIgmpPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,6,1))
fsSNIgmpPortEntry.setIndexNames((0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:fsSNIgmpPortEntry.setStatus(_B)
_FsSNIgmpPortRouterVID_Type=VlanId
_FsSNIgmpPortRouterVID_Object=MibTableColumn
fsSNIgmpPortRouterVID=_FsSNIgmpPortRouterVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,6,1,1),_FsSNIgmpPortRouterVID_Type())
fsSNIgmpPortRouterVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpPortRouterVID.setStatus(_B)
_FsSNIgmpPortIndex_Type=IfIndex
_FsSNIgmpPortIndex_Object=MibTableColumn
fsSNIgmpPortIndex=_FsSNIgmpPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,6,1,2),_FsSNIgmpPortIndex_Type())
fsSNIgmpPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpPortIndex.setStatus(_B)
class _FsSNIgmpPortRouterState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mrnone',1),('mrstatic',2),('mrdynamic',3)))
_FsSNIgmpPortRouterState_Type.__name__=_F
_FsSNIgmpPortRouterState_Object=MibTableColumn
fsSNIgmpPortRouterState=_FsSNIgmpPortRouterState_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,6,1,3),_FsSNIgmpPortRouterState_Type())
fsSNIgmpPortRouterState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpPortRouterState.setStatus(_B)
_FsSNIgmpPortRouterProfile_Type=Unsigned32
_FsSNIgmpPortRouterProfile_Object=MibTableColumn
fsSNIgmpPortRouterProfile=_FsSNIgmpPortRouterProfile_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,6,1,4),_FsSNIgmpPortRouterProfile_Type())
fsSNIgmpPortRouterProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpPortRouterProfile.setStatus(_B)
_FsSNIgmpGDANumber_Type=Unsigned32
_FsSNIgmpGDANumber_Object=MibScalar
fsSNIgmpGDANumber=_FsSNIgmpGDANumber_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,7),_FsSNIgmpGDANumber_Type())
fsSNIgmpGDANumber.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDANumber.setStatus(_B)
_FsSNIgmpGDATable_Object=MibTable
fsSNIgmpGDATable=_FsSNIgmpGDATable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,8))
if mibBuilder.loadTexts:fsSNIgmpGDATable.setStatus(_B)
_FsSNIgmpGDAEntry_Object=MibTableRow
fsSNIgmpGDAEntry=_FsSNIgmpGDAEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,8,1))
fsSNIgmpGDAEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:fsSNIgmpGDAEntry.setStatus(_B)
_FsSNIgmpGDAVID_Type=VlanId
_FsSNIgmpGDAVID_Object=MibTableColumn
fsSNIgmpGDAVID=_FsSNIgmpGDAVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,8,1,1),_FsSNIgmpGDAVID_Type())
fsSNIgmpGDAVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAVID.setStatus(_B)
_FsSNIgmpGDAAddr_Type=IpAddress
_FsSNIgmpGDAAddr_Object=MibTableColumn
fsSNIgmpGDAAddr=_FsSNIgmpGDAAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,8,1,2),_FsSNIgmpGDAAddr_Type())
fsSNIgmpGDAAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAAddr.setStatus(_B)
_FsSNIgmpGDAPortMemberAction_Type=MemberMap
_FsSNIgmpGDAPortMemberAction_Object=MibTableColumn
fsSNIgmpGDAPortMemberAction=_FsSNIgmpGDAPortMemberAction_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,8,1,3),_FsSNIgmpGDAPortMemberAction_Type())
fsSNIgmpGDAPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpGDAPortMemberAction.setStatus(_B)
_FsSNIgmpGDATrunkMemberAction_Type=MemberMap
_FsSNIgmpGDATrunkMemberAction_Object=MibTableColumn
fsSNIgmpGDATrunkMemberAction=_FsSNIgmpGDATrunkMemberAction_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,8,1,4),_FsSNIgmpGDATrunkMemberAction_Type())
fsSNIgmpGDATrunkMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpGDATrunkMemberAction.setStatus(_B)
_FsSNIgmpSvglVID_Type=Integer32
_FsSNIgmpSvglVID_Object=MibScalar
fsSNIgmpSvglVID=_FsSNIgmpSvglVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,9),_FsSNIgmpSvglVID_Type())
fsSNIgmpSvglVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpSvglVID.setStatus(_B)
_FsSNIgmpSvglProfile_Type=Unsigned32
_FsSNIgmpSvglProfile_Object=MibScalar
fsSNIgmpSvglProfile=_FsSNIgmpSvglProfile_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,10),_FsSNIgmpSvglProfile_Type())
fsSNIgmpSvglProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpSvglProfile.setStatus(_B)
_FsSNIgmpMrLearnTable_Object=MibTable
fsSNIgmpMrLearnTable=_FsSNIgmpMrLearnTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,11))
if mibBuilder.loadTexts:fsSNIgmpMrLearnTable.setStatus(_B)
_FsSNIgmpMrLearnEntry_Object=MibTableRow
fsSNIgmpMrLearnEntry=_FsSNIgmpMrLearnEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,11,1))
fsSNIgmpMrLearnEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:fsSNIgmpMrLearnEntry.setStatus(_B)
_FsSNIgmpMrLearnVID_Type=VlanId
_FsSNIgmpMrLearnVID_Object=MibTableColumn
fsSNIgmpMrLearnVID=_FsSNIgmpMrLearnVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,11,1,1),_FsSNIgmpMrLearnVID_Type())
fsSNIgmpMrLearnVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpMrLearnVID.setStatus(_B)
class _FsSNIgmpMrLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_FsSNIgmpMrLearnStatus_Type.__name__=_F
_FsSNIgmpMrLearnStatus_Object=MibTableColumn
fsSNIgmpMrLearnStatus=_FsSNIgmpMrLearnStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,11,1,2),_FsSNIgmpMrLearnStatus_Type())
fsSNIgmpMrLearnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpMrLearnStatus.setStatus(_B)
_FsSNIgmpPortFilteringTable_Object=MibTable
fsSNIgmpPortFilteringTable=_FsSNIgmpPortFilteringTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,12))
if mibBuilder.loadTexts:fsSNIgmpPortFilteringTable.setStatus(_B)
_FsSNIgmpPortFilteringEntry_Object=MibTableRow
fsSNIgmpPortFilteringEntry=_FsSNIgmpPortFilteringEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,12,1))
fsSNIgmpPortFilteringEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:fsSNIgmpPortFilteringEntry.setStatus(_B)
_FsSNPortIndex_Type=IfIndex
_FsSNPortIndex_Object=MibTableColumn
fsSNPortIndex=_FsSNPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,12,1,1),_FsSNPortIndex_Type())
fsSNPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNPortIndex.setStatus(_B)
_FsSNIgmpFilteringProfile_Type=Unsigned32
_FsSNIgmpFilteringProfile_Object=MibTableColumn
fsSNIgmpFilteringProfile=_FsSNIgmpFilteringProfile_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,12,1,2),_FsSNIgmpFilteringProfile_Type())
fsSNIgmpFilteringProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpFilteringProfile.setStatus(_B)
_FsSNIgmpFilteringMaxGroups_Type=Unsigned32
_FsSNIgmpFilteringMaxGroups_Object=MibTableColumn
fsSNIgmpFilteringMaxGroups=_FsSNIgmpFilteringMaxGroups_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,12,1,3),_FsSNIgmpFilteringMaxGroups_Type())
fsSNIgmpFilteringMaxGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpFilteringMaxGroups.setStatus(_B)
_FsSNIgmpGDAConfigTable_Object=MibTable
fsSNIgmpGDAConfigTable=_FsSNIgmpGDAConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13))
if mibBuilder.loadTexts:fsSNIgmpGDAConfigTable.setStatus(_B)
_FsSNIgmpGDAConfigEntry_Object=MibTableRow
fsSNIgmpGDAConfigEntry=_FsSNIgmpGDAConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13,1))
fsSNIgmpGDAConfigEntry.setIndexNames((0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:fsSNIgmpGDAConfigEntry.setStatus(_B)
_FsSNIgmpGDAConfigVID_Type=VlanId
_FsSNIgmpGDAConfigVID_Object=MibTableColumn
fsSNIgmpGDAConfigVID=_FsSNIgmpGDAConfigVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13,1,1),_FsSNIgmpGDAConfigVID_Type())
fsSNIgmpGDAConfigVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAConfigVID.setStatus(_B)
_FsSNIgmpGDAConfigAddr_Type=IpAddress
_FsSNIgmpGDAConfigAddr_Object=MibTableColumn
fsSNIgmpGDAConfigAddr=_FsSNIgmpGDAConfigAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13,1,2),_FsSNIgmpGDAConfigAddr_Type())
fsSNIgmpGDAConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAConfigAddr.setStatus(_B)
_FsSNIgmpGDAConfigIfIndex_Type=IfIndex
_FsSNIgmpGDAConfigIfIndex_Object=MibTableColumn
fsSNIgmpGDAConfigIfIndex=_FsSNIgmpGDAConfigIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13,1,3),_FsSNIgmpGDAConfigIfIndex_Type())
fsSNIgmpGDAConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAConfigIfIndex.setStatus(_B)
class _FsSNIgmpGDAConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('null',1),('static',2),('dynamic',3),('mrouter',4)))
_FsSNIgmpGDAConfigType_Type.__name__=_F
_FsSNIgmpGDAConfigType_Object=MibTableColumn
fsSNIgmpGDAConfigType=_FsSNIgmpGDAConfigType_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13,1,4),_FsSNIgmpGDAConfigType_Type())
fsSNIgmpGDAConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAConfigType.setStatus(_B)
class _FsSNIgmpGDAConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_FsSNIgmpGDAConfigStatus_Type.__name__=_F
_FsSNIgmpGDAConfigStatus_Object=MibTableColumn
fsSNIgmpGDAConfigStatus=_FsSNIgmpGDAConfigStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,13,1,5),_FsSNIgmpGDAConfigStatus_Type())
fsSNIgmpGDAConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsSNIgmpGDAConfigStatus.setStatus(_B)
_FsSNIgmpQueryResponeTime_Type=Unsigned32
_FsSNIgmpQueryResponeTime_Object=MibScalar
fsSNIgmpQueryResponeTime=_FsSNIgmpQueryResponeTime_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,14),_FsSNIgmpQueryResponeTime_Type())
fsSNIgmpQueryResponeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSNIgmpQueryResponeTime.setStatus(_B)
class _FsIgmpSnoopingWorkingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('svgl',2),('ivgl',3),(_f,4)))
_FsIgmpSnoopingWorkingMode_Type.__name__=_F
_FsIgmpSnoopingWorkingMode_Object=MibScalar
fsIgmpSnoopingWorkingMode=_FsIgmpSnoopingWorkingMode_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,15),_FsIgmpSnoopingWorkingMode_Type())
fsIgmpSnoopingWorkingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingWorkingMode.setStatus(_C)
_FsIgmpSnoopingGDANumber_Type=Unsigned32
_FsIgmpSnoopingGDANumber_Object=MibScalar
fsIgmpSnoopingGDANumber=_FsIgmpSnoopingGDANumber_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,16),_FsIgmpSnoopingGDANumber_Type())
fsIgmpSnoopingGDANumber.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDANumber.setStatus(_C)
_FsIgmpSnoopingGDATable_Object=MibTable
fsIgmpSnoopingGDATable=_FsIgmpSnoopingGDATable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,17))
if mibBuilder.loadTexts:fsIgmpSnoopingGDATable.setStatus(_C)
_FsIgmpSnoopingGDAEntry_Object=MibTableRow
fsIgmpSnoopingGDAEntry=_FsIgmpSnoopingGDAEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,17,1))
fsIgmpSnoopingGDAEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:fsIgmpSnoopingGDAEntry.setStatus(_C)
_FsIgmpSnoopingGDAVID_Type=VlanId
_FsIgmpSnoopingGDAVID_Object=MibTableColumn
fsIgmpSnoopingGDAVID=_FsIgmpSnoopingGDAVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,17,1,1),_FsIgmpSnoopingGDAVID_Type())
fsIgmpSnoopingGDAVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAVID.setStatus(_C)
_FsIgmpSnoopingGDAAddr_Type=IpAddress
_FsIgmpSnoopingGDAAddr_Object=MibTableColumn
fsIgmpSnoopingGDAAddr=_FsIgmpSnoopingGDAAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,17,1,2),_FsIgmpSnoopingGDAAddr_Type())
fsIgmpSnoopingGDAAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAAddr.setStatus(_C)
_FsIgmpSnoopingGDAPortMemberAction_Type=MemberMap
_FsIgmpSnoopingGDAPortMemberAction_Object=MibTableColumn
fsIgmpSnoopingGDAPortMemberAction=_FsIgmpSnoopingGDAPortMemberAction_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,17,1,3),_FsIgmpSnoopingGDAPortMemberAction_Type())
fsIgmpSnoopingGDAPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAPortMemberAction.setStatus(_C)
_FsIgmpSnoopingVlanStatusTable_Object=MibTable
fsIgmpSnoopingVlanStatusTable=_FsIgmpSnoopingVlanStatusTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,18))
if mibBuilder.loadTexts:fsIgmpSnoopingVlanStatusTable.setStatus(_C)
_FsIgmpSnoopingVlanStatusEntry_Object=MibTableRow
fsIgmpSnoopingVlanStatusEntry=_FsIgmpSnoopingVlanStatusEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,18,1))
fsIgmpSnoopingVlanStatusEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:fsIgmpSnoopingVlanStatusEntry.setStatus(_C)
_FsIgmpSnoopingVlanStatusVID_Type=VlanId
_FsIgmpSnoopingVlanStatusVID_Object=MibTableColumn
fsIgmpSnoopingVlanStatusVID=_FsIgmpSnoopingVlanStatusVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,18,1,1),_FsIgmpSnoopingVlanStatusVID_Type())
fsIgmpSnoopingVlanStatusVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingVlanStatusVID.setStatus(_C)
_FsIgmpSnoopingVlanStatusStatus_Type=EnabledStatus
_FsIgmpSnoopingVlanStatusStatus_Object=MibTableColumn
fsIgmpSnoopingVlanStatusStatus=_FsIgmpSnoopingVlanStatusStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,18,1,2),_FsIgmpSnoopingVlanStatusStatus_Type())
fsIgmpSnoopingVlanStatusStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingVlanStatusStatus.setStatus(_C)
_FsIgmpSnoopingSvglVID_Type=Integer32
_FsIgmpSnoopingSvglVID_Object=MibScalar
fsIgmpSnoopingSvglVID=_FsIgmpSnoopingSvglVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,19),_FsIgmpSnoopingSvglVID_Type())
fsIgmpSnoopingSvglVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingSvglVID.setStatus(_C)
_FsIgmpSnoopingSvglProfile_Type=Unsigned32
_FsIgmpSnoopingSvglProfile_Object=MibScalar
fsIgmpSnoopingSvglProfile=_FsIgmpSnoopingSvglProfile_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,20),_FsIgmpSnoopingSvglProfile_Type())
fsIgmpSnoopingSvglProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingSvglProfile.setStatus(_C)
_FsIgmpSnoopingMrLearnTable_Object=MibTable
fsIgmpSnoopingMrLearnTable=_FsIgmpSnoopingMrLearnTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,21))
if mibBuilder.loadTexts:fsIgmpSnoopingMrLearnTable.setStatus(_C)
_FsIgmpSnoopingMrLearnEntry_Object=MibTableRow
fsIgmpSnoopingMrLearnEntry=_FsIgmpSnoopingMrLearnEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,21,1))
fsIgmpSnoopingMrLearnEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:fsIgmpSnoopingMrLearnEntry.setStatus(_C)
_FsIgmpSnoopingMrLearnVID_Type=VlanId
_FsIgmpSnoopingMrLearnVID_Object=MibTableColumn
fsIgmpSnoopingMrLearnVID=_FsIgmpSnoopingMrLearnVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,21,1,1),_FsIgmpSnoopingMrLearnVID_Type())
fsIgmpSnoopingMrLearnVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingMrLearnVID.setStatus(_C)
class _FsIgmpSnoopingMrLearnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_FsIgmpSnoopingMrLearnStatus_Type.__name__=_F
_FsIgmpSnoopingMrLearnStatus_Object=MibTableColumn
fsIgmpSnoopingMrLearnStatus=_FsIgmpSnoopingMrLearnStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,21,1,2),_FsIgmpSnoopingMrLearnStatus_Type())
fsIgmpSnoopingMrLearnStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingMrLearnStatus.setStatus(_C)
_FsIgmpSnoopingPortFilteringTable_Object=MibTable
fsIgmpSnoopingPortFilteringTable=_FsIgmpSnoopingPortFilteringTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,22))
if mibBuilder.loadTexts:fsIgmpSnoopingPortFilteringTable.setStatus(_C)
_FsIgmpSnoopingPortFilteringEntry_Object=MibTableRow
fsIgmpSnoopingPortFilteringEntry=_FsIgmpSnoopingPortFilteringEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,22,1))
fsIgmpSnoopingPortFilteringEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:fsIgmpSnoopingPortFilteringEntry.setStatus(_C)
_FsIgmpSnoopingportIndex_Type=IfIndex
_FsIgmpSnoopingportIndex_Object=MibTableColumn
fsIgmpSnoopingportIndex=_FsIgmpSnoopingportIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,22,1,1),_FsIgmpSnoopingportIndex_Type())
fsIgmpSnoopingportIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingportIndex.setStatus(_C)
_FsIgmpSnoopingFilteringProfile_Type=Unsigned32
_FsIgmpSnoopingFilteringProfile_Object=MibTableColumn
fsIgmpSnoopingFilteringProfile=_FsIgmpSnoopingFilteringProfile_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,22,1,2),_FsIgmpSnoopingFilteringProfile_Type())
fsIgmpSnoopingFilteringProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingFilteringProfile.setStatus(_C)
_FsIgmpSnoopingFilteringMaxGroups_Type=Unsigned32
_FsIgmpSnoopingFilteringMaxGroups_Object=MibTableColumn
fsIgmpSnoopingFilteringMaxGroups=_FsIgmpSnoopingFilteringMaxGroups_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,22,1,3),_FsIgmpSnoopingFilteringMaxGroups_Type())
fsIgmpSnoopingFilteringMaxGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingFilteringMaxGroups.setStatus(_C)
_FsIgmpSnoopingGDAConfigTable_Object=MibTable
fsIgmpSnoopingGDAConfigTable=_FsIgmpSnoopingGDAConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,23))
if mibBuilder.loadTexts:fsIgmpSnoopingGDAConfigTable.setStatus(_C)
_FsIgmpSnoopingGDAConfigEntry_Object=MibTableRow
fsIgmpSnoopingGDAConfigEntry=_FsIgmpSnoopingGDAConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,23,1))
fsIgmpSnoopingGDAConfigEntry.setIndexNames((0,_A,_X),(0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:fsIgmpSnoopingGDAConfigEntry.setStatus(_C)
_FsIgmpSnoopingGDAConfigVID_Type=VlanId
_FsIgmpSnoopingGDAConfigVID_Object=MibTableColumn
fsIgmpSnoopingGDAConfigVID=_FsIgmpSnoopingGDAConfigVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,23,1,1),_FsIgmpSnoopingGDAConfigVID_Type())
fsIgmpSnoopingGDAConfigVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAConfigVID.setStatus(_C)
_FsIgmpSnoopingGDAConfigAddr_Type=IpAddress
_FsIgmpSnoopingGDAConfigAddr_Object=MibTableColumn
fsIgmpSnoopingGDAConfigAddr=_FsIgmpSnoopingGDAConfigAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,23,1,2),_FsIgmpSnoopingGDAConfigAddr_Type())
fsIgmpSnoopingGDAConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAConfigAddr.setStatus(_C)
_FsIgmpSnoopingGDAConfigIfIndex_Type=IfIndex
_FsIgmpSnoopingGDAConfigIfIndex_Object=MibTableColumn
fsIgmpSnoopingGDAConfigIfIndex=_FsIgmpSnoopingGDAConfigIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,23,1,3),_FsIgmpSnoopingGDAConfigIfIndex_Type())
fsIgmpSnoopingGDAConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAConfigIfIndex.setStatus(_C)
_FsIgmpSnoopingQueryResponeTime_Type=Unsigned32
_FsIgmpSnoopingQueryResponeTime_Object=MibScalar
fsIgmpSnoopingQueryResponeTime=_FsIgmpSnoopingQueryResponeTime_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,24),_FsIgmpSnoopingQueryResponeTime_Type())
fsIgmpSnoopingQueryResponeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingQueryResponeTime.setStatus(_C)
_FsIgmpSnoopingReportSuppress_Type=TruthValue
_FsIgmpSnoopingReportSuppress_Object=MibScalar
fsIgmpSnoopingReportSuppress=_FsIgmpSnoopingReportSuppress_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,25),_FsIgmpSnoopingReportSuppress_Type())
fsIgmpSnoopingReportSuppress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingReportSuppress.setStatus(_C)
_FsIgmpSnoopingFastleave_Type=TruthValue
_FsIgmpSnoopingFastleave_Object=MibScalar
fsIgmpSnoopingFastleave=_FsIgmpSnoopingFastleave_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,26),_FsIgmpSnoopingFastleave_Type())
fsIgmpSnoopingFastleave.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingFastleave.setStatus(_C)
_FsIgmpSnoopingGDANewTable_Object=MibTable
fsIgmpSnoopingGDANewTable=_FsIgmpSnoopingGDANewTable_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27))
if mibBuilder.loadTexts:fsIgmpSnoopingGDANewTable.setStatus(_C)
_FsIgmpSnoopingGDANewEntry_Object=MibTableRow
fsIgmpSnoopingGDANewEntry=_FsIgmpSnoopingGDANewEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1))
fsIgmpSnoopingGDANewEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c),(0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:fsIgmpSnoopingGDANewEntry.setStatus(_C)
_FsIgmpSnoopingGDANewInVID_Type=VlanId
_FsIgmpSnoopingGDANewInVID_Object=MibTableColumn
fsIgmpSnoopingGDANewInVID=_FsIgmpSnoopingGDANewInVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1,1),_FsIgmpSnoopingGDANewInVID_Type())
fsIgmpSnoopingGDANewInVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDANewInVID.setStatus(_C)
_FsIgmpSnoopingGDANewOutVID_Type=VlanId
_FsIgmpSnoopingGDANewOutVID_Object=MibTableColumn
fsIgmpSnoopingGDANewOutVID=_FsIgmpSnoopingGDANewOutVID_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1,2),_FsIgmpSnoopingGDANewOutVID_Type())
fsIgmpSnoopingGDANewOutVID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDANewOutVID.setStatus(_C)
_FsIgsmpSnoopingGDASrc_Type=IpAddress
_FsIgsmpSnoopingGDASrc_Object=MibTableColumn
fsIgsmpSnoopingGDASrc=_FsIgsmpSnoopingGDASrc_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1,3),_FsIgsmpSnoopingGDASrc_Type())
fsIgsmpSnoopingGDASrc.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgsmpSnoopingGDASrc.setStatus(_C)
_FsIgmpSnoopingGDAGrp_Type=IpAddress
_FsIgmpSnoopingGDAGrp_Object=MibTableColumn
fsIgmpSnoopingGDAGrp=_FsIgmpSnoopingGDAGrp_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1,4),_FsIgmpSnoopingGDAGrp_Type())
fsIgmpSnoopingGDAGrp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAGrp.setStatus(_C)
_FsIgmpSnoopingGDAIfx_Type=IfIndex
_FsIgmpSnoopingGDAIfx_Object=MibTableColumn
fsIgmpSnoopingGDAIfx=_FsIgmpSnoopingGDAIfx_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1,5),_FsIgmpSnoopingGDAIfx_Type())
fsIgmpSnoopingGDAIfx.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAIfx.setStatus(_C)
_FsIgmpSnoopingGDAIfxAction_Type=Integer32
_FsIgmpSnoopingGDAIfxAction_Object=MibTableColumn
fsIgmpSnoopingGDAIfxAction=_FsIgmpSnoopingGDAIfxAction_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,27,1,6),_FsIgmpSnoopingGDAIfxAction_Type())
fsIgmpSnoopingGDAIfxAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingGDAIfxAction.setStatus(_C)
class _FsIgmpSnoopingMulticastWlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('enable',1)))
_FsIgmpSnoopingMulticastWlan_Type.__name__=_F
_FsIgmpSnoopingMulticastWlan_Object=MibScalar
fsIgmpSnoopingMulticastWlan=_FsIgmpSnoopingMulticastWlan_Object((1,3,6,1,4,1,52642,1,1,10,2,8,1,28),_FsIgmpSnoopingMulticastWlan_Type())
fsIgmpSnoopingMulticastWlan.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpSnoopingMulticastWlan.setStatus(_C)
_FsIgmpSnoopingMIBConformance_ObjectIdentity=ObjectIdentity
fsIgmpSnoopingMIBConformance=_FsIgmpSnoopingMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,8,2))
_FsIgmpSnoopingMIBCompliances_ObjectIdentity=ObjectIdentity
fsIgmpSnoopingMIBCompliances=_FsIgmpSnoopingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,8,2,1))
_FsIgmpSnoopingMIBGroups_ObjectIdentity=ObjectIdentity
fsIgmpSnoopingMIBGroups=_FsIgmpSnoopingMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,8,2,2))
fsIgmpSnoopingMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,8,2,2,1))
fsIgmpSnoopingMIBGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_I),(_A,_J),(_A,_n),(_A,_o),(_A,_K),(_A,_L),(_A,_p),(_A,_q),(_A,_r),(_A,_M),(_A,_N),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_O),(_A,_w),(_A,_P),(_A,_x),(_A,_y),(_A,_Q),(_A,_R),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:fsIgmpSnoopingMIBGroup.setStatus(_B)
fsIgmpSnoopingMIBGroup2=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,8,2,2,2))
fsIgmpSnoopingMIBGroup2.setObjects(*((_A,_A3),(_A,_A4),(_A,_S),(_A,_T),(_A,_A5),(_A,_U),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_V),(_A,_A9),(_A,_W),(_A,_AA),(_A,_AB),(_A,_X),(_A,_Y),(_A,_Z),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:fsIgmpSnoopingMIBGroup2.setStatus(_C)
fsIgmpSnoopingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,8,2,1,1))
fsIgmpSnoopingMIBCompliance.setObjects((_A,_AH))
if mibBuilder.loadTexts:fsIgmpSnoopingMIBCompliance.setStatus(_B)
fsIgmpSnoopingMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,8,2,1,2))
fsIgmpSnoopingMIBCompliance2.setObjects((_A,_AI))
if mibBuilder.loadTexts:fsIgmpSnoopingMIBCompliance2.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'fsIgmpSnoopingMIB':fsIgmpSnoopingMIB,'fsIgmpSnoopingMIBObjects':fsIgmpSnoopingMIBObjects,_j:fsSNIgmpWorkingMode,_k:fsSNIgmpSourcePortCheck,_l:fsSNIgmpSourceIpCheck,_m:fsSNIgmpSourceIpCheckDefIp,'fsSNIgmpSrcIpCheckTable':fsSNIgmpSrcIpCheckTable,'fsSNIgmpSrcIpCheckEntry':fsSNIgmpSrcIpCheckEntry,_I:fsSNIgmpSrcIpCheckVID,_J:fsSNIgmpSrcIpCheckMultiIpAddr,_n:fsSNIgmpSrcIpCheckSrcIpAddr,_o:fsSNIgmpSrcIpCheckEntryStatus,'fsSNIgmpPortTable':fsSNIgmpPortTable,'fsSNIgmpPortEntry':fsSNIgmpPortEntry,_K:fsSNIgmpPortRouterVID,_L:fsSNIgmpPortIndex,_p:fsSNIgmpPortRouterState,_q:fsSNIgmpPortRouterProfile,_r:fsSNIgmpGDANumber,'fsSNIgmpGDATable':fsSNIgmpGDATable,'fsSNIgmpGDAEntry':fsSNIgmpGDAEntry,_M:fsSNIgmpGDAVID,_N:fsSNIgmpGDAAddr,_s:fsSNIgmpGDAPortMemberAction,_t:fsSNIgmpGDATrunkMemberAction,_u:fsSNIgmpSvglVID,_v:fsSNIgmpSvglProfile,'fsSNIgmpMrLearnTable':fsSNIgmpMrLearnTable,'fsSNIgmpMrLearnEntry':fsSNIgmpMrLearnEntry,_O:fsSNIgmpMrLearnVID,_w:fsSNIgmpMrLearnStatus,'fsSNIgmpPortFilteringTable':fsSNIgmpPortFilteringTable,'fsSNIgmpPortFilteringEntry':fsSNIgmpPortFilteringEntry,_P:fsSNPortIndex,_x:fsSNIgmpFilteringProfile,_y:fsSNIgmpFilteringMaxGroups,'fsSNIgmpGDAConfigTable':fsSNIgmpGDAConfigTable,'fsSNIgmpGDAConfigEntry':fsSNIgmpGDAConfigEntry,_Q:fsSNIgmpGDAConfigVID,_R:fsSNIgmpGDAConfigAddr,_z:fsSNIgmpGDAConfigIfIndex,_A0:fsSNIgmpGDAConfigType,_A1:fsSNIgmpGDAConfigStatus,_A2:fsSNIgmpQueryResponeTime,_A3:fsIgmpSnoopingWorkingMode,_A4:fsIgmpSnoopingGDANumber,'fsIgmpSnoopingGDATable':fsIgmpSnoopingGDATable,'fsIgmpSnoopingGDAEntry':fsIgmpSnoopingGDAEntry,_S:fsIgmpSnoopingGDAVID,_T:fsIgmpSnoopingGDAAddr,_A5:fsIgmpSnoopingGDAPortMemberAction,'fsIgmpSnoopingVlanStatusTable':fsIgmpSnoopingVlanStatusTable,'fsIgmpSnoopingVlanStatusEntry':fsIgmpSnoopingVlanStatusEntry,_U:fsIgmpSnoopingVlanStatusVID,_A6:fsIgmpSnoopingVlanStatusStatus,_A7:fsIgmpSnoopingSvglVID,_A8:fsIgmpSnoopingSvglProfile,'fsIgmpSnoopingMrLearnTable':fsIgmpSnoopingMrLearnTable,'fsIgmpSnoopingMrLearnEntry':fsIgmpSnoopingMrLearnEntry,_V:fsIgmpSnoopingMrLearnVID,_A9:fsIgmpSnoopingMrLearnStatus,'fsIgmpSnoopingPortFilteringTable':fsIgmpSnoopingPortFilteringTable,'fsIgmpSnoopingPortFilteringEntry':fsIgmpSnoopingPortFilteringEntry,_W:fsIgmpSnoopingportIndex,_AA:fsIgmpSnoopingFilteringProfile,_AB:fsIgmpSnoopingFilteringMaxGroups,'fsIgmpSnoopingGDAConfigTable':fsIgmpSnoopingGDAConfigTable,'fsIgmpSnoopingGDAConfigEntry':fsIgmpSnoopingGDAConfigEntry,_X:fsIgmpSnoopingGDAConfigVID,_Y:fsIgmpSnoopingGDAConfigAddr,_Z:fsIgmpSnoopingGDAConfigIfIndex,_AC:fsIgmpSnoopingQueryResponeTime,_AD:fsIgmpSnoopingReportSuppress,_AE:fsIgmpSnoopingFastleave,'fsIgmpSnoopingGDANewTable':fsIgmpSnoopingGDANewTable,'fsIgmpSnoopingGDANewEntry':fsIgmpSnoopingGDANewEntry,_a:fsIgmpSnoopingGDANewInVID,_b:fsIgmpSnoopingGDANewOutVID,_c:fsIgsmpSnoopingGDASrc,_d:fsIgmpSnoopingGDAGrp,_e:fsIgmpSnoopingGDAIfx,_AF:fsIgmpSnoopingGDAIfxAction,_AG:fsIgmpSnoopingMulticastWlan,'fsIgmpSnoopingMIBConformance':fsIgmpSnoopingMIBConformance,'fsIgmpSnoopingMIBCompliances':fsIgmpSnoopingMIBCompliances,'fsIgmpSnoopingMIBCompliance':fsIgmpSnoopingMIBCompliance,'fsIgmpSnoopingMIBCompliance2':fsIgmpSnoopingMIBCompliance2,'fsIgmpSnoopingMIBGroups':fsIgmpSnoopingMIBGroups,_AH:fsIgmpSnoopingMIBGroup,_AI:fsIgmpSnoopingMIBGroup2})