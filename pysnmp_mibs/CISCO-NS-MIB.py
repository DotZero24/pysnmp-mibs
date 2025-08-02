_A4='fcNameServerDBGroup3'
_A3='fcNameServerDBGroup2'
_A2='fcNameServerDBGroup1'
_A1='fcNameServerDBGroup'
_A0='fcNameServerEntryDelete'
_z='fcNameServerEntryAdd'
_y='fcNameServerPermanentPortName'
_x='fcNameServerPortFunction'
_w='fcNameServerRejReqNotifyEnable'
_v='fcNameServerRejects'
_u='fcNameServerOutRscns'
_t='fcNameServerInRscns'
_s='fcNameServerInDeRegReqs'
_r='fcNameServerInRegReqs'
_q='fcNameServerOutGetReqs'
_p='fcNameServerInGetReqs'
_o='fcNameServerTotalRejects'
_n='fcNameServerPortIdentifier'
_m='TruthValue'
_l='notifyVsanIndex'
_k='FcNameIdOrZero'
_j='fcNameServerNotifyGroupRev1'
_i='fcNameServerNotifyGroup'
_h='fcNameServerDatabaseFull'
_g='fcNameServerRejectRegNotify'
_f='fcNameServerRejReasonCodeExp'
_e='fcNameServerRejectReasonCode'
_d='0000000000000000'
_c='Integer32'
_b='SnmpAdminString'
_a='vsanIndex'
_Z='FcNameId'
_Y='fcNameServerNotifyControlGroup'
_X='fcNameServerStatsGroup'
_W='fcNameServerFC4Features'
_V='fcNameServerSymbolicNodeName'
_U='fcNameServerSymbolicPortName'
_T='fcNameServerHardAddress'
_S='fcNameServerFabricPortName'
_R='fcNameServerPortIpAddress'
_Q='fcNameServerFC4Type'
_P='fcNameServerProcAssoc'
_O='fcNameServerNodeIpAddress'
_N='fcNameServerClassOfSvc'
_M='fcNameServerNodeName'
_L='fcNameServerTableLastChange'
_K='fcNameServerNumRows'
_J='fcNameServerProxyPortName'
_I='CISCO-VSAN-MIB'
_H='OctetString'
_G='fcNameServerPortType'
_F='deprecated'
_E='fcNameServerPortName'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-NS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddressId,FcClassOfServices,FcNameId,FcNameIdOrZero=mibBuilder.importSymbols('CISCO-ST-TC','FcAddressId','FcClassOfServices',_Z,_k)
notifyVsanIndex,vsanIndex=mibBuilder.importSymbols(_I,_l,_a)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_c,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_m)
ciscoNsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,293))
if mibBuilder.loadTexts:ciscoNsMIB.setRevisions(('2004-08-30 00:00','2004-02-19 00:00','2003-03-06 00:00','2002-10-03 00:00'))
class FcGs3RejectReasonCode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),('invalidCmdCode',2),('invalidVerLevel',3),('logicalError',4),('invalidIUSize',5),('logicalBusy',6),('protocolError',7),('unableToPerformCmdReq',8),('cmdNotSupported',9),('vendorError',10)))
class FcNameServerRejReasonExpl(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('noAdditionalExplanation',1),('portIdentifierNotRegistered',2),('portNameNotRegistered',3),('nodeNameNotRegistered',4),('classOfServiceNotRegistered',5),('nodeIpAddressNotRegistered',6),('ipaNotRegistered',7),('fc4TypeNotRegistered',8),('symbolicPortNameNotRegistered',9),('symbolicNodeNameNotRegistered',10),('portTypeNotRegistered',11),('portIpAddressNotRegistered',12),('fabricPortNameNotRegistered',13),('hardAddressNotRegistered',14),('fc4DescriptorNotRegistered',15),('fc4FeaturesNotRegistered',16),('accessDenied',17),('unacceptablePortIdentifier',18),('databaseEmpty',19),('noObjectRegInSpecifiedScope',20)))
_CiscoNameServerMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNameServerMIBObjects=_CiscoNameServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,293,1))
_FcNameServerConfiguration_ObjectIdentity=ObjectIdentity
fcNameServerConfiguration=_FcNameServerConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,293,1,1))
_FcNameServerProxyPortTable_Object=MibTable
fcNameServerProxyPortTable=_FcNameServerProxyPortTable_Object((1,3,6,1,4,1,9,9,293,1,1,1))
if mibBuilder.loadTexts:fcNameServerProxyPortTable.setStatus(_B)
_FcNameServerProxyPortEntry_Object=MibTableRow
fcNameServerProxyPortEntry=_FcNameServerProxyPortEntry_Object((1,3,6,1,4,1,9,9,293,1,1,1,1))
fcNameServerProxyPortEntry.setIndexNames((0,_I,_a))
if mibBuilder.loadTexts:fcNameServerProxyPortEntry.setStatus(_B)
class _FcNameServerProxyPortName_Type(FcNameIdOrZero):defaultHexValue=''
_FcNameServerProxyPortName_Type.__name__=_k
_FcNameServerProxyPortName_Object=MibTableColumn
fcNameServerProxyPortName=_FcNameServerProxyPortName_Object((1,3,6,1,4,1,9,9,293,1,1,1,1,1),_FcNameServerProxyPortName_Type())
fcNameServerProxyPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerProxyPortName.setStatus(_B)
_FcNameServerTableLastChange_Type=TimeStamp
_FcNameServerTableLastChange_Object=MibScalar
fcNameServerTableLastChange=_FcNameServerTableLastChange_Object((1,3,6,1,4,1,9,9,293,1,1,2),_FcNameServerTableLastChange_Type())
fcNameServerTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerTableLastChange.setStatus(_B)
class _FcNameServerNumRows_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FcNameServerNumRows_Type.__name__=_c
_FcNameServerNumRows_Object=MibScalar
fcNameServerNumRows=_FcNameServerNumRows_Object((1,3,6,1,4,1,9,9,293,1,1,3),_FcNameServerNumRows_Type())
fcNameServerNumRows.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerNumRows.setStatus(_B)
_FcNameServerTable_Object=MibTable
fcNameServerTable=_FcNameServerTable_Object((1,3,6,1,4,1,9,9,293,1,1,4))
if mibBuilder.loadTexts:fcNameServerTable.setStatus(_B)
_FcNameServerEntry_Object=MibTableRow
fcNameServerEntry=_FcNameServerEntry_Object((1,3,6,1,4,1,9,9,293,1,1,4,1))
fcNameServerEntry.setIndexNames((0,_I,_a),(0,_A,_n))
if mibBuilder.loadTexts:fcNameServerEntry.setStatus(_B)
_FcNameServerPortIdentifier_Type=FcAddressId
_FcNameServerPortIdentifier_Object=MibTableColumn
fcNameServerPortIdentifier=_FcNameServerPortIdentifier_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,1),_FcNameServerPortIdentifier_Type())
fcNameServerPortIdentifier.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fcNameServerPortIdentifier.setStatus(_B)
class _FcNameServerPortName_Type(FcNameId):defaultHexValue=_d
_FcNameServerPortName_Type.__name__=_Z
_FcNameServerPortName_Object=MibTableColumn
fcNameServerPortName=_FcNameServerPortName_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,2),_FcNameServerPortName_Type())
fcNameServerPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerPortName.setStatus(_B)
class _FcNameServerNodeName_Type(FcNameId):defaultHexValue=_d
_FcNameServerNodeName_Type.__name__=_Z
_FcNameServerNodeName_Object=MibTableColumn
fcNameServerNodeName=_FcNameServerNodeName_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,3),_FcNameServerNodeName_Type())
fcNameServerNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerNodeName.setStatus(_B)
_FcNameServerClassOfSvc_Type=FcClassOfServices
_FcNameServerClassOfSvc_Object=MibTableColumn
fcNameServerClassOfSvc=_FcNameServerClassOfSvc_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,4),_FcNameServerClassOfSvc_Type())
fcNameServerClassOfSvc.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerClassOfSvc.setStatus(_B)
class _FcNameServerNodeIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FcNameServerNodeIpAddress_Type.__name__=_H
_FcNameServerNodeIpAddress_Object=MibTableColumn
fcNameServerNodeIpAddress=_FcNameServerNodeIpAddress_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,5),_FcNameServerNodeIpAddress_Type())
fcNameServerNodeIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerNodeIpAddress.setStatus(_B)
class _FcNameServerProcAssoc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_FcNameServerProcAssoc_Type.__name__=_H
_FcNameServerProcAssoc_Object=MibTableColumn
fcNameServerProcAssoc=_FcNameServerProcAssoc_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,6),_FcNameServerProcAssoc_Type())
fcNameServerProcAssoc.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerProcAssoc.setStatus(_B)
class _FcNameServerFC4Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FcNameServerFC4Type_Type.__name__=_H
_FcNameServerFC4Type_Object=MibTableColumn
fcNameServerFC4Type=_FcNameServerFC4Type_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,7),_FcNameServerFC4Type_Type())
fcNameServerFC4Type.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerFC4Type.setStatus(_B)
class _FcNameServerPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('nPort',2),('nlPort',3)))
_FcNameServerPortType_Type.__name__=_c
_FcNameServerPortType_Object=MibTableColumn
fcNameServerPortType=_FcNameServerPortType_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,8),_FcNameServerPortType_Type())
fcNameServerPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerPortType.setStatus(_B)
class _FcNameServerPortIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FcNameServerPortIpAddress_Type.__name__=_H
_FcNameServerPortIpAddress_Object=MibTableColumn
fcNameServerPortIpAddress=_FcNameServerPortIpAddress_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,9),_FcNameServerPortIpAddress_Type())
fcNameServerPortIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerPortIpAddress.setStatus(_B)
class _FcNameServerFabricPortName_Type(FcNameId):defaultHexValue=_d
_FcNameServerFabricPortName_Type.__name__=_Z
_FcNameServerFabricPortName_Object=MibTableColumn
fcNameServerFabricPortName=_FcNameServerFabricPortName_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,10),_FcNameServerFabricPortName_Type())
fcNameServerFabricPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerFabricPortName.setStatus(_B)
_FcNameServerHardAddress_Type=FcAddressId
_FcNameServerHardAddress_Object=MibTableColumn
fcNameServerHardAddress=_FcNameServerHardAddress_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,11),_FcNameServerHardAddress_Type())
fcNameServerHardAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerHardAddress.setStatus(_B)
class _FcNameServerSymbolicPortName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FcNameServerSymbolicPortName_Type.__name__=_b
_FcNameServerSymbolicPortName_Object=MibTableColumn
fcNameServerSymbolicPortName=_FcNameServerSymbolicPortName_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,12),_FcNameServerSymbolicPortName_Type())
fcNameServerSymbolicPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerSymbolicPortName.setStatus(_B)
class _FcNameServerSymbolicNodeName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FcNameServerSymbolicNodeName_Type.__name__=_b
_FcNameServerSymbolicNodeName_Object=MibTableColumn
fcNameServerSymbolicNodeName=_FcNameServerSymbolicNodeName_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,13),_FcNameServerSymbolicNodeName_Type())
fcNameServerSymbolicNodeName.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerSymbolicNodeName.setStatus(_B)
class _FcNameServerFC4Features_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FcNameServerFC4Features_Type.__name__=_H
_FcNameServerFC4Features_Object=MibTableColumn
fcNameServerFC4Features=_FcNameServerFC4Features_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,14),_FcNameServerFC4Features_Type())
fcNameServerFC4Features.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerFC4Features.setStatus(_B)
class _FcNameServerPortFunction_Type(Bits):namedValues=NamedValues(*(('trapPort',0),('vep',1),('volOwner',2),('ipfcPort',3),('intPort',4)))
_FcNameServerPortFunction_Type.__name__='Bits'
_FcNameServerPortFunction_Object=MibTableColumn
fcNameServerPortFunction=_FcNameServerPortFunction_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,15),_FcNameServerPortFunction_Type())
fcNameServerPortFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerPortFunction.setStatus(_F)
_FcNameServerPermanentPortName_Type=FcNameId
_FcNameServerPermanentPortName_Object=MibTableColumn
fcNameServerPermanentPortName=_FcNameServerPermanentPortName_Object((1,3,6,1,4,1,9,9,293,1,1,4,1,16),_FcNameServerPermanentPortName_Type())
fcNameServerPermanentPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerPermanentPortName.setStatus(_B)
class _FcNameServerRejReqNotifyEnable_Type(TruthValue):defaultValue=2
_FcNameServerRejReqNotifyEnable_Type.__name__=_m
_FcNameServerRejReqNotifyEnable_Object=MibScalar
fcNameServerRejReqNotifyEnable=_FcNameServerRejReqNotifyEnable_Object((1,3,6,1,4,1,9,9,293,1,1,5),_FcNameServerRejReqNotifyEnable_Type())
fcNameServerRejReqNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fcNameServerRejReqNotifyEnable.setStatus(_B)
_FcNameServerStats_ObjectIdentity=ObjectIdentity
fcNameServerStats=_FcNameServerStats_ObjectIdentity((1,3,6,1,4,1,9,9,293,1,2))
_FcNameServerTotalRejects_Type=Counter32
_FcNameServerTotalRejects_Object=MibScalar
fcNameServerTotalRejects=_FcNameServerTotalRejects_Object((1,3,6,1,4,1,9,9,293,1,2,1),_FcNameServerTotalRejects_Type())
fcNameServerTotalRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerTotalRejects.setStatus(_B)
_FcNameServerStatsTable_Object=MibTable
fcNameServerStatsTable=_FcNameServerStatsTable_Object((1,3,6,1,4,1,9,9,293,1,2,2))
if mibBuilder.loadTexts:fcNameServerStatsTable.setStatus(_B)
_FcNameServerStatsEntry_Object=MibTableRow
fcNameServerStatsEntry=_FcNameServerStatsEntry_Object((1,3,6,1,4,1,9,9,293,1,2,2,1))
fcNameServerStatsEntry.setIndexNames((0,_I,_a))
if mibBuilder.loadTexts:fcNameServerStatsEntry.setStatus(_B)
_FcNameServerInGetReqs_Type=Counter32
_FcNameServerInGetReqs_Object=MibTableColumn
fcNameServerInGetReqs=_FcNameServerInGetReqs_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,1),_FcNameServerInGetReqs_Type())
fcNameServerInGetReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerInGetReqs.setStatus(_B)
_FcNameServerOutGetReqs_Type=Counter32
_FcNameServerOutGetReqs_Object=MibTableColumn
fcNameServerOutGetReqs=_FcNameServerOutGetReqs_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,2),_FcNameServerOutGetReqs_Type())
fcNameServerOutGetReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerOutGetReqs.setStatus(_B)
_FcNameServerInRegReqs_Type=Counter32
_FcNameServerInRegReqs_Object=MibTableColumn
fcNameServerInRegReqs=_FcNameServerInRegReqs_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,3),_FcNameServerInRegReqs_Type())
fcNameServerInRegReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerInRegReqs.setStatus(_B)
_FcNameServerInDeRegReqs_Type=Counter32
_FcNameServerInDeRegReqs_Object=MibTableColumn
fcNameServerInDeRegReqs=_FcNameServerInDeRegReqs_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,4),_FcNameServerInDeRegReqs_Type())
fcNameServerInDeRegReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerInDeRegReqs.setStatus(_B)
_FcNameServerInRscns_Type=Counter32
_FcNameServerInRscns_Object=MibTableColumn
fcNameServerInRscns=_FcNameServerInRscns_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,5),_FcNameServerInRscns_Type())
fcNameServerInRscns.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerInRscns.setStatus(_B)
_FcNameServerOutRscns_Type=Counter32
_FcNameServerOutRscns_Object=MibTableColumn
fcNameServerOutRscns=_FcNameServerOutRscns_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,6),_FcNameServerOutRscns_Type())
fcNameServerOutRscns.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerOutRscns.setStatus(_B)
_FcNameServerRejects_Type=Counter32
_FcNameServerRejects_Object=MibTableColumn
fcNameServerRejects=_FcNameServerRejects_Object((1,3,6,1,4,1,9,9,293,1,2,2,1,7),_FcNameServerRejects_Type())
fcNameServerRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerRejects.setStatus(_B)
_FcNameServerInformation_ObjectIdentity=ObjectIdentity
fcNameServerInformation=_FcNameServerInformation_ObjectIdentity((1,3,6,1,4,1,9,9,293,1,3))
_FcNameServerRejectReasonCode_Type=FcGs3RejectReasonCode
_FcNameServerRejectReasonCode_Object=MibScalar
fcNameServerRejectReasonCode=_FcNameServerRejectReasonCode_Object((1,3,6,1,4,1,9,9,293,1,3,1),_FcNameServerRejectReasonCode_Type())
fcNameServerRejectReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerRejectReasonCode.setStatus(_B)
_FcNameServerRejReasonCodeExp_Type=FcNameServerRejReasonExpl
_FcNameServerRejReasonCodeExp_Object=MibScalar
fcNameServerRejReasonCodeExp=_FcNameServerRejReasonCodeExp_Object((1,3,6,1,4,1,9,9,293,1,3,2),_FcNameServerRejReasonCodeExp_Type())
fcNameServerRejReasonCodeExp.setMaxAccess(_C)
if mibBuilder.loadTexts:fcNameServerRejReasonCodeExp.setStatus(_B)
_FcNameServerNotification_ObjectIdentity=ObjectIdentity
fcNameServerNotification=_FcNameServerNotification_ObjectIdentity((1,3,6,1,4,1,9,9,293,1,4))
_FcNameServerNotifications_ObjectIdentity=ObjectIdentity
fcNameServerNotifications=_FcNameServerNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,293,1,4,0))
_FcNameServerMIBConformance_ObjectIdentity=ObjectIdentity
fcNameServerMIBConformance=_FcNameServerMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,293,2))
_FcNameServerMIBCompliances_ObjectIdentity=ObjectIdentity
fcNameServerMIBCompliances=_FcNameServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,293,2,1))
_FcNameServerMIBGroups_ObjectIdentity=ObjectIdentity
fcNameServerMIBGroups=_FcNameServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,293,2,2))
fcNameServerDBGroup=ObjectGroup((1,3,6,1,4,1,9,9,293,2,2,1))
fcNameServerDBGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_E),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_G),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:fcNameServerDBGroup.setStatus(_F)
fcNameServerStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,293,2,2,2))
fcNameServerStatsGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:fcNameServerStatsGroup.setStatus(_B)
fcNameServerNotifyControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,293,2,2,3))
fcNameServerNotifyControlGroup.setObjects(*((_A,_e),(_A,_f),(_A,_w)))
if mibBuilder.loadTexts:fcNameServerNotifyControlGroup.setStatus(_B)
fcNameServerDBGroup1=ObjectGroup((1,3,6,1,4,1,9,9,293,2,2,5))
fcNameServerDBGroup1.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_E),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_G),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_x)))
if mibBuilder.loadTexts:fcNameServerDBGroup1.setStatus(_F)
fcNameServerDBGroup2=ObjectGroup((1,3,6,1,4,1,9,9,293,2,2,7))
fcNameServerDBGroup2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_E),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_G),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:fcNameServerDBGroup2.setStatus(_B)
fcNameServerDBGroup3=ObjectGroup((1,3,6,1,4,1,9,9,293,2,2,8))
fcNameServerDBGroup3.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_E),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_G),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_y)))
if mibBuilder.loadTexts:fcNameServerDBGroup3.setStatus(_B)
fcNameServerRejectRegNotify=NotificationType((1,3,6,1,4,1,9,9,293,1,4,0,1))
fcNameServerRejectRegNotify.setObjects(*((_A,_E),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:fcNameServerRejectRegNotify.setStatus(_B)
fcNameServerDatabaseFull=NotificationType((1,3,6,1,4,1,9,9,293,1,4,0,2))
fcNameServerDatabaseFull.setObjects((_I,_l))
if mibBuilder.loadTexts:fcNameServerDatabaseFull.setStatus(_B)
fcNameServerEntryAdd=NotificationType((1,3,6,1,4,1,9,9,293,1,4,0,3))
fcNameServerEntryAdd.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:fcNameServerEntryAdd.setStatus(_B)
fcNameServerEntryDelete=NotificationType((1,3,6,1,4,1,9,9,293,1,4,0,4))
fcNameServerEntryDelete.setObjects(*((_A,_E),(_A,_G)))
if mibBuilder.loadTexts:fcNameServerEntryDelete.setStatus(_B)
fcNameServerNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,293,2,2,4))
fcNameServerNotifyGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:fcNameServerNotifyGroup.setStatus(_F)
fcNameServerNotifyGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,293,2,2,6))
fcNameServerNotifyGroupRev1.setObjects(*((_A,_g),(_A,_h),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:fcNameServerNotifyGroupRev1.setStatus(_B)
fcNameServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,293,2,1,1))
fcNameServerMIBCompliance.setObjects(*((_A,_A1),(_A,_X),(_A,_Y),(_A,_i)))
if mibBuilder.loadTexts:fcNameServerMIBCompliance.setStatus(_F)
fcNameServerMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,293,2,1,2))
fcNameServerMIBCompliance1.setObjects(*((_A,_A2),(_A,_X),(_A,_Y),(_A,_i)))
if mibBuilder.loadTexts:fcNameServerMIBCompliance1.setStatus(_F)
fcNameServerMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,293,2,1,3))
fcNameServerMIBCompliance2.setObjects(*((_A,_A3),(_A,_X),(_A,_Y),(_A,_j)))
if mibBuilder.loadTexts:fcNameServerMIBCompliance2.setStatus(_F)
fcNameServerMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,293,2,1,4))
fcNameServerMIBCompliance3.setObjects(*((_A,_A4),(_A,_X),(_A,_Y),(_A,_j)))
if mibBuilder.loadTexts:fcNameServerMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FcGs3RejectReasonCode':FcGs3RejectReasonCode,'FcNameServerRejReasonExpl':FcNameServerRejReasonExpl,'ciscoNsMIB':ciscoNsMIB,'ciscoNameServerMIBObjects':ciscoNameServerMIBObjects,'fcNameServerConfiguration':fcNameServerConfiguration,'fcNameServerProxyPortTable':fcNameServerProxyPortTable,'fcNameServerProxyPortEntry':fcNameServerProxyPortEntry,_J:fcNameServerProxyPortName,_L:fcNameServerTableLastChange,_K:fcNameServerNumRows,'fcNameServerTable':fcNameServerTable,'fcNameServerEntry':fcNameServerEntry,_n:fcNameServerPortIdentifier,_E:fcNameServerPortName,_M:fcNameServerNodeName,_N:fcNameServerClassOfSvc,_O:fcNameServerNodeIpAddress,_P:fcNameServerProcAssoc,_Q:fcNameServerFC4Type,_G:fcNameServerPortType,_R:fcNameServerPortIpAddress,_S:fcNameServerFabricPortName,_T:fcNameServerHardAddress,_U:fcNameServerSymbolicPortName,_V:fcNameServerSymbolicNodeName,_W:fcNameServerFC4Features,_x:fcNameServerPortFunction,_y:fcNameServerPermanentPortName,_w:fcNameServerRejReqNotifyEnable,'fcNameServerStats':fcNameServerStats,_o:fcNameServerTotalRejects,'fcNameServerStatsTable':fcNameServerStatsTable,'fcNameServerStatsEntry':fcNameServerStatsEntry,_p:fcNameServerInGetReqs,_q:fcNameServerOutGetReqs,_r:fcNameServerInRegReqs,_s:fcNameServerInDeRegReqs,_t:fcNameServerInRscns,_u:fcNameServerOutRscns,_v:fcNameServerRejects,'fcNameServerInformation':fcNameServerInformation,_e:fcNameServerRejectReasonCode,_f:fcNameServerRejReasonCodeExp,'fcNameServerNotification':fcNameServerNotification,'fcNameServerNotifications':fcNameServerNotifications,_g:fcNameServerRejectRegNotify,_h:fcNameServerDatabaseFull,_z:fcNameServerEntryAdd,_A0:fcNameServerEntryDelete,'fcNameServerMIBConformance':fcNameServerMIBConformance,'fcNameServerMIBCompliances':fcNameServerMIBCompliances,'fcNameServerMIBCompliance':fcNameServerMIBCompliance,'fcNameServerMIBCompliance1':fcNameServerMIBCompliance1,'fcNameServerMIBCompliance2':fcNameServerMIBCompliance2,'fcNameServerMIBCompliance3':fcNameServerMIBCompliance3,'fcNameServerMIBGroups':fcNameServerMIBGroups,_A1:fcNameServerDBGroup,_X:fcNameServerStatsGroup,_Y:fcNameServerNotifyControlGroup,_i:fcNameServerNotifyGroup,_A2:fcNameServerDBGroup1,_j:fcNameServerNotifyGroupRev1,_A3:fcNameServerDBGroup2,_A4:fcNameServerDBGroup3})