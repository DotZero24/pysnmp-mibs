_S='cadSpMgtUpChannelEntry'
_R='cadSpMgtHistoryTime'
_Q='cadSpMgtHistoryUpChannelIfIndex'
_P='SpTimeOfDay'
_O='SpTriggerType'
_N='TenthdB'
_M='cadSpMgtTriggerIndex'
_L='cadSpMgtStateIndex'
_K='TruthValue'
_J='cadSpMgtGroupIndex'
_I='not-accessible'
_H='0.001 percentage'
_G='read-write'
_F='Unsigned32'
_E='CADANT-CMTS-SPECTRUM-MGMT-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadIfUpstreamChannelEntry,=mibBuilder.importSymbols('CADANT-CMTS-UPCHANNEL-MIB','cadIfUpstreamChannelEntry')
cadSpectrum,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadSpectrum')
TenthdB,=mibBuilder.importSymbols('DOCS-IF-MIB',_N)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
cadSpMgtMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,15,4))
if mibBuilder.loadTexts:cadSpMgtMib.setRevisions(('2013-04-30 00:00','2012-07-03 00:00','2012-07-02 00:00','2006-02-21 00:00','2006-02-06 00:00','2005-11-10 00:00'))
class SpTriggerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tod',1),('periodic',2),('degradation',3),('improvement',4)))
class SpTriggerDay(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('everyday',7)))
class SpTimeOfDay(TextualConvention,OctetString):status=_A;displayHint='1d:1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class Unsigned16(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CadSpMgtNotifications_ObjectIdentity=ObjectIdentity
cadSpMgtNotifications=_CadSpMgtNotifications_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,4,1))
_CadSpMgtObjects_ObjectIdentity=ObjectIdentity
cadSpMgtObjects=_CadSpMgtObjects_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,4,2))
_CadSpMgtGroup_ObjectIdentity=ObjectIdentity
cadSpMgtGroup=_CadSpMgtGroup_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,4,2,1))
_CadSpMgtGroupTable_Object=MibTable
cadSpMgtGroupTable=_CadSpMgtGroupTable_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1))
if mibBuilder.loadTexts:cadSpMgtGroupTable.setStatus(_A)
_CadSpMgtGroupEntry_Object=MibTableRow
cadSpMgtGroupEntry=_CadSpMgtGroupEntry_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1))
cadSpMgtGroupEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:cadSpMgtGroupEntry.setStatus(_A)
class _CadSpMgtGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_CadSpMgtGroupIndex_Type.__name__=_D
_CadSpMgtGroupIndex_Object=MibTableColumn
cadSpMgtGroupIndex=_CadSpMgtGroupIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,1),_CadSpMgtGroupIndex_Type())
cadSpMgtGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cadSpMgtGroupIndex.setStatus(_A)
class _CadSpMgtGroupSamplePeriod_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CadSpMgtGroupSamplePeriod_Type.__name__=_D
_CadSpMgtGroupSamplePeriod_Object=MibTableColumn
cadSpMgtGroupSamplePeriod=_CadSpMgtGroupSamplePeriod_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,2),_CadSpMgtGroupSamplePeriod_Type())
cadSpMgtGroupSamplePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtGroupSamplePeriod.setStatus(_A)
class _CadSpMgtGroupHopPeriod_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CadSpMgtGroupHopPeriod_Type.__name__=_D
_CadSpMgtGroupHopPeriod_Object=MibTableColumn
cadSpMgtGroupHopPeriod=_CadSpMgtGroupHopPeriod_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,3),_CadSpMgtGroupHopPeriod_Type())
cadSpMgtGroupHopPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtGroupHopPeriod.setStatus(_A)
class _CadSpMgtGroupCodeword_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,32768))
_CadSpMgtGroupCodeword_Type.__name__=_D
_CadSpMgtGroupCodeword_Object=MibTableColumn
cadSpMgtGroupCodeword=_CadSpMgtGroupCodeword_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,4),_CadSpMgtGroupCodeword_Type())
cadSpMgtGroupCodeword.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtGroupCodeword.setStatus(_A)
class _CadSpMgtGroupRetryPeriod_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_CadSpMgtGroupRetryPeriod_Type.__name__=_D
_CadSpMgtGroupRetryPeriod_Object=MibTableColumn
cadSpMgtGroupRetryPeriod=_CadSpMgtGroupRetryPeriod_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,5),_CadSpMgtGroupRetryPeriod_Type())
cadSpMgtGroupRetryPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtGroupRetryPeriod.setStatus(_A)
class _CadSpMgtGroupEnabled_Type(TruthValue):defaultValue=1
_CadSpMgtGroupEnabled_Type.__name__=_K
_CadSpMgtGroupEnabled_Object=MibTableColumn
cadSpMgtGroupEnabled=_CadSpMgtGroupEnabled_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,6),_CadSpMgtGroupEnabled_Type())
cadSpMgtGroupEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtGroupEnabled.setStatus(_A)
_CadSpMgtGroupRowStatus_Type=RowStatus
_CadSpMgtGroupRowStatus_Object=MibTableColumn
cadSpMgtGroupRowStatus=_CadSpMgtGroupRowStatus_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,1,1,7),_CadSpMgtGroupRowStatus_Type())
cadSpMgtGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtGroupRowStatus.setStatus(_A)
_CadSpMgtStateTable_Object=MibTable
cadSpMgtStateTable=_CadSpMgtStateTable_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2))
if mibBuilder.loadTexts:cadSpMgtStateTable.setStatus(_A)
_CadSpMgtStateEntry_Object=MibTableRow
cadSpMgtStateEntry=_CadSpMgtStateEntry_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2,1))
cadSpMgtStateEntry.setIndexNames((0,_E,_J),(0,_E,_L))
if mibBuilder.loadTexts:cadSpMgtStateEntry.setStatus(_A)
class _CadSpMgtStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CadSpMgtStateIndex_Type.__name__=_D
_CadSpMgtStateIndex_Object=MibTableColumn
cadSpMgtStateIndex=_CadSpMgtStateIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2,1,1),_CadSpMgtStateIndex_Type())
cadSpMgtStateIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cadSpMgtStateIndex.setStatus(_A)
class _CadSpMgtStateFrequency_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000000,85000000))
_CadSpMgtStateFrequency_Type.__name__=_D
_CadSpMgtStateFrequency_Object=MibTableColumn
cadSpMgtStateFrequency=_CadSpMgtStateFrequency_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2,1,2),_CadSpMgtStateFrequency_Type())
cadSpMgtStateFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtStateFrequency.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtStateFrequency.setUnits('hertz')
class _CadSpMgtStateWidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6400000))
_CadSpMgtStateWidth_Type.__name__=_D
_CadSpMgtStateWidth_Object=MibTableColumn
cadSpMgtStateWidth=_CadSpMgtStateWidth_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2,1,3),_CadSpMgtStateWidth_Type())
cadSpMgtStateWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtStateWidth.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtStateWidth.setUnits('hertz')
class _CadSpMgtStateModulationProfile_Type(Unsigned32):defaultValue=0
_CadSpMgtStateModulationProfile_Type.__name__=_F
_CadSpMgtStateModulationProfile_Object=MibTableColumn
cadSpMgtStateModulationProfile=_CadSpMgtStateModulationProfile_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2,1,4),_CadSpMgtStateModulationProfile_Type())
cadSpMgtStateModulationProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtStateModulationProfile.setStatus(_A)
_CadSpMgtStateRowStatus_Type=RowStatus
_CadSpMgtStateRowStatus_Object=MibTableColumn
cadSpMgtStateRowStatus=_CadSpMgtStateRowStatus_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,2,1,5),_CadSpMgtStateRowStatus_Type())
cadSpMgtStateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtStateRowStatus.setStatus(_A)
_CadSpMgtTriggerTable_Object=MibTable
cadSpMgtTriggerTable=_CadSpMgtTriggerTable_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3))
if mibBuilder.loadTexts:cadSpMgtTriggerTable.setStatus(_A)
_CadSpMgtTriggerEntry_Object=MibTableRow
cadSpMgtTriggerEntry=_CadSpMgtTriggerEntry_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1))
cadSpMgtTriggerEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:cadSpMgtTriggerEntry.setStatus(_A)
class _CadSpMgtTriggerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CadSpMgtTriggerIndex_Type.__name__=_D
_CadSpMgtTriggerIndex_Object=MibTableColumn
cadSpMgtTriggerIndex=_CadSpMgtTriggerIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,1),_CadSpMgtTriggerIndex_Type())
cadSpMgtTriggerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cadSpMgtTriggerIndex.setStatus(_A)
class _CadSpMgtTriggerType_Type(SpTriggerType):defaultValue=3
_CadSpMgtTriggerType_Type.__name__=_O
_CadSpMgtTriggerType_Object=MibTableColumn
cadSpMgtTriggerType=_CadSpMgtTriggerType_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,2),_CadSpMgtTriggerType_Type())
cadSpMgtTriggerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerType.setStatus(_A)
_CadSpMgtTriggerDay_Type=SpTriggerDay
_CadSpMgtTriggerDay_Object=MibTableColumn
cadSpMgtTriggerDay=_CadSpMgtTriggerDay_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,3),_CadSpMgtTriggerDay_Type())
cadSpMgtTriggerDay.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerDay.setStatus(_A)
class _CadSpMgtTriggerTOD_Type(SpTimeOfDay):defaultHexValue='000000'
_CadSpMgtTriggerTOD_Type.__name__=_P
_CadSpMgtTriggerTOD_Object=MibTableColumn
cadSpMgtTriggerTOD=_CadSpMgtTriggerTOD_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,4),_CadSpMgtTriggerTOD_Type())
cadSpMgtTriggerTOD.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerTOD.setStatus(_A)
class _CadSpMgtTriggerPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_CadSpMgtTriggerPeriod_Type.__name__=_D
_CadSpMgtTriggerPeriod_Object=MibTableColumn
cadSpMgtTriggerPeriod=_CadSpMgtTriggerPeriod_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,5),_CadSpMgtTriggerPeriod_Type())
cadSpMgtTriggerPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerPeriod.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtTriggerPeriod.setUnits('seconds')
class _CadSpMgtTriggerThres1_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CadSpMgtTriggerThres1_Type.__name__=_F
_CadSpMgtTriggerThres1_Object=MibTableColumn
cadSpMgtTriggerThres1=_CadSpMgtTriggerThres1_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,6),_CadSpMgtTriggerThres1_Type())
cadSpMgtTriggerThres1.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerThres1.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtTriggerThres1.setUnits(_H)
class _CadSpMgtTriggerThres2_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CadSpMgtTriggerThres2_Type.__name__=_F
_CadSpMgtTriggerThres2_Object=MibTableColumn
cadSpMgtTriggerThres2=_CadSpMgtTriggerThres2_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,7),_CadSpMgtTriggerThres2_Type())
cadSpMgtTriggerThres2.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerThres2.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtTriggerThres2.setUnits(_H)
class _CadSpMgtTriggerThres3_Type(TenthdB):defaultValue=1000;subtypeSpec=TenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CadSpMgtTriggerThres3_Type.__name__=_N
_CadSpMgtTriggerThres3_Object=MibTableColumn
cadSpMgtTriggerThres3=_CadSpMgtTriggerThres3_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,8),_CadSpMgtTriggerThres3_Type())
cadSpMgtTriggerThres3.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerThres3.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtTriggerThres3.setUnits('dB')
_CadSpMgtTriggerRowStatus_Type=RowStatus
_CadSpMgtTriggerRowStatus_Object=MibTableColumn
cadSpMgtTriggerRowStatus=_CadSpMgtTriggerRowStatus_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,3,1,9),_CadSpMgtTriggerRowStatus_Type())
cadSpMgtTriggerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTriggerRowStatus.setStatus(_A)
_CadSpMgtStateTransTable_Object=MibTable
cadSpMgtStateTransTable=_CadSpMgtStateTransTable_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,4))
if mibBuilder.loadTexts:cadSpMgtStateTransTable.setStatus(_A)
_CadSpMgtStateTransEntry_Object=MibTableRow
cadSpMgtStateTransEntry=_CadSpMgtStateTransEntry_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,4,1))
cadSpMgtStateTransEntry.setIndexNames((0,_E,_J),(0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:cadSpMgtStateTransEntry.setStatus(_A)
class _CadSpMgtTransNextState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CadSpMgtTransNextState_Type.__name__=_D
_CadSpMgtTransNextState_Object=MibTableColumn
cadSpMgtTransNextState=_CadSpMgtTransNextState_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,4,1,1),_CadSpMgtTransNextState_Type())
cadSpMgtTransNextState.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtTransNextState.setStatus(_A)
_CadSpMgtStateTransRowStatus_Type=RowStatus
_CadSpMgtStateTransRowStatus_Object=MibTableColumn
cadSpMgtStateTransRowStatus=_CadSpMgtStateTransRowStatus_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,4,1,2),_CadSpMgtStateTransRowStatus_Type())
cadSpMgtStateTransRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cadSpMgtStateTransRowStatus.setStatus(_A)
_CadSpMgtHistoryTable_Object=MibTable
cadSpMgtHistoryTable=_CadSpMgtHistoryTable_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5))
if mibBuilder.loadTexts:cadSpMgtHistoryTable.setStatus(_A)
_CadSpMgtHistoryEntry_Object=MibTableRow
cadSpMgtHistoryEntry=_CadSpMgtHistoryEntry_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1))
cadSpMgtHistoryEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:cadSpMgtHistoryEntry.setStatus(_A)
_CadSpMgtHistoryUpChannelIfIndex_Type=InterfaceIndex
_CadSpMgtHistoryUpChannelIfIndex_Object=MibTableColumn
cadSpMgtHistoryUpChannelIfIndex=_CadSpMgtHistoryUpChannelIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,1),_CadSpMgtHistoryUpChannelIfIndex_Type())
cadSpMgtHistoryUpChannelIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cadSpMgtHistoryUpChannelIfIndex.setStatus(_A)
_CadSpMgtHistoryTime_Type=DateAndTime
_CadSpMgtHistoryTime_Object=MibTableColumn
cadSpMgtHistoryTime=_CadSpMgtHistoryTime_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,2),_CadSpMgtHistoryTime_Type())
cadSpMgtHistoryTime.setMaxAccess(_I)
if mibBuilder.loadTexts:cadSpMgtHistoryTime.setStatus(_A)
_CadSpMgtHistoryTriggerIndex_Type=Integer32
_CadSpMgtHistoryTriggerIndex_Object=MibTableColumn
cadSpMgtHistoryTriggerIndex=_CadSpMgtHistoryTriggerIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,3),_CadSpMgtHistoryTriggerIndex_Type())
cadSpMgtHistoryTriggerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryTriggerIndex.setStatus(_A)
_CadSpMgtHistoryFromStateIndex_Type=Integer32
_CadSpMgtHistoryFromStateIndex_Object=MibTableColumn
cadSpMgtHistoryFromStateIndex=_CadSpMgtHistoryFromStateIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,4),_CadSpMgtHistoryFromStateIndex_Type())
cadSpMgtHistoryFromStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryFromStateIndex.setStatus(_A)
_CadSpMgtHistoryNextStateIndex_Type=Integer32
_CadSpMgtHistoryNextStateIndex_Object=MibTableColumn
cadSpMgtHistoryNextStateIndex=_CadSpMgtHistoryNextStateIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,5),_CadSpMgtHistoryNextStateIndex_Type())
cadSpMgtHistoryNextStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryNextStateIndex.setStatus(_A)
_CadSpMgtHistoryResultStateIndex_Type=Integer32
_CadSpMgtHistoryResultStateIndex_Object=MibTableColumn
cadSpMgtHistoryResultStateIndex=_CadSpMgtHistoryResultStateIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,6),_CadSpMgtHistoryResultStateIndex_Type())
cadSpMgtHistoryResultStateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryResultStateIndex.setStatus(_A)
_CadSpMgtHistorySNR_Type=TenthdB
_CadSpMgtHistorySNR_Object=MibTableColumn
cadSpMgtHistorySNR=_CadSpMgtHistorySNR_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,7),_CadSpMgtHistorySNR_Type())
cadSpMgtHistorySNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistorySNR.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtHistorySNR.setUnits('dB')
class _CadSpMgtHistoryUFecError_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CadSpMgtHistoryUFecError_Type.__name__=_F
_CadSpMgtHistoryUFecError_Object=MibTableColumn
cadSpMgtHistoryUFecError=_CadSpMgtHistoryUFecError_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,8),_CadSpMgtHistoryUFecError_Type())
cadSpMgtHistoryUFecError.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryUFecError.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtHistoryUFecError.setUnits(_H)
class _CadSpMgtHistoryFecError_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CadSpMgtHistoryFecError_Type.__name__=_F
_CadSpMgtHistoryFecError_Object=MibTableColumn
cadSpMgtHistoryFecError=_CadSpMgtHistoryFecError_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,9),_CadSpMgtHistoryFecError_Type())
cadSpMgtHistoryFecError.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryFecError.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtHistoryFecError.setUnits(_H)
class _CadSpMgtHistorySpareCardId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_CadSpMgtHistorySpareCardId_Type.__name__=_D
_CadSpMgtHistorySpareCardId_Object=MibTableColumn
cadSpMgtHistorySpareCardId=_CadSpMgtHistorySpareCardId_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,10),_CadSpMgtHistorySpareCardId_Type())
cadSpMgtHistorySpareCardId.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistorySpareCardId.setStatus(_A)
_CadSpMgtHistoryText_Type=DisplayString
_CadSpMgtHistoryText_Object=MibTableColumn
cadSpMgtHistoryText=_CadSpMgtHistoryText_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,11),_CadSpMgtHistoryText_Type())
cadSpMgtHistoryText.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryText.setStatus(_A)
_CadSpMgtHistoryGroupId_Type=Integer32
_CadSpMgtHistoryGroupId_Object=MibTableColumn
cadSpMgtHistoryGroupId=_CadSpMgtHistoryGroupId_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,12),_CadSpMgtHistoryGroupId_Type())
cadSpMgtHistoryGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryGroupId.setStatus(_A)
_CadSpMgtHistoryStateChangeCount_Type=Unsigned16
_CadSpMgtHistoryStateChangeCount_Object=MibTableColumn
cadSpMgtHistoryStateChangeCount=_CadSpMgtHistoryStateChangeCount_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,13),_CadSpMgtHistoryStateChangeCount_Type())
cadSpMgtHistoryStateChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistoryStateChangeCount.setStatus(_A)
_CadSpMgtHistorySysUpTime_Type=Unsigned32
_CadSpMgtHistorySysUpTime_Object=MibTableColumn
cadSpMgtHistorySysUpTime=_CadSpMgtHistorySysUpTime_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,5,1,14),_CadSpMgtHistorySysUpTime_Type())
cadSpMgtHistorySysUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtHistorySysUpTime.setStatus(_A)
_CadSpMgtUpChannelTable_Object=MibTable
cadSpMgtUpChannelTable=_CadSpMgtUpChannelTable_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,6))
if mibBuilder.loadTexts:cadSpMgtUpChannelTable.setStatus(_A)
_CadSpMgtUpChannelEntry_Object=MibTableRow
cadSpMgtUpChannelEntry=_CadSpMgtUpChannelEntry_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,6,1))
if mibBuilder.loadTexts:cadSpMgtUpChannelEntry.setStatus(_A)
_CadSpMgtUpChannelCurrState_Type=Integer32
_CadSpMgtUpChannelCurrState_Object=MibTableColumn
cadSpMgtUpChannelCurrState=_CadSpMgtUpChannelCurrState_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,6,1,1),_CadSpMgtUpChannelCurrState_Type())
cadSpMgtUpChannelCurrState.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtUpChannelCurrState.setStatus(_A)
_CadSpMgtUpChannelStateTransTime_Type=DateAndTime
_CadSpMgtUpChannelStateTransTime_Object=MibTableColumn
cadSpMgtUpChannelStateTransTime=_CadSpMgtUpChannelStateTransTime_Object((1,3,6,1,4,1,4998,1,1,15,4,2,1,6,1,2),_CadSpMgtUpChannelStateTransTime_Type())
cadSpMgtUpChannelStateTransTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cadSpMgtUpChannelStateTransTime.setStatus(_A)
_CadSpMgtRequests_ObjectIdentity=ObjectIdentity
cadSpMgtRequests=_CadSpMgtRequests_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,4,2,2))
_CadSpMgtRequestUpChannelIfIndex_Type=InterfaceIndex
_CadSpMgtRequestUpChannelIfIndex_Object=MibScalar
cadSpMgtRequestUpChannelIfIndex=_CadSpMgtRequestUpChannelIfIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,1),_CadSpMgtRequestUpChannelIfIndex_Type())
cadSpMgtRequestUpChannelIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestUpChannelIfIndex.setStatus(_A)
_CadSpMgtRequestTriggerIndex_Type=Integer32
_CadSpMgtRequestTriggerIndex_Object=MibScalar
cadSpMgtRequestTriggerIndex=_CadSpMgtRequestTriggerIndex_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,2),_CadSpMgtRequestTriggerIndex_Type())
cadSpMgtRequestTriggerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestTriggerIndex.setStatus(_A)
_CadSpMgtRequestNextState_Type=Integer32
_CadSpMgtRequestNextState_Object=MibScalar
cadSpMgtRequestNextState=_CadSpMgtRequestNextState_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,3),_CadSpMgtRequestNextState_Type())
cadSpMgtRequestNextState.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestNextState.setStatus(_A)
_CadSpMgtRequestSNR_Type=TenthdB
_CadSpMgtRequestSNR_Object=MibScalar
cadSpMgtRequestSNR=_CadSpMgtRequestSNR_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,4),_CadSpMgtRequestSNR_Type())
cadSpMgtRequestSNR.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestSNR.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtRequestSNR.setUnits('dB')
class _CadSpMgtRequestUFecError_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CadSpMgtRequestUFecError_Type.__name__=_F
_CadSpMgtRequestUFecError_Object=MibScalar
cadSpMgtRequestUFecError=_CadSpMgtRequestUFecError_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,5),_CadSpMgtRequestUFecError_Type())
cadSpMgtRequestUFecError.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestUFecError.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtRequestUFecError.setUnits(_H)
class _CadSpMgtRequestFecError_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CadSpMgtRequestFecError_Type.__name__=_F
_CadSpMgtRequestFecError_Object=MibScalar
cadSpMgtRequestFecError=_CadSpMgtRequestFecError_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,6),_CadSpMgtRequestFecError_Type())
cadSpMgtRequestFecError.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestFecError.setStatus(_A)
if mibBuilder.loadTexts:cadSpMgtRequestFecError.setUnits(_H)
class _CadSpMgtRequestCommit_Type(TruthValue):defaultValue=2
_CadSpMgtRequestCommit_Type.__name__=_K
_CadSpMgtRequestCommit_Object=MibScalar
cadSpMgtRequestCommit=_CadSpMgtRequestCommit_Object((1,3,6,1,4,1,4998,1,1,15,4,2,2,7),_CadSpMgtRequestCommit_Type())
cadSpMgtRequestCommit.setMaxAccess(_G)
if mibBuilder.loadTexts:cadSpMgtRequestCommit.setStatus(_A)
_CadSpMgtConformance_ObjectIdentity=ObjectIdentity
cadSpMgtConformance=_CadSpMgtConformance_ObjectIdentity((1,3,6,1,4,1,4998,1,1,15,4,3))
cadIfUpstreamChannelEntry.registerAugmentions((_E,_S))
cadSpMgtUpChannelEntry.setIndexNames(*cadIfUpstreamChannelEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_O:SpTriggerType,'SpTriggerDay':SpTriggerDay,_P:SpTimeOfDay,'Unsigned16':Unsigned16,'cadSpMgtMib':cadSpMgtMib,'cadSpMgtNotifications':cadSpMgtNotifications,'cadSpMgtObjects':cadSpMgtObjects,'cadSpMgtGroup':cadSpMgtGroup,'cadSpMgtGroupTable':cadSpMgtGroupTable,'cadSpMgtGroupEntry':cadSpMgtGroupEntry,_J:cadSpMgtGroupIndex,'cadSpMgtGroupSamplePeriod':cadSpMgtGroupSamplePeriod,'cadSpMgtGroupHopPeriod':cadSpMgtGroupHopPeriod,'cadSpMgtGroupCodeword':cadSpMgtGroupCodeword,'cadSpMgtGroupRetryPeriod':cadSpMgtGroupRetryPeriod,'cadSpMgtGroupEnabled':cadSpMgtGroupEnabled,'cadSpMgtGroupRowStatus':cadSpMgtGroupRowStatus,'cadSpMgtStateTable':cadSpMgtStateTable,'cadSpMgtStateEntry':cadSpMgtStateEntry,_L:cadSpMgtStateIndex,'cadSpMgtStateFrequency':cadSpMgtStateFrequency,'cadSpMgtStateWidth':cadSpMgtStateWidth,'cadSpMgtStateModulationProfile':cadSpMgtStateModulationProfile,'cadSpMgtStateRowStatus':cadSpMgtStateRowStatus,'cadSpMgtTriggerTable':cadSpMgtTriggerTable,'cadSpMgtTriggerEntry':cadSpMgtTriggerEntry,_M:cadSpMgtTriggerIndex,'cadSpMgtTriggerType':cadSpMgtTriggerType,'cadSpMgtTriggerDay':cadSpMgtTriggerDay,'cadSpMgtTriggerTOD':cadSpMgtTriggerTOD,'cadSpMgtTriggerPeriod':cadSpMgtTriggerPeriod,'cadSpMgtTriggerThres1':cadSpMgtTriggerThres1,'cadSpMgtTriggerThres2':cadSpMgtTriggerThres2,'cadSpMgtTriggerThres3':cadSpMgtTriggerThres3,'cadSpMgtTriggerRowStatus':cadSpMgtTriggerRowStatus,'cadSpMgtStateTransTable':cadSpMgtStateTransTable,'cadSpMgtStateTransEntry':cadSpMgtStateTransEntry,'cadSpMgtTransNextState':cadSpMgtTransNextState,'cadSpMgtStateTransRowStatus':cadSpMgtStateTransRowStatus,'cadSpMgtHistoryTable':cadSpMgtHistoryTable,'cadSpMgtHistoryEntry':cadSpMgtHistoryEntry,_Q:cadSpMgtHistoryUpChannelIfIndex,_R:cadSpMgtHistoryTime,'cadSpMgtHistoryTriggerIndex':cadSpMgtHistoryTriggerIndex,'cadSpMgtHistoryFromStateIndex':cadSpMgtHistoryFromStateIndex,'cadSpMgtHistoryNextStateIndex':cadSpMgtHistoryNextStateIndex,'cadSpMgtHistoryResultStateIndex':cadSpMgtHistoryResultStateIndex,'cadSpMgtHistorySNR':cadSpMgtHistorySNR,'cadSpMgtHistoryUFecError':cadSpMgtHistoryUFecError,'cadSpMgtHistoryFecError':cadSpMgtHistoryFecError,'cadSpMgtHistorySpareCardId':cadSpMgtHistorySpareCardId,'cadSpMgtHistoryText':cadSpMgtHistoryText,'cadSpMgtHistoryGroupId':cadSpMgtHistoryGroupId,'cadSpMgtHistoryStateChangeCount':cadSpMgtHistoryStateChangeCount,'cadSpMgtHistorySysUpTime':cadSpMgtHistorySysUpTime,'cadSpMgtUpChannelTable':cadSpMgtUpChannelTable,_S:cadSpMgtUpChannelEntry,'cadSpMgtUpChannelCurrState':cadSpMgtUpChannelCurrState,'cadSpMgtUpChannelStateTransTime':cadSpMgtUpChannelStateTransTime,'cadSpMgtRequests':cadSpMgtRequests,'cadSpMgtRequestUpChannelIfIndex':cadSpMgtRequestUpChannelIfIndex,'cadSpMgtRequestTriggerIndex':cadSpMgtRequestTriggerIndex,'cadSpMgtRequestNextState':cadSpMgtRequestNextState,'cadSpMgtRequestSNR':cadSpMgtRequestSNR,'cadSpMgtRequestUFecError':cadSpMgtRequestUFecError,'cadSpMgtRequestFecError':cadSpMgtRequestFecError,'cadSpMgtRequestCommit':cadSpMgtRequestCommit,'cadSpMgtConformance':cadSpMgtConformance})