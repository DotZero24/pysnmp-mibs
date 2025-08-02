_M='zxAnDvUserViewMac'
_L='zxAnDvGateway'
_K='zxAnDvBeginIp'
_J='zxAnDvIpPoolName'
_I='read-only'
_H='Integer32'
_G='zxAnDvIntIndex'
_F='read-create'
_E='not-accessible'
_D='read-write'
_C='DisplayString'
_B='ZTE-AN-DHCP-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnDhcpServerMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,54))
if mibBuilder.loadTexts:zxAnDhcpServerMIB.setRevisions(('2006-12-11 00:00',))
_ZxAnDhcpServerMIBNotifs_ObjectIdentity=ObjectIdentity
zxAnDhcpServerMIBNotifs=_ZxAnDhcpServerMIBNotifs_ObjectIdentity((1,3,6,1,4,1,3902,1015,54,0))
_ZxAnDhcpServerMIBObjects_ObjectIdentity=ObjectIdentity
zxAnDhcpServerMIBObjects=_ZxAnDhcpServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,54,1))
_ZxAnDvGlobal_ObjectIdentity=ObjectIdentity
zxAnDvGlobal=_ZxAnDvGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,54,1,1))
_ZxAnDvPrimaryDns_Type=IpAddress
_ZxAnDvPrimaryDns_Object=MibScalar
zxAnDvPrimaryDns=_ZxAnDvPrimaryDns_Object((1,3,6,1,4,1,3902,1015,54,1,1,1),_ZxAnDvPrimaryDns_Type())
zxAnDvPrimaryDns.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDvPrimaryDns.setStatus(_A)
_ZxAnDvSecondDns_Type=IpAddress
_ZxAnDvSecondDns_Object=MibScalar
zxAnDvSecondDns=_ZxAnDvSecondDns_Object((1,3,6,1,4,1,3902,1015,54,1,1,2),_ZxAnDvSecondDns_Type())
zxAnDvSecondDns.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDvSecondDns.setStatus(_A)
class _ZxAnDvLeaseTime_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,18000))
_ZxAnDvLeaseTime_Type.__name__=_H
_ZxAnDvLeaseTime_Object=MibScalar
zxAnDvLeaseTime=_ZxAnDvLeaseTime_Object((1,3,6,1,4,1,3902,1015,54,1,1,3),_ZxAnDvLeaseTime_Type())
zxAnDvLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDvLeaseTime.setStatus(_A)
class _ZxAnDvUpdateArp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnDvUpdateArp_Type.__name__=_H
_ZxAnDvUpdateArp_Object=MibScalar
zxAnDvUpdateArp=_ZxAnDvUpdateArp_Object((1,3,6,1,4,1,3902,1015,54,1,1,4),_ZxAnDvUpdateArp_Type())
zxAnDvUpdateArp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDvUpdateArp.setStatus(_A)
_ZxAnDvIpPool_ObjectIdentity=ObjectIdentity
zxAnDvIpPool=_ZxAnDvIpPool_ObjectIdentity((1,3,6,1,4,1,3902,1015,54,1,2))
_ZxAnDvIpPoolTable_Object=MibTable
zxAnDvIpPoolTable=_ZxAnDvIpPoolTable_Object((1,3,6,1,4,1,3902,1015,54,1,2,1))
if mibBuilder.loadTexts:zxAnDvIpPoolTable.setStatus(_A)
_ZxAnDvIpPoolEntry_Object=MibTableRow
zxAnDvIpPoolEntry=_ZxAnDvIpPoolEntry_Object((1,3,6,1,4,1,3902,1015,54,1,2,1,1))
zxAnDvIpPoolEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:zxAnDvIpPoolEntry.setStatus(_A)
class _ZxAnDvIpPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnDvIpPoolName_Type.__name__=_C
_ZxAnDvIpPoolName_Object=MibTableColumn
zxAnDvIpPoolName=_ZxAnDvIpPoolName_Object((1,3,6,1,4,1,3902,1015,54,1,2,1,1,1),_ZxAnDvIpPoolName_Type())
zxAnDvIpPoolName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDvIpPoolName.setStatus(_A)
_ZxAnDvBeginIp_Type=IpAddress
_ZxAnDvBeginIp_Object=MibTableColumn
zxAnDvBeginIp=_ZxAnDvBeginIp_Object((1,3,6,1,4,1,3902,1015,54,1,2,1,1,2),_ZxAnDvBeginIp_Type())
zxAnDvBeginIp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDvBeginIp.setStatus(_A)
_ZxAnDvEndIp_Type=IpAddress
_ZxAnDvEndIp_Object=MibTableColumn
zxAnDvEndIp=_ZxAnDvEndIp_Object((1,3,6,1,4,1,3902,1015,54,1,2,1,1,3),_ZxAnDvEndIp_Type())
zxAnDvEndIp.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDvEndIp.setStatus(_A)
_ZxAnDvMask_Type=IpAddress
_ZxAnDvMask_Object=MibTableColumn
zxAnDvMask=_ZxAnDvMask_Object((1,3,6,1,4,1,3902,1015,54,1,2,1,1,4),_ZxAnDvMask_Type())
zxAnDvMask.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDvMask.setStatus(_A)
_ZxAnDvRow_Type=RowStatus
_ZxAnDvRow_Object=MibTableColumn
zxAnDvRow=_ZxAnDvRow_Object((1,3,6,1,4,1,3902,1015,54,1,2,1,1,5),_ZxAnDvRow_Type())
zxAnDvRow.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDvRow.setStatus(_A)
_ZxAnDvVlanInterface_ObjectIdentity=ObjectIdentity
zxAnDvVlanInterface=_ZxAnDvVlanInterface_ObjectIdentity((1,3,6,1,4,1,3902,1015,54,1,3))
_ZxAnDvVlanIntTable_Object=MibTable
zxAnDvVlanIntTable=_ZxAnDvVlanIntTable_Object((1,3,6,1,4,1,3902,1015,54,1,3,1))
if mibBuilder.loadTexts:zxAnDvVlanIntTable.setStatus(_A)
_ZxAnDvVlanIntEntry_Object=MibTableRow
zxAnDvVlanIntEntry=_ZxAnDvVlanIntEntry_Object((1,3,6,1,4,1,3902,1015,54,1,3,1,1))
zxAnDvVlanIntEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:zxAnDvVlanIntEntry.setStatus(_A)
_ZxAnDvIntIndex_Type=ZxAnIfindex
_ZxAnDvIntIndex_Object=MibTableColumn
zxAnDvIntIndex=_ZxAnDvIntIndex_Object((1,3,6,1,4,1,3902,1015,54,1,3,1,1,1),_ZxAnDvIntIndex_Type())
zxAnDvIntIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDvIntIndex.setStatus(_A)
class _ZxAnDvIntIpPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnDvIntIpPoolName_Type.__name__=_C
_ZxAnDvIntIpPoolName_Object=MibTableColumn
zxAnDvIntIpPoolName=_ZxAnDvIntIpPoolName_Object((1,3,6,1,4,1,3902,1015,54,1,3,1,1,2),_ZxAnDvIntIpPoolName_Type())
zxAnDvIntIpPoolName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDvIntIpPoolName.setStatus(_A)
_ZxAnDvVlanIntGateWayTable_Object=MibTable
zxAnDvVlanIntGateWayTable=_ZxAnDvVlanIntGateWayTable_Object((1,3,6,1,4,1,3902,1015,54,1,3,2))
if mibBuilder.loadTexts:zxAnDvVlanIntGateWayTable.setStatus(_A)
_ZxAnDvVlanIntGateWayEntry_Object=MibTableRow
zxAnDvVlanIntGateWayEntry=_ZxAnDvVlanIntGateWayEntry_Object((1,3,6,1,4,1,3902,1015,54,1,3,2,1))
zxAnDvVlanIntGateWayEntry.setIndexNames((0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:zxAnDvVlanIntGateWayEntry.setStatus(_A)
_ZxAnDvGateway_Type=IpAddress
_ZxAnDvGateway_Object=MibTableColumn
zxAnDvGateway=_ZxAnDvGateway_Object((1,3,6,1,4,1,3902,1015,54,1,3,2,1,1),_ZxAnDvGateway_Type())
zxAnDvGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDvGateway.setStatus(_A)
_ZxAnDvGatewayRow_Type=RowStatus
_ZxAnDvGatewayRow_Object=MibTableColumn
zxAnDvGatewayRow=_ZxAnDvGatewayRow_Object((1,3,6,1,4,1,3902,1015,54,1,3,2,1,2),_ZxAnDvGatewayRow_Type())
zxAnDvGatewayRow.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDvGatewayRow.setStatus(_A)
_ZxAnDvShowUsers_ObjectIdentity=ObjectIdentity
zxAnDvShowUsers=_ZxAnDvShowUsers_ObjectIdentity((1,3,6,1,4,1,3902,1015,54,1,4))
_ZxAnDvUserViewTable_Object=MibTable
zxAnDvUserViewTable=_ZxAnDvUserViewTable_Object((1,3,6,1,4,1,3902,1015,54,1,4,1))
if mibBuilder.loadTexts:zxAnDvUserViewTable.setStatus(_A)
_ZxAnDvUserViewEntry_Object=MibTableRow
zxAnDvUserViewEntry=_ZxAnDvUserViewEntry_Object((1,3,6,1,4,1,3902,1015,54,1,4,1,1))
zxAnDvUserViewEntry.setIndexNames((0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:zxAnDvUserViewEntry.setStatus(_A)
_ZxAnDvUserViewMac_Type=MacAddress
_ZxAnDvUserViewMac_Object=MibTableColumn
zxAnDvUserViewMac=_ZxAnDvUserViewMac_Object((1,3,6,1,4,1,3902,1015,54,1,4,1,1,1),_ZxAnDvUserViewMac_Type())
zxAnDvUserViewMac.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDvUserViewMac.setStatus(_A)
_ZxAnDvUserViewIp_Type=IpAddress
_ZxAnDvUserViewIp_Object=MibTableColumn
zxAnDvUserViewIp=_ZxAnDvUserViewIp_Object((1,3,6,1,4,1,3902,1015,54,1,4,1,1,2),_ZxAnDvUserViewIp_Type())
zxAnDvUserViewIp.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnDvUserViewIp.setStatus(_A)
class _ZxAnDvUserViewState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_ZxAnDvUserViewState_Type.__name__=_C
_ZxAnDvUserViewState_Object=MibTableColumn
zxAnDvUserViewState=_ZxAnDvUserViewState_Object((1,3,6,1,4,1,3902,1015,54,1,4,1,1,3),_ZxAnDvUserViewState_Type())
zxAnDvUserViewState.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnDvUserViewState.setStatus(_A)
class _ZxAnDvUserViewTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_ZxAnDvUserViewTime_Type.__name__=_C
_ZxAnDvUserViewTime_Object=MibTableColumn
zxAnDvUserViewTime=_ZxAnDvUserViewTime_Object((1,3,6,1,4,1,3902,1015,54,1,4,1,1,4),_ZxAnDvUserViewTime_Type())
zxAnDvUserViewTime.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnDvUserViewTime.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnDhcpServerMIB':zxAnDhcpServerMIB,'zxAnDhcpServerMIBNotifs':zxAnDhcpServerMIBNotifs,'zxAnDhcpServerMIBObjects':zxAnDhcpServerMIBObjects,'zxAnDvGlobal':zxAnDvGlobal,'zxAnDvPrimaryDns':zxAnDvPrimaryDns,'zxAnDvSecondDns':zxAnDvSecondDns,'zxAnDvLeaseTime':zxAnDvLeaseTime,'zxAnDvUpdateArp':zxAnDvUpdateArp,'zxAnDvIpPool':zxAnDvIpPool,'zxAnDvIpPoolTable':zxAnDvIpPoolTable,'zxAnDvIpPoolEntry':zxAnDvIpPoolEntry,_J:zxAnDvIpPoolName,_K:zxAnDvBeginIp,'zxAnDvEndIp':zxAnDvEndIp,'zxAnDvMask':zxAnDvMask,'zxAnDvRow':zxAnDvRow,'zxAnDvVlanInterface':zxAnDvVlanInterface,'zxAnDvVlanIntTable':zxAnDvVlanIntTable,'zxAnDvVlanIntEntry':zxAnDvVlanIntEntry,_G:zxAnDvIntIndex,'zxAnDvIntIpPoolName':zxAnDvIntIpPoolName,'zxAnDvVlanIntGateWayTable':zxAnDvVlanIntGateWayTable,'zxAnDvVlanIntGateWayEntry':zxAnDvVlanIntGateWayEntry,_L:zxAnDvGateway,'zxAnDvGatewayRow':zxAnDvGatewayRow,'zxAnDvShowUsers':zxAnDvShowUsers,'zxAnDvUserViewTable':zxAnDvUserViewTable,'zxAnDvUserViewEntry':zxAnDvUserViewEntry,_M:zxAnDvUserViewMac,'zxAnDvUserViewIp':zxAnDvUserViewIp,'zxAnDvUserViewState':zxAnDvUserViewState,'zxAnDvUserViewTime':zxAnDvUserViewTime})