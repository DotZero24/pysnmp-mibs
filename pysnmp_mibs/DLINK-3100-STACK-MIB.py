_F='standalone'
_E='read-write'
_D='rlStackCurrentUnitId'
_C='DLINK-3100-STACK-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rlStack=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,107))
if mibBuilder.loadTexts:rlStack.setRevisions(('2005-04-14 00:00',))
_RlStackActiveUnitIdTable_Object=MibTable
rlStackActiveUnitIdTable=_RlStackActiveUnitIdTable_Object((1,3,6,1,4,1,171,10,94,89,89,107,1))
if mibBuilder.loadTexts:rlStackActiveUnitIdTable.setStatus(_A)
_RlStackActiveUnitIdEntry_Object=MibTableRow
rlStackActiveUnitIdEntry=_RlStackActiveUnitIdEntry_Object((1,3,6,1,4,1,171,10,94,89,89,107,1,1))
rlStackActiveUnitIdEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rlStackActiveUnitIdEntry.setStatus(_A)
_RlStackCurrentUnitId_Type=Integer32
_RlStackCurrentUnitId_Object=MibTableColumn
rlStackCurrentUnitId=_RlStackCurrentUnitId_Object((1,3,6,1,4,1,171,10,94,89,89,107,1,1,1),_RlStackCurrentUnitId_Type())
rlStackCurrentUnitId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlStackCurrentUnitId.setStatus(_A)
class _RlStackActiveUnitIdAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlStackActiveUnitIdAfterReset_Type.__name__=_B
_RlStackActiveUnitIdAfterReset_Object=MibTableColumn
rlStackActiveUnitIdAfterReset=_RlStackActiveUnitIdAfterReset_Object((1,3,6,1,4,1,171,10,94,89,89,107,1,1,2),_RlStackActiveUnitIdAfterReset_Type())
rlStackActiveUnitIdAfterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:rlStackActiveUnitIdAfterReset.setStatus(_A)
class _RlStackUnitModeAfterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('stack',2)))
_RlStackUnitModeAfterReset_Type.__name__=_B
_RlStackUnitModeAfterReset_Object=MibScalar
rlStackUnitModeAfterReset=_RlStackUnitModeAfterReset_Object((1,3,6,1,4,1,171,10,94,89,89,107,2),_RlStackUnitModeAfterReset_Type())
rlStackUnitModeAfterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:rlStackUnitModeAfterReset.setStatus(_A)
class _RlStackUnitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('stack',2)))
_RlStackUnitMode_Type.__name__=_B
_RlStackUnitMode_Object=MibScalar
rlStackUnitMode=_RlStackUnitMode_Object((1,3,6,1,4,1,171,10,94,89,89,107,3),_RlStackUnitMode_Type())
rlStackUnitMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlStackUnitMode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rlStack':rlStack,'rlStackActiveUnitIdTable':rlStackActiveUnitIdTable,'rlStackActiveUnitIdEntry':rlStackActiveUnitIdEntry,_D:rlStackCurrentUnitId,'rlStackActiveUnitIdAfterReset':rlStackActiveUnitIdAfterReset,'rlStackUnitModeAfterReset':rlStackUnitModeAfterReset,'rlStackUnitMode':rlStackUnitMode})