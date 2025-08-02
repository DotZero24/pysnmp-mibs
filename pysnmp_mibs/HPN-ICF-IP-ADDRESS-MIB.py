_V='hpnicfIpAddrFirstTrapTime'
_U='hpnicfIpAddrNewIpAddress'
_T='hpnicfIpAddrOldIpAddress'
_S='hpnicfIpAddrNotifyIfIndex'
_R='cluster'
_Q='hpnicfIpAddrReadAddr'
_P='hpnicfIpAddrReadAddrType'
_O='hpnicfIpAddrReadIfIndex'
_N='primary'
_M='assignedIp'
_L='hpnicfIpAddrSetAddr'
_K='hpnicfIpAddrSetAddrType'
_J='hpnicfIpAddrSetIfIndex'
_I='ifIndex'
_H='IF-MIB'
_G='read-only'
_F='accessible-for-notify'
_E='not-accessible'
_D='read-create'
_C='Integer32'
_B='HPN-ICF-IP-ADDRESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfIpAddrMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67))
if mibBuilder.loadTexts:hpnicfIpAddrMIB.setRevisions(('2005-11-22 00:00',))
_HpnicfIpAddressObjects_ObjectIdentity=ObjectIdentity
hpnicfIpAddressObjects=_HpnicfIpAddressObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67,1))
_HpnicfIpAddressConfig_ObjectIdentity=ObjectIdentity
hpnicfIpAddressConfig=_HpnicfIpAddressConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1))
_HpnicfIpAddrSetTable_Object=MibTable
hpnicfIpAddrSetTable=_HpnicfIpAddrSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1))
if mibBuilder.loadTexts:hpnicfIpAddrSetTable.setStatus(_A)
_HpnicfIpAddrSetEntry_Object=MibTableRow
hpnicfIpAddrSetEntry=_HpnicfIpAddrSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1))
hpnicfIpAddrSetEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfIpAddrSetEntry.setStatus(_A)
class _HpnicfIpAddrSetIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpAddrSetIfIndex_Type.__name__=_C
_HpnicfIpAddrSetIfIndex_Object=MibTableColumn
hpnicfIpAddrSetIfIndex=_HpnicfIpAddrSetIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,1),_HpnicfIpAddrSetIfIndex_Type())
hpnicfIpAddrSetIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpAddrSetIfIndex.setStatus(_A)
_HpnicfIpAddrSetAddrType_Type=InetAddressType
_HpnicfIpAddrSetAddrType_Object=MibTableColumn
hpnicfIpAddrSetAddrType=_HpnicfIpAddrSetAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,2),_HpnicfIpAddrSetAddrType_Type())
hpnicfIpAddrSetAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpAddrSetAddrType.setStatus(_A)
_HpnicfIpAddrSetAddr_Type=InetAddress
_HpnicfIpAddrSetAddr_Object=MibTableColumn
hpnicfIpAddrSetAddr=_HpnicfIpAddrSetAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,3),_HpnicfIpAddrSetAddr_Type())
hpnicfIpAddrSetAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpAddrSetAddr.setStatus(_A)
_HpnicfIpAddrSetMask_Type=IpAddress
_HpnicfIpAddrSetMask_Object=MibTableColumn
hpnicfIpAddrSetMask=_HpnicfIpAddrSetMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,4),_HpnicfIpAddrSetMask_Type())
hpnicfIpAddrSetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpAddrSetMask.setStatus(_A)
class _HpnicfIpAddrSetSourceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_M,1))
_HpnicfIpAddrSetSourceType_Type.__name__=_C
_HpnicfIpAddrSetSourceType_Object=MibTableColumn
hpnicfIpAddrSetSourceType=_HpnicfIpAddrSetSourceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,5),_HpnicfIpAddrSetSourceType_Type())
hpnicfIpAddrSetSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpAddrSetSourceType.setStatus(_A)
class _HpnicfIpAddrSetCatalog_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('sub',2)))
_HpnicfIpAddrSetCatalog_Type.__name__=_C
_HpnicfIpAddrSetCatalog_Object=MibTableColumn
hpnicfIpAddrSetCatalog=_HpnicfIpAddrSetCatalog_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,6),_HpnicfIpAddrSetCatalog_Type())
hpnicfIpAddrSetCatalog.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpAddrSetCatalog.setStatus(_A)
_HpnicfIpAddrSetRowStatus_Type=RowStatus
_HpnicfIpAddrSetRowStatus_Object=MibTableColumn
hpnicfIpAddrSetRowStatus=_HpnicfIpAddrSetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,1,1,7),_HpnicfIpAddrSetRowStatus_Type())
hpnicfIpAddrSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpAddrSetRowStatus.setStatus(_A)
_HpnicfIpAddrReadTable_Object=MibTable
hpnicfIpAddrReadTable=_HpnicfIpAddrReadTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2))
if mibBuilder.loadTexts:hpnicfIpAddrReadTable.setStatus(_A)
_HpnicfIpAddrReadEntry_Object=MibTableRow
hpnicfIpAddrReadEntry=_HpnicfIpAddrReadEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1))
hpnicfIpAddrReadEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfIpAddrReadEntry.setStatus(_A)
class _HpnicfIpAddrReadIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpAddrReadIfIndex_Type.__name__=_C
_HpnicfIpAddrReadIfIndex_Object=MibTableColumn
hpnicfIpAddrReadIfIndex=_HpnicfIpAddrReadIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1,1),_HpnicfIpAddrReadIfIndex_Type())
hpnicfIpAddrReadIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpAddrReadIfIndex.setStatus(_A)
_HpnicfIpAddrReadAddrType_Type=InetAddressType
_HpnicfIpAddrReadAddrType_Object=MibTableColumn
hpnicfIpAddrReadAddrType=_HpnicfIpAddrReadAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1,2),_HpnicfIpAddrReadAddrType_Type())
hpnicfIpAddrReadAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpAddrReadAddrType.setStatus(_A)
_HpnicfIpAddrReadAddr_Type=InetAddress
_HpnicfIpAddrReadAddr_Object=MibTableColumn
hpnicfIpAddrReadAddr=_HpnicfIpAddrReadAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1,3),_HpnicfIpAddrReadAddr_Type())
hpnicfIpAddrReadAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpAddrReadAddr.setStatus(_A)
_HpnicfIpAddrReadMask_Type=IpAddress
_HpnicfIpAddrReadMask_Object=MibTableColumn
hpnicfIpAddrReadMask=_HpnicfIpAddrReadMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1,4),_HpnicfIpAddrReadMask_Type())
hpnicfIpAddrReadMask.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpAddrReadMask.setStatus(_A)
class _HpnicfIpAddrReadSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),(_R,2),('dhcp',3),('bootp',4),('negotiate',5),('unnumbered',6),('vrrp',7)))
_HpnicfIpAddrReadSourceType_Type.__name__=_C
_HpnicfIpAddrReadSourceType_Object=MibTableColumn
hpnicfIpAddrReadSourceType=_HpnicfIpAddrReadSourceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1,5),_HpnicfIpAddrReadSourceType_Type())
hpnicfIpAddrReadSourceType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpAddrReadSourceType.setStatus(_A)
class _HpnicfIpAddrReadCatalog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('sub',2),(_R,3),('vrrp',4)))
_HpnicfIpAddrReadCatalog_Type.__name__=_C
_HpnicfIpAddrReadCatalog_Object=MibTableColumn
hpnicfIpAddrReadCatalog=_HpnicfIpAddrReadCatalog_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,2,1,6),_HpnicfIpAddrReadCatalog_Type())
hpnicfIpAddrReadCatalog.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfIpAddrReadCatalog.setStatus(_A)
_HpnicfIpv4AddrTable_Object=MibTable
hpnicfIpv4AddrTable=_HpnicfIpv4AddrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,3))
if mibBuilder.loadTexts:hpnicfIpv4AddrTable.setStatus(_A)
_HpnicfIpv4AddrEntry_Object=MibTableRow
hpnicfIpv4AddrEntry=_HpnicfIpv4AddrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,3,1))
hpnicfIpv4AddrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfIpv4AddrEntry.setStatus(_A)
_HpnicfIpv4AddrAddr_Type=IpAddress
_HpnicfIpv4AddrAddr_Object=MibTableColumn
hpnicfIpv4AddrAddr=_HpnicfIpv4AddrAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,3,1,1),_HpnicfIpv4AddrAddr_Type())
hpnicfIpv4AddrAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv4AddrAddr.setStatus(_A)
_HpnicfIpv4AddrMask_Type=IpAddress
_HpnicfIpv4AddrMask_Object=MibTableColumn
hpnicfIpv4AddrMask=_HpnicfIpv4AddrMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,3,1,2),_HpnicfIpv4AddrMask_Type())
hpnicfIpv4AddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv4AddrMask.setStatus(_A)
_HpnicfIpv4AddrRowStatus_Type=RowStatus
_HpnicfIpv4AddrRowStatus_Object=MibTableColumn
hpnicfIpv4AddrRowStatus=_HpnicfIpv4AddrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,1,1,3,1,3),_HpnicfIpv4AddrRowStatus_Type())
hpnicfIpv4AddrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv4AddrRowStatus.setStatus(_A)
_HpnicfIpAddrNotify_ObjectIdentity=ObjectIdentity
hpnicfIpAddrNotify=_HpnicfIpAddrNotify_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67,2))
_HpnicfIpAddrNotifyScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfIpAddrNotifyScalarObjects=_HpnicfIpAddrNotifyScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67,2,1))
class _HpnicfIpAddrNotifyIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpAddrNotifyIfIndex_Type.__name__=_C
_HpnicfIpAddrNotifyIfIndex_Object=MibScalar
hpnicfIpAddrNotifyIfIndex=_HpnicfIpAddrNotifyIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,2,1,1),_HpnicfIpAddrNotifyIfIndex_Type())
hpnicfIpAddrNotifyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpAddrNotifyIfIndex.setStatus(_A)
_HpnicfIpAddrOldIpAddress_Type=InetAddress
_HpnicfIpAddrOldIpAddress_Object=MibScalar
hpnicfIpAddrOldIpAddress=_HpnicfIpAddrOldIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,2,1,2),_HpnicfIpAddrOldIpAddress_Type())
hpnicfIpAddrOldIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpAddrOldIpAddress.setStatus(_A)
_HpnicfIpAddrNewIpAddress_Type=InetAddress
_HpnicfIpAddrNewIpAddress_Object=MibScalar
hpnicfIpAddrNewIpAddress=_HpnicfIpAddrNewIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,2,1,3),_HpnicfIpAddrNewIpAddress_Type())
hpnicfIpAddrNewIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpAddrNewIpAddress.setStatus(_A)
_HpnicfIpAddrFirstTrapTime_Type=TimeTicks
_HpnicfIpAddrFirstTrapTime_Object=MibScalar
hpnicfIpAddrFirstTrapTime=_HpnicfIpAddrFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,67,2,1,4),_HpnicfIpAddrFirstTrapTime_Type())
hpnicfIpAddrFirstTrapTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpAddrFirstTrapTime.setStatus(_A)
_HpnicfIpAddrNotifyObjects_ObjectIdentity=ObjectIdentity
hpnicfIpAddrNotifyObjects=_HpnicfIpAddrNotifyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67,2,2))
_HpnicfIpAddrNotifyObjectsPrefix_ObjectIdentity=ObjectIdentity
hpnicfIpAddrNotifyObjectsPrefix=_HpnicfIpAddrNotifyObjectsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,67,2,2,0))
hpnicfIpAddressChangeNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,67,2,2,0,1))
hpnicfIpAddressChangeNotify.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:hpnicfIpAddressChangeNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfIpAddrMIB':hpnicfIpAddrMIB,'hpnicfIpAddressObjects':hpnicfIpAddressObjects,'hpnicfIpAddressConfig':hpnicfIpAddressConfig,'hpnicfIpAddrSetTable':hpnicfIpAddrSetTable,'hpnicfIpAddrSetEntry':hpnicfIpAddrSetEntry,_J:hpnicfIpAddrSetIfIndex,_K:hpnicfIpAddrSetAddrType,_L:hpnicfIpAddrSetAddr,'hpnicfIpAddrSetMask':hpnicfIpAddrSetMask,'hpnicfIpAddrSetSourceType':hpnicfIpAddrSetSourceType,'hpnicfIpAddrSetCatalog':hpnicfIpAddrSetCatalog,'hpnicfIpAddrSetRowStatus':hpnicfIpAddrSetRowStatus,'hpnicfIpAddrReadTable':hpnicfIpAddrReadTable,'hpnicfIpAddrReadEntry':hpnicfIpAddrReadEntry,_O:hpnicfIpAddrReadIfIndex,_P:hpnicfIpAddrReadAddrType,_Q:hpnicfIpAddrReadAddr,'hpnicfIpAddrReadMask':hpnicfIpAddrReadMask,'hpnicfIpAddrReadSourceType':hpnicfIpAddrReadSourceType,'hpnicfIpAddrReadCatalog':hpnicfIpAddrReadCatalog,'hpnicfIpv4AddrTable':hpnicfIpv4AddrTable,'hpnicfIpv4AddrEntry':hpnicfIpv4AddrEntry,'hpnicfIpv4AddrAddr':hpnicfIpv4AddrAddr,'hpnicfIpv4AddrMask':hpnicfIpv4AddrMask,'hpnicfIpv4AddrRowStatus':hpnicfIpv4AddrRowStatus,'hpnicfIpAddrNotify':hpnicfIpAddrNotify,'hpnicfIpAddrNotifyScalarObjects':hpnicfIpAddrNotifyScalarObjects,_S:hpnicfIpAddrNotifyIfIndex,_T:hpnicfIpAddrOldIpAddress,_U:hpnicfIpAddrNewIpAddress,_V:hpnicfIpAddrFirstTrapTime,'hpnicfIpAddrNotifyObjects':hpnicfIpAddrNotifyObjects,'hpnicfIpAddrNotifyObjectsPrefix':hpnicfIpAddrNotifyObjectsPrefix,'hpnicfIpAddressChangeNotify':hpnicfIpAddressChangeNotify})