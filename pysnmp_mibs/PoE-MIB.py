_R='swPoEPortInfoPortIndex'
_Q='swPoEPortCtrlPortIndex'
_P='swPoESystemInfoUnitId'
_O='swPoESystemStackingCtrlUnitId'
_N='normal'
_M='DisplayString'
_L='SnmpAdminString'
_K='disabled'
_J='enabled'
_I='auto'
_H='power-limit'
_G='denyLowPriorityPort'
_F='denyNextPort'
_E='PoE-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
swPoEMIB=ModuleIdentity((1,3,6,1,4,1,171,12,24))
_SwPoESystemCtrl_ObjectIdentity=ObjectIdentity
swPoESystemCtrl=_SwPoESystemCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,24,1))
_SwPoESystemPowerLimit_Type=Integer32
_SwPoESystemPowerLimit_Object=MibScalar
swPoESystemPowerLimit=_SwPoESystemPowerLimit_Object((1,3,6,1,4,1,171,12,24,1,1),_SwPoESystemPowerLimit_Type())
swPoESystemPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemPowerLimit.setStatus(_A)
class _SwPoESystemPowerDisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPoESystemPowerDisconnectMethod_Type.__name__=_B
_SwPoESystemPowerDisconnectMethod_Object=MibScalar
swPoESystemPowerDisconnectMethod=_SwPoESystemPowerDisconnectMethod_Object((1,3,6,1,4,1,171,12,24,1,2),_SwPoESystemPowerDisconnectMethod_Type())
swPoESystemPowerDisconnectMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemPowerDisconnectMethod.setStatus(_A)
class _SwPoESystemManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwPoESystemManagementMode_Type.__name__=_B
_SwPoESystemManagementMode_Object=MibScalar
swPoESystemManagementMode=_SwPoESystemManagementMode_Object((1,3,6,1,4,1,171,12,24,1,3),_SwPoESystemManagementMode_Type())
swPoESystemManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemManagementMode.setStatus(_A)
class _SwPoESystemLedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('poe',2)))
_SwPoESystemLedMode_Type.__name__=_B
_SwPoESystemLedMode_Object=MibScalar
swPoESystemLedMode=_SwPoESystemLedMode_Object((1,3,6,1,4,1,171,12,24,1,4),_SwPoESystemLedMode_Type())
swPoESystemLedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemLedMode.setStatus(_A)
class _SwPoESystemCtrlLegacyPD_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwPoESystemCtrlLegacyPD_Type.__name__=_B
_SwPoESystemCtrlLegacyPD_Object=MibScalar
swPoESystemCtrlLegacyPD=_SwPoESystemCtrlLegacyPD_Object((1,3,6,1,4,1,171,12,24,1,6),_SwPoESystemCtrlLegacyPD_Type())
swPoESystemCtrlLegacyPD.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemCtrlLegacyPD.setStatus(_A)
_SwPoESystemStackingCtrlTable_Object=MibTable
swPoESystemStackingCtrlTable=_SwPoESystemStackingCtrlTable_Object((1,3,6,1,4,1,171,12,24,1,11))
if mibBuilder.loadTexts:swPoESystemStackingCtrlTable.setStatus(_A)
_SwPoESystemStackingCtrlEntry_Object=MibTableRow
swPoESystemStackingCtrlEntry=_SwPoESystemStackingCtrlEntry_Object((1,3,6,1,4,1,171,12,24,1,11,1))
swPoESystemStackingCtrlEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:swPoESystemStackingCtrlEntry.setStatus(_A)
class _SwPoESystemStackingCtrlUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPoESystemStackingCtrlUnitId_Type.__name__=_B
_SwPoESystemStackingCtrlUnitId_Object=MibTableColumn
swPoESystemStackingCtrlUnitId=_SwPoESystemStackingCtrlUnitId_Object((1,3,6,1,4,1,171,12,24,1,11,1,1),_SwPoESystemStackingCtrlUnitId_Type())
swPoESystemStackingCtrlUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemStackingCtrlUnitId.setStatus(_A)
_SwPoESystemStackingCtrlPowerLimit_Type=Integer32
_SwPoESystemStackingCtrlPowerLimit_Object=MibTableColumn
swPoESystemStackingCtrlPowerLimit=_SwPoESystemStackingCtrlPowerLimit_Object((1,3,6,1,4,1,171,12,24,1,11,1,2),_SwPoESystemStackingCtrlPowerLimit_Type())
swPoESystemStackingCtrlPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemStackingCtrlPowerLimit.setStatus(_A)
class _SwPoESystemStackingCtrlPowerDisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPoESystemStackingCtrlPowerDisconnectMethod_Type.__name__=_B
_SwPoESystemStackingCtrlPowerDisconnectMethod_Object=MibTableColumn
swPoESystemStackingCtrlPowerDisconnectMethod=_SwPoESystemStackingCtrlPowerDisconnectMethod_Object((1,3,6,1,4,1,171,12,24,1,11,1,3),_SwPoESystemStackingCtrlPowerDisconnectMethod_Type())
swPoESystemStackingCtrlPowerDisconnectMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemStackingCtrlPowerDisconnectMethod.setStatus(_A)
class _SwPoESystemStackingCtrlManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwPoESystemStackingCtrlManagementMode_Type.__name__=_B
_SwPoESystemStackingCtrlManagementMode_Object=MibTableColumn
swPoESystemStackingCtrlManagementMode=_SwPoESystemStackingCtrlManagementMode_Object((1,3,6,1,4,1,171,12,24,1,11,1,4),_SwPoESystemStackingCtrlManagementMode_Type())
swPoESystemStackingCtrlManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemStackingCtrlManagementMode.setStatus(_A)
class _SwPoESystemStackingCtrlLedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('poe',2)))
_SwPoESystemStackingCtrlLedMode_Type.__name__=_B
_SwPoESystemStackingCtrlLedMode_Object=MibTableColumn
swPoESystemStackingCtrlLedMode=_SwPoESystemStackingCtrlLedMode_Object((1,3,6,1,4,1,171,12,24,1,11,1,5),_SwPoESystemStackingCtrlLedMode_Type())
swPoESystemStackingCtrlLedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemStackingCtrlLedMode.setStatus(_A)
class _SwPoESystemStackingCtrlLegacyPD_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwPoESystemStackingCtrlLegacyPD_Type.__name__=_B
_SwPoESystemStackingCtrlLegacyPD_Object=MibTableColumn
swPoESystemStackingCtrlLegacyPD=_SwPoESystemStackingCtrlLegacyPD_Object((1,3,6,1,4,1,171,12,24,1,11,1,6),_SwPoESystemStackingCtrlLegacyPD_Type())
swPoESystemStackingCtrlLegacyPD.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoESystemStackingCtrlLegacyPD.setStatus(_A)
_SwPoESystemInfo_ObjectIdentity=ObjectIdentity
swPoESystemInfo=_SwPoESystemInfo_ObjectIdentity((1,3,6,1,4,1,171,12,24,2))
_SwPoESystemInfoTable_Object=MibTable
swPoESystemInfoTable=_SwPoESystemInfoTable_Object((1,3,6,1,4,1,171,12,24,2,1))
if mibBuilder.loadTexts:swPoESystemInfoTable.setStatus(_A)
_SwPoESystemInfoEntry_Object=MibTableRow
swPoESystemInfoEntry=_SwPoESystemInfoEntry_Object((1,3,6,1,4,1,171,12,24,2,1,1))
swPoESystemInfoEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:swPoESystemInfoEntry.setStatus(_A)
class _SwPoESystemInfoUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPoESystemInfoUnitId_Type.__name__=_B
_SwPoESystemInfoUnitId_Object=MibTableColumn
swPoESystemInfoUnitId=_SwPoESystemInfoUnitId_Object((1,3,6,1,4,1,171,12,24,2,1,1,1),_SwPoESystemInfoUnitId_Type())
swPoESystemInfoUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoUnitId.setStatus(_A)
_SwPoESystemInfoPowerConsumption_Type=Integer32
_SwPoESystemInfoPowerConsumption_Object=MibTableColumn
swPoESystemInfoPowerConsumption=_SwPoESystemInfoPowerConsumption_Object((1,3,6,1,4,1,171,12,24,2,1,1,2),_SwPoESystemInfoPowerConsumption_Type())
swPoESystemInfoPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoPowerConsumption.setStatus(_A)
_SwPoESystemInfoPowerRemained_Type=Integer32
_SwPoESystemInfoPowerRemained_Object=MibTableColumn
swPoESystemInfoPowerRemained=_SwPoESystemInfoPowerRemained_Object((1,3,6,1,4,1,171,12,24,2,1,1,3),_SwPoESystemInfoPowerRemained_Type())
swPoESystemInfoPowerRemained.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoPowerRemained.setStatus(_A)
_SwPoESystemInfoPowerLimit_Type=Integer32
_SwPoESystemInfoPowerLimit_Object=MibTableColumn
swPoESystemInfoPowerLimit=_SwPoESystemInfoPowerLimit_Object((1,3,6,1,4,1,171,12,24,2,1,1,4),_SwPoESystemInfoPowerLimit_Type())
swPoESystemInfoPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoPowerLimit.setStatus(_A)
class _SwPoESystemInfoPowerDisconnectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPoESystemInfoPowerDisconnectMethod_Type.__name__=_B
_SwPoESystemInfoPowerDisconnectMethod_Object=MibTableColumn
swPoESystemInfoPowerDisconnectMethod=_SwPoESystemInfoPowerDisconnectMethod_Object((1,3,6,1,4,1,171,12,24,2,1,1,5),_SwPoESystemInfoPowerDisconnectMethod_Type())
swPoESystemInfoPowerDisconnectMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoPowerDisconnectMethod.setStatus(_A)
class _SwPoESystemInfoManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SwPoESystemInfoManagementMode_Type.__name__=_B
_SwPoESystemInfoManagementMode_Object=MibTableColumn
swPoESystemInfoManagementMode=_SwPoESystemInfoManagementMode_Object((1,3,6,1,4,1,171,12,24,2,1,1,6),_SwPoESystemInfoManagementMode_Type())
swPoESystemInfoManagementMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoManagementMode.setStatus(_A)
class _SwPoESystemInfoLegacyPD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwPoESystemInfoLegacyPD_Type.__name__=_B
_SwPoESystemInfoLegacyPD_Object=MibTableColumn
swPoESystemInfoLegacyPD=_SwPoESystemInfoLegacyPD_Object((1,3,6,1,4,1,171,12,24,2,1,1,7),_SwPoESystemInfoLegacyPD_Type())
swPoESystemInfoLegacyPD.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoESystemInfoLegacyPD.setStatus(_A)
_SwPoEPortCtrl_ObjectIdentity=ObjectIdentity
swPoEPortCtrl=_SwPoEPortCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,24,3))
_SwPoEPortCtrlTable_Object=MibTable
swPoEPortCtrlTable=_SwPoEPortCtrlTable_Object((1,3,6,1,4,1,171,12,24,3,1))
if mibBuilder.loadTexts:swPoEPortCtrlTable.setStatus(_A)
_SwPoEPortCtrlEntry_Object=MibTableRow
swPoEPortCtrlEntry=_SwPoEPortCtrlEntry_Object((1,3,6,1,4,1,171,12,24,3,1,1))
swPoEPortCtrlEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:swPoEPortCtrlEntry.setStatus(_A)
class _SwPoEPortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPoEPortCtrlPortIndex_Type.__name__=_B
_SwPoEPortCtrlPortIndex_Object=MibTableColumn
swPoEPortCtrlPortIndex=_SwPoEPortCtrlPortIndex_Object((1,3,6,1,4,1,171,12,24,3,1,1,1),_SwPoEPortCtrlPortIndex_Type())
swPoEPortCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortCtrlPortIndex.setStatus(_A)
class _SwPoEPortCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('enable',2),('disable',3)))
_SwPoEPortCtrlState_Type.__name__=_B
_SwPoEPortCtrlState_Object=MibTableColumn
swPoEPortCtrlState=_SwPoEPortCtrlState_Object((1,3,6,1,4,1,171,12,24,3,1,1,2),_SwPoEPortCtrlState_Type())
swPoEPortCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoEPortCtrlState.setStatus(_A)
class _SwPoEPortCtrlPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_SwPoEPortCtrlPriority_Type.__name__=_B
_SwPoEPortCtrlPriority_Object=MibTableColumn
swPoEPortCtrlPriority=_SwPoEPortCtrlPriority_Object((1,3,6,1,4,1,171,12,24,3,1,1,3),_SwPoEPortCtrlPriority_Type())
swPoEPortCtrlPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoEPortCtrlPriority.setStatus(_A)
class _SwPoEPortCtrlPowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('user-defined',5)))
_SwPoEPortCtrlPowerLimit_Type.__name__=_B
_SwPoEPortCtrlPowerLimit_Object=MibTableColumn
swPoEPortCtrlPowerLimit=_SwPoEPortCtrlPowerLimit_Object((1,3,6,1,4,1,171,12,24,3,1,1,4),_SwPoEPortCtrlPowerLimit_Type())
swPoEPortCtrlPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoEPortCtrlPowerLimit.setStatus(_A)
class _SwPoEPortCtrlUserDefined_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,35000))
_SwPoEPortCtrlUserDefined_Type.__name__=_B
_SwPoEPortCtrlUserDefined_Object=MibTableColumn
swPoEPortCtrlUserDefined=_SwPoEPortCtrlUserDefined_Object((1,3,6,1,4,1,171,12,24,3,1,1,5),_SwPoEPortCtrlUserDefined_Type())
swPoEPortCtrlUserDefined.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoEPortCtrlUserDefined.setStatus(_A)
class _SwPoEPortCtrlTimeRangeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwPoEPortCtrlTimeRangeName_Type.__name__=_L
_SwPoEPortCtrlTimeRangeName_Object=MibTableColumn
swPoEPortCtrlTimeRangeName=_SwPoEPortCtrlTimeRangeName_Object((1,3,6,1,4,1,171,12,24,3,1,1,6),_SwPoEPortCtrlTimeRangeName_Type())
swPoEPortCtrlTimeRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:swPoEPortCtrlTimeRangeName.setStatus(_A)
_SwPoEPortInfo_ObjectIdentity=ObjectIdentity
swPoEPortInfo=_SwPoEPortInfo_ObjectIdentity((1,3,6,1,4,1,171,12,24,4))
_SwPoEPortInfoTable_Object=MibTable
swPoEPortInfoTable=_SwPoEPortInfoTable_Object((1,3,6,1,4,1,171,12,24,4,1))
if mibBuilder.loadTexts:swPoEPortInfoTable.setStatus(_A)
_SwPoEPortInfoEntry_Object=MibTableRow
swPoEPortInfoEntry=_SwPoEPortInfoEntry_Object((1,3,6,1,4,1,171,12,24,4,1,1))
swPoEPortInfoEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:swPoEPortInfoEntry.setStatus(_A)
class _SwPoEPortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPoEPortInfoPortIndex_Type.__name__=_B
_SwPoEPortInfoPortIndex_Object=MibTableColumn
swPoEPortInfoPortIndex=_SwPoEPortInfoPortIndex_Object((1,3,6,1,4,1,171,12,24,4,1,1,1),_SwPoEPortInfoPortIndex_Type())
swPoEPortInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortInfoPortIndex.setStatus(_A)
class _SwPoEPortInfoClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_SwPoEPortInfoClass_Type.__name__=_B
_SwPoEPortInfoClass_Object=MibTableColumn
swPoEPortInfoClass=_SwPoEPortInfoClass_Object((1,3,6,1,4,1,171,12,24,4,1,1,2),_SwPoEPortInfoClass_Type())
swPoEPortInfoClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortInfoClass.setStatus(_A)
_SwPoEPortInfoPower_Type=Integer32
_SwPoEPortInfoPower_Object=MibTableColumn
swPoEPortInfoPower=_SwPoEPortInfoPower_Object((1,3,6,1,4,1,171,12,24,4,1,1,3),_SwPoEPortInfoPower_Type())
swPoEPortInfoPower.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortInfoPower.setStatus(_A)
_SwPoEPortInfoVoltage_Type=Integer32
_SwPoEPortInfoVoltage_Object=MibTableColumn
swPoEPortInfoVoltage=_SwPoEPortInfoVoltage_Object((1,3,6,1,4,1,171,12,24,4,1,1,4),_SwPoEPortInfoVoltage_Type())
swPoEPortInfoVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortInfoVoltage.setStatus(_A)
_SwPoEPortInfoCurrent_Type=Integer32
_SwPoEPortInfoCurrent_Object=MibTableColumn
swPoEPortInfoCurrent=_SwPoEPortInfoCurrent_Object((1,3,6,1,4,1,171,12,24,4,1,1,5),_SwPoEPortInfoCurrent_Type())
swPoEPortInfoCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortInfoCurrent.setStatus(_A)
class _SwPoEPortInfoStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,76))
_SwPoEPortInfoStatus_Type.__name__=_M
_SwPoEPortInfoStatus_Object=MibTableColumn
swPoEPortInfoStatus=_SwPoEPortInfoStatus_Object((1,3,6,1,4,1,171,12,24,4,1,1,6),_SwPoEPortInfoStatus_Type())
swPoEPortInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPoEPortInfoStatus.setStatus(_A)
class _SwpoEPortInfoLedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('error',3)))
_SwpoEPortInfoLedStatus_Type.__name__=_B
_SwpoEPortInfoLedStatus_Object=MibTableColumn
swpoEPortInfoLedStatus=_SwpoEPortInfoLedStatus_Object((1,3,6,1,4,1,171,12,24,4,1,1,7),_SwpoEPortInfoLedStatus_Type())
swpoEPortInfoLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swpoEPortInfoLedStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swPoEMIB':swPoEMIB,'swPoESystemCtrl':swPoESystemCtrl,'swPoESystemPowerLimit':swPoESystemPowerLimit,'swPoESystemPowerDisconnectMethod':swPoESystemPowerDisconnectMethod,'swPoESystemManagementMode':swPoESystemManagementMode,'swPoESystemLedMode':swPoESystemLedMode,'swPoESystemCtrlLegacyPD':swPoESystemCtrlLegacyPD,'swPoESystemStackingCtrlTable':swPoESystemStackingCtrlTable,'swPoESystemStackingCtrlEntry':swPoESystemStackingCtrlEntry,_O:swPoESystemStackingCtrlUnitId,'swPoESystemStackingCtrlPowerLimit':swPoESystemStackingCtrlPowerLimit,'swPoESystemStackingCtrlPowerDisconnectMethod':swPoESystemStackingCtrlPowerDisconnectMethod,'swPoESystemStackingCtrlManagementMode':swPoESystemStackingCtrlManagementMode,'swPoESystemStackingCtrlLedMode':swPoESystemStackingCtrlLedMode,'swPoESystemStackingCtrlLegacyPD':swPoESystemStackingCtrlLegacyPD,'swPoESystemInfo':swPoESystemInfo,'swPoESystemInfoTable':swPoESystemInfoTable,'swPoESystemInfoEntry':swPoESystemInfoEntry,_P:swPoESystemInfoUnitId,'swPoESystemInfoPowerConsumption':swPoESystemInfoPowerConsumption,'swPoESystemInfoPowerRemained':swPoESystemInfoPowerRemained,'swPoESystemInfoPowerLimit':swPoESystemInfoPowerLimit,'swPoESystemInfoPowerDisconnectMethod':swPoESystemInfoPowerDisconnectMethod,'swPoESystemInfoManagementMode':swPoESystemInfoManagementMode,'swPoESystemInfoLegacyPD':swPoESystemInfoLegacyPD,'swPoEPortCtrl':swPoEPortCtrl,'swPoEPortCtrlTable':swPoEPortCtrlTable,'swPoEPortCtrlEntry':swPoEPortCtrlEntry,_Q:swPoEPortCtrlPortIndex,'swPoEPortCtrlState':swPoEPortCtrlState,'swPoEPortCtrlPriority':swPoEPortCtrlPriority,'swPoEPortCtrlPowerLimit':swPoEPortCtrlPowerLimit,'swPoEPortCtrlUserDefined':swPoEPortCtrlUserDefined,'swPoEPortCtrlTimeRangeName':swPoEPortCtrlTimeRangeName,'swPoEPortInfo':swPoEPortInfo,'swPoEPortInfoTable':swPoEPortInfoTable,'swPoEPortInfoEntry':swPoEPortInfoEntry,_R:swPoEPortInfoPortIndex,'swPoEPortInfoClass':swPoEPortInfoClass,'swPoEPortInfoPower':swPoEPortInfoPower,'swPoEPortInfoVoltage':swPoEPortInfoVoltage,'swPoEPortInfoCurrent':swPoEPortInfoCurrent,'swPoEPortInfoStatus':swPoEPortInfoStatus,'swpoEPortInfoLedStatus':swpoEPortInfoLedStatus})