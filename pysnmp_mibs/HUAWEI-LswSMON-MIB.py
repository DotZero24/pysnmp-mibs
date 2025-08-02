_E='hwdot1qVlanStatEnableIndex'
_D='HUAWEI-LswSMON-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiDatacomm,huaweiMgmt=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','huaweiDatacomm','huaweiMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_HwSmonExtend_ObjectIdentity=ObjectIdentity
hwSmonExtend=_HwSmonExtend_ObjectIdentity((1,3,6,1,4,1,2011,5,25,26))
_SmonExtendObject_ObjectIdentity=ObjectIdentity
smonExtendObject=_SmonExtendObject_ObjectIdentity((1,3,6,1,4,1,2011,5,25,26,1))
_Hwdot1qVlanStatNumber_Type=Integer32
_Hwdot1qVlanStatNumber_Object=MibScalar
hwdot1qVlanStatNumber=_Hwdot1qVlanStatNumber_Object((1,3,6,1,4,1,2011,5,25,26,1,1),_Hwdot1qVlanStatNumber_Type())
hwdot1qVlanStatNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanStatNumber.setStatus(_A)
_Hwdot1qVlanStatStatusTable_Object=MibTable
hwdot1qVlanStatStatusTable=_Hwdot1qVlanStatStatusTable_Object((1,3,6,1,4,1,2011,5,25,26,1,2))
if mibBuilder.loadTexts:hwdot1qVlanStatStatusTable.setStatus(_A)
_Hwdot1qVlanStatStatusEntry_Object=MibTableRow
hwdot1qVlanStatStatusEntry=_Hwdot1qVlanStatStatusEntry_Object((1,3,6,1,4,1,2011,5,25,26,1,2,1))
hwdot1qVlanStatStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hwdot1qVlanStatStatusEntry.setStatus(_A)
_Hwdot1qVlanStatEnableIndex_Type=Integer32
_Hwdot1qVlanStatEnableIndex_Object=MibTableColumn
hwdot1qVlanStatEnableIndex=_Hwdot1qVlanStatEnableIndex_Object((1,3,6,1,4,1,2011,5,25,26,1,2,1,1),_Hwdot1qVlanStatEnableIndex_Type())
hwdot1qVlanStatEnableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwdot1qVlanStatEnableIndex.setStatus(_A)
class _Hwdot1qVlanStatEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Hwdot1qVlanStatEnableStatus_Type.__name__=_B
_Hwdot1qVlanStatEnableStatus_Object=MibTableColumn
hwdot1qVlanStatEnableStatus=_Hwdot1qVlanStatEnableStatus_Object((1,3,6,1,4,1,2011,5,25,26,1,2,1,2),_Hwdot1qVlanStatEnableStatus_Type())
hwdot1qVlanStatEnableStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hwdot1qVlanStatEnableStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hwSmonExtend':hwSmonExtend,'smonExtendObject':smonExtendObject,'hwdot1qVlanStatNumber':hwdot1qVlanStatNumber,'hwdot1qVlanStatStatusTable':hwdot1qVlanStatStatusTable,'hwdot1qVlanStatStatusEntry':hwdot1qVlanStatStatusEntry,_E:hwdot1qVlanStatEnableIndex,'hwdot1qVlanStatEnableStatus':hwdot1qVlanStatEnableStatus})