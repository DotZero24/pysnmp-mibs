_H='standby'
_G='master'
_F='hpnicfLswSlotIndex'
_E='hpnicfLswFrameIndex'
_D='HPN-ICF-LSW-DEV-ADM-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfLswFrameIndex,hpnicfLswSlotIndex=mibBuilder.importSymbols(_D,_E,_F)
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfLswMix=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,17))
if mibBuilder.loadTexts:hpnicfLswMix.setRevisions(('2001-06-29 00:00',))
_HpnicfLswLastSwitchDate_Type=Integer32
_HpnicfLswLastSwitchDate_Object=MibScalar
hpnicfLswLastSwitchDate=_HpnicfLswLastSwitchDate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,1),_HpnicfLswLastSwitchDate_Type())
hpnicfLswLastSwitchDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLswLastSwitchDate.setStatus(_A)
_HpnicfLswLastSwitchTime_Type=Integer32
_HpnicfLswLastSwitchTime_Object=MibScalar
hpnicfLswLastSwitchTime=_HpnicfLswLastSwitchTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,2),_HpnicfLswLastSwitchTime_Type())
hpnicfLswLastSwitchTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLswLastSwitchTime.setStatus(_A)
_HpnicfLswMpuSwitchsNum_Type=Integer32
_HpnicfLswMpuSwitchsNum_Object=MibScalar
hpnicfLswMpuSwitchsNum=_HpnicfLswMpuSwitchsNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,3),_HpnicfLswMpuSwitchsNum_Type())
hpnicfLswMpuSwitchsNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLswMpuSwitchsNum.setStatus(_A)
class _HpnicfLswMpuSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('switch',1))
_HpnicfLswMpuSwitch_Type.__name__=_C
_HpnicfLswMpuSwitch_Object=MibScalar
hpnicfLswMpuSwitch=_HpnicfLswMpuSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,4),_HpnicfLswMpuSwitch_Type())
hpnicfLswMpuSwitch.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfLswMpuSwitch.setStatus(_A)
_HpnicfLswXSlotTable_Object=MibTable
hpnicfLswXSlotTable=_HpnicfLswXSlotTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,5))
if mibBuilder.loadTexts:hpnicfLswXSlotTable.setStatus(_A)
_HpnicfLswXSlotEntry_Object=MibTableRow
hpnicfLswXSlotEntry=_HpnicfLswXSlotEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,5,1))
hpnicfLswXSlotEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:hpnicfLswXSlotEntry.setStatus(_A)
class _HpnicfLswMainCardBoardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('process',3)))
_HpnicfLswMainCardBoardStatus_Type.__name__=_C
_HpnicfLswMainCardBoardStatus_Object=MibTableColumn
hpnicfLswMainCardBoardStatus=_HpnicfLswMainCardBoardStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,5,1,1),_HpnicfLswMainCardBoardStatus_Type())
hpnicfLswMainCardBoardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLswMainCardBoardStatus.setStatus(_A)
class _HpnicfLswCrossBarStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HpnicfLswCrossBarStatus_Type.__name__=_C
_HpnicfLswCrossBarStatus_Object=MibTableColumn
hpnicfLswCrossBarStatus=_HpnicfLswCrossBarStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,17,5,1,2),_HpnicfLswCrossBarStatus_Type())
hpnicfLswCrossBarStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLswCrossBarStatus.setStatus(_A)
_HpnicfsMixTrapMib_ObjectIdentity=ObjectIdentity
hpnicfsMixTrapMib=_HpnicfsMixTrapMib_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,17,10))
hpnicfSlaveSwitchOver=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,17,10,1))
if mibBuilder.loadTexts:hpnicfSlaveSwitchOver.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-LswMix-MIB',**{'hpnicfLswMix':hpnicfLswMix,'hpnicfLswLastSwitchDate':hpnicfLswLastSwitchDate,'hpnicfLswLastSwitchTime':hpnicfLswLastSwitchTime,'hpnicfLswMpuSwitchsNum':hpnicfLswMpuSwitchsNum,'hpnicfLswMpuSwitch':hpnicfLswMpuSwitch,'hpnicfLswXSlotTable':hpnicfLswXSlotTable,'hpnicfLswXSlotEntry':hpnicfLswXSlotEntry,'hpnicfLswMainCardBoardStatus':hpnicfLswMainCardBoardStatus,'hpnicfLswCrossBarStatus':hpnicfLswCrossBarStatus,'hpnicfsMixTrapMib':hpnicfsMixTrapMib,'hpnicfSlaveSwitchOver':hpnicfSlaveSwitchOver})