_e='atAtmfControllerAreaStatus'
_d='atAtmfTrapRemoteServersAvailable'
_c='atAtmfTrapRemoteServerStatus'
_b='atAtmfTrapRemoteBackupServerName'
_a='atAtmfTrapRemoteBackupServerId'
_Z='atAtmfTrapRollingRebootReleaseStatus'
_Y='atAtmfTrapRollingRebootReleaseName'
_X='atAtmfTrapMediaFree'
_W='atAtmfTrapMediaTotal'
_V='atAtmfTrapMediaType'
_U='atAtmfTrapInterfaceStatusChange'
_T='atAtmfTrapInterfaceName'
_S='atAtmfTrapNodeRecoveryStatus'
_R='atAtmfTrapNetworkName'
_Q='atAtmfTrapNodeStatusChange'
_P='atAtmfControllerAreaId'
_O='atAtmfNodeName'
_N='enabled'
_M='disabled'
_L='atAtmfControllerAreaName'
_K='atAtmfTrapRollingRebootStatus'
_J='atAtmfTrapBackupStatus'
_I='passed'
_H='failed'
_G='atAtmfTrapMasterNodeName'
_F='atAtmfTrapNodeName'
_E='Integer32'
_D='DisplayStringUnsized'
_C='read-only'
_B='AT-ATMF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_D,'modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atmf=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,603))
if mibBuilder.loadTexts:atmf.setRevisions(('2014-10-07 12:00','2014-07-04 12:00','2014-05-07 12:00','2013-07-15 12:00','2013-05-27 12:00'))
_AtAtmfTraps_ObjectIdentity=ObjectIdentity
atAtmfTraps=_AtAtmfTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,603,0))
_AtAtmfTrapVariable_ObjectIdentity=ObjectIdentity
atAtmfTrapVariable=_AtAtmfTrapVariable_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,603,1))
class _AtAtmfTrapNodeName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AtAtmfTrapNodeName_Type.__name__=_D
_AtAtmfTrapNodeName_Object=MibScalar
atAtmfTrapNodeName=_AtAtmfTrapNodeName_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,1),_AtAtmfTrapNodeName_Type())
atAtmfTrapNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapNodeName.setStatus(_A)
class _AtAtmfTrapMasterNodeName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AtAtmfTrapMasterNodeName_Type.__name__=_D
_AtAtmfTrapMasterNodeName_Object=MibScalar
atAtmfTrapMasterNodeName=_AtAtmfTrapMasterNodeName_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,2),_AtAtmfTrapMasterNodeName_Type())
atAtmfTrapMasterNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapMasterNodeName.setStatus(_A)
class _AtAtmfTrapNetworkName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtAtmfTrapNetworkName_Type.__name__=_D
_AtAtmfTrapNetworkName_Object=MibScalar
atAtmfTrapNetworkName=_AtAtmfTrapNetworkName_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,3),_AtAtmfTrapNetworkName_Type())
atAtmfTrapNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapNetworkName.setStatus(_A)
class _AtAtmfTrapInterfaceName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AtAtmfTrapInterfaceName_Type.__name__=_D
_AtAtmfTrapInterfaceName_Object=MibScalar
atAtmfTrapInterfaceName=_AtAtmfTrapInterfaceName_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,4),_AtAtmfTrapInterfaceName_Type())
atAtmfTrapInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapInterfaceName.setStatus(_A)
class _AtAtmfTrapBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtAtmfTrapBackupStatus_Type.__name__=_E
_AtAtmfTrapBackupStatus_Object=MibScalar
atAtmfTrapBackupStatus=_AtAtmfTrapBackupStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,5),_AtAtmfTrapBackupStatus_Type())
atAtmfTrapBackupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapBackupStatus.setStatus(_A)
class _AtAtmfTrapNodeStatusChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('left',1),('joined',2)))
_AtAtmfTrapNodeStatusChange_Type.__name__=_E
_AtAtmfTrapNodeStatusChange_Object=MibScalar
atAtmfTrapNodeStatusChange=_AtAtmfTrapNodeStatusChange_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,6),_AtAtmfTrapNodeStatusChange_Type())
atAtmfTrapNodeStatusChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapNodeStatusChange.setStatus(_A)
class _AtAtmfTrapInterfaceStatusChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blocking',1),('forwarding',2)))
_AtAtmfTrapInterfaceStatusChange_Type.__name__=_E
_AtAtmfTrapInterfaceStatusChange_Object=MibScalar
atAtmfTrapInterfaceStatusChange=_AtAtmfTrapInterfaceStatusChange_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,7),_AtAtmfTrapInterfaceStatusChange_Type())
atAtmfTrapInterfaceStatusChange.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapInterfaceStatusChange.setStatus(_A)
class _AtAtmfTrapNodeRecoveryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtAtmfTrapNodeRecoveryStatus_Type.__name__=_E
_AtAtmfTrapNodeRecoveryStatus_Object=MibScalar
atAtmfTrapNodeRecoveryStatus=_AtAtmfTrapNodeRecoveryStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,8),_AtAtmfTrapNodeRecoveryStatus_Type())
atAtmfTrapNodeRecoveryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapNodeRecoveryStatus.setStatus(_A)
class _AtAtmfTrapMediaType_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_AtAtmfTrapMediaType_Type.__name__=_D
_AtAtmfTrapMediaType_Object=MibScalar
atAtmfTrapMediaType=_AtAtmfTrapMediaType_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,9),_AtAtmfTrapMediaType_Type())
atAtmfTrapMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapMediaType.setStatus(_A)
_AtAtmfTrapMediaTotal_Type=Integer32
_AtAtmfTrapMediaTotal_Object=MibScalar
atAtmfTrapMediaTotal=_AtAtmfTrapMediaTotal_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,10),_AtAtmfTrapMediaTotal_Type())
atAtmfTrapMediaTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapMediaTotal.setStatus(_A)
_AtAtmfTrapMediaFree_Type=Integer32
_AtAtmfTrapMediaFree_Object=MibScalar
atAtmfTrapMediaFree=_AtAtmfTrapMediaFree_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,11),_AtAtmfTrapMediaFree_Type())
atAtmfTrapMediaFree.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapMediaFree.setStatus(_A)
class _AtAtmfTrapRollingRebootStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtAtmfTrapRollingRebootStatus_Type.__name__=_E
_AtAtmfTrapRollingRebootStatus_Object=MibScalar
atAtmfTrapRollingRebootStatus=_AtAtmfTrapRollingRebootStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,12),_AtAtmfTrapRollingRebootStatus_Type())
atAtmfTrapRollingRebootStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRollingRebootStatus.setStatus(_A)
class _AtAtmfTrapRollingRebootReleaseName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AtAtmfTrapRollingRebootReleaseName_Type.__name__=_D
_AtAtmfTrapRollingRebootReleaseName_Object=MibScalar
atAtmfTrapRollingRebootReleaseName=_AtAtmfTrapRollingRebootReleaseName_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,13),_AtAtmfTrapRollingRebootReleaseName_Type())
atAtmfTrapRollingRebootReleaseName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRollingRebootReleaseName.setStatus(_A)
class _AtAtmfTrapRollingRebootReleaseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AtAtmfTrapRollingRebootReleaseStatus_Type.__name__=_E
_AtAtmfTrapRollingRebootReleaseStatus_Object=MibScalar
atAtmfTrapRollingRebootReleaseStatus=_AtAtmfTrapRollingRebootReleaseStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,14),_AtAtmfTrapRollingRebootReleaseStatus_Type())
atAtmfTrapRollingRebootReleaseStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRollingRebootReleaseStatus.setStatus(_A)
_AtAtmfTrapRemoteBackupServerId_Type=Integer32
_AtAtmfTrapRemoteBackupServerId_Object=MibScalar
atAtmfTrapRemoteBackupServerId=_AtAtmfTrapRemoteBackupServerId_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,15),_AtAtmfTrapRemoteBackupServerId_Type())
atAtmfTrapRemoteBackupServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRemoteBackupServerId.setStatus(_A)
class _AtAtmfTrapRemoteBackupServerName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AtAtmfTrapRemoteBackupServerName_Type.__name__=_D
_AtAtmfTrapRemoteBackupServerName_Object=MibScalar
atAtmfTrapRemoteBackupServerName=_AtAtmfTrapRemoteBackupServerName_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,16),_AtAtmfTrapRemoteBackupServerName_Type())
atAtmfTrapRemoteBackupServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRemoteBackupServerName.setStatus(_A)
class _AtAtmfTrapRemoteServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unavailable',1),('available',2)))
_AtAtmfTrapRemoteServerStatus_Type.__name__=_E
_AtAtmfTrapRemoteServerStatus_Object=MibScalar
atAtmfTrapRemoteServerStatus=_AtAtmfTrapRemoteServerStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,17),_AtAtmfTrapRemoteServerStatus_Type())
atAtmfTrapRemoteServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRemoteServerStatus.setStatus(_A)
_AtAtmfTrapRemoteServersAvailable_Type=Integer32
_AtAtmfTrapRemoteServersAvailable_Object=MibScalar
atAtmfTrapRemoteServersAvailable=_AtAtmfTrapRemoteServersAvailable_Object((1,3,6,1,4,1,207,8,4,4,4,603,1,18),_AtAtmfTrapRemoteServersAvailable_Type())
atAtmfTrapRemoteServersAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfTrapRemoteServersAvailable.setStatus(_A)
_AtAtmfSummary_ObjectIdentity=ObjectIdentity
atAtmfSummary=_AtAtmfSummary_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,603,2))
class _AtAtmfSummaryNodeName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AtAtmfSummaryNodeName_Type.__name__=_D
_AtAtmfSummaryNodeName_Object=MibScalar
atAtmfSummaryNodeName=_AtAtmfSummaryNodeName_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,1),_AtAtmfSummaryNodeName_Type())
atAtmfSummaryNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryNodeName.setStatus(_A)
class _AtAtmfSummaryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_AtAtmfSummaryStatus_Type.__name__=_E
_AtAtmfSummaryStatus_Object=MibScalar
atAtmfSummaryStatus=_AtAtmfSummaryStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,2),_AtAtmfSummaryStatus_Type())
atAtmfSummaryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryStatus.setStatus(_A)
class _AtAtmfSummaryRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('member',1),('master',2)))
_AtAtmfSummaryRole_Type.__name__=_E
_AtAtmfSummaryRole_Object=MibScalar
atAtmfSummaryRole=_AtAtmfSummaryRole_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,3),_AtAtmfSummaryRole_Type())
atAtmfSummaryRole.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryRole.setStatus(_A)
class _AtAtmfSummaryNetworkName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AtAtmfSummaryNetworkName_Type.__name__=_D
_AtAtmfSummaryNetworkName_Object=MibScalar
atAtmfSummaryNetworkName=_AtAtmfSummaryNetworkName_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,4),_AtAtmfSummaryNetworkName_Type())
atAtmfSummaryNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryNetworkName.setStatus(_A)
class _AtAtmfSummaryParentName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AtAtmfSummaryParentName_Type.__name__=_D
_AtAtmfSummaryParentName_Object=MibScalar
atAtmfSummaryParentName=_AtAtmfSummaryParentName_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,5),_AtAtmfSummaryParentName_Type())
atAtmfSummaryParentName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryParentName.setStatus(_A)
_AtAtmfSummaryCoreDistance_Type=Integer32
_AtAtmfSummaryCoreDistance_Object=MibScalar
atAtmfSummaryCoreDistance=_AtAtmfSummaryCoreDistance_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,6),_AtAtmfSummaryCoreDistance_Type())
atAtmfSummaryCoreDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryCoreDistance.setStatus(_A)
_AtAtmfSummaryDomainId_Type=Integer32
_AtAtmfSummaryDomainId_Object=MibScalar
atAtmfSummaryDomainId=_AtAtmfSummaryDomainId_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,7),_AtAtmfSummaryDomainId_Type())
atAtmfSummaryDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryDomainId.setStatus(_A)
class _AtAtmfSummaryRestrictedLogin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_AtAtmfSummaryRestrictedLogin_Type.__name__=_E
_AtAtmfSummaryRestrictedLogin_Object=MibScalar
atAtmfSummaryRestrictedLogin=_AtAtmfSummaryRestrictedLogin_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,8),_AtAtmfSummaryRestrictedLogin_Type())
atAtmfSummaryRestrictedLogin.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryRestrictedLogin.setStatus(_A)
_AtAtmfSummaryNodes_Type=Integer32
_AtAtmfSummaryNodes_Object=MibScalar
atAtmfSummaryNodes=_AtAtmfSummaryNodes_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,9),_AtAtmfSummaryNodes_Type())
atAtmfSummaryNodes.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryNodes.setStatus(_A)
class _AtAtmfSummaryAreaName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtAtmfSummaryAreaName_Type.__name__=_D
_AtAtmfSummaryAreaName_Object=MibScalar
atAtmfSummaryAreaName=_AtAtmfSummaryAreaName_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,10),_AtAtmfSummaryAreaName_Type())
atAtmfSummaryAreaName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryAreaName.setStatus(_A)
class _AtAtmfSummaryControllerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('non-controller',1),('controller',2)))
_AtAtmfSummaryControllerRole_Type.__name__=_E
_AtAtmfSummaryControllerRole_Object=MibScalar
atAtmfSummaryControllerRole=_AtAtmfSummaryControllerRole_Object((1,3,6,1,4,1,207,8,4,4,4,603,2,11),_AtAtmfSummaryControllerRole_Type())
atAtmfSummaryControllerRole.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfSummaryControllerRole.setStatus(_A)
_AtAtmfNodeTable_Object=MibTable
atAtmfNodeTable=_AtAtmfNodeTable_Object((1,3,6,1,4,1,207,8,4,4,4,603,3))
if mibBuilder.loadTexts:atAtmfNodeTable.setStatus(_A)
_AtAtmfNodeEntry_Object=MibTableRow
atAtmfNodeEntry=_AtAtmfNodeEntry_Object((1,3,6,1,4,1,207,8,4,4,4,603,3,1))
atAtmfNodeEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:atAtmfNodeEntry.setStatus(_A)
class _AtAtmfNodeName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AtAtmfNodeName_Type.__name__=_D
_AtAtmfNodeName_Object=MibTableColumn
atAtmfNodeName=_AtAtmfNodeName_Object((1,3,6,1,4,1,207,8,4,4,4,603,3,1,1),_AtAtmfNodeName_Type())
atAtmfNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfNodeName.setStatus(_A)
_AtAtmfControllerAreaTable_Object=MibTable
atAtmfControllerAreaTable=_AtAtmfControllerAreaTable_Object((1,3,6,1,4,1,207,8,4,4,4,603,4))
if mibBuilder.loadTexts:atAtmfControllerAreaTable.setStatus(_A)
_AtAtmfControllerAreaEntry_Object=MibTableRow
atAtmfControllerAreaEntry=_AtAtmfControllerAreaEntry_Object((1,3,6,1,4,1,207,8,4,4,4,603,4,1))
atAtmfControllerAreaEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:atAtmfControllerAreaEntry.setStatus(_A)
class _AtAtmfControllerAreaId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,126))
_AtAtmfControllerAreaId_Type.__name__=_E
_AtAtmfControllerAreaId_Object=MibTableColumn
atAtmfControllerAreaId=_AtAtmfControllerAreaId_Object((1,3,6,1,4,1,207,8,4,4,4,603,4,1,1),_AtAtmfControllerAreaId_Type())
atAtmfControllerAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfControllerAreaId.setStatus(_A)
class _AtAtmfControllerAreaName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtAtmfControllerAreaName_Type.__name__=_D
_AtAtmfControllerAreaName_Object=MibTableColumn
atAtmfControllerAreaName=_AtAtmfControllerAreaName_Object((1,3,6,1,4,1,207,8,4,4,4,603,4,1,2),_AtAtmfControllerAreaName_Type())
atAtmfControllerAreaName.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfControllerAreaName.setStatus(_A)
class _AtAtmfControllerAreaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unreachable',1),('reachable',2)))
_AtAtmfControllerAreaStatus_Type.__name__=_E
_AtAtmfControllerAreaStatus_Object=MibTableColumn
atAtmfControllerAreaStatus=_AtAtmfControllerAreaStatus_Object((1,3,6,1,4,1,207,8,4,4,4,603,4,1,3),_AtAtmfControllerAreaStatus_Type())
atAtmfControllerAreaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfControllerAreaStatus.setStatus(_A)
_AtAtmfControllerAreaMemberCount_Type=Integer32
_AtAtmfControllerAreaMemberCount_Object=MibTableColumn
atAtmfControllerAreaMemberCount=_AtAtmfControllerAreaMemberCount_Object((1,3,6,1,4,1,207,8,4,4,4,603,4,1,4),_AtAtmfControllerAreaMemberCount_Type())
atAtmfControllerAreaMemberCount.setMaxAccess(_C)
if mibBuilder.loadTexts:atAtmfControllerAreaMemberCount.setStatus(_A)
atAtmfBackupStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,1))
atAtmfBackupStatusTrap.setObjects(*((_B,_F),(_B,_G),(_B,_J)))
if mibBuilder.loadTexts:atAtmfBackupStatusTrap.setStatus(_A)
atAtmfNodeStatusChangeTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,2))
atAtmfNodeStatusChangeTrap.setObjects(*((_B,_F),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:atAtmfNodeStatusChangeTrap.setStatus(_A)
atAtmfNodeRecoveryTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,3))
atAtmfNodeRecoveryTrap.setObjects(*((_B,_F),(_B,_G),(_B,_S)))
if mibBuilder.loadTexts:atAtmfNodeRecoveryTrap.setStatus(_A)
atAtmfInterfaceStatusChangeTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,4))
atAtmfInterfaceStatusChangeTrap.setObjects(*((_B,_F),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:atAtmfInterfaceStatusChangeTrap.setStatus(_A)
atAtmfExternalMediaLowMemoryTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,5))
atAtmfExternalMediaLowMemoryTrap.setObjects(*((_B,_G),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:atAtmfExternalMediaLowMemoryTrap.setStatus(_A)
atAtmfRollingRebootCompleteTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,6))
atAtmfRollingRebootCompleteTrap.setObjects(*((_B,_F),(_B,_K)))
if mibBuilder.loadTexts:atAtmfRollingRebootCompleteTrap.setStatus(_A)
atAtmfRollingRebootReleaseCompleteTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,7))
atAtmfRollingRebootReleaseCompleteTrap.setObjects(*((_B,_F),(_B,_K),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:atAtmfRollingRebootReleaseCompleteTrap.setStatus(_A)
atAtmfRemoteBackupStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,8))
atAtmfRemoteBackupStatusTrap.setObjects(*((_B,_F),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:atAtmfRemoteBackupStatusTrap.setStatus(_A)
atAtmfControllerAreaStatusChangeTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,9))
atAtmfControllerAreaStatusChangeTrap.setObjects(*((_B,_F),(_B,_L),(_B,_e)))
if mibBuilder.loadTexts:atAtmfControllerAreaStatusChangeTrap.setStatus(_A)
atAtmfControllerAreaRemoteBackupStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,603,0,10))
atAtmfControllerAreaRemoteBackupStatusTrap.setObjects(*((_B,_F),(_B,_L),(_B,_G),(_B,_J)))
if mibBuilder.loadTexts:atAtmfControllerAreaRemoteBackupStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atmf':atmf,'atAtmfTraps':atAtmfTraps,'atAtmfBackupStatusTrap':atAtmfBackupStatusTrap,'atAtmfNodeStatusChangeTrap':atAtmfNodeStatusChangeTrap,'atAtmfNodeRecoveryTrap':atAtmfNodeRecoveryTrap,'atAtmfInterfaceStatusChangeTrap':atAtmfInterfaceStatusChangeTrap,'atAtmfExternalMediaLowMemoryTrap':atAtmfExternalMediaLowMemoryTrap,'atAtmfRollingRebootCompleteTrap':atAtmfRollingRebootCompleteTrap,'atAtmfRollingRebootReleaseCompleteTrap':atAtmfRollingRebootReleaseCompleteTrap,'atAtmfRemoteBackupStatusTrap':atAtmfRemoteBackupStatusTrap,'atAtmfControllerAreaStatusChangeTrap':atAtmfControllerAreaStatusChangeTrap,'atAtmfControllerAreaRemoteBackupStatusTrap':atAtmfControllerAreaRemoteBackupStatusTrap,'atAtmfTrapVariable':atAtmfTrapVariable,_F:atAtmfTrapNodeName,_G:atAtmfTrapMasterNodeName,_R:atAtmfTrapNetworkName,_T:atAtmfTrapInterfaceName,_J:atAtmfTrapBackupStatus,_Q:atAtmfTrapNodeStatusChange,_U:atAtmfTrapInterfaceStatusChange,_S:atAtmfTrapNodeRecoveryStatus,_V:atAtmfTrapMediaType,_W:atAtmfTrapMediaTotal,_X:atAtmfTrapMediaFree,_K:atAtmfTrapRollingRebootStatus,_Y:atAtmfTrapRollingRebootReleaseName,_Z:atAtmfTrapRollingRebootReleaseStatus,_a:atAtmfTrapRemoteBackupServerId,_b:atAtmfTrapRemoteBackupServerName,_c:atAtmfTrapRemoteServerStatus,_d:atAtmfTrapRemoteServersAvailable,'atAtmfSummary':atAtmfSummary,'atAtmfSummaryNodeName':atAtmfSummaryNodeName,'atAtmfSummaryStatus':atAtmfSummaryStatus,'atAtmfSummaryRole':atAtmfSummaryRole,'atAtmfSummaryNetworkName':atAtmfSummaryNetworkName,'atAtmfSummaryParentName':atAtmfSummaryParentName,'atAtmfSummaryCoreDistance':atAtmfSummaryCoreDistance,'atAtmfSummaryDomainId':atAtmfSummaryDomainId,'atAtmfSummaryRestrictedLogin':atAtmfSummaryRestrictedLogin,'atAtmfSummaryNodes':atAtmfSummaryNodes,'atAtmfSummaryAreaName':atAtmfSummaryAreaName,'atAtmfSummaryControllerRole':atAtmfSummaryControllerRole,'atAtmfNodeTable':atAtmfNodeTable,'atAtmfNodeEntry':atAtmfNodeEntry,_O:atAtmfNodeName,'atAtmfControllerAreaTable':atAtmfControllerAreaTable,'atAtmfControllerAreaEntry':atAtmfControllerAreaEntry,_P:atAtmfControllerAreaId,_L:atAtmfControllerAreaName,_e:atAtmfControllerAreaStatus,'atAtmfControllerAreaMemberCount':atAtmfControllerAreaMemberCount})