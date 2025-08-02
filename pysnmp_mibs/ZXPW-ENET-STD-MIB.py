_J='VlanIdOrAnyOrNone'
_I='zxPwEnetPwInstance'
_H='ZXPW-ENET-STD-MIB'
_G='zxPwIndex'
_F='ZXPW-STD-MIB'
_E='StorageType'
_D='Integer32'
_C='InterfaceIndexOrZero'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention')
zxAnCesMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnCesMib')
zxPwIndex,=mibBuilder.importSymbols(_F,_G)
zxPwEnetStdMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,23))
class VlanIdOrAnyOrNone(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_ZxPwEnetObjects_ObjectIdentity=ObjectIdentity
zxPwEnetObjects=_ZxPwEnetObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,23,1))
_ZxPwEnetTable_Object=MibTable
zxPwEnetTable=_ZxPwEnetTable_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1))
if mibBuilder.loadTexts:zxPwEnetTable.setStatus(_A)
_ZxPwEnetEntry_Object=MibTableRow
zxPwEnetEntry=_ZxPwEnetEntry_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1))
zxPwEnetEntry.setIndexNames((0,_F,_G),(0,_H,_I))
if mibBuilder.loadTexts:zxPwEnetEntry.setStatus(_A)
_ZxPwEnetPwInstance_Type=Unsigned32
_ZxPwEnetPwInstance_Object=MibTableColumn
zxPwEnetPwInstance=_ZxPwEnetPwInstance_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,1),_ZxPwEnetPwInstance_Type())
zxPwEnetPwInstance.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxPwEnetPwInstance.setStatus(_A)
_ZxPwEnetPwVlan_Type=VlanIdOrAnyOrNone
_ZxPwEnetPwVlan_Object=MibTableColumn
zxPwEnetPwVlan=_ZxPwEnetPwVlan_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,2),_ZxPwEnetPwVlan_Type())
zxPwEnetPwVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetPwVlan.setStatus(_A)
class _ZxPwEnetVlanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('other',0),('portBased',1),('noChange',2),('changeVlan',3),('addVlan',4),('removeVlan',5)))
_ZxPwEnetVlanMode_Type.__name__=_D
_ZxPwEnetVlanMode_Object=MibTableColumn
zxPwEnetVlanMode=_ZxPwEnetVlanMode_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,3),_ZxPwEnetVlanMode_Type())
zxPwEnetVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetVlanMode.setStatus(_A)
class _ZxPwEnetPortVlan_Type(VlanIdOrAnyOrNone):defaultValue=4095
_ZxPwEnetPortVlan_Type.__name__=_J
_ZxPwEnetPortVlan_Object=MibTableColumn
zxPwEnetPortVlan=_ZxPwEnetPortVlan_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,4),_ZxPwEnetPortVlan_Type())
zxPwEnetPortVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetPortVlan.setStatus(_A)
_ZxPwEnetPortIfIndex_Type=InterfaceIndexOrZero
_ZxPwEnetPortIfIndex_Object=MibTableColumn
zxPwEnetPortIfIndex=_ZxPwEnetPortIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,5),_ZxPwEnetPortIfIndex_Type())
zxPwEnetPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetPortIfIndex.setStatus(_A)
class _ZxPwEnetPwIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_ZxPwEnetPwIfIndex_Type.__name__=_C
_ZxPwEnetPwIfIndex_Object=MibTableColumn
zxPwEnetPwIfIndex=_ZxPwEnetPwIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,6),_ZxPwEnetPwIfIndex_Type())
zxPwEnetPwIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetPwIfIndex.setStatus(_A)
_ZxPwEnetRowStatus_Type=RowStatus
_ZxPwEnetRowStatus_Object=MibTableColumn
zxPwEnetRowStatus=_ZxPwEnetRowStatus_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,7),_ZxPwEnetRowStatus_Type())
zxPwEnetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetRowStatus.setStatus(_A)
class _ZxPwEnetStorageType_Type(StorageType):defaultValue=3
_ZxPwEnetStorageType_Type.__name__=_E
_ZxPwEnetStorageType_Object=MibTableColumn
zxPwEnetStorageType=_ZxPwEnetStorageType_Object((1,3,6,1,4,1,3902,1015,1013,23,1,1,1,8),_ZxPwEnetStorageType_Type())
zxPwEnetStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwEnetStorageType.setStatus(_A)
_ZxPwEnetConformance_ObjectIdentity=ObjectIdentity
zxPwEnetConformance=_ZxPwEnetConformance_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,23,2))
mibBuilder.exportSymbols(_H,**{_J:VlanIdOrAnyOrNone,'zxPwEnetStdMIB':zxPwEnetStdMIB,'zxPwEnetObjects':zxPwEnetObjects,'zxPwEnetTable':zxPwEnetTable,'zxPwEnetEntry':zxPwEnetEntry,_I:zxPwEnetPwInstance,'zxPwEnetPwVlan':zxPwEnetPwVlan,'zxPwEnetVlanMode':zxPwEnetVlanMode,'zxPwEnetPortVlan':zxPwEnetPortVlan,'zxPwEnetPortIfIndex':zxPwEnetPortIfIndex,'zxPwEnetPwIfIndex':zxPwEnetPwIfIndex,'zxPwEnetRowStatus':zxPwEnetRowStatus,'zxPwEnetStorageType':zxPwEnetStorageType,'zxPwEnetConformance':zxPwEnetConformance})