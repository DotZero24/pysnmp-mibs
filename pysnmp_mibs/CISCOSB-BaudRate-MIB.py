_F='read-write'
_E='disable'
_D='enable'
_C='read-only'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlRs232=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,104))
if mibBuilder.loadTexts:rlRs232.setRevisions(('2005-04-14 00:00',))
_RlRs232MibVersion_Type=Integer32
_RlRs232MibVersion_Object=MibScalar
rlRs232MibVersion=_RlRs232MibVersion_Object((1,3,6,1,4,1,9,6,1,101,104,1),_RlRs232MibVersion_Type())
rlRs232MibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRs232MibVersion.setStatus(_B)
class _RlRs232AutoBaudRateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_RlRs232AutoBaudRateStatus_Type.__name__=_A
_RlRs232AutoBaudRateStatus_Object=MibScalar
rlRs232AutoBaudRateStatus=_RlRs232AutoBaudRateStatus_Object((1,3,6,1,4,1,9,6,1,101,104,2),_RlRs232AutoBaudRateStatus_Type())
rlRs232AutoBaudRateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlRs232AutoBaudRateStatus.setStatus(_B)
class _RlRs232AutoBaudRateStatusAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_RlRs232AutoBaudRateStatusAfterReset_Type.__name__=_A
_RlRs232AutoBaudRateStatusAfterReset_Object=MibScalar
rlRs232AutoBaudRateStatusAfterReset=_RlRs232AutoBaudRateStatusAfterReset_Object((1,3,6,1,4,1,9,6,1,101,104,3),_RlRs232AutoBaudRateStatusAfterReset_Type())
rlRs232AutoBaudRateStatusAfterReset.setMaxAccess(_F)
if mibBuilder.loadTexts:rlRs232AutoBaudRateStatusAfterReset.setStatus(_B)
class _RlRs232BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('baud2400',1),('baud4800',2),('baud9600',3),('baud19200',4),('baud38400',5),('baud57600',6),('baud115200',7)))
_RlRs232BaudRate_Type.__name__=_A
_RlRs232BaudRate_Object=MibScalar
rlRs232BaudRate=_RlRs232BaudRate_Object((1,3,6,1,4,1,9,6,1,101,104,4),_RlRs232BaudRate_Type())
rlRs232BaudRate.setMaxAccess(_F)
if mibBuilder.loadTexts:rlRs232BaudRate.setStatus(_B)
mibBuilder.exportSymbols('CISCOSB-BaudRate-MIB',**{'rlRs232':rlRs232,'rlRs232MibVersion':rlRs232MibVersion,'rlRs232AutoBaudRateStatus':rlRs232AutoBaudRateStatus,'rlRs232AutoBaudRateStatusAfterReset':rlRs232AutoBaudRateStatusAfterReset,'rlRs232BaudRate':rlRs232BaudRate})