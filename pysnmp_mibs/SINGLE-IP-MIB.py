_S='swSingleIPNBMacAddr'
_R='swSingleIPNBReceivedPort'
_Q='swSingleIPGroupMacAddr'
_P='swSingleIPCaSID'
_O='enabled'
_N='disabled'
_M='read-create'
_L='OctetString'
_K='ifIndex'
_J='IF-MIB'
_I='swSingleIPMSTrapMessage'
_H='read-write'
_G='Integer32'
_F='swSingleIPMSMacAddr'
_E='swSingleIPMSID'
_D='DisplayString'
_C='read-only'
_B='SINGLE-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swSingleIPMIB=ModuleIdentity((1,3,6,1,4,1,171,12,8))
_SwSingleIPMgmt_ObjectIdentity=ObjectIdentity
swSingleIPMgmt=_SwSingleIPMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,8,1))
_SwSingleIPInfo_ObjectIdentity=ObjectIdentity
swSingleIPInfo=_SwSingleIPInfo_ObjectIdentity((1,3,6,1,4,1,171,12,8,1,1))
class _SwSingleIPVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPVersion_Type.__name__=_D
_SwSingleIPVersion_Object=MibScalar
swSingleIPVersion=_SwSingleIPVersion_Object((1,3,6,1,4,1,171,12,8,1,1,1),_SwSingleIPVersion_Type())
swSingleIPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPVersion.setStatus(_A)
class _SwSingleIPCapability_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPCapability_Type.__name__=_D
_SwSingleIPCapability_Object=MibScalar
swSingleIPCapability=_SwSingleIPCapability_Object((1,3,6,1,4,1,171,12,8,1,1,2),_SwSingleIPCapability_Type())
swSingleIPCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCapability.setStatus(_A)
class _SwSingleIPPlatform_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPPlatform_Type.__name__=_D
_SwSingleIPPlatform_Object=MibScalar
swSingleIPPlatform=_SwSingleIPPlatform_Object((1,3,6,1,4,1,171,12,8,1,1,3),_SwSingleIPPlatform_Type())
swSingleIPPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPPlatform.setStatus(_A)
_SwSingleIPCtrl_ObjectIdentity=ObjectIdentity
swSingleIPCtrl=_SwSingleIPCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,8,1,2))
class _SwSingleIPAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_N,2),(_O,3)))
_SwSingleIPAdmin_Type.__name__=_G
_SwSingleIPAdmin_Object=MibScalar
swSingleIPAdmin=_SwSingleIPAdmin_Object((1,3,6,1,4,1,171,12,8,1,2,1),_SwSingleIPAdmin_Type())
swSingleIPAdmin.setMaxAccess(_H)
if mibBuilder.loadTexts:swSingleIPAdmin.setStatus(_A)
class _SwSingleIPRoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cs',1),('cas',2),('ms',3)))
_SwSingleIPRoleState_Type.__name__=_G
_SwSingleIPRoleState_Object=MibScalar
swSingleIPRoleState=_SwSingleIPRoleState_Object((1,3,6,1,4,1,171,12,8,1,2,2),_SwSingleIPRoleState_Type())
swSingleIPRoleState.setMaxAccess(_H)
if mibBuilder.loadTexts:swSingleIPRoleState.setStatus(_A)
class _SwSingleIPHoldtime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,255))
_SwSingleIPHoldtime_Type.__name__=_G
_SwSingleIPHoldtime_Object=MibScalar
swSingleIPHoldtime=_SwSingleIPHoldtime_Object((1,3,6,1,4,1,171,12,8,1,2,3),_SwSingleIPHoldtime_Type())
swSingleIPHoldtime.setMaxAccess(_H)
if mibBuilder.loadTexts:swSingleIPHoldtime.setStatus(_A)
class _SwSingleIPTimeInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,90))
_SwSingleIPTimeInterval_Type.__name__=_G
_SwSingleIPTimeInterval_Object=MibScalar
swSingleIPTimeInterval=_SwSingleIPTimeInterval_Object((1,3,6,1,4,1,171,12,8,1,2,4),_SwSingleIPTimeInterval_Type())
swSingleIPTimeInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:swSingleIPTimeInterval.setStatus(_A)
class _SwSingleIPCSGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPCSGroupName_Type.__name__=_D
_SwSingleIPCSGroupName_Object=MibScalar
swSingleIPCSGroupName=_SwSingleIPCSGroupName_Object((1,3,6,1,4,1,171,12,8,1,2,5),_SwSingleIPCSGroupName_Type())
swSingleIPCSGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:swSingleIPCSGroupName.setStatus(_A)
_SwSingleIPTrapMgmt_ObjectIdentity=ObjectIdentity
swSingleIPTrapMgmt=_SwSingleIPTrapMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,8,1,2,6))
class _SwSingleIPTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_N,2)))
_SwSingleIPTrapStatus_Type.__name__=_G
_SwSingleIPTrapStatus_Object=MibScalar
swSingleIPTrapStatus=_SwSingleIPTrapStatus_Object((1,3,6,1,4,1,171,12,8,1,2,6,1),_SwSingleIPTrapStatus_Type())
swSingleIPTrapStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swSingleIPTrapStatus.setStatus(_A)
_SwSingleIPMSTable_Object=MibTable
swSingleIPMSTable=_SwSingleIPMSTable_Object((1,3,6,1,4,1,171,12,8,1,3))
if mibBuilder.loadTexts:swSingleIPMSTable.setStatus(_A)
_SwSingleIPMSEntry_Object=MibTableRow
swSingleIPMSEntry=_SwSingleIPMSEntry_Object((1,3,6,1,4,1,171,12,8,1,3,1))
swSingleIPMSEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:swSingleIPMSEntry.setStatus(_A)
class _SwSingleIPMSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SwSingleIPMSID_Type.__name__=_G
_SwSingleIPMSID_Object=MibTableColumn
swSingleIPMSID=_SwSingleIPMSID_Object((1,3,6,1,4,1,171,12,8,1,3,1,1),_SwSingleIPMSID_Type())
swSingleIPMSID.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSID.setStatus(_A)
class _SwSingleIPMSDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPMSDeviceName_Type.__name__=_D
_SwSingleIPMSDeviceName_Object=MibTableColumn
swSingleIPMSDeviceName=_SwSingleIPMSDeviceName_Object((1,3,6,1,4,1,171,12,8,1,3,1,2),_SwSingleIPMSDeviceName_Type())
swSingleIPMSDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSDeviceName.setStatus(_A)
_SwSingleIPMSMacAddr_Type=MacAddress
_SwSingleIPMSMacAddr_Object=MibTableColumn
swSingleIPMSMacAddr=_SwSingleIPMSMacAddr_Object((1,3,6,1,4,1,171,12,8,1,3,1,3),_SwSingleIPMSMacAddr_Type())
swSingleIPMSMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSMacAddr.setStatus(_A)
class _SwSingleIPMSFirmwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPMSFirmwareVer_Type.__name__=_D
_SwSingleIPMSFirmwareVer_Object=MibTableColumn
swSingleIPMSFirmwareVer=_SwSingleIPMSFirmwareVer_Object((1,3,6,1,4,1,171,12,8,1,3,1,4),_SwSingleIPMSFirmwareVer_Type())
swSingleIPMSFirmwareVer.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSFirmwareVer.setStatus(_A)
class _SwSingleIPMSCapability_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPMSCapability_Type.__name__=_D
_SwSingleIPMSCapability_Object=MibTableColumn
swSingleIPMSCapability=_SwSingleIPMSCapability_Object((1,3,6,1,4,1,171,12,8,1,3,1,5),_SwSingleIPMSCapability_Type())
swSingleIPMSCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSCapability.setStatus(_A)
class _SwSingleIPMSPlatform_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPMSPlatform_Type.__name__=_D
_SwSingleIPMSPlatform_Object=MibTableColumn
swSingleIPMSPlatform=_SwSingleIPMSPlatform_Object((1,3,6,1,4,1,171,12,8,1,3,1,6),_SwSingleIPMSPlatform_Type())
swSingleIPMSPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSPlatform.setStatus(_A)
_SwSingleIPMSHoldtime_Type=Integer32
_SwSingleIPMSHoldtime_Object=MibTableColumn
swSingleIPMSHoldtime=_SwSingleIPMSHoldtime_Object((1,3,6,1,4,1,171,12,8,1,3,1,7),_SwSingleIPMSHoldtime_Type())
swSingleIPMSHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSHoldtime.setStatus(_A)
_SwSingleIPMSCasSource_Type=Integer32
_SwSingleIPMSCasSource_Object=MibTableColumn
swSingleIPMSCasSource=_SwSingleIPMSCasSource_Object((1,3,6,1,4,1,171,12,8,1,3,1,8),_SwSingleIPMSCasSource_Type())
swSingleIPMSCasSource.setMaxAccess(_M)
if mibBuilder.loadTexts:swSingleIPMSCasSource.setStatus(_A)
class _SwSingleIPMSPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SwSingleIPMSPassword_Type.__name__=_L
_SwSingleIPMSPassword_Object=MibTableColumn
swSingleIPMSPassword=_SwSingleIPMSPassword_Object((1,3,6,1,4,1,171,12,8,1,3,1,9),_SwSingleIPMSPassword_Type())
swSingleIPMSPassword.setMaxAccess(_M)
if mibBuilder.loadTexts:swSingleIPMSPassword.setStatus(_A)
_SwSingleIPMSRowStatus_Type=RowStatus
_SwSingleIPMSRowStatus_Object=MibTableColumn
swSingleIPMSRowStatus=_SwSingleIPMSRowStatus_Object((1,3,6,1,4,1,171,12,8,1,3,1,10),_SwSingleIPMSRowStatus_Type())
swSingleIPMSRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:swSingleIPMSRowStatus.setStatus(_A)
_SwSingleIPCaSTable_Object=MibTable
swSingleIPCaSTable=_SwSingleIPCaSTable_Object((1,3,6,1,4,1,171,12,8,1,4))
if mibBuilder.loadTexts:swSingleIPCaSTable.setStatus(_A)
_SwSingleIPCaSEntry_Object=MibTableRow
swSingleIPCaSEntry=_SwSingleIPCaSEntry_Object((1,3,6,1,4,1,171,12,8,1,4,1))
swSingleIPCaSEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:swSingleIPCaSEntry.setStatus(_A)
class _SwSingleIPCaSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwSingleIPCaSID_Type.__name__=_G
_SwSingleIPCaSID_Object=MibTableColumn
swSingleIPCaSID=_SwSingleIPCaSID_Object((1,3,6,1,4,1,171,12,8,1,4,1,1),_SwSingleIPCaSID_Type())
swSingleIPCaSID.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSID.setStatus(_A)
class _SwSingleIPCaSDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPCaSDeviceName_Type.__name__=_D
_SwSingleIPCaSDeviceName_Object=MibTableColumn
swSingleIPCaSDeviceName=_SwSingleIPCaSDeviceName_Object((1,3,6,1,4,1,171,12,8,1,4,1,2),_SwSingleIPCaSDeviceName_Type())
swSingleIPCaSDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSDeviceName.setStatus(_A)
_SwSingleIPCaSMacAddr_Type=MacAddress
_SwSingleIPCaSMacAddr_Object=MibTableColumn
swSingleIPCaSMacAddr=_SwSingleIPCaSMacAddr_Object((1,3,6,1,4,1,171,12,8,1,4,1,3),_SwSingleIPCaSMacAddr_Type())
swSingleIPCaSMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSMacAddr.setStatus(_A)
class _SwSingleIPCaSFirmwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPCaSFirmwareVer_Type.__name__=_D
_SwSingleIPCaSFirmwareVer_Object=MibTableColumn
swSingleIPCaSFirmwareVer=_SwSingleIPCaSFirmwareVer_Object((1,3,6,1,4,1,171,12,8,1,4,1,4),_SwSingleIPCaSFirmwareVer_Type())
swSingleIPCaSFirmwareVer.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSFirmwareVer.setStatus(_A)
class _SwSingleIPCaSCapability_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPCaSCapability_Type.__name__=_D
_SwSingleIPCaSCapability_Object=MibTableColumn
swSingleIPCaSCapability=_SwSingleIPCaSCapability_Object((1,3,6,1,4,1,171,12,8,1,4,1,5),_SwSingleIPCaSCapability_Type())
swSingleIPCaSCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSCapability.setStatus(_A)
class _SwSingleIPCaSPlatform_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPCaSPlatform_Type.__name__=_D
_SwSingleIPCaSPlatform_Object=MibTableColumn
swSingleIPCaSPlatform=_SwSingleIPCaSPlatform_Object((1,3,6,1,4,1,171,12,8,1,4,1,6),_SwSingleIPCaSPlatform_Type())
swSingleIPCaSPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSPlatform.setStatus(_A)
_SwSingleIPCaSHoldtime_Type=Integer32
_SwSingleIPCaSHoldtime_Object=MibTableColumn
swSingleIPCaSHoldtime=_SwSingleIPCaSHoldtime_Object((1,3,6,1,4,1,171,12,8,1,4,1,7),_SwSingleIPCaSHoldtime_Type())
swSingleIPCaSHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPCaSHoldtime.setStatus(_A)
_SwSingleIPGroupTable_Object=MibTable
swSingleIPGroupTable=_SwSingleIPGroupTable_Object((1,3,6,1,4,1,171,12,8,1,5))
if mibBuilder.loadTexts:swSingleIPGroupTable.setStatus(_A)
_SwSingleIPGroupEntry_Object=MibTableRow
swSingleIPGroupEntry=_SwSingleIPGroupEntry_Object((1,3,6,1,4,1,171,12,8,1,5,1))
swSingleIPGroupEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:swSingleIPGroupEntry.setStatus(_A)
_SwSingleIPGroupMacAddr_Type=MacAddress
_SwSingleIPGroupMacAddr_Object=MibTableColumn
swSingleIPGroupMacAddr=_SwSingleIPGroupMacAddr_Object((1,3,6,1,4,1,171,12,8,1,5,1,1),_SwSingleIPGroupMacAddr_Type())
swSingleIPGroupMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupMacAddr.setStatus(_A)
class _SwSingleIPGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPGroupName_Type.__name__=_D
_SwSingleIPGroupName_Object=MibTableColumn
swSingleIPGroupName=_SwSingleIPGroupName_Object((1,3,6,1,4,1,171,12,8,1,5,1,2),_SwSingleIPGroupName_Type())
swSingleIPGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupName.setStatus(_A)
class _SwSingleIPGroupDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPGroupDeviceName_Type.__name__=_D
_SwSingleIPGroupDeviceName_Object=MibTableColumn
swSingleIPGroupDeviceName=_SwSingleIPGroupDeviceName_Object((1,3,6,1,4,1,171,12,8,1,5,1,3),_SwSingleIPGroupDeviceName_Type())
swSingleIPGroupDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupDeviceName.setStatus(_A)
_SwSingleIPGroupMSNumber_Type=Integer32
_SwSingleIPGroupMSNumber_Object=MibTableColumn
swSingleIPGroupMSNumber=_SwSingleIPGroupMSNumber_Object((1,3,6,1,4,1,171,12,8,1,5,1,4),_SwSingleIPGroupMSNumber_Type())
swSingleIPGroupMSNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupMSNumber.setStatus(_A)
class _SwSingleIPGroupFirmwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPGroupFirmwareVer_Type.__name__=_D
_SwSingleIPGroupFirmwareVer_Object=MibTableColumn
swSingleIPGroupFirmwareVer=_SwSingleIPGroupFirmwareVer_Object((1,3,6,1,4,1,171,12,8,1,5,1,5),_SwSingleIPGroupFirmwareVer_Type())
swSingleIPGroupFirmwareVer.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupFirmwareVer.setStatus(_A)
class _SwSingleIPGroupCapability_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPGroupCapability_Type.__name__=_D
_SwSingleIPGroupCapability_Object=MibTableColumn
swSingleIPGroupCapability=_SwSingleIPGroupCapability_Object((1,3,6,1,4,1,171,12,8,1,5,1,6),_SwSingleIPGroupCapability_Type())
swSingleIPGroupCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupCapability.setStatus(_A)
class _SwSingleIPGroupPlatform_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwSingleIPGroupPlatform_Type.__name__=_D
_SwSingleIPGroupPlatform_Object=MibTableColumn
swSingleIPGroupPlatform=_SwSingleIPGroupPlatform_Object((1,3,6,1,4,1,171,12,8,1,5,1,7),_SwSingleIPGroupPlatform_Type())
swSingleIPGroupPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupPlatform.setStatus(_A)
_SwSingleIPGroupHoldtime_Type=Integer32
_SwSingleIPGroupHoldtime_Object=MibTableColumn
swSingleIPGroupHoldtime=_SwSingleIPGroupHoldtime_Object((1,3,6,1,4,1,171,12,8,1,5,1,8),_SwSingleIPGroupHoldtime_Type())
swSingleIPGroupHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPGroupHoldtime.setStatus(_A)
_SwSingleIPNeighborTable_Object=MibTable
swSingleIPNeighborTable=_SwSingleIPNeighborTable_Object((1,3,6,1,4,1,171,12,8,1,6))
if mibBuilder.loadTexts:swSingleIPNeighborTable.setStatus(_A)
_SwSingleIPNeighborEntry_Object=MibTableRow
swSingleIPNeighborEntry=_SwSingleIPNeighborEntry_Object((1,3,6,1,4,1,171,12,8,1,6,1))
swSingleIPNeighborEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:swSingleIPNeighborEntry.setStatus(_A)
_SwSingleIPNBReceivedPort_Type=Integer32
_SwSingleIPNBReceivedPort_Object=MibTableColumn
swSingleIPNBReceivedPort=_SwSingleIPNBReceivedPort_Object((1,3,6,1,4,1,171,12,8,1,6,1,1),_SwSingleIPNBReceivedPort_Type())
swSingleIPNBReceivedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPNBReceivedPort.setStatus(_A)
_SwSingleIPNBMacAddr_Type=MacAddress
_SwSingleIPNBMacAddr_Object=MibTableColumn
swSingleIPNBMacAddr=_SwSingleIPNBMacAddr_Object((1,3,6,1,4,1,171,12,8,1,6,1,2),_SwSingleIPNBMacAddr_Type())
swSingleIPNBMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPNBMacAddr.setStatus(_A)
class _SwSingleIPNBRoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commander',1),('candidate',2),('member',3)))
_SwSingleIPNBRoleState_Type.__name__=_G
_SwSingleIPNBRoleState_Object=MibTableColumn
swSingleIPNBRoleState=_SwSingleIPNBRoleState_Object((1,3,6,1,4,1,171,12,8,1,6,1,3),_SwSingleIPNBRoleState_Type())
swSingleIPNBRoleState.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPNBRoleState.setStatus(_A)
_SingleIPMSNotify_ObjectIdentity=ObjectIdentity
singleIPMSNotify=_SingleIPMSNotify_ObjectIdentity((1,3,6,1,4,1,171,12,8,6))
_SingleIPMSNotifyPrefix_ObjectIdentity=ObjectIdentity
singleIPMSNotifyPrefix=_SingleIPMSNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,8,6,0))
_SingleIPNotifyBidings_ObjectIdentity=ObjectIdentity
singleIPNotifyBidings=_SingleIPNotifyBidings_ObjectIdentity((1,3,6,1,4,1,171,12,8,6,1))
class _SwSingleIPMSTrapMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwSingleIPMSTrapMessage_Type.__name__=_L
_SwSingleIPMSTrapMessage_Object=MibScalar
swSingleIPMSTrapMessage=_SwSingleIPMSTrapMessage_Object((1,3,6,1,4,1,171,12,8,6,1,1),_SwSingleIPMSTrapMessage_Type())
swSingleIPMSTrapMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:swSingleIPMSTrapMessage.setStatus(_A)
swSingleIPMSColdStart=NotificationType((1,3,6,1,4,1,171,12,8,6,0,11))
swSingleIPMSColdStart.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSColdStart.setStatus(_A)
swSingleIPMSWarmStart=NotificationType((1,3,6,1,4,1,171,12,8,6,0,12))
swSingleIPMSWarmStart.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSWarmStart.setStatus(_A)
swSingleIPMSLinkDown=NotificationType((1,3,6,1,4,1,171,12,8,6,0,13))
swSingleIPMSLinkDown.setObjects(*((_B,_E),(_B,_F),(_J,_K)))
if mibBuilder.loadTexts:swSingleIPMSLinkDown.setStatus(_A)
swSingleIPMSLinkUp=NotificationType((1,3,6,1,4,1,171,12,8,6,0,14))
swSingleIPMSLinkUp.setObjects(*((_B,_E),(_B,_F),(_J,_K)))
if mibBuilder.loadTexts:swSingleIPMSLinkUp.setStatus(_A)
swSingleIPMSAuthFail=NotificationType((1,3,6,1,4,1,171,12,8,6,0,15))
swSingleIPMSAuthFail.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSAuthFail.setStatus(_A)
swSingleIPMSnewRoot=NotificationType((1,3,6,1,4,1,171,12,8,6,0,16))
swSingleIPMSnewRoot.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSnewRoot.setStatus(_A)
swSingleIPMSTopologyChange=NotificationType((1,3,6,1,4,1,171,12,8,6,0,17))
swSingleIPMSTopologyChange.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSTopologyChange.setStatus(_A)
swSingleIPMSrisingAlarm=NotificationType((1,3,6,1,4,1,171,12,8,6,0,18))
swSingleIPMSrisingAlarm.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSrisingAlarm.setStatus(_A)
swSingleIPMSfallingAlarm=NotificationType((1,3,6,1,4,1,171,12,8,6,0,19))
swSingleIPMSfallingAlarm.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:swSingleIPMSfallingAlarm.setStatus(_A)
swSingleIPMSmacNotification=NotificationType((1,3,6,1,4,1,171,12,8,6,0,20))
swSingleIPMSmacNotification.setObjects(*((_B,_E),(_B,_F),(_B,_I)))
if mibBuilder.loadTexts:swSingleIPMSmacNotification.setStatus(_A)
swSingleIPMSPortTypeChange=NotificationType((1,3,6,1,4,1,171,12,8,6,0,21))
swSingleIPMSPortTypeChange.setObjects(*((_B,_E),(_B,_F),(_J,_K),(_B,_I)))
if mibBuilder.loadTexts:swSingleIPMSPortTypeChange.setStatus(_A)
swSingleIPMSPowerStatusChg=NotificationType((1,3,6,1,4,1,171,12,8,6,0,22))
swSingleIPMSPowerStatusChg.setObjects(*((_B,_E),(_B,_F),(_B,_I)))
if mibBuilder.loadTexts:swSingleIPMSPowerStatusChg.setStatus(_A)
swSingleIPMSPowerFailure=NotificationType((1,3,6,1,4,1,171,12,8,6,0,23))
swSingleIPMSPowerFailure.setObjects(*((_B,_E),(_B,_F),(_B,_I)))
if mibBuilder.loadTexts:swSingleIPMSPowerFailure.setStatus(_A)
swSingleIPMSPowerRecover=NotificationType((1,3,6,1,4,1,171,12,8,6,0,24))
swSingleIPMSPowerRecover.setObjects(*((_B,_E),(_B,_F),(_B,_I)))
if mibBuilder.loadTexts:swSingleIPMSPowerRecover.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'swSingleIPMIB':swSingleIPMIB,'swSingleIPMgmt':swSingleIPMgmt,'swSingleIPInfo':swSingleIPInfo,'swSingleIPVersion':swSingleIPVersion,'swSingleIPCapability':swSingleIPCapability,'swSingleIPPlatform':swSingleIPPlatform,'swSingleIPCtrl':swSingleIPCtrl,'swSingleIPAdmin':swSingleIPAdmin,'swSingleIPRoleState':swSingleIPRoleState,'swSingleIPHoldtime':swSingleIPHoldtime,'swSingleIPTimeInterval':swSingleIPTimeInterval,'swSingleIPCSGroupName':swSingleIPCSGroupName,'swSingleIPTrapMgmt':swSingleIPTrapMgmt,'swSingleIPTrapStatus':swSingleIPTrapStatus,'swSingleIPMSTable':swSingleIPMSTable,'swSingleIPMSEntry':swSingleIPMSEntry,_E:swSingleIPMSID,'swSingleIPMSDeviceName':swSingleIPMSDeviceName,_F:swSingleIPMSMacAddr,'swSingleIPMSFirmwareVer':swSingleIPMSFirmwareVer,'swSingleIPMSCapability':swSingleIPMSCapability,'swSingleIPMSPlatform':swSingleIPMSPlatform,'swSingleIPMSHoldtime':swSingleIPMSHoldtime,'swSingleIPMSCasSource':swSingleIPMSCasSource,'swSingleIPMSPassword':swSingleIPMSPassword,'swSingleIPMSRowStatus':swSingleIPMSRowStatus,'swSingleIPCaSTable':swSingleIPCaSTable,'swSingleIPCaSEntry':swSingleIPCaSEntry,_P:swSingleIPCaSID,'swSingleIPCaSDeviceName':swSingleIPCaSDeviceName,'swSingleIPCaSMacAddr':swSingleIPCaSMacAddr,'swSingleIPCaSFirmwareVer':swSingleIPCaSFirmwareVer,'swSingleIPCaSCapability':swSingleIPCaSCapability,'swSingleIPCaSPlatform':swSingleIPCaSPlatform,'swSingleIPCaSHoldtime':swSingleIPCaSHoldtime,'swSingleIPGroupTable':swSingleIPGroupTable,'swSingleIPGroupEntry':swSingleIPGroupEntry,_Q:swSingleIPGroupMacAddr,'swSingleIPGroupName':swSingleIPGroupName,'swSingleIPGroupDeviceName':swSingleIPGroupDeviceName,'swSingleIPGroupMSNumber':swSingleIPGroupMSNumber,'swSingleIPGroupFirmwareVer':swSingleIPGroupFirmwareVer,'swSingleIPGroupCapability':swSingleIPGroupCapability,'swSingleIPGroupPlatform':swSingleIPGroupPlatform,'swSingleIPGroupHoldtime':swSingleIPGroupHoldtime,'swSingleIPNeighborTable':swSingleIPNeighborTable,'swSingleIPNeighborEntry':swSingleIPNeighborEntry,_R:swSingleIPNBReceivedPort,_S:swSingleIPNBMacAddr,'swSingleIPNBRoleState':swSingleIPNBRoleState,'singleIPMSNotify':singleIPMSNotify,'singleIPMSNotifyPrefix':singleIPMSNotifyPrefix,'swSingleIPMSColdStart':swSingleIPMSColdStart,'swSingleIPMSWarmStart':swSingleIPMSWarmStart,'swSingleIPMSLinkDown':swSingleIPMSLinkDown,'swSingleIPMSLinkUp':swSingleIPMSLinkUp,'swSingleIPMSAuthFail':swSingleIPMSAuthFail,'swSingleIPMSnewRoot':swSingleIPMSnewRoot,'swSingleIPMSTopologyChange':swSingleIPMSTopologyChange,'swSingleIPMSrisingAlarm':swSingleIPMSrisingAlarm,'swSingleIPMSfallingAlarm':swSingleIPMSfallingAlarm,'swSingleIPMSmacNotification':swSingleIPMSmacNotification,'swSingleIPMSPortTypeChange':swSingleIPMSPortTypeChange,'swSingleIPMSPowerStatusChg':swSingleIPMSPowerStatusChg,'swSingleIPMSPowerFailure':swSingleIPMSPowerFailure,'swSingleIPMSPowerRecover':swSingleIPMSPowerRecover,'singleIPNotifyBidings':singleIPNotifyBidings,_I:swSingleIPMSTrapMessage})