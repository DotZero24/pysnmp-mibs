_y='bfdSessionGroup'
_x='dcBfdSessConfigDetectMult'
_w='dcBfdSessConfigReqMinEchoRxIntvl'
_v='dcBfdSessConfigReqMinRxInterval'
_u='dcBfdSessConfigDesiredMinTxIntvl'
_t='dcBfdSessConfigEchoFuncModeDsrd'
_s='dcBfdSessConfigDemandModeDsrd'
_r='dcBfdSessConfigRowStatus'
_q='dcBfdSessMapBfdIndex'
_p='bfdSessControlPlanIndepFlag'
_o='bfdSessDiag'
_n='bfdSessState'
_m='bfdSessApplicationSessions'
_l='bfdSessDiscriminator'
_k='bfdVersionNumber'
_j='bfdInterfaceScope'
_i='bfdReqMinRxInterval'
_h='bfdDesiredMinTxInterval'
_g='bfdRowStatus'
_f='bfdOperStatus'
_e='bfdAdminStatus'
_d='dcBfdSessConfigLocalAddr'
_c='dcBfdSessConfigLocalAddrType'
_b='dcBfdSessConfigAddr'
_a='dcBfdSessConfigAddrType'
_Z='dcBfdSessConfigIfIndex'
_Y='dcBfdSessConfigProtocol'
_X='dcBfdSessMapEntityIndex'
_W='dcBfdSessMapEntityType'
_V='bfdSessIndex'
_U='microseconds'
_T='Integer32'
_S='InterfaceScope'
_R='AdminStatus'
_Q='bfdSessLocalAddr'
_P='bfdSessLocalAddrType'
_O='bfdSessRemoteDiscr'
_N='bfdSessAddr'
_M='bfdSessAddrType'
_L='bfdSessIntface'
_K='read-write'
_J='InetAddress'
_I='TruthValue'
_H='bfdEntityIndex'
_G='Unsigned32'
_F='BfdInterval'
_E='not-accessible'
_D='read-only'
_C='read-create'
_B='DC-BFD-STUB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AdminStatus,EntityProcType,InterfaceScope,NpgOperStatus,NumericIndex=mibBuilder.importSymbols('DC-MASTER-TC',_R,'EntityProcType',_S,'NpgOperStatus','NumericIndex')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_T,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
bfdMIB=ModuleIdentity((1,3,6,1,4,1,629,10,11))
if mibBuilder.loadTexts:bfdMIB.setRevisions(('2015-02-09 00:00',))
class BfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdInterval(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class BfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,16,255)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9),('misconnectivity',16),('noContact',255)))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Opx_ObjectIdentity=ObjectIdentity
opx=_Opx_ObjectIdentity((1,3,6,1,4,1,629,10))
_BfdNotifications_ObjectIdentity=ObjectIdentity
bfdNotifications=_BfdNotifications_ObjectIdentity((1,3,6,1,4,1,629,10,11,0))
_BfdObjects_ObjectIdentity=ObjectIdentity
bfdObjects=_BfdObjects_ObjectIdentity((1,3,6,1,4,1,629,10,11,1))
_BfdEntityTable_Object=MibTable
bfdEntityTable=_BfdEntityTable_Object((1,3,6,1,4,1,629,10,11,1,1))
if mibBuilder.loadTexts:bfdEntityTable.setStatus(_A)
_BfdEntityEntry_Object=MibTableRow
bfdEntityEntry=_BfdEntityEntry_Object((1,3,6,1,4,1,629,10,11,1,1,1))
bfdEntityEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:bfdEntityEntry.setStatus(_A)
_BfdEntityIndex_Type=NumericIndex
_BfdEntityIndex_Object=MibTableColumn
bfdEntityIndex=_BfdEntityIndex_Object((1,3,6,1,4,1,629,10,11,1,1,1,1),_BfdEntityIndex_Type())
bfdEntityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bfdEntityIndex.setStatus(_A)
class _BfdAdminStatus_Type(AdminStatus):defaultValue=1
_BfdAdminStatus_Type.__name__=_R
_BfdAdminStatus_Object=MibTableColumn
bfdAdminStatus=_BfdAdminStatus_Object((1,3,6,1,4,1,629,10,11,1,1,1,2),_BfdAdminStatus_Type())
bfdAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdAdminStatus.setStatus(_A)
_BfdOperStatus_Type=NpgOperStatus
_BfdOperStatus_Object=MibTableColumn
bfdOperStatus=_BfdOperStatus_Object((1,3,6,1,4,1,629,10,11,1,1,1,3),_BfdOperStatus_Type())
bfdOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdOperStatus.setStatus(_A)
_BfdRowStatus_Type=RowStatus
_BfdRowStatus_Object=MibTableColumn
bfdRowStatus=_BfdRowStatus_Object((1,3,6,1,4,1,629,10,11,1,1,1,4),_BfdRowStatus_Type())
bfdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdRowStatus.setStatus(_A)
class _BfdVersionNumber_Type(Unsigned32):defaultValue=1
_BfdVersionNumber_Type.__name__=_G
_BfdVersionNumber_Object=MibTableColumn
bfdVersionNumber=_BfdVersionNumber_Object((1,3,6,1,4,1,629,10,11,1,1,1,5),_BfdVersionNumber_Type())
bfdVersionNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdVersionNumber.setStatus(_A)
class _BfdDesiredMinTxInterval_Type(BfdInterval):defaultValue=150000
_BfdDesiredMinTxInterval_Type.__name__=_F
_BfdDesiredMinTxInterval_Object=MibTableColumn
bfdDesiredMinTxInterval=_BfdDesiredMinTxInterval_Object((1,3,6,1,4,1,629,10,11,1,1,1,6),_BfdDesiredMinTxInterval_Type())
bfdDesiredMinTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdDesiredMinTxInterval.setStatus(_A)
if mibBuilder.loadTexts:bfdDesiredMinTxInterval.setUnits(_U)
class _BfdReqMinRxInterval_Type(BfdInterval):defaultValue=150000
_BfdReqMinRxInterval_Type.__name__=_F
_BfdReqMinRxInterval_Object=MibTableColumn
bfdReqMinRxInterval=_BfdReqMinRxInterval_Object((1,3,6,1,4,1,629,10,11,1,1,1,7),_BfdReqMinRxInterval_Type())
bfdReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdReqMinRxInterval.setStatus(_A)
if mibBuilder.loadTexts:bfdReqMinRxInterval.setUnits(_U)
class _BfdInterfaceScope_Type(InterfaceScope):defaultHexValue=''
_BfdInterfaceScope_Type.__name__=_S
_BfdInterfaceScope_Object=MibTableColumn
bfdInterfaceScope=_BfdInterfaceScope_Object((1,3,6,1,4,1,629,10,11,1,1,1,8),_BfdInterfaceScope_Type())
bfdInterfaceScope.setMaxAccess(_C)
if mibBuilder.loadTexts:bfdInterfaceScope.setStatus(_A)
_BfdSessionTable_Object=MibTable
bfdSessionTable=_BfdSessionTable_Object((1,3,6,1,4,1,629,10,11,1,2))
if mibBuilder.loadTexts:bfdSessionTable.setStatus(_A)
_BfdSessionEntry_Object=MibTableRow
bfdSessionEntry=_BfdSessionEntry_Object((1,3,6,1,4,1,629,10,11,1,2,1))
bfdSessionEntry.setIndexNames((0,_B,_H),(0,_B,_V))
if mibBuilder.loadTexts:bfdSessionEntry.setStatus(_A)
_BfdSessIndex_Type=BfdSessIndexTC
_BfdSessIndex_Object=MibTableColumn
bfdSessIndex=_BfdSessIndex_Object((1,3,6,1,4,1,629,10,11,1,2,1,1),_BfdSessIndex_Type())
bfdSessIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bfdSessIndex.setStatus(_A)
class _BfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BfdSessDiscriminator_Type.__name__=_G
_BfdSessDiscriminator_Object=MibTableColumn
bfdSessDiscriminator=_BfdSessDiscriminator_Object((1,3,6,1,4,1,629,10,11,1,2,1,4),_BfdSessDiscriminator_Type())
bfdSessDiscriminator.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessDiscriminator.setStatus(_A)
class _BfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_BfdSessRemoteDiscr_Type.__name__=_G
_BfdSessRemoteDiscr_Object=MibTableColumn
bfdSessRemoteDiscr=_BfdSessRemoteDiscr_Object((1,3,6,1,4,1,629,10,11,1,2,1,5),_BfdSessRemoteDiscr_Type())
bfdSessRemoteDiscr.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessRemoteDiscr.setStatus(_A)
class _BfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4)))
_BfdSessState_Type.__name__=_T
_BfdSessState_Object=MibTableColumn
bfdSessState=_BfdSessState_Object((1,3,6,1,4,1,629,10,11,1,2,1,7),_BfdSessState_Type())
bfdSessState.setMaxAccess(_K)
if mibBuilder.loadTexts:bfdSessState.setStatus(_A)
_BfdSessDiag_Type=BfdDiag
_BfdSessDiag_Object=MibTableColumn
bfdSessDiag=_BfdSessDiag_Object((1,3,6,1,4,1,629,10,11,1,2,1,9),_BfdSessDiag_Type())
bfdSessDiag.setMaxAccess(_K)
if mibBuilder.loadTexts:bfdSessDiag.setStatus(_A)
class _BfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=2
_BfdSessControlPlanIndepFlag_Type.__name__=_I
_BfdSessControlPlanIndepFlag_Object=MibTableColumn
bfdSessControlPlanIndepFlag=_BfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,629,10,11,1,2,1,13),_BfdSessControlPlanIndepFlag_Type())
bfdSessControlPlanIndepFlag.setMaxAccess(_K)
if mibBuilder.loadTexts:bfdSessControlPlanIndepFlag.setStatus(_A)
_BfdSessIntface_Type=InterfaceIndexOrZero
_BfdSessIntface_Object=MibTableColumn
bfdSessIntface=_BfdSessIntface_Object((1,3,6,1,4,1,629,10,11,1,2,1,14),_BfdSessIntface_Type())
bfdSessIntface.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessIntface.setStatus(_A)
_BfdSessAddrType_Type=InetAddressType
_BfdSessAddrType_Object=MibTableColumn
bfdSessAddrType=_BfdSessAddrType_Object((1,3,6,1,4,1,629,10,11,1,2,1,15),_BfdSessAddrType_Type())
bfdSessAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessAddrType.setStatus(_A)
class _BfdSessAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_BfdSessAddr_Type.__name__=_J
_BfdSessAddr_Object=MibTableColumn
bfdSessAddr=_BfdSessAddr_Object((1,3,6,1,4,1,629,10,11,1,2,1,16),_BfdSessAddr_Type())
bfdSessAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessAddr.setStatus(_A)
_BfdSessApplicationSessions_Type=Gauge32
_BfdSessApplicationSessions_Object=MibTableColumn
bfdSessApplicationSessions=_BfdSessApplicationSessions_Object((1,3,6,1,4,1,629,10,11,1,2,1,27),_BfdSessApplicationSessions_Type())
bfdSessApplicationSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessApplicationSessions.setStatus(_A)
_BfdSessLocalAddrType_Type=InetAddressType
_BfdSessLocalAddrType_Object=MibTableColumn
bfdSessLocalAddrType=_BfdSessLocalAddrType_Object((1,3,6,1,4,1,629,10,11,1,2,1,28),_BfdSessLocalAddrType_Type())
bfdSessLocalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessLocalAddrType.setStatus(_A)
_BfdSessLocalAddr_Type=InetAddress
_BfdSessLocalAddr_Object=MibTableColumn
bfdSessLocalAddr=_BfdSessLocalAddr_Object((1,3,6,1,4,1,629,10,11,1,2,1,29),_BfdSessLocalAddr_Type())
bfdSessLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bfdSessLocalAddr.setStatus(_A)
_DcBfdSessMapTable_Object=MibTable
dcBfdSessMapTable=_DcBfdSessMapTable_Object((1,3,6,1,4,1,629,10,11,1,5))
if mibBuilder.loadTexts:dcBfdSessMapTable.setStatus(_A)
_DcBfdSessMapEntry_Object=MibTableRow
dcBfdSessMapEntry=_DcBfdSessMapEntry_Object((1,3,6,1,4,1,629,10,11,1,5,1))
dcBfdSessMapEntry.setIndexNames((0,_B,_H),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_W),(0,_B,_X),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:dcBfdSessMapEntry.setStatus(_A)
_DcBfdSessMapEntityType_Type=EntityProcType
_DcBfdSessMapEntityType_Object=MibTableColumn
dcBfdSessMapEntityType=_DcBfdSessMapEntityType_Object((1,3,6,1,4,1,629,10,11,1,5,1,1),_DcBfdSessMapEntityType_Type())
dcBfdSessMapEntityType.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessMapEntityType.setStatus(_A)
_DcBfdSessMapEntityIndex_Type=Unsigned32
_DcBfdSessMapEntityIndex_Object=MibTableColumn
dcBfdSessMapEntityIndex=_DcBfdSessMapEntityIndex_Object((1,3,6,1,4,1,629,10,11,1,5,1,2),_DcBfdSessMapEntityIndex_Type())
dcBfdSessMapEntityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessMapEntityIndex.setStatus(_A)
_DcBfdSessMapBfdIndex_Type=BfdSessIndexTC
_DcBfdSessMapBfdIndex_Object=MibTableColumn
dcBfdSessMapBfdIndex=_DcBfdSessMapBfdIndex_Object((1,3,6,1,4,1,629,10,11,1,5,1,3),_DcBfdSessMapBfdIndex_Type())
dcBfdSessMapBfdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dcBfdSessMapBfdIndex.setStatus(_A)
_DcBfdSessConfigTable_Object=MibTable
dcBfdSessConfigTable=_DcBfdSessConfigTable_Object((1,3,6,1,4,1,629,10,11,1,6))
if mibBuilder.loadTexts:dcBfdSessConfigTable.setStatus(_A)
_DcBfdSessConfigEntry_Object=MibTableRow
dcBfdSessConfigEntry=_DcBfdSessConfigEntry_Object((1,3,6,1,4,1,629,10,11,1,6,1))
dcBfdSessConfigEntry.setIndexNames((0,_B,_H),(0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:dcBfdSessConfigEntry.setStatus(_A)
class _DcBfdSessConfigProtocol_Type(Bits):namedValues=NamedValues(*(('ospf',0),('isis',1),('bgp',2),('rip',3),('pim',4),('rsvp',5),('ldp',6),('lmp',7),('static',8)))
_DcBfdSessConfigProtocol_Type.__name__='Bits'
_DcBfdSessConfigProtocol_Object=MibTableColumn
dcBfdSessConfigProtocol=_DcBfdSessConfigProtocol_Object((1,3,6,1,4,1,629,10,11,1,6,1,2),_DcBfdSessConfigProtocol_Type())
dcBfdSessConfigProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessConfigProtocol.setStatus(_A)
_DcBfdSessConfigIfIndex_Type=InterfaceIndexOrZero
_DcBfdSessConfigIfIndex_Object=MibTableColumn
dcBfdSessConfigIfIndex=_DcBfdSessConfigIfIndex_Object((1,3,6,1,4,1,629,10,11,1,6,1,3),_DcBfdSessConfigIfIndex_Type())
dcBfdSessConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessConfigIfIndex.setStatus(_A)
_DcBfdSessConfigAddrType_Type=InetAddressType
_DcBfdSessConfigAddrType_Object=MibTableColumn
dcBfdSessConfigAddrType=_DcBfdSessConfigAddrType_Object((1,3,6,1,4,1,629,10,11,1,6,1,4),_DcBfdSessConfigAddrType_Type())
dcBfdSessConfigAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessConfigAddrType.setStatus(_A)
class _DcBfdSessConfigAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_DcBfdSessConfigAddr_Type.__name__=_J
_DcBfdSessConfigAddr_Object=MibTableColumn
dcBfdSessConfigAddr=_DcBfdSessConfigAddr_Object((1,3,6,1,4,1,629,10,11,1,6,1,5),_DcBfdSessConfigAddr_Type())
dcBfdSessConfigAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessConfigAddr.setStatus(_A)
_DcBfdSessConfigRowStatus_Type=RowStatus
_DcBfdSessConfigRowStatus_Object=MibTableColumn
dcBfdSessConfigRowStatus=_DcBfdSessConfigRowStatus_Object((1,3,6,1,4,1,629,10,11,1,6,1,6),_DcBfdSessConfigRowStatus_Type())
dcBfdSessConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigRowStatus.setStatus(_A)
class _DcBfdSessConfigDemandModeDsrd_Type(TruthValue):defaultValue=2
_DcBfdSessConfigDemandModeDsrd_Type.__name__=_I
_DcBfdSessConfigDemandModeDsrd_Object=MibTableColumn
dcBfdSessConfigDemandModeDsrd=_DcBfdSessConfigDemandModeDsrd_Object((1,3,6,1,4,1,629,10,11,1,6,1,7),_DcBfdSessConfigDemandModeDsrd_Type())
dcBfdSessConfigDemandModeDsrd.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigDemandModeDsrd.setStatus(_A)
class _DcBfdSessConfigEchoFuncModeDsrd_Type(TruthValue):defaultValue=2
_DcBfdSessConfigEchoFuncModeDsrd_Type.__name__=_I
_DcBfdSessConfigEchoFuncModeDsrd_Object=MibTableColumn
dcBfdSessConfigEchoFuncModeDsrd=_DcBfdSessConfigEchoFuncModeDsrd_Object((1,3,6,1,4,1,629,10,11,1,6,1,8),_DcBfdSessConfigEchoFuncModeDsrd_Type())
dcBfdSessConfigEchoFuncModeDsrd.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigEchoFuncModeDsrd.setStatus(_A)
class _DcBfdSessConfigDesiredMinTxIntvl_Type(BfdInterval):defaultValue=150000
_DcBfdSessConfigDesiredMinTxIntvl_Type.__name__=_F
_DcBfdSessConfigDesiredMinTxIntvl_Object=MibTableColumn
dcBfdSessConfigDesiredMinTxIntvl=_DcBfdSessConfigDesiredMinTxIntvl_Object((1,3,6,1,4,1,629,10,11,1,6,1,9),_DcBfdSessConfigDesiredMinTxIntvl_Type())
dcBfdSessConfigDesiredMinTxIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigDesiredMinTxIntvl.setStatus(_A)
class _DcBfdSessConfigReqMinRxInterval_Type(BfdInterval):defaultValue=150000
_DcBfdSessConfigReqMinRxInterval_Type.__name__=_F
_DcBfdSessConfigReqMinRxInterval_Object=MibTableColumn
dcBfdSessConfigReqMinRxInterval=_DcBfdSessConfigReqMinRxInterval_Object((1,3,6,1,4,1,629,10,11,1,6,1,10),_DcBfdSessConfigReqMinRxInterval_Type())
dcBfdSessConfigReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigReqMinRxInterval.setStatus(_A)
class _DcBfdSessConfigReqMinEchoRxIntvl_Type(BfdInterval):defaultValue=150000
_DcBfdSessConfigReqMinEchoRxIntvl_Type.__name__=_F
_DcBfdSessConfigReqMinEchoRxIntvl_Object=MibTableColumn
dcBfdSessConfigReqMinEchoRxIntvl=_DcBfdSessConfigReqMinEchoRxIntvl_Object((1,3,6,1,4,1,629,10,11,1,6,1,11),_DcBfdSessConfigReqMinEchoRxIntvl_Type())
dcBfdSessConfigReqMinEchoRxIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigReqMinEchoRxIntvl.setStatus(_A)
class _DcBfdSessConfigDetectMult_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_DcBfdSessConfigDetectMult_Type.__name__=_G
_DcBfdSessConfigDetectMult_Object=MibTableColumn
dcBfdSessConfigDetectMult=_DcBfdSessConfigDetectMult_Object((1,3,6,1,4,1,629,10,11,1,6,1,12),_DcBfdSessConfigDetectMult_Type())
dcBfdSessConfigDetectMult.setMaxAccess(_C)
if mibBuilder.loadTexts:dcBfdSessConfigDetectMult.setStatus(_A)
_DcBfdSessConfigLocalAddrType_Type=InetAddressType
_DcBfdSessConfigLocalAddrType_Object=MibTableColumn
dcBfdSessConfigLocalAddrType=_DcBfdSessConfigLocalAddrType_Object((1,3,6,1,4,1,629,10,11,1,6,1,13),_DcBfdSessConfigLocalAddrType_Type())
dcBfdSessConfigLocalAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessConfigLocalAddrType.setStatus(_A)
_DcBfdSessConfigLocalAddr_Type=InetAddress
_DcBfdSessConfigLocalAddr_Object=MibTableColumn
dcBfdSessConfigLocalAddr=_DcBfdSessConfigLocalAddr_Object((1,3,6,1,4,1,629,10,11,1,6,1,14),_DcBfdSessConfigLocalAddr_Type())
dcBfdSessConfigLocalAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:dcBfdSessConfigLocalAddr.setStatus(_A)
_BfdConformance_ObjectIdentity=ObjectIdentity
bfdConformance=_BfdConformance_ObjectIdentity((1,3,6,1,4,1,629,10,11,3))
_BfdGroups_ObjectIdentity=ObjectIdentity
bfdGroups=_BfdGroups_ObjectIdentity((1,3,6,1,4,1,629,10,11,3,1))
_BfdCompliances_ObjectIdentity=ObjectIdentity
bfdCompliances=_BfdCompliances_ObjectIdentity((1,3,6,1,4,1,629,10,11,3,2))
bfdSessionGroup=ObjectGroup((1,3,6,1,4,1,629,10,11,3,1,1))
bfdSessionGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_L),(_B,_M),(_B,_N),(_B,_m),(_B,_O),(_B,_P),(_B,_Q),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:bfdSessionGroup.setStatus(_A)
bfdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,11,3,2,1))
bfdModuleFullCompliance.setObjects((_B,_y))
if mibBuilder.loadTexts:bfdModuleFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BfdSessIndexTC':BfdSessIndexTC,_F:BfdInterval,'BfdDiag':BfdDiag,'nbase':nbase,'opx':opx,'bfdMIB':bfdMIB,'bfdNotifications':bfdNotifications,'bfdObjects':bfdObjects,'bfdEntityTable':bfdEntityTable,'bfdEntityEntry':bfdEntityEntry,_H:bfdEntityIndex,_e:bfdAdminStatus,_f:bfdOperStatus,_g:bfdRowStatus,_k:bfdVersionNumber,_h:bfdDesiredMinTxInterval,_i:bfdReqMinRxInterval,_j:bfdInterfaceScope,'bfdSessionTable':bfdSessionTable,'bfdSessionEntry':bfdSessionEntry,_V:bfdSessIndex,_l:bfdSessDiscriminator,_O:bfdSessRemoteDiscr,_n:bfdSessState,_o:bfdSessDiag,_p:bfdSessControlPlanIndepFlag,_L:bfdSessIntface,_M:bfdSessAddrType,_N:bfdSessAddr,_m:bfdSessApplicationSessions,_P:bfdSessLocalAddrType,_Q:bfdSessLocalAddr,'dcBfdSessMapTable':dcBfdSessMapTable,'dcBfdSessMapEntry':dcBfdSessMapEntry,_W:dcBfdSessMapEntityType,_X:dcBfdSessMapEntityIndex,_q:dcBfdSessMapBfdIndex,'dcBfdSessConfigTable':dcBfdSessConfigTable,'dcBfdSessConfigEntry':dcBfdSessConfigEntry,_Y:dcBfdSessConfigProtocol,_Z:dcBfdSessConfigIfIndex,_a:dcBfdSessConfigAddrType,_b:dcBfdSessConfigAddr,_r:dcBfdSessConfigRowStatus,_s:dcBfdSessConfigDemandModeDsrd,_t:dcBfdSessConfigEchoFuncModeDsrd,_u:dcBfdSessConfigDesiredMinTxIntvl,_v:dcBfdSessConfigReqMinRxInterval,_w:dcBfdSessConfigReqMinEchoRxIntvl,_x:dcBfdSessConfigDetectMult,_c:dcBfdSessConfigLocalAddrType,_d:dcBfdSessConfigLocalAddr,'bfdConformance':bfdConformance,'bfdGroups':bfdGroups,_y:bfdSessionGroup,'bfdCompliances':bfdCompliances,'bfdModuleFullCompliance':bfdModuleFullCompliance})