_Z='loopdetectPortIfindex'
_Y='not-accessible'
_X='vctIfindex'
_W='DisplayString'
_V='OctetString'
_U='enable'
_T='disable'
_S='Vct-Loopdetect-59-MIB'
_R='unknow'
_Q='morethan140'
_P='from110to140'
_O='from80to110'
_N='from50to80'
_M='lessthan50'
_L='unknown'
_K='fail'
_J='mismatch'
_I='broken'
_H='short'
_G='open'
_F='good'
_E='read-write'
_D='null'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,experimental,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','experimental','iso','mgmt')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_W,'MacAddress','PhysAddress','RowStatus','TextualConvention')
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10switch_ObjectIdentity=ObjectIdentity
zxr10switch=_Zxr10switch_ObjectIdentity((1,3,6,1,4,1,3902,3,102))
_Switch59vct_ObjectIdentity=ObjectIdentity
switch59vct=_Switch59vct_ObjectIdentity((1,3,6,1,4,1,3902,3,102,24))
_VctTable_Object=MibTable
vctTable=_VctTable_Object((1,3,6,1,4,1,3902,3,102,24,1))
if mibBuilder.loadTexts:vctTable.setStatus(_A)
_VctEntry_Object=MibTableRow
vctEntry=_VctEntry_Object((1,3,6,1,4,1,3902,3,102,24,1,1))
vctEntry.setIndexNames((0,_S,_X))
if mibBuilder.loadTexts:vctEntry.setStatus(_A)
_VctIfindex_Type=Integer32
_VctIfindex_Object=MibTableColumn
vctIfindex=_VctIfindex_Object((1,3,6,1,4,1,3902,3,102,24,1,1,1),_VctIfindex_Type())
vctIfindex.setMaxAccess(_Y)
if mibBuilder.loadTexts:vctIfindex.setStatus(_A)
class _VctSetIfindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_VctSetIfindex_Type.__name__=_B
_VctSetIfindex_Object=MibTableColumn
vctSetIfindex=_VctSetIfindex_Object((1,3,6,1,4,1,3902,3,102,24,1,1,2),_VctSetIfindex_Type())
vctSetIfindex.setMaxAccess(_E)
if mibBuilder.loadTexts:vctSetIfindex.setStatus(_A)
class _CableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fault',0),(_F,1)))
_CableStatus_Type.__name__=_B
_CableStatus_Object=MibTableColumn
cableStatus=_CableStatus_Object((1,3,6,1,4,1,3902,3,102,24,1,1,3),_CableStatus_Type())
cableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cableStatus.setStatus(_A)
class _DoubleCableStatus1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_D,7)))
_DoubleCableStatus1_2_Type.__name__=_B
_DoubleCableStatus1_2_Object=MibTableColumn
doubleCableStatus1_2=_DoubleCableStatus1_2_Object((1,3,6,1,4,1,3902,3,102,24,1,1,4),_DoubleCableStatus1_2_Type())
doubleCableStatus1_2.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableStatus1_2.setStatus(_A)
class _DoubleCableStatus3_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_D,7)))
_DoubleCableStatus3_6_Type.__name__=_B
_DoubleCableStatus3_6_Object=MibTableColumn
doubleCableStatus3_6=_DoubleCableStatus3_6_Object((1,3,6,1,4,1,3902,3,102,24,1,1,5),_DoubleCableStatus3_6_Type())
doubleCableStatus3_6.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableStatus3_6.setStatus(_A)
class _DoubleCableStatus4_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_D,7)))
_DoubleCableStatus4_5_Type.__name__=_B
_DoubleCableStatus4_5_Object=MibTableColumn
doubleCableStatus4_5=_DoubleCableStatus4_5_Object((1,3,6,1,4,1,3902,3,102,24,1,1,6),_DoubleCableStatus4_5_Type())
doubleCableStatus4_5.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableStatus4_5.setStatus(_A)
class _DoubleCableStatus7_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_D,7)))
_DoubleCableStatus7_8_Type.__name__=_B
_DoubleCableStatus7_8_Object=MibTableColumn
doubleCableStatus7_8=_DoubleCableStatus7_8_Object((1,3,6,1,4,1,3902,3,102,24,1,1,7),_DoubleCableStatus7_8_Type())
doubleCableStatus7_8.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableStatus7_8.setStatus(_A)
class _DoubleCableLength1_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,201,202,203,204,205,206)));namedValues=NamedValues(*((_M,200),(_N,201),(_O,202),(_P,203),(_Q,204),(_R,205),(_D,206)))
_DoubleCableLength1_2_Type.__name__=_B
_DoubleCableLength1_2_Object=MibTableColumn
doubleCableLength1_2=_DoubleCableLength1_2_Object((1,3,6,1,4,1,3902,3,102,24,1,1,8),_DoubleCableLength1_2_Type())
doubleCableLength1_2.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableLength1_2.setStatus(_A)
class _DoubleCableLength3_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,201,202,203,204,205,206)));namedValues=NamedValues(*((_M,200),(_N,201),(_O,202),(_P,203),(_Q,204),(_R,205),(_D,206)))
_DoubleCableLength3_6_Type.__name__=_B
_DoubleCableLength3_6_Object=MibTableColumn
doubleCableLength3_6=_DoubleCableLength3_6_Object((1,3,6,1,4,1,3902,3,102,24,1,1,9),_DoubleCableLength3_6_Type())
doubleCableLength3_6.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableLength3_6.setStatus(_A)
class _DoubleCableLength4_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,201,202,203,204,205,206)));namedValues=NamedValues(*((_M,200),(_N,201),(_O,202),(_P,203),(_Q,204),(_R,205),(_D,206)))
_DoubleCableLength4_5_Type.__name__=_B
_DoubleCableLength4_5_Object=MibTableColumn
doubleCableLength4_5=_DoubleCableLength4_5_Object((1,3,6,1,4,1,3902,3,102,24,1,1,10),_DoubleCableLength4_5_Type())
doubleCableLength4_5.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableLength4_5.setStatus(_A)
class _DoubleCableLength7_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,201,202,203,204,205,206)));namedValues=NamedValues(*((_M,200),(_N,201),(_O,202),(_P,203),(_Q,204),(_R,205),(_D,206)))
_DoubleCableLength7_8_Type.__name__=_B
_DoubleCableLength7_8_Object=MibTableColumn
doubleCableLength7_8=_DoubleCableLength7_8_Object((1,3,6,1,4,1,3902,3,102,24,1,1,11),_DoubleCableLength7_8_Type())
doubleCableLength7_8.setMaxAccess(_C)
if mibBuilder.loadTexts:doubleCableLength7_8.setStatus(_A)
_Switch59loopdetect_ObjectIdentity=ObjectIdentity
switch59loopdetect=_Switch59loopdetect_ObjectIdentity((1,3,6,1,4,1,3902,3,102,25))
class _LoopdetectReopenTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777216))
_LoopdetectReopenTime_Type.__name__=_B
_LoopdetectReopenTime_Object=MibScalar
loopdetectReopenTime=_LoopdetectReopenTime_Object((1,3,6,1,4,1,3902,3,102,25,1),_LoopdetectReopenTime_Type())
loopdetectReopenTime.setMaxAccess(_E)
if mibBuilder.loadTexts:loopdetectReopenTime.setStatus(_A)
_LoopdetectTable_Object=MibTable
loopdetectTable=_LoopdetectTable_Object((1,3,6,1,4,1,3902,3,102,25,2))
if mibBuilder.loadTexts:loopdetectTable.setStatus(_A)
_LoopdetectEntry_Object=MibTableRow
loopdetectEntry=_LoopdetectEntry_Object((1,3,6,1,4,1,3902,3,102,25,2,1))
loopdetectEntry.setIndexNames((0,_S,_Z))
if mibBuilder.loadTexts:loopdetectEntry.setStatus(_A)
_LoopdetectPortIfindex_Type=Integer32
_LoopdetectPortIfindex_Object=MibTableColumn
loopdetectPortIfindex=_LoopdetectPortIfindex_Object((1,3,6,1,4,1,3902,3,102,25,2,1,1),_LoopdetectPortIfindex_Type())
loopdetectPortIfindex.setMaxAccess(_Y)
if mibBuilder.loadTexts:loopdetectPortIfindex.setStatus(_A)
class _LoopdetectPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_LoopdetectPortOperStatus_Type.__name__=_B
_LoopdetectPortOperStatus_Object=MibTableColumn
loopdetectPortOperStatus=_LoopdetectPortOperStatus_Object((1,3,6,1,4,1,3902,3,102,25,2,1,2),_LoopdetectPortOperStatus_Type())
loopdetectPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loopdetectPortOperStatus.setStatus(_A)
class _LoopdetectPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_LoopdetectPortControl_Type.__name__=_B
_LoopdetectPortControl_Object=MibTableColumn
loopdetectPortControl=_LoopdetectPortControl_Object((1,3,6,1,4,1,3902,3,102,25,2,1,3),_LoopdetectPortControl_Type())
loopdetectPortControl.setMaxAccess(_E)
if mibBuilder.loadTexts:loopdetectPortControl.setStatus(_A)
class _LoopdetectPortVid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LoopdetectPortVid_Type.__name__=_V
_LoopdetectPortVid_Object=MibTableColumn
loopdetectPortVid=_LoopdetectPortVid_Object((1,3,6,1,4,1,3902,3,102,25,2,1,4),_LoopdetectPortVid_Type())
loopdetectPortVid.setMaxAccess(_E)
if mibBuilder.loadTexts:loopdetectPortVid.setStatus(_A)
class _LoopdetectPortFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_LoopdetectPortFlag_Type.__name__=_B
_LoopdetectPortFlag_Object=MibTableColumn
loopdetectPortFlag=_LoopdetectPortFlag_Object((1,3,6,1,4,1,3902,3,102,25,2,1,5),_LoopdetectPortFlag_Type())
loopdetectPortFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:loopdetectPortFlag.setStatus(_A)
class _LoopdetectPortProtectFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_LoopdetectPortProtectFlag_Type.__name__=_B
_LoopdetectPortProtectFlag_Object=MibTableColumn
loopdetectPortProtectFlag=_LoopdetectPortProtectFlag_Object((1,3,6,1,4,1,3902,3,102,25,2,1,6),_LoopdetectPortProtectFlag_Type())
loopdetectPortProtectFlag.setMaxAccess(_E)
if mibBuilder.loadTexts:loopdetectPortProtectFlag.setStatus(_A)
_LoopdetectPortReopenTime_Type=Integer32
_LoopdetectPortReopenTime_Object=MibTableColumn
loopdetectPortReopenTime=_LoopdetectPortReopenTime_Object((1,3,6,1,4,1,3902,3,102,25,2,1,7),_LoopdetectPortReopenTime_Type())
loopdetectPortReopenTime.setMaxAccess(_C)
if mibBuilder.loadTexts:loopdetectPortReopenTime.setStatus(_A)
class _LoopdetectVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_LoopdetectVlan_Type.__name__=_B
_LoopdetectVlan_Object=MibTableColumn
loopdetectVlan=_LoopdetectVlan_Object((1,3,6,1,4,1,3902,3,102,25,2,1,8),_LoopdetectVlan_Type())
loopdetectVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:loopdetectVlan.setStatus(_A)
mibBuilder.exportSymbols(_S,**{_W:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10switch':zxr10switch,'switch59vct':switch59vct,'vctTable':vctTable,'vctEntry':vctEntry,_X:vctIfindex,'vctSetIfindex':vctSetIfindex,'cableStatus':cableStatus,'doubleCableStatus1-2':doubleCableStatus1_2,'doubleCableStatus3-6':doubleCableStatus3_6,'doubleCableStatus4-5':doubleCableStatus4_5,'doubleCableStatus7-8':doubleCableStatus7_8,'doubleCableLength1-2':doubleCableLength1_2,'doubleCableLength3-6':doubleCableLength3_6,'doubleCableLength4-5':doubleCableLength4_5,'doubleCableLength7-8':doubleCableLength7_8,'switch59loopdetect':switch59loopdetect,'loopdetectReopenTime':loopdetectReopenTime,'loopdetectTable':loopdetectTable,'loopdetectEntry':loopdetectEntry,_Z:loopdetectPortIfindex,'loopdetectPortOperStatus':loopdetectPortOperStatus,'loopdetectPortControl':loopdetectPortControl,'loopdetectPortVid':loopdetectPortVid,'loopdetectPortFlag':loopdetectPortFlag,'loopdetectPortProtectFlag':loopdetectPortProtectFlag,'loopdetectPortReopenTime':loopdetectPortReopenTime,'loopdetectVlan':loopdetectVlan})