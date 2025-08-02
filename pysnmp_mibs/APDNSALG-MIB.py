_l='apDnsAlgSvrConstraintStateChangeClearTrap'
_k='apDnsAlgSvrConstraintStateChangeTrap'
_j='apDnsAlgConstraintStateChangeClearTrap'
_i='apDnsAlgConstraintStateChangeTrap'
_h='apDnsAlgStatusChangeClearTrap'
_g='apDnsAlgStatusChangeTrap'
_f='apDnsAlgMaxBurstRate'
_e='apDnsAlgMaxLatency'
_d='apDnsAlgAvgLatency'
_c='apDnsAlgTotalOtherFailures'
_b='apDnsAlgCurrentOtherFailures'
_a='apDnsAlgTotalBadStatus'
_Z='apDnsAlgCurrentBadStatus'
_Y='apDnsAlgTotalTimeOut'
_X='apDnsAlgCurrentTimeOut'
_W='apDnsAlgTotalNotFound'
_V='apDnsAlgCurrentNotFound'
_U='apDnsAlgTotalSucess'
_T='apDnsAlgCurrentSucess'
_S='apDnsAlgTotalQueries'
_R='apDnsAlgCurrentQueries'
_Q='apDnsAlgClientRealmName'
_P='apDNSALGDomainSuffix'
_O='inservice'
_N='apDnsAlgClientRealmIndex'
_M='apDNSALGServerIndex'
_L='apDNSALGConfigIndex'
_K='apDNSALGServerStatus'
_J='accessible-for-notify'
_I='apDNSALGConstraintsStatus'
_H='DisplayString'
_G='apDNSALGServerRealm'
_F='Integer32'
_E='apDNSALGServerIpAddress'
_D='apDNSALGConfigName'
_C='read-only'
_B='current'
_A='APDNSALG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ApHardwareModuleFamily,ApRedundancyState,ApTransportType=mibBuilder.importSymbols('ACMEPACKET-TC','ApHardwareModuleFamily','ApRedundancyState','ApTransportType')
SysMgmtPercentage,=mibBuilder.importSymbols('APSYSMGMT-MIB','SysMgmtPercentage')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion,InetZoneIndex=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetVersion','InetZoneIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
apDNSALGModule=ModuleIdentity((1,3,6,1,4,1,9148,3,14))
_ApDNSALGMIBObjects_ObjectIdentity=ObjectIdentity
apDNSALGMIBObjects=_ApDNSALGMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,14,1))
_ApDNSALGMIBGeneralObjects_ObjectIdentity=ObjectIdentity
apDNSALGMIBGeneralObjects=_ApDNSALGMIBGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,14,1,1))
_ApDNSALGMIBTabularObjects_ObjectIdentity=ObjectIdentity
apDNSALGMIBTabularObjects=_ApDNSALGMIBTabularObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,14,1,2))
_ApDNSALGServerStatusTable_Object=MibTable
apDNSALGServerStatusTable=_ApDNSALGServerStatusTable_Object((1,3,6,1,4,1,9148,3,14,1,2,1))
if mibBuilder.loadTexts:apDNSALGServerStatusTable.setStatus(_B)
_ApDNSALGServerStatusEntry_Object=MibTableRow
apDNSALGServerStatusEntry=_ApDNSALGServerStatusEntry_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1))
apDNSALGServerStatusEntry.setIndexNames((0,_A,_L),(0,_A,_M),(0,_A,_E))
if mibBuilder.loadTexts:apDNSALGServerStatusEntry.setStatus(_B)
class _ApDNSALGConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApDNSALGConfigIndex_Type.__name__=_F
_ApDNSALGConfigIndex_Object=MibTableColumn
apDNSALGConfigIndex=_ApDNSALGConfigIndex_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,1),_ApDNSALGConfigIndex_Type())
apDNSALGConfigIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:apDNSALGConfigIndex.setStatus(_B)
class _ApDNSALGServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApDNSALGServerIndex_Type.__name__=_F
_ApDNSALGServerIndex_Object=MibTableColumn
apDNSALGServerIndex=_ApDNSALGServerIndex_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,2),_ApDNSALGServerIndex_Type())
apDNSALGServerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:apDNSALGServerIndex.setStatus(_B)
class _ApDNSALGConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApDNSALGConfigName_Type.__name__=_H
_ApDNSALGConfigName_Object=MibTableColumn
apDNSALGConfigName=_ApDNSALGConfigName_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,4),_ApDNSALGConfigName_Type())
apDNSALGConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSALGConfigName.setStatus(_B)
class _ApDNSALGServerRealm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApDNSALGServerRealm_Type.__name__=_H
_ApDNSALGServerRealm_Object=MibTableColumn
apDNSALGServerRealm=_ApDNSALGServerRealm_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,5),_ApDNSALGServerRealm_Type())
apDNSALGServerRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSALGServerRealm.setStatus(_B)
class _ApDNSALGDomainSuffix_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApDNSALGDomainSuffix_Type.__name__=_H
_ApDNSALGDomainSuffix_Object=MibTableColumn
apDNSALGDomainSuffix=_ApDNSALGDomainSuffix_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,6),_ApDNSALGDomainSuffix_Type())
apDNSALGDomainSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSALGDomainSuffix.setStatus(_B)
_ApDNSALGServerIpAddress_Type=IpAddress
_ApDNSALGServerIpAddress_Object=MibTableColumn
apDNSALGServerIpAddress=_ApDNSALGServerIpAddress_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,7),_ApDNSALGServerIpAddress_Type())
apDNSALGServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSALGServerIpAddress.setStatus(_B)
class _ApDNSALGServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('lowerpriority',1),('oosunreachable',2)))
_ApDNSALGServerStatus_Type.__name__=_F
_ApDNSALGServerStatus_Object=MibTableColumn
apDNSALGServerStatus=_ApDNSALGServerStatus_Object((1,3,6,1,4,1,9148,3,14,1,2,1,1,8),_ApDNSALGServerStatus_Type())
apDNSALGServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSALGServerStatus.setStatus(_B)
_ApDNSALGStatsTable_Object=MibTable
apDNSALGStatsTable=_ApDNSALGStatsTable_Object((1,3,6,1,4,1,9148,3,14,1,2,2))
if mibBuilder.loadTexts:apDNSALGStatsTable.setStatus(_B)
_ApDnsALGStatsEntry_Object=MibTableRow
apDnsALGStatsEntry=_ApDnsALGStatsEntry_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1))
apDnsALGStatsEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:apDnsALGStatsEntry.setStatus(_B)
class _ApDnsAlgClientRealmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApDnsAlgClientRealmIndex_Type.__name__=_F
_ApDnsAlgClientRealmIndex_Object=MibTableColumn
apDnsAlgClientRealmIndex=_ApDnsAlgClientRealmIndex_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,1),_ApDnsAlgClientRealmIndex_Type())
apDnsAlgClientRealmIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:apDnsAlgClientRealmIndex.setStatus(_B)
class _ApDnsAlgClientRealmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ApDnsAlgClientRealmName_Type.__name__=_H
_ApDnsAlgClientRealmName_Object=MibTableColumn
apDnsAlgClientRealmName=_ApDnsAlgClientRealmName_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,2),_ApDnsAlgClientRealmName_Type())
apDnsAlgClientRealmName.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgClientRealmName.setStatus(_B)
_ApDnsAlgCurrentQueries_Type=Gauge32
_ApDnsAlgCurrentQueries_Object=MibTableColumn
apDnsAlgCurrentQueries=_ApDnsAlgCurrentQueries_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,3),_ApDnsAlgCurrentQueries_Type())
apDnsAlgCurrentQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgCurrentQueries.setStatus(_B)
_ApDnsAlgTotalQueries_Type=Counter32
_ApDnsAlgTotalQueries_Object=MibTableColumn
apDnsAlgTotalQueries=_ApDnsAlgTotalQueries_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,4),_ApDnsAlgTotalQueries_Type())
apDnsAlgTotalQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgTotalQueries.setStatus(_B)
_ApDnsAlgCurrentSucess_Type=Gauge32
_ApDnsAlgCurrentSucess_Object=MibTableColumn
apDnsAlgCurrentSucess=_ApDnsAlgCurrentSucess_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,5),_ApDnsAlgCurrentSucess_Type())
apDnsAlgCurrentSucess.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgCurrentSucess.setStatus(_B)
_ApDnsAlgTotalSucess_Type=Counter32
_ApDnsAlgTotalSucess_Object=MibTableColumn
apDnsAlgTotalSucess=_ApDnsAlgTotalSucess_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,6),_ApDnsAlgTotalSucess_Type())
apDnsAlgTotalSucess.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgTotalSucess.setStatus(_B)
_ApDnsAlgCurrentNotFound_Type=Gauge32
_ApDnsAlgCurrentNotFound_Object=MibTableColumn
apDnsAlgCurrentNotFound=_ApDnsAlgCurrentNotFound_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,7),_ApDnsAlgCurrentNotFound_Type())
apDnsAlgCurrentNotFound.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgCurrentNotFound.setStatus(_B)
_ApDnsAlgTotalNotFound_Type=Counter32
_ApDnsAlgTotalNotFound_Object=MibTableColumn
apDnsAlgTotalNotFound=_ApDnsAlgTotalNotFound_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,8),_ApDnsAlgTotalNotFound_Type())
apDnsAlgTotalNotFound.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgTotalNotFound.setStatus(_B)
_ApDnsAlgCurrentTimeOut_Type=Gauge32
_ApDnsAlgCurrentTimeOut_Object=MibTableColumn
apDnsAlgCurrentTimeOut=_ApDnsAlgCurrentTimeOut_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,9),_ApDnsAlgCurrentTimeOut_Type())
apDnsAlgCurrentTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgCurrentTimeOut.setStatus(_B)
_ApDnsAlgTotalTimeOut_Type=Counter32
_ApDnsAlgTotalTimeOut_Object=MibTableColumn
apDnsAlgTotalTimeOut=_ApDnsAlgTotalTimeOut_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,10),_ApDnsAlgTotalTimeOut_Type())
apDnsAlgTotalTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgTotalTimeOut.setStatus(_B)
_ApDnsAlgCurrentBadStatus_Type=Gauge32
_ApDnsAlgCurrentBadStatus_Object=MibTableColumn
apDnsAlgCurrentBadStatus=_ApDnsAlgCurrentBadStatus_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,11),_ApDnsAlgCurrentBadStatus_Type())
apDnsAlgCurrentBadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgCurrentBadStatus.setStatus(_B)
_ApDnsAlgTotalBadStatus_Type=Counter32
_ApDnsAlgTotalBadStatus_Object=MibTableColumn
apDnsAlgTotalBadStatus=_ApDnsAlgTotalBadStatus_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,12),_ApDnsAlgTotalBadStatus_Type())
apDnsAlgTotalBadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgTotalBadStatus.setStatus(_B)
_ApDnsAlgCurrentOtherFailures_Type=Gauge32
_ApDnsAlgCurrentOtherFailures_Object=MibTableColumn
apDnsAlgCurrentOtherFailures=_ApDnsAlgCurrentOtherFailures_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,13),_ApDnsAlgCurrentOtherFailures_Type())
apDnsAlgCurrentOtherFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgCurrentOtherFailures.setStatus(_B)
_ApDnsAlgTotalOtherFailures_Type=Counter32
_ApDnsAlgTotalOtherFailures_Object=MibTableColumn
apDnsAlgTotalOtherFailures=_ApDnsAlgTotalOtherFailures_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,14),_ApDnsAlgTotalOtherFailures_Type())
apDnsAlgTotalOtherFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgTotalOtherFailures.setStatus(_B)
_ApDnsAlgAvgLatency_Type=Unsigned32
_ApDnsAlgAvgLatency_Object=MibTableColumn
apDnsAlgAvgLatency=_ApDnsAlgAvgLatency_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,15),_ApDnsAlgAvgLatency_Type())
apDnsAlgAvgLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgAvgLatency.setStatus(_B)
_ApDnsAlgMaxLatency_Type=Unsigned32
_ApDnsAlgMaxLatency_Object=MibTableColumn
apDnsAlgMaxLatency=_ApDnsAlgMaxLatency_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,16),_ApDnsAlgMaxLatency_Type())
apDnsAlgMaxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgMaxLatency.setStatus(_B)
_ApDnsAlgMaxBurstRate_Type=Unsigned32
_ApDnsAlgMaxBurstRate_Object=MibTableColumn
apDnsAlgMaxBurstRate=_ApDnsAlgMaxBurstRate_Object((1,3,6,1,4,1,9148,3,14,1,2,2,1,17),_ApDnsAlgMaxBurstRate_Type())
apDnsAlgMaxBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:apDnsAlgMaxBurstRate.setStatus(_B)
_ApDNSALGNotificationObjects_ObjectIdentity=ObjectIdentity
apDNSALGNotificationObjects=_ApDNSALGNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,14,2))
_ApDNSALGNotifObjects_ObjectIdentity=ObjectIdentity
apDNSALGNotifObjects=_ApDNSALGNotifObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,14,2,1))
class _ApDNSALGConstraintsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('constraintsExceeded',1)))
_ApDNSALGConstraintsStatus_Type.__name__=_F
_ApDNSALGConstraintsStatus_Object=MibScalar
apDNSALGConstraintsStatus=_ApDNSALGConstraintsStatus_Object((1,3,6,1,4,1,9148,3,14,2,1,1),_ApDNSALGConstraintsStatus_Type())
apDNSALGConstraintsStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:apDNSALGConstraintsStatus.setStatus(_B)
_ApDNSALGNotifPrefix_ObjectIdentity=ObjectIdentity
apDNSALGNotifPrefix=_ApDNSALGNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,14,2,2))
_ApDNSALGNotifications_ObjectIdentity=ObjectIdentity
apDNSALGNotifications=_ApDNSALGNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,14,2,2,0))
_ApDNSALGConformance_ObjectIdentity=ObjectIdentity
apDNSALGConformance=_ApDNSALGConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,14,3))
_ApDNSALGObjectGroups_ObjectIdentity=ObjectIdentity
apDNSALGObjectGroups=_ApDNSALGObjectGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,14,3,1))
_ApDNSALGNotificationGroups_ObjectIdentity=ObjectIdentity
apDNSALGNotificationGroups=_ApDNSALGNotificationGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,14,3,2))
apDnsAlgServerStatusGroup=ObjectGroup((1,3,6,1,4,1,9148,3,14,3,1,1))
apDnsAlgServerStatusGroup.setObjects(*((_A,_L),(_A,_M),(_A,_D),(_A,_G),(_A,_P),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:apDnsAlgServerStatusGroup.setStatus(_B)
apDnsAlgStatsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,14,3,1,2))
apDnsAlgStatsGroup.setObjects(*((_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:apDnsAlgStatsGroup.setStatus(_B)
apDnsAlgStatusChangeTrap=NotificationType((1,3,6,1,4,1,9148,3,14,2,2,0,1))
apDnsAlgStatusChangeTrap.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:apDnsAlgStatusChangeTrap.setStatus(_B)
apDnsAlgStatusChangeClearTrap=NotificationType((1,3,6,1,4,1,9148,3,14,2,2,0,2))
apDnsAlgStatusChangeClearTrap.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:apDnsAlgStatusChangeClearTrap.setStatus(_B)
apDnsAlgConstraintStateChangeTrap=NotificationType((1,3,6,1,4,1,9148,3,14,2,2,0,3))
apDnsAlgConstraintStateChangeTrap.setObjects(*((_A,_D),(_A,_I)))
if mibBuilder.loadTexts:apDnsAlgConstraintStateChangeTrap.setStatus(_B)
apDnsAlgConstraintStateChangeClearTrap=NotificationType((1,3,6,1,4,1,9148,3,14,2,2,0,4))
apDnsAlgConstraintStateChangeClearTrap.setObjects(*((_A,_D),(_A,_I)))
if mibBuilder.loadTexts:apDnsAlgConstraintStateChangeClearTrap.setStatus(_B)
apDnsAlgSvrConstraintStateChangeTrap=NotificationType((1,3,6,1,4,1,9148,3,14,2,2,0,5))
apDnsAlgSvrConstraintStateChangeTrap.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:apDnsAlgSvrConstraintStateChangeTrap.setStatus(_B)
apDnsAlgSvrConstraintStateChangeClearTrap=NotificationType((1,3,6,1,4,1,9148,3,14,2,2,0,6))
apDnsAlgSvrConstraintStateChangeClearTrap.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:apDnsAlgSvrConstraintStateChangeClearTrap.setStatus(_B)
apDNSALGNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,14,3,2,1))
apDNSALGNotificationsGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:apDNSALGNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'apDNSALGModule':apDNSALGModule,'apDNSALGMIBObjects':apDNSALGMIBObjects,'apDNSALGMIBGeneralObjects':apDNSALGMIBGeneralObjects,'apDNSALGMIBTabularObjects':apDNSALGMIBTabularObjects,'apDNSALGServerStatusTable':apDNSALGServerStatusTable,'apDNSALGServerStatusEntry':apDNSALGServerStatusEntry,_L:apDNSALGConfigIndex,_M:apDNSALGServerIndex,_D:apDNSALGConfigName,_G:apDNSALGServerRealm,_P:apDNSALGDomainSuffix,_E:apDNSALGServerIpAddress,_K:apDNSALGServerStatus,'apDNSALGStatsTable':apDNSALGStatsTable,'apDnsALGStatsEntry':apDnsALGStatsEntry,_N:apDnsAlgClientRealmIndex,_Q:apDnsAlgClientRealmName,_R:apDnsAlgCurrentQueries,_S:apDnsAlgTotalQueries,_T:apDnsAlgCurrentSucess,_U:apDnsAlgTotalSucess,_V:apDnsAlgCurrentNotFound,_W:apDnsAlgTotalNotFound,_X:apDnsAlgCurrentTimeOut,_Y:apDnsAlgTotalTimeOut,_Z:apDnsAlgCurrentBadStatus,_a:apDnsAlgTotalBadStatus,_b:apDnsAlgCurrentOtherFailures,_c:apDnsAlgTotalOtherFailures,_d:apDnsAlgAvgLatency,_e:apDnsAlgMaxLatency,_f:apDnsAlgMaxBurstRate,'apDNSALGNotificationObjects':apDNSALGNotificationObjects,'apDNSALGNotifObjects':apDNSALGNotifObjects,_I:apDNSALGConstraintsStatus,'apDNSALGNotifPrefix':apDNSALGNotifPrefix,'apDNSALGNotifications':apDNSALGNotifications,_g:apDnsAlgStatusChangeTrap,_h:apDnsAlgStatusChangeClearTrap,_i:apDnsAlgConstraintStateChangeTrap,_j:apDnsAlgConstraintStateChangeClearTrap,_k:apDnsAlgSvrConstraintStateChangeTrap,_l:apDnsAlgSvrConstraintStateChangeClearTrap,'apDNSALGConformance':apDNSALGConformance,'apDNSALGObjectGroups':apDNSALGObjectGroups,'apDnsAlgServerStatusGroup':apDnsAlgServerStatusGroup,'apDnsAlgStatsGroup':apDnsAlgStatsGroup,'apDNSALGNotificationGroups':apDNSALGNotificationGroups,'apDNSALGNotificationsGroup':apDNSALGNotificationsGroup})