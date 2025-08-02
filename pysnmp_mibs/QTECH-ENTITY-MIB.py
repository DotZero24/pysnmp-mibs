_A2='qtechTemperatureWarningGroup'
_A1='qtechTemperatureWarningDescGroup'
_A0='qtechFanStateGroup'
_z='qtechPowerStateGroup'
_y='qtechModuleTempStateGroup'
_x='qtechDeviceMIBNotificationGroup'
_w='qtechEntityChgDescGroup'
_v='qtechOptionalDevInfoMIBGroup'
_u='qtechModuleInfoMIBGroup'
_t='qtechDeviceInfoMIBGroup'
_s='qtechTemperatureWarning'
_r='qtechEntityStatusChange'
_q='qtechFanStateFanDescr'
_p='qtechFanState'
_o='qtechPowerStatePowerDescr'
_n='qtechPowerState'
_m='qtechModuleTempState'
_l='qtechSlotHWVersion'
_k='qtechSlotSerialNumber'
_j='qtechSlotSoftwareStatus'
_i='qtechSlotUserStatus'
_h='qtechSlotConfigModuleInfoDescr'
_g='qtechSlotInfoDesc'
_f='qtechSlotInfoPortMaxNumber'
_e='qtechSlotInfoPortNumber'
_d='qtechSlotModuleInfoDescr'
_c='qtechDeviceOid'
_b='qtechDeviceSerialNumber'
_a='qtechDeviceHWVersion'
_Z='qtechDeviceSWVersion'
_Y='qtechDeviceAlias'
_X='qtechDevicePriority'
_W='qtechDeviceMacAddress'
_V='qtechDevicePowerStatus'
_U='qtechDeviceInfoSlotNumber'
_T='qtechDeviceInfoDescr'
_S='qtechDeviceMaxNumber'
_R='accessible-for-notify'
_Q='read-write'
_P='qtechTemperatureWarningDesc'
_O='qtechEntityStateChgDesc'
_N='qtechFanStateIndex'
_M='qtechFanStateDeviceIndex'
_L='qtechPowerStateIndex'
_K='qtechPowerStateDeviceIndex'
_J='qtechModuleTempStateIndex'
_I='qtechModuleTempStateDeviceIndex'
_H='qtechSlotInfoIndex'
_G='qtechSlotInfoDeviceIndex'
_F='qtechDeviceInfoIndex'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='current'
_A='QTECH-ENTITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
qtechEntityMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,21))
if mibBuilder.loadTexts:qtechEntityMIB.setRevisions(('2002-03-20 00:00',))
_QtechDeviceMIBObjects_ObjectIdentity=ObjectIdentity
qtechDeviceMIBObjects=_QtechDeviceMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,21,1))
_QtechDeviceMaxNumber_Type=Integer32
_QtechDeviceMaxNumber_Object=MibScalar
qtechDeviceMaxNumber=_QtechDeviceMaxNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,1),_QtechDeviceMaxNumber_Type())
qtechDeviceMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceMaxNumber.setStatus(_B)
_QtechDeviceInfoTable_Object=MibTable
qtechDeviceInfoTable=_QtechDeviceInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2))
if mibBuilder.loadTexts:qtechDeviceInfoTable.setStatus(_B)
_QtechDeviceInfoEntry_Object=MibTableRow
qtechDeviceInfoEntry=_QtechDeviceInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1))
qtechDeviceInfoEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:qtechDeviceInfoEntry.setStatus(_B)
_QtechDeviceInfoIndex_Type=Integer32
_QtechDeviceInfoIndex_Object=MibTableColumn
qtechDeviceInfoIndex=_QtechDeviceInfoIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,1),_QtechDeviceInfoIndex_Type())
qtechDeviceInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceInfoIndex.setStatus(_B)
class _QtechDeviceInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechDeviceInfoDescr_Type.__name__=_D
_QtechDeviceInfoDescr_Object=MibTableColumn
qtechDeviceInfoDescr=_QtechDeviceInfoDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,2),_QtechDeviceInfoDescr_Type())
qtechDeviceInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceInfoDescr.setStatus(_B)
_QtechDeviceInfoSlotNumber_Type=Integer32
_QtechDeviceInfoSlotNumber_Object=MibTableColumn
qtechDeviceInfoSlotNumber=_QtechDeviceInfoSlotNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,3),_QtechDeviceInfoSlotNumber_Type())
qtechDeviceInfoSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceInfoSlotNumber.setStatus(_B)
class _QtechDevicePowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rpsNoLink',1),('rpsLinkAndNoPower',2),('rpsLinkAndReadyForPower',3),('rpsLinkAndPower',4)))
_QtechDevicePowerStatus_Type.__name__=_E
_QtechDevicePowerStatus_Object=MibTableColumn
qtechDevicePowerStatus=_QtechDevicePowerStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,4),_QtechDevicePowerStatus_Type())
qtechDevicePowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDevicePowerStatus.setStatus(_B)
_QtechDeviceMacAddress_Type=MacAddress
_QtechDeviceMacAddress_Object=MibTableColumn
qtechDeviceMacAddress=_QtechDeviceMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,5),_QtechDeviceMacAddress_Type())
qtechDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceMacAddress.setStatus(_B)
class _QtechDevicePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_QtechDevicePriority_Type.__name__=_E
_QtechDevicePriority_Object=MibTableColumn
qtechDevicePriority=_QtechDevicePriority_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,6),_QtechDevicePriority_Type())
qtechDevicePriority.setMaxAccess(_Q)
if mibBuilder.loadTexts:qtechDevicePriority.setStatus(_B)
class _QtechDeviceAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechDeviceAlias_Type.__name__=_D
_QtechDeviceAlias_Object=MibTableColumn
qtechDeviceAlias=_QtechDeviceAlias_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,7),_QtechDeviceAlias_Type())
qtechDeviceAlias.setMaxAccess(_Q)
if mibBuilder.loadTexts:qtechDeviceAlias.setStatus(_B)
class _QtechDeviceSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechDeviceSWVersion_Type.__name__=_D
_QtechDeviceSWVersion_Object=MibTableColumn
qtechDeviceSWVersion=_QtechDeviceSWVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,8),_QtechDeviceSWVersion_Type())
qtechDeviceSWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceSWVersion.setStatus(_B)
class _QtechDeviceHWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechDeviceHWVersion_Type.__name__=_D
_QtechDeviceHWVersion_Object=MibTableColumn
qtechDeviceHWVersion=_QtechDeviceHWVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,9),_QtechDeviceHWVersion_Type())
qtechDeviceHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceHWVersion.setStatus(_B)
class _QtechDeviceSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechDeviceSerialNumber_Type.__name__=_D
_QtechDeviceSerialNumber_Object=MibTableColumn
qtechDeviceSerialNumber=_QtechDeviceSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,10),_QtechDeviceSerialNumber_Type())
qtechDeviceSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceSerialNumber.setStatus(_B)
_QtechDeviceOid_Type=ObjectIdentifier
_QtechDeviceOid_Object=MibTableColumn
qtechDeviceOid=_QtechDeviceOid_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,2,1,11),_QtechDeviceOid_Type())
qtechDeviceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDeviceOid.setStatus(_B)
_QtechSlotInfoTable_Object=MibTable
qtechSlotInfoTable=_QtechSlotInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3))
if mibBuilder.loadTexts:qtechSlotInfoTable.setStatus(_B)
_QtechSlotInfoEntry_Object=MibTableRow
qtechSlotInfoEntry=_QtechSlotInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1))
qtechSlotInfoEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:qtechSlotInfoEntry.setStatus(_B)
_QtechSlotInfoDeviceIndex_Type=Integer32
_QtechSlotInfoDeviceIndex_Object=MibTableColumn
qtechSlotInfoDeviceIndex=_QtechSlotInfoDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,1),_QtechSlotInfoDeviceIndex_Type())
qtechSlotInfoDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotInfoDeviceIndex.setStatus(_B)
_QtechSlotInfoIndex_Type=Integer32
_QtechSlotInfoIndex_Object=MibTableColumn
qtechSlotInfoIndex=_QtechSlotInfoIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,2),_QtechSlotInfoIndex_Type())
qtechSlotInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotInfoIndex.setStatus(_B)
_QtechSlotModuleInfoDescr_Type=DisplayString
_QtechSlotModuleInfoDescr_Object=MibTableColumn
qtechSlotModuleInfoDescr=_QtechSlotModuleInfoDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,3),_QtechSlotModuleInfoDescr_Type())
qtechSlotModuleInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotModuleInfoDescr.setStatus(_B)
_QtechSlotInfoPortNumber_Type=Integer32
_QtechSlotInfoPortNumber_Object=MibTableColumn
qtechSlotInfoPortNumber=_QtechSlotInfoPortNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,4),_QtechSlotInfoPortNumber_Type())
qtechSlotInfoPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotInfoPortNumber.setStatus(_B)
_QtechSlotInfoPortMaxNumber_Type=Integer32
_QtechSlotInfoPortMaxNumber_Object=MibTableColumn
qtechSlotInfoPortMaxNumber=_QtechSlotInfoPortMaxNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,5),_QtechSlotInfoPortMaxNumber_Type())
qtechSlotInfoPortMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotInfoPortMaxNumber.setStatus(_B)
class _QtechSlotInfoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechSlotInfoDesc_Type.__name__=_D
_QtechSlotInfoDesc_Object=MibTableColumn
qtechSlotInfoDesc=_QtechSlotInfoDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,6),_QtechSlotInfoDesc_Type())
qtechSlotInfoDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotInfoDesc.setStatus(_B)
class _QtechSlotConfigModuleInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechSlotConfigModuleInfoDescr_Type.__name__=_D
_QtechSlotConfigModuleInfoDescr_Object=MibTableColumn
qtechSlotConfigModuleInfoDescr=_QtechSlotConfigModuleInfoDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,7),_QtechSlotConfigModuleInfoDescr_Type())
qtechSlotConfigModuleInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotConfigModuleInfoDescr.setStatus(_B)
_QtechSlotUserStatus_Type=Integer32
_QtechSlotUserStatus_Object=MibTableColumn
qtechSlotUserStatus=_QtechSlotUserStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,8),_QtechSlotUserStatus_Type())
qtechSlotUserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotUserStatus.setStatus(_B)
_QtechSlotSoftwareStatus_Type=Integer32
_QtechSlotSoftwareStatus_Object=MibTableColumn
qtechSlotSoftwareStatus=_QtechSlotSoftwareStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,9),_QtechSlotSoftwareStatus_Type())
qtechSlotSoftwareStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotSoftwareStatus.setStatus(_B)
class _QtechSlotSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechSlotSerialNumber_Type.__name__=_D
_QtechSlotSerialNumber_Object=MibTableColumn
qtechSlotSerialNumber=_QtechSlotSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,10),_QtechSlotSerialNumber_Type())
qtechSlotSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotSerialNumber.setStatus(_B)
class _QtechSlotHWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechSlotHWVersion_Type.__name__=_D
_QtechSlotHWVersion_Object=MibTableColumn
qtechSlotHWVersion=_QtechSlotHWVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,3,1,11),_QtechSlotHWVersion_Type())
qtechSlotHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlotHWVersion.setStatus(_B)
_QtechModuleTempStateTable_Object=MibTable
qtechModuleTempStateTable=_QtechModuleTempStateTable_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,4))
if mibBuilder.loadTexts:qtechModuleTempStateTable.setStatus(_B)
_QtechModuleTempStateEntry_Object=MibTableRow
qtechModuleTempStateEntry=_QtechModuleTempStateEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,4,1))
qtechModuleTempStateEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:qtechModuleTempStateEntry.setStatus(_B)
_QtechModuleTempStateDeviceIndex_Type=Integer32
_QtechModuleTempStateDeviceIndex_Object=MibTableColumn
qtechModuleTempStateDeviceIndex=_QtechModuleTempStateDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,4,1,1),_QtechModuleTempStateDeviceIndex_Type())
qtechModuleTempStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechModuleTempStateDeviceIndex.setStatus(_B)
_QtechModuleTempStateIndex_Type=Integer32
_QtechModuleTempStateIndex_Object=MibTableColumn
qtechModuleTempStateIndex=_QtechModuleTempStateIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,4,1,2),_QtechModuleTempStateIndex_Type())
qtechModuleTempStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechModuleTempStateIndex.setStatus(_B)
class _QtechModuleTempState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tempNormal',1),('tempWarning',2)))
_QtechModuleTempState_Type.__name__=_E
_QtechModuleTempState_Object=MibTableColumn
qtechModuleTempState=_QtechModuleTempState_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,4,1,3),_QtechModuleTempState_Type())
qtechModuleTempState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechModuleTempState.setStatus(_B)
_QtechPowerStateTable_Object=MibTable
qtechPowerStateTable=_QtechPowerStateTable_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,5))
if mibBuilder.loadTexts:qtechPowerStateTable.setStatus(_B)
_QtechPowerStateEntry_Object=MibTableRow
qtechPowerStateEntry=_QtechPowerStateEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,5,1))
qtechPowerStateEntry.setIndexNames((0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:qtechPowerStateEntry.setStatus(_B)
_QtechPowerStateDeviceIndex_Type=Integer32
_QtechPowerStateDeviceIndex_Object=MibTableColumn
qtechPowerStateDeviceIndex=_QtechPowerStateDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,5,1,1),_QtechPowerStateDeviceIndex_Type())
qtechPowerStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPowerStateDeviceIndex.setStatus(_B)
_QtechPowerStateIndex_Type=Integer32
_QtechPowerStateIndex_Object=MibTableColumn
qtechPowerStateIndex=_QtechPowerStateIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,5,1,2),_QtechPowerStateIndex_Type())
qtechPowerStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPowerStateIndex.setStatus(_B)
class _QtechPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noLink',1),('linkAndNoPower',2),('linkAndReadyForPower',3),('linkAndPower',4),('linkAndPowerAbnormal',5)))
_QtechPowerState_Type.__name__=_E
_QtechPowerState_Object=MibTableColumn
qtechPowerState=_QtechPowerState_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,5,1,3),_QtechPowerState_Type())
qtechPowerState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPowerState.setStatus(_B)
class _QtechPowerStatePowerDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechPowerStatePowerDescr_Type.__name__=_D
_QtechPowerStatePowerDescr_Object=MibTableColumn
qtechPowerStatePowerDescr=_QtechPowerStatePowerDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,5,1,4),_QtechPowerStatePowerDescr_Type())
qtechPowerStatePowerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPowerStatePowerDescr.setStatus(_B)
_QtechFanStateTable_Object=MibTable
qtechFanStateTable=_QtechFanStateTable_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,6))
if mibBuilder.loadTexts:qtechFanStateTable.setStatus(_B)
_QtechFanStateEntry_Object=MibTableRow
qtechFanStateEntry=_QtechFanStateEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,6,1))
qtechFanStateEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:qtechFanStateEntry.setStatus(_B)
_QtechFanStateDeviceIndex_Type=Integer32
_QtechFanStateDeviceIndex_Object=MibTableColumn
qtechFanStateDeviceIndex=_QtechFanStateDeviceIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,6,1,1),_QtechFanStateDeviceIndex_Type())
qtechFanStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFanStateDeviceIndex.setStatus(_B)
_QtechFanStateIndex_Type=Integer32
_QtechFanStateIndex_Object=MibTableColumn
qtechFanStateIndex=_QtechFanStateIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,6,1,2),_QtechFanStateIndex_Type())
qtechFanStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFanStateIndex.setStatus(_B)
class _QtechFanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('work',1),('stop',2)))
_QtechFanState_Type.__name__=_E
_QtechFanState_Object=MibTableColumn
qtechFanState=_QtechFanState_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,6,1,3),_QtechFanState_Type())
qtechFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFanState.setStatus(_B)
class _QtechFanStateFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechFanStateFanDescr_Type.__name__=_D
_QtechFanStateFanDescr_Object=MibTableColumn
qtechFanStateFanDescr=_QtechFanStateFanDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,21,1,6,1,4),_QtechFanStateFanDescr_Type())
qtechFanStateFanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFanStateFanDescr.setStatus(_B)
_QtechEntityMIBTraps_ObjectIdentity=ObjectIdentity
qtechEntityMIBTraps=_QtechEntityMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,21,2))
_QtechEntityStateChgDesc_Type=DisplayString
_QtechEntityStateChgDesc_Object=MibScalar
qtechEntityStateChgDesc=_QtechEntityStateChgDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,21,2,1),_QtechEntityStateChgDesc_Type())
qtechEntityStateChgDesc.setMaxAccess(_R)
if mibBuilder.loadTexts:qtechEntityStateChgDesc.setStatus(_B)
class _QtechTemperatureWarningDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechTemperatureWarningDesc_Type.__name__=_D
_QtechTemperatureWarningDesc_Object=MibScalar
qtechTemperatureWarningDesc=_QtechTemperatureWarningDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,21,2,3),_QtechTemperatureWarningDesc_Type())
qtechTemperatureWarningDesc.setMaxAccess(_R)
if mibBuilder.loadTexts:qtechTemperatureWarningDesc.setStatus(_B)
_QtechDeviceMIBConformance_ObjectIdentity=ObjectIdentity
qtechDeviceMIBConformance=_QtechDeviceMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,21,3))
_QtechDeviceMIBCompliances_ObjectIdentity=ObjectIdentity
qtechDeviceMIBCompliances=_QtechDeviceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,21,3,1))
_QtechDeviceMIBGroups_ObjectIdentity=ObjectIdentity
qtechDeviceMIBGroups=_QtechDeviceMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,21,3,2))
qtechDeviceInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,1))
qtechDeviceInfoMIBGroup.setObjects(*((_A,_S),(_A,_F),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:qtechDeviceInfoMIBGroup.setStatus(_B)
qtechOptionalDevInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,2))
qtechOptionalDevInfoMIBGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:qtechOptionalDevInfoMIBGroup.setStatus(_B)
qtechModuleInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,3))
qtechModuleInfoMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:qtechModuleInfoMIBGroup.setStatus(_B)
qtechEntityChgDescGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,4))
qtechEntityChgDescGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:qtechEntityChgDescGroup.setStatus(_B)
qtechModuleTempStateGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,6))
qtechModuleTempStateGroup.setObjects(*((_A,_I),(_A,_J),(_A,_m)))
if mibBuilder.loadTexts:qtechModuleTempStateGroup.setStatus(_B)
qtechPowerStateGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,7))
qtechPowerStateGroup.setObjects(*((_A,_K),(_A,_L),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:qtechPowerStateGroup.setStatus(_B)
qtechFanStateGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,8))
qtechFanStateGroup.setObjects(*((_A,_M),(_A,_N),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:qtechFanStateGroup.setStatus(_B)
qtechTemperatureWarningDescGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,9))
qtechTemperatureWarningDescGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:qtechTemperatureWarningDescGroup.setStatus(_B)
qtechEntityStatusChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,21,2,2))
qtechEntityStatusChange.setObjects((_A,_O))
if mibBuilder.loadTexts:qtechEntityStatusChange.setStatus(_B)
qtechTemperatureWarning=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,21,2,4))
qtechTemperatureWarning.setObjects((_A,_P))
if mibBuilder.loadTexts:qtechTemperatureWarning.setStatus(_B)
qtechDeviceMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,5))
qtechDeviceMIBNotificationGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:qtechDeviceMIBNotificationGroup.setStatus(_B)
qtechTemperatureWarningGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,21,3,2,10))
qtechTemperatureWarningGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:qtechTemperatureWarningGroup.setStatus(_B)
qtechDeviceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,21,3,1,1))
qtechDeviceMIBCompliance.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:qtechDeviceMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechEntityMIB':qtechEntityMIB,'qtechDeviceMIBObjects':qtechDeviceMIBObjects,_S:qtechDeviceMaxNumber,'qtechDeviceInfoTable':qtechDeviceInfoTable,'qtechDeviceInfoEntry':qtechDeviceInfoEntry,_F:qtechDeviceInfoIndex,_T:qtechDeviceInfoDescr,_U:qtechDeviceInfoSlotNumber,_V:qtechDevicePowerStatus,_W:qtechDeviceMacAddress,_X:qtechDevicePriority,_Y:qtechDeviceAlias,_Z:qtechDeviceSWVersion,_a:qtechDeviceHWVersion,_b:qtechDeviceSerialNumber,_c:qtechDeviceOid,'qtechSlotInfoTable':qtechSlotInfoTable,'qtechSlotInfoEntry':qtechSlotInfoEntry,_G:qtechSlotInfoDeviceIndex,_H:qtechSlotInfoIndex,_d:qtechSlotModuleInfoDescr,_e:qtechSlotInfoPortNumber,_f:qtechSlotInfoPortMaxNumber,_g:qtechSlotInfoDesc,_h:qtechSlotConfigModuleInfoDescr,_i:qtechSlotUserStatus,_j:qtechSlotSoftwareStatus,_k:qtechSlotSerialNumber,_l:qtechSlotHWVersion,'qtechModuleTempStateTable':qtechModuleTempStateTable,'qtechModuleTempStateEntry':qtechModuleTempStateEntry,_I:qtechModuleTempStateDeviceIndex,_J:qtechModuleTempStateIndex,_m:qtechModuleTempState,'qtechPowerStateTable':qtechPowerStateTable,'qtechPowerStateEntry':qtechPowerStateEntry,_K:qtechPowerStateDeviceIndex,_L:qtechPowerStateIndex,_n:qtechPowerState,_o:qtechPowerStatePowerDescr,'qtechFanStateTable':qtechFanStateTable,'qtechFanStateEntry':qtechFanStateEntry,_M:qtechFanStateDeviceIndex,_N:qtechFanStateIndex,_p:qtechFanState,_q:qtechFanStateFanDescr,'qtechEntityMIBTraps':qtechEntityMIBTraps,_O:qtechEntityStateChgDesc,_r:qtechEntityStatusChange,_P:qtechTemperatureWarningDesc,_s:qtechTemperatureWarning,'qtechDeviceMIBConformance':qtechDeviceMIBConformance,'qtechDeviceMIBCompliances':qtechDeviceMIBCompliances,'qtechDeviceMIBCompliance':qtechDeviceMIBCompliance,'qtechDeviceMIBGroups':qtechDeviceMIBGroups,_t:qtechDeviceInfoMIBGroup,_v:qtechOptionalDevInfoMIBGroup,_u:qtechModuleInfoMIBGroup,_w:qtechEntityChgDescGroup,_x:qtechDeviceMIBNotificationGroup,_y:qtechModuleTempStateGroup,_z:qtechPowerStateGroup,_A0:qtechFanStateGroup,_A1:qtechTemperatureWarningDescGroup,_A2:qtechTemperatureWarningGroup})