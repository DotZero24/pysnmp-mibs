_F='Integer32'
_E='ifIndex'
_D='read-write'
_C='SWITCH-PORTSTATISTIC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rcPortStatistics=ModuleIdentity((1,3,6,1,4,1,8886,6,1,7))
_RcPortStatsTrap_ObjectIdentity=ObjectIdentity
rcPortStatsTrap=_RcPortStatsTrap_ObjectIdentity((1,3,6,1,4,1,8886,6,1,7,1))
_RcPortStatsObject_ObjectIdentity=ObjectIdentity
rcPortStatsObject=_RcPortStatsObject_ObjectIdentity((1,3,6,1,4,1,8886,6,1,7,2))
_RcPortStatsScalar_ObjectIdentity=ObjectIdentity
rcPortStatsScalar=_RcPortStatsScalar_ObjectIdentity((1,3,6,1,4,1,8886,6,1,7,2,1))
class _RcPortStatsPeriod_Type(Integer32):defaultValue=2000
_RcPortStatsPeriod_Type.__name__=_F
_RcPortStatsPeriod_Object=MibScalar
rcPortStatsPeriod=_RcPortStatsPeriod_Object((1,3,6,1,4,1,8886,6,1,7,2,1,1),_RcPortStatsPeriod_Type())
rcPortStatsPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortStatsPeriod.setStatus(_A)
_RcPortStatsTable_Object=MibTable
rcPortStatsTable=_RcPortStatsTable_Object((1,3,6,1,4,1,8886,6,1,7,2,2))
if mibBuilder.loadTexts:rcPortStatsTable.setStatus(_A)
_RcPortStatsEntry_Object=MibTableRow
rcPortStatsEntry=_RcPortStatsEntry_Object((1,3,6,1,4,1,8886,6,1,7,2,2,1))
rcPortStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:rcPortStatsEntry.setStatus(_A)
_RcPortStatsEnable_Type=TruthValue
_RcPortStatsEnable_Object=MibTableColumn
rcPortStatsEnable=_RcPortStatsEnable_Object((1,3,6,1,4,1,8886,6,1,7,2,2,1,1),_RcPortStatsEnable_Type())
rcPortStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortStatsEnable.setStatus(_A)
_RcPortStatsHistoryPortStatsNextIndex_Type=Integer32
_RcPortStatsHistoryPortStatsNextIndex_Object=MibTableColumn
rcPortStatsHistoryPortStatsNextIndex=_RcPortStatsHistoryPortStatsNextIndex_Object((1,3,6,1,4,1,8886,6,1,7,2,2,1,2),_RcPortStatsHistoryPortStatsNextIndex_Type())
rcPortStatsHistoryPortStatsNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcPortStatsHistoryPortStatsNextIndex.setStatus(_A)
_RcPortStatsClear_Type=TruthValue
_RcPortStatsClear_Object=MibTableColumn
rcPortStatsClear=_RcPortStatsClear_Object((1,3,6,1,4,1,8886,6,1,7,2,2,1,3),_RcPortStatsClear_Type())
rcPortStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortStatsClear.setStatus(_A)
_RcCurrentPortStatsTable_Object=MibTable
rcCurrentPortStatsTable=_RcCurrentPortStatsTable_Object((1,3,6,1,4,1,8886,6,1,7,2,3))
if mibBuilder.loadTexts:rcCurrentPortStatsTable.setStatus(_A)
_RcCurrentPortStatsEntry_Object=MibTableRow
rcCurrentPortStatsEntry=_RcCurrentPortStatsEntry_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1))
rcCurrentPortStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:rcCurrentPortStatsEntry.setStatus(_A)
_RcCurrentPortStatsInPacket_Type=Counter64
_RcCurrentPortStatsInPacket_Object=MibTableColumn
rcCurrentPortStatsInPacket=_RcCurrentPortStatsInPacket_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1,1),_RcCurrentPortStatsInPacket_Type())
rcCurrentPortStatsInPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurrentPortStatsInPacket.setStatus(_A)
_RcCurrentPortStatsOutPacket_Type=Counter64
_RcCurrentPortStatsOutPacket_Object=MibTableColumn
rcCurrentPortStatsOutPacket=_RcCurrentPortStatsOutPacket_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1,2),_RcCurrentPortStatsOutPacket_Type())
rcCurrentPortStatsOutPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurrentPortStatsOutPacket.setStatus(_A)
_RcCurrentPortStatsInAllBits_Type=Counter64
_RcCurrentPortStatsInAllBits_Object=MibTableColumn
rcCurrentPortStatsInAllBits=_RcCurrentPortStatsInAllBits_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1,3),_RcCurrentPortStatsInAllBits_Type())
rcCurrentPortStatsInAllBits.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurrentPortStatsInAllBits.setStatus(_A)
_RcCurrentPortStatsOutAllBits_Type=Counter64
_RcCurrentPortStatsOutAllBits_Object=MibTableColumn
rcCurrentPortStatsOutAllBits=_RcCurrentPortStatsOutAllBits_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1,4),_RcCurrentPortStatsOutAllBits_Type())
rcCurrentPortStatsOutAllBits.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurrentPortStatsOutAllBits.setStatus(_A)
_RcCurrentPortStatsInBandwidthUtilization_Type=Integer32
_RcCurrentPortStatsInBandwidthUtilization_Object=MibTableColumn
rcCurrentPortStatsInBandwidthUtilization=_RcCurrentPortStatsInBandwidthUtilization_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1,5),_RcCurrentPortStatsInBandwidthUtilization_Type())
rcCurrentPortStatsInBandwidthUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurrentPortStatsInBandwidthUtilization.setStatus(_A)
_RcCurrentPortStatsEBandwidthUtilization_Type=Integer32
_RcCurrentPortStatsEBandwidthUtilization_Object=MibTableColumn
rcCurrentPortStatsEBandwidthUtilization=_RcCurrentPortStatsEBandwidthUtilization_Object((1,3,6,1,4,1,8886,6,1,7,2,3,1,6),_RcCurrentPortStatsEBandwidthUtilization_Type())
rcCurrentPortStatsEBandwidthUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCurrentPortStatsEBandwidthUtilization.setStatus(_A)
_RcHistoryPortStatsTable_Object=MibTable
rcHistoryPortStatsTable=_RcHistoryPortStatsTable_Object((1,3,6,1,4,1,8886,6,1,7,2,4))
if mibBuilder.loadTexts:rcHistoryPortStatsTable.setStatus(_A)
_RcHistoryPortStatsEntry_Object=MibTableRow
rcHistoryPortStatsEntry=_RcHistoryPortStatsEntry_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1))
rcHistoryPortStatsEntry.setIndexNames((0,_C,_E),(0,_C,'rcHistoryStatsIndex'))
if mibBuilder.loadTexts:rcHistoryPortStatsEntry.setStatus(_A)
_RcHistoryPortStatsIndex_Type=Integer32
_RcHistoryPortStatsIndex_Object=MibTableColumn
rcHistoryPortStatsIndex=_RcHistoryPortStatsIndex_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,1),_RcHistoryPortStatsIndex_Type())
rcHistoryPortStatsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcHistoryPortStatsIndex.setStatus(_A)
_RcHistoryPortStatsInPacket_Type=Counter64
_RcHistoryPortStatsInPacket_Object=MibTableColumn
rcHistoryPortStatsInPacket=_RcHistoryPortStatsInPacket_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,2),_RcHistoryPortStatsInPacket_Type())
rcHistoryPortStatsInPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHistoryPortStatsInPacket.setStatus(_A)
_RcHistoryPortStatsOutPacket_Type=Counter64
_RcHistoryPortStatsOutPacket_Object=MibTableColumn
rcHistoryPortStatsOutPacket=_RcHistoryPortStatsOutPacket_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,3),_RcHistoryPortStatsOutPacket_Type())
rcHistoryPortStatsOutPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHistoryPortStatsOutPacket.setStatus(_A)
_RcHistoryPortStatsInAllBits_Type=Counter64
_RcHistoryPortStatsInAllBits_Object=MibTableColumn
rcHistoryPortStatsInAllBits=_RcHistoryPortStatsInAllBits_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,4),_RcHistoryPortStatsInAllBits_Type())
rcHistoryPortStatsInAllBits.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHistoryPortStatsInAllBits.setStatus(_A)
_RcHistoryPortStatsOutAllBits_Type=Counter64
_RcHistoryPortStatsOutAllBits_Object=MibTableColumn
rcHistoryPortStatsOutAllBits=_RcHistoryPortStatsOutAllBits_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,5),_RcHistoryPortStatsOutAllBits_Type())
rcHistoryPortStatsOutAllBits.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHistoryPortStatsOutAllBits.setStatus(_A)
_RcHistoryPortStatsInBandwidthUtilization_Type=Integer32
_RcHistoryPortStatsInBandwidthUtilization_Object=MibTableColumn
rcHistoryPortStatsInBandwidthUtilization=_RcHistoryPortStatsInBandwidthUtilization_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,6),_RcHistoryPortStatsInBandwidthUtilization_Type())
rcHistoryPortStatsInBandwidthUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHistoryPortStatsInBandwidthUtilization.setStatus(_A)
_RcHistoryPortStatsEBandwidthUtilization_Type=Integer32
_RcHistoryPortStatsEBandwidthUtilization_Object=MibTableColumn
rcHistoryPortStatsEBandwidthUtilization=_RcHistoryPortStatsEBandwidthUtilization_Object((1,3,6,1,4,1,8886,6,1,7,2,4,1,7),_RcHistoryPortStatsEBandwidthUtilization_Type())
rcHistoryPortStatsEBandwidthUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:rcHistoryPortStatsEBandwidthUtilization.setStatus(_A)
_RcPortStatsConformance_ObjectIdentity=ObjectIdentity
rcPortStatsConformance=_RcPortStatsConformance_ObjectIdentity((1,3,6,1,4,1,8886,6,1,7,3))
mibBuilder.exportSymbols(_C,**{'rcPortStatistics':rcPortStatistics,'rcPortStatsTrap':rcPortStatsTrap,'rcPortStatsObject':rcPortStatsObject,'rcPortStatsScalar':rcPortStatsScalar,'rcPortStatsPeriod':rcPortStatsPeriod,'rcPortStatsTable':rcPortStatsTable,'rcPortStatsEntry':rcPortStatsEntry,'rcPortStatsEnable':rcPortStatsEnable,'rcPortStatsHistoryPortStatsNextIndex':rcPortStatsHistoryPortStatsNextIndex,'rcPortStatsClear':rcPortStatsClear,'rcCurrentPortStatsTable':rcCurrentPortStatsTable,'rcCurrentPortStatsEntry':rcCurrentPortStatsEntry,'rcCurrentPortStatsInPacket':rcCurrentPortStatsInPacket,'rcCurrentPortStatsOutPacket':rcCurrentPortStatsOutPacket,'rcCurrentPortStatsInAllBits':rcCurrentPortStatsInAllBits,'rcCurrentPortStatsOutAllBits':rcCurrentPortStatsOutAllBits,'rcCurrentPortStatsInBandwidthUtilization':rcCurrentPortStatsInBandwidthUtilization,'rcCurrentPortStatsEBandwidthUtilization':rcCurrentPortStatsEBandwidthUtilization,'rcHistoryPortStatsTable':rcHistoryPortStatsTable,'rcHistoryPortStatsEntry':rcHistoryPortStatsEntry,'rcHistoryPortStatsIndex':rcHistoryPortStatsIndex,'rcHistoryPortStatsInPacket':rcHistoryPortStatsInPacket,'rcHistoryPortStatsOutPacket':rcHistoryPortStatsOutPacket,'rcHistoryPortStatsInAllBits':rcHistoryPortStatsInAllBits,'rcHistoryPortStatsOutAllBits':rcHistoryPortStatsOutAllBits,'rcHistoryPortStatsInBandwidthUtilization':rcHistoryPortStatsInBandwidthUtilization,'rcHistoryPortStatsEBandwidthUtilization':rcHistoryPortStatsEBandwidthUtilization,'rcPortStatsConformance':rcPortStatsConformance})