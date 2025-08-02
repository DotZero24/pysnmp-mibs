_M='rcIpIfIndex'
_L='rcIpBaseManVlanIfIndex'
_K='rcVlanId'
_J='IpAddressCatagory'
_I='rcIpBaseAddress'
_H='rcIpBaseAddresstType'
_G='rcIpBaseAddressIfIndex'
_F='read-write'
_E='not-accessible'
_D='read-create'
_C='RAISECOM-IP-BASE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rcIpBaseMIB=ModuleIdentity((1,3,6,1,4,1,8886,6,1,16,4))
class IpAddressCatagory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('sub',2),('linklocal',3)))
_RcL3_ObjectIdentity=ObjectIdentity
rcL3=_RcL3_ObjectIdentity((1,3,6,1,4,1,8886,6,1,16))
_RcIpBaseMibObjects_ObjectIdentity=ObjectIdentity
rcIpBaseMibObjects=_RcIpBaseMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,16,4,1))
_RcIpBaseScalarGroup_ObjectIdentity=ObjectIdentity
rcIpBaseScalarGroup=_RcIpBaseScalarGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,16,4,1,1))
_RcIpBaseTableGroup_ObjectIdentity=ObjectIdentity
rcIpBaseTableGroup=_RcIpBaseTableGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,16,4,1,2))
_RcIpBaseAddressTable_Object=MibTable
rcIpBaseAddressTable=_RcIpBaseAddressTable_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1))
if mibBuilder.loadTexts:rcIpBaseAddressTable.setStatus(_A)
_RcIpBaseAddressEntry_Object=MibTableRow
rcIpBaseAddressEntry=_RcIpBaseAddressEntry_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1))
rcIpBaseAddressEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:rcIpBaseAddressEntry.setStatus(_A)
_RcIpBaseAddressIfIndex_Type=Integer32
_RcIpBaseAddressIfIndex_Object=MibTableColumn
rcIpBaseAddressIfIndex=_RcIpBaseAddressIfIndex_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,1),_RcIpBaseAddressIfIndex_Type())
rcIpBaseAddressIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpBaseAddressIfIndex.setStatus(_A)
_RcIpBaseAddresstType_Type=InetAddressType
_RcIpBaseAddresstType_Object=MibTableColumn
rcIpBaseAddresstType=_RcIpBaseAddresstType_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,2),_RcIpBaseAddresstType_Type())
rcIpBaseAddresstType.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpBaseAddresstType.setStatus(_A)
_RcIpBaseAddress_Type=InetAddress
_RcIpBaseAddress_Object=MibTableColumn
rcIpBaseAddress=_RcIpBaseAddress_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,3),_RcIpBaseAddress_Type())
rcIpBaseAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpBaseAddress.setStatus(_A)
_RcIpBaseAddressPrefixLength_Type=InetAddressPrefixLength
_RcIpBaseAddressPrefixLength_Object=MibTableColumn
rcIpBaseAddressPrefixLength=_RcIpBaseAddressPrefixLength_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,4),_RcIpBaseAddressPrefixLength_Type())
rcIpBaseAddressPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpBaseAddressPrefixLength.setStatus(_A)
class _RcIpBaseAddressSourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('assignedIp',1),('cluster',2),('dhcp',3),('bootp',4),('negotiate',5),('unnumbered',6)))
_RcIpBaseAddressSourceType_Type.__name__=_B
_RcIpBaseAddressSourceType_Object=MibTableColumn
rcIpBaseAddressSourceType=_RcIpBaseAddressSourceType_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,5),_RcIpBaseAddressSourceType_Type())
rcIpBaseAddressSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpBaseAddressSourceType.setStatus(_A)
class _RcIpBaseAddressCatagory_Type(IpAddressCatagory):defaultValue=1
_RcIpBaseAddressCatagory_Type.__name__=_J
_RcIpBaseAddressCatagory_Object=MibTableColumn
rcIpBaseAddressCatagory=_RcIpBaseAddressCatagory_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,6),_RcIpBaseAddressCatagory_Type())
rcIpBaseAddressCatagory.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpBaseAddressCatagory.setStatus(_A)
_RcIpBaseAddressRowStatus_Type=RowStatus
_RcIpBaseAddressRowStatus_Object=MibTableColumn
rcIpBaseAddressRowStatus=_RcIpBaseAddressRowStatus_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,1,1,7),_RcIpBaseAddressRowStatus_Type())
rcIpBaseAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpBaseAddressRowStatus.setStatus(_A)
_RcVlanInterfaceIndexTable_Object=MibTable
rcVlanInterfaceIndexTable=_RcVlanInterfaceIndexTable_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,2))
if mibBuilder.loadTexts:rcVlanInterfaceIndexTable.setStatus(_A)
_RcVlanInterfaceIndexEntry_Object=MibTableRow
rcVlanInterfaceIndexEntry=_RcVlanInterfaceIndexEntry_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,2,1))
rcVlanInterfaceIndexEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:rcVlanInterfaceIndexEntry.setStatus(_A)
_RcVlanId_Type=Integer32
_RcVlanId_Object=MibTableColumn
rcVlanId=_RcVlanId_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,2,1,1),_RcVlanId_Type())
rcVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanId.setStatus(_A)
_RcVlanIfIndex_Type=Integer32
_RcVlanIfIndex_Object=MibTableColumn
rcVlanIfIndex=_RcVlanIfIndex_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,2,1,2),_RcVlanIfIndex_Type())
rcVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanIfIndex.setStatus(_A)
_RcVlanIfIndexRowStatus_Type=RowStatus
_RcVlanIfIndexRowStatus_Object=MibTableColumn
rcVlanIfIndexRowStatus=_RcVlanIfIndexRowStatus_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,2,1,3),_RcVlanIfIndexRowStatus_Type())
rcVlanIfIndexRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanIfIndexRowStatus.setStatus(_A)
_RcIpBaseManVlanTable_Object=MibTable
rcIpBaseManVlanTable=_RcIpBaseManVlanTable_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3))
if mibBuilder.loadTexts:rcIpBaseManVlanTable.setStatus(_A)
_RcIpBaseManVlanEntry_Object=MibTableRow
rcIpBaseManVlanEntry=_RcIpBaseManVlanEntry_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1))
rcIpBaseManVlanEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:rcIpBaseManVlanEntry.setStatus(_A)
_RcIpBaseManVlanIfIndex_Type=Integer32
_RcIpBaseManVlanIfIndex_Object=MibTableColumn
rcIpBaseManVlanIfIndex=_RcIpBaseManVlanIfIndex_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,1),_RcIpBaseManVlanIfIndex_Type())
rcIpBaseManVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpBaseManVlanIfIndex.setStatus(_A)
class _RcIpBaseManVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single-taging',1),('double-taging',2)))
_RcIpBaseManVlanMode_Type.__name__=_B
_RcIpBaseManVlanMode_Object=MibTableColumn
rcIpBaseManVlanMode=_RcIpBaseManVlanMode_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,2),_RcIpBaseManVlanMode_Type())
rcIpBaseManVlanMode.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpBaseManVlanMode.setStatus(_A)
class _RcIpBaseInnerVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcIpBaseInnerVlan_Type.__name__=_B
_RcIpBaseInnerVlan_Object=MibTableColumn
rcIpBaseInnerVlan=_RcIpBaseInnerVlan_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,3),_RcIpBaseInnerVlan_Type())
rcIpBaseInnerVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpBaseInnerVlan.setStatus(_A)
class _RcIpBaseCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcIpBaseCos_Type.__name__=_B
_RcIpBaseCos_Object=MibTableColumn
rcIpBaseCos=_RcIpBaseCos_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,4),_RcIpBaseCos_Type())
rcIpBaseCos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpBaseCos.setStatus(_A)
class _RcIpBaseInnerCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcIpBaseInnerCos_Type.__name__=_B
_RcIpBaseInnerCos_Object=MibTableColumn
rcIpBaseInnerCos=_RcIpBaseInnerCos_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,5),_RcIpBaseInnerCos_Type())
rcIpBaseInnerCos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpBaseInnerCos.setStatus(_A)
class _RcIpBaseTpid_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcIpBaseTpid_Type.__name__=_B
_RcIpBaseTpid_Object=MibTableColumn
rcIpBaseTpid=_RcIpBaseTpid_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,6),_RcIpBaseTpid_Type())
rcIpBaseTpid.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpBaseTpid.setStatus(_A)
class _RcIpBaseInnerTpid_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcIpBaseInnerTpid_Type.__name__=_B
_RcIpBaseInnerTpid_Object=MibTableColumn
rcIpBaseInnerTpid=_RcIpBaseInnerTpid_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,3,1,7),_RcIpBaseInnerTpid_Type())
rcIpBaseInnerTpid.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpBaseInnerTpid.setStatus(_A)
_RcIpIfMtuTable_Object=MibTable
rcIpIfMtuTable=_RcIpIfMtuTable_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,4))
if mibBuilder.loadTexts:rcIpIfMtuTable.setStatus(_A)
_RcIpIfMtuEntry_Object=MibTableRow
rcIpIfMtuEntry=_RcIpIfMtuEntry_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,4,1))
rcIpIfMtuEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:rcIpIfMtuEntry.setStatus(_A)
_RcIpIfIndex_Type=Integer32
_RcIpIfIndex_Object=MibTableColumn
rcIpIfIndex=_RcIpIfIndex_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,4,1,1),_RcIpIfIndex_Type())
rcIpIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcIpIfIndex.setStatus(_A)
class _RcIpIfMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,9216))
_RcIpIfMtu_Type.__name__=_B
_RcIpIfMtu_Object=MibTableColumn
rcIpIfMtu=_RcIpIfMtu_Object((1,3,6,1,4,1,8886,6,1,16,4,1,2,4,1,2),_RcIpIfMtu_Type())
rcIpIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIpIfMtu.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_J:IpAddressCatagory,'rcL3':rcL3,'rcIpBaseMIB':rcIpBaseMIB,'rcIpBaseMibObjects':rcIpBaseMibObjects,'rcIpBaseScalarGroup':rcIpBaseScalarGroup,'rcIpBaseTableGroup':rcIpBaseTableGroup,'rcIpBaseAddressTable':rcIpBaseAddressTable,'rcIpBaseAddressEntry':rcIpBaseAddressEntry,_G:rcIpBaseAddressIfIndex,_H:rcIpBaseAddresstType,_I:rcIpBaseAddress,'rcIpBaseAddressPrefixLength':rcIpBaseAddressPrefixLength,'rcIpBaseAddressSourceType':rcIpBaseAddressSourceType,'rcIpBaseAddressCatagory':rcIpBaseAddressCatagory,'rcIpBaseAddressRowStatus':rcIpBaseAddressRowStatus,'rcVlanInterfaceIndexTable':rcVlanInterfaceIndexTable,'rcVlanInterfaceIndexEntry':rcVlanInterfaceIndexEntry,_K:rcVlanId,'rcVlanIfIndex':rcVlanIfIndex,'rcVlanIfIndexRowStatus':rcVlanIfIndexRowStatus,'rcIpBaseManVlanTable':rcIpBaseManVlanTable,'rcIpBaseManVlanEntry':rcIpBaseManVlanEntry,_L:rcIpBaseManVlanIfIndex,'rcIpBaseManVlanMode':rcIpBaseManVlanMode,'rcIpBaseInnerVlan':rcIpBaseInnerVlan,'rcIpBaseCos':rcIpBaseCos,'rcIpBaseInnerCos':rcIpBaseInnerCos,'rcIpBaseTpid':rcIpBaseTpid,'rcIpBaseInnerTpid':rcIpBaseInnerTpid,'rcIpIfMtuTable':rcIpIfMtuTable,'rcIpIfMtuEntry':rcIpIfMtuEntry,_M:rcIpIfIndex,'rcIpIfMtu':rcIpIfMtu})