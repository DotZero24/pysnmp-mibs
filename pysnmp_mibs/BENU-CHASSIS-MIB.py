_f='benuChassisFanFailureInfo'
_e='benuChassisPowerFailureInfo'
_d='benuChassisPowerFailureCardInfo'
_c='notApplicable'
_b='benuPowerSupplyIndex'
_a='benuFanCardIndex'
_Z='benuSensorIndex'
_Y='benuSensorCardIndex'
_X='benuCardIfIndex'
_W='benuCardIndex'
_V='Unsigned32'
_U='benuSensorId'
_T='benuSensorValue'
_S='benuSensorType'
_R='benuSensorName'
_Q='obsolete'
_P='ifType'
_O='ifOperStatus'
_N='ifIndex'
_M='ifDescr'
_L='ifAdminStatus'
_K='accessible-for-notify'
_J='read-write'
_I='disabled'
_H='enabled'
_G='benuChassisPowerInfo'
_F='not-accessible'
_E='IF-MIB'
_D='Integer32'
_C='BENU-CHASSIS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuPlatform,=mibBuilder.importSymbols('BENU-PLATFORM-MIB','benuPlatform')
ifAdminStatus,ifDescr,ifIndex,ifOperStatus,ifType=mibBuilder.importSymbols(_E,_L,_M,_N,_O,_P)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
benuChassisMIB=ModuleIdentity((1,3,6,1,4,1,39406,1,1))
if mibBuilder.loadTexts:benuChassisMIB.setRevisions(('2016-11-18 00:00','2016-10-14 00:00','2016-01-26 00:00','2015-10-14 00:00','2015-01-27 00:00','2015-01-05 00:00','2014-11-14 00:00','2014-06-27 00:00','2013-11-25 00:00','2012-12-12 00:00'))
_BenuChassisNotifObjects_ObjectIdentity=ObjectIdentity
benuChassisNotifObjects=_BenuChassisNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,1,1,0))
_BenuChassisMIBObjects_ObjectIdentity=ObjectIdentity
benuChassisMIBObjects=_BenuChassisMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1))
_BenuChassisInfo_ObjectIdentity=ObjectIdentity
benuChassisInfo=_BenuChassisInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,1))
class _BenuChassisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('meg100',1),('meg400',2),('meg1200',3),('meg50',4),('xMEG100',5),('xMEG10',6)))
_BenuChassisType_Type.__name__=_D
_BenuChassisType_Object=MibScalar
benuChassisType=_BenuChassisType_Object((1,3,6,1,4,1,39406,1,1,1,1,1),_BenuChassisType_Type())
benuChassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:benuChassisType.setStatus(_A)
_BenuChassisHwVersion_Type=DisplayString
_BenuChassisHwVersion_Object=MibScalar
benuChassisHwVersion=_BenuChassisHwVersion_Object((1,3,6,1,4,1,39406,1,1,1,1,2),_BenuChassisHwVersion_Type())
benuChassisHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:benuChassisHwVersion.setStatus(_A)
_BenuChassisId_Type=DisplayString
_BenuChassisId_Object=MibScalar
benuChassisId=_BenuChassisId_Object((1,3,6,1,4,1,39406,1,1,1,1,3),_BenuChassisId_Type())
benuChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:benuChassisId.setStatus(_A)
_BenuChassisNumOfSlots_Type=Integer32
_BenuChassisNumOfSlots_Object=MibScalar
benuChassisNumOfSlots=_BenuChassisNumOfSlots_Object((1,3,6,1,4,1,39406,1,1,1,1,4),_BenuChassisNumOfSlots_Type())
benuChassisNumOfSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:benuChassisNumOfSlots.setStatus(_A)
class _BenuChassisPowerTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_BenuChassisPowerTrapEnable_Type.__name__=_D
_BenuChassisPowerTrapEnable_Object=MibScalar
benuChassisPowerTrapEnable=_BenuChassisPowerTrapEnable_Object((1,3,6,1,4,1,39406,1,1,1,1,5),_BenuChassisPowerTrapEnable_Type())
benuChassisPowerTrapEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:benuChassisPowerTrapEnable.setStatus(_A)
class _BenuChassisFanTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_BenuChassisFanTrapEnable_Type.__name__=_D
_BenuChassisFanTrapEnable_Object=MibScalar
benuChassisFanTrapEnable=_BenuChassisFanTrapEnable_Object((1,3,6,1,4,1,39406,1,1,1,1,6),_BenuChassisFanTrapEnable_Type())
benuChassisFanTrapEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:benuChassisFanTrapEnable.setStatus(_A)
class _BenuChassisSensorTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_BenuChassisSensorTrapEnable_Type.__name__=_D
_BenuChassisSensorTrapEnable_Object=MibScalar
benuChassisSensorTrapEnable=_BenuChassisSensorTrapEnable_Object((1,3,6,1,4,1,39406,1,1,1,1,7),_BenuChassisSensorTrapEnable_Type())
benuChassisSensorTrapEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:benuChassisSensorTrapEnable.setStatus(_A)
_BenuSysUpTimeAtLastChassisChange_Type=TimeTicks
_BenuSysUpTimeAtLastChassisChange_Object=MibScalar
benuSysUpTimeAtLastChassisChange=_BenuSysUpTimeAtLastChassisChange_Object((1,3,6,1,4,1,39406,1,1,1,1,8),_BenuSysUpTimeAtLastChassisChange_Type())
benuSysUpTimeAtLastChassisChange.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSysUpTimeAtLastChassisChange.setStatus(_A)
_BenuCardInfo_ObjectIdentity=ObjectIdentity
benuCardInfo=_BenuCardInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,2))
_BenuCardTable_Object=MibTable
benuCardTable=_BenuCardTable_Object((1,3,6,1,4,1,39406,1,1,1,2,1))
if mibBuilder.loadTexts:benuCardTable.setStatus(_A)
_BenuCardEntry_Object=MibTableRow
benuCardEntry=_BenuCardEntry_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1))
benuCardEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:benuCardEntry.setStatus(_A)
class _BenuCardIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_BenuCardIndex_Type.__name__=_V
_BenuCardIndex_Object=MibTableColumn
benuCardIndex=_BenuCardIndex_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,1),_BenuCardIndex_Type())
benuCardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:benuCardIndex.setStatus(_A)
class _BenuCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',0),('rsm',1),('switchFabric',2),('shelfmgr',3),('seFP',4),('inputOutputCard',5),('switchMesh',6),('xmeg',7)))
_BenuCardType_Type.__name__=_D
_BenuCardType_Object=MibTableColumn
benuCardType=_BenuCardType_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,2),_BenuCardType_Type())
benuCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardType.setStatus(_A)
_BenuCardDescr_Type=DisplayString
_BenuCardDescr_Object=MibTableColumn
benuCardDescr=_BenuCardDescr_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,3),_BenuCardDescr_Type())
benuCardDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardDescr.setStatus(_A)
_BenuCardSerial_Type=DisplayString
_BenuCardSerial_Object=MibTableColumn
benuCardSerial=_BenuCardSerial_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,4),_BenuCardSerial_Type())
benuCardSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardSerial.setStatus(_A)
_BenuCardPartNumber_Type=DisplayString
_BenuCardPartNumber_Object=MibTableColumn
benuCardPartNumber=_BenuCardPartNumber_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,5),_BenuCardPartNumber_Type())
benuCardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardPartNumber.setStatus(_A)
_BenuCardHwVersion_Type=DisplayString
_BenuCardHwVersion_Object=MibTableColumn
benuCardHwVersion=_BenuCardHwVersion_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,6),_BenuCardHwVersion_Type())
benuCardHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardHwVersion.setStatus(_A)
_BenuCardSwVersion_Type=DisplayString
_BenuCardSwVersion_Object=MibTableColumn
benuCardSwVersion=_BenuCardSwVersion_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,7),_BenuCardSwVersion_Type())
benuCardSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardSwVersion.setStatus(_A)
_BenuCardSlotNumber_Type=Integer32
_BenuCardSlotNumber_Object=MibTableColumn
benuCardSlotNumber=_BenuCardSlotNumber_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,8),_BenuCardSlotNumber_Type())
benuCardSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardSlotNumber.setStatus(_A)
_BenuCardRamSize_Type=Integer32
_BenuCardRamSize_Object=MibTableColumn
benuCardRamSize=_BenuCardRamSize_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,9),_BenuCardRamSize_Type())
benuCardRamSize.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardRamSize.setStatus(_A)
_BenuCardPrimaryDiskSize_Type=Integer32
_BenuCardPrimaryDiskSize_Object=MibTableColumn
benuCardPrimaryDiskSize=_BenuCardPrimaryDiskSize_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,10),_BenuCardPrimaryDiskSize_Type())
benuCardPrimaryDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardPrimaryDiskSize.setStatus(_A)
_BenuCardSecondaryDiskSize_Type=Integer32
_BenuCardSecondaryDiskSize_Object=MibTableColumn
benuCardSecondaryDiskSize=_BenuCardSecondaryDiskSize_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,11),_BenuCardSecondaryDiskSize_Type())
benuCardSecondaryDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardSecondaryDiskSize.setStatus(_A)
class _BenuCardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notSpecified',1),('up',2),('down',3),('standby',4),('rom',5),('flash',6),('diag',7),('boot',8),('config',9)))
_BenuCardOperStatus_Type.__name__=_D
_BenuCardOperStatus_Object=MibTableColumn
benuCardOperStatus=_BenuCardOperStatus_Object((1,3,6,1,4,1,39406,1,1,1,2,1,1,12),_BenuCardOperStatus_Type())
benuCardOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardOperStatus.setStatus(_A)
_BenuCardIfInfo_ObjectIdentity=ObjectIdentity
benuCardIfInfo=_BenuCardIfInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,3))
_BenuCardIfIndexTable_Object=MibTable
benuCardIfIndexTable=_BenuCardIfIndexTable_Object((1,3,6,1,4,1,39406,1,1,1,3,1))
if mibBuilder.loadTexts:benuCardIfIndexTable.setStatus(_A)
_BenuCardIfIndexEntry_Object=MibTableRow
benuCardIfIndexEntry=_BenuCardIfIndexEntry_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1))
benuCardIfIndexEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:benuCardIfIndexEntry.setStatus(_A)
_BenuCardIfIndex_Type=Unsigned32
_BenuCardIfIndex_Object=MibTableColumn
benuCardIfIndex=_BenuCardIfIndex_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,1),_BenuCardIfIndex_Type())
benuCardIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:benuCardIfIndex.setStatus(_A)
_BenuCardIfName_Type=DisplayString
_BenuCardIfName_Object=MibTableColumn
benuCardIfName=_BenuCardIfName_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,2),_BenuCardIfName_Type())
benuCardIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfName.setStatus(_A)
_BenuCardIfPortNumber_Type=Integer32
_BenuCardIfPortNumber_Object=MibTableColumn
benuCardIfPortNumber=_BenuCardIfPortNumber_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,3),_BenuCardIfPortNumber_Type())
benuCardIfPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfPortNumber.setStatus(_A)
_BenuCardIfSlotNumber_Type=Integer32
_BenuCardIfSlotNumber_Object=MibTableColumn
benuCardIfSlotNumber=_BenuCardIfSlotNumber_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,4),_BenuCardIfSlotNumber_Type())
benuCardIfSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfSlotNumber.setStatus(_A)
class _BenuCardIfLinkUpDownEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_BenuCardIfLinkUpDownEnable_Type.__name__=_D
_BenuCardIfLinkUpDownEnable_Object=MibTableColumn
benuCardIfLinkUpDownEnable=_BenuCardIfLinkUpDownEnable_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,5),_BenuCardIfLinkUpDownEnable_Type())
benuCardIfLinkUpDownEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:benuCardIfLinkUpDownEnable.setStatus(_A)
class _BenuCardIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('none',0),('ethernet',1),('fastEthernet',2),('gigaEthernet',3),('tunnel',4),('ipGre',5),('vlan',6),('l2tp',7),('cable',8),('bridge',9),('ip',10),('multiBind',11),('p2p',12),('loopback',13),('multiBindLastResort',14),('lag',15),('max',16)))
_BenuCardIfPortType_Type.__name__=_D
_BenuCardIfPortType_Object=MibTableColumn
benuCardIfPortType=_BenuCardIfPortType_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,6),_BenuCardIfPortType_Type())
benuCardIfPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfPortType.setStatus(_A)
_BenuCardIfBindName_Type=DisplayString
_BenuCardIfBindName_Object=MibTableColumn
benuCardIfBindName=_BenuCardIfBindName_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,7),_BenuCardIfBindName_Type())
benuCardIfBindName.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfBindName.setStatus(_A)
_BenuCardIfEncapsulation_Type=DisplayString
_BenuCardIfEncapsulation_Object=MibTableColumn
benuCardIfEncapsulation=_BenuCardIfEncapsulation_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,8),_BenuCardIfEncapsulation_Type())
benuCardIfEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfEncapsulation.setStatus(_A)
class _BenuCardIfVirtualType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('physical',1),('virtual',2)))
_BenuCardIfVirtualType_Type.__name__=_D
_BenuCardIfVirtualType_Object=MibTableColumn
benuCardIfVirtualType=_BenuCardIfVirtualType_Object((1,3,6,1,4,1,39406,1,1,1,3,1,1,9),_BenuCardIfVirtualType_Type())
benuCardIfVirtualType.setMaxAccess(_B)
if mibBuilder.loadTexts:benuCardIfVirtualType.setStatus(_A)
_BenuSensorInfo_ObjectIdentity=ObjectIdentity
benuSensorInfo=_BenuSensorInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,4))
_BenuSensorTable_Object=MibTable
benuSensorTable=_BenuSensorTable_Object((1,3,6,1,4,1,39406,1,1,1,4,1))
if mibBuilder.loadTexts:benuSensorTable.setStatus(_A)
_BenuSensorEntry_Object=MibTableRow
benuSensorEntry=_BenuSensorEntry_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1))
benuSensorEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:benuSensorEntry.setStatus(_A)
_BenuSensorCardIndex_Type=Unsigned32
_BenuSensorCardIndex_Object=MibTableColumn
benuSensorCardIndex=_BenuSensorCardIndex_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,1),_BenuSensorCardIndex_Type())
benuSensorCardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:benuSensorCardIndex.setStatus(_A)
_BenuSensorIndex_Type=Unsigned32
_BenuSensorIndex_Object=MibTableColumn
benuSensorIndex=_BenuSensorIndex_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,2),_BenuSensorIndex_Type())
benuSensorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:benuSensorIndex.setStatus(_A)
_BenuSensorName_Type=DisplayString
_BenuSensorName_Object=MibTableColumn
benuSensorName=_BenuSensorName_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,3),_BenuSensorName_Type())
benuSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorName.setStatus(_A)
class _BenuSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('other',0),('temparature',1),('voltage',2),('electicCurrent',3),('fan',4),('power',5)))
_BenuSensorType_Type.__name__=_D
_BenuSensorType_Object=MibTableColumn
benuSensorType=_BenuSensorType_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,4),_BenuSensorType_Type())
benuSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorType.setStatus(_A)
_BenuSensorValue_Type=Integer32
_BenuSensorValue_Object=MibTableColumn
benuSensorValue=_BenuSensorValue_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,5),_BenuSensorValue_Type())
benuSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorValue.setStatus(_A)
_BenuSensorMinThresh_Type=Integer32
_BenuSensorMinThresh_Object=MibTableColumn
benuSensorMinThresh=_BenuSensorMinThresh_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,6),_BenuSensorMinThresh_Type())
benuSensorMinThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorMinThresh.setStatus(_A)
_BenuSensorMaxThresh_Type=Integer32
_BenuSensorMaxThresh_Object=MibTableColumn
benuSensorMaxThresh=_BenuSensorMaxThresh_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,7),_BenuSensorMaxThresh_Type())
benuSensorMaxThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorMaxThresh.setStatus(_A)
class _BenuSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('normal',1),('critical',2)))
_BenuSensorState_Type.__name__=_D
_BenuSensorState_Object=MibTableColumn
benuSensorState=_BenuSensorState_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,8),_BenuSensorState_Type())
benuSensorState.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorState.setStatus(_A)
_BenuSensorId_Type=Integer32
_BenuSensorId_Object=MibTableColumn
benuSensorId=_BenuSensorId_Object((1,3,6,1,4,1,39406,1,1,1,4,1,1,9),_BenuSensorId_Type())
benuSensorId.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSensorId.setStatus(_A)
_BenuChassisGeneralInfo_ObjectIdentity=ObjectIdentity
benuChassisGeneralInfo=_BenuChassisGeneralInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,5))
_BenuSysUpTimeSinceLastConfigChange_Type=TimeTicks
_BenuSysUpTimeSinceLastConfigChange_Object=MibScalar
benuSysUpTimeSinceLastConfigChange=_BenuSysUpTimeSinceLastConfigChange_Object((1,3,6,1,4,1,39406,1,1,1,5,1),_BenuSysUpTimeSinceLastConfigChange_Type())
benuSysUpTimeSinceLastConfigChange.setMaxAccess(_B)
if mibBuilder.loadTexts:benuSysUpTimeSinceLastConfigChange.setStatus(_A)
_BenuFanInfo_ObjectIdentity=ObjectIdentity
benuFanInfo=_BenuFanInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,6))
_BenuFanTable_Object=MibTable
benuFanTable=_BenuFanTable_Object((1,3,6,1,4,1,39406,1,1,1,6,1))
if mibBuilder.loadTexts:benuFanTable.setStatus(_A)
_BenuFanEntry_Object=MibTableRow
benuFanEntry=_BenuFanEntry_Object((1,3,6,1,4,1,39406,1,1,1,6,1,1))
benuFanEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:benuFanEntry.setStatus(_A)
_BenuFanCardIndex_Type=Unsigned32
_BenuFanCardIndex_Object=MibTableColumn
benuFanCardIndex=_BenuFanCardIndex_Object((1,3,6,1,4,1,39406,1,1,1,6,1,1,1),_BenuFanCardIndex_Type())
benuFanCardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:benuFanCardIndex.setStatus(_A)
_BenuFanMaxSpeed_Type=Unsigned32
_BenuFanMaxSpeed_Object=MibTableColumn
benuFanMaxSpeed=_BenuFanMaxSpeed_Object((1,3,6,1,4,1,39406,1,1,1,6,1,1,2),_BenuFanMaxSpeed_Type())
benuFanMaxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:benuFanMaxSpeed.setStatus(_A)
_BenuFanCurSpeed_Type=Unsigned32
_BenuFanCurSpeed_Object=MibTableColumn
benuFanCurSpeed=_BenuFanCurSpeed_Object((1,3,6,1,4,1,39406,1,1,1,6,1,1,3),_BenuFanCurSpeed_Type())
benuFanCurSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:benuFanCurSpeed.setStatus(_A)
_BenuFanStatus_Type=Integer32
_BenuFanStatus_Object=MibTableColumn
benuFanStatus=_BenuFanStatus_Object((1,3,6,1,4,1,39406,1,1,1,6,1,1,4),_BenuFanStatus_Type())
benuFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:benuFanStatus.setStatus(_A)
_BenuPowerSupplyInfo_ObjectIdentity=ObjectIdentity
benuPowerSupplyInfo=_BenuPowerSupplyInfo_ObjectIdentity((1,3,6,1,4,1,39406,1,1,1,7))
_BenuPowerSupplyTable_Object=MibTable
benuPowerSupplyTable=_BenuPowerSupplyTable_Object((1,3,6,1,4,1,39406,1,1,1,7,1))
if mibBuilder.loadTexts:benuPowerSupplyTable.setStatus(_A)
_BenuPowerSupplyEntry_Object=MibTableRow
benuPowerSupplyEntry=_BenuPowerSupplyEntry_Object((1,3,6,1,4,1,39406,1,1,1,7,1,1))
benuPowerSupplyEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:benuPowerSupplyEntry.setStatus(_A)
class _BenuPowerSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerA',1),('powerB',2)))
_BenuPowerSupplyIndex_Type.__name__=_D
_BenuPowerSupplyIndex_Object=MibTableColumn
benuPowerSupplyIndex=_BenuPowerSupplyIndex_Object((1,3,6,1,4,1,39406,1,1,1,7,1,1,1),_BenuPowerSupplyIndex_Type())
benuPowerSupplyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:benuPowerSupplyIndex.setStatus(_A)
_BenuPowerSupplyName_Type=DisplayString
_BenuPowerSupplyName_Object=MibTableColumn
benuPowerSupplyName=_BenuPowerSupplyName_Object((1,3,6,1,4,1,39406,1,1,1,7,1,1,2),_BenuPowerSupplyName_Type())
benuPowerSupplyName.setMaxAccess(_B)
if mibBuilder.loadTexts:benuPowerSupplyName.setStatus(_A)
class _BenuPowerSupplyPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_BenuPowerSupplyPresent_Type.__name__=_D
_BenuPowerSupplyPresent_Object=MibTableColumn
benuPowerSupplyPresent=_BenuPowerSupplyPresent_Object((1,3,6,1,4,1,39406,1,1,1,7,1,1,3),_BenuPowerSupplyPresent_Type())
benuPowerSupplyPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:benuPowerSupplyPresent.setStatus(_A)
class _BenuPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ac',1),('dc',2),(_c,3)))
_BenuPowerSupplyType_Type.__name__=_D
_BenuPowerSupplyType_Object=MibTableColumn
benuPowerSupplyType=_BenuPowerSupplyType_Object((1,3,6,1,4,1,39406,1,1,1,7,1,1,4),_BenuPowerSupplyType_Type())
benuPowerSupplyType.setMaxAccess(_B)
if mibBuilder.loadTexts:benuPowerSupplyType.setStatus(_A)
class _BenuPowerSupplyPowered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('powered',1),('notPowered',2),(_c,3)))
_BenuPowerSupplyPowered_Type.__name__=_D
_BenuPowerSupplyPowered_Object=MibTableColumn
benuPowerSupplyPowered=_BenuPowerSupplyPowered_Object((1,3,6,1,4,1,39406,1,1,1,7,1,1,5),_BenuPowerSupplyPowered_Type())
benuPowerSupplyPowered.setMaxAccess(_B)
if mibBuilder.loadTexts:benuPowerSupplyPowered.setStatus(_A)
_BenuChassisNotifVariables_ObjectIdentity=ObjectIdentity
benuChassisNotifVariables=_BenuChassisNotifVariables_ObjectIdentity((1,3,6,1,4,1,39406,1,1,2))
class _BenuChassisPowerFailureInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('powerFailureA',1),('powerFailureB',2),('powerRestoredA',3),('powerRestoredB',4)))
_BenuChassisPowerFailureInfo_Type.__name__=_D
_BenuChassisPowerFailureInfo_Object=MibScalar
benuChassisPowerFailureInfo=_BenuChassisPowerFailureInfo_Object((1,3,6,1,4,1,39406,1,1,2,1),_BenuChassisPowerFailureInfo_Type())
benuChassisPowerFailureInfo.setMaxAccess(_K)
if mibBuilder.loadTexts:benuChassisPowerFailureInfo.setStatus(_Q)
_BenuChassisFanFailureInfo_Type=DisplayString
_BenuChassisFanFailureInfo_Object=MibScalar
benuChassisFanFailureInfo=_BenuChassisFanFailureInfo_Object((1,3,6,1,4,1,39406,1,1,2,2),_BenuChassisFanFailureInfo_Type())
benuChassisFanFailureInfo.setMaxAccess(_K)
if mibBuilder.loadTexts:benuChassisFanFailureInfo.setStatus(_A)
_BenuChassisPowerFailureCardInfo_Type=Unsigned32
_BenuChassisPowerFailureCardInfo_Object=MibScalar
benuChassisPowerFailureCardInfo=_BenuChassisPowerFailureCardInfo_Object((1,3,6,1,4,1,39406,1,1,2,3),_BenuChassisPowerFailureCardInfo_Type())
benuChassisPowerFailureCardInfo.setMaxAccess(_K)
if mibBuilder.loadTexts:benuChassisPowerFailureCardInfo.setStatus(_Q)
class _BenuChassisPowerInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerSupplyA',1),('powerSupplyB',2)))
_BenuChassisPowerInfo_Type.__name__=_D
_BenuChassisPowerInfo_Object=MibScalar
benuChassisPowerInfo=_BenuChassisPowerInfo_Object((1,3,6,1,4,1,39406,1,1,2,4),_BenuChassisPowerInfo_Type())
benuChassisPowerInfo.setMaxAccess(_K)
if mibBuilder.loadTexts:benuChassisPowerInfo.setStatus(_A)
benuChassisPowerFailure=NotificationType((1,3,6,1,4,1,39406,1,1,0,1))
benuChassisPowerFailure.setObjects(*((_C,_d),(_C,_e)))
if mibBuilder.loadTexts:benuChassisPowerFailure.setStatus(_Q)
benuChassisFanFailureTrap=NotificationType((1,3,6,1,4,1,39406,1,1,0,2))
benuChassisFanFailureTrap.setObjects((_C,_f))
if mibBuilder.loadTexts:benuChassisFanFailureTrap.setStatus(_A)
benuLinkUpTrap=NotificationType((1,3,6,1,4,1,39406,1,1,0,3))
benuLinkUpTrap.setObjects(*((_E,_N),(_E,_M),(_E,_P),(_E,_L),(_E,_O)))
if mibBuilder.loadTexts:benuLinkUpTrap.setStatus(_A)
benuLinkDownTrap=NotificationType((1,3,6,1,4,1,39406,1,1,0,4))
benuLinkDownTrap.setObjects(*((_E,_N),(_E,_M),(_E,_P),(_E,_L),(_E,_O)))
if mibBuilder.loadTexts:benuLinkDownTrap.setStatus(_A)
benuSensorCritical=NotificationType((1,3,6,1,4,1,39406,1,1,0,5))
benuSensorCritical.setObjects(*((_C,_R),(_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:benuSensorCritical.setStatus(_A)
benuSensorNormal=NotificationType((1,3,6,1,4,1,39406,1,1,0,6))
benuSensorNormal.setObjects(*((_C,_R),(_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:benuSensorNormal.setStatus(_A)
benuChassisPowerFault=NotificationType((1,3,6,1,4,1,39406,1,1,0,7))
benuChassisPowerFault.setObjects((_C,_G))
if mibBuilder.loadTexts:benuChassisPowerFault.setStatus(_A)
benuChassisPowerRecovery=NotificationType((1,3,6,1,4,1,39406,1,1,0,8))
benuChassisPowerRecovery.setObjects((_C,_G))
if mibBuilder.loadTexts:benuChassisPowerRecovery.setStatus(_A)
benuChassisPowerPresent=NotificationType((1,3,6,1,4,1,39406,1,1,0,9))
benuChassisPowerPresent.setObjects((_C,_G))
if mibBuilder.loadTexts:benuChassisPowerPresent.setStatus(_A)
benuChassisPowerAbsent=NotificationType((1,3,6,1,4,1,39406,1,1,0,10))
benuChassisPowerAbsent.setObjects((_C,_G))
if mibBuilder.loadTexts:benuChassisPowerAbsent.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'benuChassisMIB':benuChassisMIB,'benuChassisNotifObjects':benuChassisNotifObjects,'benuChassisPowerFailure':benuChassisPowerFailure,'benuChassisFanFailureTrap':benuChassisFanFailureTrap,'benuLinkUpTrap':benuLinkUpTrap,'benuLinkDownTrap':benuLinkDownTrap,'benuSensorCritical':benuSensorCritical,'benuSensorNormal':benuSensorNormal,'benuChassisPowerFault':benuChassisPowerFault,'benuChassisPowerRecovery':benuChassisPowerRecovery,'benuChassisPowerPresent':benuChassisPowerPresent,'benuChassisPowerAbsent':benuChassisPowerAbsent,'benuChassisMIBObjects':benuChassisMIBObjects,'benuChassisInfo':benuChassisInfo,'benuChassisType':benuChassisType,'benuChassisHwVersion':benuChassisHwVersion,'benuChassisId':benuChassisId,'benuChassisNumOfSlots':benuChassisNumOfSlots,'benuChassisPowerTrapEnable':benuChassisPowerTrapEnable,'benuChassisFanTrapEnable':benuChassisFanTrapEnable,'benuChassisSensorTrapEnable':benuChassisSensorTrapEnable,'benuSysUpTimeAtLastChassisChange':benuSysUpTimeAtLastChassisChange,'benuCardInfo':benuCardInfo,'benuCardTable':benuCardTable,'benuCardEntry':benuCardEntry,_W:benuCardIndex,'benuCardType':benuCardType,'benuCardDescr':benuCardDescr,'benuCardSerial':benuCardSerial,'benuCardPartNumber':benuCardPartNumber,'benuCardHwVersion':benuCardHwVersion,'benuCardSwVersion':benuCardSwVersion,'benuCardSlotNumber':benuCardSlotNumber,'benuCardRamSize':benuCardRamSize,'benuCardPrimaryDiskSize':benuCardPrimaryDiskSize,'benuCardSecondaryDiskSize':benuCardSecondaryDiskSize,'benuCardOperStatus':benuCardOperStatus,'benuCardIfInfo':benuCardIfInfo,'benuCardIfIndexTable':benuCardIfIndexTable,'benuCardIfIndexEntry':benuCardIfIndexEntry,_X:benuCardIfIndex,'benuCardIfName':benuCardIfName,'benuCardIfPortNumber':benuCardIfPortNumber,'benuCardIfSlotNumber':benuCardIfSlotNumber,'benuCardIfLinkUpDownEnable':benuCardIfLinkUpDownEnable,'benuCardIfPortType':benuCardIfPortType,'benuCardIfBindName':benuCardIfBindName,'benuCardIfEncapsulation':benuCardIfEncapsulation,'benuCardIfVirtualType':benuCardIfVirtualType,'benuSensorInfo':benuSensorInfo,'benuSensorTable':benuSensorTable,'benuSensorEntry':benuSensorEntry,_Y:benuSensorCardIndex,_Z:benuSensorIndex,_R:benuSensorName,_S:benuSensorType,_T:benuSensorValue,'benuSensorMinThresh':benuSensorMinThresh,'benuSensorMaxThresh':benuSensorMaxThresh,'benuSensorState':benuSensorState,_U:benuSensorId,'benuChassisGeneralInfo':benuChassisGeneralInfo,'benuSysUpTimeSinceLastConfigChange':benuSysUpTimeSinceLastConfigChange,'benuFanInfo':benuFanInfo,'benuFanTable':benuFanTable,'benuFanEntry':benuFanEntry,_a:benuFanCardIndex,'benuFanMaxSpeed':benuFanMaxSpeed,'benuFanCurSpeed':benuFanCurSpeed,'benuFanStatus':benuFanStatus,'benuPowerSupplyInfo':benuPowerSupplyInfo,'benuPowerSupplyTable':benuPowerSupplyTable,'benuPowerSupplyEntry':benuPowerSupplyEntry,_b:benuPowerSupplyIndex,'benuPowerSupplyName':benuPowerSupplyName,'benuPowerSupplyPresent':benuPowerSupplyPresent,'benuPowerSupplyType':benuPowerSupplyType,'benuPowerSupplyPowered':benuPowerSupplyPowered,'benuChassisNotifVariables':benuChassisNotifVariables,_e:benuChassisPowerFailureInfo,_f:benuChassisFanFailureInfo,_d:benuChassisPowerFailureCardInfo,_G:benuChassisPowerInfo})