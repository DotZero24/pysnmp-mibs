_V='h3cIpAddrFirstTrapTime'
_U='h3cIpAddrNewIpAddress'
_T='h3cIpAddrOldIpAddress'
_S='h3cIpAddrNotifyIfIndex'
_R='cluster'
_Q='h3cIpAddrReadAddr'
_P='h3cIpAddrReadAddrType'
_O='h3cIpAddrReadIfIndex'
_N='primary'
_M='assignedIp'
_L='h3cIpAddrSetAddr'
_K='h3cIpAddrSetAddrType'
_J='h3cIpAddrSetIfIndex'
_I='ifIndex'
_H='IF-MIB'
_G='read-only'
_F='accessible-for-notify'
_E='not-accessible'
_D='read-create'
_C='Integer32'
_B='H3C-IP-ADDRESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cIpAddrMIB=ModuleIdentity((1,3,6,1,4,1,2011,10,2,67))
if mibBuilder.loadTexts:h3cIpAddrMIB.setRevisions(('2005-11-22 00:00',))
_H3cIpAddressObjects_ObjectIdentity=ObjectIdentity
h3cIpAddressObjects=_H3cIpAddressObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,67,1))
_H3cIpAddressConfig_ObjectIdentity=ObjectIdentity
h3cIpAddressConfig=_H3cIpAddressConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,67,1,1))
_H3cIpAddrSetTable_Object=MibTable
h3cIpAddrSetTable=_H3cIpAddrSetTable_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1))
if mibBuilder.loadTexts:h3cIpAddrSetTable.setStatus(_A)
_H3cIpAddrSetEntry_Object=MibTableRow
h3cIpAddrSetEntry=_H3cIpAddrSetEntry_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1))
h3cIpAddrSetEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:h3cIpAddrSetEntry.setStatus(_A)
class _H3cIpAddrSetIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpAddrSetIfIndex_Type.__name__=_C
_H3cIpAddrSetIfIndex_Object=MibTableColumn
h3cIpAddrSetIfIndex=_H3cIpAddrSetIfIndex_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,1),_H3cIpAddrSetIfIndex_Type())
h3cIpAddrSetIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpAddrSetIfIndex.setStatus(_A)
_H3cIpAddrSetAddrType_Type=InetAddressType
_H3cIpAddrSetAddrType_Object=MibTableColumn
h3cIpAddrSetAddrType=_H3cIpAddrSetAddrType_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,2),_H3cIpAddrSetAddrType_Type())
h3cIpAddrSetAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpAddrSetAddrType.setStatus(_A)
_H3cIpAddrSetAddr_Type=InetAddress
_H3cIpAddrSetAddr_Object=MibTableColumn
h3cIpAddrSetAddr=_H3cIpAddrSetAddr_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,3),_H3cIpAddrSetAddr_Type())
h3cIpAddrSetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpAddrSetAddr.setStatus(_A)
_H3cIpAddrSetMask_Type=IpAddress
_H3cIpAddrSetMask_Object=MibTableColumn
h3cIpAddrSetMask=_H3cIpAddrSetMask_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,4),_H3cIpAddrSetMask_Type())
h3cIpAddrSetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpAddrSetMask.setStatus(_A)
class _H3cIpAddrSetSourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_M,1))
_H3cIpAddrSetSourceType_Type.__name__=_C
_H3cIpAddrSetSourceType_Object=MibTableColumn
h3cIpAddrSetSourceType=_H3cIpAddrSetSourceType_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,5),_H3cIpAddrSetSourceType_Type())
h3cIpAddrSetSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpAddrSetSourceType.setStatus(_A)
class _H3cIpAddrSetCatalog_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('sub',2)))
_H3cIpAddrSetCatalog_Type.__name__=_C
_H3cIpAddrSetCatalog_Object=MibTableColumn
h3cIpAddrSetCatalog=_H3cIpAddrSetCatalog_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,6),_H3cIpAddrSetCatalog_Type())
h3cIpAddrSetCatalog.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpAddrSetCatalog.setStatus(_A)
_H3cIpAddrSetRowStatus_Type=RowStatus
_H3cIpAddrSetRowStatus_Object=MibTableColumn
h3cIpAddrSetRowStatus=_H3cIpAddrSetRowStatus_Object((1,3,6,1,4,1,2011,10,2,67,1,1,1,1,7),_H3cIpAddrSetRowStatus_Type())
h3cIpAddrSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpAddrSetRowStatus.setStatus(_A)
_H3cIpAddrReadTable_Object=MibTable
h3cIpAddrReadTable=_H3cIpAddrReadTable_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2))
if mibBuilder.loadTexts:h3cIpAddrReadTable.setStatus(_A)
_H3cIpAddrReadEntry_Object=MibTableRow
h3cIpAddrReadEntry=_H3cIpAddrReadEntry_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1))
h3cIpAddrReadEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:h3cIpAddrReadEntry.setStatus(_A)
class _H3cIpAddrReadIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpAddrReadIfIndex_Type.__name__=_C
_H3cIpAddrReadIfIndex_Object=MibTableColumn
h3cIpAddrReadIfIndex=_H3cIpAddrReadIfIndex_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1,1),_H3cIpAddrReadIfIndex_Type())
h3cIpAddrReadIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpAddrReadIfIndex.setStatus(_A)
_H3cIpAddrReadAddrType_Type=InetAddressType
_H3cIpAddrReadAddrType_Object=MibTableColumn
h3cIpAddrReadAddrType=_H3cIpAddrReadAddrType_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1,2),_H3cIpAddrReadAddrType_Type())
h3cIpAddrReadAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpAddrReadAddrType.setStatus(_A)
_H3cIpAddrReadAddr_Type=InetAddress
_H3cIpAddrReadAddr_Object=MibTableColumn
h3cIpAddrReadAddr=_H3cIpAddrReadAddr_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1,3),_H3cIpAddrReadAddr_Type())
h3cIpAddrReadAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpAddrReadAddr.setStatus(_A)
_H3cIpAddrReadMask_Type=IpAddress
_H3cIpAddrReadMask_Object=MibTableColumn
h3cIpAddrReadMask=_H3cIpAddrReadMask_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1,4),_H3cIpAddrReadMask_Type())
h3cIpAddrReadMask.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpAddrReadMask.setStatus(_A)
class _H3cIpAddrReadSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_R,2),('dhcp',3),('bootp',4),('negotiate',5),('unnumbered',6),('vrrp',7)))
_H3cIpAddrReadSourceType_Type.__name__=_C
_H3cIpAddrReadSourceType_Object=MibTableColumn
h3cIpAddrReadSourceType=_H3cIpAddrReadSourceType_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1,5),_H3cIpAddrReadSourceType_Type())
h3cIpAddrReadSourceType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpAddrReadSourceType.setStatus(_A)
class _H3cIpAddrReadCatalog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('sub',2),(_R,3),('vrrp',4)))
_H3cIpAddrReadCatalog_Type.__name__=_C
_H3cIpAddrReadCatalog_Object=MibTableColumn
h3cIpAddrReadCatalog=_H3cIpAddrReadCatalog_Object((1,3,6,1,4,1,2011,10,2,67,1,1,2,1,6),_H3cIpAddrReadCatalog_Type())
h3cIpAddrReadCatalog.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cIpAddrReadCatalog.setStatus(_A)
_H3cIpv4AddrTable_Object=MibTable
h3cIpv4AddrTable=_H3cIpv4AddrTable_Object((1,3,6,1,4,1,2011,10,2,67,1,1,3))
if mibBuilder.loadTexts:h3cIpv4AddrTable.setStatus(_A)
_H3cIpv4AddrEntry_Object=MibTableRow
h3cIpv4AddrEntry=_H3cIpv4AddrEntry_Object((1,3,6,1,4,1,2011,10,2,67,1,1,3,1))
h3cIpv4AddrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cIpv4AddrEntry.setStatus(_A)
_H3cIpv4AddrAddr_Type=IpAddress
_H3cIpv4AddrAddr_Object=MibTableColumn
h3cIpv4AddrAddr=_H3cIpv4AddrAddr_Object((1,3,6,1,4,1,2011,10,2,67,1,1,3,1,1),_H3cIpv4AddrAddr_Type())
h3cIpv4AddrAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv4AddrAddr.setStatus(_A)
_H3cIpv4AddrMask_Type=IpAddress
_H3cIpv4AddrMask_Object=MibTableColumn
h3cIpv4AddrMask=_H3cIpv4AddrMask_Object((1,3,6,1,4,1,2011,10,2,67,1,1,3,1,2),_H3cIpv4AddrMask_Type())
h3cIpv4AddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv4AddrMask.setStatus(_A)
_H3cIpv4AddrRowStatus_Type=RowStatus
_H3cIpv4AddrRowStatus_Object=MibTableColumn
h3cIpv4AddrRowStatus=_H3cIpv4AddrRowStatus_Object((1,3,6,1,4,1,2011,10,2,67,1,1,3,1,3),_H3cIpv4AddrRowStatus_Type())
h3cIpv4AddrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv4AddrRowStatus.setStatus(_A)
_H3cIpAddrNotify_ObjectIdentity=ObjectIdentity
h3cIpAddrNotify=_H3cIpAddrNotify_ObjectIdentity((1,3,6,1,4,1,2011,10,2,67,2))
_H3cIpAddrNotifyScalarObjects_ObjectIdentity=ObjectIdentity
h3cIpAddrNotifyScalarObjects=_H3cIpAddrNotifyScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,67,2,1))
class _H3cIpAddrNotifyIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpAddrNotifyIfIndex_Type.__name__=_C
_H3cIpAddrNotifyIfIndex_Object=MibScalar
h3cIpAddrNotifyIfIndex=_H3cIpAddrNotifyIfIndex_Object((1,3,6,1,4,1,2011,10,2,67,2,1,1),_H3cIpAddrNotifyIfIndex_Type())
h3cIpAddrNotifyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpAddrNotifyIfIndex.setStatus(_A)
_H3cIpAddrOldIpAddress_Type=InetAddress
_H3cIpAddrOldIpAddress_Object=MibScalar
h3cIpAddrOldIpAddress=_H3cIpAddrOldIpAddress_Object((1,3,6,1,4,1,2011,10,2,67,2,1,2),_H3cIpAddrOldIpAddress_Type())
h3cIpAddrOldIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpAddrOldIpAddress.setStatus(_A)
_H3cIpAddrNewIpAddress_Type=InetAddress
_H3cIpAddrNewIpAddress_Object=MibScalar
h3cIpAddrNewIpAddress=_H3cIpAddrNewIpAddress_Object((1,3,6,1,4,1,2011,10,2,67,2,1,3),_H3cIpAddrNewIpAddress_Type())
h3cIpAddrNewIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpAddrNewIpAddress.setStatus(_A)
_H3cIpAddrFirstTrapTime_Type=TimeTicks
_H3cIpAddrFirstTrapTime_Object=MibScalar
h3cIpAddrFirstTrapTime=_H3cIpAddrFirstTrapTime_Object((1,3,6,1,4,1,2011,10,2,67,2,1,4),_H3cIpAddrFirstTrapTime_Type())
h3cIpAddrFirstTrapTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpAddrFirstTrapTime.setStatus(_A)
_H3cIpAddrNotifyObjects_ObjectIdentity=ObjectIdentity
h3cIpAddrNotifyObjects=_H3cIpAddrNotifyObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,67,2,2))
_H3cIpAddrNotifyObjectsPrefix_ObjectIdentity=ObjectIdentity
h3cIpAddrNotifyObjectsPrefix=_H3cIpAddrNotifyObjectsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,67,2,2,0))
h3cIpAddressChangeNotify=NotificationType((1,3,6,1,4,1,2011,10,2,67,2,2,0,1))
h3cIpAddressChangeNotify.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:h3cIpAddressChangeNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cIpAddrMIB':h3cIpAddrMIB,'h3cIpAddressObjects':h3cIpAddressObjects,'h3cIpAddressConfig':h3cIpAddressConfig,'h3cIpAddrSetTable':h3cIpAddrSetTable,'h3cIpAddrSetEntry':h3cIpAddrSetEntry,_J:h3cIpAddrSetIfIndex,_K:h3cIpAddrSetAddrType,_L:h3cIpAddrSetAddr,'h3cIpAddrSetMask':h3cIpAddrSetMask,'h3cIpAddrSetSourceType':h3cIpAddrSetSourceType,'h3cIpAddrSetCatalog':h3cIpAddrSetCatalog,'h3cIpAddrSetRowStatus':h3cIpAddrSetRowStatus,'h3cIpAddrReadTable':h3cIpAddrReadTable,'h3cIpAddrReadEntry':h3cIpAddrReadEntry,_O:h3cIpAddrReadIfIndex,_P:h3cIpAddrReadAddrType,_Q:h3cIpAddrReadAddr,'h3cIpAddrReadMask':h3cIpAddrReadMask,'h3cIpAddrReadSourceType':h3cIpAddrReadSourceType,'h3cIpAddrReadCatalog':h3cIpAddrReadCatalog,'h3cIpv4AddrTable':h3cIpv4AddrTable,'h3cIpv4AddrEntry':h3cIpv4AddrEntry,'h3cIpv4AddrAddr':h3cIpv4AddrAddr,'h3cIpv4AddrMask':h3cIpv4AddrMask,'h3cIpv4AddrRowStatus':h3cIpv4AddrRowStatus,'h3cIpAddrNotify':h3cIpAddrNotify,'h3cIpAddrNotifyScalarObjects':h3cIpAddrNotifyScalarObjects,_S:h3cIpAddrNotifyIfIndex,_T:h3cIpAddrOldIpAddress,_U:h3cIpAddrNewIpAddress,_V:h3cIpAddrFirstTrapTime,'h3cIpAddrNotifyObjects':h3cIpAddrNotifyObjects,'h3cIpAddrNotifyObjectsPrefix':h3cIpAddrNotifyObjectsPrefix,'h3cIpAddressChangeNotify':h3cIpAddressChangeNotify})