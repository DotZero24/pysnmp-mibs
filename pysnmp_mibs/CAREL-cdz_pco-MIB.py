_I='% x10'
_H='C x10'
_G='sec'
_F='%'
_E='read-write'
_D='read-only'
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
cdz_pcoMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_C)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_D)
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
netSize.setMaxAccess(_E)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_C)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_E)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_C)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_C)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_C)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_C)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_C)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_C)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_C)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_C)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_C)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_C)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Z1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z1_Type.__name__=_B
_Z1_Object=MibScalar
z1=_Z1_Object((1,3,6,1,4,1,9839,2,1,1,1),_Z1_Type())
z1.setMaxAccess(_D)
if mibBuilder.loadTexts:z1.setStatus(_A)
if mibBuilder.loadTexts:z1.setUnits(_C)
class _Z3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z3_Type.__name__=_B
_Z3_Object=MibScalar
z3=_Z3_Object((1,3,6,1,4,1,9839,2,1,1,3),_Z3_Type())
z3.setMaxAccess(_D)
if mibBuilder.loadTexts:z3.setStatus(_A)
if mibBuilder.loadTexts:z3.setUnits(_C)
class _Z4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z4_Type.__name__=_B
_Z4_Object=MibScalar
z4=_Z4_Object((1,3,6,1,4,1,9839,2,1,1,4),_Z4_Type())
z4.setMaxAccess(_D)
if mibBuilder.loadTexts:z4.setStatus(_A)
if mibBuilder.loadTexts:z4.setUnits(_C)
class _Z5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z5_Type.__name__=_B
_Z5_Object=MibScalar
z5=_Z5_Object((1,3,6,1,4,1,9839,2,1,1,5),_Z5_Type())
z5.setMaxAccess(_D)
if mibBuilder.loadTexts:z5.setStatus(_A)
if mibBuilder.loadTexts:z5.setUnits(_C)
class _Z6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z6_Type.__name__=_B
_Z6_Object=MibScalar
z6=_Z6_Object((1,3,6,1,4,1,9839,2,1,1,6),_Z6_Type())
z6.setMaxAccess(_D)
if mibBuilder.loadTexts:z6.setStatus(_A)
if mibBuilder.loadTexts:z6.setUnits(_C)
class _Z7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z7_Type.__name__=_B
_Z7_Object=MibScalar
z7=_Z7_Object((1,3,6,1,4,1,9839,2,1,1,7),_Z7_Type())
z7.setMaxAccess(_D)
if mibBuilder.loadTexts:z7.setStatus(_A)
if mibBuilder.loadTexts:z7.setUnits(_C)
class _Onr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Onr_Type.__name__=_B
_Onr_Object=MibScalar
onr=_Onr_Object((1,3,6,1,4,1,9839,2,1,1,8),_Onr_Type())
onr.setMaxAccess(_D)
if mibBuilder.loadTexts:onr.setStatus(_A)
if mibBuilder.loadTexts:onr.setUnits(_C)
class _Z9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z9_Type.__name__=_B
_Z9_Object=MibScalar
z9=_Z9_Object((1,3,6,1,4,1,9839,2,1,1,9),_Z9_Type())
z9.setMaxAccess(_D)
if mibBuilder.loadTexts:z9.setStatus(_A)
if mibBuilder.loadTexts:z9.setUnits(_C)
class _Z10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z10_Type.__name__=_B
_Z10_Object=MibScalar
z10=_Z10_Object((1,3,6,1,4,1,9839,2,1,1,10),_Z10_Type())
z10.setMaxAccess(_D)
if mibBuilder.loadTexts:z10.setStatus(_A)
if mibBuilder.loadTexts:z10.setUnits(_C)
class _Z12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Z12_Type.__name__=_B
_Z12_Object=MibScalar
z12=_Z12_Object((1,3,6,1,4,1,9839,2,1,1,11),_Z12_Type())
z12.setMaxAccess(_D)
if mibBuilder.loadTexts:z12.setStatus(_A)
if mibBuilder.loadTexts:z12.setUnits(_C)
class _Val_par_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Val_par_Type.__name__=_B
_Val_par_Object=MibScalar
val_par=_Val_par_Object((1,3,6,1,4,1,9839,2,1,1,12),_Val_par_Type())
val_par.setMaxAccess(_D)
if mibBuilder.loadTexts:val_par.setStatus(_A)
if mibBuilder.loadTexts:val_par.setUnits(_C)
class _Syson2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Syson2_Type.__name__=_B
_Syson2_Object=MibScalar
syson2=_Syson2_Object((1,3,6,1,4,1,9839,2,1,1,13),_Syson2_Type())
syson2.setMaxAccess(_D)
if mibBuilder.loadTexts:syson2.setStatus(_A)
if mibBuilder.loadTexts:syson2.setUnits(_C)
class _Val_es_ok_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Val_es_ok_Type.__name__=_B
_Val_es_ok_Object=MibScalar
val_es_ok=_Val_es_ok_Object((1,3,6,1,4,1,9839,2,1,1,14),_Val_es_ok_Type())
val_es_ok.setMaxAccess(_D)
if mibBuilder.loadTexts:val_es_ok.setStatus(_A)
if mibBuilder.loadTexts:val_es_ok.setUnits(_C)
class _Umidifica_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Umidifica_Type.__name__=_B
_Umidifica_Object=MibScalar
umidifica=_Umidifica_Object((1,3,6,1,4,1,9839,2,1,1,15),_Umidifica_Type())
umidifica.setMaxAccess(_D)
if mibBuilder.loadTexts:umidifica.setStatus(_A)
if mibBuilder.loadTexts:umidifica.setUnits(_C)
class _Parz1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Parz1_Type.__name__=_B
_Parz1_Object=MibScalar
parz1=_Parz1_Object((1,3,6,1,4,1,9839,2,1,1,16),_Parz1_Type())
parz1.setMaxAccess(_D)
if mibBuilder.loadTexts:parz1.setStatus(_A)
if mibBuilder.loadTexts:parz1.setUnits(_C)
class _Parz2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Parz2_Type.__name__=_B
_Parz2_Object=MibScalar
parz2=_Parz2_Object((1,3,6,1,4,1,9839,2,1,1,17),_Parz2_Type())
parz2.setMaxAccess(_D)
if mibBuilder.loadTexts:parz2.setStatus(_A)
if mibBuilder.loadTexts:parz2.setUnits(_C)
class _Valfre_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Valfre_Type.__name__=_B
_Valfre_Object=MibScalar
valfre=_Valfre_Object((1,3,6,1,4,1,9839,2,1,1,18),_Valfre_Type())
valfre.setMaxAccess(_D)
if mibBuilder.loadTexts:valfre.setStatus(_A)
if mibBuilder.loadTexts:valfre.setUnits(_C)
class _Valfre1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Valfre1_Type.__name__=_B
_Valfre1_Object=MibScalar
valfre1=_Valfre1_Object((1,3,6,1,4,1,9839,2,1,1,19),_Valfre1_Type())
valfre1.setMaxAccess(_D)
if mibBuilder.loadTexts:valfre1.setStatus(_A)
if mibBuilder.loadTexts:valfre1.setUnits(_C)
class _Valca_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Valca_Type.__name__=_B
_Valca_Object=MibScalar
valca=_Valca_Object((1,3,6,1,4,1,9839,2,1,1,20),_Valca_Type())
valca.setMaxAccess(_D)
if mibBuilder.loadTexts:valca.setStatus(_A)
if mibBuilder.loadTexts:valca.setUnits(_C)
class _Valca1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Valca1_Type.__name__=_B
_Valca1_Object=MibScalar
valca1=_Valca1_Object((1,3,6,1,4,1,9839,2,1,1,21),_Valca1_Type())
valca1.setMaxAccess(_D)
if mibBuilder.loadTexts:valca1.setStatus(_A)
if mibBuilder.loadTexts:valca1.setUnits(_C)
class _Glb_al_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Glb_al_Type.__name__=_B
_Glb_al_Object=MibScalar
glb_al=_Glb_al_Object((1,3,6,1,4,1,9839,2,1,1,22),_Glb_al_Type())
glb_al.setMaxAccess(_D)
if mibBuilder.loadTexts:glb_al.setStatus(_A)
if mibBuilder.loadTexts:glb_al.setUnits(_C)
class _S_firmanook_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_firmanook_Type.__name__=_B
_S_firmanook_Object=MibScalar
s_firmanook=_S_firmanook_Object((1,3,6,1,4,1,9839,2,1,1,23),_S_firmanook_Type())
s_firmanook.setMaxAccess(_E)
if mibBuilder.loadTexts:s_firmanook.setStatus(_A)
if mibBuilder.loadTexts:s_firmanook.setUnits(_C)
class _S_error_io_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_error_io_Type.__name__=_B
_S_error_io_Object=MibScalar
s_error_io=_S_error_io_Object((1,3,6,1,4,1,9839,2,1,1,24),_S_error_io_Type())
s_error_io.setMaxAccess(_D)
if mibBuilder.loadTexts:s_error_io.setStatus(_A)
if mibBuilder.loadTexts:s_error_io.setUnits(_C)
class _S_bp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_bp1_Type.__name__=_B
_S_bp1_Object=MibScalar
s_bp1=_S_bp1_Object((1,3,6,1,4,1,9839,2,1,1,25),_S_bp1_Type())
s_bp1.setMaxAccess(_D)
if mibBuilder.loadTexts:s_bp1.setStatus(_A)
if mibBuilder.loadTexts:s_bp1.setUnits(_C)
class _S_bp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_bp2_Type.__name__=_B
_S_bp2_Object=MibScalar
s_bp2=_S_bp2_Object((1,3,6,1,4,1,9839,2,1,1,26),_S_bp2_Type())
s_bp2.setMaxAccess(_D)
if mibBuilder.loadTexts:s_bp2.setStatus(_A)
if mibBuilder.loadTexts:s_bp2.setUnits(_C)
class _S_fl1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_fl1_Type.__name__=_B
_S_fl1_Object=MibScalar
s_fl1=_S_fl1_Object((1,3,6,1,4,1,9839,2,1,1,27),_S_fl1_Type())
s_fl1.setMaxAccess(_D)
if mibBuilder.loadTexts:s_fl1.setStatus(_A)
if mibBuilder.loadTexts:s_fl1.setUnits(_C)
class _S_trf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_trf_Type.__name__=_B
_S_trf_Object=MibScalar
s_trf=_S_trf_Object((1,3,6,1,4,1,9839,2,1,1,28),_S_trf_Type())
s_trf.setMaxAccess(_D)
if mibBuilder.loadTexts:s_trf.setStatus(_A)
if mibBuilder.loadTexts:s_trf.setUnits(_C)
class _S_trs1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_trs1_Type.__name__=_B
_S_trs1_Object=MibScalar
s_trs1=_S_trs1_Object((1,3,6,1,4,1,9839,2,1,1,29),_S_trs1_Type())
s_trs1.setMaxAccess(_D)
if mibBuilder.loadTexts:s_trs1.setStatus(_A)
if mibBuilder.loadTexts:s_trs1.setUnits(_C)
class _S_trs2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_trs2_Type.__name__=_B
_S_trs2_Object=MibScalar
s_trs2=_S_trs2_Object((1,3,6,1,4,1,9839,2,1,1,30),_S_trs2_Type())
s_trs2.setMaxAccess(_D)
if mibBuilder.loadTexts:s_trs2.setStatus(_A)
if mibBuilder.loadTexts:s_trs2.setUnits(_C)
class _S_fsa_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_fsa_Type.__name__=_B
_S_fsa_Object=MibScalar
s_fsa=_S_fsa_Object((1,3,6,1,4,1,9839,2,1,1,31),_S_fsa_Type())
s_fsa.setMaxAccess(_D)
if mibBuilder.loadTexts:s_fsa.setStatus(_A)
if mibBuilder.loadTexts:s_fsa.setUnits(_C)
class _S_flt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_flt_Type.__name__=_B
_S_flt_Object=MibScalar
s_flt=_S_flt_Object((1,3,6,1,4,1,9839,2,1,1,32),_S_flt_Type())
s_flt.setMaxAccess(_D)
if mibBuilder.loadTexts:s_flt.setStatus(_A)
if mibBuilder.loadTexts:s_flt.setUnits(_C)
class _S_all_h_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_all_h_temp_Type.__name__=_B
_S_all_h_temp_Object=MibScalar
s_all_h_temp=_S_all_h_temp_Object((1,3,6,1,4,1,9839,2,1,1,33),_S_all_h_temp_Type())
s_all_h_temp.setMaxAccess(_D)
if mibBuilder.loadTexts:s_all_h_temp.setStatus(_A)
if mibBuilder.loadTexts:s_all_h_temp.setUnits(_C)
class _S_all_l_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_all_l_temp_Type.__name__=_B
_S_all_l_temp_Object=MibScalar
s_all_l_temp=_S_all_l_temp_Object((1,3,6,1,4,1,9839,2,1,1,34),_S_all_l_temp_Type())
s_all_l_temp.setMaxAccess(_D)
if mibBuilder.loadTexts:s_all_l_temp.setStatus(_A)
if mibBuilder.loadTexts:s_all_l_temp.setUnits(_C)
class _S_all_h_umid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_all_h_umid_Type.__name__=_B
_S_all_h_umid_Object=MibScalar
s_all_h_umid=_S_all_h_umid_Object((1,3,6,1,4,1,9839,2,1,1,35),_S_all_h_umid_Type())
s_all_h_umid.setMaxAccess(_D)
if mibBuilder.loadTexts:s_all_h_umid.setStatus(_A)
if mibBuilder.loadTexts:s_all_h_umid.setUnits(_C)
class _S_all_l_umid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_all_l_umid_Type.__name__=_B
_S_all_l_umid_Object=MibScalar
s_all_l_umid=_S_all_l_umid_Object((1,3,6,1,4,1,9839,2,1,1,36),_S_all_l_umid_Type())
s_all_l_umid.setMaxAccess(_D)
if mibBuilder.loadTexts:s_all_l_umid.setStatus(_A)
if mibBuilder.loadTexts:s_all_l_umid.setUnits(_C)
class _S_al_ore_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_al_ore_comp1_Type.__name__=_B
_S_al_ore_comp1_Object=MibScalar
s_al_ore_comp1=_S_al_ore_comp1_Object((1,3,6,1,4,1,9839,2,1,1,37),_S_al_ore_comp1_Type())
s_al_ore_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:s_al_ore_comp1.setStatus(_A)
if mibBuilder.loadTexts:s_al_ore_comp1.setUnits(_C)
class _S_al_ore_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_al_ore_comp2_Type.__name__=_B
_S_al_ore_comp2_Object=MibScalar
s_al_ore_comp2=_S_al_ore_comp2_Object((1,3,6,1,4,1,9839,2,1,1,38),_S_al_ore_comp2_Type())
s_al_ore_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:s_al_ore_comp2.setStatus(_A)
if mibBuilder.loadTexts:s_al_ore_comp2.setUnits(_C)
class _S_al_ore_umidif_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_al_ore_umidif_Type.__name__=_B
_S_al_ore_umidif_Object=MibScalar
s_al_ore_umidif=_S_al_ore_umidif_Object((1,3,6,1,4,1,9839,2,1,1,39),_S_al_ore_umidif_Type())
s_al_ore_umidif.setMaxAccess(_D)
if mibBuilder.loadTexts:s_al_ore_umidif.setStatus(_A)
if mibBuilder.loadTexts:s_al_ore_umidif.setUnits(_C)
class _S_al_ore_mac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_al_ore_mac_Type.__name__=_B
_S_al_ore_mac_Object=MibScalar
s_al_ore_mac=_S_al_ore_mac_Object((1,3,6,1,4,1,9839,2,1,1,40),_S_al_ore_mac_Type())
s_al_ore_mac.setMaxAccess(_D)
if mibBuilder.loadTexts:s_al_ore_mac.setStatus(_A)
if mibBuilder.loadTexts:s_al_ore_mac.setUnits(_C)
class _S_al_ore_res1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_al_ore_res1_Type.__name__=_B
_S_al_ore_res1_Object=MibScalar
s_al_ore_res1=_S_al_ore_res1_Object((1,3,6,1,4,1,9839,2,1,1,41),_S_al_ore_res1_Type())
s_al_ore_res1.setMaxAccess(_D)
if mibBuilder.loadTexts:s_al_ore_res1.setStatus(_A)
if mibBuilder.loadTexts:s_al_ore_res1.setUnits(_C)
class _S_al_ore_res2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_al_ore_res2_Type.__name__=_B
_S_al_ore_res2_Object=MibScalar
s_al_ore_res2=_S_al_ore_res2_Object((1,3,6,1,4,1,9839,2,1,1,42),_S_al_ore_res2_Type())
s_al_ore_res2.setMaxAccess(_D)
if mibBuilder.loadTexts:s_al_ore_res2.setStatus(_A)
if mibBuilder.loadTexts:s_al_ore_res2.setUnits(_C)
class _S_all_h_free_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_all_h_free_Type.__name__=_B
_S_all_h_free_Object=MibScalar
s_all_h_free=_S_all_h_free_Object((1,3,6,1,4,1,9839,2,1,1,43),_S_all_h_free_Type())
s_all_h_free.setMaxAccess(_D)
if mibBuilder.loadTexts:s_all_h_free.setStatus(_A)
if mibBuilder.loadTexts:s_all_h_free.setUnits(_C)
class _S_all_l_free_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_all_l_free_Type.__name__=_B
_S_all_l_free_Object=MibScalar
s_all_l_free=_S_all_l_free_Object((1,3,6,1,4,1,9839,2,1,1,44),_S_all_l_free_Type())
s_all_l_free.setMaxAccess(_D)
if mibBuilder.loadTexts:s_all_l_free.setStatus(_A)
if mibBuilder.loadTexts:s_all_l_free.setUnits(_C)
class _S_sonda1_ko_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_sonda1_ko_Type.__name__=_B
_S_sonda1_ko_Object=MibScalar
s_sonda1_ko=_S_sonda1_ko_Object((1,3,6,1,4,1,9839,2,1,1,45),_S_sonda1_ko_Type())
s_sonda1_ko.setMaxAccess(_D)
if mibBuilder.loadTexts:s_sonda1_ko.setStatus(_A)
if mibBuilder.loadTexts:s_sonda1_ko.setUnits(_C)
class _S_sonda2_ko_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_sonda2_ko_Type.__name__=_B
_S_sonda2_ko_Object=MibScalar
s_sonda2_ko=_S_sonda2_ko_Object((1,3,6,1,4,1,9839,2,1,1,46),_S_sonda2_ko_Type())
s_sonda2_ko.setMaxAccess(_D)
if mibBuilder.loadTexts:s_sonda2_ko.setStatus(_A)
if mibBuilder.loadTexts:s_sonda2_ko.setUnits(_C)
class _S_sonda4_ko_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_sonda4_ko_Type.__name__=_B
_S_sonda4_ko_Object=MibScalar
s_sonda4_ko=_S_sonda4_ko_Object((1,3,6,1,4,1,9839,2,1,1,47),_S_sonda4_ko_Type())
s_sonda4_ko.setMaxAccess(_D)
if mibBuilder.loadTexts:s_sonda4_ko.setStatus(_A)
if mibBuilder.loadTexts:s_sonda4_ko.setUnits(_C)
class _S_sonda6_ko_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_sonda6_ko_Type.__name__=_B
_S_sonda6_ko_Object=MibScalar
s_sonda6_ko=_S_sonda6_ko_Object((1,3,6,1,4,1,9839,2,1,1,48),_S_sonda6_ko_Type())
s_sonda6_ko.setMaxAccess(_D)
if mibBuilder.loadTexts:s_sonda6_ko.setStatus(_A)
if mibBuilder.loadTexts:s_sonda6_ko.setUnits(_C)
class _S_sondau_ko_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_sondau_ko_Type.__name__=_B
_S_sondau_ko_Object=MibScalar
s_sondau_ko=_S_sondau_ko_Object((1,3,6,1,4,1,9839,2,1,1,49),_S_sondau_ko_Type())
s_sondau_ko.setMaxAccess(_D)
if mibBuilder.loadTexts:s_sondau_ko.setStatus(_A)
if mibBuilder.loadTexts:s_sondau_ko.setUnits(_C)
class _S_epromnook_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_epromnook_Type.__name__=_B
_S_epromnook_Object=MibScalar
s_epromnook=_S_epromnook_Object((1,3,6,1,4,1,9839,2,1,1,51),_S_epromnook_Type())
s_epromnook.setMaxAccess(_D)
if mibBuilder.loadTexts:s_epromnook.setStatus(_A)
if mibBuilder.loadTexts:s_epromnook.setUnits(_C)
class _Pro_pi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pro_pi_Type.__name__=_B
_Pro_pi_Object=MibScalar
pro_pi=_Pro_pi_Object((1,3,6,1,4,1,9839,2,1,1,53),_Pro_pi_Type())
pro_pi.setMaxAccess(_E)
if mibBuilder.loadTexts:pro_pi.setStatus(_A)
if mibBuilder.loadTexts:pro_pi.setUnits(_C)
class _Si_sond_umid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_sond_umid_Type.__name__=_B
_Si_sond_umid_Object=MibScalar
si_sond_umid=_Si_sond_umid_Object((1,3,6,1,4,1,9839,2,1,1,55),_Si_sond_umid_Type())
si_sond_umid.setMaxAccess(_E)
if mibBuilder.loadTexts:si_sond_umid.setStatus(_A)
if mibBuilder.loadTexts:si_sond_umid.setUnits(_C)
class _Si_sond_acqua_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_sond_acqua_Type.__name__=_B
_Si_sond_acqua_Object=MibScalar
si_sond_acqua=_Si_sond_acqua_Object((1,3,6,1,4,1,9839,2,1,1,56),_Si_sond_acqua_Type())
si_sond_acqua.setMaxAccess(_E)
if mibBuilder.loadTexts:si_sond_acqua.setStatus(_A)
if mibBuilder.loadTexts:si_sond_acqua.setUnits(_C)
class _Si_sond_aria_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_sond_aria_Type.__name__=_B
_Si_sond_aria_Object=MibScalar
si_sond_aria=_Si_sond_aria_Object((1,3,6,1,4,1,9839,2,1,1,57),_Si_sond_aria_Type())
si_sond_aria.setMaxAccess(_E)
if mibBuilder.loadTexts:si_sond_aria.setStatus(_A)
if mibBuilder.loadTexts:si_sond_aria.setUnits(_C)
class _Si_sond_acquain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_sond_acquain_Type.__name__=_B
_Si_sond_acquain_Object=MibScalar
si_sond_acquain=_Si_sond_acquain_Object((1,3,6,1,4,1,9839,2,1,1,58),_Si_sond_acquain_Type())
si_sond_acquain.setMaxAccess(_E)
if mibBuilder.loadTexts:si_sond_acquain.setStatus(_A)
if mibBuilder.loadTexts:si_sond_acquain.setUnits(_C)
class _Si_sond_ariain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_sond_ariain_Type.__name__=_B
_Si_sond_ariain_Object=MibScalar
si_sond_ariain=_Si_sond_ariain_Object((1,3,6,1,4,1,9839,2,1,1,59),_Si_sond_ariain_Type())
si_sond_ariain.setMaxAccess(_E)
if mibBuilder.loadTexts:si_sond_ariain.setStatus(_A)
if mibBuilder.loadTexts:si_sond_ariain.setUnits(_C)
class _Bin_sta_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bin_sta_Type.__name__=_B
_Bin_sta_Object=MibScalar
bin_sta=_Bin_sta_Object((1,3,6,1,4,1,9839,2,1,1,60),_Bin_sta_Type())
bin_sta.setMaxAccess(_E)
if mibBuilder.loadTexts:bin_sta.setStatus(_A)
if mibBuilder.loadTexts:bin_sta.setUnits(_C)
class _Si_rampap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_rampap_Type.__name__=_B
_Si_rampap_Object=MibScalar
si_rampap=_Si_rampap_Object((1,3,6,1,4,1,9839,2,1,1,61),_Si_rampap_Type())
si_rampap.setMaxAccess(_E)
if mibBuilder.loadTexts:si_rampap.setStatus(_A)
if mibBuilder.loadTexts:si_rampap.setUnits(_C)
class _Es_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Es_Type.__name__=_B
_Es_Object=MibScalar
es=_Es_Object((1,3,6,1,4,1,9839,2,1,1,62),_Es_Type())
es.setMaxAccess(_E)
if mibBuilder.loadTexts:es.setStatus(_A)
if mibBuilder.loadTexts:es.setUnits(_C)
class _Si_comp_es_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_comp_es_Type.__name__=_B
_Si_comp_es_Object=MibScalar
si_comp_es=_Si_comp_es_Object((1,3,6,1,4,1,9839,2,1,1,63),_Si_comp_es_Type())
si_comp_es.setMaxAccess(_E)
if mibBuilder.loadTexts:si_comp_es.setStatus(_A)
if mibBuilder.loadTexts:si_comp_es.setUnits(_C)
class _Si_rampan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_rampan_Type.__name__=_B
_Si_rampan_Object=MibScalar
si_rampan=_Si_rampan_Object((1,3,6,1,4,1,9839,2,1,1,64),_Si_rampan_Type())
si_rampan.setMaxAccess(_E)
if mibBuilder.loadTexts:si_rampan.setStatus(_A)
if mibBuilder.loadTexts:si_rampan.setUnits(_C)
class _Si_parz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_parz_Type.__name__=_B
_Si_parz_Object=MibScalar
si_parz=_Si_parz_Object((1,3,6,1,4,1,9839,2,1,1,65),_Si_parz_Type())
si_parz.setMaxAccess(_E)
if mibBuilder.loadTexts:si_parz.setStatus(_A)
if mibBuilder.loadTexts:si_parz.setUnits(_C)
class _Si_rot2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_rot2_Type.__name__=_B
_Si_rot2_Object=MibScalar
si_rot2=_Si_rot2_Object((1,3,6,1,4,1,9839,2,1,1,66),_Si_rot2_Type())
si_rot2.setMaxAccess(_E)
if mibBuilder.loadTexts:si_rot2.setStatus(_A)
if mibBuilder.loadTexts:si_rot2.setUnits(_C)
class _Si_comp1_deu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_comp1_deu_Type.__name__=_B
_Si_comp1_deu_Object=MibScalar
si_comp1_deu=_Si_comp1_deu_Object((1,3,6,1,4,1,9839,2,1,1,67),_Si_comp1_deu_Type())
si_comp1_deu.setMaxAccess(_E)
if mibBuilder.loadTexts:si_comp1_deu.setStatus(_A)
if mibBuilder.loadTexts:si_comp1_deu.setUnits(_C)
class _Si_comp2_deu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_comp2_deu_Type.__name__=_B
_Si_comp2_deu_Object=MibScalar
si_comp2_deu=_Si_comp2_deu_Object((1,3,6,1,4,1,9839,2,1,1,68),_Si_comp2_deu_Type())
si_comp2_deu.setMaxAccess(_E)
if mibBuilder.loadTexts:si_comp2_deu.setStatus(_A)
if mibBuilder.loadTexts:si_comp2_deu.setUnits(_C)
class _Si_fasce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_fasce_Type.__name__=_B
_Si_fasce_Object=MibScalar
si_fasce=_Si_fasce_Object((1,3,6,1,4,1,9839,2,1,1,71),_Si_fasce_Type())
si_fasce.setMaxAccess(_E)
if mibBuilder.loadTexts:si_fasce.setStatus(_A)
if mibBuilder.loadTexts:si_fasce.setUnits(_C)
class _Syson_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Syson_Type.__name__=_B
_Syson_Object=MibScalar
syson=_Syson_Object((1,3,6,1,4,1,9839,2,1,1,73),_Syson_Type())
syson.setMaxAccess(_E)
if mibBuilder.loadTexts:syson.setStatus(_A)
if mibBuilder.loadTexts:syson.setUnits(_C)
class _Si_rampap3v_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_rampap3v_Type.__name__=_B
_Si_rampap3v_Object=MibScalar
si_rampap3v=_Si_rampap3v_Object((1,3,6,1,4,1,9839,2,1,1,74),_Si_rampap3v_Type())
si_rampap3v.setMaxAccess(_E)
if mibBuilder.loadTexts:si_rampap3v.setStatus(_A)
if mibBuilder.loadTexts:si_rampap3v.setUnits(_C)
class _Si_rampan3v_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Si_rampan3v_Type.__name__=_B
_Si_rampan3v_Object=MibScalar
si_rampan3v=_Si_rampan3v_Object((1,3,6,1,4,1,9839,2,1,1,75),_Si_rampan3v_Type())
si_rampan3v.setMaxAccess(_E)
if mibBuilder.loadTexts:si_rampan3v.setStatus(_A)
if mibBuilder.loadTexts:si_rampan3v.setUnits(_C)
class _Manuale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Manuale_Type.__name__=_B
_Manuale_Object=MibScalar
manuale=_Manuale_Object((1,3,6,1,4,1,9839,2,1,1,76),_Manuale_Type())
manuale.setMaxAccess(_E)
if mibBuilder.loadTexts:manuale.setStatus(_A)
if mibBuilder.loadTexts:manuale.setUnits(_C)
class _Start_off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Start_off_Type.__name__=_B
_Start_off_Object=MibScalar
start_off=_Start_off_Object((1,3,6,1,4,1,9839,2,1,1,77),_Start_off_Type())
start_off.setMaxAccess(_E)
if mibBuilder.loadTexts:start_off.setStatus(_A)
if mibBuilder.loadTexts:start_off.setUnits(_C)
class _Alarm_e06_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm_e06_Type.__name__=_B
_Alarm_e06_Object=MibScalar
alarm_e06=_Alarm_e06_Object((1,3,6,1,4,1,9839,2,1,1,80),_Alarm_e06_Type())
alarm_e06.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm_e06.setStatus(_A)
if mibBuilder.loadTexts:alarm_e06.setUnits(_C)
class _Alarm_e08_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm_e08_Type.__name__=_B
_Alarm_e08_Object=MibScalar
alarm_e08=_Alarm_e08_Object((1,3,6,1,4,1,9839,2,1,1,81),_Alarm_e08_Type())
alarm_e08.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm_e08.setStatus(_A)
if mibBuilder.loadTexts:alarm_e08.setUnits(_C)
class _Alarm_e09_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm_e09_Type.__name__=_B
_Alarm_e09_Object=MibScalar
alarm_e09=_Alarm_e09_Object((1,3,6,1,4,1,9839,2,1,1,82),_Alarm_e09_Type())
alarm_e09.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm_e09.setStatus(_A)
if mibBuilder.loadTexts:alarm_e09.setUnits(_C)
class _Alarm_e10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm_e10_Type.__name__=_B
_Alarm_e10_Object=MibScalar
alarm_e10=_Alarm_e10_Object((1,3,6,1,4,1,9839,2,1,1,83),_Alarm_e10_Type())
alarm_e10.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm_e10.setStatus(_A)
if mibBuilder.loadTexts:alarm_e10.setUnits(_C)
class _Alarm_e11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm_e11_Type.__name__=_B
_Alarm_e11_Object=MibScalar
alarm_e11=_Alarm_e11_Object((1,3,6,1,4,1,9839,2,1,1,84),_Alarm_e11_Type())
alarm_e11.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm_e11.setStatus(_A)
if mibBuilder.loadTexts:alarm_e11.setUnits(_C)
class _Alarm_e12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm_e12_Type.__name__=_B
_Alarm_e12_Object=MibScalar
alarm_e12=_Alarm_e12_Object((1,3,6,1,4,1,9839,2,1,1,85),_Alarm_e12_Type())
alarm_e12.setMaxAccess(_D)
if mibBuilder.loadTexts:alarm_e12.setStatus(_A)
if mibBuilder.loadTexts:alarm_e12.setUnits(_C)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Temp_Type.__name__=_B
_Temp_Object=MibScalar
temp=_Temp_Object((1,3,6,1,4,1,9839,2,1,2,1),_Temp_Type())
temp.setMaxAccess(_D)
if mibBuilder.loadTexts:temp.setStatus(_A)
if mibBuilder.loadTexts:temp.setUnits(_C)
class _Umid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Umid_Type.__name__=_B
_Umid_Object=MibScalar
umid=_Umid_Object((1,3,6,1,4,1,9839,2,1,2,2),_Umid_Type())
umid.setMaxAccess(_D)
if mibBuilder.loadTexts:umid.setStatus(_A)
if mibBuilder.loadTexts:umid.setUnits(_C)
class _Acqua_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Acqua_Type.__name__=_B
_Acqua_Object=MibScalar
acqua=_Acqua_Object((1,3,6,1,4,1,9839,2,1,2,3),_Acqua_Type())
acqua.setMaxAccess(_D)
if mibBuilder.loadTexts:acqua.setStatus(_A)
if mibBuilder.loadTexts:acqua.setUnits(_C)
class _Aria_acqua_in_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Aria_acqua_in_Type.__name__=_B
_Aria_acqua_in_Object=MibScalar
aria_acqua_in=_Aria_acqua_in_Object((1,3,6,1,4,1,9839,2,1,2,4),_Aria_acqua_in_Type())
aria_acqua_in.setMaxAccess(_D)
if mibBuilder.loadTexts:aria_acqua_in.setStatus(_A)
if mibBuilder.loadTexts:aria_acqua_in.setUnits(_C)
class _Temp_aria_man_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Temp_aria_man_Type.__name__=_B
_Temp_aria_man_Object=MibScalar
temp_aria_man=_Temp_aria_man_Object((1,3,6,1,4,1,9839,2,1,2,5),_Temp_aria_man_Type())
temp_aria_man.setMaxAccess(_D)
if mibBuilder.loadTexts:temp_aria_man.setStatus(_A)
if mibBuilder.loadTexts:temp_aria_man.setUnits(_C)
class _Zona_morta_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Zona_morta_Type.__name__=_B
_Zona_morta_Object=MibScalar
zona_morta=_Zona_morta_Object((1,3,6,1,4,1,9839,2,1,2,6),_Zona_morta_Type())
zona_morta.setMaxAccess(_E)
if mibBuilder.loadTexts:zona_morta.setStatus(_A)
if mibBuilder.loadTexts:zona_morta.setUnits(_H)
class _Banda_hum_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Banda_hum_Type.__name__=_B
_Banda_hum_Object=MibScalar
banda_hum=_Banda_hum_Object((1,3,6,1,4,1,9839,2,1,2,7),_Banda_hum_Type())
banda_hum.setMaxAccess(_E)
if mibBuilder.loadTexts:banda_hum.setStatus(_A)
if mibBuilder.loadTexts:banda_hum.setUnits(_I)
class _Set_hum_a_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_hum_a_Type.__name__=_B
_Set_hum_a_Object=MibScalar
set_hum_a=_Set_hum_a_Object((1,3,6,1,4,1,9839,2,1,2,8),_Set_hum_a_Type())
set_hum_a.setMaxAccess(_E)
if mibBuilder.loadTexts:set_hum_a.setStatus(_A)
if mibBuilder.loadTexts:set_hum_a.setUnits(_I)
class _Sgl_l_temp_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Sgl_l_temp_Type.__name__=_B
_Sgl_l_temp_Object=MibScalar
sgl_l_temp=_Sgl_l_temp_Object((1,3,6,1,4,1,9839,2,1,2,9),_Sgl_l_temp_Type())
sgl_l_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_l_temp.setStatus(_A)
if mibBuilder.loadTexts:sgl_l_temp.setUnits(_H)
class _Sgl_h_temp_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Sgl_h_temp_Type.__name__=_B
_Sgl_h_temp_Object=MibScalar
sgl_h_temp=_Sgl_h_temp_Object((1,3,6,1,4,1,9839,2,1,2,10),_Sgl_h_temp_Type())
sgl_h_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_h_temp.setStatus(_A)
if mibBuilder.loadTexts:sgl_h_temp.setUnits(_H)
class _Sgl_l_umid_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Sgl_l_umid_Type.__name__=_B
_Sgl_l_umid_Object=MibScalar
sgl_l_umid=_Sgl_l_umid_Object((1,3,6,1,4,1,9839,2,1,2,11),_Sgl_l_umid_Type())
sgl_l_umid.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_l_umid.setStatus(_A)
if mibBuilder.loadTexts:sgl_l_umid.setUnits(_I)
class _Sgl_h_umid_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Sgl_h_umid_Type.__name__=_B
_Sgl_h_umid_Object=MibScalar
sgl_h_umid=_Sgl_h_umid_Object((1,3,6,1,4,1,9839,2,1,2,12),_Sgl_h_umid_Type())
sgl_h_umid.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_h_umid.setStatus(_A)
if mibBuilder.loadTexts:sgl_h_umid.setUnits(_I)
class _Set_temp_a_Type(Integer32):defaultValue=230;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_temp_a_Type.__name__=_B
_Set_temp_a_Object=MibScalar
set_temp_a=_Set_temp_a_Object((1,3,6,1,4,1,9839,2,1,2,13),_Set_temp_a_Type())
set_temp_a.setMaxAccess(_E)
if mibBuilder.loadTexts:set_temp_a.setStatus(_A)
if mibBuilder.loadTexts:set_temp_a.setUnits(_H)
class _Banda_temp_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Banda_temp_Type.__name__=_B
_Banda_temp_Object=MibScalar
banda_temp=_Banda_temp_Object((1,3,6,1,4,1,9839,2,1,2,17),_Banda_temp_Type())
banda_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:banda_temp.setStatus(_A)
if mibBuilder.loadTexts:banda_temp.setUnits(_H)
class _Sgl_l_free_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-999,999))
_Sgl_l_free_Type.__name__=_B
_Sgl_l_free_Object=MibScalar
sgl_l_free=_Sgl_l_free_Object((1,3,6,1,4,1,9839,2,1,2,18),_Sgl_l_free_Type())
sgl_l_free.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_l_free.setStatus(_A)
if mibBuilder.loadTexts:sgl_l_free.setUnits(_H)
class _Sgl_h_free_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-999,999))
_Sgl_h_free_Type.__name__=_B
_Sgl_h_free_Object=MibScalar
sgl_h_free=_Sgl_h_free_Object((1,3,6,1,4,1,9839,2,1,2,19),_Sgl_h_free_Type())
sgl_h_free.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_h_free.setStatus(_A)
if mibBuilder.loadTexts:sgl_h_free.setUnits(_H)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _In_rampa_p_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_In_rampa_p_Type.__name__=_B
_In_rampa_p_Object=MibScalar
in_rampa_p=_In_rampa_p_Object((1,3,6,1,4,1,9839,2,1,3,10),_In_rampa_p_Type())
in_rampa_p.setMaxAccess(_E)
if mibBuilder.loadTexts:in_rampa_p.setStatus(_A)
if mibBuilder.loadTexts:in_rampa_p.setUnits(_F)
class _Fin_rampa_p_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fin_rampa_p_Type.__name__=_B
_Fin_rampa_p_Object=MibScalar
fin_rampa_p=_Fin_rampa_p_Object((1,3,6,1,4,1,9839,2,1,3,11),_Fin_rampa_p_Type())
fin_rampa_p.setMaxAccess(_E)
if mibBuilder.loadTexts:fin_rampa_p.setStatus(_A)
if mibBuilder.loadTexts:fin_rampa_p.setUnits(_F)
class _In_rampa_n_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_In_rampa_n_Type.__name__=_B
_In_rampa_n_Object=MibScalar
in_rampa_n=_In_rampa_n_Object((1,3,6,1,4,1,9839,2,1,3,12),_In_rampa_n_Type())
in_rampa_n.setMaxAccess(_E)
if mibBuilder.loadTexts:in_rampa_n.setStatus(_A)
if mibBuilder.loadTexts:in_rampa_n.setUnits(_F)
class _Fin_rampa_n_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fin_rampa_n_Type.__name__=_B
_Fin_rampa_n_Object=MibScalar
fin_rampa_n=_Fin_rampa_n_Object((1,3,6,1,4,1,9839,2,1,3,13),_Fin_rampa_n_Type())
fin_rampa_n.setMaxAccess(_E)
if mibBuilder.loadTexts:fin_rampa_n.setStatus(_A)
if mibBuilder.loadTexts:fin_rampa_n.setUnits(_F)
class _Set_comp1_cw_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_comp1_cw_Type.__name__=_B
_Set_comp1_cw_Object=MibScalar
set_comp1_cw=_Set_comp1_cw_Object((1,3,6,1,4,1,9839,2,1,3,16),_Set_comp1_cw_Type())
set_comp1_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:set_comp1_cw.setStatus(_A)
if mibBuilder.loadTexts:set_comp1_cw.setUnits(_F)
class _Ist_comp1_cw_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_comp1_cw_Type.__name__=_B
_Ist_comp1_cw_Object=MibScalar
ist_comp1_cw=_Ist_comp1_cw_Object((1,3,6,1,4,1,9839,2,1,3,17),_Ist_comp1_cw_Type())
ist_comp1_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_comp1_cw.setStatus(_A)
if mibBuilder.loadTexts:ist_comp1_cw.setUnits(_F)
class _Set_comp2_cw_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_comp2_cw_Type.__name__=_B
_Set_comp2_cw_Object=MibScalar
set_comp2_cw=_Set_comp2_cw_Object((1,3,6,1,4,1,9839,2,1,3,18),_Set_comp2_cw_Type())
set_comp2_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:set_comp2_cw.setStatus(_A)
if mibBuilder.loadTexts:set_comp2_cw.setUnits(_F)
class _Ist_comp2_cw_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_comp2_cw_Type.__name__=_B
_Ist_comp2_cw_Object=MibScalar
ist_comp2_cw=_Ist_comp2_cw_Object((1,3,6,1,4,1,9839,2,1,3,19),_Ist_comp2_cw_Type())
ist_comp2_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_comp2_cw.setStatus(_A)
if mibBuilder.loadTexts:ist_comp2_cw.setUnits(_F)
class _Set_comp1_es_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_comp1_es_Type.__name__=_B
_Set_comp1_es_Object=MibScalar
set_comp1_es=_Set_comp1_es_Object((1,3,6,1,4,1,9839,2,1,3,22),_Set_comp1_es_Type())
set_comp1_es.setMaxAccess(_E)
if mibBuilder.loadTexts:set_comp1_es.setStatus(_A)
if mibBuilder.loadTexts:set_comp1_es.setUnits(_F)
class _Ist_comp1_es_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_comp1_es_Type.__name__=_B
_Ist_comp1_es_Object=MibScalar
ist_comp1_es=_Ist_comp1_es_Object((1,3,6,1,4,1,9839,2,1,3,23),_Ist_comp1_es_Type())
ist_comp1_es.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_comp1_es.setStatus(_A)
if mibBuilder.loadTexts:ist_comp1_es.setUnits(_F)
class _Set_comp2_es_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_comp2_es_Type.__name__=_B
_Set_comp2_es_Object=MibScalar
set_comp2_es=_Set_comp2_es_Object((1,3,6,1,4,1,9839,2,1,3,24),_Set_comp2_es_Type())
set_comp2_es.setMaxAccess(_E)
if mibBuilder.loadTexts:set_comp2_es.setStatus(_A)
if mibBuilder.loadTexts:set_comp2_es.setUnits(_F)
class _Ist_comp2_es_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_comp2_es_Type.__name__=_B
_Ist_comp2_es_Object=MibScalar
ist_comp2_es=_Ist_comp2_es_Object((1,3,6,1,4,1,9839,2,1,3,25),_Ist_comp2_es_Type())
ist_comp2_es.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_comp2_es.setStatus(_A)
if mibBuilder.loadTexts:ist_comp2_es.setUnits(_F)
class _Rit_fra_ins_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_fra_ins_Type.__name__=_B
_Rit_fra_ins_Object=MibScalar
rit_fra_ins=_Rit_fra_ins_Object((1,3,6,1,4,1,9839,2,1,3,26),_Rit_fra_ins_Type())
rit_fra_ins.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_fra_ins.setStatus(_A)
if mibBuilder.loadTexts:rit_fra_ins.setUnits(_G)
class _Rit_bassa_pres_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_bassa_pres_Type.__name__=_B
_Rit_bassa_pres_Object=MibScalar
rit_bassa_pres=_Rit_bassa_pres_Object((1,3,6,1,4,1,9839,2,1,3,28),_Rit_bassa_pres_Type())
rit_bassa_pres.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_bassa_pres.setStatus(_A)
if mibBuilder.loadTexts:rit_bassa_pres.setUnits(_G)
class _Rit_riaccen_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_riaccen_Type.__name__=_B
_Rit_riaccen_Object=MibScalar
rit_riaccen=_Rit_riaccen_Object((1,3,6,1,4,1,9839,2,1,3,29),_Rit_riaccen_Type())
rit_riaccen.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_riaccen.setStatus(_A)
if mibBuilder.loadTexts:rit_riaccen.setUnits(_G)
class _Rit_tra_ins_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_tra_ins_Type.__name__=_B
_Rit_tra_ins_Object=MibScalar
rit_tra_ins=_Rit_tra_ins_Object((1,3,6,1,4,1,9839,2,1,3,30),_Rit_tra_ins_Type())
rit_tra_ins.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_tra_ins.setStatus(_A)
if mibBuilder.loadTexts:rit_tra_ins.setUnits(_G)
class _N_res_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_N_res_Type.__name__=_B
_N_res_Object=MibScalar
n_res=_N_res_Object((1,3,6,1,4,1,9839,2,1,3,31),_N_res_Type())
n_res.setMaxAccess(_E)
if mibBuilder.loadTexts:n_res.setStatus(_A)
if mibBuilder.loadTexts:n_res.setUnits(_C)
class _N_comp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_N_comp_Type.__name__=_B
_N_comp_Object=MibScalar
n_comp=_N_comp_Object((1,3,6,1,4,1,9839,2,1,3,32),_N_comp_Type())
n_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:n_comp.setStatus(_A)
if mibBuilder.loadTexts:n_comp.setUnits(_C)
class _Rit_hl_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_hl_Type.__name__=_B
_Rit_hl_Object=MibScalar
rit_hl=_Rit_hl_Object((1,3,6,1,4,1,9839,2,1,3,33),_Rit_hl_Type())
rit_hl.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_hl.setStatus(_A)
if mibBuilder.loadTexts:rit_hl.setUnits(_G)
class _Rit_resistenze_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_resistenze_Type.__name__=_B
_Rit_resistenze_Object=MibScalar
rit_resistenze=_Rit_resistenze_Object((1,3,6,1,4,1,9839,2,1,3,34),_Rit_resistenze_Type())
rit_resistenze.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_resistenze.setStatus(_A)
if mibBuilder.loadTexts:rit_resistenze.setUnits(_G)
class _Set_parz1_cw_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_parz1_cw_Type.__name__=_B
_Set_parz1_cw_Object=MibScalar
set_parz1_cw=_Set_parz1_cw_Object((1,3,6,1,4,1,9839,2,1,3,38),_Set_parz1_cw_Type())
set_parz1_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:set_parz1_cw.setStatus(_A)
if mibBuilder.loadTexts:set_parz1_cw.setUnits(_F)
class _Ist_parz1_cw_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_parz1_cw_Type.__name__=_B
_Ist_parz1_cw_Object=MibScalar
ist_parz1_cw=_Ist_parz1_cw_Object((1,3,6,1,4,1,9839,2,1,3,39),_Ist_parz1_cw_Type())
ist_parz1_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_parz1_cw.setStatus(_A)
if mibBuilder.loadTexts:ist_parz1_cw.setUnits(_F)
class _Set_parz2_cw_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_parz2_cw_Type.__name__=_B
_Set_parz2_cw_Object=MibScalar
set_parz2_cw=_Set_parz2_cw_Object((1,3,6,1,4,1,9839,2,1,3,40),_Set_parz2_cw_Type())
set_parz2_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:set_parz2_cw.setStatus(_A)
if mibBuilder.loadTexts:set_parz2_cw.setUnits(_F)
class _Ist_parz2_cw_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_parz2_cw_Type.__name__=_B
_Ist_parz2_cw_Object=MibScalar
ist_parz2_cw=_Ist_parz2_cw_Object((1,3,6,1,4,1,9839,2,1,3,41),_Ist_parz2_cw_Type())
ist_parz2_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_parz2_cw.setStatus(_A)
if mibBuilder.loadTexts:ist_parz2_cw.setUnits(_F)
class _Set_parz1_es_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_parz1_es_Type.__name__=_B
_Set_parz1_es_Object=MibScalar
set_parz1_es=_Set_parz1_es_Object((1,3,6,1,4,1,9839,2,1,3,44),_Set_parz1_es_Type())
set_parz1_es.setMaxAccess(_E)
if mibBuilder.loadTexts:set_parz1_es.setStatus(_A)
if mibBuilder.loadTexts:set_parz1_es.setUnits(_F)
class _Ist_parz1_es_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_parz1_es_Type.__name__=_B
_Ist_parz1_es_Object=MibScalar
ist_parz1_es=_Ist_parz1_es_Object((1,3,6,1,4,1,9839,2,1,3,45),_Ist_parz1_es_Type())
ist_parz1_es.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_parz1_es.setStatus(_A)
if mibBuilder.loadTexts:ist_parz1_es.setUnits(_F)
class _Set_parz2_es_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Set_parz2_es_Type.__name__=_B
_Set_parz2_es_Object=MibScalar
set_parz2_es=_Set_parz2_es_Object((1,3,6,1,4,1,9839,2,1,3,46),_Set_parz2_es_Type())
set_parz2_es.setMaxAccess(_E)
if mibBuilder.loadTexts:set_parz2_es.setStatus(_A)
if mibBuilder.loadTexts:set_parz2_es.setUnits(_F)
class _Ist_parz2_es_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ist_parz2_es_Type.__name__=_B
_Ist_parz2_es_Object=MibScalar
ist_parz2_es=_Ist_parz2_es_Object((1,3,6,1,4,1,9839,2,1,3,47),_Ist_parz2_es_Type())
ist_parz2_es.setMaxAccess(_E)
if mibBuilder.loadTexts:ist_parz2_es.setStatus(_A)
if mibBuilder.loadTexts:ist_parz2_es.setUnits(_F)
class _T_int_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_T_int_Type.__name__=_B
_T_int_Object=MibScalar
t_int=_T_int_Object((1,3,6,1,4,1,9839,2,1,3,48),_T_int_Type())
t_int.setMaxAccess(_E)
if mibBuilder.loadTexts:t_int.setStatus(_A)
if mibBuilder.loadTexts:t_int.setUnits(_G)
class _Sgl_ore_mac_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Sgl_ore_mac_Type.__name__=_B
_Sgl_ore_mac_Object=MibScalar
sgl_ore_mac=_Sgl_ore_mac_Object((1,3,6,1,4,1,9839,2,1,3,50),_Sgl_ore_mac_Type())
sgl_ore_mac.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_ore_mac.setStatus(_A)
if mibBuilder.loadTexts:sgl_ore_mac.setUnits(_G)
class _Sgl_ore_comp1_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Sgl_ore_comp1_Type.__name__=_B
_Sgl_ore_comp1_Object=MibScalar
sgl_ore_comp1=_Sgl_ore_comp1_Object((1,3,6,1,4,1,9839,2,1,3,51),_Sgl_ore_comp1_Type())
sgl_ore_comp1.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_ore_comp1.setStatus(_A)
if mibBuilder.loadTexts:sgl_ore_comp1.setUnits(_G)
class _Sgl_ore_comp2_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Sgl_ore_comp2_Type.__name__=_B
_Sgl_ore_comp2_Object=MibScalar
sgl_ore_comp2=_Sgl_ore_comp2_Object((1,3,6,1,4,1,9839,2,1,3,52),_Sgl_ore_comp2_Type())
sgl_ore_comp2.setMaxAccess(_E)
if mibBuilder.loadTexts:sgl_ore_comp2.setStatus(_A)
if mibBuilder.loadTexts:sgl_ore_comp2.setUnits(_G)
class _In_rampa_p3v_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_In_rampa_p3v_Type.__name__=_B
_In_rampa_p3v_Object=MibScalar
in_rampa_p3v=_In_rampa_p3v_Object((1,3,6,1,4,1,9839,2,1,3,54),_In_rampa_p3v_Type())
in_rampa_p3v.setMaxAccess(_E)
if mibBuilder.loadTexts:in_rampa_p3v.setStatus(_A)
if mibBuilder.loadTexts:in_rampa_p3v.setUnits(_F)
class _Fin_rampa_p3v_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fin_rampa_p3v_Type.__name__=_B
_Fin_rampa_p3v_Object=MibScalar
fin_rampa_p3v=_Fin_rampa_p3v_Object((1,3,6,1,4,1,9839,2,1,3,55),_Fin_rampa_p3v_Type())
fin_rampa_p3v.setMaxAccess(_E)
if mibBuilder.loadTexts:fin_rampa_p3v.setStatus(_A)
if mibBuilder.loadTexts:fin_rampa_p3v.setUnits(_F)
class _In_rampa_n3v_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_In_rampa_n3v_Type.__name__=_B
_In_rampa_n3v_Object=MibScalar
in_rampa_n3v=_In_rampa_n3v_Object((1,3,6,1,4,1,9839,2,1,3,56),_In_rampa_n3v_Type())
in_rampa_n3v.setMaxAccess(_E)
if mibBuilder.loadTexts:in_rampa_n3v.setStatus(_A)
if mibBuilder.loadTexts:in_rampa_n3v.setUnits(_F)
class _Fin_rampa_n3v_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fin_rampa_n3v_Type.__name__=_B
_Fin_rampa_n3v_Object=MibScalar
fin_rampa_n3v=_Fin_rampa_n3v_Object((1,3,6,1,4,1,9839,2,1,3,57),_Fin_rampa_n3v_Type())
fin_rampa_n3v.setMaxAccess(_E)
if mibBuilder.loadTexts:fin_rampa_n3v.setStatus(_A)
if mibBuilder.loadTexts:fin_rampa_n3v.setUnits(_F)
class _Tempo_run_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Tempo_run_Type.__name__=_B
_Tempo_run_Object=MibScalar
tempo_run=_Tempo_run_Object((1,3,6,1,4,1,9839,2,1,3,58),_Tempo_run_Type())
tempo_run.setMaxAccess(_E)
if mibBuilder.loadTexts:tempo_run.setStatus(_A)
if mibBuilder.loadTexts:tempo_run.setUnits(_G)
class _Rit_syson_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Rit_syson_Type.__name__=_B
_Rit_syson_Object=MibScalar
rit_syson=_Rit_syson_Object((1,3,6,1,4,1,9839,2,1,3,59),_Rit_syson_Type())
rit_syson.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_syson.setStatus(_A)
if mibBuilder.loadTexts:rit_syson.setUnits(_G)
class _Vr1cen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Vr1cen_Type.__name__=_B
_Vr1cen_Object=MibScalar
vr1cen=_Vr1cen_Object((1,3,6,1,4,1,9839,2,1,3,61),_Vr1cen_Type())
vr1cen.setMaxAccess(_D)
if mibBuilder.loadTexts:vr1cen.setStatus(_A)
if mibBuilder.loadTexts:vr1cen.setUnits(_C)
class _Vr2cen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Vr2cen_Type.__name__=_B
_Vr2cen_Object=MibScalar
vr2cen=_Vr2cen_Object((1,3,6,1,4,1,9839,2,1,3,62),_Vr2cen_Type())
vr2cen.setMaxAccess(_D)
if mibBuilder.loadTexts:vr2cen.setStatus(_A)
if mibBuilder.loadTexts:vr2cen.setUnits(_C)
class _Ore_mac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ore_mac_Type.__name__=_B
_Ore_mac_Object=MibScalar
ore_mac=_Ore_mac_Object((1,3,6,1,4,1,9839,2,1,3,63),_Ore_mac_Type())
ore_mac.setMaxAccess(_D)
if mibBuilder.loadTexts:ore_mac.setStatus(_A)
if mibBuilder.loadTexts:ore_mac.setUnits(_C)
class _Ore_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ore_comp1_Type.__name__=_B
_Ore_comp1_Object=MibScalar
ore_comp1=_Ore_comp1_Object((1,3,6,1,4,1,9839,2,1,3,65),_Ore_comp1_Type())
ore_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:ore_comp1.setStatus(_A)
if mibBuilder.loadTexts:ore_comp1.setUnits(_C)
class _Ore_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ore_comp2_Type.__name__=_B
_Ore_comp2_Object=MibScalar
ore_comp2=_Ore_comp2_Object((1,3,6,1,4,1,9839,2,1,3,66),_Ore_comp2_Type())
ore_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:ore_comp2.setStatus(_A)
if mibBuilder.loadTexts:ore_comp2.setUnits(_C)
class _X_h_main_fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_X_h_main_fan_Type.__name__=_B
_X_h_main_fan_Object=MibScalar
x_h_main_fan=_X_h_main_fan_Object((1,3,6,1,4,1,9839,2,1,3,67),_X_h_main_fan_Type())
x_h_main_fan.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_main_fan.setStatus(_A)
if mibBuilder.loadTexts:x_h_main_fan.setUnits(_C)
class _X_h_valve_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_X_h_valve_comp1_Type.__name__=_B
_X_h_valve_comp1_Object=MibScalar
x_h_valve_comp1=_X_h_valve_comp1_Object((1,3,6,1,4,1,9839,2,1,3,68),_X_h_valve_comp1_Type())
x_h_valve_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_valve_comp1.setStatus(_A)
if mibBuilder.loadTexts:x_h_valve_comp1.setUnits(_C)
class _X_h_valve_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_X_h_valve_comp2_Type.__name__=_B
_X_h_valve_comp2_Object=MibScalar
x_h_valve_comp2=_X_h_valve_comp2_Object((1,3,6,1,4,1,9839,2,1,3,69),_X_h_valve_comp2_Type())
x_h_valve_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_valve_comp2.setStatus(_A)
if mibBuilder.loadTexts:x_h_valve_comp2.setUnits(_C)
mibBuilder.exportSymbols('CAREL-cdz_pco-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'cdz_pcoMIB':cdz_pcoMIB,'digitalObjects':digitalObjects,'z1':z1,'z3':z3,'z4':z4,'z5':z5,'z6':z6,'z7':z7,'onr':onr,'z9':z9,'z10':z10,'z12':z12,'val_par':val_par,'syson2':syson2,'val_es_ok':val_es_ok,'umidifica':umidifica,'parz1':parz1,'parz2':parz2,'valfre':valfre,'valfre1':valfre1,'valca':valca,'valca1':valca1,'glb_al':glb_al,'s_firmanook':s_firmanook,'s_error_io':s_error_io,'s_bp1':s_bp1,'s_bp2':s_bp2,'s_fl1':s_fl1,'s_trf':s_trf,'s_trs1':s_trs1,'s_trs2':s_trs2,'s_fsa':s_fsa,'s_flt':s_flt,'s_all_h_temp':s_all_h_temp,'s_all_l_temp':s_all_l_temp,'s_all_h_umid':s_all_h_umid,'s_all_l_umid':s_all_l_umid,'s_al_ore_comp1':s_al_ore_comp1,'s_al_ore_comp2':s_al_ore_comp2,'s_al_ore_umidif':s_al_ore_umidif,'s_al_ore_mac':s_al_ore_mac,'s_al_ore_res1':s_al_ore_res1,'s_al_ore_res2':s_al_ore_res2,'s_all_h_free':s_all_h_free,'s_all_l_free':s_all_l_free,'s_sonda1_ko':s_sonda1_ko,'s_sonda2_ko':s_sonda2_ko,'s_sonda4_ko':s_sonda4_ko,'s_sonda6_ko':s_sonda6_ko,'s_sondau_ko':s_sondau_ko,'s_epromnook':s_epromnook,'pro_pi':pro_pi,'si_sond_umid':si_sond_umid,'si_sond_acqua':si_sond_acqua,'si_sond_aria':si_sond_aria,'si_sond_acquain':si_sond_acquain,'si_sond_ariain':si_sond_ariain,'bin_sta':bin_sta,'si_rampap':si_rampap,'es':es,'si_comp_es':si_comp_es,'si_rampan':si_rampan,'si_parz':si_parz,'si_rot2':si_rot2,'si_comp1_deu':si_comp1_deu,'si_comp2_deu':si_comp2_deu,'si_fasce':si_fasce,'syson':syson,'si_rampap3v':si_rampap3v,'si_rampan3v':si_rampan3v,'manuale':manuale,'start_off':start_off,'alarm_e06':alarm_e06,'alarm_e08':alarm_e08,'alarm_e09':alarm_e09,'alarm_e10':alarm_e10,'alarm_e11':alarm_e11,'alarm_e12':alarm_e12,'analogObjects':analogObjects,'temp':temp,'umid':umid,'acqua':acqua,'aria_acqua_in':aria_acqua_in,'temp_aria_man':temp_aria_man,'zona_morta':zona_morta,'banda_hum':banda_hum,'set_hum_a':set_hum_a,'sgl_l_temp':sgl_l_temp,'sgl_h_temp':sgl_h_temp,'sgl_l_umid':sgl_l_umid,'sgl_h_umid':sgl_h_umid,'set_temp_a':set_temp_a,'banda_temp':banda_temp,'sgl_l_free':sgl_l_free,'sgl_h_free':sgl_h_free,'integerObjects':integerObjects,'in_rampa_p':in_rampa_p,'fin_rampa_p':fin_rampa_p,'in_rampa_n':in_rampa_n,'fin_rampa_n':fin_rampa_n,'set_comp1_cw':set_comp1_cw,'ist_comp1_cw':ist_comp1_cw,'set_comp2_cw':set_comp2_cw,'ist_comp2_cw':ist_comp2_cw,'set_comp1_es':set_comp1_es,'ist_comp1_es':ist_comp1_es,'set_comp2_es':set_comp2_es,'ist_comp2_es':ist_comp2_es,'rit_fra_ins':rit_fra_ins,'rit_bassa_pres':rit_bassa_pres,'rit_riaccen':rit_riaccen,'rit_tra_ins':rit_tra_ins,'n_res':n_res,'n_comp':n_comp,'rit_hl':rit_hl,'rit_resistenze':rit_resistenze,'set_parz1_cw':set_parz1_cw,'ist_parz1_cw':ist_parz1_cw,'set_parz2_cw':set_parz2_cw,'ist_parz2_cw':ist_parz2_cw,'set_parz1_es':set_parz1_es,'ist_parz1_es':ist_parz1_es,'set_parz2_es':set_parz2_es,'ist_parz2_es':ist_parz2_es,'t_int':t_int,'sgl_ore_mac':sgl_ore_mac,'sgl_ore_comp1':sgl_ore_comp1,'sgl_ore_comp2':sgl_ore_comp2,'in_rampa_p3v':in_rampa_p3v,'fin_rampa_p3v':fin_rampa_p3v,'in_rampa_n3v':in_rampa_n3v,'fin_rampa_n3v':fin_rampa_n3v,'tempo_run':tempo_run,'rit_syson':rit_syson,'vr1cen':vr1cen,'vr2cen':vr2cen,'ore_mac':ore_mac,'ore_comp1':ore_comp1,'ore_comp2':ore_comp2,'x_h_main_fan':x_h_main_fan,'x_h_valve_comp1':x_h_valve_comp1,'x_h_valve_comp2':x_h_valve_comp2})