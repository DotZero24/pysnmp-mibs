_I='read-create'
_H='h3cVrrpExtTrackInterface'
_G='H3C-VRRP-EXT-MIB'
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
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
vrrpOperVrId,=mibBuilder.importSymbols(_E,_F)
h3cVrrpExt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,24))
_H3cVrrpExtMibObject_ObjectIdentity=ObjectIdentity
h3cVrrpExtMibObject=_H3cVrrpExtMibObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,24,1))
_H3cVrrpExtTable_Object=MibTable
h3cVrrpExtTable=_H3cVrrpExtTable_Object((1,3,6,1,4,1,2011,10,2,24,1,1))
if mibBuilder.loadTexts:h3cVrrpExtTable.setStatus(_A)
_H3cVrrpExtEntry_Object=MibTableRow
h3cVrrpExtEntry=_H3cVrrpExtEntry_Object((1,3,6,1,4,1,2011,10,2,24,1,1,1))
h3cVrrpExtEntry.setIndexNames((0,_C,_D),(0,_E,_F),(0,_G,_H))
if mibBuilder.loadTexts:h3cVrrpExtEntry.setStatus(_A)
class _H3cVrrpExtTrackInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cVrrpExtTrackInterface_Type.__name__=_B
_H3cVrrpExtTrackInterface_Object=MibTableColumn
h3cVrrpExtTrackInterface=_H3cVrrpExtTrackInterface_Object((1,3,6,1,4,1,2011,10,2,24,1,1,1,1),_H3cVrrpExtTrackInterface_Type())
h3cVrrpExtTrackInterface.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cVrrpExtTrackInterface.setStatus(_A)
class _H3cVrrpExtPriorityReduce_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cVrrpExtPriorityReduce_Type.__name__=_B
_H3cVrrpExtPriorityReduce_Object=MibTableColumn
h3cVrrpExtPriorityReduce=_H3cVrrpExtPriorityReduce_Object((1,3,6,1,4,1,2011,10,2,24,1,1,1,2),_H3cVrrpExtPriorityReduce_Type())
h3cVrrpExtPriorityReduce.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cVrrpExtPriorityReduce.setStatus(_A)
_H3cVrrpExtRowStatus_Type=RowStatus
_H3cVrrpExtRowStatus_Object=MibTableColumn
h3cVrrpExtRowStatus=_H3cVrrpExtRowStatus_Object((1,3,6,1,4,1,2011,10,2,24,1,1,1,3),_H3cVrrpExtRowStatus_Type())
h3cVrrpExtRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cVrrpExtRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'h3cVrrpExt':h3cVrrpExt,'h3cVrrpExtMibObject':h3cVrrpExtMibObject,'h3cVrrpExtTable':h3cVrrpExtTable,'h3cVrrpExtEntry':h3cVrrpExtEntry,_H:h3cVrrpExtTrackInterface,'h3cVrrpExtPriorityReduce':h3cVrrpExtPriorityReduce,'h3cVrrpExtRowStatus':h3cVrrpExtRowStatus})