_I='read-create'
_H='hpnicfVrrpExtTrackInterface'
_G='HPN-ICF-VRRP-EXT-MIB'
_F='vrrpOperVrId'
_E='VRRP-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
vrrpOperVrId,=mibBuilder.importSymbols(_E,_F)
hpnicfVrrpExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,24))
_HpnicfVrrpExtMibObject_ObjectIdentity=ObjectIdentity
hpnicfVrrpExtMibObject=_HpnicfVrrpExtMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,24,1))
_HpnicfVrrpExtTable_Object=MibTable
hpnicfVrrpExtTable=_HpnicfVrrpExtTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,24,1,1))
if mibBuilder.loadTexts:hpnicfVrrpExtTable.setStatus(_A)
_HpnicfVrrpExtEntry_Object=MibTableRow
hpnicfVrrpExtEntry=_HpnicfVrrpExtEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,24,1,1,1))
hpnicfVrrpExtEntry.setIndexNames((0,_C,_D),(0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfVrrpExtEntry.setStatus(_A)
class _HpnicfVrrpExtTrackInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfVrrpExtTrackInterface_Type.__name__=_B
_HpnicfVrrpExtTrackInterface_Object=MibTableColumn
hpnicfVrrpExtTrackInterface=_HpnicfVrrpExtTrackInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,24,1,1,1,1),_HpnicfVrrpExtTrackInterface_Type())
hpnicfVrrpExtTrackInterface.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfVrrpExtTrackInterface.setStatus(_A)
class _HpnicfVrrpExtPriorityReduce_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfVrrpExtPriorityReduce_Type.__name__=_B
_HpnicfVrrpExtPriorityReduce_Object=MibTableColumn
hpnicfVrrpExtPriorityReduce=_HpnicfVrrpExtPriorityReduce_Object((1,3,6,1,4,1,11,2,14,11,15,2,24,1,1,1,2),_HpnicfVrrpExtPriorityReduce_Type())
hpnicfVrrpExtPriorityReduce.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfVrrpExtPriorityReduce.setStatus(_A)
_HpnicfVrrpExtRowStatus_Type=RowStatus
_HpnicfVrrpExtRowStatus_Object=MibTableColumn
hpnicfVrrpExtRowStatus=_HpnicfVrrpExtRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,24,1,1,1,3),_HpnicfVrrpExtRowStatus_Type())
hpnicfVrrpExtRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfVrrpExtRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hpnicfVrrpExt':hpnicfVrrpExt,'hpnicfVrrpExtMibObject':hpnicfVrrpExtMibObject,'hpnicfVrrpExtTable':hpnicfVrrpExtTable,'hpnicfVrrpExtEntry':hpnicfVrrpExtEntry,_H:hpnicfVrrpExtTrackInterface,'hpnicfVrrpExtPriorityReduce':hpnicfVrrpExtPriorityReduce,'hpnicfVrrpExtRowStatus':hpnicfVrrpExtRowStatus})