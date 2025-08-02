_J='accessible-for-notify'
_I='h3cStormCtrlPortStatus'
_H='h3cStormTrapThreshold'
_G='h3cStormTrapType'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='H3C-STORM-CONSTRAIN-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cStormConstrain=ModuleIdentity((1,3,6,1,4,1,2011,10,2,66))
if mibBuilder.loadTexts:h3cStormConstrain.setRevisions(('2015-06-17 00:00',))
class H3cStormConstrainUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('packetsPerSecond',2),('ratio',3),('bytesPerSecond',4),('kbitsPerSecond',5)))
_H3cStormScalarGroup_ObjectIdentity=ObjectIdentity
h3cStormScalarGroup=_H3cStormScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,66,1))
class _H3cStormTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('broadcast',1),('multicast',2),('unicast',3),('knownUnicast',4)))
_H3cStormTrapType_Type.__name__=_F
_H3cStormTrapType_Object=MibScalar
h3cStormTrapType=_H3cStormTrapType_Object((1,3,6,1,4,1,2011,10,2,66,1,1),_H3cStormTrapType_Type())
h3cStormTrapType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cStormTrapType.setStatus(_A)
_H3cStormTrapThreshold_Type=Integer32
_H3cStormTrapThreshold_Object=MibScalar
h3cStormTrapThreshold=_H3cStormTrapThreshold_Object((1,3,6,1,4,1,2011,10,2,66,1,2),_H3cStormTrapThreshold_Type())
h3cStormTrapThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cStormTrapThreshold.setStatus(_A)
_H3cStormTableGroup_ObjectIdentity=ObjectIdentity
h3cStormTableGroup=_H3cStormTableGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,66,2))
_H3cStormCtrlTable_Object=MibTable
h3cStormCtrlTable=_H3cStormCtrlTable_Object((1,3,6,1,4,1,2011,10,2,66,2,1))
if mibBuilder.loadTexts:h3cStormCtrlTable.setStatus(_A)
_H3cStormCtrlEntry_Object=MibTableRow
h3cStormCtrlEntry=_H3cStormCtrlEntry_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1))
h3cStormCtrlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cStormCtrlEntry.setStatus(_A)
class _H3cStormCtrlPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlled',1),('normal',2)))
_H3cStormCtrlPortStatus_Type.__name__=_F
_H3cStormCtrlPortStatus_Object=MibTableColumn
h3cStormCtrlPortStatus=_H3cStormCtrlPortStatus_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,1),_H3cStormCtrlPortStatus_Type())
h3cStormCtrlPortStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cStormCtrlPortStatus.setStatus(_A)
_H3cStormCtrlBroadcastUnit_Type=H3cStormConstrainUnit
_H3cStormCtrlBroadcastUnit_Object=MibTableColumn
h3cStormCtrlBroadcastUnit=_H3cStormCtrlBroadcastUnit_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,2),_H3cStormCtrlBroadcastUnit_Type())
h3cStormCtrlBroadcastUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlBroadcastUnit.setStatus(_A)
_H3cStormCtrlBroadcastUpper_Type=Integer32
_H3cStormCtrlBroadcastUpper_Object=MibTableColumn
h3cStormCtrlBroadcastUpper=_H3cStormCtrlBroadcastUpper_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,3),_H3cStormCtrlBroadcastUpper_Type())
h3cStormCtrlBroadcastUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlBroadcastUpper.setStatus(_A)
_H3cStormCtrlBroadcastLower_Type=Integer32
_H3cStormCtrlBroadcastLower_Object=MibTableColumn
h3cStormCtrlBroadcastLower=_H3cStormCtrlBroadcastLower_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,4),_H3cStormCtrlBroadcastLower_Type())
h3cStormCtrlBroadcastLower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlBroadcastLower.setStatus(_A)
_H3cStormCtrlMulticastUnit_Type=H3cStormConstrainUnit
_H3cStormCtrlMulticastUnit_Object=MibTableColumn
h3cStormCtrlMulticastUnit=_H3cStormCtrlMulticastUnit_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,5),_H3cStormCtrlMulticastUnit_Type())
h3cStormCtrlMulticastUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlMulticastUnit.setStatus(_A)
_H3cStormCtrlMulticastUpper_Type=Integer32
_H3cStormCtrlMulticastUpper_Object=MibTableColumn
h3cStormCtrlMulticastUpper=_H3cStormCtrlMulticastUpper_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,6),_H3cStormCtrlMulticastUpper_Type())
h3cStormCtrlMulticastUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlMulticastUpper.setStatus(_A)
_H3cStormCtrlMulticastLower_Type=Integer32
_H3cStormCtrlMulticastLower_Object=MibTableColumn
h3cStormCtrlMulticastLower=_H3cStormCtrlMulticastLower_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,7),_H3cStormCtrlMulticastLower_Type())
h3cStormCtrlMulticastLower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlMulticastLower.setStatus(_A)
_H3cStormCtrlUnicastUnit_Type=H3cStormConstrainUnit
_H3cStormCtrlUnicastUnit_Object=MibTableColumn
h3cStormCtrlUnicastUnit=_H3cStormCtrlUnicastUnit_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,8),_H3cStormCtrlUnicastUnit_Type())
h3cStormCtrlUnicastUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlUnicastUnit.setStatus(_A)
_H3cStormCtrlUnicastUpper_Type=Integer32
_H3cStormCtrlUnicastUpper_Object=MibTableColumn
h3cStormCtrlUnicastUpper=_H3cStormCtrlUnicastUpper_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,9),_H3cStormCtrlUnicastUpper_Type())
h3cStormCtrlUnicastUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlUnicastUpper.setStatus(_A)
_H3cStormCtrlUnicastLower_Type=Integer32
_H3cStormCtrlUnicastLower_Object=MibTableColumn
h3cStormCtrlUnicastLower=_H3cStormCtrlUnicastLower_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,10),_H3cStormCtrlUnicastLower_Type())
h3cStormCtrlUnicastLower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlUnicastLower.setStatus(_A)
_H3cStormCtrlRowStatus_Type=RowStatus
_H3cStormCtrlRowStatus_Object=MibTableColumn
h3cStormCtrlRowStatus=_H3cStormCtrlRowStatus_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,11),_H3cStormCtrlRowStatus_Type())
h3cStormCtrlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlRowStatus.setStatus(_A)
class _H3cStormCtrlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('block',2),('shutdown',3)))
_H3cStormCtrlPortMode_Type.__name__=_F
_H3cStormCtrlPortMode_Object=MibTableColumn
h3cStormCtrlPortMode=_H3cStormCtrlPortMode_Object((1,3,6,1,4,1,2011,10,2,66,2,1,1,12),_H3cStormCtrlPortMode_Type())
h3cStormCtrlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStormCtrlPortMode.setStatus(_A)
_H3cStormNotifications_ObjectIdentity=ObjectIdentity
h3cStormNotifications=_H3cStormNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,66,3))
h3cStormRising=NotificationType((1,3,6,1,4,1,2011,10,2,66,3,1))
h3cStormRising.setObjects(*((_D,_E),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:h3cStormRising.setStatus(_A)
h3cStormFalling=NotificationType((1,3,6,1,4,1,2011,10,2,66,3,2))
h3cStormFalling.setObjects(*((_D,_E),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:h3cStormFalling.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'H3cStormConstrainUnit':H3cStormConstrainUnit,'h3cStormConstrain':h3cStormConstrain,'h3cStormScalarGroup':h3cStormScalarGroup,_G:h3cStormTrapType,_H:h3cStormTrapThreshold,'h3cStormTableGroup':h3cStormTableGroup,'h3cStormCtrlTable':h3cStormCtrlTable,'h3cStormCtrlEntry':h3cStormCtrlEntry,_I:h3cStormCtrlPortStatus,'h3cStormCtrlBroadcastUnit':h3cStormCtrlBroadcastUnit,'h3cStormCtrlBroadcastUpper':h3cStormCtrlBroadcastUpper,'h3cStormCtrlBroadcastLower':h3cStormCtrlBroadcastLower,'h3cStormCtrlMulticastUnit':h3cStormCtrlMulticastUnit,'h3cStormCtrlMulticastUpper':h3cStormCtrlMulticastUpper,'h3cStormCtrlMulticastLower':h3cStormCtrlMulticastLower,'h3cStormCtrlUnicastUnit':h3cStormCtrlUnicastUnit,'h3cStormCtrlUnicastUpper':h3cStormCtrlUnicastUpper,'h3cStormCtrlUnicastLower':h3cStormCtrlUnicastLower,'h3cStormCtrlRowStatus':h3cStormCtrlRowStatus,'h3cStormCtrlPortMode':h3cStormCtrlPortMode,'h3cStormNotifications':h3cStormNotifications,'h3cStormRising':h3cStormRising,'h3cStormFalling':h3cStormFalling})