_G='hh3cDiskIndex'
_F='HH3C-DISK-MIB'
_E='Hh3cStorageEnableState'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Hh3cStorageActionType,Hh3cStorageEnableState,hh3cStorageRef=mibBuilder.importSymbols('HH3C-STORAGE-REF-MIB','Hh3cStorageActionType',_E,'hh3cStorageRef')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hh3cDisk=ModuleIdentity((1,3,6,1,4,1,25506,10,3))
_Hh3cDiskMibObjects_ObjectIdentity=ObjectIdentity
hh3cDiskMibObjects=_Hh3cDiskMibObjects_ObjectIdentity((1,3,6,1,4,1,25506,10,3,1))
_Hh3cDiskTable_Object=MibTable
hh3cDiskTable=_Hh3cDiskTable_Object((1,3,6,1,4,1,25506,10,3,1,1))
if mibBuilder.loadTexts:hh3cDiskTable.setStatus(_A)
_Hh3cDiskEntry_Object=MibTableRow
hh3cDiskEntry=_Hh3cDiskEntry_Object((1,3,6,1,4,1,25506,10,3,1,1,1))
hh3cDiskEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hh3cDiskEntry.setStatus(_A)
_Hh3cDiskIndex_Type=Integer32
_Hh3cDiskIndex_Object=MibTableColumn
hh3cDiskIndex=_Hh3cDiskIndex_Object((1,3,6,1,4,1,25506,10,3,1,1,1,1),_Hh3cDiskIndex_Type())
hh3cDiskIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hh3cDiskIndex.setStatus(_A)
class _Hh3cDiskPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('sata',1),('pata',2),('sas',3),('scsi',4),('ieee1394',5),('fcal',6)))
_Hh3cDiskPortType_Type.__name__=_C
_Hh3cDiskPortType_Object=MibTableColumn
hh3cDiskPortType=_Hh3cDiskPortType_Object((1,3,6,1,4,1,25506,10,3,1,1,1,2),_Hh3cDiskPortType_Type())
hh3cDiskPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskPortType.setStatus(_A)
_Hh3cDiskPortSpeed_Type=Integer32
_Hh3cDiskPortSpeed_Object=MibTableColumn
hh3cDiskPortSpeed=_Hh3cDiskPortSpeed_Object((1,3,6,1,4,1,25506,10,3,1,1,1,3),_Hh3cDiskPortSpeed_Type())
hh3cDiskPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskPortSpeed.setStatus(_A)
if mibBuilder.loadTexts:hh3cDiskPortSpeed.setUnits('MB/second')
_Hh3cDiskSize_Type=Integer32
_Hh3cDiskSize_Object=MibTableColumn
hh3cDiskSize=_Hh3cDiskSize_Object((1,3,6,1,4,1,25506,10,3,1,1,1,4),_Hh3cDiskSize_Type())
hh3cDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskSize.setStatus(_A)
if mibBuilder.loadTexts:hh3cDiskSize.setUnits('MB')
_Hh3cDiskFreeSpace_Type=Integer32
_Hh3cDiskFreeSpace_Object=MibTableColumn
hh3cDiskFreeSpace=_Hh3cDiskFreeSpace_Object((1,3,6,1,4,1,25506,10,3,1,1,1,5),_Hh3cDiskFreeSpace_Type())
hh3cDiskFreeSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskFreeSpace.setStatus(_A)
if mibBuilder.loadTexts:hh3cDiskFreeSpace.setUnits('MB')
class _Hh3cDiskLocationState_Type(Hh3cStorageEnableState):defaultValue=1
_Hh3cDiskLocationState_Type.__name__=_E
_Hh3cDiskLocationState_Object=MibTableColumn
hh3cDiskLocationState=_Hh3cDiskLocationState_Object((1,3,6,1,4,1,25506,10,3,1,1,1,6),_Hh3cDiskLocationState_Type())
hh3cDiskLocationState.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cDiskLocationState.setStatus(_A)
class _Hh3cDiskRunLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('blink',2),('fastblink',3)))
_Hh3cDiskRunLedState_Type.__name__=_C
_Hh3cDiskRunLedState_Object=MibTableColumn
hh3cDiskRunLedState=_Hh3cDiskRunLedState_Object((1,3,6,1,4,1,25506,10,3,1,1,1,7),_Hh3cDiskRunLedState_Type())
hh3cDiskRunLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskRunLedState.setStatus(_A)
class _Hh3cDiskFaultLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('on',2),('blink',3)))
_Hh3cDiskFaultLedState_Type.__name__=_C
_Hh3cDiskFaultLedState_Object=MibTableColumn
hh3cDiskFaultLedState=_Hh3cDiskFaultLedState_Object((1,3,6,1,4,1,25506,10,3,1,1,1,8),_Hh3cDiskFaultLedState_Type())
hh3cDiskFaultLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskFaultLedState.setStatus(_A)
_Hh3cDiskInitialize_Type=Hh3cStorageActionType
_Hh3cDiskInitialize_Object=MibTableColumn
hh3cDiskInitialize=_Hh3cDiskInitialize_Object((1,3,6,1,4,1,25506,10,3,1,1,1,9),_Hh3cDiskInitialize_Type())
hh3cDiskInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cDiskInitialize.setStatus(_A)
class _Hh3cDiskGlobalSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('globalSpare',1),('nonglobalSpare',2)))
_Hh3cDiskGlobalSpare_Type.__name__=_C
_Hh3cDiskGlobalSpare_Object=MibTableColumn
hh3cDiskGlobalSpare=_Hh3cDiskGlobalSpare_Object((1,3,6,1,4,1,25506,10,3,1,1,1,10),_Hh3cDiskGlobalSpare_Type())
hh3cDiskGlobalSpare.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cDiskGlobalSpare.setStatus(_A)
class _Hh3cDiskLocalSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localSpare',1),('nonlocalSpare',2)))
_Hh3cDiskLocalSpare_Type.__name__=_C
_Hh3cDiskLocalSpare_Object=MibTableColumn
hh3cDiskLocalSpare=_Hh3cDiskLocalSpare_Object((1,3,6,1,4,1,25506,10,3,1,1,1,11),_Hh3cDiskLocalSpare_Type())
hh3cDiskLocalSpare.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskLocalSpare.setStatus(_A)
class _Hh3cDiskReadCache_Type(Hh3cStorageEnableState):defaultValue=1
_Hh3cDiskReadCache_Type.__name__=_E
_Hh3cDiskReadCache_Object=MibTableColumn
hh3cDiskReadCache=_Hh3cDiskReadCache_Object((1,3,6,1,4,1,25506,10,3,1,1,1,12),_Hh3cDiskReadCache_Type())
hh3cDiskReadCache.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cDiskReadCache.setStatus(_A)
class _Hh3cDiskWriteCache_Type(Hh3cStorageEnableState):defaultValue=1
_Hh3cDiskWriteCache_Type.__name__=_E
_Hh3cDiskWriteCache_Object=MibTableColumn
hh3cDiskWriteCache=_Hh3cDiskWriteCache_Object((1,3,6,1,4,1,25506,10,3,1,1,1,13),_Hh3cDiskWriteCache_Type())
hh3cDiskWriteCache.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cDiskWriteCache.setStatus(_A)
class _Hh3cDiskPowerOffReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('environmentUnstable',1),('mediumError',2),('smartCheckError',3),('generalError',4)))
_Hh3cDiskPowerOffReason_Type.__name__=_C
_Hh3cDiskPowerOffReason_Object=MibTableColumn
hh3cDiskPowerOffReason=_Hh3cDiskPowerOffReason_Object((1,3,6,1,4,1,25506,10,3,1,1,1,14),_Hh3cDiskPowerOffReason_Type())
hh3cDiskPowerOffReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hh3cDiskPowerOffReason.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hh3cDisk':hh3cDisk,'hh3cDiskMibObjects':hh3cDiskMibObjects,'hh3cDiskTable':hh3cDiskTable,'hh3cDiskEntry':hh3cDiskEntry,_G:hh3cDiskIndex,'hh3cDiskPortType':hh3cDiskPortType,'hh3cDiskPortSpeed':hh3cDiskPortSpeed,'hh3cDiskSize':hh3cDiskSize,'hh3cDiskFreeSpace':hh3cDiskFreeSpace,'hh3cDiskLocationState':hh3cDiskLocationState,'hh3cDiskRunLedState':hh3cDiskRunLedState,'hh3cDiskFaultLedState':hh3cDiskFaultLedState,'hh3cDiskInitialize':hh3cDiskInitialize,'hh3cDiskGlobalSpare':hh3cDiskGlobalSpare,'hh3cDiskLocalSpare':hh3cDiskLocalSpare,'hh3cDiskReadCache':hh3cDiskReadCache,'hh3cDiskWriteCache':hh3cDiskWriteCache,'hh3cDiskPowerOffReason':hh3cDiskPowerOffReason})