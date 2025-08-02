_A3='fsPtpPortPtpStatus'
_A2='fsPtpPortUnicastNegOption'
_A1='fsPtpContextRowStatus'
_A0='fsPtpAdminStatus'
_z='fsPtpPortState'
_y='fsPtpTransparentDataSetEntry'
_x='fsPtpTimeDataSetEntry'
_w='fsPtpParentDataSetEntry'
_v='fsPtpCurrentDataSetEntry'
_u='fsPtpClockDataSetEntry'
_t='accessible-for-notify'
_s='fsPtpAltTimeScaleKeyId'
_r='fsPtpSAId'
_q='fsPtpSecKeyId'
_p='fsPtpAccMasterAddr'
_o='fsPtpAccMasterAddLength'
_n='fsPtpAccMasterNetworkProtocol'
_m='fsPtpUnicastMasterAddr'
_l='fsPtpUnicastMasterAddLength'
_k='fsPtpUnicastMasterNetworkProtocol'
_j='fsPtpGrandMasterClusterAddr'
_i='fsPtpGrandMasterClusterAddLength'
_h='fsPtpGrandMasterClusterNetworkProtocol'
_g='fsPtpTransparentPortIndex'
_f='fsPtpForeignMasterPortIndex'
_e='fsPtpForeignMasterClockIdentity'
_d='peertopeer'
_c='endtoend'
_b='unknown'
_a='ieee8021'
_Z='profitnet'
_Y='controlnet'
_X='devicenet'
_W='ieee8023'
_V='udpipv6'
_U='udpipv4'
_T='critical'
_S='Unsigned32'
_R='disabled'
_Q='fsPtpTrapDomainNumber'
_P='FsPtpPortNumber'
_O='fsPtpPortIndex'
_N='fsPtpGlobalErrTrapType'
_M='DisplayString'
_L='read-create'
_K='fsPtpTrapContextName'
_J='fsPtpDomainNumber'
_I='fsPtpContextId'
_H='TruthValue'
_G='OctetString'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='SUPERMICRO-PTP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_H)
fsPtpMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,45))
if mibBuilder.loadTexts:fsPtpMIB.setRevisions(('2012-09-05 00:00',))
class FsPtpPortNumber(TextualConvention,Integer32):status=_A;displayHint='d'
_FsPtpObjects_ObjectIdentity=ObjectIdentity
fsPtpObjects=_FsPtpObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1))
_FsPtpGeneralGroup_ObjectIdentity=ObjectIdentity
fsPtpGeneralGroup=_FsPtpGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,1))
class _FsPtpGlobalSysCtrl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPtpGlobalSysCtrl_Type.__name__=_D
_FsPtpGlobalSysCtrl_Object=MibScalar
fsPtpGlobalSysCtrl=_FsPtpGlobalSysCtrl_Object((1,3,6,1,4,1,10876,101,2,45,1,1,1),_FsPtpGlobalSysCtrl_Type())
fsPtpGlobalSysCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpGlobalSysCtrl.setStatus(_A)
class _FsPtpGblTraceOption_Type(DisplayString):defaultValue=OctetString(_T)
_FsPtpGblTraceOption_Type.__name__=_M
_FsPtpGblTraceOption_Object=MibScalar
fsPtpGblTraceOption=_FsPtpGblTraceOption_Object((1,3,6,1,4,1,10876,101,2,45,1,1,2),_FsPtpGblTraceOption_Type())
fsPtpGblTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpGblTraceOption.setStatus(_A)
class _FsPtpPrimaryContext_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpPrimaryContext_Type.__name__=_D
_FsPtpPrimaryContext_Object=MibScalar
fsPtpPrimaryContext=_FsPtpPrimaryContext_Object((1,3,6,1,4,1,10876,101,2,45,1,1,3),_FsPtpPrimaryContext_Type())
fsPtpPrimaryContext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPrimaryContext.setStatus(_A)
_FsPtpTable_Object=MibTable
fsPtpTable=_FsPtpTable_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4))
if mibBuilder.loadTexts:fsPtpTable.setStatus(_A)
_FsPtpEntry_Object=MibTableRow
fsPtpEntry=_FsPtpEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1))
fsPtpEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:fsPtpEntry.setStatus(_A)
class _FsPtpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpContextId_Type.__name__=_D
_FsPtpContextId_Object=MibTableColumn
fsPtpContextId=_FsPtpContextId_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1,1),_FsPtpContextId_Type())
fsPtpContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpContextId.setStatus(_A)
class _FsPtpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_R,2)))
_FsPtpAdminStatus_Type.__name__=_D
_FsPtpAdminStatus_Object=MibTableColumn
fsPtpAdminStatus=_FsPtpAdminStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1,2),_FsPtpAdminStatus_Type())
fsPtpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAdminStatus.setStatus(_A)
class _FsPtpTraceOption_Type(DisplayString):defaultValue=OctetString(_T)
_FsPtpTraceOption_Type.__name__=_M
_FsPtpTraceOption_Object=MibTableColumn
fsPtpTraceOption=_FsPtpTraceOption_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1,3),_FsPtpTraceOption_Type())
fsPtpTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTraceOption.setStatus(_A)
class _FsPtpContextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l2Context',1),('l3Context',2),('l2Andl3Context',3)))
_FsPtpContextType_Type.__name__=_D
_FsPtpContextType_Object=MibTableColumn
fsPtpContextType=_FsPtpContextType_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1,4),_FsPtpContextType_Type())
fsPtpContextType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpContextType.setStatus(_A)
class _FsPtpPrimaryDomain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpPrimaryDomain_Type.__name__=_D
_FsPtpPrimaryDomain_Object=MibTableColumn
fsPtpPrimaryDomain=_FsPtpPrimaryDomain_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1,5),_FsPtpPrimaryDomain_Type())
fsPtpPrimaryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPrimaryDomain.setStatus(_A)
_FsPtpContextRowStatus_Type=RowStatus
_FsPtpContextRowStatus_Object=MibTableColumn
fsPtpContextRowStatus=_FsPtpContextRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,1,4,1,6),_FsPtpContextRowStatus_Type())
fsPtpContextRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsPtpContextRowStatus.setStatus(_A)
_FsPtpDomainDataSet_ObjectIdentity=ObjectIdentity
fsPtpDomainDataSet=_FsPtpDomainDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,2))
_FsPtpDomainDataSetTable_Object=MibTable
fsPtpDomainDataSetTable=_FsPtpDomainDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1))
if mibBuilder.loadTexts:fsPtpDomainDataSetTable.setStatus(_A)
_FsPtpDomainDataSetEntry_Object=MibTableRow
fsPtpDomainDataSetEntry=_FsPtpDomainDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1,1))
fsPtpDomainDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fsPtpDomainDataSetEntry.setStatus(_A)
class _FsPtpDomainNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpDomainNumber_Type.__name__=_D
_FsPtpDomainNumber_Object=MibTableColumn
fsPtpDomainNumber=_FsPtpDomainNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1,1,1),_FsPtpDomainNumber_Type())
fsPtpDomainNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpDomainNumber.setStatus(_A)
class _FsPtpDomainClockMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('boundary',1),('ordinary',2),('transparent',3),('forward',4),('management',5)))
_FsPtpDomainClockMode_Type.__name__=_D
_FsPtpDomainClockMode_Object=MibTableColumn
fsPtpDomainClockMode=_FsPtpDomainClockMode_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1,1,2),_FsPtpDomainClockMode_Type())
fsPtpDomainClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpDomainClockMode.setStatus(_A)
class _FsPtpDomainClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpDomainClockIdentity_Type.__name__=_G
_FsPtpDomainClockIdentity_Object=MibTableColumn
fsPtpDomainClockIdentity=_FsPtpDomainClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1,1,3),_FsPtpDomainClockIdentity_Type())
fsPtpDomainClockIdentity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpDomainClockIdentity.setStatus(_A)
_FsPtpDomainGMClusterQueryInterval_Type=Integer32
_FsPtpDomainGMClusterQueryInterval_Object=MibTableColumn
fsPtpDomainGMClusterQueryInterval=_FsPtpDomainGMClusterQueryInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1,1,4),_FsPtpDomainGMClusterQueryInterval_Type())
fsPtpDomainGMClusterQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpDomainGMClusterQueryInterval.setStatus(_A)
_FsPtpDomainRowStatus_Type=RowStatus
_FsPtpDomainRowStatus_Object=MibTableColumn
fsPtpDomainRowStatus=_FsPtpDomainRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,2,1,1,5),_FsPtpDomainRowStatus_Type())
fsPtpDomainRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsPtpDomainRowStatus.setStatus(_A)
_FsPtpDefaultDataSet_ObjectIdentity=ObjectIdentity
fsPtpDefaultDataSet=_FsPtpDefaultDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,3))
_FsPtpClockDataSetTable_Object=MibTable
fsPtpClockDataSetTable=_FsPtpClockDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1))
if mibBuilder.loadTexts:fsPtpClockDataSetTable.setStatus(_A)
_FsPtpClockDataSetEntry_Object=MibTableRow
fsPtpClockDataSetEntry=_FsPtpClockDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1))
if mibBuilder.loadTexts:fsPtpClockDataSetEntry.setStatus(_A)
class _FsPtpClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpClockIdentity_Type.__name__=_G
_FsPtpClockIdentity_Object=MibTableColumn
fsPtpClockIdentity=_FsPtpClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,1),_FsPtpClockIdentity_Type())
fsPtpClockIdentity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpClockIdentity.setStatus(_A)
class _FsPtpClockTwoStepFlag_Type(TruthValue):defaultValue=2
_FsPtpClockTwoStepFlag_Type.__name__=_H
_FsPtpClockTwoStepFlag_Object=MibTableColumn
fsPtpClockTwoStepFlag=_FsPtpClockTwoStepFlag_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,2),_FsPtpClockTwoStepFlag_Type())
fsPtpClockTwoStepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockTwoStepFlag.setStatus(_A)
class _FsPtpClockNumberPorts_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FsPtpClockNumberPorts_Type.__name__=_D
_FsPtpClockNumberPorts_Object=MibTableColumn
fsPtpClockNumberPorts=_FsPtpClockNumberPorts_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,3),_FsPtpClockNumberPorts_Type())
fsPtpClockNumberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockNumberPorts.setStatus(_A)
class _FsPtpClockClass_Type(Integer32):defaultValue=248;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpClockClass_Type.__name__=_D
_FsPtpClockClass_Object=MibTableColumn
fsPtpClockClass=_FsPtpClockClass_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,4),_FsPtpClockClass_Type())
fsPtpClockClass.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpClockClass.setStatus(_A)
class _FsPtpClockAccuracy_Type(Integer32):defaultValue=254;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpClockAccuracy_Type.__name__=_D
_FsPtpClockAccuracy_Object=MibTableColumn
fsPtpClockAccuracy=_FsPtpClockAccuracy_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,5),_FsPtpClockAccuracy_Type())
fsPtpClockAccuracy.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpClockAccuracy.setStatus(_A)
class _FsPtpClockOffsetScaledLogVariance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPtpClockOffsetScaledLogVariance_Type.__name__=_D
_FsPtpClockOffsetScaledLogVariance_Object=MibTableColumn
fsPtpClockOffsetScaledLogVariance=_FsPtpClockOffsetScaledLogVariance_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,6),_FsPtpClockOffsetScaledLogVariance_Type())
fsPtpClockOffsetScaledLogVariance.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpClockOffsetScaledLogVariance.setStatus(_A)
class _FsPtpClockPriority1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpClockPriority1_Type.__name__=_D
_FsPtpClockPriority1_Object=MibTableColumn
fsPtpClockPriority1=_FsPtpClockPriority1_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,7),_FsPtpClockPriority1_Type())
fsPtpClockPriority1.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockPriority1.setStatus(_A)
class _FsPtpClockPriority2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpClockPriority2_Type.__name__=_D
_FsPtpClockPriority2_Object=MibTableColumn
fsPtpClockPriority2=_FsPtpClockPriority2_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,8),_FsPtpClockPriority2_Type())
fsPtpClockPriority2.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockPriority2.setStatus(_A)
class _FsPtpClockSlaveOnly_Type(TruthValue):defaultValue=2
_FsPtpClockSlaveOnly_Type.__name__=_H
_FsPtpClockSlaveOnly_Object=MibTableColumn
fsPtpClockSlaveOnly=_FsPtpClockSlaveOnly_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,9),_FsPtpClockSlaveOnly_Type())
fsPtpClockSlaveOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockSlaveOnly.setStatus(_A)
class _FsPtpClockPathTraceOption_Type(TruthValue):defaultValue=2
_FsPtpClockPathTraceOption_Type.__name__=_H
_FsPtpClockPathTraceOption_Object=MibTableColumn
fsPtpClockPathTraceOption=_FsPtpClockPathTraceOption_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,10),_FsPtpClockPathTraceOption_Type())
fsPtpClockPathTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockPathTraceOption.setStatus(_A)
class _FsPtpClockAccMasterMaxSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPtpClockAccMasterMaxSize_Type.__name__=_D
_FsPtpClockAccMasterMaxSize_Object=MibTableColumn
fsPtpClockAccMasterMaxSize=_FsPtpClockAccMasterMaxSize_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,11),_FsPtpClockAccMasterMaxSize_Type())
fsPtpClockAccMasterMaxSize.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpClockAccMasterMaxSize.setStatus(_A)
class _FsPtpClockSecurityEnabled_Type(TruthValue):defaultValue=2
_FsPtpClockSecurityEnabled_Type.__name__=_H
_FsPtpClockSecurityEnabled_Object=MibTableColumn
fsPtpClockSecurityEnabled=_FsPtpClockSecurityEnabled_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,12),_FsPtpClockSecurityEnabled_Type())
fsPtpClockSecurityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockSecurityEnabled.setStatus(_A)
class _FsPtpClockNumOfSA_Type(Unsigned32):defaultValue=128
_FsPtpClockNumOfSA_Type.__name__=_S
_FsPtpClockNumOfSA_Object=MibTableColumn
fsPtpClockNumOfSA=_FsPtpClockNumOfSA_Object((1,3,6,1,4,1,10876,101,2,45,1,3,1,1,13),_FsPtpClockNumOfSA_Type())
fsPtpClockNumOfSA.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpClockNumOfSA.setStatus(_A)
_FsPtpCurrentDataSet_ObjectIdentity=ObjectIdentity
fsPtpCurrentDataSet=_FsPtpCurrentDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,4))
_FsPtpCurrentDataSetTable_Object=MibTable
fsPtpCurrentDataSetTable=_FsPtpCurrentDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1))
if mibBuilder.loadTexts:fsPtpCurrentDataSetTable.setStatus(_A)
_FsPtpCurrentDataSetEntry_Object=MibTableRow
fsPtpCurrentDataSetEntry=_FsPtpCurrentDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1,1))
if mibBuilder.loadTexts:fsPtpCurrentDataSetEntry.setStatus(_A)
_FsPtpCurrentStepsRemoved_Type=Integer32
_FsPtpCurrentStepsRemoved_Object=MibTableColumn
fsPtpCurrentStepsRemoved=_FsPtpCurrentStepsRemoved_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1,1,1),_FsPtpCurrentStepsRemoved_Type())
fsPtpCurrentStepsRemoved.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpCurrentStepsRemoved.setStatus(_A)
_FsPtpCurrentOffsetFromMaster_Type=DisplayString
_FsPtpCurrentOffsetFromMaster_Object=MibTableColumn
fsPtpCurrentOffsetFromMaster=_FsPtpCurrentOffsetFromMaster_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1,1,2),_FsPtpCurrentOffsetFromMaster_Type())
fsPtpCurrentOffsetFromMaster.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpCurrentOffsetFromMaster.setStatus(_A)
_FsPtpCurrentMeanPathDelay_Type=DisplayString
_FsPtpCurrentMeanPathDelay_Object=MibTableColumn
fsPtpCurrentMeanPathDelay=_FsPtpCurrentMeanPathDelay_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1,1,3),_FsPtpCurrentMeanPathDelay_Type())
fsPtpCurrentMeanPathDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpCurrentMeanPathDelay.setStatus(_A)
_FsPtpCurrentMasterToSlaveDelay_Type=DisplayString
_FsPtpCurrentMasterToSlaveDelay_Object=MibTableColumn
fsPtpCurrentMasterToSlaveDelay=_FsPtpCurrentMasterToSlaveDelay_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1,1,4),_FsPtpCurrentMasterToSlaveDelay_Type())
fsPtpCurrentMasterToSlaveDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpCurrentMasterToSlaveDelay.setStatus(_A)
_FsPtpCurrentSlaveToMasterDelay_Type=DisplayString
_FsPtpCurrentSlaveToMasterDelay_Object=MibTableColumn
fsPtpCurrentSlaveToMasterDelay=_FsPtpCurrentSlaveToMasterDelay_Object((1,3,6,1,4,1,10876,101,2,45,1,4,1,1,5),_FsPtpCurrentSlaveToMasterDelay_Type())
fsPtpCurrentSlaveToMasterDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpCurrentSlaveToMasterDelay.setStatus(_A)
_FsPtpParentDataSet_ObjectIdentity=ObjectIdentity
fsPtpParentDataSet=_FsPtpParentDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,5))
_FsPtpParentDataSetTable_Object=MibTable
fsPtpParentDataSetTable=_FsPtpParentDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1))
if mibBuilder.loadTexts:fsPtpParentDataSetTable.setStatus(_A)
_FsPtpParentDataSetEntry_Object=MibTableRow
fsPtpParentDataSetEntry=_FsPtpParentDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1))
if mibBuilder.loadTexts:fsPtpParentDataSetEntry.setStatus(_A)
class _FsPtpParentClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpParentClockIdentity_Type.__name__=_G
_FsPtpParentClockIdentity_Object=MibTableColumn
fsPtpParentClockIdentity=_FsPtpParentClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,1),_FsPtpParentClockIdentity_Type())
fsPtpParentClockIdentity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentClockIdentity.setStatus(_A)
_FsPtpParentPortNumber_Type=FsPtpPortNumber
_FsPtpParentPortNumber_Object=MibTableColumn
fsPtpParentPortNumber=_FsPtpParentPortNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,2),_FsPtpParentPortNumber_Type())
fsPtpParentPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentPortNumber.setStatus(_A)
class _FsPtpParentStats_Type(TruthValue):defaultValue=2
_FsPtpParentStats_Type.__name__=_H
_FsPtpParentStats_Object=MibTableColumn
fsPtpParentStats=_FsPtpParentStats_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,3),_FsPtpParentStats_Type())
fsPtpParentStats.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentStats.setStatus(_A)
class _FsPtpParentObservedOffsetScaledLogVariance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPtpParentObservedOffsetScaledLogVariance_Type.__name__=_D
_FsPtpParentObservedOffsetScaledLogVariance_Object=MibTableColumn
fsPtpParentObservedOffsetScaledLogVariance=_FsPtpParentObservedOffsetScaledLogVariance_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,4),_FsPtpParentObservedOffsetScaledLogVariance_Type())
fsPtpParentObservedOffsetScaledLogVariance.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentObservedOffsetScaledLogVariance.setStatus(_A)
_FsPtpParentObservedClockPhaseChangeRate_Type=Integer32
_FsPtpParentObservedClockPhaseChangeRate_Object=MibTableColumn
fsPtpParentObservedClockPhaseChangeRate=_FsPtpParentObservedClockPhaseChangeRate_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,5),_FsPtpParentObservedClockPhaseChangeRate_Type())
fsPtpParentObservedClockPhaseChangeRate.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentObservedClockPhaseChangeRate.setStatus(_A)
class _FsPtpParentGMClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpParentGMClockIdentity_Type.__name__=_G
_FsPtpParentGMClockIdentity_Object=MibTableColumn
fsPtpParentGMClockIdentity=_FsPtpParentGMClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,6),_FsPtpParentGMClockIdentity_Type())
fsPtpParentGMClockIdentity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentGMClockIdentity.setStatus(_A)
class _FsPtpParentGMClockClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpParentGMClockClass_Type.__name__=_D
_FsPtpParentGMClockClass_Object=MibTableColumn
fsPtpParentGMClockClass=_FsPtpParentGMClockClass_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,7),_FsPtpParentGMClockClass_Type())
fsPtpParentGMClockClass.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentGMClockClass.setStatus(_A)
class _FsPtpParentGMClockAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpParentGMClockAccuracy_Type.__name__=_D
_FsPtpParentGMClockAccuracy_Object=MibTableColumn
fsPtpParentGMClockAccuracy=_FsPtpParentGMClockAccuracy_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,8),_FsPtpParentGMClockAccuracy_Type())
fsPtpParentGMClockAccuracy.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentGMClockAccuracy.setStatus(_A)
class _FsPtpParentGMClockOffsetScaledLogVariance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPtpParentGMClockOffsetScaledLogVariance_Type.__name__=_D
_FsPtpParentGMClockOffsetScaledLogVariance_Object=MibTableColumn
fsPtpParentGMClockOffsetScaledLogVariance=_FsPtpParentGMClockOffsetScaledLogVariance_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,9),_FsPtpParentGMClockOffsetScaledLogVariance_Type())
fsPtpParentGMClockOffsetScaledLogVariance.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentGMClockOffsetScaledLogVariance.setStatus(_A)
class _FsPtpParentGMPriority1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpParentGMPriority1_Type.__name__=_D
_FsPtpParentGMPriority1_Object=MibTableColumn
fsPtpParentGMPriority1=_FsPtpParentGMPriority1_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,10),_FsPtpParentGMPriority1_Type())
fsPtpParentGMPriority1.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentGMPriority1.setStatus(_A)
class _FsPtpParentGMPriority2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpParentGMPriority2_Type.__name__=_D
_FsPtpParentGMPriority2_Object=MibTableColumn
fsPtpParentGMPriority2=_FsPtpParentGMPriority2_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,11),_FsPtpParentGMPriority2_Type())
fsPtpParentGMPriority2.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentGMPriority2.setStatus(_A)
_FsPtpParentClockObservedDrift_Type=Integer32
_FsPtpParentClockObservedDrift_Object=MibTableColumn
fsPtpParentClockObservedDrift=_FsPtpParentClockObservedDrift_Object((1,3,6,1,4,1,10876,101,2,45,1,5,1,1,12),_FsPtpParentClockObservedDrift_Type())
fsPtpParentClockObservedDrift.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpParentClockObservedDrift.setStatus(_A)
_FsPtpGlobalTimeProportiesDataSet_ObjectIdentity=ObjectIdentity
fsPtpGlobalTimeProportiesDataSet=_FsPtpGlobalTimeProportiesDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,6))
_FsPtpTimeDataSetTable_Object=MibTable
fsPtpTimeDataSetTable=_FsPtpTimeDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1))
if mibBuilder.loadTexts:fsPtpTimeDataSetTable.setStatus(_A)
_FsPtpTimeDataSetEntry_Object=MibTableRow
fsPtpTimeDataSetEntry=_FsPtpTimeDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1))
if mibBuilder.loadTexts:fsPtpTimeDataSetEntry.setStatus(_A)
class _FsPtpTimeCurrentUTCOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPtpTimeCurrentUTCOffset_Type.__name__=_D
_FsPtpTimeCurrentUTCOffset_Object=MibTableColumn
fsPtpTimeCurrentUTCOffset=_FsPtpTimeCurrentUTCOffset_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,1),_FsPtpTimeCurrentUTCOffset_Type())
fsPtpTimeCurrentUTCOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeCurrentUTCOffset.setStatus(_A)
_FsPtpTimeCurrentUTCOffsetValid_Type=TruthValue
_FsPtpTimeCurrentUTCOffsetValid_Object=MibTableColumn
fsPtpTimeCurrentUTCOffsetValid=_FsPtpTimeCurrentUTCOffsetValid_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,2),_FsPtpTimeCurrentUTCOffsetValid_Type())
fsPtpTimeCurrentUTCOffsetValid.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeCurrentUTCOffsetValid.setStatus(_A)
_FsPtpTimeLeap59_Type=TruthValue
_FsPtpTimeLeap59_Object=MibTableColumn
fsPtpTimeLeap59=_FsPtpTimeLeap59_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,3),_FsPtpTimeLeap59_Type())
fsPtpTimeLeap59.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeLeap59.setStatus(_A)
_FsPtpTimeLeap61_Type=TruthValue
_FsPtpTimeLeap61_Object=MibTableColumn
fsPtpTimeLeap61=_FsPtpTimeLeap61_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,4),_FsPtpTimeLeap61_Type())
fsPtpTimeLeap61.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeLeap61.setStatus(_A)
_FsPtpTimeTimeTraceable_Type=TruthValue
_FsPtpTimeTimeTraceable_Object=MibTableColumn
fsPtpTimeTimeTraceable=_FsPtpTimeTimeTraceable_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,5),_FsPtpTimeTimeTraceable_Type())
fsPtpTimeTimeTraceable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeTimeTraceable.setStatus(_A)
_FsPtpTimeFrequencyTraceable_Type=TruthValue
_FsPtpTimeFrequencyTraceable_Object=MibTableColumn
fsPtpTimeFrequencyTraceable=_FsPtpTimeFrequencyTraceable_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,6),_FsPtpTimeFrequencyTraceable_Type())
fsPtpTimeFrequencyTraceable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeFrequencyTraceable.setStatus(_A)
class _FsPtpTimeTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,48,64,80,96,144,160,255)));namedValues=NamedValues(*(('atomicclock',16),('gps',32),('terrestrialradio',48),('ptp',64),('ntp',80),('handset',96),('other',144),('internaloscillator',160),('reserved',255)))
_FsPtpTimeTimeSource_Type.__name__=_D
_FsPtpTimeTimeSource_Object=MibTableColumn
fsPtpTimeTimeSource=_FsPtpTimeTimeSource_Object((1,3,6,1,4,1,10876,101,2,45,1,6,1,1,7),_FsPtpTimeTimeSource_Type())
fsPtpTimeTimeSource.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTimeTimeSource.setStatus(_A)
_FsPtpPortConfigurationDataSet_ObjectIdentity=ObjectIdentity
fsPtpPortConfigurationDataSet=_FsPtpPortConfigurationDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,7))
_FsPtpPortConfigDataSetTable_Object=MibTable
fsPtpPortConfigDataSetTable=_FsPtpPortConfigDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1))
if mibBuilder.loadTexts:fsPtpPortConfigDataSetTable.setStatus(_A)
_FsPtpPortConfigDataSetEntry_Object=MibTableRow
fsPtpPortConfigDataSetEntry=_FsPtpPortConfigDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1))
fsPtpPortConfigDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_O))
if mibBuilder.loadTexts:fsPtpPortConfigDataSetEntry.setStatus(_A)
class _FsPtpPortIndex_Type(FsPtpPortNumber):subtypeSpec=FsPtpPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsPtpPortIndex_Type.__name__=_P
_FsPtpPortIndex_Object=MibTableColumn
fsPtpPortIndex=_FsPtpPortIndex_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,1),_FsPtpPortIndex_Type())
fsPtpPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpPortIndex.setStatus(_A)
class _FsPtpPortClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpPortClockIdentity_Type.__name__=_G
_FsPtpPortClockIdentity_Object=MibTableColumn
fsPtpPortClockIdentity=_FsPtpPortClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,2),_FsPtpPortClockIdentity_Type())
fsPtpPortClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortClockIdentity.setStatus(_A)
class _FsPtpPortInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,65534)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,65534)))
_FsPtpPortInterfaceType_Type.__name__=_D
_FsPtpPortInterfaceType_Object=MibTableColumn
fsPtpPortInterfaceType=_FsPtpPortInterfaceType_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,3),_FsPtpPortInterfaceType_Type())
fsPtpPortInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortInterfaceType.setStatus(_A)
_FsPtpPortIfaceNumber_Type=Integer32
_FsPtpPortIfaceNumber_Object=MibTableColumn
fsPtpPortIfaceNumber=_FsPtpPortIfaceNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,4),_FsPtpPortIfaceNumber_Type())
fsPtpPortIfaceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortIfaceNumber.setStatus(_A)
class _FsPtpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('faulty',0),(_R,1),('initializing',2),('listening',3),('uncalibrated',4),('slave',5),('premaster',6),('master',7),('passive',8)))
_FsPtpPortState_Type.__name__=_D
_FsPtpPortState_Object=MibTableColumn
fsPtpPortState=_FsPtpPortState_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,5),_FsPtpPortState_Type())
fsPtpPortState.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortState.setStatus(_A)
class _FsPtpPortMinDelayReqInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsPtpPortMinDelayReqInterval_Type.__name__=_D
_FsPtpPortMinDelayReqInterval_Object=MibTableColumn
fsPtpPortMinDelayReqInterval=_FsPtpPortMinDelayReqInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,6),_FsPtpPortMinDelayReqInterval_Type())
fsPtpPortMinDelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortMinDelayReqInterval.setStatus(_A)
_FsPtpPortPeerMeanPathDelay_Type=DisplayString
_FsPtpPortPeerMeanPathDelay_Object=MibTableColumn
fsPtpPortPeerMeanPathDelay=_FsPtpPortPeerMeanPathDelay_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,7),_FsPtpPortPeerMeanPathDelay_Type())
fsPtpPortPeerMeanPathDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortPeerMeanPathDelay.setStatus(_A)
class _FsPtpPortAnnounceInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_FsPtpPortAnnounceInterval_Type.__name__=_D
_FsPtpPortAnnounceInterval_Object=MibTableColumn
fsPtpPortAnnounceInterval=_FsPtpPortAnnounceInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,8),_FsPtpPortAnnounceInterval_Type())
fsPtpPortAnnounceInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortAnnounceInterval.setStatus(_A)
class _FsPtpPortAnnounceReceiptTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_FsPtpPortAnnounceReceiptTimeout_Type.__name__=_D
_FsPtpPortAnnounceReceiptTimeout_Object=MibTableColumn
fsPtpPortAnnounceReceiptTimeout=_FsPtpPortAnnounceReceiptTimeout_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,9),_FsPtpPortAnnounceReceiptTimeout_Type())
fsPtpPortAnnounceReceiptTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortAnnounceReceiptTimeout.setStatus(_A)
class _FsPtpPortSyncInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_FsPtpPortSyncInterval_Type.__name__=_D
_FsPtpPortSyncInterval_Object=MibTableColumn
fsPtpPortSyncInterval=_FsPtpPortSyncInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,10),_FsPtpPortSyncInterval_Type())
fsPtpPortSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortSyncInterval.setStatus(_A)
class _FsPtpPortSynclimit_Type(DisplayString):defaultValue=OctetString('1000000000')
_FsPtpPortSynclimit_Type.__name__=_M
_FsPtpPortSynclimit_Object=MibTableColumn
fsPtpPortSynclimit=_FsPtpPortSynclimit_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,11),_FsPtpPortSynclimit_Type())
fsPtpPortSynclimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortSynclimit.setStatus(_A)
class _FsPtpPortDelayMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_c,1),(_d,2),(_R,255)))
_FsPtpPortDelayMechanism_Type.__name__=_D
_FsPtpPortDelayMechanism_Object=MibTableColumn
fsPtpPortDelayMechanism=_FsPtpPortDelayMechanism_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,12),_FsPtpPortDelayMechanism_Type())
fsPtpPortDelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortDelayMechanism.setStatus(_A)
class _FsPtpPortMinPdelayReqInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsPtpPortMinPdelayReqInterval_Type.__name__=_D
_FsPtpPortMinPdelayReqInterval_Object=MibTableColumn
fsPtpPortMinPdelayReqInterval=_FsPtpPortMinPdelayReqInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,13),_FsPtpPortMinPdelayReqInterval_Type())
fsPtpPortMinPdelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortMinPdelayReqInterval.setStatus(_A)
class _FsPtpPortVersionNumber_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsPtpPortVersionNumber_Type.__name__=_D
_FsPtpPortVersionNumber_Object=MibTableColumn
fsPtpPortVersionNumber=_FsPtpPortVersionNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,14),_FsPtpPortVersionNumber_Type())
fsPtpPortVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortVersionNumber.setStatus(_A)
class _FsPtpPortUnicastNegOption_Type(TruthValue):defaultValue=2
_FsPtpPortUnicastNegOption_Type.__name__=_H
_FsPtpPortUnicastNegOption_Object=MibTableColumn
fsPtpPortUnicastNegOption=_FsPtpPortUnicastNegOption_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,15),_FsPtpPortUnicastNegOption_Type())
fsPtpPortUnicastNegOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortUnicastNegOption.setStatus(_A)
class _FsPtpPortUnicastMasterMaxSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPtpPortUnicastMasterMaxSize_Type.__name__=_D
_FsPtpPortUnicastMasterMaxSize_Object=MibTableColumn
fsPtpPortUnicastMasterMaxSize=_FsPtpPortUnicastMasterMaxSize_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,16),_FsPtpPortUnicastMasterMaxSize_Type())
fsPtpPortUnicastMasterMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortUnicastMasterMaxSize.setStatus(_A)
class _FsPtpPortAccMasterEnabled_Type(TruthValue):defaultValue=2
_FsPtpPortAccMasterEnabled_Type.__name__=_H
_FsPtpPortAccMasterEnabled_Object=MibTableColumn
fsPtpPortAccMasterEnabled=_FsPtpPortAccMasterEnabled_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,17),_FsPtpPortAccMasterEnabled_Type())
fsPtpPortAccMasterEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortAccMasterEnabled.setStatus(_A)
class _FsPtpPortNumOfAltMaster_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpPortNumOfAltMaster_Type.__name__=_D
_FsPtpPortNumOfAltMaster_Object=MibTableColumn
fsPtpPortNumOfAltMaster=_FsPtpPortNumOfAltMaster_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,18),_FsPtpPortNumOfAltMaster_Type())
fsPtpPortNumOfAltMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortNumOfAltMaster.setStatus(_A)
class _FsPtpPortAltMulcastSync_Type(TruthValue):defaultValue=2
_FsPtpPortAltMulcastSync_Type.__name__=_H
_FsPtpPortAltMulcastSync_Object=MibTableColumn
fsPtpPortAltMulcastSync=_FsPtpPortAltMulcastSync_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,19),_FsPtpPortAltMulcastSync_Type())
fsPtpPortAltMulcastSync.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortAltMulcastSync.setStatus(_A)
class _FsPtpPortAltMulcastSyncInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpPortAltMulcastSyncInterval_Type.__name__=_D
_FsPtpPortAltMulcastSyncInterval_Object=MibTableColumn
fsPtpPortAltMulcastSyncInterval=_FsPtpPortAltMulcastSyncInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,20),_FsPtpPortAltMulcastSyncInterval_Type())
fsPtpPortAltMulcastSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortAltMulcastSyncInterval.setStatus(_A)
class _FsPtpPortPtpStatus_Type(TruthValue):defaultValue=2
_FsPtpPortPtpStatus_Type.__name__=_H
_FsPtpPortPtpStatus_Object=MibTableColumn
fsPtpPortPtpStatus=_FsPtpPortPtpStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,21),_FsPtpPortPtpStatus_Type())
fsPtpPortPtpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpPortPtpStatus.setStatus(_A)
_FsPtpPortRcvdAnnounceMsgCnt_Type=Unsigned32
_FsPtpPortRcvdAnnounceMsgCnt_Object=MibTableColumn
fsPtpPortRcvdAnnounceMsgCnt=_FsPtpPortRcvdAnnounceMsgCnt_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,22),_FsPtpPortRcvdAnnounceMsgCnt_Type())
fsPtpPortRcvdAnnounceMsgCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortRcvdAnnounceMsgCnt.setStatus(_A)
_FsPtpPortRcvdSyncMsgCnt_Type=Unsigned32
_FsPtpPortRcvdSyncMsgCnt_Object=MibTableColumn
fsPtpPortRcvdSyncMsgCnt=_FsPtpPortRcvdSyncMsgCnt_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,23),_FsPtpPortRcvdSyncMsgCnt_Type())
fsPtpPortRcvdSyncMsgCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortRcvdSyncMsgCnt.setStatus(_A)
_FsPtpPortRcvdDelayReqMsgCnt_Type=Unsigned32
_FsPtpPortRcvdDelayReqMsgCnt_Object=MibTableColumn
fsPtpPortRcvdDelayReqMsgCnt=_FsPtpPortRcvdDelayReqMsgCnt_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,24),_FsPtpPortRcvdDelayReqMsgCnt_Type())
fsPtpPortRcvdDelayReqMsgCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortRcvdDelayReqMsgCnt.setStatus(_A)
_FsPtpPortRcvdDelayRespMsgCnt_Type=Unsigned32
_FsPtpPortRcvdDelayRespMsgCnt_Object=MibTableColumn
fsPtpPortRcvdDelayRespMsgCnt=_FsPtpPortRcvdDelayRespMsgCnt_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,25),_FsPtpPortRcvdDelayRespMsgCnt_Type())
fsPtpPortRcvdDelayRespMsgCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortRcvdDelayRespMsgCnt.setStatus(_A)
_FsPtpPortTransDelayReqMsgCnt_Type=Unsigned32
_FsPtpPortTransDelayReqMsgCnt_Object=MibTableColumn
fsPtpPortTransDelayReqMsgCnt=_FsPtpPortTransDelayReqMsgCnt_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,26),_FsPtpPortTransDelayReqMsgCnt_Type())
fsPtpPortTransDelayReqMsgCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortTransDelayReqMsgCnt.setStatus(_A)
_FsPtpPortDiscardedMsgCnt_Type=Unsigned32
_FsPtpPortDiscardedMsgCnt_Object=MibTableColumn
fsPtpPortDiscardedMsgCnt=_FsPtpPortDiscardedMsgCnt_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,27),_FsPtpPortDiscardedMsgCnt_Type())
fsPtpPortDiscardedMsgCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpPortDiscardedMsgCnt.setStatus(_A)
_FsPtpPortRowStatus_Type=RowStatus
_FsPtpPortRowStatus_Object=MibTableColumn
fsPtpPortRowStatus=_FsPtpPortRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,7,1,1,28),_FsPtpPortRowStatus_Type())
fsPtpPortRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsPtpPortRowStatus.setStatus(_A)
_FsPtpForeignMasterDataSet_ObjectIdentity=ObjectIdentity
fsPtpForeignMasterDataSet=_FsPtpForeignMasterDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,8))
_FsPtpForeignMasterDataSetTable_Object=MibTable
fsPtpForeignMasterDataSetTable=_FsPtpForeignMasterDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,8,1))
if mibBuilder.loadTexts:fsPtpForeignMasterDataSetTable.setStatus(_A)
_FsPtpForeignMasterDataSetEntry_Object=MibTableRow
fsPtpForeignMasterDataSetEntry=_FsPtpForeignMasterDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,8,1,1))
fsPtpForeignMasterDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_e),(0,_C,_f),(0,_C,_O))
if mibBuilder.loadTexts:fsPtpForeignMasterDataSetEntry.setStatus(_A)
class _FsPtpForeignMasterClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpForeignMasterClockIdentity_Type.__name__=_G
_FsPtpForeignMasterClockIdentity_Object=MibTableColumn
fsPtpForeignMasterClockIdentity=_FsPtpForeignMasterClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,8,1,1,1),_FsPtpForeignMasterClockIdentity_Type())
fsPtpForeignMasterClockIdentity.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpForeignMasterClockIdentity.setStatus(_A)
class _FsPtpForeignMasterPortIndex_Type(FsPtpPortNumber):subtypeSpec=FsPtpPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsPtpForeignMasterPortIndex_Type.__name__=_P
_FsPtpForeignMasterPortIndex_Object=MibTableColumn
fsPtpForeignMasterPortIndex=_FsPtpForeignMasterPortIndex_Object((1,3,6,1,4,1,10876,101,2,45,1,8,1,1,2),_FsPtpForeignMasterPortIndex_Type())
fsPtpForeignMasterPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpForeignMasterPortIndex.setStatus(_A)
_FsPtpForeignMasterAnnounceMsgs_Type=Integer32
_FsPtpForeignMasterAnnounceMsgs_Object=MibTableColumn
fsPtpForeignMasterAnnounceMsgs=_FsPtpForeignMasterAnnounceMsgs_Object((1,3,6,1,4,1,10876,101,2,45,1,8,1,1,3),_FsPtpForeignMasterAnnounceMsgs_Type())
fsPtpForeignMasterAnnounceMsgs.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpForeignMasterAnnounceMsgs.setStatus(_A)
_FsPtpTransparentDataSet_ObjectIdentity=ObjectIdentity
fsPtpTransparentDataSet=_FsPtpTransparentDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,9))
_FsPtpTransparentDataSetTable_Object=MibTable
fsPtpTransparentDataSetTable=_FsPtpTransparentDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1))
if mibBuilder.loadTexts:fsPtpTransparentDataSetTable.setStatus(_A)
_FsPtpTransparentDataSetEntry_Object=MibTableRow
fsPtpTransparentDataSetEntry=_FsPtpTransparentDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1,1))
if mibBuilder.loadTexts:fsPtpTransparentDataSetEntry.setStatus(_A)
class _FsPtpTransparentClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpTransparentClockIdentity_Type.__name__=_G
_FsPtpTransparentClockIdentity_Object=MibTableColumn
fsPtpTransparentClockIdentity=_FsPtpTransparentClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1,1,1),_FsPtpTransparentClockIdentity_Type())
fsPtpTransparentClockIdentity.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTransparentClockIdentity.setStatus(_A)
class _FsPtpTransparentClockTwoStepFlag_Type(TruthValue):defaultValue=2
_FsPtpTransparentClockTwoStepFlag_Type.__name__=_H
_FsPtpTransparentClockTwoStepFlag_Object=MibTableColumn
fsPtpTransparentClockTwoStepFlag=_FsPtpTransparentClockTwoStepFlag_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1,1,2),_FsPtpTransparentClockTwoStepFlag_Type())
fsPtpTransparentClockTwoStepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentClockTwoStepFlag.setStatus(_A)
class _FsPtpTransparentClockNumberPorts_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsPtpTransparentClockNumberPorts_Type.__name__=_D
_FsPtpTransparentClockNumberPorts_Object=MibTableColumn
fsPtpTransparentClockNumberPorts=_FsPtpTransparentClockNumberPorts_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1,1,3),_FsPtpTransparentClockNumberPorts_Type())
fsPtpTransparentClockNumberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentClockNumberPorts.setStatus(_A)
class _FsPtpTransparentClockDelaymechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_FsPtpTransparentClockDelaymechanism_Type.__name__=_D
_FsPtpTransparentClockDelaymechanism_Object=MibTableColumn
fsPtpTransparentClockDelaymechanism=_FsPtpTransparentClockDelaymechanism_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1,1,4),_FsPtpTransparentClockDelaymechanism_Type())
fsPtpTransparentClockDelaymechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentClockDelaymechanism.setStatus(_A)
class _FsPtpTransparentClockPrimaryDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpTransparentClockPrimaryDomain_Type.__name__=_D
_FsPtpTransparentClockPrimaryDomain_Object=MibTableColumn
fsPtpTransparentClockPrimaryDomain=_FsPtpTransparentClockPrimaryDomain_Object((1,3,6,1,4,1,10876,101,2,45,1,9,1,1,5),_FsPtpTransparentClockPrimaryDomain_Type())
fsPtpTransparentClockPrimaryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentClockPrimaryDomain.setStatus(_A)
_FsPtpTransparentPortDataSet_ObjectIdentity=ObjectIdentity
fsPtpTransparentPortDataSet=_FsPtpTransparentPortDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,10))
_FsPtpTransparentPortDataSetTable_Object=MibTable
fsPtpTransparentPortDataSetTable=_FsPtpTransparentPortDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1))
if mibBuilder.loadTexts:fsPtpTransparentPortDataSetTable.setStatus(_A)
_FsPtpTransparentPortDataSetEntry_Object=MibTableRow
fsPtpTransparentPortDataSetEntry=_FsPtpTransparentPortDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1))
fsPtpTransparentPortDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_g))
if mibBuilder.loadTexts:fsPtpTransparentPortDataSetEntry.setStatus(_A)
class _FsPtpTransparentPortIndex_Type(FsPtpPortNumber):subtypeSpec=FsPtpPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsPtpTransparentPortIndex_Type.__name__=_P
_FsPtpTransparentPortIndex_Object=MibTableColumn
fsPtpTransparentPortIndex=_FsPtpTransparentPortIndex_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,1),_FsPtpTransparentPortIndex_Type())
fsPtpTransparentPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpTransparentPortIndex.setStatus(_A)
class _FsPtpTransparentPortInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,65534)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,65534)))
_FsPtpTransparentPortInterfaceType_Type.__name__=_D
_FsPtpTransparentPortInterfaceType_Object=MibTableColumn
fsPtpTransparentPortInterfaceType=_FsPtpTransparentPortInterfaceType_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,2),_FsPtpTransparentPortInterfaceType_Type())
fsPtpTransparentPortInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentPortInterfaceType.setStatus(_A)
_FsPtpTransparentPortIfaceNumber_Type=Integer32
_FsPtpTransparentPortIfaceNumber_Object=MibTableColumn
fsPtpTransparentPortIfaceNumber=_FsPtpTransparentPortIfaceNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,3),_FsPtpTransparentPortIfaceNumber_Type())
fsPtpTransparentPortIfaceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentPortIfaceNumber.setStatus(_A)
class _FsPtpTransparentPortClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpTransparentPortClockIdentity_Type.__name__=_G
_FsPtpTransparentPortClockIdentity_Object=MibTableColumn
fsPtpTransparentPortClockIdentity=_FsPtpTransparentPortClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,4),_FsPtpTransparentPortClockIdentity_Type())
fsPtpTransparentPortClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentPortClockIdentity.setStatus(_A)
class _FsPtpTransparentPortMinPdelayReqInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FsPtpTransparentPortMinPdelayReqInterval_Type.__name__=_D
_FsPtpTransparentPortMinPdelayReqInterval_Object=MibTableColumn
fsPtpTransparentPortMinPdelayReqInterval=_FsPtpTransparentPortMinPdelayReqInterval_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,5),_FsPtpTransparentPortMinPdelayReqInterval_Type())
fsPtpTransparentPortMinPdelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentPortMinPdelayReqInterval.setStatus(_A)
class _FsPtpTransparentPortFaultyFlag_Type(TruthValue):defaultValue=2
_FsPtpTransparentPortFaultyFlag_Type.__name__=_H
_FsPtpTransparentPortFaultyFlag_Object=MibTableColumn
fsPtpTransparentPortFaultyFlag=_FsPtpTransparentPortFaultyFlag_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,6),_FsPtpTransparentPortFaultyFlag_Type())
fsPtpTransparentPortFaultyFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTransparentPortFaultyFlag.setStatus(_A)
_FsPtpTransparentPortPeerMeanPathDelay_Type=DisplayString
_FsPtpTransparentPortPeerMeanPathDelay_Object=MibTableColumn
fsPtpTransparentPortPeerMeanPathDelay=_FsPtpTransparentPortPeerMeanPathDelay_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,7),_FsPtpTransparentPortPeerMeanPathDelay_Type())
fsPtpTransparentPortPeerMeanPathDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpTransparentPortPeerMeanPathDelay.setStatus(_A)
class _FsPtpTransparentPortPtpStatus_Type(TruthValue):defaultValue=2
_FsPtpTransparentPortPtpStatus_Type.__name__=_H
_FsPtpTransparentPortPtpStatus_Object=MibTableColumn
fsPtpTransparentPortPtpStatus=_FsPtpTransparentPortPtpStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,8),_FsPtpTransparentPortPtpStatus_Type())
fsPtpTransparentPortPtpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentPortPtpStatus.setStatus(_A)
_FsPtpTransparentPortRowStatus_Type=RowStatus
_FsPtpTransparentPortRowStatus_Object=MibTableColumn
fsPtpTransparentPortRowStatus=_FsPtpTransparentPortRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,10,1,1,9),_FsPtpTransparentPortRowStatus_Type())
fsPtpTransparentPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpTransparentPortRowStatus.setStatus(_A)
_FsPtpGrandMasterClusterDataSet_ObjectIdentity=ObjectIdentity
fsPtpGrandMasterClusterDataSet=_FsPtpGrandMasterClusterDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,11))
_FsPtpGrandMasterClusterDataSetTable_Object=MibTable
fsPtpGrandMasterClusterDataSetTable=_FsPtpGrandMasterClusterDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,11,1))
if mibBuilder.loadTexts:fsPtpGrandMasterClusterDataSetTable.setStatus(_A)
_FsPtpGrandMasterClusterDataSetEntry_Object=MibTableRow
fsPtpGrandMasterClusterDataSetEntry=_FsPtpGrandMasterClusterDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,11,1,1))
fsPtpGrandMasterClusterDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_h),(0,_C,_i),(0,_C,_j))
if mibBuilder.loadTexts:fsPtpGrandMasterClusterDataSetEntry.setStatus(_A)
class _FsPtpGrandMasterClusterNetworkProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpGrandMasterClusterNetworkProtocol_Type.__name__=_D
_FsPtpGrandMasterClusterNetworkProtocol_Object=MibTableColumn
fsPtpGrandMasterClusterNetworkProtocol=_FsPtpGrandMasterClusterNetworkProtocol_Object((1,3,6,1,4,1,10876,101,2,45,1,11,1,1,1),_FsPtpGrandMasterClusterNetworkProtocol_Type())
fsPtpGrandMasterClusterNetworkProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpGrandMasterClusterNetworkProtocol.setStatus(_A)
class _FsPtpGrandMasterClusterAddLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsPtpGrandMasterClusterAddLength_Type.__name__=_D
_FsPtpGrandMasterClusterAddLength_Object=MibTableColumn
fsPtpGrandMasterClusterAddLength=_FsPtpGrandMasterClusterAddLength_Object((1,3,6,1,4,1,10876,101,2,45,1,11,1,1,2),_FsPtpGrandMasterClusterAddLength_Type())
fsPtpGrandMasterClusterAddLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpGrandMasterClusterAddLength.setStatus(_A)
class _FsPtpGrandMasterClusterAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsPtpGrandMasterClusterAddr_Type.__name__=_G
_FsPtpGrandMasterClusterAddr_Object=MibTableColumn
fsPtpGrandMasterClusterAddr=_FsPtpGrandMasterClusterAddr_Object((1,3,6,1,4,1,10876,101,2,45,1,11,1,1,3),_FsPtpGrandMasterClusterAddr_Type())
fsPtpGrandMasterClusterAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpGrandMasterClusterAddr.setStatus(_A)
_FsPtpGrandMasterClusterRowStatus_Type=RowStatus
_FsPtpGrandMasterClusterRowStatus_Object=MibTableColumn
fsPtpGrandMasterClusterRowStatus=_FsPtpGrandMasterClusterRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,11,1,1,4),_FsPtpGrandMasterClusterRowStatus_Type())
fsPtpGrandMasterClusterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpGrandMasterClusterRowStatus.setStatus(_A)
_FsPtpUnicastMasterDataSet_ObjectIdentity=ObjectIdentity
fsPtpUnicastMasterDataSet=_FsPtpUnicastMasterDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,12))
_FsPtpUnicastMasterDataSetTable_Object=MibTable
fsPtpUnicastMasterDataSetTable=_FsPtpUnicastMasterDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,12,1))
if mibBuilder.loadTexts:fsPtpUnicastMasterDataSetTable.setStatus(_A)
_FsPtpUnicastMasterDataSetEntry_Object=MibTableRow
fsPtpUnicastMasterDataSetEntry=_FsPtpUnicastMasterDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,12,1,1))
fsPtpUnicastMasterDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_O),(0,_C,_k),(0,_C,_l),(0,_C,_m))
if mibBuilder.loadTexts:fsPtpUnicastMasterDataSetEntry.setStatus(_A)
class _FsPtpUnicastMasterNetworkProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpUnicastMasterNetworkProtocol_Type.__name__=_D
_FsPtpUnicastMasterNetworkProtocol_Object=MibTableColumn
fsPtpUnicastMasterNetworkProtocol=_FsPtpUnicastMasterNetworkProtocol_Object((1,3,6,1,4,1,10876,101,2,45,1,12,1,1,1),_FsPtpUnicastMasterNetworkProtocol_Type())
fsPtpUnicastMasterNetworkProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpUnicastMasterNetworkProtocol.setStatus(_A)
class _FsPtpUnicastMasterAddLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsPtpUnicastMasterAddLength_Type.__name__=_D
_FsPtpUnicastMasterAddLength_Object=MibTableColumn
fsPtpUnicastMasterAddLength=_FsPtpUnicastMasterAddLength_Object((1,3,6,1,4,1,10876,101,2,45,1,12,1,1,2),_FsPtpUnicastMasterAddLength_Type())
fsPtpUnicastMasterAddLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpUnicastMasterAddLength.setStatus(_A)
class _FsPtpUnicastMasterAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsPtpUnicastMasterAddr_Type.__name__=_G
_FsPtpUnicastMasterAddr_Object=MibTableColumn
fsPtpUnicastMasterAddr=_FsPtpUnicastMasterAddr_Object((1,3,6,1,4,1,10876,101,2,45,1,12,1,1,3),_FsPtpUnicastMasterAddr_Type())
fsPtpUnicastMasterAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpUnicastMasterAddr.setStatus(_A)
_FsPtpUnicastMasterRowStatus_Type=RowStatus
_FsPtpUnicastMasterRowStatus_Object=MibTableColumn
fsPtpUnicastMasterRowStatus=_FsPtpUnicastMasterRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,12,1,1,4),_FsPtpUnicastMasterRowStatus_Type())
fsPtpUnicastMasterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpUnicastMasterRowStatus.setStatus(_A)
_FsPtpAccMasterDataSet_ObjectIdentity=ObjectIdentity
fsPtpAccMasterDataSet=_FsPtpAccMasterDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,13))
_FsPtpAccMasterDataSetTable_Object=MibTable
fsPtpAccMasterDataSetTable=_FsPtpAccMasterDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1))
if mibBuilder.loadTexts:fsPtpAccMasterDataSetTable.setStatus(_A)
_FsPtpAccMasterDataSetEntry_Object=MibTableRow
fsPtpAccMasterDataSetEntry=_FsPtpAccMasterDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1,1))
fsPtpAccMasterDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_n),(0,_C,_o),(0,_C,_p))
if mibBuilder.loadTexts:fsPtpAccMasterDataSetEntry.setStatus(_A)
class _FsPtpAccMasterNetworkProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpAccMasterNetworkProtocol_Type.__name__=_D
_FsPtpAccMasterNetworkProtocol_Object=MibTableColumn
fsPtpAccMasterNetworkProtocol=_FsPtpAccMasterNetworkProtocol_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1,1,1),_FsPtpAccMasterNetworkProtocol_Type())
fsPtpAccMasterNetworkProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpAccMasterNetworkProtocol.setStatus(_A)
class _FsPtpAccMasterAddLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsPtpAccMasterAddLength_Type.__name__=_D
_FsPtpAccMasterAddLength_Object=MibTableColumn
fsPtpAccMasterAddLength=_FsPtpAccMasterAddLength_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1,1,2),_FsPtpAccMasterAddLength_Type())
fsPtpAccMasterAddLength.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpAccMasterAddLength.setStatus(_A)
class _FsPtpAccMasterAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_FsPtpAccMasterAddr_Type.__name__=_G
_FsPtpAccMasterAddr_Object=MibTableColumn
fsPtpAccMasterAddr=_FsPtpAccMasterAddr_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1,1,3),_FsPtpAccMasterAddr_Type())
fsPtpAccMasterAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpAccMasterAddr.setStatus(_A)
_FsPtpAccMasterAlternatePriority_Type=Integer32
_FsPtpAccMasterAlternatePriority_Object=MibTableColumn
fsPtpAccMasterAlternatePriority=_FsPtpAccMasterAlternatePriority_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1,1,4),_FsPtpAccMasterAlternatePriority_Type())
fsPtpAccMasterAlternatePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAccMasterAlternatePriority.setStatus(_A)
_FsPtpAccMasterRowStatus_Type=RowStatus
_FsPtpAccMasterRowStatus_Object=MibTableColumn
fsPtpAccMasterRowStatus=_FsPtpAccMasterRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,13,1,1,5),_FsPtpAccMasterRowStatus_Type())
fsPtpAccMasterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAccMasterRowStatus.setStatus(_A)
_FsPtpSecKeyDataSet_ObjectIdentity=ObjectIdentity
fsPtpSecKeyDataSet=_FsPtpSecKeyDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,14))
_FsPtpSecKeyDataSetTable_Object=MibTable
fsPtpSecKeyDataSetTable=_FsPtpSecKeyDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1))
if mibBuilder.loadTexts:fsPtpSecKeyDataSetTable.setStatus(_A)
_FsPtpSecKeyDataSetEntry_Object=MibTableRow
fsPtpSecKeyDataSetEntry=_FsPtpSecKeyDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1))
fsPtpSecKeyDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_q))
if mibBuilder.loadTexts:fsPtpSecKeyDataSetEntry.setStatus(_A)
class _FsPtpSecKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpSecKeyId_Type.__name__=_D
_FsPtpSecKeyId_Object=MibTableColumn
fsPtpSecKeyId=_FsPtpSecKeyId_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,1),_FsPtpSecKeyId_Type())
fsPtpSecKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpSecKeyId.setStatus(_A)
class _FsPtpSecKeyAlgorithmId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hmacSha196',1),('hmacSha256128',2)))
_FsPtpSecKeyAlgorithmId_Type.__name__=_D
_FsPtpSecKeyAlgorithmId_Object=MibTableColumn
fsPtpSecKeyAlgorithmId=_FsPtpSecKeyAlgorithmId_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,2),_FsPtpSecKeyAlgorithmId_Type())
fsPtpSecKeyAlgorithmId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSecKeyAlgorithmId.setStatus(_A)
_FsPtpSecKeyLength_Type=Integer32
_FsPtpSecKeyLength_Object=MibTableColumn
fsPtpSecKeyLength=_FsPtpSecKeyLength_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,3),_FsPtpSecKeyLength_Type())
fsPtpSecKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSecKeyLength.setStatus(_A)
_FsPtpSecKey_Type=OctetString
_FsPtpSecKey_Object=MibTableColumn
fsPtpSecKey=_FsPtpSecKey_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,4),_FsPtpSecKey_Type())
fsPtpSecKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSecKey.setStatus(_A)
_FsPtpSecKeyStartTime_Type=TimeStamp
_FsPtpSecKeyStartTime_Object=MibTableColumn
fsPtpSecKeyStartTime=_FsPtpSecKeyStartTime_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,5),_FsPtpSecKeyStartTime_Type())
fsPtpSecKeyStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSecKeyStartTime.setStatus(_A)
_FsPtpSecKeyExpirationTime_Type=TimeStamp
_FsPtpSecKeyExpirationTime_Object=MibTableColumn
fsPtpSecKeyExpirationTime=_FsPtpSecKeyExpirationTime_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,6),_FsPtpSecKeyExpirationTime_Type())
fsPtpSecKeyExpirationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSecKeyExpirationTime.setStatus(_A)
class _FsPtpSecKeyValid_Type(TruthValue):defaultValue=2
_FsPtpSecKeyValid_Type.__name__=_H
_FsPtpSecKeyValid_Object=MibTableColumn
fsPtpSecKeyValid=_FsPtpSecKeyValid_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,7),_FsPtpSecKeyValid_Type())
fsPtpSecKeyValid.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSecKeyValid.setStatus(_A)
_FsPtpSecKeyRowStatus_Type=RowStatus
_FsPtpSecKeyRowStatus_Object=MibTableColumn
fsPtpSecKeyRowStatus=_FsPtpSecKeyRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,14,1,1,8),_FsPtpSecKeyRowStatus_Type())
fsPtpSecKeyRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsPtpSecKeyRowStatus.setStatus(_A)
_FsPtpSADataSet_ObjectIdentity=ObjectIdentity
fsPtpSADataSet=_FsPtpSADataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,15))
_FsPtpSADataSetTable_Object=MibTable
fsPtpSADataSetTable=_FsPtpSADataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1))
if mibBuilder.loadTexts:fsPtpSADataSetTable.setStatus(_A)
_FsPtpSADataSetEntry_Object=MibTableRow
fsPtpSADataSetEntry=_FsPtpSADataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1))
fsPtpSADataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_r))
if mibBuilder.loadTexts:fsPtpSADataSetEntry.setStatus(_A)
class _FsPtpSAId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPtpSAId_Type.__name__=_D
_FsPtpSAId_Object=MibTableColumn
fsPtpSAId=_FsPtpSAId_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,1),_FsPtpSAId_Type())
fsPtpSAId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpSAId.setStatus(_A)
_FsPtpSASrcPortNumber_Type=FsPtpPortNumber
_FsPtpSASrcPortNumber_Object=MibTableColumn
fsPtpSASrcPortNumber=_FsPtpSASrcPortNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,2),_FsPtpSASrcPortNumber_Type())
fsPtpSASrcPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSASrcPortNumber.setStatus(_A)
_FsPtpSASrcAddrLength_Type=Integer32
_FsPtpSASrcAddrLength_Object=MibTableColumn
fsPtpSASrcAddrLength=_FsPtpSASrcAddrLength_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,3),_FsPtpSASrcAddrLength_Type())
fsPtpSASrcAddrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSASrcAddrLength.setStatus(_A)
_FsPtpSASrcAddr_Type=OctetString
_FsPtpSASrcAddr_Object=MibTableColumn
fsPtpSASrcAddr=_FsPtpSASrcAddr_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,4),_FsPtpSASrcAddr_Type())
fsPtpSASrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSASrcAddr.setStatus(_A)
_FsPtpSADstPortNumber_Type=FsPtpPortNumber
_FsPtpSADstPortNumber_Object=MibTableColumn
fsPtpSADstPortNumber=_FsPtpSADstPortNumber_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,5),_FsPtpSADstPortNumber_Type())
fsPtpSADstPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSADstPortNumber.setStatus(_A)
_FsPtpSADstAddrLength_Type=Integer32
_FsPtpSADstAddrLength_Object=MibTableColumn
fsPtpSADstAddrLength=_FsPtpSADstAddrLength_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,6),_FsPtpSADstAddrLength_Type())
fsPtpSADstAddrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSADstAddrLength.setStatus(_A)
_FsPtpSADstAddr_Type=OctetString
_FsPtpSADstAddr_Object=MibTableColumn
fsPtpSADstAddr=_FsPtpSADstAddr_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,7),_FsPtpSADstAddr_Type())
fsPtpSADstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSADstAddr.setStatus(_A)
class _FsPtpSASrcClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpSASrcClockIdentity_Type.__name__=_G
_FsPtpSASrcClockIdentity_Object=MibTableColumn
fsPtpSASrcClockIdentity=_FsPtpSASrcClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,8),_FsPtpSASrcClockIdentity_Type())
fsPtpSASrcClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSASrcClockIdentity.setStatus(_A)
class _FsPtpSADstClockIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FsPtpSADstClockIdentity_Type.__name__=_G
_FsPtpSADstClockIdentity_Object=MibTableColumn
fsPtpSADstClockIdentity=_FsPtpSADstClockIdentity_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,9),_FsPtpSADstClockIdentity_Type())
fsPtpSADstClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSADstClockIdentity.setStatus(_A)
_FsPtpSAReplayCounter_Type=Integer32
_FsPtpSAReplayCounter_Object=MibTableColumn
fsPtpSAReplayCounter=_FsPtpSAReplayCounter_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,10),_FsPtpSAReplayCounter_Type())
fsPtpSAReplayCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSAReplayCounter.setStatus(_A)
_FsPtpSALifeTimeId_Type=Integer32
_FsPtpSALifeTimeId_Object=MibTableColumn
fsPtpSALifeTimeId=_FsPtpSALifeTimeId_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,11),_FsPtpSALifeTimeId_Type())
fsPtpSALifeTimeId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSALifeTimeId.setStatus(_A)
_FsPtpSAKeyId_Type=Integer32
_FsPtpSAKeyId_Object=MibTableColumn
fsPtpSAKeyId=_FsPtpSAKeyId_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,12),_FsPtpSAKeyId_Type())
fsPtpSAKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSAKeyId.setStatus(_A)
_FsPtpSANextLifeTimeId_Type=Integer32
_FsPtpSANextLifeTimeId_Object=MibTableColumn
fsPtpSANextLifeTimeId=_FsPtpSANextLifeTimeId_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,13),_FsPtpSANextLifeTimeId_Type())
fsPtpSANextLifeTimeId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSANextLifeTimeId.setStatus(_A)
_FsPtpSANextKeyId_Type=Integer32
_FsPtpSANextKeyId_Object=MibTableColumn
fsPtpSANextKeyId=_FsPtpSANextKeyId_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,14),_FsPtpSANextKeyId_Type())
fsPtpSANextKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSANextKeyId.setStatus(_A)
class _FsPtpSATrustState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_FsPtpSATrustState_Type.__name__=_D
_FsPtpSATrustState_Object=MibTableColumn
fsPtpSATrustState=_FsPtpSATrustState_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,15),_FsPtpSATrustState_Type())
fsPtpSATrustState.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSATrustState.setStatus(_A)
_FsPtpSATrustTimer_Type=Integer32
_FsPtpSATrustTimer_Object=MibTableColumn
fsPtpSATrustTimer=_FsPtpSATrustTimer_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,16),_FsPtpSATrustTimer_Type())
fsPtpSATrustTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSATrustTimer.setStatus(_A)
_FsPtpSATrustTimeout_Type=Integer32
_FsPtpSATrustTimeout_Object=MibTableColumn
fsPtpSATrustTimeout=_FsPtpSATrustTimeout_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,17),_FsPtpSATrustTimeout_Type())
fsPtpSATrustTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSATrustTimeout.setStatus(_A)
class _FsPtpSAChallengeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('challenging',1)))
_FsPtpSAChallengeState_Type.__name__=_D
_FsPtpSAChallengeState_Object=MibTableColumn
fsPtpSAChallengeState=_FsPtpSAChallengeState_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,18),_FsPtpSAChallengeState_Type())
fsPtpSAChallengeState.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSAChallengeState.setStatus(_A)
_FsPtpSAChallengeTimer_Type=Integer32
_FsPtpSAChallengeTimer_Object=MibTableColumn
fsPtpSAChallengeTimer=_FsPtpSAChallengeTimer_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,19),_FsPtpSAChallengeTimer_Type())
fsPtpSAChallengeTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSAChallengeTimer.setStatus(_A)
_FsPtpSAChallengeTimeOut_Type=Integer32
_FsPtpSAChallengeTimeOut_Object=MibTableColumn
fsPtpSAChallengeTimeOut=_FsPtpSAChallengeTimeOut_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,20),_FsPtpSAChallengeTimeOut_Type())
fsPtpSAChallengeTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSAChallengeTimeOut.setStatus(_A)
_FsPtpSARequestNonce_Type=Integer32
_FsPtpSARequestNonce_Object=MibTableColumn
fsPtpSARequestNonce=_FsPtpSARequestNonce_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,21),_FsPtpSARequestNonce_Type())
fsPtpSARequestNonce.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSARequestNonce.setStatus(_A)
_FsPtpSAResponseNonce_Type=Integer32
_FsPtpSAResponseNonce_Object=MibTableColumn
fsPtpSAResponseNonce=_FsPtpSAResponseNonce_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,22),_FsPtpSAResponseNonce_Type())
fsPtpSAResponseNonce.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSAResponseNonce.setStatus(_A)
_FsPtpSAChallengeRequired_Type=TruthValue
_FsPtpSAChallengeRequired_Object=MibTableColumn
fsPtpSAChallengeRequired=_FsPtpSAChallengeRequired_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,23),_FsPtpSAChallengeRequired_Type())
fsPtpSAChallengeRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSAChallengeRequired.setStatus(_A)
_FsPtpSAResponseRequired_Type=TruthValue
_FsPtpSAResponseRequired_Object=MibTableColumn
fsPtpSAResponseRequired=_FsPtpSAResponseRequired_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,24),_FsPtpSAResponseRequired_Type())
fsPtpSAResponseRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSAResponseRequired.setStatus(_A)
class _FsPtpSATypeField_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsPtpSATypeField_Type.__name__=_D
_FsPtpSATypeField_Object=MibTableColumn
fsPtpSATypeField=_FsPtpSATypeField_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,25),_FsPtpSATypeField_Type())
fsPtpSATypeField.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpSATypeField.setStatus(_A)
class _FsPtpSADirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('in',0),('out',1)))
_FsPtpSADirection_Type.__name__=_D
_FsPtpSADirection_Object=MibTableColumn
fsPtpSADirection=_FsPtpSADirection_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,26),_FsPtpSADirection_Type())
fsPtpSADirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpSADirection.setStatus(_A)
_FsPtpSARowStatus_Type=RowStatus
_FsPtpSARowStatus_Object=MibTableColumn
fsPtpSARowStatus=_FsPtpSARowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,15,1,1,27),_FsPtpSARowStatus_Type())
fsPtpSARowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsPtpSARowStatus.setStatus(_A)
_FsPtpAltTimeScaleDataSet_ObjectIdentity=ObjectIdentity
fsPtpAltTimeScaleDataSet=_FsPtpAltTimeScaleDataSet_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,1,16))
_FsPtpAltTimeScaleDataSetTable_Object=MibTable
fsPtpAltTimeScaleDataSetTable=_FsPtpAltTimeScaleDataSetTable_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1))
if mibBuilder.loadTexts:fsPtpAltTimeScaleDataSetTable.setStatus(_A)
_FsPtpAltTimeScaleDataSetEntry_Object=MibTableRow
fsPtpAltTimeScaleDataSetEntry=_FsPtpAltTimeScaleDataSetEntry_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1))
fsPtpAltTimeScaleDataSetEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_s))
if mibBuilder.loadTexts:fsPtpAltTimeScaleDataSetEntry.setStatus(_A)
class _FsPtpAltTimeScaleKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_FsPtpAltTimeScaleKeyId_Type.__name__=_D
_FsPtpAltTimeScaleKeyId_Object=MibTableColumn
fsPtpAltTimeScaleKeyId=_FsPtpAltTimeScaleKeyId_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1,1),_FsPtpAltTimeScaleKeyId_Type())
fsPtpAltTimeScaleKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPtpAltTimeScaleKeyId.setStatus(_A)
_FsPtpAltTimeScalecurrentOffset_Type=Integer32
_FsPtpAltTimeScalecurrentOffset_Object=MibTableColumn
fsPtpAltTimeScalecurrentOffset=_FsPtpAltTimeScalecurrentOffset_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1,2),_FsPtpAltTimeScalecurrentOffset_Type())
fsPtpAltTimeScalecurrentOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAltTimeScalecurrentOffset.setStatus(_A)
_FsPtpAltTimeScalejumpSeconds_Type=Integer32
_FsPtpAltTimeScalejumpSeconds_Object=MibTableColumn
fsPtpAltTimeScalejumpSeconds=_FsPtpAltTimeScalejumpSeconds_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1,3),_FsPtpAltTimeScalejumpSeconds_Type())
fsPtpAltTimeScalejumpSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAltTimeScalejumpSeconds.setStatus(_A)
class _FsPtpAltTimeScaletimeOfNextJump_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_FsPtpAltTimeScaletimeOfNextJump_Type.__name__=_G
_FsPtpAltTimeScaletimeOfNextJump_Object=MibTableColumn
fsPtpAltTimeScaletimeOfNextJump=_FsPtpAltTimeScaletimeOfNextJump_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1,4),_FsPtpAltTimeScaletimeOfNextJump_Type())
fsPtpAltTimeScaletimeOfNextJump.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAltTimeScaletimeOfNextJump.setStatus(_A)
class _FsPtpAltTimeScaledisplayName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_FsPtpAltTimeScaledisplayName_Type.__name__=_G
_FsPtpAltTimeScaledisplayName_Object=MibTableColumn
fsPtpAltTimeScaledisplayName=_FsPtpAltTimeScaledisplayName_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1,5),_FsPtpAltTimeScaledisplayName_Type())
fsPtpAltTimeScaledisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpAltTimeScaledisplayName.setStatus(_A)
_FsPtpAltTimeScaleRowStatus_Type=RowStatus
_FsPtpAltTimeScaleRowStatus_Object=MibTableColumn
fsPtpAltTimeScaleRowStatus=_FsPtpAltTimeScaleRowStatus_Object((1,3,6,1,4,1,10876,101,2,45,1,16,1,1,6),_FsPtpAltTimeScaleRowStatus_Type())
fsPtpAltTimeScaleRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsPtpAltTimeScaleRowStatus.setStatus(_A)
_FsPtpNotifications_ObjectIdentity=ObjectIdentity
fsPtpNotifications=_FsPtpNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,2))
_FsPtpTrap_ObjectIdentity=ObjectIdentity
fsPtpTrap=_FsPtpTrap_ObjectIdentity((1,3,6,1,4,1,10876,101,2,45,2,0))
class _FsPtpTrapContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsPtpTrapContextName_Type.__name__=_M
_FsPtpTrapContextName_Object=MibScalar
fsPtpTrapContextName=_FsPtpTrapContextName_Object((1,3,6,1,4,1,10876,101,2,45,2,1),_FsPtpTrapContextName_Type())
fsPtpTrapContextName.setMaxAccess(_t)
if mibBuilder.loadTexts:fsPtpTrapContextName.setStatus(_A)
_FsPtpTrapDomainNumber_Type=Integer32
_FsPtpTrapDomainNumber_Object=MibScalar
fsPtpTrapDomainNumber=_FsPtpTrapDomainNumber_Object((1,3,6,1,4,1,10876,101,2,45,2,2),_FsPtpTrapDomainNumber_Type())
fsPtpTrapDomainNumber.setMaxAccess(_t)
if mibBuilder.loadTexts:fsPtpTrapDomainNumber.setStatus(_A)
class _FsPtpGlobalErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('memfail',1),('bufffail',2),('syncfault',3),('accmasterfault',4),('gmfault',5)))
_FsPtpGlobalErrTrapType_Type.__name__=_D
_FsPtpGlobalErrTrapType_Object=MibScalar
fsPtpGlobalErrTrapType=_FsPtpGlobalErrTrapType_Object((1,3,6,1,4,1,10876,101,2,45,2,3),_FsPtpGlobalErrTrapType_Type())
fsPtpGlobalErrTrapType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPtpGlobalErrTrapType.setStatus(_A)
_FsPtpNotification_Type=OctetString
_FsPtpNotification_Object=MibScalar
fsPtpNotification=_FsPtpNotification_Object((1,3,6,1,4,1,10876,101,2,45,2,4),_FsPtpNotification_Type())
fsPtpNotification.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPtpNotification.setStatus(_A)
fsPtpDomainDataSetEntry.registerAugmentions((_C,_u))
fsPtpClockDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions((_C,_v))
fsPtpCurrentDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions((_C,_w))
fsPtpParentDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions((_C,_x))
fsPtpTimeDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpDomainDataSetEntry.registerAugmentions((_C,_y))
fsPtpTransparentDataSetEntry.setIndexNames(*fsPtpDomainDataSetEntry.getIndexNames())
fsPtpPortStateChangeTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,1))
fsPtpPortStateChangeTrap.setObjects(*((_C,_K),(_C,_z)))
if mibBuilder.loadTexts:fsPtpPortStateChangeTrap.setStatus(_A)
fsPtpGlobalErrorTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,2))
fsPtpGlobalErrorTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:fsPtpGlobalErrorTrap.setStatus(_A)
fsPtpAdminChangeTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,3))
fsPtpAdminChangeTrap.setObjects(*((_C,_K),(_C,_A0)))
if mibBuilder.loadTexts:fsPtpAdminChangeTrap.setStatus(_A)
fsPtpSysCtrlChangeTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,4))
fsPtpSysCtrlChangeTrap.setObjects(*((_C,_K),(_C,_A1)))
if mibBuilder.loadTexts:fsPtpSysCtrlChangeTrap.setStatus(_A)
fsPtpUnicastOptionTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,5))
fsPtpUnicastOptionTrap.setObjects(*((_C,_K),(_C,_A2)))
if mibBuilder.loadTexts:fsPtpUnicastOptionTrap.setStatus(_A)
fsPtpPortPtpStatusTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,6))
fsPtpPortPtpStatusTrap.setObjects(*((_C,_K),(_C,_A3)))
if mibBuilder.loadTexts:fsPtpPortPtpStatusTrap.setStatus(_A)
fsPtpSyncFaultTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,7))
fsPtpSyncFaultTrap.setObjects(*((_C,_K),(_C,_Q),(_C,_N)))
if mibBuilder.loadTexts:fsPtpSyncFaultTrap.setStatus(_A)
fsPtpAccMasterFaultTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,8))
fsPtpAccMasterFaultTrap.setObjects(*((_C,_K),(_C,_Q),(_C,_N)))
if mibBuilder.loadTexts:fsPtpAccMasterFaultTrap.setStatus(_A)
fsPtpGrandMasterFaultTrap=NotificationType((1,3,6,1,4,1,10876,101,2,45,2,0,9))
fsPtpGrandMasterFaultTrap.setObjects(*((_C,_K),(_C,_Q),(_C,_N)))
if mibBuilder.loadTexts:fsPtpGrandMasterFaultTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_P:FsPtpPortNumber,'fsPtpMIB':fsPtpMIB,'fsPtpObjects':fsPtpObjects,'fsPtpGeneralGroup':fsPtpGeneralGroup,'fsPtpGlobalSysCtrl':fsPtpGlobalSysCtrl,'fsPtpGblTraceOption':fsPtpGblTraceOption,'fsPtpPrimaryContext':fsPtpPrimaryContext,'fsPtpTable':fsPtpTable,'fsPtpEntry':fsPtpEntry,_I:fsPtpContextId,_A0:fsPtpAdminStatus,'fsPtpTraceOption':fsPtpTraceOption,'fsPtpContextType':fsPtpContextType,'fsPtpPrimaryDomain':fsPtpPrimaryDomain,_A1:fsPtpContextRowStatus,'fsPtpDomainDataSet':fsPtpDomainDataSet,'fsPtpDomainDataSetTable':fsPtpDomainDataSetTable,'fsPtpDomainDataSetEntry':fsPtpDomainDataSetEntry,_J:fsPtpDomainNumber,'fsPtpDomainClockMode':fsPtpDomainClockMode,'fsPtpDomainClockIdentity':fsPtpDomainClockIdentity,'fsPtpDomainGMClusterQueryInterval':fsPtpDomainGMClusterQueryInterval,'fsPtpDomainRowStatus':fsPtpDomainRowStatus,'fsPtpDefaultDataSet':fsPtpDefaultDataSet,'fsPtpClockDataSetTable':fsPtpClockDataSetTable,_u:fsPtpClockDataSetEntry,'fsPtpClockIdentity':fsPtpClockIdentity,'fsPtpClockTwoStepFlag':fsPtpClockTwoStepFlag,'fsPtpClockNumberPorts':fsPtpClockNumberPorts,'fsPtpClockClass':fsPtpClockClass,'fsPtpClockAccuracy':fsPtpClockAccuracy,'fsPtpClockOffsetScaledLogVariance':fsPtpClockOffsetScaledLogVariance,'fsPtpClockPriority1':fsPtpClockPriority1,'fsPtpClockPriority2':fsPtpClockPriority2,'fsPtpClockSlaveOnly':fsPtpClockSlaveOnly,'fsPtpClockPathTraceOption':fsPtpClockPathTraceOption,'fsPtpClockAccMasterMaxSize':fsPtpClockAccMasterMaxSize,'fsPtpClockSecurityEnabled':fsPtpClockSecurityEnabled,'fsPtpClockNumOfSA':fsPtpClockNumOfSA,'fsPtpCurrentDataSet':fsPtpCurrentDataSet,'fsPtpCurrentDataSetTable':fsPtpCurrentDataSetTable,_v:fsPtpCurrentDataSetEntry,'fsPtpCurrentStepsRemoved':fsPtpCurrentStepsRemoved,'fsPtpCurrentOffsetFromMaster':fsPtpCurrentOffsetFromMaster,'fsPtpCurrentMeanPathDelay':fsPtpCurrentMeanPathDelay,'fsPtpCurrentMasterToSlaveDelay':fsPtpCurrentMasterToSlaveDelay,'fsPtpCurrentSlaveToMasterDelay':fsPtpCurrentSlaveToMasterDelay,'fsPtpParentDataSet':fsPtpParentDataSet,'fsPtpParentDataSetTable':fsPtpParentDataSetTable,_w:fsPtpParentDataSetEntry,'fsPtpParentClockIdentity':fsPtpParentClockIdentity,'fsPtpParentPortNumber':fsPtpParentPortNumber,'fsPtpParentStats':fsPtpParentStats,'fsPtpParentObservedOffsetScaledLogVariance':fsPtpParentObservedOffsetScaledLogVariance,'fsPtpParentObservedClockPhaseChangeRate':fsPtpParentObservedClockPhaseChangeRate,'fsPtpParentGMClockIdentity':fsPtpParentGMClockIdentity,'fsPtpParentGMClockClass':fsPtpParentGMClockClass,'fsPtpParentGMClockAccuracy':fsPtpParentGMClockAccuracy,'fsPtpParentGMClockOffsetScaledLogVariance':fsPtpParentGMClockOffsetScaledLogVariance,'fsPtpParentGMPriority1':fsPtpParentGMPriority1,'fsPtpParentGMPriority2':fsPtpParentGMPriority2,'fsPtpParentClockObservedDrift':fsPtpParentClockObservedDrift,'fsPtpGlobalTimeProportiesDataSet':fsPtpGlobalTimeProportiesDataSet,'fsPtpTimeDataSetTable':fsPtpTimeDataSetTable,_x:fsPtpTimeDataSetEntry,'fsPtpTimeCurrentUTCOffset':fsPtpTimeCurrentUTCOffset,'fsPtpTimeCurrentUTCOffsetValid':fsPtpTimeCurrentUTCOffsetValid,'fsPtpTimeLeap59':fsPtpTimeLeap59,'fsPtpTimeLeap61':fsPtpTimeLeap61,'fsPtpTimeTimeTraceable':fsPtpTimeTimeTraceable,'fsPtpTimeFrequencyTraceable':fsPtpTimeFrequencyTraceable,'fsPtpTimeTimeSource':fsPtpTimeTimeSource,'fsPtpPortConfigurationDataSet':fsPtpPortConfigurationDataSet,'fsPtpPortConfigDataSetTable':fsPtpPortConfigDataSetTable,'fsPtpPortConfigDataSetEntry':fsPtpPortConfigDataSetEntry,_O:fsPtpPortIndex,'fsPtpPortClockIdentity':fsPtpPortClockIdentity,'fsPtpPortInterfaceType':fsPtpPortInterfaceType,'fsPtpPortIfaceNumber':fsPtpPortIfaceNumber,_z:fsPtpPortState,'fsPtpPortMinDelayReqInterval':fsPtpPortMinDelayReqInterval,'fsPtpPortPeerMeanPathDelay':fsPtpPortPeerMeanPathDelay,'fsPtpPortAnnounceInterval':fsPtpPortAnnounceInterval,'fsPtpPortAnnounceReceiptTimeout':fsPtpPortAnnounceReceiptTimeout,'fsPtpPortSyncInterval':fsPtpPortSyncInterval,'fsPtpPortSynclimit':fsPtpPortSynclimit,'fsPtpPortDelayMechanism':fsPtpPortDelayMechanism,'fsPtpPortMinPdelayReqInterval':fsPtpPortMinPdelayReqInterval,'fsPtpPortVersionNumber':fsPtpPortVersionNumber,_A2:fsPtpPortUnicastNegOption,'fsPtpPortUnicastMasterMaxSize':fsPtpPortUnicastMasterMaxSize,'fsPtpPortAccMasterEnabled':fsPtpPortAccMasterEnabled,'fsPtpPortNumOfAltMaster':fsPtpPortNumOfAltMaster,'fsPtpPortAltMulcastSync':fsPtpPortAltMulcastSync,'fsPtpPortAltMulcastSyncInterval':fsPtpPortAltMulcastSyncInterval,_A3:fsPtpPortPtpStatus,'fsPtpPortRcvdAnnounceMsgCnt':fsPtpPortRcvdAnnounceMsgCnt,'fsPtpPortRcvdSyncMsgCnt':fsPtpPortRcvdSyncMsgCnt,'fsPtpPortRcvdDelayReqMsgCnt':fsPtpPortRcvdDelayReqMsgCnt,'fsPtpPortRcvdDelayRespMsgCnt':fsPtpPortRcvdDelayRespMsgCnt,'fsPtpPortTransDelayReqMsgCnt':fsPtpPortTransDelayReqMsgCnt,'fsPtpPortDiscardedMsgCnt':fsPtpPortDiscardedMsgCnt,'fsPtpPortRowStatus':fsPtpPortRowStatus,'fsPtpForeignMasterDataSet':fsPtpForeignMasterDataSet,'fsPtpForeignMasterDataSetTable':fsPtpForeignMasterDataSetTable,'fsPtpForeignMasterDataSetEntry':fsPtpForeignMasterDataSetEntry,_e:fsPtpForeignMasterClockIdentity,_f:fsPtpForeignMasterPortIndex,'fsPtpForeignMasterAnnounceMsgs':fsPtpForeignMasterAnnounceMsgs,'fsPtpTransparentDataSet':fsPtpTransparentDataSet,'fsPtpTransparentDataSetTable':fsPtpTransparentDataSetTable,_y:fsPtpTransparentDataSetEntry,'fsPtpTransparentClockIdentity':fsPtpTransparentClockIdentity,'fsPtpTransparentClockTwoStepFlag':fsPtpTransparentClockTwoStepFlag,'fsPtpTransparentClockNumberPorts':fsPtpTransparentClockNumberPorts,'fsPtpTransparentClockDelaymechanism':fsPtpTransparentClockDelaymechanism,'fsPtpTransparentClockPrimaryDomain':fsPtpTransparentClockPrimaryDomain,'fsPtpTransparentPortDataSet':fsPtpTransparentPortDataSet,'fsPtpTransparentPortDataSetTable':fsPtpTransparentPortDataSetTable,'fsPtpTransparentPortDataSetEntry':fsPtpTransparentPortDataSetEntry,_g:fsPtpTransparentPortIndex,'fsPtpTransparentPortInterfaceType':fsPtpTransparentPortInterfaceType,'fsPtpTransparentPortIfaceNumber':fsPtpTransparentPortIfaceNumber,'fsPtpTransparentPortClockIdentity':fsPtpTransparentPortClockIdentity,'fsPtpTransparentPortMinPdelayReqInterval':fsPtpTransparentPortMinPdelayReqInterval,'fsPtpTransparentPortFaultyFlag':fsPtpTransparentPortFaultyFlag,'fsPtpTransparentPortPeerMeanPathDelay':fsPtpTransparentPortPeerMeanPathDelay,'fsPtpTransparentPortPtpStatus':fsPtpTransparentPortPtpStatus,'fsPtpTransparentPortRowStatus':fsPtpTransparentPortRowStatus,'fsPtpGrandMasterClusterDataSet':fsPtpGrandMasterClusterDataSet,'fsPtpGrandMasterClusterDataSetTable':fsPtpGrandMasterClusterDataSetTable,'fsPtpGrandMasterClusterDataSetEntry':fsPtpGrandMasterClusterDataSetEntry,_h:fsPtpGrandMasterClusterNetworkProtocol,_i:fsPtpGrandMasterClusterAddLength,_j:fsPtpGrandMasterClusterAddr,'fsPtpGrandMasterClusterRowStatus':fsPtpGrandMasterClusterRowStatus,'fsPtpUnicastMasterDataSet':fsPtpUnicastMasterDataSet,'fsPtpUnicastMasterDataSetTable':fsPtpUnicastMasterDataSetTable,'fsPtpUnicastMasterDataSetEntry':fsPtpUnicastMasterDataSetEntry,_k:fsPtpUnicastMasterNetworkProtocol,_l:fsPtpUnicastMasterAddLength,_m:fsPtpUnicastMasterAddr,'fsPtpUnicastMasterRowStatus':fsPtpUnicastMasterRowStatus,'fsPtpAccMasterDataSet':fsPtpAccMasterDataSet,'fsPtpAccMasterDataSetTable':fsPtpAccMasterDataSetTable,'fsPtpAccMasterDataSetEntry':fsPtpAccMasterDataSetEntry,_n:fsPtpAccMasterNetworkProtocol,_o:fsPtpAccMasterAddLength,_p:fsPtpAccMasterAddr,'fsPtpAccMasterAlternatePriority':fsPtpAccMasterAlternatePriority,'fsPtpAccMasterRowStatus':fsPtpAccMasterRowStatus,'fsPtpSecKeyDataSet':fsPtpSecKeyDataSet,'fsPtpSecKeyDataSetTable':fsPtpSecKeyDataSetTable,'fsPtpSecKeyDataSetEntry':fsPtpSecKeyDataSetEntry,_q:fsPtpSecKeyId,'fsPtpSecKeyAlgorithmId':fsPtpSecKeyAlgorithmId,'fsPtpSecKeyLength':fsPtpSecKeyLength,'fsPtpSecKey':fsPtpSecKey,'fsPtpSecKeyStartTime':fsPtpSecKeyStartTime,'fsPtpSecKeyExpirationTime':fsPtpSecKeyExpirationTime,'fsPtpSecKeyValid':fsPtpSecKeyValid,'fsPtpSecKeyRowStatus':fsPtpSecKeyRowStatus,'fsPtpSADataSet':fsPtpSADataSet,'fsPtpSADataSetTable':fsPtpSADataSetTable,'fsPtpSADataSetEntry':fsPtpSADataSetEntry,_r:fsPtpSAId,'fsPtpSASrcPortNumber':fsPtpSASrcPortNumber,'fsPtpSASrcAddrLength':fsPtpSASrcAddrLength,'fsPtpSASrcAddr':fsPtpSASrcAddr,'fsPtpSADstPortNumber':fsPtpSADstPortNumber,'fsPtpSADstAddrLength':fsPtpSADstAddrLength,'fsPtpSADstAddr':fsPtpSADstAddr,'fsPtpSASrcClockIdentity':fsPtpSASrcClockIdentity,'fsPtpSADstClockIdentity':fsPtpSADstClockIdentity,'fsPtpSAReplayCounter':fsPtpSAReplayCounter,'fsPtpSALifeTimeId':fsPtpSALifeTimeId,'fsPtpSAKeyId':fsPtpSAKeyId,'fsPtpSANextLifeTimeId':fsPtpSANextLifeTimeId,'fsPtpSANextKeyId':fsPtpSANextKeyId,'fsPtpSATrustState':fsPtpSATrustState,'fsPtpSATrustTimer':fsPtpSATrustTimer,'fsPtpSATrustTimeout':fsPtpSATrustTimeout,'fsPtpSAChallengeState':fsPtpSAChallengeState,'fsPtpSAChallengeTimer':fsPtpSAChallengeTimer,'fsPtpSAChallengeTimeOut':fsPtpSAChallengeTimeOut,'fsPtpSARequestNonce':fsPtpSARequestNonce,'fsPtpSAResponseNonce':fsPtpSAResponseNonce,'fsPtpSAChallengeRequired':fsPtpSAChallengeRequired,'fsPtpSAResponseRequired':fsPtpSAResponseRequired,'fsPtpSATypeField':fsPtpSATypeField,'fsPtpSADirection':fsPtpSADirection,'fsPtpSARowStatus':fsPtpSARowStatus,'fsPtpAltTimeScaleDataSet':fsPtpAltTimeScaleDataSet,'fsPtpAltTimeScaleDataSetTable':fsPtpAltTimeScaleDataSetTable,'fsPtpAltTimeScaleDataSetEntry':fsPtpAltTimeScaleDataSetEntry,_s:fsPtpAltTimeScaleKeyId,'fsPtpAltTimeScalecurrentOffset':fsPtpAltTimeScalecurrentOffset,'fsPtpAltTimeScalejumpSeconds':fsPtpAltTimeScalejumpSeconds,'fsPtpAltTimeScaletimeOfNextJump':fsPtpAltTimeScaletimeOfNextJump,'fsPtpAltTimeScaledisplayName':fsPtpAltTimeScaledisplayName,'fsPtpAltTimeScaleRowStatus':fsPtpAltTimeScaleRowStatus,'fsPtpNotifications':fsPtpNotifications,'fsPtpTrap':fsPtpTrap,'fsPtpPortStateChangeTrap':fsPtpPortStateChangeTrap,'fsPtpGlobalErrorTrap':fsPtpGlobalErrorTrap,'fsPtpAdminChangeTrap':fsPtpAdminChangeTrap,'fsPtpSysCtrlChangeTrap':fsPtpSysCtrlChangeTrap,'fsPtpUnicastOptionTrap':fsPtpUnicastOptionTrap,'fsPtpPortPtpStatusTrap':fsPtpPortPtpStatusTrap,'fsPtpSyncFaultTrap':fsPtpSyncFaultTrap,'fsPtpAccMasterFaultTrap':fsPtpAccMasterFaultTrap,'fsPtpGrandMasterFaultTrap':fsPtpGrandMasterFaultTrap,_K:fsPtpTrapContextName,_Q:fsPtpTrapDomainNumber,_N:fsPtpGlobalErrTrapType,'fsPtpNotification':fsPtpNotification})