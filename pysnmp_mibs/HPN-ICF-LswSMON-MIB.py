_E='hpnicfdot1qVlanStatEnableIndex'
_D='HPN-ICF-LswSMON-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_HpnicfSmonExtend_ObjectIdentity=ObjectIdentity
hpnicfSmonExtend=_HpnicfSmonExtend_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,26))
_HpnicfsmonExtendObject_ObjectIdentity=ObjectIdentity
hpnicfsmonExtendObject=_HpnicfsmonExtendObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,26,1))
_Hpnicfdot1qVlanStatNumber_Type=Integer32
_Hpnicfdot1qVlanStatNumber_Object=MibScalar
hpnicfdot1qVlanStatNumber=_Hpnicfdot1qVlanStatNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,26,1,1),_Hpnicfdot1qVlanStatNumber_Type())
hpnicfdot1qVlanStatNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanStatNumber.setStatus(_A)
_Hpnicfdot1qVlanStatStatusTable_Object=MibTable
hpnicfdot1qVlanStatStatusTable=_Hpnicfdot1qVlanStatStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,26,1,2))
if mibBuilder.loadTexts:hpnicfdot1qVlanStatStatusTable.setStatus(_A)
_Hpnicfdot1qVlanStatStatusEntry_Object=MibTableRow
hpnicfdot1qVlanStatStatusEntry=_Hpnicfdot1qVlanStatStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,26,1,2,1))
hpnicfdot1qVlanStatStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfdot1qVlanStatStatusEntry.setStatus(_A)
_Hpnicfdot1qVlanStatEnableIndex_Type=Integer32
_Hpnicfdot1qVlanStatEnableIndex_Object=MibTableColumn
hpnicfdot1qVlanStatEnableIndex=_Hpnicfdot1qVlanStatEnableIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,26,1,2,1,1),_Hpnicfdot1qVlanStatEnableIndex_Type())
hpnicfdot1qVlanStatEnableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfdot1qVlanStatEnableIndex.setStatus(_A)
class _Hpnicfdot1qVlanStatEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Hpnicfdot1qVlanStatEnableStatus_Type.__name__=_B
_Hpnicfdot1qVlanStatEnableStatus_Object=MibTableColumn
hpnicfdot1qVlanStatEnableStatus=_Hpnicfdot1qVlanStatEnableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,26,1,2,1,2),_Hpnicfdot1qVlanStatEnableStatus_Type())
hpnicfdot1qVlanStatEnableStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfdot1qVlanStatEnableStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfSmonExtend':hpnicfSmonExtend,'hpnicfsmonExtendObject':hpnicfsmonExtendObject,'hpnicfdot1qVlanStatNumber':hpnicfdot1qVlanStatNumber,'hpnicfdot1qVlanStatStatusTable':hpnicfdot1qVlanStatStatusTable,'hpnicfdot1qVlanStatStatusEntry':hpnicfdot1qVlanStatStatusEntry,_E:hpnicfdot1qVlanStatEnableIndex,'hpnicfdot1qVlanStatEnableStatus':hpnicfdot1qVlanStatEnableStatus})