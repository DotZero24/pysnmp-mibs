_R='raisecomApsStatus'
_Q='physical-link'
_P='raisecomApsFdLink'
_O='raisecomApsAssociationName'
_N='normal-traffic-signal'
_M='raisecomApsStatisticsLastDfop'
_L='not-accessible'
_K='EnableVar'
_J='raisecomApsId'
_I='TruthValue'
_H='read-write'
_G='RAISECOM-APS-MIB'
_F='Unsigned32'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
EnableVar,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_K,'Vlanset')
raisecomAps=ModuleIdentity((1,3,6,1,4,1,8886,1,37))
_RaisecomApsBaseGroup_ObjectIdentity=ObjectIdentity
raisecomApsBaseGroup=_RaisecomApsBaseGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,37,1))
class _RaisecomApsTrapEnable_Type(EnableVar):defaultValue=2
_RaisecomApsTrapEnable_Type.__name__=_K
_RaisecomApsTrapEnable_Object=MibScalar
raisecomApsTrapEnable=_RaisecomApsTrapEnable_Object((1,3,6,1,4,1,8886,1,37,1,1),_RaisecomApsTrapEnable_Type())
raisecomApsTrapEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsTrapEnable.setStatus(_A)
_RaisecomApsCfgTable_Object=MibTable
raisecomApsCfgTable=_RaisecomApsCfgTable_Object((1,3,6,1,4,1,8886,1,37,1,2))
if mibBuilder.loadTexts:raisecomApsCfgTable.setStatus(_A)
_RaisecomApsCfgEntry_Object=MibTableRow
raisecomApsCfgEntry=_RaisecomApsCfgEntry_Object((1,3,6,1,4,1,8886,1,37,1,2,1))
raisecomApsCfgEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:raisecomApsCfgEntry.setStatus(_A)
class _RaisecomApsId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_RaisecomApsId_Type.__name__=_F
_RaisecomApsId_Object=MibTableColumn
raisecomApsId=_RaisecomApsId_Object((1,3,6,1,4,1,8886,1,37,1,2,1,1),_RaisecomApsId_Type())
raisecomApsId.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomApsId.setStatus(_A)
class _RaisecomApsName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomApsName_Type.__name__=_E
_RaisecomApsName_Object=MibTableColumn
raisecomApsName=_RaisecomApsName_Object((1,3,6,1,4,1,8886,1,37,1,2,1,2),_RaisecomApsName_Type())
raisecomApsName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsName.setStatus(_A)
class _RaisecomApsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ether-aps',1),('mpls-aps',2)))
_RaisecomApsType_Type.__name__=_C
_RaisecomApsType_Object=MibTableColumn
raisecomApsType=_RaisecomApsType_Object((1,3,6,1,4,1,8886,1,37,1,2,1,3),_RaisecomApsType_Type())
raisecomApsType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsType.setStatus(_A)
_RaisecomApsWorkingPort_Type=Integer32
_RaisecomApsWorkingPort_Object=MibTableColumn
raisecomApsWorkingPort=_RaisecomApsWorkingPort_Object((1,3,6,1,4,1,8886,1,37,1,2,1,4),_RaisecomApsWorkingPort_Type())
raisecomApsWorkingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsWorkingPort.setStatus(_A)
_RaisecomApsWorkingBlockVlanlist_Type=Vlanset
_RaisecomApsWorkingBlockVlanlist_Object=MibTableColumn
raisecomApsWorkingBlockVlanlist=_RaisecomApsWorkingBlockVlanlist_Object((1,3,6,1,4,1,8886,1,37,1,2,1,5),_RaisecomApsWorkingBlockVlanlist_Type())
raisecomApsWorkingBlockVlanlist.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsWorkingBlockVlanlist.setStatus(_A)
_RaisecomApsProtectionPort_Type=Integer32
_RaisecomApsProtectionPort_Object=MibTableColumn
raisecomApsProtectionPort=_RaisecomApsProtectionPort_Object((1,3,6,1,4,1,8886,1,37,1,2,1,6),_RaisecomApsProtectionPort_Type())
raisecomApsProtectionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsProtectionPort.setStatus(_A)
_RaisecomApsProtectionBlockVlanlist_Type=Vlanset
_RaisecomApsProtectionBlockVlanlist_Object=MibTableColumn
raisecomApsProtectionBlockVlanlist=_RaisecomApsProtectionBlockVlanlist_Object((1,3,6,1,4,1,8886,1,37,1,2,1,7),_RaisecomApsProtectionBlockVlanlist_Type())
raisecomApsProtectionBlockVlanlist.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsProtectionBlockVlanlist.setStatus(_A)
class _RaisecomApsWorkingIngressAssociation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomApsWorkingIngressAssociation_Type.__name__=_E
_RaisecomApsWorkingIngressAssociation_Object=MibTableColumn
raisecomApsWorkingIngressAssociation=_RaisecomApsWorkingIngressAssociation_Object((1,3,6,1,4,1,8886,1,37,1,2,1,8),_RaisecomApsWorkingIngressAssociation_Type())
raisecomApsWorkingIngressAssociation.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsWorkingIngressAssociation.setStatus(_A)
class _RaisecomApsWorkingEgressAssociation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomApsWorkingEgressAssociation_Type.__name__=_E
_RaisecomApsWorkingEgressAssociation_Object=MibTableColumn
raisecomApsWorkingEgressAssociation=_RaisecomApsWorkingEgressAssociation_Object((1,3,6,1,4,1,8886,1,37,1,2,1,9),_RaisecomApsWorkingEgressAssociation_Type())
raisecomApsWorkingEgressAssociation.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsWorkingEgressAssociation.setStatus(_A)
class _RaisecomApsProtectionIngressAssociation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomApsProtectionIngressAssociation_Type.__name__=_E
_RaisecomApsProtectionIngressAssociation_Object=MibTableColumn
raisecomApsProtectionIngressAssociation=_RaisecomApsProtectionIngressAssociation_Object((1,3,6,1,4,1,8886,1,37,1,2,1,10),_RaisecomApsProtectionIngressAssociation_Type())
raisecomApsProtectionIngressAssociation.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsProtectionIngressAssociation.setStatus(_A)
class _RaisecomApsProtectionEgressAssociation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomApsProtectionEgressAssociation_Type.__name__=_E
_RaisecomApsProtectionEgressAssociation_Object=MibTableColumn
raisecomApsProtectionEgressAssociation=_RaisecomApsProtectionEgressAssociation_Object((1,3,6,1,4,1,8886,1,37,1,2,1,11),_RaisecomApsProtectionEgressAssociation_Type())
raisecomApsProtectionEgressAssociation.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsProtectionEgressAssociation.setStatus(_A)
class _RaisecomApsProtectionTypeAdmin_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RaisecomApsProtectionTypeAdmin_Type.__name__=_F
_RaisecomApsProtectionTypeAdmin_Object=MibTableColumn
raisecomApsProtectionTypeAdmin=_RaisecomApsProtectionTypeAdmin_Object((1,3,6,1,4,1,8886,1,37,1,2,1,12),_RaisecomApsProtectionTypeAdmin_Type())
raisecomApsProtectionTypeAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsProtectionTypeAdmin.setStatus(_A)
class _RaisecomApsProtectionTypeOper_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RaisecomApsProtectionTypeOper_Type.__name__=_F
_RaisecomApsProtectionTypeOper_Object=MibTableColumn
raisecomApsProtectionTypeOper=_RaisecomApsProtectionTypeOper_Object((1,3,6,1,4,1,8886,1,37,1,2,1,13),_RaisecomApsProtectionTypeOper_Type())
raisecomApsProtectionTypeOper.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsProtectionTypeOper.setStatus(_A)
class _RaisecomApsForceSwitch_Type(TruthValue):defaultValue=2
_RaisecomApsForceSwitch_Type.__name__=_I
_RaisecomApsForceSwitch_Object=MibTableColumn
raisecomApsForceSwitch=_RaisecomApsForceSwitch_Object((1,3,6,1,4,1,8886,1,37,1,2,1,14),_RaisecomApsForceSwitch_Type())
raisecomApsForceSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsForceSwitch.setStatus(_A)
class _RaisecomApsManualSwitch_Type(TruthValue):defaultValue=2
_RaisecomApsManualSwitch_Type.__name__=_I
_RaisecomApsManualSwitch_Object=MibTableColumn
raisecomApsManualSwitch=_RaisecomApsManualSwitch_Object((1,3,6,1,4,1,8886,1,37,1,2,1,15),_RaisecomApsManualSwitch_Type())
raisecomApsManualSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsManualSwitch.setStatus(_A)
class _RaisecomApsManualSwitchtoWork_Type(TruthValue):defaultValue=2
_RaisecomApsManualSwitchtoWork_Type.__name__=_I
_RaisecomApsManualSwitchtoWork_Object=MibTableColumn
raisecomApsManualSwitchtoWork=_RaisecomApsManualSwitchtoWork_Object((1,3,6,1,4,1,8886,1,37,1,2,1,16),_RaisecomApsManualSwitchtoWork_Type())
raisecomApsManualSwitchtoWork.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsManualSwitchtoWork.setStatus(_A)
class _RaisecomApsLockout_Type(TruthValue):defaultValue=2
_RaisecomApsLockout_Type.__name__=_I
_RaisecomApsLockout_Object=MibTableColumn
raisecomApsLockout=_RaisecomApsLockout_Object((1,3,6,1,4,1,8886,1,37,1,2,1,17),_RaisecomApsLockout_Type())
raisecomApsLockout.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsLockout.setStatus(_A)
class _RaisecomApsClear_Type(EnableVar):defaultValue=2
_RaisecomApsClear_Type.__name__=_K
_RaisecomApsClear_Object=MibTableColumn
raisecomApsClear=_RaisecomApsClear_Object((1,3,6,1,4,1,8886,1,37,1,2,1,18),_RaisecomApsClear_Type())
raisecomApsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsClear.setStatus(_A)
class _RaisecomApsWtrTimer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_RaisecomApsWtrTimer_Type.__name__=_F
_RaisecomApsWtrTimer_Object=MibTableColumn
raisecomApsWtrTimer=_RaisecomApsWtrTimer_Object((1,3,6,1,4,1,8886,1,37,1,2,1,19),_RaisecomApsWtrTimer_Type())
raisecomApsWtrTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsWtrTimer.setStatus(_A)
class _RaisecomApsHoldOffTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RaisecomApsHoldOffTimer_Type.__name__=_F
_RaisecomApsHoldOffTimer_Object=MibTableColumn
raisecomApsHoldOffTimer=_RaisecomApsHoldOffTimer_Object((1,3,6,1,4,1,8886,1,37,1,2,1,20),_RaisecomApsHoldOffTimer_Type())
raisecomApsHoldOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsHoldOffTimer.setStatus(_A)
class _RaisecomApsProtocolVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomApsProtocolVlan_Type.__name__=_C
_RaisecomApsProtocolVlan_Object=MibTableColumn
raisecomApsProtocolVlan=_RaisecomApsProtocolVlan_Object((1,3,6,1,4,1,8886,1,37,1,2,1,21),_RaisecomApsProtocolVlan_Type())
raisecomApsProtocolVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsProtocolVlan.setStatus(_A)
class _RaisecomApsStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('nr-w',1),('nr-p',2),('lo',3),('fs',4),('sf-w',5),('sf-p',6),('ms',7),('ms-w',8),('wtr',9),('dnr',10)))
_RaisecomApsStatus_Type.__name__=_C
_RaisecomApsStatus_Object=MibTableColumn
raisecomApsStatus=_RaisecomApsStatus_Object((1,3,6,1,4,1,8886,1,37,1,2,1,22),_RaisecomApsStatus_Type())
raisecomApsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatus.setStatus(_A)
class _RaisecomApsDfopStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('dFOP-CM',2),('dFOP-PM',3),('dFOP-NR',4)))
_RaisecomApsDfopStatus_Type.__name__=_C
_RaisecomApsDfopStatus_Object=MibTableColumn
raisecomApsDfopStatus=_RaisecomApsDfopStatus_Object((1,3,6,1,4,1,8886,1,37,1,2,1,23),_RaisecomApsDfopStatus_Type())
raisecomApsDfopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsDfopStatus.setStatus(_A)
_RaisecomApsRowStatus_Type=RowStatus
_RaisecomApsRowStatus_Object=MibTableColumn
raisecomApsRowStatus=_RaisecomApsRowStatus_Object((1,3,6,1,4,1,8886,1,37,1,2,1,24),_RaisecomApsRowStatus_Type())
raisecomApsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsRowStatus.setStatus(_A)
_RaisecomApsStatisticsTable_Object=MibTable
raisecomApsStatisticsTable=_RaisecomApsStatisticsTable_Object((1,3,6,1,4,1,8886,1,37,1,3))
if mibBuilder.loadTexts:raisecomApsStatisticsTable.setStatus(_A)
_RaisecomApsStatisticsEntry_Object=MibTableRow
raisecomApsStatisticsEntry=_RaisecomApsStatisticsEntry_Object((1,3,6,1,4,1,8886,1,37,1,3,1))
raisecomApsStatisticsEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:raisecomApsStatisticsEntry.setStatus(_A)
class _RaisecomApsStatisticsSwitchCounts_Type(Unsigned32):defaultValue=0
_RaisecomApsStatisticsSwitchCounts_Type.__name__=_F
_RaisecomApsStatisticsSwitchCounts_Object=MibTableColumn
raisecomApsStatisticsSwitchCounts=_RaisecomApsStatisticsSwitchCounts_Object((1,3,6,1,4,1,8886,1,37,1,3,1,1),_RaisecomApsStatisticsSwitchCounts_Type())
raisecomApsStatisticsSwitchCounts.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatisticsSwitchCounts.setStatus(_A)
class _RaisecomApsStatisticsApsTx_Type(Unsigned32):defaultValue=0
_RaisecomApsStatisticsApsTx_Type.__name__=_F
_RaisecomApsStatisticsApsTx_Object=MibTableColumn
raisecomApsStatisticsApsTx=_RaisecomApsStatisticsApsTx_Object((1,3,6,1,4,1,8886,1,37,1,3,1,2),_RaisecomApsStatisticsApsTx_Type())
raisecomApsStatisticsApsTx.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatisticsApsTx.setStatus(_A)
class _RaisecomApsStatisticsApsRx_Type(Unsigned32):defaultValue=0
_RaisecomApsStatisticsApsRx_Type.__name__=_F
_RaisecomApsStatisticsApsRx_Object=MibTableColumn
raisecomApsStatisticsApsRx=_RaisecomApsStatisticsApsRx_Object((1,3,6,1,4,1,8886,1,37,1,3,1,3),_RaisecomApsStatisticsApsRx_Type())
raisecomApsStatisticsApsRx.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatisticsApsRx.setStatus(_A)
_RaisecomApsStatisticsLastStatusOccur_Type=TimeTicks
_RaisecomApsStatisticsLastStatusOccur_Object=MibTableColumn
raisecomApsStatisticsLastStatusOccur=_RaisecomApsStatisticsLastStatusOccur_Object((1,3,6,1,4,1,8886,1,37,1,3,1,4),_RaisecomApsStatisticsLastStatusOccur_Type())
raisecomApsStatisticsLastStatusOccur.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatisticsLastStatusOccur.setStatus(_A)
_RaisecomApsStatisticsLastSwitchOccur_Type=TimeTicks
_RaisecomApsStatisticsLastSwitchOccur_Object=MibTableColumn
raisecomApsStatisticsLastSwitchOccur=_RaisecomApsStatisticsLastSwitchOccur_Object((1,3,6,1,4,1,8886,1,37,1,3,1,5),_RaisecomApsStatisticsLastSwitchOccur_Type())
raisecomApsStatisticsLastSwitchOccur.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatisticsLastSwitchOccur.setStatus(_A)
_RaisecomApsStatisticsLastDfop_Type=TimeTicks
_RaisecomApsStatisticsLastDfop_Object=MibTableColumn
raisecomApsStatisticsLastDfop=_RaisecomApsStatisticsLastDfop_Object((1,3,6,1,4,1,8886,1,37,1,3,1,6),_RaisecomApsStatisticsLastDfop_Type())
raisecomApsStatisticsLastDfop.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsStatisticsLastDfop.setStatus(_A)
class _RaisecomApsStatisticsClear_Type(EnableVar):defaultValue=2
_RaisecomApsStatisticsClear_Type.__name__=_K
_RaisecomApsStatisticsClear_Object=MibTableColumn
raisecomApsStatisticsClear=_RaisecomApsStatisticsClear_Object((1,3,6,1,4,1,8886,1,37,1,3,1,7),_RaisecomApsStatisticsClear_Type())
raisecomApsStatisticsClear.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsStatisticsClear.setStatus(_A)
_RaisecomApsPeerTable_Object=MibTable
raisecomApsPeerTable=_RaisecomApsPeerTable_Object((1,3,6,1,4,1,8886,1,37,1,4))
if mibBuilder.loadTexts:raisecomApsPeerTable.setStatus(_A)
_RaisecomApsPeerEntry_Object=MibTableRow
raisecomApsPeerEntry=_RaisecomApsPeerEntry_Object((1,3,6,1,4,1,8886,1,37,1,4,1))
raisecomApsPeerEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:raisecomApsPeerEntry.setStatus(_A)
class _RaisecomApsPeerProtectionType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RaisecomApsPeerProtectionType_Type.__name__=_F
_RaisecomApsPeerProtectionType_Object=MibTableColumn
raisecomApsPeerProtectionType=_RaisecomApsPeerProtectionType_Object((1,3,6,1,4,1,8886,1,37,1,4,1,1),_RaisecomApsPeerProtectionType_Type())
raisecomApsPeerProtectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsPeerProtectionType.setStatus(_A)
class _RaisecomApsPeerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('nr-w',1),('nr-p',2),('lo',3),('fs',4),('sf-w',5),('sf-p',6),('ms',7),('ms-w',8),('wtr',9),('dnr',10),('sd',11),('exer',12),('rr',13)))
_RaisecomApsPeerStatus_Type.__name__=_C
_RaisecomApsPeerStatus_Object=MibTableColumn
raisecomApsPeerStatus=_RaisecomApsPeerStatus_Object((1,3,6,1,4,1,8886,1,37,1,4,1,2),_RaisecomApsPeerStatus_Type())
raisecomApsPeerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsPeerStatus.setStatus(_A)
class _RaisecomApsRequestSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('null',0),(_N,1)))
_RaisecomApsRequestSignal_Type.__name__=_C
_RaisecomApsRequestSignal_Object=MibTableColumn
raisecomApsRequestSignal=_RaisecomApsRequestSignal_Object((1,3,6,1,4,1,8886,1,37,1,4,1,3),_RaisecomApsRequestSignal_Type())
raisecomApsRequestSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsRequestSignal.setStatus(_A)
class _RaisecomApsBridgedSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('null',0),(_N,1)))
_RaisecomApsBridgedSignal_Type.__name__=_C
_RaisecomApsBridgedSignal_Object=MibTableColumn
raisecomApsBridgedSignal=_RaisecomApsBridgedSignal_Object((1,3,6,1,4,1,8886,1,37,1,4,1,4),_RaisecomApsBridgedSignal_Type())
raisecomApsBridgedSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsBridgedSignal.setStatus(_A)
_RaisecomApsAssociationGroup_ObjectIdentity=ObjectIdentity
raisecomApsAssociationGroup=_RaisecomApsAssociationGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,37,2))
_RaisecomApsAssociationTable_Object=MibTable
raisecomApsAssociationTable=_RaisecomApsAssociationTable_Object((1,3,6,1,4,1,8886,1,37,2,1))
if mibBuilder.loadTexts:raisecomApsAssociationTable.setStatus(_A)
_RaisecomApsAssociationEntry_Object=MibTableRow
raisecomApsAssociationEntry=_RaisecomApsAssociationEntry_Object((1,3,6,1,4,1,8886,1,37,2,1,1))
raisecomApsAssociationEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:raisecomApsAssociationEntry.setStatus(_A)
class _RaisecomApsAssociationName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RaisecomApsAssociationName_Type.__name__=_E
_RaisecomApsAssociationName_Object=MibTableColumn
raisecomApsAssociationName=_RaisecomApsAssociationName_Object((1,3,6,1,4,1,8886,1,37,2,1,1,1),_RaisecomApsAssociationName_Type())
raisecomApsAssociationName.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomApsAssociationName.setStatus(_A)
class _RaisecomApsAssociationMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RaisecomApsAssociationMdName_Type.__name__=_E
_RaisecomApsAssociationMdName_Object=MibTableColumn
raisecomApsAssociationMdName=_RaisecomApsAssociationMdName_Object((1,3,6,1,4,1,8886,1,37,2,1,1,2),_RaisecomApsAssociationMdName_Type())
raisecomApsAssociationMdName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsAssociationMdName.setStatus(_A)
_RaisecomApsAssociationMdLevel_Type=Integer32
_RaisecomApsAssociationMdLevel_Object=MibTableColumn
raisecomApsAssociationMdLevel=_RaisecomApsAssociationMdLevel_Object((1,3,6,1,4,1,8886,1,37,2,1,1,3),_RaisecomApsAssociationMdLevel_Type())
raisecomApsAssociationMdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsAssociationMdLevel.setStatus(_A)
class _RaisecomApsAssociationMaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_RaisecomApsAssociationMaName_Type.__name__=_E
_RaisecomApsAssociationMaName_Object=MibTableColumn
raisecomApsAssociationMaName=_RaisecomApsAssociationMaName_Object((1,3,6,1,4,1,8886,1,37,2,1,1,4),_RaisecomApsAssociationMaName_Type())
raisecomApsAssociationMaName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsAssociationMaName.setStatus(_A)
_RaisecomApsAssociationRowStatus_Type=RowStatus
_RaisecomApsAssociationRowStatus_Object=MibTableColumn
raisecomApsAssociationRowStatus=_RaisecomApsAssociationRowStatus_Object((1,3,6,1,4,1,8886,1,37,2,1,1,5),_RaisecomApsAssociationRowStatus_Type())
raisecomApsAssociationRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomApsAssociationRowStatus.setStatus(_A)
_RaisecomApsFailureDetGroup_ObjectIdentity=ObjectIdentity
raisecomApsFailureDetGroup=_RaisecomApsFailureDetGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,37,3))
_RaisecomApsFailureDetTable_Object=MibTable
raisecomApsFailureDetTable=_RaisecomApsFailureDetTable_Object((1,3,6,1,4,1,8886,1,37,3,1))
if mibBuilder.loadTexts:raisecomApsFailureDetTable.setStatus(_A)
_RaisecomApsFailureDetEntry_Object=MibTableRow
raisecomApsFailureDetEntry=_RaisecomApsFailureDetEntry_Object((1,3,6,1,4,1,8886,1,37,3,1,1))
raisecomApsFailureDetEntry.setIndexNames((0,_G,_J),(0,_G,_P))
if mibBuilder.loadTexts:raisecomApsFailureDetEntry.setStatus(_A)
class _RaisecomApsFdLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('working',1),('protection',2)))
_RaisecomApsFdLink_Type.__name__=_C
_RaisecomApsFdLink_Object=MibTableColumn
raisecomApsFdLink=_RaisecomApsFdLink_Object((1,3,6,1,4,1,8886,1,37,3,1,1,1),_RaisecomApsFdLink_Type())
raisecomApsFdLink.setMaxAccess(_L)
if mibBuilder.loadTexts:raisecomApsFdLink.setStatus(_A)
class _RaisecomApsFdType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('cc',2),('both',3)))
_RaisecomApsFdType_Type.__name__=_C
_RaisecomApsFdType_Object=MibTableColumn
raisecomApsFdType=_RaisecomApsFdType_Object((1,3,6,1,4,1,8886,1,37,3,1,1,2),_RaisecomApsFdType_Type())
raisecomApsFdType.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsFdType.setStatus(_A)
class _RaisecomApsFdLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('sf',2)))
_RaisecomApsFdLinkStatus_Type.__name__=_C
_RaisecomApsFdLinkStatus_Object=MibTableColumn
raisecomApsFdLinkStatus=_RaisecomApsFdLinkStatus_Object((1,3,6,1,4,1,8886,1,37,3,1,1,3),_RaisecomApsFdLinkStatus_Type())
raisecomApsFdLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsFdLinkStatus.setStatus(_A)
class _RaisecomApsFdSfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_Q,2),('cc',3),('both',4)))
_RaisecomApsFdSfType_Type.__name__=_C
_RaisecomApsFdSfType_Object=MibTableColumn
raisecomApsFdSfType=_RaisecomApsFdSfType_Object((1,3,6,1,4,1,8886,1,37,3,1,1,4),_RaisecomApsFdSfType_Type())
raisecomApsFdSfType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomApsFdSfType.setStatus(_A)
class _RaisecomApsFdMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RaisecomApsFdMdName_Type.__name__=_E
_RaisecomApsFdMdName_Object=MibTableColumn
raisecomApsFdMdName=_RaisecomApsFdMdName_Object((1,3,6,1,4,1,8886,1,37,3,1,1,5),_RaisecomApsFdMdName_Type())
raisecomApsFdMdName.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsFdMdName.setStatus(_A)
class _RaisecomApsFdMaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_RaisecomApsFdMaName_Type.__name__=_E
_RaisecomApsFdMaName_Object=MibTableColumn
raisecomApsFdMaName=_RaisecomApsFdMaName_Object((1,3,6,1,4,1,8886,1,37,3,1,1,6),_RaisecomApsFdMaName_Type())
raisecomApsFdMaName.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsFdMaName.setStatus(_A)
class _RaisecomApsFdLocalMep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_RaisecomApsFdLocalMep_Type.__name__=_C
_RaisecomApsFdLocalMep_Object=MibTableColumn
raisecomApsFdLocalMep=_RaisecomApsFdLocalMep_Object((1,3,6,1,4,1,8886,1,37,3,1,1,7),_RaisecomApsFdLocalMep_Type())
raisecomApsFdLocalMep.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsFdLocalMep.setStatus(_A)
class _RaisecomApsFdRemoteMep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_RaisecomApsFdRemoteMep_Type.__name__=_C
_RaisecomApsFdRemoteMep_Object=MibTableColumn
raisecomApsFdRemoteMep=_RaisecomApsFdRemoteMep_Object((1,3,6,1,4,1,8886,1,37,3,1,1,8),_RaisecomApsFdRemoteMep_Type())
raisecomApsFdRemoteMep.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsFdRemoteMep.setStatus(_A)
class _RaisecomApsMdLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomApsMdLevel_Type.__name__=_C
_RaisecomApsMdLevel_Object=MibTableColumn
raisecomApsMdLevel=_RaisecomApsMdLevel_Object((1,3,6,1,4,1,8886,1,37,3,1,1,9),_RaisecomApsMdLevel_Type())
raisecomApsMdLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomApsMdLevel.setStatus(_A)
_RaisecomApsNotifications_ObjectIdentity=ObjectIdentity
raisecomApsNotifications=_RaisecomApsNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,37,4))
raisecomApsDfopTrap=NotificationType((1,3,6,1,4,1,8886,1,37,4,1))
raisecomApsDfopTrap.setObjects((_G,_M))
if mibBuilder.loadTexts:raisecomApsDfopTrap.setStatus(_A)
raisecomApsDfopClearTrap=NotificationType((1,3,6,1,4,1,8886,1,37,4,2))
raisecomApsDfopClearTrap.setObjects((_G,_M))
if mibBuilder.loadTexts:raisecomApsDfopClearTrap.setStatus(_A)
raisecomApsSwitchTrap=NotificationType((1,3,6,1,4,1,8886,1,37,4,3))
raisecomApsSwitchTrap.setObjects((_G,_R))
if mibBuilder.loadTexts:raisecomApsSwitchTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'raisecomAps':raisecomAps,'raisecomApsBaseGroup':raisecomApsBaseGroup,'raisecomApsTrapEnable':raisecomApsTrapEnable,'raisecomApsCfgTable':raisecomApsCfgTable,'raisecomApsCfgEntry':raisecomApsCfgEntry,_J:raisecomApsId,'raisecomApsName':raisecomApsName,'raisecomApsType':raisecomApsType,'raisecomApsWorkingPort':raisecomApsWorkingPort,'raisecomApsWorkingBlockVlanlist':raisecomApsWorkingBlockVlanlist,'raisecomApsProtectionPort':raisecomApsProtectionPort,'raisecomApsProtectionBlockVlanlist':raisecomApsProtectionBlockVlanlist,'raisecomApsWorkingIngressAssociation':raisecomApsWorkingIngressAssociation,'raisecomApsWorkingEgressAssociation':raisecomApsWorkingEgressAssociation,'raisecomApsProtectionIngressAssociation':raisecomApsProtectionIngressAssociation,'raisecomApsProtectionEgressAssociation':raisecomApsProtectionEgressAssociation,'raisecomApsProtectionTypeAdmin':raisecomApsProtectionTypeAdmin,'raisecomApsProtectionTypeOper':raisecomApsProtectionTypeOper,'raisecomApsForceSwitch':raisecomApsForceSwitch,'raisecomApsManualSwitch':raisecomApsManualSwitch,'raisecomApsManualSwitchtoWork':raisecomApsManualSwitchtoWork,'raisecomApsLockout':raisecomApsLockout,'raisecomApsClear':raisecomApsClear,'raisecomApsWtrTimer':raisecomApsWtrTimer,'raisecomApsHoldOffTimer':raisecomApsHoldOffTimer,'raisecomApsProtocolVlan':raisecomApsProtocolVlan,_R:raisecomApsStatus,'raisecomApsDfopStatus':raisecomApsDfopStatus,'raisecomApsRowStatus':raisecomApsRowStatus,'raisecomApsStatisticsTable':raisecomApsStatisticsTable,'raisecomApsStatisticsEntry':raisecomApsStatisticsEntry,'raisecomApsStatisticsSwitchCounts':raisecomApsStatisticsSwitchCounts,'raisecomApsStatisticsApsTx':raisecomApsStatisticsApsTx,'raisecomApsStatisticsApsRx':raisecomApsStatisticsApsRx,'raisecomApsStatisticsLastStatusOccur':raisecomApsStatisticsLastStatusOccur,'raisecomApsStatisticsLastSwitchOccur':raisecomApsStatisticsLastSwitchOccur,_M:raisecomApsStatisticsLastDfop,'raisecomApsStatisticsClear':raisecomApsStatisticsClear,'raisecomApsPeerTable':raisecomApsPeerTable,'raisecomApsPeerEntry':raisecomApsPeerEntry,'raisecomApsPeerProtectionType':raisecomApsPeerProtectionType,'raisecomApsPeerStatus':raisecomApsPeerStatus,'raisecomApsRequestSignal':raisecomApsRequestSignal,'raisecomApsBridgedSignal':raisecomApsBridgedSignal,'raisecomApsAssociationGroup':raisecomApsAssociationGroup,'raisecomApsAssociationTable':raisecomApsAssociationTable,'raisecomApsAssociationEntry':raisecomApsAssociationEntry,_O:raisecomApsAssociationName,'raisecomApsAssociationMdName':raisecomApsAssociationMdName,'raisecomApsAssociationMdLevel':raisecomApsAssociationMdLevel,'raisecomApsAssociationMaName':raisecomApsAssociationMaName,'raisecomApsAssociationRowStatus':raisecomApsAssociationRowStatus,'raisecomApsFailureDetGroup':raisecomApsFailureDetGroup,'raisecomApsFailureDetTable':raisecomApsFailureDetTable,'raisecomApsFailureDetEntry':raisecomApsFailureDetEntry,_P:raisecomApsFdLink,'raisecomApsFdType':raisecomApsFdType,'raisecomApsFdLinkStatus':raisecomApsFdLinkStatus,'raisecomApsFdSfType':raisecomApsFdSfType,'raisecomApsFdMdName':raisecomApsFdMdName,'raisecomApsFdMaName':raisecomApsFdMaName,'raisecomApsFdLocalMep':raisecomApsFdLocalMep,'raisecomApsFdRemoteMep':raisecomApsFdRemoteMep,'raisecomApsMdLevel':raisecomApsMdLevel,'raisecomApsNotifications':raisecomApsNotifications,'raisecomApsDfopTrap':raisecomApsDfopTrap,'raisecomApsDfopClearTrap':raisecomApsDfopClearTrap,'raisecomApsSwitchTrap':raisecomApsSwitchTrap})