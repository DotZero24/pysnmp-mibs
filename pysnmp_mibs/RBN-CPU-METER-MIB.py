_W='rbnCpuMeterStatsGroup2'
_V='rbnCpuProcLongest'
_U='rbnCpuProc5Min'
_T='rbnCpuProc1Min'
_S='rbnCpuProc5Sec'
_R='rbnCpuProcCalls'
_Q='rbnCpuProcTime'
_P='rbnCpuProcPriority'
_O='rbnCpuMeterFiveMinutePeak'
_N='rbnCpuMeterOneMinutePeak'
_M='rbnCpuMeterFiveSecondPeak'
_L='DisplayString'
_K='Unsigned32'
_J='rbnCpuProcGroup'
_I='rbnCpuMeterStatsGroup'
_H='rbnCpuMeterFiveMinuteAvg'
_G='rbnCpuMeterOneMinuteAvg'
_F='rbnCpuMeterFiveSecondAvg'
_E='rbnCpuProcName'
_D='deprecated'
_C='read-only'
_B='current'
_A='RBN-CPU-METER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnPercentage,=mibBuilder.importSymbols('RBN-TC','RbnPercentage')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
rbnCpuMeterMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,6))
if mibBuilder.loadTexts:rbnCpuMeterMIB.setRevisions(('2011-12-13 18:00','2011-01-19 18:00','2002-12-16 00:00','2002-06-26 00:00','2002-05-29 00:00','1999-06-16 23:00'))
class Percentage(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RbnCpuMeterMIBObjects_ObjectIdentity=ObjectIdentity
rbnCpuMeterMIBObjects=_RbnCpuMeterMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,6,1))
_RbnCpuMeterFiveSecondAvg_Type=RbnPercentage
_RbnCpuMeterFiveSecondAvg_Object=MibScalar
rbnCpuMeterFiveSecondAvg=_RbnCpuMeterFiveSecondAvg_Object((1,3,6,1,4,1,2352,2,6,1,1),_RbnCpuMeterFiveSecondAvg_Type())
rbnCpuMeterFiveSecondAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuMeterFiveSecondAvg.setStatus(_B)
_RbnCpuMeterOneMinuteAvg_Type=RbnPercentage
_RbnCpuMeterOneMinuteAvg_Object=MibScalar
rbnCpuMeterOneMinuteAvg=_RbnCpuMeterOneMinuteAvg_Object((1,3,6,1,4,1,2352,2,6,1,2),_RbnCpuMeterOneMinuteAvg_Type())
rbnCpuMeterOneMinuteAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuMeterOneMinuteAvg.setStatus(_B)
_RbnCpuMeterFiveMinuteAvg_Type=RbnPercentage
_RbnCpuMeterFiveMinuteAvg_Object=MibScalar
rbnCpuMeterFiveMinuteAvg=_RbnCpuMeterFiveMinuteAvg_Object((1,3,6,1,4,1,2352,2,6,1,3),_RbnCpuMeterFiveMinuteAvg_Type())
rbnCpuMeterFiveMinuteAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuMeterFiveMinuteAvg.setStatus(_B)
_RbnCpuMeterFiveSecondPeak_Type=RbnPercentage
_RbnCpuMeterFiveSecondPeak_Object=MibScalar
rbnCpuMeterFiveSecondPeak=_RbnCpuMeterFiveSecondPeak_Object((1,3,6,1,4,1,2352,2,6,1,4),_RbnCpuMeterFiveSecondPeak_Type())
rbnCpuMeterFiveSecondPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuMeterFiveSecondPeak.setStatus(_B)
_RbnCpuMeterOneMinutePeak_Type=RbnPercentage
_RbnCpuMeterOneMinutePeak_Object=MibScalar
rbnCpuMeterOneMinutePeak=_RbnCpuMeterOneMinutePeak_Object((1,3,6,1,4,1,2352,2,6,1,5),_RbnCpuMeterOneMinutePeak_Type())
rbnCpuMeterOneMinutePeak.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuMeterOneMinutePeak.setStatus(_B)
_RbnCpuMeterFiveMinutePeak_Type=RbnPercentage
_RbnCpuMeterFiveMinutePeak_Object=MibScalar
rbnCpuMeterFiveMinutePeak=_RbnCpuMeterFiveMinutePeak_Object((1,3,6,1,4,1,2352,2,6,1,6),_RbnCpuMeterFiveMinutePeak_Type())
rbnCpuMeterFiveMinutePeak.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuMeterFiveMinutePeak.setStatus(_B)
_RbnCpuMeterMIBConformance_ObjectIdentity=ObjectIdentity
rbnCpuMeterMIBConformance=_RbnCpuMeterMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,6,2))
_RbnCpuMeterMIBGroups_ObjectIdentity=ObjectIdentity
rbnCpuMeterMIBGroups=_RbnCpuMeterMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,6,2,1))
_RbnCpuMeterMIBCompliances_ObjectIdentity=ObjectIdentity
rbnCpuMeterMIBCompliances=_RbnCpuMeterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,6,2,2))
_RbnCpuProcGroups_ObjectIdentity=ObjectIdentity
rbnCpuProcGroups=_RbnCpuProcGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,6,2,3))
_RbnCpuProcMIBObjects_ObjectIdentity=ObjectIdentity
rbnCpuProcMIBObjects=_RbnCpuProcMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,6,3))
_RbnCpuProcTable_Object=MibTable
rbnCpuProcTable=_RbnCpuProcTable_Object((1,3,6,1,4,1,2352,2,6,3,1))
if mibBuilder.loadTexts:rbnCpuProcTable.setStatus(_B)
_RbnCpuProcEntry_Object=MibTableRow
rbnCpuProcEntry=_RbnCpuProcEntry_Object((1,3,6,1,4,1,2352,2,6,3,1,1))
rbnCpuProcEntry.setIndexNames((1,_A,_E))
if mibBuilder.loadTexts:rbnCpuProcEntry.setStatus(_B)
class _RbnCpuProcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,114))
_RbnCpuProcName_Type.__name__=_L
_RbnCpuProcName_Object=MibTableColumn
rbnCpuProcName=_RbnCpuProcName_Object((1,3,6,1,4,1,2352,2,6,3,1,1,1),_RbnCpuProcName_Type())
rbnCpuProcName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProcName.setStatus(_B)
class _RbnCpuProcPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RbnCpuProcPriority_Type.__name__=_K
_RbnCpuProcPriority_Object=MibTableColumn
rbnCpuProcPriority=_RbnCpuProcPriority_Object((1,3,6,1,4,1,2352,2,6,3,1,1,2),_RbnCpuProcPriority_Type())
rbnCpuProcPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProcPriority.setStatus(_B)
_RbnCpuProcTime_Type=Counter32
_RbnCpuProcTime_Object=MibTableColumn
rbnCpuProcTime=_RbnCpuProcTime_Object((1,3,6,1,4,1,2352,2,6,3,1,1,3),_RbnCpuProcTime_Type())
rbnCpuProcTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProcTime.setStatus(_B)
_RbnCpuProcCalls_Type=Counter32
_RbnCpuProcCalls_Object=MibTableColumn
rbnCpuProcCalls=_RbnCpuProcCalls_Object((1,3,6,1,4,1,2352,2,6,3,1,1,4),_RbnCpuProcCalls_Type())
rbnCpuProcCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProcCalls.setStatus(_B)
_RbnCpuProc5Sec_Type=RbnPercentage
_RbnCpuProc5Sec_Object=MibTableColumn
rbnCpuProc5Sec=_RbnCpuProc5Sec_Object((1,3,6,1,4,1,2352,2,6,3,1,1,5),_RbnCpuProc5Sec_Type())
rbnCpuProc5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProc5Sec.setStatus(_B)
_RbnCpuProc1Min_Type=RbnPercentage
_RbnCpuProc1Min_Object=MibTableColumn
rbnCpuProc1Min=_RbnCpuProc1Min_Object((1,3,6,1,4,1,2352,2,6,3,1,1,6),_RbnCpuProc1Min_Type())
rbnCpuProc1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProc1Min.setStatus(_B)
_RbnCpuProc5Min_Type=RbnPercentage
_RbnCpuProc5Min_Object=MibTableColumn
rbnCpuProc5Min=_RbnCpuProc5Min_Object((1,3,6,1,4,1,2352,2,6,3,1,1,7),_RbnCpuProc5Min_Type())
rbnCpuProc5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProc5Min.setStatus(_B)
_RbnCpuProcLongest_Type=Gauge32
_RbnCpuProcLongest_Object=MibTableColumn
rbnCpuProcLongest=_RbnCpuProcLongest_Object((1,3,6,1,4,1,2352,2,6,3,1,1,8),_RbnCpuProcLongest_Type())
rbnCpuProcLongest.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuProcLongest.setStatus(_B)
rbnCpuMeterStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,6,2,1,1))
rbnCpuMeterStatsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:rbnCpuMeterStatsGroup.setStatus(_D)
rbnCpuMeterStatsGroup2=ObjectGroup((1,3,6,1,4,1,2352,2,6,2,1,2))
rbnCpuMeterStatsGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:rbnCpuMeterStatsGroup2.setStatus(_B)
rbnCpuProcGroup=ObjectGroup((1,3,6,1,4,1,2352,2,6,2,3,1))
rbnCpuProcGroup.setObjects(*((_A,_E),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:rbnCpuProcGroup.setStatus(_B)
rbnCpuMeterMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,6,2,2,1))
rbnCpuMeterMIBCompliance.setObjects((_A,_I))
if mibBuilder.loadTexts:rbnCpuMeterMIBCompliance.setStatus(_D)
rbnCpuMeterMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,2352,2,6,2,2,2))
rbnCpuMeterMIBCompliance1.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbnCpuMeterMIBCompliance1.setStatus(_D)
rbnCpuMeterMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,6,2,2,3))
rbnCpuMeterMIBCompliance2.setObjects(*((_A,_W),(_A,_J)))
if mibBuilder.loadTexts:rbnCpuMeterMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'Percentage':Percentage,'rbnCpuMeterMIB':rbnCpuMeterMIB,'rbnCpuMeterMIBObjects':rbnCpuMeterMIBObjects,_F:rbnCpuMeterFiveSecondAvg,_G:rbnCpuMeterOneMinuteAvg,_H:rbnCpuMeterFiveMinuteAvg,_M:rbnCpuMeterFiveSecondPeak,_N:rbnCpuMeterOneMinutePeak,_O:rbnCpuMeterFiveMinutePeak,'rbnCpuMeterMIBConformance':rbnCpuMeterMIBConformance,'rbnCpuMeterMIBGroups':rbnCpuMeterMIBGroups,_I:rbnCpuMeterStatsGroup,_W:rbnCpuMeterStatsGroup2,'rbnCpuMeterMIBCompliances':rbnCpuMeterMIBCompliances,'rbnCpuMeterMIBCompliance':rbnCpuMeterMIBCompliance,'rbnCpuMeterMIBCompliance1':rbnCpuMeterMIBCompliance1,'rbnCpuMeterMIBCompliance2':rbnCpuMeterMIBCompliance2,'rbnCpuProcGroups':rbnCpuProcGroups,_J:rbnCpuProcGroup,'rbnCpuProcMIBObjects':rbnCpuProcMIBObjects,'rbnCpuProcTable':rbnCpuProcTable,'rbnCpuProcEntry':rbnCpuProcEntry,_E:rbnCpuProcName,_P:rbnCpuProcPriority,_Q:rbnCpuProcTime,_R:rbnCpuProcCalls,_S:rbnCpuProc5Sec,_T:rbnCpuProc1Min,_U:rbnCpuProc5Min,_V:rbnCpuProcLongest})