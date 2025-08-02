_J='accessible-for-notify'
_I='hpnicfStormCtrlPortStatus'
_H='hpnicfStormTrapThreshold'
_G='hpnicfStormTrapType'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='HPN-ICF-STORM-CONSTRAIN-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfStormConstrain=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,66))
class HpnicfStormConstrainUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('packetsPerSecond',2),('ratio',3),('bytesPerSecond',4),('kbitsPerSecond',5)))
_HpnicfStormScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfStormScalarGroup=_HpnicfStormScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,66,1))
class _HpnicfStormTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('broadcast',1),('multicast',2),('unicast',3)))
_HpnicfStormTrapType_Type.__name__=_F
_HpnicfStormTrapType_Object=MibScalar
hpnicfStormTrapType=_HpnicfStormTrapType_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,1,1),_HpnicfStormTrapType_Type())
hpnicfStormTrapType.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfStormTrapType.setStatus(_A)
_HpnicfStormTrapThreshold_Type=Integer32
_HpnicfStormTrapThreshold_Object=MibScalar
hpnicfStormTrapThreshold=_HpnicfStormTrapThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,1,2),_HpnicfStormTrapThreshold_Type())
hpnicfStormTrapThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfStormTrapThreshold.setStatus(_A)
_HpnicfStormTableGroup_ObjectIdentity=ObjectIdentity
hpnicfStormTableGroup=_HpnicfStormTableGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,66,2))
_HpnicfStormCtrlTable_Object=MibTable
hpnicfStormCtrlTable=_HpnicfStormCtrlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1))
if mibBuilder.loadTexts:hpnicfStormCtrlTable.setStatus(_A)
_HpnicfStormCtrlEntry_Object=MibTableRow
hpnicfStormCtrlEntry=_HpnicfStormCtrlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1))
hpnicfStormCtrlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfStormCtrlEntry.setStatus(_A)
class _HpnicfStormCtrlPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlled',1),('normal',2)))
_HpnicfStormCtrlPortStatus_Type.__name__=_F
_HpnicfStormCtrlPortStatus_Object=MibTableColumn
hpnicfStormCtrlPortStatus=_HpnicfStormCtrlPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,1),_HpnicfStormCtrlPortStatus_Type())
hpnicfStormCtrlPortStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfStormCtrlPortStatus.setStatus(_A)
_HpnicfStormCtrlBroadcastUnit_Type=HpnicfStormConstrainUnit
_HpnicfStormCtrlBroadcastUnit_Object=MibTableColumn
hpnicfStormCtrlBroadcastUnit=_HpnicfStormCtrlBroadcastUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,2),_HpnicfStormCtrlBroadcastUnit_Type())
hpnicfStormCtrlBroadcastUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlBroadcastUnit.setStatus(_A)
_HpnicfStormCtrlBroadcastUpper_Type=Integer32
_HpnicfStormCtrlBroadcastUpper_Object=MibTableColumn
hpnicfStormCtrlBroadcastUpper=_HpnicfStormCtrlBroadcastUpper_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,3),_HpnicfStormCtrlBroadcastUpper_Type())
hpnicfStormCtrlBroadcastUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlBroadcastUpper.setStatus(_A)
_HpnicfStormCtrlBroadcastLower_Type=Integer32
_HpnicfStormCtrlBroadcastLower_Object=MibTableColumn
hpnicfStormCtrlBroadcastLower=_HpnicfStormCtrlBroadcastLower_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,4),_HpnicfStormCtrlBroadcastLower_Type())
hpnicfStormCtrlBroadcastLower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlBroadcastLower.setStatus(_A)
_HpnicfStormCtrlMulticastUnit_Type=HpnicfStormConstrainUnit
_HpnicfStormCtrlMulticastUnit_Object=MibTableColumn
hpnicfStormCtrlMulticastUnit=_HpnicfStormCtrlMulticastUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,5),_HpnicfStormCtrlMulticastUnit_Type())
hpnicfStormCtrlMulticastUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlMulticastUnit.setStatus(_A)
_HpnicfStormCtrlMulticastUpper_Type=Integer32
_HpnicfStormCtrlMulticastUpper_Object=MibTableColumn
hpnicfStormCtrlMulticastUpper=_HpnicfStormCtrlMulticastUpper_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,6),_HpnicfStormCtrlMulticastUpper_Type())
hpnicfStormCtrlMulticastUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlMulticastUpper.setStatus(_A)
_HpnicfStormCtrlMulticastLower_Type=Integer32
_HpnicfStormCtrlMulticastLower_Object=MibTableColumn
hpnicfStormCtrlMulticastLower=_HpnicfStormCtrlMulticastLower_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,7),_HpnicfStormCtrlMulticastLower_Type())
hpnicfStormCtrlMulticastLower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlMulticastLower.setStatus(_A)
_HpnicfStormCtrlUnicastUnit_Type=HpnicfStormConstrainUnit
_HpnicfStormCtrlUnicastUnit_Object=MibTableColumn
hpnicfStormCtrlUnicastUnit=_HpnicfStormCtrlUnicastUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,8),_HpnicfStormCtrlUnicastUnit_Type())
hpnicfStormCtrlUnicastUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlUnicastUnit.setStatus(_A)
_HpnicfStormCtrlUnicastUpper_Type=Integer32
_HpnicfStormCtrlUnicastUpper_Object=MibTableColumn
hpnicfStormCtrlUnicastUpper=_HpnicfStormCtrlUnicastUpper_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,9),_HpnicfStormCtrlUnicastUpper_Type())
hpnicfStormCtrlUnicastUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlUnicastUpper.setStatus(_A)
_HpnicfStormCtrlUnicastLower_Type=Integer32
_HpnicfStormCtrlUnicastLower_Object=MibTableColumn
hpnicfStormCtrlUnicastLower=_HpnicfStormCtrlUnicastLower_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,10),_HpnicfStormCtrlUnicastLower_Type())
hpnicfStormCtrlUnicastLower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlUnicastLower.setStatus(_A)
_HpnicfStormCtrlRowStatus_Type=RowStatus
_HpnicfStormCtrlRowStatus_Object=MibTableColumn
hpnicfStormCtrlRowStatus=_HpnicfStormCtrlRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,11),_HpnicfStormCtrlRowStatus_Type())
hpnicfStormCtrlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlRowStatus.setStatus(_A)
class _HpnicfStormCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('block',2),('shutdown',3)))
_HpnicfStormCtrlPortMode_Type.__name__=_F
_HpnicfStormCtrlPortMode_Object=MibTableColumn
hpnicfStormCtrlPortMode=_HpnicfStormCtrlPortMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,66,2,1,1,12),_HpnicfStormCtrlPortMode_Type())
hpnicfStormCtrlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStormCtrlPortMode.setStatus(_A)
_HpnicfStormNotifications_ObjectIdentity=ObjectIdentity
hpnicfStormNotifications=_HpnicfStormNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,66,3))
hpnicfStormRising=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,66,3,1))
hpnicfStormRising.setObjects(*((_D,_E),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:hpnicfStormRising.setStatus(_A)
hpnicfStormFalling=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,66,3,2))
hpnicfStormFalling.setObjects(*((_D,_E),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:hpnicfStormFalling.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfStormConstrainUnit':HpnicfStormConstrainUnit,'hpnicfStormConstrain':hpnicfStormConstrain,'hpnicfStormScalarGroup':hpnicfStormScalarGroup,_G:hpnicfStormTrapType,_H:hpnicfStormTrapThreshold,'hpnicfStormTableGroup':hpnicfStormTableGroup,'hpnicfStormCtrlTable':hpnicfStormCtrlTable,'hpnicfStormCtrlEntry':hpnicfStormCtrlEntry,_I:hpnicfStormCtrlPortStatus,'hpnicfStormCtrlBroadcastUnit':hpnicfStormCtrlBroadcastUnit,'hpnicfStormCtrlBroadcastUpper':hpnicfStormCtrlBroadcastUpper,'hpnicfStormCtrlBroadcastLower':hpnicfStormCtrlBroadcastLower,'hpnicfStormCtrlMulticastUnit':hpnicfStormCtrlMulticastUnit,'hpnicfStormCtrlMulticastUpper':hpnicfStormCtrlMulticastUpper,'hpnicfStormCtrlMulticastLower':hpnicfStormCtrlMulticastLower,'hpnicfStormCtrlUnicastUnit':hpnicfStormCtrlUnicastUnit,'hpnicfStormCtrlUnicastUpper':hpnicfStormCtrlUnicastUpper,'hpnicfStormCtrlUnicastLower':hpnicfStormCtrlUnicastLower,'hpnicfStormCtrlRowStatus':hpnicfStormCtrlRowStatus,'hpnicfStormCtrlPortMode':hpnicfStormCtrlPortMode,'hpnicfStormNotifications':hpnicfStormNotifications,'hpnicfStormRising':hpnicfStormRising,'hpnicfStormFalling':hpnicfStormFalling})