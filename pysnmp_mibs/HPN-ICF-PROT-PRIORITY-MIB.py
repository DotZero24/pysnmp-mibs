_E='hpnicfPPriProtocolType'
_D='HPN-ICF-PROT-PRIORITY-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfProtocolPriority=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,37))
if mibBuilder.loadTexts:hpnicfProtocolPriority.setRevisions(('2005-01-17 16:33',))
_HpnicfProtocolPriorityObjects_ObjectIdentity=ObjectIdentity
hpnicfProtocolPriorityObjects=_HpnicfProtocolPriorityObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,37,1))
_HpnicfPPri_ObjectIdentity=ObjectIdentity
hpnicfPPri=_HpnicfPPri_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1))
_HpnicfProtocolPriorityTable_Object=MibTable
hpnicfProtocolPriorityTable=_HpnicfProtocolPriorityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1,1))
if mibBuilder.loadTexts:hpnicfProtocolPriorityTable.setStatus(_A)
_HpnicfProtocolPriorityEntry_Object=MibTableRow
hpnicfProtocolPriorityEntry=_HpnicfProtocolPriorityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1,1,1))
hpnicfProtocolPriorityEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfProtocolPriorityEntry.setStatus(_A)
class _HpnicfPPriProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ospf',1),('telnet',2),('snmp',3),('icmp',4),('bgp',5),('ldp',6)))
_HpnicfPPriProtocolType_Type.__name__=_B
_HpnicfPPriProtocolType_Object=MibTableColumn
hpnicfPPriProtocolType=_HpnicfPPriProtocolType_Object((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1,1,1,1),_HpnicfPPriProtocolType_Type())
hpnicfPPriProtocolType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfPPriProtocolType.setStatus(_A)
class _HpnicfPPriPriorityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipPrecedence',1),('dscp',2)))
_HpnicfPPriPriorityType_Type.__name__=_B
_HpnicfPPriPriorityType_Object=MibTableColumn
hpnicfPPriPriorityType=_HpnicfPPriPriorityType_Object((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1,1,1,2),_HpnicfPPriPriorityType_Type())
hpnicfPPriPriorityType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPPriPriorityType.setStatus(_A)
class _HpnicfPPriPriorityVlaue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfPPriPriorityVlaue_Type.__name__=_B
_HpnicfPPriPriorityVlaue_Object=MibTableColumn
hpnicfPPriPriorityVlaue=_HpnicfPPriPriorityVlaue_Object((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1,1,1,3),_HpnicfPPriPriorityVlaue_Type())
hpnicfPPriPriorityVlaue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPPriPriorityVlaue.setStatus(_A)
_HpnicfPPriRowStatus_Type=RowStatus
_HpnicfPPriRowStatus_Object=MibTableColumn
hpnicfPPriRowStatus=_HpnicfPPriRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,37,1,1,1,1,4),_HpnicfPPriRowStatus_Type())
hpnicfPPriRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPPriRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfProtocolPriority':hpnicfProtocolPriority,'hpnicfProtocolPriorityObjects':hpnicfProtocolPriorityObjects,'hpnicfPPri':hpnicfPPri,'hpnicfProtocolPriorityTable':hpnicfProtocolPriorityTable,'hpnicfProtocolPriorityEntry':hpnicfProtocolPriorityEntry,_E:hpnicfPPriProtocolType,'hpnicfPPriPriorityType':hpnicfPPriPriorityType,'hpnicfPPriPriorityVlaue':hpnicfPPriPriorityVlaue,'hpnicfPPriRowStatus':hpnicfPPriRowStatus})