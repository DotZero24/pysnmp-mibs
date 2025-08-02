_G='min'
_F='C x10'
_E='read-only'
_D='read-write'
_C='N/A'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols('SNMPv2-MIB','sysContact','sysLocation','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ir32un_tMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_C)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_C)
_Instruments_ObjectIdentity=ObjectIdentity
instruments=_Instruments_ObjectIdentity((1,3,6,1,4,1,9839,2))
_WebGateInfo_ObjectIdentity=ObjectIdentity
webGateInfo=_WebGateInfo_ObjectIdentity((1,3,6,1,4,1,9839,2,0))
_AgentParameters_ObjectIdentity=ObjectIdentity
agentParameters=_AgentParameters_ObjectIdentity((1,3,6,1,4,1,9839,2,0,1))
class _NetSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NetSize_Type.__name__=_B
_NetSize_Object=MibScalar
netSize=_NetSize_Object((1,3,6,1,4,1,9839,2,0,1,1),_NetSize_Type())
netSize.setMaxAccess(_D)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_C)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_C)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_C)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_C)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_C)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_C)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_C)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_C)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_C)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_C)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_C)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Stato_id_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_id_1_Type.__name__=_B
_Stato_id_1_Object=MibScalar
stato_id_1=_Stato_id_1_Object((1,3,6,1,4,1,9839,2,1,1,1),_Stato_id_1_Type())
stato_id_1.setMaxAccess(_E)
if mibBuilder.loadTexts:stato_id_1.setStatus(_A)
if mibBuilder.loadTexts:stato_id_1.setUnits(_C)
class _Stato_id_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_id_2_Type.__name__=_B
_Stato_id_2_Object=MibScalar
stato_id_2=_Stato_id_2_Object((1,3,6,1,4,1,9839,2,1,1,2),_Stato_id_2_Type())
stato_id_2.setMaxAccess(_E)
if mibBuilder.loadTexts:stato_id_2.setStatus(_A)
if mibBuilder.loadTexts:stato_id_2.setUnits(_C)
class _Stato_ud_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_ud_1_Type.__name__=_B
_Stato_ud_1_Object=MibScalar
stato_ud_1=_Stato_ud_1_Object((1,3,6,1,4,1,9839,2,1,1,3),_Stato_ud_1_Type())
stato_ud_1.setMaxAccess(_E)
if mibBuilder.loadTexts:stato_ud_1.setStatus(_A)
if mibBuilder.loadTexts:stato_ud_1.setUnits(_C)
class _Stato_ud_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_ud_2_Type.__name__=_B
_Stato_ud_2_Object=MibScalar
stato_ud_2=_Stato_ud_2_Object((1,3,6,1,4,1,9839,2,1,1,4),_Stato_ud_2_Type())
stato_ud_2.setMaxAccess(_E)
if mibBuilder.loadTexts:stato_ud_2.setStatus(_A)
if mibBuilder.loadTexts:stato_ud_2.setUnits(_C)
class _Stato_ud_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_ud_3_Type.__name__=_B
_Stato_ud_3_Object=MibScalar
stato_ud_3=_Stato_ud_3_Object((1,3,6,1,4,1,9839,2,1,1,5),_Stato_ud_3_Type())
stato_ud_3.setMaxAccess(_E)
if mibBuilder.loadTexts:stato_ud_3.setStatus(_A)
if mibBuilder.loadTexts:stato_ud_3.setUnits(_C)
class _Stato_ud_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_ud_4_Type.__name__=_B
_Stato_ud_4_Object=MibScalar
stato_ud_4=_Stato_ud_4_Object((1,3,6,1,4,1,9839,2,1,1,6),_Stato_ud_4_Type())
stato_ud_4.setMaxAccess(_E)
if mibBuilder.loadTexts:stato_ud_4.setStatus(_A)
if mibBuilder.loadTexts:stato_ud_4.setUnits(_C)
class _All_sonda_0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sonda_0_Type.__name__=_B
_All_sonda_0_Object=MibScalar
all_sonda_0=_All_sonda_0_Object((1,3,6,1,4,1,9839,2,1,1,8),_All_sonda_0_Type())
all_sonda_0.setMaxAccess(_E)
if mibBuilder.loadTexts:all_sonda_0.setStatus(_A)
if mibBuilder.loadTexts:all_sonda_0.setUnits(_C)
class _All_sonda_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sonda_1_Type.__name__=_B
_All_sonda_1_Object=MibScalar
all_sonda_1=_All_sonda_1_Object((1,3,6,1,4,1,9839,2,1,1,9),_All_sonda_1_Type())
all_sonda_1.setMaxAccess(_E)
if mibBuilder.loadTexts:all_sonda_1.setStatus(_A)
if mibBuilder.loadTexts:all_sonda_1.setUnits(_C)
class _All_eeprom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_eeprom_Type.__name__=_B
_All_eeprom_Object=MibScalar
all_eeprom=_All_eeprom_Object((1,3,6,1,4,1,9839,2,1,1,10),_All_eeprom_Type())
all_eeprom.setMaxAccess(_E)
if mibBuilder.loadTexts:all_eeprom.setStatus(_A)
if mibBuilder.loadTexts:all_eeprom.setUnits(_C)
class _All_id_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_id_1_Type.__name__=_B
_All_id_1_Object=MibScalar
all_id_1=_All_id_1_Object((1,3,6,1,4,1,9839,2,1,1,11),_All_id_1_Type())
all_id_1.setMaxAccess(_E)
if mibBuilder.loadTexts:all_id_1.setStatus(_A)
if mibBuilder.loadTexts:all_id_1.setUnits(_C)
class _All_alta_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_alta_temp_Type.__name__=_B
_All_alta_temp_Object=MibScalar
all_alta_temp=_All_alta_temp_Object((1,3,6,1,4,1,9839,2,1,1,12),_All_alta_temp_Type())
all_alta_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:all_alta_temp.setStatus(_A)
if mibBuilder.loadTexts:all_alta_temp.setUnits(_C)
class _All_bassa_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_bassa_temp_Type.__name__=_B
_All_bassa_temp_Object=MibScalar
all_bassa_temp=_All_bassa_temp_Object((1,3,6,1,4,1,9839,2,1,1,13),_All_bassa_temp_Type())
all_bassa_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:all_bassa_temp.setStatus(_A)
if mibBuilder.loadTexts:all_bassa_temp.setUnits(_C)
class _Prop_prop_int_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Prop_prop_int_Type.__name__=_B
_Prop_prop_int_Object=MibScalar
prop_prop_int=_Prop_prop_int_Object((1,3,6,1,4,1,9839,2,1,1,14),_Prop_prop_int_Type())
prop_prop_int.setMaxAccess(_D)
if mibBuilder.loadTexts:prop_prop_int.setStatus(_A)
if mibBuilder.loadTexts:prop_prop_int.setUnits(_C)
class _Tipo_sonda_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tipo_sonda_Type.__name__=_B
_Tipo_sonda_Object=MibScalar
tipo_sonda=_Tipo_sonda_Object((1,3,6,1,4,1,9839,2,1,1,15),_Tipo_sonda_Type())
tipo_sonda.setMaxAccess(_D)
if mibBuilder.loadTexts:tipo_sonda.setStatus(_A)
if mibBuilder.loadTexts:tipo_sonda.setUnits(_C)
class _Celsius_farhan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Celsius_farhan_Type.__name__=_B
_Celsius_farhan_Object=MibScalar
celsius_farhan=_Celsius_farhan_Object((1,3,6,1,4,1,9839,2,1,1,16),_Celsius_farhan_Type())
celsius_farhan.setMaxAccess(_D)
if mibBuilder.loadTexts:celsius_farhan.setStatus(_A)
if mibBuilder.loadTexts:celsius_farhan.setUnits(_C)
class _Modo_speciale_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Modo_speciale_Type.__name__=_B
_Modo_speciale_Object=MibScalar
modo_speciale=_Modo_speciale_Object((1,3,6,1,4,1,9839,2,1,1,17),_Modo_speciale_Type())
modo_speciale.setMaxAccess(_D)
if mibBuilder.loadTexts:modo_speciale.setStatus(_A)
if mibBuilder.loadTexts:modo_speciale.setUnits(_C)
class _Tipo_out_grad4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tipo_out_grad4_Type.__name__=_B
_Tipo_out_grad4_Object=MibScalar
tipo_out_grad4=_Tipo_out_grad4_Object((1,3,6,1,4,1,9839,2,1,1,18),_Tipo_out_grad4_Type())
tipo_out_grad4.setMaxAccess(_D)
if mibBuilder.loadTexts:tipo_out_grad4.setStatus(_A)
if mibBuilder.loadTexts:tipo_out_grad4.setUnits(_C)
class _Tipo_out_grad3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tipo_out_grad3_Type.__name__=_B
_Tipo_out_grad3_Object=MibScalar
tipo_out_grad3=_Tipo_out_grad3_Object((1,3,6,1,4,1,9839,2,1,1,19),_Tipo_out_grad3_Type())
tipo_out_grad3.setMaxAccess(_D)
if mibBuilder.loadTexts:tipo_out_grad3.setStatus(_A)
if mibBuilder.loadTexts:tipo_out_grad3.setUnits(_C)
class _Tipo_out_grad2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tipo_out_grad2_Type.__name__=_B
_Tipo_out_grad2_Object=MibScalar
tipo_out_grad2=_Tipo_out_grad2_Object((1,3,6,1,4,1,9839,2,1,1,20),_Tipo_out_grad2_Type())
tipo_out_grad2.setMaxAccess(_D)
if mibBuilder.loadTexts:tipo_out_grad2.setStatus(_A)
if mibBuilder.loadTexts:tipo_out_grad2.setUnits(_C)
class _Tipo_out_grad1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tipo_out_grad1_Type.__name__=_B
_Tipo_out_grad1_Object=MibScalar
tipo_out_grad1=_Tipo_out_grad1_Object((1,3,6,1,4,1,9839,2,1,1,21),_Tipo_out_grad1_Type())
tipo_out_grad1.setMaxAccess(_D)
if mibBuilder.loadTexts:tipo_out_grad1.setStatus(_A)
if mibBuilder.loadTexts:tipo_out_grad1.setUnits(_C)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Ing_sonda_0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ing_sonda_0_Type.__name__=_B
_Ing_sonda_0_Object=MibScalar
ing_sonda_0=_Ing_sonda_0_Object((1,3,6,1,4,1,9839,2,1,2,1),_Ing_sonda_0_Type())
ing_sonda_0.setMaxAccess(_E)
if mibBuilder.loadTexts:ing_sonda_0.setStatus(_A)
if mibBuilder.loadTexts:ing_sonda_0.setUnits(_F)
class _Ing_sonda_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ing_sonda_1_Type.__name__=_B
_Ing_sonda_1_Object=MibScalar
ing_sonda_1=_Ing_sonda_1_Object((1,3,6,1,4,1,9839,2,1,2,2),_Ing_sonda_1_Type())
ing_sonda_1.setMaxAccess(_E)
if mibBuilder.loadTexts:ing_sonda_1.setStatus(_A)
if mibBuilder.loadTexts:ing_sonda_1.setUnits(_F)
class _Set_point1_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_point1_Type.__name__=_B
_Set_point1_Object=MibScalar
set_point1=_Set_point1_Object((1,3,6,1,4,1,9839,2,1,2,3),_Set_point1_Type())
set_point1.setMaxAccess(_D)
if mibBuilder.loadTexts:set_point1.setStatus(_A)
if mibBuilder.loadTexts:set_point1.setUnits(_F)
class _Set_point2_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_point2_Type.__name__=_B
_Set_point2_Object=MibScalar
set_point2=_Set_point2_Object((1,3,6,1,4,1,9839,2,1,2,4),_Set_point2_Type())
set_point2.setMaxAccess(_D)
if mibBuilder.loadTexts:set_point2.setStatus(_A)
if mibBuilder.loadTexts:set_point2.setUnits(_F)
class _Differenziale1_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_Differenziale1_Type.__name__=_B
_Differenziale1_Object=MibScalar
differenziale1=_Differenziale1_Object((1,3,6,1,4,1,9839,2,1,2,5),_Differenziale1_Type())
differenziale1.setMaxAccess(_D)
if mibBuilder.loadTexts:differenziale1.setStatus(_A)
if mibBuilder.loadTexts:differenziale1.setUnits(_F)
class _Differenziale2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_Differenziale2_Type.__name__=_B
_Differenziale2_Object=MibScalar
differenziale2=_Differenziale2_Object((1,3,6,1,4,1,9839,2,1,2,6),_Differenziale2_Type())
differenziale2.setMaxAccess(_D)
if mibBuilder.loadTexts:differenziale2.setStatus(_A)
if mibBuilder.loadTexts:differenziale2.setUnits(_F)
class _Zona_morta_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Zona_morta_Type.__name__=_B
_Zona_morta_Object=MibScalar
zona_morta=_Zona_morta_Object((1,3,6,1,4,1,9839,2,1,2,7),_Zona_morta_Type())
zona_morta.setMaxAccess(_D)
if mibBuilder.loadTexts:zona_morta.setStatus(_A)
if mibBuilder.loadTexts:zona_morta.setUnits(_F)
class _Offset_sonda_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Offset_sonda_Type.__name__=_B
_Offset_sonda_Object=MibScalar
offset_sonda=_Offset_sonda_Object((1,3,6,1,4,1,9839,2,1,2,8),_Offset_sonda_Type())
offset_sonda.setMaxAccess(_D)
if mibBuilder.loadTexts:offset_sonda.setStatus(_A)
if mibBuilder.loadTexts:offset_sonda.setUnits(_F)
class _Sog_bassa_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,32767))
_Sog_bassa_temp_Type.__name__=_B
_Sog_bassa_temp_Object=MibScalar
sog_bassa_temp=_Sog_bassa_temp_Object((1,3,6,1,4,1,9839,2,1,2,9),_Sog_bassa_temp_Type())
sog_bassa_temp.setMaxAccess(_D)
if mibBuilder.loadTexts:sog_bassa_temp.setStatus(_A)
if mibBuilder.loadTexts:sog_bassa_temp.setUnits(_F)
class _Sog_alta_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,9990))
_Sog_alta_temp_Type.__name__=_B
_Sog_alta_temp_Object=MibScalar
sog_alta_temp=_Sog_alta_temp_Object((1,3,6,1,4,1,9839,2,1,2,10),_Sog_alta_temp_Type())
sog_alta_temp.setMaxAccess(_D)
if mibBuilder.loadTexts:sog_alta_temp.setStatus(_A)
if mibBuilder.loadTexts:sog_alta_temp.setUnits(_F)
class _Differenz_all_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,990))
_Differenz_all_Type.__name__=_B
_Differenz_all_Object=MibScalar
differenz_all=_Differenz_all_Object((1,3,6,1,4,1,9839,2,1,2,11),_Differenz_all_Type())
differenz_all.setMaxAccess(_D)
if mibBuilder.loadTexts:differenz_all.setStatus(_A)
if mibBuilder.loadTexts:differenz_all.setUnits(_F)
class _Tempo_di_pwm_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,9990))
_Tempo_di_pwm_Type.__name__=_B
_Tempo_di_pwm_Object=MibScalar
tempo_di_pwm=_Tempo_di_pwm_Object((1,3,6,1,4,1,9839,2,1,2,12),_Tempo_di_pwm_Type())
tempo_di_pwm.setMaxAccess(_D)
if mibBuilder.loadTexts:tempo_di_pwm.setStatus(_A)
if mibBuilder.loadTexts:tempo_di_pwm.setUnits('sec-0.2 x10')
class _Val_minimo_av_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,32767))
_Val_minimo_av_Type.__name__=_B
_Val_minimo_av_Object=MibScalar
val_minimo_av=_Val_minimo_av_Object((1,3,6,1,4,1,9839,2,1,2,13),_Val_minimo_av_Type())
val_minimo_av.setMaxAccess(_D)
if mibBuilder.loadTexts:val_minimo_av.setStatus(_A)
if mibBuilder.loadTexts:val_minimo_av.setUnits(_C)
class _Val_massimo_av_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,9990))
_Val_massimo_av_Type.__name__=_B
_Val_massimo_av_Object=MibScalar
val_massimo_av=_Val_massimo_av_Object((1,3,6,1,4,1,9839,2,1,2,14),_Val_massimo_av_Type())
val_massimo_av.setMaxAccess(_D)
if mibBuilder.loadTexts:val_massimo_av.setStatus(_A)
if mibBuilder.loadTexts:val_massimo_av.setUnits(_C)
class _Set1_min_ok_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,32767))
_Set1_min_ok_Type.__name__=_B
_Set1_min_ok_Object=MibScalar
set1_min_ok=_Set1_min_ok_Object((1,3,6,1,4,1,9839,2,1,2,15),_Set1_min_ok_Type())
set1_min_ok.setMaxAccess(_D)
if mibBuilder.loadTexts:set1_min_ok.setStatus(_A)
if mibBuilder.loadTexts:set1_min_ok.setUnits(_F)
class _Set1_max_ok_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,9990))
_Set1_max_ok_Type.__name__=_B
_Set1_max_ok_Object=MibScalar
set1_max_ok=_Set1_max_ok_Object((1,3,6,1,4,1,9839,2,1,2,16),_Set1_max_ok_Type())
set1_max_ok.setMaxAccess(_D)
if mibBuilder.loadTexts:set1_max_ok.setStatus(_A)
if mibBuilder.loadTexts:set1_max_ok.setUnits(_F)
class _Set2_min_ok_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,32767))
_Set2_min_ok_Type.__name__=_B
_Set2_min_ok_Object=MibScalar
set2_min_ok=_Set2_min_ok_Object((1,3,6,1,4,1,9839,2,1,2,17),_Set2_min_ok_Type())
set2_min_ok.setMaxAccess(_D)
if mibBuilder.loadTexts:set2_min_ok.setStatus(_A)
if mibBuilder.loadTexts:set2_min_ok.setUnits(_F)
class _Set2_max_ok_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,9990))
_Set2_max_ok_Type.__name__=_B
_Set2_max_ok_Object=MibScalar
set2_max_ok=_Set2_max_ok_Object((1,3,6,1,4,1,9839,2,1,2,18),_Set2_max_ok_Type())
set2_max_ok.setMaxAccess(_D)
if mibBuilder.loadTexts:set2_max_ok.setStatus(_A)
if mibBuilder.loadTexts:set2_max_ok.setUnits(_F)
class _Autorita_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_Autorita_Type.__name__=_B
_Autorita_Object=MibScalar
autorita=_Autorita_Object((1,3,6,1,4,1,9839,2,1,2,19),_Autorita_Type())
autorita.setMaxAccess(_D)
if mibBuilder.loadTexts:autorita.setStatus(_A)
if mibBuilder.loadTexts:autorita.setUnits(_C)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Modo_funz_c0_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_Modo_funz_c0_Type.__name__=_B
_Modo_funz_c0_Object=MibScalar
modo_funz_c0=_Modo_funz_c0_Object((1,3,6,1,4,1,9839,2,1,3,1),_Modo_funz_c0_Type())
modo_funz_c0.setMaxAccess(_D)
if mibBuilder.loadTexts:modo_funz_c0.setStatus(_A)
if mibBuilder.loadTexts:modo_funz_c0.setUnits(_C)
class _Rit_2ins_c6_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Rit_2ins_c6_Type.__name__=_B
_Rit_2ins_c6_Object=MibScalar
rit_2ins_c6=_Rit_2ins_c6_Object((1,3,6,1,4,1,9839,2,1,3,2),_Rit_2ins_c6_Type())
rit_2ins_c6.setMaxAccess(_D)
if mibBuilder.loadTexts:rit_2ins_c6.setStatus(_A)
if mibBuilder.loadTexts:rit_2ins_c6.setUnits('sec')
class _Tmin_2out_c7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Tmin_2out_c7_Type.__name__=_B
_Tmin_2out_c7_Object=MibScalar
tmin_2out_c7=_Tmin_2out_c7_Object((1,3,6,1,4,1,9839,2,1,3,3),_Tmin_2out_c7_Type())
tmin_2out_c7.setMaxAccess(_D)
if mibBuilder.loadTexts:tmin_2out_c7.setStatus(_A)
if mibBuilder.loadTexts:tmin_2out_c7.setUnits(_G)
class _Tmin_off_out_c8_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Tmin_off_out_c8_Type.__name__=_B
_Tmin_off_out_c8_Object=MibScalar
tmin_off_out_c8=_Tmin_off_out_c8_Object((1,3,6,1,4,1,9839,2,1,3,4),_Tmin_off_out_c8_Type())
tmin_off_out_c8.setMaxAccess(_D)
if mibBuilder.loadTexts:tmin_off_out_c8.setStatus(_A)
if mibBuilder.loadTexts:tmin_off_out_c8.setUnits(_G)
class _Tmin_on_c9_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Tmin_on_c9_Type.__name__=_B
_Tmin_on_c9_Object=MibScalar
tmin_on_c9=_Tmin_on_c9_Object((1,3,6,1,4,1,9839,2,1,3,5),_Tmin_on_c9_Type())
tmin_on_c9.setMaxAccess(_D)
if mibBuilder.loadTexts:tmin_on_c9.setStatus(_A)
if mibBuilder.loadTexts:tmin_on_c9.setUnits(_G)
class _Sicur_sonde_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Sicur_sonde_Type.__name__=_B
_Sicur_sonde_Object=MibScalar
sicur_sonde=_Sicur_sonde_Object((1,3,6,1,4,1,9839,2,1,3,6),_Sicur_sonde_Type())
sicur_sonde.setMaxAccess(_D)
if mibBuilder.loadTexts:sicur_sonde.setStatus(_A)
if mibBuilder.loadTexts:sicur_sonde.setUnits(_C)
class _Rotazione_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Rotazione_Type.__name__=_B
_Rotazione_Object=MibScalar
rotazione=_Rotazione_Object((1,3,6,1,4,1,9839,2,1,3,7),_Rotazione_Type())
rotazione.setMaxAccess(_D)
if mibBuilder.loadTexts:rotazione.setStatus(_A)
if mibBuilder.loadTexts:rotazione.setUnits(_C)
class _Velocita_sonda_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_Velocita_sonda_Type.__name__=_B
_Velocita_sonda_Object=MibScalar
velocita_sonda=_Velocita_sonda_Object((1,3,6,1,4,1,9839,2,1,3,8),_Velocita_sonda_Type())
velocita_sonda.setMaxAccess(_D)
if mibBuilder.loadTexts:velocita_sonda.setStatus(_A)
if mibBuilder.loadTexts:velocita_sonda.setUnits(_C)
class _Presenza_sonda_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Presenza_sonda_Type.__name__=_B
_Presenza_sonda_Object=MibScalar
presenza_sonda=_Presenza_sonda_Object((1,3,6,1,4,1,9839,2,1,3,9),_Presenza_sonda_Type())
presenza_sonda.setMaxAccess(_D)
if mibBuilder.loadTexts:presenza_sonda.setStatus(_A)
if mibBuilder.loadTexts:presenza_sonda.setUnits(_C)
class _Tempo_allarme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Tempo_allarme_Type.__name__=_B
_Tempo_allarme_Object=MibScalar
tempo_allarme=_Tempo_allarme_Object((1,3,6,1,4,1,9839,2,1,3,10),_Tempo_allarme_Type())
tempo_allarme.setMaxAccess(_D)
if mibBuilder.loadTexts:tempo_allarme.setStatus(_A)
if mibBuilder.loadTexts:tempo_allarme.setUnits(_G)
class _Gestione_id1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Gestione_id1_Type.__name__=_B
_Gestione_id1_Object=MibScalar
gestione_id1=_Gestione_id1_Object((1,3,6,1,4,1,9839,2,1,3,11),_Gestione_id1_Type())
gestione_id1.setMaxAccess(_D)
if mibBuilder.loadTexts:gestione_id1.setStatus(_A)
if mibBuilder.loadTexts:gestione_id1.setUnits(_C)
class _Gestione_id2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Gestione_id2_Type.__name__=_B
_Gestione_id2_Object=MibScalar
gestione_id2=_Gestione_id2_Object((1,3,6,1,4,1,9839,2,1,3,12),_Gestione_id2_Type())
gestione_id2.setMaxAccess(_D)
if mibBuilder.loadTexts:gestione_id2.setStatus(_A)
if mibBuilder.loadTexts:gestione_id2.setUnits(_C)
class _Sicur_all_id_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Sicur_all_id_Type.__name__=_B
_Sicur_all_id_Object=MibScalar
sicur_all_id=_Sicur_all_id_Object((1,3,6,1,4,1,9839,2,1,3,13),_Sicur_all_id_Type())
sicur_all_id.setMaxAccess(_D)
if mibBuilder.loadTexts:sicur_all_id.setStatus(_A)
if mibBuilder.loadTexts:sicur_all_id.setUnits(_C)
class _Set_gradino1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Set_gradino1_Type.__name__=_B
_Set_gradino1_Object=MibScalar
set_gradino1=_Set_gradino1_Object((1,3,6,1,4,1,9839,2,1,3,14),_Set_gradino1_Type())
set_gradino1.setMaxAccess(_D)
if mibBuilder.loadTexts:set_gradino1.setStatus(_A)
if mibBuilder.loadTexts:set_gradino1.setUnits(_C)
class _Offset_grad1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Offset_grad1_Type.__name__=_B
_Offset_grad1_Object=MibScalar
offset_grad1=_Offset_grad1_Object((1,3,6,1,4,1,9839,2,1,3,15),_Offset_grad1_Type())
offset_grad1.setMaxAccess(_D)
if mibBuilder.loadTexts:offset_grad1.setStatus(_A)
if mibBuilder.loadTexts:offset_grad1.setUnits(_C)
class _Diff_gradino1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Diff_gradino1_Type.__name__=_B
_Diff_gradino1_Object=MibScalar
diff_gradino1=_Diff_gradino1_Object((1,3,6,1,4,1,9839,2,1,3,16),_Diff_gradino1_Type())
diff_gradino1.setMaxAccess(_D)
if mibBuilder.loadTexts:diff_gradino1.setStatus(_A)
if mibBuilder.loadTexts:diff_gradino1.setUnits(_C)
class _Set_gradino2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Set_gradino2_Type.__name__=_B
_Set_gradino2_Object=MibScalar
set_gradino2=_Set_gradino2_Object((1,3,6,1,4,1,9839,2,1,3,17),_Set_gradino2_Type())
set_gradino2.setMaxAccess(_D)
if mibBuilder.loadTexts:set_gradino2.setStatus(_A)
if mibBuilder.loadTexts:set_gradino2.setUnits(_C)
class _Offset_grad2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Offset_grad2_Type.__name__=_B
_Offset_grad2_Object=MibScalar
offset_grad2=_Offset_grad2_Object((1,3,6,1,4,1,9839,2,1,3,18),_Offset_grad2_Type())
offset_grad2.setMaxAccess(_D)
if mibBuilder.loadTexts:offset_grad2.setStatus(_A)
if mibBuilder.loadTexts:offset_grad2.setUnits(_C)
class _Diff_gradino2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Diff_gradino2_Type.__name__=_B
_Diff_gradino2_Object=MibScalar
diff_gradino2=_Diff_gradino2_Object((1,3,6,1,4,1,9839,2,1,3,19),_Diff_gradino2_Type())
diff_gradino2.setMaxAccess(_D)
if mibBuilder.loadTexts:diff_gradino2.setStatus(_A)
if mibBuilder.loadTexts:diff_gradino2.setUnits(_C)
class _Set_gradino3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Set_gradino3_Type.__name__=_B
_Set_gradino3_Object=MibScalar
set_gradino3=_Set_gradino3_Object((1,3,6,1,4,1,9839,2,1,3,20),_Set_gradino3_Type())
set_gradino3.setMaxAccess(_D)
if mibBuilder.loadTexts:set_gradino3.setStatus(_A)
if mibBuilder.loadTexts:set_gradino3.setUnits(_C)
class _Offset_grad3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Offset_grad3_Type.__name__=_B
_Offset_grad3_Object=MibScalar
offset_grad3=_Offset_grad3_Object((1,3,6,1,4,1,9839,2,1,3,21),_Offset_grad3_Type())
offset_grad3.setMaxAccess(_D)
if mibBuilder.loadTexts:offset_grad3.setStatus(_A)
if mibBuilder.loadTexts:offset_grad3.setUnits(_C)
class _Diff_gradino3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Diff_gradino3_Type.__name__=_B
_Diff_gradino3_Object=MibScalar
diff_gradino3=_Diff_gradino3_Object((1,3,6,1,4,1,9839,2,1,3,22),_Diff_gradino3_Type())
diff_gradino3.setMaxAccess(_D)
if mibBuilder.loadTexts:diff_gradino3.setStatus(_A)
if mibBuilder.loadTexts:diff_gradino3.setUnits(_C)
class _Set_gradino4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Set_gradino4_Type.__name__=_B
_Set_gradino4_Object=MibScalar
set_gradino4=_Set_gradino4_Object((1,3,6,1,4,1,9839,2,1,3,23),_Set_gradino4_Type())
set_gradino4.setMaxAccess(_D)
if mibBuilder.loadTexts:set_gradino4.setStatus(_A)
if mibBuilder.loadTexts:set_gradino4.setUnits(_C)
class _Offset_grad4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Offset_grad4_Type.__name__=_B
_Offset_grad4_Object=MibScalar
offset_grad4=_Offset_grad4_Object((1,3,6,1,4,1,9839,2,1,3,24),_Offset_grad4_Type())
offset_grad4.setMaxAccess(_D)
if mibBuilder.loadTexts:offset_grad4.setStatus(_A)
if mibBuilder.loadTexts:offset_grad4.setUnits(_C)
class _Diff_gradino4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Diff_gradino4_Type.__name__=_B
_Diff_gradino4_Object=MibScalar
diff_gradino4=_Diff_gradino4_Object((1,3,6,1,4,1,9839,2,1,3,25),_Diff_gradino4_Type())
diff_gradino4.setMaxAccess(_D)
if mibBuilder.loadTexts:diff_gradino4.setStatus(_A)
if mibBuilder.loadTexts:diff_gradino4.setUnits(_C)
class _Tast_telecom_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Tast_telecom_Type.__name__=_B
_Tast_telecom_Object=MibScalar
tast_telecom=_Tast_telecom_Object((1,3,6,1,4,1,9839,2,1,3,26),_Tast_telecom_Type())
tast_telecom.setMaxAccess(_D)
if mibBuilder.loadTexts:tast_telecom.setStatus(_A)
if mibBuilder.loadTexts:tast_telecom.setUnits(_C)
class _Codice_telecom_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Codice_telecom_Type.__name__=_B
_Codice_telecom_Object=MibScalar
codice_telecom=_Codice_telecom_Object((1,3,6,1,4,1,9839,2,1,3,27),_Codice_telecom_Type())
codice_telecom.setMaxAccess(_D)
if mibBuilder.loadTexts:codice_telecom.setStatus(_A)
if mibBuilder.loadTexts:codice_telecom.setUnits(_C)
mibBuilder.exportSymbols('CAREL-ir32un_t-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'ir32un_tMIB':ir32un_tMIB,'digitalObjects':digitalObjects,'stato_id_1':stato_id_1,'stato_id_2':stato_id_2,'stato_ud_1':stato_ud_1,'stato_ud_2':stato_ud_2,'stato_ud_3':stato_ud_3,'stato_ud_4':stato_ud_4,'all_sonda_0':all_sonda_0,'all_sonda_1':all_sonda_1,'all_eeprom':all_eeprom,'all_id_1':all_id_1,'all_alta_temp':all_alta_temp,'all_bassa_temp':all_bassa_temp,'prop_prop_int':prop_prop_int,'tipo_sonda':tipo_sonda,'celsius_farhan':celsius_farhan,'modo_speciale':modo_speciale,'tipo_out_grad4':tipo_out_grad4,'tipo_out_grad3':tipo_out_grad3,'tipo_out_grad2':tipo_out_grad2,'tipo_out_grad1':tipo_out_grad1,'analogObjects':analogObjects,'ing_sonda_0':ing_sonda_0,'ing_sonda_1':ing_sonda_1,'set_point1':set_point1,'set_point2':set_point2,'differenziale1':differenziale1,'differenziale2':differenziale2,'zona_morta':zona_morta,'offset_sonda':offset_sonda,'sog_bassa_temp':sog_bassa_temp,'sog_alta_temp':sog_alta_temp,'differenz_all':differenz_all,'tempo_di_pwm':tempo_di_pwm,'val_minimo_av':val_minimo_av,'val_massimo_av':val_massimo_av,'set1_min_ok':set1_min_ok,'set1_max_ok':set1_max_ok,'set2_min_ok':set2_min_ok,'set2_max_ok':set2_max_ok,'autorita':autorita,'integerObjects':integerObjects,'modo_funz_c0':modo_funz_c0,'rit_2ins_c6':rit_2ins_c6,'tmin_2out_c7':tmin_2out_c7,'tmin_off_out_c8':tmin_off_out_c8,'tmin_on_c9':tmin_on_c9,'sicur_sonde':sicur_sonde,'rotazione':rotazione,'velocita_sonda':velocita_sonda,'presenza_sonda':presenza_sonda,'tempo_allarme':tempo_allarme,'gestione_id1':gestione_id1,'gestione_id2':gestione_id2,'sicur_all_id':sicur_all_id,'set_gradino1':set_gradino1,'offset_grad1':offset_grad1,'diff_gradino1':diff_gradino1,'set_gradino2':set_gradino2,'offset_grad2':offset_grad2,'diff_gradino2':diff_gradino2,'set_gradino3':set_gradino3,'offset_grad3':offset_grad3,'diff_gradino3':diff_gradino3,'set_gradino4':set_gradino4,'offset_grad4':offset_grad4,'diff_gradino4':diff_gradino4,'tast_telecom':tast_telecom,'codice_telecom':codice_telecom})