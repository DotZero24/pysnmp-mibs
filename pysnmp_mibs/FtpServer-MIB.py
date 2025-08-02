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
_FtpServer_ObjectIdentity=ObjectIdentity
ftpServer=_FtpServer_ObjectIdentity((1,3,6,1,4,1,311,1,7,2))
_FtpStatistics_ObjectIdentity=ObjectIdentity
ftpStatistics=_FtpStatistics_ObjectIdentity((1,3,6,1,4,1,311,1,7,2,1))
_TotalBytesSentHighWord_Type=Counter32
_TotalBytesSentHighWord_Object=MibScalar
totalBytesSentHighWord=_TotalBytesSentHighWord_Object((1,3,6,1,4,1,311,1,7,2,1,1),_TotalBytesSentHighWord_Type())
totalBytesSentHighWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesSentHighWord.setStatus(_B)
_TotalBytesSentLowWord_Type=Counter32
_TotalBytesSentLowWord_Object=MibScalar
totalBytesSentLowWord=_TotalBytesSentLowWord_Object((1,3,6,1,4,1,311,1,7,2,1,2),_TotalBytesSentLowWord_Type())
totalBytesSentLowWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesSentLowWord.setStatus(_B)
_TotalBytesReceivedHighWord_Type=Counter32
_TotalBytesReceivedHighWord_Object=MibScalar
totalBytesReceivedHighWord=_TotalBytesReceivedHighWord_Object((1,3,6,1,4,1,311,1,7,2,1,3),_TotalBytesReceivedHighWord_Type())
totalBytesReceivedHighWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesReceivedHighWord.setStatus(_B)
_TotalBytesReceivedLowWord_Type=Counter32
_TotalBytesReceivedLowWord_Object=MibScalar
totalBytesReceivedLowWord=_TotalBytesReceivedLowWord_Object((1,3,6,1,4,1,311,1,7,2,1,4),_TotalBytesReceivedLowWord_Type())
totalBytesReceivedLowWord.setMaxAccess(_A)
if mibBuilder.loadTexts:totalBytesReceivedLowWord.setStatus(_B)
_TotalFilesSent_Type=Counter32
_TotalFilesSent_Object=MibScalar
totalFilesSent=_TotalFilesSent_Object((1,3,6,1,4,1,311,1,7,2,1,5),_TotalFilesSent_Type())
totalFilesSent.setMaxAccess(_A)
if mibBuilder.loadTexts:totalFilesSent.setStatus(_B)
_TotalFilesReceived_Type=Counter32
_TotalFilesReceived_Object=MibScalar
totalFilesReceived=_TotalFilesReceived_Object((1,3,6,1,4,1,311,1,7,2,1,6),_TotalFilesReceived_Type())
totalFilesReceived.setMaxAccess(_A)
if mibBuilder.loadTexts:totalFilesReceived.setStatus(_B)
_CurrentAnonymousUsers_Type=Integer32
_CurrentAnonymousUsers_Object=MibScalar
currentAnonymousUsers=_CurrentAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,2,1,7),_CurrentAnonymousUsers_Type())
currentAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:currentAnonymousUsers.setStatus(_B)
_CurrentNonAnonymousUsers_Type=Integer32
_CurrentNonAnonymousUsers_Object=MibScalar
currentNonAnonymousUsers=_CurrentNonAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,2,1,8),_CurrentNonAnonymousUsers_Type())
currentNonAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:currentNonAnonymousUsers.setStatus(_B)
_TotalAnonymousUsers_Type=Counter32
_TotalAnonymousUsers_Object=MibScalar
totalAnonymousUsers=_TotalAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,2,1,9),_TotalAnonymousUsers_Type())
totalAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:totalAnonymousUsers.setStatus(_B)
_TotalNonAnonymousUsers_Type=Counter32
_TotalNonAnonymousUsers_Object=MibScalar
totalNonAnonymousUsers=_TotalNonAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,2,1,10),_TotalNonAnonymousUsers_Type())
totalNonAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:totalNonAnonymousUsers.setStatus(_B)
_MaxAnonymousUsers_Type=Counter32
_MaxAnonymousUsers_Object=MibScalar
maxAnonymousUsers=_MaxAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,2,1,11),_MaxAnonymousUsers_Type())
maxAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:maxAnonymousUsers.setStatus(_B)
_MaxNonAnonymousUsers_Type=Counter32
_MaxNonAnonymousUsers_Object=MibScalar
maxNonAnonymousUsers=_MaxNonAnonymousUsers_Object((1,3,6,1,4,1,311,1,7,2,1,12),_MaxNonAnonymousUsers_Type())
maxNonAnonymousUsers.setMaxAccess(_A)
if mibBuilder.loadTexts:maxNonAnonymousUsers.setStatus(_B)
_CurrentConnections_Type=Integer32
_CurrentConnections_Object=MibScalar
currentConnections=_CurrentConnections_Object((1,3,6,1,4,1,311,1,7,2,1,13),_CurrentConnections_Type())
currentConnections.setMaxAccess(_A)
if mibBuilder.loadTexts:currentConnections.setStatus(_B)
_MaxConnections_Type=Counter32
_MaxConnections_Object=MibScalar
maxConnections=_MaxConnections_Object((1,3,6,1,4,1,311,1,7,2,1,14),_MaxConnections_Type())
maxConnections.setMaxAccess(_A)
if mibBuilder.loadTexts:maxConnections.setStatus(_B)
_ConnectionAttempts_Type=Counter32
_ConnectionAttempts_Object=MibScalar
connectionAttempts=_ConnectionAttempts_Object((1,3,6,1,4,1,311,1,7,2,1,15),_ConnectionAttempts_Type())
connectionAttempts.setMaxAccess(_A)
if mibBuilder.loadTexts:connectionAttempts.setStatus(_B)
_LogonAttempts_Type=Counter32
_LogonAttempts_Object=MibScalar
logonAttempts=_LogonAttempts_Object((1,3,6,1,4,1,311,1,7,2,1,16),_LogonAttempts_Type())
logonAttempts.setMaxAccess(_A)
if mibBuilder.loadTexts:logonAttempts.setStatus(_B)
mibBuilder.exportSymbols('FtpServer-MIB',**{'microsoft':microsoft,'software':software,'internetServer':internetServer,'ftpServer':ftpServer,'ftpStatistics':ftpStatistics,'totalBytesSentHighWord':totalBytesSentHighWord,'totalBytesSentLowWord':totalBytesSentLowWord,'totalBytesReceivedHighWord':totalBytesReceivedHighWord,'totalBytesReceivedLowWord':totalBytesReceivedLowWord,'totalFilesSent':totalFilesSent,'totalFilesReceived':totalFilesReceived,'currentAnonymousUsers':currentAnonymousUsers,'currentNonAnonymousUsers':currentNonAnonymousUsers,'totalAnonymousUsers':totalAnonymousUsers,'totalNonAnonymousUsers':totalNonAnonymousUsers,'maxAnonymousUsers':maxAnonymousUsers,'maxNonAnonymousUsers':maxNonAnonymousUsers,'currentConnections':currentConnections,'maxConnections':maxConnections,'connectionAttempts':connectionAttempts,'logonAttempts':logonAttempts})