_F='swSrcIpIfType'
_E='SRC-IPIF-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
swSrcIpIfMIB=ModuleIdentity((1,3,6,1,4,1,171,12,81))
_SwSrcIpIfCtrl_ObjectIdentity=ObjectIdentity
swSrcIpIfCtrl=_SwSrcIpIfCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,81,1))
_SwSrcIpIfInfo_ObjectIdentity=ObjectIdentity
swSrcIpIfInfo=_SwSrcIpIfInfo_ObjectIdentity((1,3,6,1,4,1,171,12,81,2))
_SwSrcIpIfMgmt_ObjectIdentity=ObjectIdentity
swSrcIpIfMgmt=_SwSrcIpIfMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,81,3))
_SwSrcIpIfTable_Object=MibTable
swSrcIpIfTable=_SwSrcIpIfTable_Object((1,3,6,1,4,1,171,12,81,3,1))
if mibBuilder.loadTexts:swSrcIpIfTable.setStatus(_A)
_SwSrcIpIfEntry_Object=MibTableRow
swSrcIpIfEntry=_SwSrcIpIfEntry_Object((1,3,6,1,4,1,171,12,81,3,1,1))
swSrcIpIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:swSrcIpIfEntry.setStatus(_A)
class _SwSrcIpIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('trap',1),('syslog',2),('radius',3),('tacacs',4)))
_SwSrcIpIfType_Type.__name__=_C
_SwSrcIpIfType_Object=MibTableColumn
swSrcIpIfType=_SwSrcIpIfType_Object((1,3,6,1,4,1,171,12,81,3,1,1,1),_SwSrcIpIfType_Type())
swSrcIpIfType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swSrcIpIfType.setStatus(_A)
_SwSrcIpIfRowStatus_Type=RowStatus
_SwSrcIpIfRowStatus_Object=MibTableColumn
swSrcIpIfRowStatus=_SwSrcIpIfRowStatus_Object((1,3,6,1,4,1,171,12,81,3,1,1,2),_SwSrcIpIfRowStatus_Type())
swSrcIpIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swSrcIpIfRowStatus.setStatus(_A)
class _SwSrcIpIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwSrcIpIfName_Type.__name__=_D
_SwSrcIpIfName_Object=MibTableColumn
swSrcIpIfName=_SwSrcIpIfName_Object((1,3,6,1,4,1,171,12,81,3,1,1,3),_SwSrcIpIfName_Type())
swSrcIpIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:swSrcIpIfName.setStatus(_A)
_SwSrcIpIfIPAddr_Type=IpAddress
_SwSrcIpIfIPAddr_Object=MibTableColumn
swSrcIpIfIPAddr=_SwSrcIpIfIPAddr_Object((1,3,6,1,4,1,171,12,81,3,1,1,4),_SwSrcIpIfIPAddr_Type())
swSrcIpIfIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSrcIpIfIPAddr.setStatus(_A)
_SwSrcIpIfIPv6Addr_Type=Ipv6Address
_SwSrcIpIfIPv6Addr_Object=MibTableColumn
swSrcIpIfIPv6Addr=_SwSrcIpIfIPv6Addr_Object((1,3,6,1,4,1,171,12,81,3,1,1,5),_SwSrcIpIfIPv6Addr_Type())
swSrcIpIfIPv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:swSrcIpIfIPv6Addr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swSrcIpIfMIB':swSrcIpIfMIB,'swSrcIpIfCtrl':swSrcIpIfCtrl,'swSrcIpIfInfo':swSrcIpIfInfo,'swSrcIpIfMgmt':swSrcIpIfMgmt,'swSrcIpIfTable':swSrcIpIfTable,'swSrcIpIfEntry':swSrcIpIfEntry,_F:swSrcIpIfType,'swSrcIpIfRowStatus':swSrcIpIfRowStatus,'swSrcIpIfName':swSrcIpIfName,'swSrcIpIfIPAddr':swSrcIpIfIPAddr,'swSrcIpIfIPv6Addr':swSrcIpIfIPv6Addr})