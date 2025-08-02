_K='inbStatsINB'
_J='inbStatsSlot'
_I='inbMonarchSlot'
_H='read-write'
_G='inbB'
_F='inbA'
_E='inbMonarchINB'
_D='CTINB-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctINBinfo,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctINBinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_InbMonarchSystem_ObjectIdentity=ObjectIdentity
inbMonarchSystem=_InbMonarchSystem_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,12,1,1))
_InbMonarchSystemTable_Object=MibTable
inbMonarchSystemTable=_InbMonarchSystemTable_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1))
if mibBuilder.loadTexts:inbMonarchSystemTable.setStatus(_A)
_InbMonarchSystemEntry_Object=MibTableRow
inbMonarchSystemEntry=_InbMonarchSystemEntry_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1))
inbMonarchSystemEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:inbMonarchSystemEntry.setStatus(_A)
class _InbMonarchSystemINB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_InbMonarchSystemINB_Type.__name__=_C
_InbMonarchSystemINB_Object=MibTableColumn
inbMonarchSystemINB=_InbMonarchSystemINB_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,1),_InbMonarchSystemINB_Type())
inbMonarchSystemINB.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchSystemINB.setStatus(_A)
_InbMonarchStatusTimeStamp_Type=TimeTicks
_InbMonarchStatusTimeStamp_Object=MibTableColumn
inbMonarchStatusTimeStamp=_InbMonarchStatusTimeStamp_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,2),_InbMonarchStatusTimeStamp_Type())
inbMonarchStatusTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchStatusTimeStamp.setStatus(_A)
_InbMonarchBandwidth_Type=Integer32
_InbMonarchBandwidth_Object=MibTableColumn
inbMonarchBandwidth=_InbMonarchBandwidth_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,3),_InbMonarchBandwidth_Type())
inbMonarchBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchBandwidth.setStatus(_A)
class _InbMonarchTDMSlotMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('userPolicy',2)))
_InbMonarchTDMSlotMode_Type.__name__=_C
_InbMonarchTDMSlotMode_Object=MibTableColumn
inbMonarchTDMSlotMode=_InbMonarchTDMSlotMode_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,4),_InbMonarchTDMSlotMode_Type())
inbMonarchTDMSlotMode.setMaxAccess(_H)
if mibBuilder.loadTexts:inbMonarchTDMSlotMode.setStatus(_A)
_InbMonarchTDMSlotTotal_Type=Integer32
_InbMonarchTDMSlotTotal_Object=MibTableColumn
inbMonarchTDMSlotTotal=_InbMonarchTDMSlotTotal_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,5),_InbMonarchTDMSlotTotal_Type())
inbMonarchTDMSlotTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchTDMSlotTotal.setStatus(_A)
_InbMonarchSystemTDMSlotActual_Type=Integer32
_InbMonarchSystemTDMSlotActual_Object=MibTableColumn
inbMonarchSystemTDMSlotActual=_InbMonarchSystemTDMSlotActual_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,6),_InbMonarchSystemTDMSlotActual_Type())
inbMonarchSystemTDMSlotActual.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchSystemTDMSlotActual.setStatus(_A)
_InbMonarchTDMSlotbandwidth_Type=Integer32
_InbMonarchTDMSlotbandwidth_Object=MibTableColumn
inbMonarchTDMSlotbandwidth=_InbMonarchTDMSlotbandwidth_Object((1,3,6,1,4,1,52,4,1,2,12,1,1,1,1,7),_InbMonarchTDMSlotbandwidth_Type())
inbMonarchTDMSlotbandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchTDMSlotbandwidth.setStatus(_A)
_InbMonarch_ObjectIdentity=ObjectIdentity
inbMonarch=_InbMonarch_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,12,1,2))
_InbMonarchTable_Object=MibTable
inbMonarchTable=_InbMonarchTable_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1))
if mibBuilder.loadTexts:inbMonarchTable.setStatus(_A)
_InbMonarchEntry_Object=MibTableRow
inbMonarchEntry=_InbMonarchEntry_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1))
inbMonarchEntry.setIndexNames((0,_D,_I),(0,_D,_E))
if mibBuilder.loadTexts:inbMonarchEntry.setStatus(_A)
_InbMonarchSlot_Type=Integer32
_InbMonarchSlot_Object=MibTableColumn
inbMonarchSlot=_InbMonarchSlot_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,1),_InbMonarchSlot_Type())
inbMonarchSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchSlot.setStatus(_A)
class _InbMonarchINB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_InbMonarchINB_Type.__name__=_C
_InbMonarchINB_Object=MibTableColumn
inbMonarchINB=_InbMonarchINB_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,2),_InbMonarchINB_Type())
inbMonarchINB.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchINB.setStatus(_A)
class _InbMonarchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standBy',1),('sysUndefined',2),('operational',3)))
_InbMonarchStatus_Type.__name__=_C
_InbMonarchStatus_Object=MibTableColumn
inbMonarchStatus=_InbMonarchStatus_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,3),_InbMonarchStatus_Type())
inbMonarchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchStatus.setStatus(_A)
class _InbMonarchLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkUp',1),('linkDown',2)))
_InbMonarchLinkStatus_Type.__name__=_C
_InbMonarchLinkStatus_Object=MibTableColumn
inbMonarchLinkStatus=_InbMonarchLinkStatus_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,4),_InbMonarchLinkStatus_Type())
inbMonarchLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchLinkStatus.setStatus(_A)
_InbMonarchLinkCapacity_Type=Integer32
_InbMonarchLinkCapacity_Object=MibTableColumn
inbMonarchLinkCapacity=_InbMonarchLinkCapacity_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,5),_InbMonarchLinkCapacity_Type())
inbMonarchLinkCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchLinkCapacity.setStatus(_A)
_InbMonarchTDMSlotRequest_Type=Integer32
_InbMonarchTDMSlotRequest_Object=MibTableColumn
inbMonarchTDMSlotRequest=_InbMonarchTDMSlotRequest_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,6),_InbMonarchTDMSlotRequest_Type())
inbMonarchTDMSlotRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:inbMonarchTDMSlotRequest.setStatus(_A)
_InbMonarchTDMSlotActual_Type=Integer32
_InbMonarchTDMSlotActual_Object=MibTableColumn
inbMonarchTDMSlotActual=_InbMonarchTDMSlotActual_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,7),_InbMonarchTDMSlotActual_Type())
inbMonarchTDMSlotActual.setMaxAccess(_H)
if mibBuilder.loadTexts:inbMonarchTDMSlotActual.setStatus(_A)
class _InbMonarchRoundRobinControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_InbMonarchRoundRobinControl_Type.__name__=_C
_InbMonarchRoundRobinControl_Object=MibTableColumn
inbMonarchRoundRobinControl=_InbMonarchRoundRobinControl_Object((1,3,6,1,4,1,52,4,1,2,12,1,2,1,1,8),_InbMonarchRoundRobinControl_Type())
inbMonarchRoundRobinControl.setMaxAccess(_B)
if mibBuilder.loadTexts:inbMonarchRoundRobinControl.setStatus(_A)
_InbStats_ObjectIdentity=ObjectIdentity
inbStats=_InbStats_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,12,1,3))
_InbStatsTable_Object=MibTable
inbStatsTable=_InbStatsTable_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1))
if mibBuilder.loadTexts:inbStatsTable.setStatus(_A)
_InbStatsEntry_Object=MibTableRow
inbStatsEntry=_InbStatsEntry_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1))
inbStatsEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:inbStatsEntry.setStatus(_A)
_InbStatsSlot_Type=Integer32
_InbStatsSlot_Object=MibTableColumn
inbStatsSlot=_InbStatsSlot_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,1),_InbStatsSlot_Type())
inbStatsSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsSlot.setStatus(_A)
class _InbStatsINB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_InbStatsINB_Type.__name__=_C
_InbStatsINB_Object=MibTableColumn
inbStatsINB=_InbStatsINB_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,2),_InbStatsINB_Type())
inbStatsINB.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsINB.setStatus(_A)
_InbStatsIfindex_Type=Integer32
_InbStatsIfindex_Object=MibTableColumn
inbStatsIfindex=_InbStatsIfindex_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,3),_InbStatsIfindex_Type())
inbStatsIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsIfindex.setStatus(_A)
_InbStatsUniCastCells_Type=Counter32
_InbStatsUniCastCells_Object=MibTableColumn
inbStatsUniCastCells=_InbStatsUniCastCells_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,4),_InbStatsUniCastCells_Type())
inbStatsUniCastCells.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsUniCastCells.setStatus(_A)
_InbStatsMultiCastCells_Type=Counter32
_InbStatsMultiCastCells_Object=MibTableColumn
inbStatsMultiCastCells=_InbStatsMultiCastCells_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,5),_InbStatsMultiCastCells_Type())
inbStatsMultiCastCells.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsMultiCastCells.setStatus(_A)
_InbStatsBroadCastCells_Type=Counter32
_InbStatsBroadCastCells_Object=MibTableColumn
inbStatsBroadCastCells=_InbStatsBroadCastCells_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,6),_InbStatsBroadCastCells_Type())
inbStatsBroadCastCells.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsBroadCastCells.setStatus(_A)
_InbStatsXmitCells_Type=Counter32
_InbStatsXmitCells_Object=MibTableColumn
inbStatsXmitCells=_InbStatsXmitCells_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,7),_InbStatsXmitCells_Type())
inbStatsXmitCells.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsXmitCells.setStatus(_A)
_InbStatsRecvSeqErrs_Type=Counter32
_InbStatsRecvSeqErrs_Object=MibTableColumn
inbStatsRecvSeqErrs=_InbStatsRecvSeqErrs_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,8),_InbStatsRecvSeqErrs_Type())
inbStatsRecvSeqErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsRecvSeqErrs.setStatus(_A)
_InbStatsRecvChksumErrs_Type=Counter32
_InbStatsRecvChksumErrs_Object=MibTableColumn
inbStatsRecvChksumErrs=_InbStatsRecvChksumErrs_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,9),_InbStatsRecvChksumErrs_Type())
inbStatsRecvChksumErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsRecvChksumErrs.setStatus(_A)
_InbStatsxmitToFps_Type=Counter32
_InbStatsxmitToFps_Object=MibTableColumn
inbStatsxmitToFps=_InbStatsxmitToFps_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,10),_InbStatsxmitToFps_Type())
inbStatsxmitToFps.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsxmitToFps.setStatus(_A)
_InbStatsToFpsDrops_Type=Counter32
_InbStatsToFpsDrops_Object=MibTableColumn
inbStatsToFpsDrops=_InbStatsToFpsDrops_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,11),_InbStatsToFpsDrops_Type())
inbStatsToFpsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsToFpsDrops.setStatus(_A)
_InbStatsFromInbErrs_Type=Counter32
_InbStatsFromInbErrs_Object=MibTableColumn
inbStatsFromInbErrs=_InbStatsFromInbErrs_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,12),_InbStatsFromInbErrs_Type())
inbStatsFromInbErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsFromInbErrs.setStatus(_A)
_InbStatsToINBDrops_Type=Counter32
_InbStatsToINBDrops_Object=MibTableColumn
inbStatsToINBDrops=_InbStatsToINBDrops_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,13),_InbStatsToINBDrops_Type())
inbStatsToINBDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsToINBDrops.setStatus(_A)
_InbStatsToInbErrs_Type=Counter32
_InbStatsToInbErrs_Object=MibTableColumn
inbStatsToInbErrs=_InbStatsToInbErrs_Object((1,3,6,1,4,1,52,4,1,2,12,1,3,1,1,14),_InbStatsToInbErrs_Type())
inbStatsToInbErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:inbStatsToInbErrs.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'inbMonarchSystem':inbMonarchSystem,'inbMonarchSystemTable':inbMonarchSystemTable,'inbMonarchSystemEntry':inbMonarchSystemEntry,'inbMonarchSystemINB':inbMonarchSystemINB,'inbMonarchStatusTimeStamp':inbMonarchStatusTimeStamp,'inbMonarchBandwidth':inbMonarchBandwidth,'inbMonarchTDMSlotMode':inbMonarchTDMSlotMode,'inbMonarchTDMSlotTotal':inbMonarchTDMSlotTotal,'inbMonarchSystemTDMSlotActual':inbMonarchSystemTDMSlotActual,'inbMonarchTDMSlotbandwidth':inbMonarchTDMSlotbandwidth,'inbMonarch':inbMonarch,'inbMonarchTable':inbMonarchTable,'inbMonarchEntry':inbMonarchEntry,_I:inbMonarchSlot,_E:inbMonarchINB,'inbMonarchStatus':inbMonarchStatus,'inbMonarchLinkStatus':inbMonarchLinkStatus,'inbMonarchLinkCapacity':inbMonarchLinkCapacity,'inbMonarchTDMSlotRequest':inbMonarchTDMSlotRequest,'inbMonarchTDMSlotActual':inbMonarchTDMSlotActual,'inbMonarchRoundRobinControl':inbMonarchRoundRobinControl,'inbStats':inbStats,'inbStatsTable':inbStatsTable,'inbStatsEntry':inbStatsEntry,_J:inbStatsSlot,_K:inbStatsINB,'inbStatsIfindex':inbStatsIfindex,'inbStatsUniCastCells':inbStatsUniCastCells,'inbStatsMultiCastCells':inbStatsMultiCastCells,'inbStatsBroadCastCells':inbStatsBroadCastCells,'inbStatsXmitCells':inbStatsXmitCells,'inbStatsRecvSeqErrs':inbStatsRecvSeqErrs,'inbStatsRecvChksumErrs':inbStatsRecvChksumErrs,'inbStatsxmitToFps':inbStatsxmitToFps,'inbStatsToFpsDrops':inbStatsToFpsDrops,'inbStatsFromInbErrs':inbStatsFromInbErrs,'inbStatsToINBDrops':inbStatsToINBDrops,'inbStatsToInbErrs':inbStatsToInbErrs})