_v='remote'
_u='set2hw'
_t='default'
_s='ip113sr'
_r='ip113s'
_q='abnormal'
_p='slave_3'
_o='slave_2'
_n='slave_1'
_m='shelfName'
_l='mcLoOrRmtFg'
_k='reset'
_j='idle'
_i='removed'
_h='inserted'
_g='down'
_f='fr600f-ms'
_e='fr600f-mm'
_d='mc_1g_o2o'
_c='mc_1g_e2o'
_b='normal'
_a='off'
_Z='master'
_Y='na'
_X='mAuto'
_W='mandatory'
_V='store-forward'
_U='cut-through'
_T='ip113f'
_S='mcCardIdx'
_R='mcShelfIdx'
_Q='nc'
_P='disable'
_O='enable'
_N='m1G-full'
_M='m10-half'
_L='m10-full'
_K='m100-half'
_J='m100-full'
_I='no_card'
_H='slotIdx'
_G='read-write'
_F='shelfIdx'
_E='not-support'
_D='Integer32'
_C='XXX-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
company=ModuleIdentity((1,3,6,1,4,1,34592))
if mibBuilder.loadTexts:company.setRevisions(('2009-03-05 00:00',))
_IpProduct_ObjectIdentity=ObjectIdentity
ipProduct=_IpProduct_ObjectIdentity((1,3,6,1,4,1,34592,1))
if mibBuilder.loadTexts:ipProduct.setStatus(_A)
_Height2HU_ObjectIdentity=ObjectIdentity
height2HU=_Height2HU_ObjectIdentity((1,3,6,1,4,1,34592,1,1))
_SystemMIB_ObjectIdentity=ObjectIdentity
systemMIB=_SystemMIB_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1))
class _ShelfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ShelfNum_Type.__name__=_D
_ShelfNum_Object=MibScalar
shelfNum=_ShelfNum_Object((1,3,6,1,4,1,34592,1,1,1,1),_ShelfNum_Type())
shelfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfNum.setStatus(_A)
_ShelfTable_Object=MibTable
shelfTable=_ShelfTable_Object((1,3,6,1,4,1,34592,1,1,1,2))
if mibBuilder.loadTexts:shelfTable.setStatus(_A)
_ShelfEntry_Object=MibTableRow
shelfEntry=_ShelfEntry_Object((1,3,6,1,4,1,34592,1,1,1,2,1))
shelfEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:shelfEntry.setStatus(_A)
class _ShelfName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Z,1),(_n,2),(_o,3),(_p,4)))
_ShelfName_Type.__name__=_D
_ShelfName_Object=MibTableColumn
shelfName=_ShelfName_Object((1,3,6,1,4,1,34592,1,1,1,2,1,1),_ShelfName_Type())
shelfName.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfName.setStatus(_A)
class _PsuA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_a,2),(_Q,3)))
_PsuA_Type.__name__=_D
_PsuA_Object=MibTableColumn
psuA=_PsuA_Object((1,3,6,1,4,1,34592,1,1,1,2,1,2),_PsuA_Type())
psuA.setMaxAccess(_B)
if mibBuilder.loadTexts:psuA.setStatus(_A)
class _PsuB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_a,2),(_Q,3)))
_PsuB_Type.__name__=_D
_PsuB_Object=MibTableColumn
psuB=_PsuB_Object((1,3,6,1,4,1,34592,1,1,1,2,1,3),_PsuB_Type())
psuB.setMaxAccess(_B)
if mibBuilder.loadTexts:psuB.setStatus(_A)
class _VolA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),(_q,2),(_Q,3)))
_VolA_Type.__name__=_D
_VolA_Object=MibTableColumn
volA=_VolA_Object((1,3,6,1,4,1,34592,1,1,1,2,1,4),_VolA_Type())
volA.setMaxAccess(_B)
if mibBuilder.loadTexts:volA.setStatus(_A)
class _VolB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),(_q,2),(_Q,3)))
_VolB_Type.__name__=_D
_VolB_Object=MibTableColumn
volB=_VolB_Object((1,3,6,1,4,1,34592,1,1,1,2,1,5),_VolB_Type())
volB.setMaxAccess(_B)
if mibBuilder.loadTexts:volB.setStatus(_A)
class _Fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_a,2),(_Q,3)))
_Fan_Type.__name__=_D
_Fan_Object=MibTableColumn
fan=_Fan_Object((1,3,6,1,4,1,34592,1,1,1,2,1,6),_Fan_Type())
fan.setMaxAccess(_B)
if mibBuilder.loadTexts:fan.setStatus(_A)
_Temperature_Type=Integer32
_Temperature_Object=MibTableColumn
temperature=_Temperature_Object((1,3,6,1,4,1,34592,1,1,1,2,1,7),_Temperature_Type())
temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature.setStatus(_A)
if mibBuilder.loadTexts:temperature.setUnits(' °C')
class _CoCardNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CoCardNum_Type.__name__=_D
_CoCardNum_Object=MibTableColumn
coCardNum=_CoCardNum_Object((1,3,6,1,4,1,34592,1,1,1,2,1,8),_CoCardNum_Type())
coCardNum.setMaxAccess(_B)
if mibBuilder.loadTexts:coCardNum.setStatus(_A)
class _RmtCardNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RmtCardNum_Type.__name__=_D
_RmtCardNum_Object=MibTableColumn
rmtCardNum=_RmtCardNum_Object((1,3,6,1,4,1,34592,1,1,1,2,1,9),_RmtCardNum_Type())
rmtCardNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rmtCardNum.setStatus(_A)
_SlotObjects_ObjectIdentity=ObjectIdentity
slotObjects=_SlotObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,3))
_SlotTable_Object=MibTable
slotTable=_SlotTable_Object((1,3,6,1,4,1,34592,1,1,1,3,1))
if mibBuilder.loadTexts:slotTable.setStatus(_A)
_SlotEntry_Object=MibTableRow
slotEntry=_SlotEntry_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1))
slotEntry.setIndexNames((0,_C,_F),(0,_C,_H))
if mibBuilder.loadTexts:slotEntry.setStatus(_A)
class _ShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Z,1),(_n,2),(_o,3),(_p,4)))
_ShelfIdx_Type.__name__=_D
_ShelfIdx_Object=MibTableColumn
shelfIdx=_ShelfIdx_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1,1),_ShelfIdx_Type())
shelfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfIdx.setStatus(_A)
class _SlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('slot01',1),('slot02',2),('slot03',3),('slot04',4),('slot05',5),('slot06',6),('slot07',7),('slot08',8),('slot09',9),('slot10',10),('slot11',11),('slot12',12),('slot13',13),('slot14',14),('slot15',15),('slot16',16),('slot17',17)))
_SlotIdx_Type.__name__=_D
_SlotIdx_Object=MibTableColumn
slotIdx=_SlotIdx_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1,2),_SlotIdx_Type())
slotIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIdx.setStatus(_A)
class _CoCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,100,101,102)));namedValues=NamedValues(*((_I,0),(_r,1),(_T,2),(_c,3),(_d,4),(_e,100),(_f,101),(_E,102)))
_CoCardType_Type.__name__=_D
_CoCardType_Object=MibTableColumn
coCardType=_CoCardType_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1,3),_CoCardType_Type())
coCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:coCardType.setStatus(_A)
_CoCardDesc_Type=DisplayString
_CoCardDesc_Object=MibTableColumn
coCardDesc=_CoCardDesc_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1,4),_CoCardDesc_Type())
coCardDesc.setMaxAccess(_G)
if mibBuilder.loadTexts:coCardDesc.setStatus(_A)
class _RmtCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,100,101,102)));namedValues=NamedValues(*((_I,0),(_s,1),(_T,2),(_c,3),(_d,4),(_e,100),(_f,101),(_E,102)))
_RmtCardType_Type.__name__=_D
_RmtCardType_Object=MibTableColumn
rmtCardType=_RmtCardType_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1,5),_RmtCardType_Type())
rmtCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:rmtCardType.setStatus(_A)
_RmtCardDesc_Type=DisplayString
_RmtCardDesc_Object=MibTableColumn
rmtCardDesc=_RmtCardDesc_Object((1,3,6,1,4,1,34592,1,1,1,3,1,1,6),_RmtCardDesc_Type())
rmtCardDesc.setMaxAccess(_G)
if mibBuilder.loadTexts:rmtCardDesc.setStatus(_A)
_CardObjects_ObjectIdentity=ObjectIdentity
cardObjects=_CardObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4))
_NmuObjects_ObjectIdentity=ObjectIdentity
nmuObjects=_NmuObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,1))
_NmuConfig_ObjectIdentity=ObjectIdentity
nmuConfig=_NmuConfig_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,1,1))
class _NmuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101,102)));namedValues=NamedValues(*((_e,100),(_f,101),(_E,102)))
_NmuType_Type.__name__=_D
_NmuType_Object=MibScalar
nmuType=_NmuType_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,1),_NmuType_Type())
nmuType.setMaxAccess(_B)
if mibBuilder.loadTexts:nmuType.setStatus(_A)
_Ipaddr_Type=IpAddress
_Ipaddr_Object=MibScalar
ipaddr=_Ipaddr_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,2),_Ipaddr_Type())
ipaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipaddr.setStatus(_A)
_Subnet_Type=IpAddress
_Subnet_Object=MibScalar
subnet=_Subnet_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,3),_Subnet_Type())
subnet.setMaxAccess(_B)
if mibBuilder.loadTexts:subnet.setStatus(_A)
_Gateway_Type=IpAddress
_Gateway_Object=MibScalar
gateway=_Gateway_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,4),_Gateway_Type())
gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:gateway.setStatus(_A)
_SysContact_Type=DisplayString
_SysContact_Object=MibScalar
sysContact=_SysContact_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,5),_SysContact_Type())
sysContact.setMaxAccess(_G)
if mibBuilder.loadTexts:sysContact.setStatus(_A)
_SysName_Type=DisplayString
_SysName_Object=MibScalar
sysName=_SysName_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,6),_SysName_Type())
sysName.setMaxAccess(_G)
if mibBuilder.loadTexts:sysName.setStatus(_A)
_SysLocation_Type=DisplayString
_SysLocation_Object=MibScalar
sysLocation=_SysLocation_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,7),_SysLocation_Type())
sysLocation.setMaxAccess(_G)
if mibBuilder.loadTexts:sysLocation.setStatus(_A)
_TrapHost1_Type=IpAddress
_TrapHost1_Object=MibScalar
trapHost1=_TrapHost1_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,8),_TrapHost1_Type())
trapHost1.setMaxAccess(_G)
if mibBuilder.loadTexts:trapHost1.setStatus(_A)
_TrapHost2_Type=IpAddress
_TrapHost2_Object=MibScalar
trapHost2=_TrapHost2_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,9),_TrapHost2_Type())
trapHost2.setMaxAccess(_G)
if mibBuilder.loadTexts:trapHost2.setStatus(_A)
_TrapHost3_Type=IpAddress
_TrapHost3_Object=MibScalar
trapHost3=_TrapHost3_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,10),_TrapHost3_Type())
trapHost3.setMaxAccess(_G)
if mibBuilder.loadTexts:trapHost3.setStatus(_A)
_TrapHost4_Type=IpAddress
_TrapHost4_Object=MibScalar
trapHost4=_TrapHost4_Object((1,3,6,1,4,1,34592,1,1,1,4,1,1,11),_TrapHost4_Type())
trapHost4.setMaxAccess(_G)
if mibBuilder.loadTexts:trapHost4.setStatus(_A)
_McCmObjects_ObjectIdentity=ObjectIdentity
mcCmObjects=_McCmObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,2))
_McCmTable_Object=MibTable
mcCmTable=_McCmTable_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1))
if mibBuilder.loadTexts:mcCmTable.setStatus(_A)
_McCmEntry_Object=MibTableRow
mcCmEntry=_McCmEntry_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1))
mcCmEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:mcCmEntry.setStatus(_A)
class _McShelfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Z,1),('slave1',2),('slave2',3),('slave3',4)))
_McShelfIdx_Type.__name__=_D
_McShelfIdx_Object=MibTableColumn
mcShelfIdx=_McShelfIdx_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,1),_McShelfIdx_Type())
mcShelfIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:mcShelfIdx.setStatus(_A)
class _McCardIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('card01',1),('card02',2),('card03',3),('card04',4),('card05',5),('card06',6),('card07',7),('card08',8),('card09',9),('card10',10),('card11',11),('card12',12),('card13',13),('card14',14),('card15',15),('card16',16)))
_McCardIdx_Type.__name__=_D
_McCardIdx_Object=MibTableColumn
mcCardIdx=_McCardIdx_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,2),_McCardIdx_Type())
mcCardIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:mcCardIdx.setStatus(_A)
class _McType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_r,1),(_T,2),(_c,3),(_d,4),(_E,5)))
_McType_Type.__name__=_D
_McType_Object=MibTableColumn
mcType=_McType_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,3),_McType_Type())
mcType.setMaxAccess(_B)
if mibBuilder.loadTexts:mcType.setStatus(_A)
class _McTransceiverMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bidi',1),('duplex_fiber',2),('sfp',3),(_E,4)))
_McTransceiverMode_Type.__name__=_D
_McTransceiverMode_Object=MibTableColumn
mcTransceiverMode=_McTransceiverMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,4),_McTransceiverMode_Type())
mcTransceiverMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcTransceiverMode.setStatus(_A)
class _McTransceiverDist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_McTransceiverDist_Type.__name__=_D
_McTransceiverDist_Object=MibTableColumn
mcTransceiverDist=_McTransceiverDist_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,5),_McTransceiverDist_Type())
mcTransceiverDist.setMaxAccess(_B)
if mibBuilder.loadTexts:mcTransceiverDist.setStatus(_A)
class _McPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('locked',1),('unlocked',2),(_E,3)))
_McPortState_Type.__name__=_D
_McPortState_Object=MibTableColumn
mcPortState=_McPortState_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,6),_McPortState_Type())
mcPortState.setMaxAccess(_G)
if mibBuilder.loadTexts:mcPortState.setStatus(_A)
class _McTransmitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_E,3)))
_McTransmitMode_Type.__name__=_D
_McTransmitMode_Object=MibTableColumn
mcTransmitMode=_McTransmitMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,7),_McTransmitMode_Type())
mcTransmitMode.setMaxAccess(_G)
if mibBuilder.loadTexts:mcTransmitMode.setStatus(_A)
class _McCurWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_E,7)))
_McCurWorkMode_Type.__name__=_D
_McCurWorkMode_Object=MibTableColumn
mcCurWorkMode=_McCurWorkMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,8),_McCurWorkMode_Type())
mcCurWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcCurWorkMode.setStatus(_W)
class _McCfgWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_X,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_E,7)))
_McCfgWorkMode_Type.__name__=_D
_McCfgWorkMode_Object=MibTableColumn
mcCfgWorkMode=_McCfgWorkMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,9),_McCfgWorkMode_Type())
mcCfgWorkMode.setMaxAccess(_G)
if mibBuilder.loadTexts:mcCfgWorkMode.setStatus(_W)
class _McLFPCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_E,3)))
_McLFPCfg_Type.__name__=_D
_McLFPCfg_Object=MibTableColumn
mcLFPCfg=_McLFPCfg_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,10),_McLFPCfg_Type())
mcLFPCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:mcLFPCfg.setStatus(_A)
_McUpStream_Type=Gauge32
_McUpStream_Object=MibTableColumn
mcUpStream=_McUpStream_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,11),_McUpStream_Type())
mcUpStream.setMaxAccess(_G)
if mibBuilder.loadTexts:mcUpStream.setStatus(_A)
_McDownStream_Type=Gauge32
_McDownStream_Object=MibTableColumn
mcDownStream=_McDownStream_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,12),_McDownStream_Type())
mcDownStream.setMaxAccess(_G)
if mibBuilder.loadTexts:mcDownStream.setStatus(_A)
class _McTxlink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_g,2),(_E,3)))
_McTxlink_Type.__name__=_D
_McTxlink_Object=MibTableColumn
mcTxlink=_McTxlink_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,13),_McTxlink_Type())
mcTxlink.setMaxAccess(_B)
if mibBuilder.loadTexts:mcTxlink.setStatus(_A)
class _McFxlink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_g,2),(_E,3)))
_McFxlink_Type.__name__=_D
_McFxlink_Object=MibTableColumn
mcFxlink=_McFxlink_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,14),_McFxlink_Type())
mcFxlink.setMaxAccess(_B)
if mibBuilder.loadTexts:mcFxlink.setStatus(_A)
class _McHWLFP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_E,3)))
_McHWLFP_Type.__name__=_D
_McHWLFP_Object=MibTableColumn
mcHWLFP=_McHWLFP_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,15),_McHWLFP_Type())
mcHWLFP.setMaxAccess(_B)
if mibBuilder.loadTexts:mcHWLFP.setStatus(_A)
class _McHWTransmitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_E,3)))
_McHWTransmitMode_Type.__name__=_D
_McHWTransmitMode_Object=MibTableColumn
mcHWTransmitMode=_McHWTransmitMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,16),_McHWTransmitMode_Type())
mcHWTransmitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcHWTransmitMode.setStatus(_A)
class _McHWWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_X,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_E,7)))
_McHWWorkMode_Type.__name__=_D
_McHWWorkMode_Object=MibTableColumn
mcHWWorkMode=_McHWWorkMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,17),_McHWWorkMode_Type())
mcHWWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcHWWorkMode.setStatus(_A)
class _McHWRmtCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_E,3)))
_McHWRmtCtrlMode_Type.__name__=_D
_McHWRmtCtrlMode_Object=MibTableColumn
mcHWRmtCtrlMode=_McHWRmtCtrlMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,18),_McHWRmtCtrlMode_Type())
mcHWRmtCtrlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcHWRmtCtrlMode.setStatus(_A)
class _McNtwSfpExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_Y,3),(_E,4)))
_McNtwSfpExist_Type.__name__=_D
_McNtwSfpExist_Object=MibTableColumn
mcNtwSfpExist=_McNtwSfpExist_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,19),_McNtwSfpExist_Type())
mcNtwSfpExist.setMaxAccess(_B)
if mibBuilder.loadTexts:mcNtwSfpExist.setStatus(_A)
class _McAccSfpExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_Y,3),(_E,4)))
_McAccSfpExist_Type.__name__=_D
_McAccSfpExist_Object=MibTableColumn
mcAccSfpExist=_McAccSfpExist_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,20),_McAccSfpExist_Type())
mcAccSfpExist.setMaxAccess(_B)
if mibBuilder.loadTexts:mcAccSfpExist.setStatus(_A)
class _McUtility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_j,1),(_k,2),(_t,3),(_u,4),(_E,5)))
_McUtility_Type.__name__=_D
_McUtility_Object=MibTableColumn
mcUtility=_McUtility_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,21),_McUtility_Type())
mcUtility.setMaxAccess(_G)
if mibBuilder.loadTexts:mcUtility.setStatus(_A)
class _McRmtDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('no_remote',0),('yes',1),(_E,2)))
_McRmtDetect_Type.__name__=_D
_McRmtDetect_Object=MibTableColumn
mcRmtDetect=_McRmtDetect_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,22),_McRmtDetect_Type())
mcRmtDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtDetect.setStatus(_A)
class _McRmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_s,1),(_T,2),('mc_1g_e2or',3),('mc_1g_o2or',4),(_E,5)))
_McRmtType_Type.__name__=_D
_McRmtType_Object=MibTableColumn
mcRmtType=_McRmtType_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,23),_McRmtType_Type())
mcRmtType.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtType.setStatus(_A)
class _McRmtTransmitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_U,1),(_V,2),(_E,3)))
_McRmtTransmitMode_Type.__name__=_D
_McRmtTransmitMode_Object=MibTableColumn
mcRmtTransmitMode=_McRmtTransmitMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,24),_McRmtTransmitMode_Type())
mcRmtTransmitMode.setMaxAccess(_G)
if mibBuilder.loadTexts:mcRmtTransmitMode.setStatus(_A)
class _McRmtCurWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_E,7)))
_McRmtCurWorkMode_Type.__name__=_D
_McRmtCurWorkMode_Object=MibTableColumn
mcRmtCurWorkMode=_McRmtCurWorkMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,25),_McRmtCurWorkMode_Type())
mcRmtCurWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtCurWorkMode.setStatus(_W)
class _McRmtCfgWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_X,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_E,7)))
_McRmtCfgWorkMode_Type.__name__=_D
_McRmtCfgWorkMode_Object=MibTableColumn
mcRmtCfgWorkMode=_McRmtCfgWorkMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,26),_McRmtCfgWorkMode_Type())
mcRmtCfgWorkMode.setMaxAccess(_G)
if mibBuilder.loadTexts:mcRmtCfgWorkMode.setStatus(_W)
class _McRmtLFP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_E,3)))
_McRmtLFP_Type.__name__=_D
_McRmtLFP_Object=MibTableColumn
mcRmtLFP=_McRmtLFP_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,27),_McRmtLFP_Type())
mcRmtLFP.setMaxAccess(_G)
if mibBuilder.loadTexts:mcRmtLFP.setStatus(_A)
class _McRmtTxlink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('up',1),(_g,2),(_E,3)))
_McRmtTxlink_Type.__name__=_D
_McRmtTxlink_Object=MibTableColumn
mcRmtTxlink=_McRmtTxlink_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,28),_McRmtTxlink_Type())
mcRmtTxlink.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtTxlink.setStatus(_A)
class _McRmtHWLFP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_E,3)))
_McRmtHWLFP_Type.__name__=_D
_McRmtHWLFP_Object=MibTableColumn
mcRmtHWLFP=_McRmtHWLFP_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,29),_McRmtHWLFP_Type())
mcRmtHWLFP.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtHWLFP.setStatus(_A)
class _McRmtHWTransmitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_U,1),(_V,2),(_E,3)))
_McRmtHWTransmitMode_Type.__name__=_D
_McRmtHWTransmitMode_Object=MibTableColumn
mcRmtHWTransmitMode=_McRmtHWTransmitMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,30),_McRmtHWTransmitMode_Type())
mcRmtHWTransmitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtHWTransmitMode.setStatus(_A)
class _McRmtHWWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,0),(_X,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_E,7)))
_McRmtHWWorkMode_Type.__name__=_D
_McRmtHWWorkMode_Object=MibTableColumn
mcRmtHWWorkMode=_McRmtHWWorkMode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,31),_McRmtHWWorkMode_Type())
mcRmtHWWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtHWWorkMode.setStatus(_A)
class _McRmtLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_E,3)))
_McRmtLoopback_Type.__name__=_D
_McRmtLoopback_Object=MibTableColumn
mcRmtLoopback=_McRmtLoopback_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,32),_McRmtLoopback_Type())
mcRmtLoopback.setMaxAccess(_G)
if mibBuilder.loadTexts:mcRmtLoopback.setStatus(_A)
class _McRmtPwrDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('powerdown',1),(_b,2),(_E,3)))
_McRmtPwrDown_Type.__name__=_D
_McRmtPwrDown_Object=MibTableColumn
mcRmtPwrDown=_McRmtPwrDown_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,33),_McRmtPwrDown_Type())
mcRmtPwrDown.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtPwrDown.setStatus(_A)
class _McRmtAccSfpExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_h,1),(_i,2),(_Y,3),('support',4)))
_McRmtAccSfpExist_Type.__name__=_D
_McRmtAccSfpExist_Object=MibTableColumn
mcRmtAccSfpExist=_McRmtAccSfpExist_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,34),_McRmtAccSfpExist_Type())
mcRmtAccSfpExist.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRmtAccSfpExist.setStatus(_A)
class _McRmtUtility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_j,1),(_k,2),(_t,3),(_u,4),(_E,5)))
_McRmtUtility_Type.__name__=_D
_McRmtUtility_Object=MibTableColumn
mcRmtUtility=_McRmtUtility_Object((1,3,6,1,4,1,34592,1,1,1,4,2,1,1,35),_McRmtUtility_Type())
mcRmtUtility.setMaxAccess(_G)
if mibBuilder.loadTexts:mcRmtUtility.setStatus(_A)
_McCm1gSpecificObjects_ObjectIdentity=ObjectIdentity
mcCm1gSpecificObjects=_McCm1gSpecificObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,2,2))
_McCm1gIpObjects_ObjectIdentity=ObjectIdentity
mcCm1gIpObjects=_McCm1gIpObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,2,2,1))
_McCm1gIpTable_Object=MibTable
mcCm1gIpTable=_McCm1gIpTable_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,1,1))
if mibBuilder.loadTexts:mcCm1gIpTable.setStatus(_A)
_McCm1gIpEntry_Object=MibTableRow
mcCm1gIpEntry=_McCm1gIpEntry_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,1,1,1))
mcCm1gIpEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_l))
if mibBuilder.loadTexts:mcCm1gIpEntry.setStatus(_A)
class _McLoOrRmtFg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_v,2)))
_McLoOrRmtFg_Type.__name__=_D
_McLoOrRmtFg_Object=MibTableColumn
mcLoOrRmtFg=_McLoOrRmtFg_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,1,1,1,1),_McLoOrRmtFg_Type())
mcLoOrRmtFg.setMaxAccess(_B)
if mibBuilder.loadTexts:mcLoOrRmtFg.setStatus(_A)
_McIpAddr_Type=IpAddress
_McIpAddr_Object=MibTableColumn
mcIpAddr=_McIpAddr_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,1,1,1,2),_McIpAddr_Type())
mcIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:mcIpAddr.setStatus(_A)
_McCm1gSfpObjects_ObjectIdentity=ObjectIdentity
mcCm1gSfpObjects=_McCm1gSfpObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,2,2,2))
_McCm1gSfpTable_Object=MibTable
mcCm1gSfpTable=_McCm1gSfpTable_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1))
if mibBuilder.loadTexts:mcCm1gSfpTable.setStatus(_A)
_McCm1gSfpEntry_Object=MibTableRow
mcCm1gSfpEntry=_McCm1gSfpEntry_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1))
mcCm1gSfpEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_l))
if mibBuilder.loadTexts:mcCm1gSfpEntry.setStatus(_A)
class _GetSfpCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Y,0),('local',1),(_v,2)))
_GetSfpCmd_Type.__name__=_D
_GetSfpCmd_Object=MibTableColumn
getSfpCmd=_GetSfpCmd_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,1),_GetSfpCmd_Type())
getSfpCmd.setMaxAccess(_G)
if mibBuilder.loadTexts:getSfpCmd.setStatus(_A)
_SfpCompliance_Type=Integer32
_SfpCompliance_Object=MibTableColumn
sfpCompliance=_SfpCompliance_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,2),_SfpCompliance_Type())
sfpCompliance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpCompliance.setStatus(_A)
_SfpConnector_Type=Integer32
_SfpConnector_Object=MibTableColumn
sfpConnector=_SfpConnector_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,3),_SfpConnector_Type())
sfpConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpConnector.setStatus(_A)
_SfpTransCode_Type=Integer32
_SfpTransCode_Object=MibTableColumn
sfpTransCode=_SfpTransCode_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,4),_SfpTransCode_Type())
sfpTransCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTransCode.setStatus(_A)
_SfpSmLength_Type=Integer32
_SfpSmLength_Object=MibTableColumn
sfpSmLength=_SfpSmLength_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,5),_SfpSmLength_Type())
sfpSmLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpSmLength.setStatus(_A)
_SfpMmLength_Type=Integer32
_SfpMmLength_Object=MibTableColumn
sfpMmLength=_SfpMmLength_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,6),_SfpMmLength_Type())
sfpMmLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpMmLength.setStatus(_A)
_SfpCopperLength_Type=Integer32
_SfpCopperLength_Object=MibTableColumn
sfpCopperLength=_SfpCopperLength_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,7),_SfpCopperLength_Type())
sfpCopperLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpCopperLength.setStatus(_A)
_SfpBrSpeed_Type=Integer32
_SfpBrSpeed_Object=MibTableColumn
sfpBrSpeed=_SfpBrSpeed_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,8),_SfpBrSpeed_Type())
sfpBrSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpBrSpeed.setStatus(_A)
_SfpWavelength_Type=Integer32
_SfpWavelength_Object=MibTableColumn
sfpWavelength=_SfpWavelength_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,9),_SfpWavelength_Type())
sfpWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpWavelength.setStatus(_A)
_SfpTemperature_Type=Integer32
_SfpTemperature_Object=MibTableColumn
sfpTemperature=_SfpTemperature_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,10),_SfpTemperature_Type())
sfpTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTemperature.setStatus(_A)
_SfpTranPower_Type=Integer32
_SfpTranPower_Object=MibTableColumn
sfpTranPower=_SfpTranPower_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,11),_SfpTranPower_Type())
sfpTranPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpTranPower.setStatus(_A)
_SfpRecvPower_Type=Integer32
_SfpRecvPower_Object=MibTableColumn
sfpRecvPower=_SfpRecvPower_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,12),_SfpRecvPower_Type())
sfpRecvPower.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpRecvPower.setStatus(_A)
_SfpVoltage_Type=Integer32
_SfpVoltage_Object=MibTableColumn
sfpVoltage=_SfpVoltage_Object((1,3,6,1,4,1,34592,1,1,1,4,2,2,2,1,1,13),_SfpVoltage_Type())
sfpVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpVoltage.setStatus(_A)
_McPmObjects_ObjectIdentity=ObjectIdentity
mcPmObjects=_McPmObjects_ObjectIdentity((1,3,6,1,4,1,34592,1,1,1,4,3))
_McPmTable_Object=MibTable
mcPmTable=_McPmTable_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1))
if mibBuilder.loadTexts:mcPmTable.setStatus(_A)
_McPmEntry_Object=MibTableRow
mcPmEntry=_McPmEntry_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1,1))
mcPmEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:mcPmEntry.setStatus(_A)
_McRxByteHi_Type=Counter32
_McRxByteHi_Object=MibTableColumn
mcRxByteHi=_McRxByteHi_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1,1,1),_McRxByteHi_Type())
mcRxByteHi.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRxByteHi.setStatus(_A)
_McRxByteLo_Type=Counter32
_McRxByteLo_Object=MibTableColumn
mcRxByteLo=_McRxByteLo_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1,1,2),_McRxByteLo_Type())
mcRxByteLo.setMaxAccess(_B)
if mibBuilder.loadTexts:mcRxByteLo.setStatus(_A)
_McTxByteHi_Type=Counter32
_McTxByteHi_Object=MibTableColumn
mcTxByteHi=_McTxByteHi_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1,1,3),_McTxByteHi_Type())
mcTxByteHi.setMaxAccess(_B)
if mibBuilder.loadTexts:mcTxByteHi.setStatus(_A)
_McTxByteLo_Type=Counter32
_McTxByteLo_Object=MibTableColumn
mcTxByteLo=_McTxByteLo_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1,1,4),_McTxByteLo_Type())
mcTxByteLo.setMaxAccess(_B)
if mibBuilder.loadTexts:mcTxByteLo.setStatus(_A)
class _McPmRest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_j,1),(_k,2),(_E,3)))
_McPmRest_Type.__name__=_D
_McPmRest_Object=MibTableColumn
mcPmRest=_McPmRest_Object((1,3,6,1,4,1,34592,1,1,1,4,3,1,1,5),_McPmRest_Type())
mcPmRest.setMaxAccess(_G)
if mibBuilder.loadTexts:mcPmRest.setStatus(_A)
_AlarmMIB_ObjectIdentity=ObjectIdentity
alarmMIB=_AlarmMIB_ObjectIdentity((1,3,6,1,4,1,34592,1,1,2))
shelf_Detected=NotificationType((1,3,6,1,4,1,34592,1,1,2,1))
shelf_Detected.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_Detected.setStatus(_A)
shelf_Lost=NotificationType((1,3,6,1,4,1,34592,1,1,2,2))
shelf_Lost.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_Lost.setStatus(_A)
shelf_psuA_On=NotificationType((1,3,6,1,4,1,34592,1,1,2,3))
shelf_psuA_On.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_psuA_On.setStatus(_A)
shelf_psuA_Off=NotificationType((1,3,6,1,4,1,34592,1,1,2,4))
shelf_psuA_Off.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_psuA_Off.setStatus(_A)
shelf_psuB_On=NotificationType((1,3,6,1,4,1,34592,1,1,2,5))
shelf_psuB_On.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_psuB_On.setStatus(_A)
shelf_psuB_Off=NotificationType((1,3,6,1,4,1,34592,1,1,2,6))
shelf_psuB_Off.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_psuB_Off.setStatus(_A)
shelf_fan_On=NotificationType((1,3,6,1,4,1,34592,1,1,2,7))
shelf_fan_On.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_fan_On.setStatus(_A)
shelf_fan_Off=NotificationType((1,3,6,1,4,1,34592,1,1,2,8))
shelf_fan_Off.setObjects((_C,_F))
if mibBuilder.loadTexts:shelf_fan_Off.setStatus(_A)
card_Detected=NotificationType((1,3,6,1,4,1,34592,1,1,2,20))
card_Detected.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_Detected.setStatus(_A)
card_Lost=NotificationType((1,3,6,1,4,1,34592,1,1,2,21))
card_Lost.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_Lost.setStatus(_A)
card_MC_Co_Tx_Up=NotificationType((1,3,6,1,4,1,34592,1,1,2,30))
card_MC_Co_Tx_Up.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Tx_Up.setStatus(_A)
card_MC_Co_Tx_Down=NotificationType((1,3,6,1,4,1,34592,1,1,2,31))
card_MC_Co_Tx_Down.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Tx_Down.setStatus(_A)
card_MC_Co_Fx_Up=NotificationType((1,3,6,1,4,1,34592,1,1,2,32))
card_MC_Co_Fx_Up.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Fx_Up.setStatus(_A)
card_MC_Co_Fx_Down=NotificationType((1,3,6,1,4,1,34592,1,1,2,33))
card_MC_Co_Fx_Down.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Fx_Down.setStatus(_A)
card_MC_Rmt_Tx_Up=NotificationType((1,3,6,1,4,1,34592,1,1,2,34))
card_MC_Rmt_Tx_Up.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Rmt_Tx_Up.setStatus(_A)
card_MC_Rmt_Tx_Down=NotificationType((1,3,6,1,4,1,34592,1,1,2,35))
card_MC_Rmt_Tx_Down.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Rmt_Tx_Down.setStatus(_A)
card_MC_Rmt_PwrDown=NotificationType((1,3,6,1,4,1,34592,1,1,2,36))
card_MC_Rmt_PwrDown.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Rmt_PwrDown.setStatus(_A)
card_MC_Co_Ntw_SFP_Inserted=NotificationType((1,3,6,1,4,1,34592,1,1,2,37))
card_MC_Co_Ntw_SFP_Inserted.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Ntw_SFP_Inserted.setStatus(_A)
card_MC_Co_Ntw_SFP_Removed=NotificationType((1,3,6,1,4,1,34592,1,1,2,38))
card_MC_Co_Ntw_SFP_Removed.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Ntw_SFP_Removed.setStatus(_A)
card_MC_Co_Acc_SFP_Inserted=NotificationType((1,3,6,1,4,1,34592,1,1,2,39))
card_MC_Co_Acc_SFP_Inserted.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Acc_SFP_Inserted.setStatus(_A)
card_MC_Co_Acc_SFP_Removed=NotificationType((1,3,6,1,4,1,34592,1,1,2,40))
card_MC_Co_Acc_SFP_Removed.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Co_Acc_SFP_Removed.setStatus(_A)
card_MC_Rmt_Acc_SFP_Inserted=NotificationType((1,3,6,1,4,1,34592,1,1,2,41))
card_MC_Rmt_Acc_SFP_Inserted.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Rmt_Acc_SFP_Inserted.setStatus(_A)
card_MC_Rmt_Acc_SFP_Removed=NotificationType((1,3,6,1,4,1,34592,1,1,2,42))
card_MC_Rmt_Acc_SFP_Removed.setObjects(*((_C,_F),(_C,_H)))
if mibBuilder.loadTexts:card_MC_Rmt_Acc_SFP_Removed.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'company':company,'ipProduct':ipProduct,'height2HU':height2HU,'systemMIB':systemMIB,'shelfNum':shelfNum,'shelfTable':shelfTable,'shelfEntry':shelfEntry,_m:shelfName,'psuA':psuA,'psuB':psuB,'volA':volA,'volB':volB,'fan':fan,'temperature':temperature,'coCardNum':coCardNum,'rmtCardNum':rmtCardNum,'slotObjects':slotObjects,'slotTable':slotTable,'slotEntry':slotEntry,_F:shelfIdx,_H:slotIdx,'coCardType':coCardType,'coCardDesc':coCardDesc,'rmtCardType':rmtCardType,'rmtCardDesc':rmtCardDesc,'cardObjects':cardObjects,'nmuObjects':nmuObjects,'nmuConfig':nmuConfig,'nmuType':nmuType,'ipaddr':ipaddr,'subnet':subnet,'gateway':gateway,'sysContact':sysContact,'sysName':sysName,'sysLocation':sysLocation,'trapHost1':trapHost1,'trapHost2':trapHost2,'trapHost3':trapHost3,'trapHost4':trapHost4,'mcCmObjects':mcCmObjects,'mcCmTable':mcCmTable,'mcCmEntry':mcCmEntry,_R:mcShelfIdx,_S:mcCardIdx,'mcType':mcType,'mcTransceiverMode':mcTransceiverMode,'mcTransceiverDist':mcTransceiverDist,'mcPortState':mcPortState,'mcTransmitMode':mcTransmitMode,'mcCurWorkMode':mcCurWorkMode,'mcCfgWorkMode':mcCfgWorkMode,'mcLFPCfg':mcLFPCfg,'mcUpStream':mcUpStream,'mcDownStream':mcDownStream,'mcTxlink':mcTxlink,'mcFxlink':mcFxlink,'mcHWLFP':mcHWLFP,'mcHWTransmitMode':mcHWTransmitMode,'mcHWWorkMode':mcHWWorkMode,'mcHWRmtCtrlMode':mcHWRmtCtrlMode,'mcNtwSfpExist':mcNtwSfpExist,'mcAccSfpExist':mcAccSfpExist,'mcUtility':mcUtility,'mcRmtDetect':mcRmtDetect,'mcRmtType':mcRmtType,'mcRmtTransmitMode':mcRmtTransmitMode,'mcRmtCurWorkMode':mcRmtCurWorkMode,'mcRmtCfgWorkMode':mcRmtCfgWorkMode,'mcRmtLFP':mcRmtLFP,'mcRmtTxlink':mcRmtTxlink,'mcRmtHWLFP':mcRmtHWLFP,'mcRmtHWTransmitMode':mcRmtHWTransmitMode,'mcRmtHWWorkMode':mcRmtHWWorkMode,'mcRmtLoopback':mcRmtLoopback,'mcRmtPwrDown':mcRmtPwrDown,'mcRmtAccSfpExist':mcRmtAccSfpExist,'mcRmtUtility':mcRmtUtility,'mcCm1gSpecificObjects':mcCm1gSpecificObjects,'mcCm1gIpObjects':mcCm1gIpObjects,'mcCm1gIpTable':mcCm1gIpTable,'mcCm1gIpEntry':mcCm1gIpEntry,_l:mcLoOrRmtFg,'mcIpAddr':mcIpAddr,'mcCm1gSfpObjects':mcCm1gSfpObjects,'mcCm1gSfpTable':mcCm1gSfpTable,'mcCm1gSfpEntry':mcCm1gSfpEntry,'getSfpCmd':getSfpCmd,'sfpCompliance':sfpCompliance,'sfpConnector':sfpConnector,'sfpTransCode':sfpTransCode,'sfpSmLength':sfpSmLength,'sfpMmLength':sfpMmLength,'sfpCopperLength':sfpCopperLength,'sfpBrSpeed':sfpBrSpeed,'sfpWavelength':sfpWavelength,'sfpTemperature':sfpTemperature,'sfpTranPower':sfpTranPower,'sfpRecvPower':sfpRecvPower,'sfpVoltage':sfpVoltage,'mcPmObjects':mcPmObjects,'mcPmTable':mcPmTable,'mcPmEntry':mcPmEntry,'mcRxByteHi':mcRxByteHi,'mcRxByteLo':mcRxByteLo,'mcTxByteHi':mcTxByteHi,'mcTxByteLo':mcTxByteLo,'mcPmRest':mcPmRest,'alarmMIB':alarmMIB,'shelf-Detected':shelf_Detected,'shelf-Lost':shelf_Lost,'shelf-psuA-On':shelf_psuA_On,'shelf-psuA-Off':shelf_psuA_Off,'shelf-psuB-On':shelf_psuB_On,'shelf-psuB-Off':shelf_psuB_Off,'shelf-fan-On':shelf_fan_On,'shelf-fan-Off':shelf_fan_Off,'card-Detected':card_Detected,'card-Lost':card_Lost,'card-MC-Co-Tx-Up':card_MC_Co_Tx_Up,'card-MC-Co-Tx-Down':card_MC_Co_Tx_Down,'card-MC-Co-Fx-Up':card_MC_Co_Fx_Up,'card-MC-Co-Fx-Down':card_MC_Co_Fx_Down,'card-MC-Rmt-Tx-Up':card_MC_Rmt_Tx_Up,'card-MC-Rmt-Tx-Down':card_MC_Rmt_Tx_Down,'card-MC-Rmt-PwrDown':card_MC_Rmt_PwrDown,'card-MC-Co-Ntw-SFP-Inserted':card_MC_Co_Ntw_SFP_Inserted,'card-MC-Co-Ntw-SFP-Removed':card_MC_Co_Ntw_SFP_Removed,'card-MC-Co-Acc-SFP-Inserted':card_MC_Co_Acc_SFP_Inserted,'card-MC-Co-Acc-SFP-Removed':card_MC_Co_Acc_SFP_Removed,'card-MC-Rmt-Acc-SFP-Inserted':card_MC_Rmt_Acc_SFP_Inserted,'card-MC-Rmt-Acc-SFP-Removed':card_MC_Rmt_Acc_SFP_Removed})