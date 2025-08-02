_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
utModules,=mibBuilder.importSymbols('UTS-COMMON-MIB','utModules')
utCommonTCModules=ModuleIdentity((1,3,6,1,4,1,1949,1,1,1,3))
if mibBuilder.loadTexts:utCommonTCModules.setRevisions(('2002-04-28 00:00','2003-12-15 13:51'))
class ActionCorrelationNo(TextualConvention,OctetString):status=_A
class ActionMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sychronization',0),('asychronization',1)))
class ActionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('processing',0),('action-success',1),('action-failure',2),('action-partial-failure',3)))
class AdministrativeState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('lock',0),('unlock',1),('shutdown',2)))
class AlarmStatus(TextualConvention,Unsigned32):status=_A
class AvailableStatus(TextualConvention,Unsigned32):status=_A
class BOOL(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
class BYTE(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ControlStatus(TextualConvention,Unsigned32):status=_A
class OperationalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class ProceduralStatus(TextualConvention,Unsigned32):status=_A
class StandbyStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hot-standby',1),('cold-standby',2),('providing-service',3)))
class UsageState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('idle',0),('active',1),('busy',2),('not-available',3)))
class WORD(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
mibBuilder.exportSymbols('UTS-COMMON-TC-MIB',**{'ActionCorrelationNo':ActionCorrelationNo,'ActionMode':ActionMode,'ActionStatus':ActionStatus,'AdministrativeState':AdministrativeState,'AlarmStatus':AlarmStatus,'AvailableStatus':AvailableStatus,'BOOL':BOOL,'BYTE':BYTE,'ControlStatus':ControlStatus,'OperationalState':OperationalState,'ProceduralStatus':ProceduralStatus,'StandbyStatus':StandbyStatus,'UsageState':UsageState,'WORD':WORD,'utCommonTCModules':utCommonTCModules})