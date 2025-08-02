_K='sysName'
_J='SNMPv2-MIB'
_I='adTrapInformSeqNum'
_H='ADTRAN-GENTRAPINFORM-MIB'
_G='read-write'
_F='adGenAccessoryModuleIndex'
_E='adGenAccessoryIndex'
_D='Integer32'
_C='ADTRAN-GENMAX-ACCESSORY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTrapInformSeqNum,=mibBuilder.importSymbols(_H,_I)
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
AdPresence,AdProductIdentifier=mibBuilder.importSymbols('ADTRAN-TC','AdPresence','AdProductIdentifier')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAccessory=ModuleIdentity((1,3,6,1,4,1,664,5,54))
if mibBuilder.loadTexts:adGenAccessory.setRevisions(('2010-02-24 13:00',))
_AdGenAccessoryNotificationEvents_ObjectIdentity=ObjectIdentity
adGenAccessoryNotificationEvents=_AdGenAccessoryNotificationEvents_ObjectIdentity((1,3,6,1,4,1,664,5,54,0))
if mibBuilder.loadTexts:adGenAccessoryNotificationEvents.setStatus(_A)
class _AdGenAccessoryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAccessoryCount_Type.__name__=_D
_AdGenAccessoryCount_Object=MibScalar
adGenAccessoryCount=_AdGenAccessoryCount_Object((1,3,6,1,4,1,664,5,54,1),_AdGenAccessoryCount_Type())
adGenAccessoryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryCount.setStatus(_A)
class _AdGenAccessoryStartIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAccessoryStartIndex_Type.__name__=_D
_AdGenAccessoryStartIndex_Object=MibScalar
adGenAccessoryStartIndex=_AdGenAccessoryStartIndex_Object((1,3,6,1,4,1,664,5,54,2),_AdGenAccessoryStartIndex_Type())
adGenAccessoryStartIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryStartIndex.setStatus(_A)
class _AdGenAccessoryModuleCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAccessoryModuleCount_Type.__name__=_D
_AdGenAccessoryModuleCount_Object=MibScalar
adGenAccessoryModuleCount=_AdGenAccessoryModuleCount_Object((1,3,6,1,4,1,664,5,54,3),_AdGenAccessoryModuleCount_Type())
adGenAccessoryModuleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryModuleCount.setStatus(_A)
_AdGenAccessoryTable_Object=MibTable
adGenAccessoryTable=_AdGenAccessoryTable_Object((1,3,6,1,4,1,664,5,54,6))
if mibBuilder.loadTexts:adGenAccessoryTable.setStatus(_A)
_AdGenAccessoryEntry_Object=MibTableRow
adGenAccessoryEntry=_AdGenAccessoryEntry_Object((1,3,6,1,4,1,664,5,54,6,1))
adGenAccessoryEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:adGenAccessoryEntry.setStatus(_A)
class _AdGenAccessoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAccessoryIndex_Type.__name__=_D
_AdGenAccessoryIndex_Object=MibTableColumn
adGenAccessoryIndex=_AdGenAccessoryIndex_Object((1,3,6,1,4,1,664,5,54,6,1,1),_AdGenAccessoryIndex_Type())
adGenAccessoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryIndex.setStatus(_A)
class _AdGenAccessoryModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenAccessoryModuleIndex_Type.__name__=_D
_AdGenAccessoryModuleIndex_Object=MibTableColumn
adGenAccessoryModuleIndex=_AdGenAccessoryModuleIndex_Object((1,3,6,1,4,1,664,5,54,6,1,2),_AdGenAccessoryModuleIndex_Type())
adGenAccessoryModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryModuleIndex.setStatus(_A)
_AdGenAccessoryState_Type=AdPresence
_AdGenAccessoryState_Object=MibTableColumn
adGenAccessoryState=_AdGenAccessoryState_Object((1,3,6,1,4,1,664,5,54,6,1,3),_AdGenAccessoryState_Type())
adGenAccessoryState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryState.setStatus(_A)
_AdGenAccessoryProduct_Type=AdProductIdentifier
_AdGenAccessoryProduct_Object=MibTableColumn
adGenAccessoryProduct=_AdGenAccessoryProduct_Object((1,3,6,1,4,1,664,5,54,6,1,4),_AdGenAccessoryProduct_Type())
adGenAccessoryProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProduct.setStatus(_A)
class _AdGenAccessoryTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableTraps',1),('disableTraps',2)))
_AdGenAccessoryTrapEnable_Type.__name__=_D
_AdGenAccessoryTrapEnable_Object=MibTableColumn
adGenAccessoryTrapEnable=_AdGenAccessoryTrapEnable_Object((1,3,6,1,4,1,664,5,54,6,1,5),_AdGenAccessoryTrapEnable_Type())
adGenAccessoryTrapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenAccessoryTrapEnable.setStatus(_A)
_AdGenAccessoryAlarmStatus_Type=OctetString
_AdGenAccessoryAlarmStatus_Object=MibTableColumn
adGenAccessoryAlarmStatus=_AdGenAccessoryAlarmStatus_Object((1,3,6,1,4,1,664,5,54,6,1,6),_AdGenAccessoryAlarmStatus_Type())
adGenAccessoryAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryAlarmStatus.setStatus(_A)
_AdGenAccessoryFaceplate_Type=OctetString
_AdGenAccessoryFaceplate_Object=MibTableColumn
adGenAccessoryFaceplate=_AdGenAccessoryFaceplate_Object((1,3,6,1,4,1,664,5,54,6,1,7),_AdGenAccessoryFaceplate_Type())
adGenAccessoryFaceplate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryFaceplate.setStatus(_A)
class _AdGenAccessoryStatServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,8,9,10)));namedValues=NamedValues(*(('is',1),('oosUas',2),('oosMA',3),('fault',5),('isStbyHot',8),('isActLock',9),('isStbyLock',10)))
_AdGenAccessoryStatServiceState_Type.__name__=_D
_AdGenAccessoryStatServiceState_Object=MibTableColumn
adGenAccessoryStatServiceState=_AdGenAccessoryStatServiceState_Object((1,3,6,1,4,1,664,5,54,6,1,8),_AdGenAccessoryStatServiceState_Type())
adGenAccessoryStatServiceState.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenAccessoryStatServiceState.setStatus(_A)
_AdGenAccessoryPortNumber_Type=Integer32
_AdGenAccessoryPortNumber_Object=MibTableColumn
adGenAccessoryPortNumber=_AdGenAccessoryPortNumber_Object((1,3,6,1,4,1,664,5,54,6,1,9),_AdGenAccessoryPortNumber_Type())
adGenAccessoryPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryPortNumber.setStatus(_A)
_AdGenAccessoryProvVersion_Type=Integer32
_AdGenAccessoryProvVersion_Object=MibTableColumn
adGenAccessoryProvVersion=_AdGenAccessoryProvVersion_Object((1,3,6,1,4,1,664,5,54,6,1,10),_AdGenAccessoryProvVersion_Type())
adGenAccessoryProvVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProvVersion.setStatus(_A)
_AdGenAccessoryTFileName_Type=DisplayString
_AdGenAccessoryTFileName_Object=MibTableColumn
adGenAccessoryTFileName=_AdGenAccessoryTFileName_Object((1,3,6,1,4,1,664,5,54,6,1,13),_AdGenAccessoryTFileName_Type())
adGenAccessoryTFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenAccessoryTFileName.setStatus(_A)
class _AdGenAccessoryUpdateSoftware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiate',1))
_AdGenAccessoryUpdateSoftware_Type.__name__=_D
_AdGenAccessoryUpdateSoftware_Object=MibTableColumn
adGenAccessoryUpdateSoftware=_AdGenAccessoryUpdateSoftware_Object((1,3,6,1,4,1,664,5,54,6,1,15),_AdGenAccessoryUpdateSoftware_Type())
adGenAccessoryUpdateSoftware.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenAccessoryUpdateSoftware.setStatus(_A)
_AdGenAccessoryUpdateStatus_Type=DisplayString
_AdGenAccessoryUpdateStatus_Object=MibTableColumn
adGenAccessoryUpdateStatus=_AdGenAccessoryUpdateStatus_Object((1,3,6,1,4,1,664,5,54,6,1,16),_AdGenAccessoryUpdateStatus_Type())
adGenAccessoryUpdateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryUpdateStatus.setStatus(_A)
_AdGenAccessoryUpTime_Type=TimeTicks
_AdGenAccessoryUpTime_Object=MibTableColumn
adGenAccessoryUpTime=_AdGenAccessoryUpTime_Object((1,3,6,1,4,1,664,5,54,6,1,17),_AdGenAccessoryUpTime_Type())
adGenAccessoryUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryUpTime.setStatus(_A)
_AdGenAccessoryProdTable_Object=MibTable
adGenAccessoryProdTable=_AdGenAccessoryProdTable_Object((1,3,6,1,4,1,664,5,54,7))
if mibBuilder.loadTexts:adGenAccessoryProdTable.setStatus(_A)
_AdGenAccessoryProdEntry_Object=MibTableRow
adGenAccessoryProdEntry=_AdGenAccessoryProdEntry_Object((1,3,6,1,4,1,664,5,54,7,1))
adGenAccessoryProdEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:adGenAccessoryProdEntry.setStatus(_A)
_AdGenAccessoryProdName_Type=DisplayString
_AdGenAccessoryProdName_Object=MibTableColumn
adGenAccessoryProdName=_AdGenAccessoryProdName_Object((1,3,6,1,4,1,664,5,54,7,1,2),_AdGenAccessoryProdName_Type())
adGenAccessoryProdName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdName.setStatus(_A)
_AdGenAccessoryProdPartNumber_Type=DisplayString
_AdGenAccessoryProdPartNumber_Object=MibTableColumn
adGenAccessoryProdPartNumber=_AdGenAccessoryProdPartNumber_Object((1,3,6,1,4,1,664,5,54,7,1,3),_AdGenAccessoryProdPartNumber_Type())
adGenAccessoryProdPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdPartNumber.setStatus(_A)
_AdGenAccessoryProdCLEIcode_Type=DisplayString
_AdGenAccessoryProdCLEIcode_Object=MibTableColumn
adGenAccessoryProdCLEIcode=_AdGenAccessoryProdCLEIcode_Object((1,3,6,1,4,1,664,5,54,7,1,4),_AdGenAccessoryProdCLEIcode_Type())
adGenAccessoryProdCLEIcode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdCLEIcode.setStatus(_A)
_AdGenAccessoryProdSerialNumber_Type=DisplayString
_AdGenAccessoryProdSerialNumber_Object=MibTableColumn
adGenAccessoryProdSerialNumber=_AdGenAccessoryProdSerialNumber_Object((1,3,6,1,4,1,664,5,54,7,1,5),_AdGenAccessoryProdSerialNumber_Type())
adGenAccessoryProdSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdSerialNumber.setStatus(_A)
_AdGenAccessoryProdRevision_Type=DisplayString
_AdGenAccessoryProdRevision_Object=MibTableColumn
adGenAccessoryProdRevision=_AdGenAccessoryProdRevision_Object((1,3,6,1,4,1,664,5,54,7,1,6),_AdGenAccessoryProdRevision_Type())
adGenAccessoryProdRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdRevision.setStatus(_A)
_AdGenAccessoryProdSwVersion_Type=DisplayString
_AdGenAccessoryProdSwVersion_Object=MibTableColumn
adGenAccessoryProdSwVersion=_AdGenAccessoryProdSwVersion_Object((1,3,6,1,4,1,664,5,54,7,1,7),_AdGenAccessoryProdSwVersion_Type())
adGenAccessoryProdSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdSwVersion.setStatus(_A)
_AdGenAccessoryProdPhysAddress_Type=PhysAddress
_AdGenAccessoryProdPhysAddress_Object=MibTableColumn
adGenAccessoryProdPhysAddress=_AdGenAccessoryProdPhysAddress_Object((1,3,6,1,4,1,664,5,54,7,1,8),_AdGenAccessoryProdPhysAddress_Type())
adGenAccessoryProdPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdPhysAddress.setStatus(_A)
_AdGenAccessoryProdProductID_Type=ObjectIdentifier
_AdGenAccessoryProdProductID_Object=MibTableColumn
adGenAccessoryProdProductID=_AdGenAccessoryProdProductID_Object((1,3,6,1,4,1,664,5,54,7,1,9),_AdGenAccessoryProdProductID_Type())
adGenAccessoryProdProductID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdProductID.setStatus(_A)
_AdGenAccessoryProdTransType_Type=DisplayString
_AdGenAccessoryProdTransType_Object=MibTableColumn
adGenAccessoryProdTransType=_AdGenAccessoryProdTransType_Object((1,3,6,1,4,1,664,5,54,7,1,10),_AdGenAccessoryProdTransType_Type())
adGenAccessoryProdTransType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAccessoryProdTransType.setStatus(_A)
_AdGenAccessoryConfigTable_Object=MibTable
adGenAccessoryConfigTable=_AdGenAccessoryConfigTable_Object((1,3,6,1,4,1,664,5,54,9))
if mibBuilder.loadTexts:adGenAccessoryConfigTable.setStatus(_A)
_AdGenAccessoryConfigEntry_Object=MibTableRow
adGenAccessoryConfigEntry=_AdGenAccessoryConfigEntry_Object((1,3,6,1,4,1,664,5,54,9,1))
adGenAccessoryConfigEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:adGenAccessoryConfigEntry.setStatus(_A)
_AdGenAccessoryStateConfig_Type=AdPresence
_AdGenAccessoryStateConfig_Object=MibTableColumn
adGenAccessoryStateConfig=_AdGenAccessoryStateConfig_Object((1,3,6,1,4,1,664,5,54,9,1,1),_AdGenAccessoryStateConfig_Type())
adGenAccessoryStateConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenAccessoryStateConfig.setStatus(_A)
adTAAccessoryModuleInserted=NotificationType((1,3,6,1,4,1,664,5,54,0,1005402))
adTAAccessoryModuleInserted.setObjects(*((_H,_I),(_J,_K),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:adTAAccessoryModuleInserted.setStatus(_A)
adTAAccessoryModuleRemoved=NotificationType((1,3,6,1,4,1,664,5,54,0,1005403))
adTAAccessoryModuleRemoved.setObjects(*((_H,_I),(_J,_K),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:adTAAccessoryModuleRemoved.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adGenAccessory':adGenAccessory,'adGenAccessoryNotificationEvents':adGenAccessoryNotificationEvents,'adTAAccessoryModuleInserted':adTAAccessoryModuleInserted,'adTAAccessoryModuleRemoved':adTAAccessoryModuleRemoved,'adGenAccessoryCount':adGenAccessoryCount,'adGenAccessoryStartIndex':adGenAccessoryStartIndex,'adGenAccessoryModuleCount':adGenAccessoryModuleCount,'adGenAccessoryTable':adGenAccessoryTable,'adGenAccessoryEntry':adGenAccessoryEntry,_E:adGenAccessoryIndex,_F:adGenAccessoryModuleIndex,'adGenAccessoryState':adGenAccessoryState,'adGenAccessoryProduct':adGenAccessoryProduct,'adGenAccessoryTrapEnable':adGenAccessoryTrapEnable,'adGenAccessoryAlarmStatus':adGenAccessoryAlarmStatus,'adGenAccessoryFaceplate':adGenAccessoryFaceplate,'adGenAccessoryStatServiceState':adGenAccessoryStatServiceState,'adGenAccessoryPortNumber':adGenAccessoryPortNumber,'adGenAccessoryProvVersion':adGenAccessoryProvVersion,'adGenAccessoryTFileName':adGenAccessoryTFileName,'adGenAccessoryUpdateSoftware':adGenAccessoryUpdateSoftware,'adGenAccessoryUpdateStatus':adGenAccessoryUpdateStatus,'adGenAccessoryUpTime':adGenAccessoryUpTime,'adGenAccessoryProdTable':adGenAccessoryProdTable,'adGenAccessoryProdEntry':adGenAccessoryProdEntry,'adGenAccessoryProdName':adGenAccessoryProdName,'adGenAccessoryProdPartNumber':adGenAccessoryProdPartNumber,'adGenAccessoryProdCLEIcode':adGenAccessoryProdCLEIcode,'adGenAccessoryProdSerialNumber':adGenAccessoryProdSerialNumber,'adGenAccessoryProdRevision':adGenAccessoryProdRevision,'adGenAccessoryProdSwVersion':adGenAccessoryProdSwVersion,'adGenAccessoryProdPhysAddress':adGenAccessoryProdPhysAddress,'adGenAccessoryProdProductID':adGenAccessoryProdProductID,'adGenAccessoryProdTransType':adGenAccessoryProdTransType,'adGenAccessoryConfigTable':adGenAccessoryConfigTable,'adGenAccessoryConfigEntry':adGenAccessoryConfigEntry,'adGenAccessoryStateConfig':adGenAccessoryStateConfig})