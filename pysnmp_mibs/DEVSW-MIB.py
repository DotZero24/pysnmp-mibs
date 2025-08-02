_C='current'
_B='read-only'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
aniDevSoftware=ModuleIdentity((1,3,6,1,4,1,4325,2,2))
class _AniDevSwConfigFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevSwConfigFile_Type.__name__=_A
_AniDevSwConfigFile_Object=MibScalar
aniDevSwConfigFile=_AniDevSwConfigFile_Object((1,3,6,1,4,1,4325,2,2,1),_AniDevSwConfigFile_Type())
aniDevSwConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSwConfigFile.setStatus(_C)
class _AniDevSwSystemSoftwareFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevSwSystemSoftwareFile_Type.__name__=_A
_AniDevSwSystemSoftwareFile_Object=MibScalar
aniDevSwSystemSoftwareFile=_AniDevSwSystemSoftwareFile_Object((1,3,6,1,4,1,4325,2,2,2),_AniDevSwSystemSoftwareFile_Type())
aniDevSwSystemSoftwareFile.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSwSystemSoftwareFile.setStatus(_C)
class _AniDevSwWssSoftwareFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevSwWssSoftwareFile_Type.__name__=_A
_AniDevSwWssSoftwareFile_Object=MibScalar
aniDevSwWssSoftwareFile=_AniDevSwWssSoftwareFile_Object((1,3,6,1,4,1,4325,2,2,3),_AniDevSwWssSoftwareFile_Type())
aniDevSwWssSoftwareFile.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSwWssSoftwareFile.setStatus(_C)
class _AniDevSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AniDevSwVersion_Type.__name__=_A
_AniDevSwVersion_Object=MibScalar
aniDevSwVersion=_AniDevSwVersion_Object((1,3,6,1,4,1,4325,2,2,4),_AniDevSwVersion_Type())
aniDevSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSwVersion.setStatus(_C)
_AniDevSwBuild_Type=Integer32
_AniDevSwBuild_Object=MibScalar
aniDevSwBuild=_AniDevSwBuild_Object((1,3,6,1,4,1,4325,2,2,5),_AniDevSwBuild_Type())
aniDevSwBuild.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSwBuild.setStatus(_C)
class _AniDevSwBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_AniDevSwBuildDate_Type.__name__=_A
_AniDevSwBuildDate_Object=MibScalar
aniDevSwBuildDate=_AniDevSwBuildDate_Object((1,3,6,1,4,1,4325,2,2,6),_AniDevSwBuildDate_Type())
aniDevSwBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevSwBuildDate.setStatus(_C)
mibBuilder.exportSymbols('DEVSW-MIB',**{'aniDevSoftware':aniDevSoftware,'aniDevSwConfigFile':aniDevSwConfigFile,'aniDevSwSystemSoftwareFile':aniDevSwSystemSoftwareFile,'aniDevSwWssSoftwareFile':aniDevSwWssSoftwareFile,'aniDevSwVersion':aniDevSwVersion,'aniDevSwBuild':aniDevSwBuild,'aniDevSwBuildDate':aniDevSwBuildDate})