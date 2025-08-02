_E='h3cPPriProtocolType'
_D='A3COM-HUAWEI-PROT-PRIORITY-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cProtocolPriority=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,37))
if mibBuilder.loadTexts:h3cProtocolPriority.setRevisions(('2005-01-17 16:33',))
_H3cProtocolPriorityObjects_ObjectIdentity=ObjectIdentity
h3cProtocolPriorityObjects=_H3cProtocolPriorityObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,37,1))
_H3cPPri_ObjectIdentity=ObjectIdentity
h3cPPri=_H3cPPri_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,37,1,1))
_H3cProtocolPriorityTable_Object=MibTable
h3cProtocolPriorityTable=_H3cProtocolPriorityTable_Object((1,3,6,1,4,1,43,45,1,10,2,37,1,1,1))
if mibBuilder.loadTexts:h3cProtocolPriorityTable.setStatus(_A)
_H3cProtocolPriorityEntry_Object=MibTableRow
h3cProtocolPriorityEntry=_H3cProtocolPriorityEntry_Object((1,3,6,1,4,1,43,45,1,10,2,37,1,1,1,1))
h3cProtocolPriorityEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cProtocolPriorityEntry.setStatus(_A)
class _H3cPPriProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ospf',1),('telnet',2),('snmp',3),('icmp',4),('bgp',5),('ldp',6)))
_H3cPPriProtocolType_Type.__name__=_B
_H3cPPriProtocolType_Object=MibTableColumn
h3cPPriProtocolType=_H3cPPriProtocolType_Object((1,3,6,1,4,1,43,45,1,10,2,37,1,1,1,1,1),_H3cPPriProtocolType_Type())
h3cPPriProtocolType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cPPriProtocolType.setStatus(_A)
class _H3cPPriPriorityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipPrecedence',1),('dscp',2)))
_H3cPPriPriorityType_Type.__name__=_B
_H3cPPriPriorityType_Object=MibTableColumn
h3cPPriPriorityType=_H3cPPriPriorityType_Object((1,3,6,1,4,1,43,45,1,10,2,37,1,1,1,1,2),_H3cPPriPriorityType_Type())
h3cPPriPriorityType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPPriPriorityType.setStatus(_A)
class _H3cPPriPriorityVlaue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cPPriPriorityVlaue_Type.__name__=_B
_H3cPPriPriorityVlaue_Object=MibTableColumn
h3cPPriPriorityVlaue=_H3cPPriPriorityVlaue_Object((1,3,6,1,4,1,43,45,1,10,2,37,1,1,1,1,3),_H3cPPriPriorityVlaue_Type())
h3cPPriPriorityVlaue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPPriPriorityVlaue.setStatus(_A)
_H3cPPriRowStatus_Type=RowStatus
_H3cPPriRowStatus_Object=MibTableColumn
h3cPPriRowStatus=_H3cPPriRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,37,1,1,1,1,4),_H3cPPriRowStatus_Type())
h3cPPriRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPPriRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cProtocolPriority':h3cProtocolPriority,'h3cProtocolPriorityObjects':h3cProtocolPriorityObjects,'h3cPPri':h3cPPri,'h3cProtocolPriorityTable':h3cProtocolPriorityTable,'h3cProtocolPriorityEntry':h3cProtocolPriorityEntry,_E:h3cPPriProtocolType,'h3cPPriPriorityType':h3cPPriPriorityType,'h3cPPriPriorityVlaue':h3cPPriPriorityVlaue,'h3cPPriRowStatus':h3cPPriRowStatus})