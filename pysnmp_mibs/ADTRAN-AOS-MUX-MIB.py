_g='adGenAOSTdmGroupGrp'
_f='adGenAOSXConnectGrp'
_e='adGenAOSTdmGroupUsage'
_d='adGenAOSTdmGroupMask'
_c='adGenAOSXConnectRowStatus'
_b='adGenAOSXConnectPreserveRbs'
_a='adGenAOSXConnectSecondTdmGroupDS0'
_Z='adGenAOSXConnectSecondTdmGroup'
_Y='adGenAOSXConnectSecondIfPort'
_X='adGenAOSXConnectSecondIfSlot'
_W='adGenAOSXConnectSecondSubIfNumber'
_V='adGenAOSXConnectSecondIfNumber'
_U='adGenAOSXConnectSecondIfType'
_T='adGenAOSXConnectFirstTdmGroupDS0'
_S='adGenAOSXConnectFirstTdmGroup'
_R='adGenAOSXConnectFirstIfPort'
_Q='adGenAOSXConnectFirstIfSlot'
_P='adGenAOSXConnectFirstSubIfNumber'
_O='adGenAOSXConnectFirstIfNumber'
_N='adGenAOSXConnectFirstIfType'
_M='read-write'
_L='frameRelay'
_K='serial'
_J='notAssigned'
_I='read-only'
_H='adGenAOSTdmGroupID'
_G='adGenAOSTdmGroupIfPort'
_F='adGenAOSTdmGroupIfSlot'
_E='adGenAOSXConnectIndex'
_D='read-create'
_C='Integer32'
_B='ADTRAN-AOS-MUX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSCommon,adGenAOSConformance=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSCommon','adGenAOSConformance')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
adGenAOSMuxID=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,1,5))
_AdGenAOSMux_ObjectIdentity=ObjectIdentity
adGenAOSMux=_AdGenAOSMux_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,5))
_AdGenAOSXConnect_ObjectIdentity=ObjectIdentity
adGenAOSXConnect=_AdGenAOSXConnect_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,5,1))
_AdGenAOSXConnectTable_Object=MibTable
adGenAOSXConnectTable=_AdGenAOSXConnectTable_Object((1,3,6,1,4,1,664,5,53,1,5,1,1))
if mibBuilder.loadTexts:adGenAOSXConnectTable.setStatus(_A)
_AdGenAOSXConnectEntry_Object=MibTableRow
adGenAOSXConnectEntry=_AdGenAOSXConnectEntry_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1))
adGenAOSXConnectEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:adGenAOSXConnectEntry.setStatus(_A)
class _AdGenAOSXConnectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_AdGenAOSXConnectIndex_Type.__name__=_C
_AdGenAOSXConnectIndex_Object=MibTableColumn
adGenAOSXConnectIndex=_AdGenAOSXConnectIndex_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,1),_AdGenAOSXConnectIndex_Type())
adGenAOSXConnectIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectIndex.setStatus(_A)
class _AdGenAOSXConnectFirstIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,0),('dds',1),('t1E1',2),('eth',3),(_K,4),('shdsl',5),('fxs',6),(_L,7),('ppp',8)))
_AdGenAOSXConnectFirstIfType_Type.__name__=_C
_AdGenAOSXConnectFirstIfType_Object=MibTableColumn
adGenAOSXConnectFirstIfType=_AdGenAOSXConnectFirstIfType_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,2),_AdGenAOSXConnectFirstIfType_Type())
adGenAOSXConnectFirstIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstIfType.setStatus(_A)
class _AdGenAOSXConnectFirstIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_AdGenAOSXConnectFirstIfNumber_Type.__name__=_C
_AdGenAOSXConnectFirstIfNumber_Object=MibTableColumn
adGenAOSXConnectFirstIfNumber=_AdGenAOSXConnectFirstIfNumber_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,3),_AdGenAOSXConnectFirstIfNumber_Type())
adGenAOSXConnectFirstIfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstIfNumber.setStatus(_A)
class _AdGenAOSXConnectFirstSubIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1007))
_AdGenAOSXConnectFirstSubIfNumber_Type.__name__=_C
_AdGenAOSXConnectFirstSubIfNumber_Object=MibTableColumn
adGenAOSXConnectFirstSubIfNumber=_AdGenAOSXConnectFirstSubIfNumber_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,4),_AdGenAOSXConnectFirstSubIfNumber_Type())
adGenAOSXConnectFirstSubIfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstSubIfNumber.setStatus(_A)
class _AdGenAOSXConnectFirstIfSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenAOSXConnectFirstIfSlot_Type.__name__=_C
_AdGenAOSXConnectFirstIfSlot_Object=MibTableColumn
adGenAOSXConnectFirstIfSlot=_AdGenAOSXConnectFirstIfSlot_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,5),_AdGenAOSXConnectFirstIfSlot_Type())
adGenAOSXConnectFirstIfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstIfSlot.setStatus(_A)
class _AdGenAOSXConnectFirstIfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_AdGenAOSXConnectFirstIfPort_Type.__name__=_C
_AdGenAOSXConnectFirstIfPort_Object=MibTableColumn
adGenAOSXConnectFirstIfPort=_AdGenAOSXConnectFirstIfPort_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,6),_AdGenAOSXConnectFirstIfPort_Type())
adGenAOSXConnectFirstIfPort.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstIfPort.setStatus(_A)
class _AdGenAOSXConnectFirstTdmGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenAOSXConnectFirstTdmGroup_Type.__name__=_C
_AdGenAOSXConnectFirstTdmGroup_Object=MibTableColumn
adGenAOSXConnectFirstTdmGroup=_AdGenAOSXConnectFirstTdmGroup_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,7),_AdGenAOSXConnectFirstTdmGroup_Type())
adGenAOSXConnectFirstTdmGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstTdmGroup.setStatus(_A)
class _AdGenAOSXConnectFirstTdmGroupDS0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AdGenAOSXConnectFirstTdmGroupDS0_Type.__name__=_C
_AdGenAOSXConnectFirstTdmGroupDS0_Object=MibTableColumn
adGenAOSXConnectFirstTdmGroupDS0=_AdGenAOSXConnectFirstTdmGroupDS0_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,8),_AdGenAOSXConnectFirstTdmGroupDS0_Type())
adGenAOSXConnectFirstTdmGroupDS0.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectFirstTdmGroupDS0.setStatus(_A)
class _AdGenAOSXConnectSecondIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,0),('dds',1),('t1E1',2),('eth',3),(_K,4),('shdsl',5),('fxs',6),(_L,7),('ppp',8)))
_AdGenAOSXConnectSecondIfType_Type.__name__=_C
_AdGenAOSXConnectSecondIfType_Object=MibTableColumn
adGenAOSXConnectSecondIfType=_AdGenAOSXConnectSecondIfType_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,9),_AdGenAOSXConnectSecondIfType_Type())
adGenAOSXConnectSecondIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondIfType.setStatus(_A)
class _AdGenAOSXConnectSecondIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_AdGenAOSXConnectSecondIfNumber_Type.__name__=_C
_AdGenAOSXConnectSecondIfNumber_Object=MibTableColumn
adGenAOSXConnectSecondIfNumber=_AdGenAOSXConnectSecondIfNumber_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,10),_AdGenAOSXConnectSecondIfNumber_Type())
adGenAOSXConnectSecondIfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondIfNumber.setStatus(_A)
class _AdGenAOSXConnectSecondSubIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1007))
_AdGenAOSXConnectSecondSubIfNumber_Type.__name__=_C
_AdGenAOSXConnectSecondSubIfNumber_Object=MibTableColumn
adGenAOSXConnectSecondSubIfNumber=_AdGenAOSXConnectSecondSubIfNumber_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,11),_AdGenAOSXConnectSecondSubIfNumber_Type())
adGenAOSXConnectSecondSubIfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondSubIfNumber.setStatus(_A)
class _AdGenAOSXConnectSecondIfSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenAOSXConnectSecondIfSlot_Type.__name__=_C
_AdGenAOSXConnectSecondIfSlot_Object=MibTableColumn
adGenAOSXConnectSecondIfSlot=_AdGenAOSXConnectSecondIfSlot_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,12),_AdGenAOSXConnectSecondIfSlot_Type())
adGenAOSXConnectSecondIfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondIfSlot.setStatus(_A)
class _AdGenAOSXConnectSecondIfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_AdGenAOSXConnectSecondIfPort_Type.__name__=_C
_AdGenAOSXConnectSecondIfPort_Object=MibTableColumn
adGenAOSXConnectSecondIfPort=_AdGenAOSXConnectSecondIfPort_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,13),_AdGenAOSXConnectSecondIfPort_Type())
adGenAOSXConnectSecondIfPort.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondIfPort.setStatus(_A)
class _AdGenAOSXConnectSecondTdmGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AdGenAOSXConnectSecondTdmGroup_Type.__name__=_C
_AdGenAOSXConnectSecondTdmGroup_Object=MibTableColumn
adGenAOSXConnectSecondTdmGroup=_AdGenAOSXConnectSecondTdmGroup_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,14),_AdGenAOSXConnectSecondTdmGroup_Type())
adGenAOSXConnectSecondTdmGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondTdmGroup.setStatus(_A)
class _AdGenAOSXConnectSecondTdmGroupDS0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AdGenAOSXConnectSecondTdmGroupDS0_Type.__name__=_C
_AdGenAOSXConnectSecondTdmGroupDS0_Object=MibTableColumn
adGenAOSXConnectSecondTdmGroupDS0=_AdGenAOSXConnectSecondTdmGroupDS0_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,15),_AdGenAOSXConnectSecondTdmGroupDS0_Type())
adGenAOSXConnectSecondTdmGroupDS0.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectSecondTdmGroupDS0.setStatus(_A)
class _AdGenAOSXConnectPreserveRbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AdGenAOSXConnectPreserveRbs_Type.__name__=_C
_AdGenAOSXConnectPreserveRbs_Object=MibTableColumn
adGenAOSXConnectPreserveRbs=_AdGenAOSXConnectPreserveRbs_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,16),_AdGenAOSXConnectPreserveRbs_Type())
adGenAOSXConnectPreserveRbs.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectPreserveRbs.setStatus(_A)
_AdGenAOSXConnectRowStatus_Type=RowStatus
_AdGenAOSXConnectRowStatus_Object=MibTableColumn
adGenAOSXConnectRowStatus=_AdGenAOSXConnectRowStatus_Object((1,3,6,1,4,1,664,5,53,1,5,1,1,1,17),_AdGenAOSXConnectRowStatus_Type())
adGenAOSXConnectRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenAOSXConnectRowStatus.setStatus(_A)
_AdGenAOSTdmGroup_ObjectIdentity=ObjectIdentity
adGenAOSTdmGroup=_AdGenAOSTdmGroup_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,5,2))
_AdGenAOSTdmGroupTable_Object=MibTable
adGenAOSTdmGroupTable=_AdGenAOSTdmGroupTable_Object((1,3,6,1,4,1,664,5,53,1,5,2,1))
if mibBuilder.loadTexts:adGenAOSTdmGroupTable.setStatus(_A)
_AdGenAOSTdmGroupEntry_Object=MibTableRow
adGenAOSTdmGroupEntry=_AdGenAOSTdmGroupEntry_Object((1,3,6,1,4,1,664,5,53,1,5,2,1,1))
adGenAOSTdmGroupEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:adGenAOSTdmGroupEntry.setStatus(_A)
class _AdGenAOSTdmGroupIfSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_AdGenAOSTdmGroupIfSlot_Type.__name__=_C
_AdGenAOSTdmGroupIfSlot_Object=MibTableColumn
adGenAOSTdmGroupIfSlot=_AdGenAOSTdmGroupIfSlot_Object((1,3,6,1,4,1,664,5,53,1,5,2,1,1,1),_AdGenAOSTdmGroupIfSlot_Type())
adGenAOSTdmGroupIfSlot.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenAOSTdmGroupIfSlot.setStatus(_A)
class _AdGenAOSTdmGroupIfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_AdGenAOSTdmGroupIfPort_Type.__name__=_C
_AdGenAOSTdmGroupIfPort_Object=MibTableColumn
adGenAOSTdmGroupIfPort=_AdGenAOSTdmGroupIfPort_Object((1,3,6,1,4,1,664,5,53,1,5,2,1,1,2),_AdGenAOSTdmGroupIfPort_Type())
adGenAOSTdmGroupIfPort.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenAOSTdmGroupIfPort.setStatus(_A)
class _AdGenAOSTdmGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAOSTdmGroupID_Type.__name__=_C
_AdGenAOSTdmGroupID_Object=MibTableColumn
adGenAOSTdmGroupID=_AdGenAOSTdmGroupID_Object((1,3,6,1,4,1,664,5,53,1,5,2,1,1,3),_AdGenAOSTdmGroupID_Type())
adGenAOSTdmGroupID.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenAOSTdmGroupID.setStatus(_A)
class _AdGenAOSTdmGroupMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_AdGenAOSTdmGroupMask_Type.__name__=_C
_AdGenAOSTdmGroupMask_Object=MibTableColumn
adGenAOSTdmGroupMask=_AdGenAOSTdmGroupMask_Object((1,3,6,1,4,1,664,5,53,1,5,2,1,1,4),_AdGenAOSTdmGroupMask_Type())
adGenAOSTdmGroupMask.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenAOSTdmGroupMask.setStatus(_A)
class _AdGenAOSTdmGroupUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fiftySixKbps',1),('sixtyFourKbps',2)))
_AdGenAOSTdmGroupUsage_Type.__name__=_C
_AdGenAOSTdmGroupUsage_Object=MibTableColumn
adGenAOSTdmGroupUsage=_AdGenAOSTdmGroupUsage_Object((1,3,6,1,4,1,664,5,53,1,5,2,1,1,5),_AdGenAOSTdmGroupUsage_Type())
adGenAOSTdmGroupUsage.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenAOSTdmGroupUsage.setStatus(_A)
_AdGenAOSMuxConformance_ObjectIdentity=ObjectIdentity
adGenAOSMuxConformance=_AdGenAOSMuxConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,5,99))
_AdGenAOSMuxCompliance_ObjectIdentity=ObjectIdentity
adGenAOSMuxCompliance=_AdGenAOSMuxCompliance_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,5,99,1))
_AdGenAOSMuxMibGroups_ObjectIdentity=ObjectIdentity
adGenAOSMuxMibGroups=_AdGenAOSMuxMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,5,99,2))
adGenAOSXConnectGrp=ObjectGroup((1,3,6,1,4,1,664,5,53,1,5,99,2,1))
adGenAOSXConnectGrp.setObjects(*((_B,_E),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:adGenAOSXConnectGrp.setStatus(_A)
adGenAOSTdmGroupGrp=ObjectGroup((1,3,6,1,4,1,664,5,53,1,5,99,2,2))
adGenAOSTdmGroupGrp.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:adGenAOSTdmGroupGrp.setStatus(_A)
adGenAOSMuxConformancemModule=ModuleCompliance((1,3,6,1,4,1,664,5,53,1,5,99,1,1))
adGenAOSMuxConformancemModule.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:adGenAOSMuxConformancemModule.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenAOSMux':adGenAOSMux,'adGenAOSXConnect':adGenAOSXConnect,'adGenAOSXConnectTable':adGenAOSXConnectTable,'adGenAOSXConnectEntry':adGenAOSXConnectEntry,_E:adGenAOSXConnectIndex,_N:adGenAOSXConnectFirstIfType,_O:adGenAOSXConnectFirstIfNumber,_P:adGenAOSXConnectFirstSubIfNumber,_Q:adGenAOSXConnectFirstIfSlot,_R:adGenAOSXConnectFirstIfPort,_S:adGenAOSXConnectFirstTdmGroup,_T:adGenAOSXConnectFirstTdmGroupDS0,_U:adGenAOSXConnectSecondIfType,_V:adGenAOSXConnectSecondIfNumber,_W:adGenAOSXConnectSecondSubIfNumber,_X:adGenAOSXConnectSecondIfSlot,_Y:adGenAOSXConnectSecondIfPort,_Z:adGenAOSXConnectSecondTdmGroup,_a:adGenAOSXConnectSecondTdmGroupDS0,_b:adGenAOSXConnectPreserveRbs,_c:adGenAOSXConnectRowStatus,'adGenAOSTdmGroup':adGenAOSTdmGroup,'adGenAOSTdmGroupTable':adGenAOSTdmGroupTable,'adGenAOSTdmGroupEntry':adGenAOSTdmGroupEntry,_F:adGenAOSTdmGroupIfSlot,_G:adGenAOSTdmGroupIfPort,_H:adGenAOSTdmGroupID,_d:adGenAOSTdmGroupMask,_e:adGenAOSTdmGroupUsage,'adGenAOSMuxConformance':adGenAOSMuxConformance,'adGenAOSMuxCompliance':adGenAOSMuxCompliance,'adGenAOSMuxConformancemModule':adGenAOSMuxConformancemModule,'adGenAOSMuxMibGroups':adGenAOSMuxMibGroups,_f:adGenAOSXConnectGrp,_g:adGenAOSTdmGroupGrp,'adGenAOSMuxID':adGenAOSMuxID})