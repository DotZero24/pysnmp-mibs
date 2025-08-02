_t='myTemperatureWarningGroup'
_s='myTemperatureWarningDescGroup'
_r='myFanStateGroup'
_q='myPowerStateGroup'
_p='myModuleTempStateGroup'
_o='myDeviceMIBNotificationGroup'
_n='myEntityChgDescGroup'
_m='myOptionalDevInfoMIBGroup'
_l='myModuleInfoMIBGroup'
_k='myDeviceInfoMIBGroup'
_j='myTemperatureWarning'
_i='myEntityStatusChange'
_h='myFanState'
_g='myPowerState'
_f='myModuleTempState'
_e='mySlotInfoDesc'
_d='mySlotInfoPortMaxNumber'
_c='mySlotInfoPortNumber'
_b='mySlotModuleInfoDescr'
_a='myDeviceHWVersion'
_Z='myDeviceSWVersion'
_Y='myDeviceAlias'
_X='myDevicePriority'
_W='myDeviceMacAddress'
_V='myDevicePowerStatus'
_U='myDeviceInfoSlotNumber'
_T='myDeviceInfoDescr'
_S='myDeviceMaxNumber'
_R='accessible-for-notify'
_Q='read-write'
_P='myTemperatureWarningDesc'
_O='myEntityStateChgDesc'
_N='myFanStateIndex'
_M='myFanStateDeviceIndex'
_L='myPowerStateIndex'
_K='myPowerStateDeviceIndex'
_J='myModuleTempStateIndex'
_I='myModuleTempStateDeviceIndex'
_H='mySlotInfoIndex'
_G='mySlotInfoDeviceIndex'
_F='myDeviceInfoIndex'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='current'
_A='MY-ENTITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myEntityMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,21))
if mibBuilder.loadTexts:myEntityMIB.setRevisions(('2002-03-20 00:00',))
_MyDeviceMIBObjects_ObjectIdentity=ObjectIdentity
myDeviceMIBObjects=_MyDeviceMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,21,1))
_MyDeviceMaxNumber_Type=Integer32
_MyDeviceMaxNumber_Object=MibScalar
myDeviceMaxNumber=_MyDeviceMaxNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,1),_MyDeviceMaxNumber_Type())
myDeviceMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceMaxNumber.setStatus(_B)
_MyDeviceInfoTable_Object=MibTable
myDeviceInfoTable=_MyDeviceInfoTable_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2))
if mibBuilder.loadTexts:myDeviceInfoTable.setStatus(_B)
_MyDeviceInfoEntry_Object=MibTableRow
myDeviceInfoEntry=_MyDeviceInfoEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1))
myDeviceInfoEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:myDeviceInfoEntry.setStatus(_B)
_MyDeviceInfoIndex_Type=Integer32
_MyDeviceInfoIndex_Object=MibTableColumn
myDeviceInfoIndex=_MyDeviceInfoIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,1),_MyDeviceInfoIndex_Type())
myDeviceInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceInfoIndex.setStatus(_B)
class _MyDeviceInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyDeviceInfoDescr_Type.__name__=_D
_MyDeviceInfoDescr_Object=MibTableColumn
myDeviceInfoDescr=_MyDeviceInfoDescr_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,2),_MyDeviceInfoDescr_Type())
myDeviceInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceInfoDescr.setStatus(_B)
_MyDeviceInfoSlotNumber_Type=Integer32
_MyDeviceInfoSlotNumber_Object=MibTableColumn
myDeviceInfoSlotNumber=_MyDeviceInfoSlotNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,3),_MyDeviceInfoSlotNumber_Type())
myDeviceInfoSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceInfoSlotNumber.setStatus(_B)
class _MyDevicePowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rpsNoLink',1),('rpsLinkAndNoPower',2),('rpsLinkAndReadyForPower',3),('rpsLinkAndPower',4)))
_MyDevicePowerStatus_Type.__name__=_E
_MyDevicePowerStatus_Object=MibTableColumn
myDevicePowerStatus=_MyDevicePowerStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,4),_MyDevicePowerStatus_Type())
myDevicePowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myDevicePowerStatus.setStatus(_B)
_MyDeviceMacAddress_Type=MacAddress
_MyDeviceMacAddress_Object=MibTableColumn
myDeviceMacAddress=_MyDeviceMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,5),_MyDeviceMacAddress_Type())
myDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceMacAddress.setStatus(_B)
class _MyDevicePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MyDevicePriority_Type.__name__=_E
_MyDevicePriority_Object=MibTableColumn
myDevicePriority=_MyDevicePriority_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,6),_MyDevicePriority_Type())
myDevicePriority.setMaxAccess(_Q)
if mibBuilder.loadTexts:myDevicePriority.setStatus(_B)
class _MyDeviceAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyDeviceAlias_Type.__name__=_D
_MyDeviceAlias_Object=MibTableColumn
myDeviceAlias=_MyDeviceAlias_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,7),_MyDeviceAlias_Type())
myDeviceAlias.setMaxAccess(_Q)
if mibBuilder.loadTexts:myDeviceAlias.setStatus(_B)
class _MyDeviceSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyDeviceSWVersion_Type.__name__=_D
_MyDeviceSWVersion_Object=MibTableColumn
myDeviceSWVersion=_MyDeviceSWVersion_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,8),_MyDeviceSWVersion_Type())
myDeviceSWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceSWVersion.setStatus(_B)
class _MyDeviceHWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyDeviceHWVersion_Type.__name__=_D
_MyDeviceHWVersion_Object=MibTableColumn
myDeviceHWVersion=_MyDeviceHWVersion_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,2,1,9),_MyDeviceHWVersion_Type())
myDeviceHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:myDeviceHWVersion.setStatus(_B)
_MySlotInfoTable_Object=MibTable
mySlotInfoTable=_MySlotInfoTable_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3))
if mibBuilder.loadTexts:mySlotInfoTable.setStatus(_B)
_MySlotInfoEntry_Object=MibTableRow
mySlotInfoEntry=_MySlotInfoEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1))
mySlotInfoEntry.setIndexNames((0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:mySlotInfoEntry.setStatus(_B)
_MySlotInfoDeviceIndex_Type=Integer32
_MySlotInfoDeviceIndex_Object=MibTableColumn
mySlotInfoDeviceIndex=_MySlotInfoDeviceIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1,1),_MySlotInfoDeviceIndex_Type())
mySlotInfoDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mySlotInfoDeviceIndex.setStatus(_B)
_MySlotInfoIndex_Type=Integer32
_MySlotInfoIndex_Object=MibTableColumn
mySlotInfoIndex=_MySlotInfoIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1,2),_MySlotInfoIndex_Type())
mySlotInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mySlotInfoIndex.setStatus(_B)
_MySlotModuleInfoDescr_Type=DisplayString
_MySlotModuleInfoDescr_Object=MibTableColumn
mySlotModuleInfoDescr=_MySlotModuleInfoDescr_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1,3),_MySlotModuleInfoDescr_Type())
mySlotModuleInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mySlotModuleInfoDescr.setStatus(_B)
_MySlotInfoPortNumber_Type=Integer32
_MySlotInfoPortNumber_Object=MibTableColumn
mySlotInfoPortNumber=_MySlotInfoPortNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1,4),_MySlotInfoPortNumber_Type())
mySlotInfoPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mySlotInfoPortNumber.setStatus(_B)
_MySlotInfoPortMaxNumber_Type=Integer32
_MySlotInfoPortMaxNumber_Object=MibTableColumn
mySlotInfoPortMaxNumber=_MySlotInfoPortMaxNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1,5),_MySlotInfoPortMaxNumber_Type())
mySlotInfoPortMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mySlotInfoPortMaxNumber.setStatus(_B)
class _MySlotInfoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MySlotInfoDesc_Type.__name__=_D
_MySlotInfoDesc_Object=MibTableColumn
mySlotInfoDesc=_MySlotInfoDesc_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,3,1,6),_MySlotInfoDesc_Type())
mySlotInfoDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:mySlotInfoDesc.setStatus(_B)
_MyModuleTempStateTable_Object=MibTable
myModuleTempStateTable=_MyModuleTempStateTable_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,4))
if mibBuilder.loadTexts:myModuleTempStateTable.setStatus(_B)
_MyModuleTempStateEntry_Object=MibTableRow
myModuleTempStateEntry=_MyModuleTempStateEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,4,1))
myModuleTempStateEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:myModuleTempStateEntry.setStatus(_B)
_MyModuleTempStateDeviceIndex_Type=Integer32
_MyModuleTempStateDeviceIndex_Object=MibTableColumn
myModuleTempStateDeviceIndex=_MyModuleTempStateDeviceIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,4,1,1),_MyModuleTempStateDeviceIndex_Type())
myModuleTempStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myModuleTempStateDeviceIndex.setStatus(_B)
_MyModuleTempStateIndex_Type=Integer32
_MyModuleTempStateIndex_Object=MibTableColumn
myModuleTempStateIndex=_MyModuleTempStateIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,4,1,2),_MyModuleTempStateIndex_Type())
myModuleTempStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myModuleTempStateIndex.setStatus(_B)
class _MyModuleTempState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tempNormal',1),('tempWarning',2)))
_MyModuleTempState_Type.__name__=_E
_MyModuleTempState_Object=MibTableColumn
myModuleTempState=_MyModuleTempState_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,4,1,3),_MyModuleTempState_Type())
myModuleTempState.setMaxAccess(_C)
if mibBuilder.loadTexts:myModuleTempState.setStatus(_B)
_MyPowerStateTable_Object=MibTable
myPowerStateTable=_MyPowerStateTable_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,5))
if mibBuilder.loadTexts:myPowerStateTable.setStatus(_B)
_MyPowerStateEntry_Object=MibTableRow
myPowerStateEntry=_MyPowerStateEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,5,1))
myPowerStateEntry.setIndexNames((0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:myPowerStateEntry.setStatus(_B)
_MyPowerStateDeviceIndex_Type=Integer32
_MyPowerStateDeviceIndex_Object=MibTableColumn
myPowerStateDeviceIndex=_MyPowerStateDeviceIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,5,1,1),_MyPowerStateDeviceIndex_Type())
myPowerStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myPowerStateDeviceIndex.setStatus(_B)
_MyPowerStateIndex_Type=Integer32
_MyPowerStateIndex_Object=MibTableColumn
myPowerStateIndex=_MyPowerStateIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,5,1,2),_MyPowerStateIndex_Type())
myPowerStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myPowerStateIndex.setStatus(_B)
class _MyPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noLink',1),('linkAndNoPower',2),('linkAndReadyForPower',3),('linkAndPower',4),('linkAndPowerAbnormal',5)))
_MyPowerState_Type.__name__=_E
_MyPowerState_Object=MibTableColumn
myPowerState=_MyPowerState_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,5,1,3),_MyPowerState_Type())
myPowerState.setMaxAccess(_C)
if mibBuilder.loadTexts:myPowerState.setStatus(_B)
_MyFanStateTable_Object=MibTable
myFanStateTable=_MyFanStateTable_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,6))
if mibBuilder.loadTexts:myFanStateTable.setStatus(_B)
_MyFanStateEntry_Object=MibTableRow
myFanStateEntry=_MyFanStateEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,6,1))
myFanStateEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:myFanStateEntry.setStatus(_B)
_MyFanStateDeviceIndex_Type=Integer32
_MyFanStateDeviceIndex_Object=MibTableColumn
myFanStateDeviceIndex=_MyFanStateDeviceIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,6,1,1),_MyFanStateDeviceIndex_Type())
myFanStateDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myFanStateDeviceIndex.setStatus(_B)
_MyFanStateIndex_Type=Integer32
_MyFanStateIndex_Object=MibTableColumn
myFanStateIndex=_MyFanStateIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,6,1,2),_MyFanStateIndex_Type())
myFanStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myFanStateIndex.setStatus(_B)
class _MyFanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('work',1),('stop',2)))
_MyFanState_Type.__name__=_E
_MyFanState_Object=MibTableColumn
myFanState=_MyFanState_Object((1,3,6,1,4,1,4881,1,1,10,2,21,1,6,1,3),_MyFanState_Type())
myFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:myFanState.setStatus(_B)
_MyEntityMIBTraps_ObjectIdentity=ObjectIdentity
myEntityMIBTraps=_MyEntityMIBTraps_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,21,2))
_MyEntityStateChgDesc_Type=DisplayString
_MyEntityStateChgDesc_Object=MibScalar
myEntityStateChgDesc=_MyEntityStateChgDesc_Object((1,3,6,1,4,1,4881,1,1,10,2,21,2,1),_MyEntityStateChgDesc_Type())
myEntityStateChgDesc.setMaxAccess(_R)
if mibBuilder.loadTexts:myEntityStateChgDesc.setStatus(_B)
class _MyTemperatureWarningDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_MyTemperatureWarningDesc_Type.__name__=_D
_MyTemperatureWarningDesc_Object=MibScalar
myTemperatureWarningDesc=_MyTemperatureWarningDesc_Object((1,3,6,1,4,1,4881,1,1,10,2,21,2,3),_MyTemperatureWarningDesc_Type())
myTemperatureWarningDesc.setMaxAccess(_R)
if mibBuilder.loadTexts:myTemperatureWarningDesc.setStatus(_B)
_MyDeviceMIBConformance_ObjectIdentity=ObjectIdentity
myDeviceMIBConformance=_MyDeviceMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,21,3))
_MyDeviceMIBCompliances_ObjectIdentity=ObjectIdentity
myDeviceMIBCompliances=_MyDeviceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,21,3,1))
_MyDeviceMIBGroups_ObjectIdentity=ObjectIdentity
myDeviceMIBGroups=_MyDeviceMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,21,3,2))
myDeviceInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,1))
myDeviceInfoMIBGroup.setObjects(*((_A,_S),(_A,_F),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:myDeviceInfoMIBGroup.setStatus(_B)
myOptionalDevInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,2))
myOptionalDevInfoMIBGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:myOptionalDevInfoMIBGroup.setStatus(_B)
myModuleInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,3))
myModuleInfoMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:myModuleInfoMIBGroup.setStatus(_B)
myEntityChgDescGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,4))
myEntityChgDescGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:myEntityChgDescGroup.setStatus(_B)
myModuleTempStateGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,6))
myModuleTempStateGroup.setObjects(*((_A,_I),(_A,_J),(_A,_f)))
if mibBuilder.loadTexts:myModuleTempStateGroup.setStatus(_B)
myPowerStateGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,7))
myPowerStateGroup.setObjects(*((_A,_K),(_A,_L),(_A,_g)))
if mibBuilder.loadTexts:myPowerStateGroup.setStatus(_B)
myFanStateGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,8))
myFanStateGroup.setObjects(*((_A,_M),(_A,_N),(_A,_h)))
if mibBuilder.loadTexts:myFanStateGroup.setStatus(_B)
myTemperatureWarningDescGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,9))
myTemperatureWarningDescGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:myTemperatureWarningDescGroup.setStatus(_B)
myEntityStatusChange=NotificationType((1,3,6,1,4,1,4881,1,1,10,2,21,2,2))
myEntityStatusChange.setObjects((_A,_O))
if mibBuilder.loadTexts:myEntityStatusChange.setStatus(_B)
myTemperatureWarning=NotificationType((1,3,6,1,4,1,4881,1,1,10,2,21,2,4))
myTemperatureWarning.setObjects((_A,_P))
if mibBuilder.loadTexts:myTemperatureWarning.setStatus(_B)
myDeviceMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,5))
myDeviceMIBNotificationGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:myDeviceMIBNotificationGroup.setStatus(_B)
myTemperatureWarningGroup=NotificationGroup((1,3,6,1,4,1,4881,1,1,10,2,21,3,2,10))
myTemperatureWarningGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:myTemperatureWarningGroup.setStatus(_B)
myDeviceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,21,3,1,1))
myDeviceMIBCompliance.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:myDeviceMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'myEntityMIB':myEntityMIB,'myDeviceMIBObjects':myDeviceMIBObjects,_S:myDeviceMaxNumber,'myDeviceInfoTable':myDeviceInfoTable,'myDeviceInfoEntry':myDeviceInfoEntry,_F:myDeviceInfoIndex,_T:myDeviceInfoDescr,_U:myDeviceInfoSlotNumber,_V:myDevicePowerStatus,_W:myDeviceMacAddress,_X:myDevicePriority,_Y:myDeviceAlias,_Z:myDeviceSWVersion,_a:myDeviceHWVersion,'mySlotInfoTable':mySlotInfoTable,'mySlotInfoEntry':mySlotInfoEntry,_G:mySlotInfoDeviceIndex,_H:mySlotInfoIndex,_b:mySlotModuleInfoDescr,_c:mySlotInfoPortNumber,_d:mySlotInfoPortMaxNumber,_e:mySlotInfoDesc,'myModuleTempStateTable':myModuleTempStateTable,'myModuleTempStateEntry':myModuleTempStateEntry,_I:myModuleTempStateDeviceIndex,_J:myModuleTempStateIndex,_f:myModuleTempState,'myPowerStateTable':myPowerStateTable,'myPowerStateEntry':myPowerStateEntry,_K:myPowerStateDeviceIndex,_L:myPowerStateIndex,_g:myPowerState,'myFanStateTable':myFanStateTable,'myFanStateEntry':myFanStateEntry,_M:myFanStateDeviceIndex,_N:myFanStateIndex,_h:myFanState,'myEntityMIBTraps':myEntityMIBTraps,_O:myEntityStateChgDesc,_i:myEntityStatusChange,_P:myTemperatureWarningDesc,_j:myTemperatureWarning,'myDeviceMIBConformance':myDeviceMIBConformance,'myDeviceMIBCompliances':myDeviceMIBCompliances,'myDeviceMIBCompliance':myDeviceMIBCompliance,'myDeviceMIBGroups':myDeviceMIBGroups,_k:myDeviceInfoMIBGroup,_m:myOptionalDevInfoMIBGroup,_l:myModuleInfoMIBGroup,_n:myEntityChgDescGroup,_o:myDeviceMIBNotificationGroup,_p:myModuleTempStateGroup,_q:myPowerStateGroup,_r:myFanStateGroup,_s:myTemperatureWarningDescGroup,_t:myTemperatureWarningGroup})