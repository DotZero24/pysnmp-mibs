_AG='hpSwitchAllowlistGroup'
_AF='hpSwitchDevProfileGroup2'
_AE='hpSwitchDevProfileGroup'
_AD='hpSwitchAllowlistRowStatus'
_AC='hpSwitchProfPoeAllocateBy'
_AB='hpSwitchDevPortDeviceName'
_AA='hpSwitchDevIdentAssociationDeviceType'
_A9='hpSwitchDevIdentAssociationStatus'
_A8='hpSwitchDevIdentAssociationProfID'
_A7='hpSwitchDevIdentAssociationProfName'
_A6='hpSwitchDevIdentAssociationRowStatus'
_A5='hpSwitchWhitelistRowStatus'
_A4='hpSwitchNeighborDevMacAddress'
_A3='hpSwitchRogueDevAction'
_A2='hpSwitchRogueDevStatus'
_A1='hpSwitchDevAssociationStatus'
_A0='hpSwitchDevAssociationProfID'
_z='hpSwitchDevAssociationProfName'
_y='hpSwitchAllowlistMacAddress'
_x='hpSwitchDevIdentAssociationSubType'
_w='hpSwitchDevIdentAssociationType'
_v='hpSwitchDevPortIndex'
_u='hpSwitchWhitelistMacAddress'
_t='hpSwitchRogueDevMacAddress'
_s='read-write'
_r='hpSwitchDevAssociationType'
_q='hpSwitchProfIndex'
_p='deviceIdentity'
_o='scsWanCpe'
_n='ciscoPhone'
_m='ciscoBridgeRouter'
_l='hpBridgeRouter'
_k='arubaBridgeRouter'
_j='arubaAccessPoint'
_i='TruthValue'
_h='hpSwitchDevProfileGroup3'
_g='hpSwitchDevProfileGroupNew'
_f='hpSwitchDevPortGroup'
_e='hpSwitchDevAssociationGroup'
_d='hpSwitchProfMode'
_c='hpSwitchDevPortProfName'
_b='hpSwitchDevPortType'
_a='hpSwitchProfTunneledNodeSupport'
_Z='hpSwitchProfJumboFrameSupport'
_Y='disable'
_X='enable'
_W='hpSwitchDevIdentAssociationGroup'
_V='hpSwitchDevPortGroupNew'
_U='hpSwitchProfPoePriority'
_T='hpSwitchProfPoeMaxPower'
_S='hpSwitchProfPortSpeed'
_R='hpSwitchProfCosPriority'
_Q='hpSwitchProfEgressBandwidth'
_P='hpSwitchProfIngressBandwidth'
_O='hpSwitchProfTaggedVlanList'
_N='hpSwitchProfUntaggedVlanID'
_M='hpSwitchProfRowStatus'
_L='hpSwitchProfName'
_K='read-only'
_J='OctetString'
_I='hpSwitchWhitelistGroup'
_H='hpSwitchRogueDevGroup'
_G='not-accessible'
_F='Unsigned32'
_E='Integer32'
_D='deprecated'
_C='read-create'
_B='current'
_A='HP-ICF-DEV-CONF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VidList,=mibBuilder.importSymbols('HP-ICF-TC','VidList')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_i)
hpicfDevConf=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126))
if mibBuilder.loadTexts:hpicfDevConf.setRevisions(('2021-06-15 00:00','2020-05-25 00:00','2018-01-15 00:00','2017-05-02 00:00','2016-11-02 00:00','2016-06-07 00:00','2016-02-01 00:00','2016-01-28 00:00','2015-12-18 00:00','2015-12-04 00:00','2015-09-08 00:00'))
class HpPartnerDeviceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),(_j,2),(_k,3),(_l,4),(_m,5),(_n,6),(_o,7),(_p,8)))
class HpPartnerDeviceTypeList(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('reserved',0),('none',1),(_j,2),(_k,3),(_l,4),(_m,5),(_n,6),(_o,7),(_p,8)))
_HpSwitchDevNotifications_ObjectIdentity=ObjectIdentity
hpSwitchDevNotifications=_HpSwitchDevNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,0))
_HpSwitchDevScalar_ObjectIdentity=ObjectIdentity
hpSwitchDevScalar=_HpSwitchDevScalar_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,1))
_HpSwitchDevGlobals_ObjectIdentity=ObjectIdentity
hpSwitchDevGlobals=_HpSwitchDevGlobals_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,2))
_HpSwitchDevConformance_ObjectIdentity=ObjectIdentity
hpSwitchDevConformance=_HpSwitchDevConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,3))
_HpSwitchDevCompliances_ObjectIdentity=ObjectIdentity
hpSwitchDevCompliances=_HpSwitchDevCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1))
_HpSwitchDevConfigGroups_ObjectIdentity=ObjectIdentity
hpSwitchDevConfigGroups=_HpSwitchDevConfigGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2))
_HpSwitchDevConfig_ObjectIdentity=ObjectIdentity
hpSwitchDevConfig=_HpSwitchDevConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,4))
_HpSwitchDevProfTable_Object=MibTable
hpSwitchDevProfTable=_HpSwitchDevProfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1))
if mibBuilder.loadTexts:hpSwitchDevProfTable.setStatus(_B)
_HpSwitchDevProfEntry_Object=MibTableRow
hpSwitchDevProfEntry=_HpSwitchDevProfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1))
hpSwitchDevProfEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:hpSwitchDevProfEntry.setStatus(_B)
class _HpSwitchProfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpSwitchProfIndex_Type.__name__=_F
_HpSwitchProfIndex_Object=MibTableColumn
hpSwitchProfIndex=_HpSwitchProfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,1),_HpSwitchProfIndex_Type())
hpSwitchProfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchProfIndex.setStatus(_B)
_HpSwitchProfRowStatus_Type=RowStatus
_HpSwitchProfRowStatus_Object=MibTableColumn
hpSwitchProfRowStatus=_HpSwitchProfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,2),_HpSwitchProfRowStatus_Type())
hpSwitchProfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfRowStatus.setStatus(_B)
class _HpSwitchProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpSwitchProfName_Type.__name__=_J
_HpSwitchProfName_Object=MibTableColumn
hpSwitchProfName=_HpSwitchProfName_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,3),_HpSwitchProfName_Type())
hpSwitchProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfName.setStatus(_B)
class _HpSwitchProfUntaggedVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpSwitchProfUntaggedVlanID_Type.__name__=_F
_HpSwitchProfUntaggedVlanID_Object=MibTableColumn
hpSwitchProfUntaggedVlanID=_HpSwitchProfUntaggedVlanID_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,4),_HpSwitchProfUntaggedVlanID_Type())
hpSwitchProfUntaggedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfUntaggedVlanID.setStatus(_B)
_HpSwitchProfTaggedVlanList_Type=VidList
_HpSwitchProfTaggedVlanList_Object=MibTableColumn
hpSwitchProfTaggedVlanList=_HpSwitchProfTaggedVlanList_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,5),_HpSwitchProfTaggedVlanList_Type())
hpSwitchProfTaggedVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfTaggedVlanList.setStatus(_B)
class _HpSwitchProfIngressBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchProfIngressBandwidth_Type.__name__=_F
_HpSwitchProfIngressBandwidth_Object=MibTableColumn
hpSwitchProfIngressBandwidth=_HpSwitchProfIngressBandwidth_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,6),_HpSwitchProfIngressBandwidth_Type())
hpSwitchProfIngressBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfIngressBandwidth.setStatus(_B)
class _HpSwitchProfEgressBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchProfEgressBandwidth_Type.__name__=_F
_HpSwitchProfEgressBandwidth_Object=MibTableColumn
hpSwitchProfEgressBandwidth=_HpSwitchProfEgressBandwidth_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,7),_HpSwitchProfEgressBandwidth_Type())
hpSwitchProfEgressBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfEgressBandwidth.setStatus(_B)
class _HpSwitchProfCosPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchProfCosPriority_Type.__name__=_F
_HpSwitchProfCosPriority_Object=MibTableColumn
hpSwitchProfCosPriority=_HpSwitchProfCosPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,8),_HpSwitchProfCosPriority_Type())
hpSwitchProfCosPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfCosPriority.setStatus(_B)
class _HpSwitchProfPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('halfDuplex10Mbits',1),('halfDuplex100Mbits',2),('fullDuplex10Mbits',3),('fullDuplex100Mbits',4),('autoNeg',5),('fullDuplex1000Mbits',6),('auto10Mbits',7),('auto100Mbits',8),('auto1000Mbits',9),('auto10Gbits',10),('auto10or100Mbits',11),('auto40Gbits',12),('auto2500Mbits',13),('auto5000Mbits',14),('auto2500or5000Mbits',15),('auto1000or2500Mbits',16),('auto1000or2500or5000Mbits',17)))
_HpSwitchProfPortSpeed_Type.__name__=_E
_HpSwitchProfPortSpeed_Object=MibTableColumn
hpSwitchProfPortSpeed=_HpSwitchProfPortSpeed_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,9),_HpSwitchProfPortSpeed_Type())
hpSwitchProfPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfPortSpeed.setStatus(_B)
_HpSwitchProfPoeMaxPower_Type=Unsigned32
_HpSwitchProfPoeMaxPower_Object=MibTableColumn
hpSwitchProfPoeMaxPower=_HpSwitchProfPoeMaxPower_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,10),_HpSwitchProfPoeMaxPower_Type())
hpSwitchProfPoeMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfPoeMaxPower.setStatus(_B)
class _HpSwitchProfPoePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_HpSwitchProfPoePriority_Type.__name__=_E
_HpSwitchProfPoePriority_Object=MibTableColumn
hpSwitchProfPoePriority=_HpSwitchProfPoePriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,11),_HpSwitchProfPoePriority_Type())
hpSwitchProfPoePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfPoePriority.setStatus(_B)
class _HpSwitchProfJumboFrameSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HpSwitchProfJumboFrameSupport_Type.__name__=_E
_HpSwitchProfJumboFrameSupport_Object=MibTableColumn
hpSwitchProfJumboFrameSupport=_HpSwitchProfJumboFrameSupport_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,12),_HpSwitchProfJumboFrameSupport_Type())
hpSwitchProfJumboFrameSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfJumboFrameSupport.setStatus(_B)
class _HpSwitchProfTunneledNodeSupport_Type(TruthValue):defaultValue=1
_HpSwitchProfTunneledNodeSupport_Type.__name__=_i
_HpSwitchProfTunneledNodeSupport_Object=MibTableColumn
hpSwitchProfTunneledNodeSupport=_HpSwitchProfTunneledNodeSupport_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,13),_HpSwitchProfTunneledNodeSupport_Type())
hpSwitchProfTunneledNodeSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfTunneledNodeSupport.setStatus(_B)
class _HpSwitchProfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clientMode',1),('portMode',2)))
_HpSwitchProfMode_Type.__name__=_E
_HpSwitchProfMode_Object=MibTableColumn
hpSwitchProfMode=_HpSwitchProfMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,14),_HpSwitchProfMode_Type())
hpSwitchProfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfMode.setStatus(_B)
class _HpSwitchProfPoeAllocateBy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('usage',1),('class',2)))
_HpSwitchProfPoeAllocateBy_Type.__name__=_E
_HpSwitchProfPoeAllocateBy_Object=MibTableColumn
hpSwitchProfPoeAllocateBy=_HpSwitchProfPoeAllocateBy_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,1,1,15),_HpSwitchProfPoeAllocateBy_Type())
hpSwitchProfPoeAllocateBy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProfPoeAllocateBy.setStatus(_B)
_HpSwitchDevAssociationTable_Object=MibTable
hpSwitchDevAssociationTable=_HpSwitchDevAssociationTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,2))
if mibBuilder.loadTexts:hpSwitchDevAssociationTable.setStatus(_D)
_HpSwitchDevAssociationEntry_Object=MibTableRow
hpSwitchDevAssociationEntry=_HpSwitchDevAssociationEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,2,1))
hpSwitchDevAssociationEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:hpSwitchDevAssociationEntry.setStatus(_D)
_HpSwitchDevAssociationType_Type=HpPartnerDeviceType
_HpSwitchDevAssociationType_Object=MibTableColumn
hpSwitchDevAssociationType=_HpSwitchDevAssociationType_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,2,1,1),_HpSwitchDevAssociationType_Type())
hpSwitchDevAssociationType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchDevAssociationType.setStatus(_D)
class _HpSwitchDevAssociationProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpSwitchDevAssociationProfName_Type.__name__=_J
_HpSwitchDevAssociationProfName_Object=MibTableColumn
hpSwitchDevAssociationProfName=_HpSwitchDevAssociationProfName_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,2,1,2),_HpSwitchDevAssociationProfName_Type())
hpSwitchDevAssociationProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevAssociationProfName.setStatus(_D)
class _HpSwitchDevAssociationProfID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpSwitchDevAssociationProfID_Type.__name__=_F
_HpSwitchDevAssociationProfID_Object=MibTableColumn
hpSwitchDevAssociationProfID=_HpSwitchDevAssociationProfID_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,2,1,3),_HpSwitchDevAssociationProfID_Type())
hpSwitchDevAssociationProfID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevAssociationProfID.setStatus(_D)
class _HpSwitchDevAssociationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HpSwitchDevAssociationStatus_Type.__name__=_E
_HpSwitchDevAssociationStatus_Object=MibTableColumn
hpSwitchDevAssociationStatus=_HpSwitchDevAssociationStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,2,1,4),_HpSwitchDevAssociationStatus_Type())
hpSwitchDevAssociationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevAssociationStatus.setStatus(_D)
_HpSwitchRogueDevice_ObjectIdentity=ObjectIdentity
hpSwitchRogueDevice=_HpSwitchRogueDevice_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3))
class _HpSwitchRogueDevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HpSwitchRogueDevStatus_Type.__name__=_E
_HpSwitchRogueDevStatus_Object=MibScalar
hpSwitchRogueDevStatus=_HpSwitchRogueDevStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3,1),_HpSwitchRogueDevStatus_Type())
hpSwitchRogueDevStatus.setMaxAccess(_s)
if mibBuilder.loadTexts:hpSwitchRogueDevStatus.setStatus(_B)
class _HpSwitchRogueDevAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('block',1),('log',2)))
_HpSwitchRogueDevAction_Type.__name__=_E
_HpSwitchRogueDevAction_Object=MibScalar
hpSwitchRogueDevAction=_HpSwitchRogueDevAction_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3,2),_HpSwitchRogueDevAction_Type())
hpSwitchRogueDevAction.setMaxAccess(_s)
if mibBuilder.loadTexts:hpSwitchRogueDevAction.setStatus(_B)
_HpSwitchRogueDevMacTable_Object=MibTable
hpSwitchRogueDevMacTable=_HpSwitchRogueDevMacTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3,3))
if mibBuilder.loadTexts:hpSwitchRogueDevMacTable.setStatus(_B)
_HpSwitchRogueDevMacEntry_Object=MibTableRow
hpSwitchRogueDevMacEntry=_HpSwitchRogueDevMacEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3,3,1))
hpSwitchRogueDevMacEntry.setIndexNames((0,_A,_t))
if mibBuilder.loadTexts:hpSwitchRogueDevMacEntry.setStatus(_B)
_HpSwitchRogueDevMacAddress_Type=MacAddress
_HpSwitchRogueDevMacAddress_Object=MibTableColumn
hpSwitchRogueDevMacAddress=_HpSwitchRogueDevMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3,3,1,1),_HpSwitchRogueDevMacAddress_Type())
hpSwitchRogueDevMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchRogueDevMacAddress.setStatus(_B)
_HpSwitchNeighborDevMacAddress_Type=MacAddress
_HpSwitchNeighborDevMacAddress_Object=MibTableColumn
hpSwitchNeighborDevMacAddress=_HpSwitchNeighborDevMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,3,3,1,2),_HpSwitchNeighborDevMacAddress_Type())
hpSwitchNeighborDevMacAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchNeighborDevMacAddress.setStatus(_B)
_HpSwitchWhitelistMacTable_Object=MibTable
hpSwitchWhitelistMacTable=_HpSwitchWhitelistMacTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,4))
if mibBuilder.loadTexts:hpSwitchWhitelistMacTable.setStatus(_B)
_HpSwitchWhitelistMacEntry_Object=MibTableRow
hpSwitchWhitelistMacEntry=_HpSwitchWhitelistMacEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,4,1))
hpSwitchWhitelistMacEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:hpSwitchWhitelistMacEntry.setStatus(_B)
_HpSwitchWhitelistMacAddress_Type=MacAddress
_HpSwitchWhitelistMacAddress_Object=MibTableColumn
hpSwitchWhitelistMacAddress=_HpSwitchWhitelistMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,4,1,1),_HpSwitchWhitelistMacAddress_Type())
hpSwitchWhitelistMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchWhitelistMacAddress.setStatus(_B)
_HpSwitchWhitelistRowStatus_Type=RowStatus
_HpSwitchWhitelistRowStatus_Object=MibTableColumn
hpSwitchWhitelistRowStatus=_HpSwitchWhitelistRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,4,1,2),_HpSwitchWhitelistRowStatus_Type())
hpSwitchWhitelistRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchWhitelistRowStatus.setStatus(_B)
_HpSwitchDevPortTable_Object=MibTable
hpSwitchDevPortTable=_HpSwitchDevPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,5))
if mibBuilder.loadTexts:hpSwitchDevPortTable.setStatus(_B)
_HpSwitchDevPortEntry_Object=MibTableRow
hpSwitchDevPortEntry=_HpSwitchDevPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,5,1))
hpSwitchDevPortEntry.setIndexNames((0,_A,_v))
if mibBuilder.loadTexts:hpSwitchDevPortEntry.setStatus(_B)
_HpSwitchDevPortIndex_Type=InterfaceIndex
_HpSwitchDevPortIndex_Object=MibTableColumn
hpSwitchDevPortIndex=_HpSwitchDevPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,5,1,1),_HpSwitchDevPortIndex_Type())
hpSwitchDevPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchDevPortIndex.setStatus(_B)
_HpSwitchDevPortType_Type=HpPartnerDeviceType
_HpSwitchDevPortType_Object=MibTableColumn
hpSwitchDevPortType=_HpSwitchDevPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,5,1,2),_HpSwitchDevPortType_Type())
hpSwitchDevPortType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchDevPortType.setStatus(_B)
class _HpSwitchDevPortProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpSwitchDevPortProfName_Type.__name__=_J
_HpSwitchDevPortProfName_Object=MibTableColumn
hpSwitchDevPortProfName=_HpSwitchDevPortProfName_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,5,1,3),_HpSwitchDevPortProfName_Type())
hpSwitchDevPortProfName.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchDevPortProfName.setStatus(_B)
class _HpSwitchDevPortDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpSwitchDevPortDeviceName_Type.__name__=_J
_HpSwitchDevPortDeviceName_Object=MibTableColumn
hpSwitchDevPortDeviceName=_HpSwitchDevPortDeviceName_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,5,1,4),_HpSwitchDevPortDeviceName_Type())
hpSwitchDevPortDeviceName.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchDevPortDeviceName.setStatus(_B)
_HpSwitchDevIdentAssociationTable_Object=MibTable
hpSwitchDevIdentAssociationTable=_HpSwitchDevIdentAssociationTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6))
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationTable.setStatus(_B)
_HpSwitchDevIdentAssociationEntry_Object=MibTableRow
hpSwitchDevIdentAssociationEntry=_HpSwitchDevIdentAssociationEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1))
hpSwitchDevIdentAssociationEntry.setIndexNames((0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationEntry.setStatus(_B)
_HpSwitchDevIdentAssociationType_Type=HpPartnerDeviceType
_HpSwitchDevIdentAssociationType_Object=MibTableColumn
hpSwitchDevIdentAssociationType=_HpSwitchDevIdentAssociationType_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,1),_HpSwitchDevIdentAssociationType_Type())
hpSwitchDevIdentAssociationType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationType.setStatus(_B)
class _HpSwitchDevIdentAssociationSubType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HpSwitchDevIdentAssociationSubType_Type.__name__=_F
_HpSwitchDevIdentAssociationSubType_Object=MibTableColumn
hpSwitchDevIdentAssociationSubType=_HpSwitchDevIdentAssociationSubType_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,2),_HpSwitchDevIdentAssociationSubType_Type())
hpSwitchDevIdentAssociationSubType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationSubType.setStatus(_B)
_HpSwitchDevIdentAssociationRowStatus_Type=RowStatus
_HpSwitchDevIdentAssociationRowStatus_Object=MibTableColumn
hpSwitchDevIdentAssociationRowStatus=_HpSwitchDevIdentAssociationRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,3),_HpSwitchDevIdentAssociationRowStatus_Type())
hpSwitchDevIdentAssociationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationRowStatus.setStatus(_B)
class _HpSwitchDevIdentAssociationProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpSwitchDevIdentAssociationProfName_Type.__name__=_J
_HpSwitchDevIdentAssociationProfName_Object=MibTableColumn
hpSwitchDevIdentAssociationProfName=_HpSwitchDevIdentAssociationProfName_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,4),_HpSwitchDevIdentAssociationProfName_Type())
hpSwitchDevIdentAssociationProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationProfName.setStatus(_B)
class _HpSwitchDevIdentAssociationProfID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpSwitchDevIdentAssociationProfID_Type.__name__=_F
_HpSwitchDevIdentAssociationProfID_Object=MibTableColumn
hpSwitchDevIdentAssociationProfID=_HpSwitchDevIdentAssociationProfID_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,5),_HpSwitchDevIdentAssociationProfID_Type())
hpSwitchDevIdentAssociationProfID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationProfID.setStatus(_B)
class _HpSwitchDevIdentAssociationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_HpSwitchDevIdentAssociationStatus_Type.__name__=_E
_HpSwitchDevIdentAssociationStatus_Object=MibTableColumn
hpSwitchDevIdentAssociationStatus=_HpSwitchDevIdentAssociationStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,6),_HpSwitchDevIdentAssociationStatus_Type())
hpSwitchDevIdentAssociationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationStatus.setStatus(_B)
class _HpSwitchDevIdentAssociationDeviceType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpSwitchDevIdentAssociationDeviceType_Type.__name__=_F
_HpSwitchDevIdentAssociationDeviceType_Object=MibTableColumn
hpSwitchDevIdentAssociationDeviceType=_HpSwitchDevIdentAssociationDeviceType_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,6,1,7),_HpSwitchDevIdentAssociationDeviceType_Type())
hpSwitchDevIdentAssociationDeviceType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationDeviceType.setStatus(_B)
_HpSwitchAllowlistMacTable_Object=MibTable
hpSwitchAllowlistMacTable=_HpSwitchAllowlistMacTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,7))
if mibBuilder.loadTexts:hpSwitchAllowlistMacTable.setStatus(_B)
_HpSwitchAllowlistMacEntry_Object=MibTableRow
hpSwitchAllowlistMacEntry=_HpSwitchAllowlistMacEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,7,1))
hpSwitchAllowlistMacEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:hpSwitchAllowlistMacEntry.setStatus(_B)
_HpSwitchAllowlistMacAddress_Type=MacAddress
_HpSwitchAllowlistMacAddress_Object=MibTableColumn
hpSwitchAllowlistMacAddress=_HpSwitchAllowlistMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,7,1,1),_HpSwitchAllowlistMacAddress_Type())
hpSwitchAllowlistMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSwitchAllowlistMacAddress.setStatus(_B)
_HpSwitchAllowlistRowStatus_Type=RowStatus
_HpSwitchAllowlistRowStatus_Object=MibTableColumn
hpSwitchAllowlistRowStatus=_HpSwitchAllowlistRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,126,4,7,1,2),_HpSwitchAllowlistRowStatus_Type())
hpSwitchAllowlistRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAllowlistRowStatus.setStatus(_B)
hpSwitchDevProfileGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,1))
hpSwitchDevProfileGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hpSwitchDevProfileGroup.setStatus(_D)
hpSwitchDevAssociationGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,2))
hpSwitchDevAssociationGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:hpSwitchDevAssociationGroup.setStatus(_D)
hpSwitchRogueDevGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,3))
hpSwitchRogueDevGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:hpSwitchRogueDevGroup.setStatus(_B)
hpSwitchWhitelistGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,4))
hpSwitchWhitelistGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:hpSwitchWhitelistGroup.setStatus(_B)
hpSwitchDevPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,5))
hpSwitchDevPortGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hpSwitchDevPortGroup.setStatus(_D)
hpSwitchDevProfileGroupNew=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,6))
hpSwitchDevProfileGroupNew.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpSwitchDevProfileGroupNew.setStatus(_D)
hpSwitchDevIdentAssociationGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,7))
hpSwitchDevIdentAssociationGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:hpSwitchDevIdentAssociationGroup.setStatus(_B)
hpSwitchDevPortGroupNew=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,8))
hpSwitchDevPortGroupNew.setObjects(*((_A,_b),(_A,_c),(_A,_AB)))
if mibBuilder.loadTexts:hpSwitchDevPortGroupNew.setStatus(_B)
hpSwitchDevProfileGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,9))
hpSwitchDevProfileGroup2.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z),(_A,_a),(_A,_d)))
if mibBuilder.loadTexts:hpSwitchDevProfileGroup2.setStatus(_D)
hpSwitchDevProfileGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,10))
hpSwitchDevProfileGroup3.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Z),(_A,_a),(_A,_d),(_A,_AC)))
if mibBuilder.loadTexts:hpSwitchDevProfileGroup3.setStatus(_B)
hpSwitchAllowlistGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,126,3,2,11))
hpSwitchAllowlistGroup.setObjects((_A,_AD))
if mibBuilder.loadTexts:hpSwitchAllowlistGroup.setStatus(_B)
hpSwitchDevCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1,1))
hpSwitchDevCompliance.setObjects(*((_A,_AE),(_A,_e),(_A,_H),(_A,_I),(_A,_f)))
if mibBuilder.loadTexts:hpSwitchDevCompliance.setStatus(_D)
hpSwitchDevCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1,2))
hpSwitchDevCompliance1.setObjects(*((_A,_e),(_A,_H),(_A,_I),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:hpSwitchDevCompliance1.setStatus(_D)
hpSwitchDevCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1,3))
hpSwitchDevCompliance2.setObjects(*((_A,_H),(_A,_I),(_A,_g),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:hpSwitchDevCompliance2.setStatus(_D)
hpSwitchDevCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1,4))
hpSwitchDevCompliance3.setObjects(*((_A,_H),(_A,_I),(_A,_AF),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:hpSwitchDevCompliance3.setStatus(_D)
hpSwitchDevCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1,5))
hpSwitchDevCompliance4.setObjects(*((_A,_H),(_A,_I),(_A,_h),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:hpSwitchDevCompliance4.setStatus(_D)
hpSwitchDevCompliance5=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,126,3,1,6))
hpSwitchDevCompliance5.setObjects(*((_A,_H),(_A,_I),(_A,_h),(_A,_V),(_A,_W),(_A,_AG)))
if mibBuilder.loadTexts:hpSwitchDevCompliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpPartnerDeviceType':HpPartnerDeviceType,'HpPartnerDeviceTypeList':HpPartnerDeviceTypeList,'hpicfDevConf':hpicfDevConf,'hpSwitchDevNotifications':hpSwitchDevNotifications,'hpSwitchDevScalar':hpSwitchDevScalar,'hpSwitchDevGlobals':hpSwitchDevGlobals,'hpSwitchDevConformance':hpSwitchDevConformance,'hpSwitchDevCompliances':hpSwitchDevCompliances,'hpSwitchDevCompliance':hpSwitchDevCompliance,'hpSwitchDevCompliance1':hpSwitchDevCompliance1,'hpSwitchDevCompliance2':hpSwitchDevCompliance2,'hpSwitchDevCompliance3':hpSwitchDevCompliance3,'hpSwitchDevCompliance4':hpSwitchDevCompliance4,'hpSwitchDevCompliance5':hpSwitchDevCompliance5,'hpSwitchDevConfigGroups':hpSwitchDevConfigGroups,_AE:hpSwitchDevProfileGroup,_e:hpSwitchDevAssociationGroup,_H:hpSwitchRogueDevGroup,_I:hpSwitchWhitelistGroup,_f:hpSwitchDevPortGroup,_g:hpSwitchDevProfileGroupNew,_W:hpSwitchDevIdentAssociationGroup,_V:hpSwitchDevPortGroupNew,_AF:hpSwitchDevProfileGroup2,_h:hpSwitchDevProfileGroup3,_AG:hpSwitchAllowlistGroup,'hpSwitchDevConfig':hpSwitchDevConfig,'hpSwitchDevProfTable':hpSwitchDevProfTable,'hpSwitchDevProfEntry':hpSwitchDevProfEntry,_q:hpSwitchProfIndex,_M:hpSwitchProfRowStatus,_L:hpSwitchProfName,_N:hpSwitchProfUntaggedVlanID,_O:hpSwitchProfTaggedVlanList,_P:hpSwitchProfIngressBandwidth,_Q:hpSwitchProfEgressBandwidth,_R:hpSwitchProfCosPriority,_S:hpSwitchProfPortSpeed,_T:hpSwitchProfPoeMaxPower,_U:hpSwitchProfPoePriority,_Z:hpSwitchProfJumboFrameSupport,_a:hpSwitchProfTunneledNodeSupport,_d:hpSwitchProfMode,_AC:hpSwitchProfPoeAllocateBy,'hpSwitchDevAssociationTable':hpSwitchDevAssociationTable,'hpSwitchDevAssociationEntry':hpSwitchDevAssociationEntry,_r:hpSwitchDevAssociationType,_z:hpSwitchDevAssociationProfName,_A0:hpSwitchDevAssociationProfID,_A1:hpSwitchDevAssociationStatus,'hpSwitchRogueDevice':hpSwitchRogueDevice,_A2:hpSwitchRogueDevStatus,_A3:hpSwitchRogueDevAction,'hpSwitchRogueDevMacTable':hpSwitchRogueDevMacTable,'hpSwitchRogueDevMacEntry':hpSwitchRogueDevMacEntry,_t:hpSwitchRogueDevMacAddress,_A4:hpSwitchNeighborDevMacAddress,'hpSwitchWhitelistMacTable':hpSwitchWhitelistMacTable,'hpSwitchWhitelistMacEntry':hpSwitchWhitelistMacEntry,_u:hpSwitchWhitelistMacAddress,_A5:hpSwitchWhitelistRowStatus,'hpSwitchDevPortTable':hpSwitchDevPortTable,'hpSwitchDevPortEntry':hpSwitchDevPortEntry,_v:hpSwitchDevPortIndex,_b:hpSwitchDevPortType,_c:hpSwitchDevPortProfName,_AB:hpSwitchDevPortDeviceName,'hpSwitchDevIdentAssociationTable':hpSwitchDevIdentAssociationTable,'hpSwitchDevIdentAssociationEntry':hpSwitchDevIdentAssociationEntry,_w:hpSwitchDevIdentAssociationType,_x:hpSwitchDevIdentAssociationSubType,_A6:hpSwitchDevIdentAssociationRowStatus,_A7:hpSwitchDevIdentAssociationProfName,_A8:hpSwitchDevIdentAssociationProfID,_A9:hpSwitchDevIdentAssociationStatus,_AA:hpSwitchDevIdentAssociationDeviceType,'hpSwitchAllowlistMacTable':hpSwitchAllowlistMacTable,'hpSwitchAllowlistMacEntry':hpSwitchAllowlistMacEntry,_y:hpSwitchAllowlistMacAddress,_AD:hpSwitchAllowlistRowStatus})