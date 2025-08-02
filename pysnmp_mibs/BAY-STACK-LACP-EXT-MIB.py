_D='bsleDot3adAggPortExtIndex'
_C='BAY-STACK-LACP-EXT-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackLacpExtMib=ModuleIdentity((1,3,6,1,4,1,45,5,7))
if mibBuilder.loadTexts:bayStackLacpExtMib.setRevisions(('2005-11-14 00:00','2004-06-04 00:00'))
_BsleNotifications_ObjectIdentity=ObjectIdentity
bsleNotifications=_BsleNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,7,0))
_BsleObjects_ObjectIdentity=ObjectIdentity
bsleObjects=_BsleObjects_ObjectIdentity((1,3,6,1,4,1,45,5,7,1))
_BsleScalars_ObjectIdentity=ObjectIdentity
bsleScalars=_BsleScalars_ObjectIdentity((1,3,6,1,4,1,45,5,7,1,1))
class _BsleDot3adCompatibilityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('advanced',2)))
_BsleDot3adCompatibilityMode_Type.__name__=_B
_BsleDot3adCompatibilityMode_Object=MibScalar
bsleDot3adCompatibilityMode=_BsleDot3adCompatibilityMode_Object((1,3,6,1,4,1,45,5,7,1,1,1),_BsleDot3adCompatibilityMode_Type())
bsleDot3adCompatibilityMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:bsleDot3adCompatibilityMode.setStatus(_A)
_BsleDot3adAggPortExtTable_Object=MibTable
bsleDot3adAggPortExtTable=_BsleDot3adAggPortExtTable_Object((1,3,6,1,4,1,45,5,7,2))
if mibBuilder.loadTexts:bsleDot3adAggPortExtTable.setStatus(_A)
_BsleDot3adAggPortExtEntry_Object=MibTableRow
bsleDot3adAggPortExtEntry=_BsleDot3adAggPortExtEntry_Object((1,3,6,1,4,1,45,5,7,2,1))
bsleDot3adAggPortExtEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bsleDot3adAggPortExtEntry.setStatus(_A)
_BsleDot3adAggPortExtIndex_Type=InterfaceIndex
_BsleDot3adAggPortExtIndex_Object=MibTableColumn
bsleDot3adAggPortExtIndex=_BsleDot3adAggPortExtIndex_Object((1,3,6,1,4,1,45,5,7,2,1,1),_BsleDot3adAggPortExtIndex_Type())
bsleDot3adAggPortExtIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsleDot3adAggPortExtIndex.setStatus(_A)
_BsleDot3adAggPortExtAdminEnabled_Type=TruthValue
_BsleDot3adAggPortExtAdminEnabled_Object=MibTableColumn
bsleDot3adAggPortExtAdminEnabled=_BsleDot3adAggPortExtAdminEnabled_Object((1,3,6,1,4,1,45,5,7,2,1,2),_BsleDot3adAggPortExtAdminEnabled_Type())
bsleDot3adAggPortExtAdminEnabled.setMaxAccess('read-create')
if mibBuilder.loadTexts:bsleDot3adAggPortExtAdminEnabled.setStatus(_A)
_BsleDot3adAggPortExtOperEnabled_Type=TruthValue
_BsleDot3adAggPortExtOperEnabled_Object=MibTableColumn
bsleDot3adAggPortExtOperEnabled=_BsleDot3adAggPortExtOperEnabled_Object((1,3,6,1,4,1,45,5,7,2,1,3),_BsleDot3adAggPortExtOperEnabled_Type())
bsleDot3adAggPortExtOperEnabled.setMaxAccess('read-only')
if mibBuilder.loadTexts:bsleDot3adAggPortExtOperEnabled.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bayStackLacpExtMib':bayStackLacpExtMib,'bsleNotifications':bsleNotifications,'bsleObjects':bsleObjects,'bsleScalars':bsleScalars,'bsleDot3adCompatibilityMode':bsleDot3adCompatibilityMode,'bsleDot3adAggPortExtTable':bsleDot3adAggPortExtTable,'bsleDot3adAggPortExtEntry':bsleDot3adAggPortExtEntry,_D:bsleDot3adAggPortExtIndex,'bsleDot3adAggPortExtAdminEnabled':bsleDot3adAggPortExtAdminEnabled,'bsleDot3adAggPortExtOperEnabled':bsleDot3adAggPortExtOperEnabled})