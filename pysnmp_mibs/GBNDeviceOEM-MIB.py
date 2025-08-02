_h='oemChipGroup'
_g='oemArchIfaceGroup'
_f='oemChipStub'
_e='oemArchIfaceRxIpInHdrErrors'
_d='oemArchIfaceTxL3AbortedPkts'
_c='oemArchIfaceTxL3Pkts'
_b='oemArchIfaceTxVlanTagPkts'
_a='oemArchIfaceFlowControl'
_Z='oemArchIfacePortLoop'
_Y='oemArchIfaceDuplexSpeedGet'
_X='oemArchIfaceDuplexSpeedSet'
_W='oemArchIfaceLink'
_V='oemArchIfaceSTPEnable'
_U='oemArchIfaceEnable'
_T='oemArchIfaceName'
_S='oemArchIfaceIfIndex'
_R='oemArchIfaceLLWHPort'
_Q='disable'
_P='illegal'
_O='full-1000'
_N='half-1000'
_M='full-100'
_L='half-100'
_K='full-10'
_J='half-10'
_I='oemArchIfacePort'
_H='oemArchIfaceUnit'
_G='DisplayString'
_F='ifIndex'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='GBNDeviceOEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnDevice,=mibBuilder.importSymbols('GREENTECH-MASTER-MIB','gbnDevice')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
bcm5600=ModuleIdentity((1,3,6,1,4,1,13464,1,2,2,3))
if mibBuilder.loadTexts:bcm5600.setRevisions(('2018-02-14 00:00','1901-05-03 00:00'))
_OemArchIface_ObjectIdentity=ObjectIdentity
oemArchIface=_OemArchIface_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,3,1))
_OemArchIfaceTable_Object=MibTable
oemArchIfaceTable=_OemArchIfaceTable_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1))
if mibBuilder.loadTexts:oemArchIfaceTable.setStatus(_A)
_OemArchIfaceEntry_Object=MibTableRow
oemArchIfaceEntry=_OemArchIfaceEntry_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1))
oemArchIfaceEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:oemArchIfaceEntry.setStatus(_A)
class _OemArchIfaceUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_OemArchIfaceUnit_Type.__name__=_C
_OemArchIfaceUnit_Object=MibTableColumn
oemArchIfaceUnit=_OemArchIfaceUnit_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,1),_OemArchIfaceUnit_Type())
oemArchIfaceUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceUnit.setStatus(_A)
_OemArchIfacePort_Type=Integer32
_OemArchIfacePort_Object=MibTableColumn
oemArchIfacePort=_OemArchIfacePort_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,2),_OemArchIfacePort_Type())
oemArchIfacePort.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfacePort.setStatus(_A)
class _OemArchIfaceLLWHPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8193,8296))
_OemArchIfaceLLWHPort_Type.__name__=_C
_OemArchIfaceLLWHPort_Object=MibTableColumn
oemArchIfaceLLWHPort=_OemArchIfaceLLWHPort_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,3),_OemArchIfaceLLWHPort_Type())
oemArchIfaceLLWHPort.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceLLWHPort.setStatus(_A)
_OemArchIfaceIfIndex_Type=Integer32
_OemArchIfaceIfIndex_Object=MibTableColumn
oemArchIfaceIfIndex=_OemArchIfaceIfIndex_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,4),_OemArchIfaceIfIndex_Type())
oemArchIfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceIfIndex.setStatus(_A)
class _OemArchIfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OemArchIfaceName_Type.__name__=_G
_OemArchIfaceName_Object=MibTableColumn
oemArchIfaceName=_OemArchIfaceName_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,5),_OemArchIfaceName_Type())
oemArchIfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfaceName.setStatus(_A)
class _OemArchIfaceEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_OemArchIfaceEnable_Type.__name__=_C
_OemArchIfaceEnable_Object=MibTableColumn
oemArchIfaceEnable=_OemArchIfaceEnable_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,6),_OemArchIfaceEnable_Type())
oemArchIfaceEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfaceEnable.setStatus(_A)
_OemArchIfaceSTPEnable_Type=TruthValue
_OemArchIfaceSTPEnable_Object=MibTableColumn
oemArchIfaceSTPEnable=_OemArchIfaceSTPEnable_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,7),_OemArchIfaceSTPEnable_Type())
oemArchIfaceSTPEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfaceSTPEnable.setStatus(_A)
class _OemArchIfaceLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_OemArchIfaceLink_Type.__name__=_C
_OemArchIfaceLink_Object=MibTableColumn
oemArchIfaceLink=_OemArchIfaceLink_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,8),_OemArchIfaceLink_Type())
oemArchIfaceLink.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceLink.setStatus(_A)
class _OemArchIfaceDuplexSpeedSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*(('autonegotiate',1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,99)))
_OemArchIfaceDuplexSpeedSet_Type.__name__=_C
_OemArchIfaceDuplexSpeedSet_Object=MibTableColumn
oemArchIfaceDuplexSpeedSet=_OemArchIfaceDuplexSpeedSet_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,9),_OemArchIfaceDuplexSpeedSet_Type())
oemArchIfaceDuplexSpeedSet.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfaceDuplexSpeedSet.setStatus(_A)
class _OemArchIfaceDuplexSpeedGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,99)));namedValues=NamedValues(*(('unknown',1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),('auto-10',8),('auto-100',9),('auto-1000',10),(_P,99)))
_OemArchIfaceDuplexSpeedGet_Type.__name__=_C
_OemArchIfaceDuplexSpeedGet_Object=MibTableColumn
oemArchIfaceDuplexSpeedGet=_OemArchIfaceDuplexSpeedGet_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,10),_OemArchIfaceDuplexSpeedGet_Type())
oemArchIfaceDuplexSpeedGet.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceDuplexSpeedGet.setStatus(_A)
class _OemArchIfacePortLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('internalEnable',1),('externalEnable',2),(_Q,3)))
_OemArchIfacePortLoop_Type.__name__=_C
_OemArchIfacePortLoop_Object=MibTableColumn
oemArchIfacePortLoop=_OemArchIfacePortLoop_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,11),_OemArchIfacePortLoop_Type())
oemArchIfacePortLoop.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfacePortLoop.setStatus(_A)
class _OemArchIfaceFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_Q,2)))
_OemArchIfaceFlowControl_Type.__name__=_C
_OemArchIfaceFlowControl_Object=MibTableColumn
oemArchIfaceFlowControl=_OemArchIfaceFlowControl_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,12),_OemArchIfaceFlowControl_Type())
oemArchIfaceFlowControl.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfaceFlowControl.setStatus(_A)
_OemArchIfaceTxVlanTagPkts_Type=Counter64
_OemArchIfaceTxVlanTagPkts_Object=MibTableColumn
oemArchIfaceTxVlanTagPkts=_OemArchIfaceTxVlanTagPkts_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,13),_OemArchIfaceTxVlanTagPkts_Type())
oemArchIfaceTxVlanTagPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceTxVlanTagPkts.setStatus(_A)
_OemArchIfaceTxL3Pkts_Type=Counter64
_OemArchIfaceTxL3Pkts_Object=MibTableColumn
oemArchIfaceTxL3Pkts=_OemArchIfaceTxL3Pkts_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,14),_OemArchIfaceTxL3Pkts_Type())
oemArchIfaceTxL3Pkts.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceTxL3Pkts.setStatus(_A)
_OemArchIfaceTxL3AbortedPkts_Type=Counter64
_OemArchIfaceTxL3AbortedPkts_Object=MibTableColumn
oemArchIfaceTxL3AbortedPkts=_OemArchIfaceTxL3AbortedPkts_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,15),_OemArchIfaceTxL3AbortedPkts_Type())
oemArchIfaceTxL3AbortedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceTxL3AbortedPkts.setStatus(_A)
_OemArchIfaceRxIpInHdrErrors_Type=Counter64
_OemArchIfaceRxIpInHdrErrors_Object=MibTableColumn
oemArchIfaceRxIpInHdrErrors=_OemArchIfaceRxIpInHdrErrors_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,16),_OemArchIfaceRxIpInHdrErrors_Type())
oemArchIfaceRxIpInHdrErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:oemArchIfaceRxIpInHdrErrors.setStatus(_A)
class _OemArchIfaceL2Tunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_OemArchIfaceL2Tunneling_Type.__name__=_C
_OemArchIfaceL2Tunneling_Object=MibTableColumn
oemArchIfaceL2Tunneling=_OemArchIfaceL2Tunneling_Object((1,3,6,1,4,1,13464,1,2,2,3,1,1,1,17),_OemArchIfaceL2Tunneling_Type())
oemArchIfaceL2Tunneling.setMaxAccess(_E)
if mibBuilder.loadTexts:oemArchIfaceL2Tunneling.setStatus(_A)
_OemArchIfaceTrap_ObjectIdentity=ObjectIdentity
oemArchIfaceTrap=_OemArchIfaceTrap_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,3,1,2))
_OemChip_ObjectIdentity=ObjectIdentity
oemChip=_OemChip_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,3,2))
class _OemChipStub_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noop',1),('chip-value2',2),('chip-value3',3)))
_OemChipStub_Type.__name__=_C
_OemChipStub_Object=MibScalar
oemChipStub=_OemChipStub_Object((1,3,6,1,4,1,13464,1,2,2,3,2,1),_OemChipStub_Type())
oemChipStub.setMaxAccess(_E)
if mibBuilder.loadTexts:oemChipStub.setStatus(_A)
_OemProdConformance_ObjectIdentity=ObjectIdentity
oemProdConformance=_OemProdConformance_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,3,3))
_OemProdGroups_ObjectIdentity=ObjectIdentity
oemProdGroups=_OemProdGroups_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,3,3,1))
_OemProdCompliances_ObjectIdentity=ObjectIdentity
oemProdCompliances=_OemProdCompliances_ObjectIdentity((1,3,6,1,4,1,13464,1,2,2,3,3,2))
oemArchIfaceGroup=ObjectGroup((1,3,6,1,4,1,13464,1,2,2,3,3,1,1))
oemArchIfaceGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:oemArchIfaceGroup.setStatus(_A)
oemChipGroup=ObjectGroup((1,3,6,1,4,1,13464,1,2,2,3,3,1,2))
oemChipGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:oemChipGroup.setStatus(_A)
macAddrLimitOn=NotificationType((1,3,6,1,4,1,13464,1,2,2,3,1,2,1))
macAddrLimitOn.setObjects((_B,_F))
if mibBuilder.loadTexts:macAddrLimitOn.setStatus(_A)
macAddrLimitOff=NotificationType((1,3,6,1,4,1,13464,1,2,2,3,1,2,2))
macAddrLimitOff.setObjects((_B,_F))
if mibBuilder.loadTexts:macAddrLimitOff.setStatus(_A)
stormCtrlPortShutdown=NotificationType((1,3,6,1,4,1,13464,1,2,2,3,1,2,3))
stormCtrlPortShutdown.setObjects((_B,_F))
if mibBuilder.loadTexts:stormCtrlPortShutdown.setStatus(_A)
stormCtrlPortFree=NotificationType((1,3,6,1,4,1,13464,1,2,2,3,1,2,4))
stormCtrlPortFree.setObjects((_B,_F))
if mibBuilder.loadTexts:stormCtrlPortFree.setStatus(_A)
oemProdCompliance=ModuleCompliance((1,3,6,1,4,1,13464,1,2,2,3,3,2,1))
oemProdCompliance.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:oemProdCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bcm5600':bcm5600,'oemArchIface':oemArchIface,'oemArchIfaceTable':oemArchIfaceTable,'oemArchIfaceEntry':oemArchIfaceEntry,_H:oemArchIfaceUnit,_I:oemArchIfacePort,_R:oemArchIfaceLLWHPort,_S:oemArchIfaceIfIndex,_T:oemArchIfaceName,_U:oemArchIfaceEnable,_V:oemArchIfaceSTPEnable,_W:oemArchIfaceLink,_X:oemArchIfaceDuplexSpeedSet,_Y:oemArchIfaceDuplexSpeedGet,_Z:oemArchIfacePortLoop,_a:oemArchIfaceFlowControl,_b:oemArchIfaceTxVlanTagPkts,_c:oemArchIfaceTxL3Pkts,_d:oemArchIfaceTxL3AbortedPkts,_e:oemArchIfaceRxIpInHdrErrors,'oemArchIfaceL2Tunneling':oemArchIfaceL2Tunneling,'oemArchIfaceTrap':oemArchIfaceTrap,'macAddrLimitOn':macAddrLimitOn,'macAddrLimitOff':macAddrLimitOff,'stormCtrlPortShutdown':stormCtrlPortShutdown,'stormCtrlPortFree':stormCtrlPortFree,'oemChip':oemChip,_f:oemChipStub,'oemProdConformance':oemProdConformance,'oemProdGroups':oemProdGroups,_g:oemArchIfaceGroup,_h:oemChipGroup,'oemProdCompliances':oemProdCompliances,'oemProdCompliance':oemProdCompliance})