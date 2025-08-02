_E='unknown'
_D='ieee802dot1x'
_C='localAndProfile'
_B='profile'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisModules,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisTextualConventions=ModuleIdentity((1,3,6,1,4,1,8744,4,1))
class ColubrisAuthenticationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),(_B,2),(_C,3)))
class ColubrisUsersAuthenticationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('local',1),(_B,2),(_C,3)))
class ColubrisUsersAuthenticationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mac',1),(_D,2),('html',3)))
class ColubrisNotificationEnable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
class ColubrisProfileIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ColubrisProfileIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ColubrisServerIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ColubrisServerIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ColubrisSSID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class ColubrisSSIDOrNone(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class ColubrisSecurity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),('none',1),('wep',2),(_D,3),('ieee802dot1xWithWep',4),('wpa',5),('wpaPsk',6)))
class ColubrisPriorityQueue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('normal',2),('high',3),('veryHigh',4)))
class ColubrisDataRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_E,0),('rateLowestAvailable',1),('rate1Meg',2),('rate2Meg',3),('rate5dot5Meg',4),('rate6Meg',5),('rate9Meg',6),('rate11Meg',7),('rate12Meg',8),('rate18Meg',9),('rate24Meg',10),('rate36Meg',11),('rate48Meg',12),('rate54Meg',13),('rateHighestAvailable',14)))
class ColubrisRadioType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6,7,8,9)));namedValues=NamedValues(*(('cm6',1),('cm9',2),('sunfish',3),('mb82',5),('ar2317',6),('xb114',7),('bcm43460',8),('cus223',9)))
mibBuilder.exportSymbols('COLUBRIS-TC',**{'ColubrisAuthenticationMode':ColubrisAuthenticationMode,'ColubrisUsersAuthenticationMode':ColubrisUsersAuthenticationMode,'ColubrisUsersAuthenticationType':ColubrisUsersAuthenticationType,'ColubrisNotificationEnable':ColubrisNotificationEnable,'ColubrisProfileIndex':ColubrisProfileIndex,'ColubrisProfileIndexOrZero':ColubrisProfileIndexOrZero,'ColubrisServerIndex':ColubrisServerIndex,'ColubrisServerIndexOrZero':ColubrisServerIndexOrZero,'ColubrisSSID':ColubrisSSID,'ColubrisSSIDOrNone':ColubrisSSIDOrNone,'ColubrisSecurity':ColubrisSecurity,'ColubrisPriorityQueue':ColubrisPriorityQueue,'ColubrisDataRate':ColubrisDataRate,'ColubrisRadioType':ColubrisRadioType,'colubrisTextualConventions':colubrisTextualConventions})