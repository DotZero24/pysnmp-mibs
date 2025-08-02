_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_B,_C)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxDslPortMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,43))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslPortMibObjects_ObjectIdentity=ObjectIdentity
zxDslPortMibObjects=_ZxDslPortMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,43,1))
_ZxDslPortObjects_ObjectIdentity=ObjectIdentity
zxDslPortObjects=_ZxDslPortObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,43,1,1))
_ZxDslPortTable_Object=MibTable
zxDslPortTable=_ZxDslPortTable_Object((1,3,6,1,4,1,3902,1004,43,1,1,10))
if mibBuilder.loadTexts:zxDslPortTable.setStatus(_A)
_ZxDslPortEntry_Object=MibTableRow
zxDslPortEntry=_ZxDslPortEntry_Object((1,3,6,1,4,1,3902,1004,43,1,1,10,1))
zxDslPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zxDslPortEntry.setStatus(_A)
class _ZxDslPortLockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unlock',1),('lock',2)))
_ZxDslPortLockStatus_Type.__name__=_D
_ZxDslPortLockStatus_Object=MibTableColumn
zxDslPortLockStatus=_ZxDslPortLockStatus_Object((1,3,6,1,4,1,3902,1004,43,1,1,10,1,1),_ZxDslPortLockStatus_Type())
zxDslPortLockStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxDslPortLockStatus.setStatus(_A)
_ZxDslPortTrapObjects_ObjectIdentity=ObjectIdentity
zxDslPortTrapObjects=_ZxDslPortTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,43,1,3))
mibBuilder.exportSymbols('ZTE-DSL-PORT-MIB',**{'zte':zte,'zxDsl':zxDsl,'zxDslPortMib':zxDslPortMib,'zxDslPortMibObjects':zxDslPortMibObjects,'zxDslPortObjects':zxDslPortObjects,'zxDslPortTable':zxDslPortTable,'zxDslPortEntry':zxDslPortEntry,'zxDslPortLockStatus':zxDslPortLockStatus,'zxDslPortTrapObjects':zxDslPortTrapObjects})