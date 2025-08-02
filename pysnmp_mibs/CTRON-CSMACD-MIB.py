_K='ctFnbPortConnectPortIndex'
_J='ctFnbPortConnectBoardIndex'
_I='connectA'
_H='connectC'
_G='connectB'
_F='ctFnbCSMACDIndex'
_E='read-write'
_D='Integer32'
_C='CTRON-CSMACD-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctCSMACD,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctCSMACD')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFnbCSMACD_ObjectIdentity=ObjectIdentity
ctFnbCSMACD=_CtFnbCSMACD_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,4,1,1))
_CtFnbCSMACDTable_Object=MibTable
ctFnbCSMACDTable=_CtFnbCSMACDTable_Object((1,3,6,1,4,1,52,4,1,2,4,1,1,1))
if mibBuilder.loadTexts:ctFnbCSMACDTable.setStatus(_A)
_CtFnbCSMACDEntry_Object=MibTableRow
ctFnbCSMACDEntry=_CtFnbCSMACDEntry_Object((1,3,6,1,4,1,52,4,1,2,4,1,1,1,1))
ctFnbCSMACDEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:ctFnbCSMACDEntry.setStatus(_A)
_CtFnbCSMACDIndex_Type=Integer32
_CtFnbCSMACDIndex_Object=MibTableColumn
ctFnbCSMACDIndex=_CtFnbCSMACDIndex_Object((1,3,6,1,4,1,52,4,1,2,4,1,1,1,1,1),_CtFnbCSMACDIndex_Type())
ctFnbCSMACDIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFnbCSMACDIndex.setStatus(_A)
class _CtFnbConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),(_H,2),('disconnect',3),(_I,4),('subnetB',5),('subnetC',6),('multiChannel',7),('frontpanel',8)))
_CtFnbConnect_Type.__name__=_D
_CtFnbConnect_Object=MibTableColumn
ctFnbConnect=_CtFnbConnect_Object((1,3,6,1,4,1,52,4,1,2,4,1,1,1,1,2),_CtFnbConnect_Type())
ctFnbConnect.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFnbConnect.setStatus(_A)
_CtFnbPortChanges_Type=Counter32
_CtFnbPortChanges_Object=MibTableColumn
ctFnbPortChanges=_CtFnbPortChanges_Object((1,3,6,1,4,1,52,4,1,2,4,1,1,1,1,3),_CtFnbPortChanges_Type())
ctFnbPortChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFnbPortChanges.setStatus(_A)
_CtFnbPortConnect_ObjectIdentity=ObjectIdentity
ctFnbPortConnect=_CtFnbPortConnect_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,4,1,2))
_CtFnbPortConnectTable_Object=MibTable
ctFnbPortConnectTable=_CtFnbPortConnectTable_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,1))
if mibBuilder.loadTexts:ctFnbPortConnectTable.setStatus(_A)
_CtFnbPortConnectEntry_Object=MibTableRow
ctFnbPortConnectEntry=_CtFnbPortConnectEntry_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,1,1))
ctFnbPortConnectEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:ctFnbPortConnectEntry.setStatus(_A)
_CtFnbPortConnectBoardIndex_Type=Integer32
_CtFnbPortConnectBoardIndex_Object=MibTableColumn
ctFnbPortConnectBoardIndex=_CtFnbPortConnectBoardIndex_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,1,1,1),_CtFnbPortConnectBoardIndex_Type())
ctFnbPortConnectBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFnbPortConnectBoardIndex.setStatus(_A)
_CtFnbPortConnectPortIndex_Type=Integer32
_CtFnbPortConnectPortIndex_Object=MibTableColumn
ctFnbPortConnectPortIndex=_CtFnbPortConnectPortIndex_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,1,1,2),_CtFnbPortConnectPortIndex_Type())
ctFnbPortConnectPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFnbPortConnectPortIndex.setStatus(_A)
class _CtFnbPortConnectPortAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_CtFnbPortConnectPortAssignment_Type.__name__=_D
_CtFnbPortConnectPortAssignment_Object=MibTableColumn
ctFnbPortConnectPortAssignment=_CtFnbPortConnectPortAssignment_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,1,1,3),_CtFnbPortConnectPortAssignment_Type())
ctFnbPortConnectPortAssignment.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFnbPortConnectPortAssignment.setStatus(_A)
_CtFnbPortCompID_Type=Integer32
_CtFnbPortCompID_Object=MibTableColumn
ctFnbPortCompID=_CtFnbPortCompID_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,1,1,4),_CtFnbPortCompID_Type())
ctFnbPortCompID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFnbPortCompID.setStatus(_A)
_CtFnbPortConnectionChanges_Type=Counter32
_CtFnbPortConnectionChanges_Object=MibScalar
ctFnbPortConnectionChanges=_CtFnbPortConnectionChanges_Object((1,3,6,1,4,1,52,4,1,2,4,1,2,2),_CtFnbPortConnectionChanges_Type())
ctFnbPortConnectionChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFnbPortConnectionChanges.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctFnbCSMACD':ctFnbCSMACD,'ctFnbCSMACDTable':ctFnbCSMACDTable,'ctFnbCSMACDEntry':ctFnbCSMACDEntry,_F:ctFnbCSMACDIndex,'ctFnbConnect':ctFnbConnect,'ctFnbPortChanges':ctFnbPortChanges,'ctFnbPortConnect':ctFnbPortConnect,'ctFnbPortConnectTable':ctFnbPortConnectTable,'ctFnbPortConnectEntry':ctFnbPortConnectEntry,_J:ctFnbPortConnectBoardIndex,_K:ctFnbPortConnectPortIndex,'ctFnbPortConnectPortAssignment':ctFnbPortConnectPortAssignment,'ctFnbPortCompID':ctFnbPortCompID,'ctFnbPortConnectionChanges':ctFnbPortConnectionChanges})