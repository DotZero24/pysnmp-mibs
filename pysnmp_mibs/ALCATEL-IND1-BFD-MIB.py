_AE='alaBfdSessPerfGroup'
_AD='alaBfdSessGroup'
_AC='alaBfdIntfCfgGroup'
_AB='alaBfdbasicGroup'
_AA='alaBfdSessPerfDiscTime'
_A9='alaBfdSessPerfSessUpCount'
_A8='alaBfdSessPerfLastCommLostDiag'
_A7='alaBfdSessPerfLastSessDownTime'
_A6='alaBfdSessPerfUpTime'
_A5='alaBfdSessPerfEchoOut'
_A4='alaBfdSessPerfPktOut'
_A3='alaBfdSessPerfPktIn'
_A2='alaBfdSessProtocols'
_A1='alaBfdSessNegotiatedRxInterval'
_A0='alaBfdSessNegotiatedTxInterval'
_z='alaBfdSessInterface'
_y='alaBfdSessControlPlanIndepFlag'
_x='alaBfdSessEchoFuncModeDesiredFlag'
_w='alaBfdSessOperMode'
_v='alaBfdSessDiag'
_u='alaBfdSessRemoteHeardFlag'
_t='alaBfdSessState'
_s='alaBfdSessUdpPort'
_r='alaBfdSessRemoteDiscr'
_q='alaBfdSessNeighborAddr'
_p='alaBfdSessNeighborAddrType'
_o='alaBfdIntfRowStatus'
_n='alaBfdIntfL2HoldTimer'
_m='alaBfdIntfAuthenticationType'
_l='alaBfdIntfAuthPresFlag'
_k='alaBfdIntfsesstype'
_j='alaBfdIntfDetectMult'
_i='alaBfdIntfOperMode'
_h='alaBfdIntfReqMinEchoRxInterval'
_g='alaBfdIntfEchoMode'
_f='alaBfdIntfReqMinRxInterval'
_e='alaBfdIntfDesiredMinTxInterval'
_d='alabfdIntfAdminStatus'
_c='alaBfdIntfIndex'
_b='alaBfdGlobalEchoRxInterval'
_a='alaBfdGlobalEcho'
_Z='alaBfdGlobalProtocols'
_Y='alaBfdGlobalL2HoldTimer'
_X='alaBfdGlobalVersionNumber'
_W='alaBfdGlobalOperMode'
_V='alaBfdGlobalRxInterval'
_U='alaBfdGlobalTxInterval'
_T='alaBfdGlobalAdminStatus'
_S='alaBfdSessPerfEntry'
_R='alaBfdSessDiscriminator'
_Q='alaBfdIntfAddr'
_P='alaBfdIntfAddrType'
_O='not-accessible'
_N='echoOnly'
_M='demandMode'
_L='asyncMode'
_K='AlaBfdStatus'
_J='TruthValue'
_I='Bits'
_H='AlaBfdInterval'
_G='Unsigned32'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='ALCATEL-IND1-BFD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1BFD,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1BFD')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
alcatelIND1BfdMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1))
if mibBuilder.loadTexts:alcatelIND1BfdMIB.setRevisions(('2008-05-03 00:00',))
class AlaBfdInterval(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class AlaBfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',1),('controlDetectionTimeExpired',2),('echoFunctionFailed',3),('neighborSignaledSessionDown',4),('forwardingPlaneReset',5),('pathDown',6),('concatenatedPathDown',7),('administrativelyDown',8),('reverseConcatenatedPathDown',9)))
class AlaBfdStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaBfdObjects_ObjectIdentity=ObjectIdentity
alaBfdObjects=_AlaBfdObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1,1))
if mibBuilder.loadTexts:alaBfdObjects.setStatus(_A)
_AlaBfdGlobalObjects_ObjectIdentity=ObjectIdentity
alaBfdGlobalObjects=_AlaBfdGlobalObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1))
class _AlaBfdGlobalAdminStatus_Type(AlaBfdStatus):defaultValue=1
_AlaBfdGlobalAdminStatus_Type.__name__=_K
_AlaBfdGlobalAdminStatus_Object=MibScalar
alaBfdGlobalAdminStatus=_AlaBfdGlobalAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,1),_AlaBfdGlobalAdminStatus_Type())
alaBfdGlobalAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalAdminStatus.setStatus(_A)
class _AlaBfdGlobalTxInterval_Type(AlaBfdInterval):defaultValue=300
_AlaBfdGlobalTxInterval_Type.__name__=_H
_AlaBfdGlobalTxInterval_Object=MibScalar
alaBfdGlobalTxInterval=_AlaBfdGlobalTxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,2),_AlaBfdGlobalTxInterval_Type())
alaBfdGlobalTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalTxInterval.setStatus(_A)
class _AlaBfdGlobalRxInterval_Type(AlaBfdInterval):defaultValue=300
_AlaBfdGlobalRxInterval_Type.__name__=_H
_AlaBfdGlobalRxInterval_Object=MibScalar
alaBfdGlobalRxInterval=_AlaBfdGlobalRxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,3),_AlaBfdGlobalRxInterval_Type())
alaBfdGlobalRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalRxInterval.setStatus(_A)
class _AlaBfdGlobalOperMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_AlaBfdGlobalOperMode_Type.__name__=_E
_AlaBfdGlobalOperMode_Object=MibScalar
alaBfdGlobalOperMode=_AlaBfdGlobalOperMode_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,4),_AlaBfdGlobalOperMode_Type())
alaBfdGlobalOperMode.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalOperMode.setStatus(_A)
class _AlaBfdGlobalVersionNumber_Type(Unsigned32):defaultValue=1
_AlaBfdGlobalVersionNumber_Type.__name__=_G
_AlaBfdGlobalVersionNumber_Object=MibScalar
alaBfdGlobalVersionNumber=_AlaBfdGlobalVersionNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,5),_AlaBfdGlobalVersionNumber_Type())
alaBfdGlobalVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdGlobalVersionNumber.setStatus(_A)
class _AlaBfdGlobalL2HoldTimer_Type(AlaBfdInterval):defaultValue=500
_AlaBfdGlobalL2HoldTimer_Type.__name__=_H
_AlaBfdGlobalL2HoldTimer_Object=MibScalar
alaBfdGlobalL2HoldTimer=_AlaBfdGlobalL2HoldTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,6),_AlaBfdGlobalL2HoldTimer_Type())
alaBfdGlobalL2HoldTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalL2HoldTimer.setStatus(_A)
class _AlaBfdGlobalProtocols_Type(Bits):namedValues=NamedValues(*(('ospf',0),('bgp',1),('dvmrp',2),('vrrp',3)))
_AlaBfdGlobalProtocols_Type.__name__=_I
_AlaBfdGlobalProtocols_Object=MibScalar
alaBfdGlobalProtocols=_AlaBfdGlobalProtocols_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,1,7),_AlaBfdGlobalProtocols_Type())
alaBfdGlobalProtocols.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdGlobalProtocols.setStatus(_A)
_AlaBfdGlobalEchoObjects_ObjectIdentity=ObjectIdentity
alaBfdGlobalEchoObjects=_AlaBfdGlobalEchoObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,2))
_AlaBfdGlobalEcho_Type=AlaBfdStatus
_AlaBfdGlobalEcho_Object=MibScalar
alaBfdGlobalEcho=_AlaBfdGlobalEcho_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,2,1),_AlaBfdGlobalEcho_Type())
alaBfdGlobalEcho.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalEcho.setStatus(_A)
class _AlaBfdGlobalEchoRxInterval_Type(AlaBfdInterval):defaultValue=300
_AlaBfdGlobalEchoRxInterval_Type.__name__=_H
_AlaBfdGlobalEchoRxInterval_Object=MibScalar
alaBfdGlobalEchoRxInterval=_AlaBfdGlobalEchoRxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,2,2),_AlaBfdGlobalEchoRxInterval_Type())
alaBfdGlobalEchoRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalEchoRxInterval.setStatus(_A)
_AlaBfdIntfTable_Object=MibTable
alaBfdIntfTable=_AlaBfdIntfTable_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3))
if mibBuilder.loadTexts:alaBfdIntfTable.setStatus(_A)
_AlaBfdIntfEntry_Object=MibTableRow
alaBfdIntfEntry=_AlaBfdIntfEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1))
alaBfdIntfEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:alaBfdIntfEntry.setStatus(_A)
_AlaBfdIntfAddrType_Type=InetAddressType
_AlaBfdIntfAddrType_Object=MibTableColumn
alaBfdIntfAddrType=_AlaBfdIntfAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,1),_AlaBfdIntfAddrType_Type())
alaBfdIntfAddrType.setMaxAccess(_O)
if mibBuilder.loadTexts:alaBfdIntfAddrType.setStatus(_A)
_AlaBfdIntfAddr_Type=InetAddress
_AlaBfdIntfAddr_Object=MibTableColumn
alaBfdIntfAddr=_AlaBfdIntfAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,2),_AlaBfdIntfAddr_Type())
alaBfdIntfAddr.setMaxAccess(_O)
if mibBuilder.loadTexts:alaBfdIntfAddr.setStatus(_A)
_AlaBfdIntfIndex_Type=InterfaceIndex
_AlaBfdIntfIndex_Object=MibTableColumn
alaBfdIntfIndex=_AlaBfdIntfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,3),_AlaBfdIntfIndex_Type())
alaBfdIntfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdIntfIndex.setStatus(_A)
class _AlabfdIntfAdminStatus_Type(AlaBfdStatus):defaultValue=2
_AlabfdIntfAdminStatus_Type.__name__=_K
_AlabfdIntfAdminStatus_Object=MibTableColumn
alabfdIntfAdminStatus=_AlabfdIntfAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,4),_AlabfdIntfAdminStatus_Type())
alabfdIntfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alabfdIntfAdminStatus.setStatus(_A)
_AlaBfdIntfDesiredMinTxInterval_Type=AlaBfdInterval
_AlaBfdIntfDesiredMinTxInterval_Object=MibTableColumn
alaBfdIntfDesiredMinTxInterval=_AlaBfdIntfDesiredMinTxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,5),_AlaBfdIntfDesiredMinTxInterval_Type())
alaBfdIntfDesiredMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfDesiredMinTxInterval.setStatus(_A)
_AlaBfdIntfReqMinRxInterval_Type=AlaBfdInterval
_AlaBfdIntfReqMinRxInterval_Object=MibTableColumn
alaBfdIntfReqMinRxInterval=_AlaBfdIntfReqMinRxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,6),_AlaBfdIntfReqMinRxInterval_Type())
alaBfdIntfReqMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfReqMinRxInterval.setStatus(_A)
class _AlaBfdIntfOperMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_AlaBfdIntfOperMode_Type.__name__=_E
_AlaBfdIntfOperMode_Object=MibTableColumn
alaBfdIntfOperMode=_AlaBfdIntfOperMode_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,7),_AlaBfdIntfOperMode_Type())
alaBfdIntfOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfOperMode.setStatus(_A)
_AlaBfdIntfEchoMode_Type=AlaBfdStatus
_AlaBfdIntfEchoMode_Object=MibTableColumn
alaBfdIntfEchoMode=_AlaBfdIntfEchoMode_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,8),_AlaBfdIntfEchoMode_Type())
alaBfdIntfEchoMode.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfEchoMode.setStatus(_A)
_AlaBfdIntfReqMinEchoRxInterval_Type=AlaBfdInterval
_AlaBfdIntfReqMinEchoRxInterval_Object=MibTableColumn
alaBfdIntfReqMinEchoRxInterval=_AlaBfdIntfReqMinEchoRxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,9),_AlaBfdIntfReqMinEchoRxInterval_Type())
alaBfdIntfReqMinEchoRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfReqMinEchoRxInterval.setStatus(_A)
class _AlaBfdIntfDetectMult_Type(Unsigned32):defaultValue=3
_AlaBfdIntfDetectMult_Type.__name__=_G
_AlaBfdIntfDetectMult_Object=MibTableColumn
alaBfdIntfDetectMult=_AlaBfdIntfDetectMult_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,10),_AlaBfdIntfDetectMult_Type())
alaBfdIntfDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfDetectMult.setStatus(_A)
class _AlaBfdIntfsesstype_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleHop',1),('multiHop',2)))
_AlaBfdIntfsesstype_Type.__name__=_E
_AlaBfdIntfsesstype_Object=MibTableColumn
alaBfdIntfsesstype=_AlaBfdIntfsesstype_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,11),_AlaBfdIntfsesstype_Type())
alaBfdIntfsesstype.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfsesstype.setStatus(_A)
class _AlaBfdIntfAuthPresFlag_Type(TruthValue):defaultValue=2
_AlaBfdIntfAuthPresFlag_Type.__name__=_J
_AlaBfdIntfAuthPresFlag_Object=MibTableColumn
alaBfdIntfAuthPresFlag=_AlaBfdIntfAuthPresFlag_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,12),_AlaBfdIntfAuthPresFlag_Type())
alaBfdIntfAuthPresFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAuthPresFlag.setStatus(_A)
class _AlaBfdIntfAuthenticationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('simplePassword',2),('keyedMD5',3),('meticulousKeyedMD5',4),('keyedSHA1',5),('meticulousKeyedSHA1',6)))
_AlaBfdIntfAuthenticationType_Type.__name__=_E
_AlaBfdIntfAuthenticationType_Object=MibTableColumn
alaBfdIntfAuthenticationType=_AlaBfdIntfAuthenticationType_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,13),_AlaBfdIntfAuthenticationType_Type())
alaBfdIntfAuthenticationType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAuthenticationType.setStatus(_A)
_AlaBfdIntfL2HoldTimer_Type=AlaBfdInterval
_AlaBfdIntfL2HoldTimer_Object=MibTableColumn
alaBfdIntfL2HoldTimer=_AlaBfdIntfL2HoldTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,14),_AlaBfdIntfL2HoldTimer_Type())
alaBfdIntfL2HoldTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfL2HoldTimer.setStatus(_A)
_AlaBfdIntfRowStatus_Type=RowStatus
_AlaBfdIntfRowStatus_Object=MibTableColumn
alaBfdIntfRowStatus=_AlaBfdIntfRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,3,1,15),_AlaBfdIntfRowStatus_Type())
alaBfdIntfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfRowStatus.setStatus(_A)
_AlaBfdSessTable_Object=MibTable
alaBfdSessTable=_AlaBfdSessTable_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4))
if mibBuilder.loadTexts:alaBfdSessTable.setStatus(_A)
_AlaBfdSessEntry_Object=MibTableRow
alaBfdSessEntry=_AlaBfdSessEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1))
alaBfdSessEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:alaBfdSessEntry.setStatus(_A)
class _AlaBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AlaBfdSessDiscriminator_Type.__name__=_G
_AlaBfdSessDiscriminator_Object=MibTableColumn
alaBfdSessDiscriminator=_AlaBfdSessDiscriminator_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,1),_AlaBfdSessDiscriminator_Type())
alaBfdSessDiscriminator.setMaxAccess(_O)
if mibBuilder.loadTexts:alaBfdSessDiscriminator.setStatus(_A)
_AlaBfdSessNeighborAddrType_Type=InetAddressType
_AlaBfdSessNeighborAddrType_Object=MibTableColumn
alaBfdSessNeighborAddrType=_AlaBfdSessNeighborAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,2),_AlaBfdSessNeighborAddrType_Type())
alaBfdSessNeighborAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNeighborAddrType.setStatus(_A)
_AlaBfdSessNeighborAddr_Type=InetAddress
_AlaBfdSessNeighborAddr_Object=MibTableColumn
alaBfdSessNeighborAddr=_AlaBfdSessNeighborAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,3),_AlaBfdSessNeighborAddr_Type())
alaBfdSessNeighborAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNeighborAddr.setStatus(_A)
class _AlaBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AlaBfdSessRemoteDiscr_Type.__name__=_G
_AlaBfdSessRemoteDiscr_Object=MibTableColumn
alaBfdSessRemoteDiscr=_AlaBfdSessRemoteDiscr_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,4),_AlaBfdSessRemoteDiscr_Type())
alaBfdSessRemoteDiscr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessRemoteDiscr.setStatus(_A)
_AlaBfdSessUdpPort_Type=InetPortNumber
_AlaBfdSessUdpPort_Object=MibTableColumn
alaBfdSessUdpPort=_AlaBfdSessUdpPort_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,5),_AlaBfdSessUdpPort_Type())
alaBfdSessUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessUdpPort.setStatus(_A)
class _AlaBfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
_AlaBfdSessState_Type.__name__=_E
_AlaBfdSessState_Object=MibTableColumn
alaBfdSessState=_AlaBfdSessState_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,6),_AlaBfdSessState_Type())
alaBfdSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessState.setStatus(_A)
_AlaBfdSessRemoteHeardFlag_Type=TruthValue
_AlaBfdSessRemoteHeardFlag_Object=MibTableColumn
alaBfdSessRemoteHeardFlag=_AlaBfdSessRemoteHeardFlag_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,7),_AlaBfdSessRemoteHeardFlag_Type())
alaBfdSessRemoteHeardFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessRemoteHeardFlag.setStatus(_A)
_AlaBfdSessDiag_Type=AlaBfdDiag
_AlaBfdSessDiag_Object=MibTableColumn
alaBfdSessDiag=_AlaBfdSessDiag_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,8),_AlaBfdSessDiag_Type())
alaBfdSessDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessDiag.setStatus(_A)
class _AlaBfdSessOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_AlaBfdSessOperMode_Type.__name__=_E
_AlaBfdSessOperMode_Object=MibTableColumn
alaBfdSessOperMode=_AlaBfdSessOperMode_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,9),_AlaBfdSessOperMode_Type())
alaBfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessOperMode.setStatus(_A)
_AlaBfdSessEchoFuncModeDesiredFlag_Type=TruthValue
_AlaBfdSessEchoFuncModeDesiredFlag_Object=MibTableColumn
alaBfdSessEchoFuncModeDesiredFlag=_AlaBfdSessEchoFuncModeDesiredFlag_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,10),_AlaBfdSessEchoFuncModeDesiredFlag_Type())
alaBfdSessEchoFuncModeDesiredFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessEchoFuncModeDesiredFlag.setStatus(_A)
class _AlaBfdSessControlPlanIndepFlag_Type(TruthValue):defaultValue=1
_AlaBfdSessControlPlanIndepFlag_Type.__name__=_J
_AlaBfdSessControlPlanIndepFlag_Object=MibTableColumn
alaBfdSessControlPlanIndepFlag=_AlaBfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,11),_AlaBfdSessControlPlanIndepFlag_Type())
alaBfdSessControlPlanIndepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessControlPlanIndepFlag.setStatus(_A)
_AlaBfdSessInterface_Type=InterfaceIndexOrZero
_AlaBfdSessInterface_Object=MibTableColumn
alaBfdSessInterface=_AlaBfdSessInterface_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,12),_AlaBfdSessInterface_Type())
alaBfdSessInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessInterface.setStatus(_A)
_AlaBfdSessNegotiatedTxInterval_Type=AlaBfdInterval
_AlaBfdSessNegotiatedTxInterval_Object=MibTableColumn
alaBfdSessNegotiatedTxInterval=_AlaBfdSessNegotiatedTxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,13),_AlaBfdSessNegotiatedTxInterval_Type())
alaBfdSessNegotiatedTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNegotiatedTxInterval.setStatus(_A)
_AlaBfdSessNegotiatedRxInterval_Type=AlaBfdInterval
_AlaBfdSessNegotiatedRxInterval_Object=MibTableColumn
alaBfdSessNegotiatedRxInterval=_AlaBfdSessNegotiatedRxInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,14),_AlaBfdSessNegotiatedRxInterval_Type())
alaBfdSessNegotiatedRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNegotiatedRxInterval.setStatus(_A)
class _AlaBfdSessProtocols_Type(Bits):namedValues=NamedValues(*(('ospf',0),('bgp',1),('dvmrp',2),('vrrp',3),('iprm',4)))
_AlaBfdSessProtocols_Type.__name__=_I
_AlaBfdSessProtocols_Object=MibTableColumn
alaBfdSessProtocols=_AlaBfdSessProtocols_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,4,1,15),_AlaBfdSessProtocols_Type())
alaBfdSessProtocols.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessProtocols.setStatus(_A)
_AlaBfdSessPerfTable_Object=MibTable
alaBfdSessPerfTable=_AlaBfdSessPerfTable_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5))
if mibBuilder.loadTexts:alaBfdSessPerfTable.setStatus(_A)
_AlaBfdSessPerfEntry_Object=MibTableRow
alaBfdSessPerfEntry=_AlaBfdSessPerfEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1))
if mibBuilder.loadTexts:alaBfdSessPerfEntry.setStatus(_A)
_AlaBfdSessPerfPktIn_Type=Counter64
_AlaBfdSessPerfPktIn_Object=MibTableColumn
alaBfdSessPerfPktIn=_AlaBfdSessPerfPktIn_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,1),_AlaBfdSessPerfPktIn_Type())
alaBfdSessPerfPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfPktIn.setStatus(_A)
_AlaBfdSessPerfPktOut_Type=Counter64
_AlaBfdSessPerfPktOut_Object=MibTableColumn
alaBfdSessPerfPktOut=_AlaBfdSessPerfPktOut_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,2),_AlaBfdSessPerfPktOut_Type())
alaBfdSessPerfPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfPktOut.setStatus(_A)
_AlaBfdSessPerfEchoOut_Type=Counter64
_AlaBfdSessPerfEchoOut_Object=MibTableColumn
alaBfdSessPerfEchoOut=_AlaBfdSessPerfEchoOut_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,3),_AlaBfdSessPerfEchoOut_Type())
alaBfdSessPerfEchoOut.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfEchoOut.setStatus(_A)
_AlaBfdSessPerfUpTime_Type=TimeTicks
_AlaBfdSessPerfUpTime_Object=MibTableColumn
alaBfdSessPerfUpTime=_AlaBfdSessPerfUpTime_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,4),_AlaBfdSessPerfUpTime_Type())
alaBfdSessPerfUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfUpTime.setStatus(_A)
_AlaBfdSessPerfLastSessDownTime_Type=TimeTicks
_AlaBfdSessPerfLastSessDownTime_Object=MibTableColumn
alaBfdSessPerfLastSessDownTime=_AlaBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,5),_AlaBfdSessPerfLastSessDownTime_Type())
alaBfdSessPerfLastSessDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfLastSessDownTime.setStatus(_A)
_AlaBfdSessPerfLastCommLostDiag_Type=AlaBfdDiag
_AlaBfdSessPerfLastCommLostDiag_Object=MibTableColumn
alaBfdSessPerfLastCommLostDiag=_AlaBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,6),_AlaBfdSessPerfLastCommLostDiag_Type())
alaBfdSessPerfLastCommLostDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfLastCommLostDiag.setStatus(_A)
_AlaBfdSessPerfSessUpCount_Type=Counter64
_AlaBfdSessPerfSessUpCount_Object=MibTableColumn
alaBfdSessPerfSessUpCount=_AlaBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,7),_AlaBfdSessPerfSessUpCount_Type())
alaBfdSessPerfSessUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfSessUpCount.setStatus(_A)
_AlaBfdSessPerfDiscTime_Type=TimeTicks
_AlaBfdSessPerfDiscTime_Object=MibTableColumn
alaBfdSessPerfDiscTime=_AlaBfdSessPerfDiscTime_Object((1,3,6,1,4,1,6486,800,1,2,1,45,1,1,5,1,8),_AlaBfdSessPerfDiscTime_Type())
alaBfdSessPerfDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfDiscTime.setStatus(_A)
_AlcatelIND1BfdMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1BfdMIBConformance=_AlcatelIND1BfdMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1,2))
if mibBuilder.loadTexts:alcatelIND1BfdMIBConformance.setStatus(_A)
_AlcatelIND1BfdMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1BfdMIBGroups=_AlcatelIND1BfdMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,1))
_AlcatelIND1BfdMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1BfdMIBCompliances=_AlcatelIND1BfdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,2))
alaBfdSessEntry.registerAugmentions((_B,_S))
alaBfdSessPerfEntry.setIndexNames(*alaBfdSessEntry.getIndexNames())
alaBfdbasicGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,1,1))
alaBfdbasicGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:alaBfdbasicGroup.setStatus(_A)
alaBfdIntfCfgGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,1,2))
alaBfdIntfCfgGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:alaBfdIntfCfgGroup.setStatus(_A)
alaBfdSessGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,1,3))
alaBfdSessGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:alaBfdSessGroup.setStatus(_A)
alaBfdSessPerfGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,1,4))
alaBfdSessPerfGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:alaBfdSessPerfGroup.setStatus(_A)
alcatelIND1BfdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,45,1,2,2,1))
alcatelIND1BfdMIBCompliance.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:alcatelIND1BfdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:AlaBfdInterval,'AlaBfdDiag':AlaBfdDiag,_K:AlaBfdStatus,'alcatelIND1BfdMIB':alcatelIND1BfdMIB,'alaBfdObjects':alaBfdObjects,'alaBfdGlobalObjects':alaBfdGlobalObjects,_T:alaBfdGlobalAdminStatus,_U:alaBfdGlobalTxInterval,_V:alaBfdGlobalRxInterval,_W:alaBfdGlobalOperMode,_X:alaBfdGlobalVersionNumber,_Y:alaBfdGlobalL2HoldTimer,_Z:alaBfdGlobalProtocols,'alaBfdGlobalEchoObjects':alaBfdGlobalEchoObjects,_a:alaBfdGlobalEcho,_b:alaBfdGlobalEchoRxInterval,'alaBfdIntfTable':alaBfdIntfTable,'alaBfdIntfEntry':alaBfdIntfEntry,_P:alaBfdIntfAddrType,_Q:alaBfdIntfAddr,_c:alaBfdIntfIndex,_d:alabfdIntfAdminStatus,_e:alaBfdIntfDesiredMinTxInterval,_f:alaBfdIntfReqMinRxInterval,_i:alaBfdIntfOperMode,_g:alaBfdIntfEchoMode,_h:alaBfdIntfReqMinEchoRxInterval,_j:alaBfdIntfDetectMult,_k:alaBfdIntfsesstype,_l:alaBfdIntfAuthPresFlag,_m:alaBfdIntfAuthenticationType,_n:alaBfdIntfL2HoldTimer,_o:alaBfdIntfRowStatus,'alaBfdSessTable':alaBfdSessTable,'alaBfdSessEntry':alaBfdSessEntry,_R:alaBfdSessDiscriminator,_p:alaBfdSessNeighborAddrType,_q:alaBfdSessNeighborAddr,_r:alaBfdSessRemoteDiscr,_s:alaBfdSessUdpPort,_t:alaBfdSessState,_u:alaBfdSessRemoteHeardFlag,_v:alaBfdSessDiag,_w:alaBfdSessOperMode,_x:alaBfdSessEchoFuncModeDesiredFlag,_y:alaBfdSessControlPlanIndepFlag,_z:alaBfdSessInterface,_A0:alaBfdSessNegotiatedTxInterval,_A1:alaBfdSessNegotiatedRxInterval,_A2:alaBfdSessProtocols,'alaBfdSessPerfTable':alaBfdSessPerfTable,_S:alaBfdSessPerfEntry,_A3:alaBfdSessPerfPktIn,_A4:alaBfdSessPerfPktOut,_A5:alaBfdSessPerfEchoOut,_A6:alaBfdSessPerfUpTime,_A7:alaBfdSessPerfLastSessDownTime,_A8:alaBfdSessPerfLastCommLostDiag,_A9:alaBfdSessPerfSessUpCount,_AA:alaBfdSessPerfDiscTime,'alcatelIND1BfdMIBConformance':alcatelIND1BfdMIBConformance,'alcatelIND1BfdMIBGroups':alcatelIND1BfdMIBGroups,_AB:alaBfdbasicGroup,_AC:alaBfdIntfCfgGroup,_AD:alaBfdSessGroup,_AE:alaBfdSessPerfGroup,'alcatelIND1BfdMIBCompliances':alcatelIND1BfdMIBCompliances,'alcatelIND1BfdMIBCompliance':alcatelIND1BfdMIBCompliance})