_d='h3cIssuOpTimeCompleted'
_c='h3cIssuFailedReason'
_b='h3cIssuOpStatus'
_a='h3cIssuOpType'
_Z='h3cIssuUpgradeResultIndex'
_Y='incompatibleUpgrade'
_X='fileUpgrade'
_W='serviceUpgrade'
_V='issuReboot'
_U='sequenceReboot'
_T='reboot'
_S='h3cIssuTestResultIndex'
_R='rollbackSuccess'
_Q='rollbackInProgress'
_P='inProgress'
_O='rollback'
_N='install'
_M='h3cIssuUpgradeImageIndex'
_L='success'
_K='read-write'
_J='read-create'
_I='not-accessible'
_H='TruthValue'
_G='failure'
_F='none'
_E='H3C-ISSU-MIB'
_D='DisplayString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_H)
h3cIssuUpgrade=ModuleIdentity((1,3,6,1,4,1,2011,10,2,133))
if mibBuilder.loadTexts:h3cIssuUpgrade.setRevisions(('2013-01-15 15:36',))
_H3cIssuUpgradeMibObjects_ObjectIdentity=ObjectIdentity
h3cIssuUpgradeMibObjects=_H3cIssuUpgradeMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,1))
_H3cIssuUpgradeGroup_ObjectIdentity=ObjectIdentity
h3cIssuUpgradeGroup=_H3cIssuUpgradeGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,1,1))
_H3cIssuUpgradeImageTable_Object=MibTable
h3cIssuUpgradeImageTable=_H3cIssuUpgradeImageTable_Object((1,3,6,1,4,1,2011,10,2,133,1,1,1))
if mibBuilder.loadTexts:h3cIssuUpgradeImageTable.setStatus(_A)
_H3cIssuUpgradeImageEntry_Object=MibTableRow
h3cIssuUpgradeImageEntry=_H3cIssuUpgradeImageEntry_Object((1,3,6,1,4,1,2011,10,2,133,1,1,1,1))
h3cIssuUpgradeImageEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:h3cIssuUpgradeImageEntry.setStatus(_A)
class _H3cIssuUpgradeImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIssuUpgradeImageIndex_Type.__name__=_B
_H3cIssuUpgradeImageIndex_Object=MibTableColumn
h3cIssuUpgradeImageIndex=_H3cIssuUpgradeImageIndex_Object((1,3,6,1,4,1,2011,10,2,133,1,1,1,1,1),_H3cIssuUpgradeImageIndex_Type())
h3cIssuUpgradeImageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cIssuUpgradeImageIndex.setStatus(_A)
class _H3cIssuUpgradeImageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('boot',1),('system',2),('feature',3),('ipe',4),('patch',5)))
_H3cIssuUpgradeImageType_Type.__name__=_B
_H3cIssuUpgradeImageType_Object=MibTableColumn
h3cIssuUpgradeImageType=_H3cIssuUpgradeImageType_Object((1,3,6,1,4,1,2011,10,2,133,1,1,1,1,2),_H3cIssuUpgradeImageType_Type())
h3cIssuUpgradeImageType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIssuUpgradeImageType.setStatus(_A)
class _H3cIssuUpgradeImageURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cIssuUpgradeImageURL_Type.__name__=_D
_H3cIssuUpgradeImageURL_Object=MibTableColumn
h3cIssuUpgradeImageURL=_H3cIssuUpgradeImageURL_Object((1,3,6,1,4,1,2011,10,2,133,1,1,1,1,3),_H3cIssuUpgradeImageURL_Type())
h3cIssuUpgradeImageURL.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIssuUpgradeImageURL.setStatus(_A)
_H3cIssuUpgradeImageRowStatus_Type=RowStatus
_H3cIssuUpgradeImageRowStatus_Object=MibTableColumn
h3cIssuUpgradeImageRowStatus=_H3cIssuUpgradeImageRowStatus_Object((1,3,6,1,4,1,2011,10,2,133,1,1,1,1,4),_H3cIssuUpgradeImageRowStatus_Type())
h3cIssuUpgradeImageRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIssuUpgradeImageRowStatus.setStatus(_A)
_H3cIssuOp_ObjectIdentity=ObjectIdentity
h3cIssuOp=_H3cIssuOp_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,1,1,2))
class _H3cIssuOpType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('done',2),('test',3),(_N,4),(_O,5)))
_H3cIssuOpType_Type.__name__=_B
_H3cIssuOpType_Object=MibScalar
h3cIssuOpType=_H3cIssuOpType_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,1),_H3cIssuOpType_Type())
h3cIssuOpType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cIssuOpType.setStatus(_A)
class _H3cIssuImageFileOverwrite_Type(TruthValue):defaultValue=1
_H3cIssuImageFileOverwrite_Type.__name__=_H
_H3cIssuImageFileOverwrite_Object=MibScalar
h3cIssuImageFileOverwrite=_H3cIssuImageFileOverwrite_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,2),_H3cIssuImageFileOverwrite_Type())
h3cIssuImageFileOverwrite.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cIssuImageFileOverwrite.setStatus(_A)
class _H3cIssuOpTrapEnable_Type(TruthValue):defaultValue=1
_H3cIssuOpTrapEnable_Type.__name__=_H
_H3cIssuOpTrapEnable_Object=MibScalar
h3cIssuOpTrapEnable=_H3cIssuOpTrapEnable_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,3),_H3cIssuOpTrapEnable_Type())
h3cIssuOpTrapEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cIssuOpTrapEnable.setStatus(_A)
class _H3cIssuOpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_P,3),(_L,4),(_Q,5),(_R,6)))
_H3cIssuOpStatus_Type.__name__=_B
_H3cIssuOpStatus_Object=MibScalar
h3cIssuOpStatus=_H3cIssuOpStatus_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,4),_H3cIssuOpStatus_Type())
h3cIssuOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuOpStatus.setStatus(_A)
class _H3cIssuFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIssuFailedReason_Type.__name__=_D
_H3cIssuFailedReason_Object=MibScalar
h3cIssuFailedReason=_H3cIssuFailedReason_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,5),_H3cIssuFailedReason_Type())
h3cIssuFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuFailedReason.setStatus(_A)
class _H3cIssuOpTimeCompleted_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIssuOpTimeCompleted_Type.__name__=_D
_H3cIssuOpTimeCompleted_Object=MibScalar
h3cIssuOpTimeCompleted=_H3cIssuOpTimeCompleted_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,6),_H3cIssuOpTimeCompleted_Type())
h3cIssuOpTimeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuOpTimeCompleted.setStatus(_A)
class _H3cIssuLastOpType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('done',2),('test',3),(_N,4),(_O,5)))
_H3cIssuLastOpType_Type.__name__=_B
_H3cIssuLastOpType_Object=MibScalar
h3cIssuLastOpType=_H3cIssuLastOpType_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,7),_H3cIssuLastOpType_Type())
h3cIssuLastOpType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuLastOpType.setStatus(_A)
class _H3cIssuLastOpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_G,2),(_P,3),(_L,4),(_Q,5),(_R,6)))
_H3cIssuLastOpStatus_Type.__name__=_B
_H3cIssuLastOpStatus_Object=MibScalar
h3cIssuLastOpStatus=_H3cIssuLastOpStatus_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,8),_H3cIssuLastOpStatus_Type())
h3cIssuLastOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuLastOpStatus.setStatus(_A)
class _H3cIssuLastOpFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIssuLastOpFailedReason_Type.__name__=_D
_H3cIssuLastOpFailedReason_Object=MibScalar
h3cIssuLastOpFailedReason=_H3cIssuLastOpFailedReason_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,9),_H3cIssuLastOpFailedReason_Type())
h3cIssuLastOpFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuLastOpFailedReason.setStatus(_A)
class _H3cIssuLastOpTimeCompleted_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIssuLastOpTimeCompleted_Type.__name__=_D
_H3cIssuLastOpTimeCompleted_Object=MibScalar
h3cIssuLastOpTimeCompleted=_H3cIssuLastOpTimeCompleted_Object((1,3,6,1,4,1,2011,10,2,133,1,1,2,10),_H3cIssuLastOpTimeCompleted_Type())
h3cIssuLastOpTimeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuLastOpTimeCompleted.setStatus(_A)
_H3cIssuUpgradeResultGroup_ObjectIdentity=ObjectIdentity
h3cIssuUpgradeResultGroup=_H3cIssuUpgradeResultGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,1,2))
_H3cIssuCompatibleResult_ObjectIdentity=ObjectIdentity
h3cIssuCompatibleResult=_H3cIssuCompatibleResult_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,1,2,1))
class _H3cIssuCompatibleResultStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('inCompatible',2),('compatible',3),(_G,4)))
_H3cIssuCompatibleResultStatus_Type.__name__=_B
_H3cIssuCompatibleResultStatus_Object=MibScalar
h3cIssuCompatibleResultStatus=_H3cIssuCompatibleResultStatus_Object((1,3,6,1,4,1,2011,10,2,133,1,2,1,1),_H3cIssuCompatibleResultStatus_Type())
h3cIssuCompatibleResultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuCompatibleResultStatus.setStatus(_A)
class _H3cIssuCompatibleResultFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIssuCompatibleResultFailedReason_Type.__name__=_D
_H3cIssuCompatibleResultFailedReason_Object=MibScalar
h3cIssuCompatibleResultFailedReason=_H3cIssuCompatibleResultFailedReason_Object((1,3,6,1,4,1,2011,10,2,133,1,2,1,2),_H3cIssuCompatibleResultFailedReason_Type())
h3cIssuCompatibleResultFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuCompatibleResultFailedReason.setStatus(_A)
_H3cIssuTestResultTable_Object=MibTable
h3cIssuTestResultTable=_H3cIssuTestResultTable_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2))
if mibBuilder.loadTexts:h3cIssuTestResultTable.setStatus(_A)
_H3cIssuTestResultEntry_Object=MibTableRow
h3cIssuTestResultEntry=_H3cIssuTestResultEntry_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2,1))
h3cIssuTestResultEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:h3cIssuTestResultEntry.setStatus(_A)
class _H3cIssuTestResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cIssuTestResultIndex_Type.__name__=_B
_H3cIssuTestResultIndex_Object=MibTableColumn
h3cIssuTestResultIndex=_H3cIssuTestResultIndex_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2,1,1),_H3cIssuTestResultIndex_Type())
h3cIssuTestResultIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cIssuTestResultIndex.setStatus(_A)
class _H3cIssuTestDeviceChassisID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cIssuTestDeviceChassisID_Type.__name__=_B
_H3cIssuTestDeviceChassisID_Object=MibTableColumn
h3cIssuTestDeviceChassisID=_H3cIssuTestDeviceChassisID_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2,1,2),_H3cIssuTestDeviceChassisID_Type())
h3cIssuTestDeviceChassisID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuTestDeviceChassisID.setStatus(_A)
class _H3cIssuTestDeviceSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cIssuTestDeviceSlotID_Type.__name__=_B
_H3cIssuTestDeviceSlotID_Object=MibTableColumn
h3cIssuTestDeviceSlotID=_H3cIssuTestDeviceSlotID_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2,1,3),_H3cIssuTestDeviceSlotID_Type())
h3cIssuTestDeviceSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuTestDeviceSlotID.setStatus(_A)
class _H3cIssuTestDeviceCpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cIssuTestDeviceCpuID_Type.__name__=_B
_H3cIssuTestDeviceCpuID_Object=MibTableColumn
h3cIssuTestDeviceCpuID=_H3cIssuTestDeviceCpuID_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2,1,4),_H3cIssuTestDeviceCpuID_Type())
h3cIssuTestDeviceCpuID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuTestDeviceCpuID.setStatus(_A)
class _H3cIssuTestDeviceUpgradeWay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,6),(_Y,7)))
_H3cIssuTestDeviceUpgradeWay_Type.__name__=_B
_H3cIssuTestDeviceUpgradeWay_Object=MibTableColumn
h3cIssuTestDeviceUpgradeWay=_H3cIssuTestDeviceUpgradeWay_Object((1,3,6,1,4,1,2011,10,2,133,1,2,2,1,5),_H3cIssuTestDeviceUpgradeWay_Type())
h3cIssuTestDeviceUpgradeWay.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuTestDeviceUpgradeWay.setStatus(_A)
_H3cIssuUpgradeResultTable_Object=MibTable
h3cIssuUpgradeResultTable=_H3cIssuUpgradeResultTable_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3))
if mibBuilder.loadTexts:h3cIssuUpgradeResultTable.setStatus(_A)
_H3cIssuUpgradeResultEntry_Object=MibTableRow
h3cIssuUpgradeResultEntry=_H3cIssuUpgradeResultEntry_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1))
h3cIssuUpgradeResultEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:h3cIssuUpgradeResultEntry.setStatus(_A)
class _H3cIssuUpgradeResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cIssuUpgradeResultIndex_Type.__name__=_B
_H3cIssuUpgradeResultIndex_Object=MibTableColumn
h3cIssuUpgradeResultIndex=_H3cIssuUpgradeResultIndex_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,1),_H3cIssuUpgradeResultIndex_Type())
h3cIssuUpgradeResultIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cIssuUpgradeResultIndex.setStatus(_A)
class _H3cIssuUpgradeDeviceChassisID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cIssuUpgradeDeviceChassisID_Type.__name__=_B
_H3cIssuUpgradeDeviceChassisID_Object=MibTableColumn
h3cIssuUpgradeDeviceChassisID=_H3cIssuUpgradeDeviceChassisID_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,2),_H3cIssuUpgradeDeviceChassisID_Type())
h3cIssuUpgradeDeviceChassisID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuUpgradeDeviceChassisID.setStatus(_A)
class _H3cIssuUpgradeDeviceSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cIssuUpgradeDeviceSlotID_Type.__name__=_B
_H3cIssuUpgradeDeviceSlotID_Object=MibTableColumn
h3cIssuUpgradeDeviceSlotID=_H3cIssuUpgradeDeviceSlotID_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,3),_H3cIssuUpgradeDeviceSlotID_Type())
h3cIssuUpgradeDeviceSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuUpgradeDeviceSlotID.setStatus(_A)
class _H3cIssuUpgradeDeviceCpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cIssuUpgradeDeviceCpuID_Type.__name__=_B
_H3cIssuUpgradeDeviceCpuID_Object=MibTableColumn
h3cIssuUpgradeDeviceCpuID=_H3cIssuUpgradeDeviceCpuID_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,4),_H3cIssuUpgradeDeviceCpuID_Type())
h3cIssuUpgradeDeviceCpuID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuUpgradeDeviceCpuID.setStatus(_A)
class _H3cIssuUpgradeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('init',1),('loading',2),('loaded',3),('switching',4),('switchover',5),('committing',6),('committed',7),('rollbacking',8),('rollbacked',9)))
_H3cIssuUpgradeState_Type.__name__=_B
_H3cIssuUpgradeState_Object=MibTableColumn
h3cIssuUpgradeState=_H3cIssuUpgradeState_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,5),_H3cIssuUpgradeState_Type())
h3cIssuUpgradeState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuUpgradeState.setStatus(_A)
class _H3cIssuDeviceUpgradeWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,6),(_Y,7)))
_H3cIssuDeviceUpgradeWay_Type.__name__=_B
_H3cIssuDeviceUpgradeWay_Object=MibTableColumn
h3cIssuDeviceUpgradeWay=_H3cIssuDeviceUpgradeWay_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,6),_H3cIssuDeviceUpgradeWay_Type())
h3cIssuDeviceUpgradeWay.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuDeviceUpgradeWay.setStatus(_A)
class _H3cIssuUpgradeDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('waitingUpgrade',1),('inProcess',2),(_L,3),(_G,4)))
_H3cIssuUpgradeDeviceStatus_Type.__name__=_B
_H3cIssuUpgradeDeviceStatus_Object=MibTableColumn
h3cIssuUpgradeDeviceStatus=_H3cIssuUpgradeDeviceStatus_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,7),_H3cIssuUpgradeDeviceStatus_Type())
h3cIssuUpgradeDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuUpgradeDeviceStatus.setStatus(_A)
class _H3cIssuUpgradeFailedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIssuUpgradeFailedReason_Type.__name__=_D
_H3cIssuUpgradeFailedReason_Object=MibTableColumn
h3cIssuUpgradeFailedReason=_H3cIssuUpgradeFailedReason_Object((1,3,6,1,4,1,2011,10,2,133,1,2,3,1,8),_H3cIssuUpgradeFailedReason_Type())
h3cIssuUpgradeFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIssuUpgradeFailedReason.setStatus(_A)
_H3cIssuUpgradeNotify_ObjectIdentity=ObjectIdentity
h3cIssuUpgradeNotify=_H3cIssuUpgradeNotify_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,2))
_H3cIssuUpgradeTrapPrefix_ObjectIdentity=ObjectIdentity
h3cIssuUpgradeTrapPrefix=_H3cIssuUpgradeTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,133,2,0))
h3cIssuUpgradeOpCompletionNotify=NotificationType((1,3,6,1,4,1,2011,10,2,133,2,0,1))
h3cIssuUpgradeOpCompletionNotify.setObjects(*((_E,_a),(_E,_b),(_E,_c),(_E,_d)))
if mibBuilder.loadTexts:h3cIssuUpgradeOpCompletionNotify.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cIssuUpgrade':h3cIssuUpgrade,'h3cIssuUpgradeMibObjects':h3cIssuUpgradeMibObjects,'h3cIssuUpgradeGroup':h3cIssuUpgradeGroup,'h3cIssuUpgradeImageTable':h3cIssuUpgradeImageTable,'h3cIssuUpgradeImageEntry':h3cIssuUpgradeImageEntry,_M:h3cIssuUpgradeImageIndex,'h3cIssuUpgradeImageType':h3cIssuUpgradeImageType,'h3cIssuUpgradeImageURL':h3cIssuUpgradeImageURL,'h3cIssuUpgradeImageRowStatus':h3cIssuUpgradeImageRowStatus,'h3cIssuOp':h3cIssuOp,_a:h3cIssuOpType,'h3cIssuImageFileOverwrite':h3cIssuImageFileOverwrite,'h3cIssuOpTrapEnable':h3cIssuOpTrapEnable,_b:h3cIssuOpStatus,_c:h3cIssuFailedReason,_d:h3cIssuOpTimeCompleted,'h3cIssuLastOpType':h3cIssuLastOpType,'h3cIssuLastOpStatus':h3cIssuLastOpStatus,'h3cIssuLastOpFailedReason':h3cIssuLastOpFailedReason,'h3cIssuLastOpTimeCompleted':h3cIssuLastOpTimeCompleted,'h3cIssuUpgradeResultGroup':h3cIssuUpgradeResultGroup,'h3cIssuCompatibleResult':h3cIssuCompatibleResult,'h3cIssuCompatibleResultStatus':h3cIssuCompatibleResultStatus,'h3cIssuCompatibleResultFailedReason':h3cIssuCompatibleResultFailedReason,'h3cIssuTestResultTable':h3cIssuTestResultTable,'h3cIssuTestResultEntry':h3cIssuTestResultEntry,_S:h3cIssuTestResultIndex,'h3cIssuTestDeviceChassisID':h3cIssuTestDeviceChassisID,'h3cIssuTestDeviceSlotID':h3cIssuTestDeviceSlotID,'h3cIssuTestDeviceCpuID':h3cIssuTestDeviceCpuID,'h3cIssuTestDeviceUpgradeWay':h3cIssuTestDeviceUpgradeWay,'h3cIssuUpgradeResultTable':h3cIssuUpgradeResultTable,'h3cIssuUpgradeResultEntry':h3cIssuUpgradeResultEntry,_Z:h3cIssuUpgradeResultIndex,'h3cIssuUpgradeDeviceChassisID':h3cIssuUpgradeDeviceChassisID,'h3cIssuUpgradeDeviceSlotID':h3cIssuUpgradeDeviceSlotID,'h3cIssuUpgradeDeviceCpuID':h3cIssuUpgradeDeviceCpuID,'h3cIssuUpgradeState':h3cIssuUpgradeState,'h3cIssuDeviceUpgradeWay':h3cIssuDeviceUpgradeWay,'h3cIssuUpgradeDeviceStatus':h3cIssuUpgradeDeviceStatus,'h3cIssuUpgradeFailedReason':h3cIssuUpgradeFailedReason,'h3cIssuUpgradeNotify':h3cIssuUpgradeNotify,'h3cIssuUpgradeTrapPrefix':h3cIssuUpgradeTrapPrefix,'h3cIssuUpgradeOpCompletionNotify':h3cIssuUpgradeOpCompletionNotify})