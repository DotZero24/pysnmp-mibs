_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
datacomDevicesMIBs,=mibBuilder.importSymbols('DATACOM-SMI','datacomDevicesMIBs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dmosRebootMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,10))
if mibBuilder.loadTexts:dmosRebootMIB.setRevisions(('2019-10-17 00:00',))
class String(TextualConvention,OctetString):status=_A;displayHint='1t'
_RebootReason_Type=String
_RebootReason_Object=MibScalar
rebootReason=_RebootReason_Object((1,3,6,1,4,1,3709,3,6,10,1),_RebootReason_Type())
rebootReason.setMaxAccess('read-only')
if mibBuilder.loadTexts:rebootReason.setStatus(_A)
mibBuilder.exportSymbols('DMOS-REBOOT-MIB',**{'String':String,'dmosRebootMIB':dmosRebootMIB,'rebootReason':rebootReason})