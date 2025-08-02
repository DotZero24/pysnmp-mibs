_C='enable'
_B='disable'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniTextualConventions=ModuleIdentity((1,3,6,1,4,1,4874,2,2,1))
if mibBuilder.loadTexts:juniTextualConventions.setRevisions(('2005-12-21 20:13','2005-11-18 22:30','2004-12-03 22:12','2003-11-12 22:31','2002-09-16 21:44','2002-04-04 16:35','2001-03-08 22:26','1999-12-12 00:00','1999-07-14 00:00','1998-11-13 00:00'))
class JuniEnable(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_B,0),(_C,1)))
class JuniName(TextualConvention,OctetString):status=_A;displayHint='256a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class JuniVrfName(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class JuniNextIfIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JuniIpAddrLessIf(TextualConvention,IpAddress):status=_A
class JuniTimeSlotMap(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class JuniAcctngAdminType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class JuniAcctngOperType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_B,0),(_C,1),('notSupported',2)))
class JuniLogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('off',-1),('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
class JuniSetMap(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class JuniInterfaceDescrFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('proprietary',0),('industryCommon',1)))
class JuniInterfaceLocation(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class JuniInterfaceLocationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('slotPort',1),('slotAdapterPort',2),('adapterPort',3)))
class JuniInterfaceLocationValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
class JuniVrfGroupName(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class JuniTimeFilter(TextualConvention,TimeTicks):status=_A
class JuniNibbleConfig(TextualConvention,Integer32):status=_A
mibBuilder.exportSymbols('Juniper-TC',**{'JuniEnable':JuniEnable,'JuniName':JuniName,'JuniVrfName':JuniVrfName,'JuniNextIfIndex':JuniNextIfIndex,'JuniIpAddrLessIf':JuniIpAddrLessIf,'JuniTimeSlotMap':JuniTimeSlotMap,'JuniAcctngAdminType':JuniAcctngAdminType,'JuniAcctngOperType':JuniAcctngOperType,'JuniLogSeverity':JuniLogSeverity,'JuniSetMap':JuniSetMap,'JuniInterfaceDescrFormat':JuniInterfaceDescrFormat,'JuniInterfaceLocation':JuniInterfaceLocation,'JuniInterfaceLocationType':JuniInterfaceLocationType,'JuniInterfaceLocationValue':JuniInterfaceLocationValue,'JuniVrfGroupName':JuniVrfGroupName,'JuniTimeFilter':JuniTimeFilter,'JuniNibbleConfig':JuniNibbleConfig,'juniTextualConventions':juniTextualConventions})