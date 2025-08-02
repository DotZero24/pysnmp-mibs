_T='osDevNotificationsGroup'
_S='osDevMandatoryGroup'
_R='osDevModuleLedConnOff'
_Q='osDevModuleLedConnOn'
_P='osDevModuleLedWanOff'
_O='osDevModuleLedWanOn'
_N='osDevModuleLedPowerOff'
_M='osDevModuleLedPowerOn'
_L='osDevModuleRemoved'
_K='osDevModuleInserted'
_J='osDevSerialAdminBaudrate'
_I='osDevSerialOperBaudrate'
_H='osDevSerialNumber'
_G='osDevSerialIndex'
_F='Integer32'
_E='read-only'
_D='osDevModuleType'
_C='osDevModuleSlotNumber'
_B='current'
_A='OS-DEVICE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osDevice=ModuleIdentity((1,3,6,1,4,1,6926,2,40))
if mibBuilder.loadTexts:osDevice.setRevisions(('2019-04-04 00:00','2016-09-14 00:00'))
class DevModuleType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('lte0',2),('vdsl0',3)))
class SerialBaudRate(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9600,9600),ValueRangeConstraint(115200,115200))
_OsDevNotifications_ObjectIdentity=ObjectIdentity
osDevNotifications=_OsDevNotifications_ObjectIdentity((1,3,6,1,4,1,6926,2,40,0))
_OsDevModule_ObjectIdentity=ObjectIdentity
osDevModule=_OsDevModule_ObjectIdentity((1,3,6,1,4,1,6926,2,40,1))
_OsDevModuleType_Type=DevModuleType
_OsDevModuleType_Object=MibScalar
osDevModuleType=_OsDevModuleType_Object((1,3,6,1,4,1,6926,2,40,1,1),_OsDevModuleType_Type())
osDevModuleType.setMaxAccess(_E)
if mibBuilder.loadTexts:osDevModuleType.setStatus(_B)
class _OsDevModuleSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_OsDevModuleSlotNumber_Type.__name__=_F
_OsDevModuleSlotNumber_Object=MibScalar
osDevModuleSlotNumber=_OsDevModuleSlotNumber_Object((1,3,6,1,4,1,6926,2,40,1,2),_OsDevModuleSlotNumber_Type())
osDevModuleSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:osDevModuleSlotNumber.setStatus(_B)
_OsDevParams_ObjectIdentity=ObjectIdentity
osDevParams=_OsDevParams_ObjectIdentity((1,3,6,1,4,1,6926,2,40,2))
_OsDevSerial_ObjectIdentity=ObjectIdentity
osDevSerial=_OsDevSerial_ObjectIdentity((1,3,6,1,4,1,6926,2,40,2,1))
_OsDevSerialNumber_Type=Integer32
_OsDevSerialNumber_Object=MibScalar
osDevSerialNumber=_OsDevSerialNumber_Object((1,3,6,1,4,1,6926,2,40,2,1,1),_OsDevSerialNumber_Type())
osDevSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:osDevSerialNumber.setStatus(_B)
_OsDevSerialTable_Object=MibTable
osDevSerialTable=_OsDevSerialTable_Object((1,3,6,1,4,1,6926,2,40,2,1,2))
if mibBuilder.loadTexts:osDevSerialTable.setStatus(_B)
_OsDevSerialEntry_Object=MibTableRow
osDevSerialEntry=_OsDevSerialEntry_Object((1,3,6,1,4,1,6926,2,40,2,1,2,1))
osDevSerialEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:osDevSerialEntry.setStatus(_B)
_OsDevSerialIndex_Type=Unsigned32
_OsDevSerialIndex_Object=MibTableColumn
osDevSerialIndex=_OsDevSerialIndex_Object((1,3,6,1,4,1,6926,2,40,2,1,2,1,1),_OsDevSerialIndex_Type())
osDevSerialIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osDevSerialIndex.setStatus(_B)
_OsDevSerialOperBaudrate_Type=SerialBaudRate
_OsDevSerialOperBaudrate_Object=MibTableColumn
osDevSerialOperBaudrate=_OsDevSerialOperBaudrate_Object((1,3,6,1,4,1,6926,2,40,2,1,2,1,2),_OsDevSerialOperBaudrate_Type())
osDevSerialOperBaudrate.setMaxAccess(_E)
if mibBuilder.loadTexts:osDevSerialOperBaudrate.setStatus(_B)
_OsDevSerialAdminBaudrate_Type=SerialBaudRate
_OsDevSerialAdminBaudrate_Object=MibTableColumn
osDevSerialAdminBaudrate=_OsDevSerialAdminBaudrate_Object((1,3,6,1,4,1,6926,2,40,2,1,2,1,3),_OsDevSerialAdminBaudrate_Type())
osDevSerialAdminBaudrate.setMaxAccess('read-write')
if mibBuilder.loadTexts:osDevSerialAdminBaudrate.setStatus(_B)
_OsDevConformance_ObjectIdentity=ObjectIdentity
osDevConformance=_OsDevConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,40,101))
_OsDevMIBCompliances_ObjectIdentity=ObjectIdentity
osDevMIBCompliances=_OsDevMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,40,101,1))
_OsDevMIBGroups_ObjectIdentity=ObjectIdentity
osDevMIBGroups=_OsDevMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,40,101,2))
osDevMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,40,101,2,1))
osDevMandatoryGroup.setObjects(*((_A,_C),(_A,_D),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:osDevMandatoryGroup.setStatus(_B)
osDevModuleInserted=NotificationType((1,3,6,1,4,1,6926,2,40,0,1))
osDevModuleInserted.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleInserted.setStatus(_B)
osDevModuleRemoved=NotificationType((1,3,6,1,4,1,6926,2,40,0,2))
osDevModuleRemoved.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleRemoved.setStatus(_B)
osDevModuleLedPowerOn=NotificationType((1,3,6,1,4,1,6926,2,40,0,3))
osDevModuleLedPowerOn.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleLedPowerOn.setStatus(_B)
osDevModuleLedPowerOff=NotificationType((1,3,6,1,4,1,6926,2,40,0,4))
osDevModuleLedPowerOff.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleLedPowerOff.setStatus(_B)
osDevModuleLedWanOn=NotificationType((1,3,6,1,4,1,6926,2,40,0,5))
osDevModuleLedWanOn.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleLedWanOn.setStatus(_B)
osDevModuleLedWanOff=NotificationType((1,3,6,1,4,1,6926,2,40,0,6))
osDevModuleLedWanOff.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleLedWanOff.setStatus(_B)
osDevModuleLedConnOn=NotificationType((1,3,6,1,4,1,6926,2,40,0,7))
osDevModuleLedConnOn.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleLedConnOn.setStatus(_B)
osDevModuleLedConnOff=NotificationType((1,3,6,1,4,1,6926,2,40,0,8))
osDevModuleLedConnOff.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:osDevModuleLedConnOff.setStatus(_B)
osDevNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6926,2,40,101,2,2))
osDevNotificationsGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:osDevNotificationsGroup.setStatus(_B)
osDevMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,40,101,1,1))
osDevMIBCompliance.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:osDevMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DevModuleType':DevModuleType,'SerialBaudRate':SerialBaudRate,'osDevice':osDevice,'osDevNotifications':osDevNotifications,_K:osDevModuleInserted,_L:osDevModuleRemoved,_M:osDevModuleLedPowerOn,_N:osDevModuleLedPowerOff,_O:osDevModuleLedWanOn,_P:osDevModuleLedWanOff,_Q:osDevModuleLedConnOn,_R:osDevModuleLedConnOff,'osDevModule':osDevModule,_D:osDevModuleType,_C:osDevModuleSlotNumber,'osDevParams':osDevParams,'osDevSerial':osDevSerial,_H:osDevSerialNumber,'osDevSerialTable':osDevSerialTable,'osDevSerialEntry':osDevSerialEntry,_G:osDevSerialIndex,_I:osDevSerialOperBaudrate,_J:osDevSerialAdminBaudrate,'osDevConformance':osDevConformance,'osDevMIBCompliances':osDevMIBCompliances,'osDevMIBCompliance':osDevMIBCompliance,'osDevMIBGroups':osDevMIBGroups,_S:osDevMandatoryGroup,_T:osDevNotificationsGroup})