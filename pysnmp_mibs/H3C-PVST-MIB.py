_G='h3cPvstVlanID'
_F='read-only'
_E='h3cPvstPortIndex'
_D='h3cPvstPortVlanID'
_C='Integer32'
_B='H3C-PVST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cPvst=ModuleIdentity((1,3,6,1,4,1,2011,10,2,131))
if mibBuilder.loadTexts:h3cPvst.setRevisions(('2014-05-27 00:00',))
_H3cPvstObjects_ObjectIdentity=ObjectIdentity
h3cPvstObjects=_H3cPvstObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,131,1))
_H3cPvstVlanConfigTable_Object=MibTable
h3cPvstVlanConfigTable=_H3cPvstVlanConfigTable_Object((1,3,6,1,4,1,2011,10,2,131,1,1))
if mibBuilder.loadTexts:h3cPvstVlanConfigTable.setStatus(_A)
_H3cPvstVlanConfigEntry_Object=MibTableRow
h3cPvstVlanConfigEntry=_H3cPvstVlanConfigEntry_Object((1,3,6,1,4,1,2011,10,2,131,1,1,1))
h3cPvstVlanConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cPvstVlanConfigEntry.setStatus(_A)
class _H3cPvstVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cPvstVlanID_Type.__name__=_C
_H3cPvstVlanID_Object=MibTableColumn
h3cPvstVlanID=_H3cPvstVlanID_Object((1,3,6,1,4,1,2011,10,2,131,1,1,1,1),_H3cPvstVlanID_Type())
h3cPvstVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPvstVlanID.setStatus(_A)
_H3cPvstVlanPortConfigTable_Object=MibTable
h3cPvstVlanPortConfigTable=_H3cPvstVlanPortConfigTable_Object((1,3,6,1,4,1,2011,10,2,131,1,2))
if mibBuilder.loadTexts:h3cPvstVlanPortConfigTable.setStatus(_A)
_H3cPvstVlanPortConfigEntry_Object=MibTableRow
h3cPvstVlanPortConfigEntry=_H3cPvstVlanPortConfigEntry_Object((1,3,6,1,4,1,2011,10,2,131,1,2,1))
h3cPvstVlanPortConfigEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:h3cPvstVlanPortConfigEntry.setStatus(_A)
class _H3cPvstPortVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cPvstPortVlanID_Type.__name__=_C
_H3cPvstPortVlanID_Object=MibTableColumn
h3cPvstPortVlanID=_H3cPvstPortVlanID_Object((1,3,6,1,4,1,2011,10,2,131,1,2,1,1),_H3cPvstPortVlanID_Type())
h3cPvstPortVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPvstPortVlanID.setStatus(_A)
class _H3cPvstPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPvstPortIndex_Type.__name__=_C
_H3cPvstPortIndex_Object=MibTableColumn
h3cPvstPortIndex=_H3cPvstPortIndex_Object((1,3,6,1,4,1,2011,10,2,131,1,2,1,2),_H3cPvstPortIndex_Type())
h3cPvstPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cPvstPortIndex.setStatus(_A)
_H3cPvstNotifications_ObjectIdentity=ObjectIdentity
h3cPvstNotifications=_H3cPvstNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,131,2))
_H3cPvstEvents_ObjectIdentity=ObjectIdentity
h3cPvstEvents=_H3cPvstEvents_ObjectIdentity((1,3,6,1,4,1,2011,10,2,131,2,0))
h3cPvstVlanPortDetectedTc=NotificationType((1,3,6,1,4,1,2011,10,2,131,2,0,1))
h3cPvstVlanPortDetectedTc.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:h3cPvstVlanPortDetectedTc.setStatus(_A)
h3cPvstVlanPortRcvdTc=NotificationType((1,3,6,1,4,1,2011,10,2,131,2,0,2))
h3cPvstVlanPortRcvdTc.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:h3cPvstVlanPortRcvdTc.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cPvst':h3cPvst,'h3cPvstObjects':h3cPvstObjects,'h3cPvstVlanConfigTable':h3cPvstVlanConfigTable,'h3cPvstVlanConfigEntry':h3cPvstVlanConfigEntry,_G:h3cPvstVlanID,'h3cPvstVlanPortConfigTable':h3cPvstVlanPortConfigTable,'h3cPvstVlanPortConfigEntry':h3cPvstVlanPortConfigEntry,_D:h3cPvstPortVlanID,_E:h3cPvstPortIndex,'h3cPvstNotifications':h3cPvstNotifications,'h3cPvstEvents':h3cPvstEvents,'h3cPvstVlanPortDetectedTc':h3cPvstVlanPortDetectedTc,'h3cPvstVlanPortRcvdTc':h3cPvstVlanPortRcvdTc})