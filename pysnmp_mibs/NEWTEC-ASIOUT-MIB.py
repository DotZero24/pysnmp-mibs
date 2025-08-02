_X='ntcAsiOutConfGrpV1Standard'
_W='ntcAsiOutAlmNoOutputSignalAsi2'
_V='ntcAsiOutAlmNoOutputSignalAsi1'
_U='ntcAsiOutAlmNoOutputSignal'
_T='ntcAsiOutAlmGeneralAsiOutput'
_S='ntcAsiOutNcrGenOutputTsBitRate'
_R='ntcAsiOutPrbsGenNumberNullPkt'
_Q='ntcAsiOutPrbsGenNumberDataPkt'
_P='ntcAsiOutPrbsGenPidValue'
_O='ntcAsiOutPrbsGenPidHandling'
_N='ntcAsiOutPrbsGenType'
_M='ntcAsiOutPrbsGenOutputTsBitRate'
_L='ntcAsiOutMeasuredTsBitRate'
_K='ntcAsiOutOutputSelection'
_J='ntcAsiOutInputSelection'
_I='NtcPid'
_H='NtcEnable'
_G='bps'
_F='Integer32'
_E='read-only'
_D='Unsigned32'
_C='read-write'
_B='NEWTEC-ASIOUT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable,NtcPid=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcAsiOut=ModuleIdentity((1,3,6,1,4,1,5835,5,2,900))
if mibBuilder.loadTexts:ntcAsiOut.setRevisions(('2014-09-09 09:00','2013-03-27 10:00','2012-06-28 12:00'))
_NtcAsiOutObjects_ObjectIdentity=ObjectIdentity
ntcAsiOutObjects=_NtcAsiOutObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,1))
if mibBuilder.loadTexts:ntcAsiOutObjects.setStatus(_A)
class _NtcAsiOutInputSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,100,101)));namedValues=NamedValues(*(('none',0),('modulatorinput',2),('activeinput',3),('nonactiveinput',4),('demod',5),('prbsgenerator',100),('ncrstream',101)))
_NtcAsiOutInputSelection_Type.__name__=_F
_NtcAsiOutInputSelection_Object=MibScalar
ntcAsiOutInputSelection=_NtcAsiOutInputSelection_Object((1,3,6,1,4,1,5835,5,2,900,1,1),_NtcAsiOutInputSelection_Type())
ntcAsiOutInputSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutInputSelection.setStatus(_A)
class _NtcAsiOutOutputSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,40)));namedValues=NamedValues(*(('none',0),('asi1',1),('asi2',2),('asi1and2',40)))
_NtcAsiOutOutputSelection_Type.__name__=_F
_NtcAsiOutOutputSelection_Object=MibScalar
ntcAsiOutOutputSelection=_NtcAsiOutOutputSelection_Object((1,3,6,1,4,1,5835,5,2,900,1,2),_NtcAsiOutOutputSelection_Type())
ntcAsiOutOutputSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutOutputSelection.setStatus(_A)
_NtcAsiOutMeasuredTsBitRate_Type=Unsigned32
_NtcAsiOutMeasuredTsBitRate_Object=MibScalar
ntcAsiOutMeasuredTsBitRate=_NtcAsiOutMeasuredTsBitRate_Object((1,3,6,1,4,1,5835,5,2,900,1,3),_NtcAsiOutMeasuredTsBitRate_Type())
ntcAsiOutMeasuredTsBitRate.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAsiOutMeasuredTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiOutMeasuredTsBitRate.setUnits(_G)
_NtcAsiOutPrbsGenerator_ObjectIdentity=ObjectIdentity
ntcAsiOutPrbsGenerator=_NtcAsiOutPrbsGenerator_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,1,4))
if mibBuilder.loadTexts:ntcAsiOutPrbsGenerator.setStatus(_A)
class _NtcAsiOutPrbsGenOutputTsBitRate_Type(Unsigned32):defaultValue=1000000
_NtcAsiOutPrbsGenOutputTsBitRate_Type.__name__=_D
_NtcAsiOutPrbsGenOutputTsBitRate_Object=MibScalar
ntcAsiOutPrbsGenOutputTsBitRate=_NtcAsiOutPrbsGenOutputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,900,1,4,1),_NtcAsiOutPrbsGenOutputTsBitRate_Type())
ntcAsiOutPrbsGenOutputTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenOutputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenOutputTsBitRate.setUnits(_G)
class _NtcAsiOutPrbsGenType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('prbs',0),('counter',1)))
_NtcAsiOutPrbsGenType_Type.__name__=_F
_NtcAsiOutPrbsGenType_Object=MibScalar
ntcAsiOutPrbsGenType=_NtcAsiOutPrbsGenType_Object((1,3,6,1,4,1,5835,5,2,900,1,4,2),_NtcAsiOutPrbsGenType_Type())
ntcAsiOutPrbsGenType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenType.setStatus(_A)
class _NtcAsiOutPrbsGenPidHandling_Type(NtcEnable):defaultValue=0
_NtcAsiOutPrbsGenPidHandling_Type.__name__=_H
_NtcAsiOutPrbsGenPidHandling_Object=MibScalar
ntcAsiOutPrbsGenPidHandling=_NtcAsiOutPrbsGenPidHandling_Object((1,3,6,1,4,1,5835,5,2,900,1,4,3),_NtcAsiOutPrbsGenPidHandling_Type())
ntcAsiOutPrbsGenPidHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenPidHandling.setStatus(_A)
class _NtcAsiOutPrbsGenPidValue_Type(NtcPid):defaultValue=1
_NtcAsiOutPrbsGenPidValue_Type.__name__=_I
_NtcAsiOutPrbsGenPidValue_Object=MibScalar
ntcAsiOutPrbsGenPidValue=_NtcAsiOutPrbsGenPidValue_Object((1,3,6,1,4,1,5835,5,2,900,1,4,4),_NtcAsiOutPrbsGenPidValue_Type())
ntcAsiOutPrbsGenPidValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenPidValue.setStatus(_A)
class _NtcAsiOutPrbsGenNumberDataPkt_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NtcAsiOutPrbsGenNumberDataPkt_Type.__name__=_D
_NtcAsiOutPrbsGenNumberDataPkt_Object=MibScalar
ntcAsiOutPrbsGenNumberDataPkt=_NtcAsiOutPrbsGenNumberDataPkt_Object((1,3,6,1,4,1,5835,5,2,900,1,4,5),_NtcAsiOutPrbsGenNumberDataPkt_Type())
ntcAsiOutPrbsGenNumberDataPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenNumberDataPkt.setStatus(_A)
class _NtcAsiOutPrbsGenNumberNullPkt_Type(Unsigned32):defaultValue=0
_NtcAsiOutPrbsGenNumberNullPkt_Type.__name__=_D
_NtcAsiOutPrbsGenNumberNullPkt_Object=MibScalar
ntcAsiOutPrbsGenNumberNullPkt=_NtcAsiOutPrbsGenNumberNullPkt_Object((1,3,6,1,4,1,5835,5,2,900,1,4,6),_NtcAsiOutPrbsGenNumberNullPkt_Type())
ntcAsiOutPrbsGenNumberNullPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutPrbsGenNumberNullPkt.setStatus(_A)
_NtcAsiOutNcrGenerator_ObjectIdentity=ObjectIdentity
ntcAsiOutNcrGenerator=_NtcAsiOutNcrGenerator_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,1,5))
if mibBuilder.loadTexts:ntcAsiOutNcrGenerator.setStatus(_A)
class _NtcAsiOutNcrGenOutputTsBitRate_Type(Unsigned32):defaultValue=1000000
_NtcAsiOutNcrGenOutputTsBitRate_Type.__name__=_D
_NtcAsiOutNcrGenOutputTsBitRate_Object=MibScalar
ntcAsiOutNcrGenOutputTsBitRate=_NtcAsiOutNcrGenOutputTsBitRate_Object((1,3,6,1,4,1,5835,5,2,900,1,5,1),_NtcAsiOutNcrGenOutputTsBitRate_Type())
ntcAsiOutNcrGenOutputTsBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAsiOutNcrGenOutputTsBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcAsiOutNcrGenOutputTsBitRate.setUnits(_G)
_NtcAsiOutAlarm_ObjectIdentity=ObjectIdentity
ntcAsiOutAlarm=_NtcAsiOutAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,1,6))
if mibBuilder.loadTexts:ntcAsiOutAlarm.setStatus(_A)
_NtcAsiOutAlmGeneralAsiOutput_Type=NtcAlarmState
_NtcAsiOutAlmGeneralAsiOutput_Object=MibScalar
ntcAsiOutAlmGeneralAsiOutput=_NtcAsiOutAlmGeneralAsiOutput_Object((1,3,6,1,4,1,5835,5,2,900,1,6,1),_NtcAsiOutAlmGeneralAsiOutput_Type())
ntcAsiOutAlmGeneralAsiOutput.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAsiOutAlmGeneralAsiOutput.setStatus(_A)
_NtcAsiOutAlmNoOutputSignal_Type=NtcAlarmState
_NtcAsiOutAlmNoOutputSignal_Object=MibScalar
ntcAsiOutAlmNoOutputSignal=_NtcAsiOutAlmNoOutputSignal_Object((1,3,6,1,4,1,5835,5,2,900,1,6,2),_NtcAsiOutAlmNoOutputSignal_Type())
ntcAsiOutAlmNoOutputSignal.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAsiOutAlmNoOutputSignal.setStatus(_A)
_NtcAsiOutAlmNoOutputSignalAsi1_Type=NtcAlarmState
_NtcAsiOutAlmNoOutputSignalAsi1_Object=MibScalar
ntcAsiOutAlmNoOutputSignalAsi1=_NtcAsiOutAlmNoOutputSignalAsi1_Object((1,3,6,1,4,1,5835,5,2,900,1,6,3),_NtcAsiOutAlmNoOutputSignalAsi1_Type())
ntcAsiOutAlmNoOutputSignalAsi1.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAsiOutAlmNoOutputSignalAsi1.setStatus(_A)
_NtcAsiOutAlmNoOutputSignalAsi2_Type=NtcAlarmState
_NtcAsiOutAlmNoOutputSignalAsi2_Object=MibScalar
ntcAsiOutAlmNoOutputSignalAsi2=_NtcAsiOutAlmNoOutputSignalAsi2_Object((1,3,6,1,4,1,5835,5,2,900,1,6,4),_NtcAsiOutAlmNoOutputSignalAsi2_Type())
ntcAsiOutAlmNoOutputSignalAsi2.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAsiOutAlmNoOutputSignalAsi2.setStatus(_A)
_NtcAsiOutConformance_ObjectIdentity=ObjectIdentity
ntcAsiOutConformance=_NtcAsiOutConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,2))
if mibBuilder.loadTexts:ntcAsiOutConformance.setStatus(_A)
_NtcAsiOutConfCompliance_ObjectIdentity=ObjectIdentity
ntcAsiOutConfCompliance=_NtcAsiOutConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,2,1))
if mibBuilder.loadTexts:ntcAsiOutConfCompliance.setStatus(_A)
_NtcAsiOutConfGroup_ObjectIdentity=ObjectIdentity
ntcAsiOutConfGroup=_NtcAsiOutConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,900,2,2))
if mibBuilder.loadTexts:ntcAsiOutConfGroup.setStatus(_A)
ntcAsiOutConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,900,2,2,1))
ntcAsiOutConfGrpV1Standard.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ntcAsiOutConfGrpV1Standard.setStatus(_A)
ntcAsiOutConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,900,2,1,1))
ntcAsiOutConfCompV1Standard.setObjects((_B,_X))
if mibBuilder.loadTexts:ntcAsiOutConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAsiOut':ntcAsiOut,'ntcAsiOutObjects':ntcAsiOutObjects,_J:ntcAsiOutInputSelection,_K:ntcAsiOutOutputSelection,_L:ntcAsiOutMeasuredTsBitRate,'ntcAsiOutPrbsGenerator':ntcAsiOutPrbsGenerator,_M:ntcAsiOutPrbsGenOutputTsBitRate,_N:ntcAsiOutPrbsGenType,_O:ntcAsiOutPrbsGenPidHandling,_P:ntcAsiOutPrbsGenPidValue,_Q:ntcAsiOutPrbsGenNumberDataPkt,_R:ntcAsiOutPrbsGenNumberNullPkt,'ntcAsiOutNcrGenerator':ntcAsiOutNcrGenerator,_S:ntcAsiOutNcrGenOutputTsBitRate,'ntcAsiOutAlarm':ntcAsiOutAlarm,_T:ntcAsiOutAlmGeneralAsiOutput,_U:ntcAsiOutAlmNoOutputSignal,_V:ntcAsiOutAlmNoOutputSignalAsi1,_W:ntcAsiOutAlmNoOutputSignalAsi2,'ntcAsiOutConformance':ntcAsiOutConformance,'ntcAsiOutConfCompliance':ntcAsiOutConfCompliance,'ntcAsiOutConfCompV1Standard':ntcAsiOutConfCompV1Standard,'ntcAsiOutConfGroup':ntcAsiOutConfGroup,_X:ntcAsiOutConfGrpV1Standard})