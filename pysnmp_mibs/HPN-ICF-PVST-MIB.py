_G='hpnicfPvstVlanID'
_F='read-only'
_E='hpnicfPvstPortIndex'
_D='hpnicfPvstPortVlanID'
_C='Integer32'
_B='HPN-ICF-PVST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfPvst=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,131))
if mibBuilder.loadTexts:hpnicfPvst.setRevisions(('2014-05-27 00:00',))
_HpnicfPvstObjects_ObjectIdentity=ObjectIdentity
hpnicfPvstObjects=_HpnicfPvstObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,131,1))
_HpnicfPvstVlanConfigTable_Object=MibTable
hpnicfPvstVlanConfigTable=_HpnicfPvstVlanConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,1))
if mibBuilder.loadTexts:hpnicfPvstVlanConfigTable.setStatus(_A)
_HpnicfPvstVlanConfigEntry_Object=MibTableRow
hpnicfPvstVlanConfigEntry=_HpnicfPvstVlanConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,1,1))
hpnicfPvstVlanConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfPvstVlanConfigEntry.setStatus(_A)
class _HpnicfPvstVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfPvstVlanID_Type.__name__=_C
_HpnicfPvstVlanID_Object=MibTableColumn
hpnicfPvstVlanID=_HpnicfPvstVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,1,1,1),_HpnicfPvstVlanID_Type())
hpnicfPvstVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPvstVlanID.setStatus(_A)
_HpnicfPvstVlanPortConfigTable_Object=MibTable
hpnicfPvstVlanPortConfigTable=_HpnicfPvstVlanPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,2))
if mibBuilder.loadTexts:hpnicfPvstVlanPortConfigTable.setStatus(_A)
_HpnicfPvstVlanPortConfigEntry_Object=MibTableRow
hpnicfPvstVlanPortConfigEntry=_HpnicfPvstVlanPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,2,1))
hpnicfPvstVlanPortConfigEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:hpnicfPvstVlanPortConfigEntry.setStatus(_A)
class _HpnicfPvstPortVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfPvstPortVlanID_Type.__name__=_C
_HpnicfPvstPortVlanID_Object=MibTableColumn
hpnicfPvstPortVlanID=_HpnicfPvstPortVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,2,1,1),_HpnicfPvstPortVlanID_Type())
hpnicfPvstPortVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPvstPortVlanID.setStatus(_A)
class _HpnicfPvstPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPvstPortIndex_Type.__name__=_C
_HpnicfPvstPortIndex_Object=MibTableColumn
hpnicfPvstPortIndex=_HpnicfPvstPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,131,1,2,1,2),_HpnicfPvstPortIndex_Type())
hpnicfPvstPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPvstPortIndex.setStatus(_A)
_HpnicfPvstNotifications_ObjectIdentity=ObjectIdentity
hpnicfPvstNotifications=_HpnicfPvstNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,131,2))
_HpnicfPvstEvents_ObjectIdentity=ObjectIdentity
hpnicfPvstEvents=_HpnicfPvstEvents_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,131,2,0))
hpnicfPvstVlanPortDetectedTc=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,131,2,0,1))
hpnicfPvstVlanPortDetectedTc.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hpnicfPvstVlanPortDetectedTc.setStatus(_A)
hpnicfPvstVlanPortRcvdTc=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,131,2,0,2))
hpnicfPvstVlanPortRcvdTc.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hpnicfPvstVlanPortRcvdTc.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfPvst':hpnicfPvst,'hpnicfPvstObjects':hpnicfPvstObjects,'hpnicfPvstVlanConfigTable':hpnicfPvstVlanConfigTable,'hpnicfPvstVlanConfigEntry':hpnicfPvstVlanConfigEntry,_G:hpnicfPvstVlanID,'hpnicfPvstVlanPortConfigTable':hpnicfPvstVlanPortConfigTable,'hpnicfPvstVlanPortConfigEntry':hpnicfPvstVlanPortConfigEntry,_D:hpnicfPvstPortVlanID,_E:hpnicfPvstPortIndex,'hpnicfPvstNotifications':hpnicfPvstNotifications,'hpnicfPvstEvents':hpnicfPvstEvents,'hpnicfPvstVlanPortDetectedTc':hpnicfPvstVlanPortDetectedTc,'hpnicfPvstVlanPortRcvdTc':hpnicfPvstVlanPortRcvdTc})