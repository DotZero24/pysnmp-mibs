_N='eltMesIssPoePortUtilIfIndex'
_M='eltMesIssPoePortUtilGroupIndex'
_L='eltMesIssPoePortConfigIfIndex'
_K='eltMesIssPoePortConfigGroupIndex'
_J='eltMesIssPoeStatGroupIndex'
_I='EltMesIssPoeInrushTestStatus'
_H='eltMesIssPoeGlobalConfigGroupIndex'
_G='TruthValue'
_F='read-write'
_E='read-only'
_D='not-accessible'
_C='ELTEX-MES-ISS-POE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
eltMesIssPoeMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,11))
if mibBuilder.loadTexts:eltMesIssPoeMIB.setRevisions(('2022-07-27 00:00','2019-07-12 00:00','2019-04-02 00:00'))
class EltMesIssPoeInrushTestStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_EltMesIssPoeNotifications_ObjectIdentity=ObjectIdentity
eltMesIssPoeNotifications=_EltMesIssPoeNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,11,0))
_EltMesIssPoeObjects_ObjectIdentity=ObjectIdentity
eltMesIssPoeObjects=_EltMesIssPoeObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,11,1))
_EltMesIssPoeGlobals_ObjectIdentity=ObjectIdentity
eltMesIssPoeGlobals=_EltMesIssPoeGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,11,1,1))
_EltMesIssPoeGlobalConfigTable_Object=MibTable
eltMesIssPoeGlobalConfigTable=_EltMesIssPoeGlobalConfigTable_Object((1,3,6,1,4,1,35265,1,139,11,1,1,1))
if mibBuilder.loadTexts:eltMesIssPoeGlobalConfigTable.setStatus(_A)
_EltMesIssPoeGlobalConfigEntry_Object=MibTableRow
eltMesIssPoeGlobalConfigEntry=_EltMesIssPoeGlobalConfigEntry_Object((1,3,6,1,4,1,35265,1,139,11,1,1,1,1))
eltMesIssPoeGlobalConfigEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:eltMesIssPoeGlobalConfigEntry.setStatus(_A)
class _EltMesIssPoeGlobalConfigGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssPoeGlobalConfigGroupIndex_Type.__name__=_B
_EltMesIssPoeGlobalConfigGroupIndex_Object=MibTableColumn
eltMesIssPoeGlobalConfigGroupIndex=_EltMesIssPoeGlobalConfigGroupIndex_Object((1,3,6,1,4,1,35265,1,139,11,1,1,1,1,1),_EltMesIssPoeGlobalConfigGroupIndex_Type())
eltMesIssPoeGlobalConfigGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPoeGlobalConfigGroupIndex.setStatus(_A)
class _EltMesIssPoeInrushTest_Type(EltMesIssPoeInrushTestStatus):defaultValue=1
_EltMesIssPoeInrushTest_Type.__name__=_I
_EltMesIssPoeInrushTest_Object=MibTableColumn
eltMesIssPoeInrushTest=_EltMesIssPoeInrushTest_Object((1,3,6,1,4,1,35265,1,139,11,1,1,1,1,2),_EltMesIssPoeInrushTest_Type())
eltMesIssPoeInrushTest.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssPoeInrushTest.setStatus(_A)
class _EltMesIssPoeAutoRestart_Type(TruthValue):defaultValue=1
_EltMesIssPoeAutoRestart_Type.__name__=_G
_EltMesIssPoeAutoRestart_Object=MibScalar
eltMesIssPoeAutoRestart=_EltMesIssPoeAutoRestart_Object((1,3,6,1,4,1,35265,1,139,11,1,1,2),_EltMesIssPoeAutoRestart_Type())
eltMesIssPoeAutoRestart.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssPoeAutoRestart.setStatus(_A)
_EltMesIssPoeRestartAction_Type=TruthValue
_EltMesIssPoeRestartAction_Object=MibScalar
eltMesIssPoeRestartAction=_EltMesIssPoeRestartAction_Object((1,3,6,1,4,1,35265,1,139,11,1,1,3),_EltMesIssPoeRestartAction_Type())
eltMesIssPoeRestartAction.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssPoeRestartAction.setStatus(_A)
_EltMesIssPoeStatistics_ObjectIdentity=ObjectIdentity
eltMesIssPoeStatistics=_EltMesIssPoeStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,139,11,1,2))
_EltMesIssPoeStatTable_Object=MibTable
eltMesIssPoeStatTable=_EltMesIssPoeStatTable_Object((1,3,6,1,4,1,35265,1,139,11,1,2,1))
if mibBuilder.loadTexts:eltMesIssPoeStatTable.setStatus(_A)
_EltMesIssPoeStatEntry_Object=MibTableRow
eltMesIssPoeStatEntry=_EltMesIssPoeStatEntry_Object((1,3,6,1,4,1,35265,1,139,11,1,2,1,1))
eltMesIssPoeStatEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:eltMesIssPoeStatEntry.setStatus(_A)
class _EltMesIssPoeStatGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssPoeStatGroupIndex_Type.__name__=_B
_EltMesIssPoeStatGroupIndex_Object=MibTableColumn
eltMesIssPoeStatGroupIndex=_EltMesIssPoeStatGroupIndex_Object((1,3,6,1,4,1,35265,1,139,11,1,2,1,1,1),_EltMesIssPoeStatGroupIndex_Type())
eltMesIssPoeStatGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPoeStatGroupIndex.setStatus(_A)
_EltMesIssPoeTemperature_Type=Integer32
_EltMesIssPoeTemperature_Object=MibTableColumn
eltMesIssPoeTemperature=_EltMesIssPoeTemperature_Object((1,3,6,1,4,1,35265,1,139,11,1,2,1,1,2),_EltMesIssPoeTemperature_Type())
eltMesIssPoeTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssPoeTemperature.setStatus(_A)
_EltMesIssPoePortConfig_ObjectIdentity=ObjectIdentity
eltMesIssPoePortConfig=_EltMesIssPoePortConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,11,1,3))
_EltMesIssPoePortConfigTable_Object=MibTable
eltMesIssPoePortConfigTable=_EltMesIssPoePortConfigTable_Object((1,3,6,1,4,1,35265,1,139,11,1,3,1))
if mibBuilder.loadTexts:eltMesIssPoePortConfigTable.setStatus(_A)
_EltMesIssPoePortConfigEntry_Object=MibTableRow
eltMesIssPoePortConfigEntry=_EltMesIssPoePortConfigEntry_Object((1,3,6,1,4,1,35265,1,139,11,1,3,1,1))
eltMesIssPoePortConfigEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:eltMesIssPoePortConfigEntry.setStatus(_A)
class _EltMesIssPoePortConfigGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssPoePortConfigGroupIndex_Type.__name__=_B
_EltMesIssPoePortConfigGroupIndex_Object=MibTableColumn
eltMesIssPoePortConfigGroupIndex=_EltMesIssPoePortConfigGroupIndex_Object((1,3,6,1,4,1,35265,1,139,11,1,3,1,1,1),_EltMesIssPoePortConfigGroupIndex_Type())
eltMesIssPoePortConfigGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPoePortConfigGroupIndex.setStatus(_A)
class _EltMesIssPoePortConfigIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssPoePortConfigIfIndex_Type.__name__=_B
_EltMesIssPoePortConfigIfIndex_Object=MibTableColumn
eltMesIssPoePortConfigIfIndex=_EltMesIssPoePortConfigIfIndex_Object((1,3,6,1,4,1,35265,1,139,11,1,3,1,1,2),_EltMesIssPoePortConfigIfIndex_Type())
eltMesIssPoePortConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPoePortConfigIfIndex.setStatus(_A)
class _EltMesIssPoePortMaxPowerLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31200))
_EltMesIssPoePortMaxPowerLimit_Type.__name__=_B
_EltMesIssPoePortMaxPowerLimit_Object=MibTableColumn
eltMesIssPoePortMaxPowerLimit=_EltMesIssPoePortMaxPowerLimit_Object((1,3,6,1,4,1,35265,1,139,11,1,3,1,1,3),_EltMesIssPoePortMaxPowerLimit_Type())
eltMesIssPoePortMaxPowerLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssPoePortMaxPowerLimit.setStatus(_A)
_EltMesIssPoePortStatistics_ObjectIdentity=ObjectIdentity
eltMesIssPoePortStatistics=_EltMesIssPoePortStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,139,11,1,4))
_EltMesIssPoePortUtilTable_Object=MibTable
eltMesIssPoePortUtilTable=_EltMesIssPoePortUtilTable_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1))
if mibBuilder.loadTexts:eltMesIssPoePortUtilTable.setStatus(_A)
_EltMesIssPoePortUtilEntry_Object=MibTableRow
eltMesIssPoePortUtilEntry=_EltMesIssPoePortUtilEntry_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1))
eltMesIssPoePortUtilEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:eltMesIssPoePortUtilEntry.setStatus(_A)
class _EltMesIssPoePortUtilGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssPoePortUtilGroupIndex_Type.__name__=_B
_EltMesIssPoePortUtilGroupIndex_Object=MibTableColumn
eltMesIssPoePortUtilGroupIndex=_EltMesIssPoePortUtilGroupIndex_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1,1),_EltMesIssPoePortUtilGroupIndex_Type())
eltMesIssPoePortUtilGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPoePortUtilGroupIndex.setStatus(_A)
class _EltMesIssPoePortUtilIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssPoePortUtilIfIndex_Type.__name__=_B
_EltMesIssPoePortUtilIfIndex_Object=MibTableColumn
eltMesIssPoePortUtilIfIndex=_EltMesIssPoePortUtilIfIndex_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1,2),_EltMesIssPoePortUtilIfIndex_Type())
eltMesIssPoePortUtilIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPoePortUtilIfIndex.setStatus(_A)
_EltMesIssPoePortUtilOutputVoltage_Type=Integer32
_EltMesIssPoePortUtilOutputVoltage_Object=MibTableColumn
eltMesIssPoePortUtilOutputVoltage=_EltMesIssPoePortUtilOutputVoltage_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1,3),_EltMesIssPoePortUtilOutputVoltage_Type())
eltMesIssPoePortUtilOutputVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssPoePortUtilOutputVoltage.setStatus(_A)
_EltMesIssPoePortUtilOutputCurrent_Type=Integer32
_EltMesIssPoePortUtilOutputCurrent_Object=MibTableColumn
eltMesIssPoePortUtilOutputCurrent=_EltMesIssPoePortUtilOutputCurrent_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1,4),_EltMesIssPoePortUtilOutputCurrent_Type())
eltMesIssPoePortUtilOutputCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssPoePortUtilOutputCurrent.setStatus(_A)
_EltMesIssPoePortUtilOutputPower_Type=Integer32
_EltMesIssPoePortUtilOutputPower_Object=MibTableColumn
eltMesIssPoePortUtilOutputPower=_EltMesIssPoePortUtilOutputPower_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1,5),_EltMesIssPoePortUtilOutputPower_Type())
eltMesIssPoePortUtilOutputPower.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssPoePortUtilOutputPower.setStatus(_A)
_EltMesIssPoePortUtilMaxPower_Type=Integer32
_EltMesIssPoePortUtilMaxPower_Object=MibTableColumn
eltMesIssPoePortUtilMaxPower=_EltMesIssPoePortUtilMaxPower_Object((1,3,6,1,4,1,35265,1,139,11,1,4,1,1,6),_EltMesIssPoePortUtilMaxPower_Type())
eltMesIssPoePortUtilMaxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:eltMesIssPoePortUtilMaxPower.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_I:EltMesIssPoeInrushTestStatus,'eltMesIssPoeMIB':eltMesIssPoeMIB,'eltMesIssPoeNotifications':eltMesIssPoeNotifications,'eltMesIssPoeObjects':eltMesIssPoeObjects,'eltMesIssPoeGlobals':eltMesIssPoeGlobals,'eltMesIssPoeGlobalConfigTable':eltMesIssPoeGlobalConfigTable,'eltMesIssPoeGlobalConfigEntry':eltMesIssPoeGlobalConfigEntry,_H:eltMesIssPoeGlobalConfigGroupIndex,'eltMesIssPoeInrushTest':eltMesIssPoeInrushTest,'eltMesIssPoeAutoRestart':eltMesIssPoeAutoRestart,'eltMesIssPoeRestartAction':eltMesIssPoeRestartAction,'eltMesIssPoeStatistics':eltMesIssPoeStatistics,'eltMesIssPoeStatTable':eltMesIssPoeStatTable,'eltMesIssPoeStatEntry':eltMesIssPoeStatEntry,_J:eltMesIssPoeStatGroupIndex,'eltMesIssPoeTemperature':eltMesIssPoeTemperature,'eltMesIssPoePortConfig':eltMesIssPoePortConfig,'eltMesIssPoePortConfigTable':eltMesIssPoePortConfigTable,'eltMesIssPoePortConfigEntry':eltMesIssPoePortConfigEntry,_K:eltMesIssPoePortConfigGroupIndex,_L:eltMesIssPoePortConfigIfIndex,'eltMesIssPoePortMaxPowerLimit':eltMesIssPoePortMaxPowerLimit,'eltMesIssPoePortStatistics':eltMesIssPoePortStatistics,'eltMesIssPoePortUtilTable':eltMesIssPoePortUtilTable,'eltMesIssPoePortUtilEntry':eltMesIssPoePortUtilEntry,_M:eltMesIssPoePortUtilGroupIndex,_N:eltMesIssPoePortUtilIfIndex,'eltMesIssPoePortUtilOutputVoltage':eltMesIssPoePortUtilOutputVoltage,'eltMesIssPoePortUtilOutputCurrent':eltMesIssPoePortUtilOutputCurrent,'eltMesIssPoePortUtilOutputPower':eltMesIssPoePortUtilOutputPower,'eltMesIssPoePortUtilMaxPower':eltMesIssPoePortUtilMaxPower})