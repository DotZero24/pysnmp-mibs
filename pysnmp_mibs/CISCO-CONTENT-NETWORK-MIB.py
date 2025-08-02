_U='ccnNotifGroupRev1'
_T='ccnNotifGroup'
_S='ccnNotifOnline'
_R='ccnNotifWaitingForCdm'
_Q='ccnNotifNeedsAttention'
_P='ccnNotifOffline'
_O='ccnNotifServerStop'
_N='ccnNotifServerStart'
_M='ccnReportAcctCacheMissRate'
_L='ccnReportAcctCacheHitRate'
_K='ccnReportAcctObjectsCached'
_J='ccnReportAcctBytesServed'
_I='ccnReportDnsRequests'
_H='ccnReportDnsClientCount'
_G='ccnReportDnsRequestRate'
_F='objects-per-minute'
_E='ccnReportingGroup'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-CONTENT-NETWORK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoContentNetworkMIB=ModuleIdentity((1,3,6,1,4,1,9,9,216))
if mibBuilder.loadTexts:ciscoContentNetworkMIB.setRevisions(('2001-10-11 18:25','2001-05-23 21:34'))
_CiscoContentNetworkMIBObjects_ObjectIdentity=ObjectIdentity
ciscoContentNetworkMIBObjects=_CiscoContentNetworkMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,216,1))
_CcnReport_ObjectIdentity=ObjectIdentity
ccnReport=_CcnReport_ObjectIdentity((1,3,6,1,4,1,9,9,216,1,1))
_CcnReportDns_ObjectIdentity=ObjectIdentity
ccnReportDns=_CcnReportDns_ObjectIdentity((1,3,6,1,4,1,9,9,216,1,1,1))
_CcnReportDnsRequestRate_Type=Gauge32
_CcnReportDnsRequestRate_Object=MibScalar
ccnReportDnsRequestRate=_CcnReportDnsRequestRate_Object((1,3,6,1,4,1,9,9,216,1,1,1,1),_CcnReportDnsRequestRate_Type())
ccnReportDnsRequestRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportDnsRequestRate.setStatus(_B)
if mibBuilder.loadTexts:ccnReportDnsRequestRate.setUnits('requests-per-second')
_CcnReportDnsClientCount_Type=ZeroBasedCounter32
_CcnReportDnsClientCount_Object=MibScalar
ccnReportDnsClientCount=_CcnReportDnsClientCount_Object((1,3,6,1,4,1,9,9,216,1,1,1,2),_CcnReportDnsClientCount_Type())
ccnReportDnsClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportDnsClientCount.setStatus(_B)
if mibBuilder.loadTexts:ccnReportDnsClientCount.setUnits('clients')
_CcnReportDnsRequests_Type=ZeroBasedCounter32
_CcnReportDnsRequests_Object=MibScalar
ccnReportDnsRequests=_CcnReportDnsRequests_Object((1,3,6,1,4,1,9,9,216,1,1,1,3),_CcnReportDnsRequests_Type())
ccnReportDnsRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportDnsRequests.setStatus(_B)
if mibBuilder.loadTexts:ccnReportDnsRequests.setUnits('requests')
_CcnReportAcct_ObjectIdentity=ObjectIdentity
ccnReportAcct=_CcnReportAcct_ObjectIdentity((1,3,6,1,4,1,9,9,216,1,1,2))
_CcnReportAcctBytesServed_Type=ZeroBasedCounter32
_CcnReportAcctBytesServed_Object=MibScalar
ccnReportAcctBytesServed=_CcnReportAcctBytesServed_Object((1,3,6,1,4,1,9,9,216,1,1,2,1),_CcnReportAcctBytesServed_Type())
ccnReportAcctBytesServed.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportAcctBytesServed.setStatus(_B)
if mibBuilder.loadTexts:ccnReportAcctBytesServed.setUnits('bytes')
_CcnReportAcctObjectsCached_Type=Gauge32
_CcnReportAcctObjectsCached_Object=MibScalar
ccnReportAcctObjectsCached=_CcnReportAcctObjectsCached_Object((1,3,6,1,4,1,9,9,216,1,1,2,2),_CcnReportAcctObjectsCached_Type())
ccnReportAcctObjectsCached.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportAcctObjectsCached.setStatus(_B)
if mibBuilder.loadTexts:ccnReportAcctObjectsCached.setUnits('objects')
_CcnReportAcctCacheHitRate_Type=Gauge32
_CcnReportAcctCacheHitRate_Object=MibScalar
ccnReportAcctCacheHitRate=_CcnReportAcctCacheHitRate_Object((1,3,6,1,4,1,9,9,216,1,1,2,3),_CcnReportAcctCacheHitRate_Type())
ccnReportAcctCacheHitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportAcctCacheHitRate.setStatus(_B)
if mibBuilder.loadTexts:ccnReportAcctCacheHitRate.setUnits(_F)
_CcnReportAcctCacheMissRate_Type=Gauge32
_CcnReportAcctCacheMissRate_Object=MibScalar
ccnReportAcctCacheMissRate=_CcnReportAcctCacheMissRate_Object((1,3,6,1,4,1,9,9,216,1,1,2,4),_CcnReportAcctCacheMissRate_Type())
ccnReportAcctCacheMissRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccnReportAcctCacheMissRate.setStatus(_B)
if mibBuilder.loadTexts:ccnReportAcctCacheMissRate.setUnits(_F)
_CiscoContentNetworkMIBNotif_ObjectIdentity=ObjectIdentity
ciscoContentNetworkMIBNotif=_CiscoContentNetworkMIBNotif_ObjectIdentity((1,3,6,1,4,1,9,9,216,2))
_CcnNotifications_ObjectIdentity=ObjectIdentity
ccnNotifications=_CcnNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,216,2,0))
_CcnMIBConformance_ObjectIdentity=ObjectIdentity
ccnMIBConformance=_CcnMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,216,3))
_CcnMIBCompliances_ObjectIdentity=ObjectIdentity
ccnMIBCompliances=_CcnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,216,3,1))
_CcnMIBGroups_ObjectIdentity=ObjectIdentity
ccnMIBGroups=_CcnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,216,3,2))
ccnReportingGroup=ObjectGroup((1,3,6,1,4,1,9,9,216,3,2,1))
ccnReportingGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ccnReportingGroup.setStatus(_B)
ccnNotifServerStart=NotificationType((1,3,6,1,4,1,9,9,216,2,0,1))
if mibBuilder.loadTexts:ccnNotifServerStart.setStatus(_D)
ccnNotifServerStop=NotificationType((1,3,6,1,4,1,9,9,216,2,0,2))
if mibBuilder.loadTexts:ccnNotifServerStop.setStatus(_D)
ccnNotifOffline=NotificationType((1,3,6,1,4,1,9,9,216,2,0,3))
if mibBuilder.loadTexts:ccnNotifOffline.setStatus(_B)
ccnNotifNeedsAttention=NotificationType((1,3,6,1,4,1,9,9,216,2,0,4))
if mibBuilder.loadTexts:ccnNotifNeedsAttention.setStatus(_B)
ccnNotifWaitingForCdm=NotificationType((1,3,6,1,4,1,9,9,216,2,0,5))
if mibBuilder.loadTexts:ccnNotifWaitingForCdm.setStatus(_B)
ccnNotifOnline=NotificationType((1,3,6,1,4,1,9,9,216,2,0,6))
if mibBuilder.loadTexts:ccnNotifOnline.setStatus(_B)
ccnNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,216,3,2,2))
ccnNotifGroup.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ccnNotifGroup.setStatus(_D)
ccnNotifGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,216,3,2,3))
ccnNotifGroupRev1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ccnNotifGroupRev1.setStatus(_B)
ccnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,216,3,1,1))
ccnMIBCompliance.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:ccnMIBCompliance.setStatus(_D)
ccnMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,216,3,1,2))
ccnMIBComplianceRev1.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:ccnMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoContentNetworkMIB':ciscoContentNetworkMIB,'ciscoContentNetworkMIBObjects':ciscoContentNetworkMIBObjects,'ccnReport':ccnReport,'ccnReportDns':ccnReportDns,_G:ccnReportDnsRequestRate,_H:ccnReportDnsClientCount,_I:ccnReportDnsRequests,'ccnReportAcct':ccnReportAcct,_J:ccnReportAcctBytesServed,_K:ccnReportAcctObjectsCached,_L:ccnReportAcctCacheHitRate,_M:ccnReportAcctCacheMissRate,'ciscoContentNetworkMIBNotif':ciscoContentNetworkMIBNotif,'ccnNotifications':ccnNotifications,_N:ccnNotifServerStart,_O:ccnNotifServerStop,_P:ccnNotifOffline,_Q:ccnNotifNeedsAttention,_R:ccnNotifWaitingForCdm,_S:ccnNotifOnline,'ccnMIBConformance':ccnMIBConformance,'ccnMIBCompliances':ccnMIBCompliances,'ccnMIBCompliance':ccnMIBCompliance,'ccnMIBComplianceRev1':ccnMIBComplianceRev1,'ccnMIBGroups':ccnMIBGroups,_E:ccnReportingGroup,_T:ccnNotifGroup,_U:ccnNotifGroupRev1})