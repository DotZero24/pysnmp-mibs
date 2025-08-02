_Y='tnLagConfigXEntry'
_X='tnLagPortEntry'
_W='tnLagOperationEntry'
_V='tnLagSubgroup'
_U='LAGSubgroup'
_T='not-accessible'
_S='TItemLongDescription'
_R='tnPortPortID'
_Q='TN-PORT-MIB'
_P='Unsigned32'
_O='InetAddressType'
_N='InetAddress'
_M='OctetString'
_L='tnLagPortThreshold'
_K='active'
_J='tnLagIndex'
_I='tnSysSwitchId'
_H='TROPIC-SYSTEM-MIB'
_G='read-write'
_F='TruthValue'
_E='TN-LAG-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3adAggPortEntry,=mibBuilder.importSymbols('IEEE8023-LAG-MIB','dot3adAggPortEntry')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_F)
tnPortPortID,=mibBuilder.importSymbols(_Q,_R)
TItemLongDescription,TNamedItemOrEmpty=mibBuilder.importSymbols('TN-TC-MIB',_S,'TNamedItemOrEmpty')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_H,_I)
tnLagMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,15))
if mibBuilder.loadTexts:tnLagMIBModule.setRevisions(('2020-02-14 00:00','2019-09-13 00:00','2019-03-01 00:00','2014-11-25 00:00','2012-12-13 00:00','2012-12-05 00:00','2012-04-27 00:00','2012-02-21 00:00','2009-02-28 00:00','2008-07-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-03-15 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2001-02-09 00:00'))
class LAGInterfaceNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
class LAGSubgroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,-2),ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,8))
_TnLagObjects_ObjectIdentity=ObjectIdentity
tnLagObjects=_TnLagObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,15))
_TnLagConfigTable_Object=MibTable
tnLagConfigTable=_TnLagConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,15,2))
if mibBuilder.loadTexts:tnLagConfigTable.setStatus(_A)
_TnLagConfigEntry_Object=MibTableRow
tnLagConfigEntry=_TnLagConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1))
tnLagConfigEntry.setIndexNames((0,_H,_I),(0,_E,_J))
if mibBuilder.loadTexts:tnLagConfigEntry.setStatus(_A)
_TnLagIndex_Type=LAGInterfaceNumber
_TnLagIndex_Object=MibTableColumn
tnLagIndex=_TnLagIndex_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,1),_TnLagIndex_Type())
tnLagIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:tnLagIndex.setStatus(_A)
_TnLagRowStatus_Type=RowStatus
_TnLagRowStatus_Object=MibTableColumn
tnLagRowStatus=_TnLagRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,2),_TnLagRowStatus_Type())
tnLagRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagRowStatus.setStatus(_A)
class _TnLagPortThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_TnLagPortThreshold_Type.__name__=_D
_TnLagPortThreshold_Object=MibTableColumn
tnLagPortThreshold=_TnLagPortThreshold_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,3),_TnLagPortThreshold_Type())
tnLagPortThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagPortThreshold.setStatus(_A)
class _TnLagPortThresholdAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('dynamicCost',2)))
_TnLagPortThresholdAction_Type.__name__=_D
_TnLagPortThresholdAction_Object=MibTableColumn
tnLagPortThresholdAction=_TnLagPortThresholdAction_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,4),_TnLagPortThresholdAction_Type())
tnLagPortThresholdAction.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagPortThresholdAction.setStatus(_A)
class _TnLagEnableMarkerGenerator_Type(TruthValue):defaultValue=2
_TnLagEnableMarkerGenerator_Type.__name__=_F
_TnLagEnableMarkerGenerator_Object=MibTableColumn
tnLagEnableMarkerGenerator=_TnLagEnableMarkerGenerator_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,5),_TnLagEnableMarkerGenerator_Type())
tnLagEnableMarkerGenerator.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagEnableMarkerGenerator.setStatus(_A)
class _TnLagEnableLACP_Type(TruthValue):defaultValue=2
_TnLagEnableLACP_Type.__name__=_F
_TnLagEnableLACP_Object=MibTableColumn
tnLagEnableLACP=_TnLagEnableLACP_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,6),_TnLagEnableLACP_Type())
tnLagEnableLACP.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagEnableLACP.setStatus(_A)
class _TnLagDescription_Type(TItemLongDescription):defaultHexValue=''
_TnLagDescription_Type.__name__=_S
_TnLagDescription_Object=MibTableColumn
tnLagDescription=_TnLagDescription_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,7),_TnLagDescription_Type())
tnLagDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagDescription.setStatus(_A)
class _TnLagDynamicCosting_Type(TruthValue):defaultValue=2
_TnLagDynamicCosting_Type.__name__=_F
_TnLagDynamicCosting_Object=MibTableColumn
tnLagDynamicCosting=_TnLagDynamicCosting_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,8),_TnLagDynamicCosting_Type())
tnLagDynamicCosting.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagDynamicCosting.setStatus(_A)
class _TnLagLACPMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passive',1),(_K,2)))
_TnLagLACPMode_Type.__name__=_D
_TnLagLACPMode_Object=MibTableColumn
tnLagLACPMode=_TnLagLACPMode_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,9),_TnLagLACPMode_Type())
tnLagLACPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLACPMode.setStatus(_A)
class _TnLagLACPAdminKeyAutogen_Type(TruthValue):defaultValue=1
_TnLagLACPAdminKeyAutogen_Type.__name__=_F
_TnLagLACPAdminKeyAutogen_Object=MibTableColumn
tnLagLACPAdminKeyAutogen=_TnLagLACPAdminKeyAutogen_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,10),_TnLagLACPAdminKeyAutogen_Type())
tnLagLACPAdminKeyAutogen.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagLACPAdminKeyAutogen.setStatus(_A)
class _TnLagLACPTransmitInterval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slow',1),('fast',2)))
_TnLagLACPTransmitInterval_Type.__name__=_D
_TnLagLACPTransmitInterval_Object=MibTableColumn
tnLagLACPTransmitInterval=_TnLagLACPTransmitInterval_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,11),_TnLagLACPTransmitInterval_Type())
tnLagLACPTransmitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLACPTransmitInterval.setStatus(_A)
class _TnLagAccessAdaptQos_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),('distribute',2)))
_TnLagAccessAdaptQos_Type.__name__=_D
_TnLagAccessAdaptQos_Object=MibTableColumn
tnLagAccessAdaptQos=_TnLagAccessAdaptQos_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,12),_TnLagAccessAdaptQos_Type())
tnLagAccessAdaptQos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagAccessAdaptQos.setStatus(_A)
class _TnLagLACPXmitStdby_Type(TruthValue):defaultValue=1
_TnLagLACPXmitStdby_Type.__name__=_F
_TnLagLACPXmitStdby_Object=MibTableColumn
tnLagLACPXmitStdby=_TnLagLACPXmitStdby_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,13),_TnLagLACPXmitStdby_Type())
tnLagLACPXmitStdby.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLACPXmitStdby.setStatus(_A)
class _TnLagLACPSelCrit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('highest-count',1),('highest-weight',2)))
_TnLagLACPSelCrit_Type.__name__=_D
_TnLagLACPSelCrit_Object=MibTableColumn
tnLagLACPSelCrit=_TnLagLACPSelCrit_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,14),_TnLagLACPSelCrit_Type())
tnLagLACPSelCrit.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLACPSelCrit.setStatus(_A)
class _TnLagLACPSelCritSlaveToPartner_Type(TruthValue):defaultValue=2
_TnLagLACPSelCritSlaveToPartner_Type.__name__=_F
_TnLagLACPSelCritSlaveToPartner_Object=MibTableColumn
tnLagLACPSelCritSlaveToPartner=_TnLagLACPSelCritSlaveToPartner_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,15),_TnLagLACPSelCritSlaveToPartner_Type())
tnLagLACPSelCritSlaveToPartner.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLACPSelCritSlaveToPartner.setStatus(_A)
_TnLagLACPNbrOfSubGroups_Type=Unsigned32
_TnLagLACPNbrOfSubGroups_Object=MibTableColumn
tnLagLACPNbrOfSubGroups=_TnLagLACPNbrOfSubGroups_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,16),_TnLagLACPNbrOfSubGroups_Type())
tnLagLACPNbrOfSubGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagLACPNbrOfSubGroups.setStatus(_A)
class _TnLagholdTimeDown_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_TnLagholdTimeDown_Type.__name__=_P
_TnLagholdTimeDown_Object=MibTableColumn
tnLagholdTimeDown=_TnLagholdTimeDown_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,17),_TnLagholdTimeDown_Type())
tnLagholdTimeDown.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagholdTimeDown.setStatus(_A)
if mibBuilder.loadTexts:tnLagholdTimeDown.setUnits('100s of milliseconds')
class _TnLagPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('hsmda',2)))
_TnLagPortType_Type.__name__=_D
_TnLagPortType_Object=MibTableColumn
tnLagPortType=_TnLagPortType_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,18),_TnLagPortType_Type())
tnLagPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagPortType.setStatus(_A)
class _TnLagPerFpIngQueuing_Type(TruthValue):defaultValue=2
_TnLagPerFpIngQueuing_Type.__name__=_F
_TnLagPerFpIngQueuing_Object=MibTableColumn
tnLagPerFpIngQueuing=_TnLagPerFpIngQueuing_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,19),_TnLagPerFpIngQueuing_Type())
tnLagPerFpIngQueuing.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagPerFpIngQueuing.setStatus(_A)
class _TnLagAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnLagAlmProfName_Type.__name__=_M
_TnLagAlmProfName_Object=MibTableColumn
tnLagAlmProfName=_TnLagAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,15,2,1,20),_TnLagAlmProfName_Type())
tnLagAlmProfName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagAlmProfName.setStatus(_A)
_TnLagOperationTable_Object=MibTable
tnLagOperationTable=_TnLagOperationTable_Object((1,3,6,1,4,1,7483,6,1,2,15,3))
if mibBuilder.loadTexts:tnLagOperationTable.setStatus(_A)
_TnLagOperationEntry_Object=MibTableRow
tnLagOperationEntry=_TnLagOperationEntry_Object((1,3,6,1,4,1,7483,6,1,2,15,3,1))
if mibBuilder.loadTexts:tnLagOperationEntry.setStatus(_A)
_TnLagIfIndex_Type=InterfaceIndexOrZero
_TnLagIfIndex_Object=MibTableColumn
tnLagIfIndex=_TnLagIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,15,3,1,1),_TnLagIfIndex_Type())
tnLagIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagIfIndex.setStatus(_A)
_TnLagConfigLastChange_Type=TimeStamp
_TnLagConfigLastChange_Object=MibTableColumn
tnLagConfigLastChange=_TnLagConfigLastChange_Object((1,3,6,1,4,1,7483,6,1,2,15,3,1,2),_TnLagConfigLastChange_Type())
tnLagConfigLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagConfigLastChange.setStatus(_A)
_TnLagPortThresholdFalling_Type=Counter32
_TnLagPortThresholdFalling_Object=MibTableColumn
tnLagPortThresholdFalling=_TnLagPortThresholdFalling_Object((1,3,6,1,4,1,7483,6,1,2,15,3,1,3),_TnLagPortThresholdFalling_Type())
tnLagPortThresholdFalling.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagPortThresholdFalling.setStatus(_A)
_TnLagPortThresholdRising_Type=Counter32
_TnLagPortThresholdRising_Object=MibTableColumn
tnLagPortThresholdRising=_TnLagPortThresholdRising_Object((1,3,6,1,4,1,7483,6,1,2,15,3,1,4),_TnLagPortThresholdRising_Type())
tnLagPortThresholdRising.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagPortThresholdRising.setStatus(_A)
_TnLagScalar1_Type=Unsigned32
_TnLagScalar1_Object=MibScalar
tnLagScalar1=_TnLagScalar1_Object((1,3,6,1,4,1,7483,6,1,2,15,4),_TnLagScalar1_Type())
tnLagScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagScalar1.setStatus(_A)
_TnLagMemberTable_Object=MibTable
tnLagMemberTable=_TnLagMemberTable_Object((1,3,6,1,4,1,7483,6,1,2,15,5))
if mibBuilder.loadTexts:tnLagMemberTable.setStatus(_A)
_TnLagMemberEntry_Object=MibTableRow
tnLagMemberEntry=_TnLagMemberEntry_Object((1,3,6,1,4,1,7483,6,1,2,15,5,1))
tnLagMemberEntry.setIndexNames((0,_H,_I),(0,_E,_J),(0,_Q,_R))
if mibBuilder.loadTexts:tnLagMemberEntry.setStatus(_A)
_TnLagMemberPortName_Type=TNamedItemOrEmpty
_TnLagMemberPortName_Object=MibTableColumn
tnLagMemberPortName=_TnLagMemberPortName_Object((1,3,6,1,4,1,7483,6,1,2,15,5,1,1),_TnLagMemberPortName_Type())
tnLagMemberPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagMemberPortName.setStatus(_A)
_TnLagMemberPortIsPrimary_Type=TruthValue
_TnLagMemberPortIsPrimary_Object=MibTableColumn
tnLagMemberPortIsPrimary=_TnLagMemberPortIsPrimary_Object((1,3,6,1,4,1,7483,6,1,2,15,5,1,2),_TnLagMemberPortIsPrimary_Type())
tnLagMemberPortIsPrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagMemberPortIsPrimary.setStatus(_A)
_TnLagPortTable_Object=MibTable
tnLagPortTable=_TnLagPortTable_Object((1,3,6,1,4,1,7483,6,1,2,15,6))
if mibBuilder.loadTexts:tnLagPortTable.setStatus(_A)
_TnLagPortEntry_Object=MibTableRow
tnLagPortEntry=_TnLagPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,15,6,1))
if mibBuilder.loadTexts:tnLagPortEntry.setStatus(_A)
class _TnLagPortSubgroup_Type(LAGSubgroup):defaultValue=1
_TnLagPortSubgroup_Type.__name__=_U
_TnLagPortSubgroup_Object=MibTableColumn
tnLagPortSubgroup=_TnLagPortSubgroup_Object((1,3,6,1,4,1,7483,6,1,2,15,6,1,1),_TnLagPortSubgroup_Type())
tnLagPortSubgroup.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagPortSubgroup.setStatus(_A)
class _TnLagPortActiveStdby_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('stand-by',2)))
_TnLagPortActiveStdby_Type.__name__=_D
_TnLagPortActiveStdby_Object=MibTableColumn
tnLagPortActiveStdby=_TnLagPortActiveStdby_Object((1,3,6,1,4,1,7483,6,1,2,15,6,1,2),_TnLagPortActiveStdby_Type())
tnLagPortActiveStdby.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagPortActiveStdby.setStatus(_A)
_TnLagConfigXTable_Object=MibTable
tnLagConfigXTable=_TnLagConfigXTable_Object((1,3,6,1,4,1,7483,6,1,2,15,7))
if mibBuilder.loadTexts:tnLagConfigXTable.setStatus(_A)
_TnLagConfigXEntry_Object=MibTableRow
tnLagConfigXEntry=_TnLagConfigXEntry_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1))
if mibBuilder.loadTexts:tnLagConfigXEntry.setStatus(_A)
_TnLagConfigXIngressAvailBandwidth_Type=Unsigned32
_TnLagConfigXIngressAvailBandwidth_Object=MibTableColumn
tnLagConfigXIngressAvailBandwidth=_TnLagConfigXIngressAvailBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,1),_TnLagConfigXIngressAvailBandwidth_Type())
tnLagConfigXIngressAvailBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagConfigXIngressAvailBandwidth.setStatus(_A)
_TnLagConfigXEgressAvailBandwidth_Type=Unsigned32
_TnLagConfigXEgressAvailBandwidth_Object=MibTableColumn
tnLagConfigXEgressAvailBandwidth=_TnLagConfigXEgressAvailBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,2),_TnLagConfigXEgressAvailBandwidth_Type())
tnLagConfigXEgressAvailBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagConfigXEgressAvailBandwidth.setStatus(_A)
class _TnLagConfigXMaxPortSize_Type(Integer32):defaultValue=4
_TnLagConfigXMaxPortSize_Type.__name__=_D
_TnLagConfigXMaxPortSize_Object=MibTableColumn
tnLagConfigXMaxPortSize=_TnLagConfigXMaxPortSize_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,3),_TnLagConfigXMaxPortSize_Type())
tnLagConfigXMaxPortSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagConfigXMaxPortSize.setStatus(_A)
_TnLagConfigXNumSelectedPorts_Type=Unsigned32
_TnLagConfigXNumSelectedPorts_Object=MibTableColumn
tnLagConfigXNumSelectedPorts=_TnLagConfigXNumSelectedPorts_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,4),_TnLagConfigXNumSelectedPorts_Type())
tnLagConfigXNumSelectedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagConfigXNumSelectedPorts.setStatus(_A)
_TnLagConfigXNumAttachedPorts_Type=Unsigned32
_TnLagConfigXNumAttachedPorts_Object=MibTableColumn
tnLagConfigXNumAttachedPorts=_TnLagConfigXNumAttachedPorts_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,5),_TnLagConfigXNumAttachedPorts_Type())
tnLagConfigXNumAttachedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagConfigXNumAttachedPorts.setStatus(_A)
_TnLagConfigXPrimaryPort_Type=InterfaceIndex
_TnLagConfigXPrimaryPort_Object=MibTableColumn
tnLagConfigXPrimaryPort=_TnLagConfigXPrimaryPort_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,6),_TnLagConfigXPrimaryPort_Type())
tnLagConfigXPrimaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagConfigXPrimaryPort.setStatus(_A)
class _TnLagAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_TnLagAdminState_Type.__name__=_D
_TnLagAdminState_Object=MibTableColumn
tnLagAdminState=_TnLagAdminState_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,7),_TnLagAdminState_Type())
tnLagAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagAdminState.setStatus(_A)
class _TnLagLPTConsequenceAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAction',1),('oneShutDown',2),('allShutDown',3)))
_TnLagLPTConsequenceAction_Type.__name__=_D
_TnLagLPTConsequenceAction_Object=MibTableColumn
tnLagLPTConsequenceAction=_TnLagLPTConsequenceAction_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,8),_TnLagLPTConsequenceAction_Type())
tnLagLPTConsequenceAction.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLPTConsequenceAction.setStatus(_A)
class _TnLagLosProp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('laserOn',1),('laserOff',2)))
_TnLagLosProp_Type.__name__=_D
_TnLagLosProp_Object=MibTableColumn
tnLagLosProp=_TnLagLosProp_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,9),_TnLagLosProp_Type())
tnLagLosProp.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagLosProp.setStatus(_A)
class _TnLagTPID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('qinqtpid1',1),('qinqtpid2',2),('qinqtpid3',3),('qinqtpid4',4)))
_TnLagTPID_Type.__name__=_D
_TnLagTPID_Object=MibTableColumn
tnLagTPID=_TnLagTPID_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,10),_TnLagTPID_Type())
tnLagTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagTPID.setStatus(_A)
class _TnLagMtu_Type(Integer32):defaultValue=9600
_TnLagMtu_Type.__name__=_D
_TnLagMtu_Object=MibTableColumn
tnLagMtu=_TnLagMtu_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,11),_TnLagMtu_Type())
tnLagMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLagMtu.setStatus(_A)
_TnLagSpeed_Type=Gauge32
_TnLagSpeed_Object=MibTableColumn
tnLagSpeed=_TnLagSpeed_Object((1,3,6,1,4,1,7483,6,1,2,15,7,1,12),_TnLagSpeed_Type())
tnLagSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagSpeed.setStatus(_A)
_TnLagCommandTable_Object=MibTable
tnLagCommandTable=_TnLagCommandTable_Object((1,3,6,1,4,1,7483,6,1,2,15,20))
if mibBuilder.loadTexts:tnLagCommandTable.setStatus(_A)
_TnLagCommandEntry_Object=MibTableRow
tnLagCommandEntry=_TnLagCommandEntry_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1))
tnLagCommandEntry.setIndexNames((0,_H,_I),(0,_E,_J),(0,_E,_V))
if mibBuilder.loadTexts:tnLagCommandEntry.setStatus(_A)
_TnLagSubgroup_Type=LAGSubgroup
_TnLagSubgroup_Object=MibTableColumn
tnLagSubgroup=_TnLagSubgroup_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1,1),_TnLagSubgroup_Type())
tnLagSubgroup.setMaxAccess(_T)
if mibBuilder.loadTexts:tnLagSubgroup.setStatus(_A)
class _TnLagCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noCmd',0),('clearForce',1),('force',2)))
_TnLagCommand_Type.__name__=_D
_TnLagCommand_Object=MibTableColumn
tnLagCommand=_TnLagCommand_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1,2),_TnLagCommand_Type())
tnLagCommand.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagCommand.setStatus(_A)
class _TnLagCommandActiveStdby_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('standby',2)))
_TnLagCommandActiveStdby_Type.__name__=_D
_TnLagCommandActiveStdby_Object=MibTableColumn
tnLagCommandActiveStdby=_TnLagCommandActiveStdby_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1,3),_TnLagCommandActiveStdby_Type())
tnLagCommandActiveStdby.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagCommandActiveStdby.setStatus(_A)
class _TnLagCommandAllMc_Type(TruthValue):defaultValue=2
_TnLagCommandAllMc_Type.__name__=_F
_TnLagCommandAllMc_Object=MibTableColumn
tnLagCommandAllMc=_TnLagCommandAllMc_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1,4),_TnLagCommandAllMc_Type())
tnLagCommandAllMc.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagCommandAllMc.setStatus(_A)
class _TnLagCommandMcPeerIpType_Type(InetAddressType):defaultValue=1
_TnLagCommandMcPeerIpType_Type.__name__=_O
_TnLagCommandMcPeerIpType_Object=MibTableColumn
tnLagCommandMcPeerIpType=_TnLagCommandMcPeerIpType_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1,5),_TnLagCommandMcPeerIpType_Type())
tnLagCommandMcPeerIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagCommandMcPeerIpType.setStatus(_A)
class _TnLagCommandMcPeerIpAddr_Type(InetAddress):defaultValue=OctetString('');subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_TnLagCommandMcPeerIpAddr_Type.__name__=_N
_TnLagCommandMcPeerIpAddr_Object=MibTableColumn
tnLagCommandMcPeerIpAddr=_TnLagCommandMcPeerIpAddr_Object((1,3,6,1,4,1,7483,6,1,2,15,20,1,6),_TnLagCommandMcPeerIpAddr_Type())
tnLagCommandMcPeerIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:tnLagCommandMcPeerIpAddr.setStatus(_A)
_TnLagScalar2_Type=Unsigned32
_TnLagScalar2_Object=MibScalar
tnLagScalar2=_TnLagScalar2_Object((1,3,6,1,4,1,7483,6,1,2,15,101),_TnLagScalar2_Type())
tnLagScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagScalar2.setStatus(_A)
_TnLagScalar3_Type=Unsigned32
_TnLagScalar3_Object=MibScalar
tnLagScalar3=_TnLagScalar3_Object((1,3,6,1,4,1,7483,6,1,2,15,102),_TnLagScalar3_Type())
tnLagScalar3.setMaxAccess(_C)
if mibBuilder.loadTexts:tnLagScalar3.setStatus(_A)
_TnLagNotifyPrefix_ObjectIdentity=ObjectIdentity
tnLagNotifyPrefix=_TnLagNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,15))
_TnLagNotifications_ObjectIdentity=ObjectIdentity
tnLagNotifications=_TnLagNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,15,0))
tnLagConfigEntry.registerAugmentions((_E,_W))
tnLagOperationEntry.setIndexNames(*tnLagConfigEntry.getIndexNames())
dot3adAggPortEntry.registerAugmentions((_E,_X))
tnLagPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
tnLagConfigEntry.registerAugmentions((_E,_Y))
tnLagConfigXEntry.setIndexNames(*tnLagConfigEntry.getIndexNames())
tnLagDynamicCostOn=NotificationType((1,3,6,1,4,1,7483,6,1,3,15,0,1))
tnLagDynamicCostOn.setObjects((_E,_L))
if mibBuilder.loadTexts:tnLagDynamicCostOn.setStatus(_A)
tnLagDynamicCostOff=NotificationType((1,3,6,1,4,1,7483,6,1,3,15,0,2))
tnLagDynamicCostOff.setObjects((_E,_L))
if mibBuilder.loadTexts:tnLagDynamicCostOff.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'LAGInterfaceNumber':LAGInterfaceNumber,_U:LAGSubgroup,'tnLagMIBModule':tnLagMIBModule,'tnLagObjects':tnLagObjects,'tnLagConfigTable':tnLagConfigTable,'tnLagConfigEntry':tnLagConfigEntry,_J:tnLagIndex,'tnLagRowStatus':tnLagRowStatus,_L:tnLagPortThreshold,'tnLagPortThresholdAction':tnLagPortThresholdAction,'tnLagEnableMarkerGenerator':tnLagEnableMarkerGenerator,'tnLagEnableLACP':tnLagEnableLACP,'tnLagDescription':tnLagDescription,'tnLagDynamicCosting':tnLagDynamicCosting,'tnLagLACPMode':tnLagLACPMode,'tnLagLACPAdminKeyAutogen':tnLagLACPAdminKeyAutogen,'tnLagLACPTransmitInterval':tnLagLACPTransmitInterval,'tnLagAccessAdaptQos':tnLagAccessAdaptQos,'tnLagLACPXmitStdby':tnLagLACPXmitStdby,'tnLagLACPSelCrit':tnLagLACPSelCrit,'tnLagLACPSelCritSlaveToPartner':tnLagLACPSelCritSlaveToPartner,'tnLagLACPNbrOfSubGroups':tnLagLACPNbrOfSubGroups,'tnLagholdTimeDown':tnLagholdTimeDown,'tnLagPortType':tnLagPortType,'tnLagPerFpIngQueuing':tnLagPerFpIngQueuing,'tnLagAlmProfName':tnLagAlmProfName,'tnLagOperationTable':tnLagOperationTable,_W:tnLagOperationEntry,'tnLagIfIndex':tnLagIfIndex,'tnLagConfigLastChange':tnLagConfigLastChange,'tnLagPortThresholdFalling':tnLagPortThresholdFalling,'tnLagPortThresholdRising':tnLagPortThresholdRising,'tnLagScalar1':tnLagScalar1,'tnLagMemberTable':tnLagMemberTable,'tnLagMemberEntry':tnLagMemberEntry,'tnLagMemberPortName':tnLagMemberPortName,'tnLagMemberPortIsPrimary':tnLagMemberPortIsPrimary,'tnLagPortTable':tnLagPortTable,_X:tnLagPortEntry,'tnLagPortSubgroup':tnLagPortSubgroup,'tnLagPortActiveStdby':tnLagPortActiveStdby,'tnLagConfigXTable':tnLagConfigXTable,_Y:tnLagConfigXEntry,'tnLagConfigXIngressAvailBandwidth':tnLagConfigXIngressAvailBandwidth,'tnLagConfigXEgressAvailBandwidth':tnLagConfigXEgressAvailBandwidth,'tnLagConfigXMaxPortSize':tnLagConfigXMaxPortSize,'tnLagConfigXNumSelectedPorts':tnLagConfigXNumSelectedPorts,'tnLagConfigXNumAttachedPorts':tnLagConfigXNumAttachedPorts,'tnLagConfigXPrimaryPort':tnLagConfigXPrimaryPort,'tnLagAdminState':tnLagAdminState,'tnLagLPTConsequenceAction':tnLagLPTConsequenceAction,'tnLagLosProp':tnLagLosProp,'tnLagTPID':tnLagTPID,'tnLagMtu':tnLagMtu,'tnLagSpeed':tnLagSpeed,'tnLagCommandTable':tnLagCommandTable,'tnLagCommandEntry':tnLagCommandEntry,_V:tnLagSubgroup,'tnLagCommand':tnLagCommand,'tnLagCommandActiveStdby':tnLagCommandActiveStdby,'tnLagCommandAllMc':tnLagCommandAllMc,'tnLagCommandMcPeerIpType':tnLagCommandMcPeerIpType,'tnLagCommandMcPeerIpAddr':tnLagCommandMcPeerIpAddr,'tnLagScalar2':tnLagScalar2,'tnLagScalar3':tnLagScalar3,'tnLagNotifyPrefix':tnLagNotifyPrefix,'tnLagNotifications':tnLagNotifications,'tnLagDynamicCostOn':tnLagDynamicCostOn,'tnLagDynamicCostOff':tnLagDynamicCostOff})