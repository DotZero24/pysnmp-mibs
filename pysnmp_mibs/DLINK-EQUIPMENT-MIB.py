_M='master'
_L='stand-alone'
_K='swUnitMgmtId'
_J='OctetString'
_I='swPowerStatus'
_H='other'
_G='DisplayString'
_F='swPowerID'
_E='swPowerUnitIndex'
_D='DLINK-EQUIPMENT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentNotifyLevel,dlink_common_mgmt=mibBuilder.importSymbols('DLINK-ID-REC-MIB','AgentNotifyLevel','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention','TruthValue')
swDlinkEquipmentMIB=ModuleIdentity((1,3,6,1,4,1,171,12,11))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwDlinkEquipmentMib_ObjectIdentity=ObjectIdentity
swDlinkEquipmentMib=_SwDlinkEquipmentMib_ObjectIdentity((1,3,6,1,4,1,171,12,11,1))
class _SwDlinkEquipmentCapacity_Type(Bits):namedValues=NamedValues(*(('fanCapable',0),('redundantPowerCapable',1),('tempteratureDetection',2),('stackingCapable',3),('chassisCapable',4)))
_SwDlinkEquipmentCapacity_Type.__name__='Bits'
_SwDlinkEquipmentCapacity_Object=MibScalar
swDlinkEquipmentCapacity=_SwDlinkEquipmentCapacity_Object((1,3,6,1,4,1,171,12,11,1,1),_SwDlinkEquipmentCapacity_Type())
swDlinkEquipmentCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:swDlinkEquipmentCapacity.setStatus(_A)
_SwPowerTable_Object=MibTable
swPowerTable=_SwPowerTable_Object((1,3,6,1,4,1,171,12,11,1,6))
if mibBuilder.loadTexts:swPowerTable.setStatus(_A)
_SwPowerEntry_Object=MibTableRow
swPowerEntry=_SwPowerEntry_Object((1,3,6,1,4,1,171,12,11,1,6,1))
swPowerEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:swPowerEntry.setStatus(_A)
class _SwPowerUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPowerUnitIndex_Type.__name__=_C
_SwPowerUnitIndex_Object=MibTableColumn
swPowerUnitIndex=_SwPowerUnitIndex_Object((1,3,6,1,4,1,171,12,11,1,6,1,1),_SwPowerUnitIndex_Type())
swPowerUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swPowerUnitIndex.setStatus(_A)
class _SwPowerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPowerID_Type.__name__=_C
_SwPowerID_Object=MibTableColumn
swPowerID=_SwPowerID_Object((1,3,6,1,4,1,171,12,11,1,6,1,2),_SwPowerID_Type())
swPowerID.setMaxAccess(_B)
if mibBuilder.loadTexts:swPowerID.setStatus(_A)
class _SwPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),('lowVoltage',1),('overCurrent',2),('working',3),('fail',4),('connect',5),('disconnect',6)))
_SwPowerStatus_Type.__name__=_C
_SwPowerStatus_Object=MibTableColumn
swPowerStatus=_SwPowerStatus_Object((1,3,6,1,4,1,171,12,11,1,6,1,3),_SwPowerStatus_Type())
swPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swPowerStatus.setStatus(_A)
_SwUnitMgmt_ObjectIdentity=ObjectIdentity
swUnitMgmt=_SwUnitMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,9))
class _SwUnitStackingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitStackingVersion_Type.__name__=_C
_SwUnitStackingVersion_Object=MibScalar
swUnitStackingVersion=_SwUnitStackingVersion_Object((1,3,6,1,4,1,171,12,11,1,9,1),_SwUnitStackingVersion_Type())
swUnitStackingVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitStackingVersion.setStatus(_A)
class _SwUnitMaxSupportedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitMaxSupportedUnits_Type.__name__=_C
_SwUnitMaxSupportedUnits_Object=MibScalar
swUnitMaxSupportedUnits=_SwUnitMaxSupportedUnits_Object((1,3,6,1,4,1,171,12,11,1,9,2),_SwUnitMaxSupportedUnits_Type())
swUnitMaxSupportedUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMaxSupportedUnits.setStatus(_A)
class _SwUnitNumOfUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitNumOfUnit_Type.__name__=_C
_SwUnitNumOfUnit_Object=MibScalar
swUnitNumOfUnit=_SwUnitNumOfUnit_Object((1,3,6,1,4,1,171,12,11,1,9,3),_SwUnitNumOfUnit_Type())
swUnitNumOfUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitNumOfUnit.setStatus(_A)
_SwUnitMgmtTable_Object=MibTable
swUnitMgmtTable=_SwUnitMgmtTable_Object((1,3,6,1,4,1,171,12,11,1,9,4))
if mibBuilder.loadTexts:swUnitMgmtTable.setStatus(_A)
_SwUnitMgmtEntry_Object=MibTableRow
swUnitMgmtEntry=_SwUnitMgmtEntry_Object((1,3,6,1,4,1,171,12,11,1,9,4,1))
swUnitMgmtEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:swUnitMgmtEntry.setStatus(_A)
class _SwUnitMgmtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_SwUnitMgmtId_Type.__name__=_C
_SwUnitMgmtId_Object=MibTableColumn
swUnitMgmtId=_SwUnitMgmtId_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,1),_SwUnitMgmtId_Type())
swUnitMgmtId.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtId.setStatus(_A)
_SwUnitMgmtMacAddr_Type=MacAddress
_SwUnitMgmtMacAddr_Object=MibTableColumn
swUnitMgmtMacAddr=_SwUnitMgmtMacAddr_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,2),_SwUnitMgmtMacAddr_Type())
swUnitMgmtMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtMacAddr.setStatus(_A)
class _SwUnitMgmtStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwUnitMgmtStartPort_Type.__name__=_C
_SwUnitMgmtStartPort_Object=MibTableColumn
swUnitMgmtStartPort=_SwUnitMgmtStartPort_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,3),_SwUnitMgmtStartPort_Type())
swUnitMgmtStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtStartPort.setStatus(_A)
class _SwUnitMgmtPortRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitMgmtPortRange_Type.__name__=_C
_SwUnitMgmtPortRange_Object=MibTableColumn
swUnitMgmtPortRange=_SwUnitMgmtPortRange_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,4),_SwUnitMgmtPortRange_Type())
swUnitMgmtPortRange.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtPortRange.setStatus(_A)
class _SwUnitMgmtFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwUnitMgmtFrontPanelLedStatus_Type.__name__=_J
_SwUnitMgmtFrontPanelLedStatus_Object=MibTableColumn
swUnitMgmtFrontPanelLedStatus=_SwUnitMgmtFrontPanelLedStatus_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,5),_SwUnitMgmtFrontPanelLedStatus_Type())
swUnitMgmtFrontPanelLedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtFrontPanelLedStatus.setStatus(_A)
class _SwUnitMgmtCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('auto',2),(_L,3),(_M,4),('slave',5)))
_SwUnitMgmtCtrlMode_Type.__name__=_C
_SwUnitMgmtCtrlMode_Object=MibTableColumn
swUnitMgmtCtrlMode=_SwUnitMgmtCtrlMode_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,6),_SwUnitMgmtCtrlMode_Type())
swUnitMgmtCtrlMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:swUnitMgmtCtrlMode.setStatus(_A)
class _SwUnitMgmtCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('auto',2),(_L,3),(_M,4),('slave',5)))
_SwUnitMgmtCurrentMode_Type.__name__=_C
_SwUnitMgmtCurrentMode_Object=MibTableColumn
swUnitMgmtCurrentMode=_SwUnitMgmtCurrentMode_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,7),_SwUnitMgmtCurrentMode_Type())
swUnitMgmtCurrentMode.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtCurrentMode.setStatus(_A)
class _SwUnitMgmtVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwUnitMgmtVersion_Type.__name__=_G
_SwUnitMgmtVersion_Object=MibTableColumn
swUnitMgmtVersion=_SwUnitMgmtVersion_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,8),_SwUnitMgmtVersion_Type())
swUnitMgmtVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtVersion.setStatus(_A)
class _SwUnitMgmtModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwUnitMgmtModuleName_Type.__name__=_G
_SwUnitMgmtModuleName_Object=MibTableColumn
swUnitMgmtModuleName=_SwUnitMgmtModuleName_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,9),_SwUnitMgmtModuleName_Type())
swUnitMgmtModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:swUnitMgmtModuleName.setStatus(_A)
_SwDlinkEquipmentNotify_ObjectIdentity=ObjectIdentity
swDlinkEquipmentNotify=_SwDlinkEquipmentNotify_ObjectIdentity((1,3,6,1,4,1,171,12,11,2))
_SwEquipmentNotification_ObjectIdentity=ObjectIdentity
swEquipmentNotification=_SwEquipmentNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2))
_SwEquipPowerNotification_ObjectIdentity=ObjectIdentity
swEquipPowerNotification=_SwEquipPowerNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,2))
_SwEquipPowerNotifyPerfix_ObjectIdentity=ObjectIdentity
swEquipPowerNotifyPerfix=_SwEquipPowerNotifyPerfix_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,2,0))
_SwNotificationBindings_ObjectIdentity=ObjectIdentity
swNotificationBindings=_SwNotificationBindings_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,3))
swPowerFailure=NotificationType((1,3,6,1,4,1,171,12,11,2,2,2,0,2))
swPowerFailure.setObjects(*((_D,_E),(_D,_F),(_D,_I)))
if mibBuilder.loadTexts:swPowerFailure.setStatus(_A)
swPowerRecover=NotificationType((1,3,6,1,4,1,171,12,11,2,2,2,0,3))
swPowerRecover.setObjects(*((_D,_E),(_D,_F),(_D,_I)))
if mibBuilder.loadTexts:swPowerRecover.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'swDlinkEquipmentMIB':swDlinkEquipmentMIB,'swDlinkEquipmentMib':swDlinkEquipmentMib,'swDlinkEquipmentCapacity':swDlinkEquipmentCapacity,'swPowerTable':swPowerTable,'swPowerEntry':swPowerEntry,_E:swPowerUnitIndex,_F:swPowerID,_I:swPowerStatus,'swUnitMgmt':swUnitMgmt,'swUnitStackingVersion':swUnitStackingVersion,'swUnitMaxSupportedUnits':swUnitMaxSupportedUnits,'swUnitNumOfUnit':swUnitNumOfUnit,'swUnitMgmtTable':swUnitMgmtTable,'swUnitMgmtEntry':swUnitMgmtEntry,_K:swUnitMgmtId,'swUnitMgmtMacAddr':swUnitMgmtMacAddr,'swUnitMgmtStartPort':swUnitMgmtStartPort,'swUnitMgmtPortRange':swUnitMgmtPortRange,'swUnitMgmtFrontPanelLedStatus':swUnitMgmtFrontPanelLedStatus,'swUnitMgmtCtrlMode':swUnitMgmtCtrlMode,'swUnitMgmtCurrentMode':swUnitMgmtCurrentMode,'swUnitMgmtVersion':swUnitMgmtVersion,'swUnitMgmtModuleName':swUnitMgmtModuleName,'swDlinkEquipmentNotify':swDlinkEquipmentNotify,'swEquipmentNotification':swEquipmentNotification,'swEquipPowerNotification':swEquipPowerNotification,'swEquipPowerNotifyPerfix':swEquipPowerNotifyPerfix,'swPowerFailure':swPowerFailure,'swPowerRecover':swPowerRecover,'swNotificationBindings':swNotificationBindings})