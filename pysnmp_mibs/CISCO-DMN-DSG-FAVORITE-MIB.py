_Q='favoriteMapChPosition'
_P='favoriteMapID'
_O='read-only'
_N='favoriteListID'
_M='favorite2'
_L='favorite1'
_K='DisplayString'
_J='not-accessible'
_I='read-write'
_H='favorite6'
_G='favorite5'
_F='favorite4'
_E='favorite3'
_D='CISCO-DMN-DSG-FAVORITE-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention')
ciscoDSGFavorite=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,29))
if mibBuilder.loadTexts:ciscoDSGFavorite.setRevisions(('2010-08-30 11:00','2010-05-11 09:30','2010-04-12 06:00'))
_FavoriteCtrl_ObjectIdentity=ObjectIdentity
favoriteCtrl=_FavoriteCtrl_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,29,1))
class _FavoriteCtrlID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_E,3),(_F,4),(_G,5),(_H,6)))
_FavoriteCtrlID_Type.__name__=_B
_FavoriteCtrlID_Object=MibScalar
favoriteCtrlID=_FavoriteCtrlID_Object((1,3,6,1,4,1,1429,2,2,5,29,1,1),_FavoriteCtrlID_Type())
favoriteCtrlID.setMaxAccess(_I)
if mibBuilder.loadTexts:favoriteCtrlID.setStatus(_A)
class _FavoriteCtrlCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('writeOnly',1),('change',2)))
_FavoriteCtrlCmd_Type.__name__=_B
_FavoriteCtrlCmd_Object=MibScalar
favoriteCtrlCmd=_FavoriteCtrlCmd_Object((1,3,6,1,4,1,1429,2,2,5,29,1,2),_FavoriteCtrlCmd_Type())
favoriteCtrlCmd.setMaxAccess(_I)
if mibBuilder.loadTexts:favoriteCtrlCmd.setStatus(_A)
class _FavoriteChScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),('authorizedOnly',2)))
_FavoriteChScanMode_Type.__name__=_B
_FavoriteChScanMode_Object=MibScalar
favoriteChScanMode=_FavoriteChScanMode_Object((1,3,6,1,4,1,1429,2,2,5,29,1,3),_FavoriteChScanMode_Type())
favoriteChScanMode.setMaxAccess(_I)
if mibBuilder.loadTexts:favoriteChScanMode.setStatus(_A)
_FavoriteTable_ObjectIdentity=ObjectIdentity
favoriteTable=_FavoriteTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,29,2))
_FavoriteListTable_Object=MibTable
favoriteListTable=_FavoriteListTable_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1))
if mibBuilder.loadTexts:favoriteListTable.setStatus(_A)
_FavoriteListEntry_Object=MibTableRow
favoriteListEntry=_FavoriteListEntry_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1))
favoriteListEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:favoriteListEntry.setStatus(_A)
class _FavoriteListID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_E,3),(_F,4),(_G,5),(_H,6)))
_FavoriteListID_Type.__name__=_B
_FavoriteListID_Object=MibTableColumn
favoriteListID=_FavoriteListID_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1,1),_FavoriteListID_Type())
favoriteListID.setMaxAccess(_J)
if mibBuilder.loadTexts:favoriteListID.setStatus(_A)
class _FavoriteListPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FavoriteListPosition_Type.__name__=_B
_FavoriteListPosition_Object=MibTableColumn
favoriteListPosition=_FavoriteListPosition_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1,2),_FavoriteListPosition_Type())
favoriteListPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:favoriteListPosition.setStatus(_A)
class _FavoriteListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FavoriteListName_Type.__name__=_K
_FavoriteListName_Object=MibTableColumn
favoriteListName=_FavoriteListName_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1,3),_FavoriteListName_Type())
favoriteListName.setMaxAccess(_C)
if mibBuilder.loadTexts:favoriteListName.setStatus(_A)
class _FavoriteListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('userRadio',1),('userTv',2),('providerRadio',3),('providerTv',4)))
_FavoriteListType_Type.__name__=_B
_FavoriteListType_Object=MibTableColumn
favoriteListType=_FavoriteListType_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1,4),_FavoriteListType_Type())
favoriteListType.setMaxAccess(_O)
if mibBuilder.loadTexts:favoriteListType.setStatus(_A)
class _FavoriteListChLastViewed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FavoriteListChLastViewed_Type.__name__=_B
_FavoriteListChLastViewed_Object=MibTableColumn
favoriteListChLastViewed=_FavoriteListChLastViewed_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1,5),_FavoriteListChLastViewed_Type())
favoriteListChLastViewed.setMaxAccess(_O)
if mibBuilder.loadTexts:favoriteListChLastViewed.setStatus(_A)
_FavoriteListRowStatus_Type=RowStatus
_FavoriteListRowStatus_Object=MibTableColumn
favoriteListRowStatus=_FavoriteListRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,29,2,1,1,6),_FavoriteListRowStatus_Type())
favoriteListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:favoriteListRowStatus.setStatus(_A)
_FavoriteMapTable_Object=MibTable
favoriteMapTable=_FavoriteMapTable_Object((1,3,6,1,4,1,1429,2,2,5,29,2,2))
if mibBuilder.loadTexts:favoriteMapTable.setStatus(_A)
_FavoriteMapEntry_Object=MibTableRow
favoriteMapEntry=_FavoriteMapEntry_Object((1,3,6,1,4,1,1429,2,2,5,29,2,2,1))
favoriteMapEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:favoriteMapEntry.setStatus(_A)
class _FavoriteMapID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*((_E,3),(_F,4),(_G,5),(_H,6)))
_FavoriteMapID_Type.__name__=_B
_FavoriteMapID_Object=MibTableColumn
favoriteMapID=_FavoriteMapID_Object((1,3,6,1,4,1,1429,2,2,5,29,2,2,1,1),_FavoriteMapID_Type())
favoriteMapID.setMaxAccess(_J)
if mibBuilder.loadTexts:favoriteMapID.setStatus(_A)
class _FavoriteMapChPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,150))
_FavoriteMapChPosition_Type.__name__=_B
_FavoriteMapChPosition_Object=MibTableColumn
favoriteMapChPosition=_FavoriteMapChPosition_Object((1,3,6,1,4,1,1429,2,2,5,29,2,2,1,2),_FavoriteMapChPosition_Type())
favoriteMapChPosition.setMaxAccess(_J)
if mibBuilder.loadTexts:favoriteMapChPosition.setStatus(_A)
class _FavoriteMapChNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FavoriteMapChNum_Type.__name__=_B
_FavoriteMapChNum_Object=MibTableColumn
favoriteMapChNum=_FavoriteMapChNum_Object((1,3,6,1,4,1,1429,2,2,5,29,2,2,1,3),_FavoriteMapChNum_Type())
favoriteMapChNum.setMaxAccess(_C)
if mibBuilder.loadTexts:favoriteMapChNum.setStatus(_A)
_FavoriteMapRowStatus_Type=RowStatus
_FavoriteMapRowStatus_Object=MibTableColumn
favoriteMapRowStatus=_FavoriteMapRowStatus_Object((1,3,6,1,4,1,1429,2,2,5,29,2,2,1,4),_FavoriteMapRowStatus_Type())
favoriteMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:favoriteMapRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ciscoDSGFavorite':ciscoDSGFavorite,'favoriteCtrl':favoriteCtrl,'favoriteCtrlID':favoriteCtrlID,'favoriteCtrlCmd':favoriteCtrlCmd,'favoriteChScanMode':favoriteChScanMode,'favoriteTable':favoriteTable,'favoriteListTable':favoriteListTable,'favoriteListEntry':favoriteListEntry,_N:favoriteListID,'favoriteListPosition':favoriteListPosition,'favoriteListName':favoriteListName,'favoriteListType':favoriteListType,'favoriteListChLastViewed':favoriteListChLastViewed,'favoriteListRowStatus':favoriteListRowStatus,'favoriteMapTable':favoriteMapTable,'favoriteMapEntry':favoriteMapEntry,_P:favoriteMapID,_Q:favoriteMapChPosition,'favoriteMapChNum':favoriteMapChNum,'favoriteMapRowStatus':favoriteMapRowStatus})