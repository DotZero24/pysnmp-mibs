_M='zxAnPortIdDhcpVmacVid'
_L='zxAnPortIdDhcpVmacIfIndex'
_K='zxAnDhcpv6PortLocatingDhcpIndex'
_J='discard'
_I='replace'
_H='zxAnPortLocatingDhcpIndex'
_G='not-accessible'
_F='ZTE-AN-DHCP-MIB'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxAnPortLocatingMib,=mibBuilder.importSymbols('ZTE-AN-PORT-LOCATING-MIB','zxAnPortLocatingMib')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnDhcpMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,32,21))
class _ZxAnDhcpV4L2RAEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDhcpV4L2RAEnable_Type.__name__=_B
_ZxAnDhcpV4L2RAEnable_Object=MibScalar
zxAnDhcpV4L2RAEnable=_ZxAnDhcpV4L2RAEnable_Object((1,3,6,1,4,1,3902,1015,32,21,1),_ZxAnDhcpV4L2RAEnable_Type())
zxAnDhcpV4L2RAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV4L2RAEnable.setStatus(_A)
class _ZxAnPortLocatingDhcp128Enable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnPortLocatingDhcp128Enable_Type.__name__=_B
_ZxAnPortLocatingDhcp128Enable_Object=MibScalar
zxAnPortLocatingDhcp128Enable=_ZxAnPortLocatingDhcp128Enable_Object((1,3,6,1,4,1,3902,1015,32,21,2),_ZxAnPortLocatingDhcp128Enable_Type())
zxAnPortLocatingDhcp128Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingDhcp128Enable.setStatus(_A)
class _ZxAnDhcpV6L2RAEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDhcpV6L2RAEnable_Type.__name__=_B
_ZxAnDhcpV6L2RAEnable_Object=MibScalar
zxAnDhcpV6L2RAEnable=_ZxAnDhcpV6L2RAEnable_Object((1,3,6,1,4,1,3902,1015,32,21,3),_ZxAnDhcpV6L2RAEnable_Type())
zxAnDhcpV6L2RAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV6L2RAEnable.setStatus(_A)
class _ZxAnPortLocatingDhcpVmacEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnPortLocatingDhcpVmacEnable_Type.__name__=_B
_ZxAnPortLocatingDhcpVmacEnable_Object=MibScalar
zxAnPortLocatingDhcpVmacEnable=_ZxAnPortLocatingDhcpVmacEnable_Object((1,3,6,1,4,1,3902,1015,32,21,4),_ZxAnPortLocatingDhcpVmacEnable_Type())
zxAnPortLocatingDhcpVmacEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingDhcpVmacEnable.setStatus(_A)
class _ZxAnDhcpv6PortLocatingWorkMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcMode',1),('layer2Mode',2),('layer3Mode',3)))
_ZxAnDhcpv6PortLocatingWorkMode_Type.__name__=_B
_ZxAnDhcpv6PortLocatingWorkMode_Object=MibScalar
zxAnDhcpv6PortLocatingWorkMode=_ZxAnDhcpv6PortLocatingWorkMode_Object((1,3,6,1,4,1,3902,1015,32,21,5),_ZxAnDhcpv6PortLocatingWorkMode_Type())
zxAnDhcpv6PortLocatingWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpv6PortLocatingWorkMode.setStatus(_A)
_ZxAnPortLocatingDhcpTable_Object=MibTable
zxAnPortLocatingDhcpTable=_ZxAnPortLocatingDhcpTable_Object((1,3,6,1,4,1,3902,1015,32,21,20))
if mibBuilder.loadTexts:zxAnPortLocatingDhcpTable.setStatus(_A)
_ZxAnPortLocatingDhcpEntry_Object=MibTableRow
zxAnPortLocatingDhcpEntry=_ZxAnPortLocatingDhcpEntry_Object((1,3,6,1,4,1,3902,1015,32,21,20,1))
zxAnPortLocatingDhcpEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zxAnPortLocatingDhcpEntry.setStatus(_A)
_ZxAnPortLocatingDhcpIndex_Type=ZxAnIfindex
_ZxAnPortLocatingDhcpIndex_Object=MibTableColumn
zxAnPortLocatingDhcpIndex=_ZxAnPortLocatingDhcpIndex_Object((1,3,6,1,4,1,3902,1015,32,21,20,1,1),_ZxAnPortLocatingDhcpIndex_Type())
zxAnPortLocatingDhcpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPortLocatingDhcpIndex.setStatus(_A)
class _ZxAnDhcpV4L2RAIfConfEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDhcpV4L2RAIfConfEnable_Type.__name__=_B
_ZxAnDhcpV4L2RAIfConfEnable_Object=MibTableColumn
zxAnDhcpV4L2RAIfConfEnable=_ZxAnDhcpV4L2RAIfConfEnable_Object((1,3,6,1,4,1,3902,1015,32,21,20,1,2),_ZxAnDhcpV4L2RAIfConfEnable_Type())
zxAnDhcpV4L2RAIfConfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV4L2RAIfConfEnable.setStatus(_A)
class _ZxAnPortLocatingPortDhcp128Enable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnPortLocatingPortDhcp128Enable_Type.__name__=_B
_ZxAnPortLocatingPortDhcp128Enable_Object=MibTableColumn
zxAnPortLocatingPortDhcp128Enable=_ZxAnPortLocatingPortDhcp128Enable_Object((1,3,6,1,4,1,3902,1015,32,21,20,1,3),_ZxAnPortLocatingPortDhcp128Enable_Type())
zxAnPortLocatingPortDhcp128Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingPortDhcp128Enable.setStatus(_A)
class _ZxAnDhcpV4L2RAIfConfTrust_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ZxAnDhcpV4L2RAIfConfTrust_Type.__name__=_B
_ZxAnDhcpV4L2RAIfConfTrust_Object=MibTableColumn
zxAnDhcpV4L2RAIfConfTrust=_ZxAnDhcpV4L2RAIfConfTrust_Object((1,3,6,1,4,1,3902,1015,32,21,20,1,4),_ZxAnDhcpV4L2RAIfConfTrust_Type())
zxAnDhcpV4L2RAIfConfTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV4L2RAIfConfTrust.setStatus(_A)
class _ZxAnDhcpV4L2RAIfConfPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('keep',1),(_I,2),(_J,3),('add',4)))
_ZxAnDhcpV4L2RAIfConfPolicy_Type.__name__=_B
_ZxAnDhcpV4L2RAIfConfPolicy_Object=MibTableColumn
zxAnDhcpV4L2RAIfConfPolicy=_ZxAnDhcpV4L2RAIfConfPolicy_Object((1,3,6,1,4,1,3902,1015,32,21,20,1,5),_ZxAnDhcpV4L2RAIfConfPolicy_Type())
zxAnDhcpV4L2RAIfConfPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV4L2RAIfConfPolicy.setStatus(_A)
class _ZxAnPortLocatingPortDhcpSnoopEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnPortLocatingPortDhcpSnoopEnable_Type.__name__=_B
_ZxAnPortLocatingPortDhcpSnoopEnable_Object=MibTableColumn
zxAnPortLocatingPortDhcpSnoopEnable=_ZxAnPortLocatingPortDhcpSnoopEnable_Object((1,3,6,1,4,1,3902,1015,32,21,20,1,6),_ZxAnPortLocatingPortDhcpSnoopEnable_Type())
zxAnPortLocatingPortDhcpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPortLocatingPortDhcpSnoopEnable.setStatus(_A)
_ZxAnDhcpv6PortLocatingDhcpTable_Object=MibTable
zxAnDhcpv6PortLocatingDhcpTable=_ZxAnDhcpv6PortLocatingDhcpTable_Object((1,3,6,1,4,1,3902,1015,32,21,21))
if mibBuilder.loadTexts:zxAnDhcpv6PortLocatingDhcpTable.setStatus(_A)
_ZxAnDhcpv6PortLocatingDhcpEntry_Object=MibTableRow
zxAnDhcpv6PortLocatingDhcpEntry=_ZxAnDhcpv6PortLocatingDhcpEntry_Object((1,3,6,1,4,1,3902,1015,32,21,21,1))
zxAnDhcpv6PortLocatingDhcpEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:zxAnDhcpv6PortLocatingDhcpEntry.setStatus(_A)
_ZxAnDhcpv6PortLocatingDhcpIndex_Type=ZxAnIfindex
_ZxAnDhcpv6PortLocatingDhcpIndex_Object=MibTableColumn
zxAnDhcpv6PortLocatingDhcpIndex=_ZxAnDhcpv6PortLocatingDhcpIndex_Object((1,3,6,1,4,1,3902,1015,32,21,21,1,1),_ZxAnDhcpv6PortLocatingDhcpIndex_Type())
zxAnDhcpv6PortLocatingDhcpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDhcpv6PortLocatingDhcpIndex.setStatus(_A)
class _ZxAnDhcpV6L2RAIfConfEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDhcpV6L2RAIfConfEnable_Type.__name__=_B
_ZxAnDhcpV6L2RAIfConfEnable_Object=MibTableColumn
zxAnDhcpV6L2RAIfConfEnable=_ZxAnDhcpV6L2RAIfConfEnable_Object((1,3,6,1,4,1,3902,1015,32,21,21,1,2),_ZxAnDhcpV6L2RAIfConfEnable_Type())
zxAnDhcpV6L2RAIfConfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV6L2RAIfConfEnable.setStatus(_A)
class _ZxAnDhcpV6L2RAIfConfTrust_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ZxAnDhcpV6L2RAIfConfTrust_Type.__name__=_B
_ZxAnDhcpV6L2RAIfConfTrust_Object=MibTableColumn
zxAnDhcpV6L2RAIfConfTrust=_ZxAnDhcpV6L2RAIfConfTrust_Object((1,3,6,1,4,1,3902,1015,32,21,21,1,3),_ZxAnDhcpV6L2RAIfConfTrust_Type())
zxAnDhcpV6L2RAIfConfTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV6L2RAIfConfTrust.setStatus(_A)
class _ZxAnDhcpV6L2RAIfConfPolicy_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('keep',1),(_I,2),(_J,3),('add',4)))
_ZxAnDhcpV6L2RAIfConfPolicy_Type.__name__=_B
_ZxAnDhcpV6L2RAIfConfPolicy_Object=MibTableColumn
zxAnDhcpV6L2RAIfConfPolicy=_ZxAnDhcpV6L2RAIfConfPolicy_Object((1,3,6,1,4,1,3902,1015,32,21,21,1,4),_ZxAnDhcpV6L2RAIfConfPolicy_Type())
zxAnDhcpV6L2RAIfConfPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpV6L2RAIfConfPolicy.setStatus(_A)
class _ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Type.__name__=_B
_ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Object=MibTableColumn
zxAnDhcpv6PortLocatingPortDhcpSnoopEnable=_ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Object((1,3,6,1,4,1,3902,1015,32,21,21,1,5),_ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Type())
zxAnDhcpv6PortLocatingPortDhcpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDhcpv6PortLocatingPortDhcpSnoopEnable.setStatus(_A)
_ZxAnPortIdDhcpVmacTable_Object=MibTable
zxAnPortIdDhcpVmacTable=_ZxAnPortIdDhcpVmacTable_Object((1,3,6,1,4,1,3902,1015,32,21,22))
if mibBuilder.loadTexts:zxAnPortIdDhcpVmacTable.setStatus(_A)
_ZxAnPortIdDhcpVmacEntry_Object=MibTableRow
zxAnPortIdDhcpVmacEntry=_ZxAnPortIdDhcpVmacEntry_Object((1,3,6,1,4,1,3902,1015,32,21,22,1))
zxAnPortIdDhcpVmacEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:zxAnPortIdDhcpVmacEntry.setStatus(_A)
_ZxAnPortIdDhcpVmacIfIndex_Type=ZxAnIfindex
_ZxAnPortIdDhcpVmacIfIndex_Object=MibTableColumn
zxAnPortIdDhcpVmacIfIndex=_ZxAnPortIdDhcpVmacIfIndex_Object((1,3,6,1,4,1,3902,1015,32,21,22,1,1),_ZxAnPortIdDhcpVmacIfIndex_Type())
zxAnPortIdDhcpVmacIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPortIdDhcpVmacIfIndex.setStatus(_A)
class _ZxAnPortIdDhcpVmacVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxAnPortIdDhcpVmacVid_Type.__name__=_B
_ZxAnPortIdDhcpVmacVid_Object=MibTableColumn
zxAnPortIdDhcpVmacVid=_ZxAnPortIdDhcpVmacVid_Object((1,3,6,1,4,1,3902,1015,32,21,22,1,2),_ZxAnPortIdDhcpVmacVid_Type())
zxAnPortIdDhcpVmacVid.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPortIdDhcpVmacVid.setStatus(_A)
_ZxAnPortIdDhcpVmacRowStatus_Type=RowStatus
_ZxAnPortIdDhcpVmacRowStatus_Object=MibTableColumn
zxAnPortIdDhcpVmacRowStatus=_ZxAnPortIdDhcpVmacRowStatus_Object((1,3,6,1,4,1,3902,1015,32,21,22,1,50),_ZxAnPortIdDhcpVmacRowStatus_Type())
zxAnPortIdDhcpVmacRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zxAnPortIdDhcpVmacRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zxAnDhcpMib':zxAnDhcpMib,'zxAnDhcpV4L2RAEnable':zxAnDhcpV4L2RAEnable,'zxAnPortLocatingDhcp128Enable':zxAnPortLocatingDhcp128Enable,'zxAnDhcpV6L2RAEnable':zxAnDhcpV6L2RAEnable,'zxAnPortLocatingDhcpVmacEnable':zxAnPortLocatingDhcpVmacEnable,'zxAnDhcpv6PortLocatingWorkMode':zxAnDhcpv6PortLocatingWorkMode,'zxAnPortLocatingDhcpTable':zxAnPortLocatingDhcpTable,'zxAnPortLocatingDhcpEntry':zxAnPortLocatingDhcpEntry,_H:zxAnPortLocatingDhcpIndex,'zxAnDhcpV4L2RAIfConfEnable':zxAnDhcpV4L2RAIfConfEnable,'zxAnPortLocatingPortDhcp128Enable':zxAnPortLocatingPortDhcp128Enable,'zxAnDhcpV4L2RAIfConfTrust':zxAnDhcpV4L2RAIfConfTrust,'zxAnDhcpV4L2RAIfConfPolicy':zxAnDhcpV4L2RAIfConfPolicy,'zxAnPortLocatingPortDhcpSnoopEnable':zxAnPortLocatingPortDhcpSnoopEnable,'zxAnDhcpv6PortLocatingDhcpTable':zxAnDhcpv6PortLocatingDhcpTable,'zxAnDhcpv6PortLocatingDhcpEntry':zxAnDhcpv6PortLocatingDhcpEntry,_K:zxAnDhcpv6PortLocatingDhcpIndex,'zxAnDhcpV6L2RAIfConfEnable':zxAnDhcpV6L2RAIfConfEnable,'zxAnDhcpV6L2RAIfConfTrust':zxAnDhcpV6L2RAIfConfTrust,'zxAnDhcpV6L2RAIfConfPolicy':zxAnDhcpV6L2RAIfConfPolicy,'zxAnDhcpv6PortLocatingPortDhcpSnoopEnable':zxAnDhcpv6PortLocatingPortDhcpSnoopEnable,'zxAnPortIdDhcpVmacTable':zxAnPortIdDhcpVmacTable,'zxAnPortIdDhcpVmacEntry':zxAnPortIdDhcpVmacEntry,_L:zxAnPortIdDhcpVmacIfIndex,_M:zxAnPortIdDhcpVmacVid,'zxAnPortIdDhcpVmacRowStatus':zxAnPortIdDhcpVmacRowStatus})