_T='rlAutoSmartTrunkRefreshIfIndex'
_S='rlAutoSmartTrunkRefreshSmartPortType'
_R='rlAutoSmartPortParamName'
_Q='rlAutoSmartPortIfIndex'
_P='rlAutoSmartPortPort'
_O='rlAutoSmartPortMacrosParamName'
_N='rlAutoSmartPortMacroType'
_M='router'
_L='switch'
_K='SmartPortType'
_J='rlAutoSmartPortTypesType'
_I='default'
_H='disabled'
_G='enabled'
_F='read-only'
_E='not-accessible'
_D='Integer32'
_C='CISCOSB-AUTOSMARTPORTS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
RlSmartPortsMacroNameOrZero,=mibBuilder.importSymbols('CISCOSB-MACRO-MIB','RlSmartPortsMacroNameOrZero')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlAutoSmartportsMib=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,150))
if mibBuilder.loadTexts:rlAutoSmartportsMib.setRevisions(('2010-09-11 00:00',))
class SmartPortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('unknown',1),(_I,2),('printer',3),('desktop',4),('guest',5),('server',6),('host',7),('ip-camera',8),('ip-phone',9),('ip-phone-desktop',10),(_L,11),(_M,12),('ap',13)))
class SmartPortMacroParameterName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class SmartPortMacroParameterValue(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
class SmartPortMacroType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('built-in',1),('user-defined',2)))
class SmartPortMacroParameterOrder(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('single',1),('first',2),('middle',3),('last',4)))
_RlPortEvents_ObjectIdentity=ObjectIdentity
rlPortEvents=_RlPortEvents_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,150,1))
class _RlAutoSmartPortAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('controlled',3)))
_RlAutoSmartPortAdminStatus_Type.__name__=_D
_RlAutoSmartPortAdminStatus_Object=MibScalar
rlAutoSmartPortAdminStatus=_RlAutoSmartPortAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,150,1,1),_RlAutoSmartPortAdminStatus_Type())
rlAutoSmartPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortAdminStatus.setStatus(_A)
class _RlAutoSmartPortOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RlAutoSmartPortOperStatus_Type.__name__=_D
_RlAutoSmartPortOperStatus_Object=MibScalar
rlAutoSmartPortOperStatus=_RlAutoSmartPortOperStatus_Object((1,3,6,1,4,1,9,6,1,101,150,1,2),_RlAutoSmartPortOperStatus_Type())
rlAutoSmartPortOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortOperStatus.setStatus(_A)
class _RlAutoSmartPortLastVoiceVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RlAutoSmartPortLastVoiceVlanStatus_Type.__name__=_D
_RlAutoSmartPortLastVoiceVlanStatus_Object=MibScalar
rlAutoSmartPortLastVoiceVlanStatus=_RlAutoSmartPortLastVoiceVlanStatus_Object((1,3,6,1,4,1,9,6,1,101,150,1,3),_RlAutoSmartPortLastVoiceVlanStatus_Type())
rlAutoSmartPortLastVoiceVlanStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortLastVoiceVlanStatus.setStatus(_A)
_RlAutoSmartPortLastVoiceVlanId_Type=Integer32
_RlAutoSmartPortLastVoiceVlanId_Object=MibScalar
rlAutoSmartPortLastVoiceVlanId=_RlAutoSmartPortLastVoiceVlanId_Object((1,3,6,1,4,1,9,6,1,101,150,1,4),_RlAutoSmartPortLastVoiceVlanId_Type())
rlAutoSmartPortLastVoiceVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortLastVoiceVlanId.setStatus(_A)
class _RlAutoSmartPortLearningProtocols_Type(Bits):namedValues=NamedValues(*(('cdp',0),('lldp',1)))
_RlAutoSmartPortLearningProtocols_Type.__name__='Bits'
_RlAutoSmartPortLearningProtocols_Object=MibScalar
rlAutoSmartPortLearningProtocols=_RlAutoSmartPortLearningProtocols_Object((1,3,6,1,4,1,9,6,1,101,150,1,5),_RlAutoSmartPortLearningProtocols_Type())
rlAutoSmartPortLearningProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortLearningProtocols.setStatus(_A)
_RlAutoSmartPortTypesTable_Object=MibTable
rlAutoSmartPortTypesTable=_RlAutoSmartPortTypesTable_Object((1,3,6,1,4,1,9,6,1,101,150,1,6))
if mibBuilder.loadTexts:rlAutoSmartPortTypesTable.setStatus(_A)
_RlAutoSmartPortTypesEntry_Object=MibTableRow
rlAutoSmartPortTypesEntry=_RlAutoSmartPortTypesEntry_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1))
rlAutoSmartPortTypesEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:rlAutoSmartPortTypesEntry.setStatus(_A)
_RlAutoSmartPortTypesType_Type=SmartPortType
_RlAutoSmartPortTypesType_Object=MibTableColumn
rlAutoSmartPortTypesType=_RlAutoSmartPortTypesType_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1,1),_RlAutoSmartPortTypesType_Type())
rlAutoSmartPortTypesType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortTypesType.setStatus(_A)
class _RlAutoSmartPortTypeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_RlAutoSmartPortTypeStatus_Type.__name__=_D
_RlAutoSmartPortTypeStatus_Object=MibTableColumn
rlAutoSmartPortTypeStatus=_RlAutoSmartPortTypeStatus_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1,2),_RlAutoSmartPortTypeStatus_Type())
rlAutoSmartPortTypeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortTypeStatus.setStatus(_A)
_RlAutoSmartPortMacro_Type=RlSmartPortsMacroNameOrZero
_RlAutoSmartPortMacro_Object=MibTableColumn
rlAutoSmartPortMacro=_RlAutoSmartPortMacro_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1,3),_RlAutoSmartPortMacro_Type())
rlAutoSmartPortMacro.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortMacro.setStatus(_A)
_RlAutoSmartPortTypesRevertToDefaultMacro_Type=TruthValue
_RlAutoSmartPortTypesRevertToDefaultMacro_Object=MibTableColumn
rlAutoSmartPortTypesRevertToDefaultMacro=_RlAutoSmartPortTypesRevertToDefaultMacro_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1,4),_RlAutoSmartPortTypesRevertToDefaultMacro_Type())
rlAutoSmartPortTypesRevertToDefaultMacro.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortTypesRevertToDefaultMacro.setStatus(_A)
_RlAutoSmartPortTypesRevertToDefaultParams_Type=TruthValue
_RlAutoSmartPortTypesRevertToDefaultParams_Object=MibTableColumn
rlAutoSmartPortTypesRevertToDefaultParams=_RlAutoSmartPortTypesRevertToDefaultParams_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1,5),_RlAutoSmartPortTypesRevertToDefaultParams_Type())
rlAutoSmartPortTypesRevertToDefaultParams.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortTypesRevertToDefaultParams.setStatus(_A)
_RlAutoSmartPortTypesBuiltinMacro_Type=SmartPortMacroType
_RlAutoSmartPortTypesBuiltinMacro_Object=MibTableColumn
rlAutoSmartPortTypesBuiltinMacro=_RlAutoSmartPortTypesBuiltinMacro_Object((1,3,6,1,4,1,9,6,1,101,150,1,6,1,6),_RlAutoSmartPortTypesBuiltinMacro_Type())
rlAutoSmartPortTypesBuiltinMacro.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortTypesBuiltinMacro.setStatus(_A)
_RlAutoSmartPortMacrosParamTable_Object=MibTable
rlAutoSmartPortMacrosParamTable=_RlAutoSmartPortMacrosParamTable_Object((1,3,6,1,4,1,9,6,1,101,150,1,7))
if mibBuilder.loadTexts:rlAutoSmartPortMacrosParamTable.setStatus(_A)
_RlAutoSmartPortMacrosParamEntry_Object=MibTableRow
rlAutoSmartPortMacrosParamEntry=_RlAutoSmartPortMacrosParamEntry_Object((1,3,6,1,4,1,9,6,1,101,150,1,7,1))
rlAutoSmartPortMacrosParamEntry.setIndexNames((0,_C,_J),(0,_C,_N),(1,_C,_O))
if mibBuilder.loadTexts:rlAutoSmartPortMacrosParamEntry.setStatus(_A)
_RlAutoSmartPortMacroType_Type=SmartPortMacroType
_RlAutoSmartPortMacroType_Object=MibTableColumn
rlAutoSmartPortMacroType=_RlAutoSmartPortMacroType_Object((1,3,6,1,4,1,9,6,1,101,150,1,7,1,1),_RlAutoSmartPortMacroType_Type())
rlAutoSmartPortMacroType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortMacroType.setStatus(_A)
_RlAutoSmartPortMacrosParamName_Type=SmartPortMacroParameterName
_RlAutoSmartPortMacrosParamName_Object=MibTableColumn
rlAutoSmartPortMacrosParamName=_RlAutoSmartPortMacrosParamName_Object((1,3,6,1,4,1,9,6,1,101,150,1,7,1,2),_RlAutoSmartPortMacrosParamName_Type())
rlAutoSmartPortMacrosParamName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortMacrosParamName.setStatus(_A)
_RlAutoSmartPortMacrosParamOrder_Type=SmartPortMacroParameterOrder
_RlAutoSmartPortMacrosParamOrder_Object=MibTableColumn
rlAutoSmartPortMacrosParamOrder=_RlAutoSmartPortMacrosParamOrder_Object((1,3,6,1,4,1,9,6,1,101,150,1,7,1,3),_RlAutoSmartPortMacrosParamOrder_Type())
rlAutoSmartPortMacrosParamOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortMacrosParamOrder.setStatus(_A)
_RlAutoSmartPortMacrosParamValue_Type=SmartPortMacroParameterValue
_RlAutoSmartPortMacrosParamValue_Object=MibTableColumn
rlAutoSmartPortMacrosParamValue=_RlAutoSmartPortMacrosParamValue_Object((1,3,6,1,4,1,9,6,1,101,150,1,7,1,4),_RlAutoSmartPortMacrosParamValue_Type())
rlAutoSmartPortMacrosParamValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortMacrosParamValue.setStatus(_A)
_RlAutoSmartPortPortsTable_Object=MibTable
rlAutoSmartPortPortsTable=_RlAutoSmartPortPortsTable_Object((1,3,6,1,4,1,9,6,1,101,150,1,8))
if mibBuilder.loadTexts:rlAutoSmartPortPortsTable.setStatus(_A)
_RlAutoSmartPortPortsEntry_Object=MibTableRow
rlAutoSmartPortPortsEntry=_RlAutoSmartPortPortsEntry_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1))
rlAutoSmartPortPortsEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:rlAutoSmartPortPortsEntry.setStatus(_A)
_RlAutoSmartPortPort_Type=InterfaceIndex
_RlAutoSmartPortPort_Object=MibTableColumn
rlAutoSmartPortPort=_RlAutoSmartPortPort_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,1),_RlAutoSmartPortPort_Type())
rlAutoSmartPortPort.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortPort.setStatus(_A)
class _RlAutoSmartPortPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RlAutoSmartPortPortStatus_Type.__name__=_D
_RlAutoSmartPortPortStatus_Object=MibTableColumn
rlAutoSmartPortPortStatus=_RlAutoSmartPortPortStatus_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,2),_RlAutoSmartPortPortStatus_Type())
rlAutoSmartPortPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortPortStatus.setStatus(_A)
class _RlAutoSmartPortPortType_Type(SmartPortType):defaultValue=2
_RlAutoSmartPortPortType_Type.__name__=_K
_RlAutoSmartPortPortType_Object=MibTableColumn
rlAutoSmartPortPortType=_RlAutoSmartPortPortType_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,3),_RlAutoSmartPortPortType_Type())
rlAutoSmartPortPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortPortType.setStatus(_A)
class _RlAutoSmartPortPersistency_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('persistent',1),('not-persistent',2)))
_RlAutoSmartPortPersistency_Type.__name__=_D
_RlAutoSmartPortPersistency_Object=MibTableColumn
rlAutoSmartPortPersistency=_RlAutoSmartPortPersistency_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,4),_RlAutoSmartPortPersistency_Type())
rlAutoSmartPortPersistency.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortPersistency.setStatus(_A)
class _RlAutoSmartPortLearntPortType_Type(SmartPortType):defaultValue=2
_RlAutoSmartPortLearntPortType_Type.__name__=_K
_RlAutoSmartPortLearntPortType_Object=MibTableColumn
rlAutoSmartPortLearntPortType=_RlAutoSmartPortLearntPortType_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,5),_RlAutoSmartPortLearntPortType_Type())
rlAutoSmartPortLearntPortType.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortLearntPortType.setStatus(_A)
class _RlAutoSmartPortPortAcquiringType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('configuration',2),('persistency',3),('learning',4)))
_RlAutoSmartPortPortAcquiringType_Type.__name__=_D
_RlAutoSmartPortPortAcquiringType_Object=MibTableColumn
rlAutoSmartPortPortAcquiringType=_RlAutoSmartPortPortAcquiringType_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,6),_RlAutoSmartPortPortAcquiringType_Type())
rlAutoSmartPortPortAcquiringType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortPortAcquiringType.setStatus(_A)
_RlAutoSmartPortLastActivatedMacro_Type=RlSmartPortsMacroNameOrZero
_RlAutoSmartPortLastActivatedMacro_Object=MibTableColumn
rlAutoSmartPortLastActivatedMacro=_RlAutoSmartPortLastActivatedMacro_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,7),_RlAutoSmartPortLastActivatedMacro_Type())
rlAutoSmartPortLastActivatedMacro.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortLastActivatedMacro.setStatus(_A)
_RlAutoSmartPortFailedCommandNumber_Type=Integer32
_RlAutoSmartPortFailedCommandNumber_Object=MibTableColumn
rlAutoSmartPortFailedCommandNumber=_RlAutoSmartPortFailedCommandNumber_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,8),_RlAutoSmartPortFailedCommandNumber_Type())
rlAutoSmartPortFailedCommandNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartPortFailedCommandNumber.setStatus(_A)
_RlAutoSmartPortSetLearntPortType_Type=TruthValue
_RlAutoSmartPortSetLearntPortType_Object=MibTableColumn
rlAutoSmartPortSetLearntPortType=_RlAutoSmartPortSetLearntPortType_Object((1,3,6,1,4,1,9,6,1,101,150,1,8,1,9),_RlAutoSmartPortSetLearntPortType_Type())
rlAutoSmartPortSetLearntPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortSetLearntPortType.setStatus(_A)
_RlAutoSmartPortParamsTable_Object=MibTable
rlAutoSmartPortParamsTable=_RlAutoSmartPortParamsTable_Object((1,3,6,1,4,1,9,6,1,101,150,1,9))
if mibBuilder.loadTexts:rlAutoSmartPortParamsTable.setStatus(_A)
_RlAutoSmartPortParamsEntry_Object=MibTableRow
rlAutoSmartPortParamsEntry=_RlAutoSmartPortParamsEntry_Object((1,3,6,1,4,1,9,6,1,101,150,1,9,1))
rlAutoSmartPortParamsEntry.setIndexNames((0,_C,_Q),(1,_C,_R))
if mibBuilder.loadTexts:rlAutoSmartPortParamsEntry.setStatus(_A)
_RlAutoSmartPortIfIndex_Type=InterfaceIndex
_RlAutoSmartPortIfIndex_Object=MibTableColumn
rlAutoSmartPortIfIndex=_RlAutoSmartPortIfIndex_Object((1,3,6,1,4,1,9,6,1,101,150,1,9,1,1),_RlAutoSmartPortIfIndex_Type())
rlAutoSmartPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortIfIndex.setStatus(_A)
_RlAutoSmartPortParamName_Type=SmartPortMacroParameterName
_RlAutoSmartPortParamName_Object=MibTableColumn
rlAutoSmartPortParamName=_RlAutoSmartPortParamName_Object((1,3,6,1,4,1,9,6,1,101,150,1,9,1,2),_RlAutoSmartPortParamName_Type())
rlAutoSmartPortParamName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortParamName.setStatus(_A)
_RlAutoSmartPortParamOrder_Type=SmartPortMacroParameterOrder
_RlAutoSmartPortParamOrder_Object=MibTableColumn
rlAutoSmartPortParamOrder=_RlAutoSmartPortParamOrder_Object((1,3,6,1,4,1,9,6,1,101,150,1,9,1,3),_RlAutoSmartPortParamOrder_Type())
rlAutoSmartPortParamOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:rlAutoSmartPortParamOrder.setStatus(_A)
_RlAutoSmartPortParamValue_Type=SmartPortMacroParameterValue
_RlAutoSmartPortParamValue_Object=MibTableColumn
rlAutoSmartPortParamValue=_RlAutoSmartPortParamValue_Object((1,3,6,1,4,1,9,6,1,101,150,1,9,1,4),_RlAutoSmartPortParamValue_Type())
rlAutoSmartPortParamValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartPortParamValue.setStatus(_A)
_RlAutoSmartTrunkRefreshTable_Object=MibTable
rlAutoSmartTrunkRefreshTable=_RlAutoSmartTrunkRefreshTable_Object((1,3,6,1,4,1,9,6,1,101,150,1,10))
if mibBuilder.loadTexts:rlAutoSmartTrunkRefreshTable.setStatus(_A)
_RlAutoSmartTrunkRefreshEntry_Object=MibTableRow
rlAutoSmartTrunkRefreshEntry=_RlAutoSmartTrunkRefreshEntry_Object((1,3,6,1,4,1,9,6,1,101,150,1,10,1))
rlAutoSmartTrunkRefreshEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:rlAutoSmartTrunkRefreshEntry.setStatus(_A)
class _RlAutoSmartTrunkRefreshSmartPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,11,12,13)));namedValues=NamedValues(*((_I,1),(_L,11),(_M,12),('ap',13)))
_RlAutoSmartTrunkRefreshSmartPortType_Type.__name__=_D
_RlAutoSmartTrunkRefreshSmartPortType_Object=MibTableColumn
rlAutoSmartTrunkRefreshSmartPortType=_RlAutoSmartTrunkRefreshSmartPortType_Object((1,3,6,1,4,1,9,6,1,101,150,1,10,1,1),_RlAutoSmartTrunkRefreshSmartPortType_Type())
rlAutoSmartTrunkRefreshSmartPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartTrunkRefreshSmartPortType.setStatus(_A)
_RlAutoSmartTrunkRefreshIfIndex_Type=InterfaceIndexOrZero
_RlAutoSmartTrunkRefreshIfIndex_Object=MibTableColumn
rlAutoSmartTrunkRefreshIfIndex=_RlAutoSmartTrunkRefreshIfIndex_Object((1,3,6,1,4,1,9,6,1,101,150,1,10,1,2),_RlAutoSmartTrunkRefreshIfIndex_Type())
rlAutoSmartTrunkRefreshIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlAutoSmartTrunkRefreshIfIndex.setStatus(_A)
_RlAutoSmartTrunkRefreshRowStatus_Type=RowStatus
_RlAutoSmartTrunkRefreshRowStatus_Object=MibTableColumn
rlAutoSmartTrunkRefreshRowStatus=_RlAutoSmartTrunkRefreshRowStatus_Object((1,3,6,1,4,1,9,6,1,101,150,1,10,1,3),_RlAutoSmartTrunkRefreshRowStatus_Type())
rlAutoSmartTrunkRefreshRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:rlAutoSmartTrunkRefreshRowStatus.setStatus(_A)
_RlAutoSmartBusy_Type=TruthValue
_RlAutoSmartBusy_Object=MibScalar
rlAutoSmartBusy=_RlAutoSmartBusy_Object((1,3,6,1,4,1,9,6,1,101,150,1,11),_RlAutoSmartBusy_Type())
rlAutoSmartBusy.setMaxAccess(_F)
if mibBuilder.loadTexts:rlAutoSmartBusy.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_K:SmartPortType,'SmartPortMacroParameterName':SmartPortMacroParameterName,'SmartPortMacroParameterValue':SmartPortMacroParameterValue,'SmartPortMacroType':SmartPortMacroType,'SmartPortMacroParameterOrder':SmartPortMacroParameterOrder,'rlAutoSmartportsMib':rlAutoSmartportsMib,'rlPortEvents':rlPortEvents,'rlAutoSmartPortAdminStatus':rlAutoSmartPortAdminStatus,'rlAutoSmartPortOperStatus':rlAutoSmartPortOperStatus,'rlAutoSmartPortLastVoiceVlanStatus':rlAutoSmartPortLastVoiceVlanStatus,'rlAutoSmartPortLastVoiceVlanId':rlAutoSmartPortLastVoiceVlanId,'rlAutoSmartPortLearningProtocols':rlAutoSmartPortLearningProtocols,'rlAutoSmartPortTypesTable':rlAutoSmartPortTypesTable,'rlAutoSmartPortTypesEntry':rlAutoSmartPortTypesEntry,_J:rlAutoSmartPortTypesType,'rlAutoSmartPortTypeStatus':rlAutoSmartPortTypeStatus,'rlAutoSmartPortMacro':rlAutoSmartPortMacro,'rlAutoSmartPortTypesRevertToDefaultMacro':rlAutoSmartPortTypesRevertToDefaultMacro,'rlAutoSmartPortTypesRevertToDefaultParams':rlAutoSmartPortTypesRevertToDefaultParams,'rlAutoSmartPortTypesBuiltinMacro':rlAutoSmartPortTypesBuiltinMacro,'rlAutoSmartPortMacrosParamTable':rlAutoSmartPortMacrosParamTable,'rlAutoSmartPortMacrosParamEntry':rlAutoSmartPortMacrosParamEntry,_N:rlAutoSmartPortMacroType,_O:rlAutoSmartPortMacrosParamName,'rlAutoSmartPortMacrosParamOrder':rlAutoSmartPortMacrosParamOrder,'rlAutoSmartPortMacrosParamValue':rlAutoSmartPortMacrosParamValue,'rlAutoSmartPortPortsTable':rlAutoSmartPortPortsTable,'rlAutoSmartPortPortsEntry':rlAutoSmartPortPortsEntry,_P:rlAutoSmartPortPort,'rlAutoSmartPortPortStatus':rlAutoSmartPortPortStatus,'rlAutoSmartPortPortType':rlAutoSmartPortPortType,'rlAutoSmartPortPersistency':rlAutoSmartPortPersistency,'rlAutoSmartPortLearntPortType':rlAutoSmartPortLearntPortType,'rlAutoSmartPortPortAcquiringType':rlAutoSmartPortPortAcquiringType,'rlAutoSmartPortLastActivatedMacro':rlAutoSmartPortLastActivatedMacro,'rlAutoSmartPortFailedCommandNumber':rlAutoSmartPortFailedCommandNumber,'rlAutoSmartPortSetLearntPortType':rlAutoSmartPortSetLearntPortType,'rlAutoSmartPortParamsTable':rlAutoSmartPortParamsTable,'rlAutoSmartPortParamsEntry':rlAutoSmartPortParamsEntry,_Q:rlAutoSmartPortIfIndex,_R:rlAutoSmartPortParamName,'rlAutoSmartPortParamOrder':rlAutoSmartPortParamOrder,'rlAutoSmartPortParamValue':rlAutoSmartPortParamValue,'rlAutoSmartTrunkRefreshTable':rlAutoSmartTrunkRefreshTable,'rlAutoSmartTrunkRefreshEntry':rlAutoSmartTrunkRefreshEntry,_S:rlAutoSmartTrunkRefreshSmartPortType,_T:rlAutoSmartTrunkRefreshIfIndex,'rlAutoSmartTrunkRefreshRowStatus':rlAutoSmartTrunkRefreshRowStatus,'rlAutoSmartBusy':rlAutoSmartBusy})