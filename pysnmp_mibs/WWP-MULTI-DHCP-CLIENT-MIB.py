_I='wwpDhcpIfIndex'
_H='WWP-MULTI-DHCP-CLIENT-MIB'
_G='DisplayString'
_F='TruthValue'
_E='read-write'
_D='seconds'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_F)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpMultiDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,42))
if mibBuilder.loadTexts:wwpMultiDhcpClientMIB.setRevisions(('2002-11-01 17:00',))
_WwpMultiDhcpClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClientMIBObjects=_WwpMultiDhcpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,42,1))
_WwpMultiDhcpClient_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClient=_WwpMultiDhcpClient_ObjectIdentity((1,3,6,1,4,1,6141,2,42,1,1))
_WwpMultiDhcpClientNumber_Type=Integer32
_WwpMultiDhcpClientNumber_Object=MibScalar
wwpMultiDhcpClientNumber=_WwpMultiDhcpClientNumber_Object((1,3,6,1,4,1,6141,2,42,1,1,1),_WwpMultiDhcpClientNumber_Type())
wwpMultiDhcpClientNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpMultiDhcpClientNumber.setStatus(_A)
_WwpMultiDhcpClientTable_Object=MibTable
wwpMultiDhcpClientTable=_WwpMultiDhcpClientTable_Object((1,3,6,1,4,1,6141,2,42,1,1,2))
if mibBuilder.loadTexts:wwpMultiDhcpClientTable.setStatus(_A)
_WwpMultiDhcpClientEntry_Object=MibTableRow
wwpMultiDhcpClientEntry=_WwpMultiDhcpClientEntry_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1))
wwpMultiDhcpClientEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:wwpMultiDhcpClientEntry.setStatus(_A)
class _WwpDhcpIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpDhcpIfIndex_Type.__name__=_B
_WwpDhcpIfIndex_Object=MibTableColumn
wwpDhcpIfIndex=_WwpDhcpIfIndex_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,1),_WwpDhcpIfIndex_Type())
wwpDhcpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpIfIndex.setStatus(_A)
class _WwpDhcpIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpDhcpIfName_Type.__name__=_G
_WwpDhcpIfName_Object=MibTableColumn
wwpDhcpIfName=_WwpDhcpIfName_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,2),_WwpDhcpIfName_Type())
wwpDhcpIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpIfName.setStatus(_A)
class _WwpDhcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpDhcpStatus_Type.__name__=_B
_WwpDhcpStatus_Object=MibTableColumn
wwpDhcpStatus=_WwpDhcpStatus_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,3),_WwpDhcpStatus_Type())
wwpDhcpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpDhcpStatus.setStatus(_A)
class _WwpDhcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('bound',1),('disabled',2),('inform',3),('init',4),('rebinding',5),('renewing',6),('requesting',7),('selecting',8),('unknown',9)))
_WwpDhcpState_Type.__name__=_B
_WwpDhcpState_Object=MibTableColumn
wwpDhcpState=_WwpDhcpState_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,4),_WwpDhcpState_Type())
wwpDhcpState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpState.setStatus(_A)
class _WwpDhcpLeaseTimeRequested_Type(Integer32):defaultValue=45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpLeaseTimeRequested_Type.__name__=_B
_WwpDhcpLeaseTimeRequested_Object=MibTableColumn
wwpDhcpLeaseTimeRequested=_WwpDhcpLeaseTimeRequested_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,5),_WwpDhcpLeaseTimeRequested_Type())
wwpDhcpLeaseTimeRequested.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpDhcpLeaseTimeRequested.setStatus(_A)
if mibBuilder.loadTexts:wwpDhcpLeaseTimeRequested.setUnits(_D)
class _WwpDhcpLeaseOffered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpLeaseOffered_Type.__name__=_B
_WwpDhcpLeaseOffered_Object=MibTableColumn
wwpDhcpLeaseOffered=_WwpDhcpLeaseOffered_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,6),_WwpDhcpLeaseOffered_Type())
wwpDhcpLeaseOffered.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpLeaseOffered.setStatus(_A)
if mibBuilder.loadTexts:wwpDhcpLeaseOffered.setUnits(_D)
class _WwpDhcpLeaseRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpLeaseRemaining_Type.__name__=_B
_WwpDhcpLeaseRemaining_Object=MibTableColumn
wwpDhcpLeaseRemaining=_WwpDhcpLeaseRemaining_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,7),_WwpDhcpLeaseRemaining_Type())
wwpDhcpLeaseRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpLeaseRemaining.setStatus(_A)
if mibBuilder.loadTexts:wwpDhcpLeaseRemaining.setUnits(_D)
class _WwpDhcpDiscoveryMsgInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpDiscoveryMsgInterval_Type.__name__=_B
_WwpDhcpDiscoveryMsgInterval_Object=MibTableColumn
wwpDhcpDiscoveryMsgInterval=_WwpDhcpDiscoveryMsgInterval_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,8),_WwpDhcpDiscoveryMsgInterval_Type())
wwpDhcpDiscoveryMsgInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpDhcpDiscoveryMsgInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpDhcpDiscoveryMsgInterval.setUnits(_D)
class _WwpDhcpRenewalTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpRenewalTime_Type.__name__=_B
_WwpDhcpRenewalTime_Object=MibTableColumn
wwpDhcpRenewalTime=_WwpDhcpRenewalTime_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,9),_WwpDhcpRenewalTime_Type())
wwpDhcpRenewalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpRenewalTime.setStatus(_A)
if mibBuilder.loadTexts:wwpDhcpRenewalTime.setUnits(_D)
class _WwpDhcpRebindingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpDhcpRebindingTime_Type.__name__=_B
_WwpDhcpRebindingTime_Object=MibTableColumn
wwpDhcpRebindingTime=_WwpDhcpRebindingTime_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,10),_WwpDhcpRebindingTime_Type())
wwpDhcpRebindingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpRebindingTime.setStatus(_A)
if mibBuilder.loadTexts:wwpDhcpRebindingTime.setUnits(_D)
_WwpDhcpServerAddress_Type=IpAddress
_WwpDhcpServerAddress_Object=MibTableColumn
wwpDhcpServerAddress=_WwpDhcpServerAddress_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,11),_WwpDhcpServerAddress_Type())
wwpDhcpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpDhcpServerAddress.setStatus(_A)
class _WwpDhcpRenewLease_Type(TruthValue):defaultValue=2
_WwpDhcpRenewLease_Type.__name__=_F
_WwpDhcpRenewLease_Object=MibTableColumn
wwpDhcpRenewLease=_WwpDhcpRenewLease_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,12),_WwpDhcpRenewLease_Type())
wwpDhcpRenewLease.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpDhcpRenewLease.setStatus(_A)
class _WwpDhcpReleaseLease_Type(TruthValue):defaultValue=2
_WwpDhcpReleaseLease_Type.__name__=_F
_WwpDhcpReleaseLease_Object=MibTableColumn
wwpDhcpReleaseLease=_WwpDhcpReleaseLease_Object((1,3,6,1,4,1,6141,2,42,1,1,2,1,13),_WwpDhcpReleaseLease_Type())
wwpDhcpReleaseLease.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpDhcpReleaseLease.setStatus(_A)
_WwpMultiDhcpClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClientMIBNotificationPrefix=_WwpMultiDhcpClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,42,2))
_WwpMultiDhcpClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClientMIBNotifications=_WwpMultiDhcpClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,42,2,0))
_WwpMultiDhcpClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClientMIBConformance=_WwpMultiDhcpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,42,3))
_WwpMultiDhcpClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClientMIBCompliances=_WwpMultiDhcpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,42,3,1))
_WwpMultiDhcpClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpMultiDhcpClientMIBGroups=_WwpMultiDhcpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,42,3,2))
mibBuilder.exportSymbols(_H,**{'wwpMultiDhcpClientMIB':wwpMultiDhcpClientMIB,'wwpMultiDhcpClientMIBObjects':wwpMultiDhcpClientMIBObjects,'wwpMultiDhcpClient':wwpMultiDhcpClient,'wwpMultiDhcpClientNumber':wwpMultiDhcpClientNumber,'wwpMultiDhcpClientTable':wwpMultiDhcpClientTable,'wwpMultiDhcpClientEntry':wwpMultiDhcpClientEntry,_I:wwpDhcpIfIndex,'wwpDhcpIfName':wwpDhcpIfName,'wwpDhcpStatus':wwpDhcpStatus,'wwpDhcpState':wwpDhcpState,'wwpDhcpLeaseTimeRequested':wwpDhcpLeaseTimeRequested,'wwpDhcpLeaseOffered':wwpDhcpLeaseOffered,'wwpDhcpLeaseRemaining':wwpDhcpLeaseRemaining,'wwpDhcpDiscoveryMsgInterval':wwpDhcpDiscoveryMsgInterval,'wwpDhcpRenewalTime':wwpDhcpRenewalTime,'wwpDhcpRebindingTime':wwpDhcpRebindingTime,'wwpDhcpServerAddress':wwpDhcpServerAddress,'wwpDhcpRenewLease':wwpDhcpRenewLease,'wwpDhcpReleaseLease':wwpDhcpReleaseLease,'wwpMultiDhcpClientMIBNotificationPrefix':wwpMultiDhcpClientMIBNotificationPrefix,'wwpMultiDhcpClientMIBNotifications':wwpMultiDhcpClientMIBNotifications,'wwpMultiDhcpClientMIBConformance':wwpMultiDhcpClientMIBConformance,'wwpMultiDhcpClientMIBCompliances':wwpMultiDhcpClientMIBCompliances,'wwpMultiDhcpClientMIBGroups':wwpMultiDhcpClientMIBGroups})