_K='slAlsOperStatus'
_J='SL-ALS-MIB'
_I='activate'
_H='ms2250'
_G='ms2000'
_F='ms1750'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
slAlsMib=ModuleIdentity((1,3,6,1,4,1,4515,1,12))
class AlsManualPulseTimeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
class AlsAutomaticPulseTimeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SlAlsConfig_ObjectIdentity=ObjectIdentity
slAlsConfig=_SlAlsConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,12,1))
_SlAlsConfigTable_Object=MibTable
slAlsConfigTable=_SlAlsConfigTable_Object((1,3,6,1,4,1,4515,1,12,1,1))
if mibBuilder.loadTexts:slAlsConfigTable.setStatus(_A)
_SlAlsConfigEntry_Object=MibTableRow
slAlsConfigEntry=_SlAlsConfigEntry_Object((1,3,6,1,4,1,4515,1,12,1,1,1))
slAlsConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slAlsConfigEntry.setStatus(_A)
class _SlAlsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SlAlsMode_Type.__name__=_B
_SlAlsMode_Object=MibTableColumn
slAlsMode=_SlAlsMode_Object((1,3,6,1,4,1,4515,1,12,1,1,1,1),_SlAlsMode_Type())
slAlsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsMode.setStatus(_A)
class _SlAlsLosDeclareTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ms500',1),('ms550',2),('ms600',3)))
_SlAlsLosDeclareTime_Type.__name__=_B
_SlAlsLosDeclareTime_Object=MibTableColumn
slAlsLosDeclareTime=_SlAlsLosDeclareTime_Object((1,3,6,1,4,1,4515,1,12,1,1,1,2),_SlAlsLosDeclareTime_Type())
slAlsLosDeclareTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsLosDeclareTime.setStatus(_A)
class _SlAlsTestPulseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('s80',1),('s90',2),('s100',3)))
_SlAlsTestPulseTime_Type.__name__=_B
_SlAlsTestPulseTime_Object=MibTableColumn
slAlsTestPulseTime=_SlAlsTestPulseTime_Object((1,3,6,1,4,1,4515,1,12,1,1,1,3),_SlAlsTestPulseTime_Type())
slAlsTestPulseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsTestPulseTime.setStatus(_A)
_SlAlsManualPulseTime_Type=Integer32
_SlAlsManualPulseTime_Object=MibTableColumn
slAlsManualPulseTime=_SlAlsManualPulseTime_Object((1,3,6,1,4,1,4515,1,12,1,1,1,4),_SlAlsManualPulseTime_Type())
slAlsManualPulseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsManualPulseTime.setStatus(_A)
_SlAlsAutomaticPulseTime_Type=Integer32
_SlAlsAutomaticPulseTime_Object=MibTableColumn
slAlsAutomaticPulseTime=_SlAlsAutomaticPulseTime_Object((1,3,6,1,4,1,4515,1,12,1,1,1,5),_SlAlsAutomaticPulseTime_Type())
slAlsAutomaticPulseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsAutomaticPulseTime.setStatus(_A)
class _SlAlsAutomaticDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_SlAlsAutomaticDelayTime_Type.__name__=_B
_SlAlsAutomaticDelayTime_Object=MibTableColumn
slAlsAutomaticDelayTime=_SlAlsAutomaticDelayTime_Object((1,3,6,1,4,1,4515,1,12,1,1,1,6),_SlAlsAutomaticDelayTime_Type())
slAlsAutomaticDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsAutomaticDelayTime.setStatus(_A)
class _SlAlsLaserTestActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_SlAlsLaserTestActivate_Type.__name__=_B
_SlAlsLaserTestActivate_Object=MibTableColumn
slAlsLaserTestActivate=_SlAlsLaserTestActivate_Object((1,3,6,1,4,1,4515,1,12,1,1,1,7),_SlAlsLaserTestActivate_Type())
slAlsLaserTestActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsLaserTestActivate.setStatus(_A)
class _SlAlsLaserManualActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_SlAlsLaserManualActivate_Type.__name__=_B
_SlAlsLaserManualActivate_Object=MibTableColumn
slAlsLaserManualActivate=_SlAlsLaserManualActivate_Object((1,3,6,1,4,1,4515,1,12,1,1,1,8),_SlAlsLaserManualActivate_Type())
slAlsLaserManualActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsLaserManualActivate.setStatus(_A)
class _SlAlsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_SlAlsOperStatus_Type.__name__=_B
_SlAlsOperStatus_Object=MibTableColumn
slAlsOperStatus=_SlAlsOperStatus_Object((1,3,6,1,4,1,4515,1,12,1,1,1,9),_SlAlsOperStatus_Type())
slAlsOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:slAlsOperStatus.setStatus(_A)
class _SlAlsResetParams_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('resetCounters',1))
_SlAlsResetParams_Type.__name__=_B
_SlAlsResetParams_Object=MibTableColumn
slAlsResetParams=_SlAlsResetParams_Object((1,3,6,1,4,1,4515,1,12,1,1,1,10),_SlAlsResetParams_Type())
slAlsResetParams.setMaxAccess(_C)
if mibBuilder.loadTexts:slAlsResetParams.setStatus(_A)
_SlAlsTraps_ObjectIdentity=ObjectIdentity
slAlsTraps=_SlAlsTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,12,2))
slAlsStatusChangeTrap=NotificationType((1,3,6,1,4,1,4515,1,12,2,1))
slAlsStatusChangeTrap.setObjects(*((_D,_E),(_J,_K)))
if mibBuilder.loadTexts:slAlsStatusChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'AlsManualPulseTimeType':AlsManualPulseTimeType,'AlsAutomaticPulseTimeType':AlsAutomaticPulseTimeType,'slAlsMib':slAlsMib,'slAlsConfig':slAlsConfig,'slAlsConfigTable':slAlsConfigTable,'slAlsConfigEntry':slAlsConfigEntry,'slAlsMode':slAlsMode,'slAlsLosDeclareTime':slAlsLosDeclareTime,'slAlsTestPulseTime':slAlsTestPulseTime,'slAlsManualPulseTime':slAlsManualPulseTime,'slAlsAutomaticPulseTime':slAlsAutomaticPulseTime,'slAlsAutomaticDelayTime':slAlsAutomaticDelayTime,'slAlsLaserTestActivate':slAlsLaserTestActivate,'slAlsLaserManualActivate':slAlsLaserManualActivate,_K:slAlsOperStatus,'slAlsResetParams':slAlsResetParams,'slAlsTraps':slAlsTraps,'slAlsStatusChangeTrap':slAlsStatusChangeTrap})