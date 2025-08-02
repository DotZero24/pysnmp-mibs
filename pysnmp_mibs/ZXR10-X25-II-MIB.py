_O='zxr10X25TrunkX121Address'
_N='zxr10X25TrunkIfIndex'
_M='zxr10X25UserIfIndex'
_L='zxr10X25StatLapbIndex'
_K='zxr10X25LapbStatIfIndex'
_J='zxr10X25SVCNo'
_I='zxr10X25OperIfIndex'
_H='zxr10X25PVCNo'
_G='NotificationType'
_F='Integer32'
_E='ZXR10-X25-II-MIB'
_D='DisplayString'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
class DisplayString(OctetString):0
class UShort(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class UChar(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class UCHAR(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class X25Address(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10X25MIBII_ObjectIdentity=ObjectIdentity
zxr10X25MIBII=_Zxr10X25MIBII_ObjectIdentity((1,3,6,1,4,1,3902,3,4001))
_Zxr10X25II_ObjectIdentity=ObjectIdentity
zxr10X25II=_Zxr10X25II_ObjectIdentity((1,3,6,1,4,1,3902,3,4001,1))
_Zxr10X25PVCTable_Object=MibTable
zxr10X25PVCTable=_Zxr10X25PVCTable_Object((1,3,6,1,4,1,3902,3,4001,1,4))
if mibBuilder.loadTexts:zxr10X25PVCTable.setStatus(_A)
_Zxr10X25PVCEntry_Object=MibTableRow
zxr10X25PVCEntry=_Zxr10X25PVCEntry_Object((1,3,6,1,4,1,3902,3,4001,1,4,1))
zxr10X25PVCEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:zxr10X25PVCEntry.setStatus(_A)
_Zxr10X25PVCRowStatus_Type=RowStatus
_Zxr10X25PVCRowStatus_Object=MibTableColumn
zxr10X25PVCRowStatus=_Zxr10X25PVCRowStatus_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,1),_Zxr10X25PVCRowStatus_Type())
zxr10X25PVCRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25PVCRowStatus.setStatus(_A)
_Zxr10X25PVCNo_Type=UShort
_Zxr10X25PVCNo_Object=MibTableColumn
zxr10X25PVCNo=_Zxr10X25PVCNo_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,2),_Zxr10X25PVCNo_Type())
zxr10X25PVCNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25PVCNo.setStatus(_A)
_Zxr10X25PVCStartLcn_Type=UShort
_Zxr10X25PVCStartLcn_Object=MibTableColumn
zxr10X25PVCStartLcn=_Zxr10X25PVCStartLcn_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,3),_Zxr10X25PVCStartLcn_Type())
zxr10X25PVCStartLcn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25PVCStartLcn.setStatus(_A)
_Zxr10X25PVCNextLcn_Type=UShort
_Zxr10X25PVCNextLcn_Object=MibTableColumn
zxr10X25PVCNextLcn=_Zxr10X25PVCNextLcn_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,4),_Zxr10X25PVCNextLcn_Type())
zxr10X25PVCNextLcn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25PVCNextLcn.setStatus(_A)
class _Zxr10X25PVCStartPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25PVCStartPortName_Type.__name__=_D
_Zxr10X25PVCStartPortName_Object=MibTableColumn
zxr10X25PVCStartPortName=_Zxr10X25PVCStartPortName_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,5),_Zxr10X25PVCStartPortName_Type())
zxr10X25PVCStartPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25PVCStartPortName.setStatus(_A)
class _Zxr10X25PVCNextPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25PVCNextPortName_Type.__name__=_D
_Zxr10X25PVCNextPortName_Object=MibTableColumn
zxr10X25PVCNextPortName=_Zxr10X25PVCNextPortName_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,6),_Zxr10X25PVCNextPortName_Type())
zxr10X25PVCNextPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25PVCNextPortName.setStatus(_A)
_Zxr10X25PVCStartPortIfIndex_Type=Unsigned32
_Zxr10X25PVCStartPortIfIndex_Object=MibTableColumn
zxr10X25PVCStartPortIfIndex=_Zxr10X25PVCStartPortIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,7),_Zxr10X25PVCStartPortIfIndex_Type())
zxr10X25PVCStartPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25PVCStartPortIfIndex.setStatus(_A)
_Zxr10X25PVCNextPortIfIndex_Type=Unsigned32
_Zxr10X25PVCNextPortIfIndex_Object=MibTableColumn
zxr10X25PVCNextPortIfIndex=_Zxr10X25PVCNextPortIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,4,1,8),_Zxr10X25PVCNextPortIfIndex_Type())
zxr10X25PVCNextPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25PVCNextPortIfIndex.setStatus(_A)
_Zxr10X25OperTable_Object=MibTable
zxr10X25OperTable=_Zxr10X25OperTable_Object((1,3,6,1,4,1,3902,3,4001,1,6))
if mibBuilder.loadTexts:zxr10X25OperTable.setStatus(_A)
_Zxr10X25OperEntry_Object=MibTableRow
zxr10X25OperEntry=_Zxr10X25OperEntry_Object((1,3,6,1,4,1,3902,3,4001,1,6,1))
zxr10X25OperEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:zxr10X25OperEntry.setStatus(_A)
class _Zxr10X25OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6,7,8,9,10,11)));namedValues=NamedValues(*(('active',1),('modify',4),('resetDefault',6),('encapFrx25',7),('encapX25',8),('noencap',9),('enable',10),('noenable',11)))
_Zxr10X25OperStatus_Type.__name__=_F
_Zxr10X25OperStatus_Object=MibTableColumn
zxr10X25OperStatus=_Zxr10X25OperStatus_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,1),_Zxr10X25OperStatus_Type())
zxr10X25OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperStatus.setStatus(_A)
_Zxr10X25OperIfIndex_Type=Unsigned32
_Zxr10X25OperIfIndex_Object=MibTableColumn
zxr10X25OperIfIndex=_Zxr10X25OperIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,2),_Zxr10X25OperIfIndex_Type())
zxr10X25OperIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25OperIfIndex.setStatus(_A)
_Zxr10X25OperLapbMode_Type=UCHAR
_Zxr10X25OperLapbMode_Object=MibTableColumn
zxr10X25OperLapbMode=_Zxr10X25OperLapbMode_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,3),_Zxr10X25OperLapbMode_Type())
zxr10X25OperLapbMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbMode.setStatus(_A)
_Zxr10X25OperLapbPSSize_Type=UShort
_Zxr10X25OperLapbPSSize_Object=MibTableColumn
zxr10X25OperLapbPSSize=_Zxr10X25OperLapbPSSize_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,4),_Zxr10X25OperLapbPSSize_Type())
zxr10X25OperLapbPSSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPSSize.setStatus(_A)
_Zxr10X25OperLapbWinSize_Type=UShort
_Zxr10X25OperLapbWinSize_Object=MibTableColumn
zxr10X25OperLapbWinSize=_Zxr10X25OperLapbWinSize_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,5),_Zxr10X25OperLapbWinSize_Type())
zxr10X25OperLapbWinSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbWinSize.setStatus(_A)
_Zxr10X25OperLapbRetranCount_Type=UShort
_Zxr10X25OperLapbRetranCount_Object=MibTableColumn
zxr10X25OperLapbRetranCount=_Zxr10X25OperLapbRetranCount_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,6),_Zxr10X25OperLapbRetranCount_Type())
zxr10X25OperLapbRetranCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbRetranCount.setStatus(_A)
_Zxr10X25OperLapbTimeoutT1_Type=UShort
_Zxr10X25OperLapbTimeoutT1_Object=MibTableColumn
zxr10X25OperLapbTimeoutT1=_Zxr10X25OperLapbTimeoutT1_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,7),_Zxr10X25OperLapbTimeoutT1_Type())
zxr10X25OperLapbTimeoutT1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbTimeoutT1.setStatus(_A)
_Zxr10X25OperLapbTimeoutT2_Type=UShort
_Zxr10X25OperLapbTimeoutT2_Object=MibTableColumn
zxr10X25OperLapbTimeoutT2=_Zxr10X25OperLapbTimeoutT2_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,8),_Zxr10X25OperLapbTimeoutT2_Type())
zxr10X25OperLapbTimeoutT2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbTimeoutT2.setStatus(_A)
_Zxr10X25OperLapbTimeoutT3_Type=UShort
_Zxr10X25OperLapbTimeoutT3_Object=MibTableColumn
zxr10X25OperLapbTimeoutT3=_Zxr10X25OperLapbTimeoutT3_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,9),_Zxr10X25OperLapbTimeoutT3_Type())
zxr10X25OperLapbTimeoutT3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbTimeoutT3.setStatus(_A)
_Zxr10X25OperLapbPktMaxVC_Type=UShort
_Zxr10X25OperLapbPktMaxVC_Object=MibTableColumn
zxr10X25OperLapbPktMaxVC=_Zxr10X25OperLapbPktMaxVC_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,10),_Zxr10X25OperLapbPktMaxVC_Type())
zxr10X25OperLapbPktMaxVC.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktMaxVC.setStatus(_A)
_Zxr10X25OperLapbPktT20_Type=UShort
_Zxr10X25OperLapbPktT20_Object=MibTableColumn
zxr10X25OperLapbPktT20=_Zxr10X25OperLapbPktT20_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,11),_Zxr10X25OperLapbPktT20_Type())
zxr10X25OperLapbPktT20.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktT20.setStatus(_A)
_Zxr10X25OperLapbPktT21_Type=UShort
_Zxr10X25OperLapbPktT21_Object=MibTableColumn
zxr10X25OperLapbPktT21=_Zxr10X25OperLapbPktT21_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,12),_Zxr10X25OperLapbPktT21_Type())
zxr10X25OperLapbPktT21.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktT21.setStatus(_A)
_Zxr10X25OperLapbPktT22_Type=UShort
_Zxr10X25OperLapbPktT22_Object=MibTableColumn
zxr10X25OperLapbPktT22=_Zxr10X25OperLapbPktT22_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,13),_Zxr10X25OperLapbPktT22_Type())
zxr10X25OperLapbPktT22.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktT22.setStatus(_A)
_Zxr10X25OperLapbPktT23_Type=UShort
_Zxr10X25OperLapbPktT23_Object=MibTableColumn
zxr10X25OperLapbPktT23=_Zxr10X25OperLapbPktT23_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,14),_Zxr10X25OperLapbPktT23_Type())
zxr10X25OperLapbPktT23.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktT23.setStatus(_A)
_Zxr10X25OperLapbPktWinSize_Type=UShort
_Zxr10X25OperLapbPktWinSize_Object=MibTableColumn
zxr10X25OperLapbPktWinSize=_Zxr10X25OperLapbPktWinSize_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,15),_Zxr10X25OperLapbPktWinSize_Type())
zxr10X25OperLapbPktWinSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktWinSize.setStatus(_A)
_Zxr10X25OperLapbPktPSize_Type=UShort
_Zxr10X25OperLapbPktPSize_Object=MibTableColumn
zxr10X25OperLapbPktPSize=_Zxr10X25OperLapbPktPSize_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,16),_Zxr10X25OperLapbPktPSize_Type())
zxr10X25OperLapbPktPSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktPSize.setStatus(_A)
_Zxr10X25OperLapbPktSvcIdleTime_Type=UShort
_Zxr10X25OperLapbPktSvcIdleTime_Object=MibTableColumn
zxr10X25OperLapbPktSvcIdleTime=_Zxr10X25OperLapbPktSvcIdleTime_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,17),_Zxr10X25OperLapbPktSvcIdleTime_Type())
zxr10X25OperLapbPktSvcIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbPktSvcIdleTime.setStatus(_A)
_Zxr10X25OperLapbDteDce_Type=UCHAR
_Zxr10X25OperLapbDteDce_Object=MibTableColumn
zxr10X25OperLapbDteDce=_Zxr10X25OperLapbDteDce_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,18),_Zxr10X25OperLapbDteDce_Type())
zxr10X25OperLapbDteDce.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbDteDce.setStatus(_A)
_Zxr10X25OperLapbUserOrTrunk_Type=UCHAR
_Zxr10X25OperLapbUserOrTrunk_Object=MibTableColumn
zxr10X25OperLapbUserOrTrunk=_Zxr10X25OperLapbUserOrTrunk_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,19),_Zxr10X25OperLapbUserOrTrunk_Type())
zxr10X25OperLapbUserOrTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OperLapbUserOrTrunk.setStatus(_A)
class _Zxr10X25OperIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25OperIfName_Type.__name__=_D
_Zxr10X25OperIfName_Object=MibTableColumn
zxr10X25OperIfName=_Zxr10X25OperIfName_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,20),_Zxr10X25OperIfName_Type())
zxr10X25OperIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25OperIfName.setStatus(_A)
_Zxr10X25OperLabpStatus_Type=UCHAR
_Zxr10X25OperLabpStatus_Object=MibTableColumn
zxr10X25OperLabpStatus=_Zxr10X25OperLabpStatus_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,21),_Zxr10X25OperLabpStatus_Type())
zxr10X25OperLabpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25OperLabpStatus.setStatus(_A)
_Zxr10X25OperInterfaceType_Type=UCHAR
_Zxr10X25OperInterfaceType_Object=MibTableColumn
zxr10X25OperInterfaceType=_Zxr10X25OperInterfaceType_Object((1,3,6,1,4,1,3902,3,4001,1,6,1,22),_Zxr10X25OperInterfaceType_Type())
zxr10X25OperInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25OperInterfaceType.setStatus(_A)
_Zxr10X25SVCTable_Object=MibTable
zxr10X25SVCTable=_Zxr10X25SVCTable_Object((1,3,6,1,4,1,3902,3,4001,1,7))
if mibBuilder.loadTexts:zxr10X25SVCTable.setStatus(_A)
_Zxr10X25SVCEntry_Object=MibTableRow
zxr10X25SVCEntry=_Zxr10X25SVCEntry_Object((1,3,6,1,4,1,3902,3,4001,1,7,1))
zxr10X25SVCEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:zxr10X25SVCEntry.setStatus(_A)
_Zxr10X25SVCNo_Type=UShort
_Zxr10X25SVCNo_Object=MibTableColumn
zxr10X25SVCNo=_Zxr10X25SVCNo_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,1),_Zxr10X25SVCNo_Type())
zxr10X25SVCNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCNo.setStatus(_A)
_Zxr10X25SVCStartLcn_Type=UShort
_Zxr10X25SVCStartLcn_Object=MibTableColumn
zxr10X25SVCStartLcn=_Zxr10X25SVCStartLcn_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,2),_Zxr10X25SVCStartLcn_Type())
zxr10X25SVCStartLcn.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCStartLcn.setStatus(_A)
_Zxr10X25SVCNextLcn_Type=UShort
_Zxr10X25SVCNextLcn_Object=MibTableColumn
zxr10X25SVCNextLcn=_Zxr10X25SVCNextLcn_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,3),_Zxr10X25SVCNextLcn_Type())
zxr10X25SVCNextLcn.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCNextLcn.setStatus(_A)
class _Zxr10X25SVCStartPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25SVCStartPortName_Type.__name__=_D
_Zxr10X25SVCStartPortName_Object=MibTableColumn
zxr10X25SVCStartPortName=_Zxr10X25SVCStartPortName_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,4),_Zxr10X25SVCStartPortName_Type())
zxr10X25SVCStartPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCStartPortName.setStatus(_A)
class _Zxr10X25SVCNextPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25SVCNextPortName_Type.__name__=_D
_Zxr10X25SVCNextPortName_Object=MibTableColumn
zxr10X25SVCNextPortName=_Zxr10X25SVCNextPortName_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,5),_Zxr10X25SVCNextPortName_Type())
zxr10X25SVCNextPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCNextPortName.setStatus(_A)
_Zxr10X25SVCStartPortIfIndex_Type=Unsigned32
_Zxr10X25SVCStartPortIfIndex_Object=MibTableColumn
zxr10X25SVCStartPortIfIndex=_Zxr10X25SVCStartPortIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,6),_Zxr10X25SVCStartPortIfIndex_Type())
zxr10X25SVCStartPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCStartPortIfIndex.setStatus(_A)
_Zxr10X25SVCNextPortIfIndex_Type=Unsigned32
_Zxr10X25SVCNextPortIfIndex_Object=MibTableColumn
zxr10X25SVCNextPortIfIndex=_Zxr10X25SVCNextPortIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,7,1,7),_Zxr10X25SVCNextPortIfIndex_Type())
zxr10X25SVCNextPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25SVCNextPortIfIndex.setStatus(_A)
_Zxr10X25LapbFlowTable_Object=MibTable
zxr10X25LapbFlowTable=_Zxr10X25LapbFlowTable_Object((1,3,6,1,4,1,3902,3,4001,1,8))
if mibBuilder.loadTexts:zxr10X25LapbFlowTable.setStatus(_A)
_Zxr10X25LapbFlowEntry_Object=MibTableRow
zxr10X25LapbFlowEntry=_Zxr10X25LapbFlowEntry_Object((1,3,6,1,4,1,3902,3,4001,1,8,1))
zxr10X25LapbFlowEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:zxr10X25LapbFlowEntry.setStatus(_A)
_Zxr10X25LapbFlowBusyDefers_Type=Unsigned32
_Zxr10X25LapbFlowBusyDefers_Object=MibTableColumn
zxr10X25LapbFlowBusyDefers=_Zxr10X25LapbFlowBusyDefers_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,1),_Zxr10X25LapbFlowBusyDefers_Type())
zxr10X25LapbFlowBusyDefers.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowBusyDefers.setStatus(_A)
_Zxr10X25LapbFlowRejOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowRejOutPkts_Object=MibTableColumn
zxr10X25LapbFlowRejOutPkts=_Zxr10X25LapbFlowRejOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,2),_Zxr10X25LapbFlowRejOutPkts_Type())
zxr10X25LapbFlowRejOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowRejOutPkts.setStatus(_A)
_Zxr10X25LapbFlowRejInPkts_Type=Unsigned32
_Zxr10X25LapbFlowRejInPkts_Object=MibTableColumn
zxr10X25LapbFlowRejInPkts=_Zxr10X25LapbFlowRejInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,3),_Zxr10X25LapbFlowRejInPkts_Type())
zxr10X25LapbFlowRejInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowRejInPkts.setStatus(_A)
_Zxr10X25LapbFlowT1Timeouts_Type=Unsigned32
_Zxr10X25LapbFlowT1Timeouts_Object=MibTableColumn
zxr10X25LapbFlowT1Timeouts=_Zxr10X25LapbFlowT1Timeouts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,4),_Zxr10X25LapbFlowT1Timeouts_Type())
zxr10X25LapbFlowT1Timeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowT1Timeouts.setStatus(_A)
_Zxr10X25LapbFlowRROutPkts_Type=Unsigned32
_Zxr10X25LapbFlowRROutPkts_Object=MibTableColumn
zxr10X25LapbFlowRROutPkts=_Zxr10X25LapbFlowRROutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,5),_Zxr10X25LapbFlowRROutPkts_Type())
zxr10X25LapbFlowRROutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowRROutPkts.setStatus(_A)
_Zxr10X25LapbFlowRRInPkts_Type=Unsigned32
_Zxr10X25LapbFlowRRInPkts_Object=MibTableColumn
zxr10X25LapbFlowRRInPkts=_Zxr10X25LapbFlowRRInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,6),_Zxr10X25LapbFlowRRInPkts_Type())
zxr10X25LapbFlowRRInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowRRInPkts.setStatus(_A)
_Zxr10X25LapbFlowRNROutPkts_Type=Unsigned32
_Zxr10X25LapbFlowRNROutPkts_Object=MibTableColumn
zxr10X25LapbFlowRNROutPkts=_Zxr10X25LapbFlowRNROutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,7),_Zxr10X25LapbFlowRNROutPkts_Type())
zxr10X25LapbFlowRNROutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowRNROutPkts.setStatus(_A)
_Zxr10X25LapbFlowRNRInPkts_Type=Unsigned32
_Zxr10X25LapbFlowRNRInPkts_Object=MibTableColumn
zxr10X25LapbFlowRNRInPkts=_Zxr10X25LapbFlowRNRInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,8),_Zxr10X25LapbFlowRNRInPkts_Type())
zxr10X25LapbFlowRNRInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowRNRInPkts.setStatus(_A)
_Zxr10X25LapbFlowIOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowIOutPkts_Object=MibTableColumn
zxr10X25LapbFlowIOutPkts=_Zxr10X25LapbFlowIOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,9),_Zxr10X25LapbFlowIOutPkts_Type())
zxr10X25LapbFlowIOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowIOutPkts.setStatus(_A)
_Zxr10X25LapbFlowIInPkts_Type=Unsigned32
_Zxr10X25LapbFlowIInPkts_Object=MibTableColumn
zxr10X25LapbFlowIInPkts=_Zxr10X25LapbFlowIInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,10),_Zxr10X25LapbFlowIInPkts_Type())
zxr10X25LapbFlowIInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowIInPkts.setStatus(_A)
_Zxr10X25LapbFlowDMOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowDMOutPkts_Object=MibTableColumn
zxr10X25LapbFlowDMOutPkts=_Zxr10X25LapbFlowDMOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,11),_Zxr10X25LapbFlowDMOutPkts_Type())
zxr10X25LapbFlowDMOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowDMOutPkts.setStatus(_A)
_Zxr10X25LapbFlowDMInPkts_Type=Unsigned32
_Zxr10X25LapbFlowDMInPkts_Object=MibTableColumn
zxr10X25LapbFlowDMInPkts=_Zxr10X25LapbFlowDMInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,12),_Zxr10X25LapbFlowDMInPkts_Type())
zxr10X25LapbFlowDMInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowDMInPkts.setStatus(_A)
_Zxr10X25LapbFlowSABOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowSABOutPkts_Object=MibTableColumn
zxr10X25LapbFlowSABOutPkts=_Zxr10X25LapbFlowSABOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,13),_Zxr10X25LapbFlowSABOutPkts_Type())
zxr10X25LapbFlowSABOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowSABOutPkts.setStatus(_A)
_Zxr10X25LapbFlowSABInPkts_Type=Unsigned32
_Zxr10X25LapbFlowSABInPkts_Object=MibTableColumn
zxr10X25LapbFlowSABInPkts=_Zxr10X25LapbFlowSABInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,14),_Zxr10X25LapbFlowSABInPkts_Type())
zxr10X25LapbFlowSABInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowSABInPkts.setStatus(_A)
_Zxr10X25LapbFlowUAOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowUAOutPkts_Object=MibTableColumn
zxr10X25LapbFlowUAOutPkts=_Zxr10X25LapbFlowUAOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,15),_Zxr10X25LapbFlowUAOutPkts_Type())
zxr10X25LapbFlowUAOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowUAOutPkts.setStatus(_A)
_Zxr10X25LapbFlowUAInPkts_Type=Unsigned32
_Zxr10X25LapbFlowUAInPkts_Object=MibTableColumn
zxr10X25LapbFlowUAInPkts=_Zxr10X25LapbFlowUAInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,16),_Zxr10X25LapbFlowUAInPkts_Type())
zxr10X25LapbFlowUAInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowUAInPkts.setStatus(_A)
_Zxr10X25LapbFlowDISCOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowDISCOutPkts_Object=MibTableColumn
zxr10X25LapbFlowDISCOutPkts=_Zxr10X25LapbFlowDISCOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,17),_Zxr10X25LapbFlowDISCOutPkts_Type())
zxr10X25LapbFlowDISCOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowDISCOutPkts.setStatus(_A)
_Zxr10X25LapbFlowDISCInPkts_Type=Unsigned32
_Zxr10X25LapbFlowDISCInPkts_Object=MibTableColumn
zxr10X25LapbFlowDISCInPkts=_Zxr10X25LapbFlowDISCInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,18),_Zxr10X25LapbFlowDISCInPkts_Type())
zxr10X25LapbFlowDISCInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowDISCInPkts.setStatus(_A)
_Zxr10X25LapbFlowFRMROutPkts_Type=Unsigned32
_Zxr10X25LapbFlowFRMROutPkts_Object=MibTableColumn
zxr10X25LapbFlowFRMROutPkts=_Zxr10X25LapbFlowFRMROutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,19),_Zxr10X25LapbFlowFRMROutPkts_Type())
zxr10X25LapbFlowFRMROutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowFRMROutPkts.setStatus(_A)
_Zxr10X25LapbFlowFRMRInPkts_Type=Unsigned32
_Zxr10X25LapbFlowFRMRInPkts_Object=MibTableColumn
zxr10X25LapbFlowFRMRInPkts=_Zxr10X25LapbFlowFRMRInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,20),_Zxr10X25LapbFlowFRMRInPkts_Type())
zxr10X25LapbFlowFRMRInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowFRMRInPkts.setStatus(_A)
_Zxr10X25LapbFlowOutPkts_Type=Unsigned32
_Zxr10X25LapbFlowOutPkts_Object=MibTableColumn
zxr10X25LapbFlowOutPkts=_Zxr10X25LapbFlowOutPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,21),_Zxr10X25LapbFlowOutPkts_Type())
zxr10X25LapbFlowOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowOutPkts.setStatus(_A)
_Zxr10X25LapbFlowInPkts_Type=Unsigned32
_Zxr10X25LapbFlowInPkts_Object=MibTableColumn
zxr10X25LapbFlowInPkts=_Zxr10X25LapbFlowInPkts_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,22),_Zxr10X25LapbFlowInPkts_Type())
zxr10X25LapbFlowInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowInPkts.setStatus(_A)
_Zxr10X25LapbFlowStateChanges_Type=Unsigned32
_Zxr10X25LapbFlowStateChanges_Object=MibTableColumn
zxr10X25LapbFlowStateChanges=_Zxr10X25LapbFlowStateChanges_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,23),_Zxr10X25LapbFlowStateChanges_Type())
zxr10X25LapbFlowStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbFlowStateChanges.setStatus(_A)
_Zxr10X25LapbStatIfIndex_Type=Unsigned32
_Zxr10X25LapbStatIfIndex_Object=MibTableColumn
zxr10X25LapbStatIfIndex=_Zxr10X25LapbStatIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,8,1,24),_Zxr10X25LapbStatIfIndex_Type())
zxr10X25LapbStatIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25LapbStatIfIndex.setStatus(_A)
_Zxr10X25StatTable_Object=MibTable
zxr10X25StatTable=_Zxr10X25StatTable_Object((1,3,6,1,4,1,3902,3,4001,1,9))
if mibBuilder.loadTexts:zxr10X25StatTable.setStatus(_A)
_Zxr10X25StatEntry_Object=MibTableRow
zxr10X25StatEntry=_Zxr10X25StatEntry_Object((1,3,6,1,4,1,3902,3,4001,1,9,1))
zxr10X25StatEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:zxr10X25StatEntry.setStatus(_A)
_Zxr10X25StatLapbIndex_Type=Unsigned32
_Zxr10X25StatLapbIndex_Object=MibTableColumn
zxr10X25StatLapbIndex=_Zxr10X25StatLapbIndex_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,1),_Zxr10X25StatLapbIndex_Type())
zxr10X25StatLapbIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25StatLapbIndex.setStatus(_A)
_Zxr10StatRecvX25CALLREQUESTCnt_Type=Unsigned32
_Zxr10StatRecvX25CALLREQUESTCnt_Object=MibTableColumn
zxr10StatRecvX25CALLREQUESTCnt=_Zxr10StatRecvX25CALLREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,2),_Zxr10StatRecvX25CALLREQUESTCnt_Type())
zxr10StatRecvX25CALLREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25CALLREQUESTCnt.setStatus(_A)
_Zxr10StatRecvX25CALLACCEPTEDCnt_Type=Unsigned32
_Zxr10StatRecvX25CALLACCEPTEDCnt_Object=MibTableColumn
zxr10StatRecvX25CALLACCEPTEDCnt=_Zxr10StatRecvX25CALLACCEPTEDCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,3),_Zxr10StatRecvX25CALLACCEPTEDCnt_Type())
zxr10StatRecvX25CALLACCEPTEDCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25CALLACCEPTEDCnt.setStatus(_A)
_Zxr10StatRecvX25CLEARREQUESTCnt_Type=Unsigned32
_Zxr10StatRecvX25CLEARREQUESTCnt_Object=MibTableColumn
zxr10StatRecvX25CLEARREQUESTCnt=_Zxr10StatRecvX25CLEARREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,4),_Zxr10StatRecvX25CLEARREQUESTCnt_Type())
zxr10StatRecvX25CLEARREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25CLEARREQUESTCnt.setStatus(_A)
_Zxr10StatRecvX25CLEARCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatRecvX25CLEARCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatRecvX25CLEARCONFIRMATIONCnt=_Zxr10StatRecvX25CLEARCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,5),_Zxr10StatRecvX25CLEARCONFIRMATIONCnt_Type())
zxr10StatRecvX25CLEARCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25CLEARCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatRecvX25DATACnt_Type=Unsigned32
_Zxr10StatRecvX25DATACnt_Object=MibTableColumn
zxr10StatRecvX25DATACnt=_Zxr10StatRecvX25DATACnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,6),_Zxr10StatRecvX25DATACnt_Type())
zxr10StatRecvX25DATACnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25DATACnt.setStatus(_A)
_Zxr10StatRecvX25INTERRUPTCnt_Type=Unsigned32
_Zxr10StatRecvX25INTERRUPTCnt_Object=MibTableColumn
zxr10StatRecvX25INTERRUPTCnt=_Zxr10StatRecvX25INTERRUPTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,7),_Zxr10StatRecvX25INTERRUPTCnt_Type())
zxr10StatRecvX25INTERRUPTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25INTERRUPTCnt.setStatus(_A)
_Zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt=_Zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,8),_Zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt_Type())
zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatRecvX25RRCnt_Type=Unsigned32
_Zxr10StatRecvX25RRCnt_Object=MibTableColumn
zxr10StatRecvX25RRCnt=_Zxr10StatRecvX25RRCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,9),_Zxr10StatRecvX25RRCnt_Type())
zxr10StatRecvX25RRCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25RRCnt.setStatus(_A)
_Zxr10StatRecvX25RNRCnt_Type=Unsigned32
_Zxr10StatRecvX25RNRCnt_Object=MibTableColumn
zxr10StatRecvX25RNRCnt=_Zxr10StatRecvX25RNRCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,10),_Zxr10StatRecvX25RNRCnt_Type())
zxr10StatRecvX25RNRCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25RNRCnt.setStatus(_A)
_Zxr10StatRecvX25REJCnt_Type=Unsigned32
_Zxr10StatRecvX25REJCnt_Object=MibTableColumn
zxr10StatRecvX25REJCnt=_Zxr10StatRecvX25REJCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,11),_Zxr10StatRecvX25REJCnt_Type())
zxr10StatRecvX25REJCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25REJCnt.setStatus(_A)
_Zxr10StatRecvX25RESETREQUESTCnt_Type=Unsigned32
_Zxr10StatRecvX25RESETREQUESTCnt_Object=MibTableColumn
zxr10StatRecvX25RESETREQUESTCnt=_Zxr10StatRecvX25RESETREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,12),_Zxr10StatRecvX25RESETREQUESTCnt_Type())
zxr10StatRecvX25RESETREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25RESETREQUESTCnt.setStatus(_A)
_Zxr10StatRecvX25RESETCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatRecvX25RESETCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatRecvX25RESETCONFIRMATIONCnt=_Zxr10StatRecvX25RESETCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,13),_Zxr10StatRecvX25RESETCONFIRMATIONCnt_Type())
zxr10StatRecvX25RESETCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25RESETCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatRecvX25REGISTRATIONREQUESTCnt_Type=Unsigned32
_Zxr10StatRecvX25REGISTRATIONREQUESTCnt_Object=MibTableColumn
zxr10StatRecvX25REGISTRATIONREQUESTCnt=_Zxr10StatRecvX25REGISTRATIONREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,14),_Zxr10StatRecvX25REGISTRATIONREQUESTCnt_Type())
zxr10StatRecvX25REGISTRATIONREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25REGISTRATIONREQUESTCnt.setStatus(_A)
_Zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt=_Zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,15),_Zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt_Type())
zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatRecvX25RESTARTREQUESTCnt_Type=Unsigned32
_Zxr10StatRecvX25RESTARTREQUESTCnt_Object=MibTableColumn
zxr10StatRecvX25RESTARTREQUESTCnt=_Zxr10StatRecvX25RESTARTREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,16),_Zxr10StatRecvX25RESTARTREQUESTCnt_Type())
zxr10StatRecvX25RESTARTREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25RESTARTREQUESTCnt.setStatus(_A)
_Zxr10StatRecvX25RESTARTCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatRecvX25RESTARTCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatRecvX25RESTARTCONFIRMATIONCnt=_Zxr10StatRecvX25RESTARTCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,17),_Zxr10StatRecvX25RESTARTCONFIRMATIONCnt_Type())
zxr10StatRecvX25RESTARTCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25RESTARTCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatRecvX25DIAGNOSTICCnt_Type=Unsigned32
_Zxr10StatRecvX25DIAGNOSTICCnt_Object=MibTableColumn
zxr10StatRecvX25DIAGNOSTICCnt=_Zxr10StatRecvX25DIAGNOSTICCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,18),_Zxr10StatRecvX25DIAGNOSTICCnt_Type())
zxr10StatRecvX25DIAGNOSTICCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25DIAGNOSTICCnt.setStatus(_A)
_Zxr10StatRecvX25ILLEGALCnt_Type=Unsigned32
_Zxr10StatRecvX25ILLEGALCnt_Object=MibTableColumn
zxr10StatRecvX25ILLEGALCnt=_Zxr10StatRecvX25ILLEGALCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,19),_Zxr10StatRecvX25ILLEGALCnt_Type())
zxr10StatRecvX25ILLEGALCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25ILLEGALCnt.setStatus(_A)
_Zxr10StatRecvX25TotalDataSize_Type=Unsigned32
_Zxr10StatRecvX25TotalDataSize_Object=MibTableColumn
zxr10StatRecvX25TotalDataSize=_Zxr10StatRecvX25TotalDataSize_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,20),_Zxr10StatRecvX25TotalDataSize_Type())
zxr10StatRecvX25TotalDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatRecvX25TotalDataSize.setStatus(_A)
_Zxr10StatSendX25CALLREQUESTCnt_Type=Unsigned32
_Zxr10StatSendX25CALLREQUESTCnt_Object=MibTableColumn
zxr10StatSendX25CALLREQUESTCnt=_Zxr10StatSendX25CALLREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,21),_Zxr10StatSendX25CALLREQUESTCnt_Type())
zxr10StatSendX25CALLREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25CALLREQUESTCnt.setStatus(_A)
_Zxr10StatSendX25CALLACCEPTEDCnt_Type=Unsigned32
_Zxr10StatSendX25CALLACCEPTEDCnt_Object=MibTableColumn
zxr10StatSendX25CALLACCEPTEDCnt=_Zxr10StatSendX25CALLACCEPTEDCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,22),_Zxr10StatSendX25CALLACCEPTEDCnt_Type())
zxr10StatSendX25CALLACCEPTEDCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25CALLACCEPTEDCnt.setStatus(_A)
_Zxr10StatSendX25CLEARREQUESTCnt_Type=Unsigned32
_Zxr10StatSendX25CLEARREQUESTCnt_Object=MibTableColumn
zxr10StatSendX25CLEARREQUESTCnt=_Zxr10StatSendX25CLEARREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,23),_Zxr10StatSendX25CLEARREQUESTCnt_Type())
zxr10StatSendX25CLEARREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25CLEARREQUESTCnt.setStatus(_A)
_Zxr10StatSendX25CLEARCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatSendX25CLEARCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatSendX25CLEARCONFIRMATIONCnt=_Zxr10StatSendX25CLEARCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,24),_Zxr10StatSendX25CLEARCONFIRMATIONCnt_Type())
zxr10StatSendX25CLEARCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25CLEARCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatSendX25DATACnt_Type=Unsigned32
_Zxr10StatSendX25DATACnt_Object=MibTableColumn
zxr10StatSendX25DATACnt=_Zxr10StatSendX25DATACnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,25),_Zxr10StatSendX25DATACnt_Type())
zxr10StatSendX25DATACnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25DATACnt.setStatus(_A)
_Zxr10StatSendX25INTERRUPTCnt_Type=Unsigned32
_Zxr10StatSendX25INTERRUPTCnt_Object=MibTableColumn
zxr10StatSendX25INTERRUPTCnt=_Zxr10StatSendX25INTERRUPTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,26),_Zxr10StatSendX25INTERRUPTCnt_Type())
zxr10StatSendX25INTERRUPTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25INTERRUPTCnt.setStatus(_A)
_Zxr10StatSendX25INTERRUPTCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatSendX25INTERRUPTCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatSendX25INTERRUPTCONFIRMATIONCnt=_Zxr10StatSendX25INTERRUPTCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,27),_Zxr10StatSendX25INTERRUPTCONFIRMATIONCnt_Type())
zxr10StatSendX25INTERRUPTCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25INTERRUPTCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatSendX25RRCnt_Type=Unsigned32
_Zxr10StatSendX25RRCnt_Object=MibTableColumn
zxr10StatSendX25RRCnt=_Zxr10StatSendX25RRCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,28),_Zxr10StatSendX25RRCnt_Type())
zxr10StatSendX25RRCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25RRCnt.setStatus(_A)
_Zxr10StatSendX25RNRCnt_Type=Unsigned32
_Zxr10StatSendX25RNRCnt_Object=MibTableColumn
zxr10StatSendX25RNRCnt=_Zxr10StatSendX25RNRCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,29),_Zxr10StatSendX25RNRCnt_Type())
zxr10StatSendX25RNRCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25RNRCnt.setStatus(_A)
_Zxr10StatSendX25REJCnt_Type=Unsigned32
_Zxr10StatSendX25REJCnt_Object=MibTableColumn
zxr10StatSendX25REJCnt=_Zxr10StatSendX25REJCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,30),_Zxr10StatSendX25REJCnt_Type())
zxr10StatSendX25REJCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25REJCnt.setStatus(_A)
_Zxr10StatSendX25RESETREQUESTCnt_Type=Unsigned32
_Zxr10StatSendX25RESETREQUESTCnt_Object=MibTableColumn
zxr10StatSendX25RESETREQUESTCnt=_Zxr10StatSendX25RESETREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,31),_Zxr10StatSendX25RESETREQUESTCnt_Type())
zxr10StatSendX25RESETREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25RESETREQUESTCnt.setStatus(_A)
_Zxr10StatSendX25RESETCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatSendX25RESETCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatSendX25RESETCONFIRMATIONCnt=_Zxr10StatSendX25RESETCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,32),_Zxr10StatSendX25RESETCONFIRMATIONCnt_Type())
zxr10StatSendX25RESETCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25RESETCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatSendX25REGISTRATIONREQUESTCnt_Type=Unsigned32
_Zxr10StatSendX25REGISTRATIONREQUESTCnt_Object=MibTableColumn
zxr10StatSendX25REGISTRATIONREQUESTCnt=_Zxr10StatSendX25REGISTRATIONREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,33),_Zxr10StatSendX25REGISTRATIONREQUESTCnt_Type())
zxr10StatSendX25REGISTRATIONREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25REGISTRATIONREQUESTCnt.setStatus(_A)
_Zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt=_Zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,34),_Zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt_Type())
zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatSendX25RESTARTREQUESTCnt_Type=Unsigned32
_Zxr10StatSendX25RESTARTREQUESTCnt_Object=MibTableColumn
zxr10StatSendX25RESTARTREQUESTCnt=_Zxr10StatSendX25RESTARTREQUESTCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,35),_Zxr10StatSendX25RESTARTREQUESTCnt_Type())
zxr10StatSendX25RESTARTREQUESTCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25RESTARTREQUESTCnt.setStatus(_A)
_Zxr10StatSendX25RESTARTCONFIRMATIONCnt_Type=Unsigned32
_Zxr10StatSendX25RESTARTCONFIRMATIONCnt_Object=MibTableColumn
zxr10StatSendX25RESTARTCONFIRMATIONCnt=_Zxr10StatSendX25RESTARTCONFIRMATIONCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,36),_Zxr10StatSendX25RESTARTCONFIRMATIONCnt_Type())
zxr10StatSendX25RESTARTCONFIRMATIONCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25RESTARTCONFIRMATIONCnt.setStatus(_A)
_Zxr10StatSendX25DIAGNOSTICCnt_Type=Unsigned32
_Zxr10StatSendX25DIAGNOSTICCnt_Object=MibTableColumn
zxr10StatSendX25DIAGNOSTICCnt=_Zxr10StatSendX25DIAGNOSTICCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,37),_Zxr10StatSendX25DIAGNOSTICCnt_Type())
zxr10StatSendX25DIAGNOSTICCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25DIAGNOSTICCnt.setStatus(_A)
_Zxr10StatSendX25ILLEGALCnt_Type=Unsigned32
_Zxr10StatSendX25ILLEGALCnt_Object=MibTableColumn
zxr10StatSendX25ILLEGALCnt=_Zxr10StatSendX25ILLEGALCnt_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,38),_Zxr10StatSendX25ILLEGALCnt_Type())
zxr10StatSendX25ILLEGALCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25ILLEGALCnt.setStatus(_A)
_Zxr10StatSendX25TotalDataSize_Type=Unsigned32
_Zxr10StatSendX25TotalDataSize_Object=MibTableColumn
zxr10StatSendX25TotalDataSize=_Zxr10StatSendX25TotalDataSize_Object((1,3,6,1,4,1,3902,3,4001,1,9,1,39),_Zxr10StatSendX25TotalDataSize_Type())
zxr10StatSendX25TotalDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10StatSendX25TotalDataSize.setStatus(_A)
_Zxr10X25UserAddrTable_Object=MibTable
zxr10X25UserAddrTable=_Zxr10X25UserAddrTable_Object((1,3,6,1,4,1,3902,3,4001,1,10))
if mibBuilder.loadTexts:zxr10X25UserAddrTable.setStatus(_A)
_Zxr10X25UserAddrEntry_Object=MibTableRow
zxr10X25UserAddrEntry=_Zxr10X25UserAddrEntry_Object((1,3,6,1,4,1,3902,3,4001,1,10,1))
zxr10X25UserAddrEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:zxr10X25UserAddrEntry.setStatus(_A)
class _Zxr10X25UserX121Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Zxr10X25UserX121Address_Type.__name__=_D
_Zxr10X25UserX121Address_Object=MibTableColumn
zxr10X25UserX121Address=_Zxr10X25UserX121Address_Object((1,3,6,1,4,1,3902,3,4001,1,10,1,1),_Zxr10X25UserX121Address_Type())
zxr10X25UserX121Address.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25UserX121Address.setStatus(_A)
_Zxr10X25UserIfIndex_Type=Unsigned32
_Zxr10X25UserIfIndex_Object=MibTableColumn
zxr10X25UserIfIndex=_Zxr10X25UserIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,10,1,2),_Zxr10X25UserIfIndex_Type())
zxr10X25UserIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25UserIfIndex.setStatus(_A)
class _Zxr10X25UserIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Zxr10X25UserIfName_Type.__name__=_D
_Zxr10X25UserIfName_Object=MibTableColumn
zxr10X25UserIfName=_Zxr10X25UserIfName_Object((1,3,6,1,4,1,3902,3,4001,1,10,1,3),_Zxr10X25UserIfName_Type())
zxr10X25UserIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25UserIfName.setStatus(_A)
class _Zxr10X25UserQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3)))
_Zxr10X25UserQoS_Type.__name__=_F
_Zxr10X25UserQoS_Object=MibTableColumn
zxr10X25UserQoS=_Zxr10X25UserQoS_Object((1,3,6,1,4,1,3902,3,4001,1,10,1,4),_Zxr10X25UserQoS_Type())
zxr10X25UserQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25UserQoS.setStatus(_A)
_Zxr10X25UserRowStatus_Type=RowStatus
_Zxr10X25UserRowStatus_Object=MibTableColumn
zxr10X25UserRowStatus=_Zxr10X25UserRowStatus_Object((1,3,6,1,4,1,3902,3,4001,1,10,1,5),_Zxr10X25UserRowStatus_Type())
zxr10X25UserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25UserRowStatus.setStatus(_A)
_Zxr10X25TrunkTable_Object=MibTable
zxr10X25TrunkTable=_Zxr10X25TrunkTable_Object((1,3,6,1,4,1,3902,3,4001,1,11))
if mibBuilder.loadTexts:zxr10X25TrunkTable.setStatus(_A)
_Zxr10X25TrunkEntry_Object=MibTableRow
zxr10X25TrunkEntry=_Zxr10X25TrunkEntry_Object((1,3,6,1,4,1,3902,3,4001,1,11,1))
zxr10X25TrunkEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:zxr10X25TrunkEntry.setStatus(_A)
class _Zxr10X25TrunkX121Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_Zxr10X25TrunkX121Address_Type.__name__=_D
_Zxr10X25TrunkX121Address_Object=MibTableColumn
zxr10X25TrunkX121Address=_Zxr10X25TrunkX121Address_Object((1,3,6,1,4,1,3902,3,4001,1,11,1,1),_Zxr10X25TrunkX121Address_Type())
zxr10X25TrunkX121Address.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25TrunkX121Address.setStatus(_A)
class _Zxr10X25TrunkIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Zxr10X25TrunkIfName_Type.__name__=_D
_Zxr10X25TrunkIfName_Object=MibTableColumn
zxr10X25TrunkIfName=_Zxr10X25TrunkIfName_Object((1,3,6,1,4,1,3902,3,4001,1,11,1,2),_Zxr10X25TrunkIfName_Type())
zxr10X25TrunkIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25TrunkIfName.setStatus(_A)
class _Zxr10X25TrunkQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('first-select-trunk',1),('second-select-trunk',2),('third-select-trunk',3)))
_Zxr10X25TrunkQoS_Type.__name__=_F
_Zxr10X25TrunkQoS_Object=MibTableColumn
zxr10X25TrunkQoS=_Zxr10X25TrunkQoS_Object((1,3,6,1,4,1,3902,3,4001,1,11,1,3),_Zxr10X25TrunkQoS_Type())
zxr10X25TrunkQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25TrunkQoS.setStatus(_A)
_Zxr10X25TrunkRowStatus_Type=RowStatus
_Zxr10X25TrunkRowStatus_Object=MibTableColumn
zxr10X25TrunkRowStatus=_Zxr10X25TrunkRowStatus_Object((1,3,6,1,4,1,3902,3,4001,1,11,1,4),_Zxr10X25TrunkRowStatus_Type())
zxr10X25TrunkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25TrunkRowStatus.setStatus(_A)
_Zxr10X25TrunkIfIndex_Type=Unsigned32
_Zxr10X25TrunkIfIndex_Object=MibTableColumn
zxr10X25TrunkIfIndex=_Zxr10X25TrunkIfIndex_Object((1,3,6,1,4,1,3902,3,4001,1,11,1,5),_Zxr10X25TrunkIfIndex_Type())
zxr10X25TrunkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10X25TrunkIfIndex.setStatus(_A)
class _Zxr10X25StationAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Zxr10X25StationAddress_Type.__name__=_D
_Zxr10X25StationAddress_Object=MibScalar
zxr10X25StationAddress=_Zxr10X25StationAddress_Object((1,3,6,1,4,1,3902,3,4001,1,12),_Zxr10X25StationAddress_Type())
zxr10X25StationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25StationAddress.setStatus(_A)
class _Zxr10X25DefaultTrunk_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Zxr10X25DefaultTrunk_Type.__name__=_D
_Zxr10X25DefaultTrunk_Object=MibScalar
zxr10X25DefaultTrunk=_Zxr10X25DefaultTrunk_Object((1,3,6,1,4,1,3902,3,4001,1,13),_Zxr10X25DefaultTrunk_Type())
zxr10X25DefaultTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25DefaultTrunk.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_D:DisplayString,'UShort':UShort,'UChar':UChar,'UCHAR':UCHAR,'X25Address':X25Address,'zte':zte,'zxr10':zxr10,'zxr10X25MIBII':zxr10X25MIBII,'zxr10X25II':zxr10X25II,'zxr10X25PVCTable':zxr10X25PVCTable,'zxr10X25PVCEntry':zxr10X25PVCEntry,'zxr10X25PVCRowStatus':zxr10X25PVCRowStatus,_H:zxr10X25PVCNo,'zxr10X25PVCStartLcn':zxr10X25PVCStartLcn,'zxr10X25PVCNextLcn':zxr10X25PVCNextLcn,'zxr10X25PVCStartPortName':zxr10X25PVCStartPortName,'zxr10X25PVCNextPortName':zxr10X25PVCNextPortName,'zxr10X25PVCStartPortIfIndex':zxr10X25PVCStartPortIfIndex,'zxr10X25PVCNextPortIfIndex':zxr10X25PVCNextPortIfIndex,'zxr10X25OperTable':zxr10X25OperTable,'zxr10X25OperEntry':zxr10X25OperEntry,'zxr10X25OperStatus':zxr10X25OperStatus,_I:zxr10X25OperIfIndex,'zxr10X25OperLapbMode':zxr10X25OperLapbMode,'zxr10X25OperLapbPSSize':zxr10X25OperLapbPSSize,'zxr10X25OperLapbWinSize':zxr10X25OperLapbWinSize,'zxr10X25OperLapbRetranCount':zxr10X25OperLapbRetranCount,'zxr10X25OperLapbTimeoutT1':zxr10X25OperLapbTimeoutT1,'zxr10X25OperLapbTimeoutT2':zxr10X25OperLapbTimeoutT2,'zxr10X25OperLapbTimeoutT3':zxr10X25OperLapbTimeoutT3,'zxr10X25OperLapbPktMaxVC':zxr10X25OperLapbPktMaxVC,'zxr10X25OperLapbPktT20':zxr10X25OperLapbPktT20,'zxr10X25OperLapbPktT21':zxr10X25OperLapbPktT21,'zxr10X25OperLapbPktT22':zxr10X25OperLapbPktT22,'zxr10X25OperLapbPktT23':zxr10X25OperLapbPktT23,'zxr10X25OperLapbPktWinSize':zxr10X25OperLapbPktWinSize,'zxr10X25OperLapbPktPSize':zxr10X25OperLapbPktPSize,'zxr10X25OperLapbPktSvcIdleTime':zxr10X25OperLapbPktSvcIdleTime,'zxr10X25OperLapbDteDce':zxr10X25OperLapbDteDce,'zxr10X25OperLapbUserOrTrunk':zxr10X25OperLapbUserOrTrunk,'zxr10X25OperIfName':zxr10X25OperIfName,'zxr10X25OperLabpStatus':zxr10X25OperLabpStatus,'zxr10X25OperInterfaceType':zxr10X25OperInterfaceType,'zxr10X25SVCTable':zxr10X25SVCTable,'zxr10X25SVCEntry':zxr10X25SVCEntry,_J:zxr10X25SVCNo,'zxr10X25SVCStartLcn':zxr10X25SVCStartLcn,'zxr10X25SVCNextLcn':zxr10X25SVCNextLcn,'zxr10X25SVCStartPortName':zxr10X25SVCStartPortName,'zxr10X25SVCNextPortName':zxr10X25SVCNextPortName,'zxr10X25SVCStartPortIfIndex':zxr10X25SVCStartPortIfIndex,'zxr10X25SVCNextPortIfIndex':zxr10X25SVCNextPortIfIndex,'zxr10X25LapbFlowTable':zxr10X25LapbFlowTable,'zxr10X25LapbFlowEntry':zxr10X25LapbFlowEntry,'zxr10X25LapbFlowBusyDefers':zxr10X25LapbFlowBusyDefers,'zxr10X25LapbFlowRejOutPkts':zxr10X25LapbFlowRejOutPkts,'zxr10X25LapbFlowRejInPkts':zxr10X25LapbFlowRejInPkts,'zxr10X25LapbFlowT1Timeouts':zxr10X25LapbFlowT1Timeouts,'zxr10X25LapbFlowRROutPkts':zxr10X25LapbFlowRROutPkts,'zxr10X25LapbFlowRRInPkts':zxr10X25LapbFlowRRInPkts,'zxr10X25LapbFlowRNROutPkts':zxr10X25LapbFlowRNROutPkts,'zxr10X25LapbFlowRNRInPkts':zxr10X25LapbFlowRNRInPkts,'zxr10X25LapbFlowIOutPkts':zxr10X25LapbFlowIOutPkts,'zxr10X25LapbFlowIInPkts':zxr10X25LapbFlowIInPkts,'zxr10X25LapbFlowDMOutPkts':zxr10X25LapbFlowDMOutPkts,'zxr10X25LapbFlowDMInPkts':zxr10X25LapbFlowDMInPkts,'zxr10X25LapbFlowSABOutPkts':zxr10X25LapbFlowSABOutPkts,'zxr10X25LapbFlowSABInPkts':zxr10X25LapbFlowSABInPkts,'zxr10X25LapbFlowUAOutPkts':zxr10X25LapbFlowUAOutPkts,'zxr10X25LapbFlowUAInPkts':zxr10X25LapbFlowUAInPkts,'zxr10X25LapbFlowDISCOutPkts':zxr10X25LapbFlowDISCOutPkts,'zxr10X25LapbFlowDISCInPkts':zxr10X25LapbFlowDISCInPkts,'zxr10X25LapbFlowFRMROutPkts':zxr10X25LapbFlowFRMROutPkts,'zxr10X25LapbFlowFRMRInPkts':zxr10X25LapbFlowFRMRInPkts,'zxr10X25LapbFlowOutPkts':zxr10X25LapbFlowOutPkts,'zxr10X25LapbFlowInPkts':zxr10X25LapbFlowInPkts,'zxr10X25LapbFlowStateChanges':zxr10X25LapbFlowStateChanges,_K:zxr10X25LapbStatIfIndex,'zxr10X25StatTable':zxr10X25StatTable,'zxr10X25StatEntry':zxr10X25StatEntry,_L:zxr10X25StatLapbIndex,'zxr10StatRecvX25CALLREQUESTCnt':zxr10StatRecvX25CALLREQUESTCnt,'zxr10StatRecvX25CALLACCEPTEDCnt':zxr10StatRecvX25CALLACCEPTEDCnt,'zxr10StatRecvX25CLEARREQUESTCnt':zxr10StatRecvX25CLEARREQUESTCnt,'zxr10StatRecvX25CLEARCONFIRMATIONCnt':zxr10StatRecvX25CLEARCONFIRMATIONCnt,'zxr10StatRecvX25DATACnt':zxr10StatRecvX25DATACnt,'zxr10StatRecvX25INTERRUPTCnt':zxr10StatRecvX25INTERRUPTCnt,'zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt':zxr10StatRecvX25INTERRUPTCONFIRMATIONCnt,'zxr10StatRecvX25RRCnt':zxr10StatRecvX25RRCnt,'zxr10StatRecvX25RNRCnt':zxr10StatRecvX25RNRCnt,'zxr10StatRecvX25REJCnt':zxr10StatRecvX25REJCnt,'zxr10StatRecvX25RESETREQUESTCnt':zxr10StatRecvX25RESETREQUESTCnt,'zxr10StatRecvX25RESETCONFIRMATIONCnt':zxr10StatRecvX25RESETCONFIRMATIONCnt,'zxr10StatRecvX25REGISTRATIONREQUESTCnt':zxr10StatRecvX25REGISTRATIONREQUESTCnt,'zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt':zxr10StatRecvX25REGISTRATIONCONFIRMATIONCnt,'zxr10StatRecvX25RESTARTREQUESTCnt':zxr10StatRecvX25RESTARTREQUESTCnt,'zxr10StatRecvX25RESTARTCONFIRMATIONCnt':zxr10StatRecvX25RESTARTCONFIRMATIONCnt,'zxr10StatRecvX25DIAGNOSTICCnt':zxr10StatRecvX25DIAGNOSTICCnt,'zxr10StatRecvX25ILLEGALCnt':zxr10StatRecvX25ILLEGALCnt,'zxr10StatRecvX25TotalDataSize':zxr10StatRecvX25TotalDataSize,'zxr10StatSendX25CALLREQUESTCnt':zxr10StatSendX25CALLREQUESTCnt,'zxr10StatSendX25CALLACCEPTEDCnt':zxr10StatSendX25CALLACCEPTEDCnt,'zxr10StatSendX25CLEARREQUESTCnt':zxr10StatSendX25CLEARREQUESTCnt,'zxr10StatSendX25CLEARCONFIRMATIONCnt':zxr10StatSendX25CLEARCONFIRMATIONCnt,'zxr10StatSendX25DATACnt':zxr10StatSendX25DATACnt,'zxr10StatSendX25INTERRUPTCnt':zxr10StatSendX25INTERRUPTCnt,'zxr10StatSendX25INTERRUPTCONFIRMATIONCnt':zxr10StatSendX25INTERRUPTCONFIRMATIONCnt,'zxr10StatSendX25RRCnt':zxr10StatSendX25RRCnt,'zxr10StatSendX25RNRCnt':zxr10StatSendX25RNRCnt,'zxr10StatSendX25REJCnt':zxr10StatSendX25REJCnt,'zxr10StatSendX25RESETREQUESTCnt':zxr10StatSendX25RESETREQUESTCnt,'zxr10StatSendX25RESETCONFIRMATIONCnt':zxr10StatSendX25RESETCONFIRMATIONCnt,'zxr10StatSendX25REGISTRATIONREQUESTCnt':zxr10StatSendX25REGISTRATIONREQUESTCnt,'zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt':zxr10StatSendX25REGISTRATIONCONFIRMATIONCnt,'zxr10StatSendX25RESTARTREQUESTCnt':zxr10StatSendX25RESTARTREQUESTCnt,'zxr10StatSendX25RESTARTCONFIRMATIONCnt':zxr10StatSendX25RESTARTCONFIRMATIONCnt,'zxr10StatSendX25DIAGNOSTICCnt':zxr10StatSendX25DIAGNOSTICCnt,'zxr10StatSendX25ILLEGALCnt':zxr10StatSendX25ILLEGALCnt,'zxr10StatSendX25TotalDataSize':zxr10StatSendX25TotalDataSize,'zxr10X25UserAddrTable':zxr10X25UserAddrTable,'zxr10X25UserAddrEntry':zxr10X25UserAddrEntry,'zxr10X25UserX121Address':zxr10X25UserX121Address,_M:zxr10X25UserIfIndex,'zxr10X25UserIfName':zxr10X25UserIfName,'zxr10X25UserQoS':zxr10X25UserQoS,'zxr10X25UserRowStatus':zxr10X25UserRowStatus,'zxr10X25TrunkTable':zxr10X25TrunkTable,'zxr10X25TrunkEntry':zxr10X25TrunkEntry,_O:zxr10X25TrunkX121Address,'zxr10X25TrunkIfName':zxr10X25TrunkIfName,'zxr10X25TrunkQoS':zxr10X25TrunkQoS,'zxr10X25TrunkRowStatus':zxr10X25TrunkRowStatus,_N:zxr10X25TrunkIfIndex,'zxr10X25StationAddress':zxr10X25StationAddress,'zxr10X25DefaultTrunk':zxr10X25DefaultTrunk})