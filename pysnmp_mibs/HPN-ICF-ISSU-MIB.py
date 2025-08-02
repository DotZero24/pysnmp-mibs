_d='hpnicfIssuOpTimeCompleted'
_c='hpnicfIssuFailedReason'
_b='hpnicfIssuOpStatus'
_a='hpnicfIssuOpType'
_Z='hpnicfIssuUpgradeResultIndex'
_Y='incompatibleUpgrade'
_X='fileUpgrade'
_W='serviceUpgrade'
_V='issuReboot'
_U='sequenceReboot'
_T='reboot'
_S='hpnicfIssuTestResultIndex'
_R='rollbackSuccess'
_Q='rollbackInProgress'
_P='inProgress'
_O='rollback'
_N='install'
_M='hpnicfIssuUpgradeImageIndex'
_L='success'
_K='read-write'
_J='read-create'
_I='not-accessible'
_H='TruthValue'
_G='failure'
_F='none'
_E='HPN-ICF-ISSU-MIB'
_D='DisplayString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_H)
hpnicfIssuUpgrade=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133))
if mibBuilder.loadTexts:hpnicfIssuUpgrade.setRevisions(('2013-01-15 15:36',))
_HpnicfIssuUpgradeMibObjects_ObjectIdentity=ObjectIdentity
hpnicfIssuUpgradeMibObjects=_HpnicfIssuUpgradeMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,1))
_HpnicfIssuUpgradeGroup_ObjectIdentity=ObjectIdentity
hpnicfIssuUpgradeGroup=_HpnicfIssuUpgradeGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1))
_HpnicfIssuUpgradeImageTable_Object=MibTable
hpnicfIssuUpgradeImageTable=_HpnicfIssuUpgradeImageTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,1))
if mibBuilder.loadTexts:hpnicfIssuUpgradeImageTable.setStatus(_A)
_HpnicfIssuUpgradeImageEntry_Object=MibTableRow
hpnicfIssuUpgradeImageEntry=_HpnicfIssuUpgradeImageEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,1,1))
hpnicfIssuUpgradeImageEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:hpnicfIssuUpgradeImageEntry.setStatus(_A)
class _HpnicfIssuUpgradeImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIssuUpgradeImageIndex_Type.__name__=_B
_HpnicfIssuUpgradeImageIndex_Object=MibTableColumn
hpnicfIssuUpgradeImageIndex=_HpnicfIssuUpgradeImageIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,1,1,1),_HpnicfIssuUpgradeImageIndex_Type())
hpnicfIssuUpgradeImageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIssuUpgradeImageIndex.setStatus(_A)
class _HpnicfIssuUpgradeImageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('boot',1),('system',2),('feature',3),('ipe',4)))
_HpnicfIssuUpgradeImageType_Type.__name__=_B
_HpnicfIssuUpgradeImageType_Object=MibTableColumn
hpnicfIssuUpgradeImageType=_HpnicfIssuUpgradeImageType_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,1,1,2),_HpnicfIssuUpgradeImageType_Type())
hpnicfIssuUpgradeImageType.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfIssuUpgradeImageType.setStatus(_A)
class _HpnicfIssuUpgradeImageURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_HpnicfIssuUpgradeImageURL_Type.__name__=_D
_HpnicfIssuUpgradeImageURL_Object=MibTableColumn
hpnicfIssuUpgradeImageURL=_HpnicfIssuUpgradeImageURL_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,1,1,3),_HpnicfIssuUpgradeImageURL_Type())
hpnicfIssuUpgradeImageURL.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfIssuUpgradeImageURL.setStatus(_A)
_HpnicfIssuUpgradeImageRowStatus_Type=RowStatus
_HpnicfIssuUpgradeImageRowStatus_Object=MibTableColumn
hpnicfIssuUpgradeImageRowStatus=_HpnicfIssuUpgradeImageRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,1,1,4),_HpnicfIssuUpgradeImageRowStatus_Type())
hpnicfIssuUpgradeImageRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfIssuUpgradeImageRowStatus.setStatus(_A)
_HpnicfIssuOp_ObjectIdentity=ObjectIdentity
hpnicfIssuOp=_HpnicfIssuOp_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2))
class _HpnicfIssuOpType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('done',2),('test',3),(_N,4),(_O,5)))
_HpnicfIssuOpType_Type.__name__=_B
_HpnicfIssuOpType_Object=MibScalar
hpnicfIssuOpType=_HpnicfIssuOpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,1),_HpnicfIssuOpType_Type())
hpnicfIssuOpType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfIssuOpType.setStatus(_A)
class _HpnicfIssuImageFileOverwrite_Type(TruthValue):defaultValue=1
_HpnicfIssuImageFileOverwrite_Type.__name__=_H
_HpnicfIssuImageFileOverwrite_Object=MibScalar
hpnicfIssuImageFileOverwrite=_HpnicfIssuImageFileOverwrite_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,2),_HpnicfIssuImageFileOverwrite_Type())
hpnicfIssuImageFileOverwrite.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfIssuImageFileOverwrite.setStatus(_A)
class _HpnicfIssuOpTrapEnable_Type(TruthValue):defaultValue=1
_HpnicfIssuOpTrapEnable_Type.__name__=_H
_HpnicfIssuOpTrapEnable_Object=MibScalar
hpnicfIssuOpTrapEnable=_HpnicfIssuOpTrapEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,3),_HpnicfIssuOpTrapEnable_Type())
hpnicfIssuOpTrapEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfIssuOpTrapEnable.setStatus(_A)
class _HpnicfIssuOpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_P,3),(_L,4),(_Q,5),(_R,6)))
_HpnicfIssuOpStatus_Type.__name__=_B
_HpnicfIssuOpStatus_Object=MibScalar
hpnicfIssuOpStatus=_HpnicfIssuOpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,4),_HpnicfIssuOpStatus_Type())
hpnicfIssuOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuOpStatus.setStatus(_A)
class _HpnicfIssuFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIssuFailedReason_Type.__name__=_D
_HpnicfIssuFailedReason_Object=MibScalar
hpnicfIssuFailedReason=_HpnicfIssuFailedReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,5),_HpnicfIssuFailedReason_Type())
hpnicfIssuFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuFailedReason.setStatus(_A)
class _HpnicfIssuOpTimeCompleted_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIssuOpTimeCompleted_Type.__name__=_D
_HpnicfIssuOpTimeCompleted_Object=MibScalar
hpnicfIssuOpTimeCompleted=_HpnicfIssuOpTimeCompleted_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,6),_HpnicfIssuOpTimeCompleted_Type())
hpnicfIssuOpTimeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuOpTimeCompleted.setStatus(_A)
class _HpnicfIssuLastOpType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('done',2),('test',3),(_N,4),(_O,5)))
_HpnicfIssuLastOpType_Type.__name__=_B
_HpnicfIssuLastOpType_Object=MibScalar
hpnicfIssuLastOpType=_HpnicfIssuLastOpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,7),_HpnicfIssuLastOpType_Type())
hpnicfIssuLastOpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuLastOpType.setStatus(_A)
class _HpnicfIssuLastOpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_P,3),(_L,4),(_Q,5),(_R,6)))
_HpnicfIssuLastOpStatus_Type.__name__=_B
_HpnicfIssuLastOpStatus_Object=MibScalar
hpnicfIssuLastOpStatus=_HpnicfIssuLastOpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,8),_HpnicfIssuLastOpStatus_Type())
hpnicfIssuLastOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuLastOpStatus.setStatus(_A)
class _HpnicfIssuLastOpFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIssuLastOpFailedReason_Type.__name__=_D
_HpnicfIssuLastOpFailedReason_Object=MibScalar
hpnicfIssuLastOpFailedReason=_HpnicfIssuLastOpFailedReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,9),_HpnicfIssuLastOpFailedReason_Type())
hpnicfIssuLastOpFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuLastOpFailedReason.setStatus(_A)
class _HpnicfIssuLastOpTimeCompleted_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIssuLastOpTimeCompleted_Type.__name__=_D
_HpnicfIssuLastOpTimeCompleted_Object=MibScalar
hpnicfIssuLastOpTimeCompleted=_HpnicfIssuLastOpTimeCompleted_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,1,2,10),_HpnicfIssuLastOpTimeCompleted_Type())
hpnicfIssuLastOpTimeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuLastOpTimeCompleted.setStatus(_A)
_HpnicfIssuUpgradeResultGroup_ObjectIdentity=ObjectIdentity
hpnicfIssuUpgradeResultGroup=_HpnicfIssuUpgradeResultGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2))
_HpnicfIssuCompatibleResult_ObjectIdentity=ObjectIdentity
hpnicfIssuCompatibleResult=_HpnicfIssuCompatibleResult_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,1))
class _HpnicfIssuCompatibleResultStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('inCompatible',2),('compatible',3),(_G,4)))
_HpnicfIssuCompatibleResultStatus_Type.__name__=_B
_HpnicfIssuCompatibleResultStatus_Object=MibScalar
hpnicfIssuCompatibleResultStatus=_HpnicfIssuCompatibleResultStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,1,1),_HpnicfIssuCompatibleResultStatus_Type())
hpnicfIssuCompatibleResultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuCompatibleResultStatus.setStatus(_A)
class _HpnicfIssuCompatibleResultFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIssuCompatibleResultFailedReason_Type.__name__=_D
_HpnicfIssuCompatibleResultFailedReason_Object=MibScalar
hpnicfIssuCompatibleResultFailedReason=_HpnicfIssuCompatibleResultFailedReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,1,2),_HpnicfIssuCompatibleResultFailedReason_Type())
hpnicfIssuCompatibleResultFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuCompatibleResultFailedReason.setStatus(_A)
_HpnicfIssuTestResultTable_Object=MibTable
hpnicfIssuTestResultTable=_HpnicfIssuTestResultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2))
if mibBuilder.loadTexts:hpnicfIssuTestResultTable.setStatus(_A)
_HpnicfIssuTestResultEntry_Object=MibTableRow
hpnicfIssuTestResultEntry=_HpnicfIssuTestResultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2,1))
hpnicfIssuTestResultEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:hpnicfIssuTestResultEntry.setStatus(_A)
class _HpnicfIssuTestResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfIssuTestResultIndex_Type.__name__=_B
_HpnicfIssuTestResultIndex_Object=MibTableColumn
hpnicfIssuTestResultIndex=_HpnicfIssuTestResultIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2,1,1),_HpnicfIssuTestResultIndex_Type())
hpnicfIssuTestResultIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIssuTestResultIndex.setStatus(_A)
class _HpnicfIssuTestDeviceChassisID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfIssuTestDeviceChassisID_Type.__name__=_B
_HpnicfIssuTestDeviceChassisID_Object=MibTableColumn
hpnicfIssuTestDeviceChassisID=_HpnicfIssuTestDeviceChassisID_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2,1,2),_HpnicfIssuTestDeviceChassisID_Type())
hpnicfIssuTestDeviceChassisID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuTestDeviceChassisID.setStatus(_A)
class _HpnicfIssuTestDeviceSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfIssuTestDeviceSlotID_Type.__name__=_B
_HpnicfIssuTestDeviceSlotID_Object=MibTableColumn
hpnicfIssuTestDeviceSlotID=_HpnicfIssuTestDeviceSlotID_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2,1,3),_HpnicfIssuTestDeviceSlotID_Type())
hpnicfIssuTestDeviceSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuTestDeviceSlotID.setStatus(_A)
class _HpnicfIssuTestDeviceCpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfIssuTestDeviceCpuID_Type.__name__=_B
_HpnicfIssuTestDeviceCpuID_Object=MibTableColumn
hpnicfIssuTestDeviceCpuID=_HpnicfIssuTestDeviceCpuID_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2,1,4),_HpnicfIssuTestDeviceCpuID_Type())
hpnicfIssuTestDeviceCpuID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuTestDeviceCpuID.setStatus(_A)
class _HpnicfIssuTestDeviceUpgradeWay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,6),(_Y,7)))
_HpnicfIssuTestDeviceUpgradeWay_Type.__name__=_B
_HpnicfIssuTestDeviceUpgradeWay_Object=MibTableColumn
hpnicfIssuTestDeviceUpgradeWay=_HpnicfIssuTestDeviceUpgradeWay_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,2,1,5),_HpnicfIssuTestDeviceUpgradeWay_Type())
hpnicfIssuTestDeviceUpgradeWay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuTestDeviceUpgradeWay.setStatus(_A)
_HpnicfIssuUpgradeResultTable_Object=MibTable
hpnicfIssuUpgradeResultTable=_HpnicfIssuUpgradeResultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3))
if mibBuilder.loadTexts:hpnicfIssuUpgradeResultTable.setStatus(_A)
_HpnicfIssuUpgradeResultEntry_Object=MibTableRow
hpnicfIssuUpgradeResultEntry=_HpnicfIssuUpgradeResultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1))
hpnicfIssuUpgradeResultEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:hpnicfIssuUpgradeResultEntry.setStatus(_A)
class _HpnicfIssuUpgradeResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfIssuUpgradeResultIndex_Type.__name__=_B
_HpnicfIssuUpgradeResultIndex_Object=MibTableColumn
hpnicfIssuUpgradeResultIndex=_HpnicfIssuUpgradeResultIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,1),_HpnicfIssuUpgradeResultIndex_Type())
hpnicfIssuUpgradeResultIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIssuUpgradeResultIndex.setStatus(_A)
class _HpnicfIssuUpgradeDeviceChassisID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfIssuUpgradeDeviceChassisID_Type.__name__=_B
_HpnicfIssuUpgradeDeviceChassisID_Object=MibTableColumn
hpnicfIssuUpgradeDeviceChassisID=_HpnicfIssuUpgradeDeviceChassisID_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,2),_HpnicfIssuUpgradeDeviceChassisID_Type())
hpnicfIssuUpgradeDeviceChassisID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuUpgradeDeviceChassisID.setStatus(_A)
class _HpnicfIssuUpgradeDeviceSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfIssuUpgradeDeviceSlotID_Type.__name__=_B
_HpnicfIssuUpgradeDeviceSlotID_Object=MibTableColumn
hpnicfIssuUpgradeDeviceSlotID=_HpnicfIssuUpgradeDeviceSlotID_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,3),_HpnicfIssuUpgradeDeviceSlotID_Type())
hpnicfIssuUpgradeDeviceSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuUpgradeDeviceSlotID.setStatus(_A)
class _HpnicfIssuUpgradeDeviceCpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfIssuUpgradeDeviceCpuID_Type.__name__=_B
_HpnicfIssuUpgradeDeviceCpuID_Object=MibTableColumn
hpnicfIssuUpgradeDeviceCpuID=_HpnicfIssuUpgradeDeviceCpuID_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,4),_HpnicfIssuUpgradeDeviceCpuID_Type())
hpnicfIssuUpgradeDeviceCpuID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuUpgradeDeviceCpuID.setStatus(_A)
class _HpnicfIssuUpgradeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('init',1),('loading',2),('loaded',3),('switching',4),('switchover',5),('committing',6),('committed',7),('rollbacking',8),('rollbacked',9)))
_HpnicfIssuUpgradeState_Type.__name__=_B
_HpnicfIssuUpgradeState_Object=MibTableColumn
hpnicfIssuUpgradeState=_HpnicfIssuUpgradeState_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,5),_HpnicfIssuUpgradeState_Type())
hpnicfIssuUpgradeState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuUpgradeState.setStatus(_A)
class _HpnicfIssuDeviceUpgradeWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,6),(_Y,7)))
_HpnicfIssuDeviceUpgradeWay_Type.__name__=_B
_HpnicfIssuDeviceUpgradeWay_Object=MibTableColumn
hpnicfIssuDeviceUpgradeWay=_HpnicfIssuDeviceUpgradeWay_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,6),_HpnicfIssuDeviceUpgradeWay_Type())
hpnicfIssuDeviceUpgradeWay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuDeviceUpgradeWay.setStatus(_A)
class _HpnicfIssuUpgradeDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('waitingUpgrade',1),('inProcess',2),(_L,3),(_G,4)))
_HpnicfIssuUpgradeDeviceStatus_Type.__name__=_B
_HpnicfIssuUpgradeDeviceStatus_Object=MibTableColumn
hpnicfIssuUpgradeDeviceStatus=_HpnicfIssuUpgradeDeviceStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,7),_HpnicfIssuUpgradeDeviceStatus_Type())
hpnicfIssuUpgradeDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuUpgradeDeviceStatus.setStatus(_A)
class _HpnicfIssuUpgradeFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIssuUpgradeFailedReason_Type.__name__=_D
_HpnicfIssuUpgradeFailedReason_Object=MibTableColumn
hpnicfIssuUpgradeFailedReason=_HpnicfIssuUpgradeFailedReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,133,1,2,3,1,8),_HpnicfIssuUpgradeFailedReason_Type())
hpnicfIssuUpgradeFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIssuUpgradeFailedReason.setStatus(_A)
_HpnicfIssuUpgradeNotify_ObjectIdentity=ObjectIdentity
hpnicfIssuUpgradeNotify=_HpnicfIssuUpgradeNotify_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,2))
_HpnicfIssuUpgradeTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfIssuUpgradeTrapPrefix=_HpnicfIssuUpgradeTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,133,2,0))
hpnicfIssuUpgradeOpCompletionNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,133,2,0,1))
hpnicfIssuUpgradeOpCompletionNotify.setObjects(*((_E,_a),(_E,_b),(_E,_c),(_E,_d)))
if mibBuilder.loadTexts:hpnicfIssuUpgradeOpCompletionNotify.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfIssuUpgrade':hpnicfIssuUpgrade,'hpnicfIssuUpgradeMibObjects':hpnicfIssuUpgradeMibObjects,'hpnicfIssuUpgradeGroup':hpnicfIssuUpgradeGroup,'hpnicfIssuUpgradeImageTable':hpnicfIssuUpgradeImageTable,'hpnicfIssuUpgradeImageEntry':hpnicfIssuUpgradeImageEntry,_M:hpnicfIssuUpgradeImageIndex,'hpnicfIssuUpgradeImageType':hpnicfIssuUpgradeImageType,'hpnicfIssuUpgradeImageURL':hpnicfIssuUpgradeImageURL,'hpnicfIssuUpgradeImageRowStatus':hpnicfIssuUpgradeImageRowStatus,'hpnicfIssuOp':hpnicfIssuOp,_a:hpnicfIssuOpType,'hpnicfIssuImageFileOverwrite':hpnicfIssuImageFileOverwrite,'hpnicfIssuOpTrapEnable':hpnicfIssuOpTrapEnable,_b:hpnicfIssuOpStatus,_c:hpnicfIssuFailedReason,_d:hpnicfIssuOpTimeCompleted,'hpnicfIssuLastOpType':hpnicfIssuLastOpType,'hpnicfIssuLastOpStatus':hpnicfIssuLastOpStatus,'hpnicfIssuLastOpFailedReason':hpnicfIssuLastOpFailedReason,'hpnicfIssuLastOpTimeCompleted':hpnicfIssuLastOpTimeCompleted,'hpnicfIssuUpgradeResultGroup':hpnicfIssuUpgradeResultGroup,'hpnicfIssuCompatibleResult':hpnicfIssuCompatibleResult,'hpnicfIssuCompatibleResultStatus':hpnicfIssuCompatibleResultStatus,'hpnicfIssuCompatibleResultFailedReason':hpnicfIssuCompatibleResultFailedReason,'hpnicfIssuTestResultTable':hpnicfIssuTestResultTable,'hpnicfIssuTestResultEntry':hpnicfIssuTestResultEntry,_S:hpnicfIssuTestResultIndex,'hpnicfIssuTestDeviceChassisID':hpnicfIssuTestDeviceChassisID,'hpnicfIssuTestDeviceSlotID':hpnicfIssuTestDeviceSlotID,'hpnicfIssuTestDeviceCpuID':hpnicfIssuTestDeviceCpuID,'hpnicfIssuTestDeviceUpgradeWay':hpnicfIssuTestDeviceUpgradeWay,'hpnicfIssuUpgradeResultTable':hpnicfIssuUpgradeResultTable,'hpnicfIssuUpgradeResultEntry':hpnicfIssuUpgradeResultEntry,_Z:hpnicfIssuUpgradeResultIndex,'hpnicfIssuUpgradeDeviceChassisID':hpnicfIssuUpgradeDeviceChassisID,'hpnicfIssuUpgradeDeviceSlotID':hpnicfIssuUpgradeDeviceSlotID,'hpnicfIssuUpgradeDeviceCpuID':hpnicfIssuUpgradeDeviceCpuID,'hpnicfIssuUpgradeState':hpnicfIssuUpgradeState,'hpnicfIssuDeviceUpgradeWay':hpnicfIssuDeviceUpgradeWay,'hpnicfIssuUpgradeDeviceStatus':hpnicfIssuUpgradeDeviceStatus,'hpnicfIssuUpgradeFailedReason':hpnicfIssuUpgradeFailedReason,'hpnicfIssuUpgradeNotify':hpnicfIssuUpgradeNotify,'hpnicfIssuUpgradeTrapPrefix':hpnicfIssuUpgradeTrapPrefix,'hpnicfIssuUpgradeOpCompletionNotify':hpnicfIssuUpgradeOpCompletionNotify})