_A2='fsTemperatureWarningGroup'
_A1='fsTemperatureWarningDescGroup'
_A0='fsFanStateGroup'
_z='fsPowerStateGroup'
_y='fsModuleTempStateGroup'
_x='fsDeviceMIBNotificationGroup'
_w='fsEntityChgDescGroup'
_v='fsOptionalDevInfoMIBGroup'
_u='fsModuleInfoMIBGroup'
_t='fsDeviceInfoMIBGroup'
_s='fsTemperatureWarning'
_r='fsEntityStatusChange'
_q='fsFanStateFanDescr'
_p='fsFanState'
_o='fsPowerStatePowerDescr'
_n='fsPowerState'
_m='fsModuleTempState'
_l='fsSlotHWVersion'
_k='fsSlotSerialNumber'
_j='fsSlotSoftwareStatus'
_i='fsSlotUserStatus'
_h='fsSlotConfigModuleInfoDescr'
_g='fsSlotInfoDesc'
_f='fsSlotInfoPortMaxNumber'
_e='fsSlotInfoPortNumber'
_d='fsSlotModuleInfoDescr'
_c='fsDeviceOid'
_b='fsDeviceSerialNumber'
_a='fsDeviceHWVersion'
_Z='fsDeviceSWVersion'
_Y='fsDeviceAlias'
_X='fsDevicePriority'
_W='fsDeviceMacAddress'
_V='fsDevicePowerStatus'
_U='fsDeviceInfoSlotNumber'
_T='fsDeviceInfoDescr'
_S='fsDeviceMaxNumber'
_R='accessible-for-notify'
_Q='read-write'
_P='fsTemperatureWarningDesc'
_O='fsEntityStateChgDesc'
_N='fsFanStateIndex'
_M='fsFanStateDeviceIndex'
_L='fsPowerStateIndex'
_K='fsPowerStateDeviceIndex'
_J='fsModuleTempStateIndex'
_I='fsModuleTempStateDeviceIndex'
_H='fsSlotInfoIndex'
_G='fsSlotInfoDeviceIndex'
_F='fsDeviceInfoIndex'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='FS-ENTITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
fsEntityMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,21))
if mibBuilder.loadTexts:fsEntityMIB.setRevisions(('2002-03-20 00:00',))
_FsDeviceMIBObjects_ObjectIdentity=ObjectIdentity
fsDeviceMIBObjects=_FsDeviceMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,21,1))
_FsDeviceMaxNumber_Type=Integer32
_FsDeviceMaxNumber_Object=MibScalar
fsDeviceMaxNumber=_FsDeviceMaxNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,1),_FsDeviceMaxNumber_Type())
fsDeviceMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceMaxNumber.setStatus(_A)
_FsDeviceInfoTable_Object=MibTable
fsDeviceInfoTable=_FsDeviceInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2))
if mibBuilder.loadTexts:fsDeviceInfoTable.setStatus(_A)
_FsDeviceInfoEntry_Object=MibTableRow
fsDeviceInfoEntry=_FsDeviceInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1))
fsDeviceInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsDeviceInfoEntry.setStatus(_A)
_FsDeviceInfoIndex_Type=Integer32
_FsDeviceInfoIndex_Object=MibTableColumn
fsDeviceInfoIndex=_FsDeviceInfoIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,1),_FsDeviceInfoIndex_Type())
fsDeviceInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceInfoIndex.setStatus(_A)
class _FsDeviceInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDeviceInfoDescr_Type.__name__=_D
_FsDeviceInfoDescr_Object=MibTableColumn
fsDeviceInfoDescr=_FsDeviceInfoDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,2),_FsDeviceInfoDescr_Type())
fsDeviceInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceInfoDescr.setStatus(_A)
_FsDeviceInfoSlotNumber_Type=Integer32
_FsDeviceInfoSlotNumber_Object=MibTableColumn
fsDeviceInfoSlotNumber=_FsDeviceInfoSlotNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,3),_FsDeviceInfoSlotNumber_Type())
fsDeviceInfoSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceInfoSlotNumber.setStatus(_A)
class _FsDevicePowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rpsNoLink',1),('rpsLinkAndNoPower',2),('rpsLinkAndReadyForPower',3),('rpsLinkAndPower',4)))
_FsDevicePowerStatus_Type.__name__=_E
_FsDevicePowerStatus_Object=MibTableColumn
fsDevicePowerStatus=_FsDevicePowerStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,4),_FsDevicePowerStatus_Type())
fsDevicePowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDevicePowerStatus.setStatus(_A)
_FsDeviceMacAddress_Type=MacAddress
_FsDeviceMacAddress_Object=MibTableColumn
fsDeviceMacAddress=_FsDeviceMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,5),_FsDeviceMacAddress_Type())
fsDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceMacAddress.setStatus(_A)
class _FsDevicePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsDevicePriority_Type.__name__=_E
_FsDevicePriority_Object=MibTableColumn
fsDevicePriority=_FsDevicePriority_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,6),_FsDevicePriority_Type())
fsDevicePriority.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsDevicePriority.setStatus(_A)
class _FsDeviceAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsDeviceAlias_Type.__name__=_D
_FsDeviceAlias_Object=MibTableColumn
fsDeviceAlias=_FsDeviceAlias_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,7),_FsDeviceAlias_Type())
fsDeviceAlias.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsDeviceAlias.setStatus(_A)
class _FsDeviceSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsDeviceSWVersion_Type.__name__=_D
_FsDeviceSWVersion_Object=MibTableColumn
fsDeviceSWVersion=_FsDeviceSWVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,8),_FsDeviceSWVersion_Type())
fsDeviceSWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceSWVersion.setStatus(_A)
class _FsDeviceHWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsDeviceHWVersion_Type.__name__=_D
_FsDeviceHWVersion_Object=MibTableColumn
fsDeviceHWVersion=_FsDeviceHWVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,9),_FsDeviceHWVersion_Type())
fsDeviceHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceHWVersion.setStatus(_A)
class _FsDeviceSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsDeviceSerialNumber_Type.__name__=_D
_FsDeviceSerialNumber_Object=MibTableColumn
fsDeviceSerialNumber=_FsDeviceSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,10),_FsDeviceSerialNumber_Type())
fsDeviceSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceSerialNumber.setStatus(_A)
_FsDeviceOid_Type=ObjectIdentifier
_FsDeviceOid_Object=MibTableColumn
fsDeviceOid=_FsDeviceOid_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,2,1,11),_FsDeviceOid_Type())
fsDeviceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDeviceOid.setStatus(_A)
_FsSlotInfoTable_Object=MibTable
fsSlotInfoTable=_FsSlotInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3))
if mibBuilder.loadTexts:fsSlotInfoTable.setStatus(_A)
_FsSlotInfoEntry_Object=MibTableRow
fsSlotInfoEntry=_FsSlotInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1))
fsSlotInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:fsSlotInfoEntry.setStatus(_A)
_FsSlotInfoDeviceIndex_Type=Integer32
_FsSlotInfoDeviceIndex_Object=MibTableColumn
fsSlotInfoDeviceIndex=_FsSlotInfoDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,1),_FsSlotInfoDeviceIndex_Type())
fsSlotInfoDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotInfoDeviceIndex.setStatus(_A)
_FsSlotInfoIndex_Type=Integer32
_FsSlotInfoIndex_Object=MibTableColumn
fsSlotInfoIndex=_FsSlotInfoIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,2),_FsSlotInfoIndex_Type())
fsSlotInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotInfoIndex.setStatus(_A)
_FsSlotModuleInfoDescr_Type=DisplayString
_FsSlotModuleInfoDescr_Object=MibTableColumn
fsSlotModuleInfoDescr=_FsSlotModuleInfoDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,3),_FsSlotModuleInfoDescr_Type())
fsSlotModuleInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotModuleInfoDescr.setStatus(_A)
_FsSlotInfoPortNumber_Type=Integer32
_FsSlotInfoPortNumber_Object=MibTableColumn
fsSlotInfoPortNumber=_FsSlotInfoPortNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,4),_FsSlotInfoPortNumber_Type())
fsSlotInfoPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotInfoPortNumber.setStatus(_A)
_FsSlotInfoPortMaxNumber_Type=Integer32
_FsSlotInfoPortMaxNumber_Object=MibTableColumn
fsSlotInfoPortMaxNumber=_FsSlotInfoPortMaxNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,5),_FsSlotInfoPortMaxNumber_Type())
fsSlotInfoPortMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotInfoPortMaxNumber.setStatus(_A)
class _FsSlotInfoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsSlotInfoDesc_Type.__name__=_D
_FsSlotInfoDesc_Object=MibTableColumn
fsSlotInfoDesc=_FsSlotInfoDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,6),_FsSlotInfoDesc_Type())
fsSlotInfoDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotInfoDesc.setStatus(_A)
class _FsSlotConfigModuleInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsSlotConfigModuleInfoDescr_Type.__name__=_D
_FsSlotConfigModuleInfoDescr_Object=MibTableColumn
fsSlotConfigModuleInfoDescr=_FsSlotConfigModuleInfoDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,7),_FsSlotConfigModuleInfoDescr_Type())
fsSlotConfigModuleInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotConfigModuleInfoDescr.setStatus(_A)
_FsSlotUserStatus_Type=Integer32
_FsSlotUserStatus_Object=MibTableColumn
fsSlotUserStatus=_FsSlotUserStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,8),_FsSlotUserStatus_Type())
fsSlotUserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotUserStatus.setStatus(_A)
_FsSlotSoftwareStatus_Type=Integer32
_FsSlotSoftwareStatus_Object=MibTableColumn
fsSlotSoftwareStatus=_FsSlotSoftwareStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,9),_FsSlotSoftwareStatus_Type())
fsSlotSoftwareStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotSoftwareStatus.setStatus(_A)
class _FsSlotSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsSlotSerialNumber_Type.__name__=_D
_FsSlotSerialNumber_Object=MibTableColumn
fsSlotSerialNumber=_FsSlotSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,10),_FsSlotSerialNumber_Type())
fsSlotSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotSerialNumber.setStatus(_A)
class _FsSlotHWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsSlotHWVersion_Type.__name__=_D
_FsSlotHWVersion_Object=MibTableColumn
fsSlotHWVersion=_FsSlotHWVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,3,1,11),_FsSlotHWVersion_Type())
fsSlotHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlotHWVersion.setStatus(_A)
_FsModuleTempStateTable_Object=MibTable
fsModuleTempStateTable=_FsModuleTempStateTable_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,4))
if mibBuilder.loadTexts:fsModuleTempStateTable.setStatus(_A)
_FsModuleTempStateEntry_Object=MibTableRow
fsModuleTempStateEntry=_FsModuleTempStateEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,4,1))
fsModuleTempStateEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:fsModuleTempStateEntry.setStatus(_A)
_FsModuleTempStateDeviceIndex_Type=Integer32
_FsModuleTempStateDeviceIndex_Object=MibTableColumn
fsModuleTempStateDeviceIndex=_FsModuleTempStateDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,4,1,1),_FsModuleTempStateDeviceIndex_Type())
fsModuleTempStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsModuleTempStateDeviceIndex.setStatus(_A)
_FsModuleTempStateIndex_Type=Integer32
_FsModuleTempStateIndex_Object=MibTableColumn
fsModuleTempStateIndex=_FsModuleTempStateIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,4,1,2),_FsModuleTempStateIndex_Type())
fsModuleTempStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsModuleTempStateIndex.setStatus(_A)
class _FsModuleTempState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tempNormal',1),('tempWarning',2)))
_FsModuleTempState_Type.__name__=_E
_FsModuleTempState_Object=MibTableColumn
fsModuleTempState=_FsModuleTempState_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,4,1,3),_FsModuleTempState_Type())
fsModuleTempState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsModuleTempState.setStatus(_A)
_FsPowerStateTable_Object=MibTable
fsPowerStateTable=_FsPowerStateTable_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5))
if mibBuilder.loadTexts:fsPowerStateTable.setStatus(_A)
_FsPowerStateEntry_Object=MibTableRow
fsPowerStateEntry=_FsPowerStateEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5,1))
fsPowerStateEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsPowerStateEntry.setStatus(_A)
_FsPowerStateDeviceIndex_Type=Integer32
_FsPowerStateDeviceIndex_Object=MibTableColumn
fsPowerStateDeviceIndex=_FsPowerStateDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5,1,1),_FsPowerStateDeviceIndex_Type())
fsPowerStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPowerStateDeviceIndex.setStatus(_A)
_FsPowerStateIndex_Type=Integer32
_FsPowerStateIndex_Object=MibTableColumn
fsPowerStateIndex=_FsPowerStateIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5,1,2),_FsPowerStateIndex_Type())
fsPowerStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPowerStateIndex.setStatus(_A)
class _FsPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noLink',1),('linkAndNoPower',2),('linkAndReadyForPower',3),('linkAndPower',4),('linkAndPowerAbnormal',5)))
_FsPowerState_Type.__name__=_E
_FsPowerState_Object=MibTableColumn
fsPowerState=_FsPowerState_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5,1,3),_FsPowerState_Type())
fsPowerState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPowerState.setStatus(_A)
class _FsPowerStatePowerDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPowerStatePowerDescr_Type.__name__=_D
_FsPowerStatePowerDescr_Object=MibTableColumn
fsPowerStatePowerDescr=_FsPowerStatePowerDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5,1,4),_FsPowerStatePowerDescr_Type())
fsPowerStatePowerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPowerStatePowerDescr.setStatus(_A)
class _FsPowerStateSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPowerStateSerialNumber_Type.__name__=_D
_FsPowerStateSerialNumber_Object=MibTableColumn
fsPowerStateSerialNumber=_FsPowerStateSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,5,1,5),_FsPowerStateSerialNumber_Type())
fsPowerStateSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPowerStateSerialNumber.setStatus(_A)
_FsFanStateTable_Object=MibTable
fsFanStateTable=_FsFanStateTable_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6))
if mibBuilder.loadTexts:fsFanStateTable.setStatus(_A)
_FsFanStateEntry_Object=MibTableRow
fsFanStateEntry=_FsFanStateEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6,1))
fsFanStateEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:fsFanStateEntry.setStatus(_A)
_FsFanStateDeviceIndex_Type=Integer32
_FsFanStateDeviceIndex_Object=MibTableColumn
fsFanStateDeviceIndex=_FsFanStateDeviceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6,1,1),_FsFanStateDeviceIndex_Type())
fsFanStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFanStateDeviceIndex.setStatus(_A)
_FsFanStateIndex_Type=Integer32
_FsFanStateIndex_Object=MibTableColumn
fsFanStateIndex=_FsFanStateIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6,1,2),_FsFanStateIndex_Type())
fsFanStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFanStateIndex.setStatus(_A)
class _FsFanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('work',1),('stop',2)))
_FsFanState_Type.__name__=_E
_FsFanState_Object=MibTableColumn
fsFanState=_FsFanState_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6,1,3),_FsFanState_Type())
fsFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFanState.setStatus(_A)
class _FsFanStateFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsFanStateFanDescr_Type.__name__=_D
_FsFanStateFanDescr_Object=MibTableColumn
fsFanStateFanDescr=_FsFanStateFanDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6,1,4),_FsFanStateFanDescr_Type())
fsFanStateFanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFanStateFanDescr.setStatus(_A)
class _FsFanStateSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsFanStateSerialNumber_Type.__name__=_D
_FsFanStateSerialNumber_Object=MibTableColumn
fsFanStateSerialNumber=_FsFanStateSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,21,1,6,1,5),_FsFanStateSerialNumber_Type())
fsFanStateSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFanStateSerialNumber.setStatus(_A)
_FsEntityMIBTraps_ObjectIdentity=ObjectIdentity
fsEntityMIBTraps=_FsEntityMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,21,2))
_FsEntityStateChgDesc_Type=DisplayString
_FsEntityStateChgDesc_Object=MibScalar
fsEntityStateChgDesc=_FsEntityStateChgDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,21,2,1),_FsEntityStateChgDesc_Type())
fsEntityStateChgDesc.setMaxAccess(_R)
if mibBuilder.loadTexts:fsEntityStateChgDesc.setStatus(_A)
class _FsTemperatureWarningDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsTemperatureWarningDesc_Type.__name__=_D
_FsTemperatureWarningDesc_Object=MibScalar
fsTemperatureWarningDesc=_FsTemperatureWarningDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,21,2,3),_FsTemperatureWarningDesc_Type())
fsTemperatureWarningDesc.setMaxAccess(_R)
if mibBuilder.loadTexts:fsTemperatureWarningDesc.setStatus(_A)
_FsDeviceMIBConformance_ObjectIdentity=ObjectIdentity
fsDeviceMIBConformance=_FsDeviceMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,21,3))
_FsDeviceMIBCompliances_ObjectIdentity=ObjectIdentity
fsDeviceMIBCompliances=_FsDeviceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,21,3,1))
_FsDeviceMIBGroups_ObjectIdentity=ObjectIdentity
fsDeviceMIBGroups=_FsDeviceMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,21,3,2))
fsDeviceInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,1))
fsDeviceInfoMIBGroup.setObjects(*((_B,_S),(_B,_F),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsDeviceInfoMIBGroup.setStatus(_A)
fsOptionalDevInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,2))
fsOptionalDevInfoMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:fsOptionalDevInfoMIBGroup.setStatus(_A)
fsModuleInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,3))
fsModuleInfoMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:fsModuleInfoMIBGroup.setStatus(_A)
fsEntityChgDescGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,4))
fsEntityChgDescGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:fsEntityChgDescGroup.setStatus(_A)
fsModuleTempStateGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,6))
fsModuleTempStateGroup.setObjects(*((_B,_I),(_B,_J),(_B,_m)))
if mibBuilder.loadTexts:fsModuleTempStateGroup.setStatus(_A)
fsPowerStateGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,7))
fsPowerStateGroup.setObjects(*((_B,_K),(_B,_L),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:fsPowerStateGroup.setStatus(_A)
fsFanStateGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,8))
fsFanStateGroup.setObjects(*((_B,_M),(_B,_N),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:fsFanStateGroup.setStatus(_A)
fsTemperatureWarningDescGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,9))
fsTemperatureWarningDescGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:fsTemperatureWarningDescGroup.setStatus(_A)
fsEntityStatusChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,21,2,2))
fsEntityStatusChange.setObjects((_B,_O))
if mibBuilder.loadTexts:fsEntityStatusChange.setStatus(_A)
fsTemperatureWarning=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,21,2,4))
fsTemperatureWarning.setObjects((_B,_P))
if mibBuilder.loadTexts:fsTemperatureWarning.setStatus(_A)
fsDeviceMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,5))
fsDeviceMIBNotificationGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:fsDeviceMIBNotificationGroup.setStatus(_A)
fsTemperatureWarningGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,21,3,2,10))
fsTemperatureWarningGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:fsTemperatureWarningGroup.setStatus(_A)
fsDeviceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,21,3,1,1))
fsDeviceMIBCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:fsDeviceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsEntityMIB':fsEntityMIB,'fsDeviceMIBObjects':fsDeviceMIBObjects,_S:fsDeviceMaxNumber,'fsDeviceInfoTable':fsDeviceInfoTable,'fsDeviceInfoEntry':fsDeviceInfoEntry,_F:fsDeviceInfoIndex,_T:fsDeviceInfoDescr,_U:fsDeviceInfoSlotNumber,_V:fsDevicePowerStatus,_W:fsDeviceMacAddress,_X:fsDevicePriority,_Y:fsDeviceAlias,_Z:fsDeviceSWVersion,_a:fsDeviceHWVersion,_b:fsDeviceSerialNumber,_c:fsDeviceOid,'fsSlotInfoTable':fsSlotInfoTable,'fsSlotInfoEntry':fsSlotInfoEntry,_G:fsSlotInfoDeviceIndex,_H:fsSlotInfoIndex,_d:fsSlotModuleInfoDescr,_e:fsSlotInfoPortNumber,_f:fsSlotInfoPortMaxNumber,_g:fsSlotInfoDesc,_h:fsSlotConfigModuleInfoDescr,_i:fsSlotUserStatus,_j:fsSlotSoftwareStatus,_k:fsSlotSerialNumber,_l:fsSlotHWVersion,'fsModuleTempStateTable':fsModuleTempStateTable,'fsModuleTempStateEntry':fsModuleTempStateEntry,_I:fsModuleTempStateDeviceIndex,_J:fsModuleTempStateIndex,_m:fsModuleTempState,'fsPowerStateTable':fsPowerStateTable,'fsPowerStateEntry':fsPowerStateEntry,_K:fsPowerStateDeviceIndex,_L:fsPowerStateIndex,_n:fsPowerState,_o:fsPowerStatePowerDescr,'fsPowerStateSerialNumber':fsPowerStateSerialNumber,'fsFanStateTable':fsFanStateTable,'fsFanStateEntry':fsFanStateEntry,_M:fsFanStateDeviceIndex,_N:fsFanStateIndex,_p:fsFanState,_q:fsFanStateFanDescr,'fsFanStateSerialNumber':fsFanStateSerialNumber,'fsEntityMIBTraps':fsEntityMIBTraps,_O:fsEntityStateChgDesc,_r:fsEntityStatusChange,_P:fsTemperatureWarningDesc,_s:fsTemperatureWarning,'fsDeviceMIBConformance':fsDeviceMIBConformance,'fsDeviceMIBCompliances':fsDeviceMIBCompliances,'fsDeviceMIBCompliance':fsDeviceMIBCompliance,'fsDeviceMIBGroups':fsDeviceMIBGroups,_t:fsDeviceInfoMIBGroup,_v:fsOptionalDevInfoMIBGroup,_u:fsModuleInfoMIBGroup,_w:fsEntityChgDescGroup,_x:fsDeviceMIBNotificationGroup,_y:fsModuleTempStateGroup,_z:fsPowerStateGroup,_A0:fsFanStateGroup,_A1:fsTemperatureWarningDescGroup,_A2:fsTemperatureWarningGroup})