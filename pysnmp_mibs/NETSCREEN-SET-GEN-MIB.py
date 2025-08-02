_F='enabled'
_E='disable'
_D='Integer32'
_C='DisplayString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenSetGenMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,1))
if mibBuilder.loadTexts:netscreenSetGenMibModule.setRevisions(('2005-08-12 00:00','2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetGeneral_ObjectIdentity=ObjectIdentity
nsSetGeneral=_NsSetGeneral_ObjectIdentity((1,3,6,1,4,1,3224,7,1))
_NsSetGenSysIp_Type=IpAddress
_NsSetGenSysIp_Object=MibScalar
nsSetGenSysIp=_NsSetGenSysIp_Object((1,3,6,1,4,1,3224,7,1,1),_NsSetGenSysIp_Type())
nsSetGenSysIp.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenSysIp.setStatus('obsolete')
class _NsSetGenHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetGenHostName_Type.__name__=_C
_NsSetGenHostName_Object=MibScalar
nsSetGenHostName=_NsSetGenHostName_Object((1,3,6,1,4,1,3224,7,1,2),_NsSetGenHostName_Type())
nsSetGenHostName.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenHostName.setStatus(_B)
class _NsSetGenDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetGenDomain_Type.__name__=_C
_NsSetGenDomain_Object=MibScalar
nsSetGenDomain=_NsSetGenDomain_Object((1,3,6,1,4,1,3224,7,1,3),_NsSetGenDomain_Type())
nsSetGenDomain.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenDomain.setStatus(_B)
class _NsSetGenOpMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetGenOpMode_Type.__name__=_C
_NsSetGenOpMode_Object=MibScalar
nsSetGenOpMode=_NsSetGenOpMode_Object((1,3,6,1,4,1,3224,7,1,4),_NsSetGenOpMode_Type())
nsSetGenOpMode.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenOpMode.setStatus(_B)
class _NsSetGenSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NsSetGenSwVer_Type.__name__=_C
_NsSetGenSwVer_Object=MibScalar
nsSetGenSwVer=_NsSetGenSwVer_Object((1,3,6,1,4,1,3224,7,1,5),_NsSetGenSwVer_Type())
nsSetGenSwVer.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenSwVer.setStatus(_B)
class _NsSetGenLicInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetGenLicInfo_Type.__name__=_C
_NsSetGenLicInfo_Object=MibScalar
nsSetGenLicInfo=_NsSetGenLicInfo_Object((1,3,6,1,4,1,3224,7,1,6),_NsSetGenLicInfo_Type())
nsSetGenLicInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenLicInfo.setStatus(_B)
class _NsSetGenSCSAdminEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsSetGenSCSAdminEnable_Type.__name__=_D
_NsSetGenSCSAdminEnable_Object=MibScalar
nsSetGenSCSAdminEnable=_NsSetGenSCSAdminEnable_Object((1,3,6,1,4,1,3224,7,1,7),_NsSetGenSCSAdminEnable_Type())
nsSetGenSCSAdminEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenSCSAdminEnable.setStatus(_B)
class _NsSetGenDropSelfLogPac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsSetGenDropSelfLogPac_Type.__name__=_D
_NsSetGenDropSelfLogPac_Object=MibScalar
nsSetGenDropSelfLogPac=_NsSetGenDropSelfLogPac_Object((1,3,6,1,4,1,3224,7,1,8),_NsSetGenDropSelfLogPac_Type())
nsSetGenDropSelfLogPac.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetGenDropSelfLogPac.setStatus(_B)
mibBuilder.exportSymbols('NETSCREEN-SET-GEN-MIB',**{'netscreenSetGenMibModule':netscreenSetGenMibModule,'nsSetGeneral':nsSetGeneral,'nsSetGenSysIp':nsSetGenSysIp,'nsSetGenHostName':nsSetGenHostName,'nsSetGenDomain':nsSetGenDomain,'nsSetGenOpMode':nsSetGenOpMode,'nsSetGenSwVer':nsSetGenSwVer,'nsSetGenLicInfo':nsSetGenLicInfo,'nsSetGenSCSAdminEnable':nsSetGenSCSAdminEnable,'nsSetGenDropSelfLogPac':nsSetGenDropSelfLogPac})