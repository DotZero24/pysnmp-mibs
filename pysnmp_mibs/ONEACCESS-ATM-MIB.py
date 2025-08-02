_i='oacAtmStatGeneralGroup'
_h='oacAtmAal5PortRxFramesDiscarded'
_g='oacAtmAal5PortRxErrors'
_f='oacAtmAal5PortRxFrames'
_e='oacAtmAal5PortRxBytes'
_d='oacAtmAal5PortTxFramesDiscarded'
_c='oacAtmAal5PortTxFrames'
_b='oacAtmAal5PortTxBytes'
_a='oacAtmPortHecErrors'
_Z='oacAtmPortRxCellsDiscarded'
_Y='oacAtmPortRxCells'
_X='oacAtmPortTxCells'
_W='oacAtmAal5ChanReassemblyTimeouts'
_V='oacAtmAal5ChanLengthErrors'
_U='oacAtmAal5ChanCrc32Errors'
_T='oacAtmAal5ChanRxFramesDiscarded'
_S='oacAtmAal5ChanRxFrames'
_R='oacAtmAal5ChanTxFrames'
_Q='oacAtmAal1ChanRxOverflows'
_P='oacAtmAal1ChanTxUnderflows'
_O='oacAtmAal0ChanRxCellsDiscarded'
_N='oacAtmChanTxOverflows'
_M='oacAtmChanRxErrors'
_L='oacAtmChanRxCells'
_K='oacAtmChanRxBytes'
_J='oacAtmChanTxCells'
_I='oacAtmChanTxBytes'
_H='not-accessible'
_G='oacAtmChanVci'
_F='oacAtmChanVpi'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ONEACCESS-ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
oacExpIMAtmStatistics,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMAtmStatistics','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacAtmMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,667))
if mibBuilder.loadTexts:oacAtmMIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 00:01'))
_OacAtmStatObjects_ObjectIdentity=ObjectIdentity
oacAtmStatObjects=_OacAtmStatObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,1,1))
_OacAtmChannelTable_Object=MibTable
oacAtmChannelTable=_OacAtmChannelTable_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1))
if mibBuilder.loadTexts:oacAtmChannelTable.setStatus(_A)
_OacAtmChannelEntry_Object=MibTableRow
oacAtmChannelEntry=_OacAtmChannelEntry_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1))
oacAtmChannelEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oacAtmChannelEntry.setStatus(_A)
_OacAtmChanVpi_Type=AtmVpIdentifier
_OacAtmChanVpi_Object=MibTableColumn
oacAtmChanVpi=_OacAtmChanVpi_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,1),_OacAtmChanVpi_Type())
oacAtmChanVpi.setMaxAccess(_H)
if mibBuilder.loadTexts:oacAtmChanVpi.setStatus(_A)
_OacAtmChanVci_Type=AtmVcIdentifier
_OacAtmChanVci_Object=MibTableColumn
oacAtmChanVci=_OacAtmChanVci_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,2),_OacAtmChanVci_Type())
oacAtmChanVci.setMaxAccess(_H)
if mibBuilder.loadTexts:oacAtmChanVci.setStatus(_A)
_OacAtmChanTxBytes_Type=Counter32
_OacAtmChanTxBytes_Object=MibTableColumn
oacAtmChanTxBytes=_OacAtmChanTxBytes_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,3),_OacAtmChanTxBytes_Type())
oacAtmChanTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmChanTxBytes.setStatus(_A)
_OacAtmChanTxCells_Type=Counter32
_OacAtmChanTxCells_Object=MibTableColumn
oacAtmChanTxCells=_OacAtmChanTxCells_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,4),_OacAtmChanTxCells_Type())
oacAtmChanTxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmChanTxCells.setStatus(_A)
_OacAtmChanRxBytes_Type=Counter32
_OacAtmChanRxBytes_Object=MibTableColumn
oacAtmChanRxBytes=_OacAtmChanRxBytes_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,5),_OacAtmChanRxBytes_Type())
oacAtmChanRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmChanRxBytes.setStatus(_A)
_OacAtmChanRxCells_Type=Counter32
_OacAtmChanRxCells_Object=MibTableColumn
oacAtmChanRxCells=_OacAtmChanRxCells_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,6),_OacAtmChanRxCells_Type())
oacAtmChanRxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmChanRxCells.setStatus(_A)
_OacAtmChanRxErrors_Type=Counter32
_OacAtmChanRxErrors_Object=MibTableColumn
oacAtmChanRxErrors=_OacAtmChanRxErrors_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,7),_OacAtmChanRxErrors_Type())
oacAtmChanRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmChanRxErrors.setStatus(_A)
_OacAtmChanTxOverflows_Type=Counter32
_OacAtmChanTxOverflows_Object=MibTableColumn
oacAtmChanTxOverflows=_OacAtmChanTxOverflows_Object((1,3,6,1,4,1,13191,10,3,2,1,1,1,1,8),_OacAtmChanTxOverflows_Type())
oacAtmChanTxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmChanTxOverflows.setStatus(_A)
_OacAtmAal0ChannelGlobalStatTable_Object=MibTable
oacAtmAal0ChannelGlobalStatTable=_OacAtmAal0ChannelGlobalStatTable_Object((1,3,6,1,4,1,13191,10,3,2,1,1,2))
if mibBuilder.loadTexts:oacAtmAal0ChannelGlobalStatTable.setStatus(_A)
_OacAtmAal0ChannelGlobalStatEntry_Object=MibTableRow
oacAtmAal0ChannelGlobalStatEntry=_OacAtmAal0ChannelGlobalStatEntry_Object((1,3,6,1,4,1,13191,10,3,2,1,1,2,1))
oacAtmAal0ChannelGlobalStatEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oacAtmAal0ChannelGlobalStatEntry.setStatus(_A)
_OacAtmAal0ChanRxCellsDiscarded_Type=Counter32
_OacAtmAal0ChanRxCellsDiscarded_Object=MibTableColumn
oacAtmAal0ChanRxCellsDiscarded=_OacAtmAal0ChanRxCellsDiscarded_Object((1,3,6,1,4,1,13191,10,3,2,1,1,2,1,1),_OacAtmAal0ChanRxCellsDiscarded_Type())
oacAtmAal0ChanRxCellsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal0ChanRxCellsDiscarded.setStatus(_A)
_OacAtmAal1ChannelGlobalStatTable_Object=MibTable
oacAtmAal1ChannelGlobalStatTable=_OacAtmAal1ChannelGlobalStatTable_Object((1,3,6,1,4,1,13191,10,3,2,1,1,3))
if mibBuilder.loadTexts:oacAtmAal1ChannelGlobalStatTable.setStatus(_A)
_OacAtmAal1ChannelGlobalStatEntry_Object=MibTableRow
oacAtmAal1ChannelGlobalStatEntry=_OacAtmAal1ChannelGlobalStatEntry_Object((1,3,6,1,4,1,13191,10,3,2,1,1,3,1))
oacAtmAal1ChannelGlobalStatEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oacAtmAal1ChannelGlobalStatEntry.setStatus(_A)
_OacAtmAal1ChanTxUnderflows_Type=Counter32
_OacAtmAal1ChanTxUnderflows_Object=MibTableColumn
oacAtmAal1ChanTxUnderflows=_OacAtmAal1ChanTxUnderflows_Object((1,3,6,1,4,1,13191,10,3,2,1,1,3,1,1),_OacAtmAal1ChanTxUnderflows_Type())
oacAtmAal1ChanTxUnderflows.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal1ChanTxUnderflows.setStatus(_A)
_OacAtmAal1ChanRxOverflows_Type=Counter32
_OacAtmAal1ChanRxOverflows_Object=MibTableColumn
oacAtmAal1ChanRxOverflows=_OacAtmAal1ChanRxOverflows_Object((1,3,6,1,4,1,13191,10,3,2,1,1,3,1,2),_OacAtmAal1ChanRxOverflows_Type())
oacAtmAal1ChanRxOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal1ChanRxOverflows.setStatus(_A)
_OacAtmAal5ChannelGlobalStatTable_Object=MibTable
oacAtmAal5ChannelGlobalStatTable=_OacAtmAal5ChannelGlobalStatTable_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4))
if mibBuilder.loadTexts:oacAtmAal5ChannelGlobalStatTable.setStatus(_A)
_OacAtmAal5ChannelGlobalStatEntry_Object=MibTableRow
oacAtmAal5ChannelGlobalStatEntry=_OacAtmAal5ChannelGlobalStatEntry_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1))
oacAtmAal5ChannelGlobalStatEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oacAtmAal5ChannelGlobalStatEntry.setStatus(_A)
_OacAtmAal5ChanTxFrames_Type=Counter32
_OacAtmAal5ChanTxFrames_Object=MibTableColumn
oacAtmAal5ChanTxFrames=_OacAtmAal5ChanTxFrames_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1,1),_OacAtmAal5ChanTxFrames_Type())
oacAtmAal5ChanTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5ChanTxFrames.setStatus(_A)
_OacAtmAal5ChanRxFrames_Type=Counter32
_OacAtmAal5ChanRxFrames_Object=MibTableColumn
oacAtmAal5ChanRxFrames=_OacAtmAal5ChanRxFrames_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1,2),_OacAtmAal5ChanRxFrames_Type())
oacAtmAal5ChanRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5ChanRxFrames.setStatus(_A)
_OacAtmAal5ChanRxFramesDiscarded_Type=Counter32
_OacAtmAal5ChanRxFramesDiscarded_Object=MibTableColumn
oacAtmAal5ChanRxFramesDiscarded=_OacAtmAal5ChanRxFramesDiscarded_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1,3),_OacAtmAal5ChanRxFramesDiscarded_Type())
oacAtmAal5ChanRxFramesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5ChanRxFramesDiscarded.setStatus(_A)
_OacAtmAal5ChanCrc32Errors_Type=Counter32
_OacAtmAal5ChanCrc32Errors_Object=MibTableColumn
oacAtmAal5ChanCrc32Errors=_OacAtmAal5ChanCrc32Errors_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1,4),_OacAtmAal5ChanCrc32Errors_Type())
oacAtmAal5ChanCrc32Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5ChanCrc32Errors.setStatus(_A)
_OacAtmAal5ChanLengthErrors_Type=Counter32
_OacAtmAal5ChanLengthErrors_Object=MibTableColumn
oacAtmAal5ChanLengthErrors=_OacAtmAal5ChanLengthErrors_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1,5),_OacAtmAal5ChanLengthErrors_Type())
oacAtmAal5ChanLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5ChanLengthErrors.setStatus(_A)
_OacAtmAal5ChanReassemblyTimeouts_Type=Counter32
_OacAtmAal5ChanReassemblyTimeouts_Object=MibTableColumn
oacAtmAal5ChanReassemblyTimeouts=_OacAtmAal5ChanReassemblyTimeouts_Object((1,3,6,1,4,1,13191,10,3,2,1,1,4,1,6),_OacAtmAal5ChanReassemblyTimeouts_Type())
oacAtmAal5ChanReassemblyTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5ChanReassemblyTimeouts.setStatus(_A)
_OacAtmPortStatTable_Object=MibTable
oacAtmPortStatTable=_OacAtmPortStatTable_Object((1,3,6,1,4,1,13191,10,3,2,1,1,5))
if mibBuilder.loadTexts:oacAtmPortStatTable.setStatus(_A)
_OacAtmPortStatEntry_Object=MibTableRow
oacAtmPortStatEntry=_OacAtmPortStatEntry_Object((1,3,6,1,4,1,13191,10,3,2,1,1,5,1))
oacAtmPortStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oacAtmPortStatEntry.setStatus(_A)
_OacAtmPortTxCells_Type=Counter32
_OacAtmPortTxCells_Object=MibTableColumn
oacAtmPortTxCells=_OacAtmPortTxCells_Object((1,3,6,1,4,1,13191,10,3,2,1,1,5,1,1),_OacAtmPortTxCells_Type())
oacAtmPortTxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmPortTxCells.setStatus(_A)
_OacAtmPortRxCells_Type=Counter32
_OacAtmPortRxCells_Object=MibTableColumn
oacAtmPortRxCells=_OacAtmPortRxCells_Object((1,3,6,1,4,1,13191,10,3,2,1,1,5,1,2),_OacAtmPortRxCells_Type())
oacAtmPortRxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmPortRxCells.setStatus(_A)
_OacAtmPortRxCellsDiscarded_Type=Counter32
_OacAtmPortRxCellsDiscarded_Object=MibTableColumn
oacAtmPortRxCellsDiscarded=_OacAtmPortRxCellsDiscarded_Object((1,3,6,1,4,1,13191,10,3,2,1,1,5,1,3),_OacAtmPortRxCellsDiscarded_Type())
oacAtmPortRxCellsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmPortRxCellsDiscarded.setStatus(_A)
_OacAtmPortHecErrors_Type=Counter32
_OacAtmPortHecErrors_Object=MibTableColumn
oacAtmPortHecErrors=_OacAtmPortHecErrors_Object((1,3,6,1,4,1,13191,10,3,2,1,1,5,1,4),_OacAtmPortHecErrors_Type())
oacAtmPortHecErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmPortHecErrors.setStatus(_A)
_OacAtmAal5PortStatTable_Object=MibTable
oacAtmAal5PortStatTable=_OacAtmAal5PortStatTable_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6))
if mibBuilder.loadTexts:oacAtmAal5PortStatTable.setStatus(_A)
_OacAtmAal5PortStatEntry_Object=MibTableRow
oacAtmAal5PortStatEntry=_OacAtmAal5PortStatEntry_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1))
oacAtmAal5PortStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oacAtmAal5PortStatEntry.setStatus(_A)
_OacAtmAal5PortTxBytes_Type=Counter32
_OacAtmAal5PortTxBytes_Object=MibTableColumn
oacAtmAal5PortTxBytes=_OacAtmAal5PortTxBytes_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,1),_OacAtmAal5PortTxBytes_Type())
oacAtmAal5PortTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortTxBytes.setStatus(_A)
_OacAtmAal5PortTxFrames_Type=Counter32
_OacAtmAal5PortTxFrames_Object=MibTableColumn
oacAtmAal5PortTxFrames=_OacAtmAal5PortTxFrames_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,2),_OacAtmAal5PortTxFrames_Type())
oacAtmAal5PortTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortTxFrames.setStatus(_A)
_OacAtmAal5PortTxFramesDiscarded_Type=Counter32
_OacAtmAal5PortTxFramesDiscarded_Object=MibTableColumn
oacAtmAal5PortTxFramesDiscarded=_OacAtmAal5PortTxFramesDiscarded_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,3),_OacAtmAal5PortTxFramesDiscarded_Type())
oacAtmAal5PortTxFramesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortTxFramesDiscarded.setStatus(_A)
_OacAtmAal5PortRxBytes_Type=Counter32
_OacAtmAal5PortRxBytes_Object=MibTableColumn
oacAtmAal5PortRxBytes=_OacAtmAal5PortRxBytes_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,4),_OacAtmAal5PortRxBytes_Type())
oacAtmAal5PortRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortRxBytes.setStatus(_A)
_OacAtmAal5PortRxFrames_Type=Counter32
_OacAtmAal5PortRxFrames_Object=MibTableColumn
oacAtmAal5PortRxFrames=_OacAtmAal5PortRxFrames_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,5),_OacAtmAal5PortRxFrames_Type())
oacAtmAal5PortRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortRxFrames.setStatus(_A)
_OacAtmAal5PortRxErrors_Type=Counter32
_OacAtmAal5PortRxErrors_Object=MibTableColumn
oacAtmAal5PortRxErrors=_OacAtmAal5PortRxErrors_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,6),_OacAtmAal5PortRxErrors_Type())
oacAtmAal5PortRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortRxErrors.setStatus(_A)
_OacAtmAal5PortRxFramesDiscarded_Type=Counter32
_OacAtmAal5PortRxFramesDiscarded_Object=MibTableColumn
oacAtmAal5PortRxFramesDiscarded=_OacAtmAal5PortRxFramesDiscarded_Object((1,3,6,1,4,1,13191,10,3,2,1,1,6,1,7),_OacAtmAal5PortRxFramesDiscarded_Type())
oacAtmAal5PortRxFramesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmAal5PortRxFramesDiscarded.setStatus(_A)
_OacAtmStatNotifications_ObjectIdentity=ObjectIdentity
oacAtmStatNotifications=_OacAtmStatNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,1,2))
_OacAtmStatConformance_ObjectIdentity=ObjectIdentity
oacAtmStatConformance=_OacAtmStatConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,1,3))
_OacAtmStatGroups_ObjectIdentity=ObjectIdentity
oacAtmStatGroups=_OacAtmStatGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,1,3,1))
_OacAtmStatCompliances_ObjectIdentity=ObjectIdentity
oacAtmStatCompliances=_OacAtmStatCompliances_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,1,3,2))
oacAtmStatGeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,2,1,3,1,1))
oacAtmStatGeneralGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:oacAtmStatGeneralGroup.setStatus(_A)
oacAtmStatCompliance=ModuleCompliance((1,3,6,1,4,1,13191,10,3,2,1,3,2,1))
oacAtmStatCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:oacAtmStatCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oacAtmMIBModule':oacAtmMIBModule,'oacAtmStatObjects':oacAtmStatObjects,'oacAtmChannelTable':oacAtmChannelTable,'oacAtmChannelEntry':oacAtmChannelEntry,_F:oacAtmChanVpi,_G:oacAtmChanVci,_I:oacAtmChanTxBytes,_J:oacAtmChanTxCells,_K:oacAtmChanRxBytes,_L:oacAtmChanRxCells,_M:oacAtmChanRxErrors,_N:oacAtmChanTxOverflows,'oacAtmAal0ChannelGlobalStatTable':oacAtmAal0ChannelGlobalStatTable,'oacAtmAal0ChannelGlobalStatEntry':oacAtmAal0ChannelGlobalStatEntry,_O:oacAtmAal0ChanRxCellsDiscarded,'oacAtmAal1ChannelGlobalStatTable':oacAtmAal1ChannelGlobalStatTable,'oacAtmAal1ChannelGlobalStatEntry':oacAtmAal1ChannelGlobalStatEntry,_P:oacAtmAal1ChanTxUnderflows,_Q:oacAtmAal1ChanRxOverflows,'oacAtmAal5ChannelGlobalStatTable':oacAtmAal5ChannelGlobalStatTable,'oacAtmAal5ChannelGlobalStatEntry':oacAtmAal5ChannelGlobalStatEntry,_R:oacAtmAal5ChanTxFrames,_S:oacAtmAal5ChanRxFrames,_T:oacAtmAal5ChanRxFramesDiscarded,_U:oacAtmAal5ChanCrc32Errors,_V:oacAtmAal5ChanLengthErrors,_W:oacAtmAal5ChanReassemblyTimeouts,'oacAtmPortStatTable':oacAtmPortStatTable,'oacAtmPortStatEntry':oacAtmPortStatEntry,_X:oacAtmPortTxCells,_Y:oacAtmPortRxCells,_Z:oacAtmPortRxCellsDiscarded,_a:oacAtmPortHecErrors,'oacAtmAal5PortStatTable':oacAtmAal5PortStatTable,'oacAtmAal5PortStatEntry':oacAtmAal5PortStatEntry,_b:oacAtmAal5PortTxBytes,_c:oacAtmAal5PortTxFrames,_d:oacAtmAal5PortTxFramesDiscarded,_e:oacAtmAal5PortRxBytes,_f:oacAtmAal5PortRxFrames,_g:oacAtmAal5PortRxErrors,_h:oacAtmAal5PortRxFramesDiscarded,'oacAtmStatNotifications':oacAtmStatNotifications,'oacAtmStatConformance':oacAtmStatConformance,'oacAtmStatGroups':oacAtmStatGroups,_i:oacAtmStatGeneralGroup,'oacAtmStatCompliances':oacAtmStatCompliances,'oacAtmStatCompliance':oacAtmStatCompliance})