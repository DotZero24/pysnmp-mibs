_I='unkown'
_H='mprSwPortNo'
_G='mprSwSlotNo'
_F='cE1IfIndex'
_E='panelIndex'
_D='Integer32'
_C='MPPANEL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpPanelMib=ModuleIdentity((1,3,6,1,4,1,5651,3,1))
_PanelTable_Object=MibTable
panelTable=_PanelTable_Object((1,3,6,1,4,1,5651,3,1,1))
if mibBuilder.loadTexts:panelTable.setStatus(_A)
_PanelEntry_Object=MibTableRow
panelEntry=_PanelEntry_Object((1,3,6,1,4,1,5651,3,1,1,1))
panelEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:panelEntry.setStatus(_A)
_PanelIndex_Type=DisplayString
_PanelIndex_Object=MibTableColumn
panelIndex=_PanelIndex_Object((1,3,6,1,4,1,5651,3,1,1,1,1),_PanelIndex_Type())
panelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:panelIndex.setStatus(_A)
_PanelType_Type=Integer32
_PanelType_Object=MibTableColumn
panelType=_PanelType_Object((1,3,6,1,4,1,5651,3,1,1,1,2),_PanelType_Type())
panelType.setMaxAccess(_B)
if mibBuilder.loadTexts:panelType.setStatus(_A)
_PanelIfIndex_Type=Integer32
_PanelIfIndex_Object=MibTableColumn
panelIfIndex=_PanelIfIndex_Object((1,3,6,1,4,1,5651,3,1,1,1,3),_PanelIfIndex_Type())
panelIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:panelIfIndex.setStatus(_A)
_CE1TimeslotsTable_Object=MibTable
cE1TimeslotsTable=_CE1TimeslotsTable_Object((1,3,6,1,4,1,5651,3,1,3))
if mibBuilder.loadTexts:cE1TimeslotsTable.setStatus(_A)
_CE1TimeslotsEntry_Object=MibTableRow
cE1TimeslotsEntry=_CE1TimeslotsEntry_Object((1,3,6,1,4,1,5651,3,1,3,1))
cE1TimeslotsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cE1TimeslotsEntry.setStatus(_A)
_CE1IfIndex_Type=Integer32
_CE1IfIndex_Object=MibTableColumn
cE1IfIndex=_CE1IfIndex_Object((1,3,6,1,4,1,5651,3,1,3,1,1),_CE1IfIndex_Type())
cE1IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cE1IfIndex.setStatus(_A)
_CE1Timeslots_Type=Integer32
_CE1Timeslots_Object=MibTableColumn
cE1Timeslots=_CE1Timeslots_Object((1,3,6,1,4,1,5651,3,1,3,1,2),_CE1Timeslots_Type())
cE1Timeslots.setMaxAccess(_B)
if mibBuilder.loadTexts:cE1Timeslots.setStatus(_A)
_MprSwPortTable_Object=MibTable
mprSwPortTable=_MprSwPortTable_Object((1,3,6,1,4,1,5651,3,1,10))
if mibBuilder.loadTexts:mprSwPortTable.setStatus(_A)
_MprSwPortEntry_Object=MibTableRow
mprSwPortEntry=_MprSwPortEntry_Object((1,3,6,1,4,1,5651,3,1,10,1))
mprSwPortEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:mprSwPortEntry.setStatus(_A)
_MprSwSlotNo_Type=Integer32
_MprSwSlotNo_Object=MibTableColumn
mprSwSlotNo=_MprSwSlotNo_Object((1,3,6,1,4,1,5651,3,1,10,1,1),_MprSwSlotNo_Type())
mprSwSlotNo.setMaxAccess(_B)
if mibBuilder.loadTexts:mprSwSlotNo.setStatus(_A)
_MprSwPortNo_Type=Integer32
_MprSwPortNo_Object=MibTableColumn
mprSwPortNo=_MprSwPortNo_Object((1,3,6,1,4,1,5651,3,1,10,1,2),_MprSwPortNo_Type())
mprSwPortNo.setMaxAccess(_B)
if mibBuilder.loadTexts:mprSwPortNo.setStatus(_A)
class _MprSwPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MprSwPortLinkStatus_Type.__name__=_D
_MprSwPortLinkStatus_Object=MibTableColumn
mprSwPortLinkStatus=_MprSwPortLinkStatus_Object((1,3,6,1,4,1,5651,3,1,10,1,3),_MprSwPortLinkStatus_Type())
mprSwPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mprSwPortLinkStatus.setStatus(_A)
class _MprSwPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('speed10',2),('speed100',3),('speed1000',4)))
_MprSwPortSpeed_Type.__name__=_D
_MprSwPortSpeed_Object=MibTableColumn
mprSwPortSpeed=_MprSwPortSpeed_Object((1,3,6,1,4,1,5651,3,1,10,1,4),_MprSwPortSpeed_Type())
mprSwPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:mprSwPortSpeed.setStatus(_A)
class _MprSwPortDeplux_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('half',2),('full',3)))
_MprSwPortDeplux_Type.__name__=_D
_MprSwPortDeplux_Object=MibTableColumn
mprSwPortDeplux=_MprSwPortDeplux_Object((1,3,6,1,4,1,5651,3,1,10,1,5),_MprSwPortDeplux_Type())
mprSwPortDeplux.setMaxAccess(_B)
if mibBuilder.loadTexts:mprSwPortDeplux.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mpPanelMib':mpPanelMib,'panelTable':panelTable,'panelEntry':panelEntry,_E:panelIndex,'panelType':panelType,'panelIfIndex':panelIfIndex,'cE1TimeslotsTable':cE1TimeslotsTable,'cE1TimeslotsEntry':cE1TimeslotsEntry,_F:cE1IfIndex,'cE1Timeslots':cE1Timeslots,'mprSwPortTable':mprSwPortTable,'mprSwPortEntry':mprSwPortEntry,_G:mprSwSlotNo,_H:mprSwPortNo,'mprSwPortLinkStatus':mprSwPortLinkStatus,'mprSwPortSpeed':mprSwPortSpeed,'mprSwPortDeplux':mprSwPortDeplux})