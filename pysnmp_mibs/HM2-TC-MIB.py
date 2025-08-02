_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2TcMib=ModuleIdentity((1,3,6,1,4,1,248,11,1))
if mibBuilder.loadTexts:hm2TcMib.setRevisions(('2011-03-16 00:00',))
class HmEnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
class HmActionValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noop',1),('action',2)))
class HmTimeHHMM24(TextualConvention,OctetString):status=_A;displayHint='5a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
class HmTimeSeconds1970(TextualConvention,Unsigned32):status=_A
class HmLargeDisplayString(TextualConvention,OctetString):status=_A;displayHint='1024a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
class HmExtraLargeDisplayString(TextualConvention,OctetString):status=_A;displayHint='1400a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1400))
class HmAccessLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readWrite',1),('readOnly',2)))
_Hirschmann_ObjectIdentity=ObjectIdentity
hirschmann=_Hirschmann_ObjectIdentity((1,3,6,1,4,1,248))
_Hm2ConfigurationMibs_ObjectIdentity=ObjectIdentity
hm2ConfigurationMibs=_Hm2ConfigurationMibs_ObjectIdentity((1,3,6,1,4,1,248,11))
_Hm2PlatformMibs_ObjectIdentity=ObjectIdentity
hm2PlatformMibs=_Hm2PlatformMibs_ObjectIdentity((1,3,6,1,4,1,248,12))
mibBuilder.exportSymbols('HM2-TC-MIB',**{'HmEnabledStatus':HmEnabledStatus,'HmActionValue':HmActionValue,'HmTimeHHMM24':HmTimeHHMM24,'HmTimeSeconds1970':HmTimeSeconds1970,'HmLargeDisplayString':HmLargeDisplayString,'HmExtraLargeDisplayString':HmExtraLargeDisplayString,'HmAccessLevel':HmAccessLevel,'hirschmann':hirschmann,'hm2ConfigurationMibs':hm2ConfigurationMibs,'hm2TcMib':hm2TcMib,'hm2PlatformMibs':hm2PlatformMibs})