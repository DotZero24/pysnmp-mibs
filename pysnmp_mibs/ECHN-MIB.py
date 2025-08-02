_I='nbsEthChnPossIndex'
_H='nbsEthChnPermIndex'
_G='invalid'
_F='nbsEthChnRunIndex'
_E='read-write'
_D='ECHN-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NbsEthChn_ObjectIdentity=ObjectIdentity
nbsEthChn=_NbsEthChn_ObjectIdentity((1,3,6,1,4,1,629,1,50,5))
_NbsEthChnRun_ObjectIdentity=ObjectIdentity
nbsEthChnRun=_NbsEthChnRun_ObjectIdentity((1,3,6,1,4,1,629,1,50,5,1))
_NbsEthChnRunTable_Object=MibTable
nbsEthChnRunTable=_NbsEthChnRunTable_Object((1,3,6,1,4,1,629,1,50,5,1,1))
if mibBuilder.loadTexts:nbsEthChnRunTable.setStatus(_A)
_NbsEthChnRunEntry_Object=MibTableRow
nbsEthChnRunEntry=_NbsEthChnRunEntry_Object((1,3,6,1,4,1,629,1,50,5,1,1,1))
nbsEthChnRunEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:nbsEthChnRunEntry.setStatus(_A)
_NbsEthChnRunIndex_Type=Integer32
_NbsEthChnRunIndex_Object=MibTableColumn
nbsEthChnRunIndex=_NbsEthChnRunIndex_Object((1,3,6,1,4,1,629,1,50,5,1,1,1,1),_NbsEthChnRunIndex_Type())
nbsEthChnRunIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnRunIndex.setStatus(_A)
class _NbsEthChnRunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_G,2)))
_NbsEthChnRunStatus_Type.__name__=_C
_NbsEthChnRunStatus_Object=MibTableColumn
nbsEthChnRunStatus=_NbsEthChnRunStatus_Object((1,3,6,1,4,1,629,1,50,5,1,1,1,2),_NbsEthChnRunStatus_Type())
nbsEthChnRunStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsEthChnRunStatus.setStatus(_A)
_NbsEthChnRunList_Type=OctetString
_NbsEthChnRunList_Object=MibTableColumn
nbsEthChnRunList=_NbsEthChnRunList_Object((1,3,6,1,4,1,629,1,50,5,1,1,1,3),_NbsEthChnRunList_Type())
nbsEthChnRunList.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsEthChnRunList.setStatus(_A)
_NbsEthChnRunLinkList_Type=OctetString
_NbsEthChnRunLinkList_Object=MibTableColumn
nbsEthChnRunLinkList=_NbsEthChnRunLinkList_Object((1,3,6,1,4,1,629,1,50,5,1,1,1,4),_NbsEthChnRunLinkList_Type())
nbsEthChnRunLinkList.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnRunLinkList.setStatus(_A)
_NbsEthChnPerm_ObjectIdentity=ObjectIdentity
nbsEthChnPerm=_NbsEthChnPerm_ObjectIdentity((1,3,6,1,4,1,629,1,50,5,2))
_NbsEthChnPermTable_Object=MibTable
nbsEthChnPermTable=_NbsEthChnPermTable_Object((1,3,6,1,4,1,629,1,50,5,2,1))
if mibBuilder.loadTexts:nbsEthChnPermTable.setStatus(_A)
_NbsEthChnPermEntry_Object=MibTableRow
nbsEthChnPermEntry=_NbsEthChnPermEntry_Object((1,3,6,1,4,1,629,1,50,5,2,1,1))
nbsEthChnPermEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:nbsEthChnPermEntry.setStatus(_A)
_NbsEthChnPermIndex_Type=Integer32
_NbsEthChnPermIndex_Object=MibTableColumn
nbsEthChnPermIndex=_NbsEthChnPermIndex_Object((1,3,6,1,4,1,629,1,50,5,2,1,1,1),_NbsEthChnPermIndex_Type())
nbsEthChnPermIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPermIndex.setStatus(_A)
class _NbsEthChnPermStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_G,2)))
_NbsEthChnPermStatus_Type.__name__=_C
_NbsEthChnPermStatus_Object=MibTableColumn
nbsEthChnPermStatus=_NbsEthChnPermStatus_Object((1,3,6,1,4,1,629,1,50,5,2,1,1,2),_NbsEthChnPermStatus_Type())
nbsEthChnPermStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsEthChnPermStatus.setStatus(_A)
_NbsEthChnPermList_Type=OctetString
_NbsEthChnPermList_Object=MibTableColumn
nbsEthChnPermList=_NbsEthChnPermList_Object((1,3,6,1,4,1,629,1,50,5,2,1,1,3),_NbsEthChnPermList_Type())
nbsEthChnPermList.setMaxAccess(_E)
if mibBuilder.loadTexts:nbsEthChnPermList.setStatus(_A)
_NbsEthChnPoss_ObjectIdentity=ObjectIdentity
nbsEthChnPoss=_NbsEthChnPoss_ObjectIdentity((1,3,6,1,4,1,629,1,50,5,3))
_NbsEthChnPossTable_Object=MibTable
nbsEthChnPossTable=_NbsEthChnPossTable_Object((1,3,6,1,4,1,629,1,50,5,3,1))
if mibBuilder.loadTexts:nbsEthChnPossTable.setStatus(_A)
_NbsEthChnPossEntry_Object=MibTableRow
nbsEthChnPossEntry=_NbsEthChnPossEntry_Object((1,3,6,1,4,1,629,1,50,5,3,1,1))
nbsEthChnPossEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:nbsEthChnPossEntry.setStatus(_A)
_NbsEthChnPossIndex_Type=Integer32
_NbsEthChnPossIndex_Object=MibTableColumn
nbsEthChnPossIndex=_NbsEthChnPossIndex_Object((1,3,6,1,4,1,629,1,50,5,3,1,1,1),_NbsEthChnPossIndex_Type())
nbsEthChnPossIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPossIndex.setStatus(_A)
class _NbsEthChnPossRunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_NbsEthChnPossRunStatus_Type.__name__=_C
_NbsEthChnPossRunStatus_Object=MibTableColumn
nbsEthChnPossRunStatus=_NbsEthChnPossRunStatus_Object((1,3,6,1,4,1,629,1,50,5,3,1,1,2),_NbsEthChnPossRunStatus_Type())
nbsEthChnPossRunStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPossRunStatus.setStatus(_A)
class _NbsEthChnPossPermStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_NbsEthChnPossPermStatus_Type.__name__=_C
_NbsEthChnPossPermStatus_Object=MibTableColumn
nbsEthChnPossPermStatus=_NbsEthChnPossPermStatus_Object((1,3,6,1,4,1,629,1,50,5,3,1,1,3),_NbsEthChnPossPermStatus_Type())
nbsEthChnPossPermStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPossPermStatus.setStatus(_A)
_NbsEthChnPossPortMaxNum_Type=Integer32
_NbsEthChnPossPortMaxNum_Object=MibTableColumn
nbsEthChnPossPortMaxNum=_NbsEthChnPossPortMaxNum_Object((1,3,6,1,4,1,629,1,50,5,3,1,1,4),_NbsEthChnPossPortMaxNum_Type())
nbsEthChnPossPortMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPossPortMaxNum.setStatus(_A)
_NbsEthChnPossList_Type=OctetString
_NbsEthChnPossList_Object=MibTableColumn
nbsEthChnPossList=_NbsEthChnPossList_Object((1,3,6,1,4,1,629,1,50,5,3,1,1,5),_NbsEthChnPossList_Type())
nbsEthChnPossList.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPossList.setStatus(_A)
class _NbsEthChnEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_NbsEthChnEnable_Type.__name__=_C
_NbsEthChnEnable_Object=MibScalar
nbsEthChnEnable=_NbsEthChnEnable_Object((1,3,6,1,4,1,629,1,50,5,4),_NbsEthChnEnable_Type())
nbsEthChnEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnEnable.setStatus(_A)
_NbsEthChnPossNum_Type=Integer32
_NbsEthChnPossNum_Object=MibScalar
nbsEthChnPossNum=_NbsEthChnPossNum_Object((1,3,6,1,4,1,629,1,50,5,5),_NbsEthChnPossNum_Type())
nbsEthChnPossNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPossNum.setStatus(_A)
_NbsEthChnMaxNum_Type=Integer32
_NbsEthChnMaxNum_Object=MibScalar
nbsEthChnMaxNum=_NbsEthChnMaxNum_Object((1,3,6,1,4,1,629,1,50,5,6),_NbsEthChnMaxNum_Type())
nbsEthChnMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnMaxNum.setStatus(_A)
_NbsEthChnRunNum_Type=Integer32
_NbsEthChnRunNum_Object=MibScalar
nbsEthChnRunNum=_NbsEthChnRunNum_Object((1,3,6,1,4,1,629,1,50,5,7),_NbsEthChnRunNum_Type())
nbsEthChnRunNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnRunNum.setStatus(_A)
_NbsEthChnPermNum_Type=Integer32
_NbsEthChnPermNum_Object=MibScalar
nbsEthChnPermNum=_NbsEthChnPermNum_Object((1,3,6,1,4,1,629,1,50,5,8),_NbsEthChnPermNum_Type())
nbsEthChnPermNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEthChnPermNum.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsEthChn':nbsEthChn,'nbsEthChnRun':nbsEthChnRun,'nbsEthChnRunTable':nbsEthChnRunTable,'nbsEthChnRunEntry':nbsEthChnRunEntry,_F:nbsEthChnRunIndex,'nbsEthChnRunStatus':nbsEthChnRunStatus,'nbsEthChnRunList':nbsEthChnRunList,'nbsEthChnRunLinkList':nbsEthChnRunLinkList,'nbsEthChnPerm':nbsEthChnPerm,'nbsEthChnPermTable':nbsEthChnPermTable,'nbsEthChnPermEntry':nbsEthChnPermEntry,_H:nbsEthChnPermIndex,'nbsEthChnPermStatus':nbsEthChnPermStatus,'nbsEthChnPermList':nbsEthChnPermList,'nbsEthChnPoss':nbsEthChnPoss,'nbsEthChnPossTable':nbsEthChnPossTable,'nbsEthChnPossEntry':nbsEthChnPossEntry,_I:nbsEthChnPossIndex,'nbsEthChnPossRunStatus':nbsEthChnPossRunStatus,'nbsEthChnPossPermStatus':nbsEthChnPossPermStatus,'nbsEthChnPossPortMaxNum':nbsEthChnPossPortMaxNum,'nbsEthChnPossList':nbsEthChnPossList,'nbsEthChnEnable':nbsEthChnEnable,'nbsEthChnPossNum':nbsEthChnPossNum,'nbsEthChnMaxNum':nbsEthChnMaxNum,'nbsEthChnRunNum':nbsEthChnRunNum,'nbsEthChnPermNum':nbsEthChnPermNum})