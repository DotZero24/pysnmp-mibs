_E='panEventIndex'
_D='PANASAS-EVENTS-MIB-V1'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
panFs,=mibBuilder.importSymbols('PANASAS-PANFS-MIB-V1','panFs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
panEvents=ModuleIdentity((1,3,6,1,4,1,10159,1,3,1))
if mibBuilder.loadTexts:panEvents.setRevisions(('2011-04-07 00:00',))
class _PanEventTableSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_PanEventTableSize_Type.__name__=_C
_PanEventTableSize_Object=MibScalar
panEventTableSize=_PanEventTableSize_Object((1,3,6,1,4,1,10159,1,3,1,1),_PanEventTableSize_Type())
panEventTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventTableSize.setStatus(_A)
_PanEventTable_Object=MibTable
panEventTable=_PanEventTable_Object((1,3,6,1,4,1,10159,1,3,1,2))
if mibBuilder.loadTexts:panEventTable.setStatus(_A)
_PanEventEntry_Object=MibTableRow
panEventEntry=_PanEventEntry_Object((1,3,6,1,4,1,10159,1,3,1,2,1))
panEventEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:panEventEntry.setStatus(_A)
class _PanEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PanEventIndex_Type.__name__=_C
_PanEventIndex_Object=MibTableColumn
panEventIndex=_PanEventIndex_Object((1,3,6,1,4,1,10159,1,3,1,2,1,1),_PanEventIndex_Type())
panEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventIndex.setStatus(_A)
_PanEventCategory_Type=DisplayString
_PanEventCategory_Object=MibTableColumn
panEventCategory=_PanEventCategory_Object((1,3,6,1,4,1,10159,1,3,1,2,1,2),_PanEventCategory_Type())
panEventCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventCategory.setStatus(_A)
_PanEventDate_Type=DisplayString
_PanEventDate_Object=MibTableColumn
panEventDate=_PanEventDate_Object((1,3,6,1,4,1,10159,1,3,1,2,1,3),_PanEventDate_Type())
panEventDate.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventDate.setStatus(_A)
_PanEventTime_Type=DisplayString
_PanEventTime_Object=MibTableColumn
panEventTime=_PanEventTime_Object((1,3,6,1,4,1,10159,1,3,1,2,1,4),_PanEventTime_Type())
panEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventTime.setStatus(_A)
_PanEventShelfName_Type=DisplayString
_PanEventShelfName_Object=MibTableColumn
panEventShelfName=_PanEventShelfName_Object((1,3,6,1,4,1,10159,1,3,1,2,1,5),_PanEventShelfName_Type())
panEventShelfName.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventShelfName.setStatus(_A)
_PanEventShelfSlot_Type=Unsigned32
_PanEventShelfSlot_Object=MibTableColumn
panEventShelfSlot=_PanEventShelfSlot_Object((1,3,6,1,4,1,10159,1,3,1,2,1,6),_PanEventShelfSlot_Type())
panEventShelfSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventShelfSlot.setStatus(_A)
_PanEventHwDesc_Type=DisplayString
_PanEventHwDesc_Object=MibTableColumn
panEventHwDesc=_PanEventHwDesc_Object((1,3,6,1,4,1,10159,1,3,1,2,1,7),_PanEventHwDesc_Type())
panEventHwDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventHwDesc.setStatus(_A)
_PanEventBladeIPAddr_Type=IpAddress
_PanEventBladeIPAddr_Object=MibTableColumn
panEventBladeIPAddr=_PanEventBladeIPAddr_Object((1,3,6,1,4,1,10159,1,3,1,2,1,8),_PanEventBladeIPAddr_Type())
panEventBladeIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventBladeIPAddr.setStatus(_A)
_PanEventText_Type=DisplayString
_PanEventText_Object=MibTableColumn
panEventText=_PanEventText_Object((1,3,6,1,4,1,10159,1,3,1,2,1,9),_PanEventText_Type())
panEventText.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventText.setStatus(_A)
class _PanEventCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PanEventCode_Type.__name__=_C
_PanEventCode_Object=MibTableColumn
panEventCode=_PanEventCode_Object((1,3,6,1,4,1,10159,1,3,1,2,1,10),_PanEventCode_Type())
panEventCode.setMaxAccess(_B)
if mibBuilder.loadTexts:panEventCode.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'panEvents':panEvents,'panEventTableSize':panEventTableSize,'panEventTable':panEventTable,'panEventEntry':panEventEntry,_E:panEventIndex,'panEventCategory':panEventCategory,'panEventDate':panEventDate,'panEventTime':panEventTime,'panEventShelfName':panEventShelfName,'panEventShelfSlot':panEventShelfSlot,'panEventHwDesc':panEventHwDesc,'panEventBladeIPAddr':panEventBladeIPAddr,'panEventText':panEventText,'panEventCode':panEventCode})