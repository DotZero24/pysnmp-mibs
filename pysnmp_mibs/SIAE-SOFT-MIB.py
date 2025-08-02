_O='softwareDownloadStatus'
_N='softwareElementId'
_M='softwareUnitId'
_L='running'
_K='loaded'
_J='notLoaded'
_I='equipIpSnmpAgentAddress'
_H='SIAE-EQUIP-MIB'
_G='OctetString'
_F='SIAE-SOFT-MIB'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmTrap,=mibBuilder.importSymbols('SIAE-ALARM-MIB','alarmTrap')
equipIpSnmpAgentAddress,=mibBuilder.importSymbols(_H,_I)
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
software=ModuleIdentity((1,3,6,1,4,1,3373,1103,7))
if mibBuilder.loadTexts:software.setRevisions(('2017-10-16 00:00','2015-03-23 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _SoftwareMibVersion_Type(Integer32):defaultValue=1
_SoftwareMibVersion_Type.__name__=_C
_SoftwareMibVersion_Object=MibScalar
softwareMibVersion=_SoftwareMibVersion_Object((1,3,6,1,4,1,3373,1103,7,1),_SoftwareMibVersion_Type())
softwareMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareMibVersion.setStatus(_A)
class _SoftwareEquipmentReleaseBench1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SoftwareEquipmentReleaseBench1_Type.__name__=_D
_SoftwareEquipmentReleaseBench1_Object=MibScalar
softwareEquipmentReleaseBench1=_SoftwareEquipmentReleaseBench1_Object((1,3,6,1,4,1,3373,1103,7,2),_SoftwareEquipmentReleaseBench1_Type())
softwareEquipmentReleaseBench1.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareEquipmentReleaseBench1.setStatus(_A)
class _SoftwareEquipmentReleaseBench1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_SoftwareEquipmentReleaseBench1Status_Type.__name__=_C
_SoftwareEquipmentReleaseBench1Status_Object=MibScalar
softwareEquipmentReleaseBench1Status=_SoftwareEquipmentReleaseBench1Status_Object((1,3,6,1,4,1,3373,1103,7,3),_SoftwareEquipmentReleaseBench1Status_Type())
softwareEquipmentReleaseBench1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareEquipmentReleaseBench1Status.setStatus(_A)
class _SoftwareEquipmentReleaseBench2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SoftwareEquipmentReleaseBench2_Type.__name__=_D
_SoftwareEquipmentReleaseBench2_Object=MibScalar
softwareEquipmentReleaseBench2=_SoftwareEquipmentReleaseBench2_Object((1,3,6,1,4,1,3373,1103,7,4),_SoftwareEquipmentReleaseBench2_Type())
softwareEquipmentReleaseBench2.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareEquipmentReleaseBench2.setStatus(_A)
class _SoftwareEquipmentReleaseBench2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_SoftwareEquipmentReleaseBench2Status_Type.__name__=_C
_SoftwareEquipmentReleaseBench2Status_Object=MibScalar
softwareEquipmentReleaseBench2Status=_SoftwareEquipmentReleaseBench2Status_Object((1,3,6,1,4,1,3373,1103,7,5),_SoftwareEquipmentReleaseBench2Status_Type())
softwareEquipmentReleaseBench2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareEquipmentReleaseBench2Status.setStatus(_A)
_SoftwareIpAddressDwlServer_Type=IpAddress
_SoftwareIpAddressDwlServer_Object=MibScalar
softwareIpAddressDwlServer=_SoftwareIpAddressDwlServer_Object((1,3,6,1,4,1,3373,1103,7,6),_SoftwareIpAddressDwlServer_Type())
softwareIpAddressDwlServer.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareIpAddressDwlServer.setStatus(_A)
class _SoftwareGosipAddressDwlServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_SoftwareGosipAddressDwlServer_Type.__name__=_G
_SoftwareGosipAddressDwlServer_Object=MibScalar
softwareGosipAddressDwlServer=_SoftwareGosipAddressDwlServer_Object((1,3,6,1,4,1,3373,1103,7,7),_SoftwareGosipAddressDwlServer_Type())
softwareGosipAddressDwlServer.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareGosipAddressDwlServer.setStatus(_A)
class _SoftwareDownloadfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SoftwareDownloadfile_Type.__name__=_D
_SoftwareDownloadfile_Object=MibScalar
softwareDownloadfile=_SoftwareDownloadfile_Object((1,3,6,1,4,1,3373,1103,7,8),_SoftwareDownloadfile_Type())
softwareDownloadfile.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareDownloadfile.setStatus(_A)
_SoftwareActionRequest_Type=Integer32
_SoftwareActionRequest_Object=MibScalar
softwareActionRequest=_SoftwareActionRequest_Object((1,3,6,1,4,1,3373,1103,7,9),_SoftwareActionRequest_Type())
softwareActionRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareActionRequest.setStatus(_A)
class _SoftwareDownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,8)));namedValues=NamedValues(*(('downloading',1),('completed',2),('interrupted',3),('perifDownloading',4),('configurationDownloading',5),('rejectedDowngrade',8)))
_SoftwareDownloadStatus_Type.__name__=_C
_SoftwareDownloadStatus_Object=MibScalar
softwareDownloadStatus=_SoftwareDownloadStatus_Object((1,3,6,1,4,1,3373,1103,7,10),_SoftwareDownloadStatus_Type())
softwareDownloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareDownloadStatus.setStatus(_A)
_SoftwareUnitTable_Object=MibTable
softwareUnitTable=_SoftwareUnitTable_Object((1,3,6,1,4,1,3373,1103,7,11))
if mibBuilder.loadTexts:softwareUnitTable.setStatus(_A)
_SoftwareUnitRecord_Object=MibTableRow
softwareUnitRecord=_SoftwareUnitRecord_Object((1,3,6,1,4,1,3373,1103,7,11,1))
softwareUnitRecord.setIndexNames((0,_F,_M),(0,_F,_N))
if mibBuilder.loadTexts:softwareUnitRecord.setStatus(_A)
_SoftwareUnitId_Type=Integer32
_SoftwareUnitId_Object=MibTableColumn
softwareUnitId=_SoftwareUnitId_Object((1,3,6,1,4,1,3373,1103,7,11,1,1),_SoftwareUnitId_Type())
softwareUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareUnitId.setStatus(_A)
_SoftwareElementId_Type=Integer32
_SoftwareElementId_Object=MibTableColumn
softwareElementId=_SoftwareElementId_Object((1,3,6,1,4,1,3373,1103,7,11,1,2),_SoftwareElementId_Type())
softwareElementId.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareElementId.setStatus(_A)
class _SoftwareType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('s-record',1),('image-FPGA',2),('volatile',3)))
_SoftwareType_Type.__name__=_C
_SoftwareType_Object=MibTableColumn
softwareType=_SoftwareType_Object((1,3,6,1,4,1,3373,1103,7,11,1,3),_SoftwareType_Type())
softwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareType.setStatus(_A)
class _SoftwareUnitReleaseBench1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SoftwareUnitReleaseBench1_Type.__name__=_D
_SoftwareUnitReleaseBench1_Object=MibTableColumn
softwareUnitReleaseBench1=_SoftwareUnitReleaseBench1_Object((1,3,6,1,4,1,3373,1103,7,11,1,4),_SoftwareUnitReleaseBench1_Type())
softwareUnitReleaseBench1.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareUnitReleaseBench1.setStatus(_A)
class _SoftwareUnitReleaseBench2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SoftwareUnitReleaseBench2_Type.__name__=_D
_SoftwareUnitReleaseBench2_Object=MibTableColumn
softwareUnitReleaseBench2=_SoftwareUnitReleaseBench2_Object((1,3,6,1,4,1,3373,1103,7,11,1,5),_SoftwareUnitReleaseBench2_Type())
softwareUnitReleaseBench2.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareUnitReleaseBench2.setStatus(_A)
class _SoftwareUnitActualRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SoftwareUnitActualRelease_Type.__name__=_D
_SoftwareUnitActualRelease_Object=MibTableColumn
softwareUnitActualRelease=_SoftwareUnitActualRelease_Object((1,3,6,1,4,1,3373,1103,7,11,1,6),_SoftwareUnitActualRelease_Type())
softwareUnitActualRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:softwareUnitActualRelease.setStatus(_A)
class _SoftwareDownloadStatusTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,34)));namedValues=NamedValues(*(('trapDisable',1),('trapEnable',2),('trapEnableWithACK',34)))
_SoftwareDownloadStatusTrapNotification_Type.__name__=_C
_SoftwareDownloadStatusTrapNotification_Object=MibScalar
softwareDownloadStatusTrapNotification=_SoftwareDownloadStatusTrapNotification_Object((1,3,6,1,4,1,3373,1103,7,12),_SoftwareDownloadStatusTrapNotification_Type())
softwareDownloadStatusTrapNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareDownloadStatusTrapNotification.setStatus(_A)
_SoftwareRemoteIpAddressDwlServer_Type=IpAddress
_SoftwareRemoteIpAddressDwlServer_Object=MibScalar
softwareRemoteIpAddressDwlServer=_SoftwareRemoteIpAddressDwlServer_Object((1,3,6,1,4,1,3373,1103,7,13),_SoftwareRemoteIpAddressDwlServer_Type())
softwareRemoteIpAddressDwlServer.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareRemoteIpAddressDwlServer.setStatus(_A)
softwareDownloadStatusTrap=NotificationType((1,3,6,1,4,1,3373,1103,0,701))
softwareDownloadStatusTrap.setObjects(*((_H,_I),(_F,_O)))
if mibBuilder.loadTexts:softwareDownloadStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'softwareDownloadStatusTrap':softwareDownloadStatusTrap,'software':software,'softwareMibVersion':softwareMibVersion,'softwareEquipmentReleaseBench1':softwareEquipmentReleaseBench1,'softwareEquipmentReleaseBench1Status':softwareEquipmentReleaseBench1Status,'softwareEquipmentReleaseBench2':softwareEquipmentReleaseBench2,'softwareEquipmentReleaseBench2Status':softwareEquipmentReleaseBench2Status,'softwareIpAddressDwlServer':softwareIpAddressDwlServer,'softwareGosipAddressDwlServer':softwareGosipAddressDwlServer,'softwareDownloadfile':softwareDownloadfile,'softwareActionRequest':softwareActionRequest,_O:softwareDownloadStatus,'softwareUnitTable':softwareUnitTable,'softwareUnitRecord':softwareUnitRecord,_M:softwareUnitId,_N:softwareElementId,'softwareType':softwareType,'softwareUnitReleaseBench1':softwareUnitReleaseBench1,'softwareUnitReleaseBench2':softwareUnitReleaseBench2,'softwareUnitActualRelease':softwareUnitActualRelease,'softwareDownloadStatusTrapNotification':softwareDownloadStatusTrapNotification,'softwareRemoteIpAddressDwlServer':softwareRemoteIpAddressDwlServer})