_X='fruHistoryFactorySerialNum'
_W='fruHistoryFactoryPartNum'
_V='fruHistoryTime'
_U='fruHistoryEvent'
_T='fruHistoryObjectNum'
_S='fruHistoryClass'
_R='cpLastEvent'
_Q='cpStatus'
_P='fruObjectNum'
_O='fruClass'
_N='fruStatus'
_M='fruHistoryIndex'
_L='faulty'
_K='entPhysicalName'
_J='SW-MIB'
_I='unknown'
_H='other'
_G='DisplayString'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='Integer32'
_C='HA-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fibrechannel,=mibBuilder.importSymbols('Brocade-REG-MIB','fibrechannel')
entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_E,_F,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
swID,swSsn=mibBuilder.importSymbols(_J,'swID','swSsn')
haMIB=ModuleIdentity((1,3,6,1,4,1,1588,2,1,2))
if mibBuilder.loadTexts:haMIB.setRevisions(('2002-08-16 00:00','2004-02-25 15:30','2009-02-09 00:00','2009-04-06 00:00','2009-06-25 12:00','2010-07-22 10:00','2012-09-25 10:00','2013-05-07 17:57'))
class FruClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_H,1),(_I,2),('chassis',3),('cp',4),('other-CP',5),('switchblade',6),('wwn',7),('powerSupply',8),('fan',9),('coreblade',10),('applicationblade',11)))
_HighAvailability_ObjectIdentity=ObjectIdentity
highAvailability=_HighAvailability_ObjectIdentity((1,3,6,1,4,1,1588,2,1,2,1))
class _HaStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('redundant',0),('nonredundant',1)))
_HaStatus_Type.__name__=_D
_HaStatus_Object=MibScalar
haStatus=_HaStatus_Object((1,3,6,1,4,1,1588,2,1,2,1,1),_HaStatus_Type())
haStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:haStatus.setStatus(_A)
_FruTable_Object=MibTable
fruTable=_FruTable_Object((1,3,6,1,4,1,1588,2,1,2,1,5))
if mibBuilder.loadTexts:fruTable.setStatus(_A)
_FRUEntry_Object=MibTableRow
fRUEntry=_FRUEntry_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1))
fRUEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fRUEntry.setStatus(_A)
_FruClass_Type=FruClass
_FruClass_Object=MibTableColumn
fruClass=_FruClass_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,1),_FruClass_Type())
fruClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fruClass.setStatus(_A)
class _FruStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),(_I,2),('on',3),('off',4),(_L,5),('poweredon',6),('initialized',7)))
_FruStatus_Type.__name__=_D
_FruStatus_Object=MibTableColumn
fruStatus=_FruStatus_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,2),_FruStatus_Type())
fruStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fruStatus.setStatus(_A)
_FruObjectNum_Type=Integer32
_FruObjectNum_Object=MibTableColumn
fruObjectNum=_FruObjectNum_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,3),_FruObjectNum_Type())
fruObjectNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fruObjectNum.setStatus(_A)
_FruSupplierId_Type=DisplayString
_FruSupplierId_Object=MibTableColumn
fruSupplierId=_FruSupplierId_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,4),_FruSupplierId_Type())
fruSupplierId.setMaxAccess(_B)
if mibBuilder.loadTexts:fruSupplierId.setStatus(_A)
_FruSupplierPartNum_Type=DisplayString
_FruSupplierPartNum_Object=MibTableColumn
fruSupplierPartNum=_FruSupplierPartNum_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,5),_FruSupplierPartNum_Type())
fruSupplierPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fruSupplierPartNum.setStatus(_A)
class _FruSupplierSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FruSupplierSerialNum_Type.__name__=_G
_FruSupplierSerialNum_Object=MibTableColumn
fruSupplierSerialNum=_FruSupplierSerialNum_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,6),_FruSupplierSerialNum_Type())
fruSupplierSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fruSupplierSerialNum.setStatus(_A)
_FruSupplierRevCode_Type=DisplayString
_FruSupplierRevCode_Object=MibTableColumn
fruSupplierRevCode=_FruSupplierRevCode_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,7),_FruSupplierRevCode_Type())
fruSupplierRevCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fruSupplierRevCode.setStatus(_A)
_FruPowerConsumption_Type=DisplayString
_FruPowerConsumption_Object=MibTableColumn
fruPowerConsumption=_FruPowerConsumption_Object((1,3,6,1,4,1,1588,2,1,2,1,5,1,8),_FruPowerConsumption_Type())
fruPowerConsumption.setMaxAccess(_B)
if mibBuilder.loadTexts:fruPowerConsumption.setStatus(_A)
if mibBuilder.loadTexts:fruPowerConsumption.setUnits('watt')
_FruHistoryTable_Object=MibTable
fruHistoryTable=_FruHistoryTable_Object((1,3,6,1,4,1,1588,2,1,2,1,6))
if mibBuilder.loadTexts:fruHistoryTable.setStatus(_A)
_FruHistoryEntry_Object=MibTableRow
fruHistoryEntry=_FruHistoryEntry_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1))
fruHistoryEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:fruHistoryEntry.setStatus(_A)
_FruHistoryIndex_Type=Integer32
_FruHistoryIndex_Object=MibTableColumn
fruHistoryIndex=_FruHistoryIndex_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,1),_FruHistoryIndex_Type())
fruHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryIndex.setStatus(_A)
_FruHistoryClass_Type=FruClass
_FruHistoryClass_Object=MibTableColumn
fruHistoryClass=_FruHistoryClass_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,2),_FruHistoryClass_Type())
fruHistoryClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryClass.setStatus(_A)
_FruHistoryObjectNum_Type=Integer32
_FruHistoryObjectNum_Object=MibTableColumn
fruHistoryObjectNum=_FruHistoryObjectNum_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,3),_FruHistoryObjectNum_Type())
fruHistoryObjectNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryObjectNum.setStatus(_A)
class _FruHistoryEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('added',1),('removed',2),('invalid',3)))
_FruHistoryEvent_Type.__name__=_D
_FruHistoryEvent_Object=MibTableColumn
fruHistoryEvent=_FruHistoryEvent_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,4),_FruHistoryEvent_Type())
fruHistoryEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryEvent.setStatus(_A)
_FruHistoryTime_Type=DisplayString
_FruHistoryTime_Object=MibTableColumn
fruHistoryTime=_FruHistoryTime_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,5),_FruHistoryTime_Type())
fruHistoryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryTime.setStatus(_A)
_FruHistoryFactoryPartNum_Type=DisplayString
_FruHistoryFactoryPartNum_Object=MibTableColumn
fruHistoryFactoryPartNum=_FruHistoryFactoryPartNum_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,6),_FruHistoryFactoryPartNum_Type())
fruHistoryFactoryPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryFactoryPartNum.setStatus(_A)
_FruHistoryFactorySerialNum_Type=DisplayString
_FruHistoryFactorySerialNum_Object=MibTableColumn
fruHistoryFactorySerialNum=_FruHistoryFactorySerialNum_Object((1,3,6,1,4,1,1588,2,1,2,1,6,1,7),_FruHistoryFactorySerialNum_Type())
fruHistoryFactorySerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fruHistoryFactorySerialNum.setStatus(_A)
_CpTable_Object=MibTable
cpTable=_CpTable_Object((1,3,6,1,4,1,1588,2,1,2,1,7))
if mibBuilder.loadTexts:cpTable.setStatus(_A)
_CpEntry_Object=MibTableRow
cpEntry=_CpEntry_Object((1,3,6,1,4,1,1588,2,1,2,1,7,1))
cpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cpEntry.setStatus(_A)
class _CpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),('active',3),('standby',4),('failed',5)))
_CpStatus_Type.__name__=_D
_CpStatus_Object=MibTableColumn
cpStatus=_CpStatus_Object((1,3,6,1,4,1,1588,2,1,2,1,7,1,1),_CpStatus_Type())
cpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpStatus.setStatus(_A)
_CpIpAddress_Type=IpAddress
_CpIpAddress_Object=MibTableColumn
cpIpAddress=_CpIpAddress_Object((1,3,6,1,4,1,1588,2,1,2,1,7,1,2),_CpIpAddress_Type())
cpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpIpAddress.setStatus(_A)
_CpIpMask_Type=IpAddress
_CpIpMask_Object=MibTableColumn
cpIpMask=_CpIpMask_Object((1,3,6,1,4,1,1588,2,1,2,1,7,1,3),_CpIpMask_Type())
cpIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cpIpMask.setStatus(_A)
_CpIpGateway_Type=IpAddress
_CpIpGateway_Object=MibTableColumn
cpIpGateway=_CpIpGateway_Object((1,3,6,1,4,1,1588,2,1,2,1,7,1,4),_CpIpGateway_Type())
cpIpGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:cpIpGateway.setStatus(_A)
class _CpLastEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_H,1),(_I,2),('haSync',3),('haOutSync',4),('cpFaulty',5),('cpHealthy',6),('cpActive',7),('configChange',8),('failOverStart',9),('failOverDone',10),('firmwareCommit',11),('firmwareUpgrade',12)))
_CpLastEvent_Type.__name__=_D
_CpLastEvent_Object=MibTableColumn
cpLastEvent=_CpLastEvent_Object((1,3,6,1,4,1,1588,2,1,2,1,7,1,5),_CpLastEvent_Type())
cpLastEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpLastEvent.setStatus(_A)
_BpTable_Object=MibTable
bpTable=_BpTable_Object((1,3,6,1,4,1,1588,2,1,2,1,8))
if mibBuilder.loadTexts:bpTable.setStatus(_A)
_BpEntry_Object=MibTableRow
bpEntry=_BpEntry_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1))
bpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bpEntry.setStatus(_A)
class _BpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('on',1),('off',2),(_L,3),('unknow',4),('others',5)))
_BpStatus_Type.__name__=_D
_BpStatus_Object=MibTableColumn
bpStatus=_BpStatus_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,1),_BpStatus_Type())
bpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bpStatus.setStatus(_A)
_Bpeth0IpAddress_Type=IpAddress
_Bpeth0IpAddress_Object=MibTableColumn
bpeth0IpAddress=_Bpeth0IpAddress_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,2),_Bpeth0IpAddress_Type())
bpeth0IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bpeth0IpAddress.setStatus(_A)
_Bpeth1IpAddress_Type=IpAddress
_Bpeth1IpAddress_Object=MibTableColumn
bpeth1IpAddress=_Bpeth1IpAddress_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,3),_Bpeth1IpAddress_Type())
bpeth1IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bpeth1IpAddress.setStatus(_A)
_BpsubNetMaskIpaddress_Type=IpAddress
_BpsubNetMaskIpaddress_Object=MibTableColumn
bpsubNetMaskIpaddress=_BpsubNetMaskIpaddress_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,4),_BpsubNetMaskIpaddress_Type())
bpsubNetMaskIpaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bpsubNetMaskIpaddress.setStatus(_A)
_BpIpGateway_Type=IpAddress
_BpIpGateway_Object=MibTableColumn
bpIpGateway=_BpIpGateway_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,5),_BpIpGateway_Type())
bpIpGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:bpIpGateway.setStatus(_A)
class _BpSasPriVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_BpSasPriVersion_Type.__name__=_G
_BpSasPriVersion_Object=MibTableColumn
bpSasPriVersion=_BpSasPriVersion_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,6),_BpSasPriVersion_Type())
bpSasPriVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bpSasPriVersion.setStatus(_A)
class _BpSasSecVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_BpSasSecVersion_Type.__name__=_G
_BpSasSecVersion_Object=MibTableColumn
bpSasSecVersion=_BpSasSecVersion_Object((1,3,6,1,4,1,1588,2,1,2,1,8,1,7),_BpSasSecVersion_Type())
bpSasSecVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bpSasSecVersion.setStatus(_A)
_HaMIBTraps_ObjectIdentity=ObjectIdentity
haMIBTraps=_HaMIBTraps_ObjectIdentity((1,3,6,1,4,1,1588,2,1,2,2))
_HaMIBTrapPrefix_ObjectIdentity=ObjectIdentity
haMIBTrapPrefix=_HaMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1588,2,1,2,2,0))
fruStatusChanged=NotificationType((1,3,6,1,4,1,1588,2,1,2,2,0,1))
fruStatusChanged.setObjects(*((_E,_K),(_C,_N),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:fruStatusChanged.setStatus(_A)
cpStatusChanged=NotificationType((1,3,6,1,4,1,1588,2,1,2,2,0,2))
cpStatusChanged.setObjects(*((_C,_Q),(_C,_R),(_J,'swID'),(_J,'swSsn')))
if mibBuilder.loadTexts:cpStatusChanged.setStatus(_A)
fruHistoryTrap=NotificationType((1,3,6,1,4,1,1588,2,1,2,2,0,3))
fruHistoryTrap.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X)))
if mibBuilder.loadTexts:fruHistoryTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FruClass':FruClass,'haMIB':haMIB,'highAvailability':highAvailability,'haStatus':haStatus,'fruTable':fruTable,'fRUEntry':fRUEntry,_O:fruClass,_N:fruStatus,_P:fruObjectNum,'fruSupplierId':fruSupplierId,'fruSupplierPartNum':fruSupplierPartNum,'fruSupplierSerialNum':fruSupplierSerialNum,'fruSupplierRevCode':fruSupplierRevCode,'fruPowerConsumption':fruPowerConsumption,'fruHistoryTable':fruHistoryTable,'fruHistoryEntry':fruHistoryEntry,_M:fruHistoryIndex,_S:fruHistoryClass,_T:fruHistoryObjectNum,_U:fruHistoryEvent,_V:fruHistoryTime,_W:fruHistoryFactoryPartNum,_X:fruHistoryFactorySerialNum,'cpTable':cpTable,'cpEntry':cpEntry,_Q:cpStatus,'cpIpAddress':cpIpAddress,'cpIpMask':cpIpMask,'cpIpGateway':cpIpGateway,_R:cpLastEvent,'bpTable':bpTable,'bpEntry':bpEntry,'bpStatus':bpStatus,'bpeth0IpAddress':bpeth0IpAddress,'bpeth1IpAddress':bpeth1IpAddress,'bpsubNetMaskIpaddress':bpsubNetMaskIpaddress,'bpIpGateway':bpIpGateway,'bpSasPriVersion':bpSasPriVersion,'bpSasSecVersion':bpSasSecVersion,'haMIBTraps':haMIBTraps,'haMIBTrapPrefix':haMIBTrapPrefix,'fruStatusChanged':fruStatusChanged,'cpStatusChanged':cpStatusChanged,'fruHistoryTrap':fruHistoryTrap})