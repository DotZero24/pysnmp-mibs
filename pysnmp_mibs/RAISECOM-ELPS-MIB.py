_Q='rcElpsStatus'
_P='physical-link'
_O='rcElpsFdLink'
_N='normal-traffic-signal'
_M='not-accessible'
_L='rcElpsStatisticsLastDfop'
_K='EnableVar'
_J='OctetString'
_I='rcElpsId'
_H='TruthValue'
_G='Unsigned32'
_F='RAISECOM-ELPS-MIB'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
EnableVar,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_K,'Vlanset')
rcElps=ModuleIdentity((1,3,6,1,4,1,8886,6,1,54))
_RcElpsBaseGroup_ObjectIdentity=ObjectIdentity
rcElpsBaseGroup=_RcElpsBaseGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,54,1))
class _RcElpsTrapEnable_Type(EnableVar):defaultValue=2
_RcElpsTrapEnable_Type.__name__=_K
_RcElpsTrapEnable_Object=MibScalar
rcElpsTrapEnable=_RcElpsTrapEnable_Object((1,3,6,1,4,1,8886,6,1,54,1,1),_RcElpsTrapEnable_Type())
rcElpsTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsTrapEnable.setStatus(_A)
_RcElpsCfgTable_Object=MibTable
rcElpsCfgTable=_RcElpsCfgTable_Object((1,3,6,1,4,1,8886,6,1,54,1,2))
if mibBuilder.loadTexts:rcElpsCfgTable.setStatus(_A)
_RcElpsCfgEntry_Object=MibTableRow
rcElpsCfgEntry=_RcElpsCfgEntry_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1))
rcElpsCfgEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:rcElpsCfgEntry.setStatus(_A)
class _RcElpsId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcElpsId_Type.__name__=_G
_RcElpsId_Object=MibTableColumn
rcElpsId=_RcElpsId_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,1),_RcElpsId_Type())
rcElpsId.setMaxAccess(_M)
if mibBuilder.loadTexts:rcElpsId.setStatus(_A)
class _RcElpsName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RcElpsName_Type.__name__=_J
_RcElpsName_Object=MibTableColumn
rcElpsName=_RcElpsName_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,2),_RcElpsName_Type())
rcElpsName.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsName.setStatus(_A)
_RcElpsWorkingPort_Type=Integer32
_RcElpsWorkingPort_Object=MibTableColumn
rcElpsWorkingPort=_RcElpsWorkingPort_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,3),_RcElpsWorkingPort_Type())
rcElpsWorkingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsWorkingPort.setStatus(_A)
_RcElpsWorkingBlockVlanlist_Type=Vlanset
_RcElpsWorkingBlockVlanlist_Object=MibTableColumn
rcElpsWorkingBlockVlanlist=_RcElpsWorkingBlockVlanlist_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,4),_RcElpsWorkingBlockVlanlist_Type())
rcElpsWorkingBlockVlanlist.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsWorkingBlockVlanlist.setStatus(_A)
_RcElpsProtectionPort_Type=Integer32
_RcElpsProtectionPort_Object=MibTableColumn
rcElpsProtectionPort=_RcElpsProtectionPort_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,5),_RcElpsProtectionPort_Type())
rcElpsProtectionPort.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsProtectionPort.setStatus(_A)
_RcElpsProtectionBlockVlanlist_Type=Vlanset
_RcElpsProtectionBlockVlanlist_Object=MibTableColumn
rcElpsProtectionBlockVlanlist=_RcElpsProtectionBlockVlanlist_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,6),_RcElpsProtectionBlockVlanlist_Type())
rcElpsProtectionBlockVlanlist.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsProtectionBlockVlanlist.setStatus(_A)
class _RcElpsProtectionTypeAdmin_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RcElpsProtectionTypeAdmin_Type.__name__=_G
_RcElpsProtectionTypeAdmin_Object=MibTableColumn
rcElpsProtectionTypeAdmin=_RcElpsProtectionTypeAdmin_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,7),_RcElpsProtectionTypeAdmin_Type())
rcElpsProtectionTypeAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsProtectionTypeAdmin.setStatus(_A)
class _RcElpsProtectionTypeOper_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RcElpsProtectionTypeOper_Type.__name__=_G
_RcElpsProtectionTypeOper_Object=MibTableColumn
rcElpsProtectionTypeOper=_RcElpsProtectionTypeOper_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,8),_RcElpsProtectionTypeOper_Type())
rcElpsProtectionTypeOper.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsProtectionTypeOper.setStatus(_A)
class _RcElpsForceSwitch_Type(TruthValue):defaultValue=2
_RcElpsForceSwitch_Type.__name__=_H
_RcElpsForceSwitch_Object=MibTableColumn
rcElpsForceSwitch=_RcElpsForceSwitch_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,9),_RcElpsForceSwitch_Type())
rcElpsForceSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsForceSwitch.setStatus(_A)
class _RcElpsManualSwitch_Type(TruthValue):defaultValue=2
_RcElpsManualSwitch_Type.__name__=_H
_RcElpsManualSwitch_Object=MibTableColumn
rcElpsManualSwitch=_RcElpsManualSwitch_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,10),_RcElpsManualSwitch_Type())
rcElpsManualSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsManualSwitch.setStatus(_A)
class _RcElpsManualSwitchtoWork_Type(TruthValue):defaultValue=2
_RcElpsManualSwitchtoWork_Type.__name__=_H
_RcElpsManualSwitchtoWork_Object=MibTableColumn
rcElpsManualSwitchtoWork=_RcElpsManualSwitchtoWork_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,11),_RcElpsManualSwitchtoWork_Type())
rcElpsManualSwitchtoWork.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsManualSwitchtoWork.setStatus(_A)
class _RcElpsLockout_Type(TruthValue):defaultValue=2
_RcElpsLockout_Type.__name__=_H
_RcElpsLockout_Object=MibTableColumn
rcElpsLockout=_RcElpsLockout_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,12),_RcElpsLockout_Type())
rcElpsLockout.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsLockout.setStatus(_A)
class _RcElpsClear_Type(TruthValue):defaultValue=2
_RcElpsClear_Type.__name__=_H
_RcElpsClear_Object=MibTableColumn
rcElpsClear=_RcElpsClear_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,13),_RcElpsClear_Type())
rcElpsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsClear.setStatus(_A)
class _RcElpsWtrTimer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_RcElpsWtrTimer_Type.__name__=_G
_RcElpsWtrTimer_Object=MibTableColumn
rcElpsWtrTimer=_RcElpsWtrTimer_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,14),_RcElpsWtrTimer_Type())
rcElpsWtrTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsWtrTimer.setStatus(_A)
class _RcElpsHoldOffTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RcElpsHoldOffTimer_Type.__name__=_G
_RcElpsHoldOffTimer_Object=MibTableColumn
rcElpsHoldOffTimer=_RcElpsHoldOffTimer_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,15),_RcElpsHoldOffTimer_Type())
rcElpsHoldOffTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsHoldOffTimer.setStatus(_A)
class _RcElpsProtocolVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcElpsProtocolVlan_Type.__name__=_C
_RcElpsProtocolVlan_Object=MibTableColumn
rcElpsProtocolVlan=_RcElpsProtocolVlan_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,16),_RcElpsProtocolVlan_Type())
rcElpsProtocolVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsProtocolVlan.setStatus(_A)
class _RcElpsStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('nr-w',1),('nr-p',2),('lo',3),('fs',4),('sf-w',5),('sf-p',6),('ms',7),('ms-w',8),('wtr',9),('dnr',10)))
_RcElpsStatus_Type.__name__=_C
_RcElpsStatus_Object=MibTableColumn
rcElpsStatus=_RcElpsStatus_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,17),_RcElpsStatus_Type())
rcElpsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatus.setStatus(_A)
class _RcElpsDfopStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('dFOP-CM',2),('dFOP-PM',3),('dFOP-NR',4)))
_RcElpsDfopStatus_Type.__name__=_C
_RcElpsDfopStatus_Object=MibTableColumn
rcElpsDfopStatus=_RcElpsDfopStatus_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,18),_RcElpsDfopStatus_Type())
rcElpsDfopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsDfopStatus.setStatus(_A)
_RcElpsRowStatus_Type=RowStatus
_RcElpsRowStatus_Object=MibTableColumn
rcElpsRowStatus=_RcElpsRowStatus_Object((1,3,6,1,4,1,8886,6,1,54,1,2,1,19),_RcElpsRowStatus_Type())
rcElpsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcElpsRowStatus.setStatus(_A)
_RcElpsStatisticsTable_Object=MibTable
rcElpsStatisticsTable=_RcElpsStatisticsTable_Object((1,3,6,1,4,1,8886,6,1,54,1,3))
if mibBuilder.loadTexts:rcElpsStatisticsTable.setStatus(_A)
_RcElpsStatisticsEntry_Object=MibTableRow
rcElpsStatisticsEntry=_RcElpsStatisticsEntry_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1))
rcElpsStatisticsEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:rcElpsStatisticsEntry.setStatus(_A)
_RcElpsStatisticsSwitchCounts_Type=Unsigned32
_RcElpsStatisticsSwitchCounts_Object=MibTableColumn
rcElpsStatisticsSwitchCounts=_RcElpsStatisticsSwitchCounts_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,1),_RcElpsStatisticsSwitchCounts_Type())
rcElpsStatisticsSwitchCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatisticsSwitchCounts.setStatus(_A)
_RcElpsStatisticsApsTx_Type=Unsigned32
_RcElpsStatisticsApsTx_Object=MibTableColumn
rcElpsStatisticsApsTx=_RcElpsStatisticsApsTx_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,2),_RcElpsStatisticsApsTx_Type())
rcElpsStatisticsApsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatisticsApsTx.setStatus(_A)
_RcElpsStatisticsApsRx_Type=Unsigned32
_RcElpsStatisticsApsRx_Object=MibTableColumn
rcElpsStatisticsApsRx=_RcElpsStatisticsApsRx_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,3),_RcElpsStatisticsApsRx_Type())
rcElpsStatisticsApsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatisticsApsRx.setStatus(_A)
_RcElpsStatisticsLastStatusOccur_Type=TimeTicks
_RcElpsStatisticsLastStatusOccur_Object=MibTableColumn
rcElpsStatisticsLastStatusOccur=_RcElpsStatisticsLastStatusOccur_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,4),_RcElpsStatisticsLastStatusOccur_Type())
rcElpsStatisticsLastStatusOccur.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatisticsLastStatusOccur.setStatus(_A)
_RcElpsStatisticsLastSwitchOccur_Type=TimeTicks
_RcElpsStatisticsLastSwitchOccur_Object=MibTableColumn
rcElpsStatisticsLastSwitchOccur=_RcElpsStatisticsLastSwitchOccur_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,5),_RcElpsStatisticsLastSwitchOccur_Type())
rcElpsStatisticsLastSwitchOccur.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatisticsLastSwitchOccur.setStatus(_A)
_RcElpsStatisticsLastDfop_Type=TimeTicks
_RcElpsStatisticsLastDfop_Object=MibTableColumn
rcElpsStatisticsLastDfop=_RcElpsStatisticsLastDfop_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,6),_RcElpsStatisticsLastDfop_Type())
rcElpsStatisticsLastDfop.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsStatisticsLastDfop.setStatus(_A)
class _RcElpsStatisticsClear_Type(EnableVar):defaultValue=2
_RcElpsStatisticsClear_Type.__name__=_K
_RcElpsStatisticsClear_Object=MibTableColumn
rcElpsStatisticsClear=_RcElpsStatisticsClear_Object((1,3,6,1,4,1,8886,6,1,54,1,3,1,7),_RcElpsStatisticsClear_Type())
rcElpsStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsStatisticsClear.setStatus(_A)
_RcElpsPeerTable_Object=MibTable
rcElpsPeerTable=_RcElpsPeerTable_Object((1,3,6,1,4,1,8886,6,1,54,1,4))
if mibBuilder.loadTexts:rcElpsPeerTable.setStatus(_A)
_RcElpsPeerEntry_Object=MibTableRow
rcElpsPeerEntry=_RcElpsPeerEntry_Object((1,3,6,1,4,1,8886,6,1,54,1,4,1))
rcElpsPeerEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:rcElpsPeerEntry.setStatus(_A)
class _RcElpsPeerProtectionType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,15))
_RcElpsPeerProtectionType_Type.__name__=_G
_RcElpsPeerProtectionType_Object=MibTableColumn
rcElpsPeerProtectionType=_RcElpsPeerProtectionType_Object((1,3,6,1,4,1,8886,6,1,54,1,4,1,1),_RcElpsPeerProtectionType_Type())
rcElpsPeerProtectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsPeerProtectionType.setStatus(_A)
class _RcElpsPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('nr-w',1),('nr-p',2),('lo',3),('fs',4),('sf-w',5),('sf-p',6),('ms',7),('ms-w',8),('wtr',9),('dnr',10),('sd',11),('exer',12),('rr',13)))
_RcElpsPeerStatus_Type.__name__=_C
_RcElpsPeerStatus_Object=MibTableColumn
rcElpsPeerStatus=_RcElpsPeerStatus_Object((1,3,6,1,4,1,8886,6,1,54,1,4,1,2),_RcElpsPeerStatus_Type())
rcElpsPeerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsPeerStatus.setStatus(_A)
class _RcElpsRequestSignal_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('null',0),(_N,1)))
_RcElpsRequestSignal_Type.__name__=_C
_RcElpsRequestSignal_Object=MibTableColumn
rcElpsRequestSignal=_RcElpsRequestSignal_Object((1,3,6,1,4,1,8886,6,1,54,1,4,1,3),_RcElpsRequestSignal_Type())
rcElpsRequestSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsRequestSignal.setStatus(_A)
class _RcElpsBridgedSignal_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('null',0),(_N,1)))
_RcElpsBridgedSignal_Type.__name__=_C
_RcElpsBridgedSignal_Object=MibTableColumn
rcElpsBridgedSignal=_RcElpsBridgedSignal_Object((1,3,6,1,4,1,8886,6,1,54,1,4,1,4),_RcElpsBridgedSignal_Type())
rcElpsBridgedSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsBridgedSignal.setStatus(_A)
_RcElpsNotifications_ObjectIdentity=ObjectIdentity
rcElpsNotifications=_RcElpsNotifications_ObjectIdentity((1,3,6,1,4,1,8886,6,1,54,1,5))
_RcElpsFailureDetGroup_ObjectIdentity=ObjectIdentity
rcElpsFailureDetGroup=_RcElpsFailureDetGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,54,2))
_RcElpsFailureDetTable_Object=MibTable
rcElpsFailureDetTable=_RcElpsFailureDetTable_Object((1,3,6,1,4,1,8886,6,1,54,2,1))
if mibBuilder.loadTexts:rcElpsFailureDetTable.setStatus(_A)
_RcElpsFailureDetEntry_Object=MibTableRow
rcElpsFailureDetEntry=_RcElpsFailureDetEntry_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1))
rcElpsFailureDetEntry.setIndexNames((0,_F,_I),(0,_F,_O))
if mibBuilder.loadTexts:rcElpsFailureDetEntry.setStatus(_A)
class _RcElpsFdLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('working',1),('protection',2)))
_RcElpsFdLink_Type.__name__=_C
_RcElpsFdLink_Object=MibTableColumn
rcElpsFdLink=_RcElpsFdLink_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,1),_RcElpsFdLink_Type())
rcElpsFdLink.setMaxAccess(_M)
if mibBuilder.loadTexts:rcElpsFdLink.setStatus(_A)
class _RcElpsFdType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('cc',2),('both',3)))
_RcElpsFdType_Type.__name__=_C
_RcElpsFdType_Object=MibTableColumn
rcElpsFdType=_RcElpsFdType_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,2),_RcElpsFdType_Type())
rcElpsFdType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsFdType.setStatus(_A)
class _RcElpsFdLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('sf',2)))
_RcElpsFdLinkStatus_Type.__name__=_C
_RcElpsFdLinkStatus_Object=MibTableColumn
rcElpsFdLinkStatus=_RcElpsFdLinkStatus_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,3),_RcElpsFdLinkStatus_Type())
rcElpsFdLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsFdLinkStatus.setStatus(_A)
class _RcElpsFdSfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_P,2),('cc',3),('both',4)))
_RcElpsFdSfType_Type.__name__=_C
_RcElpsFdSfType_Object=MibTableColumn
rcElpsFdSfType=_RcElpsFdSfType_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,4),_RcElpsFdSfType_Type())
rcElpsFdSfType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcElpsFdSfType.setStatus(_A)
class _RcElpsFdMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcElpsFdMdName_Type.__name__=_J
_RcElpsFdMdName_Object=MibTableColumn
rcElpsFdMdName=_RcElpsFdMdName_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,5),_RcElpsFdMdName_Type())
rcElpsFdMdName.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsFdMdName.setStatus(_A)
class _RcElpsFdMaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_RcElpsFdMaName_Type.__name__=_J
_RcElpsFdMaName_Object=MibTableColumn
rcElpsFdMaName=_RcElpsFdMaName_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,6),_RcElpsFdMaName_Type())
rcElpsFdMaName.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsFdMaName.setStatus(_A)
class _RcElpsFdLocalMep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_RcElpsFdLocalMep_Type.__name__=_C
_RcElpsFdLocalMep_Object=MibTableColumn
rcElpsFdLocalMep=_RcElpsFdLocalMep_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,7),_RcElpsFdLocalMep_Type())
rcElpsFdLocalMep.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsFdLocalMep.setStatus(_A)
class _RcElpsFdRemoteMep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_RcElpsFdRemoteMep_Type.__name__=_C
_RcElpsFdRemoteMep_Object=MibTableColumn
rcElpsFdRemoteMep=_RcElpsFdRemoteMep_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,8),_RcElpsFdRemoteMep_Type())
rcElpsFdRemoteMep.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsFdRemoteMep.setStatus(_A)
class _RcElpsMdLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcElpsMdLevel_Type.__name__=_C
_RcElpsMdLevel_Object=MibTableColumn
rcElpsMdLevel=_RcElpsMdLevel_Object((1,3,6,1,4,1,8886,6,1,54,2,1,1,9),_RcElpsMdLevel_Type())
rcElpsMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:rcElpsMdLevel.setStatus(_A)
rcElpsDfopTrap=NotificationType((1,3,6,1,4,1,8886,6,1,54,1,5,1))
rcElpsDfopTrap.setObjects((_F,_L))
if mibBuilder.loadTexts:rcElpsDfopTrap.setStatus(_A)
rcElpsDfopClearTrap=NotificationType((1,3,6,1,4,1,8886,6,1,54,1,5,2))
rcElpsDfopClearTrap.setObjects((_F,_L))
if mibBuilder.loadTexts:rcElpsDfopClearTrap.setStatus(_A)
rcElpsSwitchTrap=NotificationType((1,3,6,1,4,1,8886,6,1,54,1,5,3))
rcElpsSwitchTrap.setObjects((_F,_Q))
if mibBuilder.loadTexts:rcElpsSwitchTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rcElps':rcElps,'rcElpsBaseGroup':rcElpsBaseGroup,'rcElpsTrapEnable':rcElpsTrapEnable,'rcElpsCfgTable':rcElpsCfgTable,'rcElpsCfgEntry':rcElpsCfgEntry,_I:rcElpsId,'rcElpsName':rcElpsName,'rcElpsWorkingPort':rcElpsWorkingPort,'rcElpsWorkingBlockVlanlist':rcElpsWorkingBlockVlanlist,'rcElpsProtectionPort':rcElpsProtectionPort,'rcElpsProtectionBlockVlanlist':rcElpsProtectionBlockVlanlist,'rcElpsProtectionTypeAdmin':rcElpsProtectionTypeAdmin,'rcElpsProtectionTypeOper':rcElpsProtectionTypeOper,'rcElpsForceSwitch':rcElpsForceSwitch,'rcElpsManualSwitch':rcElpsManualSwitch,'rcElpsManualSwitchtoWork':rcElpsManualSwitchtoWork,'rcElpsLockout':rcElpsLockout,'rcElpsClear':rcElpsClear,'rcElpsWtrTimer':rcElpsWtrTimer,'rcElpsHoldOffTimer':rcElpsHoldOffTimer,'rcElpsProtocolVlan':rcElpsProtocolVlan,_Q:rcElpsStatus,'rcElpsDfopStatus':rcElpsDfopStatus,'rcElpsRowStatus':rcElpsRowStatus,'rcElpsStatisticsTable':rcElpsStatisticsTable,'rcElpsStatisticsEntry':rcElpsStatisticsEntry,'rcElpsStatisticsSwitchCounts':rcElpsStatisticsSwitchCounts,'rcElpsStatisticsApsTx':rcElpsStatisticsApsTx,'rcElpsStatisticsApsRx':rcElpsStatisticsApsRx,'rcElpsStatisticsLastStatusOccur':rcElpsStatisticsLastStatusOccur,'rcElpsStatisticsLastSwitchOccur':rcElpsStatisticsLastSwitchOccur,_L:rcElpsStatisticsLastDfop,'rcElpsStatisticsClear':rcElpsStatisticsClear,'rcElpsPeerTable':rcElpsPeerTable,'rcElpsPeerEntry':rcElpsPeerEntry,'rcElpsPeerProtectionType':rcElpsPeerProtectionType,'rcElpsPeerStatus':rcElpsPeerStatus,'rcElpsRequestSignal':rcElpsRequestSignal,'rcElpsBridgedSignal':rcElpsBridgedSignal,'rcElpsNotifications':rcElpsNotifications,'rcElpsDfopTrap':rcElpsDfopTrap,'rcElpsDfopClearTrap':rcElpsDfopClearTrap,'rcElpsSwitchTrap':rcElpsSwitchTrap,'rcElpsFailureDetGroup':rcElpsFailureDetGroup,'rcElpsFailureDetTable':rcElpsFailureDetTable,'rcElpsFailureDetEntry':rcElpsFailureDetEntry,_O:rcElpsFdLink,'rcElpsFdType':rcElpsFdType,'rcElpsFdLinkStatus':rcElpsFdLinkStatus,'rcElpsFdSfType':rcElpsFdSfType,'rcElpsFdMdName':rcElpsFdMdName,'rcElpsFdMaName':rcElpsFdMaName,'rcElpsFdLocalMep':rcElpsFdLocalMep,'rcElpsFdRemoteMep':rcElpsFdRemoteMep,'rcElpsMdLevel':rcElpsMdLevel})