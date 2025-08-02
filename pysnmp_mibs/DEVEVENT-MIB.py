_D='Integer32'
_C='current'
_B='read-write'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
device,=mibBuilder.importSymbols('ANIROOT-MIB','device')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
aniDevEvent=ModuleIdentity((1,3,6,1,4,1,4325,2,6))
_AniDevEvNotify_ObjectIdentity=ObjectIdentity
aniDevEvNotify=_AniDevEvNotify_ObjectIdentity((1,3,6,1,4,1,4325,2,6,2))
class _AniDevEmailSending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AniDevEmailSending_Type.__name__=_D
_AniDevEmailSending_Object=MibScalar
aniDevEmailSending=_AniDevEmailSending_Object((1,3,6,1,4,1,4325,2,6,2,1),_AniDevEmailSending_Type())
aniDevEmailSending.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevEmailSending.setStatus(_C)
class _AniDevEmailSender_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevEmailSender_Type.__name__=_A
_AniDevEmailSender_Object=MibScalar
aniDevEmailSender=_AniDevEmailSender_Object((1,3,6,1,4,1,4325,2,6,2,2),_AniDevEmailSender_Type())
aniDevEmailSender.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevEmailSender.setStatus(_C)
class _AniDevDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevDomainName_Type.__name__=_A
_AniDevDomainName_Object=MibScalar
aniDevDomainName=_AniDevDomainName_Object((1,3,6,1,4,1,4325,2,6,2,3),_AniDevDomainName_Type())
aniDevDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevDomainName.setStatus(_C)
class _AniDevEmailReceiver1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevEmailReceiver1_Type.__name__=_A
_AniDevEmailReceiver1_Object=MibScalar
aniDevEmailReceiver1=_AniDevEmailReceiver1_Object((1,3,6,1,4,1,4325,2,6,2,4),_AniDevEmailReceiver1_Type())
aniDevEmailReceiver1.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevEmailReceiver1.setStatus(_C)
class _AniDevEmailReceiver2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AniDevEmailReceiver2_Type.__name__=_A
_AniDevEmailReceiver2_Object=MibScalar
aniDevEmailReceiver2=_AniDevEmailReceiver2_Object((1,3,6,1,4,1,4325,2,6,2,5),_AniDevEmailReceiver2_Type())
aniDevEmailReceiver2.setMaxAccess(_B)
if mibBuilder.loadTexts:aniDevEmailReceiver2.setStatus(_C)
mibBuilder.exportSymbols('DEVEVENT-MIB',**{'aniDevEvent':aniDevEvent,'aniDevEvNotify':aniDevEvNotify,'aniDevEmailSending':aniDevEmailSending,'aniDevEmailSender':aniDevEmailSender,'aniDevDomainName':aniDevDomainName,'aniDevEmailReceiver1':aniDevEmailReceiver1,'aniDevEmailReceiver2':aniDevEmailReceiver2})