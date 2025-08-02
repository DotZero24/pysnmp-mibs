_x='hpicfTrunkPortStatsGroup'
_w='hpicfTrunkStatsGroup'
_v='hpicfTrunkStatsClearGroup'
_u='hpicfLoadBalanceGroup5'
_t='hpicfLoadBalanceGroup'
_s='hpicfLoadBalanceStatus'
_r='hpicfLoadBalanceOutboundPort'
_q='hpicfLoadBalanceInboundPort'
_p='hpicfLoadBalanceInboundVlan'
_o='hpicfLoadBalanceEtherType'
_n='hpicfLoadBalanceDestPort'
_m='hpicfLoadBalanceSourcePort'
_l='hpicfLoadBalanceIPDestAddr'
_k='hpicfLoadBalanceIPDestAddrType'
_j='hpicfLoadBalanceIPSourceAddr'
_i='hpicfLoadBalanceIPSourceAddrType'
_h='hpicfLoadBalanceDestMacAddr'
_g='hpicfLoadBalanceSourceMacAddr'
_f='hpicfLoadBalanceTrunkId'
_e='hpicfTrunkPortDropTxFramePercent'
_d='hpicfTrunkPortTxFramePercent'
_c='hpicfTrunkPortRxFramePercent'
_b='hpicfTrunkPortFramesDropTx'
_a='hpicfTrunkPortFramesTx'
_Z='hpicfTrunkPortFramesRx'
_Y='hpicfTrunkPortBytesTx'
_X='hpicfTrunkPortBytesRx'
_W='hpicfTrunkTotalDropsTx'
_V='hpicfTrunkTotalFramesRx'
_U='hpicfTrunkTotalFramesTx'
_T='hpicfTrunkTotalBytesTx'
_S='hpicfTrunkTotalBytesRx'
_R='hpicfTrunkUpTime'
_Q='hpicfTrunkStatsClear'
_P='hpicfTrunkLoadBalanceMethod'
_O='hpicfLoadBalanceIndex'
_N='Percent'
_M='not-accessible'
_L='read-write'
_K='ifIndex'
_J='IF-MIB'
_I='InetAddress'
_H='Bytes'
_G='hpicfTrunkId'
_F='Integer32'
_E='Frames'
_D='read-create'
_C='read-only'
_B='HP-LOADBALANCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndex',_K)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfLoadBalanceMod=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76))
if mibBuilder.loadTexts:hpicfLoadBalanceMod.setRevisions(('2011-03-22 22:22','2010-06-22 22:22'))
_HpicfLoadBalanceNotifications_ObjectIdentity=ObjectIdentity
hpicfLoadBalanceNotifications=_HpicfLoadBalanceNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76,0))
_HpicfLoadBalanceMethodMod_ObjectIdentity=ObjectIdentity
hpicfLoadBalanceMethodMod=_HpicfLoadBalanceMethodMod_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76,1))
class _HpicfTrunkLoadBalanceMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l3based',1),('l4based',2),('l2based',3)))
_HpicfTrunkLoadBalanceMethod_Type.__name__=_F
_HpicfTrunkLoadBalanceMethod_Object=MibScalar
hpicfTrunkLoadBalanceMethod=_HpicfTrunkLoadBalanceMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,1),_HpicfTrunkLoadBalanceMethod_Type())
hpicfTrunkLoadBalanceMethod.setMaxAccess(_L)
if mibBuilder.loadTexts:hpicfTrunkLoadBalanceMethod.setStatus(_A)
_HpicfTrunkClearStatsTable_Object=MibTable
hpicfTrunkClearStatsTable=_HpicfTrunkClearStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,2))
if mibBuilder.loadTexts:hpicfTrunkClearStatsTable.setStatus(_A)
_HpicfTrunkClearStatsEntry_Object=MibTableRow
hpicfTrunkClearStatsEntry=_HpicfTrunkClearStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,2,1))
hpicfTrunkClearStatsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpicfTrunkClearStatsEntry.setStatus(_A)
class _HpicfTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfTrunkId_Type.__name__=_F
_HpicfTrunkId_Object=MibTableColumn
hpicfTrunkId=_HpicfTrunkId_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,2,1,1),_HpicfTrunkId_Type())
hpicfTrunkId.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfTrunkId.setStatus(_A)
_HpicfTrunkStatsClear_Type=TruthValue
_HpicfTrunkStatsClear_Object=MibTableColumn
hpicfTrunkStatsClear=_HpicfTrunkStatsClear_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,2,1,2),_HpicfTrunkStatsClear_Type())
hpicfTrunkStatsClear.setMaxAccess(_L)
if mibBuilder.loadTexts:hpicfTrunkStatsClear.setStatus(_A)
_HpicfTrunkStatsTable_Object=MibTable
hpicfTrunkStatsTable=_HpicfTrunkStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3))
if mibBuilder.loadTexts:hpicfTrunkStatsTable.setStatus(_A)
_HpicfTrunkStatsEntry_Object=MibTableRow
hpicfTrunkStatsEntry=_HpicfTrunkStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1))
hpicfTrunkStatsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpicfTrunkStatsEntry.setStatus(_A)
_HpicfTrunkUpTime_Type=Unsigned32
_HpicfTrunkUpTime_Object=MibTableColumn
hpicfTrunkUpTime=_HpicfTrunkUpTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1,1),_HpicfTrunkUpTime_Type())
hpicfTrunkUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkUpTime.setUnits('minutes')
_HpicfTrunkTotalBytesRx_Type=Counter64
_HpicfTrunkTotalBytesRx_Object=MibTableColumn
hpicfTrunkTotalBytesRx=_HpicfTrunkTotalBytesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1,2),_HpicfTrunkTotalBytesRx_Type())
hpicfTrunkTotalBytesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkTotalBytesRx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkTotalBytesRx.setUnits(_H)
_HpicfTrunkTotalBytesTx_Type=Counter64
_HpicfTrunkTotalBytesTx_Object=MibTableColumn
hpicfTrunkTotalBytesTx=_HpicfTrunkTotalBytesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1,3),_HpicfTrunkTotalBytesTx_Type())
hpicfTrunkTotalBytesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkTotalBytesTx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkTotalBytesTx.setUnits(_H)
_HpicfTrunkTotalFramesRx_Type=Counter64
_HpicfTrunkTotalFramesRx_Object=MibTableColumn
hpicfTrunkTotalFramesRx=_HpicfTrunkTotalFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1,4),_HpicfTrunkTotalFramesRx_Type())
hpicfTrunkTotalFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkTotalFramesRx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkTotalFramesRx.setUnits(_E)
_HpicfTrunkTotalFramesTx_Type=Counter64
_HpicfTrunkTotalFramesTx_Object=MibTableColumn
hpicfTrunkTotalFramesTx=_HpicfTrunkTotalFramesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1,5),_HpicfTrunkTotalFramesTx_Type())
hpicfTrunkTotalFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkTotalFramesTx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkTotalFramesTx.setUnits(_E)
_HpicfTrunkTotalDropsTx_Type=Counter64
_HpicfTrunkTotalDropsTx_Object=MibTableColumn
hpicfTrunkTotalDropsTx=_HpicfTrunkTotalDropsTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,3,1,6),_HpicfTrunkTotalDropsTx_Type())
hpicfTrunkTotalDropsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkTotalDropsTx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkTotalDropsTx.setUnits(_E)
_HpicfTrunkPortStatsTable_Object=MibTable
hpicfTrunkPortStatsTable=_HpicfTrunkPortStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4))
if mibBuilder.loadTexts:hpicfTrunkPortStatsTable.setStatus(_A)
_HpicfTrunkPortStatsEntry_Object=MibTableRow
hpicfTrunkPortStatsEntry=_HpicfTrunkPortStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1))
hpicfTrunkPortStatsEntry.setIndexNames((0,_B,_G),(0,_J,_K))
if mibBuilder.loadTexts:hpicfTrunkPortStatsEntry.setStatus(_A)
_HpicfTrunkPortBytesRx_Type=Counter64
_HpicfTrunkPortBytesRx_Object=MibTableColumn
hpicfTrunkPortBytesRx=_HpicfTrunkPortBytesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,1),_HpicfTrunkPortBytesRx_Type())
hpicfTrunkPortBytesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortBytesRx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortBytesRx.setUnits(_H)
_HpicfTrunkPortBytesTx_Type=Counter64
_HpicfTrunkPortBytesTx_Object=MibTableColumn
hpicfTrunkPortBytesTx=_HpicfTrunkPortBytesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,2),_HpicfTrunkPortBytesTx_Type())
hpicfTrunkPortBytesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortBytesTx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortBytesTx.setUnits(_H)
_HpicfTrunkPortFramesRx_Type=Counter64
_HpicfTrunkPortFramesRx_Object=MibTableColumn
hpicfTrunkPortFramesRx=_HpicfTrunkPortFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,3),_HpicfTrunkPortFramesRx_Type())
hpicfTrunkPortFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortFramesRx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortFramesRx.setUnits(_E)
_HpicfTrunkPortFramesTx_Type=Counter64
_HpicfTrunkPortFramesTx_Object=MibTableColumn
hpicfTrunkPortFramesTx=_HpicfTrunkPortFramesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,4),_HpicfTrunkPortFramesTx_Type())
hpicfTrunkPortFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortFramesTx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortFramesTx.setUnits(_E)
_HpicfTrunkPortFramesDropTx_Type=Counter64
_HpicfTrunkPortFramesDropTx_Object=MibTableColumn
hpicfTrunkPortFramesDropTx=_HpicfTrunkPortFramesDropTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,5),_HpicfTrunkPortFramesDropTx_Type())
hpicfTrunkPortFramesDropTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortFramesDropTx.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortFramesDropTx.setUnits(_E)
_HpicfTrunkPortRxFramePercent_Type=Unsigned32
_HpicfTrunkPortRxFramePercent_Object=MibTableColumn
hpicfTrunkPortRxFramePercent=_HpicfTrunkPortRxFramePercent_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,6),_HpicfTrunkPortRxFramePercent_Type())
hpicfTrunkPortRxFramePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortRxFramePercent.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortRxFramePercent.setUnits(_N)
_HpicfTrunkPortTxFramePercent_Type=Unsigned32
_HpicfTrunkPortTxFramePercent_Object=MibTableColumn
hpicfTrunkPortTxFramePercent=_HpicfTrunkPortTxFramePercent_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,7),_HpicfTrunkPortTxFramePercent_Type())
hpicfTrunkPortTxFramePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortTxFramePercent.setStatus(_A)
if mibBuilder.loadTexts:hpicfTrunkPortTxFramePercent.setUnits(_N)
_HpicfTrunkPortDropTxFramePercent_Type=Unsigned32
_HpicfTrunkPortDropTxFramePercent_Object=MibTableColumn
hpicfTrunkPortDropTxFramePercent=_HpicfTrunkPortDropTxFramePercent_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,4,1,8),_HpicfTrunkPortDropTxFramePercent_Type())
hpicfTrunkPortDropTxFramePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTrunkPortDropTxFramePercent.setStatus(_A)
_HpicfLoadBalanceObjects_ObjectIdentity=ObjectIdentity
hpicfLoadBalanceObjects=_HpicfLoadBalanceObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5))
_HpicfLoadBalanceTable_Object=MibTable
hpicfLoadBalanceTable=_HpicfLoadBalanceTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1))
if mibBuilder.loadTexts:hpicfLoadBalanceTable.setStatus(_A)
_HpicfLoadBalanceEntry_Object=MibTableRow
hpicfLoadBalanceEntry=_HpicfLoadBalanceEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1))
hpicfLoadBalanceEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:hpicfLoadBalanceEntry.setStatus(_A)
class _HpicfLoadBalanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfLoadBalanceIndex_Type.__name__=_F
_HpicfLoadBalanceIndex_Object=MibTableColumn
hpicfLoadBalanceIndex=_HpicfLoadBalanceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,1),_HpicfLoadBalanceIndex_Type())
hpicfLoadBalanceIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfLoadBalanceIndex.setStatus(_A)
_HpicfLoadBalanceTrunkId_Type=InterfaceIndex
_HpicfLoadBalanceTrunkId_Object=MibTableColumn
hpicfLoadBalanceTrunkId=_HpicfLoadBalanceTrunkId_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,2),_HpicfLoadBalanceTrunkId_Type())
hpicfLoadBalanceTrunkId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceTrunkId.setStatus(_A)
_HpicfLoadBalanceSourceMacAddr_Type=MacAddress
_HpicfLoadBalanceSourceMacAddr_Object=MibTableColumn
hpicfLoadBalanceSourceMacAddr=_HpicfLoadBalanceSourceMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,3),_HpicfLoadBalanceSourceMacAddr_Type())
hpicfLoadBalanceSourceMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceSourceMacAddr.setStatus(_A)
_HpicfLoadBalanceDestMacAddr_Type=MacAddress
_HpicfLoadBalanceDestMacAddr_Object=MibTableColumn
hpicfLoadBalanceDestMacAddr=_HpicfLoadBalanceDestMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,4),_HpicfLoadBalanceDestMacAddr_Type())
hpicfLoadBalanceDestMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceDestMacAddr.setStatus(_A)
_HpicfLoadBalanceIPSourceAddrType_Type=InetAddressType
_HpicfLoadBalanceIPSourceAddrType_Object=MibTableColumn
hpicfLoadBalanceIPSourceAddrType=_HpicfLoadBalanceIPSourceAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,5),_HpicfLoadBalanceIPSourceAddrType_Type())
hpicfLoadBalanceIPSourceAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceIPSourceAddrType.setStatus(_A)
class _HpicfLoadBalanceIPSourceAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_HpicfLoadBalanceIPSourceAddr_Type.__name__=_I
_HpicfLoadBalanceIPSourceAddr_Object=MibTableColumn
hpicfLoadBalanceIPSourceAddr=_HpicfLoadBalanceIPSourceAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,6),_HpicfLoadBalanceIPSourceAddr_Type())
hpicfLoadBalanceIPSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceIPSourceAddr.setStatus(_A)
_HpicfLoadBalanceIPDestAddrType_Type=InetAddressType
_HpicfLoadBalanceIPDestAddrType_Object=MibTableColumn
hpicfLoadBalanceIPDestAddrType=_HpicfLoadBalanceIPDestAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,7),_HpicfLoadBalanceIPDestAddrType_Type())
hpicfLoadBalanceIPDestAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceIPDestAddrType.setStatus(_A)
class _HpicfLoadBalanceIPDestAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_HpicfLoadBalanceIPDestAddr_Type.__name__=_I
_HpicfLoadBalanceIPDestAddr_Object=MibTableColumn
hpicfLoadBalanceIPDestAddr=_HpicfLoadBalanceIPDestAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,8),_HpicfLoadBalanceIPDestAddr_Type())
hpicfLoadBalanceIPDestAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceIPDestAddr.setStatus(_A)
_HpicfLoadBalanceSourcePort_Type=Integer32
_HpicfLoadBalanceSourcePort_Object=MibTableColumn
hpicfLoadBalanceSourcePort=_HpicfLoadBalanceSourcePort_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,9),_HpicfLoadBalanceSourcePort_Type())
hpicfLoadBalanceSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceSourcePort.setStatus(_A)
_HpicfLoadBalanceDestPort_Type=Integer32
_HpicfLoadBalanceDestPort_Object=MibTableColumn
hpicfLoadBalanceDestPort=_HpicfLoadBalanceDestPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,10),_HpicfLoadBalanceDestPort_Type())
hpicfLoadBalanceDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceDestPort.setStatus(_A)
_HpicfLoadBalanceEtherType_Type=Integer32
_HpicfLoadBalanceEtherType_Object=MibTableColumn
hpicfLoadBalanceEtherType=_HpicfLoadBalanceEtherType_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,11),_HpicfLoadBalanceEtherType_Type())
hpicfLoadBalanceEtherType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceEtherType.setStatus(_A)
_HpicfLoadBalanceInboundVlan_Type=Integer32
_HpicfLoadBalanceInboundVlan_Object=MibTableColumn
hpicfLoadBalanceInboundVlan=_HpicfLoadBalanceInboundVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,12),_HpicfLoadBalanceInboundVlan_Type())
hpicfLoadBalanceInboundVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceInboundVlan.setStatus(_A)
_HpicfLoadBalanceInboundPort_Type=InterfaceIndex
_HpicfLoadBalanceInboundPort_Object=MibTableColumn
hpicfLoadBalanceInboundPort=_HpicfLoadBalanceInboundPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,13),_HpicfLoadBalanceInboundPort_Type())
hpicfLoadBalanceInboundPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceInboundPort.setStatus(_A)
_HpicfLoadBalanceOutboundPort_Type=InterfaceIndex
_HpicfLoadBalanceOutboundPort_Object=MibTableColumn
hpicfLoadBalanceOutboundPort=_HpicfLoadBalanceOutboundPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,14),_HpicfLoadBalanceOutboundPort_Type())
hpicfLoadBalanceOutboundPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfLoadBalanceOutboundPort.setStatus(_A)
_HpicfLoadBalanceStatus_Type=RowStatus
_HpicfLoadBalanceStatus_Object=MibTableColumn
hpicfLoadBalanceStatus=_HpicfLoadBalanceStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,76,1,5,1,1,15),_HpicfLoadBalanceStatus_Type())
hpicfLoadBalanceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfLoadBalanceStatus.setStatus(_A)
_HpicfLoadBalanceConformance_ObjectIdentity=ObjectIdentity
hpicfLoadBalanceConformance=_HpicfLoadBalanceConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76,2))
_HpicfLoadBalanceCompliances_ObjectIdentity=ObjectIdentity
hpicfLoadBalanceCompliances=_HpicfLoadBalanceCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76,2,1))
_HpicfLoadBalanceGroups_ObjectIdentity=ObjectIdentity
hpicfLoadBalanceGroups=_HpicfLoadBalanceGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,76,2,2))
hpicfLoadBalanceGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,76,2,2,1))
hpicfLoadBalanceGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:hpicfLoadBalanceGroup.setStatus(_A)
hpicfTrunkStatsClearGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,76,2,2,2))
hpicfTrunkStatsClearGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:hpicfTrunkStatsClearGroup.setStatus(_A)
hpicfTrunkStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,76,2,2,3))
hpicfTrunkStatsGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpicfTrunkStatsGroup.setStatus(_A)
hpicfTrunkPortStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,76,2,2,4))
hpicfTrunkPortStatsGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:hpicfTrunkPortStatsGroup.setStatus(_A)
hpicfLoadBalanceGroup5=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,76,2,2,5))
hpicfLoadBalanceGroup5.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:hpicfLoadBalanceGroup5.setStatus(_A)
hpicfLoadBalanceCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,76,2,1,1))
hpicfLoadBalanceCompliance.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:hpicfLoadBalanceCompliance.setStatus(_A)
hpicfTrunkStatsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,76,2,1,2))
hpicfTrunkStatsCompliance.setObjects(*((_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:hpicfTrunkStatsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfLoadBalanceMod':hpicfLoadBalanceMod,'hpicfLoadBalanceNotifications':hpicfLoadBalanceNotifications,'hpicfLoadBalanceMethodMod':hpicfLoadBalanceMethodMod,_P:hpicfTrunkLoadBalanceMethod,'hpicfTrunkClearStatsTable':hpicfTrunkClearStatsTable,'hpicfTrunkClearStatsEntry':hpicfTrunkClearStatsEntry,_G:hpicfTrunkId,_Q:hpicfTrunkStatsClear,'hpicfTrunkStatsTable':hpicfTrunkStatsTable,'hpicfTrunkStatsEntry':hpicfTrunkStatsEntry,_R:hpicfTrunkUpTime,_S:hpicfTrunkTotalBytesRx,_T:hpicfTrunkTotalBytesTx,_V:hpicfTrunkTotalFramesRx,_U:hpicfTrunkTotalFramesTx,_W:hpicfTrunkTotalDropsTx,'hpicfTrunkPortStatsTable':hpicfTrunkPortStatsTable,'hpicfTrunkPortStatsEntry':hpicfTrunkPortStatsEntry,_X:hpicfTrunkPortBytesRx,_Y:hpicfTrunkPortBytesTx,_Z:hpicfTrunkPortFramesRx,_a:hpicfTrunkPortFramesTx,_b:hpicfTrunkPortFramesDropTx,_c:hpicfTrunkPortRxFramePercent,_d:hpicfTrunkPortTxFramePercent,_e:hpicfTrunkPortDropTxFramePercent,'hpicfLoadBalanceObjects':hpicfLoadBalanceObjects,'hpicfLoadBalanceTable':hpicfLoadBalanceTable,'hpicfLoadBalanceEntry':hpicfLoadBalanceEntry,_O:hpicfLoadBalanceIndex,_f:hpicfLoadBalanceTrunkId,_g:hpicfLoadBalanceSourceMacAddr,_h:hpicfLoadBalanceDestMacAddr,_i:hpicfLoadBalanceIPSourceAddrType,_j:hpicfLoadBalanceIPSourceAddr,_k:hpicfLoadBalanceIPDestAddrType,_l:hpicfLoadBalanceIPDestAddr,_m:hpicfLoadBalanceSourcePort,_n:hpicfLoadBalanceDestPort,_o:hpicfLoadBalanceEtherType,_p:hpicfLoadBalanceInboundVlan,_q:hpicfLoadBalanceInboundPort,_r:hpicfLoadBalanceOutboundPort,_s:hpicfLoadBalanceStatus,'hpicfLoadBalanceConformance':hpicfLoadBalanceConformance,'hpicfLoadBalanceCompliances':hpicfLoadBalanceCompliances,'hpicfLoadBalanceCompliance':hpicfLoadBalanceCompliance,'hpicfTrunkStatsCompliance':hpicfTrunkStatsCompliance,'hpicfLoadBalanceGroups':hpicfLoadBalanceGroups,_t:hpicfLoadBalanceGroup,_v:hpicfTrunkStatsClearGroup,_w:hpicfTrunkStatsGroup,_x:hpicfTrunkPortStatsGroup,_u:hpicfLoadBalanceGroup5})