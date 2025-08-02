_p='acPMTrunkTestDurationInterval'
_o='acPMTrunkTestInProgressInterval'
_n='acPMTrunkTestInterval'
_m='acPMTrunkTestType'
_l='acPMConfDurationInterval'
_k='acPMConfInProgressInterval'
_j='acPMConfInProgressType'
_i='acPMConfInterval'
_h='acPMConfType'
_g='acPMBctDurationInterval'
_f='acPMBctInProgressInterval'
_e='acPMBctInProgressType'
_d='acPMBctInterval'
_c='acPMBctType'
_b='acPMIvrContDigitCollectDurationInterval'
_a='acPMIvrContDigitCollectInProgressInterval'
_Z='acPMIvrContDigitCollectInterval'
_Y='acPMIvrContDigitCollectType'
_X='acPMIvrPlayRecordDurationInterval'
_W='acPMIvrPlayRecordInProgressInterval'
_V='acPMIvrPlayRecordInterval'
_U='acPMIvrPlayRecordType'
_T='acPMIvrPlayCollectDurationInterval'
_S='acPMIvrPlayCollectInProgressInterval'
_R='acPMIvrPlayCollectInterval'
_Q='acPMIvrPlayCollectType'
_P='acPMIvrPlayDurationInterval'
_O='acPMIvrPlayInProgressInterval'
_N='acPMIvrPlayInterval'
_M='acPMIvrPlayType'
_L='read-write'
_K='failedDueToProvMismatch'
_J='participants'
_I='failedDueToLackOfResources'
_H='successful'
_G='requstes'
_F='Integer32'
_E='Unsigned32'
_D='not-accessible'
_C='AC-PM-MediaServer-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acBoardMibs,acGeneric,acPerformance,acProducts,acRegistrations,audioCodes=mibBuilder.importSymbols('AUDIOCODES-TYPES-MIB','acBoardMibs','acGeneric','acPerformance','acProducts','acRegistrations','audioCodes')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TAddress','TextualConvention')
acPMMediaServer=ModuleIdentity((1,3,6,1,4,1,5003,10,14))
_AcPMMediaServerConfiguration_ObjectIdentity=ObjectIdentity
acPMMediaServerConfiguration=_AcPMMediaServerConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,10,14,1))
class _AcPMMediaServerConfigurationPeriodLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,894780))
_AcPMMediaServerConfigurationPeriodLength_Type.__name__=_E
_AcPMMediaServerConfigurationPeriodLength_Object=MibScalar
acPMMediaServerConfigurationPeriodLength=_AcPMMediaServerConfigurationPeriodLength_Object((1,3,6,1,4,1,5003,10,14,1,1),_AcPMMediaServerConfigurationPeriodLength_Type())
acPMMediaServerConfigurationPeriodLength.setMaxAccess(_L)
if mibBuilder.loadTexts:acPMMediaServerConfigurationPeriodLength.setStatus(_A)
class _AcPMMediaServerConfigurationResetTotalCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('resetCountersDone',1),('resetTotalCounters',2)))
_AcPMMediaServerConfigurationResetTotalCounters_Type.__name__=_F
_AcPMMediaServerConfigurationResetTotalCounters_Object=MibScalar
acPMMediaServerConfigurationResetTotalCounters=_AcPMMediaServerConfigurationResetTotalCounters_Object((1,3,6,1,4,1,5003,10,14,1,2),_AcPMMediaServerConfigurationResetTotalCounters_Type())
acPMMediaServerConfigurationResetTotalCounters.setMaxAccess(_L)
if mibBuilder.loadTexts:acPMMediaServerConfigurationResetTotalCounters.setStatus(_A)
_AcPMMediaServerData_ObjectIdentity=ObjectIdentity
acPMMediaServerData=_AcPMMediaServerData_ObjectIdentity((1,3,6,1,4,1,5003,10,14,2))
class _AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Type.__name__=_E
_AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Object=MibScalar
acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval=_AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Object((1,3,6,1,4,1,5003,10,14,2,1),_AcPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval_Type())
acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval.setStatus(_A)
_AcPMMediaServerIvr_ObjectIdentity=ObjectIdentity
acPMMediaServerIvr=_AcPMMediaServerIvr_ObjectIdentity((1,3,6,1,4,1,5003,10,14,2,21))
_AcPMIvrPlayTable_Object=MibTable
acPMIvrPlayTable=_AcPMIvrPlayTable_Object((1,3,6,1,4,1,5003,10,14,2,21,21))
if mibBuilder.loadTexts:acPMIvrPlayTable.setStatus(_A)
_AcPMIvrPlayEntry_Object=MibTableRow
acPMIvrPlayEntry=_AcPMIvrPlayEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,21,1))
acPMIvrPlayEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:acPMIvrPlayEntry.setStatus(_A)
class _AcPMIvrPlayType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_K,3)))
_AcPMIvrPlayType_Type.__name__=_F
_AcPMIvrPlayType_Object=MibTableColumn
acPMIvrPlayType=_AcPMIvrPlayType_Object((1,3,6,1,4,1,5003,10,14,2,21,21,1,1),_AcPMIvrPlayType_Type())
acPMIvrPlayType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayType.setStatus(_A)
class _AcPMIvrPlayInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayInterval_Type.__name__=_E
_AcPMIvrPlayInterval_Object=MibTableColumn
acPMIvrPlayInterval=_AcPMIvrPlayInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,21,1,2),_AcPMIvrPlayInterval_Type())
acPMIvrPlayInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayInterval.setStatus(_A)
_AcPMIvrPlayVal_Type=Counter32
_AcPMIvrPlayVal_Object=MibTableColumn
acPMIvrPlayVal=_AcPMIvrPlayVal_Object((1,3,6,1,4,1,5003,10,14,2,21,21,1,3),_AcPMIvrPlayVal_Type())
acPMIvrPlayVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayVal.setStatus(_A)
_AcPMIvrPlayInProgressTable_Object=MibTable
acPMIvrPlayInProgressTable=_AcPMIvrPlayInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,21,22))
if mibBuilder.loadTexts:acPMIvrPlayInProgressTable.setStatus(_A)
_AcPMIvrPlayInProgressEntry_Object=MibTableRow
acPMIvrPlayInProgressEntry=_AcPMIvrPlayInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,22,1))
acPMIvrPlayInProgressEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:acPMIvrPlayInProgressEntry.setStatus(_A)
class _AcPMIvrPlayInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayInProgressInterval_Type.__name__=_E
_AcPMIvrPlayInProgressInterval_Object=MibTableColumn
acPMIvrPlayInProgressInterval=_AcPMIvrPlayInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,22,1,1),_AcPMIvrPlayInProgressInterval_Type())
acPMIvrPlayInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayInProgressInterval.setStatus(_A)
_AcPMIvrPlayInProgressVal_Type=Gauge32
_AcPMIvrPlayInProgressVal_Object=MibTableColumn
acPMIvrPlayInProgressVal=_AcPMIvrPlayInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,21,22,1,2),_AcPMIvrPlayInProgressVal_Type())
acPMIvrPlayInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayInProgressVal.setStatus(_A)
_AcPMIvrPlayInProgressVolume_Type=Counter32
_AcPMIvrPlayInProgressVolume_Object=MibTableColumn
acPMIvrPlayInProgressVolume=_AcPMIvrPlayInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,22,1,3),_AcPMIvrPlayInProgressVolume_Type())
acPMIvrPlayInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayInProgressVolume.setStatus(_A)
class _AcPMIvrPlayInProgressFullDayAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrPlayInProgressFullDayAverage_Type.__name__=_F
_AcPMIvrPlayInProgressFullDayAverage_Object=MibTableColumn
acPMIvrPlayInProgressFullDayAverage=_AcPMIvrPlayInProgressFullDayAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,22,1,4),_AcPMIvrPlayInProgressFullDayAverage_Type())
acPMIvrPlayInProgressFullDayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayInProgressFullDayAverage.setStatus(_A)
_AcPMIvrPlayDurationTable_Object=MibTable
acPMIvrPlayDurationTable=_AcPMIvrPlayDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,21,23))
if mibBuilder.loadTexts:acPMIvrPlayDurationTable.setStatus(_A)
_AcPMIvrPlayDurationEntry_Object=MibTableRow
acPMIvrPlayDurationEntry=_AcPMIvrPlayDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,23,1))
acPMIvrPlayDurationEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:acPMIvrPlayDurationEntry.setStatus(_A)
class _AcPMIvrPlayDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayDurationInterval_Type.__name__=_E
_AcPMIvrPlayDurationInterval_Object=MibTableColumn
acPMIvrPlayDurationInterval=_AcPMIvrPlayDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,23,1,1),_AcPMIvrPlayDurationInterval_Type())
acPMIvrPlayDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayDurationInterval.setStatus(_A)
_AcPMIvrPlayDurationVal_Type=Gauge32
_AcPMIvrPlayDurationVal_Object=MibTableColumn
acPMIvrPlayDurationVal=_AcPMIvrPlayDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,21,23,1,2),_AcPMIvrPlayDurationVal_Type())
acPMIvrPlayDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayDurationVal.setStatus(_A)
_AcPMIvrPlayDurationVolume_Type=Counter32
_AcPMIvrPlayDurationVolume_Object=MibTableColumn
acPMIvrPlayDurationVolume=_AcPMIvrPlayDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,23,1,3),_AcPMIvrPlayDurationVolume_Type())
acPMIvrPlayDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayDurationVolume.setStatus(_A)
class _AcPMIvrPlayDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrPlayDurationAverage_Type.__name__=_F
_AcPMIvrPlayDurationAverage_Object=MibTableColumn
acPMIvrPlayDurationAverage=_AcPMIvrPlayDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,23,1,4),_AcPMIvrPlayDurationAverage_Type())
acPMIvrPlayDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayDurationAverage.setStatus(_A)
_AcPMIvrPlayCollectTable_Object=MibTable
acPMIvrPlayCollectTable=_AcPMIvrPlayCollectTable_Object((1,3,6,1,4,1,5003,10,14,2,21,24))
if mibBuilder.loadTexts:acPMIvrPlayCollectTable.setStatus(_A)
_AcPMIvrPlayCollectEntry_Object=MibTableRow
acPMIvrPlayCollectEntry=_AcPMIvrPlayCollectEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,24,1))
acPMIvrPlayCollectEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:acPMIvrPlayCollectEntry.setStatus(_A)
class _AcPMIvrPlayCollectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_K,3)))
_AcPMIvrPlayCollectType_Type.__name__=_F
_AcPMIvrPlayCollectType_Object=MibTableColumn
acPMIvrPlayCollectType=_AcPMIvrPlayCollectType_Object((1,3,6,1,4,1,5003,10,14,2,21,24,1,1),_AcPMIvrPlayCollectType_Type())
acPMIvrPlayCollectType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayCollectType.setStatus(_A)
class _AcPMIvrPlayCollectInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayCollectInterval_Type.__name__=_E
_AcPMIvrPlayCollectInterval_Object=MibTableColumn
acPMIvrPlayCollectInterval=_AcPMIvrPlayCollectInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,24,1,2),_AcPMIvrPlayCollectInterval_Type())
acPMIvrPlayCollectInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayCollectInterval.setStatus(_A)
_AcPMIvrPlayCollectVal_Type=Counter32
_AcPMIvrPlayCollectVal_Object=MibTableColumn
acPMIvrPlayCollectVal=_AcPMIvrPlayCollectVal_Object((1,3,6,1,4,1,5003,10,14,2,21,24,1,3),_AcPMIvrPlayCollectVal_Type())
acPMIvrPlayCollectVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectVal.setStatus(_A)
_AcPMIvrPlayCollectInProgressTable_Object=MibTable
acPMIvrPlayCollectInProgressTable=_AcPMIvrPlayCollectInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,21,25))
if mibBuilder.loadTexts:acPMIvrPlayCollectInProgressTable.setStatus(_A)
_AcPMIvrPlayCollectInProgressEntry_Object=MibTableRow
acPMIvrPlayCollectInProgressEntry=_AcPMIvrPlayCollectInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,25,1))
acPMIvrPlayCollectInProgressEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:acPMIvrPlayCollectInProgressEntry.setStatus(_A)
class _AcPMIvrPlayCollectInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayCollectInProgressInterval_Type.__name__=_E
_AcPMIvrPlayCollectInProgressInterval_Object=MibTableColumn
acPMIvrPlayCollectInProgressInterval=_AcPMIvrPlayCollectInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,25,1,1),_AcPMIvrPlayCollectInProgressInterval_Type())
acPMIvrPlayCollectInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayCollectInProgressInterval.setStatus(_A)
_AcPMIvrPlayCollectInProgressVal_Type=Gauge32
_AcPMIvrPlayCollectInProgressVal_Object=MibTableColumn
acPMIvrPlayCollectInProgressVal=_AcPMIvrPlayCollectInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,21,25,1,2),_AcPMIvrPlayCollectInProgressVal_Type())
acPMIvrPlayCollectInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectInProgressVal.setStatus(_A)
_AcPMIvrPlayCollectInProgressVolume_Type=Counter32
_AcPMIvrPlayCollectInProgressVolume_Object=MibTableColumn
acPMIvrPlayCollectInProgressVolume=_AcPMIvrPlayCollectInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,25,1,3),_AcPMIvrPlayCollectInProgressVolume_Type())
acPMIvrPlayCollectInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectInProgressVolume.setStatus(_A)
class _AcPMIvrPlayCollectInProgressFullDayAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrPlayCollectInProgressFullDayAverage_Type.__name__=_F
_AcPMIvrPlayCollectInProgressFullDayAverage_Object=MibTableColumn
acPMIvrPlayCollectInProgressFullDayAverage=_AcPMIvrPlayCollectInProgressFullDayAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,25,1,4),_AcPMIvrPlayCollectInProgressFullDayAverage_Type())
acPMIvrPlayCollectInProgressFullDayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectInProgressFullDayAverage.setStatus(_A)
_AcPMIvrPlayCollectDurationTable_Object=MibTable
acPMIvrPlayCollectDurationTable=_AcPMIvrPlayCollectDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,21,26))
if mibBuilder.loadTexts:acPMIvrPlayCollectDurationTable.setStatus(_A)
_AcPMIvrPlayCollectDurationEntry_Object=MibTableRow
acPMIvrPlayCollectDurationEntry=_AcPMIvrPlayCollectDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,26,1))
acPMIvrPlayCollectDurationEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:acPMIvrPlayCollectDurationEntry.setStatus(_A)
class _AcPMIvrPlayCollectDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayCollectDurationInterval_Type.__name__=_E
_AcPMIvrPlayCollectDurationInterval_Object=MibTableColumn
acPMIvrPlayCollectDurationInterval=_AcPMIvrPlayCollectDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,26,1,1),_AcPMIvrPlayCollectDurationInterval_Type())
acPMIvrPlayCollectDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayCollectDurationInterval.setStatus(_A)
_AcPMIvrPlayCollectDurationVal_Type=Gauge32
_AcPMIvrPlayCollectDurationVal_Object=MibTableColumn
acPMIvrPlayCollectDurationVal=_AcPMIvrPlayCollectDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,21,26,1,2),_AcPMIvrPlayCollectDurationVal_Type())
acPMIvrPlayCollectDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectDurationVal.setStatus(_A)
_AcPMIvrPlayCollectDurationVolume_Type=Counter32
_AcPMIvrPlayCollectDurationVolume_Object=MibTableColumn
acPMIvrPlayCollectDurationVolume=_AcPMIvrPlayCollectDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,26,1,3),_AcPMIvrPlayCollectDurationVolume_Type())
acPMIvrPlayCollectDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectDurationVolume.setStatus(_A)
class _AcPMIvrPlayCollectDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrPlayCollectDurationAverage_Type.__name__=_F
_AcPMIvrPlayCollectDurationAverage_Object=MibTableColumn
acPMIvrPlayCollectDurationAverage=_AcPMIvrPlayCollectDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,26,1,4),_AcPMIvrPlayCollectDurationAverage_Type())
acPMIvrPlayCollectDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayCollectDurationAverage.setStatus(_A)
_AcPMIvrPlayRecordTable_Object=MibTable
acPMIvrPlayRecordTable=_AcPMIvrPlayRecordTable_Object((1,3,6,1,4,1,5003,10,14,2,21,27))
if mibBuilder.loadTexts:acPMIvrPlayRecordTable.setStatus(_A)
_AcPMIvrPlayRecordEntry_Object=MibTableRow
acPMIvrPlayRecordEntry=_AcPMIvrPlayRecordEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,27,1))
acPMIvrPlayRecordEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:acPMIvrPlayRecordEntry.setStatus(_A)
class _AcPMIvrPlayRecordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_K,3)))
_AcPMIvrPlayRecordType_Type.__name__=_F
_AcPMIvrPlayRecordType_Object=MibTableColumn
acPMIvrPlayRecordType=_AcPMIvrPlayRecordType_Object((1,3,6,1,4,1,5003,10,14,2,21,27,1,1),_AcPMIvrPlayRecordType_Type())
acPMIvrPlayRecordType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayRecordType.setStatus(_A)
class _AcPMIvrPlayRecordInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayRecordInterval_Type.__name__=_E
_AcPMIvrPlayRecordInterval_Object=MibTableColumn
acPMIvrPlayRecordInterval=_AcPMIvrPlayRecordInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,27,1,2),_AcPMIvrPlayRecordInterval_Type())
acPMIvrPlayRecordInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayRecordInterval.setStatus(_A)
_AcPMIvrPlayRecordVal_Type=Counter32
_AcPMIvrPlayRecordVal_Object=MibTableColumn
acPMIvrPlayRecordVal=_AcPMIvrPlayRecordVal_Object((1,3,6,1,4,1,5003,10,14,2,21,27,1,3),_AcPMIvrPlayRecordVal_Type())
acPMIvrPlayRecordVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordVal.setStatus(_A)
_AcPMIvrPlayRecordInProgressTable_Object=MibTable
acPMIvrPlayRecordInProgressTable=_AcPMIvrPlayRecordInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,21,28))
if mibBuilder.loadTexts:acPMIvrPlayRecordInProgressTable.setStatus(_A)
_AcPMIvrPlayRecordInProgressEntry_Object=MibTableRow
acPMIvrPlayRecordInProgressEntry=_AcPMIvrPlayRecordInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,28,1))
acPMIvrPlayRecordInProgressEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:acPMIvrPlayRecordInProgressEntry.setStatus(_A)
class _AcPMIvrPlayRecordInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayRecordInProgressInterval_Type.__name__=_E
_AcPMIvrPlayRecordInProgressInterval_Object=MibTableColumn
acPMIvrPlayRecordInProgressInterval=_AcPMIvrPlayRecordInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,28,1,1),_AcPMIvrPlayRecordInProgressInterval_Type())
acPMIvrPlayRecordInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayRecordInProgressInterval.setStatus(_A)
_AcPMIvrPlayRecordInProgressVal_Type=Gauge32
_AcPMIvrPlayRecordInProgressVal_Object=MibTableColumn
acPMIvrPlayRecordInProgressVal=_AcPMIvrPlayRecordInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,21,28,1,2),_AcPMIvrPlayRecordInProgressVal_Type())
acPMIvrPlayRecordInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordInProgressVal.setStatus(_A)
_AcPMIvrPlayRecordInProgressVolume_Type=Counter32
_AcPMIvrPlayRecordInProgressVolume_Object=MibTableColumn
acPMIvrPlayRecordInProgressVolume=_AcPMIvrPlayRecordInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,28,1,3),_AcPMIvrPlayRecordInProgressVolume_Type())
acPMIvrPlayRecordInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordInProgressVolume.setStatus(_A)
class _AcPMIvrPlayRecordInProgressFullDayAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrPlayRecordInProgressFullDayAverage_Type.__name__=_F
_AcPMIvrPlayRecordInProgressFullDayAverage_Object=MibTableColumn
acPMIvrPlayRecordInProgressFullDayAverage=_AcPMIvrPlayRecordInProgressFullDayAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,28,1,4),_AcPMIvrPlayRecordInProgressFullDayAverage_Type())
acPMIvrPlayRecordInProgressFullDayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordInProgressFullDayAverage.setStatus(_A)
_AcPMIvrPlayRecordDurationTable_Object=MibTable
acPMIvrPlayRecordDurationTable=_AcPMIvrPlayRecordDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,21,29))
if mibBuilder.loadTexts:acPMIvrPlayRecordDurationTable.setStatus(_A)
_AcPMIvrPlayRecordDurationEntry_Object=MibTableRow
acPMIvrPlayRecordDurationEntry=_AcPMIvrPlayRecordDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,29,1))
acPMIvrPlayRecordDurationEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:acPMIvrPlayRecordDurationEntry.setStatus(_A)
class _AcPMIvrPlayRecordDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrPlayRecordDurationInterval_Type.__name__=_E
_AcPMIvrPlayRecordDurationInterval_Object=MibTableColumn
acPMIvrPlayRecordDurationInterval=_AcPMIvrPlayRecordDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,29,1,1),_AcPMIvrPlayRecordDurationInterval_Type())
acPMIvrPlayRecordDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrPlayRecordDurationInterval.setStatus(_A)
_AcPMIvrPlayRecordDurationVal_Type=Gauge32
_AcPMIvrPlayRecordDurationVal_Object=MibTableColumn
acPMIvrPlayRecordDurationVal=_AcPMIvrPlayRecordDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,21,29,1,2),_AcPMIvrPlayRecordDurationVal_Type())
acPMIvrPlayRecordDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordDurationVal.setStatus(_A)
_AcPMIvrPlayRecordDurationVolume_Type=Counter32
_AcPMIvrPlayRecordDurationVolume_Object=MibTableColumn
acPMIvrPlayRecordDurationVolume=_AcPMIvrPlayRecordDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,29,1,3),_AcPMIvrPlayRecordDurationVolume_Type())
acPMIvrPlayRecordDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordDurationVolume.setStatus(_A)
class _AcPMIvrPlayRecordDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrPlayRecordDurationAverage_Type.__name__=_F
_AcPMIvrPlayRecordDurationAverage_Object=MibTableColumn
acPMIvrPlayRecordDurationAverage=_AcPMIvrPlayRecordDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,29,1,4),_AcPMIvrPlayRecordDurationAverage_Type())
acPMIvrPlayRecordDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrPlayRecordDurationAverage.setStatus(_A)
_AcPMIvrContDigitCollectTable_Object=MibTable
acPMIvrContDigitCollectTable=_AcPMIvrContDigitCollectTable_Object((1,3,6,1,4,1,5003,10,14,2,21,30))
if mibBuilder.loadTexts:acPMIvrContDigitCollectTable.setStatus(_A)
_AcPMIvrContDigitCollectEntry_Object=MibTableRow
acPMIvrContDigitCollectEntry=_AcPMIvrContDigitCollectEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,30,1))
acPMIvrContDigitCollectEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:acPMIvrContDigitCollectEntry.setStatus(_A)
class _AcPMIvrContDigitCollectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2)))
_AcPMIvrContDigitCollectType_Type.__name__=_F
_AcPMIvrContDigitCollectType_Object=MibTableColumn
acPMIvrContDigitCollectType=_AcPMIvrContDigitCollectType_Object((1,3,6,1,4,1,5003,10,14,2,21,30,1,1),_AcPMIvrContDigitCollectType_Type())
acPMIvrContDigitCollectType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrContDigitCollectType.setStatus(_A)
class _AcPMIvrContDigitCollectInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrContDigitCollectInterval_Type.__name__=_E
_AcPMIvrContDigitCollectInterval_Object=MibTableColumn
acPMIvrContDigitCollectInterval=_AcPMIvrContDigitCollectInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,30,1,2),_AcPMIvrContDigitCollectInterval_Type())
acPMIvrContDigitCollectInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrContDigitCollectInterval.setStatus(_A)
_AcPMIvrContDigitCollectVal_Type=Counter32
_AcPMIvrContDigitCollectVal_Object=MibTableColumn
acPMIvrContDigitCollectVal=_AcPMIvrContDigitCollectVal_Object((1,3,6,1,4,1,5003,10,14,2,21,30,1,3),_AcPMIvrContDigitCollectVal_Type())
acPMIvrContDigitCollectVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrContDigitCollectVal.setStatus(_A)
_AcPMIvrContDigitCollectInProgressTable_Object=MibTable
acPMIvrContDigitCollectInProgressTable=_AcPMIvrContDigitCollectInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,21,31))
if mibBuilder.loadTexts:acPMIvrContDigitCollectInProgressTable.setStatus(_A)
_AcPMIvrContDigitCollectInProgressEntry_Object=MibTableRow
acPMIvrContDigitCollectInProgressEntry=_AcPMIvrContDigitCollectInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,31,1))
acPMIvrContDigitCollectInProgressEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:acPMIvrContDigitCollectInProgressEntry.setStatus(_A)
class _AcPMIvrContDigitCollectInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrContDigitCollectInProgressInterval_Type.__name__=_E
_AcPMIvrContDigitCollectInProgressInterval_Object=MibTableColumn
acPMIvrContDigitCollectInProgressInterval=_AcPMIvrContDigitCollectInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,31,1,1),_AcPMIvrContDigitCollectInProgressInterval_Type())
acPMIvrContDigitCollectInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrContDigitCollectInProgressInterval.setStatus(_A)
_AcPMIvrContDigitCollectInProgressVal_Type=Gauge32
_AcPMIvrContDigitCollectInProgressVal_Object=MibTableColumn
acPMIvrContDigitCollectInProgressVal=_AcPMIvrContDigitCollectInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,21,31,1,2),_AcPMIvrContDigitCollectInProgressVal_Type())
acPMIvrContDigitCollectInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrContDigitCollectInProgressVal.setStatus(_A)
_AcPMIvrContDigitCollectInProgressVolume_Type=Counter32
_AcPMIvrContDigitCollectInProgressVolume_Object=MibTableColumn
acPMIvrContDigitCollectInProgressVolume=_AcPMIvrContDigitCollectInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,31,1,3),_AcPMIvrContDigitCollectInProgressVolume_Type())
acPMIvrContDigitCollectInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrContDigitCollectInProgressVolume.setStatus(_A)
_AcPMIvrContDigitCollectDurationTable_Object=MibTable
acPMIvrContDigitCollectDurationTable=_AcPMIvrContDigitCollectDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,21,32))
if mibBuilder.loadTexts:acPMIvrContDigitCollectDurationTable.setStatus(_A)
_AcPMIvrContDigitCollectDurationEntry_Object=MibTableRow
acPMIvrContDigitCollectDurationEntry=_AcPMIvrContDigitCollectDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,21,32,1))
acPMIvrContDigitCollectDurationEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:acPMIvrContDigitCollectDurationEntry.setStatus(_A)
class _AcPMIvrContDigitCollectDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMIvrContDigitCollectDurationInterval_Type.__name__=_E
_AcPMIvrContDigitCollectDurationInterval_Object=MibTableColumn
acPMIvrContDigitCollectDurationInterval=_AcPMIvrContDigitCollectDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,21,32,1,1),_AcPMIvrContDigitCollectDurationInterval_Type())
acPMIvrContDigitCollectDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMIvrContDigitCollectDurationInterval.setStatus(_A)
_AcPMIvrContDigitCollectDurationVal_Type=Gauge32
_AcPMIvrContDigitCollectDurationVal_Object=MibTableColumn
acPMIvrContDigitCollectDurationVal=_AcPMIvrContDigitCollectDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,21,32,1,2),_AcPMIvrContDigitCollectDurationVal_Type())
acPMIvrContDigitCollectDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrContDigitCollectDurationVal.setStatus(_A)
_AcPMIvrContDigitCollectDurationVolume_Type=Counter32
_AcPMIvrContDigitCollectDurationVolume_Object=MibTableColumn
acPMIvrContDigitCollectDurationVolume=_AcPMIvrContDigitCollectDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,21,32,1,3),_AcPMIvrContDigitCollectDurationVolume_Type())
acPMIvrContDigitCollectDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrContDigitCollectDurationVolume.setStatus(_A)
class _AcPMIvrContDigitCollectDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMIvrContDigitCollectDurationAverage_Type.__name__=_F
_AcPMIvrContDigitCollectDurationAverage_Object=MibTableColumn
acPMIvrContDigitCollectDurationAverage=_AcPMIvrContDigitCollectDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,21,32,1,4),_AcPMIvrContDigitCollectDurationAverage_Type())
acPMIvrContDigitCollectDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMIvrContDigitCollectDurationAverage.setStatus(_A)
_AcPMMediaServerBct_ObjectIdentity=ObjectIdentity
acPMMediaServerBct=_AcPMMediaServerBct_ObjectIdentity((1,3,6,1,4,1,5003,10,14,2,31))
_AcPMBctTable_Object=MibTable
acPMBctTable=_AcPMBctTable_Object((1,3,6,1,4,1,5003,10,14,2,31,21))
if mibBuilder.loadTexts:acPMBctTable.setStatus(_A)
_AcPMBctEntry_Object=MibTableRow
acPMBctEntry=_AcPMBctEntry_Object((1,3,6,1,4,1,5003,10,14,2,31,21,1))
acPMBctEntry.setIndexNames((0,_C,_c),(0,_C,_d))
if mibBuilder.loadTexts:acPMBctEntry.setStatus(_A)
class _AcPMBctType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3)))
_AcPMBctType_Type.__name__=_F
_AcPMBctType_Object=MibTableColumn
acPMBctType=_AcPMBctType_Object((1,3,6,1,4,1,5003,10,14,2,31,21,1,1),_AcPMBctType_Type())
acPMBctType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMBctType.setStatus(_A)
class _AcPMBctInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMBctInterval_Type.__name__=_E
_AcPMBctInterval_Object=MibTableColumn
acPMBctInterval=_AcPMBctInterval_Object((1,3,6,1,4,1,5003,10,14,2,31,21,1,2),_AcPMBctInterval_Type())
acPMBctInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMBctInterval.setStatus(_A)
_AcPMBctVal_Type=Counter32
_AcPMBctVal_Object=MibTableColumn
acPMBctVal=_AcPMBctVal_Object((1,3,6,1,4,1,5003,10,14,2,31,21,1,3),_AcPMBctVal_Type())
acPMBctVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMBctVal.setStatus(_A)
_AcPMBctInProgressTable_Object=MibTable
acPMBctInProgressTable=_AcPMBctInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,31,22))
if mibBuilder.loadTexts:acPMBctInProgressTable.setStatus(_A)
_AcPMBctInProgressEntry_Object=MibTableRow
acPMBctInProgressEntry=_AcPMBctInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,31,22,1))
acPMBctInProgressEntry.setIndexNames((0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:acPMBctInProgressEntry.setStatus(_A)
class _AcPMBctInProgressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bct',0),(_J,1)))
_AcPMBctInProgressType_Type.__name__=_F
_AcPMBctInProgressType_Object=MibTableColumn
acPMBctInProgressType=_AcPMBctInProgressType_Object((1,3,6,1,4,1,5003,10,14,2,31,22,1,1),_AcPMBctInProgressType_Type())
acPMBctInProgressType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMBctInProgressType.setStatus(_A)
class _AcPMBctInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMBctInProgressInterval_Type.__name__=_E
_AcPMBctInProgressInterval_Object=MibTableColumn
acPMBctInProgressInterval=_AcPMBctInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,31,22,1,2),_AcPMBctInProgressInterval_Type())
acPMBctInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMBctInProgressInterval.setStatus(_A)
_AcPMBctInProgressVal_Type=Gauge32
_AcPMBctInProgressVal_Object=MibTableColumn
acPMBctInProgressVal=_AcPMBctInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,31,22,1,3),_AcPMBctInProgressVal_Type())
acPMBctInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMBctInProgressVal.setStatus(_A)
_AcPMBctInProgressVolume_Type=Counter32
_AcPMBctInProgressVolume_Object=MibTableColumn
acPMBctInProgressVolume=_AcPMBctInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,31,22,1,4),_AcPMBctInProgressVolume_Type())
acPMBctInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMBctInProgressVolume.setStatus(_A)
_AcPMBctDurationTable_Object=MibTable
acPMBctDurationTable=_AcPMBctDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,31,23))
if mibBuilder.loadTexts:acPMBctDurationTable.setStatus(_A)
_AcPMBctDurationEntry_Object=MibTableRow
acPMBctDurationEntry=_AcPMBctDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,31,23,1))
acPMBctDurationEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:acPMBctDurationEntry.setStatus(_A)
class _AcPMBctDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMBctDurationInterval_Type.__name__=_E
_AcPMBctDurationInterval_Object=MibTableColumn
acPMBctDurationInterval=_AcPMBctDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,31,23,1,1),_AcPMBctDurationInterval_Type())
acPMBctDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMBctDurationInterval.setStatus(_A)
_AcPMBctDurationVal_Type=Gauge32
_AcPMBctDurationVal_Object=MibTableColumn
acPMBctDurationVal=_AcPMBctDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,31,23,1,2),_AcPMBctDurationVal_Type())
acPMBctDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMBctDurationVal.setStatus(_A)
_AcPMBctDurationVolume_Type=Counter32
_AcPMBctDurationVolume_Object=MibTableColumn
acPMBctDurationVolume=_AcPMBctDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,31,23,1,3),_AcPMBctDurationVolume_Type())
acPMBctDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMBctDurationVolume.setStatus(_A)
class _AcPMBctDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMBctDurationAverage_Type.__name__=_F
_AcPMBctDurationAverage_Object=MibTableColumn
acPMBctDurationAverage=_AcPMBctDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,31,23,1,4),_AcPMBctDurationAverage_Type())
acPMBctDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMBctDurationAverage.setStatus(_A)
_AcPMMediaServerConference_ObjectIdentity=ObjectIdentity
acPMMediaServerConference=_AcPMMediaServerConference_ObjectIdentity((1,3,6,1,4,1,5003,10,14,2,41))
_AcPMConfTable_Object=MibTable
acPMConfTable=_AcPMConfTable_Object((1,3,6,1,4,1,5003,10,14,2,41,21))
if mibBuilder.loadTexts:acPMConfTable.setStatus(_A)
_AcPMConfEntry_Object=MibTableRow
acPMConfEntry=_AcPMConfEntry_Object((1,3,6,1,4,1,5003,10,14,2,41,21,1))
acPMConfEntry.setIndexNames((0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:acPMConfEntry.setStatus(_A)
class _AcPMConfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3)))
_AcPMConfType_Type.__name__=_F
_AcPMConfType_Object=MibTableColumn
acPMConfType=_AcPMConfType_Object((1,3,6,1,4,1,5003,10,14,2,41,21,1,1),_AcPMConfType_Type())
acPMConfType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMConfType.setStatus(_A)
class _AcPMConfInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMConfInterval_Type.__name__=_E
_AcPMConfInterval_Object=MibTableColumn
acPMConfInterval=_AcPMConfInterval_Object((1,3,6,1,4,1,5003,10,14,2,41,21,1,2),_AcPMConfInterval_Type())
acPMConfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMConfInterval.setStatus(_A)
_AcPMConfVal_Type=Counter32
_AcPMConfVal_Object=MibTableColumn
acPMConfVal=_AcPMConfVal_Object((1,3,6,1,4,1,5003,10,14,2,41,21,1,3),_AcPMConfVal_Type())
acPMConfVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMConfVal.setStatus(_A)
_AcPMConfInProgressTable_Object=MibTable
acPMConfInProgressTable=_AcPMConfInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,41,22))
if mibBuilder.loadTexts:acPMConfInProgressTable.setStatus(_A)
_AcPMConfInProgressEntry_Object=MibTableRow
acPMConfInProgressEntry=_AcPMConfInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,41,22,1))
acPMConfInProgressEntry.setIndexNames((0,_C,_j),(0,_C,_k))
if mibBuilder.loadTexts:acPMConfInProgressEntry.setStatus(_A)
class _AcPMConfInProgressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('conference',0),(_J,1)))
_AcPMConfInProgressType_Type.__name__=_F
_AcPMConfInProgressType_Object=MibTableColumn
acPMConfInProgressType=_AcPMConfInProgressType_Object((1,3,6,1,4,1,5003,10,14,2,41,22,1,1),_AcPMConfInProgressType_Type())
acPMConfInProgressType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMConfInProgressType.setStatus(_A)
class _AcPMConfInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMConfInProgressInterval_Type.__name__=_E
_AcPMConfInProgressInterval_Object=MibTableColumn
acPMConfInProgressInterval=_AcPMConfInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,41,22,1,2),_AcPMConfInProgressInterval_Type())
acPMConfInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMConfInProgressInterval.setStatus(_A)
_AcPMConfInProgressVal_Type=Gauge32
_AcPMConfInProgressVal_Object=MibTableColumn
acPMConfInProgressVal=_AcPMConfInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,41,22,1,3),_AcPMConfInProgressVal_Type())
acPMConfInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMConfInProgressVal.setStatus(_A)
_AcPMConfInProgressVolume_Type=Counter32
_AcPMConfInProgressVolume_Object=MibTableColumn
acPMConfInProgressVolume=_AcPMConfInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,41,22,1,4),_AcPMConfInProgressVolume_Type())
acPMConfInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMConfInProgressVolume.setStatus(_A)
_AcPMConfDurationTable_Object=MibTable
acPMConfDurationTable=_AcPMConfDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,41,23))
if mibBuilder.loadTexts:acPMConfDurationTable.setStatus(_A)
_AcPMConfDurationEntry_Object=MibTableRow
acPMConfDurationEntry=_AcPMConfDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,41,23,1))
acPMConfDurationEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:acPMConfDurationEntry.setStatus(_A)
class _AcPMConfDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMConfDurationInterval_Type.__name__=_E
_AcPMConfDurationInterval_Object=MibTableColumn
acPMConfDurationInterval=_AcPMConfDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,41,23,1,1),_AcPMConfDurationInterval_Type())
acPMConfDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMConfDurationInterval.setStatus(_A)
_AcPMConfDurationVal_Type=Gauge32
_AcPMConfDurationVal_Object=MibTableColumn
acPMConfDurationVal=_AcPMConfDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,41,23,1,2),_AcPMConfDurationVal_Type())
acPMConfDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMConfDurationVal.setStatus(_A)
_AcPMConfDurationVolume_Type=Counter32
_AcPMConfDurationVolume_Object=MibTableColumn
acPMConfDurationVolume=_AcPMConfDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,41,23,1,3),_AcPMConfDurationVolume_Type())
acPMConfDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMConfDurationVolume.setStatus(_A)
class _AcPMConfDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMConfDurationAverage_Type.__name__=_F
_AcPMConfDurationAverage_Object=MibTableColumn
acPMConfDurationAverage=_AcPMConfDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,41,23,1,4),_AcPMConfDurationAverage_Type())
acPMConfDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMConfDurationAverage.setStatus(_A)
_AcPMMediaServerTrunkTest_ObjectIdentity=ObjectIdentity
acPMMediaServerTrunkTest=_AcPMMediaServerTrunkTest_ObjectIdentity((1,3,6,1,4,1,5003,10,14,2,51))
_AcPMTrunkTestTable_Object=MibTable
acPMTrunkTestTable=_AcPMTrunkTestTable_Object((1,3,6,1,4,1,5003,10,14,2,51,21))
if mibBuilder.loadTexts:acPMTrunkTestTable.setStatus(_A)
_AcPMTrunkTestEntry_Object=MibTableRow
acPMTrunkTestEntry=_AcPMTrunkTestEntry_Object((1,3,6,1,4,1,5003,10,14,2,51,21,1))
acPMTrunkTestEntry.setIndexNames((0,_C,_m),(0,_C,_n))
if mibBuilder.loadTexts:acPMTrunkTestEntry.setStatus(_A)
class _AcPMTrunkTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2)))
_AcPMTrunkTestType_Type.__name__=_F
_AcPMTrunkTestType_Object=MibTableColumn
acPMTrunkTestType=_AcPMTrunkTestType_Object((1,3,6,1,4,1,5003,10,14,2,51,21,1,1),_AcPMTrunkTestType_Type())
acPMTrunkTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMTrunkTestType.setStatus(_A)
class _AcPMTrunkTestInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMTrunkTestInterval_Type.__name__=_E
_AcPMTrunkTestInterval_Object=MibTableColumn
acPMTrunkTestInterval=_AcPMTrunkTestInterval_Object((1,3,6,1,4,1,5003,10,14,2,51,21,1,2),_AcPMTrunkTestInterval_Type())
acPMTrunkTestInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMTrunkTestInterval.setStatus(_A)
_AcPMTrunkTestVal_Type=Counter32
_AcPMTrunkTestVal_Object=MibTableColumn
acPMTrunkTestVal=_AcPMTrunkTestVal_Object((1,3,6,1,4,1,5003,10,14,2,51,21,1,3),_AcPMTrunkTestVal_Type())
acPMTrunkTestVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMTrunkTestVal.setStatus(_A)
_AcPMTrunkTestInProgressTable_Object=MibTable
acPMTrunkTestInProgressTable=_AcPMTrunkTestInProgressTable_Object((1,3,6,1,4,1,5003,10,14,2,51,22))
if mibBuilder.loadTexts:acPMTrunkTestInProgressTable.setStatus(_A)
_AcPMTrunkTestInProgressEntry_Object=MibTableRow
acPMTrunkTestInProgressEntry=_AcPMTrunkTestInProgressEntry_Object((1,3,6,1,4,1,5003,10,14,2,51,22,1))
acPMTrunkTestInProgressEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:acPMTrunkTestInProgressEntry.setStatus(_A)
class _AcPMTrunkTestInProgressInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMTrunkTestInProgressInterval_Type.__name__=_E
_AcPMTrunkTestInProgressInterval_Object=MibTableColumn
acPMTrunkTestInProgressInterval=_AcPMTrunkTestInProgressInterval_Object((1,3,6,1,4,1,5003,10,14,2,51,22,1,1),_AcPMTrunkTestInProgressInterval_Type())
acPMTrunkTestInProgressInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMTrunkTestInProgressInterval.setStatus(_A)
_AcPMTrunkTestInProgressVal_Type=Gauge32
_AcPMTrunkTestInProgressVal_Object=MibTableColumn
acPMTrunkTestInProgressVal=_AcPMTrunkTestInProgressVal_Object((1,3,6,1,4,1,5003,10,14,2,51,22,1,2),_AcPMTrunkTestInProgressVal_Type())
acPMTrunkTestInProgressVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMTrunkTestInProgressVal.setStatus(_A)
_AcPMTrunkTestInProgressVolume_Type=Counter32
_AcPMTrunkTestInProgressVolume_Object=MibTableColumn
acPMTrunkTestInProgressVolume=_AcPMTrunkTestInProgressVolume_Object((1,3,6,1,4,1,5003,10,14,2,51,22,1,3),_AcPMTrunkTestInProgressVolume_Type())
acPMTrunkTestInProgressVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMTrunkTestInProgressVolume.setStatus(_A)
_AcPMTrunkTestDurationTable_Object=MibTable
acPMTrunkTestDurationTable=_AcPMTrunkTestDurationTable_Object((1,3,6,1,4,1,5003,10,14,2,51,23))
if mibBuilder.loadTexts:acPMTrunkTestDurationTable.setStatus(_A)
_AcPMTrunkTestDurationEntry_Object=MibTableRow
acPMTrunkTestDurationEntry=_AcPMTrunkTestDurationEntry_Object((1,3,6,1,4,1,5003,10,14,2,51,23,1))
acPMTrunkTestDurationEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:acPMTrunkTestDurationEntry.setStatus(_A)
class _AcPMTrunkTestDurationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMTrunkTestDurationInterval_Type.__name__=_E
_AcPMTrunkTestDurationInterval_Object=MibTableColumn
acPMTrunkTestDurationInterval=_AcPMTrunkTestDurationInterval_Object((1,3,6,1,4,1,5003,10,14,2,51,23,1,1),_AcPMTrunkTestDurationInterval_Type())
acPMTrunkTestDurationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:acPMTrunkTestDurationInterval.setStatus(_A)
_AcPMTrunkTestDurationVal_Type=Gauge32
_AcPMTrunkTestDurationVal_Object=MibTableColumn
acPMTrunkTestDurationVal=_AcPMTrunkTestDurationVal_Object((1,3,6,1,4,1,5003,10,14,2,51,23,1,2),_AcPMTrunkTestDurationVal_Type())
acPMTrunkTestDurationVal.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMTrunkTestDurationVal.setStatus(_A)
_AcPMTrunkTestDurationVolume_Type=Counter32
_AcPMTrunkTestDurationVolume_Object=MibTableColumn
acPMTrunkTestDurationVolume=_AcPMTrunkTestDurationVolume_Object((1,3,6,1,4,1,5003,10,14,2,51,23,1,3),_AcPMTrunkTestDurationVolume_Type())
acPMTrunkTestDurationVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMTrunkTestDurationVolume.setStatus(_A)
class _AcPMTrunkTestDurationAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMTrunkTestDurationAverage_Type.__name__=_F
_AcPMTrunkTestDurationAverage_Object=MibTableColumn
acPMTrunkTestDurationAverage=_AcPMTrunkTestDurationAverage_Object((1,3,6,1,4,1,5003,10,14,2,51,23,1,4),_AcPMTrunkTestDurationAverage_Type())
acPMTrunkTestDurationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:acPMTrunkTestDurationAverage.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'acPMMediaServer':acPMMediaServer,'acPMMediaServerConfiguration':acPMMediaServerConfiguration,'acPMMediaServerConfigurationPeriodLength':acPMMediaServerConfigurationPeriodLength,'acPMMediaServerConfigurationResetTotalCounters':acPMMediaServerConfigurationResetTotalCounters,'acPMMediaServerData':acPMMediaServerData,'acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval':acPMMediaServerDataAcPMMediaServerTimeFromStartOfInterval,'acPMMediaServerIvr':acPMMediaServerIvr,'acPMIvrPlayTable':acPMIvrPlayTable,'acPMIvrPlayEntry':acPMIvrPlayEntry,_M:acPMIvrPlayType,_N:acPMIvrPlayInterval,'acPMIvrPlayVal':acPMIvrPlayVal,'acPMIvrPlayInProgressTable':acPMIvrPlayInProgressTable,'acPMIvrPlayInProgressEntry':acPMIvrPlayInProgressEntry,_O:acPMIvrPlayInProgressInterval,'acPMIvrPlayInProgressVal':acPMIvrPlayInProgressVal,'acPMIvrPlayInProgressVolume':acPMIvrPlayInProgressVolume,'acPMIvrPlayInProgressFullDayAverage':acPMIvrPlayInProgressFullDayAverage,'acPMIvrPlayDurationTable':acPMIvrPlayDurationTable,'acPMIvrPlayDurationEntry':acPMIvrPlayDurationEntry,_P:acPMIvrPlayDurationInterval,'acPMIvrPlayDurationVal':acPMIvrPlayDurationVal,'acPMIvrPlayDurationVolume':acPMIvrPlayDurationVolume,'acPMIvrPlayDurationAverage':acPMIvrPlayDurationAverage,'acPMIvrPlayCollectTable':acPMIvrPlayCollectTable,'acPMIvrPlayCollectEntry':acPMIvrPlayCollectEntry,_Q:acPMIvrPlayCollectType,_R:acPMIvrPlayCollectInterval,'acPMIvrPlayCollectVal':acPMIvrPlayCollectVal,'acPMIvrPlayCollectInProgressTable':acPMIvrPlayCollectInProgressTable,'acPMIvrPlayCollectInProgressEntry':acPMIvrPlayCollectInProgressEntry,_S:acPMIvrPlayCollectInProgressInterval,'acPMIvrPlayCollectInProgressVal':acPMIvrPlayCollectInProgressVal,'acPMIvrPlayCollectInProgressVolume':acPMIvrPlayCollectInProgressVolume,'acPMIvrPlayCollectInProgressFullDayAverage':acPMIvrPlayCollectInProgressFullDayAverage,'acPMIvrPlayCollectDurationTable':acPMIvrPlayCollectDurationTable,'acPMIvrPlayCollectDurationEntry':acPMIvrPlayCollectDurationEntry,_T:acPMIvrPlayCollectDurationInterval,'acPMIvrPlayCollectDurationVal':acPMIvrPlayCollectDurationVal,'acPMIvrPlayCollectDurationVolume':acPMIvrPlayCollectDurationVolume,'acPMIvrPlayCollectDurationAverage':acPMIvrPlayCollectDurationAverage,'acPMIvrPlayRecordTable':acPMIvrPlayRecordTable,'acPMIvrPlayRecordEntry':acPMIvrPlayRecordEntry,_U:acPMIvrPlayRecordType,_V:acPMIvrPlayRecordInterval,'acPMIvrPlayRecordVal':acPMIvrPlayRecordVal,'acPMIvrPlayRecordInProgressTable':acPMIvrPlayRecordInProgressTable,'acPMIvrPlayRecordInProgressEntry':acPMIvrPlayRecordInProgressEntry,_W:acPMIvrPlayRecordInProgressInterval,'acPMIvrPlayRecordInProgressVal':acPMIvrPlayRecordInProgressVal,'acPMIvrPlayRecordInProgressVolume':acPMIvrPlayRecordInProgressVolume,'acPMIvrPlayRecordInProgressFullDayAverage':acPMIvrPlayRecordInProgressFullDayAverage,'acPMIvrPlayRecordDurationTable':acPMIvrPlayRecordDurationTable,'acPMIvrPlayRecordDurationEntry':acPMIvrPlayRecordDurationEntry,_X:acPMIvrPlayRecordDurationInterval,'acPMIvrPlayRecordDurationVal':acPMIvrPlayRecordDurationVal,'acPMIvrPlayRecordDurationVolume':acPMIvrPlayRecordDurationVolume,'acPMIvrPlayRecordDurationAverage':acPMIvrPlayRecordDurationAverage,'acPMIvrContDigitCollectTable':acPMIvrContDigitCollectTable,'acPMIvrContDigitCollectEntry':acPMIvrContDigitCollectEntry,_Y:acPMIvrContDigitCollectType,_Z:acPMIvrContDigitCollectInterval,'acPMIvrContDigitCollectVal':acPMIvrContDigitCollectVal,'acPMIvrContDigitCollectInProgressTable':acPMIvrContDigitCollectInProgressTable,'acPMIvrContDigitCollectInProgressEntry':acPMIvrContDigitCollectInProgressEntry,_a:acPMIvrContDigitCollectInProgressInterval,'acPMIvrContDigitCollectInProgressVal':acPMIvrContDigitCollectInProgressVal,'acPMIvrContDigitCollectInProgressVolume':acPMIvrContDigitCollectInProgressVolume,'acPMIvrContDigitCollectDurationTable':acPMIvrContDigitCollectDurationTable,'acPMIvrContDigitCollectDurationEntry':acPMIvrContDigitCollectDurationEntry,_b:acPMIvrContDigitCollectDurationInterval,'acPMIvrContDigitCollectDurationVal':acPMIvrContDigitCollectDurationVal,'acPMIvrContDigitCollectDurationVolume':acPMIvrContDigitCollectDurationVolume,'acPMIvrContDigitCollectDurationAverage':acPMIvrContDigitCollectDurationAverage,'acPMMediaServerBct':acPMMediaServerBct,'acPMBctTable':acPMBctTable,'acPMBctEntry':acPMBctEntry,_c:acPMBctType,_d:acPMBctInterval,'acPMBctVal':acPMBctVal,'acPMBctInProgressTable':acPMBctInProgressTable,'acPMBctInProgressEntry':acPMBctInProgressEntry,_e:acPMBctInProgressType,_f:acPMBctInProgressInterval,'acPMBctInProgressVal':acPMBctInProgressVal,'acPMBctInProgressVolume':acPMBctInProgressVolume,'acPMBctDurationTable':acPMBctDurationTable,'acPMBctDurationEntry':acPMBctDurationEntry,_g:acPMBctDurationInterval,'acPMBctDurationVal':acPMBctDurationVal,'acPMBctDurationVolume':acPMBctDurationVolume,'acPMBctDurationAverage':acPMBctDurationAverage,'acPMMediaServerConference':acPMMediaServerConference,'acPMConfTable':acPMConfTable,'acPMConfEntry':acPMConfEntry,_h:acPMConfType,_i:acPMConfInterval,'acPMConfVal':acPMConfVal,'acPMConfInProgressTable':acPMConfInProgressTable,'acPMConfInProgressEntry':acPMConfInProgressEntry,_j:acPMConfInProgressType,_k:acPMConfInProgressInterval,'acPMConfInProgressVal':acPMConfInProgressVal,'acPMConfInProgressVolume':acPMConfInProgressVolume,'acPMConfDurationTable':acPMConfDurationTable,'acPMConfDurationEntry':acPMConfDurationEntry,_l:acPMConfDurationInterval,'acPMConfDurationVal':acPMConfDurationVal,'acPMConfDurationVolume':acPMConfDurationVolume,'acPMConfDurationAverage':acPMConfDurationAverage,'acPMMediaServerTrunkTest':acPMMediaServerTrunkTest,'acPMTrunkTestTable':acPMTrunkTestTable,'acPMTrunkTestEntry':acPMTrunkTestEntry,_m:acPMTrunkTestType,_n:acPMTrunkTestInterval,'acPMTrunkTestVal':acPMTrunkTestVal,'acPMTrunkTestInProgressTable':acPMTrunkTestInProgressTable,'acPMTrunkTestInProgressEntry':acPMTrunkTestInProgressEntry,_o:acPMTrunkTestInProgressInterval,'acPMTrunkTestInProgressVal':acPMTrunkTestInProgressVal,'acPMTrunkTestInProgressVolume':acPMTrunkTestInProgressVolume,'acPMTrunkTestDurationTable':acPMTrunkTestDurationTable,'acPMTrunkTestDurationEntry':acPMTrunkTestDurationEntry,_p:acPMTrunkTestDurationInterval,'acPMTrunkTestDurationVal':acPMTrunkTestDurationVal,'acPMTrunkTestDurationVolume':acPMTrunkTestDurationVolume,'acPMTrunkTestDurationAverage':acPMTrunkTestDurationAverage})