_j='raisecomRemoteVlanGroupIndex'
_i='norecalculate'
_h='recalculate'
_g='raisecomRemoteStatsPortIfindex'
_f='raisecomRemoteStatsIfindex'
_e='disable'
_d='enable'
_c='full-1000'
_b='half-1000'
_a='full-100'
_Z='half-100'
_Y='full-10'
_X='half-10'
_W='raisecomRemoteIfindex'
_V='raisecomRemoteL3Index'
_U='raisecomRemoteEnvironmentIndex'
_T='raisecomRemoteInvariableInfoIndex'
_S='failed'
_R='successful'
_Q='RcRemoteConfigFrameSendStatus'
_P='unavailable'
_O='raisecomRemoteSysCfgIndex'
_N='TruthValue'
_M='down'
_L='raisecomRemotePortIfindex'
_K='unknown'
_J='normal'
_I='not-accessible'
_H='OctetString'
_G='RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
EntryStatus,=mibBuilder.importSymbols('SWITCH-RMON-MIB','EntryStatus')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC','EnableVar','PortList')
raisecomRemoteManagementLocal=ModuleIdentity((1,3,6,1,4,1,8886,1,12))
class RcRemoteVlanStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vlan-forbid',1),('vlan-dot1q',2),('vlan-port',3)))
class RcRemotePortTagStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('untag',1),('tag',2)))
class RcRemoteConfigFrameSendStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('send',1),('save',2),('sendandsave',3),('waitting',4),(_R,5),(_S,6)))
class RcRemoteSfpDdmMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('inside',1),('outside',2)))
class RcRemoteSfpDdmAlarmStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('low',1),('high',2)))
_RaisecomRemoteManagementLocalMibObjects_ObjectIdentity=ObjectIdentity
raisecomRemoteManagementLocalMibObjects=_RaisecomRemoteManagementLocalMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,12,1))
_RaisecomRemoteTrapEnable_Type=EnableVar
_RaisecomRemoteTrapEnable_Object=MibScalar
raisecomRemoteTrapEnable=_RaisecomRemoteTrapEnable_Object((1,3,6,1,4,1,8886,1,12,1,1),_RaisecomRemoteTrapEnable_Type())
raisecomRemoteTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteTrapEnable.setStatus(_A)
_RaisecomRemoteInvariableInfoTable_Object=MibTable
raisecomRemoteInvariableInfoTable=_RaisecomRemoteInvariableInfoTable_Object((1,3,6,1,4,1,8886,1,12,1,2))
if mibBuilder.loadTexts:raisecomRemoteInvariableInfoTable.setStatus(_A)
_RaisecomRemoteInvariableInfoEntry_Object=MibTableRow
raisecomRemoteInvariableInfoEntry=_RaisecomRemoteInvariableInfoEntry_Object((1,3,6,1,4,1,8886,1,12,1,2,1))
raisecomRemoteInvariableInfoEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:raisecomRemoteInvariableInfoEntry.setStatus(_A)
_RaisecomRemoteInvariableInfoIndex_Type=Integer32
_RaisecomRemoteInvariableInfoIndex_Object=MibTableColumn
raisecomRemoteInvariableInfoIndex=_RaisecomRemoteInvariableInfoIndex_Object((1,3,6,1,4,1,8886,1,12,1,2,1,1),_RaisecomRemoteInvariableInfoIndex_Type())
raisecomRemoteInvariableInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteInvariableInfoIndex.setStatus(_A)
_RaisecomRemoteSysOid_Type=ObjectIdentifier
_RaisecomRemoteSysOid_Object=MibTableColumn
raisecomRemoteSysOid=_RaisecomRemoteSysOid_Object((1,3,6,1,4,1,8886,1,12,1,2,1,2),_RaisecomRemoteSysOid_Type())
raisecomRemoteSysOid.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSysOid.setStatus(_A)
_RaisecomRemoteModuleType_Type=Integer32
_RaisecomRemoteModuleType_Object=MibTableColumn
raisecomRemoteModuleType=_RaisecomRemoteModuleType_Object((1,3,6,1,4,1,8886,1,12,1,2,1,3),_RaisecomRemoteModuleType_Type())
raisecomRemoteModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteModuleType.setStatus(_A)
class _RaisecomRemoteOidCapability_Type(TruthValue):defaultValue=2
_RaisecomRemoteOidCapability_Type.__name__=_N
_RaisecomRemoteOidCapability_Object=MibTableColumn
raisecomRemoteOidCapability=_RaisecomRemoteOidCapability_Object((1,3,6,1,4,1,8886,1,12,1,2,1,4),_RaisecomRemoteOidCapability_Type())
raisecomRemoteOidCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteOidCapability.setStatus(_A)
class _RaisecomRemoteFileTransCapability_Type(TruthValue):defaultValue=2
_RaisecomRemoteFileTransCapability_Type.__name__=_N
_RaisecomRemoteFileTransCapability_Object=MibTableColumn
raisecomRemoteFileTransCapability=_RaisecomRemoteFileTransCapability_Object((1,3,6,1,4,1,8886,1,12,1,2,1,5),_RaisecomRemoteFileTransCapability_Type())
raisecomRemoteFileTransCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteFileTransCapability.setStatus(_A)
class _RaisecomRemoteOtherCapability_Type(Integer32):defaultValue=0
_RaisecomRemoteOtherCapability_Type.__name__=_C
_RaisecomRemoteOtherCapability_Object=MibTableColumn
raisecomRemoteOtherCapability=_RaisecomRemoteOtherCapability_Object((1,3,6,1,4,1,8886,1,12,1,2,1,6),_RaisecomRemoteOtherCapability_Type())
raisecomRemoteOtherCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteOtherCapability.setStatus(_A)
class _RaisecomRemoteMainChipId_Type(Integer32):defaultValue=0
_RaisecomRemoteMainChipId_Type.__name__=_C
_RaisecomRemoteMainChipId_Object=MibTableColumn
raisecomRemoteMainChipId=_RaisecomRemoteMainChipId_Object((1,3,6,1,4,1,8886,1,12,1,2,1,7),_RaisecomRemoteMainChipId_Type())
raisecomRemoteMainChipId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteMainChipId.setStatus(_A)
class _RaisecomRemoteFpgaChipId_Type(Integer32):defaultValue=0
_RaisecomRemoteFpgaChipId_Type.__name__=_C
_RaisecomRemoteFpgaChipId_Object=MibTableColumn
raisecomRemoteFpgaChipId=_RaisecomRemoteFpgaChipId_Object((1,3,6,1,4,1,8886,1,12,1,2,1,8),_RaisecomRemoteFpgaChipId_Type())
raisecomRemoteFpgaChipId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteFpgaChipId.setStatus(_A)
_RaisecomRemoteFpgaSwVer_Type=OctetString
_RaisecomRemoteFpgaSwVer_Object=MibTableColumn
raisecomRemoteFpgaSwVer=_RaisecomRemoteFpgaSwVer_Object((1,3,6,1,4,1,8886,1,12,1,2,1,9),_RaisecomRemoteFpgaSwVer_Type())
raisecomRemoteFpgaSwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteFpgaSwVer.setStatus(_A)
_RaisecomRemoteSystemSwVer_Type=OctetString
_RaisecomRemoteSystemSwVer_Object=MibTableColumn
raisecomRemoteSystemSwVer=_RaisecomRemoteSystemSwVer_Object((1,3,6,1,4,1,8886,1,12,1,2,1,10),_RaisecomRemoteSystemSwVer_Type())
raisecomRemoteSystemSwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSystemSwVer.setStatus(_A)
_RaisecomRemoteSystemHwVer_Type=OctetString
_RaisecomRemoteSystemHwVer_Object=MibTableColumn
raisecomRemoteSystemHwVer=_RaisecomRemoteSystemHwVer_Object((1,3,6,1,4,1,8886,1,12,1,2,1,11),_RaisecomRemoteSystemHwVer_Type())
raisecomRemoteSystemHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSystemHwVer.setStatus(_A)
_RaisecomRemotePortNum_Type=Integer32
_RaisecomRemotePortNum_Object=MibTableColumn
raisecomRemotePortNum=_RaisecomRemotePortNum_Object((1,3,6,1,4,1,8886,1,12,1,2,1,12),_RaisecomRemotePortNum_Type())
raisecomRemotePortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortNum.setStatus(_A)
_RaisecomRemoteDeviceName_Type=OctetString
_RaisecomRemoteDeviceName_Object=MibTableColumn
raisecomRemoteDeviceName=_RaisecomRemoteDeviceName_Object((1,3,6,1,4,1,8886,1,12,1,2,1,13),_RaisecomRemoteDeviceName_Type())
raisecomRemoteDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteDeviceName.setStatus(_A)
_RaisecomRemoteInvariableInfoStatus_Type=EntryStatus
_RaisecomRemoteInvariableInfoStatus_Object=MibTableColumn
raisecomRemoteInvariableInfoStatus=_RaisecomRemoteInvariableInfoStatus_Object((1,3,6,1,4,1,8886,1,12,1,2,1,14),_RaisecomRemoteInvariableInfoStatus_Type())
raisecomRemoteInvariableInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteInvariableInfoStatus.setStatus(_A)
_RaisecomRemoteEnvironmentTable_Object=MibTable
raisecomRemoteEnvironmentTable=_RaisecomRemoteEnvironmentTable_Object((1,3,6,1,4,1,8886,1,12,1,3))
if mibBuilder.loadTexts:raisecomRemoteEnvironmentTable.setStatus(_A)
_RaisecomRemoteEnvironmentEntry_Object=MibTableRow
raisecomRemoteEnvironmentEntry=_RaisecomRemoteEnvironmentEntry_Object((1,3,6,1,4,1,8886,1,12,1,3,1))
raisecomRemoteEnvironmentEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:raisecomRemoteEnvironmentEntry.setStatus(_A)
_RaisecomRemoteEnvironmentIndex_Type=Integer32
_RaisecomRemoteEnvironmentIndex_Object=MibTableColumn
raisecomRemoteEnvironmentIndex=_RaisecomRemoteEnvironmentIndex_Object((1,3,6,1,4,1,8886,1,12,1,3,1,1),_RaisecomRemoteEnvironmentIndex_Type())
raisecomRemoteEnvironmentIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteEnvironmentIndex.setStatus(_A)
class _RaisecomRemoteTemperature_Type(Integer32):defaultValue=65535
_RaisecomRemoteTemperature_Type.__name__=_C
_RaisecomRemoteTemperature_Object=MibTableColumn
raisecomRemoteTemperature=_RaisecomRemoteTemperature_Object((1,3,6,1,4,1,8886,1,12,1,3,1,2),_RaisecomRemoteTemperature_Type())
raisecomRemoteTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteTemperature.setStatus(_A)
class _RaisecomRemoteVolt3300_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt3300_Type.__name__=_C
_RaisecomRemoteVolt3300_Object=MibTableColumn
raisecomRemoteVolt3300=_RaisecomRemoteVolt3300_Object((1,3,6,1,4,1,8886,1,12,1,3,1,3),_RaisecomRemoteVolt3300_Type())
raisecomRemoteVolt3300.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt3300.setStatus(_A)
class _RaisecomRemoteVolt2500_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt2500_Type.__name__=_C
_RaisecomRemoteVolt2500_Object=MibTableColumn
raisecomRemoteVolt2500=_RaisecomRemoteVolt2500_Object((1,3,6,1,4,1,8886,1,12,1,3,1,4),_RaisecomRemoteVolt2500_Type())
raisecomRemoteVolt2500.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt2500.setStatus(_A)
class _RaisecomRemoteVolt1800_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt1800_Type.__name__=_C
_RaisecomRemoteVolt1800_Object=MibTableColumn
raisecomRemoteVolt1800=_RaisecomRemoteVolt1800_Object((1,3,6,1,4,1,8886,1,12,1,3,1,5),_RaisecomRemoteVolt1800_Type())
raisecomRemoteVolt1800.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt1800.setStatus(_A)
class _RaisecomRemoteVolt1200_Type(Integer32):defaultValue=65535
_RaisecomRemoteVolt1200_Type.__name__=_C
_RaisecomRemoteVolt1200_Object=MibTableColumn
raisecomRemoteVolt1200=_RaisecomRemoteVolt1200_Object((1,3,6,1,4,1,8886,1,12,1,3,1,6),_RaisecomRemoteVolt1200_Type())
raisecomRemoteVolt1200.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVolt1200.setStatus(_A)
class _RaisecomRemoteVoltNormal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('high',2),('low',3)))
_RaisecomRemoteVoltNormal_Type.__name__=_C
_RaisecomRemoteVoltNormal_Object=MibTableColumn
raisecomRemoteVoltNormal=_RaisecomRemoteVoltNormal_Object((1,3,6,1,4,1,8886,1,12,1,3,1,7),_RaisecomRemoteVoltNormal_Type())
raisecomRemoteVoltNormal.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVoltNormal.setStatus(_A)
_RaisecomRemoteSysCfgTable_Object=MibTable
raisecomRemoteSysCfgTable=_RaisecomRemoteSysCfgTable_Object((1,3,6,1,4,1,8886,1,12,1,4))
if mibBuilder.loadTexts:raisecomRemoteSysCfgTable.setStatus(_A)
_RaisecomRemoteSysCfgEntry_Object=MibTableRow
raisecomRemoteSysCfgEntry=_RaisecomRemoteSysCfgEntry_Object((1,3,6,1,4,1,8886,1,12,1,4,1))
raisecomRemoteSysCfgEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:raisecomRemoteSysCfgEntry.setStatus(_A)
_RaisecomRemoteSysCfgIndex_Type=Integer32
_RaisecomRemoteSysCfgIndex_Object=MibTableColumn
raisecomRemoteSysCfgIndex=_RaisecomRemoteSysCfgIndex_Object((1,3,6,1,4,1,8886,1,12,1,4,1,1),_RaisecomRemoteSysCfgIndex_Type())
raisecomRemoteSysCfgIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteSysCfgIndex.setStatus(_A)
class _RaisecomRemoteSysOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('write',2),('erase',3),('reboot',4)))
_RaisecomRemoteSysOperation_Type.__name__=_C
_RaisecomRemoteSysOperation_Object=MibTableColumn
raisecomRemoteSysOperation=_RaisecomRemoteSysOperation_Object((1,3,6,1,4,1,8886,1,12,1,4,1,2),_RaisecomRemoteSysOperation_Type())
raisecomRemoteSysOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteSysOperation.setStatus(_A)
class _RaisecomRemoteSysOperationState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('running',2),(_R,3),(_S,4)))
_RaisecomRemoteSysOperationState_Type.__name__=_C
_RaisecomRemoteSysOperationState_Object=MibTableColumn
raisecomRemoteSysOperationState=_RaisecomRemoteSysOperationState_Object((1,3,6,1,4,1,8886,1,12,1,4,1,3),_RaisecomRemoteSysOperationState_Type())
raisecomRemoteSysOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSysOperationState.setStatus(_A)
class _RaisecomRemoteHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomRemoteHostName_Type.__name__=_H
_RaisecomRemoteHostName_Object=MibTableColumn
raisecomRemoteHostName=_RaisecomRemoteHostName_Object((1,3,6,1,4,1,8886,1,12,1,4,1,4),_RaisecomRemoteHostName_Type())
raisecomRemoteHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteHostName.setStatus(_A)
_RaisecomRemoteOamNotificationEnable_Type=EnableVar
_RaisecomRemoteOamNotificationEnable_Object=MibTableColumn
raisecomRemoteOamNotificationEnable=_RaisecomRemoteOamNotificationEnable_Object((1,3,6,1,4,1,8886,1,12,1,4,1,5),_RaisecomRemoteOamNotificationEnable_Type())
raisecomRemoteOamNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteOamNotificationEnable.setStatus(_A)
_RaisecomRemoteMaxAllowedFrameLength_Type=Integer32
_RaisecomRemoteMaxAllowedFrameLength_Object=MibTableColumn
raisecomRemoteMaxAllowedFrameLength=_RaisecomRemoteMaxAllowedFrameLength_Object((1,3,6,1,4,1,8886,1,12,1,4,1,6),_RaisecomRemoteMaxAllowedFrameLength_Type())
raisecomRemoteMaxAllowedFrameLength.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteMaxAllowedFrameLength.setStatus(_A)
_RaisecomRemoteCommunityTable_Object=MibTable
raisecomRemoteCommunityTable=_RaisecomRemoteCommunityTable_Object((1,3,6,1,4,1,8886,1,12,1,5))
if mibBuilder.loadTexts:raisecomRemoteCommunityTable.setStatus(_A)
_RaisecomRemoteCommunityEntry_Object=MibTableRow
raisecomRemoteCommunityEntry=_RaisecomRemoteCommunityEntry_Object((1,3,6,1,4,1,8886,1,12,1,5,1))
raisecomRemoteCommunityEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:raisecomRemoteCommunityEntry.setStatus(_A)
_RaisecomRemoteCommunityIndex_Type=Integer32
_RaisecomRemoteCommunityIndex_Object=MibTableColumn
raisecomRemoteCommunityIndex=_RaisecomRemoteCommunityIndex_Object((1,3,6,1,4,1,8886,1,12,1,5,1,1),_RaisecomRemoteCommunityIndex_Type())
raisecomRemoteCommunityIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteCommunityIndex.setStatus(_A)
class _RaisecomRemoteCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RaisecomRemoteCommunityName_Type.__name__=_H
_RaisecomRemoteCommunityName_Object=MibTableColumn
raisecomRemoteCommunityName=_RaisecomRemoteCommunityName_Object((1,3,6,1,4,1,8886,1,12,1,5,1,2),_RaisecomRemoteCommunityName_Type())
raisecomRemoteCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCommunityName.setStatus(_A)
class _RaisecomRemoteCommunityPermission_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2),('invalid',3)))
_RaisecomRemoteCommunityPermission_Type.__name__=_C
_RaisecomRemoteCommunityPermission_Object=MibTableColumn
raisecomRemoteCommunityPermission=_RaisecomRemoteCommunityPermission_Object((1,3,6,1,4,1,8886,1,12,1,5,1,3),_RaisecomRemoteCommunityPermission_Type())
raisecomRemoteCommunityPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCommunityPermission.setStatus(_A)
_RaisecomRemoteL3Table_Object=MibTable
raisecomRemoteL3Table=_RaisecomRemoteL3Table_Object((1,3,6,1,4,1,8886,1,12,1,6))
if mibBuilder.loadTexts:raisecomRemoteL3Table.setStatus(_A)
_RaisecomRemoteL3Entry_Object=MibTableRow
raisecomRemoteL3Entry=_RaisecomRemoteL3Entry_Object((1,3,6,1,4,1,8886,1,12,1,6,1))
raisecomRemoteL3Entry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:raisecomRemoteL3Entry.setStatus(_A)
_RaisecomRemoteL3Index_Type=Integer32
_RaisecomRemoteL3Index_Object=MibTableColumn
raisecomRemoteL3Index=_RaisecomRemoteL3Index_Object((1,3,6,1,4,1,8886,1,12,1,6,1,1),_RaisecomRemoteL3Index_Type())
raisecomRemoteL3Index.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteL3Index.setStatus(_A)
_RaisecomRemoteL3IpAddr_Type=IpAddress
_RaisecomRemoteL3IpAddr_Object=MibTableColumn
raisecomRemoteL3IpAddr=_RaisecomRemoteL3IpAddr_Object((1,3,6,1,4,1,8886,1,12,1,6,1,2),_RaisecomRemoteL3IpAddr_Type())
raisecomRemoteL3IpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3IpAddr.setStatus(_A)
_RaisecomRemoteL3Mask_Type=IpAddress
_RaisecomRemoteL3Mask_Object=MibTableColumn
raisecomRemoteL3Mask=_RaisecomRemoteL3Mask_Object((1,3,6,1,4,1,8886,1,12,1,6,1,3),_RaisecomRemoteL3Mask_Type())
raisecomRemoteL3Mask.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3Mask.setStatus(_A)
class _RaisecomRemoteL3VidIface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomRemoteL3VidIface_Type.__name__=_C
_RaisecomRemoteL3VidIface_Object=MibTableColumn
raisecomRemoteL3VidIface=_RaisecomRemoteL3VidIface_Object((1,3,6,1,4,1,8886,1,12,1,6,1,4),_RaisecomRemoteL3VidIface_Type())
raisecomRemoteL3VidIface.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3VidIface.setStatus(_A)
_RaisecomRemoteL3VidMemberPorts_Type=PortList
_RaisecomRemoteL3VidMemberPorts_Object=MibTableColumn
raisecomRemoteL3VidMemberPorts=_RaisecomRemoteL3VidMemberPorts_Object((1,3,6,1,4,1,8886,1,12,1,6,1,5),_RaisecomRemoteL3VidMemberPorts_Type())
raisecomRemoteL3VidMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteL3VidMemberPorts.setStatus(_A)
_RaisecomRemoteL3VidUntaggedPorts_Type=PortList
_RaisecomRemoteL3VidUntaggedPorts_Object=MibTableColumn
raisecomRemoteL3VidUntaggedPorts=_RaisecomRemoteL3VidUntaggedPorts_Object((1,3,6,1,4,1,8886,1,12,1,6,1,6),_RaisecomRemoteL3VidUntaggedPorts_Type())
raisecomRemoteL3VidUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteL3VidUntaggedPorts.setStatus(_A)
_RaisecomRemoteL3DefaultGateway_Type=IpAddress
_RaisecomRemoteL3DefaultGateway_Object=MibTableColumn
raisecomRemoteL3DefaultGateway=_RaisecomRemoteL3DefaultGateway_Object((1,3,6,1,4,1,8886,1,12,1,6,1,7),_RaisecomRemoteL3DefaultGateway_Type())
raisecomRemoteL3DefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3DefaultGateway.setStatus(_A)
_RaisecomRemoteL3ObIpAddr_Type=IpAddress
_RaisecomRemoteL3ObIpAddr_Object=MibTableColumn
raisecomRemoteL3ObIpAddr=_RaisecomRemoteL3ObIpAddr_Object((1,3,6,1,4,1,8886,1,12,1,6,1,8),_RaisecomRemoteL3ObIpAddr_Type())
raisecomRemoteL3ObIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3ObIpAddr.setStatus(_A)
_RaisecomRemoteL3ObMask_Type=IpAddress
_RaisecomRemoteL3ObMask_Object=MibTableColumn
raisecomRemoteL3ObMask=_RaisecomRemoteL3ObMask_Object((1,3,6,1,4,1,8886,1,12,1,6,1,9),_RaisecomRemoteL3ObMask_Type())
raisecomRemoteL3ObMask.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteL3ObMask.setStatus(_A)
_RaisecomRemotePortTable_Object=MibTable
raisecomRemotePortTable=_RaisecomRemotePortTable_Object((1,3,6,1,4,1,8886,1,12,1,7))
if mibBuilder.loadTexts:raisecomRemotePortTable.setStatus(_A)
_RaisecomRemotePortEntry_Object=MibTableRow
raisecomRemotePortEntry=_RaisecomRemotePortEntry_Object((1,3,6,1,4,1,8886,1,12,1,7,1))
raisecomRemotePortEntry.setIndexNames((0,_G,_W),(0,_G,_L))
if mibBuilder.loadTexts:raisecomRemotePortEntry.setStatus(_A)
_RaisecomRemoteIfindex_Type=Integer32
_RaisecomRemoteIfindex_Object=MibTableColumn
raisecomRemoteIfindex=_RaisecomRemoteIfindex_Object((1,3,6,1,4,1,8886,1,12,1,7,1,1),_RaisecomRemoteIfindex_Type())
raisecomRemoteIfindex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteIfindex.setStatus(_A)
_RaisecomRemotePortIfindex_Type=Integer32
_RaisecomRemotePortIfindex_Object=MibTableColumn
raisecomRemotePortIfindex=_RaisecomRemotePortIfindex_Object((1,3,6,1,4,1,8886,1,12,1,7,1,2),_RaisecomRemotePortIfindex_Type())
raisecomRemotePortIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortIfindex.setStatus(_A)
class _RaisecomRemotePortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('inexistence',0),('fx-1000M',1),('tx-1000M',2),('fx-100M',3),('tx-100M',4)))
_RaisecomRemotePortType_Type.__name__=_C
_RaisecomRemotePortType_Object=MibTableColumn
raisecomRemotePortType=_RaisecomRemotePortType_Object((1,3,6,1,4,1,8886,1,12,1,7,1,3),_RaisecomRemotePortType_Type())
raisecomRemotePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortType.setStatus(_A)
class _RaisecomRemotePortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomRemotePortName_Type.__name__=_H
_RaisecomRemotePortName_Object=MibTableColumn
raisecomRemotePortName=_RaisecomRemotePortName_Object((1,3,6,1,4,1,8886,1,12,1,7,1,4),_RaisecomRemotePortName_Type())
raisecomRemotePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortName.setStatus(_A)
class _RaisecomRemotePortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_M,2)))
_RaisecomRemotePortAdminStatus_Type.__name__=_C
_RaisecomRemotePortAdminStatus_Object=MibTableColumn
raisecomRemotePortAdminStatus=_RaisecomRemotePortAdminStatus_Object((1,3,6,1,4,1,8886,1,12,1,7,1,5),_RaisecomRemotePortAdminStatus_Type())
raisecomRemotePortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortAdminStatus.setStatus(_A)
class _RaisecomRemotePortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_M,2)))
_RaisecomRemotePortOperStatus_Type.__name__=_C
_RaisecomRemotePortOperStatus_Object=MibTableColumn
raisecomRemotePortOperStatus=_RaisecomRemotePortOperStatus_Object((1,3,6,1,4,1,8886,1,12,1,7,1,6),_RaisecomRemotePortOperStatus_Type())
raisecomRemotePortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOperStatus.setStatus(_A)
class _RaisecomRemotePortDuplexSpeedSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('autonegotiate',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7)))
_RaisecomRemotePortDuplexSpeedSet_Type.__name__=_C
_RaisecomRemotePortDuplexSpeedSet_Object=MibTableColumn
raisecomRemotePortDuplexSpeedSet=_RaisecomRemotePortDuplexSpeedSet_Object((1,3,6,1,4,1,8886,1,12,1,7,1,7),_RaisecomRemotePortDuplexSpeedSet_Type())
raisecomRemotePortDuplexSpeedSet.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortDuplexSpeedSet.setStatus(_A)
class _RaisecomRemotePortDuplexSpeedGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*((_K,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7),('illegal',99)))
_RaisecomRemotePortDuplexSpeedGet_Type.__name__=_C
_RaisecomRemotePortDuplexSpeedGet_Object=MibTableColumn
raisecomRemotePortDuplexSpeedGet=_RaisecomRemotePortDuplexSpeedGet_Object((1,3,6,1,4,1,8886,1,12,1,7,1,8),_RaisecomRemotePortDuplexSpeedGet_Type())
raisecomRemotePortDuplexSpeedGet.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortDuplexSpeedGet.setStatus(_A)
_RaisecomRemotePortFlowControlEnable_Type=EnableVar
_RaisecomRemotePortFlowControlEnable_Object=MibTableColumn
raisecomRemotePortFlowControlEnable=_RaisecomRemotePortFlowControlEnable_Object((1,3,6,1,4,1,8886,1,12,1,7,1,9),_RaisecomRemotePortFlowControlEnable_Type())
raisecomRemotePortFlowControlEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFlowControlEnable.setStatus(_A)
_RaisecomRemotePortFlowControlStatus_Type=EnableVar
_RaisecomRemotePortFlowControlStatus_Object=MibTableColumn
raisecomRemotePortFlowControlStatus=_RaisecomRemotePortFlowControlStatus_Object((1,3,6,1,4,1,8886,1,12,1,7,1,10),_RaisecomRemotePortFlowControlStatus_Type())
raisecomRemotePortFlowControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFlowControlStatus.setStatus(_A)
class _RaisecomRemotePortIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RaisecomRemotePortIngressRate_Type.__name__=_C
_RaisecomRemotePortIngressRate_Object=MibTableColumn
raisecomRemotePortIngressRate=_RaisecomRemotePortIngressRate_Object((1,3,6,1,4,1,8886,1,12,1,7,1,11),_RaisecomRemotePortIngressRate_Type())
raisecomRemotePortIngressRate.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortIngressRate.setStatus(_A)
class _RaisecomRemotePortEgressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048576))
_RaisecomRemotePortEgressRate_Type.__name__=_C
_RaisecomRemotePortEgressRate_Object=MibTableColumn
raisecomRemotePortEgressRate=_RaisecomRemotePortEgressRate_Object((1,3,6,1,4,1,8886,1,12,1,7,1,12),_RaisecomRemotePortEgressRate_Type())
raisecomRemotePortEgressRate.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortEgressRate.setStatus(_A)
_RaisecomRemotePortFaultPassEnable_Type=EnableVar
_RaisecomRemotePortFaultPassEnable_Object=MibTableColumn
raisecomRemotePortFaultPassEnable=_RaisecomRemotePortFaultPassEnable_Object((1,3,6,1,4,1,8886,1,12,1,7,1,13),_RaisecomRemotePortFaultPassEnable_Type())
raisecomRemotePortFaultPassEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFaultPassEnable.setStatus(_A)
_RaisecomRemotePortFaultPassPorts_Type=PortList
_RaisecomRemotePortFaultPassPorts_Object=MibTableColumn
raisecomRemotePortFaultPassPorts=_RaisecomRemotePortFaultPassPorts_Object((1,3,6,1,4,1,8886,1,12,1,7,1,14),_RaisecomRemotePortFaultPassPorts_Type())
raisecomRemotePortFaultPassPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFaultPassPorts.setStatus(_A)
class _RaisecomRemotePortFaultPassStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_M,2)))
_RaisecomRemotePortFaultPassStatus_Type.__name__=_C
_RaisecomRemotePortFaultPassStatus_Object=MibTableColumn
raisecomRemotePortFaultPassStatus=_RaisecomRemotePortFaultPassStatus_Object((1,3,6,1,4,1,8886,1,12,1,7,1,15),_RaisecomRemotePortFaultPassStatus_Type())
raisecomRemotePortFaultPassStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFaultPassStatus.setStatus(_A)
class _RaisecomRemotePortFaultReturnEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),(_e,2),(_P,3)))
_RaisecomRemotePortFaultReturnEnable_Type.__name__=_C
_RaisecomRemotePortFaultReturnEnable_Object=MibTableColumn
raisecomRemotePortFaultReturnEnable=_RaisecomRemotePortFaultReturnEnable_Object((1,3,6,1,4,1,8886,1,12,1,7,1,16),_RaisecomRemotePortFaultReturnEnable_Type())
raisecomRemotePortFaultReturnEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortFaultReturnEnable.setStatus(_A)
class _RaisecomRemotePortFaultReturnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_M,2),(_P,3)))
_RaisecomRemotePortFaultReturnStatus_Type.__name__=_C
_RaisecomRemotePortFaultReturnStatus_Object=MibTableColumn
raisecomRemotePortFaultReturnStatus=_RaisecomRemotePortFaultReturnStatus_Object((1,3,6,1,4,1,8886,1,12,1,7,1,17),_RaisecomRemotePortFaultReturnStatus_Type())
raisecomRemotePortFaultReturnStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFaultReturnStatus.setStatus(_A)
class _RaisecomRemotePortSD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('sd',2),(_P,3)))
_RaisecomRemotePortSD_Type.__name__=_C
_RaisecomRemotePortSD_Object=MibTableColumn
raisecomRemotePortSD=_RaisecomRemotePortSD_Object((1,3,6,1,4,1,8886,1,12,1,7,1,18),_RaisecomRemotePortSD_Type())
raisecomRemotePortSD.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortSD.setStatus(_A)
class _RaisecomRemoteOptModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('optical-M',1),('optical-S1',2),('optical-S2',3),('optical-S3',4),('optical-SS13',5),('optical-SS15',6),('optical-SS23',7),('optical-SS25',8),('optical-SS35',9),(_K,10)))
_RaisecomRemoteOptModuleType_Type.__name__=_C
_RaisecomRemoteOptModuleType_Object=MibTableColumn
raisecomRemoteOptModuleType=_RaisecomRemoteOptModuleType_Object((1,3,6,1,4,1,8886,1,12,1,7,1,19),_RaisecomRemoteOptModuleType_Type())
raisecomRemoteOptModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteOptModuleType.setStatus(_A)
class _RaisecomRemotePortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RaisecomRemotePortDescr_Type.__name__=_H
_RaisecomRemotePortDescr_Object=MibTableColumn
raisecomRemotePortDescr=_RaisecomRemotePortDescr_Object((1,3,6,1,4,1,8886,1,12,1,7,1,20),_RaisecomRemotePortDescr_Type())
raisecomRemotePortDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemotePortDescr.setStatus(_A)
_RaisecomRemotePortStatsTable_Object=MibTable
raisecomRemotePortStatsTable=_RaisecomRemotePortStatsTable_Object((1,3,6,1,4,1,8886,1,12,1,8))
if mibBuilder.loadTexts:raisecomRemotePortStatsTable.setStatus(_A)
_RaisecomRemotePortStatsEntry_Object=MibTableRow
raisecomRemotePortStatsEntry=_RaisecomRemotePortStatsEntry_Object((1,3,6,1,4,1,8886,1,12,1,8,1))
raisecomRemotePortStatsEntry.setIndexNames((0,_G,_f),(0,_G,_g))
if mibBuilder.loadTexts:raisecomRemotePortStatsEntry.setStatus(_A)
_RaisecomRemoteStatsIfindex_Type=Integer32
_RaisecomRemoteStatsIfindex_Object=MibTableColumn
raisecomRemoteStatsIfindex=_RaisecomRemoteStatsIfindex_Object((1,3,6,1,4,1,8886,1,12,1,8,1,1),_RaisecomRemoteStatsIfindex_Type())
raisecomRemoteStatsIfindex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteStatsIfindex.setStatus(_A)
_RaisecomRemoteStatsPortIfindex_Type=Integer32
_RaisecomRemoteStatsPortIfindex_Object=MibTableColumn
raisecomRemoteStatsPortIfindex=_RaisecomRemoteStatsPortIfindex_Object((1,3,6,1,4,1,8886,1,12,1,8,1,2),_RaisecomRemoteStatsPortIfindex_Type())
raisecomRemoteStatsPortIfindex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteStatsPortIfindex.setStatus(_A)
_RaisecomRemotePortInOctets_Type=Counter64
_RaisecomRemotePortInOctets_Object=MibTableColumn
raisecomRemotePortInOctets=_RaisecomRemotePortInOctets_Object((1,3,6,1,4,1,8886,1,12,1,8,1,3),_RaisecomRemotePortInOctets_Type())
raisecomRemotePortInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInOctets.setStatus(_A)
_RaisecomRemotePortInPkts_Type=Counter64
_RaisecomRemotePortInPkts_Object=MibTableColumn
raisecomRemotePortInPkts=_RaisecomRemotePortInPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,4),_RaisecomRemotePortInPkts_Type())
raisecomRemotePortInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInPkts.setStatus(_A)
_RaisecomRemotePortInUcastPkts_Type=Counter64
_RaisecomRemotePortInUcastPkts_Object=MibTableColumn
raisecomRemotePortInUcastPkts=_RaisecomRemotePortInUcastPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,5),_RaisecomRemotePortInUcastPkts_Type())
raisecomRemotePortInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInUcastPkts.setStatus(_A)
_RaisecomRemotePortInMulticastPkts_Type=Counter64
_RaisecomRemotePortInMulticastPkts_Object=MibTableColumn
raisecomRemotePortInMulticastPkts=_RaisecomRemotePortInMulticastPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,6),_RaisecomRemotePortInMulticastPkts_Type())
raisecomRemotePortInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInMulticastPkts.setStatus(_A)
_RaisecomRemotePortInBroadcastPkts_Type=Counter64
_RaisecomRemotePortInBroadcastPkts_Object=MibTableColumn
raisecomRemotePortInBroadcastPkts=_RaisecomRemotePortInBroadcastPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,7),_RaisecomRemotePortInBroadcastPkts_Type())
raisecomRemotePortInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortInBroadcastPkts.setStatus(_A)
_RaisecomRemotePortOutOctets_Type=Counter64
_RaisecomRemotePortOutOctets_Object=MibTableColumn
raisecomRemotePortOutOctets=_RaisecomRemotePortOutOctets_Object((1,3,6,1,4,1,8886,1,12,1,8,1,8),_RaisecomRemotePortOutOctets_Type())
raisecomRemotePortOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutOctets.setStatus(_A)
_RaisecomRemotePortOutPkts_Type=Counter64
_RaisecomRemotePortOutPkts_Object=MibTableColumn
raisecomRemotePortOutPkts=_RaisecomRemotePortOutPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,9),_RaisecomRemotePortOutPkts_Type())
raisecomRemotePortOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutPkts.setStatus(_A)
_RaisecomRemotePortOutUcastPkts_Type=Counter64
_RaisecomRemotePortOutUcastPkts_Object=MibTableColumn
raisecomRemotePortOutUcastPkts=_RaisecomRemotePortOutUcastPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,10),_RaisecomRemotePortOutUcastPkts_Type())
raisecomRemotePortOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutUcastPkts.setStatus(_A)
_RaisecomRemotePortOutMulticastPkts_Type=Counter64
_RaisecomRemotePortOutMulticastPkts_Object=MibTableColumn
raisecomRemotePortOutMulticastPkts=_RaisecomRemotePortOutMulticastPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,11),_RaisecomRemotePortOutMulticastPkts_Type())
raisecomRemotePortOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutMulticastPkts.setStatus(_A)
_RaisecomRemotePortOutBroadcastPkts_Type=Counter64
_RaisecomRemotePortOutBroadcastPkts_Object=MibTableColumn
raisecomRemotePortOutBroadcastPkts=_RaisecomRemotePortOutBroadcastPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,12),_RaisecomRemotePortOutBroadcastPkts_Type())
raisecomRemotePortOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOutBroadcastPkts.setStatus(_A)
_RaisecomRemotePortErrorPkts_Type=Counter32
_RaisecomRemotePortErrorPkts_Object=MibTableColumn
raisecomRemotePortErrorPkts=_RaisecomRemotePortErrorPkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,13),_RaisecomRemotePortErrorPkts_Type())
raisecomRemotePortErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortErrorPkts.setStatus(_A)
_RaisecomRemotePortDropEvents_Type=Counter32
_RaisecomRemotePortDropEvents_Object=MibTableColumn
raisecomRemotePortDropEvents=_RaisecomRemotePortDropEvents_Object((1,3,6,1,4,1,8886,1,12,1,8,1,14),_RaisecomRemotePortDropEvents_Type())
raisecomRemotePortDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortDropEvents.setStatus(_A)
_RaisecomRemotePortCRCAlignErrors_Type=Counter32
_RaisecomRemotePortCRCAlignErrors_Object=MibTableColumn
raisecomRemotePortCRCAlignErrors=_RaisecomRemotePortCRCAlignErrors_Object((1,3,6,1,4,1,8886,1,12,1,8,1,15),_RaisecomRemotePortCRCAlignErrors_Type())
raisecomRemotePortCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortCRCAlignErrors.setStatus(_A)
_RaisecomRemotePortUndersizePkts_Type=Counter32
_RaisecomRemotePortUndersizePkts_Object=MibTableColumn
raisecomRemotePortUndersizePkts=_RaisecomRemotePortUndersizePkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,16),_RaisecomRemotePortUndersizePkts_Type())
raisecomRemotePortUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortUndersizePkts.setStatus(_A)
_RaisecomRemotePortOversizePkts_Type=Counter32
_RaisecomRemotePortOversizePkts_Object=MibTableColumn
raisecomRemotePortOversizePkts=_RaisecomRemotePortOversizePkts_Object((1,3,6,1,4,1,8886,1,12,1,8,1,17),_RaisecomRemotePortOversizePkts_Type())
raisecomRemotePortOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortOversizePkts.setStatus(_A)
_RaisecomRemotePortFragments_Type=Counter32
_RaisecomRemotePortFragments_Object=MibTableColumn
raisecomRemotePortFragments=_RaisecomRemotePortFragments_Object((1,3,6,1,4,1,8886,1,12,1,8,1,18),_RaisecomRemotePortFragments_Type())
raisecomRemotePortFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortFragments.setStatus(_A)
_RaisecomRemotePortJabbers_Type=Counter32
_RaisecomRemotePortJabbers_Object=MibTableColumn
raisecomRemotePortJabbers=_RaisecomRemotePortJabbers_Object((1,3,6,1,4,1,8886,1,12,1,8,1,19),_RaisecomRemotePortJabbers_Type())
raisecomRemotePortJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortJabbers.setStatus(_A)
_RaisecomRemotePortCollisions_Type=Counter32
_RaisecomRemotePortCollisions_Object=MibTableColumn
raisecomRemotePortCollisions=_RaisecomRemotePortCollisions_Object((1,3,6,1,4,1,8886,1,12,1,8,1,20),_RaisecomRemotePortCollisions_Type())
raisecomRemotePortCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemotePortCollisions.setStatus(_A)
_RaisecomRemoteSfpTable_Object=MibTable
raisecomRemoteSfpTable=_RaisecomRemoteSfpTable_Object((1,3,6,1,4,1,8886,1,12,1,9))
if mibBuilder.loadTexts:raisecomRemoteSfpTable.setStatus(_A)
_RaisecomRemoteSfpEntry_Object=MibTableRow
raisecomRemoteSfpEntry=_RaisecomRemoteSfpEntry_Object((1,3,6,1,4,1,8886,1,12,1,9,1))
raisecomRemoteSfpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpEntry.setStatus(_A)
_RaisecomRemoteSfpInterfaceId_Type=Integer32
_RaisecomRemoteSfpInterfaceId_Object=MibTableColumn
raisecomRemoteSfpInterfaceId=_RaisecomRemoteSfpInterfaceId_Object((1,3,6,1,4,1,8886,1,12,1,9,1,1),_RaisecomRemoteSfpInterfaceId_Type())
raisecomRemoteSfpInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpInterfaceId.setStatus(_A)
class _RaisecomRemoteSfpExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exist',1),('notexist',2)))
_RaisecomRemoteSfpExist_Type.__name__=_C
_RaisecomRemoteSfpExist_Object=MibTableColumn
raisecomRemoteSfpExist=_RaisecomRemoteSfpExist_Object((1,3,6,1,4,1,8886,1,12,1,9,1,2),_RaisecomRemoteSfpExist_Type())
raisecomRemoteSfpExist.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpExist.setStatus(_A)
class _RaisecomRemoteSfpMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('fibersingle',0),('fiber50um',1),('fiber625um',2),('copper',3)))
_RaisecomRemoteSfpMediaType_Type.__name__=_C
_RaisecomRemoteSfpMediaType_Object=MibTableColumn
raisecomRemoteSfpMediaType=_RaisecomRemoteSfpMediaType_Object((1,3,6,1,4,1,8886,1,12,1,9,1,3),_RaisecomRemoteSfpMediaType_Type())
raisecomRemoteSfpMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpMediaType.setStatus(_A)
class _RaisecomRemoteSfpRXLOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('alarm',2)))
_RaisecomRemoteSfpRXLOS_Type.__name__=_C
_RaisecomRemoteSfpRXLOS_Object=MibTableColumn
raisecomRemoteSfpRXLOS=_RaisecomRemoteSfpRXLOS_Object((1,3,6,1,4,1,8886,1,12,1,9,1,4),_RaisecomRemoteSfpRXLOS_Type())
raisecomRemoteSfpRXLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpRXLOS.setStatus(_A)
class _RaisecomRemoteSfpTXFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('alarm',2)))
_RaisecomRemoteSfpTXFault_Type.__name__=_C
_RaisecomRemoteSfpTXFault_Object=MibTableColumn
raisecomRemoteSfpTXFault=_RaisecomRemoteSfpTXFault_Object((1,3,6,1,4,1,8886,1,12,1,9,1,5),_RaisecomRemoteSfpTXFault_Type())
raisecomRemoteSfpTXFault.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpTXFault.setStatus(_A)
class _RaisecomRemoteSfpTXDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_RaisecomRemoteSfpTXDisable_Type.__name__=_C
_RaisecomRemoteSfpTXDisable_Object=MibTableColumn
raisecomRemoteSfpTXDisable=_RaisecomRemoteSfpTXDisable_Object((1,3,6,1,4,1,8886,1,12,1,9,1,6),_RaisecomRemoteSfpTXDisable_Type())
raisecomRemoteSfpTXDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteSfpTXDisable.setStatus(_A)
class _RaisecomRemoteSfpModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('gbic',2),('sff',3),('sfp',4)))
_RaisecomRemoteSfpModuleType_Type.__name__=_C
_RaisecomRemoteSfpModuleType_Object=MibTableColumn
raisecomRemoteSfpModuleType=_RaisecomRemoteSfpModuleType_Object((1,3,6,1,4,1,8886,1,12,1,9,1,7),_RaisecomRemoteSfpModuleType_Type())
raisecomRemoteSfpModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpModuleType.setStatus(_A)
class _RaisecomRemoteSfpOpticalInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,7,34)));namedValues=NamedValues(*((_K,0),('sc',1),('lc',7),('rj45',34)))
_RaisecomRemoteSfpOpticalInterface_Type.__name__=_C
_RaisecomRemoteSfpOpticalInterface_Object=MibTableColumn
raisecomRemoteSfpOpticalInterface=_RaisecomRemoteSfpOpticalInterface_Object((1,3,6,1,4,1,8886,1,12,1,9,1,8),_RaisecomRemoteSfpOpticalInterface_Type())
raisecomRemoteSfpOpticalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpOpticalInterface.setStatus(_A)
class _RaisecomRemoteSfpSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,6,12,25)));namedValues=NamedValues(*((_K,0),('speed125M',1),('speed155M',2),('speed622M',6),('speed1250M',12),('speed2500M',25)))
_RaisecomRemoteSfpSpeedStatus_Type.__name__=_C
_RaisecomRemoteSfpSpeedStatus_Object=MibTableColumn
raisecomRemoteSfpSpeedStatus=_RaisecomRemoteSfpSpeedStatus_Object((1,3,6,1,4,1,8886,1,12,1,9,1,9),_RaisecomRemoteSfpSpeedStatus_Type())
raisecomRemoteSfpSpeedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpSpeedStatus.setStatus(_A)
class _RaisecomRemoteSfpTransportDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomRemoteSfpTransportDistance_Type.__name__=_C
_RaisecomRemoteSfpTransportDistance_Object=MibTableColumn
raisecomRemoteSfpTransportDistance=_RaisecomRemoteSfpTransportDistance_Object((1,3,6,1,4,1,8886,1,12,1,9,1,10),_RaisecomRemoteSfpTransportDistance_Type())
raisecomRemoteSfpTransportDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpTransportDistance.setStatus(_A)
class _RaisecomRemoteSfpWaveLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomRemoteSfpWaveLength_Type.__name__=_C
_RaisecomRemoteSfpWaveLength_Object=MibTableColumn
raisecomRemoteSfpWaveLength=_RaisecomRemoteSfpWaveLength_Object((1,3,6,1,4,1,8886,1,12,1,9,1,11),_RaisecomRemoteSfpWaveLength_Type())
raisecomRemoteSfpWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpWaveLength.setStatus(_A)
class _RaisecomRemoteSfpVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RaisecomRemoteSfpVendor_Type.__name__=_H
_RaisecomRemoteSfpVendor_Object=MibTableColumn
raisecomRemoteSfpVendor=_RaisecomRemoteSfpVendor_Object((1,3,6,1,4,1,8886,1,12,1,9,1,12),_RaisecomRemoteSfpVendor_Type())
raisecomRemoteSfpVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpVendor.setStatus(_A)
class _RaisecomRemoteSfpProductType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RaisecomRemoteSfpProductType_Type.__name__=_H
_RaisecomRemoteSfpProductType_Object=MibTableColumn
raisecomRemoteSfpProductType=_RaisecomRemoteSfpProductType_Object((1,3,6,1,4,1,8886,1,12,1,9,1,13),_RaisecomRemoteSfpProductType_Type())
raisecomRemoteSfpProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpProductType.setStatus(_A)
class _RaisecomRemoteSfpVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_RaisecomRemoteSfpVersion_Type.__name__=_H
_RaisecomRemoteSfpVersion_Object=MibTableColumn
raisecomRemoteSfpVersion=_RaisecomRemoteSfpVersion_Object((1,3,6,1,4,1,8886,1,12,1,9,1,14),_RaisecomRemoteSfpVersion_Type())
raisecomRemoteSfpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpVersion.setStatus(_A)
class _RaisecomRemoteSfpSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RaisecomRemoteSfpSerialNumber_Type.__name__=_H
_RaisecomRemoteSfpSerialNumber_Object=MibTableColumn
raisecomRemoteSfpSerialNumber=_RaisecomRemoteSfpSerialNumber_Object((1,3,6,1,4,1,8886,1,12,1,9,1,15),_RaisecomRemoteSfpSerialNumber_Type())
raisecomRemoteSfpSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpSerialNumber.setStatus(_A)
_RaisecomRemoteDtTable_Object=MibTable
raisecomRemoteDtTable=_RaisecomRemoteDtTable_Object((1,3,6,1,4,1,8886,1,12,1,10))
if mibBuilder.loadTexts:raisecomRemoteDtTable.setStatus(_A)
_RaisecomRemoteDtEntry_Object=MibTableRow
raisecomRemoteDtEntry=_RaisecomRemoteDtEntry_Object((1,3,6,1,4,1,8886,1,12,1,10,1))
raisecomRemoteDtEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteDtEntry.setStatus(_A)
class _RaisecomRemoteDtSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transparent',1),('dot1q-vlan',2),('double-tagged-vlan',3)))
_RaisecomRemoteDtSwitchMode_Type.__name__=_C
_RaisecomRemoteDtSwitchMode_Object=MibTableColumn
raisecomRemoteDtSwitchMode=_RaisecomRemoteDtSwitchMode_Object((1,3,6,1,4,1,8886,1,12,1,10,1,1),_RaisecomRemoteDtSwitchMode_Type())
raisecomRemoteDtSwitchMode.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteDtSwitchMode.setStatus(_A)
class _RaisecomRemoteDtOuterTpid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomRemoteDtOuterTpid_Type.__name__=_C
_RaisecomRemoteDtOuterTpid_Object=MibTableColumn
raisecomRemoteDtOuterTpid=_RaisecomRemoteDtOuterTpid_Object((1,3,6,1,4,1,8886,1,12,1,10,1,2),_RaisecomRemoteDtOuterTpid_Type())
raisecomRemoteDtOuterTpid.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteDtOuterTpid.setStatus(_A)
class _RaisecomRemoteDtNativeVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomRemoteDtNativeVlan_Type.__name__=_C
_RaisecomRemoteDtNativeVlan_Object=MibTableColumn
raisecomRemoteDtNativeVlan=_RaisecomRemoteDtNativeVlan_Object((1,3,6,1,4,1,8886,1,12,1,10,1,3),_RaisecomRemoteDtNativeVlan_Type())
raisecomRemoteDtNativeVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteDtNativeVlan.setStatus(_A)
class _RaisecomRemoteDtAccessPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('line',1),('client',2)))
_RaisecomRemoteDtAccessPort_Type.__name__=_C
_RaisecomRemoteDtAccessPort_Object=MibTableColumn
raisecomRemoteDtAccessPort=_RaisecomRemoteDtAccessPort_Object((1,3,6,1,4,1,8886,1,12,1,10,1,4),_RaisecomRemoteDtAccessPort_Type())
raisecomRemoteDtAccessPort.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteDtAccessPort.setStatus(_A)
_RaisecomRemoteSendConfTable_Object=MibTable
raisecomRemoteSendConfTable=_RaisecomRemoteSendConfTable_Object((1,3,6,1,4,1,8886,1,12,1,11))
if mibBuilder.loadTexts:raisecomRemoteSendConfTable.setStatus(_A)
_RaisecomRemoteSendConfEntry_Object=MibTableRow
raisecomRemoteSendConfEntry=_RaisecomRemoteSendConfEntry_Object((1,3,6,1,4,1,8886,1,12,1,11,1))
raisecomRemoteSendConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSendConfEntry.setStatus(_A)
class _RaisecomRemoteSendConf_Type(RcRemoteConfigFrameSendStatus):defaultValue=5
_RaisecomRemoteSendConf_Type.__name__=_Q
_RaisecomRemoteSendConf_Object=MibTableColumn
raisecomRemoteSendConf=_RaisecomRemoteSendConf_Object((1,3,6,1,4,1,8886,1,12,1,11,1,1),_RaisecomRemoteSendConf_Type())
raisecomRemoteSendConf.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteSendConf.setStatus(_A)
_RaisecomRemoteInLoopbackTable_Object=MibTable
raisecomRemoteInLoopbackTable=_RaisecomRemoteInLoopbackTable_Object((1,3,6,1,4,1,8886,1,12,1,12))
if mibBuilder.loadTexts:raisecomRemoteInLoopbackTable.setStatus(_A)
_RaisecomRemoteInLoopbackEntry_Object=MibTableRow
raisecomRemoteInLoopbackEntry=_RaisecomRemoteInLoopbackEntry_Object((1,3,6,1,4,1,8886,1,12,1,12,1))
raisecomRemoteInLoopbackEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteInLoopbackEntry.setStatus(_A)
class _RaisecomRemoteInLoopbackMacExchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exchange',1),('noexchange',2)))
_RaisecomRemoteInLoopbackMacExchange_Type.__name__=_C
_RaisecomRemoteInLoopbackMacExchange_Object=MibTableColumn
raisecomRemoteInLoopbackMacExchange=_RaisecomRemoteInLoopbackMacExchange_Object((1,3,6,1,4,1,8886,1,12,1,12,1,1),_RaisecomRemoteInLoopbackMacExchange_Type())
raisecomRemoteInLoopbackMacExchange.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteInLoopbackMacExchange.setStatus(_A)
class _RaisecomRemoteInLoopbackCrcRecalSet_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_RaisecomRemoteInLoopbackCrcRecalSet_Type.__name__=_C
_RaisecomRemoteInLoopbackCrcRecalSet_Object=MibTableColumn
raisecomRemoteInLoopbackCrcRecalSet=_RaisecomRemoteInLoopbackCrcRecalSet_Object((1,3,6,1,4,1,8886,1,12,1,12,1,2),_RaisecomRemoteInLoopbackCrcRecalSet_Type())
raisecomRemoteInLoopbackCrcRecalSet.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteInLoopbackCrcRecalSet.setStatus(_A)
class _RaisecomRemoteInLoopbackCrcRecal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_RaisecomRemoteInLoopbackCrcRecal_Type.__name__=_C
_RaisecomRemoteInLoopbackCrcRecal_Object=MibTableColumn
raisecomRemoteInLoopbackCrcRecal=_RaisecomRemoteInLoopbackCrcRecal_Object((1,3,6,1,4,1,8886,1,12,1,12,1,3),_RaisecomRemoteInLoopbackCrcRecal_Type())
raisecomRemoteInLoopbackCrcRecal.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteInLoopbackCrcRecal.setStatus(_A)
class _RaisecomRemoteInLoopbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noloopback',1),('initiatinginloopback',2),('inloopback',3),('outloopback',4),('terminatingInloopback',5)))
_RaisecomRemoteInLoopbackStatus_Type.__name__=_C
_RaisecomRemoteInLoopbackStatus_Object=MibTableColumn
raisecomRemoteInLoopbackStatus=_RaisecomRemoteInLoopbackStatus_Object((1,3,6,1,4,1,8886,1,12,1,12,1,4),_RaisecomRemoteInLoopbackStatus_Type())
raisecomRemoteInLoopbackStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteInLoopbackStatus.setStatus(_A)
_RaisecomRemoteVctTable_Object=MibTable
raisecomRemoteVctTable=_RaisecomRemoteVctTable_Object((1,3,6,1,4,1,8886,1,12,1,13))
if mibBuilder.loadTexts:raisecomRemoteVctTable.setStatus(_A)
_RaisecomRemoteVctEntry_Object=MibTableRow
raisecomRemoteVctEntry=_RaisecomRemoteVctEntry_Object((1,3,6,1,4,1,8886,1,12,1,13,1))
raisecomRemoteVctEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteVctEntry.setStatus(_A)
class _RaisecomRemoteVctAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unSupported',1),('neverIssued',2),('issued',3),('testing',4),('begin',5)))
_RaisecomRemoteVctAttribute_Type.__name__=_C
_RaisecomRemoteVctAttribute_Object=MibTableColumn
raisecomRemoteVctAttribute=_RaisecomRemoteVctAttribute_Object((1,3,6,1,4,1,8886,1,12,1,13,1,1),_RaisecomRemoteVctAttribute_Type())
raisecomRemoteVctAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteVctAttribute.setStatus(_A)
class _RaisecomRemoteVctStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('open',2),('shorted',3),('error',4),('invalidation',5)))
_RaisecomRemoteVctStatus_Type.__name__=_C
_RaisecomRemoteVctStatus_Object=MibTableColumn
raisecomRemoteVctStatus=_RaisecomRemoteVctStatus_Object((1,3,6,1,4,1,8886,1,12,1,13,1,2),_RaisecomRemoteVctStatus_Type())
raisecomRemoteVctStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVctStatus.setStatus(_A)
_RaisecomRemoteVctLength_Type=Integer32
_RaisecomRemoteVctLength_Object=MibTableColumn
raisecomRemoteVctLength=_RaisecomRemoteVctLength_Object((1,3,6,1,4,1,8886,1,12,1,13,1,3),_RaisecomRemoteVctLength_Type())
raisecomRemoteVctLength.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteVctLength.setStatus(_A)
_RaisecomRemoteVlanConfigTable_Object=MibTable
raisecomRemoteVlanConfigTable=_RaisecomRemoteVlanConfigTable_Object((1,3,6,1,4,1,8886,1,12,1,14))
if mibBuilder.loadTexts:raisecomRemoteVlanConfigTable.setStatus(_A)
_RaisecomRemoteVlanConfigEntry_Object=MibTableRow
raisecomRemoteVlanConfigEntry=_RaisecomRemoteVlanConfigEntry_Object((1,3,6,1,4,1,8886,1,12,1,14,1))
raisecomRemoteVlanConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteVlanConfigEntry.setStatus(_A)
_RaisecomRemoteVlanStatus_Type=RcRemoteVlanStatus
_RaisecomRemoteVlanStatus_Object=MibTableColumn
raisecomRemoteVlanStatus=_RaisecomRemoteVlanStatus_Object((1,3,6,1,4,1,8886,1,12,1,14,1,1),_RaisecomRemoteVlanStatus_Type())
raisecomRemoteVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteVlanStatus.setStatus(_A)
_RaisecomRemoteCosStatus_Type=TruthValue
_RaisecomRemoteCosStatus_Object=MibTableColumn
raisecomRemoteCosStatus=_RaisecomRemoteCosStatus_Object((1,3,6,1,4,1,8886,1,12,1,14,1,2),_RaisecomRemoteCosStatus_Type())
raisecomRemoteCosStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCosStatus.setStatus(_A)
_RaisecomRemoteFiberPortTagType_Type=RcRemotePortTagStatus
_RaisecomRemoteFiberPortTagType_Object=MibTableColumn
raisecomRemoteFiberPortTagType=_RaisecomRemoteFiberPortTagType_Object((1,3,6,1,4,1,8886,1,12,1,14,1,3),_RaisecomRemoteFiberPortTagType_Type())
raisecomRemoteFiberPortTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteFiberPortTagType.setStatus(_A)
class _RaisecomRemoteFiberPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomRemoteFiberPortPriority_Type.__name__=_C
_RaisecomRemoteFiberPortPriority_Object=MibTableColumn
raisecomRemoteFiberPortPriority=_RaisecomRemoteFiberPortPriority_Object((1,3,6,1,4,1,8886,1,12,1,14,1,4),_RaisecomRemoteFiberPortPriority_Type())
raisecomRemoteFiberPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteFiberPortPriority.setStatus(_A)
class _RaisecomRemoteFiberPortPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomRemoteFiberPortPvid_Type.__name__=_C
_RaisecomRemoteFiberPortPvid_Object=MibTableColumn
raisecomRemoteFiberPortPvid=_RaisecomRemoteFiberPortPvid_Object((1,3,6,1,4,1,8886,1,12,1,14,1,5),_RaisecomRemoteFiberPortPvid_Type())
raisecomRemoteFiberPortPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteFiberPortPvid.setStatus(_A)
_RaisecomRemoteCablePortTagType_Type=RcRemotePortTagStatus
_RaisecomRemoteCablePortTagType_Object=MibTableColumn
raisecomRemoteCablePortTagType=_RaisecomRemoteCablePortTagType_Object((1,3,6,1,4,1,8886,1,12,1,14,1,6),_RaisecomRemoteCablePortTagType_Type())
raisecomRemoteCablePortTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCablePortTagType.setStatus(_A)
class _RaisecomRemoteCablePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomRemoteCablePortPriority_Type.__name__=_C
_RaisecomRemoteCablePortPriority_Object=MibTableColumn
raisecomRemoteCablePortPriority=_RaisecomRemoteCablePortPriority_Object((1,3,6,1,4,1,8886,1,12,1,14,1,7),_RaisecomRemoteCablePortPriority_Type())
raisecomRemoteCablePortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCablePortPriority.setStatus(_A)
class _RaisecomRemoteCablePortPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomRemoteCablePortPvid_Type.__name__=_C
_RaisecomRemoteCablePortPvid_Object=MibTableColumn
raisecomRemoteCablePortPvid=_RaisecomRemoteCablePortPvid_Object((1,3,6,1,4,1,8886,1,12,1,14,1,8),_RaisecomRemoteCablePortPvid_Type())
raisecomRemoteCablePortPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCablePortPvid.setStatus(_A)
_RaisecomRemoteCpuPortTagType_Type=RcRemotePortTagStatus
_RaisecomRemoteCpuPortTagType_Object=MibTableColumn
raisecomRemoteCpuPortTagType=_RaisecomRemoteCpuPortTagType_Object((1,3,6,1,4,1,8886,1,12,1,14,1,9),_RaisecomRemoteCpuPortTagType_Type())
raisecomRemoteCpuPortTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCpuPortTagType.setStatus(_A)
class _RaisecomRemoteCpuPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomRemoteCpuPortPriority_Type.__name__=_C
_RaisecomRemoteCpuPortPriority_Object=MibTableColumn
raisecomRemoteCpuPortPriority=_RaisecomRemoteCpuPortPriority_Object((1,3,6,1,4,1,8886,1,12,1,14,1,10),_RaisecomRemoteCpuPortPriority_Type())
raisecomRemoteCpuPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCpuPortPriority.setStatus(_A)
class _RaisecomRemoteCpuPortPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomRemoteCpuPortPvid_Type.__name__=_C
_RaisecomRemoteCpuPortPvid_Object=MibTableColumn
raisecomRemoteCpuPortPvid=_RaisecomRemoteCpuPortPvid_Object((1,3,6,1,4,1,8886,1,12,1,14,1,11),_RaisecomRemoteCpuPortPvid_Type())
raisecomRemoteCpuPortPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteCpuPortPvid.setStatus(_A)
class _RaisecomRemoteSendVlanConf_Type(RcRemoteConfigFrameSendStatus):defaultValue=5
_RaisecomRemoteSendVlanConf_Type.__name__=_Q
_RaisecomRemoteSendVlanConf_Object=MibTableColumn
raisecomRemoteSendVlanConf=_RaisecomRemoteSendVlanConf_Object((1,3,6,1,4,1,8886,1,12,1,14,1,12),_RaisecomRemoteSendVlanConf_Type())
raisecomRemoteSendVlanConf.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteSendVlanConf.setStatus(_A)
_RaisecomRemoteVlanGroupTable_Object=MibTable
raisecomRemoteVlanGroupTable=_RaisecomRemoteVlanGroupTable_Object((1,3,6,1,4,1,8886,1,12,1,15))
if mibBuilder.loadTexts:raisecomRemoteVlanGroupTable.setStatus(_A)
_RaisecomRemoteVlanGroupEntry_Object=MibTableRow
raisecomRemoteVlanGroupEntry=_RaisecomRemoteVlanGroupEntry_Object((1,3,6,1,4,1,8886,1,12,1,15,1))
raisecomRemoteVlanGroupEntry.setIndexNames((0,_E,_F),(0,_G,_j))
if mibBuilder.loadTexts:raisecomRemoteVlanGroupEntry.setStatus(_A)
class _RaisecomRemoteVlanGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_RaisecomRemoteVlanGroupIndex_Type.__name__=_C
_RaisecomRemoteVlanGroupIndex_Object=MibTableColumn
raisecomRemoteVlanGroupIndex=_RaisecomRemoteVlanGroupIndex_Object((1,3,6,1,4,1,8886,1,12,1,15,1,1),_RaisecomRemoteVlanGroupIndex_Type())
raisecomRemoteVlanGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomRemoteVlanGroupIndex.setStatus(_A)
class _RaisecomRemoteVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RaisecomRemoteVlanId_Type.__name__=_C
_RaisecomRemoteVlanId_Object=MibTableColumn
raisecomRemoteVlanId=_RaisecomRemoteVlanId_Object((1,3,6,1,4,1,8886,1,12,1,15,1,2),_RaisecomRemoteVlanId_Type())
raisecomRemoteVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteVlanId.setStatus(_A)
class _RaisecomRemoteVlanMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomRemoteVlanMember_Type.__name__=_C
_RaisecomRemoteVlanMember_Object=MibTableColumn
raisecomRemoteVlanMember=_RaisecomRemoteVlanMember_Object((1,3,6,1,4,1,8886,1,12,1,15,1,3),_RaisecomRemoteVlanMember_Type())
raisecomRemoteVlanMember.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomRemoteVlanMember.setStatus(_A)
_RaisecomRemoteSfpDdmTable_Object=MibTable
raisecomRemoteSfpDdmTable=_RaisecomRemoteSfpDdmTable_Object((1,3,6,1,4,1,8886,1,12,1,16))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmTable.setStatus(_A)
_RaisecomRemoteSfpDdmEntry_Object=MibTableRow
raisecomRemoteSfpDdmEntry=_RaisecomRemoteSfpDdmEntry_Object((1,3,6,1,4,1,8886,1,12,1,16,1))
raisecomRemoteSfpDdmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmEntry.setStatus(_A)
_RaisecomRemoteSfpDdmValid_Type=TruthValue
_RaisecomRemoteSfpDdmValid_Object=MibTableColumn
raisecomRemoteSfpDdmValid=_RaisecomRemoteSfpDdmValid_Object((1,3,6,1,4,1,8886,1,12,1,16,1,1),_RaisecomRemoteSfpDdmValid_Type())
raisecomRemoteSfpDdmValid.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmValid.setStatus(_A)
_RaisecomRemoteSfpDdmMode_Type=RcRemoteSfpDdmMode
_RaisecomRemoteSfpDdmMode_Object=MibTableColumn
raisecomRemoteSfpDdmMode=_RaisecomRemoteSfpDdmMode_Object((1,3,6,1,4,1,8886,1,12,1,16,1,2),_RaisecomRemoteSfpDdmMode_Type())
raisecomRemoteSfpDdmMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmMode.setStatus(_A)
class _RaisecomRemoteSfpDdmTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128000,127996))
_RaisecomRemoteSfpDdmTemperature_Type.__name__=_C
_RaisecomRemoteSfpDdmTemperature_Object=MibTableColumn
raisecomRemoteSfpDdmTemperature=_RaisecomRemoteSfpDdmTemperature_Object((1,3,6,1,4,1,8886,1,12,1,16,1,3),_RaisecomRemoteSfpDdmTemperature_Type())
raisecomRemoteSfpDdmTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmTemperature.setStatus(_A)
class _RaisecomRemoteSfpDdmSupplyVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_RaisecomRemoteSfpDdmSupplyVolt_Type.__name__=_C
_RaisecomRemoteSfpDdmSupplyVolt_Object=MibTableColumn
raisecomRemoteSfpDdmSupplyVolt=_RaisecomRemoteSfpDdmSupplyVolt_Object((1,3,6,1,4,1,8886,1,12,1,16,1,4),_RaisecomRemoteSfpDdmSupplyVolt_Type())
raisecomRemoteSfpDdmSupplyVolt.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmSupplyVolt.setStatus(_A)
class _RaisecomRemoteSfpDdmBiasCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_RaisecomRemoteSfpDdmBiasCurrent_Type.__name__=_C
_RaisecomRemoteSfpDdmBiasCurrent_Object=MibTableColumn
raisecomRemoteSfpDdmBiasCurrent=_RaisecomRemoteSfpDdmBiasCurrent_Object((1,3,6,1,4,1,8886,1,12,1,16,1,5),_RaisecomRemoteSfpDdmBiasCurrent_Type())
raisecomRemoteSfpDdmBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmBiasCurrent.setStatus(_A)
class _RaisecomRemoteSfpDdmOpticalTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomRemoteSfpDdmOpticalTxPower_Type.__name__=_C
_RaisecomRemoteSfpDdmOpticalTxPower_Object=MibTableColumn
raisecomRemoteSfpDdmOpticalTxPower=_RaisecomRemoteSfpDdmOpticalTxPower_Object((1,3,6,1,4,1,8886,1,12,1,16,1,6),_RaisecomRemoteSfpDdmOpticalTxPower_Type())
raisecomRemoteSfpDdmOpticalTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmOpticalTxPower.setStatus(_A)
class _RaisecomRemoteSfpDdmOpticalRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomRemoteSfpDdmOpticalRxPower_Type.__name__=_C
_RaisecomRemoteSfpDdmOpticalRxPower_Object=MibTableColumn
raisecomRemoteSfpDdmOpticalRxPower=_RaisecomRemoteSfpDdmOpticalRxPower_Object((1,3,6,1,4,1,8886,1,12,1,16,1,7),_RaisecomRemoteSfpDdmOpticalRxPower_Type())
raisecomRemoteSfpDdmOpticalRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmOpticalRxPower.setStatus(_A)
_RaisecomRemoteSfpDdmAlarm_Type=TruthValue
_RaisecomRemoteSfpDdmAlarm_Object=MibTableColumn
raisecomRemoteSfpDdmAlarm=_RaisecomRemoteSfpDdmAlarm_Object((1,3,6,1,4,1,8886,1,12,1,16,1,8),_RaisecomRemoteSfpDdmAlarm_Type())
raisecomRemoteSfpDdmAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmAlarm.setStatus(_A)
_RaisecomRemoteSfpDdmAlarmTemStatus_Type=RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmTemStatus_Object=MibTableColumn
raisecomRemoteSfpDdmAlarmTemStatus=_RaisecomRemoteSfpDdmAlarmTemStatus_Object((1,3,6,1,4,1,8886,1,12,1,16,1,9),_RaisecomRemoteSfpDdmAlarmTemStatus_Type())
raisecomRemoteSfpDdmAlarmTemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmAlarmTemStatus.setStatus(_A)
_RaisecomRemoteSfpDdmAlarmVoltStatus_Type=RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmVoltStatus_Object=MibTableColumn
raisecomRemoteSfpDdmAlarmVoltStatus=_RaisecomRemoteSfpDdmAlarmVoltStatus_Object((1,3,6,1,4,1,8886,1,12,1,16,1,10),_RaisecomRemoteSfpDdmAlarmVoltStatus_Type())
raisecomRemoteSfpDdmAlarmVoltStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmAlarmVoltStatus.setStatus(_A)
_RaisecomRemoteSfpDdmAlarmCurrentStatus_Type=RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmCurrentStatus_Object=MibTableColumn
raisecomRemoteSfpDdmAlarmCurrentStatus=_RaisecomRemoteSfpDdmAlarmCurrentStatus_Object((1,3,6,1,4,1,8886,1,12,1,16,1,11),_RaisecomRemoteSfpDdmAlarmCurrentStatus_Type())
raisecomRemoteSfpDdmAlarmCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmAlarmCurrentStatus.setStatus(_A)
_RaisecomRemoteSfpDdmAlarmTxPowerStatus_Type=RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmTxPowerStatus_Object=MibTableColumn
raisecomRemoteSfpDdmAlarmTxPowerStatus=_RaisecomRemoteSfpDdmAlarmTxPowerStatus_Object((1,3,6,1,4,1,8886,1,12,1,16,1,12),_RaisecomRemoteSfpDdmAlarmTxPowerStatus_Type())
raisecomRemoteSfpDdmAlarmTxPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmAlarmTxPowerStatus.setStatus(_A)
_RaisecomRemoteSfpDdmAlarmRxPowerStatus_Type=RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmRxPowerStatus_Object=MibTableColumn
raisecomRemoteSfpDdmAlarmRxPowerStatus=_RaisecomRemoteSfpDdmAlarmRxPowerStatus_Object((1,3,6,1,4,1,8886,1,12,1,16,1,13),_RaisecomRemoteSfpDdmAlarmRxPowerStatus_Type())
raisecomRemoteSfpDdmAlarmRxPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomRemoteSfpDdmAlarmRxPowerStatus.setStatus(_A)
_RaisecomRemoteManagementLocalMibTraps_ObjectIdentity=ObjectIdentity
raisecomRemoteManagementLocalMibTraps=_RaisecomRemoteManagementLocalMibTraps_ObjectIdentity((1,3,6,1,4,1,8886,1,12,2))
raisecomRemotePortLinkUp=NotificationType((1,3,6,1,4,1,8886,1,12,2,1))
raisecomRemotePortLinkUp.setObjects(*((_E,_F),(_G,_L)))
if mibBuilder.loadTexts:raisecomRemotePortLinkUp.setStatus(_A)
raisecomRemotePortLinkDown=NotificationType((1,3,6,1,4,1,8886,1,12,2,2))
raisecomRemotePortLinkDown.setObjects(*((_E,_F),(_G,_L)))
if mibBuilder.loadTexts:raisecomRemotePortLinkDown.setStatus(_A)
raisecomRemoteSfpDdmTemNormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,3))
raisecomRemoteSfpDdmTemNormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmTemNormal.setStatus(_A)
raisecomRemoteSfpDdmTemAbnormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,4))
raisecomRemoteSfpDdmTemAbnormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmTemAbnormal.setStatus(_A)
raisecomRemoteSfpDdmVoltNormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,5))
raisecomRemoteSfpDdmVoltNormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmVoltNormal.setStatus(_A)
raisecomRemoteSfpDdmVoltAbnormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,6))
raisecomRemoteSfpDdmVoltAbnormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmVoltAbnormal.setStatus(_A)
raisecomRemoteSfpDdmCurrentNormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,7))
raisecomRemoteSfpDdmCurrentNormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmCurrentNormal.setStatus(_A)
raisecomRemoteSfpDdmCurrentAbnormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,8))
raisecomRemoteSfpDdmCurrentAbnormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmCurrentAbnormal.setStatus(_A)
raisecomRemoteSfpDdmTxPowerNomal=NotificationType((1,3,6,1,4,1,8886,1,12,2,9))
raisecomRemoteSfpDdmTxPowerNomal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmTxPowerNomal.setStatus(_A)
raisecomRemoteSfpDdmTxPowerAbnormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,10))
raisecomRemoteSfpDdmTxPowerAbnormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmTxPowerAbnormal.setStatus(_A)
raisecomRemoteSfpDdmRxPowerNormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,11))
raisecomRemoteSfpDdmRxPowerNormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmRxPowerNormal.setStatus(_A)
raisecomRemoteSfpDdmRxPowerAbnormal=NotificationType((1,3,6,1,4,1,8886,1,12,2,12))
raisecomRemoteSfpDdmRxPowerAbnormal.setObjects((_E,_F))
if mibBuilder.loadTexts:raisecomRemoteSfpDdmRxPowerAbnormal.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'RcRemoteVlanStatus':RcRemoteVlanStatus,'RcRemotePortTagStatus':RcRemotePortTagStatus,_Q:RcRemoteConfigFrameSendStatus,'RcRemoteSfpDdmMode':RcRemoteSfpDdmMode,'RcRemoteSfpDdmAlarmStatus':RcRemoteSfpDdmAlarmStatus,'raisecomRemoteManagementLocal':raisecomRemoteManagementLocal,'raisecomRemoteManagementLocalMibObjects':raisecomRemoteManagementLocalMibObjects,'raisecomRemoteTrapEnable':raisecomRemoteTrapEnable,'raisecomRemoteInvariableInfoTable':raisecomRemoteInvariableInfoTable,'raisecomRemoteInvariableInfoEntry':raisecomRemoteInvariableInfoEntry,_T:raisecomRemoteInvariableInfoIndex,'raisecomRemoteSysOid':raisecomRemoteSysOid,'raisecomRemoteModuleType':raisecomRemoteModuleType,'raisecomRemoteOidCapability':raisecomRemoteOidCapability,'raisecomRemoteFileTransCapability':raisecomRemoteFileTransCapability,'raisecomRemoteOtherCapability':raisecomRemoteOtherCapability,'raisecomRemoteMainChipId':raisecomRemoteMainChipId,'raisecomRemoteFpgaChipId':raisecomRemoteFpgaChipId,'raisecomRemoteFpgaSwVer':raisecomRemoteFpgaSwVer,'raisecomRemoteSystemSwVer':raisecomRemoteSystemSwVer,'raisecomRemoteSystemHwVer':raisecomRemoteSystemHwVer,'raisecomRemotePortNum':raisecomRemotePortNum,'raisecomRemoteDeviceName':raisecomRemoteDeviceName,'raisecomRemoteInvariableInfoStatus':raisecomRemoteInvariableInfoStatus,'raisecomRemoteEnvironmentTable':raisecomRemoteEnvironmentTable,'raisecomRemoteEnvironmentEntry':raisecomRemoteEnvironmentEntry,_U:raisecomRemoteEnvironmentIndex,'raisecomRemoteTemperature':raisecomRemoteTemperature,'raisecomRemoteVolt3300':raisecomRemoteVolt3300,'raisecomRemoteVolt2500':raisecomRemoteVolt2500,'raisecomRemoteVolt1800':raisecomRemoteVolt1800,'raisecomRemoteVolt1200':raisecomRemoteVolt1200,'raisecomRemoteVoltNormal':raisecomRemoteVoltNormal,'raisecomRemoteSysCfgTable':raisecomRemoteSysCfgTable,'raisecomRemoteSysCfgEntry':raisecomRemoteSysCfgEntry,_O:raisecomRemoteSysCfgIndex,'raisecomRemoteSysOperation':raisecomRemoteSysOperation,'raisecomRemoteSysOperationState':raisecomRemoteSysOperationState,'raisecomRemoteHostName':raisecomRemoteHostName,'raisecomRemoteOamNotificationEnable':raisecomRemoteOamNotificationEnable,'raisecomRemoteMaxAllowedFrameLength':raisecomRemoteMaxAllowedFrameLength,'raisecomRemoteCommunityTable':raisecomRemoteCommunityTable,'raisecomRemoteCommunityEntry':raisecomRemoteCommunityEntry,'raisecomRemoteCommunityIndex':raisecomRemoteCommunityIndex,'raisecomRemoteCommunityName':raisecomRemoteCommunityName,'raisecomRemoteCommunityPermission':raisecomRemoteCommunityPermission,'raisecomRemoteL3Table':raisecomRemoteL3Table,'raisecomRemoteL3Entry':raisecomRemoteL3Entry,_V:raisecomRemoteL3Index,'raisecomRemoteL3IpAddr':raisecomRemoteL3IpAddr,'raisecomRemoteL3Mask':raisecomRemoteL3Mask,'raisecomRemoteL3VidIface':raisecomRemoteL3VidIface,'raisecomRemoteL3VidMemberPorts':raisecomRemoteL3VidMemberPorts,'raisecomRemoteL3VidUntaggedPorts':raisecomRemoteL3VidUntaggedPorts,'raisecomRemoteL3DefaultGateway':raisecomRemoteL3DefaultGateway,'raisecomRemoteL3ObIpAddr':raisecomRemoteL3ObIpAddr,'raisecomRemoteL3ObMask':raisecomRemoteL3ObMask,'raisecomRemotePortTable':raisecomRemotePortTable,'raisecomRemotePortEntry':raisecomRemotePortEntry,_W:raisecomRemoteIfindex,_L:raisecomRemotePortIfindex,'raisecomRemotePortType':raisecomRemotePortType,'raisecomRemotePortName':raisecomRemotePortName,'raisecomRemotePortAdminStatus':raisecomRemotePortAdminStatus,'raisecomRemotePortOperStatus':raisecomRemotePortOperStatus,'raisecomRemotePortDuplexSpeedSet':raisecomRemotePortDuplexSpeedSet,'raisecomRemotePortDuplexSpeedGet':raisecomRemotePortDuplexSpeedGet,'raisecomRemotePortFlowControlEnable':raisecomRemotePortFlowControlEnable,'raisecomRemotePortFlowControlStatus':raisecomRemotePortFlowControlStatus,'raisecomRemotePortIngressRate':raisecomRemotePortIngressRate,'raisecomRemotePortEgressRate':raisecomRemotePortEgressRate,'raisecomRemotePortFaultPassEnable':raisecomRemotePortFaultPassEnable,'raisecomRemotePortFaultPassPorts':raisecomRemotePortFaultPassPorts,'raisecomRemotePortFaultPassStatus':raisecomRemotePortFaultPassStatus,'raisecomRemotePortFaultReturnEnable':raisecomRemotePortFaultReturnEnable,'raisecomRemotePortFaultReturnStatus':raisecomRemotePortFaultReturnStatus,'raisecomRemotePortSD':raisecomRemotePortSD,'raisecomRemoteOptModuleType':raisecomRemoteOptModuleType,'raisecomRemotePortDescr':raisecomRemotePortDescr,'raisecomRemotePortStatsTable':raisecomRemotePortStatsTable,'raisecomRemotePortStatsEntry':raisecomRemotePortStatsEntry,_f:raisecomRemoteStatsIfindex,_g:raisecomRemoteStatsPortIfindex,'raisecomRemotePortInOctets':raisecomRemotePortInOctets,'raisecomRemotePortInPkts':raisecomRemotePortInPkts,'raisecomRemotePortInUcastPkts':raisecomRemotePortInUcastPkts,'raisecomRemotePortInMulticastPkts':raisecomRemotePortInMulticastPkts,'raisecomRemotePortInBroadcastPkts':raisecomRemotePortInBroadcastPkts,'raisecomRemotePortOutOctets':raisecomRemotePortOutOctets,'raisecomRemotePortOutPkts':raisecomRemotePortOutPkts,'raisecomRemotePortOutUcastPkts':raisecomRemotePortOutUcastPkts,'raisecomRemotePortOutMulticastPkts':raisecomRemotePortOutMulticastPkts,'raisecomRemotePortOutBroadcastPkts':raisecomRemotePortOutBroadcastPkts,'raisecomRemotePortErrorPkts':raisecomRemotePortErrorPkts,'raisecomRemotePortDropEvents':raisecomRemotePortDropEvents,'raisecomRemotePortCRCAlignErrors':raisecomRemotePortCRCAlignErrors,'raisecomRemotePortUndersizePkts':raisecomRemotePortUndersizePkts,'raisecomRemotePortOversizePkts':raisecomRemotePortOversizePkts,'raisecomRemotePortFragments':raisecomRemotePortFragments,'raisecomRemotePortJabbers':raisecomRemotePortJabbers,'raisecomRemotePortCollisions':raisecomRemotePortCollisions,'raisecomRemoteSfpTable':raisecomRemoteSfpTable,'raisecomRemoteSfpEntry':raisecomRemoteSfpEntry,'raisecomRemoteSfpInterfaceId':raisecomRemoteSfpInterfaceId,'raisecomRemoteSfpExist':raisecomRemoteSfpExist,'raisecomRemoteSfpMediaType':raisecomRemoteSfpMediaType,'raisecomRemoteSfpRXLOS':raisecomRemoteSfpRXLOS,'raisecomRemoteSfpTXFault':raisecomRemoteSfpTXFault,'raisecomRemoteSfpTXDisable':raisecomRemoteSfpTXDisable,'raisecomRemoteSfpModuleType':raisecomRemoteSfpModuleType,'raisecomRemoteSfpOpticalInterface':raisecomRemoteSfpOpticalInterface,'raisecomRemoteSfpSpeedStatus':raisecomRemoteSfpSpeedStatus,'raisecomRemoteSfpTransportDistance':raisecomRemoteSfpTransportDistance,'raisecomRemoteSfpWaveLength':raisecomRemoteSfpWaveLength,'raisecomRemoteSfpVendor':raisecomRemoteSfpVendor,'raisecomRemoteSfpProductType':raisecomRemoteSfpProductType,'raisecomRemoteSfpVersion':raisecomRemoteSfpVersion,'raisecomRemoteSfpSerialNumber':raisecomRemoteSfpSerialNumber,'raisecomRemoteDtTable':raisecomRemoteDtTable,'raisecomRemoteDtEntry':raisecomRemoteDtEntry,'raisecomRemoteDtSwitchMode':raisecomRemoteDtSwitchMode,'raisecomRemoteDtOuterTpid':raisecomRemoteDtOuterTpid,'raisecomRemoteDtNativeVlan':raisecomRemoteDtNativeVlan,'raisecomRemoteDtAccessPort':raisecomRemoteDtAccessPort,'raisecomRemoteSendConfTable':raisecomRemoteSendConfTable,'raisecomRemoteSendConfEntry':raisecomRemoteSendConfEntry,'raisecomRemoteSendConf':raisecomRemoteSendConf,'raisecomRemoteInLoopbackTable':raisecomRemoteInLoopbackTable,'raisecomRemoteInLoopbackEntry':raisecomRemoteInLoopbackEntry,'raisecomRemoteInLoopbackMacExchange':raisecomRemoteInLoopbackMacExchange,'raisecomRemoteInLoopbackCrcRecalSet':raisecomRemoteInLoopbackCrcRecalSet,'raisecomRemoteInLoopbackCrcRecal':raisecomRemoteInLoopbackCrcRecal,'raisecomRemoteInLoopbackStatus':raisecomRemoteInLoopbackStatus,'raisecomRemoteVctTable':raisecomRemoteVctTable,'raisecomRemoteVctEntry':raisecomRemoteVctEntry,'raisecomRemoteVctAttribute':raisecomRemoteVctAttribute,'raisecomRemoteVctStatus':raisecomRemoteVctStatus,'raisecomRemoteVctLength':raisecomRemoteVctLength,'raisecomRemoteVlanConfigTable':raisecomRemoteVlanConfigTable,'raisecomRemoteVlanConfigEntry':raisecomRemoteVlanConfigEntry,'raisecomRemoteVlanStatus':raisecomRemoteVlanStatus,'raisecomRemoteCosStatus':raisecomRemoteCosStatus,'raisecomRemoteFiberPortTagType':raisecomRemoteFiberPortTagType,'raisecomRemoteFiberPortPriority':raisecomRemoteFiberPortPriority,'raisecomRemoteFiberPortPvid':raisecomRemoteFiberPortPvid,'raisecomRemoteCablePortTagType':raisecomRemoteCablePortTagType,'raisecomRemoteCablePortPriority':raisecomRemoteCablePortPriority,'raisecomRemoteCablePortPvid':raisecomRemoteCablePortPvid,'raisecomRemoteCpuPortTagType':raisecomRemoteCpuPortTagType,'raisecomRemoteCpuPortPriority':raisecomRemoteCpuPortPriority,'raisecomRemoteCpuPortPvid':raisecomRemoteCpuPortPvid,'raisecomRemoteSendVlanConf':raisecomRemoteSendVlanConf,'raisecomRemoteVlanGroupTable':raisecomRemoteVlanGroupTable,'raisecomRemoteVlanGroupEntry':raisecomRemoteVlanGroupEntry,_j:raisecomRemoteVlanGroupIndex,'raisecomRemoteVlanId':raisecomRemoteVlanId,'raisecomRemoteVlanMember':raisecomRemoteVlanMember,'raisecomRemoteSfpDdmTable':raisecomRemoteSfpDdmTable,'raisecomRemoteSfpDdmEntry':raisecomRemoteSfpDdmEntry,'raisecomRemoteSfpDdmValid':raisecomRemoteSfpDdmValid,'raisecomRemoteSfpDdmMode':raisecomRemoteSfpDdmMode,'raisecomRemoteSfpDdmTemperature':raisecomRemoteSfpDdmTemperature,'raisecomRemoteSfpDdmSupplyVolt':raisecomRemoteSfpDdmSupplyVolt,'raisecomRemoteSfpDdmBiasCurrent':raisecomRemoteSfpDdmBiasCurrent,'raisecomRemoteSfpDdmOpticalTxPower':raisecomRemoteSfpDdmOpticalTxPower,'raisecomRemoteSfpDdmOpticalRxPower':raisecomRemoteSfpDdmOpticalRxPower,'raisecomRemoteSfpDdmAlarm':raisecomRemoteSfpDdmAlarm,'raisecomRemoteSfpDdmAlarmTemStatus':raisecomRemoteSfpDdmAlarmTemStatus,'raisecomRemoteSfpDdmAlarmVoltStatus':raisecomRemoteSfpDdmAlarmVoltStatus,'raisecomRemoteSfpDdmAlarmCurrentStatus':raisecomRemoteSfpDdmAlarmCurrentStatus,'raisecomRemoteSfpDdmAlarmTxPowerStatus':raisecomRemoteSfpDdmAlarmTxPowerStatus,'raisecomRemoteSfpDdmAlarmRxPowerStatus':raisecomRemoteSfpDdmAlarmRxPowerStatus,'raisecomRemoteManagementLocalMibTraps':raisecomRemoteManagementLocalMibTraps,'raisecomRemotePortLinkUp':raisecomRemotePortLinkUp,'raisecomRemotePortLinkDown':raisecomRemotePortLinkDown,'raisecomRemoteSfpDdmTemNormal':raisecomRemoteSfpDdmTemNormal,'raisecomRemoteSfpDdmTemAbnormal':raisecomRemoteSfpDdmTemAbnormal,'raisecomRemoteSfpDdmVoltNormal':raisecomRemoteSfpDdmVoltNormal,'raisecomRemoteSfpDdmVoltAbnormal':raisecomRemoteSfpDdmVoltAbnormal,'raisecomRemoteSfpDdmCurrentNormal':raisecomRemoteSfpDdmCurrentNormal,'raisecomRemoteSfpDdmCurrentAbnormal':raisecomRemoteSfpDdmCurrentAbnormal,'raisecomRemoteSfpDdmTxPowerNomal':raisecomRemoteSfpDdmTxPowerNomal,'raisecomRemoteSfpDdmTxPowerAbnormal':raisecomRemoteSfpDdmTxPowerAbnormal,'raisecomRemoteSfpDdmRxPowerNormal':raisecomRemoteSfpDdmRxPowerNormal,'raisecomRemoteSfpDdmRxPowerAbnormal':raisecomRemoteSfpDdmRxPowerAbnormal})