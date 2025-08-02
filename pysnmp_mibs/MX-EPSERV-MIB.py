_s='epSpecificDtmfMapTimeoutEpId'
_r='callStatisticsEpId'
_q='epSpecificDelayedHotlineEpId'
_p='anyTimeout'
_o='interDtmfOrCompletionTimeout'
_n='firstDtmfTimeout'
_m='callCompletionConfigIndex'
_l='epSpecificCallCompletionEpId'
_k='forwardNoAnswerConfigEpId'
_j='epSpecificForwardNoAnswerEpId'
_i='forwardOnBusyConfigEpId'
_h='epSpecificForwardOnBusyEpId'
_g='forwardUnconditionalConfigEpId'
_f='epSpecificForwardUnconditionalEpId'
_e='conferenceStatusEpId'
_d='epSpecificConferenceEpId'
_c='conferenceServer'
_b='transferStatusEpId'
_a='epSpecificTransferEpId'
_Z='secondCallStatusEpId'
_Y='epSpecificSecondCallEpId'
_X='autoSwitch'
_W='callWaitingUserConfigEpId'
_V='callWaitingStatusEpId'
_U='epSpecificCallWaitingEpId'
_T='holdStatusEpId'
_S='epSpecificHoldEpId'
_R='epSpecificAutoCallEpId'
_Q='callDtmfMapRefuseIndex'
_P='endpoint'
_O='callDtmfMapAllowedIndex'
_N='epSpecificCallEpId'
_M='transmitUsingSignalingProtocol'
_L='processLocally'
_K='MxIpHostNamePort'
_J='MxActivationState'
_I='OctetString'
_H='Unsigned32'
_G='MxDigitMap'
_F='Integer32'
_E='MX-EPSERV-MIB'
_D='MxEnableState'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC',_J,'MxAdvancedIpPort',_G,_D,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_K,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
epServMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700))
_EpServMIBObjects_ObjectIdentity=ObjectIdentity
epServMIBObjects=_EpServMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1))
_CallGroup_ObjectIdentity=ObjectIdentity
callGroup=_CallGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100))
class _DefaultCallHookFlashProcessing_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_L,100),(_M,200)))
_DefaultCallHookFlashProcessing_Type.__name__=_F
_DefaultCallHookFlashProcessing_Object=MibScalar
defaultCallHookFlashProcessing=_DefaultCallHookFlashProcessing_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,200),_DefaultCallHookFlashProcessing_Type())
defaultCallHookFlashProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallHookFlashProcessing.setStatus(_A)
class _DefaultCallAllowDirectIp_Type(MxEnableState):defaultValue=0
_DefaultCallAllowDirectIp_Type.__name__=_D
_DefaultCallAllowDirectIp_Object=MibScalar
defaultCallAllowDirectIp=_DefaultCallAllowDirectIp_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,300),_DefaultCallAllowDirectIp_Type())
defaultCallAllowDirectIp.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallAllowDirectIp.setStatus(_A)
_EpSpecificCallTable_Object=MibTable
epSpecificCallTable=_EpSpecificCallTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,400))
if mibBuilder.loadTexts:epSpecificCallTable.setStatus(_A)
_EpSpecificCallEntry_Object=MibTableRow
epSpecificCallEntry=_EpSpecificCallEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,400,1))
epSpecificCallEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:epSpecificCallEntry.setStatus(_A)
_EpSpecificCallEpId_Type=OctetString
_EpSpecificCallEpId_Object=MibTableColumn
epSpecificCallEpId=_EpSpecificCallEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,400,1,100),_EpSpecificCallEpId_Type())
epSpecificCallEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificCallEpId.setStatus(_A)
class _EpSpecificCallEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCallEnableConfig_Type.__name__=_D
_EpSpecificCallEnableConfig_Object=MibTableColumn
epSpecificCallEnableConfig=_EpSpecificCallEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,400,1,200),_EpSpecificCallEnableConfig_Type())
epSpecificCallEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallEnableConfig.setStatus(_A)
class _EpSpecificCallHookFlashProcessing_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_L,100),(_M,200)))
_EpSpecificCallHookFlashProcessing_Type.__name__=_F
_EpSpecificCallHookFlashProcessing_Object=MibTableColumn
epSpecificCallHookFlashProcessing=_EpSpecificCallHookFlashProcessing_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,400,1,400),_EpSpecificCallHookFlashProcessing_Type())
epSpecificCallHookFlashProcessing.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallHookFlashProcessing.setStatus(_A)
_CallDtmfMapGroup_ObjectIdentity=ObjectIdentity
callDtmfMapGroup=_CallDtmfMapGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500))
_CallDtmfMapAllowedTable_Object=MibTable
callDtmfMapAllowedTable=_CallDtmfMapAllowedTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100))
if mibBuilder.loadTexts:callDtmfMapAllowedTable.setStatus(_A)
_CallDtmfMapAllowedEntry_Object=MibTableRow
callDtmfMapAllowedEntry=_CallDtmfMapAllowedEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1))
callDtmfMapAllowedEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:callDtmfMapAllowedEntry.setStatus(_A)
class _CallDtmfMapAllowedIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CallDtmfMapAllowedIndex_Type.__name__=_H
_CallDtmfMapAllowedIndex_Object=MibTableColumn
callDtmfMapAllowedIndex=_CallDtmfMapAllowedIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,100),_CallDtmfMapAllowedIndex_Type())
callDtmfMapAllowedIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callDtmfMapAllowedIndex.setStatus(_A)
class _CallDtmfMapAllowedEnable_Type(MxEnableState):defaultValue=1
_CallDtmfMapAllowedEnable_Type.__name__=_D
_CallDtmfMapAllowedEnable_Object=MibTableColumn
callDtmfMapAllowedEnable=_CallDtmfMapAllowedEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,200),_CallDtmfMapAllowedEnable_Type())
callDtmfMapAllowedEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedEnable.setStatus(_A)
class _CallDtmfMapAllowedApplyTo_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('unit',100),(_P,200)))
_CallDtmfMapAllowedApplyTo_Type.__name__=_F
_CallDtmfMapAllowedApplyTo_Object=MibTableColumn
callDtmfMapAllowedApplyTo=_CallDtmfMapAllowedApplyTo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,300),_CallDtmfMapAllowedApplyTo_Type())
callDtmfMapAllowedApplyTo.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedApplyTo.setStatus(_A)
class _CallDtmfMapAllowedEpId_Type(OctetString):defaultValue=OctetString('')
_CallDtmfMapAllowedEpId_Type.__name__=_I
_CallDtmfMapAllowedEpId_Object=MibTableColumn
callDtmfMapAllowedEpId=_CallDtmfMapAllowedEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,400),_CallDtmfMapAllowedEpId_Type())
callDtmfMapAllowedEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedEpId.setStatus(_A)
class _CallDtmfMapAllowedDtmfMap_Type(MxDigitMap):defaultValue=OctetString('x.T')
_CallDtmfMapAllowedDtmfMap_Type.__name__=_G
_CallDtmfMapAllowedDtmfMap_Object=MibTableColumn
callDtmfMapAllowedDtmfMap=_CallDtmfMapAllowedDtmfMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,500),_CallDtmfMapAllowedDtmfMap_Type())
callDtmfMapAllowedDtmfMap.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedDtmfMap.setStatus(_A)
class _CallDtmfMapAllowedDtmfTransformation_Type(OctetString):defaultValue=OctetString('x');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CallDtmfMapAllowedDtmfTransformation_Type.__name__=_I
_CallDtmfMapAllowedDtmfTransformation_Object=MibTableColumn
callDtmfMapAllowedDtmfTransformation=_CallDtmfMapAllowedDtmfTransformation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,600),_CallDtmfMapAllowedDtmfTransformation_Type())
callDtmfMapAllowedDtmfTransformation.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedDtmfTransformation.setStatus(_A)
class _CallDtmfMapAllowedTargetHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_CallDtmfMapAllowedTargetHost_Type.__name__=_K
_CallDtmfMapAllowedTargetHost_Object=MibTableColumn
callDtmfMapAllowedTargetHost=_CallDtmfMapAllowedTargetHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,700),_CallDtmfMapAllowedTargetHost_Type())
callDtmfMapAllowedTargetHost.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedTargetHost.setStatus(_A)
class _CallDtmfMapAllowedEmergency_Type(MxEnableState):defaultValue=0
_CallDtmfMapAllowedEmergency_Type.__name__=_D
_CallDtmfMapAllowedEmergency_Object=MibTableColumn
callDtmfMapAllowedEmergency=_CallDtmfMapAllowedEmergency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,100,1,800),_CallDtmfMapAllowedEmergency_Type())
callDtmfMapAllowedEmergency.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapAllowedEmergency.setStatus(_A)
_CallDtmfMapRefuseTable_Object=MibTable
callDtmfMapRefuseTable=_CallDtmfMapRefuseTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200))
if mibBuilder.loadTexts:callDtmfMapRefuseTable.setStatus(_A)
_CallDtmfMapRefuseEntry_Object=MibTableRow
callDtmfMapRefuseEntry=_CallDtmfMapRefuseEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200,1))
callDtmfMapRefuseEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:callDtmfMapRefuseEntry.setStatus(_A)
class _CallDtmfMapRefuseIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CallDtmfMapRefuseIndex_Type.__name__=_H
_CallDtmfMapRefuseIndex_Object=MibTableColumn
callDtmfMapRefuseIndex=_CallDtmfMapRefuseIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200,1,100),_CallDtmfMapRefuseIndex_Type())
callDtmfMapRefuseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callDtmfMapRefuseIndex.setStatus(_A)
class _CallDtmfMapRefuseEnable_Type(MxEnableState):defaultValue=0
_CallDtmfMapRefuseEnable_Type.__name__=_D
_CallDtmfMapRefuseEnable_Object=MibTableColumn
callDtmfMapRefuseEnable=_CallDtmfMapRefuseEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200,1,200),_CallDtmfMapRefuseEnable_Type())
callDtmfMapRefuseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapRefuseEnable.setStatus(_A)
class _CallDtmfMapRefuseApplyTo_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('unit',100),(_P,200)))
_CallDtmfMapRefuseApplyTo_Type.__name__=_F
_CallDtmfMapRefuseApplyTo_Object=MibTableColumn
callDtmfMapRefuseApplyTo=_CallDtmfMapRefuseApplyTo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200,1,300),_CallDtmfMapRefuseApplyTo_Type())
callDtmfMapRefuseApplyTo.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapRefuseApplyTo.setStatus(_A)
class _CallDtmfMapRefuseEpId_Type(OctetString):defaultValue=OctetString('')
_CallDtmfMapRefuseEpId_Type.__name__=_I
_CallDtmfMapRefuseEpId_Object=MibTableColumn
callDtmfMapRefuseEpId=_CallDtmfMapRefuseEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200,1,400),_CallDtmfMapRefuseEpId_Type())
callDtmfMapRefuseEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapRefuseEpId.setStatus(_A)
class _CallDtmfMapRefuseDtmfMap_Type(MxDigitMap):defaultValue=OctetString('')
_CallDtmfMapRefuseDtmfMap_Type.__name__=_G
_CallDtmfMapRefuseDtmfMap_Object=MibTableColumn
callDtmfMapRefuseDtmfMap=_CallDtmfMapRefuseDtmfMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,100,500,200,1,500),_CallDtmfMapRefuseDtmfMap_Type())
callDtmfMapRefuseDtmfMap.setMaxAccess(_B)
if mibBuilder.loadTexts:callDtmfMapRefuseDtmfMap.setStatus(_A)
_AutoCallGroup_ObjectIdentity=ObjectIdentity
autoCallGroup=_AutoCallGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200))
class _DefaultAutoCallEnable_Type(MxEnableState):defaultValue=0
_DefaultAutoCallEnable_Type.__name__=_D
_DefaultAutoCallEnable_Object=MibScalar
defaultAutoCallEnable=_DefaultAutoCallEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,100),_DefaultAutoCallEnable_Type())
defaultAutoCallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultAutoCallEnable.setStatus(_A)
class _DefaultAutoCallTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DefaultAutoCallTargetAddress_Type.__name__=_I
_DefaultAutoCallTargetAddress_Object=MibScalar
defaultAutoCallTargetAddress=_DefaultAutoCallTargetAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,200),_DefaultAutoCallTargetAddress_Type())
defaultAutoCallTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultAutoCallTargetAddress.setStatus(_A)
_EpSpecificAutoCallTable_Object=MibTable
epSpecificAutoCallTable=_EpSpecificAutoCallTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,300))
if mibBuilder.loadTexts:epSpecificAutoCallTable.setStatus(_A)
_EpSpecificAutoCallEntry_Object=MibTableRow
epSpecificAutoCallEntry=_EpSpecificAutoCallEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,300,1))
epSpecificAutoCallEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:epSpecificAutoCallEntry.setStatus(_A)
_EpSpecificAutoCallEpId_Type=OctetString
_EpSpecificAutoCallEpId_Object=MibTableColumn
epSpecificAutoCallEpId=_EpSpecificAutoCallEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,300,1,100),_EpSpecificAutoCallEpId_Type())
epSpecificAutoCallEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificAutoCallEpId.setStatus(_A)
class _EpSpecificAutoCallEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificAutoCallEnableConfig_Type.__name__=_D
_EpSpecificAutoCallEnableConfig_Object=MibTableColumn
epSpecificAutoCallEnableConfig=_EpSpecificAutoCallEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,300,1,200),_EpSpecificAutoCallEnableConfig_Type())
epSpecificAutoCallEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificAutoCallEnableConfig.setStatus(_A)
class _EpSpecificAutoCallEnable_Type(MxEnableState):defaultValue=0
_EpSpecificAutoCallEnable_Type.__name__=_D
_EpSpecificAutoCallEnable_Object=MibTableColumn
epSpecificAutoCallEnable=_EpSpecificAutoCallEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,300,1,300),_EpSpecificAutoCallEnable_Type())
epSpecificAutoCallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificAutoCallEnable.setStatus(_A)
class _EpSpecificAutoCallTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_EpSpecificAutoCallTargetAddress_Type.__name__=_I
_EpSpecificAutoCallTargetAddress_Object=MibTableColumn
epSpecificAutoCallTargetAddress=_EpSpecificAutoCallTargetAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,200,300,1,400),_EpSpecificAutoCallTargetAddress_Type())
epSpecificAutoCallTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificAutoCallTargetAddress.setStatus(_A)
_HoldGroup_ObjectIdentity=ObjectIdentity
holdGroup=_HoldGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300))
class _DefaultHoldEnable_Type(MxEnableState):defaultValue=1
_DefaultHoldEnable_Type.__name__=_D
_DefaultHoldEnable_Object=MibScalar
defaultHoldEnable=_DefaultHoldEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,100),_DefaultHoldEnable_Type())
defaultHoldEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultHoldEnable.setStatus(_A)
_EpSpecificHoldTable_Object=MibTable
epSpecificHoldTable=_EpSpecificHoldTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,200))
if mibBuilder.loadTexts:epSpecificHoldTable.setStatus(_A)
_EpSpecificHoldEntry_Object=MibTableRow
epSpecificHoldEntry=_EpSpecificHoldEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,200,1))
epSpecificHoldEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:epSpecificHoldEntry.setStatus(_A)
_EpSpecificHoldEpId_Type=OctetString
_EpSpecificHoldEpId_Object=MibTableColumn
epSpecificHoldEpId=_EpSpecificHoldEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,200,1,100),_EpSpecificHoldEpId_Type())
epSpecificHoldEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificHoldEpId.setStatus(_A)
class _EpSpecificHoldEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificHoldEnableConfig_Type.__name__=_D
_EpSpecificHoldEnableConfig_Object=MibTableColumn
epSpecificHoldEnableConfig=_EpSpecificHoldEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,200,1,200),_EpSpecificHoldEnableConfig_Type())
epSpecificHoldEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificHoldEnableConfig.setStatus(_A)
class _EpSpecificHoldEnable_Type(MxEnableState):defaultValue=1
_EpSpecificHoldEnable_Type.__name__=_D
_EpSpecificHoldEnable_Object=MibTableColumn
epSpecificHoldEnable=_EpSpecificHoldEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,200,1,300),_EpSpecificHoldEnable_Type())
epSpecificHoldEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificHoldEnable.setStatus(_A)
_HoldStatusTable_Object=MibTable
holdStatusTable=_HoldStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,300))
if mibBuilder.loadTexts:holdStatusTable.setStatus(_A)
_HoldStatusEntry_Object=MibTableRow
holdStatusEntry=_HoldStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,300,1))
holdStatusEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:holdStatusEntry.setStatus(_A)
_HoldStatusEpId_Type=OctetString
_HoldStatusEpId_Object=MibTableColumn
holdStatusEpId=_HoldStatusEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,300,1,100),_HoldStatusEpId_Type())
holdStatusEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:holdStatusEpId.setStatus(_A)
_HoldStatusState_Type=MxActivationState
_HoldStatusState_Object=MibTableColumn
holdStatusState=_HoldStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,300,300,1,200),_HoldStatusState_Type())
holdStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:holdStatusState.setStatus(_A)
_CallWaitingGroup_ObjectIdentity=ObjectIdentity
callWaitingGroup=_CallWaitingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400))
class _DefaultCallWaitingEnable_Type(MxEnableState):defaultValue=1
_DefaultCallWaitingEnable_Type.__name__=_D
_DefaultCallWaitingEnable_Object=MibScalar
defaultCallWaitingEnable=_DefaultCallWaitingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,100),_DefaultCallWaitingEnable_Type())
defaultCallWaitingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallWaitingEnable.setStatus(_A)
class _DefaultCallWaitingCancelDtmfMap_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultCallWaitingCancelDtmfMap_Type.__name__=_G
_DefaultCallWaitingCancelDtmfMap_Object=MibScalar
defaultCallWaitingCancelDtmfMap=_DefaultCallWaitingCancelDtmfMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,200),_DefaultCallWaitingCancelDtmfMap_Type())
defaultCallWaitingCancelDtmfMap.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallWaitingCancelDtmfMap.setStatus(_A)
class _DefaultCallWaitingActivationDtmfMap_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultCallWaitingActivationDtmfMap_Type.__name__=_G
_DefaultCallWaitingActivationDtmfMap_Object=MibScalar
defaultCallWaitingActivationDtmfMap=_DefaultCallWaitingActivationDtmfMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,210),_DefaultCallWaitingActivationDtmfMap_Type())
defaultCallWaitingActivationDtmfMap.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallWaitingActivationDtmfMap.setStatus(_A)
class _DefaultCallWaitingDeactivationDtmfMap_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultCallWaitingDeactivationDtmfMap_Type.__name__=_G
_DefaultCallWaitingDeactivationDtmfMap_Object=MibScalar
defaultCallWaitingDeactivationDtmfMap=_DefaultCallWaitingDeactivationDtmfMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,220),_DefaultCallWaitingDeactivationDtmfMap_Type())
defaultCallWaitingDeactivationDtmfMap.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallWaitingDeactivationDtmfMap.setStatus(_A)
_EpSpecificCallWaitingTable_Object=MibTable
epSpecificCallWaitingTable=_EpSpecificCallWaitingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,300))
if mibBuilder.loadTexts:epSpecificCallWaitingTable.setStatus(_A)
_EpSpecificCallWaitingEntry_Object=MibTableRow
epSpecificCallWaitingEntry=_EpSpecificCallWaitingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,300,1))
epSpecificCallWaitingEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:epSpecificCallWaitingEntry.setStatus(_A)
_EpSpecificCallWaitingEpId_Type=OctetString
_EpSpecificCallWaitingEpId_Object=MibTableColumn
epSpecificCallWaitingEpId=_EpSpecificCallWaitingEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,300,1,100),_EpSpecificCallWaitingEpId_Type())
epSpecificCallWaitingEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificCallWaitingEpId.setStatus(_A)
class _EpSpecificCallWaitingEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCallWaitingEnableConfig_Type.__name__=_D
_EpSpecificCallWaitingEnableConfig_Object=MibTableColumn
epSpecificCallWaitingEnableConfig=_EpSpecificCallWaitingEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,300,1,200),_EpSpecificCallWaitingEnableConfig_Type())
epSpecificCallWaitingEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallWaitingEnableConfig.setStatus(_A)
class _EpSpecificCallWaitingEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCallWaitingEnable_Type.__name__=_D
_EpSpecificCallWaitingEnable_Object=MibTableColumn
epSpecificCallWaitingEnable=_EpSpecificCallWaitingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,300,1,300),_EpSpecificCallWaitingEnable_Type())
epSpecificCallWaitingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallWaitingEnable.setStatus(_A)
_CallWaitingStatusTable_Object=MibTable
callWaitingStatusTable=_CallWaitingStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,400))
if mibBuilder.loadTexts:callWaitingStatusTable.setStatus(_A)
_CallWaitingStatusEntry_Object=MibTableRow
callWaitingStatusEntry=_CallWaitingStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,400,1))
callWaitingStatusEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:callWaitingStatusEntry.setStatus(_A)
_CallWaitingStatusEpId_Type=OctetString
_CallWaitingStatusEpId_Object=MibTableColumn
callWaitingStatusEpId=_CallWaitingStatusEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,400,1,100),_CallWaitingStatusEpId_Type())
callWaitingStatusEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:callWaitingStatusEpId.setStatus(_A)
_CallWaitingStatusState_Type=MxActivationState
_CallWaitingStatusState_Object=MibTableColumn
callWaitingStatusState=_CallWaitingStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,400,1,200),_CallWaitingStatusState_Type())
callWaitingStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:callWaitingStatusState.setStatus(_A)
_CallWaitingUserConfigTable_Object=MibTable
callWaitingUserConfigTable=_CallWaitingUserConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,500))
if mibBuilder.loadTexts:callWaitingUserConfigTable.setStatus(_A)
_CallWaitingUserConfigEntry_Object=MibTableRow
callWaitingUserConfigEntry=_CallWaitingUserConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,500,1))
callWaitingUserConfigEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:callWaitingUserConfigEntry.setStatus(_A)
_CallWaitingUserConfigEpId_Type=OctetString
_CallWaitingUserConfigEpId_Object=MibTableColumn
callWaitingUserConfigEpId=_CallWaitingUserConfigEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,500,1,100),_CallWaitingUserConfigEpId_Type())
callWaitingUserConfigEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:callWaitingUserConfigEpId.setStatus(_A)
class _CallWaitingUserConfigState_Type(MxActivationState):defaultValue=1
_CallWaitingUserConfigState_Type.__name__=_J
_CallWaitingUserConfigState_Object=MibTableColumn
callWaitingUserConfigState=_CallWaitingUserConfigState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,400,500,1,200),_CallWaitingUserConfigState_Type())
callWaitingUserConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:callWaitingUserConfigState.setStatus(_A)
_SecondCallGroup_ObjectIdentity=ObjectIdentity
secondCallGroup=_SecondCallGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500))
class _DefaultSecondCallEnable_Type(MxEnableState):defaultValue=1
_DefaultSecondCallEnable_Type.__name__=_D
_DefaultSecondCallEnable_Object=MibScalar
defaultSecondCallEnable=_DefaultSecondCallEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,100),_DefaultSecondCallEnable_Type())
defaultSecondCallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSecondCallEnable.setStatus(_A)
class _DefaultSecondCallDisconnectAction_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('wait',100),(_X,200)))
_DefaultSecondCallDisconnectAction_Type.__name__=_F
_DefaultSecondCallDisconnectAction_Object=MibScalar
defaultSecondCallDisconnectAction=_DefaultSecondCallDisconnectAction_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,150),_DefaultSecondCallDisconnectAction_Type())
defaultSecondCallDisconnectAction.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSecondCallDisconnectAction.setStatus(_A)
_EpSpecificSecondCallTable_Object=MibTable
epSpecificSecondCallTable=_EpSpecificSecondCallTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,200))
if mibBuilder.loadTexts:epSpecificSecondCallTable.setStatus(_A)
_EpSpecificSecondCallEntry_Object=MibTableRow
epSpecificSecondCallEntry=_EpSpecificSecondCallEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,200,1))
epSpecificSecondCallEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:epSpecificSecondCallEntry.setStatus(_A)
_EpSpecificSecondCallEpId_Type=OctetString
_EpSpecificSecondCallEpId_Object=MibTableColumn
epSpecificSecondCallEpId=_EpSpecificSecondCallEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,200,1,100),_EpSpecificSecondCallEpId_Type())
epSpecificSecondCallEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificSecondCallEpId.setStatus(_A)
class _EpSpecificSecondCallEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificSecondCallEnableConfig_Type.__name__=_D
_EpSpecificSecondCallEnableConfig_Object=MibTableColumn
epSpecificSecondCallEnableConfig=_EpSpecificSecondCallEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,200,1,200),_EpSpecificSecondCallEnableConfig_Type())
epSpecificSecondCallEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecondCallEnableConfig.setStatus(_A)
class _EpSpecificSecondCallEnable_Type(MxEnableState):defaultValue=1
_EpSpecificSecondCallEnable_Type.__name__=_D
_EpSpecificSecondCallEnable_Object=MibTableColumn
epSpecificSecondCallEnable=_EpSpecificSecondCallEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,200,1,300),_EpSpecificSecondCallEnable_Type())
epSpecificSecondCallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecondCallEnable.setStatus(_A)
class _EpSpecificSecondCallDisconnectAction_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('wait',100),(_X,200)))
_EpSpecificSecondCallDisconnectAction_Type.__name__=_F
_EpSpecificSecondCallDisconnectAction_Object=MibTableColumn
epSpecificSecondCallDisconnectAction=_EpSpecificSecondCallDisconnectAction_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,200,1,400),_EpSpecificSecondCallDisconnectAction_Type())
epSpecificSecondCallDisconnectAction.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecondCallDisconnectAction.setStatus(_A)
_SecondCallStatusTable_Object=MibTable
secondCallStatusTable=_SecondCallStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,300))
if mibBuilder.loadTexts:secondCallStatusTable.setStatus(_A)
_SecondCallStatusEntry_Object=MibTableRow
secondCallStatusEntry=_SecondCallStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,300,1))
secondCallStatusEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:secondCallStatusEntry.setStatus(_A)
_SecondCallStatusEpId_Type=OctetString
_SecondCallStatusEpId_Object=MibTableColumn
secondCallStatusEpId=_SecondCallStatusEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,300,1,100),_SecondCallStatusEpId_Type())
secondCallStatusEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:secondCallStatusEpId.setStatus(_A)
_SecondCallStatusState_Type=MxActivationState
_SecondCallStatusState_Object=MibTableColumn
secondCallStatusState=_SecondCallStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,500,300,1,200),_SecondCallStatusState_Type())
secondCallStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:secondCallStatusState.setStatus(_A)
_TransferGroup_ObjectIdentity=ObjectIdentity
transferGroup=_TransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600))
class _DefaultTransferBlindEnable_Type(MxEnableState):defaultValue=1
_DefaultTransferBlindEnable_Type.__name__=_D
_DefaultTransferBlindEnable_Object=MibScalar
defaultTransferBlindEnable=_DefaultTransferBlindEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,100),_DefaultTransferBlindEnable_Type())
defaultTransferBlindEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultTransferBlindEnable.setStatus(_A)
class _DefaultTransferAttendedEnable_Type(MxEnableState):defaultValue=1
_DefaultTransferAttendedEnable_Type.__name__=_D
_DefaultTransferAttendedEnable_Object=MibScalar
defaultTransferAttendedEnable=_DefaultTransferAttendedEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,200),_DefaultTransferAttendedEnable_Type())
defaultTransferAttendedEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultTransferAttendedEnable.setStatus(_A)
_EpSpecificTransferTable_Object=MibTable
epSpecificTransferTable=_EpSpecificTransferTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,300))
if mibBuilder.loadTexts:epSpecificTransferTable.setStatus(_A)
_EpSpecificTransferEntry_Object=MibTableRow
epSpecificTransferEntry=_EpSpecificTransferEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,300,1))
epSpecificTransferEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:epSpecificTransferEntry.setStatus(_A)
_EpSpecificTransferEpId_Type=OctetString
_EpSpecificTransferEpId_Object=MibTableColumn
epSpecificTransferEpId=_EpSpecificTransferEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,300,1,100),_EpSpecificTransferEpId_Type())
epSpecificTransferEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificTransferEpId.setStatus(_A)
class _EpSpecificTransferEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificTransferEnableConfig_Type.__name__=_D
_EpSpecificTransferEnableConfig_Object=MibTableColumn
epSpecificTransferEnableConfig=_EpSpecificTransferEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,300,1,200),_EpSpecificTransferEnableConfig_Type())
epSpecificTransferEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificTransferEnableConfig.setStatus(_A)
class _EpSpecificTransferBlindEnable_Type(MxEnableState):defaultValue=1
_EpSpecificTransferBlindEnable_Type.__name__=_D
_EpSpecificTransferBlindEnable_Object=MibTableColumn
epSpecificTransferBlindEnable=_EpSpecificTransferBlindEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,300,1,500),_EpSpecificTransferBlindEnable_Type())
epSpecificTransferBlindEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificTransferBlindEnable.setStatus(_A)
class _EpSpecificTransferAttendedEnable_Type(MxEnableState):defaultValue=1
_EpSpecificTransferAttendedEnable_Type.__name__=_D
_EpSpecificTransferAttendedEnable_Object=MibTableColumn
epSpecificTransferAttendedEnable=_EpSpecificTransferAttendedEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,300,1,600),_EpSpecificTransferAttendedEnable_Type())
epSpecificTransferAttendedEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificTransferAttendedEnable.setStatus(_A)
_TransferStatusTable_Object=MibTable
transferStatusTable=_TransferStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,400))
if mibBuilder.loadTexts:transferStatusTable.setStatus(_A)
_TransferStatusEntry_Object=MibTableRow
transferStatusEntry=_TransferStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,400,1))
transferStatusEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:transferStatusEntry.setStatus(_A)
_TransferStatusEpId_Type=OctetString
_TransferStatusEpId_Object=MibTableColumn
transferStatusEpId=_TransferStatusEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,400,1,100),_TransferStatusEpId_Type())
transferStatusEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:transferStatusEpId.setStatus(_A)
_TransferStatusBlindState_Type=MxActivationState
_TransferStatusBlindState_Object=MibTableColumn
transferStatusBlindState=_TransferStatusBlindState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,400,1,200),_TransferStatusBlindState_Type())
transferStatusBlindState.setMaxAccess(_C)
if mibBuilder.loadTexts:transferStatusBlindState.setStatus(_A)
_TransferStatusAttendedState_Type=MxActivationState
_TransferStatusAttendedState_Object=MibTableColumn
transferStatusAttendedState=_TransferStatusAttendedState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,600,400,1,300),_TransferStatusAttendedState_Type())
transferStatusAttendedState.setMaxAccess(_C)
if mibBuilder.loadTexts:transferStatusAttendedState.setStatus(_A)
_ConferenceGroup_ObjectIdentity=ObjectIdentity
conferenceGroup=_ConferenceGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700))
class _DefaultConferenceEnable_Type(MxEnableState):defaultValue=1
_DefaultConferenceEnable_Type.__name__=_D
_DefaultConferenceEnable_Object=MibScalar
defaultConferenceEnable=_DefaultConferenceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,100),_DefaultConferenceEnable_Type())
defaultConferenceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultConferenceEnable.setStatus(_A)
class _DefaultConferenceType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('local',100),(_c,200)))
_DefaultConferenceType_Type.__name__=_F
_DefaultConferenceType_Object=MibScalar
defaultConferenceType=_DefaultConferenceType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,150),_DefaultConferenceType_Type())
defaultConferenceType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultConferenceType.setStatus(_A)
_EpSpecificConferenceTable_Object=MibTable
epSpecificConferenceTable=_EpSpecificConferenceTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,200))
if mibBuilder.loadTexts:epSpecificConferenceTable.setStatus(_A)
_EpSpecificConferenceEntry_Object=MibTableRow
epSpecificConferenceEntry=_EpSpecificConferenceEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,200,1))
epSpecificConferenceEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:epSpecificConferenceEntry.setStatus(_A)
_EpSpecificConferenceEpId_Type=OctetString
_EpSpecificConferenceEpId_Object=MibTableColumn
epSpecificConferenceEpId=_EpSpecificConferenceEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,200,1,100),_EpSpecificConferenceEpId_Type())
epSpecificConferenceEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificConferenceEpId.setStatus(_A)
class _EpSpecificConferenceEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificConferenceEnableConfig_Type.__name__=_D
_EpSpecificConferenceEnableConfig_Object=MibTableColumn
epSpecificConferenceEnableConfig=_EpSpecificConferenceEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,200,1,200),_EpSpecificConferenceEnableConfig_Type())
epSpecificConferenceEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificConferenceEnableConfig.setStatus(_A)
class _EpSpecificConferenceEnable_Type(MxEnableState):defaultValue=1
_EpSpecificConferenceEnable_Type.__name__=_D
_EpSpecificConferenceEnable_Object=MibTableColumn
epSpecificConferenceEnable=_EpSpecificConferenceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,200,1,300),_EpSpecificConferenceEnable_Type())
epSpecificConferenceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificConferenceEnable.setStatus(_A)
class _EpSpecificConferenceType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('local',100),(_c,200)))
_EpSpecificConferenceType_Type.__name__=_F
_EpSpecificConferenceType_Object=MibTableColumn
epSpecificConferenceType=_EpSpecificConferenceType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,200,1,400),_EpSpecificConferenceType_Type())
epSpecificConferenceType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificConferenceType.setStatus(_A)
_ConferenceStatusTable_Object=MibTable
conferenceStatusTable=_ConferenceStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,300))
if mibBuilder.loadTexts:conferenceStatusTable.setStatus(_A)
_ConferenceStatusEntry_Object=MibTableRow
conferenceStatusEntry=_ConferenceStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,300,1))
conferenceStatusEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:conferenceStatusEntry.setStatus(_A)
_ConferenceStatusEpId_Type=OctetString
_ConferenceStatusEpId_Object=MibTableColumn
conferenceStatusEpId=_ConferenceStatusEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,300,1,100),_ConferenceStatusEpId_Type())
conferenceStatusEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:conferenceStatusEpId.setStatus(_A)
_ConferenceStatusState_Type=MxActivationState
_ConferenceStatusState_Object=MibTableColumn
conferenceStatusState=_ConferenceStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,700,300,1,200),_ConferenceStatusState_Type())
conferenceStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:conferenceStatusState.setStatus(_A)
_ForwardGroup_ObjectIdentity=ObjectIdentity
forwardGroup=_ForwardGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800))
_ForwardUnconditionalGroup_ObjectIdentity=ObjectIdentity
forwardUnconditionalGroup=_ForwardUnconditionalGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100))
class _DefaultForwardUnconditionalEnable_Type(MxEnableState):defaultValue=0
_DefaultForwardUnconditionalEnable_Type.__name__=_D
_DefaultForwardUnconditionalEnable_Object=MibScalar
defaultForwardUnconditionalEnable=_DefaultForwardUnconditionalEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,100),_DefaultForwardUnconditionalEnable_Type())
defaultForwardUnconditionalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardUnconditionalEnable.setStatus(_A)
class _DefaultForwardUnconditionalDtmfMapActivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultForwardUnconditionalDtmfMapActivation_Type.__name__=_G
_DefaultForwardUnconditionalDtmfMapActivation_Object=MibScalar
defaultForwardUnconditionalDtmfMapActivation=_DefaultForwardUnconditionalDtmfMapActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,200),_DefaultForwardUnconditionalDtmfMapActivation_Type())
defaultForwardUnconditionalDtmfMapActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardUnconditionalDtmfMapActivation.setStatus(_A)
class _DefaultForwardUnconditionalDtmfMapDeactivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultForwardUnconditionalDtmfMapDeactivation_Type.__name__=_G
_DefaultForwardUnconditionalDtmfMapDeactivation_Object=MibScalar
defaultForwardUnconditionalDtmfMapDeactivation=_DefaultForwardUnconditionalDtmfMapDeactivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,300),_DefaultForwardUnconditionalDtmfMapDeactivation_Type())
defaultForwardUnconditionalDtmfMapDeactivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardUnconditionalDtmfMapDeactivation.setStatus(_A)
_EpSpecificForwardUnconditionalTable_Object=MibTable
epSpecificForwardUnconditionalTable=_EpSpecificForwardUnconditionalTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,400))
if mibBuilder.loadTexts:epSpecificForwardUnconditionalTable.setStatus(_A)
_EpSpecificForwardUnconditionalEntry_Object=MibTableRow
epSpecificForwardUnconditionalEntry=_EpSpecificForwardUnconditionalEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,400,1))
epSpecificForwardUnconditionalEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:epSpecificForwardUnconditionalEntry.setStatus(_A)
_EpSpecificForwardUnconditionalEpId_Type=OctetString
_EpSpecificForwardUnconditionalEpId_Object=MibTableColumn
epSpecificForwardUnconditionalEpId=_EpSpecificForwardUnconditionalEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,400,1,100),_EpSpecificForwardUnconditionalEpId_Type())
epSpecificForwardUnconditionalEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificForwardUnconditionalEpId.setStatus(_A)
class _EpSpecificForwardUnconditionalEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificForwardUnconditionalEnableConfig_Type.__name__=_D
_EpSpecificForwardUnconditionalEnableConfig_Object=MibTableColumn
epSpecificForwardUnconditionalEnableConfig=_EpSpecificForwardUnconditionalEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,400,1,200),_EpSpecificForwardUnconditionalEnableConfig_Type())
epSpecificForwardUnconditionalEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardUnconditionalEnableConfig.setStatus(_A)
class _EpSpecificForwardUnconditionalEnable_Type(MxEnableState):defaultValue=0
_EpSpecificForwardUnconditionalEnable_Type.__name__=_D
_EpSpecificForwardUnconditionalEnable_Object=MibTableColumn
epSpecificForwardUnconditionalEnable=_EpSpecificForwardUnconditionalEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,400,1,300),_EpSpecificForwardUnconditionalEnable_Type())
epSpecificForwardUnconditionalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardUnconditionalEnable.setStatus(_A)
_ForwardUnconditionalConfigTable_Object=MibTable
forwardUnconditionalConfigTable=_ForwardUnconditionalConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,500))
if mibBuilder.loadTexts:forwardUnconditionalConfigTable.setStatus(_A)
_ForwardUnconditionalConfigEntry_Object=MibTableRow
forwardUnconditionalConfigEntry=_ForwardUnconditionalConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,500,1))
forwardUnconditionalConfigEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:forwardUnconditionalConfigEntry.setStatus(_A)
_ForwardUnconditionalConfigEpId_Type=OctetString
_ForwardUnconditionalConfigEpId_Object=MibTableColumn
forwardUnconditionalConfigEpId=_ForwardUnconditionalConfigEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,500,1,100),_ForwardUnconditionalConfigEpId_Type())
forwardUnconditionalConfigEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:forwardUnconditionalConfigEpId.setStatus(_A)
class _ForwardUnconditionalConfigActivation_Type(MxActivationState):defaultValue=0
_ForwardUnconditionalConfigActivation_Type.__name__=_J
_ForwardUnconditionalConfigActivation_Object=MibTableColumn
forwardUnconditionalConfigActivation=_ForwardUnconditionalConfigActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,500,1,200),_ForwardUnconditionalConfigActivation_Type())
forwardUnconditionalConfigActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:forwardUnconditionalConfigActivation.setStatus(_A)
class _ForwardUnconditionalConfigForwardingAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ForwardUnconditionalConfigForwardingAddress_Type.__name__=_I
_ForwardUnconditionalConfigForwardingAddress_Object=MibTableColumn
forwardUnconditionalConfigForwardingAddress=_ForwardUnconditionalConfigForwardingAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,100,500,1,300),_ForwardUnconditionalConfigForwardingAddress_Type())
forwardUnconditionalConfigForwardingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:forwardUnconditionalConfigForwardingAddress.setStatus(_A)
_ForwardOnBusyGroup_ObjectIdentity=ObjectIdentity
forwardOnBusyGroup=_ForwardOnBusyGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200))
class _DefaultForwardOnBusyEnable_Type(MxEnableState):defaultValue=0
_DefaultForwardOnBusyEnable_Type.__name__=_D
_DefaultForwardOnBusyEnable_Object=MibScalar
defaultForwardOnBusyEnable=_DefaultForwardOnBusyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,100),_DefaultForwardOnBusyEnable_Type())
defaultForwardOnBusyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardOnBusyEnable.setStatus(_A)
class _DefaultForwardOnBusyDtmfMapActivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultForwardOnBusyDtmfMapActivation_Type.__name__=_G
_DefaultForwardOnBusyDtmfMapActivation_Object=MibScalar
defaultForwardOnBusyDtmfMapActivation=_DefaultForwardOnBusyDtmfMapActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,300),_DefaultForwardOnBusyDtmfMapActivation_Type())
defaultForwardOnBusyDtmfMapActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardOnBusyDtmfMapActivation.setStatus(_A)
class _DefaultForwardOnBusyDtmfMapDeactivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultForwardOnBusyDtmfMapDeactivation_Type.__name__=_G
_DefaultForwardOnBusyDtmfMapDeactivation_Object=MibScalar
defaultForwardOnBusyDtmfMapDeactivation=_DefaultForwardOnBusyDtmfMapDeactivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,400),_DefaultForwardOnBusyDtmfMapDeactivation_Type())
defaultForwardOnBusyDtmfMapDeactivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardOnBusyDtmfMapDeactivation.setStatus(_A)
_EpSpecificForwardOnBusyTable_Object=MibTable
epSpecificForwardOnBusyTable=_EpSpecificForwardOnBusyTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,500))
if mibBuilder.loadTexts:epSpecificForwardOnBusyTable.setStatus(_A)
_EpSpecificForwardOnBusyEntry_Object=MibTableRow
epSpecificForwardOnBusyEntry=_EpSpecificForwardOnBusyEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,500,1))
epSpecificForwardOnBusyEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:epSpecificForwardOnBusyEntry.setStatus(_A)
_EpSpecificForwardOnBusyEpId_Type=OctetString
_EpSpecificForwardOnBusyEpId_Object=MibTableColumn
epSpecificForwardOnBusyEpId=_EpSpecificForwardOnBusyEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,500,1,100),_EpSpecificForwardOnBusyEpId_Type())
epSpecificForwardOnBusyEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificForwardOnBusyEpId.setStatus(_A)
class _EpSpecificForwardOnBusyEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificForwardOnBusyEnableConfig_Type.__name__=_D
_EpSpecificForwardOnBusyEnableConfig_Object=MibTableColumn
epSpecificForwardOnBusyEnableConfig=_EpSpecificForwardOnBusyEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,500,1,200),_EpSpecificForwardOnBusyEnableConfig_Type())
epSpecificForwardOnBusyEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardOnBusyEnableConfig.setStatus(_A)
class _EpSpecificForwardOnBusyEnable_Type(MxEnableState):defaultValue=0
_EpSpecificForwardOnBusyEnable_Type.__name__=_D
_EpSpecificForwardOnBusyEnable_Object=MibTableColumn
epSpecificForwardOnBusyEnable=_EpSpecificForwardOnBusyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,500,1,300),_EpSpecificForwardOnBusyEnable_Type())
epSpecificForwardOnBusyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardOnBusyEnable.setStatus(_A)
_ForwardOnBusyConfigTable_Object=MibTable
forwardOnBusyConfigTable=_ForwardOnBusyConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,600))
if mibBuilder.loadTexts:forwardOnBusyConfigTable.setStatus(_A)
_ForwardOnBusyConfigEntry_Object=MibTableRow
forwardOnBusyConfigEntry=_ForwardOnBusyConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,600,1))
forwardOnBusyConfigEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:forwardOnBusyConfigEntry.setStatus(_A)
_ForwardOnBusyConfigEpId_Type=OctetString
_ForwardOnBusyConfigEpId_Object=MibTableColumn
forwardOnBusyConfigEpId=_ForwardOnBusyConfigEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,600,1,100),_ForwardOnBusyConfigEpId_Type())
forwardOnBusyConfigEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:forwardOnBusyConfigEpId.setStatus(_A)
class _ForwardOnBusyConfigActivation_Type(MxActivationState):defaultValue=0
_ForwardOnBusyConfigActivation_Type.__name__=_J
_ForwardOnBusyConfigActivation_Object=MibTableColumn
forwardOnBusyConfigActivation=_ForwardOnBusyConfigActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,600,1,200),_ForwardOnBusyConfigActivation_Type())
forwardOnBusyConfigActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:forwardOnBusyConfigActivation.setStatus(_A)
class _ForwardOnBusyConfigForwardingAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ForwardOnBusyConfigForwardingAddress_Type.__name__=_I
_ForwardOnBusyConfigForwardingAddress_Object=MibTableColumn
forwardOnBusyConfigForwardingAddress=_ForwardOnBusyConfigForwardingAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,200,600,1,300),_ForwardOnBusyConfigForwardingAddress_Type())
forwardOnBusyConfigForwardingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:forwardOnBusyConfigForwardingAddress.setStatus(_A)
_ForwardNoAnswerGroup_ObjectIdentity=ObjectIdentity
forwardNoAnswerGroup=_ForwardNoAnswerGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300))
class _DefaultForwardNoAnswerEnable_Type(MxEnableState):defaultValue=0
_DefaultForwardNoAnswerEnable_Type.__name__=_D
_DefaultForwardNoAnswerEnable_Object=MibScalar
defaultForwardNoAnswerEnable=_DefaultForwardNoAnswerEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,100),_DefaultForwardNoAnswerEnable_Type())
defaultForwardNoAnswerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardNoAnswerEnable.setStatus(_A)
class _DefaultForwardNoAnswerTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,120000))
_DefaultForwardNoAnswerTimeout_Type.__name__=_H
_DefaultForwardNoAnswerTimeout_Object=MibScalar
defaultForwardNoAnswerTimeout=_DefaultForwardNoAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,200),_DefaultForwardNoAnswerTimeout_Type())
defaultForwardNoAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardNoAnswerTimeout.setStatus(_A)
class _DefaultForwardNoAnswerDtmfMapActivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultForwardNoAnswerDtmfMapActivation_Type.__name__=_G
_DefaultForwardNoAnswerDtmfMapActivation_Object=MibScalar
defaultForwardNoAnswerDtmfMapActivation=_DefaultForwardNoAnswerDtmfMapActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,300),_DefaultForwardNoAnswerDtmfMapActivation_Type())
defaultForwardNoAnswerDtmfMapActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardNoAnswerDtmfMapActivation.setStatus(_A)
class _DefaultForwardNoAnswerDtmfMapDeactivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultForwardNoAnswerDtmfMapDeactivation_Type.__name__=_G
_DefaultForwardNoAnswerDtmfMapDeactivation_Object=MibScalar
defaultForwardNoAnswerDtmfMapDeactivation=_DefaultForwardNoAnswerDtmfMapDeactivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,400),_DefaultForwardNoAnswerDtmfMapDeactivation_Type())
defaultForwardNoAnswerDtmfMapDeactivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultForwardNoAnswerDtmfMapDeactivation.setStatus(_A)
_EpSpecificForwardNoAnswerTable_Object=MibTable
epSpecificForwardNoAnswerTable=_EpSpecificForwardNoAnswerTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,500))
if mibBuilder.loadTexts:epSpecificForwardNoAnswerTable.setStatus(_A)
_EpSpecificForwardNoAnswerEntry_Object=MibTableRow
epSpecificForwardNoAnswerEntry=_EpSpecificForwardNoAnswerEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,500,1))
epSpecificForwardNoAnswerEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:epSpecificForwardNoAnswerEntry.setStatus(_A)
_EpSpecificForwardNoAnswerEpId_Type=OctetString
_EpSpecificForwardNoAnswerEpId_Object=MibTableColumn
epSpecificForwardNoAnswerEpId=_EpSpecificForwardNoAnswerEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,500,1,100),_EpSpecificForwardNoAnswerEpId_Type())
epSpecificForwardNoAnswerEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificForwardNoAnswerEpId.setStatus(_A)
class _EpSpecificForwardNoAnswerEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificForwardNoAnswerEnableConfig_Type.__name__=_D
_EpSpecificForwardNoAnswerEnableConfig_Object=MibTableColumn
epSpecificForwardNoAnswerEnableConfig=_EpSpecificForwardNoAnswerEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,500,1,200),_EpSpecificForwardNoAnswerEnableConfig_Type())
epSpecificForwardNoAnswerEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardNoAnswerEnableConfig.setStatus(_A)
class _EpSpecificForwardNoAnswerEnable_Type(MxEnableState):defaultValue=0
_EpSpecificForwardNoAnswerEnable_Type.__name__=_D
_EpSpecificForwardNoAnswerEnable_Object=MibTableColumn
epSpecificForwardNoAnswerEnable=_EpSpecificForwardNoAnswerEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,500,1,300),_EpSpecificForwardNoAnswerEnable_Type())
epSpecificForwardNoAnswerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardNoAnswerEnable.setStatus(_A)
class _EpSpecificForwardNoAnswerTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,120000))
_EpSpecificForwardNoAnswerTimeout_Type.__name__=_H
_EpSpecificForwardNoAnswerTimeout_Object=MibTableColumn
epSpecificForwardNoAnswerTimeout=_EpSpecificForwardNoAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,500,1,400),_EpSpecificForwardNoAnswerTimeout_Type())
epSpecificForwardNoAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificForwardNoAnswerTimeout.setStatus(_A)
_ForwardNoAnswerConfigTable_Object=MibTable
forwardNoAnswerConfigTable=_ForwardNoAnswerConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,600))
if mibBuilder.loadTexts:forwardNoAnswerConfigTable.setStatus(_A)
_ForwardNoAnswerConfigEntry_Object=MibTableRow
forwardNoAnswerConfigEntry=_ForwardNoAnswerConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,600,1))
forwardNoAnswerConfigEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:forwardNoAnswerConfigEntry.setStatus(_A)
_ForwardNoAnswerConfigEpId_Type=OctetString
_ForwardNoAnswerConfigEpId_Object=MibTableColumn
forwardNoAnswerConfigEpId=_ForwardNoAnswerConfigEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,600,1,100),_ForwardNoAnswerConfigEpId_Type())
forwardNoAnswerConfigEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:forwardNoAnswerConfigEpId.setStatus(_A)
class _ForwardNoAnswerConfigActivation_Type(MxActivationState):defaultValue=0
_ForwardNoAnswerConfigActivation_Type.__name__=_J
_ForwardNoAnswerConfigActivation_Object=MibTableColumn
forwardNoAnswerConfigActivation=_ForwardNoAnswerConfigActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,600,1,200),_ForwardNoAnswerConfigActivation_Type())
forwardNoAnswerConfigActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:forwardNoAnswerConfigActivation.setStatus(_A)
class _ForwardNoAnswerConfigForwardingAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ForwardNoAnswerConfigForwardingAddress_Type.__name__=_I
_ForwardNoAnswerConfigForwardingAddress_Object=MibTableColumn
forwardNoAnswerConfigForwardingAddress=_ForwardNoAnswerConfigForwardingAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,800,300,600,1,300),_ForwardNoAnswerConfigForwardingAddress_Type())
forwardNoAnswerConfigForwardingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:forwardNoAnswerConfigForwardingAddress.setStatus(_A)
_CallCompletionGroup_ObjectIdentity=ObjectIdentity
callCompletionGroup=_CallCompletionGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900))
class _DefaultCallCompletionBusySubscriberEnable_Type(MxEnableState):defaultValue=0
_DefaultCallCompletionBusySubscriberEnable_Type.__name__=_D
_DefaultCallCompletionBusySubscriberEnable_Object=MibScalar
defaultCallCompletionBusySubscriberEnable=_DefaultCallCompletionBusySubscriberEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,100),_DefaultCallCompletionBusySubscriberEnable_Type())
defaultCallCompletionBusySubscriberEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionBusySubscriberEnable.setStatus(_A)
class _DefaultCallCompletionBusySubscriberDtmfMapActivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultCallCompletionBusySubscriberDtmfMapActivation_Type.__name__=_G
_DefaultCallCompletionBusySubscriberDtmfMapActivation_Object=MibScalar
defaultCallCompletionBusySubscriberDtmfMapActivation=_DefaultCallCompletionBusySubscriberDtmfMapActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,200),_DefaultCallCompletionBusySubscriberDtmfMapActivation_Type())
defaultCallCompletionBusySubscriberDtmfMapActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionBusySubscriberDtmfMapActivation.setStatus(_A)
class _DefaultCallCompletionNoReplyEnable_Type(MxEnableState):defaultValue=0
_DefaultCallCompletionNoReplyEnable_Type.__name__=_D
_DefaultCallCompletionNoReplyEnable_Object=MibScalar
defaultCallCompletionNoReplyEnable=_DefaultCallCompletionNoReplyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,300),_DefaultCallCompletionNoReplyEnable_Type())
defaultCallCompletionNoReplyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionNoReplyEnable.setStatus(_A)
class _DefaultCallCompletionNoReplyDtmfMapActivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultCallCompletionNoReplyDtmfMapActivation_Type.__name__=_G
_DefaultCallCompletionNoReplyDtmfMapActivation_Object=MibScalar
defaultCallCompletionNoReplyDtmfMapActivation=_DefaultCallCompletionNoReplyDtmfMapActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,400),_DefaultCallCompletionNoReplyDtmfMapActivation_Type())
defaultCallCompletionNoReplyDtmfMapActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionNoReplyDtmfMapActivation.setStatus(_A)
class _DefaultCallCompletionDtmfMapDeactivation_Type(MxDigitMap):defaultValue=OctetString('')
_DefaultCallCompletionDtmfMapDeactivation_Type.__name__=_G
_DefaultCallCompletionDtmfMapDeactivation_Object=MibScalar
defaultCallCompletionDtmfMapDeactivation=_DefaultCallCompletionDtmfMapDeactivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,500),_DefaultCallCompletionDtmfMapDeactivation_Type())
defaultCallCompletionDtmfMapDeactivation.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionDtmfMapDeactivation.setStatus(_A)
class _DefaultCallCompletionExpirationTimeout_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_DefaultCallCompletionExpirationTimeout_Type.__name__=_H
_DefaultCallCompletionExpirationTimeout_Object=MibScalar
defaultCallCompletionExpirationTimeout=_DefaultCallCompletionExpirationTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,600),_DefaultCallCompletionExpirationTimeout_Type())
defaultCallCompletionExpirationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionExpirationTimeout.setStatus(_A)
class _DefaultCallCompletionMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('monitoringOnly',100),('monitoringAndPolling',200)))
_DefaultCallCompletionMethod_Type.__name__=_F
_DefaultCallCompletionMethod_Object=MibScalar
defaultCallCompletionMethod=_DefaultCallCompletionMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,650),_DefaultCallCompletionMethod_Type())
defaultCallCompletionMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionMethod.setStatus(_A)
class _DefaultCallCompletionAutoReactivateEnable_Type(MxEnableState):defaultValue=0
_DefaultCallCompletionAutoReactivateEnable_Type.__name__=_D
_DefaultCallCompletionAutoReactivateEnable_Object=MibScalar
defaultCallCompletionAutoReactivateEnable=_DefaultCallCompletionAutoReactivateEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,700),_DefaultCallCompletionAutoReactivateEnable_Type())
defaultCallCompletionAutoReactivateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionAutoReactivateEnable.setStatus(_A)
class _DefaultCallCompletionAutoReactivateDelay_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_DefaultCallCompletionAutoReactivateDelay_Type.__name__=_H
_DefaultCallCompletionAutoReactivateDelay_Object=MibScalar
defaultCallCompletionAutoReactivateDelay=_DefaultCallCompletionAutoReactivateDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,750),_DefaultCallCompletionAutoReactivateDelay_Type())
defaultCallCompletionAutoReactivateDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionAutoReactivateDelay.setStatus(_A)
class _DefaultCallCompletionEarlyMediaBehaviour_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('none',100),('ccbs',200),('ccnr',300)))
_DefaultCallCompletionEarlyMediaBehaviour_Type.__name__=_F
_DefaultCallCompletionEarlyMediaBehaviour_Object=MibScalar
defaultCallCompletionEarlyMediaBehaviour=_DefaultCallCompletionEarlyMediaBehaviour_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,775),_DefaultCallCompletionEarlyMediaBehaviour_Type())
defaultCallCompletionEarlyMediaBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionEarlyMediaBehaviour.setStatus(_A)
_EpSpecificCallCompletionTable_Object=MibTable
epSpecificCallCompletionTable=_EpSpecificCallCompletionTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,800))
if mibBuilder.loadTexts:epSpecificCallCompletionTable.setStatus(_A)
_EpSpecificCallCompletionEntry_Object=MibTableRow
epSpecificCallCompletionEntry=_EpSpecificCallCompletionEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,800,1))
epSpecificCallCompletionEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:epSpecificCallCompletionEntry.setStatus(_A)
_EpSpecificCallCompletionEpId_Type=OctetString
_EpSpecificCallCompletionEpId_Object=MibTableColumn
epSpecificCallCompletionEpId=_EpSpecificCallCompletionEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,800,1,100),_EpSpecificCallCompletionEpId_Type())
epSpecificCallCompletionEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificCallCompletionEpId.setStatus(_A)
class _EpSpecificCallCompletionEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCallCompletionEnableConfig_Type.__name__=_D
_EpSpecificCallCompletionEnableConfig_Object=MibTableColumn
epSpecificCallCompletionEnableConfig=_EpSpecificCallCompletionEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,800,1,200),_EpSpecificCallCompletionEnableConfig_Type())
epSpecificCallCompletionEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallCompletionEnableConfig.setStatus(_A)
class _EpSpecificCallCompletionBusySubscriberEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCallCompletionBusySubscriberEnable_Type.__name__=_D
_EpSpecificCallCompletionBusySubscriberEnable_Object=MibTableColumn
epSpecificCallCompletionBusySubscriberEnable=_EpSpecificCallCompletionBusySubscriberEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,800,1,300),_EpSpecificCallCompletionBusySubscriberEnable_Type())
epSpecificCallCompletionBusySubscriberEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallCompletionBusySubscriberEnable.setStatus(_A)
class _EpSpecificCallCompletionNoReplyEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCallCompletionNoReplyEnable_Type.__name__=_D
_EpSpecificCallCompletionNoReplyEnable_Object=MibTableColumn
epSpecificCallCompletionNoReplyEnable=_EpSpecificCallCompletionNoReplyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,800,1,400),_EpSpecificCallCompletionNoReplyEnable_Type())
epSpecificCallCompletionNoReplyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCallCompletionNoReplyEnable.setStatus(_A)
_CallCompletionConfigTable_Object=MibTable
callCompletionConfigTable=_CallCompletionConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900))
if mibBuilder.loadTexts:callCompletionConfigTable.setStatus(_A)
_CallCompletionConfigEntry_Object=MibTableRow
callCompletionConfigEntry=_CallCompletionConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900,1))
callCompletionConfigEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:callCompletionConfigEntry.setStatus(_A)
_CallCompletionConfigIndex_Type=Unsigned32
_CallCompletionConfigIndex_Object=MibTableColumn
callCompletionConfigIndex=_CallCompletionConfigIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900,1,100),_CallCompletionConfigIndex_Type())
callCompletionConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:callCompletionConfigIndex.setStatus(_A)
_CallCompletionConfigEpId_Type=OctetString
_CallCompletionConfigEpId_Object=MibTableColumn
callCompletionConfigEpId=_CallCompletionConfigEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900,1,200),_CallCompletionConfigEpId_Type())
callCompletionConfigEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:callCompletionConfigEpId.setStatus(_A)
class _CallCompletionConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('ccbs',100),('ccnr',200)))
_CallCompletionConfigType_Type.__name__=_F
_CallCompletionConfigType_Object=MibTableColumn
callCompletionConfigType=_CallCompletionConfigType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900,1,300),_CallCompletionConfigType_Type())
callCompletionConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:callCompletionConfigType.setStatus(_A)
_CallCompletionConfigTargetAddress_Type=OctetString
_CallCompletionConfigTargetAddress_Object=MibTableColumn
callCompletionConfigTargetAddress=_CallCompletionConfigTargetAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900,1,400),_CallCompletionConfigTargetAddress_Type())
callCompletionConfigTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:callCompletionConfigTargetAddress.setStatus(_A)
class _CallCompletionConfigTargetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('unknown',100),('idle',200),('busy',300)))
_CallCompletionConfigTargetState_Type.__name__=_F
_CallCompletionConfigTargetState_Object=MibTableColumn
callCompletionConfigTargetState=_CallCompletionConfigTargetState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,900,1,500),_CallCompletionConfigTargetState_Type())
callCompletionConfigTargetState.setMaxAccess(_C)
if mibBuilder.loadTexts:callCompletionConfigTargetState.setStatus(_A)
_CallCompletionPollingGroup_ObjectIdentity=ObjectIdentity
callCompletionPollingGroup=_CallCompletionPollingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,10000))
class _DefaultCallCompletionPollingInterval_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_DefaultCallCompletionPollingInterval_Type.__name__=_H
_DefaultCallCompletionPollingInterval_Object=MibScalar
defaultCallCompletionPollingInterval=_DefaultCallCompletionPollingInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,900,10000,780),_DefaultCallCompletionPollingInterval_Type())
defaultCallCompletionPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCallCompletionPollingInterval.setStatus(_A)
_DelayedHotlineGroup_ObjectIdentity=ObjectIdentity
delayedHotlineGroup=_DelayedHotlineGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000))
class _DefaultDelayedHotlineEnable_Type(MxEnableState):defaultValue=0
_DefaultDelayedHotlineEnable_Type.__name__=_D
_DefaultDelayedHotlineEnable_Object=MibScalar
defaultDelayedHotlineEnable=_DefaultDelayedHotlineEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,100),_DefaultDelayedHotlineEnable_Type())
defaultDelayedHotlineEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDelayedHotlineEnable.setStatus(_A)
class _DefaultDelayedHotlineCondition_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_n,100),(_o,200),(_p,300)))
_DefaultDelayedHotlineCondition_Type.__name__=_F
_DefaultDelayedHotlineCondition_Object=MibScalar
defaultDelayedHotlineCondition=_DefaultDelayedHotlineCondition_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,200),_DefaultDelayedHotlineCondition_Type())
defaultDelayedHotlineCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDelayedHotlineCondition.setStatus(_A)
class _DefaultDelayedHotlineTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_DefaultDelayedHotlineTargetAddress_Type.__name__=_I
_DefaultDelayedHotlineTargetAddress_Object=MibScalar
defaultDelayedHotlineTargetAddress=_DefaultDelayedHotlineTargetAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,300),_DefaultDelayedHotlineTargetAddress_Type())
defaultDelayedHotlineTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDelayedHotlineTargetAddress.setStatus(_A)
_EpSpecificDelayedHotlineTable_Object=MibTable
epSpecificDelayedHotlineTable=_EpSpecificDelayedHotlineTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000))
if mibBuilder.loadTexts:epSpecificDelayedHotlineTable.setStatus(_A)
_EpSpecificDelayedHotlineEntry_Object=MibTableRow
epSpecificDelayedHotlineEntry=_EpSpecificDelayedHotlineEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000,1))
epSpecificDelayedHotlineEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:epSpecificDelayedHotlineEntry.setStatus(_A)
_EpSpecificDelayedHotlineEpId_Type=OctetString
_EpSpecificDelayedHotlineEpId_Object=MibTableColumn
epSpecificDelayedHotlineEpId=_EpSpecificDelayedHotlineEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000,1,100),_EpSpecificDelayedHotlineEpId_Type())
epSpecificDelayedHotlineEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificDelayedHotlineEpId.setStatus(_A)
class _EpSpecificDelayedHotlineEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificDelayedHotlineEnableConfig_Type.__name__=_D
_EpSpecificDelayedHotlineEnableConfig_Object=MibTableColumn
epSpecificDelayedHotlineEnableConfig=_EpSpecificDelayedHotlineEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000,1,200),_EpSpecificDelayedHotlineEnableConfig_Type())
epSpecificDelayedHotlineEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDelayedHotlineEnableConfig.setStatus(_A)
class _EpSpecificDelayedHotlineEnable_Type(MxEnableState):defaultValue=0
_EpSpecificDelayedHotlineEnable_Type.__name__=_D
_EpSpecificDelayedHotlineEnable_Object=MibTableColumn
epSpecificDelayedHotlineEnable=_EpSpecificDelayedHotlineEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000,1,300),_EpSpecificDelayedHotlineEnable_Type())
epSpecificDelayedHotlineEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDelayedHotlineEnable.setStatus(_A)
class _EpSpecificDelayedHotlineCondition_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_n,100),(_o,200),(_p,300)))
_EpSpecificDelayedHotlineCondition_Type.__name__=_F
_EpSpecificDelayedHotlineCondition_Object=MibTableColumn
epSpecificDelayedHotlineCondition=_EpSpecificDelayedHotlineCondition_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000,1,400),_EpSpecificDelayedHotlineCondition_Type())
epSpecificDelayedHotlineCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDelayedHotlineCondition.setStatus(_A)
class _EpSpecificDelayedHotlineTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_EpSpecificDelayedHotlineTargetAddress_Type.__name__=_I
_EpSpecificDelayedHotlineTargetAddress_Object=MibTableColumn
epSpecificDelayedHotlineTargetAddress=_EpSpecificDelayedHotlineTargetAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1000,1000,1,500),_EpSpecificDelayedHotlineTargetAddress_Type())
epSpecificDelayedHotlineTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDelayedHotlineTargetAddress.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200))
_CallStatisticsTable_Object=MibTable
callStatisticsTable=_CallStatisticsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100))
if mibBuilder.loadTexts:callStatisticsTable.setStatus(_A)
_CallStatisticsEntry_Object=MibTableRow
callStatisticsEntry=_CallStatisticsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1))
callStatisticsEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:callStatisticsEntry.setStatus(_A)
_CallStatisticsEpId_Type=OctetString
_CallStatisticsEpId_Object=MibTableColumn
callStatisticsEpId=_CallStatisticsEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,100),_CallStatisticsEpId_Type())
callStatisticsEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsEpId.setStatus(_A)
_CallStatisticsIncomingCallsReceived_Type=Unsigned32
_CallStatisticsIncomingCallsReceived_Object=MibTableColumn
callStatisticsIncomingCallsReceived=_CallStatisticsIncomingCallsReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,200),_CallStatisticsIncomingCallsReceived_Type())
callStatisticsIncomingCallsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsIncomingCallsReceived.setStatus(_A)
_CallStatisticsIncomingCallsAnswered_Type=Unsigned32
_CallStatisticsIncomingCallsAnswered_Object=MibTableColumn
callStatisticsIncomingCallsAnswered=_CallStatisticsIncomingCallsAnswered_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,300),_CallStatisticsIncomingCallsAnswered_Type())
callStatisticsIncomingCallsAnswered.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsIncomingCallsAnswered.setStatus(_A)
_CallStatisticsIncomingCallsConnected_Type=Unsigned32
_CallStatisticsIncomingCallsConnected_Object=MibTableColumn
callStatisticsIncomingCallsConnected=_CallStatisticsIncomingCallsConnected_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,400),_CallStatisticsIncomingCallsConnected_Type())
callStatisticsIncomingCallsConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsIncomingCallsConnected.setStatus(_A)
_CallStatisticsIncomingCallsFailed_Type=Unsigned32
_CallStatisticsIncomingCallsFailed_Object=MibTableColumn
callStatisticsIncomingCallsFailed=_CallStatisticsIncomingCallsFailed_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,500),_CallStatisticsIncomingCallsFailed_Type())
callStatisticsIncomingCallsFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsIncomingCallsFailed.setStatus(_A)
_CallStatisticsOutgoingCallsAttempted_Type=Unsigned32
_CallStatisticsOutgoingCallsAttempted_Object=MibTableColumn
callStatisticsOutgoingCallsAttempted=_CallStatisticsOutgoingCallsAttempted_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,600),_CallStatisticsOutgoingCallsAttempted_Type())
callStatisticsOutgoingCallsAttempted.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsOutgoingCallsAttempted.setStatus(_A)
_CallStatisticsOutgoingCallsAnswered_Type=Unsigned32
_CallStatisticsOutgoingCallsAnswered_Object=MibTableColumn
callStatisticsOutgoingCallsAnswered=_CallStatisticsOutgoingCallsAnswered_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,700),_CallStatisticsOutgoingCallsAnswered_Type())
callStatisticsOutgoingCallsAnswered.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsOutgoingCallsAnswered.setStatus(_A)
_CallStatisticsOutgoingCallsConnected_Type=Unsigned32
_CallStatisticsOutgoingCallsConnected_Object=MibTableColumn
callStatisticsOutgoingCallsConnected=_CallStatisticsOutgoingCallsConnected_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,800),_CallStatisticsOutgoingCallsConnected_Type())
callStatisticsOutgoingCallsConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsOutgoingCallsConnected.setStatus(_A)
_CallStatisticsOutgoingCallsFailed_Type=Unsigned32
_CallStatisticsOutgoingCallsFailed_Object=MibTableColumn
callStatisticsOutgoingCallsFailed=_CallStatisticsOutgoingCallsFailed_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,900),_CallStatisticsOutgoingCallsFailed_Type())
callStatisticsOutgoingCallsFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsOutgoingCallsFailed.setStatus(_A)
_CallStatisticsCallsDropped_Type=Unsigned32
_CallStatisticsCallsDropped_Object=MibTableColumn
callStatisticsCallsDropped=_CallStatisticsCallsDropped_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,1000),_CallStatisticsCallsDropped_Type())
callStatisticsCallsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsCallsDropped.setStatus(_A)
_CallStatisticsTotalCallTime_Type=Unsigned32
_CallStatisticsTotalCallTime_Object=MibTableColumn
callStatisticsTotalCallTime=_CallStatisticsTotalCallTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,1100),_CallStatisticsTotalCallTime_Type())
callStatisticsTotalCallTime.setMaxAccess(_C)
if mibBuilder.loadTexts:callStatisticsTotalCallTime.setStatus(_A)
class _CallStatisticsReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('reset',10)))
_CallStatisticsReset_Type.__name__=_F
_CallStatisticsReset_Object=MibTableColumn
callStatisticsReset=_CallStatisticsReset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,1200,100,1,1200),_CallStatisticsReset_Type())
callStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:callStatisticsReset.setStatus(_A)
_DtmfMapGroup_ObjectIdentity=ObjectIdentity
dtmfMapGroup=_DtmfMapGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000))
class _DtmfMapTimeoutCompletion_Type(Unsigned32):defaultValue=60000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_DtmfMapTimeoutCompletion_Type.__name__=_H
_DtmfMapTimeoutCompletion_Object=MibScalar
dtmfMapTimeoutCompletion=_DtmfMapTimeoutCompletion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,100),_DtmfMapTimeoutCompletion_Type())
dtmfMapTimeoutCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmfMapTimeoutCompletion.setStatus(_A)
class _DtmfMapTimeoutFirstDtmf_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_DtmfMapTimeoutFirstDtmf_Type.__name__=_H
_DtmfMapTimeoutFirstDtmf_Object=MibScalar
dtmfMapTimeoutFirstDtmf=_DtmfMapTimeoutFirstDtmf_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,200),_DtmfMapTimeoutFirstDtmf_Type())
dtmfMapTimeoutFirstDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmfMapTimeoutFirstDtmf.setStatus(_A)
class _DtmfMapTimeoutInterDtmf_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_DtmfMapTimeoutInterDtmf_Type.__name__=_H
_DtmfMapTimeoutInterDtmf_Object=MibScalar
dtmfMapTimeoutInterDtmf=_DtmfMapTimeoutInterDtmf_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,300),_DtmfMapTimeoutInterDtmf_Type())
dtmfMapTimeoutInterDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmfMapTimeoutInterDtmf.setStatus(_A)
_EpSpecificDtmfMapTimeoutTable_Object=MibTable
epSpecificDtmfMapTimeoutTable=_EpSpecificDtmfMapTimeoutTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000))
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutTable.setStatus(_A)
_EpSpecificDtmfMapTimeoutEntry_Object=MibTableRow
epSpecificDtmfMapTimeoutEntry=_EpSpecificDtmfMapTimeoutEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000,1))
epSpecificDtmfMapTimeoutEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutEntry.setStatus(_A)
_EpSpecificDtmfMapTimeoutEpId_Type=OctetString
_EpSpecificDtmfMapTimeoutEpId_Object=MibTableColumn
epSpecificDtmfMapTimeoutEpId=_EpSpecificDtmfMapTimeoutEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000,1,100),_EpSpecificDtmfMapTimeoutEpId_Type())
epSpecificDtmfMapTimeoutEpId.setMaxAccess(_C)
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutEpId.setStatus(_A)
class _EpSpecificDtmfMapTimeoutEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificDtmfMapTimeoutEnableConfig_Type.__name__=_D
_EpSpecificDtmfMapTimeoutEnableConfig_Object=MibTableColumn
epSpecificDtmfMapTimeoutEnableConfig=_EpSpecificDtmfMapTimeoutEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000,1,200),_EpSpecificDtmfMapTimeoutEnableConfig_Type())
epSpecificDtmfMapTimeoutEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutEnableConfig.setStatus(_A)
class _EpSpecificDtmfMapTimeoutCompletion_Type(Unsigned32):defaultValue=60000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_EpSpecificDtmfMapTimeoutCompletion_Type.__name__=_H
_EpSpecificDtmfMapTimeoutCompletion_Object=MibTableColumn
epSpecificDtmfMapTimeoutCompletion=_EpSpecificDtmfMapTimeoutCompletion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000,1,300),_EpSpecificDtmfMapTimeoutCompletion_Type())
epSpecificDtmfMapTimeoutCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutCompletion.setStatus(_A)
class _EpSpecificDtmfMapTimeoutFirstDtmf_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_EpSpecificDtmfMapTimeoutFirstDtmf_Type.__name__=_H
_EpSpecificDtmfMapTimeoutFirstDtmf_Object=MibTableColumn
epSpecificDtmfMapTimeoutFirstDtmf=_EpSpecificDtmfMapTimeoutFirstDtmf_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000,1,400),_EpSpecificDtmfMapTimeoutFirstDtmf_Type())
epSpecificDtmfMapTimeoutFirstDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutFirstDtmf.setStatus(_A)
class _EpSpecificDtmfMapTimeoutInterDtmf_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_EpSpecificDtmfMapTimeoutInterDtmf_Type.__name__=_H
_EpSpecificDtmfMapTimeoutInterDtmf_Object=MibTableColumn
epSpecificDtmfMapTimeoutInterDtmf=_EpSpecificDtmfMapTimeoutInterDtmf_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,20000,1000,1,500),_EpSpecificDtmfMapTimeoutInterDtmf_Type())
epSpecificDtmfMapTimeoutInterDtmf.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfMapTimeoutInterDtmf.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_F
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_F
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1700,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'epServMIB':epServMIB,'epServMIBObjects':epServMIBObjects,'callGroup':callGroup,'defaultCallHookFlashProcessing':defaultCallHookFlashProcessing,'defaultCallAllowDirectIp':defaultCallAllowDirectIp,'epSpecificCallTable':epSpecificCallTable,'epSpecificCallEntry':epSpecificCallEntry,_N:epSpecificCallEpId,'epSpecificCallEnableConfig':epSpecificCallEnableConfig,'epSpecificCallHookFlashProcessing':epSpecificCallHookFlashProcessing,'callDtmfMapGroup':callDtmfMapGroup,'callDtmfMapAllowedTable':callDtmfMapAllowedTable,'callDtmfMapAllowedEntry':callDtmfMapAllowedEntry,_O:callDtmfMapAllowedIndex,'callDtmfMapAllowedEnable':callDtmfMapAllowedEnable,'callDtmfMapAllowedApplyTo':callDtmfMapAllowedApplyTo,'callDtmfMapAllowedEpId':callDtmfMapAllowedEpId,'callDtmfMapAllowedDtmfMap':callDtmfMapAllowedDtmfMap,'callDtmfMapAllowedDtmfTransformation':callDtmfMapAllowedDtmfTransformation,'callDtmfMapAllowedTargetHost':callDtmfMapAllowedTargetHost,'callDtmfMapAllowedEmergency':callDtmfMapAllowedEmergency,'callDtmfMapRefuseTable':callDtmfMapRefuseTable,'callDtmfMapRefuseEntry':callDtmfMapRefuseEntry,_Q:callDtmfMapRefuseIndex,'callDtmfMapRefuseEnable':callDtmfMapRefuseEnable,'callDtmfMapRefuseApplyTo':callDtmfMapRefuseApplyTo,'callDtmfMapRefuseEpId':callDtmfMapRefuseEpId,'callDtmfMapRefuseDtmfMap':callDtmfMapRefuseDtmfMap,'autoCallGroup':autoCallGroup,'defaultAutoCallEnable':defaultAutoCallEnable,'defaultAutoCallTargetAddress':defaultAutoCallTargetAddress,'epSpecificAutoCallTable':epSpecificAutoCallTable,'epSpecificAutoCallEntry':epSpecificAutoCallEntry,_R:epSpecificAutoCallEpId,'epSpecificAutoCallEnableConfig':epSpecificAutoCallEnableConfig,'epSpecificAutoCallEnable':epSpecificAutoCallEnable,'epSpecificAutoCallTargetAddress':epSpecificAutoCallTargetAddress,'holdGroup':holdGroup,'defaultHoldEnable':defaultHoldEnable,'epSpecificHoldTable':epSpecificHoldTable,'epSpecificHoldEntry':epSpecificHoldEntry,_S:epSpecificHoldEpId,'epSpecificHoldEnableConfig':epSpecificHoldEnableConfig,'epSpecificHoldEnable':epSpecificHoldEnable,'holdStatusTable':holdStatusTable,'holdStatusEntry':holdStatusEntry,_T:holdStatusEpId,'holdStatusState':holdStatusState,'callWaitingGroup':callWaitingGroup,'defaultCallWaitingEnable':defaultCallWaitingEnable,'defaultCallWaitingCancelDtmfMap':defaultCallWaitingCancelDtmfMap,'defaultCallWaitingActivationDtmfMap':defaultCallWaitingActivationDtmfMap,'defaultCallWaitingDeactivationDtmfMap':defaultCallWaitingDeactivationDtmfMap,'epSpecificCallWaitingTable':epSpecificCallWaitingTable,'epSpecificCallWaitingEntry':epSpecificCallWaitingEntry,_U:epSpecificCallWaitingEpId,'epSpecificCallWaitingEnableConfig':epSpecificCallWaitingEnableConfig,'epSpecificCallWaitingEnable':epSpecificCallWaitingEnable,'callWaitingStatusTable':callWaitingStatusTable,'callWaitingStatusEntry':callWaitingStatusEntry,_V:callWaitingStatusEpId,'callWaitingStatusState':callWaitingStatusState,'callWaitingUserConfigTable':callWaitingUserConfigTable,'callWaitingUserConfigEntry':callWaitingUserConfigEntry,_W:callWaitingUserConfigEpId,'callWaitingUserConfigState':callWaitingUserConfigState,'secondCallGroup':secondCallGroup,'defaultSecondCallEnable':defaultSecondCallEnable,'defaultSecondCallDisconnectAction':defaultSecondCallDisconnectAction,'epSpecificSecondCallTable':epSpecificSecondCallTable,'epSpecificSecondCallEntry':epSpecificSecondCallEntry,_Y:epSpecificSecondCallEpId,'epSpecificSecondCallEnableConfig':epSpecificSecondCallEnableConfig,'epSpecificSecondCallEnable':epSpecificSecondCallEnable,'epSpecificSecondCallDisconnectAction':epSpecificSecondCallDisconnectAction,'secondCallStatusTable':secondCallStatusTable,'secondCallStatusEntry':secondCallStatusEntry,_Z:secondCallStatusEpId,'secondCallStatusState':secondCallStatusState,'transferGroup':transferGroup,'defaultTransferBlindEnable':defaultTransferBlindEnable,'defaultTransferAttendedEnable':defaultTransferAttendedEnable,'epSpecificTransferTable':epSpecificTransferTable,'epSpecificTransferEntry':epSpecificTransferEntry,_a:epSpecificTransferEpId,'epSpecificTransferEnableConfig':epSpecificTransferEnableConfig,'epSpecificTransferBlindEnable':epSpecificTransferBlindEnable,'epSpecificTransferAttendedEnable':epSpecificTransferAttendedEnable,'transferStatusTable':transferStatusTable,'transferStatusEntry':transferStatusEntry,_b:transferStatusEpId,'transferStatusBlindState':transferStatusBlindState,'transferStatusAttendedState':transferStatusAttendedState,'conferenceGroup':conferenceGroup,'defaultConferenceEnable':defaultConferenceEnable,'defaultConferenceType':defaultConferenceType,'epSpecificConferenceTable':epSpecificConferenceTable,'epSpecificConferenceEntry':epSpecificConferenceEntry,_d:epSpecificConferenceEpId,'epSpecificConferenceEnableConfig':epSpecificConferenceEnableConfig,'epSpecificConferenceEnable':epSpecificConferenceEnable,'epSpecificConferenceType':epSpecificConferenceType,'conferenceStatusTable':conferenceStatusTable,'conferenceStatusEntry':conferenceStatusEntry,_e:conferenceStatusEpId,'conferenceStatusState':conferenceStatusState,'forwardGroup':forwardGroup,'forwardUnconditionalGroup':forwardUnconditionalGroup,'defaultForwardUnconditionalEnable':defaultForwardUnconditionalEnable,'defaultForwardUnconditionalDtmfMapActivation':defaultForwardUnconditionalDtmfMapActivation,'defaultForwardUnconditionalDtmfMapDeactivation':defaultForwardUnconditionalDtmfMapDeactivation,'epSpecificForwardUnconditionalTable':epSpecificForwardUnconditionalTable,'epSpecificForwardUnconditionalEntry':epSpecificForwardUnconditionalEntry,_f:epSpecificForwardUnconditionalEpId,'epSpecificForwardUnconditionalEnableConfig':epSpecificForwardUnconditionalEnableConfig,'epSpecificForwardUnconditionalEnable':epSpecificForwardUnconditionalEnable,'forwardUnconditionalConfigTable':forwardUnconditionalConfigTable,'forwardUnconditionalConfigEntry':forwardUnconditionalConfigEntry,_g:forwardUnconditionalConfigEpId,'forwardUnconditionalConfigActivation':forwardUnconditionalConfigActivation,'forwardUnconditionalConfigForwardingAddress':forwardUnconditionalConfigForwardingAddress,'forwardOnBusyGroup':forwardOnBusyGroup,'defaultForwardOnBusyEnable':defaultForwardOnBusyEnable,'defaultForwardOnBusyDtmfMapActivation':defaultForwardOnBusyDtmfMapActivation,'defaultForwardOnBusyDtmfMapDeactivation':defaultForwardOnBusyDtmfMapDeactivation,'epSpecificForwardOnBusyTable':epSpecificForwardOnBusyTable,'epSpecificForwardOnBusyEntry':epSpecificForwardOnBusyEntry,_h:epSpecificForwardOnBusyEpId,'epSpecificForwardOnBusyEnableConfig':epSpecificForwardOnBusyEnableConfig,'epSpecificForwardOnBusyEnable':epSpecificForwardOnBusyEnable,'forwardOnBusyConfigTable':forwardOnBusyConfigTable,'forwardOnBusyConfigEntry':forwardOnBusyConfigEntry,_i:forwardOnBusyConfigEpId,'forwardOnBusyConfigActivation':forwardOnBusyConfigActivation,'forwardOnBusyConfigForwardingAddress':forwardOnBusyConfigForwardingAddress,'forwardNoAnswerGroup':forwardNoAnswerGroup,'defaultForwardNoAnswerEnable':defaultForwardNoAnswerEnable,'defaultForwardNoAnswerTimeout':defaultForwardNoAnswerTimeout,'defaultForwardNoAnswerDtmfMapActivation':defaultForwardNoAnswerDtmfMapActivation,'defaultForwardNoAnswerDtmfMapDeactivation':defaultForwardNoAnswerDtmfMapDeactivation,'epSpecificForwardNoAnswerTable':epSpecificForwardNoAnswerTable,'epSpecificForwardNoAnswerEntry':epSpecificForwardNoAnswerEntry,_j:epSpecificForwardNoAnswerEpId,'epSpecificForwardNoAnswerEnableConfig':epSpecificForwardNoAnswerEnableConfig,'epSpecificForwardNoAnswerEnable':epSpecificForwardNoAnswerEnable,'epSpecificForwardNoAnswerTimeout':epSpecificForwardNoAnswerTimeout,'forwardNoAnswerConfigTable':forwardNoAnswerConfigTable,'forwardNoAnswerConfigEntry':forwardNoAnswerConfigEntry,_k:forwardNoAnswerConfigEpId,'forwardNoAnswerConfigActivation':forwardNoAnswerConfigActivation,'forwardNoAnswerConfigForwardingAddress':forwardNoAnswerConfigForwardingAddress,'callCompletionGroup':callCompletionGroup,'defaultCallCompletionBusySubscriberEnable':defaultCallCompletionBusySubscriberEnable,'defaultCallCompletionBusySubscriberDtmfMapActivation':defaultCallCompletionBusySubscriberDtmfMapActivation,'defaultCallCompletionNoReplyEnable':defaultCallCompletionNoReplyEnable,'defaultCallCompletionNoReplyDtmfMapActivation':defaultCallCompletionNoReplyDtmfMapActivation,'defaultCallCompletionDtmfMapDeactivation':defaultCallCompletionDtmfMapDeactivation,'defaultCallCompletionExpirationTimeout':defaultCallCompletionExpirationTimeout,'defaultCallCompletionMethod':defaultCallCompletionMethod,'defaultCallCompletionAutoReactivateEnable':defaultCallCompletionAutoReactivateEnable,'defaultCallCompletionAutoReactivateDelay':defaultCallCompletionAutoReactivateDelay,'defaultCallCompletionEarlyMediaBehaviour':defaultCallCompletionEarlyMediaBehaviour,'epSpecificCallCompletionTable':epSpecificCallCompletionTable,'epSpecificCallCompletionEntry':epSpecificCallCompletionEntry,_l:epSpecificCallCompletionEpId,'epSpecificCallCompletionEnableConfig':epSpecificCallCompletionEnableConfig,'epSpecificCallCompletionBusySubscriberEnable':epSpecificCallCompletionBusySubscriberEnable,'epSpecificCallCompletionNoReplyEnable':epSpecificCallCompletionNoReplyEnable,'callCompletionConfigTable':callCompletionConfigTable,'callCompletionConfigEntry':callCompletionConfigEntry,_m:callCompletionConfigIndex,'callCompletionConfigEpId':callCompletionConfigEpId,'callCompletionConfigType':callCompletionConfigType,'callCompletionConfigTargetAddress':callCompletionConfigTargetAddress,'callCompletionConfigTargetState':callCompletionConfigTargetState,'callCompletionPollingGroup':callCompletionPollingGroup,'defaultCallCompletionPollingInterval':defaultCallCompletionPollingInterval,'delayedHotlineGroup':delayedHotlineGroup,'defaultDelayedHotlineEnable':defaultDelayedHotlineEnable,'defaultDelayedHotlineCondition':defaultDelayedHotlineCondition,'defaultDelayedHotlineTargetAddress':defaultDelayedHotlineTargetAddress,'epSpecificDelayedHotlineTable':epSpecificDelayedHotlineTable,'epSpecificDelayedHotlineEntry':epSpecificDelayedHotlineEntry,_q:epSpecificDelayedHotlineEpId,'epSpecificDelayedHotlineEnableConfig':epSpecificDelayedHotlineEnableConfig,'epSpecificDelayedHotlineEnable':epSpecificDelayedHotlineEnable,'epSpecificDelayedHotlineCondition':epSpecificDelayedHotlineCondition,'epSpecificDelayedHotlineTargetAddress':epSpecificDelayedHotlineTargetAddress,'statisticsGroup':statisticsGroup,'callStatisticsTable':callStatisticsTable,'callStatisticsEntry':callStatisticsEntry,_r:callStatisticsEpId,'callStatisticsIncomingCallsReceived':callStatisticsIncomingCallsReceived,'callStatisticsIncomingCallsAnswered':callStatisticsIncomingCallsAnswered,'callStatisticsIncomingCallsConnected':callStatisticsIncomingCallsConnected,'callStatisticsIncomingCallsFailed':callStatisticsIncomingCallsFailed,'callStatisticsOutgoingCallsAttempted':callStatisticsOutgoingCallsAttempted,'callStatisticsOutgoingCallsAnswered':callStatisticsOutgoingCallsAnswered,'callStatisticsOutgoingCallsConnected':callStatisticsOutgoingCallsConnected,'callStatisticsOutgoingCallsFailed':callStatisticsOutgoingCallsFailed,'callStatisticsCallsDropped':callStatisticsCallsDropped,'callStatisticsTotalCallTime':callStatisticsTotalCallTime,'callStatisticsReset':callStatisticsReset,'dtmfMapGroup':dtmfMapGroup,'dtmfMapTimeoutCompletion':dtmfMapTimeoutCompletion,'dtmfMapTimeoutFirstDtmf':dtmfMapTimeoutFirstDtmf,'dtmfMapTimeoutInterDtmf':dtmfMapTimeoutInterDtmf,'epSpecificDtmfMapTimeoutTable':epSpecificDtmfMapTimeoutTable,'epSpecificDtmfMapTimeoutEntry':epSpecificDtmfMapTimeoutEntry,_s:epSpecificDtmfMapTimeoutEpId,'epSpecificDtmfMapTimeoutEnableConfig':epSpecificDtmfMapTimeoutEnableConfig,'epSpecificDtmfMapTimeoutCompletion':epSpecificDtmfMapTimeoutCompletion,'epSpecificDtmfMapTimeoutFirstDtmf':epSpecificDtmfMapTimeoutFirstDtmf,'epSpecificDtmfMapTimeoutInterDtmf':epSpecificDtmfMapTimeoutInterDtmf,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})