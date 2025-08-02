_Q='agentOpenFlowGroupBucketId'
_P='agentOpenFlowBucketGroupId'
_O='agentOpenFlowGroupId'
_N='agentOpenFlowFlowTable'
_M='agentOpenFlowCfgCtrlIPPort'
_L='agentOpenFlowCfgCtrlIPAddress'
_K='obsolete'
_J='disable'
_I='enable'
_H='OctetString'
_G='read-create'
_F='DNOS-OPENFLOW-PRIVATE-MIB'
_E='read-write'
_D='Unsigned32'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
fastPathOpenFlow=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56))
if mibBuilder.loadTexts:fastPathOpenFlow.setRevisions(('2011-03-06 00:00',))
_AgentOpenFlowGroup_ObjectIdentity=ObjectIdentity
agentOpenFlowGroup=_AgentOpenFlowGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1))
_AgentOpenFlowGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentOpenFlowGlobalConfigGroup=_AgentOpenFlowGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1))
class _AgentOpenFlowAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AgentOpenFlowAdminMode_Type.__name__=_C
_AgentOpenFlowAdminMode_Object=MibScalar
agentOpenFlowAdminMode=_AgentOpenFlowAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,1),_AgentOpenFlowAdminMode_Type())
agentOpenFlowAdminMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowAdminMode.setStatus(_A)
class _AgentOpenFlowVariant_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tenantNetworkingMode',1),('openFlow10Mode',2),('openFlow13Mode',3)))
_AgentOpenFlowVariant_Type.__name__=_C
_AgentOpenFlowVariant_Object=MibScalar
agentOpenFlowVariant=_AgentOpenFlowVariant_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,2),_AgentOpenFlowVariant_Type())
agentOpenFlowVariant.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowVariant.setStatus(_A)
class _AgentOpenFlowDefaultTable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullMatch',1),('layerTwoMatch',2)))
_AgentOpenFlowDefaultTable_Type.__name__=_C
_AgentOpenFlowDefaultTable_Object=MibScalar
agentOpenFlowDefaultTable=_AgentOpenFlowDefaultTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,3),_AgentOpenFlowDefaultTable_Type())
agentOpenFlowDefaultTable.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowDefaultTable.setStatus('deprecated')
class _AgentOpenFlowStaticIPAssignmentMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AgentOpenFlowStaticIPAssignmentMode_Type.__name__=_C
_AgentOpenFlowStaticIPAssignmentMode_Object=MibScalar
agentOpenFlowStaticIPAssignmentMode=_AgentOpenFlowStaticIPAssignmentMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,4),_AgentOpenFlowStaticIPAssignmentMode_Type())
agentOpenFlowStaticIPAssignmentMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowStaticIPAssignmentMode.setStatus(_K)
_AgentOpenFlowGlobalConfigIPAddress_Type=IpAddress
_AgentOpenFlowGlobalConfigIPAddress_Object=MibScalar
agentOpenFlowGlobalConfigIPAddress=_AgentOpenFlowGlobalConfigIPAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,5),_AgentOpenFlowGlobalConfigIPAddress_Type())
agentOpenFlowGlobalConfigIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowGlobalConfigIPAddress.setStatus(_A)
class _AgentOpenFlowNetworkMTU_Type(Unsigned32):defaultValue=1518;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9216))
_AgentOpenFlowNetworkMTU_Type.__name__=_D
_AgentOpenFlowNetworkMTU_Object=MibScalar
agentOpenFlowNetworkMTU=_AgentOpenFlowNetworkMTU_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,6),_AgentOpenFlowNetworkMTU_Type())
agentOpenFlowNetworkMTU.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowNetworkMTU.setStatus(_K)
class _AgentOpenFlowIPAssignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('static',1),('serviceport',2)))
_AgentOpenFlowIPAssignmentMode_Type.__name__=_C
_AgentOpenFlowIPAssignmentMode_Object=MibScalar
agentOpenFlowIPAssignmentMode=_AgentOpenFlowIPAssignmentMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,1,7),_AgentOpenFlowIPAssignmentMode_Type())
agentOpenFlowIPAssignmentMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowIPAssignmentMode.setStatus(_A)
_AgentOpenFlowCfgControllerTable_Object=MibTable
agentOpenFlowCfgControllerTable=_AgentOpenFlowCfgControllerTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3))
if mibBuilder.loadTexts:agentOpenFlowCfgControllerTable.setStatus(_A)
_AgentOpenFlowCfgControllerEntry_Object=MibTableRow
agentOpenFlowCfgControllerEntry=_AgentOpenFlowCfgControllerEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3,1))
agentOpenFlowCfgControllerEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:agentOpenFlowCfgControllerEntry.setStatus(_A)
_AgentOpenFlowCfgCtrlIPAddress_Type=IpAddress
_AgentOpenFlowCfgCtrlIPAddress_Object=MibTableColumn
agentOpenFlowCfgCtrlIPAddress=_AgentOpenFlowCfgCtrlIPAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3,1,1),_AgentOpenFlowCfgCtrlIPAddress_Type())
agentOpenFlowCfgCtrlIPAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlIPAddress.setStatus(_A)
class _AgentOpenFlowCfgCtrlIPPort_Type(Unsigned32):defaultValue=6632;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentOpenFlowCfgCtrlIPPort_Type.__name__=_D
_AgentOpenFlowCfgCtrlIPPort_Object=MibTableColumn
agentOpenFlowCfgCtrlIPPort=_AgentOpenFlowCfgCtrlIPPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3,1,2),_AgentOpenFlowCfgCtrlIPPort_Type())
agentOpenFlowCfgCtrlIPPort.setMaxAccess(_G)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlIPPort.setStatus(_A)
class _AgentOpenFlowCfgCtrlConnectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ssl',1),('tcp',2)))
_AgentOpenFlowCfgCtrlConnectionMode_Type.__name__=_C
_AgentOpenFlowCfgCtrlConnectionMode_Object=MibTableColumn
agentOpenFlowCfgCtrlConnectionMode=_AgentOpenFlowCfgCtrlConnectionMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3,1,3),_AgentOpenFlowCfgCtrlConnectionMode_Type())
agentOpenFlowCfgCtrlConnectionMode.setMaxAccess(_G)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlConnectionMode.setStatus(_A)
_AgentOpenFlowCfgCtrlStatus_Type=RowStatus
_AgentOpenFlowCfgCtrlStatus_Object=MibTableColumn
agentOpenFlowCfgCtrlStatus=_AgentOpenFlowCfgCtrlStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3,1,4),_AgentOpenFlowCfgCtrlStatus_Type())
agentOpenFlowCfgCtrlStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlStatus.setStatus(_A)
_AgentOpenFlowCfgCtrlRole_Type=DisplayString
_AgentOpenFlowCfgCtrlRole_Object=MibTableColumn
agentOpenFlowCfgCtrlRole=_AgentOpenFlowCfgCtrlRole_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,3,1,5),_AgentOpenFlowCfgCtrlRole_Type())
agentOpenFlowCfgCtrlRole.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlRole.setStatus(_A)
_AgentOpenFlowGlobalStatusParameters_ObjectIdentity=ObjectIdentity
agentOpenFlowGlobalStatusParameters=_AgentOpenFlowGlobalStatusParameters_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,6))
class _AgentOpenFlowOperationalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),('enablePending',3),('disablePending',4)))
_AgentOpenFlowOperationalStatus_Type.__name__=_C
_AgentOpenFlowOperationalStatus_Object=MibScalar
agentOpenFlowOperationalStatus=_AgentOpenFlowOperationalStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,6,1),_AgentOpenFlowOperationalStatus_Type())
agentOpenFlowOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowOperationalStatus.setStatus(_A)
class _AgentOpenFlowDisableReason_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('administrativelyDisabled',2),('noSuitableIPInterface',3),('noSSLCertificates',4)))
_AgentOpenFlowDisableReason_Type.__name__=_C
_AgentOpenFlowDisableReason_Object=MibScalar
agentOpenFlowDisableReason=_AgentOpenFlowDisableReason_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,6,2),_AgentOpenFlowDisableReason_Type())
agentOpenFlowDisableReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowDisableReason.setStatus(_A)
_AgentOpenFlowGlobalCommands_ObjectIdentity=ObjectIdentity
agentOpenFlowGlobalCommands=_AgentOpenFlowGlobalCommands_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,7))
class _AgentOpenFlowEraseOpenFlowManagerCertificates_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alwaysReturnedOnRead',1),('eraseCertificates',2)))
_AgentOpenFlowEraseOpenFlowManagerCertificates_Type.__name__=_C
_AgentOpenFlowEraseOpenFlowManagerCertificates_Object=MibScalar
agentOpenFlowEraseOpenFlowManagerCertificates=_AgentOpenFlowEraseOpenFlowManagerCertificates_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,7,1),_AgentOpenFlowEraseOpenFlowManagerCertificates_Type())
agentOpenFlowEraseOpenFlowManagerCertificates.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowEraseOpenFlowManagerCertificates.setStatus(_A)
_AgentOpenFlowFlowTableStatusTable_Object=MibTable
agentOpenFlowFlowTableStatusTable=_AgentOpenFlowFlowTableStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8))
if mibBuilder.loadTexts:agentOpenFlowFlowTableStatusTable.setStatus(_A)
_AgentOpenFlowFlowTableStatusEntry_Object=MibTableRow
agentOpenFlowFlowTableStatusEntry=_AgentOpenFlowFlowTableStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1))
agentOpenFlowFlowTableStatusEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:agentOpenFlowFlowTableStatusEntry.setStatus(_A)
class _AgentOpenFlowFlowTable_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowFlowTable_Type.__name__=_D
_AgentOpenFlowFlowTable_Object=MibTableColumn
agentOpenFlowFlowTable=_AgentOpenFlowFlowTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,1),_AgentOpenFlowFlowTable_Type())
agentOpenFlowFlowTable.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowTable.setStatus(_A)
class _AgentOpenFlowFlowTableName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgentOpenFlowFlowTableName_Type.__name__=_H
_AgentOpenFlowFlowTableName_Object=MibTableColumn
agentOpenFlowFlowTableName=_AgentOpenFlowFlowTableName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,2),_AgentOpenFlowFlowTableName_Type())
agentOpenFlowFlowTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowTableName.setStatus(_A)
class _AgentOpenFlowFlowTableDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_AgentOpenFlowFlowTableDescription_Type.__name__=_H
_AgentOpenFlowFlowTableDescription_Object=MibTableColumn
agentOpenFlowFlowTableDescription=_AgentOpenFlowFlowTableDescription_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,3),_AgentOpenFlowFlowTableDescription_Type())
agentOpenFlowFlowTableDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowTableDescription.setStatus(_A)
_AgentOpenFlowMaximumSize_Type=Unsigned32
_AgentOpenFlowMaximumSize_Object=MibTableColumn
agentOpenFlowMaximumSize=_AgentOpenFlowMaximumSize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,4),_AgentOpenFlowMaximumSize_Type())
agentOpenFlowMaximumSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowMaximumSize.setStatus(_A)
_AgentOpenFlowNumberOfEntries_Type=Unsigned32
_AgentOpenFlowNumberOfEntries_Object=MibTableColumn
agentOpenFlowNumberOfEntries=_AgentOpenFlowNumberOfEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,5),_AgentOpenFlowNumberOfEntries_Type())
agentOpenFlowNumberOfEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowNumberOfEntries.setStatus(_A)
_AgentOpenFlowHardwareEntries_Type=Unsigned32
_AgentOpenFlowHardwareEntries_Object=MibTableColumn
agentOpenFlowHardwareEntries=_AgentOpenFlowHardwareEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,6),_AgentOpenFlowHardwareEntries_Type())
agentOpenFlowHardwareEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowHardwareEntries.setStatus(_A)
_AgentOpenFlowSoftwareOnlyEntries_Type=Unsigned32
_AgentOpenFlowSoftwareOnlyEntries_Object=MibTableColumn
agentOpenFlowSoftwareOnlyEntries=_AgentOpenFlowSoftwareOnlyEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,7),_AgentOpenFlowSoftwareOnlyEntries_Type())
agentOpenFlowSoftwareOnlyEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowSoftwareOnlyEntries.setStatus(_A)
_AgentOpenFlowWaitingForSpaceEntries_Type=Unsigned32
_AgentOpenFlowWaitingForSpaceEntries_Object=MibTableColumn
agentOpenFlowWaitingForSpaceEntries=_AgentOpenFlowWaitingForSpaceEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,8),_AgentOpenFlowWaitingForSpaceEntries_Type())
agentOpenFlowWaitingForSpaceEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowWaitingForSpaceEntries.setStatus(_A)
_AgentOpenFlowFlowInsertionCount_Type=Unsigned32
_AgentOpenFlowFlowInsertionCount_Object=MibTableColumn
agentOpenFlowFlowInsertionCount=_AgentOpenFlowFlowInsertionCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,9),_AgentOpenFlowFlowInsertionCount_Type())
agentOpenFlowFlowInsertionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowInsertionCount.setStatus(_A)
_AgentOpenFlowFlowDeletionCount_Type=Unsigned32
_AgentOpenFlowFlowDeletionCount_Object=MibTableColumn
agentOpenFlowFlowDeletionCount=_AgentOpenFlowFlowDeletionCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,10),_AgentOpenFlowFlowDeletionCount_Type())
agentOpenFlowFlowDeletionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowDeletionCount.setStatus(_A)
_AgentOpenFlowInsertionFailureCount_Type=Unsigned32
_AgentOpenFlowInsertionFailureCount_Object=MibTableColumn
agentOpenFlowInsertionFailureCount=_AgentOpenFlowInsertionFailureCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,8,1,11),_AgentOpenFlowInsertionFailureCount_Type())
agentOpenFlowInsertionFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowInsertionFailureCount.setStatus(_A)
_AgentOpenFlowInstalledGroupEntry_ObjectIdentity=ObjectIdentity
agentOpenFlowInstalledGroupEntry=_AgentOpenFlowInstalledGroupEntry_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9))
_AgentOpenFlowGrpIndirectMaxEntries_Type=Unsigned32
_AgentOpenFlowGrpIndirectMaxEntries_Object=MibScalar
agentOpenFlowGrpIndirectMaxEntries=_AgentOpenFlowGrpIndirectMaxEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9,1),_AgentOpenFlowGrpIndirectMaxEntries_Type())
agentOpenFlowGrpIndirectMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGrpIndirectMaxEntries.setStatus(_A)
_AgentOpenFlowGrpIndirectCurrentEntries_Type=Unsigned32
_AgentOpenFlowGrpIndirectCurrentEntries_Object=MibScalar
agentOpenFlowGrpIndirectCurrentEntries=_AgentOpenFlowGrpIndirectCurrentEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9,2),_AgentOpenFlowGrpIndirectCurrentEntries_Type())
agentOpenFlowGrpIndirectCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGrpIndirectCurrentEntries.setStatus(_A)
_AgentOpenFlowGrpAllMaxEntries_Type=Unsigned32
_AgentOpenFlowGrpAllMaxEntries_Object=MibScalar
agentOpenFlowGrpAllMaxEntries=_AgentOpenFlowGrpAllMaxEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9,3),_AgentOpenFlowGrpAllMaxEntries_Type())
agentOpenFlowGrpAllMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGrpAllMaxEntries.setStatus(_A)
_AgentOpenFlowGrpAllCurrentEntries_Type=Unsigned32
_AgentOpenFlowGrpAllCurrentEntries_Object=MibScalar
agentOpenFlowGrpAllCurrentEntries=_AgentOpenFlowGrpAllCurrentEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9,4),_AgentOpenFlowGrpAllCurrentEntries_Type())
agentOpenFlowGrpAllCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGrpAllCurrentEntries.setStatus(_A)
_AgentOpenFlowGrpSelectMaxEntries_Type=Unsigned32
_AgentOpenFlowGrpSelectMaxEntries_Object=MibScalar
agentOpenFlowGrpSelectMaxEntries=_AgentOpenFlowGrpSelectMaxEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9,5),_AgentOpenFlowGrpSelectMaxEntries_Type())
agentOpenFlowGrpSelectMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGrpSelectMaxEntries.setStatus(_A)
_AgentOpenFlowGrpSelectCurrentEntries_Type=Unsigned32
_AgentOpenFlowGrpSelectCurrentEntries_Object=MibScalar
agentOpenFlowGrpSelectCurrentEntries=_AgentOpenFlowGrpSelectCurrentEntries_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,9,6),_AgentOpenFlowGrpSelectCurrentEntries_Type())
agentOpenFlowGrpSelectCurrentEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGrpSelectCurrentEntries.setStatus(_A)
_AgentOpenFlowGroupDetailsTable_Object=MibTable
agentOpenFlowGroupDetailsTable=_AgentOpenFlowGroupDetailsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10))
if mibBuilder.loadTexts:agentOpenFlowGroupDetailsTable.setStatus(_A)
_AgentOpenFlowGroupDetailsEntry_Object=MibTableRow
agentOpenFlowGroupDetailsEntry=_AgentOpenFlowGroupDetailsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10,1))
agentOpenFlowGroupDetailsEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:agentOpenFlowGroupDetailsEntry.setStatus(_A)
class _AgentOpenFlowGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowGroupId_Type.__name__=_D
_AgentOpenFlowGroupId_Object=MibTableColumn
agentOpenFlowGroupId=_AgentOpenFlowGroupId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10,1,1),_AgentOpenFlowGroupId_Type())
agentOpenFlowGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupId.setStatus(_A)
_AgentOpenFlowGroupType_Type=DisplayString
_AgentOpenFlowGroupType_Object=MibTableColumn
agentOpenFlowGroupType=_AgentOpenFlowGroupType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10,1,2),_AgentOpenFlowGroupType_Type())
agentOpenFlowGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupType.setStatus(_A)
class _AgentOpenFlowGroupRefCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowGroupRefCount_Type.__name__=_D
_AgentOpenFlowGroupRefCount_Object=MibTableColumn
agentOpenFlowGroupRefCount=_AgentOpenFlowGroupRefCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10,1,3),_AgentOpenFlowGroupRefCount_Type())
agentOpenFlowGroupRefCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupRefCount.setStatus(_A)
class _AgentOpenFlowGroupDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowGroupDuration_Type.__name__=_D
_AgentOpenFlowGroupDuration_Object=MibTableColumn
agentOpenFlowGroupDuration=_AgentOpenFlowGroupDuration_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10,1,4),_AgentOpenFlowGroupDuration_Type())
agentOpenFlowGroupDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupDuration.setStatus(_A)
class _AgentOpenFlowGroupBucketCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowGroupBucketCount_Type.__name__=_D
_AgentOpenFlowGroupBucketCount_Object=MibTableColumn
agentOpenFlowGroupBucketCount=_AgentOpenFlowGroupBucketCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,10,1,5),_AgentOpenFlowGroupBucketCount_Type())
agentOpenFlowGroupBucketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketCount.setStatus(_A)
_AgentOpenFlowGroupBucketDetailsTable_Object=MibTable
agentOpenFlowGroupBucketDetailsTable=_AgentOpenFlowGroupBucketDetailsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11))
if mibBuilder.loadTexts:agentOpenFlowGroupBucketDetailsTable.setStatus(_A)
_AgentOpenFlowGroupBucketDetailsEntry_Object=MibTableRow
agentOpenFlowGroupBucketDetailsEntry=_AgentOpenFlowGroupBucketDetailsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1))
agentOpenFlowGroupBucketDetailsEntry.setIndexNames((0,_F,_P),(0,_F,_Q))
if mibBuilder.loadTexts:agentOpenFlowGroupBucketDetailsEntry.setStatus(_A)
class _AgentOpenFlowGroupBucketId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowGroupBucketId_Type.__name__=_D
_AgentOpenFlowGroupBucketId_Object=MibTableColumn
agentOpenFlowGroupBucketId=_AgentOpenFlowGroupBucketId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,1),_AgentOpenFlowGroupBucketId_Type())
agentOpenFlowGroupBucketId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketId.setStatus(_A)
_AgentOpenFlowGroupBucketOutputPort_Type=DisplayString
_AgentOpenFlowGroupBucketOutputPort_Object=MibTableColumn
agentOpenFlowGroupBucketOutputPort=_AgentOpenFlowGroupBucketOutputPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,2),_AgentOpenFlowGroupBucketOutputPort_Type())
agentOpenFlowGroupBucketOutputPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketOutputPort.setStatus(_A)
_AgentOpenFlowGroupBucketVlanId_Type=DisplayString
_AgentOpenFlowGroupBucketVlanId_Object=MibTableColumn
agentOpenFlowGroupBucketVlanId=_AgentOpenFlowGroupBucketVlanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,3),_AgentOpenFlowGroupBucketVlanId_Type())
agentOpenFlowGroupBucketVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketVlanId.setStatus(_A)
_AgentOpenFlowGroupBucketRefGroupId_Type=DisplayString
_AgentOpenFlowGroupBucketRefGroupId_Object=MibTableColumn
agentOpenFlowGroupBucketRefGroupId=_AgentOpenFlowGroupBucketRefGroupId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,4),_AgentOpenFlowGroupBucketRefGroupId_Type())
agentOpenFlowGroupBucketRefGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketRefGroupId.setStatus(_A)
_AgentOpenFlowGroupBucketSrcMac_Type=PhysAddress
_AgentOpenFlowGroupBucketSrcMac_Object=MibTableColumn
agentOpenFlowGroupBucketSrcMac=_AgentOpenFlowGroupBucketSrcMac_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,5),_AgentOpenFlowGroupBucketSrcMac_Type())
agentOpenFlowGroupBucketSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketSrcMac.setStatus(_A)
_AgentOpenFlowGroupBucketDstMac_Type=PhysAddress
_AgentOpenFlowGroupBucketDstMac_Object=MibTableColumn
agentOpenFlowGroupBucketDstMac=_AgentOpenFlowGroupBucketDstMac_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,6),_AgentOpenFlowGroupBucketDstMac_Type())
agentOpenFlowGroupBucketDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowGroupBucketDstMac.setStatus(_A)
class _AgentOpenFlowBucketGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowBucketGroupId_Type.__name__=_D
_AgentOpenFlowBucketGroupId_Object=MibTableColumn
agentOpenFlowBucketGroupId=_AgentOpenFlowBucketGroupId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,56,1,11,1,7),_AgentOpenFlowBucketGroupId_Type())
agentOpenFlowBucketGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowBucketGroupId.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fastPathOpenFlow':fastPathOpenFlow,'agentOpenFlowGroup':agentOpenFlowGroup,'agentOpenFlowGlobalConfigGroup':agentOpenFlowGlobalConfigGroup,'agentOpenFlowAdminMode':agentOpenFlowAdminMode,'agentOpenFlowVariant':agentOpenFlowVariant,'agentOpenFlowDefaultTable':agentOpenFlowDefaultTable,'agentOpenFlowStaticIPAssignmentMode':agentOpenFlowStaticIPAssignmentMode,'agentOpenFlowGlobalConfigIPAddress':agentOpenFlowGlobalConfigIPAddress,'agentOpenFlowNetworkMTU':agentOpenFlowNetworkMTU,'agentOpenFlowIPAssignmentMode':agentOpenFlowIPAssignmentMode,'agentOpenFlowCfgControllerTable':agentOpenFlowCfgControllerTable,'agentOpenFlowCfgControllerEntry':agentOpenFlowCfgControllerEntry,_L:agentOpenFlowCfgCtrlIPAddress,_M:agentOpenFlowCfgCtrlIPPort,'agentOpenFlowCfgCtrlConnectionMode':agentOpenFlowCfgCtrlConnectionMode,'agentOpenFlowCfgCtrlStatus':agentOpenFlowCfgCtrlStatus,'agentOpenFlowCfgCtrlRole':agentOpenFlowCfgCtrlRole,'agentOpenFlowGlobalStatusParameters':agentOpenFlowGlobalStatusParameters,'agentOpenFlowOperationalStatus':agentOpenFlowOperationalStatus,'agentOpenFlowDisableReason':agentOpenFlowDisableReason,'agentOpenFlowGlobalCommands':agentOpenFlowGlobalCommands,'agentOpenFlowEraseOpenFlowManagerCertificates':agentOpenFlowEraseOpenFlowManagerCertificates,'agentOpenFlowFlowTableStatusTable':agentOpenFlowFlowTableStatusTable,'agentOpenFlowFlowTableStatusEntry':agentOpenFlowFlowTableStatusEntry,_N:agentOpenFlowFlowTable,'agentOpenFlowFlowTableName':agentOpenFlowFlowTableName,'agentOpenFlowFlowTableDescription':agentOpenFlowFlowTableDescription,'agentOpenFlowMaximumSize':agentOpenFlowMaximumSize,'agentOpenFlowNumberOfEntries':agentOpenFlowNumberOfEntries,'agentOpenFlowHardwareEntries':agentOpenFlowHardwareEntries,'agentOpenFlowSoftwareOnlyEntries':agentOpenFlowSoftwareOnlyEntries,'agentOpenFlowWaitingForSpaceEntries':agentOpenFlowWaitingForSpaceEntries,'agentOpenFlowFlowInsertionCount':agentOpenFlowFlowInsertionCount,'agentOpenFlowFlowDeletionCount':agentOpenFlowFlowDeletionCount,'agentOpenFlowInsertionFailureCount':agentOpenFlowInsertionFailureCount,'agentOpenFlowInstalledGroupEntry':agentOpenFlowInstalledGroupEntry,'agentOpenFlowGrpIndirectMaxEntries':agentOpenFlowGrpIndirectMaxEntries,'agentOpenFlowGrpIndirectCurrentEntries':agentOpenFlowGrpIndirectCurrentEntries,'agentOpenFlowGrpAllMaxEntries':agentOpenFlowGrpAllMaxEntries,'agentOpenFlowGrpAllCurrentEntries':agentOpenFlowGrpAllCurrentEntries,'agentOpenFlowGrpSelectMaxEntries':agentOpenFlowGrpSelectMaxEntries,'agentOpenFlowGrpSelectCurrentEntries':agentOpenFlowGrpSelectCurrentEntries,'agentOpenFlowGroupDetailsTable':agentOpenFlowGroupDetailsTable,'agentOpenFlowGroupDetailsEntry':agentOpenFlowGroupDetailsEntry,_O:agentOpenFlowGroupId,'agentOpenFlowGroupType':agentOpenFlowGroupType,'agentOpenFlowGroupRefCount':agentOpenFlowGroupRefCount,'agentOpenFlowGroupDuration':agentOpenFlowGroupDuration,'agentOpenFlowGroupBucketCount':agentOpenFlowGroupBucketCount,'agentOpenFlowGroupBucketDetailsTable':agentOpenFlowGroupBucketDetailsTable,'agentOpenFlowGroupBucketDetailsEntry':agentOpenFlowGroupBucketDetailsEntry,_Q:agentOpenFlowGroupBucketId,'agentOpenFlowGroupBucketOutputPort':agentOpenFlowGroupBucketOutputPort,'agentOpenFlowGroupBucketVlanId':agentOpenFlowGroupBucketVlanId,'agentOpenFlowGroupBucketRefGroupId':agentOpenFlowGroupBucketRefGroupId,'agentOpenFlowGroupBucketSrcMac':agentOpenFlowGroupBucketSrcMac,'agentOpenFlowGroupBucketDstMac':agentOpenFlowGroupBucketDstMac,_P:agentOpenFlowBucketGroupId})