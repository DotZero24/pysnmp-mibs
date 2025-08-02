_d='hpicfUdldPortConfigGroup1'
_c='hpicfUdldStatsGroup'
_b='hpicfUdldPortConfigGroup'
_a='hpicfUdldLinkUp'
_Z='hpicfUdldLinkfault'
_Y='hpicfUdldConfigTimeIntervalMs'
_X='hpicfUdldConfigForwardMode'
_W='hpicfUdldStatsClearAll'
_V='hpicfUdldStatsPortStatus'
_U='hpicfUdldStatsPortNumStateChange'
_T='hpicfUdldStatsPortTotalRx'
_S='hpicfUdldStatsPortTotalTx'
_R='hpicfUdldStatsPortNeighborPort'
_Q='hpicfUdldStatsPortNeighborMAC'
_P='hpicfUdldStatsPortCurrentState'
_O='deprecated'
_N='hpicfUdldPortStatsGroup'
_M='hpicfUdldPortVlanId'
_L='hpicfUdldPortAdminStatus'
_K='hpicfUdldConfigMaxRetries'
_J='hpicfUdldConfigTimeInterval'
_I='hpicfUdldNotificationGroup'
_H='Unsigned32'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='current'
_A='HP-ICF-UDLD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
hpicfUdldMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33))
if mibBuilder.loadTexts:hpicfUdldMIB.setRevisions(('2014-06-15 00:00','2009-08-07 00:00','2006-04-10 00:00'))
_HpicfUdldNotifications_ObjectIdentity=ObjectIdentity
hpicfUdldNotifications=_HpicfUdldNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,0))
_HpicfUdldNotificationPrefix_ObjectIdentity=ObjectIdentity
hpicfUdldNotificationPrefix=_HpicfUdldNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,0,0))
_HpicfUdldObjects_ObjectIdentity=ObjectIdentity
hpicfUdldObjects=_HpicfUdldObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,1))
_HpicfUdldConfig_ObjectIdentity=ObjectIdentity
hpicfUdldConfig=_HpicfUdldConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1))
class _HpicfUdldConfigTimeInterval_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_HpicfUdldConfigTimeInterval_Type.__name__=_H
_HpicfUdldConfigTimeInterval_Object=MibScalar
hpicfUdldConfigTimeInterval=_HpicfUdldConfigTimeInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,1),_HpicfUdldConfigTimeInterval_Type())
hpicfUdldConfigTimeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldConfigTimeInterval.setStatus(_B)
class _HpicfUdldConfigMaxRetries_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_HpicfUdldConfigMaxRetries_Type.__name__=_H
_HpicfUdldConfigMaxRetries_Object=MibScalar
hpicfUdldConfigMaxRetries=_HpicfUdldConfigMaxRetries_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,2),_HpicfUdldConfigMaxRetries_Type())
hpicfUdldConfigMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldConfigMaxRetries.setStatus(_B)
_HpicfUdldPortConfigTable_Object=MibTable
hpicfUdldPortConfigTable=_HpicfUdldPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,3))
if mibBuilder.loadTexts:hpicfUdldPortConfigTable.setStatus(_B)
_HpicfUdldPortConfigEntry_Object=MibTableRow
hpicfUdldPortConfigEntry=_HpicfUdldPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,3,1))
hpicfUdldPortConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfUdldPortConfigEntry.setStatus(_B)
class _HpicfUdldPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfUdldPortAdminStatus_Type.__name__=_G
_HpicfUdldPortAdminStatus_Object=MibTableColumn
hpicfUdldPortAdminStatus=_HpicfUdldPortAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,3,1,1),_HpicfUdldPortAdminStatus_Type())
hpicfUdldPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldPortAdminStatus.setStatus(_B)
class _HpicfUdldPortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfUdldPortVlanId_Type.__name__=_G
_HpicfUdldPortVlanId_Object=MibTableColumn
hpicfUdldPortVlanId=_HpicfUdldPortVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,3,1,2),_HpicfUdldPortVlanId_Type())
hpicfUdldPortVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldPortVlanId.setStatus(_B)
class _HpicfUdldConfigForwardMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('verifyThenForward',1),('forwardThenVerify',2)))
_HpicfUdldConfigForwardMode_Type.__name__=_G
_HpicfUdldConfigForwardMode_Object=MibScalar
hpicfUdldConfigForwardMode=_HpicfUdldConfigForwardMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,4),_HpicfUdldConfigForwardMode_Type())
hpicfUdldConfigForwardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldConfigForwardMode.setStatus(_B)
class _HpicfUdldConfigTimeIntervalMs_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HpicfUdldConfigTimeIntervalMs_Type.__name__=_H
_HpicfUdldConfigTimeIntervalMs_Object=MibScalar
hpicfUdldConfigTimeIntervalMs=_HpicfUdldConfigTimeIntervalMs_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,1,5),_HpicfUdldConfigTimeIntervalMs_Type())
hpicfUdldConfigTimeIntervalMs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldConfigTimeIntervalMs.setStatus(_B)
_HpicfUdldStats_ObjectIdentity=ObjectIdentity
hpicfUdldStats=_HpicfUdldStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2))
_HpicfUdldPortStatsTable_Object=MibTable
hpicfUdldPortStatsTable=_HpicfUdldPortStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1))
if mibBuilder.loadTexts:hpicfUdldPortStatsTable.setStatus(_B)
_HpicfUdldPortStatsEntry_Object=MibTableRow
hpicfUdldPortStatsEntry=_HpicfUdldPortStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1))
hpicfUdldPortStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpicfUdldPortStatsEntry.setStatus(_B)
class _HpicfUdldStatsPortCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('offline',1),('failure',2),('up',3)))
_HpicfUdldStatsPortCurrentState_Type.__name__=_G
_HpicfUdldStatsPortCurrentState_Object=MibTableColumn
hpicfUdldStatsPortCurrentState=_HpicfUdldStatsPortCurrentState_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,1),_HpicfUdldStatsPortCurrentState_Type())
hpicfUdldStatsPortCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortCurrentState.setStatus(_B)
_HpicfUdldStatsPortNeighborMAC_Type=MacAddress
_HpicfUdldStatsPortNeighborMAC_Object=MibTableColumn
hpicfUdldStatsPortNeighborMAC=_HpicfUdldStatsPortNeighborMAC_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,2),_HpicfUdldStatsPortNeighborMAC_Type())
hpicfUdldStatsPortNeighborMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortNeighborMAC.setStatus(_B)
_HpicfUdldStatsPortNeighborPort_Type=Integer32
_HpicfUdldStatsPortNeighborPort_Object=MibTableColumn
hpicfUdldStatsPortNeighborPort=_HpicfUdldStatsPortNeighborPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,3),_HpicfUdldStatsPortNeighborPort_Type())
hpicfUdldStatsPortNeighborPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortNeighborPort.setStatus(_B)
_HpicfUdldStatsPortTotalTx_Type=Counter32
_HpicfUdldStatsPortTotalTx_Object=MibTableColumn
hpicfUdldStatsPortTotalTx=_HpicfUdldStatsPortTotalTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,4),_HpicfUdldStatsPortTotalTx_Type())
hpicfUdldStatsPortTotalTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortTotalTx.setStatus(_B)
_HpicfUdldStatsPortTotalRx_Type=Counter32
_HpicfUdldStatsPortTotalRx_Object=MibTableColumn
hpicfUdldStatsPortTotalRx=_HpicfUdldStatsPortTotalRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,5),_HpicfUdldStatsPortTotalRx_Type())
hpicfUdldStatsPortTotalRx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortTotalRx.setStatus(_B)
_HpicfUdldStatsPortNumStateChange_Type=Counter32
_HpicfUdldStatsPortNumStateChange_Object=MibTableColumn
hpicfUdldStatsPortNumStateChange=_HpicfUdldStatsPortNumStateChange_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,6),_HpicfUdldStatsPortNumStateChange_Type())
hpicfUdldStatsPortNumStateChange.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortNumStateChange.setStatus(_B)
_HpicfUdldStatsPortStatus_Type=Integer32
_HpicfUdldStatsPortStatus_Object=MibTableColumn
hpicfUdldStatsPortStatus=_HpicfUdldStatsPortStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,1,1,7),_HpicfUdldStatsPortStatus_Type())
hpicfUdldStatsPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUdldStatsPortStatus.setStatus(_B)
_HpicfUdldStatsClearAll_Type=TruthValue
_HpicfUdldStatsClearAll_Object=MibScalar
hpicfUdldStatsClearAll=_HpicfUdldStatsClearAll_Object((1,3,6,1,4,1,11,2,14,11,5,1,33,1,2,2),_HpicfUdldStatsClearAll_Type())
hpicfUdldStatsClearAll.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfUdldStatsClearAll.setStatus(_B)
_HpicfUdldConformance_ObjectIdentity=ObjectIdentity
hpicfUdldConformance=_HpicfUdldConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,2))
_HpicfUdldCompliances_ObjectIdentity=ObjectIdentity
hpicfUdldCompliances=_HpicfUdldCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,2,1))
_HpicfUdldGroups_ObjectIdentity=ObjectIdentity
hpicfUdldGroups=_HpicfUdldGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,33,2,2))
hpicfUdldPortConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,33,2,2,1))
hpicfUdldPortConfigGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfUdldPortConfigGroup.setStatus(_O)
hpicfUdldPortStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,33,2,2,2))
hpicfUdldPortStatsGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:hpicfUdldPortStatsGroup.setStatus(_B)
hpicfUdldStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,33,2,2,4))
hpicfUdldStatsGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:hpicfUdldStatsGroup.setStatus(_B)
hpicfUdldPortConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,33,2,2,5))
hpicfUdldPortConfigGroup1.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hpicfUdldPortConfigGroup1.setStatus(_B)
hpicfUdldLinkfault=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,33,0,0,1))
hpicfUdldLinkfault.setObjects((_E,_F))
if mibBuilder.loadTexts:hpicfUdldLinkfault.setStatus(_B)
hpicfUdldLinkUp=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,33,0,0,2))
hpicfUdldLinkUp.setObjects((_E,_F))
if mibBuilder.loadTexts:hpicfUdldLinkUp.setStatus(_B)
hpicfUdldNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,33,2,2,3))
hpicfUdldNotificationGroup.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpicfUdldNotificationGroup.setStatus(_B)
hpicfUdldCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,33,2,1,1))
hpicfUdldCompliance.setObjects(*((_A,_b),(_A,_N),(_A,_I),(_A,_I)))
if mibBuilder.loadTexts:hpicfUdldCompliance.setStatus(_O)
hpicfUdldCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,33,2,1,2))
hpicfUdldCompliance2.setObjects((_A,_c))
if mibBuilder.loadTexts:hpicfUdldCompliance2.setStatus(_B)
hpicfUdldCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,33,2,1,3))
hpicfUdldCompliance3.setObjects(*((_A,_d),(_A,_N),(_A,_I)))
if mibBuilder.loadTexts:hpicfUdldCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfUdldMIB':hpicfUdldMIB,'hpicfUdldNotifications':hpicfUdldNotifications,'hpicfUdldNotificationPrefix':hpicfUdldNotificationPrefix,_Z:hpicfUdldLinkfault,_a:hpicfUdldLinkUp,'hpicfUdldObjects':hpicfUdldObjects,'hpicfUdldConfig':hpicfUdldConfig,_J:hpicfUdldConfigTimeInterval,_K:hpicfUdldConfigMaxRetries,'hpicfUdldPortConfigTable':hpicfUdldPortConfigTable,'hpicfUdldPortConfigEntry':hpicfUdldPortConfigEntry,_L:hpicfUdldPortAdminStatus,_M:hpicfUdldPortVlanId,_X:hpicfUdldConfigForwardMode,_Y:hpicfUdldConfigTimeIntervalMs,'hpicfUdldStats':hpicfUdldStats,'hpicfUdldPortStatsTable':hpicfUdldPortStatsTable,'hpicfUdldPortStatsEntry':hpicfUdldPortStatsEntry,_P:hpicfUdldStatsPortCurrentState,_Q:hpicfUdldStatsPortNeighborMAC,_R:hpicfUdldStatsPortNeighborPort,_S:hpicfUdldStatsPortTotalTx,_T:hpicfUdldStatsPortTotalRx,_U:hpicfUdldStatsPortNumStateChange,_V:hpicfUdldStatsPortStatus,_W:hpicfUdldStatsClearAll,'hpicfUdldConformance':hpicfUdldConformance,'hpicfUdldCompliances':hpicfUdldCompliances,'hpicfUdldCompliance':hpicfUdldCompliance,'hpicfUdldCompliance2':hpicfUdldCompliance2,'hpicfUdldCompliance3':hpicfUdldCompliance3,'hpicfUdldGroups':hpicfUdldGroups,_b:hpicfUdldPortConfigGroup,_N:hpicfUdldPortStatsGroup,_I:hpicfUdldNotificationGroup,_c:hpicfUdldStatsGroup,_d:hpicfUdldPortConfigGroup1})