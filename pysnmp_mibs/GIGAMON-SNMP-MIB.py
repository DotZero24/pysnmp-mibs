_n='gigamonSnmpNotifBpsFailoverStatus'
_m='gigamonSnmpNotifBpsUnitName'
_l='gigamonSnmpNotifFsMountPoint'
_k='gigamonSnmpNotifCpuIndex'
_j='gigamonSnmpPowerSource'
_i='gigamonSnmpPortLinkDuplex'
_h='gigamonSnmpPortLinkSpeed'
_g='gigamonSnmpBatteryLevel'
_f='gigamonSnmpNotifUtilizationAlarm'
_e='gigamonNotifFanStatus'
_d='gigamonSnmpNotifFanName'
_c='gigamonSnmpNotifRxTxErrorType'
_b='gigamonSnmpNotifRxTxType'
_a='gigamonSnmpNotifTAPRelayStatus'
_Z='gigamonNotifSlotNumber'
_Y='gigamonSnmpNotifModuleName'
_X='gigamonSnmpNotifModuleOperationType'
_W='gigamonSnmpNotifFileName'
_V='gigamonSnmpNotifFirmwareName'
_U='gigamonSnmpNotifUserName'
_T='notApply'
_S='normal'
_R='abnormal'
_Q='failure'
_P='mid-plane'
_O='2010-07-10 10:00'
_N='2012-05-09 00:00'
_M='gigamonSnmpNotifUtilizationThreshold'
_L='gigamonNotifPowerStatus'
_K='gigamonSnmpNotifPortLinkStatus'
_J='gigamonSnmpNotifCounter'
_I='gigamonSnmpNotifPortName'
_H='read-only'
_G='Integer32'
_F='gigamonSnmpNotifDescription'
_E='gigamonSnmpNotifLevel'
_D='gigamonSnmpNotifHardWareName'
_C='accessible-for-notify'
_B='current'
_A='GIGAMON-SNMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,=mibBuilder.importSymbols('SNMPv2-MIB','sysLocation')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
gigamonSnmp=ModuleIdentity((1,3,6,1,4,1,26866))
if mibBuilder.loadTexts:gigamonSnmp.setRevisions(('2013-09-25 00:00','2013-08-09 00:00','2013-04-15 00:00','2012-12-04 00:00',_N,_N,'2012-03-27 00:00','2011-03-25 00:00','2011-03-24 00:00','2011-03-03 00:00',_O,_O))
_GigamonSnmpNotifications_ObjectIdentity=ObjectIdentity
gigamonSnmpNotifications=_GigamonSnmpNotifications_ObjectIdentity((1,3,6,1,4,1,26866,1))
_GigamonGigaVUE_ObjectIdentity=ObjectIdentity
gigamonGigaVUE=_GigamonGigaVUE_ObjectIdentity((1,3,6,1,4,1,26866,1,1))
_GigamonSnmpNotificationObjects_ObjectIdentity=ObjectIdentity
gigamonSnmpNotificationObjects=_GigamonSnmpNotificationObjects_ObjectIdentity((1,3,6,1,4,1,26866,1,2))
class _GigamonSnmpNotifLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('information',1),('minor',2),('major',3),('critical',4)))
_GigamonSnmpNotifLevel_Type.__name__=_G
_GigamonSnmpNotifLevel_Object=MibScalar
gigamonSnmpNotifLevel=_GigamonSnmpNotifLevel_Object((1,3,6,1,4,1,26866,1,2,1),_GigamonSnmpNotifLevel_Type())
gigamonSnmpNotifLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifLevel.setStatus(_B)
_GigamonSnmpNotifDescription_Type=OctetString
_GigamonSnmpNotifDescription_Object=MibScalar
gigamonSnmpNotifDescription=_GigamonSnmpNotifDescription_Object((1,3,6,1,4,1,26866,1,2,2),_GigamonSnmpNotifDescription_Type())
gigamonSnmpNotifDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifDescription.setStatus(_B)
class _GigamonSnmpNotifOpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('read',1),('write',2),('delete',3),('validate',4),('change',5)))
_GigamonSnmpNotifOpType_Type.__name__=_G
_GigamonSnmpNotifOpType_Object=MibScalar
gigamonSnmpNotifOpType=_GigamonSnmpNotifOpType_Object((1,3,6,1,4,1,26866,1,2,3),_GigamonSnmpNotifOpType_Type())
gigamonSnmpNotifOpType.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifOpType.setStatus(_B)
_GigamonSnmpNotifPortName_Type=OctetString
_GigamonSnmpNotifPortName_Object=MibScalar
gigamonSnmpNotifPortName=_GigamonSnmpNotifPortName_Object((1,3,6,1,4,1,26866,1,2,4),_GigamonSnmpNotifPortName_Type())
gigamonSnmpNotifPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifPortName.setStatus(_B)
class _GigamonSnmpNotifPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_GigamonSnmpNotifPortLinkStatus_Type.__name__=_G
_GigamonSnmpNotifPortLinkStatus_Object=MibScalar
gigamonSnmpNotifPortLinkStatus=_GigamonSnmpNotifPortLinkStatus_Object((1,3,6,1,4,1,26866,1,2,5),_GigamonSnmpNotifPortLinkStatus_Type())
gigamonSnmpNotifPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifPortLinkStatus.setStatus(_B)
class _GigamonSnmpNotifTAPRelayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('passive',1),('active',2)))
_GigamonSnmpNotifTAPRelayStatus_Type.__name__=_G
_GigamonSnmpNotifTAPRelayStatus_Object=MibScalar
gigamonSnmpNotifTAPRelayStatus=_GigamonSnmpNotifTAPRelayStatus_Object((1,3,6,1,4,1,26866,1,2,6),_GigamonSnmpNotifTAPRelayStatus_Type())
gigamonSnmpNotifTAPRelayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifTAPRelayStatus.setStatus(_B)
class _GigamonSnmpNotifRxTxType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('rx',0),('tx',1)))
_GigamonSnmpNotifRxTxType_Type.__name__=_G
_GigamonSnmpNotifRxTxType_Object=MibScalar
gigamonSnmpNotifRxTxType=_GigamonSnmpNotifRxTxType_Object((1,3,6,1,4,1,26866,1,2,7),_GigamonSnmpNotifRxTxType_Type())
gigamonSnmpNotifRxTxType.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifRxTxType.setStatus(_B)
class _GigamonSnmpNotifRxTxErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('under-size',0),('fragments',1),('obsolete',2),('jabbers',3),('crc-align',4),('unknown',5)))
_GigamonSnmpNotifRxTxErrorType_Type.__name__=_G
_GigamonSnmpNotifRxTxErrorType_Object=MibScalar
gigamonSnmpNotifRxTxErrorType=_GigamonSnmpNotifRxTxErrorType_Object((1,3,6,1,4,1,26866,1,2,8),_GigamonSnmpNotifRxTxErrorType_Type())
gigamonSnmpNotifRxTxErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifRxTxErrorType.setStatus(_B)
_GigamonSnmpNotifCounter_Type=Integer32
_GigamonSnmpNotifCounter_Object=MibScalar
gigamonSnmpNotifCounter=_GigamonSnmpNotifCounter_Object((1,3,6,1,4,1,26866,1,2,9),_GigamonSnmpNotifCounter_Type())
gigamonSnmpNotifCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifCounter.setStatus(_B)
_GigamonSnmpNotifFirmwareName_Type=OctetString
_GigamonSnmpNotifFirmwareName_Object=MibScalar
gigamonSnmpNotifFirmwareName=_GigamonSnmpNotifFirmwareName_Object((1,3,6,1,4,1,26866,1,2,10),_GigamonSnmpNotifFirmwareName_Type())
gigamonSnmpNotifFirmwareName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifFirmwareName.setStatus(_B)
class _GigamonSnmpNotifModuleOperationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('removed',0),('inserted',1),('changed',2),('mismatch',3),('shutdown',4),('up',5),('license-mismatch',6)))
_GigamonSnmpNotifModuleOperationType_Type.__name__=_G
_GigamonSnmpNotifModuleOperationType_Object=MibScalar
gigamonSnmpNotifModuleOperationType=_GigamonSnmpNotifModuleOperationType_Object((1,3,6,1,4,1,26866,1,2,11),_GigamonSnmpNotifModuleOperationType_Type())
gigamonSnmpNotifModuleOperationType.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifModuleOperationType.setStatus(_B)
_GigamonSnmpNotifModuleName_Type=OctetString
_GigamonSnmpNotifModuleName_Object=MibScalar
gigamonSnmpNotifModuleName=_GigamonSnmpNotifModuleName_Object((1,3,6,1,4,1,26866,1,2,12),_GigamonSnmpNotifModuleName_Type())
gigamonSnmpNotifModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifModuleName.setStatus(_B)
class _GigamonNotifSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_P,0),('slot-1',1),('slot-2',2),('slot-3',3),('gigaLink-Back',4),('daughter-Card',5),('slot-4',10),('slot-5',11),('slot-6',12),('slot-7',13),('slot-8',14),('slot-CC1',15),('slot-CC2',16)))
_GigamonNotifSlotNumber_Type.__name__=_G
_GigamonNotifSlotNumber_Object=MibScalar
gigamonNotifSlotNumber=_GigamonNotifSlotNumber_Object((1,3,6,1,4,1,26866,1,2,13),_GigamonNotifSlotNumber_Type())
gigamonNotifSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonNotifSlotNumber.setStatus(_B)
_GigamonSnmpNotifUserName_Type=OctetString
_GigamonSnmpNotifUserName_Object=MibScalar
gigamonSnmpNotifUserName=_GigamonSnmpNotifUserName_Object((1,3,6,1,4,1,26866,1,2,14),_GigamonSnmpNotifUserName_Type())
gigamonSnmpNotifUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifUserName.setStatus(_B)
_GigamonSnmpNotifFileName_Type=OctetString
_GigamonSnmpNotifFileName_Object=MibScalar
gigamonSnmpNotifFileName=_GigamonSnmpNotifFileName_Object((1,3,6,1,4,1,26866,1,2,15),_GigamonSnmpNotifFileName_Type())
gigamonSnmpNotifFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifFileName.setStatus(_B)
class _GigamonNotifPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_Q,-1),(_R,0),(_S,1)))
_GigamonNotifPowerStatus_Type.__name__=_G
_GigamonNotifPowerStatus_Object=MibScalar
gigamonNotifPowerStatus=_GigamonNotifPowerStatus_Object((1,3,6,1,4,1,26866,1,2,16),_GigamonNotifPowerStatus_Type())
gigamonNotifPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonNotifPowerStatus.setStatus(_B)
_GigamonSnmpNotifHardWareName_Type=OctetString
_GigamonSnmpNotifHardWareName_Object=MibScalar
gigamonSnmpNotifHardWareName=_GigamonSnmpNotifHardWareName_Object((1,3,6,1,4,1,26866,1,2,17),_GigamonSnmpNotifHardWareName_Type())
gigamonSnmpNotifHardWareName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifHardWareName.setStatus(_B)
class _GigamonSnmpNotifGigaVUE420SlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,0),('expansion-slot-1',1),('expansion-slot-2',2),('expansion-slot-3',3),('expansion-slot-4',4),('expansion-slot-5',5),('x1-slot',6),('x2-slot',7),('x3-slot',8),('x4-slot',9)))
_GigamonSnmpNotifGigaVUE420SlotNumber_Type.__name__=_G
_GigamonSnmpNotifGigaVUE420SlotNumber_Object=MibScalar
gigamonSnmpNotifGigaVUE420SlotNumber=_GigamonSnmpNotifGigaVUE420SlotNumber_Object((1,3,6,1,4,1,26866,1,2,18),_GigamonSnmpNotifGigaVUE420SlotNumber_Type())
gigamonSnmpNotifGigaVUE420SlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifGigaVUE420SlotNumber.setStatus(_B)
_GigamonSnmpNotifFanName_Type=OctetString
_GigamonSnmpNotifFanName_Object=MibScalar
gigamonSnmpNotifFanName=_GigamonSnmpNotifFanName_Object((1,3,6,1,4,1,26866,1,2,19),_GigamonSnmpNotifFanName_Type())
gigamonSnmpNotifFanName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifFanName.setStatus(_B)
class _GigamonNotifFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_Q,-1),(_R,0),(_S,1)))
_GigamonNotifFanStatus_Type.__name__=_G
_GigamonNotifFanStatus_Object=MibScalar
gigamonNotifFanStatus=_GigamonNotifFanStatus_Object((1,3,6,1,4,1,26866,1,2,20),_GigamonNotifFanStatus_Type())
gigamonNotifFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonNotifFanStatus.setStatus(_B)
class _GigamonSnmpNotifUtilizationAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('below',0),('exceed',1)))
_GigamonSnmpNotifUtilizationAlarm_Type.__name__=_G
_GigamonSnmpNotifUtilizationAlarm_Object=MibScalar
gigamonSnmpNotifUtilizationAlarm=_GigamonSnmpNotifUtilizationAlarm_Object((1,3,6,1,4,1,26866,1,2,21),_GigamonSnmpNotifUtilizationAlarm_Type())
gigamonSnmpNotifUtilizationAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifUtilizationAlarm.setStatus(_B)
_GigamonSnmpNotifUtilizationThreshold_Type=Integer32
_GigamonSnmpNotifUtilizationThreshold_Object=MibScalar
gigamonSnmpNotifUtilizationThreshold=_GigamonSnmpNotifUtilizationThreshold_Object((1,3,6,1,4,1,26866,1,2,22),_GigamonSnmpNotifUtilizationThreshold_Type())
gigamonSnmpNotifUtilizationThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifUtilizationThreshold.setStatus(_B)
class _GigamonSnmpBatteryLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('batteryChargeComplete',0),('downBelow75',1),('downBelow50',2),('downBelow25',3),('shutDownSystem',4)))
_GigamonSnmpBatteryLevel_Type.__name__=_G
_GigamonSnmpBatteryLevel_Object=MibScalar
gigamonSnmpBatteryLevel=_GigamonSnmpBatteryLevel_Object((1,3,6,1,4,1,26866,1,2,23),_GigamonSnmpBatteryLevel_Type())
gigamonSnmpBatteryLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:gigamonSnmpBatteryLevel.setStatus(_B)
class _GigamonSnmpPortLinkSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_T,0),('speed10',1),('speed100',2),('speed1000',3),('speed10000',4),('speed40000',5),('speed100000',6)))
_GigamonSnmpPortLinkSpeed_Type.__name__=_G
_GigamonSnmpPortLinkSpeed_Object=MibScalar
gigamonSnmpPortLinkSpeed=_GigamonSnmpPortLinkSpeed_Object((1,3,6,1,4,1,26866,1,2,24),_GigamonSnmpPortLinkSpeed_Type())
gigamonSnmpPortLinkSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpPortLinkSpeed.setStatus(_B)
class _GigamonSnmpPortLinkDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),('full',1),('half',2)))
_GigamonSnmpPortLinkDuplex_Type.__name__=_G
_GigamonSnmpPortLinkDuplex_Object=MibScalar
gigamonSnmpPortLinkDuplex=_GigamonSnmpPortLinkDuplex_Object((1,3,6,1,4,1,26866,1,2,25),_GigamonSnmpPortLinkDuplex_Type())
gigamonSnmpPortLinkDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpPortLinkDuplex.setStatus(_B)
_GigamonSnmpNotifCpuIndex_Type=Unsigned32
_GigamonSnmpNotifCpuIndex_Object=MibScalar
gigamonSnmpNotifCpuIndex=_GigamonSnmpNotifCpuIndex_Object((1,3,6,1,4,1,26866,1,2,26),_GigamonSnmpNotifCpuIndex_Type())
gigamonSnmpNotifCpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifCpuIndex.setStatus(_B)
_GigamonSnmpNotifFsMountPoint_Type=OctetString
_GigamonSnmpNotifFsMountPoint_Object=MibScalar
gigamonSnmpNotifFsMountPoint=_GigamonSnmpNotifFsMountPoint_Object((1,3,6,1,4,1,26866,1,2,27),_GigamonSnmpNotifFsMountPoint_Type())
gigamonSnmpNotifFsMountPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifFsMountPoint.setStatus(_B)
class _GigamonSnmpPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mainPower',0),('poe',1),('power48V',2)))
_GigamonSnmpPowerSource_Type.__name__=_G
_GigamonSnmpPowerSource_Object=MibScalar
gigamonSnmpPowerSource=_GigamonSnmpPowerSource_Object((1,3,6,1,4,1,26866,1,2,28),_GigamonSnmpPowerSource_Type())
gigamonSnmpPowerSource.setMaxAccess(_H)
if mibBuilder.loadTexts:gigamonSnmpPowerSource.setStatus(_B)
_GigamonSnmpNotifBpsUnitName_Type=OctetString
_GigamonSnmpNotifBpsUnitName_Object=MibScalar
gigamonSnmpNotifBpsUnitName=_GigamonSnmpNotifBpsUnitName_Object((1,3,6,1,4,1,26866,1,2,29),_GigamonSnmpNotifBpsUnitName_Type())
gigamonSnmpNotifBpsUnitName.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifBpsUnitName.setStatus(_B)
class _GigamonSnmpNotifBpsFailoverStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('primary',0),('secondary',1)))
_GigamonSnmpNotifBpsFailoverStatus_Type.__name__=_G
_GigamonSnmpNotifBpsFailoverStatus_Object=MibScalar
gigamonSnmpNotifBpsFailoverStatus=_GigamonSnmpNotifBpsFailoverStatus_Object((1,3,6,1,4,1,26866,1,2,30),_GigamonSnmpNotifBpsFailoverStatus_Type())
gigamonSnmpNotifBpsFailoverStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gigamonSnmpNotifBpsFailoverStatus.setStatus(_B)
_GigamonSystem_ObjectIdentity=ObjectIdentity
gigamonSystem=_GigamonSystem_ObjectIdentity((1,3,6,1,4,1,26866,2))
_Manufacturer_Type=OctetString
_Manufacturer_Object=MibScalar
manufacturer=_Manufacturer_Object((1,3,6,1,4,1,26866,2,1),_Manufacturer_Type())
manufacturer.setMaxAccess(_H)
if mibBuilder.loadTexts:manufacturer.setStatus(_B)
_Model_Type=OctetString
_Model_Object=MibScalar
model=_Model_Object((1,3,6,1,4,1,26866,2,2),_Model_Type())
model.setMaxAccess(_H)
if mibBuilder.loadTexts:model.setStatus(_B)
_Name_Type=OctetString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,26866,2,3),_Name_Type())
name.setMaxAccess(_H)
if mibBuilder.loadTexts:name.setStatus(_B)
_SerialNumber_Type=OctetString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,26866,2,4),_SerialNumber_Type())
serialNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:serialNumber.setStatus(_B)
_SystemDescription_Type=OctetString
_SystemDescription_Object=MibScalar
systemDescription=_SystemDescription_Object((1,3,6,1,4,1,26866,2,5),_SystemDescription_Type())
systemDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:systemDescription.setStatus(_B)
_Version_Type=OctetString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,26866,2,6),_Version_Type())
version.setMaxAccess(_H)
if mibBuilder.loadTexts:version.setStatus(_B)
_ChassisModelNumber_Type=OctetString
_ChassisModelNumber_Object=MibScalar
chassisModelNumber=_ChassisModelNumber_Object((1,3,6,1,4,1,26866,2,7),_ChassisModelNumber_Type())
chassisModelNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:chassisModelNumber.setStatus(_B)
_ChassisSerialNumber_Type=OctetString
_ChassisSerialNumber_Object=MibScalar
chassisSerialNumber=_ChassisSerialNumber_Object((1,3,6,1,4,1,26866,2,8),_ChassisSerialNumber_Type())
chassisSerialNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:chassisSerialNumber.setStatus(_B)
_BladeSerialNumbers_Type=OctetString
_BladeSerialNumbers_Object=MibScalar
bladeSerialNumbers=_BladeSerialNumbers_Object((1,3,6,1,4,1,26866,2,9),_BladeSerialNumbers_Type())
bladeSerialNumbers.setMaxAccess(_H)
if mibBuilder.loadTexts:bladeSerialNumbers.setStatus(_B)
_FirmwareVersion_Type=OctetString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,26866,2,10),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_H)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_B)
_HardwareVersion_Type=OctetString
_HardwareVersion_Object=MibScalar
hardwareVersion=_HardwareVersion_Object((1,3,6,1,4,1,26866,2,11),_HardwareVersion_Type())
hardwareVersion.setMaxAccess(_H)
if mibBuilder.loadTexts:hardwareVersion.setStatus(_B)
_CpuRAMSize_Type=OctetString
_CpuRAMSize_Object=MibScalar
cpuRAMSize=_CpuRAMSize_Object((1,3,6,1,4,1,26866,2,12),_CpuRAMSize_Type())
cpuRAMSize.setMaxAccess(_H)
if mibBuilder.loadTexts:cpuRAMSize.setStatus(_B)
_CpuUtilization_Type=OctetString
_CpuUtilization_Object=MibScalar
cpuUtilization=_CpuUtilization_Object((1,3,6,1,4,1,26866,2,13),_CpuUtilization_Type())
cpuUtilization.setMaxAccess(_H)
if mibBuilder.loadTexts:cpuUtilization.setStatus(_B)
_Fans_Type=OctetString
_Fans_Object=MibScalar
fans=_Fans_Object((1,3,6,1,4,1,26866,2,14),_Fans_Type())
fans.setMaxAccess(_H)
if mibBuilder.loadTexts:fans.setStatus(_B)
_TemperatureSensors_Type=OctetString
_TemperatureSensors_Object=MibScalar
temperatureSensors=_TemperatureSensors_Object((1,3,6,1,4,1,26866,2,15),_TemperatureSensors_Type())
temperatureSensors.setMaxAccess(_H)
if mibBuilder.loadTexts:temperatureSensors.setStatus(_B)
_PowerSupply_Type=OctetString
_PowerSupply_Object=MibScalar
powerSupply=_PowerSupply_Object((1,3,6,1,4,1,26866,2,16),_PowerSupply_Type())
powerSupply.setMaxAccess(_H)
if mibBuilder.loadTexts:powerSupply.setStatus(_B)
_GigamonProducts_ObjectIdentity=ObjectIdentity
gigamonProducts=_GigamonProducts_ObjectIdentity((1,3,6,1,4,1,26866,3))
_GigamonGV2404_ObjectIdentity=ObjectIdentity
gigamonGV2404=_GigamonGV2404_ObjectIdentity((1,3,6,1,4,1,26866,3,1))
_GigamonGV420_ObjectIdentity=ObjectIdentity
gigamonGV420=_GigamonGV420_ObjectIdentity((1,3,6,1,4,1,26866,3,2))
_GigamonGV212_ObjectIdentity=ObjectIdentity
gigamonGV212=_GigamonGV212_ObjectIdentity((1,3,6,1,4,1,26866,3,3))
_GigamonGV216_ObjectIdentity=ObjectIdentity
gigamonGV216=_GigamonGV216_ObjectIdentity((1,3,6,1,4,1,26866,3,4))
gigamonSnmpResetSystemNotification=NotificationType((1,3,6,1,4,1,26866,1,1,1))
gigamonSnmpResetSystemNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:gigamonSnmpResetSystemNotification.setStatus(_B)
gigamonSnmpUserAuthFailNotification=NotificationType((1,3,6,1,4,1,26866,1,1,2))
gigamonSnmpUserAuthFailNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_U)))
if mibBuilder.loadTexts:gigamonSnmpUserAuthFailNotification.setStatus(_B)
gigamonSnmpFirmwareChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,3))
gigamonSnmpFirmwareChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_V)))
if mibBuilder.loadTexts:gigamonSnmpFirmwareChangeNotification.setStatus(_B)
gigamonSnmpConfigSaveNotification=NotificationType((1,3,6,1,4,1,26866,1,1,4))
gigamonSnmpConfigSaveNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_W)))
if mibBuilder.loadTexts:gigamonSnmpConfigSaveNotification.setStatus(_B)
gigamonSnmpModuleChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,5))
gigamonSnmpModuleChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:gigamonSnmpModuleChangeNotification.setStatus(_B)
gigamonSnmpPacketDropNotification=NotificationType((1,3,6,1,4,1,26866,1,1,6))
gigamonSnmpPacketDropNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:gigamonSnmpPacketDropNotification.setStatus(_B)
gigamonSnmpTapRelayChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,7))
gigamonSnmpTapRelayChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_I),(_A,_a)))
if mibBuilder.loadTexts:gigamonSnmpTapRelayChangeNotification.setStatus(_B)
gigamonSnmpPortLinkChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,8))
gigamonSnmpPortLinkChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:gigamonSnmpPortLinkChangeNotification.setStatus(_B)
gigamonSnmpRxTxErrorNotification=NotificationType((1,3,6,1,4,1,26866,1,1,9))
gigamonSnmpRxTxErrorNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_I),(_A,_b),(_A,_c),(_A,_J)))
if mibBuilder.loadTexts:gigamonSnmpRxTxErrorNotification.setStatus(_B)
gigamonPowerChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,10))
gigamonPowerChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_L)))
if mibBuilder.loadTexts:gigamonPowerChangeNotification.setStatus(_B)
gigamonFanChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,11))
gigamonFanChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:gigamonFanChangeNotification.setStatus(_B)
gigamonSnmpOverThresholdChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,12))
gigamonSnmpOverThresholdChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_I),(_A,_f),(_A,_M)))
if mibBuilder.loadTexts:gigamonSnmpOverThresholdChangeNotification.setStatus(_B)
gigamonSnmpBatteryLevelChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,13))
gigamonSnmpBatteryLevelChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_g)))
if mibBuilder.loadTexts:gigamonSnmpBatteryLevelChangeNotification.setStatus(_B)
gigamonLinkSpeedStatusChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,14))
gigamonLinkSpeedStatusChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_I),(_A,_h),(_A,_i),(_A,_K)))
if mibBuilder.loadTexts:gigamonLinkSpeedStatusChangeNotification.setStatus(_B)
gigamonPowerSourceChangeNotification=NotificationType((1,3,6,1,4,1,26866,1,1,15))
gigamonPowerSourceChangeNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_j),(_A,_L)))
if mibBuilder.loadTexts:gigamonPowerSourceChangeNotification.setStatus(_B)
gigamonSnmpCpuUtilHighNotification=NotificationType((1,3,6,1,4,1,26866,1,1,16))
gigamonSnmpCpuUtilHighNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_k),(_A,_M)))
if mibBuilder.loadTexts:gigamonSnmpCpuUtilHighNotification.setStatus(_B)
gigamonSnmpUnexpectedShutdownNotification=NotificationType((1,3,6,1,4,1,26866,1,1,17))
gigamonSnmpUnexpectedShutdownNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:gigamonSnmpUnexpectedShutdownNotification.setStatus(_B)
gigamonSnmpDiskSpaceLowNotification=NotificationType((1,3,6,1,4,1,26866,1,1,18))
gigamonSnmpDiskSpaceLowNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_l)))
if mibBuilder.loadTexts:gigamonSnmpDiskSpaceLowNotification.setStatus(_B)
gigamonSnmpWatchdogResetNotification=NotificationType((1,3,6,1,4,1,26866,1,1,19))
gigamonSnmpWatchdogResetNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:gigamonSnmpWatchdogResetNotification.setStatus(_B)
gigamonSnmpBpsFailoverNotification=NotificationType((1,3,6,1,4,1,26866,1,1,20))
gigamonSnmpBpsFailoverNotification.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:gigamonSnmpBpsFailoverNotification.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gigamonSnmp':gigamonSnmp,'gigamonSnmpNotifications':gigamonSnmpNotifications,'gigamonGigaVUE':gigamonGigaVUE,'gigamonSnmpResetSystemNotification':gigamonSnmpResetSystemNotification,'gigamonSnmpUserAuthFailNotification':gigamonSnmpUserAuthFailNotification,'gigamonSnmpFirmwareChangeNotification':gigamonSnmpFirmwareChangeNotification,'gigamonSnmpConfigSaveNotification':gigamonSnmpConfigSaveNotification,'gigamonSnmpModuleChangeNotification':gigamonSnmpModuleChangeNotification,'gigamonSnmpPacketDropNotification':gigamonSnmpPacketDropNotification,'gigamonSnmpTapRelayChangeNotification':gigamonSnmpTapRelayChangeNotification,'gigamonSnmpPortLinkChangeNotification':gigamonSnmpPortLinkChangeNotification,'gigamonSnmpRxTxErrorNotification':gigamonSnmpRxTxErrorNotification,'gigamonPowerChangeNotification':gigamonPowerChangeNotification,'gigamonFanChangeNotification':gigamonFanChangeNotification,'gigamonSnmpOverThresholdChangeNotification':gigamonSnmpOverThresholdChangeNotification,'gigamonSnmpBatteryLevelChangeNotification':gigamonSnmpBatteryLevelChangeNotification,'gigamonLinkSpeedStatusChangeNotification':gigamonLinkSpeedStatusChangeNotification,'gigamonPowerSourceChangeNotification':gigamonPowerSourceChangeNotification,'gigamonSnmpCpuUtilHighNotification':gigamonSnmpCpuUtilHighNotification,'gigamonSnmpUnexpectedShutdownNotification':gigamonSnmpUnexpectedShutdownNotification,'gigamonSnmpDiskSpaceLowNotification':gigamonSnmpDiskSpaceLowNotification,'gigamonSnmpWatchdogResetNotification':gigamonSnmpWatchdogResetNotification,'gigamonSnmpBpsFailoverNotification':gigamonSnmpBpsFailoverNotification,'gigamonSnmpNotificationObjects':gigamonSnmpNotificationObjects,_E:gigamonSnmpNotifLevel,_F:gigamonSnmpNotifDescription,'gigamonSnmpNotifOpType':gigamonSnmpNotifOpType,_I:gigamonSnmpNotifPortName,_K:gigamonSnmpNotifPortLinkStatus,_a:gigamonSnmpNotifTAPRelayStatus,_b:gigamonSnmpNotifRxTxType,_c:gigamonSnmpNotifRxTxErrorType,_J:gigamonSnmpNotifCounter,_V:gigamonSnmpNotifFirmwareName,_X:gigamonSnmpNotifModuleOperationType,_Y:gigamonSnmpNotifModuleName,_Z:gigamonNotifSlotNumber,_U:gigamonSnmpNotifUserName,_W:gigamonSnmpNotifFileName,_L:gigamonNotifPowerStatus,_D:gigamonSnmpNotifHardWareName,'gigamonSnmpNotifGigaVUE420SlotNumber':gigamonSnmpNotifGigaVUE420SlotNumber,_d:gigamonSnmpNotifFanName,_e:gigamonNotifFanStatus,_f:gigamonSnmpNotifUtilizationAlarm,_M:gigamonSnmpNotifUtilizationThreshold,_g:gigamonSnmpBatteryLevel,_h:gigamonSnmpPortLinkSpeed,_i:gigamonSnmpPortLinkDuplex,_k:gigamonSnmpNotifCpuIndex,_l:gigamonSnmpNotifFsMountPoint,_j:gigamonSnmpPowerSource,_m:gigamonSnmpNotifBpsUnitName,_n:gigamonSnmpNotifBpsFailoverStatus,'gigamonSystem':gigamonSystem,'manufacturer':manufacturer,'model':model,'name':name,'serialNumber':serialNumber,'systemDescription':systemDescription,'version':version,'chassisModelNumber':chassisModelNumber,'chassisSerialNumber':chassisSerialNumber,'bladeSerialNumbers':bladeSerialNumbers,'firmwareVersion':firmwareVersion,'hardwareVersion':hardwareVersion,'cpuRAMSize':cpuRAMSize,'cpuUtilization':cpuUtilization,'fans':fans,'temperatureSensors':temperatureSensors,'powerSupply':powerSupply,'gigamonProducts':gigamonProducts,'gigamonGV2404':gigamonGV2404,'gigamonGV420':gigamonGV420,'gigamonGV212':gigamonGV212,'gigamonGV216':gigamonGV216})