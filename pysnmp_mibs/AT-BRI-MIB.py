_G='briChanChannelIndex'
_F='briChanIntIndex'
_E='briIntIndex'
_D='AT-BRI-MIB'
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
bri=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,41))
if mibBuilder.loadTexts:bri.setRevisions(('2006-06-28 12:22',))
_BriIntTable_Object=MibTable
briIntTable=_BriIntTable_Object((1,3,6,1,4,1,207,8,4,4,4,41,1))
if mibBuilder.loadTexts:briIntTable.setStatus(_A)
_BriIntEntry_Object=MibTableRow
briIntEntry=_BriIntEntry_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1))
briIntEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:briIntEntry.setStatus(_A)
_BriIntIndex_Type=Integer32
_BriIntIndex_Object=MibTableColumn
briIntIndex=_BriIntIndex_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1,1),_BriIntIndex_Type())
briIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:briIntIndex.setStatus(_A)
_BriIntBoardIndex_Type=Integer32
_BriIntBoardIndex_Object=MibTableColumn
briIntBoardIndex=_BriIntBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1,2),_BriIntBoardIndex_Type())
briIntBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:briIntBoardIndex.setStatus(_A)
_BriIntBoardPosition_Type=Integer32
_BriIntBoardPosition_Object=MibTableColumn
briIntBoardPosition=_BriIntBoardPosition_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1,3),_BriIntBoardPosition_Type())
briIntBoardPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:briIntBoardPosition.setStatus(_A)
class _BriIntMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('isdn',1),('tdm',2),('mixed',3)))
_BriIntMode_Type.__name__=_C
_BriIntMode_Object=MibTableColumn
briIntMode=_BriIntMode_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1,4),_BriIntMode_Type())
briIntMode.setMaxAccess(_B)
if mibBuilder.loadTexts:briIntMode.setStatus(_A)
_BriIntTdmChannelMap_Type=Integer32
_BriIntTdmChannelMap_Object=MibTableColumn
briIntTdmChannelMap=_BriIntTdmChannelMap_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1,5),_BriIntTdmChannelMap_Type())
briIntTdmChannelMap.setMaxAccess(_B)
if mibBuilder.loadTexts:briIntTdmChannelMap.setStatus(_A)
_BriIntIsdnChannelMap_Type=Integer32
_BriIntIsdnChannelMap_Object=MibTableColumn
briIntIsdnChannelMap=_BriIntIsdnChannelMap_Object((1,3,6,1,4,1,207,8,4,4,4,41,1,1,6),_BriIntIsdnChannelMap_Type())
briIntIsdnChannelMap.setMaxAccess(_B)
if mibBuilder.loadTexts:briIntIsdnChannelMap.setStatus(_A)
_BriChanTable_Object=MibTable
briChanTable=_BriChanTable_Object((1,3,6,1,4,1,207,8,4,4,4,41,2))
if mibBuilder.loadTexts:briChanTable.setStatus(_A)
_BriChanEntry_Object=MibTableRow
briChanEntry=_BriChanEntry_Object((1,3,6,1,4,1,207,8,4,4,4,41,2,1))
briChanEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:briChanEntry.setStatus(_A)
_BriChanIntIndex_Type=Integer32
_BriChanIntIndex_Object=MibTableColumn
briChanIntIndex=_BriChanIntIndex_Object((1,3,6,1,4,1,207,8,4,4,4,41,2,1,1),_BriChanIntIndex_Type())
briChanIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:briChanIntIndex.setStatus(_A)
class _BriChanChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_BriChanChannelIndex_Type.__name__=_C
_BriChanChannelIndex_Object=MibTableColumn
briChanChannelIndex=_BriChanChannelIndex_Object((1,3,6,1,4,1,207,8,4,4,4,41,2,1,2),_BriChanChannelIndex_Type())
briChanChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:briChanChannelIndex.setStatus(_A)
class _BriChanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('isdn',1),('tdm',2),('none',3)))
_BriChanMode_Type.__name__=_C
_BriChanMode_Object=MibTableColumn
briChanMode=_BriChanMode_Object((1,3,6,1,4,1,207,8,4,4,4,41,2,1,3),_BriChanMode_Type())
briChanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:briChanMode.setStatus(_A)
class _BriChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_BriChanState_Type.__name__=_C
_BriChanState_Object=MibTableColumn
briChanState=_BriChanState_Object((1,3,6,1,4,1,207,8,4,4,4,41,2,1,4),_BriChanState_Type())
briChanState.setMaxAccess(_B)
if mibBuilder.loadTexts:briChanState.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bri':bri,'briIntTable':briIntTable,'briIntEntry':briIntEntry,_E:briIntIndex,'briIntBoardIndex':briIntBoardIndex,'briIntBoardPosition':briIntBoardPosition,'briIntMode':briIntMode,'briIntTdmChannelMap':briIntTdmChannelMap,'briIntIsdnChannelMap':briIntIsdnChannelMap,'briChanTable':briChanTable,'briChanEntry':briChanEntry,_F:briChanIntIndex,_G:briChanChannelIndex,'briChanMode':briChanMode,'briChanState':briChanState})