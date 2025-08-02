_D='smQoSClassMapExtEntry'
_C='ARICENT-QoSEXT-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsQoSClassMapEntry,=mibBuilder.importSymbols('ARICENT-DIFFSERV-MIB','fsQoSClassMapEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
smfutqos=ModuleIdentity((1,3,6,1,4,1,29601,100,1,3))
_SmQoSClass_ObjectIdentity=ObjectIdentity
smQoSClass=_SmQoSClass_ObjectIdentity((1,3,6,1,4,1,29601,100,1,3,1))
_SmQoSClassMapExtTable_Object=MibTable
smQoSClassMapExtTable=_SmQoSClassMapExtTable_Object((1,3,6,1,4,1,29601,100,1,3,1,1))
if mibBuilder.loadTexts:smQoSClassMapExtTable.setStatus(_A)
_SmQoSClassMapExtEntry_Object=MibTableRow
smQoSClassMapExtEntry=_SmQoSClassMapExtEntry_Object((1,3,6,1,4,1,29601,100,1,3,1,1,1))
if mibBuilder.loadTexts:smQoSClassMapExtEntry.setStatus(_A)
class _SmQoSExtClassMapYpDeiBit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('reset',0),('set',1),('None',2)))
_SmQoSExtClassMapYpDeiBit_Type.__name__=_B
_SmQoSExtClassMapYpDeiBit_Object=MibTableColumn
smQoSExtClassMapYpDeiBit=_SmQoSExtClassMapYpDeiBit_Object((1,3,6,1,4,1,29601,100,1,3,1,1,1,1),_SmQoSExtClassMapYpDeiBit_Type())
smQoSExtClassMapYpDeiBit.setMaxAccess('read-write')
if mibBuilder.loadTexts:smQoSExtClassMapYpDeiBit.setStatus(_A)
fsQoSClassMapEntry.registerAugmentions((_C,_D))
smQoSClassMapExtEntry.setIndexNames(*fsQoSClassMapEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'smfutqos':smfutqos,'smQoSClass':smQoSClass,'smQoSClassMapExtTable':smQoSClassMapExtTable,_D:smQoSClassMapExtEntry,'smQoSExtClassMapYpDeiBit':smQoSExtClassMapYpDeiBit})