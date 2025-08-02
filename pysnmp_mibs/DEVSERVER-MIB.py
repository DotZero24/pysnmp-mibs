_D='read-write'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
aniDevServer=ModuleIdentity((1,3,6,1,4,1,4325,2,5))
_AniDevTftpServer_Type=IpAddress
_AniDevTftpServer_Object=MibScalar
aniDevTftpServer=_AniDevTftpServer_Object((1,3,6,1,4,1,4325,2,5,1),_AniDevTftpServer_Type())
aniDevTftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevTftpServer.setStatus(_A)
_AniDevDhcpServer_Type=IpAddress
_AniDevDhcpServer_Object=MibScalar
aniDevDhcpServer=_AniDevDhcpServer_Object((1,3,6,1,4,1,4325,2,5,2),_AniDevDhcpServer_Type())
aniDevDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevDhcpServer.setStatus(_A)
class _AniDevDhcpLeaseExpiration_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_AniDevDhcpLeaseExpiration_Type.__name__=_C
_AniDevDhcpLeaseExpiration_Object=MibScalar
aniDevDhcpLeaseExpiration=_AniDevDhcpLeaseExpiration_Object((1,3,6,1,4,1,4325,2,5,3),_AniDevDhcpLeaseExpiration_Type())
aniDevDhcpLeaseExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevDhcpLeaseExpiration.setStatus(_A)
_AniDevSuDhcpServer_Type=IpAddress
_AniDevSuDhcpServer_Object=MibScalar
aniDevSuDhcpServer=_AniDevSuDhcpServer_Object((1,3,6,1,4,1,4325,2,5,4),_AniDevSuDhcpServer_Type())
aniDevSuDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSuDhcpServer.setStatus(_A)
_AniDevTimeServer_Type=IpAddress
_AniDevTimeServer_Object=MibScalar
aniDevTimeServer=_AniDevTimeServer_Object((1,3,6,1,4,1,4325,2,5,5),_AniDevTimeServer_Type())
aniDevTimeServer.setMaxAccess(_D)
if mibBuilder.loadTexts:aniDevTimeServer.setStatus(_A)
_AniDevSyslogServer_Type=IpAddress
_AniDevSyslogServer_Object=MibScalar
aniDevSyslogServer=_AniDevSyslogServer_Object((1,3,6,1,4,1,4325,2,5,6),_AniDevSyslogServer_Type())
aniDevSyslogServer.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSyslogServer.setStatus(_A)
_AniDevSmtpServer_Type=IpAddress
_AniDevSmtpServer_Object=MibScalar
aniDevSmtpServer=_AniDevSmtpServer_Object((1,3,6,1,4,1,4325,2,5,7),_AniDevSmtpServer_Type())
aniDevSmtpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:aniDevSmtpServer.setStatus(_A)
mibBuilder.exportSymbols('DEVSERVER-MIB',**{'aniDevServer':aniDevServer,'aniDevTftpServer':aniDevTftpServer,'aniDevDhcpServer':aniDevDhcpServer,'aniDevDhcpLeaseExpiration':aniDevDhcpLeaseExpiration,'aniDevSuDhcpServer':aniDevSuDhcpServer,'aniDevTimeServer':aniDevTimeServer,'aniDevSyslogServer':aniDevSyslogServer,'aniDevSmtpServer':aniDevSmtpServer})