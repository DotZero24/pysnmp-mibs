_K='read-write'
_J='hpnicfSmlkIfIndex'
_I='accessible-for-notify'
_H='hpnicfSmlkPortIfIndex'
_G='read-only'
_F='hpnicfSmlkGroupID'
_E='OctetString'
_D='HPN-ICF-SMLK-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfSmlk=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,147))
if mibBuilder.loadTexts:hpnicfSmlk.setRevisions(('2014-07-23 15:03',))
_HpnicfSmlkObject_ObjectIdentity=ObjectIdentity
hpnicfSmlkObject=_HpnicfSmlkObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,147,1))
_HpnicfSmlkGroupTable_Object=MibTable
hpnicfSmlkGroupTable=_HpnicfSmlkGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1))
if mibBuilder.loadTexts:hpnicfSmlkGroupTable.setStatus(_A)
_HpnicfSmlkGroupEntry_Object=MibTableRow
hpnicfSmlkGroupEntry=_HpnicfSmlkGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1))
hpnicfSmlkGroupEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfSmlkGroupEntry.setStatus(_A)
class _HpnicfSmlkGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpnicfSmlkGroupID_Type.__name__=_C
_HpnicfSmlkGroupID_Object=MibTableColumn
hpnicfSmlkGroupID=_HpnicfSmlkGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,1),_HpnicfSmlkGroupID_Type())
hpnicfSmlkGroupID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfSmlkGroupID.setStatus(_A)
_HpnicfSmlkDeviceID_Type=MacAddress
_HpnicfSmlkDeviceID_Object=MibTableColumn
hpnicfSmlkDeviceID=_HpnicfSmlkDeviceID_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,2),_HpnicfSmlkDeviceID_Type())
hpnicfSmlkDeviceID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSmlkDeviceID.setStatus(_A)
class _HpnicfSmlkPreemptionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('role',2),('speed',3)))
_HpnicfSmlkPreemptionMode_Type.__name__=_C
_HpnicfSmlkPreemptionMode_Object=MibTableColumn
hpnicfSmlkPreemptionMode=_HpnicfSmlkPreemptionMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,3),_HpnicfSmlkPreemptionMode_Type())
hpnicfSmlkPreemptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkPreemptionMode.setStatus(_A)
class _HpnicfSmlkSpeedThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HpnicfSmlkSpeedThreshold_Type.__name__=_C
_HpnicfSmlkSpeedThreshold_Object=MibTableColumn
hpnicfSmlkSpeedThreshold=_HpnicfSmlkSpeedThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,4),_HpnicfSmlkSpeedThreshold_Type())
hpnicfSmlkSpeedThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkSpeedThreshold.setStatus(_A)
class _HpnicfSmlkPreemptionDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HpnicfSmlkPreemptionDelay_Type.__name__=_C
_HpnicfSmlkPreemptionDelay_Object=MibTableColumn
hpnicfSmlkPreemptionDelay=_HpnicfSmlkPreemptionDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,5),_HpnicfSmlkPreemptionDelay_Type())
hpnicfSmlkPreemptionDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkPreemptionDelay.setStatus(_A)
class _HpnicfSmlkControlVlanID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_HpnicfSmlkControlVlanID_Type.__name__=_C
_HpnicfSmlkControlVlanID_Object=MibTableColumn
hpnicfSmlkControlVlanID=_HpnicfSmlkControlVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,6),_HpnicfSmlkControlVlanID_Type())
hpnicfSmlkControlVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkControlVlanID.setStatus(_A)
class _HpnicfSmlkInstanceListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfSmlkInstanceListLow_Type.__name__=_E
_HpnicfSmlkInstanceListLow_Object=MibTableColumn
hpnicfSmlkInstanceListLow=_HpnicfSmlkInstanceListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,7),_HpnicfSmlkInstanceListLow_Type())
hpnicfSmlkInstanceListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkInstanceListLow.setStatus(_A)
class _HpnicfSmlkInstanceListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfSmlkInstanceListHigh_Type.__name__=_E
_HpnicfSmlkInstanceListHigh_Object=MibTableColumn
hpnicfSmlkInstanceListHigh=_HpnicfSmlkInstanceListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,8),_HpnicfSmlkInstanceListHigh_Type())
hpnicfSmlkInstanceListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkInstanceListHigh.setStatus(_A)
_HpnicfSmlkGroupRowStatus_Type=RowStatus
_HpnicfSmlkGroupRowStatus_Object=MibTableColumn
hpnicfSmlkGroupRowStatus=_HpnicfSmlkGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,1,1,9),_HpnicfSmlkGroupRowStatus_Type())
hpnicfSmlkGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkGroupRowStatus.setStatus(_A)
_HpnicfSmlkPortTable_Object=MibTable
hpnicfSmlkPortTable=_HpnicfSmlkPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2))
if mibBuilder.loadTexts:hpnicfSmlkPortTable.setStatus(_A)
_HpnicfSmlkPortEntry_Object=MibTableRow
hpnicfSmlkPortEntry=_HpnicfSmlkPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1))
hpnicfSmlkPortEntry.setIndexNames((0,_D,_F),(0,_D,_H))
if mibBuilder.loadTexts:hpnicfSmlkPortEntry.setStatus(_A)
_HpnicfSmlkPortIfIndex_Type=InterfaceIndex
_HpnicfSmlkPortIfIndex_Object=MibTableColumn
hpnicfSmlkPortIfIndex=_HpnicfSmlkPortIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1,1),_HpnicfSmlkPortIfIndex_Type())
hpnicfSmlkPortIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfSmlkPortIfIndex.setStatus(_A)
class _HpnicfSmlkPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_HpnicfSmlkPortRole_Type.__name__=_C
_HpnicfSmlkPortRole_Object=MibTableColumn
hpnicfSmlkPortRole=_HpnicfSmlkPortRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1,2),_HpnicfSmlkPortRole_Type())
hpnicfSmlkPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkPortRole.setStatus(_A)
class _HpnicfSmlkPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('active',2),('standby',3)))
_HpnicfSmlkPortStatus_Type.__name__=_C
_HpnicfSmlkPortStatus_Object=MibTableColumn
hpnicfSmlkPortStatus=_HpnicfSmlkPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1,3),_HpnicfSmlkPortStatus_Type())
hpnicfSmlkPortStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSmlkPortStatus.setStatus(_A)
_HpnicfSmlkFlushCount_Type=Counter64
_HpnicfSmlkFlushCount_Object=MibTableColumn
hpnicfSmlkFlushCount=_HpnicfSmlkFlushCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1,4),_HpnicfSmlkFlushCount_Type())
hpnicfSmlkFlushCount.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSmlkFlushCount.setStatus(_A)
_HpnicfSmlkLastFlushTime_Type=DateAndTime
_HpnicfSmlkLastFlushTime_Object=MibTableColumn
hpnicfSmlkLastFlushTime=_HpnicfSmlkLastFlushTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1,5),_HpnicfSmlkLastFlushTime_Type())
hpnicfSmlkLastFlushTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSmlkLastFlushTime.setStatus(_A)
_HpnicfSmlkPortRowStatus_Type=RowStatus
_HpnicfSmlkPortRowStatus_Object=MibTableColumn
hpnicfSmlkPortRowStatus=_HpnicfSmlkPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,2,1,6),_HpnicfSmlkPortRowStatus_Type())
hpnicfSmlkPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSmlkPortRowStatus.setStatus(_A)
_HpnicfSmlkFlushEnableTable_Object=MibTable
hpnicfSmlkFlushEnableTable=_HpnicfSmlkFlushEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,3))
if mibBuilder.loadTexts:hpnicfSmlkFlushEnableTable.setStatus(_A)
_HpnicfSmlkFlushEnableEntry_Object=MibTableRow
hpnicfSmlkFlushEnableEntry=_HpnicfSmlkFlushEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,3,1))
hpnicfSmlkFlushEnableEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfSmlkFlushEnableEntry.setStatus(_A)
_HpnicfSmlkIfIndex_Type=InterfaceIndex
_HpnicfSmlkIfIndex_Object=MibTableColumn
hpnicfSmlkIfIndex=_HpnicfSmlkIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,3,1,1),_HpnicfSmlkIfIndex_Type())
hpnicfSmlkIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfSmlkIfIndex.setStatus(_A)
class _HpnicfSmlkControlVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfSmlkControlVlanListLow_Type.__name__=_E
_HpnicfSmlkControlVlanListLow_Object=MibTableColumn
hpnicfSmlkControlVlanListLow=_HpnicfSmlkControlVlanListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,3,1,2),_HpnicfSmlkControlVlanListLow_Type())
hpnicfSmlkControlVlanListLow.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfSmlkControlVlanListLow.setStatus(_A)
class _HpnicfSmlkControlVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfSmlkControlVlanListHigh_Type.__name__=_E
_HpnicfSmlkControlVlanListHigh_Object=MibTableColumn
hpnicfSmlkControlVlanListHigh=_HpnicfSmlkControlVlanListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,147,1,3,1,3),_HpnicfSmlkControlVlanListHigh_Type())
hpnicfSmlkControlVlanListHigh.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfSmlkControlVlanListHigh.setStatus(_A)
_HpnicfSmlkTrap_ObjectIdentity=ObjectIdentity
hpnicfSmlkTrap=_HpnicfSmlkTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,147,2))
_HpnicfSmlkTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfSmlkTrapPrefix=_HpnicfSmlkTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,147,2,0))
hpnicfSmlkGroupLinkActive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,147,2,0,1))
hpnicfSmlkGroupLinkActive.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:hpnicfSmlkGroupLinkActive.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfSmlk':hpnicfSmlk,'hpnicfSmlkObject':hpnicfSmlkObject,'hpnicfSmlkGroupTable':hpnicfSmlkGroupTable,'hpnicfSmlkGroupEntry':hpnicfSmlkGroupEntry,_F:hpnicfSmlkGroupID,'hpnicfSmlkDeviceID':hpnicfSmlkDeviceID,'hpnicfSmlkPreemptionMode':hpnicfSmlkPreemptionMode,'hpnicfSmlkSpeedThreshold':hpnicfSmlkSpeedThreshold,'hpnicfSmlkPreemptionDelay':hpnicfSmlkPreemptionDelay,'hpnicfSmlkControlVlanID':hpnicfSmlkControlVlanID,'hpnicfSmlkInstanceListLow':hpnicfSmlkInstanceListLow,'hpnicfSmlkInstanceListHigh':hpnicfSmlkInstanceListHigh,'hpnicfSmlkGroupRowStatus':hpnicfSmlkGroupRowStatus,'hpnicfSmlkPortTable':hpnicfSmlkPortTable,'hpnicfSmlkPortEntry':hpnicfSmlkPortEntry,_H:hpnicfSmlkPortIfIndex,'hpnicfSmlkPortRole':hpnicfSmlkPortRole,'hpnicfSmlkPortStatus':hpnicfSmlkPortStatus,'hpnicfSmlkFlushCount':hpnicfSmlkFlushCount,'hpnicfSmlkLastFlushTime':hpnicfSmlkLastFlushTime,'hpnicfSmlkPortRowStatus':hpnicfSmlkPortRowStatus,'hpnicfSmlkFlushEnableTable':hpnicfSmlkFlushEnableTable,'hpnicfSmlkFlushEnableEntry':hpnicfSmlkFlushEnableEntry,_J:hpnicfSmlkIfIndex,'hpnicfSmlkControlVlanListLow':hpnicfSmlkControlVlanListLow,'hpnicfSmlkControlVlanListHigh':hpnicfSmlkControlVlanListHigh,'hpnicfSmlkTrap':hpnicfSmlkTrap,'hpnicfSmlkTrapPrefix':hpnicfSmlkTrapPrefix,'hpnicfSmlkGroupLinkActive':hpnicfSmlkGroupLinkActive})