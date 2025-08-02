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
netscreenSetEmailMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,7))
if mibBuilder.loadTexts:netscreenSetEmailMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetEmail_ObjectIdentity=ObjectIdentity
nsSetEmail=_NsSetEmail_ObjectIdentity((1,3,6,1,4,1,3224,7,7))
class _NsSetEmailEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsSetEmailEnable_Type.__name__=_D
_NsSetEmailEnable_Object=MibScalar
nsSetEmailEnable=_NsSetEmailEnable_Object((1,3,6,1,4,1,3224,7,7,1),_NsSetEmailEnable_Type())
nsSetEmailEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetEmailEnable.setStatus(_B)
class _NsSetEmailSMTP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetEmailSMTP_Type.__name__=_C
_NsSetEmailSMTP_Object=MibScalar
nsSetEmailSMTP=_NsSetEmailSMTP_Object((1,3,6,1,4,1,3224,7,7,2),_NsSetEmailSMTP_Type())
nsSetEmailSMTP.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetEmailSMTP.setStatus(_B)
class _NsSetEmailLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NsSetEmailLog_Type.__name__=_D
_NsSetEmailLog_Object=MibScalar
nsSetEmailLog=_NsSetEmailLog_Object((1,3,6,1,4,1,3224,7,7,3),_NsSetEmailLog_Type())
nsSetEmailLog.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetEmailLog.setStatus(_B)
class _NsSetEmailAddr1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NsSetEmailAddr1_Type.__name__=_C
_NsSetEmailAddr1_Object=MibScalar
nsSetEmailAddr1=_NsSetEmailAddr1_Object((1,3,6,1,4,1,3224,7,7,4),_NsSetEmailAddr1_Type())
nsSetEmailAddr1.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetEmailAddr1.setStatus(_B)
class _NsSetEmailAddr2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NsSetEmailAddr2_Type.__name__=_C
_NsSetEmailAddr2_Object=MibScalar
nsSetEmailAddr2=_NsSetEmailAddr2_Object((1,3,6,1,4,1,3224,7,7,5),_NsSetEmailAddr2_Type())
nsSetEmailAddr2.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetEmailAddr2.setStatus(_B)
mibBuilder.exportSymbols('NETSCREEN-SET-EMAIL-MIB',**{'netscreenSetEmailMibModule':netscreenSetEmailMibModule,'nsSetEmail':nsSetEmail,'nsSetEmailEnable':nsSetEmailEnable,'nsSetEmailSMTP':nsSetEmailSMTP,'nsSetEmailLog':nsSetEmailLog,'nsSetEmailAddr1':nsSetEmailAddr1,'nsSetEmailAddr2':nsSetEmailAddr2})