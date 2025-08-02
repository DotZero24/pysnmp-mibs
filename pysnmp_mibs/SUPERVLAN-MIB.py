_M='swSubVlanIPAddressRangeTo'
_L='swSubVlanIPAddressRangeFrom'
_K='inactive'
_J='active'
_I='swSuperVlanId'
_H='swSubVlanId'
_G='Integer32'
_F='read-only'
_E='not-accessible'
_D='SUPERVLAN-MIB'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swSuperVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,12,91))
_SwSuperVlanMIBObjects_ObjectIdentity=ObjectIdentity
swSuperVlanMIBObjects=_SwSuperVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,91,1))
_SwSuperVlanTable_Object=MibTable
swSuperVlanTable=_SwSuperVlanTable_Object((1,3,6,1,4,1,171,12,91,1,1))
if mibBuilder.loadTexts:swSuperVlanTable.setStatus(_A)
_SwSuperVlanEntry_Object=MibTableRow
swSuperVlanEntry=_SwSuperVlanEntry_Object((1,3,6,1,4,1,171,12,91,1,1,1))
swSuperVlanEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:swSuperVlanEntry.setStatus(_A)
_SwSuperVlanId_Type=VlanIndex
_SwSuperVlanId_Object=MibTableColumn
swSuperVlanId=_SwSuperVlanId_Object((1,3,6,1,4,1,171,12,91,1,1,1,1),_SwSuperVlanId_Type())
swSuperVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:swSuperVlanId.setStatus(_A)
_SwSuperVlanIPAddress_Type=IpAddress
_SwSuperVlanIPAddress_Object=MibTableColumn
swSuperVlanIPAddress=_SwSuperVlanIPAddress_Object((1,3,6,1,4,1,171,12,91,1,1,1,2),_SwSuperVlanIPAddress_Type())
swSuperVlanIPAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:swSuperVlanIPAddress.setStatus(_A)
_SwSuperVlanIPAddrMask_Type=IpAddress
_SwSuperVlanIPAddrMask_Object=MibTableColumn
swSuperVlanIPAddrMask=_SwSuperVlanIPAddrMask_Object((1,3,6,1,4,1,171,12,91,1,1,1,3),_SwSuperVlanIPAddrMask_Type())
swSuperVlanIPAddrMask.setMaxAccess(_F)
if mibBuilder.loadTexts:swSuperVlanIPAddrMask.setStatus(_A)
class _SwSubVlanList1to64_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList1to64_Type.__name__=_C
_SwSubVlanList1to64_Object=MibTableColumn
swSubVlanList1to64=_SwSubVlanList1to64_Object((1,3,6,1,4,1,171,12,91,1,1,1,4),_SwSubVlanList1to64_Type())
swSubVlanList1to64.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList1to64.setStatus(_A)
class _SwSubVlanList65to128_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList65to128_Type.__name__=_C
_SwSubVlanList65to128_Object=MibTableColumn
swSubVlanList65to128=_SwSubVlanList65to128_Object((1,3,6,1,4,1,171,12,91,1,1,1,5),_SwSubVlanList65to128_Type())
swSubVlanList65to128.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList65to128.setStatus(_A)
class _SwSubVlanList129to192_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList129to192_Type.__name__=_C
_SwSubVlanList129to192_Object=MibTableColumn
swSubVlanList129to192=_SwSubVlanList129to192_Object((1,3,6,1,4,1,171,12,91,1,1,1,6),_SwSubVlanList129to192_Type())
swSubVlanList129to192.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList129to192.setStatus(_A)
class _SwSubVlanList193to256_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList193to256_Type.__name__=_C
_SwSubVlanList193to256_Object=MibTableColumn
swSubVlanList193to256=_SwSubVlanList193to256_Object((1,3,6,1,4,1,171,12,91,1,1,1,7),_SwSubVlanList193to256_Type())
swSubVlanList193to256.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList193to256.setStatus(_A)
class _SwSubVlanList257to320_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList257to320_Type.__name__=_C
_SwSubVlanList257to320_Object=MibTableColumn
swSubVlanList257to320=_SwSubVlanList257to320_Object((1,3,6,1,4,1,171,12,91,1,1,1,8),_SwSubVlanList257to320_Type())
swSubVlanList257to320.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList257to320.setStatus(_A)
class _SwSubVlanList321to384_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList321to384_Type.__name__=_C
_SwSubVlanList321to384_Object=MibTableColumn
swSubVlanList321to384=_SwSubVlanList321to384_Object((1,3,6,1,4,1,171,12,91,1,1,1,9),_SwSubVlanList321to384_Type())
swSubVlanList321to384.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList321to384.setStatus(_A)
class _SwSubVlanList385to448_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList385to448_Type.__name__=_C
_SwSubVlanList385to448_Object=MibTableColumn
swSubVlanList385to448=_SwSubVlanList385to448_Object((1,3,6,1,4,1,171,12,91,1,1,1,10),_SwSubVlanList385to448_Type())
swSubVlanList385to448.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList385to448.setStatus(_A)
class _SwSubVlanList449to512_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwSubVlanList449to512_Type.__name__=_C
_SwSubVlanList449to512_Object=MibTableColumn
swSubVlanList449to512=_SwSubVlanList449to512_Object((1,3,6,1,4,1,171,12,91,1,1,1,11),_SwSubVlanList449to512_Type())
swSubVlanList449to512.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanList449to512.setStatus(_A)
class _SwSuperVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwSuperVlanStatus_Type.__name__=_G
_SwSuperVlanStatus_Object=MibTableColumn
swSuperVlanStatus=_SwSuperVlanStatus_Object((1,3,6,1,4,1,171,12,91,1,1,1,12),_SwSuperVlanStatus_Type())
swSuperVlanStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:swSuperVlanStatus.setStatus(_A)
_SwSuperVlanRowStatus_Type=RowStatus
_SwSuperVlanRowStatus_Object=MibTableColumn
swSuperVlanRowStatus=_SwSuperVlanRowStatus_Object((1,3,6,1,4,1,171,12,91,1,1,1,100),_SwSuperVlanRowStatus_Type())
swSuperVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swSuperVlanRowStatus.setStatus(_A)
_SwSubVlanTable_Object=MibTable
swSubVlanTable=_SwSubVlanTable_Object((1,3,6,1,4,1,171,12,91,1,2))
if mibBuilder.loadTexts:swSubVlanTable.setStatus(_A)
_SwSubVlanEntry_Object=MibTableRow
swSubVlanEntry=_SwSubVlanEntry_Object((1,3,6,1,4,1,171,12,91,1,2,1))
swSubVlanEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:swSubVlanEntry.setStatus(_A)
_SwSubVlanId_Type=VlanIndex
_SwSubVlanId_Object=MibTableColumn
swSubVlanId=_SwSubVlanId_Object((1,3,6,1,4,1,171,12,91,1,2,1,1),_SwSubVlanId_Type())
swSubVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubVlanId.setStatus(_A)
class _SwSubVlanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwSubVlanOperStatus_Type.__name__=_G
_SwSubVlanOperStatus_Object=MibTableColumn
swSubVlanOperStatus=_SwSubVlanOperStatus_Object((1,3,6,1,4,1,171,12,91,1,2,1,2),_SwSubVlanOperStatus_Type())
swSubVlanOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:swSubVlanOperStatus.setStatus(_A)
_SwSubVlanIPRangeTable_Object=MibTable
swSubVlanIPRangeTable=_SwSubVlanIPRangeTable_Object((1,3,6,1,4,1,171,12,91,1,3))
if mibBuilder.loadTexts:swSubVlanIPRangeTable.setStatus(_A)
_SwSubVlanIPRangeEntry_Object=MibTableRow
swSubVlanIPRangeEntry=_SwSubVlanIPRangeEntry_Object((1,3,6,1,4,1,171,12,91,1,3,1))
swSubVlanIPRangeEntry.setIndexNames((0,_D,_H),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swSubVlanIPRangeEntry.setStatus(_A)
_SwSubVlanIPAddressRangeFrom_Type=IpAddress
_SwSubVlanIPAddressRangeFrom_Object=MibTableColumn
swSubVlanIPAddressRangeFrom=_SwSubVlanIPAddressRangeFrom_Object((1,3,6,1,4,1,171,12,91,1,3,1,1),_SwSubVlanIPAddressRangeFrom_Type())
swSubVlanIPAddressRangeFrom.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubVlanIPAddressRangeFrom.setStatus(_A)
_SwSubVlanIPAddressRangeTo_Type=IpAddress
_SwSubVlanIPAddressRangeTo_Object=MibTableColumn
swSubVlanIPAddressRangeTo=_SwSubVlanIPAddressRangeTo_Object((1,3,6,1,4,1,171,12,91,1,3,1,2),_SwSubVlanIPAddressRangeTo_Type())
swSubVlanIPAddressRangeTo.setMaxAccess(_E)
if mibBuilder.loadTexts:swSubVlanIPAddressRangeTo.setStatus(_A)
_SwSubVlanRowStatus_Type=RowStatus
_SwSubVlanRowStatus_Object=MibTableColumn
swSubVlanRowStatus=_SwSubVlanRowStatus_Object((1,3,6,1,4,1,171,12,91,1,3,1,100),_SwSubVlanRowStatus_Type())
swSubVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swSubVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swSuperVlanMIB':swSuperVlanMIB,'swSuperVlanMIBObjects':swSuperVlanMIBObjects,'swSuperVlanTable':swSuperVlanTable,'swSuperVlanEntry':swSuperVlanEntry,_I:swSuperVlanId,'swSuperVlanIPAddress':swSuperVlanIPAddress,'swSuperVlanIPAddrMask':swSuperVlanIPAddrMask,'swSubVlanList1to64':swSubVlanList1to64,'swSubVlanList65to128':swSubVlanList65to128,'swSubVlanList129to192':swSubVlanList129to192,'swSubVlanList193to256':swSubVlanList193to256,'swSubVlanList257to320':swSubVlanList257to320,'swSubVlanList321to384':swSubVlanList321to384,'swSubVlanList385to448':swSubVlanList385to448,'swSubVlanList449to512':swSubVlanList449to512,'swSuperVlanStatus':swSuperVlanStatus,'swSuperVlanRowStatus':swSuperVlanRowStatus,'swSubVlanTable':swSubVlanTable,'swSubVlanEntry':swSubVlanEntry,_H:swSubVlanId,'swSubVlanOperStatus':swSubVlanOperStatus,'swSubVlanIPRangeTable':swSubVlanIPRangeTable,'swSubVlanIPRangeEntry':swSubVlanIPRangeEntry,_L:swSubVlanIPAddressRangeFrom,_M:swSubVlanIPAddressRangeTo,'swSubVlanRowStatus':swSubVlanRowStatus})