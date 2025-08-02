_L='read-only'
_K='AlarmInverseMode'
_J='raisecomAlarmMgmtId'
_I='RAISECOM-ALARM-MGMT-MIB'
_H='seconds'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='SnmpAdminString'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','iso','mib-2','zeroDotZero')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
raisecomAlarmMgmt=ModuleIdentity((1,3,6,1,4,1,8886,1,34))
class AlarmStorageMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('loop',2)))
class AlarmInverseMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('auto',2),('manual',3)))
_RaisecomAlarmMgmtObejcts_ObjectIdentity=ObjectIdentity
raisecomAlarmMgmtObejcts=_RaisecomAlarmMgmtObejcts_ObjectIdentity((1,3,6,1,4,1,8886,1,34,1))
class _RaisecomAlarmMgmtRaiseDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_RaisecomAlarmMgmtRaiseDelay_Type.__name__=_E
_RaisecomAlarmMgmtRaiseDelay_Object=MibScalar
raisecomAlarmMgmtRaiseDelay=_RaisecomAlarmMgmtRaiseDelay_Object((1,3,6,1,4,1,8886,1,34,1,1),_RaisecomAlarmMgmtRaiseDelay_Type())
raisecomAlarmMgmtRaiseDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtRaiseDelay.setStatus(_A)
if mibBuilder.loadTexts:raisecomAlarmMgmtRaiseDelay.setUnits(_H)
class _RaisecomAlarmMgmtClearDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_RaisecomAlarmMgmtClearDelay_Type.__name__=_E
_RaisecomAlarmMgmtClearDelay_Object=MibScalar
raisecomAlarmMgmtClearDelay=_RaisecomAlarmMgmtClearDelay_Object((1,3,6,1,4,1,8886,1,34,1,2),_RaisecomAlarmMgmtClearDelay_Type())
raisecomAlarmMgmtClearDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtClearDelay.setStatus(_A)
if mibBuilder.loadTexts:raisecomAlarmMgmtClearDelay.setUnits(_H)
_RaisecomAlarmMgmtActiveStoreMode_Type=AlarmStorageMode
_RaisecomAlarmMgmtActiveStoreMode_Object=MibScalar
raisecomAlarmMgmtActiveStoreMode=_RaisecomAlarmMgmtActiveStoreMode_Object((1,3,6,1,4,1,8886,1,34,1,3),_RaisecomAlarmMgmtActiveStoreMode_Type())
raisecomAlarmMgmtActiveStoreMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtActiveStoreMode.setStatus(_A)
class _RaisecomAlarmMgmtInhibitEnable_Type(TruthValue):defaultValue=1
_RaisecomAlarmMgmtInhibitEnable_Type.__name__=_C
_RaisecomAlarmMgmtInhibitEnable_Object=MibScalar
raisecomAlarmMgmtInhibitEnable=_RaisecomAlarmMgmtInhibitEnable_Object((1,3,6,1,4,1,8886,1,34,1,4),_RaisecomAlarmMgmtInhibitEnable_Type())
raisecomAlarmMgmtInhibitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtInhibitEnable.setStatus(_A)
class _RaisecomAlarmMgmtSyslogEnable_Type(TruthValue):defaultValue=1
_RaisecomAlarmMgmtSyslogEnable_Type.__name__=_C
_RaisecomAlarmMgmtSyslogEnable_Object=MibScalar
raisecomAlarmMgmtSyslogEnable=_RaisecomAlarmMgmtSyslogEnable_Object((1,3,6,1,4,1,8886,1,34,1,5),_RaisecomAlarmMgmtSyslogEnable_Type())
raisecomAlarmMgmtSyslogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtSyslogEnable.setStatus(_A)
_RaisecomAlarmMgmtActiveClear_Type=Integer32
_RaisecomAlarmMgmtActiveClear_Object=MibScalar
raisecomAlarmMgmtActiveClear=_RaisecomAlarmMgmtActiveClear_Object((1,3,6,1,4,1,8886,1,34,1,6),_RaisecomAlarmMgmtActiveClear_Type())
raisecomAlarmMgmtActiveClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtActiveClear.setStatus(_A)
_RaisecomAlarmMgmtConfigTable_Object=MibTable
raisecomAlarmMgmtConfigTable=_RaisecomAlarmMgmtConfigTable_Object((1,3,6,1,4,1,8886,1,34,1,7))
if mibBuilder.loadTexts:raisecomAlarmMgmtConfigTable.setStatus(_A)
_RaisecomAlarmMgmtConfigEntry_Object=MibTableRow
raisecomAlarmMgmtConfigEntry=_RaisecomAlarmMgmtConfigEntry_Object((1,3,6,1,4,1,8886,1,34,1,7,1))
raisecomAlarmMgmtConfigEntry.setIndexNames((0,_I,_J),(0,_F,_G))
if mibBuilder.loadTexts:raisecomAlarmMgmtConfigEntry.setStatus(_A)
_RaisecomAlarmMgmtId_Type=Unsigned32
_RaisecomAlarmMgmtId_Object=MibTableColumn
raisecomAlarmMgmtId=_RaisecomAlarmMgmtId_Object((1,3,6,1,4,1,8886,1,34,1,7,1,1),_RaisecomAlarmMgmtId_Type())
raisecomAlarmMgmtId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:raisecomAlarmMgmtId.setStatus(_A)
class _RaisecomAlarmMgmtClear_Type(TruthValue):defaultValue=2
_RaisecomAlarmMgmtClear_Type.__name__=_C
_RaisecomAlarmMgmtClear_Object=MibTableColumn
raisecomAlarmMgmtClear=_RaisecomAlarmMgmtClear_Object((1,3,6,1,4,1,8886,1,34,1,7,1,2),_RaisecomAlarmMgmtClear_Type())
raisecomAlarmMgmtClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtClear.setStatus(_A)
class _RaisecomAlarmMgmtReportEnable_Type(TruthValue):defaultValue=1
_RaisecomAlarmMgmtReportEnable_Type.__name__=_C
_RaisecomAlarmMgmtReportEnable_Object=MibTableColumn
raisecomAlarmMgmtReportEnable=_RaisecomAlarmMgmtReportEnable_Object((1,3,6,1,4,1,8886,1,34,1,7,1,3),_RaisecomAlarmMgmtReportEnable_Type())
raisecomAlarmMgmtReportEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtReportEnable.setStatus(_A)
class _RaisecomAlarmMgmtMonitorEnable_Type(TruthValue):defaultValue=1
_RaisecomAlarmMgmtMonitorEnable_Type.__name__=_C
_RaisecomAlarmMgmtMonitorEnable_Object=MibTableColumn
raisecomAlarmMgmtMonitorEnable=_RaisecomAlarmMgmtMonitorEnable_Object((1,3,6,1,4,1,8886,1,34,1,7,1,4),_RaisecomAlarmMgmtMonitorEnable_Type())
raisecomAlarmMgmtMonitorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtMonitorEnable.setStatus(_A)
class _RaisecomAlarmMgmtInverseMode_Type(AlarmInverseMode):defaultValue=1
_RaisecomAlarmMgmtInverseMode_Type.__name__=_K
_RaisecomAlarmMgmtInverseMode_Object=MibTableColumn
raisecomAlarmMgmtInverseMode=_RaisecomAlarmMgmtInverseMode_Object((1,3,6,1,4,1,8886,1,34,1,7,1,5),_RaisecomAlarmMgmtInverseMode_Type())
raisecomAlarmMgmtInverseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomAlarmMgmtInverseMode.setStatus(_A)
class _RaisecomAlarmMgmtModuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RaisecomAlarmMgmtModuleName_Type.__name__=_D
_RaisecomAlarmMgmtModuleName_Object=MibTableColumn
raisecomAlarmMgmtModuleName=_RaisecomAlarmMgmtModuleName_Object((1,3,6,1,4,1,8886,1,34,1,7,1,6),_RaisecomAlarmMgmtModuleName_Type())
raisecomAlarmMgmtModuleName.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomAlarmMgmtModuleName.setStatus(_A)
class _RaisecomAlarmMgmtGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RaisecomAlarmMgmtGroupName_Type.__name__=_D
_RaisecomAlarmMgmtGroupName_Object=MibTableColumn
raisecomAlarmMgmtGroupName=_RaisecomAlarmMgmtGroupName_Object((1,3,6,1,4,1,8886,1,34,1,7,1,7),_RaisecomAlarmMgmtGroupName_Type())
raisecomAlarmMgmtGroupName.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomAlarmMgmtGroupName.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'AlarmStorageMode':AlarmStorageMode,_K:AlarmInverseMode,'raisecomAlarmMgmt':raisecomAlarmMgmt,'raisecomAlarmMgmtObejcts':raisecomAlarmMgmtObejcts,'raisecomAlarmMgmtRaiseDelay':raisecomAlarmMgmtRaiseDelay,'raisecomAlarmMgmtClearDelay':raisecomAlarmMgmtClearDelay,'raisecomAlarmMgmtActiveStoreMode':raisecomAlarmMgmtActiveStoreMode,'raisecomAlarmMgmtInhibitEnable':raisecomAlarmMgmtInhibitEnable,'raisecomAlarmMgmtSyslogEnable':raisecomAlarmMgmtSyslogEnable,'raisecomAlarmMgmtActiveClear':raisecomAlarmMgmtActiveClear,'raisecomAlarmMgmtConfigTable':raisecomAlarmMgmtConfigTable,'raisecomAlarmMgmtConfigEntry':raisecomAlarmMgmtConfigEntry,_J:raisecomAlarmMgmtId,'raisecomAlarmMgmtClear':raisecomAlarmMgmtClear,'raisecomAlarmMgmtReportEnable':raisecomAlarmMgmtReportEnable,'raisecomAlarmMgmtMonitorEnable':raisecomAlarmMgmtMonitorEnable,'raisecomAlarmMgmtInverseMode':raisecomAlarmMgmtInverseMode,'raisecomAlarmMgmtModuleName':raisecomAlarmMgmtModuleName,'raisecomAlarmMgmtGroupName':raisecomAlarmMgmtGroupName})