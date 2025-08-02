_J='wwpLeosPhyBladePostCode'
_I='wwpLeosBladeOperState'
_H='read-create'
_G='read-write'
_F='DisplayString'
_E='wwpLeosBladeId'
_D='WWP-LEOS-BLADE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosBladeMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,1))
if mibBuilder.loadTexts:wwpLeosBladeMIB.setRevisions(('2011-10-19 00:00','2002-03-16 00:00'))
_WwpLeosBladeMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosBladeMIBObjects=_WwpLeosBladeMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,1))
_WwpLeosBlade_ObjectIdentity=ObjectIdentity
wwpLeosBlade=_WwpLeosBlade_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,1,1))
_WwpLeosBladeTable_Object=MibTable
wwpLeosBladeTable=_WwpLeosBladeTable_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1))
if mibBuilder.loadTexts:wwpLeosBladeTable.setStatus(_A)
_WwpLeosBladeEntry_Object=MibTableRow
wwpLeosBladeEntry=_WwpLeosBladeEntry_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1))
wwpLeosBladeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wwpLeosBladeEntry.setStatus(_A)
class _WwpLeosBladeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosBladeId_Type.__name__=_C
_WwpLeosBladeId_Object=MibTableColumn
wwpLeosBladeId=_WwpLeosBladeId_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,1),_WwpLeosBladeId_Type())
wwpLeosBladeId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBladeId.setStatus(_A)
class _WwpLeosBladeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('control',1),('io',2),('fabric',3),('single',4)))
_WwpLeosBladeType_Type.__name__=_C
_WwpLeosBladeType_Object=MibTableColumn
wwpLeosBladeType=_WwpLeosBladeType_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,2),_WwpLeosBladeType_Type())
wwpLeosBladeType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBladeType.setStatus(_A)
_WwpLeosBladeCapFilename_Type=DisplayString
_WwpLeosBladeCapFilename_Object=MibTableColumn
wwpLeosBladeCapFilename=_WwpLeosBladeCapFilename_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,3),_WwpLeosBladeCapFilename_Type())
wwpLeosBladeCapFilename.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosBladeCapFilename.setStatus(_A)
class _WwpLeosBladeAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpLeosBladeAdminState_Type.__name__=_C
_WwpLeosBladeAdminState_Object=MibTableColumn
wwpLeosBladeAdminState=_WwpLeosBladeAdminState_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,4),_WwpLeosBladeAdminState_Type())
wwpLeosBladeAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosBladeAdminState.setStatus(_A)
class _WwpLeosBladeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('init',1),('enabled',2),('disabled',3),('faulted',4),('unequipped',5)))
_WwpLeosBladeOperState_Type.__name__=_C
_WwpLeosBladeOperState_Object=MibTableColumn
wwpLeosBladeOperState=_WwpLeosBladeOperState_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,5),_WwpLeosBladeOperState_Type())
wwpLeosBladeOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBladeOperState.setStatus(_A)
_WwpLeosBladeStartMacAddr_Type=MacAddress
_WwpLeosBladeStartMacAddr_Object=MibTableColumn
wwpLeosBladeStartMacAddr=_WwpLeosBladeStartMacAddr_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,6),_WwpLeosBladeStartMacAddr_Type())
wwpLeosBladeStartMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBladeStartMacAddr.setStatus(_A)
class _WwpLeosBladeNumPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosBladeNumPorts_Type.__name__=_C
_WwpLeosBladeNumPorts_Object=MibTableColumn
wwpLeosBladeNumPorts=_WwpLeosBladeNumPorts_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,7),_WwpLeosBladeNumPorts_Type())
wwpLeosBladeNumPorts.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpLeosBladeNumPorts.setStatus(_A)
_WwpLeosBladeStatus_Type=RowStatus
_WwpLeosBladeStatus_Object=MibTableColumn
wwpLeosBladeStatus=_WwpLeosBladeStatus_Object((1,3,6,1,4,1,6141,2,60,1,1,1,1,1,8),_WwpLeosBladeStatus_Type())
wwpLeosBladeStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpLeosBladeStatus.setStatus(_A)
_WwpLeosPhyBladeTable_Object=MibTable
wwpLeosPhyBladeTable=_WwpLeosPhyBladeTable_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2))
if mibBuilder.loadTexts:wwpLeosPhyBladeTable.setStatus(_A)
_WwpLeosPhyBladeEntry_Object=MibTableRow
wwpLeosPhyBladeEntry=_WwpLeosPhyBladeEntry_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1))
wwpLeosPhyBladeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wwpLeosPhyBladeEntry.setStatus(_A)
_WwpLeosPhyBladeSysUpTime_Type=TimeTicks
_WwpLeosPhyBladeSysUpTime_Object=MibTableColumn
wwpLeosPhyBladeSysUpTime=_WwpLeosPhyBladeSysUpTime_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,1),_WwpLeosPhyBladeSysUpTime_Type())
wwpLeosPhyBladeSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeSysUpTime.setStatus(_A)
class _WwpLeosPhyBladeSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosPhyBladeSerialNum_Type.__name__=_F
_WwpLeosPhyBladeSerialNum_Object=MibTableColumn
wwpLeosPhyBladeSerialNum=_WwpLeosPhyBladeSerialNum_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,2),_WwpLeosPhyBladeSerialNum_Type())
wwpLeosPhyBladeSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeSerialNum.setStatus(_A)
class _WwpLeosPhyBladeBoardRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosPhyBladeBoardRevision_Type.__name__=_F
_WwpLeosPhyBladeBoardRevision_Object=MibTableColumn
wwpLeosPhyBladeBoardRevision=_WwpLeosPhyBladeBoardRevision_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,3),_WwpLeosPhyBladeBoardRevision_Type())
wwpLeosPhyBladeBoardRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeBoardRevision.setStatus(_A)
_WwpLeosPhyBladePostResults_Type=DisplayString
_WwpLeosPhyBladePostResults_Object=MibTableColumn
wwpLeosPhyBladePostResults=_WwpLeosPhyBladePostResults_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,4),_WwpLeosPhyBladePostResults_Type())
wwpLeosPhyBladePostResults.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladePostResults.setStatus(_A)
_WwpLeosPhyBladePostCode_Type=Unsigned32
_WwpLeosPhyBladePostCode_Object=MibTableColumn
wwpLeosPhyBladePostCode=_WwpLeosPhyBladePostCode_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,5),_WwpLeosPhyBladePostCode_Type())
wwpLeosPhyBladePostCode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladePostCode.setStatus(_A)
_WwpLeosPhyBladeMfgDate_Type=DateAndTime
_WwpLeosPhyBladeMfgDate_Object=MibTableColumn
wwpLeosPhyBladeMfgDate=_WwpLeosPhyBladeMfgDate_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,6),_WwpLeosPhyBladeMfgDate_Type())
wwpLeosPhyBladeMfgDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeMfgDate.setStatus(_A)
_WwpLeosPhyBladeBoardDesc_Type=DisplayString
_WwpLeosPhyBladeBoardDesc_Object=MibTableColumn
wwpLeosPhyBladeBoardDesc=_WwpLeosPhyBladeBoardDesc_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,7),_WwpLeosPhyBladeBoardDesc_Type())
wwpLeosPhyBladeBoardDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeBoardDesc.setStatus(_A)
_WwpLeosPhyBladeNumResets_Type=Unsigned32
_WwpLeosPhyBladeNumResets_Object=MibTableColumn
wwpLeosPhyBladeNumResets=_WwpLeosPhyBladeNumResets_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,8),_WwpLeosPhyBladeNumResets_Type())
wwpLeosPhyBladeNumResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeNumResets.setStatus(_A)
class _WwpLeosPhyBladeLastRebootReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('unknown',1),('snmp',2),('pwrFail',3),('appLoad',4),('errorHandler',5),('watchdog',6),('upgrade',7),('cli',8),('resetButton',9),('serviceModeChange',10),('guardianReboot',11),('guardianSaosRestart',12)))
_WwpLeosPhyBladeLastRebootReason_Type.__name__=_C
_WwpLeosPhyBladeLastRebootReason_Object=MibTableColumn
wwpLeosPhyBladeLastRebootReason=_WwpLeosPhyBladeLastRebootReason_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,9),_WwpLeosPhyBladeLastRebootReason_Type())
wwpLeosPhyBladeLastRebootReason.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPhyBladeLastRebootReason.setStatus(_A)
class _WwpLeosPhyBladeRebootOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('reboot',2),('rebootReinit',3),('rebootCustReinit',4)))
_WwpLeosPhyBladeRebootOperation_Type.__name__=_C
_WwpLeosPhyBladeRebootOperation_Object=MibTableColumn
wwpLeosPhyBladeRebootOperation=_WwpLeosPhyBladeRebootOperation_Object((1,3,6,1,4,1,6141,2,60,1,1,1,2,1,10),_WwpLeosPhyBladeRebootOperation_Type())
wwpLeosPhyBladeRebootOperation.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPhyBladeRebootOperation.setStatus(_A)
_WwpLeosBladeMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosBladeMIBNotificationPrefix=_WwpLeosBladeMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,2))
_WwpLeosBladeMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosBladeMIBNotifications=_WwpLeosBladeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,2,0))
_WwpLeosBladeMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosBladeMIBConformance=_WwpLeosBladeMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,3))
_WwpLeosBladeMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosBladeMIBCompliances=_WwpLeosBladeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,3,1))
_WwpLeosBladeMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosBladeMIBGroups=_WwpLeosBladeMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,1,3,2))
wwpLeosBladeStateChange=NotificationType((1,3,6,1,4,1,6141,2,60,1,2,0,1))
wwpLeosBladeStateChange.setObjects(*((_D,_E),(_D,_I)))
if mibBuilder.loadTexts:wwpLeosBladeStateChange.setStatus(_A)
wwpLeosBladePostFail=NotificationType((1,3,6,1,4,1,6141,2,60,1,2,0,2))
wwpLeosBladePostFail.setObjects(*((_D,_E),(_D,_J)))
if mibBuilder.loadTexts:wwpLeosBladePostFail.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpLeosBladeMIB':wwpLeosBladeMIB,'wwpLeosBladeMIBObjects':wwpLeosBladeMIBObjects,'wwpLeosBlade':wwpLeosBlade,'wwpLeosBladeTable':wwpLeosBladeTable,'wwpLeosBladeEntry':wwpLeosBladeEntry,_E:wwpLeosBladeId,'wwpLeosBladeType':wwpLeosBladeType,'wwpLeosBladeCapFilename':wwpLeosBladeCapFilename,'wwpLeosBladeAdminState':wwpLeosBladeAdminState,_I:wwpLeosBladeOperState,'wwpLeosBladeStartMacAddr':wwpLeosBladeStartMacAddr,'wwpLeosBladeNumPorts':wwpLeosBladeNumPorts,'wwpLeosBladeStatus':wwpLeosBladeStatus,'wwpLeosPhyBladeTable':wwpLeosPhyBladeTable,'wwpLeosPhyBladeEntry':wwpLeosPhyBladeEntry,'wwpLeosPhyBladeSysUpTime':wwpLeosPhyBladeSysUpTime,'wwpLeosPhyBladeSerialNum':wwpLeosPhyBladeSerialNum,'wwpLeosPhyBladeBoardRevision':wwpLeosPhyBladeBoardRevision,'wwpLeosPhyBladePostResults':wwpLeosPhyBladePostResults,_J:wwpLeosPhyBladePostCode,'wwpLeosPhyBladeMfgDate':wwpLeosPhyBladeMfgDate,'wwpLeosPhyBladeBoardDesc':wwpLeosPhyBladeBoardDesc,'wwpLeosPhyBladeNumResets':wwpLeosPhyBladeNumResets,'wwpLeosPhyBladeLastRebootReason':wwpLeosPhyBladeLastRebootReason,'wwpLeosPhyBladeRebootOperation':wwpLeosPhyBladeRebootOperation,'wwpLeosBladeMIBNotificationPrefix':wwpLeosBladeMIBNotificationPrefix,'wwpLeosBladeMIBNotifications':wwpLeosBladeMIBNotifications,'wwpLeosBladeStateChange':wwpLeosBladeStateChange,'wwpLeosBladePostFail':wwpLeosBladePostFail,'wwpLeosBladeMIBConformance':wwpLeosBladeMIBConformance,'wwpLeosBladeMIBCompliances':wwpLeosBladeMIBCompliances,'wwpLeosBladeMIBGroups':wwpLeosBladeMIBGroups})