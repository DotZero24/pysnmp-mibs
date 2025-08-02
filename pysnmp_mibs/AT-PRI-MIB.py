_G='priChanChannelIndex'
_F='priChanIntIndex'
_E='priIntIndex'
_D='AT-PRI-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
pri=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,42))
if mibBuilder.loadTexts:pri.setRevisions(('2006-06-28 12:22',))
_PriIntTable_Object=MibTable
priIntTable=_PriIntTable_Object((1,3,6,1,4,1,207,8,4,4,4,42,1))
if mibBuilder.loadTexts:priIntTable.setStatus(_A)
_PriIntEntry_Object=MibTableRow
priIntEntry=_PriIntEntry_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1))
priIntEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:priIntEntry.setStatus(_A)
_PriIntIndex_Type=Integer32
_PriIntIndex_Object=MibTableColumn
priIntIndex=_PriIntIndex_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,1),_PriIntIndex_Type())
priIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntIndex.setStatus(_A)
_PriIntBoardIndex_Type=Integer32
_PriIntBoardIndex_Object=MibTableColumn
priIntBoardIndex=_PriIntBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,2),_PriIntBoardIndex_Type())
priIntBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntBoardIndex.setStatus(_A)
_PriIntBoardPosition_Type=Integer32
_PriIntBoardPosition_Object=MibTableColumn
priIntBoardPosition=_PriIntBoardPosition_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,3),_PriIntBoardPosition_Type())
priIntBoardPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntBoardPosition.setStatus(_A)
class _PriIntMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('isdn',1),('tdm',2),('mixed',3)))
_PriIntMode_Type.__name__=_C
_PriIntMode_Object=MibTableColumn
priIntMode=_PriIntMode_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,4),_PriIntMode_Type())
priIntMode.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntMode.setStatus(_A)
_PriIntTdmChannelMap_Type=Integer32
_PriIntTdmChannelMap_Object=MibTableColumn
priIntTdmChannelMap=_PriIntTdmChannelMap_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,5),_PriIntTdmChannelMap_Type())
priIntTdmChannelMap.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntTdmChannelMap.setStatus(_A)
_PriIntIsdnChannelMap_Type=Integer32
_PriIntIsdnChannelMap_Object=MibTableColumn
priIntIsdnChannelMap=_PriIntIsdnChannelMap_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,6),_PriIntIsdnChannelMap_Type())
priIntIsdnChannelMap.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntIsdnChannelMap.setStatus(_A)
class _PriIntType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('e1',1),('t1',2),('unknown',3)))
_PriIntType_Type.__name__=_C
_PriIntType_Object=MibTableColumn
priIntType=_PriIntType_Object((1,3,6,1,4,1,207,8,4,4,4,42,1,1,7),_PriIntType_Type())
priIntType.setMaxAccess(_B)
if mibBuilder.loadTexts:priIntType.setStatus(_A)
_PriChanTable_Object=MibTable
priChanTable=_PriChanTable_Object((1,3,6,1,4,1,207,8,4,4,4,42,2))
if mibBuilder.loadTexts:priChanTable.setStatus(_A)
_PriChanEntry_Object=MibTableRow
priChanEntry=_PriChanEntry_Object((1,3,6,1,4,1,207,8,4,4,4,42,2,1))
priChanEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:priChanEntry.setStatus(_A)
_PriChanIntIndex_Type=Integer32
_PriChanIntIndex_Object=MibTableColumn
priChanIntIndex=_PriChanIntIndex_Object((1,3,6,1,4,1,207,8,4,4,4,42,2,1,1),_PriChanIntIndex_Type())
priChanIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:priChanIntIndex.setStatus(_A)
class _PriChanChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_PriChanChannelIndex_Type.__name__=_C
_PriChanChannelIndex_Object=MibTableColumn
priChanChannelIndex=_PriChanChannelIndex_Object((1,3,6,1,4,1,207,8,4,4,4,42,2,1,2),_PriChanChannelIndex_Type())
priChanChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:priChanChannelIndex.setStatus(_A)
class _PriChanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('isdn',1),('tdm',2),('neither',3)))
_PriChanMode_Type.__name__=_C
_PriChanMode_Object=MibTableColumn
priChanMode=_PriChanMode_Object((1,3,6,1,4,1,207,8,4,4,4,42,2,1,3),_PriChanMode_Type())
priChanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:priChanMode.setStatus(_A)
class _PriChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_PriChanState_Type.__name__=_C
_PriChanState_Object=MibTableColumn
priChanState=_PriChanState_Object((1,3,6,1,4,1,207,8,4,4,4,42,2,1,4),_PriChanState_Type())
priChanState.setMaxAccess(_B)
if mibBuilder.loadTexts:priChanState.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'pri':pri,'priIntTable':priIntTable,'priIntEntry':priIntEntry,_E:priIntIndex,'priIntBoardIndex':priIntBoardIndex,'priIntBoardPosition':priIntBoardPosition,'priIntMode':priIntMode,'priIntTdmChannelMap':priIntTdmChannelMap,'priIntIsdnChannelMap':priIntIsdnChannelMap,'priIntType':priIntType,'priChanTable':priChanTable,'priChanEntry':priChanEntry,_F:priChanIntIndex,_G:priChanChannelIndex,'priChanMode':priChanMode,'priChanState':priChanState})