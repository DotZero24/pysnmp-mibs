_K='zxr10BfdSessPerfEntry'
_J='zxr10BfdStaticSessSerial'
_I='unknown'
_H='DisplayString'
_G='zxr10BfdSessIndex'
_F='TruthValue'
_E='ZTE-BFD-MIB'
_D='Unsigned32'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention','TimeStamp',_F)
zteBfdMib=ModuleIdentity((1,3,6,1,4,1,3902,3,322))
if mibBuilder.loadTexts:zteBfdMib.setRevisions(('2009-01-07 00:00',))
class DisplayString(OctetString):0
class Zxr10BfdSessIndexTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class Zxr10BfdInterval(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class Zxr10BfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9)))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10BfdNotifications_ObjectIdentity=ObjectIdentity
zxr10BfdNotifications=_Zxr10BfdNotifications_ObjectIdentity((1,3,6,1,4,1,3902,3,322,0))
_Zxr10BfdObjects_ObjectIdentity=ObjectIdentity
zxr10BfdObjects=_Zxr10BfdObjects_ObjectIdentity((1,3,6,1,4,1,3902,3,322,1))
_Zxr10BfdScalarObjects_ObjectIdentity=ObjectIdentity
zxr10BfdScalarObjects=_Zxr10BfdScalarObjects_ObjectIdentity((1,3,6,1,4,1,3902,3,322,1,1))
class _Zxr10BfdAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Zxr10BfdAdminStatus_Type.__name__=_C
_Zxr10BfdAdminStatus_Object=MibScalar
zxr10BfdAdminStatus=_Zxr10BfdAdminStatus_Object((1,3,6,1,4,1,3902,3,322,1,1,1),_Zxr10BfdAdminStatus_Type())
zxr10BfdAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdAdminStatus.setStatus(_A)
class _Zxr10BfdVersionNumber_Type(Unsigned32):defaultValue=0
_Zxr10BfdVersionNumber_Type.__name__=_D
_Zxr10BfdVersionNumber_Object=MibScalar
zxr10BfdVersionNumber=_Zxr10BfdVersionNumber_Object((1,3,6,1,4,1,3902,3,322,1,1,2),_Zxr10BfdVersionNumber_Type())
zxr10BfdVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdVersionNumber.setStatus(_A)
class _Zxr10BfdSessNotificationsEnable_Type(TruthValue):defaultValue=2
_Zxr10BfdSessNotificationsEnable_Type.__name__=_F
_Zxr10BfdSessNotificationsEnable_Object=MibScalar
zxr10BfdSessNotificationsEnable=_Zxr10BfdSessNotificationsEnable_Object((1,3,6,1,4,1,3902,3,322,1,1,3),_Zxr10BfdSessNotificationsEnable_Type())
zxr10BfdSessNotificationsEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxr10BfdSessNotificationsEnable.setStatus(_A)
_Zxr10BfdSessTable_Object=MibTable
zxr10BfdSessTable=_Zxr10BfdSessTable_Object((1,3,6,1,4,1,3902,3,322,1,2))
if mibBuilder.loadTexts:zxr10BfdSessTable.setStatus(_A)
_Zxr10BfdSessEntry_Object=MibTableRow
zxr10BfdSessEntry=_Zxr10BfdSessEntry_Object((1,3,6,1,4,1,3902,3,322,1,2,1))
zxr10BfdSessEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:zxr10BfdSessEntry.setStatus(_A)
_Zxr10BfdSessIndex_Type=Zxr10BfdSessIndexTC
_Zxr10BfdSessIndex_Object=MibTableColumn
zxr10BfdSessIndex=_Zxr10BfdSessIndex_Object((1,3,6,1,4,1,3902,3,322,1,2,1,1),_Zxr10BfdSessIndex_Type())
zxr10BfdSessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessIndex.setStatus(_A)
_Zxr10BfdSessApplicationId_Type=Unsigned32
_Zxr10BfdSessApplicationId_Object=MibTableColumn
zxr10BfdSessApplicationId=_Zxr10BfdSessApplicationId_Object((1,3,6,1,4,1,3902,3,322,1,2,1,2),_Zxr10BfdSessApplicationId_Type())
zxr10BfdSessApplicationId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessApplicationId.setStatus(_A)
class _Zxr10BfdSessInitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_Zxr10BfdSessInitMode_Type.__name__=_C
_Zxr10BfdSessInitMode_Object=MibTableColumn
zxr10BfdSessInitMode=_Zxr10BfdSessInitMode_Object((1,3,6,1,4,1,3902,3,322,1,2,1,3),_Zxr10BfdSessInitMode_Type())
zxr10BfdSessInitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessInitMode.setStatus(_A)
class _Zxr10BfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Zxr10BfdSessDiscriminator_Type.__name__=_D
_Zxr10BfdSessDiscriminator_Object=MibTableColumn
zxr10BfdSessDiscriminator=_Zxr10BfdSessDiscriminator_Object((1,3,6,1,4,1,3902,3,322,1,2,1,4),_Zxr10BfdSessDiscriminator_Type())
zxr10BfdSessDiscriminator.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessDiscriminator.setStatus(_A)
class _Zxr10BfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Zxr10BfdSessRemoteDiscr_Type.__name__=_D
_Zxr10BfdSessRemoteDiscr_Object=MibTableColumn
zxr10BfdSessRemoteDiscr=_Zxr10BfdSessRemoteDiscr_Object((1,3,6,1,4,1,3902,3,322,1,2,1,5),_Zxr10BfdSessRemoteDiscr_Type())
zxr10BfdSessRemoteDiscr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessRemoteDiscr.setStatus(_A)
class _Zxr10BfdSessSrcUdpPort_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Zxr10BfdSessSrcUdpPort_Type.__name__=_D
_Zxr10BfdSessSrcUdpPort_Object=MibTableColumn
zxr10BfdSessSrcUdpPort=_Zxr10BfdSessSrcUdpPort_Object((1,3,6,1,4,1,3902,3,322,1,2,1,6),_Zxr10BfdSessSrcUdpPort_Type())
zxr10BfdSessSrcUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessSrcUdpPort.setStatus(_A)
class _Zxr10BfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
_Zxr10BfdSessState_Type.__name__=_C
_Zxr10BfdSessState_Object=MibTableColumn
zxr10BfdSessState=_Zxr10BfdSessState_Object((1,3,6,1,4,1,3902,3,322,1,2,1,7),_Zxr10BfdSessState_Type())
zxr10BfdSessState.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessState.setStatus(_A)
_Zxr10BfdSessRemoteHeardFlag_Type=TruthValue
_Zxr10BfdSessRemoteHeardFlag_Object=MibTableColumn
zxr10BfdSessRemoteHeardFlag=_Zxr10BfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,3902,3,322,1,2,1,8),_Zxr10BfdSessRemoteHeardFlag_Type())
zxr10BfdSessRemoteHeardFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessRemoteHeardFlag.setStatus(_A)
_Zxr10BfdSessDiag_Type=Zxr10BfdDiag
_Zxr10BfdSessDiag_Object=MibTableColumn
zxr10BfdSessDiag=_Zxr10BfdSessDiag_Object((1,3,6,1,4,1,3902,3,322,1,2,1,9),_Zxr10BfdSessDiag_Type())
zxr10BfdSessDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessDiag.setStatus(_A)
class _Zxr10BfdSessOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asyncModeWEchoFun',1),('asynchModeWOEchoFun',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4)))
_Zxr10BfdSessOperMode_Type.__name__=_C
_Zxr10BfdSessOperMode_Object=MibTableColumn
zxr10BfdSessOperMode=_Zxr10BfdSessOperMode_Object((1,3,6,1,4,1,3902,3,322,1,2,1,10),_Zxr10BfdSessOperMode_Type())
zxr10BfdSessOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessOperMode.setStatus(_A)
class _Zxr10BfdSessDemandModeDesiredFlag_Type(TruthValue):defaultValue=2
_Zxr10BfdSessDemandModeDesiredFlag_Type.__name__=_F
_Zxr10BfdSessDemandModeDesiredFlag_Object=MibTableColumn
zxr10BfdSessDemandModeDesiredFlag=_Zxr10BfdSessDemandModeDesiredFlag_Object((1,3,6,1,4,1,3902,3,322,1,2,1,11),_Zxr10BfdSessDemandModeDesiredFlag_Type())
zxr10BfdSessDemandModeDesiredFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessDemandModeDesiredFlag.setStatus(_A)
class _Zxr10BfdSessEchoFuncModeDesiredFlag_Type(TruthValue):defaultValue=2
_Zxr10BfdSessEchoFuncModeDesiredFlag_Type.__name__=_F
_Zxr10BfdSessEchoFuncModeDesiredFlag_Object=MibTableColumn
zxr10BfdSessEchoFuncModeDesiredFlag=_Zxr10BfdSessEchoFuncModeDesiredFlag_Object((1,3,6,1,4,1,3902,3,322,1,2,1,12),_Zxr10BfdSessEchoFuncModeDesiredFlag_Type())
zxr10BfdSessEchoFuncModeDesiredFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessEchoFuncModeDesiredFlag.setStatus(_A)
class _Zxr10BfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=2
_Zxr10BfdSessControlPlanIndepFlag_Type.__name__=_F
_Zxr10BfdSessControlPlanIndepFlag_Object=MibTableColumn
zxr10BfdSessControlPlanIndepFlag=_Zxr10BfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,3902,3,322,1,2,1,13),_Zxr10BfdSessControlPlanIndepFlag_Type())
zxr10BfdSessControlPlanIndepFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessControlPlanIndepFlag.setStatus(_A)
_Zxr10BfdSessAddrType_Type=InetAddressType
_Zxr10BfdSessAddrType_Object=MibTableColumn
zxr10BfdSessAddrType=_Zxr10BfdSessAddrType_Object((1,3,6,1,4,1,3902,3,322,1,2,1,14),_Zxr10BfdSessAddrType_Type())
zxr10BfdSessAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessAddrType.setStatus(_A)
_Zxr10BfdSessLocalAddr_Type=InetAddress
_Zxr10BfdSessLocalAddr_Object=MibTableColumn
zxr10BfdSessLocalAddr=_Zxr10BfdSessLocalAddr_Object((1,3,6,1,4,1,3902,3,322,1,2,1,15),_Zxr10BfdSessLocalAddr_Type())
zxr10BfdSessLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessLocalAddr.setStatus(_A)
_Zxr10BfdSessRemoteAddr_Type=InetAddress
_Zxr10BfdSessRemoteAddr_Object=MibTableColumn
zxr10BfdSessRemoteAddr=_Zxr10BfdSessRemoteAddr_Object((1,3,6,1,4,1,3902,3,322,1,2,1,16),_Zxr10BfdSessRemoteAddr_Type())
zxr10BfdSessRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessRemoteAddr.setStatus(_A)
_Zxr10BfdSessLdpDestAddr_Type=InetAddress
_Zxr10BfdSessLdpDestAddr_Object=MibTableColumn
zxr10BfdSessLdpDestAddr=_Zxr10BfdSessLdpDestAddr_Object((1,3,6,1,4,1,3902,3,322,1,2,1,17),_Zxr10BfdSessLdpDestAddr_Type())
zxr10BfdSessLdpDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessLdpDestAddr.setStatus(_A)
_Zxr10BfdSessLdpPrefixLength_Type=Unsigned32
_Zxr10BfdSessLdpPrefixLength_Object=MibTableColumn
zxr10BfdSessLdpPrefixLength=_Zxr10BfdSessLdpPrefixLength_Object((1,3,6,1,4,1,3902,3,322,1,2,1,18),_Zxr10BfdSessLdpPrefixLength_Type())
zxr10BfdSessLdpPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessLdpPrefixLength.setStatus(_A)
_Zxr10BfdSessRsvpTunnelId_Type=Unsigned32
_Zxr10BfdSessRsvpTunnelId_Object=MibTableColumn
zxr10BfdSessRsvpTunnelId=_Zxr10BfdSessRsvpTunnelId_Object((1,3,6,1,4,1,3902,3,322,1,2,1,19),_Zxr10BfdSessRsvpTunnelId_Type())
zxr10BfdSessRsvpTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessRsvpTunnelId.setStatus(_A)
_Zxr10BfdSessPWPeerAddr_Type=InetAddress
_Zxr10BfdSessPWPeerAddr_Object=MibTableColumn
zxr10BfdSessPWPeerAddr=_Zxr10BfdSessPWPeerAddr_Object((1,3,6,1,4,1,3902,3,322,1,2,1,20),_Zxr10BfdSessPWPeerAddr_Type())
zxr10BfdSessPWPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWPeerAddr.setStatus(_A)
_Zxr10BfdSessPWVcId_Type=Unsigned32
_Zxr10BfdSessPWVcId_Object=MibTableColumn
zxr10BfdSessPWVcId=_Zxr10BfdSessPWVcId_Object((1,3,6,1,4,1,3902,3,322,1,2,1,21),_Zxr10BfdSessPWVcId_Type())
zxr10BfdSessPWVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWVcId.setStatus(_A)
class _Zxr10BfdSessPWVcTtl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Zxr10BfdSessPWVcTtl_Type.__name__=_D
_Zxr10BfdSessPWVcTtl_Object=MibTableColumn
zxr10BfdSessPWVcTtl=_Zxr10BfdSessPWVcTtl_Object((1,3,6,1,4,1,3902,3,322,1,2,1,22),_Zxr10BfdSessPWVcTtl_Type())
zxr10BfdSessPWVcTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWVcTtl.setStatus(_A)
_Zxr10BfdSessDesiredMinTxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessDesiredMinTxInterval_Object=MibTableColumn
zxr10BfdSessDesiredMinTxInterval=_Zxr10BfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,3902,3,322,1,2,1,23),_Zxr10BfdSessDesiredMinTxInterval_Type())
zxr10BfdSessDesiredMinTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessDesiredMinTxInterval.setStatus(_A)
_Zxr10BfdSessReqMinRxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessReqMinRxInterval_Object=MibTableColumn
zxr10BfdSessReqMinRxInterval=_Zxr10BfdSessReqMinRxInterval_Object((1,3,6,1,4,1,3902,3,322,1,2,1,24),_Zxr10BfdSessReqMinRxInterval_Type())
zxr10BfdSessReqMinRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessReqMinRxInterval.setStatus(_A)
_Zxr10BfdSessReqMinEchoRxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessReqMinEchoRxInterval_Object=MibTableColumn
zxr10BfdSessReqMinEchoRxInterval=_Zxr10BfdSessReqMinEchoRxInterval_Object((1,3,6,1,4,1,3902,3,322,1,2,1,25),_Zxr10BfdSessReqMinEchoRxInterval_Type())
zxr10BfdSessReqMinEchoRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessReqMinEchoRxInterval.setStatus(_A)
_Zxr10BfdSessDetectMult_Type=Unsigned32
_Zxr10BfdSessDetectMult_Object=MibTableColumn
zxr10BfdSessDetectMult=_Zxr10BfdSessDetectMult_Object((1,3,6,1,4,1,3902,3,322,1,2,1,26),_Zxr10BfdSessDetectMult_Type())
zxr10BfdSessDetectMult.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessDetectMult.setStatus(_A)
_Zxr10BfdSessHoldTime_Type=Unsigned32
_Zxr10BfdSessHoldTime_Object=MibTableColumn
zxr10BfdSessHoldTime=_Zxr10BfdSessHoldTime_Object((1,3,6,1,4,1,3902,3,322,1,2,1,27),_Zxr10BfdSessHoldTime_Type())
zxr10BfdSessHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessHoldTime.setStatus(_A)
class _Zxr10BfdSessAuthPresFlag_Type(TruthValue):defaultValue=2
_Zxr10BfdSessAuthPresFlag_Type.__name__=_F
_Zxr10BfdSessAuthPresFlag_Object=MibTableColumn
zxr10BfdSessAuthPresFlag=_Zxr10BfdSessAuthPresFlag_Object((1,3,6,1,4,1,3902,3,322,1,2,1,28),_Zxr10BfdSessAuthPresFlag_Type())
zxr10BfdSessAuthPresFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessAuthPresFlag.setStatus(_A)
class _Zxr10BfdSessAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('simplePassword',1),('keyedMD5',2),('meticulousKeyedMD5',3),('keyedSHA1',4),('meticulousKeyedSHA1',5)))
_Zxr10BfdSessAuthenticationType_Type.__name__=_C
_Zxr10BfdSessAuthenticationType_Object=MibTableColumn
zxr10BfdSessAuthenticationType=_Zxr10BfdSessAuthenticationType_Object((1,3,6,1,4,1,3902,3,322,1,2,1,29),_Zxr10BfdSessAuthenticationType_Type())
zxr10BfdSessAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessAuthenticationType.setStatus(_A)
class _Zxr10BfdSessVersionNumber_Type(Unsigned32):defaultValue=0
_Zxr10BfdSessVersionNumber_Type.__name__=_D
_Zxr10BfdSessVersionNumber_Object=MibTableColumn
zxr10BfdSessVersionNumber=_Zxr10BfdSessVersionNumber_Object((1,3,6,1,4,1,3902,3,322,1,2,1,30),_Zxr10BfdSessVersionNumber_Type())
zxr10BfdSessVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessVersionNumber.setStatus(_A)
class _Zxr10BfdSessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleHop',1),('multiHop',2)))
_Zxr10BfdSessType_Type.__name__=_C
_Zxr10BfdSessType_Object=MibTableColumn
zxr10BfdSessType=_Zxr10BfdSessType_Object((1,3,6,1,4,1,3902,3,322,1,2,1,31),_Zxr10BfdSessType_Type())
zxr10BfdSessType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessType.setStatus(_A)
class _Zxr10BfdSessInterface_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10BfdSessInterface_Type.__name__=_D
_Zxr10BfdSessInterface_Object=MibTableColumn
zxr10BfdSessInterface=_Zxr10BfdSessInterface_Object((1,3,6,1,4,1,3902,3,322,1,2,1,32),_Zxr10BfdSessInterface_Type())
zxr10BfdSessInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessInterface.setStatus(_A)
class _Zxr10BfdSessPWMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('static',1),('dynamic-PWE3',2),('dynamic-Martini',3)))
_Zxr10BfdSessPWMode_Type.__name__=_C
_Zxr10BfdSessPWMode_Object=MibTableColumn
zxr10BfdSessPWMode=_Zxr10BfdSessPWMode_Object((1,3,6,1,4,1,3902,3,322,1,2,1,33),_Zxr10BfdSessPWMode_Type())
zxr10BfdSessPWMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWMode.setStatus(_A)
class _Zxr10BfdSessPWFec129Agi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Zxr10BfdSessPWFec129Agi_Type.__name__=_D
_Zxr10BfdSessPWFec129Agi_Object=MibTableColumn
zxr10BfdSessPWFec129Agi=_Zxr10BfdSessPWFec129Agi_Object((1,3,6,1,4,1,3902,3,322,1,2,1,34),_Zxr10BfdSessPWFec129Agi_Type())
zxr10BfdSessPWFec129Agi.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129Agi.setStatus(_A)
class _Zxr10BfdSessPWFec129SaiiGid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10BfdSessPWFec129SaiiGid_Type.__name__=_D
_Zxr10BfdSessPWFec129SaiiGid_Object=MibTableColumn
zxr10BfdSessPWFec129SaiiGid=_Zxr10BfdSessPWFec129SaiiGid_Object((1,3,6,1,4,1,3902,3,322,1,2,1,35),_Zxr10BfdSessPWFec129SaiiGid_Type())
zxr10BfdSessPWFec129SaiiGid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129SaiiGid.setStatus(_A)
_Zxr10BfdSessPWFec129SaiiPrefix_Type=InetAddress
_Zxr10BfdSessPWFec129SaiiPrefix_Object=MibTableColumn
zxr10BfdSessPWFec129SaiiPrefix=_Zxr10BfdSessPWFec129SaiiPrefix_Object((1,3,6,1,4,1,3902,3,322,1,2,1,36),_Zxr10BfdSessPWFec129SaiiPrefix_Type())
zxr10BfdSessPWFec129SaiiPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129SaiiPrefix.setStatus(_A)
class _Zxr10BfdSessPWFec129TaiiGid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Zxr10BfdSessPWFec129TaiiGid_Type.__name__=_D
_Zxr10BfdSessPWFec129TaiiGid_Object=MibTableColumn
zxr10BfdSessPWFec129TaiiGid=_Zxr10BfdSessPWFec129TaiiGid_Object((1,3,6,1,4,1,3902,3,322,1,2,1,37),_Zxr10BfdSessPWFec129TaiiGid_Type())
zxr10BfdSessPWFec129TaiiGid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129TaiiGid.setStatus(_A)
_Zxr10BfdSessPWFec129TaiiPrefix_Type=InetAddress
_Zxr10BfdSessPWFec129TaiiPrefix_Object=MibTableColumn
zxr10BfdSessPWFec129TaiiPrefix=_Zxr10BfdSessPWFec129TaiiPrefix_Object((1,3,6,1,4,1,3902,3,322,1,2,1,38),_Zxr10BfdSessPWFec129TaiiPrefix_Type())
zxr10BfdSessPWFec129TaiiPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129TaiiPrefix.setStatus(_A)
class _Zxr10BfdSessPWFec129SaiiACId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Zxr10BfdSessPWFec129SaiiACId_Type.__name__=_D
_Zxr10BfdSessPWFec129SaiiACId_Object=MibTableColumn
zxr10BfdSessPWFec129SaiiACId=_Zxr10BfdSessPWFec129SaiiACId_Object((1,3,6,1,4,1,3902,3,322,1,2,1,39),_Zxr10BfdSessPWFec129SaiiACId_Type())
zxr10BfdSessPWFec129SaiiACId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129SaiiACId.setStatus(_A)
class _Zxr10BfdSessPWFec129TaiiACId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Zxr10BfdSessPWFec129TaiiACId_Type.__name__=_D
_Zxr10BfdSessPWFec129TaiiACId_Object=MibTableColumn
zxr10BfdSessPWFec129TaiiACId=_Zxr10BfdSessPWFec129TaiiACId_Object((1,3,6,1,4,1,3902,3,322,1,2,1,40),_Zxr10BfdSessPWFec129TaiiACId_Type())
zxr10BfdSessPWFec129TaiiACId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFec129TaiiACId.setStatus(_A)
class _Zxr10BfdSessPWFecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('fec128',1),('fec129',2)))
_Zxr10BfdSessPWFecType_Type.__name__=_C
_Zxr10BfdSessPWFecType_Object=MibTableColumn
zxr10BfdSessPWFecType=_Zxr10BfdSessPWFecType_Object((1,3,6,1,4,1,3902,3,322,1,2,1,41),_Zxr10BfdSessPWFecType_Type())
zxr10BfdSessPWFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPWFecType.setStatus(_A)
_Zxr10BfdSessPerfTable_Object=MibTable
zxr10BfdSessPerfTable=_Zxr10BfdSessPerfTable_Object((1,3,6,1,4,1,3902,3,322,1,3))
if mibBuilder.loadTexts:zxr10BfdSessPerfTable.setStatus(_A)
_Zxr10BfdSessPerfEntry_Object=MibTableRow
zxr10BfdSessPerfEntry=_Zxr10BfdSessPerfEntry_Object((1,3,6,1,4,1,3902,3,322,1,3,1))
if mibBuilder.loadTexts:zxr10BfdSessPerfEntry.setStatus(_A)
_Zxr10BfdSessPerfIndex_Type=Zxr10BfdSessIndexTC
_Zxr10BfdSessPerfIndex_Object=MibTableColumn
zxr10BfdSessPerfIndex=_Zxr10BfdSessPerfIndex_Object((1,3,6,1,4,1,3902,3,322,1,3,1,1),_Zxr10BfdSessPerfIndex_Type())
zxr10BfdSessPerfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfIndex.setStatus(_A)
_Zxr10BfdSessPerfPktIn_Type=Counter32
_Zxr10BfdSessPerfPktIn_Object=MibTableColumn
zxr10BfdSessPerfPktIn=_Zxr10BfdSessPerfPktIn_Object((1,3,6,1,4,1,3902,3,322,1,3,1,2),_Zxr10BfdSessPerfPktIn_Type())
zxr10BfdSessPerfPktIn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfPktIn.setStatus(_A)
_Zxr10BfdSessPerfPktOut_Type=Counter32
_Zxr10BfdSessPerfPktOut_Object=MibTableColumn
zxr10BfdSessPerfPktOut=_Zxr10BfdSessPerfPktOut_Object((1,3,6,1,4,1,3902,3,322,1,3,1,3),_Zxr10BfdSessPerfPktOut_Type())
zxr10BfdSessPerfPktOut.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfPktOut.setStatus(_A)
_Zxr10BfdSessUpTime_Type=TimeStamp
_Zxr10BfdSessUpTime_Object=MibTableColumn
zxr10BfdSessUpTime=_Zxr10BfdSessUpTime_Object((1,3,6,1,4,1,3902,3,322,1,3,1,4),_Zxr10BfdSessUpTime_Type())
zxr10BfdSessUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessUpTime.setStatus(_A)
_Zxr10BfdSessPerfLastCommLostDiag_Type=Zxr10BfdDiag
_Zxr10BfdSessPerfLastCommLostDiag_Object=MibTableColumn
zxr10BfdSessPerfLastCommLostDiag=_Zxr10BfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,3902,3,322,1,3,1,5),_Zxr10BfdSessPerfLastCommLostDiag_Type())
zxr10BfdSessPerfLastCommLostDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfLastCommLostDiag.setStatus(_A)
_Zxr10BfdSessPerfMinTxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessPerfMinTxInterval_Object=MibTableColumn
zxr10BfdSessPerfMinTxInterval=_Zxr10BfdSessPerfMinTxInterval_Object((1,3,6,1,4,1,3902,3,322,1,3,1,6),_Zxr10BfdSessPerfMinTxInterval_Type())
zxr10BfdSessPerfMinTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfMinTxInterval.setStatus(_A)
_Zxr10BfdSessPerfMaxTxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessPerfMaxTxInterval_Object=MibTableColumn
zxr10BfdSessPerfMaxTxInterval=_Zxr10BfdSessPerfMaxTxInterval_Object((1,3,6,1,4,1,3902,3,322,1,3,1,7),_Zxr10BfdSessPerfMaxTxInterval_Type())
zxr10BfdSessPerfMaxTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfMaxTxInterval.setStatus(_A)
_Zxr10BfdSessPerfAvgTxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessPerfAvgTxInterval_Object=MibTableColumn
zxr10BfdSessPerfAvgTxInterval=_Zxr10BfdSessPerfAvgTxInterval_Object((1,3,6,1,4,1,3902,3,322,1,3,1,8),_Zxr10BfdSessPerfAvgTxInterval_Type())
zxr10BfdSessPerfAvgTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfAvgTxInterval.setStatus(_A)
_Zxr10BfdSessPerfMinRxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessPerfMinRxInterval_Object=MibTableColumn
zxr10BfdSessPerfMinRxInterval=_Zxr10BfdSessPerfMinRxInterval_Object((1,3,6,1,4,1,3902,3,322,1,3,1,9),_Zxr10BfdSessPerfMinRxInterval_Type())
zxr10BfdSessPerfMinRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfMinRxInterval.setStatus(_A)
_Zxr10BfdSessPerfMaxRxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessPerfMaxRxInterval_Object=MibTableColumn
zxr10BfdSessPerfMaxRxInterval=_Zxr10BfdSessPerfMaxRxInterval_Object((1,3,6,1,4,1,3902,3,322,1,3,1,10),_Zxr10BfdSessPerfMaxRxInterval_Type())
zxr10BfdSessPerfMaxRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfMaxRxInterval.setStatus(_A)
_Zxr10BfdSessPerfAvgRxInterval_Type=Zxr10BfdInterval
_Zxr10BfdSessPerfAvgRxInterval_Object=MibTableColumn
zxr10BfdSessPerfAvgRxInterval=_Zxr10BfdSessPerfAvgRxInterval_Object((1,3,6,1,4,1,3902,3,322,1,3,1,11),_Zxr10BfdSessPerfAvgRxInterval_Type())
zxr10BfdSessPerfAvgRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdSessPerfAvgRxInterval.setStatus(_A)
_Zxr10BfdStaticSessTable_Object=MibTable
zxr10BfdStaticSessTable=_Zxr10BfdStaticSessTable_Object((1,3,6,1,4,1,3902,3,322,1,4))
if mibBuilder.loadTexts:zxr10BfdStaticSessTable.setStatus(_A)
_Zxr10BfdStaticSessConfigEntry_Object=MibTableRow
zxr10BfdStaticSessConfigEntry=_Zxr10BfdStaticSessConfigEntry_Object((1,3,6,1,4,1,3902,3,322,1,4,1))
zxr10BfdStaticSessConfigEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:zxr10BfdStaticSessConfigEntry.setStatus(_A)
_Zxr10BfdStaticSessSerial_Type=Integer32
_Zxr10BfdStaticSessSerial_Object=MibTableColumn
zxr10BfdStaticSessSerial=_Zxr10BfdStaticSessSerial_Object((1,3,6,1,4,1,3902,3,322,1,4,1,1),_Zxr10BfdStaticSessSerial_Type())
zxr10BfdStaticSessSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessSerial.setStatus(_A)
_Zxr10BfdStaticSessName_Type=DisplayString
_Zxr10BfdStaticSessName_Object=MibTableColumn
zxr10BfdStaticSessName=_Zxr10BfdStaticSessName_Object((1,3,6,1,4,1,3902,3,322,1,4,1,2),_Zxr10BfdStaticSessName_Type())
zxr10BfdStaticSessName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessName.setStatus(_A)
class _Zxr10BfdStaticSessBindType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('link-bfd',1),('peer-bfd',2)))
_Zxr10BfdStaticSessBindType_Type.__name__=_C
_Zxr10BfdStaticSessBindType_Object=MibTableColumn
zxr10BfdStaticSessBindType=_Zxr10BfdStaticSessBindType_Object((1,3,6,1,4,1,3902,3,322,1,4,1,3),_Zxr10BfdStaticSessBindType_Type())
zxr10BfdStaticSessBindType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessBindType.setStatus(_A)
_Zxr10BfdStaticSessPeerIp_Type=IpAddress
_Zxr10BfdStaticSessPeerIp_Object=MibTableColumn
zxr10BfdStaticSessPeerIp=_Zxr10BfdStaticSessPeerIp_Object((1,3,6,1,4,1,3902,3,322,1,4,1,4),_Zxr10BfdStaticSessPeerIp_Type())
zxr10BfdStaticSessPeerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessPeerIp.setStatus(_A)
_Zxr10BfdStaticSessIfDefaultIp_Type=TruthValue
_Zxr10BfdStaticSessIfDefaultIp_Object=MibTableColumn
zxr10BfdStaticSessIfDefaultIp=_Zxr10BfdStaticSessIfDefaultIp_Object((1,3,6,1,4,1,3902,3,322,1,4,1,5),_Zxr10BfdStaticSessIfDefaultIp_Type())
zxr10BfdStaticSessIfDefaultIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessIfDefaultIp.setStatus(_A)
_Zxr10BfdStaticSessDefaultIp_Type=IpAddress
_Zxr10BfdStaticSessDefaultIp_Object=MibTableColumn
zxr10BfdStaticSessDefaultIp=_Zxr10BfdStaticSessDefaultIp_Object((1,3,6,1,4,1,3902,3,322,1,4,1,6),_Zxr10BfdStaticSessDefaultIp_Type())
zxr10BfdStaticSessDefaultIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessDefaultIp.setStatus(_A)
_Zxr10BfdStaticSessSourceIp_Type=IpAddress
_Zxr10BfdStaticSessSourceIp_Object=MibTableColumn
zxr10BfdStaticSessSourceIp=_Zxr10BfdStaticSessSourceIp_Object((1,3,6,1,4,1,3902,3,322,1,4,1,7),_Zxr10BfdStaticSessSourceIp_Type())
zxr10BfdStaticSessSourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessSourceIp.setStatus(_A)
_Zxr10BfdStaticSessInterfaceName_Type=DisplayString
_Zxr10BfdStaticSessInterfaceName_Object=MibTableColumn
zxr10BfdStaticSessInterfaceName=_Zxr10BfdStaticSessInterfaceName_Object((1,3,6,1,4,1,3902,3,322,1,4,1,8),_Zxr10BfdStaticSessInterfaceName_Type())
zxr10BfdStaticSessInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessInterfaceName.setStatus(_A)
_Zxr10BfdStaticSessVrfName_Type=DisplayString
_Zxr10BfdStaticSessVrfName_Object=MibTableColumn
zxr10BfdStaticSessVrfName=_Zxr10BfdStaticSessVrfName_Object((1,3,6,1,4,1,3902,3,322,1,4,1,9),_Zxr10BfdStaticSessVrfName_Type())
zxr10BfdStaticSessVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessVrfName.setStatus(_A)
_Zxr10BfdStaticSessLocalDisc_Type=Unsigned32
_Zxr10BfdStaticSessLocalDisc_Object=MibTableColumn
zxr10BfdStaticSessLocalDisc=_Zxr10BfdStaticSessLocalDisc_Object((1,3,6,1,4,1,3902,3,322,1,4,1,10),_Zxr10BfdStaticSessLocalDisc_Type())
zxr10BfdStaticSessLocalDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessLocalDisc.setStatus(_A)
_Zxr10BfdStaticSessRemoteDisc_Type=Unsigned32
_Zxr10BfdStaticSessRemoteDisc_Object=MibTableColumn
zxr10BfdStaticSessRemoteDisc=_Zxr10BfdStaticSessRemoteDisc_Object((1,3,6,1,4,1,3902,3,322,1,4,1,11),_Zxr10BfdStaticSessRemoteDisc_Type())
zxr10BfdStaticSessRemoteDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessRemoteDisc.setStatus(_A)
class _Zxr10BfdStaticSessMult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,50))
_Zxr10BfdStaticSessMult_Type.__name__=_C
_Zxr10BfdStaticSessMult_Object=MibTableColumn
zxr10BfdStaticSessMult=_Zxr10BfdStaticSessMult_Object((1,3,6,1,4,1,3902,3,322,1,4,1,12),_Zxr10BfdStaticSessMult_Type())
zxr10BfdStaticSessMult.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessMult.setStatus(_A)
class _Zxr10BfdStaticSessMinTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,999))
_Zxr10BfdStaticSessMinTx_Type.__name__=_C
_Zxr10BfdStaticSessMinTx_Object=MibTableColumn
zxr10BfdStaticSessMinTx=_Zxr10BfdStaticSessMinTx_Object((1,3,6,1,4,1,3902,3,322,1,4,1,13),_Zxr10BfdStaticSessMinTx_Type())
zxr10BfdStaticSessMinTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessMinTx.setStatus(_A)
class _Zxr10BfdStaticSessMinRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,999))
_Zxr10BfdStaticSessMinRx_Type.__name__=_C
_Zxr10BfdStaticSessMinRx_Object=MibTableColumn
zxr10BfdStaticSessMinRx=_Zxr10BfdStaticSessMinRx_Object((1,3,6,1,4,1,3902,3,322,1,4,1,14),_Zxr10BfdStaticSessMinRx_Type())
zxr10BfdStaticSessMinRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10BfdStaticSessMinRx.setStatus(_A)
zxr10BfdSessEntry.registerAugmentions((_E,_K))
zxr10BfdSessPerfEntry.setIndexNames(*zxr10BfdSessEntry.getIndexNames())
zxr10BfdSessUp=NotificationType((1,3,6,1,4,1,3902,3,322,0,1))
zxr10BfdSessUp.setObjects(*((_E,_G),(_E,_G)))
if mibBuilder.loadTexts:zxr10BfdSessUp.setStatus(_A)
zxr10BfdSessDown=NotificationType((1,3,6,1,4,1,3902,3,322,0,2))
zxr10BfdSessDown.setObjects(*((_E,_G),(_E,_G)))
if mibBuilder.loadTexts:zxr10BfdSessDown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_H:DisplayString,'Zxr10BfdSessIndexTC':Zxr10BfdSessIndexTC,'Zxr10BfdInterval':Zxr10BfdInterval,'Zxr10BfdDiag':Zxr10BfdDiag,'zte':zte,'zxr10':zxr10,'zteBfdMib':zteBfdMib,'zxr10BfdNotifications':zxr10BfdNotifications,'zxr10BfdSessUp':zxr10BfdSessUp,'zxr10BfdSessDown':zxr10BfdSessDown,'zxr10BfdObjects':zxr10BfdObjects,'zxr10BfdScalarObjects':zxr10BfdScalarObjects,'zxr10BfdAdminStatus':zxr10BfdAdminStatus,'zxr10BfdVersionNumber':zxr10BfdVersionNumber,'zxr10BfdSessNotificationsEnable':zxr10BfdSessNotificationsEnable,'zxr10BfdSessTable':zxr10BfdSessTable,'zxr10BfdSessEntry':zxr10BfdSessEntry,_G:zxr10BfdSessIndex,'zxr10BfdSessApplicationId':zxr10BfdSessApplicationId,'zxr10BfdSessInitMode':zxr10BfdSessInitMode,'zxr10BfdSessDiscriminator':zxr10BfdSessDiscriminator,'zxr10BfdSessRemoteDiscr':zxr10BfdSessRemoteDiscr,'zxr10BfdSessSrcUdpPort':zxr10BfdSessSrcUdpPort,'zxr10BfdSessState':zxr10BfdSessState,'zxr10BfdSessRemoteHeardFlag':zxr10BfdSessRemoteHeardFlag,'zxr10BfdSessDiag':zxr10BfdSessDiag,'zxr10BfdSessOperMode':zxr10BfdSessOperMode,'zxr10BfdSessDemandModeDesiredFlag':zxr10BfdSessDemandModeDesiredFlag,'zxr10BfdSessEchoFuncModeDesiredFlag':zxr10BfdSessEchoFuncModeDesiredFlag,'zxr10BfdSessControlPlanIndepFlag':zxr10BfdSessControlPlanIndepFlag,'zxr10BfdSessAddrType':zxr10BfdSessAddrType,'zxr10BfdSessLocalAddr':zxr10BfdSessLocalAddr,'zxr10BfdSessRemoteAddr':zxr10BfdSessRemoteAddr,'zxr10BfdSessLdpDestAddr':zxr10BfdSessLdpDestAddr,'zxr10BfdSessLdpPrefixLength':zxr10BfdSessLdpPrefixLength,'zxr10BfdSessRsvpTunnelId':zxr10BfdSessRsvpTunnelId,'zxr10BfdSessPWPeerAddr':zxr10BfdSessPWPeerAddr,'zxr10BfdSessPWVcId':zxr10BfdSessPWVcId,'zxr10BfdSessPWVcTtl':zxr10BfdSessPWVcTtl,'zxr10BfdSessDesiredMinTxInterval':zxr10BfdSessDesiredMinTxInterval,'zxr10BfdSessReqMinRxInterval':zxr10BfdSessReqMinRxInterval,'zxr10BfdSessReqMinEchoRxInterval':zxr10BfdSessReqMinEchoRxInterval,'zxr10BfdSessDetectMult':zxr10BfdSessDetectMult,'zxr10BfdSessHoldTime':zxr10BfdSessHoldTime,'zxr10BfdSessAuthPresFlag':zxr10BfdSessAuthPresFlag,'zxr10BfdSessAuthenticationType':zxr10BfdSessAuthenticationType,'zxr10BfdSessVersionNumber':zxr10BfdSessVersionNumber,'zxr10BfdSessType':zxr10BfdSessType,'zxr10BfdSessInterface':zxr10BfdSessInterface,'zxr10BfdSessPWMode':zxr10BfdSessPWMode,'zxr10BfdSessPWFec129Agi':zxr10BfdSessPWFec129Agi,'zxr10BfdSessPWFec129SaiiGid':zxr10BfdSessPWFec129SaiiGid,'zxr10BfdSessPWFec129SaiiPrefix':zxr10BfdSessPWFec129SaiiPrefix,'zxr10BfdSessPWFec129TaiiGid':zxr10BfdSessPWFec129TaiiGid,'zxr10BfdSessPWFec129TaiiPrefix':zxr10BfdSessPWFec129TaiiPrefix,'zxr10BfdSessPWFec129SaiiACId':zxr10BfdSessPWFec129SaiiACId,'zxr10BfdSessPWFec129TaiiACId':zxr10BfdSessPWFec129TaiiACId,'zxr10BfdSessPWFecType':zxr10BfdSessPWFecType,'zxr10BfdSessPerfTable':zxr10BfdSessPerfTable,_K:zxr10BfdSessPerfEntry,'zxr10BfdSessPerfIndex':zxr10BfdSessPerfIndex,'zxr10BfdSessPerfPktIn':zxr10BfdSessPerfPktIn,'zxr10BfdSessPerfPktOut':zxr10BfdSessPerfPktOut,'zxr10BfdSessUpTime':zxr10BfdSessUpTime,'zxr10BfdSessPerfLastCommLostDiag':zxr10BfdSessPerfLastCommLostDiag,'zxr10BfdSessPerfMinTxInterval':zxr10BfdSessPerfMinTxInterval,'zxr10BfdSessPerfMaxTxInterval':zxr10BfdSessPerfMaxTxInterval,'zxr10BfdSessPerfAvgTxInterval':zxr10BfdSessPerfAvgTxInterval,'zxr10BfdSessPerfMinRxInterval':zxr10BfdSessPerfMinRxInterval,'zxr10BfdSessPerfMaxRxInterval':zxr10BfdSessPerfMaxRxInterval,'zxr10BfdSessPerfAvgRxInterval':zxr10BfdSessPerfAvgRxInterval,'zxr10BfdStaticSessTable':zxr10BfdStaticSessTable,'zxr10BfdStaticSessConfigEntry':zxr10BfdStaticSessConfigEntry,_J:zxr10BfdStaticSessSerial,'zxr10BfdStaticSessName':zxr10BfdStaticSessName,'zxr10BfdStaticSessBindType':zxr10BfdStaticSessBindType,'zxr10BfdStaticSessPeerIp':zxr10BfdStaticSessPeerIp,'zxr10BfdStaticSessIfDefaultIp':zxr10BfdStaticSessIfDefaultIp,'zxr10BfdStaticSessDefaultIp':zxr10BfdStaticSessDefaultIp,'zxr10BfdStaticSessSourceIp':zxr10BfdStaticSessSourceIp,'zxr10BfdStaticSessInterfaceName':zxr10BfdStaticSessInterfaceName,'zxr10BfdStaticSessVrfName':zxr10BfdStaticSessVrfName,'zxr10BfdStaticSessLocalDisc':zxr10BfdStaticSessLocalDisc,'zxr10BfdStaticSessRemoteDisc':zxr10BfdStaticSessRemoteDisc,'zxr10BfdStaticSessMult':zxr10BfdStaticSessMult,'zxr10BfdStaticSessMinTx':zxr10BfdStaticSessMinTx,'zxr10BfdStaticSessMinRx':zxr10BfdStaticSessMinRx})