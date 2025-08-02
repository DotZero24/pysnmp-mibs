_o='ciscoCNOSwitchVlanGroup'
_n='ciscoCNOSwitchMonitorPortGroup'
_m='ciscoCNOSwitchPortGroup'
_l='ciscoCNOSwitchConfigGroup'
_k='ciscoCNOSwitchSysInfoGroup'
_j='cnosVlanSTPState'
_i='cnosPortVlanMember'
_h='cnosPortMonitoring'
_g='cnosSysConfigMonitorPort'
_f='cnosSysConfigMonitor'
_e='cnosPortSTPPortFastMode'
_d='cnosPortLinkStatus'
_c='cnosPortSpeedStatus'
_b='cnosPortSpeedAdmin'
_a='cnosPortDuplexStatus'
_Z='cnosPortDuplexAdmin'
_Y='cnosPortControllerRevision'
_X='cnosPortName'
_W='cnosSysConfigDefaultReset'
_V='cnosSysConfigReset'
_U='cnosSysInfoAddrCapacity'
_T='cnosSysInfoBootVersion'
_S='cnosSysInfoBoardRevision'
_R='cnosSysInfoSerialNo'
_Q='cnosVlanIndex'
_P='oneHundredMbps'
_O='tenMbps'
_N='autoNegotiate'
_M='halfDuplex'
_L='fullDuplex'
_K='noReset'
_J='ifIndex'
_I='IF-MIB'
_H='disabled'
_G='enabled'
_F='DisplayString'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-CNO-SWITCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ciscoCNOSwitchMIB=ModuleIdentity((1,3,6,1,4,1,9,10,43))
if mibBuilder.loadTexts:ciscoCNOSwitchMIB.setRevisions(('1998-10-23 00:00',))
_CiscoCNOSwitchMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCNOSwitchMIBObjects=_CiscoCNOSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,43,1))
_CnosSysInfo_ObjectIdentity=ObjectIdentity
cnosSysInfo=_CnosSysInfo_ObjectIdentity((1,3,6,1,4,1,9,10,43,1,1))
class _CnosSysInfoSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CnosSysInfoSerialNo_Type.__name__=_F
_CnosSysInfoSerialNo_Object=MibScalar
cnosSysInfoSerialNo=_CnosSysInfoSerialNo_Object((1,3,6,1,4,1,9,10,43,1,1,1),_CnosSysInfoSerialNo_Type())
cnosSysInfoSerialNo.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosSysInfoSerialNo.setStatus(_A)
class _CnosSysInfoBoardRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnosSysInfoBoardRevision_Type.__name__=_C
_CnosSysInfoBoardRevision_Object=MibScalar
cnosSysInfoBoardRevision=_CnosSysInfoBoardRevision_Object((1,3,6,1,4,1,9,10,43,1,1,2),_CnosSysInfoBoardRevision_Type())
cnosSysInfoBoardRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosSysInfoBoardRevision.setStatus(_A)
class _CnosSysInfoBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CnosSysInfoBootVersion_Type.__name__=_F
_CnosSysInfoBootVersion_Object=MibScalar
cnosSysInfoBootVersion=_CnosSysInfoBootVersion_Object((1,3,6,1,4,1,9,10,43,1,1,3),_CnosSysInfoBootVersion_Type())
cnosSysInfoBootVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosSysInfoBootVersion.setStatus(_A)
class _CnosSysInfoAddrCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnosSysInfoAddrCapacity_Type.__name__=_C
_CnosSysInfoAddrCapacity_Object=MibScalar
cnosSysInfoAddrCapacity=_CnosSysInfoAddrCapacity_Object((1,3,6,1,4,1,9,10,43,1,1,4),_CnosSysInfoAddrCapacity_Type())
cnosSysInfoAddrCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosSysInfoAddrCapacity.setStatus(_A)
_CnosSysConfig_ObjectIdentity=ObjectIdentity
cnosSysConfig=_CnosSysConfig_ObjectIdentity((1,3,6,1,4,1,9,10,43,1,2))
class _CnosSysConfigReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('reset',2)))
_CnosSysConfigReset_Type.__name__=_C
_CnosSysConfigReset_Object=MibScalar
cnosSysConfigReset=_CnosSysConfigReset_Object((1,3,6,1,4,1,9,10,43,1,2,1),_CnosSysConfigReset_Type())
cnosSysConfigReset.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosSysConfigReset.setStatus(_A)
class _CnosSysConfigDefaultReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('reset',2)))
_CnosSysConfigDefaultReset_Type.__name__=_C
_CnosSysConfigDefaultReset_Object=MibScalar
cnosSysConfigDefaultReset=_CnosSysConfigDefaultReset_Object((1,3,6,1,4,1,9,10,43,1,2,2),_CnosSysConfigDefaultReset_Type())
cnosSysConfigDefaultReset.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosSysConfigDefaultReset.setStatus(_A)
class _CnosSysConfigMonitor_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CnosSysConfigMonitor_Type.__name__=_C
_CnosSysConfigMonitor_Object=MibScalar
cnosSysConfigMonitor=_CnosSysConfigMonitor_Object((1,3,6,1,4,1,9,10,43,1,2,3),_CnosSysConfigMonitor_Type())
cnosSysConfigMonitor.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosSysConfigMonitor.setStatus(_A)
class _CnosSysConfigMonitorPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CnosSysConfigMonitorPort_Type.__name__=_C
_CnosSysConfigMonitorPort_Object=MibScalar
cnosSysConfigMonitorPort=_CnosSysConfigMonitorPort_Object((1,3,6,1,4,1,9,10,43,1,2,4),_CnosSysConfigMonitorPort_Type())
cnosSysConfigMonitorPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosSysConfigMonitorPort.setStatus(_A)
_CnosPort_ObjectIdentity=ObjectIdentity
cnosPort=_CnosPort_ObjectIdentity((1,3,6,1,4,1,9,10,43,1,3))
_CnosPortTable_Object=MibTable
cnosPortTable=_CnosPortTable_Object((1,3,6,1,4,1,9,10,43,1,3,1))
if mibBuilder.loadTexts:cnosPortTable.setStatus(_A)
_CnosPortEntry_Object=MibTableRow
cnosPortEntry=_CnosPortEntry_Object((1,3,6,1,4,1,9,10,43,1,3,1,1))
cnosPortEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cnosPortEntry.setStatus(_A)
class _CnosPortControllerRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnosPortControllerRevision_Type.__name__=_C
_CnosPortControllerRevision_Object=MibTableColumn
cnosPortControllerRevision=_CnosPortControllerRevision_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,1),_CnosPortControllerRevision_Type())
cnosPortControllerRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosPortControllerRevision.setStatus(_A)
class _CnosPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CnosPortName_Type.__name__=_F
_CnosPortName_Object=MibTableColumn
cnosPortName=_CnosPortName_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,2),_CnosPortName_Type())
cnosPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosPortName.setStatus(_A)
class _CnosPortDuplexAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_CnosPortDuplexAdmin_Type.__name__=_C
_CnosPortDuplexAdmin_Object=MibTableColumn
cnosPortDuplexAdmin=_CnosPortDuplexAdmin_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,3),_CnosPortDuplexAdmin_Type())
cnosPortDuplexAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosPortDuplexAdmin.setStatus(_A)
class _CnosPortDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CnosPortDuplexStatus_Type.__name__=_C
_CnosPortDuplexStatus_Object=MibTableColumn
cnosPortDuplexStatus=_CnosPortDuplexStatus_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,4),_CnosPortDuplexStatus_Type())
cnosPortDuplexStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosPortDuplexStatus.setStatus(_A)
class _CnosPortSpeedAdmin_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_N,3)))
_CnosPortSpeedAdmin_Type.__name__=_C
_CnosPortSpeedAdmin_Object=MibTableColumn
cnosPortSpeedAdmin=_CnosPortSpeedAdmin_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,5),_CnosPortSpeedAdmin_Type())
cnosPortSpeedAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosPortSpeedAdmin.setStatus(_A)
class _CnosPortSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_CnosPortSpeedStatus_Type.__name__=_C
_CnosPortSpeedStatus_Object=MibTableColumn
cnosPortSpeedStatus=_CnosPortSpeedStatus_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,6),_CnosPortSpeedStatus_Type())
cnosPortSpeedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosPortSpeedStatus.setStatus(_A)
class _CnosPortMonitoring_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CnosPortMonitoring_Type.__name__=_C
_CnosPortMonitoring_Object=MibTableColumn
cnosPortMonitoring=_CnosPortMonitoring_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,7),_CnosPortMonitoring_Type())
cnosPortMonitoring.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosPortMonitoring.setStatus(_A)
class _CnosPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),('noLink',2)))
_CnosPortLinkStatus_Type.__name__=_C
_CnosPortLinkStatus_Object=MibTableColumn
cnosPortLinkStatus=_CnosPortLinkStatus_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,8),_CnosPortLinkStatus_Type())
cnosPortLinkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cnosPortLinkStatus.setStatus(_A)
class _CnosPortSTPPortFastMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CnosPortSTPPortFastMode_Type.__name__=_C
_CnosPortSTPPortFastMode_Object=MibTableColumn
cnosPortSTPPortFastMode=_CnosPortSTPPortFastMode_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,9),_CnosPortSTPPortFastMode_Type())
cnosPortSTPPortFastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosPortSTPPortFastMode.setStatus(_A)
class _CnosPortVlanMember_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('vlan1',1),('vlan2',2),('vlan3',3),('vlan4',4),('all',5)))
_CnosPortVlanMember_Type.__name__=_C
_CnosPortVlanMember_Object=MibTableColumn
cnosPortVlanMember=_CnosPortVlanMember_Object((1,3,6,1,4,1,9,10,43,1,3,1,1,10),_CnosPortVlanMember_Type())
cnosPortVlanMember.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosPortVlanMember.setStatus(_A)
_CnosVlan_ObjectIdentity=ObjectIdentity
cnosVlan=_CnosVlan_ObjectIdentity((1,3,6,1,4,1,9,10,43,1,4))
_CnosVlanTable_Object=MibTable
cnosVlanTable=_CnosVlanTable_Object((1,3,6,1,4,1,9,10,43,1,4,1))
if mibBuilder.loadTexts:cnosVlanTable.setStatus(_A)
_CnosVlanEntry_Object=MibTableRow
cnosVlanEntry=_CnosVlanEntry_Object((1,3,6,1,4,1,9,10,43,1,4,1,1))
cnosVlanEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cnosVlanEntry.setStatus(_A)
class _CnosVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CnosVlanIndex_Type.__name__=_C
_CnosVlanIndex_Object=MibTableColumn
cnosVlanIndex=_CnosVlanIndex_Object((1,3,6,1,4,1,9,10,43,1,4,1,1,1),_CnosVlanIndex_Type())
cnosVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnosVlanIndex.setStatus(_A)
class _CnosVlanSTPState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CnosVlanSTPState_Type.__name__=_C
_CnosVlanSTPState_Object=MibTableColumn
cnosVlanSTPState=_CnosVlanSTPState_Object((1,3,6,1,4,1,9,10,43,1,4,1,1,2),_CnosVlanSTPState_Type())
cnosVlanSTPState.setMaxAccess(_D)
if mibBuilder.loadTexts:cnosVlanSTPState.setStatus(_A)
_CiscoCNOSwitchNotifications_ObjectIdentity=ObjectIdentity
ciscoCNOSwitchNotifications=_CiscoCNOSwitchNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,43,2))
_CiscoCNOSwitchNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoCNOSwitchNotificationsPrefix=_CiscoCNOSwitchNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,43,2,0))
_CiscoCNOSwitchMIBComformance_ObjectIdentity=ObjectIdentity
ciscoCNOSwitchMIBComformance=_CiscoCNOSwitchMIBComformance_ObjectIdentity((1,3,6,1,4,1,9,10,43,3))
_CiscoCNOSwitchMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCNOSwitchMIBCompliances=_CiscoCNOSwitchMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,43,3,1))
_CiscoCNOSwitchMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCNOSwitchMIBGroups=_CiscoCNOSwitchMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,43,3,2))
ciscoCNOSwitchSysInfoGroup=ObjectGroup((1,3,6,1,4,1,9,10,43,3,2,1))
ciscoCNOSwitchSysInfoGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoCNOSwitchSysInfoGroup.setStatus(_A)
ciscoCNOSwitchConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,43,3,2,2))
ciscoCNOSwitchConfigGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoCNOSwitchConfigGroup.setStatus(_A)
ciscoCNOSwitchPortGroup=ObjectGroup((1,3,6,1,4,1,9,10,43,3,2,3))
ciscoCNOSwitchPortGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciscoCNOSwitchPortGroup.setStatus(_A)
ciscoCNOSwitchMonitorPortGroup=ObjectGroup((1,3,6,1,4,1,9,10,43,3,2,4))
ciscoCNOSwitchMonitorPortGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ciscoCNOSwitchMonitorPortGroup.setStatus(_A)
ciscoCNOSwitchVlanGroup=ObjectGroup((1,3,6,1,4,1,9,10,43,3,2,5))
ciscoCNOSwitchVlanGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ciscoCNOSwitchVlanGroup.setStatus(_A)
ciscoCNOSwitchCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,43,3,1,1))
ciscoCNOSwitchCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoCNOSwitchCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCNOSwitchMIB':ciscoCNOSwitchMIB,'ciscoCNOSwitchMIBObjects':ciscoCNOSwitchMIBObjects,'cnosSysInfo':cnosSysInfo,_R:cnosSysInfoSerialNo,_S:cnosSysInfoBoardRevision,_T:cnosSysInfoBootVersion,_U:cnosSysInfoAddrCapacity,'cnosSysConfig':cnosSysConfig,_V:cnosSysConfigReset,_W:cnosSysConfigDefaultReset,_f:cnosSysConfigMonitor,_g:cnosSysConfigMonitorPort,'cnosPort':cnosPort,'cnosPortTable':cnosPortTable,'cnosPortEntry':cnosPortEntry,_Y:cnosPortControllerRevision,_X:cnosPortName,_Z:cnosPortDuplexAdmin,_a:cnosPortDuplexStatus,_b:cnosPortSpeedAdmin,_c:cnosPortSpeedStatus,_h:cnosPortMonitoring,_d:cnosPortLinkStatus,_e:cnosPortSTPPortFastMode,_i:cnosPortVlanMember,'cnosVlan':cnosVlan,'cnosVlanTable':cnosVlanTable,'cnosVlanEntry':cnosVlanEntry,_Q:cnosVlanIndex,_j:cnosVlanSTPState,'ciscoCNOSwitchNotifications':ciscoCNOSwitchNotifications,'ciscoCNOSwitchNotificationsPrefix':ciscoCNOSwitchNotificationsPrefix,'ciscoCNOSwitchMIBComformance':ciscoCNOSwitchMIBComformance,'ciscoCNOSwitchMIBCompliances':ciscoCNOSwitchMIBCompliances,'ciscoCNOSwitchCompliance':ciscoCNOSwitchCompliance,'ciscoCNOSwitchMIBGroups':ciscoCNOSwitchMIBGroups,_k:ciscoCNOSwitchSysInfoGroup,_l:ciscoCNOSwitchConfigGroup,_m:ciscoCNOSwitchPortGroup,_n:ciscoCNOSwitchMonitorPortGroup,_o:ciscoCNOSwitchVlanGroup})