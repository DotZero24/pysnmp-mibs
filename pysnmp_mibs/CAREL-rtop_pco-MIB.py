_H='% x10'
_G='sec'
_F='C x10'
_E='read-only'
_D='N/A'
_C='read-write'
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
rtop_pcoMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_D)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_D)
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
netSize.setMaxAccess(_C)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_D)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_D)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_D)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_D)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_D)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_D)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_D)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_D)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_D)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_D)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_D)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Start_stop_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Start_stop_Type.__name__=_B
_Start_stop_Object=MibScalar
start_stop=_Start_stop_Object((1,3,6,1,4,1,9839,2,1,1,8),_Start_stop_Type())
start_stop.setMaxAccess(_C)
if mibBuilder.loadTexts:start_stop.setStatus(_A)
if mibBuilder.loadTexts:start_stop.setUnits(_D)
class _Ventilatore_p_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ventilatore_p_Type.__name__=_B
_Ventilatore_p_Object=MibScalar
ventilatore_p=_Ventilatore_p_Object((1,3,6,1,4,1,9839,2,1,1,15),_Ventilatore_p_Type())
ventilatore_p.setMaxAccess(_E)
if mibBuilder.loadTexts:ventilatore_p.setStatus(_A)
if mibBuilder.loadTexts:ventilatore_p.setUnits(_D)
class _Cont_avv_a1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cont_avv_a1_Type.__name__=_B
_Cont_avv_a1_Object=MibScalar
cont_avv_a1=_Cont_avv_a1_Object((1,3,6,1,4,1,9839,2,1,1,16),_Cont_avv_a1_Type())
cont_avv_a1.setMaxAccess(_E)
if mibBuilder.loadTexts:cont_avv_a1.setStatus(_A)
if mibBuilder.loadTexts:cont_avv_a1.setUnits(_D)
class _Cont_avv_a2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cont_avv_a2_Type.__name__=_B
_Cont_avv_a2_Object=MibScalar
cont_avv_a2=_Cont_avv_a2_Object((1,3,6,1,4,1,9839,2,1,1,17),_Cont_avv_a2_Type())
cont_avv_a2.setMaxAccess(_E)
if mibBuilder.loadTexts:cont_avv_a2.setStatus(_A)
if mibBuilder.loadTexts:cont_avv_a2.setUnits(_D)
class _Resistenza1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Resistenza1_Type.__name__=_B
_Resistenza1_Object=MibScalar
resistenza1=_Resistenza1_Object((1,3,6,1,4,1,9839,2,1,1,20),_Resistenza1_Type())
resistenza1.setMaxAccess(_E)
if mibBuilder.loadTexts:resistenza1.setStatus(_A)
if mibBuilder.loadTexts:resistenza1.setUnits(_D)
class _Resistenza2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Resistenza2_Type.__name__=_B
_Resistenza2_Object=MibScalar
resistenza2=_Resistenza2_Object((1,3,6,1,4,1,9839,2,1,1,21),_Resistenza2_Type())
resistenza2.setMaxAccess(_E)
if mibBuilder.loadTexts:resistenza2.setStatus(_A)
if mibBuilder.loadTexts:resistenza2.setUnits(_D)
class _Umidifica_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Umidifica_Type.__name__=_B
_Umidifica_Object=MibScalar
umidifica=_Umidifica_Object((1,3,6,1,4,1,9839,2,1,1,22),_Umidifica_Type())
umidifica.setMaxAccess(_E)
if mibBuilder.loadTexts:umidifica.setStatus(_A)
if mibBuilder.loadTexts:umidifica.setUnits(_D)
class _Ventilatore1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ventilatore1_Type.__name__=_B
_Ventilatore1_Object=MibScalar
ventilatore1=_Ventilatore1_Object((1,3,6,1,4,1,9839,2,1,1,23),_Ventilatore1_Type())
ventilatore1.setMaxAccess(_E)
if mibBuilder.loadTexts:ventilatore1.setStatus(_A)
if mibBuilder.loadTexts:ventilatore1.setUnits(_D)
class _Ventilatore2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ventilatore2_Type.__name__=_B
_Ventilatore2_Object=MibScalar
ventilatore2=_Ventilatore2_Object((1,3,6,1,4,1,9839,2,1,1,24),_Ventilatore2_Type())
ventilatore2.setMaxAccess(_E)
if mibBuilder.loadTexts:ventilatore2.setStatus(_A)
if mibBuilder.loadTexts:ventilatore2.setUnits(_D)
class _Glb_al_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Glb_al_Type.__name__=_B
_Glb_al_Object=MibScalar
glb_al=_Glb_al_Object((1,3,6,1,4,1,9839,2,1,1,26),_Glb_al_Type())
glb_al.setMaxAccess(_E)
if mibBuilder.loadTexts:glb_al.setStatus(_A)
if mibBuilder.loadTexts:glb_al.setUnits(_D)
class _Mask_term1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_term1_Type.__name__=_B
_Mask_term1_Object=MibScalar
mask_term1=_Mask_term1_Object((1,3,6,1,4,1,9839,2,1,1,27),_Mask_term1_Type())
mask_term1.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_term1.setStatus(_A)
if mibBuilder.loadTexts:mask_term1.setUnits(_D)
class _Mask_term2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_term2_Type.__name__=_B
_Mask_term2_Object=MibScalar
mask_term2=_Mask_term2_Object((1,3,6,1,4,1,9839,2,1,1,28),_Mask_term2_Type())
mask_term2.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_term2.setStatus(_A)
if mibBuilder.loadTexts:mask_term2.setUnits(_D)
class _Mask_press_h1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_press_h1_Type.__name__=_B
_Mask_press_h1_Object=MibScalar
mask_press_h1=_Mask_press_h1_Object((1,3,6,1,4,1,9839,2,1,1,29),_Mask_press_h1_Type())
mask_press_h1.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_press_h1.setStatus(_A)
if mibBuilder.loadTexts:mask_press_h1.setUnits(_D)
class _Mask_press_h2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_press_h2_Type.__name__=_B
_Mask_press_h2_Object=MibScalar
mask_press_h2=_Mask_press_h2_Object((1,3,6,1,4,1,9839,2,1,1,30),_Mask_press_h2_Type())
mask_press_h2.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_press_h2.setStatus(_A)
if mibBuilder.loadTexts:mask_press_h2.setUnits(_D)
class _Mask_antigelo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_antigelo_Type.__name__=_B
_Mask_antigelo_Object=MibScalar
mask_antigelo=_Mask_antigelo_Object((1,3,6,1,4,1,9839,2,1,1,31),_Mask_antigelo_Type())
mask_antigelo.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_antigelo.setStatus(_A)
if mibBuilder.loadTexts:mask_antigelo.setUnits(_D)
class _Mask_q14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_q14_Type.__name__=_B
_Mask_q14_Object=MibScalar
mask_q14=_Mask_q14_Object((1,3,6,1,4,1,9839,2,1,1,32),_Mask_q14_Type())
mask_q14.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_q14.setStatus(_A)
if mibBuilder.loadTexts:mask_q14.setUnits(_D)
class _Mask_q15_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_q15_Type.__name__=_B
_Mask_q15_Object=MibScalar
mask_q15=_Mask_q15_Object((1,3,6,1,4,1,9839,2,1,1,33),_Mask_q15_Type())
mask_q15.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_q15.setStatus(_A)
if mibBuilder.loadTexts:mask_q15.setUnits(_D)
class _Mask_q3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_q3_Type.__name__=_B
_Mask_q3_Object=MibScalar
mask_q3=_Mask_q3_Object((1,3,6,1,4,1,9839,2,1,1,34),_Mask_q3_Type())
mask_q3.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_q3.setStatus(_A)
if mibBuilder.loadTexts:mask_q3.setUnits(_D)
class _Mask_q4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_q4_Type.__name__=_B
_Mask_q4_Object=MibScalar
mask_q4=_Mask_q4_Object((1,3,6,1,4,1,9839,2,1,1,35),_Mask_q4_Type())
mask_q4.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_q4.setStatus(_A)
if mibBuilder.loadTexts:mask_q4.setUnits(_D)
class _Mask_q5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_q5_Type.__name__=_B
_Mask_q5_Object=MibScalar
mask_q5=_Mask_q5_Object((1,3,6,1,4,1,9839,2,1,1,36),_Mask_q5_Type())
mask_q5.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_q5.setStatus(_A)
if mibBuilder.loadTexts:mask_q5.setUnits(_D)
class _Mask_q6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_q6_Type.__name__=_B
_Mask_q6_Object=MibScalar
mask_q6=_Mask_q6_Object((1,3,6,1,4,1,9839,2,1,1,37),_Mask_q6_Type())
mask_q6.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_q6.setStatus(_A)
if mibBuilder.loadTexts:mask_q6.setUnits(_D)
class _Bassa_press1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bassa_press1_Type.__name__=_B
_Bassa_press1_Object=MibScalar
bassa_press1=_Bassa_press1_Object((1,3,6,1,4,1,9839,2,1,1,38),_Bassa_press1_Type())
bassa_press1.setMaxAccess(_E)
if mibBuilder.loadTexts:bassa_press1.setStatus(_A)
if mibBuilder.loadTexts:bassa_press1.setUnits(_D)
class _Bassa_press2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bassa_press2_Type.__name__=_B
_Bassa_press2_Object=MibScalar
bassa_press2=_Bassa_press2_Object((1,3,6,1,4,1,9839,2,1,1,39),_Bassa_press2_Type())
bassa_press2.setMaxAccess(_E)
if mibBuilder.loadTexts:bassa_press2.setStatus(_A)
if mibBuilder.loadTexts:bassa_press2.setUnits(_D)
class _Mask_interbl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_interbl_Type.__name__=_B
_Mask_interbl_Object=MibScalar
mask_interbl=_Mask_interbl_Object((1,3,6,1,4,1,9839,2,1,1,40),_Mask_interbl_Type())
mask_interbl.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_interbl.setStatus(_A)
if mibBuilder.loadTexts:mask_interbl.setUnits(_D)
class _Mask_defrost1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_defrost1_Type.__name__=_B
_Mask_defrost1_Object=MibScalar
mask_defrost1=_Mask_defrost1_Object((1,3,6,1,4,1,9839,2,1,1,41),_Mask_defrost1_Type())
mask_defrost1.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_defrost1.setStatus(_A)
if mibBuilder.loadTexts:mask_defrost1.setUnits(_D)
class _Mask_defrost2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_defrost2_Type.__name__=_B
_Mask_defrost2_Object=MibScalar
mask_defrost2=_Mask_defrost2_Object((1,3,6,1,4,1,9839,2,1,1,42),_Mask_defrost2_Type())
mask_defrost2.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_defrost2.setStatus(_A)
if mibBuilder.loadTexts:mask_defrost2.setUnits(_D)
class _Mask_filtro_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_filtro_Type.__name__=_B
_Mask_filtro_Object=MibScalar
mask_filtro=_Mask_filtro_Object((1,3,6,1,4,1,9839,2,1,1,43),_Mask_filtro_Type())
mask_filtro.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_filtro.setStatus(_A)
if mibBuilder.loadTexts:mask_filtro.setUnits(_D)
class _Mask_term_res_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mask_term_res_Type.__name__=_B
_Mask_term_res_Object=MibScalar
mask_term_res=_Mask_term_res_Object((1,3,6,1,4,1,9839,2,1,1,44),_Mask_term_res_Type())
mask_term_res.setMaxAccess(_E)
if mibBuilder.loadTexts:mask_term_res.setStatus(_A)
if mibBuilder.loadTexts:mask_term_res.setUnits(_D)
class _En_pompacalore_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_pompacalore_Type.__name__=_B
_En_pompacalore_Object=MibScalar
en_pompacalore=_En_pompacalore_Object((1,3,6,1,4,1,9839,2,1,1,45),_En_pompacalore_Type())
en_pompacalore.setMaxAccess(_C)
if mibBuilder.loadTexts:en_pompacalore.setStatus(_A)
if mibBuilder.loadTexts:en_pompacalore.setUnits(_D)
class _En_orologio_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_orologio_Type.__name__=_B
_En_orologio_Object=MibScalar
en_orologio=_En_orologio_Object((1,3,6,1,4,1,9839,2,1,1,46),_En_orologio_Type())
en_orologio.setMaxAccess(_C)
if mibBuilder.loadTexts:en_orologio.setStatus(_A)
if mibBuilder.loadTexts:en_orologio.setUnits(_D)
class _En_umidita_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_umidita_Type.__name__=_B
_En_umidita_Object=MibScalar
en_umidita=_En_umidita_Object((1,3,6,1,4,1,9839,2,1,1,47),_En_umidita_Type())
en_umidita.setMaxAccess(_C)
if mibBuilder.loadTexts:en_umidita.setStatus(_A)
if mibBuilder.loadTexts:en_umidita.setUnits(_D)
class _En_mandata_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_mandata_Type.__name__=_B
_En_mandata_Object=MibScalar
en_mandata=_En_mandata_Object((1,3,6,1,4,1,9839,2,1,1,48),_En_mandata_Type())
en_mandata.setMaxAccess(_C)
if mibBuilder.loadTexts:en_mandata.setStatus(_A)
if mibBuilder.loadTexts:en_mandata.setUnits(_D)
class _En_supervisore_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_supervisore_Type.__name__=_B
_En_supervisore_Object=MibScalar
en_supervisore=_En_supervisore_Object((1,3,6,1,4,1,9839,2,1,1,50),_En_supervisore_Type())
en_supervisore.setMaxAccess(_C)
if mibBuilder.loadTexts:en_supervisore.setStatus(_A)
if mibBuilder.loadTexts:en_supervisore.setUnits(_D)
class _En_stampante_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_stampante_Type.__name__=_B
_En_stampante_Object=MibScalar
en_stampante=_En_stampante_Object((1,3,6,1,4,1,9839,2,1,1,51),_En_stampante_Type())
en_stampante.setMaxAccess(_C)
if mibBuilder.loadTexts:en_stampante.setStatus(_A)
if mibBuilder.loadTexts:en_stampante.setUnits(_D)
class _En_freecool_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_freecool_Type.__name__=_B
_En_freecool_Object=MibScalar
en_freecool=_En_freecool_Object((1,3,6,1,4,1,9839,2,1,1,52),_En_freecool_Type())
en_freecool.setMaxAccess(_C)
if mibBuilder.loadTexts:en_freecool.setStatus(_A)
if mibBuilder.loadTexts:en_freecool.setUnits(_D)
class _En_freeheat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_freeheat_Type.__name__=_B
_En_freeheat_Object=MibScalar
en_freeheat=_En_freeheat_Object((1,3,6,1,4,1,9839,2,1,1,53),_En_freeheat_Type())
en_freeheat.setMaxAccess(_C)
if mibBuilder.loadTexts:en_freeheat.setStatus(_A)
if mibBuilder.loadTexts:en_freeheat.setUnits(_D)
class _En_compensazio_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_compensazio_Type.__name__=_B
_En_compensazio_Object=MibScalar
en_compensazio=_En_compensazio_Object((1,3,6,1,4,1,9839,2,1,1,55),_En_compensazio_Type())
en_compensazio.setMaxAccess(_C)
if mibBuilder.loadTexts:en_compensazio.setStatus(_A)
if mibBuilder.loadTexts:en_compensazio.setUnits(_D)
class _Off_ventp_defr_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Off_ventp_defr_Type.__name__=_B
_Off_ventp_defr_Object=MibScalar
off_ventp_defr=_Off_ventp_defr_Object((1,3,6,1,4,1,9839,2,1,1,56),_Off_ventp_defr_Type())
off_ventp_defr.setMaxAccess(_C)
if mibBuilder.loadTexts:off_ventp_defr.setStatus(_A)
if mibBuilder.loadTexts:off_ventp_defr.setUnits(_D)
class _En_sbrin_cont_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sbrin_cont_Type.__name__=_B
_En_sbrin_cont_Object=MibScalar
en_sbrin_cont=_En_sbrin_cont_Object((1,3,6,1,4,1,9839,2,1,1,57),_En_sbrin_cont_Type())
en_sbrin_cont.setMaxAccess(_C)
if mibBuilder.loadTexts:en_sbrin_cont.setStatus(_A)
if mibBuilder.loadTexts:en_sbrin_cont.setUnits(_D)
class _Autostart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Autostart_Type.__name__=_B
_Autostart_Object=MibScalar
autostart=_Autostart_Object((1,3,6,1,4,1,9839,2,1,1,58),_Autostart_Type())
autostart.setMaxAccess(_C)
if mibBuilder.loadTexts:autostart.setStatus(_A)
if mibBuilder.loadTexts:autostart.setUnits(_D)
class _En_remoto_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_remoto_Type.__name__=_B
_En_remoto_Object=MibScalar
en_remoto=_En_remoto_Object((1,3,6,1,4,1,9839,2,1,1,59),_En_remoto_Type())
en_remoto.setMaxAccess(_C)
if mibBuilder.loadTexts:en_remoto.setStatus(_A)
if mibBuilder.loadTexts:en_remoto.setUnits(_D)
class _Abil_rotaz_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Abil_rotaz_Type.__name__=_B
_Abil_rotaz_Object=MibScalar
abil_rotaz=_Abil_rotaz_Object((1,3,6,1,4,1,9839,2,1,1,64),_Abil_rotaz_Type())
abil_rotaz.setMaxAccess(_C)
if mibBuilder.loadTexts:abil_rotaz.setStatus(_A)
if mibBuilder.loadTexts:abil_rotaz.setUnits(_D)
class _Sys_on_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sys_on_Type.__name__=_B
_Sys_on_Object=MibScalar
sys_on=_Sys_on_Object((1,3,6,1,4,1,9839,2,1,1,65),_Sys_on_Type())
sys_on.setMaxAccess(_C)
if mibBuilder.loadTexts:sys_on.setStatus(_A)
if mibBuilder.loadTexts:sys_on.setUnits(_D)
class _Syson1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Syson1_Type.__name__=_B
_Syson1_Object=MibScalar
syson1=_Syson1_Object((1,3,6,1,4,1,9839,2,1,1,74),_Syson1_Type())
syson1.setMaxAccess(_C)
if mibBuilder.loadTexts:syson1.setStatus(_A)
if mibBuilder.loadTexts:syson1.setUnits(_D)
class _En_binati_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_binati_Type.__name__=_B
_En_binati_Object=MibScalar
en_binati=_En_binati_Object((1,3,6,1,4,1,9839,2,1,1,75),_En_binati_Type())
en_binati.setMaxAccess(_C)
if mibBuilder.loadTexts:en_binati.setStatus(_A)
if mibBuilder.loadTexts:en_binati.setUnits(_D)
class _En_sond_text_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sond_text_Type.__name__=_B
_En_sond_text_Object=MibScalar
en_sond_text=_En_sond_text_Object((1,3,6,1,4,1,9839,2,1,1,76),_En_sond_text_Type())
en_sond_text.setMaxAccess(_C)
if mibBuilder.loadTexts:en_sond_text.setStatus(_A)
if mibBuilder.loadTexts:en_sond_text.setUnits(_D)
class _En_sond_uext_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sond_uext_Type.__name__=_B
_En_sond_uext_Object=MibScalar
en_sond_uext=_En_sond_uext_Object((1,3,6,1,4,1,9839,2,1,1,77),_En_sond_uext_Type())
en_sond_uext.setMaxAccess(_C)
if mibBuilder.loadTexts:en_sond_uext.setStatus(_A)
if mibBuilder.loadTexts:en_sond_uext.setUnits(_D)
class _En_sond_def1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sond_def1_Type.__name__=_B
_En_sond_def1_Object=MibScalar
en_sond_def1=_En_sond_def1_Object((1,3,6,1,4,1,9839,2,1,1,78),_En_sond_def1_Type())
en_sond_def1.setMaxAccess(_C)
if mibBuilder.loadTexts:en_sond_def1.setStatus(_A)
if mibBuilder.loadTexts:en_sond_def1.setUnits(_D)
class _En_sond_def2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sond_def2_Type.__name__=_B
_En_sond_def2_Object=MibScalar
en_sond_def2=_En_sond_def2_Object((1,3,6,1,4,1,9839,2,1,1,79),_En_sond_def2_Type())
en_sond_def2.setMaxAccess(_C)
if mibBuilder.loadTexts:en_sond_def2.setStatus(_A)
if mibBuilder.loadTexts:en_sond_def2.setUnits(_D)
class _Tipo_cont_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tipo_cont_Type.__name__=_B
_Tipo_cont_Object=MibScalar
tipo_cont=_Tipo_cont_Object((1,3,6,1,4,1,9839,2,1,1,86),_Tipo_cont_Type())
tipo_cont.setMaxAccess(_C)
if mibBuilder.loadTexts:tipo_cont.setStatus(_A)
if mibBuilder.loadTexts:tipo_cont.setUnits(_D)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Temp_aria_amb_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999990))
_Temp_aria_amb_Type.__name__=_B
_Temp_aria_amb_Object=MibScalar
temp_aria_amb=_Temp_aria_amb_Object((1,3,6,1,4,1,9839,2,1,2,1),_Temp_aria_amb_Type())
temp_aria_amb.setMaxAccess(_E)
if mibBuilder.loadTexts:temp_aria_amb.setStatus(_A)
if mibBuilder.loadTexts:temp_aria_amb.setUnits(_F)
class _Temp_aria_est_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Temp_aria_est_Type.__name__=_B
_Temp_aria_est_Object=MibScalar
temp_aria_est=_Temp_aria_est_Object((1,3,6,1,4,1,9839,2,1,2,2),_Temp_aria_est_Type())
temp_aria_est.setMaxAccess(_E)
if mibBuilder.loadTexts:temp_aria_est.setStatus(_A)
if mibBuilder.loadTexts:temp_aria_est.setUnits(_F)
class _Umid_ambiente_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Umid_ambiente_Type.__name__=_B
_Umid_ambiente_Object=MibScalar
umid_ambiente=_Umid_ambiente_Object((1,3,6,1,4,1,9839,2,1,2,5),_Umid_ambiente_Type())
umid_ambiente.setMaxAccess(_E)
if mibBuilder.loadTexts:umid_ambiente.setStatus(_A)
if mibBuilder.loadTexts:umid_ambiente.setUnits(_F)
class _Umid_esterna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,130))
_Umid_esterna_Type.__name__=_B
_Umid_esterna_Object=MibScalar
umid_esterna=_Umid_esterna_Object((1,3,6,1,4,1,9839,2,1,2,6),_Umid_esterna_Type())
umid_esterna.setMaxAccess(_E)
if mibBuilder.loadTexts:umid_esterna.setStatus(_A)
if mibBuilder.loadTexts:umid_esterna.setUnits(_F)
class _Set_temp_ariae_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_temp_ariae_Type.__name__=_B
_Set_temp_ariae_Object=MibScalar
set_temp_ariae=_Set_temp_ariae_Object((1,3,6,1,4,1,9839,2,1,2,15),_Set_temp_ariae_Type())
set_temp_ariae.setMaxAccess(_C)
if mibBuilder.loadTexts:set_temp_ariae.setStatus(_A)
if mibBuilder.loadTexts:set_temp_ariae.setUnits(_D)
class _Set_temp_ariai_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_temp_ariai_Type.__name__=_B
_Set_temp_ariai_Object=MibScalar
set_temp_ariai=_Set_temp_ariai_Object((1,3,6,1,4,1,9839,2,1,2,16),_Set_temp_ariai_Type())
set_temp_ariai.setMaxAccess(_C)
if mibBuilder.loadTexts:set_temp_ariai.setStatus(_A)
if mibBuilder.loadTexts:set_temp_ariai.setUnits(_D)
class _Set_umid_est_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_umid_est_Type.__name__=_B
_Set_umid_est_Object=MibScalar
set_umid_est=_Set_umid_est_Object((1,3,6,1,4,1,9839,2,1,2,17),_Set_umid_est_Type())
set_umid_est.setMaxAccess(_C)
if mibBuilder.loadTexts:set_umid_est.setStatus(_A)
if mibBuilder.loadTexts:set_umid_est.setUnits(_D)
class _Set_umid_inv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_umid_inv_Type.__name__=_B
_Set_umid_inv_Object=MibScalar
set_umid_inv=_Set_umid_inv_Object((1,3,6,1,4,1,9839,2,1,2,18),_Set_umid_inv_Type())
set_umid_inv.setMaxAccess(_C)
if mibBuilder.loadTexts:set_umid_inv.setStatus(_A)
if mibBuilder.loadTexts:set_umid_inv.setUnits(_D)
class _Lim_sup_temp_Type(Integer32):defaultValue=350;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Lim_sup_temp_Type.__name__=_B
_Lim_sup_temp_Object=MibScalar
lim_sup_temp=_Lim_sup_temp_Object((1,3,6,1,4,1,9839,2,1,2,19),_Lim_sup_temp_Type())
lim_sup_temp.setMaxAccess(_C)
if mibBuilder.loadTexts:lim_sup_temp.setStatus(_A)
if mibBuilder.loadTexts:lim_sup_temp.setUnits(_F)
class _Lim_inf_temp_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Lim_inf_temp_Type.__name__=_B
_Lim_inf_temp_Object=MibScalar
lim_inf_temp=_Lim_inf_temp_Object((1,3,6,1,4,1,9839,2,1,2,20),_Lim_inf_temp_Type())
lim_inf_temp.setMaxAccess(_C)
if mibBuilder.loadTexts:lim_inf_temp.setStatus(_A)
if mibBuilder.loadTexts:lim_inf_temp.setUnits(_F)
class _Banda_temp_e_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Banda_temp_e_Type.__name__=_B
_Banda_temp_e_Object=MibScalar
banda_temp_e=_Banda_temp_e_Object((1,3,6,1,4,1,9839,2,1,2,21),_Banda_temp_e_Type())
banda_temp_e.setMaxAccess(_C)
if mibBuilder.loadTexts:banda_temp_e.setStatus(_A)
if mibBuilder.loadTexts:banda_temp_e.setUnits(_F)
class _Banda_temp_i_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Banda_temp_i_Type.__name__=_B
_Banda_temp_i_Object=MibScalar
banda_temp_i=_Banda_temp_i_Object((1,3,6,1,4,1,9839,2,1,2,22),_Banda_temp_i_Type())
banda_temp_i.setMaxAccess(_C)
if mibBuilder.loadTexts:banda_temp_i.setStatus(_A)
if mibBuilder.loadTexts:banda_temp_i.setUnits(_F)
class _Lim_sup_umid_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Lim_sup_umid_Type.__name__=_B
_Lim_sup_umid_Object=MibScalar
lim_sup_umid=_Lim_sup_umid_Object((1,3,6,1,4,1,9839,2,1,2,23),_Lim_sup_umid_Type())
lim_sup_umid.setMaxAccess(_C)
if mibBuilder.loadTexts:lim_sup_umid.setStatus(_A)
if mibBuilder.loadTexts:lim_sup_umid.setUnits(_H)
class _Lim_inf_umid_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Lim_inf_umid_Type.__name__=_B
_Lim_inf_umid_Object=MibScalar
lim_inf_umid=_Lim_inf_umid_Object((1,3,6,1,4,1,9839,2,1,2,24),_Lim_inf_umid_Type())
lim_inf_umid.setMaxAccess(_C)
if mibBuilder.loadTexts:lim_inf_umid.setStatus(_A)
if mibBuilder.loadTexts:lim_inf_umid.setUnits(_H)
class _Diff_umid_e_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_Diff_umid_e_Type.__name__=_B
_Diff_umid_e_Object=MibScalar
diff_umid_e=_Diff_umid_e_Object((1,3,6,1,4,1,9839,2,1,2,25),_Diff_umid_e_Type())
diff_umid_e.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_umid_e.setStatus(_A)
if mibBuilder.loadTexts:diff_umid_e.setUnits(_H)
class _Diff_umid_i_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_Diff_umid_i_Type.__name__=_B
_Diff_umid_i_Object=MibScalar
diff_umid_i=_Diff_umid_i_Object((1,3,6,1,4,1,9839,2,1,2,26),_Diff_umid_i_Type())
diff_umid_i.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_umid_i.setStatus(_A)
if mibBuilder.loadTexts:diff_umid_i.setUnits(_H)
class _Offset_fcool_Type(Integer32):defaultValue=-20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Offset_fcool_Type.__name__=_B
_Offset_fcool_Object=MibScalar
offset_fcool=_Offset_fcool_Object((1,3,6,1,4,1,9839,2,1,2,28),_Offset_fcool_Type())
offset_fcool.setMaxAccess(_C)
if mibBuilder.loadTexts:offset_fcool.setStatus(_A)
if mibBuilder.loadTexts:offset_fcool.setUnits(_F)
class _Diff_fcool_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Diff_fcool_Type.__name__=_B
_Diff_fcool_Object=MibScalar
diff_fcool=_Diff_fcool_Object((1,3,6,1,4,1,9839,2,1,2,29),_Diff_fcool_Type())
diff_fcool.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_fcool.setStatus(_A)
if mibBuilder.loadTexts:diff_fcool.setUnits(_F)
class _Offset_fheat_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Offset_fheat_Type.__name__=_B
_Offset_fheat_Object=MibScalar
offset_fheat=_Offset_fheat_Object((1,3,6,1,4,1,9839,2,1,2,30),_Offset_fheat_Type())
offset_fheat.setMaxAccess(_C)
if mibBuilder.loadTexts:offset_fheat.setStatus(_A)
if mibBuilder.loadTexts:offset_fheat.setUnits(_F)
class _Diff_fheat_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Diff_fheat_Type.__name__=_B
_Diff_fheat_Object=MibScalar
diff_fheat=_Diff_fheat_Object((1,3,6,1,4,1,9839,2,1,2,31),_Diff_fheat_Type())
diff_fheat.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_fheat.setStatus(_A)
if mibBuilder.loadTexts:diff_fheat.setUnits(_F)
class _Set_mandata_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Set_mandata_Type.__name__=_B
_Set_mandata_Object=MibScalar
set_mandata=_Set_mandata_Object((1,3,6,1,4,1,9839,2,1,2,32),_Set_mandata_Type())
set_mandata.setMaxAccess(_C)
if mibBuilder.loadTexts:set_mandata.setStatus(_A)
if mibBuilder.loadTexts:set_mandata.setUnits(_F)
class _Ban_mandata_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Ban_mandata_Type.__name__=_B
_Ban_mandata_Object=MibScalar
ban_mandata=_Ban_mandata_Object((1,3,6,1,4,1,9839,2,1,2,33),_Ban_mandata_Type())
ban_mandata.setMaxAccess(_C)
if mibBuilder.loadTexts:ban_mandata.setStatus(_A)
if mibBuilder.loadTexts:ban_mandata.setUnits(_F)
class _Set_esterno_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Set_esterno_Type.__name__=_B
_Set_esterno_Object=MibScalar
set_esterno=_Set_esterno_Object((1,3,6,1,4,1,9839,2,1,2,34),_Set_esterno_Type())
set_esterno.setMaxAccess(_C)
if mibBuilder.loadTexts:set_esterno.setStatus(_A)
if mibBuilder.loadTexts:set_esterno.setUnits(_F)
class _Diff_esterno_e_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Diff_esterno_e_Type.__name__=_B
_Diff_esterno_e_Object=MibScalar
diff_esterno_e=_Diff_esterno_e_Object((1,3,6,1,4,1,9839,2,1,2,35),_Diff_esterno_e_Type())
diff_esterno_e.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_esterno_e.setStatus(_A)
if mibBuilder.loadTexts:diff_esterno_e.setUnits(_F)
class _Max_comp_e_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9990))
_Max_comp_e_Type.__name__=_B
_Max_comp_e_Object=MibScalar
max_comp_e=_Max_comp_e_Object((1,3,6,1,4,1,9839,2,1,2,36),_Max_comp_e_Type())
max_comp_e.setMaxAccess(_C)
if mibBuilder.loadTexts:max_comp_e.setStatus(_A)
if mibBuilder.loadTexts:max_comp_e.setUnits(_F)
class _Set_min_Type(Integer32):defaultValue=-20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_Set_min_Type.__name__=_B
_Set_min_Object=MibScalar
set_min=_Set_min_Object((1,3,6,1,4,1,9839,2,1,2,37),_Set_min_Type())
set_min.setMaxAccess(_C)
if mibBuilder.loadTexts:set_min.setStatus(_A)
if mibBuilder.loadTexts:set_min.setUnits(_F)
class _Set_stop_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_Set_stop_Type.__name__=_B
_Set_stop_Object=MibScalar
set_stop=_Set_stop_Object((1,3,6,1,4,1,9839,2,1,2,38),_Set_stop_Type())
set_stop.setMaxAccess(_C)
if mibBuilder.loadTexts:set_stop.setStatus(_A)
if mibBuilder.loadTexts:set_stop.setUnits(_F)
class _Zona_morta_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_Zona_morta_Type.__name__=_B
_Zona_morta_Object=MibScalar
zona_morta=_Zona_morta_Object((1,3,6,1,4,1,9839,2,1,2,39),_Zona_morta_Type())
zona_morta.setMaxAccess(_C)
if mibBuilder.loadTexts:zona_morta.setStatus(_A)
if mibBuilder.loadTexts:zona_morta.setUnits(_F)
class _Zona_morta_u_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_Zona_morta_u_Type.__name__=_B
_Zona_morta_u_Object=MibScalar
zona_morta_u=_Zona_morta_u_Object((1,3,6,1,4,1,9839,2,1,2,40),_Zona_morta_u_Type())
zona_morta_u.setMaxAccess(_C)
if mibBuilder.loadTexts:zona_morta_u.setStatus(_A)
if mibBuilder.loadTexts:zona_morta_u.setUnits(_H)
class _Sg_alta_in_e_Type(Integer32):defaultValue=320;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Sg_alta_in_e_Type.__name__=_B
_Sg_alta_in_e_Object=MibScalar
sg_alta_in_e=_Sg_alta_in_e_Object((1,3,6,1,4,1,9839,2,1,2,41),_Sg_alta_in_e_Type())
sg_alta_in_e.setMaxAccess(_C)
if mibBuilder.loadTexts:sg_alta_in_e.setStatus(_A)
if mibBuilder.loadTexts:sg_alta_in_e.setUnits(_F)
class _Sg_bassa_in_e_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Sg_bassa_in_e_Type.__name__=_B
_Sg_bassa_in_e_Object=MibScalar
sg_bassa_in_e=_Sg_bassa_in_e_Object((1,3,6,1,4,1,9839,2,1,2,42),_Sg_bassa_in_e_Type())
sg_bassa_in_e.setMaxAccess(_C)
if mibBuilder.loadTexts:sg_bassa_in_e.setStatus(_A)
if mibBuilder.loadTexts:sg_bassa_in_e.setUnits(_F)
class _Sg_alta_in_i_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Sg_alta_in_i_Type.__name__=_B
_Sg_alta_in_i_Object=MibScalar
sg_alta_in_i=_Sg_alta_in_i_Object((1,3,6,1,4,1,9839,2,1,2,43),_Sg_alta_in_i_Type())
sg_alta_in_i.setMaxAccess(_C)
if mibBuilder.loadTexts:sg_alta_in_i.setStatus(_A)
if mibBuilder.loadTexts:sg_alta_in_i.setUnits(_F)
class _Sg_bassa_in_i_Type(Integer32):defaultValue=170;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Sg_bassa_in_i_Type.__name__=_B
_Sg_bassa_in_i_Object=MibScalar
sg_bassa_in_i=_Sg_bassa_in_i_Object((1,3,6,1,4,1,9839,2,1,2,44),_Sg_bassa_in_i_Type())
sg_bassa_in_i.setMaxAccess(_C)
if mibBuilder.loadTexts:sg_bassa_in_i.setStatus(_A)
if mibBuilder.loadTexts:sg_bassa_in_i.setUnits(_F)
class _Tar_defrost1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,990))
_Tar_defrost1_Type.__name__=_B
_Tar_defrost1_Object=MibScalar
tar_defrost1=_Tar_defrost1_Object((1,3,6,1,4,1,9839,2,1,2,48),_Tar_defrost1_Type())
tar_defrost1.setMaxAccess(_C)
if mibBuilder.loadTexts:tar_defrost1.setStatus(_A)
if mibBuilder.loadTexts:tar_defrost1.setUnits(_F)
class _Tar_defrost2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,990))
_Tar_defrost2_Type.__name__=_B
_Tar_defrost2_Object=MibScalar
tar_defrost2=_Tar_defrost2_Object((1,3,6,1,4,1,9839,2,1,2,49),_Tar_defrost2_Type())
tar_defrost2.setMaxAccess(_C)
if mibBuilder.loadTexts:tar_defrost2.setStatus(_A)
if mibBuilder.loadTexts:tar_defrost2.setUnits(_F)
class _Offset_res_Type(Integer32):defaultValue=-20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Offset_res_Type.__name__=_B
_Offset_res_Object=MibScalar
offset_res=_Offset_res_Object((1,3,6,1,4,1,9839,2,1,2,52),_Offset_res_Type())
offset_res.setMaxAccess(_C)
if mibBuilder.loadTexts:offset_res.setStatus(_A)
if mibBuilder.loadTexts:offset_res.setUnits(_F)
class _Differ_res_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Differ_res_Type.__name__=_B
_Differ_res_Object=MibScalar
differ_res=_Differ_res_Object((1,3,6,1,4,1,9839,2,1,2,53),_Differ_res_Type())
differ_res.setMaxAccess(_C)
if mibBuilder.loadTexts:differ_res.setStatus(_A)
if mibBuilder.loadTexts:differ_res.setUnits(_F)
class _Tar_umid_amb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,130))
_Tar_umid_amb_Type.__name__=_B
_Tar_umid_amb_Object=MibScalar
tar_umid_amb=_Tar_umid_amb_Object((1,3,6,1,4,1,9839,2,1,2,54),_Tar_umid_amb_Type())
tar_umid_amb.setMaxAccess(_C)
if mibBuilder.loadTexts:tar_umid_amb.setStatus(_A)
if mibBuilder.loadTexts:tar_umid_amb.setUnits(_F)
class _Offset_valv_Type(Integer32):defaultValue=-20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Offset_valv_Type.__name__=_B
_Offset_valv_Object=MibScalar
offset_valv=_Offset_valv_Object((1,3,6,1,4,1,9839,2,1,2,62),_Offset_valv_Type())
offset_valv.setMaxAccess(_C)
if mibBuilder.loadTexts:offset_valv.setStatus(_A)
if mibBuilder.loadTexts:offset_valv.setUnits(_F)
class _Diff_valv_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Diff_valv_Type.__name__=_B
_Diff_valv_Object=MibScalar
diff_valv=_Diff_valv_Object((1,3,6,1,4,1,9839,2,1,2,63),_Diff_valv_Type())
diff_valv.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_valv.setStatus(_A)
if mibBuilder.loadTexts:diff_valv.setUnits(_F)
class _Set_esternoi_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-9990,9990))
_Set_esternoi_Type.__name__=_B
_Set_esternoi_Object=MibScalar
set_esternoi=_Set_esternoi_Object((1,3,6,1,4,1,9839,2,1,2,64),_Set_esternoi_Type())
set_esternoi.setMaxAccess(_C)
if mibBuilder.loadTexts:set_esternoi.setStatus(_A)
if mibBuilder.loadTexts:set_esternoi.setUnits(_F)
class _Max_comp_i_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9990))
_Max_comp_i_Type.__name__=_B
_Max_comp_i_Object=MibScalar
max_comp_i=_Max_comp_i_Object((1,3,6,1,4,1,9839,2,1,2,66),_Max_comp_i_Type())
max_comp_i.setMaxAccess(_C)
if mibBuilder.loadTexts:max_comp_i.setStatus(_A)
if mibBuilder.loadTexts:max_comp_i.setUnits(_F)
class _Set_vent1_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9990))
_Set_vent1_Type.__name__=_B
_Set_vent1_Object=MibScalar
set_vent1=_Set_vent1_Object((1,3,6,1,4,1,9839,2,1,2,67),_Set_vent1_Type())
set_vent1.setMaxAccess(_C)
if mibBuilder.loadTexts:set_vent1.setStatus(_A)
if mibBuilder.loadTexts:set_vent1.setUnits(_F)
class _Set_vent2_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9990))
_Set_vent2_Type.__name__=_B
_Set_vent2_Object=MibScalar
set_vent2=_Set_vent2_Object((1,3,6,1,4,1,9839,2,1,2,68),_Set_vent2_Type())
set_vent2.setMaxAccess(_C)
if mibBuilder.loadTexts:set_vent2.setStatus(_A)
if mibBuilder.loadTexts:set_vent2.setUnits(_F)
class _Diff_vent1_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9990))
_Diff_vent1_Type.__name__=_B
_Diff_vent1_Object=MibScalar
diff_vent1=_Diff_vent1_Object((1,3,6,1,4,1,9839,2,1,2,69),_Diff_vent1_Type())
diff_vent1.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_vent1.setStatus(_A)
if mibBuilder.loadTexts:diff_vent1.setUnits(_F)
class _Diff_vent2_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9990))
_Diff_vent2_Type.__name__=_B
_Diff_vent2_Object=MibScalar
diff_vent2=_Diff_vent2_Object((1,3,6,1,4,1,9839,2,1,2,70),_Diff_vent2_Type())
diff_vent2.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_vent2.setStatus(_A)
if mibBuilder.loadTexts:diff_vent2.setUnits(_F)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Ore_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Ore_comp1_Type.__name__=_B
_Ore_comp1_Object=MibScalar
ore_comp1=_Ore_comp1_Object((1,3,6,1,4,1,9839,2,1,3,10),_Ore_comp1_Type())
ore_comp1.setMaxAccess(_C)
if mibBuilder.loadTexts:ore_comp1.setStatus(_A)
if mibBuilder.loadTexts:ore_comp1.setUnits(_D)
class _Ore_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Ore_comp2_Type.__name__=_B
_Ore_comp2_Object=MibScalar
ore_comp2=_Ore_comp2_Object((1,3,6,1,4,1,9839,2,1,3,11),_Ore_comp2_Type())
ore_comp2.setMaxAccess(_C)
if mibBuilder.loadTexts:ore_comp2.setStatus(_A)
if mibBuilder.loadTexts:ore_comp2.setUnits(_D)
class _Rit_all_ht_in_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Rit_all_ht_in_Type.__name__=_B
_Rit_all_ht_in_Object=MibScalar
rit_all_ht_in=_Rit_all_ht_in_Object((1,3,6,1,4,1,9839,2,1,3,19),_Rit_all_ht_in_Type())
rit_all_ht_in.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_all_ht_in.setStatus(_A)
if mibBuilder.loadTexts:rit_all_ht_in.setUnits(_G)
class _Rit_all_press_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Rit_all_press_Type.__name__=_B
_Rit_all_press_Object=MibScalar
rit_all_press=_Rit_all_press_Object((1,3,6,1,4,1,9839,2,1,3,20),_Rit_all_press_Type())
rit_all_press.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_all_press.setStatus(_A)
if mibBuilder.loadTexts:rit_all_press.setUnits(_G)
class _N_comp_deum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_N_comp_deum_Type.__name__=_B
_N_comp_deum_Object=MibScalar
n_comp_deum=_N_comp_deum_Object((1,3,6,1,4,1,9839,2,1,3,23),_N_comp_deum_Type())
n_comp_deum.setMaxAccess(_C)
if mibBuilder.loadTexts:n_comp_deum.setStatus(_A)
if mibBuilder.loadTexts:n_comp_deum.setUnits(_D)
class _Rit_stop_ventp_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Rit_stop_ventp_Type.__name__=_B
_Rit_stop_ventp_Object=MibScalar
rit_stop_ventp=_Rit_stop_ventp_Object((1,3,6,1,4,1,9839,2,1,3,24),_Rit_stop_ventp_Type())
rit_stop_ventp.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_stop_ventp.setStatus(_A)
if mibBuilder.loadTexts:rit_stop_ventp.setUnits(_G)
class _Rit_part_comp_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Rit_part_comp_Type.__name__=_B
_Rit_part_comp_Object=MibScalar
rit_part_comp=_Rit_part_comp_Object((1,3,6,1,4,1,9839,2,1,3,25),_Rit_part_comp_Type())
rit_part_comp.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_part_comp.setStatus(_A)
if mibBuilder.loadTexts:rit_part_comp.setUnits(_G)
class _Rit_interbl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Rit_interbl_Type.__name__=_B
_Rit_interbl_Object=MibScalar
rit_interbl=_Rit_interbl_Object((1,3,6,1,4,1,9839,2,1,3,26),_Rit_interbl_Type())
rit_interbl.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_interbl.setStatus(_A)
if mibBuilder.loadTexts:rit_interbl.setUnits(_G)
class _Min_sp_comp_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Min_sp_comp_Type.__name__=_B
_Min_sp_comp_Object=MibScalar
min_sp_comp=_Min_sp_comp_Object((1,3,6,1,4,1,9839,2,1,3,27),_Min_sp_comp_Type())
min_sp_comp.setMaxAccess(_C)
if mibBuilder.loadTexts:min_sp_comp.setStatus(_A)
if mibBuilder.loadTexts:min_sp_comp.setUnits(_G)
class _New_pass_ut_Type(Integer32):defaultValue=1234;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32000))
_New_pass_ut_Type.__name__=_B
_New_pass_ut_Object=MibScalar
new_pass_ut=_New_pass_ut_Object((1,3,6,1,4,1,9839,2,1,3,28),_New_pass_ut_Type())
new_pass_ut.setMaxAccess(_C)
if mibBuilder.loadTexts:new_pass_ut.setStatus(_A)
if mibBuilder.loadTexts:new_pass_ut.setUnits(_D)
class _New_pass_cos_Type(Integer32):defaultValue=1234;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32000))
_New_pass_cos_Type.__name__=_B
_New_pass_cos_Object=MibScalar
new_pass_cos=_New_pass_cos_Object((1,3,6,1,4,1,9839,2,1,3,30),_New_pass_cos_Type())
new_pass_cos.setMaxAccess(_C)
if mibBuilder.loadTexts:new_pass_cos.setStatus(_A)
if mibBuilder.loadTexts:new_pass_cos.setUnits(_D)
class _Min_stes_comp_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Min_stes_comp_Type.__name__=_B
_Min_stes_comp_Object=MibScalar
min_stes_comp=_Min_stes_comp_Object((1,3,6,1,4,1,9839,2,1,3,31),_Min_stes_comp_Type())
min_stes_comp.setMaxAccess(_C)
if mibBuilder.loadTexts:min_stes_comp.setStatus(_A)
if mibBuilder.loadTexts:min_stes_comp.setUnits(_G)
class _Min_tra_comp_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Min_tra_comp_Type.__name__=_B
_Min_tra_comp_Object=MibScalar
min_tra_comp=_Min_tra_comp_Object((1,3,6,1,4,1,9839,2,1,3,32),_Min_tra_comp_Type())
min_tra_comp.setMaxAccess(_C)
if mibBuilder.loadTexts:min_tra_comp.setStatus(_A)
if mibBuilder.loadTexts:min_tra_comp.setUnits(_G)
class _Min_acc_comp_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Min_acc_comp_Type.__name__=_B
_Min_acc_comp_Object=MibScalar
min_acc_comp=_Min_acc_comp_Object((1,3,6,1,4,1,9839,2,1,3,33),_Min_acc_comp_Type())
min_acc_comp.setMaxAccess(_C)
if mibBuilder.loadTexts:min_acc_comp.setStatus(_A)
if mibBuilder.loadTexts:min_acc_comp.setUnits(_G)
class _Tempo_max_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Tempo_max_Type.__name__=_B
_Tempo_max_Object=MibScalar
tempo_max=_Tempo_max_Object((1,3,6,1,4,1,9839,2,1,3,35),_Tempo_max_Type())
tempo_max.setMaxAccess(_C)
if mibBuilder.loadTexts:tempo_max.setStatus(_A)
if mibBuilder.loadTexts:tempo_max.setUnits(_D)
class _Min_apertura_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_Min_apertura_Type.__name__=_B
_Min_apertura_Object=MibScalar
min_apertura=_Min_apertura_Object((1,3,6,1,4,1,9839,2,1,3,36),_Min_apertura_Type())
min_apertura.setMaxAccess(_C)
if mibBuilder.loadTexts:min_apertura.setStatus(_A)
if mibBuilder.loadTexts:min_apertura.setUnits('%')
class _Sgl_macchina_Type(Integer32):defaultValue=20000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32000))
_Sgl_macchina_Type.__name__=_B
_Sgl_macchina_Object=MibScalar
sgl_macchina=_Sgl_macchina_Object((1,3,6,1,4,1,9839,2,1,3,37),_Sgl_macchina_Type())
sgl_macchina.setMaxAccess(_C)
if mibBuilder.loadTexts:sgl_macchina.setStatus(_A)
if mibBuilder.loadTexts:sgl_macchina.setUnits(_D)
class _N_res_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_N_res_Type.__name__=_B
_N_res_Object=MibScalar
n_res=_N_res_Object((1,3,6,1,4,1,9839,2,1,3,41),_N_res_Type())
n_res.setMaxAccess(_C)
if mibBuilder.loadTexts:n_res.setStatus(_A)
if mibBuilder.loadTexts:n_res.setUnits(_D)
class _Tempo_integra_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Tempo_integra_Type.__name__=_B
_Tempo_integra_Object=MibScalar
tempo_integra=_Tempo_integra_Object((1,3,6,1,4,1,9839,2,1,3,42),_Tempo_integra_Type())
tempo_integra.setMaxAccess(_C)
if mibBuilder.loadTexts:tempo_integra.setStatus(_A)
if mibBuilder.loadTexts:tempo_integra.setUnits(_D)
mibBuilder.exportSymbols('CAREL-rtop_pco-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'rtop_pcoMIB':rtop_pcoMIB,'digitalObjects':digitalObjects,'start_stop':start_stop,'ventilatore_p':ventilatore_p,'cont_avv_a1':cont_avv_a1,'cont_avv_a2':cont_avv_a2,'resistenza1':resistenza1,'resistenza2':resistenza2,'umidifica':umidifica,'ventilatore1':ventilatore1,'ventilatore2':ventilatore2,'glb_al':glb_al,'mask_term1':mask_term1,'mask_term2':mask_term2,'mask_press_h1':mask_press_h1,'mask_press_h2':mask_press_h2,'mask_antigelo':mask_antigelo,'mask_q14':mask_q14,'mask_q15':mask_q15,'mask_q3':mask_q3,'mask_q4':mask_q4,'mask_q5':mask_q5,'mask_q6':mask_q6,'bassa_press1':bassa_press1,'bassa_press2':bassa_press2,'mask_interbl':mask_interbl,'mask_defrost1':mask_defrost1,'mask_defrost2':mask_defrost2,'mask_filtro':mask_filtro,'mask_term_res':mask_term_res,'en_pompacalore':en_pompacalore,'en_orologio':en_orologio,'en_umidita':en_umidita,'en_mandata':en_mandata,'en_supervisore':en_supervisore,'en_stampante':en_stampante,'en_freecool':en_freecool,'en_freeheat':en_freeheat,'en_compensazio':en_compensazio,'off_ventp_defr':off_ventp_defr,'en_sbrin_cont':en_sbrin_cont,'autostart':autostart,'en_remoto':en_remoto,'abil_rotaz':abil_rotaz,'sys_on':sys_on,'syson1':syson1,'en_binati':en_binati,'en_sond_text':en_sond_text,'en_sond_uext':en_sond_uext,'en_sond_def1':en_sond_def1,'en_sond_def2':en_sond_def2,'tipo_cont':tipo_cont,'analogObjects':analogObjects,'temp_aria_amb':temp_aria_amb,'temp_aria_est':temp_aria_est,'umid_ambiente':umid_ambiente,'umid_esterna':umid_esterna,'set_temp_ariae':set_temp_ariae,'set_temp_ariai':set_temp_ariai,'set_umid_est':set_umid_est,'set_umid_inv':set_umid_inv,'lim_sup_temp':lim_sup_temp,'lim_inf_temp':lim_inf_temp,'banda_temp_e':banda_temp_e,'banda_temp_i':banda_temp_i,'lim_sup_umid':lim_sup_umid,'lim_inf_umid':lim_inf_umid,'diff_umid_e':diff_umid_e,'diff_umid_i':diff_umid_i,'offset_fcool':offset_fcool,'diff_fcool':diff_fcool,'offset_fheat':offset_fheat,'diff_fheat':diff_fheat,'set_mandata':set_mandata,'ban_mandata':ban_mandata,'set_esterno':set_esterno,'diff_esterno_e':diff_esterno_e,'max_comp_e':max_comp_e,'set_min':set_min,'set_stop':set_stop,'zona_morta':zona_morta,'zona_morta_u':zona_morta_u,'sg_alta_in_e':sg_alta_in_e,'sg_bassa_in_e':sg_bassa_in_e,'sg_alta_in_i':sg_alta_in_i,'sg_bassa_in_i':sg_bassa_in_i,'tar_defrost1':tar_defrost1,'tar_defrost2':tar_defrost2,'offset_res':offset_res,'differ_res':differ_res,'tar_umid_amb':tar_umid_amb,'offset_valv':offset_valv,'diff_valv':diff_valv,'set_esternoi':set_esternoi,'max_comp_i':max_comp_i,'set_vent1':set_vent1,'set_vent2':set_vent2,'diff_vent1':diff_vent1,'diff_vent2':diff_vent2,'integerObjects':integerObjects,'ore_comp1':ore_comp1,'ore_comp2':ore_comp2,'rit_all_ht_in':rit_all_ht_in,'rit_all_press':rit_all_press,'n_comp_deum':n_comp_deum,'rit_stop_ventp':rit_stop_ventp,'rit_part_comp':rit_part_comp,'rit_interbl':rit_interbl,'min_sp_comp':min_sp_comp,'new_pass_ut':new_pass_ut,'new_pass_cos':new_pass_cos,'min_stes_comp':min_stes_comp,'min_tra_comp':min_tra_comp,'min_acc_comp':min_acc_comp,'tempo_max':tempo_max,'min_apertura':min_apertura,'sgl_macchina':sgl_macchina,'n_res':n_res,'tempo_integra':tempo_integra})