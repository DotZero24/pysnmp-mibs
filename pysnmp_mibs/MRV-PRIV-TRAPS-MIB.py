_w='mrvPrivateTrapsNotifGrp'
_v='mrvPrivateTrapsMandatoryGroup'
_u='mrvPortReflectionLinkUp'
_t='mrvPortReflectionLinkDown'
_s='mrvPortProtectionPrimary'
_r='mrvPortProtectionBackup'
_q='mrvDot1agCfmRecovery'
_p='mrvDot1agCfmFault'
_o='mrvDeviceTemperatureHigh'
_n='mrvDeviceTemperatureNormal'
_m='mrvFANUnitDown'
_l='mrvFANUnitUp'
_k='mrvPowerSupplyDown'
_j='mrvPowerSupplyUp'
_i='mrvAuthenticationFailure'
_h='mrvPortLinkDown'
_g='mrvPortLinkUp'
_f='mrvWarmStart'
_e='mrvColdStart'
_d='agRMepAliveEvent'
_c='agRMepNoConnEvent'
_b='agRMepDiscardEvent'
_a='portLinkDown'
_Z='portLinkUp'
_Y='noAction'
_X='Unsigned32'
_W='OctetString'
_V='read-write'
_U='mrvPortLinActionCause'
_T='mrvPortLinSlavePorts'
_S='mrvDevLosGrActionCause'
_R='mrvDevLosGrSecondaryPort'
_Q='mrvDevLosGrPrimaryPort'
_P='mrvDevLosGrActivePortNumber'
_O='mrvEthOamTrapCcmHighestPrDefect'
_N='mrvEthOamMepIdentifier'
_M='mrvEthOamMaIndex'
_L='mrvEthOamMdLevel'
_K='mrvDevFANIndex'
_J='mrvDevPSIndex'
_I='mrvPortIndex'
_H='Integer32'
_G='read-only'
_F='mrvElementID'
_E='mrvEventLevel'
_D='mrvEventClass'
_C='mrvEventDescription'
_B='current'
_A='MRV-PRIV-TRAPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbPrivTraps=ModuleIdentity((1,3,6,1,4,1,629,1,50,21))
if mibBuilder.loadTexts:nbPrivTraps.setRevisions(('2006-02-22 00:00',))
class TCEventClass(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('serviceAffecting',1),('nonServiceAffecting',2)))
class TCEventLevel(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('info',4),('clear',5)))
class NbEthOamMepId(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
class NbEthOamMDLevel(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class NbEthOamCcmHighestDefectPri(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('defRDICCM',1),('defMACstatus',2),('defRemoteCCM',3),('defErrorCCM',4),('defXconCCM',5)))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_MrvPrivateTraps_ObjectIdentity=ObjectIdentity
mrvPrivateTraps=_MrvPrivateTraps_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,3))
_MrvTrapParameters_ObjectIdentity=ObjectIdentity
mrvTrapParameters=_MrvTrapParameters_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,3,1))
_MrvElementID_Type=DisplayString
_MrvElementID_Object=MibScalar
mrvElementID=_MrvElementID_Object((1,3,6,1,4,1,629,1,50,21,3,1,2),_MrvElementID_Type())
mrvElementID.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvElementID.setStatus(_B)
class _MrvPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MrvPortIndex_Type.__name__=_H
_MrvPortIndex_Object=MibScalar
mrvPortIndex=_MrvPortIndex_Object((1,3,6,1,4,1,629,1,50,21,3,1,5),_MrvPortIndex_Type())
mrvPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvPortIndex.setStatus(_B)
_MrvEventDescription_Type=DisplayString
_MrvEventDescription_Object=MibScalar
mrvEventDescription=_MrvEventDescription_Object((1,3,6,1,4,1,629,1,50,21,3,1,7),_MrvEventDescription_Type())
mrvEventDescription.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEventDescription.setStatus(_B)
_MrvEventClass_Type=TCEventClass
_MrvEventClass_Object=MibScalar
mrvEventClass=_MrvEventClass_Object((1,3,6,1,4,1,629,1,50,21,3,1,8),_MrvEventClass_Type())
mrvEventClass.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEventClass.setStatus(_B)
_MrvEventLevel_Type=TCEventLevel
_MrvEventLevel_Object=MibScalar
mrvEventLevel=_MrvEventLevel_Object((1,3,6,1,4,1,629,1,50,21,3,1,9),_MrvEventLevel_Type())
mrvEventLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEventLevel.setStatus(_B)
_MrvDevPSIndex_Type=Integer32
_MrvDevPSIndex_Object=MibScalar
mrvDevPSIndex=_MrvDevPSIndex_Object((1,3,6,1,4,1,629,1,50,21,3,1,10),_MrvDevPSIndex_Type())
mrvDevPSIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvDevPSIndex.setStatus(_B)
_MrvDevFANIndex_Type=Integer32
_MrvDevFANIndex_Object=MibScalar
mrvDevFANIndex=_MrvDevFANIndex_Object((1,3,6,1,4,1,629,1,50,21,3,1,11),_MrvDevFANIndex_Type())
mrvDevFANIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvDevFANIndex.setStatus(_B)
_MrvEthOamMdLevel_Type=NbEthOamMDLevel
_MrvEthOamMdLevel_Object=MibScalar
mrvEthOamMdLevel=_MrvEthOamMdLevel_Object((1,3,6,1,4,1,629,1,50,21,3,1,12),_MrvEthOamMdLevel_Type())
mrvEthOamMdLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEthOamMdLevel.setStatus(_B)
class _MrvEthOamMaIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MrvEthOamMaIndex_Type.__name__=_X
_MrvEthOamMaIndex_Object=MibScalar
mrvEthOamMaIndex=_MrvEthOamMaIndex_Object((1,3,6,1,4,1,629,1,50,21,3,1,13),_MrvEthOamMaIndex_Type())
mrvEthOamMaIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEthOamMaIndex.setStatus(_B)
_MrvEthOamMepIdentifier_Type=NbEthOamMepId
_MrvEthOamMepIdentifier_Object=MibScalar
mrvEthOamMepIdentifier=_MrvEthOamMepIdentifier_Object((1,3,6,1,4,1,629,1,50,21,3,1,14),_MrvEthOamMepIdentifier_Type())
mrvEthOamMepIdentifier.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEthOamMepIdentifier.setStatus(_B)
_MrvEthOamTrapCcmHighestPrDefect_Type=NbEthOamCcmHighestDefectPri
_MrvEthOamTrapCcmHighestPrDefect_Object=MibScalar
mrvEthOamTrapCcmHighestPrDefect=_MrvEthOamTrapCcmHighestPrDefect_Object((1,3,6,1,4,1,629,1,50,21,3,1,15),_MrvEthOamTrapCcmHighestPrDefect_Type())
mrvEthOamTrapCcmHighestPrDefect.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvEthOamTrapCcmHighestPrDefect.setStatus(_B)
_MrvDevLosGrActivePortNumber_Type=Integer32
_MrvDevLosGrActivePortNumber_Object=MibScalar
mrvDevLosGrActivePortNumber=_MrvDevLosGrActivePortNumber_Object((1,3,6,1,4,1,629,1,50,21,3,1,16),_MrvDevLosGrActivePortNumber_Type())
mrvDevLosGrActivePortNumber.setMaxAccess(_V)
if mibBuilder.loadTexts:mrvDevLosGrActivePortNumber.setStatus(_B)
class _MrvDevLosGrPrimaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_MrvDevLosGrPrimaryPort_Type.__name__=_H
_MrvDevLosGrPrimaryPort_Object=MibScalar
mrvDevLosGrPrimaryPort=_MrvDevLosGrPrimaryPort_Object((1,3,6,1,4,1,629,1,50,21,3,1,17),_MrvDevLosGrPrimaryPort_Type())
mrvDevLosGrPrimaryPort.setMaxAccess(_V)
if mibBuilder.loadTexts:mrvDevLosGrPrimaryPort.setStatus(_B)
class _MrvDevLosGrSecondaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_MrvDevLosGrSecondaryPort_Type.__name__=_H
_MrvDevLosGrSecondaryPort_Object=MibScalar
mrvDevLosGrSecondaryPort=_MrvDevLosGrSecondaryPort_Object((1,3,6,1,4,1,629,1,50,21,3,1,18),_MrvDevLosGrSecondaryPort_Type())
mrvDevLosGrSecondaryPort.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvDevLosGrSecondaryPort.setStatus(_B)
class _MrvDevLosGrActionCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6),('activePortAdminSet',7)))
_MrvDevLosGrActionCause_Type.__name__=_H
_MrvDevLosGrActionCause_Object=MibScalar
mrvDevLosGrActionCause=_MrvDevLosGrActionCause_Object((1,3,6,1,4,1,629,1,50,21,3,1,19),_MrvDevLosGrActionCause_Type())
mrvDevLosGrActionCause.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvDevLosGrActionCause.setStatus(_B)
class _MrvPortLinSlavePorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MrvPortLinSlavePorts_Type.__name__=_W
_MrvPortLinSlavePorts_Object=MibScalar
mrvPortLinSlavePorts=_MrvPortLinSlavePorts_Object((1,3,6,1,4,1,629,1,50,21,3,1,20),_MrvPortLinSlavePorts_Type())
mrvPortLinSlavePorts.setMaxAccess(_V)
if mibBuilder.loadTexts:mrvPortLinSlavePorts.setStatus(_B)
class _MrvPortLinActionCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3),(_b,4),(_c,5),(_d,6)))
_MrvPortLinActionCause_Type.__name__=_H
_MrvPortLinActionCause_Object=MibScalar
mrvPortLinActionCause=_MrvPortLinActionCause_Object((1,3,6,1,4,1,629,1,50,21,3,1,21),_MrvPortLinActionCause_Type())
mrvPortLinActionCause.setMaxAccess(_G)
if mibBuilder.loadTexts:mrvPortLinActionCause.setStatus(_B)
_MrvPrivateGenTraps_ObjectIdentity=ObjectIdentity
mrvPrivateGenTraps=_MrvPrivateGenTraps_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,3,6))
_MrvPrivateGenTrapPrefix_ObjectIdentity=ObjectIdentity
mrvPrivateGenTrapPrefix=_MrvPrivateGenTrapPrefix_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,3,6,0))
_MrvPrivateSpecTraps_ObjectIdentity=ObjectIdentity
mrvPrivateSpecTraps=_MrvPrivateSpecTraps_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,3,7))
_MrvPrivateSpecTrapPrefix_ObjectIdentity=ObjectIdentity
mrvPrivateSpecTrapPrefix=_MrvPrivateSpecTrapPrefix_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,3,7,0))
_MrvPrivateTrapsConformance_ObjectIdentity=ObjectIdentity
mrvPrivateTrapsConformance=_MrvPrivateTrapsConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,100))
_MrvPrivateTrapsMIBCompliances_ObjectIdentity=ObjectIdentity
mrvPrivateTrapsMIBCompliances=_MrvPrivateTrapsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,100,1))
_MrvPrivateTrapsMIBGroups_ObjectIdentity=ObjectIdentity
mrvPrivateTrapsMIBGroups=_MrvPrivateTrapsMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,21,100,2))
mrvPrivateTrapsMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,21,100,2,1))
mrvPrivateTrapsMandatoryGroup.setObjects(*((_A,_I),(_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:mrvPrivateTrapsMandatoryGroup.setStatus(_B)
mrvColdStart=NotificationType((1,3,6,1,4,1,629,1,50,21,3,6,0,1))
mrvColdStart.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:mrvColdStart.setStatus(_B)
mrvWarmStart=NotificationType((1,3,6,1,4,1,629,1,50,21,3,6,0,2))
mrvWarmStart.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:mrvWarmStart.setStatus(_B)
mrvPortLinkDown=NotificationType((1,3,6,1,4,1,629,1,50,21,3,6,0,3))
mrvPortLinkDown.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:mrvPortLinkDown.setStatus(_B)
mrvPortLinkUp=NotificationType((1,3,6,1,4,1,629,1,50,21,3,6,0,4))
mrvPortLinkUp.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:mrvPortLinkUp.setStatus(_B)
mrvAuthenticationFailure=NotificationType((1,3,6,1,4,1,629,1,50,21,3,6,0,5))
mrvAuthenticationFailure.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:mrvAuthenticationFailure.setStatus(_B)
mrvPowerSupplyUp=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,1))
mrvPowerSupplyUp.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_J)))
if mibBuilder.loadTexts:mrvPowerSupplyUp.setStatus(_B)
mrvPowerSupplyDown=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,2))
mrvPowerSupplyDown.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_J)))
if mibBuilder.loadTexts:mrvPowerSupplyDown.setStatus(_B)
mrvFANUnitUp=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,3))
mrvFANUnitUp.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_K)))
if mibBuilder.loadTexts:mrvFANUnitUp.setStatus(_B)
mrvFANUnitDown=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,4))
mrvFANUnitDown.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_K)))
if mibBuilder.loadTexts:mrvFANUnitDown.setStatus(_B)
mrvDeviceTemperatureNormal=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,5))
mrvDeviceTemperatureNormal.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:mrvDeviceTemperatureNormal.setStatus(_B)
mrvDeviceTemperatureHigh=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,6))
mrvDeviceTemperatureHigh.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:mrvDeviceTemperatureHigh.setStatus(_B)
mrvDot1agCfmFault=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,7))
mrvDot1agCfmFault.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:mrvDot1agCfmFault.setStatus(_B)
mrvDot1agCfmRecovery=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,8))
mrvDot1agCfmRecovery.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:mrvDot1agCfmRecovery.setStatus(_B)
mrvPortProtectionBackup=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,9))
mrvPortProtectionBackup.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:mrvPortProtectionBackup.setStatus(_B)
mrvPortProtectionPrimary=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,10))
mrvPortProtectionPrimary.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:mrvPortProtectionPrimary.setStatus(_B)
mrvPortReflectionLinkDown=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,11))
mrvPortReflectionLinkDown.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_I),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:mrvPortReflectionLinkDown.setStatus(_B)
mrvPortReflectionLinkUp=NotificationType((1,3,6,1,4,1,629,1,50,21,3,7,0,12))
mrvPortReflectionLinkUp.setObjects(*((_A,_F),(_A,_C),(_A,_E),(_A,_D),(_A,_I),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:mrvPortReflectionLinkUp.setStatus(_B)
mrvPrivateTrapsNotifGrp=NotificationGroup((1,3,6,1,4,1,629,1,50,21,100,2,2))
mrvPrivateTrapsNotifGrp.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:mrvPrivateTrapsNotifGrp.setStatus(_B)
mrvPrivateTrapsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,21,100,1,1))
mrvPrivateTrapsMIBCompliance.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:mrvPrivateTrapsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TCEventClass':TCEventClass,'TCEventLevel':TCEventLevel,'NbEthOamMepId':NbEthOamMepId,'NbEthOamMDLevel':NbEthOamMDLevel,'NbEthOamCcmHighestDefectPri':NbEthOamCcmHighestDefectPri,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbPrivTraps':nbPrivTraps,'mrvPrivateTraps':mrvPrivateTraps,'mrvTrapParameters':mrvTrapParameters,_F:mrvElementID,_I:mrvPortIndex,_C:mrvEventDescription,_D:mrvEventClass,_E:mrvEventLevel,_J:mrvDevPSIndex,_K:mrvDevFANIndex,_L:mrvEthOamMdLevel,_M:mrvEthOamMaIndex,_N:mrvEthOamMepIdentifier,_O:mrvEthOamTrapCcmHighestPrDefect,_P:mrvDevLosGrActivePortNumber,_Q:mrvDevLosGrPrimaryPort,_R:mrvDevLosGrSecondaryPort,_S:mrvDevLosGrActionCause,_T:mrvPortLinSlavePorts,_U:mrvPortLinActionCause,'mrvPrivateGenTraps':mrvPrivateGenTraps,'mrvPrivateGenTrapPrefix':mrvPrivateGenTrapPrefix,_e:mrvColdStart,_f:mrvWarmStart,_h:mrvPortLinkDown,_g:mrvPortLinkUp,_i:mrvAuthenticationFailure,'mrvPrivateSpecTraps':mrvPrivateSpecTraps,'mrvPrivateSpecTrapPrefix':mrvPrivateSpecTrapPrefix,_j:mrvPowerSupplyUp,_k:mrvPowerSupplyDown,_l:mrvFANUnitUp,_m:mrvFANUnitDown,_n:mrvDeviceTemperatureNormal,_o:mrvDeviceTemperatureHigh,_p:mrvDot1agCfmFault,_q:mrvDot1agCfmRecovery,_r:mrvPortProtectionBackup,_s:mrvPortProtectionPrimary,_t:mrvPortReflectionLinkDown,_u:mrvPortReflectionLinkUp,'mrvPrivateTrapsConformance':mrvPrivateTrapsConformance,'mrvPrivateTrapsMIBCompliances':mrvPrivateTrapsMIBCompliances,'mrvPrivateTrapsMIBCompliance':mrvPrivateTrapsMIBCompliance,'mrvPrivateTrapsMIBGroups':mrvPrivateTrapsMIBGroups,_v:mrvPrivateTrapsMandatoryGroup,_w:mrvPrivateTrapsNotifGrp})