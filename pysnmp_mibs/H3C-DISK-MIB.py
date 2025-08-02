_G='h3cDiskIndex'
_F='H3C-DISK-MIB'
_E='H3cStorageEnableState'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cStorageActionType,H3cStorageEnableState,h3cStorageRef=mibBuilder.importSymbols('H3C-STORAGE-REF-MIB','H3cStorageActionType',_E,'h3cStorageRef')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cDisk=ModuleIdentity((1,3,6,1,4,1,2011,10,10,3))
_H3cDiskMibObjects_ObjectIdentity=ObjectIdentity
h3cDiskMibObjects=_H3cDiskMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,10,3,1))
_H3cDiskTable_Object=MibTable
h3cDiskTable=_H3cDiskTable_Object((1,3,6,1,4,1,2011,10,10,3,1,1))
if mibBuilder.loadTexts:h3cDiskTable.setStatus(_A)
_H3cDiskEntry_Object=MibTableRow
h3cDiskEntry=_H3cDiskEntry_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1))
h3cDiskEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDiskEntry.setStatus(_A)
_H3cDiskIndex_Type=Integer32
_H3cDiskIndex_Object=MibTableColumn
h3cDiskIndex=_H3cDiskIndex_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,1),_H3cDiskIndex_Type())
h3cDiskIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cDiskIndex.setStatus(_A)
class _H3cDiskPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('sata',1),('pata',2),('sas',3),('scsi',4),('ieee1394',5),('fcal',6)))
_H3cDiskPortType_Type.__name__=_C
_H3cDiskPortType_Object=MibTableColumn
h3cDiskPortType=_H3cDiskPortType_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,2),_H3cDiskPortType_Type())
h3cDiskPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskPortType.setStatus(_A)
_H3cDiskPortSpeed_Type=Integer32
_H3cDiskPortSpeed_Object=MibTableColumn
h3cDiskPortSpeed=_H3cDiskPortSpeed_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,3),_H3cDiskPortSpeed_Type())
h3cDiskPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskPortSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cDiskPortSpeed.setUnits('MB/second')
_H3cDiskSize_Type=Integer32
_H3cDiskSize_Object=MibTableColumn
h3cDiskSize=_H3cDiskSize_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,4),_H3cDiskSize_Type())
h3cDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskSize.setStatus(_A)
if mibBuilder.loadTexts:h3cDiskSize.setUnits('MB')
_H3cDiskFreeSpace_Type=Integer32
_H3cDiskFreeSpace_Object=MibTableColumn
h3cDiskFreeSpace=_H3cDiskFreeSpace_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,5),_H3cDiskFreeSpace_Type())
h3cDiskFreeSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskFreeSpace.setStatus(_A)
if mibBuilder.loadTexts:h3cDiskFreeSpace.setUnits('MB')
class _H3cDiskLocationState_Type(H3cStorageEnableState):defaultValue=1
_H3cDiskLocationState_Type.__name__=_E
_H3cDiskLocationState_Object=MibTableColumn
h3cDiskLocationState=_H3cDiskLocationState_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,6),_H3cDiskLocationState_Type())
h3cDiskLocationState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDiskLocationState.setStatus(_A)
class _H3cDiskRunLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('blink',2),('fastblink',3)))
_H3cDiskRunLedState_Type.__name__=_C
_H3cDiskRunLedState_Object=MibTableColumn
h3cDiskRunLedState=_H3cDiskRunLedState_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,7),_H3cDiskRunLedState_Type())
h3cDiskRunLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskRunLedState.setStatus(_A)
class _H3cDiskFaultLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('on',2),('blink',3)))
_H3cDiskFaultLedState_Type.__name__=_C
_H3cDiskFaultLedState_Object=MibTableColumn
h3cDiskFaultLedState=_H3cDiskFaultLedState_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,8),_H3cDiskFaultLedState_Type())
h3cDiskFaultLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskFaultLedState.setStatus(_A)
_H3cDiskInitialize_Type=H3cStorageActionType
_H3cDiskInitialize_Object=MibTableColumn
h3cDiskInitialize=_H3cDiskInitialize_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,9),_H3cDiskInitialize_Type())
h3cDiskInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDiskInitialize.setStatus(_A)
class _H3cDiskGlobalSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('globalSpare',1),('nonglobalSpare',2)))
_H3cDiskGlobalSpare_Type.__name__=_C
_H3cDiskGlobalSpare_Object=MibTableColumn
h3cDiskGlobalSpare=_H3cDiskGlobalSpare_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,10),_H3cDiskGlobalSpare_Type())
h3cDiskGlobalSpare.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDiskGlobalSpare.setStatus(_A)
class _H3cDiskLocalSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localSpare',1),('nonlocalSpare',2)))
_H3cDiskLocalSpare_Type.__name__=_C
_H3cDiskLocalSpare_Object=MibTableColumn
h3cDiskLocalSpare=_H3cDiskLocalSpare_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,11),_H3cDiskLocalSpare_Type())
h3cDiskLocalSpare.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskLocalSpare.setStatus(_A)
class _H3cDiskReadCache_Type(H3cStorageEnableState):defaultValue=1
_H3cDiskReadCache_Type.__name__=_E
_H3cDiskReadCache_Object=MibTableColumn
h3cDiskReadCache=_H3cDiskReadCache_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,12),_H3cDiskReadCache_Type())
h3cDiskReadCache.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDiskReadCache.setStatus(_A)
class _H3cDiskWriteCache_Type(H3cStorageEnableState):defaultValue=1
_H3cDiskWriteCache_Type.__name__=_E
_H3cDiskWriteCache_Object=MibTableColumn
h3cDiskWriteCache=_H3cDiskWriteCache_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,13),_H3cDiskWriteCache_Type())
h3cDiskWriteCache.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDiskWriteCache.setStatus(_A)
class _H3cDiskPowerOffReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('environmentUnstable',1),('mediumError',2),('smartCheckError',3),('generalError',4)))
_H3cDiskPowerOffReason_Type.__name__=_C
_H3cDiskPowerOffReason_Object=MibTableColumn
h3cDiskPowerOffReason=_H3cDiskPowerOffReason_Object((1,3,6,1,4,1,2011,10,10,3,1,1,1,14),_H3cDiskPowerOffReason_Type())
h3cDiskPowerOffReason.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDiskPowerOffReason.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'h3cDisk':h3cDisk,'h3cDiskMibObjects':h3cDiskMibObjects,'h3cDiskTable':h3cDiskTable,'h3cDiskEntry':h3cDiskEntry,_G:h3cDiskIndex,'h3cDiskPortType':h3cDiskPortType,'h3cDiskPortSpeed':h3cDiskPortSpeed,'h3cDiskSize':h3cDiskSize,'h3cDiskFreeSpace':h3cDiskFreeSpace,'h3cDiskLocationState':h3cDiskLocationState,'h3cDiskRunLedState':h3cDiskRunLedState,'h3cDiskFaultLedState':h3cDiskFaultLedState,'h3cDiskInitialize':h3cDiskInitialize,'h3cDiskGlobalSpare':h3cDiskGlobalSpare,'h3cDiskLocalSpare':h3cDiskLocalSpare,'h3cDiskReadCache':h3cDiskReadCache,'h3cDiskWriteCache':h3cDiskWriteCache,'h3cDiskPowerOffReason':h3cDiskPowerOffReason})