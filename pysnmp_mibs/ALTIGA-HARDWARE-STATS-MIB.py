_AJ='altigaHardwareStatsGroup'
_AI='alHardwareSerialNumber'
_AH='alHardwareClientEthPrivSwitch'
_AG='alHardwareCpuVoltageNominal'
_AF='alHardwareChassis'
_AE='alHardwareRamSize'
_AD='alHardwareSlot4Operational'
_AC='alHardwareSlot3Operational'
_AB='alHardwareSlot2Operational'
_AA='alHardwareSlot1Operational'
_A9='alHardwareSlot4Card'
_A8='alHardwareSlot3Card'
_A7='alHardwareSlot2Card'
_A6='alHardwareSlot1Card'
_A5='alHardwarePs2Type'
_A4='alHardwarePs1Type'
_A3='alHardwareFan3RpmTime'
_A2='alHardwareFan3RpmCount'
_A1='alHardwareFan3RpmAlarm'
_A0='alHardwareFan3Rpm'
_z='alHardwareFan2RpmTime'
_y='alHardwareFan2RpmCount'
_x='alHardwareFan2RpmAlarm'
_w='alHardwareFan2Rpm'
_v='alHardwareFan1RpmTime'
_u='alHardwareFan1RpmCount'
_t='alHardwareFan1RpmAlarm'
_s='alHardwareFan1Rpm'
_r='alHardwareCageTempTime'
_q='alHardwareCageTempCount'
_p='alHardwareCageTempAlarm'
_o='alHardwareCageTemp'
_n='alHardwareCpuTempTime'
_m='alHardwareCpuTempCount'
_l='alHardwareCpuTempAlarm'
_k='alHardwareCpuTemp'
_j='alHardwareBoardVoltage5vTime'
_i='alHardwareBoardVoltage5vCount'
_h='alHardwareBoardVoltage5vAlarm'
_g='alHardwareBoardVoltage5v'
_f='alHardwareBoardVoltage3vTime'
_e='alHardwareBoardVoltage3vCount'
_d='alHardwareBoardVoltage3vAlarm'
_c='alHardwareBoardVoltage3v'
_b='alHardwarePs2Voltage5vTime'
_a='alHardwarePs2Voltage5vCount'
_Z='alHardwarePs2Voltage5vAlarm'
_Y='alHardwarePs2Voltage5v'
_X='alHardwarePs2Voltage3vTime'
_W='alHardwarePs2Voltage3vCount'
_V='alHardwarePs2Voltage3vAlarm'
_U='alHardwarePs2Voltage3v'
_T='alHardwarePs1Voltage5vTime'
_S='alHardwarePs1Voltage5vCount'
_R='alHardwarePs1Voltage5vAlarm'
_Q='alHardwarePs1Voltage5v'
_P='alHardwarePs1Voltage3vTime'
_O='alHardwarePs1Voltage3vCount'
_N='alHardwarePs1Voltage3vAlarm'
_M='alHardwarePs1Voltage3v'
_L='alHardwareCpuVoltageTime'
_K='alHardwareCpuVoltageCount'
_J='alHardwareCpuVoltageAlarm'
_I='alHardwareCpuVoltage'
_H='degrees Celsius'
_G='RPM'
_F='none'
_E='Integer32'
_D='centivolts'
_C='read-only'
_B='ALTIGA-HARDWARE-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alHardwareMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alHardwareMibModule')
alHardwareGroup,alStatsHardware=mibBuilder.importSymbols('ALTIGA-MIB','alHardwareGroup','alStatsHardware')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
altigaHardwareStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,27,2))
if mibBuilder.loadTexts:altigaHardwareStatsMibModule.setRevisions(('2003-03-27 13:00','2002-09-05 13:00','2002-07-10 00:00'))
class ConcentratorCard(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('sep',2),('dualT1Wan',3),('sepE',4)))
class ConcentratorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cxx',1),('c5',2),('c1',3)))
_AltigaHardwareStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaHardwareStatsMibConformance=_AltigaHardwareStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,27,2,1))
_AltigaHardwareStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaHardwareStatsMibCompliances=_AltigaHardwareStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,27,2,1,1))
_AlStatsHardwareGlobal_ObjectIdentity=ObjectIdentity
alStatsHardwareGlobal=_AlStatsHardwareGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,22,1))
_AlHardwareCpuVoltage_Type=Gauge32
_AlHardwareCpuVoltage_Object=MibScalar
alHardwareCpuVoltage=_AlHardwareCpuVoltage_Object((1,3,6,1,4,1,3076,2,1,2,22,1,1),_AlHardwareCpuVoltage_Type())
alHardwareCpuVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuVoltage.setStatus(_A)
if mibBuilder.loadTexts:alHardwareCpuVoltage.setUnits(_D)
_AlHardwareCpuVoltageAlarm_Type=TruthValue
_AlHardwareCpuVoltageAlarm_Object=MibScalar
alHardwareCpuVoltageAlarm=_AlHardwareCpuVoltageAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,2),_AlHardwareCpuVoltageAlarm_Type())
alHardwareCpuVoltageAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuVoltageAlarm.setStatus(_A)
_AlHardwareCpuVoltageCount_Type=Counter32
_AlHardwareCpuVoltageCount_Object=MibScalar
alHardwareCpuVoltageCount=_AlHardwareCpuVoltageCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,3),_AlHardwareCpuVoltageCount_Type())
alHardwareCpuVoltageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuVoltageCount.setStatus(_A)
_AlHardwareCpuVoltageTime_Type=TimeTicks
_AlHardwareCpuVoltageTime_Object=MibScalar
alHardwareCpuVoltageTime=_AlHardwareCpuVoltageTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,4),_AlHardwareCpuVoltageTime_Type())
alHardwareCpuVoltageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuVoltageTime.setStatus(_A)
_AlHardwarePs1Voltage3v_Type=Gauge32
_AlHardwarePs1Voltage3v_Object=MibScalar
alHardwarePs1Voltage3v=_AlHardwarePs1Voltage3v_Object((1,3,6,1,4,1,3076,2,1,2,22,1,5),_AlHardwarePs1Voltage3v_Type())
alHardwarePs1Voltage3v.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage3v.setStatus(_A)
if mibBuilder.loadTexts:alHardwarePs1Voltage3v.setUnits(_D)
_AlHardwarePs1Voltage3vAlarm_Type=TruthValue
_AlHardwarePs1Voltage3vAlarm_Object=MibScalar
alHardwarePs1Voltage3vAlarm=_AlHardwarePs1Voltage3vAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,6),_AlHardwarePs1Voltage3vAlarm_Type())
alHardwarePs1Voltage3vAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage3vAlarm.setStatus(_A)
_AlHardwarePs1Voltage3vCount_Type=Counter32
_AlHardwarePs1Voltage3vCount_Object=MibScalar
alHardwarePs1Voltage3vCount=_AlHardwarePs1Voltage3vCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,7),_AlHardwarePs1Voltage3vCount_Type())
alHardwarePs1Voltage3vCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage3vCount.setStatus(_A)
_AlHardwarePs1Voltage3vTime_Type=TimeTicks
_AlHardwarePs1Voltage3vTime_Object=MibScalar
alHardwarePs1Voltage3vTime=_AlHardwarePs1Voltage3vTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,8),_AlHardwarePs1Voltage3vTime_Type())
alHardwarePs1Voltage3vTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage3vTime.setStatus(_A)
_AlHardwarePs1Voltage5v_Type=Gauge32
_AlHardwarePs1Voltage5v_Object=MibScalar
alHardwarePs1Voltage5v=_AlHardwarePs1Voltage5v_Object((1,3,6,1,4,1,3076,2,1,2,22,1,9),_AlHardwarePs1Voltage5v_Type())
alHardwarePs1Voltage5v.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage5v.setStatus(_A)
if mibBuilder.loadTexts:alHardwarePs1Voltage5v.setUnits(_D)
_AlHardwarePs1Voltage5vAlarm_Type=TruthValue
_AlHardwarePs1Voltage5vAlarm_Object=MibScalar
alHardwarePs1Voltage5vAlarm=_AlHardwarePs1Voltage5vAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,10),_AlHardwarePs1Voltage5vAlarm_Type())
alHardwarePs1Voltage5vAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage5vAlarm.setStatus(_A)
_AlHardwarePs1Voltage5vCount_Type=Counter32
_AlHardwarePs1Voltage5vCount_Object=MibScalar
alHardwarePs1Voltage5vCount=_AlHardwarePs1Voltage5vCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,11),_AlHardwarePs1Voltage5vCount_Type())
alHardwarePs1Voltage5vCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage5vCount.setStatus(_A)
_AlHardwarePs1Voltage5vTime_Type=TimeTicks
_AlHardwarePs1Voltage5vTime_Object=MibScalar
alHardwarePs1Voltage5vTime=_AlHardwarePs1Voltage5vTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,12),_AlHardwarePs1Voltage5vTime_Type())
alHardwarePs1Voltage5vTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Voltage5vTime.setStatus(_A)
_AlHardwarePs2Voltage3v_Type=Gauge32
_AlHardwarePs2Voltage3v_Object=MibScalar
alHardwarePs2Voltage3v=_AlHardwarePs2Voltage3v_Object((1,3,6,1,4,1,3076,2,1,2,22,1,13),_AlHardwarePs2Voltage3v_Type())
alHardwarePs2Voltage3v.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage3v.setStatus(_A)
if mibBuilder.loadTexts:alHardwarePs2Voltage3v.setUnits(_D)
_AlHardwarePs2Voltage3vAlarm_Type=TruthValue
_AlHardwarePs2Voltage3vAlarm_Object=MibScalar
alHardwarePs2Voltage3vAlarm=_AlHardwarePs2Voltage3vAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,14),_AlHardwarePs2Voltage3vAlarm_Type())
alHardwarePs2Voltage3vAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage3vAlarm.setStatus(_A)
_AlHardwarePs2Voltage3vCount_Type=Counter32
_AlHardwarePs2Voltage3vCount_Object=MibScalar
alHardwarePs2Voltage3vCount=_AlHardwarePs2Voltage3vCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,15),_AlHardwarePs2Voltage3vCount_Type())
alHardwarePs2Voltage3vCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage3vCount.setStatus(_A)
_AlHardwarePs2Voltage3vTime_Type=TimeTicks
_AlHardwarePs2Voltage3vTime_Object=MibScalar
alHardwarePs2Voltage3vTime=_AlHardwarePs2Voltage3vTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,16),_AlHardwarePs2Voltage3vTime_Type())
alHardwarePs2Voltage3vTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage3vTime.setStatus(_A)
_AlHardwarePs2Voltage5v_Type=Gauge32
_AlHardwarePs2Voltage5v_Object=MibScalar
alHardwarePs2Voltage5v=_AlHardwarePs2Voltage5v_Object((1,3,6,1,4,1,3076,2,1,2,22,1,17),_AlHardwarePs2Voltage5v_Type())
alHardwarePs2Voltage5v.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage5v.setStatus(_A)
if mibBuilder.loadTexts:alHardwarePs2Voltage5v.setUnits(_D)
_AlHardwarePs2Voltage5vAlarm_Type=TruthValue
_AlHardwarePs2Voltage5vAlarm_Object=MibScalar
alHardwarePs2Voltage5vAlarm=_AlHardwarePs2Voltage5vAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,18),_AlHardwarePs2Voltage5vAlarm_Type())
alHardwarePs2Voltage5vAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage5vAlarm.setStatus(_A)
_AlHardwarePs2Voltage5vCount_Type=Counter32
_AlHardwarePs2Voltage5vCount_Object=MibScalar
alHardwarePs2Voltage5vCount=_AlHardwarePs2Voltage5vCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,19),_AlHardwarePs2Voltage5vCount_Type())
alHardwarePs2Voltage5vCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage5vCount.setStatus(_A)
_AlHardwarePs2Voltage5vTime_Type=TimeTicks
_AlHardwarePs2Voltage5vTime_Object=MibScalar
alHardwarePs2Voltage5vTime=_AlHardwarePs2Voltage5vTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,20),_AlHardwarePs2Voltage5vTime_Type())
alHardwarePs2Voltage5vTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Voltage5vTime.setStatus(_A)
_AlHardwareBoardVoltage3v_Type=Gauge32
_AlHardwareBoardVoltage3v_Object=MibScalar
alHardwareBoardVoltage3v=_AlHardwareBoardVoltage3v_Object((1,3,6,1,4,1,3076,2,1,2,22,1,21),_AlHardwareBoardVoltage3v_Type())
alHardwareBoardVoltage3v.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage3v.setStatus(_A)
if mibBuilder.loadTexts:alHardwareBoardVoltage3v.setUnits(_D)
_AlHardwareBoardVoltage3vAlarm_Type=TruthValue
_AlHardwareBoardVoltage3vAlarm_Object=MibScalar
alHardwareBoardVoltage3vAlarm=_AlHardwareBoardVoltage3vAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,22),_AlHardwareBoardVoltage3vAlarm_Type())
alHardwareBoardVoltage3vAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage3vAlarm.setStatus(_A)
_AlHardwareBoardVoltage3vCount_Type=Counter32
_AlHardwareBoardVoltage3vCount_Object=MibScalar
alHardwareBoardVoltage3vCount=_AlHardwareBoardVoltage3vCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,23),_AlHardwareBoardVoltage3vCount_Type())
alHardwareBoardVoltage3vCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage3vCount.setStatus(_A)
_AlHardwareBoardVoltage3vTime_Type=TimeTicks
_AlHardwareBoardVoltage3vTime_Object=MibScalar
alHardwareBoardVoltage3vTime=_AlHardwareBoardVoltage3vTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,24),_AlHardwareBoardVoltage3vTime_Type())
alHardwareBoardVoltage3vTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage3vTime.setStatus(_A)
_AlHardwareBoardVoltage5v_Type=Gauge32
_AlHardwareBoardVoltage5v_Object=MibScalar
alHardwareBoardVoltage5v=_AlHardwareBoardVoltage5v_Object((1,3,6,1,4,1,3076,2,1,2,22,1,25),_AlHardwareBoardVoltage5v_Type())
alHardwareBoardVoltage5v.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage5v.setStatus(_A)
if mibBuilder.loadTexts:alHardwareBoardVoltage5v.setUnits(_D)
_AlHardwareBoardVoltage5vAlarm_Type=TruthValue
_AlHardwareBoardVoltage5vAlarm_Object=MibScalar
alHardwareBoardVoltage5vAlarm=_AlHardwareBoardVoltage5vAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,26),_AlHardwareBoardVoltage5vAlarm_Type())
alHardwareBoardVoltage5vAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage5vAlarm.setStatus(_A)
_AlHardwareBoardVoltage5vCount_Type=Counter32
_AlHardwareBoardVoltage5vCount_Object=MibScalar
alHardwareBoardVoltage5vCount=_AlHardwareBoardVoltage5vCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,27),_AlHardwareBoardVoltage5vCount_Type())
alHardwareBoardVoltage5vCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage5vCount.setStatus(_A)
_AlHardwareBoardVoltage5vTime_Type=TimeTicks
_AlHardwareBoardVoltage5vTime_Object=MibScalar
alHardwareBoardVoltage5vTime=_AlHardwareBoardVoltage5vTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,28),_AlHardwareBoardVoltage5vTime_Type())
alHardwareBoardVoltage5vTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareBoardVoltage5vTime.setStatus(_A)
class _AlHardwareCpuTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,120))
_AlHardwareCpuTemp_Type.__name__=_E
_AlHardwareCpuTemp_Object=MibScalar
alHardwareCpuTemp=_AlHardwareCpuTemp_Object((1,3,6,1,4,1,3076,2,1,2,22,1,29),_AlHardwareCpuTemp_Type())
alHardwareCpuTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuTemp.setStatus(_A)
if mibBuilder.loadTexts:alHardwareCpuTemp.setUnits(_H)
_AlHardwareCpuTempAlarm_Type=TruthValue
_AlHardwareCpuTempAlarm_Object=MibScalar
alHardwareCpuTempAlarm=_AlHardwareCpuTempAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,30),_AlHardwareCpuTempAlarm_Type())
alHardwareCpuTempAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuTempAlarm.setStatus(_A)
_AlHardwareCpuTempCount_Type=Counter32
_AlHardwareCpuTempCount_Object=MibScalar
alHardwareCpuTempCount=_AlHardwareCpuTempCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,31),_AlHardwareCpuTempCount_Type())
alHardwareCpuTempCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuTempCount.setStatus(_A)
_AlHardwareCpuTempTime_Type=TimeTicks
_AlHardwareCpuTempTime_Object=MibScalar
alHardwareCpuTempTime=_AlHardwareCpuTempTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,32),_AlHardwareCpuTempTime_Type())
alHardwareCpuTempTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuTempTime.setStatus(_A)
class _AlHardwareCageTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,120))
_AlHardwareCageTemp_Type.__name__=_E
_AlHardwareCageTemp_Object=MibScalar
alHardwareCageTemp=_AlHardwareCageTemp_Object((1,3,6,1,4,1,3076,2,1,2,22,1,33),_AlHardwareCageTemp_Type())
alHardwareCageTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCageTemp.setStatus(_A)
if mibBuilder.loadTexts:alHardwareCageTemp.setUnits(_H)
_AlHardwareCageTempAlarm_Type=TruthValue
_AlHardwareCageTempAlarm_Object=MibScalar
alHardwareCageTempAlarm=_AlHardwareCageTempAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,34),_AlHardwareCageTempAlarm_Type())
alHardwareCageTempAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCageTempAlarm.setStatus(_A)
_AlHardwareCageTempCount_Type=Counter32
_AlHardwareCageTempCount_Object=MibScalar
alHardwareCageTempCount=_AlHardwareCageTempCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,35),_AlHardwareCageTempCount_Type())
alHardwareCageTempCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCageTempCount.setStatus(_A)
_AlHardwareCageTempTime_Type=TimeTicks
_AlHardwareCageTempTime_Object=MibScalar
alHardwareCageTempTime=_AlHardwareCageTempTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,36),_AlHardwareCageTempTime_Type())
alHardwareCageTempTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCageTempTime.setStatus(_A)
_AlHardwareFan1Rpm_Type=Gauge32
_AlHardwareFan1Rpm_Object=MibScalar
alHardwareFan1Rpm=_AlHardwareFan1Rpm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,37),_AlHardwareFan1Rpm_Type())
alHardwareFan1Rpm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan1Rpm.setStatus(_A)
if mibBuilder.loadTexts:alHardwareFan1Rpm.setUnits(_G)
_AlHardwareFan1RpmAlarm_Type=TruthValue
_AlHardwareFan1RpmAlarm_Object=MibScalar
alHardwareFan1RpmAlarm=_AlHardwareFan1RpmAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,38),_AlHardwareFan1RpmAlarm_Type())
alHardwareFan1RpmAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan1RpmAlarm.setStatus(_A)
_AlHardwareFan1RpmCount_Type=Counter32
_AlHardwareFan1RpmCount_Object=MibScalar
alHardwareFan1RpmCount=_AlHardwareFan1RpmCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,39),_AlHardwareFan1RpmCount_Type())
alHardwareFan1RpmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan1RpmCount.setStatus(_A)
_AlHardwareFan1RpmTime_Type=TimeTicks
_AlHardwareFan1RpmTime_Object=MibScalar
alHardwareFan1RpmTime=_AlHardwareFan1RpmTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,40),_AlHardwareFan1RpmTime_Type())
alHardwareFan1RpmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan1RpmTime.setStatus(_A)
_AlHardwareFan2Rpm_Type=Gauge32
_AlHardwareFan2Rpm_Object=MibScalar
alHardwareFan2Rpm=_AlHardwareFan2Rpm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,41),_AlHardwareFan2Rpm_Type())
alHardwareFan2Rpm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan2Rpm.setStatus(_A)
if mibBuilder.loadTexts:alHardwareFan2Rpm.setUnits(_G)
_AlHardwareFan2RpmAlarm_Type=TruthValue
_AlHardwareFan2RpmAlarm_Object=MibScalar
alHardwareFan2RpmAlarm=_AlHardwareFan2RpmAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,42),_AlHardwareFan2RpmAlarm_Type())
alHardwareFan2RpmAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan2RpmAlarm.setStatus(_A)
_AlHardwareFan2RpmCount_Type=Counter32
_AlHardwareFan2RpmCount_Object=MibScalar
alHardwareFan2RpmCount=_AlHardwareFan2RpmCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,43),_AlHardwareFan2RpmCount_Type())
alHardwareFan2RpmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan2RpmCount.setStatus(_A)
_AlHardwareFan2RpmTime_Type=TimeTicks
_AlHardwareFan2RpmTime_Object=MibScalar
alHardwareFan2RpmTime=_AlHardwareFan2RpmTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,44),_AlHardwareFan2RpmTime_Type())
alHardwareFan2RpmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan2RpmTime.setStatus(_A)
_AlHardwareFan3Rpm_Type=Gauge32
_AlHardwareFan3Rpm_Object=MibScalar
alHardwareFan3Rpm=_AlHardwareFan3Rpm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,45),_AlHardwareFan3Rpm_Type())
alHardwareFan3Rpm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan3Rpm.setStatus(_A)
if mibBuilder.loadTexts:alHardwareFan3Rpm.setUnits(_G)
_AlHardwareFan3RpmAlarm_Type=TruthValue
_AlHardwareFan3RpmAlarm_Object=MibScalar
alHardwareFan3RpmAlarm=_AlHardwareFan3RpmAlarm_Object((1,3,6,1,4,1,3076,2,1,2,22,1,46),_AlHardwareFan3RpmAlarm_Type())
alHardwareFan3RpmAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan3RpmAlarm.setStatus(_A)
_AlHardwareFan3RpmCount_Type=Counter32
_AlHardwareFan3RpmCount_Object=MibScalar
alHardwareFan3RpmCount=_AlHardwareFan3RpmCount_Object((1,3,6,1,4,1,3076,2,1,2,22,1,47),_AlHardwareFan3RpmCount_Type())
alHardwareFan3RpmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan3RpmCount.setStatus(_A)
_AlHardwareFan3RpmTime_Type=TimeTicks
_AlHardwareFan3RpmTime_Object=MibScalar
alHardwareFan3RpmTime=_AlHardwareFan3RpmTime_Object((1,3,6,1,4,1,3076,2,1,2,22,1,48),_AlHardwareFan3RpmTime_Type())
alHardwareFan3RpmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareFan3RpmTime.setStatus(_A)
class _AlHardwarePs1Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('ac',2)))
_AlHardwarePs1Type_Type.__name__=_E
_AlHardwarePs1Type_Object=MibScalar
alHardwarePs1Type=_AlHardwarePs1Type_Object((1,3,6,1,4,1,3076,2,1,2,22,1,49),_AlHardwarePs1Type_Type())
alHardwarePs1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs1Type.setStatus(_A)
class _AlHardwarePs2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('ac',2)))
_AlHardwarePs2Type_Type.__name__=_E
_AlHardwarePs2Type_Object=MibScalar
alHardwarePs2Type=_AlHardwarePs2Type_Object((1,3,6,1,4,1,3076,2,1,2,22,1,50),_AlHardwarePs2Type_Type())
alHardwarePs2Type.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwarePs2Type.setStatus(_A)
_AlHardwareSlot1Card_Type=ConcentratorCard
_AlHardwareSlot1Card_Object=MibScalar
alHardwareSlot1Card=_AlHardwareSlot1Card_Object((1,3,6,1,4,1,3076,2,1,2,22,1,51),_AlHardwareSlot1Card_Type())
alHardwareSlot1Card.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot1Card.setStatus(_A)
_AlHardwareSlot2Card_Type=ConcentratorCard
_AlHardwareSlot2Card_Object=MibScalar
alHardwareSlot2Card=_AlHardwareSlot2Card_Object((1,3,6,1,4,1,3076,2,1,2,22,1,52),_AlHardwareSlot2Card_Type())
alHardwareSlot2Card.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot2Card.setStatus(_A)
_AlHardwareSlot3Card_Type=ConcentratorCard
_AlHardwareSlot3Card_Object=MibScalar
alHardwareSlot3Card=_AlHardwareSlot3Card_Object((1,3,6,1,4,1,3076,2,1,2,22,1,53),_AlHardwareSlot3Card_Type())
alHardwareSlot3Card.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot3Card.setStatus(_A)
_AlHardwareSlot4Card_Type=ConcentratorCard
_AlHardwareSlot4Card_Object=MibScalar
alHardwareSlot4Card=_AlHardwareSlot4Card_Object((1,3,6,1,4,1,3076,2,1,2,22,1,54),_AlHardwareSlot4Card_Type())
alHardwareSlot4Card.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot4Card.setStatus(_A)
_AlHardwareSlot1Operational_Type=TruthValue
_AlHardwareSlot1Operational_Object=MibScalar
alHardwareSlot1Operational=_AlHardwareSlot1Operational_Object((1,3,6,1,4,1,3076,2,1,2,22,1,55),_AlHardwareSlot1Operational_Type())
alHardwareSlot1Operational.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot1Operational.setStatus(_A)
_AlHardwareSlot2Operational_Type=TruthValue
_AlHardwareSlot2Operational_Object=MibScalar
alHardwareSlot2Operational=_AlHardwareSlot2Operational_Object((1,3,6,1,4,1,3076,2,1,2,22,1,56),_AlHardwareSlot2Operational_Type())
alHardwareSlot2Operational.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot2Operational.setStatus(_A)
_AlHardwareSlot3Operational_Type=TruthValue
_AlHardwareSlot3Operational_Object=MibScalar
alHardwareSlot3Operational=_AlHardwareSlot3Operational_Object((1,3,6,1,4,1,3076,2,1,2,22,1,57),_AlHardwareSlot3Operational_Type())
alHardwareSlot3Operational.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot3Operational.setStatus(_A)
_AlHardwareSlot4Operational_Type=TruthValue
_AlHardwareSlot4Operational_Object=MibScalar
alHardwareSlot4Operational=_AlHardwareSlot4Operational_Object((1,3,6,1,4,1,3076,2,1,2,22,1,58),_AlHardwareSlot4Operational_Type())
alHardwareSlot4Operational.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSlot4Operational.setStatus(_A)
_AlHardwareRamSize_Type=Unsigned32
_AlHardwareRamSize_Object=MibScalar
alHardwareRamSize=_AlHardwareRamSize_Object((1,3,6,1,4,1,3076,2,1,2,22,1,59),_AlHardwareRamSize_Type())
alHardwareRamSize.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareRamSize.setStatus(_A)
if mibBuilder.loadTexts:alHardwareRamSize.setUnits('MB')
_AlHardwareChassis_Type=ConcentratorType
_AlHardwareChassis_Object=MibScalar
alHardwareChassis=_AlHardwareChassis_Object((1,3,6,1,4,1,3076,2,1,2,22,1,60),_AlHardwareChassis_Type())
alHardwareChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareChassis.setStatus(_A)
_AlHardwareCpuVoltageNominal_Type=Gauge32
_AlHardwareCpuVoltageNominal_Object=MibScalar
alHardwareCpuVoltageNominal=_AlHardwareCpuVoltageNominal_Object((1,3,6,1,4,1,3076,2,1,2,22,1,61),_AlHardwareCpuVoltageNominal_Type())
alHardwareCpuVoltageNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareCpuVoltageNominal.setStatus(_A)
if mibBuilder.loadTexts:alHardwareCpuVoltageNominal.setUnits(_D)
_AlHardwareClientEthPrivSwitch_Type=TruthValue
_AlHardwareClientEthPrivSwitch_Object=MibScalar
alHardwareClientEthPrivSwitch=_AlHardwareClientEthPrivSwitch_Object((1,3,6,1,4,1,3076,2,1,2,22,1,62),_AlHardwareClientEthPrivSwitch_Type())
alHardwareClientEthPrivSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareClientEthPrivSwitch.setStatus(_A)
_AlHardwareSerialNumber_Type=DisplayString
_AlHardwareSerialNumber_Object=MibScalar
alHardwareSerialNumber=_AlHardwareSerialNumber_Object((1,3,6,1,4,1,3076,2,1,2,22,1,63),_AlHardwareSerialNumber_Type())
alHardwareSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alHardwareSerialNumber.setStatus(_A)
altigaHardwareStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,22,2))
altigaHardwareStatsGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:altigaHardwareStatsGroup.setStatus(_A)
altigaHardwareStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,27,2,1,1,1))
altigaHardwareStatsMibCompliance.setObjects((_B,_AJ))
if mibBuilder.loadTexts:altigaHardwareStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConcentratorCard':ConcentratorCard,'ConcentratorType':ConcentratorType,'altigaHardwareStatsMibModule':altigaHardwareStatsMibModule,'altigaHardwareStatsMibConformance':altigaHardwareStatsMibConformance,'altigaHardwareStatsMibCompliances':altigaHardwareStatsMibCompliances,'altigaHardwareStatsMibCompliance':altigaHardwareStatsMibCompliance,_AJ:altigaHardwareStatsGroup,'alStatsHardwareGlobal':alStatsHardwareGlobal,_I:alHardwareCpuVoltage,_J:alHardwareCpuVoltageAlarm,_K:alHardwareCpuVoltageCount,_L:alHardwareCpuVoltageTime,_M:alHardwarePs1Voltage3v,_N:alHardwarePs1Voltage3vAlarm,_O:alHardwarePs1Voltage3vCount,_P:alHardwarePs1Voltage3vTime,_Q:alHardwarePs1Voltage5v,_R:alHardwarePs1Voltage5vAlarm,_S:alHardwarePs1Voltage5vCount,_T:alHardwarePs1Voltage5vTime,_U:alHardwarePs2Voltage3v,_V:alHardwarePs2Voltage3vAlarm,_W:alHardwarePs2Voltage3vCount,_X:alHardwarePs2Voltage3vTime,_Y:alHardwarePs2Voltage5v,_Z:alHardwarePs2Voltage5vAlarm,_a:alHardwarePs2Voltage5vCount,_b:alHardwarePs2Voltage5vTime,_c:alHardwareBoardVoltage3v,_d:alHardwareBoardVoltage3vAlarm,_e:alHardwareBoardVoltage3vCount,_f:alHardwareBoardVoltage3vTime,_g:alHardwareBoardVoltage5v,_h:alHardwareBoardVoltage5vAlarm,_i:alHardwareBoardVoltage5vCount,_j:alHardwareBoardVoltage5vTime,_k:alHardwareCpuTemp,_l:alHardwareCpuTempAlarm,_m:alHardwareCpuTempCount,_n:alHardwareCpuTempTime,_o:alHardwareCageTemp,_p:alHardwareCageTempAlarm,_q:alHardwareCageTempCount,_r:alHardwareCageTempTime,_s:alHardwareFan1Rpm,_t:alHardwareFan1RpmAlarm,_u:alHardwareFan1RpmCount,_v:alHardwareFan1RpmTime,_w:alHardwareFan2Rpm,_x:alHardwareFan2RpmAlarm,_y:alHardwareFan2RpmCount,_z:alHardwareFan2RpmTime,_A0:alHardwareFan3Rpm,_A1:alHardwareFan3RpmAlarm,_A2:alHardwareFan3RpmCount,_A3:alHardwareFan3RpmTime,_A4:alHardwarePs1Type,_A5:alHardwarePs2Type,_A6:alHardwareSlot1Card,_A7:alHardwareSlot2Card,_A8:alHardwareSlot3Card,_A9:alHardwareSlot4Card,_AA:alHardwareSlot1Operational,_AB:alHardwareSlot2Operational,_AC:alHardwareSlot3Operational,_AD:alHardwareSlot4Operational,_AE:alHardwareRamSize,_AF:alHardwareChassis,_AG:alHardwareCpuVoltageNominal,_AH:alHardwareClientEthPrivSwitch,_AI:alHardwareSerialNumber})