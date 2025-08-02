_J='fsReportSimBillContent'
_I='fsQuerySimBillContent'
_H='accessible-for-notify'
_G='read-only'
_F='fsSimImsi'
_E='read-write'
_D='DisplayString'
_C='FS-SMM-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeStamp')
fsSmmMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,120))
if mibBuilder.loadTexts:fsSmmMIB.setRevisions(('2012-12-10 00:00',))
_FsSmmObjects_ObjectIdentity=ObjectIdentity
fsSmmObjects=_FsSmmObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,120,1))
_FsReportSimBillSwitch_Type=Unsigned32
_FsReportSimBillSwitch_Object=MibScalar
fsReportSimBillSwitch=_FsReportSimBillSwitch_Object((1,3,6,1,4,1,52642,1,1,10,2,120,1,1),_FsReportSimBillSwitch_Type())
fsReportSimBillSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:fsReportSimBillSwitch.setStatus(_A)
class _FsQuerySimBillCmd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsQuerySimBillCmd_Type.__name__=_B
_FsQuerySimBillCmd_Object=MibScalar
fsQuerySimBillCmd=_FsQuerySimBillCmd_Object((1,3,6,1,4,1,52642,1,1,10,2,120,1,2),_FsQuerySimBillCmd_Type())
fsQuerySimBillCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:fsQuerySimBillCmd.setStatus(_A)
_FsSmsUseTable_Object=MibTable
fsSmsUseTable=_FsSmsUseTable_Object((1,3,6,1,4,1,52642,1,1,10,2,120,1,3))
if mibBuilder.loadTexts:fsSmsUseTable.setStatus(_A)
_FsSmsUseEntry_Object=MibTableRow
fsSmsUseEntry=_FsSmsUseEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,120,1,3,1))
fsSmsUseEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:fsSmsUseEntry.setStatus(_A)
class _FsSimImsi_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsSimImsi_Type.__name__=_D
_FsSimImsi_Object=MibTableColumn
fsSimImsi=_FsSimImsi_Object((1,3,6,1,4,1,52642,1,1,10,2,120,1,3,1,1),_FsSimImsi_Type())
fsSimImsi.setMaxAccess(_G)
if mibBuilder.loadTexts:fsSimImsi.setStatus(_A)
_FsSmsUseCnt_Type=Unsigned32
_FsSmsUseCnt_Object=MibTableColumn
fsSmsUseCnt=_FsSmsUseCnt_Object((1,3,6,1,4,1,52642,1,1,10,2,120,1,3,1,2),_FsSmsUseCnt_Type())
fsSmsUseCnt.setMaxAccess(_G)
if mibBuilder.loadTexts:fsSmsUseCnt.setStatus(_A)
_FsSmmTrapObjects_ObjectIdentity=ObjectIdentity
fsSmmTrapObjects=_FsSmmTrapObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,120,2))
_FsSimBillTrapObjects_ObjectIdentity=ObjectIdentity
fsSimBillTrapObjects=_FsSimBillTrapObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,120,2,1))
class _FsQuerySimBillContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_FsQuerySimBillContent_Type.__name__=_B
_FsQuerySimBillContent_Object=MibScalar
fsQuerySimBillContent=_FsQuerySimBillContent_Object((1,3,6,1,4,1,52642,1,1,10,2,120,2,1,1),_FsQuerySimBillContent_Type())
fsQuerySimBillContent.setMaxAccess(_H)
if mibBuilder.loadTexts:fsQuerySimBillContent.setStatus(_A)
class _FsReportSimBillContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_FsReportSimBillContent_Type.__name__=_B
_FsReportSimBillContent_Object=MibScalar
fsReportSimBillContent=_FsReportSimBillContent_Object((1,3,6,1,4,1,52642,1,1,10,2,120,2,1,2),_FsReportSimBillContent_Type())
fsReportSimBillContent.setMaxAccess(_H)
if mibBuilder.loadTexts:fsReportSimBillContent.setStatus(_A)
_FsSmmTraps_ObjectIdentity=ObjectIdentity
fsSmmTraps=_FsSmmTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,120,3))
_FsSimBillNotifications_ObjectIdentity=ObjectIdentity
fsSimBillNotifications=_FsSimBillNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,120,3,1))
fsQuerySimBill=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,120,3,1,1))
fsQuerySimBill.setObjects((_C,_I))
if mibBuilder.loadTexts:fsQuerySimBill.setStatus(_A)
fsReportSimBill=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,120,3,1,2))
fsReportSimBill.setObjects((_C,_J))
if mibBuilder.loadTexts:fsReportSimBill.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsSmmMIB':fsSmmMIB,'fsSmmObjects':fsSmmObjects,'fsReportSimBillSwitch':fsReportSimBillSwitch,'fsQuerySimBillCmd':fsQuerySimBillCmd,'fsSmsUseTable':fsSmsUseTable,'fsSmsUseEntry':fsSmsUseEntry,_F:fsSimImsi,'fsSmsUseCnt':fsSmsUseCnt,'fsSmmTrapObjects':fsSmmTrapObjects,'fsSimBillTrapObjects':fsSimBillTrapObjects,_I:fsQuerySimBillContent,_J:fsReportSimBillContent,'fsSmmTraps':fsSmmTraps,'fsSimBillNotifications':fsSimBillNotifications,'fsQuerySimBill':fsQuerySimBill,'fsReportSimBill':fsReportSimBill})