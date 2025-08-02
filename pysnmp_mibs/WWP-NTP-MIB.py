_G='wwpNtpServerIpAddr'
_F='WWP-NTP-MIB'
_E='enable'
_D='disable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpNtpMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,5))
if mibBuilder.loadTexts:wwpNtpMIB.setRevisions(('2003-03-11 00:00','2001-04-03 17:00'))
_WwpNtpMIBObjects_ObjectIdentity=ObjectIdentity
wwpNtpMIBObjects=_WwpNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,5,1))
_WwpNtp_ObjectIdentity=ObjectIdentity
wwpNtp=_WwpNtp_ObjectIdentity((1,3,6,1,4,1,6141,2,5,1,1))
class _WwpNtpRcvBroadcasts_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpNtpRcvBroadcasts_Type.__name__=_B
_WwpNtpRcvBroadcasts_Object=MibScalar
wwpNtpRcvBroadcasts=_WwpNtpRcvBroadcasts_Object((1,3,6,1,4,1,6141,2,5,1,1,1),_WwpNtpRcvBroadcasts_Type())
wwpNtpRcvBroadcasts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpNtpRcvBroadcasts.setStatus(_A)
class _WwpNtpEnablePolling_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpNtpEnablePolling_Type.__name__=_B
_WwpNtpEnablePolling_Object=MibScalar
wwpNtpEnablePolling=_WwpNtpEnablePolling_Object((1,3,6,1,4,1,6141,2,5,1,1,2),_WwpNtpEnablePolling_Type())
wwpNtpEnablePolling.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpNtpEnablePolling.setStatus(_A)
class _WwpNtpPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpNtpPollFreq_Type.__name__=_B
_WwpNtpPollFreq_Object=MibScalar
wwpNtpPollFreq=_WwpNtpPollFreq_Object((1,3,6,1,4,1,6141,2,5,1,1,3),_WwpNtpPollFreq_Type())
wwpNtpPollFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpNtpPollFreq.setStatus(_A)
_WwpNtpServerTable_Object=MibTable
wwpNtpServerTable=_WwpNtpServerTable_Object((1,3,6,1,4,1,6141,2,5,1,1,4))
if mibBuilder.loadTexts:wwpNtpServerTable.setStatus(_A)
_WwpNtpServerEntry_Object=MibTableRow
wwpNtpServerEntry=_WwpNtpServerEntry_Object((1,3,6,1,4,1,6141,2,5,1,1,4,1))
wwpNtpServerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wwpNtpServerEntry.setStatus(_A)
_WwpNtpServerIpAddr_Type=IpAddress
_WwpNtpServerIpAddr_Object=MibTableColumn
wwpNtpServerIpAddr=_WwpNtpServerIpAddr_Object((1,3,6,1,4,1,6141,2,5,1,1,4,1,1),_WwpNtpServerIpAddr_Type())
wwpNtpServerIpAddr.setMaxAccess('read-only')
if mibBuilder.loadTexts:wwpNtpServerIpAddr.setStatus(_A)
_WwpNtpServerRowStatus_Type=RowStatus
_WwpNtpServerRowStatus_Object=MibTableColumn
wwpNtpServerRowStatus=_WwpNtpServerRowStatus_Object((1,3,6,1,4,1,6141,2,5,1,1,4,1,2),_WwpNtpServerRowStatus_Type())
wwpNtpServerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpNtpServerRowStatus.setStatus(_A)
_WwpNtpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpNtpMIBNotificationPrefix=_WwpNtpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,5,2))
_WwpNtpMIBNotifications_ObjectIdentity=ObjectIdentity
wwpNtpMIBNotifications=_WwpNtpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,5,2,0))
_WwpNtpMIBConformance_ObjectIdentity=ObjectIdentity
wwpNtpMIBConformance=_WwpNtpMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,5,3))
_WwpNtpMIBCompliances_ObjectIdentity=ObjectIdentity
wwpNtpMIBCompliances=_WwpNtpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,5,3,1))
_WwpNtpMIBGroups_ObjectIdentity=ObjectIdentity
wwpNtpMIBGroups=_WwpNtpMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,5,3,2))
mibBuilder.exportSymbols(_F,**{'wwpNtpMIB':wwpNtpMIB,'wwpNtpMIBObjects':wwpNtpMIBObjects,'wwpNtp':wwpNtp,'wwpNtpRcvBroadcasts':wwpNtpRcvBroadcasts,'wwpNtpEnablePolling':wwpNtpEnablePolling,'wwpNtpPollFreq':wwpNtpPollFreq,'wwpNtpServerTable':wwpNtpServerTable,'wwpNtpServerEntry':wwpNtpServerEntry,_G:wwpNtpServerIpAddr,'wwpNtpServerRowStatus':wwpNtpServerRowStatus,'wwpNtpMIBNotificationPrefix':wwpNtpMIBNotificationPrefix,'wwpNtpMIBNotifications':wwpNtpMIBNotifications,'wwpNtpMIBConformance':wwpNtpMIBConformance,'wwpNtpMIBCompliances':wwpNtpMIBCompliances,'wwpNtpMIBGroups':wwpNtpMIBGroups})