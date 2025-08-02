_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mitelIdentification,=mibBuilder.importSymbols('MITEL-MIB','mitelIdentification')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelIdApplicationPlatforms=ModuleIdentity((1,3,6,1,4,1,1027,1,6))
if mibBuilder.loadTexts:mitelIdApplicationPlatforms.setRevisions(('2014-02-11 12:00','2006-08-10 00:00','2005-08-24 21:34'))
_MitelIdAppPlatManagementApplicationServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatManagementApplicationServer=_MitelIdAppPlatManagementApplicationServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,1))
if mibBuilder.loadTexts:mitelIdAppPlatManagementApplicationServer.setStatus(_A)
_MitelIdAppPlatLXTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatLXTelephonyServer=_MitelIdAppPlatLXTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,2))
if mibBuilder.loadTexts:mitelIdAppPlatLXTelephonyServer.setStatus(_A)
_MitelIdAppPlatMXTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatMXTelephonyServer=_MitelIdAppPlatMXTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,3))
if mibBuilder.loadTexts:mitelIdAppPlatMXTelephonyServer.setStatus(_A)
_MitelIdAppPlatCXTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatCXTelephonyServer=_MitelIdAppPlatCXTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,4))
if mibBuilder.loadTexts:mitelIdAppPlatCXTelephonyServer.setStatus(_A)
_MitelIdAppPlatCXiTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatCXiTelephonyServer=_MitelIdAppPlatCXiTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,5))
if mibBuilder.loadTexts:mitelIdAppPlatCXiTelephonyServer.setStatus(_A)
_MitelIdAppPlatLiteTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatLiteTelephonyServer=_MitelIdAppPlatLiteTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,6))
if mibBuilder.loadTexts:mitelIdAppPlatLiteTelephonyServer.setStatus(_A)
_MitelIdAppPlatMXeTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatMXeTelephonyServer=_MitelIdAppPlatMXeTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,7))
if mibBuilder.loadTexts:mitelIdAppPlatMXeTelephonyServer.setStatus(_A)
_MitelIdAppPlatAXTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatAXTelephonyServer=_MitelIdAppPlatAXTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,8))
if mibBuilder.loadTexts:mitelIdAppPlatAXTelephonyServer.setStatus(_A)
_MitelIdAppPlatMXTTelephonyServer_ObjectIdentity=ObjectIdentity
mitelIdAppPlatMXTTelephonyServer=_MitelIdAppPlatMXTTelephonyServer_ObjectIdentity((1,3,6,1,4,1,1027,1,6,9))
if mibBuilder.loadTexts:mitelIdAppPlatMXTTelephonyServer.setStatus(_A)
mibBuilder.exportSymbols('MITEL-APPLICATION-PLATFORM-LIST-MIB',**{'mitelIdApplicationPlatforms':mitelIdApplicationPlatforms,'mitelIdAppPlatManagementApplicationServer':mitelIdAppPlatManagementApplicationServer,'mitelIdAppPlatLXTelephonyServer':mitelIdAppPlatLXTelephonyServer,'mitelIdAppPlatMXTelephonyServer':mitelIdAppPlatMXTelephonyServer,'mitelIdAppPlatCXTelephonyServer':mitelIdAppPlatCXTelephonyServer,'mitelIdAppPlatCXiTelephonyServer':mitelIdAppPlatCXiTelephonyServer,'mitelIdAppPlatLiteTelephonyServer':mitelIdAppPlatLiteTelephonyServer,'mitelIdAppPlatMXeTelephonyServer':mitelIdAppPlatMXeTelephonyServer,'mitelIdAppPlatAXTelephonyServer':mitelIdAppPlatAXTelephonyServer,'mitelIdAppPlatMXTTelephonyServer':mitelIdAppPlatMXTTelephonyServer})