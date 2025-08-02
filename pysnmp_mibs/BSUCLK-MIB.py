_F='disable'
_E='enable'
_D='Integer32'
_C='read-write'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bsu,=mibBuilder.importSymbols('ANIROOT-MIB','bsu')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
aniBsuClock=ModuleIdentity((1,3,6,1,4,1,4325,3,4))
class _AniBsuClkSntpTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_AniBsuClkSntpTimeZone_Type.__name__=_B
_AniBsuClkSntpTimeZone_Object=MibScalar
aniBsuClkSntpTimeZone=_AniBsuClkSntpTimeZone_Object((1,3,6,1,4,1,4325,3,4,1),_AniBsuClkSntpTimeZone_Type())
aniBsuClkSntpTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuClkSntpTimeZone.setStatus(_A)
class _AniBsuClkSntpDstEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AniBsuClkSntpDstEnable_Type.__name__=_D
_AniBsuClkSntpDstEnable_Object=MibScalar
aniBsuClkSntpDstEnable=_AniBsuClkSntpDstEnable_Object((1,3,6,1,4,1,4325,3,4,2),_AniBsuClkSntpDstEnable_Type())
aniBsuClkSntpDstEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuClkSntpDstEnable.setStatus(_A)
class _AniBsuClkSntpDstStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_AniBsuClkSntpDstStart_Type.__name__=_B
_AniBsuClkSntpDstStart_Object=MibScalar
aniBsuClkSntpDstStart=_AniBsuClkSntpDstStart_Object((1,3,6,1,4,1,4325,3,4,3),_AniBsuClkSntpDstStart_Type())
aniBsuClkSntpDstStart.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuClkSntpDstStart.setStatus(_A)
class _AniBsuClkSntpDstEnd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_AniBsuClkSntpDstEnd_Type.__name__=_B
_AniBsuClkSntpDstEnd_Object=MibScalar
aniBsuClkSntpDstEnd=_AniBsuClkSntpDstEnd_Object((1,3,6,1,4,1,4325,3,4,4),_AniBsuClkSntpDstEnd_Type())
aniBsuClkSntpDstEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuClkSntpDstEnd.setStatus(_A)
class _AniBsuClkSntpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AniBsuClkSntpEnable_Type.__name__=_D
_AniBsuClkSntpEnable_Object=MibScalar
aniBsuClkSntpEnable=_AniBsuClkSntpEnable_Object((1,3,6,1,4,1,4325,3,4,5),_AniBsuClkSntpEnable_Type())
aniBsuClkSntpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuClkSntpEnable.setStatus(_A)
class _AniBsuClkManualTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_AniBsuClkManualTime_Type.__name__=_B
_AniBsuClkManualTime_Object=MibScalar
aniBsuClkManualTime=_AniBsuClkManualTime_Object((1,3,6,1,4,1,4325,3,4,6),_AniBsuClkManualTime_Type())
aniBsuClkManualTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aniBsuClkManualTime.setStatus(_A)
class _AniBsuClkCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_AniBsuClkCurrentTime_Type.__name__=_B
_AniBsuClkCurrentTime_Object=MibScalar
aniBsuClkCurrentTime=_AniBsuClkCurrentTime_Object((1,3,6,1,4,1,4325,3,4,7),_AniBsuClkCurrentTime_Type())
aniBsuClkCurrentTime.setMaxAccess('read-only')
if mibBuilder.loadTexts:aniBsuClkCurrentTime.setStatus(_A)
mibBuilder.exportSymbols('BSUCLK-MIB',**{'aniBsuClock':aniBsuClock,'aniBsuClkSntpTimeZone':aniBsuClkSntpTimeZone,'aniBsuClkSntpDstEnable':aniBsuClkSntpDstEnable,'aniBsuClkSntpDstStart':aniBsuClkSntpDstStart,'aniBsuClkSntpDstEnd':aniBsuClkSntpDstEnd,'aniBsuClkSntpEnable':aniBsuClkSntpEnable,'aniBsuClkManualTime':aniBsuClkManualTime,'aniBsuClkCurrentTime':aniBsuClkCurrentTime})