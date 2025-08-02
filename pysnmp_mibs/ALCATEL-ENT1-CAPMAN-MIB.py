_AP='alaCapabilityIpmcMaxLimitsGroup'
_AO='alaCapManSwLicensingInfoGroup'
_AN='alaCapManSwLicensingGroup'
_AM='alaCapManHashControlGroup'
_AL='alaCapManSourceLearningTableGroup'
_AK='alaCapManMirrorTableGroup'
_AJ='alaCapManTcamTableGroup'
_AI='alaCapManVrfTableGroup'
_AH='alaLicenseManagerDemoDayAlert'
_AG='alaMibVcLicenseExpirationDate'
_AF='alaMibVcLicenseUpgradeStatus'
_AE='alaMibVcLicenseTimeRemain'
_AD='alaMibVcLicenseVcSlot'
_AC='alaMibVcLicenseType'
_AB='alaVcLicenseExpirationDate'
_AA='alaVcLicenseUpgradeStatus'
_A9='alaVcLicenseVcSlot'
_A8='alaVcLicenseType'
_A7='alaVcLicenseTimeRemain'
_A6='alaVcLicenseBitMap'
_A5='alaCapManDcbOprMode'
_A4='alaCapManDcbCfgMode'
_A3='alaCapabilityIpmcMaxOperLimit'
_A2='alaCapabilityIpmcMaxAdminLimit'
_A1='alaLicenseType'
_A0='alaLicensedApplication'
_z='alaCapManVcSwLicensingAfnStatus'
_y='alaCapManVcSwLicensingAfnInfo'
_x='alaCapManVcSwLicensingActionArg'
_w='alaCapManVcSwLicensingAction'
_v='alaCapManSwLicensingActionArg'
_u='alaCapManSwLicensingAction'
_t='alaCapManNonUCHashControl'
_s='alaCapManUdpTcpPortMode'
_r='alaCapManHashMode'
_q='alaCapabilitySourceLearningMode'
_p='alaCapabilityMirrorLimit'
_o='alaCapabilityTcamMode'
_n='alaCapabilityVrfLimit'
_m='alaMibVcLicensedMacAddress'
_l='alaMibVcLicensedSerialNum'
_k='revoked'
_j='expired'
_i='upgraded'
_h='ov-generated'
_g='timebased'
_f='alaVcLicensedMacAddress'
_e='alaVcLicensedSerialNum'
_d='alaLicenseId'
_c='applyFile'
_b='default'
_a='alaCapabilitySourceLearningCapability'
_Z='alaCapabilitySourceLearningContext'
_Y='alaCapabilityMirrorCapability'
_X='alaCapabilityMirrorContext'
_W='alaCapabilityTcamCapability'
_V='alaCapabilityTcamContext'
_U='alaCapabilityVrfCapability'
_T='alaCapabilityVrfContext'
_S='Unsigned32'
_R='alaLicenseTimeRemaining'
_Q='alaMibVcLicenseFeatureId'
_P='permanent'
_O='demo'
_N='unknown'
_M='disabled'
_L='enabled'
_K='global'
_J='SnmpAdminString'
_I='OctetString'
_H='obsolete'
_G='read-write'
_F='not-accessible'
_E='read-only'
_D='deprecated'
_C='Integer32'
_B='current'
_A='ALCATEL-ENT1-CAPMAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1CapMan,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1CapMan')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
alcatelIND1CapManMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1))
if mibBuilder.loadTexts:alcatelIND1CapManMIB.setRevisions(('2009-11-23 00:00',))
_AlcatelIND1CapManMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1CapManMIBObjects=_AlcatelIND1CapManMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1))
if mibBuilder.loadTexts:alcatelIND1CapManMIBObjects.setStatus(_B)
_AlaCapabilityMibNotifications_ObjectIdentity=ObjectIdentity
alaCapabilityMibNotifications=_AlaCapabilityMibNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,0))
_AlaCapabilityManager_ObjectIdentity=ObjectIdentity
alaCapabilityManager=_AlaCapabilityManager_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1))
_AlaCapManVrfTable_Object=MibTable
alaCapManVrfTable=_AlaCapManVrfTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,1))
if mibBuilder.loadTexts:alaCapManVrfTable.setStatus(_D)
_AlaCapManVrfEntry_Object=MibTableRow
alaCapManVrfEntry=_AlaCapManVrfEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,1,1))
alaCapManVrfEntry.setIndexNames((0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:alaCapManVrfEntry.setStatus(_D)
class _AlaCapabilityVrfContext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('primary',2),('subsidiary',3)))
_AlaCapabilityVrfContext_Type.__name__=_C
_AlaCapabilityVrfContext_Object=MibTableColumn
alaCapabilityVrfContext=_AlaCapabilityVrfContext_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,1,1,1),_AlaCapabilityVrfContext_Type())
alaCapabilityVrfContext.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilityVrfContext.setStatus(_D)
class _AlaCapabilityVrfCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('ipv4Routes',1),('ipv6Routes',2),('ipv4Interfaces',3),('ipv6Interfaces',4),('mcastInterfaces',5),('pimRPS',6),('bgpPeers',7),('bgpRoutes',8),('ripRoutes',9),('routingProtocols',10),('maxOSPF',11)))
_AlaCapabilityVrfCapability_Type.__name__=_C
_AlaCapabilityVrfCapability_Object=MibTableColumn
alaCapabilityVrfCapability=_AlaCapabilityVrfCapability_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,1,1,2),_AlaCapabilityVrfCapability_Type())
alaCapabilityVrfCapability.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilityVrfCapability.setStatus(_D)
class _AlaCapabilityVrfLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524288))
_AlaCapabilityVrfLimit_Type.__name__=_C
_AlaCapabilityVrfLimit_Object=MibTableColumn
alaCapabilityVrfLimit=_AlaCapabilityVrfLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,1,1,3),_AlaCapabilityVrfLimit_Type())
alaCapabilityVrfLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapabilityVrfLimit.setStatus(_D)
_AlaCapManTcamTable_Object=MibTable
alaCapManTcamTable=_AlaCapManTcamTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,2))
if mibBuilder.loadTexts:alaCapManTcamTable.setStatus(_D)
_AlaCapManTcamEntry_Object=MibTableRow
alaCapManTcamEntry=_AlaCapManTcamEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,2,1))
alaCapManTcamEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:alaCapManTcamEntry.setStatus(_D)
class _AlaCapabilityTcamContext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_AlaCapabilityTcamContext_Type.__name__=_C
_AlaCapabilityTcamContext_Object=MibTableColumn
alaCapabilityTcamContext=_AlaCapabilityTcamContext_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,2,1,1),_AlaCapabilityTcamContext_Type())
alaCapabilityTcamContext.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilityTcamContext.setStatus(_D)
class _AlaCapabilityTcamCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('mode',1))
_AlaCapabilityTcamCapability_Type.__name__=_C
_AlaCapabilityTcamCapability_Object=MibTableColumn
alaCapabilityTcamCapability=_AlaCapabilityTcamCapability_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,2,1,2),_AlaCapabilityTcamCapability_Type())
alaCapabilityTcamCapability.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilityTcamCapability.setStatus(_D)
class _AlaCapabilityTcamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_AlaCapabilityTcamMode_Type.__name__=_C
_AlaCapabilityTcamMode_Object=MibTableColumn
alaCapabilityTcamMode=_AlaCapabilityTcamMode_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,2,1,3),_AlaCapabilityTcamMode_Type())
alaCapabilityTcamMode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapabilityTcamMode.setStatus(_D)
_AlaCapManMirrorTable_Object=MibTable
alaCapManMirrorTable=_AlaCapManMirrorTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,3))
if mibBuilder.loadTexts:alaCapManMirrorTable.setStatus(_D)
_AlaCapManMirrorEntry_Object=MibTableRow
alaCapManMirrorEntry=_AlaCapManMirrorEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,3,1))
alaCapManMirrorEntry.setIndexNames((0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:alaCapManMirrorEntry.setStatus(_D)
class _AlaCapabilityMirrorContext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_AlaCapabilityMirrorContext_Type.__name__=_C
_AlaCapabilityMirrorContext_Object=MibTableColumn
alaCapabilityMirrorContext=_AlaCapabilityMirrorContext_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,3,1,1),_AlaCapabilityMirrorContext_Type())
alaCapabilityMirrorContext.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilityMirrorContext.setStatus(_D)
class _AlaCapabilityMirrorCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('maxMonitorSess',1))
_AlaCapabilityMirrorCapability_Type.__name__=_C
_AlaCapabilityMirrorCapability_Object=MibTableColumn
alaCapabilityMirrorCapability=_AlaCapabilityMirrorCapability_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,3,1,2),_AlaCapabilityMirrorCapability_Type())
alaCapabilityMirrorCapability.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilityMirrorCapability.setStatus(_D)
class _AlaCapabilityMirrorLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlaCapabilityMirrorLimit_Type.__name__=_C
_AlaCapabilityMirrorLimit_Object=MibTableColumn
alaCapabilityMirrorLimit=_AlaCapabilityMirrorLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,3,1,3),_AlaCapabilityMirrorLimit_Type())
alaCapabilityMirrorLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapabilityMirrorLimit.setStatus(_D)
_AlaCapManSourceLearningTable_Object=MibTable
alaCapManSourceLearningTable=_AlaCapManSourceLearningTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,4))
if mibBuilder.loadTexts:alaCapManSourceLearningTable.setStatus(_D)
_AlaCapManSourceLearningEntry_Object=MibTableRow
alaCapManSourceLearningEntry=_AlaCapManSourceLearningEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,4,1))
alaCapManSourceLearningEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:alaCapManSourceLearningEntry.setStatus(_D)
class _AlaCapabilitySourceLearningContext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_K,1))
_AlaCapabilitySourceLearningContext_Type.__name__=_C
_AlaCapabilitySourceLearningContext_Object=MibTableColumn
alaCapabilitySourceLearningContext=_AlaCapabilitySourceLearningContext_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,4,1,1),_AlaCapabilitySourceLearningContext_Type())
alaCapabilitySourceLearningContext.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilitySourceLearningContext.setStatus(_D)
class _AlaCapabilitySourceLearningCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('mode',1))
_AlaCapabilitySourceLearningCapability_Type.__name__=_C
_AlaCapabilitySourceLearningCapability_Object=MibTableColumn
alaCapabilitySourceLearningCapability=_AlaCapabilitySourceLearningCapability_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,4,1,2),_AlaCapabilitySourceLearningCapability_Type())
alaCapabilitySourceLearningCapability.setMaxAccess(_F)
if mibBuilder.loadTexts:alaCapabilitySourceLearningCapability.setStatus(_D)
class _AlaCapabilitySourceLearningMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('centralized',1),('distributed',2)))
_AlaCapabilitySourceLearningMode_Type.__name__=_C
_AlaCapabilitySourceLearningMode_Object=MibTableColumn
alaCapabilitySourceLearningMode=_AlaCapabilitySourceLearningMode_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,4,1,3),_AlaCapabilitySourceLearningMode_Type())
alaCapabilitySourceLearningMode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapabilitySourceLearningMode.setStatus(_D)
_AlaCapManHashControlCommands_ObjectIdentity=ObjectIdentity
alaCapManHashControlCommands=_AlaCapManHashControlCommands_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,5))
if mibBuilder.loadTexts:alaCapManHashControlCommands.setStatus(_B)
class _AlaCapManHashMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('brief',1),('extended',2)))
_AlaCapManHashMode_Type.__name__=_C
_AlaCapManHashMode_Object=MibScalar
alaCapManHashMode=_AlaCapManHashMode_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,5,1),_AlaCapManHashMode_Type())
alaCapManHashMode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManHashMode.setStatus(_B)
class _AlaCapManUdpTcpPortMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaCapManUdpTcpPortMode_Type.__name__=_C
_AlaCapManUdpTcpPortMode_Object=MibScalar
alaCapManUdpTcpPortMode=_AlaCapManUdpTcpPortMode_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,5,2),_AlaCapManUdpTcpPortMode_Type())
alaCapManUdpTcpPortMode.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManUdpTcpPortMode.setStatus(_B)
class _AlaCapManNonUCHashControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaCapManNonUCHashControl_Type.__name__=_C
_AlaCapManNonUCHashControl_Object=MibScalar
alaCapManNonUCHashControl=_AlaCapManNonUCHashControl_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,5,3),_AlaCapManNonUCHashControl_Type())
alaCapManNonUCHashControl.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManNonUCHashControl.setStatus(_B)
_AlaCapManSwLicensingConfig_ObjectIdentity=ObjectIdentity
alaCapManSwLicensingConfig=_AlaCapManSwLicensingConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6))
class _AlaCapManSwLicensingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_b,0),(_c,1),('applyKey',2),('deactivate',3)))
_AlaCapManSwLicensingAction_Type.__name__=_C
_AlaCapManSwLicensingAction_Object=MibScalar
alaCapManSwLicensingAction=_AlaCapManSwLicensingAction_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6,1),_AlaCapManSwLicensingAction_Type())
alaCapManSwLicensingAction.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManSwLicensingAction.setStatus(_B)
class _AlaCapManSwLicensingActionArg_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaCapManSwLicensingActionArg_Type.__name__=_J
_AlaCapManSwLicensingActionArg_Object=MibScalar
alaCapManSwLicensingActionArg=_AlaCapManSwLicensingActionArg_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6,2),_AlaCapManSwLicensingActionArg_Type())
alaCapManSwLicensingActionArg.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManSwLicensingActionArg.setStatus(_B)
class _AlaCapManVcSwLicensingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),(_c,1),('applyAfn',2)))
_AlaCapManVcSwLicensingAction_Type.__name__=_C
_AlaCapManVcSwLicensingAction_Object=MibScalar
alaCapManVcSwLicensingAction=_AlaCapManVcSwLicensingAction_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6,3),_AlaCapManVcSwLicensingAction_Type())
alaCapManVcSwLicensingAction.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManVcSwLicensingAction.setStatus(_B)
class _AlaCapManVcSwLicensingActionArg_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaCapManVcSwLicensingActionArg_Type.__name__=_J
_AlaCapManVcSwLicensingActionArg_Object=MibScalar
alaCapManVcSwLicensingActionArg=_AlaCapManVcSwLicensingActionArg_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6,4),_AlaCapManVcSwLicensingActionArg_Type())
alaCapManVcSwLicensingActionArg.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManVcSwLicensingActionArg.setStatus(_B)
class _AlaCapManVcSwLicensingAfnInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_AlaCapManVcSwLicensingAfnInfo_Type.__name__=_I
_AlaCapManVcSwLicensingAfnInfo_Object=MibScalar
alaCapManVcSwLicensingAfnInfo=_AlaCapManVcSwLicensingAfnInfo_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6,5),_AlaCapManVcSwLicensingAfnInfo_Type())
alaCapManVcSwLicensingAfnInfo.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapManVcSwLicensingAfnInfo.setStatus(_B)
class _AlaCapManVcSwLicensingAfnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('inProgress',2),('successful',3),('failed',4)))
_AlaCapManVcSwLicensingAfnStatus_Type.__name__=_C
_AlaCapManVcSwLicensingAfnStatus_Object=MibScalar
alaCapManVcSwLicensingAfnStatus=_AlaCapManVcSwLicensingAfnStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,6,6),_AlaCapManVcSwLicensingAfnStatus_Type())
alaCapManVcSwLicensingAfnStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCapManVcSwLicensingAfnStatus.setStatus(_B)
_AlaCapManSwLicensingInfoTable_Object=MibTable
alaCapManSwLicensingInfoTable=_AlaCapManSwLicensingInfoTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,7))
if mibBuilder.loadTexts:alaCapManSwLicensingInfoTable.setStatus(_B)
_AlaCapManSwLicensingInfoEntry_Object=MibTableRow
alaCapManSwLicensingInfoEntry=_AlaCapManSwLicensingInfoEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,7,1))
alaCapManSwLicensingInfoEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:alaCapManSwLicensingInfoEntry.setStatus(_B)
class _AlaLicenseId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AlaLicenseId_Type.__name__=_S
_AlaLicenseId_Object=MibTableColumn
alaLicenseId=_AlaLicenseId_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,7,1,1),_AlaLicenseId_Type())
alaLicenseId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLicenseId.setStatus(_B)
class _AlaLicensedApplication_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AlaLicensedApplication_Type.__name__=_J
_AlaLicensedApplication_Object=MibTableColumn
alaLicensedApplication=_AlaLicensedApplication_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,7,1,2),_AlaLicensedApplication_Type())
alaLicensedApplication.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLicensedApplication.setStatus(_B)
class _AlaLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('invalid',0),(_O,1),(_P,2)))
_AlaLicenseType_Type.__name__=_C
_AlaLicenseType_Object=MibTableColumn
alaLicenseType=_AlaLicenseType_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,7,1,3),_AlaLicenseType_Type())
alaLicenseType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLicenseType.setStatus(_B)
class _AlaLicenseTimeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,60))
_AlaLicenseTimeRemaining_Type.__name__=_C
_AlaLicenseTimeRemaining_Object=MibTableColumn
alaLicenseTimeRemaining=_AlaLicenseTimeRemaining_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,7,1,4),_AlaLicenseTimeRemaining_Type())
alaLicenseTimeRemaining.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLicenseTimeRemaining.setStatus(_B)
_AlaCapabilityIpmcMaxLimits_ObjectIdentity=ObjectIdentity
alaCapabilityIpmcMaxLimits=_AlaCapabilityIpmcMaxLimits_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,8))
class _AlaCapabilityIpmcMaxAdminLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_AlaCapabilityIpmcMaxAdminLimit_Type.__name__=_C
_AlaCapabilityIpmcMaxAdminLimit_Object=MibScalar
alaCapabilityIpmcMaxAdminLimit=_AlaCapabilityIpmcMaxAdminLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,8,1),_AlaCapabilityIpmcMaxAdminLimit_Type())
alaCapabilityIpmcMaxAdminLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:alaCapabilityIpmcMaxAdminLimit.setStatus(_B)
class _AlaCapabilityIpmcMaxOperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_AlaCapabilityIpmcMaxOperLimit_Type.__name__=_C
_AlaCapabilityIpmcMaxOperLimit_Object=MibScalar
alaCapabilityIpmcMaxOperLimit=_AlaCapabilityIpmcMaxOperLimit_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,8,2),_AlaCapabilityIpmcMaxOperLimit_Type())
alaCapabilityIpmcMaxOperLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCapabilityIpmcMaxOperLimit.setStatus(_B)
_AlaCapManFeatureControlCommands_ObjectIdentity=ObjectIdentity
alaCapManFeatureControlCommands=_AlaCapManFeatureControlCommands_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,9))
class _AlaCapManDcbCfgMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaCapManDcbCfgMode_Type.__name__=_C
_AlaCapManDcbCfgMode_Object=MibScalar
alaCapManDcbCfgMode=_AlaCapManDcbCfgMode_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,9,1),_AlaCapManDcbCfgMode_Type())
alaCapManDcbCfgMode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCapManDcbCfgMode.setStatus(_B)
class _AlaCapManDcbOprMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaCapManDcbOprMode_Type.__name__=_C
_AlaCapManDcbOprMode_Object=MibScalar
alaCapManDcbOprMode=_AlaCapManDcbOprMode_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,9,2),_AlaCapManDcbOprMode_Type())
alaCapManDcbOprMode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCapManDcbOprMode.setStatus(_B)
_AlaCapManVcSwLicensingInfoTable_Object=MibTable
alaCapManVcSwLicensingInfoTable=_AlaCapManVcSwLicensingInfoTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10))
if mibBuilder.loadTexts:alaCapManVcSwLicensingInfoTable.setStatus(_H)
_AlaCapManVcSwLicensingInfoEntry_Object=MibTableRow
alaCapManVcSwLicensingInfoEntry=_AlaCapManVcSwLicensingInfoEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1))
alaCapManVcSwLicensingInfoEntry.setIndexNames((0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:alaCapManVcSwLicensingInfoEntry.setStatus(_H)
class _AlaVcLicensedSerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,25));fixedLength=25
_AlaVcLicensedSerialNum_Type.__name__=_I
_AlaVcLicensedSerialNum_Object=MibTableColumn
alaVcLicensedSerialNum=_AlaVcLicensedSerialNum_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,1),_AlaVcLicensedSerialNum_Type())
alaVcLicensedSerialNum.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVcLicensedSerialNum.setStatus(_H)
_AlaVcLicensedMacAddress_Type=MacAddress
_AlaVcLicensedMacAddress_Object=MibTableColumn
alaVcLicensedMacAddress=_AlaVcLicensedMacAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,2),_AlaVcLicensedMacAddress_Type())
alaVcLicensedMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVcLicensedMacAddress.setStatus(_H)
class _AlaVcLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_g,3),(_h,4)))
_AlaVcLicenseType_Type.__name__=_C
_AlaVcLicenseType_Object=MibTableColumn
alaVcLicenseType=_AlaVcLicenseType_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,3),_AlaVcLicenseType_Type())
alaVcLicenseType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVcLicenseType.setStatus(_H)
class _AlaVcLicenseVcSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AlaVcLicenseVcSlot_Type.__name__=_C
_AlaVcLicenseVcSlot_Object=MibTableColumn
alaVcLicenseVcSlot=_AlaVcLicenseVcSlot_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,4),_AlaVcLicenseVcSlot_Type())
alaVcLicenseVcSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVcLicenseVcSlot.setStatus(_H)
class _AlaVcLicenseBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AlaVcLicenseBitMap_Type.__name__=_C
_AlaVcLicenseBitMap_Object=MibTableColumn
alaVcLicenseBitMap=_AlaVcLicenseBitMap_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,5),_AlaVcLicenseBitMap_Type())
alaVcLicenseBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVcLicenseBitMap.setStatus(_H)
class _AlaVcLicenseTimeRemain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,60))
_AlaVcLicenseTimeRemain_Type.__name__=_C
_AlaVcLicenseTimeRemain_Object=MibTableColumn
alaVcLicenseTimeRemain=_AlaVcLicenseTimeRemain_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,6),_AlaVcLicenseTimeRemain_Type())
alaVcLicenseTimeRemain.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVcLicenseTimeRemain.setStatus(_H)
class _AlaVcLicenseUpgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3),(_N,4)))
_AlaVcLicenseUpgradeStatus_Type.__name__=_C
_AlaVcLicenseUpgradeStatus_Object=MibTableColumn
alaVcLicenseUpgradeStatus=_AlaVcLicenseUpgradeStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,7),_AlaVcLicenseUpgradeStatus_Type())
alaVcLicenseUpgradeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVcLicenseUpgradeStatus.setStatus(_H)
_AlaVcLicenseExpirationDate_Type=DateAndTime
_AlaVcLicenseExpirationDate_Object=MibTableColumn
alaVcLicenseExpirationDate=_AlaVcLicenseExpirationDate_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,10,1,8),_AlaVcLicenseExpirationDate_Type())
alaVcLicenseExpirationDate.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVcLicenseExpirationDate.setStatus(_H)
_AlaCapManMibVcSwLicensingInfoTable_Object=MibTable
alaCapManMibVcSwLicensingInfoTable=_AlaCapManMibVcSwLicensingInfoTable_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11))
if mibBuilder.loadTexts:alaCapManMibVcSwLicensingInfoTable.setStatus(_B)
_AlaCapManMibVcSwLicensingInfoEntry_Object=MibTableRow
alaCapManMibVcSwLicensingInfoEntry=_AlaCapManMibVcSwLicensingInfoEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1))
alaCapManMibVcSwLicensingInfoEntry.setIndexNames((0,_A,_l),(0,_A,_m),(0,_A,_Q))
if mibBuilder.loadTexts:alaCapManMibVcSwLicensingInfoEntry.setStatus(_B)
class _AlaMibVcLicensedSerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(25,25));fixedLength=25
_AlaMibVcLicensedSerialNum_Type.__name__=_I
_AlaMibVcLicensedSerialNum_Object=MibTableColumn
alaMibVcLicensedSerialNum=_AlaMibVcLicensedSerialNum_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,1),_AlaMibVcLicensedSerialNum_Type())
alaMibVcLicensedSerialNum.setMaxAccess(_F)
if mibBuilder.loadTexts:alaMibVcLicensedSerialNum.setStatus(_B)
_AlaMibVcLicensedMacAddress_Type=MacAddress
_AlaMibVcLicensedMacAddress_Object=MibTableColumn
alaMibVcLicensedMacAddress=_AlaMibVcLicensedMacAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,2),_AlaMibVcLicensedMacAddress_Type())
alaMibVcLicensedMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:alaMibVcLicensedMacAddress.setStatus(_B)
class _AlaMibVcLicenseFeatureId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('advanced',1),('datacenter',2),('xniu16',3),('afn',4),('poe',5)))
_AlaMibVcLicenseFeatureId_Type.__name__=_C
_AlaMibVcLicenseFeatureId_Object=MibTableColumn
alaMibVcLicenseFeatureId=_AlaMibVcLicenseFeatureId_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,3),_AlaMibVcLicenseFeatureId_Type())
alaMibVcLicenseFeatureId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaMibVcLicenseFeatureId.setStatus(_B)
class _AlaMibVcLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_g,3),(_h,4)))
_AlaMibVcLicenseType_Type.__name__=_C
_AlaMibVcLicenseType_Object=MibTableColumn
alaMibVcLicenseType=_AlaMibVcLicenseType_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,4),_AlaMibVcLicenseType_Type())
alaMibVcLicenseType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaMibVcLicenseType.setStatus(_B)
class _AlaMibVcLicenseVcSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AlaMibVcLicenseVcSlot_Type.__name__=_C
_AlaMibVcLicenseVcSlot_Object=MibTableColumn
alaMibVcLicenseVcSlot=_AlaMibVcLicenseVcSlot_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,5),_AlaMibVcLicenseVcSlot_Type())
alaMibVcLicenseVcSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:alaMibVcLicenseVcSlot.setStatus(_B)
class _AlaMibVcLicenseTimeRemain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,60))
_AlaMibVcLicenseTimeRemain_Type.__name__=_C
_AlaMibVcLicenseTimeRemain_Object=MibTableColumn
alaMibVcLicenseTimeRemain=_AlaMibVcLicenseTimeRemain_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,6),_AlaMibVcLicenseTimeRemain_Type())
alaMibVcLicenseTimeRemain.setMaxAccess(_E)
if mibBuilder.loadTexts:alaMibVcLicenseTimeRemain.setStatus(_B)
class _AlaMibVcLicenseUpgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3),('not-applicable',4),(_N,5)))
_AlaMibVcLicenseUpgradeStatus_Type.__name__=_C
_AlaMibVcLicenseUpgradeStatus_Object=MibTableColumn
alaMibVcLicenseUpgradeStatus=_AlaMibVcLicenseUpgradeStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,7),_AlaMibVcLicenseUpgradeStatus_Type())
alaMibVcLicenseUpgradeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaMibVcLicenseUpgradeStatus.setStatus(_B)
_AlaMibVcLicenseExpirationDate_Type=DateAndTime
_AlaMibVcLicenseExpirationDate_Object=MibTableColumn
alaMibVcLicenseExpirationDate=_AlaMibVcLicenseExpirationDate_Object((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,1,11,1,8),_AlaMibVcLicenseExpirationDate_Type())
alaMibVcLicenseExpirationDate.setMaxAccess(_E)
if mibBuilder.loadTexts:alaMibVcLicenseExpirationDate.setStatus(_B)
_AlaCapManConformance_ObjectIdentity=ObjectIdentity
alaCapManConformance=_AlaCapManConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2))
_AlaCapManGroups_ObjectIdentity=ObjectIdentity
alaCapManGroups=_AlaCapManGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1))
_AlaCapManCompliances_ObjectIdentity=ObjectIdentity
alaCapManCompliances=_AlaCapManCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,2))
alaCapManVrfTableGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,1))
alaCapManVrfTableGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:alaCapManVrfTableGroup.setStatus(_B)
alaCapManTcamTableGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,2))
alaCapManTcamTableGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:alaCapManTcamTableGroup.setStatus(_B)
alaCapManMirrorTableGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,3))
alaCapManMirrorTableGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:alaCapManMirrorTableGroup.setStatus(_B)
alaCapManSourceLearningTableGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,4))
alaCapManSourceLearningTableGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:alaCapManSourceLearningTableGroup.setStatus(_B)
alaCapManHashControlGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,5))
alaCapManHashControlGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:alaCapManHashControlGroup.setStatus(_B)
alaCapManSwLicensingGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,6))
alaCapManSwLicensingGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:alaCapManSwLicensingGroup.setStatus(_B)
alaCapManSwLicensingInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,7))
alaCapManSwLicensingInfoGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_R)))
if mibBuilder.loadTexts:alaCapManSwLicensingInfoGroup.setStatus(_B)
alaCapabilityIpmcMaxLimitsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,8))
alaCapabilityIpmcMaxLimitsGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:alaCapabilityIpmcMaxLimitsGroup.setStatus(_B)
alaCapManDcbCfgModeGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,9))
alaCapManDcbCfgModeGroup.setObjects(*((_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:alaCapManDcbCfgModeGroup.setStatus(_B)
alaVcLicenseCfgGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,10))
alaVcLicenseCfgGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:alaVcLicenseCfgGroup.setStatus(_B)
alaMibVcLicenseCfgGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,11))
alaMibVcLicenseCfgGroup.setObjects(*((_A,_Q),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:alaMibVcLicenseCfgGroup.setStatus(_B)
alaLicenseManagerDemoDayAlert=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,0,1))
alaLicenseManagerDemoDayAlert.setObjects((_A,_R))
if mibBuilder.loadTexts:alaLicenseManagerDemoDayAlert.setStatus(_B)
alaCapManTrapGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,1,12))
alaCapManTrapGroup.setObjects((_A,_AH))
if mibBuilder.loadTexts:alaCapManTrapGroup.setStatus(_B)
alaCapManCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,60,1,1,2,2,1))
alaCapManCompliance.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:alaCapManCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1CapManMIB':alcatelIND1CapManMIB,'alcatelIND1CapManMIBObjects':alcatelIND1CapManMIBObjects,'alaCapabilityMibNotifications':alaCapabilityMibNotifications,_AH:alaLicenseManagerDemoDayAlert,'alaCapabilityManager':alaCapabilityManager,'alaCapManVrfTable':alaCapManVrfTable,'alaCapManVrfEntry':alaCapManVrfEntry,_T:alaCapabilityVrfContext,_U:alaCapabilityVrfCapability,_n:alaCapabilityVrfLimit,'alaCapManTcamTable':alaCapManTcamTable,'alaCapManTcamEntry':alaCapManTcamEntry,_V:alaCapabilityTcamContext,_W:alaCapabilityTcamCapability,_o:alaCapabilityTcamMode,'alaCapManMirrorTable':alaCapManMirrorTable,'alaCapManMirrorEntry':alaCapManMirrorEntry,_X:alaCapabilityMirrorContext,_Y:alaCapabilityMirrorCapability,_p:alaCapabilityMirrorLimit,'alaCapManSourceLearningTable':alaCapManSourceLearningTable,'alaCapManSourceLearningEntry':alaCapManSourceLearningEntry,_Z:alaCapabilitySourceLearningContext,_a:alaCapabilitySourceLearningCapability,_q:alaCapabilitySourceLearningMode,'alaCapManHashControlCommands':alaCapManHashControlCommands,_r:alaCapManHashMode,_s:alaCapManUdpTcpPortMode,_t:alaCapManNonUCHashControl,'alaCapManSwLicensingConfig':alaCapManSwLicensingConfig,_u:alaCapManSwLicensingAction,_v:alaCapManSwLicensingActionArg,_w:alaCapManVcSwLicensingAction,_x:alaCapManVcSwLicensingActionArg,_y:alaCapManVcSwLicensingAfnInfo,_z:alaCapManVcSwLicensingAfnStatus,'alaCapManSwLicensingInfoTable':alaCapManSwLicensingInfoTable,'alaCapManSwLicensingInfoEntry':alaCapManSwLicensingInfoEntry,_d:alaLicenseId,_A0:alaLicensedApplication,_A1:alaLicenseType,_R:alaLicenseTimeRemaining,'alaCapabilityIpmcMaxLimits':alaCapabilityIpmcMaxLimits,_A2:alaCapabilityIpmcMaxAdminLimit,_A3:alaCapabilityIpmcMaxOperLimit,'alaCapManFeatureControlCommands':alaCapManFeatureControlCommands,_A4:alaCapManDcbCfgMode,_A5:alaCapManDcbOprMode,'alaCapManVcSwLicensingInfoTable':alaCapManVcSwLicensingInfoTable,'alaCapManVcSwLicensingInfoEntry':alaCapManVcSwLicensingInfoEntry,_e:alaVcLicensedSerialNum,_f:alaVcLicensedMacAddress,_A8:alaVcLicenseType,_A9:alaVcLicenseVcSlot,_A6:alaVcLicenseBitMap,_A7:alaVcLicenseTimeRemain,_AA:alaVcLicenseUpgradeStatus,_AB:alaVcLicenseExpirationDate,'alaCapManMibVcSwLicensingInfoTable':alaCapManMibVcSwLicensingInfoTable,'alaCapManMibVcSwLicensingInfoEntry':alaCapManMibVcSwLicensingInfoEntry,_l:alaMibVcLicensedSerialNum,_m:alaMibVcLicensedMacAddress,_Q:alaMibVcLicenseFeatureId,_AC:alaMibVcLicenseType,_AD:alaMibVcLicenseVcSlot,_AE:alaMibVcLicenseTimeRemain,_AF:alaMibVcLicenseUpgradeStatus,_AG:alaMibVcLicenseExpirationDate,'alaCapManConformance':alaCapManConformance,'alaCapManGroups':alaCapManGroups,_AI:alaCapManVrfTableGroup,_AJ:alaCapManTcamTableGroup,_AK:alaCapManMirrorTableGroup,_AL:alaCapManSourceLearningTableGroup,_AM:alaCapManHashControlGroup,_AN:alaCapManSwLicensingGroup,_AO:alaCapManSwLicensingInfoGroup,_AP:alaCapabilityIpmcMaxLimitsGroup,'alaCapManDcbCfgModeGroup':alaCapManDcbCfgModeGroup,'alaVcLicenseCfgGroup':alaVcLicenseCfgGroup,'alaMibVcLicenseCfgGroup':alaMibVcLicenseCfgGroup,'alaCapManTrapGroup':alaCapManTrapGroup,'alaCapManCompliances':alaCapManCompliances,'alaCapManCompliance':alaCapManCompliance})