_I='dhcpRelaySvrVlanIfaceNo'
_H='read-only'
_G='dhcpRelaySvrGroupNo'
_F='GBNL3DhcpRelay-MIB'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnL3,=mibBuilder.importSymbols('GREENTECH-MASTER-MIB','gbnL3')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL3DhcpRelay=ModuleIdentity((1,3,6,1,4,1,13464,1,2,5,5))
if mibBuilder.loadTexts:gbnL3DhcpRelay.setRevisions(('1901-05-03 00:00',))
class _DhcpRelayEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayEnableStatus_Type.__name__=_B
_DhcpRelayEnableStatus_Object=MibScalar
dhcpRelayEnableStatus=_DhcpRelayEnableStatus_Object((1,3,6,1,4,1,13464,1,2,5,5,1),_DhcpRelayEnableStatus_Type())
dhcpRelayEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayEnableStatus.setStatus(_A)
class _DhcpRelayDebugStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayDebugStatus_Type.__name__=_B
_DhcpRelayDebugStatus_Object=MibScalar
dhcpRelayDebugStatus=_DhcpRelayDebugStatus_Object((1,3,6,1,4,1,13464,1,2,5,5,2),_DhcpRelayDebugStatus_Type())
dhcpRelayDebugStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayDebugStatus.setStatus('obsolete')
_DhcpRelayGroupTable_Object=MibTable
dhcpRelayGroupTable=_DhcpRelayGroupTable_Object((1,3,6,1,4,1,13464,1,2,5,5,3))
if mibBuilder.loadTexts:dhcpRelayGroupTable.setStatus(_A)
_DhcpRelayGroupEntry_Object=MibTableRow
dhcpRelayGroupEntry=_DhcpRelayGroupEntry_Object((1,3,6,1,4,1,13464,1,2,5,5,3,1))
dhcpRelayGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dhcpRelayGroupEntry.setStatus(_A)
class _DhcpRelaySvrGroupNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DhcpRelaySvrGroupNo_Type.__name__=_B
_DhcpRelaySvrGroupNo_Object=MibTableColumn
dhcpRelaySvrGroupNo=_DhcpRelaySvrGroupNo_Object((1,3,6,1,4,1,13464,1,2,5,5,3,1,1),_DhcpRelaySvrGroupNo_Type())
dhcpRelaySvrGroupNo.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpRelaySvrGroupNo.setStatus(_A)
_DhcpRelayServerIp_Type=IpAddress
_DhcpRelayServerIp_Object=MibTableColumn
dhcpRelayServerIp=_DhcpRelayServerIp_Object((1,3,6,1,4,1,13464,1,2,5,5,3,1,2),_DhcpRelayServerIp_Type())
dhcpRelayServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerIp.setStatus(_A)
_DhcpRelayIfaceTable_Object=MibTable
dhcpRelayIfaceTable=_DhcpRelayIfaceTable_Object((1,3,6,1,4,1,13464,1,2,5,5,4))
if mibBuilder.loadTexts:dhcpRelayIfaceTable.setStatus(_A)
_DhcpRelayIfaceEntry_Object=MibTableRow
dhcpRelayIfaceEntry=_DhcpRelayIfaceEntry_Object((1,3,6,1,4,1,13464,1,2,5,5,4,1))
dhcpRelayIfaceEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:dhcpRelayIfaceEntry.setStatus(_A)
class _DhcpRelaySvrVlanIfaceNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DhcpRelaySvrVlanIfaceNo_Type.__name__=_B
_DhcpRelaySvrVlanIfaceNo_Object=MibTableColumn
dhcpRelaySvrVlanIfaceNo=_DhcpRelaySvrVlanIfaceNo_Object((1,3,6,1,4,1,13464,1,2,5,5,4,1,1),_DhcpRelaySvrVlanIfaceNo_Type())
dhcpRelaySvrVlanIfaceNo.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpRelaySvrVlanIfaceNo.setStatus(_A)
class _DhcpRelayVlanIfaceGroupNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DhcpRelayVlanIfaceGroupNo_Type.__name__=_B
_DhcpRelayVlanIfaceGroupNo_Object=MibTableColumn
dhcpRelayVlanIfaceGroupNo=_DhcpRelayVlanIfaceGroupNo_Object((1,3,6,1,4,1,13464,1,2,5,5,4,1,2),_DhcpRelayVlanIfaceGroupNo_Type())
dhcpRelayVlanIfaceGroupNo.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayVlanIfaceGroupNo.setStatus(_A)
class _DhcpRelayHideServerIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayHideServerIp_Type.__name__=_B
_DhcpRelayHideServerIp_Object=MibScalar
dhcpRelayHideServerIp=_DhcpRelayHideServerIp_Object((1,3,6,1,4,1,13464,1,2,5,5,5),_DhcpRelayHideServerIp_Type())
dhcpRelayHideServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayHideServerIp.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'gbnL3DhcpRelay':gbnL3DhcpRelay,'dhcpRelayEnableStatus':dhcpRelayEnableStatus,'dhcpRelayDebugStatus':dhcpRelayDebugStatus,'dhcpRelayGroupTable':dhcpRelayGroupTable,'dhcpRelayGroupEntry':dhcpRelayGroupEntry,_G:dhcpRelaySvrGroupNo,'dhcpRelayServerIp':dhcpRelayServerIp,'dhcpRelayIfaceTable':dhcpRelayIfaceTable,'dhcpRelayIfaceEntry':dhcpRelayIfaceEntry,_I:dhcpRelaySvrVlanIfaceNo,'dhcpRelayVlanIfaceGroupNo':dhcpRelayVlanIfaceGroupNo,'dhcpRelayHideServerIp':dhcpRelayHideServerIp})