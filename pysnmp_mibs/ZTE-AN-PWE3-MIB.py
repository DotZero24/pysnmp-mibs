_h='zxAnPwe3PwVcId'
_g='disable'
_f='enable'
_e='zxAnPwe3Vcid'
_d='zxAnPwe3PortIndex'
_c='zxAnPwe3McptTimer3'
_b='zxAnPwe3McptTimer2'
_a='zxAnPwe3McptTimer1'
_Z='zxAnPwe3PvcId'
_Y='ifIndex'
_X='IF-MIB'
_W='cwordEnable'
_V='cwordDisable'
_U='encapAtmVpc'
_T='encapAtmVcc'
_S='encapCem'
_R='encapPpp'
_Q='encapHdlc'
_P='encapEth'
_O='encapEthVlan'
_N='encapAtmTranscell'
_M='encapAtmAal5'
_L='encapFrDlci'
_K='millisecond'
_J='DisplayString'
_I='read-create'
_H='encapUnknown'
_G='not-accessible'
_F='ZTE-AN-PWE3-MIB'
_E='read-write'
_D='Unsigned32'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_X,_Y)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnPwe3Mib=ModuleIdentity((1,3,6,1,4,1,3902,1015,56))
_ZxAnPwe3GlobalObjects_ObjectIdentity=ObjectIdentity
zxAnPwe3GlobalObjects=_ZxAnPwe3GlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,56,1))
class _ZxAnPwe3McptTimer1_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,4095))
_ZxAnPwe3McptTimer1_Type.__name__=_C
_ZxAnPwe3McptTimer1_Object=MibScalar
zxAnPwe3McptTimer1=_ZxAnPwe3McptTimer1_Object((1,3,6,1,4,1,3902,1015,56,1,1),_ZxAnPwe3McptTimer1_Type())
zxAnPwe3McptTimer1.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPwe3McptTimer1.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwe3McptTimer1.setUnits(_K)
class _ZxAnPwe3McptTimer2_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,4095))
_ZxAnPwe3McptTimer2_Type.__name__=_C
_ZxAnPwe3McptTimer2_Object=MibScalar
zxAnPwe3McptTimer2=_ZxAnPwe3McptTimer2_Object((1,3,6,1,4,1,3902,1015,56,1,2),_ZxAnPwe3McptTimer2_Type())
zxAnPwe3McptTimer2.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPwe3McptTimer2.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwe3McptTimer2.setUnits(_K)
class _ZxAnPwe3McptTimer3_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,4095))
_ZxAnPwe3McptTimer3_Type.__name__=_C
_ZxAnPwe3McptTimer3_Object=MibScalar
zxAnPwe3McptTimer3=_ZxAnPwe3McptTimer3_Object((1,3,6,1,4,1,3902,1015,56,1,3),_ZxAnPwe3McptTimer3_Type())
zxAnPwe3McptTimer3.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPwe3McptTimer3.setStatus(_A)
if mibBuilder.loadTexts:zxAnPwe3McptTimer3.setUnits(_K)
_ZxAnPwe3Objects_ObjectIdentity=ObjectIdentity
zxAnPwe3Objects=_ZxAnPwe3Objects_ObjectIdentity((1,3,6,1,4,1,3902,1015,56,2))
_ZxAnPwe3PortAtmEncapTable_Object=MibTable
zxAnPwe3PortAtmEncapTable=_ZxAnPwe3PortAtmEncapTable_Object((1,3,6,1,4,1,3902,1015,56,2,1))
if mibBuilder.loadTexts:zxAnPwe3PortAtmEncapTable.setStatus(_A)
_ZxAnPwe3PortAtmEncapEntry_Object=MibTableRow
zxAnPwe3PortAtmEncapEntry=_ZxAnPwe3PortAtmEncapEntry_Object((1,3,6,1,4,1,3902,1015,56,2,1,1))
zxAnPwe3PortAtmEncapEntry.setIndexNames((0,_X,_Y),(0,_F,_Z))
if mibBuilder.loadTexts:zxAnPwe3PortAtmEncapEntry.setStatus(_A)
_ZxAnPwe3PvcId_Type=Integer32
_ZxAnPwe3PvcId_Object=MibTableColumn
zxAnPwe3PvcId=_ZxAnPwe3PvcId_Object((1,3,6,1,4,1,3902,1015,56,2,1,1,1),_ZxAnPwe3PvcId_Type())
zxAnPwe3PvcId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPwe3PvcId.setStatus(_A)
class _ZxAnPwe3PortMaxCellsPerPacket_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_ZxAnPwe3PortMaxCellsPerPacket_Type.__name__=_C
_ZxAnPwe3PortMaxCellsPerPacket_Object=MibTableColumn
zxAnPwe3PortMaxCellsPerPacket=_ZxAnPwe3PortMaxCellsPerPacket_Object((1,3,6,1,4,1,3902,1015,56,2,1,1,2),_ZxAnPwe3PortMaxCellsPerPacket_Type())
zxAnPwe3PortMaxCellsPerPacket.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPwe3PortMaxCellsPerPacket.setStatus(_A)
class _ZxAnPwe3PortMcptTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noUse',0),(_a,1),(_b,2),(_c,3)))
_ZxAnPwe3PortMcptTimer_Type.__name__=_C
_ZxAnPwe3PortMcptTimer_Object=MibTableColumn
zxAnPwe3PortMcptTimer=_ZxAnPwe3PortMcptTimer_Object((1,3,6,1,4,1,3902,1015,56,2,1,1,3),_ZxAnPwe3PortMcptTimer_Type())
zxAnPwe3PortMcptTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPwe3PortMcptTimer.setStatus(_A)
class _ZxAnPwe3PortEncapsulationType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('encapAtmAal01to1',1),('encapAtmAal0nto1',2),('encapAtmAal5pdu',3),('encapEthAal5sdu',4)))
_ZxAnPwe3PortEncapsulationType_Type.__name__=_C
_ZxAnPwe3PortEncapsulationType_Object=MibTableColumn
zxAnPwe3PortEncapsulationType=_ZxAnPwe3PortEncapsulationType_Object((1,3,6,1,4,1,3902,1015,56,2,1,1,4),_ZxAnPwe3PortEncapsulationType_Type())
zxAnPwe3PortEncapsulationType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPwe3PortEncapsulationType.setStatus(_A)
_ZxAnPwe3PortToVCMappingTable_Object=MibTable
zxAnPwe3PortToVCMappingTable=_ZxAnPwe3PortToVCMappingTable_Object((1,3,6,1,4,1,3902,1015,56,2,2))
if mibBuilder.loadTexts:zxAnPwe3PortToVCMappingTable.setStatus(_A)
_ZxAnPwe3PortToVCMappingEntry_Object=MibTableRow
zxAnPwe3PortToVCMappingEntry=_ZxAnPwe3PortToVCMappingEntry_Object((1,3,6,1,4,1,3902,1015,56,2,2,1))
zxAnPwe3PortToVCMappingEntry.setIndexNames((0,_F,_d),(0,_F,_e))
if mibBuilder.loadTexts:zxAnPwe3PortToVCMappingEntry.setStatus(_A)
_ZxAnPwe3PortIndex_Type=ZxAnIfindex
_ZxAnPwe3PortIndex_Object=MibTableColumn
zxAnPwe3PortIndex=_ZxAnPwe3PortIndex_Object((1,3,6,1,4,1,3902,1015,56,2,2,1,1),_ZxAnPwe3PortIndex_Type())
zxAnPwe3PortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPwe3PortIndex.setStatus(_A)
class _ZxAnPwe3Vcid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnPwe3Vcid_Type.__name__=_D
_ZxAnPwe3Vcid_Object=MibTableColumn
zxAnPwe3Vcid=_ZxAnPwe3Vcid_Object((1,3,6,1,4,1,3902,1015,56,2,2,1,2),_ZxAnPwe3Vcid_Type())
zxAnPwe3Vcid.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPwe3Vcid.setStatus(_A)
_ZxAnPwe3PeerAddress_Type=IpAddress
_ZxAnPwe3PeerAddress_Object=MibTableColumn
zxAnPwe3PeerAddress=_ZxAnPwe3PeerAddress_Object((1,3,6,1,4,1,3902,1015,56,2,2,1,3),_ZxAnPwe3PeerAddress_Type())
zxAnPwe3PeerAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnPwe3PeerAddress.setStatus(_A)
class _ZxAnPwe3ControlWordEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_ZxAnPwe3ControlWordEnable_Type.__name__=_C
_ZxAnPwe3ControlWordEnable_Object=MibTableColumn
zxAnPwe3ControlWordEnable=_ZxAnPwe3ControlWordEnable_Object((1,3,6,1,4,1,3902,1015,56,2,2,1,4),_ZxAnPwe3ControlWordEnable_Type())
zxAnPwe3ControlWordEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnPwe3ControlWordEnable.setStatus(_A)
class _ZxAnPwe3SequenceEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_ZxAnPwe3SequenceEnable_Type.__name__=_C
_ZxAnPwe3SequenceEnable_Object=MibTableColumn
zxAnPwe3SequenceEnable=_ZxAnPwe3SequenceEnable_Object((1,3,6,1,4,1,3902,1015,56,2,2,1,5),_ZxAnPwe3SequenceEnable_Type())
zxAnPwe3SequenceEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnPwe3SequenceEnable.setStatus(_A)
_ZxAnPwe3PortVCMappingRowStatus_Type=RowStatus
_ZxAnPwe3PortVCMappingRowStatus_Object=MibTableColumn
zxAnPwe3PortVCMappingRowStatus=_ZxAnPwe3PortVCMappingRowStatus_Object((1,3,6,1,4,1,3902,1015,56,2,2,1,50),_ZxAnPwe3PortVCMappingRowStatus_Type())
zxAnPwe3PortVCMappingRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnPwe3PortVCMappingRowStatus.setStatus(_A)
_ZxAnPwe3PwTable_Object=MibTable
zxAnPwe3PwTable=_ZxAnPwe3PwTable_Object((1,3,6,1,4,1,3902,1015,56,2,4))
if mibBuilder.loadTexts:zxAnPwe3PwTable.setStatus(_A)
_ZxAnPwe3PwEntry_Object=MibTableRow
zxAnPwe3PwEntry=_ZxAnPwe3PwEntry_Object((1,3,6,1,4,1,3902,1015,56,2,4,1))
zxAnPwe3PwEntry.setIndexNames((0,_F,_h))
if mibBuilder.loadTexts:zxAnPwe3PwEntry.setStatus(_A)
class _ZxAnPwe3PwVcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ZxAnPwe3PwVcId_Type.__name__=_D
_ZxAnPwe3PwVcId_Object=MibTableColumn
zxAnPwe3PwVcId=_ZxAnPwe3PwVcId_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,1),_ZxAnPwe3PwVcId_Type())
zxAnPwe3PwVcId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnPwe3PwVcId.setStatus(_A)
class _ZxAnPwe3PwType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('pwUnknown',0),('pwSpoke',1),('pwHub',2)))
_ZxAnPwe3PwType_Type.__name__=_C
_ZxAnPwe3PwType_Object=MibTableColumn
zxAnPwe3PwType=_ZxAnPwe3PwType_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,2),_ZxAnPwe3PwType_Type())
zxAnPwe3PwType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwType.setStatus(_A)
class _ZxAnPwe3PwEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10)))
_ZxAnPwe3PwEncapType_Type.__name__=_C
_ZxAnPwe3PwEncapType_Object=MibTableColumn
zxAnPwe3PwEncapType=_ZxAnPwe3PwEncapType_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,3),_ZxAnPwe3PwEncapType_Type())
zxAnPwe3PwEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwEncapType.setStatus(_A)
_ZxAnPwe3PwVlanid_Type=Integer32
_ZxAnPwe3PwVlanid_Object=MibTableColumn
zxAnPwe3PwVlanid=_ZxAnPwe3PwVlanid_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,4),_ZxAnPwe3PwVlanid_Type())
zxAnPwe3PwVlanid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwVlanid.setStatus(_A)
class _ZxAnPwe3PwPsnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknownTunnel',0),('mplsTunnel',1),('teTunnel',2)))
_ZxAnPwe3PwPsnType_Type.__name__=_C
_ZxAnPwe3PwPsnType_Object=MibTableColumn
zxAnPwe3PwPsnType=_ZxAnPwe3PwPsnType_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,5),_ZxAnPwe3PwPsnType_Type())
zxAnPwe3PwPsnType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwPsnType.setStatus(_A)
_ZxAnPwe3PwTunnelid_Type=Unsigned32
_ZxAnPwe3PwTunnelid_Object=MibTableColumn
zxAnPwe3PwTunnelid=_ZxAnPwe3PwTunnelid_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,6),_ZxAnPwe3PwTunnelid_Type())
zxAnPwe3PwTunnelid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwTunnelid.setStatus(_A)
class _ZxAnPwe3PwInlabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnPwe3PwInlabel_Type.__name__=_D
_ZxAnPwe3PwInlabel_Object=MibTableColumn
zxAnPwe3PwInlabel=_ZxAnPwe3PwInlabel_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,7),_ZxAnPwe3PwInlabel_Type())
zxAnPwe3PwInlabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwInlabel.setStatus(_A)
class _ZxAnPwe3PwOutlabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnPwe3PwOutlabel_Type.__name__=_D
_ZxAnPwe3PwOutlabel_Object=MibTableColumn
zxAnPwe3PwOutlabel=_ZxAnPwe3PwOutlabel_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,8),_ZxAnPwe3PwOutlabel_Type())
zxAnPwe3PwOutlabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwOutlabel.setStatus(_A)
class _ZxAnPwe3PwCbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_ZxAnPwe3PwCbit_Type.__name__=_C
_ZxAnPwe3PwCbit_Object=MibTableColumn
zxAnPwe3PwCbit=_ZxAnPwe3PwCbit_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,9),_ZxAnPwe3PwCbit_Type())
zxAnPwe3PwCbit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwCbit.setStatus(_A)
class _ZxAnPwe3PwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notEstablished',0),('established',1)))
_ZxAnPwe3PwStatus_Type.__name__=_C
_ZxAnPwe3PwStatus_Object=MibTableColumn
zxAnPwe3PwStatus=_ZxAnPwe3PwStatus_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,10),_ZxAnPwe3PwStatus_Type())
zxAnPwe3PwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwStatus.setStatus(_A)
_ZxAnPwe3PwLocalGroupId_Type=Unsigned32
_ZxAnPwe3PwLocalGroupId_Object=MibTableColumn
zxAnPwe3PwLocalGroupId=_ZxAnPwe3PwLocalGroupId_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,11),_ZxAnPwe3PwLocalGroupId_Type())
zxAnPwe3PwLocalGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalGroupId.setStatus(_A)
class _ZxAnPwe3PwLocalEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10)))
_ZxAnPwe3PwLocalEncapType_Type.__name__=_C
_ZxAnPwe3PwLocalEncapType_Object=MibTableColumn
zxAnPwe3PwLocalEncapType=_ZxAnPwe3PwLocalEncapType_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,12),_ZxAnPwe3PwLocalEncapType_Type())
zxAnPwe3PwLocalEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalEncapType.setStatus(_A)
class _ZxAnPwe3PwLocalLabel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnPwe3PwLocalLabel_Type.__name__=_D
_ZxAnPwe3PwLocalLabel_Object=MibTableColumn
zxAnPwe3PwLocalLabel=_ZxAnPwe3PwLocalLabel_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,13),_ZxAnPwe3PwLocalLabel_Type())
zxAnPwe3PwLocalLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalLabel.setStatus(_A)
class _ZxAnPwe3PwLocalCbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_ZxAnPwe3PwLocalCbit_Type.__name__=_C
_ZxAnPwe3PwLocalCbit_Object=MibTableColumn
zxAnPwe3PwLocalCbit=_ZxAnPwe3PwLocalCbit_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,14),_ZxAnPwe3PwLocalCbit_Type())
zxAnPwe3PwLocalCbit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalCbit.setStatus(_A)
class _ZxAnPwe3PwLocalPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnPwe3PwLocalPortName_Type.__name__=_J
_ZxAnPwe3PwLocalPortName_Object=MibTableColumn
zxAnPwe3PwLocalPortName=_ZxAnPwe3PwLocalPortName_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,15),_ZxAnPwe3PwLocalPortName_Type())
zxAnPwe3PwLocalPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalPortName.setStatus(_A)
_ZxAnPwe3PwLocalRouterId_Type=IpAddress
_ZxAnPwe3PwLocalRouterId_Object=MibTableColumn
zxAnPwe3PwLocalRouterId=_ZxAnPwe3PwLocalRouterId_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,16),_ZxAnPwe3PwLocalRouterId_Type())
zxAnPwe3PwLocalRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalRouterId.setStatus(_A)
class _ZxAnPwe3PwLocalIfMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnPwe3PwLocalIfMtu_Type.__name__=_D
_ZxAnPwe3PwLocalIfMtu_Object=MibTableColumn
zxAnPwe3PwLocalIfMtu=_ZxAnPwe3PwLocalIfMtu_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,17),_ZxAnPwe3PwLocalIfMtu_Type())
zxAnPwe3PwLocalIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwLocalIfMtu.setStatus(_A)
_ZxAnPwe3PwRemoteGroupId_Type=Unsigned32
_ZxAnPwe3PwRemoteGroupId_Object=MibTableColumn
zxAnPwe3PwRemoteGroupId=_ZxAnPwe3PwRemoteGroupId_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,18),_ZxAnPwe3PwRemoteGroupId_Type())
zxAnPwe3PwRemoteGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemoteGroupId.setStatus(_A)
class _ZxAnPwe3PwRemoteEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10)))
_ZxAnPwe3PwRemoteEncapType_Type.__name__=_C
_ZxAnPwe3PwRemoteEncapType_Object=MibTableColumn
zxAnPwe3PwRemoteEncapType=_ZxAnPwe3PwRemoteEncapType_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,19),_ZxAnPwe3PwRemoteEncapType_Type())
zxAnPwe3PwRemoteEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemoteEncapType.setStatus(_A)
_ZxAnPwe3PwRemoteLabel_Type=Unsigned32
_ZxAnPwe3PwRemoteLabel_Object=MibTableColumn
zxAnPwe3PwRemoteLabel=_ZxAnPwe3PwRemoteLabel_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,20),_ZxAnPwe3PwRemoteLabel_Type())
zxAnPwe3PwRemoteLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemoteLabel.setStatus(_A)
class _ZxAnPwe3PwRemoteCbit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_ZxAnPwe3PwRemoteCbit_Type.__name__=_C
_ZxAnPwe3PwRemoteCbit_Object=MibTableColumn
zxAnPwe3PwRemoteCbit=_ZxAnPwe3PwRemoteCbit_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,21),_ZxAnPwe3PwRemoteCbit_Type())
zxAnPwe3PwRemoteCbit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemoteCbit.setStatus(_A)
class _ZxAnPwe3PwRemotePortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnPwe3PwRemotePortName_Type.__name__=_J
_ZxAnPwe3PwRemotePortName_Object=MibTableColumn
zxAnPwe3PwRemotePortName=_ZxAnPwe3PwRemotePortName_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,22),_ZxAnPwe3PwRemotePortName_Type())
zxAnPwe3PwRemotePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemotePortName.setStatus(_A)
_ZxAnPwe3PwRemoteRouterId_Type=IpAddress
_ZxAnPwe3PwRemoteRouterId_Object=MibTableColumn
zxAnPwe3PwRemoteRouterId=_ZxAnPwe3PwRemoteRouterId_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,23),_ZxAnPwe3PwRemoteRouterId_Type())
zxAnPwe3PwRemoteRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemoteRouterId.setStatus(_A)
_ZxAnPwe3PwRemoteIfMtu_Type=Unsigned32
_ZxAnPwe3PwRemoteIfMtu_Object=MibTableColumn
zxAnPwe3PwRemoteIfMtu=_ZxAnPwe3PwRemoteIfMtu_Object((1,3,6,1,4,1,3902,1015,56,2,4,1,24),_ZxAnPwe3PwRemoteIfMtu_Type())
zxAnPwe3PwRemoteIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnPwe3PwRemoteIfMtu.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zxAnPwe3Mib':zxAnPwe3Mib,'zxAnPwe3GlobalObjects':zxAnPwe3GlobalObjects,_a:zxAnPwe3McptTimer1,_b:zxAnPwe3McptTimer2,_c:zxAnPwe3McptTimer3,'zxAnPwe3Objects':zxAnPwe3Objects,'zxAnPwe3PortAtmEncapTable':zxAnPwe3PortAtmEncapTable,'zxAnPwe3PortAtmEncapEntry':zxAnPwe3PortAtmEncapEntry,_Z:zxAnPwe3PvcId,'zxAnPwe3PortMaxCellsPerPacket':zxAnPwe3PortMaxCellsPerPacket,'zxAnPwe3PortMcptTimer':zxAnPwe3PortMcptTimer,'zxAnPwe3PortEncapsulationType':zxAnPwe3PortEncapsulationType,'zxAnPwe3PortToVCMappingTable':zxAnPwe3PortToVCMappingTable,'zxAnPwe3PortToVCMappingEntry':zxAnPwe3PortToVCMappingEntry,_d:zxAnPwe3PortIndex,_e:zxAnPwe3Vcid,'zxAnPwe3PeerAddress':zxAnPwe3PeerAddress,'zxAnPwe3ControlWordEnable':zxAnPwe3ControlWordEnable,'zxAnPwe3SequenceEnable':zxAnPwe3SequenceEnable,'zxAnPwe3PortVCMappingRowStatus':zxAnPwe3PortVCMappingRowStatus,'zxAnPwe3PwTable':zxAnPwe3PwTable,'zxAnPwe3PwEntry':zxAnPwe3PwEntry,_h:zxAnPwe3PwVcId,'zxAnPwe3PwType':zxAnPwe3PwType,'zxAnPwe3PwEncapType':zxAnPwe3PwEncapType,'zxAnPwe3PwVlanid':zxAnPwe3PwVlanid,'zxAnPwe3PwPsnType':zxAnPwe3PwPsnType,'zxAnPwe3PwTunnelid':zxAnPwe3PwTunnelid,'zxAnPwe3PwInlabel':zxAnPwe3PwInlabel,'zxAnPwe3PwOutlabel':zxAnPwe3PwOutlabel,'zxAnPwe3PwCbit':zxAnPwe3PwCbit,'zxAnPwe3PwStatus':zxAnPwe3PwStatus,'zxAnPwe3PwLocalGroupId':zxAnPwe3PwLocalGroupId,'zxAnPwe3PwLocalEncapType':zxAnPwe3PwLocalEncapType,'zxAnPwe3PwLocalLabel':zxAnPwe3PwLocalLabel,'zxAnPwe3PwLocalCbit':zxAnPwe3PwLocalCbit,'zxAnPwe3PwLocalPortName':zxAnPwe3PwLocalPortName,'zxAnPwe3PwLocalRouterId':zxAnPwe3PwLocalRouterId,'zxAnPwe3PwLocalIfMtu':zxAnPwe3PwLocalIfMtu,'zxAnPwe3PwRemoteGroupId':zxAnPwe3PwRemoteGroupId,'zxAnPwe3PwRemoteEncapType':zxAnPwe3PwRemoteEncapType,'zxAnPwe3PwRemoteLabel':zxAnPwe3PwRemoteLabel,'zxAnPwe3PwRemoteCbit':zxAnPwe3PwRemoteCbit,'zxAnPwe3PwRemotePortName':zxAnPwe3PwRemotePortName,'zxAnPwe3PwRemoteRouterId':zxAnPwe3PwRemoteRouterId,'zxAnPwe3PwRemoteIfMtu':zxAnPwe3PwRemoteIfMtu})