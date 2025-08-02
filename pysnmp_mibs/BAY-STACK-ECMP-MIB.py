_D='bsEcmpConfigRoutingProtocol'
_C='BAY-STACK-ECMP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackEcmpMib=ModuleIdentity((1,3,6,1,4,1,45,5,15))
if mibBuilder.loadTexts:bayStackEcmpMib.setRevisions(('2016-09-06 00:00','2012-06-01 00:00','2005-09-09 00:00'))
_BsEcmpNotifications_ObjectIdentity=ObjectIdentity
bsEcmpNotifications=_BsEcmpNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,15,0))
_BsEcmpObjects_ObjectIdentity=ObjectIdentity
bsEcmpObjects=_BsEcmpObjects_ObjectIdentity((1,3,6,1,4,1,45,5,15,1))
_BsEcmpScalars_ObjectIdentity=ObjectIdentity
bsEcmpScalars=_BsEcmpScalars_ObjectIdentity((1,3,6,1,4,1,45,5,15,1,1))
_BsEcmpConfigTable_Object=MibTable
bsEcmpConfigTable=_BsEcmpConfigTable_Object((1,3,6,1,4,1,45,5,15,1,2))
if mibBuilder.loadTexts:bsEcmpConfigTable.setStatus(_A)
_BsEcmpConfigEntry_Object=MibTableRow
bsEcmpConfigEntry=_BsEcmpConfigEntry_Object((1,3,6,1,4,1,45,5,15,1,2,1))
bsEcmpConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bsEcmpConfigEntry.setStatus(_A)
class _BsEcmpConfigRoutingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('rip',2),('ospf',3),('bgp',4),('isis',5)))
_BsEcmpConfigRoutingProtocol_Type.__name__=_B
_BsEcmpConfigRoutingProtocol_Object=MibTableColumn
bsEcmpConfigRoutingProtocol=_BsEcmpConfigRoutingProtocol_Object((1,3,6,1,4,1,45,5,15,1,2,1,1),_BsEcmpConfigRoutingProtocol_Type())
bsEcmpConfigRoutingProtocol.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsEcmpConfigRoutingProtocol.setStatus(_A)
class _BsEcmpConfigMaxPath_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BsEcmpConfigMaxPath_Type.__name__=_B
_BsEcmpConfigMaxPath_Object=MibTableColumn
bsEcmpConfigMaxPath=_BsEcmpConfigMaxPath_Object((1,3,6,1,4,1,45,5,15,1,2,1,2),_BsEcmpConfigMaxPath_Type())
bsEcmpConfigMaxPath.setMaxAccess('read-write')
if mibBuilder.loadTexts:bsEcmpConfigMaxPath.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bayStackEcmpMib':bayStackEcmpMib,'bsEcmpNotifications':bsEcmpNotifications,'bsEcmpObjects':bsEcmpObjects,'bsEcmpScalars':bsEcmpScalars,'bsEcmpConfigTable':bsEcmpConfigTable,'bsEcmpConfigEntry':bsEcmpConfigEntry,_D:bsEcmpConfigRoutingProtocol,'bsEcmpConfigMaxPath':bsEcmpConfigMaxPath})