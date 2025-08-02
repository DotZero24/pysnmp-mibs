_u='ciscoSanBaseSvcInterfaceGroup'
_t='ciscoSanBaseSvcNotifsGroup'
_s='ciscoSanBaseSvcNotifControlGroup'
_r='ciscoSanBaseSvcConfigGroup'
_q='ciscoSanBaseSvcClusterNewMaster'
_p='ciscoSanBaseSvcInterfaceDelete'
_o='ciscoSanBaseSvcInterfaceCreate'
_n='cSanBaseSvcClusterInterfaceState'
_m='cSanBaseSvcNotifyEnable'
_l='cSanBaseSvcDevicePortTableLastChanged'
_k='cSanBaseSvcClusterApplication'
_j='cSanBaseSvcDevicePortRowStatus'
_i='cSanBaseSvcDevicePortStorageType'
_h='cSanBaseSvcInterfaceStorageType'
_g='cSanBaseSvcClusterMemberStorageType'
_f='cSanBaseSvcClusterStorageType'
_e='cSanBaseSvcClusterMemberRowStatus'
_d='cSanBaseSvcClusterMemberIsMaster'
_c='cSanBaseSvcClusterRowStatus'
_b='cSanBaseSvcInterfaceRowStatus'
_a='cSanBaseSvcClusterMemberFabric'
_Z='cSanBaseSvcConfigTableLastChanged'
_Y='cSanBaseSvcDevicePortClusterId'
_X='cSanBaseSvcInterfaceClusterId'
_W='cSanBaseSvcInterfaceState'
_V='cSanBaseSvcClusterMemberIsLocal'
_U='cSanBaseSvcClusterState'
_T='cSanBaseSvcClusterInterfaceIndex'
_S='cSanBaseSvcDevicePortName'
_R='cSanBaseSvcInterfaceIndex'
_Q='unknown'
_P='TruthValue'
_O='InetAddress'
_N='cSanBaseSvcClusterName'
_M='cSanBaseSvcClusterMasterInetAddr'
_L='cSanBaseSvcClusterMasterInetAddrType'
_K='cSanBaseSvcClusterMemberInetAddr'
_J='cSanBaseSvcClusterMemberInetAddrType'
_I='SnmpAdminString'
_H='ifDescr'
_G='IF-MIB'
_F='cSanBaseSvcClusterId'
_E='not-accessible'
_D='read-only'
_C='read-create'
_B='CISCO-SAN-BASE-SVC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId')
InterfaceIndex,ifDescr=mibBuilder.importSymbols(_G,'InterfaceIndex',_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_P)
ciscoSanBaseSvcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,702))
if mibBuilder.loadTexts:ciscoSanBaseSvcMIB.setRevisions(('2009-06-11 00:00',))
class CiscoSanBaseSvcInterfaceStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),('initializing',2),('offline',3),('online',4)))
class CiscoSanBaseSvcClusterStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('inactive',2),('degraded',3),('recovery',4),('active',5)))
class CiscoSanBaseSvcClusterIndex(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CiscoSanBaseSvcMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSanBaseSvcMIBNotifs=_CiscoSanBaseSvcMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,702,0))
_CiscoSanBaseSvcMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSanBaseSvcMIBObjects=_CiscoSanBaseSvcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,702,1))
_CSanBaseSvcConfig_ObjectIdentity=ObjectIdentity
cSanBaseSvcConfig=_CSanBaseSvcConfig_ObjectIdentity((1,3,6,1,4,1,9,9,702,1,1))
_CSanBaseSvcClusterTable_Object=MibTable
cSanBaseSvcClusterTable=_CSanBaseSvcClusterTable_Object((1,3,6,1,4,1,9,9,702,1,1,1))
if mibBuilder.loadTexts:cSanBaseSvcClusterTable.setStatus(_A)
_CSanBaseSvcClusterEntry_Object=MibTableRow
cSanBaseSvcClusterEntry=_CSanBaseSvcClusterEntry_Object((1,3,6,1,4,1,9,9,702,1,1,1,1))
cSanBaseSvcClusterEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cSanBaseSvcClusterEntry.setStatus(_A)
_CSanBaseSvcClusterId_Type=CiscoSanBaseSvcClusterIndex
_CSanBaseSvcClusterId_Object=MibTableColumn
cSanBaseSvcClusterId=_CSanBaseSvcClusterId_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,1),_CSanBaseSvcClusterId_Type())
cSanBaseSvcClusterId.setMaxAccess(_E)
if mibBuilder.loadTexts:cSanBaseSvcClusterId.setStatus(_A)
class _CSanBaseSvcClusterName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CSanBaseSvcClusterName_Type.__name__=_I
_CSanBaseSvcClusterName_Object=MibTableColumn
cSanBaseSvcClusterName=_CSanBaseSvcClusterName_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,2),_CSanBaseSvcClusterName_Type())
cSanBaseSvcClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterName.setStatus(_A)
_CSanBaseSvcClusterState_Type=CiscoSanBaseSvcClusterStatus
_CSanBaseSvcClusterState_Object=MibTableColumn
cSanBaseSvcClusterState=_CSanBaseSvcClusterState_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,3),_CSanBaseSvcClusterState_Type())
cSanBaseSvcClusterState.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcClusterState.setStatus(_A)
_CSanBaseSvcClusterMasterInetAddrType_Type=InetAddressType
_CSanBaseSvcClusterMasterInetAddrType_Object=MibTableColumn
cSanBaseSvcClusterMasterInetAddrType=_CSanBaseSvcClusterMasterInetAddrType_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,4),_CSanBaseSvcClusterMasterInetAddrType_Type())
cSanBaseSvcClusterMasterInetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcClusterMasterInetAddrType.setStatus(_A)
_CSanBaseSvcClusterMasterInetAddr_Type=InetAddress
_CSanBaseSvcClusterMasterInetAddr_Object=MibTableColumn
cSanBaseSvcClusterMasterInetAddr=_CSanBaseSvcClusterMasterInetAddr_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,5),_CSanBaseSvcClusterMasterInetAddr_Type())
cSanBaseSvcClusterMasterInetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcClusterMasterInetAddr.setStatus(_A)
_CSanBaseSvcClusterStorageType_Type=StorageType
_CSanBaseSvcClusterStorageType_Object=MibTableColumn
cSanBaseSvcClusterStorageType=_CSanBaseSvcClusterStorageType_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,6),_CSanBaseSvcClusterStorageType_Type())
cSanBaseSvcClusterStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterStorageType.setStatus(_A)
_CSanBaseSvcClusterRowStatus_Type=RowStatus
_CSanBaseSvcClusterRowStatus_Object=MibTableColumn
cSanBaseSvcClusterRowStatus=_CSanBaseSvcClusterRowStatus_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,7),_CSanBaseSvcClusterRowStatus_Type())
cSanBaseSvcClusterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterRowStatus.setStatus(_A)
_CSanBaseSvcClusterApplication_Type=SnmpAdminString
_CSanBaseSvcClusterApplication_Object=MibTableColumn
cSanBaseSvcClusterApplication=_CSanBaseSvcClusterApplication_Object((1,3,6,1,4,1,9,9,702,1,1,1,1,8),_CSanBaseSvcClusterApplication_Type())
cSanBaseSvcClusterApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterApplication.setStatus(_A)
_CSanBaseSvcClusterMembersTable_Object=MibTable
cSanBaseSvcClusterMembersTable=_CSanBaseSvcClusterMembersTable_Object((1,3,6,1,4,1,9,9,702,1,1,2))
if mibBuilder.loadTexts:cSanBaseSvcClusterMembersTable.setStatus(_A)
_CSanBaseSvcClusterMembersEntry_Object=MibTableRow
cSanBaseSvcClusterMembersEntry=_CSanBaseSvcClusterMembersEntry_Object((1,3,6,1,4,1,9,9,702,1,1,2,1))
cSanBaseSvcClusterMembersEntry.setIndexNames((0,_B,_F),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:cSanBaseSvcClusterMembersEntry.setStatus(_A)
_CSanBaseSvcClusterMemberInetAddrType_Type=InetAddressType
_CSanBaseSvcClusterMemberInetAddrType_Object=MibTableColumn
cSanBaseSvcClusterMemberInetAddrType=_CSanBaseSvcClusterMemberInetAddrType_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,1),_CSanBaseSvcClusterMemberInetAddrType_Type())
cSanBaseSvcClusterMemberInetAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberInetAddrType.setStatus(_A)
class _CSanBaseSvcClusterMemberInetAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CSanBaseSvcClusterMemberInetAddr_Type.__name__=_O
_CSanBaseSvcClusterMemberInetAddr_Object=MibTableColumn
cSanBaseSvcClusterMemberInetAddr=_CSanBaseSvcClusterMemberInetAddr_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,2),_CSanBaseSvcClusterMemberInetAddr_Type())
cSanBaseSvcClusterMemberInetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberInetAddr.setStatus(_A)
class _CSanBaseSvcClusterMemberFabric_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CSanBaseSvcClusterMemberFabric_Type.__name__=_I
_CSanBaseSvcClusterMemberFabric_Object=MibTableColumn
cSanBaseSvcClusterMemberFabric=_CSanBaseSvcClusterMemberFabric_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,3),_CSanBaseSvcClusterMemberFabric_Type())
cSanBaseSvcClusterMemberFabric.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberFabric.setStatus(_A)
_CSanBaseSvcClusterMemberIsLocal_Type=TruthValue
_CSanBaseSvcClusterMemberIsLocal_Object=MibTableColumn
cSanBaseSvcClusterMemberIsLocal=_CSanBaseSvcClusterMemberIsLocal_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,4),_CSanBaseSvcClusterMemberIsLocal_Type())
cSanBaseSvcClusterMemberIsLocal.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberIsLocal.setStatus(_A)
_CSanBaseSvcClusterMemberIsMaster_Type=TruthValue
_CSanBaseSvcClusterMemberIsMaster_Object=MibTableColumn
cSanBaseSvcClusterMemberIsMaster=_CSanBaseSvcClusterMemberIsMaster_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,5),_CSanBaseSvcClusterMemberIsMaster_Type())
cSanBaseSvcClusterMemberIsMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberIsMaster.setStatus(_A)
_CSanBaseSvcClusterMemberStorageType_Type=StorageType
_CSanBaseSvcClusterMemberStorageType_Object=MibTableColumn
cSanBaseSvcClusterMemberStorageType=_CSanBaseSvcClusterMemberStorageType_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,6),_CSanBaseSvcClusterMemberStorageType_Type())
cSanBaseSvcClusterMemberStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberStorageType.setStatus(_A)
_CSanBaseSvcClusterMemberRowStatus_Type=RowStatus
_CSanBaseSvcClusterMemberRowStatus_Object=MibTableColumn
cSanBaseSvcClusterMemberRowStatus=_CSanBaseSvcClusterMemberRowStatus_Object((1,3,6,1,4,1,9,9,702,1,1,2,1,7),_CSanBaseSvcClusterMemberRowStatus_Type())
cSanBaseSvcClusterMemberRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberRowStatus.setStatus(_A)
_CSanBaseSvcInterfaceTable_Object=MibTable
cSanBaseSvcInterfaceTable=_CSanBaseSvcInterfaceTable_Object((1,3,6,1,4,1,9,9,702,1,1,3))
if mibBuilder.loadTexts:cSanBaseSvcInterfaceTable.setStatus(_A)
_CSanBaseSvcInterfaceEntry_Object=MibTableRow
cSanBaseSvcInterfaceEntry=_CSanBaseSvcInterfaceEntry_Object((1,3,6,1,4,1,9,9,702,1,1,3,1))
cSanBaseSvcInterfaceEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:cSanBaseSvcInterfaceEntry.setStatus(_A)
_CSanBaseSvcInterfaceIndex_Type=InterfaceIndex
_CSanBaseSvcInterfaceIndex_Object=MibTableColumn
cSanBaseSvcInterfaceIndex=_CSanBaseSvcInterfaceIndex_Object((1,3,6,1,4,1,9,9,702,1,1,3,1,1),_CSanBaseSvcInterfaceIndex_Type())
cSanBaseSvcInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cSanBaseSvcInterfaceIndex.setStatus(_A)
_CSanBaseSvcInterfaceState_Type=CiscoSanBaseSvcInterfaceStatus
_CSanBaseSvcInterfaceState_Object=MibTableColumn
cSanBaseSvcInterfaceState=_CSanBaseSvcInterfaceState_Object((1,3,6,1,4,1,9,9,702,1,1,3,1,2),_CSanBaseSvcInterfaceState_Type())
cSanBaseSvcInterfaceState.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcInterfaceState.setStatus(_A)
_CSanBaseSvcInterfaceClusterId_Type=CiscoSanBaseSvcClusterIndex
_CSanBaseSvcInterfaceClusterId_Object=MibTableColumn
cSanBaseSvcInterfaceClusterId=_CSanBaseSvcInterfaceClusterId_Object((1,3,6,1,4,1,9,9,702,1,1,3,1,3),_CSanBaseSvcInterfaceClusterId_Type())
cSanBaseSvcInterfaceClusterId.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcInterfaceClusterId.setStatus(_A)
_CSanBaseSvcInterfaceStorageType_Type=StorageType
_CSanBaseSvcInterfaceStorageType_Object=MibTableColumn
cSanBaseSvcInterfaceStorageType=_CSanBaseSvcInterfaceStorageType_Object((1,3,6,1,4,1,9,9,702,1,1,3,1,4),_CSanBaseSvcInterfaceStorageType_Type())
cSanBaseSvcInterfaceStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcInterfaceStorageType.setStatus(_A)
_CSanBaseSvcInterfaceRowStatus_Type=RowStatus
_CSanBaseSvcInterfaceRowStatus_Object=MibTableColumn
cSanBaseSvcInterfaceRowStatus=_CSanBaseSvcInterfaceRowStatus_Object((1,3,6,1,4,1,9,9,702,1,1,3,1,5),_CSanBaseSvcInterfaceRowStatus_Type())
cSanBaseSvcInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcInterfaceRowStatus.setStatus(_A)
_CSanBaseSvcDevicePortTable_Object=MibTable
cSanBaseSvcDevicePortTable=_CSanBaseSvcDevicePortTable_Object((1,3,6,1,4,1,9,9,702,1,1,4))
if mibBuilder.loadTexts:cSanBaseSvcDevicePortTable.setStatus(_A)
_CSanBaseSvcDevicePortEntry_Object=MibTableRow
cSanBaseSvcDevicePortEntry=_CSanBaseSvcDevicePortEntry_Object((1,3,6,1,4,1,9,9,702,1,1,4,1))
cSanBaseSvcDevicePortEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:cSanBaseSvcDevicePortEntry.setStatus(_A)
_CSanBaseSvcDevicePortName_Type=FcNameId
_CSanBaseSvcDevicePortName_Object=MibTableColumn
cSanBaseSvcDevicePortName=_CSanBaseSvcDevicePortName_Object((1,3,6,1,4,1,9,9,702,1,1,4,1,1),_CSanBaseSvcDevicePortName_Type())
cSanBaseSvcDevicePortName.setMaxAccess(_E)
if mibBuilder.loadTexts:cSanBaseSvcDevicePortName.setStatus(_A)
_CSanBaseSvcDevicePortClusterId_Type=CiscoSanBaseSvcClusterIndex
_CSanBaseSvcDevicePortClusterId_Object=MibTableColumn
cSanBaseSvcDevicePortClusterId=_CSanBaseSvcDevicePortClusterId_Object((1,3,6,1,4,1,9,9,702,1,1,4,1,2),_CSanBaseSvcDevicePortClusterId_Type())
cSanBaseSvcDevicePortClusterId.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcDevicePortClusterId.setStatus(_A)
_CSanBaseSvcDevicePortStorageType_Type=StorageType
_CSanBaseSvcDevicePortStorageType_Object=MibTableColumn
cSanBaseSvcDevicePortStorageType=_CSanBaseSvcDevicePortStorageType_Object((1,3,6,1,4,1,9,9,702,1,1,4,1,3),_CSanBaseSvcDevicePortStorageType_Type())
cSanBaseSvcDevicePortStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcDevicePortStorageType.setStatus(_A)
_CSanBaseSvcDevicePortRowStatus_Type=RowStatus
_CSanBaseSvcDevicePortRowStatus_Object=MibTableColumn
cSanBaseSvcDevicePortRowStatus=_CSanBaseSvcDevicePortRowStatus_Object((1,3,6,1,4,1,9,9,702,1,1,4,1,4),_CSanBaseSvcDevicePortRowStatus_Type())
cSanBaseSvcDevicePortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cSanBaseSvcDevicePortRowStatus.setStatus(_A)
_CSanBaseSvcConfigTableLastChanged_Type=TimeStamp
_CSanBaseSvcConfigTableLastChanged_Object=MibScalar
cSanBaseSvcConfigTableLastChanged=_CSanBaseSvcConfigTableLastChanged_Object((1,3,6,1,4,1,9,9,702,1,1,5),_CSanBaseSvcConfigTableLastChanged_Type())
cSanBaseSvcConfigTableLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcConfigTableLastChanged.setStatus(_A)
_CSanBaseSvcDevicePortTableLastChanged_Type=TimeStamp
_CSanBaseSvcDevicePortTableLastChanged_Object=MibScalar
cSanBaseSvcDevicePortTableLastChanged=_CSanBaseSvcDevicePortTableLastChanged_Object((1,3,6,1,4,1,9,9,702,1,1,6),_CSanBaseSvcDevicePortTableLastChanged_Type())
cSanBaseSvcDevicePortTableLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcDevicePortTableLastChanged.setStatus(_A)
class _CSanBaseSvcNotifyEnable_Type(TruthValue):defaultValue=1
_CSanBaseSvcNotifyEnable_Type.__name__=_P
_CSanBaseSvcNotifyEnable_Object=MibScalar
cSanBaseSvcNotifyEnable=_CSanBaseSvcNotifyEnable_Object((1,3,6,1,4,1,9,9,702,1,1,7),_CSanBaseSvcNotifyEnable_Type())
cSanBaseSvcNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cSanBaseSvcNotifyEnable.setStatus(_A)
_CSanBaseSvcInterface_ObjectIdentity=ObjectIdentity
cSanBaseSvcInterface=_CSanBaseSvcInterface_ObjectIdentity((1,3,6,1,4,1,9,9,702,1,2))
_CSanBaseSvcClusterMemberIfTable_Object=MibTable
cSanBaseSvcClusterMemberIfTable=_CSanBaseSvcClusterMemberIfTable_Object((1,3,6,1,4,1,9,9,702,1,2,1))
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberIfTable.setStatus(_A)
_CSanBaseSvcClusterMemberIfEntry_Object=MibTableRow
cSanBaseSvcClusterMemberIfEntry=_CSanBaseSvcClusterMemberIfEntry_Object((1,3,6,1,4,1,9,9,702,1,2,1,1))
cSanBaseSvcClusterMemberIfEntry.setIndexNames((0,_B,_F),(0,_B,_J),(0,_B,_K),(0,_B,_T))
if mibBuilder.loadTexts:cSanBaseSvcClusterMemberIfEntry.setStatus(_A)
_CSanBaseSvcClusterInterfaceIndex_Type=InterfaceIndex
_CSanBaseSvcClusterInterfaceIndex_Object=MibTableColumn
cSanBaseSvcClusterInterfaceIndex=_CSanBaseSvcClusterInterfaceIndex_Object((1,3,6,1,4,1,9,9,702,1,2,1,1,1),_CSanBaseSvcClusterInterfaceIndex_Type())
cSanBaseSvcClusterInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cSanBaseSvcClusterInterfaceIndex.setStatus(_A)
_CSanBaseSvcClusterInterfaceState_Type=CiscoSanBaseSvcInterfaceStatus
_CSanBaseSvcClusterInterfaceState_Object=MibTableColumn
cSanBaseSvcClusterInterfaceState=_CSanBaseSvcClusterInterfaceState_Object((1,3,6,1,4,1,9,9,702,1,2,1,1,2),_CSanBaseSvcClusterInterfaceState_Type())
cSanBaseSvcClusterInterfaceState.setMaxAccess(_D)
if mibBuilder.loadTexts:cSanBaseSvcClusterInterfaceState.setStatus(_A)
_CiscoSanBaseSvcMIBConform_ObjectIdentity=ObjectIdentity
ciscoSanBaseSvcMIBConform=_CiscoSanBaseSvcMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,702,2))
_CiscoSanBaseSvcMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSanBaseSvcMIBCompliances=_CiscoSanBaseSvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,702,2,1))
_CiscoSanBaseSvcMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSanBaseSvcMIBGroups=_CiscoSanBaseSvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,702,2,2))
ciscoSanBaseSvcConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,702,2,2,1))
ciscoSanBaseSvcConfigGroup.setObjects(*((_B,_U),(_B,_L),(_B,_M),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_N),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:ciscoSanBaseSvcConfigGroup.setStatus(_A)
ciscoSanBaseSvcNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,702,2,2,2))
ciscoSanBaseSvcNotifControlGroup.setObjects((_B,_m))
if mibBuilder.loadTexts:ciscoSanBaseSvcNotifControlGroup.setStatus(_A)
ciscoSanBaseSvcInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,702,2,2,4))
ciscoSanBaseSvcInterfaceGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:ciscoSanBaseSvcInterfaceGroup.setStatus(_A)
ciscoSanBaseSvcInterfaceCreate=NotificationType((1,3,6,1,4,1,9,9,702,0,1))
ciscoSanBaseSvcInterfaceCreate.setObjects((_G,_H))
if mibBuilder.loadTexts:ciscoSanBaseSvcInterfaceCreate.setStatus(_A)
ciscoSanBaseSvcInterfaceDelete=NotificationType((1,3,6,1,4,1,9,9,702,0,2))
ciscoSanBaseSvcInterfaceDelete.setObjects((_G,_H))
if mibBuilder.loadTexts:ciscoSanBaseSvcInterfaceDelete.setStatus(_A)
ciscoSanBaseSvcClusterNewMaster=NotificationType((1,3,6,1,4,1,9,9,702,0,3))
ciscoSanBaseSvcClusterNewMaster.setObjects(*((_B,_N),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ciscoSanBaseSvcClusterNewMaster.setStatus(_A)
ciscoSanBaseSvcNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,702,2,2,3))
ciscoSanBaseSvcNotifsGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoSanBaseSvcNotifsGroup.setStatus(_A)
ciscoSanBaseSvcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,702,2,1,1))
ciscoSanBaseSvcMIBCompliance.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoSanBaseSvcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoSanBaseSvcInterfaceStatus':CiscoSanBaseSvcInterfaceStatus,'CiscoSanBaseSvcClusterStatus':CiscoSanBaseSvcClusterStatus,'CiscoSanBaseSvcClusterIndex':CiscoSanBaseSvcClusterIndex,'ciscoSanBaseSvcMIB':ciscoSanBaseSvcMIB,'ciscoSanBaseSvcMIBNotifs':ciscoSanBaseSvcMIBNotifs,_o:ciscoSanBaseSvcInterfaceCreate,_p:ciscoSanBaseSvcInterfaceDelete,_q:ciscoSanBaseSvcClusterNewMaster,'ciscoSanBaseSvcMIBObjects':ciscoSanBaseSvcMIBObjects,'cSanBaseSvcConfig':cSanBaseSvcConfig,'cSanBaseSvcClusterTable':cSanBaseSvcClusterTable,'cSanBaseSvcClusterEntry':cSanBaseSvcClusterEntry,_F:cSanBaseSvcClusterId,_N:cSanBaseSvcClusterName,_U:cSanBaseSvcClusterState,_L:cSanBaseSvcClusterMasterInetAddrType,_M:cSanBaseSvcClusterMasterInetAddr,_f:cSanBaseSvcClusterStorageType,_c:cSanBaseSvcClusterRowStatus,_k:cSanBaseSvcClusterApplication,'cSanBaseSvcClusterMembersTable':cSanBaseSvcClusterMembersTable,'cSanBaseSvcClusterMembersEntry':cSanBaseSvcClusterMembersEntry,_J:cSanBaseSvcClusterMemberInetAddrType,_K:cSanBaseSvcClusterMemberInetAddr,_a:cSanBaseSvcClusterMemberFabric,_V:cSanBaseSvcClusterMemberIsLocal,_d:cSanBaseSvcClusterMemberIsMaster,_g:cSanBaseSvcClusterMemberStorageType,_e:cSanBaseSvcClusterMemberRowStatus,'cSanBaseSvcInterfaceTable':cSanBaseSvcInterfaceTable,'cSanBaseSvcInterfaceEntry':cSanBaseSvcInterfaceEntry,_R:cSanBaseSvcInterfaceIndex,_W:cSanBaseSvcInterfaceState,_X:cSanBaseSvcInterfaceClusterId,_h:cSanBaseSvcInterfaceStorageType,_b:cSanBaseSvcInterfaceRowStatus,'cSanBaseSvcDevicePortTable':cSanBaseSvcDevicePortTable,'cSanBaseSvcDevicePortEntry':cSanBaseSvcDevicePortEntry,_S:cSanBaseSvcDevicePortName,_Y:cSanBaseSvcDevicePortClusterId,_i:cSanBaseSvcDevicePortStorageType,_j:cSanBaseSvcDevicePortRowStatus,_Z:cSanBaseSvcConfigTableLastChanged,_l:cSanBaseSvcDevicePortTableLastChanged,_m:cSanBaseSvcNotifyEnable,'cSanBaseSvcInterface':cSanBaseSvcInterface,'cSanBaseSvcClusterMemberIfTable':cSanBaseSvcClusterMemberIfTable,'cSanBaseSvcClusterMemberIfEntry':cSanBaseSvcClusterMemberIfEntry,_T:cSanBaseSvcClusterInterfaceIndex,_n:cSanBaseSvcClusterInterfaceState,'ciscoSanBaseSvcMIBConform':ciscoSanBaseSvcMIBConform,'ciscoSanBaseSvcMIBCompliances':ciscoSanBaseSvcMIBCompliances,'ciscoSanBaseSvcMIBCompliance':ciscoSanBaseSvcMIBCompliance,'ciscoSanBaseSvcMIBGroups':ciscoSanBaseSvcMIBGroups,_r:ciscoSanBaseSvcConfigGroup,_s:ciscoSanBaseSvcNotifControlGroup,_t:ciscoSanBaseSvcNotifsGroup,_u:ciscoSanBaseSvcInterfaceGroup})