_A1='cabhQos2ClassifierGroup'
_A0='cabhQos2Group'
_z='cabhQos2TrafficClassRowStatus'
_y='cabhQos2TrafficClassImpNum'
_x='cabhQos2TrafficClassDestPort'
_w='cabhQos2TrafficClassSrcPort'
_v='cabhQos2TrafficClassDestIp'
_u='cabhQos2TrafficClassSrcIp'
_t='cabhQos2PolicyIpType'
_s='cabhQos2PolicyIpProtocol'
_r='cabhQos2PolicyPortNumber'
_q='cabhQos2PolicyPortDomain'
_p='cabhQos2PolicyServiceName'
_o='cabhQos2PolicyServiceProvDomain'
_n='cabhQos2PolicyAppName'
_m='cabhQos2PolicyAppDomain'
_l='cabhQos2PolicyRuleOrder'
_k='cabhQos2NumActivePolicyHolder'
_j='cabhQos2PolicyAdmissionControl'
_i='cabhQos2PolicyHolderEnabled'
_h='cabhQos2PsIfAttribNumQueues'
_g='cabhQos2PsIfAttribNumPriorities'
_f='cabhQos2LastSetToFactory'
_e='cabhQos2SetToFactory'
_d='cabhQos2TrafficClassIdx'
_c='cabhQos2TrafficClassMethod'
_b='cabhQos2PolicyOwnerRuleId'
_a='cabhQos2PolicyOwner'
_Z='TruthValue'
_Y='Gauge32'
_X='ifIndex'
_W='IF-MIB'
_V='cabhQos2TrafficClassIpType'
_U='cabhQos2TrafficClassProtocol'
_T='cabhQos2PolicyRowStatus'
_S='cabhQos2PolicyUserImportance'
_R='cabhQos2PolicyTraffImpNum'
_Q='cabhQos2PolicyDestPort'
_P='cabhQos2PolicySrcPort'
_O='cabhQos2PolicyDestIp'
_N='cabhQos2PolicySrcIp'
_M='read-write'
_L='InetAddressType'
_K='00000000'
_J='not-accessible'
_I='read-only'
_H='Integer32'
_G='InetAddress'
_F='SnmpAdminString'
_E='InetPortNumber'
_D='Unsigned32'
_C='read-create'
_B='current'
_A='CABH-QOS2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjCableHome,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjCableHome')
ifIndex,=mibBuilder.importSymbols(_W,_X)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_L,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_Y,_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_Z)
cabhQos2Mib=ModuleIdentity((1,3,6,1,4,1,4491,2,4,8))
if mibBuilder.loadTexts:cabhQos2Mib.setRevisions(('2005-04-08 00:00',))
_CabhQos2Mib2Notifications_ObjectIdentity=ObjectIdentity
cabhQos2Mib2Notifications=_CabhQos2Mib2Notifications_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,0))
_CabhQos2MibObjects_ObjectIdentity=ObjectIdentity
cabhQos2MibObjects=_CabhQos2MibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,1))
_CabhQos2Base_ObjectIdentity=ObjectIdentity
cabhQos2Base=_CabhQos2Base_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,1,1))
_CabhQos2SetToFactory_Type=TruthValue
_CabhQos2SetToFactory_Object=MibScalar
cabhQos2SetToFactory=_CabhQos2SetToFactory_Object((1,3,6,1,4,1,4491,2,4,8,1,1,1),_CabhQos2SetToFactory_Type())
cabhQos2SetToFactory.setMaxAccess(_M)
if mibBuilder.loadTexts:cabhQos2SetToFactory.setStatus(_B)
_CabhQos2LastSetToFactory_Type=TimeStamp
_CabhQos2LastSetToFactory_Object=MibScalar
cabhQos2LastSetToFactory=_CabhQos2LastSetToFactory_Object((1,3,6,1,4,1,4491,2,4,8,1,1,2),_CabhQos2LastSetToFactory_Type())
cabhQos2LastSetToFactory.setMaxAccess(_I)
if mibBuilder.loadTexts:cabhQos2LastSetToFactory.setStatus(_B)
_CabhQos2PsIfAttributes_ObjectIdentity=ObjectIdentity
cabhQos2PsIfAttributes=_CabhQos2PsIfAttributes_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,1,2))
_CabhQos2PsIfAttribTable_Object=MibTable
cabhQos2PsIfAttribTable=_CabhQos2PsIfAttribTable_Object((1,3,6,1,4,1,4491,2,4,8,1,2,1))
if mibBuilder.loadTexts:cabhQos2PsIfAttribTable.setStatus(_B)
_CabhQos2PsIfAttribEntry_Object=MibTableRow
cabhQos2PsIfAttribEntry=_CabhQos2PsIfAttribEntry_Object((1,3,6,1,4,1,4491,2,4,8,1,2,1,1))
cabhQos2PsIfAttribEntry.setIndexNames((0,_W,_X))
if mibBuilder.loadTexts:cabhQos2PsIfAttribEntry.setStatus(_B)
class _CabhQos2PsIfAttribNumPriorities_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CabhQos2PsIfAttribNumPriorities_Type.__name__=_D
_CabhQos2PsIfAttribNumPriorities_Object=MibTableColumn
cabhQos2PsIfAttribNumPriorities=_CabhQos2PsIfAttribNumPriorities_Object((1,3,6,1,4,1,4491,2,4,8,1,2,1,1,1),_CabhQos2PsIfAttribNumPriorities_Type())
cabhQos2PsIfAttribNumPriorities.setMaxAccess(_I)
if mibBuilder.loadTexts:cabhQos2PsIfAttribNumPriorities.setStatus(_B)
class _CabhQos2PsIfAttribNumQueues_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CabhQos2PsIfAttribNumQueues_Type.__name__=_D
_CabhQos2PsIfAttribNumQueues_Object=MibTableColumn
cabhQos2PsIfAttribNumQueues=_CabhQos2PsIfAttribNumQueues_Object((1,3,6,1,4,1,4491,2,4,8,1,2,1,1,2),_CabhQos2PsIfAttribNumQueues_Type())
cabhQos2PsIfAttribNumQueues.setMaxAccess(_I)
if mibBuilder.loadTexts:cabhQos2PsIfAttribNumQueues.setStatus(_B)
_CabhQos2PolicyHolderObjects_ObjectIdentity=ObjectIdentity
cabhQos2PolicyHolderObjects=_CabhQos2PolicyHolderObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,1,3))
class _CabhQos2PolicyHolderEnabled_Type(TruthValue):defaultValue=1
_CabhQos2PolicyHolderEnabled_Type.__name__=_Z
_CabhQos2PolicyHolderEnabled_Object=MibScalar
cabhQos2PolicyHolderEnabled=_CabhQos2PolicyHolderEnabled_Object((1,3,6,1,4,1,4491,2,4,8,1,3,1),_CabhQos2PolicyHolderEnabled_Type())
cabhQos2PolicyHolderEnabled.setMaxAccess(_M)
if mibBuilder.loadTexts:cabhQos2PolicyHolderEnabled.setStatus(_B)
class _CabhQos2PolicyAdmissionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CabhQos2PolicyAdmissionControl_Type.__name__=_H
_CabhQos2PolicyAdmissionControl_Object=MibScalar
cabhQos2PolicyAdmissionControl=_CabhQos2PolicyAdmissionControl_Object((1,3,6,1,4,1,4491,2,4,8,1,3,2),_CabhQos2PolicyAdmissionControl_Type())
cabhQos2PolicyAdmissionControl.setMaxAccess(_M)
if mibBuilder.loadTexts:cabhQos2PolicyAdmissionControl.setStatus(_B)
class _CabhQos2NumActivePolicyHolder_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CabhQos2NumActivePolicyHolder_Type.__name__=_Y
_CabhQos2NumActivePolicyHolder_Object=MibScalar
cabhQos2NumActivePolicyHolder=_CabhQos2NumActivePolicyHolder_Object((1,3,6,1,4,1,4491,2,4,8,1,3,3),_CabhQos2NumActivePolicyHolder_Type())
cabhQos2NumActivePolicyHolder.setMaxAccess(_I)
if mibBuilder.loadTexts:cabhQos2NumActivePolicyHolder.setStatus(_B)
_CabhQos2PolicyTable_Object=MibTable
cabhQos2PolicyTable=_CabhQos2PolicyTable_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4))
if mibBuilder.loadTexts:cabhQos2PolicyTable.setStatus(_B)
_CabhQos2PolicyEntry_Object=MibTableRow
cabhQos2PolicyEntry=_CabhQos2PolicyEntry_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1))
cabhQos2PolicyEntry.setIndexNames((0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:cabhQos2PolicyEntry.setStatus(_B)
class _CabhQos2PolicyOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('operatorOnly',1),('homeUser',2),('operatorForHomeUser',3),('upnp',4)))
_CabhQos2PolicyOwner_Type.__name__=_H
_CabhQos2PolicyOwner_Object=MibTableColumn
cabhQos2PolicyOwner=_CabhQos2PolicyOwner_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,1),_CabhQos2PolicyOwner_Type())
cabhQos2PolicyOwner.setMaxAccess(_J)
if mibBuilder.loadTexts:cabhQos2PolicyOwner.setStatus(_B)
class _CabhQos2PolicyOwnerRuleId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CabhQos2PolicyOwnerRuleId_Type.__name__=_D
_CabhQos2PolicyOwnerRuleId_Object=MibTableColumn
cabhQos2PolicyOwnerRuleId=_CabhQos2PolicyOwnerRuleId_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,2),_CabhQos2PolicyOwnerRuleId_Type())
cabhQos2PolicyOwnerRuleId.setMaxAccess(_J)
if mibBuilder.loadTexts:cabhQos2PolicyOwnerRuleId.setStatus(_B)
class _CabhQos2PolicyRuleOrder_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CabhQos2PolicyRuleOrder_Type.__name__=_D
_CabhQos2PolicyRuleOrder_Object=MibTableColumn
cabhQos2PolicyRuleOrder=_CabhQos2PolicyRuleOrder_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,3),_CabhQos2PolicyRuleOrder_Type())
cabhQos2PolicyRuleOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyRuleOrder.setStatus(_B)
class _CabhQos2PolicyAppDomain_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CabhQos2PolicyAppDomain_Type.__name__=_F
_CabhQos2PolicyAppDomain_Object=MibTableColumn
cabhQos2PolicyAppDomain=_CabhQos2PolicyAppDomain_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,4),_CabhQos2PolicyAppDomain_Type())
cabhQos2PolicyAppDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyAppDomain.setStatus(_B)
class _CabhQos2PolicyAppName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CabhQos2PolicyAppName_Type.__name__=_F
_CabhQos2PolicyAppName_Object=MibTableColumn
cabhQos2PolicyAppName=_CabhQos2PolicyAppName_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,5),_CabhQos2PolicyAppName_Type())
cabhQos2PolicyAppName.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyAppName.setStatus(_B)
class _CabhQos2PolicyServiceProvDomain_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CabhQos2PolicyServiceProvDomain_Type.__name__=_F
_CabhQos2PolicyServiceProvDomain_Object=MibTableColumn
cabhQos2PolicyServiceProvDomain=_CabhQos2PolicyServiceProvDomain_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,6),_CabhQos2PolicyServiceProvDomain_Type())
cabhQos2PolicyServiceProvDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyServiceProvDomain.setStatus(_B)
class _CabhQos2PolicyServiceName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CabhQos2PolicyServiceName_Type.__name__=_F
_CabhQos2PolicyServiceName_Object=MibTableColumn
cabhQos2PolicyServiceName=_CabhQos2PolicyServiceName_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,7),_CabhQos2PolicyServiceName_Type())
cabhQos2PolicyServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyServiceName.setStatus(_B)
class _CabhQos2PolicyPortDomain_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CabhQos2PolicyPortDomain_Type.__name__=_F
_CabhQos2PolicyPortDomain_Object=MibTableColumn
cabhQos2PolicyPortDomain=_CabhQos2PolicyPortDomain_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,8),_CabhQos2PolicyPortDomain_Type())
cabhQos2PolicyPortDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyPortDomain.setStatus(_B)
class _CabhQos2PolicyPortNumber_Type(InetPortNumber):defaultValue=0
_CabhQos2PolicyPortNumber_Type.__name__=_E
_CabhQos2PolicyPortNumber_Object=MibTableColumn
cabhQos2PolicyPortNumber=_CabhQos2PolicyPortNumber_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,9),_CabhQos2PolicyPortNumber_Type())
cabhQos2PolicyPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyPortNumber.setStatus(_B)
class _CabhQos2PolicyIpType_Type(InetAddressType):defaultValue=1
_CabhQos2PolicyIpType_Type.__name__=_L
_CabhQos2PolicyIpType_Object=MibTableColumn
cabhQos2PolicyIpType=_CabhQos2PolicyIpType_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,10),_CabhQos2PolicyIpType_Type())
cabhQos2PolicyIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyIpType.setStatus(_B)
class _CabhQos2PolicyIpProtocol_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CabhQos2PolicyIpProtocol_Type.__name__=_D
_CabhQos2PolicyIpProtocol_Object=MibTableColumn
cabhQos2PolicyIpProtocol=_CabhQos2PolicyIpProtocol_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,11),_CabhQos2PolicyIpProtocol_Type())
cabhQos2PolicyIpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyIpProtocol.setStatus(_B)
class _CabhQos2PolicySrcIp_Type(InetAddress):defaultHexValue=_K
_CabhQos2PolicySrcIp_Type.__name__=_G
_CabhQos2PolicySrcIp_Object=MibTableColumn
cabhQos2PolicySrcIp=_CabhQos2PolicySrcIp_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,12),_CabhQos2PolicySrcIp_Type())
cabhQos2PolicySrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicySrcIp.setStatus(_B)
class _CabhQos2PolicyDestIp_Type(InetAddress):defaultHexValue=_K
_CabhQos2PolicyDestIp_Type.__name__=_G
_CabhQos2PolicyDestIp_Object=MibTableColumn
cabhQos2PolicyDestIp=_CabhQos2PolicyDestIp_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,13),_CabhQos2PolicyDestIp_Type())
cabhQos2PolicyDestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyDestIp.setStatus(_B)
class _CabhQos2PolicySrcPort_Type(InetPortNumber):defaultValue=0
_CabhQos2PolicySrcPort_Type.__name__=_E
_CabhQos2PolicySrcPort_Object=MibTableColumn
cabhQos2PolicySrcPort=_CabhQos2PolicySrcPort_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,14),_CabhQos2PolicySrcPort_Type())
cabhQos2PolicySrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicySrcPort.setStatus(_B)
class _CabhQos2PolicyDestPort_Type(InetPortNumber):defaultValue=0
_CabhQos2PolicyDestPort_Type.__name__=_E
_CabhQos2PolicyDestPort_Object=MibTableColumn
cabhQos2PolicyDestPort=_CabhQos2PolicyDestPort_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,15),_CabhQos2PolicyDestPort_Type())
cabhQos2PolicyDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyDestPort.setStatus(_B)
class _CabhQos2PolicyTraffImpNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CabhQos2PolicyTraffImpNum_Type.__name__=_D
_CabhQos2PolicyTraffImpNum_Object=MibTableColumn
cabhQos2PolicyTraffImpNum=_CabhQos2PolicyTraffImpNum_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,16),_CabhQos2PolicyTraffImpNum_Type())
cabhQos2PolicyTraffImpNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyTraffImpNum.setStatus(_B)
class _CabhQos2PolicyUserImportance_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CabhQos2PolicyUserImportance_Type.__name__=_D
_CabhQos2PolicyUserImportance_Object=MibTableColumn
cabhQos2PolicyUserImportance=_CabhQos2PolicyUserImportance_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,17),_CabhQos2PolicyUserImportance_Type())
cabhQos2PolicyUserImportance.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyUserImportance.setStatus(_B)
_CabhQos2PolicyRowStatus_Type=RowStatus
_CabhQos2PolicyRowStatus_Object=MibTableColumn
cabhQos2PolicyRowStatus=_CabhQos2PolicyRowStatus_Object((1,3,6,1,4,1,4491,2,4,8,1,3,4,1,18),_CabhQos2PolicyRowStatus_Type())
cabhQos2PolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2PolicyRowStatus.setStatus(_B)
_CabhQos2DeviceObjects_ObjectIdentity=ObjectIdentity
cabhQos2DeviceObjects=_CabhQos2DeviceObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,1,4))
_CabhQos2TrafficClassTable_Object=MibTable
cabhQos2TrafficClassTable=_CabhQos2TrafficClassTable_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1))
if mibBuilder.loadTexts:cabhQos2TrafficClassTable.setStatus(_B)
_CabhQos2TrafficClassEntry_Object=MibTableRow
cabhQos2TrafficClassEntry=_CabhQos2TrafficClassEntry_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1))
cabhQos2TrafficClassEntry.setIndexNames((0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:cabhQos2TrafficClassEntry.setStatus(_B)
class _CabhQos2TrafficClassMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('upnp',2)))
_CabhQos2TrafficClassMethod_Type.__name__=_H
_CabhQos2TrafficClassMethod_Object=MibTableColumn
cabhQos2TrafficClassMethod=_CabhQos2TrafficClassMethod_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,1),_CabhQos2TrafficClassMethod_Type())
cabhQos2TrafficClassMethod.setMaxAccess(_J)
if mibBuilder.loadTexts:cabhQos2TrafficClassMethod.setStatus(_B)
class _CabhQos2TrafficClassIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CabhQos2TrafficClassIdx_Type.__name__=_D
_CabhQos2TrafficClassIdx_Object=MibTableColumn
cabhQos2TrafficClassIdx=_CabhQos2TrafficClassIdx_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,2),_CabhQos2TrafficClassIdx_Type())
cabhQos2TrafficClassIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:cabhQos2TrafficClassIdx.setStatus(_B)
class _CabhQos2TrafficClassProtocol_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_CabhQos2TrafficClassProtocol_Type.__name__=_D
_CabhQos2TrafficClassProtocol_Object=MibTableColumn
cabhQos2TrafficClassProtocol=_CabhQos2TrafficClassProtocol_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,3),_CabhQos2TrafficClassProtocol_Type())
cabhQos2TrafficClassProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassProtocol.setStatus(_B)
class _CabhQos2TrafficClassIpType_Type(InetAddressType):defaultValue=1
_CabhQos2TrafficClassIpType_Type.__name__=_L
_CabhQos2TrafficClassIpType_Object=MibTableColumn
cabhQos2TrafficClassIpType=_CabhQos2TrafficClassIpType_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,4),_CabhQos2TrafficClassIpType_Type())
cabhQos2TrafficClassIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassIpType.setStatus(_B)
class _CabhQos2TrafficClassSrcIp_Type(InetAddress):defaultHexValue=_K
_CabhQos2TrafficClassSrcIp_Type.__name__=_G
_CabhQos2TrafficClassSrcIp_Object=MibTableColumn
cabhQos2TrafficClassSrcIp=_CabhQos2TrafficClassSrcIp_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,5),_CabhQos2TrafficClassSrcIp_Type())
cabhQos2TrafficClassSrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassSrcIp.setStatus(_B)
class _CabhQos2TrafficClassDestIp_Type(InetAddress):defaultHexValue=_K
_CabhQos2TrafficClassDestIp_Type.__name__=_G
_CabhQos2TrafficClassDestIp_Object=MibTableColumn
cabhQos2TrafficClassDestIp=_CabhQos2TrafficClassDestIp_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,6),_CabhQos2TrafficClassDestIp_Type())
cabhQos2TrafficClassDestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassDestIp.setStatus(_B)
class _CabhQos2TrafficClassSrcPort_Type(InetPortNumber):defaultValue=0
_CabhQos2TrafficClassSrcPort_Type.__name__=_E
_CabhQos2TrafficClassSrcPort_Object=MibTableColumn
cabhQos2TrafficClassSrcPort=_CabhQos2TrafficClassSrcPort_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,7),_CabhQos2TrafficClassSrcPort_Type())
cabhQos2TrafficClassSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassSrcPort.setStatus(_B)
class _CabhQos2TrafficClassDestPort_Type(InetPortNumber):defaultValue=0
_CabhQos2TrafficClassDestPort_Type.__name__=_E
_CabhQos2TrafficClassDestPort_Object=MibTableColumn
cabhQos2TrafficClassDestPort=_CabhQos2TrafficClassDestPort_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,8),_CabhQos2TrafficClassDestPort_Type())
cabhQos2TrafficClassDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassDestPort.setStatus(_B)
class _CabhQos2TrafficClassImpNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CabhQos2TrafficClassImpNum_Type.__name__=_D
_CabhQos2TrafficClassImpNum_Object=MibTableColumn
cabhQos2TrafficClassImpNum=_CabhQos2TrafficClassImpNum_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,9),_CabhQos2TrafficClassImpNum_Type())
cabhQos2TrafficClassImpNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassImpNum.setStatus(_B)
_CabhQos2TrafficClassRowStatus_Type=RowStatus
_CabhQos2TrafficClassRowStatus_Object=MibTableColumn
cabhQos2TrafficClassRowStatus=_CabhQos2TrafficClassRowStatus_Object((1,3,6,1,4,1,4491,2,4,8,1,4,1,1,10),_CabhQos2TrafficClassRowStatus_Type())
cabhQos2TrafficClassRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cabhQos2TrafficClassRowStatus.setStatus(_B)
_CabhQos2Conformance_ObjectIdentity=ObjectIdentity
cabhQos2Conformance=_CabhQos2Conformance_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,2))
_CabhQos2Compliances_ObjectIdentity=ObjectIdentity
cabhQos2Compliances=_CabhQos2Compliances_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,2,1))
_CabhQos2Groups_ObjectIdentity=ObjectIdentity
cabhQos2Groups=_CabhQos2Groups_ObjectIdentity((1,3,6,1,4,1,4491,2,4,8,2,2))
cabhQos2Group=ObjectGroup((1,3,6,1,4,1,4491,2,4,8,2,2,1))
cabhQos2Group.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cabhQos2Group.setStatus(_B)
cabhQos2ClassifierGroup=ObjectGroup((1,3,6,1,4,1,4491,2,4,8,2,2,2))
cabhQos2ClassifierGroup.setObjects(*((_A,_U),(_A,_V),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cabhQos2ClassifierGroup.setStatus(_B)
cabhQos2Compliance=ModuleCompliance((1,3,6,1,4,1,4491,2,4,8,2,1,1))
cabhQos2Compliance.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:cabhQos2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cabhQos2Mib':cabhQos2Mib,'cabhQos2Mib2Notifications':cabhQos2Mib2Notifications,'cabhQos2MibObjects':cabhQos2MibObjects,'cabhQos2Base':cabhQos2Base,_e:cabhQos2SetToFactory,_f:cabhQos2LastSetToFactory,'cabhQos2PsIfAttributes':cabhQos2PsIfAttributes,'cabhQos2PsIfAttribTable':cabhQos2PsIfAttribTable,'cabhQos2PsIfAttribEntry':cabhQos2PsIfAttribEntry,_g:cabhQos2PsIfAttribNumPriorities,_h:cabhQos2PsIfAttribNumQueues,'cabhQos2PolicyHolderObjects':cabhQos2PolicyHolderObjects,_i:cabhQos2PolicyHolderEnabled,_j:cabhQos2PolicyAdmissionControl,_k:cabhQos2NumActivePolicyHolder,'cabhQos2PolicyTable':cabhQos2PolicyTable,'cabhQos2PolicyEntry':cabhQos2PolicyEntry,_a:cabhQos2PolicyOwner,_b:cabhQos2PolicyOwnerRuleId,_l:cabhQos2PolicyRuleOrder,_m:cabhQos2PolicyAppDomain,_n:cabhQos2PolicyAppName,_o:cabhQos2PolicyServiceProvDomain,_p:cabhQos2PolicyServiceName,_q:cabhQos2PolicyPortDomain,_r:cabhQos2PolicyPortNumber,_t:cabhQos2PolicyIpType,_s:cabhQos2PolicyIpProtocol,_N:cabhQos2PolicySrcIp,_O:cabhQos2PolicyDestIp,_P:cabhQos2PolicySrcPort,_Q:cabhQos2PolicyDestPort,_R:cabhQos2PolicyTraffImpNum,_S:cabhQos2PolicyUserImportance,_T:cabhQos2PolicyRowStatus,'cabhQos2DeviceObjects':cabhQos2DeviceObjects,'cabhQos2TrafficClassTable':cabhQos2TrafficClassTable,'cabhQos2TrafficClassEntry':cabhQos2TrafficClassEntry,_c:cabhQos2TrafficClassMethod,_d:cabhQos2TrafficClassIdx,_U:cabhQos2TrafficClassProtocol,_V:cabhQos2TrafficClassIpType,_u:cabhQos2TrafficClassSrcIp,_v:cabhQos2TrafficClassDestIp,_w:cabhQos2TrafficClassSrcPort,_x:cabhQos2TrafficClassDestPort,_y:cabhQos2TrafficClassImpNum,_z:cabhQos2TrafficClassRowStatus,'cabhQos2Conformance':cabhQos2Conformance,'cabhQos2Compliances':cabhQos2Compliances,'cabhQos2Compliance':cabhQos2Compliance,'cabhQos2Groups':cabhQos2Groups,_A0:cabhQos2Group,_A1:cabhQos2ClassifierGroup})