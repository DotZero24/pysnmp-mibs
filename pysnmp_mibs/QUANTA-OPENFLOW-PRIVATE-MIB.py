_M='agentOpenFlowFlowTable'
_L='agentOpenFlowCfgCtrlIPPort'
_K='agentOpenFlowCfgCtrlIPAddress'
_J='disable'
_I='enable'
_H='read-write'
_G='Unsigned32'
_F='OctetString'
_E='read-create'
_D='QUANTA-OPENFLOW-PRIVATE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch,=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
openFlow=ModuleIdentity((1,3,6,1,4,1,7244,2,200))
if mibBuilder.loadTexts:openFlow.setRevisions(('2011-03-06 00:00',))
_AgentOpenFlowGroup_ObjectIdentity=ObjectIdentity
agentOpenFlowGroup=_AgentOpenFlowGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,200,1))
_AgentOpenFlowGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentOpenFlowGlobalConfigGroup=_AgentOpenFlowGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,200,1,1))
class _AgentOpenFlowAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AgentOpenFlowAdminMode_Type.__name__=_C
_AgentOpenFlowAdminMode_Object=MibScalar
agentOpenFlowAdminMode=_AgentOpenFlowAdminMode_Object((1,3,6,1,4,1,7244,2,200,1,1,1),_AgentOpenFlowAdminMode_Type())
agentOpenFlowAdminMode.setMaxAccess(_H)
if mibBuilder.loadTexts:agentOpenFlowAdminMode.setStatus(_A)
class _AgentOpenFlowVariant_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('openFlow10Mode',2),('openFlow11Mode',3),('openFlow12Mode',4),('openFlow13Mode',5)))
_AgentOpenFlowVariant_Type.__name__=_C
_AgentOpenFlowVariant_Object=MibScalar
agentOpenFlowVariant=_AgentOpenFlowVariant_Object((1,3,6,1,4,1,7244,2,200,1,1,2),_AgentOpenFlowVariant_Type())
agentOpenFlowVariant.setMaxAccess(_H)
if mibBuilder.loadTexts:agentOpenFlowVariant.setStatus(_A)
_AgentOpenFlowCfgControllerTable_Object=MibTable
agentOpenFlowCfgControllerTable=_AgentOpenFlowCfgControllerTable_Object((1,3,6,1,4,1,7244,2,200,1,3))
if mibBuilder.loadTexts:agentOpenFlowCfgControllerTable.setStatus(_A)
_AgentOpenFlowCfgControllerEntry_Object=MibTableRow
agentOpenFlowCfgControllerEntry=_AgentOpenFlowCfgControllerEntry_Object((1,3,6,1,4,1,7244,2,200,1,3,1))
agentOpenFlowCfgControllerEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:agentOpenFlowCfgControllerEntry.setStatus(_A)
_AgentOpenFlowCfgCtrlIPAddress_Type=IpAddress
_AgentOpenFlowCfgCtrlIPAddress_Object=MibTableColumn
agentOpenFlowCfgCtrlIPAddress=_AgentOpenFlowCfgCtrlIPAddress_Object((1,3,6,1,4,1,7244,2,200,1,3,1,1),_AgentOpenFlowCfgCtrlIPAddress_Type())
agentOpenFlowCfgCtrlIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlIPAddress.setStatus(_A)
class _AgentOpenFlowCfgCtrlIPPort_Type(Unsigned32):defaultValue=6632;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentOpenFlowCfgCtrlIPPort_Type.__name__=_G
_AgentOpenFlowCfgCtrlIPPort_Object=MibTableColumn
agentOpenFlowCfgCtrlIPPort=_AgentOpenFlowCfgCtrlIPPort_Object((1,3,6,1,4,1,7244,2,200,1,3,1,2),_AgentOpenFlowCfgCtrlIPPort_Type())
agentOpenFlowCfgCtrlIPPort.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlIPPort.setStatus(_A)
class _AgentOpenFlowCfgCtrlConnectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ssl',1),('tcp',2)))
_AgentOpenFlowCfgCtrlConnectionMode_Type.__name__=_C
_AgentOpenFlowCfgCtrlConnectionMode_Object=MibTableColumn
agentOpenFlowCfgCtrlConnectionMode=_AgentOpenFlowCfgCtrlConnectionMode_Object((1,3,6,1,4,1,7244,2,200,1,3,1,3),_AgentOpenFlowCfgCtrlConnectionMode_Type())
agentOpenFlowCfgCtrlConnectionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlConnectionMode.setStatus(_A)
_AgentOpenFlowCfgCtrlStatus_Type=RowStatus
_AgentOpenFlowCfgCtrlStatus_Object=MibTableColumn
agentOpenFlowCfgCtrlStatus=_AgentOpenFlowCfgCtrlStatus_Object((1,3,6,1,4,1,7244,2,200,1,3,1,4),_AgentOpenFlowCfgCtrlStatus_Type())
agentOpenFlowCfgCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentOpenFlowCfgCtrlStatus.setStatus(_A)
_AgentOpenFlowGlobalStatusParameters_ObjectIdentity=ObjectIdentity
agentOpenFlowGlobalStatusParameters=_AgentOpenFlowGlobalStatusParameters_ObjectIdentity((1,3,6,1,4,1,7244,2,200,1,6))
class _AgentOpenFlowOperationalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),('enablePending',3),('disablePending',4)))
_AgentOpenFlowOperationalStatus_Type.__name__=_C
_AgentOpenFlowOperationalStatus_Object=MibScalar
agentOpenFlowOperationalStatus=_AgentOpenFlowOperationalStatus_Object((1,3,6,1,4,1,7244,2,200,1,6,1),_AgentOpenFlowOperationalStatus_Type())
agentOpenFlowOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowOperationalStatus.setStatus(_A)
class _AgentOpenFlowDisableReason_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('administrativelyDisabled',2),('noSuitableIPInterface',3),('noSSLCertificates',4)))
_AgentOpenFlowDisableReason_Type.__name__=_C
_AgentOpenFlowDisableReason_Object=MibScalar
agentOpenFlowDisableReason=_AgentOpenFlowDisableReason_Object((1,3,6,1,4,1,7244,2,200,1,6,2),_AgentOpenFlowDisableReason_Type())
agentOpenFlowDisableReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowDisableReason.setStatus(_A)
_AgentOpenFlowGlobalCommands_ObjectIdentity=ObjectIdentity
agentOpenFlowGlobalCommands=_AgentOpenFlowGlobalCommands_ObjectIdentity((1,3,6,1,4,1,7244,2,200,1,7))
class _AgentOpenFlowEraseOpenFlowManagerCertificates_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alwaysReturnedOnRead',1),('eraseCertificates',2)))
_AgentOpenFlowEraseOpenFlowManagerCertificates_Type.__name__=_C
_AgentOpenFlowEraseOpenFlowManagerCertificates_Object=MibScalar
agentOpenFlowEraseOpenFlowManagerCertificates=_AgentOpenFlowEraseOpenFlowManagerCertificates_Object((1,3,6,1,4,1,7244,2,200,1,7,1),_AgentOpenFlowEraseOpenFlowManagerCertificates_Type())
agentOpenFlowEraseOpenFlowManagerCertificates.setMaxAccess(_H)
if mibBuilder.loadTexts:agentOpenFlowEraseOpenFlowManagerCertificates.setStatus(_A)
_AgentOpenFlowFlowTableStatusTable_Object=MibTable
agentOpenFlowFlowTableStatusTable=_AgentOpenFlowFlowTableStatusTable_Object((1,3,6,1,4,1,7244,2,200,1,8))
if mibBuilder.loadTexts:agentOpenFlowFlowTableStatusTable.setStatus(_A)
_AgentOpenFlowFlowTableStatusEntry_Object=MibTableRow
agentOpenFlowFlowTableStatusEntry=_AgentOpenFlowFlowTableStatusEntry_Object((1,3,6,1,4,1,7244,2,200,1,8,1))
agentOpenFlowFlowTableStatusEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:agentOpenFlowFlowTableStatusEntry.setStatus(_A)
class _AgentOpenFlowFlowTable_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentOpenFlowFlowTable_Type.__name__=_G
_AgentOpenFlowFlowTable_Object=MibTableColumn
agentOpenFlowFlowTable=_AgentOpenFlowFlowTable_Object((1,3,6,1,4,1,7244,2,200,1,8,1,1),_AgentOpenFlowFlowTable_Type())
agentOpenFlowFlowTable.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowTable.setStatus(_A)
class _AgentOpenFlowFlowTableName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgentOpenFlowFlowTableName_Type.__name__=_F
_AgentOpenFlowFlowTableName_Object=MibTableColumn
agentOpenFlowFlowTableName=_AgentOpenFlowFlowTableName_Object((1,3,6,1,4,1,7244,2,200,1,8,1,2),_AgentOpenFlowFlowTableName_Type())
agentOpenFlowFlowTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowTableName.setStatus(_A)
class _AgentOpenFlowFlowTableDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_AgentOpenFlowFlowTableDescription_Type.__name__=_F
_AgentOpenFlowFlowTableDescription_Object=MibTableColumn
agentOpenFlowFlowTableDescription=_AgentOpenFlowFlowTableDescription_Object((1,3,6,1,4,1,7244,2,200,1,8,1,3),_AgentOpenFlowFlowTableDescription_Type())
agentOpenFlowFlowTableDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowTableDescription.setStatus(_A)
_AgentOpenFlowMaximumSize_Type=Unsigned32
_AgentOpenFlowMaximumSize_Object=MibTableColumn
agentOpenFlowMaximumSize=_AgentOpenFlowMaximumSize_Object((1,3,6,1,4,1,7244,2,200,1,8,1,4),_AgentOpenFlowMaximumSize_Type())
agentOpenFlowMaximumSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowMaximumSize.setStatus(_A)
_AgentOpenFlowNumberOfEntries_Type=Unsigned32
_AgentOpenFlowNumberOfEntries_Object=MibTableColumn
agentOpenFlowNumberOfEntries=_AgentOpenFlowNumberOfEntries_Object((1,3,6,1,4,1,7244,2,200,1,8,1,5),_AgentOpenFlowNumberOfEntries_Type())
agentOpenFlowNumberOfEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowNumberOfEntries.setStatus(_A)
_AgentOpenFlowHardwareEntries_Type=Unsigned32
_AgentOpenFlowHardwareEntries_Object=MibTableColumn
agentOpenFlowHardwareEntries=_AgentOpenFlowHardwareEntries_Object((1,3,6,1,4,1,7244,2,200,1,8,1,6),_AgentOpenFlowHardwareEntries_Type())
agentOpenFlowHardwareEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowHardwareEntries.setStatus(_A)
_AgentOpenFlowSoftwareOnlyEntries_Type=Unsigned32
_AgentOpenFlowSoftwareOnlyEntries_Object=MibTableColumn
agentOpenFlowSoftwareOnlyEntries=_AgentOpenFlowSoftwareOnlyEntries_Object((1,3,6,1,4,1,7244,2,200,1,8,1,7),_AgentOpenFlowSoftwareOnlyEntries_Type())
agentOpenFlowSoftwareOnlyEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowSoftwareOnlyEntries.setStatus(_A)
_AgentOpenFlowWaitingForSpaceEntries_Type=Unsigned32
_AgentOpenFlowWaitingForSpaceEntries_Object=MibTableColumn
agentOpenFlowWaitingForSpaceEntries=_AgentOpenFlowWaitingForSpaceEntries_Object((1,3,6,1,4,1,7244,2,200,1,8,1,8),_AgentOpenFlowWaitingForSpaceEntries_Type())
agentOpenFlowWaitingForSpaceEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowWaitingForSpaceEntries.setStatus(_A)
_AgentOpenFlowFlowInsertionCount_Type=Unsigned32
_AgentOpenFlowFlowInsertionCount_Object=MibTableColumn
agentOpenFlowFlowInsertionCount=_AgentOpenFlowFlowInsertionCount_Object((1,3,6,1,4,1,7244,2,200,1,8,1,9),_AgentOpenFlowFlowInsertionCount_Type())
agentOpenFlowFlowInsertionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowInsertionCount.setStatus(_A)
_AgentOpenFlowFlowDeletionCount_Type=Unsigned32
_AgentOpenFlowFlowDeletionCount_Object=MibTableColumn
agentOpenFlowFlowDeletionCount=_AgentOpenFlowFlowDeletionCount_Object((1,3,6,1,4,1,7244,2,200,1,8,1,10),_AgentOpenFlowFlowDeletionCount_Type())
agentOpenFlowFlowDeletionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowFlowDeletionCount.setStatus(_A)
_AgentOpenFlowInsertionFailureCount_Type=Unsigned32
_AgentOpenFlowInsertionFailureCount_Object=MibTableColumn
agentOpenFlowInsertionFailureCount=_AgentOpenFlowInsertionFailureCount_Object((1,3,6,1,4,1,7244,2,200,1,8,1,11),_AgentOpenFlowInsertionFailureCount_Type())
agentOpenFlowInsertionFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOpenFlowInsertionFailureCount.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'openFlow':openFlow,'agentOpenFlowGroup':agentOpenFlowGroup,'agentOpenFlowGlobalConfigGroup':agentOpenFlowGlobalConfigGroup,'agentOpenFlowAdminMode':agentOpenFlowAdminMode,'agentOpenFlowVariant':agentOpenFlowVariant,'agentOpenFlowCfgControllerTable':agentOpenFlowCfgControllerTable,'agentOpenFlowCfgControllerEntry':agentOpenFlowCfgControllerEntry,_K:agentOpenFlowCfgCtrlIPAddress,_L:agentOpenFlowCfgCtrlIPPort,'agentOpenFlowCfgCtrlConnectionMode':agentOpenFlowCfgCtrlConnectionMode,'agentOpenFlowCfgCtrlStatus':agentOpenFlowCfgCtrlStatus,'agentOpenFlowGlobalStatusParameters':agentOpenFlowGlobalStatusParameters,'agentOpenFlowOperationalStatus':agentOpenFlowOperationalStatus,'agentOpenFlowDisableReason':agentOpenFlowDisableReason,'agentOpenFlowGlobalCommands':agentOpenFlowGlobalCommands,'agentOpenFlowEraseOpenFlowManagerCertificates':agentOpenFlowEraseOpenFlowManagerCertificates,'agentOpenFlowFlowTableStatusTable':agentOpenFlowFlowTableStatusTable,'agentOpenFlowFlowTableStatusEntry':agentOpenFlowFlowTableStatusEntry,_M:agentOpenFlowFlowTable,'agentOpenFlowFlowTableName':agentOpenFlowFlowTableName,'agentOpenFlowFlowTableDescription':agentOpenFlowFlowTableDescription,'agentOpenFlowMaximumSize':agentOpenFlowMaximumSize,'agentOpenFlowNumberOfEntries':agentOpenFlowNumberOfEntries,'agentOpenFlowHardwareEntries':agentOpenFlowHardwareEntries,'agentOpenFlowSoftwareOnlyEntries':agentOpenFlowSoftwareOnlyEntries,'agentOpenFlowWaitingForSpaceEntries':agentOpenFlowWaitingForSpaceEntries,'agentOpenFlowFlowInsertionCount':agentOpenFlowFlowInsertionCount,'agentOpenFlowFlowDeletionCount':agentOpenFlowFlowDeletionCount,'agentOpenFlowInsertionFailureCount':agentOpenFlowInsertionFailureCount})