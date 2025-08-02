_M='bTWagGTPLowThreshold'
_L='bTWagGTPHighThreshold'
_K='bTWagPmip6StatsInterval'
_J='bTWagGnGpStatsInterval'
_I='bTWagGnGpSubsStatsInterval'
_H='bTWagS2aStatsInterval'
_G='bTWagS2aSubsStatsInterval'
_F='bTWagGTPMaxNumOfTunnels'
_E='accessible-for-notify'
_D='not-accessible'
_C='BENU-TWAG-STATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
benuTWagStatsMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,7))
if mibBuilder.loadTexts:benuTWagStatsMIB.setRevisions(('2016-07-19 00:00','2016-07-27 00:00'))
_BTWagNotifications_ObjectIdentity=ObjectIdentity
bTWagNotifications=_BTWagNotifications_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,0))
if mibBuilder.loadTexts:bTWagNotifications.setStatus(_A)
_BTWagS2aSubscriberMIBObjects_ObjectIdentity=ObjectIdentity
bTWagS2aSubscriberMIBObjects=_BTWagS2aSubscriberMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,1))
if mibBuilder.loadTexts:bTWagS2aSubscriberMIBObjects.setStatus(_A)
_BTWagNumCurrentSecureSSIDS2aSubscribers_Type=Unsigned32
_BTWagNumCurrentSecureSSIDS2aSubscribers_Object=MibScalar
bTWagNumCurrentSecureSSIDS2aSubscribers=_BTWagNumCurrentSecureSSIDS2aSubscribers_Object((1,3,6,1,4,1,39406,2,1,7,1,1),_BTWagNumCurrentSecureSSIDS2aSubscribers_Type())
bTWagNumCurrentSecureSSIDS2aSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagNumCurrentSecureSSIDS2aSubscribers.setStatus(_A)
_BTWagNumPreAuthenticatedS2aSubscribers_Type=Unsigned32
_BTWagNumPreAuthenticatedS2aSubscribers_Object=MibScalar
bTWagNumPreAuthenticatedS2aSubscribers=_BTWagNumPreAuthenticatedS2aSubscribers_Object((1,3,6,1,4,1,39406,2,1,7,1,2),_BTWagNumPreAuthenticatedS2aSubscribers_Type())
bTWagNumPreAuthenticatedS2aSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagNumPreAuthenticatedS2aSubscribers.setStatus(_A)
_BTWagS2aSubscriberTable_Object=MibTable
bTWagS2aSubscriberTable=_BTWagS2aSubscriberTable_Object((1,3,6,1,4,1,39406,2,1,7,1,3))
if mibBuilder.loadTexts:bTWagS2aSubscriberTable.setStatus(_A)
_BTWagS2aSubscriberEntry_Object=MibTableRow
bTWagS2aSubscriberEntry=_BTWagS2aSubscriberEntry_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1))
bTWagS2aSubscriberEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:bTWagS2aSubscriberEntry.setStatus(_A)
_BTWagS2aSubsStatsInterval_Type=Integer32
_BTWagS2aSubsStatsInterval_Object=MibTableColumn
bTWagS2aSubsStatsInterval=_BTWagS2aSubsStatsInterval_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,1),_BTWagS2aSubsStatsInterval_Type())
bTWagS2aSubsStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bTWagS2aSubsStatsInterval.setStatus(_A)
_BTWagS2aSubsIntervalDuration_Type=Integer32
_BTWagS2aSubsIntervalDuration_Object=MibTableColumn
bTWagS2aSubsIntervalDuration=_BTWagS2aSubsIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,2),_BTWagS2aSubsIntervalDuration_Type())
bTWagS2aSubsIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsIntervalDuration.setStatus(_A)
_BTWagSecureSSIDS2aSubsAdded_Type=Unsigned32
_BTWagSecureSSIDS2aSubsAdded_Object=MibTableColumn
bTWagSecureSSIDS2aSubsAdded=_BTWagSecureSSIDS2aSubsAdded_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,3),_BTWagSecureSSIDS2aSubsAdded_Type())
bTWagSecureSSIDS2aSubsAdded.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagSecureSSIDS2aSubsAdded.setStatus(_A)
_BTWagPreAuthenticatedS2aSubsAdded_Type=Unsigned32
_BTWagPreAuthenticatedS2aSubsAdded_Object=MibTableColumn
bTWagPreAuthenticatedS2aSubsAdded=_BTWagPreAuthenticatedS2aSubsAdded_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,4),_BTWagPreAuthenticatedS2aSubsAdded_Type())
bTWagPreAuthenticatedS2aSubsAdded.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPreAuthenticatedS2aSubsAdded.setStatus(_A)
_BTWagS2aSubsDeletionsByDMinitiatedByPGW_Type=Unsigned32
_BTWagS2aSubsDeletionsByDMinitiatedByPGW_Object=MibTableColumn
bTWagS2aSubsDeletionsByDMinitiatedByPGW=_BTWagS2aSubsDeletionsByDMinitiatedByPGW_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,5),_BTWagS2aSubsDeletionsByDMinitiatedByPGW_Type())
bTWagS2aSubsDeletionsByDMinitiatedByPGW.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsDeletionsByDMinitiatedByPGW.setStatus(_A)
_BTWagS2aSubsGtpSessionCreateFailed_Type=Unsigned32
_BTWagS2aSubsGtpSessionCreateFailed_Object=MibTableColumn
bTWagS2aSubsGtpSessionCreateFailed=_BTWagS2aSubsGtpSessionCreateFailed_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,6),_BTWagS2aSubsGtpSessionCreateFailed_Type())
bTWagS2aSubsGtpSessionCreateFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsGtpSessionCreateFailed.setStatus(_A)
_BTWagS2aSubsCSRQSendFailed_Type=Unsigned32
_BTWagS2aSubsCSRQSendFailed_Object=MibTableColumn
bTWagS2aSubsCSRQSendFailed=_BTWagS2aSubsCSRQSendFailed_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,7),_BTWagS2aSubsCSRQSendFailed_Type())
bTWagS2aSubsCSRQSendFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsCSRQSendFailed.setStatus(_A)
_BTWagS2aSubsInvalidGtpVersion_Type=Unsigned32
_BTWagS2aSubsInvalidGtpVersion_Object=MibTableColumn
bTWagS2aSubsInvalidGtpVersion=_BTWagS2aSubsInvalidGtpVersion_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,9),_BTWagS2aSubsInvalidGtpVersion_Type())
bTWagS2aSubsInvalidGtpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsInvalidGtpVersion.setStatus(_A)
_BTWagS2aSubsRadiusMissingMandatoryParams_Type=Unsigned32
_BTWagS2aSubsRadiusMissingMandatoryParams_Object=MibTableColumn
bTWagS2aSubsRadiusMissingMandatoryParams=_BTWagS2aSubsRadiusMissingMandatoryParams_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,10),_BTWagS2aSubsRadiusMissingMandatoryParams_Type())
bTWagS2aSubsRadiusMissingMandatoryParams.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusMissingMandatoryParams.setStatus(_A)
_BTWagS2aSubsRadiusInvalidPGWIPAddr_Type=Unsigned32
_BTWagS2aSubsRadiusInvalidPGWIPAddr_Object=MibTableColumn
bTWagS2aSubsRadiusInvalidPGWIPAddr=_BTWagS2aSubsRadiusInvalidPGWIPAddr_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,11),_BTWagS2aSubsRadiusInvalidPGWIPAddr_Type())
bTWagS2aSubsRadiusInvalidPGWIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusInvalidPGWIPAddr.setStatus(_A)
_BTWagS2aSubsRadiusMSISDN_Type=Unsigned32
_BTWagS2aSubsRadiusMSISDN_Object=MibTableColumn
bTWagS2aSubsRadiusMSISDN=_BTWagS2aSubsRadiusMSISDN_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,12),_BTWagS2aSubsRadiusMSISDN_Type())
bTWagS2aSubsRadiusMSISDN.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusMSISDN.setStatus(_A)
_BTWagS2aSubsRadiusQoSProfile_Type=Unsigned32
_BTWagS2aSubsRadiusQoSProfile_Object=MibTableColumn
bTWagS2aSubsRadiusQoSProfile=_BTWagS2aSubsRadiusQoSProfile_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,13),_BTWagS2aSubsRadiusQoSProfile_Type())
bTWagS2aSubsRadiusQoSProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusQoSProfile.setStatus(_A)
_BTWagS2aSubsRadiusGBRQoS_Type=Unsigned32
_BTWagS2aSubsRadiusGBRQoS_Object=MibTableColumn
bTWagS2aSubsRadiusGBRQoS=_BTWagS2aSubsRadiusGBRQoS_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,14),_BTWagS2aSubsRadiusGBRQoS_Type())
bTWagS2aSubsRadiusGBRQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusGBRQoS.setStatus(_A)
_BTWagS2aSubsRadiusNonGBRQoS_Type=Unsigned32
_BTWagS2aSubsRadiusNonGBRQoS_Object=MibTableColumn
bTWagS2aSubsRadiusNonGBRQoS=_BTWagS2aSubsRadiusNonGBRQoS_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,15),_BTWagS2aSubsRadiusNonGBRQoS_Type())
bTWagS2aSubsRadiusNonGBRQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusNonGBRQoS.setStatus(_A)
_BTWagS2aSubsGtpIPAddFailed_Type=Unsigned32
_BTWagS2aSubsGtpIPAddFailed_Object=MibTableColumn
bTWagS2aSubsGtpIPAddFailed=_BTWagS2aSubsGtpIPAddFailed_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,16),_BTWagS2aSubsGtpIPAddFailed_Type())
bTWagS2aSubsGtpIPAddFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsGtpIPAddFailed.setStatus(_A)
_BTWagS2aSubsRadiusEapAkaHash_Type=Unsigned32
_BTWagS2aSubsRadiusEapAkaHash_Object=MibTableColumn
bTWagS2aSubsRadiusEapAkaHash=_BTWagS2aSubsRadiusEapAkaHash_Object((1,3,6,1,4,1,39406,2,1,7,1,3,1,17),_BTWagS2aSubsRadiusEapAkaHash_Type())
bTWagS2aSubsRadiusEapAkaHash.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSubsRadiusEapAkaHash.setStatus(_A)
_BTWagS2aSubscriberNotifObjects_ObjectIdentity=ObjectIdentity
bTWagS2aSubscriberNotifObjects=_BTWagS2aSubscriberNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,2))
if mibBuilder.loadTexts:bTWagS2aSubscriberNotifObjects.setStatus(_A)
_BTWagS2aStatsMIBObjects_ObjectIdentity=ObjectIdentity
bTWagS2aStatsMIBObjects=_BTWagS2aStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,3))
if mibBuilder.loadTexts:bTWagS2aStatsMIBObjects.setStatus(_A)
_BTWagS2aTable_Object=MibTable
bTWagS2aTable=_BTWagS2aTable_Object((1,3,6,1,4,1,39406,2,1,7,3,1))
if mibBuilder.loadTexts:bTWagS2aTable.setStatus(_A)
_BTWagS2aEntry_Object=MibTableRow
bTWagS2aEntry=_BTWagS2aEntry_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1))
bTWagS2aEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:bTWagS2aEntry.setStatus(_A)
_BTWagS2aStatsInterval_Type=Integer32
_BTWagS2aStatsInterval_Object=MibTableColumn
bTWagS2aStatsInterval=_BTWagS2aStatsInterval_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,1),_BTWagS2aStatsInterval_Type())
bTWagS2aStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bTWagS2aStatsInterval.setStatus(_A)
_BTWagS2aIntervalDuration_Type=Integer32
_BTWagS2aIntervalDuration_Object=MibTableColumn
bTWagS2aIntervalDuration=_BTWagS2aIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,2),_BTWagS2aIntervalDuration_Type())
bTWagS2aIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aIntervalDuration.setStatus(_A)
_BTWagS2aSessCreateReqSent_Type=Unsigned32
_BTWagS2aSessCreateReqSent_Object=MibTableColumn
bTWagS2aSessCreateReqSent=_BTWagS2aSessCreateReqSent_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,3),_BTWagS2aSessCreateReqSent_Type())
bTWagS2aSessCreateReqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessCreateReqSent.setStatus(_A)
_BTWagS2aSessCreateRespRcvd_Type=Unsigned32
_BTWagS2aSessCreateRespRcvd_Object=MibTableColumn
bTWagS2aSessCreateRespRcvd=_BTWagS2aSessCreateRespRcvd_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,4),_BTWagS2aSessCreateRespRcvd_Type())
bTWagS2aSessCreateRespRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessCreateRespRcvd.setStatus(_A)
_BTWagS2aSessCreateRespAccepted_Type=Unsigned32
_BTWagS2aSessCreateRespAccepted_Object=MibTableColumn
bTWagS2aSessCreateRespAccepted=_BTWagS2aSessCreateRespAccepted_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,5),_BTWagS2aSessCreateRespAccepted_Type())
bTWagS2aSessCreateRespAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessCreateRespAccepted.setStatus(_A)
_BTWagS2aSessCreateRespRej_Type=Unsigned32
_BTWagS2aSessCreateRespRej_Object=MibTableColumn
bTWagS2aSessCreateRespRej=_BTWagS2aSessCreateRespRej_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,6),_BTWagS2aSessCreateRespRej_Type())
bTWagS2aSessCreateRespRej.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessCreateRespRej.setStatus(_A)
_BTWagS2aSessDelReqSent_Type=Unsigned32
_BTWagS2aSessDelReqSent_Object=MibTableColumn
bTWagS2aSessDelReqSent=_BTWagS2aSessDelReqSent_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,7),_BTWagS2aSessDelReqSent_Type())
bTWagS2aSessDelReqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessDelReqSent.setStatus(_A)
_BTWagS2aSessDelRespRcvd_Type=Unsigned32
_BTWagS2aSessDelRespRcvd_Object=MibTableColumn
bTWagS2aSessDelRespRcvd=_BTWagS2aSessDelRespRcvd_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,8),_BTWagS2aSessDelRespRcvd_Type())
bTWagS2aSessDelRespRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessDelRespRcvd.setStatus(_A)
_BTWagS2aSessDelRespRejRcvd_Type=Unsigned32
_BTWagS2aSessDelRespRejRcvd_Object=MibTableColumn
bTWagS2aSessDelRespRejRcvd=_BTWagS2aSessDelRespRejRcvd_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,9),_BTWagS2aSessDelRespRejRcvd_Type())
bTWagS2aSessDelRespRejRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aSessDelRespRejRcvd.setStatus(_A)
_BTWagS2aDBRQRcvd_Type=Unsigned32
_BTWagS2aDBRQRcvd_Object=MibTableColumn
bTWagS2aDBRQRcvd=_BTWagS2aDBRQRcvd_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,10),_BTWagS2aDBRQRcvd_Type())
bTWagS2aDBRQRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aDBRQRcvd.setStatus(_A)
_BTWagS2aDBRPSent_Type=Unsigned32
_BTWagS2aDBRPSent_Object=MibTableColumn
bTWagS2aDBRPSent=_BTWagS2aDBRPSent_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,11),_BTWagS2aDBRPSent_Type())
bTWagS2aDBRPSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aDBRPSent.setStatus(_A)
_BTWagS2aCBRQRcvd_Type=Unsigned32
_BTWagS2aCBRQRcvd_Object=MibTableColumn
bTWagS2aCBRQRcvd=_BTWagS2aCBRQRcvd_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,12),_BTWagS2aCBRQRcvd_Type())
bTWagS2aCBRQRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aCBRQRcvd.setStatus(_A)
_BTWagS2aCBRPSent_Type=Unsigned32
_BTWagS2aCBRPSent_Object=MibTableColumn
bTWagS2aCBRPSent=_BTWagS2aCBRPSent_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,13),_BTWagS2aCBRPSent_Type())
bTWagS2aCBRPSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aCBRPSent.setStatus(_A)
_BTWagS2aUBRQRcvd_Type=Unsigned32
_BTWagS2aUBRQRcvd_Object=MibTableColumn
bTWagS2aUBRQRcvd=_BTWagS2aUBRQRcvd_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,14),_BTWagS2aUBRQRcvd_Type())
bTWagS2aUBRQRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aUBRQRcvd.setStatus(_A)
_BTWagS2aUBRPSent_Type=Unsigned32
_BTWagS2aUBRPSent_Object=MibTableColumn
bTWagS2aUBRPSent=_BTWagS2aUBRPSent_Object((1,3,6,1,4,1,39406,2,1,7,3,1,1,15),_BTWagS2aUBRPSent_Type())
bTWagS2aUBRPSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagS2aUBRPSent.setStatus(_A)
_BTWagS2aNotifObjects_ObjectIdentity=ObjectIdentity
bTWagS2aNotifObjects=_BTWagS2aNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,4))
if mibBuilder.loadTexts:bTWagS2aNotifObjects.setStatus(_A)
_BTWagGTPStatsMIBObjects_ObjectIdentity=ObjectIdentity
bTWagGTPStatsMIBObjects=_BTWagGTPStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,5))
if mibBuilder.loadTexts:bTWagGTPStatsMIBObjects.setStatus(_A)
_BTWagGTPCurrentNumOfTunnels_Type=Unsigned32
_BTWagGTPCurrentNumOfTunnels_Object=MibScalar
bTWagGTPCurrentNumOfTunnels=_BTWagGTPCurrentNumOfTunnels_Object((1,3,6,1,4,1,39406,2,1,7,5,1),_BTWagGTPCurrentNumOfTunnels_Type())
bTWagGTPCurrentNumOfTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGTPCurrentNumOfTunnels.setStatus(_A)
_BTWagGTPNotifObjects_ObjectIdentity=ObjectIdentity
bTWagGTPNotifObjects=_BTWagGTPNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,6))
if mibBuilder.loadTexts:bTWagGTPNotifObjects.setStatus(_A)
_BTWagGTPMaxNumOfTunnels_Type=Unsigned32
_BTWagGTPMaxNumOfTunnels_Object=MibScalar
bTWagGTPMaxNumOfTunnels=_BTWagGTPMaxNumOfTunnels_Object((1,3,6,1,4,1,39406,2,1,7,6,1),_BTWagGTPMaxNumOfTunnels_Type())
bTWagGTPMaxNumOfTunnels.setMaxAccess(_E)
if mibBuilder.loadTexts:bTWagGTPMaxNumOfTunnels.setStatus(_A)
_BTWagGTPHighThreshold_Type=Unsigned32
_BTWagGTPHighThreshold_Object=MibScalar
bTWagGTPHighThreshold=_BTWagGTPHighThreshold_Object((1,3,6,1,4,1,39406,2,1,7,6,2),_BTWagGTPHighThreshold_Type())
bTWagGTPHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:bTWagGTPHighThreshold.setStatus(_A)
_BTWagGTPLowThreshold_Type=Unsigned32
_BTWagGTPLowThreshold_Object=MibScalar
bTWagGTPLowThreshold=_BTWagGTPLowThreshold_Object((1,3,6,1,4,1,39406,2,1,7,6,3),_BTWagGTPLowThreshold_Type())
bTWagGTPLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:bTWagGTPLowThreshold.setStatus(_A)
_BTWagGnGpSubscriberMIBObjects_ObjectIdentity=ObjectIdentity
bTWagGnGpSubscriberMIBObjects=_BTWagGnGpSubscriberMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,7))
if mibBuilder.loadTexts:bTWagGnGpSubscriberMIBObjects.setStatus(_A)
_BTWagNumCurrentSecureSSIDGnGpSubscribers_Type=Unsigned32
_BTWagNumCurrentSecureSSIDGnGpSubscribers_Object=MibScalar
bTWagNumCurrentSecureSSIDGnGpSubscribers=_BTWagNumCurrentSecureSSIDGnGpSubscribers_Object((1,3,6,1,4,1,39406,2,1,7,7,1),_BTWagNumCurrentSecureSSIDGnGpSubscribers_Type())
bTWagNumCurrentSecureSSIDGnGpSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagNumCurrentSecureSSIDGnGpSubscribers.setStatus(_A)
_BTWagNumPreAuthenticatedGnGpSubscribers_Type=Unsigned32
_BTWagNumPreAuthenticatedGnGpSubscribers_Object=MibScalar
bTWagNumPreAuthenticatedGnGpSubscribers=_BTWagNumPreAuthenticatedGnGpSubscribers_Object((1,3,6,1,4,1,39406,2,1,7,7,2),_BTWagNumPreAuthenticatedGnGpSubscribers_Type())
bTWagNumPreAuthenticatedGnGpSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagNumPreAuthenticatedGnGpSubscribers.setStatus(_A)
_BTWagGnGpSubscriberTable_Object=MibTable
bTWagGnGpSubscriberTable=_BTWagGnGpSubscriberTable_Object((1,3,6,1,4,1,39406,2,1,7,7,3))
if mibBuilder.loadTexts:bTWagGnGpSubscriberTable.setStatus(_A)
_BTWagGnGpSubscriberEntry_Object=MibTableRow
bTWagGnGpSubscriberEntry=_BTWagGnGpSubscriberEntry_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1))
bTWagGnGpSubscriberEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:bTWagGnGpSubscriberEntry.setStatus(_A)
_BTWagGnGpSubsStatsInterval_Type=Integer32
_BTWagGnGpSubsStatsInterval_Object=MibTableColumn
bTWagGnGpSubsStatsInterval=_BTWagGnGpSubsStatsInterval_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,1),_BTWagGnGpSubsStatsInterval_Type())
bTWagGnGpSubsStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bTWagGnGpSubsStatsInterval.setStatus(_A)
_BTWagGnGpSubsIntervalDuration_Type=Integer32
_BTWagGnGpSubsIntervalDuration_Object=MibTableColumn
bTWagGnGpSubsIntervalDuration=_BTWagGnGpSubsIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,2),_BTWagGnGpSubsIntervalDuration_Type())
bTWagGnGpSubsIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsIntervalDuration.setStatus(_A)
_BTWagSecureSSIDGnGpSubsAdded_Type=Unsigned32
_BTWagSecureSSIDGnGpSubsAdded_Object=MibTableColumn
bTWagSecureSSIDGnGpSubsAdded=_BTWagSecureSSIDGnGpSubsAdded_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,3),_BTWagSecureSSIDGnGpSubsAdded_Type())
bTWagSecureSSIDGnGpSubsAdded.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagSecureSSIDGnGpSubsAdded.setStatus(_A)
_BTWagPreAuthenticatedGnGpSubsAdded_Type=Unsigned32
_BTWagPreAuthenticatedGnGpSubsAdded_Object=MibTableColumn
bTWagPreAuthenticatedGnGpSubsAdded=_BTWagPreAuthenticatedGnGpSubsAdded_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,4),_BTWagPreAuthenticatedGnGpSubsAdded_Type())
bTWagPreAuthenticatedGnGpSubsAdded.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPreAuthenticatedGnGpSubsAdded.setStatus(_A)
_BTWagGnGpSubsDeletionsByDMinitiatedByGGSN_Type=Unsigned32
_BTWagGnGpSubsDeletionsByDMinitiatedByGGSN_Object=MibTableColumn
bTWagGnGpSubsDeletionsByDMinitiatedByGGSN=_BTWagGnGpSubsDeletionsByDMinitiatedByGGSN_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,5),_BTWagGnGpSubsDeletionsByDMinitiatedByGGSN_Type())
bTWagGnGpSubsDeletionsByDMinitiatedByGGSN.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsDeletionsByDMinitiatedByGGSN.setStatus(_A)
_BTWagGnGpSubsGtpSessionCreateFailed_Type=Unsigned32
_BTWagGnGpSubsGtpSessionCreateFailed_Object=MibTableColumn
bTWagGnGpSubsGtpSessionCreateFailed=_BTWagGnGpSubsGtpSessionCreateFailed_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,6),_BTWagGnGpSubsGtpSessionCreateFailed_Type())
bTWagGnGpSubsGtpSessionCreateFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsGtpSessionCreateFailed.setStatus(_A)
_BTWagGnGpSubsCPCRQSendFailed_Type=Unsigned32
_BTWagGnGpSubsCPCRQSendFailed_Object=MibTableColumn
bTWagGnGpSubsCPCRQSendFailed=_BTWagGnGpSubsCPCRQSendFailed_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,7),_BTWagGnGpSubsCPCRQSendFailed_Type())
bTWagGnGpSubsCPCRQSendFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsCPCRQSendFailed.setStatus(_A)
_BTWagGnGpSubsPDPCtxSendFailed_Type=Unsigned32
_BTWagGnGpSubsPDPCtxSendFailed_Object=MibTableColumn
bTWagGnGpSubsPDPCtxSendFailed=_BTWagGnGpSubsPDPCtxSendFailed_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,8),_BTWagGnGpSubsPDPCtxSendFailed_Type())
bTWagGnGpSubsPDPCtxSendFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsPDPCtxSendFailed.setStatus(_A)
_BTWagGnGpSubsInvalidGtpVersion_Type=Unsigned32
_BTWagGnGpSubsInvalidGtpVersion_Object=MibTableColumn
bTWagGnGpSubsInvalidGtpVersion=_BTWagGnGpSubsInvalidGtpVersion_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,9),_BTWagGnGpSubsInvalidGtpVersion_Type())
bTWagGnGpSubsInvalidGtpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsInvalidGtpVersion.setStatus(_A)
_BTWagGnGpSubsRadiusMissingMandatoryParams_Type=Unsigned32
_BTWagGnGpSubsRadiusMissingMandatoryParams_Object=MibTableColumn
bTWagGnGpSubsRadiusMissingMandatoryParams=_BTWagGnGpSubsRadiusMissingMandatoryParams_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,10),_BTWagGnGpSubsRadiusMissingMandatoryParams_Type())
bTWagGnGpSubsRadiusMissingMandatoryParams.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusMissingMandatoryParams.setStatus(_A)
_BTWagGnGpSubsRadiusInvalidGGSNIPAddr_Type=Unsigned32
_BTWagGnGpSubsRadiusInvalidGGSNIPAddr_Object=MibTableColumn
bTWagGnGpSubsRadiusInvalidGGSNIPAddr=_BTWagGnGpSubsRadiusInvalidGGSNIPAddr_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,11),_BTWagGnGpSubsRadiusInvalidGGSNIPAddr_Type())
bTWagGnGpSubsRadiusInvalidGGSNIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusInvalidGGSNIPAddr.setStatus(_A)
_BTWagGnGpSubsRadiusMSISDN_Type=Unsigned32
_BTWagGnGpSubsRadiusMSISDN_Object=MibTableColumn
bTWagGnGpSubsRadiusMSISDN=_BTWagGnGpSubsRadiusMSISDN_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,12),_BTWagGnGpSubsRadiusMSISDN_Type())
bTWagGnGpSubsRadiusMSISDN.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusMSISDN.setStatus(_A)
_BTWagGnGpSubsRadiusQoSProfile_Type=Unsigned32
_BTWagGnGpSubsRadiusQoSProfile_Object=MibTableColumn
bTWagGnGpSubsRadiusQoSProfile=_BTWagGnGpSubsRadiusQoSProfile_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,13),_BTWagGnGpSubsRadiusQoSProfile_Type())
bTWagGnGpSubsRadiusQoSProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusQoSProfile.setStatus(_A)
_BTWagGnGpSubsRadiusGBRQoS_Type=Unsigned32
_BTWagGnGpSubsRadiusGBRQoS_Object=MibTableColumn
bTWagGnGpSubsRadiusGBRQoS=_BTWagGnGpSubsRadiusGBRQoS_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,14),_BTWagGnGpSubsRadiusGBRQoS_Type())
bTWagGnGpSubsRadiusGBRQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusGBRQoS.setStatus(_A)
_BTWagGnGpSubsRadiusNonGBRQoS_Type=Unsigned32
_BTWagGnGpSubsRadiusNonGBRQoS_Object=MibTableColumn
bTWagGnGpSubsRadiusNonGBRQoS=_BTWagGnGpSubsRadiusNonGBRQoS_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,15),_BTWagGnGpSubsRadiusNonGBRQoS_Type())
bTWagGnGpSubsRadiusNonGBRQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusNonGBRQoS.setStatus(_A)
_BTWagGnGpSubsGtpIPAddFailed_Type=Unsigned32
_BTWagGnGpSubsGtpIPAddFailed_Object=MibTableColumn
bTWagGnGpSubsGtpIPAddFailed=_BTWagGnGpSubsGtpIPAddFailed_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,16),_BTWagGnGpSubsGtpIPAddFailed_Type())
bTWagGnGpSubsGtpIPAddFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsGtpIPAddFailed.setStatus(_A)
_BTWagGnGpSubsRadiusEapAkaHash_Type=Unsigned32
_BTWagGnGpSubsRadiusEapAkaHash_Object=MibTableColumn
bTWagGnGpSubsRadiusEapAkaHash=_BTWagGnGpSubsRadiusEapAkaHash_Object((1,3,6,1,4,1,39406,2,1,7,7,3,1,17),_BTWagGnGpSubsRadiusEapAkaHash_Type())
bTWagGnGpSubsRadiusEapAkaHash.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpSubsRadiusEapAkaHash.setStatus(_A)
_BTWagGnGpSubscriberNotifObjects_ObjectIdentity=ObjectIdentity
bTWagGnGpSubscriberNotifObjects=_BTWagGnGpSubscriberNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,8))
if mibBuilder.loadTexts:bTWagGnGpSubscriberNotifObjects.setStatus(_A)
_BTWagGnGpStatsMIBObjects_ObjectIdentity=ObjectIdentity
bTWagGnGpStatsMIBObjects=_BTWagGnGpStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,9))
if mibBuilder.loadTexts:bTWagGnGpStatsMIBObjects.setStatus(_A)
_BTWagGnGpTable_Object=MibTable
bTWagGnGpTable=_BTWagGnGpTable_Object((1,3,6,1,4,1,39406,2,1,7,9,1))
if mibBuilder.loadTexts:bTWagGnGpTable.setStatus(_A)
_BTWagGnGpEntry_Object=MibTableRow
bTWagGnGpEntry=_BTWagGnGpEntry_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1))
bTWagGnGpEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:bTWagGnGpEntry.setStatus(_A)
_BTWagGnGpStatsInterval_Type=Integer32
_BTWagGnGpStatsInterval_Object=MibTableColumn
bTWagGnGpStatsInterval=_BTWagGnGpStatsInterval_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,1),_BTWagGnGpStatsInterval_Type())
bTWagGnGpStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bTWagGnGpStatsInterval.setStatus(_A)
_BTWagGnGpIntervalDuration_Type=Integer32
_BTWagGnGpIntervalDuration_Object=MibTableColumn
bTWagGnGpIntervalDuration=_BTWagGnGpIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,2),_BTWagGnGpIntervalDuration_Type())
bTWagGnGpIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpIntervalDuration.setStatus(_A)
_BTWagGnGpCPCRQSent_Type=Unsigned32
_BTWagGnGpCPCRQSent_Object=MibTableColumn
bTWagGnGpCPCRQSent=_BTWagGnGpCPCRQSent_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,3),_BTWagGnGpCPCRQSent_Type())
bTWagGnGpCPCRQSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpCPCRQSent.setStatus(_A)
_BTWagGnGpCPCRPRcvd_Type=Unsigned32
_BTWagGnGpCPCRPRcvd_Object=MibTableColumn
bTWagGnGpCPCRPRcvd=_BTWagGnGpCPCRPRcvd_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,4),_BTWagGnGpCPCRPRcvd_Type())
bTWagGnGpCPCRPRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpCPCRPRcvd.setStatus(_A)
_BTWagGnGpCPCRPAccepted_Type=Unsigned32
_BTWagGnGpCPCRPAccepted_Object=MibTableColumn
bTWagGnGpCPCRPAccepted=_BTWagGnGpCPCRPAccepted_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,5),_BTWagGnGpCPCRPAccepted_Type())
bTWagGnGpCPCRPAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpCPCRPAccepted.setStatus(_A)
_BTWagGnGpCPCRPRej_Type=Unsigned32
_BTWagGnGpCPCRPRej_Object=MibTableColumn
bTWagGnGpCPCRPRej=_BTWagGnGpCPCRPRej_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,6),_BTWagGnGpCPCRPRej_Type())
bTWagGnGpCPCRPRej.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpCPCRPRej.setStatus(_A)
_BTWagGnGpDPCRQSent_Type=Unsigned32
_BTWagGnGpDPCRQSent_Object=MibTableColumn
bTWagGnGpDPCRQSent=_BTWagGnGpDPCRQSent_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,7),_BTWagGnGpDPCRQSent_Type())
bTWagGnGpDPCRQSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpDPCRQSent.setStatus(_A)
_BTWagGnGpDPCRPRcvd_Type=Unsigned32
_BTWagGnGpDPCRPRcvd_Object=MibTableColumn
bTWagGnGpDPCRPRcvd=_BTWagGnGpDPCRPRcvd_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,8),_BTWagGnGpDPCRPRcvd_Type())
bTWagGnGpDPCRPRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpDPCRPRcvd.setStatus(_A)
_BTWagGnGpDPCRPRejRcvd_Type=Unsigned32
_BTWagGnGpDPCRPRejRcvd_Object=MibTableColumn
bTWagGnGpDPCRPRejRcvd=_BTWagGnGpDPCRPRejRcvd_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,9),_BTWagGnGpDPCRPRejRcvd_Type())
bTWagGnGpDPCRPRejRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpDPCRPRejRcvd.setStatus(_A)
_BTWagGnGpDPCRQRcvd_Type=Unsigned32
_BTWagGnGpDPCRQRcvd_Object=MibTableColumn
bTWagGnGpDPCRQRcvd=_BTWagGnGpDPCRQRcvd_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,10),_BTWagGnGpDPCRQRcvd_Type())
bTWagGnGpDPCRQRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpDPCRQRcvd.setStatus(_A)
_BTWagGnGpDPCRPSent_Type=Unsigned32
_BTWagGnGpDPCRPSent_Object=MibTableColumn
bTWagGnGpDPCRPSent=_BTWagGnGpDPCRPSent_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,11),_BTWagGnGpDPCRPSent_Type())
bTWagGnGpDPCRPSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpDPCRPSent.setStatus(_A)
_BTWagGnGpCPCRQRcvd_Type=Unsigned32
_BTWagGnGpCPCRQRcvd_Object=MibTableColumn
bTWagGnGpCPCRQRcvd=_BTWagGnGpCPCRQRcvd_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,12),_BTWagGnGpCPCRQRcvd_Type())
bTWagGnGpCPCRQRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpCPCRQRcvd.setStatus(_A)
_BTWagGnGpCPCRPSent_Type=Unsigned32
_BTWagGnGpCPCRPSent_Object=MibTableColumn
bTWagGnGpCPCRPSent=_BTWagGnGpCPCRPSent_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,13),_BTWagGnGpCPCRPSent_Type())
bTWagGnGpCPCRPSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpCPCRPSent.setStatus(_A)
_BTWagGnGpUPCRQRcvd_Type=Unsigned32
_BTWagGnGpUPCRQRcvd_Object=MibTableColumn
bTWagGnGpUPCRQRcvd=_BTWagGnGpUPCRQRcvd_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,14),_BTWagGnGpUPCRQRcvd_Type())
bTWagGnGpUPCRQRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpUPCRQRcvd.setStatus(_A)
_BTWagGnGpUPCRPSent_Type=Unsigned32
_BTWagGnGpUPCRPSent_Object=MibTableColumn
bTWagGnGpUPCRPSent=_BTWagGnGpUPCRPSent_Object((1,3,6,1,4,1,39406,2,1,7,9,1,1,15),_BTWagGnGpUPCRPSent_Type())
bTWagGnGpUPCRPSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagGnGpUPCRPSent.setStatus(_A)
_BTWagGnGpNotifObjects_ObjectIdentity=ObjectIdentity
bTWagGnGpNotifObjects=_BTWagGnGpNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,10))
if mibBuilder.loadTexts:bTWagGnGpNotifObjects.setStatus(_A)
_BTWagPmip6MIBObjects_ObjectIdentity=ObjectIdentity
bTWagPmip6MIBObjects=_BTWagPmip6MIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,7,11))
if mibBuilder.loadTexts:bTWagPmip6MIBObjects.setStatus(_A)
_BTWagNumPreAuthenticatedPmip6Subscribers_Type=Unsigned32
_BTWagNumPreAuthenticatedPmip6Subscribers_Object=MibScalar
bTWagNumPreAuthenticatedPmip6Subscribers=_BTWagNumPreAuthenticatedPmip6Subscribers_Object((1,3,6,1,4,1,39406,2,1,7,11,1),_BTWagNumPreAuthenticatedPmip6Subscribers_Type())
bTWagNumPreAuthenticatedPmip6Subscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagNumPreAuthenticatedPmip6Subscribers.setStatus(_A)
_BTWagNumGrePmip6Tunnels_Type=Unsigned32
_BTWagNumGrePmip6Tunnels_Object=MibScalar
bTWagNumGrePmip6Tunnels=_BTWagNumGrePmip6Tunnels_Object((1,3,6,1,4,1,39406,2,1,7,11,2),_BTWagNumGrePmip6Tunnels_Type())
bTWagNumGrePmip6Tunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagNumGrePmip6Tunnels.setStatus(_A)
_BTWagPmip6StatsTable_Object=MibTable
bTWagPmip6StatsTable=_BTWagPmip6StatsTable_Object((1,3,6,1,4,1,39406,2,1,7,11,3))
if mibBuilder.loadTexts:bTWagPmip6StatsTable.setStatus(_A)
_BTWagPmip6StatsEntry_Object=MibTableRow
bTWagPmip6StatsEntry=_BTWagPmip6StatsEntry_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1))
bTWagPmip6StatsEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:bTWagPmip6StatsEntry.setStatus(_A)
_BTWagPmip6StatsInterval_Type=Integer32
_BTWagPmip6StatsInterval_Object=MibTableColumn
bTWagPmip6StatsInterval=_BTWagPmip6StatsInterval_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,1),_BTWagPmip6StatsInterval_Type())
bTWagPmip6StatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bTWagPmip6StatsInterval.setStatus(_A)
_BTWagPmip6IntervalDuration_Type=Integer32
_BTWagPmip6IntervalDuration_Object=MibTableColumn
bTWagPmip6IntervalDuration=_BTWagPmip6IntervalDuration_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,2),_BTWagPmip6IntervalDuration_Type())
bTWagPmip6IntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6IntervalDuration.setStatus(_A)
_BTWagPmip6TotalPacketsRxvd_Type=Unsigned32
_BTWagPmip6TotalPacketsRxvd_Object=MibTableColumn
bTWagPmip6TotalPacketsRxvd=_BTWagPmip6TotalPacketsRxvd_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,3),_BTWagPmip6TotalPacketsRxvd_Type())
bTWagPmip6TotalPacketsRxvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalPacketsRxvd.setStatus(_A)
_BTWagPmip6TotalPacketsRxvdError_Type=Unsigned32
_BTWagPmip6TotalPacketsRxvdError_Object=MibTableColumn
bTWagPmip6TotalPacketsRxvdError=_BTWagPmip6TotalPacketsRxvdError_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,4),_BTWagPmip6TotalPacketsRxvdError_Type())
bTWagPmip6TotalPacketsRxvdError.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalPacketsRxvdError.setStatus(_A)
_BTWagPmip6TotalPacketHeaderDecodeError_Type=Unsigned32
_BTWagPmip6TotalPacketHeaderDecodeError_Object=MibTableColumn
bTWagPmip6TotalPacketHeaderDecodeError=_BTWagPmip6TotalPacketHeaderDecodeError_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,5),_BTWagPmip6TotalPacketHeaderDecodeError_Type())
bTWagPmip6TotalPacketHeaderDecodeError.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalPacketHeaderDecodeError.setStatus(_A)
_BTWagPmip6TotalPbuSent_Type=Unsigned32
_BTWagPmip6TotalPbuSent_Object=MibTableColumn
bTWagPmip6TotalPbuSent=_BTWagPmip6TotalPbuSent_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,6),_BTWagPmip6TotalPbuSent_Type())
bTWagPmip6TotalPbuSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalPbuSent.setStatus(_A)
_BTWagPmip6TotalPbuSendError_Type=Unsigned32
_BTWagPmip6TotalPbuSendError_Object=MibTableColumn
bTWagPmip6TotalPbuSendError=_BTWagPmip6TotalPbuSendError_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,7),_BTWagPmip6TotalPbuSendError_Type())
bTWagPmip6TotalPbuSendError.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalPbuSendError.setStatus(_A)
_BTWagPmip6TotalPbaReceived_Type=Unsigned32
_BTWagPmip6TotalPbaReceived_Object=MibTableColumn
bTWagPmip6TotalPbaReceived=_BTWagPmip6TotalPbaReceived_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,8),_BTWagPmip6TotalPbaReceived_Type())
bTWagPmip6TotalPbaReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalPbaReceived.setStatus(_A)
_BTWagPmip6TotalBriReceived_Type=Unsigned32
_BTWagPmip6TotalBriReceived_Object=MibTableColumn
bTWagPmip6TotalBriReceived=_BTWagPmip6TotalBriReceived_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,9),_BTWagPmip6TotalBriReceived_Type())
bTWagPmip6TotalBriReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalBriReceived.setStatus(_A)
_BTWagPmip6TotalBraSent_Type=Unsigned32
_BTWagPmip6TotalBraSent_Object=MibTableColumn
bTWagPmip6TotalBraSent=_BTWagPmip6TotalBraSent_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,10),_BTWagPmip6TotalBraSent_Type())
bTWagPmip6TotalBraSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6TotalBraSent.setStatus(_A)
_BTWagPmip6HeartBeatReqSent_Type=Unsigned32
_BTWagPmip6HeartBeatReqSent_Object=MibTableColumn
bTWagPmip6HeartBeatReqSent=_BTWagPmip6HeartBeatReqSent_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,11),_BTWagPmip6HeartBeatReqSent_Type())
bTWagPmip6HeartBeatReqSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6HeartBeatReqSent.setStatus(_A)
_BTWagPmip6HeartBeatRspSent_Type=Unsigned32
_BTWagPmip6HeartBeatRspSent_Object=MibTableColumn
bTWagPmip6HeartBeatRspSent=_BTWagPmip6HeartBeatRspSent_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,12),_BTWagPmip6HeartBeatRspSent_Type())
bTWagPmip6HeartBeatRspSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6HeartBeatRspSent.setStatus(_A)
_BTWagPmip6HeartBeatReqRestartCountMismatch_Type=Unsigned32
_BTWagPmip6HeartBeatReqRestartCountMismatch_Object=MibTableColumn
bTWagPmip6HeartBeatReqRestartCountMismatch=_BTWagPmip6HeartBeatReqRestartCountMismatch_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,13),_BTWagPmip6HeartBeatReqRestartCountMismatch_Type())
bTWagPmip6HeartBeatReqRestartCountMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6HeartBeatReqRestartCountMismatch.setStatus(_A)
_BTWagPmip6HeartBeatReqSeqMismatch_Type=Unsigned32
_BTWagPmip6HeartBeatReqSeqMismatch_Object=MibTableColumn
bTWagPmip6HeartBeatReqSeqMismatch=_BTWagPmip6HeartBeatReqSeqMismatch_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,14),_BTWagPmip6HeartBeatReqSeqMismatch_Type())
bTWagPmip6HeartBeatReqSeqMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6HeartBeatReqSeqMismatch.setStatus(_A)
_BTWagPmip6DeletedDueToLmaInitBriMsg_Type=Unsigned32
_BTWagPmip6DeletedDueToLmaInitBriMsg_Object=MibTableColumn
bTWagPmip6DeletedDueToLmaInitBriMsg=_BTWagPmip6DeletedDueToLmaInitBriMsg_Object((1,3,6,1,4,1,39406,2,1,7,11,3,1,15),_BTWagPmip6DeletedDueToLmaInitBriMsg_Type())
bTWagPmip6DeletedDueToLmaInitBriMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:bTWagPmip6DeletedDueToLmaInitBriMsg.setStatus(_A)
bTWagGTPHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,7,0,1))
bTWagGTPHighThresholdReached.setObjects(*((_C,_F),(_C,_L)))
if mibBuilder.loadTexts:bTWagGTPHighThresholdReached.setStatus(_A)
bTWagGTPLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,7,0,2))
bTWagGTPLowThresholdReached.setObjects(*((_C,_F),(_C,_M)))
if mibBuilder.loadTexts:bTWagGTPLowThresholdReached.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'benuTWagStatsMIB':benuTWagStatsMIB,'bTWagNotifications':bTWagNotifications,'bTWagGTPHighThresholdReached':bTWagGTPHighThresholdReached,'bTWagGTPLowThresholdReached':bTWagGTPLowThresholdReached,'bTWagS2aSubscriberMIBObjects':bTWagS2aSubscriberMIBObjects,'bTWagNumCurrentSecureSSIDS2aSubscribers':bTWagNumCurrentSecureSSIDS2aSubscribers,'bTWagNumPreAuthenticatedS2aSubscribers':bTWagNumPreAuthenticatedS2aSubscribers,'bTWagS2aSubscriberTable':bTWagS2aSubscriberTable,'bTWagS2aSubscriberEntry':bTWagS2aSubscriberEntry,_G:bTWagS2aSubsStatsInterval,'bTWagS2aSubsIntervalDuration':bTWagS2aSubsIntervalDuration,'bTWagSecureSSIDS2aSubsAdded':bTWagSecureSSIDS2aSubsAdded,'bTWagPreAuthenticatedS2aSubsAdded':bTWagPreAuthenticatedS2aSubsAdded,'bTWagS2aSubsDeletionsByDMinitiatedByPGW':bTWagS2aSubsDeletionsByDMinitiatedByPGW,'bTWagS2aSubsGtpSessionCreateFailed':bTWagS2aSubsGtpSessionCreateFailed,'bTWagS2aSubsCSRQSendFailed':bTWagS2aSubsCSRQSendFailed,'bTWagS2aSubsInvalidGtpVersion':bTWagS2aSubsInvalidGtpVersion,'bTWagS2aSubsRadiusMissingMandatoryParams':bTWagS2aSubsRadiusMissingMandatoryParams,'bTWagS2aSubsRadiusInvalidPGWIPAddr':bTWagS2aSubsRadiusInvalidPGWIPAddr,'bTWagS2aSubsRadiusMSISDN':bTWagS2aSubsRadiusMSISDN,'bTWagS2aSubsRadiusQoSProfile':bTWagS2aSubsRadiusQoSProfile,'bTWagS2aSubsRadiusGBRQoS':bTWagS2aSubsRadiusGBRQoS,'bTWagS2aSubsRadiusNonGBRQoS':bTWagS2aSubsRadiusNonGBRQoS,'bTWagS2aSubsGtpIPAddFailed':bTWagS2aSubsGtpIPAddFailed,'bTWagS2aSubsRadiusEapAkaHash':bTWagS2aSubsRadiusEapAkaHash,'bTWagS2aSubscriberNotifObjects':bTWagS2aSubscriberNotifObjects,'bTWagS2aStatsMIBObjects':bTWagS2aStatsMIBObjects,'bTWagS2aTable':bTWagS2aTable,'bTWagS2aEntry':bTWagS2aEntry,_H:bTWagS2aStatsInterval,'bTWagS2aIntervalDuration':bTWagS2aIntervalDuration,'bTWagS2aSessCreateReqSent':bTWagS2aSessCreateReqSent,'bTWagS2aSessCreateRespRcvd':bTWagS2aSessCreateRespRcvd,'bTWagS2aSessCreateRespAccepted':bTWagS2aSessCreateRespAccepted,'bTWagS2aSessCreateRespRej':bTWagS2aSessCreateRespRej,'bTWagS2aSessDelReqSent':bTWagS2aSessDelReqSent,'bTWagS2aSessDelRespRcvd':bTWagS2aSessDelRespRcvd,'bTWagS2aSessDelRespRejRcvd':bTWagS2aSessDelRespRejRcvd,'bTWagS2aDBRQRcvd':bTWagS2aDBRQRcvd,'bTWagS2aDBRPSent':bTWagS2aDBRPSent,'bTWagS2aCBRQRcvd':bTWagS2aCBRQRcvd,'bTWagS2aCBRPSent':bTWagS2aCBRPSent,'bTWagS2aUBRQRcvd':bTWagS2aUBRQRcvd,'bTWagS2aUBRPSent':bTWagS2aUBRPSent,'bTWagS2aNotifObjects':bTWagS2aNotifObjects,'bTWagGTPStatsMIBObjects':bTWagGTPStatsMIBObjects,'bTWagGTPCurrentNumOfTunnels':bTWagGTPCurrentNumOfTunnels,'bTWagGTPNotifObjects':bTWagGTPNotifObjects,_F:bTWagGTPMaxNumOfTunnels,_L:bTWagGTPHighThreshold,_M:bTWagGTPLowThreshold,'bTWagGnGpSubscriberMIBObjects':bTWagGnGpSubscriberMIBObjects,'bTWagNumCurrentSecureSSIDGnGpSubscribers':bTWagNumCurrentSecureSSIDGnGpSubscribers,'bTWagNumPreAuthenticatedGnGpSubscribers':bTWagNumPreAuthenticatedGnGpSubscribers,'bTWagGnGpSubscriberTable':bTWagGnGpSubscriberTable,'bTWagGnGpSubscriberEntry':bTWagGnGpSubscriberEntry,_I:bTWagGnGpSubsStatsInterval,'bTWagGnGpSubsIntervalDuration':bTWagGnGpSubsIntervalDuration,'bTWagSecureSSIDGnGpSubsAdded':bTWagSecureSSIDGnGpSubsAdded,'bTWagPreAuthenticatedGnGpSubsAdded':bTWagPreAuthenticatedGnGpSubsAdded,'bTWagGnGpSubsDeletionsByDMinitiatedByGGSN':bTWagGnGpSubsDeletionsByDMinitiatedByGGSN,'bTWagGnGpSubsGtpSessionCreateFailed':bTWagGnGpSubsGtpSessionCreateFailed,'bTWagGnGpSubsCPCRQSendFailed':bTWagGnGpSubsCPCRQSendFailed,'bTWagGnGpSubsPDPCtxSendFailed':bTWagGnGpSubsPDPCtxSendFailed,'bTWagGnGpSubsInvalidGtpVersion':bTWagGnGpSubsInvalidGtpVersion,'bTWagGnGpSubsRadiusMissingMandatoryParams':bTWagGnGpSubsRadiusMissingMandatoryParams,'bTWagGnGpSubsRadiusInvalidGGSNIPAddr':bTWagGnGpSubsRadiusInvalidGGSNIPAddr,'bTWagGnGpSubsRadiusMSISDN':bTWagGnGpSubsRadiusMSISDN,'bTWagGnGpSubsRadiusQoSProfile':bTWagGnGpSubsRadiusQoSProfile,'bTWagGnGpSubsRadiusGBRQoS':bTWagGnGpSubsRadiusGBRQoS,'bTWagGnGpSubsRadiusNonGBRQoS':bTWagGnGpSubsRadiusNonGBRQoS,'bTWagGnGpSubsGtpIPAddFailed':bTWagGnGpSubsGtpIPAddFailed,'bTWagGnGpSubsRadiusEapAkaHash':bTWagGnGpSubsRadiusEapAkaHash,'bTWagGnGpSubscriberNotifObjects':bTWagGnGpSubscriberNotifObjects,'bTWagGnGpStatsMIBObjects':bTWagGnGpStatsMIBObjects,'bTWagGnGpTable':bTWagGnGpTable,'bTWagGnGpEntry':bTWagGnGpEntry,_J:bTWagGnGpStatsInterval,'bTWagGnGpIntervalDuration':bTWagGnGpIntervalDuration,'bTWagGnGpCPCRQSent':bTWagGnGpCPCRQSent,'bTWagGnGpCPCRPRcvd':bTWagGnGpCPCRPRcvd,'bTWagGnGpCPCRPAccepted':bTWagGnGpCPCRPAccepted,'bTWagGnGpCPCRPRej':bTWagGnGpCPCRPRej,'bTWagGnGpDPCRQSent':bTWagGnGpDPCRQSent,'bTWagGnGpDPCRPRcvd':bTWagGnGpDPCRPRcvd,'bTWagGnGpDPCRPRejRcvd':bTWagGnGpDPCRPRejRcvd,'bTWagGnGpDPCRQRcvd':bTWagGnGpDPCRQRcvd,'bTWagGnGpDPCRPSent':bTWagGnGpDPCRPSent,'bTWagGnGpCPCRQRcvd':bTWagGnGpCPCRQRcvd,'bTWagGnGpCPCRPSent':bTWagGnGpCPCRPSent,'bTWagGnGpUPCRQRcvd':bTWagGnGpUPCRQRcvd,'bTWagGnGpUPCRPSent':bTWagGnGpUPCRPSent,'bTWagGnGpNotifObjects':bTWagGnGpNotifObjects,'bTWagPmip6MIBObjects':bTWagPmip6MIBObjects,'bTWagNumPreAuthenticatedPmip6Subscribers':bTWagNumPreAuthenticatedPmip6Subscribers,'bTWagNumGrePmip6Tunnels':bTWagNumGrePmip6Tunnels,'bTWagPmip6StatsTable':bTWagPmip6StatsTable,'bTWagPmip6StatsEntry':bTWagPmip6StatsEntry,_K:bTWagPmip6StatsInterval,'bTWagPmip6IntervalDuration':bTWagPmip6IntervalDuration,'bTWagPmip6TotalPacketsRxvd':bTWagPmip6TotalPacketsRxvd,'bTWagPmip6TotalPacketsRxvdError':bTWagPmip6TotalPacketsRxvdError,'bTWagPmip6TotalPacketHeaderDecodeError':bTWagPmip6TotalPacketHeaderDecodeError,'bTWagPmip6TotalPbuSent':bTWagPmip6TotalPbuSent,'bTWagPmip6TotalPbuSendError':bTWagPmip6TotalPbuSendError,'bTWagPmip6TotalPbaReceived':bTWagPmip6TotalPbaReceived,'bTWagPmip6TotalBriReceived':bTWagPmip6TotalBriReceived,'bTWagPmip6TotalBraSent':bTWagPmip6TotalBraSent,'bTWagPmip6HeartBeatReqSent':bTWagPmip6HeartBeatReqSent,'bTWagPmip6HeartBeatRspSent':bTWagPmip6HeartBeatRspSent,'bTWagPmip6HeartBeatReqRestartCountMismatch':bTWagPmip6HeartBeatReqRestartCountMismatch,'bTWagPmip6HeartBeatReqSeqMismatch':bTWagPmip6HeartBeatReqSeqMismatch,'bTWagPmip6DeletedDueToLmaInitBriMsg':bTWagPmip6DeletedDueToLmaInitBriMsg})