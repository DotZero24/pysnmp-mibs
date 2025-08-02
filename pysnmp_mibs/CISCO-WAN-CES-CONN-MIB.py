_AE='ciscoWanCesConnGeneralGroup'
_AD='ciscoWanCesConnEndptGroup'
_AC='ciscoWanCesConnGroup'
_AB='cesmChanNumNextAvailable'
_AA='cesEndLineNum'
_A9='cesEndChanNum'
_A8='cesmChanDirectRoute'
_A7='cesmChanPrefRouteId'
_A6='cesmConnAdminStatus'
_A5='cesmChanReroute'
_A4='cesmConnFGCRAEnable'
_A3='cesmConnForeSightEnable'
_A2='cesmConnRemotePercentUtil'
_A1='cesmConnRemoteMCR'
_A0='cesmConnRemotePCR'
_z='cesConnPercentUtil'
_y='cesConnMCR'
_x='cesConnPCR'
_w='cesRestrictTrunkType'
_v='cesMaxCost'
_u='cesRoutingPriority'
_t='cesConnServiceType'
_s='cesVpcFlag'
_r='cesMastership'
_q='cesRemoteNSAP'
_p='cesRemoteVci'
_o='cesRemoteVpi'
_n='cesLocalNSAP'
_m='cesLocalVci'
_l='cesLocalVpi'
_k='cesmChanConditionedSigCode'
_j='cesmChanExtTrgIdleSupp'
_i='cesChanConditionedData'
_h='cesChanOnhookCode'
_g='cesChanIdleCodeIntgnPeriod'
_f='cesChanIdleSignalCode'
_e='cesChanIdleDetEnable'
_d='cesChanStrauSciNum'
_c='cesChanConnType'
_b='cesChanPortNum'
_a='cesChanRTDResult'
_Z='cesChanTestState'
_Y='cesChanTestType'
_X='cesChanLocRmtLpbkState'
_W='cesCellLossIntegrationPeriod'
_V='cesCDVRxT'
_U='cesBufMaxSize'
_T='cesPartialFill'
_S='cesCas'
_R='cesCBRClockMode'
_Q='cesCBRService'
_P='cesMapVci'
_O='cesMapVpi'
_N='cesMapPortNum'
_M='cesChanRowStatus'
_L='milliseconds'
_K='TruthValue'
_J='cesEndPortNum'
_I='enable'
_H='cesCnfChanNum'
_G='OctetString'
_F='disable'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-CES-CONN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cesmChan,circuitEmulation=mibBuilder.importSymbols('BASIS-MIB','cesmChan','circuitEmulation')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoWanCesConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,42))
if mibBuilder.loadTexts:ciscoWanCesConnMIB.setRevisions(('2002-09-18 00:00',))
_CesmChanCnfGrp_ObjectIdentity=ObjectIdentity
cesmChanCnfGrp=_CesmChanCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,3,2,1))
_CesmChanCnfGrpTable_Object=MibTable
cesmChanCnfGrpTable=_CesmChanCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,3,2,1,1))
if mibBuilder.loadTexts:cesmChanCnfGrpTable.setStatus(_A)
_CesmChanCnfGrpEntry_Object=MibTableRow
cesmChanCnfGrpEntry=_CesmChanCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1))
cesmChanCnfGrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cesmChanCnfGrpEntry.setStatus(_A)
class _CesCnfChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,2064))
_CesCnfChanNum_Type.__name__=_C
_CesCnfChanNum_Object=MibTableColumn
cesCnfChanNum=_CesCnfChanNum_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,1),_CesCnfChanNum_Type())
cesCnfChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cesCnfChanNum.setStatus(_A)
class _CesChanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3),('outOfService',4)))
_CesChanRowStatus_Type.__name__=_C
_CesChanRowStatus_Object=MibTableColumn
cesChanRowStatus=_CesChanRowStatus_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,2),_CesChanRowStatus_Type())
cesChanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanRowStatus.setStatus(_A)
class _CesMapPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CesMapPortNum_Type.__name__=_C
_CesMapPortNum_Object=MibTableColumn
cesMapPortNum=_CesMapPortNum_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,3),_CesMapPortNum_Type())
cesMapPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cesMapPortNum.setStatus(_A)
class _CesMapVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,14))
_CesMapVpi_Type.__name__=_C
_CesMapVpi_Object=MibTableColumn
cesMapVpi=_CesMapVpi_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,4),_CesMapVpi_Type())
cesMapVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:cesMapVpi.setStatus(_A)
class _CesMapVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,2064))
_CesMapVci_Type.__name__=_C
_CesMapVci_Object=MibTableColumn
cesMapVci=_CesMapVci_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,5),_CesMapVci_Type())
cesMapVci.setMaxAccess(_E)
if mibBuilder.loadTexts:cesMapVci.setStatus(_A)
class _CesCBRService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unstructured',1),('structured',2)))
_CesCBRService_Type.__name__=_C
_CesCBRService_Object=MibTableColumn
cesCBRService=_CesCBRService_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,6),_CesCBRService_Type())
cesCBRService.setMaxAccess(_E)
if mibBuilder.loadTexts:cesCBRService.setStatus(_A)
class _CesCBRClockMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('synchronous',1),('srts',2),('adaptive',3)))
_CesCBRClockMode_Type.__name__=_C
_CesCBRClockMode_Object=MibTableColumn
cesCBRClockMode=_CesCBRClockMode_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,7),_CesCBRClockMode_Type())
cesCBRClockMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cesCBRClockMode.setStatus(_A)
class _CesCas_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('basic',1),('e1Cas',2),('ds1SfCas',3),('ds1EsfCas',4),('ccs',5),('conditionedE1Cas',6),('basicNoPointer',7),('ds1SfCasMF',8),('ds1EsfCasMF',9)))
_CesCas_Type.__name__=_C
_CesCas_Object=MibTableColumn
cesCas=_CesCas_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,8),_CesCas_Type())
cesCas.setMaxAccess(_D)
if mibBuilder.loadTexts:cesCas.setStatus(_A)
class _CesPartialFill_Type(Integer32):defaultValue=47;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,47))
_CesPartialFill_Type.__name__=_C
_CesPartialFill_Object=MibTableColumn
cesPartialFill=_CesPartialFill_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,9),_CesPartialFill_Type())
cesPartialFill.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPartialFill.setStatus(_A)
class _CesBufMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CesBufMaxSize_Type.__name__=_C
_CesBufMaxSize_Object=MibTableColumn
cesBufMaxSize=_CesBufMaxSize_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,10),_CesBufMaxSize_Type())
cesBufMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cesBufMaxSize.setStatus(_A)
class _CesCDVRxT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,65535))
_CesCDVRxT_Type.__name__=_C
_CesCDVRxT_Object=MibTableColumn
cesCDVRxT=_CesCDVRxT_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,11),_CesCDVRxT_Type())
cesCDVRxT.setMaxAccess(_D)
if mibBuilder.loadTexts:cesCDVRxT.setStatus(_A)
class _CesCellLossIntegrationPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,65535))
_CesCellLossIntegrationPeriod_Type.__name__=_C
_CesCellLossIntegrationPeriod_Object=MibTableColumn
cesCellLossIntegrationPeriod=_CesCellLossIntegrationPeriod_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,12),_CesCellLossIntegrationPeriod_Type())
cesCellLossIntegrationPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cesCellLossIntegrationPeriod.setStatus(_A)
if mibBuilder.loadTexts:cesCellLossIntegrationPeriod.setUnits(_L)
class _CesChanLocRmtLpbkState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_CesChanLocRmtLpbkState_Type.__name__=_C
_CesChanLocRmtLpbkState_Object=MibTableColumn
cesChanLocRmtLpbkState=_CesChanLocRmtLpbkState_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,13),_CesChanLocRmtLpbkState_Type())
cesChanLocRmtLpbkState.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanLocRmtLpbkState.setStatus(_A)
class _CesChanTestType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('testcon',1),('testdelay',2),('notest',3),('testconsti',4),('testdelaysti',5)))
_CesChanTestType_Type.__name__=_C
_CesChanTestType_Object=MibTableColumn
cesChanTestType=_CesChanTestType_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,14),_CesChanTestType_Type())
cesChanTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanTestType.setStatus(_A)
class _CesChanTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('passed',1),('failed',2),('inprogress',3),('notinprogress',4)))
_CesChanTestState_Type.__name__=_C
_CesChanTestState_Object=MibTableColumn
cesChanTestState=_CesChanTestState_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,15),_CesChanTestState_Type())
cesChanTestState.setMaxAccess(_E)
if mibBuilder.loadTexts:cesChanTestState.setStatus(_A)
class _CesChanRTDResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CesChanRTDResult_Type.__name__=_C
_CesChanRTDResult_Object=MibTableColumn
cesChanRTDResult=_CesChanRTDResult_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,16),_CesChanRTDResult_Type())
cesChanRTDResult.setMaxAccess(_E)
if mibBuilder.loadTexts:cesChanRTDResult.setStatus(_A)
if mibBuilder.loadTexts:cesChanRTDResult.setUnits(_L)
class _CesChanPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CesChanPortNum_Type.__name__=_C
_CesChanPortNum_Object=MibTableColumn
cesChanPortNum=_CesChanPortNum_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,17),_CesChanPortNum_Type())
cesChanPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanPortNum.setStatus(_A)
class _CesChanConnType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pvc',1),('svc',2),('spvc',3)))
_CesChanConnType_Type.__name__=_C
_CesChanConnType_Object=MibTableColumn
cesChanConnType=_CesChanConnType_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,18),_CesChanConnType_Type())
cesChanConnType.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanConnType.setStatus(_A)
class _CesChanStrauSciNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonStrauChannel',1),('sci1',2),('sci2',3),('sci3',4),('sci4',5)))
_CesChanStrauSciNum_Type.__name__=_C
_CesChanStrauSciNum_Object=MibTableColumn
cesChanStrauSciNum=_CesChanStrauSciNum_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,19),_CesChanStrauSciNum_Type())
cesChanStrauSciNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanStrauSciNum.setStatus(_A)
class _CesChanIdleDetEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('enableOnhookDet',2),('enableIdlePatternDet',3)))
_CesChanIdleDetEnable_Type.__name__=_C
_CesChanIdleDetEnable_Object=MibTableColumn
cesChanIdleDetEnable=_CesChanIdleDetEnable_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,20),_CesChanIdleDetEnable_Type())
cesChanIdleDetEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanIdleDetEnable.setStatus(_A)
class _CesChanIdleSignalCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CesChanIdleSignalCode_Type.__name__=_C
_CesChanIdleSignalCode_Object=MibTableColumn
cesChanIdleSignalCode=_CesChanIdleSignalCode_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,21),_CesChanIdleSignalCode_Type())
cesChanIdleSignalCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanIdleSignalCode.setStatus(_A)
class _CesChanIdleCodeIntgnPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CesChanIdleCodeIntgnPeriod_Type.__name__=_C
_CesChanIdleCodeIntgnPeriod_Object=MibTableColumn
cesChanIdleCodeIntgnPeriod=_CesChanIdleCodeIntgnPeriod_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,22),_CesChanIdleCodeIntgnPeriod_Type())
cesChanIdleCodeIntgnPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanIdleCodeIntgnPeriod.setStatus(_A)
if mibBuilder.loadTexts:cesChanIdleCodeIntgnPeriod.setUnits('seconds')
class _CesChanOnhookCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CesChanOnhookCode_Type.__name__=_C
_CesChanOnhookCode_Object=MibTableColumn
cesChanOnhookCode=_CesChanOnhookCode_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,23),_CesChanOnhookCode_Type())
cesChanOnhookCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanOnhookCode.setStatus(_A)
class _CesChanConditionedData_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CesChanConditionedData_Type.__name__=_C
_CesChanConditionedData_Object=MibTableColumn
cesChanConditionedData=_CesChanConditionedData_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,24),_CesChanConditionedData_Type())
cesChanConditionedData.setMaxAccess(_D)
if mibBuilder.loadTexts:cesChanConditionedData.setStatus(_A)
class _CesmChanExtTrgIdleSupp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disablesuppression',1),('enableSuppresion',2)))
_CesmChanExtTrgIdleSupp_Type.__name__=_C
_CesmChanExtTrgIdleSupp_Object=MibTableColumn
cesmChanExtTrgIdleSupp=_CesmChanExtTrgIdleSupp_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,25),_CesmChanExtTrgIdleSupp_Type())
cesmChanExtTrgIdleSupp.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmChanExtTrgIdleSupp.setStatus(_A)
class _CesmChanConditionedSigCode_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CesmChanConditionedSigCode_Type.__name__=_C
_CesmChanConditionedSigCode_Object=MibTableColumn
cesmChanConditionedSigCode=_CesmChanConditionedSigCode_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,26),_CesmChanConditionedSigCode_Type())
cesmChanConditionedSigCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmChanConditionedSigCode.setStatus(_A)
class _CesLocalVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CesLocalVpi_Type.__name__=_C
_CesLocalVpi_Object=MibTableColumn
cesLocalVpi=_CesLocalVpi_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,27),_CesLocalVpi_Type())
cesLocalVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:cesLocalVpi.setStatus(_A)
class _CesLocalVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CesLocalVci_Type.__name__=_C
_CesLocalVci_Object=MibTableColumn
cesLocalVci=_CesLocalVci_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,28),_CesLocalVci_Type())
cesLocalVci.setMaxAccess(_E)
if mibBuilder.loadTexts:cesLocalVci.setStatus(_A)
class _CesLocalNSAP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CesLocalNSAP_Type.__name__=_G
_CesLocalNSAP_Object=MibTableColumn
cesLocalNSAP=_CesLocalNSAP_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,29),_CesLocalNSAP_Type())
cesLocalNSAP.setMaxAccess(_D)
if mibBuilder.loadTexts:cesLocalNSAP.setStatus(_A)
class _CesRemoteVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CesRemoteVpi_Type.__name__=_C
_CesRemoteVpi_Object=MibTableColumn
cesRemoteVpi=_CesRemoteVpi_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,30),_CesRemoteVpi_Type())
cesRemoteVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:cesRemoteVpi.setStatus(_A)
class _CesRemoteVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CesRemoteVci_Type.__name__=_C
_CesRemoteVci_Object=MibTableColumn
cesRemoteVci=_CesRemoteVci_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,31),_CesRemoteVci_Type())
cesRemoteVci.setMaxAccess(_D)
if mibBuilder.loadTexts:cesRemoteVci.setStatus(_A)
class _CesRemoteNSAP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CesRemoteNSAP_Type.__name__=_G
_CesRemoteNSAP_Object=MibTableColumn
cesRemoteNSAP=_CesRemoteNSAP_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,32),_CesRemoteNSAP_Type())
cesRemoteNSAP.setMaxAccess(_D)
if mibBuilder.loadTexts:cesRemoteNSAP.setStatus(_A)
class _CesMastership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('unkown',3)))
_CesMastership_Type.__name__=_C
_CesMastership_Object=MibTableColumn
cesMastership=_CesMastership_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,33),_CesMastership_Type())
cesMastership.setMaxAccess(_D)
if mibBuilder.loadTexts:cesMastership.setStatus(_A)
class _CesVpcFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vpc',1),('vcc',2)))
_CesVpcFlag_Type.__name__=_C
_CesVpcFlag_Object=MibTableColumn
cesVpcFlag=_CesVpcFlag_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,34),_CesVpcFlag_Type())
cesVpcFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:cesVpcFlag.setStatus(_A)
class _CesConnServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*(('cbr',1),('vbr',2),('ubr',4),('atfr',5),('abrstd',6),('abrfst',7),('cbr1',21),('vbr1rt',22),('vbr2rt',23),('vbr3rt',24),('vbr1nrt',25),('vbr2nrt',26),('vbr3nrt',27),('ubr1',28),('ubr2',29),('stdabr',30),('cbr2',31),('cbr3',32)))
_CesConnServiceType_Type.__name__=_C
_CesConnServiceType_Object=MibTableColumn
cesConnServiceType=_CesConnServiceType_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,35),_CesConnServiceType_Type())
cesConnServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:cesConnServiceType.setStatus(_A)
class _CesRoutingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CesRoutingPriority_Type.__name__=_C
_CesRoutingPriority_Object=MibTableColumn
cesRoutingPriority=_CesRoutingPriority_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,36),_CesRoutingPriority_Type())
cesRoutingPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cesRoutingPriority.setStatus(_A)
class _CesMaxCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CesMaxCost_Type.__name__=_C
_CesMaxCost_Object=MibTableColumn
cesMaxCost=_CesMaxCost_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,37),_CesMaxCost_Type())
cesMaxCost.setMaxAccess(_D)
if mibBuilder.loadTexts:cesMaxCost.setStatus(_A)
class _CesRestrictTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noresriction',1),('terrestrialTrunk',2),('sateliteTrunk',3)))
_CesRestrictTrunkType_Type.__name__=_C
_CesRestrictTrunkType_Object=MibTableColumn
cesRestrictTrunkType=_CesRestrictTrunkType_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,38),_CesRestrictTrunkType_Type())
cesRestrictTrunkType.setMaxAccess(_D)
if mibBuilder.loadTexts:cesRestrictTrunkType.setStatus(_A)
_CesConnPCR_Type=Integer32
_CesConnPCR_Object=MibTableColumn
cesConnPCR=_CesConnPCR_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,39),_CesConnPCR_Type())
cesConnPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:cesConnPCR.setStatus(_A)
_CesConnMCR_Type=Integer32
_CesConnMCR_Object=MibTableColumn
cesConnMCR=_CesConnMCR_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,40),_CesConnMCR_Type())
cesConnMCR.setMaxAccess(_D)
if mibBuilder.loadTexts:cesConnMCR.setStatus(_A)
class _CesConnPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CesConnPercentUtil_Type.__name__=_C
_CesConnPercentUtil_Object=MibTableColumn
cesConnPercentUtil=_CesConnPercentUtil_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,41),_CesConnPercentUtil_Type())
cesConnPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:cesConnPercentUtil.setStatus(_A)
_CesmConnRemotePCR_Type=Integer32
_CesmConnRemotePCR_Object=MibTableColumn
cesmConnRemotePCR=_CesmConnRemotePCR_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,42),_CesmConnRemotePCR_Type())
cesmConnRemotePCR.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmConnRemotePCR.setStatus(_A)
_CesmConnRemoteMCR_Type=Integer32
_CesmConnRemoteMCR_Object=MibTableColumn
cesmConnRemoteMCR=_CesmConnRemoteMCR_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,43),_CesmConnRemoteMCR_Type())
cesmConnRemoteMCR.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmConnRemoteMCR.setStatus(_A)
class _CesmConnRemotePercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CesmConnRemotePercentUtil_Type.__name__=_C
_CesmConnRemotePercentUtil_Object=MibTableColumn
cesmConnRemotePercentUtil=_CesmConnRemotePercentUtil_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,44),_CesmConnRemotePercentUtil_Type())
cesmConnRemotePercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmConnRemotePercentUtil.setStatus(_A)
class _CesmConnForeSightEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_CesmConnForeSightEnable_Type.__name__=_C
_CesmConnForeSightEnable_Object=MibTableColumn
cesmConnForeSightEnable=_CesmConnForeSightEnable_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,45),_CesmConnForeSightEnable_Type())
cesmConnForeSightEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmConnForeSightEnable.setStatus(_A)
class _CesmConnFGCRAEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_F,2)))
_CesmConnFGCRAEnable_Type.__name__=_C
_CesmConnFGCRAEnable_Object=MibTableColumn
cesmConnFGCRAEnable=_CesmConnFGCRAEnable_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,46),_CesmConnFGCRAEnable_Type())
cesmConnFGCRAEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmConnFGCRAEnable.setStatus(_A)
class _CesmChanReroute_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_CesmChanReroute_Type.__name__=_C
_CesmChanReroute_Object=MibTableColumn
cesmChanReroute=_CesmChanReroute_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,47),_CesmChanReroute_Type())
cesmChanReroute.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmChanReroute.setStatus(_A)
class _CesmConnAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CesmConnAdminStatus_Type.__name__=_C
_CesmConnAdminStatus_Object=MibTableColumn
cesmConnAdminStatus=_CesmConnAdminStatus_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,48),_CesmConnAdminStatus_Type())
cesmConnAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmConnAdminStatus.setStatus(_A)
class _CesmChanPrefRouteId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CesmChanPrefRouteId_Type.__name__=_C
_CesmChanPrefRouteId_Object=MibTableColumn
cesmChanPrefRouteId=_CesmChanPrefRouteId_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,49),_CesmChanPrefRouteId_Type())
cesmChanPrefRouteId.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmChanPrefRouteId.setStatus(_A)
class _CesmChanDirectRoute_Type(TruthValue):defaultValue=2
_CesmChanDirectRoute_Type.__name__=_K
_CesmChanDirectRoute_Object=MibTableColumn
cesmChanDirectRoute=_CesmChanDirectRoute_Object((1,3,6,1,4,1,351,110,5,3,2,1,1,1,50),_CesmChanDirectRoute_Type())
cesmChanDirectRoute.setMaxAccess(_D)
if mibBuilder.loadTexts:cesmChanDirectRoute.setStatus(_A)
class _CesmChanNumNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CesmChanNumNextAvailable_Type.__name__=_C
_CesmChanNumNextAvailable_Object=MibScalar
cesmChanNumNextAvailable=_CesmChanNumNextAvailable_Object((1,3,6,1,4,1,351,110,5,3,2,1,2),_CesmChanNumNextAvailable_Type())
cesmChanNumNextAvailable.setMaxAccess(_E)
if mibBuilder.loadTexts:cesmChanNumNextAvailable.setStatus(_A)
_CesmEndPtMapGrp_ObjectIdentity=ObjectIdentity
cesmEndPtMapGrp=_CesmEndPtMapGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,3,3))
_CesmEndPtMapGrpTable_Object=MibTable
cesmEndPtMapGrpTable=_CesmEndPtMapGrpTable_Object((1,3,6,1,4,1,351,110,5,3,3,1))
if mibBuilder.loadTexts:cesmEndPtMapGrpTable.setStatus(_A)
_CesmEndPtMapGrpEntry_Object=MibTableRow
cesmEndPtMapGrpEntry=_CesmEndPtMapGrpEntry_Object((1,3,6,1,4,1,351,110,5,3,3,1,1))
cesmEndPtMapGrpEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cesmEndPtMapGrpEntry.setStatus(_A)
class _CesEndPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CesEndPortNum_Type.__name__=_C
_CesEndPortNum_Object=MibTableColumn
cesEndPortNum=_CesEndPortNum_Object((1,3,6,1,4,1,351,110,5,3,3,1,1,1),_CesEndPortNum_Type())
cesEndPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cesEndPortNum.setStatus(_A)
class _CesEndChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,2080))
_CesEndChanNum_Type.__name__=_C
_CesEndChanNum_Object=MibTableColumn
cesEndChanNum=_CesEndChanNum_Object((1,3,6,1,4,1,351,110,5,3,3,1,1,2),_CesEndChanNum_Type())
cesEndChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cesEndChanNum.setStatus(_A)
class _CesEndLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CesEndLineNum_Type.__name__=_C
_CesEndLineNum_Object=MibTableColumn
cesEndLineNum=_CesEndLineNum_Object((1,3,6,1,4,1,351,110,5,3,3,1,1,3),_CesEndLineNum_Type())
cesEndLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cesEndLineNum.setStatus(_A)
_CiscoWanCesConnMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanCesConnMIBConformance=_CiscoWanCesConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,42,2))
_CiscoWanCesConnMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanCesConnMIBGroups=_CiscoWanCesConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,42,2,1))
_CiscoWanCesConnMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanCesConnMIBCompliances=_CiscoWanCesConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,42,2,2))
ciscoWanCesConnGroup=ObjectGroup((1,3,6,1,4,1,351,150,42,2,1,1))
ciscoWanCesConnGroup.setObjects(*((_B,_H),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ciscoWanCesConnGroup.setStatus(_A)
ciscoWanCesConnEndptGroup=ObjectGroup((1,3,6,1,4,1,351,150,42,2,1,2))
ciscoWanCesConnEndptGroup.setObjects(*((_B,_J),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:ciscoWanCesConnEndptGroup.setStatus(_A)
ciscoWanCesConnGeneralGroup=ObjectGroup((1,3,6,1,4,1,351,150,42,2,1,3))
ciscoWanCesConnGeneralGroup.setObjects((_B,_AB))
if mibBuilder.loadTexts:ciscoWanCesConnGeneralGroup.setStatus(_A)
ciscoWanCesConnCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,42,2,2,1))
ciscoWanCesConnCompliance.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:ciscoWanCesConnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cesmChanCnfGrp':cesmChanCnfGrp,'cesmChanCnfGrpTable':cesmChanCnfGrpTable,'cesmChanCnfGrpEntry':cesmChanCnfGrpEntry,_H:cesCnfChanNum,_M:cesChanRowStatus,_N:cesMapPortNum,_O:cesMapVpi,_P:cesMapVci,_Q:cesCBRService,_R:cesCBRClockMode,_S:cesCas,_T:cesPartialFill,_U:cesBufMaxSize,_V:cesCDVRxT,_W:cesCellLossIntegrationPeriod,_X:cesChanLocRmtLpbkState,_Y:cesChanTestType,_Z:cesChanTestState,_a:cesChanRTDResult,_b:cesChanPortNum,_c:cesChanConnType,_d:cesChanStrauSciNum,_e:cesChanIdleDetEnable,_f:cesChanIdleSignalCode,_g:cesChanIdleCodeIntgnPeriod,_h:cesChanOnhookCode,_i:cesChanConditionedData,_j:cesmChanExtTrgIdleSupp,_k:cesmChanConditionedSigCode,_l:cesLocalVpi,_m:cesLocalVci,_n:cesLocalNSAP,_o:cesRemoteVpi,_p:cesRemoteVci,_q:cesRemoteNSAP,_r:cesMastership,_s:cesVpcFlag,_t:cesConnServiceType,_u:cesRoutingPriority,_v:cesMaxCost,_w:cesRestrictTrunkType,_x:cesConnPCR,_y:cesConnMCR,_z:cesConnPercentUtil,_A0:cesmConnRemotePCR,_A1:cesmConnRemoteMCR,_A2:cesmConnRemotePercentUtil,_A3:cesmConnForeSightEnable,_A4:cesmConnFGCRAEnable,_A5:cesmChanReroute,_A6:cesmConnAdminStatus,_A7:cesmChanPrefRouteId,_A8:cesmChanDirectRoute,_AB:cesmChanNumNextAvailable,'cesmEndPtMapGrp':cesmEndPtMapGrp,'cesmEndPtMapGrpTable':cesmEndPtMapGrpTable,'cesmEndPtMapGrpEntry':cesmEndPtMapGrpEntry,_J:cesEndPortNum,_A9:cesEndChanNum,_AA:cesEndLineNum,'ciscoWanCesConnMIB':ciscoWanCesConnMIB,'ciscoWanCesConnMIBConformance':ciscoWanCesConnMIBConformance,'ciscoWanCesConnMIBGroups':ciscoWanCesConnMIBGroups,_AC:ciscoWanCesConnGroup,_AD:ciscoWanCesConnEndptGroup,_AE:ciscoWanCesConnGeneralGroup,'ciscoWanCesConnMIBCompliances':ciscoWanCesConnMIBCompliances,'ciscoWanCesConnCompliance':ciscoWanCesConnCompliance})