_L='10 sec'
_K='bar x10'
_J='min'
_I='C/F bar x10'
_H='sec'
_G='C/F x10'
_F='flag'
_E='N/A'
_D='read-only'
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
uchiller_cmpMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_E)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_E)
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
if mibBuilder.loadTexts:netSize.setUnits(_E)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_E)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_E)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_E)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_E)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_E)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_E)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_E)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_E)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_E)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_E)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Est_inv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Est_inv_Type.__name__=_B
_Est_inv_Object=MibScalar
est_inv=_Est_inv_Object((1,3,6,1,4,1,9839,2,1,1,1),_Est_inv_Type())
est_inv.setMaxAccess(_C)
if mibBuilder.loadTexts:est_inv.setStatus(_A)
if mibBuilder.loadTexts:est_inv.setUnits(_E)
class _On_off_unita_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_On_off_unita_Type.__name__=_B
_On_off_unita_Object=MibScalar
on_off_unita=_On_off_unita_Object((1,3,6,1,4,1,9839,2,1,1,2),_On_off_unita_Type())
on_off_unita.setMaxAccess(_C)
if mibBuilder.loadTexts:on_off_unita.setStatus(_A)
if mibBuilder.loadTexts:on_off_unita.setUnits(_E)
class _Allarme_hp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Allarme_hp_Type.__name__=_B
_Allarme_hp_Object=MibScalar
allarme_hp=_Allarme_hp_Object((1,3,6,1,4,1,9839,2,1,1,5),_Allarme_hp_Type())
allarme_hp.setMaxAccess(_D)
if mibBuilder.loadTexts:allarme_hp.setStatus(_A)
if mibBuilder.loadTexts:allarme_hp.setUnits(_E)
class _Allarme_lp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Allarme_lp_Type.__name__=_B
_Allarme_lp_Object=MibScalar
allarme_lp=_Allarme_lp_Object((1,3,6,1,4,1,9839,2,1,1,6),_Allarme_lp_Type())
allarme_lp.setMaxAccess(_D)
if mibBuilder.loadTexts:allarme_lp.setStatus(_A)
if mibBuilder.loadTexts:allarme_lp.setUnits(_E)
class _All_flusso_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_flusso_Type.__name__=_B
_All_flusso_Object=MibScalar
all_flusso=_All_flusso_Object((1,3,6,1,4,1,9839,2,1,1,8),_All_flusso_Type())
all_flusso.setMaxAccess(_D)
if mibBuilder.loadTexts:all_flusso.setStatus(_A)
if mibBuilder.loadTexts:all_flusso.setUnits(_E)
class _Err_sonda_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Err_sonda_b3_Type.__name__=_B
_Err_sonda_b3_Object=MibScalar
err_sonda_b3=_Err_sonda_b3_Object((1,3,6,1,4,1,9839,2,1,1,9),_Err_sonda_b3_Type())
err_sonda_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:err_sonda_b3.setStatus(_A)
if mibBuilder.loadTexts:err_sonda_b3.setUnits(_E)
class _Err_sonda_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Err_sonda_b2_Type.__name__=_B
_Err_sonda_b2_Object=MibScalar
err_sonda_b2=_Err_sonda_b2_Object((1,3,6,1,4,1,9839,2,1,1,10),_Err_sonda_b2_Type())
err_sonda_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:err_sonda_b2.setStatus(_A)
if mibBuilder.loadTexts:err_sonda_b2.setUnits(_E)
class _Err_sonda_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Err_sonda_b1_Type.__name__=_B
_Err_sonda_b1_Object=MibScalar
err_sonda_b1=_Err_sonda_b1_Object((1,3,6,1,4,1,9839,2,1,1,11),_Err_sonda_b1_Type())
err_sonda_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:err_sonda_b1.setStatus(_A)
if mibBuilder.loadTexts:err_sonda_b1.setUnits(_E)
class _Err_eeprom_s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Err_eeprom_s_Type.__name__=_B
_Err_eeprom_s_Object=MibScalar
err_eeprom_s=_Err_eeprom_s_Object((1,3,6,1,4,1,9839,2,1,1,13),_Err_eeprom_s_Type())
err_eeprom_s.setMaxAccess(_D)
if mibBuilder.loadTexts:err_eeprom_s.setStatus(_A)
if mibBuilder.loadTexts:err_eeprom_s.setUnits(_E)
class _All_termin_off_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_termin_off_Type.__name__=_B
_All_termin_off_Object=MibScalar
all_termin_off=_All_termin_off_Object((1,3,6,1,4,1,9839,2,1,1,16),_All_termin_off_Type())
all_termin_off.setMaxAccess(_D)
if mibBuilder.loadTexts:all_termin_off.setStatus(_A)
if mibBuilder.loadTexts:all_termin_off.setUnits(_E)
class _Sbrinamento_on_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sbrinamento_on_Type.__name__=_B
_Sbrinamento_on_Object=MibScalar
sbrinamento_on=_Sbrinamento_on_Object((1,3,6,1,4,1,9839,2,1,1,17),_Sbrinamento_on_Type())
sbrinamento_on.setMaxAccess(_D)
if mibBuilder.loadTexts:sbrinamento_on.setStatus(_A)
if mibBuilder.loadTexts:sbrinamento_on.setUnits(_E)
class _All_sbrinamento_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sbrinamento_Type.__name__=_B
_All_sbrinamento_Object=MibScalar
all_sbrinamento=_All_sbrinamento_Object((1,3,6,1,4,1,9839,2,1,1,18),_All_sbrinamento_Type())
all_sbrinamento.setMaxAccess(_D)
if mibBuilder.loadTexts:all_sbrinamento.setStatus(_A)
if mibBuilder.loadTexts:all_sbrinamento.setUnits(_E)
class _All_antigelo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_antigelo_Type.__name__=_B
_All_antigelo_Object=MibScalar
all_antigelo=_All_antigelo_Object((1,3,6,1,4,1,9839,2,1,1,19),_All_antigelo_Type())
all_antigelo.setMaxAccess(_D)
if mibBuilder.loadTexts:all_antigelo.setStatus(_A)
if mibBuilder.loadTexts:all_antigelo.setUnits(_E)
class _All_agelo_sonda_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_agelo_sonda_Type.__name__=_B
_All_agelo_sonda_Object=MibScalar
all_agelo_sonda=_All_agelo_sonda_Object((1,3,6,1,4,1,9839,2,1,1,20),_All_agelo_sonda_Type())
all_agelo_sonda.setMaxAccess(_D)
if mibBuilder.loadTexts:all_agelo_sonda.setStatus(_A)
if mibBuilder.loadTexts:all_agelo_sonda.setUnits(_E)
class _All_sovratens_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sovratens_Type.__name__=_B
_All_sovratens_Object=MibScalar
all_sovratens=_All_sovratens_Object((1,3,6,1,4,1,9839,2,1,1,21),_All_sovratens_Type())
all_sovratens.setMaxAccess(_D)
if mibBuilder.loadTexts:all_sovratens.setStatus(_A)
if mibBuilder.loadTexts:all_sovratens.setUnits(_E)
class _All_sottotens_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sottotens_Type.__name__=_B
_All_sottotens_Object=MibScalar
all_sottotens=_All_sottotens_Object((1,3,6,1,4,1,9839,2,1,1,22),_All_sottotens_Type())
all_sottotens.setMaxAccess(_D)
if mibBuilder.loadTexts:all_sottotens.setStatus(_A)
if mibBuilder.loadTexts:all_sottotens.setUnits(_E)
class _Stato_pompa_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_pompa_Type.__name__=_B
_Stato_pompa_Object=MibScalar
stato_pompa=_Stato_pompa_Object((1,3,6,1,4,1,9839,2,1,1,25),_Stato_pompa_Type())
stato_pompa.setMaxAccess(_D)
if mibBuilder.loadTexts:stato_pompa.setStatus(_A)
if mibBuilder.loadTexts:stato_pompa.setUnits(_E)
class _Stato_compress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_compress_Type.__name__=_B
_Stato_compress_Object=MibScalar
stato_compress=_Stato_compress_Object((1,3,6,1,4,1,9839,2,1,1,26),_Stato_compress_Type())
stato_compress.setMaxAccess(_D)
if mibBuilder.loadTexts:stato_compress.setStatus(_A)
if mibBuilder.loadTexts:stato_compress.setUnits(_E)
class _Stato_resists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_resists_Type.__name__=_B
_Stato_resists_Object=MibScalar
stato_resists=_Stato_resists_Object((1,3,6,1,4,1,9839,2,1,1,27),_Stato_resists_Type())
stato_resists.setMaxAccess(_D)
if mibBuilder.loadTexts:stato_resists.setStatus(_A)
if mibBuilder.loadTexts:stato_resists.setUnits(_E)
class _Stato_valvola_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_valvola_Type.__name__=_B
_Stato_valvola_Object=MibScalar
stato_valvola=_Stato_valvola_Object((1,3,6,1,4,1,9839,2,1,1,28),_Stato_valvola_Type())
stato_valvola.setMaxAccess(_D)
if mibBuilder.loadTexts:stato_valvola.setStatus(_A)
if mibBuilder.loadTexts:stato_valvola.setUnits(_E)
class _Stato_ventils_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stato_ventils_Type.__name__=_B
_Stato_ventils_Object=MibScalar
stato_ventils=_Stato_ventils_Object((1,3,6,1,4,1,9839,2,1,1,30),_Stato_ventils_Type())
stato_ventils.setMaxAccess(_D)
if mibBuilder.loadTexts:stato_ventils.setStatus(_A)
if mibBuilder.loadTexts:stato_ventils.setUnits(_E)
class _Unita_misura_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Unita_misura_Type.__name__=_B
_Unita_misura_Object=MibScalar
unita_misura=_Unita_misura_Object((1,3,6,1,4,1,9839,2,1,1,40),_Unita_misura_Type())
unita_misura.setMaxAccess(_C)
if mibBuilder.loadTexts:unita_misura.setStatus(_A)
if mibBuilder.loadTexts:unita_misura.setUnits(_F)
class _Out_per_fan_f1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Out_per_fan_f1_Type.__name__=_B
_Out_per_fan_f1_Object=MibScalar
out_per_fan_f1=_Out_per_fan_f1_Object((1,3,6,1,4,1,9839,2,1,1,41),_Out_per_fan_f1_Type())
out_per_fan_f1.setMaxAccess(_C)
if mibBuilder.loadTexts:out_per_fan_f1.setStatus(_A)
if mibBuilder.loadTexts:out_per_fan_f1.setUnits('flags')
class _Esecuz_sbrin_d1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Esecuz_sbrin_d1_Type.__name__=_B
_Esecuz_sbrin_d1_Object=MibScalar
esecuz_sbrin_d1=_Esecuz_sbrin_d1_Object((1,3,6,1,4,1,9839,2,1,1,42),_Esecuz_sbrin_d1_Type())
esecuz_sbrin_d1.setMaxAccess(_C)
if mibBuilder.loadTexts:esecuz_sbrin_d1.setStatus(_A)
if mibBuilder.loadTexts:esecuz_sbrin_d1.setUnits(_F)
class _Def_time_tmp_d2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Def_time_tmp_d2_Type.__name__=_B
_Def_time_tmp_d2_Object=MibScalar
def_time_tmp_d2=_Def_time_tmp_d2_Object((1,3,6,1,4,1,9839,2,1,1,43),_Def_time_tmp_d2_Type())
def_time_tmp_d2.setMaxAccess(_C)
if mibBuilder.loadTexts:def_time_tmp_d2.setStatus(_A)
if mibBuilder.loadTexts:def_time_tmp_d2.setUnits(_F)
class _Res_gelo_sbr_db_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Res_gelo_sbr_db_Type.__name__=_B
_Res_gelo_sbr_db_Object=MibScalar
res_gelo_sbr_db=_Res_gelo_sbr_db_Object((1,3,6,1,4,1,9839,2,1,1,44),_Res_gelo_sbr_db_Type())
res_gelo_sbr_db.setMaxAccess(_C)
if mibBuilder.loadTexts:res_gelo_sbr_db.setStatus(_A)
if mibBuilder.loadTexts:res_gelo_sbr_db.setUnits(_F)
class _En_sonda_res_a6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sonda_res_a6_Type.__name__=_B
_En_sonda_res_a6_Object=MibScalar
en_sonda_res_a6=_En_sonda_res_a6_Object((1,3,6,1,4,1,9839,2,1,1,45),_En_sonda_res_a6_Type())
en_sonda_res_a6.setMaxAccess(_C)
if mibBuilder.loadTexts:en_sonda_res_a6.setStatus(_A)
if mibBuilder.loadTexts:en_sonda_res_a6.setUnits(_F)
class _All_lp_sonda_p7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_lp_sonda_p7_Type.__name__=_B
_All_lp_sonda_p7_Object=MibScalar
all_lp_sonda_p7=_All_lp_sonda_p7_Object((1,3,6,1,4,1,9839,2,1,1,46),_All_lp_sonda_p7_Type())
all_lp_sonda_p7.setMaxAccess(_C)
if mibBuilder.loadTexts:all_lp_sonda_p7.setStatus(_A)
if mibBuilder.loadTexts:all_lp_sonda_p7.setUnits(_F)
class _En_id_on_off_h7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_id_on_off_h7_Type.__name__=_B
_En_id_on_off_h7_Object=MibScalar
en_id_on_off_h7=_En_id_on_off_h7_Object((1,3,6,1,4,1,9839,2,1,1,47),_En_id_on_off_h7_Type())
en_id_on_off_h7.setMaxAccess(_C)
if mibBuilder.loadTexts:en_id_on_off_h7.setStatus(_A)
if mibBuilder.loadTexts:en_id_on_off_h7.setUnits(_F)
class _All_lp_comp_pa_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_lp_comp_pa_Type.__name__=_B
_All_lp_comp_pa_Object=MibScalar
all_lp_comp_pa=_All_lp_comp_pa_Object((1,3,6,1,4,1,9839,2,1,1,48),_All_lp_comp_pa_Type())
all_lp_comp_pa.setMaxAccess(_C)
if mibBuilder.loadTexts:all_lp_comp_pa.setStatus(_A)
if mibBuilder.loadTexts:all_lp_comp_pa.setUnits(_F)
class _En_set2_hc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_set2_hc_Type.__name__=_B
_En_set2_hc_Object=MibScalar
en_set2_hc=_En_set2_hc_Object((1,3,6,1,4,1,9839,2,1,1,49),_En_set2_hc_Type())
en_set2_hc.setMaxAccess(_C)
if mibBuilder.loadTexts:en_set2_hc.setStatus(_A)
if mibBuilder.loadTexts:en_set2_hc.setUnits(_F)
class _Inv_est_inv_hd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_est_inv_hd_Type.__name__=_B
_Inv_est_inv_hd_Object=MibScalar
inv_est_inv_hd=_Inv_est_inv_hd_Object((1,3,6,1,4,1,9839,2,1,1,50),_Inv_est_inv_hd_Type())
inv_est_inv_hd.setMaxAccess(_C)
if mibBuilder.loadTexts:inv_est_inv_hd.setStatus(_A)
if mibBuilder.loadTexts:inv_est_inv_hd.setUnits(_F)
class _Sel_rele_all_hf_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sel_rele_all_hf_Type.__name__=_B
_Sel_rele_all_hf_Object=MibScalar
sel_rele_all_hf=_Sel_rele_all_hf_Object((1,3,6,1,4,1,9839,2,1,1,51),_Sel_rele_all_hf_Type())
sel_rele_all_hf.setMaxAccess(_C)
if mibBuilder.loadTexts:sel_rele_all_hf.setStatus(_A)
if mibBuilder.loadTexts:sel_rele_all_hf.setUnits(_F)
class _Ab_estate_inv_h6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ab_estate_inv_h6_Type.__name__=_B
_Ab_estate_inv_h6_Object=MibScalar
ab_estate_inv_h6=_Ab_estate_inv_h6_Object((1,3,6,1,4,1,9839,2,1,1,55),_Ab_estate_inv_h6_Type())
ab_estate_inv_h6.setMaxAccess(_C)
if mibBuilder.loadTexts:ab_estate_inv_h6.setStatus(_A)
if mibBuilder.loadTexts:ab_estate_inv_h6.setUnits(_F)
class _Rotaz_compr_r5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rotaz_compr_r5_Type.__name__=_B
_Rotaz_compr_r5_Object=MibScalar
rotaz_compr_r5=_Rotaz_compr_r5_Object((1,3,6,1,4,1,9839,2,1,1,56),_Rotaz_compr_r5_Type())
rotaz_compr_r5.setMaxAccess(_D)
if mibBuilder.loadTexts:rotaz_compr_r5.setStatus(_A)
if mibBuilder.loadTexts:rotaz_compr_r5.setUnits(_E)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Sonda_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b1_Type.__name__=_B
_Sonda_b1_Object=MibScalar
sonda_b1=_Sonda_b1_Object((1,3,6,1,4,1,9839,2,1,2,1),_Sonda_b1_Type())
sonda_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:sonda_b1.setStatus(_A)
if mibBuilder.loadTexts:sonda_b1.setUnits(_E)
class _Sonda_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b2_Type.__name__=_B
_Sonda_b2_Object=MibScalar
sonda_b2=_Sonda_b2_Object((1,3,6,1,4,1,9839,2,1,2,2),_Sonda_b2_Type())
sonda_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:sonda_b2.setStatus(_A)
if mibBuilder.loadTexts:sonda_b2.setUnits(_E)
class _Sonda_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b3_Type.__name__=_B
_Sonda_b3_Object=MibScalar
sonda_b3=_Sonda_b3_Object((1,3,6,1,4,1,9839,2,1,2,3),_Sonda_b3_Type())
sonda_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:sonda_b3.setStatus(_A)
if mibBuilder.loadTexts:sonda_b3.setUnits(_E)
class _I_scala_press_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_I_scala_press_Type.__name__=_B
_I_scala_press_Object=MibScalar
i_scala_press=_I_scala_press_Object((1,3,6,1,4,1,9839,2,1,2,5),_I_scala_press_Type())
i_scala_press.setMaxAccess(_C)
if mibBuilder.loadTexts:i_scala_press.setStatus(_A)
if mibBuilder.loadTexts:i_scala_press.setUnits(_K)
class _F_scala_press_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,400))
_F_scala_press_Type.__name__=_B
_F_scala_press_Object=MibScalar
f_scala_press=_F_scala_press_Object((1,3,6,1,4,1,9839,2,1,2,6),_F_scala_press_Type())
f_scala_press.setMaxAccess(_C)
if mibBuilder.loadTexts:f_scala_press.setStatus(_A)
if mibBuilder.loadTexts:f_scala_press.setUnits(_K)
class _Calibra_b1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-120,120))
_Calibra_b1_Type.__name__=_B
_Calibra_b1_Object=MibScalar
calibra_b1=_Calibra_b1_Object((1,3,6,1,4,1,9839,2,1,2,7),_Calibra_b1_Type())
calibra_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:calibra_b1.setStatus(_A)
if mibBuilder.loadTexts:calibra_b1.setUnits(_G)
class _Calibra_b2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-120,120))
_Calibra_b2_Type.__name__=_B
_Calibra_b2_Object=MibScalar
calibra_b2=_Calibra_b2_Object((1,3,6,1,4,1,9839,2,1,2,8),_Calibra_b2_Type())
calibra_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:calibra_b2.setStatus(_A)
if mibBuilder.loadTexts:calibra_b2.setUnits(_G)
class _Calibra_b3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-120,120))
_Calibra_b3_Type.__name__=_B
_Calibra_b3_Object=MibScalar
calibra_b3=_Calibra_b3_Object((1,3,6,1,4,1,9839,2,1,2,9),_Calibra_b3_Type())
calibra_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:calibra_b3.setStatus(_A)
if mibBuilder.loadTexts:calibra_b3.setUnits(_G)
class _Setp_estate_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Setp_estate_Type.__name__=_B
_Setp_estate_Object=MibScalar
setp_estate=_Setp_estate_Object((1,3,6,1,4,1,9839,2,1,2,10),_Setp_estate_Type())
setp_estate.setMaxAccess(_C)
if mibBuilder.loadTexts:setp_estate.setStatus(_A)
if mibBuilder.loadTexts:setp_estate.setUnits(_G)
class _Diff_estate_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,199))
_Diff_estate_Type.__name__=_B
_Diff_estate_Object=MibScalar
diff_estate=_Diff_estate_Object((1,3,6,1,4,1,9839,2,1,2,11),_Diff_estate_Type())
diff_estate.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_estate.setStatus(_A)
if mibBuilder.loadTexts:diff_estate.setUnits(_G)
class _Setp_inverno_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Setp_inverno_Type.__name__=_B
_Setp_inverno_Object=MibScalar
setp_inverno=_Setp_inverno_Object((1,3,6,1,4,1,9839,2,1,2,12),_Setp_inverno_Type())
setp_inverno.setMaxAccess(_C)
if mibBuilder.loadTexts:setp_inverno.setStatus(_A)
if mibBuilder.loadTexts:setp_inverno.setUnits(_G)
class _Diff_inverno_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,199))
_Diff_inverno_Type.__name__=_B
_Diff_inverno_Object=MibScalar
diff_inverno=_Diff_inverno_Object((1,3,6,1,4,1,9839,2,1,2,13),_Diff_inverno_Type())
diff_inverno.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_inverno.setStatus(_A)
if mibBuilder.loadTexts:diff_inverno.setUnits(_G)
class _Min_set_est_Type(Integer32):defaultValue=-400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,32767))
_Min_set_est_Type.__name__=_B
_Min_set_est_Object=MibScalar
min_set_est=_Min_set_est_Object((1,3,6,1,4,1,9839,2,1,2,14),_Min_set_est_Type())
min_set_est.setMaxAccess(_C)
if mibBuilder.loadTexts:min_set_est.setStatus(_A)
if mibBuilder.loadTexts:min_set_est.setUnits(_G)
class _Max_set_est_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,1990))
_Max_set_est_Type.__name__=_B
_Max_set_est_Object=MibScalar
max_set_est=_Max_set_est_Object((1,3,6,1,4,1,9839,2,1,2,15),_Max_set_est_Type())
max_set_est.setMaxAccess(_C)
if mibBuilder.loadTexts:max_set_est.setStatus(_A)
if mibBuilder.loadTexts:max_set_est.setUnits(_G)
class _Min_set_inv_Type(Integer32):defaultValue=-400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,32767))
_Min_set_inv_Type.__name__=_B
_Min_set_inv_Object=MibScalar
min_set_inv=_Min_set_inv_Object((1,3,6,1,4,1,9839,2,1,2,16),_Min_set_inv_Type())
min_set_inv.setMaxAccess(_C)
if mibBuilder.loadTexts:min_set_inv.setStatus(_A)
if mibBuilder.loadTexts:min_set_inv.setUnits(_G)
class _Max_set_inv_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,1990))
_Max_set_inv_Type.__name__=_B
_Max_set_inv_Object=MibScalar
max_set_inv=_Max_set_inv_Object((1,3,6,1,4,1,9839,2,1,2,17),_Max_set_inv_Type())
max_set_inv.setMaxAccess(_C)
if mibBuilder.loadTexts:max_set_inv.setStatus(_A)
if mibBuilder.loadTexts:max_set_inv.setUnits(_G)
class _Tmin_vel_est_f5_Type(Integer32):defaultValue=130;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Tmin_vel_est_f5_Type.__name__=_B
_Tmin_vel_est_f5_Object=MibScalar
tmin_vel_est_f5=_Tmin_vel_est_f5_Object((1,3,6,1,4,1,9839,2,1,2,18),_Tmin_vel_est_f5_Type())
tmin_vel_est_f5.setMaxAccess(_C)
if mibBuilder.loadTexts:tmin_vel_est_f5.setStatus(_A)
if mibBuilder.loadTexts:tmin_vel_est_f5.setUnits(_I)
class _Tmax_vel_est_f6_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Tmax_vel_est_f6_Type.__name__=_B
_Tmax_vel_est_f6_Object=MibScalar
tmax_vel_est_f6=_Tmax_vel_est_f6_Object((1,3,6,1,4,1,9839,2,1,2,19),_Tmax_vel_est_f6_Type())
tmax_vel_est_f6.setMaxAccess(_C)
if mibBuilder.loadTexts:tmax_vel_est_f6.setStatus(_A)
if mibBuilder.loadTexts:tmax_vel_est_f6.setUnits(_I)
class _Tmin_vel_inv_f7_Type(Integer32):defaultValue=130;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Tmin_vel_inv_f7_Type.__name__=_B
_Tmin_vel_inv_f7_Object=MibScalar
tmin_vel_inv_f7=_Tmin_vel_inv_f7_Object((1,3,6,1,4,1,9839,2,1,2,20),_Tmin_vel_inv_f7_Type())
tmin_vel_inv_f7.setMaxAccess(_C)
if mibBuilder.loadTexts:tmin_vel_inv_f7.setStatus(_A)
if mibBuilder.loadTexts:tmin_vel_inv_f7.setUnits(_I)
class _Tmax_vel_inv_f8_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Tmax_vel_inv_f8_Type.__name__=_B
_Tmax_vel_inv_f8_Object=MibScalar
tmax_vel_inv_f8=_Tmax_vel_inv_f8_Object((1,3,6,1,4,1,9839,2,1,2,21),_Tmax_vel_inv_f8_Type())
tmax_vel_inv_f8.setMaxAccess(_C)
if mibBuilder.loadTexts:tmax_vel_inv_f8.setStatus(_A)
if mibBuilder.loadTexts:tmax_vel_inv_f8.setUnits(_I)
class _Toff_fan_est_f9_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Toff_fan_est_f9_Type.__name__=_B
_Toff_fan_est_f9_Object=MibScalar
toff_fan_est_f9=_Toff_fan_est_f9_Object((1,3,6,1,4,1,9839,2,1,2,22),_Toff_fan_est_f9_Type())
toff_fan_est_f9.setMaxAccess(_C)
if mibBuilder.loadTexts:toff_fan_est_f9.setStatus(_A)
if mibBuilder.loadTexts:toff_fan_est_f9.setUnits(_I)
class _Toff_fan_inv_fa_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Toff_fan_inv_fa_Type.__name__=_B
_Toff_fan_inv_fa_Object=MibScalar
toff_fan_inv_fa=_Toff_fan_inv_fa_Object((1,3,6,1,4,1,9839,2,1,2,23),_Toff_fan_inv_fa_Type())
toff_fan_inv_fa.setMaxAccess(_C)
if mibBuilder.loadTexts:toff_fan_inv_fa.setStatus(_A)
if mibBuilder.loadTexts:toff_fan_inv_fa.setUnits(_I)
class _Parametro_d3_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Parametro_d3_Type.__name__=_B
_Parametro_d3_Object=MibScalar
parametro_d3=_Parametro_d3_Object((1,3,6,1,4,1,9839,2,1,2,24),_Parametro_d3_Type())
parametro_d3.setMaxAccess(_C)
if mibBuilder.loadTexts:parametro_d3.setStatus(_A)
if mibBuilder.loadTexts:parametro_d3.setUnits(_I)
class _Parametro_d4_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Parametro_d4_Type.__name__=_B
_Parametro_d4_Object=MibScalar
parametro_d4=_Parametro_d4_Object((1,3,6,1,4,1,9839,2,1,2,25),_Parametro_d4_Type())
parametro_d4.setMaxAccess(_C)
if mibBuilder.loadTexts:parametro_d4.setStatus(_A)
if mibBuilder.loadTexts:parametro_d4.setUnits(_I)
class _Set_al_agelo_a1_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_al_agelo_a1_Type.__name__=_B
_Set_al_agelo_a1_Object=MibScalar
set_al_agelo_a1=_Set_al_agelo_a1_Object((1,3,6,1,4,1,9839,2,1,2,26),_Set_al_agelo_a1_Type())
set_al_agelo_a1.setMaxAccess(_C)
if mibBuilder.loadTexts:set_al_agelo_a1.setStatus(_A)
if mibBuilder.loadTexts:set_al_agelo_a1.setUnits(_G)
class _Dif_al_agelo_a2_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,199))
_Dif_al_agelo_a2_Type.__name__=_B
_Dif_al_agelo_a2_Object=MibScalar
dif_al_agelo_a2=_Dif_al_agelo_a2_Object((1,3,6,1,4,1,9839,2,1,2,27),_Dif_al_agelo_a2_Type())
dif_al_agelo_a2.setMaxAccess(_C)
if mibBuilder.loadTexts:dif_al_agelo_a2.setStatus(_A)
if mibBuilder.loadTexts:dif_al_agelo_a2.setUnits(_G)
class _Set_res_gelo_a4_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_res_gelo_a4_Type.__name__=_B
_Set_res_gelo_a4_Object=MibScalar
set_res_gelo_a4=_Set_res_gelo_a4_Object((1,3,6,1,4,1,9839,2,1,2,28),_Set_res_gelo_a4_Type())
set_res_gelo_a4.setMaxAccess(_C)
if mibBuilder.loadTexts:set_res_gelo_a4.setStatus(_A)
if mibBuilder.loadTexts:set_res_gelo_a4.setUnits(_G)
class _Dif_res_gelo_a5_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,199))
_Dif_res_gelo_a5_Type.__name__=_B
_Dif_res_gelo_a5_Object=MibScalar
dif_res_gelo_a5=_Dif_res_gelo_a5_Object((1,3,6,1,4,1,9839,2,1,2,29),_Dif_res_gelo_a5_Type())
dif_res_gelo_a5.setMaxAccess(_C)
if mibBuilder.loadTexts:dif_res_gelo_a5.setStatus(_A)
if mibBuilder.loadTexts:dif_res_gelo_a5.setUnits(_G)
class _Lim_set_gelo_a7_Type(Integer32):defaultValue=-400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1220))
_Lim_set_gelo_a7_Type.__name__=_B
_Lim_set_gelo_a7_Object=MibScalar
lim_set_gelo_a7=_Lim_set_gelo_a7_Object((1,3,6,1,4,1,9839,2,1,2,30),_Lim_set_gelo_a7_Type())
lim_set_gelo_a7.setMaxAccess(_C)
if mibBuilder.loadTexts:lim_set_gelo_a7.setStatus(_A)
if mibBuilder.loadTexts:lim_set_gelo_a7.setUnits(_G)
class _Set_res_risc_a8_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_res_risc_a8_Type.__name__=_B
_Set_res_risc_a8_Object=MibScalar
set_res_risc_a8=_Set_res_risc_a8_Object((1,3,6,1,4,1,9839,2,1,2,31),_Set_res_risc_a8_Type())
set_res_risc_a8.setMaxAccess(_C)
if mibBuilder.loadTexts:set_res_risc_a8.setStatus(_A)
if mibBuilder.loadTexts:set_res_risc_a8.setUnits(_G)
class _Dif_res_risc_a9_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,199))
_Dif_res_risc_a9_Type.__name__=_B
_Dif_res_risc_a9_Object=MibScalar
dif_res_risc_a9=_Dif_res_risc_a9_Object((1,3,6,1,4,1,9839,2,1,2,32),_Dif_res_risc_a9_Type())
dif_res_risc_a9.setMaxAccess(_C)
if mibBuilder.loadTexts:dif_res_risc_a9.setStatus(_A)
if mibBuilder.loadTexts:dif_res_risc_a9.setUnits(_G)
class _Set_all_at_pb_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1990))
_Set_all_at_pb_Type.__name__=_B
_Set_all_at_pb_Object=MibScalar
set_all_at_pb=_Set_all_at_pb_Object((1,3,6,1,4,1,9839,2,1,2,33),_Set_all_at_pb_Type())
set_all_at_pb.setMaxAccess(_C)
if mibBuilder.loadTexts:set_all_at_pb.setStatus(_A)
if mibBuilder.loadTexts:set_all_at_pb.setUnits('/d x10')
class _Sonda_b4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sonda_b4_Type.__name__=_B
_Sonda_b4_Object=MibScalar
sonda_b4=_Sonda_b4_Object((1,3,6,1,4,1,9839,2,1,2,34),_Sonda_b4_Type())
sonda_b4.setMaxAccess(_D)
if mibBuilder.loadTexts:sonda_b4.setStatus(_A)
if mibBuilder.loadTexts:sonda_b4.setUnits(_E)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Velocita_vent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Velocita_vent_Type.__name__=_B
_Velocita_vent_Object=MibScalar
velocita_vent=_Velocita_vent_Object((1,3,6,1,4,1,9839,2,1,3,1),_Velocita_vent_Type())
velocita_vent.setMaxAccess(_D)
if mibBuilder.loadTexts:velocita_vent.setStatus(_A)
if mibBuilder.loadTexts:velocita_vent.setUnits(_E)
class _Filtro_digitale_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Filtro_digitale_Type.__name__=_B
_Filtro_digitale_Object=MibScalar
filtro_digitale=_Filtro_digitale_Object((1,3,6,1,4,1,9839,2,1,3,6),_Filtro_digitale_Type())
filtro_digitale.setMaxAccess(_C)
if mibBuilder.loadTexts:filtro_digitale.setStatus(_A)
if mibBuilder.loadTexts:filtro_digitale.setUnits(_E)
class _Tmin_on_comp_c1_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Tmin_on_comp_c1_Type.__name__=_B
_Tmin_on_comp_c1_Object=MibScalar
tmin_on_comp_c1=_Tmin_on_comp_c1_Object((1,3,6,1,4,1,9839,2,1,3,8),_Tmin_on_comp_c1_Type())
tmin_on_comp_c1.setMaxAccess(_C)
if mibBuilder.loadTexts:tmin_on_comp_c1.setStatus(_A)
if mibBuilder.loadTexts:tmin_on_comp_c1.setUnits(_H)
class _Tmin_sp_comp_c2_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_Tmin_sp_comp_c2_Type.__name__=_B
_Tmin_sp_comp_c2_Object=MibScalar
tmin_sp_comp_c2=_Tmin_sp_comp_c2_Object((1,3,6,1,4,1,9839,2,1,3,9),_Tmin_sp_comp_c2_Type())
tmin_sp_comp_c2.setMaxAccess(_C)
if mibBuilder.loadTexts:tmin_sp_comp_c2.setStatus(_A)
if mibBuilder.loadTexts:tmin_sp_comp_c2.setUnits(_L)
class _Time_2_acc_c3_Type(Integer32):defaultValue=36;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_Time_2_acc_c3_Type.__name__=_B
_Time_2_acc_c3_Object=MibScalar
time_2_acc_c3=_Time_2_acc_c3_Object((1,3,6,1,4,1,9839,2,1,3,10),_Time_2_acc_c3_Type())
time_2_acc_c3.setMaxAccess(_C)
if mibBuilder.loadTexts:time_2_acc_c3.setStatus(_A)
if mibBuilder.loadTexts:time_2_acc_c3.setUnits(_L)
class _Rit_on_comp_c6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Rit_on_comp_c6_Type.__name__=_B
_Rit_on_comp_c6_Object=MibScalar
rit_on_comp_c6=_Rit_on_comp_c6_Object((1,3,6,1,4,1,9839,2,1,3,11),_Rit_on_comp_c6_Type())
rit_on_comp_c6.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_on_comp_c6.setStatus(_A)
if mibBuilder.loadTexts:rit_on_comp_c6.setUnits(_H)
class _Rit_c_on_pmp_c7_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Rit_c_on_pmp_c7_Type.__name__=_B
_Rit_c_on_pmp_c7_Object=MibScalar
rit_c_on_pmp_c7=_Rit_c_on_pmp_c7_Object((1,3,6,1,4,1,9839,2,1,3,12),_Rit_c_on_pmp_c7_Type())
rit_c_on_pmp_c7.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_c_on_pmp_c7.setStatus(_A)
if mibBuilder.loadTexts:rit_c_on_pmp_c7.setUnits(_H)
class _Off_p_off_v_c8_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Off_p_off_v_c8_Type.__name__=_B
_Off_p_off_v_c8_Object=MibScalar
off_p_off_v_c8=_Off_p_off_v_c8_Object((1,3,6,1,4,1,9839,2,1,3,13),_Off_p_off_v_c8_Type())
off_p_off_v_c8.setMaxAccess(_C)
if mibBuilder.loadTexts:off_p_off_v_c8.setStatus(_A)
if mibBuilder.loadTexts:off_p_off_v_c8.setUnits(_J)
class _Contaore_c1_c9_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19900))
_Contaore_c1_c9_Type.__name__=_B
_Contaore_c1_c9_Object=MibScalar
contaore_c1_c9=_Contaore_c1_c9_Object((1,3,6,1,4,1,9839,2,1,3,14),_Contaore_c1_c9_Type())
contaore_c1_c9.setMaxAccess(_D)
if mibBuilder.loadTexts:contaore_c1_c9.setStatus(_A)
if mibBuilder.loadTexts:contaore_c1_c9.setUnits('hours')
class _Max_ore_comp_cb_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Max_ore_comp_cb_Type.__name__=_B
_Max_ore_comp_cb_Object=MibScalar
max_ore_comp_cb=_Max_ore_comp_cb_Object((1,3,6,1,4,1,9839,2,1,3,15),_Max_ore_comp_cb_Type())
max_ore_comp_cb.setMaxAccess(_C)
if mibBuilder.loadTexts:max_ore_comp_cb.setStatus(_A)
if mibBuilder.loadTexts:max_ore_comp_cb.setUnits('100 hours')
class _Ore_pmp_vent_cc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19900))
_Ore_pmp_vent_cc_Type.__name__=_B
_Ore_pmp_vent_cc_Object=MibScalar
ore_pmp_vent_cc=_Ore_pmp_vent_cc_Object((1,3,6,1,4,1,9839,2,1,3,16),_Ore_pmp_vent_cc_Type())
ore_pmp_vent_cc.setMaxAccess(_D)
if mibBuilder.loadTexts:ore_pmp_vent_cc.setStatus(_A)
if mibBuilder.loadTexts:ore_pmp_vent_cc.setUnits('hours')
class _Modo_vent_f2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Modo_vent_f2_Type.__name__=_B
_Modo_vent_f2_Object=MibScalar
modo_vent_f2=_Modo_vent_f2_Object((1,3,6,1,4,1,9839,2,1,3,17),_Modo_vent_f2_Type())
modo_vent_f2.setMaxAccess(_C)
if mibBuilder.loadTexts:modo_vent_f2.setStatus(_A)
if mibBuilder.loadTexts:modo_vent_f2.setUnits('flags')
class _Min_volt_f3_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_Min_volt_f3_Type.__name__=_B
_Min_volt_f3_Object=MibScalar
min_volt_f3=_Min_volt_f3_Object((1,3,6,1,4,1,9839,2,1,3,18),_Min_volt_f3_Type())
min_volt_f3.setMaxAccess(_C)
if mibBuilder.loadTexts:min_volt_f3.setStatus(_A)
if mibBuilder.loadTexts:min_volt_f3.setUnits('step')
class _Max_volt_f4_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,100))
_Max_volt_f4_Type.__name__=_B
_Max_volt_f4_Object=MibScalar
max_volt_f4=_Max_volt_f4_Object((1,3,6,1,4,1,9839,2,1,3,19),_Max_volt_f4_Type())
max_volt_f4.setMaxAccess(_C)
if mibBuilder.loadTexts:max_volt_f4.setStatus(_A)
if mibBuilder.loadTexts:max_volt_f4.setUnits('step')
class _T_spunto_v_fb_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_T_spunto_v_fb_Type.__name__=_B
_T_spunto_v_fb_Object=MibScalar
t_spunto_v_fb=_T_spunto_v_fb_Object((1,3,6,1,4,1,9839,2,1,3,20),_T_spunto_v_fb_Type())
t_spunto_v_fb.setMaxAccess(_C)
if mibBuilder.loadTexts:t_spunto_v_fb.setStatus(_A)
if mibBuilder.loadTexts:t_spunto_v_fb.setUnits(_H)
class _T_imp_triac_fc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_T_imp_triac_fc_Type.__name__=_B
_T_imp_triac_fc_Object=MibScalar
t_imp_triac_fc=_T_imp_triac_fc_Object((1,3,6,1,4,1,9839,2,1,3,21),_T_imp_triac_fc_Type())
t_imp_triac_fc.setMaxAccess(_C)
if mibBuilder.loadTexts:t_imp_triac_fc.setStatus(_A)
if mibBuilder.loadTexts:t_imp_triac_fc.setUnits('msec')
class _T_min_on_def_d5_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,150))
_T_min_on_def_d5_Type.__name__=_B
_T_min_on_def_d5_Object=MibScalar
t_min_on_def_d5=_T_min_on_def_d5_Object((1,3,6,1,4,1,9839,2,1,3,22),_T_min_on_def_d5_Type())
t_min_on_def_d5.setMaxAccess(_C)
if mibBuilder.loadTexts:t_min_on_def_d5.setStatus(_A)
if mibBuilder.loadTexts:t_min_on_def_d5.setUnits(_H)
class _T_min_def_d6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_T_min_def_d6_Type.__name__=_B
_T_min_def_d6_Object=MibScalar
t_min_def_d6=_T_min_def_d6_Object((1,3,6,1,4,1,9839,2,1,3,23),_T_min_def_d6_Type())
t_min_def_d6.setMaxAccess(_C)
if mibBuilder.loadTexts:t_min_def_d6.setStatus(_A)
if mibBuilder.loadTexts:t_min_def_d6.setUnits(_H)
class _T_max_def_d7_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_T_max_def_d7_Type.__name__=_B
_T_max_def_d7_Object=MibScalar
t_max_def_d7=_T_max_def_d7_Object((1,3,6,1,4,1,9839,2,1,3,24),_T_max_def_d7_Type())
t_max_def_d7.setMaxAccess(_C)
if mibBuilder.loadTexts:t_max_def_d7.setStatus(_A)
if mibBuilder.loadTexts:t_max_def_d7.setUnits(_J)
class _Rit_tra_2def_d8_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,150))
_Rit_tra_2def_d8_Type.__name__=_B
_Rit_tra_2def_d8_Object=MibScalar
rit_tra_2def_d8=_Rit_tra_2def_d8_Object((1,3,6,1,4,1,9839,2,1,3,25),_Rit_tra_2def_d8_Type())
rit_tra_2def_d8.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_tra_2def_d8.setStatus(_A)
if mibBuilder.loadTexts:rit_tra_2def_d8.setUnits(_J)
class _Wait_on_def_dc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Wait_on_def_dc_Type.__name__=_B
_Wait_on_def_dc_Object=MibScalar
wait_on_def_dc=_Wait_on_def_dc_Object((1,3,6,1,4,1,9839,2,1,3,26),_Wait_on_def_dc_Type())
wait_on_def_dc.setMaxAccess(_C)
if mibBuilder.loadTexts:wait_on_def_dc.setStatus(_A)
if mibBuilder.loadTexts:wait_on_def_dc.setUnits(_J)
class _Wait_end_def_dd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Wait_end_def_dd_Type.__name__=_B
_Wait_end_def_dd_Object=MibScalar
wait_end_def_dd=_Wait_end_def_dd_Object((1,3,6,1,4,1,9839,2,1,3,27),_Wait_end_def_dd_Type())
wait_end_def_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:wait_end_def_dd.setStatus(_A)
if mibBuilder.loadTexts:wait_end_def_dd.setUnits(_J)
class _Rit_all_ag_a3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_Rit_all_ag_a3_Type.__name__=_B
_Rit_all_ag_a3_Object=MibScalar
rit_all_ag_a3=_Rit_all_ag_a3_Object((1,3,6,1,4,1,9839,2,1,3,28),_Rit_all_ag_a3_Type())
rit_all_ag_a3.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_all_ag_a3.setStatus(_A)
if mibBuilder.loadTexts:rit_all_ag_a3.setUnits(_H)
class _R_al_on_flux_p1_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_R_al_on_flux_p1_Type.__name__=_B
_R_al_on_flux_p1_Object=MibScalar
r_al_on_flux_p1=_R_al_on_flux_p1_Object((1,3,6,1,4,1,9839,2,1,3,29),_R_al_on_flux_p1_Type())
r_al_on_flux_p1.setMaxAccess(_C)
if mibBuilder.loadTexts:r_al_on_flux_p1.setStatus(_A)
if mibBuilder.loadTexts:r_al_on_flux_p1.setUnits(_H)
class _R_al_rg_flux_p2_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_R_al_rg_flux_p2_Type.__name__=_B
_R_al_rg_flux_p2_Object=MibScalar
r_al_rg_flux_p2=_R_al_rg_flux_p2_Object((1,3,6,1,4,1,9839,2,1,3,30),_R_al_rg_flux_p2_Type())
r_al_rg_flux_p2.setMaxAccess(_C)
if mibBuilder.loadTexts:r_al_rg_flux_p2.setStatus(_A)
if mibBuilder.loadTexts:r_al_rg_flux_p2.setUnits(_H)
class _Rit_all_lp_p3_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Rit_all_lp_p3_Type.__name__=_B
_Rit_all_lp_p3_Object=MibScalar
rit_all_lp_p3=_Rit_all_lp_p3_Object((1,3,6,1,4,1,9839,2,1,3,31),_Rit_all_lp_p3_Type())
rit_all_lp_p3.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_all_lp_p3.setStatus(_A)
if mibBuilder.loadTexts:rit_all_lp_p3.setUnits(_H)
class _T_buzzer_p4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_T_buzzer_p4_Type.__name__=_B
_T_buzzer_p4_Object=MibScalar
t_buzzer_p4=_T_buzzer_p4_Object((1,3,6,1,4,1,9839,2,1,3,32),_T_buzzer_p4_Type())
t_buzzer_p4.setMaxAccess(_C)
if mibBuilder.loadTexts:t_buzzer_p4.setStatus(_A)
if mibBuilder.loadTexts:t_buzzer_p4.setUnits(_J)
class _Riprist_all_p5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Riprist_all_p5_Type.__name__=_B
_Riprist_all_p5_Object=MibScalar
riprist_all_p5=_Riprist_all_p5_Object((1,3,6,1,4,1,9839,2,1,3,33),_Riprist_all_p5_Type())
riprist_all_p5.setMaxAccess(_C)
if mibBuilder.loadTexts:riprist_all_p5.setStatus(_A)
if mibBuilder.loadTexts:riprist_all_p5.setUnits(_F)
class _Selez_id1_p8_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Selez_id1_p8_Type.__name__=_B
_Selez_id1_p8_Object=MibScalar
selez_id1_p8=_Selez_id1_p8_Object((1,3,6,1,4,1,9839,2,1,3,34),_Selez_id1_p8_Type())
selez_id1_p8.setMaxAccess(_C)
if mibBuilder.loadTexts:selez_id1_p8.setStatus(_A)
if mibBuilder.loadTexts:selez_id1_p8.setUnits(_F)
class _Selez_id2_p9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Selez_id2_p9_Type.__name__=_B
_Selez_id2_p9_Object=MibScalar
selez_id2_p9=_Selez_id2_p9_Object((1,3,6,1,4,1,9839,2,1,3,35),_Selez_id2_p9_Type())
selez_id2_p9.setMaxAccess(_C)
if mibBuilder.loadTexts:selez_id2_p9.setStatus(_A)
if mibBuilder.loadTexts:selez_id2_p9.setUnits(_E)
class _Modello_mac_h1_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Modello_mac_h1_Type.__name__=_B
_Modello_mac_h1_Object=MibScalar
modello_mac_h1=_Modello_mac_h1_Object((1,3,6,1,4,1,9839,2,1,3,36),_Modello_mac_h1_Type())
modello_mac_h1.setMaxAccess(_D)
if mibBuilder.loadTexts:modello_mac_h1.setStatus(_A)
if mibBuilder.loadTexts:modello_mac_h1.setUnits(_F)
class _Modo_pmp_vnt_h5_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Modo_pmp_vnt_h5_Type.__name__=_B
_Modo_pmp_vnt_h5_Object=MibScalar
modo_pmp_vnt_h5=_Modo_pmp_vnt_h5_Object((1,3,6,1,4,1,9839,2,1,3,37),_Modo_pmp_vnt_h5_Type())
modo_pmp_vnt_h5.setMaxAccess(_C)
if mibBuilder.loadTexts:modo_pmp_vnt_h5.setStatus(_A)
if mibBuilder.loadTexts:modo_pmp_vnt_h5.setUnits(_F)
class _Blocca_tasti_h9_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Blocca_tasti_h9_Type.__name__=_B
_Blocca_tasti_h9_Object=MibScalar
blocca_tasti_h9=_Blocca_tasti_h9_Object((1,3,6,1,4,1,9839,2,1,3,38),_Blocca_tasti_h9_Type())
blocca_tasti_h9.setMaxAccess(_C)
if mibBuilder.loadTexts:blocca_tasti_h9.setStatus(_A)
if mibBuilder.loadTexts:blocca_tasti_h9.setUnits(_F)
class _Seradd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_Seradd_Type.__name__=_B
_Seradd_Object=MibScalar
seradd=_Seradd_Object((1,3,6,1,4,1,9839,2,1,3,39),_Seradd_Type())
seradd.setMaxAccess(_C)
if mibBuilder.loadTexts:seradd.setStatus(_A)
if mibBuilder.loadTexts:seradd.setUnits(_E)
class _Passw_telec_hb_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Passw_telec_hb_Type.__name__=_B
_Passw_telec_hb_Object=MibScalar
passw_telec_hb=_Passw_telec_hb_Object((1,3,6,1,4,1,9839,2,1,3,40),_Passw_telec_hb_Type())
passw_telec_hb.setMaxAccess(_C)
if mibBuilder.loadTexts:passw_telec_hb.setStatus(_A)
if mibBuilder.loadTexts:passw_telec_hb.setUnits(_E)
class _Valv_inv_ch_he_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Valv_inv_ch_he_Type.__name__=_B
_Valv_inv_ch_he_Object=MibScalar
valv_inv_ch_he=_Valv_inv_ch_he_Object((1,3,6,1,4,1,9839,2,1,3,41),_Valv_inv_ch_he_Type())
valv_inv_ch_he.setMaxAccess(_C)
if mibBuilder.loadTexts:valv_inv_ch_he.setStatus(_A)
if mibBuilder.loadTexts:valv_inv_ch_he.setUnits(_F)
class _Numero_term_h8_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Numero_term_h8_Type.__name__=_B
_Numero_term_h8_Object=MibScalar
numero_term_h8=_Numero_term_h8_Object((1,3,6,1,4,1,9839,2,1,3,42),_Numero_term_h8_Type())
numero_term_h8.setMaxAccess(_C)
if mibBuilder.loadTexts:numero_term_h8.setStatus(_A)
if mibBuilder.loadTexts:numero_term_h8.setUnits(_F)
class _High_temp_all_pc_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,150))
_High_temp_all_pc_Type.__name__=_B
_High_temp_all_pc_Object=MibScalar
high_temp_all_pc=_High_temp_all_pc_Object((1,3,6,1,4,1,9839,2,1,3,43),_High_temp_all_pc_Type())
high_temp_all_pc.setMaxAccess(_C)
if mibBuilder.loadTexts:high_temp_all_pc.setStatus(_A)
if mibBuilder.loadTexts:high_temp_all_pc.setUnits(_J)
class _Versione_sw_hg_Type(Integer32):defaultValue=13;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Versione_sw_hg_Type.__name__=_B
_Versione_sw_hg_Object=MibScalar
versione_sw_hg=_Versione_sw_hg_Object((1,3,6,1,4,1,9839,2,1,3,51),_Versione_sw_hg_Type())
versione_sw_hg.setMaxAccess(_D)
if mibBuilder.loadTexts:versione_sw_hg.setStatus(_A)
if mibBuilder.loadTexts:versione_sw_hg.setUnits(_E)
class _Rit_acc_comp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Rit_acc_comp_Type.__name__=_B
_Rit_acc_comp_Object=MibScalar
rit_acc_comp=_Rit_acc_comp_Object((1,3,6,1,4,1,9839,2,1,3,52),_Rit_acc_comp_Type())
rit_acc_comp.setMaxAccess(_D)
if mibBuilder.loadTexts:rit_acc_comp.setStatus(_A)
if mibBuilder.loadTexts:rit_acc_comp.setUnits(_H)
class _Rit_spegn_comp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Rit_spegn_comp_Type.__name__=_B
_Rit_spegn_comp_Object=MibScalar
rit_spegn_comp=_Rit_spegn_comp_Object((1,3,6,1,4,1,9839,2,1,3,53),_Rit_spegn_comp_Type())
rit_spegn_comp.setMaxAccess(_D)
if mibBuilder.loadTexts:rit_spegn_comp.setStatus(_A)
if mibBuilder.loadTexts:rit_spegn_comp.setUnits(_H)
class _Tempo_acc_pompa_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,150))
_Tempo_acc_pompa_Type.__name__=_B
_Tempo_acc_pompa_Object=MibScalar
tempo_acc_pompa=_Tempo_acc_pompa_Object((1,3,6,1,4,1,9839,2,1,3,56),_Tempo_acc_pompa_Type())
tempo_acc_pompa.setMaxAccess(_D)
if mibBuilder.loadTexts:tempo_acc_pompa.setStatus(_A)
if mibBuilder.loadTexts:tempo_acc_pompa.setUnits(_J)
mibBuilder.exportSymbols('CAREL-uchiller_cmp-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'uchiller_cmpMIB':uchiller_cmpMIB,'digitalObjects':digitalObjects,'est_inv':est_inv,'on_off_unita':on_off_unita,'allarme_hp':allarme_hp,'allarme_lp':allarme_lp,'all_flusso':all_flusso,'err_sonda_b3':err_sonda_b3,'err_sonda_b2':err_sonda_b2,'err_sonda_b1':err_sonda_b1,'err_eeprom_s':err_eeprom_s,'all_termin_off':all_termin_off,'sbrinamento_on':sbrinamento_on,'all_sbrinamento':all_sbrinamento,'all_antigelo':all_antigelo,'all_agelo_sonda':all_agelo_sonda,'all_sovratens':all_sovratens,'all_sottotens':all_sottotens,'stato_pompa':stato_pompa,'stato_compress':stato_compress,'stato_resists':stato_resists,'stato_valvola':stato_valvola,'stato_ventils':stato_ventils,'unita_misura':unita_misura,'out_per_fan_f1':out_per_fan_f1,'esecuz_sbrin_d1':esecuz_sbrin_d1,'def_time_tmp_d2':def_time_tmp_d2,'res_gelo_sbr_db':res_gelo_sbr_db,'en_sonda_res_a6':en_sonda_res_a6,'all_lp_sonda_p7':all_lp_sonda_p7,'en_id_on_off_h7':en_id_on_off_h7,'all_lp_comp_pa':all_lp_comp_pa,'en_set2_hc':en_set2_hc,'inv_est_inv_hd':inv_est_inv_hd,'sel_rele_all_hf':sel_rele_all_hf,'ab_estate_inv_h6':ab_estate_inv_h6,'rotaz_compr_r5':rotaz_compr_r5,'analogObjects':analogObjects,'sonda_b1':sonda_b1,'sonda_b2':sonda_b2,'sonda_b3':sonda_b3,'i_scala_press':i_scala_press,'f_scala_press':f_scala_press,'calibra_b1':calibra_b1,'calibra_b2':calibra_b2,'calibra_b3':calibra_b3,'setp_estate':setp_estate,'diff_estate':diff_estate,'setp_inverno':setp_inverno,'diff_inverno':diff_inverno,'min_set_est':min_set_est,'max_set_est':max_set_est,'min_set_inv':min_set_inv,'max_set_inv':max_set_inv,'tmin_vel_est_f5':tmin_vel_est_f5,'tmax_vel_est_f6':tmax_vel_est_f6,'tmin_vel_inv_f7':tmin_vel_inv_f7,'tmax_vel_inv_f8':tmax_vel_inv_f8,'toff_fan_est_f9':toff_fan_est_f9,'toff_fan_inv_fa':toff_fan_inv_fa,'parametro_d3':parametro_d3,'parametro_d4':parametro_d4,'set_al_agelo_a1':set_al_agelo_a1,'dif_al_agelo_a2':dif_al_agelo_a2,'set_res_gelo_a4':set_res_gelo_a4,'dif_res_gelo_a5':dif_res_gelo_a5,'lim_set_gelo_a7':lim_set_gelo_a7,'set_res_risc_a8':set_res_risc_a8,'dif_res_risc_a9':dif_res_risc_a9,'set_all_at_pb':set_all_at_pb,'sonda_b4':sonda_b4,'integerObjects':integerObjects,'velocita_vent':velocita_vent,'filtro_digitale':filtro_digitale,'tmin_on_comp_c1':tmin_on_comp_c1,'tmin_sp_comp_c2':tmin_sp_comp_c2,'time_2_acc_c3':time_2_acc_c3,'rit_on_comp_c6':rit_on_comp_c6,'rit_c_on_pmp_c7':rit_c_on_pmp_c7,'off_p_off_v_c8':off_p_off_v_c8,'contaore_c1_c9':contaore_c1_c9,'max_ore_comp_cb':max_ore_comp_cb,'ore_pmp_vent_cc':ore_pmp_vent_cc,'modo_vent_f2':modo_vent_f2,'min_volt_f3':min_volt_f3,'max_volt_f4':max_volt_f4,'t_spunto_v_fb':t_spunto_v_fb,'t_imp_triac_fc':t_imp_triac_fc,'t_min_on_def_d5':t_min_on_def_d5,'t_min_def_d6':t_min_def_d6,'t_max_def_d7':t_max_def_d7,'rit_tra_2def_d8':rit_tra_2def_d8,'wait_on_def_dc':wait_on_def_dc,'wait_end_def_dd':wait_end_def_dd,'rit_all_ag_a3':rit_all_ag_a3,'r_al_on_flux_p1':r_al_on_flux_p1,'r_al_rg_flux_p2':r_al_rg_flux_p2,'rit_all_lp_p3':rit_all_lp_p3,'t_buzzer_p4':t_buzzer_p4,'riprist_all_p5':riprist_all_p5,'selez_id1_p8':selez_id1_p8,'selez_id2_p9':selez_id2_p9,'modello_mac_h1':modello_mac_h1,'modo_pmp_vnt_h5':modo_pmp_vnt_h5,'blocca_tasti_h9':blocca_tasti_h9,'seradd':seradd,'passw_telec_hb':passw_telec_hb,'valv_inv_ch_he':valv_inv_ch_he,'numero_term_h8':numero_term_h8,'high_temp_all_pc':high_temp_all_pc,'versione_sw_hg':versione_sw_hg,'rit_acc_comp':rit_acc_comp,'rit_spegn_comp':rit_spegn_comp,'tempo_acc_pompa':tempo_acc_pompa})