_H='adGenAtmBulkATMFilterInstance'
_G='ADTRAN-GENATM-MIB'
_F='Integer32'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenAtm,adGenAtmID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenAtm','adGenAtmID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAtmIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,48,1))
if mibBuilder.loadTexts:adGenAtmIdentity.setRevisions(('2011-12-28 00:00',))
_AdGenAtmStatus_ObjectIdentity=ObjectIdentity
adGenAtmStatus=_AdGenAtmStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,48,1))
_AdGenAtmTotalCountStatusTable_Object=MibTable
adGenAtmTotalCountStatusTable=_AdGenAtmTotalCountStatusTable_Object((1,3,6,1,4,1,664,5,70,48,1,1))
if mibBuilder.loadTexts:adGenAtmTotalCountStatusTable.setStatus(_A)
_AdGenAtmTotalCountStatusEntry_Object=MibTableRow
adGenAtmTotalCountStatusEntry=_AdGenAtmTotalCountStatusEntry_Object((1,3,6,1,4,1,664,5,70,48,1,1,1))
adGenAtmTotalCountStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenAtmTotalCountStatusEntry.setStatus(_A)
_AdGenAtmTotalCountVcl_Type=Integer32
_AdGenAtmTotalCountVcl_Object=MibTableColumn
adGenAtmTotalCountVcl=_AdGenAtmTotalCountVcl_Object((1,3,6,1,4,1,664,5,70,48,1,1,1,1),_AdGenAtmTotalCountVcl_Type())
adGenAtmTotalCountVcl.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmTotalCountVcl.setStatus(_A)
_AdGenAtmTotalCountVpl_Type=Integer32
_AdGenAtmTotalCountVpl_Object=MibTableColumn
adGenAtmTotalCountVpl=_AdGenAtmTotalCountVpl_Object((1,3,6,1,4,1,664,5,70,48,1,1,1,2),_AdGenAtmTotalCountVpl_Type())
adGenAtmTotalCountVpl.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmTotalCountVpl.setStatus(_A)
_AdGenAtmTotalCountVccc_Type=Integer32
_AdGenAtmTotalCountVccc_Object=MibTableColumn
adGenAtmTotalCountVccc=_AdGenAtmTotalCountVccc_Object((1,3,6,1,4,1,664,5,70,48,1,1,1,3),_AdGenAtmTotalCountVccc_Type())
adGenAtmTotalCountVccc.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmTotalCountVccc.setStatus(_A)
_AdGenAtmTotalCountVpcc_Type=Integer32
_AdGenAtmTotalCountVpcc_Object=MibTableColumn
adGenAtmTotalCountVpcc=_AdGenAtmTotalCountVpcc_Object((1,3,6,1,4,1,664,5,70,48,1,1,1,4),_AdGenAtmTotalCountVpcc_Type())
adGenAtmTotalCountVpcc.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmTotalCountVpcc.setStatus(_A)
_AdGenAtmTotalCountVcIntwk_Type=Integer32
_AdGenAtmTotalCountVcIntwk_Object=MibTableColumn
adGenAtmTotalCountVcIntwk=_AdGenAtmTotalCountVcIntwk_Object((1,3,6,1,4,1,664,5,70,48,1,1,1,5),_AdGenAtmTotalCountVcIntwk_Type())
adGenAtmTotalCountVcIntwk.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmTotalCountVcIntwk.setStatus(_A)
_AdGenAtmTotalCountVpIntwk_Type=Integer32
_AdGenAtmTotalCountVpIntwk_Object=MibTableColumn
adGenAtmTotalCountVpIntwk=_AdGenAtmTotalCountVpIntwk_Object((1,3,6,1,4,1,664,5,70,48,1,1,1,6),_AdGenAtmTotalCountVpIntwk_Type())
adGenAtmTotalCountVpIntwk.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmTotalCountVpIntwk.setStatus(_A)
_AdGenAtmBulkATM_ObjectIdentity=ObjectIdentity
adGenAtmBulkATM=_AdGenAtmBulkATM_ObjectIdentity((1,3,6,1,4,1,664,5,70,48,2))
_AdGenAtmReserveInstanceBulkATMSlotTable_Object=MibTable
adGenAtmReserveInstanceBulkATMSlotTable=_AdGenAtmReserveInstanceBulkATMSlotTable_Object((1,3,6,1,4,1,664,5,70,48,2,1))
if mibBuilder.loadTexts:adGenAtmReserveInstanceBulkATMSlotTable.setStatus(_A)
_AdGenAtmReserveInstanceBulkATMSlotEntry_Object=MibTableRow
adGenAtmReserveInstanceBulkATMSlotEntry=_AdGenAtmReserveInstanceBulkATMSlotEntry_Object((1,3,6,1,4,1,664,5,70,48,2,1,1))
adGenAtmReserveInstanceBulkATMSlotEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenAtmReserveInstanceBulkATMSlotEntry.setStatus(_A)
_AdGenAtmReserveInstanceBulkATMSlotInstance_Type=Integer32
_AdGenAtmReserveInstanceBulkATMSlotInstance_Object=MibTableColumn
adGenAtmReserveInstanceBulkATMSlotInstance=_AdGenAtmReserveInstanceBulkATMSlotInstance_Object((1,3,6,1,4,1,664,5,70,48,2,1,1,1),_AdGenAtmReserveInstanceBulkATMSlotInstance_Type())
adGenAtmReserveInstanceBulkATMSlotInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenAtmReserveInstanceBulkATMSlotInstance.setStatus(_A)
_AdGenAtmBulkATMFilterTable_Object=MibTable
adGenAtmBulkATMFilterTable=_AdGenAtmBulkATMFilterTable_Object((1,3,6,1,4,1,664,5,70,48,2,2))
if mibBuilder.loadTexts:adGenAtmBulkATMFilterTable.setStatus(_A)
_AdGenAtmBulkATMFilterEntry_Object=MibTableRow
adGenAtmBulkATMFilterEntry=_AdGenAtmBulkATMFilterEntry_Object((1,3,6,1,4,1,664,5,70,48,2,2,1))
adGenAtmBulkATMFilterEntry.setIndexNames((0,_D,_E),(0,_G,_H))
if mibBuilder.loadTexts:adGenAtmBulkATMFilterEntry.setStatus(_A)
_AdGenAtmBulkATMFilterInstance_Type=Integer32
_AdGenAtmBulkATMFilterInstance_Object=MibTableColumn
adGenAtmBulkATMFilterInstance=_AdGenAtmBulkATMFilterInstance_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,1),_AdGenAtmBulkATMFilterInstance_Type())
adGenAtmBulkATMFilterInstance.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenAtmBulkATMFilterInstance.setStatus(_A)
class _AdGenAtmBulkATMFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('notspecified',0),('vccc',1),('vpcc',2),('vcl',3),('vpl',4),('vpintwk',5),('vcintwk',6)))
_AdGenAtmBulkATMFilterType_Type.__name__=_F
_AdGenAtmBulkATMFilterType_Object=MibTableColumn
adGenAtmBulkATMFilterType=_AdGenAtmBulkATMFilterType_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,2),_AdGenAtmBulkATMFilterType_Type())
adGenAtmBulkATMFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterType.setStatus(_A)
_AdGenAtmBulkATMFilterSlot1_Type=Unsigned32
_AdGenAtmBulkATMFilterSlot1_Object=MibTableColumn
adGenAtmBulkATMFilterSlot1=_AdGenAtmBulkATMFilterSlot1_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,3),_AdGenAtmBulkATMFilterSlot1_Type())
adGenAtmBulkATMFilterSlot1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterSlot1.setStatus(_A)
_AdGenAtmBulkATMFilterPort1_Type=Unsigned32
_AdGenAtmBulkATMFilterPort1_Object=MibTableColumn
adGenAtmBulkATMFilterPort1=_AdGenAtmBulkATMFilterPort1_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,4),_AdGenAtmBulkATMFilterPort1_Type())
adGenAtmBulkATMFilterPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterPort1.setStatus(_A)
_AdGenAtmBulkATMFilterVpi1_Type=Unsigned32
_AdGenAtmBulkATMFilterVpi1_Object=MibTableColumn
adGenAtmBulkATMFilterVpi1=_AdGenAtmBulkATMFilterVpi1_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,5),_AdGenAtmBulkATMFilterVpi1_Type())
adGenAtmBulkATMFilterVpi1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterVpi1.setStatus(_A)
_AdGenAtmBulkATMFilterVci1_Type=Unsigned32
_AdGenAtmBulkATMFilterVci1_Object=MibTableColumn
adGenAtmBulkATMFilterVci1=_AdGenAtmBulkATMFilterVci1_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,6),_AdGenAtmBulkATMFilterVci1_Type())
adGenAtmBulkATMFilterVci1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterVci1.setStatus(_A)
_AdGenAtmBulkATMFilterNode_Type=Unsigned32
_AdGenAtmBulkATMFilterNode_Object=MibTableColumn
adGenAtmBulkATMFilterNode=_AdGenAtmBulkATMFilterNode_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,7),_AdGenAtmBulkATMFilterNode_Type())
adGenAtmBulkATMFilterNode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterNode.setStatus(_A)
_AdGenAtmBulkATMFilterSlot2_Type=Unsigned32
_AdGenAtmBulkATMFilterSlot2_Object=MibTableColumn
adGenAtmBulkATMFilterSlot2=_AdGenAtmBulkATMFilterSlot2_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,8),_AdGenAtmBulkATMFilterSlot2_Type())
adGenAtmBulkATMFilterSlot2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterSlot2.setStatus(_A)
_AdGenAtmBulkATMFilterPort2_Type=Unsigned32
_AdGenAtmBulkATMFilterPort2_Object=MibTableColumn
adGenAtmBulkATMFilterPort2=_AdGenAtmBulkATMFilterPort2_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,9),_AdGenAtmBulkATMFilterPort2_Type())
adGenAtmBulkATMFilterPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterPort2.setStatus(_A)
_AdGenAtmBulkATMFilterVpi2_Type=Unsigned32
_AdGenAtmBulkATMFilterVpi2_Object=MibTableColumn
adGenAtmBulkATMFilterVpi2=_AdGenAtmBulkATMFilterVpi2_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,10),_AdGenAtmBulkATMFilterVpi2_Type())
adGenAtmBulkATMFilterVpi2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterVpi2.setStatus(_A)
_AdGenAtmBulkATMFilterVci2_Type=Unsigned32
_AdGenAtmBulkATMFilterVci2_Object=MibTableColumn
adGenAtmBulkATMFilterVci2=_AdGenAtmBulkATMFilterVci2_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,11),_AdGenAtmBulkATMFilterVci2_Type())
adGenAtmBulkATMFilterVci2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterVci2.setStatus(_A)
_AdGenAtmBulkATMFilterStag_Type=Unsigned32
_AdGenAtmBulkATMFilterStag_Object=MibTableColumn
adGenAtmBulkATMFilterStag=_AdGenAtmBulkATMFilterStag_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,12),_AdGenAtmBulkATMFilterStag_Type())
adGenAtmBulkATMFilterStag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterStag.setStatus(_A)
_AdGenAtmBulkATMFilterCtag_Type=Unsigned32
_AdGenAtmBulkATMFilterCtag_Object=MibTableColumn
adGenAtmBulkATMFilterCtag=_AdGenAtmBulkATMFilterCtag_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,13),_AdGenAtmBulkATMFilterCtag_Type())
adGenAtmBulkATMFilterCtag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMFilterCtag.setStatus(_A)
class _AdGenAtmBulkATMSlotInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('updateinstance',1))
_AdGenAtmBulkATMSlotInstance_Type.__name__=_F
_AdGenAtmBulkATMSlotInstance_Object=MibTableColumn
adGenAtmBulkATMSlotInstance=_AdGenAtmBulkATMSlotInstance_Object((1,3,6,1,4,1,664,5,70,48,2,2,1,14),_AdGenAtmBulkATMSlotInstance_Type())
adGenAtmBulkATMSlotInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenAtmBulkATMSlotInstance.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'adGenAtmStatus':adGenAtmStatus,'adGenAtmTotalCountStatusTable':adGenAtmTotalCountStatusTable,'adGenAtmTotalCountStatusEntry':adGenAtmTotalCountStatusEntry,'adGenAtmTotalCountVcl':adGenAtmTotalCountVcl,'adGenAtmTotalCountVpl':adGenAtmTotalCountVpl,'adGenAtmTotalCountVccc':adGenAtmTotalCountVccc,'adGenAtmTotalCountVpcc':adGenAtmTotalCountVpcc,'adGenAtmTotalCountVcIntwk':adGenAtmTotalCountVcIntwk,'adGenAtmTotalCountVpIntwk':adGenAtmTotalCountVpIntwk,'adGenAtmBulkATM':adGenAtmBulkATM,'adGenAtmReserveInstanceBulkATMSlotTable':adGenAtmReserveInstanceBulkATMSlotTable,'adGenAtmReserveInstanceBulkATMSlotEntry':adGenAtmReserveInstanceBulkATMSlotEntry,'adGenAtmReserveInstanceBulkATMSlotInstance':adGenAtmReserveInstanceBulkATMSlotInstance,'adGenAtmBulkATMFilterTable':adGenAtmBulkATMFilterTable,'adGenAtmBulkATMFilterEntry':adGenAtmBulkATMFilterEntry,_H:adGenAtmBulkATMFilterInstance,'adGenAtmBulkATMFilterType':adGenAtmBulkATMFilterType,'adGenAtmBulkATMFilterSlot1':adGenAtmBulkATMFilterSlot1,'adGenAtmBulkATMFilterPort1':adGenAtmBulkATMFilterPort1,'adGenAtmBulkATMFilterVpi1':adGenAtmBulkATMFilterVpi1,'adGenAtmBulkATMFilterVci1':adGenAtmBulkATMFilterVci1,'adGenAtmBulkATMFilterNode':adGenAtmBulkATMFilterNode,'adGenAtmBulkATMFilterSlot2':adGenAtmBulkATMFilterSlot2,'adGenAtmBulkATMFilterPort2':adGenAtmBulkATMFilterPort2,'adGenAtmBulkATMFilterVpi2':adGenAtmBulkATMFilterVpi2,'adGenAtmBulkATMFilterVci2':adGenAtmBulkATMFilterVci2,'adGenAtmBulkATMFilterStag':adGenAtmBulkATMFilterStag,'adGenAtmBulkATMFilterCtag':adGenAtmBulkATMFilterCtag,'adGenAtmBulkATMSlotInstance':adGenAtmBulkATMSlotInstance,'adGenAtmIdentity':adGenAtmIdentity})