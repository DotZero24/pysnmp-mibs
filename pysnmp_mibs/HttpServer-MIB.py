_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Microsoft_ObjectIdentity=ObjectIdentity
microsoft=_Microsoft_ObjectIdentity((1,3,6,1,4,1,311))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,311,1))
_InternetServer_ObjectIdentity=ObjectIdentity
internetServer=_InternetServer_ObjectIdentity((1,3,6,1,4,1,311,1,7))
_HttpServer_ObjectIdentity=ObjectIdentity
httpServer=_HttpServer_ObjectIdentity((1,3,6,1,4,1,311,1,7,3))
_HttpStatistics_ObjectIdentity=ObjectIdentity
httpStatistics=_HttpStatistics_ObjectIdentity((1,3,6,1,4,1,311,1,7,3,1))
_TotalBytesSentHighWord_Type=Counter32
_TotalBytesSentHighWord_Object=MibScalar
totalBytesSentHighWord=_TotalBytesSentHighWord_Object((1,3,6,1,4,1,311,1,7,3,1,1),_TotalBytesSentHighWord_Type())
totalBytesSentHighWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesSentHighWord.setStatus(_B)
_TotalBytesSentLowWord_Type=Counter32
_TotalBytesSentLowWord_Object=MibScalar
totalBytesSentLowWord=_TotalBytesSentLowWord_Object((1,3,6,1,4,1,311,1,7,3,1,2),_TotalBytesSentLowWord_Type())
totalBytesSentLowWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesSentLowWord.setStatus(_B)
_TotalBytesReceivedHighWord_Type=Counter32
_TotalBytesReceivedHighWord_Object=MibScalar
totalBytesReceivedHighWord=_TotalBytesReceivedHighWord_Object((1,3,6,1,4,1,311,1,7,3,1,3),_TotalBytesReceivedHighWord_Type())
totalBytesReceivedHighWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesReceivedHighWord.setStatus(_B)
_TotalBytesReceivedLowWord_Type=Counter32
_TotalBytesReceivedLowWord_Object=MibScalar
totalBytesReceivedLowWord=_TotalBytesReceivedLowWord_Object((1,3,6,1,4,1,311,1,7,3,1,4),_TotalBytesReceivedLowWord_Type())
totalBytesReceivedLowWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesReceivedLowWord.setStatus(_B)
_TotalFilesSent_Type=Counter32
_TotalFilesSent_Object=MibScalar
totalFilesSent=_TotalFilesSent_Object((1,3,6,1,4,1,311,1,7,3,1,5),_TotalFilesSent_Type())
totalFilesSent.setMaxAccess(_A)
if mibBuilder.loadTexts:totalFilesSent.setStatus(_B)
_CurrentAnonymousUsers_Type=Integer32
_CurrentAnonymousUsers_Object=MibScalar
currentAnonymousUsers=_CurrentAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,3,1,6),_CurrentAnonymousUsers_Type())
currentAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:currentAnonymousUsers.setStatus(_B)
_CurrentNonAnonymousUsers_Type=Integer32
_CurrentNonAnonymousUsers_Object=MibScalar
currentNonAnonymousUsers=_CurrentNonAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,3,1,7),_CurrentNonAnonymousUsers_Type())
currentNonAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:currentNonAnonymousUsers.setStatus(_B)
_TotalAnonymousUsers_Type=Counter32
_TotalAnonymousUsers_Object=MibScalar
totalAnonymousUsers=_TotalAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,3,1,8),_TotalAnonymousUsers_Type())
totalAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:totalAnonymousUsers.setStatus(_B)
_TotalNonAnonymousUsers_Type=Counter32
_TotalNonAnonymousUsers_Object=MibScalar
totalNonAnonymousUsers=_TotalNonAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,3,1,9),_TotalNonAnonymousUsers_Type())
totalNonAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:totalNonAnonymousUsers.setStatus(_B)
_MaxAnonymousUsers_Type=Counter32
_MaxAnonymousUsers_Object=MibScalar
maxAnonymousUsers=_MaxAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,3,1,10),_MaxAnonymousUsers_Type())
maxAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:maxAnonymousUsers.setStatus(_B)
_MaxNonAnonymousUsers_Type=Counter32
_MaxNonAnonymousUsers_Object=MibScalar
maxNonAnonymousUsers=_MaxNonAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,3,1,11),_MaxNonAnonymousUsers_Type())
maxNonAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:maxNonAnonymousUsers.setStatus(_B)
_CurrentConnections_Type=Integer32
_CurrentConnections_Object=MibScalar
currentConnections=_CurrentConnections_Object((1,3,6,1,4,1,311,1,7,3,1,12),_CurrentConnections_Type())
currentConnections.setMaxAccess(_A)
if mibBuilder.loadTexts:currentConnections.setStatus(_B)
_MaxConnections_Type=Counter32
_MaxConnections_Object=MibScalar
maxConnections=_MaxConnections_Object((1,3,6,1,4,1,311,1,7,3,1,13),_MaxConnections_Type())
maxConnections.setMaxAccess(_A)
if mibBuilder.loadTexts:maxConnections.setStatus(_B)
_ConnectionAttempts_Type=Counter32
_ConnectionAttempts_Object=MibScalar
connectionAttempts=_ConnectionAttempts_Object((1,3,6,1,4,1,311,1,7,3,1,14),_ConnectionAttempts_Type())
connectionAttempts.setMaxAccess(_A)
if mibBuilder.loadTexts:connectionAttempts.setStatus(_B)
_LogonAttempts_Type=Counter32
_LogonAttempts_Object=MibScalar
logonAttempts=_LogonAttempts_Object((1,3,6,1,4,1,311,1,7,3,1,15),_LogonAttempts_Type())
logonAttempts.setMaxAccess(_A)
if mibBuilder.loadTexts:logonAttempts.setStatus(_B)
_TotalGets_Type=Counter32
_TotalGets_Object=MibScalar
totalGets=_TotalGets_Object((1,3,6,1,4,1,311,1,7,3,1,16),_TotalGets_Type())
totalGets.setMaxAccess(_A)
if mibBuilder.loadTexts:totalGets.setStatus(_B)
_TotalPosts_Type=Counter32
_TotalPosts_Object=MibScalar
totalPosts=_TotalPosts_Object((1,3,6,1,4,1,311,1,7,3,1,17),_TotalPosts_Type())
totalPosts.setMaxAccess(_A)
if mibBuilder.loadTexts:totalPosts.setStatus(_B)
_TotalHeads_Type=Counter32
_TotalHeads_Object=MibScalar
totalHeads=_TotalHeads_Object((1,3,6,1,4,1,311,1,7,3,1,18),_TotalHeads_Type())
totalHeads.setMaxAccess(_A)
if mibBuilder.loadTexts:totalHeads.setStatus(_B)
_TotalOthers_Type=Counter32
_TotalOthers_Object=MibScalar
totalOthers=_TotalOthers_Object((1,3,6,1,4,1,311,1,7,3,1,19),_TotalOthers_Type())
totalOthers.setMaxAccess(_A)
if mibBuilder.loadTexts:totalOthers.setStatus(_B)
_TotalCGIRequests_Type=Counter32
_TotalCGIRequests_Object=MibScalar
totalCGIRequests=_TotalCGIRequests_Object((1,3,6,1,4,1,311,1,7,3,1,20),_TotalCGIRequests_Type())
totalCGIRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:totalCGIRequests.setStatus(_B)
_TotalBGIRequests_Type=Counter32
_TotalBGIRequests_Object=MibScalar
totalBGIRequests=_TotalBGIRequests_Object((1,3,6,1,4,1,311,1,7,3,1,21),_TotalBGIRequests_Type())
totalBGIRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBGIRequests.setStatus(_B)
_TotalNotFoundErrors_Type=Counter32
_TotalNotFoundErrors_Object=MibScalar
totalNotFoundErrors=_TotalNotFoundErrors_Object((1,3,6,1,4,1,311,1,7,3,1,22),_TotalNotFoundErrors_Type())
totalNotFoundErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:totalNotFoundErrors.setStatus(_B)
mibBuilder.exportSymbols('HttpServer-MIB',**{'microsoft':microsoft,'software':software,'internetServer':internetServer,'httpServer':httpServer,'httpStatistics':httpStatistics,'totalBytesSentHighWord':totalBytesSentHighWord,'totalBytesSentLowWord':totalBytesSentLowWord,'totalBytesReceivedHighWord':totalBytesReceivedHighWord,'totalBytesReceivedLowWord':totalBytesReceivedLowWord,'totalFilesSent':totalFilesSent,'currentAnonymousUsers':currentAnonymousUsers,'currentNonAnonymousUsers':currentNonAnonymousUsers,'totalAnonymousUsers':totalAnonymousUsers,'totalNonAnonymousUsers':totalNonAnonymousUsers,'maxAnonymousUsers':maxAnonymousUsers,'maxNonAnonymousUsers':maxNonAnonymousUsers,'currentConnections':currentConnections,'maxConnections':maxConnections,'connectionAttempts':connectionAttempts,'logonAttempts':logonAttempts,'totalGets':totalGets,'totalPosts':totalPosts,'totalHeads':totalHeads,'totalOthers':totalOthers,'totalCGIRequests':totalCGIRequests,'totalBGIRequests':totalBGIRequests,'totalNotFoundErrors':totalNotFoundErrors})