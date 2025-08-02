_l='maintEtherRingSwitchControlPortId'
_k='maintEtherRingSwitchControlRingId'
_j='maintEtherRingLoopDetectClearPortId'
_i='maintEtherRingLoopDetectClearRingId'
_h='provEtherRingEquipmentIndex'
_g='provEtherRingExtraTimerRingIndex'
_f='10 milliseconds'
_e='provEtherRingTimerRingIndex'
_d='IpeEtherRingPortIdOrZero'
_c='provEtherRingRPLPortRingIndex'
_b='provEtherRingMemberVlanRingIndex'
_a='provEtherRingCtrlVlanRingIndex'
_Z='provEtherRingVirtualChannelRingIndex'
_Y='IpeMepIdOrZero'
_X='provEtherRingPortId'
_W='provEtherRingPortRingIndex'
_V='provEtherRingInterConnRingIndex'
_U='provEtherRingIndex'
_T='asEtherRingPortId'
_S='asEtherRingPortRingIndex'
_R='manual'
_Q='forced'
_P='asEtherRingRingIndex'
_O='read-write'
_N='IpeAdminStatus'
_M='IpeEtherRingProtoVersion'
_L='detected'
_K='disabled'
_J='DisplayString'
_I='IpeEnableDisableValue'
_H='none'
_G='read-only'
_F='invalid'
_E='Integer32'
_D='IPE-ETH-RING-MIB'
_C='read-create'
_B='not-accessible'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
class IpeAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('down',1),('up',2)))
class IpeEnableDisableValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_K,1),('enabled',2)))
class IpeEtherRingIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
class IpeEtherRingIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
class IpeEtherRingPortId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
class IpeEtherRingPortIdOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
class IpeEtherRingProtoVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('g8032v1',1),('g8032v2',2)))
class IpeEtherRingVlanIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class IpeMepIdOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
class IpeRingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('major',1),('sub',2)))
class IpeVlanList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_RadioEquipment_ObjectIdentity=ObjectIdentity
radioEquipment=_RadioEquipment_ObjectIdentity((1,3,6,1,4,1,119,2,3,69))
_PasoNeoIpe_common_ObjectIdentity=ObjectIdentity
pasoNeoIpe_common=_PasoNeoIpe_common_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501))
_AlarmStatusGroup_ObjectIdentity=ObjectIdentity
alarmStatusGroup=_AlarmStatusGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,3))
_AsEtherRingGroup_ObjectIdentity=ObjectIdentity
asEtherRingGroup=_AsEtherRingGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,3,39))
_AsEtherRingTable_Object=MibTable
asEtherRingTable=_AsEtherRingTable_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1))
if mibBuilder.loadTexts:asEtherRingTable.setStatus(_A)
_AsEtherRingEntry_Object=MibTableRow
asEtherRingEntry=_AsEtherRingEntry_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1,1))
asEtherRingEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:asEtherRingEntry.setStatus(_A)
_AsEtherRingRingIndex_Type=IpeEtherRingIndex
_AsEtherRingRingIndex_Object=MibTableColumn
asEtherRingRingIndex=_AsEtherRingRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1,1,1),_AsEtherRingRingIndex_Type())
asEtherRingRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:asEtherRingRingIndex.setStatus(_A)
_AsEtherRingNEAddress_Type=IpAddress
_AsEtherRingNEAddress_Object=MibTableColumn
asEtherRingNEAddress=_AsEtherRingNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1,1,2),_AsEtherRingNEAddress_Type())
asEtherRingNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:asEtherRingNEAddress.setStatus(_A)
class _AsEtherRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_F,0),(_K,1),('idle',2),('protection',3),(_Q,4),(_R,5),('pending',6)))
_AsEtherRingState_Type.__name__=_E
_AsEtherRingState_Object=MibTableColumn
asEtherRingState=_AsEtherRingState_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1,1,3),_AsEtherRingState_Type())
asEtherRingState.setMaxAccess(_G)
if mibBuilder.loadTexts:asEtherRingState.setStatus(_A)
class _AsEtherRingCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,0),(_H,1),('localSf',2),('localNr',3),('remoteSf',4),('remoteNr',5),('localFs',6),('localMs',7),('remoteFs',8),('remoteMs',9)))
_AsEtherRingCause_Type.__name__=_E
_AsEtherRingCause_Object=MibTableColumn
asEtherRingCause=_AsEtherRingCause_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1,1,4),_AsEtherRingCause_Type())
asEtherRingCause.setMaxAccess(_G)
if mibBuilder.loadTexts:asEtherRingCause.setStatus(_A)
class _AsEtherRingMultiRplOwnerDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_L,2)))
_AsEtherRingMultiRplOwnerDetect_Type.__name__=_E
_AsEtherRingMultiRplOwnerDetect_Object=MibTableColumn
asEtherRingMultiRplOwnerDetect=_AsEtherRingMultiRplOwnerDetect_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,1,1,5),_AsEtherRingMultiRplOwnerDetect_Type())
asEtherRingMultiRplOwnerDetect.setMaxAccess(_G)
if mibBuilder.loadTexts:asEtherRingMultiRplOwnerDetect.setStatus(_A)
_AsEtherRingPortTable_Object=MibTable
asEtherRingPortTable=_AsEtherRingPortTable_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2))
if mibBuilder.loadTexts:asEtherRingPortTable.setStatus(_A)
_AsEtherRingPortEntry_Object=MibTableRow
asEtherRingPortEntry=_AsEtherRingPortEntry_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1))
asEtherRingPortEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:asEtherRingPortEntry.setStatus(_A)
_AsEtherRingPortRingIndex_Type=IpeEtherRingIndex
_AsEtherRingPortRingIndex_Object=MibTableColumn
asEtherRingPortRingIndex=_AsEtherRingPortRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1,1),_AsEtherRingPortRingIndex_Type())
asEtherRingPortRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:asEtherRingPortRingIndex.setStatus(_A)
_AsEtherRingPortId_Type=IpeEtherRingPortId
_AsEtherRingPortId_Object=MibTableColumn
asEtherRingPortId=_AsEtherRingPortId_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1,2),_AsEtherRingPortId_Type())
asEtherRingPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:asEtherRingPortId.setStatus(_A)
_AsEtherRingPortNEAddress_Type=IpAddress
_AsEtherRingPortNEAddress_Object=MibTableColumn
asEtherRingPortNEAddress=_AsEtherRingPortNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1,3),_AsEtherRingPortNEAddress_Type())
asEtherRingPortNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:asEtherRingPortNEAddress.setStatus(_A)
class _AsEtherRingPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,0),(_K,1),('initBlocking',2),('rplBlocking',3),('forwarding',4),('signalFail',5),('recovery',6),('waitToRestore',7),('forcedSwitch',8),('manualSwitch',9),('waitToBlock',10)))
_AsEtherRingPortState_Type.__name__=_E
_AsEtherRingPortState_Object=MibTableColumn
asEtherRingPortState=_AsEtherRingPortState_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1,4),_AsEtherRingPortState_Type())
asEtherRingPortState.setMaxAccess(_G)
if mibBuilder.loadTexts:asEtherRingPortState.setStatus(_A)
class _AsEtherRingPortLoopDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_L,2)))
_AsEtherRingPortLoopDetect_Type.__name__=_E
_AsEtherRingPortLoopDetect_Object=MibTableColumn
asEtherRingPortLoopDetect=_AsEtherRingPortLoopDetect_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1,5),_AsEtherRingPortLoopDetect_Type())
asEtherRingPortLoopDetect.setMaxAccess(_G)
if mibBuilder.loadTexts:asEtherRingPortLoopDetect.setStatus(_A)
class _AsEtherRingPortProtoTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_L,2)))
_AsEtherRingPortProtoTimeout_Type.__name__=_E
_AsEtherRingPortProtoTimeout_Object=MibTableColumn
asEtherRingPortProtoTimeout=_AsEtherRingPortProtoTimeout_Object((1,3,6,1,4,1,119,2,3,69,501,3,39,2,1,6),_AsEtherRingPortProtoTimeout_Type())
asEtherRingPortProtoTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:asEtherRingPortProtoTimeout.setStatus(_A)
_ProvisioningGroup_ObjectIdentity=ObjectIdentity
provisioningGroup=_ProvisioningGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,5))
_ProvEtherRingGroup_ObjectIdentity=ObjectIdentity
provEtherRingGroup=_ProvEtherRingGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,5,39))
_ProvEtherRingTable_Object=MibTable
provEtherRingTable=_ProvEtherRingTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1))
if mibBuilder.loadTexts:provEtherRingTable.setStatus(_A)
_ProvEtherRingEntry_Object=MibTableRow
provEtherRingEntry=_ProvEtherRingEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1))
provEtherRingEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:provEtherRingEntry.setStatus(_A)
_ProvEtherRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingIndex_Object=MibTableColumn
provEtherRingIndex=_ProvEtherRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,1),_ProvEtherRingIndex_Type())
provEtherRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingIndex.setStatus(_A)
_ProvEtherRingNEAddress_Type=IpAddress
_ProvEtherRingNEAddress_Object=MibTableColumn
provEtherRingNEAddress=_ProvEtherRingNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,2),_ProvEtherRingNEAddress_Type())
provEtherRingNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingNEAddress.setStatus(_A)
class _ProvEtherRingProtoVersion_Type(IpeEtherRingProtoVersion):defaultValue=2
_ProvEtherRingProtoVersion_Type.__name__=_M
_ProvEtherRingProtoVersion_Object=MibTableColumn
provEtherRingProtoVersion=_ProvEtherRingProtoVersion_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,3),_ProvEtherRingProtoVersion_Type())
provEtherRingProtoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingProtoVersion.setStatus(_A)
class _ProvEtherRingName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProvEtherRingName_Type.__name__=_J
_ProvEtherRingName_Object=MibTableColumn
provEtherRingName=_ProvEtherRingName_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,4),_ProvEtherRingName_Type())
provEtherRingName.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingName.setStatus(_A)
class _ProvEtherRingAdminStatus_Type(IpeAdminStatus):defaultValue=1
_ProvEtherRingAdminStatus_Type.__name__=_N
_ProvEtherRingAdminStatus_Object=MibTableColumn
provEtherRingAdminStatus=_ProvEtherRingAdminStatus_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,5),_ProvEtherRingAdminStatus_Type())
provEtherRingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingAdminStatus.setStatus(_A)
_ProvEtherRingRowStatus_Type=RowStatus
_ProvEtherRingRowStatus_Object=MibTableColumn
provEtherRingRowStatus=_ProvEtherRingRowStatus_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,6),_ProvEtherRingRowStatus_Type())
provEtherRingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingRowStatus.setStatus(_A)
_ProvEtherRingType_Type=IpeRingType
_ProvEtherRingType_Object=MibTableColumn
provEtherRingType=_ProvEtherRingType_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,1,1,7),_ProvEtherRingType_Type())
provEtherRingType.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingType.setStatus(_A)
_ProvEtherRingInterConnTable_Object=MibTable
provEtherRingInterConnTable=_ProvEtherRingInterConnTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2))
if mibBuilder.loadTexts:provEtherRingInterConnTable.setStatus(_A)
_ProvEtherRingInterConnEntry_Object=MibTableRow
provEtherRingInterConnEntry=_ProvEtherRingInterConnEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1))
provEtherRingInterConnEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:provEtherRingInterConnEntry.setStatus(_A)
_ProvEtherRingInterConnRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingInterConnRingIndex_Object=MibTableColumn
provEtherRingInterConnRingIndex=_ProvEtherRingInterConnRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,1),_ProvEtherRingInterConnRingIndex_Type())
provEtherRingInterConnRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingInterConnRingIndex.setStatus(_A)
_ProvEtherRingInterConnNEAddress_Type=IpAddress
_ProvEtherRingInterConnNEAddress_Object=MibTableColumn
provEtherRingInterConnNEAddress=_ProvEtherRingInterConnNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,2),_ProvEtherRingInterConnNEAddress_Type())
provEtherRingInterConnNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingInterConnNEAddress.setStatus(_A)
class _ProvEtherRingInterConnProtoVersion_Type(IpeEtherRingProtoVersion):defaultValue=2
_ProvEtherRingInterConnProtoVersion_Type.__name__=_M
_ProvEtherRingInterConnProtoVersion_Object=MibTableColumn
provEtherRingInterConnProtoVersion=_ProvEtherRingInterConnProtoVersion_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,3),_ProvEtherRingInterConnProtoVersion_Type())
provEtherRingInterConnProtoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingInterConnProtoVersion.setStatus(_A)
_ProvEtherRingInterConnUpperRingIndex_Type=IpeEtherRingIndexOrZero
_ProvEtherRingInterConnUpperRingIndex_Object=MibTableColumn
provEtherRingInterConnUpperRingIndex=_ProvEtherRingInterConnUpperRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,4),_ProvEtherRingInterConnUpperRingIndex_Type())
provEtherRingInterConnUpperRingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingInterConnUpperRingIndex.setStatus(_A)
class _ProvEtherRingInterConnName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProvEtherRingInterConnName_Type.__name__=_J
_ProvEtherRingInterConnName_Object=MibTableColumn
provEtherRingInterConnName=_ProvEtherRingInterConnName_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,5),_ProvEtherRingInterConnName_Type())
provEtherRingInterConnName.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingInterConnName.setStatus(_A)
class _ProvEtherRingInterConnAdminStatus_Type(IpeAdminStatus):defaultValue=1
_ProvEtherRingInterConnAdminStatus_Type.__name__=_N
_ProvEtherRingInterConnAdminStatus_Object=MibTableColumn
provEtherRingInterConnAdminStatus=_ProvEtherRingInterConnAdminStatus_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,6),_ProvEtherRingInterConnAdminStatus_Type())
provEtherRingInterConnAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingInterConnAdminStatus.setStatus(_A)
class _ProvEtherRingInterConnFlushPropagate_Type(IpeEnableDisableValue):defaultValue=2
_ProvEtherRingInterConnFlushPropagate_Type.__name__=_I
_ProvEtherRingInterConnFlushPropagate_Object=MibTableColumn
provEtherRingInterConnFlushPropagate=_ProvEtherRingInterConnFlushPropagate_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,7),_ProvEtherRingInterConnFlushPropagate_Type())
provEtherRingInterConnFlushPropagate.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingInterConnFlushPropagate.setStatus(_A)
_ProvEtherRingInterConnRowStatus_Type=RowStatus
_ProvEtherRingInterConnRowStatus_Object=MibTableColumn
provEtherRingInterConnRowStatus=_ProvEtherRingInterConnRowStatus_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,2,1,8),_ProvEtherRingInterConnRowStatus_Type())
provEtherRingInterConnRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingInterConnRowStatus.setStatus(_A)
_ProvEtherRingPortTable_Object=MibTable
provEtherRingPortTable=_ProvEtherRingPortTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3))
if mibBuilder.loadTexts:provEtherRingPortTable.setStatus(_A)
_ProvEtherRingPortEntry_Object=MibTableRow
provEtherRingPortEntry=_ProvEtherRingPortEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1))
provEtherRingPortEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:provEtherRingPortEntry.setStatus(_A)
_ProvEtherRingPortRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingPortRingIndex_Object=MibTableColumn
provEtherRingPortRingIndex=_ProvEtherRingPortRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1,1),_ProvEtherRingPortRingIndex_Type())
provEtherRingPortRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingPortRingIndex.setStatus(_A)
_ProvEtherRingPortId_Type=IpeEtherRingPortId
_ProvEtherRingPortId_Object=MibTableColumn
provEtherRingPortId=_ProvEtherRingPortId_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1,2),_ProvEtherRingPortId_Type())
provEtherRingPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingPortId.setStatus(_A)
_ProvEtherRingPortNEAddress_Type=IpAddress
_ProvEtherRingPortNEAddress_Object=MibTableColumn
provEtherRingPortNEAddress=_ProvEtherRingPortNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1,3),_ProvEtherRingPortNEAddress_Type())
provEtherRingPortNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingPortNEAddress.setStatus(_A)
_ProvEtherRingPortRowStatus_Type=RowStatus
_ProvEtherRingPortRowStatus_Object=MibTableColumn
provEtherRingPortRowStatus=_ProvEtherRingPortRowStatus_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1,4),_ProvEtherRingPortRowStatus_Type())
provEtherRingPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingPortRowStatus.setStatus(_A)
_ProvEtherRingPortIfIndex_Type=InterfaceIndex
_ProvEtherRingPortIfIndex_Object=MibTableColumn
provEtherRingPortIfIndex=_ProvEtherRingPortIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1,5),_ProvEtherRingPortIfIndex_Type())
provEtherRingPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingPortIfIndex.setStatus(_A)
class _ProvEtherRingPortLocDetectMep_Type(IpeMepIdOrZero):defaultValue=0
_ProvEtherRingPortLocDetectMep_Type.__name__=_Y
_ProvEtherRingPortLocDetectMep_Object=MibTableColumn
provEtherRingPortLocDetectMep=_ProvEtherRingPortLocDetectMep_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,3,1,6),_ProvEtherRingPortLocDetectMep_Type())
provEtherRingPortLocDetectMep.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingPortLocDetectMep.setStatus(_A)
_ProvEtherRingVirtualChannelTable_Object=MibTable
provEtherRingVirtualChannelTable=_ProvEtherRingVirtualChannelTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,4))
if mibBuilder.loadTexts:provEtherRingVirtualChannelTable.setStatus(_A)
_ProvEtherRingVirtualChannelEntry_Object=MibTableRow
provEtherRingVirtualChannelEntry=_ProvEtherRingVirtualChannelEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,4,1))
provEtherRingVirtualChannelEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:provEtherRingVirtualChannelEntry.setStatus(_A)
_ProvEtherRingVirtualChannelRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingVirtualChannelRingIndex_Object=MibTableColumn
provEtherRingVirtualChannelRingIndex=_ProvEtherRingVirtualChannelRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,4,1,1),_ProvEtherRingVirtualChannelRingIndex_Type())
provEtherRingVirtualChannelRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingVirtualChannelRingIndex.setStatus(_A)
_ProvEtherRingVirtualChannelNEAddress_Type=IpAddress
_ProvEtherRingVirtualChannelNEAddress_Object=MibTableColumn
provEtherRingVirtualChannelNEAddress=_ProvEtherRingVirtualChannelNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,4,1,2),_ProvEtherRingVirtualChannelNEAddress_Type())
provEtherRingVirtualChannelNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingVirtualChannelNEAddress.setStatus(_A)
class _ProvEtherRingVirtualChannelEnabled_Type(IpeEnableDisableValue):defaultValue=2
_ProvEtherRingVirtualChannelEnabled_Type.__name__=_I
_ProvEtherRingVirtualChannelEnabled_Object=MibTableColumn
provEtherRingVirtualChannelEnabled=_ProvEtherRingVirtualChannelEnabled_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,4,1,3),_ProvEtherRingVirtualChannelEnabled_Type())
provEtherRingVirtualChannelEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingVirtualChannelEnabled.setStatus(_A)
_ProvEtherRingCtrlVlanTable_Object=MibTable
provEtherRingCtrlVlanTable=_ProvEtherRingCtrlVlanTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5))
if mibBuilder.loadTexts:provEtherRingCtrlVlanTable.setStatus(_A)
_ProvEtherRingCtrlVlanEntry_Object=MibTableRow
provEtherRingCtrlVlanEntry=_ProvEtherRingCtrlVlanEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1))
provEtherRingCtrlVlanEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:provEtherRingCtrlVlanEntry.setStatus(_A)
_ProvEtherRingCtrlVlanRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingCtrlVlanRingIndex_Object=MibTableColumn
provEtherRingCtrlVlanRingIndex=_ProvEtherRingCtrlVlanRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1,1),_ProvEtherRingCtrlVlanRingIndex_Type())
provEtherRingCtrlVlanRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingCtrlVlanRingIndex.setStatus(_A)
_ProvEtherRingCtrlVlanNEAddress_Type=IpAddress
_ProvEtherRingCtrlVlanNEAddress_Object=MibTableColumn
provEtherRingCtrlVlanNEAddress=_ProvEtherRingCtrlVlanNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1,2),_ProvEtherRingCtrlVlanNEAddress_Type())
provEtherRingCtrlVlanNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingCtrlVlanNEAddress.setStatus(_A)
_ProvEtherRingCtrlVlanId_Type=IpeEtherRingVlanIndex
_ProvEtherRingCtrlVlanId_Object=MibTableColumn
provEtherRingCtrlVlanId=_ProvEtherRingCtrlVlanId_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1,3),_ProvEtherRingCtrlVlanId_Type())
provEtherRingCtrlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingCtrlVlanId.setStatus(_A)
class _ProvEtherRingCtrlVlanRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,239))
_ProvEtherRingCtrlVlanRingId_Type.__name__=_E
_ProvEtherRingCtrlVlanRingId_Object=MibTableColumn
provEtherRingCtrlVlanRingId=_ProvEtherRingCtrlVlanRingId_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1,4),_ProvEtherRingCtrlVlanRingId_Type())
provEtherRingCtrlVlanRingId.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingCtrlVlanRingId.setStatus(_A)
class _ProvEtherRingCtrlVlanMegLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ProvEtherRingCtrlVlanMegLevel_Type.__name__=_E
_ProvEtherRingCtrlVlanMegLevel_Object=MibTableColumn
provEtherRingCtrlVlanMegLevel=_ProvEtherRingCtrlVlanMegLevel_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1,5),_ProvEtherRingCtrlVlanMegLevel_Type())
provEtherRingCtrlVlanMegLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingCtrlVlanMegLevel.setStatus(_A)
class _ProvEtherRingCtrlVlanPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ProvEtherRingCtrlVlanPriority_Type.__name__=_E
_ProvEtherRingCtrlVlanPriority_Object=MibTableColumn
provEtherRingCtrlVlanPriority=_ProvEtherRingCtrlVlanPriority_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,5,1,6),_ProvEtherRingCtrlVlanPriority_Type())
provEtherRingCtrlVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingCtrlVlanPriority.setStatus(_A)
_ProvEtherRingMemberVlanTable_Object=MibTable
provEtherRingMemberVlanTable=_ProvEtherRingMemberVlanTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,6))
if mibBuilder.loadTexts:provEtherRingMemberVlanTable.setStatus(_A)
_ProvEtherRingMemberVlanEntry_Object=MibTableRow
provEtherRingMemberVlanEntry=_ProvEtherRingMemberVlanEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,6,1))
provEtherRingMemberVlanEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:provEtherRingMemberVlanEntry.setStatus(_A)
_ProvEtherRingMemberVlanRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingMemberVlanRingIndex_Object=MibTableColumn
provEtherRingMemberVlanRingIndex=_ProvEtherRingMemberVlanRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,6,1,1),_ProvEtherRingMemberVlanRingIndex_Type())
provEtherRingMemberVlanRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingMemberVlanRingIndex.setStatus(_A)
_ProvEtherRingMemberVlanNEAddress_Type=IpAddress
_ProvEtherRingMemberVlanNEAddress_Object=MibTableColumn
provEtherRingMemberVlanNEAddress=_ProvEtherRingMemberVlanNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,6,1,2),_ProvEtherRingMemberVlanNEAddress_Type())
provEtherRingMemberVlanNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingMemberVlanNEAddress.setStatus(_A)
_ProvEtherRingMemberVlanList_Type=IpeVlanList
_ProvEtherRingMemberVlanList_Object=MibTableColumn
provEtherRingMemberVlanList=_ProvEtherRingMemberVlanList_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,6,1,3),_ProvEtherRingMemberVlanList_Type())
provEtherRingMemberVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingMemberVlanList.setStatus(_A)
_ProvEtherRingRPLPortTable_Object=MibTable
provEtherRingRPLPortTable=_ProvEtherRingRPLPortTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7))
if mibBuilder.loadTexts:provEtherRingRPLPortTable.setStatus(_A)
_ProvEtherRingRPLPortEntry_Object=MibTableRow
provEtherRingRPLPortEntry=_ProvEtherRingRPLPortEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7,1))
provEtherRingRPLPortEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:provEtherRingRPLPortEntry.setStatus(_A)
_ProvEtherRingRPLPortRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingRPLPortRingIndex_Object=MibTableColumn
provEtherRingRPLPortRingIndex=_ProvEtherRingRPLPortRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7,1,1),_ProvEtherRingRPLPortRingIndex_Type())
provEtherRingRPLPortRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingRPLPortRingIndex.setStatus(_A)
_ProvEtherRingRPLPortNEAddress_Type=IpAddress
_ProvEtherRingRPLPortNEAddress_Object=MibTableColumn
provEtherRingRPLPortNEAddress=_ProvEtherRingRPLPortNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7,1,2),_ProvEtherRingRPLPortNEAddress_Type())
provEtherRingRPLPortNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingRPLPortNEAddress.setStatus(_A)
class _ProvEtherRingRPLPortEnable_Type(IpeEnableDisableValue):defaultValue=1
_ProvEtherRingRPLPortEnable_Type.__name__=_I
_ProvEtherRingRPLPortEnable_Object=MibTableColumn
provEtherRingRPLPortEnable=_ProvEtherRingRPLPortEnable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7,1,3),_ProvEtherRingRPLPortEnable_Type())
provEtherRingRPLPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingRPLPortEnable.setStatus(_A)
class _ProvEtherRingRPLPortId_Type(IpeEtherRingPortIdOrZero):defaultValue=0
_ProvEtherRingRPLPortId_Type.__name__=_d
_ProvEtherRingRPLPortId_Object=MibTableColumn
provEtherRingRPLPortId=_ProvEtherRingRPLPortId_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7,1,4),_ProvEtherRingRPLPortId_Type())
provEtherRingRPLPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingRPLPortId.setStatus(_A)
class _ProvEtherRingRPLMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('revertive',1),('nonRevertive',2)))
_ProvEtherRingRPLMode_Type.__name__=_E
_ProvEtherRingRPLMode_Object=MibTableColumn
provEtherRingRPLMode=_ProvEtherRingRPLMode_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,7,1,5),_ProvEtherRingRPLMode_Type())
provEtherRingRPLMode.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingRPLMode.setStatus(_A)
_ProvEtherRingTimerTable_Object=MibTable
provEtherRingTimerTable=_ProvEtherRingTimerTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,8))
if mibBuilder.loadTexts:provEtherRingTimerTable.setStatus(_A)
_ProvEtherRingTimerEntry_Object=MibTableRow
provEtherRingTimerEntry=_ProvEtherRingTimerEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,8,1))
provEtherRingTimerEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:provEtherRingTimerEntry.setStatus(_A)
_ProvEtherRingTimerRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingTimerRingIndex_Object=MibTableColumn
provEtherRingTimerRingIndex=_ProvEtherRingTimerRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,8,1,1),_ProvEtherRingTimerRingIndex_Type())
provEtherRingTimerRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingTimerRingIndex.setStatus(_A)
_ProvEtherRingTimerNEAddress_Type=IpAddress
_ProvEtherRingTimerNEAddress_Object=MibTableColumn
provEtherRingTimerNEAddress=_ProvEtherRingTimerNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,8,1,2),_ProvEtherRingTimerNEAddress_Type())
provEtherRingTimerNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingTimerNEAddress.setStatus(_A)
class _ProvEtherRingTimerWtrTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ProvEtherRingTimerWtrTimer_Type.__name__=_E
_ProvEtherRingTimerWtrTimer_Object=MibTableColumn
provEtherRingTimerWtrTimer=_ProvEtherRingTimerWtrTimer_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,8,1,3),_ProvEtherRingTimerWtrTimer_Type())
provEtherRingTimerWtrTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingTimerWtrTimer.setStatus(_A)
if mibBuilder.loadTexts:provEtherRingTimerWtrTimer.setUnits('minutes')
class _ProvEtherRingTimerGrdTimer_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_ProvEtherRingTimerGrdTimer_Type.__name__=_E
_ProvEtherRingTimerGrdTimer_Object=MibTableColumn
provEtherRingTimerGrdTimer=_ProvEtherRingTimerGrdTimer_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,8,1,4),_ProvEtherRingTimerGrdTimer_Type())
provEtherRingTimerGrdTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingTimerGrdTimer.setStatus(_A)
if mibBuilder.loadTexts:provEtherRingTimerGrdTimer.setUnits(_f)
_ProvEtherRingExtraTimerTable_Object=MibTable
provEtherRingExtraTimerTable=_ProvEtherRingExtraTimerTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,9))
if mibBuilder.loadTexts:provEtherRingExtraTimerTable.setStatus(_A)
_ProvEtherRingExtraTimerEntry_Object=MibTableRow
provEtherRingExtraTimerEntry=_ProvEtherRingExtraTimerEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,9,1))
provEtherRingExtraTimerEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:provEtherRingExtraTimerEntry.setStatus(_A)
_ProvEtherRingExtraTimerRingIndex_Type=IpeEtherRingIndex
_ProvEtherRingExtraTimerRingIndex_Object=MibTableColumn
provEtherRingExtraTimerRingIndex=_ProvEtherRingExtraTimerRingIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,9,1,1),_ProvEtherRingExtraTimerRingIndex_Type())
provEtherRingExtraTimerRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingExtraTimerRingIndex.setStatus(_A)
_ProvEtherRingExtraTimerNEAddress_Type=IpAddress
_ProvEtherRingExtraTimerNEAddress_Object=MibTableColumn
provEtherRingExtraTimerNEAddress=_ProvEtherRingExtraTimerNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,9,1,2),_ProvEtherRingExtraTimerNEAddress_Type())
provEtherRingExtraTimerNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingExtraTimerNEAddress.setStatus(_A)
class _ProvEtherRingExtraTimerFlushGrd_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_ProvEtherRingExtraTimerFlushGrd_Type.__name__=_E
_ProvEtherRingExtraTimerFlushGrd_Object=MibTableColumn
provEtherRingExtraTimerFlushGrd=_ProvEtherRingExtraTimerFlushGrd_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,9,1,3),_ProvEtherRingExtraTimerFlushGrd_Type())
provEtherRingExtraTimerFlushGrd.setMaxAccess(_C)
if mibBuilder.loadTexts:provEtherRingExtraTimerFlushGrd.setStatus(_A)
if mibBuilder.loadTexts:provEtherRingExtraTimerFlushGrd.setUnits(_f)
_ProvEtherRingEquipmentTable_Object=MibTable
provEtherRingEquipmentTable=_ProvEtherRingEquipmentTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,10))
if mibBuilder.loadTexts:provEtherRingEquipmentTable.setStatus(_A)
_ProvEtherRingEquipmentEntry_Object=MibTableRow
provEtherRingEquipmentEntry=_ProvEtherRingEquipmentEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,10,1))
provEtherRingEquipmentEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:provEtherRingEquipmentEntry.setStatus(_A)
class _ProvEtherRingEquipmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ProvEtherRingEquipmentIndex_Type.__name__=_E
_ProvEtherRingEquipmentIndex_Object=MibTableColumn
provEtherRingEquipmentIndex=_ProvEtherRingEquipmentIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,10,1,1),_ProvEtherRingEquipmentIndex_Type())
provEtherRingEquipmentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingEquipmentIndex.setStatus(_A)
_ProvEtherRingEquipmentNEAddress_Type=IpAddress
_ProvEtherRingEquipmentNEAddress_Object=MibTableColumn
provEtherRingEquipmentNEAddress=_ProvEtherRingEquipmentNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,10,1,2),_ProvEtherRingEquipmentNEAddress_Type())
provEtherRingEquipmentNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provEtherRingEquipmentNEAddress.setStatus(_A)
class _ProvEtherRingEquipmentEnable_Type(IpeEnableDisableValue):defaultValue=1
_ProvEtherRingEquipmentEnable_Type.__name__=_I
_ProvEtherRingEquipmentEnable_Object=MibTableColumn
provEtherRingEquipmentEnable=_ProvEtherRingEquipmentEnable_Object((1,3,6,1,4,1,119,2,3,69,501,5,39,10,1,3),_ProvEtherRingEquipmentEnable_Type())
provEtherRingEquipmentEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:provEtherRingEquipmentEnable.setStatus(_A)
_MaintenanceGroup_ObjectIdentity=ObjectIdentity
maintenanceGroup=_MaintenanceGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,6))
_MaintEtherRingGroup_ObjectIdentity=ObjectIdentity
maintEtherRingGroup=_MaintEtherRingGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,6,39))
_MaintEtherRingLoopDetectClearTable_Object=MibTable
maintEtherRingLoopDetectClearTable=_MaintEtherRingLoopDetectClearTable_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,1))
if mibBuilder.loadTexts:maintEtherRingLoopDetectClearTable.setStatus(_A)
_MaintEtherRingLoopDetectClearEntry_Object=MibTableRow
maintEtherRingLoopDetectClearEntry=_MaintEtherRingLoopDetectClearEntry_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,1,1))
maintEtherRingLoopDetectClearEntry.setIndexNames((0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:maintEtherRingLoopDetectClearEntry.setStatus(_A)
_MaintEtherRingLoopDetectClearRingId_Type=IpeEtherRingIndex
_MaintEtherRingLoopDetectClearRingId_Object=MibTableColumn
maintEtherRingLoopDetectClearRingId=_MaintEtherRingLoopDetectClearRingId_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,1,1,1),_MaintEtherRingLoopDetectClearRingId_Type())
maintEtherRingLoopDetectClearRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:maintEtherRingLoopDetectClearRingId.setStatus(_A)
_MaintEtherRingLoopDetectClearPortId_Type=IpeEtherRingPortId
_MaintEtherRingLoopDetectClearPortId_Object=MibTableColumn
maintEtherRingLoopDetectClearPortId=_MaintEtherRingLoopDetectClearPortId_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,1,1,2),_MaintEtherRingLoopDetectClearPortId_Type())
maintEtherRingLoopDetectClearPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:maintEtherRingLoopDetectClearPortId.setStatus(_A)
_MaintEtherRingLoopDetectClearNEAddress_Type=IpAddress
_MaintEtherRingLoopDetectClearNEAddress_Object=MibTableColumn
maintEtherRingLoopDetectClearNEAddress=_MaintEtherRingLoopDetectClearNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,1,1,3),_MaintEtherRingLoopDetectClearNEAddress_Type())
maintEtherRingLoopDetectClearNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:maintEtherRingLoopDetectClearNEAddress.setStatus(_A)
class _MaintEtherRingLoopDetectClearCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),('clear',2)))
_MaintEtherRingLoopDetectClearCommand_Type.__name__=_E
_MaintEtherRingLoopDetectClearCommand_Object=MibTableColumn
maintEtherRingLoopDetectClearCommand=_MaintEtherRingLoopDetectClearCommand_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,1,1,4),_MaintEtherRingLoopDetectClearCommand_Type())
maintEtherRingLoopDetectClearCommand.setMaxAccess(_O)
if mibBuilder.loadTexts:maintEtherRingLoopDetectClearCommand.setStatus(_A)
_MaintEtherRingSwitchControlTable_Object=MibTable
maintEtherRingSwitchControlTable=_MaintEtherRingSwitchControlTable_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,2))
if mibBuilder.loadTexts:maintEtherRingSwitchControlTable.setStatus(_A)
_MaintEtherRingSwitchControlEntry_Object=MibTableRow
maintEtherRingSwitchControlEntry=_MaintEtherRingSwitchControlEntry_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,2,1))
maintEtherRingSwitchControlEntry.setIndexNames((0,_D,_k),(0,_D,_l))
if mibBuilder.loadTexts:maintEtherRingSwitchControlEntry.setStatus(_A)
_MaintEtherRingSwitchControlRingId_Type=IpeEtherRingIndex
_MaintEtherRingSwitchControlRingId_Object=MibTableColumn
maintEtherRingSwitchControlRingId=_MaintEtherRingSwitchControlRingId_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,2,1,1),_MaintEtherRingSwitchControlRingId_Type())
maintEtherRingSwitchControlRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:maintEtherRingSwitchControlRingId.setStatus(_A)
_MaintEtherRingSwitchControlPortId_Type=IpeEtherRingPortId
_MaintEtherRingSwitchControlPortId_Object=MibTableColumn
maintEtherRingSwitchControlPortId=_MaintEtherRingSwitchControlPortId_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,2,1,2),_MaintEtherRingSwitchControlPortId_Type())
maintEtherRingSwitchControlPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:maintEtherRingSwitchControlPortId.setStatus(_A)
_MaintEtherRingSwitchControlNEAddress_Type=IpAddress
_MaintEtherRingSwitchControlNEAddress_Object=MibTableColumn
maintEtherRingSwitchControlNEAddress=_MaintEtherRingSwitchControlNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,2,1,3),_MaintEtherRingSwitchControlNEAddress_Type())
maintEtherRingSwitchControlNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:maintEtherRingSwitchControlNEAddress.setStatus(_A)
class _MaintEtherRingSwitchControlCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_H,1),(_Q,2),(_R,3),('clear',4)))
_MaintEtherRingSwitchControlCommand_Type.__name__=_E
_MaintEtherRingSwitchControlCommand_Object=MibTableColumn
maintEtherRingSwitchControlCommand=_MaintEtherRingSwitchControlCommand_Object((1,3,6,1,4,1,119,2,3,69,501,6,39,2,1,4),_MaintEtherRingSwitchControlCommand_Type())
maintEtherRingSwitchControlCommand.setMaxAccess(_O)
if mibBuilder.loadTexts:maintEtherRingSwitchControlCommand.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_N:IpeAdminStatus,_I:IpeEnableDisableValue,'IpeEtherRingIndex':IpeEtherRingIndex,'IpeEtherRingIndexOrZero':IpeEtherRingIndexOrZero,'IpeEtherRingPortId':IpeEtherRingPortId,_d:IpeEtherRingPortIdOrZero,_M:IpeEtherRingProtoVersion,'IpeEtherRingVlanIndex':IpeEtherRingVlanIndex,_Y:IpeMepIdOrZero,'IpeRingType':IpeRingType,'IpeVlanList':IpeVlanList,'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'radioEquipment':radioEquipment,'pasoNeoIpe-common':pasoNeoIpe_common,'alarmStatusGroup':alarmStatusGroup,'asEtherRingGroup':asEtherRingGroup,'asEtherRingTable':asEtherRingTable,'asEtherRingEntry':asEtherRingEntry,_P:asEtherRingRingIndex,'asEtherRingNEAddress':asEtherRingNEAddress,'asEtherRingState':asEtherRingState,'asEtherRingCause':asEtherRingCause,'asEtherRingMultiRplOwnerDetect':asEtherRingMultiRplOwnerDetect,'asEtherRingPortTable':asEtherRingPortTable,'asEtherRingPortEntry':asEtherRingPortEntry,_S:asEtherRingPortRingIndex,_T:asEtherRingPortId,'asEtherRingPortNEAddress':asEtherRingPortNEAddress,'asEtherRingPortState':asEtherRingPortState,'asEtherRingPortLoopDetect':asEtherRingPortLoopDetect,'asEtherRingPortProtoTimeout':asEtherRingPortProtoTimeout,'provisioningGroup':provisioningGroup,'provEtherRingGroup':provEtherRingGroup,'provEtherRingTable':provEtherRingTable,'provEtherRingEntry':provEtherRingEntry,_U:provEtherRingIndex,'provEtherRingNEAddress':provEtherRingNEAddress,'provEtherRingProtoVersion':provEtherRingProtoVersion,'provEtherRingName':provEtherRingName,'provEtherRingAdminStatus':provEtherRingAdminStatus,'provEtherRingRowStatus':provEtherRingRowStatus,'provEtherRingType':provEtherRingType,'provEtherRingInterConnTable':provEtherRingInterConnTable,'provEtherRingInterConnEntry':provEtherRingInterConnEntry,_V:provEtherRingInterConnRingIndex,'provEtherRingInterConnNEAddress':provEtherRingInterConnNEAddress,'provEtherRingInterConnProtoVersion':provEtherRingInterConnProtoVersion,'provEtherRingInterConnUpperRingIndex':provEtherRingInterConnUpperRingIndex,'provEtherRingInterConnName':provEtherRingInterConnName,'provEtherRingInterConnAdminStatus':provEtherRingInterConnAdminStatus,'provEtherRingInterConnFlushPropagate':provEtherRingInterConnFlushPropagate,'provEtherRingInterConnRowStatus':provEtherRingInterConnRowStatus,'provEtherRingPortTable':provEtherRingPortTable,'provEtherRingPortEntry':provEtherRingPortEntry,_W:provEtherRingPortRingIndex,_X:provEtherRingPortId,'provEtherRingPortNEAddress':provEtherRingPortNEAddress,'provEtherRingPortRowStatus':provEtherRingPortRowStatus,'provEtherRingPortIfIndex':provEtherRingPortIfIndex,'provEtherRingPortLocDetectMep':provEtherRingPortLocDetectMep,'provEtherRingVirtualChannelTable':provEtherRingVirtualChannelTable,'provEtherRingVirtualChannelEntry':provEtherRingVirtualChannelEntry,_Z:provEtherRingVirtualChannelRingIndex,'provEtherRingVirtualChannelNEAddress':provEtherRingVirtualChannelNEAddress,'provEtherRingVirtualChannelEnabled':provEtherRingVirtualChannelEnabled,'provEtherRingCtrlVlanTable':provEtherRingCtrlVlanTable,'provEtherRingCtrlVlanEntry':provEtherRingCtrlVlanEntry,_a:provEtherRingCtrlVlanRingIndex,'provEtherRingCtrlVlanNEAddress':provEtherRingCtrlVlanNEAddress,'provEtherRingCtrlVlanId':provEtherRingCtrlVlanId,'provEtherRingCtrlVlanRingId':provEtherRingCtrlVlanRingId,'provEtherRingCtrlVlanMegLevel':provEtherRingCtrlVlanMegLevel,'provEtherRingCtrlVlanPriority':provEtherRingCtrlVlanPriority,'provEtherRingMemberVlanTable':provEtherRingMemberVlanTable,'provEtherRingMemberVlanEntry':provEtherRingMemberVlanEntry,_b:provEtherRingMemberVlanRingIndex,'provEtherRingMemberVlanNEAddress':provEtherRingMemberVlanNEAddress,'provEtherRingMemberVlanList':provEtherRingMemberVlanList,'provEtherRingRPLPortTable':provEtherRingRPLPortTable,'provEtherRingRPLPortEntry':provEtherRingRPLPortEntry,_c:provEtherRingRPLPortRingIndex,'provEtherRingRPLPortNEAddress':provEtherRingRPLPortNEAddress,'provEtherRingRPLPortEnable':provEtherRingRPLPortEnable,'provEtherRingRPLPortId':provEtherRingRPLPortId,'provEtherRingRPLMode':provEtherRingRPLMode,'provEtherRingTimerTable':provEtherRingTimerTable,'provEtherRingTimerEntry':provEtherRingTimerEntry,_e:provEtherRingTimerRingIndex,'provEtherRingTimerNEAddress':provEtherRingTimerNEAddress,'provEtherRingTimerWtrTimer':provEtherRingTimerWtrTimer,'provEtherRingTimerGrdTimer':provEtherRingTimerGrdTimer,'provEtherRingExtraTimerTable':provEtherRingExtraTimerTable,'provEtherRingExtraTimerEntry':provEtherRingExtraTimerEntry,_g:provEtherRingExtraTimerRingIndex,'provEtherRingExtraTimerNEAddress':provEtherRingExtraTimerNEAddress,'provEtherRingExtraTimerFlushGrd':provEtherRingExtraTimerFlushGrd,'provEtherRingEquipmentTable':provEtherRingEquipmentTable,'provEtherRingEquipmentEntry':provEtherRingEquipmentEntry,_h:provEtherRingEquipmentIndex,'provEtherRingEquipmentNEAddress':provEtherRingEquipmentNEAddress,'provEtherRingEquipmentEnable':provEtherRingEquipmentEnable,'maintenanceGroup':maintenanceGroup,'maintEtherRingGroup':maintEtherRingGroup,'maintEtherRingLoopDetectClearTable':maintEtherRingLoopDetectClearTable,'maintEtherRingLoopDetectClearEntry':maintEtherRingLoopDetectClearEntry,_i:maintEtherRingLoopDetectClearRingId,_j:maintEtherRingLoopDetectClearPortId,'maintEtherRingLoopDetectClearNEAddress':maintEtherRingLoopDetectClearNEAddress,'maintEtherRingLoopDetectClearCommand':maintEtherRingLoopDetectClearCommand,'maintEtherRingSwitchControlTable':maintEtherRingSwitchControlTable,'maintEtherRingSwitchControlEntry':maintEtherRingSwitchControlEntry,_k:maintEtherRingSwitchControlRingId,_l:maintEtherRingSwitchControlPortId,'maintEtherRingSwitchControlNEAddress':maintEtherRingSwitchControlNEAddress,'maintEtherRingSwitchControlCommand':maintEtherRingSwitchControlCommand})