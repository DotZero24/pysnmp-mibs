_I='min'
_H='kh x10'
_G='s'
_F='read-only'
_E='C x10'
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
ariaMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_F)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_D)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_F)
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
unit1_Type.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_D)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_D)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_D)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_D)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_D)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_D)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_D)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_D)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_D)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Id1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Id1_Type.__name__=_B
_Id1_Object=MibScalar
id1=_Id1_Object((1,3,6,1,4,1,9839,2,1,1,1),_Id1_Type())
id1.setMaxAccess(_F)
if mibBuilder.loadTexts:id1.setStatus(_A)
if mibBuilder.loadTexts:id1.setUnits(_D)
class _Id2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Id2_Type.__name__=_B
_Id2_Object=MibScalar
id2=_Id2_Object((1,3,6,1,4,1,9839,2,1,1,2),_Id2_Type())
id2.setMaxAccess(_F)
if mibBuilder.loadTexts:id2.setStatus(_A)
if mibBuilder.loadTexts:id2.setUnits(_D)
class _Id3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Id3_Type.__name__=_B
_Id3_Object=MibScalar
id3=_Id3_Object((1,3,6,1,4,1,9839,2,1,1,3),_Id3_Type())
id3.setMaxAccess(_F)
if mibBuilder.loadTexts:id3.setStatus(_A)
if mibBuilder.loadTexts:id3.setUnits(_D)
class _Reset_allarmi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Reset_allarmi_Type.__name__=_B
_Reset_allarmi_Object=MibScalar
reset_allarmi=_Reset_allarmi_Object((1,3,6,1,4,1,9839,2,1,1,4),_Reset_allarmi_Type())
reset_allarmi.setMaxAccess(_C)
if mibBuilder.loadTexts:reset_allarmi.setStatus(_A)
if mibBuilder.loadTexts:reset_allarmi.setUnits(_D)
class _Reset_hardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Reset_hardware_Type.__name__=_B
_Reset_hardware_Object=MibScalar
reset_hardware=_Reset_hardware_Object((1,3,6,1,4,1,9839,2,1,1,5),_Reset_hardware_Type())
reset_hardware.setMaxAccess(_C)
if mibBuilder.loadTexts:reset_hardware.setStatus(_A)
if mibBuilder.loadTexts:reset_hardware.setUnits(_D)
class _Forza_invio_parametri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Forza_invio_parametri_Type.__name__=_B
_Forza_invio_parametri_Object=MibScalar
forza_invio_parametri=_Forza_invio_parametri_Object((1,3,6,1,4,1,9839,2,1,1,6),_Forza_invio_parametri_Type())
forza_invio_parametri.setMaxAccess(_C)
if mibBuilder.loadTexts:forza_invio_parametri.setStatus(_A)
if mibBuilder.loadTexts:forza_invio_parametri.setUnits(_D)
class _Stato_uscite_remoto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_uscite_remoto_Type.__name__=_B
_Stato_uscite_remoto_Object=MibScalar
stato_uscite_remoto=_Stato_uscite_remoto_Object((1,3,6,1,4,1,9839,2,1,1,7),_Stato_uscite_remoto_Type())
stato_uscite_remoto.setMaxAccess(_C)
if mibBuilder.loadTexts:stato_uscite_remoto.setStatus(_A)
if mibBuilder.loadTexts:stato_uscite_remoto.setUnits(_D)
class _Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Buzzer_Type.__name__=_B
_Buzzer_Object=MibScalar
buzzer=_Buzzer_Object((1,3,6,1,4,1,9839,2,1,1,8),_Buzzer_Type())
buzzer.setMaxAccess(_C)
if mibBuilder.loadTexts:buzzer.setStatus(_A)
if mibBuilder.loadTexts:buzzer.setUnits(_D)
class _Allarme_remoto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Allarme_remoto_Type.__name__=_B
_Allarme_remoto_Object=MibScalar
allarme_remoto=_Allarme_remoto_Object((1,3,6,1,4,1,9839,2,1,1,9),_Allarme_remoto_Type())
allarme_remoto.setMaxAccess(_F)
if mibBuilder.loadTexts:allarme_remoto.setStatus(_A)
if mibBuilder.loadTexts:allarme_remoto.setUnits(_D)
class _Id1_remoto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Id1_remoto_Type.__name__=_B
_Id1_remoto_Object=MibScalar
id1_remoto=_Id1_remoto_Object((1,3,6,1,4,1,9839,2,1,1,10),_Id1_remoto_Type())
id1_remoto.setMaxAccess(_C)
if mibBuilder.loadTexts:id1_remoto.setStatus(_A)
if mibBuilder.loadTexts:id1_remoto.setUnits(_D)
class _Id2_remoto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Id2_remoto_Type.__name__=_B
_Id2_remoto_Object=MibScalar
id2_remoto=_Id2_remoto_Object((1,3,6,1,4,1,9839,2,1,1,11),_Id2_remoto_Type())
id2_remoto.setMaxAccess(_C)
if mibBuilder.loadTexts:id2_remoto.setStatus(_A)
if mibBuilder.loadTexts:id2_remoto.setUnits(_D)
class _Id3_remoto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Id3_remoto_Type.__name__=_B
_Id3_remoto_Object=MibScalar
id3_remoto=_Id3_remoto_Object((1,3,6,1,4,1,9839,2,1,1,12),_Id3_remoto_Type())
id3_remoto.setMaxAccess(_C)
if mibBuilder.loadTexts:id3_remoto.setStatus(_A)
if mibBuilder.loadTexts:id3_remoto.setUnits(_D)
class _Stato_regolazione_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_regolazione_Type.__name__=_B
_Stato_regolazione_Object=MibScalar
stato_regolazione=_Stato_regolazione_Object((1,3,6,1,4,1,9839,2,1,1,13),_Stato_regolazione_Type())
stato_regolazione.setMaxAccess(_C)
if mibBuilder.loadTexts:stato_regolazione.setStatus(_A)
if mibBuilder.loadTexts:stato_regolazione.setUnits(_D)
class _Sbrinamento_manuale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sbrinamento_manuale_Type.__name__=_B
_Sbrinamento_manuale_Object=MibScalar
sbrinamento_manuale=_Sbrinamento_manuale_Object((1,3,6,1,4,1,9839,2,1,1,14),_Sbrinamento_manuale_Type())
sbrinamento_manuale.setMaxAccess(_C)
if mibBuilder.loadTexts:sbrinamento_manuale.setStatus(_A)
if mibBuilder.loadTexts:sbrinamento_manuale.setUnits(_D)
class _Forzatura_on_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Forzatura_on_Type.__name__=_B
_Forzatura_on_Object=MibScalar
forzatura_on=_Forzatura_on_Object((1,3,6,1,4,1,9839,2,1,1,15),_Forzatura_on_Type())
forzatura_on.setMaxAccess(_C)
if mibBuilder.loadTexts:forzatura_on.setStatus(_A)
if mibBuilder.loadTexts:forzatura_on.setUnits(_D)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Sonda_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b1_Type.__name__=_B
_Sonda_b1_Object=MibScalar
sonda_b1=_Sonda_b1_Object((1,3,6,1,4,1,9839,2,1,2,1),_Sonda_b1_Type())
sonda_b1.setMaxAccess(_F)
if mibBuilder.loadTexts:sonda_b1.setStatus(_A)
if mibBuilder.loadTexts:sonda_b1.setUnits(_E)
class _Sonda_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b2_Type.__name__=_B
_Sonda_b2_Object=MibScalar
sonda_b2=_Sonda_b2_Object((1,3,6,1,4,1,9839,2,1,2,2),_Sonda_b2_Type())
sonda_b2.setMaxAccess(_F)
if mibBuilder.loadTexts:sonda_b2.setStatus(_A)
if mibBuilder.loadTexts:sonda_b2.setUnits('C / %RH x10')
class _Sonda_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b3_Type.__name__=_B
_Sonda_b3_Object=MibScalar
sonda_b3=_Sonda_b3_Object((1,3,6,1,4,1,9839,2,1,2,3),_Sonda_b3_Type())
sonda_b3.setMaxAccess(_F)
if mibBuilder.loadTexts:sonda_b3.setStatus(_A)
if mibBuilder.loadTexts:sonda_b3.setUnits(_E)
class _Setpoint_valigia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Setpoint_valigia_Type.__name__=_B
_Setpoint_valigia_Object=MibScalar
setpoint_valigia=_Setpoint_valigia_Object((1,3,6,1,4,1,9839,2,1,2,5),_Setpoint_valigia_Type())
setpoint_valigia.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_valigia.setStatus(_A)
if mibBuilder.loadTexts:setpoint_valigia.setUnits(_E)
class _Setpoint_poltrona_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Setpoint_poltrona_Type.__name__=_B
_Setpoint_poltrona_Object=MibScalar
setpoint_poltrona=_Setpoint_poltrona_Object((1,3,6,1,4,1,9839,2,1,2,6),_Setpoint_poltrona_Type())
setpoint_poltrona.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_poltrona.setStatus(_A)
if mibBuilder.loadTexts:setpoint_poltrona.setUnits(_E)
class _Setpoint_luna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Setpoint_luna_Type.__name__=_B
_Setpoint_luna_Object=MibScalar
setpoint_luna=_Setpoint_luna_Object((1,3,6,1,4,1,9839,2,1,2,7),_Setpoint_luna_Type())
setpoint_luna.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_luna.setStatus(_A)
if mibBuilder.loadTexts:setpoint_luna.setUnits(_E)
class _Diffheat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_Diffheat_Type.__name__=_B
_Diffheat_Object=MibScalar
diffheat=_Diffheat_Object((1,3,6,1,4,1,9839,2,1,2,8),_Diffheat_Type())
diffheat.setMaxAccess(_C)
if mibBuilder.loadTexts:diffheat.setStatus(_A)
if mibBuilder.loadTexts:diffheat.setUnits(_E)
class _R1_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,380))
_R1_Type.__name__=_B
_R1_Object=MibScalar
r1=_R1_Object((1,3,6,1,4,1,9839,2,1,2,21),_R1_Type())
r1.setMaxAccess(_C)
if mibBuilder.loadTexts:r1.setStatus(_A)
if mibBuilder.loadTexts:r1.setUnits(_E)
class _R8_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_R8_Type.__name__=_B
_R8_Object=MibScalar
r8=_R8_Object((1,3,6,1,4,1,9839,2,1,2,23),_R8_Type())
r8.setMaxAccess(_C)
if mibBuilder.loadTexts:r8.setStatus(_A)
if mibBuilder.loadTexts:r8.setUnits(_E)
class _R12_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_R12_Type.__name__=_B
_R12_Object=MibScalar
r12=_R12_Object((1,3,6,1,4,1,9839,2,1,2,25),_R12_Type())
r12.setMaxAccess(_C)
if mibBuilder.loadTexts:r12.setStatus(_A)
if mibBuilder.loadTexts:r12.setUnits(_E)
class _R13_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,500))
_R13_Type.__name__=_B
_R13_Object=MibScalar
r13=_R13_Object((1,3,6,1,4,1,9839,2,1,2,26),_R13_Type())
r13.setMaxAccess(_C)
if mibBuilder.loadTexts:r13.setStatus(_A)
if mibBuilder.loadTexts:r13.setUnits(_E)
class _R9_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,220))
_R9_Type.__name__=_B
_R9_Object=MibScalar
r9=_R9_Object((1,3,6,1,4,1,9839,2,1,2,30),_R9_Type())
r9.setMaxAccess(_C)
if mibBuilder.loadTexts:r9.setStatus(_A)
if mibBuilder.loadTexts:r9.setUnits(_E)
class _R2_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_R2_Type.__name__=_B
_R2_Object=MibScalar
r2=_R2_Object((1,3,6,1,4,1,9839,2,1,2,31),_R2_Type())
r2.setMaxAccess(_C)
if mibBuilder.loadTexts:r2.setStatus(_A)
if mibBuilder.loadTexts:r2.setUnits(_E)
class _R4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_R4_Type.__name__=_B
_R4_Object=MibScalar
r4=_R4_Object((1,3,6,1,4,1,9839,2,1,2,32),_R4_Type())
r4.setMaxAccess(_C)
if mibBuilder.loadTexts:r4.setStatus(_A)
if mibBuilder.loadTexts:r4.setUnits(_E)
class _C5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_C5_Type.__name__=_B
_C5_Object=MibScalar
c5=_C5_Object((1,3,6,1,4,1,9839,2,1,2,33),_C5_Type())
c5.setMaxAccess(_F)
if mibBuilder.loadTexts:c5.setStatus(_A)
if mibBuilder.loadTexts:c5.setUnits(_H)
class _C6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_C6_Type.__name__=_B
_C6_Object=MibScalar
c6=_C6_Object((1,3,6,1,4,1,9839,2,1,2,34),_C6_Type())
c6.setMaxAccess(_F)
if mibBuilder.loadTexts:c6.setStatus(_A)
if mibBuilder.loadTexts:c6.setUnits(_H)
class _F3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_F3_Type.__name__=_B
_F3_Object=MibScalar
f3=_F3_Object((1,3,6,1,4,1,9839,2,1,2,37),_F3_Type())
f3.setMaxAccess(_F)
if mibBuilder.loadTexts:f3.setStatus(_A)
if mibBuilder.loadTexts:f3.setUnits(_H)
class _C7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_C7_Type.__name__=_B
_C7_Object=MibScalar
c7=_C7_Object((1,3,6,1,4,1,9839,2,1,2,38),_C7_Type())
c7.setMaxAccess(_C)
if mibBuilder.loadTexts:c7.setStatus(_A)
if mibBuilder.loadTexts:c7.setUnits(_H)
class _F4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_F4_Type.__name__=_B
_F4_Object=MibScalar
f4=_F4_Object((1,3,6,1,4,1,9839,2,1,2,39),_F4_Type())
f4.setMaxAccess(_C)
if mibBuilder.loadTexts:f4.setStatus(_A)
if mibBuilder.loadTexts:f4.setUnits(_H)
class _P3_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,1500))
_P3_Type.__name__=_B
_P3_Object=MibScalar
p3=_P3_Object((1,3,6,1,4,1,9839,2,1,2,40),_P3_Type())
p3.setMaxAccess(_C)
if mibBuilder.loadTexts:p3.setStatus(_A)
if mibBuilder.loadTexts:p3.setUnits(_E)
class _P4_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_P4_Type.__name__=_B
_P4_Object=MibScalar
p4=_P4_Object((1,3,6,1,4,1,9839,2,1,2,41),_P4_Type())
p4.setMaxAccess(_C)
if mibBuilder.loadTexts:p4.setStatus(_A)
if mibBuilder.loadTexts:p4.setUnits(_E)
class _D3_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-300,32767))
_D3_Type.__name__=_B
_D3_Object=MibScalar
d3=_D3_Object((1,3,6,1,4,1,9839,2,1,2,44),_D3_Type())
d3.setMaxAccess(_C)
if mibBuilder.loadTexts:d3.setStatus(_A)
if mibBuilder.loadTexts:d3.setUnits(_E)
class _D4_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,500))
_D4_Type.__name__=_B
_D4_Object=MibScalar
d4=_D4_Object((1,3,6,1,4,1,9839,2,1,2,45),_D4_Type())
d4.setMaxAccess(_C)
if mibBuilder.loadTexts:d4.setStatus(_A)
if mibBuilder.loadTexts:d4.setUnits(_E)
class _D11_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_D11_Type.__name__=_B
_D11_Object=MibScalar
d11=_D11_Object((1,3,6,1,4,1,9839,2,1,2,46),_D11_Type())
d11.setMaxAccess(_C)
if mibBuilder.loadTexts:d11.setStatus(_A)
if mibBuilder.loadTexts:d11.setUnits(_E)
class _R28_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,150))
_R28_Type.__name__=_B
_R28_Object=MibScalar
r28=_R28_Object((1,3,6,1,4,1,9839,2,1,2,51),_R28_Type())
r28.setMaxAccess(_C)
if mibBuilder.loadTexts:r28.setStatus(_A)
if mibBuilder.loadTexts:r28.setUnits(_E)
class _R29_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_R29_Type.__name__=_B
_R29_Object=MibScalar
r29=_R29_Object((1,3,6,1,4,1,9839,2,1,2,52),_R29_Type())
r29.setMaxAccess(_C)
if mibBuilder.loadTexts:r29.setStatus(_A)
if mibBuilder.loadTexts:r29.setUnits(_E)
class _R23_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_R23_Type.__name__=_B
_R23_Object=MibScalar
r23=_R23_Object((1,3,6,1,4,1,9839,2,1,2,53),_R23_Type())
r23.setMaxAccess(_C)
if mibBuilder.loadTexts:r23.setStatus(_A)
if mibBuilder.loadTexts:r23.setUnits('- x10')
class _R24_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_R24_Type.__name__=_B
_R24_Object=MibScalar
r24=_R24_Object((1,3,6,1,4,1,9839,2,1,2,54),_R24_Type())
r24.setMaxAccess(_C)
if mibBuilder.loadTexts:r24.setStatus(_A)
if mibBuilder.loadTexts:r24.setUnits('- x10')
class _R25_Type(Integer32):defaultValue=-30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,0))
_R25_Type.__name__=_B
_R25_Object=MibScalar
r25=_R25_Object((1,3,6,1,4,1,9839,2,1,2,55),_R25_Type())
r25.setMaxAccess(_C)
if mibBuilder.loadTexts:r25.setStatus(_A)
if mibBuilder.loadTexts:r25.setUnits(_E)
class _R26_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_R26_Type.__name__=_B
_R26_Object=MibScalar
r26=_R26_Object((1,3,6,1,4,1,9839,2,1,2,56),_R26_Type())
r26.setMaxAccess(_C)
if mibBuilder.loadTexts:r26.setStatus(_A)
if mibBuilder.loadTexts:r26.setUnits(_E)
class _S2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1500,32767))
_S2_Type.__name__=_B
_S2_Object=MibScalar
s2=_S2_Object((1,3,6,1,4,1,9839,2,1,2,57),_S2_Type())
s2.setMaxAccess(_C)
if mibBuilder.loadTexts:s2.setStatus(_A)
if mibBuilder.loadTexts:s2.setUnits(_E)
class _S3_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,1500))
_S3_Type.__name__=_B
_S3_Object=MibScalar
s3=_S3_Object((1,3,6,1,4,1,9839,2,1,2,58),_S3_Type())
s3.setMaxAccess(_C)
if mibBuilder.loadTexts:s3.setStatus(_A)
if mibBuilder.loadTexts:s3.setUnits(_E)
class _S4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-120,120))
_S4_Type.__name__=_B
_S4_Object=MibScalar
s4=_S4_Object((1,3,6,1,4,1,9839,2,1,2,59),_S4_Type())
s4.setMaxAccess(_C)
if mibBuilder.loadTexts:s4.setStatus(_A)
if mibBuilder.loadTexts:s4.setUnits(_E)
class _S5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-120,120))
_S5_Type.__name__=_B
_S5_Object=MibScalar
s5=_S5_Object((1,3,6,1,4,1,9839,2,1,2,60),_S5_Type())
s5.setMaxAccess(_C)
if mibBuilder.loadTexts:s5.setStatus(_A)
if mibBuilder.loadTexts:s5.setUnits(_E)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Modalita_ventole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Modalita_ventole_Type.__name__=_B
_Modalita_ventole_Object=MibScalar
modalita_ventole=_Modalita_ventole_Object((1,3,6,1,4,1,9839,2,1,3,8),_Modalita_ventole_Type())
modalita_ventole.setMaxAccess(_C)
if mibBuilder.loadTexts:modalita_ventole.setStatus(_A)
if mibBuilder.loadTexts:modalita_ventole.setUnits('-')
class _S1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_S1_Type.__name__=_B
_S1_Object=MibScalar
s1=_S1_Object((1,3,6,1,4,1,9839,2,1,3,21),_S1_Type())
s1.setMaxAccess(_C)
if mibBuilder.loadTexts:s1.setStatus(_A)
if mibBuilder.loadTexts:s1.setUnits(_D)
class _S8_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S8_Type.__name__=_B
_S8_Object=MibScalar
s8=_S8_Object((1,3,6,1,4,1,9839,2,1,3,22),_S8_Type())
s8.setMaxAccess(_C)
if mibBuilder.loadTexts:s8.setStatus(_A)
if mibBuilder.loadTexts:s8.setUnits(_D)
class _S6_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_S6_Type.__name__=_B
_S6_Object=MibScalar
s6=_S6_Object((1,3,6,1,4,1,9839,2,1,3,23),_S6_Type())
s6.setMaxAccess(_C)
if mibBuilder.loadTexts:s6.setStatus(_A)
if mibBuilder.loadTexts:s6.setUnits(_D)
class _S9_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_S9_Type.__name__=_B
_S9_Object=MibScalar
s9=_S9_Object((1,3,6,1,4,1,9839,2,1,3,24),_S9_Type())
s9.setMaxAccess(_C)
if mibBuilder.loadTexts:s9.setStatus(_A)
if mibBuilder.loadTexts:s9.setUnits(_D)
class _S10_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_S10_Type.__name__=_B
_S10_Object=MibScalar
s10=_S10_Object((1,3,6,1,4,1,9839,2,1,3,25),_S10_Type())
s10.setMaxAccess(_C)
if mibBuilder.loadTexts:s10.setStatus(_A)
if mibBuilder.loadTexts:s10.setUnits(_D)
class _R19_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_R19_Type.__name__=_B
_R19_Object=MibScalar
r19=_R19_Object((1,3,6,1,4,1,9839,2,1,3,26),_R19_Type())
r19.setMaxAccess(_C)
if mibBuilder.loadTexts:r19.setStatus(_A)
if mibBuilder.loadTexts:r19.setUnits(_D)
class _R20_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,999))
_R20_Type.__name__=_B
_R20_Object=MibScalar
r20=_R20_Object((1,3,6,1,4,1,9839,2,1,3,27),_R20_Type())
r20.setMaxAccess(_C)
if mibBuilder.loadTexts:r20.setStatus(_A)
if mibBuilder.loadTexts:r20.setUnits(_G)
class _R21_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_R21_Type.__name__=_B
_R21_Object=MibScalar
r21=_R21_Object((1,3,6,1,4,1,9839,2,1,3,28),_R21_Type())
r21.setMaxAccess(_C)
if mibBuilder.loadTexts:r21.setStatus(_A)
if mibBuilder.loadTexts:r21.setUnits(_G)
class _H3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_H3_Type.__name__=_B
_H3_Object=MibScalar
h3=_H3_Object((1,3,6,1,4,1,9839,2,1,3,29),_H3_Type())
h3.setMaxAccess(_C)
if mibBuilder.loadTexts:h3.setStatus(_A)
if mibBuilder.loadTexts:h3.setUnits(_D)
class _H4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_H4_Type.__name__=_B
_H4_Object=MibScalar
h4=_H4_Object((1,3,6,1,4,1,9839,2,1,3,30),_H4_Type())
h4.setMaxAccess(_C)
if mibBuilder.loadTexts:h4.setStatus(_A)
if mibBuilder.loadTexts:h4.setUnits(_D)
class _H5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_H5_Type.__name__=_B
_H5_Object=MibScalar
h5=_H5_Object((1,3,6,1,4,1,9839,2,1,3,31),_H5_Type())
h5.setMaxAccess(_C)
if mibBuilder.loadTexts:h5.setStatus(_A)
if mibBuilder.loadTexts:h5.setUnits(_D)
class _P2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_P2_Type.__name__=_B
_P2_Object=MibScalar
p2=_P2_Object((1,3,6,1,4,1,9839,2,1,3,32),_P2_Type())
p2.setMaxAccess(_C)
if mibBuilder.loadTexts:p2.setStatus(_A)
if mibBuilder.loadTexts:p2.setUnits(_D)
class _S7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S7_Type.__name__=_B
_S7_Object=MibScalar
s7=_S7_Object((1,3,6,1,4,1,9839,2,1,3,33),_S7_Type())
s7.setMaxAccess(_C)
if mibBuilder.loadTexts:s7.setStatus(_A)
if mibBuilder.loadTexts:s7.setUnits(_D)
class _H18_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_H18_Type.__name__=_B
_H18_Object=MibScalar
h18=_H18_Object((1,3,6,1,4,1,9839,2,1,3,35),_H18_Type())
h18.setMaxAccess(_C)
if mibBuilder.loadTexts:h18.setStatus(_A)
if mibBuilder.loadTexts:h18.setUnits(_D)
class _C1_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_C1_Type.__name__=_B
_C1_Object=MibScalar
c1=_C1_Object((1,3,6,1,4,1,9839,2,1,3,36),_C1_Type())
c1.setMaxAccess(_C)
if mibBuilder.loadTexts:c1.setStatus(_A)
if mibBuilder.loadTexts:c1.setUnits(_G)
class _C2_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_C2_Type.__name__=_B
_C2_Object=MibScalar
c2=_C2_Object((1,3,6,1,4,1,9839,2,1,3,37),_C2_Type())
c2.setMaxAccess(_C)
if mibBuilder.loadTexts:c2.setStatus(_A)
if mibBuilder.loadTexts:c2.setUnits(_G)
class _C3_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_C3_Type.__name__=_B
_C3_Object=MibScalar
c3=_C3_Object((1,3,6,1,4,1,9839,2,1,3,38),_C3_Type())
c3.setMaxAccess(_C)
if mibBuilder.loadTexts:c3.setStatus(_A)
if mibBuilder.loadTexts:c3.setUnits(_G)
class _C4_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_C4_Type.__name__=_B
_C4_Object=MibScalar
c4=_C4_Object((1,3,6,1,4,1,9839,2,1,3,39),_C4_Type())
c4.setMaxAccess(_C)
if mibBuilder.loadTexts:c4.setStatus(_A)
if mibBuilder.loadTexts:c4.setUnits(_G)
class _C8_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_C8_Type.__name__=_B
_C8_Object=MibScalar
c8=_C8_Object((1,3,6,1,4,1,9839,2,1,3,40),_C8_Type())
c8.setMaxAccess(_C)
if mibBuilder.loadTexts:c8.setStatus(_A)
if mibBuilder.loadTexts:c8.setUnits(_D)
class _F1_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_F1_Type.__name__=_B
_F1_Object=MibScalar
f1=_F1_Object((1,3,6,1,4,1,9839,2,1,3,41),_F1_Type())
f1.setMaxAccess(_C)
if mibBuilder.loadTexts:f1.setStatus(_A)
if mibBuilder.loadTexts:f1.setUnits(_G)
class _F2_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_F2_Type.__name__=_B
_F2_Object=MibScalar
f2=_F2_Object((1,3,6,1,4,1,9839,2,1,3,42),_F2_Type())
f2.setMaxAccess(_C)
if mibBuilder.loadTexts:f2.setStatus(_A)
if mibBuilder.loadTexts:f2.setUnits(_G)
class _F6_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_F6_Type.__name__=_B
_F6_Object=MibScalar
f6=_F6_Object((1,3,6,1,4,1,9839,2,1,3,43),_F6_Type())
f6.setMaxAccess(_C)
if mibBuilder.loadTexts:f6.setStatus(_A)
if mibBuilder.loadTexts:f6.setUnits(_G)
class _F14_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_F14_Type.__name__=_B
_F14_Object=MibScalar
f14=_F14_Object((1,3,6,1,4,1,9839,2,1,3,46),_F14_Type())
f14.setMaxAccess(_C)
if mibBuilder.loadTexts:f14.setStatus(_A)
if mibBuilder.loadTexts:f14.setUnits(_I)
class _F15_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_F15_Type.__name__=_B
_F15_Object=MibScalar
f15=_F15_Object((1,3,6,1,4,1,9839,2,1,3,47),_F15_Type())
f15.setMaxAccess(_C)
if mibBuilder.loadTexts:f15.setStatus(_A)
if mibBuilder.loadTexts:f15.setUnits(_I)
class _R18_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_R18_Type.__name__=_B
_R18_Object=MibScalar
r18=_R18_Object((1,3,6,1,4,1,9839,2,1,3,48),_R18_Type())
r18.setMaxAccess(_C)
if mibBuilder.loadTexts:r18.setStatus(_A)
if mibBuilder.loadTexts:r18.setUnits(_D)
class _R10_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_R10_Type.__name__=_B
_R10_Object=MibScalar
r10=_R10_Object((1,3,6,1,4,1,9839,2,1,3,49),_R10_Type())
r10.setMaxAccess(_C)
if mibBuilder.loadTexts:r10.setStatus(_A)
if mibBuilder.loadTexts:r10.setUnits(_D)
class _R11_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_R11_Type.__name__=_B
_R11_Object=MibScalar
r11=_R11_Object((1,3,6,1,4,1,9839,2,1,3,50),_R11_Type())
r11.setMaxAccess(_C)
if mibBuilder.loadTexts:r11.setStatus(_A)
if mibBuilder.loadTexts:r11.setUnits(_D)
class _F7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_F7_Type.__name__=_B
_F7_Object=MibScalar
f7=_F7_Object((1,3,6,1,4,1,9839,2,1,3,51),_F7_Type())
f7.setMaxAccess(_C)
if mibBuilder.loadTexts:f7.setStatus(_A)
if mibBuilder.loadTexts:f7.setUnits(_D)
class _P5_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_P5_Type.__name__=_B
_P5_Object=MibScalar
p5=_P5_Object((1,3,6,1,4,1,9839,2,1,3,52),_P5_Type())
p5.setMaxAccess(_C)
if mibBuilder.loadTexts:p5.setStatus(_A)
if mibBuilder.loadTexts:p5.setUnits(_I)
class _P9_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_P9_Type.__name__=_B
_P9_Object=MibScalar
p9=_P9_Object((1,3,6,1,4,1,9839,2,1,3,53),_P9_Type())
p9.setMaxAccess(_C)
if mibBuilder.loadTexts:p9.setStatus(_A)
if mibBuilder.loadTexts:p9.setUnits(_D)
class _P10_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_P10_Type.__name__=_B
_P10_Object=MibScalar
p10=_P10_Object((1,3,6,1,4,1,9839,2,1,3,54),_P10_Type())
p10.setMaxAccess(_C)
if mibBuilder.loadTexts:p10.setStatus(_A)
if mibBuilder.loadTexts:p10.setUnits(_D)
class _P11_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_P11_Type.__name__=_B
_P11_Object=MibScalar
p11=_P11_Object((1,3,6,1,4,1,9839,2,1,3,55),_P11_Type())
p11.setMaxAccess(_C)
if mibBuilder.loadTexts:p11.setStatus(_A)
if mibBuilder.loadTexts:p11.setUnits(_D)
class _P6_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_P6_Type.__name__=_B
_P6_Object=MibScalar
p6=_P6_Object((1,3,6,1,4,1,9839,2,1,3,56),_P6_Type())
p6.setMaxAccess(_C)
if mibBuilder.loadTexts:p6.setStatus(_A)
if mibBuilder.loadTexts:p6.setUnits(_G)
class _H7_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_H7_Type.__name__=_B
_H7_Object=MibScalar
h7=_H7_Object((1,3,6,1,4,1,9839,2,1,3,57),_H7_Type())
h7.setMaxAccess(_C)
if mibBuilder.loadTexts:h7.setStatus(_A)
if mibBuilder.loadTexts:h7.setUnits(_D)
class _H13_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_H13_Type.__name__=_B
_H13_Object=MibScalar
h13=_H13_Object((1,3,6,1,4,1,9839,2,1,3,59),_H13_Type())
h13.setMaxAccess(_C)
if mibBuilder.loadTexts:h13.setStatus(_A)
if mibBuilder.loadTexts:h13.setUnits(_D)
class _H6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_H6_Type.__name__=_B
_H6_Object=MibScalar
h6=_H6_Object((1,3,6,1,4,1,9839,2,1,3,60),_H6_Type())
h6.setMaxAccess(_C)
if mibBuilder.loadTexts:h6.setStatus(_A)
if mibBuilder.loadTexts:h6.setUnits(_D)
class _H10_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-25,25))
_H10_Type.__name__=_B
_H10_Object=MibScalar
h10=_H10_Object((1,3,6,1,4,1,9839,2,1,3,61),_H10_Type())
h10.setMaxAccess(_C)
if mibBuilder.loadTexts:h10.setStatus(_A)
if mibBuilder.loadTexts:h10.setUnits(_D)
class _H1_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_H1_Type.__name__=_B
_H1_Object=MibScalar
h1=_H1_Object((1,3,6,1,4,1,9839,2,1,3,67),_H1_Type())
h1.setMaxAccess(_C)
if mibBuilder.loadTexts:h1.setStatus(_A)
if mibBuilder.loadTexts:h1.setUnits(_D)
class _H2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_H2_Type.__name__=_B
_H2_Object=MibScalar
h2=_H2_Object((1,3,6,1,4,1,9839,2,1,3,68),_H2_Type())
h2.setMaxAccess(_C)
if mibBuilder.loadTexts:h2.setStatus(_A)
if mibBuilder.loadTexts:h2.setUnits(_D)
class _F5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_F5_Type.__name__=_B
_F5_Object=MibScalar
f5=_F5_Object((1,3,6,1,4,1,9839,2,1,3,70),_F5_Type())
f5.setMaxAccess(_C)
if mibBuilder.loadTexts:f5.setStatus(_A)
if mibBuilder.loadTexts:f5.setUnits(_D)
class _D1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_D1_Type.__name__=_B
_D1_Object=MibScalar
d1=_D1_Object((1,3,6,1,4,1,9839,2,1,3,71),_D1_Type())
d1.setMaxAccess(_C)
if mibBuilder.loadTexts:d1.setStatus(_A)
if mibBuilder.loadTexts:d1.setUnits(_D)
class _D2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_D2_Type.__name__=_B
_D2_Object=MibScalar
d2=_D2_Object((1,3,6,1,4,1,9839,2,1,3,72),_D2_Type())
d2.setMaxAccess(_C)
if mibBuilder.loadTexts:d2.setStatus(_A)
if mibBuilder.loadTexts:d2.setUnits(_D)
class _D5_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_D5_Type.__name__=_B
_D5_Object=MibScalar
d5=_D5_Object((1,3,6,1,4,1,9839,2,1,3,73),_D5_Type())
d5.setMaxAccess(_C)
if mibBuilder.loadTexts:d5.setStatus(_A)
if mibBuilder.loadTexts:d5.setUnits(_G)
class _D6_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_D6_Type.__name__=_B
_D6_Object=MibScalar
d6=_D6_Object((1,3,6,1,4,1,9839,2,1,3,74),_D6_Type())
d6.setMaxAccess(_C)
if mibBuilder.loadTexts:d6.setStatus(_A)
if mibBuilder.loadTexts:d6.setUnits(_G)
class _D7_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,180))
_D7_Type.__name__=_B
_D7_Object=MibScalar
d7=_D7_Object((1,3,6,1,4,1,9839,2,1,3,75),_D7_Type())
d7.setMaxAccess(_C)
if mibBuilder.loadTexts:d7.setStatus(_A)
if mibBuilder.loadTexts:d7.setUnits(_I)
class _D8_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_D8_Type.__name__=_B
_D8_Object=MibScalar
d8=_D8_Object((1,3,6,1,4,1,9839,2,1,3,76),_D8_Type())
d8.setMaxAccess(_C)
if mibBuilder.loadTexts:d8.setStatus(_A)
if mibBuilder.loadTexts:d8.setUnits(_D)
class _D9_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_D9_Type.__name__=_B
_D9_Object=MibScalar
d9=_D9_Object((1,3,6,1,4,1,9839,2,1,3,77),_D9_Type())
d9.setMaxAccess(_C)
if mibBuilder.loadTexts:d9.setStatus(_A)
if mibBuilder.loadTexts:d9.setUnits(_D)
class _D10_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_D10_Type.__name__=_B
_D10_Object=MibScalar
d10=_D10_Object((1,3,6,1,4,1,9839,2,1,3,78),_D10_Type())
d10.setMaxAccess(_C)
if mibBuilder.loadTexts:d10.setStatus(_A)
if mibBuilder.loadTexts:d10.setUnits(_G)
class _D12_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,36))
_D12_Type.__name__=_B
_D12_Object=MibScalar
d12=_D12_Object((1,3,6,1,4,1,9839,2,1,3,79),_D12_Type())
d12.setMaxAccess(_C)
if mibBuilder.loadTexts:d12.setStatus(_A)
if mibBuilder.loadTexts:d12.setUnits(_I)
class _D13_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_D13_Type.__name__=_B
_D13_Object=MibScalar
d13=_D13_Object((1,3,6,1,4,1,9839,2,1,3,80),_D13_Type())
d13.setMaxAccess(_C)
if mibBuilder.loadTexts:d13.setStatus(_A)
if mibBuilder.loadTexts:d13.setUnits(_D)
class _R27_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_R27_Type.__name__=_B
_R27_Object=MibScalar
r27=_R27_Object((1,3,6,1,4,1,9839,2,1,3,83),_R27_Type())
r27.setMaxAccess(_C)
if mibBuilder.loadTexts:r27.setStatus(_A)
if mibBuilder.loadTexts:r27.setUnits(_D)
class _L4_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_L4_Type.__name__=_B
_L4_Object=MibScalar
l4=_L4_Object((1,3,6,1,4,1,9839,2,1,3,84),_L4_Type())
l4.setMaxAccess(_C)
if mibBuilder.loadTexts:l4.setStatus(_A)
if mibBuilder.loadTexts:l4.setUnits(_G)
class _H16_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_H16_Type.__name__=_B
_H16_Object=MibScalar
h16=_H16_Object((1,3,6,1,4,1,9839,2,1,3,85),_H16_Type())
h16.setMaxAccess(_C)
if mibBuilder.loadTexts:h16.setStatus(_A)
if mibBuilder.loadTexts:h16.setUnits(_D)
class _P12_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_P12_Type.__name__=_B
_P12_Object=MibScalar
p12=_P12_Object((1,3,6,1,4,1,9839,2,1,3,86),_P12_Type())
p12.setMaxAccess(_C)
if mibBuilder.loadTexts:p12.setStatus(_A)
if mibBuilder.loadTexts:p12.setUnits(_D)
class _L1_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_L1_Type.__name__=_B
_L1_Object=MibScalar
l1=_L1_Object((1,3,6,1,4,1,9839,2,1,3,87),_L1_Type())
l1.setMaxAccess(_F)
if mibBuilder.loadTexts:l1.setStatus(_A)
if mibBuilder.loadTexts:l1.setUnits(_D)
class _L2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L2_Type.__name__=_B
_L2_Object=MibScalar
l2=_L2_Object((1,3,6,1,4,1,9839,2,1,3,88),_L2_Type())
l2.setMaxAccess(_C)
if mibBuilder.loadTexts:l2.setStatus(_A)
if mibBuilder.loadTexts:l2.setUnits(_D)
class _L3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L3_Type.__name__=_B
_L3_Object=MibScalar
l3=_L3_Object((1,3,6,1,4,1,9839,2,1,3,89),_L3_Type())
l3.setMaxAccess(_C)
if mibBuilder.loadTexts:l3.setStatus(_A)
if mibBuilder.loadTexts:l3.setUnits(_D)
class _L5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_L5_Type.__name__=_B
_L5_Object=MibScalar
l5=_L5_Object((1,3,6,1,4,1,9839,2,1,3,90),_L5_Type())
l5.setMaxAccess(_C)
if mibBuilder.loadTexts:l5.setStatus(_A)
if mibBuilder.loadTexts:l5.setUnits(_D)
class _R14_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_R14_Type.__name__=_B
_R14_Object=MibScalar
r14=_R14_Object((1,3,6,1,4,1,9839,2,1,3,91),_R14_Type())
r14.setMaxAccess(_C)
if mibBuilder.loadTexts:r14.setStatus(_A)
if mibBuilder.loadTexts:r14.setUnits(_D)
mibBuilder.exportSymbols('CAREL-aria-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'ariaMIB':ariaMIB,'digitalObjects':digitalObjects,'id1':id1,'id2':id2,'id3':id3,'reset_allarmi':reset_allarmi,'reset_hardware':reset_hardware,'forza_invio_parametri':forza_invio_parametri,'stato_uscite_remoto':stato_uscite_remoto,'buzzer':buzzer,'allarme_remoto':allarme_remoto,'id1_remoto':id1_remoto,'id2_remoto':id2_remoto,'id3_remoto':id3_remoto,'stato_regolazione':stato_regolazione,'sbrinamento_manuale':sbrinamento_manuale,'forzatura_on':forzatura_on,'analogObjects':analogObjects,'sonda_b1':sonda_b1,'sonda_b2':sonda_b2,'sonda_b3':sonda_b3,'setpoint_valigia':setpoint_valigia,'setpoint_poltrona':setpoint_poltrona,'setpoint_luna':setpoint_luna,'diffheat':diffheat,'r1':r1,'r8':r8,'r12':r12,'r13':r13,'r9':r9,'r2':r2,'r4':r4,'c5':c5,'c6':c6,'f3':f3,'c7':c7,'f4':f4,'p3':p3,'p4':p4,'d3':d3,'d4':d4,'d11':d11,'r28':r28,'r29':r29,'r23':r23,'r24':r24,'r25':r25,'r26':r26,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'integerObjects':integerObjects,'modalita_ventole':modalita_ventole,'s1':s1,'s8':s8,'s6':s6,'s9':s9,'s10':s10,'r19':r19,'r20':r20,'r21':r21,'h3':h3,'h4':h4,'h5':h5,'p2':p2,'s7':s7,'h18':h18,'c1':c1,'c2':c2,'c3':c3,'c4':c4,'c8':c8,'f1':f1,'f2':f2,'f6':f6,'f14':f14,'f15':f15,'r18':r18,'r10':r10,'r11':r11,'f7':f7,'p5':p5,'p9':p9,'p10':p10,'p11':p11,'p6':p6,'h7':h7,'h13':h13,'h6':h6,'h10':h10,'h1':h1,'h2':h2,'f5':f5,'d1':d1,'d2':d2,'d5':d5,'d6':d6,'d7':d7,'d8':d8,'d9':d9,'d10':d10,'d12':d12,'d13':d13,'r27':r27,'l4':l4,'h16':h16,'p12':p12,'l1':l1,'l2':l2,'l3':l3,'l5':l5,'r14':r14})