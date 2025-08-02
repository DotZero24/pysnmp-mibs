_Q='zxAnDrUserViewMac'
_P='zxAnDrVlanIntServIp'
_O='security'
_N='standard'
_M='zxAnDrOption60Srv'
_L='zxAnDrOption60Str'
_K='disable'
_J='enable'
_I='read-only'
_H='zxAnDrIntIndex'
_G='read-create'
_F='DisplayString'
_E='not-accessible'
_D='ZTE-AN-DHCP-RELAY-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnDhcpRelayMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,53))
_ZxAnDhcpRelayMIBNotifs_ObjectIdentity=ObjectIdentity
zxAnDhcpRelayMIBNotifs=_ZxAnDhcpRelayMIBNotifs_ObjectIdentity((1,3,6,1,4,1,3902,1015,53,0))
_ZxAnDhcpRelayMIBObjects_ObjectIdentity=ObjectIdentity
zxAnDhcpRelayMIBObjects=_ZxAnDhcpRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,53,1))
_ZxAnDrGlobal_ObjectIdentity=ObjectIdentity
zxAnDrGlobal=_ZxAnDrGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,53,1,1))
class _ZxAnDrDatabaseOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('read',1),('write',2)))
_ZxAnDrDatabaseOper_Type.__name__=_B
_ZxAnDrDatabaseOper_Object=MibScalar
zxAnDrDatabaseOper=_ZxAnDrDatabaseOper_Object((1,3,6,1,4,1,3902,1015,53,1,1,1),_ZxAnDrDatabaseOper_Type())
zxAnDrDatabaseOper.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrDatabaseOper.setStatus(_A)
class _ZxAnDrServMaxRetryTimes_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,1000))
_ZxAnDrServMaxRetryTimes_Type.__name__=_B
_ZxAnDrServMaxRetryTimes_Object=MibScalar
zxAnDrServMaxRetryTimes=_ZxAnDrServMaxRetryTimes_Object((1,3,6,1,4,1,3902,1015,53,1,1,2),_ZxAnDrServMaxRetryTimes_Type())
zxAnDrServMaxRetryTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrServMaxRetryTimes.setStatus(_A)
class _ZxAnDrUpdateArp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnDrUpdateArp_Type.__name__=_B
_ZxAnDrUpdateArp_Object=MibScalar
zxAnDrUpdateArp=_ZxAnDrUpdateArp_Object((1,3,6,1,4,1,3902,1015,53,1,1,3),_ZxAnDrUpdateArp_Type())
zxAnDrUpdateArp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrUpdateArp.setStatus(_A)
class _ZxAnDrProxyLeaseTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,18000))
_ZxAnDrProxyLeaseTime_Type.__name__=_B
_ZxAnDrProxyLeaseTime_Object=MibScalar
zxAnDrProxyLeaseTime=_ZxAnDrProxyLeaseTime_Object((1,3,6,1,4,1,3902,1015,53,1,1,4),_ZxAnDrProxyLeaseTime_Type())
zxAnDrProxyLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrProxyLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnDrProxyLeaseTime.setUnits('seconds')
class _ZxAnDrForwardMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allSimultaneously',1),('roundRobin',2)))
_ZxAnDrForwardMode_Type.__name__=_B
_ZxAnDrForwardMode_Object=MibScalar
zxAnDrForwardMode=_ZxAnDrForwardMode_Object((1,3,6,1,4,1,3902,1015,53,1,1,5),_ZxAnDrForwardMode_Type())
zxAnDrForwardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrForwardMode.setStatus(_A)
class _ZxAnDrCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnDrCos_Type.__name__=_B
_ZxAnDrCos_Object=MibScalar
zxAnDrCos=_ZxAnDrCos_Object((1,3,6,1,4,1,3902,1015,53,1,1,6),_ZxAnDrCos_Type())
zxAnDrCos.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrCos.setStatus(_A)
_ZxAnDrOption60_ObjectIdentity=ObjectIdentity
zxAnDrOption60=_ZxAnDrOption60_ObjectIdentity((1,3,6,1,4,1,3902,1015,53,1,2))
_ZxAnDrOption60Table_Object=MibTable
zxAnDrOption60Table=_ZxAnDrOption60Table_Object((1,3,6,1,4,1,3902,1015,53,1,2,1))
if mibBuilder.loadTexts:zxAnDrOption60Table.setStatus(_A)
_ZxAnDrOption60Entry_Object=MibTableRow
zxAnDrOption60Entry=_ZxAnDrOption60Entry_Object((1,3,6,1,4,1,3902,1015,53,1,2,1,1))
zxAnDrOption60Entry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:zxAnDrOption60Entry.setStatus(_A)
class _ZxAnDrOption60Str_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_ZxAnDrOption60Str_Type.__name__=_F
_ZxAnDrOption60Str_Object=MibTableColumn
zxAnDrOption60Str=_ZxAnDrOption60Str_Object((1,3,6,1,4,1,3902,1015,53,1,2,1,1,1),_ZxAnDrOption60Str_Type())
zxAnDrOption60Str.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDrOption60Str.setStatus(_A)
_ZxAnDrOption60Srv_Type=IpAddress
_ZxAnDrOption60Srv_Object=MibTableColumn
zxAnDrOption60Srv=_ZxAnDrOption60Srv_Object((1,3,6,1,4,1,3902,1015,53,1,2,1,1,2),_ZxAnDrOption60Srv_Type())
zxAnDrOption60Srv.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDrOption60Srv.setStatus(_A)
class _ZxAnDrOption60Frd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('smart',0),(_N,1),(_O,2)))
_ZxAnDrOption60Frd_Type.__name__=_B
_ZxAnDrOption60Frd_Object=MibTableColumn
zxAnDrOption60Frd=_ZxAnDrOption60Frd_Object((1,3,6,1,4,1,3902,1015,53,1,2,1,1,3),_ZxAnDrOption60Frd_Type())
zxAnDrOption60Frd.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDrOption60Frd.setStatus(_A)
_ZxAnDrOption60Row_Type=RowStatus
_ZxAnDrOption60Row_Object=MibTableColumn
zxAnDrOption60Row=_ZxAnDrOption60Row_Object((1,3,6,1,4,1,3902,1015,53,1,2,1,1,4),_ZxAnDrOption60Row_Type())
zxAnDrOption60Row.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDrOption60Row.setStatus(_A)
_ZxAnDrVlanInterface_ObjectIdentity=ObjectIdentity
zxAnDrVlanInterface=_ZxAnDrVlanInterface_ObjectIdentity((1,3,6,1,4,1,3902,1015,53,1,3))
_ZxAnDrVlanIntTable_Object=MibTable
zxAnDrVlanIntTable=_ZxAnDrVlanIntTable_Object((1,3,6,1,4,1,3902,1015,53,1,3,1))
if mibBuilder.loadTexts:zxAnDrVlanIntTable.setStatus(_A)
_ZxAnDrVlanIntEntry_Object=MibTableRow
zxAnDrVlanIntEntry=_ZxAnDrVlanIntEntry_Object((1,3,6,1,4,1,3902,1015,53,1,3,1,1))
zxAnDrVlanIntEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:zxAnDrVlanIntEntry.setStatus(_A)
_ZxAnDrIntIndex_Type=ZxAnIfindex
_ZxAnDrIntIndex_Object=MibTableColumn
zxAnDrIntIndex=_ZxAnDrIntIndex_Object((1,3,6,1,4,1,3902,1015,53,1,3,1,1,1),_ZxAnDrIntIndex_Type())
zxAnDrIntIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDrIntIndex.setStatus(_A)
class _ZxAnDrOption60Oper_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ZxAnDrOption60Oper_Type.__name__=_B
_ZxAnDrOption60Oper_Object=MibTableColumn
zxAnDrOption60Oper=_ZxAnDrOption60Oper_Object((1,3,6,1,4,1,3902,1015,53,1,3,1,1,2),_ZxAnDrOption60Oper_Type())
zxAnDrOption60Oper.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrOption60Oper.setStatus(_A)
_ZxAnDrAgentIp_Type=IpAddress
_ZxAnDrAgentIp_Object=MibTableColumn
zxAnDrAgentIp=_ZxAnDrAgentIp_Object((1,3,6,1,4,1,3902,1015,53,1,3,1,1,3),_ZxAnDrAgentIp_Type())
zxAnDrAgentIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDrAgentIp.setStatus(_A)
_ZxAnDrVlanIntServTable_Object=MibTable
zxAnDrVlanIntServTable=_ZxAnDrVlanIntServTable_Object((1,3,6,1,4,1,3902,1015,53,1,3,2))
if mibBuilder.loadTexts:zxAnDrVlanIntServTable.setStatus(_A)
_ZxAnDrVlanIntServEntry_Object=MibTableRow
zxAnDrVlanIntServEntry=_ZxAnDrVlanIntServEntry_Object((1,3,6,1,4,1,3902,1015,53,1,3,2,1))
zxAnDrVlanIntServEntry.setIndexNames((0,_D,_H),(0,_D,_P))
if mibBuilder.loadTexts:zxAnDrVlanIntServEntry.setStatus(_A)
_ZxAnDrVlanIntServIp_Type=IpAddress
_ZxAnDrVlanIntServIp_Object=MibTableColumn
zxAnDrVlanIntServIp=_ZxAnDrVlanIntServIp_Object((1,3,6,1,4,1,3902,1015,53,1,3,2,1,1),_ZxAnDrVlanIntServIp_Type())
zxAnDrVlanIntServIp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDrVlanIntServIp.setStatus(_A)
class _ZxAnDrVlanIntServFrd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('smart',0),(_N,1),(_O,2)))
_ZxAnDrVlanIntServFrd_Type.__name__=_B
_ZxAnDrVlanIntServFrd_Object=MibTableColumn
zxAnDrVlanIntServFrd=_ZxAnDrVlanIntServFrd_Object((1,3,6,1,4,1,3902,1015,53,1,3,2,1,2),_ZxAnDrVlanIntServFrd_Type())
zxAnDrVlanIntServFrd.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDrVlanIntServFrd.setStatus(_A)
_ZxAnDrVlanIntServRow_Type=RowStatus
_ZxAnDrVlanIntServRow_Object=MibTableColumn
zxAnDrVlanIntServRow=_ZxAnDrVlanIntServRow_Object((1,3,6,1,4,1,3902,1015,53,1,3,2,1,3),_ZxAnDrVlanIntServRow_Type())
zxAnDrVlanIntServRow.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDrVlanIntServRow.setStatus(_A)
_ZxAnDrShowUsers_ObjectIdentity=ObjectIdentity
zxAnDrShowUsers=_ZxAnDrShowUsers_ObjectIdentity((1,3,6,1,4,1,3902,1015,53,1,4))
_ZxAnDrUserViewTable_Object=MibTable
zxAnDrUserViewTable=_ZxAnDrUserViewTable_Object((1,3,6,1,4,1,3902,1015,53,1,4,1))
if mibBuilder.loadTexts:zxAnDrUserViewTable.setStatus(_A)
_ZxAnDrUserViewEntry_Object=MibTableRow
zxAnDrUserViewEntry=_ZxAnDrUserViewEntry_Object((1,3,6,1,4,1,3902,1015,53,1,4,1,1))
zxAnDrUserViewEntry.setIndexNames((0,_D,_H),(0,_D,_Q))
if mibBuilder.loadTexts:zxAnDrUserViewEntry.setStatus(_A)
_ZxAnDrUserViewMac_Type=MacAddress
_ZxAnDrUserViewMac_Object=MibTableColumn
zxAnDrUserViewMac=_ZxAnDrUserViewMac_Object((1,3,6,1,4,1,3902,1015,53,1,4,1,1,1),_ZxAnDrUserViewMac_Type())
zxAnDrUserViewMac.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDrUserViewMac.setStatus(_A)
_ZxAnDrUserViewIp_Type=IpAddress
_ZxAnDrUserViewIp_Object=MibTableColumn
zxAnDrUserViewIp=_ZxAnDrUserViewIp_Object((1,3,6,1,4,1,3902,1015,53,1,4,1,1,2),_ZxAnDrUserViewIp_Type())
zxAnDrUserViewIp.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnDrUserViewIp.setStatus(_A)
class _ZxAnDrUserViewState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_ZxAnDrUserViewState_Type.__name__=_F
_ZxAnDrUserViewState_Object=MibTableColumn
zxAnDrUserViewState=_ZxAnDrUserViewState_Object((1,3,6,1,4,1,3902,1015,53,1,4,1,1,3),_ZxAnDrUserViewState_Type())
zxAnDrUserViewState.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnDrUserViewState.setStatus(_A)
class _ZxAnDrUserViewTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_ZxAnDrUserViewTime_Type.__name__=_F
_ZxAnDrUserViewTime_Object=MibTableColumn
zxAnDrUserViewTime=_ZxAnDrUserViewTime_Object((1,3,6,1,4,1,3902,1015,53,1,4,1,1,4),_ZxAnDrUserViewTime_Type())
zxAnDrUserViewTime.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnDrUserViewTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zxAnDhcpRelayMIB':zxAnDhcpRelayMIB,'zxAnDhcpRelayMIBNotifs':zxAnDhcpRelayMIBNotifs,'zxAnDhcpRelayMIBObjects':zxAnDhcpRelayMIBObjects,'zxAnDrGlobal':zxAnDrGlobal,'zxAnDrDatabaseOper':zxAnDrDatabaseOper,'zxAnDrServMaxRetryTimes':zxAnDrServMaxRetryTimes,'zxAnDrUpdateArp':zxAnDrUpdateArp,'zxAnDrProxyLeaseTime':zxAnDrProxyLeaseTime,'zxAnDrForwardMode':zxAnDrForwardMode,'zxAnDrCos':zxAnDrCos,'zxAnDrOption60':zxAnDrOption60,'zxAnDrOption60Table':zxAnDrOption60Table,'zxAnDrOption60Entry':zxAnDrOption60Entry,_L:zxAnDrOption60Str,_M:zxAnDrOption60Srv,'zxAnDrOption60Frd':zxAnDrOption60Frd,'zxAnDrOption60Row':zxAnDrOption60Row,'zxAnDrVlanInterface':zxAnDrVlanInterface,'zxAnDrVlanIntTable':zxAnDrVlanIntTable,'zxAnDrVlanIntEntry':zxAnDrVlanIntEntry,_H:zxAnDrIntIndex,'zxAnDrOption60Oper':zxAnDrOption60Oper,'zxAnDrAgentIp':zxAnDrAgentIp,'zxAnDrVlanIntServTable':zxAnDrVlanIntServTable,'zxAnDrVlanIntServEntry':zxAnDrVlanIntServEntry,_P:zxAnDrVlanIntServIp,'zxAnDrVlanIntServFrd':zxAnDrVlanIntServFrd,'zxAnDrVlanIntServRow':zxAnDrVlanIntServRow,'zxAnDrShowUsers':zxAnDrShowUsers,'zxAnDrUserViewTable':zxAnDrUserViewTable,'zxAnDrUserViewEntry':zxAnDrUserViewEntry,_Q:zxAnDrUserViewMac,'zxAnDrUserViewIp':zxAnDrUserViewIp,'zxAnDrUserViewState':zxAnDrUserViewState,'zxAnDrUserViewTime':zxAnDrUserViewTime})