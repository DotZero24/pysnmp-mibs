_G='DisplayString'
_F='xemInfoBayId'
_E='xemInfoMemberId'
_D='Unsigned32'
_C='read-only'
_B='AT-XEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
xem=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,11))
if mibBuilder.loadTexts:xem.setRevisions(('2010-09-07 00:00','2010-06-15 00:15','2009-07-15 00:00','2008-02-29 00:00'))
_XemTraps_ObjectIdentity=ObjectIdentity
xemTraps=_XemTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,11,0))
class _XemNumOfXem_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_XemNumOfXem_Type.__name__=_D
_XemNumOfXem_Object=MibScalar
xemNumOfXem=_XemNumOfXem_Object((1,3,6,1,4,1,207,8,4,4,3,11,1),_XemNumOfXem_Type())
xemNumOfXem.setMaxAccess(_C)
if mibBuilder.loadTexts:xemNumOfXem.setStatus(_A)
_XemInfoTable_Object=MibTable
xemInfoTable=_XemInfoTable_Object((1,3,6,1,4,1,207,8,4,4,3,11,2))
if mibBuilder.loadTexts:xemInfoTable.setStatus(_A)
_XemInfoEntry_Object=MibTableRow
xemInfoEntry=_XemInfoEntry_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1))
xemInfoEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:xemInfoEntry.setStatus(_A)
class _XemInfoMemberId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_XemInfoMemberId_Type.__name__=_D
_XemInfoMemberId_Object=MibTableColumn
xemInfoMemberId=_XemInfoMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,1),_XemInfoMemberId_Type())
xemInfoMemberId.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoMemberId.setStatus(_A)
class _XemInfoBayId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_XemInfoBayId_Type.__name__=_D
_XemInfoBayId_Object=MibTableColumn
xemInfoBayId=_XemInfoBayId_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,2),_XemInfoBayId_Type())
xemInfoBayId.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoBayId.setStatus(_A)
class _XemInfoXemId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_XemInfoXemId_Type.__name__=_D
_XemInfoXemId_Object=MibTableColumn
xemInfoXemId=_XemInfoXemId_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,3),_XemInfoXemId_Type())
xemInfoXemId.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoXemId.setStatus(_A)
_XemInfoBoardType_Type=DisplayString
_XemInfoBoardType_Object=MibTableColumn
xemInfoBoardType=_XemInfoBoardType_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,4),_XemInfoBoardType_Type())
xemInfoBoardType.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoBoardType.setStatus(_A)
class _XemInfoBoardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_XemInfoBoardName_Type.__name__=_G
_XemInfoBoardName_Object=MibTableColumn
xemInfoBoardName=_XemInfoBoardName_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,5),_XemInfoBoardName_Type())
xemInfoBoardName.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoBoardName.setStatus(_A)
class _XemInfoRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_XemInfoRevision_Type.__name__=_G
_XemInfoRevision_Object=MibTableColumn
xemInfoRevision=_XemInfoRevision_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,6),_XemInfoRevision_Type())
xemInfoRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoRevision.setStatus(_A)
class _XemInfoSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_XemInfoSerialNumber_Type.__name__=_G
_XemInfoSerialNumber_Object=MibTableColumn
xemInfoSerialNumber=_XemInfoSerialNumber_Object((1,3,6,1,4,1,207,8,4,4,3,11,2,1,7),_XemInfoSerialNumber_Type())
xemInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xemInfoSerialNumber.setStatus(_A)
xemInserted=NotificationType((1,3,6,1,4,1,207,8,4,4,3,11,0,1))
xemInserted.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:xemInserted.setStatus(_A)
xemRemoved=NotificationType((1,3,6,1,4,1,207,8,4,4,3,11,0,2))
xemRemoved.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:xemRemoved.setStatus(_A)
xemInsertedFail=NotificationType((1,3,6,1,4,1,207,8,4,4,3,11,0,3))
xemInsertedFail.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:xemInsertedFail.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xem':xem,'xemTraps':xemTraps,'xemInserted':xemInserted,'xemRemoved':xemRemoved,'xemInsertedFail':xemInsertedFail,'xemNumOfXem':xemNumOfXem,'xemInfoTable':xemInfoTable,'xemInfoEntry':xemInfoEntry,_E:xemInfoMemberId,_F:xemInfoBayId,'xemInfoXemId':xemInfoXemId,'xemInfoBoardType':xemInfoBoardType,'xemInfoBoardName':xemInfoBoardName,'xemInfoRevision':xemInfoRevision,'xemInfoSerialNumber':xemInfoSerialNumber})