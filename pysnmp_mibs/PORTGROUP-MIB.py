_E='swPortGroupID'
_D='PORTGROUP-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
swPortGroupMIB=ModuleIdentity((1,3,6,1,4,1,171,12,88))
_SwPortGroupMIBObjects_ObjectIdentity=ObjectIdentity
swPortGroupMIBObjects=_SwPortGroupMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,88,1))
_SwPortGroupTable_Object=MibTable
swPortGroupTable=_SwPortGroupTable_Object((1,3,6,1,4,1,171,12,88,1,1))
if mibBuilder.loadTexts:swPortGroupTable.setStatus(_A)
_SwPortGroupEntry_Object=MibTableRow
swPortGroupEntry=_SwPortGroupEntry_Object((1,3,6,1,4,1,171,12,88,1,1,1))
swPortGroupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swPortGroupEntry.setStatus(_A)
_SwPortGroupID_Type=Integer32
_SwPortGroupID_Object=MibTableColumn
swPortGroupID=_SwPortGroupID_Object((1,3,6,1,4,1,171,12,88,1,1,1,1),_SwPortGroupID_Type())
swPortGroupID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swPortGroupID.setStatus(_A)
_SwPortGroupRowStatus_Type=RowStatus
_SwPortGroupRowStatus_Object=MibTableColumn
swPortGroupRowStatus=_SwPortGroupRowStatus_Object((1,3,6,1,4,1,171,12,88,1,1,1,2),_SwPortGroupRowStatus_Type())
swPortGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortGroupRowStatus.setStatus(_A)
class _SwPortGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwPortGroupName_Type.__name__=_C
_SwPortGroupName_Object=MibTableColumn
swPortGroupName=_SwPortGroupName_Object((1,3,6,1,4,1,171,12,88,1,1,1,3),_SwPortGroupName_Type())
swPortGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortGroupName.setStatus(_A)
_SwPortGroupPorts_Type=PortList
_SwPortGroupPorts_Object=MibTableColumn
swPortGroupPorts=_SwPortGroupPorts_Object((1,3,6,1,4,1,171,12,88,1,1,1,4),_SwPortGroupPorts_Type())
swPortGroupPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swPortGroupPorts.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swPortGroupMIB':swPortGroupMIB,'swPortGroupMIBObjects':swPortGroupMIBObjects,'swPortGroupTable':swPortGroupTable,'swPortGroupEntry':swPortGroupEntry,_E:swPortGroupID,'swPortGroupRowStatus':swPortGroupRowStatus,'swPortGroupName':swPortGroupName,'swPortGroupPorts':swPortGroupPorts})