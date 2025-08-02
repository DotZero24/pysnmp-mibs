_A1='juniLagIfGroup'
_A0='juniVlanSubIfGroup'
_z='juniLagNextIfIndex'
_y='juniEthernetIfEgressLineUtilization'
_x='juniEthernetIfIngressLineUtilization'
_w='juniEthernetIfSecondaryLength'
_v='juniEthernetIfPrimaryLength'
_u='juniEthernetIfSecondaryMauType'
_t='juniEthernetIfPrimaryMauType'
_s='juniVlanSubIfVlanAdvisoryTxSpeed'
_r='juniVlanSubIfVlanAdvisoryRxSpeed'
_q='juniVlanSubIfVlanStackEthertype'
_p='juniVlanSubIfVlanStackId'
_o='juniVlanMajorIfRowStatus'
_n='juniVlanMajorIfLowerIfIndex'
_m='juniVlanMajorNextIfIndex'
_l='juniEthernetSubIfId'
_k='juniEthernetSubIfLowerIfIndex'
_j='juniEthernetSubIfRowStatus'
_i='juniEthernetSubIfNextIfIndex'
_h='percent'
_g='juniEthernetIfStatsIndex'
_f='juniVlanSubIfIndex'
_e='juniVlanMajorIfIndex'
_d='juniEthernetSubIfIndex'
_c='fullDuplex'
_b='halfDuplex'
_a='autoDuplex'
_Z='juniEthernetIfIndex'
_Y='juniEthernetIfStatsGroup'
_X='juniVlanSubIfRowStatus'
_W='juniVlanSubIfLowerIfIndex'
_V='juniVlanSubIfVlanUntagged'
_U='juniVlanSubIfVlanId'
_T='juniVlanSubNextIfIndex'
_S='juniEthernetIfOperDuplexMode'
_R='juniEthernetIfMtu'
_Q='juniEthernetIfSpeed'
_P='juniEthernetIfDuplexMode'
_O='JuniEthernetIfMauType'
_N='read-write'
_M='Unsigned32'
_L='juniEthernetGroup2'
_K='juniEthernetGroup'
_J='juniVlanSubIfGroup2'
_I='not-accessible'
_H='juniVlanGroup'
_G='juniEthernetSubIfGroup'
_F='obsolete'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='current'
_A='Juniper-ETHERNET-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
juniEthernetMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,34))
if mibBuilder.loadTexts:juniEthernetMIB.setRevisions(('2006-01-11 21:16','2005-09-14 20:08','2004-12-14 15:14','2004-05-26 19:40','2003-07-28 21:33','2003-02-20 21:51','2002-10-02 15:34','2002-10-01 17:44','2002-04-05 19:47','2001-01-02 16:55','2000-04-18 00:00','2000-02-03 00:00'))
class JuniEthernetIfMauType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('mauNotPresent',0),('mauNotSupported',1),('mau10BaseT',2),('mau100BaseTx',3),('mau1000BaseT',4),('mau1000BaseCx',5),('mau1000BaseSx',6),('mau1000BaseLx',7),('mau1000BaseZx',8),('mauSfpUnknown',9),('mauSfpNotPresent',10),('mau100BaseFxSm',11),('mau100BaseFxMm',12),('mauSfpNotJnprCompliant',13),('mau10000BaseSr',14),('mau10000BaseLr',15),('mau10000BaseEr',16),('mauXfpUnknown',17),('mauXfpNotPresent',18),('mauXfpNotJnprCompliant',19)))
_JuniEthernetObjects_ObjectIdentity=ObjectIdentity
juniEthernetObjects=_JuniEthernetObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1))
_JuniEthernetIfLayer_ObjectIdentity=ObjectIdentity
juniEthernetIfLayer=_JuniEthernetIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1,1))
_JuniEthernetIfTable_Object=MibTable
juniEthernetIfTable=_JuniEthernetIfTable_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1))
if mibBuilder.loadTexts:juniEthernetIfTable.setStatus(_B)
_JuniEthernetIfEntry_Object=MibTableRow
juniEthernetIfEntry=_JuniEthernetIfEntry_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1))
juniEthernetIfEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:juniEthernetIfEntry.setStatus(_B)
_JuniEthernetIfIndex_Type=InterfaceIndex
_JuniEthernetIfIndex_Object=MibTableColumn
juniEthernetIfIndex=_JuniEthernetIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,1),_JuniEthernetIfIndex_Type())
juniEthernetIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniEthernetIfIndex.setStatus(_B)
class _JuniEthernetIfDuplexMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_JuniEthernetIfDuplexMode_Type.__name__=_C
_JuniEthernetIfDuplexMode_Object=MibTableColumn
juniEthernetIfDuplexMode=_JuniEthernetIfDuplexMode_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,2),_JuniEthernetIfDuplexMode_Type())
juniEthernetIfDuplexMode.setMaxAccess(_N)
if mibBuilder.loadTexts:juniEthernetIfDuplexMode.setStatus(_B)
class _JuniEthernetIfSpeed_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('autoNegotiate',1),('speed10Mbps',2),('speed100Mbps',3),('speed1000Mbps',4),('speed10000Mbps',5)))
_JuniEthernetIfSpeed_Type.__name__=_C
_JuniEthernetIfSpeed_Object=MibTableColumn
juniEthernetIfSpeed=_JuniEthernetIfSpeed_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,3),_JuniEthernetIfSpeed_Type())
juniEthernetIfSpeed.setMaxAccess(_N)
if mibBuilder.loadTexts:juniEthernetIfSpeed.setStatus(_B)
class _JuniEthernetIfMtu_Type(Integer32):defaultValue=1518;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9188))
_JuniEthernetIfMtu_Type.__name__=_C
_JuniEthernetIfMtu_Object=MibTableColumn
juniEthernetIfMtu=_JuniEthernetIfMtu_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,4),_JuniEthernetIfMtu_Type())
juniEthernetIfMtu.setMaxAccess(_N)
if mibBuilder.loadTexts:juniEthernetIfMtu.setStatus(_B)
class _JuniEthernetIfOperDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_JuniEthernetIfOperDuplexMode_Type.__name__=_C
_JuniEthernetIfOperDuplexMode_Object=MibTableColumn
juniEthernetIfOperDuplexMode=_JuniEthernetIfOperDuplexMode_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,5),_JuniEthernetIfOperDuplexMode_Type())
juniEthernetIfOperDuplexMode.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfOperDuplexMode.setStatus(_B)
class _JuniEthernetIfPrimaryMauType_Type(JuniEthernetIfMauType):defaultValue=0
_JuniEthernetIfPrimaryMauType_Type.__name__=_O
_JuniEthernetIfPrimaryMauType_Object=MibTableColumn
juniEthernetIfPrimaryMauType=_JuniEthernetIfPrimaryMauType_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,6),_JuniEthernetIfPrimaryMauType_Type())
juniEthernetIfPrimaryMauType.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfPrimaryMauType.setStatus(_B)
class _JuniEthernetIfSecondaryMauType_Type(JuniEthernetIfMauType):defaultValue=1
_JuniEthernetIfSecondaryMauType_Type.__name__=_O
_JuniEthernetIfSecondaryMauType_Object=MibTableColumn
juniEthernetIfSecondaryMauType=_JuniEthernetIfSecondaryMauType_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,7),_JuniEthernetIfSecondaryMauType_Type())
juniEthernetIfSecondaryMauType.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfSecondaryMauType.setStatus(_B)
class _JuniEthernetIfPrimaryLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_JuniEthernetIfPrimaryLength_Type.__name__=_C
_JuniEthernetIfPrimaryLength_Object=MibTableColumn
juniEthernetIfPrimaryLength=_JuniEthernetIfPrimaryLength_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,8),_JuniEthernetIfPrimaryLength_Type())
juniEthernetIfPrimaryLength.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfPrimaryLength.setStatus(_B)
class _JuniEthernetIfSecondaryLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_JuniEthernetIfSecondaryLength_Type.__name__=_C
_JuniEthernetIfSecondaryLength_Object=MibTableColumn
juniEthernetIfSecondaryLength=_JuniEthernetIfSecondaryLength_Object((1,3,6,1,4,1,4874,2,2,34,1,1,1,1,9),_JuniEthernetIfSecondaryLength_Type())
juniEthernetIfSecondaryLength.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfSecondaryLength.setStatus(_B)
_JuniEthernetSubIfLayer_ObjectIdentity=ObjectIdentity
juniEthernetSubIfLayer=_JuniEthernetSubIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1,2))
_JuniEthernetSubIfNextIfIndex_Type=JuniNextIfIndex
_JuniEthernetSubIfNextIfIndex_Object=MibScalar
juniEthernetSubIfNextIfIndex=_JuniEthernetSubIfNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,2,1),_JuniEthernetSubIfNextIfIndex_Type())
juniEthernetSubIfNextIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetSubIfNextIfIndex.setStatus(_B)
_JuniEthernetSubIfTable_Object=MibTable
juniEthernetSubIfTable=_JuniEthernetSubIfTable_Object((1,3,6,1,4,1,4874,2,2,34,1,2,2))
if mibBuilder.loadTexts:juniEthernetSubIfTable.setStatus(_B)
_JuniEthernetSubIfEntry_Object=MibTableRow
juniEthernetSubIfEntry=_JuniEthernetSubIfEntry_Object((1,3,6,1,4,1,4874,2,2,34,1,2,2,1))
juniEthernetSubIfEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:juniEthernetSubIfEntry.setStatus(_B)
_JuniEthernetSubIfIndex_Type=InterfaceIndex
_JuniEthernetSubIfIndex_Object=MibTableColumn
juniEthernetSubIfIndex=_JuniEthernetSubIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,2,2,1,1),_JuniEthernetSubIfIndex_Type())
juniEthernetSubIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniEthernetSubIfIndex.setStatus(_B)
_JuniEthernetSubIfRowStatus_Type=RowStatus
_JuniEthernetSubIfRowStatus_Object=MibTableColumn
juniEthernetSubIfRowStatus=_JuniEthernetSubIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,34,1,2,2,1,2),_JuniEthernetSubIfRowStatus_Type())
juniEthernetSubIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniEthernetSubIfRowStatus.setStatus(_B)
_JuniEthernetSubIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniEthernetSubIfLowerIfIndex_Object=MibTableColumn
juniEthernetSubIfLowerIfIndex=_JuniEthernetSubIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,2,2,1,3),_JuniEthernetSubIfLowerIfIndex_Type())
juniEthernetSubIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniEthernetSubIfLowerIfIndex.setStatus(_B)
class _JuniEthernetSubIfId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_JuniEthernetSubIfId_Type.__name__=_C
_JuniEthernetSubIfId_Object=MibTableColumn
juniEthernetSubIfId=_JuniEthernetSubIfId_Object((1,3,6,1,4,1,4874,2,2,34,1,2,2,1,4),_JuniEthernetSubIfId_Type())
juniEthernetSubIfId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniEthernetSubIfId.setStatus(_B)
_JuniVlanMajorIfLayer_ObjectIdentity=ObjectIdentity
juniVlanMajorIfLayer=_JuniVlanMajorIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1,3))
_JuniVlanMajorNextIfIndex_Type=JuniNextIfIndex
_JuniVlanMajorNextIfIndex_Object=MibScalar
juniVlanMajorNextIfIndex=_JuniVlanMajorNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,3,1),_JuniVlanMajorNextIfIndex_Type())
juniVlanMajorNextIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniVlanMajorNextIfIndex.setStatus(_B)
_JuniVlanMajorIfTable_Object=MibTable
juniVlanMajorIfTable=_JuniVlanMajorIfTable_Object((1,3,6,1,4,1,4874,2,2,34,1,3,2))
if mibBuilder.loadTexts:juniVlanMajorIfTable.setStatus(_B)
_JuniVlanMajorIfEntry_Object=MibTableRow
juniVlanMajorIfEntry=_JuniVlanMajorIfEntry_Object((1,3,6,1,4,1,4874,2,2,34,1,3,2,1))
juniVlanMajorIfEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:juniVlanMajorIfEntry.setStatus(_B)
_JuniVlanMajorIfIndex_Type=InterfaceIndex
_JuniVlanMajorIfIndex_Object=MibTableColumn
juniVlanMajorIfIndex=_JuniVlanMajorIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,3,2,1,1),_JuniVlanMajorIfIndex_Type())
juniVlanMajorIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniVlanMajorIfIndex.setStatus(_B)
_JuniVlanMajorIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniVlanMajorIfLowerIfIndex_Object=MibTableColumn
juniVlanMajorIfLowerIfIndex=_JuniVlanMajorIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,3,2,1,2),_JuniVlanMajorIfLowerIfIndex_Type())
juniVlanMajorIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanMajorIfLowerIfIndex.setStatus(_B)
_JuniVlanMajorIfRowStatus_Type=RowStatus
_JuniVlanMajorIfRowStatus_Object=MibTableColumn
juniVlanMajorIfRowStatus=_JuniVlanMajorIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,34,1,3,2,1,3),_JuniVlanMajorIfRowStatus_Type())
juniVlanMajorIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanMajorIfRowStatus.setStatus(_B)
_JuniVlanSubIfLayer_ObjectIdentity=ObjectIdentity
juniVlanSubIfLayer=_JuniVlanSubIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1,4))
_JuniVlanSubNextIfIndex_Type=JuniNextIfIndex
_JuniVlanSubNextIfIndex_Object=MibScalar
juniVlanSubNextIfIndex=_JuniVlanSubNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,4,1),_JuniVlanSubNextIfIndex_Type())
juniVlanSubNextIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniVlanSubNextIfIndex.setStatus(_B)
_JuniVlanSubIfTable_Object=MibTable
juniVlanSubIfTable=_JuniVlanSubIfTable_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2))
if mibBuilder.loadTexts:juniVlanSubIfTable.setStatus(_B)
_JuniVlanSubIfEntry_Object=MibTableRow
juniVlanSubIfEntry=_JuniVlanSubIfEntry_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1))
juniVlanSubIfEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:juniVlanSubIfEntry.setStatus(_B)
_JuniVlanSubIfIndex_Type=InterfaceIndex
_JuniVlanSubIfIndex_Object=MibTableColumn
juniVlanSubIfIndex=_JuniVlanSubIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,1),_JuniVlanSubIfIndex_Type())
juniVlanSubIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniVlanSubIfIndex.setStatus(_B)
class _JuniVlanSubIfVlanId_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(5000,5000),ValueRangeConstraint(5001,5001))
_JuniVlanSubIfVlanId_Type.__name__=_C
_JuniVlanSubIfVlanId_Object=MibTableColumn
juniVlanSubIfVlanId=_JuniVlanSubIfVlanId_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,2),_JuniVlanSubIfVlanId_Type())
juniVlanSubIfVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfVlanId.setStatus(_B)
_JuniVlanSubIfVlanUntagged_Type=TruthValue
_JuniVlanSubIfVlanUntagged_Object=MibTableColumn
juniVlanSubIfVlanUntagged=_JuniVlanSubIfVlanUntagged_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,3),_JuniVlanSubIfVlanUntagged_Type())
juniVlanSubIfVlanUntagged.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfVlanUntagged.setStatus(_B)
_JuniVlanSubIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniVlanSubIfLowerIfIndex_Object=MibTableColumn
juniVlanSubIfLowerIfIndex=_JuniVlanSubIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,4),_JuniVlanSubIfLowerIfIndex_Type())
juniVlanSubIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfLowerIfIndex.setStatus(_B)
_JuniVlanSubIfRowStatus_Type=RowStatus
_JuniVlanSubIfRowStatus_Object=MibTableColumn
juniVlanSubIfRowStatus=_JuniVlanSubIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,5),_JuniVlanSubIfRowStatus_Type())
juniVlanSubIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfRowStatus.setStatus(_B)
class _JuniVlanSubIfVlanStackId_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(5000,5000))
_JuniVlanSubIfVlanStackId_Type.__name__=_C
_JuniVlanSubIfVlanStackId_Object=MibTableColumn
juniVlanSubIfVlanStackId=_JuniVlanSubIfVlanStackId_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,6),_JuniVlanSubIfVlanStackId_Type())
juniVlanSubIfVlanStackId.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfVlanStackId.setStatus(_B)
class _JuniVlanSubIfVlanStackEthertype_Type(Integer32):defaultValue=37120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(33024,34984,37120)));namedValues=NamedValues(*(('etherType8100h',33024),('etherType88a8h',34984),('etherType9100h',37120)))
_JuniVlanSubIfVlanStackEthertype_Type.__name__=_C
_JuniVlanSubIfVlanStackEthertype_Object=MibTableColumn
juniVlanSubIfVlanStackEthertype=_JuniVlanSubIfVlanStackEthertype_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,7),_JuniVlanSubIfVlanStackEthertype_Type())
juniVlanSubIfVlanStackEthertype.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfVlanStackEthertype.setStatus(_B)
class _JuniVlanSubIfVlanAdvisoryRxSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniVlanSubIfVlanAdvisoryRxSpeed_Type.__name__=_C
_JuniVlanSubIfVlanAdvisoryRxSpeed_Object=MibTableColumn
juniVlanSubIfVlanAdvisoryRxSpeed=_JuniVlanSubIfVlanAdvisoryRxSpeed_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,8),_JuniVlanSubIfVlanAdvisoryRxSpeed_Type())
juniVlanSubIfVlanAdvisoryRxSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfVlanAdvisoryRxSpeed.setStatus(_B)
class _JuniVlanSubIfVlanAdvisoryTxSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniVlanSubIfVlanAdvisoryTxSpeed_Type.__name__=_C
_JuniVlanSubIfVlanAdvisoryTxSpeed_Object=MibTableColumn
juniVlanSubIfVlanAdvisoryTxSpeed=_JuniVlanSubIfVlanAdvisoryTxSpeed_Object((1,3,6,1,4,1,4874,2,2,34,1,4,2,1,9),_JuniVlanSubIfVlanAdvisoryTxSpeed_Type())
juniVlanSubIfVlanAdvisoryTxSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:juniVlanSubIfVlanAdvisoryTxSpeed.setStatus(_B)
_JuniEthernetIfStats_ObjectIdentity=ObjectIdentity
juniEthernetIfStats=_JuniEthernetIfStats_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1,5))
_JuniEthernetIfStatsTable_Object=MibTable
juniEthernetIfStatsTable=_JuniEthernetIfStatsTable_Object((1,3,6,1,4,1,4874,2,2,34,1,5,1))
if mibBuilder.loadTexts:juniEthernetIfStatsTable.setStatus(_B)
_JuniEthernetIfStatsEntry_Object=MibTableRow
juniEthernetIfStatsEntry=_JuniEthernetIfStatsEntry_Object((1,3,6,1,4,1,4874,2,2,34,1,5,1,1))
juniEthernetIfStatsEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:juniEthernetIfStatsEntry.setStatus(_B)
_JuniEthernetIfStatsIndex_Type=InterfaceIndex
_JuniEthernetIfStatsIndex_Object=MibTableColumn
juniEthernetIfStatsIndex=_JuniEthernetIfStatsIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,5,1,1,1),_JuniEthernetIfStatsIndex_Type())
juniEthernetIfStatsIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniEthernetIfStatsIndex.setStatus(_B)
class _JuniEthernetIfIngressLineUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_JuniEthernetIfIngressLineUtilization_Type.__name__=_M
_JuniEthernetIfIngressLineUtilization_Object=MibTableColumn
juniEthernetIfIngressLineUtilization=_JuniEthernetIfIngressLineUtilization_Object((1,3,6,1,4,1,4874,2,2,34,1,5,1,1,2),_JuniEthernetIfIngressLineUtilization_Type())
juniEthernetIfIngressLineUtilization.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfIngressLineUtilization.setStatus(_B)
if mibBuilder.loadTexts:juniEthernetIfIngressLineUtilization.setUnits(_h)
class _JuniEthernetIfEgressLineUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_JuniEthernetIfEgressLineUtilization_Type.__name__=_M
_JuniEthernetIfEgressLineUtilization_Object=MibTableColumn
juniEthernetIfEgressLineUtilization=_JuniEthernetIfEgressLineUtilization_Object((1,3,6,1,4,1,4874,2,2,34,1,5,1,1,3),_JuniEthernetIfEgressLineUtilization_Type())
juniEthernetIfEgressLineUtilization.setMaxAccess(_E)
if mibBuilder.loadTexts:juniEthernetIfEgressLineUtilization.setStatus(_B)
if mibBuilder.loadTexts:juniEthernetIfEgressLineUtilization.setUnits(_h)
_JuniLagIfLayer_ObjectIdentity=ObjectIdentity
juniLagIfLayer=_JuniLagIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,1,6))
_JuniLagNextIfIndex_Type=JuniNextIfIndex
_JuniLagNextIfIndex_Object=MibScalar
juniLagNextIfIndex=_JuniLagNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,34,1,6,1),_JuniLagNextIfIndex_Type())
juniLagNextIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniLagNextIfIndex.setStatus(_B)
_JuniEthernetConformance_ObjectIdentity=ObjectIdentity
juniEthernetConformance=_JuniEthernetConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,4))
_JuniEthernetCompliances_ObjectIdentity=ObjectIdentity
juniEthernetCompliances=_JuniEthernetCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,4,1))
_JuniEthernetGroups_ObjectIdentity=ObjectIdentity
juniEthernetGroups=_JuniEthernetGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,34,4,2))
juniEthernetGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,1))
juniEthernetGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniEthernetGroup.setStatus(_F)
juniEthernetSubIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,2))
juniEthernetSubIfGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:juniEthernetSubIfGroup.setStatus(_B)
juniVlanGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,3))
juniVlanGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:juniVlanGroup.setStatus(_B)
juniVlanSubIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,4))
juniVlanSubIfGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:juniVlanSubIfGroup.setStatus(_F)
juniVlanSubIfGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,5))
juniVlanSubIfGroup2.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_p),(_A,_W),(_A,_X),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:juniVlanSubIfGroup2.setStatus(_B)
juniEthernetGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,6))
juniEthernetGroup2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:juniEthernetGroup2.setStatus(_B)
juniEthernetIfStatsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,7))
juniEthernetIfStatsGroup.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:juniEthernetIfStatsGroup.setStatus(_B)
juniLagIfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,34,4,2,8))
juniLagIfGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:juniLagIfGroup.setStatus(_B)
juniEthernetCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,34,4,1,1))
juniEthernetCompliance.setObjects(*((_A,_K),(_A,_G)))
if mibBuilder.loadTexts:juniEthernetCompliance.setStatus(_F)
juniEthernetCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,34,4,1,2))
juniEthernetCompliance2.setObjects(*((_A,_K),(_A,_G),(_A,_H),(_A,_A0)))
if mibBuilder.loadTexts:juniEthernetCompliance2.setStatus(_F)
juniEthernetCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,34,4,1,3))
juniEthernetCompliance3.setObjects(*((_A,_K),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:juniEthernetCompliance3.setStatus(_F)
juniEthernetCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,34,4,1,4))
juniEthernetCompliance4.setObjects(*((_A,_L),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:juniEthernetCompliance4.setStatus(_F)
juniEthernetCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,34,4,1,5))
juniEthernetCompliance5.setObjects(*((_A,_L),(_A,_G),(_A,_Y),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:juniEthernetCompliance5.setStatus(_F)
juniEthernetCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,34,4,1,6))
juniEthernetCompliance6.setObjects(*((_A,_L),(_A,_G),(_A,_Y),(_A,_H),(_A,_J),(_A,_A1)))
if mibBuilder.loadTexts:juniEthernetCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_O:JuniEthernetIfMauType,'juniEthernetMIB':juniEthernetMIB,'juniEthernetObjects':juniEthernetObjects,'juniEthernetIfLayer':juniEthernetIfLayer,'juniEthernetIfTable':juniEthernetIfTable,'juniEthernetIfEntry':juniEthernetIfEntry,_Z:juniEthernetIfIndex,_P:juniEthernetIfDuplexMode,_Q:juniEthernetIfSpeed,_R:juniEthernetIfMtu,_S:juniEthernetIfOperDuplexMode,_t:juniEthernetIfPrimaryMauType,_u:juniEthernetIfSecondaryMauType,_v:juniEthernetIfPrimaryLength,_w:juniEthernetIfSecondaryLength,'juniEthernetSubIfLayer':juniEthernetSubIfLayer,_i:juniEthernetSubIfNextIfIndex,'juniEthernetSubIfTable':juniEthernetSubIfTable,'juniEthernetSubIfEntry':juniEthernetSubIfEntry,_d:juniEthernetSubIfIndex,_j:juniEthernetSubIfRowStatus,_k:juniEthernetSubIfLowerIfIndex,_l:juniEthernetSubIfId,'juniVlanMajorIfLayer':juniVlanMajorIfLayer,_m:juniVlanMajorNextIfIndex,'juniVlanMajorIfTable':juniVlanMajorIfTable,'juniVlanMajorIfEntry':juniVlanMajorIfEntry,_e:juniVlanMajorIfIndex,_n:juniVlanMajorIfLowerIfIndex,_o:juniVlanMajorIfRowStatus,'juniVlanSubIfLayer':juniVlanSubIfLayer,_T:juniVlanSubNextIfIndex,'juniVlanSubIfTable':juniVlanSubIfTable,'juniVlanSubIfEntry':juniVlanSubIfEntry,_f:juniVlanSubIfIndex,_U:juniVlanSubIfVlanId,_V:juniVlanSubIfVlanUntagged,_W:juniVlanSubIfLowerIfIndex,_X:juniVlanSubIfRowStatus,_p:juniVlanSubIfVlanStackId,_q:juniVlanSubIfVlanStackEthertype,_r:juniVlanSubIfVlanAdvisoryRxSpeed,_s:juniVlanSubIfVlanAdvisoryTxSpeed,'juniEthernetIfStats':juniEthernetIfStats,'juniEthernetIfStatsTable':juniEthernetIfStatsTable,'juniEthernetIfStatsEntry':juniEthernetIfStatsEntry,_g:juniEthernetIfStatsIndex,_x:juniEthernetIfIngressLineUtilization,_y:juniEthernetIfEgressLineUtilization,'juniLagIfLayer':juniLagIfLayer,_z:juniLagNextIfIndex,'juniEthernetConformance':juniEthernetConformance,'juniEthernetCompliances':juniEthernetCompliances,'juniEthernetCompliance':juniEthernetCompliance,'juniEthernetCompliance2':juniEthernetCompliance2,'juniEthernetCompliance3':juniEthernetCompliance3,'juniEthernetCompliance4':juniEthernetCompliance4,'juniEthernetCompliance5':juniEthernetCompliance5,'juniEthernetCompliance6':juniEthernetCompliance6,'juniEthernetGroups':juniEthernetGroups,_K:juniEthernetGroup,_G:juniEthernetSubIfGroup,_H:juniVlanGroup,_A0:juniVlanSubIfGroup,_J:juniVlanSubIfGroup2,_L:juniEthernetGroup2,_Y:juniEthernetIfStatsGroup,_A1:juniLagIfGroup})