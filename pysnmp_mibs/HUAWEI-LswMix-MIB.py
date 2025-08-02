_H='standby'
_G='master'
_F='hwLswSlotIndex'
_E='hwLswFrameIndex'
_D='HUAWEI-LSW-DEV-ADM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','lswCommon')
hwLswFrameIndex,hwLswSlotIndex=mibBuilder.importSymbols(_D,_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwLswMix=ModuleIdentity((1,3,6,1,4,1,2011,2,23,1,17))
if mibBuilder.loadTexts:hwLswMix.setRevisions(('2001-06-29 00:00',))
_HwLswLastSwitchDate_Type=Integer32
_HwLswLastSwitchDate_Object=MibScalar
hwLswLastSwitchDate=_HwLswLastSwitchDate_Object((1,3,6,1,4,1,2011,2,23,1,17,1),_HwLswLastSwitchDate_Type())
hwLswLastSwitchDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hwLswLastSwitchDate.setStatus(_A)
_HwLswLastSwitchTime_Type=Integer32
_HwLswLastSwitchTime_Object=MibScalar
hwLswLastSwitchTime=_HwLswLastSwitchTime_Object((1,3,6,1,4,1,2011,2,23,1,17,2),_HwLswLastSwitchTime_Type())
hwLswLastSwitchTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hwLswLastSwitchTime.setStatus(_A)
_HwLswMpuSwitchsNum_Type=Integer32
_HwLswMpuSwitchsNum_Object=MibScalar
hwLswMpuSwitchsNum=_HwLswMpuSwitchsNum_Object((1,3,6,1,4,1,2011,2,23,1,17,3),_HwLswMpuSwitchsNum_Type())
hwLswMpuSwitchsNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwLswMpuSwitchsNum.setStatus(_A)
class _HwLswMpuSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('switch',1))
_HwLswMpuSwitch_Type.__name__=_C
_HwLswMpuSwitch_Object=MibScalar
hwLswMpuSwitch=_HwLswMpuSwitch_Object((1,3,6,1,4,1,2011,2,23,1,17,4),_HwLswMpuSwitch_Type())
hwLswMpuSwitch.setMaxAccess('read-write')
if mibBuilder.loadTexts:hwLswMpuSwitch.setStatus(_A)
_HwLswXSlotTable_Object=MibTable
hwLswXSlotTable=_HwLswXSlotTable_Object((1,3,6,1,4,1,2011,2,23,1,17,5))
if mibBuilder.loadTexts:hwLswXSlotTable.setStatus(_A)
_HwLswXSlotEntry_Object=MibTableRow
hwLswXSlotEntry=_HwLswXSlotEntry_Object((1,3,6,1,4,1,2011,2,23,1,17,5,1))
hwLswXSlotEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:hwLswXSlotEntry.setStatus(_A)
class _HwLswMainCardBoardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('process',3)))
_HwLswMainCardBoardStatus_Type.__name__=_C
_HwLswMainCardBoardStatus_Object=MibTableColumn
hwLswMainCardBoardStatus=_HwLswMainCardBoardStatus_Object((1,3,6,1,4,1,2011,2,23,1,17,5,1,1),_HwLswMainCardBoardStatus_Type())
hwLswMainCardBoardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwLswMainCardBoardStatus.setStatus(_A)
class _HwLswCrossBarStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HwLswCrossBarStatus_Type.__name__=_C
_HwLswCrossBarStatus_Object=MibTableColumn
hwLswCrossBarStatus=_HwLswCrossBarStatus_Object((1,3,6,1,4,1,2011,2,23,1,17,5,1,2),_HwLswCrossBarStatus_Type())
hwLswCrossBarStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwLswCrossBarStatus.setStatus(_A)
_HwsMixTrapMib_ObjectIdentity=ObjectIdentity
hwsMixTrapMib=_HwsMixTrapMib_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,17,10))
hwSlaveSwitchOver=NotificationType((1,3,6,1,4,1,2011,2,23,1,17,10,1))
if mibBuilder.loadTexts:hwSlaveSwitchOver.setStatus(_A)
mibBuilder.exportSymbols('HUAWEI-LswMix-MIB',**{'hwLswMix':hwLswMix,'hwLswLastSwitchDate':hwLswLastSwitchDate,'hwLswLastSwitchTime':hwLswLastSwitchTime,'hwLswMpuSwitchsNum':hwLswMpuSwitchsNum,'hwLswMpuSwitch':hwLswMpuSwitch,'hwLswXSlotTable':hwLswXSlotTable,'hwLswXSlotEntry':hwLswXSlotEntry,'hwLswMainCardBoardStatus':hwLswMainCardBoardStatus,'hwLswCrossBarStatus':hwLswCrossBarStatus,'hwsMixTrapMib':hwsMixTrapMib,'hwSlaveSwitchOver':hwSlaveSwitchOver})