_A1='rpkiRtrCacheServerErrorsGroup'
_A0='rpkiRtrNotificationsGroup'
_z='rpkiRtrPrefixOriginGroup'
_y='rpkiRtrCacheServerGroup'
_x='rpkiRtrCacheServerConnectionToGoStale'
_w='rpkiRtrCacheServerConnectionStateChange'
_v='rpkiRtrCacheServerErrorsDuplicateAnnounce'
_u='rpkiRtrCacheServerErrorsWithdrawalUnknown'
_t='rpkiRtrCacheServerErrorsUnsupportedPdu'
_s='rpkiRtrCacheServerErrorsUnsupportedVersion'
_r='rpkiRtrCacheServerErrorsInvalidRequest'
_q='rpkiRtrCacheServerErrorsNoData'
_p='rpkiRtrCacheServerErrorsInternalError'
_o='rpkiRtrCacheServerErrorsCorruptData'
_n='rpkiRtrCacheServerId'
_m='rpkiRtrCacheServerV6Withdrawals'
_l='rpkiRtrCacheServerV6Announcements'
_k='rpkiRtrCacheServerV4Withdrawals'
_j='rpkiRtrCacheServerV4Announcements'
_i='rpkiRtrCacheServerMsgsSent'
_h='rpkiRtrCacheServerMsgsReceived'
_g='rpkiRtrCacheServerDescription'
_f='rpkiRtrCacheServerConnectionType'
_e='rpkiRtrCacheServerPreference'
_d='rpkiRtrCacheServerLocalPort'
_c='rpkiRtrCacheServerLocalAddress'
_b='rpkiRtrCacheServerLocalAddressType'
_a='rpkiRtrDiscontinuityTimer'
_Z='rpkiRtrCacheServerErrorsTableEntry'
_Y='rpkiRtrPrefixOriginASN'
_X='rpkiRtrPrefixOriginMaxLength'
_W='rpkiRtrPrefixOriginMinLength'
_V='rpkiRtrPrefixOriginAddress'
_U='rpkiRtrPrefixOriginAddressType'
_T='seconds'
_S='rpkiRtrCacheServerRemotePort'
_R='rpkiRtrCacheServerRemoteAddress'
_Q='rpkiRtrCacheServerRemoteAddressType'
_P='Integer32'
_O='InetAutonomousSystemNumber'
_N='rpkiRtrCacheServerTimeToRefresh'
_M='rpkiRtrCacheServerRefreshTimer'
_L='rpkiRtrCacheServerV6ActiveRecords'
_K='rpkiRtrCacheServerV4ActiveRecords'
_J='rpkiRtrCacheServerConnectionStatus'
_I='rpkiRtrPrefixOriginCacheServerId'
_H='InetPortNumber'
_G='rpkiRtrCacheServerSessionID'
_F='rpkiRtrCacheServerLatestSerial'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='current'
_A='RPKI-ROUTER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType',_O,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
LongUtf8String,=mibBuilder.importSymbols('SYSAPPL-MIB','LongUtf8String')
rpkiRtrMIB=ModuleIdentity((1,3,6,1,2,1,218))
if mibBuilder.loadTexts:rpkiRtrMIB.setRevisions(('2013-05-01 00:00',))
class RpkiRtrConnectionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ssh',1),('tls',2),('tcpMD5',3),('tcpAO',4),('tcp',5),('ipsec',6),('other',7)))
_RpkiRtrNotifications_ObjectIdentity=ObjectIdentity
rpkiRtrNotifications=_RpkiRtrNotifications_ObjectIdentity((1,3,6,1,2,1,218,0))
_RpkiRtrObjects_ObjectIdentity=ObjectIdentity
rpkiRtrObjects=_RpkiRtrObjects_ObjectIdentity((1,3,6,1,2,1,218,1))
_RpkiRtrDiscontinuityTimer_Type=TimeStamp
_RpkiRtrDiscontinuityTimer_Object=MibScalar
rpkiRtrDiscontinuityTimer=_RpkiRtrDiscontinuityTimer_Object((1,3,6,1,2,1,218,1,1),_RpkiRtrDiscontinuityTimer_Type())
rpkiRtrDiscontinuityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrDiscontinuityTimer.setStatus(_B)
_RpkiRtrCacheServerTable_Object=MibTable
rpkiRtrCacheServerTable=_RpkiRtrCacheServerTable_Object((1,3,6,1,2,1,218,1,2))
if mibBuilder.loadTexts:rpkiRtrCacheServerTable.setStatus(_B)
_RpkiRtrCacheServerTableEntry_Object=MibTableRow
rpkiRtrCacheServerTableEntry=_RpkiRtrCacheServerTableEntry_Object((1,3,6,1,2,1,218,1,2,1))
rpkiRtrCacheServerTableEntry.setIndexNames((0,_A,_Q),(0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:rpkiRtrCacheServerTableEntry.setStatus(_B)
_RpkiRtrCacheServerRemoteAddressType_Type=InetAddressType
_RpkiRtrCacheServerRemoteAddressType_Object=MibTableColumn
rpkiRtrCacheServerRemoteAddressType=_RpkiRtrCacheServerRemoteAddressType_Object((1,3,6,1,2,1,218,1,2,1,1),_RpkiRtrCacheServerRemoteAddressType_Type())
rpkiRtrCacheServerRemoteAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrCacheServerRemoteAddressType.setStatus(_B)
_RpkiRtrCacheServerRemoteAddress_Type=InetAddress
_RpkiRtrCacheServerRemoteAddress_Object=MibTableColumn
rpkiRtrCacheServerRemoteAddress=_RpkiRtrCacheServerRemoteAddress_Object((1,3,6,1,2,1,218,1,2,1,2),_RpkiRtrCacheServerRemoteAddress_Type())
rpkiRtrCacheServerRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrCacheServerRemoteAddress.setStatus(_B)
class _RpkiRtrCacheServerRemotePort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RpkiRtrCacheServerRemotePort_Type.__name__=_H
_RpkiRtrCacheServerRemotePort_Object=MibTableColumn
rpkiRtrCacheServerRemotePort=_RpkiRtrCacheServerRemotePort_Object((1,3,6,1,2,1,218,1,2,1,3),_RpkiRtrCacheServerRemotePort_Type())
rpkiRtrCacheServerRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrCacheServerRemotePort.setStatus(_B)
_RpkiRtrCacheServerLocalAddressType_Type=InetAddressType
_RpkiRtrCacheServerLocalAddressType_Object=MibTableColumn
rpkiRtrCacheServerLocalAddressType=_RpkiRtrCacheServerLocalAddressType_Object((1,3,6,1,2,1,218,1,2,1,4),_RpkiRtrCacheServerLocalAddressType_Type())
rpkiRtrCacheServerLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerLocalAddressType.setStatus(_B)
_RpkiRtrCacheServerLocalAddress_Type=InetAddress
_RpkiRtrCacheServerLocalAddress_Object=MibTableColumn
rpkiRtrCacheServerLocalAddress=_RpkiRtrCacheServerLocalAddress_Object((1,3,6,1,2,1,218,1,2,1,5),_RpkiRtrCacheServerLocalAddress_Type())
rpkiRtrCacheServerLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerLocalAddress.setStatus(_B)
class _RpkiRtrCacheServerLocalPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RpkiRtrCacheServerLocalPort_Type.__name__=_H
_RpkiRtrCacheServerLocalPort_Object=MibTableColumn
rpkiRtrCacheServerLocalPort=_RpkiRtrCacheServerLocalPort_Object((1,3,6,1,2,1,218,1,2,1,6),_RpkiRtrCacheServerLocalPort_Type())
rpkiRtrCacheServerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerLocalPort.setStatus(_B)
class _RpkiRtrCacheServerPreference_Type(Unsigned32):defaultValue=4294967295
_RpkiRtrCacheServerPreference_Type.__name__=_E
_RpkiRtrCacheServerPreference_Object=MibTableColumn
rpkiRtrCacheServerPreference=_RpkiRtrCacheServerPreference_Object((1,3,6,1,2,1,218,1,2,1,7),_RpkiRtrCacheServerPreference_Type())
rpkiRtrCacheServerPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerPreference.setStatus(_B)
_RpkiRtrCacheServerConnectionType_Type=RpkiRtrConnectionType
_RpkiRtrCacheServerConnectionType_Object=MibTableColumn
rpkiRtrCacheServerConnectionType=_RpkiRtrCacheServerConnectionType_Object((1,3,6,1,2,1,218,1,2,1,8),_RpkiRtrCacheServerConnectionType_Type())
rpkiRtrCacheServerConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerConnectionType.setStatus(_B)
class _RpkiRtrCacheServerConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RpkiRtrCacheServerConnectionStatus_Type.__name__=_P
_RpkiRtrCacheServerConnectionStatus_Object=MibTableColumn
rpkiRtrCacheServerConnectionStatus=_RpkiRtrCacheServerConnectionStatus_Object((1,3,6,1,2,1,218,1,2,1,9),_RpkiRtrCacheServerConnectionStatus_Type())
rpkiRtrCacheServerConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerConnectionStatus.setStatus(_B)
_RpkiRtrCacheServerDescription_Type=LongUtf8String
_RpkiRtrCacheServerDescription_Object=MibTableColumn
rpkiRtrCacheServerDescription=_RpkiRtrCacheServerDescription_Object((1,3,6,1,2,1,218,1,2,1,10),_RpkiRtrCacheServerDescription_Type())
rpkiRtrCacheServerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerDescription.setStatus(_B)
_RpkiRtrCacheServerMsgsReceived_Type=Counter32
_RpkiRtrCacheServerMsgsReceived_Object=MibTableColumn
rpkiRtrCacheServerMsgsReceived=_RpkiRtrCacheServerMsgsReceived_Object((1,3,6,1,2,1,218,1,2,1,11),_RpkiRtrCacheServerMsgsReceived_Type())
rpkiRtrCacheServerMsgsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerMsgsReceived.setStatus(_B)
_RpkiRtrCacheServerMsgsSent_Type=Counter32
_RpkiRtrCacheServerMsgsSent_Object=MibTableColumn
rpkiRtrCacheServerMsgsSent=_RpkiRtrCacheServerMsgsSent_Object((1,3,6,1,2,1,218,1,2,1,12),_RpkiRtrCacheServerMsgsSent_Type())
rpkiRtrCacheServerMsgsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerMsgsSent.setStatus(_B)
_RpkiRtrCacheServerV4ActiveRecords_Type=Gauge32
_RpkiRtrCacheServerV4ActiveRecords_Object=MibTableColumn
rpkiRtrCacheServerV4ActiveRecords=_RpkiRtrCacheServerV4ActiveRecords_Object((1,3,6,1,2,1,218,1,2,1,13),_RpkiRtrCacheServerV4ActiveRecords_Type())
rpkiRtrCacheServerV4ActiveRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerV4ActiveRecords.setStatus(_B)
_RpkiRtrCacheServerV4Announcements_Type=Counter32
_RpkiRtrCacheServerV4Announcements_Object=MibTableColumn
rpkiRtrCacheServerV4Announcements=_RpkiRtrCacheServerV4Announcements_Object((1,3,6,1,2,1,218,1,2,1,14),_RpkiRtrCacheServerV4Announcements_Type())
rpkiRtrCacheServerV4Announcements.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerV4Announcements.setStatus(_B)
_RpkiRtrCacheServerV4Withdrawals_Type=Counter32
_RpkiRtrCacheServerV4Withdrawals_Object=MibTableColumn
rpkiRtrCacheServerV4Withdrawals=_RpkiRtrCacheServerV4Withdrawals_Object((1,3,6,1,2,1,218,1,2,1,15),_RpkiRtrCacheServerV4Withdrawals_Type())
rpkiRtrCacheServerV4Withdrawals.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerV4Withdrawals.setStatus(_B)
_RpkiRtrCacheServerV6ActiveRecords_Type=Gauge32
_RpkiRtrCacheServerV6ActiveRecords_Object=MibTableColumn
rpkiRtrCacheServerV6ActiveRecords=_RpkiRtrCacheServerV6ActiveRecords_Object((1,3,6,1,2,1,218,1,2,1,16),_RpkiRtrCacheServerV6ActiveRecords_Type())
rpkiRtrCacheServerV6ActiveRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerV6ActiveRecords.setStatus(_B)
_RpkiRtrCacheServerV6Announcements_Type=Counter32
_RpkiRtrCacheServerV6Announcements_Object=MibTableColumn
rpkiRtrCacheServerV6Announcements=_RpkiRtrCacheServerV6Announcements_Object((1,3,6,1,2,1,218,1,2,1,17),_RpkiRtrCacheServerV6Announcements_Type())
rpkiRtrCacheServerV6Announcements.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerV6Announcements.setStatus(_B)
_RpkiRtrCacheServerV6Withdrawals_Type=Counter32
_RpkiRtrCacheServerV6Withdrawals_Object=MibTableColumn
rpkiRtrCacheServerV6Withdrawals=_RpkiRtrCacheServerV6Withdrawals_Object((1,3,6,1,2,1,218,1,2,1,18),_RpkiRtrCacheServerV6Withdrawals_Type())
rpkiRtrCacheServerV6Withdrawals.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerV6Withdrawals.setStatus(_B)
_RpkiRtrCacheServerLatestSerial_Type=Unsigned32
_RpkiRtrCacheServerLatestSerial_Object=MibTableColumn
rpkiRtrCacheServerLatestSerial=_RpkiRtrCacheServerLatestSerial_Object((1,3,6,1,2,1,218,1,2,1,19),_RpkiRtrCacheServerLatestSerial_Type())
rpkiRtrCacheServerLatestSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerLatestSerial.setStatus(_B)
class _RpkiRtrCacheServerSessionID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpkiRtrCacheServerSessionID_Type.__name__=_E
_RpkiRtrCacheServerSessionID_Object=MibTableColumn
rpkiRtrCacheServerSessionID=_RpkiRtrCacheServerSessionID_Object((1,3,6,1,2,1,218,1,2,1,20),_RpkiRtrCacheServerSessionID_Type())
rpkiRtrCacheServerSessionID.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerSessionID.setStatus(_B)
class _RpkiRtrCacheServerRefreshTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,7200))
_RpkiRtrCacheServerRefreshTimer_Type.__name__=_E
_RpkiRtrCacheServerRefreshTimer_Object=MibTableColumn
rpkiRtrCacheServerRefreshTimer=_RpkiRtrCacheServerRefreshTimer_Object((1,3,6,1,2,1,218,1,2,1,21),_RpkiRtrCacheServerRefreshTimer_Type())
rpkiRtrCacheServerRefreshTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerRefreshTimer.setStatus(_B)
if mibBuilder.loadTexts:rpkiRtrCacheServerRefreshTimer.setUnits(_T)
_RpkiRtrCacheServerTimeToRefresh_Type=Integer32
_RpkiRtrCacheServerTimeToRefresh_Object=MibTableColumn
rpkiRtrCacheServerTimeToRefresh=_RpkiRtrCacheServerTimeToRefresh_Object((1,3,6,1,2,1,218,1,2,1,22),_RpkiRtrCacheServerTimeToRefresh_Type())
rpkiRtrCacheServerTimeToRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerTimeToRefresh.setStatus(_B)
if mibBuilder.loadTexts:rpkiRtrCacheServerTimeToRefresh.setUnits(_T)
class _RpkiRtrCacheServerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RpkiRtrCacheServerId_Type.__name__=_E
_RpkiRtrCacheServerId_Object=MibTableColumn
rpkiRtrCacheServerId=_RpkiRtrCacheServerId_Object((1,3,6,1,2,1,218,1,2,1,23),_RpkiRtrCacheServerId_Type())
rpkiRtrCacheServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerId.setStatus(_B)
_RpkiRtrCacheServerErrorsTable_Object=MibTable
rpkiRtrCacheServerErrorsTable=_RpkiRtrCacheServerErrorsTable_Object((1,3,6,1,2,1,218,1,3))
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsTable.setStatus(_B)
_RpkiRtrCacheServerErrorsTableEntry_Object=MibTableRow
rpkiRtrCacheServerErrorsTableEntry=_RpkiRtrCacheServerErrorsTableEntry_Object((1,3,6,1,2,1,218,1,3,1))
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsTableEntry.setStatus(_B)
_RpkiRtrCacheServerErrorsCorruptData_Type=Counter32
_RpkiRtrCacheServerErrorsCorruptData_Object=MibTableColumn
rpkiRtrCacheServerErrorsCorruptData=_RpkiRtrCacheServerErrorsCorruptData_Object((1,3,6,1,2,1,218,1,3,1,1),_RpkiRtrCacheServerErrorsCorruptData_Type())
rpkiRtrCacheServerErrorsCorruptData.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsCorruptData.setStatus(_B)
_RpkiRtrCacheServerErrorsInternalError_Type=Counter32
_RpkiRtrCacheServerErrorsInternalError_Object=MibTableColumn
rpkiRtrCacheServerErrorsInternalError=_RpkiRtrCacheServerErrorsInternalError_Object((1,3,6,1,2,1,218,1,3,1,2),_RpkiRtrCacheServerErrorsInternalError_Type())
rpkiRtrCacheServerErrorsInternalError.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsInternalError.setStatus(_B)
_RpkiRtrCacheServerErrorsNoData_Type=Counter32
_RpkiRtrCacheServerErrorsNoData_Object=MibTableColumn
rpkiRtrCacheServerErrorsNoData=_RpkiRtrCacheServerErrorsNoData_Object((1,3,6,1,2,1,218,1,3,1,3),_RpkiRtrCacheServerErrorsNoData_Type())
rpkiRtrCacheServerErrorsNoData.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsNoData.setStatus(_B)
_RpkiRtrCacheServerErrorsInvalidRequest_Type=Counter32
_RpkiRtrCacheServerErrorsInvalidRequest_Object=MibTableColumn
rpkiRtrCacheServerErrorsInvalidRequest=_RpkiRtrCacheServerErrorsInvalidRequest_Object((1,3,6,1,2,1,218,1,3,1,4),_RpkiRtrCacheServerErrorsInvalidRequest_Type())
rpkiRtrCacheServerErrorsInvalidRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsInvalidRequest.setStatus(_B)
_RpkiRtrCacheServerErrorsUnsupportedVersion_Type=Counter32
_RpkiRtrCacheServerErrorsUnsupportedVersion_Object=MibTableColumn
rpkiRtrCacheServerErrorsUnsupportedVersion=_RpkiRtrCacheServerErrorsUnsupportedVersion_Object((1,3,6,1,2,1,218,1,3,1,5),_RpkiRtrCacheServerErrorsUnsupportedVersion_Type())
rpkiRtrCacheServerErrorsUnsupportedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsUnsupportedVersion.setStatus(_B)
_RpkiRtrCacheServerErrorsUnsupportedPdu_Type=Counter32
_RpkiRtrCacheServerErrorsUnsupportedPdu_Object=MibTableColumn
rpkiRtrCacheServerErrorsUnsupportedPdu=_RpkiRtrCacheServerErrorsUnsupportedPdu_Object((1,3,6,1,2,1,218,1,3,1,6),_RpkiRtrCacheServerErrorsUnsupportedPdu_Type())
rpkiRtrCacheServerErrorsUnsupportedPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsUnsupportedPdu.setStatus(_B)
_RpkiRtrCacheServerErrorsWithdrawalUnknown_Type=Counter32
_RpkiRtrCacheServerErrorsWithdrawalUnknown_Object=MibTableColumn
rpkiRtrCacheServerErrorsWithdrawalUnknown=_RpkiRtrCacheServerErrorsWithdrawalUnknown_Object((1,3,6,1,2,1,218,1,3,1,7),_RpkiRtrCacheServerErrorsWithdrawalUnknown_Type())
rpkiRtrCacheServerErrorsWithdrawalUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsWithdrawalUnknown.setStatus(_B)
_RpkiRtrCacheServerErrorsDuplicateAnnounce_Type=Counter32
_RpkiRtrCacheServerErrorsDuplicateAnnounce_Object=MibTableColumn
rpkiRtrCacheServerErrorsDuplicateAnnounce=_RpkiRtrCacheServerErrorsDuplicateAnnounce_Object((1,3,6,1,2,1,218,1,3,1,8),_RpkiRtrCacheServerErrorsDuplicateAnnounce_Type())
rpkiRtrCacheServerErrorsDuplicateAnnounce.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsDuplicateAnnounce.setStatus(_B)
_RpkiRtrPrefixOriginTable_Object=MibTable
rpkiRtrPrefixOriginTable=_RpkiRtrPrefixOriginTable_Object((1,3,6,1,2,1,218,1,4))
if mibBuilder.loadTexts:rpkiRtrPrefixOriginTable.setStatus(_B)
_RpkiRtrPrefixOriginTableEntry_Object=MibTableRow
rpkiRtrPrefixOriginTableEntry=_RpkiRtrPrefixOriginTableEntry_Object((1,3,6,1,2,1,218,1,4,1))
rpkiRtrPrefixOriginTableEntry.setIndexNames((0,_A,_U),(0,_A,_V),(0,_A,_W),(0,_A,_X),(0,_A,_Y),(0,_A,_I))
if mibBuilder.loadTexts:rpkiRtrPrefixOriginTableEntry.setStatus(_B)
_RpkiRtrPrefixOriginAddressType_Type=InetAddressType
_RpkiRtrPrefixOriginAddressType_Object=MibTableColumn
rpkiRtrPrefixOriginAddressType=_RpkiRtrPrefixOriginAddressType_Object((1,3,6,1,2,1,218,1,4,1,1),_RpkiRtrPrefixOriginAddressType_Type())
rpkiRtrPrefixOriginAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrPrefixOriginAddressType.setStatus(_B)
_RpkiRtrPrefixOriginAddress_Type=InetAddress
_RpkiRtrPrefixOriginAddress_Object=MibTableColumn
rpkiRtrPrefixOriginAddress=_RpkiRtrPrefixOriginAddress_Object((1,3,6,1,2,1,218,1,4,1,2),_RpkiRtrPrefixOriginAddress_Type())
rpkiRtrPrefixOriginAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrPrefixOriginAddress.setStatus(_B)
_RpkiRtrPrefixOriginMinLength_Type=InetAddressPrefixLength
_RpkiRtrPrefixOriginMinLength_Object=MibTableColumn
rpkiRtrPrefixOriginMinLength=_RpkiRtrPrefixOriginMinLength_Object((1,3,6,1,2,1,218,1,4,1,3),_RpkiRtrPrefixOriginMinLength_Type())
rpkiRtrPrefixOriginMinLength.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrPrefixOriginMinLength.setStatus(_B)
_RpkiRtrPrefixOriginMaxLength_Type=InetAddressPrefixLength
_RpkiRtrPrefixOriginMaxLength_Object=MibTableColumn
rpkiRtrPrefixOriginMaxLength=_RpkiRtrPrefixOriginMaxLength_Object((1,3,6,1,2,1,218,1,4,1,4),_RpkiRtrPrefixOriginMaxLength_Type())
rpkiRtrPrefixOriginMaxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrPrefixOriginMaxLength.setStatus(_B)
class _RpkiRtrPrefixOriginASN_Type(InetAutonomousSystemNumber):subtypeSpec=InetAutonomousSystemNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RpkiRtrPrefixOriginASN_Type.__name__=_O
_RpkiRtrPrefixOriginASN_Object=MibTableColumn
rpkiRtrPrefixOriginASN=_RpkiRtrPrefixOriginASN_Object((1,3,6,1,2,1,218,1,4,1,5),_RpkiRtrPrefixOriginASN_Type())
rpkiRtrPrefixOriginASN.setMaxAccess(_D)
if mibBuilder.loadTexts:rpkiRtrPrefixOriginASN.setStatus(_B)
class _RpkiRtrPrefixOriginCacheServerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RpkiRtrPrefixOriginCacheServerId_Type.__name__=_E
_RpkiRtrPrefixOriginCacheServerId_Object=MibTableColumn
rpkiRtrPrefixOriginCacheServerId=_RpkiRtrPrefixOriginCacheServerId_Object((1,3,6,1,2,1,218,1,4,1,6),_RpkiRtrPrefixOriginCacheServerId_Type())
rpkiRtrPrefixOriginCacheServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:rpkiRtrPrefixOriginCacheServerId.setStatus(_B)
_RpkiRtrConformance_ObjectIdentity=ObjectIdentity
rpkiRtrConformance=_RpkiRtrConformance_ObjectIdentity((1,3,6,1,2,1,218,2))
_RpkiRtrCompliances_ObjectIdentity=ObjectIdentity
rpkiRtrCompliances=_RpkiRtrCompliances_ObjectIdentity((1,3,6,1,2,1,218,2,1))
_RpkiRtrGroups_ObjectIdentity=ObjectIdentity
rpkiRtrGroups=_RpkiRtrGroups_ObjectIdentity((1,3,6,1,2,1,218,2,2))
rpkiRtrCacheServerTableEntry.registerAugmentions((_A,_Z))
rpkiRtrCacheServerErrorsTableEntry.setIndexNames(*rpkiRtrCacheServerTableEntry.getIndexNames())
rpkiRtrCacheServerGroup=ObjectGroup((1,3,6,1,2,1,218,2,2,1))
rpkiRtrCacheServerGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_J),(_A,_g),(_A,_h),(_A,_i),(_A,_K),(_A,_j),(_A,_k),(_A,_L),(_A,_l),(_A,_m),(_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_n)))
if mibBuilder.loadTexts:rpkiRtrCacheServerGroup.setStatus(_B)
rpkiRtrCacheServerErrorsGroup=ObjectGroup((1,3,6,1,2,1,218,2,2,2))
rpkiRtrCacheServerErrorsGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:rpkiRtrCacheServerErrorsGroup.setStatus(_B)
rpkiRtrPrefixOriginGroup=ObjectGroup((1,3,6,1,2,1,218,2,2,3))
rpkiRtrPrefixOriginGroup.setObjects((_A,_I))
if mibBuilder.loadTexts:rpkiRtrPrefixOriginGroup.setStatus(_B)
rpkiRtrCacheServerConnectionStateChange=NotificationType((1,3,6,1,2,1,218,0,1))
rpkiRtrCacheServerConnectionStateChange.setObjects(*((_A,_J),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:rpkiRtrCacheServerConnectionStateChange.setStatus(_B)
rpkiRtrCacheServerConnectionToGoStale=NotificationType((1,3,6,1,2,1,218,0,2))
rpkiRtrCacheServerConnectionToGoStale.setObjects(*((_A,_K),(_A,_L),(_A,_F),(_A,_G),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:rpkiRtrCacheServerConnectionToGoStale.setStatus(_B)
rpkiRtrNotificationsGroup=NotificationGroup((1,3,6,1,2,1,218,2,2,4))
rpkiRtrNotificationsGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:rpkiRtrNotificationsGroup.setStatus(_B)
rpkiRtrRFC6945ReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,218,2,1,1))
rpkiRtrRFC6945ReadOnlyCompliance.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:rpkiRtrRFC6945ReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RpkiRtrConnectionType':RpkiRtrConnectionType,'rpkiRtrMIB':rpkiRtrMIB,'rpkiRtrNotifications':rpkiRtrNotifications,_w:rpkiRtrCacheServerConnectionStateChange,_x:rpkiRtrCacheServerConnectionToGoStale,'rpkiRtrObjects':rpkiRtrObjects,_a:rpkiRtrDiscontinuityTimer,'rpkiRtrCacheServerTable':rpkiRtrCacheServerTable,'rpkiRtrCacheServerTableEntry':rpkiRtrCacheServerTableEntry,_Q:rpkiRtrCacheServerRemoteAddressType,_R:rpkiRtrCacheServerRemoteAddress,_S:rpkiRtrCacheServerRemotePort,_b:rpkiRtrCacheServerLocalAddressType,_c:rpkiRtrCacheServerLocalAddress,_d:rpkiRtrCacheServerLocalPort,_e:rpkiRtrCacheServerPreference,_f:rpkiRtrCacheServerConnectionType,_J:rpkiRtrCacheServerConnectionStatus,_g:rpkiRtrCacheServerDescription,_h:rpkiRtrCacheServerMsgsReceived,_i:rpkiRtrCacheServerMsgsSent,_K:rpkiRtrCacheServerV4ActiveRecords,_j:rpkiRtrCacheServerV4Announcements,_k:rpkiRtrCacheServerV4Withdrawals,_L:rpkiRtrCacheServerV6ActiveRecords,_l:rpkiRtrCacheServerV6Announcements,_m:rpkiRtrCacheServerV6Withdrawals,_F:rpkiRtrCacheServerLatestSerial,_G:rpkiRtrCacheServerSessionID,_M:rpkiRtrCacheServerRefreshTimer,_N:rpkiRtrCacheServerTimeToRefresh,_n:rpkiRtrCacheServerId,'rpkiRtrCacheServerErrorsTable':rpkiRtrCacheServerErrorsTable,_Z:rpkiRtrCacheServerErrorsTableEntry,_o:rpkiRtrCacheServerErrorsCorruptData,_p:rpkiRtrCacheServerErrorsInternalError,_q:rpkiRtrCacheServerErrorsNoData,_r:rpkiRtrCacheServerErrorsInvalidRequest,_s:rpkiRtrCacheServerErrorsUnsupportedVersion,_t:rpkiRtrCacheServerErrorsUnsupportedPdu,_u:rpkiRtrCacheServerErrorsWithdrawalUnknown,_v:rpkiRtrCacheServerErrorsDuplicateAnnounce,'rpkiRtrPrefixOriginTable':rpkiRtrPrefixOriginTable,'rpkiRtrPrefixOriginTableEntry':rpkiRtrPrefixOriginTableEntry,_U:rpkiRtrPrefixOriginAddressType,_V:rpkiRtrPrefixOriginAddress,_W:rpkiRtrPrefixOriginMinLength,_X:rpkiRtrPrefixOriginMaxLength,_Y:rpkiRtrPrefixOriginASN,_I:rpkiRtrPrefixOriginCacheServerId,'rpkiRtrConformance':rpkiRtrConformance,'rpkiRtrCompliances':rpkiRtrCompliances,'rpkiRtrRFC6945ReadOnlyCompliance':rpkiRtrRFC6945ReadOnlyCompliance,'rpkiRtrGroups':rpkiRtrGroups,_y:rpkiRtrCacheServerGroup,_A1:rpkiRtrCacheServerErrorsGroup,_z:rpkiRtrPrefixOriginGroup,_A0:rpkiRtrNotificationsGroup})