_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mitelIdentification,=mibBuilder.importSymbols('MITEL-MIB','mitelIdentification')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelIdApplications=ModuleIdentity((1,3,6,1,4,1,1027,1,7))
if mibBuilder.loadTexts:mitelIdApplications.setRevisions(('2014-02-11 12:00','2008-11-25 00:00','2008-10-02 00:00','2008-08-13 00:00','2007-06-07 00:00','2007-04-09 00:00','2007-02-12 00:00','2006-08-10 00:00','2005-02-23 21:34'))
_MitelIdAppMasTeleworker_ObjectIdentity=ObjectIdentity
mitelIdAppMasTeleworker=_MitelIdAppMasTeleworker_ObjectIdentity((1,3,6,1,4,1,1027,1,7,1))
if mibBuilder.loadTexts:mitelIdAppMasTeleworker.setStatus(_A)
_MitelIdAppMasOfficeServerSuite_ObjectIdentity=ObjectIdentity
mitelIdAppMasOfficeServerSuite=_MitelIdAppMasOfficeServerSuite_ObjectIdentity((1,3,6,1,4,1,1027,1,7,2))
if mibBuilder.loadTexts:mitelIdAppMasOfficeServerSuite.setStatus(_A)
_MitelIdAppMasManagedVpn_ObjectIdentity=ObjectIdentity
mitelIdAppMasManagedVpn=_MitelIdAppMasManagedVpn_ObjectIdentity((1,3,6,1,4,1,1027,1,7,3))
if mibBuilder.loadTexts:mitelIdAppMasManagedVpn.setStatus(_A)
_MitelIdAppMasMobileExtention_ObjectIdentity=ObjectIdentity
mitelIdAppMasMobileExtention=_MitelIdAppMasMobileExtention_ObjectIdentity((1,3,6,1,4,1,1027,1,7,4))
if mibBuilder.loadTexts:mitelIdAppMasMobileExtention.setStatus(_A)
_MitelIdAppCallServer_ObjectIdentity=ObjectIdentity
mitelIdAppCallServer=_MitelIdAppCallServer_ObjectIdentity((1,3,6,1,4,1,1027,1,7,5))
if mibBuilder.loadTexts:mitelIdAppCallServer.setStatus(_A)
_MitelIdAppQuickConference_ObjectIdentity=ObjectIdentity
mitelIdAppQuickConference=_MitelIdAppQuickConference_ObjectIdentity((1,3,6,1,4,1,1027,1,7,6))
if mibBuilder.loadTexts:mitelIdAppQuickConference.setStatus(_A)
_MitelIdAppSecureCallRecConn_ObjectIdentity=ObjectIdentity
mitelIdAppSecureCallRecConn=_MitelIdAppSecureCallRecConn_ObjectIdentity((1,3,6,1,4,1,1027,1,7,7))
if mibBuilder.loadTexts:mitelIdAppSecureCallRecConn.setStatus(_A)
_MitelIdAppSuiteAppService_ObjectIdentity=ObjectIdentity
mitelIdAppSuiteAppService=_MitelIdAppSuiteAppService_ObjectIdentity((1,3,6,1,4,1,1027,1,7,8))
if mibBuilder.loadTexts:mitelIdAppSuiteAppService.setStatus(_A)
_MitelIdAppAudioWebConferencing_ObjectIdentity=ObjectIdentity
mitelIdAppAudioWebConferencing=_MitelIdAppAudioWebConferencing_ObjectIdentity((1,3,6,1,4,1,1027,1,7,9))
if mibBuilder.loadTexts:mitelIdAppAudioWebConferencing.setStatus(_A)
_MitelIdAppCustomerServiceManager_ObjectIdentity=ObjectIdentity
mitelIdAppCustomerServiceManager=_MitelIdAppCustomerServiceManager_ObjectIdentity((1,3,6,1,4,1,1027,1,7,10))
if mibBuilder.loadTexts:mitelIdAppCustomerServiceManager.setStatus(_A)
_MitelIdAppNupointUnifiedMessenger_ObjectIdentity=ObjectIdentity
mitelIdAppNupointUnifiedMessenger=_MitelIdAppNupointUnifiedMessenger_ObjectIdentity((1,3,6,1,4,1,1027,1,7,11))
if mibBuilder.loadTexts:mitelIdAppNupointUnifiedMessenger.setStatus(_A)
_MitelIdAppUnifiedCommunicationsServer_ObjectIdentity=ObjectIdentity
mitelIdAppUnifiedCommunicationsServer=_MitelIdAppUnifiedCommunicationsServer_ObjectIdentity((1,3,6,1,4,1,1027,1,7,12))
if mibBuilder.loadTexts:mitelIdAppUnifiedCommunicationsServer.setStatus(_A)
_MitelIdAppUnifiedIPClient_ObjectIdentity=ObjectIdentity
mitelIdAppUnifiedIPClient=_MitelIdAppUnifiedIPClient_ObjectIdentity((1,3,6,1,4,1,1027,1,7,13))
if mibBuilder.loadTexts:mitelIdAppUnifiedIPClient.setStatus(_A)
_MitelIdAppMediaServiceManager_ObjectIdentity=ObjectIdentity
mitelIdAppMediaServiceManager=_MitelIdAppMediaServiceManager_ObjectIdentity((1,3,6,1,4,1,1027,1,7,14))
if mibBuilder.loadTexts:mitelIdAppMediaServiceManager.setStatus(_A)
_MitelIdAppMitelCommunicationDirectorManager_ObjectIdentity=ObjectIdentity
mitelIdAppMitelCommunicationDirectorManager=_MitelIdAppMitelCommunicationDirectorManager_ObjectIdentity((1,3,6,1,4,1,1027,1,7,15))
if mibBuilder.loadTexts:mitelIdAppMitelCommunicationDirectorManager.setStatus(_A)
mibBuilder.exportSymbols('MITEL-APPLIST-MIB',**{'mitelIdApplications':mitelIdApplications,'mitelIdAppMasTeleworker':mitelIdAppMasTeleworker,'mitelIdAppMasOfficeServerSuite':mitelIdAppMasOfficeServerSuite,'mitelIdAppMasManagedVpn':mitelIdAppMasManagedVpn,'mitelIdAppMasMobileExtention':mitelIdAppMasMobileExtention,'mitelIdAppCallServer':mitelIdAppCallServer,'mitelIdAppQuickConference':mitelIdAppQuickConference,'mitelIdAppSecureCallRecConn':mitelIdAppSecureCallRecConn,'mitelIdAppSuiteAppService':mitelIdAppSuiteAppService,'mitelIdAppAudioWebConferencing':mitelIdAppAudioWebConferencing,'mitelIdAppCustomerServiceManager':mitelIdAppCustomerServiceManager,'mitelIdAppNupointUnifiedMessenger':mitelIdAppNupointUnifiedMessenger,'mitelIdAppUnifiedCommunicationsServer':mitelIdAppUnifiedCommunicationsServer,'mitelIdAppUnifiedIPClient':mitelIdAppUnifiedIPClient,'mitelIdAppMediaServiceManager':mitelIdAppMediaServiceManager,'mitelIdAppMitelCommunicationDirectorManager':mitelIdAppMitelCommunicationDirectorManager})