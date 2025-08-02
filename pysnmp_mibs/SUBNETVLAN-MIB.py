_J='swSubnetVLANIPv6PrefixLength'
_I='swSubnetVLANIPv6Address'
_H='swSubnetVLANIPMask'
_G='swSubnetVLANIPAddress'
_F='swVlanPrecedencePortIndex'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='SUBNETVLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swSubnetVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,12,75))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwSubnetVlanCtrl_ObjectIdentity=ObjectIdentity
swSubnetVlanCtrl=_SwSubnetVlanCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,75,1))
_SwSubnetVlanInfo_ObjectIdentity=ObjectIdentity
swSubnetVlanInfo=_SwSubnetVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,12,75,2))
_SwSubnetVlanMgmt_ObjectIdentity=ObjectIdentity
swSubnetVlanMgmt=_SwSubnetVlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,75,3))
_SwVlanPrecedenceTable_Object=MibTable
swVlanPrecedenceTable=_SwVlanPrecedenceTable_Object((1,3,6,1,4,1,171,12,75,3,1))
if mibBuilder.loadTexts:swVlanPrecedenceTable.setStatus(_A)
_SwVlanPrecedenceEntry_Object=MibTableRow
swVlanPrecedenceEntry=_SwVlanPrecedenceEntry_Object((1,3,6,1,4,1,171,12,75,3,1,1))
swVlanPrecedenceEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:swVlanPrecedenceEntry.setStatus(_A)
class _SwVlanPrecedencePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwVlanPrecedencePortIndex_Type.__name__=_D
_SwVlanPrecedencePortIndex_Object=MibTableColumn
swVlanPrecedencePortIndex=_SwVlanPrecedencePortIndex_Object((1,3,6,1,4,1,171,12,75,3,1,1,1),_SwVlanPrecedencePortIndex_Type())
swVlanPrecedencePortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swVlanPrecedencePortIndex.setStatus(_A)
class _SwVlanPrecedenceClassification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('macBased',1),('subnetBased',2)))
_SwVlanPrecedenceClassification_Type.__name__=_D
_SwVlanPrecedenceClassification_Object=MibTableColumn
swVlanPrecedenceClassification=_SwVlanPrecedenceClassification_Object((1,3,6,1,4,1,171,12,75,3,1,1,2),_SwVlanPrecedenceClassification_Type())
swVlanPrecedenceClassification.setMaxAccess('read-write')
if mibBuilder.loadTexts:swVlanPrecedenceClassification.setStatus(_A)
_SwSubnetVLANTable_Object=MibTable
swSubnetVLANTable=_SwSubnetVLANTable_Object((1,3,6,1,4,1,171,12,75,3,2))
if mibBuilder.loadTexts:swSubnetVLANTable.setStatus(_A)
_SwSubnetVLANEntry_Object=MibTableRow
swSubnetVLANEntry=_SwSubnetVLANEntry_Object((1,3,6,1,4,1,171,12,75,3,2,1))
swSubnetVLANEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:swSubnetVLANEntry.setStatus(_A)
_SwSubnetVLANIPAddress_Type=IpAddress
_SwSubnetVLANIPAddress_Object=MibTableColumn
swSubnetVLANIPAddress=_SwSubnetVLANIPAddress_Object((1,3,6,1,4,1,171,12,75,3,2,1,1),_SwSubnetVLANIPAddress_Type())
swSubnetVLANIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubnetVLANIPAddress.setStatus(_A)
_SwSubnetVLANIPMask_Type=IpAddress
_SwSubnetVLANIPMask_Object=MibTableColumn
swSubnetVLANIPMask=_SwSubnetVLANIPMask_Object((1,3,6,1,4,1,171,12,75,3,2,1,2),_SwSubnetVLANIPMask_Type())
swSubnetVLANIPMask.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubnetVLANIPMask.setStatus(_A)
_SwSubnetVLANID_Type=VlanId
_SwSubnetVLANID_Object=MibTableColumn
swSubnetVLANID=_SwSubnetVLANID_Object((1,3,6,1,4,1,171,12,75,3,2,1,3),_SwSubnetVLANID_Type())
swSubnetVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:swSubnetVLANID.setStatus(_A)
class _SwSubnetVLANPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwSubnetVLANPriority_Type.__name__=_D
_SwSubnetVLANPriority_Object=MibTableColumn
swSubnetVLANPriority=_SwSubnetVLANPriority_Object((1,3,6,1,4,1,171,12,75,3,2,1,4),_SwSubnetVLANPriority_Type())
swSubnetVLANPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swSubnetVLANPriority.setStatus(_A)
_SwSubnetVLANRowStatus_Type=RowStatus
_SwSubnetVLANRowStatus_Object=MibTableColumn
swSubnetVLANRowStatus=_SwSubnetVLANRowStatus_Object((1,3,6,1,4,1,171,12,75,3,2,1,5),_SwSubnetVLANRowStatus_Type())
swSubnetVLANRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swSubnetVLANRowStatus.setStatus(_A)
_SwSubnetVLANIPv6Table_Object=MibTable
swSubnetVLANIPv6Table=_SwSubnetVLANIPv6Table_Object((1,3,6,1,4,1,171,12,75,3,3))
if mibBuilder.loadTexts:swSubnetVLANIPv6Table.setStatus(_A)
_SwSubnetVLANIPv6Entry_Object=MibTableRow
swSubnetVLANIPv6Entry=_SwSubnetVLANIPv6Entry_Object((1,3,6,1,4,1,171,12,75,3,3,1))
swSubnetVLANIPv6Entry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:swSubnetVLANIPv6Entry.setStatus(_A)
_SwSubnetVLANIPv6Address_Type=Ipv6Address
_SwSubnetVLANIPv6Address_Object=MibTableColumn
swSubnetVLANIPv6Address=_SwSubnetVLANIPv6Address_Object((1,3,6,1,4,1,171,12,75,3,3,1,1),_SwSubnetVLANIPv6Address_Type())
swSubnetVLANIPv6Address.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubnetVLANIPv6Address.setStatus(_A)
_SwSubnetVLANIPv6PrefixLength_Type=Integer32
_SwSubnetVLANIPv6PrefixLength_Object=MibTableColumn
swSubnetVLANIPv6PrefixLength=_SwSubnetVLANIPv6PrefixLength_Object((1,3,6,1,4,1,171,12,75,3,3,1,2),_SwSubnetVLANIPv6PrefixLength_Type())
swSubnetVLANIPv6PrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubnetVLANIPv6PrefixLength.setStatus(_A)
_SwSubnetVLANIPv6VID_Type=VlanId
_SwSubnetVLANIPv6VID_Object=MibTableColumn
swSubnetVLANIPv6VID=_SwSubnetVLANIPv6VID_Object((1,3,6,1,4,1,171,12,75,3,3,1,3),_SwSubnetVLANIPv6VID_Type())
swSubnetVLANIPv6VID.setMaxAccess(_C)
if mibBuilder.loadTexts:swSubnetVLANIPv6VID.setStatus(_A)
class _SwSubnetVLANIPv6Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwSubnetVLANIPv6Priority_Type.__name__=_D
_SwSubnetVLANIPv6Priority_Object=MibTableColumn
swSubnetVLANIPv6Priority=_SwSubnetVLANIPv6Priority_Object((1,3,6,1,4,1,171,12,75,3,3,1,4),_SwSubnetVLANIPv6Priority_Type())
swSubnetVLANIPv6Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:swSubnetVLANIPv6Priority.setStatus(_A)
_SwSubnetVLANIPv6RowStatus_Type=RowStatus
_SwSubnetVLANIPv6RowStatus_Object=MibTableColumn
swSubnetVLANIPv6RowStatus=_SwSubnetVLANIPv6RowStatus_Object((1,3,6,1,4,1,171,12,75,3,3,1,5),_SwSubnetVLANIPv6RowStatus_Type())
swSubnetVLANIPv6RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swSubnetVLANIPv6RowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanId':VlanId,'Ipv6Address':Ipv6Address,'swSubnetVlanMIB':swSubnetVlanMIB,'swSubnetVlanCtrl':swSubnetVlanCtrl,'swSubnetVlanInfo':swSubnetVlanInfo,'swSubnetVlanMgmt':swSubnetVlanMgmt,'swVlanPrecedenceTable':swVlanPrecedenceTable,'swVlanPrecedenceEntry':swVlanPrecedenceEntry,_F:swVlanPrecedencePortIndex,'swVlanPrecedenceClassification':swVlanPrecedenceClassification,'swSubnetVLANTable':swSubnetVLANTable,'swSubnetVLANEntry':swSubnetVLANEntry,_G:swSubnetVLANIPAddress,_H:swSubnetVLANIPMask,'swSubnetVLANID':swSubnetVLANID,'swSubnetVLANPriority':swSubnetVLANPriority,'swSubnetVLANRowStatus':swSubnetVLANRowStatus,'swSubnetVLANIPv6Table':swSubnetVLANIPv6Table,'swSubnetVLANIPv6Entry':swSubnetVLANIPv6Entry,_I:swSubnetVLANIPv6Address,_J:swSubnetVLANIPv6PrefixLength,'swSubnetVLANIPv6VID':swSubnetVLANIPv6VID,'swSubnetVLANIPv6Priority':swSubnetVLANIPv6Priority,'swSubnetVLANIPv6RowStatus':swSubnetVLANIPv6RowStatus})