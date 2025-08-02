_M='accessible-for-notify'
_L='DisplayString'
_K='entPhysicalIndex'
_J='hpnicfPexEntPhysicalIndexBind'
_I='hpnicfPexPortDescr'
_H='read-create'
_G='entPhysicalDescr'
_F='hpnicfPexPortId'
_E='ENTITY-MIB'
_D='Integer32'
_C='HPN-ICF-PEX-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalDescr,entPhysicalIndex=mibBuilder.importSymbols(_E,_G,_K)
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention')
hpnicfPex=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,129))
if mibBuilder.loadTexts:hpnicfPex.setRevisions(('2012-11-12 11:29',))
_HpnicfPexSpecInfo_ObjectIdentity=ObjectIdentity
hpnicfPexSpecInfo=_HpnicfPexSpecInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,129,1))
_HpnicfPexPortMinId_Type=Integer32
_HpnicfPexPortMinId_Object=MibScalar
hpnicfPexPortMinId=_HpnicfPexPortMinId_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,1,1),_HpnicfPexPortMinId_Type())
hpnicfPexPortMinId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexPortMinId.setStatus(_A)
_HpnicfPexPortMaxId_Type=Integer32
_HpnicfPexPortMaxId_Object=MibScalar
hpnicfPexPortMaxId=_HpnicfPexPortMaxId_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,1,2),_HpnicfPexPortMaxId_Type())
hpnicfPexPortMaxId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexPortMaxId.setStatus(_A)
_HpnicfPexMinAssociateId_Type=Integer32
_HpnicfPexMinAssociateId_Object=MibScalar
hpnicfPexMinAssociateId=_HpnicfPexMinAssociateId_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,1,3),_HpnicfPexMinAssociateId_Type())
hpnicfPexMinAssociateId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexMinAssociateId.setStatus(_A)
_HpnicfPexMaxAssociateId_Type=Integer32
_HpnicfPexMaxAssociateId_Object=MibScalar
hpnicfPexMaxAssociateId=_HpnicfPexMaxAssociateId_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,1,4),_HpnicfPexMaxAssociateId_Type())
hpnicfPexMaxAssociateId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexMaxAssociateId.setStatus(_A)
_HpnicfPexMaxPortPerPexPort_Type=Integer32
_HpnicfPexMaxPortPerPexPort_Object=MibScalar
hpnicfPexMaxPortPerPexPort=_HpnicfPexMaxPortPerPexPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,1,5),_HpnicfPexMaxPortPerPexPort_Type())
hpnicfPexMaxPortPerPexPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexMaxPortPerPexPort.setStatus(_A)
_HpnicfPexTable_ObjectIdentity=ObjectIdentity
hpnicfPexTable=_HpnicfPexTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,129,2))
_HpnicfPexPortTable_Object=MibTable
hpnicfPexPortTable=_HpnicfPexPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1))
if mibBuilder.loadTexts:hpnicfPexPortTable.setStatus(_A)
_HpnicfPexPortEntry_Object=MibTableRow
hpnicfPexPortEntry=_HpnicfPexPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1))
hpnicfPexPortEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hpnicfPexPortEntry.setStatus(_A)
class _HpnicfPexPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPexPortId_Type.__name__=_D
_HpnicfPexPortId_Object=MibTableColumn
hpnicfPexPortId=_HpnicfPexPortId_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1,1),_HpnicfPexPortId_Type())
hpnicfPexPortId.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfPexPortId.setStatus(_A)
class _HpnicfPexPortAssociateId_Type(Integer32):defaultValue=65535
_HpnicfPexPortAssociateId_Type.__name__=_D
_HpnicfPexPortAssociateId_Object=MibTableColumn
hpnicfPexPortAssociateId=_HpnicfPexPortAssociateId_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1,2),_HpnicfPexPortAssociateId_Type())
hpnicfPexPortAssociateId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPexPortAssociateId.setStatus(_A)
class _HpnicfPexPortEntPhysicalIndex_Type(Integer32):defaultValue=0
_HpnicfPexPortEntPhysicalIndex_Type.__name__=_D
_HpnicfPexPortEntPhysicalIndex_Object=MibTableColumn
hpnicfPexPortEntPhysicalIndex=_HpnicfPexPortEntPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1,3),_HpnicfPexPortEntPhysicalIndex_Type())
hpnicfPexPortEntPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexPortEntPhysicalIndex.setStatus(_A)
class _HpnicfPexPortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_HpnicfPexPortDescr_Type.__name__=_L
_HpnicfPexPortDescr_Object=MibTableColumn
hpnicfPexPortDescr=_HpnicfPexPortDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1,4),_HpnicfPexPortDescr_Type())
hpnicfPexPortDescr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPexPortDescr.setStatus(_A)
class _HpnicfPexPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('offline',1),('loading',2),('online',3)))
_HpnicfPexPortStatus_Type.__name__=_D
_HpnicfPexPortStatus_Object=MibTableColumn
hpnicfPexPortStatus=_HpnicfPexPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1,5),_HpnicfPexPortStatus_Type())
hpnicfPexPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexPortStatus.setStatus(_A)
_HpnicfPexPortRowStatus_Type=RowStatus
_HpnicfPexPortRowStatus_Object=MibTableColumn
hpnicfPexPortRowStatus=_HpnicfPexPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,1,1,6),_HpnicfPexPortRowStatus_Type())
hpnicfPexPortRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPexPortRowStatus.setStatus(_A)
_HpnicfPexPhyPortTable_Object=MibTable
hpnicfPexPhyPortTable=_HpnicfPexPhyPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,2))
if mibBuilder.loadTexts:hpnicfPexPhyPortTable.setStatus(_A)
_HpnicfPexPhyPortEntry_Object=MibTableRow
hpnicfPexPhyPortEntry=_HpnicfPexPhyPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,2,1))
hpnicfPexPhyPortEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hpnicfPexPhyPortEntry.setStatus(_A)
class _HpnicfPexPhyPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('down',2),('blocked',3),('forwarding',4)))
_HpnicfPexPhyPortStatus_Type.__name__=_D
_HpnicfPexPhyPortStatus_Object=MibTableColumn
hpnicfPexPhyPortStatus=_HpnicfPexPhyPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,2,1,1),_HpnicfPexPhyPortStatus_Type())
hpnicfPexPhyPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexPhyPortStatus.setStatus(_A)
class _HpnicfPexPhyPortBelongToPexPort_Type(Integer32):defaultValue=0
_HpnicfPexPhyPortBelongToPexPort_Type.__name__=_D
_HpnicfPexPhyPortBelongToPexPort_Object=MibTableColumn
hpnicfPexPhyPortBelongToPexPort=_HpnicfPexPhyPortBelongToPexPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,2,1,2),_HpnicfPexPhyPortBelongToPexPort_Type())
hpnicfPexPhyPortBelongToPexPort.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfPexPhyPortBelongToPexPort.setStatus(_A)
_HpnicfPexPhyPortNeighborEntIndex_Type=Integer32
_HpnicfPexPhyPortNeighborEntIndex_Object=MibTableColumn
hpnicfPexPhyPortNeighborEntIndex=_HpnicfPexPhyPortNeighborEntIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,2,2,1,3),_HpnicfPexPhyPortNeighborEntIndex_Type())
hpnicfPexPhyPortNeighborEntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPexPhyPortNeighborEntIndex.setStatus(_A)
_HpnicfPexTraps_ObjectIdentity=ObjectIdentity
hpnicfPexTraps=_HpnicfPexTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,129,3))
_HpnicfPexTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfPexTrapPrefix=_HpnicfPexTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,129,3,0))
_HpnicfPexTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfPexTrapObjects=_HpnicfPexTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,129,4))
_HpnicfPexEntPhysicalIndexBind_Type=Integer32
_HpnicfPexEntPhysicalIndexBind_Object=MibScalar
hpnicfPexEntPhysicalIndexBind=_HpnicfPexEntPhysicalIndexBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,129,4,1),_HpnicfPexEntPhysicalIndexBind_Type())
hpnicfPexEntPhysicalIndexBind.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfPexEntPhysicalIndexBind.setStatus(_A)
hpnicfPexPortOnline=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,129,3,0,1))
hpnicfPexPortOnline.setObjects(*((_C,_F),(_C,_I)))
if mibBuilder.loadTexts:hpnicfPexPortOnline.setStatus(_A)
hpnicfPexPortOffline=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,129,3,0,2))
hpnicfPexPortOffline.setObjects(*((_C,_F),(_C,_I)))
if mibBuilder.loadTexts:hpnicfPexPortOffline.setStatus(_A)
hpnicfPexPhyPortForwarding=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,129,3,0,3))
hpnicfPexPhyPortForwarding.setObjects(*((_C,_J),(_E,_G)))
if mibBuilder.loadTexts:hpnicfPexPhyPortForwarding.setStatus(_A)
hpnicfPexPhyPortBlocked=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,129,3,0,4))
hpnicfPexPhyPortBlocked.setObjects(*((_C,_J),(_E,_G)))
if mibBuilder.loadTexts:hpnicfPexPhyPortBlocked.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfPex':hpnicfPex,'hpnicfPexSpecInfo':hpnicfPexSpecInfo,'hpnicfPexPortMinId':hpnicfPexPortMinId,'hpnicfPexPortMaxId':hpnicfPexPortMaxId,'hpnicfPexMinAssociateId':hpnicfPexMinAssociateId,'hpnicfPexMaxAssociateId':hpnicfPexMaxAssociateId,'hpnicfPexMaxPortPerPexPort':hpnicfPexMaxPortPerPexPort,'hpnicfPexTable':hpnicfPexTable,'hpnicfPexPortTable':hpnicfPexPortTable,'hpnicfPexPortEntry':hpnicfPexPortEntry,_F:hpnicfPexPortId,'hpnicfPexPortAssociateId':hpnicfPexPortAssociateId,'hpnicfPexPortEntPhysicalIndex':hpnicfPexPortEntPhysicalIndex,_I:hpnicfPexPortDescr,'hpnicfPexPortStatus':hpnicfPexPortStatus,'hpnicfPexPortRowStatus':hpnicfPexPortRowStatus,'hpnicfPexPhyPortTable':hpnicfPexPhyPortTable,'hpnicfPexPhyPortEntry':hpnicfPexPhyPortEntry,'hpnicfPexPhyPortStatus':hpnicfPexPhyPortStatus,'hpnicfPexPhyPortBelongToPexPort':hpnicfPexPhyPortBelongToPexPort,'hpnicfPexPhyPortNeighborEntIndex':hpnicfPexPhyPortNeighborEntIndex,'hpnicfPexTraps':hpnicfPexTraps,'hpnicfPexTrapPrefix':hpnicfPexTrapPrefix,'hpnicfPexPortOnline':hpnicfPexPortOnline,'hpnicfPexPortOffline':hpnicfPexPortOffline,'hpnicfPexPhyPortForwarding':hpnicfPexPhyPortForwarding,'hpnicfPexPhyPortBlocked':hpnicfPexPhyPortBlocked,'hpnicfPexTrapObjects':hpnicfPexTrapObjects,_J:hpnicfPexEntPhysicalIndexBind})