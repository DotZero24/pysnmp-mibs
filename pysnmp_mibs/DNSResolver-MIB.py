_O='swDNSResDynamicHostIndex'
_N='swDNSResStaticHostIndex'
_M='swDNSResStaticIPv6NameSrvIndex'
_L='swDNSResDynamicNameSrvIndex'
_K='swDNSResStaticNameSrvIndex'
_J='secondary'
_I='primary'
_H='DisplayString'
_G='read-only'
_F='not-accessible'
_E='DNSResolver-MIB'
_D='read-write'
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
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
swDNSResolverMIB=ModuleIdentity((1,3,6,1,4,1,171,12,85))
class DnsName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class DnsTime(TextualConvention,Integer32):status=_A;displayHint='4d'
_SwDNSResolverMIBObjects_ObjectIdentity=ObjectIdentity
swDNSResolverMIBObjects=_SwDNSResolverMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,85,1))
class _SwDNSResState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwDNSResState_Type.__name__=_C
_SwDNSResState_Object=MibScalar
swDNSResState=_SwDNSResState_Object((1,3,6,1,4,1,171,12,85,1,1),_SwDNSResState_Type())
swDNSResState.setMaxAccess(_D)
if mibBuilder.loadTexts:swDNSResState.setStatus(_A)
class _SwDNSResNameSrvTimeOut_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SwDNSResNameSrvTimeOut_Type.__name__=_C
_SwDNSResNameSrvTimeOut_Object=MibScalar
swDNSResNameSrvTimeOut=_SwDNSResNameSrvTimeOut_Object((1,3,6,1,4,1,171,12,85,1,2),_SwDNSResNameSrvTimeOut_Type())
swDNSResNameSrvTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:swDNSResNameSrvTimeOut.setStatus(_A)
_SwDNSResNameSrv_ObjectIdentity=ObjectIdentity
swDNSResNameSrv=_SwDNSResNameSrv_ObjectIdentity((1,3,6,1,4,1,171,12,85,1,3))
_SwDNSResStaticNameSrvTable_Object=MibTable
swDNSResStaticNameSrvTable=_SwDNSResStaticNameSrvTable_Object((1,3,6,1,4,1,171,12,85,1,3,1))
if mibBuilder.loadTexts:swDNSResStaticNameSrvTable.setStatus(_A)
_SwDNSResStaticNameSrvEntry_Object=MibTableRow
swDNSResStaticNameSrvEntry=_SwDNSResStaticNameSrvEntry_Object((1,3,6,1,4,1,171,12,85,1,3,1,1))
swDNSResStaticNameSrvEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:swDNSResStaticNameSrvEntry.setStatus(_A)
_SwDNSResStaticNameSrvIndex_Type=Integer32
_SwDNSResStaticNameSrvIndex_Object=MibTableColumn
swDNSResStaticNameSrvIndex=_SwDNSResStaticNameSrvIndex_Object((1,3,6,1,4,1,171,12,85,1,3,1,1,1),_SwDNSResStaticNameSrvIndex_Type())
swDNSResStaticNameSrvIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swDNSResStaticNameSrvIndex.setStatus(_A)
_SwDNSResStaticNameSrvRowStatus_Type=RowStatus
_SwDNSResStaticNameSrvRowStatus_Object=MibTableColumn
swDNSResStaticNameSrvRowStatus=_SwDNSResStaticNameSrvRowStatus_Object((1,3,6,1,4,1,171,12,85,1,3,1,1,2),_SwDNSResStaticNameSrvRowStatus_Type())
swDNSResStaticNameSrvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticNameSrvRowStatus.setStatus(_A)
_SwDNSResStaticNameSrvIPaddr_Type=IpAddress
_SwDNSResStaticNameSrvIPaddr_Object=MibTableColumn
swDNSResStaticNameSrvIPaddr=_SwDNSResStaticNameSrvIPaddr_Object((1,3,6,1,4,1,171,12,85,1,3,1,1,3),_SwDNSResStaticNameSrvIPaddr_Type())
swDNSResStaticNameSrvIPaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticNameSrvIPaddr.setStatus(_A)
class _SwDNSResStaticNameSrvPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SwDNSResStaticNameSrvPriority_Type.__name__=_C
_SwDNSResStaticNameSrvPriority_Object=MibTableColumn
swDNSResStaticNameSrvPriority=_SwDNSResStaticNameSrvPriority_Object((1,3,6,1,4,1,171,12,85,1,3,1,1,4),_SwDNSResStaticNameSrvPriority_Type())
swDNSResStaticNameSrvPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticNameSrvPriority.setStatus(_A)
_SwDNSResDynamicNameSrvTable_Object=MibTable
swDNSResDynamicNameSrvTable=_SwDNSResDynamicNameSrvTable_Object((1,3,6,1,4,1,171,12,85,1,3,2))
if mibBuilder.loadTexts:swDNSResDynamicNameSrvTable.setStatus(_A)
_SwDNSResDynamicNameSrvEntry_Object=MibTableRow
swDNSResDynamicNameSrvEntry=_SwDNSResDynamicNameSrvEntry_Object((1,3,6,1,4,1,171,12,85,1,3,2,1))
swDNSResDynamicNameSrvEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swDNSResDynamicNameSrvEntry.setStatus(_A)
_SwDNSResDynamicNameSrvIndex_Type=Integer32
_SwDNSResDynamicNameSrvIndex_Object=MibTableColumn
swDNSResDynamicNameSrvIndex=_SwDNSResDynamicNameSrvIndex_Object((1,3,6,1,4,1,171,12,85,1,3,2,1,1),_SwDNSResDynamicNameSrvIndex_Type())
swDNSResDynamicNameSrvIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swDNSResDynamicNameSrvIndex.setStatus(_A)
_SwDNSResDynamicNameSrvIPaddr_Type=IpAddress
_SwDNSResDynamicNameSrvIPaddr_Object=MibTableColumn
swDNSResDynamicNameSrvIPaddr=_SwDNSResDynamicNameSrvIPaddr_Object((1,3,6,1,4,1,171,12,85,1,3,2,1,2),_SwDNSResDynamicNameSrvIPaddr_Type())
swDNSResDynamicNameSrvIPaddr.setMaxAccess(_G)
if mibBuilder.loadTexts:swDNSResDynamicNameSrvIPaddr.setStatus(_A)
class _SwDNSResDynamicNameSrvPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SwDNSResDynamicNameSrvPriority_Type.__name__=_C
_SwDNSResDynamicNameSrvPriority_Object=MibTableColumn
swDNSResDynamicNameSrvPriority=_SwDNSResDynamicNameSrvPriority_Object((1,3,6,1,4,1,171,12,85,1,3,2,1,3),_SwDNSResDynamicNameSrvPriority_Type())
swDNSResDynamicNameSrvPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:swDNSResDynamicNameSrvPriority.setStatus(_A)
_SwDNSResStaticIPv6NameSrvTable_Object=MibTable
swDNSResStaticIPv6NameSrvTable=_SwDNSResStaticIPv6NameSrvTable_Object((1,3,6,1,4,1,171,12,85,1,3,3))
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvTable.setStatus(_A)
_SwDNSResStaticIPv6NameSrvEntry_Object=MibTableRow
swDNSResStaticIPv6NameSrvEntry=_SwDNSResStaticIPv6NameSrvEntry_Object((1,3,6,1,4,1,171,12,85,1,3,3,1))
swDNSResStaticIPv6NameSrvEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvEntry.setStatus(_A)
_SwDNSResStaticIPv6NameSrvIndex_Type=Integer32
_SwDNSResStaticIPv6NameSrvIndex_Object=MibTableColumn
swDNSResStaticIPv6NameSrvIndex=_SwDNSResStaticIPv6NameSrvIndex_Object((1,3,6,1,4,1,171,12,85,1,3,3,1,1),_SwDNSResStaticIPv6NameSrvIndex_Type())
swDNSResStaticIPv6NameSrvIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvIndex.setStatus(_A)
_SwDNSResStaticIPv6NameSrvaddr_Type=Ipv6Address
_SwDNSResStaticIPv6NameSrvaddr_Object=MibTableColumn
swDNSResStaticIPv6NameSrvaddr=_SwDNSResStaticIPv6NameSrvaddr_Object((1,3,6,1,4,1,171,12,85,1,3,3,1,2),_SwDNSResStaticIPv6NameSrvaddr_Type())
swDNSResStaticIPv6NameSrvaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvaddr.setStatus(_A)
class _SwDNSResStaticIPv6NameSrvIntfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwDNSResStaticIPv6NameSrvIntfName_Type.__name__=_H
_SwDNSResStaticIPv6NameSrvIntfName_Object=MibTableColumn
swDNSResStaticIPv6NameSrvIntfName=_SwDNSResStaticIPv6NameSrvIntfName_Object((1,3,6,1,4,1,171,12,85,1,3,3,1,3),_SwDNSResStaticIPv6NameSrvIntfName_Type())
swDNSResStaticIPv6NameSrvIntfName.setMaxAccess(_D)
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvIntfName.setStatus(_A)
class _SwDNSResStaticIPv6NameSrvPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SwDNSResStaticIPv6NameSrvPriority_Type.__name__=_C
_SwDNSResStaticIPv6NameSrvPriority_Object=MibTableColumn
swDNSResStaticIPv6NameSrvPriority=_SwDNSResStaticIPv6NameSrvPriority_Object((1,3,6,1,4,1,171,12,85,1,3,3,1,4),_SwDNSResStaticIPv6NameSrvPriority_Type())
swDNSResStaticIPv6NameSrvPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvPriority.setStatus(_A)
_SwDNSResStaticIPv6NameSrvRowStatus_Type=RowStatus
_SwDNSResStaticIPv6NameSrvRowStatus_Object=MibTableColumn
swDNSResStaticIPv6NameSrvRowStatus=_SwDNSResStaticIPv6NameSrvRowStatus_Object((1,3,6,1,4,1,171,12,85,1,3,3,1,100),_SwDNSResStaticIPv6NameSrvRowStatus_Type())
swDNSResStaticIPv6NameSrvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticIPv6NameSrvRowStatus.setStatus(_A)
_SwDNSResHost_ObjectIdentity=ObjectIdentity
swDNSResHost=_SwDNSResHost_ObjectIdentity((1,3,6,1,4,1,171,12,85,1,4))
_SwDNSResStaticHostTable_Object=MibTable
swDNSResStaticHostTable=_SwDNSResStaticHostTable_Object((1,3,6,1,4,1,171,12,85,1,4,1))
if mibBuilder.loadTexts:swDNSResStaticHostTable.setStatus(_A)
_SwDNSResStaticHostEntry_Object=MibTableRow
swDNSResStaticHostEntry=_SwDNSResStaticHostEntry_Object((1,3,6,1,4,1,171,12,85,1,4,1,1))
swDNSResStaticHostEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:swDNSResStaticHostEntry.setStatus(_A)
_SwDNSResStaticHostIndex_Type=Integer32
_SwDNSResStaticHostIndex_Object=MibTableColumn
swDNSResStaticHostIndex=_SwDNSResStaticHostIndex_Object((1,3,6,1,4,1,171,12,85,1,4,1,1,1),_SwDNSResStaticHostIndex_Type())
swDNSResStaticHostIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swDNSResStaticHostIndex.setStatus(_A)
_SwDNSResStaticHostRowStatus_Type=RowStatus
_SwDNSResStaticHostRowStatus_Object=MibTableColumn
swDNSResStaticHostRowStatus=_SwDNSResStaticHostRowStatus_Object((1,3,6,1,4,1,171,12,85,1,4,1,1,2),_SwDNSResStaticHostRowStatus_Type())
swDNSResStaticHostRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticHostRowStatus.setStatus(_A)
_SwDNSResStaticHostName_Type=DnsName
_SwDNSResStaticHostName_Object=MibTableColumn
swDNSResStaticHostName=_SwDNSResStaticHostName_Object((1,3,6,1,4,1,171,12,85,1,4,1,1,3),_SwDNSResStaticHostName_Type())
swDNSResStaticHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticHostName.setStatus(_A)
_SwDNSResStaticHostIPaddr_Type=IpAddress
_SwDNSResStaticHostIPaddr_Object=MibTableColumn
swDNSResStaticHostIPaddr=_SwDNSResStaticHostIPaddr_Object((1,3,6,1,4,1,171,12,85,1,4,1,1,4),_SwDNSResStaticHostIPaddr_Type())
swDNSResStaticHostIPaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticHostIPaddr.setStatus(_A)
_SwDNSResStaticHostIPv6addr_Type=Ipv6Address
_SwDNSResStaticHostIPv6addr_Object=MibTableColumn
swDNSResStaticHostIPv6addr=_SwDNSResStaticHostIPv6addr_Object((1,3,6,1,4,1,171,12,85,1,4,1,1,6),_SwDNSResStaticHostIPv6addr_Type())
swDNSResStaticHostIPv6addr.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResStaticHostIPv6addr.setStatus(_A)
class _SwDNSResStaticHostIPv6IntfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwDNSResStaticHostIPv6IntfName_Type.__name__=_H
_SwDNSResStaticHostIPv6IntfName_Object=MibTableColumn
swDNSResStaticHostIPv6IntfName=_SwDNSResStaticHostIPv6IntfName_Object((1,3,6,1,4,1,171,12,85,1,4,1,1,7),_SwDNSResStaticHostIPv6IntfName_Type())
swDNSResStaticHostIPv6IntfName.setMaxAccess(_D)
if mibBuilder.loadTexts:swDNSResStaticHostIPv6IntfName.setStatus(_A)
_SwDNSResDynamicHostTable_Object=MibTable
swDNSResDynamicHostTable=_SwDNSResDynamicHostTable_Object((1,3,6,1,4,1,171,12,85,1,4,2))
if mibBuilder.loadTexts:swDNSResDynamicHostTable.setStatus(_A)
_SwDNSResDynamicHostEntry_Object=MibTableRow
swDNSResDynamicHostEntry=_SwDNSResDynamicHostEntry_Object((1,3,6,1,4,1,171,12,85,1,4,2,1))
swDNSResDynamicHostEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:swDNSResDynamicHostEntry.setStatus(_A)
_SwDNSResDynamicHostIndex_Type=Integer32
_SwDNSResDynamicHostIndex_Object=MibTableColumn
swDNSResDynamicHostIndex=_SwDNSResDynamicHostIndex_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,1),_SwDNSResDynamicHostIndex_Type())
swDNSResDynamicHostIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swDNSResDynamicHostIndex.setStatus(_A)
_SwDNSResDynamicHostName_Type=DnsName
_SwDNSResDynamicHostName_Object=MibTableColumn
swDNSResDynamicHostName=_SwDNSResDynamicHostName_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,2),_SwDNSResDynamicHostName_Type())
swDNSResDynamicHostName.setMaxAccess(_G)
if mibBuilder.loadTexts:swDNSResDynamicHostName.setStatus(_A)
_SwDNSResDynamicHostIPaddr_Type=IpAddress
_SwDNSResDynamicHostIPaddr_Object=MibTableColumn
swDNSResDynamicHostIPaddr=_SwDNSResDynamicHostIPaddr_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,3),_SwDNSResDynamicHostIPaddr_Type())
swDNSResDynamicHostIPaddr.setMaxAccess(_G)
if mibBuilder.loadTexts:swDNSResDynamicHostIPaddr.setStatus(_A)
_SwDNSResDynamicHostTTL_Type=DnsTime
_SwDNSResDynamicHostTTL_Object=MibTableColumn
swDNSResDynamicHostTTL=_SwDNSResDynamicHostTTL_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,4),_SwDNSResDynamicHostTTL_Type())
swDNSResDynamicHostTTL.setMaxAccess(_G)
if mibBuilder.loadTexts:swDNSResDynamicHostTTL.setStatus(_A)
class _SwDNSResDynamicHostClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('start',2)))
_SwDNSResDynamicHostClearCtrl_Type.__name__=_C
_SwDNSResDynamicHostClearCtrl_Object=MibTableColumn
swDNSResDynamicHostClearCtrl=_SwDNSResDynamicHostClearCtrl_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,5),_SwDNSResDynamicHostClearCtrl_Type())
swDNSResDynamicHostClearCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swDNSResDynamicHostClearCtrl.setStatus(_A)
_SwDNSResDynamicHostIPv6addr_Type=Ipv6Address
_SwDNSResDynamicHostIPv6addr_Object=MibTableColumn
swDNSResDynamicHostIPv6addr=_SwDNSResDynamicHostIPv6addr_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,7),_SwDNSResDynamicHostIPv6addr_Type())
swDNSResDynamicHostIPv6addr.setMaxAccess(_B)
if mibBuilder.loadTexts:swDNSResDynamicHostIPv6addr.setStatus(_A)
class _SwDNSResDynamicHostIPv6IntfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwDNSResDynamicHostIPv6IntfName_Type.__name__=_H
_SwDNSResDynamicHostIPv6IntfName_Object=MibTableColumn
swDNSResDynamicHostIPv6IntfName=_SwDNSResDynamicHostIPv6IntfName_Object((1,3,6,1,4,1,171,12,85,1,4,2,1,8),_SwDNSResDynamicHostIPv6IntfName_Type())
swDNSResDynamicHostIPv6IntfName.setMaxAccess(_D)
if mibBuilder.loadTexts:swDNSResDynamicHostIPv6IntfName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'DnsName':DnsName,'DnsTime':DnsTime,'swDNSResolverMIB':swDNSResolverMIB,'swDNSResolverMIBObjects':swDNSResolverMIBObjects,'swDNSResState':swDNSResState,'swDNSResNameSrvTimeOut':swDNSResNameSrvTimeOut,'swDNSResNameSrv':swDNSResNameSrv,'swDNSResStaticNameSrvTable':swDNSResStaticNameSrvTable,'swDNSResStaticNameSrvEntry':swDNSResStaticNameSrvEntry,_K:swDNSResStaticNameSrvIndex,'swDNSResStaticNameSrvRowStatus':swDNSResStaticNameSrvRowStatus,'swDNSResStaticNameSrvIPaddr':swDNSResStaticNameSrvIPaddr,'swDNSResStaticNameSrvPriority':swDNSResStaticNameSrvPriority,'swDNSResDynamicNameSrvTable':swDNSResDynamicNameSrvTable,'swDNSResDynamicNameSrvEntry':swDNSResDynamicNameSrvEntry,_L:swDNSResDynamicNameSrvIndex,'swDNSResDynamicNameSrvIPaddr':swDNSResDynamicNameSrvIPaddr,'swDNSResDynamicNameSrvPriority':swDNSResDynamicNameSrvPriority,'swDNSResStaticIPv6NameSrvTable':swDNSResStaticIPv6NameSrvTable,'swDNSResStaticIPv6NameSrvEntry':swDNSResStaticIPv6NameSrvEntry,_M:swDNSResStaticIPv6NameSrvIndex,'swDNSResStaticIPv6NameSrvaddr':swDNSResStaticIPv6NameSrvaddr,'swDNSResStaticIPv6NameSrvIntfName':swDNSResStaticIPv6NameSrvIntfName,'swDNSResStaticIPv6NameSrvPriority':swDNSResStaticIPv6NameSrvPriority,'swDNSResStaticIPv6NameSrvRowStatus':swDNSResStaticIPv6NameSrvRowStatus,'swDNSResHost':swDNSResHost,'swDNSResStaticHostTable':swDNSResStaticHostTable,'swDNSResStaticHostEntry':swDNSResStaticHostEntry,_N:swDNSResStaticHostIndex,'swDNSResStaticHostRowStatus':swDNSResStaticHostRowStatus,'swDNSResStaticHostName':swDNSResStaticHostName,'swDNSResStaticHostIPaddr':swDNSResStaticHostIPaddr,'swDNSResStaticHostIPv6addr':swDNSResStaticHostIPv6addr,'swDNSResStaticHostIPv6IntfName':swDNSResStaticHostIPv6IntfName,'swDNSResDynamicHostTable':swDNSResDynamicHostTable,'swDNSResDynamicHostEntry':swDNSResDynamicHostEntry,_O:swDNSResDynamicHostIndex,'swDNSResDynamicHostName':swDNSResDynamicHostName,'swDNSResDynamicHostIPaddr':swDNSResDynamicHostIPaddr,'swDNSResDynamicHostTTL':swDNSResDynamicHostTTL,'swDNSResDynamicHostClearCtrl':swDNSResDynamicHostClearCtrl,'swDNSResDynamicHostIPv6addr':swDNSResDynamicHostIPv6addr,'swDNSResDynamicHostIPv6IntfName':swDNSResDynamicHostIPv6IntfName})