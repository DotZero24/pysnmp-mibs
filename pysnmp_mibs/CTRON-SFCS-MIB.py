_AQ='sfcsProxyReadANIMIndex'
_AP='sfcsProxyTransANIMIndex'
_AO='sfcsProxyConfigANIMIndex'
_AN='sfcsBuffPrioPriority'
_AM='sfcsBuffPrioPortIndex'
_AL='sfcsBwPortPoolTrapMgmtPoolIndex'
_AK='sfcsBwPortPoolTrapMgmtIndex'
_AJ='sfcsBwPortPoolStatsPoolIndex'
_AI='sfcsBwPortPoolStatsIndex'
_AH='sfcsBwPortPoolLimitsPoolIndex'
_AG='sfcsBwPortPoolLimitsIndex'
_AF='sfcsBwPortsIndex'
_AE='sfcsBwNimsIndex'
_AD='sfcsCTMQueueStatsInterfaceIndex'
_AC='sfcsCTMQueueConfigInterfaceIndex'
_AB='sfcsCTMInterfaceStatsInterfaceIndex'
_AA='sfcsCTMInterfaceConfigInterfaceIndex'
_A9='sfcsCnxStatsCrossConnectHighVci'
_A8='sfcsCnxStatsCrossConnectHighVpi'
_A7='sfcsCnxStatsCrossConnectHighIfIndex'
_A6='sfcsCnxStatsCrossConnectLowVci'
_A5='sfcsCnxStatsCrossConnectLowVpi'
_A4='sfcsCnxStatsCrossConnectLowIfIndex'
_A3='sfcsCnxStatsCrossConnectIndex'
_A2='sfcsCnxCfgCrossConnectHighVci'
_A1='sfcsCnxCfgCrossConnectHighVpi'
_A0='sfcsCnxCfgCrossConnectHighIfIndex'
_z='sfcsCnxCfgCrossConnectLowVci'
_y='sfcsCnxCfgCrossConnectLowVpi'
_x='sfcsCnxCfgCrossConnectLowIfIndex'
_w='sfcsCnxCfgCrossConnectIndex'
_v='sfcsQueueStatsInterfaceIndex'
_u='sfcsQueueConfigInterfaceIndex'
_t='sfcsInterfaceStatsInterfaceIndex'
_s='host-ctl-port'
_r='host-mgmt-port'
_q='network-port'
_p='access-port'
_o='sfcsInterfaceConfigInterfaceIndex'
_n='sfcsANIMPicIndex'
_m='sfcsANIMStatsANIMIndex'
_l='local-anim-clock'
_k='sfcsANIMConfigANIMIndex'
_j='sfcsPacketDiscardEngineSlotIndex'
_i='sfcsStatsEngineSlotIndex'
_h='sfcsUPCSlotIndex'
_g='sfcsStatusSlotIndex'
_f='sfcsConfigSlotIndex'
_e='invalid-config'
_d='pending-enable'
_c='pending-disable'
_b='atmVcCrossConnectLowVpi'
_a='atmVcCrossConnectLowVci'
_Z='atmVcCrossConnectLowIfIndex'
_Y='atmVcCrossConnectIndex'
_X='atmVcCrossConnectHighVpi'
_W='atmVcCrossConnectHighVci'
_V='atmVcCrossConnectHighIfIndex'
_U='sfcsQueueStatsQueue'
_T='sfcsQueueConfigQueueIndex'
_S='backplane-two'
_R='backplane-one'
_Q='anim-four-clk'
_P='anim-three-clk'
_O='anim-two-clk'
_N='anim-one-clk'
_M='OctetString'
_L='reset'
_K='write-only'
_J='ATM-MIB'
_I='disabled'
_H='enabled'
_G='DisplayString'
_F='other'
_E='CTRON-SFCS-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVcCrossConnectHighIfIndex,atmVcCrossConnectHighVci,atmVcCrossConnectHighVpi,atmVcCrossConnectIndex,atmVcCrossConnectLowIfIndex,atmVcCrossConnectLowVci,atmVcCrossConnectLowVpi=mibBuilder.importSymbols(_J,_V,_W,_X,_Y,_Z,_a,_b)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,52,4))
_Ctron_ObjectIdentity=ObjectIdentity
ctron=_Ctron_ObjectIdentity((1,3,6,1,4,1,52,4,1))
_CtDataLink_ObjectIdentity=ObjectIdentity
ctDataLink=_CtDataLink_ObjectIdentity((1,3,6,1,4,1,52,4,1,2))
_CtSwitch_ObjectIdentity=ObjectIdentity
ctSwitch=_CtSwitch_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11))
_CtsfSwitch_ObjectIdentity=ObjectIdentity
ctsfSwitch=_CtsfSwitch_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1))
_CtSFCS_ObjectIdentity=ObjectIdentity
ctSFCS=_CtSFCS_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1))
_SfcsSystem_ObjectIdentity=ObjectIdentity
sfcsSystem=_SfcsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1))
_SfcsSysConfig_ObjectIdentity=ObjectIdentity
sfcsSysConfig=_SfcsSysConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1))
_SfcsSysConfigTable_ObjectIdentity=ObjectIdentity
sfcsSysConfigTable=_SfcsSysConfigTable_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1))
_SfcsSysConfigEnt_ObjectIdentity=ObjectIdentity
sfcsSysConfigEnt=_SfcsSysConfigEnt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1))
class _SfcsSysConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsSysConfigAdminStatus_Type.__name__=_D
_SfcsSysConfigAdminStatus_Object=MibScalar
sfcsSysConfigAdminStatus=_SfcsSysConfigAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,1),_SfcsSysConfigAdminStatus_Type())
sfcsSysConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigAdminStatus.setStatus(_A)
class _SfcsSysConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3),(_c,4),(_d,5),(_e,6)))
_SfcsSysConfigOperStatus_Type.__name__=_D
_SfcsSysConfigOperStatus_Object=MibScalar
sfcsSysConfigOperStatus=_SfcsSysConfigOperStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,2),_SfcsSysConfigOperStatus_Type())
sfcsSysConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigOperStatus.setStatus(_A)
_SfcsSysConfigOperTime_Type=TimeTicks
_SfcsSysConfigOperTime_Object=MibScalar
sfcsSysConfigOperTime=_SfcsSysConfigOperTime_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,3),_SfcsSysConfigOperTime_Type())
sfcsSysConfigOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigOperTime.setStatus(_A)
_SfcsSysConfigLastChange_Type=TimeTicks
_SfcsSysConfigLastChange_Object=MibScalar
sfcsSysConfigLastChange=_SfcsSysConfigLastChange_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,4),_SfcsSysConfigLastChange_Type())
sfcsSysConfigLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigLastChange.setStatus(_A)
_SfcsSysConfigSwitchCapacity_Type=Integer32
_SfcsSysConfigSwitchCapacity_Object=MibScalar
sfcsSysConfigSwitchCapacity=_SfcsSysConfigSwitchCapacity_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,5),_SfcsSysConfigSwitchCapacity_Type())
sfcsSysConfigSwitchCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigSwitchCapacity.setStatus(_A)
_SfcsSysConfigMaxCnxEntries_Type=Integer32
_SfcsSysConfigMaxCnxEntries_Object=MibScalar
sfcsSysConfigMaxCnxEntries=_SfcsSysConfigMaxCnxEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,6),_SfcsSysConfigMaxCnxEntries_Type())
sfcsSysConfigMaxCnxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigMaxCnxEntries.setStatus(_A)
_SfcsSysConfigMaxStatEntries_Type=Integer32
_SfcsSysConfigMaxStatEntries_Object=MibScalar
sfcsSysConfigMaxStatEntries=_SfcsSysConfigMaxStatEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,7),_SfcsSysConfigMaxStatEntries_Type())
sfcsSysConfigMaxStatEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigMaxStatEntries.setStatus(_A)
_SfcsSysConfigMaxUpcEntries_Type=Integer32
_SfcsSysConfigMaxUpcEntries_Object=MibScalar
sfcsSysConfigMaxUpcEntries=_SfcsSysConfigMaxUpcEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,8),_SfcsSysConfigMaxUpcEntries_Type())
sfcsSysConfigMaxUpcEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigMaxUpcEntries.setStatus(_A)
_SfcsSysConfigNumberANIMS_Type=Integer32
_SfcsSysConfigNumberANIMS_Object=MibScalar
sfcsSysConfigNumberANIMS=_SfcsSysConfigNumberANIMS_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,9),_SfcsSysConfigNumberANIMS_Type())
sfcsSysConfigNumberANIMS.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigNumberANIMS.setStatus(_A)
_SfcsSysConfigInterfaceCapability_Type=Integer32
_SfcsSysConfigInterfaceCapability_Object=MibScalar
sfcsSysConfigInterfaceCapability=_SfcsSysConfigInterfaceCapability_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,10),_SfcsSysConfigInterfaceCapability_Type())
sfcsSysConfigInterfaceCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigInterfaceCapability.setStatus(_A)
class _SfcsSysConfigTypeofSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('sfcellswitch',2),('sfpacketswitch',3)))
_SfcsSysConfigTypeofSwitch_Type.__name__=_D
_SfcsSysConfigTypeofSwitch_Object=MibScalar
sfcsSysConfigTypeofSwitch=_SfcsSysConfigTypeofSwitch_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,11),_SfcsSysConfigTypeofSwitch_Type())
sfcsSysConfigTypeofSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigTypeofSwitch.setStatus(_A)
_SfcsSysConfigPolicingSupport_Type=TruthValue
_SfcsSysConfigPolicingSupport_Object=MibScalar
sfcsSysConfigPolicingSupport=_SfcsSysConfigPolicingSupport_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,12),_SfcsSysConfigPolicingSupport_Type())
sfcsSysConfigPolicingSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigPolicingSupport.setStatus(_A)
class _SfcsSysConfigPnniNsapPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_SfcsSysConfigPnniNsapPrefix_Type.__name__=_M
_SfcsSysConfigPnniNsapPrefix_Object=MibScalar
sfcsSysConfigPnniNsapPrefix=_SfcsSysConfigPnniNsapPrefix_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,13),_SfcsSysConfigPnniNsapPrefix_Type())
sfcsSysConfigPnniNsapPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigPnniNsapPrefix.setStatus(_A)
_SfcsSysConfigPnniNodeLevel_Type=Integer32
_SfcsSysConfigPnniNodeLevel_Object=MibScalar
sfcsSysConfigPnniNodeLevel=_SfcsSysConfigPnniNodeLevel_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,14),_SfcsSysConfigPnniNodeLevel_Type())
sfcsSysConfigPnniNodeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigPnniNodeLevel.setStatus(_A)
_SfcsSysConfigPnniAddessingMode_Type=Integer32
_SfcsSysConfigPnniAddessingMode_Object=MibScalar
sfcsSysConfigPnniAddessingMode=_SfcsSysConfigPnniAddessingMode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,15),_SfcsSysConfigPnniAddessingMode_Type())
sfcsSysConfigPnniAddessingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigPnniAddessingMode.setStatus(_A)
_SfcsSysConfigPnniAddessingAdmnStatus_Type=Integer32
_SfcsSysConfigPnniAddessingAdmnStatus_Object=MibScalar
sfcsSysConfigPnniAddessingAdmnStatus=_SfcsSysConfigPnniAddessingAdmnStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,16),_SfcsSysConfigPnniAddessingAdmnStatus_Type())
sfcsSysConfigPnniAddessingAdmnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigPnniAddessingAdmnStatus.setStatus(_A)
class _SfcsSysConfigFMVer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SfcsSysConfigFMVer_Type.__name__=_M
_SfcsSysConfigFMVer_Object=MibScalar
sfcsSysConfigFMVer=_SfcsSysConfigFMVer_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,17),_SfcsSysConfigFMVer_Type())
sfcsSysConfigFMVer.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigFMVer.setStatus(_A)
_SfcsSysConfigCTMSlotMask_Type=Integer32
_SfcsSysConfigCTMSlotMask_Object=MibScalar
sfcsSysConfigCTMSlotMask=_SfcsSysConfigCTMSlotMask_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,18),_SfcsSysConfigCTMSlotMask_Type())
sfcsSysConfigCTMSlotMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysConfigCTMSlotMask.setStatus(_A)
_SfcsSysConfigMaxfreecva_Type=Integer32
_SfcsSysConfigMaxfreecva_Object=MibScalar
sfcsSysConfigMaxfreecva=_SfcsSysConfigMaxfreecva_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,19),_SfcsSysConfigMaxfreecva_Type())
sfcsSysConfigMaxfreecva.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigMaxfreecva.setStatus(_A)
_SfcsSysConfigUBR_Type=Integer32
_SfcsSysConfigUBR_Object=MibScalar
sfcsSysConfigUBR=_SfcsSysConfigUBR_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,1,1,1,20),_SfcsSysConfigUBR_Type())
sfcsSysConfigUBR.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigUBR.setStatus(_A)
_SfcsSysStatus_ObjectIdentity=ObjectIdentity
sfcsSysStatus=_SfcsSysStatus_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2))
_SfcsSysStatusTable_ObjectIdentity=ObjectIdentity
sfcsSysStatusTable=_SfcsSysStatusTable_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1))
_SfcsSysStatusEnt_ObjectIdentity=ObjectIdentity
sfcsSysStatusEnt=_SfcsSysStatusEnt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1))
_SfcsSysStatusTdmCellCount_Type=OctetString
_SfcsSysStatusTdmCellCount_Object=MibScalar
sfcsSysStatusTdmCellCount=_SfcsSysStatusTdmCellCount_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1,1),_SfcsSysStatusTdmCellCount_Type())
sfcsSysStatusTdmCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysStatusTdmCellCount.setStatus(_A)
class _SfcsSysStatusTdmUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsSysStatusTdmUtilization_Type.__name__=_D
_SfcsSysStatusTdmUtilization_Object=MibScalar
sfcsSysStatusTdmUtilization=_SfcsSysStatusTdmUtilization_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1,2),_SfcsSysStatusTdmUtilization_Type())
sfcsSysStatusTdmUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysStatusTdmUtilization.setStatus(_A)
_SfcsSysStatusCurrCnxEntries_Type=Integer32
_SfcsSysStatusCurrCnxEntries_Object=MibScalar
sfcsSysStatusCurrCnxEntries=_SfcsSysStatusCurrCnxEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1,3),_SfcsSysStatusCurrCnxEntries_Type())
sfcsSysStatusCurrCnxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysStatusCurrCnxEntries.setStatus(_A)
_SfcsSysStatusCurrUPCEntries_Type=Integer32
_SfcsSysStatusCurrUPCEntries_Object=MibScalar
sfcsSysStatusCurrUPCEntries=_SfcsSysStatusCurrUPCEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1,4),_SfcsSysStatusCurrUPCEntries_Type())
sfcsSysStatusCurrUPCEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysStatusCurrUPCEntries.setStatus(_A)
_SfcsSysStatusCurrStatsEntries_Type=Integer32
_SfcsSysStatusCurrStatsEntries_Object=MibScalar
sfcsSysStatusCurrStatsEntries=_SfcsSysStatusCurrStatsEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1,5),_SfcsSysStatusCurrStatsEntries_Type())
sfcsSysStatusCurrStatsEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysStatusCurrStatsEntries.setStatus(_A)
_SfcsSysStatusAllocatedBw_Type=Integer32
_SfcsSysStatusAllocatedBw_Object=MibScalar
sfcsSysStatusAllocatedBw=_SfcsSysStatusAllocatedBw_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,2,1,1,6),_SfcsSysStatusAllocatedBw_Type())
sfcsSysStatusAllocatedBw.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsSysStatusAllocatedBw.setStatus(_A)
_SfcsSysSystemCfg_ObjectIdentity=ObjectIdentity
sfcsSysSystemCfg=_SfcsSysSystemCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3))
_SfcsSysSystemCfgTable_ObjectIdentity=ObjectIdentity
sfcsSysSystemCfgTable=_SfcsSysSystemCfgTable_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3,1))
_SfcsSysSystemCfgEnt_ObjectIdentity=ObjectIdentity
sfcsSysSystemCfgEnt=_SfcsSysSystemCfgEnt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3,1,1))
class _SfcsSysConfigAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_L,2)))
_SfcsSysConfigAdminReset_Type.__name__=_D
_SfcsSysConfigAdminReset_Object=MibScalar
sfcsSysConfigAdminReset=_SfcsSysConfigAdminReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3,1,1,1),_SfcsSysConfigAdminReset_Type())
sfcsSysConfigAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigAdminReset.setStatus(_A)
class _SfcsSysConfigATOMPersistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfcsSysConfigATOMPersistance_Type.__name__=_D
_SfcsSysConfigATOMPersistance_Object=MibScalar
sfcsSysConfigATOMPersistance=_SfcsSysConfigATOMPersistance_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3,1,1,2),_SfcsSysConfigATOMPersistance_Type())
sfcsSysConfigATOMPersistance.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigATOMPersistance.setStatus(_A)
_SfcsSysConfigVcSize_Type=Integer32
_SfcsSysConfigVcSize_Object=MibScalar
sfcsSysConfigVcSize=_SfcsSysConfigVcSize_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3,1,1,3),_SfcsSysConfigVcSize_Type())
sfcsSysConfigVcSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigVcSize.setStatus(_A)
class _SfcsSysConfigPowerUpDiags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfcsSysConfigPowerUpDiags_Type.__name__=_D
_SfcsSysConfigPowerUpDiags_Object=MibScalar
sfcsSysConfigPowerUpDiags=_SfcsSysConfigPowerUpDiags_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,3,1,1,4),_SfcsSysConfigPowerUpDiags_Type())
sfcsSysConfigPowerUpDiags.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysConfigPowerUpDiags.setStatus(_A)
_SfcsSysBPCfg_ObjectIdentity=ObjectIdentity
sfcsSysBPCfg=_SfcsSysBPCfg_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,4))
_SfcsSysBPTable_ObjectIdentity=ObjectIdentity
sfcsSysBPTable=_SfcsSysBPTable_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,4,1))
_SfcsSysBPEnt_ObjectIdentity=ObjectIdentity
sfcsSysBPEnt=_SfcsSysBPEnt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,1,4,1,1))
_SfcsSysBPClkSelect_Type=Integer32
_SfcsSysBPClkSelect_Object=MibScalar
sfcsSysBPClkSelect=_SfcsSysBPClkSelect_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,1,4,1,1,1),_SfcsSysBPClkSelect_Type())
sfcsSysBPClkSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsSysBPClkSelect.setStatus(_A)
_SfcsEngine_ObjectIdentity=ObjectIdentity
sfcsEngine=_SfcsEngine_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,2))
_SfcsConfig_ObjectIdentity=ObjectIdentity
sfcsConfig=_SfcsConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1))
_SfcsConfigTable_Object=MibTable
sfcsConfigTable=_SfcsConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1))
if mibBuilder.loadTexts:sfcsConfigTable.setStatus(_A)
_SfcsConfigEntry_Object=MibTableRow
sfcsConfigEntry=_SfcsConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1))
sfcsConfigEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:sfcsConfigEntry.setStatus(_A)
_SfcsConfigSlotIndex_Type=Integer32
_SfcsConfigSlotIndex_Object=MibTableColumn
sfcsConfigSlotIndex=_SfcsConfigSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,1),_SfcsConfigSlotIndex_Type())
sfcsConfigSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigSlotIndex.setStatus(_A)
class _SfcsConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsConfigAdminStatus_Type.__name__=_D
_SfcsConfigAdminStatus_Object=MibTableColumn
sfcsConfigAdminStatus=_SfcsConfigAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,2),_SfcsConfigAdminStatus_Type())
sfcsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsConfigAdminStatus.setStatus(_A)
class _SfcsConfigAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_L,2)))
_SfcsConfigAdminReset_Type.__name__=_D
_SfcsConfigAdminReset_Object=MibTableColumn
sfcsConfigAdminReset=_SfcsConfigAdminReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,3),_SfcsConfigAdminReset_Type())
sfcsConfigAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsConfigAdminReset.setStatus(_A)
class _SfcsConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3),(_c,4),(_d,5),(_e,6)))
_SfcsConfigOperStatus_Type.__name__=_D
_SfcsConfigOperStatus_Object=MibTableColumn
sfcsConfigOperStatus=_SfcsConfigOperStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,4),_SfcsConfigOperStatus_Type())
sfcsConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigOperStatus.setStatus(_A)
_SfcsConfigOperTime_Type=TimeTicks
_SfcsConfigOperTime_Object=MibTableColumn
sfcsConfigOperTime=_SfcsConfigOperTime_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,5),_SfcsConfigOperTime_Type())
sfcsConfigOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigOperTime.setStatus(_A)
_SfcsConfigLastChange_Type=TimeTicks
_SfcsConfigLastChange_Object=MibTableColumn
sfcsConfigLastChange=_SfcsConfigLastChange_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,6),_SfcsConfigLastChange_Type())
sfcsConfigLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigLastChange.setStatus(_A)
_SfcsConfigVersion_Type=Integer32
_SfcsConfigVersion_Object=MibTableColumn
sfcsConfigVersion=_SfcsConfigVersion_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,7),_SfcsConfigVersion_Type())
sfcsConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigVersion.setStatus(_A)
_SfcsConfigMibRev_Type=DisplayString
_SfcsConfigMibRev_Object=MibTableColumn
sfcsConfigMibRev=_SfcsConfigMibRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,8),_SfcsConfigMibRev_Type())
sfcsConfigMibRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigMibRev.setStatus(_A)
_SfcsConfigSwitchHostPort_Type=Integer32
_SfcsConfigSwitchHostPort_Object=MibTableColumn
sfcsConfigSwitchHostPort=_SfcsConfigSwitchHostPort_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,9),_SfcsConfigSwitchHostPort_Type())
sfcsConfigSwitchHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigSwitchHostPort.setStatus(_A)
_SfcsConfigHostCtrlATMAddr_Type=OctetString
_SfcsConfigHostCtrlATMAddr_Object=MibTableColumn
sfcsConfigHostCtrlATMAddr=_SfcsConfigHostCtrlATMAddr_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,10),_SfcsConfigHostCtrlATMAddr_Type())
sfcsConfigHostCtrlATMAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigHostCtrlATMAddr.setStatus(_A)
_SfcsConfigSwitchCapacity_Type=Integer32
_SfcsConfigSwitchCapacity_Object=MibTableColumn
sfcsConfigSwitchCapacity=_SfcsConfigSwitchCapacity_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,11),_SfcsConfigSwitchCapacity_Type())
sfcsConfigSwitchCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigSwitchCapacity.setStatus(_A)
_SfcsConfigMaxCnxEntries_Type=Integer32
_SfcsConfigMaxCnxEntries_Object=MibTableColumn
sfcsConfigMaxCnxEntries=_SfcsConfigMaxCnxEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,12),_SfcsConfigMaxCnxEntries_Type())
sfcsConfigMaxCnxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigMaxCnxEntries.setStatus(_A)
_SfcsConfigMaxStatEntries_Type=Integer32
_SfcsConfigMaxStatEntries_Object=MibTableColumn
sfcsConfigMaxStatEntries=_SfcsConfigMaxStatEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,13),_SfcsConfigMaxStatEntries_Type())
sfcsConfigMaxStatEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigMaxStatEntries.setStatus(_A)
_SfcsConfigMaxUpcEntries_Type=Integer32
_SfcsConfigMaxUpcEntries_Object=MibTableColumn
sfcsConfigMaxUpcEntries=_SfcsConfigMaxUpcEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,14),_SfcsConfigMaxUpcEntries_Type())
sfcsConfigMaxUpcEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigMaxUpcEntries.setStatus(_A)
_SfcsConfigNumberANIMS_Type=Integer32
_SfcsConfigNumberANIMS_Object=MibTableColumn
sfcsConfigNumberANIMS=_SfcsConfigNumberANIMS_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,15),_SfcsConfigNumberANIMS_Type())
sfcsConfigNumberANIMS.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigNumberANIMS.setStatus(_A)
_SfcsConfigBwCapability_Type=Integer32
_SfcsConfigBwCapability_Object=MibTableColumn
sfcsConfigBwCapability=_SfcsConfigBwCapability_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,16),_SfcsConfigBwCapability_Type())
sfcsConfigBwCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsConfigBwCapability.setStatus(_A)
class _SfcsConfigMasterClock1Source_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_SfcsConfigMasterClock1Source_Type.__name__=_D
_SfcsConfigMasterClock1Source_Object=MibTableColumn
sfcsConfigMasterClock1Source=_SfcsConfigMasterClock1Source_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,17),_SfcsConfigMasterClock1Source_Type())
sfcsConfigMasterClock1Source.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsConfigMasterClock1Source.setStatus(_A)
class _SfcsConfigMasterClock2Source_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6)))
_SfcsConfigMasterClock2Source_Type.__name__=_D
_SfcsConfigMasterClock2Source_Object=MibTableColumn
sfcsConfigMasterClock2Source=_SfcsConfigMasterClock2Source_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,18),_SfcsConfigMasterClock2Source_Type())
sfcsConfigMasterClock2Source.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsConfigMasterClock2Source.setStatus(_A)
class _SfcsConfigMasterClock1Standby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),('none',7)))
_SfcsConfigMasterClock1Standby_Type.__name__=_D
_SfcsConfigMasterClock1Standby_Object=MibTableColumn
sfcsConfigMasterClock1Standby=_SfcsConfigMasterClock1Standby_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,19),_SfcsConfigMasterClock1Standby_Type())
sfcsConfigMasterClock1Standby.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsConfigMasterClock1Standby.setStatus(_A)
class _SfcsConfigMasterClock2Standby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),('none',7)))
_SfcsConfigMasterClock2Standby_Type.__name__=_D
_SfcsConfigMasterClock2Standby_Object=MibTableColumn
sfcsConfigMasterClock2Standby=_SfcsConfigMasterClock2Standby_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,1,1,1,20),_SfcsConfigMasterClock2Standby_Type())
sfcsConfigMasterClock2Standby.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsConfigMasterClock2Standby.setStatus(_A)
_SfcsStatus_ObjectIdentity=ObjectIdentity
sfcsStatus=_SfcsStatus_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2))
_SfcsStatusTable_Object=MibTable
sfcsStatusTable=_SfcsStatusTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1))
if mibBuilder.loadTexts:sfcsStatusTable.setStatus(_A)
_SfcsStatusEntry_Object=MibTableRow
sfcsStatusEntry=_SfcsStatusEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1))
sfcsStatusEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:sfcsStatusEntry.setStatus(_A)
_SfcsStatusSlotIndex_Type=Integer32
_SfcsStatusSlotIndex_Object=MibTableColumn
sfcsStatusSlotIndex=_SfcsStatusSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,1),_SfcsStatusSlotIndex_Type())
sfcsStatusSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusSlotIndex.setStatus(_A)
_SfcsStatusTdmCellCount_Type=OctetString
_SfcsStatusTdmCellCount_Object=MibTableColumn
sfcsStatusTdmCellCount=_SfcsStatusTdmCellCount_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,2),_SfcsStatusTdmCellCount_Type())
sfcsStatusTdmCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusTdmCellCount.setStatus(_A)
class _SfcsStatusTdmUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsStatusTdmUtilization_Type.__name__=_D
_SfcsStatusTdmUtilization_Object=MibTableColumn
sfcsStatusTdmUtilization=_SfcsStatusTdmUtilization_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,3),_SfcsStatusTdmUtilization_Type())
sfcsStatusTdmUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusTdmUtilization.setStatus(_A)
_SfcsStatusCurrCnxEntries_Type=Integer32
_SfcsStatusCurrCnxEntries_Object=MibTableColumn
sfcsStatusCurrCnxEntries=_SfcsStatusCurrCnxEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,4),_SfcsStatusCurrCnxEntries_Type())
sfcsStatusCurrCnxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusCurrCnxEntries.setStatus(_A)
_SfcsStatusCurrUPCEntries_Type=Integer32
_SfcsStatusCurrUPCEntries_Object=MibTableColumn
sfcsStatusCurrUPCEntries=_SfcsStatusCurrUPCEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,5),_SfcsStatusCurrUPCEntries_Type())
sfcsStatusCurrUPCEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusCurrUPCEntries.setStatus(_A)
_SfcsStatusCurrStatsEntries_Type=Integer32
_SfcsStatusCurrStatsEntries_Object=MibTableColumn
sfcsStatusCurrStatsEntries=_SfcsStatusCurrStatsEntries_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,6),_SfcsStatusCurrStatsEntries_Type())
sfcsStatusCurrStatsEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusCurrStatsEntries.setStatus(_A)
_SfcsStatusCurrCtmAgent_Type=Integer32
_SfcsStatusCurrCtmAgent_Object=MibTableColumn
sfcsStatusCurrCtmAgent=_SfcsStatusCurrCtmAgent_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,2,1,1,7),_SfcsStatusCurrCtmAgent_Type())
sfcsStatusCurrCtmAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatusCurrCtmAgent.setStatus(_A)
_SfcsUPCEngine_ObjectIdentity=ObjectIdentity
sfcsUPCEngine=_SfcsUPCEngine_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3))
_SfcsUPCTable_Object=MibTable
sfcsUPCTable=_SfcsUPCTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1))
if mibBuilder.loadTexts:sfcsUPCTable.setStatus(_A)
_SfcsUPCEntry_Object=MibTableRow
sfcsUPCEntry=_SfcsUPCEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1,1))
sfcsUPCEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:sfcsUPCEntry.setStatus(_A)
_SfcsUPCSlotIndex_Type=Integer32
_SfcsUPCSlotIndex_Object=MibTableColumn
sfcsUPCSlotIndex=_SfcsUPCSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1,1,1),_SfcsUPCSlotIndex_Type())
sfcsUPCSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsUPCSlotIndex.setStatus(_A)
class _SfcsUPCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsUPCAdminStatus_Type.__name__=_D
_SfcsUPCAdminStatus_Object=MibTableColumn
sfcsUPCAdminStatus=_SfcsUPCAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1,1,2),_SfcsUPCAdminStatus_Type())
sfcsUPCAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsUPCAdminStatus.setStatus(_A)
class _SfcsUPCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsUPCOperStatus_Type.__name__=_D
_SfcsUPCOperStatus_Object=MibTableColumn
sfcsUPCOperStatus=_SfcsUPCOperStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1,1,3),_SfcsUPCOperStatus_Type())
sfcsUPCOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsUPCOperStatus.setStatus(_A)
class _SfcsUPCReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_L,2)))
_SfcsUPCReset_Type.__name__=_D
_SfcsUPCReset_Object=MibTableColumn
sfcsUPCReset=_SfcsUPCReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1,1,4),_SfcsUPCReset_Type())
sfcsUPCReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsUPCReset.setStatus(_A)
_SfcsUPCOperTime_Type=TimeTicks
_SfcsUPCOperTime_Object=MibTableColumn
sfcsUPCOperTime=_SfcsUPCOperTime_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,3,1,1,5),_SfcsUPCOperTime_Type())
sfcsUPCOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsUPCOperTime.setStatus(_A)
_SfcsStatisticsEngine_ObjectIdentity=ObjectIdentity
sfcsStatisticsEngine=_SfcsStatisticsEngine_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4))
_SfcsStatsEngineTable_Object=MibTable
sfcsStatsEngineTable=_SfcsStatsEngineTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1))
if mibBuilder.loadTexts:sfcsStatsEngineTable.setStatus(_A)
_SfcsStatsEngineEntry_Object=MibTableRow
sfcsStatsEngineEntry=_SfcsStatsEngineEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1,1))
sfcsStatsEngineEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:sfcsStatsEngineEntry.setStatus(_A)
_SfcsStatsEngineSlotIndex_Type=Integer32
_SfcsStatsEngineSlotIndex_Object=MibTableColumn
sfcsStatsEngineSlotIndex=_SfcsStatsEngineSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1,1,1),_SfcsStatsEngineSlotIndex_Type())
sfcsStatsEngineSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatsEngineSlotIndex.setStatus(_A)
class _SfcsStatsEngineAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsStatsEngineAdminStatus_Type.__name__=_D
_SfcsStatsEngineAdminStatus_Object=MibTableColumn
sfcsStatsEngineAdminStatus=_SfcsStatsEngineAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1,1,2),_SfcsStatsEngineAdminStatus_Type())
sfcsStatsEngineAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsStatsEngineAdminStatus.setStatus(_A)
class _SfcsStatsEngineOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsStatsEngineOperStatus_Type.__name__=_D
_SfcsStatsEngineOperStatus_Object=MibTableColumn
sfcsStatsEngineOperStatus=_SfcsStatsEngineOperStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1,1,3),_SfcsStatsEngineOperStatus_Type())
sfcsStatsEngineOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatsEngineOperStatus.setStatus(_A)
class _SfcsStatsEngineReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_L,2)))
_SfcsStatsEngineReset_Type.__name__=_D
_SfcsStatsEngineReset_Object=MibTableColumn
sfcsStatsEngineReset=_SfcsStatsEngineReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1,1,4),_SfcsStatsEngineReset_Type())
sfcsStatsEngineReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsStatsEngineReset.setStatus(_A)
_SfcsStatsEngineOperTime_Type=TimeTicks
_SfcsStatsEngineOperTime_Object=MibTableColumn
sfcsStatsEngineOperTime=_SfcsStatsEngineOperTime_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,4,1,1,5),_SfcsStatsEngineOperTime_Type())
sfcsStatsEngineOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsStatsEngineOperTime.setStatus(_A)
_SfcsPacketDiscardEngine_ObjectIdentity=ObjectIdentity
sfcsPacketDiscardEngine=_SfcsPacketDiscardEngine_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5))
_SfcsPacketDiscardEngineTable_Object=MibTable
sfcsPacketDiscardEngineTable=_SfcsPacketDiscardEngineTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1))
if mibBuilder.loadTexts:sfcsPacketDiscardEngineTable.setStatus(_A)
_SfcsPacketDiscardEngineEntry_Object=MibTableRow
sfcsPacketDiscardEngineEntry=_SfcsPacketDiscardEngineEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1))
sfcsPacketDiscardEngineEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:sfcsPacketDiscardEngineEntry.setStatus(_A)
_SfcsPacketDiscardEngineSlotIndex_Type=Integer32
_SfcsPacketDiscardEngineSlotIndex_Object=MibTableColumn
sfcsPacketDiscardEngineSlotIndex=_SfcsPacketDiscardEngineSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1,1),_SfcsPacketDiscardEngineSlotIndex_Type())
sfcsPacketDiscardEngineSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsPacketDiscardEngineSlotIndex.setStatus(_A)
class _SfcsPacketDiscardEngineAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsPacketDiscardEngineAdminStatus_Type.__name__=_D
_SfcsPacketDiscardEngineAdminStatus_Object=MibTableColumn
sfcsPacketDiscardEngineAdminStatus=_SfcsPacketDiscardEngineAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1,2),_SfcsPacketDiscardEngineAdminStatus_Type())
sfcsPacketDiscardEngineAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsPacketDiscardEngineAdminStatus.setStatus(_A)
class _SfcsPacketDiscardEngineOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsPacketDiscardEngineOperStatus_Type.__name__=_D
_SfcsPacketDiscardEngineOperStatus_Object=MibTableColumn
sfcsPacketDiscardEngineOperStatus=_SfcsPacketDiscardEngineOperStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1,3),_SfcsPacketDiscardEngineOperStatus_Type())
sfcsPacketDiscardEngineOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsPacketDiscardEngineOperStatus.setStatus(_A)
class _SfcsPacketDiscardEngineReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_L,2)))
_SfcsPacketDiscardEngineReset_Type.__name__=_D
_SfcsPacketDiscardEngineReset_Object=MibTableColumn
sfcsPacketDiscardEngineReset=_SfcsPacketDiscardEngineReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1,4),_SfcsPacketDiscardEngineReset_Type())
sfcsPacketDiscardEngineReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsPacketDiscardEngineReset.setStatus(_A)
class _SfcsPacketDiscardEngineEPDPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsPacketDiscardEngineEPDPercentage_Type.__name__=_D
_SfcsPacketDiscardEngineEPDPercentage_Object=MibTableColumn
sfcsPacketDiscardEngineEPDPercentage=_SfcsPacketDiscardEngineEPDPercentage_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1,5),_SfcsPacketDiscardEngineEPDPercentage_Type())
sfcsPacketDiscardEngineEPDPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsPacketDiscardEngineEPDPercentage.setStatus(_A)
_SfcsPacketDiscardEngineOperTime_Type=TimeTicks
_SfcsPacketDiscardEngineOperTime_Object=MibTableColumn
sfcsPacketDiscardEngineOperTime=_SfcsPacketDiscardEngineOperTime_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,2,5,1,1,6),_SfcsPacketDiscardEngineOperTime_Type())
sfcsPacketDiscardEngineOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsPacketDiscardEngineOperTime.setStatus(_A)
_SfcsANIM_ObjectIdentity=ObjectIdentity
sfcsANIM=_SfcsANIM_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,3))
_SfcsANIMConfig_ObjectIdentity=ObjectIdentity
sfcsANIMConfig=_SfcsANIMConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1))
_SfcsANIMConfigTable_Object=MibTable
sfcsANIMConfigTable=_SfcsANIMConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1))
if mibBuilder.loadTexts:sfcsANIMConfigTable.setStatus(_A)
_SfcsANIMConfigEntry_Object=MibTableRow
sfcsANIMConfigEntry=_SfcsANIMConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1))
sfcsANIMConfigEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:sfcsANIMConfigEntry.setStatus(_A)
_SfcsANIMConfigANIMIndex_Type=Integer32
_SfcsANIMConfigANIMIndex_Object=MibTableColumn
sfcsANIMConfigANIMIndex=_SfcsANIMConfigANIMIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,1),_SfcsANIMConfigANIMIndex_Type())
sfcsANIMConfigANIMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMConfigANIMIndex.setStatus(_A)
class _SfcsANIMConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsANIMConfigAdminStatus_Type.__name__=_D
_SfcsANIMConfigAdminStatus_Object=MibTableColumn
sfcsANIMConfigAdminStatus=_SfcsANIMConfigAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,2),_SfcsANIMConfigAdminStatus_Type())
sfcsANIMConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsANIMConfigAdminStatus.setStatus(_A)
class _SfcsANIMConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsANIMConfigOperStatus_Type.__name__=_D
_SfcsANIMConfigOperStatus_Object=MibTableColumn
sfcsANIMConfigOperStatus=_SfcsANIMConfigOperStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,3),_SfcsANIMConfigOperStatus_Type())
sfcsANIMConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMConfigOperStatus.setStatus(_A)
_SfcsANIMConfigANIMType_Type=ObjectIdentifier
_SfcsANIMConfigANIMType_Object=MibTableColumn
sfcsANIMConfigANIMType=_SfcsANIMConfigANIMType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,4),_SfcsANIMConfigANIMType_Type())
sfcsANIMConfigANIMType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMConfigANIMType.setStatus(_A)
_SfcsANIMConfigNumInterfaces_Type=Integer32
_SfcsANIMConfigNumInterfaces_Object=MibTableColumn
sfcsANIMConfigNumInterfaces=_SfcsANIMConfigNumInterfaces_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,5),_SfcsANIMConfigNumInterfaces_Type())
sfcsANIMConfigNumInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMConfigNumInterfaces.setStatus(_A)
_SfcsANIMConfigLineRate_Type=Integer32
_SfcsANIMConfigLineRate_Object=MibTableColumn
sfcsANIMConfigLineRate=_SfcsANIMConfigLineRate_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,6),_SfcsANIMConfigLineRate_Type())
sfcsANIMConfigLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMConfigLineRate.setStatus(_A)
class _SfcsANIMConfigToMB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_l,1),('port-one-clock',2),('port-two-clock',3),('port-three-clock',4),('port-four-clock',5)))
_SfcsANIMConfigToMB_Type.__name__=_D
_SfcsANIMConfigToMB_Object=MibTableColumn
sfcsANIMConfigToMB=_SfcsANIMConfigToMB_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,7),_SfcsANIMConfigToMB_Type())
sfcsANIMConfigToMB.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsANIMConfigToMB.setStatus(_A)
class _SfcsANIMConfigMBClockSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master-clk-one',1),('master-clk-two',2)))
_SfcsANIMConfigMBClockSelect_Type.__name__=_D
_SfcsANIMConfigMBClockSelect_Object=MibTableColumn
sfcsANIMConfigMBClockSelect=_SfcsANIMConfigMBClockSelect_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,1,1,1,8),_SfcsANIMConfigMBClockSelect_Type())
sfcsANIMConfigMBClockSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsANIMConfigMBClockSelect.setStatus(_A)
_SfcsANIMStatistics_ObjectIdentity=ObjectIdentity
sfcsANIMStatistics=_SfcsANIMStatistics_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,3,2))
_SfcsANIMStatsTable_Object=MibTable
sfcsANIMStatsTable=_SfcsANIMStatsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,2,1))
if mibBuilder.loadTexts:sfcsANIMStatsTable.setStatus(_A)
_SfcsANIMStatsEntry_Object=MibTableRow
sfcsANIMStatsEntry=_SfcsANIMStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,2,1,1))
sfcsANIMStatsEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:sfcsANIMStatsEntry.setStatus(_A)
_SfcsANIMStatsANIMIndex_Type=Integer32
_SfcsANIMStatsANIMIndex_Object=MibTableColumn
sfcsANIMStatsANIMIndex=_SfcsANIMStatsANIMIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,2,1,1,1),_SfcsANIMStatsANIMIndex_Type())
sfcsANIMStatsANIMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMStatsANIMIndex.setStatus(_A)
_SfcsANIMStatsRxCells_Type=OctetString
_SfcsANIMStatsRxCells_Object=MibTableColumn
sfcsANIMStatsRxCells=_SfcsANIMStatsRxCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,2,1,1,2),_SfcsANIMStatsRxCells_Type())
sfcsANIMStatsRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMStatsRxCells.setStatus(_A)
_SfcsANIMStatsTxCells_Type=OctetString
_SfcsANIMStatsTxCells_Object=MibTableColumn
sfcsANIMStatsTxCells=_SfcsANIMStatsTxCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,2,1,1,3),_SfcsANIMStatsTxCells_Type())
sfcsANIMStatsTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMStatsTxCells.setStatus(_A)
_SfcsANIMPic_ObjectIdentity=ObjectIdentity
sfcsANIMPic=_SfcsANIMPic_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3))
_SfcsANIMPicTable_Object=MibTable
sfcsANIMPicTable=_SfcsANIMPicTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1))
if mibBuilder.loadTexts:sfcsANIMPicTable.setStatus(_A)
_SfcsANIMPicEntry_Object=MibTableRow
sfcsANIMPicEntry=_SfcsANIMPicEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1))
sfcsANIMPicEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:sfcsANIMPicEntry.setStatus(_A)
_SfcsANIMPicSlot_Type=Integer32
_SfcsANIMPicSlot_Object=MibTableColumn
sfcsANIMPicSlot=_SfcsANIMPicSlot_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,1),_SfcsANIMPicSlot_Type())
sfcsANIMPicSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicSlot.setStatus(_A)
_SfcsANIMPicIndex_Type=Integer32
_SfcsANIMPicIndex_Object=MibTableColumn
sfcsANIMPicIndex=_SfcsANIMPicIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,2),_SfcsANIMPicIndex_Type())
sfcsANIMPicIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicIndex.setStatus(_A)
_SfcsANIMPicLocation_Type=ObjectIdentifier
_SfcsANIMPicLocation_Object=MibTableColumn
sfcsANIMPicLocation=_SfcsANIMPicLocation_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,3),_SfcsANIMPicLocation_Type())
sfcsANIMPicLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicLocation.setStatus(_A)
class _SfcsANIMPicStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('present',2),('notPresent',3),('checkSum',4),('error',5),('limited',6)))
_SfcsANIMPicStatus_Type.__name__=_D
_SfcsANIMPicStatus_Object=MibTableColumn
sfcsANIMPicStatus=_SfcsANIMPicStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,4),_SfcsANIMPicStatus_Type())
sfcsANIMPicStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicStatus.setStatus(_A)
class _SfcsANIMPicVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SfcsANIMPicVersion_Type.__name__=_G
_SfcsANIMPicVersion_Object=MibTableColumn
sfcsANIMPicVersion=_SfcsANIMPicVersion_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,5),_SfcsANIMPicVersion_Type())
sfcsANIMPicVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicVersion.setStatus(_A)
_SfcsANIMPicModuleType_Type=ObjectIdentifier
_SfcsANIMPicModuleType_Object=MibTableColumn
sfcsANIMPicModuleType=_SfcsANIMPicModuleType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,6),_SfcsANIMPicModuleType_Type())
sfcsANIMPicModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicModuleType.setStatus(_A)
class _SfcsANIMPicMfgPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,9));fixedLength=9
_SfcsANIMPicMfgPN_Type.__name__=_G
_SfcsANIMPicMfgPN_Object=MibTableColumn
sfcsANIMPicMfgPN=_SfcsANIMPicMfgPN_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,7),_SfcsANIMPicMfgPN_Type())
sfcsANIMPicMfgPN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgPN.setStatus(_A)
class _SfcsANIMPicMfgSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_SfcsANIMPicMfgSN_Type.__name__=_G
_SfcsANIMPicMfgSN_Object=MibTableColumn
sfcsANIMPicMfgSN=_SfcsANIMPicMfgSN_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,8),_SfcsANIMPicMfgSN_Type())
sfcsANIMPicMfgSN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgSN.setStatus(_A)
class _SfcsANIMPicMfgPartNumb_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_SfcsANIMPicMfgPartNumb_Type.__name__=_G
_SfcsANIMPicMfgPartNumb_Object=MibTableColumn
sfcsANIMPicMfgPartNumb=_SfcsANIMPicMfgPartNumb_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,9),_SfcsANIMPicMfgPartNumb_Type())
sfcsANIMPicMfgPartNumb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgPartNumb.setStatus(_A)
class _SfcsANIMPicMfgSerialNumb_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SfcsANIMPicMfgSerialNumb_Type.__name__=_G
_SfcsANIMPicMfgSerialNumb_Object=MibTableColumn
sfcsANIMPicMfgSerialNumb=_SfcsANIMPicMfgSerialNumb_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,10),_SfcsANIMPicMfgSerialNumb_Type())
sfcsANIMPicMfgSerialNumb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgSerialNumb.setStatus(_A)
class _SfcsANIMPicMfgReworkLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SfcsANIMPicMfgReworkLocation_Type.__name__=_G
_SfcsANIMPicMfgReworkLocation_Object=MibTableColumn
sfcsANIMPicMfgReworkLocation=_SfcsANIMPicMfgReworkLocation_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,11),_SfcsANIMPicMfgReworkLocation_Type())
sfcsANIMPicMfgReworkLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgReworkLocation.setStatus(_A)
class _SfcsANIMPicMfgMfgLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SfcsANIMPicMfgMfgLocation_Type.__name__=_G
_SfcsANIMPicMfgMfgLocation_Object=MibTableColumn
sfcsANIMPicMfgMfgLocation=_SfcsANIMPicMfgMfgLocation_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,12),_SfcsANIMPicMfgMfgLocation_Type())
sfcsANIMPicMfgMfgLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgMfgLocation.setStatus(_A)
class _SfcsANIMPicMfgDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfcsANIMPicMfgDateCode_Type.__name__=_G
_SfcsANIMPicMfgDateCode_Object=MibTableColumn
sfcsANIMPicMfgDateCode=_SfcsANIMPicMfgDateCode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,13),_SfcsANIMPicMfgDateCode_Type())
sfcsANIMPicMfgDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgDateCode.setStatus(_A)
class _SfcsANIMPicMfgRevisionCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfcsANIMPicMfgRevisionCode_Type.__name__=_G
_SfcsANIMPicMfgRevisionCode_Object=MibTableColumn
sfcsANIMPicMfgRevisionCode=_SfcsANIMPicMfgRevisionCode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,14),_SfcsANIMPicMfgRevisionCode_Type())
sfcsANIMPicMfgRevisionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMfgRevisionCode.setStatus(_A)
class _SfcsANIMPicTLPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,9));fixedLength=9
_SfcsANIMPicTLPN_Type.__name__=_G
_SfcsANIMPicTLPN_Object=MibTableColumn
sfcsANIMPicTLPN=_SfcsANIMPicTLPN_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,15),_SfcsANIMPicTLPN_Type())
sfcsANIMPicTLPN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLPN.setStatus(_A)
class _SfcsANIMPicTLSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_SfcsANIMPicTLSN_Type.__name__=_G
_SfcsANIMPicTLSN_Object=MibTableColumn
sfcsANIMPicTLSN=_SfcsANIMPicTLSN_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,16),_SfcsANIMPicTLSN_Type())
sfcsANIMPicTLSN.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLSN.setStatus(_A)
class _SfcsANIMPicTLPartNumb_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_SfcsANIMPicTLPartNumb_Type.__name__=_G
_SfcsANIMPicTLPartNumb_Object=MibTableColumn
sfcsANIMPicTLPartNumb=_SfcsANIMPicTLPartNumb_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,17),_SfcsANIMPicTLPartNumb_Type())
sfcsANIMPicTLPartNumb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLPartNumb.setStatus(_A)
class _SfcsANIMPicTLSerialNumb_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SfcsANIMPicTLSerialNumb_Type.__name__=_G
_SfcsANIMPicTLSerialNumb_Object=MibTableColumn
sfcsANIMPicTLSerialNumb=_SfcsANIMPicTLSerialNumb_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,18),_SfcsANIMPicTLSerialNumb_Type())
sfcsANIMPicTLSerialNumb.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLSerialNumb.setStatus(_A)
class _SfcsANIMPicTLReworkLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SfcsANIMPicTLReworkLocation_Type.__name__=_G
_SfcsANIMPicTLReworkLocation_Object=MibTableColumn
sfcsANIMPicTLReworkLocation=_SfcsANIMPicTLReworkLocation_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,19),_SfcsANIMPicTLReworkLocation_Type())
sfcsANIMPicTLReworkLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLReworkLocation.setStatus(_A)
class _SfcsANIMPicTLMfgLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SfcsANIMPicTLMfgLocation_Type.__name__=_G
_SfcsANIMPicTLMfgLocation_Object=MibTableColumn
sfcsANIMPicTLMfgLocation=_SfcsANIMPicTLMfgLocation_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,20),_SfcsANIMPicTLMfgLocation_Type())
sfcsANIMPicTLMfgLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLMfgLocation.setStatus(_A)
class _SfcsANIMPicTLDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfcsANIMPicTLDateCode_Type.__name__=_G
_SfcsANIMPicTLDateCode_Object=MibTableColumn
sfcsANIMPicTLDateCode=_SfcsANIMPicTLDateCode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,21),_SfcsANIMPicTLDateCode_Type())
sfcsANIMPicTLDateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLDateCode.setStatus(_A)
class _SfcsANIMPicTLRevisionCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfcsANIMPicTLRevisionCode_Type.__name__=_G
_SfcsANIMPicTLRevisionCode_Object=MibTableColumn
sfcsANIMPicTLRevisionCode=_SfcsANIMPicTLRevisionCode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,22),_SfcsANIMPicTLRevisionCode_Type())
sfcsANIMPicTLRevisionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLRevisionCode.setStatus(_A)
class _SfcsANIMPicTLPcbRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SfcsANIMPicTLPcbRevision_Type.__name__=_G
_SfcsANIMPicTLPcbRevision_Object=MibTableColumn
sfcsANIMPicTLPcbRevision=_SfcsANIMPicTLPcbRevision_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,23),_SfcsANIMPicTLPcbRevision_Type())
sfcsANIMPicTLPcbRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicTLPcbRevision.setStatus(_A)
class _SfcsANIMPicMacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_SfcsANIMPicMacAddr_Type.__name__=_M
_SfcsANIMPicMacAddr_Object=MibTableColumn
sfcsANIMPicMacAddr=_SfcsANIMPicMacAddr_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,24),_SfcsANIMPicMacAddr_Type())
sfcsANIMPicMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicMacAddr.setStatus(_A)
_SfcsANIMPicNumbRsvdAddrs_Type=Integer32
_SfcsANIMPicNumbRsvdAddrs_Object=MibTableColumn
sfcsANIMPicNumbRsvdAddrs=_SfcsANIMPicNumbRsvdAddrs_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,25),_SfcsANIMPicNumbRsvdAddrs_Type())
sfcsANIMPicNumbRsvdAddrs.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicNumbRsvdAddrs.setStatus(_A)
class _SfcsANIMPicBoardLevelRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfcsANIMPicBoardLevelRevision_Type.__name__=_G
_SfcsANIMPicBoardLevelRevision_Object=MibTableColumn
sfcsANIMPicBoardLevelRevision=_SfcsANIMPicBoardLevelRevision_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,26),_SfcsANIMPicBoardLevelRevision_Type())
sfcsANIMPicBoardLevelRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicBoardLevelRevision.setStatus(_A)
class _SfcsANIMPicModuleTypeString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SfcsANIMPicModuleTypeString_Type.__name__=_G
_SfcsANIMPicModuleTypeString_Object=MibTableColumn
sfcsANIMPicModuleTypeString=_SfcsANIMPicModuleTypeString_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,27),_SfcsANIMPicModuleTypeString_Type())
sfcsANIMPicModuleTypeString.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicModuleTypeString.setStatus(_A)
class _SfcsANIMPicDcDcConverterType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_SfcsANIMPicDcDcConverterType_Type.__name__=_G
_SfcsANIMPicDcDcConverterType_Object=MibTableColumn
sfcsANIMPicDcDcConverterType=_SfcsANIMPicDcDcConverterType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,28),_SfcsANIMPicDcDcConverterType_Type())
sfcsANIMPicDcDcConverterType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicDcDcConverterType.setStatus(_A)
class _SfcsANIMPicDcDcConverterInputPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_SfcsANIMPicDcDcConverterInputPower_Type.__name__=_G
_SfcsANIMPicDcDcConverterInputPower_Object=MibTableColumn
sfcsANIMPicDcDcConverterInputPower=_SfcsANIMPicDcDcConverterInputPower_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,29),_SfcsANIMPicDcDcConverterInputPower_Type())
sfcsANIMPicDcDcConverterInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicDcDcConverterInputPower.setStatus(_A)
class _SfcsANIMPicSmb1PromVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SfcsANIMPicSmb1PromVersion_Type.__name__=_G
_SfcsANIMPicSmb1PromVersion_Object=MibTableColumn
sfcsANIMPicSmb1PromVersion=_SfcsANIMPicSmb1PromVersion_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,3,3,1,1,30),_SfcsANIMPicSmb1PromVersion_Type())
sfcsANIMPicSmb1PromVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsANIMPicSmb1PromVersion.setStatus(_A)
_SfcsInterface_ObjectIdentity=ObjectIdentity
sfcsInterface=_SfcsInterface_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,4))
_SfcsInterfaceConfig_ObjectIdentity=ObjectIdentity
sfcsInterfaceConfig=_SfcsInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1))
_SfcsInterfaceConfigTable_Object=MibTable
sfcsInterfaceConfigTable=_SfcsInterfaceConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1))
if mibBuilder.loadTexts:sfcsInterfaceConfigTable.setStatus(_A)
_SfcsInterfaceConfigEntry_Object=MibTableRow
sfcsInterfaceConfigEntry=_SfcsInterfaceConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1))
sfcsInterfaceConfigEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:sfcsInterfaceConfigEntry.setStatus(_A)
_SfcsInterfaceConfigInterfaceIndex_Type=Integer32
_SfcsInterfaceConfigInterfaceIndex_Object=MibTableColumn
sfcsInterfaceConfigInterfaceIndex=_SfcsInterfaceConfigInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1,1),_SfcsInterfaceConfigInterfaceIndex_Type())
sfcsInterfaceConfigInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceConfigInterfaceIndex.setStatus(_A)
class _SfcsInterfaceConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_p,2),(_q,3),(_r,4),(_s,5)))
_SfcsInterfaceConfigType_Type.__name__=_D
_SfcsInterfaceConfigType_Object=MibTableColumn
sfcsInterfaceConfigType=_SfcsInterfaceConfigType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1,2),_SfcsInterfaceConfigType_Type())
sfcsInterfaceConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceConfigType.setStatus('deprecated')
class _SfcsInterfacePeakBufferUseage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsInterfacePeakBufferUseage_Type.__name__=_D
_SfcsInterfacePeakBufferUseage_Object=MibTableColumn
sfcsInterfacePeakBufferUseage=_SfcsInterfacePeakBufferUseage_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1,3),_SfcsInterfacePeakBufferUseage_Type())
sfcsInterfacePeakBufferUseage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfacePeakBufferUseage.setStatus(_A)
_SfcsInterfaceConfigNumberOfQueues_Type=Integer32
_SfcsInterfaceConfigNumberOfQueues_Object=MibTableColumn
sfcsInterfaceConfigNumberOfQueues=_SfcsInterfaceConfigNumberOfQueues_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1,4),_SfcsInterfaceConfigNumberOfQueues_Type())
sfcsInterfaceConfigNumberOfQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceConfigNumberOfQueues.setStatus(_A)
_SfcsInterfaceConfigSigStackID_Type=Integer32
_SfcsInterfaceConfigSigStackID_Object=MibTableColumn
sfcsInterfaceConfigSigStackID=_SfcsInterfaceConfigSigStackID_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1,5),_SfcsInterfaceConfigSigStackID_Type())
sfcsInterfaceConfigSigStackID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceConfigSigStackID.setStatus(_A)
class _SfcsInterfaceConfigClockingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),('mother-board-master-clock',2)))
_SfcsInterfaceConfigClockingSource_Type.__name__=_D
_SfcsInterfaceConfigClockingSource_Object=MibTableColumn
sfcsInterfaceConfigClockingSource=_SfcsInterfaceConfigClockingSource_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,1,1,1,6),_SfcsInterfaceConfigClockingSource_Type())
sfcsInterfaceConfigClockingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsInterfaceConfigClockingSource.setStatus(_A)
_SfcsInterfaceStatistics_ObjectIdentity=ObjectIdentity
sfcsInterfaceStatistics=_SfcsInterfaceStatistics_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2))
_SfcsInterfaceStatsTable_Object=MibTable
sfcsInterfaceStatsTable=_SfcsInterfaceStatsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1))
if mibBuilder.loadTexts:sfcsInterfaceStatsTable.setStatus(_A)
_SfcsInterfaceStatsEntry_Object=MibTableRow
sfcsInterfaceStatsEntry=_SfcsInterfaceStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1))
sfcsInterfaceStatsEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:sfcsInterfaceStatsEntry.setStatus(_A)
_SfcsInterfaceStatsInterfaceIndex_Type=Integer32
_SfcsInterfaceStatsInterfaceIndex_Object=MibTableColumn
sfcsInterfaceStatsInterfaceIndex=_SfcsInterfaceStatsInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,1),_SfcsInterfaceStatsInterfaceIndex_Type())
sfcsInterfaceStatsInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsInterfaceIndex.setStatus(_A)
_SfcsInterfaceStatsRxErrors_Type=OctetString
_SfcsInterfaceStatsRxErrors_Object=MibTableColumn
sfcsInterfaceStatsRxErrors=_SfcsInterfaceStatsRxErrors_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,2),_SfcsInterfaceStatsRxErrors_Type())
sfcsInterfaceStatsRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsRxErrors.setStatus(_A)
_SfcsInterfaceStatsVPILookupInvalidErrors_Type=OctetString
_SfcsInterfaceStatsVPILookupInvalidErrors_Object=MibTableColumn
sfcsInterfaceStatsVPILookupInvalidErrors=_SfcsInterfaceStatsVPILookupInvalidErrors_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,3),_SfcsInterfaceStatsVPILookupInvalidErrors_Type())
sfcsInterfaceStatsVPILookupInvalidErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsVPILookupInvalidErrors.setStatus(_A)
_SfcsInterfaceStatsRxCnxLookupInvalidErrors_Type=OctetString
_SfcsInterfaceStatsRxCnxLookupInvalidErrors_Object=MibTableColumn
sfcsInterfaceStatsRxCnxLookupInvalidErrors=_SfcsInterfaceStatsRxCnxLookupInvalidErrors_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,4),_SfcsInterfaceStatsRxCnxLookupInvalidErrors_Type())
sfcsInterfaceStatsRxCnxLookupInvalidErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsRxCnxLookupInvalidErrors.setStatus(_A)
_SfcsInterfaceStatsRxCellCnt_Type=OctetString
_SfcsInterfaceStatsRxCellCnt_Object=MibTableColumn
sfcsInterfaceStatsRxCellCnt=_SfcsInterfaceStatsRxCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,5),_SfcsInterfaceStatsRxCellCnt_Type())
sfcsInterfaceStatsRxCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsRxCellCnt.setStatus(_A)
_SfcsInterfaceStatsTxCellCnt_Type=OctetString
_SfcsInterfaceStatsTxCellCnt_Object=MibTableColumn
sfcsInterfaceStatsTxCellCnt=_SfcsInterfaceStatsTxCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,6),_SfcsInterfaceStatsTxCellCnt_Type())
sfcsInterfaceStatsTxCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsTxCellCnt.setStatus(_A)
_SfcsInterfaceStatsOverflowDropCellCnt_Type=OctetString
_SfcsInterfaceStatsOverflowDropCellCnt_Object=MibTableColumn
sfcsInterfaceStatsOverflowDropCellCnt=_SfcsInterfaceStatsOverflowDropCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,4,2,1,1,7),_SfcsInterfaceStatsOverflowDropCellCnt_Type())
sfcsInterfaceStatsOverflowDropCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsInterfaceStatsOverflowDropCellCnt.setStatus(_A)
_SfcsQueue_ObjectIdentity=ObjectIdentity
sfcsQueue=_SfcsQueue_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,5))
_SfcsQueueConfig_ObjectIdentity=ObjectIdentity
sfcsQueueConfig=_SfcsQueueConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1))
_SfcsQueueConfigTable_Object=MibTable
sfcsQueueConfigTable=_SfcsQueueConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1))
if mibBuilder.loadTexts:sfcsQueueConfigTable.setStatus(_A)
_SfcsQueueConfigEntry_Object=MibTableRow
sfcsQueueConfigEntry=_SfcsQueueConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1))
sfcsQueueConfigEntry.setIndexNames((0,_E,_u),(0,_E,_T))
if mibBuilder.loadTexts:sfcsQueueConfigEntry.setStatus(_A)
_SfcsQueueConfigInterfaceIndex_Type=Integer32
_SfcsQueueConfigInterfaceIndex_Object=MibTableColumn
sfcsQueueConfigInterfaceIndex=_SfcsQueueConfigInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,1),_SfcsQueueConfigInterfaceIndex_Type())
sfcsQueueConfigInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueConfigInterfaceIndex.setStatus(_A)
_SfcsQueueConfigQueueIndex_Type=Integer32
_SfcsQueueConfigQueueIndex_Object=MibTableColumn
sfcsQueueConfigQueueIndex=_SfcsQueueConfigQueueIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,2),_SfcsQueueConfigQueueIndex_Type())
sfcsQueueConfigQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueConfigQueueIndex.setStatus(_A)
_SfcsQueueConfigQueueSize_Type=Integer32
_SfcsQueueConfigQueueSize_Object=MibTableColumn
sfcsQueueConfigQueueSize=_SfcsQueueConfigQueueSize_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,3),_SfcsQueueConfigQueueSize_Type())
sfcsQueueConfigQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueConfigQueueSize.setStatus(_A)
class _SfcsQueueConfigQueueBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsQueueConfigQueueBandwidth_Type.__name__=_D
_SfcsQueueConfigQueueBandwidth_Object=MibTableColumn
sfcsQueueConfigQueueBandwidth=_SfcsQueueConfigQueueBandwidth_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,4),_SfcsQueueConfigQueueBandwidth_Type())
sfcsQueueConfigQueueBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueConfigQueueBandwidth.setStatus(_A)
class _SfcsQueueConfigClpDropThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsQueueConfigClpDropThreshold_Type.__name__=_D
_SfcsQueueConfigClpDropThreshold_Object=MibTableColumn
sfcsQueueConfigClpDropThreshold=_SfcsQueueConfigClpDropThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,5),_SfcsQueueConfigClpDropThreshold_Type())
sfcsQueueConfigClpDropThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsQueueConfigClpDropThreshold.setStatus(_A)
class _SfcsQueueConfigCongestionThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsQueueConfigCongestionThreshold_Type.__name__=_D
_SfcsQueueConfigCongestionThreshold_Object=MibTableColumn
sfcsQueueConfigCongestionThreshold=_SfcsQueueConfigCongestionThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,6),_SfcsQueueConfigCongestionThreshold_Type())
sfcsQueueConfigCongestionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsQueueConfigCongestionThreshold.setStatus(_A)
class _SfcsQueueConfigEFCILowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsQueueConfigEFCILowThreshold_Type.__name__=_D
_SfcsQueueConfigEFCILowThreshold_Object=MibTableColumn
sfcsQueueConfigEFCILowThreshold=_SfcsQueueConfigEFCILowThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,7),_SfcsQueueConfigEFCILowThreshold_Type())
sfcsQueueConfigEFCILowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsQueueConfigEFCILowThreshold.setStatus(_A)
class _SfcsQueueConfigRMThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsQueueConfigRMThreshold_Type.__name__=_D
_SfcsQueueConfigRMThreshold_Object=MibTableColumn
sfcsQueueConfigRMThreshold=_SfcsQueueConfigRMThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,8),_SfcsQueueConfigRMThreshold_Type())
sfcsQueueConfigRMThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsQueueConfigRMThreshold.setStatus(_A)
class _SfcsQueueConfigEPDThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsQueueConfigEPDThreshold_Type.__name__=_D
_SfcsQueueConfigEPDThreshold_Object=MibTableColumn
sfcsQueueConfigEPDThreshold=_SfcsQueueConfigEPDThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,1,1,1,9),_SfcsQueueConfigEPDThreshold_Type())
sfcsQueueConfigEPDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsQueueConfigEPDThreshold.setStatus(_A)
_SfcsQueueStatistics_ObjectIdentity=ObjectIdentity
sfcsQueueStatistics=_SfcsQueueStatistics_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2))
_SfcsQueueStatsTable_Object=MibTable
sfcsQueueStatsTable=_SfcsQueueStatsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1))
if mibBuilder.loadTexts:sfcsQueueStatsTable.setStatus(_A)
_SfcsQueueStatsEntry_Object=MibTableRow
sfcsQueueStatsEntry=_SfcsQueueStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1))
sfcsQueueStatsEntry.setIndexNames((0,_E,_v),(0,_E,_U))
if mibBuilder.loadTexts:sfcsQueueStatsEntry.setStatus(_A)
_SfcsQueueStatsInterfaceIndex_Type=Integer32
_SfcsQueueStatsInterfaceIndex_Object=MibTableColumn
sfcsQueueStatsInterfaceIndex=_SfcsQueueStatsInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1,1),_SfcsQueueStatsInterfaceIndex_Type())
sfcsQueueStatsInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueStatsInterfaceIndex.setStatus(_A)
_SfcsQueueStatsQueue_Type=Integer32
_SfcsQueueStatsQueue_Object=MibTableColumn
sfcsQueueStatsQueue=_SfcsQueueStatsQueue_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1,2),_SfcsQueueStatsQueue_Type())
sfcsQueueStatsQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueStatsQueue.setStatus(_A)
_SfcsQueueStatsTxClpCellsDiscarded_Type=OctetString
_SfcsQueueStatsTxClpCellsDiscarded_Object=MibTableColumn
sfcsQueueStatsTxClpCellsDiscarded=_SfcsQueueStatsTxClpCellsDiscarded_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1,3),_SfcsQueueStatsTxClpCellsDiscarded_Type())
sfcsQueueStatsTxClpCellsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueStatsTxClpCellsDiscarded.setStatus(_A)
_SfcsQueueStatsTxCellsDropped_Type=OctetString
_SfcsQueueStatsTxCellsDropped_Object=MibTableColumn
sfcsQueueStatsTxCellsDropped=_SfcsQueueStatsTxCellsDropped_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1,4),_SfcsQueueStatsTxCellsDropped_Type())
sfcsQueueStatsTxCellsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueStatsTxCellsDropped.setStatus(_A)
_SfcsQueueStatsQueuePeakLevel_Type=Integer32
_SfcsQueueStatsQueuePeakLevel_Object=MibTableColumn
sfcsQueueStatsQueuePeakLevel=_SfcsQueueStatsQueuePeakLevel_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1,5),_SfcsQueueStatsQueuePeakLevel_Type())
sfcsQueueStatsQueuePeakLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueStatsQueuePeakLevel.setStatus(_A)
_SfcsQueueStatsTxCellCnt_Type=OctetString
_SfcsQueueStatsTxCellCnt_Object=MibTableColumn
sfcsQueueStatsTxCellCnt=_SfcsQueueStatsTxCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,5,2,1,1,6),_SfcsQueueStatsTxCellCnt_Type())
sfcsQueueStatsTxCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsQueueStatsTxCellCnt.setStatus(_A)
_SfcsConnection_ObjectIdentity=ObjectIdentity
sfcsConnection=_SfcsConnection_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,7))
_SfcsConnectionConfig_ObjectIdentity=ObjectIdentity
sfcsConnectionConfig=_SfcsConnectionConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1))
_SfcsCnxCfgTable_Object=MibTable
sfcsCnxCfgTable=_SfcsCnxCfgTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1))
if mibBuilder.loadTexts:sfcsCnxCfgTable.setStatus(_A)
_SfcsCnxCfgEntry_Object=MibTableRow
sfcsCnxCfgEntry=_SfcsCnxCfgEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1))
sfcsCnxCfgEntry.setIndexNames((0,_E,_w),(0,_E,_x),(0,_E,_y),(0,_E,_z),(0,_E,_A0),(0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:sfcsCnxCfgEntry.setStatus(_A)
_SfcsCnxCfgCrossConnectIndex_Type=Integer32
_SfcsCnxCfgCrossConnectIndex_Object=MibTableColumn
sfcsCnxCfgCrossConnectIndex=_SfcsCnxCfgCrossConnectIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,1),_SfcsCnxCfgCrossConnectIndex_Type())
sfcsCnxCfgCrossConnectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectIndex.setStatus(_A)
_SfcsCnxCfgCrossConnectLowIfIndex_Type=Integer32
_SfcsCnxCfgCrossConnectLowIfIndex_Object=MibTableColumn
sfcsCnxCfgCrossConnectLowIfIndex=_SfcsCnxCfgCrossConnectLowIfIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,2),_SfcsCnxCfgCrossConnectLowIfIndex_Type())
sfcsCnxCfgCrossConnectLowIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectLowIfIndex.setStatus(_A)
class _SfcsCnxCfgCrossConnectLowVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SfcsCnxCfgCrossConnectLowVpi_Type.__name__=_D
_SfcsCnxCfgCrossConnectLowVpi_Object=MibTableColumn
sfcsCnxCfgCrossConnectLowVpi=_SfcsCnxCfgCrossConnectLowVpi_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,3),_SfcsCnxCfgCrossConnectLowVpi_Type())
sfcsCnxCfgCrossConnectLowVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectLowVpi.setStatus(_A)
class _SfcsCnxCfgCrossConnectLowVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfcsCnxCfgCrossConnectLowVci_Type.__name__=_D
_SfcsCnxCfgCrossConnectLowVci_Object=MibTableColumn
sfcsCnxCfgCrossConnectLowVci=_SfcsCnxCfgCrossConnectLowVci_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,4),_SfcsCnxCfgCrossConnectLowVci_Type())
sfcsCnxCfgCrossConnectLowVci.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectLowVci.setStatus(_A)
_SfcsCnxCfgCrossConnectHighIfIndex_Type=Integer32
_SfcsCnxCfgCrossConnectHighIfIndex_Object=MibTableColumn
sfcsCnxCfgCrossConnectHighIfIndex=_SfcsCnxCfgCrossConnectHighIfIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,5),_SfcsCnxCfgCrossConnectHighIfIndex_Type())
sfcsCnxCfgCrossConnectHighIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectHighIfIndex.setStatus(_A)
class _SfcsCnxCfgCrossConnectHighVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SfcsCnxCfgCrossConnectHighVpi_Type.__name__=_D
_SfcsCnxCfgCrossConnectHighVpi_Object=MibTableColumn
sfcsCnxCfgCrossConnectHighVpi=_SfcsCnxCfgCrossConnectHighVpi_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,6),_SfcsCnxCfgCrossConnectHighVpi_Type())
sfcsCnxCfgCrossConnectHighVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectHighVpi.setStatus(_A)
class _SfcsCnxCfgCrossConnectHighVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfcsCnxCfgCrossConnectHighVci_Type.__name__=_D
_SfcsCnxCfgCrossConnectHighVci_Object=MibTableColumn
sfcsCnxCfgCrossConnectHighVci=_SfcsCnxCfgCrossConnectHighVci_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,7),_SfcsCnxCfgCrossConnectHighVci_Type())
sfcsCnxCfgCrossConnectHighVci.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgCrossConnectHighVci.setStatus(_A)
class _SfcsCnxCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('point-to-point-vpl',1),('point-to-mpoint-vpl',2),('mpoint-to-mpoint-vpl',3),('point-to-point-vcl',4),('point-to-mpoint-vcl',5),('mpoint-to-mpoint-vcl',6)))
_SfcsCnxCfgType_Type.__name__=_D
_SfcsCnxCfgType_Object=MibTableColumn
sfcsCnxCfgType=_SfcsCnxCfgType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,8),_SfcsCnxCfgType_Type())
sfcsCnxCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgType.setStatus(_A)
class _SfcsCnxCfgTmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('efci',2),('er',3)))
_SfcsCnxCfgTmType_Type.__name__=_D
_SfcsCnxCfgTmType_Object=MibTableColumn
sfcsCnxCfgTmType=_SfcsCnxCfgTmType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,9),_SfcsCnxCfgTmType_Type())
sfcsCnxCfgTmType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgTmType.setStatus(_A)
class _SfcsCnxCfgUPCEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('l-h-upc-enabled',1),('l-h-tag-enabled',2),('l-h-upc-tag-enabled',3),('h-l-upc-enabled',4),('l-h-upc-and-h-l-upc-enabled',5),('l-h-Tag-and-h-l-upc-enabled',6),('l-h-upc-tag-and-h-l-upc-enabled',7),('h-l-tag-enabled',8),('l-h-upc-and-h-l-tag-enabled',9),('l-h-tag-and-h-l-tag-enabled',10),('l-h-upc-tag-and-h-l-tag-enabled',11),('h-l-upc-tag-enabled',12),('l-h-upc-and-h-l-upc-tag-enabled',13),('l-h-tag-and-h-l-upc-tag-enabled',14),('l-h-upc-tag-and-h-l-upc-tag-enabled',15)))
_SfcsCnxCfgUPCEnable_Type.__name__=_D
_SfcsCnxCfgUPCEnable_Object=MibTableColumn
sfcsCnxCfgUPCEnable=_SfcsCnxCfgUPCEnable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,10),_SfcsCnxCfgUPCEnable_Type())
sfcsCnxCfgUPCEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgUPCEnable.setStatus(_A)
class _SfcsCnxCfgStatsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_F,3)))
_SfcsCnxCfgStatsEnable_Type.__name__=_D
_SfcsCnxCfgStatsEnable_Object=MibTableColumn
sfcsCnxCfgStatsEnable=_SfcsCnxCfgStatsEnable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,11),_SfcsCnxCfgStatsEnable_Type())
sfcsCnxCfgStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgStatsEnable.setStatus(_A)
class _SfcsCnxCfgStatsTableCounterSizes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('thirtytwobittagcounter',1),('thirtytwobitdropcounter',2),('sixteenbiteachcounter',3)))
_SfcsCnxCfgStatsTableCounterSizes_Type.__name__=_D
_SfcsCnxCfgStatsTableCounterSizes_Object=MibTableColumn
sfcsCnxCfgStatsTableCounterSizes=_SfcsCnxCfgStatsTableCounterSizes_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,12),_SfcsCnxCfgStatsTableCounterSizes_Type())
sfcsCnxCfgStatsTableCounterSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgStatsTableCounterSizes.setStatus(_A)
class _SfcsCnxCfgOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('own',2),('dontown',3)))
_SfcsCnxCfgOwner_Type.__name__=_D
_SfcsCnxCfgOwner_Object=MibTableColumn
sfcsCnxCfgOwner=_SfcsCnxCfgOwner_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,1,1,1,13),_SfcsCnxCfgOwner_Type())
sfcsCnxCfgOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxCfgOwner.setStatus(_A)
_SfcsConnectionStatistics_ObjectIdentity=ObjectIdentity
sfcsConnectionStatistics=_SfcsConnectionStatistics_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2))
_SfcsCnxStatsTable_Object=MibTable
sfcsCnxStatsTable=_SfcsCnxStatsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1))
if mibBuilder.loadTexts:sfcsCnxStatsTable.setStatus(_A)
_SfcsCnxStatsEntry_Object=MibTableRow
sfcsCnxStatsEntry=_SfcsCnxStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1))
sfcsCnxStatsEntry.setIndexNames((0,_E,_A3),(0,_E,_A4),(0,_E,_A5),(0,_E,_A6),(0,_E,_A7),(0,_E,_A8),(0,_E,_A9))
if mibBuilder.loadTexts:sfcsCnxStatsEntry.setStatus(_A)
_SfcsCnxStatsCrossConnectIndex_Type=Integer32
_SfcsCnxStatsCrossConnectIndex_Object=MibTableColumn
sfcsCnxStatsCrossConnectIndex=_SfcsCnxStatsCrossConnectIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,1),_SfcsCnxStatsCrossConnectIndex_Type())
sfcsCnxStatsCrossConnectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectIndex.setStatus(_A)
_SfcsCnxStatsCrossConnectLowIfIndex_Type=Integer32
_SfcsCnxStatsCrossConnectLowIfIndex_Object=MibTableColumn
sfcsCnxStatsCrossConnectLowIfIndex=_SfcsCnxStatsCrossConnectLowIfIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,2),_SfcsCnxStatsCrossConnectLowIfIndex_Type())
sfcsCnxStatsCrossConnectLowIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectLowIfIndex.setStatus(_A)
class _SfcsCnxStatsCrossConnectLowVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SfcsCnxStatsCrossConnectLowVpi_Type.__name__=_D
_SfcsCnxStatsCrossConnectLowVpi_Object=MibTableColumn
sfcsCnxStatsCrossConnectLowVpi=_SfcsCnxStatsCrossConnectLowVpi_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,3),_SfcsCnxStatsCrossConnectLowVpi_Type())
sfcsCnxStatsCrossConnectLowVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectLowVpi.setStatus(_A)
class _SfcsCnxStatsCrossConnectLowVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfcsCnxStatsCrossConnectLowVci_Type.__name__=_D
_SfcsCnxStatsCrossConnectLowVci_Object=MibTableColumn
sfcsCnxStatsCrossConnectLowVci=_SfcsCnxStatsCrossConnectLowVci_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,4),_SfcsCnxStatsCrossConnectLowVci_Type())
sfcsCnxStatsCrossConnectLowVci.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectLowVci.setStatus(_A)
_SfcsCnxStatsCrossConnectHighIfIndex_Type=Integer32
_SfcsCnxStatsCrossConnectHighIfIndex_Object=MibTableColumn
sfcsCnxStatsCrossConnectHighIfIndex=_SfcsCnxStatsCrossConnectHighIfIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,5),_SfcsCnxStatsCrossConnectHighIfIndex_Type())
sfcsCnxStatsCrossConnectHighIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectHighIfIndex.setStatus(_A)
class _SfcsCnxStatsCrossConnectHighVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SfcsCnxStatsCrossConnectHighVpi_Type.__name__=_D
_SfcsCnxStatsCrossConnectHighVpi_Object=MibTableColumn
sfcsCnxStatsCrossConnectHighVpi=_SfcsCnxStatsCrossConnectHighVpi_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,6),_SfcsCnxStatsCrossConnectHighVpi_Type())
sfcsCnxStatsCrossConnectHighVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectHighVpi.setStatus(_A)
class _SfcsCnxStatsCrossConnectHighVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SfcsCnxStatsCrossConnectHighVci_Type.__name__=_D
_SfcsCnxStatsCrossConnectHighVci_Object=MibTableColumn
sfcsCnxStatsCrossConnectHighVci=_SfcsCnxStatsCrossConnectHighVci_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,7),_SfcsCnxStatsCrossConnectHighVci_Type())
sfcsCnxStatsCrossConnectHighVci.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsCrossConnectHighVci.setStatus(_A)
_SfcsCnxStatsLoToHiHTxCells_Type=OctetString
_SfcsCnxStatsLoToHiHTxCells_Object=MibTableColumn
sfcsCnxStatsLoToHiHTxCells=_SfcsCnxStatsLoToHiHTxCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,8),_SfcsCnxStatsLoToHiHTxCells_Type())
sfcsCnxStatsLoToHiHTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsLoToHiHTxCells.setStatus(_A)
_SfcsCnxStatsLoToHiDroppedCells_Type=OctetString
_SfcsCnxStatsLoToHiDroppedCells_Object=MibTableColumn
sfcsCnxStatsLoToHiDroppedCells=_SfcsCnxStatsLoToHiDroppedCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,9),_SfcsCnxStatsLoToHiDroppedCells_Type())
sfcsCnxStatsLoToHiDroppedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsLoToHiDroppedCells.setStatus(_A)
_SfcsCnxStatsLoToHiTaggedCells_Type=OctetString
_SfcsCnxStatsLoToHiTaggedCells_Object=MibTableColumn
sfcsCnxStatsLoToHiTaggedCells=_SfcsCnxStatsLoToHiTaggedCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,10),_SfcsCnxStatsLoToHiTaggedCells_Type())
sfcsCnxStatsLoToHiTaggedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsLoToHiTaggedCells.setStatus(_A)
_SfcsCnxStatsHiToLoHTxCells_Type=OctetString
_SfcsCnxStatsHiToLoHTxCells_Object=MibTableColumn
sfcsCnxStatsHiToLoHTxCells=_SfcsCnxStatsHiToLoHTxCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,11),_SfcsCnxStatsHiToLoHTxCells_Type())
sfcsCnxStatsHiToLoHTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsHiToLoHTxCells.setStatus(_A)
_SfcsCnxStatsHiToLoDroppedCells_Type=OctetString
_SfcsCnxStatsHiToLoDroppedCells_Object=MibTableColumn
sfcsCnxStatsHiToLoDroppedCells=_SfcsCnxStatsHiToLoDroppedCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,12),_SfcsCnxStatsHiToLoDroppedCells_Type())
sfcsCnxStatsHiToLoDroppedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsHiToLoDroppedCells.setStatus(_A)
_SfcsCnxStatsHiToLoTaggedCells_Type=OctetString
_SfcsCnxStatsHiToLoTaggedCells_Object=MibTableColumn
sfcsCnxStatsHiToLoTaggedCells=_SfcsCnxStatsHiToLoTaggedCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,2,1,1,13),_SfcsCnxStatsHiToLoTaggedCells_Type())
sfcsCnxStatsHiToLoTaggedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxStatsHiToLoTaggedCells.setStatus(_A)
_SfcsConnectionError_ObjectIdentity=ObjectIdentity
sfcsConnectionError=_SfcsConnectionError_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,7,3))
_SfcsCnxErrorTable_Object=MibTable
sfcsCnxErrorTable=_SfcsCnxErrorTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,3,1))
if mibBuilder.loadTexts:sfcsCnxErrorTable.setStatus(_A)
_SfcsCnxErrorEntry_Object=MibTableRow
sfcsCnxErrorEntry=_SfcsCnxErrorEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,3,1,1))
sfcsCnxErrorEntry.setIndexNames((0,_J,_Y),(0,_J,_Z),(0,_J,_b),(0,_J,_a),(0,_J,_V),(0,_J,_X),(0,_J,_W))
if mibBuilder.loadTexts:sfcsCnxErrorEntry.setStatus(_A)
_SfcsCnxErrorCode_Type=OctetString
_SfcsCnxErrorCode_Object=MibTableColumn
sfcsCnxErrorCode=_SfcsCnxErrorCode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,3,1,1,1),_SfcsCnxErrorCode_Type())
sfcsCnxErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxErrorCode.setStatus(_A)
_SfcsCnxErrorTimeStamp_Type=TimeTicks
_SfcsCnxErrorTimeStamp_Object=MibTableColumn
sfcsCnxErrorTimeStamp=_SfcsCnxErrorTimeStamp_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,3,1,1,2),_SfcsCnxErrorTimeStamp_Type())
sfcsCnxErrorTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxErrorTimeStamp.setStatus(_A)
class _SfcsCnxErrorRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('inactive',2),('active',3),('delete',4)))
_SfcsCnxErrorRowStatus_Type.__name__=_D
_SfcsCnxErrorRowStatus_Object=MibTableColumn
sfcsCnxErrorRowStatus=_SfcsCnxErrorRowStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,7,3,1,1,3),_SfcsCnxErrorRowStatus_Type())
sfcsCnxErrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCnxErrorRowStatus.setStatus(_A)
_SfcsConnectionAPI_ObjectIdentity=ObjectIdentity
sfcsConnectionAPI=_SfcsConnectionAPI_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,8))
class _SfcsCnxAPIEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_SfcsCnxAPIEntry_Type.__name__=_D
_SfcsCnxAPIEntry_Object=MibScalar
sfcsCnxAPIEntry=_SfcsCnxAPIEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,8,1),_SfcsCnxAPIEntry_Type())
sfcsCnxAPIEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCnxAPIEntry.setStatus(_A)
_SfcsCTM_ObjectIdentity=ObjectIdentity
sfcsCTM=_SfcsCTM_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,9))
_SfcsCTMInterfaceConfig_ObjectIdentity=ObjectIdentity
sfcsCTMInterfaceConfig=_SfcsCTMInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1))
_SfcsCTMInterfaceConfigTable_Object=MibTable
sfcsCTMInterfaceConfigTable=_SfcsCTMInterfaceConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1))
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigTable.setStatus(_A)
_SfcsCTMInterfaceConfigEntry_Object=MibTableRow
sfcsCTMInterfaceConfigEntry=_SfcsCTMInterfaceConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1))
sfcsCTMInterfaceConfigEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigEntry.setStatus(_A)
_SfcsCTMInterfaceConfigInterfaceIndex_Type=Integer32
_SfcsCTMInterfaceConfigInterfaceIndex_Object=MibTableColumn
sfcsCTMInterfaceConfigInterfaceIndex=_SfcsCTMInterfaceConfigInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,1),_SfcsCTMInterfaceConfigInterfaceIndex_Type())
sfcsCTMInterfaceConfigInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigInterfaceIndex.setStatus(_A)
class _SfcsCTMInterfaceConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_p,2),(_q,3),(_r,4),(_s,5)))
_SfcsCTMInterfaceConfigType_Type.__name__=_D
_SfcsCTMInterfaceConfigType_Object=MibTableColumn
sfcsCTMInterfaceConfigType=_SfcsCTMInterfaceConfigType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,2),_SfcsCTMInterfaceConfigType_Type())
sfcsCTMInterfaceConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigType.setStatus(_A)
class _SfcsCTMInterfacePeakBufferUseage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsCTMInterfacePeakBufferUseage_Type.__name__=_D
_SfcsCTMInterfacePeakBufferUseage_Object=MibTableColumn
sfcsCTMInterfacePeakBufferUseage=_SfcsCTMInterfacePeakBufferUseage_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,3),_SfcsCTMInterfacePeakBufferUseage_Type())
sfcsCTMInterfacePeakBufferUseage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfacePeakBufferUseage.setStatus(_A)
_SfcsCTMInterfaceConfigNumberOfQueues_Type=Integer32
_SfcsCTMInterfaceConfigNumberOfQueues_Object=MibTableColumn
sfcsCTMInterfaceConfigNumberOfQueues=_SfcsCTMInterfaceConfigNumberOfQueues_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,4),_SfcsCTMInterfaceConfigNumberOfQueues_Type())
sfcsCTMInterfaceConfigNumberOfQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigNumberOfQueues.setStatus(_A)
_SfcsCTMInterfaceConfigSigStackID_Type=Integer32
_SfcsCTMInterfaceConfigSigStackID_Object=MibTableColumn
sfcsCTMInterfaceConfigSigStackID=_SfcsCTMInterfaceConfigSigStackID_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,5),_SfcsCTMInterfaceConfigSigStackID_Type())
sfcsCTMInterfaceConfigSigStackID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigSigStackID.setStatus(_A)
class _SfcsCTMInterfaceConfigClocking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('generated-transmit-clock',1),('channel-recovered-clock',2),('system-master-clock',3),('not-supported',4)))
_SfcsCTMInterfaceConfigClocking_Type.__name__=_D
_SfcsCTMInterfaceConfigClocking_Object=MibTableColumn
sfcsCTMInterfaceConfigClocking=_SfcsCTMInterfaceConfigClocking_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,6),_SfcsCTMInterfaceConfigClocking_Type())
sfcsCTMInterfaceConfigClocking.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigClocking.setStatus(_A)
_SfcsCTMInterfaceConfigNextVPI_Type=Integer32
_SfcsCTMInterfaceConfigNextVPI_Object=MibTableColumn
sfcsCTMInterfaceConfigNextVPI=_SfcsCTMInterfaceConfigNextVPI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,7),_SfcsCTMInterfaceConfigNextVPI_Type())
sfcsCTMInterfaceConfigNextVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigNextVPI.setStatus(_A)
_SfcsCTMInterfaceConfigNextVCI_Type=Integer32
_SfcsCTMInterfaceConfigNextVCI_Object=MibTableColumn
sfcsCTMInterfaceConfigNextVCI=_SfcsCTMInterfaceConfigNextVCI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,1,1,1,8),_SfcsCTMInterfaceConfigNextVCI_Type())
sfcsCTMInterfaceConfigNextVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceConfigNextVCI.setStatus(_A)
_SfcsCTMInterfaceStatistics_ObjectIdentity=ObjectIdentity
sfcsCTMInterfaceStatistics=_SfcsCTMInterfaceStatistics_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2))
_SfcsCTMInterfaceStatsTable_Object=MibTable
sfcsCTMInterfaceStatsTable=_SfcsCTMInterfaceStatsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1))
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsTable.setStatus(_A)
_SfcsCTMInterfaceStatsEntry_Object=MibTableRow
sfcsCTMInterfaceStatsEntry=_SfcsCTMInterfaceStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1))
sfcsCTMInterfaceStatsEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsEntry.setStatus(_A)
_SfcsCTMInterfaceStatsInterfaceIndex_Type=Integer32
_SfcsCTMInterfaceStatsInterfaceIndex_Object=MibTableColumn
sfcsCTMInterfaceStatsInterfaceIndex=_SfcsCTMInterfaceStatsInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,1),_SfcsCTMInterfaceStatsInterfaceIndex_Type())
sfcsCTMInterfaceStatsInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsInterfaceIndex.setStatus(_A)
_SfcsCTMInterfaceStatsRxErrors_Type=OctetString
_SfcsCTMInterfaceStatsRxErrors_Object=MibTableColumn
sfcsCTMInterfaceStatsRxErrors=_SfcsCTMInterfaceStatsRxErrors_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,2),_SfcsCTMInterfaceStatsRxErrors_Type())
sfcsCTMInterfaceStatsRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsRxErrors.setStatus(_A)
_SfcsCTMInterfaceStatsVPILookupInvalidErrors_Type=OctetString
_SfcsCTMInterfaceStatsVPILookupInvalidErrors_Object=MibTableColumn
sfcsCTMInterfaceStatsVPILookupInvalidErrors=_SfcsCTMInterfaceStatsVPILookupInvalidErrors_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,3),_SfcsCTMInterfaceStatsVPILookupInvalidErrors_Type())
sfcsCTMInterfaceStatsVPILookupInvalidErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsVPILookupInvalidErrors.setStatus(_A)
_SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Type=OctetString
_SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Object=MibTableColumn
sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors=_SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,4),_SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Type())
sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors.setStatus(_A)
_SfcsCTMInterfaceStatsRxCellCnt_Type=OctetString
_SfcsCTMInterfaceStatsRxCellCnt_Object=MibTableColumn
sfcsCTMInterfaceStatsRxCellCnt=_SfcsCTMInterfaceStatsRxCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,7),_SfcsCTMInterfaceStatsRxCellCnt_Type())
sfcsCTMInterfaceStatsRxCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsRxCellCnt.setStatus(_A)
_SfcsCTMInterfaceStatsTxCellCnt_Type=OctetString
_SfcsCTMInterfaceStatsTxCellCnt_Object=MibTableColumn
sfcsCTMInterfaceStatsTxCellCnt=_SfcsCTMInterfaceStatsTxCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,8),_SfcsCTMInterfaceStatsTxCellCnt_Type())
sfcsCTMInterfaceStatsTxCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsTxCellCnt.setStatus(_A)
_SfcsCTMInterfaceStatsOverflowDropCellCnt_Type=OctetString
_SfcsCTMInterfaceStatsOverflowDropCellCnt_Object=MibTableColumn
sfcsCTMInterfaceStatsOverflowDropCellCnt=_SfcsCTMInterfaceStatsOverflowDropCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,2,1,1,9),_SfcsCTMInterfaceStatsOverflowDropCellCnt_Type())
sfcsCTMInterfaceStatsOverflowDropCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMInterfaceStatsOverflowDropCellCnt.setStatus(_A)
_SfcsCTMQueueConfig_ObjectIdentity=ObjectIdentity
sfcsCTMQueueConfig=_SfcsCTMQueueConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3))
_SfcsCTMQueueConfigTable_Object=MibTable
sfcsCTMQueueConfigTable=_SfcsCTMQueueConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1))
if mibBuilder.loadTexts:sfcsCTMQueueConfigTable.setStatus(_A)
_SfcsCTMQueueConfigEntry_Object=MibTableRow
sfcsCTMQueueConfigEntry=_SfcsCTMQueueConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1))
sfcsCTMQueueConfigEntry.setIndexNames((0,_E,_AC),(0,_E,_T))
if mibBuilder.loadTexts:sfcsCTMQueueConfigEntry.setStatus(_A)
_SfcsCTMQueueConfigInterfaceIndex_Type=Integer32
_SfcsCTMQueueConfigInterfaceIndex_Object=MibTableColumn
sfcsCTMQueueConfigInterfaceIndex=_SfcsCTMQueueConfigInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,1),_SfcsCTMQueueConfigInterfaceIndex_Type())
sfcsCTMQueueConfigInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueConfigInterfaceIndex.setStatus(_A)
_SfcsCTMQueueConfigQueueIndex_Type=Integer32
_SfcsCTMQueueConfigQueueIndex_Object=MibTableColumn
sfcsCTMQueueConfigQueueIndex=_SfcsCTMQueueConfigQueueIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,2),_SfcsCTMQueueConfigQueueIndex_Type())
sfcsCTMQueueConfigQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueConfigQueueIndex.setStatus(_A)
_SfcsCTMQueueConfigQueueSize_Type=Integer32
_SfcsCTMQueueConfigQueueSize_Object=MibTableColumn
sfcsCTMQueueConfigQueueSize=_SfcsCTMQueueConfigQueueSize_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,3),_SfcsCTMQueueConfigQueueSize_Type())
sfcsCTMQueueConfigQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMQueueConfigQueueSize.setStatus(_A)
class _SfcsCTMQueueConfigQueueBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsCTMQueueConfigQueueBandwidth_Type.__name__=_D
_SfcsCTMQueueConfigQueueBandwidth_Object=MibTableColumn
sfcsCTMQueueConfigQueueBandwidth=_SfcsCTMQueueConfigQueueBandwidth_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,4),_SfcsCTMQueueConfigQueueBandwidth_Type())
sfcsCTMQueueConfigQueueBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMQueueConfigQueueBandwidth.setStatus(_A)
class _SfcsCTMQueueConfigClpDropThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsCTMQueueConfigClpDropThreshold_Type.__name__=_D
_SfcsCTMQueueConfigClpDropThreshold_Object=MibTableColumn
sfcsCTMQueueConfigClpDropThreshold=_SfcsCTMQueueConfigClpDropThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,5),_SfcsCTMQueueConfigClpDropThreshold_Type())
sfcsCTMQueueConfigClpDropThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMQueueConfigClpDropThreshold.setStatus(_A)
class _SfcsCTMQueueConfigCongestionThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsCTMQueueConfigCongestionThreshold_Type.__name__=_D
_SfcsCTMQueueConfigCongestionThreshold_Object=MibTableColumn
sfcsCTMQueueConfigCongestionThreshold=_SfcsCTMQueueConfigCongestionThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,6),_SfcsCTMQueueConfigCongestionThreshold_Type())
sfcsCTMQueueConfigCongestionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMQueueConfigCongestionThreshold.setStatus(_A)
class _SfcsCTMQueueConfigEFCILowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsCTMQueueConfigEFCILowThreshold_Type.__name__=_D
_SfcsCTMQueueConfigEFCILowThreshold_Object=MibTableColumn
sfcsCTMQueueConfigEFCILowThreshold=_SfcsCTMQueueConfigEFCILowThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,7),_SfcsCTMQueueConfigEFCILowThreshold_Type())
sfcsCTMQueueConfigEFCILowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMQueueConfigEFCILowThreshold.setStatus(_A)
class _SfcsCTMQueueConfigRMThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SfcsCTMQueueConfigRMThreshold_Type.__name__=_D
_SfcsCTMQueueConfigRMThreshold_Object=MibTableColumn
sfcsCTMQueueConfigRMThreshold=_SfcsCTMQueueConfigRMThreshold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,3,1,1,8),_SfcsCTMQueueConfigRMThreshold_Type())
sfcsCTMQueueConfigRMThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsCTMQueueConfigRMThreshold.setStatus(_A)
_SfcsCTMQueueStatistics_ObjectIdentity=ObjectIdentity
sfcsCTMQueueStatistics=_SfcsCTMQueueStatistics_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4))
_SfcsCTMQueueStatsTable_Object=MibTable
sfcsCTMQueueStatsTable=_SfcsCTMQueueStatsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1))
if mibBuilder.loadTexts:sfcsCTMQueueStatsTable.setStatus(_A)
_SfcsCTMQueueStatsEntry_Object=MibTableRow
sfcsCTMQueueStatsEntry=_SfcsCTMQueueStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1))
sfcsCTMQueueStatsEntry.setIndexNames((0,_E,_AD),(0,_E,_U))
if mibBuilder.loadTexts:sfcsCTMQueueStatsEntry.setStatus(_A)
_SfcsCTMQueueStatsInterfaceIndex_Type=Integer32
_SfcsCTMQueueStatsInterfaceIndex_Object=MibTableColumn
sfcsCTMQueueStatsInterfaceIndex=_SfcsCTMQueueStatsInterfaceIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1,1),_SfcsCTMQueueStatsInterfaceIndex_Type())
sfcsCTMQueueStatsInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueStatsInterfaceIndex.setStatus(_A)
_SfcsCTMQueueStatsQueue_Type=Integer32
_SfcsCTMQueueStatsQueue_Object=MibTableColumn
sfcsCTMQueueStatsQueue=_SfcsCTMQueueStatsQueue_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1,2),_SfcsCTMQueueStatsQueue_Type())
sfcsCTMQueueStatsQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueStatsQueue.setStatus(_A)
_SfcsCTMQueueStatsTxClpCellsDiscarded_Type=OctetString
_SfcsCTMQueueStatsTxClpCellsDiscarded_Object=MibTableColumn
sfcsCTMQueueStatsTxClpCellsDiscarded=_SfcsCTMQueueStatsTxClpCellsDiscarded_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1,3),_SfcsCTMQueueStatsTxClpCellsDiscarded_Type())
sfcsCTMQueueStatsTxClpCellsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueStatsTxClpCellsDiscarded.setStatus(_A)
_SfcsCTMQueueStatsTxCellsDropped_Type=OctetString
_SfcsCTMQueueStatsTxCellsDropped_Object=MibTableColumn
sfcsCTMQueueStatsTxCellsDropped=_SfcsCTMQueueStatsTxCellsDropped_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1,4),_SfcsCTMQueueStatsTxCellsDropped_Type())
sfcsCTMQueueStatsTxCellsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueStatsTxCellsDropped.setStatus(_A)
_SfcsCTMQueueStatsQueuePeakLevel_Type=Integer32
_SfcsCTMQueueStatsQueuePeakLevel_Object=MibTableColumn
sfcsCTMQueueStatsQueuePeakLevel=_SfcsCTMQueueStatsQueuePeakLevel_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1,5),_SfcsCTMQueueStatsQueuePeakLevel_Type())
sfcsCTMQueueStatsQueuePeakLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueStatsQueuePeakLevel.setStatus(_A)
_SfcsCTMQueueStatsTxCellCnt_Type=OctetString
_SfcsCTMQueueStatsTxCellCnt_Object=MibTableColumn
sfcsCTMQueueStatsTxCellCnt=_SfcsCTMQueueStatsTxCellCnt_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,9,4,1,1,6),_SfcsCTMQueueStatsTxCellCnt_Type())
sfcsCTMQueueStatsTxCellCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsCTMQueueStatsTxCellCnt.setStatus(_A)
_SfcsBWMgr_ObjectIdentity=ObjectIdentity
sfcsBWMgr=_SfcsBWMgr_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,12))
_SfcsBwNims_ObjectIdentity=ObjectIdentity
sfcsBwNims=_SfcsBwNims_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1))
_SfcsBwNimsTable_Object=MibTable
sfcsBwNimsTable=_SfcsBwNimsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1))
if mibBuilder.loadTexts:sfcsBwNimsTable.setStatus(_A)
_SfcsBwNimsEntry_Object=MibTableRow
sfcsBwNimsEntry=_SfcsBwNimsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1,1))
sfcsBwNimsEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:sfcsBwNimsEntry.setStatus(_A)
_SfcsBwNimsIndex_Type=Integer32
_SfcsBwNimsIndex_Object=MibTableColumn
sfcsBwNimsIndex=_SfcsBwNimsIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1,1,1),_SfcsBwNimsIndex_Type())
sfcsBwNimsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwNimsIndex.setStatus(_A)
_SfcsBwNimsAdminStatus_Type=Integer32
_SfcsBwNimsAdminStatus_Object=MibTableColumn
sfcsBwNimsAdminStatus=_SfcsBwNimsAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1,1,2),_SfcsBwNimsAdminStatus_Type())
sfcsBwNimsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwNimsAdminStatus.setStatus(_A)
_SfcsBWNimsBuffCount_Type=Integer32
_SfcsBWNimsBuffCount_Object=MibTableColumn
sfcsBWNimsBuffCount=_SfcsBWNimsBuffCount_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1,1,3),_SfcsBWNimsBuffCount_Type())
sfcsBWNimsBuffCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBWNimsBuffCount.setStatus(_A)
_SfcsBWNimsPortCount_Type=Integer32
_SfcsBWNimsPortCount_Object=MibTableColumn
sfcsBWNimsPortCount=_SfcsBWNimsPortCount_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1,1,4),_SfcsBWNimsPortCount_Type())
sfcsBWNimsPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBWNimsPortCount.setStatus(_A)
_SfcsBWNimsPrioCount_Type=Integer32
_SfcsBWNimsPrioCount_Object=MibTableColumn
sfcsBWNimsPrioCount=_SfcsBWNimsPrioCount_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,1,1,1,5),_SfcsBWNimsPrioCount_Type())
sfcsBWNimsPrioCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBWNimsPrioCount.setStatus(_A)
_SfcsBwPorts_ObjectIdentity=ObjectIdentity
sfcsBwPorts=_SfcsBwPorts_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2))
_SfcsBwPortsTable_Object=MibTable
sfcsBwPortsTable=_SfcsBwPortsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1))
if mibBuilder.loadTexts:sfcsBwPortsTable.setStatus(_A)
_SfcsBwPortsEntry_Object=MibTableRow
sfcsBwPortsEntry=_SfcsBwPortsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1))
sfcsBwPortsEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:sfcsBwPortsEntry.setStatus(_A)
_SfcsBwPortsIndex_Type=Integer32
_SfcsBwPortsIndex_Object=MibTableColumn
sfcsBwPortsIndex=_SfcsBwPortsIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1,1),_SfcsBwPortsIndex_Type())
sfcsBwPortsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortsIndex.setStatus(_A)
_SfcsBwPortsAdminStatus_Type=Integer32
_SfcsBwPortsAdminStatus_Object=MibTableColumn
sfcsBwPortsAdminStatus=_SfcsBwPortsAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1,2),_SfcsBwPortsAdminStatus_Type())
sfcsBwPortsAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortsAdminStatus.setStatus(_A)
_SfcsBwPortsPhysBwFwd_Type=Integer32
_SfcsBwPortsPhysBwFwd_Object=MibTableColumn
sfcsBwPortsPhysBwFwd=_SfcsBwPortsPhysBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1,3),_SfcsBwPortsPhysBwFwd_Type())
sfcsBwPortsPhysBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortsPhysBwFwd.setStatus(_A)
_SfcsBwPortsPhysBwRev_Type=Integer32
_SfcsBwPortsPhysBwRev_Object=MibTableColumn
sfcsBwPortsPhysBwRev=_SfcsBwPortsPhysBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1,4),_SfcsBwPortsPhysBwRev_Type())
sfcsBwPortsPhysBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortsPhysBwRev.setStatus(_A)
_SfcsBwPortsZone_Type=Integer32
_SfcsBwPortsZone_Object=MibTableColumn
sfcsBwPortsZone=_SfcsBwPortsZone_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1,5),_SfcsBwPortsZone_Type())
sfcsBwPortsZone.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortsZone.setStatus(_A)
_SfcsBwPortsMetric_Type=Integer32
_SfcsBwPortsMetric_Object=MibTableColumn
sfcsBwPortsMetric=_SfcsBwPortsMetric_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,2,1,1,6),_SfcsBwPortsMetric_Type())
sfcsBwPortsMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortsMetric.setStatus(_A)
_SfcsBwPortPools_ObjectIdentity=ObjectIdentity
sfcsBwPortPools=_SfcsBwPortPools_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3))
_SfcsBwPortPoolLimitsTable_Object=MibTable
sfcsBwPortPoolLimitsTable=_SfcsBwPortPoolLimitsTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1))
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsTable.setStatus(_A)
_SfcsBwPortPoolLimitsEntry_Object=MibTableRow
sfcsBwPortPoolLimitsEntry=_SfcsBwPortPoolLimitsEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1))
sfcsBwPortPoolLimitsEntry.setIndexNames((0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsEntry.setStatus(_A)
_SfcsBwPortPoolLimitsIndex_Type=Integer32
_SfcsBwPortPoolLimitsIndex_Object=MibTableColumn
sfcsBwPortPoolLimitsIndex=_SfcsBwPortPoolLimitsIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,1),_SfcsBwPortPoolLimitsIndex_Type())
sfcsBwPortPoolLimitsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsIndex.setStatus(_A)
_SfcsBwPortPoolLimitsPoolIndex_Type=Integer32
_SfcsBwPortPoolLimitsPoolIndex_Object=MibTableColumn
sfcsBwPortPoolLimitsPoolIndex=_SfcsBwPortPoolLimitsPoolIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,2),_SfcsBwPortPoolLimitsPoolIndex_Type())
sfcsBwPortPoolLimitsPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsPoolIndex.setStatus(_A)
_SfcsBwPortPoolLimitsMaxAllocBwFwd_Type=Integer32
_SfcsBwPortPoolLimitsMaxAllocBwFwd_Object=MibTableColumn
sfcsBwPortPoolLimitsMaxAllocBwFwd=_SfcsBwPortPoolLimitsMaxAllocBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,3),_SfcsBwPortPoolLimitsMaxAllocBwFwd_Type())
sfcsBwPortPoolLimitsMaxAllocBwFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsMaxAllocBwFwd.setStatus(_A)
_SfcsBwPortPoolLimitsMaxAllocBwRev_Type=Integer32
_SfcsBwPortPoolLimitsMaxAllocBwRev_Object=MibTableColumn
sfcsBwPortPoolLimitsMaxAllocBwRev=_SfcsBwPortPoolLimitsMaxAllocBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,4),_SfcsBwPortPoolLimitsMaxAllocBwRev_Type())
sfcsBwPortPoolLimitsMaxAllocBwRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsMaxAllocBwRev.setStatus(_A)
_SfcsBwPortPoolLimitsBwAllocStrat_Type=Integer32
_SfcsBwPortPoolLimitsBwAllocStrat_Object=MibTableColumn
sfcsBwPortPoolLimitsBwAllocStrat=_SfcsBwPortPoolLimitsBwAllocStrat_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,5),_SfcsBwPortPoolLimitsBwAllocStrat_Type())
sfcsBwPortPoolLimitsBwAllocStrat.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsBwAllocStrat.setStatus(_A)
_SfcsBwPortPoolLimitsBwConstant_Type=Integer32
_SfcsBwPortPoolLimitsBwConstant_Object=MibTableColumn
sfcsBwPortPoolLimitsBwConstant=_SfcsBwPortPoolLimitsBwConstant_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,6),_SfcsBwPortPoolLimitsBwConstant_Type())
sfcsBwPortPoolLimitsBwConstant.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsBwConstant.setStatus(_A)
_SfcsBwPortPoolLimitsCBRLimitFwd_Type=Integer32
_SfcsBwPortPoolLimitsCBRLimitFwd_Object=MibTableColumn
sfcsBwPortPoolLimitsCBRLimitFwd=_SfcsBwPortPoolLimitsCBRLimitFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,7),_SfcsBwPortPoolLimitsCBRLimitFwd_Type())
sfcsBwPortPoolLimitsCBRLimitFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsCBRLimitFwd.setStatus(_A)
_SfcsBwPortPoolLimitsCBRLimitRev_Type=Integer32
_SfcsBwPortPoolLimitsCBRLimitRev_Object=MibTableColumn
sfcsBwPortPoolLimitsCBRLimitRev=_SfcsBwPortPoolLimitsCBRLimitRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,8),_SfcsBwPortPoolLimitsCBRLimitRev_Type())
sfcsBwPortPoolLimitsCBRLimitRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsCBRLimitRev.setStatus(_A)
_SfcsBwPortPoolLimitsABRLimitFwd_Type=Integer32
_SfcsBwPortPoolLimitsABRLimitFwd_Object=MibTableColumn
sfcsBwPortPoolLimitsABRLimitFwd=_SfcsBwPortPoolLimitsABRLimitFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,9),_SfcsBwPortPoolLimitsABRLimitFwd_Type())
sfcsBwPortPoolLimitsABRLimitFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsABRLimitFwd.setStatus(_A)
_SfcsBwPortPoolLimitsABRLimitRev_Type=Integer32
_SfcsBwPortPoolLimitsABRLimitRev_Object=MibTableColumn
sfcsBwPortPoolLimitsABRLimitRev=_SfcsBwPortPoolLimitsABRLimitRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,10),_SfcsBwPortPoolLimitsABRLimitRev_Type())
sfcsBwPortPoolLimitsABRLimitRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsABRLimitRev.setStatus(_A)
_SfcsBwPortPoolLimitsVBRLimitFwd_Type=Integer32
_SfcsBwPortPoolLimitsVBRLimitFwd_Object=MibTableColumn
sfcsBwPortPoolLimitsVBRLimitFwd=_SfcsBwPortPoolLimitsVBRLimitFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,11),_SfcsBwPortPoolLimitsVBRLimitFwd_Type())
sfcsBwPortPoolLimitsVBRLimitFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsVBRLimitFwd.setStatus(_A)
_SfcsBwPortPoolLimitsVBRLimitRev_Type=Integer32
_SfcsBwPortPoolLimitsVBRLimitRev_Object=MibTableColumn
sfcsBwPortPoolLimitsVBRLimitRev=_SfcsBwPortPoolLimitsVBRLimitRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,12),_SfcsBwPortPoolLimitsVBRLimitRev_Type())
sfcsBwPortPoolLimitsVBRLimitRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsVBRLimitRev.setStatus(_A)
_SfcsBwPortPoolLimitsUBRLimitFwd_Type=Integer32
_SfcsBwPortPoolLimitsUBRLimitFwd_Object=MibTableColumn
sfcsBwPortPoolLimitsUBRLimitFwd=_SfcsBwPortPoolLimitsUBRLimitFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,13),_SfcsBwPortPoolLimitsUBRLimitFwd_Type())
sfcsBwPortPoolLimitsUBRLimitFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsUBRLimitFwd.setStatus(_A)
_SfcsBwPortPoolLimitsUBRLimitRev_Type=Integer32
_SfcsBwPortPoolLimitsUBRLimitRev_Object=MibTableColumn
sfcsBwPortPoolLimitsUBRLimitRev=_SfcsBwPortPoolLimitsUBRLimitRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,14),_SfcsBwPortPoolLimitsUBRLimitRev_Type())
sfcsBwPortPoolLimitsUBRLimitRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsUBRLimitRev.setStatus(_A)
_SfcsBwPortPoolLimitsUBRConnLimitFwd_Type=Integer32
_SfcsBwPortPoolLimitsUBRConnLimitFwd_Object=MibTableColumn
sfcsBwPortPoolLimitsUBRConnLimitFwd=_SfcsBwPortPoolLimitsUBRConnLimitFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,15),_SfcsBwPortPoolLimitsUBRConnLimitFwd_Type())
sfcsBwPortPoolLimitsUBRConnLimitFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsUBRConnLimitFwd.setStatus(_A)
_SfcsBwPortPoolLimitsUBRConnLimitRev_Type=Integer32
_SfcsBwPortPoolLimitsUBRConnLimitRev_Object=MibTableColumn
sfcsBwPortPoolLimitsUBRConnLimitRev=_SfcsBwPortPoolLimitsUBRConnLimitRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,1,1,16),_SfcsBwPortPoolLimitsUBRConnLimitRev_Type())
sfcsBwPortPoolLimitsUBRConnLimitRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolLimitsUBRConnLimitRev.setStatus(_A)
_SfcsBwPortPoolStatTable_Object=MibTable
sfcsBwPortPoolStatTable=_SfcsBwPortPoolStatTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2))
if mibBuilder.loadTexts:sfcsBwPortPoolStatTable.setStatus(_A)
_SfcsBwPortPoolStatEntry_Object=MibTableRow
sfcsBwPortPoolStatEntry=_SfcsBwPortPoolStatEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1))
sfcsBwPortPoolStatEntry.setIndexNames((0,_E,_AI),(0,_E,_AJ))
if mibBuilder.loadTexts:sfcsBwPortPoolStatEntry.setStatus(_A)
_SfcsBwPortPoolStatsIndex_Type=Integer32
_SfcsBwPortPoolStatsIndex_Object=MibTableColumn
sfcsBwPortPoolStatsIndex=_SfcsBwPortPoolStatsIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,1),_SfcsBwPortPoolStatsIndex_Type())
sfcsBwPortPoolStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatsIndex.setStatus(_A)
_SfcsBwPortPoolStatsPoolIndex_Type=Integer32
_SfcsBwPortPoolStatsPoolIndex_Object=MibTableColumn
sfcsBwPortPoolStatsPoolIndex=_SfcsBwPortPoolStatsPoolIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,2),_SfcsBwPortPoolStatsPoolIndex_Type())
sfcsBwPortPoolStatsPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatsPoolIndex.setStatus(_A)
_SfcsBwPortPoolStatConnCntFwd_Type=Integer32
_SfcsBwPortPoolStatConnCntFwd_Object=MibTableColumn
sfcsBwPortPoolStatConnCntFwd=_SfcsBwPortPoolStatConnCntFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,3),_SfcsBwPortPoolStatConnCntFwd_Type())
sfcsBwPortPoolStatConnCntFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatConnCntFwd.setStatus(_A)
_SfcsBwPortPoolStatConnCntRev_Type=Integer32
_SfcsBwPortPoolStatConnCntRev_Object=MibTableColumn
sfcsBwPortPoolStatConnCntRev=_SfcsBwPortPoolStatConnCntRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,4),_SfcsBwPortPoolStatConnCntRev_Type())
sfcsBwPortPoolStatConnCntRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatConnCntRev.setStatus(_A)
_SfcsBwPortPoolStatAllocBwFwd_Type=Integer32
_SfcsBwPortPoolStatAllocBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatAllocBwFwd=_SfcsBwPortPoolStatAllocBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,5),_SfcsBwPortPoolStatAllocBwFwd_Type())
sfcsBwPortPoolStatAllocBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatAllocBwFwd.setStatus(_A)
_SfcsBwPortPoolStatAllocBwRev_Type=Integer32
_SfcsBwPortPoolStatAllocBwRev_Object=MibTableColumn
sfcsBwPortPoolStatAllocBwRev=_SfcsBwPortPoolStatAllocBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,6),_SfcsBwPortPoolStatAllocBwRev_Type())
sfcsBwPortPoolStatAllocBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatAllocBwRev.setStatus(_A)
_SfcsBwPortPoolStatAvailBwFwd_Type=Integer32
_SfcsBwPortPoolStatAvailBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatAvailBwFwd=_SfcsBwPortPoolStatAvailBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,7),_SfcsBwPortPoolStatAvailBwFwd_Type())
sfcsBwPortPoolStatAvailBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatAvailBwFwd.setStatus(_A)
_SfcsBwPortPoolStatAvailBwRev_Type=Integer32
_SfcsBwPortPoolStatAvailBwRev_Object=MibTableColumn
sfcsBwPortPoolStatAvailBwRev=_SfcsBwPortPoolStatAvailBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,8),_SfcsBwPortPoolStatAvailBwRev_Type())
sfcsBwPortPoolStatAvailBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatAvailBwRev.setStatus(_A)
_SfcsBwPortPoolStatPeakBwFwd_Type=Integer32
_SfcsBwPortPoolStatPeakBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatPeakBwFwd=_SfcsBwPortPoolStatPeakBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,9),_SfcsBwPortPoolStatPeakBwFwd_Type())
sfcsBwPortPoolStatPeakBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatPeakBwFwd.setStatus(_A)
_SfcsBwPortPoolStatPeakBwRev_Type=Integer32
_SfcsBwPortPoolStatPeakBwRev_Object=MibTableColumn
sfcsBwPortPoolStatPeakBwRev=_SfcsBwPortPoolStatPeakBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,10),_SfcsBwPortPoolStatPeakBwRev_Type())
sfcsBwPortPoolStatPeakBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatPeakBwRev.setStatus(_A)
_SfcsBwPortPoolStatRejConnFwd_Type=Integer32
_SfcsBwPortPoolStatRejConnFwd_Object=MibTableColumn
sfcsBwPortPoolStatRejConnFwd=_SfcsBwPortPoolStatRejConnFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,11),_SfcsBwPortPoolStatRejConnFwd_Type())
sfcsBwPortPoolStatRejConnFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatRejConnFwd.setStatus(_A)
_SfcsBwPortPoolStatRejConnRev_Type=Integer32
_SfcsBwPortPoolStatRejConnRev_Object=MibTableColumn
sfcsBwPortPoolStatRejConnRev=_SfcsBwPortPoolStatRejConnRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,12),_SfcsBwPortPoolStatRejConnRev_Type())
sfcsBwPortPoolStatRejConnRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatRejConnRev.setStatus(_A)
_SfcsBwPortPoolStatPrevAdverMAXCRFwd_Type=Integer32
_SfcsBwPortPoolStatPrevAdverMAXCRFwd_Object=MibTableColumn
sfcsBwPortPoolStatPrevAdverMAXCRFwd=_SfcsBwPortPoolStatPrevAdverMAXCRFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,13),_SfcsBwPortPoolStatPrevAdverMAXCRFwd_Type())
sfcsBwPortPoolStatPrevAdverMAXCRFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatPrevAdverMAXCRFwd.setStatus(_A)
_SfcsBwPortPoolStatPrevAdverMAXCRRev_Type=Integer32
_SfcsBwPortPoolStatPrevAdverMAXCRRev_Object=MibTableColumn
sfcsBwPortPoolStatPrevAdverMAXCRRev=_SfcsBwPortPoolStatPrevAdverMAXCRRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,14),_SfcsBwPortPoolStatPrevAdverMAXCRRev_Type())
sfcsBwPortPoolStatPrevAdverMAXCRRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatPrevAdverMAXCRRev.setStatus(_A)
_SfcsBwPortPoolStatPrevAdverAvailCRFwd_Type=Integer32
_SfcsBwPortPoolStatPrevAdverAvailCRFwd_Object=MibTableColumn
sfcsBwPortPoolStatPrevAdverAvailCRFwd=_SfcsBwPortPoolStatPrevAdverAvailCRFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,15),_SfcsBwPortPoolStatPrevAdverAvailCRFwd_Type())
sfcsBwPortPoolStatPrevAdverAvailCRFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatPrevAdverAvailCRFwd.setStatus(_A)
_SfcsBwPortPoolStatPrevAdverAvailCRRev_Type=Integer32
_SfcsBwPortPoolStatPrevAdverAvailCRRev_Object=MibTableColumn
sfcsBwPortPoolStatPrevAdverAvailCRRev=_SfcsBwPortPoolStatPrevAdverAvailCRRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,16),_SfcsBwPortPoolStatPrevAdverAvailCRRev_Type())
sfcsBwPortPoolStatPrevAdverAvailCRRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatPrevAdverAvailCRRev.setStatus(_A)
_SfcsBwPortPoolStatCBRConnCntFwd_Type=Integer32
_SfcsBwPortPoolStatCBRConnCntFwd_Object=MibTableColumn
sfcsBwPortPoolStatCBRConnCntFwd=_SfcsBwPortPoolStatCBRConnCntFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,17),_SfcsBwPortPoolStatCBRConnCntFwd_Type())
sfcsBwPortPoolStatCBRConnCntFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRConnCntFwd.setStatus(_A)
_SfcsBwPortPoolStatCBRConnCntRev_Type=Integer32
_SfcsBwPortPoolStatCBRConnCntRev_Object=MibTableColumn
sfcsBwPortPoolStatCBRConnCntRev=_SfcsBwPortPoolStatCBRConnCntRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,18),_SfcsBwPortPoolStatCBRConnCntRev_Type())
sfcsBwPortPoolStatCBRConnCntRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRConnCntRev.setStatus(_A)
_SfcsBwPortPoolStatCBRConnRejFwd_Type=Integer32
_SfcsBwPortPoolStatCBRConnRejFwd_Object=MibTableColumn
sfcsBwPortPoolStatCBRConnRejFwd=_SfcsBwPortPoolStatCBRConnRejFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,19),_SfcsBwPortPoolStatCBRConnRejFwd_Type())
sfcsBwPortPoolStatCBRConnRejFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRConnRejFwd.setStatus(_A)
_SfcsBwPortPoolStatCBRConnRejRev_Type=Integer32
_SfcsBwPortPoolStatCBRConnRejRev_Object=MibTableColumn
sfcsBwPortPoolStatCBRConnRejRev=_SfcsBwPortPoolStatCBRConnRejRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,20),_SfcsBwPortPoolStatCBRConnRejRev_Type())
sfcsBwPortPoolStatCBRConnRejRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRConnRejRev.setStatus(_A)
_SfcsBwPortPoolStatCBRAllocBwFwd_Type=Integer32
_SfcsBwPortPoolStatCBRAllocBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatCBRAllocBwFwd=_SfcsBwPortPoolStatCBRAllocBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,21),_SfcsBwPortPoolStatCBRAllocBwFwd_Type())
sfcsBwPortPoolStatCBRAllocBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRAllocBwFwd.setStatus(_A)
_SfcsBwPortPoolStatCBRAllocBwRev_Type=Integer32
_SfcsBwPortPoolStatCBRAllocBwRev_Object=MibTableColumn
sfcsBwPortPoolStatCBRAllocBwRev=_SfcsBwPortPoolStatCBRAllocBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,22),_SfcsBwPortPoolStatCBRAllocBwRev_Type())
sfcsBwPortPoolStatCBRAllocBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRAllocBwRev.setStatus(_A)
_SfcsBwPortPoolStatCBRAggPCRFwd_Type=Integer32
_SfcsBwPortPoolStatCBRAggPCRFwd_Object=MibTableColumn
sfcsBwPortPoolStatCBRAggPCRFwd=_SfcsBwPortPoolStatCBRAggPCRFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,23),_SfcsBwPortPoolStatCBRAggPCRFwd_Type())
sfcsBwPortPoolStatCBRAggPCRFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRAggPCRFwd.setStatus(_A)
_SfcsBwPortPoolStatCBRAggPCRRev_Type=Integer32
_SfcsBwPortPoolStatCBRAggPCRRev_Object=MibTableColumn
sfcsBwPortPoolStatCBRAggPCRRev=_SfcsBwPortPoolStatCBRAggPCRRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,24),_SfcsBwPortPoolStatCBRAggPCRRev_Type())
sfcsBwPortPoolStatCBRAggPCRRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRAggPCRRev.setStatus(_A)
_SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Type=Integer32
_SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Object=MibTableColumn
sfcsBwPortPoolStatCBRPrevAdverMAXCTD=_SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,25),_SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Type())
sfcsBwPortPoolStatCBRPrevAdverMAXCTD.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRPrevAdverMAXCTD.setStatus(_A)
_SfcsBwPortPoolStatCBRPrevAdverCDV_Type=Integer32
_SfcsBwPortPoolStatCBRPrevAdverCDV_Object=MibTableColumn
sfcsBwPortPoolStatCBRPrevAdverCDV=_SfcsBwPortPoolStatCBRPrevAdverCDV_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,26),_SfcsBwPortPoolStatCBRPrevAdverCDV_Type())
sfcsBwPortPoolStatCBRPrevAdverCDV.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatCBRPrevAdverCDV.setStatus(_A)
_SfcsBwPortPoolStatABRConnCntFwd_Type=Integer32
_SfcsBwPortPoolStatABRConnCntFwd_Object=MibTableColumn
sfcsBwPortPoolStatABRConnCntFwd=_SfcsBwPortPoolStatABRConnCntFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,27),_SfcsBwPortPoolStatABRConnCntFwd_Type())
sfcsBwPortPoolStatABRConnCntFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRConnCntFwd.setStatus(_A)
_SfcsBwPortPoolStatABRConnCntRev_Type=Integer32
_SfcsBwPortPoolStatABRConnCntRev_Object=MibTableColumn
sfcsBwPortPoolStatABRConnCntRev=_SfcsBwPortPoolStatABRConnCntRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,28),_SfcsBwPortPoolStatABRConnCntRev_Type())
sfcsBwPortPoolStatABRConnCntRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRConnCntRev.setStatus(_A)
_SfcsBwPortPoolStatABRConnRejFwd_Type=Integer32
_SfcsBwPortPoolStatABRConnRejFwd_Object=MibTableColumn
sfcsBwPortPoolStatABRConnRejFwd=_SfcsBwPortPoolStatABRConnRejFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,29),_SfcsBwPortPoolStatABRConnRejFwd_Type())
sfcsBwPortPoolStatABRConnRejFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRConnRejFwd.setStatus(_A)
_SfcsBwPortPoolStatABRConnRejRev_Type=Integer32
_SfcsBwPortPoolStatABRConnRejRev_Object=MibTableColumn
sfcsBwPortPoolStatABRConnRejRev=_SfcsBwPortPoolStatABRConnRejRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,30),_SfcsBwPortPoolStatABRConnRejRev_Type())
sfcsBwPortPoolStatABRConnRejRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRConnRejRev.setStatus(_A)
_SfcsBwPortPoolStatABRAllocBwFwd_Type=Integer32
_SfcsBwPortPoolStatABRAllocBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatABRAllocBwFwd=_SfcsBwPortPoolStatABRAllocBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,31),_SfcsBwPortPoolStatABRAllocBwFwd_Type())
sfcsBwPortPoolStatABRAllocBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRAllocBwFwd.setStatus(_A)
_SfcsBwPortPoolStatABRAllocBwRev_Type=Integer32
_SfcsBwPortPoolStatABRAllocBwRev_Object=MibTableColumn
sfcsBwPortPoolStatABRAllocBwRev=_SfcsBwPortPoolStatABRAllocBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,32),_SfcsBwPortPoolStatABRAllocBwRev_Type())
sfcsBwPortPoolStatABRAllocBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRAllocBwRev.setStatus(_A)
_SfcsBwPortPoolStatABRAggPCRFwd_Type=Integer32
_SfcsBwPortPoolStatABRAggPCRFwd_Object=MibTableColumn
sfcsBwPortPoolStatABRAggPCRFwd=_SfcsBwPortPoolStatABRAggPCRFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,33),_SfcsBwPortPoolStatABRAggPCRFwd_Type())
sfcsBwPortPoolStatABRAggPCRFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRAggPCRFwd.setStatus(_A)
_SfcsBwPortPoolStatABRAggPCRRev_Type=Integer32
_SfcsBwPortPoolStatABRAggPCRRev_Object=MibTableColumn
sfcsBwPortPoolStatABRAggPCRRev=_SfcsBwPortPoolStatABRAggPCRRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,34),_SfcsBwPortPoolStatABRAggPCRRev_Type())
sfcsBwPortPoolStatABRAggPCRRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRAggPCRRev.setStatus(_A)
_SfcsBwPortPoolStatABRPrevAdverMAXCTD_Type=Integer32
_SfcsBwPortPoolStatABRPrevAdverMAXCTD_Object=MibTableColumn
sfcsBwPortPoolStatABRPrevAdverMAXCTD=_SfcsBwPortPoolStatABRPrevAdverMAXCTD_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,35),_SfcsBwPortPoolStatABRPrevAdverMAXCTD_Type())
sfcsBwPortPoolStatABRPrevAdverMAXCTD.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRPrevAdverMAXCTD.setStatus(_A)
_SfcsBwPortPoolStatABRPrevAdverCDV_Type=Integer32
_SfcsBwPortPoolStatABRPrevAdverCDV_Object=MibTableColumn
sfcsBwPortPoolStatABRPrevAdverCDV=_SfcsBwPortPoolStatABRPrevAdverCDV_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,36),_SfcsBwPortPoolStatABRPrevAdverCDV_Type())
sfcsBwPortPoolStatABRPrevAdverCDV.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatABRPrevAdverCDV.setStatus(_A)
_SfcsBwPortPoolStatVBRConnCntFwd_Type=Integer32
_SfcsBwPortPoolStatVBRConnCntFwd_Object=MibTableColumn
sfcsBwPortPoolStatVBRConnCntFwd=_SfcsBwPortPoolStatVBRConnCntFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,37),_SfcsBwPortPoolStatVBRConnCntFwd_Type())
sfcsBwPortPoolStatVBRConnCntFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRConnCntFwd.setStatus(_A)
_SfcsBwPortPoolStatVBRConnCntRev_Type=Integer32
_SfcsBwPortPoolStatVBRConnCntRev_Object=MibTableColumn
sfcsBwPortPoolStatVBRConnCntRev=_SfcsBwPortPoolStatVBRConnCntRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,38),_SfcsBwPortPoolStatVBRConnCntRev_Type())
sfcsBwPortPoolStatVBRConnCntRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRConnCntRev.setStatus(_A)
_SfcsBwPortPoolStatVBRConnRejFwd_Type=Integer32
_SfcsBwPortPoolStatVBRConnRejFwd_Object=MibTableColumn
sfcsBwPortPoolStatVBRConnRejFwd=_SfcsBwPortPoolStatVBRConnRejFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,39),_SfcsBwPortPoolStatVBRConnRejFwd_Type())
sfcsBwPortPoolStatVBRConnRejFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRConnRejFwd.setStatus(_A)
_SfcsBwPortPoolStatVBRConnRejRev_Type=Integer32
_SfcsBwPortPoolStatVBRConnRejRev_Object=MibTableColumn
sfcsBwPortPoolStatVBRConnRejRev=_SfcsBwPortPoolStatVBRConnRejRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,40),_SfcsBwPortPoolStatVBRConnRejRev_Type())
sfcsBwPortPoolStatVBRConnRejRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRConnRejRev.setStatus(_A)
_SfcsBwPortPoolStatVBRAllocBwFwd_Type=Integer32
_SfcsBwPortPoolStatVBRAllocBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatVBRAllocBwFwd=_SfcsBwPortPoolStatVBRAllocBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,41),_SfcsBwPortPoolStatVBRAllocBwFwd_Type())
sfcsBwPortPoolStatVBRAllocBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRAllocBwFwd.setStatus(_A)
_SfcsBwPortPoolStatVBRAllocBwRev_Type=Integer32
_SfcsBwPortPoolStatVBRAllocBwRev_Object=MibTableColumn
sfcsBwPortPoolStatVBRAllocBwRev=_SfcsBwPortPoolStatVBRAllocBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,42),_SfcsBwPortPoolStatVBRAllocBwRev_Type())
sfcsBwPortPoolStatVBRAllocBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRAllocBwRev.setStatus(_A)
_SfcsBwPortPoolStatVBRAggPCRFwd_Type=Integer32
_SfcsBwPortPoolStatVBRAggPCRFwd_Object=MibTableColumn
sfcsBwPortPoolStatVBRAggPCRFwd=_SfcsBwPortPoolStatVBRAggPCRFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,43),_SfcsBwPortPoolStatVBRAggPCRFwd_Type())
sfcsBwPortPoolStatVBRAggPCRFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRAggPCRFwd.setStatus(_A)
_SfcsBwPortPoolStatVBRAggPCRRev_Type=Integer32
_SfcsBwPortPoolStatVBRAggPCRRev_Object=MibTableColumn
sfcsBwPortPoolStatVBRAggPCRRev=_SfcsBwPortPoolStatVBRAggPCRRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,44),_SfcsBwPortPoolStatVBRAggPCRRev_Type())
sfcsBwPortPoolStatVBRAggPCRRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRAggPCRRev.setStatus(_A)
_SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Type=Integer32
_SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Object=MibTableColumn
sfcsBwPortPoolStatVBRPrevAdverMAXCTD=_SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,45),_SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Type())
sfcsBwPortPoolStatVBRPrevAdverMAXCTD.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRPrevAdverMAXCTD.setStatus(_A)
_SfcsBwPortPoolStatVBRPrevAdverCDV_Type=Integer32
_SfcsBwPortPoolStatVBRPrevAdverCDV_Object=MibTableColumn
sfcsBwPortPoolStatVBRPrevAdverCDV=_SfcsBwPortPoolStatVBRPrevAdverCDV_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,46),_SfcsBwPortPoolStatVBRPrevAdverCDV_Type())
sfcsBwPortPoolStatVBRPrevAdverCDV.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatVBRPrevAdverCDV.setStatus(_A)
_SfcsBwPortPoolStatUBRConnCntFwd_Type=Integer32
_SfcsBwPortPoolStatUBRConnCntFwd_Object=MibTableColumn
sfcsBwPortPoolStatUBRConnCntFwd=_SfcsBwPortPoolStatUBRConnCntFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,47),_SfcsBwPortPoolStatUBRConnCntFwd_Type())
sfcsBwPortPoolStatUBRConnCntFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRConnCntFwd.setStatus(_A)
_SfcsBwPortPoolStatUBRConnCntRev_Type=Integer32
_SfcsBwPortPoolStatUBRConnCntRev_Object=MibTableColumn
sfcsBwPortPoolStatUBRConnCntRev=_SfcsBwPortPoolStatUBRConnCntRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,48),_SfcsBwPortPoolStatUBRConnCntRev_Type())
sfcsBwPortPoolStatUBRConnCntRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRConnCntRev.setStatus(_A)
_SfcsBwPortPoolStatUBRConnRejFwd_Type=Integer32
_SfcsBwPortPoolStatUBRConnRejFwd_Object=MibTableColumn
sfcsBwPortPoolStatUBRConnRejFwd=_SfcsBwPortPoolStatUBRConnRejFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,49),_SfcsBwPortPoolStatUBRConnRejFwd_Type())
sfcsBwPortPoolStatUBRConnRejFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRConnRejFwd.setStatus(_A)
_SfcsBwPortPoolStatUBRConnRejRev_Type=Integer32
_SfcsBwPortPoolStatUBRConnRejRev_Object=MibTableColumn
sfcsBwPortPoolStatUBRConnRejRev=_SfcsBwPortPoolStatUBRConnRejRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,50),_SfcsBwPortPoolStatUBRConnRejRev_Type())
sfcsBwPortPoolStatUBRConnRejRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRConnRejRev.setStatus(_A)
_SfcsBwPortPoolStatUBRAllocBwFwd_Type=Integer32
_SfcsBwPortPoolStatUBRAllocBwFwd_Object=MibTableColumn
sfcsBwPortPoolStatUBRAllocBwFwd=_SfcsBwPortPoolStatUBRAllocBwFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,51),_SfcsBwPortPoolStatUBRAllocBwFwd_Type())
sfcsBwPortPoolStatUBRAllocBwFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRAllocBwFwd.setStatus(_A)
_SfcsBwPortPoolStatUBRAllocBwRev_Type=Integer32
_SfcsBwPortPoolStatUBRAllocBwRev_Object=MibTableColumn
sfcsBwPortPoolStatUBRAllocBwRev=_SfcsBwPortPoolStatUBRAllocBwRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,52),_SfcsBwPortPoolStatUBRAllocBwRev_Type())
sfcsBwPortPoolStatUBRAllocBwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRAllocBwRev.setStatus(_A)
_SfcsBwPortPoolStatUBRAggPCRFwd_Type=Integer32
_SfcsBwPortPoolStatUBRAggPCRFwd_Object=MibTableColumn
sfcsBwPortPoolStatUBRAggPCRFwd=_SfcsBwPortPoolStatUBRAggPCRFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,53),_SfcsBwPortPoolStatUBRAggPCRFwd_Type())
sfcsBwPortPoolStatUBRAggPCRFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRAggPCRFwd.setStatus(_A)
_SfcsBwPortPoolStatUBRAggPCRRev_Type=Integer32
_SfcsBwPortPoolStatUBRAggPCRRev_Object=MibTableColumn
sfcsBwPortPoolStatUBRAggPCRRev=_SfcsBwPortPoolStatUBRAggPCRRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,54),_SfcsBwPortPoolStatUBRAggPCRRev_Type())
sfcsBwPortPoolStatUBRAggPCRRev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRAggPCRRev.setStatus(_A)
_SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Type=Integer32
_SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Object=MibTableColumn
sfcsBwPortPoolStatUBRPrevAdverMAXCTD=_SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,55),_SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Type())
sfcsBwPortPoolStatUBRPrevAdverMAXCTD.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRPrevAdverMAXCTD.setStatus(_A)
_SfcsBwPortPoolStatUBRPrevAdverCDV_Type=Integer32
_SfcsBwPortPoolStatUBRPrevAdverCDV_Object=MibTableColumn
sfcsBwPortPoolStatUBRPrevAdverCDV=_SfcsBwPortPoolStatUBRPrevAdverCDV_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,2,1,56),_SfcsBwPortPoolStatUBRPrevAdverCDV_Type())
sfcsBwPortPoolStatUBRPrevAdverCDV.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolStatUBRPrevAdverCDV.setStatus(_A)
_SfcsBwPortPoolTrapMgmtTable_Object=MibTable
sfcsBwPortPoolTrapMgmtTable=_SfcsBwPortPoolTrapMgmtTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3))
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtTable.setStatus(_A)
_SfcsBwPortPoolTrapMgmtEntry_Object=MibTableRow
sfcsBwPortPoolTrapMgmtEntry=_SfcsBwPortPoolTrapMgmtEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1))
sfcsBwPortPoolTrapMgmtEntry.setIndexNames((0,_E,_AK),(0,_E,_AL))
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtEntry.setStatus(_A)
_SfcsBwPortPoolTrapMgmtIndex_Type=Integer32
_SfcsBwPortPoolTrapMgmtIndex_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtIndex=_SfcsBwPortPoolTrapMgmtIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,1),_SfcsBwPortPoolTrapMgmtIndex_Type())
sfcsBwPortPoolTrapMgmtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtIndex.setStatus(_A)
_SfcsBwPortPoolTrapMgmtPoolIndex_Type=Integer32
_SfcsBwPortPoolTrapMgmtPoolIndex_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtPoolIndex=_SfcsBwPortPoolTrapMgmtPoolIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,2),_SfcsBwPortPoolTrapMgmtPoolIndex_Type())
sfcsBwPortPoolTrapMgmtPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtPoolIndex.setStatus(_A)
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd=_SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,3),_SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev=_SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,4),_SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd=_SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,5),_SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev=_SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,6),_SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtPeakBwTholdFwd=_SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,7),_SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Type())
sfcsBwPortPoolTrapMgmtPeakBwTholdFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtPeakBwTholdFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtPeakBwTholdRev=_SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,8),_SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Type())
sfcsBwPortPoolTrapMgmtPeakBwTholdRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtPeakBwTholdRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtHoldDownTime_Type=Integer32
_SfcsBwPortPoolTrapMgmtHoldDownTime_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtHoldDownTime=_SfcsBwPortPoolTrapMgmtHoldDownTime_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,9),_SfcsBwPortPoolTrapMgmtHoldDownTime_Type())
sfcsBwPortPoolTrapMgmtHoldDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtHoldDownTime.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd=_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,10),_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev=_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,11),_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd=_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,12),_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev=_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,13),_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd=_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,14),_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev=_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,15),_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd=_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,16),_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev=_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,17),_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd=_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,18),_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev=_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,19),_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd=_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,20),_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev=_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,21),_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd=_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,22),_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev=_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,23),_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd=_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,24),_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev=_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,25),_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd=_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,26),_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev=_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,27),_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd=_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,28),_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev=_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,29),_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd=_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,30),_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev=_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,31),_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd=_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,32),_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev=_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,33),_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd=_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,34),_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev=_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,35),_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd=_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,36),_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev=_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,37),_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd=_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,38),_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Type())
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev=_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,39),_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Type())
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd=_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,40),_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Type())
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd.setStatus(_A)
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Type=Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Object=MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev=_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,41),_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Type())
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev.setStatus(_A)
_SfcsBWPortPoolTrapMgmtBuffUpThold_Type=Integer32
_SfcsBWPortPoolTrapMgmtBuffUpThold_Object=MibTableColumn
sfcsBWPortPoolTrapMgmtBuffUpThold=_SfcsBWPortPoolTrapMgmtBuffUpThold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,42),_SfcsBWPortPoolTrapMgmtBuffUpThold_Type())
sfcsBWPortPoolTrapMgmtBuffUpThold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBWPortPoolTrapMgmtBuffUpThold.setStatus(_A)
_SfcsBWPortPoolTrapMgmtBuffLoThold_Type=Integer32
_SfcsBWPortPoolTrapMgmtBuffLoThold_Object=MibTableColumn
sfcsBWPortPoolTrapMgmtBuffLoThold=_SfcsBWPortPoolTrapMgmtBuffLoThold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,43),_SfcsBWPortPoolTrapMgmtBuffLoThold_Type())
sfcsBWPortPoolTrapMgmtBuffLoThold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBWPortPoolTrapMgmtBuffLoThold.setStatus(_A)
_SfcsBWPortPoolTrapMgmtConnRejThold_Type=Integer32
_SfcsBWPortPoolTrapMgmtConnRejThold_Object=MibTableColumn
sfcsBWPortPoolTrapMgmtConnRejThold=_SfcsBWPortPoolTrapMgmtConnRejThold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,3,3,1,44),_SfcsBWPortPoolTrapMgmtConnRejThold_Type())
sfcsBWPortPoolTrapMgmtConnRejThold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBWPortPoolTrapMgmtConnRejThold.setStatus(_A)
_SfcsBuffPools_ObjectIdentity=ObjectIdentity
sfcsBuffPools=_SfcsBuffPools_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4))
_SfcsBuffPrioTable_Object=MibTable
sfcsBuffPrioTable=_SfcsBuffPrioTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1))
if mibBuilder.loadTexts:sfcsBuffPrioTable.setStatus(_A)
_SfcsBuffPrioEntry_Object=MibTableRow
sfcsBuffPrioEntry=_SfcsBuffPrioEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1))
sfcsBuffPrioEntry.setIndexNames((0,_E,_AM),(0,_E,_AN))
if mibBuilder.loadTexts:sfcsBuffPrioEntry.setStatus(_A)
_SfcsBuffPrioPortIndex_Type=Integer32
_SfcsBuffPrioPortIndex_Object=MibTableColumn
sfcsBuffPrioPortIndex=_SfcsBuffPrioPortIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,1),_SfcsBuffPrioPortIndex_Type())
sfcsBuffPrioPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBuffPrioPortIndex.setStatus(_A)
_SfcsBuffPrioPriority_Type=Integer32
_SfcsBuffPrioPriority_Object=MibTableColumn
sfcsBuffPrioPriority=_SfcsBuffPrioPriority_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,2),_SfcsBuffPrioPriority_Type())
sfcsBuffPrioPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBuffPrioPriority.setStatus(_A)
_SfcsBuffPrioAssignCtl_Type=Integer32
_SfcsBuffPrioAssignCtl_Object=MibTableColumn
sfcsBuffPrioAssignCtl=_SfcsBuffPrioAssignCtl_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,3),_SfcsBuffPrioAssignCtl_Type())
sfcsBuffPrioAssignCtl.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBuffPrioAssignCtl.setStatus(_A)
_SfcsBuffPrioMinCtl_Type=Integer32
_SfcsBuffPrioMinCtl_Object=MibTableColumn
sfcsBuffPrioMinCtl=_SfcsBuffPrioMinCtl_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,4),_SfcsBuffPrioMinCtl_Type())
sfcsBuffPrioMinCtl.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBuffPrioMinCtl.setStatus(_A)
_SfcsBuffPrioAssigned_Type=Integer32
_SfcsBuffPrioAssigned_Object=MibTableColumn
sfcsBuffPrioAssigned=_SfcsBuffPrioAssigned_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,5),_SfcsBuffPrioAssigned_Type())
sfcsBuffPrioAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBuffPrioAssigned.setStatus(_A)
_SfcsBuffPrioAllocated_Type=Integer32
_SfcsBuffPrioAllocated_Object=MibTableColumn
sfcsBuffPrioAllocated=_SfcsBuffPrioAllocated_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,6),_SfcsBuffPrioAllocated_Type())
sfcsBuffPrioAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBuffPrioAllocated.setStatus(_A)
_SfcsBuffPrioAvailable_Type=Integer32
_SfcsBuffPrioAvailable_Object=MibTableColumn
sfcsBuffPrioAvailable=_SfcsBuffPrioAvailable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,7),_SfcsBuffPrioAvailable_Type())
sfcsBuffPrioAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBuffPrioAvailable.setStatus(_A)
_SfcsBuffPrioPeakAlloc_Type=Integer32
_SfcsBuffPrioPeakAlloc_Object=MibTableColumn
sfcsBuffPrioPeakAlloc=_SfcsBuffPrioPeakAlloc_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,8),_SfcsBuffPrioPeakAlloc_Type())
sfcsBuffPrioPeakAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsBuffPrioPeakAlloc.setStatus(_A)
_SfcsBuffPrioConnRejs_Type=Integer32
_SfcsBuffPrioConnRejs_Object=MibTableColumn
sfcsBuffPrioConnRejs=_SfcsBuffPrioConnRejs_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,9),_SfcsBuffPrioConnRejs_Type())
sfcsBuffPrioConnRejs.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBuffPrioConnRejs.setStatus(_A)
_SfcsBuffPrioUpTholdTrap_Type=Integer32
_SfcsBuffPrioUpTholdTrap_Object=MibTableColumn
sfcsBuffPrioUpTholdTrap=_SfcsBuffPrioUpTholdTrap_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,10),_SfcsBuffPrioUpTholdTrap_Type())
sfcsBuffPrioUpTholdTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBuffPrioUpTholdTrap.setStatus(_A)
_SfcsBuffPrioLoTholdTrap_Type=Integer32
_SfcsBuffPrioLoTholdTrap_Object=MibTableColumn
sfcsBuffPrioLoTholdTrap=_SfcsBuffPrioLoTholdTrap_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,11),_SfcsBuffPrioLoTholdTrap_Type())
sfcsBuffPrioLoTholdTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBuffPrioLoTholdTrap.setStatus(_A)
_SfcsBuffPrioConnRejThold_Type=Integer32
_SfcsBuffPrioConnRejThold_Object=MibTableColumn
sfcsBuffPrioConnRejThold=_SfcsBuffPrioConnRejThold_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,12,4,1,1,12),_SfcsBuffPrioConnRejThold_Type())
sfcsBuffPrioConnRejThold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsBuffPrioConnRejThold.setStatus(_A)
_SfcsProxy_ObjectIdentity=ObjectIdentity
sfcsProxy=_SfcsProxy_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,13))
_SfcsProxyConfig_ObjectIdentity=ObjectIdentity
sfcsProxyConfig=_SfcsProxyConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1))
_SfcsProxyConfigTable_Object=MibTable
sfcsProxyConfigTable=_SfcsProxyConfigTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1))
if mibBuilder.loadTexts:sfcsProxyConfigTable.setStatus(_A)
_SfcsProxyConfigEntry_Object=MibTableRow
sfcsProxyConfigEntry=_SfcsProxyConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1))
sfcsProxyConfigEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:sfcsProxyConfigEntry.setStatus(_A)
_SfcsProxyConfigANIMIndex_Type=Integer32
_SfcsProxyConfigANIMIndex_Object=MibTableColumn
sfcsProxyConfigANIMIndex=_SfcsProxyConfigANIMIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,1),_SfcsProxyConfigANIMIndex_Type())
sfcsProxyConfigANIMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigANIMIndex.setStatus(_A)
_SfcsProxyConfigNUMPORTS_Type=Integer32
_SfcsProxyConfigNUMPORTS_Object=MibTableColumn
sfcsProxyConfigNUMPORTS=_SfcsProxyConfigNUMPORTS_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,2),_SfcsProxyConfigNUMPORTS_Type())
sfcsProxyConfigNUMPORTS.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigNUMPORTS.setStatus(_A)
_SfcsProxyConfigTxMemSize_Type=Integer32
_SfcsProxyConfigTxMemSize_Object=MibTableColumn
sfcsProxyConfigTxMemSize=_SfcsProxyConfigTxMemSize_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,3),_SfcsProxyConfigTxMemSize_Type())
sfcsProxyConfigTxMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigTxMemSize.setStatus(_A)
_SfcsProxyConfigRxMaxPduSize_Type=Integer32
_SfcsProxyConfigRxMaxPduSize_Object=MibTableColumn
sfcsProxyConfigRxMaxPduSize=_SfcsProxyConfigRxMaxPduSize_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,4),_SfcsProxyConfigRxMaxPduSize_Type())
sfcsProxyConfigRxMaxPduSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigRxMaxPduSize.setStatus(_A)
_SfcsProxyConfigBandWidth_Type=Integer32
_SfcsProxyConfigBandWidth_Object=MibTableColumn
sfcsProxyConfigBandWidth=_SfcsProxyConfigBandWidth_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,5),_SfcsProxyConfigBandWidth_Type())
sfcsProxyConfigBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigBandWidth.setStatus(_A)
class _SfcsProxyConfigTransmitDone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_SfcsProxyConfigTransmitDone_Type.__name__=_D
_SfcsProxyConfigTransmitDone_Object=MibTableColumn
sfcsProxyConfigTransmitDone=_SfcsProxyConfigTransmitDone_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,6),_SfcsProxyConfigTransmitDone_Type())
sfcsProxyConfigTransmitDone.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigTransmitDone.setStatus(_A)
class _SfcsProxyConfigReceiveFifoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('not-full',2)))
_SfcsProxyConfigReceiveFifoState_Type.__name__=_D
_SfcsProxyConfigReceiveFifoState_Object=MibTableColumn
sfcsProxyConfigReceiveFifoState=_SfcsProxyConfigReceiveFifoState_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,7),_SfcsProxyConfigReceiveFifoState_Type())
sfcsProxyConfigReceiveFifoState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigReceiveFifoState.setStatus(_A)
class _SfcsProxyConfigPortTransmitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stop',1),('start-stay',2),('reread',3)))
_SfcsProxyConfigPortTransmitMode_Type.__name__=_D
_SfcsProxyConfigPortTransmitMode_Object=MibTableColumn
sfcsProxyConfigPortTransmitMode=_SfcsProxyConfigPortTransmitMode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,8),_SfcsProxyConfigPortTransmitMode_Type())
sfcsProxyConfigPortTransmitMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyConfigPortTransmitMode.setStatus(_A)
_SfcsProxyConfigReceiveFifoReset_Type=Integer32
_SfcsProxyConfigReceiveFifoReset_Object=MibTableColumn
sfcsProxyConfigReceiveFifoReset=_SfcsProxyConfigReceiveFifoReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,9),_SfcsProxyConfigReceiveFifoReset_Type())
sfcsProxyConfigReceiveFifoReset.setMaxAccess(_K)
if mibBuilder.loadTexts:sfcsProxyConfigReceiveFifoReset.setStatus(_A)
_SfcsProxyConfigTxFifoReset_Type=Integer32
_SfcsProxyConfigTxFifoReset_Object=MibTableColumn
sfcsProxyConfigTxFifoReset=_SfcsProxyConfigTxFifoReset_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,10),_SfcsProxyConfigTxFifoReset_Type())
sfcsProxyConfigTxFifoReset.setMaxAccess(_K)
if mibBuilder.loadTexts:sfcsProxyConfigTxFifoReset.setStatus(_A)
class _SfcsProxyConfigReceiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receiving',1),('not-receiving',2)))
_SfcsProxyConfigReceiveMode_Type.__name__=_D
_SfcsProxyConfigReceiveMode_Object=MibTableColumn
sfcsProxyConfigReceiveMode=_SfcsProxyConfigReceiveMode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,11),_SfcsProxyConfigReceiveMode_Type())
sfcsProxyConfigReceiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyConfigReceiveMode.setStatus(_A)
class _SfcsProxyConfigCaptureMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),('header',2)))
_SfcsProxyConfigCaptureMode_Type.__name__=_D
_SfcsProxyConfigCaptureMode_Object=MibTableColumn
sfcsProxyConfigCaptureMode=_SfcsProxyConfigCaptureMode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,12),_SfcsProxyConfigCaptureMode_Type())
sfcsProxyConfigCaptureMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyConfigCaptureMode.setStatus(_A)
_SfcsProxyConfigInitPort_Type=Integer32
_SfcsProxyConfigInitPort_Object=MibTableColumn
sfcsProxyConfigInitPort=_SfcsProxyConfigInitPort_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,13),_SfcsProxyConfigInitPort_Type())
sfcsProxyConfigInitPort.setMaxAccess(_K)
if mibBuilder.loadTexts:sfcsProxyConfigInitPort.setStatus(_A)
_SfcsProxyConfigLoad_Type=Integer32
_SfcsProxyConfigLoad_Object=MibTableColumn
sfcsProxyConfigLoad=_SfcsProxyConfigLoad_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,14),_SfcsProxyConfigLoad_Type())
sfcsProxyConfigLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyConfigLoad.setStatus(_A)
_SfcsProxyConfigGumbo_Type=OctetString
_SfcsProxyConfigGumbo_Object=MibTableColumn
sfcsProxyConfigGumbo=_SfcsProxyConfigGumbo_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,1,1,1,15),_SfcsProxyConfigGumbo_Type())
sfcsProxyConfigGumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyConfigGumbo.setStatus(_A)
_SfcsProxyTrans_ObjectIdentity=ObjectIdentity
sfcsProxyTrans=_SfcsProxyTrans_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2))
_SfcsProxyTransTable_Object=MibTable
sfcsProxyTransTable=_SfcsProxyTransTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1))
if mibBuilder.loadTexts:sfcsProxyTransTable.setStatus(_A)
_SfcsProxyTransEntry_Object=MibTableRow
sfcsProxyTransEntry=_SfcsProxyTransEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1))
sfcsProxyTransEntry.setIndexNames((0,_E,_AP))
if mibBuilder.loadTexts:sfcsProxyTransEntry.setStatus(_A)
_SfcsProxyTransANIMIndex_Type=Integer32
_SfcsProxyTransANIMIndex_Object=MibTableColumn
sfcsProxyTransANIMIndex=_SfcsProxyTransANIMIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,1),_SfcsProxyTransANIMIndex_Type())
sfcsProxyTransANIMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyTransANIMIndex.setStatus(_A)
_SfcsProxyTransEncodeNewPdu_Type=Integer32
_SfcsProxyTransEncodeNewPdu_Object=MibTableColumn
sfcsProxyTransEncodeNewPdu=_SfcsProxyTransEncodeNewPdu_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,2),_SfcsProxyTransEncodeNewPdu_Type())
sfcsProxyTransEncodeNewPdu.setMaxAccess(_K)
if mibBuilder.loadTexts:sfcsProxyTransEncodeNewPdu.setStatus(_A)
_SfcsProxyTransVPI_Type=Integer32
_SfcsProxyTransVPI_Object=MibTableColumn
sfcsProxyTransVPI=_SfcsProxyTransVPI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,3),_SfcsProxyTransVPI_Type())
sfcsProxyTransVPI.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransVPI.setStatus(_A)
_SfcsProxyTransVCI_Type=Integer32
_SfcsProxyTransVCI_Object=MibTableColumn
sfcsProxyTransVCI=_SfcsProxyTransVCI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,4),_SfcsProxyTransVCI_Type())
sfcsProxyTransVCI.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransVCI.setStatus(_A)
class _SfcsProxyTransPTI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SfcsProxyTransPTI_Type.__name__=_D
_SfcsProxyTransPTI_Object=MibTableColumn
sfcsProxyTransPTI=_SfcsProxyTransPTI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,5),_SfcsProxyTransPTI_Type())
sfcsProxyTransPTI.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransPTI.setStatus(_A)
_SfcsProxyTransCLP_Type=Integer32
_SfcsProxyTransCLP_Object=MibTableColumn
sfcsProxyTransCLP=_SfcsProxyTransCLP_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,6),_SfcsProxyTransCLP_Type())
sfcsProxyTransCLP.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransCLP.setStatus(_A)
class _SfcsProxyTransPayloadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user-input',1),('sequential',2),('uniform',3)))
_SfcsProxyTransPayloadType_Type.__name__=_D
_SfcsProxyTransPayloadType_Object=MibTableColumn
sfcsProxyTransPayloadType=_SfcsProxyTransPayloadType_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,7),_SfcsProxyTransPayloadType_Type())
sfcsProxyTransPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransPayloadType.setStatus(_A)
_SfcsProxyTransPayloadLength_Type=Integer32
_SfcsProxyTransPayloadLength_Object=MibTableColumn
sfcsProxyTransPayloadLength=_SfcsProxyTransPayloadLength_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,8),_SfcsProxyTransPayloadLength_Type())
sfcsProxyTransPayloadLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransPayloadLength.setStatus(_A)
_SfcsProxyTransPayloadData_Type=OctetString
_SfcsProxyTransPayloadData_Object=MibTableColumn
sfcsProxyTransPayloadData=_SfcsProxyTransPayloadData_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,9),_SfcsProxyTransPayloadData_Type())
sfcsProxyTransPayloadData.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransPayloadData.setStatus(_A)
_SfcsProxyTransCount_Type=Integer32
_SfcsProxyTransCount_Object=MibTableColumn
sfcsProxyTransCount=_SfcsProxyTransCount_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,10),_SfcsProxyTransCount_Type())
sfcsProxyTransCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransCount.setStatus(_A)
class _SfcsProxyTransPayloadAdaptionLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raw',1),('aal5',2)))
_SfcsProxyTransPayloadAdaptionLayer_Type.__name__=_D
_SfcsProxyTransPayloadAdaptionLayer_Object=MibTableColumn
sfcsProxyTransPayloadAdaptionLayer=_SfcsProxyTransPayloadAdaptionLayer_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,11),_SfcsProxyTransPayloadAdaptionLayer_Type())
sfcsProxyTransPayloadAdaptionLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransPayloadAdaptionLayer.setStatus(_A)
_SfcsProxyTransMpxMethod_Type=Integer32
_SfcsProxyTransMpxMethod_Object=MibTableColumn
sfcsProxyTransMpxMethod=_SfcsProxyTransMpxMethod_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,12),_SfcsProxyTransMpxMethod_Type())
sfcsProxyTransMpxMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransMpxMethod.setStatus(_A)
class _SfcsProxyTransControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('send-once',1),('repeat',2)))
_SfcsProxyTransControl_Type.__name__=_D
_SfcsProxyTransControl_Object=MibTableColumn
sfcsProxyTransControl=_SfcsProxyTransControl_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,13),_SfcsProxyTransControl_Type())
sfcsProxyTransControl.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyTransControl.setStatus(_A)
_SfcsProxyTransGumbo_Type=OctetString
_SfcsProxyTransGumbo_Object=MibTableColumn
sfcsProxyTransGumbo=_SfcsProxyTransGumbo_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,2,1,1,14),_SfcsProxyTransGumbo_Type())
sfcsProxyTransGumbo.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyTransGumbo.setStatus(_A)
_SfcsProxyRead_ObjectIdentity=ObjectIdentity
sfcsProxyRead=_SfcsProxyRead_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3))
_SfcsProxyReadTable_Object=MibTable
sfcsProxyReadTable=_SfcsProxyReadTable_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1))
if mibBuilder.loadTexts:sfcsProxyReadTable.setStatus(_A)
_SfcsProxyReadEntry_Object=MibTableRow
sfcsProxyReadEntry=_SfcsProxyReadEntry_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1))
sfcsProxyReadEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:sfcsProxyReadEntry.setStatus(_A)
_SfcsProxyReadANIMIndex_Type=Integer32
_SfcsProxyReadANIMIndex_Object=MibTableColumn
sfcsProxyReadANIMIndex=_SfcsProxyReadANIMIndex_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,1),_SfcsProxyReadANIMIndex_Type())
sfcsProxyReadANIMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadANIMIndex.setStatus(_A)
class _SfcsProxyReadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reassemble-PDU',1),('cell-by-cell',2),('all-data',3)))
_SfcsProxyReadMode_Type.__name__=_D
_SfcsProxyReadMode_Object=MibTableColumn
sfcsProxyReadMode=_SfcsProxyReadMode_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,2),_SfcsProxyReadMode_Type())
sfcsProxyReadMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sfcsProxyReadMode.setStatus(_A)
class _SfcsProxyReadNewPdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('get-next-pdu',1),('reread-from-beginning',2)))
_SfcsProxyReadNewPdu_Type.__name__=_D
_SfcsProxyReadNewPdu_Object=MibTableColumn
sfcsProxyReadNewPdu=_SfcsProxyReadNewPdu_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,3),_SfcsProxyReadNewPdu_Type())
sfcsProxyReadNewPdu.setMaxAccess(_K)
if mibBuilder.loadTexts:sfcsProxyReadNewPdu.setStatus(_A)
_SfcsProxyReadGumbo_Type=OctetString
_SfcsProxyReadGumbo_Object=MibTableColumn
sfcsProxyReadGumbo=_SfcsProxyReadGumbo_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,4),_SfcsProxyReadGumbo_Type())
sfcsProxyReadGumbo.setMaxAccess(_K)
if mibBuilder.loadTexts:sfcsProxyReadGumbo.setStatus(_A)
_SfcsProxyReadVPI_Type=Integer32
_SfcsProxyReadVPI_Object=MibTableColumn
sfcsProxyReadVPI=_SfcsProxyReadVPI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,5),_SfcsProxyReadVPI_Type())
sfcsProxyReadVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadVPI.setStatus(_A)
_SfcsProxyReadVCI_Type=Integer32
_SfcsProxyReadVCI_Object=MibTableColumn
sfcsProxyReadVCI=_SfcsProxyReadVCI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,6),_SfcsProxyReadVCI_Type())
sfcsProxyReadVCI.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadVCI.setStatus(_A)
class _SfcsProxyReadPTI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SfcsProxyReadPTI_Type.__name__=_D
_SfcsProxyReadPTI_Object=MibTableColumn
sfcsProxyReadPTI=_SfcsProxyReadPTI_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,7),_SfcsProxyReadPTI_Type())
sfcsProxyReadPTI.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadPTI.setStatus(_A)
_SfcsProxyReadCLP_Type=Integer32
_SfcsProxyReadCLP_Object=MibTableColumn
sfcsProxyReadCLP=_SfcsProxyReadCLP_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,8),_SfcsProxyReadCLP_Type())
sfcsProxyReadCLP.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadCLP.setStatus(_A)
_SfcsProxyReadDataLength_Type=Integer32
_SfcsProxyReadDataLength_Object=MibTableColumn
sfcsProxyReadDataLength=_SfcsProxyReadDataLength_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,9),_SfcsProxyReadDataLength_Type())
sfcsProxyReadDataLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadDataLength.setStatus(_A)
_SfcsProxyReadData_Type=OctetString
_SfcsProxyReadData_Object=MibTableColumn
sfcsProxyReadData=_SfcsProxyReadData_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,10),_SfcsProxyReadData_Type())
sfcsProxyReadData.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadData.setStatus(_A)
class _SfcsProxyReadPal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raw',1),('aal5',2)))
_SfcsProxyReadPal_Type.__name__=_D
_SfcsProxyReadPal_Object=MibTableColumn
sfcsProxyReadPal=_SfcsProxyReadPal_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,11),_SfcsProxyReadPal_Type())
sfcsProxyReadPal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadPal.setStatus(_A)
_SfcsProxyReadInbyteslosts_Type=Integer32
_SfcsProxyReadInbyteslosts_Object=MibTableColumn
sfcsProxyReadInbyteslosts=_SfcsProxyReadInbyteslosts_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,12),_SfcsProxyReadInbyteslosts_Type())
sfcsProxyReadInbyteslosts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInbyteslosts.setStatus(_A)
_SfcsProxyReadInCells_Type=Integer32
_SfcsProxyReadInCells_Object=MibTableColumn
sfcsProxyReadInCells=_SfcsProxyReadInCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,13),_SfcsProxyReadInCells_Type())
sfcsProxyReadInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInCells.setStatus(_A)
_SfcsProxyReadInError_Type=Integer32
_SfcsProxyReadInError_Object=MibTableColumn
sfcsProxyReadInError=_SfcsProxyReadInError_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,14),_SfcsProxyReadInError_Type())
sfcsProxyReadInError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInError.setStatus(_A)
_SfcsProxyReadInCellReadError_Type=Integer32
_SfcsProxyReadInCellReadError_Object=MibTableColumn
sfcsProxyReadInCellReadError=_SfcsProxyReadInCellReadError_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,15),_SfcsProxyReadInCellReadError_Type())
sfcsProxyReadInCellReadError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInCellReadError.setStatus(_A)
_SfcsProxyReadInHecError_Type=Integer32
_SfcsProxyReadInHecError_Object=MibTableColumn
sfcsProxyReadInHecError=_SfcsProxyReadInHecError_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,16),_SfcsProxyReadInHecError_Type())
sfcsProxyReadInHecError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInHecError.setStatus(_A)
_SfcsProxyReadInTooBigError_Type=Integer32
_SfcsProxyReadInTooBigError_Object=MibTableColumn
sfcsProxyReadInTooBigError=_SfcsProxyReadInTooBigError_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,17),_SfcsProxyReadInTooBigError_Type())
sfcsProxyReadInTooBigError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInTooBigError.setStatus(_A)
_SfcsProxyReadInCRCError_Type=Integer32
_SfcsProxyReadInCRCError_Object=MibTableColumn
sfcsProxyReadInCRCError=_SfcsProxyReadInCRCError_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,18),_SfcsProxyReadInCRCError_Type())
sfcsProxyReadInCRCError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInCRCError.setStatus(_A)
_SfcsProxyReadInLengthMismatchError_Type=Integer32
_SfcsProxyReadInLengthMismatchError_Object=MibTableColumn
sfcsProxyReadInLengthMismatchError=_SfcsProxyReadInLengthMismatchError_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,19),_SfcsProxyReadInLengthMismatchError_Type())
sfcsProxyReadInLengthMismatchError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInLengthMismatchError.setStatus(_A)
_SfcsProxyReadInTotalCells_Type=Integer32
_SfcsProxyReadInTotalCells_Object=MibTableColumn
sfcsProxyReadInTotalCells=_SfcsProxyReadInTotalCells_Object((1,3,6,1,4,1,52,4,1,2,11,1,1,13,3,1,1,20),_SfcsProxyReadInTotalCells_Type())
sfcsProxyReadInTotalCells.setMaxAccess(_B)
if mibBuilder.loadTexts:sfcsProxyReadInTotalCells.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cabletron':cabletron,'mibs':mibs,'ctron':ctron,'ctDataLink':ctDataLink,'ctSwitch':ctSwitch,'ctsfSwitch':ctsfSwitch,'ctSFCS':ctSFCS,'sfcsSystem':sfcsSystem,'sfcsSysConfig':sfcsSysConfig,'sfcsSysConfigTable':sfcsSysConfigTable,'sfcsSysConfigEnt':sfcsSysConfigEnt,'sfcsSysConfigAdminStatus':sfcsSysConfigAdminStatus,'sfcsSysConfigOperStatus':sfcsSysConfigOperStatus,'sfcsSysConfigOperTime':sfcsSysConfigOperTime,'sfcsSysConfigLastChange':sfcsSysConfigLastChange,'sfcsSysConfigSwitchCapacity':sfcsSysConfigSwitchCapacity,'sfcsSysConfigMaxCnxEntries':sfcsSysConfigMaxCnxEntries,'sfcsSysConfigMaxStatEntries':sfcsSysConfigMaxStatEntries,'sfcsSysConfigMaxUpcEntries':sfcsSysConfigMaxUpcEntries,'sfcsSysConfigNumberANIMS':sfcsSysConfigNumberANIMS,'sfcsSysConfigInterfaceCapability':sfcsSysConfigInterfaceCapability,'sfcsSysConfigTypeofSwitch':sfcsSysConfigTypeofSwitch,'sfcsSysConfigPolicingSupport':sfcsSysConfigPolicingSupport,'sfcsSysConfigPnniNsapPrefix':sfcsSysConfigPnniNsapPrefix,'sfcsSysConfigPnniNodeLevel':sfcsSysConfigPnniNodeLevel,'sfcsSysConfigPnniAddessingMode':sfcsSysConfigPnniAddessingMode,'sfcsSysConfigPnniAddessingAdmnStatus':sfcsSysConfigPnniAddessingAdmnStatus,'sfcsSysConfigFMVer':sfcsSysConfigFMVer,'sfcsSysConfigCTMSlotMask':sfcsSysConfigCTMSlotMask,'sfcsSysConfigMaxfreecva':sfcsSysConfigMaxfreecva,'sfcsSysConfigUBR':sfcsSysConfigUBR,'sfcsSysStatus':sfcsSysStatus,'sfcsSysStatusTable':sfcsSysStatusTable,'sfcsSysStatusEnt':sfcsSysStatusEnt,'sfcsSysStatusTdmCellCount':sfcsSysStatusTdmCellCount,'sfcsSysStatusTdmUtilization':sfcsSysStatusTdmUtilization,'sfcsSysStatusCurrCnxEntries':sfcsSysStatusCurrCnxEntries,'sfcsSysStatusCurrUPCEntries':sfcsSysStatusCurrUPCEntries,'sfcsSysStatusCurrStatsEntries':sfcsSysStatusCurrStatsEntries,'sfcsSysStatusAllocatedBw':sfcsSysStatusAllocatedBw,'sfcsSysSystemCfg':sfcsSysSystemCfg,'sfcsSysSystemCfgTable':sfcsSysSystemCfgTable,'sfcsSysSystemCfgEnt':sfcsSysSystemCfgEnt,'sfcsSysConfigAdminReset':sfcsSysConfigAdminReset,'sfcsSysConfigATOMPersistance':sfcsSysConfigATOMPersistance,'sfcsSysConfigVcSize':sfcsSysConfigVcSize,'sfcsSysConfigPowerUpDiags':sfcsSysConfigPowerUpDiags,'sfcsSysBPCfg':sfcsSysBPCfg,'sfcsSysBPTable':sfcsSysBPTable,'sfcsSysBPEnt':sfcsSysBPEnt,'sfcsSysBPClkSelect':sfcsSysBPClkSelect,'sfcsEngine':sfcsEngine,'sfcsConfig':sfcsConfig,'sfcsConfigTable':sfcsConfigTable,'sfcsConfigEntry':sfcsConfigEntry,_f:sfcsConfigSlotIndex,'sfcsConfigAdminStatus':sfcsConfigAdminStatus,'sfcsConfigAdminReset':sfcsConfigAdminReset,'sfcsConfigOperStatus':sfcsConfigOperStatus,'sfcsConfigOperTime':sfcsConfigOperTime,'sfcsConfigLastChange':sfcsConfigLastChange,'sfcsConfigVersion':sfcsConfigVersion,'sfcsConfigMibRev':sfcsConfigMibRev,'sfcsConfigSwitchHostPort':sfcsConfigSwitchHostPort,'sfcsConfigHostCtrlATMAddr':sfcsConfigHostCtrlATMAddr,'sfcsConfigSwitchCapacity':sfcsConfigSwitchCapacity,'sfcsConfigMaxCnxEntries':sfcsConfigMaxCnxEntries,'sfcsConfigMaxStatEntries':sfcsConfigMaxStatEntries,'sfcsConfigMaxUpcEntries':sfcsConfigMaxUpcEntries,'sfcsConfigNumberANIMS':sfcsConfigNumberANIMS,'sfcsConfigBwCapability':sfcsConfigBwCapability,'sfcsConfigMasterClock1Source':sfcsConfigMasterClock1Source,'sfcsConfigMasterClock2Source':sfcsConfigMasterClock2Source,'sfcsConfigMasterClock1Standby':sfcsConfigMasterClock1Standby,'sfcsConfigMasterClock2Standby':sfcsConfigMasterClock2Standby,'sfcsStatus':sfcsStatus,'sfcsStatusTable':sfcsStatusTable,'sfcsStatusEntry':sfcsStatusEntry,_g:sfcsStatusSlotIndex,'sfcsStatusTdmCellCount':sfcsStatusTdmCellCount,'sfcsStatusTdmUtilization':sfcsStatusTdmUtilization,'sfcsStatusCurrCnxEntries':sfcsStatusCurrCnxEntries,'sfcsStatusCurrUPCEntries':sfcsStatusCurrUPCEntries,'sfcsStatusCurrStatsEntries':sfcsStatusCurrStatsEntries,'sfcsStatusCurrCtmAgent':sfcsStatusCurrCtmAgent,'sfcsUPCEngine':sfcsUPCEngine,'sfcsUPCTable':sfcsUPCTable,'sfcsUPCEntry':sfcsUPCEntry,_h:sfcsUPCSlotIndex,'sfcsUPCAdminStatus':sfcsUPCAdminStatus,'sfcsUPCOperStatus':sfcsUPCOperStatus,'sfcsUPCReset':sfcsUPCReset,'sfcsUPCOperTime':sfcsUPCOperTime,'sfcsStatisticsEngine':sfcsStatisticsEngine,'sfcsStatsEngineTable':sfcsStatsEngineTable,'sfcsStatsEngineEntry':sfcsStatsEngineEntry,_i:sfcsStatsEngineSlotIndex,'sfcsStatsEngineAdminStatus':sfcsStatsEngineAdminStatus,'sfcsStatsEngineOperStatus':sfcsStatsEngineOperStatus,'sfcsStatsEngineReset':sfcsStatsEngineReset,'sfcsStatsEngineOperTime':sfcsStatsEngineOperTime,'sfcsPacketDiscardEngine':sfcsPacketDiscardEngine,'sfcsPacketDiscardEngineTable':sfcsPacketDiscardEngineTable,'sfcsPacketDiscardEngineEntry':sfcsPacketDiscardEngineEntry,_j:sfcsPacketDiscardEngineSlotIndex,'sfcsPacketDiscardEngineAdminStatus':sfcsPacketDiscardEngineAdminStatus,'sfcsPacketDiscardEngineOperStatus':sfcsPacketDiscardEngineOperStatus,'sfcsPacketDiscardEngineReset':sfcsPacketDiscardEngineReset,'sfcsPacketDiscardEngineEPDPercentage':sfcsPacketDiscardEngineEPDPercentage,'sfcsPacketDiscardEngineOperTime':sfcsPacketDiscardEngineOperTime,'sfcsANIM':sfcsANIM,'sfcsANIMConfig':sfcsANIMConfig,'sfcsANIMConfigTable':sfcsANIMConfigTable,'sfcsANIMConfigEntry':sfcsANIMConfigEntry,_k:sfcsANIMConfigANIMIndex,'sfcsANIMConfigAdminStatus':sfcsANIMConfigAdminStatus,'sfcsANIMConfigOperStatus':sfcsANIMConfigOperStatus,'sfcsANIMConfigANIMType':sfcsANIMConfigANIMType,'sfcsANIMConfigNumInterfaces':sfcsANIMConfigNumInterfaces,'sfcsANIMConfigLineRate':sfcsANIMConfigLineRate,'sfcsANIMConfigToMB':sfcsANIMConfigToMB,'sfcsANIMConfigMBClockSelect':sfcsANIMConfigMBClockSelect,'sfcsANIMStatistics':sfcsANIMStatistics,'sfcsANIMStatsTable':sfcsANIMStatsTable,'sfcsANIMStatsEntry':sfcsANIMStatsEntry,_m:sfcsANIMStatsANIMIndex,'sfcsANIMStatsRxCells':sfcsANIMStatsRxCells,'sfcsANIMStatsTxCells':sfcsANIMStatsTxCells,'sfcsANIMPic':sfcsANIMPic,'sfcsANIMPicTable':sfcsANIMPicTable,'sfcsANIMPicEntry':sfcsANIMPicEntry,'sfcsANIMPicSlot':sfcsANIMPicSlot,_n:sfcsANIMPicIndex,'sfcsANIMPicLocation':sfcsANIMPicLocation,'sfcsANIMPicStatus':sfcsANIMPicStatus,'sfcsANIMPicVersion':sfcsANIMPicVersion,'sfcsANIMPicModuleType':sfcsANIMPicModuleType,'sfcsANIMPicMfgPN':sfcsANIMPicMfgPN,'sfcsANIMPicMfgSN':sfcsANIMPicMfgSN,'sfcsANIMPicMfgPartNumb':sfcsANIMPicMfgPartNumb,'sfcsANIMPicMfgSerialNumb':sfcsANIMPicMfgSerialNumb,'sfcsANIMPicMfgReworkLocation':sfcsANIMPicMfgReworkLocation,'sfcsANIMPicMfgMfgLocation':sfcsANIMPicMfgMfgLocation,'sfcsANIMPicMfgDateCode':sfcsANIMPicMfgDateCode,'sfcsANIMPicMfgRevisionCode':sfcsANIMPicMfgRevisionCode,'sfcsANIMPicTLPN':sfcsANIMPicTLPN,'sfcsANIMPicTLSN':sfcsANIMPicTLSN,'sfcsANIMPicTLPartNumb':sfcsANIMPicTLPartNumb,'sfcsANIMPicTLSerialNumb':sfcsANIMPicTLSerialNumb,'sfcsANIMPicTLReworkLocation':sfcsANIMPicTLReworkLocation,'sfcsANIMPicTLMfgLocation':sfcsANIMPicTLMfgLocation,'sfcsANIMPicTLDateCode':sfcsANIMPicTLDateCode,'sfcsANIMPicTLRevisionCode':sfcsANIMPicTLRevisionCode,'sfcsANIMPicTLPcbRevision':sfcsANIMPicTLPcbRevision,'sfcsANIMPicMacAddr':sfcsANIMPicMacAddr,'sfcsANIMPicNumbRsvdAddrs':sfcsANIMPicNumbRsvdAddrs,'sfcsANIMPicBoardLevelRevision':sfcsANIMPicBoardLevelRevision,'sfcsANIMPicModuleTypeString':sfcsANIMPicModuleTypeString,'sfcsANIMPicDcDcConverterType':sfcsANIMPicDcDcConverterType,'sfcsANIMPicDcDcConverterInputPower':sfcsANIMPicDcDcConverterInputPower,'sfcsANIMPicSmb1PromVersion':sfcsANIMPicSmb1PromVersion,'sfcsInterface':sfcsInterface,'sfcsInterfaceConfig':sfcsInterfaceConfig,'sfcsInterfaceConfigTable':sfcsInterfaceConfigTable,'sfcsInterfaceConfigEntry':sfcsInterfaceConfigEntry,_o:sfcsInterfaceConfigInterfaceIndex,'sfcsInterfaceConfigType':sfcsInterfaceConfigType,'sfcsInterfacePeakBufferUseage':sfcsInterfacePeakBufferUseage,'sfcsInterfaceConfigNumberOfQueues':sfcsInterfaceConfigNumberOfQueues,'sfcsInterfaceConfigSigStackID':sfcsInterfaceConfigSigStackID,'sfcsInterfaceConfigClockingSource':sfcsInterfaceConfigClockingSource,'sfcsInterfaceStatistics':sfcsInterfaceStatistics,'sfcsInterfaceStatsTable':sfcsInterfaceStatsTable,'sfcsInterfaceStatsEntry':sfcsInterfaceStatsEntry,_t:sfcsInterfaceStatsInterfaceIndex,'sfcsInterfaceStatsRxErrors':sfcsInterfaceStatsRxErrors,'sfcsInterfaceStatsVPILookupInvalidErrors':sfcsInterfaceStatsVPILookupInvalidErrors,'sfcsInterfaceStatsRxCnxLookupInvalidErrors':sfcsInterfaceStatsRxCnxLookupInvalidErrors,'sfcsInterfaceStatsRxCellCnt':sfcsInterfaceStatsRxCellCnt,'sfcsInterfaceStatsTxCellCnt':sfcsInterfaceStatsTxCellCnt,'sfcsInterfaceStatsOverflowDropCellCnt':sfcsInterfaceStatsOverflowDropCellCnt,'sfcsQueue':sfcsQueue,'sfcsQueueConfig':sfcsQueueConfig,'sfcsQueueConfigTable':sfcsQueueConfigTable,'sfcsQueueConfigEntry':sfcsQueueConfigEntry,_u:sfcsQueueConfigInterfaceIndex,_T:sfcsQueueConfigQueueIndex,'sfcsQueueConfigQueueSize':sfcsQueueConfigQueueSize,'sfcsQueueConfigQueueBandwidth':sfcsQueueConfigQueueBandwidth,'sfcsQueueConfigClpDropThreshold':sfcsQueueConfigClpDropThreshold,'sfcsQueueConfigCongestionThreshold':sfcsQueueConfigCongestionThreshold,'sfcsQueueConfigEFCILowThreshold':sfcsQueueConfigEFCILowThreshold,'sfcsQueueConfigRMThreshold':sfcsQueueConfigRMThreshold,'sfcsQueueConfigEPDThreshold':sfcsQueueConfigEPDThreshold,'sfcsQueueStatistics':sfcsQueueStatistics,'sfcsQueueStatsTable':sfcsQueueStatsTable,'sfcsQueueStatsEntry':sfcsQueueStatsEntry,_v:sfcsQueueStatsInterfaceIndex,_U:sfcsQueueStatsQueue,'sfcsQueueStatsTxClpCellsDiscarded':sfcsQueueStatsTxClpCellsDiscarded,'sfcsQueueStatsTxCellsDropped':sfcsQueueStatsTxCellsDropped,'sfcsQueueStatsQueuePeakLevel':sfcsQueueStatsQueuePeakLevel,'sfcsQueueStatsTxCellCnt':sfcsQueueStatsTxCellCnt,'sfcsConnection':sfcsConnection,'sfcsConnectionConfig':sfcsConnectionConfig,'sfcsCnxCfgTable':sfcsCnxCfgTable,'sfcsCnxCfgEntry':sfcsCnxCfgEntry,_w:sfcsCnxCfgCrossConnectIndex,_x:sfcsCnxCfgCrossConnectLowIfIndex,_y:sfcsCnxCfgCrossConnectLowVpi,_z:sfcsCnxCfgCrossConnectLowVci,_A0:sfcsCnxCfgCrossConnectHighIfIndex,_A1:sfcsCnxCfgCrossConnectHighVpi,_A2:sfcsCnxCfgCrossConnectHighVci,'sfcsCnxCfgType':sfcsCnxCfgType,'sfcsCnxCfgTmType':sfcsCnxCfgTmType,'sfcsCnxCfgUPCEnable':sfcsCnxCfgUPCEnable,'sfcsCnxCfgStatsEnable':sfcsCnxCfgStatsEnable,'sfcsCnxCfgStatsTableCounterSizes':sfcsCnxCfgStatsTableCounterSizes,'sfcsCnxCfgOwner':sfcsCnxCfgOwner,'sfcsConnectionStatistics':sfcsConnectionStatistics,'sfcsCnxStatsTable':sfcsCnxStatsTable,'sfcsCnxStatsEntry':sfcsCnxStatsEntry,_A3:sfcsCnxStatsCrossConnectIndex,_A4:sfcsCnxStatsCrossConnectLowIfIndex,_A5:sfcsCnxStatsCrossConnectLowVpi,_A6:sfcsCnxStatsCrossConnectLowVci,_A7:sfcsCnxStatsCrossConnectHighIfIndex,_A8:sfcsCnxStatsCrossConnectHighVpi,_A9:sfcsCnxStatsCrossConnectHighVci,'sfcsCnxStatsLoToHiHTxCells':sfcsCnxStatsLoToHiHTxCells,'sfcsCnxStatsLoToHiDroppedCells':sfcsCnxStatsLoToHiDroppedCells,'sfcsCnxStatsLoToHiTaggedCells':sfcsCnxStatsLoToHiTaggedCells,'sfcsCnxStatsHiToLoHTxCells':sfcsCnxStatsHiToLoHTxCells,'sfcsCnxStatsHiToLoDroppedCells':sfcsCnxStatsHiToLoDroppedCells,'sfcsCnxStatsHiToLoTaggedCells':sfcsCnxStatsHiToLoTaggedCells,'sfcsConnectionError':sfcsConnectionError,'sfcsCnxErrorTable':sfcsCnxErrorTable,'sfcsCnxErrorEntry':sfcsCnxErrorEntry,'sfcsCnxErrorCode':sfcsCnxErrorCode,'sfcsCnxErrorTimeStamp':sfcsCnxErrorTimeStamp,'sfcsCnxErrorRowStatus':sfcsCnxErrorRowStatus,'sfcsConnectionAPI':sfcsConnectionAPI,'sfcsCnxAPIEntry':sfcsCnxAPIEntry,'sfcsCTM':sfcsCTM,'sfcsCTMInterfaceConfig':sfcsCTMInterfaceConfig,'sfcsCTMInterfaceConfigTable':sfcsCTMInterfaceConfigTable,'sfcsCTMInterfaceConfigEntry':sfcsCTMInterfaceConfigEntry,_AA:sfcsCTMInterfaceConfigInterfaceIndex,'sfcsCTMInterfaceConfigType':sfcsCTMInterfaceConfigType,'sfcsCTMInterfacePeakBufferUseage':sfcsCTMInterfacePeakBufferUseage,'sfcsCTMInterfaceConfigNumberOfQueues':sfcsCTMInterfaceConfigNumberOfQueues,'sfcsCTMInterfaceConfigSigStackID':sfcsCTMInterfaceConfigSigStackID,'sfcsCTMInterfaceConfigClocking':sfcsCTMInterfaceConfigClocking,'sfcsCTMInterfaceConfigNextVPI':sfcsCTMInterfaceConfigNextVPI,'sfcsCTMInterfaceConfigNextVCI':sfcsCTMInterfaceConfigNextVCI,'sfcsCTMInterfaceStatistics':sfcsCTMInterfaceStatistics,'sfcsCTMInterfaceStatsTable':sfcsCTMInterfaceStatsTable,'sfcsCTMInterfaceStatsEntry':sfcsCTMInterfaceStatsEntry,_AB:sfcsCTMInterfaceStatsInterfaceIndex,'sfcsCTMInterfaceStatsRxErrors':sfcsCTMInterfaceStatsRxErrors,'sfcsCTMInterfaceStatsVPILookupInvalidErrors':sfcsCTMInterfaceStatsVPILookupInvalidErrors,'sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors':sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors,'sfcsCTMInterfaceStatsRxCellCnt':sfcsCTMInterfaceStatsRxCellCnt,'sfcsCTMInterfaceStatsTxCellCnt':sfcsCTMInterfaceStatsTxCellCnt,'sfcsCTMInterfaceStatsOverflowDropCellCnt':sfcsCTMInterfaceStatsOverflowDropCellCnt,'sfcsCTMQueueConfig':sfcsCTMQueueConfig,'sfcsCTMQueueConfigTable':sfcsCTMQueueConfigTable,'sfcsCTMQueueConfigEntry':sfcsCTMQueueConfigEntry,_AC:sfcsCTMQueueConfigInterfaceIndex,'sfcsCTMQueueConfigQueueIndex':sfcsCTMQueueConfigQueueIndex,'sfcsCTMQueueConfigQueueSize':sfcsCTMQueueConfigQueueSize,'sfcsCTMQueueConfigQueueBandwidth':sfcsCTMQueueConfigQueueBandwidth,'sfcsCTMQueueConfigClpDropThreshold':sfcsCTMQueueConfigClpDropThreshold,'sfcsCTMQueueConfigCongestionThreshold':sfcsCTMQueueConfigCongestionThreshold,'sfcsCTMQueueConfigEFCILowThreshold':sfcsCTMQueueConfigEFCILowThreshold,'sfcsCTMQueueConfigRMThreshold':sfcsCTMQueueConfigRMThreshold,'sfcsCTMQueueStatistics':sfcsCTMQueueStatistics,'sfcsCTMQueueStatsTable':sfcsCTMQueueStatsTable,'sfcsCTMQueueStatsEntry':sfcsCTMQueueStatsEntry,_AD:sfcsCTMQueueStatsInterfaceIndex,'sfcsCTMQueueStatsQueue':sfcsCTMQueueStatsQueue,'sfcsCTMQueueStatsTxClpCellsDiscarded':sfcsCTMQueueStatsTxClpCellsDiscarded,'sfcsCTMQueueStatsTxCellsDropped':sfcsCTMQueueStatsTxCellsDropped,'sfcsCTMQueueStatsQueuePeakLevel':sfcsCTMQueueStatsQueuePeakLevel,'sfcsCTMQueueStatsTxCellCnt':sfcsCTMQueueStatsTxCellCnt,'sfcsBWMgr':sfcsBWMgr,'sfcsBwNims':sfcsBwNims,'sfcsBwNimsTable':sfcsBwNimsTable,'sfcsBwNimsEntry':sfcsBwNimsEntry,_AE:sfcsBwNimsIndex,'sfcsBwNimsAdminStatus':sfcsBwNimsAdminStatus,'sfcsBWNimsBuffCount':sfcsBWNimsBuffCount,'sfcsBWNimsPortCount':sfcsBWNimsPortCount,'sfcsBWNimsPrioCount':sfcsBWNimsPrioCount,'sfcsBwPorts':sfcsBwPorts,'sfcsBwPortsTable':sfcsBwPortsTable,'sfcsBwPortsEntry':sfcsBwPortsEntry,_AF:sfcsBwPortsIndex,'sfcsBwPortsAdminStatus':sfcsBwPortsAdminStatus,'sfcsBwPortsPhysBwFwd':sfcsBwPortsPhysBwFwd,'sfcsBwPortsPhysBwRev':sfcsBwPortsPhysBwRev,'sfcsBwPortsZone':sfcsBwPortsZone,'sfcsBwPortsMetric':sfcsBwPortsMetric,'sfcsBwPortPools':sfcsBwPortPools,'sfcsBwPortPoolLimitsTable':sfcsBwPortPoolLimitsTable,'sfcsBwPortPoolLimitsEntry':sfcsBwPortPoolLimitsEntry,_AG:sfcsBwPortPoolLimitsIndex,_AH:sfcsBwPortPoolLimitsPoolIndex,'sfcsBwPortPoolLimitsMaxAllocBwFwd':sfcsBwPortPoolLimitsMaxAllocBwFwd,'sfcsBwPortPoolLimitsMaxAllocBwRev':sfcsBwPortPoolLimitsMaxAllocBwRev,'sfcsBwPortPoolLimitsBwAllocStrat':sfcsBwPortPoolLimitsBwAllocStrat,'sfcsBwPortPoolLimitsBwConstant':sfcsBwPortPoolLimitsBwConstant,'sfcsBwPortPoolLimitsCBRLimitFwd':sfcsBwPortPoolLimitsCBRLimitFwd,'sfcsBwPortPoolLimitsCBRLimitRev':sfcsBwPortPoolLimitsCBRLimitRev,'sfcsBwPortPoolLimitsABRLimitFwd':sfcsBwPortPoolLimitsABRLimitFwd,'sfcsBwPortPoolLimitsABRLimitRev':sfcsBwPortPoolLimitsABRLimitRev,'sfcsBwPortPoolLimitsVBRLimitFwd':sfcsBwPortPoolLimitsVBRLimitFwd,'sfcsBwPortPoolLimitsVBRLimitRev':sfcsBwPortPoolLimitsVBRLimitRev,'sfcsBwPortPoolLimitsUBRLimitFwd':sfcsBwPortPoolLimitsUBRLimitFwd,'sfcsBwPortPoolLimitsUBRLimitRev':sfcsBwPortPoolLimitsUBRLimitRev,'sfcsBwPortPoolLimitsUBRConnLimitFwd':sfcsBwPortPoolLimitsUBRConnLimitFwd,'sfcsBwPortPoolLimitsUBRConnLimitRev':sfcsBwPortPoolLimitsUBRConnLimitRev,'sfcsBwPortPoolStatTable':sfcsBwPortPoolStatTable,'sfcsBwPortPoolStatEntry':sfcsBwPortPoolStatEntry,_AI:sfcsBwPortPoolStatsIndex,_AJ:sfcsBwPortPoolStatsPoolIndex,'sfcsBwPortPoolStatConnCntFwd':sfcsBwPortPoolStatConnCntFwd,'sfcsBwPortPoolStatConnCntRev':sfcsBwPortPoolStatConnCntRev,'sfcsBwPortPoolStatAllocBwFwd':sfcsBwPortPoolStatAllocBwFwd,'sfcsBwPortPoolStatAllocBwRev':sfcsBwPortPoolStatAllocBwRev,'sfcsBwPortPoolStatAvailBwFwd':sfcsBwPortPoolStatAvailBwFwd,'sfcsBwPortPoolStatAvailBwRev':sfcsBwPortPoolStatAvailBwRev,'sfcsBwPortPoolStatPeakBwFwd':sfcsBwPortPoolStatPeakBwFwd,'sfcsBwPortPoolStatPeakBwRev':sfcsBwPortPoolStatPeakBwRev,'sfcsBwPortPoolStatRejConnFwd':sfcsBwPortPoolStatRejConnFwd,'sfcsBwPortPoolStatRejConnRev':sfcsBwPortPoolStatRejConnRev,'sfcsBwPortPoolStatPrevAdverMAXCRFwd':sfcsBwPortPoolStatPrevAdverMAXCRFwd,'sfcsBwPortPoolStatPrevAdverMAXCRRev':sfcsBwPortPoolStatPrevAdverMAXCRRev,'sfcsBwPortPoolStatPrevAdverAvailCRFwd':sfcsBwPortPoolStatPrevAdverAvailCRFwd,'sfcsBwPortPoolStatPrevAdverAvailCRRev':sfcsBwPortPoolStatPrevAdverAvailCRRev,'sfcsBwPortPoolStatCBRConnCntFwd':sfcsBwPortPoolStatCBRConnCntFwd,'sfcsBwPortPoolStatCBRConnCntRev':sfcsBwPortPoolStatCBRConnCntRev,'sfcsBwPortPoolStatCBRConnRejFwd':sfcsBwPortPoolStatCBRConnRejFwd,'sfcsBwPortPoolStatCBRConnRejRev':sfcsBwPortPoolStatCBRConnRejRev,'sfcsBwPortPoolStatCBRAllocBwFwd':sfcsBwPortPoolStatCBRAllocBwFwd,'sfcsBwPortPoolStatCBRAllocBwRev':sfcsBwPortPoolStatCBRAllocBwRev,'sfcsBwPortPoolStatCBRAggPCRFwd':sfcsBwPortPoolStatCBRAggPCRFwd,'sfcsBwPortPoolStatCBRAggPCRRev':sfcsBwPortPoolStatCBRAggPCRRev,'sfcsBwPortPoolStatCBRPrevAdverMAXCTD':sfcsBwPortPoolStatCBRPrevAdverMAXCTD,'sfcsBwPortPoolStatCBRPrevAdverCDV':sfcsBwPortPoolStatCBRPrevAdverCDV,'sfcsBwPortPoolStatABRConnCntFwd':sfcsBwPortPoolStatABRConnCntFwd,'sfcsBwPortPoolStatABRConnCntRev':sfcsBwPortPoolStatABRConnCntRev,'sfcsBwPortPoolStatABRConnRejFwd':sfcsBwPortPoolStatABRConnRejFwd,'sfcsBwPortPoolStatABRConnRejRev':sfcsBwPortPoolStatABRConnRejRev,'sfcsBwPortPoolStatABRAllocBwFwd':sfcsBwPortPoolStatABRAllocBwFwd,'sfcsBwPortPoolStatABRAllocBwRev':sfcsBwPortPoolStatABRAllocBwRev,'sfcsBwPortPoolStatABRAggPCRFwd':sfcsBwPortPoolStatABRAggPCRFwd,'sfcsBwPortPoolStatABRAggPCRRev':sfcsBwPortPoolStatABRAggPCRRev,'sfcsBwPortPoolStatABRPrevAdverMAXCTD':sfcsBwPortPoolStatABRPrevAdverMAXCTD,'sfcsBwPortPoolStatABRPrevAdverCDV':sfcsBwPortPoolStatABRPrevAdverCDV,'sfcsBwPortPoolStatVBRConnCntFwd':sfcsBwPortPoolStatVBRConnCntFwd,'sfcsBwPortPoolStatVBRConnCntRev':sfcsBwPortPoolStatVBRConnCntRev,'sfcsBwPortPoolStatVBRConnRejFwd':sfcsBwPortPoolStatVBRConnRejFwd,'sfcsBwPortPoolStatVBRConnRejRev':sfcsBwPortPoolStatVBRConnRejRev,'sfcsBwPortPoolStatVBRAllocBwFwd':sfcsBwPortPoolStatVBRAllocBwFwd,'sfcsBwPortPoolStatVBRAllocBwRev':sfcsBwPortPoolStatVBRAllocBwRev,'sfcsBwPortPoolStatVBRAggPCRFwd':sfcsBwPortPoolStatVBRAggPCRFwd,'sfcsBwPortPoolStatVBRAggPCRRev':sfcsBwPortPoolStatVBRAggPCRRev,'sfcsBwPortPoolStatVBRPrevAdverMAXCTD':sfcsBwPortPoolStatVBRPrevAdverMAXCTD,'sfcsBwPortPoolStatVBRPrevAdverCDV':sfcsBwPortPoolStatVBRPrevAdverCDV,'sfcsBwPortPoolStatUBRConnCntFwd':sfcsBwPortPoolStatUBRConnCntFwd,'sfcsBwPortPoolStatUBRConnCntRev':sfcsBwPortPoolStatUBRConnCntRev,'sfcsBwPortPoolStatUBRConnRejFwd':sfcsBwPortPoolStatUBRConnRejFwd,'sfcsBwPortPoolStatUBRConnRejRev':sfcsBwPortPoolStatUBRConnRejRev,'sfcsBwPortPoolStatUBRAllocBwFwd':sfcsBwPortPoolStatUBRAllocBwFwd,'sfcsBwPortPoolStatUBRAllocBwRev':sfcsBwPortPoolStatUBRAllocBwRev,'sfcsBwPortPoolStatUBRAggPCRFwd':sfcsBwPortPoolStatUBRAggPCRFwd,'sfcsBwPortPoolStatUBRAggPCRRev':sfcsBwPortPoolStatUBRAggPCRRev,'sfcsBwPortPoolStatUBRPrevAdverMAXCTD':sfcsBwPortPoolStatUBRPrevAdverMAXCTD,'sfcsBwPortPoolStatUBRPrevAdverCDV':sfcsBwPortPoolStatUBRPrevAdverCDV,'sfcsBwPortPoolTrapMgmtTable':sfcsBwPortPoolTrapMgmtTable,'sfcsBwPortPoolTrapMgmtEntry':sfcsBwPortPoolTrapMgmtEntry,_AK:sfcsBwPortPoolTrapMgmtIndex,_AL:sfcsBwPortPoolTrapMgmtPoolIndex,'sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd':sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd,'sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev':sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev,'sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd':sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd,'sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev':sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev,'sfcsBwPortPoolTrapMgmtPeakBwTholdFwd':sfcsBwPortPoolTrapMgmtPeakBwTholdFwd,'sfcsBwPortPoolTrapMgmtPeakBwTholdRev':sfcsBwPortPoolTrapMgmtPeakBwTholdRev,'sfcsBwPortPoolTrapMgmtHoldDownTime':sfcsBwPortPoolTrapMgmtHoldDownTime,'sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd':sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd,'sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev':sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev,'sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd':sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd,'sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev':sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev,'sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd':sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd,'sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev':sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev,'sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd':sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd,'sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev':sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev,'sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd':sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd,'sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev':sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev,'sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd':sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd,'sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev':sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev,'sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd':sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd,'sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev':sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev,'sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd':sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd,'sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev':sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev,'sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd':sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd,'sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev':sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev,'sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd':sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd,'sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev':sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev,'sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd':sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd,'sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev':sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev,'sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd':sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd,'sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev':sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev,'sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd':sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd,'sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev':sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev,'sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd':sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd,'sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev':sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev,'sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd':sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd,'sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev':sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev,'sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd':sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd,'sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev':sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev,'sfcsBWPortPoolTrapMgmtBuffUpThold':sfcsBWPortPoolTrapMgmtBuffUpThold,'sfcsBWPortPoolTrapMgmtBuffLoThold':sfcsBWPortPoolTrapMgmtBuffLoThold,'sfcsBWPortPoolTrapMgmtConnRejThold':sfcsBWPortPoolTrapMgmtConnRejThold,'sfcsBuffPools':sfcsBuffPools,'sfcsBuffPrioTable':sfcsBuffPrioTable,'sfcsBuffPrioEntry':sfcsBuffPrioEntry,_AM:sfcsBuffPrioPortIndex,_AN:sfcsBuffPrioPriority,'sfcsBuffPrioAssignCtl':sfcsBuffPrioAssignCtl,'sfcsBuffPrioMinCtl':sfcsBuffPrioMinCtl,'sfcsBuffPrioAssigned':sfcsBuffPrioAssigned,'sfcsBuffPrioAllocated':sfcsBuffPrioAllocated,'sfcsBuffPrioAvailable':sfcsBuffPrioAvailable,'sfcsBuffPrioPeakAlloc':sfcsBuffPrioPeakAlloc,'sfcsBuffPrioConnRejs':sfcsBuffPrioConnRejs,'sfcsBuffPrioUpTholdTrap':sfcsBuffPrioUpTholdTrap,'sfcsBuffPrioLoTholdTrap':sfcsBuffPrioLoTholdTrap,'sfcsBuffPrioConnRejThold':sfcsBuffPrioConnRejThold,'sfcsProxy':sfcsProxy,'sfcsProxyConfig':sfcsProxyConfig,'sfcsProxyConfigTable':sfcsProxyConfigTable,'sfcsProxyConfigEntry':sfcsProxyConfigEntry,_AO:sfcsProxyConfigANIMIndex,'sfcsProxyConfigNUMPORTS':sfcsProxyConfigNUMPORTS,'sfcsProxyConfigTxMemSize':sfcsProxyConfigTxMemSize,'sfcsProxyConfigRxMaxPduSize':sfcsProxyConfigRxMaxPduSize,'sfcsProxyConfigBandWidth':sfcsProxyConfigBandWidth,'sfcsProxyConfigTransmitDone':sfcsProxyConfigTransmitDone,'sfcsProxyConfigReceiveFifoState':sfcsProxyConfigReceiveFifoState,'sfcsProxyConfigPortTransmitMode':sfcsProxyConfigPortTransmitMode,'sfcsProxyConfigReceiveFifoReset':sfcsProxyConfigReceiveFifoReset,'sfcsProxyConfigTxFifoReset':sfcsProxyConfigTxFifoReset,'sfcsProxyConfigReceiveMode':sfcsProxyConfigReceiveMode,'sfcsProxyConfigCaptureMode':sfcsProxyConfigCaptureMode,'sfcsProxyConfigInitPort':sfcsProxyConfigInitPort,'sfcsProxyConfigLoad':sfcsProxyConfigLoad,'sfcsProxyConfigGumbo':sfcsProxyConfigGumbo,'sfcsProxyTrans':sfcsProxyTrans,'sfcsProxyTransTable':sfcsProxyTransTable,'sfcsProxyTransEntry':sfcsProxyTransEntry,_AP:sfcsProxyTransANIMIndex,'sfcsProxyTransEncodeNewPdu':sfcsProxyTransEncodeNewPdu,'sfcsProxyTransVPI':sfcsProxyTransVPI,'sfcsProxyTransVCI':sfcsProxyTransVCI,'sfcsProxyTransPTI':sfcsProxyTransPTI,'sfcsProxyTransCLP':sfcsProxyTransCLP,'sfcsProxyTransPayloadType':sfcsProxyTransPayloadType,'sfcsProxyTransPayloadLength':sfcsProxyTransPayloadLength,'sfcsProxyTransPayloadData':sfcsProxyTransPayloadData,'sfcsProxyTransCount':sfcsProxyTransCount,'sfcsProxyTransPayloadAdaptionLayer':sfcsProxyTransPayloadAdaptionLayer,'sfcsProxyTransMpxMethod':sfcsProxyTransMpxMethod,'sfcsProxyTransControl':sfcsProxyTransControl,'sfcsProxyTransGumbo':sfcsProxyTransGumbo,'sfcsProxyRead':sfcsProxyRead,'sfcsProxyReadTable':sfcsProxyReadTable,'sfcsProxyReadEntry':sfcsProxyReadEntry,_AQ:sfcsProxyReadANIMIndex,'sfcsProxyReadMode':sfcsProxyReadMode,'sfcsProxyReadNewPdu':sfcsProxyReadNewPdu,'sfcsProxyReadGumbo':sfcsProxyReadGumbo,'sfcsProxyReadVPI':sfcsProxyReadVPI,'sfcsProxyReadVCI':sfcsProxyReadVCI,'sfcsProxyReadPTI':sfcsProxyReadPTI,'sfcsProxyReadCLP':sfcsProxyReadCLP,'sfcsProxyReadDataLength':sfcsProxyReadDataLength,'sfcsProxyReadData':sfcsProxyReadData,'sfcsProxyReadPal':sfcsProxyReadPal,'sfcsProxyReadInbyteslosts':sfcsProxyReadInbyteslosts,'sfcsProxyReadInCells':sfcsProxyReadInCells,'sfcsProxyReadInError':sfcsProxyReadInError,'sfcsProxyReadInCellReadError':sfcsProxyReadInCellReadError,'sfcsProxyReadInHecError':sfcsProxyReadInHecError,'sfcsProxyReadInTooBigError':sfcsProxyReadInTooBigError,'sfcsProxyReadInCRCError':sfcsProxyReadInCRCError,'sfcsProxyReadInLengthMismatchError':sfcsProxyReadInLengthMismatchError,'sfcsProxyReadInTotalCells':sfcsProxyReadInTotalCells})