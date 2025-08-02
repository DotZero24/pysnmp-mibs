_S='eltIpBfdSessStateRemoteDiscr'
_R='eltIpBfdSessStateLocalAddr'
_Q='eltIpBfdSessStateLocalAddrType'
_P='eltIpBfdSessStatePeerAddr'
_O='eltIpBfdSessStatePeerAddrType'
_N='eltIpBfdSessStateIfIndex'
_M='eltIpBfdSessConfigLocalAddr'
_L='eltIpBfdSessConfigLocalAddrType'
_K='eltIpBfdSessConfigAddr'
_J='eltIpBfdSessConfigAddrType'
_I='eltIpBfdSessConfigIfIndex'
_H='EltIpBfdInterval'
_G='Unsigned32'
_F='read-write'
_E='InetAddress'
_D='read-only'
_C='not-accessible'
_B='ELTEX-MES-IP-BFD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','InterfaceIndexOrZero')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltMesIpBfd=ModuleIdentity((1,3,6,1,4,1,35265,1,23,6))
if mibBuilder.loadTexts:eltMesIpBfd.setRevisions(('2014-03-28 00:00',))
class EltIpBfdInterval(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,1000))
class EltIpBfdDiag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,16,255)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8),('misconnectivity',16),('noContact',255)))
class EltIpBfdState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminDown',1),('down',2),('init',3),('up',4)))
_EltIpBfdSessConfigTable_Object=MibTable
eltIpBfdSessConfigTable=_EltIpBfdSessConfigTable_Object((1,3,6,1,4,1,35265,1,23,6,3))
if mibBuilder.loadTexts:eltIpBfdSessConfigTable.setStatus(_A)
_EltIpBfdSessConfigEntry_Object=MibTableRow
eltIpBfdSessConfigEntry=_EltIpBfdSessConfigEntry_Object((1,3,6,1,4,1,35265,1,23,6,3,1))
eltIpBfdSessConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:eltIpBfdSessConfigEntry.setStatus(_A)
_EltIpBfdSessConfigIfIndex_Type=InterfaceIndexOrZero
_EltIpBfdSessConfigIfIndex_Object=MibTableColumn
eltIpBfdSessConfigIfIndex=_EltIpBfdSessConfigIfIndex_Object((1,3,6,1,4,1,35265,1,23,6,3,1,1),_EltIpBfdSessConfigIfIndex_Type())
eltIpBfdSessConfigIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessConfigIfIndex.setStatus(_A)
_EltIpBfdSessConfigAddrType_Type=InetAddressType
_EltIpBfdSessConfigAddrType_Object=MibTableColumn
eltIpBfdSessConfigAddrType=_EltIpBfdSessConfigAddrType_Object((1,3,6,1,4,1,35265,1,23,6,3,1,2),_EltIpBfdSessConfigAddrType_Type())
eltIpBfdSessConfigAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessConfigAddrType.setStatus(_A)
class _EltIpBfdSessConfigAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_EltIpBfdSessConfigAddr_Type.__name__=_E
_EltIpBfdSessConfigAddr_Object=MibTableColumn
eltIpBfdSessConfigAddr=_EltIpBfdSessConfigAddr_Object((1,3,6,1,4,1,35265,1,23,6,3,1,3),_EltIpBfdSessConfigAddr_Type())
eltIpBfdSessConfigAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessConfigAddr.setStatus(_A)
_EltIpBfdSessConfigLocalAddrType_Type=InetAddressType
_EltIpBfdSessConfigLocalAddrType_Object=MibTableColumn
eltIpBfdSessConfigLocalAddrType=_EltIpBfdSessConfigLocalAddrType_Object((1,3,6,1,4,1,35265,1,23,6,3,1,4),_EltIpBfdSessConfigLocalAddrType_Type())
eltIpBfdSessConfigLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessConfigLocalAddrType.setStatus(_A)
class _EltIpBfdSessConfigLocalAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_EltIpBfdSessConfigLocalAddr_Type.__name__=_E
_EltIpBfdSessConfigLocalAddr_Object=MibTableColumn
eltIpBfdSessConfigLocalAddr=_EltIpBfdSessConfigLocalAddr_Object((1,3,6,1,4,1,35265,1,23,6,3,1,5),_EltIpBfdSessConfigLocalAddr_Type())
eltIpBfdSessConfigLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessConfigLocalAddr.setStatus(_A)
_EltIpBfdSessConfigRowStatus_Type=RowStatus
_EltIpBfdSessConfigRowStatus_Object=MibTableColumn
eltIpBfdSessConfigRowStatus=_EltIpBfdSessConfigRowStatus_Object((1,3,6,1,4,1,35265,1,23,6,3,1,6),_EltIpBfdSessConfigRowStatus_Type())
eltIpBfdSessConfigRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:eltIpBfdSessConfigRowStatus.setStatus(_A)
class _EltIpBfdSessConfigDesiredMinTxIntvl_Type(EltIpBfdInterval):defaultValue=150
_EltIpBfdSessConfigDesiredMinTxIntvl_Type.__name__=_H
_EltIpBfdSessConfigDesiredMinTxIntvl_Object=MibTableColumn
eltIpBfdSessConfigDesiredMinTxIntvl=_EltIpBfdSessConfigDesiredMinTxIntvl_Object((1,3,6,1,4,1,35265,1,23,6,3,1,7),_EltIpBfdSessConfigDesiredMinTxIntvl_Type())
eltIpBfdSessConfigDesiredMinTxIntvl.setMaxAccess(_F)
if mibBuilder.loadTexts:eltIpBfdSessConfigDesiredMinTxIntvl.setStatus(_A)
class _EltIpBfdSessConfigReqMinRxInterval_Type(EltIpBfdInterval):defaultValue=150
_EltIpBfdSessConfigReqMinRxInterval_Type.__name__=_H
_EltIpBfdSessConfigReqMinRxInterval_Object=MibTableColumn
eltIpBfdSessConfigReqMinRxInterval=_EltIpBfdSessConfigReqMinRxInterval_Object((1,3,6,1,4,1,35265,1,23,6,3,1,8),_EltIpBfdSessConfigReqMinRxInterval_Type())
eltIpBfdSessConfigReqMinRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:eltIpBfdSessConfigReqMinRxInterval.setStatus(_A)
class _EltIpBfdSessConfigDetectMult_Type(Unsigned32):defaultValue=3
_EltIpBfdSessConfigDetectMult_Type.__name__=_G
_EltIpBfdSessConfigDetectMult_Object=MibTableColumn
eltIpBfdSessConfigDetectMult=_EltIpBfdSessConfigDetectMult_Object((1,3,6,1,4,1,35265,1,23,6,3,1,9),_EltIpBfdSessConfigDetectMult_Type())
eltIpBfdSessConfigDetectMult.setMaxAccess(_F)
if mibBuilder.loadTexts:eltIpBfdSessConfigDetectMult.setStatus(_A)
_EltIpBfdSessStateTable_Object=MibTable
eltIpBfdSessStateTable=_EltIpBfdSessStateTable_Object((1,3,6,1,4,1,35265,1,23,6,4))
if mibBuilder.loadTexts:eltIpBfdSessStateTable.setStatus(_A)
_EltIpBfdSessStateEntry_Object=MibTableRow
eltIpBfdSessStateEntry=_EltIpBfdSessStateEntry_Object((1,3,6,1,4,1,35265,1,23,6,4,1))
eltIpBfdSessStateEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:eltIpBfdSessStateEntry.setStatus(_A)
_EltIpBfdSessStateIfIndex_Type=InterfaceIndexOrZero
_EltIpBfdSessStateIfIndex_Object=MibTableColumn
eltIpBfdSessStateIfIndex=_EltIpBfdSessStateIfIndex_Object((1,3,6,1,4,1,35265,1,23,6,4,1,1),_EltIpBfdSessStateIfIndex_Type())
eltIpBfdSessStateIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessStateIfIndex.setStatus(_A)
_EltIpBfdSessStatePeerAddrType_Type=InetAddressType
_EltIpBfdSessStatePeerAddrType_Object=MibTableColumn
eltIpBfdSessStatePeerAddrType=_EltIpBfdSessStatePeerAddrType_Object((1,3,6,1,4,1,35265,1,23,6,4,1,2),_EltIpBfdSessStatePeerAddrType_Type())
eltIpBfdSessStatePeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessStatePeerAddrType.setStatus(_A)
_EltIpBfdSessStatePeerAddr_Type=InetAddress
_EltIpBfdSessStatePeerAddr_Object=MibTableColumn
eltIpBfdSessStatePeerAddr=_EltIpBfdSessStatePeerAddr_Object((1,3,6,1,4,1,35265,1,23,6,4,1,3),_EltIpBfdSessStatePeerAddr_Type())
eltIpBfdSessStatePeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessStatePeerAddr.setStatus(_A)
_EltIpBfdSessStateLocalAddrType_Type=InetAddressType
_EltIpBfdSessStateLocalAddrType_Object=MibTableColumn
eltIpBfdSessStateLocalAddrType=_EltIpBfdSessStateLocalAddrType_Object((1,3,6,1,4,1,35265,1,23,6,4,1,4),_EltIpBfdSessStateLocalAddrType_Type())
eltIpBfdSessStateLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessStateLocalAddrType.setStatus(_A)
class _EltIpBfdSessStateLocalAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_EltIpBfdSessStateLocalAddr_Type.__name__=_E
_EltIpBfdSessStateLocalAddr_Object=MibTableColumn
eltIpBfdSessStateLocalAddr=_EltIpBfdSessStateLocalAddr_Object((1,3,6,1,4,1,35265,1,23,6,4,1,5),_EltIpBfdSessStateLocalAddr_Type())
eltIpBfdSessStateLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessStateLocalAddr.setStatus(_A)
class _EltIpBfdSessStateRemoteDiscr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EltIpBfdSessStateRemoteDiscr_Type.__name__=_G
_EltIpBfdSessStateRemoteDiscr_Object=MibTableColumn
eltIpBfdSessStateRemoteDiscr=_EltIpBfdSessStateRemoteDiscr_Object((1,3,6,1,4,1,35265,1,23,6,4,1,6),_EltIpBfdSessStateRemoteDiscr_Type())
eltIpBfdSessStateRemoteDiscr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIpBfdSessStateRemoteDiscr.setStatus(_A)
_EltIpBfdSessStateState_Type=EltIpBfdState
_EltIpBfdSessStateState_Object=MibTableColumn
eltIpBfdSessStateState=_EltIpBfdSessStateState_Object((1,3,6,1,4,1,35265,1,23,6,4,1,7),_EltIpBfdSessStateState_Type())
eltIpBfdSessStateState.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateState.setStatus(_A)
_EltIpBfdSessStateDiag_Type=EltIpBfdDiag
_EltIpBfdSessStateDiag_Object=MibTableColumn
eltIpBfdSessStateDiag=_EltIpBfdSessStateDiag_Object((1,3,6,1,4,1,35265,1,23,6,4,1,8),_EltIpBfdSessStateDiag_Type())
eltIpBfdSessStateDiag.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateDiag.setStatus(_A)
_EltIpBfdSessStateOperIfIndex_Type=InterfaceIndexOrZero
_EltIpBfdSessStateOperIfIndex_Object=MibTableColumn
eltIpBfdSessStateOperIfIndex=_EltIpBfdSessStateOperIfIndex_Object((1,3,6,1,4,1,35265,1,23,6,4,1,9),_EltIpBfdSessStateOperIfIndex_Type())
eltIpBfdSessStateOperIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateOperIfIndex.setStatus(_A)
_EltIpBfdSessStateOperPeerAddrType_Type=InetAddressType
_EltIpBfdSessStateOperPeerAddrType_Object=MibTableColumn
eltIpBfdSessStateOperPeerAddrType=_EltIpBfdSessStateOperPeerAddrType_Object((1,3,6,1,4,1,35265,1,23,6,4,1,10),_EltIpBfdSessStateOperPeerAddrType_Type())
eltIpBfdSessStateOperPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateOperPeerAddrType.setStatus(_A)
_EltIpBfdSessStateOperPeerAddr_Type=InetAddress
_EltIpBfdSessStateOperPeerAddr_Object=MibTableColumn
eltIpBfdSessStateOperPeerAddr=_EltIpBfdSessStateOperPeerAddr_Object((1,3,6,1,4,1,35265,1,23,6,4,1,11),_EltIpBfdSessStateOperPeerAddr_Type())
eltIpBfdSessStateOperPeerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateOperPeerAddr.setStatus(_A)
_EltIpBfdSessStateOperLocalAddrType_Type=InetAddressType
_EltIpBfdSessStateOperLocalAddrType_Object=MibTableColumn
eltIpBfdSessStateOperLocalAddrType=_EltIpBfdSessStateOperLocalAddrType_Object((1,3,6,1,4,1,35265,1,23,6,4,1,12),_EltIpBfdSessStateOperLocalAddrType_Type())
eltIpBfdSessStateOperLocalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateOperLocalAddrType.setStatus(_A)
_EltIpBfdSessStateOperLocalAddr_Type=InetAddress
_EltIpBfdSessStateOperLocalAddr_Object=MibTableColumn
eltIpBfdSessStateOperLocalAddr=_EltIpBfdSessStateOperLocalAddr_Object((1,3,6,1,4,1,35265,1,23,6,4,1,13),_EltIpBfdSessStateOperLocalAddr_Type())
eltIpBfdSessStateOperLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateOperLocalAddr.setStatus(_A)
_EltIpBfdSessStateOperRemoteDiscr_Type=Unsigned32
_EltIpBfdSessStateOperRemoteDiscr_Object=MibTableColumn
eltIpBfdSessStateOperRemoteDiscr=_EltIpBfdSessStateOperRemoteDiscr_Object((1,3,6,1,4,1,35265,1,23,6,4,1,14),_EltIpBfdSessStateOperRemoteDiscr_Type())
eltIpBfdSessStateOperRemoteDiscr.setMaxAccess(_D)
if mibBuilder.loadTexts:eltIpBfdSessStateOperRemoteDiscr.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:EltIpBfdInterval,'EltIpBfdDiag':EltIpBfdDiag,'EltIpBfdState':EltIpBfdState,'eltMesIpBfd':eltMesIpBfd,'eltIpBfdSessConfigTable':eltIpBfdSessConfigTable,'eltIpBfdSessConfigEntry':eltIpBfdSessConfigEntry,_I:eltIpBfdSessConfigIfIndex,_J:eltIpBfdSessConfigAddrType,_K:eltIpBfdSessConfigAddr,_L:eltIpBfdSessConfigLocalAddrType,_M:eltIpBfdSessConfigLocalAddr,'eltIpBfdSessConfigRowStatus':eltIpBfdSessConfigRowStatus,'eltIpBfdSessConfigDesiredMinTxIntvl':eltIpBfdSessConfigDesiredMinTxIntvl,'eltIpBfdSessConfigReqMinRxInterval':eltIpBfdSessConfigReqMinRxInterval,'eltIpBfdSessConfigDetectMult':eltIpBfdSessConfigDetectMult,'eltIpBfdSessStateTable':eltIpBfdSessStateTable,'eltIpBfdSessStateEntry':eltIpBfdSessStateEntry,_N:eltIpBfdSessStateIfIndex,_O:eltIpBfdSessStatePeerAddrType,_P:eltIpBfdSessStatePeerAddr,_Q:eltIpBfdSessStateLocalAddrType,_R:eltIpBfdSessStateLocalAddr,_S:eltIpBfdSessStateRemoteDiscr,'eltIpBfdSessStateState':eltIpBfdSessStateState,'eltIpBfdSessStateDiag':eltIpBfdSessStateDiag,'eltIpBfdSessStateOperIfIndex':eltIpBfdSessStateOperIfIndex,'eltIpBfdSessStateOperPeerAddrType':eltIpBfdSessStateOperPeerAddrType,'eltIpBfdSessStateOperPeerAddr':eltIpBfdSessStateOperPeerAddr,'eltIpBfdSessStateOperLocalAddrType':eltIpBfdSessStateOperLocalAddrType,'eltIpBfdSessStateOperLocalAddr':eltIpBfdSessStateOperLocalAddr,'eltIpBfdSessStateOperRemoteDiscr':eltIpBfdSessStateOperRemoteDiscr})