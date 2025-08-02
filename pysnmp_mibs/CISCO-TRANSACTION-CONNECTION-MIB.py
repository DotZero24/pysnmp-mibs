_A6='ciscoTransConnTransactionGroup'
_A5='ciscoTransConnConnectionGroup'
_A4='ciscoTransConnServerGroup'
_A3='ciscoTransConnRouteGroup'
_A2='ciscoTransConnDestinationGroup'
_A1='ciscoTransConnLicenseGroup'
_A0='ctcTransactionUserId'
_z='ctcTransactionTPName'
_y='ctcTransactionState'
_x='ctcTransactionConnectionId'
_w='ctcTransactionServer'
_v='ctcTransactionSessionId'
_u='ctcConnectionTotalBytesRecvd'
_t='ctcConnectionIdleTime'
_s='ctcConnectionConnectTime'
_r='ctcConnectionTotalConversations'
_q='ctcConnectionClientPort'
_p='ctcConnectionClientIPAddr'
_o='ctcConnectionSessionCount'
_n='ctcConnectionState'
_m='ctcConnectionServer'
_l='ctcConnectionId'
_k='ctcServerProgNameUpperCase'
_j='ctcServerConnectionCount'
_i='ctcServerWindowSize'
_h='ctcServerHostTimeout'
_g='ctcServerClientTimeout'
_f='ctcServerDestinationName'
_e='ctcServerPort'
_d='ctcServerIPAddr'
_c='ctcServerListening'
_b='ctcServerName'
_a='ctcRouteDestinationName'
_Z='ctcRouteTransactionID'
_Y='ctcRouteOwningServer'
_X='ctcDestinationNumHits'
_W='ctcDestinationModeName'
_V='ctcDestinationRemoteLUName'
_U='ctcLicenseExpiration'
_T='ctcLicenseCurrConn'
_S='ctcLicenseMaxConn'
_R='ctcLicenseKey'
_Q='ctcLicenseState'
_P='receiving'
_O='closing'
_N='minutes'
_M='TruthValue'
_L='IpAddress'
_K='ctcServerIndex'
_J='ctcDestinationName'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-only'
_B='CISCO-TRANSACTION-CONNECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeInterval',_M)
ciscoTransactionConnectionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,144))
if mibBuilder.loadTexts:ciscoTransactionConnectionMIB.setRevisions(('2005-12-22 00:00','1999-08-19 00:00'))
_CiscoTransConnMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTransConnMIBObjects=_CiscoTransConnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,144,1))
_CtcLicense_ObjectIdentity=ObjectIdentity
ctcLicense=_CtcLicense_ObjectIdentity((1,3,6,1,4,1,9,9,144,1,1))
if mibBuilder.loadTexts:ctcLicense.setStatus(_A)
class _CtcLicenseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unconfigured',1),('notValidatedYet',2),('badKey',3),('licenseOK',4),('expired',5)))
_CtcLicenseState_Type.__name__=_I
_CtcLicenseState_Object=MibScalar
ctcLicenseState=_CtcLicenseState_Object((1,3,6,1,4,1,9,9,144,1,1,1),_CtcLicenseState_Type())
ctcLicenseState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcLicenseState.setStatus(_A)
class _CtcLicenseKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CtcLicenseKey_Type.__name__=_F
_CtcLicenseKey_Object=MibScalar
ctcLicenseKey=_CtcLicenseKey_Object((1,3,6,1,4,1,9,9,144,1,1,2),_CtcLicenseKey_Type())
ctcLicenseKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcLicenseKey.setStatus(_A)
_CtcLicenseMaxConn_Type=Unsigned32
_CtcLicenseMaxConn_Object=MibScalar
ctcLicenseMaxConn=_CtcLicenseMaxConn_Object((1,3,6,1,4,1,9,9,144,1,1,3),_CtcLicenseMaxConn_Type())
ctcLicenseMaxConn.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcLicenseMaxConn.setStatus(_A)
_CtcLicenseCurrConn_Type=Unsigned32
_CtcLicenseCurrConn_Object=MibScalar
ctcLicenseCurrConn=_CtcLicenseCurrConn_Object((1,3,6,1,4,1,9,9,144,1,1,4),_CtcLicenseCurrConn_Type())
ctcLicenseCurrConn.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcLicenseCurrConn.setStatus(_A)
_CtcLicenseExpiration_Type=DateAndTime
_CtcLicenseExpiration_Object=MibScalar
ctcLicenseExpiration=_CtcLicenseExpiration_Object((1,3,6,1,4,1,9,9,144,1,1,5),_CtcLicenseExpiration_Type())
ctcLicenseExpiration.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcLicenseExpiration.setStatus(_A)
_CtcDestinationTable_Object=MibTable
ctcDestinationTable=_CtcDestinationTable_Object((1,3,6,1,4,1,9,9,144,1,2))
if mibBuilder.loadTexts:ctcDestinationTable.setStatus(_A)
_CtcDestinationEntry_Object=MibTableRow
ctcDestinationEntry=_CtcDestinationEntry_Object((1,3,6,1,4,1,9,9,144,1,2,1))
ctcDestinationEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ctcDestinationEntry.setStatus(_A)
class _CtcDestinationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtcDestinationName_Type.__name__=_D
_CtcDestinationName_Object=MibTableColumn
ctcDestinationName=_CtcDestinationName_Object((1,3,6,1,4,1,9,9,144,1,2,1,1),_CtcDestinationName_Type())
ctcDestinationName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcDestinationName.setStatus(_A)
class _CtcDestinationRemoteLUName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CtcDestinationRemoteLUName_Type.__name__=_D
_CtcDestinationRemoteLUName_Object=MibTableColumn
ctcDestinationRemoteLUName=_CtcDestinationRemoteLUName_Object((1,3,6,1,4,1,9,9,144,1,2,1,2),_CtcDestinationRemoteLUName_Type())
ctcDestinationRemoteLUName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcDestinationRemoteLUName.setStatus(_A)
class _CtcDestinationModeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CtcDestinationModeName_Type.__name__=_D
_CtcDestinationModeName_Object=MibTableColumn
ctcDestinationModeName=_CtcDestinationModeName_Object((1,3,6,1,4,1,9,9,144,1,2,1,3),_CtcDestinationModeName_Type())
ctcDestinationModeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcDestinationModeName.setStatus(_A)
_CtcDestinationNumHits_Type=Unsigned32
_CtcDestinationNumHits_Object=MibTableColumn
ctcDestinationNumHits=_CtcDestinationNumHits_Object((1,3,6,1,4,1,9,9,144,1,2,1,4),_CtcDestinationNumHits_Type())
ctcDestinationNumHits.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcDestinationNumHits.setStatus(_A)
_CtcRouteTable_Object=MibTable
ctcRouteTable=_CtcRouteTable_Object((1,3,6,1,4,1,9,9,144,1,3))
if mibBuilder.loadTexts:ctcRouteTable.setStatus(_A)
_CtcRouteEntry_Object=MibTableRow
ctcRouteEntry=_CtcRouteEntry_Object((1,3,6,1,4,1,9,9,144,1,3,1))
ctcRouteEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ctcRouteEntry.setStatus(_A)
_CtcRouteOwningServer_Type=Unsigned32
_CtcRouteOwningServer_Object=MibTableColumn
ctcRouteOwningServer=_CtcRouteOwningServer_Object((1,3,6,1,4,1,9,9,144,1,3,1,1),_CtcRouteOwningServer_Type())
ctcRouteOwningServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcRouteOwningServer.setStatus(_A)
class _CtcRouteTransactionID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtcRouteTransactionID_Type.__name__=_D
_CtcRouteTransactionID_Object=MibTableColumn
ctcRouteTransactionID=_CtcRouteTransactionID_Object((1,3,6,1,4,1,9,9,144,1,3,1,2),_CtcRouteTransactionID_Type())
ctcRouteTransactionID.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcRouteTransactionID.setStatus(_A)
class _CtcRouteDestinationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtcRouteDestinationName_Type.__name__=_D
_CtcRouteDestinationName_Object=MibTableColumn
ctcRouteDestinationName=_CtcRouteDestinationName_Object((1,3,6,1,4,1,9,9,144,1,3,1,3),_CtcRouteDestinationName_Type())
ctcRouteDestinationName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcRouteDestinationName.setStatus(_A)
_CtcServerTable_Object=MibTable
ctcServerTable=_CtcServerTable_Object((1,3,6,1,4,1,9,9,144,1,4))
if mibBuilder.loadTexts:ctcServerTable.setStatus(_A)
_CtcServerEntry_Object=MibTableRow
ctcServerEntry=_CtcServerEntry_Object((1,3,6,1,4,1,9,9,144,1,4,1))
ctcServerEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ctcServerEntry.setStatus(_A)
_CtcServerIndex_Type=Unsigned32
_CtcServerIndex_Object=MibTableColumn
ctcServerIndex=_CtcServerIndex_Object((1,3,6,1,4,1,9,9,144,1,4,1,1),_CtcServerIndex_Type())
ctcServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerIndex.setStatus(_A)
class _CtcServerName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtcServerName_Type.__name__=_D
_CtcServerName_Object=MibTableColumn
ctcServerName=_CtcServerName_Object((1,3,6,1,4,1,9,9,144,1,4,1,2),_CtcServerName_Type())
ctcServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerName.setStatus(_A)
_CtcServerListening_Type=TruthValue
_CtcServerListening_Object=MibTableColumn
ctcServerListening=_CtcServerListening_Object((1,3,6,1,4,1,9,9,144,1,4,1,3),_CtcServerListening_Type())
ctcServerListening.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerListening.setStatus(_A)
class _CtcServerIPAddr_Type(IpAddress):defaultHexValue='00000000'
_CtcServerIPAddr_Type.__name__=_L
_CtcServerIPAddr_Object=MibTableColumn
ctcServerIPAddr=_CtcServerIPAddr_Object((1,3,6,1,4,1,9,9,144,1,4,1,4),_CtcServerIPAddr_Type())
ctcServerIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerIPAddr.setStatus(_A)
class _CtcServerPort_Type(Unsigned32):defaultValue=1435;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtcServerPort_Type.__name__=_E
_CtcServerPort_Object=MibTableColumn
ctcServerPort=_CtcServerPort_Object((1,3,6,1,4,1,9,9,144,1,4,1,5),_CtcServerPort_Type())
ctcServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerPort.setStatus(_A)
class _CtcServerDestinationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtcServerDestinationName_Type.__name__=_D
_CtcServerDestinationName_Object=MibTableColumn
ctcServerDestinationName=_CtcServerDestinationName_Object((1,3,6,1,4,1,9,9,144,1,4,1,6),_CtcServerDestinationName_Type())
ctcServerDestinationName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerDestinationName.setStatus(_A)
class _CtcServerClientTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CtcServerClientTimeout_Type.__name__=_E
_CtcServerClientTimeout_Object=MibTableColumn
ctcServerClientTimeout=_CtcServerClientTimeout_Object((1,3,6,1,4,1,9,9,144,1,4,1,7),_CtcServerClientTimeout_Type())
ctcServerClientTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerClientTimeout.setStatus(_A)
if mibBuilder.loadTexts:ctcServerClientTimeout.setUnits(_N)
class _CtcServerHostTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CtcServerHostTimeout_Type.__name__=_E
_CtcServerHostTimeout_Object=MibTableColumn
ctcServerHostTimeout=_CtcServerHostTimeout_Object((1,3,6,1,4,1,9,9,144,1,4,1,8),_CtcServerHostTimeout_Type())
ctcServerHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerHostTimeout.setStatus(_A)
if mibBuilder.loadTexts:ctcServerHostTimeout.setUnits(_N)
class _CtcServerWindowSize_Type(Unsigned32):defaultValue=4096
_CtcServerWindowSize_Type.__name__=_E
_CtcServerWindowSize_Object=MibTableColumn
ctcServerWindowSize=_CtcServerWindowSize_Object((1,3,6,1,4,1,9,9,144,1,4,1,9),_CtcServerWindowSize_Type())
ctcServerWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerWindowSize.setStatus(_A)
if mibBuilder.loadTexts:ctcServerWindowSize.setUnits('bytes')
_CtcServerConnectionCount_Type=Unsigned32
_CtcServerConnectionCount_Object=MibTableColumn
ctcServerConnectionCount=_CtcServerConnectionCount_Object((1,3,6,1,4,1,9,9,144,1,4,1,10),_CtcServerConnectionCount_Type())
ctcServerConnectionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerConnectionCount.setStatus(_A)
class _CtcServerProgNameUpperCase_Type(TruthValue):defaultValue=1
_CtcServerProgNameUpperCase_Type.__name__=_M
_CtcServerProgNameUpperCase_Object=MibTableColumn
ctcServerProgNameUpperCase=_CtcServerProgNameUpperCase_Object((1,3,6,1,4,1,9,9,144,1,4,1,11),_CtcServerProgNameUpperCase_Type())
ctcServerProgNameUpperCase.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcServerProgNameUpperCase.setStatus(_A)
_CtcConnectionTable_Object=MibTable
ctcConnectionTable=_CtcConnectionTable_Object((1,3,6,1,4,1,9,9,144,1,5))
if mibBuilder.loadTexts:ctcConnectionTable.setStatus(_A)
_CtcConnectionEntry_Object=MibTableRow
ctcConnectionEntry=_CtcConnectionEntry_Object((1,3,6,1,4,1,9,9,144,1,5,1))
ctcConnectionEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ctcConnectionEntry.setStatus(_A)
class _CtcConnectionId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CtcConnectionId_Type.__name__=_F
_CtcConnectionId_Object=MibTableColumn
ctcConnectionId=_CtcConnectionId_Object((1,3,6,1,4,1,9,9,144,1,5,1,1),_CtcConnectionId_Type())
ctcConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionId.setStatus(_A)
_CtcConnectionServer_Type=Unsigned32
_CtcConnectionServer_Object=MibTableColumn
ctcConnectionServer=_CtcConnectionServer_Object((1,3,6,1,4,1,9,9,144,1,5,1,2),_CtcConnectionServer_Type())
ctcConnectionServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionServer.setStatus(_A)
class _CtcConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('reset',1),(_O,2),('halt',3),(_P,4)))
_CtcConnectionState_Type.__name__=_I
_CtcConnectionState_Object=MibTableColumn
ctcConnectionState=_CtcConnectionState_Object((1,3,6,1,4,1,9,9,144,1,5,1,3),_CtcConnectionState_Type())
ctcConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionState.setStatus(_A)
_CtcConnectionSessionCount_Type=Unsigned32
_CtcConnectionSessionCount_Object=MibTableColumn
ctcConnectionSessionCount=_CtcConnectionSessionCount_Object((1,3,6,1,4,1,9,9,144,1,5,1,4),_CtcConnectionSessionCount_Type())
ctcConnectionSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionSessionCount.setStatus(_A)
_CtcConnectionClientIPAddr_Type=IpAddress
_CtcConnectionClientIPAddr_Object=MibTableColumn
ctcConnectionClientIPAddr=_CtcConnectionClientIPAddr_Object((1,3,6,1,4,1,9,9,144,1,5,1,5),_CtcConnectionClientIPAddr_Type())
ctcConnectionClientIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionClientIPAddr.setStatus(_A)
class _CtcConnectionClientPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtcConnectionClientPort_Type.__name__=_E
_CtcConnectionClientPort_Object=MibTableColumn
ctcConnectionClientPort=_CtcConnectionClientPort_Object((1,3,6,1,4,1,9,9,144,1,5,1,6),_CtcConnectionClientPort_Type())
ctcConnectionClientPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionClientPort.setStatus(_A)
_CtcConnectionTotalConversations_Type=Unsigned32
_CtcConnectionTotalConversations_Object=MibTableColumn
ctcConnectionTotalConversations=_CtcConnectionTotalConversations_Object((1,3,6,1,4,1,9,9,144,1,5,1,7),_CtcConnectionTotalConversations_Type())
ctcConnectionTotalConversations.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionTotalConversations.setStatus(_A)
_CtcConnectionConnectTime_Type=DateAndTime
_CtcConnectionConnectTime_Object=MibTableColumn
ctcConnectionConnectTime=_CtcConnectionConnectTime_Object((1,3,6,1,4,1,9,9,144,1,5,1,8),_CtcConnectionConnectTime_Type())
ctcConnectionConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionConnectTime.setStatus(_A)
_CtcConnectionIdleTime_Type=TimeInterval
_CtcConnectionIdleTime_Object=MibTableColumn
ctcConnectionIdleTime=_CtcConnectionIdleTime_Object((1,3,6,1,4,1,9,9,144,1,5,1,9),_CtcConnectionIdleTime_Type())
ctcConnectionIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionIdleTime.setStatus(_A)
_CtcConnectionTotalBytesRecvd_Type=Unsigned32
_CtcConnectionTotalBytesRecvd_Object=MibTableColumn
ctcConnectionTotalBytesRecvd=_CtcConnectionTotalBytesRecvd_Object((1,3,6,1,4,1,9,9,144,1,5,1,10),_CtcConnectionTotalBytesRecvd_Type())
ctcConnectionTotalBytesRecvd.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcConnectionTotalBytesRecvd.setStatus(_A)
_CtcTransactionTable_Object=MibTable
ctcTransactionTable=_CtcTransactionTable_Object((1,3,6,1,4,1,9,9,144,1,6))
if mibBuilder.loadTexts:ctcTransactionTable.setStatus(_A)
_CtcTransactionEntry_Object=MibTableRow
ctcTransactionEntry=_CtcTransactionEntry_Object((1,3,6,1,4,1,9,9,144,1,6,1))
ctcTransactionEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ctcTransactionEntry.setStatus(_A)
class _CtcTransactionSessionId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CtcTransactionSessionId_Type.__name__=_F
_CtcTransactionSessionId_Object=MibTableColumn
ctcTransactionSessionId=_CtcTransactionSessionId_Object((1,3,6,1,4,1,9,9,144,1,6,1,1),_CtcTransactionSessionId_Type())
ctcTransactionSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcTransactionSessionId.setStatus(_A)
_CtcTransactionServer_Type=Unsigned32
_CtcTransactionServer_Object=MibTableColumn
ctcTransactionServer=_CtcTransactionServer_Object((1,3,6,1,4,1,9,9,144,1,6,1,2),_CtcTransactionServer_Type())
ctcTransactionServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcTransactionServer.setStatus(_A)
class _CtcTransactionConnectionId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CtcTransactionConnectionId_Type.__name__=_F
_CtcTransactionConnectionId_Object=MibTableColumn
ctcTransactionConnectionId=_CtcTransactionConnectionId_Object((1,3,6,1,4,1,9,9,144,1,6,1,3),_CtcTransactionConnectionId_Type())
ctcTransactionConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcTransactionConnectionId.setStatus(_A)
class _CtcTransactionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reset',1),('opening',2),('sending',3),(_P,4),('exception',5),('exceptionresponse',6),(_O,7)))
_CtcTransactionState_Type.__name__=_I
_CtcTransactionState_Object=MibTableColumn
ctcTransactionState=_CtcTransactionState_Object((1,3,6,1,4,1,9,9,144,1,6,1,4),_CtcTransactionState_Type())
ctcTransactionState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcTransactionState.setStatus(_A)
class _CtcTransactionTPName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CtcTransactionTPName_Type.__name__=_D
_CtcTransactionTPName_Object=MibTableColumn
ctcTransactionTPName=_CtcTransactionTPName_Object((1,3,6,1,4,1,9,9,144,1,6,1,5),_CtcTransactionTPName_Type())
ctcTransactionTPName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcTransactionTPName.setStatus(_A)
class _CtcTransactionUserId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CtcTransactionUserId_Type.__name__=_D
_CtcTransactionUserId_Object=MibTableColumn
ctcTransactionUserId=_CtcTransactionUserId_Object((1,3,6,1,4,1,9,9,144,1,6,1,6),_CtcTransactionUserId_Type())
ctcTransactionUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcTransactionUserId.setStatus(_A)
_CiscoTransConnMIBConformance_ObjectIdentity=ObjectIdentity
ciscoTransConnMIBConformance=_CiscoTransConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,144,3))
_CiscoTransConnMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTransConnMIBCompliances=_CiscoTransConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,144,3,1))
_CiscoTransConnMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTransConnMIBGroups=_CiscoTransConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,144,3,2))
ciscoTransConnLicenseGroup=ObjectGroup((1,3,6,1,4,1,9,9,144,3,2,1))
ciscoTransConnLicenseGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoTransConnLicenseGroup.setStatus(_A)
ciscoTransConnDestinationGroup=ObjectGroup((1,3,6,1,4,1,9,9,144,3,2,2))
ciscoTransConnDestinationGroup.setObjects(*((_B,_J),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoTransConnDestinationGroup.setStatus(_A)
ciscoTransConnRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,144,3,2,3))
ciscoTransConnRouteGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoTransConnRouteGroup.setStatus(_A)
ciscoTransConnServerGroup=ObjectGroup((1,3,6,1,4,1,9,9,144,3,2,4))
ciscoTransConnServerGroup.setObjects(*((_B,_K),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoTransConnServerGroup.setStatus(_A)
ciscoTransConnConnectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,144,3,2,5))
ciscoTransConnConnectionGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoTransConnConnectionGroup.setStatus(_A)
ciscoTransConnTransactionGroup=ObjectGroup((1,3,6,1,4,1,9,9,144,3,2,6))
ciscoTransConnTransactionGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ciscoTransConnTransactionGroup.setStatus(_A)
ciscoTransConnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,144,3,1,1))
ciscoTransConnMIBCompliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoTransConnMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoTransactionConnectionMIB':ciscoTransactionConnectionMIB,'ciscoTransConnMIBObjects':ciscoTransConnMIBObjects,'ctcLicense':ctcLicense,_Q:ctcLicenseState,_R:ctcLicenseKey,_S:ctcLicenseMaxConn,_T:ctcLicenseCurrConn,_U:ctcLicenseExpiration,'ctcDestinationTable':ctcDestinationTable,'ctcDestinationEntry':ctcDestinationEntry,_J:ctcDestinationName,_V:ctcDestinationRemoteLUName,_W:ctcDestinationModeName,_X:ctcDestinationNumHits,'ctcRouteTable':ctcRouteTable,'ctcRouteEntry':ctcRouteEntry,_Y:ctcRouteOwningServer,_Z:ctcRouteTransactionID,_a:ctcRouteDestinationName,'ctcServerTable':ctcServerTable,'ctcServerEntry':ctcServerEntry,_K:ctcServerIndex,_b:ctcServerName,_c:ctcServerListening,_d:ctcServerIPAddr,_e:ctcServerPort,_f:ctcServerDestinationName,_g:ctcServerClientTimeout,_h:ctcServerHostTimeout,_i:ctcServerWindowSize,_j:ctcServerConnectionCount,_k:ctcServerProgNameUpperCase,'ctcConnectionTable':ctcConnectionTable,'ctcConnectionEntry':ctcConnectionEntry,_l:ctcConnectionId,_m:ctcConnectionServer,_n:ctcConnectionState,_o:ctcConnectionSessionCount,_p:ctcConnectionClientIPAddr,_q:ctcConnectionClientPort,_r:ctcConnectionTotalConversations,_s:ctcConnectionConnectTime,_t:ctcConnectionIdleTime,_u:ctcConnectionTotalBytesRecvd,'ctcTransactionTable':ctcTransactionTable,'ctcTransactionEntry':ctcTransactionEntry,_v:ctcTransactionSessionId,_w:ctcTransactionServer,_x:ctcTransactionConnectionId,_y:ctcTransactionState,_z:ctcTransactionTPName,_A0:ctcTransactionUserId,'ciscoTransConnMIBConformance':ciscoTransConnMIBConformance,'ciscoTransConnMIBCompliances':ciscoTransConnMIBCompliances,'ciscoTransConnMIBCompliance':ciscoTransConnMIBCompliance,'ciscoTransConnMIBGroups':ciscoTransConnMIBGroups,_A1:ciscoTransConnLicenseGroup,_A2:ciscoTransConnDestinationGroup,_A3:ciscoTransConnRouteGroup,_A4:ciscoTransConnServerGroup,_A5:ciscoTransConnConnectionGroup,_A6:ciscoTransConnTransactionGroup})