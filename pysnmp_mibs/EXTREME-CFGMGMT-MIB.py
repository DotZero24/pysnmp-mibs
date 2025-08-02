_P='read-write'
_O='extremeLastChangeCfgSlotId'
_N='remoteDevice'
_M='extremeLastSaveConfigSlotId'
_L='extremeLastChangeConfigSource'
_K='extremeLastChangeConfigFileName'
_J='extremeLastChangeConfigTime'
_I='extremeLastSaveConfigSource'
_H='extremeLastSaveConfigFileName'
_G='extremeLastSaveConfigTime'
_F='TruthValue'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='EXTREME-CFGMGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','PortList','extremeAgent')
ifDescr,=mibBuilder.importSymbols('IF-MIB','ifDescr')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols('SNMPv2-MIB','sysDescr','sysUpTime')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention',_F)
extremeCfgMgmt=ModuleIdentity((1,3,6,1,4,1,1916,1,42))
if mibBuilder.loadTexts:extremeCfgMgmt.setRevisions(('2017-09-12 00:00',))
_ExtremeCfgMgmtCommon_ObjectIdentity=ObjectIdentity
extremeCfgMgmtCommon=_ExtremeCfgMgmtCommon_ObjectIdentity((1,3,6,1,4,1,1916,1,42,1))
_ExtremeLastSaveCfgTable_Object=MibTable
extremeLastSaveCfgTable=_ExtremeLastSaveCfgTable_Object((1,3,6,1,4,1,1916,1,42,1,1))
if mibBuilder.loadTexts:extremeLastSaveCfgTable.setStatus(_A)
_ExtremeLastSavedEntry_Object=MibTableRow
extremeLastSavedEntry=_ExtremeLastSavedEntry_Object((1,3,6,1,4,1,1916,1,42,1,1,1))
extremeLastSavedEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:extremeLastSavedEntry.setStatus(_A)
class _ExtremeLastSaveConfigSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeLastSaveConfigSlotId_Type.__name__=_D
_ExtremeLastSaveConfigSlotId_Object=MibTableColumn
extremeLastSaveConfigSlotId=_ExtremeLastSaveConfigSlotId_Object((1,3,6,1,4,1,1916,1,42,1,1,1,1),_ExtremeLastSaveConfigSlotId_Type())
extremeLastSaveConfigSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastSaveConfigSlotId.setStatus(_A)
class _ExtremeLastSaveConfigTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeLastSaveConfigTime_Type.__name__=_E
_ExtremeLastSaveConfigTime_Object=MibTableColumn
extremeLastSaveConfigTime=_ExtremeLastSaveConfigTime_Object((1,3,6,1,4,1,1916,1,42,1,1,1,2),_ExtremeLastSaveConfigTime_Type())
extremeLastSaveConfigTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastSaveConfigTime.setStatus(_A)
class _ExtremeLastSaveConfigFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ExtremeLastSaveConfigFileName_Type.__name__=_E
_ExtremeLastSaveConfigFileName_Object=MibTableColumn
extremeLastSaveConfigFileName=_ExtremeLastSaveConfigFileName_Object((1,3,6,1,4,1,1916,1,42,1,1,1,3),_ExtremeLastSaveConfigFileName_Type())
extremeLastSaveConfigFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastSaveConfigFileName.setStatus(_A)
class _ExtremeLastSaveConfigSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmp',1),(_N,2),('none',3)))
_ExtremeLastSaveConfigSource_Type.__name__=_D
_ExtremeLastSaveConfigSource_Object=MibTableColumn
extremeLastSaveConfigSource=_ExtremeLastSaveConfigSource_Object((1,3,6,1,4,1,1916,1,42,1,1,1,4),_ExtremeLastSaveConfigSource_Type())
extremeLastSaveConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastSaveConfigSource.setStatus(_A)
_ExtremeLastChangeCfgTable_Object=MibTable
extremeLastChangeCfgTable=_ExtremeLastChangeCfgTable_Object((1,3,6,1,4,1,1916,1,42,1,2))
if mibBuilder.loadTexts:extremeLastChangeCfgTable.setStatus(_A)
_ExtremeLastChangeCfgEntry_Object=MibTableRow
extremeLastChangeCfgEntry=_ExtremeLastChangeCfgEntry_Object((1,3,6,1,4,1,1916,1,42,1,2,1))
extremeLastChangeCfgEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:extremeLastChangeCfgEntry.setStatus(_A)
class _ExtremeLastChangeCfgSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeLastChangeCfgSlotId_Type.__name__=_D
_ExtremeLastChangeCfgSlotId_Object=MibTableColumn
extremeLastChangeCfgSlotId=_ExtremeLastChangeCfgSlotId_Object((1,3,6,1,4,1,1916,1,42,1,2,1,1),_ExtremeLastChangeCfgSlotId_Type())
extremeLastChangeCfgSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastChangeCfgSlotId.setStatus(_A)
class _ExtremeLastChangeConfigTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeLastChangeConfigTime_Type.__name__=_E
_ExtremeLastChangeConfigTime_Object=MibTableColumn
extremeLastChangeConfigTime=_ExtremeLastChangeConfigTime_Object((1,3,6,1,4,1,1916,1,42,1,2,1,2),_ExtremeLastChangeConfigTime_Type())
extremeLastChangeConfigTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastChangeConfigTime.setStatus(_A)
class _ExtremeLastChangeConfigFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ExtremeLastChangeConfigFileName_Type.__name__=_E
_ExtremeLastChangeConfigFileName_Object=MibTableColumn
extremeLastChangeConfigFileName=_ExtremeLastChangeConfigFileName_Object((1,3,6,1,4,1,1916,1,42,1,2,1,3),_ExtremeLastChangeConfigFileName_Type())
extremeLastChangeConfigFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastChangeConfigFileName.setStatus(_A)
class _ExtremeLastChangeConfigSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmp',1),(_N,2),('none',3)))
_ExtremeLastChangeConfigSource_Type.__name__=_D
_ExtremeLastChangeConfigSource_Object=MibTableColumn
extremeLastChangeConfigSource=_ExtremeLastChangeConfigSource_Object((1,3,6,1,4,1,1916,1,42,1,2,1,4),_ExtremeLastChangeConfigSource_Type())
extremeLastChangeConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeLastChangeConfigSource.setStatus(_A)
_ExtremeCfgGroups_ObjectIdentity=ObjectIdentity
extremeCfgGroups=_ExtremeCfgGroups_ObjectIdentity((1,3,6,1,4,1,1916,1,42,9))
_ExtremeCfgMgmtTrapPrefix_ObjectIdentity=ObjectIdentity
extremeCfgMgmtTrapPrefix=_ExtremeCfgMgmtTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,42,10))
_CfgMgmtTraps_ObjectIdentity=ObjectIdentity
cfgMgmtTraps=_CfgMgmtTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,42,10,0))
_CfgMgmtControl_ObjectIdentity=ObjectIdentity
cfgMgmtControl=_CfgMgmtControl_ObjectIdentity((1,3,6,1,4,1,1916,1,42,11))
class _CfgMgmtConfigSaveTrapEnable_Type(TruthValue):defaultValue=2
_CfgMgmtConfigSaveTrapEnable_Type.__name__=_F
_CfgMgmtConfigSaveTrapEnable_Object=MibScalar
cfgMgmtConfigSaveTrapEnable=_CfgMgmtConfigSaveTrapEnable_Object((1,3,6,1,4,1,1916,1,42,11,1),_CfgMgmtConfigSaveTrapEnable_Type())
cfgMgmtConfigSaveTrapEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:cfgMgmtConfigSaveTrapEnable.setStatus(_A)
class _CfgMgmtConfigChangeTrapEnable_Type(TruthValue):defaultValue=2
_CfgMgmtConfigChangeTrapEnable_Type.__name__=_F
_CfgMgmtConfigChangeTrapEnable_Object=MibScalar
cfgMgmtConfigChangeTrapEnable=_CfgMgmtConfigChangeTrapEnable_Object((1,3,6,1,4,1,1916,1,42,11,2),_CfgMgmtConfigChangeTrapEnable_Type())
cfgMgmtConfigChangeTrapEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:cfgMgmtConfigChangeTrapEnable.setStatus(_A)
extremeRunningLastSavedCfgGroup=ObjectGroup((1,3,6,1,4,1,1916,1,42,9,1))
extremeRunningLastSavedCfgGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:extremeRunningLastSavedCfgGroup.setStatus(_A)
extremeRunningLastChangeCfgGroup=ObjectGroup((1,3,6,1,4,1,1916,1,42,9,2))
extremeRunningLastChangeCfgGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:extremeRunningLastChangeCfgGroup.setStatus(_A)
cfgMgmtConfigSaveTrap=NotificationType((1,3,6,1,4,1,1916,1,42,10,0,1))
cfgMgmtConfigSaveTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cfgMgmtConfigSaveTrap.setStatus(_A)
cfgMgmtConfigChangeTrap=NotificationType((1,3,6,1,4,1,1916,1,42,10,0,2))
cfgMgmtConfigChangeTrap.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cfgMgmtConfigChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeCfgMgmt':extremeCfgMgmt,'extremeCfgMgmtCommon':extremeCfgMgmtCommon,'extremeLastSaveCfgTable':extremeLastSaveCfgTable,'extremeLastSavedEntry':extremeLastSavedEntry,_M:extremeLastSaveConfigSlotId,_G:extremeLastSaveConfigTime,_H:extremeLastSaveConfigFileName,_I:extremeLastSaveConfigSource,'extremeLastChangeCfgTable':extremeLastChangeCfgTable,'extremeLastChangeCfgEntry':extremeLastChangeCfgEntry,_O:extremeLastChangeCfgSlotId,_J:extremeLastChangeConfigTime,_K:extremeLastChangeConfigFileName,_L:extremeLastChangeConfigSource,'extremeCfgGroups':extremeCfgGroups,'extremeRunningLastSavedCfgGroup':extremeRunningLastSavedCfgGroup,'extremeRunningLastChangeCfgGroup':extremeRunningLastChangeCfgGroup,'extremeCfgMgmtTrapPrefix':extremeCfgMgmtTrapPrefix,'cfgMgmtTraps':cfgMgmtTraps,'cfgMgmtConfigSaveTrap':cfgMgmtConfigSaveTrap,'cfgMgmtConfigChangeTrap':cfgMgmtConfigChangeTrap,'cfgMgmtControl':cfgMgmtControl,'cfgMgmtConfigSaveTrapEnable':cfgMgmtConfigSaveTrapEnable,'cfgMgmtConfigChangeTrapEnable':cfgMgmtConfigChangeTrapEnable})