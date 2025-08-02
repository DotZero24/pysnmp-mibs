_J='sec'
_I='deg.C'
_H='rH%'
_G='deg.C x 10'
_F='h'
_E='read-write'
_D='Integer32'
_C='N/A'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols('SNMPv2-MIB','sysContact','sysLocation','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
uncdz_MIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
if mibBuilder.loadTexts:uncdz_MIB.setRevisions(('2004-08-12 15:52',))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_C)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_C)
_Instruments_ObjectIdentity=ObjectIdentity
instruments=_Instruments_ObjectIdentity((1,3,6,1,4,1,9839,2))
_PCOWebInfo_ObjectIdentity=ObjectIdentity
pCOWebInfo=_PCOWebInfo_ObjectIdentity((1,3,6,1,4,1,9839,2,0))
_PCOStatusgroup_ObjectIdentity=ObjectIdentity
pCOStatusgroup=_PCOStatusgroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_PCOId1_Status_Type=Integer32
_PCOId1_Status_Object=MibScalar
pCOId1_Status=_PCOId1_Status_Object((1,3,6,1,4,1,9839,2,0,10,1),_PCOId1_Status_Type())
pCOId1_Status.setMaxAccess(_B)
if mibBuilder.loadTexts:pCOId1_Status.setStatus(_A)
if mibBuilder.loadTexts:pCOId1_Status.setUnits(_C)
_PCOErrorsNumbergroup_ObjectIdentity=ObjectIdentity
pCOErrorsNumbergroup=_PCOErrorsNumbergroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,11))
_PCOId1_ErrorsNumber_Type=Integer32
_PCOId1_ErrorsNumber_Object=MibScalar
pCOId1_ErrorsNumber=_PCOId1_ErrorsNumber_Object((1,3,6,1,4,1,9839,2,0,11,1),_PCOId1_ErrorsNumber_Type())
pCOId1_ErrorsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pCOId1_ErrorsNumber.setStatus(_A)
if mibBuilder.loadTexts:pCOId1_ErrorsNumber.setUnits(_C)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
_Vent_on_Type=Integer32
_Vent_on_Object=MibScalar
vent_on=_Vent_on_Object((1,3,6,1,4,1,9839,2,1,1,1),_Vent_on_Type())
vent_on.setMaxAccess(_B)
if mibBuilder.loadTexts:vent_on.setStatus(_A)
if mibBuilder.loadTexts:vent_on.setUnits(_C)
_Compressore1_Type=Integer32
_Compressore1_Object=MibScalar
compressore1=_Compressore1_Object((1,3,6,1,4,1,9839,2,1,1,2),_Compressore1_Type())
compressore1.setMaxAccess(_B)
if mibBuilder.loadTexts:compressore1.setStatus(_A)
if mibBuilder.loadTexts:compressore1.setUnits(_C)
_Compressore2_Type=Integer32
_Compressore2_Object=MibScalar
compressore2=_Compressore2_Object((1,3,6,1,4,1,9839,2,1,1,3),_Compressore2_Type())
compressore2.setMaxAccess(_B)
if mibBuilder.loadTexts:compressore2.setStatus(_A)
if mibBuilder.loadTexts:compressore2.setUnits(_C)
_Compressore3_Type=Integer32
_Compressore3_Object=MibScalar
compressore3=_Compressore3_Object((1,3,6,1,4,1,9839,2,1,1,4),_Compressore3_Type())
compressore3.setMaxAccess(_B)
if mibBuilder.loadTexts:compressore3.setStatus(_A)
if mibBuilder.loadTexts:compressore3.setUnits(_C)
_Compressore4_Type=Integer32
_Compressore4_Object=MibScalar
compressore4=_Compressore4_Object((1,3,6,1,4,1,9839,2,1,1,5),_Compressore4_Type())
compressore4.setMaxAccess(_B)
if mibBuilder.loadTexts:compressore4.setStatus(_A)
if mibBuilder.loadTexts:compressore4.setUnits(_C)
_Out_h1_Type=Integer32
_Out_h1_Object=MibScalar
out_h1=_Out_h1_Object((1,3,6,1,4,1,9839,2,1,1,6),_Out_h1_Type())
out_h1.setMaxAccess(_B)
if mibBuilder.loadTexts:out_h1.setStatus(_A)
if mibBuilder.loadTexts:out_h1.setUnits(_C)
_Out_h2_Type=Integer32
_Out_h2_Object=MibScalar
out_h2=_Out_h2_Object((1,3,6,1,4,1,9839,2,1,1,7),_Out_h2_Type())
out_h2.setMaxAccess(_B)
if mibBuilder.loadTexts:out_h2.setStatus(_A)
if mibBuilder.loadTexts:out_h2.setUnits(_C)
_Out_h3_Type=Integer32
_Out_h3_Object=MibScalar
out_h3=_Out_h3_Object((1,3,6,1,4,1,9839,2,1,1,8),_Out_h3_Type())
out_h3.setMaxAccess(_B)
if mibBuilder.loadTexts:out_h3.setStatus(_A)
if mibBuilder.loadTexts:out_h3.setUnits(_C)
_Gas_caldo_on_Type=Integer32
_Gas_caldo_on_Object=MibScalar
gas_caldo_on=_Gas_caldo_on_Object((1,3,6,1,4,1,9839,2,1,1,9),_Gas_caldo_on_Type())
gas_caldo_on.setMaxAccess(_B)
if mibBuilder.loadTexts:gas_caldo_on.setStatus(_A)
if mibBuilder.loadTexts:gas_caldo_on.setUnits(_C)
_On_deum_Type=Integer32
_On_deum_Object=MibScalar
on_deum=_On_deum_Object((1,3,6,1,4,1,9839,2,1,1,10),_On_deum_Type())
on_deum.setMaxAccess(_B)
if mibBuilder.loadTexts:on_deum.setStatus(_A)
if mibBuilder.loadTexts:on_deum.setUnits(_C)
_Power_Type=Integer32
_Power_Object=MibScalar
power=_Power_Object((1,3,6,1,4,1,9839,2,1,1,11),_Power_Type())
power.setMaxAccess(_B)
if mibBuilder.loadTexts:power.setStatus(_A)
if mibBuilder.loadTexts:power.setUnits(_C)
_Mal_access_Type=Integer32
_Mal_access_Object=MibScalar
mal_access=_Mal_access_Object((1,3,6,1,4,1,9839,2,1,1,12),_Mal_access_Type())
mal_access.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_access.setStatus(_A)
if mibBuilder.loadTexts:mal_access.setUnits(_C)
_Mal_ata_Type=Integer32
_Mal_ata_Object=MibScalar
mal_ata=_Mal_ata_Object((1,3,6,1,4,1,9839,2,1,1,13),_Mal_ata_Type())
mal_ata.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ata.setStatus(_A)
if mibBuilder.loadTexts:mal_ata.setUnits(_C)
_Mal_bta_Type=Integer32
_Mal_bta_Object=MibScalar
mal_bta=_Mal_bta_Object((1,3,6,1,4,1,9839,2,1,1,14),_Mal_bta_Type())
mal_bta.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_bta.setStatus(_A)
if mibBuilder.loadTexts:mal_bta.setUnits(_C)
_Mal_aua_Type=Integer32
_Mal_aua_Object=MibScalar
mal_aua=_Mal_aua_Object((1,3,6,1,4,1,9839,2,1,1,15),_Mal_aua_Type())
mal_aua.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_aua.setStatus(_A)
if mibBuilder.loadTexts:mal_aua.setUnits(_C)
_Mal_bua_Type=Integer32
_Mal_bua_Object=MibScalar
mal_bua=_Mal_bua_Object((1,3,6,1,4,1,9839,2,1,1,16),_Mal_bua_Type())
mal_bua.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_bua.setStatus(_A)
if mibBuilder.loadTexts:mal_bua.setUnits(_C)
_Mal_eap_Type=Integer32
_Mal_eap_Object=MibScalar
mal_eap=_Mal_eap_Object((1,3,6,1,4,1,9839,2,1,1,17),_Mal_eap_Type())
mal_eap.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_eap.setStatus(_A)
if mibBuilder.loadTexts:mal_eap.setUnits(_C)
_Mal_filter_Type=Integer32
_Mal_filter_Object=MibScalar
mal_filter=_Mal_filter_Object((1,3,6,1,4,1,9839,2,1,1,18),_Mal_filter_Type())
mal_filter.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_filter.setStatus(_A)
if mibBuilder.loadTexts:mal_filter.setUnits(_C)
_Mal_flood_Type=Integer32
_Mal_flood_Object=MibScalar
mal_flood=_Mal_flood_Object((1,3,6,1,4,1,9839,2,1,1,19),_Mal_flood_Type())
mal_flood.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_flood.setStatus(_A)
if mibBuilder.loadTexts:mal_flood.setUnits(_C)
_Mal_flux_Type=Integer32
_Mal_flux_Object=MibScalar
mal_flux=_Mal_flux_Object((1,3,6,1,4,1,9839,2,1,1,20),_Mal_flux_Type())
mal_flux.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_flux.setStatus(_A)
if mibBuilder.loadTexts:mal_flux.setUnits(_C)
_Mal_heater_Type=Integer32
_Mal_heater_Object=MibScalar
mal_heater=_Mal_heater_Object((1,3,6,1,4,1,9839,2,1,1,21),_Mal_heater_Type())
mal_heater.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_heater.setStatus(_A)
if mibBuilder.loadTexts:mal_heater.setUnits(_C)
_Mal_hp1_Type=Integer32
_Mal_hp1_Object=MibScalar
mal_hp1=_Mal_hp1_Object((1,3,6,1,4,1,9839,2,1,1,22),_Mal_hp1_Type())
mal_hp1.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_hp1.setStatus(_A)
if mibBuilder.loadTexts:mal_hp1.setUnits(_C)
_Mal_hp2_Type=Integer32
_Mal_hp2_Object=MibScalar
mal_hp2=_Mal_hp2_Object((1,3,6,1,4,1,9839,2,1,1,23),_Mal_hp2_Type())
mal_hp2.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_hp2.setStatus(_A)
if mibBuilder.loadTexts:mal_hp2.setUnits(_C)
_Mal_lp1_Type=Integer32
_Mal_lp1_Object=MibScalar
mal_lp1=_Mal_lp1_Object((1,3,6,1,4,1,9839,2,1,1,24),_Mal_lp1_Type())
mal_lp1.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_lp1.setStatus(_A)
if mibBuilder.loadTexts:mal_lp1.setUnits(_C)
_Mal_lp2_Type=Integer32
_Mal_lp2_Object=MibScalar
mal_lp2=_Mal_lp2_Object((1,3,6,1,4,1,9839,2,1,1,25),_Mal_lp2_Type())
mal_lp2.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_lp2.setStatus(_A)
if mibBuilder.loadTexts:mal_lp2.setUnits(_C)
_Mal_phase_Type=Integer32
_Mal_phase_Object=MibScalar
mal_phase=_Mal_phase_Object((1,3,6,1,4,1,9839,2,1,1,26),_Mal_phase_Type())
mal_phase.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_phase.setStatus(_A)
if mibBuilder.loadTexts:mal_phase.setUnits(_C)
_Mal_smoke_Type=Integer32
_Mal_smoke_Object=MibScalar
mal_smoke=_Mal_smoke_Object((1,3,6,1,4,1,9839,2,1,1,27),_Mal_smoke_Type())
mal_smoke.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_smoke.setStatus(_A)
if mibBuilder.loadTexts:mal_smoke.setUnits(_C)
_Mal_lan_Type=Integer32
_Mal_lan_Object=MibScalar
mal_lan=_Mal_lan_Object((1,3,6,1,4,1,9839,2,1,1,28),_Mal_lan_Type())
mal_lan.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_lan.setStatus(_A)
if mibBuilder.loadTexts:mal_lan.setUnits(_C)
_Mal_hcurr_Type=Integer32
_Mal_hcurr_Object=MibScalar
mal_hcurr=_Mal_hcurr_Object((1,3,6,1,4,1,9839,2,1,1,29),_Mal_hcurr_Type())
mal_hcurr.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_hcurr.setStatus(_A)
if mibBuilder.loadTexts:mal_hcurr.setUnits(_C)
_Mal_nopower_Type=Integer32
_Mal_nopower_Object=MibScalar
mal_nopower=_Mal_nopower_Object((1,3,6,1,4,1,9839,2,1,1,30),_Mal_nopower_Type())
mal_nopower.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_nopower.setStatus(_A)
if mibBuilder.loadTexts:mal_nopower.setUnits(_C)
_Mal_nowater_Type=Integer32
_Mal_nowater_Object=MibScalar
mal_nowater=_Mal_nowater_Object((1,3,6,1,4,1,9839,2,1,1,31),_Mal_nowater_Type())
mal_nowater.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_nowater.setStatus(_A)
if mibBuilder.loadTexts:mal_nowater.setUnits(_C)
_Mal_cw_dh_Type=Integer32
_Mal_cw_dh_Object=MibScalar
mal_cw_dh=_Mal_cw_dh_Object((1,3,6,1,4,1,9839,2,1,1,32),_Mal_cw_dh_Type())
mal_cw_dh.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_cw_dh.setStatus(_A)
if mibBuilder.loadTexts:mal_cw_dh.setUnits(_C)
_Mal_tc_cw_Type=Integer32
_Mal_tc_cw_Object=MibScalar
mal_tc_cw=_Mal_tc_cw_Object((1,3,6,1,4,1,9839,2,1,1,33),_Mal_tc_cw_Type())
mal_tc_cw.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_tc_cw.setStatus(_A)
if mibBuilder.loadTexts:mal_tc_cw.setUnits(_C)
_Mal_wflow_Type=Integer32
_Mal_wflow_Object=MibScalar
mal_wflow=_Mal_wflow_Object((1,3,6,1,4,1,9839,2,1,1,34),_Mal_wflow_Type())
mal_wflow.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_wflow.setStatus(_A)
if mibBuilder.loadTexts:mal_wflow.setUnits(_C)
_Mal_wht_Type=Integer32
_Mal_wht_Object=MibScalar
mal_wht=_Mal_wht_Object((1,3,6,1,4,1,9839,2,1,1,35),_Mal_wht_Type())
mal_wht.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_wht.setStatus(_A)
if mibBuilder.loadTexts:mal_wht.setUnits(_C)
_Mal_sonda_ta_Type=Integer32
_Mal_sonda_ta_Object=MibScalar
mal_sonda_ta=_Mal_sonda_ta_Object((1,3,6,1,4,1,9839,2,1,1,36),_Mal_sonda_ta_Type())
mal_sonda_ta.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_sonda_ta.setStatus(_A)
if mibBuilder.loadTexts:mal_sonda_ta.setUnits(_C)
_Mal_sonda_tac_Type=Integer32
_Mal_sonda_tac_Object=MibScalar
mal_sonda_tac=_Mal_sonda_tac_Object((1,3,6,1,4,1,9839,2,1,1,37),_Mal_sonda_tac_Type())
mal_sonda_tac.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_sonda_tac.setStatus(_A)
if mibBuilder.loadTexts:mal_sonda_tac.setUnits(_C)
_Mal_sonda_tc_Type=Integer32
_Mal_sonda_tc_Object=MibScalar
mal_sonda_tc=_Mal_sonda_tc_Object((1,3,6,1,4,1,9839,2,1,1,38),_Mal_sonda_tc_Type())
mal_sonda_tc.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_sonda_tc.setStatus(_A)
if mibBuilder.loadTexts:mal_sonda_tc.setUnits(_C)
_Mal_sonda_te_Type=Integer32
_Mal_sonda_te_Object=MibScalar
mal_sonda_te=_Mal_sonda_te_Object((1,3,6,1,4,1,9839,2,1,1,39),_Mal_sonda_te_Type())
mal_sonda_te.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_sonda_te.setStatus(_A)
if mibBuilder.loadTexts:mal_sonda_te.setUnits(_C)
_Mal_sonda_tm_Type=Integer32
_Mal_sonda_tm_Object=MibScalar
mal_sonda_tm=_Mal_sonda_tm_Object((1,3,6,1,4,1,9839,2,1,1,40),_Mal_sonda_tm_Type())
mal_sonda_tm.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_sonda_tm.setStatus(_A)
if mibBuilder.loadTexts:mal_sonda_tm.setUnits(_C)
_Mal_sonda_ua_Type=Integer32
_Mal_sonda_ua_Object=MibScalar
mal_sonda_ua=_Mal_sonda_ua_Object((1,3,6,1,4,1,9839,2,1,1,41),_Mal_sonda_ua_Type())
mal_sonda_ua.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_sonda_ua.setStatus(_A)
if mibBuilder.loadTexts:mal_sonda_ua.setUnits(_C)
_Mal_ore_compr1_Type=Integer32
_Mal_ore_compr1_Object=MibScalar
mal_ore_compr1=_Mal_ore_compr1_Object((1,3,6,1,4,1,9839,2,1,1,42),_Mal_ore_compr1_Type())
mal_ore_compr1.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_compr1.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_compr1.setUnits(_C)
_Mal_ore_compr2_Type=Integer32
_Mal_ore_compr2_Object=MibScalar
mal_ore_compr2=_Mal_ore_compr2_Object((1,3,6,1,4,1,9839,2,1,1,43),_Mal_ore_compr2_Type())
mal_ore_compr2.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_compr2.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_compr2.setUnits(_C)
_Mal_ore_compr3_Type=Integer32
_Mal_ore_compr3_Object=MibScalar
mal_ore_compr3=_Mal_ore_compr3_Object((1,3,6,1,4,1,9839,2,1,1,44),_Mal_ore_compr3_Type())
mal_ore_compr3.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_compr3.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_compr3.setUnits(_C)
_Mal_ore_compr4_Type=Integer32
_Mal_ore_compr4_Object=MibScalar
mal_ore_compr4=_Mal_ore_compr4_Object((1,3,6,1,4,1,9839,2,1,1,45),_Mal_ore_compr4_Type())
mal_ore_compr4.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_compr4.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_compr4.setUnits(_C)
_Mal_ore_filtro_Type=Integer32
_Mal_ore_filtro_Object=MibScalar
mal_ore_filtro=_Mal_ore_filtro_Object((1,3,6,1,4,1,9839,2,1,1,46),_Mal_ore_filtro_Type())
mal_ore_filtro.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_filtro.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_filtro.setUnits(_C)
_Mal_ore_risc1_Type=Integer32
_Mal_ore_risc1_Object=MibScalar
mal_ore_risc1=_Mal_ore_risc1_Object((1,3,6,1,4,1,9839,2,1,1,47),_Mal_ore_risc1_Type())
mal_ore_risc1.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_risc1.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_risc1.setUnits(_C)
_Mal_ore_risc2_Type=Integer32
_Mal_ore_risc2_Object=MibScalar
mal_ore_risc2=_Mal_ore_risc2_Object((1,3,6,1,4,1,9839,2,1,1,48),_Mal_ore_risc2_Type())
mal_ore_risc2.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_risc2.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_risc2.setUnits(_C)
_Mal_ore_umid_Type=Integer32
_Mal_ore_umid_Object=MibScalar
mal_ore_umid=_Mal_ore_umid_Object((1,3,6,1,4,1,9839,2,1,1,49),_Mal_ore_umid_Type())
mal_ore_umid.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_umid.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_umid.setUnits(_C)
_Mal_ore_unit_Type=Integer32
_Mal_ore_unit_Object=MibScalar
mal_ore_unit=_Mal_ore_unit_Object((1,3,6,1,4,1,9839,2,1,1,50),_Mal_ore_unit_Type())
mal_ore_unit.setMaxAccess(_B)
if mibBuilder.loadTexts:mal_ore_unit.setStatus(_A)
if mibBuilder.loadTexts:mal_ore_unit.setUnits(_C)
_Glb_al_Type=Integer32
_Glb_al_Object=MibScalar
glb_al=_Glb_al_Object((1,3,6,1,4,1,9839,2,1,1,51),_Glb_al_Type())
glb_al.setMaxAccess(_B)
if mibBuilder.loadTexts:glb_al.setStatus(_A)
if mibBuilder.loadTexts:glb_al.setUnits(_C)
_Or_al_2lev_Type=Integer32
_Or_al_2lev_Object=MibScalar
or_al_2lev=_Or_al_2lev_Object((1,3,6,1,4,1,9839,2,1,1,52),_Or_al_2lev_Type())
or_al_2lev.setMaxAccess(_B)
if mibBuilder.loadTexts:or_al_2lev.setStatus(_A)
if mibBuilder.loadTexts:or_al_2lev.setUnits(_C)
_Range_t_ext_Type=Integer32
_Range_t_ext_Object=MibScalar
range_t_ext=_Range_t_ext_Object((1,3,6,1,4,1,9839,2,1,1,53),_Range_t_ext_Type())
range_t_ext.setMaxAccess(_B)
if mibBuilder.loadTexts:range_t_ext.setStatus(_A)
if mibBuilder.loadTexts:range_t_ext.setUnits(_C)
_Range_t_circ_Type=Integer32
_Range_t_circ_Object=MibScalar
range_t_circ=_Range_t_circ_Object((1,3,6,1,4,1,9839,2,1,1,54),_Range_t_circ_Type())
range_t_circ.setMaxAccess(_B)
if mibBuilder.loadTexts:range_t_circ.setStatus(_A)
if mibBuilder.loadTexts:range_t_circ.setUnits(_C)
_Range_t_man_Type=Integer32
_Range_t_man_Object=MibScalar
range_t_man=_Range_t_man_Object((1,3,6,1,4,1,9839,2,1,1,55),_Range_t_man_Type())
range_t_man.setMaxAccess(_B)
if mibBuilder.loadTexts:range_t_man.setStatus(_A)
if mibBuilder.loadTexts:range_t_man.setUnits(_C)
_Range_t_ac_Type=Integer32
_Range_t_ac_Object=MibScalar
range_t_ac=_Range_t_ac_Object((1,3,6,1,4,1,9839,2,1,1,56),_Range_t_ac_Type())
range_t_ac.setMaxAccess(_B)
if mibBuilder.loadTexts:range_t_ac.setStatus(_A)
if mibBuilder.loadTexts:range_t_ac.setUnits(_C)
_Umid_al_Type=Integer32
_Umid_al_Object=MibScalar
umid_al=_Umid_al_Object((1,3,6,1,4,1,9839,2,1,1,57),_Umid_al_Type())
umid_al.setMaxAccess(_B)
if mibBuilder.loadTexts:umid_al.setStatus(_A)
if mibBuilder.loadTexts:umid_al.setUnits(_C)
_Range_u_amb_Type=Integer32
_Range_u_amb_Object=MibScalar
range_u_amb=_Range_u_amb_Object((1,3,6,1,4,1,9839,2,1,1,58),_Range_u_amb_Type())
range_u_amb.setMaxAccess(_B)
if mibBuilder.loadTexts:range_u_amb.setStatus(_A)
if mibBuilder.loadTexts:range_u_amb.setUnits(_C)
class _K_syson_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_K_syson_Type.__name__=_D
_K_syson_Object=MibScalar
k_syson=_K_syson_Object((1,3,6,1,4,1,9839,2,1,1,60),_K_syson_Type())
k_syson.setMaxAccess(_E)
if mibBuilder.loadTexts:k_syson.setStatus(_A)
if mibBuilder.loadTexts:k_syson.setUnits(_C)
class _Xs_res_al_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Xs_res_al_Type.__name__=_D
_Xs_res_al_Object=MibScalar
xs_res_al=_Xs_res_al_Object((1,3,6,1,4,1,9839,2,1,1,61),_Xs_res_al_Type())
xs_res_al.setMaxAccess(_E)
if mibBuilder.loadTexts:xs_res_al.setStatus(_A)
if mibBuilder.loadTexts:xs_res_al.setUnits(_C)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sleep_mode_Type.__name__=_D
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,9839,2,1,1,63),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:sleep_mode.setStatus(_A)
if mibBuilder.loadTexts:sleep_mode.setUnits(_C)
class _Test_sm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Test_sm_Type.__name__=_D
_Test_sm_Object=MibScalar
test_sm=_Test_sm_Object((1,3,6,1,4,1,9839,2,1,1,64),_Test_sm_Type())
test_sm.setMaxAccess(_E)
if mibBuilder.loadTexts:test_sm.setStatus(_A)
if mibBuilder.loadTexts:test_sm.setUnits(_C)
class _Ab_mediath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ab_mediath_Type.__name__=_D
_Ab_mediath_Object=MibScalar
ab_mediath=_Ab_mediath_Object((1,3,6,1,4,1,9839,2,1,1,65),_Ab_mediath_Type())
ab_mediath.setMaxAccess(_E)
if mibBuilder.loadTexts:ab_mediath.setStatus(_A)
if mibBuilder.loadTexts:ab_mediath.setUnits(_C)
class _Ustdby1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ustdby1_2_Type.__name__=_D
_Ustdby1_2_Object=MibScalar
ustdby1_2=_Ustdby1_2_Object((1,3,6,1,4,1,9839,2,1,1,66),_Ustdby1_2_Type())
ustdby1_2.setMaxAccess(_E)
if mibBuilder.loadTexts:ustdby1_2.setStatus(_A)
if mibBuilder.loadTexts:ustdby1_2.setUnits(_C)
_Emerg_Type=Integer32
_Emerg_Object=MibScalar
emerg=_Emerg_Object((1,3,6,1,4,1,9839,2,1,1,67),_Emerg_Type())
emerg.setMaxAccess(_B)
if mibBuilder.loadTexts:emerg.setStatus(_A)
if mibBuilder.loadTexts:emerg.setUnits(_C)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
_Temp_amb_Type=Integer32
_Temp_amb_Object=MibScalar
temp_amb=_Temp_amb_Object((1,3,6,1,4,1,9839,2,1,2,1),_Temp_amb_Type())
temp_amb.setMaxAccess(_B)
if mibBuilder.loadTexts:temp_amb.setStatus(_A)
if mibBuilder.loadTexts:temp_amb.setUnits(_C)
_Temp_ext_Type=Integer32
_Temp_ext_Object=MibScalar
temp_ext=_Temp_ext_Object((1,3,6,1,4,1,9839,2,1,2,2),_Temp_ext_Type())
temp_ext.setMaxAccess(_B)
if mibBuilder.loadTexts:temp_ext.setStatus(_A)
if mibBuilder.loadTexts:temp_ext.setUnits(_G)
_Temp_mand_Type=Integer32
_Temp_mand_Object=MibScalar
temp_mand=_Temp_mand_Object((1,3,6,1,4,1,9839,2,1,2,3),_Temp_mand_Type())
temp_mand.setMaxAccess(_B)
if mibBuilder.loadTexts:temp_mand.setStatus(_A)
if mibBuilder.loadTexts:temp_mand.setUnits(_G)
_Temp_circ_Type=Integer32
_Temp_circ_Object=MibScalar
temp_circ=_Temp_circ_Object((1,3,6,1,4,1,9839,2,1,2,4),_Temp_circ_Type())
temp_circ.setMaxAccess(_B)
if mibBuilder.loadTexts:temp_circ.setStatus(_A)
if mibBuilder.loadTexts:temp_circ.setUnits(_G)
_Temp_ac_Type=Integer32
_Temp_ac_Object=MibScalar
temp_ac=_Temp_ac_Object((1,3,6,1,4,1,9839,2,1,2,5),_Temp_ac_Type())
temp_ac.setMaxAccess(_B)
if mibBuilder.loadTexts:temp_ac.setStatus(_A)
if mibBuilder.loadTexts:temp_ac.setUnits(_G)
_Umid_amb_Type=Integer32
_Umid_amb_Object=MibScalar
umid_amb=_Umid_amb_Object((1,3,6,1,4,1,9839,2,1,2,6),_Umid_amb_Type())
umid_amb.setMaxAccess(_B)
if mibBuilder.loadTexts:umid_amb.setStatus(_A)
if mibBuilder.loadTexts:umid_amb.setUnits('rH% x 10')
class _T_set_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_set_Type.__name__=_D
_T_set_Object=MibScalar
t_set=_T_set_Object((1,3,6,1,4,1,9839,2,1,2,7),_T_set_Type())
t_set.setMaxAccess(_E)
if mibBuilder.loadTexts:t_set.setStatus(_A)
if mibBuilder.loadTexts:t_set.setUnits(_G)
class _T_diff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_diff_Type.__name__=_D
_T_diff_Object=MibScalar
t_diff=_T_diff_Object((1,3,6,1,4,1,9839,2,1,2,8),_T_diff_Type())
t_diff.setMaxAccess(_E)
if mibBuilder.loadTexts:t_diff.setStatus(_A)
if mibBuilder.loadTexts:t_diff.setUnits(_G)
class _T_set_c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_set_c_Type.__name__=_D
_T_set_c_Object=MibScalar
t_set_c=_T_set_c_Object((1,3,6,1,4,1,9839,2,1,2,9),_T_set_c_Type())
t_set_c.setMaxAccess(_E)
if mibBuilder.loadTexts:t_set_c.setStatus(_A)
if mibBuilder.loadTexts:t_set_c.setUnits(_G)
class _T_diff_c_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_diff_c_Type.__name__=_D
_T_diff_c_Object=MibScalar
t_diff_c=_T_diff_c_Object((1,3,6,1,4,1,9839,2,1,2,10),_T_diff_c_Type())
t_diff_c.setMaxAccess(_E)
if mibBuilder.loadTexts:t_diff_c.setStatus(_A)
if mibBuilder.loadTexts:t_diff_c.setUnits(_G)
class _Ht_set_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ht_set_Type.__name__=_D
_Ht_set_Object=MibScalar
ht_set=_Ht_set_Object((1,3,6,1,4,1,9839,2,1,2,11),_Ht_set_Type())
ht_set.setMaxAccess(_E)
if mibBuilder.loadTexts:ht_set.setStatus(_A)
if mibBuilder.loadTexts:ht_set.setUnits(_I)
class _Lt_set_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lt_set_Type.__name__=_D
_Lt_set_Object=MibScalar
lt_set=_Lt_set_Object((1,3,6,1,4,1,9839,2,1,2,12),_Lt_set_Type())
lt_set.setMaxAccess(_E)
if mibBuilder.loadTexts:lt_set.setStatus(_A)
if mibBuilder.loadTexts:lt_set.setUnits(_I)
class _T_set_sm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_set_sm_Type.__name__=_D
_T_set_sm_Object=MibScalar
t_set_sm=_T_set_sm_Object((1,3,6,1,4,1,9839,2,1,2,13),_T_set_sm_Type())
t_set_sm.setMaxAccess(_E)
if mibBuilder.loadTexts:t_set_sm.setStatus(_A)
if mibBuilder.loadTexts:t_set_sm.setUnits(_C)
class _T_set_c_sm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_set_c_sm_Type.__name__=_D
_T_set_c_sm_Object=MibScalar
t_set_c_sm=_T_set_c_sm_Object((1,3,6,1,4,1,9839,2,1,2,14),_T_set_c_sm_Type())
t_set_c_sm.setMaxAccess(_E)
if mibBuilder.loadTexts:t_set_c_sm.setStatus(_A)
if mibBuilder.loadTexts:t_set_c_sm.setUnits(_C)
class _T_cw_dh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_cw_dh_Type.__name__=_D
_T_cw_dh_Object=MibScalar
t_cw_dh=_T_cw_dh_Object((1,3,6,1,4,1,9839,2,1,2,15),_T_cw_dh_Type())
t_cw_dh.setMaxAccess(_E)
if mibBuilder.loadTexts:t_cw_dh.setStatus(_A)
if mibBuilder.loadTexts:t_cw_dh.setUnits(_C)
class _Htset_cw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Htset_cw_Type.__name__=_D
_Htset_cw_Object=MibScalar
htset_cw=_Htset_cw_Object((1,3,6,1,4,1,9839,2,1,2,16),_Htset_cw_Type())
htset_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:htset_cw.setStatus(_A)
if mibBuilder.loadTexts:htset_cw.setUnits(_C)
class _T_set_cw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_set_cw_Type.__name__=_D
_T_set_cw_Object=MibScalar
t_set_cw=_T_set_cw_Object((1,3,6,1,4,1,9839,2,1,2,17),_T_set_cw_Type())
t_set_cw.setMaxAccess(_E)
if mibBuilder.loadTexts:t_set_cw.setStatus(_A)
if mibBuilder.loadTexts:t_set_cw.setUnits(_C)
class _T_rc_es_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_rc_es_Type.__name__=_D
_T_rc_es_Object=MibScalar
t_rc_es=_T_rc_es_Object((1,3,6,1,4,1,9839,2,1,2,18),_T_rc_es_Type())
t_rc_es.setMaxAccess(_E)
if mibBuilder.loadTexts:t_rc_es.setStatus(_A)
if mibBuilder.loadTexts:t_rc_es.setUnits(_C)
class _T_rc_est_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_rc_est_Type.__name__=_D
_T_rc_est_Object=MibScalar
t_rc_est=_T_rc_est_Object((1,3,6,1,4,1,9839,2,1,2,19),_T_rc_est_Type())
t_rc_est.setMaxAccess(_E)
if mibBuilder.loadTexts:t_rc_est.setStatus(_A)
if mibBuilder.loadTexts:t_rc_est.setUnits(_C)
_Rampa_valv_Type=Integer32
_Rampa_valv_Object=MibScalar
rampa_valv=_Rampa_valv_Object((1,3,6,1,4,1,9839,2,1,2,20),_Rampa_valv_Type())
rampa_valv.setMaxAccess(_B)
if mibBuilder.loadTexts:rampa_valv.setStatus(_A)
if mibBuilder.loadTexts:rampa_valv.setUnits(_C)
_Anaout2_Type=Integer32
_Anaout2_Object=MibScalar
anaout2=_Anaout2_Object((1,3,6,1,4,1,9839,2,1,2,21),_Anaout2_Type())
anaout2.setMaxAccess(_B)
if mibBuilder.loadTexts:anaout2.setStatus(_A)
if mibBuilder.loadTexts:anaout2.setUnits(_C)
_Steam_production_Type=Integer32
_Steam_production_Object=MibScalar
steam_production=_Steam_production_Object((1,3,6,1,4,1,9839,2,1,2,22),_Steam_production_Type())
steam_production.setMaxAccess(_B)
if mibBuilder.loadTexts:steam_production.setStatus(_A)
if mibBuilder.loadTexts:steam_production.setUnits('kg/h x 10')
class _T_set_lm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_set_lm_Type.__name__=_D
_T_set_lm_Object=MibScalar
t_set_lm=_T_set_lm_Object((1,3,6,1,4,1,9839,2,1,2,23),_T_set_lm_Type())
t_set_lm.setMaxAccess(_E)
if mibBuilder.loadTexts:t_set_lm.setStatus(_A)
if mibBuilder.loadTexts:t_set_lm.setUnits(_I)
class _Delta_lm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Delta_lm_Type.__name__=_D
_Delta_lm_Object=MibScalar
delta_lm=_Delta_lm_Object((1,3,6,1,4,1,9839,2,1,2,24),_Delta_lm_Type())
delta_lm.setMaxAccess(_E)
if mibBuilder.loadTexts:delta_lm.setStatus(_A)
if mibBuilder.loadTexts:delta_lm.setUnits(_G)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
_Ore_filtro_Type=Integer32
_Ore_filtro_Object=MibScalar
ore_filtro=_Ore_filtro_Object((1,3,6,1,4,1,9839,2,1,3,1),_Ore_filtro_Type())
ore_filtro.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_filtro.setStatus(_A)
if mibBuilder.loadTexts:ore_filtro.setUnits(_F)
_Ore_unit_Type=Integer32
_Ore_unit_Object=MibScalar
ore_unit=_Ore_unit_Object((1,3,6,1,4,1,9839,2,1,3,2),_Ore_unit_Type())
ore_unit.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_unit.setStatus(_A)
if mibBuilder.loadTexts:ore_unit.setUnits(_F)
_Ore_compr1_Type=Integer32
_Ore_compr1_Object=MibScalar
ore_compr1=_Ore_compr1_Object((1,3,6,1,4,1,9839,2,1,3,3),_Ore_compr1_Type())
ore_compr1.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_compr1.setStatus(_A)
if mibBuilder.loadTexts:ore_compr1.setUnits(_F)
_Ore_compr2_Type=Integer32
_Ore_compr2_Object=MibScalar
ore_compr2=_Ore_compr2_Object((1,3,6,1,4,1,9839,2,1,3,4),_Ore_compr2_Type())
ore_compr2.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_compr2.setStatus(_A)
if mibBuilder.loadTexts:ore_compr2.setUnits(_F)
_Ore_compr3_Type=Integer32
_Ore_compr3_Object=MibScalar
ore_compr3=_Ore_compr3_Object((1,3,6,1,4,1,9839,2,1,3,5),_Ore_compr3_Type())
ore_compr3.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_compr3.setStatus(_A)
if mibBuilder.loadTexts:ore_compr3.setUnits(_F)
_Ore_compr4_Type=Integer32
_Ore_compr4_Object=MibScalar
ore_compr4=_Ore_compr4_Object((1,3,6,1,4,1,9839,2,1,3,6),_Ore_compr4_Type())
ore_compr4.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_compr4.setStatus(_A)
if mibBuilder.loadTexts:ore_compr4.setUnits(_F)
_Ore_heat1_Type=Integer32
_Ore_heat1_Object=MibScalar
ore_heat1=_Ore_heat1_Object((1,3,6,1,4,1,9839,2,1,3,7),_Ore_heat1_Type())
ore_heat1.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_heat1.setStatus(_A)
if mibBuilder.loadTexts:ore_heat1.setUnits(_F)
_Ore_heat2_Type=Integer32
_Ore_heat2_Object=MibScalar
ore_heat2=_Ore_heat2_Object((1,3,6,1,4,1,9839,2,1,3,8),_Ore_heat2_Type())
ore_heat2.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_heat2.setStatus(_A)
if mibBuilder.loadTexts:ore_heat2.setUnits(_F)
_Ore_umid_Type=Integer32
_Ore_umid_Object=MibScalar
ore_umid=_Ore_umid_Object((1,3,6,1,4,1,9839,2,1,3,9),_Ore_umid_Type())
ore_umid.setMaxAccess(_B)
if mibBuilder.loadTexts:ore_umid.setStatus(_A)
if mibBuilder.loadTexts:ore_umid.setUnits(_F)
class _Hdiff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hdiff_Type.__name__=_D
_Hdiff_Object=MibScalar
hdiff=_Hdiff_Object((1,3,6,1,4,1,9839,2,1,3,12),_Hdiff_Type())
hdiff.setMaxAccess(_E)
if mibBuilder.loadTexts:hdiff.setStatus(_A)
if mibBuilder.loadTexts:hdiff.setUnits(_H)
class _Hu_diff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hu_diff_Type.__name__=_D
_Hu_diff_Object=MibScalar
hu_diff=_Hu_diff_Object((1,3,6,1,4,1,9839,2,1,3,13),_Hu_diff_Type())
hu_diff.setMaxAccess(_E)
if mibBuilder.loadTexts:hu_diff.setStatus(_A)
if mibBuilder.loadTexts:hu_diff.setUnits(_H)
class _Hh_set_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hh_set_Type.__name__=_D
_Hh_set_Object=MibScalar
hh_set=_Hh_set_Object((1,3,6,1,4,1,9839,2,1,3,14),_Hh_set_Type())
hh_set.setMaxAccess(_E)
if mibBuilder.loadTexts:hh_set.setStatus(_A)
if mibBuilder.loadTexts:hh_set.setUnits(_H)
class _Lh_set_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lh_set_Type.__name__=_D
_Lh_set_Object=MibScalar
lh_set=_Lh_set_Object((1,3,6,1,4,1,9839,2,1,3,15),_Lh_set_Type())
lh_set.setMaxAccess(_E)
if mibBuilder.loadTexts:lh_set.setStatus(_A)
if mibBuilder.loadTexts:lh_set.setUnits(_H)
class _Hset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hset_Type.__name__=_D
_Hset_Object=MibScalar
hset=_Hset_Object((1,3,6,1,4,1,9839,2,1,3,16),_Hset_Type())
hset.setMaxAccess(_E)
if mibBuilder.loadTexts:hset.setStatus(_A)
if mibBuilder.loadTexts:hset.setUnits(_H)
class _Hset_sm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hset_sm_Type.__name__=_D
_Hset_sm_Object=MibScalar
hset_sm=_Hset_sm_Object((1,3,6,1,4,1,9839,2,1,3,17),_Hset_sm_Type())
hset_sm.setMaxAccess(_E)
if mibBuilder.loadTexts:hset_sm.setStatus(_A)
if mibBuilder.loadTexts:hset_sm.setUnits(_H)
class _Hu_set_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hu_set_Type.__name__=_D
_Hu_set_Object=MibScalar
hu_set=_Hu_set_Object((1,3,6,1,4,1,9839,2,1,3,18),_Hu_set_Type())
hu_set.setMaxAccess(_E)
if mibBuilder.loadTexts:hu_set.setStatus(_A)
if mibBuilder.loadTexts:hu_set.setUnits(_H)
class _Hu_set_sm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hu_set_sm_Type.__name__=_D
_Hu_set_sm_Object=MibScalar
hu_set_sm=_Hu_set_sm_Object((1,3,6,1,4,1,9839,2,1,3,19),_Hu_set_sm_Type())
hu_set_sm.setMaxAccess(_E)
if mibBuilder.loadTexts:hu_set_sm.setStatus(_A)
if mibBuilder.loadTexts:hu_set_sm.setUnits(_H)
class _Restart_delay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Restart_delay_Type.__name__=_D
_Restart_delay_Object=MibScalar
restart_delay=_Restart_delay_Object((1,3,6,1,4,1,9839,2,1,3,20),_Restart_delay_Type())
restart_delay.setMaxAccess(_E)
if mibBuilder.loadTexts:restart_delay.setStatus(_A)
if mibBuilder.loadTexts:restart_delay.setUnits(_J)
class _Regul_delay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Regul_delay_Type.__name__=_D
_Regul_delay_Object=MibScalar
regul_delay=_Regul_delay_Object((1,3,6,1,4,1,9839,2,1,3,21),_Regul_delay_Type())
regul_delay.setMaxAccess(_E)
if mibBuilder.loadTexts:regul_delay.setStatus(_A)
if mibBuilder.loadTexts:regul_delay.setUnits(_J)
class _Time_lowp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Time_lowp_Type.__name__=_D
_Time_lowp_Object=MibScalar
time_lowp=_Time_lowp_Object((1,3,6,1,4,1,9839,2,1,3,22),_Time_lowp_Type())
time_lowp.setMaxAccess(_E)
if mibBuilder.loadTexts:time_lowp.setStatus(_A)
if mibBuilder.loadTexts:time_lowp.setUnits(_J)
class _Alarm_delay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Alarm_delay_Type.__name__=_D
_Alarm_delay_Object=MibScalar
alarm_delay=_Alarm_delay_Object((1,3,6,1,4,1,9839,2,1,3,23),_Alarm_delay_Type())
alarm_delay.setMaxAccess(_E)
if mibBuilder.loadTexts:alarm_delay.setStatus(_A)
if mibBuilder.loadTexts:alarm_delay.setUnits('m')
class _Exc_time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Exc_time_Type.__name__=_D
_Exc_time_Object=MibScalar
exc_time=_Exc_time_Object((1,3,6,1,4,1,9839,2,1,3,24),_Exc_time_Type())
exc_time.setMaxAccess(_E)
if mibBuilder.loadTexts:exc_time.setStatus(_A)
if mibBuilder.loadTexts:exc_time.setUnits('m')
class _T_std_by_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_T_std_by_Type.__name__=_D
_T_std_by_Object=MibScalar
t_std_by=_T_std_by_Object((1,3,6,1,4,1,9839,2,1,3,25),_T_std_by_Type())
t_std_by.setMaxAccess(_E)
if mibBuilder.loadTexts:t_std_by.setStatus(_A)
if mibBuilder.loadTexts:t_std_by.setUnits(_F)
class _Lan_unit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lan_unit_Type.__name__=_D
_Lan_unit_Object=MibScalar
lan_unit=_Lan_unit_Object((1,3,6,1,4,1,9839,2,1,3,27),_Lan_unit_Type())
lan_unit.setMaxAccess(_E)
if mibBuilder.loadTexts:lan_unit.setStatus(_A)
if mibBuilder.loadTexts:lan_unit.setUnits('n')
class _Ciclo_sm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ciclo_sm_Type.__name__=_D
_Ciclo_sm_Object=MibScalar
ciclo_sm=_Ciclo_sm_Object((1,3,6,1,4,1,9839,2,1,3,28),_Ciclo_sm_Type())
ciclo_sm.setMaxAccess(_E)
if mibBuilder.loadTexts:ciclo_sm.setStatus(_A)
if mibBuilder.loadTexts:ciclo_sm.setUnits('m')
mibBuilder.exportSymbols('UNCDZ-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'pCOWebInfo':pCOWebInfo,'pCOStatusgroup':pCOStatusgroup,'pCOId1-Status':pCOId1_Status,'pCOErrorsNumbergroup':pCOErrorsNumbergroup,'pCOId1-ErrorsNumber':pCOId1_ErrorsNumber,'uncdz-MIB':uncdz_MIB,'digitalObjects':digitalObjects,'vent-on':vent_on,'compressore1':compressore1,'compressore2':compressore2,'compressore3':compressore3,'compressore4':compressore4,'out-h1':out_h1,'out-h2':out_h2,'out-h3':out_h3,'gas-caldo-on':gas_caldo_on,'on-deum':on_deum,'power':power,'mal-access':mal_access,'mal-ata':mal_ata,'mal-bta':mal_bta,'mal-aua':mal_aua,'mal-bua':mal_bua,'mal-eap':mal_eap,'mal-filter':mal_filter,'mal-flood':mal_flood,'mal-flux':mal_flux,'mal-heater':mal_heater,'mal-hp1':mal_hp1,'mal-hp2':mal_hp2,'mal-lp1':mal_lp1,'mal-lp2':mal_lp2,'mal-phase':mal_phase,'mal-smoke':mal_smoke,'mal-lan':mal_lan,'mal-hcurr':mal_hcurr,'mal-nopower':mal_nopower,'mal-nowater':mal_nowater,'mal-cw-dh':mal_cw_dh,'mal-tc-cw':mal_tc_cw,'mal-wflow':mal_wflow,'mal-wht':mal_wht,'mal-sonda-ta':mal_sonda_ta,'mal-sonda-tac':mal_sonda_tac,'mal-sonda-tc':mal_sonda_tc,'mal-sonda-te':mal_sonda_te,'mal-sonda-tm':mal_sonda_tm,'mal-sonda-ua':mal_sonda_ua,'mal-ore-compr1':mal_ore_compr1,'mal-ore-compr2':mal_ore_compr2,'mal-ore-compr3':mal_ore_compr3,'mal-ore-compr4':mal_ore_compr4,'mal-ore-filtro':mal_ore_filtro,'mal-ore-risc1':mal_ore_risc1,'mal-ore-risc2':mal_ore_risc2,'mal-ore-umid':mal_ore_umid,'mal-ore-unit':mal_ore_unit,'glb-al':glb_al,'or-al-2lev':or_al_2lev,'range-t-ext':range_t_ext,'range-t-circ':range_t_circ,'range-t-man':range_t_man,'range-t-ac':range_t_ac,'umid-al':umid_al,'range-u-amb':range_u_amb,'k-syson':k_syson,'xs-res-al':xs_res_al,'sleep-mode':sleep_mode,'test-sm':test_sm,'ab-mediath':ab_mediath,'ustdby1-2':ustdby1_2,'emerg':emerg,'analogObjects':analogObjects,'temp-amb':temp_amb,'temp-ext':temp_ext,'temp-mand':temp_mand,'temp-circ':temp_circ,'temp-ac':temp_ac,'umid-amb':umid_amb,'t-set':t_set,'t-diff':t_diff,'t-set-c':t_set_c,'t-diff-c':t_diff_c,'ht-set':ht_set,'lt-set':lt_set,'t-set-sm':t_set_sm,'t-set-c-sm':t_set_c_sm,'t-cw-dh':t_cw_dh,'htset-cw':htset_cw,'t-set-cw':t_set_cw,'t-rc-es':t_rc_es,'t-rc-est':t_rc_est,'rampa-valv':rampa_valv,'anaout2':anaout2,'steam-production':steam_production,'t-set-lm':t_set_lm,'delta-lm':delta_lm,'integerObjects':integerObjects,'ore-filtro':ore_filtro,'ore-unit':ore_unit,'ore-compr1':ore_compr1,'ore-compr2':ore_compr2,'ore-compr3':ore_compr3,'ore-compr4':ore_compr4,'ore-heat1':ore_heat1,'ore-heat2':ore_heat2,'ore-umid':ore_umid,'hdiff':hdiff,'hu-diff':hu_diff,'hh-set':hh_set,'lh-set':lh_set,'hset':hset,'hset-sm':hset_sm,'hu-set':hu_set,'hu-set-sm':hu_set_sm,'restart-delay':restart_delay,'regul-delay':regul_delay,'time-lowp':time_lowp,'alarm-delay':alarm_delay,'exc-time':exc_time,'t-std-by':t_std_by,'lan-unit':lan_unit,'ciclo-sm':ciclo_sm})