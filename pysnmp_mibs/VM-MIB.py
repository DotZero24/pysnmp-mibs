_Af='vmBulkNotificationOptionalGroup'
_Ae='vmBulkNotificationsVariablesGroup'
_Ad='vmPerVMNotificationOptionalGroup'
_Ac='vmBulkDeleted'
_Ab='vmBulkCrashed'
_Aa='vmBulkMigrating'
_AZ='vmBulkResuming'
_AY='vmBulkSuspended'
_AX='vmBulkSuspending'
_AW='vmBulkPaused'
_AV='vmBulkShutdown'
_AU='vmBulkShuttingdown'
_AT='vmBulkRunning'
_AS='vmDeleted'
_AR='vmCrashed'
_AQ='vmMigrating'
_AP='vmResuming'
_AO='vmSuspended'
_AN='vmSuspending'
_AM='vmShutdown'
_AL='vmShuttingdown'
_AK='vmRunning'
_AJ='vmNetworkPhysAddress'
_AI='vmNetworkModel'
_AH='vmNetworkParent'
_AG='vmNetworkIfIndex'
_AF='vmStorageWriteLatency'
_AE='vmStorageReadLatency'
_AD='vmStorageWriteOctets'
_AC='vmStorageReadOctets'
_AB='vmStorageWriteIOs'
_AA='vmStorageReadIOs'
_A9='vmStorageAllocatedSize'
_A8='vmStorageDefinedSize'
_A7='vmStorageSizeUnit'
_A6='vmStorageMediaTypeString'
_A5='vmStorageMediaType'
_A4='vmStorageAccess'
_A3='vmStorageResourceID'
_A2='vmStorageSourceTypeString'
_A1='vmStorageSourceType'
_A0='vmStorageParent'
_z='vmCpuAffinity'
_y='vmCpuCoreTime'
_x='vmCpuTime'
_w='vmUpTime'
_v='vmMaxMem'
_u='vmMinMem'
_t='vmCurMem'
_s='vmMemUnit'
_r='vmMaxCpuNumber'
_q='vmMinCpuNumber'
_p='vmCurCpuNumber'
_o='vmAutoStart'
_n='vmAdminState'
_m='vmOSType'
_l='vmBulkNotificationsEnabled'
_k='vmPerVMNotificationsEnabled'
_j='vmTableLastChange'
_i='vmNumber'
_h='vmHvUpTime'
_g='vmHvObjectID'
_f='vmHvVersion'
_e='vmHvSoftware'
_d='read-write'
_c='vmNetworkIndex'
_b='vmStorageIndex'
_a='vmStorageVmIndex'
_Z='vmCpuPhysIndex'
_Y='microsecond'
_X='shutdown'
_W='paused'
_V='suspended'
_U='running'
_T='vmNetworkGroup'
_S='vmStorageGroup'
_R='vmCpuAffinityGroup'
_Q='vmCpuGroup'
_P='vmVirtualMachineGroup'
_O='vmHypervisorGroup'
_N='vmPersistent'
_M='vmCpuIndex'
_L='vmIndex'
_K='not-accessible'
_J='unknown'
_I='SnmpAdminString'
_H='vmAffectedVMs'
_G='vmOperState'
_F='vmUUID'
_E='vmName'
_D='Integer32'
_C='read-only'
_B='current'
_A='VM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAStorageMediaType,=mibBuilder.importSymbols('IANA-STORAGE-MEDIA-TYPE-MIB','IANAStorageMediaType')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
UUIDorZero,=mibBuilder.importSymbols('UUID-TC-MIB','UUIDorZero')
vmMIB=ModuleIdentity((1,3,6,1,2,1,236))
if mibBuilder.loadTexts:vmMIB.setRevisions(('2015-10-12 00:00',))
class VirtualMachineIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VirtualMachineIndexOrZero(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class VirtualMachineAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4)))
class VirtualMachineOperState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_J,1),('other',2),('preparing',3),(_U,4),('suspending',5),(_V,6),('resuming',7),(_W,8),('migrating',9),('shuttingdown',10),(_X,11),('crashed',12)))
class VirtualMachineAutoStart(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('enabled',2),('disabled',3)))
class VirtualMachinePersistent(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('persistent',2),('transient',3)))
class VirtualMachineCpuIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VirtualMachineStorageIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VirtualMachineStorageSourceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('other',2),('block',3),('raw',4),('sparse',5),('network',6)))
class VirtualMachineStorageAccess(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('readwrite',2),('readonly',3)))
class VirtualMachineNetworkIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VirtualMachineList(TextualConvention,OctetString):status=_B;displayHint='1x'
_VmNotifications_ObjectIdentity=ObjectIdentity
vmNotifications=_VmNotifications_ObjectIdentity((1,3,6,1,2,1,236,0))
_VmObjects_ObjectIdentity=ObjectIdentity
vmObjects=_VmObjects_ObjectIdentity((1,3,6,1,2,1,236,1))
_VmHypervisor_ObjectIdentity=ObjectIdentity
vmHypervisor=_VmHypervisor_ObjectIdentity((1,3,6,1,2,1,236,1,1))
class _VmHvSoftware_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmHvSoftware_Type.__name__=_I
_VmHvSoftware_Object=MibScalar
vmHvSoftware=_VmHvSoftware_Object((1,3,6,1,2,1,236,1,1,1),_VmHvSoftware_Type())
vmHvSoftware.setMaxAccess(_C)
if mibBuilder.loadTexts:vmHvSoftware.setStatus(_B)
class _VmHvVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmHvVersion_Type.__name__=_I
_VmHvVersion_Object=MibScalar
vmHvVersion=_VmHvVersion_Object((1,3,6,1,2,1,236,1,1,2),_VmHvVersion_Type())
vmHvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vmHvVersion.setStatus(_B)
_VmHvObjectID_Type=ObjectIdentifier
_VmHvObjectID_Object=MibScalar
vmHvObjectID=_VmHvObjectID_Object((1,3,6,1,2,1,236,1,1,3),_VmHvObjectID_Type())
vmHvObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmHvObjectID.setStatus(_B)
_VmHvUpTime_Type=TimeTicks
_VmHvUpTime_Object=MibScalar
vmHvUpTime=_VmHvUpTime_Object((1,3,6,1,2,1,236,1,1,4),_VmHvUpTime_Type())
vmHvUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmHvUpTime.setStatus(_B)
class _VmNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VmNumber_Type.__name__=_D
_VmNumber_Object=MibScalar
vmNumber=_VmNumber_Object((1,3,6,1,2,1,236,1,2),_VmNumber_Type())
vmNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vmNumber.setStatus(_B)
_VmTableLastChange_Type=TimeTicks
_VmTableLastChange_Object=MibScalar
vmTableLastChange=_VmTableLastChange_Object((1,3,6,1,2,1,236,1,3),_VmTableLastChange_Type())
vmTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vmTableLastChange.setStatus(_B)
_VmTable_Object=MibTable
vmTable=_VmTable_Object((1,3,6,1,2,1,236,1,4))
if mibBuilder.loadTexts:vmTable.setStatus(_B)
_VmEntry_Object=MibTableRow
vmEntry=_VmEntry_Object((1,3,6,1,2,1,236,1,4,1))
vmEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:vmEntry.setStatus(_B)
_VmIndex_Type=VirtualMachineIndex
_VmIndex_Object=MibTableColumn
vmIndex=_VmIndex_Object((1,3,6,1,2,1,236,1,4,1,1),_VmIndex_Type())
vmIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vmIndex.setStatus(_B)
class _VmName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmName_Type.__name__=_I
_VmName_Object=MibTableColumn
vmName=_VmName_Object((1,3,6,1,2,1,236,1,4,1,2),_VmName_Type())
vmName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmName.setStatus(_B)
_VmUUID_Type=UUIDorZero
_VmUUID_Object=MibTableColumn
vmUUID=_VmUUID_Object((1,3,6,1,2,1,236,1,4,1,3),_VmUUID_Type())
vmUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmUUID.setStatus(_B)
class _VmOSType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmOSType_Type.__name__=_I
_VmOSType_Object=MibTableColumn
vmOSType=_VmOSType_Object((1,3,6,1,2,1,236,1,4,1,4),_VmOSType_Type())
vmOSType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmOSType.setStatus(_B)
_VmAdminState_Type=VirtualMachineAdminState
_VmAdminState_Object=MibTableColumn
vmAdminState=_VmAdminState_Object((1,3,6,1,2,1,236,1,4,1,5),_VmAdminState_Type())
vmAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vmAdminState.setStatus(_B)
_VmOperState_Type=VirtualMachineOperState
_VmOperState_Object=MibTableColumn
vmOperState=_VmOperState_Object((1,3,6,1,2,1,236,1,4,1,6),_VmOperState_Type())
vmOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vmOperState.setStatus(_B)
_VmAutoStart_Type=VirtualMachineAutoStart
_VmAutoStart_Object=MibTableColumn
vmAutoStart=_VmAutoStart_Object((1,3,6,1,2,1,236,1,4,1,7),_VmAutoStart_Type())
vmAutoStart.setMaxAccess(_C)
if mibBuilder.loadTexts:vmAutoStart.setStatus(_B)
_VmPersistent_Type=VirtualMachinePersistent
_VmPersistent_Object=MibTableColumn
vmPersistent=_VmPersistent_Object((1,3,6,1,2,1,236,1,4,1,8),_VmPersistent_Type())
vmPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:vmPersistent.setStatus(_B)
class _VmCurCpuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VmCurCpuNumber_Type.__name__=_D
_VmCurCpuNumber_Object=MibTableColumn
vmCurCpuNumber=_VmCurCpuNumber_Object((1,3,6,1,2,1,236,1,4,1,9),_VmCurCpuNumber_Type())
vmCurCpuNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vmCurCpuNumber.setStatus(_B)
class _VmMinCpuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_VmMinCpuNumber_Type.__name__=_D
_VmMinCpuNumber_Object=MibTableColumn
vmMinCpuNumber=_VmMinCpuNumber_Object((1,3,6,1,2,1,236,1,4,1,10),_VmMinCpuNumber_Type())
vmMinCpuNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMinCpuNumber.setStatus(_B)
class _VmMaxCpuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_VmMaxCpuNumber_Type.__name__=_D
_VmMaxCpuNumber_Object=MibTableColumn
vmMaxCpuNumber=_VmMaxCpuNumber_Object((1,3,6,1,2,1,236,1,4,1,11),_VmMaxCpuNumber_Type())
vmMaxCpuNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMaxCpuNumber.setStatus(_B)
class _VmMemUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VmMemUnit_Type.__name__=_D
_VmMemUnit_Object=MibTableColumn
vmMemUnit=_VmMemUnit_Object((1,3,6,1,2,1,236,1,4,1,12),_VmMemUnit_Type())
vmMemUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMemUnit.setStatus(_B)
class _VmCurMem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VmCurMem_Type.__name__=_D
_VmCurMem_Object=MibTableColumn
vmCurMem=_VmCurMem_Object((1,3,6,1,2,1,236,1,4,1,13),_VmCurMem_Type())
vmCurMem.setMaxAccess(_C)
if mibBuilder.loadTexts:vmCurMem.setStatus(_B)
class _VmMinMem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_VmMinMem_Type.__name__=_D
_VmMinMem_Object=MibTableColumn
vmMinMem=_VmMinMem_Object((1,3,6,1,2,1,236,1,4,1,14),_VmMinMem_Type())
vmMinMem.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMinMem.setStatus(_B)
class _VmMaxMem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_VmMaxMem_Type.__name__=_D
_VmMaxMem_Object=MibTableColumn
vmMaxMem=_VmMaxMem_Object((1,3,6,1,2,1,236,1,4,1,15),_VmMaxMem_Type())
vmMaxMem.setMaxAccess(_C)
if mibBuilder.loadTexts:vmMaxMem.setStatus(_B)
_VmUpTime_Type=TimeTicks
_VmUpTime_Object=MibTableColumn
vmUpTime=_VmUpTime_Object((1,3,6,1,2,1,236,1,4,1,16),_VmUpTime_Type())
vmUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmUpTime.setStatus(_B)
_VmCpuTime_Type=Counter64
_VmCpuTime_Object=MibTableColumn
vmCpuTime=_VmCpuTime_Object((1,3,6,1,2,1,236,1,4,1,17),_VmCpuTime_Type())
vmCpuTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmCpuTime.setStatus(_B)
if mibBuilder.loadTexts:vmCpuTime.setUnits(_Y)
_VmCpuTable_Object=MibTable
vmCpuTable=_VmCpuTable_Object((1,3,6,1,2,1,236,1,5))
if mibBuilder.loadTexts:vmCpuTable.setStatus(_B)
_VmCpuEntry_Object=MibTableRow
vmCpuEntry=_VmCpuEntry_Object((1,3,6,1,2,1,236,1,5,1))
vmCpuEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:vmCpuEntry.setStatus(_B)
_VmCpuIndex_Type=VirtualMachineCpuIndex
_VmCpuIndex_Object=MibTableColumn
vmCpuIndex=_VmCpuIndex_Object((1,3,6,1,2,1,236,1,5,1,1),_VmCpuIndex_Type())
vmCpuIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vmCpuIndex.setStatus(_B)
_VmCpuCoreTime_Type=Counter64
_VmCpuCoreTime_Object=MibTableColumn
vmCpuCoreTime=_VmCpuCoreTime_Object((1,3,6,1,2,1,236,1,5,1,2),_VmCpuCoreTime_Type())
vmCpuCoreTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmCpuCoreTime.setStatus(_B)
if mibBuilder.loadTexts:vmCpuCoreTime.setUnits(_Y)
_VmCpuAffinityTable_Object=MibTable
vmCpuAffinityTable=_VmCpuAffinityTable_Object((1,3,6,1,2,1,236,1,6))
if mibBuilder.loadTexts:vmCpuAffinityTable.setStatus(_B)
_VmCpuAffinityEntry_Object=MibTableRow
vmCpuAffinityEntry=_VmCpuAffinityEntry_Object((1,3,6,1,2,1,236,1,6,1))
vmCpuAffinityEntry.setIndexNames((0,_A,_L),(0,_A,_M),(0,_A,_Z))
if mibBuilder.loadTexts:vmCpuAffinityEntry.setStatus(_B)
class _VmCpuPhysIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VmCpuPhysIndex_Type.__name__=_D
_VmCpuPhysIndex_Object=MibTableColumn
vmCpuPhysIndex=_VmCpuPhysIndex_Object((1,3,6,1,2,1,236,1,6,1,2),_VmCpuPhysIndex_Type())
vmCpuPhysIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vmCpuPhysIndex.setStatus(_B)
class _VmCpuAffinity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('enable',1),('disable',2)))
_VmCpuAffinity_Type.__name__=_D
_VmCpuAffinity_Object=MibTableColumn
vmCpuAffinity=_VmCpuAffinity_Object((1,3,6,1,2,1,236,1,6,1,3),_VmCpuAffinity_Type())
vmCpuAffinity.setMaxAccess(_C)
if mibBuilder.loadTexts:vmCpuAffinity.setStatus(_B)
_VmStorageTable_Object=MibTable
vmStorageTable=_VmStorageTable_Object((1,3,6,1,2,1,236,1,7))
if mibBuilder.loadTexts:vmStorageTable.setStatus(_B)
_VmStorageEntry_Object=MibTableRow
vmStorageEntry=_VmStorageEntry_Object((1,3,6,1,2,1,236,1,7,1))
vmStorageEntry.setIndexNames((0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:vmStorageEntry.setStatus(_B)
_VmStorageVmIndex_Type=VirtualMachineIndexOrZero
_VmStorageVmIndex_Object=MibTableColumn
vmStorageVmIndex=_VmStorageVmIndex_Object((1,3,6,1,2,1,236,1,7,1,1),_VmStorageVmIndex_Type())
vmStorageVmIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vmStorageVmIndex.setStatus(_B)
_VmStorageIndex_Type=VirtualMachineStorageIndex
_VmStorageIndex_Object=MibTableColumn
vmStorageIndex=_VmStorageIndex_Object((1,3,6,1,2,1,236,1,7,1,2),_VmStorageIndex_Type())
vmStorageIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vmStorageIndex.setStatus(_B)
class _VmStorageParent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VmStorageParent_Type.__name__=_D
_VmStorageParent_Object=MibTableColumn
vmStorageParent=_VmStorageParent_Object((1,3,6,1,2,1,236,1,7,1,3),_VmStorageParent_Type())
vmStorageParent.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageParent.setStatus(_B)
_VmStorageSourceType_Type=VirtualMachineStorageSourceType
_VmStorageSourceType_Object=MibTableColumn
vmStorageSourceType=_VmStorageSourceType_Object((1,3,6,1,2,1,236,1,7,1,4),_VmStorageSourceType_Type())
vmStorageSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageSourceType.setStatus(_B)
class _VmStorageSourceTypeString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmStorageSourceTypeString_Type.__name__=_I
_VmStorageSourceTypeString_Object=MibTableColumn
vmStorageSourceTypeString=_VmStorageSourceTypeString_Object((1,3,6,1,2,1,236,1,7,1,5),_VmStorageSourceTypeString_Type())
vmStorageSourceTypeString.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageSourceTypeString.setStatus(_B)
class _VmStorageResourceID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmStorageResourceID_Type.__name__=_I
_VmStorageResourceID_Object=MibTableColumn
vmStorageResourceID=_VmStorageResourceID_Object((1,3,6,1,2,1,236,1,7,1,6),_VmStorageResourceID_Type())
vmStorageResourceID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageResourceID.setStatus(_B)
_VmStorageAccess_Type=VirtualMachineStorageAccess
_VmStorageAccess_Object=MibTableColumn
vmStorageAccess=_VmStorageAccess_Object((1,3,6,1,2,1,236,1,7,1,7),_VmStorageAccess_Type())
vmStorageAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageAccess.setStatus(_B)
_VmStorageMediaType_Type=IANAStorageMediaType
_VmStorageMediaType_Object=MibTableColumn
vmStorageMediaType=_VmStorageMediaType_Object((1,3,6,1,2,1,236,1,7,1,8),_VmStorageMediaType_Type())
vmStorageMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageMediaType.setStatus(_B)
class _VmStorageMediaTypeString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmStorageMediaTypeString_Type.__name__=_I
_VmStorageMediaTypeString_Object=MibTableColumn
vmStorageMediaTypeString=_VmStorageMediaTypeString_Object((1,3,6,1,2,1,236,1,7,1,9),_VmStorageMediaTypeString_Type())
vmStorageMediaTypeString.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageMediaTypeString.setStatus(_B)
class _VmStorageSizeUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VmStorageSizeUnit_Type.__name__=_D
_VmStorageSizeUnit_Object=MibTableColumn
vmStorageSizeUnit=_VmStorageSizeUnit_Object((1,3,6,1,2,1,236,1,7,1,10),_VmStorageSizeUnit_Type())
vmStorageSizeUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageSizeUnit.setStatus(_B)
class _VmStorageDefinedSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_VmStorageDefinedSize_Type.__name__=_D
_VmStorageDefinedSize_Object=MibTableColumn
vmStorageDefinedSize=_VmStorageDefinedSize_Object((1,3,6,1,2,1,236,1,7,1,11),_VmStorageDefinedSize_Type())
vmStorageDefinedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageDefinedSize.setStatus(_B)
class _VmStorageAllocatedSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_VmStorageAllocatedSize_Type.__name__=_D
_VmStorageAllocatedSize_Object=MibTableColumn
vmStorageAllocatedSize=_VmStorageAllocatedSize_Object((1,3,6,1,2,1,236,1,7,1,12),_VmStorageAllocatedSize_Type())
vmStorageAllocatedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageAllocatedSize.setStatus(_B)
_VmStorageReadIOs_Type=Counter64
_VmStorageReadIOs_Object=MibTableColumn
vmStorageReadIOs=_VmStorageReadIOs_Object((1,3,6,1,2,1,236,1,7,1,13),_VmStorageReadIOs_Type())
vmStorageReadIOs.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageReadIOs.setStatus(_B)
_VmStorageWriteIOs_Type=Counter64
_VmStorageWriteIOs_Object=MibTableColumn
vmStorageWriteIOs=_VmStorageWriteIOs_Object((1,3,6,1,2,1,236,1,7,1,14),_VmStorageWriteIOs_Type())
vmStorageWriteIOs.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageWriteIOs.setStatus(_B)
_VmStorageReadOctets_Type=Counter64
_VmStorageReadOctets_Object=MibTableColumn
vmStorageReadOctets=_VmStorageReadOctets_Object((1,3,6,1,2,1,236,1,7,1,15),_VmStorageReadOctets_Type())
vmStorageReadOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageReadOctets.setStatus(_B)
_VmStorageWriteOctets_Type=Counter64
_VmStorageWriteOctets_Object=MibTableColumn
vmStorageWriteOctets=_VmStorageWriteOctets_Object((1,3,6,1,2,1,236,1,7,1,16),_VmStorageWriteOctets_Type())
vmStorageWriteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageWriteOctets.setStatus(_B)
_VmStorageReadLatency_Type=Counter64
_VmStorageReadLatency_Object=MibTableColumn
vmStorageReadLatency=_VmStorageReadLatency_Object((1,3,6,1,2,1,236,1,7,1,17),_VmStorageReadLatency_Type())
vmStorageReadLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageReadLatency.setStatus(_B)
_VmStorageWriteLatency_Type=Counter64
_VmStorageWriteLatency_Object=MibTableColumn
vmStorageWriteLatency=_VmStorageWriteLatency_Object((1,3,6,1,2,1,236,1,7,1,18),_VmStorageWriteLatency_Type())
vmStorageWriteLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStorageWriteLatency.setStatus(_B)
_VmNetworkTable_Object=MibTable
vmNetworkTable=_VmNetworkTable_Object((1,3,6,1,2,1,236,1,8))
if mibBuilder.loadTexts:vmNetworkTable.setStatus(_B)
_VmNetworkEntry_Object=MibTableRow
vmNetworkEntry=_VmNetworkEntry_Object((1,3,6,1,2,1,236,1,8,1))
vmNetworkEntry.setIndexNames((0,_A,_L),(0,_A,_c))
if mibBuilder.loadTexts:vmNetworkEntry.setStatus(_B)
_VmNetworkIndex_Type=VirtualMachineNetworkIndex
_VmNetworkIndex_Object=MibTableColumn
vmNetworkIndex=_VmNetworkIndex_Object((1,3,6,1,2,1,236,1,8,1,1),_VmNetworkIndex_Type())
vmNetworkIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:vmNetworkIndex.setStatus(_B)
_VmNetworkIfIndex_Type=InterfaceIndexOrZero
_VmNetworkIfIndex_Object=MibTableColumn
vmNetworkIfIndex=_VmNetworkIfIndex_Object((1,3,6,1,2,1,236,1,8,1,2),_VmNetworkIfIndex_Type())
vmNetworkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vmNetworkIfIndex.setStatus(_B)
_VmNetworkParent_Type=InterfaceIndexOrZero
_VmNetworkParent_Object=MibTableColumn
vmNetworkParent=_VmNetworkParent_Object((1,3,6,1,2,1,236,1,8,1,3),_VmNetworkParent_Type())
vmNetworkParent.setMaxAccess(_C)
if mibBuilder.loadTexts:vmNetworkParent.setStatus(_B)
class _VmNetworkModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmNetworkModel_Type.__name__=_I
_VmNetworkModel_Object=MibTableColumn
vmNetworkModel=_VmNetworkModel_Object((1,3,6,1,2,1,236,1,8,1,4),_VmNetworkModel_Type())
vmNetworkModel.setMaxAccess(_C)
if mibBuilder.loadTexts:vmNetworkModel.setStatus(_B)
_VmNetworkPhysAddress_Type=PhysAddress
_VmNetworkPhysAddress_Object=MibTableColumn
vmNetworkPhysAddress=_VmNetworkPhysAddress_Object((1,3,6,1,2,1,236,1,8,1,5),_VmNetworkPhysAddress_Type())
vmNetworkPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vmNetworkPhysAddress.setStatus(_B)
_VmPerVMNotificationsEnabled_Type=TruthValue
_VmPerVMNotificationsEnabled_Object=MibScalar
vmPerVMNotificationsEnabled=_VmPerVMNotificationsEnabled_Object((1,3,6,1,2,1,236,1,9),_VmPerVMNotificationsEnabled_Type())
vmPerVMNotificationsEnabled.setMaxAccess(_d)
if mibBuilder.loadTexts:vmPerVMNotificationsEnabled.setStatus(_B)
_VmBulkNotificationsEnabled_Type=TruthValue
_VmBulkNotificationsEnabled_Object=MibScalar
vmBulkNotificationsEnabled=_VmBulkNotificationsEnabled_Object((1,3,6,1,2,1,236,1,10),_VmBulkNotificationsEnabled_Type())
vmBulkNotificationsEnabled.setMaxAccess(_d)
if mibBuilder.loadTexts:vmBulkNotificationsEnabled.setStatus(_B)
_VmAffectedVMs_Type=VirtualMachineList
_VmAffectedVMs_Object=MibScalar
vmAffectedVMs=_VmAffectedVMs_Object((1,3,6,1,2,1,236,1,11),_VmAffectedVMs_Type())
vmAffectedVMs.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:vmAffectedVMs.setStatus(_B)
_VmConformance_ObjectIdentity=ObjectIdentity
vmConformance=_VmConformance_ObjectIdentity((1,3,6,1,2,1,236,2))
_VmCompliances_ObjectIdentity=ObjectIdentity
vmCompliances=_VmCompliances_ObjectIdentity((1,3,6,1,2,1,236,2,1))
_VmGroups_ObjectIdentity=ObjectIdentity
vmGroups=_VmGroups_ObjectIdentity((1,3,6,1,2,1,236,2,2))
vmHypervisorGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,1))
vmHypervisorGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:vmHypervisorGroup.setStatus(_B)
vmVirtualMachineGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,2))
vmVirtualMachineGroup.setObjects(*((_A,_E),(_A,_F),(_A,_m),(_A,_n),(_A,_G),(_A,_o),(_A,_N),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:vmVirtualMachineGroup.setStatus(_B)
vmCpuGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,3))
vmCpuGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:vmCpuGroup.setStatus(_B)
vmCpuAffinityGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,4))
vmCpuAffinityGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:vmCpuAffinityGroup.setStatus(_B)
vmStorageGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,5))
vmStorageGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:vmStorageGroup.setStatus(_B)
vmNetworkGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,6))
vmNetworkGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:vmNetworkGroup.setStatus(_B)
vmBulkNotificationsVariablesGroup=ObjectGroup((1,3,6,1,2,1,236,2,2,8))
vmBulkNotificationsVariablesGroup.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkNotificationsVariablesGroup.setStatus(_B)
vmRunning=NotificationType((1,3,6,1,2,1,236,0,1))
vmRunning.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmRunning.setStatus(_B)
vmShuttingdown=NotificationType((1,3,6,1,2,1,236,0,2))
vmShuttingdown.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmShuttingdown.setStatus(_B)
vmShutdown=NotificationType((1,3,6,1,2,1,236,0,3))
vmShutdown.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmShutdown.setStatus(_B)
vmPaused=NotificationType((1,3,6,1,2,1,236,0,4))
vmPaused.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmPaused.setStatus(_B)
vmSuspending=NotificationType((1,3,6,1,2,1,236,0,5))
vmSuspending.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmSuspending.setStatus(_B)
vmSuspended=NotificationType((1,3,6,1,2,1,236,0,6))
vmSuspended.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmSuspended.setStatus(_B)
vmResuming=NotificationType((1,3,6,1,2,1,236,0,7))
vmResuming.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmResuming.setStatus(_B)
vmMigrating=NotificationType((1,3,6,1,2,1,236,0,8))
vmMigrating.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmMigrating.setStatus(_B)
vmCrashed=NotificationType((1,3,6,1,2,1,236,0,9))
vmCrashed.setObjects(*((_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmCrashed.setStatus(_B)
vmDeleted=NotificationType((1,3,6,1,2,1,236,0,10))
vmDeleted.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_N)))
if mibBuilder.loadTexts:vmDeleted.setStatus(_B)
vmBulkRunning=NotificationType((1,3,6,1,2,1,236,0,11))
vmBulkRunning.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkRunning.setStatus(_B)
vmBulkShuttingdown=NotificationType((1,3,6,1,2,1,236,0,12))
vmBulkShuttingdown.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkShuttingdown.setStatus(_B)
vmBulkShutdown=NotificationType((1,3,6,1,2,1,236,0,13))
vmBulkShutdown.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkShutdown.setStatus(_B)
vmBulkPaused=NotificationType((1,3,6,1,2,1,236,0,14))
vmBulkPaused.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkPaused.setStatus(_B)
vmBulkSuspending=NotificationType((1,3,6,1,2,1,236,0,15))
vmBulkSuspending.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkSuspending.setStatus(_B)
vmBulkSuspended=NotificationType((1,3,6,1,2,1,236,0,16))
vmBulkSuspended.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkSuspended.setStatus(_B)
vmBulkResuming=NotificationType((1,3,6,1,2,1,236,0,17))
vmBulkResuming.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkResuming.setStatus(_B)
vmBulkMigrating=NotificationType((1,3,6,1,2,1,236,0,18))
vmBulkMigrating.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkMigrating.setStatus(_B)
vmBulkCrashed=NotificationType((1,3,6,1,2,1,236,0,19))
vmBulkCrashed.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkCrashed.setStatus(_B)
vmBulkDeleted=NotificationType((1,3,6,1,2,1,236,0,20))
vmBulkDeleted.setObjects((_A,_H))
if mibBuilder.loadTexts:vmBulkDeleted.setStatus(_B)
vmPerVMNotificationOptionalGroup=NotificationGroup((1,3,6,1,2,1,236,2,2,7))
vmPerVMNotificationOptionalGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,'vmPaused'),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:vmPerVMNotificationOptionalGroup.setStatus(_B)
vmBulkNotificationOptionalGroup=NotificationGroup((1,3,6,1,2,1,236,2,2,9))
vmBulkNotificationOptionalGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:vmBulkNotificationOptionalGroup.setStatus(_B)
vmFullCompliances=ModuleCompliance((1,3,6,1,2,1,236,2,1,1))
vmFullCompliances.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:vmFullCompliances.setStatus(_B)
vmReadOnlyCompliances=ModuleCompliance((1,3,6,1,2,1,236,2,1,2))
vmReadOnlyCompliances.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:vmReadOnlyCompliances.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VirtualMachineIndex':VirtualMachineIndex,'VirtualMachineIndexOrZero':VirtualMachineIndexOrZero,'VirtualMachineAdminState':VirtualMachineAdminState,'VirtualMachineOperState':VirtualMachineOperState,'VirtualMachineAutoStart':VirtualMachineAutoStart,'VirtualMachinePersistent':VirtualMachinePersistent,'VirtualMachineCpuIndex':VirtualMachineCpuIndex,'VirtualMachineStorageIndex':VirtualMachineStorageIndex,'VirtualMachineStorageSourceType':VirtualMachineStorageSourceType,'VirtualMachineStorageAccess':VirtualMachineStorageAccess,'VirtualMachineNetworkIndex':VirtualMachineNetworkIndex,'VirtualMachineList':VirtualMachineList,'vmMIB':vmMIB,'vmNotifications':vmNotifications,_AK:vmRunning,_AL:vmShuttingdown,_AM:vmShutdown,'vmPaused':vmPaused,_AN:vmSuspending,_AO:vmSuspended,_AP:vmResuming,_AQ:vmMigrating,_AR:vmCrashed,_AS:vmDeleted,_AT:vmBulkRunning,_AU:vmBulkShuttingdown,_AV:vmBulkShutdown,_AW:vmBulkPaused,_AX:vmBulkSuspending,_AY:vmBulkSuspended,_AZ:vmBulkResuming,_Aa:vmBulkMigrating,_Ab:vmBulkCrashed,_Ac:vmBulkDeleted,'vmObjects':vmObjects,'vmHypervisor':vmHypervisor,_e:vmHvSoftware,_f:vmHvVersion,_g:vmHvObjectID,_h:vmHvUpTime,_i:vmNumber,_j:vmTableLastChange,'vmTable':vmTable,'vmEntry':vmEntry,_L:vmIndex,_E:vmName,_F:vmUUID,_m:vmOSType,_n:vmAdminState,_G:vmOperState,_o:vmAutoStart,_N:vmPersistent,_p:vmCurCpuNumber,_q:vmMinCpuNumber,_r:vmMaxCpuNumber,_s:vmMemUnit,_t:vmCurMem,_u:vmMinMem,_v:vmMaxMem,_w:vmUpTime,_x:vmCpuTime,'vmCpuTable':vmCpuTable,'vmCpuEntry':vmCpuEntry,_M:vmCpuIndex,_y:vmCpuCoreTime,'vmCpuAffinityTable':vmCpuAffinityTable,'vmCpuAffinityEntry':vmCpuAffinityEntry,_Z:vmCpuPhysIndex,_z:vmCpuAffinity,'vmStorageTable':vmStorageTable,'vmStorageEntry':vmStorageEntry,_a:vmStorageVmIndex,_b:vmStorageIndex,_A0:vmStorageParent,_A1:vmStorageSourceType,_A2:vmStorageSourceTypeString,_A3:vmStorageResourceID,_A4:vmStorageAccess,_A5:vmStorageMediaType,_A6:vmStorageMediaTypeString,_A7:vmStorageSizeUnit,_A8:vmStorageDefinedSize,_A9:vmStorageAllocatedSize,_AA:vmStorageReadIOs,_AB:vmStorageWriteIOs,_AC:vmStorageReadOctets,_AD:vmStorageWriteOctets,_AE:vmStorageReadLatency,_AF:vmStorageWriteLatency,'vmNetworkTable':vmNetworkTable,'vmNetworkEntry':vmNetworkEntry,_c:vmNetworkIndex,_AG:vmNetworkIfIndex,_AH:vmNetworkParent,_AI:vmNetworkModel,_AJ:vmNetworkPhysAddress,_k:vmPerVMNotificationsEnabled,_l:vmBulkNotificationsEnabled,_H:vmAffectedVMs,'vmConformance':vmConformance,'vmCompliances':vmCompliances,'vmFullCompliances':vmFullCompliances,'vmReadOnlyCompliances':vmReadOnlyCompliances,'vmGroups':vmGroups,_O:vmHypervisorGroup,_P:vmVirtualMachineGroup,_Q:vmCpuGroup,_R:vmCpuAffinityGroup,_S:vmStorageGroup,_T:vmNetworkGroup,_Ad:vmPerVMNotificationOptionalGroup,_Ae:vmBulkNotificationsVariablesGroup,_Af:vmBulkNotificationOptionalGroup})