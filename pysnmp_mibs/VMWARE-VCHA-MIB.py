_f='vmwVchaNotificationGroup'
_e='vmwVchaNotificationInfoGroup'
_d='vmwVchaFileReplicationStateChanged'
_c='vmwVchaDbReplicationStateChanged'
_b='vmwVchaContinueAsActive'
_a='vmwVchaFailoverFailedPassiveNotReady'
_Z='vmwVchaFailoverFailedNodeLost'
_Y='vmwVchaFailoverFailedDisabledMode'
_X='vmwVchaFailoverSucceeded'
_W='vmwVchaFailoverTriggered'
_V='vmwVchaPublicIpDown'
_U='vmwVchaPublicIpUp'
_T='vmwVchaClusterModeChanged'
_S='vmwVchaClusterStateChanged'
_R='vmwVchaNodeIsolated'
_Q='vmwVchaNodeLeft'
_P='vmwVchaNodeJoined'
_O='vmwVchaFileReplicationProvider'
_N='vmwVchaIsFileProviderInSync'
_M='vmwVchaDbReplicationState'
_L='vmwVchaIsPlannedFailover'
_K='vmwVchaClusterMode'
_J='vmwVchaClusterState'
_I='vmwVchaPublicAddressType'
_H='vmwVchaPublicAddressAddr'
_G='vmwVchaTargetNodeRole'
_F='vmwVchaPrivateAddressType'
_E='vmwVchaPrivateAddressAddr'
_D='accessible-for-notify'
_C='vmwVchaInstanceUuid'
_B='current'
_A='VMWARE-VCHA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
vmwVCHA,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwVCHA')
vmwVchaMIB=ModuleIdentity((1,3,6,1,4,1,6876,53,1))
if mibBuilder.loadTexts:vmwVchaMIB.setRevisions(('2016-07-19 00:00','2016-04-06 00:00','2016-02-03 00:00','2016-01-27 00:00','2016-01-15 00:00','2016-01-04 00:00'))
class VmwVchaNodeRoleType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('passive',2),('witness',3),('unknown',4)))
class VmwVchaClusterModeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('maintenance',3)))
class VmwVchaClusterStateType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('healthy',1),('degraded',2),('isolated',3)))
class VmwVchaDbReplicationStateType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*(('noReplication',1),('sync',3),('async',4)))
class VmwVchaFileReplicationProviderType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('serviceConfig',1),('serviceState',2)))
_VmwVCHANotifications_ObjectIdentity=ObjectIdentity
vmwVCHANotifications=_VmwVCHANotifications_ObjectIdentity((1,3,6,1,4,1,6876,53,0))
_VmwVchaMIBConformance_ObjectIdentity=ObjectIdentity
vmwVchaMIBConformance=_VmwVchaMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,53,1,2))
_VmwVchaMIBCompliances_ObjectIdentity=ObjectIdentity
vmwVchaMIBCompliances=_VmwVchaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,53,1,2,1))
_VmwVchaMIBGroups_ObjectIdentity=ObjectIdentity
vmwVchaMIBGroups=_VmwVchaMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,53,1,2,2))
_VmwVchaInstanceUuid_Type=OctetString
_VmwVchaInstanceUuid_Object=MibScalar
vmwVchaInstanceUuid=_VmwVchaInstanceUuid_Object((1,3,6,1,4,1,6876,53,5),_VmwVchaInstanceUuid_Type())
vmwVchaInstanceUuid.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaInstanceUuid.setStatus(_B)
_VmwVchaPrivateAddressType_Type=InetAddressType
_VmwVchaPrivateAddressType_Object=MibScalar
vmwVchaPrivateAddressType=_VmwVchaPrivateAddressType_Object((1,3,6,1,4,1,6876,53,11),_VmwVchaPrivateAddressType_Type())
vmwVchaPrivateAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaPrivateAddressType.setStatus(_B)
_VmwVchaPublicAddressType_Type=InetAddressType
_VmwVchaPublicAddressType_Object=MibScalar
vmwVchaPublicAddressType=_VmwVchaPublicAddressType_Object((1,3,6,1,4,1,6876,53,12),_VmwVchaPublicAddressType_Type())
vmwVchaPublicAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaPublicAddressType.setStatus(_B)
_VmwVchaPrivateAddressAddr_Type=InetAddress
_VmwVchaPrivateAddressAddr_Object=MibScalar
vmwVchaPrivateAddressAddr=_VmwVchaPrivateAddressAddr_Object((1,3,6,1,4,1,6876,53,15),_VmwVchaPrivateAddressAddr_Type())
vmwVchaPrivateAddressAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaPrivateAddressAddr.setStatus(_B)
_VmwVchaPublicAddressAddr_Type=InetAddress
_VmwVchaPublicAddressAddr_Object=MibScalar
vmwVchaPublicAddressAddr=_VmwVchaPublicAddressAddr_Object((1,3,6,1,4,1,6876,53,16),_VmwVchaPublicAddressAddr_Type())
vmwVchaPublicAddressAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaPublicAddressAddr.setStatus(_B)
_VmwVchaTargetNodeRole_Type=VmwVchaNodeRoleType
_VmwVchaTargetNodeRole_Object=MibScalar
vmwVchaTargetNodeRole=_VmwVchaTargetNodeRole_Object((1,3,6,1,4,1,6876,53,20),_VmwVchaTargetNodeRole_Type())
vmwVchaTargetNodeRole.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaTargetNodeRole.setStatus(_B)
_VmwVchaClusterState_Type=VmwVchaClusterStateType
_VmwVchaClusterState_Object=MibScalar
vmwVchaClusterState=_VmwVchaClusterState_Object((1,3,6,1,4,1,6876,53,25),_VmwVchaClusterState_Type())
vmwVchaClusterState.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaClusterState.setStatus(_B)
_VmwVchaClusterMode_Type=VmwVchaClusterModeType
_VmwVchaClusterMode_Object=MibScalar
vmwVchaClusterMode=_VmwVchaClusterMode_Object((1,3,6,1,4,1,6876,53,30),_VmwVchaClusterMode_Type())
vmwVchaClusterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaClusterMode.setStatus(_B)
_VmwVchaIsPlannedFailover_Type=TruthValue
_VmwVchaIsPlannedFailover_Object=MibScalar
vmwVchaIsPlannedFailover=_VmwVchaIsPlannedFailover_Object((1,3,6,1,4,1,6876,53,40),_VmwVchaIsPlannedFailover_Type())
vmwVchaIsPlannedFailover.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaIsPlannedFailover.setStatus(_B)
_VmwVchaDbReplicationState_Type=VmwVchaDbReplicationStateType
_VmwVchaDbReplicationState_Object=MibScalar
vmwVchaDbReplicationState=_VmwVchaDbReplicationState_Object((1,3,6,1,4,1,6876,53,50),_VmwVchaDbReplicationState_Type())
vmwVchaDbReplicationState.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaDbReplicationState.setStatus(_B)
_VmwVchaIsFileProviderInSync_Type=TruthValue
_VmwVchaIsFileProviderInSync_Object=MibScalar
vmwVchaIsFileProviderInSync=_VmwVchaIsFileProviderInSync_Object((1,3,6,1,4,1,6876,53,55),_VmwVchaIsFileProviderInSync_Type())
vmwVchaIsFileProviderInSync.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaIsFileProviderInSync.setStatus(_B)
_VmwVchaFileReplicationProvider_Type=VmwVchaFileReplicationProviderType
_VmwVchaFileReplicationProvider_Object=MibScalar
vmwVchaFileReplicationProvider=_VmwVchaFileReplicationProvider_Object((1,3,6,1,4,1,6876,53,60),_VmwVchaFileReplicationProvider_Type())
vmwVchaFileReplicationProvider.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwVchaFileReplicationProvider.setStatus(_B)
_VmwVchaActive_ObjectIdentity=ObjectIdentity
vmwVchaActive=_VmwVchaActive_ObjectIdentity((1,3,6,1,4,1,6876,53,250))
_VmwVchaPassive_ObjectIdentity=ObjectIdentity
vmwVchaPassive=_VmwVchaPassive_ObjectIdentity((1,3,6,1,4,1,6876,53,255))
_VmwVchaWitness_ObjectIdentity=ObjectIdentity
vmwVchaWitness=_VmwVchaWitness_ObjectIdentity((1,3,6,1,4,1,6876,53,260))
vmwVchaNotificationInfoGroup=ObjectGroup((1,3,6,1,4,1,6876,53,1,2,2,1))
vmwVchaNotificationInfoGroup.setObjects(*((_A,_C),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:vmwVchaNotificationInfoGroup.setStatus(_B)
vmwVchaNodeJoined=NotificationType((1,3,6,1,4,1,6876,53,0,100))
vmwVchaNodeJoined.setObjects(*((_A,_C),(_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:vmwVchaNodeJoined.setStatus(_B)
vmwVchaNodeLeft=NotificationType((1,3,6,1,4,1,6876,53,0,105))
vmwVchaNodeLeft.setObjects(*((_A,_C),(_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:vmwVchaNodeLeft.setStatus(_B)
vmwVchaNodeIsolated=NotificationType((1,3,6,1,4,1,6876,53,0,110))
vmwVchaNodeIsolated.setObjects(*((_A,_C),(_A,_F),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:vmwVchaNodeIsolated.setStatus(_B)
vmwVchaClusterStateChanged=NotificationType((1,3,6,1,4,1,6876,53,0,130))
vmwVchaClusterStateChanged.setObjects(*((_A,_C),(_A,_J)))
if mibBuilder.loadTexts:vmwVchaClusterStateChanged.setStatus(_B)
vmwVchaClusterModeChanged=NotificationType((1,3,6,1,4,1,6876,53,0,150))
vmwVchaClusterModeChanged.setObjects(*((_A,_C),(_A,_K)))
if mibBuilder.loadTexts:vmwVchaClusterModeChanged.setStatus(_B)
vmwVchaPublicIpUp=NotificationType((1,3,6,1,4,1,6876,53,0,205))
vmwVchaPublicIpUp.setObjects(*((_A,_C),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:vmwVchaPublicIpUp.setStatus(_B)
vmwVchaPublicIpDown=NotificationType((1,3,6,1,4,1,6876,53,0,206))
vmwVchaPublicIpDown.setObjects(*((_A,_C),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:vmwVchaPublicIpDown.setStatus(_B)
vmwVchaFailoverTriggered=NotificationType((1,3,6,1,4,1,6876,53,0,210))
vmwVchaFailoverTriggered.setObjects(*((_A,_C),(_A,_L)))
if mibBuilder.loadTexts:vmwVchaFailoverTriggered.setStatus(_B)
vmwVchaFailoverSucceeded=NotificationType((1,3,6,1,4,1,6876,53,0,220))
vmwVchaFailoverSucceeded.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwVchaFailoverSucceeded.setStatus(_B)
vmwVchaFailoverFailedDisabledMode=NotificationType((1,3,6,1,4,1,6876,53,0,225))
vmwVchaFailoverFailedDisabledMode.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwVchaFailoverFailedDisabledMode.setStatus(_B)
vmwVchaFailoverFailedNodeLost=NotificationType((1,3,6,1,4,1,6876,53,0,226))
vmwVchaFailoverFailedNodeLost.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwVchaFailoverFailedNodeLost.setStatus(_B)
vmwVchaFailoverFailedPassiveNotReady=NotificationType((1,3,6,1,4,1,6876,53,0,227))
vmwVchaFailoverFailedPassiveNotReady.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwVchaFailoverFailedPassiveNotReady.setStatus(_B)
vmwVchaContinueAsActive=NotificationType((1,3,6,1,4,1,6876,53,0,230))
vmwVchaContinueAsActive.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwVchaContinueAsActive.setStatus(_B)
vmwVchaDbReplicationStateChanged=NotificationType((1,3,6,1,4,1,6876,53,0,300))
vmwVchaDbReplicationStateChanged.setObjects(*((_A,_C),(_A,_M)))
if mibBuilder.loadTexts:vmwVchaDbReplicationStateChanged.setStatus(_B)
vmwVchaFileReplicationStateChanged=NotificationType((1,3,6,1,4,1,6876,53,0,350))
vmwVchaFileReplicationStateChanged.setObjects(*((_A,_C),(_A,_O),(_A,_N)))
if mibBuilder.loadTexts:vmwVchaFileReplicationStateChanged.setStatus(_B)
vmwVchaNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,53,1,2,2,2))
vmwVchaNotificationGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:vmwVchaNotificationGroup.setStatus(_B)
vmwVchaMIBBasicComplianceRev2=ModuleCompliance((1,3,6,1,4,1,6876,53,1,2,1,3))
vmwVchaMIBBasicComplianceRev2.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:vmwVchaMIBBasicComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VmwVchaNodeRoleType':VmwVchaNodeRoleType,'VmwVchaClusterModeType':VmwVchaClusterModeType,'VmwVchaClusterStateType':VmwVchaClusterStateType,'VmwVchaDbReplicationStateType':VmwVchaDbReplicationStateType,'VmwVchaFileReplicationProviderType':VmwVchaFileReplicationProviderType,'vmwVCHANotifications':vmwVCHANotifications,_P:vmwVchaNodeJoined,_Q:vmwVchaNodeLeft,_R:vmwVchaNodeIsolated,_S:vmwVchaClusterStateChanged,_T:vmwVchaClusterModeChanged,_U:vmwVchaPublicIpUp,_V:vmwVchaPublicIpDown,_W:vmwVchaFailoverTriggered,_X:vmwVchaFailoverSucceeded,_Y:vmwVchaFailoverFailedDisabledMode,_Z:vmwVchaFailoverFailedNodeLost,_a:vmwVchaFailoverFailedPassiveNotReady,_b:vmwVchaContinueAsActive,_c:vmwVchaDbReplicationStateChanged,_d:vmwVchaFileReplicationStateChanged,'vmwVchaMIB':vmwVchaMIB,'vmwVchaMIBConformance':vmwVchaMIBConformance,'vmwVchaMIBCompliances':vmwVchaMIBCompliances,'vmwVchaMIBBasicComplianceRev2':vmwVchaMIBBasicComplianceRev2,'vmwVchaMIBGroups':vmwVchaMIBGroups,_e:vmwVchaNotificationInfoGroup,_f:vmwVchaNotificationGroup,_C:vmwVchaInstanceUuid,_F:vmwVchaPrivateAddressType,_I:vmwVchaPublicAddressType,_E:vmwVchaPrivateAddressAddr,_H:vmwVchaPublicAddressAddr,_G:vmwVchaTargetNodeRole,_J:vmwVchaClusterState,_K:vmwVchaClusterMode,_L:vmwVchaIsPlannedFailover,_M:vmwVchaDbReplicationState,_N:vmwVchaIsFileProviderInSync,_O:vmwVchaFileReplicationProvider,'vmwVchaActive':vmwVchaActive,'vmwVchaPassive':vmwVchaPassive,'vmwVchaWitness':vmwVchaWitness})