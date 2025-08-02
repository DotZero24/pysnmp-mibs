_e='cwpanNotificationGroup'
_d='cwpanNotificationControlGroup'
_c='cwpanInterfaceInfoGroup'
_b='cwpanHAFailureNotif'
_a='cwpanHAStateChangeNotif'
_Z='cwpanFallingIfRplTblMajorThreshNodesNotif'
_Y='cwpanRisingIfRplTblMajorThreshNodesNotif'
_X='cwpanFallingIfRplTblMinorThreshNodesNotif'
_W='cwpanRisingIfRplTblMinorThreshNodesNotif'
_V='cwpanRplTableResetNotif'
_U='cwpanServiceStatusChangeNotif'
_T='cwpanIfServiceStatus'
_S='read-write'
_R='unknown'
_Q='ifIndex'
_P='cwpanIfHAStandbyReady'
_O='cwpanIfHAStateChangeReason'
_N='cwpanNotificationEnable'
_M='cwpanIfHAFailureCode'
_L='cwpanIfHAState'
_K='cwpanIfRplTableResetReason'
_J='cwpanIfServiceStatusReason'
_I='cwpanIfRplTableMinorThreshNodes'
_H='cwpanIfRplTableMajorThreshNodes'
_G='cwpanIfRplTableNodes'
_F='Integer32'
_E='read-only'
_D='ifName'
_C='IF-MIB'
_B='current'
_A='CISCO-WPAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_C,_Q,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoWpanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,819))
if mibBuilder.loadTexts:ciscoWpanMIB.setRevisions(('2013-11-19 00:00',))
_CiscoWpanMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWpanMIBNotifs=_CiscoWpanMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,819,0))
_CiscoWpanMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWpanMIBObjects=_CiscoWpanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,819,1))
_CiscoWpanConfig_ObjectIdentity=ObjectIdentity
ciscoWpanConfig=_CiscoWpanConfig_ObjectIdentity((1,3,6,1,4,1,9,9,819,1,1))
_CwpanInterfaceTable_Object=MibTable
cwpanInterfaceTable=_CwpanInterfaceTable_Object((1,3,6,1,4,1,9,9,819,1,1,1))
if mibBuilder.loadTexts:cwpanInterfaceTable.setStatus(_B)
_CwpanInterfaceEntry_Object=MibTableRow
cwpanInterfaceEntry=_CwpanInterfaceEntry_Object((1,3,6,1,4,1,9,9,819,1,1,1,1))
cwpanInterfaceEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cwpanInterfaceEntry.setStatus(_B)
class _CwpanIfServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_CwpanIfServiceStatus_Type.__name__=_F
_CwpanIfServiceStatus_Object=MibTableColumn
cwpanIfServiceStatus=_CwpanIfServiceStatus_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,1),_CwpanIfServiceStatus_Type())
cwpanIfServiceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfServiceStatus.setStatus(_B)
class _CwpanIfServiceStatusReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_R,1),('powerDown',2),('powerUp',3),('moduleRemove',4),('moduleReload',5),('driverStop',6),('driverStart',7),('firmwareUpgrade',8),('firmwareReset',9),('watchDog',10)))
_CwpanIfServiceStatusReason_Type.__name__=_F
_CwpanIfServiceStatusReason_Object=MibTableColumn
cwpanIfServiceStatusReason=_CwpanIfServiceStatusReason_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,2),_CwpanIfServiceStatusReason_Type())
cwpanIfServiceStatusReason.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfServiceStatusReason.setStatus(_B)
class _CwpanIfRplTableResetReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('manuallyClear',2),('configChange',3),('interfaceDown',4),('timeout',5),('serviceStop',6)))
_CwpanIfRplTableResetReason_Type.__name__=_F
_CwpanIfRplTableResetReason_Object=MibTableColumn
cwpanIfRplTableResetReason=_CwpanIfRplTableResetReason_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,3),_CwpanIfRplTableResetReason_Type())
cwpanIfRplTableResetReason.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfRplTableResetReason.setStatus(_B)
_CwpanIfRplTableNodes_Type=Unsigned32
_CwpanIfRplTableNodes_Object=MibTableColumn
cwpanIfRplTableNodes=_CwpanIfRplTableNodes_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,4),_CwpanIfRplTableNodes_Type())
cwpanIfRplTableNodes.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfRplTableNodes.setStatus(_B)
_CwpanIfRplTableMajorThreshNodes_Type=Unsigned32
_CwpanIfRplTableMajorThreshNodes_Object=MibTableColumn
cwpanIfRplTableMajorThreshNodes=_CwpanIfRplTableMajorThreshNodes_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,5),_CwpanIfRplTableMajorThreshNodes_Type())
cwpanIfRplTableMajorThreshNodes.setMaxAccess(_S)
if mibBuilder.loadTexts:cwpanIfRplTableMajorThreshNodes.setStatus(_B)
_CwpanIfRplTableMinorThreshNodes_Type=Unsigned32
_CwpanIfRplTableMinorThreshNodes_Object=MibTableColumn
cwpanIfRplTableMinorThreshNodes=_CwpanIfRplTableMinorThreshNodes_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,6),_CwpanIfRplTableMinorThreshNodes_Type())
cwpanIfRplTableMinorThreshNodes.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfRplTableMinorThreshNodes.setStatus(_B)
class _CwpanIfHAState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('active',2),('standby',3)))
_CwpanIfHAState_Type.__name__=_F
_CwpanIfHAState_Object=MibTableColumn
cwpanIfHAState=_CwpanIfHAState_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,7),_CwpanIfHAState_Type())
cwpanIfHAState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfHAState.setStatus(_B)
class _CwpanIfHAFailureCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768)));namedValues=NamedValues(*(('registrationFailed',1),('sessionMismatch',2),('modeMismatch',4),('processEnableFail',8),('modeSetFail',16),('eui64SetFail',32),('eui64GetFail',64),('beaconVersionSetFail',128),('rplVersionSetFail',256),('neighbourSetFail',512),('sockCloseFail',1024),('peerConnectionFail',2048),('invalidEvent',4096),('prefixUpdateFail',8192),('standbyNotReady',16384),('configMismatch',32768)))
_CwpanIfHAFailureCode_Type.__name__=_F
_CwpanIfHAFailureCode_Object=MibTableColumn
cwpanIfHAFailureCode=_CwpanIfHAFailureCode_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,8),_CwpanIfHAFailureCode_Type())
cwpanIfHAFailureCode.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfHAFailureCode.setStatus(_B)
class _CwpanIfHAStateChangeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('automatic',2),('manual',3)))
_CwpanIfHAStateChangeReason_Type.__name__=_F
_CwpanIfHAStateChangeReason_Object=MibTableColumn
cwpanIfHAStateChangeReason=_CwpanIfHAStateChangeReason_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,9),_CwpanIfHAStateChangeReason_Type())
cwpanIfHAStateChangeReason.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfHAStateChangeReason.setStatus(_B)
class _CwpanIfHAStandbyReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_CwpanIfHAStandbyReady_Type.__name__=_F
_CwpanIfHAStandbyReady_Object=MibTableColumn
cwpanIfHAStandbyReady=_CwpanIfHAStandbyReady_Object((1,3,6,1,4,1,9,9,819,1,1,1,1,10),_CwpanIfHAStandbyReady_Type())
cwpanIfHAStandbyReady.setMaxAccess(_E)
if mibBuilder.loadTexts:cwpanIfHAStandbyReady.setStatus(_B)
_CwpanNotificationEnable_Type=TruthValue
_CwpanNotificationEnable_Object=MibScalar
cwpanNotificationEnable=_CwpanNotificationEnable_Object((1,3,6,1,4,1,9,9,819,1,1,2),_CwpanNotificationEnable_Type())
cwpanNotificationEnable.setMaxAccess(_S)
if mibBuilder.loadTexts:cwpanNotificationEnable.setStatus(_B)
_CiscoWpanMIBConform_ObjectIdentity=ObjectIdentity
ciscoWpanMIBConform=_CiscoWpanMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,819,2))
_CiscoWpanMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWpanMIBCompliances=_CiscoWpanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,819,2,1))
_CiscoWpanMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWpanMIBGroups=_CiscoWpanMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,819,2,2))
cwpanInterfaceInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,819,2,2,1))
cwpanInterfaceInfoGroup.setObjects(*((_A,_T),(_A,_J),(_A,_K),(_A,_G),(_A,_H),(_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cwpanInterfaceInfoGroup.setStatus(_B)
cwpanNotificationControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,819,2,2,2))
cwpanNotificationControlGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:cwpanNotificationControlGroup.setStatus(_B)
cwpanServiceStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,1))
cwpanServiceStatusChangeNotif.setObjects(*((_C,_D),(_A,_J)))
if mibBuilder.loadTexts:cwpanServiceStatusChangeNotif.setStatus(_B)
cwpanRplTableResetNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,2))
cwpanRplTableResetNotif.setObjects(*((_C,_D),(_A,_K)))
if mibBuilder.loadTexts:cwpanRplTableResetNotif.setStatus(_B)
cwpanRisingIfRplTblMinorThreshNodesNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,3))
cwpanRisingIfRplTblMinorThreshNodesNotif.setObjects(*((_C,_D),(_A,_G),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:cwpanRisingIfRplTblMinorThreshNodesNotif.setStatus(_B)
cwpanFallingIfRplTblMinorThreshNodesNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,4))
cwpanFallingIfRplTblMinorThreshNodesNotif.setObjects(*((_C,_D),(_A,_G),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:cwpanFallingIfRplTblMinorThreshNodesNotif.setStatus(_B)
cwpanRisingIfRplTblMajorThreshNodesNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,5))
cwpanRisingIfRplTblMajorThreshNodesNotif.setObjects(*((_C,_D),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cwpanRisingIfRplTblMajorThreshNodesNotif.setStatus(_B)
cwpanFallingIfRplTblMajorThreshNodesNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,6))
cwpanFallingIfRplTblMajorThreshNodesNotif.setObjects(*((_C,_D),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cwpanFallingIfRplTblMajorThreshNodesNotif.setStatus(_B)
cwpanHAStateChangeNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,7))
cwpanHAStateChangeNotif.setObjects(*((_C,_D),(_A,_P),(_A,_O),(_A,_L)))
if mibBuilder.loadTexts:cwpanHAStateChangeNotif.setStatus(_B)
cwpanHAFailureNotif=NotificationType((1,3,6,1,4,1,9,9,819,0,8))
cwpanHAFailureNotif.setObjects(*((_C,_D),(_A,_M)))
if mibBuilder.loadTexts:cwpanHAFailureNotif.setStatus(_B)
cwpanNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,819,2,2,3))
cwpanNotificationGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cwpanNotificationGroup.setStatus(_B)
ciscoWpanMIBModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,819,2,1,1))
ciscoWpanMIBModuleCompliance.setObjects(*((_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoWpanMIBModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWpanMIB':ciscoWpanMIB,'ciscoWpanMIBNotifs':ciscoWpanMIBNotifs,_U:cwpanServiceStatusChangeNotif,_V:cwpanRplTableResetNotif,_W:cwpanRisingIfRplTblMinorThreshNodesNotif,_X:cwpanFallingIfRplTblMinorThreshNodesNotif,_Y:cwpanRisingIfRplTblMajorThreshNodesNotif,_Z:cwpanFallingIfRplTblMajorThreshNodesNotif,_a:cwpanHAStateChangeNotif,_b:cwpanHAFailureNotif,'ciscoWpanMIBObjects':ciscoWpanMIBObjects,'ciscoWpanConfig':ciscoWpanConfig,'cwpanInterfaceTable':cwpanInterfaceTable,'cwpanInterfaceEntry':cwpanInterfaceEntry,_T:cwpanIfServiceStatus,_J:cwpanIfServiceStatusReason,_K:cwpanIfRplTableResetReason,_G:cwpanIfRplTableNodes,_H:cwpanIfRplTableMajorThreshNodes,_I:cwpanIfRplTableMinorThreshNodes,_L:cwpanIfHAState,_M:cwpanIfHAFailureCode,_O:cwpanIfHAStateChangeReason,_P:cwpanIfHAStandbyReady,_N:cwpanNotificationEnable,'ciscoWpanMIBConform':ciscoWpanMIBConform,'ciscoWpanMIBCompliances':ciscoWpanMIBCompliances,'ciscoWpanMIBModuleCompliance':ciscoWpanMIBModuleCompliance,'ciscoWpanMIBGroups':ciscoWpanMIBGroups,_c:cwpanInterfaceInfoGroup,_d:cwpanNotificationControlGroup,_e:cwpanNotificationGroup})