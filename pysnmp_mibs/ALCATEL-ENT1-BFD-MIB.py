_A9='alaBfdSessPerfGroup'
_A8='alaBfdSessGroup'
_A7='alaBfdIntfCfgGroup'
_A6='alaBfdBasicGroup'
_A5='alaBfdSessPerfDiscTime'
_A4='alaBfdSessPerfSessUpCount'
_A3='alaBfdSessPerfLastCommLostDiag'
_A2='alaBfdSessPerfLastSessDownTime'
_A1='alaBfdSessPerfUpTime'
_A0='alaBfdSessPerfEchoIn'
_z='alaBfdSessPerfEchoOut'
_y='alaBfdSessPerfPktOut'
_x='alaBfdSessPerfPktIn'
_w='alaBfdSessProtocolApps'
_v='alaBfdSessEchoRxInterval'
_u='alaBfdSessNegotiatedRxInterval'
_t='alaBfdSessNegotiatedTxInterval'
_s='alaBfdSessIfIndex'
_r='alaBfdSessControlPlanIndepFlag'
_q='alaBfdSessOperMode'
_p='alaBfdSessDiag'
_o='alaBfdSessState'
_n='alaBfdSessUdpPort'
_m='alaBfdSessRemoteDiscr'
_l='alaBfdSessSessionType'
_k='alaBfdSessNeighborAddr'
_j='alaBfdSessNeighborAddrType'
_i='alaBfdIntfRowStatus'
_h='alaBfdIntfOperStatus'
_g='alaBfdIntfIfName'
_f='alaBfdIntfAuthenticationType'
_e='alaBfdIntfAuthPresFlag'
_d='alaBfdIntfDetectMult'
_c='alaBfdIntfReqMinEchoRxInterval'
_b='alaBfdIntfReqMinRxInterval'
_a='alaBfdIntfDesiredMinTxInterval'
_Z='alaBfdIntfAdminStatus'
_Y='alaBfdIntfAddrType'
_X='alaBfdIntfAddr'
_W='alaBfdGlobalProtocolApps'
_V='alaBfdGlobalEchoRxInterval'
_U='alaBfdGlobalDetectMult'
_T='alaBfdGlobalRxInterval'
_S='alaBfdGlobalTxInterval'
_R='alaBfdGlobalAdminStatus'
_Q='alaBfdGlobalVersionNumber'
_P='alaBfdSessPerfEntry'
_O='alaBfdSessDiscriminator'
_N='not-accessible'
_M='alaBfdIntfIndex'
_L='staticRtg'
_K='TruthValue'
_J='AlaBfdStatus'
_I='AlaBfdInterval'
_H='Unsigned32'
_G='Bits'
_F='read-write'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='ALCATEL-ENT1-BFD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1BFD,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1BFD')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
alcatelIND1BfdMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,45,1))
if mibBuilder.loadTexts:alcatelIND1BfdMIB.setRevisions(('2010-05-05 00:00',))
class AlaBfdInterval(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class AlaBfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8)))
class AlaBfdStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaBfdObjects_ObjectIdentity=ObjectIdentity
alaBfdObjects=_AlaBfdObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,45,1,1))
if mibBuilder.loadTexts:alaBfdObjects.setStatus(_A)
_AlaBfdGlobalObjects_ObjectIdentity=ObjectIdentity
alaBfdGlobalObjects=_AlaBfdGlobalObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1))
class _AlaBfdGlobalVersionNumber_Type(Unsigned32):defaultValue=1
_AlaBfdGlobalVersionNumber_Type.__name__=_H
_AlaBfdGlobalVersionNumber_Object=MibScalar
alaBfdGlobalVersionNumber=_AlaBfdGlobalVersionNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,1),_AlaBfdGlobalVersionNumber_Type())
alaBfdGlobalVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdGlobalVersionNumber.setStatus(_A)
class _AlaBfdGlobalAdminStatus_Type(AlaBfdStatus):defaultValue=2
_AlaBfdGlobalAdminStatus_Type.__name__=_J
_AlaBfdGlobalAdminStatus_Object=MibScalar
alaBfdGlobalAdminStatus=_AlaBfdGlobalAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,2),_AlaBfdGlobalAdminStatus_Type())
alaBfdGlobalAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalAdminStatus.setStatus(_A)
class _AlaBfdGlobalTxInterval_Type(AlaBfdInterval):defaultValue=300
_AlaBfdGlobalTxInterval_Type.__name__=_I
_AlaBfdGlobalTxInterval_Object=MibScalar
alaBfdGlobalTxInterval=_AlaBfdGlobalTxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,3),_AlaBfdGlobalTxInterval_Type())
alaBfdGlobalTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalTxInterval.setStatus(_A)
class _AlaBfdGlobalRxInterval_Type(AlaBfdInterval):defaultValue=300
_AlaBfdGlobalRxInterval_Type.__name__=_I
_AlaBfdGlobalRxInterval_Object=MibScalar
alaBfdGlobalRxInterval=_AlaBfdGlobalRxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,4),_AlaBfdGlobalRxInterval_Type())
alaBfdGlobalRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalRxInterval.setStatus(_A)
class _AlaBfdGlobalDetectMult_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_AlaBfdGlobalDetectMult_Type.__name__=_E
_AlaBfdGlobalDetectMult_Object=MibScalar
alaBfdGlobalDetectMult=_AlaBfdGlobalDetectMult_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,5),_AlaBfdGlobalDetectMult_Type())
alaBfdGlobalDetectMult.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalDetectMult.setStatus(_A)
class _AlaBfdGlobalEchoRxInterval_Type(AlaBfdInterval):defaultValue=300
_AlaBfdGlobalEchoRxInterval_Type.__name__=_I
_AlaBfdGlobalEchoRxInterval_Object=MibScalar
alaBfdGlobalEchoRxInterval=_AlaBfdGlobalEchoRxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,6),_AlaBfdGlobalEchoRxInterval_Type())
alaBfdGlobalEchoRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:alaBfdGlobalEchoRxInterval.setStatus(_A)
class _AlaBfdGlobalProtocolApps_Type(Bits):namedValues=NamedValues(*(('vrrp',0),(_L,1),('ospf',2),('bgp',3),('isis',4),('pim',5),('dvmrp',6),('ospf3',7)))
_AlaBfdGlobalProtocolApps_Type.__name__=_G
_AlaBfdGlobalProtocolApps_Object=MibScalar
alaBfdGlobalProtocolApps=_AlaBfdGlobalProtocolApps_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,1,7),_AlaBfdGlobalProtocolApps_Type())
alaBfdGlobalProtocolApps.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdGlobalProtocolApps.setStatus(_A)
_AlaBfdIntfTable_Object=MibTable
alaBfdIntfTable=_AlaBfdIntfTable_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2))
if mibBuilder.loadTexts:alaBfdIntfTable.setStatus(_A)
_AlaBfdIntfEntry_Object=MibTableRow
alaBfdIntfEntry=_AlaBfdIntfEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1))
alaBfdIntfEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:alaBfdIntfEntry.setStatus(_A)
_AlaBfdIntfIndex_Type=InterfaceIndex
_AlaBfdIntfIndex_Object=MibTableColumn
alaBfdIntfIndex=_AlaBfdIntfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,1),_AlaBfdIntfIndex_Type())
alaBfdIntfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:alaBfdIntfIndex.setStatus(_A)
_AlaBfdIntfAddrType_Type=InetAddressType
_AlaBfdIntfAddrType_Object=MibTableColumn
alaBfdIntfAddrType=_AlaBfdIntfAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,2),_AlaBfdIntfAddrType_Type())
alaBfdIntfAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAddrType.setStatus(_A)
_AlaBfdIntfAddr_Type=InetAddress
_AlaBfdIntfAddr_Object=MibTableColumn
alaBfdIntfAddr=_AlaBfdIntfAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,3),_AlaBfdIntfAddr_Type())
alaBfdIntfAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAddr.setStatus(_A)
class _AlaBfdIntfAdminStatus_Type(AlaBfdStatus):defaultValue=2
_AlaBfdIntfAdminStatus_Type.__name__=_J
_AlaBfdIntfAdminStatus_Object=MibTableColumn
alaBfdIntfAdminStatus=_AlaBfdIntfAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,4),_AlaBfdIntfAdminStatus_Type())
alaBfdIntfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAdminStatus.setStatus(_A)
_AlaBfdIntfDesiredMinTxInterval_Type=AlaBfdInterval
_AlaBfdIntfDesiredMinTxInterval_Object=MibTableColumn
alaBfdIntfDesiredMinTxInterval=_AlaBfdIntfDesiredMinTxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,5),_AlaBfdIntfDesiredMinTxInterval_Type())
alaBfdIntfDesiredMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfDesiredMinTxInterval.setStatus(_A)
_AlaBfdIntfReqMinRxInterval_Type=AlaBfdInterval
_AlaBfdIntfReqMinRxInterval_Object=MibTableColumn
alaBfdIntfReqMinRxInterval=_AlaBfdIntfReqMinRxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,6),_AlaBfdIntfReqMinRxInterval_Type())
alaBfdIntfReqMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfReqMinRxInterval.setStatus(_A)
_AlaBfdIntfReqMinEchoRxInterval_Type=AlaBfdInterval
_AlaBfdIntfReqMinEchoRxInterval_Object=MibTableColumn
alaBfdIntfReqMinEchoRxInterval=_AlaBfdIntfReqMinEchoRxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,7),_AlaBfdIntfReqMinEchoRxInterval_Type())
alaBfdIntfReqMinEchoRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfReqMinEchoRxInterval.setStatus(_A)
class _AlaBfdIntfDetectMult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_AlaBfdIntfDetectMult_Type.__name__=_E
_AlaBfdIntfDetectMult_Object=MibTableColumn
alaBfdIntfDetectMult=_AlaBfdIntfDetectMult_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,8),_AlaBfdIntfDetectMult_Type())
alaBfdIntfDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfDetectMult.setStatus(_A)
class _AlaBfdIntfAuthPresFlag_Type(TruthValue):defaultValue=2
_AlaBfdIntfAuthPresFlag_Type.__name__=_K
_AlaBfdIntfAuthPresFlag_Object=MibTableColumn
alaBfdIntfAuthPresFlag=_AlaBfdIntfAuthPresFlag_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,9),_AlaBfdIntfAuthPresFlag_Type())
alaBfdIntfAuthPresFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAuthPresFlag.setStatus(_A)
class _AlaBfdIntfAuthenticationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('simplePassword',2),('keyedMD5',3),('meticulousKeyedMD5',4),('keyedSHA1',5),('meticulousKeyedSHA1',6)))
_AlaBfdIntfAuthenticationType_Type.__name__=_E
_AlaBfdIntfAuthenticationType_Object=MibTableColumn
alaBfdIntfAuthenticationType=_AlaBfdIntfAuthenticationType_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,10),_AlaBfdIntfAuthenticationType_Type())
alaBfdIntfAuthenticationType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfAuthenticationType.setStatus(_A)
_AlaBfdIntfIfName_Type=SnmpAdminString
_AlaBfdIntfIfName_Object=MibTableColumn
alaBfdIntfIfName=_AlaBfdIntfIfName_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,11),_AlaBfdIntfIfName_Type())
alaBfdIntfIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfIfName.setStatus(_A)
class _AlaBfdIntfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AlaBfdIntfOperStatus_Type.__name__=_E
_AlaBfdIntfOperStatus_Object=MibTableColumn
alaBfdIntfOperStatus=_AlaBfdIntfOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,12),_AlaBfdIntfOperStatus_Type())
alaBfdIntfOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfOperStatus.setStatus(_A)
_AlaBfdIntfRowStatus_Type=RowStatus
_AlaBfdIntfRowStatus_Object=MibTableColumn
alaBfdIntfRowStatus=_AlaBfdIntfRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,2,1,13),_AlaBfdIntfRowStatus_Type())
alaBfdIntfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaBfdIntfRowStatus.setStatus(_A)
_AlaBfdSessTable_Object=MibTable
alaBfdSessTable=_AlaBfdSessTable_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3))
if mibBuilder.loadTexts:alaBfdSessTable.setStatus(_A)
_AlaBfdSessEntry_Object=MibTableRow
alaBfdSessEntry=_AlaBfdSessEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1))
alaBfdSessEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:alaBfdSessEntry.setStatus(_A)
class _AlaBfdSessDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_AlaBfdSessDiscriminator_Type.__name__=_H
_AlaBfdSessDiscriminator_Object=MibTableColumn
alaBfdSessDiscriminator=_AlaBfdSessDiscriminator_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,1),_AlaBfdSessDiscriminator_Type())
alaBfdSessDiscriminator.setMaxAccess(_N)
if mibBuilder.loadTexts:alaBfdSessDiscriminator.setStatus(_A)
_AlaBfdSessNeighborAddrType_Type=InetAddressType
_AlaBfdSessNeighborAddrType_Object=MibTableColumn
alaBfdSessNeighborAddrType=_AlaBfdSessNeighborAddrType_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,2),_AlaBfdSessNeighborAddrType_Type())
alaBfdSessNeighborAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNeighborAddrType.setStatus(_A)
_AlaBfdSessNeighborAddr_Type=InetAddress
_AlaBfdSessNeighborAddr_Object=MibTableColumn
alaBfdSessNeighborAddr=_AlaBfdSessNeighborAddr_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,3),_AlaBfdSessNeighborAddr_Type())
alaBfdSessNeighborAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNeighborAddr.setStatus(_A)
class _AlaBfdSessSessionType_Type(Bits):namedValues=NamedValues(*(('asynchronous',0),('echo',1),('demand',2)))
_AlaBfdSessSessionType_Type.__name__=_G
_AlaBfdSessSessionType_Object=MibTableColumn
alaBfdSessSessionType=_AlaBfdSessSessionType_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,4),_AlaBfdSessSessionType_Type())
alaBfdSessSessionType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessSessionType.setStatus(_A)
class _AlaBfdSessRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AlaBfdSessRemoteDiscr_Type.__name__=_H
_AlaBfdSessRemoteDiscr_Object=MibTableColumn
alaBfdSessRemoteDiscr=_AlaBfdSessRemoteDiscr_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,5),_AlaBfdSessRemoteDiscr_Type())
alaBfdSessRemoteDiscr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessRemoteDiscr.setStatus(_A)
_AlaBfdSessUdpPort_Type=InetPortNumber
_AlaBfdSessUdpPort_Object=MibTableColumn
alaBfdSessUdpPort=_AlaBfdSessUdpPort_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,6),_AlaBfdSessUdpPort_Type())
alaBfdSessUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessUdpPort.setStatus(_A)
class _AlaBfdSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4)))
_AlaBfdSessState_Type.__name__=_E
_AlaBfdSessState_Object=MibTableColumn
alaBfdSessState=_AlaBfdSessState_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,7),_AlaBfdSessState_Type())
alaBfdSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessState.setStatus(_A)
_AlaBfdSessDiag_Type=AlaBfdDiag
_AlaBfdSessDiag_Object=MibTableColumn
alaBfdSessDiag=_AlaBfdSessDiag_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,8),_AlaBfdSessDiag_Type())
alaBfdSessDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessDiag.setStatus(_A)
class _AlaBfdSessOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('asyncModeWEchoFunction',1),('asynchModeWOEchoFunction',2),('demandModeWEchoFunction',3),('demandModeWOEchoFunction',4),('echoOnly',5)))
_AlaBfdSessOperMode_Type.__name__=_E
_AlaBfdSessOperMode_Object=MibTableColumn
alaBfdSessOperMode=_AlaBfdSessOperMode_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,10),_AlaBfdSessOperMode_Type())
alaBfdSessOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessOperMode.setStatus(_A)
_AlaBfdSessControlPlanIndepFlag_Type=TruthValue
_AlaBfdSessControlPlanIndepFlag_Object=MibTableColumn
alaBfdSessControlPlanIndepFlag=_AlaBfdSessControlPlanIndepFlag_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,11),_AlaBfdSessControlPlanIndepFlag_Type())
alaBfdSessControlPlanIndepFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessControlPlanIndepFlag.setStatus(_A)
_AlaBfdSessIfIndex_Type=InterfaceIndexOrZero
_AlaBfdSessIfIndex_Object=MibTableColumn
alaBfdSessIfIndex=_AlaBfdSessIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,12),_AlaBfdSessIfIndex_Type())
alaBfdSessIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessIfIndex.setStatus(_A)
_AlaBfdSessNegotiatedTxInterval_Type=AlaBfdInterval
_AlaBfdSessNegotiatedTxInterval_Object=MibTableColumn
alaBfdSessNegotiatedTxInterval=_AlaBfdSessNegotiatedTxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,13),_AlaBfdSessNegotiatedTxInterval_Type())
alaBfdSessNegotiatedTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNegotiatedTxInterval.setStatus(_A)
_AlaBfdSessNegotiatedRxInterval_Type=AlaBfdInterval
_AlaBfdSessNegotiatedRxInterval_Object=MibTableColumn
alaBfdSessNegotiatedRxInterval=_AlaBfdSessNegotiatedRxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,14),_AlaBfdSessNegotiatedRxInterval_Type())
alaBfdSessNegotiatedRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessNegotiatedRxInterval.setStatus(_A)
_AlaBfdSessEchoRxInterval_Type=AlaBfdInterval
_AlaBfdSessEchoRxInterval_Object=MibTableColumn
alaBfdSessEchoRxInterval=_AlaBfdSessEchoRxInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,15),_AlaBfdSessEchoRxInterval_Type())
alaBfdSessEchoRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessEchoRxInterval.setStatus(_A)
class _AlaBfdSessProtocolApps_Type(Bits):namedValues=NamedValues(*(('vrrp',0),(_L,1),('ospf',2),('bgp',3),('isis',4),('pim',5),('dvmrp',6),('ospf3',7)))
_AlaBfdSessProtocolApps_Type.__name__=_G
_AlaBfdSessProtocolApps_Object=MibTableColumn
alaBfdSessProtocolApps=_AlaBfdSessProtocolApps_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,3,1,16),_AlaBfdSessProtocolApps_Type())
alaBfdSessProtocolApps.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessProtocolApps.setStatus(_A)
_AlaBfdSessPerfTable_Object=MibTable
alaBfdSessPerfTable=_AlaBfdSessPerfTable_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4))
if mibBuilder.loadTexts:alaBfdSessPerfTable.setStatus(_A)
_AlaBfdSessPerfEntry_Object=MibTableRow
alaBfdSessPerfEntry=_AlaBfdSessPerfEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1))
if mibBuilder.loadTexts:alaBfdSessPerfEntry.setStatus(_A)
_AlaBfdSessPerfPktIn_Type=Counter64
_AlaBfdSessPerfPktIn_Object=MibTableColumn
alaBfdSessPerfPktIn=_AlaBfdSessPerfPktIn_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,1),_AlaBfdSessPerfPktIn_Type())
alaBfdSessPerfPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfPktIn.setStatus(_A)
_AlaBfdSessPerfPktOut_Type=Counter64
_AlaBfdSessPerfPktOut_Object=MibTableColumn
alaBfdSessPerfPktOut=_AlaBfdSessPerfPktOut_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,2),_AlaBfdSessPerfPktOut_Type())
alaBfdSessPerfPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfPktOut.setStatus(_A)
_AlaBfdSessPerfEchoOut_Type=Counter64
_AlaBfdSessPerfEchoOut_Object=MibTableColumn
alaBfdSessPerfEchoOut=_AlaBfdSessPerfEchoOut_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,3),_AlaBfdSessPerfEchoOut_Type())
alaBfdSessPerfEchoOut.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfEchoOut.setStatus(_A)
_AlaBfdSessPerfEchoIn_Type=Counter64
_AlaBfdSessPerfEchoIn_Object=MibTableColumn
alaBfdSessPerfEchoIn=_AlaBfdSessPerfEchoIn_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,4),_AlaBfdSessPerfEchoIn_Type())
alaBfdSessPerfEchoIn.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfEchoIn.setStatus(_A)
_AlaBfdSessPerfUpTime_Type=TimeTicks
_AlaBfdSessPerfUpTime_Object=MibTableColumn
alaBfdSessPerfUpTime=_AlaBfdSessPerfUpTime_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,5),_AlaBfdSessPerfUpTime_Type())
alaBfdSessPerfUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfUpTime.setStatus(_A)
_AlaBfdSessPerfLastSessDownTime_Type=TimeTicks
_AlaBfdSessPerfLastSessDownTime_Object=MibTableColumn
alaBfdSessPerfLastSessDownTime=_AlaBfdSessPerfLastSessDownTime_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,6),_AlaBfdSessPerfLastSessDownTime_Type())
alaBfdSessPerfLastSessDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfLastSessDownTime.setStatus(_A)
_AlaBfdSessPerfLastCommLostDiag_Type=AlaBfdDiag
_AlaBfdSessPerfLastCommLostDiag_Object=MibTableColumn
alaBfdSessPerfLastCommLostDiag=_AlaBfdSessPerfLastCommLostDiag_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,7),_AlaBfdSessPerfLastCommLostDiag_Type())
alaBfdSessPerfLastCommLostDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfLastCommLostDiag.setStatus(_A)
_AlaBfdSessPerfSessUpCount_Type=Counter64
_AlaBfdSessPerfSessUpCount_Object=MibTableColumn
alaBfdSessPerfSessUpCount=_AlaBfdSessPerfSessUpCount_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,8),_AlaBfdSessPerfSessUpCount_Type())
alaBfdSessPerfSessUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfSessUpCount.setStatus(_A)
_AlaBfdSessPerfDiscTime_Type=TimeTicks
_AlaBfdSessPerfDiscTime_Object=MibTableColumn
alaBfdSessPerfDiscTime=_AlaBfdSessPerfDiscTime_Object((1,3,6,1,4,1,6486,801,1,2,1,45,1,1,4,1,9),_AlaBfdSessPerfDiscTime_Type())
alaBfdSessPerfDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaBfdSessPerfDiscTime.setStatus(_A)
_AlcatelIND1BfdMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1BfdMIBConformance=_AlcatelIND1BfdMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,45,1,2))
if mibBuilder.loadTexts:alcatelIND1BfdMIBConformance.setStatus(_A)
_AlcatelIND1BfdMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1BfdMIBGroups=_AlcatelIND1BfdMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,1))
_AlcatelIND1BfdMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1BfdMIBCompliances=_AlcatelIND1BfdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,2))
alaBfdSessEntry.registerAugmentions((_B,_P))
alaBfdSessPerfEntry.setIndexNames(*alaBfdSessEntry.getIndexNames())
alaBfdBasicGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,1,1))
alaBfdBasicGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:alaBfdBasicGroup.setStatus(_A)
alaBfdIntfCfgGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,1,2))
alaBfdIntfCfgGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:alaBfdIntfCfgGroup.setStatus(_A)
alaBfdSessGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,1,3))
alaBfdSessGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:alaBfdSessGroup.setStatus(_A)
alaBfdSessPerfGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,1,4))
alaBfdSessPerfGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:alaBfdSessPerfGroup.setStatus(_A)
alcatelIND1BfdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,45,1,2,2,1))
alcatelIND1BfdMIBCompliance.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:alcatelIND1BfdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_I:AlaBfdInterval,'AlaBfdDiag':AlaBfdDiag,_J:AlaBfdStatus,'alcatelIND1BfdMIB':alcatelIND1BfdMIB,'alaBfdObjects':alaBfdObjects,'alaBfdGlobalObjects':alaBfdGlobalObjects,_Q:alaBfdGlobalVersionNumber,_R:alaBfdGlobalAdminStatus,_S:alaBfdGlobalTxInterval,_T:alaBfdGlobalRxInterval,_U:alaBfdGlobalDetectMult,_V:alaBfdGlobalEchoRxInterval,_W:alaBfdGlobalProtocolApps,'alaBfdIntfTable':alaBfdIntfTable,'alaBfdIntfEntry':alaBfdIntfEntry,_M:alaBfdIntfIndex,_Y:alaBfdIntfAddrType,_X:alaBfdIntfAddr,_Z:alaBfdIntfAdminStatus,_a:alaBfdIntfDesiredMinTxInterval,_b:alaBfdIntfReqMinRxInterval,_c:alaBfdIntfReqMinEchoRxInterval,_d:alaBfdIntfDetectMult,_e:alaBfdIntfAuthPresFlag,_f:alaBfdIntfAuthenticationType,_g:alaBfdIntfIfName,_h:alaBfdIntfOperStatus,_i:alaBfdIntfRowStatus,'alaBfdSessTable':alaBfdSessTable,'alaBfdSessEntry':alaBfdSessEntry,_O:alaBfdSessDiscriminator,_j:alaBfdSessNeighborAddrType,_k:alaBfdSessNeighborAddr,_l:alaBfdSessSessionType,_m:alaBfdSessRemoteDiscr,_n:alaBfdSessUdpPort,_o:alaBfdSessState,_p:alaBfdSessDiag,_q:alaBfdSessOperMode,_r:alaBfdSessControlPlanIndepFlag,_s:alaBfdSessIfIndex,_t:alaBfdSessNegotiatedTxInterval,_u:alaBfdSessNegotiatedRxInterval,_v:alaBfdSessEchoRxInterval,_w:alaBfdSessProtocolApps,'alaBfdSessPerfTable':alaBfdSessPerfTable,_P:alaBfdSessPerfEntry,_x:alaBfdSessPerfPktIn,_y:alaBfdSessPerfPktOut,_z:alaBfdSessPerfEchoOut,_A0:alaBfdSessPerfEchoIn,_A1:alaBfdSessPerfUpTime,_A2:alaBfdSessPerfLastSessDownTime,_A3:alaBfdSessPerfLastCommLostDiag,_A4:alaBfdSessPerfSessUpCount,_A5:alaBfdSessPerfDiscTime,'alcatelIND1BfdMIBConformance':alcatelIND1BfdMIBConformance,'alcatelIND1BfdMIBGroups':alcatelIND1BfdMIBGroups,_A6:alaBfdBasicGroup,_A7:alaBfdIntfCfgGroup,_A8:alaBfdSessGroup,_A9:alaBfdSessPerfGroup,'alcatelIND1BfdMIBCompliances':alcatelIND1BfdMIBCompliances,'alcatelIND1BfdMIBCompliance':alcatelIND1BfdMIBCompliance})