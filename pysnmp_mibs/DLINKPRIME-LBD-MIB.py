_P='dpLbdIfCfgGroup'
_O='dpLbdCfgGroup'
_N='dpLbdLoopRecovery'
_M='dpLbdLoopOccurred'
_L='dpLbdIfLoopStatus'
_K='dpLbdIfCfgEnabled'
_J='dpLbdNotifyEnabled'
_I='dpLbdCtrlGlobalEnabled'
_H='dpLbdCtrlInterval'
_G='dpLbdIfCfgIndex'
_F='seconds'
_E='dpLbdNotifyInfoIfIndex'
_D='Integer32'
_C='read-write'
_B='DLINKPRIME-LBD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dlinkPrimeLoopbackDetectMIB=ModuleIdentity((1,3,6,1,4,1,171,15,7))
if mibBuilder.loadTexts:dlinkPrimeLoopbackDetectMIB.setRevisions(('2014-04-26 00:00',))
_DpLbdNotifications_ObjectIdentity=ObjectIdentity
dpLbdNotifications=_DpLbdNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,7,0))
_DpLbdObjects_ObjectIdentity=ObjectIdentity
dpLbdObjects=_DpLbdObjects_ObjectIdentity((1,3,6,1,4,1,171,15,7,1))
_DpLbdCtrlGlobalEnabled_Type=TruthValue
_DpLbdCtrlGlobalEnabled_Object=MibScalar
dpLbdCtrlGlobalEnabled=_DpLbdCtrlGlobalEnabled_Object((1,3,6,1,4,1,171,15,7,1,1),_DpLbdCtrlGlobalEnabled_Type())
dpLbdCtrlGlobalEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpLbdCtrlGlobalEnabled.setStatus(_A)
class _DpLbdCtrlInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_DpLbdCtrlInterval_Type.__name__=_D
_DpLbdCtrlInterval_Object=MibScalar
dpLbdCtrlInterval=_DpLbdCtrlInterval_Object((1,3,6,1,4,1,171,15,7,1,2),_DpLbdCtrlInterval_Type())
dpLbdCtrlInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:dpLbdCtrlInterval.setStatus(_A)
if mibBuilder.loadTexts:dpLbdCtrlInterval.setUnits(_F)
class _DpLbdCtrlRecover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,1000000))
_DpLbdCtrlRecover_Type.__name__=_D
_DpLbdCtrlRecover_Object=MibScalar
dpLbdCtrlRecover=_DpLbdCtrlRecover_Object((1,3,6,1,4,1,171,15,7,1,3),_DpLbdCtrlRecover_Type())
dpLbdCtrlRecover.setMaxAccess(_C)
if mibBuilder.loadTexts:dpLbdCtrlRecover.setStatus(_A)
if mibBuilder.loadTexts:dpLbdCtrlRecover.setUnits(_F)
_DpLbdNotifyEnabled_Type=TruthValue
_DpLbdNotifyEnabled_Object=MibScalar
dpLbdNotifyEnabled=_DpLbdNotifyEnabled_Object((1,3,6,1,4,1,171,15,7,1,4),_DpLbdNotifyEnabled_Type())
dpLbdNotifyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpLbdNotifyEnabled.setStatus(_A)
_DpLbdIfCfgTable_Object=MibTable
dpLbdIfCfgTable=_DpLbdIfCfgTable_Object((1,3,6,1,4,1,171,15,7,1,5))
if mibBuilder.loadTexts:dpLbdIfCfgTable.setStatus(_A)
_DpLbdIfCfgEntry_Object=MibTableRow
dpLbdIfCfgEntry=_DpLbdIfCfgEntry_Object((1,3,6,1,4,1,171,15,7,1,5,1))
dpLbdIfCfgEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dpLbdIfCfgEntry.setStatus(_A)
_DpLbdIfCfgIndex_Type=InterfaceIndex
_DpLbdIfCfgIndex_Object=MibTableColumn
dpLbdIfCfgIndex=_DpLbdIfCfgIndex_Object((1,3,6,1,4,1,171,15,7,1,5,1,1),_DpLbdIfCfgIndex_Type())
dpLbdIfCfgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dpLbdIfCfgIndex.setStatus(_A)
_DpLbdIfCfgEnabled_Type=TruthValue
_DpLbdIfCfgEnabled_Object=MibTableColumn
dpLbdIfCfgEnabled=_DpLbdIfCfgEnabled_Object((1,3,6,1,4,1,171,15,7,1,5,1,2),_DpLbdIfCfgEnabled_Type())
dpLbdIfCfgEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpLbdIfCfgEnabled.setStatus(_A)
class _DpLbdIfLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('loop',2)))
_DpLbdIfLoopStatus_Type.__name__=_D
_DpLbdIfLoopStatus_Object=MibTableColumn
dpLbdIfLoopStatus=_DpLbdIfLoopStatus_Object((1,3,6,1,4,1,171,15,7,1,5,1,3),_DpLbdIfLoopStatus_Type())
dpLbdIfLoopStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:dpLbdIfLoopStatus.setStatus(_A)
_DpLbdNotifyInfo_ObjectIdentity=ObjectIdentity
dpLbdNotifyInfo=_DpLbdNotifyInfo_ObjectIdentity((1,3,6,1,4,1,171,15,7,1,8))
if mibBuilder.loadTexts:dpLbdNotifyInfo.setStatus(_A)
_DpLbdNotifyInfoIfIndex_Type=InterfaceIndex
_DpLbdNotifyInfoIfIndex_Object=MibScalar
dpLbdNotifyInfoIfIndex=_DpLbdNotifyInfoIfIndex_Object((1,3,6,1,4,1,171,15,7,1,8,1),_DpLbdNotifyInfoIfIndex_Type())
dpLbdNotifyInfoIfIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:dpLbdNotifyInfoIfIndex.setStatus(_A)
_DpLbdConformance_ObjectIdentity=ObjectIdentity
dpLbdConformance=_DpLbdConformance_ObjectIdentity((1,3,6,1,4,1,171,15,7,2))
_DpLbdMIBCompliances_ObjectIdentity=ObjectIdentity
dpLbdMIBCompliances=_DpLbdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,7,2,1))
_DpLbdMIBGroups_ObjectIdentity=ObjectIdentity
dpLbdMIBGroups=_DpLbdMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,7,2,2))
dpLbdCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,7,2,2,1))
dpLbdCfgGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_E)))
if mibBuilder.loadTexts:dpLbdCfgGroup.setStatus(_A)
dpLbdIfCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,7,2,2,2))
dpLbdIfCfgGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:dpLbdIfCfgGroup.setStatus(_A)
dpLbdLoopOccurred=NotificationType((1,3,6,1,4,1,171,15,7,0,1))
dpLbdLoopOccurred.setObjects((_B,_E))
if mibBuilder.loadTexts:dpLbdLoopOccurred.setStatus(_A)
dpLbdLoopRecovery=NotificationType((1,3,6,1,4,1,171,15,7,0,2))
dpLbdLoopRecovery.setObjects((_B,_E))
if mibBuilder.loadTexts:dpLbdLoopRecovery.setStatus(_A)
dpLbdNotificationGroup=NotificationGroup((1,3,6,1,4,1,171,15,7,2,2,3))
dpLbdNotificationGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:dpLbdNotificationGroup.setStatus(_A)
dpLbdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,7,2,1,1))
dpLbdMIBCompliance.setObjects(*((_B,_O),(_B,_P),(_B,'dpLbdCtrlModeGroup'),(_B,'dpLbdVlanCtrlGroup')))
if mibBuilder.loadTexts:dpLbdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeLoopbackDetectMIB':dlinkPrimeLoopbackDetectMIB,'dpLbdNotifications':dpLbdNotifications,_M:dpLbdLoopOccurred,_N:dpLbdLoopRecovery,'dpLbdObjects':dpLbdObjects,_I:dpLbdCtrlGlobalEnabled,_H:dpLbdCtrlInterval,'dpLbdCtrlRecover':dpLbdCtrlRecover,_J:dpLbdNotifyEnabled,'dpLbdIfCfgTable':dpLbdIfCfgTable,'dpLbdIfCfgEntry':dpLbdIfCfgEntry,_G:dpLbdIfCfgIndex,_K:dpLbdIfCfgEnabled,_L:dpLbdIfLoopStatus,'dpLbdNotifyInfo':dpLbdNotifyInfo,_E:dpLbdNotifyInfoIfIndex,'dpLbdConformance':dpLbdConformance,'dpLbdMIBCompliances':dpLbdMIBCompliances,'dpLbdMIBCompliance':dpLbdMIBCompliance,'dpLbdMIBGroups':dpLbdMIBGroups,_O:dpLbdCfgGroup,_P:dpLbdIfCfgGroup,'dpLbdNotificationGroup':dpLbdNotificationGroup})