_V='rcRelayStatsProtocolIndex'
_U='PDUs/sec'
_T='not-accessible'
_S='rcRelayThresholdProtocolIndex'
_R='read-only'
_Q='RAISECOM-RELAY-MIB'
_P='pagp'
_O='udld'
_N='pvst'
_M='vtp'
_L='cdp'
_K='gvrp'
_J='gmrp'
_I='lacp'
_H='dot1x'
_G='stp'
_F='rcPortIndex'
_E='SWITCH-SYSTEM-MIB'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols(_E,_F)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcRelay=ModuleIdentity((1,3,6,1,4,1,8886,6,1,35))
if mibBuilder.loadTexts:rcRelay.setRevisions(('2008-03-11 00:00',))
_RcRelayGrobal_ObjectIdentity=ObjectIdentity
rcRelayGrobal=_RcRelayGrobal_ObjectIdentity((1,3,6,1,4,1,8886,6,1,35,1))
_RcRelayMacAddress_Type=MacAddress
_RcRelayMacAddress_Object=MibScalar
rcRelayMacAddress=_RcRelayMacAddress_Object((1,3,6,1,4,1,8886,6,1,35,1,1),_RcRelayMacAddress_Type())
rcRelayMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayMacAddress.setStatus(_A)
class _RcRelayCos_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcRelayCos_Type.__name__=_D
_RcRelayCos_Object=MibScalar
rcRelayCos=_RcRelayCos_Object((1,3,6,1,4,1,8886,6,1,35,1,2),_RcRelayCos_Type())
rcRelayCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayCos.setStatus(_A)
_RcRelayTransparentEnable_Type=EnableVar
_RcRelayTransparentEnable_Object=MibScalar
rcRelayTransparentEnable=_RcRelayTransparentEnable_Object((1,3,6,1,4,1,8886,6,1,35,1,3),_RcRelayTransparentEnable_Type())
rcRelayTransparentEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayTransparentEnable.setStatus(_A)
_RcRelayProtocolTable_Object=MibTable
rcRelayProtocolTable=_RcRelayProtocolTable_Object((1,3,6,1,4,1,8886,6,1,35,2))
if mibBuilder.loadTexts:rcRelayProtocolTable.setStatus(_A)
_RcRelayProtocolEntry_Object=MibTableRow
rcRelayProtocolEntry=_RcRelayProtocolEntry_Object((1,3,6,1,4,1,8886,6,1,35,2,1))
rcRelayProtocolEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rcRelayProtocolEntry.setStatus(_A)
class _RcRelayProtocolType_Type(Bits):namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9)))
_RcRelayProtocolType_Type.__name__='Bits'
_RcRelayProtocolType_Object=MibTableColumn
rcRelayProtocolType=_RcRelayProtocolType_Object((1,3,6,1,4,1,8886,6,1,35,2,1,1),_RcRelayProtocolType_Type())
rcRelayProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayProtocolType.setStatus(_A)
_RcRelayProtocolVlan_Type=Unsigned32
_RcRelayProtocolVlan_Object=MibTableColumn
rcRelayProtocolVlan=_RcRelayProtocolVlan_Object((1,3,6,1,4,1,8886,6,1,35,2,1,2),_RcRelayProtocolVlan_Type())
rcRelayProtocolVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayProtocolVlan.setStatus(_A)
_RcRelayProtocolEgressPort_Type=Unsigned32
_RcRelayProtocolEgressPort_Object=MibTableColumn
rcRelayProtocolEgressPort=_RcRelayProtocolEgressPort_Object((1,3,6,1,4,1,8886,6,1,35,2,1,3),_RcRelayProtocolEgressPort_Type())
rcRelayProtocolEgressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayProtocolEgressPort.setStatus(_A)
class _RcRelayProtocolPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RcRelayProtocolPortStatus_Type.__name__=_C
_RcRelayProtocolPortStatus_Object=MibTableColumn
rcRelayProtocolPortStatus=_RcRelayProtocolPortStatus_Object((1,3,6,1,4,1,8886,6,1,35,2,1,4),_RcRelayProtocolPortStatus_Type())
rcRelayProtocolPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayProtocolPortStatus.setStatus(_A)
_RcRelayThresholdTable_Object=MibTable
rcRelayThresholdTable=_RcRelayThresholdTable_Object((1,3,6,1,4,1,8886,6,1,35,3))
if mibBuilder.loadTexts:rcRelayThresholdTable.setStatus(_A)
_RcRelayThresholdEntry_Object=MibTableRow
rcRelayThresholdEntry=_RcRelayThresholdEntry_Object((1,3,6,1,4,1,8886,6,1,35,3,1))
rcRelayThresholdEntry.setIndexNames((0,_E,_F),(0,_Q,_S))
if mibBuilder.loadTexts:rcRelayThresholdEntry.setStatus(_A)
class _RcRelayThresholdProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10)))
_RcRelayThresholdProtocolIndex_Type.__name__=_C
_RcRelayThresholdProtocolIndex_Object=MibTableColumn
rcRelayThresholdProtocolIndex=_RcRelayThresholdProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,35,3,1,1),_RcRelayThresholdProtocolIndex_Type())
rcRelayThresholdProtocolIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:rcRelayThresholdProtocolIndex.setStatus(_A)
class _RcRelayDropThreshold_Type(Unsigned32):defaultValue=0
_RcRelayDropThreshold_Type.__name__=_D
_RcRelayDropThreshold_Object=MibTableColumn
rcRelayDropThreshold=_RcRelayDropThreshold_Object((1,3,6,1,4,1,8886,6,1,35,3,1,2),_RcRelayDropThreshold_Type())
rcRelayDropThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayDropThreshold.setStatus(_A)
if mibBuilder.loadTexts:rcRelayDropThreshold.setUnits(_U)
class _RcRelayShutdownThreshold_Type(Unsigned32):defaultValue=0
_RcRelayShutdownThreshold_Type.__name__=_D
_RcRelayShutdownThreshold_Object=MibTableColumn
rcRelayShutdownThreshold=_RcRelayShutdownThreshold_Object((1,3,6,1,4,1,8886,6,1,35,3,1,3),_RcRelayShutdownThreshold_Type())
rcRelayShutdownThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRelayShutdownThreshold.setStatus(_A)
if mibBuilder.loadTexts:rcRelayShutdownThreshold.setUnits(_U)
_RcRelayStatisticsTable_Object=MibTable
rcRelayStatisticsTable=_RcRelayStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,35,4))
if mibBuilder.loadTexts:rcRelayStatisticsTable.setStatus(_A)
_RcRelayStatisticsEntry_Object=MibTableRow
rcRelayStatisticsEntry=_RcRelayStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,35,4,1))
rcRelayStatisticsEntry.setIndexNames((0,_E,_F),(0,_Q,_V))
if mibBuilder.loadTexts:rcRelayStatisticsEntry.setStatus(_A)
class _RcRelayStatsProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10)))
_RcRelayStatsProtocolIndex_Type.__name__=_C
_RcRelayStatsProtocolIndex_Object=MibTableColumn
rcRelayStatsProtocolIndex=_RcRelayStatsProtocolIndex_Object((1,3,6,1,4,1,8886,6,1,35,4,1,1),_RcRelayStatsProtocolIndex_Type())
rcRelayStatsProtocolIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:rcRelayStatsProtocolIndex.setStatus(_A)
_RcRelayEncapStats_Type=Counter32
_RcRelayEncapStats_Object=MibTableColumn
rcRelayEncapStats=_RcRelayEncapStats_Object((1,3,6,1,4,1,8886,6,1,35,4,1,2),_RcRelayEncapStats_Type())
rcRelayEncapStats.setMaxAccess(_R)
if mibBuilder.loadTexts:rcRelayEncapStats.setStatus(_A)
if mibBuilder.loadTexts:rcRelayEncapStats.setUnits('encapsulated PDUs')
_RcRelayDeEncapStats_Type=Counter32
_RcRelayDeEncapStats_Object=MibTableColumn
rcRelayDeEncapStats=_RcRelayDeEncapStats_Object((1,3,6,1,4,1,8886,6,1,35,4,1,3),_RcRelayDeEncapStats_Type())
rcRelayDeEncapStats.setMaxAccess(_R)
if mibBuilder.loadTexts:rcRelayDeEncapStats.setStatus(_A)
if mibBuilder.loadTexts:rcRelayDeEncapStats.setUnits('de-encapsulated PDUs')
_RcRelayDropStats_Type=Counter32
_RcRelayDropStats_Object=MibTableColumn
rcRelayDropStats=_RcRelayDropStats_Object((1,3,6,1,4,1,8886,6,1,35,4,1,4),_RcRelayDropStats_Type())
rcRelayDropStats.setMaxAccess(_R)
if mibBuilder.loadTexts:rcRelayDropStats.setStatus(_A)
if mibBuilder.loadTexts:rcRelayDropStats.setUnits('PDUs')
mibBuilder.exportSymbols(_Q,**{'rcRelay':rcRelay,'rcRelayGrobal':rcRelayGrobal,'rcRelayMacAddress':rcRelayMacAddress,'rcRelayCos':rcRelayCos,'rcRelayTransparentEnable':rcRelayTransparentEnable,'rcRelayProtocolTable':rcRelayProtocolTable,'rcRelayProtocolEntry':rcRelayProtocolEntry,'rcRelayProtocolType':rcRelayProtocolType,'rcRelayProtocolVlan':rcRelayProtocolVlan,'rcRelayProtocolEgressPort':rcRelayProtocolEgressPort,'rcRelayProtocolPortStatus':rcRelayProtocolPortStatus,'rcRelayThresholdTable':rcRelayThresholdTable,'rcRelayThresholdEntry':rcRelayThresholdEntry,_S:rcRelayThresholdProtocolIndex,'rcRelayDropThreshold':rcRelayDropThreshold,'rcRelayShutdownThreshold':rcRelayShutdownThreshold,'rcRelayStatisticsTable':rcRelayStatisticsTable,'rcRelayStatisticsEntry':rcRelayStatisticsEntry,_V:rcRelayStatsProtocolIndex,'rcRelayEncapStats':rcRelayEncapStats,'rcRelayDeEncapStats':rcRelayDeEncapStats,'rcRelayDropStats':rcRelayDropStats})