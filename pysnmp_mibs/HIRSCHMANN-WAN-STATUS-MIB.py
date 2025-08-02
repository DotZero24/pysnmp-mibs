_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanStatusMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,3))
if mibBuilder.loadTexts:hmWanStatusMib.setRevisions(('2015-02-13 00:00',))
class _HmWanStatusMBusOverload1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_HmWanStatusMBusOverload1_Type.__name__=_C
_HmWanStatusMBusOverload1_Object=MibScalar
hmWanStatusMBusOverload1=_HmWanStatusMBusOverload1_Object((1,3,6,1,4,1,248,40,1,3,1),_HmWanStatusMBusOverload1_Type())
hmWanStatusMBusOverload1.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanStatusMBusOverload1.setStatus(_B)
class _HmWanStatusMBusOverload2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_HmWanStatusMBusOverload2_Type.__name__=_C
_HmWanStatusMBusOverload2_Object=MibScalar
hmWanStatusMBusOverload2=_HmWanStatusMBusOverload2_Object((1,3,6,1,4,1,248,40,1,3,2),_HmWanStatusMBusOverload2_Type())
hmWanStatusMBusOverload2.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanStatusMBusOverload2.setStatus(_B)
_HmWanStatusTemperature_Type=Integer32
_HmWanStatusTemperature_Object=MibScalar
hmWanStatusTemperature=_HmWanStatusTemperature_Object((1,3,6,1,4,1,248,40,1,3,3),_HmWanStatusTemperature_Type())
hmWanStatusTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanStatusTemperature.setStatus(_B)
_HmWanStatusVoltage_Type=Integer32
_HmWanStatusVoltage_Object=MibScalar
hmWanStatusVoltage=_HmWanStatusVoltage_Object((1,3,6,1,4,1,248,40,1,3,4),_HmWanStatusVoltage_Type())
hmWanStatusVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanStatusVoltage.setStatus(_B)
mibBuilder.exportSymbols('HIRSCHMANN-WAN-STATUS-MIB',**{'hmWanStatusMib':hmWanStatusMib,'hmWanStatusMBusOverload1':hmWanStatusMBusOverload1,'hmWanStatusMBusOverload2':hmWanStatusMBusOverload2,'hmWanStatusTemperature':hmWanStatusTemperature,'hmWanStatusVoltage':hmWanStatusVoltage})