_A6='zxAnDdnGhdbSlot'
_A5='zxAnDdnGhdbShelf'
_A4='zxAnDdnGhdbRack'
_A3='zxAnDdnModemDiagnosePort'
_A2='zxAnDdnModemDiagnoseSlot'
_A1='zxAnDdnModemDiagnoseShelf'
_A0='zxAnDdnModemDiagnoseRack'
_z='zxAnDdnModemQueryPort'
_y='zxAnDdnModemQuerySlot'
_x='zxAnDdnModemQueryShelf'
_w='zxAnDdnModemQueryRack'
_v='zxAnDdnModemPort'
_u='zxAnDdnModemSlot'
_t='zxAnDdnModemShelf'
_s='zxAnDdnModemRack'
_r='zxAnDdnBertStatsTs'
_q='zxAnDdnBertStatsCircuit'
_p='zxAnDdnBertStatsSlot'
_o='zxAnDdnBertStatsShelf'
_n='zxAnDdnBertStatsRack'
_m='zxAnDdnBertConfTs'
_l='zxAnDdnBertConfCircuit'
_k='zxAnDdnBertConfSlot'
_j='zxAnDdnBertConfShelf'
_i='zxAnDdnBertConfRack'
_h='audbPCTs'
_g='audbPCCircuit'
_f='audbPCSlot'
_e='audbPCShelf'
_d='audbPCRack'
_c='hdbPCSlot'
_b='hdbPCShelf'
_a='hdbPCRack'
_Z='ddnConPort1Ts'
_Y='ddnConPort1Circuit'
_X='ddnConPort1Slot'
_W='ddnConPort1Shelf'
_V='ddnConPort1Rack'
_U='ddnPortTs'
_T='ddnPortCircuit'
_S='ddnPortSlot'
_R='ddnPortShelf'
_Q='ddnPortRack'
_P='Unsigned32'
_O='OctetString'
_N='zxAnDdnModemOperStatus'
_M='zxAnDdnModemLineStatus'
_L='failed'
_K='success'
_J='inProgress'
_I='notStarted'
_H='DisplayString'
_G='read-write'
_F='read-only'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='ZTE-AN-DDN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnDDNMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
if mibBuilder.loadTexts:zxAnDDNMib.setRevisions(('2013-10-10 00:00',))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_MsagmajorVersion_ObjectIdentity=ObjectIdentity
msagmajorVersion=_MsagmajorVersion_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_MsagDDNConfig_ObjectIdentity=ObjectIdentity
msagDDNConfig=_MsagDDNConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,2))
_DdnPortTable_Object=MibTable
ddnPortTable=_DdnPortTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1))
if mibBuilder.loadTexts:ddnPortTable.setStatus(_A)
_DdnPortEntry_Object=MibTableRow
ddnPortEntry=_DdnPortEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1))
ddnPortEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ddnPortEntry.setStatus(_A)
class _DdnPortRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DdnPortRack_Type.__name__=_C
_DdnPortRack_Object=MibTableColumn
ddnPortRack=_DdnPortRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,1),_DdnPortRack_Type())
ddnPortRack.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnPortRack.setStatus(_A)
class _DdnPortShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_DdnPortShelf_Type.__name__=_C
_DdnPortShelf_Object=MibTableColumn
ddnPortShelf=_DdnPortShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,2),_DdnPortShelf_Type())
ddnPortShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnPortShelf.setStatus(_A)
class _DdnPortSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_DdnPortSlot_Type.__name__=_C
_DdnPortSlot_Object=MibTableColumn
ddnPortSlot=_DdnPortSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,3),_DdnPortSlot_Type())
ddnPortSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnPortSlot.setStatus(_A)
class _DdnPortCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_DdnPortCircuit_Type.__name__=_C
_DdnPortCircuit_Object=MibTableColumn
ddnPortCircuit=_DdnPortCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,4),_DdnPortCircuit_Type())
ddnPortCircuit.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnPortCircuit.setStatus(_A)
class _DdnPortTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DdnPortTs_Type.__name__=_C
_DdnPortTs_Object=MibTableColumn
ddnPortTs=_DdnPortTs_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,5),_DdnPortTs_Type())
ddnPortTs.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnPortTs.setStatus(_A)
class _DdnPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_DdnPortName_Type.__name__=_H
_DdnPortName_Object=MibTableColumn
ddnPortName=_DdnPortName_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,6),_DdnPortName_Type())
ddnPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnPortName.setStatus(_A)
class _DdnPortMainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('type64K',0),('type2B',1),('typeHSB',2),('typeSDM',3),('typeU',4),('typeHDB',5),('typeE1',6),('typePwe3',7),('typeShdsl',8)))
_DdnPortMainType_Type.__name__=_C
_DdnPortMainType_Object=MibTableColumn
ddnPortMainType=_DdnPortMainType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,7),_DdnPortMainType_Type())
ddnPortMainType.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnPortMainType.setStatus(_A)
class _DdnPortSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)));namedValues=NamedValues(*(('type1X64K',1),('type2X64K',2),('type3X64K',3),('type4X64K',4),('type5X64K',5),('type6X64K',6),('type7X64K',7),('type8X64K',8),('type9X64K',9),('type10X64K',10),('type11X64K',11),('type12X64K',12),('type13X64K',13),('type14X64K',14),('type15X64K',15),('type16X64K',16),('type17X64K',17),('type18X64K',18),('type19X64K',19),('type20X64K',20),('type21X64K',21),('type22X64K',22),('type23X64K',23),('type24X64K',24),('type25X64K',25),('type26X64K',26),('type27X64K',27),('type28X64K',28),('type29X64K',29),('type30X64K',30),('type31X64K',31),('type32X64K',32),('type24',33),('type48',34),('type96',35),('type192',36)))
_DdnPortSubType_Type.__name__=_C
_DdnPortSubType_Object=MibTableColumn
ddnPortSubType=_DdnPortSubType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,8),_DdnPortSubType_Type())
ddnPortSubType.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnPortSubType.setStatus(_A)
_DdnPortRowStatus_Type=RowStatus
_DdnPortRowStatus_Object=MibTableColumn
ddnPortRowStatus=_DdnPortRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,9),_DdnPortRowStatus_Type())
ddnPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnPortRowStatus.setStatus(_A)
class _DdnPortLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('noLoopback',1),('localLoopback',2),('remoteLineLoopback',3),('unsupported',255)))
_DdnPortLoopback_Type.__name__=_C
_DdnPortLoopback_Object=MibTableColumn
ddnPortLoopback=_DdnPortLoopback_Object((1,3,6,1,4,1,3902,1015,5200,3,2,1,1,10),_DdnPortLoopback_Type())
ddnPortLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnPortLoopback.setStatus(_A)
_DdnConnectTable_Object=MibTable
ddnConnectTable=_DdnConnectTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2))
if mibBuilder.loadTexts:ddnConnectTable.setStatus(_A)
_DdnConnectEntry_Object=MibTableRow
ddnConnectEntry=_DdnConnectEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1))
ddnConnectEntry.setIndexNames((0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:ddnConnectEntry.setStatus(_A)
class _DdnConPort1Rack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DdnConPort1Rack_Type.__name__=_C
_DdnConPort1Rack_Object=MibTableColumn
ddnConPort1Rack=_DdnConPort1Rack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,1),_DdnConPort1Rack_Type())
ddnConPort1Rack.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnConPort1Rack.setStatus(_A)
class _DdnConPort1Shelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_DdnConPort1Shelf_Type.__name__=_C
_DdnConPort1Shelf_Object=MibTableColumn
ddnConPort1Shelf=_DdnConPort1Shelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,2),_DdnConPort1Shelf_Type())
ddnConPort1Shelf.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnConPort1Shelf.setStatus(_A)
class _DdnConPort1Slot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_DdnConPort1Slot_Type.__name__=_C
_DdnConPort1Slot_Object=MibTableColumn
ddnConPort1Slot=_DdnConPort1Slot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,3),_DdnConPort1Slot_Type())
ddnConPort1Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnConPort1Slot.setStatus(_A)
class _DdnConPort1Circuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_DdnConPort1Circuit_Type.__name__=_C
_DdnConPort1Circuit_Object=MibTableColumn
ddnConPort1Circuit=_DdnConPort1Circuit_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,4),_DdnConPort1Circuit_Type())
ddnConPort1Circuit.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnConPort1Circuit.setStatus(_A)
class _DdnConPort1Ts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DdnConPort1Ts_Type.__name__=_C
_DdnConPort1Ts_Object=MibTableColumn
ddnConPort1Ts=_DdnConPort1Ts_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,5),_DdnConPort1Ts_Type())
ddnConPort1Ts.setMaxAccess(_D)
if mibBuilder.loadTexts:ddnConPort1Ts.setStatus(_A)
class _DdnConPort1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_DdnConPort1Name_Type.__name__=_H
_DdnConPort1Name_Object=MibTableColumn
ddnConPort1Name=_DdnConPort1Name_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,6),_DdnConPort1Name_Type())
ddnConPort1Name.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort1Name.setStatus(_A)
class _DdnConPort2Rack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DdnConPort2Rack_Type.__name__=_C
_DdnConPort2Rack_Object=MibTableColumn
ddnConPort2Rack=_DdnConPort2Rack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,7),_DdnConPort2Rack_Type())
ddnConPort2Rack.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort2Rack.setStatus(_A)
class _DdnConPort2Shelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_DdnConPort2Shelf_Type.__name__=_C
_DdnConPort2Shelf_Object=MibTableColumn
ddnConPort2Shelf=_DdnConPort2Shelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,8),_DdnConPort2Shelf_Type())
ddnConPort2Shelf.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort2Shelf.setStatus(_A)
class _DdnConPort2Slot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_DdnConPort2Slot_Type.__name__=_C
_DdnConPort2Slot_Object=MibTableColumn
ddnConPort2Slot=_DdnConPort2Slot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,9),_DdnConPort2Slot_Type())
ddnConPort2Slot.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort2Slot.setStatus(_A)
class _DdnConPort2Circuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_DdnConPort2Circuit_Type.__name__=_C
_DdnConPort2Circuit_Object=MibTableColumn
ddnConPort2Circuit=_DdnConPort2Circuit_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,10),_DdnConPort2Circuit_Type())
ddnConPort2Circuit.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort2Circuit.setStatus(_A)
class _DdnConPort2Ts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DdnConPort2Ts_Type.__name__=_C
_DdnConPort2Ts_Object=MibTableColumn
ddnConPort2Ts=_DdnConPort2Ts_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,11),_DdnConPort2Ts_Type())
ddnConPort2Ts.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort2Ts.setStatus(_A)
class _DdnConPort2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_DdnConPort2Name_Type.__name__=_H
_DdnConPort2Name_Object=MibTableColumn
ddnConPort2Name=_DdnConPort2Name_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,12),_DdnConPort2Name_Type())
ddnConPort2Name.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConPort2Name.setStatus(_A)
class _DdnConName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_DdnConName_Type.__name__=_H
_DdnConName_Object=MibTableColumn
ddnConName=_DdnConName_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,13),_DdnConName_Type())
ddnConName.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConName.setStatus(_A)
class _DdnConnExOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_DdnConnExOperType_Type.__name__=_C
_DdnConnExOperType_Object=MibTableColumn
ddnConnExOperType=_DdnConnExOperType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,14),_DdnConnExOperType_Type())
ddnConnExOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConnExOperType.setStatus(_A)
_DdnConRowStatus_Type=RowStatus
_DdnConRowStatus_Object=MibTableColumn
ddnConRowStatus=_DdnConRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,2,1,15),_DdnConRowStatus_Type())
ddnConRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ddnConRowStatus.setStatus(_A)
_HdbPortConfigTable_Object=MibTable
hdbPortConfigTable=_HdbPortConfigTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,3))
if mibBuilder.loadTexts:hdbPortConfigTable.setStatus(_A)
_HdbPortConfigEntry_Object=MibTableRow
hdbPortConfigEntry=_HdbPortConfigEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,3,1))
hdbPortConfigEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:hdbPortConfigEntry.setStatus(_A)
class _HdbPCRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_HdbPCRack_Type.__name__=_C
_HdbPCRack_Object=MibTableColumn
hdbPCRack=_HdbPCRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,3,1,1),_HdbPCRack_Type())
hdbPCRack.setMaxAccess(_D)
if mibBuilder.loadTexts:hdbPCRack.setStatus(_A)
class _HdbPCShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_HdbPCShelf_Type.__name__=_C
_HdbPCShelf_Object=MibTableColumn
hdbPCShelf=_HdbPCShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,3,1,2),_HdbPCShelf_Type())
hdbPCShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:hdbPCShelf.setStatus(_A)
class _HdbPCSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_HdbPCSlot_Type.__name__=_C
_HdbPCSlot_Object=MibTableColumn
hdbPCSlot=_HdbPCSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,3,1,3),_HdbPCSlot_Type())
hdbPCSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:hdbPCSlot.setStatus(_A)
class _HdbPCPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HdbPCPortNumber_Type.__name__=_C
_HdbPCPortNumber_Object=MibTableColumn
hdbPCPortNumber=_HdbPCPortNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,2,3,1,4),_HdbPCPortNumber_Type())
hdbPCPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hdbPCPortNumber.setStatus(_A)
_AudbPortConfigTable_Object=MibTable
audbPortConfigTable=_AudbPortConfigTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4))
if mibBuilder.loadTexts:audbPortConfigTable.setStatus(_A)
_AudbPortConfigEntry_Object=MibTableRow
audbPortConfigEntry=_AudbPortConfigEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1))
audbPortConfigEntry.setIndexNames((0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:audbPortConfigEntry.setStatus(_A)
class _AudbPCRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AudbPCRack_Type.__name__=_C
_AudbPCRack_Object=MibTableColumn
audbPCRack=_AudbPCRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,1),_AudbPCRack_Type())
audbPCRack.setMaxAccess(_D)
if mibBuilder.loadTexts:audbPCRack.setStatus(_A)
class _AudbPCShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AudbPCShelf_Type.__name__=_C
_AudbPCShelf_Object=MibTableColumn
audbPCShelf=_AudbPCShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,2),_AudbPCShelf_Type())
audbPCShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:audbPCShelf.setStatus(_A)
class _AudbPCSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_AudbPCSlot_Type.__name__=_C
_AudbPCSlot_Object=MibTableColumn
audbPCSlot=_AudbPCSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,3),_AudbPCSlot_Type())
audbPCSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:audbPCSlot.setStatus(_A)
class _AudbPCCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AudbPCCircuit_Type.__name__=_C
_AudbPCCircuit_Object=MibTableColumn
audbPCCircuit=_AudbPCCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,4),_AudbPCCircuit_Type())
audbPCCircuit.setMaxAccess(_D)
if mibBuilder.loadTexts:audbPCCircuit.setStatus(_A)
class _AudbPCTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(255,255))
_AudbPCTs_Type.__name__=_C
_AudbPCTs_Object=MibTableColumn
audbPCTs=_AudbPCTs_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,5),_AudbPCTs_Type())
audbPCTs.setMaxAccess(_D)
if mibBuilder.loadTexts:audbPCTs.setStatus(_A)
class _AudbPortLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twolinetrans',1),('fourlinetrans',2)))
_AudbPortLineType_Type.__name__=_C
_AudbPortLineType_Object=MibTableColumn
audbPortLineType=_AudbPortLineType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,9),_AudbPortLineType_Type())
audbPortLineType.setMaxAccess(_G)
if mibBuilder.loadTexts:audbPortLineType.setStatus(_A)
class _AudbPortInputGain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_AudbPortInputGain_Type.__name__=_H
_AudbPortInputGain_Object=MibTableColumn
audbPortInputGain=_AudbPortInputGain_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,10),_AudbPortInputGain_Type())
audbPortInputGain.setMaxAccess(_G)
if mibBuilder.loadTexts:audbPortInputGain.setStatus(_A)
class _AudbPortOutputGain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_AudbPortOutputGain_Type.__name__=_H
_AudbPortOutputGain_Object=MibTableColumn
audbPortOutputGain=_AudbPortOutputGain_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,11),_AudbPortOutputGain_Type())
audbPortOutputGain.setMaxAccess(_G)
if mibBuilder.loadTexts:audbPortOutputGain.setStatus(_A)
class _AudbPortLoopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loop',1),('notloop',2)))
_AudbPortLoopState_Type.__name__=_C
_AudbPortLoopState_Object=MibTableColumn
audbPortLoopState=_AudbPortLoopState_Object((1,3,6,1,4,1,3902,1015,5200,3,2,4,1,12),_AudbPortLoopState_Type())
audbPortLoopState.setMaxAccess(_G)
if mibBuilder.loadTexts:audbPortLoopState.setStatus(_A)
_ZxAnDdnBertMgmtGroup_ObjectIdentity=ObjectIdentity
zxAnDdnBertMgmtGroup=_ZxAnDdnBertMgmtGroup_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,2,5))
_ZxAnDdnBertConfTable_Object=MibTable
zxAnDdnBertConfTable=_ZxAnDdnBertConfTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1))
if mibBuilder.loadTexts:zxAnDdnBertConfTable.setStatus(_A)
_ZxAnDdnBertConfEntry_Object=MibTableRow
zxAnDdnBertConfEntry=_ZxAnDdnBertConfEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1))
zxAnDdnBertConfEntry.setIndexNames((0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:zxAnDdnBertConfEntry.setStatus(_A)
_ZxAnDdnBertConfRack_Type=Integer32
_ZxAnDdnBertConfRack_Object=MibTableColumn
zxAnDdnBertConfRack=_ZxAnDdnBertConfRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,1),_ZxAnDdnBertConfRack_Type())
zxAnDdnBertConfRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertConfRack.setStatus(_A)
_ZxAnDdnBertConfShelf_Type=Integer32
_ZxAnDdnBertConfShelf_Object=MibTableColumn
zxAnDdnBertConfShelf=_ZxAnDdnBertConfShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,2),_ZxAnDdnBertConfShelf_Type())
zxAnDdnBertConfShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertConfShelf.setStatus(_A)
_ZxAnDdnBertConfSlot_Type=Integer32
_ZxAnDdnBertConfSlot_Object=MibTableColumn
zxAnDdnBertConfSlot=_ZxAnDdnBertConfSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,3),_ZxAnDdnBertConfSlot_Type())
zxAnDdnBertConfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertConfSlot.setStatus(_A)
_ZxAnDdnBertConfCircuit_Type=Integer32
_ZxAnDdnBertConfCircuit_Object=MibTableColumn
zxAnDdnBertConfCircuit=_ZxAnDdnBertConfCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,4),_ZxAnDdnBertConfCircuit_Type())
zxAnDdnBertConfCircuit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertConfCircuit.setStatus(_A)
_ZxAnDdnBertConfTs_Type=Integer32
_ZxAnDdnBertConfTs_Object=MibTableColumn
zxAnDdnBertConfTs=_ZxAnDdnBertConfTs_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,5),_ZxAnDdnBertConfTs_Type())
zxAnDdnBertConfTs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertConfTs.setStatus(_A)
class _ZxAnDdnBertAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxAnDdnBertAction_Type.__name__=_C
_ZxAnDdnBertAction_Object=MibTableColumn
zxAnDdnBertAction=_ZxAnDdnBertAction_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,6),_ZxAnDdnBertAction_Type())
zxAnDdnBertAction.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertAction.setStatus(_A)
class _ZxAnDdnBertTestPattern_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,20)));namedValues=NamedValues(*(('twoE9MinusOne',1),('twoE11MinusOne',2),('twoE15MinusOne',3),('twoE20MinusOne',4),('twoE23MinusOne',5),('userPattern',20)))
_ZxAnDdnBertTestPattern_Type.__name__=_C
_ZxAnDdnBertTestPattern_Object=MibTableColumn
zxAnDdnBertTestPattern=_ZxAnDdnBertTestPattern_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,7),_ZxAnDdnBertTestPattern_Type())
zxAnDdnBertTestPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertTestPattern.setStatus(_A)
class _ZxAnDdnBertUserPattern_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_ZxAnDdnBertUserPattern_Type.__name__=_O
_ZxAnDdnBertUserPattern_Object=MibTableColumn
zxAnDdnBertUserPattern=_ZxAnDdnBertUserPattern_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,8),_ZxAnDdnBertUserPattern_Type())
zxAnDdnBertUserPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertUserPattern.setStatus(_A)
class _ZxAnDdnBertMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('break',1),('monitor',2)))
_ZxAnDdnBertMode_Type.__name__=_C
_ZxAnDdnBertMode_Object=MibTableColumn
zxAnDdnBertMode=_ZxAnDdnBertMode_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,9),_ZxAnDdnBertMode_Type())
zxAnDdnBertMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertMode.setStatus(_A)
class _ZxAnDdnBertDuration_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2880))
_ZxAnDdnBertDuration_Type.__name__=_C
_ZxAnDdnBertDuration_Object=MibTableColumn
zxAnDdnBertDuration=_ZxAnDdnBertDuration_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,10),_ZxAnDdnBertDuration_Type())
zxAnDdnBertDuration.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnDdnBertDuration.setUnits('Minutes')
class _ZxAnDdnBertStartDateAndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnDdnBertStartDateAndTime_Type.__name__=_H
_ZxAnDdnBertStartDateAndTime_Object=MibTableColumn
zxAnDdnBertStartDateAndTime=_ZxAnDdnBertStartDateAndTime_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,11),_ZxAnDdnBertStartDateAndTime_Type())
zxAnDdnBertStartDateAndTime.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertStartDateAndTime.setStatus(_A)
class _ZxAnDdnBertOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_ZxAnDdnBertOperStatus_Type.__name__=_C
_ZxAnDdnBertOperStatus_Object=MibTableColumn
zxAnDdnBertOperStatus=_ZxAnDdnBertOperStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,12),_ZxAnDdnBertOperStatus_Type())
zxAnDdnBertOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertOperStatus.setStatus(_A)
class _ZxAnDdnBertTargetType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('link',2)))
_ZxAnDdnBertTargetType_Type.__name__=_C
_ZxAnDdnBertTargetType_Object=MibTableColumn
zxAnDdnBertTargetType=_ZxAnDdnBertTargetType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,13),_ZxAnDdnBertTargetType_Type())
zxAnDdnBertTargetType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertTargetType.setStatus(_A)
_ZxAnDdnBertRowStatus_Type=RowStatus
_ZxAnDdnBertRowStatus_Object=MibTableColumn
zxAnDdnBertRowStatus=_ZxAnDdnBertRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,1,1,20),_ZxAnDdnBertRowStatus_Type())
zxAnDdnBertRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnDdnBertRowStatus.setStatus(_A)
_ZxAnDdnBertStatsTable_Object=MibTable
zxAnDdnBertStatsTable=_ZxAnDdnBertStatsTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2))
if mibBuilder.loadTexts:zxAnDdnBertStatsTable.setStatus(_A)
_ZxAnDdnBertStatsEntry_Object=MibTableRow
zxAnDdnBertStatsEntry=_ZxAnDdnBertStatsEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1))
zxAnDdnBertStatsEntry.setIndexNames((0,_B,_n),(0,_B,_o),(0,_B,_p),(0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:zxAnDdnBertStatsEntry.setStatus(_A)
_ZxAnDdnBertStatsRack_Type=Integer32
_ZxAnDdnBertStatsRack_Object=MibTableColumn
zxAnDdnBertStatsRack=_ZxAnDdnBertStatsRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,1),_ZxAnDdnBertStatsRack_Type())
zxAnDdnBertStatsRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertStatsRack.setStatus(_A)
_ZxAnDdnBertStatsShelf_Type=Integer32
_ZxAnDdnBertStatsShelf_Object=MibTableColumn
zxAnDdnBertStatsShelf=_ZxAnDdnBertStatsShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,2),_ZxAnDdnBertStatsShelf_Type())
zxAnDdnBertStatsShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertStatsShelf.setStatus(_A)
_ZxAnDdnBertStatsSlot_Type=Integer32
_ZxAnDdnBertStatsSlot_Object=MibTableColumn
zxAnDdnBertStatsSlot=_ZxAnDdnBertStatsSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,3),_ZxAnDdnBertStatsSlot_Type())
zxAnDdnBertStatsSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertStatsSlot.setStatus(_A)
_ZxAnDdnBertStatsCircuit_Type=Integer32
_ZxAnDdnBertStatsCircuit_Object=MibTableColumn
zxAnDdnBertStatsCircuit=_ZxAnDdnBertStatsCircuit_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,4),_ZxAnDdnBertStatsCircuit_Type())
zxAnDdnBertStatsCircuit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertStatsCircuit.setStatus(_A)
_ZxAnDdnBertStatsTs_Type=Integer32
_ZxAnDdnBertStatsTs_Object=MibTableColumn
zxAnDdnBertStatsTs=_ZxAnDdnBertStatsTs_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,5),_ZxAnDdnBertStatsTs_Type())
zxAnDdnBertStatsTs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnBertStatsTs.setStatus(_A)
_ZxAnDdnBertRxTotalBits_Type=Counter64
_ZxAnDdnBertRxTotalBits_Object=MibTableColumn
zxAnDdnBertRxTotalBits=_ZxAnDdnBertRxTotalBits_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,6),_ZxAnDdnBertRxTotalBits_Type())
zxAnDdnBertRxTotalBits.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertRxTotalBits.setStatus(_A)
_ZxAnDdnBertRxErrorBits_Type=Counter32
_ZxAnDdnBertRxErrorBits_Object=MibTableColumn
zxAnDdnBertRxErrorBits=_ZxAnDdnBertRxErrorBits_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,7),_ZxAnDdnBertRxErrorBits_Type())
zxAnDdnBertRxErrorBits.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertRxErrorBits.setStatus(_A)
class _ZxAnDdnBertRxBitErrorRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnDdnBertRxBitErrorRatio_Type.__name__=_P
_ZxAnDdnBertRxBitErrorRatio_Object=MibTableColumn
zxAnDdnBertRxBitErrorRatio=_ZxAnDdnBertRxBitErrorRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,8),_ZxAnDdnBertRxBitErrorRatio_Type())
zxAnDdnBertRxBitErrorRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertRxBitErrorRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnDdnBertRxBitErrorRatio.setUnits('percents')
_ZxAnDdnBertTimeElapsed_Type=Integer32
_ZxAnDdnBertTimeElapsed_Object=MibTableColumn
zxAnDdnBertTimeElapsed=_ZxAnDdnBertTimeElapsed_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,9),_ZxAnDdnBertTimeElapsed_Type())
zxAnDdnBertTimeElapsed.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:zxAnDdnBertTimeElapsed.setUnits('seconds')
_ZxAnDdnBertEs_Type=Counter32
_ZxAnDdnBertEs_Object=MibTableColumn
zxAnDdnBertEs=_ZxAnDdnBertEs_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,10),_ZxAnDdnBertEs_Type())
zxAnDdnBertEs.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertEs.setStatus(_A)
_ZxAnDdnBertSes_Type=Counter32
_ZxAnDdnBertSes_Object=MibTableColumn
zxAnDdnBertSes=_ZxAnDdnBertSes_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,11),_ZxAnDdnBertSes_Type())
zxAnDdnBertSes.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertSes.setStatus(_A)
_ZxAnDdnBertUas_Type=Counter32
_ZxAnDdnBertUas_Object=MibTableColumn
zxAnDdnBertUas=_ZxAnDdnBertUas_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,12),_ZxAnDdnBertUas_Type())
zxAnDdnBertUas.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertUas.setStatus(_A)
_ZxAnDdnBertDm_Type=Counter32
_ZxAnDdnBertDm_Object=MibTableColumn
zxAnDdnBertDm=_ZxAnDdnBertDm_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,13),_ZxAnDdnBertDm_Type())
zxAnDdnBertDm.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertDm.setStatus(_A)
_ZxAnDdnBertBbe_Type=Counter32
_ZxAnDdnBertBbe_Object=MibTableColumn
zxAnDdnBertBbe=_ZxAnDdnBertBbe_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,14),_ZxAnDdnBertBbe_Type())
zxAnDdnBertBbe.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertBbe.setStatus(_A)
_ZxAnDdnBertCses_Type=Counter32
_ZxAnDdnBertCses_Object=MibTableColumn
zxAnDdnBertCses=_ZxAnDdnBertCses_Object((1,3,6,1,4,1,3902,1015,5200,3,2,5,2,1,15),_ZxAnDdnBertCses_Type())
zxAnDdnBertCses.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnBertCses.setStatus(_A)
_ZxAnDdnModemMgmtGroup_ObjectIdentity=ObjectIdentity
zxAnDdnModemMgmtGroup=_ZxAnDdnModemMgmtGroup_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,2,7))
_ZxAnDdnModemMgmtTable_Object=MibTable
zxAnDdnModemMgmtTable=_ZxAnDdnModemMgmtTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1))
if mibBuilder.loadTexts:zxAnDdnModemMgmtTable.setStatus(_A)
_ZxAnDdnModemMgmtEntry_Object=MibTableRow
zxAnDdnModemMgmtEntry=_ZxAnDdnModemMgmtEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1))
zxAnDdnModemMgmtEntry.setIndexNames((0,_B,_s),(0,_B,_t),(0,_B,_u),(0,_B,_v))
if mibBuilder.loadTexts:zxAnDdnModemMgmtEntry.setStatus(_A)
_ZxAnDdnModemRack_Type=Integer32
_ZxAnDdnModemRack_Object=MibTableColumn
zxAnDdnModemRack=_ZxAnDdnModemRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,1),_ZxAnDdnModemRack_Type())
zxAnDdnModemRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemRack.setStatus(_A)
_ZxAnDdnModemShelf_Type=Integer32
_ZxAnDdnModemShelf_Object=MibTableColumn
zxAnDdnModemShelf=_ZxAnDdnModemShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,2),_ZxAnDdnModemShelf_Type())
zxAnDdnModemShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemShelf.setStatus(_A)
_ZxAnDdnModemSlot_Type=Integer32
_ZxAnDdnModemSlot_Object=MibTableColumn
zxAnDdnModemSlot=_ZxAnDdnModemSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,3),_ZxAnDdnModemSlot_Type())
zxAnDdnModemSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemSlot.setStatus(_A)
_ZxAnDdnModemPort_Type=Integer32
_ZxAnDdnModemPort_Object=MibTableColumn
zxAnDdnModemPort=_ZxAnDdnModemPort_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,4),_ZxAnDdnModemPort_Type())
zxAnDdnModemPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemPort.setStatus(_A)
class _ZxAnDdnModemOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_ZxAnDdnModemOperStatus_Type.__name__=_C
_ZxAnDdnModemOperStatus_Object=MibTableColumn
zxAnDdnModemOperStatus=_ZxAnDdnModemOperStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,5),_ZxAnDdnModemOperStatus_Type())
zxAnDdnModemOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnModemOperStatus.setStatus(_A)
_ZxAnDdnModemConfigData_Type=DisplayString
_ZxAnDdnModemConfigData_Object=MibTableColumn
zxAnDdnModemConfigData=_ZxAnDdnModemConfigData_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,6),_ZxAnDdnModemConfigData_Type())
zxAnDdnModemConfigData.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDdnModemConfigData.setStatus(_A)
class _ZxAnDdnModemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_ZxAnDdnModemReset_Type.__name__=_C
_ZxAnDdnModemReset_Object=MibTableColumn
zxAnDdnModemReset=_ZxAnDdnModemReset_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,7),_ZxAnDdnModemReset_Type())
zxAnDdnModemReset.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDdnModemReset.setStatus(_A)
class _ZxAnDdnModemSaveData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('saveData',1))
_ZxAnDdnModemSaveData_Type.__name__=_C
_ZxAnDdnModemSaveData_Object=MibTableColumn
zxAnDdnModemSaveData=_ZxAnDdnModemSaveData_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,8),_ZxAnDdnModemSaveData_Type())
zxAnDdnModemSaveData.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDdnModemSaveData.setStatus(_A)
class _ZxAnDdnModemLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,12,13,14,21)));namedValues=NamedValues(*(('shdslSnrMarginCrossing',1),('shdslLoopAttenCrossing',2),('shdslLossOfSyncWord',3),('e1LossOfSignal',11),('e1LossOfFrame',12),('e1CrcError',13),('v35IfConnectionBroken',14),('dteIfConnectionBroken',21)))
_ZxAnDdnModemLineStatus_Type.__name__=_C
_ZxAnDdnModemLineStatus_Object=MibTableColumn
zxAnDdnModemLineStatus=_ZxAnDdnModemLineStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,1,1,9),_ZxAnDdnModemLineStatus_Type())
zxAnDdnModemLineStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnModemLineStatus.setStatus(_A)
_ZxAnDdnModemQueryTable_Object=MibTable
zxAnDdnModemQueryTable=_ZxAnDdnModemQueryTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2))
if mibBuilder.loadTexts:zxAnDdnModemQueryTable.setStatus(_A)
_ZxAnDdnModemQueryEntry_Object=MibTableRow
zxAnDdnModemQueryEntry=_ZxAnDdnModemQueryEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1))
zxAnDdnModemQueryEntry.setIndexNames((0,_B,_w),(0,_B,_x),(0,_B,_y),(0,_B,_z))
if mibBuilder.loadTexts:zxAnDdnModemQueryEntry.setStatus(_A)
_ZxAnDdnModemQueryRack_Type=Integer32
_ZxAnDdnModemQueryRack_Object=MibTableColumn
zxAnDdnModemQueryRack=_ZxAnDdnModemQueryRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,1),_ZxAnDdnModemQueryRack_Type())
zxAnDdnModemQueryRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemQueryRack.setStatus(_A)
_ZxAnDdnModemQueryShelf_Type=Integer32
_ZxAnDdnModemQueryShelf_Object=MibTableColumn
zxAnDdnModemQueryShelf=_ZxAnDdnModemQueryShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,2),_ZxAnDdnModemQueryShelf_Type())
zxAnDdnModemQueryShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemQueryShelf.setStatus(_A)
_ZxAnDdnModemQuerySlot_Type=Integer32
_ZxAnDdnModemQuerySlot_Object=MibTableColumn
zxAnDdnModemQuerySlot=_ZxAnDdnModemQuerySlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,3),_ZxAnDdnModemQuerySlot_Type())
zxAnDdnModemQuerySlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemQuerySlot.setStatus(_A)
_ZxAnDdnModemQueryPort_Type=Integer32
_ZxAnDdnModemQueryPort_Object=MibTableColumn
zxAnDdnModemQueryPort=_ZxAnDdnModemQueryPort_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,4),_ZxAnDdnModemQueryPort_Type())
zxAnDdnModemQueryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemQueryPort.setStatus(_A)
class _ZxAnDdnModemQueryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('config',1),('perf',2)))
_ZxAnDdnModemQueryType_Type.__name__=_C
_ZxAnDdnModemQueryType_Object=MibTableColumn
zxAnDdnModemQueryType=_ZxAnDdnModemQueryType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,5),_ZxAnDdnModemQueryType_Type())
zxAnDdnModemQueryType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDdnModemQueryType.setStatus(_A)
class _ZxAnDdnModemQueryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_ZxAnDdnModemQueryStatus_Type.__name__=_C
_ZxAnDdnModemQueryStatus_Object=MibTableColumn
zxAnDdnModemQueryStatus=_ZxAnDdnModemQueryStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,6),_ZxAnDdnModemQueryStatus_Type())
zxAnDdnModemQueryStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnModemQueryStatus.setStatus(_A)
_ZxAnDdnModemQueryResult_Type=DisplayString
_ZxAnDdnModemQueryResult_Object=MibTableColumn
zxAnDdnModemQueryResult=_ZxAnDdnModemQueryResult_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,2,1,7),_ZxAnDdnModemQueryResult_Type())
zxAnDdnModemQueryResult.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnModemQueryResult.setStatus(_A)
_ZxAnDdnModemDiagnoseTable_Object=MibTable
zxAnDdnModemDiagnoseTable=_ZxAnDdnModemDiagnoseTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3))
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseTable.setStatus(_A)
_ZxAnDdnModemDiagnoseEntry_Object=MibTableRow
zxAnDdnModemDiagnoseEntry=_ZxAnDdnModemDiagnoseEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1))
zxAnDdnModemDiagnoseEntry.setIndexNames((0,_B,_A0),(0,_B,_A1),(0,_B,_A2),(0,_B,_A3))
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseEntry.setStatus(_A)
_ZxAnDdnModemDiagnoseRack_Type=Integer32
_ZxAnDdnModemDiagnoseRack_Object=MibTableColumn
zxAnDdnModemDiagnoseRack=_ZxAnDdnModemDiagnoseRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1,1),_ZxAnDdnModemDiagnoseRack_Type())
zxAnDdnModemDiagnoseRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseRack.setStatus(_A)
_ZxAnDdnModemDiagnoseShelf_Type=Integer32
_ZxAnDdnModemDiagnoseShelf_Object=MibTableColumn
zxAnDdnModemDiagnoseShelf=_ZxAnDdnModemDiagnoseShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1,2),_ZxAnDdnModemDiagnoseShelf_Type())
zxAnDdnModemDiagnoseShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseShelf.setStatus(_A)
_ZxAnDdnModemDiagnoseSlot_Type=Integer32
_ZxAnDdnModemDiagnoseSlot_Object=MibTableColumn
zxAnDdnModemDiagnoseSlot=_ZxAnDdnModemDiagnoseSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1,3),_ZxAnDdnModemDiagnoseSlot_Type())
zxAnDdnModemDiagnoseSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseSlot.setStatus(_A)
_ZxAnDdnModemDiagnosePort_Type=Integer32
_ZxAnDdnModemDiagnosePort_Object=MibTableColumn
zxAnDdnModemDiagnosePort=_ZxAnDdnModemDiagnosePort_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1,4),_ZxAnDdnModemDiagnosePort_Type())
zxAnDdnModemDiagnosePort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnModemDiagnosePort.setStatus(_A)
class _ZxAnDdnModemDiagnoseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('selfDiagnose',1))
_ZxAnDdnModemDiagnoseType_Type.__name__=_C
_ZxAnDdnModemDiagnoseType_Object=MibTableColumn
zxAnDdnModemDiagnoseType=_ZxAnDdnModemDiagnoseType_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1,5),_ZxAnDdnModemDiagnoseType_Type())
zxAnDdnModemDiagnoseType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseType.setStatus(_A)
class _ZxAnDdnModemDiagnoseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4)))
_ZxAnDdnModemDiagnoseStatus_Type.__name__=_C
_ZxAnDdnModemDiagnoseStatus_Object=MibTableColumn
zxAnDdnModemDiagnoseStatus=_ZxAnDdnModemDiagnoseStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,2,7,3,1,6),_ZxAnDdnModemDiagnoseStatus_Type())
zxAnDdnModemDiagnoseStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDdnModemDiagnoseStatus.setStatus(_A)
_ZxAnDdnGhdbCardTable_Object=MibTable
zxAnDdnGhdbCardTable=_ZxAnDdnGhdbCardTable_Object((1,3,6,1,4,1,3902,1015,5200,3,2,8))
if mibBuilder.loadTexts:zxAnDdnGhdbCardTable.setStatus(_A)
_ZxAnDdnGhdbCardEntry_Object=MibTableRow
zxAnDdnGhdbCardEntry=_ZxAnDdnGhdbCardEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,2,8,1))
zxAnDdnGhdbCardEntry.setIndexNames((0,_B,_A4),(0,_B,_A5),(0,_B,_A6))
if mibBuilder.loadTexts:zxAnDdnGhdbCardEntry.setStatus(_A)
_ZxAnDdnGhdbRack_Type=Integer32
_ZxAnDdnGhdbRack_Object=MibTableColumn
zxAnDdnGhdbRack=_ZxAnDdnGhdbRack_Object((1,3,6,1,4,1,3902,1015,5200,3,2,8,1,1),_ZxAnDdnGhdbRack_Type())
zxAnDdnGhdbRack.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnGhdbRack.setStatus(_A)
_ZxAnDdnGhdbShelf_Type=Integer32
_ZxAnDdnGhdbShelf_Object=MibTableColumn
zxAnDdnGhdbShelf=_ZxAnDdnGhdbShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,2,8,1,2),_ZxAnDdnGhdbShelf_Type())
zxAnDdnGhdbShelf.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnGhdbShelf.setStatus(_A)
_ZxAnDdnGhdbSlot_Type=Integer32
_ZxAnDdnGhdbSlot_Object=MibTableColumn
zxAnDdnGhdbSlot=_ZxAnDdnGhdbSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,2,8,1,3),_ZxAnDdnGhdbSlot_Type())
zxAnDdnGhdbSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDdnGhdbSlot.setStatus(_A)
class _ZxAnDdnGhdbWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('tdm',1),('e1Transparent',2),('narrowbandConvergence',3),('cesopsn',4),('satop',5),('mixed',6)))
_ZxAnDdnGhdbWorkMode_Type.__name__=_C
_ZxAnDdnGhdbWorkMode_Object=MibTableColumn
zxAnDdnGhdbWorkMode=_ZxAnDdnGhdbWorkMode_Object((1,3,6,1,4,1,3902,1015,5200,3,2,8,1,4),_ZxAnDdnGhdbWorkMode_Type())
zxAnDdnGhdbWorkMode.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnDdnGhdbWorkMode.setStatus(_A)
_ZxAnDdnTrapObjects_ObjectIdentity=ObjectIdentity
zxAnDdnTrapObjects=_ZxAnDdnTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,2,100))
_ZxAnDdnModemTrapGroup_ObjectIdentity=ObjectIdentity
zxAnDdnModemTrapGroup=_ZxAnDdnModemTrapGroup_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,2,100,1))
zxAnDdnModemLineStatusAbnormal=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,2,100,1,1))
zxAnDdnModemLineStatusAbnormal.setObjects((_B,_M))
if mibBuilder.loadTexts:zxAnDdnModemLineStatusAbnormal.setStatus(_A)
zxAnDdnModemLineStatusNormal=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,2,100,1,2))
zxAnDdnModemLineStatusNormal.setObjects((_B,_M))
if mibBuilder.loadTexts:zxAnDdnModemLineStatusNormal.setStatus(_A)
zxAnDdnPortLinkDown=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,2,100,1,3))
zxAnDdnPortLinkDown.setObjects((_B,_N))
if mibBuilder.loadTexts:zxAnDdnPortLinkDown.setStatus(_A)
zxAnDdnPortLinkUp=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,2,100,1,4))
zxAnDdnPortLinkUp.setObjects((_B,_N))
if mibBuilder.loadTexts:zxAnDdnPortLinkUp.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zte':zte,'zxAn':zxAn,'zxAnDDNMib':zxAnDDNMib,'msagmajorVersion':msagmajorVersion,'msagDDNConfig':msagDDNConfig,'ddnPortTable':ddnPortTable,'ddnPortEntry':ddnPortEntry,_Q:ddnPortRack,_R:ddnPortShelf,_S:ddnPortSlot,_T:ddnPortCircuit,_U:ddnPortTs,'ddnPortName':ddnPortName,'ddnPortMainType':ddnPortMainType,'ddnPortSubType':ddnPortSubType,'ddnPortRowStatus':ddnPortRowStatus,'ddnPortLoopback':ddnPortLoopback,'ddnConnectTable':ddnConnectTable,'ddnConnectEntry':ddnConnectEntry,_V:ddnConPort1Rack,_W:ddnConPort1Shelf,_X:ddnConPort1Slot,_Y:ddnConPort1Circuit,_Z:ddnConPort1Ts,'ddnConPort1Name':ddnConPort1Name,'ddnConPort2Rack':ddnConPort2Rack,'ddnConPort2Shelf':ddnConPort2Shelf,'ddnConPort2Slot':ddnConPort2Slot,'ddnConPort2Circuit':ddnConPort2Circuit,'ddnConPort2Ts':ddnConPort2Ts,'ddnConPort2Name':ddnConPort2Name,'ddnConName':ddnConName,'ddnConnExOperType':ddnConnExOperType,'ddnConRowStatus':ddnConRowStatus,'hdbPortConfigTable':hdbPortConfigTable,'hdbPortConfigEntry':hdbPortConfigEntry,_a:hdbPCRack,_b:hdbPCShelf,_c:hdbPCSlot,'hdbPCPortNumber':hdbPCPortNumber,'audbPortConfigTable':audbPortConfigTable,'audbPortConfigEntry':audbPortConfigEntry,_d:audbPCRack,_e:audbPCShelf,_f:audbPCSlot,_g:audbPCCircuit,_h:audbPCTs,'audbPortLineType':audbPortLineType,'audbPortInputGain':audbPortInputGain,'audbPortOutputGain':audbPortOutputGain,'audbPortLoopState':audbPortLoopState,'zxAnDdnBertMgmtGroup':zxAnDdnBertMgmtGroup,'zxAnDdnBertConfTable':zxAnDdnBertConfTable,'zxAnDdnBertConfEntry':zxAnDdnBertConfEntry,_i:zxAnDdnBertConfRack,_j:zxAnDdnBertConfShelf,_k:zxAnDdnBertConfSlot,_l:zxAnDdnBertConfCircuit,_m:zxAnDdnBertConfTs,'zxAnDdnBertAction':zxAnDdnBertAction,'zxAnDdnBertTestPattern':zxAnDdnBertTestPattern,'zxAnDdnBertUserPattern':zxAnDdnBertUserPattern,'zxAnDdnBertMode':zxAnDdnBertMode,'zxAnDdnBertDuration':zxAnDdnBertDuration,'zxAnDdnBertStartDateAndTime':zxAnDdnBertStartDateAndTime,'zxAnDdnBertOperStatus':zxAnDdnBertOperStatus,'zxAnDdnBertTargetType':zxAnDdnBertTargetType,'zxAnDdnBertRowStatus':zxAnDdnBertRowStatus,'zxAnDdnBertStatsTable':zxAnDdnBertStatsTable,'zxAnDdnBertStatsEntry':zxAnDdnBertStatsEntry,_n:zxAnDdnBertStatsRack,_o:zxAnDdnBertStatsShelf,_p:zxAnDdnBertStatsSlot,_q:zxAnDdnBertStatsCircuit,_r:zxAnDdnBertStatsTs,'zxAnDdnBertRxTotalBits':zxAnDdnBertRxTotalBits,'zxAnDdnBertRxErrorBits':zxAnDdnBertRxErrorBits,'zxAnDdnBertRxBitErrorRatio':zxAnDdnBertRxBitErrorRatio,'zxAnDdnBertTimeElapsed':zxAnDdnBertTimeElapsed,'zxAnDdnBertEs':zxAnDdnBertEs,'zxAnDdnBertSes':zxAnDdnBertSes,'zxAnDdnBertUas':zxAnDdnBertUas,'zxAnDdnBertDm':zxAnDdnBertDm,'zxAnDdnBertBbe':zxAnDdnBertBbe,'zxAnDdnBertCses':zxAnDdnBertCses,'zxAnDdnModemMgmtGroup':zxAnDdnModemMgmtGroup,'zxAnDdnModemMgmtTable':zxAnDdnModemMgmtTable,'zxAnDdnModemMgmtEntry':zxAnDdnModemMgmtEntry,_s:zxAnDdnModemRack,_t:zxAnDdnModemShelf,_u:zxAnDdnModemSlot,_v:zxAnDdnModemPort,_N:zxAnDdnModemOperStatus,'zxAnDdnModemConfigData':zxAnDdnModemConfigData,'zxAnDdnModemReset':zxAnDdnModemReset,'zxAnDdnModemSaveData':zxAnDdnModemSaveData,_M:zxAnDdnModemLineStatus,'zxAnDdnModemQueryTable':zxAnDdnModemQueryTable,'zxAnDdnModemQueryEntry':zxAnDdnModemQueryEntry,_w:zxAnDdnModemQueryRack,_x:zxAnDdnModemQueryShelf,_y:zxAnDdnModemQuerySlot,_z:zxAnDdnModemQueryPort,'zxAnDdnModemQueryType':zxAnDdnModemQueryType,'zxAnDdnModemQueryStatus':zxAnDdnModemQueryStatus,'zxAnDdnModemQueryResult':zxAnDdnModemQueryResult,'zxAnDdnModemDiagnoseTable':zxAnDdnModemDiagnoseTable,'zxAnDdnModemDiagnoseEntry':zxAnDdnModemDiagnoseEntry,_A0:zxAnDdnModemDiagnoseRack,_A1:zxAnDdnModemDiagnoseShelf,_A2:zxAnDdnModemDiagnoseSlot,_A3:zxAnDdnModemDiagnosePort,'zxAnDdnModemDiagnoseType':zxAnDdnModemDiagnoseType,'zxAnDdnModemDiagnoseStatus':zxAnDdnModemDiagnoseStatus,'zxAnDdnGhdbCardTable':zxAnDdnGhdbCardTable,'zxAnDdnGhdbCardEntry':zxAnDdnGhdbCardEntry,_A4:zxAnDdnGhdbRack,_A5:zxAnDdnGhdbShelf,_A6:zxAnDdnGhdbSlot,'zxAnDdnGhdbWorkMode':zxAnDdnGhdbWorkMode,'zxAnDdnTrapObjects':zxAnDdnTrapObjects,'zxAnDdnModemTrapGroup':zxAnDdnModemTrapGroup,'zxAnDdnModemLineStatusAbnormal':zxAnDdnModemLineStatusAbnormal,'zxAnDdnModemLineStatusNormal':zxAnDdnModemLineStatusNormal,'zxAnDdnPortLinkDown':zxAnDdnPortLinkDown,'zxAnDdnPortLinkUp':zxAnDdnPortLinkUp})