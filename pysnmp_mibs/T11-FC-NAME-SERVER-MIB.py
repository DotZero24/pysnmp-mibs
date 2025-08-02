_A2='t11NsNotifyGroup'
_A1='t11NsNotifyControlGroup'
_A0='t11NsDBGroup'
_z='t11NsRejectRegNotify'
_y='t11NsInfoSubsetRejReqNotfyEnable'
_x='t11NsRejects'
_w='t11NsInfoSubsetTotalRejects'
_v='t11NsOutRscns'
_u='t11NsInRscns'
_t='t11NsDatabaseFull'
_s='t11NsInDeRegReqs'
_r='t11NsInRegReqs'
_q='t11NsOutGetReqs'
_p='t11NsInGetReqs'
_o='t11NsRegFc4Descriptor'
_n='t11NsRegFc4Features'
_m='t11NsRegSymbolicNodeName'
_l='t11NsRegSymbolicPortName'
_k='t11NsRegHardAddress'
_j='t11NsRegFabricPortName'
_i='t11NsRegPortIpAddress'
_h='t11NsRegPortType'
_g='t11NsRegFc4Type'
_f='t11NsRegProcAssoc'
_e='t11NsRegNodeIpAddress'
_d='t11NsRegClassOfSvc'
_c='t11NsRegNodeName'
_b='t11NsInfoSubsetNumRows'
_a='t11NsInfoSubsetTableLastChange'
_Z='t11NsInfoSubsetSwitchIndex'
_Y='t11NsRegFc4TypeValue'
_X='t11FamLocalSwitchWwn'
_W='T11-FC-FABRIC-ADDR-MGR-MIB'
_V='TruthValue'
_U='Integer32'
_T='FcPortType'
_S='FcAddressIdOrZero'
_R='t11NsRejReasonVendorCode'
_Q='t11NsRejReasonCodeExp'
_P='t11NsRejectReasonCode'
_O='t11NsRejectCtCommandString'
_N='t11NsRegPortName'
_M='SnmpAdminString'
_L='t11NsRegPortIdentifier'
_K='not-accessible'
_J='Unsigned32'
_I='FcNameIdOrZero'
_H='t11NsRegFabricIndex'
_G='t11NsInfoSubsetIndex'
_F='fcmInstanceIndex'
_E='FC-MGMT-MIB'
_D='OctetString'
_C='read-only'
_B='T11-FC-NAME-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FcAddressIdOrZero,FcClasses,FcNameIdOrZero,FcPortType,fcmInstanceIndex=mibBuilder.importSymbols(_E,_S,'FcClasses',_I,_T,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_U,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_V)
t11FamLocalSwitchWwn,=mibBuilder.importSymbols(_W,_X)
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
t11FcNameServerMIB=ModuleIdentity((1,3,6,1,2,1,135))
if mibBuilder.loadTexts:t11FcNameServerMIB.setRevisions(('2006-03-02 00:00',))
class T11NsGs4RejectReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('none',1),('invalidCmdCode',2),('invalidVerLevel',3),('logicalError',4),('invalidIUSize',5),('logicalBusy',6),('protocolError',7),('unableToPerformCmdReq',8),('cmdNotSupported',9),('serverNotAvailable',10),('couldNotEstabSession',11),('vendorError',12)))
class T11NsRejReasonCodeExpl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('noAdditionalExplanation',1),('portIdentifierNotRegistered',2),('portNameNotRegistered',3),('nodeNameNotRegistered',4),('classOfServiceNotRegistered',5),('nodeIpAddressNotRegistered',6),('ipaNotRegistered',7),('fc4TypeNotRegistered',8),('symbolicPortNameNotRegistered',9),('symbolicNodeNameNotRegistered',10),('portTypeNotRegistered',11),('portIpAddressNotRegistered',12),('fabricPortNameNotRegistered',13),('hardAddressNotRegistered',14),('fc4DescriptorNotRegistered',15),('fc4FeaturesNotRegistered',16),('accessDenied',17),('unacceptablePortIdentifier',18),('databaseEmpty',19),('noObjectRegInSpecifiedScope',20),('domainIdNotPresent',21),('portIdNotPresent',22),('noDeviceAttached',23),('authorizationException',24),('authenticationException',25),('databaseFull',26)))
_T11NsNotifications_ObjectIdentity=ObjectIdentity
t11NsNotifications=_T11NsNotifications_ObjectIdentity((1,3,6,1,2,1,135,0))
_T11NsMIBObjects_ObjectIdentity=ObjectIdentity
t11NsMIBObjects=_T11NsMIBObjects_ObjectIdentity((1,3,6,1,2,1,135,1))
_T11NsStatus_ObjectIdentity=ObjectIdentity
t11NsStatus=_T11NsStatus_ObjectIdentity((1,3,6,1,2,1,135,1,1))
_T11NsInfoSubsetTable_Object=MibTable
t11NsInfoSubsetTable=_T11NsInfoSubsetTable_Object((1,3,6,1,2,1,135,1,1,1))
if mibBuilder.loadTexts:t11NsInfoSubsetTable.setStatus(_A)
_T11NsInfoSubsetEntry_Object=MibTableRow
t11NsInfoSubsetEntry=_T11NsInfoSubsetEntry_Object((1,3,6,1,2,1,135,1,1,1,1))
t11NsInfoSubsetEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:t11NsInfoSubsetEntry.setStatus(_A)
class _T11NsInfoSubsetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_T11NsInfoSubsetIndex_Type.__name__=_J
_T11NsInfoSubsetIndex_Object=MibTableColumn
t11NsInfoSubsetIndex=_T11NsInfoSubsetIndex_Object((1,3,6,1,2,1,135,1,1,1,1,1),_T11NsInfoSubsetIndex_Type())
t11NsInfoSubsetIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:t11NsInfoSubsetIndex.setStatus(_A)
class _T11NsInfoSubsetSwitchIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_T11NsInfoSubsetSwitchIndex_Type.__name__=_J
_T11NsInfoSubsetSwitchIndex_Object=MibTableColumn
t11NsInfoSubsetSwitchIndex=_T11NsInfoSubsetSwitchIndex_Object((1,3,6,1,2,1,135,1,1,1,1,2),_T11NsInfoSubsetSwitchIndex_Type())
t11NsInfoSubsetSwitchIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInfoSubsetSwitchIndex.setStatus(_A)
_T11NsInfoSubsetTableLastChange_Type=TimeStamp
_T11NsInfoSubsetTableLastChange_Object=MibTableColumn
t11NsInfoSubsetTableLastChange=_T11NsInfoSubsetTableLastChange_Object((1,3,6,1,2,1,135,1,1,1,1,3),_T11NsInfoSubsetTableLastChange_Type())
t11NsInfoSubsetTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInfoSubsetTableLastChange.setStatus(_A)
class _T11NsInfoSubsetNumRows_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_T11NsInfoSubsetNumRows_Type.__name__=_U
_T11NsInfoSubsetNumRows_Object=MibTableColumn
t11NsInfoSubsetNumRows=_T11NsInfoSubsetNumRows_Object((1,3,6,1,2,1,135,1,1,1,1,4),_T11NsInfoSubsetNumRows_Type())
t11NsInfoSubsetNumRows.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInfoSubsetNumRows.setStatus(_A)
_T11NsInfoSubsetTotalRejects_Type=Counter32
_T11NsInfoSubsetTotalRejects_Object=MibTableColumn
t11NsInfoSubsetTotalRejects=_T11NsInfoSubsetTotalRejects_Object((1,3,6,1,2,1,135,1,1,1,1,5),_T11NsInfoSubsetTotalRejects_Type())
t11NsInfoSubsetTotalRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInfoSubsetTotalRejects.setStatus(_A)
class _T11NsInfoSubsetRejReqNotfyEnable_Type(TruthValue):defaultValue=2
_T11NsInfoSubsetRejReqNotfyEnable_Type.__name__=_V
_T11NsInfoSubsetRejReqNotfyEnable_Object=MibTableColumn
t11NsInfoSubsetRejReqNotfyEnable=_T11NsInfoSubsetRejReqNotfyEnable_Object((1,3,6,1,2,1,135,1,1,1,1,6),_T11NsInfoSubsetRejReqNotfyEnable_Type())
t11NsInfoSubsetRejReqNotfyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:t11NsInfoSubsetRejReqNotfyEnable.setStatus(_A)
_T11NsRegTable_Object=MibTable
t11NsRegTable=_T11NsRegTable_Object((1,3,6,1,2,1,135,1,1,2))
if mibBuilder.loadTexts:t11NsRegTable.setStatus(_A)
_T11NsRegEntry_Object=MibTableRow
t11NsRegEntry=_T11NsRegEntry_Object((1,3,6,1,2,1,135,1,1,2,1))
t11NsRegEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H),(0,_B,_L))
if mibBuilder.loadTexts:t11NsRegEntry.setStatus(_A)
_T11NsRegFabricIndex_Type=T11FabricIndex
_T11NsRegFabricIndex_Object=MibTableColumn
t11NsRegFabricIndex=_T11NsRegFabricIndex_Object((1,3,6,1,2,1,135,1,1,2,1,1),_T11NsRegFabricIndex_Type())
t11NsRegFabricIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:t11NsRegFabricIndex.setStatus(_A)
_T11NsRegPortIdentifier_Type=FcAddressIdOrZero
_T11NsRegPortIdentifier_Object=MibTableColumn
t11NsRegPortIdentifier=_T11NsRegPortIdentifier_Object((1,3,6,1,2,1,135,1,1,2,1,2),_T11NsRegPortIdentifier_Type())
t11NsRegPortIdentifier.setMaxAccess(_K)
if mibBuilder.loadTexts:t11NsRegPortIdentifier.setStatus(_A)
class _T11NsRegPortName_Type(FcNameIdOrZero):defaultHexValue=''
_T11NsRegPortName_Type.__name__=_I
_T11NsRegPortName_Object=MibTableColumn
t11NsRegPortName=_T11NsRegPortName_Object((1,3,6,1,2,1,135,1,1,2,1,3),_T11NsRegPortName_Type())
t11NsRegPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegPortName.setStatus(_A)
class _T11NsRegNodeName_Type(FcNameIdOrZero):defaultHexValue=''
_T11NsRegNodeName_Type.__name__=_I
_T11NsRegNodeName_Object=MibTableColumn
t11NsRegNodeName=_T11NsRegNodeName_Object((1,3,6,1,2,1,135,1,1,2,1,4),_T11NsRegNodeName_Type())
t11NsRegNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegNodeName.setStatus(_A)
_T11NsRegClassOfSvc_Type=FcClasses
_T11NsRegClassOfSvc_Object=MibTableColumn
t11NsRegClassOfSvc=_T11NsRegClassOfSvc_Object((1,3,6,1,2,1,135,1,1,2,1,5),_T11NsRegClassOfSvc_Type())
t11NsRegClassOfSvc.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegClassOfSvc.setStatus(_A)
class _T11NsRegNodeIpAddress_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_T11NsRegNodeIpAddress_Type.__name__=_D
_T11NsRegNodeIpAddress_Object=MibTableColumn
t11NsRegNodeIpAddress=_T11NsRegNodeIpAddress_Object((1,3,6,1,2,1,135,1,1,2,1,6),_T11NsRegNodeIpAddress_Type())
t11NsRegNodeIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegNodeIpAddress.setStatus(_A)
class _T11NsRegProcAssoc_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
_T11NsRegProcAssoc_Type.__name__=_D
_T11NsRegProcAssoc_Object=MibTableColumn
t11NsRegProcAssoc=_T11NsRegProcAssoc_Object((1,3,6,1,2,1,135,1,1,2,1,7),_T11NsRegProcAssoc_Type())
t11NsRegProcAssoc.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegProcAssoc.setStatus(_A)
class _T11NsRegFc4Type_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(32,32))
_T11NsRegFc4Type_Type.__name__=_D
_T11NsRegFc4Type_Object=MibTableColumn
t11NsRegFc4Type=_T11NsRegFc4Type_Object((1,3,6,1,2,1,135,1,1,2,1,8),_T11NsRegFc4Type_Type())
t11NsRegFc4Type.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegFc4Type.setStatus(_A)
class _T11NsRegPortType_Type(FcPortType):defaultValue=1
_T11NsRegPortType_Type.__name__=_T
_T11NsRegPortType_Object=MibTableColumn
t11NsRegPortType=_T11NsRegPortType_Object((1,3,6,1,2,1,135,1,1,2,1,9),_T11NsRegPortType_Type())
t11NsRegPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegPortType.setStatus(_A)
class _T11NsRegPortIpAddress_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_T11NsRegPortIpAddress_Type.__name__=_D
_T11NsRegPortIpAddress_Object=MibTableColumn
t11NsRegPortIpAddress=_T11NsRegPortIpAddress_Object((1,3,6,1,2,1,135,1,1,2,1,10),_T11NsRegPortIpAddress_Type())
t11NsRegPortIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegPortIpAddress.setStatus(_A)
class _T11NsRegFabricPortName_Type(FcNameIdOrZero):defaultHexValue=''
_T11NsRegFabricPortName_Type.__name__=_I
_T11NsRegFabricPortName_Object=MibTableColumn
t11NsRegFabricPortName=_T11NsRegFabricPortName_Object((1,3,6,1,2,1,135,1,1,2,1,11),_T11NsRegFabricPortName_Type())
t11NsRegFabricPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegFabricPortName.setStatus(_A)
class _T11NsRegHardAddress_Type(FcAddressIdOrZero):defaultHexValue=''
_T11NsRegHardAddress_Type.__name__=_S
_T11NsRegHardAddress_Object=MibTableColumn
t11NsRegHardAddress=_T11NsRegHardAddress_Object((1,3,6,1,2,1,135,1,1,2,1,12),_T11NsRegHardAddress_Type())
t11NsRegHardAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegHardAddress.setStatus(_A)
class _T11NsRegSymbolicPortName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_T11NsRegSymbolicPortName_Type.__name__=_M
_T11NsRegSymbolicPortName_Object=MibTableColumn
t11NsRegSymbolicPortName=_T11NsRegSymbolicPortName_Object((1,3,6,1,2,1,135,1,1,2,1,13),_T11NsRegSymbolicPortName_Type())
t11NsRegSymbolicPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegSymbolicPortName.setStatus(_A)
class _T11NsRegSymbolicNodeName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_T11NsRegSymbolicNodeName_Type.__name__=_M
_T11NsRegSymbolicNodeName_Object=MibTableColumn
t11NsRegSymbolicNodeName=_T11NsRegSymbolicNodeName_Object((1,3,6,1,2,1,135,1,1,2,1,14),_T11NsRegSymbolicNodeName_Type())
t11NsRegSymbolicNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegSymbolicNodeName.setStatus(_A)
class _T11NsRegFc4Features_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(128,128))
_T11NsRegFc4Features_Type.__name__=_D
_T11NsRegFc4Features_Object=MibTableColumn
t11NsRegFc4Features=_T11NsRegFc4Features_Object((1,3,6,1,2,1,135,1,1,2,1,15),_T11NsRegFc4Features_Type())
t11NsRegFc4Features.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegFc4Features.setStatus(_A)
_T11NsRegFc4DescriptorTable_Object=MibTable
t11NsRegFc4DescriptorTable=_T11NsRegFc4DescriptorTable_Object((1,3,6,1,2,1,135,1,1,3))
if mibBuilder.loadTexts:t11NsRegFc4DescriptorTable.setStatus(_A)
_T11NsRegFc4DescriptorEntry_Object=MibTableRow
t11NsRegFc4DescriptorEntry=_T11NsRegFc4DescriptorEntry_Object((1,3,6,1,2,1,135,1,1,3,1))
t11NsRegFc4DescriptorEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H),(0,_B,_L),(0,_B,_Y))
if mibBuilder.loadTexts:t11NsRegFc4DescriptorEntry.setStatus(_A)
class _T11NsRegFc4TypeValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_T11NsRegFc4TypeValue_Type.__name__=_J
_T11NsRegFc4TypeValue_Object=MibTableColumn
t11NsRegFc4TypeValue=_T11NsRegFc4TypeValue_Object((1,3,6,1,2,1,135,1,1,3,1,1),_T11NsRegFc4TypeValue_Type())
t11NsRegFc4TypeValue.setMaxAccess(_K)
if mibBuilder.loadTexts:t11NsRegFc4TypeValue.setStatus(_A)
class _T11NsRegFc4Descriptor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_T11NsRegFc4Descriptor_Type.__name__=_D
_T11NsRegFc4Descriptor_Object=MibTableColumn
t11NsRegFc4Descriptor=_T11NsRegFc4Descriptor_Object((1,3,6,1,2,1,135,1,1,3,1,2),_T11NsRegFc4Descriptor_Type())
t11NsRegFc4Descriptor.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRegFc4Descriptor.setStatus(_A)
_T11NsRejectTable_Object=MibTable
t11NsRejectTable=_T11NsRejectTable_Object((1,3,6,1,2,1,135,1,1,4))
if mibBuilder.loadTexts:t11NsRejectTable.setStatus(_A)
_T11NsRejectEntry_Object=MibTableRow
t11NsRejectEntry=_T11NsRejectEntry_Object((1,3,6,1,2,1,135,1,1,4,1))
t11NsRejectEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H),(0,_B,_L))
if mibBuilder.loadTexts:t11NsRejectEntry.setStatus(_A)
class _T11NsRejectCtCommandString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_T11NsRejectCtCommandString_Type.__name__=_D
_T11NsRejectCtCommandString_Object=MibTableColumn
t11NsRejectCtCommandString=_T11NsRejectCtCommandString_Object((1,3,6,1,2,1,135,1,1,4,1,1),_T11NsRejectCtCommandString_Type())
t11NsRejectCtCommandString.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRejectCtCommandString.setStatus(_A)
_T11NsRejectReasonCode_Type=T11NsGs4RejectReasonCode
_T11NsRejectReasonCode_Object=MibTableColumn
t11NsRejectReasonCode=_T11NsRejectReasonCode_Object((1,3,6,1,2,1,135,1,1,4,1,2),_T11NsRejectReasonCode_Type())
t11NsRejectReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRejectReasonCode.setStatus(_A)
_T11NsRejReasonCodeExp_Type=T11NsRejReasonCodeExpl
_T11NsRejReasonCodeExp_Object=MibTableColumn
t11NsRejReasonCodeExp=_T11NsRejReasonCodeExp_Object((1,3,6,1,2,1,135,1,1,4,1,3),_T11NsRejReasonCodeExp_Type())
t11NsRejReasonCodeExp.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRejReasonCodeExp.setStatus(_A)
class _T11NsRejReasonVendorCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_T11NsRejReasonVendorCode_Type.__name__=_D
_T11NsRejReasonVendorCode_Object=MibTableColumn
t11NsRejReasonVendorCode=_T11NsRejReasonVendorCode_Object((1,3,6,1,2,1,135,1,1,4,1,4),_T11NsRejReasonVendorCode_Type())
t11NsRejReasonVendorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRejReasonVendorCode.setStatus(_A)
_T11NsStatistics_ObjectIdentity=ObjectIdentity
t11NsStatistics=_T11NsStatistics_ObjectIdentity((1,3,6,1,2,1,135,1,2))
_T11NsStatsTable_Object=MibTable
t11NsStatsTable=_T11NsStatsTable_Object((1,3,6,1,2,1,135,1,2,1))
if mibBuilder.loadTexts:t11NsStatsTable.setStatus(_A)
_T11NsStatsEntry_Object=MibTableRow
t11NsStatsEntry=_T11NsStatsEntry_Object((1,3,6,1,2,1,135,1,2,1,1))
t11NsStatsEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:t11NsStatsEntry.setStatus(_A)
_T11NsInGetReqs_Type=Counter32
_T11NsInGetReqs_Object=MibTableColumn
t11NsInGetReqs=_T11NsInGetReqs_Object((1,3,6,1,2,1,135,1,2,1,1,1),_T11NsInGetReqs_Type())
t11NsInGetReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInGetReqs.setStatus(_A)
_T11NsOutGetReqs_Type=Counter32
_T11NsOutGetReqs_Object=MibTableColumn
t11NsOutGetReqs=_T11NsOutGetReqs_Object((1,3,6,1,2,1,135,1,2,1,1,2),_T11NsOutGetReqs_Type())
t11NsOutGetReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsOutGetReqs.setStatus(_A)
_T11NsInRegReqs_Type=Counter32
_T11NsInRegReqs_Object=MibTableColumn
t11NsInRegReqs=_T11NsInRegReqs_Object((1,3,6,1,2,1,135,1,2,1,1,3),_T11NsInRegReqs_Type())
t11NsInRegReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInRegReqs.setStatus(_A)
_T11NsInDeRegReqs_Type=Counter32
_T11NsInDeRegReqs_Object=MibTableColumn
t11NsInDeRegReqs=_T11NsInDeRegReqs_Object((1,3,6,1,2,1,135,1,2,1,1,4),_T11NsInDeRegReqs_Type())
t11NsInDeRegReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInDeRegReqs.setStatus(_A)
_T11NsInRscns_Type=Counter32
_T11NsInRscns_Object=MibTableColumn
t11NsInRscns=_T11NsInRscns_Object((1,3,6,1,2,1,135,1,2,1,1,5),_T11NsInRscns_Type())
t11NsInRscns.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsInRscns.setStatus(_A)
_T11NsOutRscns_Type=Counter32
_T11NsOutRscns_Object=MibTableColumn
t11NsOutRscns=_T11NsOutRscns_Object((1,3,6,1,2,1,135,1,2,1,1,6),_T11NsOutRscns_Type())
t11NsOutRscns.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsOutRscns.setStatus(_A)
_T11NsRejects_Type=Counter32
_T11NsRejects_Object=MibTableColumn
t11NsRejects=_T11NsRejects_Object((1,3,6,1,2,1,135,1,2,1,1,7),_T11NsRejects_Type())
t11NsRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsRejects.setStatus(_A)
_T11NsDatabaseFull_Type=TruthValue
_T11NsDatabaseFull_Object=MibTableColumn
t11NsDatabaseFull=_T11NsDatabaseFull_Object((1,3,6,1,2,1,135,1,2,1,1,8),_T11NsDatabaseFull_Type())
t11NsDatabaseFull.setMaxAccess(_C)
if mibBuilder.loadTexts:t11NsDatabaseFull.setStatus(_A)
_T11NsMIBConformance_ObjectIdentity=ObjectIdentity
t11NsMIBConformance=_T11NsMIBConformance_ObjectIdentity((1,3,6,1,2,1,135,2))
_T11NsMIBCompliances_ObjectIdentity=ObjectIdentity
t11NsMIBCompliances=_T11NsMIBCompliances_ObjectIdentity((1,3,6,1,2,1,135,2,1))
_T11NsMIBGroups_ObjectIdentity=ObjectIdentity
t11NsMIBGroups=_T11NsMIBGroups_ObjectIdentity((1,3,6,1,2,1,135,2,2))
t11NsDBGroup=ObjectGroup((1,3,6,1,2,1,135,2,2,1))
t11NsDBGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_N),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:t11NsDBGroup.setStatus(_A)
t11NsRequestStatsGroup=ObjectGroup((1,3,6,1,2,1,135,2,2,2))
t11NsRequestStatsGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:t11NsRequestStatsGroup.setStatus(_A)
t11NsRscnStatsGroup=ObjectGroup((1,3,6,1,2,1,135,2,2,3))
t11NsRscnStatsGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:t11NsRscnStatsGroup.setStatus(_A)
t11NsRejectStatsGroup=ObjectGroup((1,3,6,1,2,1,135,2,2,4))
t11NsRejectStatsGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:t11NsRejectStatsGroup.setStatus(_A)
t11NsNotifyControlGroup=ObjectGroup((1,3,6,1,2,1,135,2,2,5))
t11NsNotifyControlGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_y)))
if mibBuilder.loadTexts:t11NsNotifyControlGroup.setStatus(_A)
t11NsRejectRegNotify=NotificationType((1,3,6,1,2,1,135,0,1))
t11NsRejectRegNotify.setObjects(*((_W,_X),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:t11NsRejectRegNotify.setStatus(_A)
t11NsNotifyGroup=NotificationGroup((1,3,6,1,2,1,135,2,2,6))
t11NsNotifyGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:t11NsNotifyGroup.setStatus(_A)
t11NsMIBCompliance=ModuleCompliance((1,3,6,1,2,1,135,2,1,1))
t11NsMIBCompliance.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:t11NsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'T11NsGs4RejectReasonCode':T11NsGs4RejectReasonCode,'T11NsRejReasonCodeExpl':T11NsRejReasonCodeExpl,'t11FcNameServerMIB':t11FcNameServerMIB,'t11NsNotifications':t11NsNotifications,_z:t11NsRejectRegNotify,'t11NsMIBObjects':t11NsMIBObjects,'t11NsStatus':t11NsStatus,'t11NsInfoSubsetTable':t11NsInfoSubsetTable,'t11NsInfoSubsetEntry':t11NsInfoSubsetEntry,_G:t11NsInfoSubsetIndex,_Z:t11NsInfoSubsetSwitchIndex,_a:t11NsInfoSubsetTableLastChange,_b:t11NsInfoSubsetNumRows,_w:t11NsInfoSubsetTotalRejects,_y:t11NsInfoSubsetRejReqNotfyEnable,'t11NsRegTable':t11NsRegTable,'t11NsRegEntry':t11NsRegEntry,_H:t11NsRegFabricIndex,_L:t11NsRegPortIdentifier,_N:t11NsRegPortName,_c:t11NsRegNodeName,_d:t11NsRegClassOfSvc,_e:t11NsRegNodeIpAddress,_f:t11NsRegProcAssoc,_g:t11NsRegFc4Type,_h:t11NsRegPortType,_i:t11NsRegPortIpAddress,_j:t11NsRegFabricPortName,_k:t11NsRegHardAddress,_l:t11NsRegSymbolicPortName,_m:t11NsRegSymbolicNodeName,_n:t11NsRegFc4Features,'t11NsRegFc4DescriptorTable':t11NsRegFc4DescriptorTable,'t11NsRegFc4DescriptorEntry':t11NsRegFc4DescriptorEntry,_Y:t11NsRegFc4TypeValue,_o:t11NsRegFc4Descriptor,'t11NsRejectTable':t11NsRejectTable,'t11NsRejectEntry':t11NsRejectEntry,_O:t11NsRejectCtCommandString,_P:t11NsRejectReasonCode,_Q:t11NsRejReasonCodeExp,_R:t11NsRejReasonVendorCode,'t11NsStatistics':t11NsStatistics,'t11NsStatsTable':t11NsStatsTable,'t11NsStatsEntry':t11NsStatsEntry,_p:t11NsInGetReqs,_q:t11NsOutGetReqs,_r:t11NsInRegReqs,_s:t11NsInDeRegReqs,_u:t11NsInRscns,_v:t11NsOutRscns,_x:t11NsRejects,_t:t11NsDatabaseFull,'t11NsMIBConformance':t11NsMIBConformance,'t11NsMIBCompliances':t11NsMIBCompliances,'t11NsMIBCompliance':t11NsMIBCompliance,'t11NsMIBGroups':t11NsMIBGroups,_A0:t11NsDBGroup,'t11NsRequestStatsGroup':t11NsRequestStatsGroup,'t11NsRscnStatsGroup':t11NsRscnStatsGroup,'t11NsRejectStatsGroup':t11NsRejectStatsGroup,_A1:t11NsNotifyControlGroup,_A2:t11NsNotifyGroup})