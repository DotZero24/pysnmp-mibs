_K='read-write'
_J='h3cSmlkIfIndex'
_I='accessible-for-notify'
_H='h3cSmlkPortIfIndex'
_G='read-only'
_F='h3cSmlkGroupID'
_E='OctetString'
_D='H3C-SMLK-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
h3cSmlk=ModuleIdentity((1,3,6,1,4,1,2011,10,2,147))
if mibBuilder.loadTexts:h3cSmlk.setRevisions(('2014-07-23 15:03',))
_H3cSmlkObject_ObjectIdentity=ObjectIdentity
h3cSmlkObject=_H3cSmlkObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,147,1))
_H3cSmlkGroupTable_Object=MibTable
h3cSmlkGroupTable=_H3cSmlkGroupTable_Object((1,3,6,1,4,1,2011,10,2,147,1,1))
if mibBuilder.loadTexts:h3cSmlkGroupTable.setStatus(_A)
_H3cSmlkGroupEntry_Object=MibTableRow
h3cSmlkGroupEntry=_H3cSmlkGroupEntry_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1))
h3cSmlkGroupEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cSmlkGroupEntry.setStatus(_A)
class _H3cSmlkGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_H3cSmlkGroupID_Type.__name__=_C
_H3cSmlkGroupID_Object=MibTableColumn
h3cSmlkGroupID=_H3cSmlkGroupID_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,1),_H3cSmlkGroupID_Type())
h3cSmlkGroupID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSmlkGroupID.setStatus(_A)
_H3cSmlkDeviceID_Type=MacAddress
_H3cSmlkDeviceID_Object=MibTableColumn
h3cSmlkDeviceID=_H3cSmlkDeviceID_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,2),_H3cSmlkDeviceID_Type())
h3cSmlkDeviceID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSmlkDeviceID.setStatus(_A)
class _H3cSmlkPreemptionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('role',2),('speed',3)))
_H3cSmlkPreemptionMode_Type.__name__=_C
_H3cSmlkPreemptionMode_Object=MibTableColumn
h3cSmlkPreemptionMode=_H3cSmlkPreemptionMode_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,3),_H3cSmlkPreemptionMode_Type())
h3cSmlkPreemptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkPreemptionMode.setStatus(_A)
class _H3cSmlkSpeedThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_H3cSmlkSpeedThreshold_Type.__name__=_C
_H3cSmlkSpeedThreshold_Object=MibTableColumn
h3cSmlkSpeedThreshold=_H3cSmlkSpeedThreshold_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,4),_H3cSmlkSpeedThreshold_Type())
h3cSmlkSpeedThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkSpeedThreshold.setStatus(_A)
class _H3cSmlkPreemptionDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_H3cSmlkPreemptionDelay_Type.__name__=_C
_H3cSmlkPreemptionDelay_Object=MibTableColumn
h3cSmlkPreemptionDelay=_H3cSmlkPreemptionDelay_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,5),_H3cSmlkPreemptionDelay_Type())
h3cSmlkPreemptionDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkPreemptionDelay.setStatus(_A)
class _H3cSmlkControlVlanID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_H3cSmlkControlVlanID_Type.__name__=_C
_H3cSmlkControlVlanID_Object=MibTableColumn
h3cSmlkControlVlanID=_H3cSmlkControlVlanID_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,6),_H3cSmlkControlVlanID_Type())
h3cSmlkControlVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkControlVlanID.setStatus(_A)
class _H3cSmlkInstanceListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cSmlkInstanceListLow_Type.__name__=_E
_H3cSmlkInstanceListLow_Object=MibTableColumn
h3cSmlkInstanceListLow=_H3cSmlkInstanceListLow_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,7),_H3cSmlkInstanceListLow_Type())
h3cSmlkInstanceListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkInstanceListLow.setStatus(_A)
class _H3cSmlkInstanceListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cSmlkInstanceListHigh_Type.__name__=_E
_H3cSmlkInstanceListHigh_Object=MibTableColumn
h3cSmlkInstanceListHigh=_H3cSmlkInstanceListHigh_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,8),_H3cSmlkInstanceListHigh_Type())
h3cSmlkInstanceListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkInstanceListHigh.setStatus(_A)
_H3cSmlkGroupRowStatus_Type=RowStatus
_H3cSmlkGroupRowStatus_Object=MibTableColumn
h3cSmlkGroupRowStatus=_H3cSmlkGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,147,1,1,1,9),_H3cSmlkGroupRowStatus_Type())
h3cSmlkGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkGroupRowStatus.setStatus(_A)
_H3cSmlkPortTable_Object=MibTable
h3cSmlkPortTable=_H3cSmlkPortTable_Object((1,3,6,1,4,1,2011,10,2,147,1,2))
if mibBuilder.loadTexts:h3cSmlkPortTable.setStatus(_A)
_H3cSmlkPortEntry_Object=MibTableRow
h3cSmlkPortEntry=_H3cSmlkPortEntry_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1))
h3cSmlkPortEntry.setIndexNames((0,_D,_F),(0,_D,_H))
if mibBuilder.loadTexts:h3cSmlkPortEntry.setStatus(_A)
_H3cSmlkPortIfIndex_Type=InterfaceIndex
_H3cSmlkPortIfIndex_Object=MibTableColumn
h3cSmlkPortIfIndex=_H3cSmlkPortIfIndex_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1,1),_H3cSmlkPortIfIndex_Type())
h3cSmlkPortIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cSmlkPortIfIndex.setStatus(_A)
class _H3cSmlkPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_H3cSmlkPortRole_Type.__name__=_C
_H3cSmlkPortRole_Object=MibTableColumn
h3cSmlkPortRole=_H3cSmlkPortRole_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1,2),_H3cSmlkPortRole_Type())
h3cSmlkPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkPortRole.setStatus(_A)
class _H3cSmlkPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('active',2),('standby',3)))
_H3cSmlkPortStatus_Type.__name__=_C
_H3cSmlkPortStatus_Object=MibTableColumn
h3cSmlkPortStatus=_H3cSmlkPortStatus_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1,3),_H3cSmlkPortStatus_Type())
h3cSmlkPortStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSmlkPortStatus.setStatus(_A)
_H3cSmlkFlushCount_Type=Counter64
_H3cSmlkFlushCount_Object=MibTableColumn
h3cSmlkFlushCount=_H3cSmlkFlushCount_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1,4),_H3cSmlkFlushCount_Type())
h3cSmlkFlushCount.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSmlkFlushCount.setStatus(_A)
_H3cSmlkLastFlushTime_Type=DateAndTime
_H3cSmlkLastFlushTime_Object=MibTableColumn
h3cSmlkLastFlushTime=_H3cSmlkLastFlushTime_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1,5),_H3cSmlkLastFlushTime_Type())
h3cSmlkLastFlushTime.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSmlkLastFlushTime.setStatus(_A)
_H3cSmlkPortRowStatus_Type=RowStatus
_H3cSmlkPortRowStatus_Object=MibTableColumn
h3cSmlkPortRowStatus=_H3cSmlkPortRowStatus_Object((1,3,6,1,4,1,2011,10,2,147,1,2,1,6),_H3cSmlkPortRowStatus_Type())
h3cSmlkPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSmlkPortRowStatus.setStatus(_A)
_H3cSmlkFlushEnableTable_Object=MibTable
h3cSmlkFlushEnableTable=_H3cSmlkFlushEnableTable_Object((1,3,6,1,4,1,2011,10,2,147,1,3))
if mibBuilder.loadTexts:h3cSmlkFlushEnableTable.setStatus(_A)
_H3cSmlkFlushEnableEntry_Object=MibTableRow
h3cSmlkFlushEnableEntry=_H3cSmlkFlushEnableEntry_Object((1,3,6,1,4,1,2011,10,2,147,1,3,1))
h3cSmlkFlushEnableEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:h3cSmlkFlushEnableEntry.setStatus(_A)
_H3cSmlkIfIndex_Type=InterfaceIndex
_H3cSmlkIfIndex_Object=MibTableColumn
h3cSmlkIfIndex=_H3cSmlkIfIndex_Object((1,3,6,1,4,1,2011,10,2,147,1,3,1,1),_H3cSmlkIfIndex_Type())
h3cSmlkIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cSmlkIfIndex.setStatus(_A)
class _H3cSmlkControlVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cSmlkControlVlanListLow_Type.__name__=_E
_H3cSmlkControlVlanListLow_Object=MibTableColumn
h3cSmlkControlVlanListLow=_H3cSmlkControlVlanListLow_Object((1,3,6,1,4,1,2011,10,2,147,1,3,1,2),_H3cSmlkControlVlanListLow_Type())
h3cSmlkControlVlanListLow.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSmlkControlVlanListLow.setStatus(_A)
class _H3cSmlkControlVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cSmlkControlVlanListHigh_Type.__name__=_E
_H3cSmlkControlVlanListHigh_Object=MibTableColumn
h3cSmlkControlVlanListHigh=_H3cSmlkControlVlanListHigh_Object((1,3,6,1,4,1,2011,10,2,147,1,3,1,3),_H3cSmlkControlVlanListHigh_Type())
h3cSmlkControlVlanListHigh.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cSmlkControlVlanListHigh.setStatus(_A)
_H3cSmlkTrap_ObjectIdentity=ObjectIdentity
h3cSmlkTrap=_H3cSmlkTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,147,2))
_H3cSmlkTrapPrefix_ObjectIdentity=ObjectIdentity
h3cSmlkTrapPrefix=_H3cSmlkTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,147,2,0))
h3cSmlkGroupLinkActive=NotificationType((1,3,6,1,4,1,2011,10,2,147,2,0,1))
h3cSmlkGroupLinkActive.setObjects(*((_D,_F),(_D,_H)))
if mibBuilder.loadTexts:h3cSmlkGroupLinkActive.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cSmlk':h3cSmlk,'h3cSmlkObject':h3cSmlkObject,'h3cSmlkGroupTable':h3cSmlkGroupTable,'h3cSmlkGroupEntry':h3cSmlkGroupEntry,_F:h3cSmlkGroupID,'h3cSmlkDeviceID':h3cSmlkDeviceID,'h3cSmlkPreemptionMode':h3cSmlkPreemptionMode,'h3cSmlkSpeedThreshold':h3cSmlkSpeedThreshold,'h3cSmlkPreemptionDelay':h3cSmlkPreemptionDelay,'h3cSmlkControlVlanID':h3cSmlkControlVlanID,'h3cSmlkInstanceListLow':h3cSmlkInstanceListLow,'h3cSmlkInstanceListHigh':h3cSmlkInstanceListHigh,'h3cSmlkGroupRowStatus':h3cSmlkGroupRowStatus,'h3cSmlkPortTable':h3cSmlkPortTable,'h3cSmlkPortEntry':h3cSmlkPortEntry,_H:h3cSmlkPortIfIndex,'h3cSmlkPortRole':h3cSmlkPortRole,'h3cSmlkPortStatus':h3cSmlkPortStatus,'h3cSmlkFlushCount':h3cSmlkFlushCount,'h3cSmlkLastFlushTime':h3cSmlkLastFlushTime,'h3cSmlkPortRowStatus':h3cSmlkPortRowStatus,'h3cSmlkFlushEnableTable':h3cSmlkFlushEnableTable,'h3cSmlkFlushEnableEntry':h3cSmlkFlushEnableEntry,_J:h3cSmlkIfIndex,'h3cSmlkControlVlanListLow':h3cSmlkControlVlanListLow,'h3cSmlkControlVlanListHigh':h3cSmlkControlVlanListHigh,'h3cSmlkTrap':h3cSmlkTrap,'h3cSmlkTrapPrefix':h3cSmlkTrapPrefix,'h3cSmlkGroupLinkActive':h3cSmlkGroupLinkActive})