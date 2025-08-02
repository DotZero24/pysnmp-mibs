_m='wwpLeosEtherPortLinkFlapHoldTime'
_l='enabled'
_k='disabled'
_j='not-applicable'
_i='PortEgressFrameCosPolicy'
_h='PortIngressFixedColor'
_g='asymRx'
_f='deprecated'
_e='tenGig'
_d='hundredMb'
_c='dot3adAggPortListPorts'
_b='dot3adAggPortActorAdminKey'
_a='wwpLeosEtherPortStateMirrorGroupId'
_Z='kbps'
_Y='sym'
_X='asymTx'
_W='off'
_V='full'
_U='half'
_T='ethernet'
_S='IEEE8023-LAG-MIB'
_R='wwpLeosEtherPortAdminStatus'
_Q='read-create'
_P='DisplayString'
_O='wwpLeosEtherPortOperStatus'
_N='wwpLeosEtherPortType'
_M='sysName'
_L='sysLocation'
_K='wwpLeosEtherPortDesc'
_J='wwpLeosEtherPortName'
_I='unknown'
_H='SNMPv2-MIB'
_G='wwpLeosEtherPortId'
_F='TruthValue'
_E='read-only'
_D='WWP-LEOS-PORT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3adAggPortActorAdminKey,dot3adAggPortListPorts=mibBuilder.importSymbols(_S,_b,_c)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,sysName=mibBuilder.importSymbols(_H,_L,_M)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosPortMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,2))
if mibBuilder.loadTexts:wwpLeosPortMIB.setRevisions(('2012-05-25 00:00','2011-02-02 00:00','2010-11-01 00:00','2010-07-28 00:00','2010-05-05 17:00','2008-11-14 00:00','2008-07-21 00:00','2007-08-11 00:00','2007-06-20 00:00','2006-05-26 00:00','2006-05-18 00:00','2006-03-15 00:00','2005-07-28 00:00','2004-04-18 17:00'))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class PortEgressFrameCosPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingore',1),('rcosToL2OuterPcpMap',2)))
class PortIngressFixedColor(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('green',1),('yellow',2)))
_WwpLeosPortMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosPortMIBObjects=_WwpLeosPortMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,1))
_WwpLeosEtherPort_ObjectIdentity=ObjectIdentity
wwpLeosEtherPort=_WwpLeosEtherPort_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,1,1))
_WwpLeosEtherPortTable_Object=MibTable
wwpLeosEtherPortTable=_WwpLeosEtherPortTable_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1))
if mibBuilder.loadTexts:wwpLeosEtherPortTable.setStatus(_A)
_WwpLeosEtherPortEntry_Object=MibTableRow
wwpLeosEtherPortEntry=_WwpLeosEtherPortEntry_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1))
wwpLeosEtherPortEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpLeosEtherPortEntry.setStatus(_A)
class _WwpLeosEtherPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosEtherPortId_Type.__name__=_C
_WwpLeosEtherPortId_Object=MibTableColumn
wwpLeosEtherPortId=_WwpLeosEtherPortId_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,1),_WwpLeosEtherPortId_Type())
wwpLeosEtherPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortId.setStatus(_A)
class _WwpLeosEtherPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_WwpLeosEtherPortName_Type.__name__=_P
_WwpLeosEtherPortName_Object=MibTableColumn
wwpLeosEtherPortName=_WwpLeosEtherPortName_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,2),_WwpLeosEtherPortName_Type())
wwpLeosEtherPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortName.setStatus(_A)
class _WwpLeosEtherPortDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosEtherPortDesc_Type.__name__=_P
_WwpLeosEtherPortDesc_Object=MibTableColumn
wwpLeosEtherPortDesc=_WwpLeosEtherPortDesc_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,3),_WwpLeosEtherPortDesc_Type())
wwpLeosEtherPortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortDesc.setStatus(_A)
class _WwpLeosEtherPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_T,1),('fastEthernet',2),('hundredFx',3),('gigEthernet',4),('lagPort',5),(_I,6),('gigHundredFx',7),('tripleSpeed',8),('tenGigEthernet',9),('gigTenGigEthernet',10)))
_WwpLeosEtherPortType_Type.__name__=_C
_WwpLeosEtherPortType_Object=MibTableColumn
wwpLeosEtherPortType=_WwpLeosEtherPortType_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,4),_WwpLeosEtherPortType_Type())
wwpLeosEtherPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortType.setStatus(_A)
_WwpLeosEtherPortPhysAddr_Type=MacAddress
_WwpLeosEtherPortPhysAddr_Object=MibTableColumn
wwpLeosEtherPortPhysAddr=_WwpLeosEtherPortPhysAddr_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,5),_WwpLeosEtherPortPhysAddr_Type())
wwpLeosEtherPortPhysAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortPhysAddr.setStatus(_A)
_WwpLeosEtherPortAutoNeg_Type=TruthValue
_WwpLeosEtherPortAutoNeg_Object=MibTableColumn
wwpLeosEtherPortAutoNeg=_WwpLeosEtherPortAutoNeg_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,6),_WwpLeosEtherPortAutoNeg_Type())
wwpLeosEtherPortAutoNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAutoNeg.setStatus(_A)
class _WwpLeosEtherPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_WwpLeosEtherPortAdminStatus_Type.__name__=_C
_WwpLeosEtherPortAdminStatus_Object=MibTableColumn
wwpLeosEtherPortAdminStatus=_WwpLeosEtherPortAdminStatus_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,7),_WwpLeosEtherPortAdminStatus_Type())
wwpLeosEtherPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdminStatus.setStatus(_A)
class _WwpLeosEtherPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('down',2),('notauth',3),('lbtx',4),('lbrx',5),('linkflap',6)))
_WwpLeosEtherPortOperStatus_Type.__name__=_C
_WwpLeosEtherPortOperStatus_Object=MibTableColumn
wwpLeosEtherPortOperStatus=_WwpLeosEtherPortOperStatus_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,8),_WwpLeosEtherPortOperStatus_Type())
wwpLeosEtherPortOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortOperStatus.setStatus(_A)
class _WwpLeosEtherPortAdminSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tenMb',1),(_d,2),('gig',3),('auto',4),(_e,5)))
_WwpLeosEtherPortAdminSpeed_Type.__name__=_C
_WwpLeosEtherPortAdminSpeed_Object=MibTableColumn
wwpLeosEtherPortAdminSpeed=_WwpLeosEtherPortAdminSpeed_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,9),_WwpLeosEtherPortAdminSpeed_Type())
wwpLeosEtherPortAdminSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdminSpeed.setStatus(_A)
class _WwpLeosEtherPortOperSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('tenMb',1),(_d,2),('gig',3),(_e,4)))
_WwpLeosEtherPortOperSpeed_Type.__name__=_C
_WwpLeosEtherPortOperSpeed_Object=MibTableColumn
wwpLeosEtherPortOperSpeed=_WwpLeosEtherPortOperSpeed_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,10),_WwpLeosEtherPortOperSpeed_Type())
wwpLeosEtherPortOperSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortOperSpeed.setStatus(_f)
class _WwpLeosEtherPortAdminDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_WwpLeosEtherPortAdminDuplex_Type.__name__=_C
_WwpLeosEtherPortAdminDuplex_Object=MibTableColumn
wwpLeosEtherPortAdminDuplex=_WwpLeosEtherPortAdminDuplex_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,11),_WwpLeosEtherPortAdminDuplex_Type())
wwpLeosEtherPortAdminDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdminDuplex.setStatus(_A)
class _WwpLeosEtherPortOperDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_WwpLeosEtherPortOperDuplex_Type.__name__=_C
_WwpLeosEtherPortOperDuplex_Object=MibTableColumn
wwpLeosEtherPortOperDuplex=_WwpLeosEtherPortOperDuplex_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,12),_WwpLeosEtherPortOperDuplex_Type())
wwpLeosEtherPortOperDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortOperDuplex.setStatus(_A)
class _WwpLeosEtherPortAdminFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_W,2),(_X,3),(_g,4),(_Y,5)))
_WwpLeosEtherPortAdminFlowCtrl_Type.__name__=_C
_WwpLeosEtherPortAdminFlowCtrl_Object=MibTableColumn
wwpLeosEtherPortAdminFlowCtrl=_WwpLeosEtherPortAdminFlowCtrl_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,13),_WwpLeosEtherPortAdminFlowCtrl_Type())
wwpLeosEtherPortAdminFlowCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdminFlowCtrl.setStatus(_A)
class _WwpLeosEtherPortOperFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_W,2),(_X,3),(_g,4),(_Y,5)))
_WwpLeosEtherPortOperFlowCtrl_Type.__name__=_C
_WwpLeosEtherPortOperFlowCtrl_Object=MibTableColumn
wwpLeosEtherPortOperFlowCtrl=_WwpLeosEtherPortOperFlowCtrl_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,14),_WwpLeosEtherPortOperFlowCtrl_Type())
wwpLeosEtherPortOperFlowCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortOperFlowCtrl.setStatus(_A)
class _WwpLeosEtherIngressPvid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosEtherIngressPvid_Type.__name__=_C
_WwpLeosEtherIngressPvid_Object=MibTableColumn
wwpLeosEtherIngressPvid=_WwpLeosEtherIngressPvid_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,15),_WwpLeosEtherIngressPvid_Type())
wwpLeosEtherIngressPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherIngressPvid.setStatus(_A)
class _WwpLeosEtherUntagEgressVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosEtherUntagEgressVlanId_Type.__name__=_C
_WwpLeosEtherUntagEgressVlanId_Object=MibTableColumn
wwpLeosEtherUntagEgressVlanId=_WwpLeosEtherUntagEgressVlanId_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,16),_WwpLeosEtherUntagEgressVlanId_Type())
wwpLeosEtherUntagEgressVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherUntagEgressVlanId.setStatus(_A)
class _WwpLeosEtherPortAcceptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('admitAll',1),('admitOnlyVlanTagged',2),('admitOnlyUntagged',3)))
_WwpLeosEtherPortAcceptableFrameTypes_Type.__name__=_C
_WwpLeosEtherPortAcceptableFrameTypes_Object=MibTableColumn
wwpLeosEtherPortAcceptableFrameTypes=_WwpLeosEtherPortAcceptableFrameTypes_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,17),_WwpLeosEtherPortAcceptableFrameTypes_Type())
wwpLeosEtherPortAcceptableFrameTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAcceptableFrameTypes.setStatus(_A)
class _WwpLeosEtherPortUntaggedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('p0',0),('p1',1),('p2',2),('p3',3),('p4',4),('p5',5),('p6',6),('p7',7)))
_WwpLeosEtherPortUntaggedPriority_Type.__name__=_C
_WwpLeosEtherPortUntaggedPriority_Object=MibTableColumn
wwpLeosEtherPortUntaggedPriority=_WwpLeosEtherPortUntaggedPriority_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,18),_WwpLeosEtherPortUntaggedPriority_Type())
wwpLeosEtherPortUntaggedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortUntaggedPriority.setStatus(_f)
class _WwpLeosEtherPortMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1522,9216))
_WwpLeosEtherPortMaxFrameSize_Type.__name__=_C
_WwpLeosEtherPortMaxFrameSize_Object=MibTableColumn
wwpLeosEtherPortMaxFrameSize=_WwpLeosEtherPortMaxFrameSize_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,19),_WwpLeosEtherPortMaxFrameSize_Type())
wwpLeosEtherPortMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMaxFrameSize.setStatus(_A)
class _WwpLeosEtherPortVlanIngressFiltering_Type(TruthValue):defaultValue=1
_WwpLeosEtherPortVlanIngressFiltering_Type.__name__=_F
_WwpLeosEtherPortVlanIngressFiltering_Object=MibTableColumn
wwpLeosEtherPortVlanIngressFiltering=_WwpLeosEtherPortVlanIngressFiltering_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,20),_WwpLeosEtherPortVlanIngressFiltering_Type())
wwpLeosEtherPortVlanIngressFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortVlanIngressFiltering.setStatus(_A)
class _WwpLeosEtherPortAdminAdvertisedFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_W,2),(_X,3),(_Y,4),('symAsymRx',5)))
_WwpLeosEtherPortAdminAdvertisedFlowCtrl_Type.__name__=_C
_WwpLeosEtherPortAdminAdvertisedFlowCtrl_Object=MibTableColumn
wwpLeosEtherPortAdminAdvertisedFlowCtrl=_WwpLeosEtherPortAdminAdvertisedFlowCtrl_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,21),_WwpLeosEtherPortAdminAdvertisedFlowCtrl_Type())
wwpLeosEtherPortAdminAdvertisedFlowCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdminAdvertisedFlowCtrl.setStatus(_A)
class _WwpLeosEtherPortVplsPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notDefined',1),('subscriber',2),('networkFacing',3)))
_WwpLeosEtherPortVplsPortType_Type.__name__=_C
_WwpLeosEtherPortVplsPortType_Object=MibTableColumn
wwpLeosEtherPortVplsPortType=_WwpLeosEtherPortVplsPortType_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,22),_WwpLeosEtherPortVplsPortType_Type())
wwpLeosEtherPortVplsPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortVplsPortType.setStatus(_A)
class _WwpLeosEtherPortIngressCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('leave',1),('fixed',2),('ippInherit',3),('phbgInherit',4)))
_WwpLeosEtherPortIngressCosPolicy_Type.__name__=_C
_WwpLeosEtherPortIngressCosPolicy_Object=MibTableColumn
wwpLeosEtherPortIngressCosPolicy=_WwpLeosEtherPortIngressCosPolicy_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,23),_WwpLeosEtherPortIngressCosPolicy_Type())
wwpLeosEtherPortIngressCosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortIngressCosPolicy.setStatus(_A)
class _WwpLeosEtherPortIngressFixedDot1dPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosEtherPortIngressFixedDot1dPri_Type.__name__=_C
_WwpLeosEtherPortIngressFixedDot1dPri_Object=MibTableColumn
wwpLeosEtherPortIngressFixedDot1dPri=_WwpLeosEtherPortIngressFixedDot1dPri_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,24),_WwpLeosEtherPortIngressFixedDot1dPri_Type())
wwpLeosEtherPortIngressFixedDot1dPri.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortIngressFixedDot1dPri.setStatus(_A)
class _WwpLeosEtherPortUntagDataVsi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosEtherPortUntagDataVsi_Type.__name__=_C
_WwpLeosEtherPortUntagDataVsi_Object=MibTableColumn
wwpLeosEtherPortUntagDataVsi=_WwpLeosEtherPortUntagDataVsi_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,25),_WwpLeosEtherPortUntagDataVsi_Type())
wwpLeosEtherPortUntagDataVsi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortUntagDataVsi.setStatus(_A)
_WwpLeosEtherPortOperationalSpeed_Type=Gauge32
_WwpLeosEtherPortOperationalSpeed_Object=MibTableColumn
wwpLeosEtherPortOperationalSpeed=_WwpLeosEtherPortOperationalSpeed_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,26),_WwpLeosEtherPortOperationalSpeed_Type())
wwpLeosEtherPortOperationalSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortOperationalSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosEtherPortOperationalSpeed.setUnits(_Z)
class _WwpLeosEtherPortUntagCtrlVsi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosEtherPortUntagCtrlVsi_Type.__name__=_C
_WwpLeosEtherPortUntagCtrlVsi_Object=MibTableColumn
wwpLeosEtherPortUntagCtrlVsi=_WwpLeosEtherPortUntagCtrlVsi_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,27),_WwpLeosEtherPortUntagCtrlVsi_Type())
wwpLeosEtherPortUntagCtrlVsi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortUntagCtrlVsi.setStatus(_A)
class _WwpLeosEtherPortMirrorPort_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortMirrorPort_Type.__name__=_F
_WwpLeosEtherPortMirrorPort_Object=MibTableColumn
wwpLeosEtherPortMirrorPort=_WwpLeosEtherPortMirrorPort_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,28),_WwpLeosEtherPortMirrorPort_Type())
wwpLeosEtherPortMirrorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMirrorPort.setStatus(_A)
class _WwpLeosEtherPortMirrorIngress_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosEtherPortMirrorIngress_Type.__name__=_C
_WwpLeosEtherPortMirrorIngress_Object=MibTableColumn
wwpLeosEtherPortMirrorIngress=_WwpLeosEtherPortMirrorIngress_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,29),_WwpLeosEtherPortMirrorIngress_Type())
wwpLeosEtherPortMirrorIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMirrorIngress.setStatus(_A)
class _WwpLeosEtherPortMirrorEgress_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosEtherPortMirrorEgress_Type.__name__=_C
_WwpLeosEtherPortMirrorEgress_Object=MibTableColumn
wwpLeosEtherPortMirrorEgress=_WwpLeosEtherPortMirrorEgress_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,30),_WwpLeosEtherPortMirrorEgress_Type())
wwpLeosEtherPortMirrorEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMirrorEgress.setStatus(_A)
class _WwpLeosEtherPortUntagDataVsiType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('mpls',2)))
_WwpLeosEtherPortUntagDataVsiType_Type.__name__=_C
_WwpLeosEtherPortUntagDataVsiType_Object=MibTableColumn
wwpLeosEtherPortUntagDataVsiType=_WwpLeosEtherPortUntagDataVsiType_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,31),_WwpLeosEtherPortUntagDataVsiType_Type())
wwpLeosEtherPortUntagDataVsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortUntagDataVsiType.setStatus(_A)
class _WwpLeosEtherPortUntagCtrlVsiType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('mpls',2)))
_WwpLeosEtherPortUntagCtrlVsiType_Type.__name__=_C
_WwpLeosEtherPortUntagCtrlVsiType_Object=MibTableColumn
wwpLeosEtherPortUntagCtrlVsiType=_WwpLeosEtherPortUntagCtrlVsiType_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,32),_WwpLeosEtherPortUntagCtrlVsiType_Type())
wwpLeosEtherPortUntagCtrlVsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortUntagCtrlVsiType.setStatus(_A)
class _WwpLeosEtherPortVsIngressFiltering_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortVsIngressFiltering_Type.__name__=_F
_WwpLeosEtherPortVsIngressFiltering_Object=MibTableColumn
wwpLeosEtherPortVsIngressFiltering=_WwpLeosEtherPortVsIngressFiltering_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,33),_WwpLeosEtherPortVsIngressFiltering_Type())
wwpLeosEtherPortVsIngressFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortVsIngressFiltering.setStatus(_A)
_WwpLeosEtherPortOperAutoNeg_Type=TruthValue
_WwpLeosEtherPortOperAutoNeg_Object=MibTableColumn
wwpLeosEtherPortOperAutoNeg=_WwpLeosEtherPortOperAutoNeg_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,34),_WwpLeosEtherPortOperAutoNeg_Type())
wwpLeosEtherPortOperAutoNeg.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortOperAutoNeg.setStatus(_A)
_WwpLeosEtherPortUpTime_Type=TimeTicks
_WwpLeosEtherPortUpTime_Object=MibTableColumn
wwpLeosEtherPortUpTime=_WwpLeosEtherPortUpTime_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,35),_WwpLeosEtherPortUpTime_Type())
wwpLeosEtherPortUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortUpTime.setStatus(_A)
class _WwpLeosEtherPortUntagDataVid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosEtherPortUntagDataVid_Type.__name__=_C
_WwpLeosEtherPortUntagDataVid_Object=MibTableColumn
wwpLeosEtherPortUntagDataVid=_WwpLeosEtherPortUntagDataVid_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,36),_WwpLeosEtherPortUntagDataVid_Type())
wwpLeosEtherPortUntagDataVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortUntagDataVid.setStatus(_A)
class _WwpLeosEtherPortPhyLoopback_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortPhyLoopback_Type.__name__=_F
_WwpLeosEtherPortPhyLoopback_Object=MibTableColumn
wwpLeosEtherPortPhyLoopback=_WwpLeosEtherPortPhyLoopback_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,37),_WwpLeosEtherPortPhyLoopback_Type())
wwpLeosEtherPortPhyLoopback.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortPhyLoopback.setStatus(_A)
class _WwpLeosEtherPortVlanIngressFilterStrict_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortVlanIngressFilterStrict_Type.__name__=_F
_WwpLeosEtherPortVlanIngressFilterStrict_Object=MibTableColumn
wwpLeosEtherPortVlanIngressFilterStrict=_WwpLeosEtherPortVlanIngressFilterStrict_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,38),_WwpLeosEtherPortVlanIngressFilterStrict_Type())
wwpLeosEtherPortVlanIngressFilterStrict.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortVlanIngressFilterStrict.setStatus(_A)
class _WwpLeosEtherPortMacSaDaSwap_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortMacSaDaSwap_Type.__name__=_F
_WwpLeosEtherPortMacSaDaSwap_Object=MibTableColumn
wwpLeosEtherPortMacSaDaSwap=_WwpLeosEtherPortMacSaDaSwap_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,39),_WwpLeosEtherPortMacSaDaSwap_Type())
wwpLeosEtherPortMacSaDaSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMacSaDaSwap.setStatus(_A)
class _WwpLeosEtherPortMacSaDaSwapVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosEtherPortMacSaDaSwapVlan_Type.__name__=_C
_WwpLeosEtherPortMacSaDaSwapVlan_Object=MibTableColumn
wwpLeosEtherPortMacSaDaSwapVlan=_WwpLeosEtherPortMacSaDaSwapVlan_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,40),_WwpLeosEtherPortMacSaDaSwapVlan_Type())
wwpLeosEtherPortMacSaDaSwapVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMacSaDaSwapVlan.setStatus(_A)
class _WwpLeosEtherPortResolvedCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('dot1d',1),('l3DscpCos',2),('fixedCos',3),(_I,99)))
_WwpLeosEtherPortResolvedCosPolicy_Type.__name__=_C
_WwpLeosEtherPortResolvedCosPolicy_Object=MibTableColumn
wwpLeosEtherPortResolvedCosPolicy=_WwpLeosEtherPortResolvedCosPolicy_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,41),_WwpLeosEtherPortResolvedCosPolicy_Type())
wwpLeosEtherPortResolvedCosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortResolvedCosPolicy.setStatus(_A)
class _WwpLeosEtherPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('rj45',1),('sfp',2),('default',3),(_I,99)))
_WwpLeosEtherPortMode_Type.__name__=_C
_WwpLeosEtherPortMode_Object=MibTableColumn
wwpLeosEtherPortMode=_WwpLeosEtherPortMode_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,42),_WwpLeosEtherPortMode_Type())
wwpLeosEtherPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMode.setStatus(_A)
class _WwpLeosEtherFixedRcos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosEtherFixedRcos_Type.__name__=_C
_WwpLeosEtherFixedRcos_Object=MibTableColumn
wwpLeosEtherFixedRcos=_WwpLeosEtherFixedRcos_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,43),_WwpLeosEtherFixedRcos_Type())
wwpLeosEtherFixedRcos.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherFixedRcos.setStatus(_A)
class _WwpLeosEtherPortEgressPortQueueMapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosEtherPortEgressPortQueueMapId_Type.__name__=_C
_WwpLeosEtherPortEgressPortQueueMapId_Object=MibTableColumn
wwpLeosEtherPortEgressPortQueueMapId=_WwpLeosEtherPortEgressPortQueueMapId_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,44),_WwpLeosEtherPortEgressPortQueueMapId_Type())
wwpLeosEtherPortEgressPortQueueMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortEgressPortQueueMapId.setStatus(_A)
class _WwpLeosEtherPortResolvedCosMapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosEtherPortResolvedCosMapId_Type.__name__=_C
_WwpLeosEtherPortResolvedCosMapId_Object=MibTableColumn
wwpLeosEtherPortResolvedCosMapId=_WwpLeosEtherPortResolvedCosMapId_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,45),_WwpLeosEtherPortResolvedCosMapId_Type())
wwpLeosEtherPortResolvedCosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortResolvedCosMapId.setStatus(_A)
_WwpLeosEtherPortResolvedCosRemarkL2_Type=TruthValue
_WwpLeosEtherPortResolvedCosRemarkL2_Object=MibTableColumn
wwpLeosEtherPortResolvedCosRemarkL2=_WwpLeosEtherPortResolvedCosRemarkL2_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,46),_WwpLeosEtherPortResolvedCosRemarkL2_Type())
wwpLeosEtherPortResolvedCosRemarkL2.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortResolvedCosRemarkL2.setStatus(_A)
class _WwpLeosEtherPortL2TransformMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('iPush-e-Pop',1),('iStamp-Push-e-QualifiedPopStamp',2),('iPush-e-PopStamp',3)))
_WwpLeosEtherPortL2TransformMode_Type.__name__=_C
_WwpLeosEtherPortL2TransformMode_Object=MibTableColumn
wwpLeosEtherPortL2TransformMode=_WwpLeosEtherPortL2TransformMode_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,47),_WwpLeosEtherPortL2TransformMode_Type())
wwpLeosEtherPortL2TransformMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortL2TransformMode.setStatus(_A)
class _WwpLeosEtherPortLinkFlapDetection_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortLinkFlapDetection_Type.__name__=_F
_WwpLeosEtherPortLinkFlapDetection_Object=MibTableColumn
wwpLeosEtherPortLinkFlapDetection=_WwpLeosEtherPortLinkFlapDetection_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,48),_WwpLeosEtherPortLinkFlapDetection_Type())
wwpLeosEtherPortLinkFlapDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortLinkFlapDetection.setStatus(_A)
class _WwpLeosEtherPortLinkFlapCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosEtherPortLinkFlapCount_Type.__name__=_C
_WwpLeosEtherPortLinkFlapCount_Object=MibTableColumn
wwpLeosEtherPortLinkFlapCount=_WwpLeosEtherPortLinkFlapCount_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,49),_WwpLeosEtherPortLinkFlapCount_Type())
wwpLeosEtherPortLinkFlapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortLinkFlapCount.setStatus(_A)
class _WwpLeosEtherPortLinkFlapDetectTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_WwpLeosEtherPortLinkFlapDetectTime_Type.__name__=_C
_WwpLeosEtherPortLinkFlapDetectTime_Object=MibTableColumn
wwpLeosEtherPortLinkFlapDetectTime=_WwpLeosEtherPortLinkFlapDetectTime_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,50),_WwpLeosEtherPortLinkFlapDetectTime_Type())
wwpLeosEtherPortLinkFlapDetectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortLinkFlapDetectTime.setStatus(_A)
class _WwpLeosEtherPortLinkFlapHoldTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_WwpLeosEtherPortLinkFlapHoldTime_Type.__name__=_C
_WwpLeosEtherPortLinkFlapHoldTime_Object=MibTableColumn
wwpLeosEtherPortLinkFlapHoldTime=_WwpLeosEtherPortLinkFlapHoldTime_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,51),_WwpLeosEtherPortLinkFlapHoldTime_Type())
wwpLeosEtherPortLinkFlapHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortLinkFlapHoldTime.setStatus(_A)
class _WwpLeosEtherFixedRColor_Type(PortIngressFixedColor):defaultValue=1
_WwpLeosEtherFixedRColor_Type.__name__=_h
_WwpLeosEtherFixedRColor_Object=MibTableColumn
wwpLeosEtherFixedRColor=_WwpLeosEtherFixedRColor_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,52),_WwpLeosEtherFixedRColor_Type())
wwpLeosEtherFixedRColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherFixedRColor.setStatus(_A)
class _WwpLeosEtherPortFrameCosMapId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosEtherPortFrameCosMapId_Type.__name__=_C
_WwpLeosEtherPortFrameCosMapId_Object=MibTableColumn
wwpLeosEtherPortFrameCosMapId=_WwpLeosEtherPortFrameCosMapId_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,53),_WwpLeosEtherPortFrameCosMapId_Type())
wwpLeosEtherPortFrameCosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortFrameCosMapId.setStatus(_A)
class _WwpLeosEtherPortEgressCosPolicy_Type(PortEgressFrameCosPolicy):defaultValue=1
_WwpLeosEtherPortEgressCosPolicy_Type.__name__=_i
_WwpLeosEtherPortEgressCosPolicy_Object=MibTableColumn
wwpLeosEtherPortEgressCosPolicy=_WwpLeosEtherPortEgressCosPolicy_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,54),_WwpLeosEtherPortEgressCosPolicy_Type())
wwpLeosEtherPortEgressCosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortEgressCosPolicy.setStatus(_A)
_WwpLeosEtherPortEgressSpeed_Type=Gauge32
_WwpLeosEtherPortEgressSpeed_Object=MibTableColumn
wwpLeosEtherPortEgressSpeed=_WwpLeosEtherPortEgressSpeed_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,55),_WwpLeosEtherPortEgressSpeed_Type())
wwpLeosEtherPortEgressSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortEgressSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosEtherPortEgressSpeed.setUnits(_Z)
_WwpLeosEtherPortAdaptiveRateSpeed_Type=Gauge32
_WwpLeosEtherPortAdaptiveRateSpeed_Object=MibTableColumn
wwpLeosEtherPortAdaptiveRateSpeed=_WwpLeosEtherPortAdaptiveRateSpeed_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,56),_WwpLeosEtherPortAdaptiveRateSpeed_Type())
wwpLeosEtherPortAdaptiveRateSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortAdaptiveRateSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosEtherPortAdaptiveRateSpeed.setUnits(_Z)
class _WwpLeosEtherPortMirrorEncap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('vlanTag',1)))
_WwpLeosEtherPortMirrorEncap_Type.__name__=_C
_WwpLeosEtherPortMirrorEncap_Object=MibTableColumn
wwpLeosEtherPortMirrorEncap=_WwpLeosEtherPortMirrorEncap_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,57),_WwpLeosEtherPortMirrorEncap_Type())
wwpLeosEtherPortMirrorEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMirrorEncap.setStatus(_A)
class _WwpLeosEtherPortMirrorEncapVid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosEtherPortMirrorEncapVid_Type.__name__=_C
_WwpLeosEtherPortMirrorEncapVid_Object=MibTableColumn
wwpLeosEtherPortMirrorEncapVid=_WwpLeosEtherPortMirrorEncapVid_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,58),_WwpLeosEtherPortMirrorEncapVid_Type())
wwpLeosEtherPortMirrorEncapVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMirrorEncapVid.setStatus(_A)
class _WwpLeosEtherPortMirrorEncapTpid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tpid8100',1),('tpid9100',2),('tpid88A8',3)))
_WwpLeosEtherPortMirrorEncapTpid_Type.__name__=_C
_WwpLeosEtherPortMirrorEncapTpid_Object=MibTableColumn
wwpLeosEtherPortMirrorEncapTpid=_WwpLeosEtherPortMirrorEncapTpid_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,59),_WwpLeosEtherPortMirrorEncapTpid_Type())
wwpLeosEtherPortMirrorEncapTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortMirrorEncapTpid.setStatus(_A)
class _WwpLeosEtherPortIfgDecrease_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_WwpLeosEtherPortIfgDecrease_Type.__name__=_C
_WwpLeosEtherPortIfgDecrease_Object=MibTableColumn
wwpLeosEtherPortIfgDecrease=_WwpLeosEtherPortIfgDecrease_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,60),_WwpLeosEtherPortIfgDecrease_Type())
wwpLeosEtherPortIfgDecrease.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortIfgDecrease.setStatus(_A)
class _WwpLeosEtherPortAdvertSpeed_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_j,1),('ten',2),('hundred',3),('gigabit',4),('ten-hundred-gigabit',5)))
_WwpLeosEtherPortAdvertSpeed_Type.__name__=_C
_WwpLeosEtherPortAdvertSpeed_Object=MibTableColumn
wwpLeosEtherPortAdvertSpeed=_WwpLeosEtherPortAdvertSpeed_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,61),_WwpLeosEtherPortAdvertSpeed_Type())
wwpLeosEtherPortAdvertSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdvertSpeed.setStatus(_A)
class _WwpLeosEtherPortAdvertDuplex_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_j,1),(_U,2),(_V,3),('half-full',4)))
_WwpLeosEtherPortAdvertDuplex_Type.__name__=_C
_WwpLeosEtherPortAdvertDuplex_Object=MibTableColumn
wwpLeosEtherPortAdvertDuplex=_WwpLeosEtherPortAdvertDuplex_Object((1,3,6,1,4,1,6141,2,60,2,1,1,1,1,62),_WwpLeosEtherPortAdvertDuplex_Type())
wwpLeosEtherPortAdvertDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortAdvertDuplex.setStatus(_A)
_WwpLeosEtherPortFlushTable_Object=MibTable
wwpLeosEtherPortFlushTable=_WwpLeosEtherPortFlushTable_Object((1,3,6,1,4,1,6141,2,60,2,1,1,2))
if mibBuilder.loadTexts:wwpLeosEtherPortFlushTable.setStatus(_A)
_WwpLeosEtherPortFlushEntry_Object=MibTableRow
wwpLeosEtherPortFlushEntry=_WwpLeosEtherPortFlushEntry_Object((1,3,6,1,4,1,6141,2,60,2,1,1,2,1))
wwpLeosEtherPortFlushEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpLeosEtherPortFlushEntry.setStatus(_A)
class _WwpLeosEtherPortFlushActivate_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortFlushActivate_Type.__name__=_F
_WwpLeosEtherPortFlushActivate_Object=MibTableColumn
wwpLeosEtherPortFlushActivate=_WwpLeosEtherPortFlushActivate_Object((1,3,6,1,4,1,6141,2,60,2,1,1,2,1,1),_WwpLeosEtherPortFlushActivate_Type())
wwpLeosEtherPortFlushActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortFlushActivate.setStatus(_A)
_WwpLeosEtherPortTrapsTable_Object=MibTable
wwpLeosEtherPortTrapsTable=_WwpLeosEtherPortTrapsTable_Object((1,3,6,1,4,1,6141,2,60,2,1,1,3))
if mibBuilder.loadTexts:wwpLeosEtherPortTrapsTable.setStatus(_A)
_WwpLeosEtherPortTrapsEntry_Object=MibTableRow
wwpLeosEtherPortTrapsEntry=_WwpLeosEtherPortTrapsEntry_Object((1,3,6,1,4,1,6141,2,60,2,1,1,3,1))
wwpLeosEtherPortTrapsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpLeosEtherPortTrapsEntry.setStatus(_A)
class _WwpLeosEtherPortTrapsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_WwpLeosEtherPortTrapsState_Type.__name__=_C
_WwpLeosEtherPortTrapsState_Object=MibTableColumn
wwpLeosEtherPortTrapsState=_WwpLeosEtherPortTrapsState_Object((1,3,6,1,4,1,6141,2,60,2,1,1,3,1,1),_WwpLeosEtherPortTrapsState_Type())
wwpLeosEtherPortTrapsState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortTrapsState.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupTable_Object=MibTable
wwpLeosEtherPortStateMirrorGroupTable=_WwpLeosEtherPortStateMirrorGroupTable_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4))
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupTable.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupEntry_Object=MibTableRow
wwpLeosEtherPortStateMirrorGroupEntry=_WwpLeosEtherPortStateMirrorGroupEntry_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1))
wwpLeosEtherPortStateMirrorGroupEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupEntry.setStatus(_A)
class _WwpLeosEtherPortStateMirrorGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosEtherPortStateMirrorGroupId_Type.__name__=_C
_WwpLeosEtherPortStateMirrorGroupId_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupId=_WwpLeosEtherPortStateMirrorGroupId_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,1),_WwpLeosEtherPortStateMirrorGroupId_Type())
wwpLeosEtherPortStateMirrorGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupId.setStatus(_A)
class _WwpLeosEtherPortStateMirrorGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosEtherPortStateMirrorGroupName_Type.__name__=_P
_WwpLeosEtherPortStateMirrorGroupName_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupName=_WwpLeosEtherPortStateMirrorGroupName_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,2),_WwpLeosEtherPortStateMirrorGroupName_Type())
wwpLeosEtherPortStateMirrorGroupName.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupName.setStatus(_A)
class _WwpLeosEtherPortStateMirrorGroupOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_WwpLeosEtherPortStateMirrorGroupOperStatus_Type.__name__=_C
_WwpLeosEtherPortStateMirrorGroupOperStatus_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupOperStatus=_WwpLeosEtherPortStateMirrorGroupOperStatus_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,3),_WwpLeosEtherPortStateMirrorGroupOperStatus_Type())
wwpLeosEtherPortStateMirrorGroupOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupOperStatus.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Type=Counter32
_WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupNumSrcPorts=_WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,4),_WwpLeosEtherPortStateMirrorGroupNumSrcPorts_Type())
wwpLeosEtherPortStateMirrorGroupNumSrcPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupNumSrcPorts.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupNumDstPorts_Type=Counter32
_WwpLeosEtherPortStateMirrorGroupNumDstPorts_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupNumDstPorts=_WwpLeosEtherPortStateMirrorGroupNumDstPorts_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,5),_WwpLeosEtherPortStateMirrorGroupNumDstPorts_Type())
wwpLeosEtherPortStateMirrorGroupNumDstPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupNumDstPorts.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupStatus_Type=RowStatus
_WwpLeosEtherPortStateMirrorGroupStatus_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupStatus=_WwpLeosEtherPortStateMirrorGroupStatus_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,6),_WwpLeosEtherPortStateMirrorGroupStatus_Type())
wwpLeosEtherPortStateMirrorGroupStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupStatus.setStatus(_A)
class _WwpLeosEtherPortStateMirrorGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_WwpLeosEtherPortStateMirrorGroupType_Type.__name__=_C
_WwpLeosEtherPortStateMirrorGroupType_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupType=_WwpLeosEtherPortStateMirrorGroupType_Object((1,3,6,1,4,1,6141,2,60,2,1,1,4,1,7),_WwpLeosEtherPortStateMirrorGroupType_Type())
wwpLeosEtherPortStateMirrorGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupType.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupMemTable_Object=MibTable
wwpLeosEtherPortStateMirrorGroupMemTable=_WwpLeosEtherPortStateMirrorGroupMemTable_Object((1,3,6,1,4,1,6141,2,60,2,1,1,5))
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupMemTable.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupMemEntry_Object=MibTableRow
wwpLeosEtherPortStateMirrorGroupMemEntry=_WwpLeosEtherPortStateMirrorGroupMemEntry_Object((1,3,6,1,4,1,6141,2,60,2,1,1,5,1))
wwpLeosEtherPortStateMirrorGroupMemEntry.setIndexNames((0,_D,_a),(0,_D,_G))
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupMemEntry.setStatus(_A)
class _WwpLeosEtherPortStateMirrorGroupMemType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('srcPort',1),('dstPort',2)))
_WwpLeosEtherPortStateMirrorGroupMemType_Type.__name__=_C
_WwpLeosEtherPortStateMirrorGroupMemType_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupMemType=_WwpLeosEtherPortStateMirrorGroupMemType_Object((1,3,6,1,4,1,6141,2,60,2,1,1,5,1,1),_WwpLeosEtherPortStateMirrorGroupMemType_Type())
wwpLeosEtherPortStateMirrorGroupMemType.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupMemType.setStatus(_A)
class _WwpLeosEtherPortStateMirrorGroupMemOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_WwpLeosEtherPortStateMirrorGroupMemOperState_Type.__name__=_C
_WwpLeosEtherPortStateMirrorGroupMemOperState_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupMemOperState=_WwpLeosEtherPortStateMirrorGroupMemOperState_Object((1,3,6,1,4,1,6141,2,60,2,1,1,5,1,2),_WwpLeosEtherPortStateMirrorGroupMemOperState_Type())
wwpLeosEtherPortStateMirrorGroupMemOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupMemOperState.setStatus(_A)
_WwpLeosEtherPortStateMirrorGroupMemStatus_Type=RowStatus
_WwpLeosEtherPortStateMirrorGroupMemStatus_Object=MibTableColumn
wwpLeosEtherPortStateMirrorGroupMemStatus=_WwpLeosEtherPortStateMirrorGroupMemStatus_Object((1,3,6,1,4,1,6141,2,60,2,1,1,5,1,3),_WwpLeosEtherPortStateMirrorGroupMemStatus_Type())
wwpLeosEtherPortStateMirrorGroupMemStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosEtherPortStateMirrorGroupMemStatus.setStatus(_A)
_WwpLeosEtherPortNotif_ObjectIdentity=ObjectIdentity
wwpLeosEtherPortNotif=_WwpLeosEtherPortNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,1,2))
class _WwpLeosEtherStndLinkUpDownTrapsEnable_Type(TruthValue):defaultValue=1
_WwpLeosEtherStndLinkUpDownTrapsEnable_Type.__name__=_F
_WwpLeosEtherStndLinkUpDownTrapsEnable_Object=MibScalar
wwpLeosEtherStndLinkUpDownTrapsEnable=_WwpLeosEtherStndLinkUpDownTrapsEnable_Object((1,3,6,1,4,1,6141,2,60,2,1,2,1),_WwpLeosEtherStndLinkUpDownTrapsEnable_Type())
wwpLeosEtherStndLinkUpDownTrapsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherStndLinkUpDownTrapsEnable.setStatus(_A)
class _WwpLeosEtherPortLinkUpDownTrapsEnable_Type(TruthValue):defaultValue=2
_WwpLeosEtherPortLinkUpDownTrapsEnable_Type.__name__=_F
_WwpLeosEtherPortLinkUpDownTrapsEnable_Object=MibScalar
wwpLeosEtherPortLinkUpDownTrapsEnable=_WwpLeosEtherPortLinkUpDownTrapsEnable_Object((1,3,6,1,4,1,6141,2,60,2,1,2,2),_WwpLeosEtherPortLinkUpDownTrapsEnable_Type())
wwpLeosEtherPortLinkUpDownTrapsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherPortLinkUpDownTrapsEnable.setStatus(_A)
class _WwpLeosEtherAggPortLinkUpDownTrapsEnable_Type(TruthValue):defaultValue=2
_WwpLeosEtherAggPortLinkUpDownTrapsEnable_Type.__name__=_F
_WwpLeosEtherAggPortLinkUpDownTrapsEnable_Object=MibScalar
wwpLeosEtherAggPortLinkUpDownTrapsEnable=_WwpLeosEtherAggPortLinkUpDownTrapsEnable_Object((1,3,6,1,4,1,6141,2,60,2,1,2,3),_WwpLeosEtherAggPortLinkUpDownTrapsEnable_Type())
wwpLeosEtherAggPortLinkUpDownTrapsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosEtherAggPortLinkUpDownTrapsEnable.setStatus(_A)
_WwpLeosPortMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosPortMIBNotificationPrefix=_WwpLeosPortMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,2))
_WwpLeosPortMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosPortMIBNotifications=_WwpLeosPortMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,2,0))
_WwpLeosPortMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosPortMIBConformance=_WwpLeosPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,3))
_WwpLeosPortMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosPortMIBCompliances=_WwpLeosPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,3,1))
_WwpLeosPortMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosPortMIBGroups=_WwpLeosPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,2,3,2))
wwpLeosEthLinkUp=NotificationType((1,3,6,1,4,1,6141,2,60,2,2,0,3))
wwpLeosEthLinkUp.setObjects(*((_H,_M),(_H,_L),(_D,_G),(_D,_J),(_D,_N),(_D,_R),(_D,_O),(_D,_K)))
if mibBuilder.loadTexts:wwpLeosEthLinkUp.setStatus(_A)
wwpLeosEthLinkDown=NotificationType((1,3,6,1,4,1,6141,2,60,2,2,0,4))
wwpLeosEthLinkDown.setObjects(*((_H,_M),(_H,_L),(_D,_G),(_D,_N),(_D,_J),(_D,_R),(_D,_O),(_D,_K)))
if mibBuilder.loadTexts:wwpLeosEthLinkDown.setStatus(_A)
wwpLeosEthAdminSpeedIncompatible=NotificationType((1,3,6,1,4,1,6141,2,60,2,2,0,5))
wwpLeosEthAdminSpeedIncompatible.setObjects((_D,_G))
if mibBuilder.loadTexts:wwpLeosEthAdminSpeedIncompatible.setStatus(_A)
wwpLeosEthLinkFlap=NotificationType((1,3,6,1,4,1,6141,2,60,2,2,0,6))
wwpLeosEthLinkFlap.setObjects(*((_H,_M),(_H,_L),(_D,_G),(_D,_N),(_D,_J),(_D,_O),(_D,_K),(_D,_m)))
if mibBuilder.loadTexts:wwpLeosEthLinkFlap.setStatus(_A)
wwpLeosAggLinkUpDown=NotificationType((1,3,6,1,4,1,6141,2,60,2,2,0,7))
wwpLeosAggLinkUpDown.setObjects(*((_H,_M),(_H,_L),(_D,_G),(_D,_J),(_D,_K),(_D,_N),(_D,_R),(_D,_O),(_S,_b),(_S,_c),(_D,_J),(_D,_K)))
if mibBuilder.loadTexts:wwpLeosAggLinkUpDown.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,_i:PortEgressFrameCosPolicy,_h:PortIngressFixedColor,'wwpLeosPortMIB':wwpLeosPortMIB,'wwpLeosPortMIBObjects':wwpLeosPortMIBObjects,'wwpLeosEtherPort':wwpLeosEtherPort,'wwpLeosEtherPortTable':wwpLeosEtherPortTable,'wwpLeosEtherPortEntry':wwpLeosEtherPortEntry,_G:wwpLeosEtherPortId,_J:wwpLeosEtherPortName,_K:wwpLeosEtherPortDesc,_N:wwpLeosEtherPortType,'wwpLeosEtherPortPhysAddr':wwpLeosEtherPortPhysAddr,'wwpLeosEtherPortAutoNeg':wwpLeosEtherPortAutoNeg,_R:wwpLeosEtherPortAdminStatus,_O:wwpLeosEtherPortOperStatus,'wwpLeosEtherPortAdminSpeed':wwpLeosEtherPortAdminSpeed,'wwpLeosEtherPortOperSpeed':wwpLeosEtherPortOperSpeed,'wwpLeosEtherPortAdminDuplex':wwpLeosEtherPortAdminDuplex,'wwpLeosEtherPortOperDuplex':wwpLeosEtherPortOperDuplex,'wwpLeosEtherPortAdminFlowCtrl':wwpLeosEtherPortAdminFlowCtrl,'wwpLeosEtherPortOperFlowCtrl':wwpLeosEtherPortOperFlowCtrl,'wwpLeosEtherIngressPvid':wwpLeosEtherIngressPvid,'wwpLeosEtherUntagEgressVlanId':wwpLeosEtherUntagEgressVlanId,'wwpLeosEtherPortAcceptableFrameTypes':wwpLeosEtherPortAcceptableFrameTypes,'wwpLeosEtherPortUntaggedPriority':wwpLeosEtherPortUntaggedPriority,'wwpLeosEtherPortMaxFrameSize':wwpLeosEtherPortMaxFrameSize,'wwpLeosEtherPortVlanIngressFiltering':wwpLeosEtherPortVlanIngressFiltering,'wwpLeosEtherPortAdminAdvertisedFlowCtrl':wwpLeosEtherPortAdminAdvertisedFlowCtrl,'wwpLeosEtherPortVplsPortType':wwpLeosEtherPortVplsPortType,'wwpLeosEtherPortIngressCosPolicy':wwpLeosEtherPortIngressCosPolicy,'wwpLeosEtherPortIngressFixedDot1dPri':wwpLeosEtherPortIngressFixedDot1dPri,'wwpLeosEtherPortUntagDataVsi':wwpLeosEtherPortUntagDataVsi,'wwpLeosEtherPortOperationalSpeed':wwpLeosEtherPortOperationalSpeed,'wwpLeosEtherPortUntagCtrlVsi':wwpLeosEtherPortUntagCtrlVsi,'wwpLeosEtherPortMirrorPort':wwpLeosEtherPortMirrorPort,'wwpLeosEtherPortMirrorIngress':wwpLeosEtherPortMirrorIngress,'wwpLeosEtherPortMirrorEgress':wwpLeosEtherPortMirrorEgress,'wwpLeosEtherPortUntagDataVsiType':wwpLeosEtherPortUntagDataVsiType,'wwpLeosEtherPortUntagCtrlVsiType':wwpLeosEtherPortUntagCtrlVsiType,'wwpLeosEtherPortVsIngressFiltering':wwpLeosEtherPortVsIngressFiltering,'wwpLeosEtherPortOperAutoNeg':wwpLeosEtherPortOperAutoNeg,'wwpLeosEtherPortUpTime':wwpLeosEtherPortUpTime,'wwpLeosEtherPortUntagDataVid':wwpLeosEtherPortUntagDataVid,'wwpLeosEtherPortPhyLoopback':wwpLeosEtherPortPhyLoopback,'wwpLeosEtherPortVlanIngressFilterStrict':wwpLeosEtherPortVlanIngressFilterStrict,'wwpLeosEtherPortMacSaDaSwap':wwpLeosEtherPortMacSaDaSwap,'wwpLeosEtherPortMacSaDaSwapVlan':wwpLeosEtherPortMacSaDaSwapVlan,'wwpLeosEtherPortResolvedCosPolicy':wwpLeosEtherPortResolvedCosPolicy,'wwpLeosEtherPortMode':wwpLeosEtherPortMode,'wwpLeosEtherFixedRcos':wwpLeosEtherFixedRcos,'wwpLeosEtherPortEgressPortQueueMapId':wwpLeosEtherPortEgressPortQueueMapId,'wwpLeosEtherPortResolvedCosMapId':wwpLeosEtherPortResolvedCosMapId,'wwpLeosEtherPortResolvedCosRemarkL2':wwpLeosEtherPortResolvedCosRemarkL2,'wwpLeosEtherPortL2TransformMode':wwpLeosEtherPortL2TransformMode,'wwpLeosEtherPortLinkFlapDetection':wwpLeosEtherPortLinkFlapDetection,'wwpLeosEtherPortLinkFlapCount':wwpLeosEtherPortLinkFlapCount,'wwpLeosEtherPortLinkFlapDetectTime':wwpLeosEtherPortLinkFlapDetectTime,_m:wwpLeosEtherPortLinkFlapHoldTime,'wwpLeosEtherFixedRColor':wwpLeosEtherFixedRColor,'wwpLeosEtherPortFrameCosMapId':wwpLeosEtherPortFrameCosMapId,'wwpLeosEtherPortEgressCosPolicy':wwpLeosEtherPortEgressCosPolicy,'wwpLeosEtherPortEgressSpeed':wwpLeosEtherPortEgressSpeed,'wwpLeosEtherPortAdaptiveRateSpeed':wwpLeosEtherPortAdaptiveRateSpeed,'wwpLeosEtherPortMirrorEncap':wwpLeosEtherPortMirrorEncap,'wwpLeosEtherPortMirrorEncapVid':wwpLeosEtherPortMirrorEncapVid,'wwpLeosEtherPortMirrorEncapTpid':wwpLeosEtherPortMirrorEncapTpid,'wwpLeosEtherPortIfgDecrease':wwpLeosEtherPortIfgDecrease,'wwpLeosEtherPortAdvertSpeed':wwpLeosEtherPortAdvertSpeed,'wwpLeosEtherPortAdvertDuplex':wwpLeosEtherPortAdvertDuplex,'wwpLeosEtherPortFlushTable':wwpLeosEtherPortFlushTable,'wwpLeosEtherPortFlushEntry':wwpLeosEtherPortFlushEntry,'wwpLeosEtherPortFlushActivate':wwpLeosEtherPortFlushActivate,'wwpLeosEtherPortTrapsTable':wwpLeosEtherPortTrapsTable,'wwpLeosEtherPortTrapsEntry':wwpLeosEtherPortTrapsEntry,'wwpLeosEtherPortTrapsState':wwpLeosEtherPortTrapsState,'wwpLeosEtherPortStateMirrorGroupTable':wwpLeosEtherPortStateMirrorGroupTable,'wwpLeosEtherPortStateMirrorGroupEntry':wwpLeosEtherPortStateMirrorGroupEntry,_a:wwpLeosEtherPortStateMirrorGroupId,'wwpLeosEtherPortStateMirrorGroupName':wwpLeosEtherPortStateMirrorGroupName,'wwpLeosEtherPortStateMirrorGroupOperStatus':wwpLeosEtherPortStateMirrorGroupOperStatus,'wwpLeosEtherPortStateMirrorGroupNumSrcPorts':wwpLeosEtherPortStateMirrorGroupNumSrcPorts,'wwpLeosEtherPortStateMirrorGroupNumDstPorts':wwpLeosEtherPortStateMirrorGroupNumDstPorts,'wwpLeosEtherPortStateMirrorGroupStatus':wwpLeosEtherPortStateMirrorGroupStatus,'wwpLeosEtherPortStateMirrorGroupType':wwpLeosEtherPortStateMirrorGroupType,'wwpLeosEtherPortStateMirrorGroupMemTable':wwpLeosEtherPortStateMirrorGroupMemTable,'wwpLeosEtherPortStateMirrorGroupMemEntry':wwpLeosEtherPortStateMirrorGroupMemEntry,'wwpLeosEtherPortStateMirrorGroupMemType':wwpLeosEtherPortStateMirrorGroupMemType,'wwpLeosEtherPortStateMirrorGroupMemOperState':wwpLeosEtherPortStateMirrorGroupMemOperState,'wwpLeosEtherPortStateMirrorGroupMemStatus':wwpLeosEtherPortStateMirrorGroupMemStatus,'wwpLeosEtherPortNotif':wwpLeosEtherPortNotif,'wwpLeosEtherStndLinkUpDownTrapsEnable':wwpLeosEtherStndLinkUpDownTrapsEnable,'wwpLeosEtherPortLinkUpDownTrapsEnable':wwpLeosEtherPortLinkUpDownTrapsEnable,'wwpLeosEtherAggPortLinkUpDownTrapsEnable':wwpLeosEtherAggPortLinkUpDownTrapsEnable,'wwpLeosPortMIBNotificationPrefix':wwpLeosPortMIBNotificationPrefix,'wwpLeosPortMIBNotifications':wwpLeosPortMIBNotifications,'wwpLeosEthLinkUp':wwpLeosEthLinkUp,'wwpLeosEthLinkDown':wwpLeosEthLinkDown,'wwpLeosEthAdminSpeedIncompatible':wwpLeosEthAdminSpeedIncompatible,'wwpLeosEthLinkFlap':wwpLeosEthLinkFlap,'wwpLeosAggLinkUpDown':wwpLeosAggLinkUpDown,'wwpLeosPortMIBConformance':wwpLeosPortMIBConformance,'wwpLeosPortMIBCompliances':wwpLeosPortMIBCompliances,'wwpLeosPortMIBGroups':wwpLeosPortMIBGroups})