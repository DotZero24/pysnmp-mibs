_AE='adslExtNotificationsGroup'
_AD='adslExtAturPhysPerfCounterGroup'
_AC='adslExtAtucPhysPerfCounterGroup'
_AB='adslExtLineAlarmConfProfileGroup'
_AA='adslExtLineConfProfileControlGroup'
_A9='adslExtLineGroup'
_A8='adslAturUasLThreshTrap'
_A7='adslAturSesLThreshTrap'
_A6='adslAtucUasLThreshTrap'
_A5='adslAtucSesLThreshTrap'
_A4='adslAtucFailedFastRThreshTrap'
_A3='adslAturThreshold15MinUasL'
_A2='adslAturThreshold15MinSesL'
_A1='adslAtucThreshold15MinUasL'
_A0='adslAtucThreshold15MinSesL'
_z='adslAtucThreshold15MinFailedFastR'
_y='adslConfProfileLineType'
_x='adslAturIntervalUasL'
_w='adslAturIntervalSesL'
_v='adslAturPerfPrev1DayUasL'
_u='adslAturPerfPrev1DaySesL'
_t='adslAturPerfCurr1DayUasL'
_s='adslAturPerfCurr1DaySesL'
_r='adslAturPerfStatUasL'
_q='adslAturPerfStatSesL'
_p='adslAtucIntervalUasL'
_o='adslAtucIntervalSesL'
_n='adslAtucIntervalFailedFastR'
_m='adslAtucIntervalFastR'
_l='adslAtucPerfPrev1DayUasL'
_k='adslAtucPerfPrev1DaySesL'
_j='adslAtucPerfCurr1DayUasL'
_i='adslAtucPerfCurr1DaySesL'
_h='adslAtucPerfStatUasL'
_g='adslAtucPerfStatSesL'
_f='adslAtucPerfPrev1DayFailedFastR'
_e='adslAtucPerfPrev1DayFastR'
_d='adslAtucPerfCurr1DayFailedFastR'
_c='adslAtucPerfCurr1DayFastR'
_b='adslAtucPerfCurr15MinFastR'
_a='adslAtucPerfStatFailedFastR'
_Z='adslAtucPerfStatFastR'
_Y='adslLineGlitePowerState'
_X='adslLineTransAtucActual'
_W='adslLineTransAtucConfig'
_V='adslLineTransAtucCap'
_U='adslLineConfProfileDualLite'
_T='adslAlarmConfProfileExtEntry'
_S='adslConfProfileExtEntry'
_R='adslAturIntervalExtEntry'
_Q='adslAturPerfDataExtEntry'
_P='adslAtucIntervalExtEntry'
_O='adslAtucPerfDataExtEntry'
_N='adslLineExtEntry'
_M='line retrains'
_L='read-write'
_K='adslAturPerfCurr15MinUasL'
_J='adslAturPerfCurr15MinSesL'
_I='adslAtucPerfCurr15MinUasL'
_H='adslAtucPerfCurr15MinSesL'
_G='adslAtucPerfCurr15MinFailedFastR'
_F='read-create'
_E='Integer32'
_D='seconds'
_C='read-only'
_B='ADSL-LINE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslAtucIntervalEntry,adslAtucPerfDataEntry,adslAturIntervalEntry,adslAturPerfDataEntry,adslLineAlarmConfProfileEntry,adslLineConfProfileEntry,adslLineEntry,adslMIB=mibBuilder.importSymbols('ADSL-LINE-MIB','adslAtucIntervalEntry','adslAtucPerfDataEntry','adslAturIntervalEntry','adslAturPerfDataEntry','adslLineAlarmConfProfileEntry','adslLineConfProfileEntry','adslLineEntry','adslMIB')
AdslPerfCurrDayCount,AdslPerfPrevDayCount=mibBuilder.importSymbols('ADSL-TC-MIB','AdslPerfCurrDayCount','AdslPerfPrevDayCount')
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adslExtMIB=ModuleIdentity((1,3,6,1,2,1,10,94,3))
if mibBuilder.loadTexts:adslExtMIB.setRevisions(('2002-12-10 00:00',))
class AdslTransmissionModeType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('ansit1413',0),('etsi',1),('q9921PotsNonOverlapped',2),('q9921PotsOverlapped',3),('q9921IsdnNonOverlapped',4),('q9921isdnOverlapped',5),('q9921tcmIsdnNonOverlapped',6),('q9921tcmIsdnOverlapped',7),('q9922potsNonOverlapeed',8),('q9922potsOverlapped',9),('q9922tcmIsdnNonOverlapped',10),('q9922tcmIsdnOverlapped',11),('q9921tcmIsdnSymmetric',12)))
_AdslExtMibObjects_ObjectIdentity=ObjectIdentity
adslExtMibObjects=_AdslExtMibObjects_ObjectIdentity((1,3,6,1,2,1,10,94,3,1))
_AdslLineExtTable_Object=MibTable
adslLineExtTable=_AdslLineExtTable_Object((1,3,6,1,2,1,10,94,3,1,17))
if mibBuilder.loadTexts:adslLineExtTable.setStatus(_A)
_AdslLineExtEntry_Object=MibTableRow
adslLineExtEntry=_AdslLineExtEntry_Object((1,3,6,1,2,1,10,94,3,1,17,1))
if mibBuilder.loadTexts:adslLineExtEntry.setStatus(_A)
_AdslLineTransAtucCap_Type=AdslTransmissionModeType
_AdslLineTransAtucCap_Object=MibTableColumn
adslLineTransAtucCap=_AdslLineTransAtucCap_Object((1,3,6,1,2,1,10,94,3,1,17,1,1),_AdslLineTransAtucCap_Type())
adslLineTransAtucCap.setMaxAccess(_C)
if mibBuilder.loadTexts:adslLineTransAtucCap.setStatus(_A)
_AdslLineTransAtucConfig_Type=AdslTransmissionModeType
_AdslLineTransAtucConfig_Object=MibTableColumn
adslLineTransAtucConfig=_AdslLineTransAtucConfig_Object((1,3,6,1,2,1,10,94,3,1,17,1,2),_AdslLineTransAtucConfig_Type())
adslLineTransAtucConfig.setMaxAccess(_L)
if mibBuilder.loadTexts:adslLineTransAtucConfig.setStatus(_A)
_AdslLineTransAtucActual_Type=AdslTransmissionModeType
_AdslLineTransAtucActual_Object=MibTableColumn
adslLineTransAtucActual=_AdslLineTransAtucActual_Object((1,3,6,1,2,1,10,94,3,1,17,1,3),_AdslLineTransAtucActual_Type())
adslLineTransAtucActual.setMaxAccess(_C)
if mibBuilder.loadTexts:adslLineTransAtucActual.setStatus(_A)
class _AdslLineGlitePowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('l0',2),('l1',3),('l3',4)))
_AdslLineGlitePowerState_Type.__name__=_E
_AdslLineGlitePowerState_Object=MibTableColumn
adslLineGlitePowerState=_AdslLineGlitePowerState_Object((1,3,6,1,2,1,10,94,3,1,17,1,4),_AdslLineGlitePowerState_Type())
adslLineGlitePowerState.setMaxAccess(_C)
if mibBuilder.loadTexts:adslLineGlitePowerState.setStatus(_A)
_AdslLineConfProfileDualLite_Type=SnmpAdminString
_AdslLineConfProfileDualLite_Object=MibTableColumn
adslLineConfProfileDualLite=_AdslLineConfProfileDualLite_Object((1,3,6,1,2,1,10,94,3,1,17,1,5),_AdslLineConfProfileDualLite_Type())
adslLineConfProfileDualLite.setMaxAccess(_L)
if mibBuilder.loadTexts:adslLineConfProfileDualLite.setStatus(_A)
_AdslAtucPerfDataExtTable_Object=MibTable
adslAtucPerfDataExtTable=_AdslAtucPerfDataExtTable_Object((1,3,6,1,2,1,10,94,3,1,18))
if mibBuilder.loadTexts:adslAtucPerfDataExtTable.setStatus(_A)
_AdslAtucPerfDataExtEntry_Object=MibTableRow
adslAtucPerfDataExtEntry=_AdslAtucPerfDataExtEntry_Object((1,3,6,1,2,1,10,94,3,1,18,1))
if mibBuilder.loadTexts:adslAtucPerfDataExtEntry.setStatus(_A)
_AdslAtucPerfStatFastR_Type=Counter32
_AdslAtucPerfStatFastR_Object=MibTableColumn
adslAtucPerfStatFastR=_AdslAtucPerfStatFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,1),_AdslAtucPerfStatFastR_Type())
adslAtucPerfStatFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfStatFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfStatFastR.setUnits(_M)
_AdslAtucPerfStatFailedFastR_Type=Counter32
_AdslAtucPerfStatFailedFastR_Object=MibTableColumn
adslAtucPerfStatFailedFastR=_AdslAtucPerfStatFailedFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,2),_AdslAtucPerfStatFailedFastR_Type())
adslAtucPerfStatFailedFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfStatFailedFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfStatFailedFastR.setUnits(_M)
_AdslAtucPerfStatSesL_Type=Counter32
_AdslAtucPerfStatSesL_Object=MibTableColumn
adslAtucPerfStatSesL=_AdslAtucPerfStatSesL_Object((1,3,6,1,2,1,10,94,3,1,18,1,3),_AdslAtucPerfStatSesL_Type())
adslAtucPerfStatSesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfStatSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfStatSesL.setUnits(_D)
_AdslAtucPerfStatUasL_Type=Counter32
_AdslAtucPerfStatUasL_Object=MibTableColumn
adslAtucPerfStatUasL=_AdslAtucPerfStatUasL_Object((1,3,6,1,2,1,10,94,3,1,18,1,4),_AdslAtucPerfStatUasL_Type())
adslAtucPerfStatUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfStatUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfStatUasL.setUnits(_D)
_AdslAtucPerfCurr15MinFastR_Type=PerfCurrentCount
_AdslAtucPerfCurr15MinFastR_Object=MibTableColumn
adslAtucPerfCurr15MinFastR=_AdslAtucPerfCurr15MinFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,5),_AdslAtucPerfCurr15MinFastR_Type())
adslAtucPerfCurr15MinFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinFastR.setUnits(_D)
_AdslAtucPerfCurr15MinFailedFastR_Type=PerfCurrentCount
_AdslAtucPerfCurr15MinFailedFastR_Object=MibTableColumn
adslAtucPerfCurr15MinFailedFastR=_AdslAtucPerfCurr15MinFailedFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,6),_AdslAtucPerfCurr15MinFailedFastR_Type())
adslAtucPerfCurr15MinFailedFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinFailedFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinFailedFastR.setUnits(_D)
_AdslAtucPerfCurr15MinSesL_Type=PerfCurrentCount
_AdslAtucPerfCurr15MinSesL_Object=MibTableColumn
adslAtucPerfCurr15MinSesL=_AdslAtucPerfCurr15MinSesL_Object((1,3,6,1,2,1,10,94,3,1,18,1,7),_AdslAtucPerfCurr15MinSesL_Type())
adslAtucPerfCurr15MinSesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinSesL.setUnits(_D)
_AdslAtucPerfCurr15MinUasL_Type=PerfCurrentCount
_AdslAtucPerfCurr15MinUasL_Object=MibTableColumn
adslAtucPerfCurr15MinUasL=_AdslAtucPerfCurr15MinUasL_Object((1,3,6,1,2,1,10,94,3,1,18,1,8),_AdslAtucPerfCurr15MinUasL_Type())
adslAtucPerfCurr15MinUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr15MinUasL.setUnits(_D)
_AdslAtucPerfCurr1DayFastR_Type=AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayFastR_Object=MibTableColumn
adslAtucPerfCurr1DayFastR=_AdslAtucPerfCurr1DayFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,9),_AdslAtucPerfCurr1DayFastR_Type())
adslAtucPerfCurr1DayFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr1DayFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr1DayFastR.setUnits(_D)
_AdslAtucPerfCurr1DayFailedFastR_Type=AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayFailedFastR_Object=MibTableColumn
adslAtucPerfCurr1DayFailedFastR=_AdslAtucPerfCurr1DayFailedFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,10),_AdslAtucPerfCurr1DayFailedFastR_Type())
adslAtucPerfCurr1DayFailedFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr1DayFailedFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr1DayFailedFastR.setUnits(_D)
_AdslAtucPerfCurr1DaySesL_Type=AdslPerfCurrDayCount
_AdslAtucPerfCurr1DaySesL_Object=MibTableColumn
adslAtucPerfCurr1DaySesL=_AdslAtucPerfCurr1DaySesL_Object((1,3,6,1,2,1,10,94,3,1,18,1,11),_AdslAtucPerfCurr1DaySesL_Type())
adslAtucPerfCurr1DaySesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr1DaySesL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr1DaySesL.setUnits(_D)
_AdslAtucPerfCurr1DayUasL_Type=AdslPerfCurrDayCount
_AdslAtucPerfCurr1DayUasL_Object=MibTableColumn
adslAtucPerfCurr1DayUasL=_AdslAtucPerfCurr1DayUasL_Object((1,3,6,1,2,1,10,94,3,1,18,1,12),_AdslAtucPerfCurr1DayUasL_Type())
adslAtucPerfCurr1DayUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfCurr1DayUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfCurr1DayUasL.setUnits(_D)
_AdslAtucPerfPrev1DayFastR_Type=AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayFastR_Object=MibTableColumn
adslAtucPerfPrev1DayFastR=_AdslAtucPerfPrev1DayFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,13),_AdslAtucPerfPrev1DayFastR_Type())
adslAtucPerfPrev1DayFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfPrev1DayFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfPrev1DayFastR.setUnits(_D)
_AdslAtucPerfPrev1DayFailedFastR_Type=AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayFailedFastR_Object=MibTableColumn
adslAtucPerfPrev1DayFailedFastR=_AdslAtucPerfPrev1DayFailedFastR_Object((1,3,6,1,2,1,10,94,3,1,18,1,14),_AdslAtucPerfPrev1DayFailedFastR_Type())
adslAtucPerfPrev1DayFailedFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfPrev1DayFailedFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfPrev1DayFailedFastR.setUnits(_D)
_AdslAtucPerfPrev1DaySesL_Type=AdslPerfPrevDayCount
_AdslAtucPerfPrev1DaySesL_Object=MibTableColumn
adslAtucPerfPrev1DaySesL=_AdslAtucPerfPrev1DaySesL_Object((1,3,6,1,2,1,10,94,3,1,18,1,15),_AdslAtucPerfPrev1DaySesL_Type())
adslAtucPerfPrev1DaySesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfPrev1DaySesL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfPrev1DaySesL.setUnits(_D)
_AdslAtucPerfPrev1DayUasL_Type=AdslPerfPrevDayCount
_AdslAtucPerfPrev1DayUasL_Object=MibTableColumn
adslAtucPerfPrev1DayUasL=_AdslAtucPerfPrev1DayUasL_Object((1,3,6,1,2,1,10,94,3,1,18,1,16),_AdslAtucPerfPrev1DayUasL_Type())
adslAtucPerfPrev1DayUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucPerfPrev1DayUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucPerfPrev1DayUasL.setUnits(_D)
_AdslAtucIntervalExtTable_Object=MibTable
adslAtucIntervalExtTable=_AdslAtucIntervalExtTable_Object((1,3,6,1,2,1,10,94,3,1,19))
if mibBuilder.loadTexts:adslAtucIntervalExtTable.setStatus(_A)
_AdslAtucIntervalExtEntry_Object=MibTableRow
adslAtucIntervalExtEntry=_AdslAtucIntervalExtEntry_Object((1,3,6,1,2,1,10,94,3,1,19,1))
if mibBuilder.loadTexts:adslAtucIntervalExtEntry.setStatus(_A)
_AdslAtucIntervalFastR_Type=PerfIntervalCount
_AdslAtucIntervalFastR_Object=MibTableColumn
adslAtucIntervalFastR=_AdslAtucIntervalFastR_Object((1,3,6,1,2,1,10,94,3,1,19,1,1),_AdslAtucIntervalFastR_Type())
adslAtucIntervalFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucIntervalFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucIntervalFastR.setUnits(_D)
_AdslAtucIntervalFailedFastR_Type=PerfIntervalCount
_AdslAtucIntervalFailedFastR_Object=MibTableColumn
adslAtucIntervalFailedFastR=_AdslAtucIntervalFailedFastR_Object((1,3,6,1,2,1,10,94,3,1,19,1,2),_AdslAtucIntervalFailedFastR_Type())
adslAtucIntervalFailedFastR.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucIntervalFailedFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucIntervalFailedFastR.setUnits(_D)
_AdslAtucIntervalSesL_Type=PerfIntervalCount
_AdslAtucIntervalSesL_Object=MibTableColumn
adslAtucIntervalSesL=_AdslAtucIntervalSesL_Object((1,3,6,1,2,1,10,94,3,1,19,1,3),_AdslAtucIntervalSesL_Type())
adslAtucIntervalSesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucIntervalSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucIntervalSesL.setUnits(_D)
_AdslAtucIntervalUasL_Type=PerfIntervalCount
_AdslAtucIntervalUasL_Object=MibTableColumn
adslAtucIntervalUasL=_AdslAtucIntervalUasL_Object((1,3,6,1,2,1,10,94,3,1,19,1,4),_AdslAtucIntervalUasL_Type())
adslAtucIntervalUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAtucIntervalUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucIntervalUasL.setUnits(_D)
_AdslAturPerfDataExtTable_Object=MibTable
adslAturPerfDataExtTable=_AdslAturPerfDataExtTable_Object((1,3,6,1,2,1,10,94,3,1,20))
if mibBuilder.loadTexts:adslAturPerfDataExtTable.setStatus(_A)
_AdslAturPerfDataExtEntry_Object=MibTableRow
adslAturPerfDataExtEntry=_AdslAturPerfDataExtEntry_Object((1,3,6,1,2,1,10,94,3,1,20,1))
if mibBuilder.loadTexts:adslAturPerfDataExtEntry.setStatus(_A)
_AdslAturPerfStatSesL_Type=Counter32
_AdslAturPerfStatSesL_Object=MibTableColumn
adslAturPerfStatSesL=_AdslAturPerfStatSesL_Object((1,3,6,1,2,1,10,94,3,1,20,1,1),_AdslAturPerfStatSesL_Type())
adslAturPerfStatSesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfStatSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfStatSesL.setUnits(_D)
_AdslAturPerfStatUasL_Type=Counter32
_AdslAturPerfStatUasL_Object=MibTableColumn
adslAturPerfStatUasL=_AdslAturPerfStatUasL_Object((1,3,6,1,2,1,10,94,3,1,20,1,2),_AdslAturPerfStatUasL_Type())
adslAturPerfStatUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfStatUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfStatUasL.setUnits(_D)
_AdslAturPerfCurr15MinSesL_Type=PerfCurrentCount
_AdslAturPerfCurr15MinSesL_Object=MibTableColumn
adslAturPerfCurr15MinSesL=_AdslAturPerfCurr15MinSesL_Object((1,3,6,1,2,1,10,94,3,1,20,1,3),_AdslAturPerfCurr15MinSesL_Type())
adslAturPerfCurr15MinSesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfCurr15MinSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfCurr15MinSesL.setUnits(_D)
_AdslAturPerfCurr15MinUasL_Type=PerfCurrentCount
_AdslAturPerfCurr15MinUasL_Object=MibTableColumn
adslAturPerfCurr15MinUasL=_AdslAturPerfCurr15MinUasL_Object((1,3,6,1,2,1,10,94,3,1,20,1,4),_AdslAturPerfCurr15MinUasL_Type())
adslAturPerfCurr15MinUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfCurr15MinUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfCurr15MinUasL.setUnits(_D)
_AdslAturPerfCurr1DaySesL_Type=AdslPerfCurrDayCount
_AdslAturPerfCurr1DaySesL_Object=MibTableColumn
adslAturPerfCurr1DaySesL=_AdslAturPerfCurr1DaySesL_Object((1,3,6,1,2,1,10,94,3,1,20,1,5),_AdslAturPerfCurr1DaySesL_Type())
adslAturPerfCurr1DaySesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfCurr1DaySesL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfCurr1DaySesL.setUnits(_D)
_AdslAturPerfCurr1DayUasL_Type=AdslPerfCurrDayCount
_AdslAturPerfCurr1DayUasL_Object=MibTableColumn
adslAturPerfCurr1DayUasL=_AdslAturPerfCurr1DayUasL_Object((1,3,6,1,2,1,10,94,3,1,20,1,6),_AdslAturPerfCurr1DayUasL_Type())
adslAturPerfCurr1DayUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfCurr1DayUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfCurr1DayUasL.setUnits(_D)
_AdslAturPerfPrev1DaySesL_Type=AdslPerfPrevDayCount
_AdslAturPerfPrev1DaySesL_Object=MibTableColumn
adslAturPerfPrev1DaySesL=_AdslAturPerfPrev1DaySesL_Object((1,3,6,1,2,1,10,94,3,1,20,1,7),_AdslAturPerfPrev1DaySesL_Type())
adslAturPerfPrev1DaySesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfPrev1DaySesL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfPrev1DaySesL.setUnits(_D)
_AdslAturPerfPrev1DayUasL_Type=AdslPerfPrevDayCount
_AdslAturPerfPrev1DayUasL_Object=MibTableColumn
adslAturPerfPrev1DayUasL=_AdslAturPerfPrev1DayUasL_Object((1,3,6,1,2,1,10,94,3,1,20,1,8),_AdslAturPerfPrev1DayUasL_Type())
adslAturPerfPrev1DayUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturPerfPrev1DayUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAturPerfPrev1DayUasL.setUnits(_D)
_AdslAturIntervalExtTable_Object=MibTable
adslAturIntervalExtTable=_AdslAturIntervalExtTable_Object((1,3,6,1,2,1,10,94,3,1,21))
if mibBuilder.loadTexts:adslAturIntervalExtTable.setStatus(_A)
_AdslAturIntervalExtEntry_Object=MibTableRow
adslAturIntervalExtEntry=_AdslAturIntervalExtEntry_Object((1,3,6,1,2,1,10,94,3,1,21,1))
if mibBuilder.loadTexts:adslAturIntervalExtEntry.setStatus(_A)
_AdslAturIntervalSesL_Type=PerfIntervalCount
_AdslAturIntervalSesL_Object=MibTableColumn
adslAturIntervalSesL=_AdslAturIntervalSesL_Object((1,3,6,1,2,1,10,94,3,1,21,1,1),_AdslAturIntervalSesL_Type())
adslAturIntervalSesL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturIntervalSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAturIntervalSesL.setUnits(_D)
_AdslAturIntervalUasL_Type=PerfIntervalCount
_AdslAturIntervalUasL_Object=MibTableColumn
adslAturIntervalUasL=_AdslAturIntervalUasL_Object((1,3,6,1,2,1,10,94,3,1,21,1,2),_AdslAturIntervalUasL_Type())
adslAturIntervalUasL.setMaxAccess(_C)
if mibBuilder.loadTexts:adslAturIntervalUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAturIntervalUasL.setUnits(_D)
_AdslConfProfileExtTable_Object=MibTable
adslConfProfileExtTable=_AdslConfProfileExtTable_Object((1,3,6,1,2,1,10,94,3,1,22))
if mibBuilder.loadTexts:adslConfProfileExtTable.setStatus(_A)
_AdslConfProfileExtEntry_Object=MibTableRow
adslConfProfileExtEntry=_AdslConfProfileExtEntry_Object((1,3,6,1,2,1,10,94,3,1,22,1))
if mibBuilder.loadTexts:adslConfProfileExtEntry.setStatus(_A)
class _AdslConfProfileLineType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noChannel',1),('fastOnly',2),('interleavedOnly',3),('fastOrInterleaved',4),('fastAndInterleaved',5)))
_AdslConfProfileLineType_Type.__name__=_E
_AdslConfProfileLineType_Object=MibTableColumn
adslConfProfileLineType=_AdslConfProfileLineType_Object((1,3,6,1,2,1,10,94,3,1,22,1,1),_AdslConfProfileLineType_Type())
adslConfProfileLineType.setMaxAccess(_F)
if mibBuilder.loadTexts:adslConfProfileLineType.setStatus(_A)
_AdslAlarmConfProfileExtTable_Object=MibTable
adslAlarmConfProfileExtTable=_AdslAlarmConfProfileExtTable_Object((1,3,6,1,2,1,10,94,3,1,23))
if mibBuilder.loadTexts:adslAlarmConfProfileExtTable.setStatus(_A)
_AdslAlarmConfProfileExtEntry_Object=MibTableRow
adslAlarmConfProfileExtEntry=_AdslAlarmConfProfileExtEntry_Object((1,3,6,1,2,1,10,94,3,1,23,1))
if mibBuilder.loadTexts:adslAlarmConfProfileExtEntry.setStatus(_A)
class _AdslAtucThreshold15MinFailedFastR_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_AdslAtucThreshold15MinFailedFastR_Type.__name__=_E
_AdslAtucThreshold15MinFailedFastR_Object=MibTableColumn
adslAtucThreshold15MinFailedFastR=_AdslAtucThreshold15MinFailedFastR_Object((1,3,6,1,2,1,10,94,3,1,23,1,1),_AdslAtucThreshold15MinFailedFastR_Type())
adslAtucThreshold15MinFailedFastR.setMaxAccess(_F)
if mibBuilder.loadTexts:adslAtucThreshold15MinFailedFastR.setStatus(_A)
if mibBuilder.loadTexts:adslAtucThreshold15MinFailedFastR.setUnits(_D)
class _AdslAtucThreshold15MinSesL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_AdslAtucThreshold15MinSesL_Type.__name__=_E
_AdslAtucThreshold15MinSesL_Object=MibTableColumn
adslAtucThreshold15MinSesL=_AdslAtucThreshold15MinSesL_Object((1,3,6,1,2,1,10,94,3,1,23,1,2),_AdslAtucThreshold15MinSesL_Type())
adslAtucThreshold15MinSesL.setMaxAccess(_F)
if mibBuilder.loadTexts:adslAtucThreshold15MinSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucThreshold15MinSesL.setUnits(_D)
class _AdslAtucThreshold15MinUasL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_AdslAtucThreshold15MinUasL_Type.__name__=_E
_AdslAtucThreshold15MinUasL_Object=MibTableColumn
adslAtucThreshold15MinUasL=_AdslAtucThreshold15MinUasL_Object((1,3,6,1,2,1,10,94,3,1,23,1,3),_AdslAtucThreshold15MinUasL_Type())
adslAtucThreshold15MinUasL.setMaxAccess(_F)
if mibBuilder.loadTexts:adslAtucThreshold15MinUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAtucThreshold15MinUasL.setUnits(_D)
class _AdslAturThreshold15MinSesL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_AdslAturThreshold15MinSesL_Type.__name__=_E
_AdslAturThreshold15MinSesL_Object=MibTableColumn
adslAturThreshold15MinSesL=_AdslAturThreshold15MinSesL_Object((1,3,6,1,2,1,10,94,3,1,23,1,4),_AdslAturThreshold15MinSesL_Type())
adslAturThreshold15MinSesL.setMaxAccess(_F)
if mibBuilder.loadTexts:adslAturThreshold15MinSesL.setStatus(_A)
if mibBuilder.loadTexts:adslAturThreshold15MinSesL.setUnits(_D)
class _AdslAturThreshold15MinUasL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_AdslAturThreshold15MinUasL_Type.__name__=_E
_AdslAturThreshold15MinUasL_Object=MibTableColumn
adslAturThreshold15MinUasL=_AdslAturThreshold15MinUasL_Object((1,3,6,1,2,1,10,94,3,1,23,1,5),_AdslAturThreshold15MinUasL_Type())
adslAturThreshold15MinUasL.setMaxAccess(_F)
if mibBuilder.loadTexts:adslAturThreshold15MinUasL.setStatus(_A)
if mibBuilder.loadTexts:adslAturThreshold15MinUasL.setUnits(_D)
_AdslExtTraps_ObjectIdentity=ObjectIdentity
adslExtTraps=_AdslExtTraps_ObjectIdentity((1,3,6,1,2,1,10,94,3,1,24))
_AdslExtAtucTraps_ObjectIdentity=ObjectIdentity
adslExtAtucTraps=_AdslExtAtucTraps_ObjectIdentity((1,3,6,1,2,1,10,94,3,1,24,1))
_AdslExtAtucTrapsPrefix_ObjectIdentity=ObjectIdentity
adslExtAtucTrapsPrefix=_AdslExtAtucTrapsPrefix_ObjectIdentity((1,3,6,1,2,1,10,94,3,1,24,1,0))
_AdslExtAturTraps_ObjectIdentity=ObjectIdentity
adslExtAturTraps=_AdslExtAturTraps_ObjectIdentity((1,3,6,1,2,1,10,94,3,1,24,2))
_AdslExtAturTrapsPrefix_ObjectIdentity=ObjectIdentity
adslExtAturTrapsPrefix=_AdslExtAturTrapsPrefix_ObjectIdentity((1,3,6,1,2,1,10,94,3,1,24,2,0))
_AdslExtConformance_ObjectIdentity=ObjectIdentity
adslExtConformance=_AdslExtConformance_ObjectIdentity((1,3,6,1,2,1,10,94,3,2))
_AdslExtGroups_ObjectIdentity=ObjectIdentity
adslExtGroups=_AdslExtGroups_ObjectIdentity((1,3,6,1,2,1,10,94,3,2,1))
_AdslExtCompliances_ObjectIdentity=ObjectIdentity
adslExtCompliances=_AdslExtCompliances_ObjectIdentity((1,3,6,1,2,1,10,94,3,2,2))
adslLineEntry.registerAugmentions((_B,_N))
adslLineExtEntry.setIndexNames(*adslLineEntry.getIndexNames())
adslAtucPerfDataEntry.registerAugmentions((_B,_O))
adslAtucPerfDataExtEntry.setIndexNames(*adslAtucPerfDataEntry.getIndexNames())
adslAtucIntervalEntry.registerAugmentions((_B,_P))
adslAtucIntervalExtEntry.setIndexNames(*adslAtucIntervalEntry.getIndexNames())
adslAturPerfDataEntry.registerAugmentions((_B,_Q))
adslAturPerfDataExtEntry.setIndexNames(*adslAturPerfDataEntry.getIndexNames())
adslAturIntervalEntry.registerAugmentions((_B,_R))
adslAturIntervalExtEntry.setIndexNames(*adslAturIntervalEntry.getIndexNames())
adslLineConfProfileEntry.registerAugmentions((_B,_S))
adslConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineAlarmConfProfileEntry.registerAugmentions((_B,_T))
adslAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())
adslExtLineGroup=ObjectGroup((1,3,6,1,2,1,10,94,3,2,1,1))
adslExtLineGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:adslExtLineGroup.setStatus(_A)
adslExtAtucPhysPerfCounterGroup=ObjectGroup((1,3,6,1,2,1,10,94,3,2,1,2))
adslExtAtucPhysPerfCounterGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_G),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_H),(_B,_I),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:adslExtAtucPhysPerfCounterGroup.setStatus(_A)
adslExtAturPhysPerfCounterGroup=ObjectGroup((1,3,6,1,2,1,10,94,3,2,1,3))
adslExtAturPhysPerfCounterGroup.setObjects(*((_B,_q),(_B,_r),(_B,_J),(_B,_K),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:adslExtAturPhysPerfCounterGroup.setStatus(_A)
adslExtLineConfProfileControlGroup=ObjectGroup((1,3,6,1,2,1,10,94,3,2,1,4))
adslExtLineConfProfileControlGroup.setObjects((_B,_y))
if mibBuilder.loadTexts:adslExtLineConfProfileControlGroup.setStatus(_A)
adslExtLineAlarmConfProfileGroup=ObjectGroup((1,3,6,1,2,1,10,94,3,2,1,5))
adslExtLineAlarmConfProfileGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:adslExtLineAlarmConfProfileGroup.setStatus(_A)
adslAtucFailedFastRThreshTrap=NotificationType((1,3,6,1,2,1,10,94,3,1,24,1,0,1))
adslAtucFailedFastRThreshTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:adslAtucFailedFastRThreshTrap.setStatus(_A)
adslAtucSesLThreshTrap=NotificationType((1,3,6,1,2,1,10,94,3,1,24,1,0,2))
adslAtucSesLThreshTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:adslAtucSesLThreshTrap.setStatus(_A)
adslAtucUasLThreshTrap=NotificationType((1,3,6,1,2,1,10,94,3,1,24,1,0,3))
adslAtucUasLThreshTrap.setObjects((_B,_I))
if mibBuilder.loadTexts:adslAtucUasLThreshTrap.setStatus(_A)
adslAturSesLThreshTrap=NotificationType((1,3,6,1,2,1,10,94,3,1,24,2,0,1))
adslAturSesLThreshTrap.setObjects((_B,_J))
if mibBuilder.loadTexts:adslAturSesLThreshTrap.setStatus(_A)
adslAturUasLThreshTrap=NotificationType((1,3,6,1,2,1,10,94,3,1,24,2,0,2))
adslAturUasLThreshTrap.setObjects((_B,_K))
if mibBuilder.loadTexts:adslAturUasLThreshTrap.setStatus(_A)
adslExtNotificationsGroup=NotificationGroup((1,3,6,1,2,1,10,94,3,2,1,6))
adslExtNotificationsGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:adslExtNotificationsGroup.setStatus(_A)
adslExtLineMibAtucCompliance=ModuleCompliance((1,3,6,1,2,1,10,94,3,2,2,1))
adslExtLineMibAtucCompliance.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:adslExtLineMibAtucCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AdslTransmissionModeType':AdslTransmissionModeType,'adslExtMIB':adslExtMIB,'adslExtMibObjects':adslExtMibObjects,'adslLineExtTable':adslLineExtTable,_N:adslLineExtEntry,_V:adslLineTransAtucCap,_W:adslLineTransAtucConfig,_X:adslLineTransAtucActual,_Y:adslLineGlitePowerState,_U:adslLineConfProfileDualLite,'adslAtucPerfDataExtTable':adslAtucPerfDataExtTable,_O:adslAtucPerfDataExtEntry,_Z:adslAtucPerfStatFastR,_a:adslAtucPerfStatFailedFastR,_g:adslAtucPerfStatSesL,_h:adslAtucPerfStatUasL,_b:adslAtucPerfCurr15MinFastR,_G:adslAtucPerfCurr15MinFailedFastR,_H:adslAtucPerfCurr15MinSesL,_I:adslAtucPerfCurr15MinUasL,_c:adslAtucPerfCurr1DayFastR,_d:adslAtucPerfCurr1DayFailedFastR,_i:adslAtucPerfCurr1DaySesL,_j:adslAtucPerfCurr1DayUasL,_e:adslAtucPerfPrev1DayFastR,_f:adslAtucPerfPrev1DayFailedFastR,_k:adslAtucPerfPrev1DaySesL,_l:adslAtucPerfPrev1DayUasL,'adslAtucIntervalExtTable':adslAtucIntervalExtTable,_P:adslAtucIntervalExtEntry,_m:adslAtucIntervalFastR,_n:adslAtucIntervalFailedFastR,_o:adslAtucIntervalSesL,_p:adslAtucIntervalUasL,'adslAturPerfDataExtTable':adslAturPerfDataExtTable,_Q:adslAturPerfDataExtEntry,_q:adslAturPerfStatSesL,_r:adslAturPerfStatUasL,_J:adslAturPerfCurr15MinSesL,_K:adslAturPerfCurr15MinUasL,_s:adslAturPerfCurr1DaySesL,_t:adslAturPerfCurr1DayUasL,_u:adslAturPerfPrev1DaySesL,_v:adslAturPerfPrev1DayUasL,'adslAturIntervalExtTable':adslAturIntervalExtTable,_R:adslAturIntervalExtEntry,_w:adslAturIntervalSesL,_x:adslAturIntervalUasL,'adslConfProfileExtTable':adslConfProfileExtTable,_S:adslConfProfileExtEntry,_y:adslConfProfileLineType,'adslAlarmConfProfileExtTable':adslAlarmConfProfileExtTable,_T:adslAlarmConfProfileExtEntry,_z:adslAtucThreshold15MinFailedFastR,_A0:adslAtucThreshold15MinSesL,_A1:adslAtucThreshold15MinUasL,_A2:adslAturThreshold15MinSesL,_A3:adslAturThreshold15MinUasL,'adslExtTraps':adslExtTraps,'adslExtAtucTraps':adslExtAtucTraps,'adslExtAtucTrapsPrefix':adslExtAtucTrapsPrefix,_A4:adslAtucFailedFastRThreshTrap,_A5:adslAtucSesLThreshTrap,_A6:adslAtucUasLThreshTrap,'adslExtAturTraps':adslExtAturTraps,'adslExtAturTrapsPrefix':adslExtAturTrapsPrefix,_A7:adslAturSesLThreshTrap,_A8:adslAturUasLThreshTrap,'adslExtConformance':adslExtConformance,'adslExtGroups':adslExtGroups,_A9:adslExtLineGroup,_AC:adslExtAtucPhysPerfCounterGroup,_AD:adslExtAturPhysPerfCounterGroup,_AA:adslExtLineConfProfileControlGroup,_AB:adslExtLineAlarmConfProfileGroup,_AE:adslExtNotificationsGroup,'adslExtCompliances':adslExtCompliances,'adslExtLineMibAtucCompliance':adslExtLineMibAtucCompliance})