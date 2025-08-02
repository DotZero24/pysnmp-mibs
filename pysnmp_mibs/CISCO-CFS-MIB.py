_AW='cfsFeatureOpExtGroupRev1'
_AV='cfsFeatureOpGroupRev1'
_AU='cfsFeatureOpGroup'
_AT='ciscoCFSDiscoveryCompleteNotif'
_AS='ciscoCFSMergeFailNotif'
_AR='ciscoCFSFeatureActionNotif'
_AQ='cfsFeatureOpExtLastActionTime'
_AP='cfsFeatureOpAttribs'
_AO='cfsDistCtrlAction'
_AN='cfsDistCtrlAddr'
_AM='cfsDistCtrl'
_AL='cfsStartPeersDiscovery'
_AK='cfsMergeMemberRole'
_AJ='cfsMergeMemberFabricType'
_AI='cfsPendingConfOwnerID'
_AH='cfsPendingConfOwnerIDType'
_AG='cfsPendingConfOwnerAddr'
_AF='cfsPendingConfOwnerAddrType'
_AE='cfsFeatureOpShowCfgOption'
_AD='cfsDistCtrlAddrType'
_AC='cfsFeatureOpExtScopeVal'
_AB='cfsFeatureOpExtScopeType'
_AA='cfsFeaturePeersAddrType'
_A9='cfsFeaturePeersScopeVal'
_A8='cfsFeaturePeersScopeType'
_A7='cfsPeerAddrType'
_A6='cfsMergeMemberAddr'
_A5='cfsMergeMemberAddrType'
_A4='cfsPendingConfOwnerScopeVal'
_A3='cfsPendingConfOwnerScopeType'
_A2='pendingConfig'
_A1='runningConfig'
_A0='CiscoCFSScopeType'
_z='success'
_y='cfsDistCtrlInetGroup'
_x='cfsFeatureOpGroupRev2'
_w='cfsFeatureOpExtGroup'
_v='cfsFeatureOpExtShowCfgOption'
_u='cfsFeatureOpExtLastFailureReason'
_t='cfsFeatureOpExtLastActionResult'
_s='cfsFeatureOpExtLastAction'
_r='cfsPeersDiscoveryFailureReason'
_q='cfsPeersDiscoveryResult'
_p='cfsMergeFailReasonDescription'
_o='cfsMergeFailScopeVal'
_n='cfsMergeFailScopeType'
_m='cfsMergeFailFeatureName'
_l='cfsFeaturePeersAddr'
_k='cfsPeerAddr'
_j='cfsMergeStatusScopeVal'
_i='cfsMergeStatusScopeType'
_h='inProgress'
_g='unknown'
_f='disable'
_e='enable'
_d='Bits'
_c='SnmpAdminString'
_b='cfsDistCtrlGroup'
_a='cfsPeerDiscoveryNotifGroup'
_Z='cfsMembersGroup'
_Y='cfsMergeStatusValue'
_X='cfsFeatureOpStatus'
_W='cfsFeatureOpLastFailureReason'
_V='cfsFeatureOpScopeVal'
_U='cfsFeatureOpScopeType'
_T='cfsFeatureOpAction'
_S='accessible-for-notify'
_R='InetAddress'
_Q='cfsMergeFailNotifGroup'
_P='cfsFeatureNotifObjectsGroup'
_O='cfsFeatureActionNotifGroup'
_N='cfsPendingConfOwnerGroup'
_M='cfsFeatureOpLastActionResult'
_L='cfsFeatureOpLastScopeVal'
_K='cfsFeatureOpLastScopeType'
_J='cfsFeatureOpLastAction'
_I='deprecated'
_H='cfsFeatureOpName'
_G='CiscoCFSScopeValue'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-CFS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_c)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_d,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoCFSMIB=ModuleIdentity((1,3,6,1,4,1,9,9,433))
if mibBuilder.loadTexts:ciscoCFSMIB.setRevisions(('2006-06-13 00:00','2005-11-30 00:00','2005-04-27 00:00','2004-12-24 00:00','2004-12-03 00:00','2004-09-15 00:00'))
class CiscoCFSAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noop',1),(_e,2),(_f,3),('commit',4),('abort',5),('clear',6)))
class CiscoCFSFeatureStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('enabled',2),('disabled',3)))
class CiscoCFSFeatureActionResult(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),(_z,2),('failed',3),(_h,4),('partialSuccess',5)))
class CiscoCFSScopeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('vsanID',2)))
class CiscoCFSScopeValue(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoCFSMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCFSMIBNotifs=_CiscoCFSMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,433,0))
_CiscoCFSMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCFSMIBObjects=_CiscoCFSMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,433,1))
_CfsFeature_ObjectIdentity=ObjectIdentity
cfsFeature=_CfsFeature_ObjectIdentity((1,3,6,1,4,1,9,9,433,1,1))
_CfsFeatureOpTable_Object=MibTable
cfsFeatureOpTable=_CfsFeatureOpTable_Object((1,3,6,1,4,1,9,9,433,1,1,1))
if mibBuilder.loadTexts:cfsFeatureOpTable.setStatus(_B)
_CfsFeatureOpEntry_Object=MibTableRow
cfsFeatureOpEntry=_CfsFeatureOpEntry_Object((1,3,6,1,4,1,9,9,433,1,1,1,1))
cfsFeatureOpEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cfsFeatureOpEntry.setStatus(_B)
class _CfsFeatureOpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsFeatureOpName_Type.__name__=_c
_CfsFeatureOpName_Object=MibTableColumn
cfsFeatureOpName=_CfsFeatureOpName_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,1),_CfsFeatureOpName_Type())
cfsFeatureOpName.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsFeatureOpName.setStatus(_B)
_CfsFeatureOpAction_Type=CiscoCFSAction
_CfsFeatureOpAction_Object=MibTableColumn
cfsFeatureOpAction=_CfsFeatureOpAction_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,2),_CfsFeatureOpAction_Type())
cfsFeatureOpAction.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsFeatureOpAction.setStatus(_B)
class _CfsFeatureOpScopeType_Type(CiscoCFSScopeType):defaultValue=1
_CfsFeatureOpScopeType_Type.__name__=_A0
_CfsFeatureOpScopeType_Object=MibTableColumn
cfsFeatureOpScopeType=_CfsFeatureOpScopeType_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,3),_CfsFeatureOpScopeType_Type())
cfsFeatureOpScopeType.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsFeatureOpScopeType.setStatus(_B)
class _CfsFeatureOpScopeVal_Type(CiscoCFSScopeValue):defaultHexValue='';subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsFeatureOpScopeVal_Type.__name__=_G
_CfsFeatureOpScopeVal_Object=MibTableColumn
cfsFeatureOpScopeVal=_CfsFeatureOpScopeVal_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,4),_CfsFeatureOpScopeVal_Type())
cfsFeatureOpScopeVal.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsFeatureOpScopeVal.setStatus(_B)
_CfsFeatureOpLastAction_Type=CiscoCFSAction
_CfsFeatureOpLastAction_Object=MibTableColumn
cfsFeatureOpLastAction=_CfsFeatureOpLastAction_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,5),_CfsFeatureOpLastAction_Type())
cfsFeatureOpLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpLastAction.setStatus(_B)
_CfsFeatureOpLastScopeType_Type=CiscoCFSScopeType
_CfsFeatureOpLastScopeType_Object=MibTableColumn
cfsFeatureOpLastScopeType=_CfsFeatureOpLastScopeType_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,6),_CfsFeatureOpLastScopeType_Type())
cfsFeatureOpLastScopeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpLastScopeType.setStatus(_B)
class _CfsFeatureOpLastScopeVal_Type(CiscoCFSScopeValue):subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsFeatureOpLastScopeVal_Type.__name__=_G
_CfsFeatureOpLastScopeVal_Object=MibTableColumn
cfsFeatureOpLastScopeVal=_CfsFeatureOpLastScopeVal_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,7),_CfsFeatureOpLastScopeVal_Type())
cfsFeatureOpLastScopeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpLastScopeVal.setStatus(_B)
_CfsFeatureOpLastActionResult_Type=CiscoCFSFeatureActionResult
_CfsFeatureOpLastActionResult_Object=MibTableColumn
cfsFeatureOpLastActionResult=_CfsFeatureOpLastActionResult_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,8),_CfsFeatureOpLastActionResult_Type())
cfsFeatureOpLastActionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpLastActionResult.setStatus(_B)
_CfsFeatureOpLastFailureReason_Type=SnmpAdminString
_CfsFeatureOpLastFailureReason_Object=MibTableColumn
cfsFeatureOpLastFailureReason=_CfsFeatureOpLastFailureReason_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,9),_CfsFeatureOpLastFailureReason_Type())
cfsFeatureOpLastFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpLastFailureReason.setStatus(_B)
class _CfsFeatureOpShowCfgOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A1,1),(_A2,2)))
_CfsFeatureOpShowCfgOption_Type.__name__=_E
_CfsFeatureOpShowCfgOption_Object=MibTableColumn
cfsFeatureOpShowCfgOption=_CfsFeatureOpShowCfgOption_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,10),_CfsFeatureOpShowCfgOption_Type())
cfsFeatureOpShowCfgOption.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsFeatureOpShowCfgOption.setStatus(_I)
_CfsFeatureOpStatus_Type=CiscoCFSFeatureStatus
_CfsFeatureOpStatus_Object=MibTableColumn
cfsFeatureOpStatus=_CfsFeatureOpStatus_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,11),_CfsFeatureOpStatus_Type())
cfsFeatureOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpStatus.setStatus(_B)
class _CfsFeatureOpAttribs_Type(Bits):namedValues=NamedValues(*(('fcFabric',0),('ipNetwork',1),('vsanScope',2)))
_CfsFeatureOpAttribs_Type.__name__=_d
_CfsFeatureOpAttribs_Object=MibTableColumn
cfsFeatureOpAttribs=_CfsFeatureOpAttribs_Object((1,3,6,1,4,1,9,9,433,1,1,1,1,12),_CfsFeatureOpAttribs_Type())
cfsFeatureOpAttribs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpAttribs.setStatus(_B)
_CfsPendingConfOwnerTable_Object=MibTable
cfsPendingConfOwnerTable=_CfsPendingConfOwnerTable_Object((1,3,6,1,4,1,9,9,433,1,1,2))
if mibBuilder.loadTexts:cfsPendingConfOwnerTable.setStatus(_B)
_CfsPendingConfOwnerEntry_Object=MibTableRow
cfsPendingConfOwnerEntry=_CfsPendingConfOwnerEntry_Object((1,3,6,1,4,1,9,9,433,1,1,2,1))
cfsPendingConfOwnerEntry.setIndexNames((0,_A,_H),(0,_A,_A3),(0,_A,_A4))
if mibBuilder.loadTexts:cfsPendingConfOwnerEntry.setStatus(_B)
_CfsPendingConfOwnerScopeType_Type=CiscoCFSScopeType
_CfsPendingConfOwnerScopeType_Object=MibTableColumn
cfsPendingConfOwnerScopeType=_CfsPendingConfOwnerScopeType_Object((1,3,6,1,4,1,9,9,433,1,1,2,1,1),_CfsPendingConfOwnerScopeType_Type())
cfsPendingConfOwnerScopeType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsPendingConfOwnerScopeType.setStatus(_B)
class _CfsPendingConfOwnerScopeVal_Type(CiscoCFSScopeValue):subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsPendingConfOwnerScopeVal_Type.__name__=_G
_CfsPendingConfOwnerScopeVal_Object=MibTableColumn
cfsPendingConfOwnerScopeVal=_CfsPendingConfOwnerScopeVal_Object((1,3,6,1,4,1,9,9,433,1,1,2,1,2),_CfsPendingConfOwnerScopeVal_Type())
cfsPendingConfOwnerScopeVal.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsPendingConfOwnerScopeVal.setStatus(_B)
_CfsPendingConfOwnerAddrType_Type=InetAddressType
_CfsPendingConfOwnerAddrType_Object=MibTableColumn
cfsPendingConfOwnerAddrType=_CfsPendingConfOwnerAddrType_Object((1,3,6,1,4,1,9,9,433,1,1,2,1,3),_CfsPendingConfOwnerAddrType_Type())
cfsPendingConfOwnerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPendingConfOwnerAddrType.setStatus(_B)
_CfsPendingConfOwnerAddr_Type=InetAddress
_CfsPendingConfOwnerAddr_Object=MibTableColumn
cfsPendingConfOwnerAddr=_CfsPendingConfOwnerAddr_Object((1,3,6,1,4,1,9,9,433,1,1,2,1,4),_CfsPendingConfOwnerAddr_Type())
cfsPendingConfOwnerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPendingConfOwnerAddr.setStatus(_B)
class _CfsPendingConfOwnerIDType_Type(Bits):namedValues=NamedValues(*(('other',0),('snmpCommunityName',1),('snmpv3SecurityName',2),('cliLoginName',3)))
_CfsPendingConfOwnerIDType_Type.__name__=_d
_CfsPendingConfOwnerIDType_Object=MibTableColumn
cfsPendingConfOwnerIDType=_CfsPendingConfOwnerIDType_Object((1,3,6,1,4,1,9,9,433,1,1,2,1,5),_CfsPendingConfOwnerIDType_Type())
cfsPendingConfOwnerIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPendingConfOwnerIDType.setStatus(_B)
_CfsPendingConfOwnerID_Type=SnmpAdminString
_CfsPendingConfOwnerID_Object=MibTableColumn
cfsPendingConfOwnerID=_CfsPendingConfOwnerID_Object((1,3,6,1,4,1,9,9,433,1,1,2,1,6),_CfsPendingConfOwnerID_Type())
cfsPendingConfOwnerID.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPendingConfOwnerID.setStatus(_B)
_CfsMergeStatusTable_Object=MibTable
cfsMergeStatusTable=_CfsMergeStatusTable_Object((1,3,6,1,4,1,9,9,433,1,1,3))
if mibBuilder.loadTexts:cfsMergeStatusTable.setStatus(_B)
_CfsMergeStatusEntry_Object=MibTableRow
cfsMergeStatusEntry=_CfsMergeStatusEntry_Object((1,3,6,1,4,1,9,9,433,1,1,3,1))
cfsMergeStatusEntry.setIndexNames((0,_A,_H),(0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:cfsMergeStatusEntry.setStatus(_B)
_CfsMergeStatusScopeType_Type=CiscoCFSScopeType
_CfsMergeStatusScopeType_Object=MibTableColumn
cfsMergeStatusScopeType=_CfsMergeStatusScopeType_Object((1,3,6,1,4,1,9,9,433,1,1,3,1,1),_CfsMergeStatusScopeType_Type())
cfsMergeStatusScopeType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsMergeStatusScopeType.setStatus(_B)
class _CfsMergeStatusScopeVal_Type(CiscoCFSScopeValue):subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsMergeStatusScopeVal_Type.__name__=_G
_CfsMergeStatusScopeVal_Object=MibTableColumn
cfsMergeStatusScopeVal=_CfsMergeStatusScopeVal_Object((1,3,6,1,4,1,9,9,433,1,1,3,1,2),_CfsMergeStatusScopeVal_Type())
cfsMergeStatusScopeVal.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsMergeStatusScopeVal.setStatus(_B)
class _CfsMergeStatusValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_z,1),(_h,2),('failure',3),('waiting',4),('other',5)))
_CfsMergeStatusValue_Type.__name__=_E
_CfsMergeStatusValue_Object=MibTableColumn
cfsMergeStatusValue=_CfsMergeStatusValue_Object((1,3,6,1,4,1,9,9,433,1,1,3,1,3),_CfsMergeStatusValue_Type())
cfsMergeStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsMergeStatusValue.setStatus(_B)
_CfsMergeMembersTable_Object=MibTable
cfsMergeMembersTable=_CfsMergeMembersTable_Object((1,3,6,1,4,1,9,9,433,1,1,4))
if mibBuilder.loadTexts:cfsMergeMembersTable.setStatus(_B)
_CfsMergeMembersEntry_Object=MibTableRow
cfsMergeMembersEntry=_CfsMergeMembersEntry_Object((1,3,6,1,4,1,9,9,433,1,1,4,1))
cfsMergeMembersEntry.setIndexNames((0,_A,_H),(0,_A,_i),(0,_A,_j),(0,_A,_A5),(0,_A,_A6))
if mibBuilder.loadTexts:cfsMergeMembersEntry.setStatus(_B)
_CfsMergeMemberAddrType_Type=InetAddressType
_CfsMergeMemberAddrType_Object=MibTableColumn
cfsMergeMemberAddrType=_CfsMergeMemberAddrType_Object((1,3,6,1,4,1,9,9,433,1,1,4,1,1),_CfsMergeMemberAddrType_Type())
cfsMergeMemberAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsMergeMemberAddrType.setStatus(_B)
class _CfsMergeMemberAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsMergeMemberAddr_Type.__name__=_R
_CfsMergeMemberAddr_Object=MibTableColumn
cfsMergeMemberAddr=_CfsMergeMemberAddr_Object((1,3,6,1,4,1,9,9,433,1,1,4,1,2),_CfsMergeMemberAddr_Type())
cfsMergeMemberAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsMergeMemberAddr.setStatus(_B)
class _CfsMergeMemberFabricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('local',2),('remote',3)))
_CfsMergeMemberFabricType_Type.__name__=_E
_CfsMergeMemberFabricType_Object=MibTableColumn
cfsMergeMemberFabricType=_CfsMergeMemberFabricType_Object((1,3,6,1,4,1,9,9,433,1,1,4,1,3),_CfsMergeMemberFabricType_Type())
cfsMergeMemberFabricType.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsMergeMemberFabricType.setStatus(_B)
class _CfsMergeMemberRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('master',2),('peer',3)))
_CfsMergeMemberRole_Type.__name__=_E
_CfsMergeMemberRole_Object=MibTableColumn
cfsMergeMemberRole=_CfsMergeMemberRole_Object((1,3,6,1,4,1,9,9,433,1,1,4,1,4),_CfsMergeMemberRole_Type())
cfsMergeMemberRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsMergeMemberRole.setStatus(_B)
_CfsPeersTable_Object=MibTable
cfsPeersTable=_CfsPeersTable_Object((1,3,6,1,4,1,9,9,433,1,1,5))
if mibBuilder.loadTexts:cfsPeersTable.setStatus(_B)
_CfsPeersEntry_Object=MibTableRow
cfsPeersEntry=_CfsPeersEntry_Object((1,3,6,1,4,1,9,9,433,1,1,5,1))
cfsPeersEntry.setIndexNames((0,_A,_A7),(0,_A,_k))
if mibBuilder.loadTexts:cfsPeersEntry.setStatus(_B)
_CfsPeerAddrType_Type=InetAddressType
_CfsPeerAddrType_Object=MibTableColumn
cfsPeerAddrType=_CfsPeerAddrType_Object((1,3,6,1,4,1,9,9,433,1,1,5,1,1),_CfsPeerAddrType_Type())
cfsPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsPeerAddrType.setStatus(_B)
class _CfsPeerAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsPeerAddr_Type.__name__=_R
_CfsPeerAddr_Object=MibTableColumn
cfsPeerAddr=_CfsPeerAddr_Object((1,3,6,1,4,1,9,9,433,1,1,5,1,2),_CfsPeerAddr_Type())
cfsPeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPeerAddr.setStatus(_B)
_CfsFeaturePeersTable_Object=MibTable
cfsFeaturePeersTable=_CfsFeaturePeersTable_Object((1,3,6,1,4,1,9,9,433,1,1,6))
if mibBuilder.loadTexts:cfsFeaturePeersTable.setStatus(_B)
_CfsFeaturePeersEntry_Object=MibTableRow
cfsFeaturePeersEntry=_CfsFeaturePeersEntry_Object((1,3,6,1,4,1,9,9,433,1,1,6,1))
cfsFeaturePeersEntry.setIndexNames((0,_A,_H),(0,_A,_A8),(0,_A,_A9),(0,_A,_AA),(0,_A,_l))
if mibBuilder.loadTexts:cfsFeaturePeersEntry.setStatus(_B)
_CfsFeaturePeersScopeType_Type=CiscoCFSScopeType
_CfsFeaturePeersScopeType_Object=MibTableColumn
cfsFeaturePeersScopeType=_CfsFeaturePeersScopeType_Object((1,3,6,1,4,1,9,9,433,1,1,6,1,1),_CfsFeaturePeersScopeType_Type())
cfsFeaturePeersScopeType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsFeaturePeersScopeType.setStatus(_B)
class _CfsFeaturePeersScopeVal_Type(CiscoCFSScopeValue):subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsFeaturePeersScopeVal_Type.__name__=_G
_CfsFeaturePeersScopeVal_Object=MibTableColumn
cfsFeaturePeersScopeVal=_CfsFeaturePeersScopeVal_Object((1,3,6,1,4,1,9,9,433,1,1,6,1,2),_CfsFeaturePeersScopeVal_Type())
cfsFeaturePeersScopeVal.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsFeaturePeersScopeVal.setStatus(_B)
_CfsFeaturePeersAddrType_Type=InetAddressType
_CfsFeaturePeersAddrType_Object=MibTableColumn
cfsFeaturePeersAddrType=_CfsFeaturePeersAddrType_Object((1,3,6,1,4,1,9,9,433,1,1,6,1,3),_CfsFeaturePeersAddrType_Type())
cfsFeaturePeersAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsFeaturePeersAddrType.setStatus(_B)
class _CfsFeaturePeersAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsFeaturePeersAddr_Type.__name__=_R
_CfsFeaturePeersAddr_Object=MibTableColumn
cfsFeaturePeersAddr=_CfsFeaturePeersAddr_Object((1,3,6,1,4,1,9,9,433,1,1,6,1,4),_CfsFeaturePeersAddr_Type())
cfsFeaturePeersAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeaturePeersAddr.setStatus(_B)
_CfsFeatureOpExtTable_Object=MibTable
cfsFeatureOpExtTable=_CfsFeatureOpExtTable_Object((1,3,6,1,4,1,9,9,433,1,1,7))
if mibBuilder.loadTexts:cfsFeatureOpExtTable.setStatus(_B)
_CfsFeatureOpExtEntry_Object=MibTableRow
cfsFeatureOpExtEntry=_CfsFeatureOpExtEntry_Object((1,3,6,1,4,1,9,9,433,1,1,7,1))
cfsFeatureOpExtEntry.setIndexNames((0,_A,_H),(0,_A,_AB),(0,_A,_AC))
if mibBuilder.loadTexts:cfsFeatureOpExtEntry.setStatus(_B)
_CfsFeatureOpExtScopeType_Type=CiscoCFSScopeType
_CfsFeatureOpExtScopeType_Object=MibTableColumn
cfsFeatureOpExtScopeType=_CfsFeatureOpExtScopeType_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,1),_CfsFeatureOpExtScopeType_Type())
cfsFeatureOpExtScopeType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsFeatureOpExtScopeType.setStatus(_B)
class _CfsFeatureOpExtScopeVal_Type(CiscoCFSScopeValue):subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsFeatureOpExtScopeVal_Type.__name__=_G
_CfsFeatureOpExtScopeVal_Object=MibTableColumn
cfsFeatureOpExtScopeVal=_CfsFeatureOpExtScopeVal_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,2),_CfsFeatureOpExtScopeVal_Type())
cfsFeatureOpExtScopeVal.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsFeatureOpExtScopeVal.setStatus(_B)
_CfsFeatureOpExtLastAction_Type=CiscoCFSAction
_CfsFeatureOpExtLastAction_Object=MibTableColumn
cfsFeatureOpExtLastAction=_CfsFeatureOpExtLastAction_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,3),_CfsFeatureOpExtLastAction_Type())
cfsFeatureOpExtLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpExtLastAction.setStatus(_B)
_CfsFeatureOpExtLastActionResult_Type=CiscoCFSFeatureActionResult
_CfsFeatureOpExtLastActionResult_Object=MibTableColumn
cfsFeatureOpExtLastActionResult=_CfsFeatureOpExtLastActionResult_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,4),_CfsFeatureOpExtLastActionResult_Type())
cfsFeatureOpExtLastActionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpExtLastActionResult.setStatus(_B)
_CfsFeatureOpExtLastFailureReason_Type=SnmpAdminString
_CfsFeatureOpExtLastFailureReason_Object=MibTableColumn
cfsFeatureOpExtLastFailureReason=_CfsFeatureOpExtLastFailureReason_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,5),_CfsFeatureOpExtLastFailureReason_Type())
cfsFeatureOpExtLastFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpExtLastFailureReason.setStatus(_B)
class _CfsFeatureOpExtShowCfgOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A1,1),(_A2,2)))
_CfsFeatureOpExtShowCfgOption_Type.__name__=_E
_CfsFeatureOpExtShowCfgOption_Object=MibTableColumn
cfsFeatureOpExtShowCfgOption=_CfsFeatureOpExtShowCfgOption_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,6),_CfsFeatureOpExtShowCfgOption_Type())
cfsFeatureOpExtShowCfgOption.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsFeatureOpExtShowCfgOption.setStatus(_B)
_CfsFeatureOpExtLastActionTime_Type=TimeStamp
_CfsFeatureOpExtLastActionTime_Object=MibTableColumn
cfsFeatureOpExtLastActionTime=_CfsFeatureOpExtLastActionTime_Object((1,3,6,1,4,1,9,9,433,1,1,7,1,7),_CfsFeatureOpExtLastActionTime_Type())
cfsFeatureOpExtLastActionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsFeatureOpExtLastActionTime.setStatus(_B)
_CfsNotifObjects_ObjectIdentity=ObjectIdentity
cfsNotifObjects=_CfsNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,433,1,2))
class _CfsMergeFailFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsMergeFailFeatureName_Type.__name__=_c
_CfsMergeFailFeatureName_Object=MibScalar
cfsMergeFailFeatureName=_CfsMergeFailFeatureName_Object((1,3,6,1,4,1,9,9,433,1,2,1),_CfsMergeFailFeatureName_Type())
cfsMergeFailFeatureName.setMaxAccess(_S)
if mibBuilder.loadTexts:cfsMergeFailFeatureName.setStatus(_B)
_CfsMergeFailScopeType_Type=CiscoCFSScopeType
_CfsMergeFailScopeType_Object=MibScalar
cfsMergeFailScopeType=_CfsMergeFailScopeType_Object((1,3,6,1,4,1,9,9,433,1,2,2),_CfsMergeFailScopeType_Type())
cfsMergeFailScopeType.setMaxAccess(_S)
if mibBuilder.loadTexts:cfsMergeFailScopeType.setStatus(_B)
class _CfsMergeFailScopeVal_Type(CiscoCFSScopeValue):subtypeSpec=CiscoCFSScopeValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfsMergeFailScopeVal_Type.__name__=_G
_CfsMergeFailScopeVal_Object=MibScalar
cfsMergeFailScopeVal=_CfsMergeFailScopeVal_Object((1,3,6,1,4,1,9,9,433,1,2,3),_CfsMergeFailScopeVal_Type())
cfsMergeFailScopeVal.setMaxAccess(_S)
if mibBuilder.loadTexts:cfsMergeFailScopeVal.setStatus(_B)
_CfsMergeFailReasonDescription_Type=SnmpAdminString
_CfsMergeFailReasonDescription_Object=MibScalar
cfsMergeFailReasonDescription=_CfsMergeFailReasonDescription_Object((1,3,6,1,4,1,9,9,433,1,2,4),_CfsMergeFailReasonDescription_Type())
cfsMergeFailReasonDescription.setMaxAccess(_S)
if mibBuilder.loadTexts:cfsMergeFailReasonDescription.setStatus(_B)
_CfsDiscoveryObjects_ObjectIdentity=ObjectIdentity
cfsDiscoveryObjects=_CfsDiscoveryObjects_ObjectIdentity((1,3,6,1,4,1,9,9,433,1,3))
class _CfsStartPeersDiscovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('startDiscovery',1),('noOp',2)))
_CfsStartPeersDiscovery_Type.__name__=_E
_CfsStartPeersDiscovery_Object=MibScalar
cfsStartPeersDiscovery=_CfsStartPeersDiscovery_Object((1,3,6,1,4,1,9,9,433,1,3,1),_CfsStartPeersDiscovery_Type())
cfsStartPeersDiscovery.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsStartPeersDiscovery.setStatus(_B)
class _CfsPeersDiscoveryResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notInitiated',1),(_h,2),('successful',3),('failed',4)))
_CfsPeersDiscoveryResult_Type.__name__=_E
_CfsPeersDiscoveryResult_Object=MibScalar
cfsPeersDiscoveryResult=_CfsPeersDiscoveryResult_Object((1,3,6,1,4,1,9,9,433,1,3,2),_CfsPeersDiscoveryResult_Type())
cfsPeersDiscoveryResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPeersDiscoveryResult.setStatus(_B)
_CfsPeersDiscoveryFailureReason_Type=SnmpAdminString
_CfsPeersDiscoveryFailureReason_Object=MibScalar
cfsPeersDiscoveryFailureReason=_CfsPeersDiscoveryFailureReason_Object((1,3,6,1,4,1,9,9,433,1,3,3),_CfsPeersDiscoveryFailureReason_Type())
cfsPeersDiscoveryFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfsPeersDiscoveryFailureReason.setStatus(_B)
_CfsDistCtrlObjects_ObjectIdentity=ObjectIdentity
cfsDistCtrlObjects=_CfsDistCtrlObjects_ObjectIdentity((1,3,6,1,4,1,9,9,433,1,4))
class _CfsDistCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_CfsDistCtrl_Type.__name__=_E
_CfsDistCtrl_Object=MibScalar
cfsDistCtrl=_CfsDistCtrl_Object((1,3,6,1,4,1,9,9,433,1,4,1),_CfsDistCtrl_Type())
cfsDistCtrl.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsDistCtrl.setStatus(_B)
_CfsDistCtrlTable_Object=MibTable
cfsDistCtrlTable=_CfsDistCtrlTable_Object((1,3,6,1,4,1,9,9,433,1,4,2))
if mibBuilder.loadTexts:cfsDistCtrlTable.setStatus(_B)
_CfsDistCtrlEntry_Object=MibTableRow
cfsDistCtrlEntry=_CfsDistCtrlEntry_Object((1,3,6,1,4,1,9,9,433,1,4,2,1))
cfsDistCtrlEntry.setIndexNames((0,_A,_AD))
if mibBuilder.loadTexts:cfsDistCtrlEntry.setStatus(_B)
_CfsDistCtrlAddrType_Type=InetAddressType
_CfsDistCtrlAddrType_Object=MibTableColumn
cfsDistCtrlAddrType=_CfsDistCtrlAddrType_Object((1,3,6,1,4,1,9,9,433,1,4,2,1,1),_CfsDistCtrlAddrType_Type())
cfsDistCtrlAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cfsDistCtrlAddrType.setStatus(_B)
_CfsDistCtrlAddr_Type=InetAddress
_CfsDistCtrlAddr_Object=MibTableColumn
cfsDistCtrlAddr=_CfsDistCtrlAddr_Object((1,3,6,1,4,1,9,9,433,1,4,2,1,2),_CfsDistCtrlAddr_Type())
cfsDistCtrlAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsDistCtrlAddr.setStatus(_B)
class _CfsDistCtrlAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_CfsDistCtrlAction_Type.__name__=_E
_CfsDistCtrlAction_Object=MibTableColumn
cfsDistCtrlAction=_CfsDistCtrlAction_Object((1,3,6,1,4,1,9,9,433,1,4,2,1,3),_CfsDistCtrlAction_Type())
cfsDistCtrlAction.setMaxAccess(_F)
if mibBuilder.loadTexts:cfsDistCtrlAction.setStatus(_B)
_CiscoCFSMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCFSMIBConformance=_CiscoCFSMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,433,2))
_CiscoCFSMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCFSMIBCompliances=_CiscoCFSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,433,2,1))
_CiscoCFSMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCFSMIBGroups=_CiscoCFSMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,433,2,2))
cfsFeatureOpGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,1))
cfsFeatureOpGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_W),(_A,_AE),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cfsFeatureOpGroup.setStatus(_I)
cfsPendingConfOwnerGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,2))
cfsPendingConfOwnerGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:cfsPendingConfOwnerGroup.setStatus(_B)
cfsFeatureNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,3))
cfsFeatureNotifObjectsGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cfsFeatureNotifObjectsGroup.setStatus(_B)
cfsMembersGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,6))
cfsMembersGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_q),(_A,_r),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cfsMembersGroup.setStatus(_B)
cfsFeatureOpExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,7))
cfsFeatureOpExtGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:cfsFeatureOpExtGroup.setStatus(_I)
cfsFeatureOpGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,9))
cfsFeatureOpGroupRev1.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cfsFeatureOpGroupRev1.setStatus(_I)
cfsDistCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,10))
cfsDistCtrlGroup.setObjects((_A,_AM))
if mibBuilder.loadTexts:cfsDistCtrlGroup.setStatus(_B)
cfsDistCtrlInetGroup=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,11))
cfsDistCtrlInetGroup.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cfsDistCtrlInetGroup.setStatus(_B)
cfsFeatureOpGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,12))
cfsFeatureOpGroupRev2.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_W),(_A,_X),(_A,_Y),(_A,_AP)))
if mibBuilder.loadTexts:cfsFeatureOpGroupRev2.setStatus(_B)
cfsFeatureOpExtGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,433,2,2,13))
cfsFeatureOpExtGroupRev1.setObjects(*((_A,_s),(_A,_AQ),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:cfsFeatureOpExtGroupRev1.setStatus(_B)
ciscoCFSFeatureActionNotif=NotificationType((1,3,6,1,4,1,9,9,433,0,1))
ciscoCFSFeatureActionNotif.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoCFSFeatureActionNotif.setStatus(_B)
ciscoCFSMergeFailNotif=NotificationType((1,3,6,1,4,1,9,9,433,0,2))
ciscoCFSMergeFailNotif.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ciscoCFSMergeFailNotif.setStatus(_B)
ciscoCFSDiscoveryCompleteNotif=NotificationType((1,3,6,1,4,1,9,9,433,0,3))
ciscoCFSDiscoveryCompleteNotif.setObjects(*((_A,_q),(_A,_r)))
if mibBuilder.loadTexts:ciscoCFSDiscoveryCompleteNotif.setStatus(_B)
cfsFeatureActionNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,433,2,2,4))
cfsFeatureActionNotifGroup.setObjects((_A,_AR))
if mibBuilder.loadTexts:cfsFeatureActionNotifGroup.setStatus(_B)
cfsMergeFailNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,433,2,2,5))
cfsMergeFailNotifGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:cfsMergeFailNotifGroup.setStatus(_B)
cfsPeerDiscoveryNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,433,2,2,8))
cfsPeerDiscoveryNotifGroup.setObjects((_A,_AT))
if mibBuilder.loadTexts:cfsPeerDiscoveryNotifGroup.setStatus(_B)
ciscoCFSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,433,2,1,1))
ciscoCFSMIBCompliance.setObjects(*((_A,_AU),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoCFSMIBCompliance.setStatus(_I)
ciscoCFSMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,433,2,1,2))
ciscoCFSMIBComplianceRev1.setObjects(*((_A,_AV),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_w),(_A,_P),(_A,_Q),(_A,_b)))
if mibBuilder.loadTexts:ciscoCFSMIBComplianceRev1.setStatus(_I)
ciscoCFSMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,433,2,1,3))
ciscoCFSMIBComplianceRev2.setObjects(*((_A,_x),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_w),(_A,_P),(_A,_Q),(_A,_b),(_A,_y)))
if mibBuilder.loadTexts:ciscoCFSMIBComplianceRev2.setStatus(_I)
ciscoCFSMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,433,2,1,4))
ciscoCFSMIBComplianceRev3.setObjects(*((_A,_x),(_A,_N),(_A,_O),(_A,_Z),(_A,_a),(_A,_AW),(_A,_P),(_A,_Q),(_A,_b),(_A,_y)))
if mibBuilder.loadTexts:ciscoCFSMIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoCFSAction':CiscoCFSAction,'CiscoCFSFeatureStatus':CiscoCFSFeatureStatus,'CiscoCFSFeatureActionResult':CiscoCFSFeatureActionResult,_A0:CiscoCFSScopeType,_G:CiscoCFSScopeValue,'ciscoCFSMIB':ciscoCFSMIB,'ciscoCFSMIBNotifs':ciscoCFSMIBNotifs,_AR:ciscoCFSFeatureActionNotif,_AS:ciscoCFSMergeFailNotif,_AT:ciscoCFSDiscoveryCompleteNotif,'ciscoCFSMIBObjects':ciscoCFSMIBObjects,'cfsFeature':cfsFeature,'cfsFeatureOpTable':cfsFeatureOpTable,'cfsFeatureOpEntry':cfsFeatureOpEntry,_H:cfsFeatureOpName,_T:cfsFeatureOpAction,_U:cfsFeatureOpScopeType,_V:cfsFeatureOpScopeVal,_J:cfsFeatureOpLastAction,_K:cfsFeatureOpLastScopeType,_L:cfsFeatureOpLastScopeVal,_M:cfsFeatureOpLastActionResult,_W:cfsFeatureOpLastFailureReason,_AE:cfsFeatureOpShowCfgOption,_X:cfsFeatureOpStatus,_AP:cfsFeatureOpAttribs,'cfsPendingConfOwnerTable':cfsPendingConfOwnerTable,'cfsPendingConfOwnerEntry':cfsPendingConfOwnerEntry,_A3:cfsPendingConfOwnerScopeType,_A4:cfsPendingConfOwnerScopeVal,_AF:cfsPendingConfOwnerAddrType,_AG:cfsPendingConfOwnerAddr,_AH:cfsPendingConfOwnerIDType,_AI:cfsPendingConfOwnerID,'cfsMergeStatusTable':cfsMergeStatusTable,'cfsMergeStatusEntry':cfsMergeStatusEntry,_i:cfsMergeStatusScopeType,_j:cfsMergeStatusScopeVal,_Y:cfsMergeStatusValue,'cfsMergeMembersTable':cfsMergeMembersTable,'cfsMergeMembersEntry':cfsMergeMembersEntry,_A5:cfsMergeMemberAddrType,_A6:cfsMergeMemberAddr,_AJ:cfsMergeMemberFabricType,_AK:cfsMergeMemberRole,'cfsPeersTable':cfsPeersTable,'cfsPeersEntry':cfsPeersEntry,_A7:cfsPeerAddrType,_k:cfsPeerAddr,'cfsFeaturePeersTable':cfsFeaturePeersTable,'cfsFeaturePeersEntry':cfsFeaturePeersEntry,_A8:cfsFeaturePeersScopeType,_A9:cfsFeaturePeersScopeVal,_AA:cfsFeaturePeersAddrType,_l:cfsFeaturePeersAddr,'cfsFeatureOpExtTable':cfsFeatureOpExtTable,'cfsFeatureOpExtEntry':cfsFeatureOpExtEntry,_AB:cfsFeatureOpExtScopeType,_AC:cfsFeatureOpExtScopeVal,_s:cfsFeatureOpExtLastAction,_t:cfsFeatureOpExtLastActionResult,_u:cfsFeatureOpExtLastFailureReason,_v:cfsFeatureOpExtShowCfgOption,_AQ:cfsFeatureOpExtLastActionTime,'cfsNotifObjects':cfsNotifObjects,_m:cfsMergeFailFeatureName,_n:cfsMergeFailScopeType,_o:cfsMergeFailScopeVal,_p:cfsMergeFailReasonDescription,'cfsDiscoveryObjects':cfsDiscoveryObjects,_AL:cfsStartPeersDiscovery,_q:cfsPeersDiscoveryResult,_r:cfsPeersDiscoveryFailureReason,'cfsDistCtrlObjects':cfsDistCtrlObjects,_AM:cfsDistCtrl,'cfsDistCtrlTable':cfsDistCtrlTable,'cfsDistCtrlEntry':cfsDistCtrlEntry,_AD:cfsDistCtrlAddrType,_AN:cfsDistCtrlAddr,_AO:cfsDistCtrlAction,'ciscoCFSMIBConformance':ciscoCFSMIBConformance,'ciscoCFSMIBCompliances':ciscoCFSMIBCompliances,'ciscoCFSMIBCompliance':ciscoCFSMIBCompliance,'ciscoCFSMIBComplianceRev1':ciscoCFSMIBComplianceRev1,'ciscoCFSMIBComplianceRev2':ciscoCFSMIBComplianceRev2,'ciscoCFSMIBComplianceRev3':ciscoCFSMIBComplianceRev3,'ciscoCFSMIBGroups':ciscoCFSMIBGroups,_AU:cfsFeatureOpGroup,_N:cfsPendingConfOwnerGroup,_P:cfsFeatureNotifObjectsGroup,_O:cfsFeatureActionNotifGroup,_Q:cfsMergeFailNotifGroup,_Z:cfsMembersGroup,_w:cfsFeatureOpExtGroup,_a:cfsPeerDiscoveryNotifGroup,_AV:cfsFeatureOpGroupRev1,_b:cfsDistCtrlGroup,_y:cfsDistCtrlInetGroup,_x:cfsFeatureOpGroupRev2,_AW:cfsFeatureOpExtGroupRev1})