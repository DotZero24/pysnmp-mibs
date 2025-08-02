_I='deprecated'
_H='mgnt4nodeIndexChassis'
_G='read-write'
_F='mgnt4nodeManagerIpIndex'
_E='EKINOPS-MGNT4NODE-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiLoadGWSW,EkiLoadPermutMethod,EkiLoadPermutMode,EkiLoadState,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiLoadGWSW','EkiLoadPermutMethod','EkiLoadPermutMode','EkiLoadState','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mgnt4node=ModuleIdentity((1,3,6,1,4,1,20044,111))
if mibBuilder.loadTexts:mgnt4node.setRevisions(('2012-05-04 00:00','2015-03-03 00:00'))
_Mgnt4nodeSNMPAgentData_ObjectIdentity=ObjectIdentity
mgnt4nodeSNMPAgentData=_Mgnt4nodeSNMPAgentData_ObjectIdentity((1,3,6,1,4,1,20044,111,1))
_Mgnt4nodeIPmanagment_ObjectIdentity=ObjectIdentity
mgnt4nodeIPmanagment=_Mgnt4nodeIPmanagment_ObjectIdentity((1,3,6,1,4,1,20044,111,1,1))
_Mgnt4nodeManagerIpAddressTable_Object=MibTable
mgnt4nodeManagerIpAddressTable=_Mgnt4nodeManagerIpAddressTable_Object((1,3,6,1,4,1,20044,111,1,1,1))
if mibBuilder.loadTexts:mgnt4nodeManagerIpAddressTable.setStatus(_A)
_Mgnt4nodeManagerIpAddressEntry_Object=MibTableRow
mgnt4nodeManagerIpAddressEntry=_Mgnt4nodeManagerIpAddressEntry_Object((1,3,6,1,4,1,20044,111,1,1,1,1))
mgnt4nodeManagerIpAddressEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mgnt4nodeManagerIpAddressEntry.setStatus(_A)
class _Mgnt4nodeManagerIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Mgnt4nodeManagerIpIndex_Type.__name__=_D
_Mgnt4nodeManagerIpIndex_Object=MibTableColumn
mgnt4nodeManagerIpIndex=_Mgnt4nodeManagerIpIndex_Object((1,3,6,1,4,1,20044,111,1,1,1,1,1),_Mgnt4nodeManagerIpIndex_Type())
mgnt4nodeManagerIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerIpIndex.setStatus(_A)
_Mgnt4nodeManagerIpAddress_Type=IpAddress
_Mgnt4nodeManagerIpAddress_Object=MibTableColumn
mgnt4nodeManagerIpAddress=_Mgnt4nodeManagerIpAddress_Object((1,3,6,1,4,1,20044,111,1,1,1,1,2),_Mgnt4nodeManagerIpAddress_Type())
mgnt4nodeManagerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerIpAddress.setStatus(_A)
_Mgnt4nodeManagerIpAddressTableRowStatus_Type=RowStatus
_Mgnt4nodeManagerIpAddressTableRowStatus_Object=MibTableColumn
mgnt4nodeManagerIpAddressTableRowStatus=_Mgnt4nodeManagerIpAddressTableRowStatus_Object((1,3,6,1,4,1,20044,111,1,1,1,1,3),_Mgnt4nodeManagerIpAddressTableRowStatus_Type())
mgnt4nodeManagerIpAddressTableRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerIpAddressTableRowStatus.setStatus(_A)
_Mgnt4nodeManagerTrapPort_Type=Integer32
_Mgnt4nodeManagerTrapPort_Object=MibTableColumn
mgnt4nodeManagerTrapPort=_Mgnt4nodeManagerTrapPort_Object((1,3,6,1,4,1,20044,111,1,1,1,1,4),_Mgnt4nodeManagerTrapPort_Type())
mgnt4nodeManagerTrapPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerTrapPort.setStatus(_A)
_Mgnt4nodeManagerEnableCtrl_Type=EkiOnOff
_Mgnt4nodeManagerEnableCtrl_Object=MibTableColumn
mgnt4nodeManagerEnableCtrl=_Mgnt4nodeManagerEnableCtrl_Object((1,3,6,1,4,1,20044,111,1,1,1,1,5),_Mgnt4nodeManagerEnableCtrl_Type())
mgnt4nodeManagerEnableCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableCtrl.setStatus(_A)
_Mgnt4nodeManagerEnableConfig_Type=EkiOnOff
_Mgnt4nodeManagerEnableConfig_Object=MibTableColumn
mgnt4nodeManagerEnableConfig=_Mgnt4nodeManagerEnableConfig_Object((1,3,6,1,4,1,20044,111,1,1,1,1,6),_Mgnt4nodeManagerEnableConfig_Type())
mgnt4nodeManagerEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableConfig.setStatus(_A)
_Mgnt4nodeManagerEnableEvent_Type=EkiOnOff
_Mgnt4nodeManagerEnableEvent_Object=MibTableColumn
mgnt4nodeManagerEnableEvent=_Mgnt4nodeManagerEnableEvent_Object((1,3,6,1,4,1,20044,111,1,1,1,1,7),_Mgnt4nodeManagerEnableEvent_Type())
mgnt4nodeManagerEnableEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableEvent.setStatus(_A)
_Mgnt4nodeManagerEnableAlarmCrit_Type=EkiOnOff
_Mgnt4nodeManagerEnableAlarmCrit_Object=MibTableColumn
mgnt4nodeManagerEnableAlarmCrit=_Mgnt4nodeManagerEnableAlarmCrit_Object((1,3,6,1,4,1,20044,111,1,1,1,1,8),_Mgnt4nodeManagerEnableAlarmCrit_Type())
mgnt4nodeManagerEnableAlarmCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableAlarmCrit.setStatus(_A)
_Mgnt4nodeManagerEnableAlarmMajor_Type=EkiOnOff
_Mgnt4nodeManagerEnableAlarmMajor_Object=MibTableColumn
mgnt4nodeManagerEnableAlarmMajor=_Mgnt4nodeManagerEnableAlarmMajor_Object((1,3,6,1,4,1,20044,111,1,1,1,1,9),_Mgnt4nodeManagerEnableAlarmMajor_Type())
mgnt4nodeManagerEnableAlarmMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableAlarmMajor.setStatus(_A)
_Mgnt4nodeManagerEnableAlarmMinor_Type=EkiOnOff
_Mgnt4nodeManagerEnableAlarmMinor_Object=MibTableColumn
mgnt4nodeManagerEnableAlarmMinor=_Mgnt4nodeManagerEnableAlarmMinor_Object((1,3,6,1,4,1,20044,111,1,1,1,1,10),_Mgnt4nodeManagerEnableAlarmMinor_Type())
mgnt4nodeManagerEnableAlarmMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableAlarmMinor.setStatus(_A)
_Mgnt4nodeManagerRegistrationTimeout_Type=Integer32
_Mgnt4nodeManagerRegistrationTimeout_Object=MibTableColumn
mgnt4nodeManagerRegistrationTimeout=_Mgnt4nodeManagerRegistrationTimeout_Object((1,3,6,1,4,1,20044,111,1,1,1,1,11),_Mgnt4nodeManagerRegistrationTimeout_Type())
mgnt4nodeManagerRegistrationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerRegistrationTimeout.setStatus(_A)
_Mgnt4nodeManagerEnableAlarmWarning_Type=EkiOnOff
_Mgnt4nodeManagerEnableAlarmWarning_Object=MibTableColumn
mgnt4nodeManagerEnableAlarmWarning=_Mgnt4nodeManagerEnableAlarmWarning_Object((1,3,6,1,4,1,20044,111,1,1,1,1,12),_Mgnt4nodeManagerEnableAlarmWarning_Type())
mgnt4nodeManagerEnableAlarmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableAlarmWarning.setStatus(_A)
_Mgnt4nodeManagerEnableAlarmIndeterminate_Type=EkiOnOff
_Mgnt4nodeManagerEnableAlarmIndeterminate_Object=MibTableColumn
mgnt4nodeManagerEnableAlarmIndeterminate=_Mgnt4nodeManagerEnableAlarmIndeterminate_Object((1,3,6,1,4,1,20044,111,1,1,1,1,13),_Mgnt4nodeManagerEnableAlarmIndeterminate_Type())
mgnt4nodeManagerEnableAlarmIndeterminate.setMaxAccess(_B)
if mibBuilder.loadTexts:mgnt4nodeManagerEnableAlarmIndeterminate.setStatus(_A)
_Mgnt4nodeNodeIpAddress_Type=IpAddress
_Mgnt4nodeNodeIpAddress_Object=MibScalar
mgnt4nodeNodeIpAddress=_Mgnt4nodeNodeIpAddress_Object((1,3,6,1,4,1,20044,111,1,1,8),_Mgnt4nodeNodeIpAddress_Type())
mgnt4nodeNodeIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:mgnt4nodeNodeIpAddress.setStatus(_A)
_Mgnt4nodeChassisManagement_ObjectIdentity=ObjectIdentity
mgnt4nodeChassisManagement=_Mgnt4nodeChassisManagement_ObjectIdentity((1,3,6,1,4,1,20044,111,1,2))
_Mgnt4nodeChassisTable_Object=MibTable
mgnt4nodeChassisTable=_Mgnt4nodeChassisTable_Object((1,3,6,1,4,1,20044,111,1,2,1))
if mibBuilder.loadTexts:mgnt4nodeChassisTable.setStatus(_A)
_Mgnt4nodeChassisEntry_Object=MibTableRow
mgnt4nodeChassisEntry=_Mgnt4nodeChassisEntry_Object((1,3,6,1,4,1,20044,111,1,2,1,1))
mgnt4nodeChassisEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:mgnt4nodeChassisEntry.setStatus(_A)
class _Mgnt4nodeIndexChassis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Mgnt4nodeIndexChassis_Type.__name__=_D
_Mgnt4nodeIndexChassis_Object=MibTableColumn
mgnt4nodeIndexChassis=_Mgnt4nodeIndexChassis_Object((1,3,6,1,4,1,20044,111,1,2,1,1,1),_Mgnt4nodeIndexChassis_Type())
mgnt4nodeIndexChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeIndexChassis.setStatus(_A)
_Mgnt4nodeChassisIpAddress_Type=IpAddress
_Mgnt4nodeChassisIpAddress_Object=MibTableColumn
mgnt4nodeChassisIpAddress=_Mgnt4nodeChassisIpAddress_Object((1,3,6,1,4,1,20044,111,1,2,1,1,2),_Mgnt4nodeChassisIpAddress_Type())
mgnt4nodeChassisIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisIpAddress.setStatus(_A)
class _Mgnt4nodeChassisNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Mgnt4nodeChassisNumber_Type.__name__=_D
_Mgnt4nodeChassisNumber_Object=MibTableColumn
mgnt4nodeChassisNumber=_Mgnt4nodeChassisNumber_Object((1,3,6,1,4,1,20044,111,1,2,1,1,3),_Mgnt4nodeChassisNumber_Type())
mgnt4nodeChassisNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisNumber.setStatus(_A)
_Mgnt4nodeChassisName_Type=DisplayString
_Mgnt4nodeChassisName_Object=MibTableColumn
mgnt4nodeChassisName=_Mgnt4nodeChassisName_Object((1,3,6,1,4,1,20044,111,1,2,1,1,4),_Mgnt4nodeChassisName_Type())
mgnt4nodeChassisName.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisName.setStatus(_A)
_Mgnt4nodeChassisOperational_Type=EkiOnOff
_Mgnt4nodeChassisOperational_Object=MibTableColumn
mgnt4nodeChassisOperational=_Mgnt4nodeChassisOperational_Object((1,3,6,1,4,1,20044,111,1,2,1,1,5),_Mgnt4nodeChassisOperational_Type())
mgnt4nodeChassisOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisOperational.setStatus(_A)
_Mgnt4nodeChassisType_Type=DisplayString
_Mgnt4nodeChassisType_Object=MibTableColumn
mgnt4nodeChassisType=_Mgnt4nodeChassisType_Object((1,3,6,1,4,1,20044,111,1,2,1,1,6),_Mgnt4nodeChassisType_Type())
mgnt4nodeChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisType.setStatus(_A)
_Mgnt4nodeChassisCapability_Type=DisplayString
_Mgnt4nodeChassisCapability_Object=MibTableColumn
mgnt4nodeChassisCapability=_Mgnt4nodeChassisCapability_Object((1,3,6,1,4,1,20044,111,1,2,1,1,7),_Mgnt4nodeChassisCapability_Type())
mgnt4nodeChassisCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisCapability.setStatus(_A)
_Mgnt4nodeChassisSetUp_Type=DisplayString
_Mgnt4nodeChassisSetUp_Object=MibTableColumn
mgnt4nodeChassisSetUp=_Mgnt4nodeChassisSetUp_Object((1,3,6,1,4,1,20044,111,1,2,1,1,8),_Mgnt4nodeChassisSetUp_Type())
mgnt4nodeChassisSetUp.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisSetUp.setStatus(_A)
_Mgnt4nodeChassisPriority_Type=DisplayString
_Mgnt4nodeChassisPriority_Object=MibTableColumn
mgnt4nodeChassisPriority=_Mgnt4nodeChassisPriority_Object((1,3,6,1,4,1,20044,111,1,2,1,1,9),_Mgnt4nodeChassisPriority_Type())
mgnt4nodeChassisPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisPriority.setStatus(_A)
class _Mgnt4nodeChassisGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Mgnt4nodeChassisGroupNumber_Type.__name__=_D
_Mgnt4nodeChassisGroupNumber_Object=MibTableColumn
mgnt4nodeChassisGroupNumber=_Mgnt4nodeChassisGroupNumber_Object((1,3,6,1,4,1,20044,111,1,2,1,1,10),_Mgnt4nodeChassisGroupNumber_Type())
mgnt4nodeChassisGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisGroupNumber.setStatus(_I)
class _Mgnt4nodeChassisRackNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Mgnt4nodeChassisRackNumber_Type.__name__=_D
_Mgnt4nodeChassisRackNumber_Object=MibTableColumn
mgnt4nodeChassisRackNumber=_Mgnt4nodeChassisRackNumber_Object((1,3,6,1,4,1,20044,111,1,2,1,1,11),_Mgnt4nodeChassisRackNumber_Type())
mgnt4nodeChassisRackNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeChassisRackNumber.setStatus(_I)
_Mgnt4nodeName_Type=DisplayString
_Mgnt4nodeName_Object=MibScalar
mgnt4nodeName=_Mgnt4nodeName_Object((1,3,6,1,4,1,20044,111,1,5),_Mgnt4nodeName_Type())
mgnt4nodeName.setMaxAccess(_G)
if mibBuilder.loadTexts:mgnt4nodeName.setStatus(_A)
class _Mgnt4nodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Mgnt4nodeType_Type.__name__=_D
_Mgnt4nodeType_Object=MibScalar
mgnt4nodeType=_Mgnt4nodeType_Object((1,3,6,1,4,1,20044,111,1,6),_Mgnt4nodeType_Type())
mgnt4nodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:mgnt4nodeType.setStatus(_A)
_Mgnt4nodeHardware_ObjectIdentity=ObjectIdentity
mgnt4nodeHardware=_Mgnt4nodeHardware_ObjectIdentity((1,3,6,1,4,1,20044,111,2))
_Mgnt4nodealarms_ObjectIdentity=ObjectIdentity
mgnt4nodealarms=_Mgnt4nodealarms_ObjectIdentity((1,3,6,1,4,1,20044,111,2,1))
_Mgnt4nodecontrols_ObjectIdentity=ObjectIdentity
mgnt4nodecontrols=_Mgnt4nodecontrols_ObjectIdentity((1,3,6,1,4,1,20044,111,2,2))
_Mgnt4nodeconfig_ObjectIdentity=ObjectIdentity
mgnt4nodeconfig=_Mgnt4nodeconfig_ObjectIdentity((1,3,6,1,4,1,20044,111,2,3))
_Mgnt4nodeTraps_ObjectIdentity=ObjectIdentity
mgnt4nodeTraps=_Mgnt4nodeTraps_ObjectIdentity((1,3,6,1,4,1,20044,111,3))
_Mgnt4nodeSoftwareManagement_ObjectIdentity=ObjectIdentity
mgnt4nodeSoftwareManagement=_Mgnt4nodeSoftwareManagement_ObjectIdentity((1,3,6,1,4,1,20044,111,4))
_Mgnt4nodeConfigManagement_ObjectIdentity=ObjectIdentity
mgnt4nodeConfigManagement=_Mgnt4nodeConfigManagement_ObjectIdentity((1,3,6,1,4,1,20044,111,5))
_Mgnt4nodeRemoteInventory_ObjectIdentity=ObjectIdentity
mgnt4nodeRemoteInventory=_Mgnt4nodeRemoteInventory_ObjectIdentity((1,3,6,1,4,1,20044,111,6))
_Mgnt4nodeErrorCounters_ObjectIdentity=ObjectIdentity
mgnt4nodeErrorCounters=_Mgnt4nodeErrorCounters_ObjectIdentity((1,3,6,1,4,1,20044,111,7))
_Mgnt4nodePerf_ObjectIdentity=ObjectIdentity
mgnt4nodePerf=_Mgnt4nodePerf_ObjectIdentity((1,3,6,1,4,1,20044,111,8))
mibBuilder.exportSymbols(_E,**{'mgnt4node':mgnt4node,'mgnt4nodeSNMPAgentData':mgnt4nodeSNMPAgentData,'mgnt4nodeIPmanagment':mgnt4nodeIPmanagment,'mgnt4nodeManagerIpAddressTable':mgnt4nodeManagerIpAddressTable,'mgnt4nodeManagerIpAddressEntry':mgnt4nodeManagerIpAddressEntry,_F:mgnt4nodeManagerIpIndex,'mgnt4nodeManagerIpAddress':mgnt4nodeManagerIpAddress,'mgnt4nodeManagerIpAddressTableRowStatus':mgnt4nodeManagerIpAddressTableRowStatus,'mgnt4nodeManagerTrapPort':mgnt4nodeManagerTrapPort,'mgnt4nodeManagerEnableCtrl':mgnt4nodeManagerEnableCtrl,'mgnt4nodeManagerEnableConfig':mgnt4nodeManagerEnableConfig,'mgnt4nodeManagerEnableEvent':mgnt4nodeManagerEnableEvent,'mgnt4nodeManagerEnableAlarmCrit':mgnt4nodeManagerEnableAlarmCrit,'mgnt4nodeManagerEnableAlarmMajor':mgnt4nodeManagerEnableAlarmMajor,'mgnt4nodeManagerEnableAlarmMinor':mgnt4nodeManagerEnableAlarmMinor,'mgnt4nodeManagerRegistrationTimeout':mgnt4nodeManagerRegistrationTimeout,'mgnt4nodeManagerEnableAlarmWarning':mgnt4nodeManagerEnableAlarmWarning,'mgnt4nodeManagerEnableAlarmIndeterminate':mgnt4nodeManagerEnableAlarmIndeterminate,'mgnt4nodeNodeIpAddress':mgnt4nodeNodeIpAddress,'mgnt4nodeChassisManagement':mgnt4nodeChassisManagement,'mgnt4nodeChassisTable':mgnt4nodeChassisTable,'mgnt4nodeChassisEntry':mgnt4nodeChassisEntry,_H:mgnt4nodeIndexChassis,'mgnt4nodeChassisIpAddress':mgnt4nodeChassisIpAddress,'mgnt4nodeChassisNumber':mgnt4nodeChassisNumber,'mgnt4nodeChassisName':mgnt4nodeChassisName,'mgnt4nodeChassisOperational':mgnt4nodeChassisOperational,'mgnt4nodeChassisType':mgnt4nodeChassisType,'mgnt4nodeChassisCapability':mgnt4nodeChassisCapability,'mgnt4nodeChassisSetUp':mgnt4nodeChassisSetUp,'mgnt4nodeChassisPriority':mgnt4nodeChassisPriority,'mgnt4nodeChassisGroupNumber':mgnt4nodeChassisGroupNumber,'mgnt4nodeChassisRackNumber':mgnt4nodeChassisRackNumber,'mgnt4nodeName':mgnt4nodeName,'mgnt4nodeType':mgnt4nodeType,'mgnt4nodeHardware':mgnt4nodeHardware,'mgnt4nodealarms':mgnt4nodealarms,'mgnt4nodecontrols':mgnt4nodecontrols,'mgnt4nodeconfig':mgnt4nodeconfig,'mgnt4nodeTraps':mgnt4nodeTraps,'mgnt4nodeSoftwareManagement':mgnt4nodeSoftwareManagement,'mgnt4nodeConfigManagement':mgnt4nodeConfigManagement,'mgnt4nodeRemoteInventory':mgnt4nodeRemoteInventory,'mgnt4nodeErrorCounters':mgnt4nodeErrorCounters,'mgnt4nodePerf':mgnt4nodePerf})